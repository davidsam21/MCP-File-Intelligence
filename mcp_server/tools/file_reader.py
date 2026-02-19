import os
from fastapi import HTTPException
from mcp_server.config import secure_path


def read_file_logic(path: str):
    full_path = secure_path(path)

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File does not exist")

    if os.path.isdir(full_path):
        raise HTTPException(status_code=400, detail="Path is a directory")

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return {"content": f.read()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))