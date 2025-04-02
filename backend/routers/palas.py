from fastapi import APIRouter
from typing import List
from crud import get_all_palas
from models import Pala

router = APIRouter()

@router.get("/", response_model=List[Pala])
def listar_palas():
    return get_all_palas()
