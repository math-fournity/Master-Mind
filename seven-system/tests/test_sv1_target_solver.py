"""WP-SV1 TargetSolver/Harness 测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- TargetSolverPort 协议（prepare/launch/observe/collect/cancel/reconcile）
- SolverJob / PreparedSolverJob / LaunchTicket / LaunchReceipt
- HarnessProfile / NoToolPolicy
- FakeHarnessAdapter 确定性 lifecycle
- SafeLaunchReport / AnswerIsolationReport / SolverCapabilityReport
- Blocker tests：
  - direct-devin bypass detected → FAIL
  - tool event in trajectory → FAIL
  - missing trajectory → FAIL
  - repo workspace not isolated → FAIL
  - answer not isolated from process → FAIL
  - NoTool policy violation → FAIL
  - cancel after terminal → FAIL
  - fence mismatch → FAIL
  - budget exceeded → FAIL
  - hash drift → FAIL
  - profile mismatch → FAIL
- Deterministic hash tests
- SV1 boundary tests (allowed/forbidden output kinds)
- All constants verified

所有 blocker test 失败 → 工作包 FAIL。
SIDE_EFFECT_FREE：不接触真实 CLI / DB / D-volume。
"""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import (
    SV_ALLOWED_OUTPUT_KINDS,
    SV_ANSWER_KINDS,
    SV_CAPABILITY_KINDS,
    SV_FORBIDDEN_OUTPUT_KINDS,
    SV_LAUNCH_STATES,
    SV_TERMINAL_REASONS,
    SV_TOOL_POLICY_KINDS,
    SV_TRAJECTORY_KINDS,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.contracts.completion_contract import VerificationResult
from seven_system.adapters.solver.port import (
    TargetSolverPort,
    SolverJob,
    PreparedSolverJob,
    LaunchTicket,
    LaunchReceipt,
    SolverJobError,
    build_solver_job,
    prepare_solver_job,
    verify_solver_job,
    verify_prepared_solver_job,
    verify_launch_ticket,
    verify_launch_receipt,
    build_launch_receipt,
)
from seven_system.adapters.solver.harness_profile import (
    HarnessProfile,
    build_harness_profile,
    verify_harness_profile,
    HARNESS_KINDS,
)
from seven_system.adapters.solver.notool_policy import (
    NoToolPolicy,
    build_notool_policy,
    verify_notool_policy,
    check_trajectory_for_tool_events,
)
from seven_system.adapters.solver.harness_adapter import (
    HarnessAdapter,
    FakeHarnessAdapter,
    HarnessAdapterError,
)
from seven_system.adapters.solver.safe_launch_report import (
    SafeLaunchReport,
    build_safe_launch_report,
    verify_safe_launch_report,
    SAFE_LAUNCH_CHECK_IDS,
)
from seven_system.adapters.solver.answer_isolation_report import (
    AnswerIsolationReport,
    build_answer_isolation_report,
    verify_answer_isolation_report,
    ANSWER_ISOLATION_CHECK_IDS,
)
from seven_system.adapters.solver.solver_capability_report import (
    SolverCapabilityReport,
    build_solver_capability_report,
    verify_solver_capability_report,
    SolverCapabilityReportError,
    SOLVER_REPORT_SCHEMA_VERSION,
    SOLVER_CHECK_IDS,
    SOLVER_CLAIMS,
    SOLVER_NONCLAIMS,
    SOLVER_SIDE_EFFECT_KEYS,
)


# ─── helpers ────────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64
_FAKE_HASH_A = "a" * 64
_FAKE_HASH_B = "b" * 64


def _sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _make_ref(ref_id: str, sha256: str = _ZERO_HASH) -> dict[str, str]:
    return {"ref_id": ref_id, "sha256": sha256}


def _make_budget() -> dict:
    return {
        "wallclock_seconds": 3600,
        "max_tokens": 100000,
        "max_cost_microunits": 1000000,
    }


def _make_workspace_spec() -> dict:
    return {
        "isolation_kind": "ISOLATED",
        "root_path": "/tmp/solver-workspace-isolated",
    }


def _make_default_profile() -> HarnessProfile:
    content = hashlib.sha256(b"fake-harness-content-v1").hexdigest()
    return build_harness_profile(
        version="fake-harness-v1",
        content_hash=content,
        harness_kind="FAKE_HARNESS",
        tool_policy_kind="NO_TOOL",
    )


def _make_solver_job(
    *,
    attempt_id: str = "attempt-001",
    fence_token: str = "fence-001",
    profile: HarnessProfile | None = None,
    tool_policy_kind: str = "NO_TOOL",
    workspace_spec: dict | None = None,
) -> SolverJob:
    if profile is None:
        profile = _make_default_profile()
    return build_solver_job(
        problem_ref_id="problem-001",
        problem_sha256=_FAKE_HASH_A,
        view_ref_id="view-001",
        view_sha256=_FAKE_HASH_B,
        budget_contract=_make_budget(),
        tool_policy_kind=tool_policy_kind,
        idempotency_key="idem-001",
        fence_token=fence_token,
        attempt_id=attempt_id,
        repo_workspace_spec=workspace_spec or _make_workspace_spec(),
        harness_profile_ref_id="harness-profile-001",
        harness_profile_sha256=profile.profile_hash,
    )


# ─── Constants verification ─────────────────────────────────────────────


class TestSV1Constants(unittest.TestCase):
    """验证 SV1 常量集合。"""

    def test_sv_terminal_reasons(self):
        self.assertIn("COMPLETED", SV_TERMINAL_REASONS)
        self.assertIn("CANCELLED", SV_TERMINAL_REASONS)
        self.assertIn("TIMED_OUT", SV_TERMINAL_REASONS)
        self.assertIn("BUDGET_EXCEEDED", SV_TERMINAL_REASONS)
        self.assertIn("TERMINATED", SV_TERMINAL_REASONS)
        self.assertIn("FAILED_PERMANENT", SV_TERMINAL_REASONS)
        self.assertIn("QUARANTINED", SV_TERMINAL_REASONS)

    def test_sv_tool_policy_kinds(self):
        self.assertIn("NO_TOOL", SV_TOOL_POLICY_KINDS)
        self.assertIn("READ_ONLY_TOOLS", SV_TOOL_POLICY_KINDS)
        self.assertIn("SANDBOXED_TOOLS", SV_TOOL_POLICY_KINDS)

    def test_sv_capability_kinds(self):
        self.assertIn("TARGET_SOLVER_HARNESS", SV_CAPABILITY_KINDS)
        self.assertIn("TARGET_SOLVER_NO_TOOL", SV_CAPABILITY_KINDS)
        self.assertIn("TARGET_SOLVER_SAFE_LAUNCH", SV_CAPABILITY_KINDS)
        self.assertIn("TARGET_SOLVER_ANSWER_ISOLATION", SV_CAPABILITY_KINDS)
        self.assertEqual(len(SV_CAPABILITY_KINDS), 4)

    def test_sv_launch_states(self):
        self.assertIn("PREPARED", SV_LAUNCH_STATES)
        self.assertIn("LAUNCHED", SV_LAUNCH_STATES)
        self.assertIn("OBSERVED", SV_LAUNCH_STATES)
        self.assertIn("COLLECTED", SV_LAUNCH_STATES)
        self.assertIn("CANCELLED", SV_LAUNCH_STATES)
        self.assertIn("FAILED", SV_LAUNCH_STATES)
        self.assertIn("QUARANTINED", SV_LAUNCH_STATES)

    def test_sv_trajectory_kinds(self):
        self.assertIn("FULL_TRAJECTORY", SV_TRAJECTORY_KINDS)
        self.assertIn("PARTIAL_TRAJECTORY", SV_TRAJECTORY_KINDS)
        self.assertIn("EMPTY_TRAJECTORY", SV_TRAJECTORY_KINDS)

    def test_sv_answer_kinds(self):
        self.assertIn("FINAL_ANSWER", SV_ANSWER_KINDS)
        self.assertIn("PARTIAL_ANSWER", SV_ANSWER_KINDS)
        self.assertIn("NO_ANSWER", SV_ANSWER_KINDS)

    def test_sv_allowed_output_kinds(self):
        self.assertIn("SolverHarnessCapabilityReport", SV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("SolverNoToolCapabilityReport", SV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("SolverSafeLaunchReport", SV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("SolverAnswerIsolationReport", SV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("SolverLaunchReceipt", SV_ALLOWED_OUTPUT_KINDS)

    def test_sv_forbidden_output_kinds(self):
        self.assertIn("DatabaseSchemaStateReport", SV_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SchemaBootstrapReceipt", SV_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("DatabaseRuntimeCapabilityReport", SV_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("ArtifactCommitReconcileCapabilityReport", SV_FORBIDDEN_OUTPUT_KINDS)

    def test_sv_error_codes_exist(self):
        """验证所有 SV1 错误码存在于 VerificationErrorCode 中。"""
        sv_codes = [
            EC.SV_DIRECT_DEVIN_BYPASS,
            EC.SV_TOOL_EVENT_DETECTED,
            EC.SV_TRAJECTORY_MISSING,
            EC.SV_REPO_WORKSPACE_NOT_ISOLATED,
            EC.SV_ANSWER_NOT_ISOLATED,
            EC.SV_NOTOOL_VIOLATION,
            EC.SV_LAUNCH_RECEIPT_INCOMPLETE,
            EC.SV_HARNESS_PROFILE_HASH_MISMATCH,
            EC.SV_FENCE_TOKEN_INVALID,
            EC.SV_PREPARED_JOB_HASH_DRIFT,
            EC.SV_CANCEL_AFTER_TERMINAL,
            EC.SV_RECONCILE_FENCE_MISMATCH,
            EC.SV_BUDGET_EXCEEDED,
            EC.SV_TERMINAL_REASON_INVALID,
            EC.SV_LAUNCH_STATE_INVALID,
            EC.SV_IDEMPOTENCY_KEY_CONFLICT,
            EC.SV_PROBLEM_REF_HASH_MISMATCH,
            EC.SV_VIEW_REF_HASH_MISMATCH,
            EC.SV_BUDGET_CONTRACT_INVALID,
            EC.SV_TOOL_POLICY_KIND_INVALID,
            EC.SV_TRAJECTORY_KIND_INVALID,
            EC.SV_ANSWER_KIND_INVALID,
            EC.SV_OUTPUT_KIND_FORBIDDEN,
            EC.SV_CAPABILITY_KIND_INVALID,
            EC.SV_SAFE_LAUNCH_VERDICT_FAIL,
            EC.SV_ANSWER_ISOLATION_VERDICT_FAIL,
            EC.SV_NOTOOL_REPORT_VERDICT_FAIL,
            EC.SV_HARNESS_REPORT_VERDICT_FAIL,
            EC.SV_OBSERVE_TICKET_UNKNOWN,
            EC.SV_COLLECT_TICKET_UNKNOWN,
            EC.SV_PREPARE_JOB_INVALID,
            EC.SV_PREPARED_JOB_INVALID,
            EC.SV_LAUNCH_TICKET_INVALID,
            EC.SV_RECONCILE_UNKNOWN_ATTEMPT,
        ]
        for code in sv_codes:
            self.assertIsInstance(code, EC)


# ─── TargetSolverPort protocol ──────────────────────────────────────────


class TestTargetSolverPortProtocol(unittest.TestCase):
    """验证 TargetSolverPort 是 Protocol。"""

    def test_protocol_is_runtime_checkable(self):
        self.assertTrue(hasattr(TargetSolverPort, "_is_protocol"))
        # FakeHarnessAdapter should satisfy the protocol structurally
        adapter = FakeHarnessAdapter()
        self.assertIsInstance(adapter, TargetSolverPort)

    def test_protocol_methods_exist(self):
        for method in ("prepare", "launch", "observe", "collect", "cancel", "reconcile"):
            self.assertTrue(hasattr(TargetSolverPort, method))


# ─── SolverJob tests ────────────────────────────────────────────────────


class TestSolverJob(unittest.TestCase):
    """SolverJob 构建 + 验证 + hash。"""

    def test_build_solver_job_golden(self):
        job = _make_solver_job()
        self.assertEqual(job.attempt_id, "attempt-001")
        self.assertEqual(job.tool_policy_kind, "NO_TOOL")
        self.assertEqual(job.problem_ref_and_hash["ref_id"], "problem-001")

    def test_solver_job_hash_deterministic(self):
        job1 = _make_solver_job()
        job2 = _make_solver_job()
        self.assertEqual(job1.job_hash, job2.job_hash)

    def test_solver_job_hash_differs_on_change(self):
        job1 = _make_solver_job()
        job2 = _make_solver_job(attempt_id="attempt-002")
        self.assertNotEqual(job1.job_hash, job2.job_hash)

    def test_verify_solver_job_pass(self):
        job = _make_solver_job()
        result = verify_solver_job(job)
        self.assertTrue(result.passed)

    def test_verify_solver_job_to_dict_roundtrip(self):
        job = _make_solver_job()
        result = verify_solver_job(job.to_dict())
        self.assertTrue(result.passed)

    def test_verify_solver_job_missing_problem_ref(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["problem_ref_and_hash"] = {}
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_PROBLEM_REF_HASH_MISMATCH, result.error_codes)

    def test_verify_solver_job_missing_view_ref(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["view_ref_and_hash"] = {"ref_id": "v", "sha256": "bad"}
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_VIEW_REF_HASH_MISMATCH, result.error_codes)

    def test_verify_solver_job_invalid_budget(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["budget_contract"] = {"wallclock_seconds": -1}
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_BUDGET_CONTRACT_INVALID, result.error_codes)

    def test_verify_solver_job_invalid_tool_policy(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["tool_policy_kind"] = "UNKNOWN_POLICY"
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TOOL_POLICY_KIND_INVALID, result.error_codes)

    def test_verify_solver_job_empty_idempotency_key(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["idempotency_key"] = ""
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_verify_solver_job_empty_fence_token(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["fence_token"] = ""
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_FENCE_TOKEN_INVALID, result.error_codes)

    def test_verify_solver_job_repo_workspace_not_isolated(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["repo_workspace_spec"] = {"isolation_kind": "SHARED_REPO"}
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_REPO_WORKSPACE_NOT_ISOLATED, result.error_codes)

    def test_verify_solver_job_harness_profile_ref_invalid(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["harness_profile_ref_and_hash"] = {}
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_HARNESS_PROFILE_HASH_MISMATCH, result.error_codes)

    def test_verify_solver_job_hash_drift(self):
        job_dict = _make_solver_job().to_dict()
        job_dict["job_hash"] = "wrong"
        result = verify_solver_job(job_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_PREPARED_JOB_HASH_DRIFT, result.error_codes)


# ─── PreparedSolverJob tests ────────────────────────────────────────────


class TestPreparedSolverJob(unittest.TestCase):
    """PreparedSolverJob prepare + 验证 + hash。"""

    def test_prepare_solver_job_golden(self):
        job = _make_solver_job()
        prepared, result = prepare_solver_job(job)
        self.assertIsNotNone(prepared)
        self.assertTrue(result.passed)
        self.assertEqual(prepared.job_hash, job.job_hash)
        self.assertTrue(prepared.harness_profile_verified)

    def test_prepare_solver_job_hash_deterministic(self):
        job = _make_solver_job()
        prepared1, _ = prepare_solver_job(job)
        prepared2, _ = prepare_solver_job(job)
        self.assertEqual(prepared1.prepared_hash, prepared2.prepared_hash)

    def test_prepare_solver_job_invalid_job(self):
        job = _make_solver_job()
        job_dict = job.to_dict()
        job_dict["tool_policy_kind"] = "UNKNOWN"
        from seven_system.adapters.solver.port import SolverJob as SJ
        bad_job = SJ(**{
            "problem_ref_and_hash": job_dict["problem_ref_and_hash"],
            "view_ref_and_hash": job_dict["view_ref_and_hash"],
            "budget_contract": job_dict["budget_contract"],
            "tool_policy_kind": "UNKNOWN",
            "idempotency_key": job_dict["idempotency_key"],
            "fence_token": job_dict["fence_token"],
            "attempt_id": job_dict["attempt_id"],
            "repo_workspace_spec": job_dict["repo_workspace_spec"],
            "harness_profile_ref_and_hash": job_dict["harness_profile_ref_and_hash"],
        })
        prepared, result = prepare_solver_job(bad_job)
        self.assertIsNone(prepared)
        self.assertFalse(result.passed)

    def test_verify_prepared_solver_job_pass(self):
        job = _make_solver_job()
        prepared, _ = prepare_solver_job(job)
        result = verify_prepared_solver_job(prepared)
        self.assertTrue(result.passed)

    def test_verify_prepared_solver_job_hash_drift(self):
        job = _make_solver_job()
        prepared, _ = prepare_solver_job(job)
        prepared_dict = prepared.to_dict()
        prepared_dict["prepared_hash"] = "wrong"
        result = verify_prepared_solver_job(prepared_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_PREPARED_JOB_HASH_DRIFT, result.error_codes)

    def test_verify_prepared_solver_job_profile_not_verified(self):
        job = _make_solver_job()
        prepared, _ = prepare_solver_job(job, harness_profile_verified=False)
        result = verify_prepared_solver_job(prepared)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_HARNESS_PROFILE_HASH_MISMATCH, result.error_codes)


# ─── LaunchTicket tests ─────────────────────────────────────────────────


class TestLaunchTicket(unittest.TestCase):
    """LaunchTicket 验证。"""

    def test_verify_launch_ticket_pass(self):
        ticket = LaunchTicket(
            attempt_id="attempt-001",
            fence_token="fence-001",
            launch_timestamp="2026-08-14T12:00:00Z",
            launch_state="LAUNCHED",
            prepared_hash=_ZERO_HASH,
        )
        result = verify_launch_ticket(ticket)
        self.assertTrue(result.passed)

    def test_verify_launch_ticket_empty_attempt_id(self):
        ticket_dict = {
            "attempt_id": "",
            "fence_token": "fence-001",
            "launch_timestamp": "2026-08-14T12:00:00Z",
            "launch_state": "LAUNCHED",
            "prepared_hash": _ZERO_HASH,
        }
        result = verify_launch_ticket(ticket_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_LAUNCH_TICKET_INVALID, result.error_codes)

    def test_verify_launch_ticket_invalid_state(self):
        ticket_dict = {
            "attempt_id": "attempt-001",
            "fence_token": "fence-001",
            "launch_timestamp": "2026-08-14T12:00:00Z",
            "launch_state": "UNKNOWN_STATE",
            "prepared_hash": _ZERO_HASH,
        }
        result = verify_launch_ticket(ticket_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_LAUNCH_STATE_INVALID, result.error_codes)

    def test_verify_launch_ticket_bad_prepared_hash(self):
        ticket_dict = {
            "attempt_id": "attempt-001",
            "fence_token": "fence-001",
            "launch_timestamp": "2026-08-14T12:00:00Z",
            "launch_state": "LAUNCHED",
            "prepared_hash": "bad",
        }
        result = verify_launch_ticket(ticket_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_LAUNCH_TICKET_INVALID, result.error_codes)


# ─── LaunchReceipt tests ────────────────────────────────────────────────


class TestLaunchReceipt(unittest.TestCase):
    """LaunchReceipt 构建 + 验证 + hash。"""

    def test_build_launch_receipt_golden(self):
        receipt = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="answer-001",
            answer_sha256=_FAKE_HASH_B,
        )
        self.assertEqual(receipt.terminal_reason, "COMPLETED")
        self.assertEqual(receipt.trajectory_kind, "FULL_TRAJECTORY")
        self.assertEqual(receipt.answer_kind, "FINAL_ANSWER")

    def test_launch_receipt_hash_deterministic(self):
        r1 = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="t1", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="a1", answer_sha256=_FAKE_HASH_B,
        )
        r2 = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="t1", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="a1", answer_sha256=_FAKE_HASH_B,
        )
        self.assertEqual(r1.report_hash, r2.report_hash)

    def test_launch_receipt_hash_differs_on_change(self):
        r1 = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="t1", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="ans1", answer_sha256=_FAKE_HASH_B,
        )
        r2 = build_launch_receipt(
            attempt_id="a2", fence_token="f1",
            trajectory_ref_id="t1", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="ans1", answer_sha256=_FAKE_HASH_B,
        )
        self.assertNotEqual(r1.report_hash, r2.report_hash)

    def test_verify_launch_receipt_pass(self):
        receipt = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="answer-001",
            answer_sha256=_FAKE_HASH_B,
        )
        result = verify_launch_receipt(receipt)
        self.assertTrue(result.passed)

    def test_verify_launch_receipt_missing_trajectory(self):
        """Blocker: missing trajectory → FAIL."""
        receipt_dict = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="answer-001",
            answer_sha256=_FAKE_HASH_B,
        ).to_dict()
        receipt_dict["trajectory_ref_and_hash"] = {}
        result = verify_launch_receipt(receipt_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TRAJECTORY_MISSING, result.error_codes)

    def test_verify_launch_receipt_answer_not_isolated(self):
        """Blocker: answer not isolated → FAIL."""
        receipt_dict = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="traj-001",  # same as trajectory!
            answer_sha256=_FAKE_HASH_B,
        ).to_dict()
        result = verify_launch_receipt(receipt_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_ANSWER_NOT_ISOLATED, result.error_codes)

    def test_verify_launch_receipt_invalid_terminal_reason(self):
        receipt_dict = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="answer-001",
            answer_sha256=_FAKE_HASH_B,
            terminal_reason="UNKNOWN_REASON",
        ).to_dict()
        result = verify_launch_receipt(receipt_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TERMINAL_REASON_INVALID, result.error_codes)

    def test_verify_launch_receipt_invalid_trajectory_kind(self):
        receipt_dict = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="answer-001",
            answer_sha256=_FAKE_HASH_B,
            trajectory_kind="UNKNOWN_KIND",
        ).to_dict()
        result = verify_launch_receipt(receipt_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TRAJECTORY_KIND_INVALID, result.error_codes)

    def test_verify_launch_receipt_invalid_answer_kind(self):
        receipt_dict = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="answer-001",
            answer_sha256=_FAKE_HASH_B,
            answer_kind="UNKNOWN_ANSWER",
        ).to_dict()
        result = verify_launch_receipt(receipt_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_ANSWER_KIND_INVALID, result.error_codes)

    def test_verify_launch_receipt_hash_mismatch(self):
        receipt_dict = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="answer-001",
            answer_sha256=_FAKE_HASH_B,
        ).to_dict()
        receipt_dict["report_hash"] = "wrong"
        result = verify_launch_receipt(receipt_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.OBJECT_HASH_MISMATCH, result.error_codes)

    def test_verify_launch_receipt_bad_cost_observability(self):
        receipt_dict = build_launch_receipt(
            attempt_id="attempt-001",
            fence_token="fence-001",
            trajectory_ref_id="traj-001",
            trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="answer-001",
            answer_sha256=_FAKE_HASH_B,
        ).to_dict()
        receipt_dict["cost_observability"]["input_tokens"] = -1
        result = verify_launch_receipt(receipt_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_LAUNCH_RECEIPT_INCOMPLETE, result.error_codes)


