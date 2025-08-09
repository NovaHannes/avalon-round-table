# arte/core/orchestrator.py

from arte.schemas.deliberation import ProposalSchema, CritiqueSchema, VerdictSchema
from typing import List
import uuid

class Orchestrator:
    def __init__(self, agents):
        self.agents = agents
        self.transcript = []

    def initiate_deliberation(self, topic: str) -> VerdictSchema:
        proposals = []
        for agent in self.agents:
            proposal = agent.generate_proposal(topic)
            proposals.append(proposal)
            self.transcript.append({
                "agent": agent.name,
                "action": "proposal",
                "content": proposal
            })

        critiques = []
        for agent in self.agents:
            agent_critiques = agent.critique_proposals(proposals)
            critiques.extend(agent_critiques)
            for critique in agent_critiques:
                self.transcript.append({
                    "agent": agent.name,
                    "action": "critique",
                    "content": critique
                })

        return self.publish_verdict(proposals, critiques)

    def publish_verdict(self, proposals: List[ProposalSchema], critiques: List[CritiqueSchema]) -> VerdictSchema:
        # Placeholder consensus logic
        synthesized_response = "Consensus not yet implemented."
        contributing_ids = [p["proposal_id"] for p in proposals]
        avg_dissent = sum(c["dissent_score"] for c in critiques) / len(critiques) if critiques else 0.0

        return {
            "synthesized_response": synthesized_response,
            "contributing_proposals": contributing_ids,
            "final_dissent_score": avg_dissent,
            "full_transcript": self.transcript
        }
