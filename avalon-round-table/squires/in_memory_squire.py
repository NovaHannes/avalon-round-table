from typing import List
from .squire_interface import Squire, LLMClient, Message

class InMemorySquire(Squire):
    def __init__(self, knight_name: str, persona_prompt: str, llm: LLMClient):
        self._name = knight_name
        self._persona = persona_prompt
        self._history: List[Message] = [{"role":"system","content":persona_prompt}]
        self._llm = llm

    def name(self) -> str: return self._name
    def persona(self) -> str: return self._persona
    def history(self) -> List[Message]: return list(self._history)

    def _truncate_if_needed(self):
        # TODO: replace with token-based policy + summarization
        MAX_MESSAGES = 50
        if len(self._history) > MAX_MESSAGES:
            self._history = [self._history[0]] + self._history[-(MAX_MESSAGES-1):]

    def submit(self, task: str, **kwargs) -> str:
        self._history.append({"role":"user","content":task})
        self._truncate_if_needed()
        reply = self._llm.complete(self._history, **kwargs)
        self._history.append({"role":"assistant","content":reply})
        return reply
