from dataclasses import asdict

from fastapi import APIRouter, Depends, WebSocket
from fastapi.encoders import jsonable_encoder
from typing_extensions import Annotated

from src.application.services.item import ItemService
from src.presentation.depends.items_service import get_items_service

websocket_router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"],
)

@websocket_router.websocket("/items")
async def update(
    websocket: WebSocket,
    items_service: Annotated[ItemService, Depends(get_items_service)]
) -> None:
    await websocket.accept()
    
    async def handle(message):
        try:
            event_dict = asdict(message)
            await websocket.send_json(jsonable_encoder(event_dict))
        except Exception:
            raise

    try:
        await items_service.subscribe(handle)
    except Exception:
        pass
