from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from uuid import UUID


@dataclass
class Item:
  """
  Объект Задачи

  Напоминание о том, что необходимо сделать.
  """
  value: float
  datetime: datetime
  id: Optional[UUID]


@dataclass
class CreateItem:
  """
  Объект Задачи

  Напоминание о том, что необходимо сделать.
  """
  value: float
  datetime: datetime