"""WP-CW1 Production Cognitive Workers 测试。

测试层级：Golden → P3N → P6 → Negative → Independence → Determinism → Boundary → Constants
覆盖：
- RoleQualificationMatrix build + cell lookup + production routing with PASS cell
- P3N workers: trace_analyst, solution_analyst, adjudicator with DB lease/reconcile
- P6 workers: process_auditor, proof_judge, leakage_auditor with blinding + independence
- Negative: unqualified cell routed, same session author+reviewer, judge reads
  unauthorized view, fake independence, no fallback, missing conclusion, wildcard
  rejected, hash mismatch, lease acquire failed, fence mismatch
- Independence enforcement tests
- Deterministic hash tests
- CW1 boundary tests (allowed/forbidden output kinds)
- All constants verified

所有 blocker test 失败 → 工作包 FAIL。
"""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import (
    CW_P3N_ROLES,
    CW_P6_ROLES,
    CW_CELL_STATUSES,
    CW_CELL_CONCLUSIONS,
    CW_COMPLETENESS_KINDS,
    CW_INDEPENDENCE_KINDS,
    CW_ALLOWED_OUTPUT_KINDS,
    CW_FORBIDDEN_OUTPUT_KINDS,
    CW_ROUTER_DECISIONS,
    CW_QUALIFICATION_SCOPES,
    CW_WILDCARD_SENTINELS,
    CW_CHECK_IDS,
    CW_CLAIMS,
    CW_NONCLAIMS,
    CW_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.cognitive.production.role_qualification_matrix import (
    RoleQualificationCell,
    RoleQualificationMatrix,
    Completeness,
    build_role_qualification_cell,
    build_role_qualification_matrix,
    verify_role_qualification_cell,
    verify_role_qualification_matrix,
    verify_completeness,
    compute_completeness,
    compute_cell_key,
)
from seven_system.cognitive.production.production_role_router import (
    ProductionRoleRouter,
    RouterDecision,
)
from seven_system.cognitive.production.independence_enforcer import (
    IndependenceEnforcer,
    WorkerSession,
    IndependenceViolation,
)
from seven_system.cognitive.production.production_workers import (
    P3NWorkers,
    P6Workers,
    DBLeaseReconcileIntegration,
    WorkerState,
)
from seven_system.cognitive.production.worker_capability_report import (
    build_worker_capability_report,
    verify_worker_capability_report,
    WORKER_REPORT_SCHEMA_VERSION,
    WORKER_REPORT_SCOPE,
)


# ─── helpers ────────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64
_TS = "2026-08-14T12:00:00Z"


def _ref(ref_id: str, sha256: str = _ZERO_HASH) -> dict[str, str]:
    return {"ref": ref_id, "sha256": sha256}


def _profile_hash(model: str = "glm-5-2", carrier: str = "devin") -> str:
    return hashlib.sha256(canonical_json_bytes({"model": model, "carrier": carrier})).hexdigest()


def _make_cell(
    *,
    role_type_id: str = "trace_analyst",
    carrier_id: str = "devin",
    model_id: str = "glm-5-2",
    qualification_level: str = "PRODUCTION",
    verdict: str = "PASS",
    carrier_profile_hash: str | None = None,
    cell_id: str = "cell-001",
    valid_until: str | None = _TS,
) -> RoleQualificationCell:
    """构建一个合法的 RoleQualificationCell。"""
    cph = carrier_profile_hash or _profile_hash()
    cap_report = [_ref("cap-report-001")] if verdict == "PASS" else []
    evidence = [_ref("evidence-001")] if verdict in ("PASS", "PARTIAL", "FAIL", "BLOCKED", "EXPIRED") else []
    return build_role_qualification_cell(
        qualification_cell_id=cell_id,
        role_type_id=role_type_id,
        carrier_id=carrier_id,
        model_id=model_id,
        carrier_profile_ref_and_hash=_ref("profile-001", cph),
        input_view_ref_and_hash=_ref("view-001"),
        input_view_policy_ref_and_hash=_ref("view-policy-001"),
        input_acl_policy_ref_and_hash=_ref("acl-policy-001"),
        vault_access_capability_ref_and_hash=_ref("vault-cap-001"),
        tool_network_sandbox_policy_ref_and_hash=_ref("tool-policy-001"),
        output_sensitivity_and_sink_policy_ref_and_hash=_ref("sink-policy-001"),
        prompt_release_ref_and_hash=_ref("prompt-001"),
        output_schema_ref_and_hash=_ref("output-schema-001"),
        adapter_ref_and_hash=_ref("adapter-001"),
        parser_ref_and_hash=_ref("parser-001"),
        capability_requirement_ref_and_hash=_ref("cap-req-001"),
        qualification_level=qualification_level,
        verdict=verdict,
        capability_report_refs_and_hashes=cap_report,
        evidence_bundle_refs_and_hashes=evidence,
        valid_from=_TS,
        valid_until=valid_until,
    )


def _make_matrix(
    *,
    cells: list[RoleQualificationCell],
    required_cell_keys: list[str] | None = None,
    qualification_scope: str = "PRODUCTION",
    matrix_id: str = "matrix-001",
    matrix_version: int = 1,
) -> RoleQualificationMatrix:
    """构建一个 RoleQualificationMatrix。"""
    if required_cell_keys is None:
        required_cell_keys = [c.cell_key for c in cells]
    return build_role_qualification_matrix(
        matrix_id=matrix_id,
        matrix_version=matrix_version,
        role_type_registry_ref_and_hash=_ref("registry-001"),
        runtime_manifest_ref_and_hash=_ref("manifest-001"),
        qualification_scope=qualification_scope,
        cells=cells,
        required_cell_keys=required_cell_keys,
        generated_at=_TS,
        issuer_principal_id="issuer-001",
    )


def _make_router(matrix: RoleQualificationMatrix) -> ProductionRoleRouter:
    return ProductionRoleRouter(matrix=matrix)


def _make_p3n(
    matrix: RoleQualificationMatrix,
    db_integration: DBLeaseReconcileIntegration | None = None,
) -> P3NWorkers:
    return P3NWorkers(
        router=_make_router(matrix),
        db_integration=db_integration or DBLeaseReconcileIntegration(),
    )


def _make_p6(
    matrix: RoleQualificationMatrix,
    db_integration: DBLeaseReconcileIntegration | None = None,
) -> P6Workers:
    return P6Workers(
        router=_make_router(matrix),
        db_integration=db_integration or DBLeaseReconcileIntegration(),
    )


# ─── Constants verification ─────────────────────────────────────────────


class TestCW1Constants(unittest.TestCase):
    """验证所有 CW1 常量集合。"""

    def test_p3n_roles(self):
        self.assertEqual(CW_P3N_ROLES, frozenset({"trace_analyst", "solution_analyst", "adjudicator"}))

    def test_p6_roles(self):
        self.assertEqual(
            CW_P6_ROLES,
            frozenset({"process_auditor", "proof_judge", "leakage_auditor"}),
        )

    def test_cell_statuses(self):
        self.assertEqual(
            CW_CELL_STATUSES,
            frozenset({"NOT_TESTED", "PASS", "PARTIAL", "FAIL", "BLOCKED", "EXPIRED"}),
        )

    def test_cell_conclusions(self):
        self.assertEqual(CW_CELL_CONCLUSIONS, frozenset({"PASS", "NOT_TESTED", "FAILED"}))

    def test_completeness_kinds(self):
        self.assertEqual(
            CW_COMPLETENESS_KINDS,
            frozenset({
                "required_cell_keys",
                "pass_cell_keys",
                "not_tested_cell_keys",
                "failed_cell_keys",
                "extra_cell_keys",
                "missing_cell_keys",
                "remainder_cell_keys",
            }),
        )

    def test_independence_kinds(self):
        self.assertEqual(
            CW_INDEPENDENCE_KINDS,
            frozenset({
                "DIFFERENT_SESSION",
                "DIFFERENT_MODEL",
                "DIFFERENT_CARRIER",
                "BLINDED_VIEW",
                "SAME_MODEL_FRESH_SESSION",
            }),
        )

    def test_allowed_output_kinds(self):
        self.assertIn("MechanismContract", CW_ALLOWED_OUTPUT_KINDS)
        self.assertIn("RunAudit", CW_ALLOWED_OUTPUT_KINDS)
        self.assertIn("CognitiveWorkerCapabilityReport", CW_ALLOWED_OUTPUT_KINDS)

    def test_forbidden_output_kinds(self):
        self.assertIn("DatabaseSchemaStateReport", CW_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("TargetSolverRunArtifact", CW_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SolverDispatchReceipt", CW_FORBIDDEN_OUTPUT_KINDS)

    def test_router_decisions(self):
        self.assertEqual(
            CW_ROUTER_DECISIONS,
            frozenset({"DISPATCH", "BLOCK", "BLOCK_UNQUALIFIED", "BLOCK_NO_PASS_CELL", "BLOCK_EXPIRED"}),
        )

    def test_qualification_scopes(self):
        self.assertEqual(CW_QUALIFICATION_SCOPES, frozenset({"CANARY", "PRODUCTION"}))

    def test_wildcard_sentinels(self):
        self.assertIn("*", CW_WILDCARD_SENTINELS)
        self.assertIn("?", CW_WILDCARD_SENTINELS)
        self.assertIn("ANY", CW_WILDCARD_SENTINELS)
        self.assertIn("ALL", CW_WILDCARD_SENTINELS)
        self.assertIn("DEFAULT", CW_WILDCARD_SENTINELS)

    def test_check_ids(self):
        self.assertEqual(len(CW_CHECK_IDS), 15)
        self.assertTrue(all(cid.startswith("cw1.") for cid in CW_CHECK_IDS))

    def test_claims(self):
        self.assertEqual(len(CW_CLAIMS), 15)
        self.assertIn("role_qualification_matrix_build_verified", CW_CLAIMS)

    def test_nonclaims(self):
        self.assertEqual(len(CW_NONCLAIMS), 5)

    def test_side_effect_keys(self):
        self.assertEqual(len(CW_SIDE_EFFECT_KEYS), 6)
        self.assertIn("database_writes", CW_SIDE_EFFECT_KEYS)
        self.assertIn("solver_launches", CW_SIDE_EFFECT_KEYS)

    def test_error_codes_exist(self):
        """验证所有 CW1 error codes 存在。"""
        for code_name in [
            "CW_UNQUALIFIED_CELL_ROUTED",
            "CW_SAME_SESSION_AUTHOR_REVIEWER",
            "CW_JUDGE_READ_UNAUTHORIZED_VIEW",
            "CW_FAKE_INDEPENDENCE_SAME_MODEL",
            "CW_NO_FALLBACK_CARRIER",
            "CW_CELL_CONCLUSION_MISSING",
            "CW_MATRIX_WILDCARD_REJECTED",
            "CW_MATRIX_HASH_MISMATCH",
            "CW_LEASE_ACQUIRE_FAILED",
            "CW_RECONCILE_FENCE_MISMATCH",
            "CW_WORKER_NOT_INDEPENDENT",
            "CW_CELL_COMPLETENESS_REMAINDER_NONZERO",
            "CW_PROFILE_HASH_MISMATCH",
            "CW_ROLE_TYPE_UNKNOWN",
            "CW_CELL_KEY_MISMATCH",
            "CW_CELL_VERDICT_INVALID",
            "CW_QUALIFICATION_SCOPE_INVALID",
            "CW_CELL_EXPIRED",
            "CW_CELL_INVALIDATED",
            "CW_BLINDING_VIOLATED",
            "CW_VIEW_POLICY_MISMATCH",
            "CW_OUTPUT_KIND_FORBIDDEN",
            "CW_WORKER_SESSION_REUSE",
            "CW_MATRIX_SUPERSEDES_REF_INVALID",
            "CW_COMPLETENESS_SETS_NOT_DISJOINT",
            "CW_COMPLETENESS_VERDICT_INVALID",
        ]:
            self.assertTrue(hasattr(EC, code_name), f"missing error code: {code_name}")


# ─── RoleQualificationCell tests ────────────────────────────────────────


class TestRoleQualificationCell(unittest.TestCase):
    """RoleQualificationCell 构建与验证。"""

    def test_build_and_verify_pass_cell(self):
        cell = _make_cell(verdict="PASS")
        result = verify_role_qualification_cell(cell)
        self.assertTrue(result.passed, f"errors: {result.details}")
        self.assertTrue(cell.is_pass)
        self.assertTrue(cell.is_production)
        self.assertTrue(cell.has_conclusion)
        self.assertEqual(cell.conclusion, "PASS")

    def test_build_not_tested_cell(self):
        cell = _make_cell(verdict="NOT_TESTED", valid_until=None)
        result = verify_role_qualification_cell(cell)
        self.assertTrue(result.passed, f"errors: {result.details}")
        self.assertFalse(cell.is_pass)
        self.assertTrue(cell.has_conclusion)
        self.assertEqual(cell.conclusion, "NOT_TESTED")

    def test_build_failed_cell(self):
        cell = _make_cell(verdict="FAIL")
        result = verify_role_qualification_cell(cell)
        self.assertTrue(result.passed, f"errors: {result.details}")
        self.assertTrue(cell.has_conclusion)
        self.assertEqual(cell.conclusion, "FAILED")

    def test_build_partial_cell(self):
        cell = _make_cell(verdict="PARTIAL")
        result = verify_role_qualification_cell(cell)
        self.assertTrue(result.passed, f"errors: {result.details}")
        self.assertEqual(cell.conclusion, "FAILED")

    def test_build_blocked_cell(self):
        cell = _make_cell(verdict="BLOCKED")
        result = verify_role_qualification_cell(cell)
        self.assertTrue(result.passed, f"errors: {result.details}")
        self.assertEqual(cell.conclusion, "FAILED")

    def test_build_expired_cell(self):
        cell = _make_cell(verdict="EXPIRED")
        result = verify_role_qualification_cell(cell)
        self.assertTrue(result.passed, f"errors: {result.details}")
        self.assertTrue(cell.is_expired)
        self.assertEqual(cell.conclusion, "FAILED")

    def test_cell_key_deterministic(self):
        """相同字段 → 相同 cell_key。"""
        cell1 = _make_cell(cell_id="cell-a")
        cell2 = _make_cell(cell_id="cell-b")
        # cell_id 不参与 cell_key 计算
        self.assertEqual(cell1.cell_key, cell2.cell_key)

    def test_cell_key_differs_on_role(self):
        cell1 = _make_cell(role_type_id="trace_analyst")
        cell2 = _make_cell(role_type_id="solution_analyst")
        self.assertNotEqual(cell1.cell_key, cell2.cell_key)

    def test_cell_key_differs_on_carrier(self):
        cell1 = _make_cell(carrier_id="devin")
        cell2 = _make_cell(carrier_id="codex")
        self.assertNotEqual(cell1.cell_key, cell2.cell_key)

    def test_cell_key_differs_on_scope(self):
        cell1 = _make_cell(qualification_level="PRODUCTION")
        cell2 = _make_cell(qualification_level="CANARY")
        self.assertNotEqual(cell1.cell_key, cell2.cell_key)

    def test_wildcard_rejected_in_role_type_id(self):
        """通配符哨兵在 role_type_id 中被拒绝。"""
        cell = _make_cell(role_type_id="ANY")
        result = verify_role_qualification_cell(cell)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_MATRIX_WILDCARD_REJECTED, result.error_codes)

    def test_wildcard_rejected_in_carrier_id(self):
        cell = _make_cell(carrier_id="*")
        result = verify_role_qualification_cell(cell)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_MATRIX_WILDCARD_REJECTED, result.error_codes)

    def test_wildcard_rejected_in_model_id(self):
        cell = _make_cell(model_id="DEFAULT")
        result = verify_role_qualification_cell(cell)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_MATRIX_WILDCARD_REJECTED, result.error_codes)

    def test_glob_char_rejected(self):
        cell = _make_cell(carrier_id="devin?")
        result = verify_role_qualification_cell(cell)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_MATRIX_WILDCARD_REJECTED, result.error_codes)

    def test_invalid_verdict_rejected(self):
        cell = _make_cell(verdict="UNKNOWN")
        result = verify_role_qualification_cell(cell)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_CELL_VERDICT_INVALID, result.error_codes)

    def test_invalid_qualification_level_rejected(self):
        cell = _make_cell(qualification_level="STAGING")
        result = verify_role_qualification_cell(cell)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_QUALIFICATION_SCOPE_INVALID, result.error_codes)

    def test_pass_cell_requires_capability_report(self):
        """PASS cell 必须有 capability_report_refs。"""
        cell = _make_cell(verdict="PASS")
        # 手动构建一个没有 cap_report 的 PASS cell
        cell_dict = cell.to_dict()
        cell_dict["capability_report_refs_and_hashes"] = []
        result = verify_role_qualification_cell(cell_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_pass_cell_requires_evidence(self):
        cell = _make_cell(verdict="PASS")
        cell_dict = cell.to_dict()
        cell_dict["evidence_bundle_refs_and_hashes"] = []
        result = verify_role_qualification_cell(cell_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_pass_cell_requires_valid_until(self):
        cell = _make_cell(verdict="PASS", valid_until=None)
        result = verify_role_qualification_cell(cell)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_not_tested_cell_must_have_empty_reports(self):
        """NOT_TESTED cell 必须没有 capability_report_refs。"""
        cell = _make_cell(verdict="NOT_TESTED", valid_until=None)
        cell_dict = cell.to_dict()
        cell_dict["capability_report_refs_and_hashes"] = [_ref("cap-001")]
        result = verify_role_qualification_cell(cell_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_cell_key_mismatch_detected(self):
        """cell_key 不匹配被检测。"""
        cell = _make_cell()
        cell_dict = cell.to_dict()
        cell_dict["cell_key"] = "a" * 64  # 错误的 key
        result = verify_role_qualification_cell(cell_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_CELL_KEY_MISMATCH, result.error_codes)

    def test_to_dict_roundtrip(self):
        cell = _make_cell()
        d = cell.to_dict()
        self.assertIn("qualification_cell_id", d)
        self.assertIn("cell_key", d)
        self.assertIn("verdict", d)


# ─── RoleQualificationMatrix tests ──────────────────────────────────────


class TestRoleQualificationMatrix(unittest.TestCase):
    """RoleQualificationMatrix 构建与验证。"""

    def test_build_and_verify_matrix(self):
        cell = _make_cell()
        matrix = _make_matrix(cells=[cell])
        result = verify_role_qualification_matrix(matrix)
        self.assertTrue(result.passed, f"errors: {result.details}")
        self.assertTrue(matrix.is_production)
        self.assertEqual(len(matrix.cells), 1)

    def test_matrix_hash_deterministic(self):
        """相同内容 → 相同 matrix_hash。"""
        cell = _make_cell()
        m1 = _make_matrix(cells=[cell], matrix_id="m-1")
        m2 = _make_matrix(cells=[cell], matrix_id="m-1")
        self.assertEqual(m1.matrix_hash, m2.matrix_hash)

    def test_matrix_hash_differs_on_cells(self):
        cell1 = _make_cell(role_type_id="trace_analyst")
        cell2 = _make_cell(role_type_id="solution_analyst")
        m1 = _make_matrix(cells=[cell1], matrix_id="m-1")
        m2 = _make_matrix(cells=[cell2], matrix_id="m-1")
        self.assertNotEqual(m1.matrix_hash, m2.matrix_hash)

    def test_get_cell_by_key(self):
        cell = _make_cell()
        matrix = _make_matrix(cells=[cell])
        found = matrix.get_cell_by_key(cell.cell_key)
        self.assertIsNotNone(found)
        self.assertEqual(found.qualification_cell_id, cell.qualification_cell_id)

    def test_get_cells_by_role(self):
        cell1 = _make_cell(role_type_id="trace_analyst", cell_id="c1")
        cell2 = _make_cell(role_type_id="solution_analyst", cell_id="c2")
        matrix = _make_matrix(cells=[cell1, cell2])
        trace_cells = matrix.get_cells_by_role("trace_analyst")
        self.assertEqual(len(trace_cells), 1)

    def test_get_production_pass_cells(self):
        cell_pass = _make_cell(role_type_id="trace_analyst", verdict="PASS", cell_id="c1")
        cell_not_tested = _make_cell(role_type_id="trace_analyst", verdict="NOT_TESTED", cell_id="c2", valid_until=None)
        matrix = _make_matrix(cells=[cell_pass, cell_not_tested])
        pass_cells = matrix.get_production_pass_cells("trace_analyst")
        self.assertEqual(len(pass_cells), 1)
        self.assertEqual(pass_cells[0].qualification_cell_id, "c1")

    def test_matrix_wildcard_rejected_in_matrix_id(self):
        cell = _make_cell()
        matrix = _make_matrix(cells=[cell], matrix_id="ANY")
        result = verify_role_qualification_matrix(matrix)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_MATRIX_WILDCARD_REJECTED, result.error_codes)

    def test_matrix_hash_mismatch_detected(self):
        cell = _make_cell()
        matrix = _make_matrix(cells=[cell])
        matrix_dict = matrix.to_dict()
        matrix_dict["matrix_hash"] = "b" * 64
        result = verify_role_qualification_matrix(matrix_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_MATRIX_HASH_MISMATCH, result.error_codes)

    def test_matrix_invalid_scope_rejected(self):
        cell = _make_cell()
        matrix = _make_matrix(cells=[cell], qualification_scope="STAGING")
        result = verify_role_qualification_matrix(matrix)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_QUALIFICATION_SCOPE_INVALID, result.error_codes)

    def test_duplicate_cell_key_rejected(self):
        cell1 = _make_cell(cell_id="c1")
        cell2 = _make_cell(cell_id="c2")  # same fields → same cell_key
        matrix = _make_matrix(cells=[cell1, cell2])
        result = verify_role_qualification_matrix(matrix)
        self.assertFalse(result.passed)

    def test_supersedes_ref(self):
        cell = _make_cell()
        matrix = _make_matrix(
            cells=[cell],
            matrix_version=2,
        )
        # 手动构建带 supersedes_ref 的 matrix
        matrix_dict = matrix.to_dict()
        matrix_dict["supersedes_ref"] = _ref("matrix-001@1")
        # 重新计算 hash
        obj = dict(matrix_dict)
        obj["matrix_hash"] = None
        matrix_dict["matrix_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_role_qualification_matrix(matrix_dict)
        self.assertTrue(result.passed, f"errors: {result.details}")


# ─── Completeness tests ─────────────────────────────────────────────────


class TestCompleteness(unittest.TestCase):
    """Completeness 集合计算与验证。"""

    def test_all_pass_completeness(self):
        """所有 required cell 都 PASS → completeness PASS。"""
        cell = _make_cell(verdict="PASS")
        comp = compute_completeness(
            required_cell_keys=[cell.cell_key],
            cells=[cell],
            algorithm_ref_and_hash=_ref("algo-001"),
        )
        self.assertEqual(comp.verdict, "PASS")
        self.assertEqual(comp.remainder_count, 0)
        result = verify_completeness(comp)
        self.assertTrue(result.passed, f"errors: {result.details}")

    def test_not_tested_in_completeness(self):
        """NOT_TESTED cell → remainder 非空 → BLOCKED。"""
        cell = _make_cell(verdict="NOT_TESTED", valid_until=None)
        comp = compute_completeness(
            required_cell_keys=[cell.cell_key],
            cells=[cell],
            algorithm_ref_and_hash=_ref("algo-001"),
        )
        self.assertEqual(comp.verdict, "BLOCKED")
        self.assertEqual(comp.remainder_count, 1)
        self.assertIn(cell.cell_key, comp.not_tested_cell_keys)
        self.assertIn(cell.cell_key, comp.remainder_cell_keys)

    def test_missing_cell(self):
        """required 中有但 observed 中没有 → missing。"""
        cell = _make_cell(verdict="PASS")
        comp = compute_completeness(
            required_cell_keys=[cell.cell_key, "missing-key"],
            cells=[cell],
            algorithm_ref_and_hash=_ref("algo-001"),
        )
        self.assertEqual(comp.verdict, "BLOCKED")
        self.assertIn("missing-key", comp.missing_cell_keys)

    def test_extra_cell(self):
        """observed 中有但 required 中没有 → extra。"""
        cell = _make_cell(verdict="PASS")
        comp = compute_completeness(
            required_cell_keys=[],
            cells=[cell],
            algorithm_ref_and_hash=_ref("algo-001"),
        )
        self.assertEqual(comp.verdict, "BLOCKED")
        self.assertIn(cell.cell_key, comp.extra_cell_keys)

    def test_failed_cell(self):
        """FAIL cell → failed 集合。"""
        cell = _make_cell(verdict="FAIL")
        comp = compute_completeness(
            required_cell_keys=[cell.cell_key],
            cells=[cell],
            algorithm_ref_and_hash=_ref("algo-001"),
        )
        self.assertEqual(comp.verdict, "BLOCKED")
        self.assertIn(cell.cell_key, comp.failed_cell_keys)

    def test_completeness_sets_disjoint(self):
        """pass/not_tested/failed 互斥。"""
        cell = _make_cell(verdict="PASS")
        comp = compute_completeness(
            required_cell_keys=[cell.cell_key],
            cells=[cell],
            algorithm_ref_and_hash=_ref("algo-001"),
        )
        result = verify_completeness(comp)
        self.assertTrue(result.passed)

    def test_completeness_verdict_invalid_when_pass_but_remainder_nonzero(self):
        comp_dict = {
            "required_cell_keys": ["a"],
            "pass_cell_keys": ["a"],
            "not_tested_cell_keys": ["b"],
            "failed_cell_keys": [],
            "extra_cell_keys": ["b"],
            "missing_cell_keys": [],
            "remainder_cell_keys": ["b"],
            "remainder_count": 1,
            "verdict": "PASS",  # 错误：remainder 非零但 verdict=PASS
            "algorithm_ref_and_hash": _ref("algo-001"),
        }
        result = verify_completeness(comp_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_COMPLETENESS_VERDICT_INVALID, result.error_codes)


# ─── ProductionRoleRouter tests ─────────────────────────────────────────


class TestProductionRoleRouter(unittest.TestCase):
    """ProductionRoleRouter 路由测试。"""

    def test_golden_path_dispatch_with_pass_cell(self):
        """Golden path: PASS cell → DISPATCH。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        decision = router.route(
            role_type_id="trace_analyst",
            carrier_id="devin",
            model_id="glm-5-2",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
        )
        self.assertTrue(decision.is_dispatch)
        self.assertEqual(decision.decision, "DISPATCH")
        self.assertIsNotNone(decision.cell)

    def test_no_pass_cell_blocks(self):
        """No exact PRODUCTION PASS cell → BLOCK (no fallback)。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="NOT_TESTED", valid_until=None)
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        decision = router.route(
            role_type_id="trace_analyst",
            carrier_id="devin",
            model_id="glm-5-2",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
        )
        self.assertTrue(decision.is_block)
        self.assertEqual(decision.decision, "BLOCK_UNQUALIFIED")
        self.assertIn(EC.CW_UNQUALIFIED_CELL_ROUTED, decision.error_codes)

    def test_no_cell_at_all_blocks_no_fallback(self):
        """No cell for role → BLOCK_NO_PASS_CELL, no fallback to another carrier。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        # 查找不存在的 role
        decision = router.route(
            role_type_id="solution_analyst",
            carrier_id="devin",
            model_id="glm-5-2",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
        )
        self.assertTrue(decision.is_block)
        self.assertEqual(decision.decision, "BLOCK_NO_PASS_CELL")
        self.assertIn(EC.CW_NO_FALLBACK_CARRIER, decision.error_codes)

    def test_no_fallback_to_different_carrier(self):
        """有 devin PASS cell，但请求 codex → BLOCK，不 fallback 到 devin。"""
        cell = _make_cell(role_type_id="trace_analyst", carrier_id="devin", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        decision = router.route(
            role_type_id="trace_analyst",
            carrier_id="codex",  # 不同 carrier
            model_id="glm-5-2",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
        )
        self.assertTrue(decision.is_block)
        self.assertEqual(decision.decision, "BLOCK_NO_PASS_CELL")
        self.assertIn(EC.CW_NO_FALLBACK_CARRIER, decision.error_codes)

    def test_expired_cell_blocks(self):
        """EXPIRED cell → BLOCK_EXPIRED。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="EXPIRED")
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        decision = router.route(
            role_type_id="trace_analyst",
            carrier_id="devin",
            model_id="glm-5-2",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
        )
        self.assertTrue(decision.is_block)
        self.assertEqual(decision.decision, "BLOCK_EXPIRED")
        self.assertIn(EC.CW_CELL_EXPIRED, decision.error_codes)

    def test_canary_scope_matrix_blocks_production_router(self):
        """CANARY scope 矩阵不能用于 production router。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS", qualification_level="CANARY")
        matrix = _make_matrix(cells=[cell], qualification_scope="CANARY")
        router = _make_router(matrix)
        decision = router.route(
            role_type_id="trace_analyst",
            carrier_id="devin",
            model_id="glm-5-2",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
        )
        self.assertTrue(decision.is_block)
        self.assertIn(EC.CW_QUALIFICATION_SCOPE_INVALID, decision.error_codes)

    def test_profile_hash_mismatch_blocks(self):
        """carrier_profile_hash 不匹配 → BLOCK。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        decision = router.route(
            role_type_id="trace_analyst",
            carrier_id="devin",
            model_id="glm-5-2",
            carrier_profile_hash="e" * 64,  # 不匹配的 hash
        )
        self.assertTrue(decision.is_block)

    def test_verify_all_production_cells_have_conclusions_pass(self):
        cell = _make_cell(verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        result = router.verify_all_production_cells_have_conclusions()
        self.assertTrue(result.passed)

    def test_verify_all_production_cells_have_conclusions_missing(self):
        """cell 没有结论 → CW_CELL_CONCLUSION_MISSING。"""
        # 构建一个 verdict 不在结论集合中的 cell（通过手动修改）
        cell = _make_cell(verdict="PASS")
        cell_dict = cell.to_dict()
        cell_dict["verdict"] = "UNKNOWN_STATUS"
        # 重新构建 matrix 用 dict
        matrix = _make_matrix(cells=[cell])
        # 手动替换 matrix 中的 cell verdict
        matrix_dict = matrix.to_dict()
        matrix_dict["cells"][0]["verdict"] = "UNKNOWN_STATUS"
        # 重新计算 hash
        obj = dict(matrix_dict)
        obj["matrix_hash"] = None
        matrix_dict["matrix_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        # 重新构建 router 用修改后的 matrix
        from seven_system.cognitive.production.role_qualification_matrix import RoleQualificationMatrix
        # 直接用原始 matrix 但手动检查
        # 由于 cell 是 frozen，我们用 router 的 verify 方法直接检查
        # 构建一个自定义 matrix 对象
        class FakeMatrix:
            cells = [type(cell)(**{**cell.to_dict(), "verdict": "UNKNOWN_STATUS"})]
        router = ProductionRoleRouter(matrix=matrix)  # type: ignore
        # 替换 cells
        router.matrix.cells = tuple(FakeMatrix.cells)
        result = router.verify_all_production_cells_have_conclusions()
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_CELL_CONCLUSION_MISSING, result.error_codes)


# ─── P3N Workers tests ──────────────────────────────────────────────────


class TestP3NWorkers(unittest.TestCase):
    """P3N workers 测试。"""

    def test_p3n_trace_analyst_dispatch(self):
        """trace_analyst worker 成功 dispatch。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        p3n = _make_p3n(matrix)
        state = p3n.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-trace-001",
            session_id="session-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-001",
        )
        self.assertEqual(state.state, "COMPLETED")
        self.assertTrue(state.sealed)
        self.assertEqual(state.output_kind, "MechanismContract")
        self.assertNotEqual(state.output_hash, "")
        self.assertNotEqual(state.fence_token, 0)

    def test_p3n_solution_analyst_dispatch(self):
        cell = _make_cell(role_type_id="solution_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        p3n = _make_p3n(matrix)
        state = p3n.dispatch_worker(
            role_type_id="solution_analyst",
            worker_id="w-sol-001",
            session_id="session-002",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-002",
        )
        self.assertEqual(state.state, "COMPLETED")
        self.assertEqual(state.output_kind, "RelationMapping")

    def test_p3n_adjudicator_dispatch(self):
        cell = _make_cell(role_type_id="adjudicator", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        p3n = _make_p3n(matrix)
        state = p3n.dispatch_worker(
            role_type_id="adjudicator",
            worker_id="w-adj-001",
            session_id="session-003",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-003",
        )
        self.assertEqual(state.state, "COMPLETED")
        self.assertEqual(state.output_kind, "NaturalCaseReviewBundle")

    def test_p3n_db_lease_acquired_and_released(self):
        """DB lease 被获取和释放，WorkEvent 被记录。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        db = DBLeaseReconcileIntegration()
        p3n = _make_p3n(matrix, db_integration=db)
        p3n.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-trace-001",
            session_id="session-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-001",
        )
        # 检查 WorkEvent 被记录
        events = db.events
        self.assertGreater(len(events), 0)
        event_types = [e.event_type for e in events]
        self.assertIn("LEASE_ACQUIRED", event_types)
        self.assertIn("LEASE_RELEASED", event_types)
        self.assertIn("WORK_ITEM_STATE_CHANGED", event_types)

    def test_p3n_unknown_role_blocks(self):
        """未知角色 → FAILED。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        p3n = _make_p3n(matrix)
        state = p3n.dispatch_worker(
            role_type_id="question_architect",  # 不在 P3N 角色集中
            worker_id="w-bad-001",
            session_id="session-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-001",
        )
        self.assertEqual(state.state, "FAILED")
        self.assertIn(EC.CW_ROLE_TYPE_UNKNOWN, state.error_codes)

    def test_p3n_unqualified_cell_blocks(self):
        """未合格 cell → FAILED。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="NOT_TESTED", valid_until=None)
        matrix = _make_matrix(cells=[cell])
        p3n = _make_p3n(matrix)
        state = p3n.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-trace-001",
            session_id="session-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-001",
        )
        self.assertEqual(state.state, "FAILED")
        self.assertIn(EC.CW_UNQUALIFIED_CELL_ROUTED, state.error_codes)

    def test_p3n_no_pass_cell_blocks(self):
        """没有 PASS cell → FAILED。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        p3n = _make_p3n(matrix)
        state = p3n.dispatch_worker(
            role_type_id="solution_analyst",  # 没有 solution_analyst cell
            worker_id="w-sol-001",
            session_id="session-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-001",
        )
        self.assertEqual(state.state, "FAILED")
        self.assertIn(EC.CW_NO_FALLBACK_CARRIER, state.error_codes)

    def test_p3n_reconcile_fence_match(self):
        """reconcile fence 匹配 → 无错误。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        db = DBLeaseReconcileIntegration()
        p3n = _make_p3n(matrix, db_integration=db)
        state = p3n.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-trace-001",
            session_id="session-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-001",
        )
        errors = p3n.reconcile_worker("w-trace-001", state.fence_token)
        self.assertEqual(errors, [])

    def test_p3n_reconcile_fence_mismatch(self):
        """reconcile fence 不匹配 → CW_RECONCILE_FENCE_MISMATCH。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        db = DBLeaseReconcileIntegration()
        p3n = _make_p3n(matrix, db_integration=db)
        p3n.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-trace-001",
            session_id="session-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="view-001",
        )
        errors = p3n.reconcile_worker("w-trace-001", 999)  # 错误的 fence
        self.assertIn(EC.CW_RECONCILE_FENCE_MISMATCH, errors)


# ─── P6 Workers tests ───────────────────────────────────────────────────


class TestP6Workers(unittest.TestCase):
    """P6 workers 测试。"""

    def _make_p6_matrix(self) -> RoleQualificationMatrix:
        """构建包含三个 P6 PASS cell 的矩阵。"""
        cells = [
            _make_cell(role_type_id="process_auditor", verdict="PASS", cell_id="c-pa"),
            _make_cell(role_type_id="proof_judge", verdict="PASS", cell_id="c-pj"),
            _make_cell(role_type_id="leakage_auditor", verdict="PASS", cell_id="c-la"),
        ]
        return _make_matrix(cells=cells)

    def test_p6_process_auditor_dispatch(self):
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        state = p6.dispatch_auditor(
            role_type_id="process_auditor",
            worker_id="w-pa-001",
            session_id="session-pa",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="process_auditor").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pa",
        )
        self.assertEqual(state.state, "COMPLETED")
        self.assertTrue(state.sealed)
        self.assertEqual(state.output_kind, "ProcessAuditRecord")

    def test_p6_proof_judge_dispatch(self):
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        state = p6.dispatch_auditor(
            role_type_id="proof_judge",
            worker_id="w-pj-001",
            session_id="session-pj",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="proof_judge").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pj",
        )
        self.assertEqual(state.state, "COMPLETED")
        self.assertEqual(state.output_kind, "ProofJudgmentRecord")

    def test_p6_leakage_auditor_dispatch(self):
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        state = p6.dispatch_auditor(
            role_type_id="leakage_auditor",
            worker_id="w-la-001",
            session_id="session-la",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="leakage_auditor").carrier_profile_ref_and_hash["sha256"],
            view_id="view-la",
        )
        self.assertEqual(state.state, "COMPLETED")
        self.assertEqual(state.output_kind, "LeakageAuditRecord")

    def test_p6_blinding_enforced(self):
        """每个审计获得独立 view（blinding）。"""
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        p6.dispatch_auditor(
            role_type_id="process_auditor",
            worker_id="w-pa",
            session_id="s-pa",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="process_auditor").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pa",
        )
        p6.dispatch_auditor(
            role_type_id="proof_judge",
            worker_id="w-pj",
            session_id="s-pj",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="proof_judge").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pj",
        )
        p6.dispatch_auditor(
            role_type_id="leakage_auditor",
            worker_id="w-la",
            session_id="s-la",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="leakage_auditor").carrier_profile_ref_and_hash["sha256"],
            view_id="view-la",
        )
        # 三个 view 各不相同
        self.assertEqual(len(p6.view_assignments), 3)
        self.assertIn("view-pa", p6.view_assignments)
        self.assertIn("view-pj", p6.view_assignments)
        self.assertIn("view-la", p6.view_assignments)

    def test_p6_assemble_run_audit(self):
        """三个审计 seal 后组装 RunAudit。"""
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        for role, wid, sid, vid in [
            ("process_auditor", "w-pa", "s-pa", "v-pa"),
            ("proof_judge", "w-pj", "s-pj", "v-pj"),
            ("leakage_auditor", "w-la", "s-la", "v-la"),
        ]:
            p6.dispatch_auditor(
                role_type_id=role,
                worker_id=wid,
                session_id=sid,
                model_uid="glm-5-2",
                carrier_id="devin",
                carrier_profile_hash=_make_cell(role_type_id=role).carrier_profile_ref_and_hash["sha256"],
                view_id=vid,
            )
        audit_hash, errors = p6.assemble_run_audit()
        self.assertEqual(errors, [])
        self.assertNotEqual(audit_hash, "")
        self.assertTrue(p6.run_audit_assembled)

    def test_p6_judge_reads_unauthorized_view_blocks(self):
        """Judge 读取越权 view → blocker。"""
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        p6.dispatch_auditor(
            role_type_id="proof_judge",
            worker_id="w-pj",
            session_id="s-pj",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="proof_judge").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pj",
        )
        # judge 试图读取 process_auditor 的 view
        errors = p6.check_judge_view_access("w-pj", "view-pa")
        self.assertIn(EC.CW_JUDGE_READ_UNAUTHORIZED_VIEW, errors)

    def test_p6_judge_reads_own_view_ok(self):
        """Judge 读取自己的 view → 无错误。"""
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        p6.dispatch_auditor(
            role_type_id="proof_judge",
            worker_id="w-pj",
            session_id="s-pj",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="proof_judge").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pj",
        )
        errors = p6.check_judge_view_access("w-pj", "view-pj")
        self.assertEqual(errors, [])

    def test_p6_same_session_blocks(self):
        """同 session 的两个审计 → blocker。"""
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        p6.dispatch_auditor(
            role_type_id="process_auditor",
            worker_id="w-pa",
            session_id="same-session",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="process_auditor").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pa",
        )
        p6.dispatch_auditor(
            role_type_id="proof_judge",
            worker_id="w-pj",
            session_id="same-session",  # 同 session
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="proof_judge").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pj",
        )
        result = p6.verify_independence()
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_WORKER_NOT_INDEPENDENT, result.error_codes)

    def test_p6_same_view_blocks(self):
        """同 view 的两个审计 → blinding 违规。"""
        matrix = self._make_p6_matrix()
        p6 = _make_p6(matrix)
        p6.dispatch_auditor(
            role_type_id="process_auditor",
            worker_id="w-pa",
            session_id="s-pa",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="process_auditor").carrier_profile_ref_and_hash["sha256"],
            view_id="same-view",
        )
        p6.dispatch_auditor(
            role_type_id="proof_judge",
            worker_id="w-pj",
            session_id="s-pj",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="proof_judge").carrier_profile_ref_and_hash["sha256"],
            view_id="same-view",  # 同 view
        )
        result = p6.verify_independence()
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_BLINDING_VIOLATED, result.error_codes)

    def test_p6_db_lease_events(self):
        """P6 worker 的 DB lease 事件被记录。"""
        matrix = self._make_p6_matrix()
        db = DBLeaseReconcileIntegration()
        p6 = _make_p6(matrix, db_integration=db)
        p6.dispatch_auditor(
            role_type_id="process_auditor",
            worker_id="w-pa",
            session_id="s-pa",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=_make_cell(role_type_id="process_auditor").carrier_profile_ref_and_hash["sha256"],
            view_id="view-pa",
        )
        event_types = [e.event_type for e in db.events]
        self.assertIn("LEASE_ACQUIRED", event_types)
        self.assertIn("WORK_ITEM_STATE_CHANGED", event_types)


# ─── IndependenceEnforcer tests ─────────────────────────────────────────


class TestIndependenceEnforcer(unittest.TestCase):
    """IndependenceEnforcer 独立性强制测试。"""

    def test_same_session_author_reviewer_blocks(self):
        """同 session 作者+审稿 → CW_SAME_SESSION_AUTHOR_REVIEWER。"""
        enforcer = IndependenceEnforcer()
        author = WorkerSession("w-author", "trace_analyst", "glm-5-2", "same-session", "devin", "view-1")
        reviewer = WorkerSession("w-reviewer", "adjudicator", "glm-5-2", "same-session", "devin", "view-2")
        violations = enforcer.check_author_reviewer_independence(author, reviewer)
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].error_code, EC.CW_SAME_SESSION_AUTHOR_REVIEWER)

    def test_different_session_author_reviewer_ok(self):
        """不同 session 作者+审稿 → 无违规。"""
        enforcer = IndependenceEnforcer()
        author = WorkerSession("w-author", "trace_analyst", "glm-5-2", "session-a", "devin", "view-1")
        reviewer = WorkerSession("w-reviewer", "adjudicator", "glm-5-2", "session-b", "devin", "view-2")
        violations = enforcer.check_author_reviewer_independence(author, reviewer)
        self.assertEqual(len(violations), 0)

    def test_judge_reads_unauthorized_view_blocks(self):
        """Judge 读越权 view → CW_JUDGE_READ_UNAUTHORIZED_VIEW。"""
        enforcer = IndependenceEnforcer()
        judge = WorkerSession("w-judge", "proof_judge", "glm-5-2", "s-judge", "devin", "view-judge")
        enforcer.register_session(judge)
        violations = enforcer.check_judge_view_isolation(judge, "view-other")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].error_code, EC.CW_JUDGE_READ_UNAUTHORIZED_VIEW)

    def test_judge_reads_own_view_ok(self):
        """Judge 读自己的 view → 无违规。"""
        enforcer = IndependenceEnforcer()
        judge = WorkerSession("w-judge", "proof_judge", "glm-5-2", "s-judge", "devin", "view-judge")
        enforcer.register_session(judge)
        violations = enforcer.check_judge_view_isolation(judge, "view-judge")
        self.assertEqual(len(violations), 0)

    def test_fake_independence_same_model_blocks(self):
        """同模型 fresh session 声称不同模型独立性 → CW_FAKE_INDEPENDENCE_SAME_MODEL。"""
        enforcer = IndependenceEnforcer()
        worker_a = WorkerSession("w-a", "trace_analyst", "glm-5-2", "s-a", "devin", "v-a")
        worker_b = WorkerSession("w-b", "solution_analyst", "glm-5-2", "s-b", "devin", "v-b")
        violations = enforcer.check_fake_independence(worker_a, worker_b, claimed_kind="DIFFERENT_MODEL")
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].error_code, EC.CW_FAKE_INDEPENDENCE_SAME_MODEL)

    def test_different_model_independence_ok(self):
        """真正不同模型 → 无伪独立性违规。"""
        enforcer = IndependenceEnforcer()
        worker_a = WorkerSession("w-a", "trace_analyst", "glm-5-2", "s-a", "devin", "v-a")
        worker_b = WorkerSession("w-b", "solution_analyst", "gpt-5.6", "s-b", "codex", "v-b")
        violations = enforcer.check_fake_independence(worker_a, worker_b, claimed_kind="DIFFERENT_MODEL")
        self.assertEqual(len(violations), 0)

    def test_p6_independence_all_different_ok(self):
        """三个审计各自独立 session + view → 无违规。"""
        enforcer = IndependenceEnforcer()
        auditors = [
            WorkerSession("w-pa", "process_auditor", "glm-5-2", "s-pa", "devin", "v-pa"),
            WorkerSession("w-pj", "proof_judge", "glm-5-2", "s-pj", "devin", "v-pj"),
            WorkerSession("w-la", "leakage_auditor", "glm-5-2", "s-la", "devin", "v-la"),
        ]
        violations = enforcer.check_p6_independence(auditors)
        self.assertEqual(len(violations), 0)

    def test_p6_independence_same_session_blocks(self):
        """两个审计同 session → CW_WORKER_NOT_INDEPENDENT。"""
        enforcer = IndependenceEnforcer()
        auditors = [
            WorkerSession("w-pa", "process_auditor", "glm-5-2", "same-s", "devin", "v-pa"),
            WorkerSession("w-pj", "proof_judge", "glm-5-2", "same-s", "devin", "v-pj"),
        ]
        violations = enforcer.check_p6_independence(auditors)
        self.assertTrue(any(v.error_code == EC.CW_WORKER_NOT_INDEPENDENT for v in violations))

    def test_p6_independence_same_view_blocks(self):
        """两个审计同 view → CW_BLINDING_VIOLATED。"""
        enforcer = IndependenceEnforcer()
        auditors = [
            WorkerSession("w-pa", "process_auditor", "glm-5-2", "s-pa", "devin", "same-v"),
            WorkerSession("w-pj", "proof_judge", "glm-5-2", "s-pj", "devin", "same-v"),
        ]
        violations = enforcer.check_p6_independence(auditors)
        self.assertTrue(any(v.error_code == EC.CW_BLINDING_VIOLATED for v in violations))

    def test_author_reviewer_pair_via_check_all(self):
        """通过 check_all 检查作者-审稿者配对。"""
        enforcer = IndependenceEnforcer()
        author = WorkerSession("w-author", "trace_analyst", "glm-5-2", "same-s", "devin", "v-a")
        reviewer = WorkerSession("w-reviewer", "adjudicator", "glm-5-2", "same-s", "devin", "v-r")
        enforcer.register_session(author)
        enforcer.register_session(reviewer)
        enforcer.record_author_reviewer("w-author", "w-reviewer")
        violations = enforcer.check_all()
        self.assertTrue(any(v.error_code == EC.CW_SAME_SESSION_AUTHOR_REVIEWER for v in violations))

    def test_verify_independence_pass(self):
        enforcer = IndependenceEnforcer()
        author = WorkerSession("w-a", "trace_analyst", "glm-5-2", "s-a", "devin", "v-a")
        reviewer = WorkerSession("w-r", "adjudicator", "glm-5-2", "s-r", "devin", "v-r")
        enforcer.register_session(author)
        enforcer.register_session(reviewer)
        enforcer.record_author_reviewer("w-a", "w-r")
        result = enforcer.verify_independence()
        self.assertTrue(result.passed)


# ─── DBLeaseReconcileIntegration tests ──────────────────────────────────


class TestDBLeaseReconcileIntegration(unittest.TestCase):
    """DB lease/reconcile 集成测试。"""

    def test_acquire_and_release_lease(self):
        db = DBLeaseReconcileIntegration()
        fence, lease_id, errors = db.acquire_lease(
            worker_id="w-001",
            aggregate_id="agg-001",
        )
        self.assertEqual(errors, [])
        self.assertGreater(fence, 0)
        self.assertNotEqual(lease_id, "")
        release_errors = db.release_lease(
            lease_id=lease_id,
            fence_token=fence,
            aggregate_id="agg-001",
            worker_id="w-001",
        )
        self.assertEqual(release_errors, [])

    def test_lease_events_logged(self):
        db = DBLeaseReconcileIntegration()
        fence, lease_id, _ = db.acquire_lease(worker_id="w-001", aggregate_id="agg-001")
        db.release_lease(lease_id=lease_id, fence_token=fence, aggregate_id="agg-001", worker_id="w-001")
        event_types = [e.event_type for e in db.events]
        self.assertIn("LEASE_ACQUIRED", event_types)
        self.assertIn("LEASE_RELEASED", event_types)

    def test_state_change_logged(self):
        db = DBLeaseReconcileIntegration()
        fence, _, _ = db.acquire_lease(worker_id="w-001", aggregate_id="agg-001")
        db.log_state_change(
            aggregate_id="agg-001",
            worker_id="w-001",
            fence_token=fence,
            old_state="PENDING",
            new_state="LEASED",
        )
        event_types = [e.event_type for e in db.events]
        self.assertIn("WORK_ITEM_STATE_CHANGED", event_types)

    def test_reconcile_fence_match(self):
        db = DBLeaseReconcileIntegration()
        fence, _, _ = db.acquire_lease(worker_id="w-001", aggregate_id="agg-001")
        state = WorkerState(
            worker_id="w-001",
            role_type_id="trace_analyst",
            session_id="s-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            view_id="v-001",
            fence_token=fence,
        )
        errors = db.reconcile_worker(
            worker_state=state,
            expected_fence_token=fence,
            aggregate_id="agg-001",
        )
        self.assertEqual(errors, [])

    def test_reconcile_fence_mismatch(self):
        db = DBLeaseReconcileIntegration()
        fence, _, _ = db.acquire_lease(worker_id="w-001", aggregate_id="agg-001")
        state = WorkerState(
            worker_id="w-001",
            role_type_id="trace_analyst",
            session_id="s-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            view_id="v-001",
            fence_token=fence,
        )
        errors = db.reconcile_worker(
            worker_state=state,
            expected_fence_token=999,  # 不匹配
            aggregate_id="agg-001",
        )
        self.assertIn(EC.CW_RECONCILE_FENCE_MISMATCH, errors)

    def test_reconcile_stale_fence(self):
        """新 worker 取得更高 fence 后，旧 worker reconcile → fence mismatch。"""
        db = DBLeaseReconcileIntegration()
        fence1, _, _ = db.acquire_lease(worker_id="w-001", aggregate_id="agg-001")
        # 新 worker 取得更高 fence
        fence2, _, _ = db.acquire_lease(worker_id="w-002", aggregate_id="agg-001")
        self.assertGreater(fence2, fence1)
        # 旧 worker reconcile
        state = WorkerState(
            worker_id="w-001",
            role_type_id="trace_analyst",
            session_id="s-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            view_id="v-001",
            fence_token=fence1,
        )
        errors = db.reconcile_worker(
            worker_state=state,
            expected_fence_token=fence1,
            aggregate_id="agg-001",
        )
        self.assertIn(EC.CW_RECONCILE_FENCE_MISMATCH, errors)


# ─── WorkerCapabilityReport tests ───────────────────────────────────────


class TestWorkerCapabilityReport(unittest.TestCase):
    """WorkerCapabilityReport 测试。"""

    def test_build_report_all_conclusions(self):
        """所有 cell 有结论 → PASS 报告。"""
        cells = [
            _make_cell(role_type_id="trace_analyst", verdict="PASS", cell_id="c1"),
            _make_cell(role_type_id="solution_analyst", verdict="PASS", cell_id="c2"),
            _make_cell(role_type_id="adjudicator", verdict="NOT_TESTED", cell_id="c3", valid_until=None),
        ]
        matrix = _make_matrix(cells=cells)
        router = _make_router(matrix)
        report = build_worker_capability_report(
            matrix=matrix,
            router=router,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["blockers"], [])
        self.assertEqual(report["schema_version"], WORKER_REPORT_SCHEMA_VERSION)
        self.assertEqual(report["scope"], WORKER_REPORT_SCOPE)

    def test_verify_report_pass(self):
        cells = [_make_cell(role_type_id="trace_analyst", verdict="PASS")]
        matrix = _make_matrix(cells=cells)
        router = _make_router(matrix)
        report = build_worker_capability_report(
            matrix=matrix,
            router=router,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        errors = verify_worker_capability_report(report)
        self.assertEqual(errors, ())

    def test_report_side_effects_zero(self):
        cells = [_make_cell(role_type_id="trace_analyst", verdict="PASS")]
        matrix = _make_matrix(cells=cells)
        router = _make_router(matrix)
        report = build_worker_capability_report(
            matrix=matrix,
            router=router,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        for key in CW_SIDE_EFFECT_KEYS:
            self.assertEqual(report["side_effects"][key], 0)

    def test_report_checks_match_canonical(self):
        cells = [_make_cell(role_type_id="trace_analyst", verdict="PASS")]
        matrix = _make_matrix(cells=cells)
        router = _make_router(matrix)
        report = build_worker_capability_report(
            matrix=matrix,
            router=router,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        check_ids = [c["check_id"] for c in report["checks"]]
        self.assertEqual(check_ids, list(CW_CHECK_IDS))

    def test_report_claims_match(self):
        cells = [_make_cell(role_type_id="trace_analyst", verdict="PASS")]
        matrix = _make_matrix(cells=cells)
        router = _make_router(matrix)
        report = build_worker_capability_report(
            matrix=matrix,
            router=router,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        self.assertEqual(set(report["claims"]), set(CW_CLAIMS))

    def test_report_nonclaims_match(self):
        cells = [_make_cell(role_type_id="trace_analyst", verdict="PASS")]
        matrix = _make_matrix(cells=cells)
        router = _make_router(matrix)
        report = build_worker_capability_report(
            matrix=matrix,
            router=router,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        self.assertEqual(set(report["explicit_nonclaims"]), set(CW_NONCLAIMS))


# ─── Deterministic hash tests ───────────────────────────────────────────


class TestDeterministicHashes(unittest.TestCase):
    """确定性 hash 测试。"""

    def test_cell_key_deterministic(self):
        """相同字段 → 相同 cell_key。"""
        fields = {
            "role_type_id": "trace_analyst",
            "carrier_id": "devin",
            "model_id": "glm-5-2",
            "carrier_profile_ref_and_hash": _ref("p", _ZERO_HASH),
            "input_view_ref_and_hash": _ref("v"),
            "input_view_policy_ref_and_hash": _ref("vp"),
            "input_acl_policy_ref_and_hash": _ref("acl"),
            "vault_access_capability_ref_and_hash": _ref("vac"),
            "tool_network_sandbox_policy_ref_and_hash": _ref("tns"),
            "output_sensitivity_and_sink_policy_ref_and_hash": _ref("oss"),
            "prompt_release_ref_and_hash": _ref("pr"),
            "output_schema_ref_and_hash": _ref("os"),
            "adapter_ref_and_hash": _ref("ad"),
            "parser_ref_and_hash": _ref("pa"),
            "capability_requirement_ref_and_hash": _ref("cr"),
            "qualification_level": "PRODUCTION",
        }
        key1 = compute_cell_key(fields)
        key2 = compute_cell_key(fields)
        self.assertEqual(key1, key2)
        self.assertEqual(len(key1), 64)

    def test_matrix_hash_deterministic(self):
        cell = _make_cell()
        m1 = _make_matrix(cells=[cell], matrix_id="m-1")
        m2 = _make_matrix(cells=[cell], matrix_id="m-1")
        self.assertEqual(m1.matrix_hash, m2.matrix_hash)

    def test_output_hash_deterministic(self):
        """P3N worker 输出 hash 确定性。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        p3n1 = _make_p3n(matrix)
        p3n2 = _make_p3n(matrix)
        s1 = p3n1.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-1",
            session_id="s-1",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="v-1",
        )
        s2 = p3n2.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-1",
            session_id="s-1",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="v-1",
        )
        self.assertEqual(s1.output_hash, s2.output_hash)

    def test_output_hash_differs_on_view(self):
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        p3n = _make_p3n(matrix)
        s1 = p3n.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-1",
            session_id="s-1",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="v-1",
        )
        s2 = p3n.dispatch_worker(
            role_type_id="trace_analyst",
            worker_id="w-2",
            session_id="s-2",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
            view_id="v-2",
        )
        self.assertNotEqual(s1.output_hash, s2.output_hash)


