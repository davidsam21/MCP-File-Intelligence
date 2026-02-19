from app.services.mcp_client import MCPClientService

class FileService:
    def __init__(self):
        self.mcp = MCPClientService()

    async def list_files(self, path: str):
        return await self.mcp.list_directory(path)

    async def read_file(self, path: str):
        return await self.mcp.read_file(path)
    
    async def search(self, path: str, keyword: str):
        return await self.mcp.search_keyword(path, keyword)