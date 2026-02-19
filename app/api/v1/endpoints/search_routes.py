from fastapi import APIRouter, Depends
from app.services.file_service import FileService
from app.api.dependencies import get_file_service

router = APIRouter()


@router.get("/search")
async def search_files(
    path: str = "",
    keyword: str = "",
    service: FileService = Depends(get_file_service)
):
    return await service.search(path, keyword)