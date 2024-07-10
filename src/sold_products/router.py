from fastapi import APIRouter, Depends, status
from typing import Annotated, List
from . import schemas, crud
from ..products.crud import ProductsService, product_service

sold_products_router = APIRouter(
    prefix="/sold_products",
    tags=["sold_products"],
)


@sold_products_router.get(
    path="/get/all/sold/products/",
    response_model=List[schemas.SoldProductsRead],
)
async def get_sold_products(
        service: Annotated[crud.SoldProductsService, Depends(crud.sold_products_service)]
):
    answer = await service.find_all()
    return answer


@sold_products_router.get(
    path="/get/one/sold/product/{pk}/",
    response_model=schemas.SoldProductsRead
)
async def get_one_sold_product(
        pk: int,
        service: Annotated[crud.SoldProductsService, Depends(crud.sold_products_service)]
):
    answer = await service.find_one(pk=pk)
    return answer


@sold_products_router.post(
    path="/create/sold/product/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.SoldProductsCreate,
)
async def create_sold_product(
        name_of_products: str,
        schema: schemas.SoldProductsCreate,
        service: Annotated[crud.SoldProductsService, Depends(crud.sold_products_service)],
        products: Annotated[ProductsService, Depends(product_service)]
):
    answer = await service.add_one_with_rel(
        schema=schema,
        product_name=name_of_products,
        service=products
    )
    return answer


@sold_products_router.patch(
    path="/update/sold/product/{pk}/",
    status_code=status.HTTP_200_OK,
    response_model=schemas.SoldProductsRead,
)
async def update_sold_product(
        pk: int,
        schema: schemas.SoldProductsUpdate,
        service: Annotated[crud.SoldProductsService, Depends(crud.sold_products_service)]
):
    answer = await service.edit_one(pk=pk, schemas=schema)
    return answer


@sold_products_router.delete("/delete/one/sold/product/{pk}")
async def delete_one_product(
        pk: int,
        service: Annotated[crud.SoldProductsService, Depends(crud.sold_products_service)]
):
    answer = await service.delete_one(pk=pk)
    return answer
