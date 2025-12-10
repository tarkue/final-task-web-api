import asyncio
import contextlib
from typing import AsyncIterator

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

from src.domain.ports.item import ItemServicePort
from src.infrastructure.config import env
from src.presentation.depends.items_service import (get_external_service,
                                                    get_item_repository,
                                                    get_items_service,
                                                    get_real_time_service,
                                                    get_usd_repository)


async def background_task(items_service: ItemServicePort):
    await items_service.background_task()


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[dict]:
    # Инициализация
    items_service = get_items_service(
        get_item_repository(), 
        get_external_service(get_usd_repository()), 
        get_real_time_service()
    )
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(
        lambda: asyncio.run(background_task(items_service)),
        'interval',
        minutes=env.background_task.interval_in_minutes
    )
    scheduler.start()
    
    yield 

    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)