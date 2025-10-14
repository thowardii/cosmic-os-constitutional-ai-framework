"""
Tests for Byzantine Consensus
==============================
"""

import pytest
from datetime import datetime, timedelta
from decimal import Decimal
from cosmic_os.governance import (
    ByzantineConsensus,
    ConsensusThreshold,
    Vote,
    VoteType,
    GovernanceProposal,
    ProposalStatus,
    ProposalType
)


class TestByzantineConsensus:
    """Test suite for Byzantine consensus"""

    def setup_method(self):
        """Setup test fixtures"""
        self.consensus = ByzantineConsensus(
            threshold=ConsensusThreshold.SUPERMAJORITY,
            voting_period=timedelta(days=7)
        )

    def test_consensus_initialization(self):
        """Test consensus initializes with 67% threshold"""
        assert self.consensus.threshold == ConsensusThreshold.SUPERMAJORITY
        assert self.consensus.threshold.value == Decimal("0.67")
        assert self.consensus.voting_period == timedelta(days=7)
        assert self.consensus.quorum == Decimal("0.10")

    @pytest.mark.skip(reason="Implementation pending")
    def test_cast_vote_yes(self):
        """Test casting a YES vote"""
        success = self.consensus.cast_vote(
            proposal_id="proposal_1",
            voter_id="voter_1",
            vote_type=VoteType.YES,
            reasoning="I support this proposal"
        )
        assert success is True

    @pytest.mark.skip(reason="Implementation pending")
    def test_cast_vote_duplicate_rejected(self):
        """Test duplicate votes are rejected"""
        # First vote succeeds
        self.consensus.cast_vote(
            proposal_id="proposal_1",
            voter_id="voter_1",
            vote_type=VoteType.YES
        )

        # Second vote from same user fails
        success = self.consensus.cast_vote(
            proposal_id="proposal_1",
            voter_id="voter_1",
            vote_type=VoteType.NO
        )
        assert success is False

    @pytest.mark.skip(reason="Implementation pending")
    def test_calculate_consensus_passes(self):
        """Test consensus calculation when proposal passes"""
        # Cast 67 YES votes, 33 NO votes (67% yes)
        for i in range(67):
            self.consensus.cast_vote(
                proposal_id="proposal_1",
                voter_id=f"voter_{i}",
                vote_type=VoteType.YES
            )

        for i in range(67, 100):
            self.consensus.cast_vote(
                proposal_id="proposal_1",
                voter_id=f"voter_{i}",
                vote_type=VoteType.NO
            )

        eligible_voters = set(f"voter_{i}" for i in range(100))
        result = self.consensus.calculate_consensus("proposal_1", eligible_voters)

        assert result.passed is True
        assert result.yes_percentage >= Decimal("0.67")
        assert result.threshold_met is True

    @pytest.mark.skip(reason="Implementation pending")
    def test_calculate_consensus_fails(self):
        """Test consensus calculation when proposal fails"""
        # Cast 66 YES votes, 34 NO votes (66% yes - below threshold)
        for i in range(66):
            self.consensus.cast_vote(
                proposal_id="proposal_1",
                voter_id=f"voter_{i}",
                vote_type=VoteType.YES
            )

        for i in range(66, 100):
            self.consensus.cast_vote(
                proposal_id="proposal_1",
                voter_id=f"voter_{i}",
                vote_type=VoteType.NO
            )

        eligible_voters = set(f"voter_{i}" for i in range(100))
        result = self.consensus.calculate_consensus("proposal_1", eligible_voters)

        assert result.passed is False
        assert result.yes_percentage < Decimal("0.67")
        assert result.threshold_met is False

    @pytest.mark.skip(reason="Implementation pending")
    def test_quorum_not_met(self):
        """Test consensus fails if quorum not met"""
        # Only 5 votes out of 1000 eligible (0.5% < 10% quorum)
        for i in range(5):
            self.consensus.cast_vote(
                proposal_id="proposal_1",
                voter_id=f"voter_{i}",
                vote_type=VoteType.YES
            )

        eligible_voters = set(f"voter_{i}" for i in range(1000))
        result = self.consensus.calculate_consensus("proposal_1", eligible_voters)

        assert result.passed is False

    def test_voting_period_open(self):
        """Test voting period is open within timeframe"""
        created_at = datetime.utcnow() - timedelta(days=3)
        is_open = self.consensus.is_voting_open("proposal_1", created_at)
        assert is_open is True

    def test_voting_period_closed(self):
        """Test voting period is closed after timeframe"""
        created_at = datetime.utcnow() - timedelta(days=8)
        is_open = self.consensus.is_voting_open("proposal_1", created_at)
        assert is_open is False


class TestGovernanceProposal:
    """Test suite for governance proposals"""

    def test_proposal_creation(self):
        """Test creating a governance proposal"""
        proposal = GovernanceProposal(
            title="Test Proposal",
            description="A test proposal",
            proposal_type=ProposalType.FEATURE,
            proposed_by="user123"
        )

        assert proposal.title == "Test Proposal"
        assert proposal.status == ProposalStatus.DRAFT
        assert proposal.proposal_id is not None
        assert proposal.created_at is not None

    def test_proposal_to_dict(self):
        """Test proposal serialization"""
        proposal = GovernanceProposal(
            title="Test",
            description="Test",
            proposal_type=ProposalType.POLICY,
            proposed_by="user123"
        )

        data = proposal.to_dict()
        assert data["title"] == "Test"
        assert data["proposal_type"] == "policy"
        assert data["status"] == "draft"

    @pytest.mark.skip(reason="Implementation pending")
    def test_start_voting(self):
        """Test starting voting period"""
        proposal = GovernanceProposal(
            title="Test",
            description="Test",
            proposal_type=ProposalType.FEATURE,
            proposed_by="user123"
        )

        proposal.start_voting(voting_period_days=7)

        assert proposal.status == ProposalStatus.VOTING
        assert proposal.voting_started_at is not None
        assert proposal.voting_ends_at is not None

    def test_mark_implemented(self):
        """Test marking proposal as implemented"""
        proposal = GovernanceProposal(
            title="Test",
            description="Test",
            proposal_type=ProposalType.FEATURE,
            proposed_by="user123",
            status=ProposalStatus.PASSED
        )

        proposal.mark_implemented()
        assert proposal.status == ProposalStatus.IMPLEMENTED

    def test_mark_implemented_not_passed_raises_error(self):
        """Test marking non-passed proposal as implemented raises error"""
        proposal = GovernanceProposal(
            title="Test",
            description="Test",
            proposal_type=ProposalType.FEATURE,
            proposed_by="user123",
            status=ProposalStatus.DRAFT
        )

        with pytest.raises(ValueError):
            proposal.mark_implemented()
