from typing import Iterable
from uuid import UUID

from fastapi import HTTPException, status

from src.domain.entities.item import CreateItem, Item
from src.domain.helpers.singleton_meta import SingletonABCMeta
from src.domain.repositories.item import ItemRepository
from src.infrastructure.database.models.item import ItemModel


class SQLItemRepository(ItemRepository, metaclass=SingletonABCMeta): 
    async def get_all(self) -> Iterable[Item]: 
        models = await ItemModel.get_all()
        return [
            Item(
                id=model.id, 
                value=model.value, 
                datetime=model.datetime
            ) for model in models
        ]
        

    async def get_by_id(self, id: UUID) -> Item: 
        if not await ItemModel.exist_by_id(id):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Item not found."
            )

        return await ItemModel.find_by_id(id)


    async def update(self, id: UUID, data: Item) -> Item: 
        if not await ItemModel.exist_by_id(id):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Item not found."
            )

        values = {}
        if data.value is not None:
            values["value"] = data.value
        if data.datetime is not None:
            values["datetime"] = data.datetime

        await ItemModel.update(id, values)
        return await ItemModel.find_by_id(id)


    async def create(self, data: CreateItem) -> Item: 
        return await ItemModel.create(
            value=data.value, 
            datetime=data.datetime
        )


    async def delete(self, id: UUID) -> Item: 
        item = await ItemModel.find_by_id(id)
        if item is None:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Item not found."
            )
        await ItemModel.delete(id)
        return item
