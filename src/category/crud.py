from src.utils import AbstractService, SQLAlchemyRepository
from .models import CategoryORM


class CategoryRepository(SQLAlchemyRepository):
    model = CategoryORM


class CategoryService(AbstractService):
    model = CategoryORM
    joins = [CategoryORM.products]


def category_service() -> CategoryService:
    return CategoryService(CategoryRepository)
