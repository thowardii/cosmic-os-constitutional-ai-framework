"""
Cosmic OS Constitutional AI Framework
======================================

A constitutional AI governance framework implementing:
- Local-first architecture
- Zero-knowledge encryption
- Byzantine consensus governance
- Democratic accountability
- User sovereignty

License: MIT with Constitutional Compliance Requirement
See LICENSE file for details.
"""

__version__ = "1.0.0"
__author__ = "Cosmic OS Community"

from .core import ConstitutionalValidator, Article, DigitalRight
from .storage import LocalFirstStorage
from .crypto import ZeroKnowledgeEncryption
from .governance import ByzantineConsensus, GovernanceProposal
from .rhythm import RhythmEngine, RhythmPattern

__all__ = [
    "ConstitutionalValidator",
    "Article",
    "DigitalRight",
    "LocalFirstStorage",
    "ZeroKnowledgeEncryption",
    "ByzantineConsensus",
    "GovernanceProposal",
    "RhythmEngine",
    "RhythmPattern",
]
