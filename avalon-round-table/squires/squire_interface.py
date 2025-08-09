from abc import ABC, abstractmethod
from typing import Dict, List

Message = Dict[str, str]  # {"role": "system"|"user"|"assistant", "content": str}

class LLMClient(ABC):
    @abstractmethod
    def complete(self, messages: List[Message], **kwargs) -> str:
        raise NotImplementedError

class Squire(ABC):
    @abstractmethod
    def name(self) -> str: ...
    @abstractmethod
    def persona(self) -> str: ...
    @abstractmethod
    def history(self) -> List[Message]: ...
    @abstractmethod
    def submit(self, task: str, **kwargs) -> str:
        raise NotImplementedError
