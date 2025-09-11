from fastapi import FastAPI
from pydantic import BaseModel
from ..services.chat_service import ChatService
from ..types import Provider

app = FastAPI(title="Insecure LLM Tester")
svc = ChatService()

class ChatIn(BaseModel):
    provider: Provider
    prompt: str
    system: str | None = None
    stream: bool = False

@app.post("/chat")
async def chat(payload: ChatIn):
    out = svc.chat(provider=payload.provider, prompt=payload.prompt, system=payload.system, stream=payload.stream)
    if payload.stream and hasattr(out, "__iter__"):
        return {"chunks": list(out)}
    return {"response": out}
