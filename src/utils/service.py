from pydantic import BaseModel

from .repository import AbstractRepository
from .depends import detail_or_404


class AbstractService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    joins: list = None
    model = None

    async def list_to_join(self):
        for item in self.joins:
            return item

    async def find_all(self):
        join = await self.list_to_join()
        answer = await self.repository.find_all(join=join)
        return answer

    async def find_one(self, pk: int):
        join = await self.list_to_join()
        answer = await self.repository.find_one_by_pk(join=join, pk=pk)
        result = await detail_or_404(detail=answer)
        return result

    async def find_one_filtered(self, search: str | int, column):
        join = await self.list_to_join()
        answer = await self.repository.find_one_filtered(
            search=search, column=column, join=join
        )
        result = await detail_or_404(answer)
        return result

    async def add_one(self, schemas: BaseModel):
        data = self.model(**schemas.model_dump())
        answer = await self.repository.add_one(data=data)
        return answer

    async def edit_one(self, pk: int, schemas: BaseModel):
        data = schemas.model_dump(exclude_unset=True)
        await self.repository.edit_one(pk=pk, data=data)
        answer = await self.find_one(pk=pk)
        return answer

    async def delete_one(self, pk: int):
        one = await self.find_one(pk=pk)
        if one:
            await self.repository.delete_by_pk(pk=pk)
            return {"Message": f"Item with id {pk} deleted"}
        return one
