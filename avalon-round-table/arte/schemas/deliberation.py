# arte/schemas/deliberation.py

from typing import List, Dict, TypedDict, Any

class ProposalSchema(TypedDict):
    """A structured proposal from an agent."""
    agent_name: str
    proposal_id: str
    content: str

class CritiqueSchema(TypedDict):
    """A structured critique from one agent to another's proposal."""
    agent_name: str
    target_proposal_id: str
    content: str
    dissent_score: float  # From 0.0 (agreement) to 1.0 (total dissent)

class VerdictSchema(TypedDict):
    """The final synthesized output of the deliberation."""
    synthesized_response: str
    contributing_proposals: List[str]  # List of proposal_ids
    final_dissent_score: float
    full_transcript: List[Dict[str, Any]]
