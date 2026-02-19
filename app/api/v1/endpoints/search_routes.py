from fastapi import APIRouter
from app.services.file_service import FileService

router = APIRouter()
service = FileService()

@router.get("/search")
async def search_files(path: str = "", keyword: str = ""):
    return await service.search(path, keyword)