# ─── HarnessProfile tests ───────────────────────────────────────────────


class TestHarnessProfile(unittest.TestCase):
    """HarnessProfile 构建 + 验证 + hash。"""

    def test_build_harness_profile_golden(self):
        content = hashlib.sha256(b"harness-content").hexdigest()
        profile = build_harness_profile(
            version="harness-v1",
            content_hash=content,
            harness_kind="DEVIN_HARNESS",
            tool_policy_kind="NO_TOOL",
        )
        self.assertEqual(profile.version, "harness-v1")
        self.assertEqual(profile.harness_kind, "DEVIN_HARNESS")

    def test_harness_profile_hash_deterministic(self):
        content = hashlib.sha256(b"harness-content").hexdigest()
        p1 = build_harness_profile(version="v1", content_hash=content)
        p2 = build_harness_profile(version="v1", content_hash=content)
        self.assertEqual(p1.profile_hash, p2.profile_hash)

    def test_harness_profile_hash_differs_on_change(self):
        content = hashlib.sha256(b"harness-content").hexdigest()
        p1 = build_harness_profile(version="v1", content_hash=content)
        p2 = build_harness_profile(version="v2", content_hash=content)
        self.assertNotEqual(p1.profile_hash, p2.profile_hash)

    def test_verify_harness_profile_pass(self):
        content = hashlib.sha256(b"harness-content").hexdigest()
        profile = build_harness_profile(version="v1", content_hash=content)
        result = verify_harness_profile(profile)
        self.assertTrue(result.passed)

    def test_verify_harness_profile_empty_version(self):
        profile_dict = build_harness_profile(
            version="v1", content_hash=_ZERO_HASH,
        ).to_dict()
        profile_dict["version"] = ""
        result = verify_harness_profile(profile_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_HARNESS_PROFILE_HASH_MISMATCH, result.error_codes)

    def test_verify_harness_profile_bad_content_hash(self):
        profile_dict = build_harness_profile(
            version="v1", content_hash=_ZERO_HASH,
        ).to_dict()
        profile_dict["content_hash"] = "bad"
        result = verify_harness_profile(profile_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_HARNESS_PROFILE_HASH_MISMATCH, result.error_codes)

    def test_verify_harness_profile_invalid_harness_kind(self):
        profile_dict = build_harness_profile(
            version="v1", content_hash=_ZERO_HASH,
        ).to_dict()
        profile_dict["harness_kind"] = "UNKNOWN"
        result = verify_harness_profile(profile_dict)
        self.assertFalse(result.passed)

    def test_verify_harness_profile_invalid_tool_policy(self):
        profile_dict = build_harness_profile(
            version="v1", content_hash=_ZERO_HASH,
        ).to_dict()
        profile_dict["tool_policy_kind"] = "UNKNOWN"
        result = verify_harness_profile(profile_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TOOL_POLICY_KIND_INVALID, result.error_codes)

    def test_verify_harness_profile_hash_mismatch(self):
        profile_dict = build_harness_profile(
            version="v1", content_hash=_ZERO_HASH,
        ).to_dict()
        profile_dict["profile_hash"] = "wrong"
        result = verify_harness_profile(profile_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_HARNESS_PROFILE_HASH_MISMATCH, result.error_codes)

    def test_harness_kinds_constant(self):
        self.assertIn("DEVIN_HARNESS", HARNESS_KINDS)
        self.assertIn("FAKE_HARNESS", HARNESS_KINDS)


