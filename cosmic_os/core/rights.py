"""
Digital Rights and Constitutional Articles
==========================================

Defines the structure of constitutional rights and articles.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional


class Article(Enum):
    """Constitutional Articles"""
    PREAMBLE = "preamble"
    DIGITAL_BILL_OF_RIGHTS = "article_ii"
    ENFORCEMENT = "article_iii"
    GOVERNANCE = "article_iv"
    AMENDMENT = "article_v"
    SUPREMACY = "article_vi"
    RATIFICATION = "article_vii"


class DigitalRight(Enum):
    """Digital Bill of Rights (Article II)"""
    PRIVACY = "privacy"
    CONSENT = "consent"
    TRANSPARENCY = "transparency"
    SOVEREIGNTY = "sovereignty"
    ACCOUNTABILITY = "accountability"
    REMEDY = "remedy"
    EXIT = "exit"


@dataclass
class RightDefinition:
    """Definition of a constitutional right"""
    right: DigitalRight
    title: str
    description: str
    requirements: List[str]
    enforcement_mechanism: str


# Article II: Digital Bill of Rights Definitions
DIGITAL_RIGHTS_DEFINITIONS = {
    DigitalRight.PRIVACY: RightDefinition(
        right=DigitalRight.PRIVACY,
        title="Right to Privacy",
        description="Users have an absolute right to privacy of their data and communications.",
        requirements=[
            "Local-first data storage by default",
            "Zero-knowledge encryption for all transmitted data",
            "No third-party data sharing without explicit consent",
            "Privacy-by-design architecture"
        ],
        enforcement_mechanism="Constitutional compliance testing in CI/CD"
    ),
    DigitalRight.CONSENT: RightDefinition(
        right=DigitalRight.CONSENT,
        title="Right to Consent",
        description="Users have the right to informed, explicit consent for all data operations.",
        requirements=[
            "Explicit opt-in for all operations",
            "Granular permission controls",
            "Consent can be withdrawn at any time",
            "No implied or default consent"
        ],
        enforcement_mechanism="Consent validation before all operations"
    ),
    DigitalRight.TRANSPARENCY: RightDefinition(
        right=DigitalRight.TRANSPARENCY,
        title="Right to Transparency",
        description="Users have the right to understand how decisions are made.",
        requirements=[
            "Plain-language explanations for all AI decisions",
            "Audit logs accessible to users",
            "Algorithm logic publicly documented",
            "Decision justifications on demand"
        ],
        enforcement_mechanism="Automated transparency reporting"
    ),
    DigitalRight.SOVEREIGNTY: RightDefinition(
        right=DigitalRight.SOVEREIGNTY,
        title="Right to Sovereignty",
        description="Users have absolute sovereignty over their data and digital experience.",
        requirements=[
            "Local-first architecture (cloud optional)",
            "User can override any AI decision",
            "No mandatory cloud dependencies",
            "Data portability guaranteed"
        ],
        enforcement_mechanism="Local-first architecture validation"
    ),
    DigitalRight.ACCOUNTABILITY: RightDefinition(
        right=DigitalRight.ACCOUNTABILITY,
        title="Right to Accountability",
        description="Users have the right to hold systems and decision-makers accountable.",
        requirements=[
            "Clear attribution of all decisions",
            "Appeal mechanism for disputed decisions",
            "Byzantine consensus for governance (67% threshold)",
            "Violation reporting to Cosmic Ethics Council"
        ],
        enforcement_mechanism="Byzantine consensus + CEC oversight"
    ),
    DigitalRight.REMEDY: RightDefinition(
        right=DigitalRight.REMEDY,
        title="Right to Remedy",
        description="Users have the right to remedy when rights are violated.",
        requirements=[
            "30-day cure period for violations",
            "Escalation to Cosmic Ethics Council",
            "Violation tracking and reporting",
            "Enforced remediation or license termination"
        ],
        enforcement_mechanism="CEC arbitration process"
    ),
    DigitalRight.EXIT: RightDefinition(
        right=DigitalRight.EXIT,
        title="Right to Exit",
        description="Users have the unconditional right to exit the system with their data.",
        requirements=[
            "One-click data export in open formats",
            "Complete data deletion on request",
            "No lock-in mechanisms",
            "Lifeboat protocol for framework survival"
        ],
        enforcement_mechanism="Exit functionality compliance testing"
    )
}


def get_right_definition(right: DigitalRight) -> RightDefinition:
    """
    Get the definition of a constitutional right

    Args:
        right: The digital right to look up

    Returns:
        RightDefinition for the specified right
    """
    return DIGITAL_RIGHTS_DEFINITIONS[right]


def get_all_rights() -> List[RightDefinition]:
    """
    Get all digital rights definitions

    Returns:
        List of all RightDefinitions
    """
    return list(DIGITAL_RIGHTS_DEFINITIONS.values())
