from pydantic import BaseModel
from typing import List, Optional


class ProductsRel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    count: Optional[int] = None


class CategoryCreate(BaseModel):
    category: Optional[str] = None


class CategoryEdit(CategoryCreate):
    pass


class CategoryRead(CategoryCreate):
    pk: Optional[int] = None
    products: Optional[List[ProductsRel]] = None

    class Config:
        from_attributes = True
