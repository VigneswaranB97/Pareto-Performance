from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Dict, Optional
from utils.engine import get_overall_score

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class SupplierData(BaseModel):
    suppliers: List
    filters: Dict
    attributes: Dict


@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {
        "access_token": form_data.username
    }

@app.get("/")
async def getAllSuppliers(page):
    pass

@app.post("/process")
async def process(data: SupplierData) -> Dict:
    score, message = get_overall_score(data.suppliers, data.filters, data.attributes)
    return {
        "message": message,
        "score": score
    }
