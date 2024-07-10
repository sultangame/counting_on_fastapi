from .category.router import category_router
from .products.router import products_router
from .sold_products.router import sold_products_router
from fastapi import APIRouter


api_v1 = APIRouter(
    prefix="/api/v1",
)
api_v1.include_router(category_router)
api_v1.include_router(products_router)
api_v1.include_router(sold_products_router)
