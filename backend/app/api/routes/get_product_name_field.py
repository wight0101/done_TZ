from fastapi import APIRouter, HTTPException
from app.data import sample_data


router = APIRouter()


@router.get("/products/{product_name}/{product_field}")
async def get_product_field(product_name: str, product_field: str):
    if product_name in sample_data:
        product = sample_data[product_name]
        if product_field in product:
            return {product_field: product[product_field]}
        else:
            raise HTTPException(status_code=404, detail="Product field not found")
    else:
        raise HTTPException(status_code=404, detail="Product not found")
    