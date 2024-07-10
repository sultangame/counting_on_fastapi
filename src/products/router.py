from typing import List, Annotated
from fastapi import APIRouter, Depends, status
from . import crud, schemas, models


products_router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@products_router.get(
    "/get/all/products/",
    response_model=List[schemas.ProductsRead],
    status_code=status.HTTP_200_OK
)
async def get_all_products(
        service: Annotated[crud.ProductsService, Depends(crud.product_service)]
) -> List[schemas.ProductsRead]:
    answer = await service.find_all()
    return answer


@products_router.get(
    "/get/one/product/{pk}/",
    response_model=schemas.ProductsRead,
    status_code=status.HTTP_200_OK
)
async def get_all_products(
        pk: int,
        service: Annotated[crud.ProductsService, Depends(crud.product_service)]
) -> schemas.ProductsRead:
    answer = await service.find_one(pk=pk)
    return answer


@products_router.get(
    "/get/all/products/filtered/",
    response_model=List[schemas.ProductsRead],
    status_code=status.HTTP_200_OK
)
async def get_all_filtered_products(
        name: str,
        service: Annotated[crud.ProductsService, Depends(crud.product_service)]
) -> List[schemas.ProductsRead]:
    answer = await service.find_one_filtered(search=name, column=models.ProductsORM.name)
    return answer


@products_router.post(
    path="/add/one/product/",
    response_model=schemas.ProductsCreate,
    status_code=status.HTTP_201_CREATED
)
async def add_product(
        schema: schemas.ProductsCreate,
        service: Annotated[crud.ProductsService, Depends(crud.product_service)]
) -> schemas.ProductsCreate:
    answer = await service.add_one(schemas=schema)
    return answer


@products_router.patch(
    path="/update/one/product/{pk}/",
    response_model=schemas.ProductsRead,
)
async def edit_product(
        pk: int,
        schema: schemas.ProductsEdit,
        service: Annotated[crud.ProductsService, Depends(crud.product_service)]
) -> schemas.ProductsRead:
    answer = await service.edit_one(pk=pk, schemas=schema)
    return answer


@products_router.delete(
    path="/delete/one/product/{pk}/",
)
async def delete_product(
        pk: int,
        service: Annotated[crud.ProductsService, Depends(crud.product_service)]
):
    answer = await service.delete_one(pk=pk)
    return answer
