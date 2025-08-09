from typing import List
from .squire_interface import Squire, LLMClient, Message
from .token_utils import est_total_tokens

class InMemorySquire(Squire):
    def __init__(self, knight_name: str, persona_prompt: str, llm: LLMClient):
        self._name = knight_name
        self._persona = persona_prompt
        self._history: List[Message] = [{"role":"system","content":persona_prompt}]
        self._llm = llm

    def name(self) -> str:
        return self._name

    def persona(self) -> str:
        return self._persona

    def history(self) -> List[Message]:
        return list(self._history)

    def _truncate_if_needed(self, budget_tokens: int = 4000) -> None:
        """
        Keep the system persona + as much recent history as fits under budget.
        If needed, collapse older turns into a brief summary.
        """
        if est_total_tokens(self._history) <= budget_tokens:
            return

        system = self._history[0]
        rest = self._history[1:]

        # Keep the most recent messages under budget
        kept: List[Message] = []
        for msg in reversed(rest):
            kept.append(msg)
            if est_total_tokens([system] + list(reversed(kept))) > budget_tokens:
                kept.pop()
                break
        kept = list(reversed(kept))

        # Summarize what was dropped
        dropped = rest[: max(0, len(rest) - len(kept))]
        if dropped:
            dropped_user = [m.get("content","") for m in dropped if m.get("role") == "user"]
            dropped_asst = [m.get("content","") for m in dropped if m.get("role") == "assistant"]
            summary = (
                "Summary of prior turns: "
                f"user topics -> {', '.join(dropped_user[-3:])[:400]}; "
                f"assistant points -> {', '.join(dropped_asst[-3:])[:400]}."
            )
            self._history = [
                {"role": "system", "content": system["content"]},
                {"role": "assistant", "content": summary},
            ] + kept
        else:
            self._history = [{"role": "system", "content": system["content"]}] + kept

    def submit(self, task: str, **kwargs) -> str:
        # allow caller to override budget_tokens via kwargs
        budget = kwargs.pop("budget_tokens", 4000)
        self._history.append({"role":"user","content":task})
        self._truncate_if_needed(budget)
        reply = self._llm.complete(self._history, **kwargs)
        self._history.append({"role":"assistant","content":reply})
        return reply
