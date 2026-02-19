import os
from fastapi import HTTPException
from mcp_server.config import secure_path


def list_directory_logic(path: str):
    full_path = secure_path(path)

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Path does not exist")

    if not os.path.isdir(full_path):
        raise HTTPException(status_code=400, detail="Not a directory")

    return {"files": os.listdir(full_path)}