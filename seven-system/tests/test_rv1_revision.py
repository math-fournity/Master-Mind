"""WP-RV1 P8 NO_CHANGE/Revision 测试。

测试层级：ProvenanceSnapshot → FailureLocalization → NoChangeDecision →
          RevisionProposal → HoldoutConsumption → CandidateRelease →
          ProspectiveEvaluation → RevisionPolicy → EvidenceImmutability →
          CapabilityReport → Negative → Determinism → Boundary → Constants
覆盖：
- Golden path NO_CHANGE: ProvenanceSnapshot → FailureLocalization →
  NoChangeDecision (signed, holdout not unsealed)
- Golden path CONTROLLED_REVISION: ProvenanceSnapshot → FailureLocalization →
  RevisionProposal → CandidateRelease → ProspectiveEvaluation → two HumanGate
- Holdout consumption tracking
- Negative: EvidenceIndex read in P8, fit=confirmation, holdout repeated peek,
  single-case split, candidate self-approved, old evidence modified,
  NoChange unseals holdout, revision without two gates, ProvenanceSnapshot
  not readonly, localization incomplete, unsigned decisions
- Evidence immutability tests
- Deterministic hash tests
- RV1 boundary tests (allowed/forbidden output kinds — EvidenceIndex FORBIDDEN in P8)
- All constants verified

所有 blocker test 失败 → 工作包 FAIL。
"""

from __future__ import annotations

import dataclasses
import hashlib
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import (
    RV_ALLOWED_OUTPUT_KINDS,
    RV_CANDIDATE_STATES,
    RV_CHECK_IDS,
    RV_CLAIMS,
    RV_FORBIDDEN_OUTPUT_KINDS,
    RV_HOLDOUT_STATUSES,
    RV_LOCALIZATION_LAYERS,
    RV_NOCHANGE_STATES,
    RV_NONCLAIMS,
    RV_PROSPECTIVE_STATES,
    RV_REVISION_PROPOSAL_STATES,
    RV_REVISION_STATES,
    RV_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.revision.provenance import (
    ProvenanceSnapshot,
    make_provenance_snapshot,
    verify_provenance_snapshot,
    check_provenance_readonly,
    check_no_evidence_index_in_provenance,
)
from seven_system.revision.localization import (
    FailureLocalization,
    make_failure_localization,
    verify_failure_localization,
)
from seven_system.revision.no_change import (
    NoChangeDecision,
    make_no_change_decision,
    verify_no_change_decision,
    check_nochange_does_not_unseal_holdout,
)
from seven_system.revision.revision_proposal import (
    RevisionProposal,
    make_revision_proposal,
    verify_revision_proposal,
    check_revision_two_human_gates,
)
from seven_system.revision.holdout import (
    HoldoutView,
    HoldoutConsumption,
    make_holdout_consumption,
    verify_holdout_consumption,
    record_holdout_view,
    check_fit_not_confirmation,
    check_no_repeated_peek,
    check_no_single_case_split,
)
from seven_system.revision.candidate import (
    CandidateRelease,
    make_candidate_release,
    verify_candidate_release,
    check_candidate_not_self_approved,
)
from seven_system.revision.prospective import (
    ProspectiveEvaluation,
    make_prospective_evaluation,
    verify_prospective_evaluation,
    check_prospective_one_time,
    check_prospective_no_reuse_viewed_holdout,
)
from seven_system.revision.policy import (
    RevisionPolicy,
    make_revision_policy,
    verify_revision_policy,
)
from seven_system.revision.immutability import (
    check_old_evidence_not_modified,
    check_evidence_immutability,
)
from seven_system.revision.boundary import (
    check_no_evidence_index_in_p8,
    check_p8_output_boundary,
)
from seven_system.revision.capability_report import (
    RevisionCapabilityReportError,
    build_revision_capability_report,
    verify_revision_capability_report,
    REVISION_REPORT_SCHEMA_VERSION,
    REVISION_REPORT_SCOPE,
)


# ─── helpers ────────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64
_TS = "2026-08-14T12:00:00Z"


def _hash(value: object) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _make_record_hashes(n: int = 3) -> list[str]:
    return [_hash(f"record-{i:03d}") for i in range(n)]


def _make_provenance_snapshot(
    snapshot_id: str = "snap-001",
    record_hashes: list[str] | None = None,
) -> ProvenanceSnapshot:
    hashes = _make_record_hashes() if record_hashes is None else record_hashes
    root_hash = hashlib.sha256(canonical_json_bytes(sorted(hashes))).hexdigest()
    return make_provenance_snapshot(
        snapshot_id=snapshot_id,
        plan_id="plan-001",
        evidence_seal_hash=_hash("seal-001"),
        evidence_seal_root_hash=root_hash,
        record_hashes=hashes,
        lineage=[{"stage": "P7", "seal_hash": _hash("seal-001")}],
        frozen_at=_TS,
    )


def _make_localization(
    localization_id: str = "loc-001",
    failed_layer: str = "SELECTOR",
    snapshot_hash: str = "",
) -> FailureLocalization:
    return make_failure_localization(
        localization_id=localization_id,
        provenance_snapshot_hash=snapshot_hash or _hash("snap-001"),
        failed_layer=failed_layer,
        evidence_refs=[_hash("record-000")],
        diagnosis="selector chose wrong arm",
        localized_at=_TS,
    )


def _make_signed_nochange(
    decision_id: str = "nc-001",
    snapshot_hash: str = "",
    localization_hash: str = "",
) -> NoChangeDecision:
    return make_no_change_decision(
        decision_id=decision_id,
        provenance_snapshot_hash=snapshot_hash or _hash("snap-001"),
        localization_hash=localization_hash or _hash("loc-001"),
        rationale="evidence supports causal claim, no revision needed",
        signed=True,
        gate_decision_ref={"decision_id": "gate-dec-001", "decision_hash": _hash("gate-dec-001")},
        decided_at=_TS,
    )


def _make_revision_proposal(
    proposal_id: str = "rev-001",
    snapshot_hash: str = "",
    localization_hash: str = "",
    signed: bool = True,
    gate_count: int = 2,
) -> RevisionProposal:
    gates = [
        {"decision_id": f"gate-dec-{i:03d}", "decision_hash": _hash(f"gate-dec-{i:03d}")}
        for i in range(gate_count)
    ]
    return make_revision_proposal(
        proposal_id=proposal_id,
        provenance_snapshot_hash=snapshot_hash or _hash("snap-001"),
        localization_hash=localization_hash or _hash("loc-001"),
        what_to_change="replace selector with stratified version",
        fit_regression_plan="fit on holdout-A, regression on holdout-B",
        candidate_freeze_ref={"candidate_id": "cand-001", "content_hash": _hash("cand-001")},
        prospective_ref={"prospective_id": "pros-001", "content_hash": _hash("pros-001")},
        signed=signed,
        gate_decision_refs=gates,
        proposed_at=_TS,
    )


def _make_candidate(
    candidate_id: str = "cand-001",
    proposal_hash: str = "",
    frozen: bool = True,
    creator_actor_id: str = "human-architect-001",
    approver_actor_id: str = "human-reviewer-001",
) -> CandidateRelease:
    return make_candidate_release(
        candidate_id=candidate_id,
        revision_proposal_hash=proposal_hash or _hash("rev-001"),
        candidate_artifact_ref={"artifact_id": "artifact-001", "content_hash": _hash("artifact-001")},
        creator_actor_id=creator_actor_id,
        frozen=frozen,
        approver_actor_id=approver_actor_id,
        frozen_at=_TS,
    )


def _make_prospective(
    prospective_id: str = "pros-001",
    candidate_hash: str = "",
    confirmed: bool = True,
    reused_viewed_holdout: bool = False,
) -> ProspectiveEvaluation:
    return make_prospective_evaluation(
        prospective_id=prospective_id,
        candidate_release_hash=candidate_hash or _hash("cand-001"),
        holdout_view_ref={"view_id": "view-001", "holdout_id": "holdout-C"},
        confirmed=confirmed,
        reused_viewed_holdout=reused_viewed_holdout,
        evaluated_at=_TS,
    )


def _make_policy(policy_id: str = "pol-001") -> RevisionPolicy:
    return make_revision_policy(
        policy_id=policy_id,
        frozen=True,
        frozen_at=_TS,
    )


# ─── ProvenanceSnapshot tests ───────────────────────────────────────────


class TestProvenanceSnapshot(unittest.TestCase):
    """ProvenanceSnapshot 测试。"""

    def test_snapshot_passes_verification(self):
        snap = _make_provenance_snapshot()
        result = verify_provenance_snapshot(snap)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(snap.is_hash_valid)
        self.assertTrue(snap.is_readonly)

    def test_snapshot_readonly_flag(self):
        snap = _make_provenance_snapshot()
        self.assertTrue(snap.readonly)
        check = check_provenance_readonly(snap)
        self.assertTrue(check.passed)

    def test_snapshot_not_readonly_blocks(self):
        snap = _make_provenance_snapshot()
        bad = dataclasses.replace(snap, readonly=False, content_hash="")
        bad = dataclasses.replace(bad, content_hash=bad.compute_content_hash())
        result = verify_provenance_snapshot(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROVENANCE_SNAPSHOT_NOT_READONLY, result.error_codes)

    def test_snapshot_references_evidence_index_blocks(self):
        snap = _make_provenance_snapshot()
        bad = dataclasses.replace(
            snap,
            lineage=tuple(list(snap.lineage) + [{"stage": "P9", "ref": "EvidenceIndex"}]),
            content_hash="",
        )
        bad = dataclasses.replace(bad, content_hash=bad.compute_content_hash())
        result = verify_provenance_snapshot(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_EVIDENCE_INDEX_READ_IN_P8, result.error_codes)

    def test_snapshot_incomplete_no_records_blocks(self):
        snap = _make_provenance_snapshot(record_hashes=[])
        result = verify_provenance_snapshot(snap)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROVENANCE_SNAPSHOT_INCOMPLETE, result.error_codes)

    def test_snapshot_incomplete_no_seal_hash_blocks(self):
        hashes = _make_record_hashes()
        root_hash = hashlib.sha256(canonical_json_bytes(sorted(hashes))).hexdigest()
        snap = make_provenance_snapshot(
            snapshot_id="snap-001",
            plan_id="plan-001",
            evidence_seal_hash="",
            evidence_seal_root_hash=root_hash,
            record_hashes=hashes,
            frozen_at=_TS,
        )
        result = verify_provenance_snapshot(snap)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROVENANCE_SNAPSHOT_INCOMPLETE, result.error_codes)

    def test_snapshot_root_hash_mismatch_blocks(self):
        snap = _make_provenance_snapshot()
        bad = dataclasses.replace(snap, evidence_seal_root_hash=_ZERO_HASH, content_hash="")
        bad = dataclasses.replace(bad, content_hash=bad.compute_content_hash())
        result = verify_provenance_snapshot(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROVENANCE_SNAPSHOT_HASH_MISMATCH, result.error_codes)

    def test_snapshot_hash_mismatch_blocks(self):
        snap = _make_provenance_snapshot()
        bad = dataclasses.replace(snap, content_hash="deadbeef" + "0" * 56)
        result = verify_provenance_snapshot(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROVENANCE_SNAPSHOT_HASH_MISMATCH, result.error_codes)

    def test_snapshot_record_count_consistency(self):
        snap = _make_provenance_snapshot()
        self.assertEqual(snap.record_count, len(snap.record_hashes))


