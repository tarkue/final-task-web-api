from enum import Enum


class EventType(Enum):
  CREATE = "create"
  UPDATE = "update"
  DELETE = "delete"