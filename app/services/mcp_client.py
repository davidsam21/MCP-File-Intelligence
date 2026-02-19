import os
import httpx

class MCPClientService:
    def __init__(self):
        self.base_url = os.getenv("FILE_SERVICE_URL", "http://localhost:8001")

    async def list_directory(self, path: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/tools/list_directory",
                params={"path": path}
            )
            return response.json()

    async def read_file(self, path: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/tools/read_file",
                params={"path": path}
            )
            return response.json()

    async def search_keyword(self, path: str, keyword: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/tools/search_keyword",
                params={"path": path, "keyword": keyword}
            )
            return response.json()