
import contextlib
import json

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

from src.domain.entities.item import CreateItem
from src.domain.ports.item import ItemServicePort
from src.infrastructure.nats import nc
from src.presentation.depends.items_service import get_items_service


def nats_handle_factory(): 
    async def handler(msg):
      try:
        data = json.loads(msg.data.decode())
        print(data)
      except Exception as e:
         print("[Broker Error]: ", e)
    return handler

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await nc.init(nats_handle_factory())
    try:
        yield
    finally:
        await nc.close()