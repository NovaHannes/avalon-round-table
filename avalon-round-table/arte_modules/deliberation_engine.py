from arte_modules.agent_interface import AgentInterface
from arte_modules.concord import assess_concord

def run_roundtable(agents, prompt):
    responses = [agent.deliberate(prompt) for agent in agents]
    concord = assess_concord(responses)
    return {"responses": responses, "concord": concord}
