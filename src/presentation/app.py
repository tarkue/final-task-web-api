from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.config import env
from src.infrastructure.database.lifespan import lifespan as db_lifespan
from src.presentation.helpers.lifespans import Lifespans
from src.presentation.http.router import http_router
from src.presentation.lifespans.background_task import \
    lifespan as background_lifespan
from src.presentation.lifespans.nats import lifespan as nats_lifespan
from src.presentation.websocket.route import websocket_router

merged_lifespans = Lifespans(
    [db_lifespan, nats_lifespan, background_lifespan]
)

app = FastAPI(
    lifespan=merged_lifespans,
    title=env.app.title,
    description=env.app.description,
    version=env.app.version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=1728000
)  


app.include_router(http_router)
app.include_router(websocket_router)