"""WP-AU1 P6 Independent Audits 测试。

测试层级：Golden → BlindingBroker → Three Audits → RunAudit → LaneStatus →
          CausalEligibility → Disagreement → Negative → Determinism → Boundary → Constants
覆盖：
- Golden path: BlindingBroker generates 3 views → 3 audits run separately →
  each sealed → RunAudit assembled
- All 3 audit roles (Process Auditor, Proof Judge, Leakage Auditor)
- AuditLaneStatus transitions (VALID/INVALID_PROTOCOL/INCONCLUSIVE/MISSING/
  JUDGE_DISAGREEMENT/CONTAMINATED)
- CausalEligibility derivation from lane inputs
- Negative: arm leaked, judge cross-read, restate as action, disagreement
  auto-resolved, missing not terminal, contamination not flagged, not sealed
  separately, process-only in result layer
- Disagreement resolution tests
- Deterministic hash tests
- AU1 boundary tests (allowed/forbidden output kinds)
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
    AU_AUDIT_ROLES,
    AU_ALLOWED_OUTPUT_KINDS,
    AU_CAUSAL_ELIGIBILITY_STATUSES,
    AU_CAUSAL_ELIGIBILITY_TRANSITIONS,
    AU_CHECK_IDS,
    AU_CLAIMS,
    AU_FORBIDDEN_OUTPUT_KINDS,
    AU_LANE_PRIORITY,
    AU_LANE_STATUSES,
    AU_LANE_TERMINAL_STATUSES,
    AU_LANE_TRANSITIONS,
    AU_NONCLAIMS,
    AU_RUN_AUDIT_STATES,
    AU_SIDE_EFFECT_KEYS,
    AU_VIEW_KINDS,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.audit.audit_plan import (
    AuditPlan,
    AuditRoleBinding,
    make_audit_plan,
    verify_audit_plan,
    check_audit_plan_modified_after_start,
)
from seven_system.audit.blinding_broker import (
    BlindingBroker,
    BlindedView,
    verify_blinded_view,
    check_arm_leakage,
)
from seven_system.audit.process_audit import (
    ProcessAudit,
    make_process_audit,
    verify_process_audit,
)
from seven_system.audit.proof_judgment import (
    ProofJudgment,
    make_proof_judgment,
    verify_proof_judgment,
)
from seven_system.audit.leakage_audit import (
    LeakageAudit,
    make_leakage_audit,
    verify_leakage_audit,
)
from seven_system.audit.run_audit import (
    RunAudit,
    make_run_audit,
    verify_run_audit,
    RunAuditAssembler,
    AuditLaneStatus,
    CausalEligibility,
    DisagreementResolution,
    derive_causal_eligibility,
    make_disagreement_resolution,
    verify_disagreement_resolution,
    aggregate_lane_statuses,
    is_valid_lane_transition,
    is_valid_causal_transition,
)
from seven_system.audit.capability_report import (
    build_audit_capability_report,
    verify_audit_capability_report,
    AUDIT_REPORT_SCHEMA_VERSION,
    AUDIT_REPORT_SCOPE,
)


# ─── helpers ────────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64
_TS = "2026-08-14T12:00:00Z"


def _profile_hash(model: str = "glm-5-2", carrier: str = "devin") -> str:
    return hashlib.sha256(canonical_json_bytes({"model": model, "carrier": carrier})).hexdigest()


def _make_role_bindings() -> list[AuditRoleBinding]:
    """构建三个审计角色的绑定规格。"""
    cph = _profile_hash()
    return [
        AuditRoleBinding(
            role_type_id="process_auditor",
            adapter_id="devin",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cph,
            view_kind="process_auditor_view",
            independence_kind="DIFFERENT_SESSION",
            session_id="sess-process-001",
        ),
        AuditRoleBinding(
            role_type_id="proof_judge",
            adapter_id="codex",
            model_uid="gpt-5.6-sol",
            carrier_id="codex",
            carrier_profile_hash=_profile_hash("gpt-5.6-sol", "codex"),
            view_kind="proof_judge_view",
            independence_kind="DIFFERENT_SESSION",
            session_id="sess-proof-001",
        ),
        AuditRoleBinding(
            role_type_id="leakage_auditor",
            adapter_id="devin",
            model_uid="glm-5-2",
            carrier_id="devin",
            carrier_profile_hash=cph,
            view_kind="leakage_auditor_view",
            independence_kind="DIFFERENT_SESSION",
            session_id="sess-leakage-001",
        ),
    ]


def _make_bundle_dict() -> dict:
    """构建一个模拟的 sealed P5 RunArtifactBundle dict。"""
    return {
        "bundle_id": "bundle-001",
        "arm_id": "arm-lineage-001",
        "arm_kind": "lineage",
        "plan_id": "plan-001",
        "purpose": "causal_experiment",
        "run_state": "COMPLETED",
        "raw_artifact_ref": {"ref_id": "raw-001", "sha256": _ZERO_HASH},
        "parser_ref": {"ref_id": "parser-001", "sha256": _ZERO_HASH},
        "termination_reason": "COMPLETED",
        "observability_status": "COMPLETE",
        "observability_state": {"events": 10},
        "trajectory_ref": {"ref_id": "traj-001", "sha256": _ZERO_HASH},
        "answer_ref": {"ref_id": "ans-001", "sha256": _ZERO_HASH},
        "cost_observability": {"tokens": 1000, "cost_usd": 0.5},
        "process_events": [
            {"event": "trigger", "observed": True},
            {"event": "binding", "observed": True},
            {"event": "action", "observed": True},
        ],
        "problem_ref": {"ref_id": "prob-001", "sha256": _ZERO_HASH},
        "solution_ref": {"ref_id": "sol-001", "sha256": _ZERO_HASH},
        "trajectory_math_steps": [
            {"step": 1, "content": "apply theorem X", "observed": True},
            {"step": 2, "content": "simplify", "observed": True},
        ],
        "solution_information_atoms": [
            {"atom": "theorem_X_applied", "observed": True},
            {"atom": "simplification_done", "observed": True},
        ],
        "solver_payload": {"prompt": "solve this", "observed": True},
        "sealed": True,
    }


def _make_audit_plan(plan_id: str = "audit-plan-001") -> AuditPlan:
    """构建一个合法的冻结 AuditPlan。"""
    bundle_dict = _make_bundle_dict()
    bundle_hash = hashlib.sha256(canonical_json_bytes(bundle_dict)).hexdigest()
    return make_audit_plan(
        plan_id=plan_id,
        run_refs=[{
            "bundle_id": bundle_dict["bundle_id"],
            "arm_id": bundle_dict["arm_id"],
            "content_hash": bundle_hash,
        }],
        role_bindings=_make_role_bindings(),
        blinding_spec={
            "process_auditor_view": {"redact": ["arm_id", "arm_kind"]},
            "proof_judge_view": {"redact": ["arm_id", "arm_kind"]},
            "leakage_auditor_view": {"redact": ["arm_id", "arm_kind"]},
        },
        independence_requirements={
            "sessions": "all_distinct",
            "views": "all_distinct",
        },
        leakage_budget={"atoms_limit": 100},
        frozen_at=_TS,
    )


# ─── Golden path tests ──────────────────────────────────────────────────


class TestGoldenPath(unittest.TestCase):
    """Golden path: BlindingBroker → 3 views → 3 audits → sealed → RunAudit。"""

    def test_golden_path_full_flow(self):
        # 1. 冻结 AuditPlan
        plan = _make_audit_plan()
        plan_result = verify_audit_plan(plan)
        self.assertTrue(plan_result.passed, f"plan verification failed: {plan_result.details}")

        # 2. BlindingBroker 生成三个 view
        broker = BlindingBroker()
        bundle_dict = _make_bundle_dict()
        bundle_hash = plan.run_refs[0]["content_hash"]
        broker_result, views = broker.generate_views(
            bundle_id=bundle_dict["bundle_id"],
            bundle_content_hash=bundle_hash,
            bundle_dict=bundle_dict,
            sealed=True,
            plan_id=plan.plan_id,
        )
        self.assertTrue(broker_result.passed, f"broker failed: {broker_result.details}")
        self.assertIsNotNone(views)
        self.assertEqual(len(views), 3)
        self.assertEqual(set(views.keys()), AU_VIEW_KINDS)

        # 3. 验证每个 view
        for view_kind, view in views.items():
            v_result = verify_blinded_view(view)
            self.assertTrue(v_result.passed, f"view {view_kind} failed: {v_result.details}")
            self.assertFalse(check_arm_leakage(view), f"arm leaked in {view_kind}")

        # 4. ProcessAudit
        process_view = views["process_auditor_view"]
        process_audit = make_process_audit(
            audit_id="pa-001",
            plan_id=plan.plan_id,
            view_ref={"view_id": process_view.view_id, "view_hash": process_view.view_hash},
            trigger_analysis={"trigger": "observed", "observed": True},
            binding_analysis={"binding": "observed", "observed": True},
            action_analysis={"actions": [{"kind": "compute", "counted_as_action": True, "observed": True}]},
            progress_analysis={"progress": "observed", "observed": True},
            termination_analysis={"termination": "COMPLETED", "observed": True},
            first_divergence={"divergence": "none", "observed": True},
            observed_facts=[{"fact": "trigger observed", "observed": True}],
            lane_status="VALID",
            sealed=True,
        )
        pa_result = verify_process_audit(process_audit, expected_view_hash=process_view.view_hash)
        self.assertTrue(pa_result.passed, f"process audit failed: {pa_result.details}")

        # 5. ProofJudgment
        proof_view = views["proof_judge_view"]
        proof_judgment = make_proof_judgment(
            judgment_id="pj-001",
            plan_id=plan.plan_id,
            view_ref={"view_id": proof_view.view_id, "view_hash": proof_view.view_hash},
            math_correctness={"correct": True, "observed": True},
            completeness={"complete": True, "observed": True},
            observed_facts=[{"fact": "math correct", "observed": True}],
            conclusion="CORRECT",
            lane_status="VALID",
            sealed=True,
        )
        pj_result = verify_proof_judgment(proof_judgment, expected_view_hash=proof_view.view_hash)
        self.assertTrue(pj_result.passed, f"proof judgment failed: {pj_result.details}")

        # 6. LeakageAudit
        leakage_view = views["leakage_auditor_view"]
        leakage_audit = make_leakage_audit(
            audit_id="la-001",
            plan_id=plan.plan_id,
            view_ref={"view_id": leakage_view.view_id, "view_hash": leakage_view.view_hash},
            solver_payload_analysis={"payload_complete": True, "observed": True},
            solution_information_atoms=[{"atom": "atom1", "observed": True}],
            leakage_budget_check={"exceeded": False, "limit": 100, "count": 1},
            contamination_flagged=False,
            observed_facts=[{"fact": "no leakage", "observed": True}],
            lane_status="VALID",
            sealed=True,
        )
        la_result = verify_leakage_audit(leakage_audit, expected_view_hash=leakage_view.view_hash)
        self.assertTrue(la_result.passed, f"leakage audit failed: {la_result.details}")

        # 7. RunAudit 组装
        assembler = RunAuditAssembler()
        ra_result, run_audit = assembler.assemble(
            run_audit_id="ra-001",
            plan_id=plan.plan_id,
            bundle_ref={"bundle_id": bundle_dict["bundle_id"], "content_hash": bundle_hash},
            process_audit=process_audit,
            proof_judgment=proof_judgment,
            leakage_audit=leakage_audit,
        )
        self.assertTrue(ra_result.passed, f"run audit assembly failed: {ra_result.details}")
        self.assertIsNotNone(run_audit)
        self.assertEqual(run_audit.state, "ASSEMBLED")
        self.assertTrue(run_audit.sealed)
        self.assertEqual(run_audit.causal_eligibility, "ELIGIBLE")

        # 8. 验证 RunAudit
        verify_result = verify_run_audit(
            run_audit,
            expected_process_hash=process_audit.content_hash,
            expected_proof_hash=proof_judgment.content_hash,
            expected_leakage_hash=leakage_audit.content_hash,
        )
        self.assertTrue(verify_result.passed, f"run audit verification failed: {verify_result.details}")


# ─── AuditPlan tests ────────────────────────────────────────────────────


class TestAuditPlan(unittest.TestCase):

    def test_plan_frozen_and_verified(self):
        plan = _make_audit_plan()
        self.assertTrue(plan.is_frozen)
        result = verify_audit_plan(plan)
        self.assertTrue(result.passed)

    def test_plan_not_frozen_blocked(self):
        from seven_system.audit.audit_plan import AuditPlan
        plan = AuditPlan(plan_id="x", state="DRAFT")
        result = verify_audit_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_PLAN_NOT_FROZEN, result.error_codes)

    def test_plan_modified_after_start_detected(self):
        plan = _make_audit_plan()
        # 模拟启动后被修改
        import dataclasses
        modified = dataclasses.replace(plan, state="STARTED", content_hash="wrong")
        self.assertTrue(check_audit_plan_modified_after_start(modified, plan.content_hash))

    def test_plan_missing_roles_blocked(self):
        plan = make_audit_plan(
            plan_id="x",
            run_refs=[{"bundle_id": "b1", "content_hash": _ZERO_HASH}],
            role_bindings=_make_role_bindings()[:2],  # only 2 roles
        )
        result = verify_audit_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_ROLE_UNKNOWN, result.error_codes)

    def test_plan_duplicate_sessions_blocked(self):
        bindings = _make_role_bindings()
        # make two sessions the same
        bindings[1] = AuditRoleBinding(
            role_type_id="proof_judge", adapter_id="codex", model_uid="gpt-5.6-sol",
            carrier_id="codex", carrier_profile_hash=_profile_hash("gpt-5.6-sol", "codex"),
            view_kind="proof_judge_view", independence_kind="DIFFERENT_SESSION",
            session_id="sess-process-001",  # same as process
        )
        plan = make_audit_plan(
            plan_id="x",
            run_refs=[{"bundle_id": "b1", "content_hash": _ZERO_HASH}],
            role_bindings=bindings,
        )
        result = verify_audit_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_INDEPENDENCE_VIOLATED, result.error_codes)

    def test_plan_no_run_refs_blocked(self):
        plan = make_audit_plan(plan_id="x", role_bindings=_make_role_bindings())
        result = verify_audit_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_BUNDLE_REF_MISSING, result.error_codes)

    def test_plan_hash_deterministic(self):
        plan1 = _make_audit_plan()
        plan2 = _make_audit_plan()
        self.assertEqual(plan1.content_hash, plan2.content_hash)


# ─── BlindingBroker tests ───────────────────────────────────────────────


class TestBlindingBroker(unittest.TestCase):

    def test_three_views_generated(self):
        broker = BlindingBroker()
        bundle_dict = _make_bundle_dict()
        result, views = broker.generate_views(
            bundle_id="b1", bundle_content_hash=_ZERO_HASH,
            bundle_dict=bundle_dict, sealed=True,
        )
        self.assertTrue(result.passed)
        self.assertEqual(len(views), 3)
        self.assertEqual(set(views.keys()), AU_VIEW_KINDS)

    def test_arm_identity_not_leaked(self):
        broker = BlindingBroker()
        bundle_dict = _make_bundle_dict()
        result, views = broker.generate_views(
            bundle_id="b1", bundle_content_hash=_ZERO_HASH,
            bundle_dict=bundle_dict, sealed=True,
        )
        self.assertTrue(result.passed)
        for view_kind, view in views.items():
            self.assertFalse(check_arm_leakage(view), f"arm leaked in {view_kind}")

    def test_view_hashes_distinct(self):
        broker = BlindingBroker()
        bundle_dict = _make_bundle_dict()
        result, views = broker.generate_views(
            bundle_id="b1", bundle_content_hash=_ZERO_HASH,
            bundle_dict=bundle_dict, sealed=True,
        )
        self.assertTrue(result.passed)
        hashes = [v.view_hash for v in views.values()]
        self.assertEqual(len(set(hashes)), 3)

    def test_unsealed_bundle_blocked(self):
        broker = BlindingBroker()
        bundle_dict = _make_bundle_dict()
        result, views = broker.generate_views(
            bundle_id="b1", bundle_content_hash=_ZERO_HASH,
            bundle_dict=bundle_dict, sealed=False,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_BUNDLE_REF_MISSING, result.error_codes)

    def test_view_hash_deterministic(self):
        broker1 = BlindingBroker()
        broker2 = BlindingBroker()
        bundle_dict = _make_bundle_dict()
        r1, v1 = broker1.generate_views(
            bundle_id="b1", bundle_content_hash=_ZERO_HASH,
            bundle_dict=bundle_dict, sealed=True,
        )
        r2, v2 = broker2.generate_views(
            bundle_id="b1", bundle_content_hash=_ZERO_HASH,
            bundle_dict=bundle_dict, sealed=True,
        )
        for vk in AU_VIEW_KINDS:
            self.assertEqual(v1[vk].view_hash, v2[vk].view_hash)

    def test_verify_blinded_view_valid(self):
        broker = BlindingBroker()
        bundle_dict = _make_bundle_dict()
        _, views = broker.generate_views(
            bundle_id="b1", bundle_content_hash=_ZERO_HASH,
            bundle_dict=bundle_dict, sealed=True,
        )
        for view in views.values():
            result = verify_blinded_view(view)
            self.assertTrue(result.passed)

    def test_arm_leaked_into_view_blocked(self):
        # 构造一个泄漏 arm 身份的 view
        view = BlindedView(
            view_id="v1", view_kind="process_auditor_view",
            role_type_id="process_auditor",
            source_bundle_ref={"bundle_id": "b1", "content_hash": _ZERO_HASH},
            redacted_payload={"arm_id": "arm-001", "data": "x"},
            view_hash="x",
            source_hash=_ZERO_HASH,
        )
        result = verify_blinded_view(view)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_ARM_LEAKED_INTO_VIEW, result.error_codes)


# ─── ProcessAudit tests ─────────────────────────────────────────────────


class TestProcessAudit(unittest.TestCase):

    def test_valid_process_audit(self):
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            observed_facts=[{"fact": "x", "observed": True}],
            lane_status="VALID", sealed=True,
        )
        result = verify_process_audit(audit)
        self.assertTrue(result.passed)

    def test_not_sealed_blocked(self):
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=False,
        )
        result = verify_process_audit(audit)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_NOT_SEALED_SEPARATELY, result.error_codes)

    def test_restate_as_action_blocked(self):
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            action_analysis={"actions": [
                {"kind": "restate", "is_restate": True, "counted_as_action": True},
            ]},
            sealed=True,
        )
        result = verify_process_audit(audit)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_RESTATE_AS_ACTION, result.error_codes)

    def test_restate_not_counted_ok(self):
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            action_analysis={"actions": [
                {"kind": "restate", "is_restate": True, "counted_as_action": False},
            ]},
            sealed=True,
        )
        result = verify_process_audit(audit)
        self.assertTrue(result.passed)

    def test_non_observed_fact_blocked(self):
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            observed_facts=[{"fact": "x", "observed": False}],
            sealed=True,
        )
        result = verify_process_audit(audit)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_OBSERVATION_NOT_FACT, result.error_codes)

    def test_causal_claim_in_fact_blocked(self):
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            observed_facts=[{"fact": "x", "observed": True, "causal_claim": "A causes B"}],
            sealed=True,
        )
        result = verify_process_audit(audit)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_OBSERVATION_NOT_FACT, result.error_codes)

    def test_view_hash_mismatch_blocked(self):
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=True,
        )
        result = verify_process_audit(audit, expected_view_hash="a" * 64)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_VIEW_HASH_MISMATCH, result.error_codes)

    def test_hash_deterministic(self):
        a1 = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=True,
        )
        a2 = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=True,
        )
        self.assertEqual(a1.content_hash, a2.content_hash)


# ─── ProofJudgment tests ────────────────────────────────────────────────


class TestProofJudgment(unittest.TestCase):

    def test_valid_proof_judgment(self):
        j = make_proof_judgment(
            judgment_id="pj-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            conclusion="CORRECT", sealed=True,
        )
        result = verify_proof_judgment(j)
        self.assertTrue(result.passed)

    def test_not_sealed_blocked(self):
        j = make_proof_judgment(
            judgment_id="pj-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=False,
        )
        result = verify_proof_judgment(j)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_NOT_SEALED_SEPARATELY, result.error_codes)

    def test_judge_cross_read_blocked(self):
        j = make_proof_judgment(
            judgment_id="pj-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            math_correctness={"other_judge_conclusion": "CORRECT"},
            sealed=True,
        )
        result = verify_proof_judgment(j)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_JUDGE_CONCLUSION_CROSS_READ, result.error_codes)

    def test_judge_referenced_judgment_id_blocked(self):
        j = make_proof_judgment(
            judgment_id="pj-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            completeness={"referenced_judgment_id": "pj-other"},
            sealed=True,
        )
        result = verify_proof_judgment(j)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_JUDGE_CONCLUSION_CROSS_READ, result.error_codes)

    def test_hash_deterministic(self):
        j1 = make_proof_judgment(
            judgment_id="pj-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=True,
        )
        j2 = make_proof_judgment(
            judgment_id="pj-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=True,
        )
        self.assertEqual(j1.content_hash, j2.content_hash)


# ─── LeakageAudit tests ─────────────────────────────────────────────────


class TestLeakageAudit(unittest.TestCase):

    def test_valid_leakage_audit(self):
        a = make_leakage_audit(
            audit_id="la-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=True,
        )
        result = verify_leakage_audit(a)
        self.assertTrue(result.passed)

    def test_not_sealed_blocked(self):
        a = make_leakage_audit(
            audit_id="la-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=False,
        )
        result = verify_leakage_audit(a)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_NOT_SEALED_SEPARATELY, result.error_codes)

    def test_contamination_not_flagged_blocked(self):
        a = make_leakage_audit(
            audit_id="la-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            solver_payload_analysis={"contamination_detected": True},
            contamination_flagged=False,
            sealed=True,
        )
        result = verify_leakage_audit(a)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_CONTAMINATION_NOT_FLAGGED, result.error_codes)

    def test_contamination_flagged_ok(self):
        a = make_leakage_audit(
            audit_id="la-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            solver_payload_analysis={"contamination_detected": True},
            contamination_flagged=True,
            lane_status="CONTAMINATED",
            sealed=True,
        )
        result = verify_leakage_audit(a)
        self.assertTrue(result.passed)

    def test_leakage_budget_exceeded_blocked(self):
        atoms = [{"atom": f"a{i}", "observed": True} for i in range(10)]
        a = make_leakage_audit(
            audit_id="la-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            solution_information_atoms=atoms,
            leakage_budget_check={"exceeded": False, "limit": 5, "count": 10},
            sealed=True,
        )
        result = verify_leakage_audit(a, leakage_budget_limit=5)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_LEAKAGE_BUDGET_EXCEEDED, result.error_codes)

    def test_hash_deterministic(self):
        a1 = make_leakage_audit(
            audit_id="la-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=True,
        )
        a2 = make_leakage_audit(
            audit_id="la-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=True,
        )
        self.assertEqual(a1.content_hash, a2.content_hash)


# ─── RunAudit assembly tests ────────────────────────────────────────────


class TestRunAuditAssembly(unittest.TestCase):

    def test_assemble_all_three_sealed(self):
        plan = _make_audit_plan()
        bundle_dict = _make_bundle_dict()
        bundle_hash = plan.run_refs[0]["content_hash"]

        broker = BlindingBroker()
        _, views = broker.generate_views(
            bundle_id=bundle_dict["bundle_id"],
            bundle_content_hash=bundle_hash,
            bundle_dict=bundle_dict, sealed=True,
        )

        pa = make_process_audit(
            audit_id="pa-1", plan_id=plan.plan_id,
            view_ref={"view_id": views["process_auditor_view"].view_id,
                      "view_hash": views["process_auditor_view"].view_hash},
            lane_status="VALID", sealed=True,
        )
        pj = make_proof_judgment(
            judgment_id="pj-1", plan_id=plan.plan_id,
            view_ref={"view_id": views["proof_judge_view"].view_id,
                      "view_hash": views["proof_judge_view"].view_hash},
            lane_status="VALID", sealed=True,
        )
        la = make_leakage_audit(
            audit_id="la-1", plan_id=plan.plan_id,
            view_ref={"view_id": views["leakage_auditor_view"].view_id,
                      "view_hash": views["leakage_auditor_view"].view_hash},
            lane_status="VALID", sealed=True,
        )

        assembler = RunAuditAssembler()
        result, run_audit = assembler.assemble(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": bundle_dict["bundle_id"], "content_hash": bundle_hash},
            process_audit=pa, proof_judgment=pj, leakage_audit=la,
        )
        self.assertTrue(result.passed, result.details)
        self.assertEqual(run_audit.causal_eligibility, "ELIGIBLE")
        self.assertEqual(run_audit.state, "ASSEMBLED")

    def test_assemble_missing_audit_recorded_as_missing(self):
        plan = _make_audit_plan()
        bundle_dict = _make_bundle_dict()
        bundle_hash = plan.run_refs[0]["content_hash"]

        pa = make_process_audit(
            audit_id="pa-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )
        pj = make_proof_judgment(
            judgment_id="pj-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v2", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )
        # leakage_audit = None → MISSING

        assembler = RunAuditAssembler()
        result, run_audit = assembler.assemble(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": "b1", "content_hash": bundle_hash},
            process_audit=pa, proof_judgment=pj, leakage_audit=None,
        )
        # MISSING is a legal terminal → assembly should pass
        self.assertTrue(result.passed, result.details)
        self.assertEqual(run_audit.lane_statuses["leakage_auditor"], "MISSING")
        # MISSING lane → INCONCLUSIVE causal eligibility
        self.assertEqual(run_audit.causal_eligibility, "INCONCLUSIVE")

    def test_assemble_not_sealed_blocked(self):
        plan = _make_audit_plan()
        bundle_hash = plan.run_refs[0]["content_hash"]

        pa = make_process_audit(
            audit_id="pa-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=False,  # not sealed
        )
        pj = make_proof_judgment(
            judgment_id="pj-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v2", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )
        la = make_leakage_audit(
            audit_id="la-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v3", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )

        assembler = RunAuditAssembler()
        result, run_audit = assembler.assemble(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": "b1", "content_hash": bundle_hash},
            process_audit=pa, proof_judgment=pj, leakage_audit=la,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_NOT_SEALED_SEPARATELY, result.error_codes)

    def test_assemble_contamination_flagged(self):
        plan = _make_audit_plan()
        bundle_hash = plan.run_refs[0]["content_hash"]

        pa = make_process_audit(
            audit_id="pa-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )
        pj = make_proof_judgment(
            judgment_id="pj-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v2", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )
        la = make_leakage_audit(
            audit_id="la-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v3", "view_hash": _ZERO_HASH},
            solver_payload_analysis={"contamination_detected": True},
            contamination_flagged=True,
            lane_status="CONTAMINATED", sealed=True,
        )

        assembler = RunAuditAssembler()
        result, run_audit = assembler.assemble(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": "b1", "content_hash": bundle_hash},
            process_audit=pa, proof_judgment=pj, leakage_audit=la,
        )
        self.assertTrue(result.passed, result.details)
        self.assertEqual(run_audit.lane_statuses["leakage_auditor"], "CONTAMINATED")
        self.assertEqual(run_audit.causal_eligibility, "CONTAMINATED")

    def test_assemble_contamination_not_flagged_blocked(self):
        plan = _make_audit_plan()
        bundle_hash = plan.run_refs[0]["content_hash"]

        pa = make_process_audit(
            audit_id="pa-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )
        pj = make_proof_judgment(
            judgment_id="pj-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v2", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )
        la = make_leakage_audit(
            audit_id="la-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v3", "view_hash": _ZERO_HASH},
            solver_payload_analysis={"contamination_detected": True},
            contamination_flagged=False,  # not flagged!
            lane_status="VALID", sealed=True,
        )

        assembler = RunAuditAssembler()
        result, _ = assembler.assemble(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": "b1", "content_hash": bundle_hash},
            process_audit=pa, proof_judgment=pj, leakage_audit=la,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_CONTAMINATION_NOT_FLAGGED, result.error_codes)

    def test_run_audit_hash_deterministic(self):
        plan = _make_audit_plan()
        bundle_hash = plan.run_refs[0]["content_hash"]

        ra1 = make_run_audit(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": "b1", "content_hash": bundle_hash},
            process_audit_ref={"audit_id": "pa-1", "content_hash": _ZERO_HASH},
            proof_judgment_ref={"judgment_id": "pj-1", "content_hash": _ZERO_HASH},
            leakage_audit_ref={"audit_id": "la-1", "content_hash": _ZERO_HASH},
            lane_statuses={"process_auditor": "VALID", "proof_judge": "VALID", "leakage_auditor": "VALID"},
            causal_eligibility="ELIGIBLE",
        )
        ra2 = make_run_audit(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": "b1", "content_hash": bundle_hash},
            process_audit_ref={"audit_id": "pa-1", "content_hash": _ZERO_HASH},
            proof_judgment_ref={"judgment_id": "pj-1", "content_hash": _ZERO_HASH},
            leakage_audit_ref={"audit_id": "la-1", "content_hash": _ZERO_HASH},
            lane_statuses={"process_auditor": "VALID", "proof_judge": "VALID", "leakage_auditor": "VALID"},
            causal_eligibility="ELIGIBLE",
        )
        self.assertEqual(ra1.content_hash, ra2.content_hash)

    def test_run_audit_seal_hash_mismatch_blocked(self):
        plan = _make_audit_plan()
        bundle_hash = plan.run_refs[0]["content_hash"]

        ra = make_run_audit(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": "b1", "content_hash": bundle_hash},
            process_audit_ref={"audit_id": "pa-1", "content_hash": _ZERO_HASH},
            proof_judgment_ref={"judgment_id": "pj-1", "content_hash": _ZERO_HASH},
            leakage_audit_ref={"audit_id": "la-1", "content_hash": _ZERO_HASH},
            lane_statuses={"process_auditor": "VALID", "proof_judge": "VALID", "leakage_auditor": "VALID"},
            causal_eligibility="ELIGIBLE",
        )
        result = verify_run_audit(ra, expected_process_hash="a" * 64)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_SEAL_HASH_MISMATCH, result.error_codes)


# ─── AuditLaneStatus tests ──────────────────────────────────────────────


class TestAuditLaneStatus(unittest.TestCase):

    def test_all_lane_statuses_valid(self):
        for status in AU_LANE_STATUSES:
            ls = AuditLaneStatus(lane="process_auditor", status=status)
            self.assertTrue(ls.is_terminal)

    def test_lane_priority_ordering(self):
        # CONTAMINATED > INVALID_PROTOCOL > JUDGE_DISAGREEMENT/MISSING/INCONCLUSIVE > VALID
        self.assertGreater(AU_LANE_PRIORITY["CONTAMINATED"], AU_LANE_PRIORITY["INVALID_PROTOCOL"])
        self.assertGreater(AU_LANE_PRIORITY["INVALID_PROTOCOL"], AU_LANE_PRIORITY["VALID"])
        self.assertEqual(AU_LANE_PRIORITY["JUDGE_DISAGREEMENT"], AU_LANE_PRIORITY["MISSING"])
        self.assertEqual(AU_LANE_PRIORITY["MISSING"], AU_LANE_PRIORITY["INCONCLUSIVE"])
        self.assertGreater(AU_LANE_PRIORITY["INCONCLUSIVE"], AU_LANE_PRIORITY["VALID"])

    def test_aggregate_highest_priority_wins(self):
        lanes = [
            AuditLaneStatus(lane="process_auditor", status="VALID"),
            AuditLaneStatus(lane="proof_judge", status="MISSING"),
            AuditLaneStatus(lane="leakage_auditor", status="CONTAMINATED"),
        ]
        agg = aggregate_lane_statuses(lanes)
        self.assertEqual(agg.status, "CONTAMINATED")

    def test_aggregate_valid_when_all_valid(self):
        lanes = [
            AuditLaneStatus(lane="process_auditor", status="VALID"),
            AuditLaneStatus(lane="proof_judge", status="VALID"),
            AuditLaneStatus(lane="leakage_auditor", status="VALID"),
        ]
        agg = aggregate_lane_statuses(lanes)
        self.assertEqual(agg.status, "VALID")

    def test_aggregate_empty_is_missing(self):
        agg = aggregate_lane_statuses([])
        self.assertEqual(agg.status, "MISSING")

    def test_lane_transition_pending_to_terminal(self):
        for status in AU_LANE_STATUSES:
            self.assertTrue(is_valid_lane_transition("PENDING", status))

    def test_lane_transition_terminal_blocked(self):
        for status in AU_LANE_STATUSES:
            self.assertFalse(is_valid_lane_transition(status, "VALID"))

    def test_missing_is_terminal(self):
        self.assertIn("MISSING", AU_LANE_TERMINAL_STATUSES)


# ─── CausalEligibility tests ────────────────────────────────────────────


class TestCausalEligibility(unittest.TestCase):

    def test_all_valid_eligible(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "VALID",
                "leakage_auditor": "VALID",
            },
        )
        self.assertEqual(ce.status, "ELIGIBLE")

    def test_any_contaminated(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "VALID",
                "leakage_auditor": "CONTAMINATED",
            },
        )
        self.assertEqual(ce.status, "CONTAMINATED")

    def test_any_invalid_protocol(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "INVALID_PROTOCOL",
                "proof_judge": "VALID",
                "leakage_auditor": "VALID",
            },
        )
        self.assertEqual(ce.status, "INVALID")

    def test_any_missing(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "MISSING",
                "leakage_auditor": "VALID",
            },
        )
        self.assertEqual(ce.status, "INCONCLUSIVE")

    def test_any_judge_disagreement(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "JUDGE_DISAGREEMENT",
                "leakage_auditor": "VALID",
            },
        )
        self.assertEqual(ce.status, "INCONCLUSIVE")

    def test_any_inconclusive(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "INCONCLUSIVE",
                "proof_judge": "VALID",
                "leakage_auditor": "VALID",
            },
        )
        self.assertEqual(ce.status, "INCONCLUSIVE")

    def test_blind_breach_contaminated(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "VALID",
                "leakage_auditor": "VALID",
            },
            blind_breach=True,
        )
        self.assertEqual(ce.status, "CONTAMINATED")

    def test_leakage_breach_contaminated(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "VALID",
                "leakage_auditor": "VALID",
            },
            leakage_breach=True,
        )
        self.assertEqual(ce.status, "CONTAMINATED")

    def test_missing_lane_status_inconclusive(self):
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "VALID",
                # leakage_auditor missing
            },
        )
        self.assertEqual(ce.status, "INCONCLUSIVE")

    def test_process_only_when_result_not_required(self):
        ce = derive_causal_eligibility(
            lane_statuses={"process_auditor": "VALID"},
            required_lanes=("process_auditor",),
        )
        self.assertEqual(ce.status, "PROCESS_ONLY")

    def test_result_only_when_process_not_required(self):
        ce = derive_causal_eligibility(
            lane_statuses={"proof_judge": "VALID", "leakage_auditor": "VALID"},
            required_lanes=("proof_judge", "leakage_auditor"),
        )
        self.assertEqual(ce.status, "RESULT_ONLY")

    def test_process_only_in_result_layer_blocked(self):
        # process_lane in result_lanes → INVALID (mechanical rejection)
        ce = derive_causal_eligibility(
            lane_statuses={"process_auditor": "VALID", "proof_judge": "VALID"},
            required_lanes=("process_auditor", "proof_judge"),
            result_lanes=("process_auditor", "proof_judge"),  # process in result!
        )
        self.assertEqual(ce.status, "INVALID")

    def test_process_only_not_in_result_layer_eligible(self):
        # process valid + result valid + process not in result_lanes → ELIGIBLE
        ce = derive_causal_eligibility(
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "VALID",
                "leakage_auditor": "VALID",
            },
            result_lanes=("proof_judge", "leakage_auditor"),
        )
        self.assertEqual(ce.status, "ELIGIBLE")

    def test_causal_transition_pending_to_terminal(self):
        for status in AU_CAUSAL_ELIGIBILITY_STATUSES:
            self.assertTrue(is_valid_causal_transition("PENDING", status))

    def test_causal_transition_terminal_blocked(self):
        for status in AU_CAUSAL_ELIGIBILITY_STATUSES:
            self.assertFalse(is_valid_causal_transition(status, "ELIGIBLE"))

    def test_run_audit_process_only_in_result_layer_blocked(self):
        # causal_eligibility=RESULT_ONLY but process_auditor not VALID
        ra = make_run_audit(
            run_audit_id="ra-1", plan_id="plan-1",
            bundle_ref={"bundle_id": "b1", "content_hash": _ZERO_HASH},
            process_audit_ref={"audit_id": "pa-1", "content_hash": _ZERO_HASH},
            proof_judgment_ref={"judgment_id": "pj-1", "content_hash": _ZERO_HASH},
            leakage_audit_ref={"audit_id": "la-1", "content_hash": _ZERO_HASH},
            lane_statuses={
                "process_auditor": "MISSING",  # process not valid
                "proof_judge": "VALID",
                "leakage_auditor": "VALID",
            },
            causal_eligibility="RESULT_ONLY",  # claims result only but process missing
        )
        result = verify_run_audit(ra)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_PROCESS_ONLY_IN_RESULT_LAYER, result.error_codes)

    def test_run_audit_process_only_with_valid_result_blocked(self):
        # causal_eligibility=PROCESS_ONLY but result lanes VALID
        ra = make_run_audit(
            run_audit_id="ra-1", plan_id="plan-1",
            bundle_ref={"bundle_id": "b1", "content_hash": _ZERO_HASH},
            process_audit_ref={"audit_id": "pa-1", "content_hash": _ZERO_HASH},
            proof_judgment_ref={"judgment_id": "pj-1", "content_hash": _ZERO_HASH},
            leakage_audit_ref={"audit_id": "la-1", "content_hash": _ZERO_HASH},
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "VALID",  # result valid → process-only shouldn't apply
                "leakage_auditor": "VALID",
            },
            causal_eligibility="PROCESS_ONLY",
        )
        result = verify_run_audit(ra)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_PROCESS_ONLY_IN_RESULT_LAYER, result.error_codes)


# ─── DisagreementResolution tests ───────────────────────────────────────


class TestDisagreementResolution(unittest.TestCase):

    def test_no_disagreement(self):
        dr = make_disagreement_resolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "CORRECT"},
        )
        self.assertFalse(dr.is_disagreement)
        self.assertEqual(dr.resolution, "NO_DISAGREEMENT")
        result = verify_disagreement_resolution(dr)
        self.assertTrue(result.passed)

    def test_disagreement_no_preregistered_rule_preserved(self):
        dr = make_disagreement_resolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "INCORRECT"},
        )
        self.assertTrue(dr.is_disagreement)
        self.assertEqual(dr.resolution, "PRESERVED")
        self.assertFalse(dr.auto_resolved)
        self.assertTrue(dr.recorded)
        result = verify_disagreement_resolution(dr)
        self.assertTrue(result.passed)

    def test_disagreement_with_preregistered_third_judge(self):
        dr = make_disagreement_resolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "INCORRECT"},
            preregistered_rule={"rule_kind": "third_judge", "ref": "rule-001"},
        )
        self.assertTrue(dr.is_disagreement)
        self.assertEqual(dr.resolution, "THIRD_JUDGE")
        result = verify_disagreement_resolution(dr)
        self.assertTrue(result.passed)

    def test_disagreement_with_preregistered_human_expert(self):
        dr = make_disagreement_resolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "INCORRECT"},
            preregistered_rule={"rule_kind": "human_expert", "ref": "rule-002"},
        )
        self.assertEqual(dr.resolution, "HUMAN_EXPERT")

    def test_disagreement_with_preregistered_formal_checker(self):
        dr = make_disagreement_resolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "INCORRECT"},
            preregistered_rule={"rule_kind": "formal_checker", "ref": "rule-003"},
        )
        self.assertEqual(dr.resolution, "FORMAL_CHECKER")

    def test_auto_resolved_blocked(self):
        from seven_system.audit.run_audit import DisagreementResolution
        dr = DisagreementResolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "INCORRECT"},
            is_disagreement=True,
            resolution="PRESERVED",
            auto_resolved=True,  # violation!
            recorded=True,
        )
        result = verify_disagreement_resolution(dr)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_DISAGREEMENT_AUTO_RESOLVED, result.error_codes)

    def test_not_recorded_blocked(self):
        from seven_system.audit.run_audit import DisagreementResolution
        dr = DisagreementResolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "INCORRECT"},
            is_disagreement=True,
            resolution="PRESERVED",
            auto_resolved=False,
            recorded=False,  # violation!
        )
        result = verify_disagreement_resolution(dr)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_DISAGREEMENT_NOT_RECORDED, result.error_codes)

    def test_disagreement_without_rule_not_auto_resolved(self):
        # 无预注册规则的分歧不得被自选解决
        dr = make_disagreement_resolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "INCORRECT"},
        )
        # resolution must be PRESERVED, not THIRD_JUDGE or similar
        self.assertEqual(dr.resolution, "PRESERVED")
        self.assertFalse(dr.auto_resolved)

    def test_disagreement_in_run_audit_assembly(self):
        plan = _make_audit_plan()
        bundle_hash = plan.run_refs[0]["content_hash"]

        pa = make_process_audit(
            audit_id="pa-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )
        pj = make_proof_judgment(
            judgment_id="pj-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v2", "view_hash": _ZERO_HASH},
            math_correctness={"judge_conclusions": {"j1": "CORRECT", "j2": "INCORRECT"}},
            lane_status="JUDGE_DISAGREEMENT", sealed=True,
        )
        la = make_leakage_audit(
            audit_id="la-1", plan_id=plan.plan_id,
            view_ref={"view_id": "v3", "view_hash": _ZERO_HASH},
            lane_status="VALID", sealed=True,
        )

        assembler = RunAuditAssembler()
        result, run_audit = assembler.assemble(
            run_audit_id="ra-1", plan_id=plan.plan_id,
            bundle_ref={"bundle_id": "b1", "content_hash": bundle_hash},
            process_audit=pa, proof_judgment=pj, leakage_audit=la,
        )
        self.assertTrue(result.passed, result.details)
        self.assertEqual(run_audit.lane_statuses["proof_judge"], "JUDGE_DISAGREEMENT")
        # disagreement should be recorded
        self.assertTrue(run_audit.disagreement_resolution)
        self.assertEqual(run_audit.disagreement_resolution.get("resolution"), "PRESERVED")
        self.assertFalse(run_audit.disagreement_resolution.get("auto_resolved"))
        # JUDGE_DISAGREEMENT → INCONCLUSIVE
        self.assertEqual(run_audit.causal_eligibility, "INCONCLUSIVE")


# ─── Capability report tests ────────────────────────────────────────────


class TestAuditCapabilityReport(unittest.TestCase):

    def test_valid_report(self):
        plan = _make_audit_plan()
        report = build_audit_capability_report(
            plan_hash=plan.content_hash,
            bundle_count=1,
            views_generated=3,
            process_audits_sealed=1,
            proof_judgments_sealed=1,
            leakage_audits_sealed=1,
            run_audits_assembled=1,
            missing_terminal_count=0,
            disagreement_preserved_count=0,
            contamination_flagged_count=0,
            verifier_identity="au1-verifier",
        )
        errors = verify_audit_capability_report(report)
        self.assertEqual(len(errors), 0, [f"{e[0]}:{e[1]}" for e in errors])

    def test_report_with_disagreement_and_missing(self):
        plan = _make_audit_plan()
        report = build_audit_capability_report(
            plan_hash=plan.content_hash,
            bundle_count=2,
            views_generated=6,
            process_audits_sealed=2,
            proof_judgments_sealed=2,
            leakage_audits_sealed=1,  # one missing
            run_audits_assembled=2,
            missing_terminal_count=1,
            disagreement_preserved_count=1,
            contamination_flagged_count=0,
            verifier_identity="au1-verifier",
        )
        errors = verify_audit_capability_report(report)
        self.assertEqual(len(errors), 0, [f"{e[0]}:{e[1]}" for e in errors])

    def test_report_wrong_schema_version(self):
        plan = _make_audit_plan()
        report = build_audit_capability_report(
            plan_hash=plan.content_hash,
            bundle_count=1, views_generated=3,
            process_audits_sealed=1, proof_judgments_sealed=1,
            leakage_audits_sealed=1, run_audits_assembled=1,
            missing_terminal_count=0, disagreement_preserved_count=0,
            contamination_flagged_count=0, verifier_identity="v",
        )
        report["schema_version"] = "wrong"
        errors = verify_audit_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_report_forbidden_output_kind(self):
        plan = _make_audit_plan()
        report = build_audit_capability_report(
            plan_hash=plan.content_hash,
            bundle_count=1, views_generated=3,
            process_audits_sealed=1, proof_judgments_sealed=1,
            leakage_audits_sealed=1, run_audits_assembled=1,
            missing_terminal_count=0, disagreement_preserved_count=0,
            contamination_flagged_count=0, verifier_identity="v",
        )
        report["report_kind"] = "EvidenceRecord"  # forbidden
        errors = verify_audit_capability_report(report)
        self.assertTrue(any(e[0] == EC.AU_OUTPUT_KIND_FORBIDDEN for e in errors))

    def test_report_side_effects_nonzero(self):
        plan = _make_audit_plan()
        report = build_audit_capability_report(
            plan_hash=plan.content_hash,
            bundle_count=1, views_generated=3,
            process_audits_sealed=1, proof_judgments_sealed=1,
            leakage_audits_sealed=1, run_audits_assembled=1,
            missing_terminal_count=0, disagreement_preserved_count=0,
            contamination_flagged_count=0, verifier_identity="v",
        )
        report["side_effects"]["database_writes"] = 1
        errors = verify_audit_capability_report(report)
        self.assertTrue(any(e[0] == EC.AU_OUTPUT_KIND_FORBIDDEN for e in errors))

    def test_report_claims_mismatch(self):
        plan = _make_audit_plan()
        report = build_audit_capability_report(
            plan_hash=plan.content_hash,
            bundle_count=1, views_generated=3,
            process_audits_sealed=1, proof_judgments_sealed=1,
            leakage_audits_sealed=1, run_audits_assembled=1,
            missing_terminal_count=0, disagreement_preserved_count=0,
            contamination_flagged_count=0, verifier_identity="v",
        )
        report["claims"]["audit_plan_frozen_before_audit"] = False
        errors = verify_audit_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))


# ─── Boundary tests ─────────────────────────────────────────────────────


class TestBoundary(unittest.TestCase):

    def test_allowed_output_kinds(self):
        expected = {
            "AuditPlan", "BlindedView", "ProcessAudit",
            "ProofJudgment", "LeakageAudit", "RunAudit",
            "AuditCapabilityReport",
        }
        self.assertEqual(AU_ALLOWED_OUTPUT_KINDS, expected)

    def test_forbidden_output_kinds(self):
        # must include other WP's outputs
        self.assertIn("EvidenceRecord", AU_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("ExperimentPlan", AU_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("RunArtifactBundle", AU_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("DatabaseSchemaStateReport", AU_FORBIDDEN_OUTPUT_KINDS)

    def test_allowed_and_forbidden_disjoint(self):
        self.assertEqual(AU_ALLOWED_OUTPUT_KINDS & AU_FORBIDDEN_OUTPUT_KINDS, set())

    def test_audit_roles_match_cw_p6(self):
        from seven_system.contracts.errors import CW_P6_ROLES
        self.assertEqual(AU_AUDIT_ROLES, CW_P6_ROLES)

    def test_view_kinds_three(self):
        self.assertEqual(len(AU_VIEW_KINDS), 3)


# ─── Constants verification tests ───────────────────────────────────────


class TestConstants(unittest.TestCase):

    def test_lane_statuses_six(self):
        expected = {"VALID", "INVALID_PROTOCOL", "INCONCLUSIVE",
                    "MISSING", "JUDGE_DISAGREEMENT", "CONTAMINATED"}
        self.assertEqual(AU_LANE_STATUSES, expected)

    def test_causal_eligibility_six(self):
        expected = {"ELIGIBLE", "PROCESS_ONLY", "RESULT_ONLY",
                    "CONTAMINATED", "INVALID", "INCONCLUSIVE"}
        self.assertEqual(AU_CAUSAL_ELIGIBILITY_STATUSES, expected)

    def test_run_audit_states(self):
        expected = {"PENDING", "ASSEMBLED", "INCOMPLETE"}
        self.assertEqual(AU_RUN_AUDIT_STATES, expected)

    def test_lane_transitions_pending_to_all(self):
        self.assertEqual(AU_LANE_TRANSITIONS["PENDING"], AU_LANE_STATUSES)

    def test_lane_transitions_terminal_empty(self):
        for status in AU_LANE_STATUSES:
            self.assertEqual(AU_LANE_TRANSITIONS[status], frozenset())

    def test_causal_transitions_pending_to_all(self):
        self.assertEqual(AU_CAUSAL_ELIGIBILITY_TRANSITIONS["PENDING"], AU_CAUSAL_ELIGIBILITY_STATUSES)

    def test_causal_transitions_terminal_empty(self):
        for status in AU_CAUSAL_ELIGIBILITY_STATUSES:
            self.assertEqual(AU_CAUSAL_ELIGIBILITY_TRANSITIONS[status], frozenset())

    def test_check_ids_unique_and_ordered(self):
        self.assertEqual(len(AU_CHECK_IDS), len(set(AU_CHECK_IDS)))
        self.assertEqual(len(AU_CHECK_IDS), 20)

    def test_claims_unique(self):
        self.assertEqual(len(AU_CLAIMS), len(set(AU_CLAIMS)))

    def test_nonclaims_unique(self):
        self.assertEqual(len(AU_NONCLAIMS), len(set(AU_NONCLAIMS)))

    def test_side_effect_keys(self):
        expected = ("database_writes", "redis_writes", "d_volume_writes",
                    "solver_launches", "model_live_calls", "human_gate_commits")
        self.assertEqual(AU_SIDE_EFFECT_KEYS, expected)

    def test_lane_priority_keys_match_statuses(self):
        self.assertEqual(set(AU_LANE_PRIORITY.keys()), AU_LANE_STATUSES)

    def test_lane_terminal_statuses_match(self):
        self.assertEqual(AU_LANE_TERMINAL_STATUSES, AU_LANE_STATUSES)

    def test_au_error_codes_exist(self):
        # Verify all required error codes exist
        required = [
            EC.AU_ARM_LEAKED_INTO_VIEW,
            EC.AU_JUDGE_CONCLUSION_CROSS_READ,
            EC.AU_RESTATE_AS_ACTION,
            EC.AU_DISAGREEMENT_AUTO_RESOLVED,
            EC.AU_MISSING_NOT_TERMINAL,
            EC.AU_CONTAMINATION_NOT_FLAGGED,
            EC.AU_AUDIT_NOT_SEALED_SEPARATELY,
            EC.AU_PROCESS_ONLY_IN_RESULT_LAYER,
            EC.AU_VIEW_HASH_MISMATCH,
            EC.AU_AUDIT_PLAN_NOT_FROZEN,
            EC.AU_AUDIT_PLAN_MODIFIED,
            EC.AU_BLINDING_INVALID,
            EC.AU_SEAL_HASH_MISMATCH,
            EC.AU_RUN_AUDIT_INCOMPLETE,
            EC.AU_LANE_STATUS_INVALID,
            EC.AU_CAUSAL_ELIGIBILITY_INVALID,
            EC.AU_INDEPENDENCE_VIOLATED,
        ]
        for ec in required:
            self.assertIsNotNone(ec.value)

    def test_au_error_codes_are_strings(self):
        for ec in [
            EC.AU_ARM_LEAKED_INTO_VIEW, EC.AU_JUDGE_CONCLUSION_CROSS_READ,
            EC.AU_RESTATE_AS_ACTION, EC.AU_DISAGREEMENT_AUTO_RESOLVED,
            EC.AU_MISSING_NOT_TERMINAL, EC.AU_CONTAMINATION_NOT_FLAGGED,
            EC.AU_AUDIT_NOT_SEALED_SEPARATELY, EC.AU_PROCESS_ONLY_IN_RESULT_LAYER,
        ]:
            self.assertIsInstance(ec.value, str)
            self.assertTrue(ec.value.startswith("AU_"))


# ─── Negative blocker tests ─────────────────────────────────────────────


class TestBlockers(unittest.TestCase):
    """所有 blocker test——这些违规必须被检测到。"""

    def test_blocker_arm_leaked_into_view(self):
        """真 arm 泄漏 → BLOCK"""
        view = BlindedView(
            view_id="v1", view_kind="process_auditor_view",
            role_type_id="process_auditor",
            source_bundle_ref={"bundle_id": "b1", "content_hash": _ZERO_HASH},
            redacted_payload={"arm_id": "arm-secret", "data": "x"},
            view_hash="x", source_hash=_ZERO_HASH,
        )
        result = verify_blinded_view(view)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_ARM_LEAKED_INTO_VIEW, result.error_codes)

    def test_blocker_judge_cross_read(self):
        """Judge A 看到 Judge B 结论 → BLOCK"""
        j = make_proof_judgment(
            judgment_id="pj-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            math_correctness={"other_judge_conclusion": "CORRECT"},
            sealed=True,
        )
        result = verify_proof_judgment(j)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_JUDGE_CONCLUSION_CROSS_READ, result.error_codes)

    def test_blocker_restate_as_action(self):
        """复述当 action → BLOCK"""
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            action_analysis={"actions": [
                {"kind": "restate", "is_restate": True, "counted_as_action": True},
            ]},
            sealed=True,
        )
        result = verify_process_audit(audit)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_RESTATE_AS_ACTION, result.error_codes)

    def test_blocker_disagreement_auto_resolved(self):
        """分歧自选 → BLOCK"""
        from seven_system.audit.run_audit import DisagreementResolution
        dr = DisagreementResolution(
            disagreement_id="d-1", plan_id="plan-1",
            judge_conclusions={"j1": "CORRECT", "j2": "INCORRECT"},
            is_disagreement=True, resolution="PRESERVED",
            auto_resolved=True, recorded=True,
        )
        result = verify_disagreement_resolution(dr)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_DISAGREEMENT_AUTO_RESOLVED, result.error_codes)

    def test_blocker_missing_not_terminal(self):
        """缺失审计未记为 MISSING terminal → BLOCK"""
        # 构造一个 lane_statuses 中缺失 lane 没有记为 MISSING 的 RunAudit
        ra = make_run_audit(
            run_audit_id="ra-1", plan_id="plan-1",
            bundle_ref={"bundle_id": "b1", "content_hash": _ZERO_HASH},
            process_audit_ref={"audit_id": "pa-1", "content_hash": _ZERO_HASH},
            proof_judgment_ref={"judgment_id": "pj-1", "content_hash": _ZERO_HASH},
            leakage_audit_ref={"audit_id": "la-1", "content_hash": _ZERO_HASH},
            lane_statuses={
                "process_auditor": "VALID",
                "proof_judge": "VALID",
                # leakage_auditor missing entirely
            },
            causal_eligibility="INCONCLUSIVE",
        )
        result = verify_run_audit(ra)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_LANE_STATUS_INVALID, result.error_codes)

    def test_blocker_contamination_not_flagged(self):
        """污染未标记 → BLOCK"""
        audit = make_leakage_audit(
            audit_id="la-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            solver_payload_analysis={"contamination_detected": True},
            contamination_flagged=False,
            sealed=True,
        )
        result = verify_leakage_audit(audit)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_CONTAMINATION_NOT_FLAGGED, result.error_codes)

    def test_blocker_audit_not_sealed_separately(self):
        """审计未分别 seal → BLOCK"""
        audit = make_process_audit(
            audit_id="pa-1", plan_id="plan-1",
            view_ref={"view_id": "v1", "view_hash": _ZERO_HASH},
            sealed=False,
        )
        result = verify_process_audit(audit)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_NOT_SEALED_SEPARATELY, result.error_codes)

    def test_blocker_process_only_in_result_layer(self):
        """process-only 进入 result-layer → BLOCK"""
        ra = make_run_audit(
            run_audit_id="ra-1", plan_id="plan-1",
            bundle_ref={"bundle_id": "b1", "content_hash": _ZERO_HASH},
            process_audit_ref={"audit_id": "pa-1", "content_hash": _ZERO_HASH},
            proof_judgment_ref={"judgment_id": "pj-1", "content_hash": _ZERO_HASH},
            leakage_audit_ref={"audit_id": "la-1", "content_hash": _ZERO_HASH},
            lane_statuses={
                "process_auditor": "MISSING",
                "proof_judge": "VALID",
                "leakage_auditor": "VALID",
            },
            causal_eligibility="ELIGIBLE",  # claims eligible but process missing
        )
        result = verify_run_audit(ra)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_PROCESS_ONLY_IN_RESULT_LAYER, result.error_codes)

    def test_blocker_plan_not_frozen(self):
        """审计计划未冻结 → BLOCK"""
        from seven_system.audit.audit_plan import AuditPlan
        plan = AuditPlan(plan_id="x", state="DRAFT")
        result = verify_audit_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_PLAN_NOT_FROZEN, result.error_codes)

    def test_blocker_plan_hash_mismatch(self):
        """审计计划哈希不匹配 → BLOCK"""
        import dataclasses
        plan = _make_audit_plan()
        tampered = dataclasses.replace(plan, content_hash="wrong")
        result = verify_audit_plan(tampered)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_AUDIT_PLAN_MODIFIED, result.error_codes)

    def test_blocker_view_hash_mismatch(self):
        """view hash 不匹配 → BLOCK"""
        view = BlindedView(
            view_id="v1", view_kind="process_auditor_view",
            role_type_id="process_auditor",
            source_bundle_ref={"bundle_id": "b1", "content_hash": _ZERO_HASH},
            redacted_payload={"data": "x"},
            view_hash="wrong", source_hash=_ZERO_HASH,
        )
        result = verify_blinded_view(view)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_VIEW_HASH_MISMATCH, result.error_codes)

    def test_blocker_independence_violated(self):
        """独立性违规 → BLOCK"""
        bindings = _make_role_bindings()
        bindings[1] = AuditRoleBinding(
            role_type_id="proof_judge", adapter_id="codex", model_uid="gpt-5.6-sol",
            carrier_id="codex", carrier_profile_hash=_profile_hash("gpt-5.6-sol", "codex"),
            view_kind="proof_judge_view", independence_kind="DIFFERENT_SESSION",
            session_id="sess-process-001",
        )
        plan = make_audit_plan(
            plan_id="x",
            run_refs=[{"bundle_id": "b1", "content_hash": _ZERO_HASH}],
            role_bindings=bindings,
        )
        result = verify_audit_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_INDEPENDENCE_VIOLATED, result.error_codes)

    def test_blocker_blinding_invalid_view_kind(self):
        """盲化 view_kind 无效 → BLOCK"""
        bindings = _make_role_bindings()
        bindings[0] = AuditRoleBinding(
            role_type_id="process_auditor", adapter_id="devin", model_uid="glm-5-2",
            carrier_id="devin", carrier_profile_hash=_profile_hash(),
            view_kind="invalid_view_kind",  # invalid
            session_id="s1",
        )
        plan = make_audit_plan(
            plan_id="x",
            run_refs=[{"bundle_id": "b1", "content_hash": _ZERO_HASH}],
            role_bindings=bindings,
        )
        result = verify_audit_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.AU_BLINDING_INVALID, result.error_codes)


if __name__ == "__main__":
    unittest.main()