# ─── FailureLocalization tests ──────────────────────────────────────────


class TestFailureLocalization(unittest.TestCase):
    """FailureLocalization 测试。"""

    def test_localization_passes_verification(self):
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        result = verify_failure_localization(loc)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(loc.is_hash_valid)

    def test_localization_all_layers_valid(self):
        snap = _make_provenance_snapshot()
        for layer in RV_LOCALIZATION_LAYERS:
            loc = _make_localization(failed_layer=layer, snapshot_hash=snap.content_hash)
            result = verify_failure_localization(loc)
            self.assertTrue(result.passed, msg=f"layer {layer}: {result.details}")

    def test_localization_invalid_layer_blocks(self):
        loc = FailureLocalization(
            localization_id="loc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            failed_layer="INVALID_LAYER",
            evidence_refs=(_hash("record-000"),),
            localized_at=_TS,
            content_hash="",
        )
        loc = dataclasses.replace(loc, content_hash=loc.compute_content_hash())
        result = verify_failure_localization(loc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_LOCALIZATION_LAYER_INVALID, result.error_codes)

    def test_localization_make_rejects_invalid_layer(self):
        with self.assertRaises(ValueError):
            make_failure_localization(
                localization_id="loc-bad",
                provenance_snapshot_hash=_hash("snap-001"),
                failed_layer="INVALID_LAYER",
                evidence_refs=[_hash("record-000")],
            )

    def test_localization_incomplete_no_evidence_refs_blocks(self):
        loc = FailureLocalization(
            localization_id="loc-002",
            provenance_snapshot_hash=_hash("snap-001"),
            failed_layer="CORE",
            evidence_refs=(),
            localized_at=_TS,
            content_hash="",
        )
        loc = dataclasses.replace(loc, content_hash=loc.compute_content_hash())
        result = verify_failure_localization(loc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_FAILURE_LOCALIZATION_INCOMPLETE, result.error_codes)

    def test_localization_incomplete_no_snapshot_hash_blocks(self):
        loc = FailureLocalization(
            localization_id="loc-003",
            provenance_snapshot_hash="",
            failed_layer="CORE",
            evidence_refs=(_hash("record-000"),),
            localized_at=_TS,
            content_hash="",
        )
        loc = dataclasses.replace(loc, content_hash=loc.compute_content_hash())
        result = verify_failure_localization(loc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_FAILURE_LOCALIZATION_INCOMPLETE, result.error_codes)

    def test_localization_references_evidence_index_blocks(self):
        loc = FailureLocalization(
            localization_id="loc-004",
            provenance_snapshot_hash=_hash("snap-001"),
            failed_layer="CORE",
            evidence_refs=("EvidenceIndex",),
            localized_at=_TS,
            content_hash="",
        )
        loc = dataclasses.replace(loc, content_hash=loc.compute_content_hash())
        result = verify_failure_localization(loc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_LOCALIZATION_REFERENCES_EVIDENCE_INDEX, result.error_codes)

    def test_localization_hash_mismatch_blocks(self):
        loc = _make_localization()
        bad = dataclasses.replace(loc, content_hash="deadbeef" + "0" * 56)
        result = verify_failure_localization(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_LOCALIZATION_HASH_MISMATCH, result.error_codes)


