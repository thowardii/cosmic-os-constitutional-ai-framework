"""
Byzantine Consensus Governance Module
======================================

Implements democratic governance using Byzantine consensus
with 67% threshold for decision-making.
"""

from .consensus import (
    ByzantineConsensus,
    ConsensusThreshold,
    Vote,
    VoteType
)
from .proposal import (
    GovernanceProposal,
    ProposalStatus,
    ProposalType
)

__all__ = [
    "ByzantineConsensus",
    "ConsensusThreshold",
    "Vote",
    "VoteType",
    "GovernanceProposal",
    "ProposalStatus",
    "ProposalType"
]
