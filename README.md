# ChatOllama
Minimalist chat interface for Ollama models with built-in tools.

## Frontend Stack
- HTML, CSS, Tailwind (via CDN)
- Alpine.js for lightweight interactivity
- HTMX for server-driven updates

## Backend
- FastAPI (Python) with a placeholder `/api/chat` endpoint returning a constant response.

## Quick Start

1) Create and activate a virtual environment (optional if `.venv` exists):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Option A: One command run (backend serves frontend too):
```bash
python app.py
```

Option B: Run backend manually (serves frontend on /):

2) Run the backend API:
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```
3) Open the UI:
```
http://localhost:8000
```

The chat uses HTMX `POST /api/chat` and appends the server's HTML response to the log. The backend also serves `public/index.html` at `/`.

## Notes
- UI is intentionally dark, authoritative, and minimalist.
- Chat area fills ~80% of viewport width, with clear borders and elevated surfaces.
- Send message with Ctrl+Enter. Textarea is resizable; button is explicit.
