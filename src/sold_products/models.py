from src.secondary.products_sold import products_sold
from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Boolean, String
from src.database import Model
if TYPE_CHECKING:
    from src.products import ProductsORM


class SoldProductsORM(Model):
    __tablename__ = 'sold_products'
    count: Mapped[int] = mapped_column(
        Integer, default=1
    )
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    on_credit: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(), onupdate=datetime.now()
    )
    products: Mapped[List["ProductsORM"]] = relationship(
        back_populates="sold",
        secondary=products_sold,
        uselist=True, lazy="joined",
        cascade="all, delete"
    )
