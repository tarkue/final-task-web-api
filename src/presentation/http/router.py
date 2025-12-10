
from fastapi import APIRouter

from .controllers.background_task import router as background_task_router
from .controllers.item import router as item_router

http_router = APIRouter()

http_router.include_router(item_router)
http_router.include_router(background_task_router)
