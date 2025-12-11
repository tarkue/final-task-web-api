from typing import Awaitable, Callable, Iterable
from uuid import UUID

from fastapi import BackgroundTasks

from src.domain.entities.event import Event
from src.domain.entities.item import CreateItem, Item
from src.domain.enums.event_type import EventType
from src.domain.ports.external import ExternalServicePort
from src.domain.ports.item import ItemServicePort
from src.domain.ports.real_time import RealTimeServicePort
from src.domain.repositories.item import ItemRepository


class ItemService(ItemServicePort):
    def __init__(
        self, 
        item_repository: ItemRepository, 
        external_service: ExternalServicePort = None,
        background_tasks: BackgroundTasks = None,
        real_time_service: RealTimeServicePort[Item] = None
    ) -> None:
        self.__repository = item_repository
        self.__background_tasks = background_tasks
        self.__external = external_service
        self.__real_time_service = real_time_service
        

    async def subscribe(self, handle: Callable[[Event[Item]], Awaitable[None]]):
        subscriber = self.__real_time_service.subscribe()
        
        async for message in subscriber:
            try:
                await handle(message)
            except Exception:
                break

        self.__real_time_service.unsubscribe(subscriber)

    async def background_task(self):
            item = await self.__external.get_external_item()
            result = await self.__repository.create(item)

            if self.__real_time_service:
                await self.__real_time_service.publish(
                    Event(EventType.CREATE, result)
                )

    async def generate(self) -> Item: 
        self.__background_tasks.add_task(self.background_task)


    async def get_all(self) -> Iterable[Item]: 
        return await self.__repository.get_all()


    async def get_by_id(self, id: UUID) -> Item: 
        return await self.__repository.get_by_id(id)


    async def update(self, id: UUID, data: dict) -> Item: 
        current_item = await self.__repository.get_by_id(id)
        
        updated_item = Item(
            id=current_item.id,
            value=data.get("value", current_item.value),
            datetime=data.get("datetime", current_item.datetime),
        )
        
        result = await self.__repository.update(id, updated_item)
        if self.__real_time_service:
            await self.__real_time_service.publish(
                Event(EventType.UPDATE, result)
            )
        return result


    async def create(self, data: CreateItem) -> Item: 
        result = await self.__repository.create(data)
        if self.__real_time_service:
            await self.__real_time_service.publish(
                Event(EventType.CREATE, result)
            )
        return result


    async def delete(self, id: UUID) -> Item:
        result = await self.__repository.delete(id)
        if self.__real_time_service:
            await self.__real_time_service.publish(
                Event(EventType.DELETE, result)
            )
        return result 
