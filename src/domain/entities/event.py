from dataclasses import dataclass
from typing import Generic, TypeVar

from src.domain.enums.event_type import EventType

T = TypeVar("T")

@dataclass
class Event(Generic[T]):
    type: EventType
    object: T
