from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List, Dict, Optional, Union
from utils.engine import get_overall_score
from enum import Enum

app = FastAPI()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class Supplier(BaseModel):
    supplier_name: str = "Infosys"
    country: str = "India"
    service: str = "APAC"
    avg_cost: int = 100_000
    rating: int = 99
    avg_delivery_time: int = 240
    num_of_escalations: int = 200
    resources: int = 2000
    rank: int = 4
    year: int = 2022

class Criteria(Enum):
    gte = '>='
    gt = '>'
    lte = '<='
    lt = '<'
    equal = '=='

class Objective(Enum):
    max = "Maximize"
    min = "Minimize"

class FilterKeys(BaseModel):
    criteria: Criteria = "=="
    value: Union[int, str]

class Filter(BaseModel):
    country: FilterKeys
    service: FilterKeys
    avg_cost: FilterKeys
    rating: FilterKeys
    avg_delivery_time: FilterKeys
    num_of_escalations: FilterKeys
    resources: FilterKeys
    rank: FilterKeys
    year: FilterKeys

class AttributeKeys(BaseModel):
    objective: Objective = "Minimize"
    weightage: int = 20
    tends_to_value: int = 1

class Attribute(BaseModel):
    avg_cost: AttributeKeys
    rating: AttributeKeys
    avg_delivery_time: AttributeKeys
    num_of_escalations: AttributeKeys
    resources: AttributeKeys
    rank: AttributeKeys

class SupplierData(BaseModel):
    suppliers: List[Supplier]
    filters: Filter
    attributes: Attribute

# @app.post("/token")
# async def token(form_data: OAuth2PasswordRequestForm = Depends()):
#     return {
#         "access_token": form_data.username
#     }

# @app.get("/")
# async def getAllSuppliers(page):
#     pass

@app.post("/process")
async def process(data: SupplierData) -> Dict:
    score, message = get_overall_score(data.suppliers, data.filters, data.attributes)
    return {
        "message": message,
        "score": score
    }
