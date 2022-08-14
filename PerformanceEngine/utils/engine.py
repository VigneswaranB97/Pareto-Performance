import copy
import json
from itertools import chain, combinations
import time
import logging
import multiprocessing

from .lp_helper import get_linear_programming_scores
from .optimisation import moo_run_combination
from .constants import moo_all_objectives, moo_score

logging.basicConfig(filename='all_logs.log', format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(2, len(ss)+1)))

def update_weightage(attributes, prioritize=True):
    num_attributes = len(attributes)
    if not prioritize:
        for attr in attributes:
            attributes[attr]['weightage'] = 100 / num_attributes
    else:
        # weightages = {k: v['weightage'] for k, v in attributes.items()}
        attr_tuple = sorted(attributes.items(), key=lambda i: i[1]['weightage'])
        start_weightage = 50 / num_attributes
        diff = 25 / num_attributes
        for idx, attr in enumerate(attr_tuple):
            attributes[attr[0]]['weightage'] = start_weightage + (diff * idx)

    logging.info("Attributes after readjusting {}".format(attributes))

def get_overall_score(supplier_data, filters, attributes):
    sum_weightage = 0
    message = ""
    for attr, val in attributes.items():
        if "weightage" not in val:
            sum_weightage = 0
            break
        sum_weightage += val["weightage"]

    if sum_weightage == 0:
        msg = "Weightage is Equally re-adjusted. "
        logging.info(msg)
        message += msg
        update_weightage(attributes, prioritize=False)
    elif sum_weightage != 100:
        msg = "Total Weightage Not equal to 100. So weightage re-adjusted based on the input. "
        logging.info(msg)
        message += msg
        update_weightage(attributes, prioritize=True)

    before_filter = copy.deepcopy(supplier_data)
    for f in filters:
        start = time.time()
        logging.info("Filtering {} in progress...".format(f))
        if filters[f]["criteria"] == ">=":
            current_filter = [i for i in supplier_data if filters[f]["value"] >= i[f]]
            if len(current_filter) == 0:
                message += "No Supplier found with value {} for {}, So Ignoring {}! ".format(filters[f]["value"], f, f)
            else:
                supplier_data = current_filter
        elif filters[f]["criteria"] == "<=":
            current_filter = [i for i in supplier_data if i[f] <= filters[f]["value"]]
            if len(current_filter) == 0:
                message += "No Supplier found with value {} for {}, So Ignoring {}! ".format(filters[f]["value"], f, f)
            else:
                supplier_data = current_filter
        elif filters[f]["criteria"] == ">":
            current_filter = [i for i in supplier_data if i[f] > filters[f]["value"]]
            if len(current_filter) == 0:
                message += "No Supplier found with value {} for {}, So Ignoring {}! ".format(filters[f]["value"], f, f)
            else:
                supplier_data = current_filter
        elif filters[f]["criteria"] == "<":
            current_filter = [i for i in supplier_data if i[f] < filters[f]["value"]]
            if len(current_filter) == 0:
                message += "No Supplier found with value {} for {}, So Ignoring {}! ".format(filters[f]["value"], f, f)
            else:
                supplier_data = current_filter
        else:
            current_filter = [i for i in supplier_data if i[f] == filters[f]["value"]]
            if len(current_filter) == 0:
                message += "No Supplier found with value {} for {}, So Ignoring {}! ".format(filters[f]["value"], f, f)
            else:
                supplier_data = current_filter
        end = time.time()
        logging.info("Filtering {} completed in {}".format(f, end - start))

    message += "{} Suppliers Found after filtration! ".format(len(supplier_data))
    manager = multiprocessing.Manager()
    overall_scores = manager.dict()

    if not supplier_data:
        supplier_data = copy.deepcopy(before_filter)

    for idx, supplier in enumerate(supplier_data):
        supplier['score'] = 0
        supplier['id'] = "supplier_{}".format(idx)
        overall_scores[idx] = 0

    logging.info(f"Total Competing Suppliers: {len(supplier_data)}")

    moo_start = time.time()
    # Get Scores using moo logic
    logging.info(f"Running moo logic")
    all_combinations = all_subsets(attributes)

    processes = []
    for comb in all_combinations:
        logging.info(f"Starting {comb} for Multi-Objective-Optimisation")
        p = multiprocessing.Process(target=moo_run_combination, args=(comb, supplier_data, attributes, overall_scores,))
        # moo_run_combination(comb, supplier_data, attributes, overall_scores)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    moo_end = time.time()
    logging.info(f"moo Completed in {int(moo_end - moo_start)} seconds")

    # lp_start = time.time()
    # Get Scores using Linear Programming
    # logging.info(f"Running LP logic")
    # all_lp_process = []
    # for key, value in attributes.items():
    #     logging.info(f"Running {key} attribute for LP logic")
    #     suppliers = []
    #     all_constants = {}
    #     for i in supplier_data:
    #         suppliers.append(i["id"])
    #         all_constants[i["id"]] = int(i[key])
    #
    #     p = multiprocessing.Process(target=get_linear_programming_scores, args=(suppliers, all_constants, value["objective"], value["tends_to_value"], attributes, overall_scores, key))  # get_linear_programming_scores(suppliers, all_constants, value["Objective"], value["tends_to_value"], attributes, overall_scores, attribute=key)
    #     p.start()
    #     all_lp_process.append(p)
    #
    # for p in all_lp_process:
    #     p.join()
    #
    # lp_end = time.time()
    # logging.info(f"LP Completed in {int(lp_end - lp_start)} seconds")

    sorted_suppliers = sorted(list(overall_scores.items()), key=lambda i: i[1], reverse=True)
    all_non_zero_scorers = []
    for sup in sorted_suppliers:
        idx, score = sup
        if score == 0:
            break
        supplier_data[idx]["score"] = score
        all_non_zero_scorers.append(supplier_data[idx])

    if len(all_non_zero_scorers) > 0:
        message += "Recommending {}".format(all_non_zero_scorers[0])
    return all_non_zero_scorers, message

# get_overall_score(filters, attributes)

#
# attribute_wise_score = {}
#

# # logging.info(get_optimal_supplier(sample_data, attributes))
