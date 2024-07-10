from typing import Annotated

from src.products.crud import product_service, ProductsService
from src.products import ProductsORM
from src.utils import AbstractService, SQLAlchemyRepository
from . import schemas
from .models import SoldProductsORM
from fastapi import Depends, HTTPException, status


class ProductsSoldRepository(SQLAlchemyRepository):
    model = SoldProductsORM


class SoldProductsService(AbstractService):
    model = SoldProductsORM
    joins = [SoldProductsORM.products]

    async def add_one_with_rel(
            self,
            schema: schemas.SoldProductsCreate,
            product_name: str,
            service: Annotated[ProductsService, Depends(product_service)]
    ):
        exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Couldn't add it because we don't have enough products"
        )
        product: ProductsORM = await service.find_by_name(name=product_name)
        data = schema.model_dump()
        if product.count > 0:
            new_count = product.count - data.get("count")
            if new_count < 0:
                raise exception
            await service.edit_count(name=product_name, new_count=new_count)
            sold_product = self.model(**data)
            sold_product.products.append(product)
            answer = await self.repository.add_one(data=sold_product)
            return answer
        raise exception


def sold_products_service() -> SoldProductsService:
    return SoldProductsService(ProductsSoldRepository)
