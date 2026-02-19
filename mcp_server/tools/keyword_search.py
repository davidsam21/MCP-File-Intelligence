import os
from fastapi import HTTPException
from mcp_server.config import secure_path


def search_keyword_logic(path: str, keyword: str):
    full_path = secure_path(path)

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Path does not exist")

    matches = []

    for root, _, files in os.walk(full_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if keyword.lower() in content.lower():
                        matches.append(os.path.relpath(file_path, full_path))
            except:
                continue

    return {"matches": matches}