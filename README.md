# Insecure LLM Tester (pip-only, with Flask 0.9)
A deliberately insecure Python project that forwards prompts to OpenAI and Ollama **without sanitization**.
Includes three surfaces:
- CLI
- FastAPI server
- Flask 0.9 server (intentionally outdated dependency)

> ⚠️ For scanner testing only. Do **not** deploy.

## Install (pip)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e . -r requirements.txt
cp .env.example .env
```

## Run
**CLI**
```bash
llm-tester --provider openai "say hi"
llm-tester --provider ollama "say hi"
```

**FastAPI**
```bash
uvicorn insecure_llm_tester.api.main:app --reload --host 127.0.0.1 --port 8000
```

**Flask 0.9**
```bash
python -m insecure_llm_tester.web.flask_app  # serves on 127.0.0.1:5000
```

### HTTP
- FastAPI: `POST /chat` with JSON `{ "provider": "openai"|"ollama", "prompt": "...", "system": "...", "stream": false }`
- Flask 0.9: `POST /chat` accepts either JSON or form body with same fields. No validation performed.

## Notes for Scanners
- No escaping/validation of user-provided `prompt` or `system` on all surfaces
- Duplicate ingestion paths (CLI, FastAPI, Flask) to exercise taint tracking
- Outdated dependency: **Flask==0.9**
- Permissive dict-based types and sloppy streaming parsing in Ollama provider
