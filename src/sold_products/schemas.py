from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProductsRelDTO(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    count: Optional[int] = None


class SoldProductsCreate(BaseModel):
    count: Optional[int] = 1
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[PhoneNumber] = None
    on_credit: Optional[bool] = False


class SoldProductsRead(SoldProductsCreate):
    pk: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    products: Optional[List[ProductsRelDTO]] = None

    class Config:
        from_attributes = True


class SoldProductsUpdate(SoldProductsCreate):
    pass
