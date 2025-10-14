"""
Rhythm Engine Module
====================

FFT-based rhythm analysis and pattern detection.
Implements the Rhythm Interface Protocol (RIP).
"""

from .engine import RhythmEngine, RhythmPattern, RhythmFeatures
from .protocol import RIPMessage, RIPMessageType, RhythmInterfaceProtocol

__all__ = [
    "RhythmEngine",
    "RhythmPattern",
    "RhythmFeatures",
    "RIPMessage",
    "RIPMessageType",
    "RhythmInterfaceProtocol"
]
