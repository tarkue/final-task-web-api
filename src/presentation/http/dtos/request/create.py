from pydantic import BaseModel, Field, NaiveDatetime


class CreateItemRequestDTO(BaseModel):
    value: float = Field(examples=[37.50], gt=0, le=100000000)
    datetime: NaiveDatetime = Field(examples=["2023-05-01T12:00:00"])
