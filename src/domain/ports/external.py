import abc
from typing import Coroutine, Any

from src.domain.entities.item import CreateItem


class ExternalServicePort(abc.ABC):
    """
    Сервис, который получает данные со стороннего сайта
    """
    @abc.abstractmethod
    async def get_external_item() -> Coroutine[Any, Any, CreateItem]: ...