# ─── NoChangeDecision tests ─────────────────────────────────────────────


class TestNoChangeDecision(unittest.TestCase):
    """NoChangeDecision 测试。"""

    def test_signed_nochange_passes_verification(self):
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        nc = _make_signed_nochange(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        result = verify_no_change_decision(nc)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(nc.is_hash_valid)
        self.assertFalse(nc.holdout_unsealed)

    def test_nochange_does_not_unseal_holdout(self):
        nc = _make_signed_nochange()
        check = check_nochange_does_not_unseal_holdout(nc)
        self.assertTrue(check.passed)
        self.assertFalse(nc.holdout_unsealed)

    def test_unsigned_nochange_blocks(self):
        nc = make_no_change_decision(
            decision_id="nc-unsigned",
            provenance_snapshot_hash=_hash("snap-001"),
            localization_hash=_hash("loc-001"),
            rationale="no revision needed",
            signed=False,
            decided_at=_TS,
        )
        result = verify_no_change_decision(nc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_NOCHANGE_NOT_SIGNED, result.error_codes)

    def test_signed_nochange_without_gate_ref_blocks(self):
        nc = NoChangeDecision(
            decision_id="nc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            localization_hash=_hash("loc-001"),
            state="SIGNED",
            rationale="no revision",
            signed=True,
            gate_decision_ref={},
            holdout_unsealed=False,
            decided_at=_TS,
            content_hash="",
        )
        nc = dataclasses.replace(nc, content_hash=nc.compute_content_hash())
        result = verify_no_change_decision(nc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_NOCHANGE_NOT_SIGNED, result.error_codes)

    def test_nochange_unseals_holdout_blocks(self):
        nc = NoChangeDecision(
            decision_id="nc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            localization_hash=_hash("loc-001"),
            state="SIGNED",
            rationale="no revision",
            signed=True,
            gate_decision_ref={"decision_id": "gate-001", "decision_hash": _hash("gate-001")},
            holdout_unsealed=True,
            decided_at=_TS,
            content_hash="",
        )
        nc = dataclasses.replace(nc, content_hash=nc.compute_content_hash())
        result = verify_no_change_decision(nc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_NOCHANGE_UNSEALS_HOLDOUT, result.error_codes)

    def test_nochange_state_invalid_blocks(self):
        nc = NoChangeDecision(
            decision_id="nc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            localization_hash=_hash("loc-001"),
            state="INVALID_STATE",
            rationale="no revision",
            signed=True,
            gate_decision_ref={"decision_id": "gate-001", "decision_hash": _hash("gate-001")},
            holdout_unsealed=False,
            decided_at=_TS,
            content_hash="",
        )
        nc = dataclasses.replace(nc, content_hash=nc.compute_content_hash())
        result = verify_no_change_decision(nc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_NOCHANGE_STATE_INVALID, result.error_codes)

    def test_nochange_references_evidence_index_blocks(self):
        nc = NoChangeDecision(
            decision_id="nc-bad",
            provenance_snapshot_hash="EvidenceIndex",
            localization_hash=_hash("loc-001"),
            state="SIGNED",
            rationale="no revision",
            signed=True,
            gate_decision_ref={"decision_id": "gate-001", "decision_hash": _hash("gate-001")},
            holdout_unsealed=False,
            decided_at=_TS,
            content_hash="",
        )
        nc = dataclasses.replace(nc, content_hash=nc.compute_content_hash())
        result = verify_no_change_decision(nc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_NOCHANGE_REFERENCES_EVIDENCE_INDEX, result.error_codes)

    def test_nochange_hash_mismatch_blocks(self):
        nc = _make_signed_nochange()
        bad = dataclasses.replace(nc, content_hash="deadbeef" + "0" * 56)
        result = verify_no_change_decision(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_NOCHANGE_HASH_MISMATCH, result.error_codes)


# ─── RevisionProposal tests ─────────────────────────────────────────────


class TestRevisionProposal(unittest.TestCase):
    """RevisionProposal 测试。"""

    def test_signed_proposal_with_two_gates_passes(self):
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        prop = _make_revision_proposal(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        result = verify_revision_proposal(prop)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(prop.is_hash_valid)
        self.assertEqual(prop.gate_count, 2)

    def test_revision_two_gates_check(self):
        prop = _make_revision_proposal()
        check = check_revision_two_human_gates(prop)
        self.assertTrue(check.passed)

    def test_unsigned_proposal_blocks(self):
        prop = _make_revision_proposal(signed=False, gate_count=2)
        result = verify_revision_proposal(prop)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_PROPOSAL_NOT_SIGNED, result.error_codes)

    def test_proposal_without_two_gates_blocks(self):
        prop = _make_revision_proposal(signed=True, gate_count=1)
        result = verify_revision_proposal(prop)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_WITHOUT_TWO_GATES, result.error_codes)
        self.assertIn(EC.RV_REVISION_GATE_COUNT_INSUFFICIENT, result.error_codes)

    def test_proposal_with_zero_gates_blocks(self):
        prop = _make_revision_proposal(signed=True, gate_count=0)
        result = verify_revision_proposal(prop)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_WITHOUT_TWO_GATES, result.error_codes)

    def test_proposal_state_invalid_blocks(self):
        prop = NoChangeDecision = RevisionProposal(
            proposal_id="rev-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            localization_hash=_hash("loc-001"),
            what_to_change="change selector",
            fit_regression_plan="fit/regression",
            state="INVALID_STATE",
            signed=True,
            gate_decision_refs=(
                {"decision_id": "g1", "decision_hash": _hash("g1")},
                {"decision_id": "g2", "decision_hash": _hash("g2")},
            ),
            proposed_at=_TS,
            content_hash="",
        )
        prop = dataclasses.replace(prop, content_hash=prop.compute_content_hash())
        result = verify_revision_proposal(prop)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_PROPOSAL_STATE_INVALID, result.error_codes)

    def test_proposal_references_evidence_index_blocks(self):
        prop = RevisionProposal(
            proposal_id="rev-bad",
            provenance_snapshot_hash="EvidenceIndex",
            localization_hash=_hash("loc-001"),
            what_to_change="change",
            fit_regression_plan="plan",
            state="TWO_GATE_APPROVED",
            signed=True,
            gate_decision_refs=(
                {"decision_id": "g1", "decision_hash": _hash("g1")},
                {"decision_id": "g2", "decision_hash": _hash("g2")},
            ),
            proposed_at=_TS,
            content_hash="",
        )
        prop = dataclasses.replace(prop, content_hash=prop.compute_content_hash())
        result = verify_revision_proposal(prop)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_REFERENCES_EVIDENCE_INDEX, result.error_codes)

    def test_proposal_hash_mismatch_blocks(self):
        prop = _make_revision_proposal()
        bad = dataclasses.replace(prop, content_hash="deadbeef" + "0" * 56)
        result = verify_revision_proposal(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_PROPOSAL_HASH_MISMATCH, result.error_codes)


# ─── HoldoutConsumption tests ───────────────────────────────────────────


