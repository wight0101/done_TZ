from fastapi import APIRouter, HTTPException
from app.data import sample_data


router = APIRouter()


@router.get("/products/{product_name}")
async def get_product(product_name: str):
    if product_name in sample_data:
        return sample_data[product_name]
    else:
        raise HTTPException(status_code=404, detail="Product not found")
