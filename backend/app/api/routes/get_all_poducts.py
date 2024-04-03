from fastapi import APIRouter

router = APIRouter()
from app.data import sample_data

@router.get("/all_products/")
async def get_all_products():
    return sample_data