# ─── NoToolPolicy tests ─────────────────────────────────────────────────


class TestNoToolPolicy(unittest.TestCase):
    """NoToolPolicy 构建 + 验证 + tool event 检测。"""

    def test_build_notool_policy_golden(self):
        policy = build_notool_policy()
        self.assertEqual(policy.policy_kind, "NO_TOOL")
        self.assertEqual(policy.declared_tool_events, [])

    def test_notool_policy_hash_deterministic(self):
        p1 = build_notool_policy()
        p2 = build_notool_policy()
        self.assertEqual(p1.policy_hash, p2.policy_hash)

    def test_verify_notool_policy_pass(self):
        policy = build_notool_policy()
        result = verify_notool_policy(policy)
        self.assertTrue(result.passed)

    def test_verify_notool_policy_violation_with_events(self):
        """Blocker: NoTool policy violation → FAIL."""
        policy_dict = build_notool_policy(
            declared_tool_events=[{"tool_name": "shell"}],
        ).to_dict()
        result = verify_notool_policy(policy_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_NOTOOL_VIOLATION, result.error_codes)

    def test_verify_notool_policy_wrong_kind(self):
        policy_dict = build_notool_policy().to_dict()
        policy_dict["policy_kind"] = "READ_ONLY_TOOLS"
        result = verify_notool_policy(policy_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_NOTOOL_VIOLATION, result.error_codes)

    def test_verify_notool_policy_hash_mismatch(self):
        policy_dict = build_notool_policy().to_dict()
        policy_dict["policy_hash"] = "wrong"
        result = verify_notool_policy(policy_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.OBJECT_HASH_MISMATCH, result.error_codes)

    def test_check_trajectory_no_tool_events_pass(self):
        trajectory = {
            "steps": [
                {"step_type": "assistant", "content": "reasoning"},
                {"step_type": "terminal", "event": "COMPLETED"},
            ],
        }
        result = check_trajectory_for_tool_events(trajectory)
        self.assertTrue(result.passed)

    def test_check_trajectory_tool_event_detected(self):
        """Blocker: tool event in trajectory → FAIL."""
        trajectory = {
            "steps": [
                {"step_type": "assistant", "content": "reasoning"},
                {"step_type": "tool", "tool_name": "shell", "content": "ls"},
                {"step_type": "terminal", "event": "COMPLETED"},
            ],
        }
        result = check_trajectory_for_tool_events(trajectory)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TOOL_EVENT_DETECTED, result.error_codes)

    def test_check_trajectory_list_format(self):
        trajectory = [
            {"step_type": "assistant", "content": "reasoning"},
            {"step_type": "tool", "tool_name": "shell"},
        ]
        result = check_trajectory_for_tool_events(trajectory)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TOOL_EVENT_DETECTED, result.error_codes)

    def test_check_trajectory_empty_pass(self):
        result = check_trajectory_for_tool_events({"steps": []})
        self.assertTrue(result.passed)

    def test_check_trajectory_invalid_type(self):
        result = check_trajectory_for_tool_events("invalid")
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TOOL_EVENT_DETECTED, result.error_codes)


