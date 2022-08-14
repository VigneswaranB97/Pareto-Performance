import json
import logging
from utils.engine import get_overall_score

_filters = {
      "service": {
          "criteria": "==",
          "value": "Applications Development"
      }
   }
_attributes = {
    "rating": {
        "objective": "Maximize",
        "weightage": 50,
        "tends_to_value": 100,
    },
    "resources": {
        "objective": "Minimize",
        "weightage": 8,
        "tends_to_value": 1,
    },
    "avg_cost": {
        "objective": "Minimize",
        "weightage": 20,
        "tends_to_value": 1,
    },
    "avg_delivery_time": {
        "objective": "Minimize",
        "weightage": 10,
        "tends_to_value": 1,
    },
    "num_of_escalations": {
        "objective": "Minimize",
        "weightage": 12,
        "tends_to_value": 1,
    }
}
_json_data_path = f'sample_data/all_suppliers.json'

def run_test(filters, attributes, json_data_path):
    with open(json_data_path, 'r') as f:
        logging.info("Getting data...")
        supplier_data = json.load(f)
        logging.info("Starting to Process...")
        print(get_overall_score(supplier_data, filters, attributes))


if __name__ == "__main__":
    run_test(_filters, _attributes, _json_data_path)

# pareToTest1759

# mongoimport --host ac-czsi2w9-shard-00-02.lkpj03b.mongodb.net:27017 --db supliers --type json --file "/Users/vigneswaran/Projects/sirion/SupplierPerformance/sample_data/all_suppliers.json" --jsonArray --authenticationDatabase admin --ssl --username VigneswaranB97 --password pareToTest1759