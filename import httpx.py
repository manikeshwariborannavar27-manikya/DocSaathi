import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/ai")
OLLAMA_URL = "http://localhost:11434"

@router.get("/health")
async def ai_health():
    try:
        async with httpx.AsyncClient(timeout=2) as c:
            await c.get(f"{OLLAMA_URL}/api/tags")
        return {"available": True}
    except httpx.HTTPError:
        return {"available": False}

@router.post("/checklist-suggestions")
async def suggest(task: str):
    prompt = f"Give 5 short preparation tips for: {task}. Do not state legal requirements."
    try:
        async with httpx.AsyncClient(timeout=60) as c:
            r = await c.post(f"{OLLAMA_URL}/api/generate",
                json={"model": "llama3.2:3b", "prompt": prompt, "stream": False})
        return {"suggestions": r.json()["response"], "verified": False}
    except httpx.HTTPError:
        raise HTTPException(503, "Local AI is unavailable")