# ─── FakeHarnessAdapter golden lifecycle ────────────────────────────────


class TestFakeHarnessAdapterGolden(unittest.TestCase):
    """Golden: prepare→launch→observe→collect→reconcile full lifecycle。"""

    def test_full_lifecycle(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        self.assertTrue(prepared.harness_profile_verified)

        ticket = adapter.launch(prepared)
        self.assertEqual(ticket.launch_state, "LAUNCHED")

        snapshot = adapter.observe(ticket)
        self.assertEqual(snapshot["attempt_id"], ticket.attempt_id)
        self.assertFalse(snapshot["is_terminal"])

        receipt = adapter.collect(ticket)
        self.assertEqual(receipt.terminal_reason, "COMPLETED")
        self.assertEqual(receipt.trajectory_kind, "FULL_TRAJECTORY")
        self.assertEqual(receipt.answer_kind, "FINAL_ANSWER")

        # verify receipt
        receipt_result = verify_launch_receipt(receipt)
        self.assertTrue(receipt_result.passed)

        # after collect, should be terminal
        snapshot2 = adapter.observe(ticket)
        self.assertTrue(snapshot2["is_terminal"])

        # reconcile
        reconcile_result = adapter.reconcile(ticket.attempt_id, ticket.fence_token)
        self.assertTrue(reconcile_result.passed)

    def test_adapter_satisfies_protocol(self):
        adapter = FakeHarnessAdapter()
        self.assertIsInstance(adapter, TargetSolverPort)
        self.assertIsInstance(adapter, HarnessAdapter)

    def test_adapter_default_profile_and_policy(self):
        adapter = FakeHarnessAdapter()
        self.assertIsNotNone(adapter.harness_profile)
        self.assertIsNotNone(adapter.notool_policy)
        self.assertEqual(adapter.harness_profile.harness_kind, "FAKE_HARNESS")
        self.assertEqual(adapter.notool_policy.policy_kind, "NO_TOOL")

    def test_receipt_answer_isolated_from_trajectory(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        self.assertNotEqual(
            receipt.trajectory_ref_and_hash["ref_id"],
            receipt.answer_ref_and_hash["ref_id"],
        )
        self.assertNotEqual(
            receipt.trajectory_ref_and_hash["sha256"],
            receipt.answer_ref_and_hash["sha256"],
        )

    def test_receipt_trajectory_present(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        self.assertTrue(receipt.trajectory_ref_and_hash["ref_id"])
        self.assertTrue(receipt.trajectory_ref_and_hash["sha256"])

    def test_cancel_before_terminal(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.cancel(ticket, ticket.fence_token)
        self.assertEqual(receipt.terminal_reason, "CANCELLED")
        self.assertEqual(receipt.answer_kind, "NO_ANSWER")


# ─── FakeHarnessAdapter negative / blocker tests ────────────────────────


class TestFakeHarnessAdapterBlockers(unittest.TestCase):
    """Blocker tests: fault injection 触发各 blocker。"""

    def test_blocker_direct_devin_bypass(self):
        """Blocker: direct-devin bypass detected → FAIL."""
        adapter = FakeHarnessAdapter(force_direct_devin_bypass=True)
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        self.assertEqual(receipt.failure_or_quarantine_state, "DIRECT_DEVIN_BYPASS_DETECTED")
        self.assertEqual(receipt.terminal_reason, "FAILED_PERMANENT")

    def test_blocker_tool_event_in_trajectory(self):
        """Blocker: tool event in trajectory → FAIL."""
        adapter = FakeHarnessAdapter(force_tool_events=True)
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        # receipt itself is valid, but trajectory has tool events
        # verify via SafeLaunchReport
        report = build_safe_launch_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
            trajectory={
                "steps": [
                    {"step_type": "assistant"},
                    {"step_type": "tool", "tool_name": "shell"},
                    {"step_type": "terminal"},
                ],
            },
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_TOOL_EVENT_DETECTED", report.blockers)

    def test_blocker_missing_trajectory(self):
        """Blocker: missing trajectory → FAIL."""
        adapter = FakeHarnessAdapter(force_missing_trajectory=True)
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        # receipt has empty trajectory
        result = verify_launch_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_TRAJECTORY_MISSING, result.error_codes)

    def test_blocker_repo_workspace_not_isolated(self):
        """Blocker: repo workspace not isolated → FAIL."""
        adapter = FakeHarnessAdapter(force_repo_workspace_not_isolated=True)
        job = _make_solver_job(profile=adapter.harness_profile)
        with self.assertRaises(SolverJobError) as ctx:
            adapter.prepare(job)
        self.assertEqual(ctx.exception.code, EC.SV_REPO_WORKSPACE_NOT_ISOLATED)

    def test_blocker_answer_not_isolated(self):
        """Blocker: answer not isolated from process → FAIL."""
        adapter = FakeHarnessAdapter(force_answer_not_isolated=True)
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        # answer_ref_id == trajectory_ref_id
        self.assertEqual(
            receipt.trajectory_ref_and_hash["ref_id"],
            receipt.answer_ref_and_hash["ref_id"],
        )
        result = verify_launch_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_ANSWER_NOT_ISOLATED, result.error_codes)

    def test_blocker_notool_violation(self):
        """Blocker: NoTool policy violation → FAIL."""
        policy_dict = build_notool_policy(
            declared_tool_events=[{"tool_name": "shell"}],
        ).to_dict()
        result = verify_notool_policy(policy_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_NOTOOL_VIOLATION, result.error_codes)

    def test_blocker_cancel_after_terminal(self):
        """Blocker: cancel after terminal → FAIL."""
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        adapter.collect(ticket)  # makes it terminal
        with self.assertRaises(SolverJobError) as ctx:
            adapter.cancel(ticket, ticket.fence_token)
        self.assertEqual(ctx.exception.code, EC.SV_CANCEL_AFTER_TERMINAL)

    def test_blocker_fence_mismatch_on_collect(self):
        """Blocker: fence mismatch → FAIL."""
        adapter = FakeHarnessAdapter(force_fence_mismatch=True)
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        with self.assertRaises(SolverJobError) as ctx:
            adapter.collect(ticket)
        self.assertEqual(ctx.exception.code, EC.SV_FENCE_TOKEN_INVALID)

    def test_blocker_fence_mismatch_on_cancel(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        with self.assertRaises(SolverJobError) as ctx:
            adapter.cancel(ticket, "wrong-fence")
        self.assertEqual(ctx.exception.code, EC.SV_FENCE_TOKEN_INVALID)

    def test_blocker_budget_exceeded(self):
        """Blocker: budget exceeded → FAIL."""
        adapter = FakeHarnessAdapter(force_budget_exceeded=True)
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        with self.assertRaises(SolverJobError) as ctx:
            adapter.launch(prepared)
        self.assertEqual(ctx.exception.code, EC.SV_BUDGET_EXCEEDED)

    def test_blocker_profile_hash_mismatch(self):
        """Blocker: profile hash mismatch → FAIL."""
        adapter = FakeHarnessAdapter(force_profile_hash_mismatch=True)
        job = _make_solver_job(profile=adapter.harness_profile)
        with self.assertRaises(SolverJobError) as ctx:
            adapter.prepare(job)
        self.assertEqual(ctx.exception.code, EC.SV_HARNESS_PROFILE_HASH_MISMATCH)

    def test_blocker_observe_unknown_ticket(self):
        adapter = FakeHarnessAdapter()
        fake_ticket = LaunchTicket(
            attempt_id="unknown",
            fence_token="fence",
            launch_timestamp="2026-08-14T12:00:00Z",
            launch_state="LAUNCHED",
            prepared_hash=_ZERO_HASH,
        )
        with self.assertRaises(SolverJobError) as ctx:
            adapter.observe(fake_ticket)
        self.assertEqual(ctx.exception.code, EC.SV_OBSERVE_TICKET_UNKNOWN)

    def test_blocker_collect_unknown_ticket(self):
        adapter = FakeHarnessAdapter()
        fake_ticket = LaunchTicket(
            attempt_id="unknown",
            fence_token="fence",
            launch_timestamp="2026-08-14T12:00:00Z",
            launch_state="LAUNCHED",
            prepared_hash=_ZERO_HASH,
        )
        with self.assertRaises(SolverJobError) as ctx:
            adapter.collect(fake_ticket)
        self.assertEqual(ctx.exception.code, EC.SV_COLLECT_TICKET_UNKNOWN)

    def test_reconcile_unknown_attempt(self):
        adapter = FakeHarnessAdapter()
        result = adapter.reconcile("unknown", "fence")
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_RECONCILE_UNKNOWN_ATTEMPT, result.error_codes)

    def test_reconcile_fence_mismatch(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        adapter.collect(ticket)
        result = adapter.reconcile(ticket.attempt_id, "wrong-fence")
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_RECONCILE_FENCE_MISMATCH, result.error_codes)

    def test_prepare_invalid_job_raises(self):
        adapter = FakeHarnessAdapter()
        bad_job = _make_solver_job(profile=adapter.harness_profile, tool_policy_kind="UNKNOWN")
        with self.assertRaises(SolverJobError):
            adapter.prepare(bad_job)

    def test_launch_invalid_prepared_raises(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared, _ = prepare_solver_job(job)
        # tamper with prepared
        tampered = PreparedSolverJob(
            job=prepared.job,
            job_hash="wrong",
            prepared_hash=prepared.prepared_hash,
            prepared_at=prepared.prepared_at,
            harness_profile_verified=True,
        )
        with self.assertRaises(SolverJobError) as ctx:
            adapter.launch(tampered)
        self.assertEqual(ctx.exception.code, EC.SV_PREPARED_JOB_HASH_DRIFT)


# ─── SafeLaunchReport tests ─────────────────────────────────────────────


class TestSafeLaunchReport(unittest.TestCase):
    """SafeLaunchReport build + verify + boundary。"""

    def test_build_safe_launch_report_pass(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report = build_safe_launch_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
            adapter_metadata={"repo_workspace_isolated": True},
        )
        self.assertEqual(report.verdict, "PASS")
        self.assertEqual(report.blockers, [])

    def test_verify_safe_launch_report_pass(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report = build_safe_launch_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
        )
        result = verify_safe_launch_report(report)
        self.assertTrue(result.passed)

    def test_safe_launch_report_check_ids(self):
        self.assertEqual(len(SAFE_LAUNCH_CHECK_IDS), 5)
        self.assertIn("sv1.safe_launch.no_direct_devin_bypass", SAFE_LAUNCH_CHECK_IDS)
        self.assertIn("sv1.safe_launch.repo_workspace_isolated", SAFE_LAUNCH_CHECK_IDS)
        self.assertIn("sv1.safe_launch.no_tool_events", SAFE_LAUNCH_CHECK_IDS)
        self.assertIn("sv1.safe_launch.trajectory_present", SAFE_LAUNCH_CHECK_IDS)
        self.assertIn("sv1.safe_launch.answer_isolation_maintained", SAFE_LAUNCH_CHECK_IDS)

    def test_safe_launch_report_direct_devin_bypass(self):
        """Blocker: direct-devin bypass detected → FAIL."""
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report = build_safe_launch_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
            adapter_metadata={"direct_devin_bypass": True},
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_DIRECT_DEVIN_BYPASS", report.blockers)

    def test_safe_launch_report_repo_workspace_not_isolated(self):
        """Blocker: repo workspace not isolated → FAIL."""
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report = build_safe_launch_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
            adapter_metadata={"repo_workspace_isolated": False},
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_REPO_WORKSPACE_NOT_ISOLATED", report.blockers)

    def test_safe_launch_report_tool_events(self):
        """Blocker: tool event detected → FAIL."""
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report = build_safe_launch_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
            trajectory={"steps": [{"step_type": "tool", "tool_name": "shell"}]},
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_TOOL_EVENT_DETECTED", report.blockers)

    def test_safe_launch_report_missing_trajectory(self):
        """Blocker: missing trajectory → FAIL."""
        receipt_dict = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="t1", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="ans1", answer_sha256=_FAKE_HASH_B,
        ).to_dict()
        receipt_dict["trajectory_ref_and_hash"] = {}
        report = build_safe_launch_report(
            attempt_id="a1",
            receipt=receipt_dict,
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_TRAJECTORY_MISSING", report.blockers)

    def test_safe_launch_report_answer_not_isolated(self):
        """Blocker: answer not isolated → FAIL."""
        receipt_dict = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="same", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="same", answer_sha256=_FAKE_HASH_B,
        ).to_dict()
        report = build_safe_launch_report(
            attempt_id="a1",
            receipt=receipt_dict,
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_ANSWER_NOT_ISOLATED", report.blockers)

    def test_safe_launch_report_hash_deterministic(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        r1 = build_safe_launch_report(attempt_id=ticket.attempt_id, receipt=receipt)
        r2 = build_safe_launch_report(attempt_id=ticket.attempt_id, receipt=receipt)
        self.assertEqual(r1.report_hash, r2.report_hash)

    def test_verify_safe_launch_report_hash_mismatch(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report_dict = build_safe_launch_report(
            attempt_id=ticket.attempt_id, receipt=receipt,
        ).to_dict()
        report_dict["report_hash"] = "wrong"
        result = verify_safe_launch_report(report_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.OBJECT_HASH_MISMATCH, result.error_codes)

    def test_verify_safe_launch_report_verdict_inconsistency(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report_dict = build_safe_launch_report(
            attempt_id=ticket.attempt_id, receipt=receipt,
        ).to_dict()
        # flip verdict but keep no blockers
        report_dict["verdict"] = "FAIL"
        result = verify_safe_launch_report(report_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_SAFE_LAUNCH_VERDICT_FAIL, result.error_codes)


# ─── AnswerIsolationReport tests ────────────────────────────────────────


class TestAnswerIsolationReport(unittest.TestCase):
    """AnswerIsolationReport build + verify + boundary。"""

    def test_build_answer_isolation_report_pass(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report = build_answer_isolation_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
        )
        self.assertEqual(report.verdict, "PASS")
        self.assertEqual(report.blockers, [])

    def test_verify_answer_isolation_report_pass(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report = build_answer_isolation_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
        )
        result = verify_answer_isolation_report(report)
        self.assertTrue(result.passed)

    def test_answer_isolation_check_ids(self):
        self.assertEqual(len(ANSWER_ISOLATION_CHECK_IDS), 4)
        self.assertIn(
            "sv1.answer_isolation.answer_ref_separate_from_trajectory_ref",
            ANSWER_ISOLATION_CHECK_IDS,
        )

    def test_answer_isolation_report_refs_not_separate(self):
        """Blocker: answer not isolated → FAIL."""
        receipt_dict = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="same", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="same", answer_sha256=_FAKE_HASH_B,
        ).to_dict()
        report = build_answer_isolation_report(
            attempt_id="a1",
            receipt=receipt_dict,
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_ANSWER_NOT_ISOLATED", report.blockers)

    def test_answer_isolation_report_hashes_not_independent(self):
        """Blocker: answer hash same as trajectory hash → FAIL."""
        receipt_dict = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="traj1", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="ans1", answer_sha256=_FAKE_HASH_A,  # same hash!
        ).to_dict()
        report = build_answer_isolation_report(
            attempt_id="a1",
            receipt=receipt_dict,
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_ANSWER_NOT_ISOLATED", report.blockers)

    def test_answer_isolation_report_answer_embedded_in_trajectory(self):
        """Blocker: answer embedded in trajectory → FAIL."""
        receipt = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="traj1", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="ans1", answer_sha256=_FAKE_HASH_B,
        )
        report = build_answer_isolation_report(
            attempt_id="a1",
            receipt=receipt,
            trajectory_content="the answer is 42 and some reasoning",
            answer_content="the answer is 42",
        )
        self.assertEqual(report.verdict, "FAIL")
        self.assertIn("SV_ANSWER_NOT_ISOLATED", report.blockers)

    def test_answer_isolation_report_answer_not_embedded_pass(self):
        receipt = build_launch_receipt(
            attempt_id="a1", fence_token="f1",
            trajectory_ref_id="traj1", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="ans1", answer_sha256=_FAKE_HASH_B,
        )
        report = build_answer_isolation_report(
            attempt_id="a1",
            receipt=receipt,
            trajectory_content="step by step reasoning process",
            answer_content="42",
        )
        self.assertEqual(report.verdict, "PASS")

    def test_answer_isolation_report_hash_deterministic(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        r1 = build_answer_isolation_report(attempt_id=ticket.attempt_id, receipt=receipt)
        r2 = build_answer_isolation_report(attempt_id=ticket.attempt_id, receipt=receipt)
        self.assertEqual(r1.report_hash, r2.report_hash)

    def test_verify_answer_isolation_report_hash_mismatch(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report_dict = build_answer_isolation_report(
            attempt_id=ticket.attempt_id, receipt=receipt,
        ).to_dict()
        report_dict["report_hash"] = "wrong"
        result = verify_answer_isolation_report(report_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.OBJECT_HASH_MISMATCH, result.error_codes)

    def test_verify_answer_isolation_report_verdict_inconsistency(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)
        report_dict = build_answer_isolation_report(
            attempt_id=ticket.attempt_id, receipt=receipt,
        ).to_dict()
        report_dict["verdict"] = "FAIL"
        result = verify_answer_isolation_report(report_dict)
        self.assertFalse(result.passed)
        self.assertIn(EC.SV_ANSWER_ISOLATION_VERDICT_FAIL, result.error_codes)


# ─── SolverCapabilityReport tests ───────────────────────────────────────


class TestSolverCapabilityReport(unittest.TestCase):
    """SolverCapabilityReport build + verify + boundary。"""

    def _build_report(self, **overrides) -> dict:
        defaults = dict(
            harness_profile_hash=_ZERO_HASH,
            notool_policy_hash=_ZERO_HASH,
            safe_launch_report_hash=_ZERO_HASH,
            answer_isolation_report_hash=_ZERO_HASH,
            dag_hash=_ZERO_HASH,
            probe_results=[],
            positive_evidence_refs=[],
            negative_evidence_refs=[],
            residual_risks=[],
            verifier_identity="sv1-test-verifier",
            generated_at="2026-08-14T12:00:00+00:00",
        )
        defaults.update(overrides)
        return build_solver_capability_report(**defaults)

    def test_build_solver_capability_report_golden(self):
        report = self._build_report()
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["report_kind"], "SolverCapabilityReport")
        self.assertEqual(report["blockers"], [])

    def test_verify_solver_capability_report_pass(self):
        report = self._build_report()
        errors = verify_solver_capability_report(report)
        self.assertEqual(errors, ())

    def test_solver_check_ids(self):
        self.assertEqual(len(SOLVER_CHECK_IDS), 5)
        self.assertIn("sv1.solver.harness_adapter_isolated", SOLVER_CHECK_IDS)
        self.assertIn("sv1.solver.notool_policy_enforced", SOLVER_CHECK_IDS)
        self.assertIn("sv1.solver.safe_launch_verified", SOLVER_CHECK_IDS)
        self.assertIn("sv1.solver.answer_isolation_verified", SOLVER_CHECK_IDS)
        self.assertIn("sv1.solver.boundary_no_other_wp_reports", SOLVER_CHECK_IDS)

    def test_solver_claims(self):
        self.assertEqual(len(SOLVER_CLAIMS), 5)
        for claim in SOLVER_CLAIMS:
            self.assertIsInstance(claim, str)

    def test_solver_nonclaims(self):
        self.assertEqual(len(SOLVER_NONCLAIMS), 5)
        for nc in SOLVER_NONCLAIMS:
            self.assertIsInstance(nc, str)

    def test_solver_side_effect_keys(self):
        self.assertIn("solver_launches", SOLVER_SIDE_EFFECT_KEYS)
        self.assertIn("database_writes", SOLVER_SIDE_EFFECT_KEYS)
        self.assertIn("subprocess_calls", SOLVER_SIDE_EFFECT_KEYS)

    def test_capability_kinds_match(self):
        report = self._build_report()
        self.assertEqual(set(report["capability_kinds"]), set(SV_CAPABILITY_KINDS))

    def test_side_effects_all_zero(self):
        report = self._build_report()
        for key in SOLVER_SIDE_EFFECT_KEYS:
            self.assertEqual(report["side_effects"][key], 0)

    def test_build_report_invalid_hash_raises(self):
        with self.assertRaises(SolverCapabilityReportError):
            self._build_report(harness_profile_hash="bad")

    def test_verify_report_wrong_schema_version(self):
        report = self._build_report()
        report["schema_version"] = "wrong"
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_verify_report_wrong_report_kind(self):
        report = self._build_report()
        report["report_kind"] = "DatabaseRuntimeCapabilityReport"
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.SV_OUTPUT_KIND_FORBIDDEN for e in errors))

    def test_verify_report_wrong_scope(self):
        report = self._build_report()
        report["scope"] = "wrong"
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_verify_report_bad_capability_kinds(self):
        report = self._build_report()
        report["capability_kinds"] = ["WRONG_KIND"]
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.SV_CAPABILITY_KIND_INVALID for e in errors))

    def test_verify_report_nonzero_side_effects(self):
        report = self._build_report()
        report["side_effects"]["solver_launches"] = 1
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.SV_DIRECT_DEVIN_BYPASS for e in errors))

    def test_verify_report_wrong_verdict(self):
        report = self._build_report()
        report["verdict"] = "FAIL"
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_verify_report_blockers_not_empty(self):
        report = self._build_report()
        report["blockers"] = ["some_blocker"]
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_verify_report_wrong_nonclaims(self):
        report = self._build_report()
        report["explicit_nonclaims"] = ["wrong"]
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_verify_report_wrong_checks(self):
        report = self._build_report()
        report["checks"] = [{"check_id": "wrong", "verdict": "PASS", "evidence": []}]
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_verify_report_check_not_pass(self):
        report = self._build_report()
        report["checks"][0]["verdict"] = "FAIL"
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_verify_report_wrong_claims(self):
        report = self._build_report()
        report["claims"] = {"wrong": True}
        errors = verify_solver_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_verify_report_not_dict(self):
        errors = verify_solver_capability_report("not a dict")
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))