# ─── CW1 Boundary tests ─────────────────────────────────────────────────


class TestCW1Boundary(unittest.TestCase):
    """CW1 边界测试（allowed/forbidden output kinds）。"""

    def test_p3n_output_kinds_in_allowed(self):
        """P3N 输出种类在 CW_ALLOWED_OUTPUT_KINDS 中。"""
        for kind in ["MechanismContract", "RelationMapping", "NaturalCaseReviewBundle"]:
            self.assertIn(kind, CW_ALLOWED_OUTPUT_KINDS)

    def test_p6_output_kinds_in_allowed(self):
        """P6 输出种类在 CW_ALLOWED_OUTPUT_KINDS 中。"""
        for kind in ["ProcessAuditRecord", "ProofJudgmentRecord", "LeakageAuditRecord"]:
            self.assertIn(kind, CW_ALLOWED_OUTPUT_KINDS)

    def test_run_audit_in_allowed(self):
        self.assertIn("RunAudit", CW_ALLOWED_OUTPUT_KINDS)

    def test_forbidden_kinds_not_in_allowed(self):
        """禁止的种类不在允许集合中。"""
        for kind in CW_FORBIDDEN_OUTPUT_KINDS:
            self.assertNotIn(kind, CW_ALLOWED_OUTPUT_KINDS)

    def test_solver_output_forbidden(self):
        self.assertIn("TargetSolverRunArtifact", CW_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SolverDispatchReceipt", CW_FORBIDDEN_OUTPUT_KINDS)

    def test_schema_report_forbidden(self):
        self.assertIn("DatabaseSchemaStateReport", CW_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SchemaBootstrapReceipt", CW_FORBIDDEN_OUTPUT_KINDS)

    def test_db_report_forbidden(self):
        self.assertIn("DatabaseRuntimeCapabilityReport", CW_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("ArtifactCommitReconcileCapabilityReport", CW_FORBIDDEN_OUTPUT_KINDS)

    def test_allowed_and_forbidden_disjoint(self):
        """允许和禁止集合不相交。"""
        self.assertEqual(CW_ALLOWED_OUTPUT_KINDS & CW_FORBIDDEN_OUTPUT_KINDS, frozenset())


# ─── Blocker tests (negative) ───────────────────────────────────────────


class TestCW1Blockers(unittest.TestCase):
    """所有 blocker test — 失败则工作包 FAIL。"""

    def test_blocker_unqualified_cell_routed(self):
        """Blocker: 未合格 cell 路由到生产 → BLOCK。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="NOT_TESTED", valid_until=None)
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        decision = router.route(
            role_type_id="trace_analyst",
            carrier_id="devin",
            model_id="glm-5-2",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
        )
        self.assertFalse(decision.is_dispatch)
        self.assertIn(EC.CW_UNQUALIFIED_CELL_ROUTED, decision.error_codes)

    def test_blocker_same_session_author_reviewer(self):
        """Blocker: 同 session 作者+审稿 → BLOCK。"""
        enforcer = IndependenceEnforcer()
        author = WorkerSession("w-a", "trace_analyst", "glm-5-2", "same", "devin", "v-a")
        reviewer = WorkerSession("w-r", "adjudicator", "glm-5-2", "same", "devin", "v-r")
        violations = enforcer.check_author_reviewer_independence(author, reviewer)
        self.assertTrue(any(v.error_code == EC.CW_SAME_SESSION_AUTHOR_REVIEWER for v in violations))

    def test_blocker_judge_reads_unauthorized_view(self):
        """Blocker: Judge 读越权 view → BLOCK。"""
        enforcer = IndependenceEnforcer()
        judge = WorkerSession("w-j", "proof_judge", "glm-5-2", "s-j", "devin", "v-j")
        enforcer.register_session(judge)
        violations = enforcer.check_judge_view_isolation(judge, "v-other")
        self.assertTrue(any(v.error_code == EC.CW_JUDGE_READ_UNAUTHORIZED_VIEW for v in violations))

    def test_blocker_fake_independence_same_model(self):
        """Blocker: 同模型 fresh session 声称不同模型独立性 → BLOCK。"""
        enforcer = IndependenceEnforcer()
        a = WorkerSession("w-a", "trace_analyst", "glm-5-2", "s-a", "devin", "v-a")
        b = WorkerSession("w-b", "solution_analyst", "glm-5-2", "s-b", "devin", "v-b")
        violations = enforcer.check_fake_independence(a, b, claimed_kind="DIFFERENT_MODEL")
        self.assertTrue(any(v.error_code == EC.CW_FAKE_INDEPENDENCE_SAME_MODEL for v in violations))

    def test_blocker_no_fallback_carrier(self):
        """Blocker: 没有 PASS cell 时不 fallback 到另一个 carrier → BLOCK。"""
        cell = _make_cell(role_type_id="trace_analyst", carrier_id="devin", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        decision = router.route(
            role_type_id="trace_analyst",
            carrier_id="codex",  # 不同 carrier，不 fallback
            model_id="glm-5-2",
            carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
        )
        self.assertFalse(decision.is_dispatch)
        self.assertIn(EC.CW_NO_FALLBACK_CARRIER, decision.error_codes)

    def test_blocker_missing_cell_conclusion(self):
        """Blocker: cell 缺失结论（既非 PASS 也非 NOT_TESTED 也非 FAILED）→ BLOCK。"""
        cell = _make_cell(role_type_id="trace_analyst", verdict="PASS")
        matrix = _make_matrix(cells=[cell])
        router = _make_router(matrix)
        # 替换 cells 为没有结论的 cell
        from seven_system.cognitive.production.role_qualification_matrix import RoleQualificationCell
        bad_cell = RoleQualificationCell(
            **{**cell.to_dict(), "verdict": "UNKNOWN"}
        )
        router.matrix.cells = tuple([bad_cell])
        result = router.verify_all_production_cells_have_conclusions()
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_CELL_CONCLUSION_MISSING, result.error_codes)

    def test_blocker_wildcard_rejected(self):
        """Blocker: 通配符哨兵被拒绝。"""
        cell = _make_cell(role_type_id="ANY")
        result = verify_role_qualification_cell(cell)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_MATRIX_WILDCARD_REJECTED, result.error_codes)

    def test_blocker_hash_mismatch(self):
        """Blocker: hash 不匹配被检测。"""
        cell = _make_cell()
        cell_dict = cell.to_dict()
        cell_dict["cell_key"] = "f" * 64
        result = verify_role_qualification_cell(cell_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_CELL_KEY_MISMATCH, result.error_codes)

    def test_blocker_matrix_hash_mismatch(self):
        """Blocker: matrix hash 不匹配被检测。"""
        cell = _make_cell()
        matrix = _make_matrix(cells=[cell])
        matrix_dict = matrix.to_dict()
        matrix_dict["matrix_hash"] = "e" * 64
        result = verify_role_qualification_matrix(matrix_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_MATRIX_HASH_MISMATCH, result.error_codes)

    def test_blocker_lease_acquire_failed(self):
        """Blocker: lease 获取失败（重复 lease_id）。"""
        db = DBLeaseReconcileIntegration()
        # 第一次成功
        db.acquire_lease(worker_id="w-001", aggregate_id="agg-001")
        # 第二次用相同 lease_id → 失败
        fence, _, errors = db.acquire_lease(worker_id="w-001", aggregate_id="agg-001")
        self.assertTrue(len(errors) > 0)
        self.assertEqual(fence, 0)

    def test_blocker_fence_mismatch(self):
        """Blocker: reconcile fence 不匹配。"""
        db = DBLeaseReconcileIntegration()
        fence, _, _ = db.acquire_lease(worker_id="w-001", aggregate_id="agg-001")
        state = WorkerState(
            worker_id="w-001",
            role_type_id="trace_analyst",
            session_id="s-001",
            model_uid="glm-5-2",
            carrier_id="devin",
            view_id="v-001",
            fence_token=fence,
        )
        errors = db.reconcile_worker(
            worker_state=state,
            expected_fence_token=fence + 100,
            aggregate_id="agg-001",
        )
        self.assertIn(EC.CW_RECONCILE_FENCE_MISMATCH, errors)

    def test_blocker_completeness_remainder_nonzero(self):
        """Blocker: completeness remainder 非零时 verdict 不能 PASS。"""
        comp_dict = {
            "required_cell_keys": ["a"],
            "pass_cell_keys": ["a"],
            "not_tested_cell_keys": ["b"],
            "failed_cell_keys": [],
            "extra_cell_keys": ["b"],
            "missing_cell_keys": [],
            "remainder_cell_keys": ["b"],
            "remainder_count": 1,
            "verdict": "PASS",
            "algorithm_ref_and_hash": _ref("algo"),
        }
        result = verify_completeness(comp_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW_COMPLETENESS_VERDICT_INVALID, result.error_codes)


# ─── Golden path integration ────────────────────────────────────────────


class TestGoldenPathIntegration(unittest.TestCase):
    """Golden path 完整集成测试。"""

    def test_full_p3n_pipeline(self):
        """完整 P3N pipeline：matrix build → cell lookup → routing → dispatch。"""
        cells = [
            _make_cell(role_type_id="trace_analyst", verdict="PASS", cell_id="c-ta"),
            _make_cell(role_type_id="solution_analyst", verdict="PASS", cell_id="c-sa"),
            _make_cell(role_type_id="adjudicator", verdict="PASS", cell_id="c-adj"),
        ]
        matrix = _make_matrix(cells=cells)
        # 验证 matrix
        matrix_result = verify_role_qualification_matrix(matrix)
        self.assertTrue(matrix_result.passed, f"matrix errors: {matrix_result.details}")

        router = _make_router(matrix)
        db = DBLeaseReconcileIntegration()
        p3n = P3NWorkers(router=router, db_integration=db)

        # dispatch 三个 worker
        for role, wid, sid, vid in [
            ("trace_analyst", "w-ta", "s-ta", "v-ta"),
            ("solution_analyst", "w-sa", "s-sa", "v-sa"),
            ("adjudicator", "w-adj", "s-adj", "v-adj"),
        ]:
            cell = next(c for c in cells if c.role_type_id == role)
            state = p3n.dispatch_worker(
                role_type_id=role,
                worker_id=wid,
                session_id=sid,
                model_uid="glm-5-2",
                carrier_id="devin",
                carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
                view_id=vid,
            )
            self.assertEqual(state.state, "COMPLETED", f"{role} failed: {state.details}")
            self.assertTrue(state.sealed)

        # 验证独立性
        indep_result = p3n.verify_independence()
        self.assertTrue(indep_result.passed, f"independence: {indep_result.details}")

    def test_full_p6_pipeline_with_run_audit(self):
        """完整 P6 pipeline：三个审计 → blinding → seal → RunAudit。"""
        cells = [
            _make_cell(role_type_id="process_auditor", verdict="PASS", cell_id="c-pa"),
            _make_cell(role_type_id="proof_judge", verdict="PASS", cell_id="c-pj"),
            _make_cell(role_type_id="leakage_auditor", verdict="PASS", cell_id="c-la"),
        ]
        matrix = _make_matrix(cells=cells)
        router = _make_router(matrix)
        db = DBLeaseReconcileIntegration()
        p6 = P6Workers(router=router, db_integration=db)

        for role, wid, sid, vid in [
            ("process_auditor", "w-pa", "s-pa", "v-pa"),
            ("proof_judge", "w-pj", "s-pj", "v-pj"),
            ("leakage_auditor", "w-la", "s-la", "v-la"),
        ]:
            cell = next(c for c in cells if c.role_type_id == role)
            state = p6.dispatch_auditor(
                role_type_id=role,
                worker_id=wid,
                session_id=sid,
                model_uid="glm-5-2",
                carrier_id="devin",
                carrier_profile_hash=cell.carrier_profile_ref_and_hash["sha256"],
                view_id=vid,
            )
            self.assertEqual(state.state, "COMPLETED", f"{role} failed: {state.details}")
            self.assertTrue(state.sealed)

        # 组装 RunAudit
        audit_hash, errors = p6.assemble_run_audit()
        self.assertEqual(errors, [])
        self.assertNotEqual(audit_hash, "")

        # 验证独立性
        indep_result = p6.verify_independence()
        self.assertTrue(indep_result.passed)

    def test_full_capability_report(self):
        """完整能力报告构建与验证。"""
        cells = [
            _make_cell(role_type_id="trace_analyst", verdict="PASS", cell_id="c1"),
            _make_cell(role_type_id="solution_analyst", verdict="NOT_TESTED", cell_id="c2", valid_until=None),
            _make_cell(role_type_id="adjudicator", verdict="PASS", cell_id="c3"),
        ]
        matrix = _make_matrix(cells=cells)
        router = _make_router(matrix)
        report = build_worker_capability_report(
            matrix=matrix,
            router=router,
            verifier_identity="verifier-001",
            generated_at=_TS,
        )
        errors = verify_worker_capability_report(report)
        self.assertEqual(errors, ())
        self.assertEqual(report["verdict"], "PASS")


if __name__ == "__main__":
    unittest.main()
