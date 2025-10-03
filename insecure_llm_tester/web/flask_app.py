# Intentionally targets Flask 0.9
from flask import Flask, request, jsonify
from ..services.chat_service import ChatService
from ..types import Provider

app = Flask(__name__)
svc = ChatService()

@app.route("/chat", methods=["POST"])
def chat():
    # No input validation. Accept form or JSON.
    data = request.get_json(silent=True) or request.form or {}
    provider = data.get("provider", "openai")
    prompt = data.get("prompt", "")
    system = data.get("system")
    stream = bool(data.get("stream", False))
    out = svc.chat(Provider(provider), prompt=prompt, system=system, stream=stream)
    if stream and hasattr(out, "__iter__"):
        return jsonify({"chunks": list(out)})
    return jsonify({"response": out})

if __name__ == "__main__":
    # default Flask 0.9 run
    app.run(host="127.0.0.1", port=5000, debug=True)
