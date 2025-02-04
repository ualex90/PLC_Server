import json
from fastapi import APIRouter

from core.models.base import Data


router = APIRouter(prefix="/criptosem", tags=["criptosem"])

# @router.post()
# def load_data(data: Data):
#     return Data.data

@router.post("/data")
def list_items(data: Data):
    print(data.data)
    return data
    