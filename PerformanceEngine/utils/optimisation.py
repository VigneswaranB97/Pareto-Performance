import logging

from .constants import moo_all_objectives, moo_score
from .multi_objective_optimisation import moo_set, score
import pandas as pd

def get_moo_scores(data, all_objectives):
    suppliers = pd.DataFrame(data)
    mask = moo_set(suppliers, all_objectives=all_objectives)
    return suppliers[mask].index.to_list()

def moo_run_combination(comb, supplier_data, attributes, overall_scores):
    logging.info(f"Running {comb} for Multi-Objective-Optimisation")
    data = {}
    all_objectives = []
    total_weightage = 0
    for attribute in comb:
        data[attribute] = []
        for supplier in supplier_data:
            data[attribute].append(supplier[attribute])
        all_objectives.append(moo_all_objectives[attributes[attribute]["Objective"]])
        total_weightage += attributes[attribute]["Weightage"]

    scores = get_moo_scores(data, all_objectives)
    for i in scores:
        overall_scores[i] += moo_score * (total_weightage if total_weightage != 0 else 1)

# hotels = pd.DataFrame({"price": [50, 53, 62, 87, 83, 39, 60, 44],
#                        "distance_to_beach": [13, 21, 19, 13, 5, 22, 22, 25],
#                        })
# mask = score(hotels, sense=["min", "max"])
# print(mask)
# paretoset_hotels = hotels[mask]
# print(paretoset_hotels)
