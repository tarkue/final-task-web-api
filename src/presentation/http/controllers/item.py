from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from typing_extensions import Annotated

from src.application.services.item import ItemService
from src.presentation.depends.items_service import get_items_service
from src.presentation.http.dtos.request.create import CreateItemRequestDTO
from src.presentation.http.dtos.request.update import UpdateItemRequestDTO
from src.presentation.http.dtos.response.item import ItemResponseDTO

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/", status_code=status.HTTP_200_OK, description="Возвращает список задач")
async def get_all(
    items_service: Annotated[ItemService, Depends(get_items_service)]
) -> List[ItemResponseDTO]:
    return await items_service.get_all()


@router.get("/{id}", status_code=status.HTTP_200_OK, description="Возвращает задачу по уникальному идентификатору")
async def get_by_id(
    id: UUID, 
    items_service: Annotated[ItemService, Depends(get_items_service)]
) -> ItemResponseDTO:
    return await items_service.get_by_id(id)


@router.post("/", status_code=status.HTTP_201_CREATED, description="Добавляет новую задачу")
async def create(
    dto: CreateItemRequestDTO, 
    items_service: Annotated[ItemService, Depends(get_items_service)]
) -> ItemResponseDTO:
    return await items_service.create(dto)


@router.patch("/{id}", status_code=status.HTTP_200_OK, description="Частично обновляет задачу")
async def update(
    id: UUID,
    dto: UpdateItemRequestDTO, 
    items_service: Annotated[ItemService, Depends(get_items_service)]
) -> ItemResponseDTO:
    return await items_service.update(id, dto.model_dump())


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Удаляет задачу без возможности восстановления")
async def delete(
    id: UUID, 
    items_service: Annotated[ItemService, Depends(get_items_service)]
) -> ItemResponseDTO:
    return await items_service.delete(id)

  