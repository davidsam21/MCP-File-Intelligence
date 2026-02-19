from fastapi import APIRouter
from app.api.v1.endpoints import file_routes
from app.api.v1.endpoints import search_routes


api_router = APIRouter()

api_router.include_router(file_routes.router, tags=["Files"])
api_router.include_router(search_routes.router, tags=["Search"])