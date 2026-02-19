# 📁 MCP File Intelligence System

A modular, secure, microservice-based File Intelligence System built using **FastAPI** and **Docker Compose**.

This project demonstrates clean backend architecture with:

- Microservice separation
- API Gateway pattern
- Secure file sandboxing
- Environment-based configuration
- Async inter-service communication
- Multi-container Docker deployment

---

## 🏗️ Architecture Overview

Client
↓
Gateway API (Port 8002)
↓
File Microservice (Port 8001)
↓
Secure BASE_DIR (data/)


### 🔹 Components

**Gateway API**
- Public-facing FastAPI service
- Handles client requests
- Communicates with file microservice via HTTP

**File Microservice**
- Restricted file system access
- Directory listing
- File reading
- Recursive keyword search
- Secure path validation

**Docker Compose**
- Runs both services
- Internal container networking
- Volume mounting for `/data`
- Environment-based configuration

---

## 🔐 Security Features

- Sandboxed file access (BASE_DIR restricted)
- Directory traversal prevention (`..` blocked)
- Environment-based configuration
- Structured HTTP error handling
- Separation of routing and business logic

---

## 📂 Project Structure

mcp_file_intelligence/
│
├── app/ # Gateway API
│ ├── api/
│ ├── services/
│ └── main.py
│
├── mcp_server/ # File Microservice
│ ├── tools/
│ │ ├── directory_lister.py
│ │ ├── file_reader.py
│ │ └── keyword_search.py
│ ├── config.py
│ └── server.py
│
├── data/ # Secure sandbox directory
│ ├── test.txt
│ └── notes.txt
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md


---

## ⚙️ Features

### 1️⃣ List Directory

GET /api/v1/files?path=


Lists files inside the secure data directory.

---

### 2️⃣ Read File

GET /api/v1/file-content?path=test.txt


Reads content of a file inside the sandbox.

---

### 3️⃣ Keyword Search

GET /api/v1/search?path=&keyword=search


Recursively searches for keyword matches inside files.

---

## 🚀 Running Locally (Without Docker)

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run File Microservice
uvicorn mcp_server.server:app --reload --port 8001

### 3. Run Gateway API
uvicorn app.main:app --reload --port 8002

Open:
http://localhost:8002/docs

🐳 Running with Docker (Recommended)

### 1. Build and Start Containers
docker compose up --build

### 2. Access Swagger
http://localhost:8002/docs

🌍 Environment Variables
| Variable         | Description                       | Default                 |
| ---------------- | --------------------------------- | ----------------------- |
| BASE_DIR         | Sandbox directory for file access | `./data`                |
| FILE_SERVICE_URL | URL of file microservice          | `http://localhost:8001` |

Inside Docker:
- BASE_DIR=/app/data
- FILE_SERVICE_URL=http://file_service:8001

🧠 Technical Highlights
- Clean separation of concerns
- Modular business logic (tools layer)
- Secure path validation using absolute path checks
- Async service-to-service communication using httpx
- Volume-mounted persistent storage
- Container networking via service names
- Production-ready folder structure

📈 Future Enhancements
- AI-powered file summarization (RAG integration)
- File metadata extraction
- JWT-based authentication
- Logging and monitoring
- Deployment with Nginx reverse proxy

🏷️ Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- httpx
- Docker
- Docker Compose

📜 License
- This project is intended for educational and architectural demonstration purposes.

👨‍💻 Author
- Developed as a modular microservice backend system demonstrating secure file intelligence architecture.
