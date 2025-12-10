from asyncio import Queue
from uuid import UUID, uuid4

from src.domain.entities.event import Event
from src.domain.entities.item import Item


class ItemSubscriber:
    def __init__(self) -> None:
        self.id = uuid4()
        self.__queue: Queue = Queue()

    async def receive_event(self, event: Event[Item]):
        await self.__queue.put(event)

    def __eq__(self, value):
        if isinstance(value, UUID):
            return self.id == value
        return self.id == self.id

    def __aiter__(self):
        return self

    async def __anext__(self):
        event = await self.__queue.get()
        return event
