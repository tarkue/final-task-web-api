from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ItemResponseDTO(BaseModel): 
  id: UUID
  value: float
  datetime: datetime
  