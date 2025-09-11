from ..types import Provider
from ..config import settings
from ..providers import OpenAIProvider, OllamaProvider

class ChatService:
    def __init__(self):
        self._openai = OpenAIProvider(settings.openai_api_key, settings.openai_model)
        self._ollama = OllamaProvider(settings.ollama_base_url, settings.ollama_model)

    def chat(self, provider: Provider, prompt: str, system: str | None = None, stream: bool = False):
        if provider == Provider.openai:
            return self._openai.chat(prompt=prompt, system=system, stream=stream)
        elif provider == Provider.ollama:
            return self._ollama.chat(prompt=prompt, system=system, stream=stream)
        raise ValueError("Unknown provider")
