"""WP-VR1 P9 Verdict/Replay 测试。

测试层级：VerdictRuleRegistry → MachineVerdict → SixGateVerdict →
          EvidenceIndex → RuntimeCheckpoint → EvidenceReplay →
          CompletionContractRemainder → FullChainRemainder →
          CostAndCoverageDelta → HumanReadableSummary →
          VerdictBuilder → VerdictCapabilityReport →
          Negative → Determinism → Boundary → Constants

覆盖：
- Golden path: sealed P0-P8 DAG → VerdictBuilder → 全套 P9 产物
- VerdictRuleRegistry tests (all status combinations, fail-closed for unknown)
- Evidence replay tests (all objects have legal destination, no orphans)
- Completion contract remainder=0 tests
- Full chain remainder=0 tests
- Negative: PASS averaged FAIL, NOT_TESTED as PASS, orphan object,
  non-retraceable, owner/contract mismatch, EvidenceIndex before P9,
  remainder != 0, unknown verdict rule not fail-closed
- Cost and coverage delta tests
- Deterministic hash tests
- VR1 boundary tests (allowed/forbidden output kinds)
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
    VR_ALLOWED_OUTPUT_KINDS,
    VR_CHECK_IDS,
    VR_CLAIMS,
    VR_FORBIDDEN_OUTPUT_KINDS,
    VR_GATE_KINDS,
    VR_GATE_STATUSES,
    VR_NONCLAIMS,
    VR_REMAINDER_KINDS,
    VR_REPLAY_STATUSES,
    VR_SIDE_EFFECT_KEYS,
    VR_VERDICT_AXES,
    VR_VERDICT_RULE_STATUSES,
    VR_VERDICT_STATUSES,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.verdict.rule_registry import (
    VerdictRuleRegistry,
    make_verdict_rule_registry,
    lookup_verdict_rule,
    verify_verdict_rule_registry,
    check_not_tested_not_pass as check_registry_not_tested_not_pass,
    check_fail_closed_unknown,
)
from seven_system.verdict.machine_verdict import (
    AxisVerdict,
    MachineVerdict,
    make_machine_verdict,
    verify_machine_verdict,
    check_no_pass_averaged_fail,
    check_not_tested_not_pass as check_verdict_not_tested_not_pass,
)
from seven_system.verdict.six_gate import (
    GateVerdict,
    SixGateVerdict,
    make_six_gate_verdict,
    verify_six_gate_verdict,
    check_gate_not_tested_not_pass,
)
from seven_system.verdict.evidence_index import (
    EvidenceEntry,
    EvidenceIndex,
    make_evidence_index,
    verify_evidence_index,
    check_evidence_index_in_p9,
    check_retraceable,
)
from seven_system.verdict.checkpoint import (
    VerdictCheckpoint,
    make_verdict_checkpoint,
    verify_verdict_checkpoint,
    verify_checkpoint_against_hashes,
    CHECKPOINT_STATES,
)
from seven_system.verdict.replay import (
    ReplayObject,
    ReplayResult,
    EvidenceReplay,
    make_evidence_replay,
    verify_evidence_replay,
    check_no_orphans,
    WorkPackageCompletion,
    CompletionContractRemainder,
    make_completion_contract_remainder,
    verify_completion_contract_remainder,
    PhaseSealStatus,
    FullChainRemainder,
    make_full_chain_remainder,
    verify_full_chain_remainder,
)
from seven_system.verdict.cost_coverage import (
    CostAggregation,
    CoverageCell,
    CostAndCoverageDelta,
    make_cost_and_coverage_delta,
    verify_cost_and_coverage_delta,
)
from seven_system.verdict.summary import (
    HumanReadableSummary,
    make_human_readable_summary,
    verify_human_readable_summary,
)
from seven_system.verdict.builder import (
    SealedDAG,
    VerdictBuilder,
    VerdictBuildResult,
)
from seven_system.verdict.capability_report import (
    VerdictCapabilityReportError,
    build_verdict_capability_report,
    verify_verdict_capability_report,
    VERDICT_REPORT_SCHEMA_VERSION,
    VERDICT_REPORT_SCOPE,
)


# ─── Test fixtures ───────────────────────────────────────────────────────


def _make_test_dag_hash() -> str:
    """生成测试用 DAG hash。"""
    return hashlib.sha256(b"test-dag-p0-p8-sealed").hexdigest()


def _make_test_evidence_hash(seed: str) -> str:
    """生成测试用 evidence hash。"""
    return hashlib.sha256(f"evidence-{seed}".encode()).hexdigest()


def _make_sealed_dag() -> SealedDAG:
    """构建测试用 sealed P0-P8 DAG。"""
    dag_hash = _make_test_dag_hash()
    work_packages = [
        {
            "wp_id": "WP-DOC0",
            "owner_type": "IMPLEMENTER",
            "completion_contract": "DOC_BOOTSTRAP_RECORD",
            "state": "IMPLEMENTED_PENDING_EVIDENCE",
            "submitted_schema_id": "seven/docs/doc-bootstrap-completion-record",
            "actor_type": "IMPLEMENTER",
        },
        {
            "wp_id": "WP-GV0",
            "owner_type": "IMPLEMENTER",
            "completion_contract": "IMPLEMENTATION_BUNDLE",
            "state": "IMPLEMENTED_PENDING_EVIDENCE",
            "submitted_schema_id": "seven/implementation-completion-bundle",
            "actor_type": "IMPLEMENTER",
        },
        {
            "wp_id": "WP-EV1",
            "owner_type": "IMPLEMENTER",
            "completion_contract": "IMPLEMENTATION_BUNDLE",
            "state": "IMPLEMENTED_PENDING_EVIDENCE",
            "submitted_schema_id": "seven/implementation-completion-bundle",
            "actor_type": "IMPLEMENTER",
        },
    ]
    phase_seals = {
        "P0": True, "P1": True, "P2": True, "P3": True,
        "P4": True, "P5": True, "P6": True, "P7": True, "P8": True,
    }
    evidence_records = [
        {"hash": _make_test_evidence_hash("ev1"), "phase": "P7", "wp_id": "WP-EV1"},
        {"hash": _make_test_evidence_hash("ev2"), "phase": "P7", "wp_id": "WP-EV1"},
    ]
    run_audits = [
        {"hash": _make_test_evidence_hash("au1"), "phase": "P6", "wp_id": "WP-AU1"},
    ]
    run_artifact_bundles = [
        {"hash": _make_test_evidence_hash("ex1"), "phase": "P5", "wp_id": "WP-EX1"},
    ]
    gate_statuses = {
        "G_P0_READINESS": "PASS",
        "G_P1_DRYRUN": "PASS",
        "G_P2_CANDIDATE": "PASS",
        "G_P3_QUESTION": "PASS",
        "G_P4_PLAN": "PASS",
        "G_P5_RUN": "PASS",
    }
    return SealedDAG(
        dag_hash=dag_hash,
        work_packages=work_packages,
        phase_seals=phase_seals,
        evidence_records=evidence_records,
        run_audits=run_audits,
        run_artifact_bundles=run_artifact_bundles,
        gate_statuses=gate_statuses,
    )


# ─── VerdictRuleRegistry tests ───────────────────────────────────────────


class TestVerdictRuleRegistry(unittest.TestCase):
    """VerdictRuleRegistry 测试。"""

    def test_make_registry(self):
        registry = make_verdict_rule_registry()
        self.assertIsInstance(registry, VerdictRuleRegistry)
        self.assertTrue(registry.is_frozen)
        self.assertTrue(registry.is_hash_valid)

    def test_verify_registry_pass(self):
        registry = make_verdict_rule_registry()
        result = verify_verdict_rule_registry(registry)
        self.assertTrue(result.passed, f"Registry verification failed: {result.details}")

    def test_all_evidence_statuses_mapped(self):
        """所有已知 evidence status 都在规则表中。"""
        registry = make_verdict_rule_registry()
        table = registry.to_dict()["rule_table"]
        from seven_system.contracts.errors import EV_EVIDENCE_STATUSES
        for status in EV_EVIDENCE_STATUSES:
            self.assertIn(status, table, f"status {status} missing from rule table")

    def test_lookup_supports(self):
        registry = make_verdict_rule_registry()
        result = lookup_verdict_rule(registry, "SUPPORTS")
        self.assertEqual(result["FACTORY"], "PASS")
        self.assertEqual(result["SCIENTIFIC"], "PASS")
        self.assertEqual(result["SCALE"], "NOT_TESTED")

    def test_lookup_contradicts(self):
        registry = make_verdict_rule_registry()
        result = lookup_verdict_rule(registry, "CONTRADICTS")
        self.assertEqual(result["FACTORY"], "PASS")
        self.assertEqual(result["SCIENTIFIC"], "FAIL")
        self.assertEqual(result["SCALE"], "NOT_TESTED")

    def test_lookup_not_tested(self):
        """NOT_TESTED 不得映射为 PASS。"""
        registry = make_verdict_rule_registry()
        result = lookup_verdict_rule(registry, "NOT_TESTED")
        for axis in VR_VERDICT_AXES:
            self.assertNotEqual(result[axis], "PASS",
                                f"NOT_TESTED mapped to PASS for {axis}")
            self.assertEqual(result[axis], "NOT_TESTED")

    def test_fail_closed_unknown(self):
        """未知组合 fail-closed → BLOCKED。"""
        registry = make_verdict_rule_registry()
        result = lookup_verdict_rule(registry, "__UNKNOWN_STATUS__")
        for axis in VR_VERDICT_AXES:
            self.assertEqual(result[axis], "BLOCKED",
                             f"unknown status not fail-closed for {axis}")

    def test_check_fail_closed_unknown(self):
        registry = make_verdict_rule_registry()
        result = check_fail_closed_unknown(registry)
        self.assertTrue(result.passed)

    def test_check_not_tested_not_pass(self):
        registry = make_verdict_rule_registry()
        result = check_registry_not_tested_not_pass(registry)
        self.assertTrue(result.passed)

    def test_registry_hash_deterministic(self):
        """registry hash 确定性。"""
        r1 = make_verdict_rule_registry()
        r2 = make_verdict_rule_registry()
        self.assertEqual(r1.registry_hash, r2.registry_hash)

    def test_registry_hash_tamper_detected(self):
        """registry hash 篡改被检测。"""
        registry = make_verdict_rule_registry()
        tampered = dataclasses.replace(registry, registry_hash="tampered")
        result = verify_verdict_rule_registry(tampered)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_VERDICT_HASH_MISMATCH, result.error_codes)


# ─── MachineVerdict tests ────────────────────────────────────────────────


class TestMachineVerdict(unittest.TestCase):
    """MachineVerdict 分轴测试。"""

    def test_make_verdict_all_pass(self):
        dag_hash = _make_test_dag_hash()
        verdict = make_machine_verdict(
            verdict_id="mv-001",
            dag_hash=dag_hash,
            factory_status="PASS",
            scientific_status="PASS",
            scale_status="PASS",
        )
        self.assertEqual(verdict.overall_status, "PASS")
        self.assertTrue(verdict.is_hash_valid)

    def test_verify_verdict_all_pass(self):
        dag_hash = _make_test_dag_hash()
        verdict = make_machine_verdict(
            verdict_id="mv-001",
            dag_hash=dag_hash,
            factory_status="PASS",
            scientific_status="PASS",
            scale_status="PASS",
        )
        result = verify_machine_verdict(verdict)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_three_axes_present(self):
        """三轴必须都存在。"""
        dag_hash = _make_test_dag_hash()
        verdict = make_machine_verdict(
            verdict_id="mv-001",
            dag_hash=dag_hash,
            factory_status="PASS",
            scientific_status="PASS",
            scale_status="NOT_TESTED",
        )
        axes = {ax.axis for ax in verdict.axes}
        self.assertEqual(axes, VR_VERDICT_AXES)

    def test_factory_scientific_separate(self):
        """Factory 和 Scientific 分轴独立。"""
        dag_hash = _make_test_dag_hash()
        verdict = make_machine_verdict(
            verdict_id="mv-001",
            dag_hash=dag_hash,
            factory_status="PASS",
            scientific_status="FAIL",
            scale_status="NOT_TESTED",
        )
        factory = verdict.get_axis("FACTORY")
        scientific = verdict.get_axis("SCIENTIFIC")
        self.assertEqual(factory.status, "PASS")
        self.assertEqual(scientific.status, "FAIL")

    def test_overall_takes_strictest(self):
        """overall_status 取最严状态。"""
        dag_hash = _make_test_dag_hash()
        verdict = make_machine_verdict(
            verdict_id="mv-001",
            dag_hash=dag_hash,
            factory_status="PASS",
            scientific_status="FAIL",
            scale_status="NOT_TESTED",
        )
        self.assertEqual(verdict.overall_status, "FAIL")

    def test_negative_pass_averaged_fail(self):
        """BLOCKER: factory PASS + scientific FAIL averaged to PASS。"""
        dag_hash = _make_test_dag_hash()
        # 手动构造 overall=PASS 但有 FAIL 轴
        verdict = MachineVerdict(
            verdict_id="mv-bad",
            dag_hash=dag_hash,
            axes=(
                AxisVerdict(axis="FACTORY", status="PASS"),
                AxisVerdict(axis="SCIENTIFIC", status="FAIL"),
                AxisVerdict(axis="SCALE", status="PASS"),
            ),
            overall_status="PASS",  # 错误：平均了
            content_hash="",
        )
        # 重新计算 hash（因为手动构造）
        verdict = dataclasses.replace(
            verdict, content_hash=verdict.compute_content_hash()
        )
        result = verify_machine_verdict(verdict)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_PASS_AVERAGED_FAIL, result.error_codes)

    def test_check_no_pass_averaged_fail(self):
        dag_hash = _make_test_dag_hash()
        verdict = MachineVerdict(
            verdict_id="mv-bad",
            dag_hash=dag_hash,
            axes=(
                AxisVerdict(axis="FACTORY", status="PASS"),
                AxisVerdict(axis="SCIENTIFIC", status="FAIL"),
                AxisVerdict(axis="SCALE", status="PASS"),
            ),
            overall_status="PASS",
            content_hash="",
        )
        verdict = dataclasses.replace(
            verdict, content_hash=verdict.compute_content_hash()
        )
        result = check_no_pass_averaged_fail(verdict)
        self.assertFalse(result.passed)

    def test_negative_not_tested_as_pass(self):
        """BLOCKER: NOT_TESTED treated as PASS。"""
        dag_hash = _make_test_dag_hash()
        verdict = MachineVerdict(
            verdict_id="mv-bad",
            dag_hash=dag_hash,
            axes=(
                AxisVerdict(axis="FACTORY", status="PASS"),
                AxisVerdict(axis="SCIENTIFIC", status="PASS"),
                AxisVerdict(axis="SCALE", status="NOT_TESTED"),
            ),
            overall_status="PASS",  # 错误：NOT_TESTED 当 PASS
            content_hash="",
        )
        verdict = dataclasses.replace(
            verdict, content_hash=verdict.compute_content_hash()
        )
        result = verify_machine_verdict(verdict)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_NOT_TESTED_AS_PASS, result.error_codes)

    def test_check_not_tested_not_pass(self):
        dag_hash = _make_test_dag_hash()
        verdict = MachineVerdict(
            verdict_id="mv-bad",
            dag_hash=dag_hash,
            axes=(
                AxisVerdict(axis="FACTORY", status="PASS"),
                AxisVerdict(axis="SCIENTIFIC", status="PASS"),
                AxisVerdict(axis="SCALE", status="NOT_TESTED"),
            ),
            overall_status="PASS",
            content_hash="",
        )
        verdict = dataclasses.replace(
            verdict, content_hash=verdict.compute_content_hash()
        )
        result = check_verdict_not_tested_not_pass(verdict)
        self.assertFalse(result.passed)

    def test_verdict_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        v1 = make_machine_verdict(
            verdict_id="mv-001", dag_hash=dag_hash,
            factory_status="PASS", scientific_status="PASS", scale_status="PASS",
        )
        v2 = make_machine_verdict(
            verdict_id="mv-001", dag_hash=dag_hash,
            factory_status="PASS", scientific_status="PASS", scale_status="PASS",
        )
        self.assertEqual(v1.content_hash, v2.content_hash)

    def test_negative_invalid_axis(self):
        """BLOCKER: 轴不在合法集合。"""
        dag_hash = _make_test_dag_hash()
        verdict = MachineVerdict(
            verdict_id="mv-bad",
            dag_hash=dag_hash,
            axes=(
                AxisVerdict(axis="FACTORY", status="PASS"),
                AxisVerdict(axis="SCIENTIFIC", status="PASS"),
                AxisVerdict(axis="INVALID_AXIS", status="PASS"),
            ),
            overall_status="PASS",
            content_hash="",
        )
        verdict = dataclasses.replace(
            verdict, content_hash=verdict.compute_content_hash()
        )
        result = verify_machine_verdict(verdict)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_AXIS_INVALID, result.error_codes)


# ─── SixGateVerdict tests ────────────────────────────────────────────────


class TestSixGateVerdict(unittest.TestCase):
    """SixGateVerdict 六门测试。"""

    def test_make_gate_verdict(self):
        dag_hash = _make_test_dag_hash()
        gate_statuses = {kind: "PASS" for kind in VR_GATE_KINDS}
        verdict = make_six_gate_verdict(
            verdict_id="gv-001",
            dag_hash=dag_hash,
            gate_statuses=gate_statuses,
        )
        self.assertEqual(verdict.overall_status, "PASS")
        self.assertTrue(verdict.is_hash_valid)

    def test_verify_gate_verdict_pass(self):
        dag_hash = _make_test_dag_hash()
        gate_statuses = {kind: "PASS" for kind in VR_GATE_KINDS}
        verdict = make_six_gate_verdict(
            verdict_id="gv-001", dag_hash=dag_hash, gate_statuses=gate_statuses,
        )
        result = verify_six_gate_verdict(verdict)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_six_gates_present(self):
        dag_hash = _make_test_dag_hash()
        gate_statuses = {kind: "PASS" for kind in VR_GATE_KINDS}
        verdict = make_six_gate_verdict(
            verdict_id="gv-001", dag_hash=dag_hash, gate_statuses=gate_statuses,
        )
        gate_kinds = {g.gate_kind for g in verdict.gates}
        self.assertEqual(gate_kinds, VR_GATE_KINDS)

    def test_gates_independent(self):
        """每门独立评估。"""
        dag_hash = _make_test_dag_hash()
        gate_statuses = {
            "G_P0_READINESS": "PASS",
            "G_P1_DRYRUN": "PASS",
            "G_P2_CANDIDATE": "FAIL",
            "G_P3_QUESTION": "PASS",
            "G_P4_PLAN": "PASS",
            "G_P5_RUN": "PASS",
        }
        verdict = make_six_gate_verdict(
            verdict_id="gv-001", dag_hash=dag_hash, gate_statuses=gate_statuses,
        )
        self.assertEqual(verdict.get_gate("G_P2_CANDIDATE").status, "FAIL")
        self.assertEqual(verdict.get_gate("G_P0_READINESS").status, "PASS")
        self.assertEqual(verdict.overall_status, "FAIL")

    def test_negative_not_tested_as_pass(self):
        """BLOCKER: NOT_TESTED gate treated as PASS。"""
        dag_hash = _make_test_dag_hash()
        verdict = SixGateVerdict(
            verdict_id="gv-bad",
            dag_hash=dag_hash,
            gates=(
                GateVerdict(gate_kind="G_P0_READINESS", status="PASS"),
                GateVerdict(gate_kind="G_P1_DRYRUN", status="PASS"),
                GateVerdict(gate_kind="G_P2_CANDIDATE", status="PASS"),
                GateVerdict(gate_kind="G_P3_QUESTION", status="PASS"),
                GateVerdict(gate_kind="G_P4_PLAN", status="PASS"),
                GateVerdict(gate_kind="G_P5_RUN", status="NOT_TESTED"),
            ),
            overall_status="PASS",
            content_hash="",
        )
        verdict = dataclasses.replace(
            verdict, content_hash=verdict.compute_content_hash()
        )
        result = verify_six_gate_verdict(verdict)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_NOT_TESTED_AS_PASS, result.error_codes)

    def test_check_gate_not_tested_not_pass(self):
        dag_hash = _make_test_dag_hash()
        verdict = SixGateVerdict(
            verdict_id="gv-bad",
            dag_hash=dag_hash,
            gates=(
                GateVerdict(gate_kind="G_P0_READINESS", status="PASS"),
                GateVerdict(gate_kind="G_P1_DRYRUN", status="PASS"),
                GateVerdict(gate_kind="G_P2_CANDIDATE", status="PASS"),
                GateVerdict(gate_kind="G_P3_QUESTION", status="PASS"),
                GateVerdict(gate_kind="G_P4_PLAN", status="PASS"),
                GateVerdict(gate_kind="G_P5_RUN", status="NOT_TESTED"),
            ),
            overall_status="PASS",
            content_hash="",
        )
        verdict = dataclasses.replace(
            verdict, content_hash=verdict.compute_content_hash()
        )
        result = check_gate_not_tested_not_pass(verdict)
        self.assertFalse(result.passed)

    def test_negative_invalid_gate(self):
        """BLOCKER: 门不在合法集合。"""
        dag_hash = _make_test_dag_hash()
        verdict = SixGateVerdict(
            verdict_id="gv-bad",
            dag_hash=dag_hash,
            gates=(
                GateVerdict(gate_kind="G_P0_READINESS", status="PASS"),
                GateVerdict(gate_kind="G_P1_DRYRUN", status="PASS"),
                GateVerdict(gate_kind="G_P2_CANDIDATE", status="PASS"),
                GateVerdict(gate_kind="G_P3_QUESTION", status="PASS"),
                GateVerdict(gate_kind="G_P4_PLAN", status="PASS"),
                GateVerdict(gate_kind="INVALID_GATE", status="PASS"),
            ),
            overall_status="PASS",
            content_hash="",
        )
        verdict = dataclasses.replace(
            verdict, content_hash=verdict.compute_content_hash()
        )
        result = verify_six_gate_verdict(verdict)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_GATE_INVALID, result.error_codes)

    def test_gate_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        gate_statuses = {kind: "PASS" for kind in VR_GATE_KINDS}
        v1 = make_six_gate_verdict(
            verdict_id="gv-001", dag_hash=dag_hash, gate_statuses=gate_statuses,
        )
        v2 = make_six_gate_verdict(
            verdict_id="gv-001", dag_hash=dag_hash, gate_statuses=gate_statuses,
        )
        self.assertEqual(v1.content_hash, v2.content_hash)


# ─── EvidenceIndex tests ─────────────────────────────────────────────────


class TestEvidenceIndex(unittest.TestCase):
    """EvidenceIndex 测试。"""

    def test_make_evidence_index(self):
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        entries = [
            EvidenceEntry(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                phase="P7",
                wp_id="WP-EV1",
            ),
            EvidenceEntry(
                object_kind="RunAudit",
                object_hash=_make_test_evidence_hash("au1"),
                phase="P6",
                wp_id="WP-AU1",
            ),
        ]
        index = make_evidence_index(
            index_id="ei-001",
            dag_hash=dag_hash,
            verdict_hash=verdict_hash,
            entries=entries,
        )
        self.assertTrue(index.is_hash_valid)
        self.assertEqual(index.entry_count, 2)

    def test_verify_evidence_index_pass(self):
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        entries = [
            EvidenceEntry(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                phase="P7",
            ),
        ]
        index = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
        )
        result = verify_evidence_index(index)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_generated_in_p9(self):
        """EvidenceIndex 必须在 P9 生成。"""
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        entries = [
            EvidenceEntry(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                phase="P7",
            ),
        ]
        index = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
        )
        result = check_evidence_index_in_p9(index)
        self.assertTrue(result.passed)

    def test_negative_evidence_index_before_p9(self):
        """BLOCKER: EvidenceIndex generated before P9。"""
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        entries = [
            EvidenceEntry(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                phase="P7",
            ),
        ]
        index = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
            generated_in_phase="P7",  # 错误：在 P7 生成
        )
        result = verify_evidence_index(index)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_EVIDENCE_INDEX_BEFORE_P9, result.error_codes)

    def test_check_evidence_index_in_p9_negative(self):
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        entries = [
            EvidenceEntry(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                phase="P7",
            ),
        ]
        index = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
            generated_in_phase="P8",
        )
        result = check_evidence_index_in_p9(index)
        self.assertFalse(result.passed)

    def test_retraceable(self):
        """evidence 可从 verdict 反查。"""
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        ev_hash = _make_test_evidence_hash("ev1")
        entries = [
            EvidenceEntry(
                object_kind="EvidenceRecord",
                object_hash=ev_hash,
                phase="P7",
            ),
        ]
        index = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
        )
        result = check_retraceable(index, ev_hash)
        self.assertTrue(result.passed)

    def test_negative_non_retraceable(self):
        """BLOCKER: evidence cannot be traced back from verdict。"""
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        entries = [
            EvidenceEntry(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                phase="P7",
            ),
        ]
        index = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
        )
        unknown_hash = _make_test_evidence_hash("unknown")
        result = check_retraceable(index, unknown_hash)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_NON_RETRACEABLE, result.error_codes)

    def test_negative_duplicate_hash(self):
        """BLOCKER: EvidenceIndex 重复 hash。"""
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        ev_hash = _make_test_evidence_hash("ev1")
        entries = [
            EvidenceEntry(object_kind="EvidenceRecord", object_hash=ev_hash, phase="P7"),
            EvidenceEntry(object_kind="RunAudit", object_hash=ev_hash, phase="P6"),
        ]
        index = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
        )
        result = verify_evidence_index(index)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_DUPLICATE_OBJECT, result.error_codes)

    def test_index_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        verdict_hash = _make_test_evidence_hash("verdict")
        entries = [
            EvidenceEntry(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                phase="P7",
            ),
        ]
        i1 = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
        )
        i2 = make_evidence_index(
            index_id="ei-001", dag_hash=dag_hash,
            verdict_hash=verdict_hash, entries=entries,
        )
        self.assertEqual(i1.content_hash, i2.content_hash)


# ─── RuntimeCheckpoint tests ─────────────────────────────────────────────


class TestVerdictCheckpoint(unittest.TestCase):
    """P9 RuntimeCheckpoint 测试。"""

    def test_make_checkpoint(self):
        dag_hash = _make_test_dag_hash()
        checkpoint = make_verdict_checkpoint(
            checkpoint_id="ck-001",
            dag_hash=dag_hash,
            verdict_hash=_make_test_evidence_hash("verdict"),
            gate_verdict_hash=_make_test_evidence_hash("gate"),
            evidence_index_hash=_make_test_evidence_hash("index"),
            replay_hash=_make_test_evidence_hash("replay"),
            state_snapshot={"P0": "SEALED", "P1": "SEALED"},
        )
        self.assertTrue(checkpoint.is_hash_valid)
        self.assertEqual(checkpoint.state, "RECORDED")

    def test_verify_checkpoint_pass(self):
        dag_hash = _make_test_dag_hash()
        checkpoint = make_verdict_checkpoint(
            checkpoint_id="ck-001",
            dag_hash=dag_hash,
            verdict_hash=_make_test_evidence_hash("verdict"),
            gate_verdict_hash=_make_test_evidence_hash("gate"),
            evidence_index_hash=_make_test_evidence_hash("index"),
            replay_hash=_make_test_evidence_hash("replay"),
        )
        result = verify_verdict_checkpoint(checkpoint)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_checkpoint_hash_mismatch(self):
        """BLOCKER: checkpoint hash mismatch。"""
        dag_hash = _make_test_dag_hash()
        checkpoint = make_verdict_checkpoint(
            checkpoint_id="ck-001",
            dag_hash=dag_hash,
            verdict_hash=_make_test_evidence_hash("verdict"),
            gate_verdict_hash=_make_test_evidence_hash("gate"),
            evidence_index_hash=_make_test_evidence_hash("index"),
            replay_hash=_make_test_evidence_hash("replay"),
        )
        tampered = dataclasses.replace(checkpoint, checkpoint_hash="tampered")
        result = verify_verdict_checkpoint(tampered)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_CHECKPOINT_HASH_MISMATCH, result.error_codes)

    def test_verify_checkpoint_against_hashes(self):
        """验证 checkpoint 与实际 hash 一致。"""
        dag_hash = _make_test_dag_hash()
        v_hash = _make_test_evidence_hash("verdict")
        g_hash = _make_test_evidence_hash("gate")
        ei_hash = _make_test_evidence_hash("index")
        r_hash = _make_test_evidence_hash("replay")
        checkpoint = make_verdict_checkpoint(
            checkpoint_id="ck-001",
            dag_hash=dag_hash,
            verdict_hash=v_hash,
            gate_verdict_hash=g_hash,
            evidence_index_hash=ei_hash,
            replay_hash=r_hash,
        )
        result = verify_checkpoint_against_hashes(
            checkpoint,
            verdict_hash=v_hash,
            gate_verdict_hash=g_hash,
            evidence_index_hash=ei_hash,
            replay_hash=r_hash,
            dag_hash=dag_hash,
        )
        self.assertTrue(result.passed)

    def test_verify_checkpoint_against_hashes_mismatch(self):
        """checkpoint hash 与实际不一致。"""
        dag_hash = _make_test_dag_hash()
        checkpoint = make_verdict_checkpoint(
            checkpoint_id="ck-001",
            dag_hash=dag_hash,
            verdict_hash=_make_test_evidence_hash("verdict"),
            gate_verdict_hash=_make_test_evidence_hash("gate"),
            evidence_index_hash=_make_test_evidence_hash("index"),
            replay_hash=_make_test_evidence_hash("replay"),
        )
        result = verify_checkpoint_against_hashes(
            checkpoint,
            verdict_hash=_make_test_evidence_hash("wrong"),
            gate_verdict_hash=_make_test_evidence_hash("gate"),
            evidence_index_hash=_make_test_evidence_hash("index"),
            replay_hash=_make_test_evidence_hash("replay"),
            dag_hash=dag_hash,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_CHECKPOINT_HASH_MISMATCH, result.error_codes)

    def test_checkpoint_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        kwargs = dict(
            checkpoint_id="ck-001",
            dag_hash=dag_hash,
            verdict_hash=_make_test_evidence_hash("verdict"),
            gate_verdict_hash=_make_test_evidence_hash("gate"),
            evidence_index_hash=_make_test_evidence_hash("index"),
            replay_hash=_make_test_evidence_hash("replay"),
            created_at="2026-01-01T00:00:00+00:00",
        )
        c1 = make_verdict_checkpoint(**kwargs)
        c2 = make_verdict_checkpoint(**kwargs)
        self.assertEqual(c1.checkpoint_hash, c2.checkpoint_hash)


# ─── EvidenceReplay tests ────────────────────────────────────────────────


class TestEvidenceReplay(unittest.TestCase):
    """EvidenceReplay 测试。"""

    def test_make_replay_all_placed(self):
        dag_hash = _make_test_dag_hash()
        objects = [
            ReplayObject(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                source_phase="P7",
                destination="EvidenceIndex",
            ),
            ReplayObject(
                object_kind="RunAudit",
                object_hash=_make_test_evidence_hash("au1"),
                source_phase="P6",
                destination="EvidenceIndex",
            ),
        ]
        replay = make_evidence_replay(
            replay_id="rp-001", dag_hash=dag_hash, objects=objects,
        )
        self.assertEqual(replay.placed_count, 2)
        self.assertEqual(replay.remainder, 0)
        self.assertTrue(replay.is_complete)

    def test_verify_replay_pass(self):
        dag_hash = _make_test_dag_hash()
        objects = [
            ReplayObject(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                source_phase="P7",
                destination="EvidenceIndex",
            ),
        ]
        replay = make_evidence_replay(
            replay_id="rp-001", dag_hash=dag_hash, objects=objects,
        )
        result = verify_evidence_replay(replay)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_negative_orphan_object(self):
        """BLOCKER: orphan object (no legal destination)。"""
        dag_hash = _make_test_dag_hash()
        objects = [
            ReplayObject(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                source_phase="P7",
                destination="InvalidDestination",  # 非法归宿
            ),
        ]
        replay = make_evidence_replay(
            replay_id="rp-001", dag_hash=dag_hash, objects=objects,
        )
        result = verify_evidence_replay(replay)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_ORPHAN_OBJECT, result.error_codes)
        self.assertIn(EC.VR_REPLAY_INCOMPLETE, result.error_codes)

    def test_check_no_orphans(self):
        dag_hash = _make_test_dag_hash()
        objects = [
            ReplayObject(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                source_phase="P7",
                destination="EvidenceIndex",
            ),
        ]
        replay = make_evidence_replay(
            replay_id="rp-001", dag_hash=dag_hash, objects=objects,
        )
        result = check_no_orphans(replay)
        self.assertTrue(result.passed)

    def test_check_no_orphans_negative(self):
        dag_hash = _make_test_dag_hash()
        objects = [
            ReplayObject(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                source_phase="P7",
                destination="InvalidDest",
            ),
        ]
        replay = make_evidence_replay(
            replay_id="rp-001", dag_hash=dag_hash, objects=objects,
        )
        result = check_no_orphans(replay)
        self.assertFalse(result.passed)

    def test_negative_duplicate_object(self):
        """BLOCKER: duplicate object。"""
        dag_hash = _make_test_dag_hash()
        ev_hash = _make_test_evidence_hash("ev1")
        objects = [
            ReplayObject(
                object_kind="EvidenceRecord",
                object_hash=ev_hash,
                source_phase="P7",
                destination="EvidenceIndex",
            ),
            ReplayObject(
                object_kind="RunAudit",
                object_hash=ev_hash,  # 重复 hash
                source_phase="P6",
                destination="EvidenceIndex",
            ),
        ]
        replay = make_evidence_replay(
            replay_id="rp-001", dag_hash=dag_hash, objects=objects,
        )
        result = verify_evidence_replay(replay)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_DUPLICATE_OBJECT, result.error_codes)

    def test_replay_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        objects = [
            ReplayObject(
                object_kind="EvidenceRecord",
                object_hash=_make_test_evidence_hash("ev1"),
                source_phase="P7",
                destination="EvidenceIndex",
            ),
        ]
        r1 = make_evidence_replay(
            replay_id="rp-001", dag_hash=dag_hash, objects=objects,
        )
        r2 = make_evidence_replay(
            replay_id="rp-001", dag_hash=dag_hash, objects=objects,
        )
        self.assertEqual(r1.content_hash, r2.content_hash)


# ─── CompletionContractRemainder tests ───────────────────────────────────


class TestCompletionContractRemainder(unittest.TestCase):
    """CompletionContractRemainder 测试。"""

    def test_make_remainder_zero(self):
        dag_hash = _make_test_dag_hash()
        wps = [
            WorkPackageCompletion(
                wp_id="WP-GV0",
                owner_type="IMPLEMENTER",
                completion_contract="IMPLEMENTATION_BUNDLE",
                state="IMPLEMENTED_PENDING_EVIDENCE",
                actor_type="IMPLEMENTER",
            ),
            WorkPackageCompletion(
                wp_id="WP-AU1",
                owner_type="AUDITOR",
                completion_contract="AUDIT_RECORD",
                state="READY_FOR_AUDIT",
                actor_type="AUDITOR",
            ),
        ]
        remainder = make_completion_contract_remainder(
            remainder_id="cc-001", dag_hash=dag_hash, wp_completions=wps,
        )
        self.assertTrue(remainder.is_zero)
        self.assertEqual(remainder.remainder, 0)

    def test_verify_remainder_zero_pass(self):
        dag_hash = _make_test_dag_hash()
        wps = [
            WorkPackageCompletion(
                wp_id="WP-GV0",
                owner_type="IMPLEMENTER",
                completion_contract="IMPLEMENTATION_BUNDLE",
                state="IMPLEMENTED_PENDING_EVIDENCE",
                actor_type="IMPLEMENTER",
            ),
        ]
        remainder = make_completion_contract_remainder(
            remainder_id="cc-001", dag_hash=dag_hash, wp_completions=wps,
        )
        result = verify_completion_contract_remainder(remainder)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_negative_remainder_nonzero(self):
        """BLOCKER: completion contract remainder != 0。"""
        dag_hash = _make_test_dag_hash()
        wps = [
            WorkPackageCompletion(
                wp_id="WP-GV0",
                owner_type="IMPLEMENTER",
                completion_contract="IMPLEMENTATION_BUNDLE",
                state="NOT_STARTED",  # 未完成
                actor_type="IMPLEMENTER",
            ),
        ]
        remainder = make_completion_contract_remainder(
            remainder_id="cc-001", dag_hash=dag_hash, wp_completions=wps,
        )
        result = verify_completion_contract_remainder(remainder)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_COMPLETION_CONTRACT_REMAINDER_NONZERO, result.error_codes)

    def test_negative_owner_contract_mismatch(self):
        """BLOCKER: owner/contract mismatch。"""
        dag_hash = _make_test_dag_hash()
        wps = [
            WorkPackageCompletion(
                wp_id="WP-GV0",
                owner_type="IMPLEMENTER",
                completion_contract="AUDIT_RECORD",  # 错配：实施者不应有 AUDIT_RECORD
                state="IMPLEMENTED_PENDING_EVIDENCE",
                actor_type="IMPLEMENTER",
            ),
        ]
        remainder = make_completion_contract_remainder(
            remainder_id="cc-001", dag_hash=dag_hash, wp_completions=wps,
        )
        result = verify_completion_contract_remainder(remainder)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_OWNER_CONTRACT_MISMATCH, result.error_codes)

    def test_negative_auditor_actor_mismatch(self):
        """BLOCKER: auditor-owned WP with implementer actor。"""
        dag_hash = _make_test_dag_hash()
        wps = [
            WorkPackageCompletion(
                wp_id="WP-AU1",
                owner_type="AUDITOR",
                completion_contract="AUDIT_RECORD",
                state="READY_FOR_AUDIT",
                actor_type="IMPLEMENTER",  # 错配
            ),
        ]
        remainder = make_completion_contract_remainder(
            remainder_id="cc-001", dag_hash=dag_hash, wp_completions=wps,
        )
        result = verify_completion_contract_remainder(remainder)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_OWNER_CONTRACT_MISMATCH, result.error_codes)

    def test_remainder_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        wps = [
            WorkPackageCompletion(
                wp_id="WP-GV0",
                owner_type="IMPLEMENTER",
                completion_contract="IMPLEMENTATION_BUNDLE",
                state="IMPLEMENTED_PENDING_EVIDENCE",
                actor_type="IMPLEMENTER",
            ),
        ]
        r1 = make_completion_contract_remainder(
            remainder_id="cc-001", dag_hash=dag_hash, wp_completions=wps,
        )
        r2 = make_completion_contract_remainder(
            remainder_id="cc-001", dag_hash=dag_hash, wp_completions=wps,
        )
        self.assertEqual(r1.content_hash, r2.content_hash)


# ─── FullChainRemainder tests ────────────────────────────────────────────


class TestFullChainRemainder(unittest.TestCase):
    """FullChainRemainder 测试。"""

    def test_make_remainder_zero(self):
        dag_hash = _make_test_dag_hash()
        phases = [
            PhaseSealStatus(phase=p, sealed=True, dag_edge_satisfied=True)
            for p in ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
        ]
        remainder = make_full_chain_remainder(
            remainder_id="fc-001", dag_hash=dag_hash,
            phase_statuses=phases, orphan_count=0,
        )
        self.assertTrue(remainder.is_zero)
        self.assertEqual(remainder.remainder, 0)

    def test_verify_remainder_zero_pass(self):
        dag_hash = _make_test_dag_hash()
        phases = [
            PhaseSealStatus(phase=p, sealed=True, dag_edge_satisfied=True)
            for p in ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
        ]
        remainder = make_full_chain_remainder(
            remainder_id="fc-001", dag_hash=dag_hash,
            phase_statuses=phases, orphan_count=0,
        )
        result = verify_full_chain_remainder(remainder)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_negative_unsealed_phase(self):
        """BLOCKER: full chain remainder != 0 (unsealed phase)。"""
        dag_hash = _make_test_dag_hash()
        phases = [
            PhaseSealStatus(phase="P0", sealed=True, dag_edge_satisfied=True),
            PhaseSealStatus(phase="P1", sealed=False, dag_edge_satisfied=True),  # 未 sealed
            PhaseSealStatus(phase="P2", sealed=True, dag_edge_satisfied=True),
            PhaseSealStatus(phase="P3", sealed=True, dag_edge_satisfied=True),
            PhaseSealStatus(phase="P4", sealed=True, dag_edge_satisfied=True),
            PhaseSealStatus(phase="P5", sealed=True, dag_edge_satisfied=True),
            PhaseSealStatus(phase="P6", sealed=True, dag_edge_satisfied=True),
            PhaseSealStatus(phase="P7", sealed=True, dag_edge_satisfied=True),
            PhaseSealStatus(phase="P8", sealed=True, dag_edge_satisfied=True),
        ]
        remainder = make_full_chain_remainder(
            remainder_id="fc-001", dag_hash=dag_hash,
            phase_statuses=phases, orphan_count=0,
        )
        result = verify_full_chain_remainder(remainder)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_FULL_CHAIN_REMAINDER_NONZERO, result.error_codes)
        self.assertIn(EC.VR_PHASE_NOT_SEALED, result.error_codes)

    def test_negative_edge_violation(self):
        """BLOCKER: DAG edge violation。"""
        dag_hash = _make_test_dag_hash()
        phases = [
            PhaseSealStatus(phase=p, sealed=True, dag_edge_satisfied=False)
            for p in ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
        ]
        remainder = make_full_chain_remainder(
            remainder_id="fc-001", dag_hash=dag_hash,
            phase_statuses=phases, orphan_count=0,
        )
        result = verify_full_chain_remainder(remainder)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_DAG_NOT_SEALED, result.error_codes)

    def test_negative_orphan_in_chain(self):
        """BLOCKER: orphan objects in chain。"""
        dag_hash = _make_test_dag_hash()
        phases = [
            PhaseSealStatus(phase=p, sealed=True, dag_edge_satisfied=True)
            for p in ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
        ]
        remainder = make_full_chain_remainder(
            remainder_id="fc-001", dag_hash=dag_hash,
            phase_statuses=phases, orphan_count=3,
        )
        result = verify_full_chain_remainder(remainder)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_ORPHAN_OBJECT, result.error_codes)

    def test_remainder_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        phases = [
            PhaseSealStatus(phase=p, sealed=True, dag_edge_satisfied=True)
            for p in ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
        ]
        r1 = make_full_chain_remainder(
            remainder_id="fc-001", dag_hash=dag_hash,
            phase_statuses=phases, orphan_count=0,
        )
        r2 = make_full_chain_remainder(
            remainder_id="fc-001", dag_hash=dag_hash,
            phase_statuses=phases, orphan_count=0,
        )
        self.assertEqual(r1.content_hash, r2.content_hash)


# ─── CostAndCoverageDelta tests ──────────────────────────────────────────


class TestCostAndCoverageDelta(unittest.TestCase):
    """CostAndCoverageDelta 测试。"""

    def test_make_delta(self):
        dag_hash = _make_test_dag_hash()
        cost_p0 = CostAggregation(tokens=100, wallclock_seconds=10.0)
        cost_p9 = CostAggregation(tokens=500, wallclock_seconds=50.0)
        coverage_before = [
            CoverageCell(cell_key="cell_A", covered=False),
            CoverageCell(cell_key="cell_B", covered=False),
        ]
        coverage_after = [
            CoverageCell(cell_key="cell_A", covered=True),
            CoverageCell(cell_key="cell_B", covered=False),
        ]
        delta = make_cost_and_coverage_delta(
            delta_id="cd-001", dag_hash=dag_hash,
            cost_p0=cost_p0, cost_p9=cost_p9,
            coverage_before=coverage_before, coverage_after=coverage_after,
        )
        self.assertTrue(delta.is_hash_valid)
        self.assertEqual(delta.cost_delta.tokens, 400)
        self.assertEqual(delta.coverage_delta_covered, 1)
        self.assertEqual(delta.coverage_delta_uncovered, 1)

    def test_verify_delta_pass(self):
        dag_hash = _make_test_dag_hash()
        cost_p0 = CostAggregation(tokens=100)
        cost_p9 = CostAggregation(tokens=500)
        coverage_before = [CoverageCell(cell_key="cell_A", covered=False)]
        coverage_after = [CoverageCell(cell_key="cell_A", covered=True)]
        delta = make_cost_and_coverage_delta(
            delta_id="cd-001", dag_hash=dag_hash,
            cost_p0=cost_p0, cost_p9=cost_p9,
            coverage_before=coverage_before, coverage_after=coverage_after,
        )
        result = verify_cost_and_coverage_delta(delta)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_next_eligible_coverage_cells(self):
        """next eligible coverage cells = 仍未覆盖的 cells。"""
        dag_hash = _make_test_dag_hash()
        coverage_after = [
            CoverageCell(cell_key="cell_A", covered=True),
            CoverageCell(cell_key="cell_B", covered=False),
            CoverageCell(cell_key="cell_C", covered=False),
        ]
        delta = make_cost_and_coverage_delta(
            delta_id="cd-001", dag_hash=dag_hash,
            cost_p0=CostAggregation(), cost_p9=CostAggregation(),
            coverage_before=[], coverage_after=coverage_after,
        )
        self.assertIn("cell_B", delta.next_eligible_coverage_cells)
        self.assertIn("cell_C", delta.next_eligible_coverage_cells)
        self.assertNotIn("cell_A", delta.next_eligible_coverage_cells)

    def test_negative_cost_delta_incomplete(self):
        """BLOCKER: cost delta incomplete。"""
        dag_hash = _make_test_dag_hash()
        cost_p0 = CostAggregation(tokens=100, complete=True)
        cost_p9 = CostAggregation(tokens=500, complete=False)  # 不完整
        coverage_after = [CoverageCell(cell_key="cell_A", covered=True)]
        delta = make_cost_and_coverage_delta(
            delta_id="cd-001", dag_hash=dag_hash,
            cost_p0=cost_p0, cost_p9=cost_p9,
            coverage_before=[], coverage_after=coverage_after,
        )
        result = verify_cost_and_coverage_delta(delta)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_COST_DELTA_INCOMPLETE, result.error_codes)

    def test_negative_coverage_delta_incomplete(self):
        """BLOCKER: coverage delta incomplete。"""
        dag_hash = _make_test_dag_hash()
        delta = make_cost_and_coverage_delta(
            delta_id="cd-001", dag_hash=dag_hash,
            cost_p0=CostAggregation(), cost_p9=CostAggregation(),
            coverage_before=[], coverage_after=[],  # 空 = 不完整
        )
        result = verify_cost_and_coverage_delta(delta)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_COVERAGE_DELTA_INCOMPLETE, result.error_codes)

    def test_delta_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        cost_p0 = CostAggregation(tokens=100)
        cost_p9 = CostAggregation(tokens=500)
        coverage_before = [CoverageCell(cell_key="cell_A", covered=False)]
        coverage_after = [CoverageCell(cell_key="cell_A", covered=True)]
        d1 = make_cost_and_coverage_delta(
            delta_id="cd-001", dag_hash=dag_hash,
            cost_p0=cost_p0, cost_p9=cost_p9,
            coverage_before=coverage_before, coverage_after=coverage_after,
        )
        d2 = make_cost_and_coverage_delta(
            delta_id="cd-001", dag_hash=dag_hash,
            cost_p0=cost_p0, cost_p9=cost_p9,
            coverage_before=coverage_before, coverage_after=coverage_after,
        )
        self.assertEqual(d1.content_hash, d2.content_hash)


# ─── HumanReadableSummary tests ──────────────────────────────────────────


class TestHumanReadableSummary(unittest.TestCase):
    """HumanReadableSummary 测试。"""

    def test_make_summary(self):
        dag_hash = _make_test_dag_hash()
        verdict = make_machine_verdict(
            verdict_id="mv-001", dag_hash=dag_hash,
            factory_status="PASS", scientific_status="PASS",
            scale_status="NOT_TESTED",
        )
        gate_verdict = make_six_gate_verdict(
            verdict_id="gv-001", dag_hash=dag_hash,
            gate_statuses={k: "PASS" for k in VR_GATE_KINDS},
        )
        summary = make_human_readable_summary(
            summary_id="sm-001", dag_hash=dag_hash,
            verdict=verdict, gate_verdict=gate_verdict,
            completion_remainder_zero=True,
            full_chain_remainder_zero=True,
            cost_summary="tokens: 400",
            coverage_summary="covered: 1, uncovered: 1",
        )
        self.assertTrue(summary.is_hash_valid)
        self.assertIn("P9 Verdict Summary", summary.title)
        self.assertIn("Factory", summary.full_text)

    def test_verify_summary_pass(self):
        dag_hash = _make_test_dag_hash()
        verdict = make_machine_verdict(
            verdict_id="mv-001", dag_hash=dag_hash,
            factory_status="PASS", scientific_status="PASS",
            scale_status="NOT_TESTED",
        )
        gate_verdict = make_six_gate_verdict(
            verdict_id="gv-001", dag_hash=dag_hash,
            gate_statuses={k: "PASS" for k in VR_GATE_KINDS},
        )
        summary = make_human_readable_summary(
            summary_id="sm-001", dag_hash=dag_hash,
            verdict=verdict, gate_verdict=gate_verdict,
            completion_remainder_zero=True,
            full_chain_remainder_zero=True,
        )
        result = verify_human_readable_summary(summary)
        self.assertTrue(result.passed, f"Verification failed: {result.details}")

    def test_negative_summary_invalid(self):
        """BLOCKER: summary invalid。"""
        dag_hash = _make_test_dag_hash()
        summary = HumanReadableSummary(
            summary_id="",  # 空 ID
            dag_hash=dag_hash,
            verdict_hash=_make_test_evidence_hash("v"),
            content_hash="",
        )
        summary = dataclasses.replace(
            summary, content_hash=summary.compute_content_hash()
        )
        result = verify_human_readable_summary(summary)
        self.assertFalse(result.passed)
        self.assertIn(EC.VR_SUMMARY_INVALID, result.error_codes)

    def test_summary_hash_deterministic(self):
        dag_hash = _make_test_dag_hash()
        verdict = make_machine_verdict(
            verdict_id="mv-001", dag_hash=dag_hash,
            factory_status="PASS", scientific_status="PASS",
            scale_status="NOT_TESTED",
        )
        gate_verdict = make_six_gate_verdict(
            verdict_id="gv-001", dag_hash=dag_hash,
            gate_statuses={k: "PASS" for k in VR_GATE_KINDS},
        )
        s1 = make_human_readable_summary(
            summary_id="sm-001", dag_hash=dag_hash,
            verdict=verdict, gate_verdict=gate_verdict,
            completion_remainder_zero=True,
            full_chain_remainder_zero=True,
        )
        s2 = make_human_readable_summary(
            summary_id="sm-001", dag_hash=dag_hash,
            verdict=verdict, gate_verdict=gate_verdict,
            completion_remainder_zero=True,
            full_chain_remainder_zero=True,
        )
        self.assertEqual(s1.content_hash, s2.content_hash)


# ─── VerdictBuilder golden path tests ────────────────────────────────────


class TestVerdictBuilder(unittest.TestCase):
    """VerdictBuilder golden path 测试。"""

    def test_golden_path_build(self):
        """Golden path: sealed P0-P8 DAG → VerdictBuilder → 全套 P9 产物。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(
            dag=dag,
            factory_status="PASS",
            scientific_status="PASS",
            scale_status="NOT_TESTED",
        )
        # 所有产物存在
        self.assertIsInstance(result.verdict, MachineVerdict)
        self.assertIsInstance(result.gate_verdict, SixGateVerdict)
        self.assertIsInstance(result.evidence_index, EvidenceIndex)
        self.assertIsInstance(result.checkpoint, VerdictCheckpoint)
        self.assertIsInstance(result.replay, EvidenceReplay)
        self.assertIsInstance(result.completion_remainder, CompletionContractRemainder)
        self.assertIsInstance(result.full_chain_remainder, FullChainRemainder)
        self.assertIsInstance(result.cost_coverage_delta, CostAndCoverageDelta)
        self.assertIsInstance(result.summary, HumanReadableSummary)
        self.assertIsInstance(result.rule_registry, VerdictRuleRegistry)

    def test_golden_path_no_errors(self):
        """Golden path 构建无错误。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        self.assertEqual(result.errors, [], f"Build errors: {result.errors}")
        self.assertTrue(result.passed)

    def test_golden_path_remainders_zero(self):
        """Golden path: completion-contract remainder=0, full chain remainder=0。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        self.assertTrue(result.completion_remainder.is_zero)
        self.assertTrue(result.full_chain_remainder.is_zero)

    def test_golden_path_replay_complete(self):
        """Golden path: replay remainder=0。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        self.assertTrue(result.replay.is_complete)
        self.assertEqual(result.replay.remainder, 0)

    def test_golden_path_evidence_index_in_p9(self):
        """Golden path: EvidenceIndex 在 P9 生成。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        self.assertEqual(result.evidence_index.generated_in_phase, "P9")

    def test_golden_path_checkpoint_valid(self):
        """Golden path: checkpoint hash 有效。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        self.assertTrue(result.checkpoint.is_hash_valid)

    def test_golden_path_summary_has_text(self):
        """Golden path: summary 有完整文本。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        self.assertTrue(len(result.summary.full_text) > 0)
        self.assertIn("Factory", result.summary.full_text)

    def test_golden_path_axes_independent(self):
        """Golden path: 三轴独立评估。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(
            dag=dag,
            factory_status="PASS",
            scientific_status="FAIL",
            scale_status="NOT_TESTED",
        )
        self.assertEqual(result.verdict.get_axis("FACTORY").status, "PASS")
        self.assertEqual(result.verdict.get_axis("SCIENTIFIC").status, "FAIL")
        self.assertEqual(result.verdict.get_axis("SCALE").status, "NOT_TESTED")
        self.assertEqual(result.verdict.overall_status, "FAIL")

    def test_builder_deterministic(self):
        """VerdictBuilder 确定性——同样输入同样输出（除时间戳外）。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        r1 = builder.build(dag=dag)
        r2 = builder.build(dag=dag)
        self.assertEqual(r1.verdict.content_hash, r2.verdict.content_hash)
        self.assertEqual(r1.gate_verdict.content_hash, r2.gate_verdict.content_hash)
        self.assertEqual(r1.evidence_index.content_hash, r2.evidence_index.content_hash)
        self.assertEqual(r1.replay.content_hash, r2.replay.content_hash)
        # checkpoint hash 包含 created_at 时间戳，不要求确定性
        # 但 checkpoint 自身 hash 必须有效
        self.assertTrue(r1.checkpoint.is_hash_valid)
        self.assertTrue(r2.checkpoint.is_hash_valid)


