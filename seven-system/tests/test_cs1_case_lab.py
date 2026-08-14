"""WP-CS1 CaseLab Dual-Entry & P3C 测试。

测试层级：Golden → Negative → Fault injection → Boundary
覆盖：
- Golden path: natural entry (P2A+P3N → CasePack), generated entry (P3A+P3B → CasePack),
  P3C role freeze
- Dual-entry fixture tests
- P3C verification tests
- Negative: natural case forged draft, model self-signing role, process-only in result
  layer, missing evidence refs, hash mismatch, unsigned admission, role without evidence
- Deterministic hash tests
- CS1 boundary tests (allowed/forbidden output kinds)
- All constants verified

所有 blocker test 失败 → 工作包 FAIL。
"""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path
from typing import Any

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import (
    VerificationErrorCode as EC,
    CS_CASE_ROLES,
    CS_ENTRY_PATHS,
    CS_ADMISSION_STATUSES,
    CS_CASE_PACK_STATES,
    CS_MECHANISM_REVIEW_KINDS,
    CS_ALLOWED_OUTPUT_KINDS,
    CS_FORBIDDEN_OUTPUT_KINDS,
    CS_P3C_STATES,
    CS_GATE_TYPE_CASE_ROLE,
    CS_SIDE_EFFECT_KEYS,
    CS_CHECK_IDS,
    CS_CLAIMS,
    CS_NONCLAIMS,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.case_lab import (
    CaseRole,
    build_case_role,
    verify_case_role,
    MechanismReview,
    build_mechanism_review,
    verify_mechanism_review,
    RelationMapping,
    build_relation_mapping,
    verify_relation_mapping,
    CasePack,
    CasePackVersion,
    build_case_pack,
    verify_case_pack,
    build_case_pack_version,
    verify_case_pack_version,
    freeze_case_pack_version,
    check_case_pack_immutable,
    AdmissionDecision,
    build_admission_decision,
    verify_admission_decision,
    check_process_only_not_in_result_layer,
    NaturalEntryEvidence,
    GeneratedEntryEvidence,
    DualEntryFixture,
    DualEntry,
    build_natural_entry_evidence,
    build_generated_entry_evidence,
    verify_natural_entry_evidence,
    verify_generated_entry_evidence,
    build_dual_entry_fixture,
    verify_dual_entry_fixture,
    P3CVerifier,
    P3CVerificationReport,
    check_natural_case_not_forged_draft,
    check_model_not_self_signing_role,
    check_process_only_excluded_from_result,
    CaseLabCapabilityReport,
    build_case_lab_capability_report,
    verify_case_lab_capability_report,
)


# ─── helpers ───────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64


def _ref_hash(ref_id: str, sha: str = _ZERO_HASH) -> dict[str, str]:
    return {"ref_id": ref_id, "sha256": sha}


def _make_mechanism_contract_ref() -> dict[str, str]:
    return _ref_hash("mc-001", hashlib.sha256(b"mechanism-contract-v1").hexdigest())


def _make_relation_mapping_ref() -> dict[str, str]:
    return _ref_hash("rm-001", hashlib.sha256(b"relation-mapping-v1").hexdigest())


def _make_role_assignment_refs() -> list[dict[str, str]]:
    return [
        _ref_hash("role-positive-001", hashlib.sha256(b"role-positive").hexdigest()),
        _ref_hash("role-false-friend-001", hashlib.sha256(b"role-false-friend").hexdigest()),
        _ref_hash("role-boundary-001", hashlib.sha256(b"role-boundary").hexdigest()),
        _ref_hash("role-unrelated-001", hashlib.sha256(b"role-unrelated").hexdigest()),
    ]


def _make_case_roles(
    case_pack_ref_id: str = "cp-001",
    signed_by_human: bool = True,
) -> list[CaseRole]:
    """构建覆盖所有 CS_CASE_ROLES 的 CaseRole 列表。"""
    roles = []
    for role_name in sorted(CS_CASE_ROLES):
        roles.append(build_case_role(
            role_id=f"cr-{role_name}-001",
            case_pack_ref_id=case_pack_ref_id,
            role=role_name,
            evidence_refs=[_ref_hash(f"evidence-{role_name}", hashlib.sha256(f"ev-{role_name}".encode()).hexdigest())],
            signed_by_human=signed_by_human,
            description=f"Role: {role_name}",
        ))
    return roles


def _make_admission_decision(
    case_pack_ref_id: str = "cp-001",
    case_pack_sha: str = _ZERO_HASH,
    signed_by_human: bool = True,
    signed_by_model: bool = False,
    admitted_for_process_only: bool = False,
    admission_status: str = "ADMITTED",
) -> AdmissionDecision:
    return build_admission_decision(
        decision_id="ad-001",
        case_pack_ref_and_hash=_ref_hash(case_pack_ref_id, case_pack_sha),
        admission_status=admission_status,
        frozen_roles=sorted(CS_CASE_ROLES),
        signed_by_human=signed_by_human,
        signed_by_model=signed_by_model,
        admitted_for_process_only=admitted_for_process_only,
        gate_decision_ref_and_hash=_ref_hash("gd-001", hashlib.sha256(b"gate-decision").hexdigest()),
        actor_id="human-actor-001",
        actor_role="MATH_VERIFIER",
        nonce="nonce-cs1-001-abcdef",
        issued_at="2026-08-14T12:00:00Z",
    )


def _make_case_pack(
    pack_id: str = "cp-001",
    entry_path: str = "NATURAL",
    role_assignment_refs: list[dict[str, str]] | None = None,
) -> CasePack:
    return build_case_pack(
        pack_id=pack_id,
        entry_path=entry_path,
        problem_statement="Find the minimum of x+y given xy=1.",
        solution="By AM-GM, x+y >= 2*sqrt(xy) = 2. Minimum is 2.",
        mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
        relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
        p3n_review_refs=[_ref_hash("p3n-001", hashlib.sha256(b"p3n-review").hexdigest())] if entry_path == "NATURAL" else None,
        bare_result_refs=[_ref_hash("bare-001", hashlib.sha256(b"bare-result").hexdigest())] if entry_path == "GENERATED" else None,
        role_assignment_refs=role_assignment_refs or _make_role_assignment_refs(),
    )


def _make_case_pack_version(
    pack_id: str = "cp-001",
    pack_sha: str = _ZERO_HASH,
    state: str = "FROZEN",
    signed_by_human: bool = True,
    version_number: int = 0,
) -> CasePackVersion:
    return build_case_pack_version(
        version_id="cpv-001",
        pack_ref_and_hash=_ref_hash(pack_id, pack_sha),
        version_number=version_number,
        supersedes_ref=None if version_number == 0 else {"version_id": "cpv-000", "content_hash": hashlib.sha256(b"prev-version").hexdigest()},
        state=state,
        signed_by_human=signed_by_human,
        admission_decision_ref_and_hash=_ref_hash("ad-001", hashlib.sha256(b"admission-decision").hexdigest()),
    )


# ─── Constants tests ───────────────────────────────────────────────────


class TestCS1Constants(unittest.TestCase):
    """CS1 常量验证。"""

    def test_cs_case_roles(self):
        self.assertEqual(CS_CASE_ROLES, frozenset({"positive", "false_friend", "boundary", "unrelated"}))

    def test_cs_entry_paths(self):
        self.assertEqual(CS_ENTRY_PATHS, frozenset({"NATURAL", "GENERATED"}))

    def test_cs_admission_statuses(self):
        self.assertEqual(CS_ADMISSION_STATUSES, frozenset({"PENDING", "ADMITTED", "REJECTED", "PROCESS_ONLY"}))

    def test_cs_case_pack_states(self):
        self.assertEqual(CS_CASE_PACK_STATES, frozenset({"DRAFT", "FROZEN", "SUPERSEDED"}))

    def test_cs_mechanism_review_kinds(self):
        self.assertEqual(CS_MECHANISM_REVIEW_KINDS, frozenset({"IDENTIFICATION", "BOUNDARY_CHECK", "COMPLETENESS"}))

    def test_cs_p3c_states(self):
        self.assertEqual(CS_P3C_STATES, frozenset({"UNVERIFIED", "VERIFIED", "BLOCKED"}))

    def test_cs_gate_type_case_role(self):
        self.assertEqual(CS_GATE_TYPE_CASE_ROLE, "G-CASE-ROLE")

    def test_cs_allowed_output_kinds(self):
        expected = frozenset({
            "CasePack", "CasePackVersion", "AdmissionDecision", "CaseRole",
            "MechanismReview", "RelationMapping", "DualEntryFixture",
            "P3CVerificationReport", "CaseLabCapabilityReport",
        })
        self.assertEqual(CS_ALLOWED_OUTPUT_KINDS, expected)

    def test_cs_forbidden_output_kinds(self):
        expected = frozenset({
            "EvidenceRecord", "ConfirmatoryEvidenceRecord", "P5ClaimRecord",
            "RunAudit", "DatabaseSchemaStateReport", "SchemaBootstrapReceipt",
            "DatabaseRuntimeCapabilityReport", "SolverLaunchReceipt",
            "RedisProjection",
        })
        self.assertEqual(CS_FORBIDDEN_OUTPUT_KINDS, expected)

    def test_cs_allowed_forbidden_disjoint(self):
        self.assertEqual(CS_ALLOWED_OUTPUT_KINDS & CS_FORBIDDEN_OUTPUT_KINDS, frozenset())

    def test_cs_side_effect_keys(self):
        self.assertEqual(set(CS_SIDE_EFFECT_KEYS), {
            "database_writes", "redis_writes", "d_volume_writes",
            "solver_launches", "model_live_calls", "human_gate_commits",
        })

    def test_cs_check_ids(self):
        self.assertIsInstance(CS_CHECK_IDS, tuple)
        self.assertTrue(len(CS_CHECK_IDS) > 0)
        for cid in CS_CHECK_IDS:
            self.assertTrue(cid.startswith("cs1."))

    def test_cs_claims(self):
        self.assertIsInstance(CS_CLAIMS, tuple)
        self.assertTrue(len(CS_CLAIMS) > 0)

    def test_cs_nonclaims(self):
        self.assertIsInstance(CS_NONCLAIMS, tuple)
        self.assertTrue(len(CS_NONCLAIMS) > 0)
        self.assertIn("no_p5_claim", CS_NONCLAIMS)
        self.assertIn("status_implemented_pending_evidence", CS_NONCLAIMS)

    def test_cs_error_codes_exist(self):
        """所有 CS1 错误码都在 enum 中。"""
        cs_codes = [
            EC.CS_NATURAL_CASE_FORGED_DRAFT,
            EC.CS_MODEL_SELF_SIGNED_ROLE,
            EC.CS_PROCESS_ONLY_IN_RESULT_LAYER,
            EC.CS_EVIDENCE_REF_MISSING,
            EC.CS_CASE_PACK_HASH_MISMATCH,
            EC.CS_ADMISSION_DECISION_UNSIGNED,
            EC.CS_ROLE_WITHOUT_EVIDENCE,
            EC.CS_CASE_ROLE_INVALID,
            EC.CS_DUAL_ENTRY_PATH_INVALID,
            EC.CS_MECHANISM_REVIEW_FAILED,
            EC.CS_RELATION_MAPPING_INVALID,
            EC.CS_CASE_PACK_NOT_IMMUTABLE,
            EC.CS_P3C_VERIFICATION_FAILED,
            EC.CS_ROLE_NOT_FROZEN,
            EC.CS_ADMISSION_ROLE_UNKNOWN,
            EC.CS_CASE_PACK_VERSION_REF_BROKEN,
            EC.CS_CASE_PACK_STATE_INVALID,
            EC.CS_ADMISSION_STATE_INVALID,
            EC.CS_P3C_STATE_INVALID,
            EC.CS_OUTPUT_KIND_FORBIDDEN,
            EC.CS_CAPABILITY_HASH_MISMATCH,
        ]
        for code in cs_codes:
            self.assertTrue(code.value.startswith("CS_"))


# ─── CaseRole tests ────────────────────────────────────────────────────


class TestCaseRole(unittest.TestCase):
    """CaseRole 测试。"""

    def test_build_and_verify_case_role(self):
        """Golden: 构建 + 验证 CaseRole。"""
        role = build_case_role(
            role_id="cr-positive-001",
            case_pack_ref_id="cp-001",
            role="positive",
            evidence_refs=[_ref_hash("ev-001", hashlib.sha256(b"evidence").hexdigest())],
            signed_by_human=True,
            description="Target mechanism present",
        )
        result = verify_case_role(role)
        self.assertTrue(result.passed, f"verify failed: {result.details}")
        self.assertEqual(role.role, "positive")
        self.assertTrue(role.signed_by_human)

    def test_case_role_all_roles(self):
        """所有 CS_CASE_ROLES 都能构建和验证。"""
        for role_name in CS_CASE_ROLES:
            role = build_case_role(
                role_id=f"cr-{role_name}-001",
                case_pack_ref_id="cp-001",
                role=role_name,
                evidence_refs=[_ref_hash(f"ev-{role_name}", _ZERO_HASH)],
                signed_by_human=True,
            )
            result = verify_case_role(role)
            self.assertTrue(result.passed, f"role {role_name} failed: {result.details}")

    def test_case_role_without_evidence_blocked(self):
        """Blocker: role without evidence → BLOCK。"""
        role = build_case_role(
            role_id="cr-noev-001",
            case_pack_ref_id="cp-001",
            role="positive",
            evidence_refs=[],
            signed_by_human=True,
        )
        result = verify_case_role(role)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_ROLE_WITHOUT_EVIDENCE, result.error_codes)

    def test_case_role_model_signed_blocked(self):
        """Blocker: model self-signing role → BLOCK。"""
        role = build_case_role(
            role_id="cr-model-001",
            case_pack_ref_id="cp-001",
            role="positive",
            evidence_refs=[_ref_hash("ev-001", _ZERO_HASH)],
            signed_by_human=False,
        )
        result = verify_case_role(role)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_MODEL_SELF_SIGNED_ROLE, result.error_codes)

    def test_case_role_invalid_role_blocked(self):
        """Blocker: invalid role → BLOCK。"""
        role = build_case_role(
            role_id="cr-invalid-001",
            case_pack_ref_id="cp-001",
            role="invalid_role",
            evidence_refs=[_ref_hash("ev-001", _ZERO_HASH)],
            signed_by_human=True,
        )
        result = verify_case_role(role)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_CASE_ROLE_INVALID, result.error_codes)

    def test_case_role_hash_deterministic(self):
        """Deterministic hash: 相同输入 → 相同 hash。"""
        role1 = build_case_role(
            role_id="cr-001",
            case_pack_ref_id="cp-001",
            role="positive",
            evidence_refs=[_ref_hash("ev-001", _ZERO_HASH)],
            signed_by_human=True,
        )
        role2 = build_case_role(
            role_id="cr-001",
            case_pack_ref_id="cp-001",
            role="positive",
            evidence_refs=[_ref_hash("ev-001", _ZERO_HASH)],
            signed_by_human=True,
        )
        self.assertEqual(role1.content_hash, role2.content_hash)

    def test_case_role_hash_mismatch_blocked(self):
        """Blocker: hash mismatch → BLOCK。"""
        role = build_case_role(
            role_id="cr-001",
            case_pack_ref_id="cp-001",
            role="positive",
            evidence_refs=[_ref_hash("ev-001", _ZERO_HASH)],
            signed_by_human=True,
        )
        d = role.to_dict()
        d["content_hash"] = "a" * 64
        result = verify_case_role(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_CASE_PACK_HASH_MISMATCH, result.error_codes)


