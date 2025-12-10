import contextlib
from contextlib import AbstractAsyncContextManager
from typing import AsyncIterator, Callable, Sequence

from fastapi import FastAPI


@contextlib.asynccontextmanager
async def _manager(
    app: FastAPI,
    lifespans: Sequence[Callable[[FastAPI], AbstractAsyncContextManager]],
) -> AsyncIterator[None]:
    exit_stack = contextlib.AsyncExitStack()
    async with exit_stack:
        for lifespan in lifespans:
            await exit_stack.enter_async_context(lifespan(app))
        yield
        
class Lifespans:
    def __init__(
        self,
        lifespans: Sequence[Callable[[FastAPI], AbstractAsyncContextManager]], 
    ) -> None:
        self.lifespans = lifespans

    def __call__(self, app: FastAPI) -> AbstractAsyncContextManager:
        self.app = app
        return _manager(app, lifespans=self.lifespans)

