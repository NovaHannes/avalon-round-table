import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from typing import Dict
from squires.squire_interface import Squire
from squires.file_backed_squire import FileBackedSquire
from squires.dummy_llm import EchoLLM

PERSONAS = {
    "nexus": "You are Sir Nexus, a systems strategist. Be concise and rigorous.",
    "cadmus": "You are Sir Cadmus, a technical architect. Be precise and actionable.",
    "lancelot": "You are Sir Lancelot, a pragmatic tester and challenger.",
}

class OrchestratorDemo:
    def __init__(self):
        self.llm = EchoLLM()
        self.squires: Dict[str, Squire] = {k: FileBackedSquire(k, p, self.llm) for k,p in PERSONAS.items()}

    def assign(self, knight: str, task: str) -> str:
        if knight not in self.squires:
            raise ValueError(f"Unknown knight: {knight}")
        return self.squires[knight].submit(task)

    def roundtable(self, tasks: Dict[str, str]) -> Dict[str, str]:
        return {k: self.assign(k, t) for k, t in tasks.items()}

if __name__ == "__main__":
    orch = OrchestratorDemo()
    demo = {
        "nexus": "Outline Squire responsibilities.",
        "cadmus": "Define the Squire <-> Orchestrator interface surface.",
        "lancelot": "List 3 failure modes to test first.",
    }
    out = orch.roundtable(demo)
    for k,v in out.items():
        print(f"\n[{k.upper()}]\n{v}")