# ─── MechanismReview tests ─────────────────────────────────────────────


class TestMechanismReview(unittest.TestCase):
    """MechanismReview 测试。"""

    def test_build_and_verify(self):
        """Golden: 构建 + 验证 MechanismReview。"""
        review = build_mechanism_review(
            review_id="mr-001",
            case_pack_ref_id="cp-001",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            review_kind="IDENTIFICATION",
            verdict="PASS",
            findings=["Mechanism correctly identified"],
            reviewer_role="trace_analyst",
        )
        result = verify_mechanism_review(review)
        self.assertTrue(result.passed, f"verify failed: {result.details}")

    def test_all_review_kinds(self):
        """所有 CS_MECHANISM_REVIEW_KINDS 都能构建和验证。"""
        for kind in CS_MECHANISM_REVIEW_KINDS:
            review = build_mechanism_review(
                review_id=f"mr-{kind}-001",
                case_pack_ref_id="cp-001",
                mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
                review_kind=kind,
                verdict="PASS",
                findings=[],
                reviewer_role="trace_analyst",
            )
            result = verify_mechanism_review(review)
            self.assertTrue(result.passed, f"kind {kind} failed: {result.details}")

    def test_invalid_review_kind_blocked(self):
        """Blocker: invalid review_kind → BLOCK。"""
        review = build_mechanism_review(
            review_id="mr-bad-001",
            case_pack_ref_id="cp-001",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            review_kind="INVALID",
            verdict="PASS",
            findings=[],
            reviewer_role="trace_analyst",
        )
        result = verify_mechanism_review(review)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_MECHANISM_REVIEW_FAILED, result.error_codes)

    def test_invalid_verdict_blocked(self):
        """Blocker: invalid verdict → BLOCK。"""
        review = build_mechanism_review(
            review_id="mr-bad-verdict-001",
            case_pack_ref_id="cp-001",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            review_kind="IDENTIFICATION",
            verdict="INVALID",
            findings=[],
            reviewer_role="trace_analyst",
        )
        result = verify_mechanism_review(review)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_MECHANISM_REVIEW_FAILED, result.error_codes)

    def test_missing_mechanism_ref_blocked(self):
        """Blocker: missing mechanism_contract_ref → BLOCK。"""
        review = build_mechanism_review(
            review_id="mr-noref-001",
            case_pack_ref_id="cp-001",
            mechanism_contract_ref_and_hash={},
            review_kind="IDENTIFICATION",
            verdict="PASS",
            findings=[],
            reviewer_role="trace_analyst",
        )
        result = verify_mechanism_review(review)
        self.assertFalse(result.passed)

    def test_hash_deterministic(self):
        """Deterministic hash。"""
        r1 = build_mechanism_review(
            review_id="mr-001", case_pack_ref_id="cp-001",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            review_kind="IDENTIFICATION", verdict="PASS",
            findings=["f1"], reviewer_role="trace_analyst",
        )
        r2 = build_mechanism_review(
            review_id="mr-001", case_pack_ref_id="cp-001",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            review_kind="IDENTIFICATION", verdict="PASS",
            findings=["f1"], reviewer_role="trace_analyst",
        )
        self.assertEqual(r1.content_hash, r2.content_hash)