class TestHoldoutConsumption(unittest.TestCase):
    """HoldoutConsumption 测试。"""

    def test_valid_consumption_passes(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001", "case-002"),
                viewed_at=_TS,
                status="VIEWED",
            ),
            HoldoutView(
                view_id="view-002",
                holdout_id="holdout-B",
                purpose="CONFIRMATION",
                case_ids=("case-003",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-001",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        result = verify_holdout_consumption(hc)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertIn("holdout-A", hc.consumed_holdout_ids)
        self.assertIn("holdout-B", hc.consumed_holdout_ids)

    def test_viewed_immediately_consumed(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-001",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        self.assertIn("holdout-A", hc.consumed_holdout_ids)

    def test_record_holdout_view_appends(self):
        hc = make_holdout_consumption(
            consumption_id="hc-001",
            provenance_snapshot_hash=_hash("snap-001"),
            views=[],
        )
        view = HoldoutView(
            view_id="view-001",
            holdout_id="holdout-A",
            purpose="FIT",
            case_ids=("case-001",),
            viewed_at=_TS,
            status="VIEWED",
        )
        hc2 = record_holdout_view(hc, view)
        self.assertEqual(len(hc2.views), 1)
        self.assertIn("holdout-A", hc2.consumed_holdout_ids)

    def test_fit_equals_confirmation_blocks(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
            HoldoutView(
                view_id="view-002",
                holdout_id="holdout-B",
                purpose="CONFIRMATION",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        result = verify_holdout_consumption(hc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_FIT_EQUALS_CONFIRMATION, result.error_codes)

    def test_fit_not_confirmation_check(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
            HoldoutView(
                view_id="view-002",
                holdout_id="holdout-B",
                purpose="CONFIRMATION",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        check = check_fit_not_confirmation(hc)
        self.assertFalse(check.passed)

    def test_single_case_split_blocks(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
            HoldoutView(
                view_id="view-002",
                holdout_id="holdout-B",
                purpose="TEST",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        result = verify_holdout_consumption(hc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_SINGLE_CASE_SPLIT, result.error_codes)

    def test_no_single_case_split_check(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
            HoldoutView(
                view_id="view-002",
                holdout_id="holdout-B",
                purpose="TEST",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        check = check_no_single_case_split(hc)
        self.assertFalse(check.passed)

    def test_repeated_peek_blocks(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
            HoldoutView(
                view_id="view-002",
                holdout_id="holdout-A",
                purpose="CONFIRMATION",
                case_ids=("case-002",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        result = verify_holdout_consumption(hc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_HOLDOUT_REPEATED_PEEK, result.error_codes)

    def test_no_repeated_peek_check(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="VIEWED",
            ),
            HoldoutView(
                view_id="view-002",
                holdout_id="holdout-A",
                purpose="CONFIRMATION",
                case_ids=("case-002",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        check = check_no_repeated_peek(hc)
        self.assertFalse(check.passed)

    def test_holdout_status_invalid_blocks(self):
        views = [
            HoldoutView(
                view_id="view-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001",),
                viewed_at=_TS,
                status="INVALID_STATUS",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-bad",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        result = verify_holdout_consumption(hc)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_HOLDOUT_STATUS_INVALID, result.error_codes)

    def test_holdout_hash_mismatch_blocks(self):
        hc = _make_valid_holdout_consumption()
        bad = dataclasses.replace(hc, content_hash="deadbeef" + "0" * 56)
        result = verify_holdout_consumption(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_HOLDOUT_CONSUMPTION_HASH_MISMATCH, result.error_codes)


def _make_valid_holdout_consumption() -> HoldoutConsumption:
    views = [
        HoldoutView(
            view_id="view-001",
            holdout_id="holdout-A",
            purpose="FIT",
            case_ids=("case-001", "case-002"),
            viewed_at=_TS,
            status="VIEWED",
        ),
        HoldoutView(
            view_id="view-002",
            holdout_id="holdout-B",
            purpose="CONFIRMATION",
            case_ids=("case-003",),
            viewed_at=_TS,
            status="VIEWED",
        ),
    ]
    return make_holdout_consumption(
        consumption_id="hc-001",
        provenance_snapshot_hash=_hash("snap-001"),
        views=views,
    )


# ─── CandidateRelease tests ─────────────────────────────────────────────


class TestCandidateRelease(unittest.TestCase):
    """CandidateRelease 测试。"""

    def test_frozen_candidate_passes(self):
        cand = _make_candidate()
        result = verify_candidate_release(cand)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(cand.is_hash_valid)
        self.assertTrue(cand.frozen)

    def test_candidate_not_self_approved_check(self):
        cand = _make_candidate()
        check = check_candidate_not_self_approved(cand)
        self.assertTrue(check.passed)

    def test_unfrozen_candidate_blocks(self):
        cand = _make_candidate(frozen=False)
        result = verify_candidate_release(cand)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_CANDIDATE_NOT_FROZEN, result.error_codes)

    def test_candidate_self_approved_blocks(self):
        cand = make_candidate_release(
            candidate_id="cand-bad",
            revision_proposal_hash=_hash("rev-001"),
            candidate_artifact_ref={"artifact_id": "a-001", "content_hash": _hash("a-001")},
            creator_actor_id="human-001",
            frozen=True,
            approver_actor_id="human-001",
            frozen_at=_TS,
        )
        result = verify_candidate_release(cand)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_CANDIDATE_SELF_APPROVED, result.error_codes)

    def test_candidate_self_approved_check_blocks(self):
        cand = make_candidate_release(
            candidate_id="cand-bad",
            revision_proposal_hash=_hash("rev-001"),
            candidate_artifact_ref={"artifact_id": "a-001", "content_hash": _hash("a-001")},
            creator_actor_id="human-001",
            frozen=True,
            approver_actor_id="human-001",
            frozen_at=_TS,
        )
        check = check_candidate_not_self_approved(cand)
        self.assertFalse(check.passed)

    def test_candidate_state_invalid_blocks(self):
        cand = CandidateRelease(
            candidate_id="cand-bad",
            revision_proposal_hash=_hash("rev-001"),
            candidate_artifact_ref={"artifact_id": "a-001", "content_hash": _hash("a-001")},
            state="INVALID_STATE",
            frozen=True,
            frozen_at=_TS,
            creator_actor_id="human-001",
            approver_actor_id="human-002",
            content_hash="",
        )
        cand = dataclasses.replace(cand, content_hash=cand.compute_content_hash())
        result = verify_candidate_release(cand)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_CANDIDATE_STATE_INVALID, result.error_codes)

    def test_candidate_hash_mismatch_blocks(self):
        cand = _make_candidate()
        bad = dataclasses.replace(cand, content_hash="deadbeef" + "0" * 56)
        result = verify_candidate_release(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_CANDIDATE_HASH_MISMATCH, result.error_codes)


# ─── ProspectiveEvaluation tests ────────────────────────────────────────


class TestProspectiveEvaluation(unittest.TestCase):
    """ProspectiveEvaluation 测试。"""

    def test_confirmed_prospective_passes(self):
        pe = _make_prospective(confirmed=True)
        result = verify_prospective_evaluation(pe)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(pe.is_hash_valid)
        self.assertTrue(pe.one_time)

    def test_prospective_one_time_check(self):
        pe = _make_prospective()
        check = check_prospective_one_time(pe)
        self.assertTrue(check.passed)

    def test_not_one_time_blocks(self):
        pe = ProspectiveEvaluation(
            prospective_id="pros-bad",
            candidate_release_hash=_hash("cand-001"),
            holdout_view_ref={"view_id": "view-001", "holdout_id": "holdout-C"},
            state="CONFIRMED",
            one_time=False,
            reused_viewed_holdout=False,
            confirmed=True,
            evaluated_at=_TS,
            content_hash="",
        )
        pe = dataclasses.replace(pe, content_hash=pe.compute_content_hash())
        result = verify_prospective_evaluation(pe)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROSPECTIVE_NOT_ONE_TIME, result.error_codes)

    def test_reuse_viewed_holdout_blocks(self):
        pe = _make_prospective(confirmed=False, reused_viewed_holdout=True)
        result = verify_prospective_evaluation(pe)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROSPECTIVE_REUSES_HOLDOUT, result.error_codes)

    def test_reuse_viewed_holdout_check_with_viewed_set(self):
        pe = _make_prospective()
        viewed = {"holdout-C"}
        check = check_prospective_no_reuse_viewed_holdout(pe, viewed_holdout_ids=viewed)
        self.assertFalse(check.passed)

    def test_reuse_viewed_holdout_check_clean(self):
        pe = _make_prospective()
        viewed: set[str] = set()
        check = check_prospective_no_reuse_viewed_holdout(pe, viewed_holdout_ids=viewed)
        self.assertTrue(check.passed)

    def test_prospective_state_invalid_blocks(self):
        pe = ProspectiveEvaluation(
            prospective_id="pros-bad",
            candidate_release_hash=_hash("cand-001"),
            holdout_view_ref={"view_id": "view-001", "holdout_id": "holdout-C"},
            state="INVALID_STATE",
            one_time=True,
            reused_viewed_holdout=False,
            confirmed=True,
            evaluated_at=_TS,
            content_hash="",
        )
        pe = dataclasses.replace(pe, content_hash=pe.compute_content_hash())
        result = verify_prospective_evaluation(pe)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROSPECTIVE_STATE_INVALID, result.error_codes)

    def test_prospective_hash_mismatch_blocks(self):
        pe = _make_prospective()
        bad = dataclasses.replace(pe, content_hash="deadbeef" + "0" * 56)
        result = verify_prospective_evaluation(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_PROSPECTIVE_HASH_MISMATCH, result.error_codes)


# ─── RevisionPolicy tests ───────────────────────────────────────────────


class TestRevisionPolicy(unittest.TestCase):
    """RevisionPolicy 测试。"""

    def test_frozen_policy_passes(self):
        policy = _make_policy()
        result = verify_revision_policy(policy)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(policy.is_hash_valid)
        self.assertTrue(policy.frozen)

    def test_unfrozen_policy_blocks(self):
        policy = make_revision_policy(policy_id="pol-bad", frozen=False, frozen_at=_TS)
        result = verify_revision_policy(policy)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_POLICY_NOT_FROZEN, result.error_codes)

    def test_policy_constraint_disabled_blocks(self):
        policy = RevisionPolicy(
            policy_id="pol-bad",
            frozen=True,
            frozen_at=_TS,
            requires_two_human_gates=False,
            content_hash="",
        )
        policy = dataclasses.replace(policy, content_hash=policy.compute_content_hash())
        result = verify_revision_policy(policy)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_WITHOUT_TWO_GATES, result.error_codes)

    def test_policy_no_evidence_index_disabled_blocks(self):
        policy = RevisionPolicy(
            policy_id="pol-bad",
            frozen=True,
            frozen_at=_TS,
            no_evidence_index_in_p8=False,
            content_hash="",
        )
        policy = dataclasses.replace(policy, content_hash=policy.compute_content_hash())
        result = verify_revision_policy(policy)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_EVIDENCE_INDEX_READ_IN_P8, result.error_codes)

    def test_policy_hash_mismatch_blocks(self):
        policy = _make_policy()
        bad = dataclasses.replace(policy, content_hash="deadbeef" + "0" * 56)
        result = verify_revision_policy(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.RV_REVISION_POLICY_HASH_MISMATCH, result.error_codes)


# ─── EvidenceImmutability tests ─────────────────────────────────────────


class TestEvidenceImmutability(unittest.TestCase):
    """EvidenceImmutability 测试。"""

    def test_old_evidence_not_modified_passes(self):
        hashes = _make_record_hashes()
        check = check_old_evidence_not_modified(hashes, list(hashes))
        self.assertTrue(check.passed)

    def test_old_evidence_modified_blocks(self):
        original = _make_record_hashes()
        current = list(original) + [_hash("extra-record")]
        check = check_old_evidence_not_modified(original, current)
        self.assertFalse(check.passed)
        self.assertIn(EC.RV_OLD_EVIDENCE_MODIFIED, check.error_codes)

    def test_old_evidence_removed_blocks(self):
        original = _make_record_hashes()
        current = original[:-1]
        check = check_old_evidence_not_modified(original, current)
        self.assertFalse(check.passed)
        self.assertIn(EC.RV_OLD_EVIDENCE_MODIFIED, check.error_codes)

    def test_evidence_immutability_comprehensive_passes(self):
        hashes = _make_record_hashes()
        check = check_evidence_immutability(
            provenance_readonly=True,
            original_record_hashes=hashes,
            current_record_hashes=list(hashes),
        )
        self.assertTrue(check.passed)

    def test_evidence_immutability_not_readonly_blocks(self):
        hashes = _make_record_hashes()
        check = check_evidence_immutability(
            provenance_readonly=False,
            original_record_hashes=hashes,
            current_record_hashes=list(hashes),
        )
        self.assertFalse(check.passed)
        self.assertIn(EC.RV_PROVENANCE_SNAPSHOT_NOT_READONLY, check.error_codes)

    def test_evidence_immutability_modified_blocks(self):
        original = _make_record_hashes()
        current = [_hash(h) for h in original]
        check = check_evidence_immutability(
            provenance_readonly=True,
            original_record_hashes=original,
            current_record_hashes=current,
        )
        self.assertFalse(check.passed)
        self.assertIn(EC.RV_OLD_EVIDENCE_MODIFIED, check.error_codes)

    def test_provenance_snapshot_is_readonly(self):
        snap = _make_provenance_snapshot()
        self.assertTrue(snap.is_readonly)
        # frozen dataclass — cannot mutate
        with self.assertRaises(dataclasses.FrozenInstanceError):
            snap.readonly = False  # type: ignore[misc]


# ─── Boundary tests ─────────────────────────────────────────────────────


class TestBoundary(unittest.TestCase):
    """RV1 边界测试。"""

    def test_no_evidence_index_in_p8_passes(self):
        outputs = {"ProvenanceSnapshot": {"report_kind": "ProvenanceSnapshot"}}
        check = check_no_evidence_index_in_p8(outputs)
        self.assertTrue(check.passed)

    def test_evidence_index_in_p8_blocks(self):
        outputs = {"EvidenceIndex": {"report_kind": "EvidenceIndex"}}
        check = check_no_evidence_index_in_p8(outputs)
        self.assertFalse(check.passed)
        self.assertIn(EC.RV_EVIDENCE_INDEX_READ_IN_P8, check.error_codes)

    def test_p8_output_boundary_allows_revision_outputs(self):
        outputs = {
            "ProvenanceSnapshot": {"report_kind": "ProvenanceSnapshot"},
            "NoChangeDecision": {"report_kind": "NoChangeDecision"},
            "RevisionProposal": {"report_kind": "RevisionProposal"},
        }
        check = check_p8_output_boundary(outputs)
        self.assertTrue(check.passed)

    def test_p8_output_boundary_forbids_evidence_index(self):
        outputs = {"EvidenceIndex": {"report_kind": "EvidenceIndex"}}
        check = check_p8_output_boundary(outputs)
        self.assertFalse(check.passed)
        self.assertIn(EC.RV_OUTPUT_KIND_FORBIDDEN, check.error_codes)

    def test_p8_output_boundary_forbids_verdict_record(self):
        outputs = {"VerdictRecord": {"report_kind": "VerdictRecord"}}
        check = check_p8_output_boundary(outputs)
        self.assertFalse(check.passed)

    def test_p8_output_boundary_forbids_confirmatory_evidence(self):
        outputs = {"ConfirmatoryEvidenceRecord": {"report_kind": "ConfirmatoryEvidenceRecord"}}
        check = check_p8_output_boundary(outputs)
        self.assertFalse(check.passed)

    def test_provenance_no_evidence_index_check(self):
        snap = _make_provenance_snapshot()
        check = check_no_evidence_index_in_provenance(snap)
        self.assertTrue(check.passed)


# ─── CapabilityReport tests ─────────────────────────────────────────────


class TestRevisionCapabilityReport(unittest.TestCase):
    """RevisionCapabilityReport 测试。"""

    def test_build_nochange_report_passes(self):
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        nc = _make_signed_nochange(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        policy = _make_policy()
        report = build_revision_capability_report(
            provenance_snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
            outcome_kind="NO_CHANGE",
            nochange_decision_hash=nc.content_hash,
            revision_policy_hash=policy.content_hash,
            old_evidence_not_modified=True,
            no_evidence_index_in_p8=True,
            holdout_not_unsealed_on_nochange=True,
            two_human_gates_for_revision=True,
            candidate_not_self_approved=True,
            holdout_fit_not_confirmation=True,
            holdout_no_repeated_peek=True,
            holdout_no_single_case_split=True,
            prospective_one_time=True,
            prospective_no_reuse_viewed_holdout=True,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        errors = verify_revision_capability_report(report)
        self.assertEqual(errors, (), msg=str(errors))

    def test_build_revision_report_passes(self):
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        prop = _make_revision_proposal(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        cand = _make_candidate(proposal_hash=prop.content_hash)
        pe = _make_prospective(candidate_hash=cand.content_hash)
        policy = _make_policy()
        report = build_revision_capability_report(
            provenance_snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
            outcome_kind="CONTROLLED_REVISION",
            revision_proposal_hash=prop.content_hash,
            candidate_release_hash=cand.content_hash,
            prospective_evaluation_hash=pe.content_hash,
            revision_policy_hash=policy.content_hash,
            old_evidence_not_modified=True,
            no_evidence_index_in_p8=True,
            holdout_not_unsealed_on_nochange=True,
            two_human_gates_for_revision=True,
            candidate_not_self_approved=True,
            holdout_fit_not_confirmation=True,
            holdout_no_repeated_peek=True,
            holdout_no_single_case_split=True,
            prospective_one_time=True,
            prospective_no_reuse_viewed_holdout=True,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        errors = verify_revision_capability_report(report)
        self.assertEqual(errors, (), msg=str(errors))

    def test_report_old_evidence_modified_blocks(self):
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        nc = _make_signed_nochange(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        policy = _make_policy()
        report = build_revision_capability_report(
            provenance_snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
            outcome_kind="NO_CHANGE",
            nochange_decision_hash=nc.content_hash,
            revision_policy_hash=policy.content_hash,
            old_evidence_not_modified=True,
            no_evidence_index_in_p8=True,
            holdout_not_unsealed_on_nochange=True,
            two_human_gates_for_revision=True,
            candidate_not_self_approved=True,
            holdout_fit_not_confirmation=True,
            holdout_no_repeated_peek=True,
            holdout_no_single_case_split=True,
            prospective_one_time=True,
            prospective_no_reuse_viewed_holdout=True,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        report["old_evidence_not_modified"] = False
        errors = verify_revision_capability_report(report)
        codes = [e[0] for e in errors]
        self.assertIn(EC.RV_OLD_EVIDENCE_MODIFIED, codes)

    def test_report_evidence_index_in_p8_blocks(self):
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        nc = _make_signed_nochange(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        policy = _make_policy()
        report = build_revision_capability_report(
            provenance_snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
            outcome_kind="NO_CHANGE",
            nochange_decision_hash=nc.content_hash,
            revision_policy_hash=policy.content_hash,
            old_evidence_not_modified=True,
            no_evidence_index_in_p8=True,
            holdout_not_unsealed_on_nochange=True,
            two_human_gates_for_revision=True,
            candidate_not_self_approved=True,
            holdout_fit_not_confirmation=True,
            holdout_no_repeated_peek=True,
            holdout_no_single_case_split=True,
            prospective_one_time=True,
            prospective_no_reuse_viewed_holdout=True,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        report["no_evidence_index_in_p8"] = False
        errors = verify_revision_capability_report(report)
        codes = [e[0] for e in errors]
        self.assertIn(EC.RV_EVIDENCE_INDEX_READ_IN_P8, codes)

    def test_report_raises_on_construction_failure(self):
        with self.assertRaises(RevisionCapabilityReportError):
            build_revision_capability_report(
                provenance_snapshot_hash=_hash("snap-001"),
                localization_hash=_hash("loc-001"),
                outcome_kind="NO_CHANGE",
                nochange_decision_hash="",
                revision_policy_hash=_hash("pol-001"),
                old_evidence_not_modified=True,
                no_evidence_index_in_p8=True,
                holdout_not_unsealed_on_nochange=True,
                two_human_gates_for_revision=True,
                candidate_not_self_approved=True,
                holdout_fit_not_confirmation=True,
                holdout_no_repeated_peek=True,
                holdout_no_single_case_split=True,
                prospective_one_time=True,
                prospective_no_reuse_viewed_holdout=True,
                verifier_identity="verifier-001",
                generated_at=_TS,
            )

    def test_report_side_effects_all_zero(self):
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        nc = _make_signed_nochange(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        policy = _make_policy()
        report = build_revision_capability_report(
            provenance_snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
            outcome_kind="NO_CHANGE",
            nochange_decision_hash=nc.content_hash,
            revision_policy_hash=policy.content_hash,
            old_evidence_not_modified=True,
            no_evidence_index_in_p8=True,
            holdout_not_unsealed_on_nochange=True,
            two_human_gates_for_revision=True,
            candidate_not_self_approved=True,
            holdout_fit_not_confirmation=True,
            holdout_no_repeated_peek=True,
            holdout_no_single_case_split=True,
            prospective_one_time=True,
            prospective_no_reuse_viewed_holdout=True,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        for key in RV_SIDE_EFFECT_KEYS:
            self.assertEqual(report["side_effects"][key], 0)


# ─── Deterministic hash tests ───────────────────────────────────────────


class TestDeterministicHash(unittest.TestCase):
    """确定性 hash 测试。"""

    def test_provenance_snapshot_hash_deterministic(self):
        s1 = _make_provenance_snapshot()
        s2 = _make_provenance_snapshot()
        self.assertEqual(s1.content_hash, s2.content_hash)

    def test_localization_hash_deterministic(self):
        l1 = _make_localization()
        l2 = _make_localization()
        self.assertEqual(l1.content_hash, l2.content_hash)

    def test_nochange_hash_deterministic(self):
        n1 = _make_signed_nochange()
        n2 = _make_signed_nochange()
        self.assertEqual(n1.content_hash, n2.content_hash)

    def test_revision_proposal_hash_deterministic(self):
        r1 = _make_revision_proposal()
        r2 = _make_revision_proposal()
        self.assertEqual(r1.content_hash, r2.content_hash)

    def test_candidate_hash_deterministic(self):
        c1 = _make_candidate()
        c2 = _make_candidate()
        self.assertEqual(c1.content_hash, c2.content_hash)

    def test_prospective_hash_deterministic(self):
        p1 = _make_prospective()
        p2 = _make_prospective()
        self.assertEqual(p1.content_hash, p2.content_hash)

    def test_policy_hash_deterministic(self):
        p1 = _make_policy()
        p2 = _make_policy()
        self.assertEqual(p1.content_hash, p2.content_hash)

    def test_holdout_consumption_hash_deterministic(self):
        h1 = _make_valid_holdout_consumption()
        h2 = _make_valid_holdout_consumption()
        self.assertEqual(h1.content_hash, h2.content_hash)

    def test_provenance_snapshot_hash_order_independent(self):
        hashes = _make_record_hashes()
        s1 = _make_provenance_snapshot(record_hashes=list(hashes))
        s2 = _make_provenance_snapshot(record_hashes=list(reversed(hashes)))
        self.assertEqual(s1.content_hash, s2.content_hash)


# ─── Constants tests ────────────────────────────────────────────────────


class TestConstants(unittest.TestCase):
    """RV1 常量验证。"""

    def test_rv_localization_layers(self):
        self.assertIn("CORE", RV_LOCALIZATION_LAYERS)
        self.assertIn("BOUNDARY", RV_LOCALIZATION_LAYERS)
        self.assertIn("SELECTOR", RV_LOCALIZATION_LAYERS)
        self.assertIn("RENDERER", RV_LOCALIZATION_LAYERS)
        self.assertIn("INJECTION", RV_LOCALIZATION_LAYERS)
        self.assertIn("CRITIC", RV_LOCALIZATION_LAYERS)
        self.assertIn("MODEL_RESOURCE", RV_LOCALIZATION_LAYERS)

    def test_rv_revision_states(self):
        self.assertIn("LOCALIZED", RV_REVISION_STATES)
        self.assertIn("NO_CHANGE_DECIDED", RV_REVISION_STATES)
        self.assertIn("REVISION_PROPOSED", RV_REVISION_STATES)
        self.assertIn("REVISED", RV_REVISION_STATES)

    def test_rv_holdout_statuses(self):
        self.assertEqual(RV_HOLDOUT_STATUSES, frozenset({"UNVIEWED", "VIEWED", "CONSUMED"}))

    def test_rv_nochange_states(self):
        self.assertEqual(RV_NOCHANGE_STATES, frozenset({"DRAFT", "SIGNED", "ACCEPTED"}))

    def test_rv_revision_proposal_states(self):
        self.assertIn("TWO_GATE_APPROVED", RV_REVISION_PROPOSAL_STATES)
        self.assertIn("ONE_GATE_APPROVED", RV_REVISION_PROPOSAL_STATES)
        self.assertIn("DRAFT", RV_REVISION_PROPOSAL_STATES)

    def test_rv_candidate_states(self):
        self.assertIn("FROZEN", RV_CANDIDATE_STATES)
        self.assertIn("DRAFT", RV_CANDIDATE_STATES)

    def test_rv_prospective_states(self):
        self.assertEqual(RV_PROSPECTIVE_STATES, frozenset({"PENDING", "CONFIRMED", "REJECTED"}))

    def test_rv_allowed_output_kinds(self):
        self.assertIn("ProvenanceSnapshot", RV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("FailureLocalization", RV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("NoChangeDecision", RV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("RevisionProposal", RV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("HoldoutConsumption", RV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("CandidateRelease", RV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("ProspectiveEvaluation", RV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("RevisionPolicy", RV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("RevisionCapabilityReport", RV_ALLOWED_OUTPUT_KINDS)

    def test_rv_forbidden_output_kinds(self):
        self.assertIn("EvidenceIndex", RV_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("VerdictRecord", RV_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("ConfirmatoryEvidenceRecord", RV_FORBIDDEN_OUTPUT_KINDS)

    def test_rv_allowed_and_forbidden_disjoint(self):
        self.assertEqual(RV_ALLOWED_OUTPUT_KINDS & RV_FORBIDDEN_OUTPUT_KINDS, frozenset())

    def test_rv_check_ids_unique(self):
        self.assertEqual(len(RV_CHECK_IDS), len(set(RV_CHECK_IDS)))

    def test_rv_claims_unique(self):
        self.assertEqual(len(RV_CLAIMS), len(set(RV_CLAIMS)))

    def test_rv_nonclaims_unique(self):
        self.assertEqual(len(RV_NONCLAIMS), len(set(RV_NONCLAIMS)))

    def test_rv_side_effect_keys(self):
        self.assertIn("database_writes", RV_SIDE_EFFECT_KEYS)
        self.assertIn("redis_writes", RV_SIDE_EFFECT_KEYS)
        self.assertIn("solver_launches", RV_SIDE_EFFECT_KEYS)
        self.assertIn("model_live_calls", RV_SIDE_EFFECT_KEYS)
        self.assertIn("holdout_unseals", RV_SIDE_EFFECT_KEYS)

    def test_error_codes_exist(self):
        for code_name in (
            "RV_EVIDENCE_INDEX_READ_IN_P8",
            "RV_FIT_EQUALS_CONFIRMATION",
            "RV_HOLDOUT_REPEATED_PEEK",
            "RV_SINGLE_CASE_SPLIT",
            "RV_CANDIDATE_SELF_APPROVED",
            "RV_OLD_EVIDENCE_MODIFIED",
            "RV_NOCHANGE_UNSEALS_HOLDOUT",
            "RV_REVISION_WITHOUT_TWO_GATES",
            "RV_PROVENANCE_SNAPSHOT_NOT_READONLY",
            "RV_FAILURE_LOCALIZATION_INCOMPLETE",
            "RV_NOCHANGE_NOT_SIGNED",
            "RV_REVISION_PROPOSAL_NOT_SIGNED",
            "RV_HOLDOUT_ALREADY_CONSUMED",
            "RV_PROSPECTIVE_REUSES_HOLDOUT",
            "RV_CANDIDATE_NOT_FROZEN",
            "RV_REVISION_POLICY_NOT_FROZEN",
            "RV_LOCALIZATION_LAYER_INVALID",
            "RV_PROVENANCE_SNAPSHOT_HASH_MISMATCH",
            "RV_PROVENANCE_SNAPSHOT_INCOMPLETE",
            "RV_NOCHANGE_STATE_INVALID",
            "RV_REVISION_PROPOSAL_STATE_INVALID",
            "RV_CANDIDATE_STATE_INVALID",
            "RV_PROSPECTIVE_STATE_INVALID",
            "RV_HOLDOUT_STATUS_INVALID",
            "RV_REVISION_PROPOSAL_HASH_MISMATCH",
            "RV_CANDIDATE_HASH_MISMATCH",
            "RV_PROSPECTIVE_HASH_MISMATCH",
            "RV_NOCHANGE_HASH_MISMATCH",
            "RV_LOCALIZATION_HASH_MISMATCH",
            "RV_HOLDOUT_CONSUMPTION_HASH_MISMATCH",
            "RV_REVISION_POLICY_HASH_MISMATCH",
            "RV_OUTPUT_KIND_FORBIDDEN",
            "RV_HOLDOUT_VIEW_MISSING",
            "RV_PROSPECTIVE_NOT_ONE_TIME",
            "RV_REVISION_GATE_COUNT_INSUFFICIENT",
            "RV_NOCHANGE_REFERENCES_EVIDENCE_INDEX",
            "RV_REVISION_REFERENCES_EVIDENCE_INDEX",
            "RV_LOCALIZATION_REFERENCES_EVIDENCE_INDEX",
            "RV_CAPABILITY_HASH_MISMATCH",
        ):
            self.assertTrue(
                hasattr(EC, code_name),
                msg=f"EC.{code_name} missing",
            )


# ─── Full pipeline tests ────────────────────────────────────────────────


class TestFullPipeline(unittest.TestCase):
    """完整流水线测试。"""

    def test_golden_path_no_change(self):
        """Golden path: ProvenanceSnapshot → FailureLocalization → NoChangeDecision."""
        snap = _make_provenance_snapshot()
        snap_result = verify_provenance_snapshot(snap)
        self.assertTrue(snap_result.passed, msg=str(snap_result.details))

        loc = _make_localization(snapshot_hash=snap.content_hash)
        loc_result = verify_failure_localization(loc)
        self.assertTrue(loc_result.passed, msg=str(loc_result.details))

        nc = _make_signed_nochange(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        nc_result = verify_no_change_decision(nc)
        self.assertTrue(nc_result.passed, msg=str(nc_result.details))

        # holdout not unsealed
        self.assertFalse(nc.holdout_unsealed)
        holdout_check = check_nochange_does_not_unseal_holdout(nc)
        self.assertTrue(holdout_check.passed)

        # old evidence not modified
        immutability_check = check_old_evidence_not_modified(
            list(snap.record_hashes), list(snap.record_hashes)
        )
        self.assertTrue(immutability_check.passed)

    def test_golden_path_controlled_revision(self):
        """Golden path: ProvenanceSnapshot → FailureLocalization →
        RevisionProposal → CandidateRelease → ProspectiveEvaluation → two HumanGate."""
        snap = _make_provenance_snapshot()
        snap_result = verify_provenance_snapshot(snap)
        self.assertTrue(snap_result.passed, msg=str(snap_result.details))

        loc = _make_localization(snapshot_hash=snap.content_hash)
        loc_result = verify_failure_localization(loc)
        self.assertTrue(loc_result.passed, msg=str(loc_result.details))

        prop = _make_revision_proposal(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        prop_result = verify_revision_proposal(prop)
        self.assertTrue(prop_result.passed, msg=str(prop_result.details))
        self.assertEqual(prop.gate_count, 2)

        cand = _make_candidate(proposal_hash=prop.content_hash)
        cand_result = verify_candidate_release(cand)
        self.assertTrue(cand_result.passed, msg=str(cand_result.details))

        pe = _make_prospective(candidate_hash=cand.content_hash)
        pe_result = verify_prospective_evaluation(pe)
        self.assertTrue(pe_result.passed, msg=str(pe_result.details))

        # two HumanGate approvals
        gate_check = check_revision_two_human_gates(prop)
        self.assertTrue(gate_check.passed)

        # candidate not self-approved
        self_cand_check = check_candidate_not_self_approved(cand)
        self.assertTrue(self_cand_check.passed)

        # prospective one-time
        one_time_check = check_prospective_one_time(pe)
        self.assertTrue(one_time_check.passed)

    def test_golden_path_holdout_consumption(self):
        """Golden path: holdout consumption tracking with fit≠confirmation."""
        views = [
            HoldoutView(
                view_id="view-fit-001",
                holdout_id="holdout-A",
                purpose="FIT",
                case_ids=("case-001", "case-002"),
                viewed_at=_TS,
                status="VIEWED",
            ),
            HoldoutView(
                view_id="view-conf-001",
                holdout_id="holdout-B",
                purpose="CONFIRMATION",
                case_ids=("case-003",),
                viewed_at=_TS,
                status="VIEWED",
            ),
        ]
        hc = make_holdout_consumption(
            consumption_id="hc-pipeline",
            provenance_snapshot_hash=_hash("snap-001"),
            views=views,
        )
        result = verify_holdout_consumption(hc)
        self.assertTrue(result.passed, msg=str(result.details))
        # viewed immediately consumed
        self.assertIn("holdout-A", hc.consumed_holdout_ids)
        self.assertIn("holdout-B", hc.consumed_holdout_ids)
        # fit ≠ confirmation
        fit_check = check_fit_not_confirmation(hc)
        self.assertTrue(fit_check.passed)
        # no repeated peek
        peek_check = check_no_repeated_peek(hc)
        self.assertTrue(peek_check.passed)
        # no single case split
        split_check = check_no_single_case_split(hc)
        self.assertTrue(split_check.passed)

    def test_full_pipeline_with_capability_report_no_change(self):
        """Full pipeline with NO_CHANGE capability report."""
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        nc = _make_signed_nochange(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        policy = _make_policy()
        report = build_revision_capability_report(
            provenance_snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
            outcome_kind="NO_CHANGE",
            nochange_decision_hash=nc.content_hash,
            revision_policy_hash=policy.content_hash,
            old_evidence_not_modified=True,
            no_evidence_index_in_p8=True,
            holdout_not_unsealed_on_nochange=True,
            two_human_gates_for_revision=True,
            candidate_not_self_approved=True,
            holdout_fit_not_confirmation=True,
            holdout_no_repeated_peek=True,
            holdout_no_single_case_split=True,
            prospective_one_time=True,
            prospective_no_reuse_viewed_holdout=True,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        errors = verify_revision_capability_report(report)
        self.assertEqual(errors, (), msg=str(errors))
        self.assertEqual(report["outcome_kind"], "NO_CHANGE")

    def test_full_pipeline_with_capability_report_revision(self):
        """Full pipeline with CONTROLLED_REVISION capability report."""
        snap = _make_provenance_snapshot()
        loc = _make_localization(snapshot_hash=snap.content_hash)
        prop = _make_revision_proposal(
            snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
        )
        cand = _make_candidate(proposal_hash=prop.content_hash)
        pe = _make_prospective(candidate_hash=cand.content_hash)
        policy = _make_policy()
        report = build_revision_capability_report(
            provenance_snapshot_hash=snap.content_hash,
            localization_hash=loc.content_hash,
            outcome_kind="CONTROLLED_REVISION",
            revision_proposal_hash=prop.content_hash,
            candidate_release_hash=cand.content_hash,
            prospective_evaluation_hash=pe.content_hash,
            revision_policy_hash=policy.content_hash,
            old_evidence_not_modified=True,
            no_evidence_index_in_p8=True,
            holdout_not_unsealed_on_nochange=True,
            two_human_gates_for_revision=True,
            candidate_not_self_approved=True,
            holdout_fit_not_confirmation=True,
            holdout_no_repeated_peek=True,
            holdout_no_single_case_split=True,
            prospective_one_time=True,
            prospective_no_reuse_viewed_holdout=True,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        errors = verify_revision_capability_report(report)
        self.assertEqual(errors, (), msg=str(errors))
        self.assertEqual(report["outcome_kind"], "CONTROLLED_REVISION")


if __name__ == "__main__":
    unittest.main()
