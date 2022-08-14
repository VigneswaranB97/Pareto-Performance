import logging
from paretoset import paretoset
from .constants import moo_all_objectives, moo_score
from .multi_objective_optimisation import moo_set, score
import pandas as pd

def get_moo_scores(data, all_objectives):
    suppliers = pd.DataFrame(data)
    mask = moo_set(suppliers, all_objectives=all_objectives)
    return suppliers[mask].index.to_list()

def get_avg_weightage(supplier, attributes, comb):
    data = {k: attributes[k]["weightage"] for k, v in supplier.items() if k in comb}
    return sum(data.values()) / len(data)

def get_max_weightage(supplier, attributes, comb):
    data = {k: attributes[k]["weightage"] for k, v in supplier.items() if k in comb}
    max_attribute = max(data, key=data.get)
    return data[max_attribute]

def moo_run_combination(comb, supplier_data, attributes, overall_scores):
    logging.info(f"Running {comb} for Multi-Objective-Optimisation")
    data = {}
    all_objectives = []
    for attribute in comb:
        data[attribute] = []
        for supplier in supplier_data:
            data[attribute].append(supplier[attribute])
        all_objectives.append(moo_all_objectives[attributes[attribute]["objective"]])

    scores = get_moo_scores(data, all_objectives)
    for i in scores:
        weightage = get_max_weightage(supplier_data[i], attributes, comb)
        overall_scores[i] += moo_score * (weightage if weightage != 0 else 1)