# ─── RelationMapping tests ─────────────────────────────────────────────


class TestRelationMapping(unittest.TestCase):
    """RelationMapping 测试。"""

    def test_build_and_verify(self):
        """Golden: 构建 + 验证 RelationMapping。"""
        mapping = build_relation_mapping(
            mapping_id="rm-001",
            case_pack_ref_id="cp-001",
            taxonomy_snapshot_ref_and_hash=_ref_hash("tx-snap-001", _ZERO_HASH),
            tell_core_refs=[_ref_hash("tc-001", _ZERO_HASH)],
            boundary_refs=[_ref_hash("bd-001", _ZERO_HASH)],
            hint_refs=[_ref_hash("ht-001", _ZERO_HASH)],
        )
        result = verify_relation_mapping(mapping)
        self.assertTrue(result.passed, f"verify failed: {result.details}")

    def test_empty_mapping_blocked(self):
        """Blocker: empty mapping (no refs) → BLOCK。"""
        mapping = build_relation_mapping(
            mapping_id="rm-empty-001",
            case_pack_ref_id="cp-001",
            taxonomy_snapshot_ref_and_hash=_ref_hash("tx-snap-001", _ZERO_HASH),
            tell_core_refs=[],
            boundary_refs=[],
            hint_refs=[],
        )
        result = verify_relation_mapping(mapping)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_RELATION_MAPPING_INVALID, result.error_codes)

    def test_missing_taxonomy_ref_blocked(self):
        """Blocker: missing taxonomy_snapshot_ref → BLOCK。"""
        mapping = build_relation_mapping(
            mapping_id="rm-notx-001",
            case_pack_ref_id="cp-001",
            taxonomy_snapshot_ref_and_hash={},
            tell_core_refs=[_ref_hash("tc-001", _ZERO_HASH)],
            boundary_refs=[],
            hint_refs=[],
        )
        result = verify_relation_mapping(mapping)
        self.assertFalse(result.passed)

    def test_hash_deterministic(self):
        """Deterministic hash。"""
        kwargs = dict(
            mapping_id="rm-001", case_pack_ref_id="cp-001",
            taxonomy_snapshot_ref_and_hash=_ref_hash("tx-snap-001", _ZERO_HASH),
            tell_core_refs=[_ref_hash("tc-001", _ZERO_HASH)],
            boundary_refs=[], hint_refs=[],
        )
        m1 = build_relation_mapping(**kwargs)
        m2 = build_relation_mapping(**kwargs)
        self.assertEqual(m1.content_hash, m2.content_hash)


