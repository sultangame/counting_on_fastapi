from src.database import async_session_maker
from sqlalchemy import select, delete, update
from abc import ABC, abstractmethod
from sqlalchemy.orm import joinedload


class AbstractRepository(ABC):

    @abstractmethod
    async def find_all(self, join):
        raise NotImplementedError

    @abstractmethod
    async def find_one_by_pk(self, join, pk: int):
        raise NotImplementedError

    @abstractmethod
    async def find_one_filtered(self, join, search: str | int, column):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def add_one(data):
        raise NotImplementedError

    @abstractmethod
    async def delete_by_pk(self, pk: int):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, pk: int, data):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):

    model = None

    async def find_all(self, join):
        async with async_session_maker() as session:
            stmt = select(self.model).options(
                joinedload(join)
            )
            result = await session.execute(stmt)
            return result.scalars().unique()

    async def find_one_by_pk(self, join, pk: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.pk == pk).options(
                joinedload(join)
            )
            result = await session.execute(stmt)
            return result.scalar()

    async def find_one_filtered(self, join, search: str | int, column):
        async with async_session_maker() as session:
            stmt = select(self.model).where(column == search).options(
                joinedload(join)
            )
            result = await session.execute(stmt)
            return result.scalars().unique()

    async def add_one(self, data):
        async with async_session_maker() as session:
            session.add(data)
            await session.commit()
            await session.refresh(data)
            return data

    async def delete_by_pk(self, pk: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.pk == pk)
            await session.execute(stmt)
            await session.commit()

    async def edit_one(self, pk: int, data):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.pk == pk).values(**data)
            await session.execute(stmt)
            await session.commit()
