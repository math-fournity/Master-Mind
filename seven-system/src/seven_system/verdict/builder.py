"""VerdictBuilder — 从 sealed P0-P8 DAG 构建 P9 verdict。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

VerdictBuilder 从 sealed P0-P8 DAG 构建 P9 verdict。
Factory 轴（系统完备性）和 Scientific 轴（证据质量）是分离的。
Scale 轴用于生产就绪。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    VR_VERDICT_AXES,
    VR_VERDICT_STATUSES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from .machine_verdict import (
    MachineVerdict,
    AxisVerdict,
    make_machine_verdict,
    verify_machine_verdict,
)
from .six_gate import (
    SixGateVerdict,
    make_six_gate_verdict,
    verify_six_gate_verdict,
)
from .evidence_index import (
    EvidenceIndex,
    EvidenceEntry,
    make_evidence_index,
    verify_evidence_index,
)
from .checkpoint import (
    VerdictCheckpoint,
    make_verdict_checkpoint,
    verify_verdict_checkpoint,
)
from .replay import (
    EvidenceReplay,
    ReplayObject,
    CompletionContractRemainder,
    WorkPackageCompletion,
    FullChainRemainder,
    PhaseSealStatus,
    make_evidence_replay,
    verify_evidence_replay,
    make_completion_contract_remainder,
    verify_completion_contract_remainder,
    make_full_chain_remainder,
    verify_full_chain_remainder,
)
from .cost_coverage import (
    CostAndCoverageDelta,
    CostAggregation,
    CoverageCell,
    make_cost_and_coverage_delta,
    verify_cost_and_coverage_delta,
)
from .summary import (
    HumanReadableSummary,
    make_human_readable_summary,
    verify_human_readable_summary,
)
from .rule_registry import (
    VerdictRuleRegistry,
    make_verdict_rule_registry,
    lookup_verdict_rule,
    verify_verdict_rule_registry,
)


@dataclass
class SealedDAG:
    """sealed P0-P8 DAG 的内存表示。

    字段：
        dag_hash: DAG hash
        work_packages: 工作包列表
        phase_seals: P0-P8 各阶段 sealed 状态
        evidence_records: sealed evidence record hash 列表
        run_audits: sealed run audit hash 列表
        run_artifact_bundles: sealed run artifact bundle hash 列表
    """

    dag_hash: str = ""
    work_packages: list[dict[str, Any]] = field(default_factory=list)
    phase_seals: dict[str, bool] = field(default_factory=dict)
    evidence_records: list[dict[str, str]] = field(default_factory=list)
    run_audits: list[dict[str, str]] = field(default_factory=list)
    run_artifact_bundles: list[dict[str, str]] = field(default_factory=list)
    gate_statuses: dict[str, str] = field(default_factory=dict)

    @property
    def is_sealed(self) -> bool:
        """所有 P0-P8 阶段都 sealed。"""
        phases = ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
        return all(self.phase_seals.get(p, False) for p in phases)


@dataclass
class VerdictBuildResult:
    """VerdictBuilder 的构建结果。"""

    verdict: MachineVerdict
    gate_verdict: SixGateVerdict
    evidence_index: EvidenceIndex
    checkpoint: VerdictCheckpoint
    replay: EvidenceReplay
    completion_remainder: CompletionContractRemainder
    full_chain_remainder: FullChainRemainder
    cost_coverage_delta: CostAndCoverageDelta
    summary: HumanReadableSummary
    rule_registry: VerdictRuleRegistry
    errors: list[tuple[EC, str]] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        """所有验证通过且无错误。"""
        return len(self.errors) == 0


class VerdictBuilder:
    """P9 VerdictBuilder — 从 sealed P0-P8 DAG 构建 P9 verdict。

    构建顺序：
    1. VerdictRuleRegistry（冻结映射）
    2. MachineVerdict（分轴）
    3. SixGateVerdict（六门）
    4. EvidenceIndex（DAG index）
    5. EvidenceReplay（replay/remainder）
    6. CompletionContractRemainder
    7. FullChainRemainder
    8. CostAndCoverageDelta
    9. RuntimeCheckpoint
    10. HumanReadableSummary
    """

    def __init__(self) -> None:
        self._registry: VerdictRuleRegistry | None = None

    @property
    def registry(self) -> VerdictRuleRegistry:
        if self._registry is None:
            self._registry = make_verdict_rule_registry()
        return self._registry

    def build(
        self,
        *,
        dag: SealedDAG,
        verdict_id: str = "vr1-verdict-001",
        gate_verdict_id: str = "vr1-gate-verdict-001",
        index_id: str = "vr1-evidence-index-001",
        checkpoint_id: str = "vr1-checkpoint-001",
        replay_id: str = "vr1-replay-001",
        completion_remainder_id: str = "vr1-cc-remainder-001",
        full_chain_remainder_id: str = "vr1-fc-remainder-001",
        delta_id: str = "vr1-cost-coverage-001",
        summary_id: str = "vr1-summary-001",
        factory_status: str = "PASS",
        scientific_status: str = "PASS",
        scale_status: str = "NOT_TESTED",
        factory_reason: str = "",
        scientific_reason: str = "",
        scale_reason: str = "",
        cost_p0: CostAggregation | None = None,
        cost_p9: CostAggregation | None = None,
        coverage_before: list[CoverageCell] | None = None,
        coverage_after: list[CoverageCell] | None = None,
        next_eligible_work_cells: list[str] | None = None,
    ) -> VerdictBuildResult:
        """从 sealed DAG 构建 P9 verdict 全套产物。"""
        errors: list[tuple[EC, str]] = []

        # 1. VerdictRuleRegistry
        registry = self.registry
        reg_result = verify_verdict_rule_registry(registry)
        if not reg_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(reg_result.error_codes, reg_result.details)
            )

        # 2. MachineVerdict
        verdict = make_machine_verdict(
            verdict_id=verdict_id,
            dag_hash=dag.dag_hash,
            factory_status=factory_status,
            scientific_status=scientific_status,
            scale_status=scale_status,
            factory_reason=factory_reason,
            scientific_reason=scientific_reason,
            scale_reason=scale_reason,
        )
        mv_result = verify_machine_verdict(verdict)
        if not mv_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(mv_result.error_codes, mv_result.details)
            )

        # 3. SixGateVerdict
        gate_verdict = make_six_gate_verdict(
            verdict_id=gate_verdict_id,
            dag_hash=dag.dag_hash,
            gate_statuses=dag.gate_statuses,
        )
        gv_result = verify_six_gate_verdict(gate_verdict)
        if not gv_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(gv_result.error_codes, gv_result.details)
            )

        # 4. EvidenceIndex
        entries: list[EvidenceEntry] = []
        for rec in dag.evidence_records:
            entries.append(
                EvidenceEntry(
                    object_kind="EvidenceRecord",
                    object_hash=rec.get("hash", ""),
                    phase=rec.get("phase", "P7"),
                    wp_id=rec.get("wp_id", ""),
                )
            )
        for audit in dag.run_audits:
            entries.append(
                EvidenceEntry(
                    object_kind="RunAudit",
                    object_hash=audit.get("hash", ""),
                    phase=audit.get("phase", "P6"),
                    wp_id=audit.get("wp_id", ""),
                )
            )
        for bundle in dag.run_artifact_bundles:
            entries.append(
                EvidenceEntry(
                    object_kind="RunArtifactBundle",
                    object_hash=bundle.get("hash", ""),
                    phase=bundle.get("phase", "P5"),
                    wp_id=bundle.get("wp_id", ""),
                )
            )
        evidence_index = make_evidence_index(
            index_id=index_id,
            dag_hash=dag.dag_hash,
            verdict_hash=verdict.content_hash,
            entries=entries,
        )
        ei_result = verify_evidence_index(evidence_index)
        if not ei_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(ei_result.error_codes, ei_result.details)
            )

        # 5. EvidenceReplay
        replay_objects: list[ReplayObject] = []
        for entry in entries:
            replay_objects.append(
                ReplayObject(
                    object_kind=entry.object_kind,
                    object_hash=entry.object_hash,
                    source_phase=entry.phase,
                    wp_id=entry.wp_id,
                    destination="EvidenceIndex",
                )
            )
        replay = make_evidence_replay(
            replay_id=replay_id,
            dag_hash=dag.dag_hash,
            objects=replay_objects,
        )
        rp_result = verify_evidence_replay(replay)
        if not rp_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(rp_result.error_codes, rp_result.details)
            )

        # 6. CompletionContractRemainder
        wp_completions: list[WorkPackageCompletion] = []
        for wp in dag.work_packages:
            wp_completions.append(
                WorkPackageCompletion(
                    wp_id=wp.get("wp_id", ""),
                    owner_type=wp.get("owner_type", ""),
                    completion_contract=wp.get("completion_contract", ""),
                    state=wp.get("state", "NOT_STARTED"),
                    submitted_schema_id=wp.get("submitted_schema_id", ""),
                    actor_type=wp.get("actor_type", ""),
                )
            )
        completion_remainder = make_completion_contract_remainder(
            remainder_id=completion_remainder_id,
            dag_hash=dag.dag_hash,
            wp_completions=wp_completions,
        )
        cc_result = verify_completion_contract_remainder(completion_remainder)
        if not cc_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(cc_result.error_codes, cc_result.details)
            )

        # 7. FullChainRemainder
        phase_statuses: list[PhaseSealStatus] = []
        phases = ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
        for phase in phases:
            sealed = dag.phase_seals.get(phase, False)
            phase_statuses.append(
                PhaseSealStatus(
                    phase=phase,
                    sealed=sealed,
                    dag_edge_satisfied=sealed,
                    object_count=0,
                )
            )
        full_chain_remainder = make_full_chain_remainder(
            remainder_id=full_chain_remainder_id,
            dag_hash=dag.dag_hash,
            phase_statuses=phase_statuses,
            orphan_count=0,
        )
        fc_result = verify_full_chain_remainder(full_chain_remainder)
        if not fc_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(fc_result.error_codes, fc_result.details)
            )

        # 8. CostAndCoverageDelta
        cp0 = cost_p0 or CostAggregation()
        cp9 = cost_p9 or CostAggregation()
        cov_before = coverage_before or []
        cov_after = coverage_after or [
            CoverageCell(cell_key="default", covered=True)
        ]
        cost_coverage_delta = make_cost_and_coverage_delta(
            delta_id=delta_id,
            dag_hash=dag.dag_hash,
            cost_p0=cp0,
            cost_p9=cp9,
            coverage_before=cov_before,
            coverage_after=cov_after,
            next_eligible_work_cells=next_eligible_work_cells,
        )
        cd_result = verify_cost_and_coverage_delta(cost_coverage_delta)
        if not cd_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(cd_result.error_codes, cd_result.details)
            )

        # 9. RuntimeCheckpoint
        checkpoint = make_verdict_checkpoint(
            checkpoint_id=checkpoint_id,
            dag_hash=dag.dag_hash,
            verdict_hash=verdict.content_hash,
            gate_verdict_hash=gate_verdict.content_hash,
            evidence_index_hash=evidence_index.content_hash,
            replay_hash=replay.content_hash,
            state_snapshot={
                phase: "SEALED" if dag.phase_seals.get(phase) else "UNSEALED"
                for phase in phases
            },
        )
        ck_result = verify_verdict_checkpoint(checkpoint)
        if not ck_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(ck_result.error_codes, ck_result.details)
            )

        # 10. HumanReadableSummary
        summary = make_human_readable_summary(
            summary_id=summary_id,
            dag_hash=dag.dag_hash,
            verdict=verdict,
            gate_verdict=gate_verdict,
            completion_remainder_zero=completion_remainder.is_zero,
            full_chain_remainder_zero=full_chain_remainder.is_zero,
            cost_summary=f"tokens: {cost_coverage_delta.cost_delta.tokens}",
            coverage_summary=(
                f"covered: {cost_coverage_delta.coverage_delta_covered}, "
                f"uncovered: {cost_coverage_delta.coverage_delta_uncovered}"
            ),
            next_steps=list(cost_coverage_delta.next_eligible_coverage_cells),
        )
        sm_result = verify_human_readable_summary(summary)
        if not sm_result.passed:
            errors.extend(
                (ec, detail)
                for ec, detail in zip(sm_result.error_codes, sm_result.details)
            )

        return VerdictBuildResult(
            verdict=verdict,
            gate_verdict=gate_verdict,
            evidence_index=evidence_index,
            checkpoint=checkpoint,
            replay=replay,
            completion_remainder=completion_remainder,
            full_chain_remainder=full_chain_remainder,
            cost_coverage_delta=cost_coverage_delta,
            summary=summary,
            rule_registry=registry,
            errors=errors,
        )