# ─── CasePack tests ────────────────────────────────────────────────────


class TestCasePack(unittest.TestCase):
    """CasePack 测试。"""

    def test_build_and_verify_natural(self):
        """Golden: natural entry CasePack。"""
        pack = _make_case_pack(entry_path="NATURAL")
        result = verify_case_pack(pack)
        self.assertTrue(result.passed, f"verify failed: {result.details}")
        self.assertEqual(pack.entry_path, "NATURAL")
        self.assertTrue(len(pack.p3n_review_refs) > 0)

    def test_build_and_verify_generated(self):
        """Golden: generated entry CasePack。"""
        pack = _make_case_pack(entry_path="GENERATED")
        result = verify_case_pack(pack)
        self.assertTrue(result.passed, f"verify failed: {result.details}")
        self.assertEqual(pack.entry_path, "GENERATED")
        self.assertTrue(len(pack.bare_result_refs) > 0)

    def test_invalid_entry_path_blocked(self):
        """Blocker: invalid entry_path → BLOCK。"""
        pack = build_case_pack(
            pack_id="cp-bad-001",
            entry_path="INVALID",
            problem_statement="test",
            solution="test",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
        )
        result = verify_case_pack(pack)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_DUAL_ENTRY_PATH_INVALID, result.error_codes)

    def test_empty_role_assignments_blocked(self):
        """Blocker: empty role_assignment_refs → BLOCK。"""
        pack = build_case_pack(
            pack_id="cp-noroles-001",
            entry_path="NATURAL",
            problem_statement="test",
            solution="test",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=[],
        )
        result = verify_case_pack(pack)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_ROLE_WITHOUT_EVIDENCE, result.error_codes)

    def test_missing_mechanism_ref_blocked(self):
        """Blocker: missing mechanism_contract_ref → BLOCK。"""
        pack = build_case_pack(
            pack_id="cp-nomc-001",
            entry_path="NATURAL",
            problem_statement="test",
            solution="test",
            mechanism_contract_ref_and_hash={},
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
        )
        result = verify_case_pack(pack)
        self.assertFalse(result.passed)

    def test_hash_deterministic(self):
        """Deterministic hash。"""
        p1 = _make_case_pack(pack_id="cp-deterministic-001")
        p2 = _make_case_pack(pack_id="cp-deterministic-001")
        self.assertEqual(p1.content_hash, p2.content_hash)

    def test_hash_mismatch_blocked(self):
        """Blocker: hash mismatch → BLOCK。"""
        pack = _make_case_pack()
        d = pack.to_dict()
        d["content_hash"] = "b" * 64
        result = verify_case_pack(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_CASE_PACK_HASH_MISMATCH, result.error_codes)


# ─── CasePackVersion tests ─────────────────────────────────────────────


class TestCasePackVersion(unittest.TestCase):
    """CasePackVersion 测试。"""

    def test_build_and_verify_draft(self):
        """Golden: DRAFT CasePackVersion。"""
        version = _make_case_pack_version(state="DRAFT", signed_by_human=False)
        result = verify_case_pack_version(version)
        self.assertTrue(result.passed, f"verify failed: {result.details}")
        self.assertEqual(version.state, "DRAFT")

    def test_build_and_verify_frozen(self):
        """Golden: FROZEN CasePackVersion。"""
        version = _make_case_pack_version(state="FROZEN", signed_by_human=True)
        result = verify_case_pack_version(version)
        self.assertTrue(result.passed, f"verify failed: {result.details}")
        self.assertEqual(version.state, "FROZEN")

    def test_frozen_without_human_blocked(self):
        """Blocker: FROZEN without human signature → BLOCK。"""
        version = _make_case_pack_version(state="FROZEN", signed_by_human=False)
        result = verify_case_pack_version(version)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_MODEL_SELF_SIGNED_ROLE, result.error_codes)

    def test_invalid_state_blocked(self):
        """Blocker: invalid state → BLOCK。"""
        version = build_case_pack_version(
            version_id="cpv-bad-001",
            pack_ref_and_hash=_ref_hash("cp-001", _ZERO_HASH),
            version_number=0,
            state="INVALID",
            signed_by_human=True,
            admission_decision_ref_and_hash=_ref_hash("ad-001", _ZERO_HASH),
        )
        result = verify_case_pack_version(version)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_CASE_PACK_STATE_INVALID, result.error_codes)

    def test_supersedes_ref_v0_must_be_empty(self):
        """Blocker: v0 with supersedes_ref → BLOCK。"""
        version = build_case_pack_version(
            version_id="cpv-bad-v0-001",
            pack_ref_and_hash=_ref_hash("cp-001", _ZERO_HASH),
            version_number=0,
            supersedes_ref={"version_id": "cpv-prev", "content_hash": _ZERO_HASH},
            state="DRAFT",
            admission_decision_ref_and_hash=_ref_hash("ad-001", _ZERO_HASH),
        )
        result = verify_case_pack_version(version)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_CASE_PACK_VERSION_REF_BROKEN, result.error_codes)

    def test_supersedes_ref_v1_must_be_valid(self):
        """Blocker: v1 without supersedes_ref → BLOCK。"""
        version = build_case_pack_version(
            version_id="cpv-bad-v1-001",
            pack_ref_and_hash=_ref_hash("cp-001", _ZERO_HASH),
            version_number=1,
            supersedes_ref={},
            state="DRAFT",
            admission_decision_ref_and_hash=_ref_hash("ad-001", _ZERO_HASH),
        )
        result = verify_case_pack_version(version)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_CASE_PACK_VERSION_REF_BROKEN, result.error_codes)

    def test_freeze_case_pack_version(self):
        """freeze_case_pack_version: DRAFT → FROZEN。"""
        draft = _make_case_pack_version(state="DRAFT", signed_by_human=False)
        frozen = freeze_case_pack_version(draft, signed_by_human=True)
        self.assertEqual(frozen.state, "FROZEN")
        self.assertTrue(frozen.signed_by_human)
        result = verify_case_pack_version(frozen)
        self.assertTrue(result.passed, f"verify failed: {result.details}")

    def test_check_case_pack_immutable(self):
        """check_case_pack_immutable: FROZEN without human → FAIL。"""
        version = _make_case_pack_version(state="FROZEN", signed_by_human=False)
        result = check_case_pack_immutable(version)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_CASE_PACK_NOT_IMMUTABLE, result.error_codes)

    def test_check_case_pack_immutable_pass(self):
        """check_case_pack_immutable: FROZEN with human → PASS。"""
        version = _make_case_pack_version(state="FROZEN", signed_by_human=True)
        result = check_case_pack_immutable(version)
        self.assertTrue(result.passed)

    def test_hash_deterministic(self):
        """Deterministic hash。"""
        v1 = _make_case_pack_version()
        v2 = _make_case_pack_version()
        self.assertEqual(v1.content_hash, v2.content_hash)


