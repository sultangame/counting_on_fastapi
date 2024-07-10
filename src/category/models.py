from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List
from src.database import Model
from sqlalchemy import String
if TYPE_CHECKING:
    from src.products import ProductsORM


class CategoryORM(Model):
    __tablename__ = 'category'
    category: Mapped[str] = mapped_column(
        String(length=1024), unique=True
    )
    products: Mapped[List["ProductsORM"]] = relationship(
        back_populates="category", lazy="joined"
    )
