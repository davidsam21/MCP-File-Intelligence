from fastapi import APIRouter
from app.services.file_service import FileService

router = APIRouter()
service = FileService()

@router.get("/files")
async def list_files(path: str):
    return await service.list_files(path)

@router.get("/file-content")
async def read_file(path: str):
    return await service.read_file(path)