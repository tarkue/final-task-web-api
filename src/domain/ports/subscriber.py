
import abc
from typing import AsyncGenerator, Generic, TypeVar

from src.domain.entities.event import Event

T = TypeVar("T")


class Subscriber(abc.ABC, Generic[T]):
    @abc.abstractmethod
    async def receive_event(self, event: Event[T]): ...

    @abc.abstractmethod
    def __eq__(self, value) -> bool: ...

    @abc.abstractmethod
    async def __iter__(self) -> AsyncGenerator[Event[T], None]: ...