# ─── AdmissionDecision tests ───────────────────────────────────────────


class TestAdmissionDecision(unittest.TestCase):
    """AdmissionDecision 测试。"""

    def test_build_and_verify(self):
        """Golden: 构建 + 验证 AdmissionDecision。"""
        decision = _make_admission_decision()
        result = verify_admission_decision(decision)
        self.assertTrue(result.passed, f"verify failed: {result.details}")
        self.assertEqual(decision.gate_type, CS_GATE_TYPE_CASE_ROLE)
        self.assertTrue(decision.signed_by_human)

    def test_unsigned_admission_blocked(self):
        """Blocker: unsigned AdmissionDecision → BLOCK。"""
        decision = _make_admission_decision(signed_by_human=False)
        result = verify_admission_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_ADMISSION_DECISION_UNSIGNED, result.error_codes)

    def test_model_self_signing_blocked(self):
        """Blocker: model self-signing role → BLOCK。"""
        decision = _make_admission_decision(signed_by_human=True, signed_by_model=True)
        result = verify_admission_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_MODEL_SELF_SIGNED_ROLE, result.error_codes)

    def test_role_not_frozen_blocked(self):
        """Blocker: role not frozen (missing roles) → BLOCK。"""
        decision = build_admission_decision(
            decision_id="ad-incomplete-001",
            case_pack_ref_and_hash=_ref_hash("cp-001", _ZERO_HASH),
            admission_status="ADMITTED",
            frozen_roles=["positive"],  # Missing other roles
            signed_by_human=True,
            admitted_for_process_only=False,
            gate_decision_ref_and_hash=_ref_hash("gd-001", _ZERO_HASH),
            actor_id="human-001",
            actor_role="MATH_VERIFIER",
            nonce="nonce-incomplete-001-abcdef",
            issued_at="2026-08-14T12:00:00Z",
        )
        result = verify_admission_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_ROLE_NOT_FROZEN, result.error_codes)

    def test_unknown_role_blocked(self):
        """Blocker: unknown role in frozen_roles → BLOCK。"""
        decision = build_admission_decision(
            decision_id="ad-unknown-001",
            case_pack_ref_and_hash=_ref_hash("cp-001", _ZERO_HASH),
            admission_status="ADMITTED",
            frozen_roles=sorted(CS_CASE_ROLES) + ["unknown_role"],
            signed_by_human=True,
            admitted_for_process_only=False,
            gate_decision_ref_and_hash=_ref_hash("gd-001", _ZERO_HASH),
            actor_id="human-001",
            actor_role="MATH_VERIFIER",
            nonce="nonce-unknown-001-abcdef",
            issued_at="2026-08-14T12:00:00Z",
        )
        result = verify_admission_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_ADMISSION_ROLE_UNKNOWN, result.error_codes)

    def test_invalid_admission_status_blocked(self):
        """Blocker: invalid admission_status → BLOCK。"""
        decision = build_admission_decision(
            decision_id="ad-badstatus-001",
            case_pack_ref_and_hash=_ref_hash("cp-001", _ZERO_HASH),
            admission_status="INVALID",
            frozen_roles=sorted(CS_CASE_ROLES),
            signed_by_human=True,
            admitted_for_process_only=False,
            gate_decision_ref_and_hash=_ref_hash("gd-001", _ZERO_HASH),
            actor_id="human-001",
            actor_role="MATH_VERIFIER",
            nonce="nonce-badstatus-001-abcdef",
            issued_at="2026-08-14T12:00:00Z",
        )
        result = verify_admission_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_ADMISSION_STATE_INVALID, result.error_codes)

    def test_process_only_not_in_result_layer_pass(self):
        """check_process_only_not_in_result_layer: process-only not in result → PASS。"""
        decision = _make_admission_decision(admitted_for_process_only=True)
        result = check_process_only_not_in_result_layer(decision, result_layer_claim={"other": "data"})
        self.assertTrue(result.passed)

    def test_process_only_in_result_layer_blocked(self):
        """Blocker: process-only entering result layer → BLOCK。"""
        decision = _make_admission_decision(admitted_for_process_only=True)
        result = check_process_only_not_in_result_layer(
            decision,
            result_layer_claim={"case_pack_ref": "cp-001", "claim": "confirmatory"},
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_PROCESS_ONLY_IN_RESULT_LAYER, result.error_codes)

    def test_hash_deterministic(self):
        """Deterministic hash。"""
        d1 = _make_admission_decision()
        d2 = _make_admission_decision()
        self.assertEqual(d1.content_hash, d2.content_hash)


# ─── DualEntry tests ───────────────────────────────────────────────────


