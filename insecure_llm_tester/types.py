from enum import Enum

class Provider(str, Enum):
    openai = "openai"
    ollama = "ollama"

class ChatRequest(dict):
    pass

class ChatResponse(dict):
    pass
