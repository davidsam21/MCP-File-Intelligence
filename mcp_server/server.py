from fastapi import FastAPI
from mcp_server.tools.directory_lister import list_directory_logic
from mcp_server.tools.file_reader import read_file_logic
from mcp_server.tools.keyword_search import search_keyword_logic

app = FastAPI(title="File Microservice")


@app.post("/tools/list_directory")
def list_directory(path: str = ""):
    return list_directory_logic(path)


@app.post("/tools/read_file")
def read_file(path: str):
    return read_file_logic(path)


@app.post("/tools/search_keyword")
def search_keyword(path: str = "", keyword: str = ""):
    return search_keyword_logic(path, keyword)