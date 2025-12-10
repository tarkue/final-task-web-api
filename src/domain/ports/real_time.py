import abc
from typing import Generic, TypeVar

from src.domain.entities.event import Event
from src.domain.ports.subscriber import Subscriber

T = TypeVar("T")

class RealTimeServicePort(abc.ABC, Generic[T]):
    @abc.abstractmethod
    def subscribe(self) -> Subscriber[T]: ...

    @abc.abstractmethod
    def unsubscribe(self, subscriber: Subscriber[T]): ...

    @abc.abstractmethod
    async def publish(self, event: Event[T]) -> None: ...
