import json
from arte.agents.agent_interface import AgentInterface
from arte.core.deliberation_engine import run_roundtable
from arte.core.signal_relay import log_event

def load_config(path="data/sample_roundtable_config.json"):
    with open(path, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    config = load_config()
    agents = [AgentInterface(name) for name in config["agents"]]
    result = run_roundtable(agents, config["prompt"])
    log_event(result)
    print("Deliberation complete. Log saved.")