# ─── VerdictCapabilityReport tests ───────────────────────────────────────


class TestVerdictCapabilityReport(unittest.TestCase):
    """VerdictCapabilityReport 测试。"""

    def _make_report_kwargs(self):
        """构建合法报告参数。"""
        h = lambda s: hashlib.sha256(s.encode()).hexdigest()
        return dict(
            dag_hash=h("dag"),
            verdict_hash=h("verdict"),
            gate_verdict_hash=h("gate"),
            evidence_index_hash=h("index"),
            replay_hash=h("replay"),
            completion_remainder_hash=h("cc"),
            full_chain_remainder_hash=h("fc"),
            cost_coverage_delta_hash=h("cd"),
            summary_hash=h("summary"),
            checkpoint_hash=h("checkpoint"),
            registry_hash=h("registry"),
            factory_axis_independent=True,
            scientific_axis_independent=True,
            scale_axis_independent=True,
            no_pass_averaged_fail=True,
            not_tested_not_pass=True,
            six_gates_independent=True,
            evidence_index_in_p9_only=True,
            evidence_retraceable=True,
            checkpoint_hash_bound=True,
            all_objects_placed=True,
            no_orphans=True,
            no_duplicates=True,
            no_missing=True,
            completion_contract_remainder_zero=True,
            full_chain_remainder_zero=True,
            verdict_rule_registry_fail_closed=True,
            cost_delta_complete=True,
            coverage_delta_complete=True,
            summary_valid=True,
            verifier_identity="test-verifier",
        )

    def test_build_report_pass(self):
        kwargs = self._make_report_kwargs()
        report = build_verdict_capability_report(**kwargs)
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["report_kind"], "VerdictCapabilityReport")

    def test_verify_report_pass(self):
        kwargs = self._make_report_kwargs()
        report = build_verdict_capability_report(**kwargs)
        errors = verify_verdict_capability_report(report)
        self.assertEqual(len(errors), 0, f"Verification errors: {errors}")

    def test_report_side_effects_zero(self):
        kwargs = self._make_report_kwargs()
        report = build_verdict_capability_report(**kwargs)
        for key in VR_SIDE_EFFECT_KEYS:
            self.assertEqual(report["side_effects"][key], 0)

    def test_report_claims_match(self):
        kwargs = self._make_report_kwargs()
        report = build_verdict_capability_report(**kwargs)
        self.assertEqual(set(report["claims"]), set(VR_CLAIMS))

    def test_report_nonclaims_match(self):
        kwargs = self._make_report_kwargs()
        report = build_verdict_capability_report(**kwargs)
        self.assertEqual(set(report["explicit_nonclaims"]), set(VR_NONCLAIMS))

    def test_report_checks_match(self):
        kwargs = self._make_report_kwargs()
        report = build_verdict_capability_report(**kwargs)
        check_ids = [c["check_id"] for c in report["checks"]]
        self.assertEqual(check_ids, list(VR_CHECK_IDS))

    def test_negative_report_flag_false(self):
        """BLOCKER: flag 为 False 时报告构建失败。"""
        kwargs = self._make_report_kwargs()
        kwargs["no_pass_averaged_fail"] = False
        with self.assertRaises(VerdictCapabilityReportError):
            build_verdict_capability_report(**kwargs)

    def test_negative_report_completion_remainder_nonzero(self):
        """BLOCKER: completion_contract_remainder_zero=False。"""
        kwargs = self._make_report_kwargs()
        kwargs["completion_contract_remainder_zero"] = False
        with self.assertRaises(VerdictCapabilityReportError):
            build_verdict_capability_report(**kwargs)

    def test_negative_report_full_chain_remainder_nonzero(self):
        """BLOCKER: full_chain_remainder_zero=False。"""
        kwargs = self._make_report_kwargs()
        kwargs["full_chain_remainder_zero"] = False
        with self.assertRaises(VerdictCapabilityReportError):
            build_verdict_capability_report(**kwargs)

    def test_negative_report_not_tested_as_pass(self):
        """BLOCKER: not_tested_not_pass=False。"""
        kwargs = self._make_report_kwargs()
        kwargs["not_tested_not_pass"] = False
        with self.assertRaises(VerdictCapabilityReportError):
            build_verdict_capability_report(**kwargs)

    def test_negative_report_orphan(self):
        """BLOCKER: no_orphans=False。"""
        kwargs = self._make_report_kwargs()
        kwargs["no_orphans"] = False
        with self.assertRaises(VerdictCapabilityReportError):
            build_verdict_capability_report(**kwargs)

    def test_negative_report_fail_closed(self):
        """BLOCKER: verdict_rule_registry_fail_closed=False。"""
        kwargs = self._make_report_kwargs()
        kwargs["verdict_rule_registry_fail_closed"] = False
        with self.assertRaises(VerdictCapabilityReportError):
            build_verdict_capability_report(**kwargs)

    def test_negative_report_boundary(self):
        """BLOCKER: report_kind in forbidden output kinds。"""
        kwargs = self._make_report_kwargs()
        report = build_verdict_capability_report(**kwargs)
        report["report_kind"] = "AuditRecord"  # 禁止的
        errors = verify_verdict_capability_report(report)
        self.assertTrue(any(e[0] == EC.VR_OUTPUT_KIND_FORBIDDEN for e in errors))


