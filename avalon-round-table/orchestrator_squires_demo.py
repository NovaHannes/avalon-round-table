import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from typing import Dict
from squires.squire_interface import Squire
from squires.file_backed_squire import FileBackedSquire
from squires.dummy_llm import EchoLLM
from util.personas import load_personas

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "router", "knights_config.yaml")

class OrchestratorDemo:
    def __init__(self):
        self.llm = EchoLLM()
        self.personas: Dict[str, str] = load_personas(CONFIG_PATH)
        self.squires: Dict[str, Squire] = {
            k: FileBackedSquire(k, p, self.llm) for k, p in self.personas.items()
        }

    def assign(self, knight: str, task: str) -> str:
        if knight not in self.squires:
            raise ValueError(f"Unknown knight: {knight}")
        return self.squires[knight].submit(task, budget_tokens=4000)

    def roundtable(self, tasks: Dict[str, str]) -> Dict[str, str]:
        return {k: self.assign(k, t) for k, t in tasks.items()}

if __name__ == "__main__":
    orch = OrchestratorDemo()
    # Build demo tasks for whatever knights were loaded from YAML
    tasks = {k: f"State your primary responsibilities as {k}."
             for k in orch.squires.keys()}
    # Run
    out = orch.roundtable(tasks)
    for k, v in out.items():
        print(f"\n[{k.upper()}]\n{v}")