class TestDualEntry(unittest.TestCase):
    """DualEntry 双入口测试。"""

    def test_natural_entry_golden(self):
        """Golden: natural entry (P2A+P3N → CasePack)。"""
        dual = DualEntry()
        pack, fixture, result = dual.natural_entry(
            fixture_id="fix-natural-001",
            pack_id="cp-natural-001",
            problem_statement="Find the minimum of x+y given xy=1.",
            solution="By AM-GM, x+y >= 2*sqrt(xy) = 2.",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p2a_ref_and_hash=_ref_hash("p2a-001", _ZERO_HASH),
            p3n_review_refs=[_ref_hash("p3n-001", _ZERO_HASH)],
            question_draft_ref_and_hash=_ref_hash("qd-001", _ZERO_HASH),
        )
        self.assertTrue(result.passed, f"natural entry failed: {result.details}")
        self.assertIsNotNone(pack)
        self.assertIsNotNone(fixture)
        self.assertEqual(pack.entry_path, "NATURAL")
        self.assertEqual(fixture.entry_path, "NATURAL")

    def test_generated_entry_golden(self):
        """Golden: generated entry (P3A+P3B → CasePack)。"""
        dual = DualEntry()
        pack, fixture, result = dual.generated_entry(
            fixture_id="fix-generated-001",
            pack_id="cp-generated-001",
            problem_statement="Find the maximum of xy given x+y=10.",
            solution="By AM-GM, xy <= (x+y)^2/4 = 25.",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p3a_ref_and_hash=_ref_hash("p3a-001", _ZERO_HASH),
            p3b_ref_and_hash=_ref_hash("p3b-001", _ZERO_HASH),
            bare_result_refs=[_ref_hash("bare-001", _ZERO_HASH)],
            question_release_ref_and_hash=_ref_hash("qr-001", _ZERO_HASH),
        )
        self.assertTrue(result.passed, f"generated entry failed: {result.details}")
        self.assertIsNotNone(pack)
        self.assertIsNotNone(fixture)
        self.assertEqual(pack.entry_path, "GENERATED")
        self.assertEqual(fixture.entry_path, "GENERATED")

    def test_natural_entry_forged_draft_blocked(self):
        """Blocker: natural case forged draft → BLOCK。"""
        dual = DualEntry()
        pack, fixture, result = dual.natural_entry(
            fixture_id="fix-forged-001",
            pack_id="cp-forged-001",
            problem_statement="test",
            solution="test",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p2a_ref_and_hash=_ref_hash("p2a-001", _ZERO_HASH),
            p3n_review_refs=[_ref_hash("p3n-001", _ZERO_HASH)],
            question_draft_ref_and_hash=_ref_hash("qd-001", _ZERO_HASH),
            draft_is_forged=True,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_NATURAL_CASE_FORGED_DRAFT, result.error_codes)
        self.assertIsNone(pack)
        self.assertIsNone(fixture)

    def test_natural_entry_missing_p3n_blocked(self):
        """Blocker: missing P3N review refs → BLOCK。"""
        dual = DualEntry()
        pack, fixture, result = dual.natural_entry(
            fixture_id="fix-nop3n-001",
            pack_id="cp-nop3n-001",
            problem_statement="test",
            solution="test",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p2a_ref_and_hash=_ref_hash("p2a-001", _ZERO_HASH),
            p3n_review_refs=[],
            question_draft_ref_and_hash=_ref_hash("qd-001", _ZERO_HASH),
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_EVIDENCE_REF_MISSING, result.error_codes)

    def test_generated_entry_missing_bare_blocked(self):
        """Blocker: missing bare results → BLOCK。"""
        dual = DualEntry()
        pack, fixture, result = dual.generated_entry(
            fixture_id="fix-nobare-001",
            pack_id="cp-nobare-001",
            problem_statement="test",
            solution="test",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p3a_ref_and_hash=_ref_hash("p3a-001", _ZERO_HASH),
            p3b_ref_and_hash=_ref_hash("p3b-001", _ZERO_HASH),
            bare_result_refs=[],
            question_release_ref_and_hash=_ref_hash("qr-001", _ZERO_HASH),
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_EVIDENCE_REF_MISSING, result.error_codes)

    def test_dual_entry_fixture_verify(self):
        """DualEntryFixture verify。"""
        fixture = build_dual_entry_fixture(
            fixture_id="fix-001",
            entry_path="NATURAL",
            case_pack_ref_and_hash=_ref_hash("cp-001", _ZERO_HASH),
            natural_evidence=build_natural_entry_evidence(
                p2a_ref_and_hash=_ref_hash("p2a-001", _ZERO_HASH),
                p3n_review_refs=[_ref_hash("p3n-001", _ZERO_HASH)],
                question_draft_ref_and_hash=_ref_hash("qd-001", _ZERO_HASH),
            ).to_dict(),
        )
        result = verify_dual_entry_fixture(fixture)
        self.assertTrue(result.passed, f"verify failed: {result.details}")

    def test_dual_entry_fixture_invalid_path_blocked(self):
        """Blocker: invalid entry_path → BLOCK。"""
        fixture = build_dual_entry_fixture(
            fixture_id="fix-bad-001",
            entry_path="INVALID",
            case_pack_ref_and_hash=_ref_hash("cp-001", _ZERO_HASH),
        )
        result = verify_dual_entry_fixture(fixture)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_DUAL_ENTRY_PATH_INVALID, result.error_codes)

    def test_dual_entry_fixtures_tracked(self):
        """DualEntry tracks fixtures。"""
        dual = DualEntry()
        dual.natural_entry(
            fixture_id="fix-1",
            pack_id="cp-1",
            problem_statement="p", solution="s",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p2a_ref_and_hash=_ref_hash("p2a-1", _ZERO_HASH),
            p3n_review_refs=[_ref_hash("p3n-1", _ZERO_HASH)],
            question_draft_ref_and_hash=_ref_hash("qd-1", _ZERO_HASH),
        )
        dual.generated_entry(
            fixture_id="fix-2",
            pack_id="cp-2",
            problem_statement="p", solution="s",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p3a_ref_and_hash=_ref_hash("p3a-1", _ZERO_HASH),
            p3b_ref_and_hash=_ref_hash("p3b-1", _ZERO_HASH),
            bare_result_refs=[_ref_hash("bare-1", _ZERO_HASH)],
            question_release_ref_and_hash=_ref_hash("qr-1", _ZERO_HASH),
        )
        self.assertEqual(len(dual.fixtures), 2)


# ─── P3C Verifier tests ────────────────────────────────────────────────


