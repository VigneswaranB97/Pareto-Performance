# Pareto-Performance

Selecting a supplier from among thousands and doing a predictive performance analysis is a challenge which most of the client's face. Evaluating supplier performance based on multiple attributes would not only help clients mitigate risk but also help reduce costs. 

## Technologies
Project is created with:
* Python 3.6+
* Pandas
* Numpy
* Linear Programming
* Operational research

## Installation Procedure
Download Submitted zip file or clone the repo
```
$ cd PerformanceEngine
$ mkdir sample_data
$ pip3 install -r requirements.txt
$ python3 data_generator.py
$ python3 run.py
```

## To run FastAPI Server
```
$ cd PerformanceEngine
$ pip3 install -r requirements.txt
$ uvicorn index:app --reload
```

### Request Example

`POST /process/`

```
$ curl --location --request POST 'http://localhost:8000/process' \
--header 'Content-Type: application/json' \
--data-raw '{
    "suppliers": [
        {
            "Supplier Name": "TCS elastic_franklin",
            "Country": "Algeria",
            "Service": "Applications Development",
            "Avg. Cost($)": 143601,
            "Rating": 80,
            "Average Delivery Time": 151,
            "Number of Escalations": 308,
            "Year": 2021,
            "Resources": 6064,
            "Rank": "1"
        },
        {
            "Supplier Name": "TCS vigorous_bhabha",
            "Country": "Algeria",
            "Service": "Applications Maintenance",
            "Avg. Cost($)": 256872,
            "Rating": 92,
            "Average Delivery Time": 231,
            "Number of Escalations": 129,
            "Year": 2020,
            "Resources": 6361,
            "Rank": "1"
        },
        {
            "Supplier Name": "TCS zen_lalande",
            "Country": "Algeria",
            "Service": "Mainframe services",
            "Avg. Cost($)": 280612,
            "Rating": 95,
            "Average Delivery Time": 292,
            "Number of Escalations": 411,
            "Year": 2016,
            "Resources": 789,
            "Rank": "1"
        }
    ],
    "filters": {
        "Service": {
            "criteria": "==",
            "value": "Applications Development"
        },
        "Average Delivery Time": {
            "criteria": "<=",
            "value": 100
        }
    },
    "attributes": {
        "Rating": {
            "objective": "Maximize",
            "weightage": 20,
            "tends_to_value": 100
        },
        "Resources": {
            "objective": "Minimize",
            "weightage": 20,
            "tends_to_value": 1
        },
        "Avg. Cost($)": {
            "objective": "Minimize",
            "weightage": 20,
            "tends_to_value": 1
        },
        "Average Delivery Time": {
            "objective": "Minimize",
            "weightage": 20,
            "tends_to_value": 1
        },
        "Number of Escalations": {
            "objective": "Minimize",
            "weightage": 20,
            "tends_to_value": 1
        }
    }
}'
```

### Response
```
{
    "message": "No Supplier found with value 100 for Average Delivery Time, So Ignoring Average Delivery Time! 1 Suppliers Found after filtration! Recommending {'Supplier Name': 'TCS elastic_franklin', 'Country': 'Algeria', 'Service': 'Applications Development', 'Avg. Cost($)': 143601, 'Rating': 80, 'Average Delivery Time': 151, 'Number of Escalations': 308, 'Year': 2021, 'Resources': 6064, 'Rank': '1', 'score': 6900, 'id': 'supplier_0'}",
    "score": [
        {
            "Supplier Name": "TCS elastic_franklin",
            "Country": "Algeria",
            "Service": "Applications Development",
            "Avg. Cost($)": 143601,
            "Rating": 80,
            "Average Delivery Time": 151,
            "Number of Escalations": 308,
            "Year": 2021,
            "Resources": 6064,
            "Rank": "1",
            "score": 6900,
            "id": "supplier_0"
        }
    ]
}
```
