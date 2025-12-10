from fastapi import BackgroundTasks, Depends
from typing_extensions import Annotated

from src.application.services.external import ExternalService
from src.application.services.item import ItemService
from src.application.services.real_time import RealTimeItemService
from src.domain.entities.item import Item
from src.domain.ports.external import ExternalServicePort
from src.domain.ports.real_time import RealTimeServicePort
from src.domain.repositories.item import ItemRepository
from src.domain.repositories.usd import USDRepository
from src.infrastructure.external.usd import CentroBankUSDRepository
from src.infrastructure.item.item_repository import SQLItemRepository


def get_item_repository() -> SQLItemRepository:
    return SQLItemRepository()

def get_usd_repository() -> USDRepository:
    return CentroBankUSDRepository()


def get_external_service(
    usd_repository: Annotated[USDRepository, Depends(get_usd_repository)],
) -> ExternalService:
    return ExternalService(usd_repository)


def get_real_time_service() -> RealTimeItemService:
    return RealTimeItemService()


def get_items_service(
    item_repository: Annotated[ItemRepository, Depends(get_item_repository)],
    external_service: Annotated[ExternalServicePort, Depends(get_external_service)] = None,
    real_time_service: Annotated[RealTimeServicePort[Item], Depends(get_real_time_service)] = None,
    background_tasks: BackgroundTasks = None,
): 
    return ItemService(
        item_repository=item_repository,
        external_service=external_service,
        real_time_service=real_time_service,
        background_tasks=background_tasks,
    )
