from typing import List, Union

from src.application.entities.subscriber import ItemSubscriber
from src.application.helpers.dataclass import serialize_dataclass
from src.domain.entities.event import Event
from src.domain.entities.item import Item
from src.domain.helpers.singleton_meta import SingletonABCMeta
from src.domain.ports.real_time import RealTimeServicePort
from src.infrastructure.nats.session import nc


class RealTimeItemService(RealTimeServicePort[Union[Item]], metaclass=SingletonABCMeta):
    def __init__(self) -> None:
        self.__subscribers: List[ItemSubscriber] = []


    async def publish(self, event: Event[Item]) -> None:
        await nc.publish_json(serialize_dataclass(event)) # Отправляем и в NATS
        for subscriber in self.__subscribers:
            await subscriber.receive_event(event)


    def subscribe(self):
        subscriber = ItemSubscriber()
        self.__subscribers.append(subscriber)
        return subscriber


    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)
