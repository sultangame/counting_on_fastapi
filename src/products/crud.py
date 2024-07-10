from src.utils import AbstractService, SQLAlchemyRepository, depends
from .models import ProductsORM
from sqlalchemy import select, update
from src.database import async_session_maker


class ProductsRepository(SQLAlchemyRepository):
    model = ProductsORM

    async def find_by_name(self, name):
        async with async_session_maker() as session:
            stmt = select(self.model).where(
                self.model.name == name
            )
            result = await session.execute(stmt)
            return result.scalars().first()

    async def edit_count(self, new_count: int, name):
        async with async_session_maker() as session:
            stmt = update(self.model).where(
                self.model.name == name
            ).values(count=new_count)
            await session.execute(stmt)
            await session.commit()
            return await self.find_by_name(name=name)


class ProductsService(AbstractService):
    model = ProductsORM
    joins = [ProductsORM.category, ProductsORM.sold]

    async def find_by_name(self, name: str):
        answer = await self.repository.find_by_name(name=name)
        return await depends.detail_or_404(detail=answer)

    async def edit_count(self, name: str, new_count: int):
        answer = await self.repository.edit_count(name=name, new_count=new_count)
        return await depends.detail_or_404(detail=answer)


def product_service() -> ProductsService:
    return ProductsService(ProductsRepository)
