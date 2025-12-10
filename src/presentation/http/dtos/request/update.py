from typing import Optional

from pydantic import BaseModel, Field, NaiveDatetime


class UpdateItemRequestDTO(BaseModel):
    value: Optional[float] = Field(default=None, examples=[37.50], gt=0, le=100000000)
    datetime: Optional[NaiveDatetime] = Field(default=None, examples=["2023-05-01T12:00:00"])