# ─── Constants verification tests ────────────────────────────────────────


class TestConstants(unittest.TestCase):
    """所有 VR1 常量验证。"""

    def test_verdict_axes(self):
        self.assertEqual(VR_VERDICT_AXES, frozenset({"FACTORY", "SCIENTIFIC", "SCALE"}))

    def test_verdict_statuses(self):
        self.assertEqual(
            VR_VERDICT_STATUSES,
            frozenset({"PASS", "FAIL", "NOT_TESTED", "BLOCKED"}),
        )

    def test_gate_kinds(self):
        self.assertEqual(
            VR_GATE_KINDS,
            frozenset({
                "G_P0_READINESS", "G_P1_DRYRUN", "G_P2_CANDIDATE",
                "G_P3_QUESTION", "G_P4_PLAN", "G_P5_RUN",
            }),
        )

    def test_gate_statuses(self):
        self.assertEqual(
            VR_GATE_STATUSES,
            frozenset({"PASS", "FAIL", "NOT_TESTED", "BLOCKED"}),
        )

    def test_replay_statuses(self):
        self.assertEqual(
            VR_REPLAY_STATUSES,
            frozenset({"PLACED", "ORPHAN", "DUPLICATE", "MISSING"}),
        )

    def test_remainder_kinds(self):
        self.assertEqual(
            VR_REMAINDER_KINDS,
            frozenset({"COMPLETION_CONTRACT", "FULL_CHAIN"}),
        )

    def test_verdict_rule_statuses(self):
        self.assertEqual(
            VR_VERDICT_RULE_STATUSES,
            frozenset({"PASS", "FAIL", "NOT_TESTED", "BLOCKED"}),
        )

    def test_allowed_output_kinds(self):
        expected = {
            "MachineVerdict", "SixGateVerdict", "EvidenceIndex",
            "RuntimeCheckpoint", "EvidenceReplay",
            "CompletionContractRemainder", "FullChainRemainder",
            "CostAndCoverageDelta", "HumanReadableSummary",
            "VerdictCapabilityReport",
        }
        self.assertEqual(VR_ALLOWED_OUTPUT_KINDS, frozenset(expected))

    def test_forbidden_output_kinds(self):
        expected = {
            "DatabaseSchemaStateReport", "SchemaBootstrapReceipt",
            "DatabaseRuntimeCapabilityReport",
            "ArtifactCommitReconcileCapabilityReport",
            "RedisProjection", "AuditRecord", "SystemCompletionBundle",
        }
        self.assertEqual(VR_FORBIDDEN_OUTPUT_KINDS, frozenset(expected))

    def test_allowed_and_forbidden_disjoint(self):
        """allowed 和 forbidden 不相交。"""
        self.assertEqual(
            VR_ALLOWED_OUTPUT_KINDS & VR_FORBIDDEN_OUTPUT_KINDS, frozenset()
        )

    def test_side_effect_keys(self):
        expected = (
            "database_writes", "redis_writes", "d_volume_writes",
            "solver_launches", "model_live_calls", "human_gate_commits",
        )
        self.assertEqual(VR_SIDE_EFFECT_KEYS, expected)

    def test_check_ids_unique(self):
        self.assertEqual(len(VR_CHECK_IDS), len(set(VR_CHECK_IDS)))

    def test_claims_unique(self):
        self.assertEqual(len(VR_CLAIMS), len(set(VR_CLAIMS)))

    def test_nonclaims_unique(self):
        self.assertEqual(len(VR_NONCLAIMS), len(set(VR_NONCLAIMS)))

    def test_error_codes_exist(self):
        """所有 VR1 错误码存在。"""
        codes = [
            EC.VR_PASS_AVERAGED_FAIL,
            EC.VR_NOT_TESTED_AS_PASS,
            EC.VR_ORPHAN_OBJECT,
            EC.VR_NON_RETRACEABLE,
            EC.VR_OWNER_CONTRACT_MISMATCH,
            EC.VR_EVIDENCE_INDEX_BEFORE_P9,
            EC.VR_COMPLETION_CONTRACT_REMAINDER_NONZERO,
            EC.VR_FULL_CHAIN_REMAINDER_NONZERO,
            EC.VR_VERDICT_RULE_UNKNOWN_NOT_FAIL_CLOSED,
            EC.VR_AXIS_INVALID,
            EC.VR_GATE_INVALID,
            EC.VR_REPLAY_INCOMPLETE,
            EC.VR_CHECKPOINT_HASH_MISMATCH,
            EC.VR_VERDICT_HASH_MISMATCH,
            EC.VR_EVIDENCE_INDEX_HASH_MISMATCH,
            EC.VR_COST_DELTA_INCOMPLETE,
            EC.VR_COVERAGE_DELTA_INCOMPLETE,
            EC.VR_SUMMARY_INVALID,
            EC.VR_RUNTIME_CHECKPOINT_INVALID,
            EC.VR_OUTPUT_KIND_FORBIDDEN,
            EC.VR_CAPABILITY_HASH_MISMATCH,
            EC.VR_DUPLICATE_OBJECT,
            EC.VR_MISSING_OBJECT,
            EC.VR_AXIS_NOT_INDEPENDENT,
            EC.VR_GATE_NOT_INDEPENDENT,
            EC.VR_DAG_NOT_SEALED,
            EC.VR_PHASE_NOT_SEALED,
        ]
        for code in codes:
            self.assertIsNotNone(code.value)


