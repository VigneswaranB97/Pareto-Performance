import collections.abc

import numpy as np


def validation(functions, all_objectives):
    n_functions, n_objectives = functions.shape
    if all_objectives is None:
        return functions, ["min"] * n_objectives
    else:
        all_objectives = list(all_objectives)
    if not isinstance(all_objectives, collections.abc.Sequence):
        raise TypeError("`all_objectives` parameter must be a sequence (e.g. list).")

    if not len(all_objectives) == n_objectives:
        raise ValueError("Length of `all_objectives` must match second dimensions (i.e. columns).")

    all_objectives = [s.__name__ if callable(s) else s for s in all_objectives]
    if not all(isinstance(s, str) for s in all_objectives):
        raise TypeError("`all_objectives` parameter must be a sequence of strings.")
    all_objectives = [s.lower() for s in all_objectives]
    all_objectives_map = {
        "min": "min",
        "minimum": "min",
        "max": "max",
        "maximum": "max",
        "diff": "diff",
        "different": "diff"
    }
    all_objectives = [all_objectives_map.get(s) for s in all_objectives]
    valid = ["min", "max", "diff"]
    if not all(s in valid for s in all_objectives):
        raise TypeError("`all_objectives` must be one of: {}".format(valid))

    return functions, all_objectives


def validate_inputs(functions, all_objectives=None):
    return validation(np.asarray(functions), all_objectives=all_objectives)