class TestP3CVerifier(unittest.TestCase):
    """P3CVerifier 测试。"""

    def test_p3c_verify_golden(self):
        """Golden: P3C verification passes for valid case。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(case_pack_sha=pack.content_hash)
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "VERIFIED")
        self.assertTrue(report.all_roles_signed_by_human)
        self.assertTrue(report.admission_signed)
        self.assertTrue(report.roles_have_evidence)
        self.assertEqual(len(report.error_codes), 0)

    def test_p3c_verify_model_self_signed_blocked(self):
        """Blocker: model self-signing role → BLOCK。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(
            case_pack_sha=pack.content_hash,
            signed_by_human=True,
            signed_by_model=True,
        )
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "BLOCKED")
        self.assertIn("CS_MODEL_SELF_SIGNED_ROLE", report.error_codes)

    def test_p3c_verify_unsigned_admission_blocked(self):
        """Blocker: unsigned AdmissionDecision → BLOCK。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(
            case_pack_sha=pack.content_hash,
            signed_by_human=False,
        )
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "BLOCKED")
        self.assertIn("CS_ADMISSION_DECISION_UNSIGNED", report.error_codes)

    def test_p3c_verify_process_only_in_result_blocked(self):
        """Blocker: process-only entering result layer → BLOCK。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(
            case_pack_sha=pack.content_hash,
            admitted_for_process_only=True,
        )
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
            result_layer_claim={"case_pack_ref": "cp-001", "claim": "confirmatory"},
        )
        self.assertEqual(report.p3c_state, "BLOCKED")
        self.assertIn("CS_PROCESS_ONLY_IN_RESULT_LAYER", report.error_codes)

    def test_p3c_verify_process_only_not_in_result_pass(self):
        """process-only not in result layer → PASS。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(
            case_pack_sha=pack.content_hash,
            admitted_for_process_only=True,
        )
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
            result_layer_claim={"other": "data"},
        )
        self.assertEqual(report.p3c_state, "VERIFIED")

    def test_p3c_verify_role_without_evidence_blocked(self):
        """Blocker: role without evidence → BLOCK。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(case_pack_sha=pack.content_hash)
        roles = []
        for role_name in sorted(CS_CASE_ROLES):
            roles.append(build_case_role(
                role_id=f"cr-noev-{role_name}",
                case_pack_ref_id=pack.pack_id,
                role=role_name,
                evidence_refs=[],  # No evidence
                signed_by_human=True,
            ))

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "BLOCKED")
        self.assertIn("CS_ROLE_WITHOUT_EVIDENCE", report.error_codes)

    def test_p3c_verify_missing_evidence_refs_blocked(self):
        """Blocker: missing evidence refs → BLOCK。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(case_pack_sha=pack.content_hash)
        # Create roles with invalid evidence refs (missing sha256)
        roles = []
        for role_name in sorted(CS_CASE_ROLES):
            roles.append(build_case_role(
                role_id=f"cr-badref-{role_name}",
                case_pack_ref_id=pack.pack_id,
                role=role_name,
                evidence_refs=[{"ref_id": f"ev-{role_name}", "sha256": "invalid"}],
                signed_by_human=True,
            ))

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "BLOCKED")

    def test_p3c_verify_hash_mismatch_blocked(self):
        """Blocker: hash mismatch → BLOCK。"""
        pack = _make_case_pack()
        # Tamper with pack hash
        pack_dict = pack.to_dict()
        pack_dict["content_hash"] = "c" * 64
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(case_pack_sha=pack.content_hash)
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack_dict,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "BLOCKED")
        self.assertIn("CS_CASE_PACK_HASH_MISMATCH", report.error_codes)

    def test_p3c_verify_role_not_frozen_blocked(self):
        """Blocker: role not frozen (missing roles) → BLOCK。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(case_pack_sha=pack.content_hash)
        # Only provide one role
        roles = [build_case_role(
            role_id="cr-positive-only",
            case_pack_ref_id=pack.pack_id,
            role="positive",
            evidence_refs=[_ref_hash("ev-001", _ZERO_HASH)],
            signed_by_human=True,
        )]

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "BLOCKED")
        self.assertIn("CS_ROLE_NOT_FROZEN", report.error_codes)

    def test_p3c_verify_report_hash(self):
        """P3CVerificationReport hash is deterministic。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(case_pack_sha=pack.content_hash)
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        verifier = P3CVerifier()
        report1 = verifier.verify(
            case_pack=pack, case_pack_version=version,
            admission_decision=decision, case_roles=roles,
            report_id="r1",
        )
        report2 = verifier.verify(
            case_pack=pack, case_pack_version=version,
            admission_decision=decision, case_roles=roles,
            report_id="r1",
        )
        self.assertEqual(report1.report_hash, report2.report_hash)

    def test_p3c_verify_report_verify(self):
        """verify_report: verify the report itself。"""
        pack = _make_case_pack()
        version = _make_case_pack_version(pack_sha=pack.content_hash)
        decision = _make_admission_decision(case_pack_sha=pack.content_hash)
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack, case_pack_version=version,
            admission_decision=decision, case_roles=roles,
        )
        result = verifier.verify_report(report)
        self.assertTrue(result.passed, f"report verify failed: {result.details}")

    def test_p3c_blocker_check_functions(self):
        """Blocker check functions。"""
        # check_natural_case_not_forged_draft
        forged_ev = {"draft_is_forged": True}
        result = check_natural_case_not_forged_draft(forged_ev)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_NATURAL_CASE_FORGED_DRAFT, result.error_codes)

        ok_ev = {"draft_is_forged": False}
        result = check_natural_case_not_forged_draft(ok_ev)
        self.assertTrue(result.passed)

        # check_model_not_self_signing_role
        model_signed = _make_admission_decision(signed_by_model=True)
        result = check_model_not_self_signing_role(model_signed)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_MODEL_SELF_SIGNED_ROLE, result.error_codes)

        human_signed = _make_admission_decision()
        result = check_model_not_self_signing_role(human_signed)
        self.assertTrue(result.passed)

        # check_process_only_excluded_from_result
        process_only = _make_admission_decision(admitted_for_process_only=True)
        result = check_process_only_excluded_from_result(
            process_only, result_layer_claim={"ref": "cp-001"}
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_PROCESS_ONLY_IN_RESULT_LAYER, result.error_codes)


# ─── CaseLabCapabilityReport tests ─────────────────────────────────────


class TestCaseLabCapabilityReport(unittest.TestCase):
    """CaseLabCapabilityReport 测试。"""

    def test_build_and_verify(self):
        """Golden: 构建 + 验证 CaseLabCapabilityReport。"""
        report = build_case_lab_capability_report(report_id="clr-001")
        result = verify_case_lab_capability_report(report)
        self.assertTrue(result.passed, f"verify failed: {result.details}")
        self.assertTrue(report.dual_entry_fixture_support)
        self.assertTrue(report.p3c_verification)
        self.assertTrue(report.role_freezing)
        self.assertTrue(report.no_p5_claim)
        self.assertTrue(report.no_confirmatory_evidence)

    def test_side_effect_counters_zero(self):
        """所有 side_effect_counters 为 0。"""
        report = build_case_lab_capability_report(report_id="clr-002")
        for key in CS_SIDE_EFFECT_KEYS:
            self.assertEqual(report.side_effect_counters[key], 0)

    def test_allowed_output_kinds_match(self):
        """allowed_output_kinds 与常量一致。"""
        report = build_case_lab_capability_report(report_id="clr-003")
        self.assertEqual(set(report.allowed_output_kinds), set(CS_ALLOWED_OUTPUT_KINDS))

    def test_forbidden_output_kinds_match(self):
        """forbidden_output_kinds 与常量一致。"""
        report = build_case_lab_capability_report(report_id="clr-004")
        self.assertEqual(set(report.forbidden_output_kinds), set(CS_FORBIDDEN_OUTPUT_KINDS))

    def test_hash_deterministic(self):
        """Deterministic hash。"""
        r1 = build_case_lab_capability_report(report_id="clr-deterministic")
        r2 = build_case_lab_capability_report(report_id="clr-deterministic")
        self.assertEqual(r1.report_hash, r2.report_hash)

    def test_hash_mismatch_blocked(self):
        """Blocker: hash mismatch → BLOCK。"""
        report = build_case_lab_capability_report(report_id="clr-bad")
        d = report.to_dict()
        d["report_hash"] = "d" * 64
        result = verify_case_lab_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.CS_CAPABILITY_HASH_MISMATCH, result.error_codes)

    def test_no_p5_claim_in_claims(self):
        """claims 不含 P5 claim。"""
        report = build_case_lab_capability_report(report_id="clr-005")
        for claim in report.claims:
            claim_lower = claim.lower()
            self.assertFalse(
                "p5" in claim_lower and "no_p5" not in claim_lower and "not_p5" not in claim_lower,
                f"claim contains P5 claim: {claim!r}",
            )


# ─── Boundary tests ────────────────────────────────────────────────────


class TestCS1Boundary(unittest.TestCase):
    """CS1 boundary tests — allowed/forbidden output kinds。"""

    def test_cs1_output_kinds_disjoint(self):
        """allowed and forbidden output kinds are disjoint。"""
        self.assertEqual(CS_ALLOWED_OUTPUT_KINDS & CS_FORBIDDEN_OUTPUT_KINDS, frozenset())

    def test_cs1_forbidden_does_not_include_cs1_objects(self):
        """forbidden output kinds don't include CS1's own objects。"""
        cs1_objects = {
            "CasePack", "CasePackVersion", "AdmissionDecision", "CaseRole",
            "MechanismReview", "RelationMapping", "DualEntryFixture",
            "P3CVerificationReport", "CaseLabCapabilityReport",
        }
        self.assertEqual(cs1_objects & CS_FORBIDDEN_OUTPUT_KINDS, frozenset())

    def test_cs1_capability_report_boundary(self):
        """CaseLabCapabilityReport enforces boundary。"""
        report = build_case_lab_capability_report(report_id="clr-boundary")
        result = verify_case_lab_capability_report(report)
        self.assertTrue(result.passed)
        # Verify no forbidden objects in allowed
        for kind in report.allowed_output_kinds:
            self.assertNotIn(kind, CS_FORBIDDEN_OUTPUT_KINDS)

    def test_cs1_no_confirmatory_evidence(self):
        """CS1 does not produce confirmatory evidence。"""
        report = build_case_lab_capability_report(report_id="clr-no-conf")
        self.assertTrue(report.no_confirmatory_evidence)
        self.assertNotIn("ConfirmatoryEvidenceRecord", report.allowed_output_kinds)

    def test_cs1_no_p5_claim(self):
        """CS1 does not produce P5 claim。"""
        report = build_case_lab_capability_report(report_id="clr-no-p5")
        self.assertTrue(report.no_p5_claim)
        self.assertNotIn("P5ClaimRecord", report.allowed_output_kinds)


# ─── Integration: full P3C flow ────────────────────────────────────────


class TestP3CFullFlow(unittest.TestCase):
    """Full P3C flow integration tests。"""

    def test_natural_entry_to_p3c_freeze(self):
        """Full flow: natural entry → P3C role freeze。"""
        # 1. DualEntry natural path
        dual = DualEntry()
        pack, fixture, result = dual.natural_entry(
            fixture_id="fix-full-natural",
            pack_id="cp-full-natural",
            problem_statement="Find the minimum of x+y given xy=1.",
            solution="By AM-GM, x+y >= 2*sqrt(xy) = 2.",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p2a_ref_and_hash=_ref_hash("p2a-full", _ZERO_HASH),
            p3n_review_refs=[_ref_hash("p3n-full", _ZERO_HASH)],
            question_draft_ref_and_hash=_ref_hash("qd-full", _ZERO_HASH),
        )
        self.assertTrue(result.passed)

        # 2. Build AdmissionDecision
        decision = _make_admission_decision(
            case_pack_ref_id=pack.pack_id,
            case_pack_sha=pack.content_hash,
        )

        # 3. Build CasePackVersion
        version = _make_case_pack_version(
            pack_id=pack.pack_id,
            pack_sha=pack.content_hash,
        )

        # 4. Build CaseRoles
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        # 5. P3C verify
        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "VERIFIED")

    def test_generated_entry_to_p3c_freeze(self):
        """Full flow: generated entry → P3C role freeze。"""
        # 1. DualEntry generated path
        dual = DualEntry()
        pack, fixture, result = dual.generated_entry(
            fixture_id="fix-full-generated",
            pack_id="cp-full-generated",
            problem_statement="Find the maximum of xy given x+y=10.",
            solution="By AM-GM, xy <= (x+y)^2/4 = 25.",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p3a_ref_and_hash=_ref_hash("p3a-full", _ZERO_HASH),
            p3b_ref_and_hash=_ref_hash("p3b-full", _ZERO_HASH),
            bare_result_refs=[_ref_hash("bare-full", _ZERO_HASH)],
            question_release_ref_and_hash=_ref_hash("qr-full", _ZERO_HASH),
        )
        self.assertTrue(result.passed)

        # 2. Build AdmissionDecision
        decision = _make_admission_decision(
            case_pack_ref_id=pack.pack_id,
            case_pack_sha=pack.content_hash,
        )

        # 3. Build CasePackVersion
        version = _make_case_pack_version(
            pack_id=pack.pack_id,
            pack_sha=pack.content_hash,
        )

        # 4. Build CaseRoles
        roles = _make_case_roles(case_pack_ref_id=pack.pack_id)

        # 5. P3C verify
        verifier = P3CVerifier()
        report = verifier.verify(
            case_pack=pack,
            case_pack_version=version,
            admission_decision=decision,
            case_roles=roles,
        )
        self.assertEqual(report.p3c_state, "VERIFIED")

    def test_freeze_version_after_p3c(self):
        """Freeze CasePackVersion after P3C verification。"""
        dual = DualEntry()
        pack, _, result = dual.natural_entry(
            fixture_id="fix-freeze",
            pack_id="cp-freeze",
            problem_statement="p", solution="s",
            mechanism_contract_ref_and_hash=_make_mechanism_contract_ref(),
            relation_mapping_ref_and_hash=_make_relation_mapping_ref(),
            role_assignment_refs=_make_role_assignment_refs(),
            p2a_ref_and_hash=_ref_hash("p2a", _ZERO_HASH),
            p3n_review_refs=[_ref_hash("p3n", _ZERO_HASH)],
            question_draft_ref_and_hash=_ref_hash("qd", _ZERO_HASH),
        )
        self.assertTrue(result.passed)

        # Build DRAFT version
        draft = build_case_pack_version(
            version_id="cpv-freeze",
            pack_ref_and_hash=_ref_hash(pack.pack_id, pack.content_hash),
            version_number=0,
            state="DRAFT",
            signed_by_human=False,
            admission_decision_ref_and_hash=_ref_hash("ad-001", _ZERO_HASH),
        )

        # Freeze
        frozen = freeze_case_pack_version(draft, signed_by_human=True)
        self.assertEqual(frozen.state, "FROZEN")
        self.assertTrue(frozen.signed_by_human)

        # Verify frozen version
        result = verify_case_pack_version(frozen)
        self.assertTrue(result.passed, f"verify failed: {result.details}")


if __name__ == "__main__":
    unittest.main()
