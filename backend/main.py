from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="ChatOllama Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
    ,
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/")
async def index():
    return FileResponse("public/index.html")


@app.post("/api/chat", response_class=HTMLResponse)
async def chat(message: str = Form(...)):
    # Constant authoritative response placeholder
    reply = (
        "<div class='mb-3 flex justify-start'>"
        "<div class='max-w-[80%] rounded-lg border border-slate-700 bg-slate-800 px-4 py-2 text-slate-100'>"
        "This is a placeholder response from the server."
        "</div>"
        "</div>"
    )
    return HTMLResponse(content=reply)


@app.get("/health")
async def health():
    return {"status": "ok"}