# ─── SV1 boundary tests ─────────────────────────────────────────────────


class TestSV1Boundary(unittest.TestCase):
    """SV1 boundary tests: allowed/forbidden output kinds。"""

    def test_allowed_output_kinds_not_in_forbidden(self):
        self.assertEqual(
            SV_ALLOWED_OUTPUT_KINDS & SV_FORBIDDEN_OUTPUT_KINDS,
            frozenset(),
        )

    def test_solver_capability_report_in_allowed(self):
        self.assertIn("SolverSafeLaunchReport", SV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("SolverAnswerIsolationReport", SV_ALLOWED_OUTPUT_KINDS)
        self.assertIn("SolverLaunchReceipt", SV_ALLOWED_OUTPUT_KINDS)

    def test_other_wp_reports_in_forbidden(self):
        """SV1 不得输出其他工作包的报告。"""
        for forbidden in SV_FORBIDDEN_OUTPUT_KINDS:
            self.assertNotIn(forbidden, SV_ALLOWED_OUTPUT_KINDS)

    def test_solver_capability_report_does_not_produce_forbidden(self):
        """SolverCapabilityReport 的 report_kind 不在 forbidden 集合中。"""
        report = build_solver_capability_report(
            harness_profile_hash=_ZERO_HASH,
            notool_policy_hash=_ZERO_HASH,
            safe_launch_report_hash=_ZERO_HASH,
            answer_isolation_report_hash=_ZERO_HASH,
            dag_hash=_ZERO_HASH,
            probe_results=[],
            positive_evidence_refs=[],
            negative_evidence_refs=[],
            residual_risks=[],
            verifier_identity="test",
            generated_at="2026-08-14T12:00:00+00:00",
        )
        self.assertNotIn(report["report_kind"], SV_FORBIDDEN_OUTPUT_KINDS)


# ─── Deterministic hash tests ───────────────────────────────────────────


class TestDeterministicHashes(unittest.TestCase):
    """确定性 hash 测试。"""

    def test_solver_job_hash_stable_across_instances(self):
        job = _make_solver_job()
        h1 = job.job_hash
        # rebuild from dict
        from seven_system.adapters.solver.port import SolverJob as SJ
        job2 = SJ(**job.to_dict())
        self.assertEqual(h1, job2.job_hash)

    def test_launch_receipt_hash_stable(self):
        r1 = build_launch_receipt(
            attempt_id="a", fence_token="f",
            trajectory_ref_id="t", trajectory_sha256=_FAKE_HASH_A,
            answer_ref_id="ans", answer_sha256=_FAKE_HASH_B,
        )
        # rebuild from dict and verify hash
        r2_dict = r1.to_dict()
        computed = hashlib.sha256(
            canonical_json_bytes({**r2_dict, "report_hash": None})
        ).hexdigest()
        self.assertEqual(r1.report_hash, computed)

    def test_harness_profile_hash_stable(self):
        content = hashlib.sha256(b"test").hexdigest()
        p = build_harness_profile(version="v1", content_hash=content)
        p_dict = p.to_dict()
        computed = hashlib.sha256(
            canonical_json_bytes({**p_dict, "profile_hash": None})
        ).hexdigest()
        self.assertEqual(p.profile_hash, computed)

    def test_notool_policy_hash_stable(self):
        p = build_notool_policy()
        p_dict = p.to_dict()
        computed = hashlib.sha256(
            canonical_json_bytes({**p_dict, "policy_hash": None})
        ).hexdigest()
        self.assertEqual(p.policy_hash, computed)


# ─── Integration: full lifecycle with reports ──────────────────────────


class TestSV1FullLifecycleWithReports(unittest.TestCase):
    """完整 lifecycle + 所有 reports 集成测试。"""

    def test_full_lifecycle_with_all_reports(self):
        adapter = FakeHarnessAdapter()
        job = _make_solver_job(profile=adapter.harness_profile)
        prepared = adapter.prepare(job)
        ticket = adapter.launch(prepared)
        receipt = adapter.collect(ticket)

        # verify receipt
        self.assertTrue(verify_launch_receipt(receipt).passed)

        # build SafeLaunchReport
        safe_report = build_safe_launch_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
            adapter_metadata={"repo_workspace_isolated": True},
        )
        self.assertEqual(safe_report.verdict, "PASS")
        self.assertTrue(verify_safe_launch_report(safe_report).passed)

        # build AnswerIsolationReport
        isolation_report = build_answer_isolation_report(
            attempt_id=ticket.attempt_id,
            receipt=receipt,
        )
        self.assertEqual(isolation_report.verdict, "PASS")
        self.assertTrue(verify_answer_isolation_report(isolation_report).passed)

        # reconcile
        reconcile_result = adapter.reconcile(ticket.attempt_id, ticket.fence_token)
        self.assertTrue(reconcile_result.passed)

        # build SolverCapabilityReport
        cap_report = build_solver_capability_report(
            harness_profile_hash=adapter.harness_profile.profile_hash,
            notool_policy_hash=adapter.notool_policy.policy_hash,
            safe_launch_report_hash=safe_report.report_hash,
            answer_isolation_report_hash=isolation_report.report_hash,
            dag_hash=_ZERO_HASH,
            probe_results=[],
            positive_evidence_refs=["safe_launch_pass", "answer_isolation_pass"],
            negative_evidence_refs=["direct_devin_bypass_blocked"],
            residual_risks=["live_solver_not_tested"],
            verifier_identity="sv1-integration-test",
            generated_at="2026-08-14T12:00:00+00:00",
        )
        self.assertEqual(cap_report["verdict"], "PASS")
        errors = verify_solver_capability_report(cap_report)
        self.assertEqual(errors, ())


if __name__ == "__main__":
    unittest.main()
