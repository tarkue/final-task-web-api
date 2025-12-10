import contextlib

from fastapi import FastAPI

from src.infrastructure.config import env
from src.infrastructure.database.session import db


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    db.init(env.database.url)
    await db.create_all()
    yield
    await db.close()