# arte/agents/base_agent.py

from arte.schemas.deliberation import ProposalSchema, CritiqueSchema
import uuid
import random
from typing import List, Dict

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def generate_proposal(self, topic: str) -> ProposalSchema:
        return {
            "agent_name": self.name,
            "proposal_id": str(uuid.uuid4()),
            "content": f"{self.name} believes the answer to '{topic}' is YES."
        }

    def critique_proposals(self, proposals: List[ProposalSchema]) -> List[CritiqueSchema]:
        critiques = []
        for proposal in proposals:
            if proposal["agent_name"] != self.name:
                score = random.uniform(0.0, 1.0)
                critiques.append({
                    "agent_name": self.name,
                    "target_proposal_id": proposal["proposal_id"],
                    "content": f"{self.name} critiques proposal by {proposal['agent_name']}.",
                    "dissent_score": round(score, 2)
                })
        return critiques
