import random
from arte.schemas.deliberation import ProposalSchema, CritiqueSchema

class AgentInterface:
    def __init__(self, name: str):
        self.name = name

    def generate_proposal(self, topic: str) -> ProposalSchema:
        content = f"My suggestion on '{topic}' is to prioritize ethical AI governance."
        return ProposalSchema(
            proposal_id=f"{self.name}-proposal",
            agent_name=self.name,
            content=content
        )

    def critique_proposals(self, proposals: list[ProposalSchema]) -> list[CritiqueSchema]:
        critiques = []
        for proposal in proposals:
            if proposal.agent_name != self.name:
                critique = CritiqueSchema(
                    proposal_id=proposal.proposal_id,
                    agent_name=self.name,
                    content=f"{self.name} thinks this needs clarification.",
                    dissent_score=random.uniform(0, 1)
                )
                critiques.append(critique)
        return critiques
