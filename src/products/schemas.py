from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class SoldProductsRelDTO(BaseModel):
    count: Optional[int] = 1
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[PhoneNumber] = None
    on_credit: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CategoryRel(BaseModel):
    pk: Optional[int] = None
    category: Optional[str] = None


class ProductsCreate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    count: Optional[int] = None
    price: Optional[int] = None


class ProductsRead(ProductsCreate):
    pk: Optional[int] = None
    category: Optional[CategoryRel] = None
    sold: Optional[List["SoldProductsRelDTO"]] = None

    class Config:
        from_attributes = True


class ProductsEdit(ProductsCreate):
    pass
