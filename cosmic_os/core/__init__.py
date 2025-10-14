"""
Core Constitutional Compliance Module
======================================

Implements the constitutional validation and enforcement mechanisms
defined in Article II (Digital Bill of Rights).
"""

from .validator import ConstitutionalValidator
from .rights import DigitalRight, Article

__all__ = ["ConstitutionalValidator", "DigitalRight", "Article"]
