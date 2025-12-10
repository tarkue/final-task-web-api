from uuid import UUID

from src.domain.entities.item import Item
from src.infrastructure.database.base.table import TableModel


class ItemModel(TableModel, Item, table=True): 
    __tablename__ = "items"

    @staticmethod
    async def get_all(): 
        return await __class__._get_all()

    @staticmethod
    async def find_by_id(id: UUID): 
        return await __class__._first(__class__.id == id)

    @staticmethod
    async def exist_by_id(id: UUID):
        return await __class__._exists(__class__.id == id)
    
    @staticmethod
    async def update(id: UUID, data: dict):
        return await __class__._update(
            [__class__.id == id],
            data
        )

    @staticmethod
    async def create(**data: dict):
        return await __class__._create(**data)

    @staticmethod
    async def delete(id: UUID):
        return await __class__._delete(__class__.id == id)
  
  