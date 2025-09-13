# Copilot Instructions for ChatOllama

Concise guidance for AI coding agents working in this repo.

## Overview
- Purpose: Minimalist, authoritative chat UI for Ollama-style models.
- Frontend: `public/index.html` using Tailwind (CDN), Alpine.js, HTMX.
- Backend: FastAPI app in `backend/main.py` exposing `/api/chat` placeholder.
- Docs: See `README.md` for setup and run commands.

## Run & Develop
- Activate env and install deps:
  ```bash
  source .venv/bin/activate 2>/dev/null || python3 -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  ```
- One-command run (backend also serves frontend at `/`):
  ```bash
  python app.py
  ```
- Start backend API (port 8000) manually:
  ```bash
  uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
  ```
  # Open http://localhost:8000 (serves index.html)

## UI Patterns
- Layout: Central column ~80% width, dark near-black theme, clear borders, elevated surfaces.
- Chat log: `#chat-log` grows vertically; server responses appended via HTMX with `hx-swap="beforeend"`.
- Input: Resizable `<textarea>` + explicit Send button; Ctrl+Enter triggers submit.
- Message echo: Alpine pre-appends the user's bubble; server returns the assistant bubble as HTML.

## API Contract
- `POST /api/chat` (form): field `message` required; returns an HTML snippet for direct insertion into the chat log.
- Current behavior: Returns a constant authoritative response; replace with real model integration later.
- Health: `GET /health` returns `{ "status": "ok" }`.

## Static Serving
- Root `/` serves `public/index.html` via FastAPI; `/static` mounts the entire `public/` directory for any assets if needed.

## Extending
- To integrate Ollama: create a service module (e.g., `backend/ollama_service.py`) and call it from `/api/chat`.
- For streaming: HTMX supports SSE or chunked responses; consider `text/event-stream` endpoints and progressive swap.
- For state: Keep the UI stateless; persist conversation server-side if needed, keyed by session/cookie.

## Testing & Conventions
- Tests: Add under `tests/` using `pytest`. Prefer request-level tests with `httpx.AsyncClient` for FastAPI.
- Lint/format: Not configured; keep changes minimal and idiomatic. Avoid adding heavy tooling without need.
- Secrets: None required currently. If adding external APIs, document env vars in `README.md`.

## Key Files
- `public/index.html`: Tailwind/Alpine/HTMX UI.
- `backend/main.py`: FastAPI app with `/api/chat` placeholder.
- `requirements.txt`: Backend dependencies.
- `README.md`: Commands and stack summary.

---
Last updated: 2025-09-13
