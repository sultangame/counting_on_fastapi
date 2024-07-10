from fastapi import APIRouter, Depends, status
from typing import Annotated, List
from . import schemas, crud, models

category_router = APIRouter(
    prefix="/category",
    tags=["category"]
)


@category_router.get(
    path="/get/all/categories",
    response_model=List[schemas.CategoryRead],
    status_code=status.HTTP_200_OK
)
async def get_all_categories(
        service: Annotated[crud.CategoryService, Depends(crud.category_service)]
) -> List[schemas.CategoryRead]:
    answer = await service.find_all()
    return answer


@category_router.get(
    path="/get/category/{pk}",
    response_model=schemas.CategoryRead,
    status_code=status.HTTP_200_OK
)
async def get_one_category(
        pk: int,
        service: Annotated[crud.CategoryService, Depends(crud.category_service)],
) -> schemas.CategoryRead:
    answer = await service.find_one(pk=pk)
    return answer


@category_router.get(
    path="/get/one/category/filtered/{category}",
    response_model=List[schemas.CategoryRead],
    status_code=status.HTTP_200_OK
)
async def get_one_category_filtered(
        category: str,
        service: Annotated[crud.CategoryService, Depends(crud.category_service)],
) -> List[schemas.CategoryRead]:
    answer = await service.find_one_filtered(search=category, column=models.CategoryORM.category)
    return answer


@category_router.post(
    path="/add/one/category/",
    response_model=schemas.CategoryCreate,
    status_code=status.HTTP_201_CREATED
)
async def add_one_category(
        schema: schemas.CategoryCreate,
        service: Annotated[crud.CategoryService, Depends(crud.category_service)],
) -> schemas.CategoryCreate:
    answer = await service.add_one(schemas=schema)
    return answer


@category_router.patch(
    path="/edit/one/category/{pk}",
    response_model=schemas.CategoryRead,
    status_code=status.HTTP_200_OK
)
async def edit_one_category(
        pk: int,
        schema: schemas.CategoryEdit,
        service: Annotated[crud.CategoryService, Depends(crud.category_service)],
):
    answer = await service.edit_one(pk=pk, schemas=schema)
    return answer


@category_router.delete(
    path="/delete/one/category/{pk}",
    status_code=status.HTTP_200_OK
)
async def delete_one_category(
        pk: int,
        service: Annotated[crud.CategoryService, Depends(crud.category_service)],
):
    answer = await service.delete_one(pk=pk)
    return answer
