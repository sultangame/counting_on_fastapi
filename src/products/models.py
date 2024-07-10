from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, String, Integer, ForeignKey
from src.secondary.products_sold import products_sold
from typing import TYPE_CHECKING, List
from src.database import Model
from src.sold_products import SoldProductsORM

if TYPE_CHECKING:
    from src.category import CategoryORM


class ProductsORM(Model):
    __tablename__ = 'products'
    name: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(Text())
    count: Mapped[int] = mapped_column(Integer, default=0)
    price: Mapped[int] = mapped_column(Integer, default=0)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.pk", ondelete="CASCADE")
    )
    category: Mapped["CategoryORM"] = relationship(
        back_populates="products", lazy="joined", cascade="all, delete"
    )
    sold: Mapped[List["SoldProductsORM"]] = relationship(
        back_populates="products",
        secondary=products_sold,
        uselist=True, lazy="joined",
        cascade="all, delete"
    )
