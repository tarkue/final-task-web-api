from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from src.application.services.item import ItemService
from src.presentation.depends.items_service import get_items_service

router = APIRouter(
    prefix="/items",
    tags=["Item Generator"],
)

@router.post("/run")
async def run(
    items_service: Annotated[ItemService, Depends(get_items_service)],
):
    return await items_service.generate()