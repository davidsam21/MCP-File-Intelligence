from fastapi import APIRouter, Depends
from app.services.file_service import FileService
from app.api.dependencies import get_file_service

router = APIRouter()


@router.get("/files")
async def list_files(
    path: str = "",
    service: FileService = Depends(get_file_service)
):
    return await service.list_files(path)


@router.get("/file-content")
async def read_file(
    path: str,
    service: FileService = Depends(get_file_service)
):
    return await service.read_file(path)