from arte.core.orchestrator import Orchestrator
from arte.agents.agent_interface import AgentInterface  # if needed

def run_roundtable(agents, topic):
    orchestrator = Orchestrator(agents)
    verdict = orchestrator.initiate_deliberation(topic)
    return verdict
