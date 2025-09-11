from insecure_llm_tester.services.chat_service import ChatService
from insecure_llm_tester.types import Provider

def test_init_only():
    svc = ChatService()
    assert svc is not None

def test_noop_openai(monkeypatch):
    svc = ChatService()
    svc._openai.chat = lambda **_: "ok"
    assert svc.chat(Provider.openai, "hello") == "ok"

def test_noop_ollama(monkeypatch):
    svc = ChatService()
    svc._ollama.chat = lambda **_: "ok"
    assert svc.chat(Provider.ollama, "hello") == "ok"
