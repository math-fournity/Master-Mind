"""WP-QA1 Generated Bare Admission & Bakeoff-B 测试。

测试层级：Golden → Negative → Fault injection → Boundary
覆盖：
- Golden path: QuestionRelease → P3B bare submission via FakeHarnessAdapter →
  BareBaseline + BareQualificationResult
- Bakeoff-B blinded scoring with bare dimension
- Negative: Tell/Hint sneaked in, question modified, successful deleted,
  retry-until-fail, bare flows back to draft, calibration entering confirmatory
  Evidence, missing QuestionRelease, P5 claim in report, not problem-only
- Result retention tests (all results retained)
- Deterministic hash tests
- QA1 boundary tests (no P5 claim, no Tell/Hint, no confirmatory Evidence;
  allowed/forbidden output kinds)
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
    QA1_P3B_STATES,
    QA1_P3B_TRANSITIONS,
    QA1_P3B_TERMINAL_STATES,
    QA1_BARE_STATUSES,
    QA1_QUALIFICATION_STATUSES,
    QA1_BAKEOFF_B_METRICS,
    QA1_BAKEOFF_B_STATES,
    QA1_ALLOWED_OUTPUT_KINDS,
    QA1_FORBIDDEN_OUTPUT_KINDS,
    QA1_RETENTION_POLICIES,
    QA1_SIDE_EFFECT_KEYS,
    QA1_CHECK_IDS,
    QA1_CLAIMS,
    QA1_NONCLAIMS,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.authoring.question_release import (
    build_question_release,
    verify_question_release,
)
from seven_system.adapters.solver.harness_adapter import FakeHarnessAdapter
from seven_system.authoring.bare import (
    BareAttemptResult,
    BareBaseline,
    build_bare_baseline,
    verify_bare_baseline,
    ProblemQualification,
    BareQualificationResult,
    build_bare_qualification_result,
    verify_bare_qualification_result,
    P3BBareAdmission,
    RunArtifactBundle,
    check_no_tell_hint_in_submission,
    check_question_not_modified_after_bare,
    check_no_successful_question_deleted,
    check_no_retry_until_fail,
    check_no_bare_result_flowback_to_draft,
    BakeoffBPlan,
    build_bakeoff_b_plan,
    verify_bakeoff_b_plan,
    BakeoffBScoring,
    BakeoffBSubmission,
    BakeoffBScoringReport,
    verify_bakeoff_b_scoring_report,
    check_no_calibration_in_confirmatory_evidence,
    BareResultRetention,
    BareResultRetentionRecord,
    verify_bare_result_retention_record,
    BareCapabilityReport,
    build_bare_capability_report,
    verify_bare_capability_report,
)


# ─── helpers ───────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64


def _ref_hash(ref_id: str, sha: str = _ZERO_HASH) -> dict[str, str]:
    return {"ref_id": ref_id, "sha256": sha}


def _make_question_release(
    release_id: str = "qr-001",
    statement: str = "Find the minimum of x+y given xy=1.",
) -> Any:
    """构建一个合法的 QuestionRelease。"""
    return build_question_release(
        release_id=release_id,
        draft_ref_and_hash=_ref_hash("draft-001"),
        adversarial_review_ref_and_hash=_ref_hash("ar-001"),
        verification_dossier_ref_and_hash=_ref_hash("vd-001"),
        gate_decision_ref_and_hash=_ref_hash("gd-001"),
        public_statement=statement,
    )


def _make_bare_attempt_result(
    problem_ref_id: str = "qr-001",
    bare_status: str = "PASS",
    attempt_ref_id: str = "bare-001",
    terminal_reason: str = "COMPLETED",
) -> BareAttemptResult:
    return BareAttemptResult(
        problem_ref_id=problem_ref_id,
        bare_status=bare_status,
        attempt_ref_id=attempt_ref_id,
        terminal_reason=terminal_reason,
        tell_hint_included=False,
    )


# ─── 常量验证测试 ──────────────────────────────────────────────────────


class TestQA1Constants(unittest.TestCase):
    """验证所有 QA1 常量集合。"""

    def test_qa1_p3b_states_order(self):
        """P3B 状态机有序且完整。"""
        self.assertEqual(QA1_P3B_STATES, (
            "RELEASE_FROZEN",
            "BARE_SUBMITTED",
            "BARE_COLLECTED",
            "BASELINE_BUILT",
            "QUALIFICATION_JUDGED",
        ))

    def test_qa1_p3b_transitions(self):
        """P3B 状态转换合法。"""
        self.assertEqual(QA1_P3B_TRANSITIONS["RELEASE_FROZEN"], frozenset({"BARE_SUBMITTED"}))
        self.assertEqual(QA1_P3B_TRANSITIONS["QUALIFICATION_JUDGED"], frozenset())

    def test_qa1_p3b_terminal_states(self):
        """P3B 终态。"""
        self.assertEqual(QA1_P3B_TERMINAL_STATES, frozenset({"QUALIFICATION_JUDGED"}))

    def test_qa1_bare_statuses(self):
        """Bare attempt 结果状态全集。"""
        self.assertEqual(QA1_BARE_STATUSES, frozenset(
            {"PASS", "FAIL", "TIMEOUT", "QUARANTINE"}
        ))

    def test_qa1_qualification_statuses(self):
        """Bare qualification 状态全集。"""
        self.assertEqual(QA1_QUALIFICATION_STATUSES, frozenset(
            {"QUALIFIED", "NOT_QUALIFIED", "INCONCLUSIVE", "QUARANTINED"}
        ))

    def test_qa1_bakeoff_b_metrics(self):
        """Bakeoff-B 指标全集（含 bare 维度）。"""
        # Bakeoff-A 指标都在 Bakeoff-B 中
        for metric in ("math_correct", "mechanism_faithful", "orthogonal_distance",
                       "shortcut_leakage", "diversity", "human_revision_amount", "cost"):
            self.assertIn(metric, QA1_BAKEOFF_B_METRICS)
        # bare 维度指标
        for metric in ("bare_correct", "bare_pass", "bare_baseline",
                       "bare_qualification", "target_solver_result"):
            self.assertIn(metric, QA1_BAKEOFF_B_METRICS)

    def test_qa1_bakeoff_b_states(self):
        """Bakeoff-B 状态枚举。"""
        self.assertEqual(QA1_BAKEOFF_B_STATES, frozenset(
            {"PLANNED", "BLINDED", "SCORED", "COMPLETED", "BLOCKED"}
        ))

    def test_qa1_allowed_output_kinds(self):
        """QA1 允许的输出对象种类。"""
        for kind in ("BareBaseline", "BareQualificationResult", "BakeoffBPlan",
                     "BakeoffBScoringReport", "BareCapabilityReport",
                     "BareResultRetentionRecord", "RunArtifactBundle"):
            self.assertIn(kind, QA1_ALLOWED_OUTPUT_KINDS)

    def test_qa1_forbidden_output_kinds(self):
        """QA1 明确禁止输出的对象种类。"""
        for kind in ("EvidenceRecord", "ConfirmatoryEvidenceRecord",
                     "P5ClaimRecord", "RunAudit"):
            self.assertIn(kind, QA1_FORBIDDEN_OUTPUT_KINDS)

    def test_qa1_allowed_and_forbidden_disjoint(self):
        """allowed 和 forbidden 不重叠。"""
        overlap = set(QA1_ALLOWED_OUTPUT_KINDS) & set(QA1_FORBIDDEN_OUTPUT_KINDS)
        self.assertEqual(overlap, set())

    def test_qa1_retention_policies(self):
        """Bare result retention 策略全集。"""
        self.assertEqual(QA1_RETENTION_POLICIES, frozenset(
            {
                "RETAIN_ALL_RESULTS",
                "NO_QUESTION_MODIFICATION",
                "NO_SUCCESSFUL_DELETION",
                "NO_RETRY_UNTIL_FAIL",
                "NO_DRAFT_FLOWBACK",
            }
        ))

    def test_qa1_side_effect_keys(self):
        """QA1 side-effect 键全集。"""
        self.assertEqual(QA1_SIDE_EFFECT_KEYS, (
            "database_writes",
            "redis_writes",
            "d_volume_writes",
            "solver_launches",
            "model_live_calls",
            "human_gate_commits",
        ))

    def test_qa1_check_ids(self):
        """QA1 check IDs 非空。"""
        self.assertTrue(len(QA1_CHECK_IDS) > 0)
        for check_id in QA1_CHECK_IDS:
            self.assertTrue(check_id.startswith("qa1."))

    def test_qa1_claims(self):
        """QA1 claims 非空且不含 P5 claim。"""
        self.assertTrue(len(QA1_CLAIMS) > 0)
        for claim in QA1_CLAIMS:
            self.assertNotIn("p5_claim", claim.lower())

    def test_qa1_nonclaims(self):
        """QA1 nonclaims 包含 no_p5_claim。"""
        self.assertIn("no_p5_claim", QA1_NONCLAIMS)
        self.assertIn("no_tell_hint_in_bare", QA1_NONCLAIMS)
        self.assertIn("no_confirmatory_evidence", QA1_NONCLAIMS)

    def test_qa1_error_codes_exist(self):
        """QA1 错误码都在枚举中。"""
        for code_name in (
            "QA1_TELL_HINT_SNEAKED_INTO_BARE",
            "QA1_QUESTION_MODIFIED_AFTER_BARE",
            "QA1_SUCCESSFUL_QUESTION_DELETED",
            "QA1_RETRY_UNTIL_FAIL",
            "QA1_BARE_RESULT_FLOWS_BACK_TO_DRAFT",
            "QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE",
            "QA1_QUESTION_RELEASE_REF_MISSING",
            "QA1_P5_CLAIM_IN_BARE_REPORT",
            "QA1_BARE_NOT_PROBLEM_ONLY",
            "QA1_BARELINE_HASH_MISMATCH",
            "QA1_QUALIFICATION_RESULT_HASH_MISMATCH",
            "QA1_BAKEOFF_B_PLAN_NOT_FROZEN",
            "QA1_BAKEOFF_B_NOT_BLINDED",
            "QA1_BARE_RESULT_NOT_RETAINED",
        ):
            self.assertTrue(hasattr(EC, code_name), f"missing error code: {code_name}")


# ─── BareBaseline 测试 ─────────────────────────────────────────────────


class TestBareBaseline(unittest.TestCase):
    """BareBaseline 构建和验证测试。"""

    def test_build_and_verify_bare_baseline_golden(self):
        """Golden path: 构建并验证 BareBaseline。"""
        results = [
            _make_bare_attempt_result("qr-001", "PASS", "bare-001", "COMPLETED"),
            _make_bare_attempt_result("qr-002", "FAIL", "bare-002", "FAILED_PERMANENT"),
        ]
        baseline = build_bare_baseline(
            baseline_id="bb-001",
            question_release_ref_id="qr-001",
            question_release_sha256=_ZERO_HASH,
            bare_attempt_results=results,
        )
        result = verify_bare_baseline(baseline)
        self.assertTrue(result.passed, f"verification failed: {result.details}")
        self.assertEqual(baseline.problem_only, True)
        self.assertEqual(baseline.no_tell_hint, True)
        self.assertEqual(baseline.all_results_retained, True)
        self.assertEqual(len(baseline.bare_attempt_results), 2)

    def test_bare_baseline_missing_question_release_ref(self):
        """Blocker: 缺 QuestionRelease ref → FAIL。"""
        baseline = BareBaseline(
            baseline_id="bb-001",
            question_release_ref_and_hash={},
            problem_only=True,
            no_tell_hint=True,
            all_results_retained=True,
            bare_attempt_results=[],
            baseline_hash="0" * 64,
        )
        result = verify_bare_baseline(baseline.to_dict())
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_QUESTION_RELEASE_REF_MISSING, result.error_codes)

    def test_bare_baseline_not_problem_only(self):
        """Blocker: bare 不是 problem-only → FAIL。"""
        results = [_make_bare_attempt_result()]
        baseline = build_bare_baseline(
            baseline_id="bb-001",
            question_release_ref_id="qr-001",
            question_release_sha256=_ZERO_HASH,
            bare_attempt_results=results,
        )
        d = baseline.to_dict()
        d["problem_only"] = False
        d["baseline_hash"] = _ZERO_HASH  # will fail hash too, but we check the specific error
        result = verify_bare_baseline(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BARE_NOT_PROBLEM_ONLY, result.error_codes)

    def test_bare_baseline_tell_hint_included(self):
        """Blocker: bare result 包含 Tell/Hint → FAIL。"""
        bad_result = BareAttemptResult(
            problem_ref_id="qr-001",
            bare_status="PASS",
            attempt_ref_id="bare-001",
            terminal_reason="COMPLETED",
            tell_hint_included=True,  # BLOCKER
        )
        baseline = build_bare_baseline(
            baseline_id="bb-001",
            question_release_ref_id="qr-001",
            question_release_sha256=_ZERO_HASH,
            bare_attempt_results=[bad_result],
        )
        d = baseline.to_dict()
        result = verify_bare_baseline(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE, result.error_codes)

    def test_bare_baseline_invalid_bare_status(self):
        """Blocker: 无效 bare_status → FAIL。"""
        bad_result = BareAttemptResult(
            problem_ref_id="qr-001",
            bare_status="INVALID",
            attempt_ref_id="bare-001",
            terminal_reason="COMPLETED",
            tell_hint_included=False,
        )
        baseline = build_bare_baseline(
            baseline_id="bb-001",
            question_release_ref_id="qr-001",
            question_release_sha256=_ZERO_HASH,
            bare_attempt_results=[bad_result],
        )
        d = baseline.to_dict()
        result = verify_bare_baseline(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BARE_STATUS_INVALID, result.error_codes)

    def test_bare_baseline_all_results_not_retained(self):
        """Blocker: all_results_retained == False → FAIL。"""
        results = [_make_bare_attempt_result()]
        baseline = build_bare_baseline(
            baseline_id="bb-001",
            question_release_ref_id="qr-001",
            question_release_sha256=_ZERO_HASH,
            bare_attempt_results=results,
        )
        d = baseline.to_dict()
        d["all_results_retained"] = False
        result = verify_bare_baseline(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BARE_RESULT_NOT_RETAINED, result.error_codes)

    def test_bare_baseline_hash_deterministic(self):
        """确定性 hash：相同输入产生相同 hash。"""
        results = [_make_bare_attempt_result()]
        b1 = build_bare_baseline(
            baseline_id="bb-001",
            question_release_ref_id="qr-001",
            question_release_sha256=_ZERO_HASH,
            bare_attempt_results=results,
        )
        b2 = build_bare_baseline(
            baseline_id="bb-001",
            question_release_ref_id="qr-001",
            question_release_sha256=_ZERO_HASH,
            bare_attempt_results=results,
        )
        self.assertEqual(b1.baseline_hash, b2.baseline_hash)

    def test_bare_baseline_hash_tampered(self):
        """Blocker: baseline_hash 被篡改 → FAIL。"""
        results = [_make_bare_attempt_result()]
        baseline = build_bare_baseline(
            baseline_id="bb-001",
            question_release_ref_id="qr-001",
            question_release_sha256=_ZERO_HASH,
            bare_attempt_results=results,
        )
        d = baseline.to_dict()
        d["baseline_hash"] = "1" * 64
        result = verify_bare_baseline(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BARELINE_HASH_MISMATCH, result.error_codes)


# ─── BareQualificationResult 测试 ──────────────────────────────────────


class TestBareQualificationResult(unittest.TestCase):
    """BareQualificationResult 构建和验证测试。"""

    def test_build_and_verify_qualification_golden(self):
        """Golden path: 构建并验证 BareQualificationResult。"""
        quals = [
            ProblemQualification("qr-001", "QUALIFIED", "PASS", True),
            ProblemQualification("qr-002", "NOT_QUALIFIED", "FAIL", True),
        ]
        result = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=quals,
        )
        v = verify_bare_qualification_result(result)
        self.assertTrue(v.passed, f"verification failed: {v.details}")
        self.assertEqual(result.no_p5_claim, True)
        self.assertEqual(result.no_draft_flowback, True)

    def test_qualification_missing_baseline_ref(self):
        """Blocker: 缺 BareBaseline ref → FAIL。"""
        quals = [ProblemQualification("qr-001", "QUALIFIED", "PASS", True)]
        result = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=quals,
        )
        d = result.to_dict()
        d["bare_baseline_ref_and_hash"] = {}
        v = verify_bare_qualification_result(d)
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_BARELINE_REF_MISSING, v.error_codes)

    def test_qualification_p5_claim(self):
        """Blocker: no_p5_claim == False → FAIL。"""
        quals = [ProblemQualification("qr-001", "QUALIFIED", "PASS", True)]
        result = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=quals,
        )
        d = result.to_dict()
        d["no_p5_claim"] = False
        v = verify_bare_qualification_result(d)
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_P5_CLAIM_IN_BARE_REPORT, v.error_codes)

    def test_qualification_draft_flowback(self):
        """Blocker: no_draft_flowback == False → FAIL。"""
        quals = [ProblemQualification("qr-001", "QUALIFIED", "PASS", True)]
        result = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=quals,
        )
        d = result.to_dict()
        d["no_draft_flowback"] = False
        v = verify_bare_qualification_result(d)
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_BARE_RESULT_FLOWS_BACK_TO_DRAFT, v.error_codes)

    def test_qualification_invalid_status(self):
        """Blocker: 无效 qualification_status → FAIL。"""
        bad_qual = ProblemQualification("qr-001", "INVALID", "PASS", True)
        result = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=[bad_qual],
        )
        d = result.to_dict()
        v = verify_bare_qualification_result(d)
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_QUALIFICATION_STATUS_INVALID, v.error_codes)

    def test_qualification_problem_not_p5_claim(self):
        """Blocker: problem qualification not_p5_claim == False → FAIL。"""
        bad_qual = ProblemQualification("qr-001", "QUALIFIED", "PASS", False)
        result = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=[bad_qual],
        )
        d = result.to_dict()
        v = verify_bare_qualification_result(d)
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_P5_CLAIM_IN_BARE_REPORT, v.error_codes)

    def test_qualification_hash_deterministic(self):
        """确定性 hash。"""
        quals = [ProblemQualification("qr-001", "QUALIFIED", "PASS", True)]
        r1 = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=quals,
        )
        r2 = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=quals,
        )
        self.assertEqual(r1.result_hash, r2.result_hash)

    def test_qualification_hash_tampered(self):
        """Blocker: result_hash 被篡改 → FAIL。"""
        quals = [ProblemQualification("qr-001", "QUALIFIED", "PASS", True)]
        result = build_bare_qualification_result(
            result_id="bqr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
            problem_qualifications=quals,
        )
        d = result.to_dict()
        d["result_hash"] = "1" * 64
        v = verify_bare_qualification_result(d)
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_QUALIFICATION_RESULT_HASH_MISMATCH, v.error_codes)


# ─── P3BBareAdmission Golden Path 测试 ─────────────────────────────────


class TestP3BBareAdmissionGolden(unittest.TestCase):
    """P3B bare admission pipeline golden path 测试。"""

    def test_p3b_golden_path(self):
        """Golden path: QuestionRelease → P3B → BareBaseline + BareQualificationResult。"""
        release = _make_question_release()
        adapter = FakeHarnessAdapter()
        pipeline = P3BBareAdmission(adapter)

        bundle, result = pipeline.admit(
            question_release=release,
            baseline_id="bb-001",
            result_id="bqr-001",
            bundle_id="rab-001",
        )
        self.assertTrue(result.passed, f"pipeline failed: {result.details}")
        self.assertIsNotNone(bundle)
        self.assertEqual(bundle.problem_only, True)
        self.assertEqual(bundle.no_tell_hint, True)
        self.assertEqual(pipeline.state, "QUALIFICATION_JUDGED")

        # Verify baseline
        baseline = pipeline.baseline
        self.assertIsNotNone(baseline)
        bv = verify_bare_baseline(baseline)
        self.assertTrue(bv.passed, f"baseline verification failed: {bv.details}")

        # Verify qualification
        qual = pipeline.qualification
        self.assertIsNotNone(qual)
        qv = verify_bare_qualification_result(qual)
        self.assertTrue(qv.passed, f"qualification verification failed: {qv.details}")

        # Bare results retained (success)
        self.assertEqual(len(pipeline.bare_results), 1)
        self.assertEqual(pipeline.bare_results[0].bare_status, "PASS")

    def test_p3b_state_transitions(self):
        """P3B 状态机正确转换。"""
        release = _make_question_release()
        adapter = FakeHarnessAdapter()
        pipeline = P3BBareAdmission(adapter)
        self.assertEqual(pipeline.state, "RELEASE_FROZEN")

        pipeline.admit(
            question_release=release,
            baseline_id="bb-001",
            result_id="bqr-001",
            bundle_id="rab-001",
        )
        self.assertEqual(pipeline.state, "QUALIFICATION_JUDGED")

    def test_p3b_run_artifact_bundle(self):
        """RunArtifactBundle 包含所有资产引用。"""
        release = _make_question_release()
        adapter = FakeHarnessAdapter()
        pipeline = P3BBareAdmission(adapter)

        bundle, result = pipeline.admit(
            question_release=release,
            baseline_id="bb-001",
            result_id="bqr-001",
            bundle_id="rab-001",
        )
        self.assertTrue(result.passed)
        self.assertEqual(bundle.bundle_id, "rab-001")
        self.assertEqual(
            bundle.question_release_ref_and_hash["ref_id"], "qr-001"
        )
        self.assertEqual(
            bundle.bare_baseline_ref_and_hash["ref_id"], "bb-001"
        )
        self.assertEqual(
            bundle.qualification_result_ref_and_hash["ref_id"], "bqr-001"
        )
        self.assertTrue(len(bundle.attempt_receipt_refs) > 0)


# ─── P3B Blocker 测试 ──────────────────────────────────────────────────


class TestP3BBlockers(unittest.TestCase):
    """P3B bare admission blocker 测试。"""

    def test_blocker_tell_hint_sneaked_into_bare(self):
        """Blocker: Tell/Hint sneaked into bare submission → FAIL。"""
        release = _make_question_release()
        adapter = FakeHarnessAdapter()
        pipeline = P3BBareAdmission(adapter)

        bundle, result = pipeline.admit(
            question_release=release,
            baseline_id="bb-001",
            result_id="bqr-001",
            bundle_id="rab-001",
            bare_submission_payload={"tell": "use AM-GM inequality"},
        )
        self.assertIsNone(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE, result.error_codes)

    def test_blocker_hint_keyword_in_submission(self):
        """Blocker: hint 关键词在 submission 中 → FAIL。"""
        release = _make_question_release()
        adapter = FakeHarnessAdapter()
        pipeline = P3BBareAdmission(adapter)

        bundle, result = pipeline.admit(
            question_release=release,
            baseline_id="bb-001",
            result_id="bqr-001",
            bundle_id="rab-001",
            bare_submission_payload={"hint": "try substitution"},
        )
        self.assertIsNone(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE, result.error_codes)

    def test_blocker_missing_question_release_ref(self):
        """Blocker: 缺 QuestionRelease ref → FAIL。"""
        # Create a release with empty content_hash
        release = _make_question_release()
        # Manually create a broken release
        from seven_system.authoring.question_release import QuestionRelease
        broken = QuestionRelease(
            release_id="",
            draft_ref_and_hash=_ref_hash("draft-001"),
            adversarial_review_ref_and_hash=_ref_hash("ar-001"),
            verification_dossier_ref_and_hash=_ref_hash("vd-001"),
            gate_decision_ref_and_hash=_ref_hash("gd-001"),
            gate_type="G-Q-RELEASE",
            public_statement="test",
            immutable=True,
            content_hash="",
        )
        adapter = FakeHarnessAdapter()
        pipeline = P3BBareAdmission(adapter)

        bundle, result = pipeline.admit(
            question_release=broken,
            baseline_id="bb-001",
            result_id="bqr-001",
            bundle_id="rab-001",
        )
        self.assertIsNone(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_QUESTION_RELEASE_REF_MISSING, result.error_codes)

    def test_check_no_tell_hint_in_submission_clean(self):
        """check_no_tell_hint_in_submission: 干净 submission → PASS。"""
        submission = {"public_statement": "Find the minimum of x+y."}
        result = check_no_tell_hint_in_submission(submission)
        self.assertTrue(result.passed)

    def test_check_no_tell_hint_in_submission_with_tell(self):
        """check_no_tell_hint_in_submission: 含 tell → FAIL。"""
        submission = {"public_statement": "Find the minimum.", "tell": "use AM-GM"}
        result = check_no_tell_hint_in_submission(submission)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE, result.error_codes)

    def test_check_question_not_modified_after_bare_clean(self):
        """check_question_not_modified_after_bare: 未修改 → PASS。"""
        result = check_question_not_modified_after_bare(_ZERO_HASH, _ZERO_HASH)
        self.assertTrue(result.passed)

    def test_check_question_not_modified_after_bare_modified(self):
        """check_question_not_modified_after_bare: 已修改 → FAIL。"""
        result = check_question_not_modified_after_bare(_ZERO_HASH, "1" * 64)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_QUESTION_MODIFIED_AFTER_BARE, result.error_codes)

    def test_check_no_successful_question_deleted_clean(self):
        """check_no_successful_question_deleted: 未删除 → PASS。"""
        results = [_make_bare_attempt_result("qr-001", "PASS")]
        r = check_no_successful_question_deleted(
            ["qr-001", "qr-002"], ["qr-001", "qr-002"], results
        )
        self.assertTrue(r.passed)

    def test_check_no_successful_question_deleted_blocked(self):
        """Blocker: 成功题被删除 → FAIL。"""
        results = [_make_bare_attempt_result("qr-001", "PASS")]
        r = check_no_successful_question_deleted(
            ["qr-001", "qr-002"], ["qr-002"], results  # qr-001 (PASS) deleted
        )
        self.assertFalse(r.passed)
        self.assertIn(EC.QA1_SUCCESSFUL_QUESTION_DELETED, r.error_codes)

    def test_check_no_retry_until_fail_clean(self):
        """check_no_retry_until_fail: 无重试 → PASS。"""
        r = check_no_retry_until_fail({"qr-001": 1, "qr-002": 1})
        self.assertTrue(r.passed)

    def test_check_no_retry_until_fail_blocked(self):
        """Blocker: retry-until-fail → FAIL。"""
        r = check_no_retry_until_fail({"qr-001": 3, "qr-002": 1})
        self.assertFalse(r.passed)
        self.assertIn(EC.QA1_RETRY_UNTIL_FAIL, r.error_codes)

    def test_check_no_bare_result_flowback_to_draft_clean(self):
        """check_no_bare_result_flowback_to_draft: 未回流 → PASS。"""
        r = check_no_bare_result_flowback_to_draft(_ZERO_HASH, _ZERO_HASH)
        self.assertTrue(r.passed)

    def test_check_no_bare_result_flowback_to_draft_blocked(self):
        """Blocker: bare 结果回流改 draft → FAIL。"""
        r = check_no_bare_result_flowback_to_draft(_ZERO_HASH, "1" * 64)
        self.assertFalse(r.passed)
        self.assertIn(EC.QA1_BARE_RESULT_FLOWS_BACK_TO_DRAFT, r.error_codes)


# ─── BakeoffBPlan 测试 ─────────────────────────────────────────────────


class TestBakeoffBPlan(unittest.TestCase):
    """BakeoffBPlan 构建和验证测试。"""

    def test_build_and_verify_plan_golden(self):
        """Golden path: 构建并验证 BakeoffBPlan。"""
        plan = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001"), _ref_hash("qr-002")],
            profile_labels=["devin_glm_5_2_high", "codex_candidate"],
            metrics=["math_correct", "bare_correct", "bare_pass"],
            stop_conditions={"max_cost_exceeded": True, "all_profiles_evaluated": True},
        )
        result = verify_bakeoff_b_plan(plan)
        self.assertTrue(result.passed, f"plan verification failed: {result.details}")
        self.assertEqual(plan.frozen, True)
        self.assertEqual(plan.no_calibration_in_confirmatory_evidence, True)
        self.assertEqual(plan.per_role_defaults, True)

    def test_plan_not_frozen(self):
        """Blocker: plan 未冻结 → FAIL。"""
        plan = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001")],
            profile_labels=["devin_glm_5_2_high"],
            metrics=["math_correct"],
        )
        d = plan.to_dict()
        d["frozen"] = False
        result = verify_bakeoff_b_plan(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BAKEOFF_B_PLAN_NOT_FROZEN, result.error_codes)

    def test_plan_missing_bakeoff_a_ref(self):
        """Blocker: 缺 Bakeoff-A ref → FAIL。"""
        plan = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001")],
            profile_labels=["devin_glm_5_2_high"],
            metrics=["math_correct"],
        )
        d = plan.to_dict()
        d["bakeoff_a_ref_and_hash"] = {}
        result = verify_bakeoff_b_plan(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BAKEOFF_A_REF_MISSING, result.error_codes)

    def test_plan_calibration_in_confirmatory_evidence(self):
        """Blocker: calibration 进入 confirmatory Evidence → FAIL。"""
        plan = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001")],
            profile_labels=["devin_glm_5_2_high"],
            metrics=["math_correct"],
        )
        d = plan.to_dict()
        d["no_calibration_in_confirmatory_evidence"] = False
        result = verify_bakeoff_b_plan(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE, result.error_codes)

    def test_plan_missing_question_release_refs(self):
        """Blocker: 缺 question_release_refs → FAIL。"""
        plan = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001")],
            profile_labels=["devin_glm_5_2_high"],
            metrics=["math_correct"],
        )
        d = plan.to_dict()
        d["question_release_refs"] = []
        result = verify_bakeoff_b_plan(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_QUESTION_RELEASE_REF_MISSING, result.error_codes)

    def test_plan_invalid_metric(self):
        """Blocker: 无效 metric → FAIL。"""
        plan = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001")],
            profile_labels=["devin_glm_5_2_high"],
            metrics=["invalid_metric"],
        )
        d = plan.to_dict()
        result = verify_bakeoff_b_plan(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED, result.error_codes)

    def test_plan_hash_deterministic(self):
        """确定性 hash。"""
        p1 = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001")],
            profile_labels=["devin_glm_5_2_high"],
            metrics=["math_correct"],
        )
        p2 = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001")],
            profile_labels=["devin_glm_5_2_high"],
            metrics=["math_correct"],
        )
        self.assertEqual(p1.plan_hash, p2.plan_hash)

    def test_plan_hash_tampered(self):
        """Blocker: plan_hash 被篡改 → FAIL。"""
        plan = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[_ref_hash("qr-001")],
            profile_labels=["devin_glm_5_2_high"],
            metrics=["math_correct"],
        )
        d = plan.to_dict()
        d["plan_hash"] = "1" * 64
        result = verify_bakeoff_b_plan(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BAKEOFF_B_PLAN_HASH_MISMATCH, result.error_codes)


# ─── BakeoffBScoring 测试 ──────────────────────────────────────────────


class TestBakeoffBScoring(unittest.TestCase):
    """BakeoffBScoring 盲评评分测试。"""

    def test_score_and_build_golden(self):
        """Golden path: Bakeoff-B 评分含 bare 维度。"""
        submissions = [
            BakeoffBSubmission(
                blinded_label="devin_glm_5_2_high",
                draft_ref_and_hash=_ref_hash("draft-001"),
                bare_baseline_ref_and_hash=_ref_hash("bb-001"),
                scores={
                    "math_correct": 0.9,
                    "bare_correct": 0.7,
                    "bare_pass": 0.8,
                },
            ),
            BakeoffBSubmission(
                blinded_label="codex_candidate",
                draft_ref_and_hash=_ref_hash("draft-002"),
                bare_baseline_ref_and_hash=_ref_hash("bb-002"),
                scores={
                    "math_correct": 0.85,
                    "bare_correct": 0.6,
                    "bare_pass": 0.75,
                },
            ),
        ]
        scorer = BakeoffBScoring()
        plan_ref = _ref_hash("bbp-001")
        result = scorer.score(
            bakeoff_b_plan_ref_and_hash=plan_ref,
            submissions=submissions,
        )
        self.assertTrue(result.passed, f"scoring failed: {result.details}")

        report = scorer.build_report(
            report_id="bbsr-001",
            bakeoff_b_plan_ref_and_hash=plan_ref,
            submissions=submissions,
        )
        rv = verify_bakeoff_b_scoring_report(report)
        self.assertTrue(rv.passed, f"report verification failed: {rv.details}")
        self.assertEqual(report.author_identity_hidden, True)
        self.assertEqual(report.has_bare_dimension, True)
        self.assertEqual(report.no_calibration_in_confirmatory_evidence, True)

    def test_score_no_bare_dimension(self):
        """Blocker: 无 bare 维度指标 → FAIL。"""
        submissions = [
            BakeoffBSubmission(
                blinded_label="devin_glm_5_2_high",
                draft_ref_and_hash=_ref_hash("draft-001"),
                bare_baseline_ref_and_hash=_ref_hash("bb-001"),
                scores={"math_correct": 0.9},  # no bare metrics
            ),
        ]
        scorer = BakeoffBScoring()
        result = scorer.score(
            bakeoff_b_plan_ref_and_hash=_ref_hash("bbp-001"),
            submissions=submissions,
        )
        self.assertFalse(result.passed)

    def test_score_author_identity_leaked(self):
        """Blocker: 作者身份泄漏 → FAIL。"""
        submissions = [
            BakeoffBSubmission(
                blinded_label="devin_real_name",  # not in allowed labels
                draft_ref_and_hash=_ref_hash("draft-001"),
                bare_baseline_ref_and_hash=_ref_hash("bb-001"),
                scores={"math_correct": 0.9, "bare_correct": 0.7},
            ),
        ]
        scorer = BakeoffBScoring()
        result = scorer.score(
            bakeoff_b_plan_ref_and_hash=_ref_hash("bbp-001"),
            submissions=submissions,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.QA_AUTHOR_IDENTITY_LEAKED, result.error_codes)

    def test_score_invalid_metric(self):
        """Blocker: 无效 metric → FAIL。"""
        submissions = [
            BakeoffBSubmission(
                blinded_label="devin_glm_5_2_high",
                draft_ref_and_hash=_ref_hash("draft-001"),
                bare_baseline_ref_and_hash=_ref_hash("bb-001"),
                scores={"invalid_metric": 0.5, "bare_correct": 0.7},
            ),
        ]
        scorer = BakeoffBScoring()
        result = scorer.score(
            bakeoff_b_plan_ref_and_hash=_ref_hash("bbp-001"),
            submissions=submissions,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED, result.error_codes)

    def test_report_not_blinded(self):
        """Blocker: 报告不是 blinded → FAIL。"""
        submissions = [
            BakeoffBSubmission(
                blinded_label="devin_glm_5_2_high",
                draft_ref_and_hash=_ref_hash("draft-001"),
                bare_baseline_ref_and_hash=_ref_hash("bb-001"),
                scores={"math_correct": 0.9, "bare_correct": 0.7},
            ),
        ]
        scorer = BakeoffBScoring()
        report = scorer.build_report(
            report_id="bbsr-001",
            bakeoff_b_plan_ref_and_hash=_ref_hash("bbp-001"),
            submissions=submissions,
        )
        d = report.to_dict()
        d["author_identity_hidden"] = False
        result = verify_bakeoff_b_scoring_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BAKEOFF_B_NOT_BLINDED, result.error_codes)

    def test_report_calibration_in_confirmatory_evidence(self):
        """Blocker: calibration 进入 confirmatory Evidence → FAIL。"""
        submissions = [
            BakeoffBSubmission(
                blinded_label="devin_glm_5_2_high",
                draft_ref_and_hash=_ref_hash("draft-001"),
                bare_baseline_ref_and_hash=_ref_hash("bb-001"),
                scores={"math_correct": 0.9, "bare_correct": 0.7},
            ),
        ]
        scorer = BakeoffBScoring()
        report = scorer.build_report(
            report_id="bbsr-001",
            bakeoff_b_plan_ref_and_hash=_ref_hash("bbp-001"),
            submissions=submissions,
        )
        d = report.to_dict()
        d["no_calibration_in_confirmatory_evidence"] = False
        result = verify_bakeoff_b_scoring_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE, result.error_codes)

    def test_report_hash_deterministic(self):
        """确定性 hash。"""
        submissions = [
            BakeoffBSubmission(
                blinded_label="devin_glm_5_2_high",
                draft_ref_and_hash=_ref_hash("draft-001"),
                bare_baseline_ref_and_hash=_ref_hash("bb-001"),
                scores={"math_correct": 0.9, "bare_correct": 0.7},
            ),
        ]
        scorer = BakeoffBScoring()
        r1 = scorer.build_report(
            report_id="bbsr-001",
            bakeoff_b_plan_ref_and_hash=_ref_hash("bbp-001"),
            submissions=submissions,
        )
        r2 = scorer.build_report(
            report_id="bbsr-001",
            bakeoff_b_plan_ref_and_hash=_ref_hash("bbp-001"),
            submissions=submissions,
        )
        self.assertEqual(r1.report_hash, r2.report_hash)

    def test_check_no_calibration_in_confirmatory_evidence_clean(self):
        """check_no_calibration_in_confirmatory_evidence: 无重叠 → PASS。"""
        result = check_no_calibration_in_confirmatory_evidence(
            ["calib-001", "calib-002"],
            ["evidence-001", "evidence-002"],
        )
        self.assertTrue(result.passed)

    def test_check_no_calibration_in_confirmatory_evidence_blocked(self):
        """Blocker: calibration 进入 confirmatory Evidence → FAIL。"""
        result = check_no_calibration_in_confirmatory_evidence(
            ["calib-001", "calib-002"],
            ["evidence-001", "calib-001"],  # overlap
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE, result.error_codes)


# ─── BareResultRetention 测试 ──────────────────────────────────────────


class TestBareResultRetention(unittest.TestCase):
    """BareResultRetention 结果保留测试。"""

    def test_retention_all_results_retained(self):
        """所有结果（成功和失败）都保留。"""
        retention = BareResultRetention()
        results = [
            _make_bare_attempt_result("qr-001", "PASS", "bare-001", "COMPLETED"),
            _make_bare_attempt_result("qr-002", "FAIL", "bare-002", "FAILED_PERMANENT"),
            _make_bare_attempt_result("qr-003", "TIMEOUT", "bare-003", "TIMED_OUT"),
            _make_bare_attempt_result("qr-004", "QUARANTINE", "bare-004", "QUARANTINED"),
        ]
        r = retention.register_results(results)
        self.assertTrue(r.passed)
        v = retention.verify_retention()
        self.assertTrue(v.passed, f"retention verification failed: {v.details}")
        self.assertEqual(len(retention.results), 4)

    def test_retention_question_modified_after_bare(self):
        """Blocker: bare 后改题 → FAIL。"""
        retention = BareResultRetention()
        results = [_make_bare_attempt_result("qr-001", "PASS")]
        retention.register_results(results)
        retention.set_question_hash_before(_ZERO_HASH)
        retention.set_question_hash_after("1" * 64)
        v = retention.verify_retention()
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_QUESTION_MODIFIED_AFTER_BARE, v.error_codes)

    def test_retention_successful_question_deleted(self):
        """Blocker: 成功题被删除 → FAIL。"""
        retention = BareResultRetention()
        results = [_make_bare_attempt_result("qr-001", "PASS")]
        retention.register_results(results)
        retention.set_original_problem_refs(["qr-001", "qr-002"])
        retention.set_current_problem_refs(["qr-002"])  # qr-001 (PASS) deleted
        v = retention.verify_retention()
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_SUCCESSFUL_QUESTION_DELETED, v.error_codes)

    def test_retention_retry_until_fail(self):
        """Blocker: retry-until-fail → FAIL。"""
        retention = BareResultRetention()
        # Same problem attempted 3 times
        results = [
            _make_bare_attempt_result("qr-001", "PASS", "bare-001", "COMPLETED"),
            _make_bare_attempt_result("qr-001", "FAIL", "bare-002", "FAILED_PERMANENT"),
            _make_bare_attempt_result("qr-001", "FAIL", "bare-003", "FAILED_PERMANENT"),
        ]
        retention.register_results(results)
        v = retention.verify_retention()
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_RETRY_UNTIL_FAIL, v.error_codes)

    def test_retention_bare_result_flowback_to_draft(self):
        """Blocker: bare 结果回流改 draft → FAIL。"""
        retention = BareResultRetention()
        results = [_make_bare_attempt_result("qr-001", "PASS")]
        retention.register_results(results)
        retention.set_draft_hash_before(_ZERO_HASH)
        retention.set_draft_hash_after("1" * 64)
        v = retention.verify_retention()
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_BARE_RESULT_FLOWS_BACK_TO_DRAFT, v.error_codes)

    def test_retention_build_record(self):
        """构建 BareResultRetentionRecord。"""
        retention = BareResultRetention()
        results = [
            _make_bare_attempt_result("qr-001", "PASS"),
            _make_bare_attempt_result("qr-002", "FAIL"),
        ]
        retention.register_results(results)
        record = retention.build_record(
            record_id="brrr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
        )
        v = verify_bare_result_retention_record(record)
        self.assertTrue(v.passed, f"record verification failed: {v.details}")
        self.assertEqual(record.total_results, 2)
        self.assertEqual(record.pass_count, 1)
        self.assertEqual(record.fail_count, 1)
        self.assertEqual(record.all_retained, True)

    def test_retention_record_not_all_retained(self):
        """Blocker: all_retained == False → FAIL。"""
        retention = BareResultRetention()
        results = [_make_bare_attempt_result("qr-001", "PASS")]
        retention.register_results(results)
        record = retention.build_record(
            record_id="brrr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
        )
        d = record.to_dict()
        d["all_retained"] = False
        v = verify_bare_result_retention_record(d)
        self.assertFalse(v.passed)
        self.assertIn(EC.QA1_BARE_RESULT_NOT_RETAINED, v.error_codes)

    def test_retention_record_hash_deterministic(self):
        """确定性 hash。"""
        retention = BareResultRetention()
        results = [_make_bare_attempt_result("qr-001", "PASS")]
        retention.register_results(results)
        r1 = retention.build_record(
            record_id="brrr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
        )
        r2 = retention.build_record(
            record_id="brrr-001",
            bare_baseline_ref_id="bb-001",
            bare_baseline_sha256=_ZERO_HASH,
        )
        self.assertEqual(r1.record_hash, r2.record_hash)


# ─── BareCapabilityReport 测试 ─────────────────────────────────────────


class TestBareCapabilityReport(unittest.TestCase):
    """BareCapabilityReport 能力报告测试。"""

    def test_build_and_verify_report_golden(self):
        """Golden path: 构建并验证 BareCapabilityReport。"""
        report = build_bare_capability_report(report_id="bcr-001")
        result = verify_bare_capability_report(report)
        self.assertTrue(result.passed, f"report verification failed: {result.details}")
        self.assertEqual(report.no_p5_claim, True)
        self.assertEqual(report.no_tell_hint, True)
        self.assertEqual(report.no_confirmatory_evidence, True)

    def test_report_p5_claim(self):
        """Blocker: no_p5_claim == False → FAIL。"""
        report = build_bare_capability_report(report_id="bcr-001")
        d = report.to_dict()
        d["no_p5_claim"] = False
        result = verify_bare_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_P5_CLAIM_IN_BARE_REPORT, result.error_codes)

    def test_report_tell_hint(self):
        """Blocker: no_tell_hint == False → FAIL。"""
        report = build_bare_capability_report(report_id="bcr-001")
        d = report.to_dict()
        d["no_tell_hint"] = False
        result = verify_bare_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE, result.error_codes)

    def test_report_confirmatory_evidence(self):
        """Blocker: no_confirmatory_evidence == False → FAIL。"""
        report = build_bare_capability_report(report_id="bcr-001")
        d = report.to_dict()
        d["no_confirmatory_evidence"] = False
        result = verify_bare_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE, result.error_codes)

    def test_report_side_effects_nonzero(self):
        """Blocker: side_effect_counters 非零 → FAIL。"""
        report = build_bare_capability_report(report_id="bcr-001")
        d = report.to_dict()
        d["side_effect_counters"]["database_writes"] = 1
        result = verify_bare_capability_report(d)
        self.assertFalse(result.passed)

    def test_report_allowed_output_kinds_mismatch(self):
        """Blocker: allowed_output_kinds 不匹配 → FAIL。"""
        report = build_bare_capability_report(report_id="bcr-001")
        d = report.to_dict()
        d["allowed_output_kinds"] = ["WrongKind"]
        result = verify_bare_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_OUTPUT_KIND_FORBIDDEN, result.error_codes)

    def test_report_forbidden_output_kinds_mismatch(self):
        """Blocker: forbidden_output_kinds 不匹配 → FAIL。"""
        report = build_bare_capability_report(report_id="bcr-001")
        d = report.to_dict()
        d["forbidden_output_kinds"] = ["WrongForbidden"]
        result = verify_bare_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_OUTPUT_KIND_FORBIDDEN, result.error_codes)

    def test_report_claim_contains_p5(self):
        """Blocker: claims 中含 P5 claim → FAIL。"""
        report = build_bare_capability_report(report_id="bcr-001")
        d = report.to_dict()
        d["claims"] = ["this is a p5 claim about bare results"]
        result = verify_bare_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_P5_CLAIM_IN_BARE_REPORT, result.error_codes)

    def test_report_hash_deterministic(self):
        """确定性 hash。"""
        r1 = build_bare_capability_report(report_id="bcr-001")
        r2 = build_bare_capability_report(report_id="bcr-001")
        self.assertEqual(r1.report_hash, r2.report_hash)

    def test_report_hash_tampered(self):
        """Blocker: report_hash 被篡改 → FAIL。"""
        report = build_bare_capability_report(report_id="bcr-001")
        d = report.to_dict()
        d["report_hash"] = "1" * 64
        result = verify_bare_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.QA1_BARE_CAPABILITY_HASH_MISMATCH, result.error_codes)

    def test_report_nonclaims_contain_boundary(self):
        """nonclaims 包含边界声明。"""
        report = build_bare_capability_report(report_id="bcr-001")
        nonclaim_text = " ".join(report.nonclaims)
        self.assertIn("no_p5_claim", nonclaim_text)
        self.assertIn("no_tell_hint", nonclaim_text)
        self.assertIn("no_confirmatory_evidence", nonclaim_text)


# ─── QA1 边界测试 ──────────────────────────────────────────────────────


class TestQA1Boundary(unittest.TestCase):
    """QA1 边界测试：no P5 claim, no Tell/Hint, no confirmatory Evidence。"""

    def test_boundary_no_p5_claim_in_capability_report(self):
        """边界: capability report 无 P5 claim。"""
        report = build_bare_capability_report(report_id="bcr-001")
        self.assertTrue(report.no_p5_claim)
        for claim in report.claims:
            self.assertNotIn("p5 claim", claim.lower())

    def test_boundary_no_tell_hint_in_capability_report(self):
        """边界: capability report 无 Tell/Hint。"""
        report = build_bare_capability_report(report_id="bcr-001")
        self.assertTrue(report.no_tell_hint)

    def test_boundary_no_confirmatory_evidence_in_capability_report(self):
        """边界: capability report 无 confirmatory Evidence。"""
        report = build_bare_capability_report(report_id="bcr-001")
        self.assertTrue(report.no_confirmatory_evidence)

    def test_boundary_allowed_output_kinds_correct(self):
        """边界: allowed_output_kinds 正确。"""
        report = build_bare_capability_report(report_id="bcr-001")
        self.assertEqual(
            set(report.allowed_output_kinds),
            set(QA1_ALLOWED_OUTPUT_KINDS),
        )

    def test_boundary_forbidden_output_kinds_correct(self):
        """边界: forbidden_output_kinds 正确。"""
        report = build_bare_capability_report(report_id="bcr-001")
        self.assertEqual(
            set(report.forbidden_output_kinds),
            set(QA1_FORBIDDEN_OUTPUT_KINDS),
        )

    def test_boundary_forbidden_not_in_allowed(self):
        """边界: forbidden 不在 allowed 中。"""
        report = build_bare_capability_report(report_id="bcr-001")
        overlap = set(report.allowed_output_kinds) & set(report.forbidden_output_kinds)
        self.assertEqual(overlap, set())

    def test_boundary_side_effects_all_zero(self):
        """边界: 所有 side_effect_counters 为 0。"""
        report = build_bare_capability_report(report_id="bcr-001")
        for key, val in report.side_effect_counters.items():
            self.assertEqual(val, 0, f"side_effect_counters[{key}] must be 0")

    def test_boundary_p5_forbidden_in_output(self):
        """边界: P5ClaimRecord 在 forbidden output kinds 中。"""
        self.assertIn("P5ClaimRecord", QA1_FORBIDDEN_OUTPUT_KINDS)

    def test_boundary_evidence_forbidden_in_output(self):
        """边界: EvidenceRecord 在 forbidden output kinds 中。"""
        self.assertIn("EvidenceRecord", QA1_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("ConfirmatoryEvidenceRecord", QA1_FORBIDDEN_OUTPUT_KINDS)

    def test_boundary_bare_baseline_in_allowed(self):
        """边界: BareBaseline 在 allowed output kinds 中。"""
        self.assertIn("BareBaseline", QA1_ALLOWED_OUTPUT_KINDS)

    def test_boundary_qualification_in_allowed(self):
        """边界: BareQualificationResult 在 allowed output kinds 中。"""
        self.assertIn("BareQualificationResult", QA1_ALLOWED_OUTPUT_KINDS)

    def test_boundary_check_ids_contain_boundary_checks(self):
        """边界: check_ids 包含边界检查。"""
        check_text = " ".join(QA1_CHECK_IDS)
        self.assertIn("no_p5_claim", check_text)
        self.assertIn("no_tell_hint", check_text)
        self.assertIn("no_confirmatory_evidence", check_text)


# ─── 端到端集成测试 ────────────────────────────────────────────────────


class TestQA1EndToEnd(unittest.TestCase):
    """端到端集成测试：完整 P3B + Bakeoff-B 流程。"""

    def test_end_to_end_p3b_then_bakeoff_b(self):
        """端到端: P3B bare admission → Bakeoff-B plan → Bakeoff-B scoring。"""
        # 1. P3B bare admission
        release = _make_question_release()
        adapter = FakeHarnessAdapter()
        pipeline = P3BBareAdmission(adapter)
        bundle, p3b_result = pipeline.admit(
            question_release=release,
            baseline_id="bb-001",
            result_id="bqr-001",
            bundle_id="rab-001",
        )
        self.assertTrue(p3b_result.passed)
        self.assertIsNotNone(bundle)

        baseline = pipeline.baseline
        qual = pipeline.qualification

        # 2. Bakeoff-B plan
        plan = build_bakeoff_b_plan(
            plan_id="bbp-001",
            bakeoff_a_ref_id="bar-001",
            bakeoff_a_sha256=_ZERO_HASH,
            question_release_refs=[
                {"ref_id": release.release_id, "sha256": release.content_hash}
            ],
            profile_labels=["devin_glm_5_2_high", "codex_candidate"],
            metrics=["math_correct", "bare_correct", "bare_pass", "bare_qualification"],
            stop_conditions={"max_cost_exceeded": True},
        )
        plan_v = verify_bakeoff_b_plan(plan)
        self.assertTrue(plan_v.passed)

        # 3. Bakeoff-B scoring
        submissions = [
            BakeoffBSubmission(
                blinded_label="devin_glm_5_2_high",
                draft_ref_and_hash=_ref_hash("draft-001"),
                bare_baseline_ref_and_hash={
                    "ref_id": baseline.baseline_id,
                    "sha256": baseline.baseline_hash,
                },
                scores={
                    "math_correct": 0.9,
                    "bare_correct": 0.7,
                    "bare_pass": 0.8,
                    "bare_qualification": 0.75,
                },
            ),
        ]
        scorer = BakeoffBScoring()
        score_result = scorer.score(
            bakeoff_b_plan_ref_and_hash={
                "ref_id": plan.plan_id,
                "sha256": plan.plan_hash,
            },
            submissions=submissions,
        )
        self.assertTrue(score_result.passed)

        report = scorer.build_report(
            report_id="bbsr-001",
            bakeoff_b_plan_ref_and_hash={
                "ref_id": plan.plan_id,
                "sha256": plan.plan_hash,
            },
            submissions=submissions,
        )
        report_v = verify_bakeoff_b_scoring_report(report)
        self.assertTrue(report_v.passed)

        # 4. Bare result retention
        retention = BareResultRetention()
        retention.register_results(pipeline.bare_results)
        retention_v = retention.verify_retention()
        self.assertTrue(retention_v.passed)

        # 5. Capability report
        cap_report = build_bare_capability_report(report_id="bcr-001")
        cap_v = verify_bare_capability_report(cap_report)
        self.assertTrue(cap_v.passed)

    def test_end_to_end_all_results_retained(self):
        """端到端: 所有 bare 结果保留（成功和失败）。"""
        release = _make_question_release()
        adapter = FakeHarnessAdapter()
        pipeline = P3BBareAdmission(adapter)
        bundle, result = pipeline.admit(
            question_release=release,
            baseline_id="bb-001",
            result_id="bqr-001",
            bundle_id="rab-001",
        )
        self.assertTrue(result.passed)

        # All results retained
        self.assertTrue(len(pipeline.bare_results) > 0)
        for bare_result in pipeline.bare_results:
            self.assertFalse(bare_result.tell_hint_included)

        # Baseline has all results
        baseline = pipeline.baseline
        self.assertEqual(
            len(baseline.bare_attempt_results),
            len(pipeline.bare_results),
        )
        self.assertTrue(baseline.all_results_retained)


if __name__ == "__main__":
    unittest.main()
