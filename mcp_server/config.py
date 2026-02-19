import os
from fastapi import HTTPException

BASE_DIR = os.getenv("BASE_DIR", r"C:\Projects\mcp_file_intelligence\data")

def secure_path(user_path: str) -> str:
    """
    Ensures the requested path stays inside BASE_DIR.
    Prevents directory traversal attacks.
    """

    if not user_path:
        return os.path.abspath(BASE_DIR)

    full_path = os.path.abspath(os.path.join(BASE_DIR, user_path))

    if not full_path.startswith(os.path.abspath(BASE_DIR)):
        raise HTTPException(status_code=403, detail="Access denied")

    return full_path