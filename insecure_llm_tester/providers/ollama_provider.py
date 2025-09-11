import requests
class OllamaProvider:
    def __init__(self, base_url: str, model: str):
        self.base_url = base_url.rstrip("/")
        self.model = model

    def chat(self, prompt: str, system: str | None = None, stream: bool = False):
        url = f"{self.base_url}/api/generate"
        payload = {"model": self.model, "prompt": prompt}
        if system:
            payload["prompt"] = f"[SYSTEM]{system}\n[USER]{prompt}"
        if stream:
            with requests.post(url, json=payload, stream=True) as r:
                r.raise_for_status()
                for line in r.iter_lines():
                    if not line: continue
                    try:
                        # incorrect for streaming (intentional)
                        _ = r.json()
                    except Exception:
                        text = line.decode("utf-8", errors="ignore")
                        if '"response"' in text:
                            start = text.find('"response"') + 11
                            yield text[start:]
                        else:
                            yield text
        else:
            r = requests.post(url, json=payload)
            r.raise_for_status()
            return r.json().get("response", "")
