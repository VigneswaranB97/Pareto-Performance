from .multi_objective_optimisation import moo_set, score
import pandas as pd

def get_moo_scores(data, all_objectives):
    suppliers = pd.DataFrame(data)
    mask = moo_set(suppliers, all_objectives=all_objectives)
    return suppliers[mask].index.to_list()

# hotels = pd.DataFrame({"price": [50, 53, 62, 87, 83, 39, 60, 44],
#                        "distance_to_beach": [13, 21, 19, 13, 5, 22, 22, 25],
#                        })
# mask = score(hotels, sense=["min", "max"])
# print(mask)
# paretoset_hotels = hotels[mask]
# print(paretoset_hotels)
