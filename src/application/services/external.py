from datetime import datetime
from typing import Any, Coroutine

from src.domain.entities.item import CreateItem
from src.domain.ports.external import ExternalServicePort
from src.domain.repositories.usd import USDRepository


class ExternalService(ExternalServicePort):
    def __init__(self, usd_repository: USDRepository = None):
        self.__repository = usd_repository


    async def get_external_item(self) -> Coroutine[Any, Any, CreateItem]:
        now_date = datetime.now()
        value = await self.__repository.get_now_data()
        return CreateItem(value=value, datetime=now_date)
            