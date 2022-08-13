import numpy as np
import pandas as pd

from .validation import validate_inputs


def moo_set_efficient(functions, distinct=True):
    functions = functions.copy()  # The algorithm mutates the `functions` variable, so we take a copy
    n_functions, n_objectives = functions.shape
    is_efficient = np.arange(n_functions)
    next_point_index = 0  # Next index in the is_efficient array to search for
    while next_point_index < len(functions):
        this_cost = functions[next_point_index]

        # Two points `a` and `b` are *incomparable* if neither dom(a, b) nor dom(b, a).
        # Points that are incomparable to `this_cost`, or dominate `this_cost`.
        # In 2D, these points are below or to the left of `this_cost`.
        current_efficient_points = np.any(functions < this_cost, axis=1)

        # If we're not looking for distinct, keep points equal to this cost
        if not distinct:
            no_smaller = np.logical_not(current_efficient_points)
            equal_to_this_cost = np.all(functions[no_smaller] == this_cost, axis=1)
            current_efficient_points[no_smaller] = np.logical_or(
                current_efficient_points[no_smaller], equal_to_this_cost
            )

        # Any point is incomparable to itself, so keep this point
        current_efficient_points[next_point_index] = True

        # Remove dominated points
        is_efficient = is_efficient[current_efficient_points]
        functions = functions[current_efficient_points]

        # Re-adjust the index
        next_point_index = np.sum(current_efficient_points[:next_point_index]) + 1

    # Create a boolean mask from indices and return it
    is_efficient_mask = np.zeros(n_functions, dtype=np.bool_)
    is_efficient_mask[is_efficient] = True
    return is_efficient_mask


def moo_set(functions, all_objectives=None, distinct=True):
    moo_set_algorithm = moo_set_efficient

    functions, all_objectives = validate_inputs(functions=functions, all_objectives=all_objectives)
    assert isinstance(all_objectives, list)

    n_functions, n_objectives = functions.shape

    diff_cols = [i for i in range(n_objectives) if all_objectives[i] == "diff"]
    max_cols = [i for i in range(n_objectives) if all_objectives[i] == "max"]
    min_cols = [i for i in range(n_objectives) if all_objectives[i] == "min"]

    # Check data types (MIN and MAX must be numerical)
    message = "Data must be numerical. Please convert it. Data has type: {}"

    if isinstance(functions, pd.DataFrame):
        data_types = [functions.dtypes.values[i] for i in (max_cols + min_cols)]
        if any(d == np.dtype("O") for d in data_types):
            raise TypeError(message.format(data_types))

    else:
        if functions.dtype == np.dtype("O"):
            raise TypeError(message.format(functions.dtype))

    # No diff columns, use numpy array
    if not diff_cols:
        if isinstance(functions, pd.DataFrame):
            functions = functions.to_numpy(copy=True)
        for col in max_cols:
            functions[:, col] = -functions[:, col]
        return moo_set_algorithm(functions, distinct=distinct)

    n_functions, n_objectives = functions.shape

    # Diff columns are present, use pandas dataframe
    if isinstance(functions, pd.DataFrame):
        df = functions.copy()  # Copy to avoid mutating inputs
        df.columns = np.arange(n_objectives)
    else:
        df = pd.DataFrame(functions)

    assert isinstance(df, pd.DataFrame)
    assert np.all(df.columns == np.arange(n_objectives))

    # If `object` columns are present, and they can be converted, do it.
    for col in max_cols:
        df[col] = -pd.to_numeric(df[col], errors="coerce")
    for col in min_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    is_efficient = np.zeros(n_functions, dtype=np.bool_)

    # Create the groupby object
    # We could've implemented our own groupby, but choose to use pandas since
    # it's likely better than what we can come up with on our own.
    groupby = df.groupby(diff_cols)

    # Iteration through the groups
    for key, data in groupby:
        # Get the relevant data for the group and compute the efficient points
        relevant_data = data[max_cols + min_cols].to_numpy(copy=True)
        efficient_mask = moo_set_algorithm(relevant_data.copy(), distinct=distinct)

        # The `pd.DataFrame.groupby.indices` dict holds the row indices of the group
        data_mask = groupby.indices[key]
        is_efficient[data_mask] = efficient_mask

    return is_efficient


def score(functions, distinct=True):
    n_functions, n_objectives = functions.shape
    scores = np.zeros(n_functions, dtype=np.int_)
    remaining = np.ones(n_functions, dtype=np.bool_)
    processed = np.zeros(n_functions, dtype=np.bool_)

    current_score = 1
    while np.sum(remaining) > 0:
        frontier_mask = moo_set(functions[remaining], distinct=distinct)
        processed[np.logical_not(processed)] = frontier_mask
        scores[np.logical_and(processed, remaining)] = current_score
        remaining[remaining] = np.logical_not(frontier_mask)
        current_score += 1

    max_score = max(scores)
    return [max_score - r + 1 for r in scores]


def get_moo__score(functions, all_objectives=None, distinct=True):
    moo_score_algorithm = score

    functions, all_objectives = validate_inputs(functions=functions, all_objectives=all_objectives)
    assert isinstance(all_objectives, list)

    n_functions, n_objectives = functions.shape

    diff_cols = [i for i in range(n_objectives) if all_objectives[i] == "diff"]
    max_cols = [i for i in range(n_objectives) if all_objectives[i] == "max"]
    min_cols = [i for i in range(n_objectives) if all_objectives[i] == "min"]

    # Check data types (MIN and MAX must be numerical)
    message = "Data must be numerical. Please convert it. Data has type: {}"

    if isinstance(functions, pd.DataFrame):
        data_types = [functions.dtypes.values[i] for i in (max_cols + min_cols)]
        if any(d == np.dtype("O") for d in data_types):
            raise TypeError(message.format(data_types))

    else:
        if functions.dtype == np.dtype("O"):
            raise TypeError(message.format(functions.dtype))

    # CASE 1: THE ONLY all_objectives IS MINIMIZATION
    # ---------------------------------------
    if all(s == "min" for s in all_objectives):
        if isinstance(functions, pd.DataFrame):
            functions = functions.to_numpy(copy=True)
        return moo_score_algorithm(functions, distinct=distinct)

    n_functions, n_objectives = functions.shape

    if not diff_cols:
        # It's an array
        if not isinstance(functions, np.ndarray):
            functions = functions.to_numpy(copy=True)
        for col in max_cols:
            functions[:, col] = -functions[:, col]

        return moo_score_algorithm(functions, distinct=distinct)

    if isinstance(functions, pd.DataFrame):
        df = functions.copy()  # Copy to avoid mutating inputs
        df.columns = np.arange(n_objectives)
    else:
        df = pd.DataFrame(functions)

    assert isinstance(df, pd.DataFrame)
    assert np.all(df.columns == np.arange(n_objectives))

    # If `object` columns are present, and they can be converted, do it.
    for col in max_cols + min_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    all_scores = np.zeros(n_functions, dtype=np.int_)

    # Create the groupby object
    # We could've implemented our own groupby, but choose to use pandas since
    # it's likely better than what we can come up with on our own.
    groupby = df.groupby(diff_cols)

    # Iteration through the groups
    for key, data in groupby:
        # Get the relevant data for the group and compute the efficient points
        relevant_data = data[max_cols + min_cols].to_numpy(copy=True)
        scores = moo_score_algorithm(relevant_data.copy(), distinct=distinct)

        # The `pd.DataFrame.groupby.indices` dict holds the row indices of the group
        data_mask = groupby.indices[key]
        all_scores[data_mask] = scores

    return all_scores
