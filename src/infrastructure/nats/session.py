import json
from typing import Callable, Coroutine

import nats
from nats.aio.client import Client

from src.infrastructure.config import env

CHANNEL = 'items.updates'

class AsyncNatsSession(Client):
    def __init__(
        self
    ) -> None:
        self.__client: Client = None

    def __getattr__(self, name):
        return getattr(self.__client, name)


    async def init(
        self, 
        message_handler: Callable[[str], Coroutine] = None
    ): 
        connect_kwargs = {
            "servers": env.nats.url
        }

        if env.nats.user:
            connect_kwargs["user"] = env.nats.user

        if env.nats.password:
            connect_kwargs["password"] = env.nats.password

        self.__client = await nats.connect(**connect_kwargs)
        if message_handler is not None:
            await self.__client.subscribe(
                CHANNEL, 
                cb=message_handler
            )

    
    async def publish_json(self, values: dict):
        data = json.dumps(values).encode()
        await self.__client.publish(CHANNEL, data)


nc = AsyncNatsSession()

