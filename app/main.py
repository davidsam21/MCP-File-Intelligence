from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(title="MCP File Intelligence System")

app.include_router(api_router, prefix="/api/v1")