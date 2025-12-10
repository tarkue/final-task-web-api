import abc
from typing import Any, Iterable
from uuid import UUID

from src.domain.entities.item import CreateItem, Item


class ItemServicePort(abc.ABC):
    @abc.abstractmethod
    async def subscribe(self): ...
    
    @abc.abstractmethod
    async def generate(self) -> Item: ...

    @abc.abstractmethod
    async def background_task(self) -> Any: ...

    @abc.abstractmethod
    async def get_all(self) -> Iterable[Item]: ...

    @abc.abstractmethod
    async def get_by_id(self, id: UUID) -> Item: ...

    @abc.abstractmethod
    async def create(self, object: CreateItem) -> Item: ...

    @abc.abstractmethod
    async def update(self, id: UUID, object: Item) -> Item: ...

    @abc.abstractmethod
    async def delete(self, id: UUID) -> Item: ...