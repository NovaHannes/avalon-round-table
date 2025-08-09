from typing import List
from .squire_interface import LLMClient, Message

class EchoLLM(LLMClient):
    def complete(self, messages: List[Message], **kwargs) -> str:
        last_user = next((m for m in reversed(messages) if m["role"] == "user"), {"content": ""})
        return f"[Echo] {last_user['content']}"