# ─── VR1 boundary tests ──────────────────────────────────────────────────


class TestVR1Boundary(unittest.TestCase):
    """VR1 boundary tests (allowed/forbidden output kinds)。"""

    def test_verdict_capability_report_in_allowed(self):
        self.assertIn("VerdictCapabilityReport", VR_ALLOWED_OUTPUT_KINDS)

    def test_machine_verdict_in_allowed(self):
        self.assertIn("MachineVerdict", VR_ALLOWED_OUTPUT_KINDS)

    def test_evidence_index_in_allowed(self):
        self.assertIn("EvidenceIndex", VR_ALLOWED_OUTPUT_KINDS)

    def test_audit_record_in_forbidden(self):
        self.assertIn("AuditRecord", VR_FORBIDDEN_OUTPUT_KINDS)

    def test_system_completion_bundle_in_forbidden(self):
        self.assertIn("SystemCompletionBundle", VR_FORBIDDEN_OUTPUT_KINDS)

    def test_redis_projection_in_forbidden(self):
        self.assertIn("RedisProjection", VR_FORBIDDEN_OUTPUT_KINDS)

    def test_checkpoint_states(self):
        self.assertEqual(
            CHECKPOINT_STATES,
            frozenset({"RECORDED", "VERIFIED", "RECOVERED", "INCOMPLETE"}),
        )


