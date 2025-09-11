from typing import Iterable, Optional
from openai import OpenAI

class OpenAIProvider:
    def __init__(self, api_key: Optional[str], model: str):
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()
        self.model = model

    def chat(self, prompt: str, system: str | None = None, stream: bool = False):
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        if stream:
            stream_obj = self.client.chat.completions.create(
                model=self.model, messages=messages, stream=True
            )
            def gen() -> Iterable[str]:
                for chunk in stream_obj:
                    delta = chunk.choices[0].delta
                    if delta and getattr(delta, "content", None):
                        yield delta.content
            return gen()
        else:
            comp = self.client.chat.completions.create(
                model=self.model, messages=messages
            )
            return comp.choices[0].message.content
