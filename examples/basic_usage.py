"""
Basic Usage Example
===================

Demonstrates basic usage of the Cosmic OS Constitutional AI Framework.
"""

from cosmic_os import (
    ConstitutionalValidator,
    LocalFirstStorage,
    ZeroKnowledgeEncryption,
    ByzantineConsensus,
    GovernanceProposal,
    RhythmEngine
)
from pathlib import Path
from datetime import datetime


def example_constitutional_validation():
    """Example: Validating operations against constitutional rights"""
    print("=== Constitutional Validation Example ===\n")

    validator = ConstitutionalValidator()

    # Example: Validate privacy compliance
    try:
        result = validator.validate_privacy(
            operation="store_user_data",
            data_access={"user_id": "user123", "data": "sensitive_info"},
            user_consent={"data_storage": True}
        )
        print(f"Privacy validation: {'✓ Compliant' if result.compliant else '✗ Violation'}")
    except NotImplementedError:
        print("Privacy validation: [Pending implementation]")

    print()


def example_local_first_storage():
    """Example: Local-first data storage with optional cloud sync"""
    print("=== Local-First Storage Example ===\n")

    # Initialize with local storage path
    storage = LocalFirstStorage(
        storage_path=Path("./data/local"),
        cloud_sync_enabled=False  # Cloud sync disabled by default
    )

    print("Local-first storage initialized")
    print(f"Storage path: {storage.storage_path}")
    print(f"Cloud sync: {'Enabled (requires consent)' if storage.cloud_sync_enabled else 'Disabled'}")
    print()


def example_zero_knowledge_encryption():
    """Example: Zero-knowledge encryption (client-side only)"""
    print("=== Zero-Knowledge Encryption Example ===\n")

    crypto = ZeroKnowledgeEncryption()

    print("Zero-knowledge encryption initialized")
    print("CRITICAL: All encryption happens CLIENT-SIDE")
    print("Server NEVER sees plaintext or keys")
    print()

    # Example workflow (all client-side)
    user_passphrase = "my-secret-passphrase"  # NEVER transmitted to server
    print(f"1. User enters passphrase (NEVER transmitted): {user_passphrase}")
    print("2. Derive encryption key from passphrase (CLIENT-SIDE)")
    print("3. Encrypt data with key (CLIENT-SIDE)")
    print("4. Transmit only encrypted data to server")
    print("5. Server stores encrypted data (zero knowledge)")
    print()


def example_byzantine_consensus():
    """Example: Democratic governance with 67% consensus"""
    print("=== Byzantine Consensus Example ===\n")

    consensus = ByzantineConsensus()

    print("Byzantine consensus initialized")
    print(f"Threshold: {consensus.threshold.value} (67% supermajority)")
    print(f"Voting period: {consensus.voting_period.days} days")
    print(f"Quorum: {consensus.quorum} (10% minimum participation)")
    print()

    print("Example: Creating a governance proposal")
    proposal = GovernanceProposal(
        title="Add Dark Mode Feature",
        description="Implement dark mode across all UI components",
        proposal_type="feature",
        proposed_by="user123"
    )
    print(f"Proposal created: {proposal.title}")
    print(f"Status: {proposal.status.value}")
    print(f"Proposal ID: {proposal.proposal_id}")
    print()


def example_rhythm_engine():
    """Example: FFT-based rhythm detection"""
    print("=== Rhythm Engine Example ===\n")

    engine = RhythmEngine(
        sample_rate=1.0,
        min_pattern_length=3,
        confidence_threshold=0.7
    )

    print("Rhythm engine initialized")
    print(f"Sample rate: {engine.sample_rate} Hz")
    print(f"Min pattern length: {engine.min_pattern_length}")
    print(f"Confidence threshold: {engine.confidence_threshold}")
    print()

    print("Example: Analyzing daily check-in pattern")
    timestamps = [
        datetime(2025, 10, 1, 9, 0),  # Day 1: 9am
        datetime(2025, 10, 2, 9, 15), # Day 2: 9:15am
        datetime(2025, 10, 3, 8, 45), # Day 3: 8:45am
        datetime(2025, 10, 4, 9, 10), # Day 4: 9:10am
    ]
    print(f"Analyzing {len(timestamps)} timestamps...")
    print("Expected pattern: Daily rhythm around 9am")
    print("[Implementation pending]")
    print()


def example_full_workflow():
    """Example: Complete workflow with all components"""
    print("=== Complete Workflow Example ===\n")

    print("1. Initialize local-first storage")
    storage = LocalFirstStorage(Path("./data"))

    print("2. Initialize zero-knowledge encryption")
    crypto = ZeroKnowledgeEncryption()

    print("3. Initialize constitutional validator")
    validator = ConstitutionalValidator()

    print("4. User creates data locally")
    user_data = "My sensitive rhythm patterns"

    print("5. Validate privacy compliance")
    print("   [Constitutional check: Right to Privacy]")

    print("6. Encrypt data client-side (zero-knowledge)")
    print("   [Server will never see plaintext]")

    print("7. Store encrypted data locally")
    print("   [Local-first: Data on device]")

    print("8. Optional: Sync to cloud (requires explicit consent)")
    print("   [Only if user grants permission]")

    print("\n✓ Complete workflow demonstrates constitutional compliance")
    print()


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Cosmic OS Constitutional AI Framework - Examples")
    print("="*60 + "\n")

    example_constitutional_validation()
    example_local_first_storage()
    example_zero_knowledge_encryption()
    example_byzantine_consensus()
    example_rhythm_engine()
    example_full_workflow()

    print("="*60)
    print("All examples completed!")
    print("Note: Most implementations are stubs pending full development")
    print("="*60 + "\n")