# ─── Cross-component integration tests ───────────────────────────────────


class TestIntegration(unittest.TestCase):
    """跨组件集成测试。"""

    def test_full_pipeline_remainder_zero(self):
        """完整 pipeline: 所有 remainder=0。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        self.assertTrue(result.completion_remainder.is_zero)
        self.assertTrue(result.full_chain_remainder.is_zero)
        self.assertTrue(result.replay.is_complete)

    def test_full_pipeline_checkpoint_consistent(self):
        """checkpoint 与所有产物 hash 一致。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        ck_result = verify_checkpoint_against_hashes(
            result.checkpoint,
            verdict_hash=result.verdict.content_hash,
            gate_verdict_hash=result.gate_verdict.content_hash,
            evidence_index_hash=result.evidence_index.content_hash,
            replay_hash=result.replay.content_hash,
            dag_hash=dag.dag_hash,
        )
        self.assertTrue(ck_result.passed, f"Checkpoint inconsistent: {ck_result.details}")

    def test_full_pipeline_evidence_retraceable(self):
        """所有 evidence 可从 EvidenceIndex 反查。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        for rec in dag.evidence_records:
            r = check_retraceable(result.evidence_index, rec["hash"])
            self.assertTrue(r.passed, f"Evidence {rec['hash']} not retraceable")

    def test_full_pipeline_capability_report(self):
        """从 VerdictBuildResult 构建 VerdictCapabilityReport。"""
        dag = _make_sealed_dag()
        builder = VerdictBuilder()
        result = builder.build(dag=dag)
        report = build_verdict_capability_report(
            dag_hash=dag.dag_hash,
            verdict_hash=result.verdict.content_hash,
            gate_verdict_hash=result.gate_verdict.content_hash,
            evidence_index_hash=result.evidence_index.content_hash,
            replay_hash=result.replay.content_hash,
            completion_remainder_hash=result.completion_remainder.content_hash,
            full_chain_remainder_hash=result.full_chain_remainder.content_hash,
            cost_coverage_delta_hash=result.cost_coverage_delta.content_hash,
            summary_hash=result.summary.content_hash,
            checkpoint_hash=result.checkpoint.checkpoint_hash,
            registry_hash=result.rule_registry.registry_hash,
            factory_axis_independent=True,
            scientific_axis_independent=True,
            scale_axis_independent=True,
            no_pass_averaged_fail=True,
            not_tested_not_pass=True,
            six_gates_independent=True,
            evidence_index_in_p9_only=True,
            evidence_retraceable=True,
            checkpoint_hash_bound=True,
            all_objects_placed=True,
            no_orphans=True,
            no_duplicates=True,
            no_missing=True,
            completion_contract_remainder_zero=result.completion_remainder.is_zero,
            full_chain_remainder_zero=result.full_chain_remainder.is_zero,
            verdict_rule_registry_fail_closed=True,
            cost_delta_complete=result.cost_coverage_delta.cost_complete,
            coverage_delta_complete=result.cost_coverage_delta.coverage_complete,
            summary_valid=True,
            verifier_identity="vr1-test",
        )
        self.assertEqual(report["verdict"], "PASS")


if __name__ == "__main__":
    unittest.main()
