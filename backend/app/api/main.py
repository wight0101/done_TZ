from fastapi import APIRouter

from app.api.routes import get_all_poducts, get_product_name, get_product_name_field

api_router = APIRouter()
api_router.include_router(get_all_poducts.router, tags=["get_all_products"])
api_router.include_router(get_product_name.router, tags=["get_product_name"])
api_router.include_router(get_product_name_field.router, tags=["get_product_name_field"])