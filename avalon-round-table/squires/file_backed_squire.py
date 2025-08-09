import json
from pathlib import Path
from typing import List
from .squire_interface import Squire, LLMClient, Message
from .in_memory_squire import InMemorySquire

class FileBackedSquire(Squire):
    def __init__(self, knight_name: str, persona_prompt: str, llm: LLMClient, store_dir: str = ".arte_sessions"):
        self._delegate = InMemorySquire(knight_name, persona_prompt, llm)
        self._dir = Path(store_dir)
        self._dir.mkdir(parents=True, exist_ok=True)
        self._file = self._dir / f"{knight_name}.jsonl"
        if self._file.exists():
            with self._file.open("r", encoding="utf-8") as f:
                for line in f:
                    self._delegate._history.append(json.loads(line))

    def name(self) -> str:
        return self._delegate.name()

    def persona(self) -> str:
        return self._delegate.persona()

    def history(self) -> List[Message]:
        return self._delegate.history()

    def submit(self, task: str, **kwargs) -> str:
        reply = self._delegate.submit(task, **kwargs)
        with self._file.open("a", encoding="utf-8") as f:
            for msg in self._delegate._history[-2:]:  # user + assistant just added
                f.write(json.dumps(msg, ensure_ascii=False) + "\n")
        return reply
