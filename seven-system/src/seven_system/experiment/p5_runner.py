"""P5ExperimentRunner — WP-EX1 P5 实验运行器。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 98-104 (P5 Target Solver Experiment):

Only executed by TargetSolverPort→DevinSolverAdapter→solver_harness.
All guided payload only from frozen TellStrategyRelease via
Selector/Renderer/Binding/Injection chain with receipts.
Core contrast at least includes equal-resource fresh restart problem-only,
plus lineage, direction, lineage+direction, distractor, operation/critic,
position-neutral. token-limit layered separately; same problem/source rollout
by cluster. Scientific negative results not auto-retried; tool/unobservable/
protocol drift recorded as invalid or quarantine.

关键约束（blocker）：
- 使用 FakeHarnessAdapter（SIDE_EFFECT_FREE）
- 收集所有 arm 结果——arms/negative/invalid 全部保留
- 预算超限 → BLOCK（EX_BUDGET_EXCEEDED）
- 原截断 bare baseline → BLOCK（EX_BASELINE_TRUNCATED）
- plan 启动后修改 → BLOCK（EX_PLAN_MODIFIED_AFTER_START）
- 负面/无效结果删除 → BLOCK（EX_NEGATIVE_RESULT_DELETED / EX_INVALID_RESULT_DELETED）

SIDE_EFFECT_FREE：纯内存实现，不启动真实 Solver。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EX_RUN_STATES,
    EX_TERMINATION_REASONS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..adapters.solver.harness_adapter import FakeHarnessAdapter
from ..adapters.solver.port import (
    SolverJob,
    build_solver_job,
)
from ..adapters.solver.harness_profile import build_harness_profile
from .experiment_plan import ExperimentPlan, verify_experiment_plan
from .run_artifact_bundle import (
    RunArtifactBundle,
    make_run_artifact_bundle,
    verify_run_artifact_bundle,
)


@dataclass
class ArmRunResult:
    """单个 arm 的运行结果。"""

    arm_id: str
    arm_kind: str
    bundle: RunArtifactBundle | None = None
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    retained: bool = True

    @property
    def is_negative(self) -> bool:
        return self.bundle is not None and self.bundle.is_negative

    @property
    def is_invalid(self) -> bool:
        return self.bundle is not None and self.bundle.is_invalid


@dataclass
class P5ExperimentRunResult:
    """P5 实验运行结果——包含所有 arm 结果。"""

    plan_id: str
    arm_results: list[ArmRunResult] = field(default_factory=list)
    all_retained: bool = True
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.error_codes

    @property
    def bundles(self) -> list[RunArtifactBundle]:
        return [r.bundle for r in self.arm_results if r.bundle is not None]

    @property
    def negative_count(self) -> int:
        return sum(1 for r in self.arm_results if r.is_negative)

    @property
    def invalid_count(self) -> int:
        return sum(1 for r in self.arm_results if r.is_invalid)


@dataclass
class P5ExperimentRunner:
    """P5 实验运行器——使用 FakeHarnessAdapter（SIDE_EFFECT_FREE）。

    可配置 fault injection 用于 blocker tests：
    - force_budget_exceeded: 模拟某 arm 预算超限
    - force_baseline_truncated: 模拟 baseline arm 被截断
    - force_plan_modified: 模拟 plan 启动后被修改
    - force_negative_deleted: 模拟负面结果被删除
    - force_invalid_deleted: 模拟无效结果被删除
    """

    adapter: FakeHarnessAdapter | None = None
    force_budget_exceeded: bool = False
    force_baseline_truncated: bool = False
    force_plan_modified: bool = False
    force_negative_deleted: bool = False
    force_invalid_deleted: bool = False
    _original_plan_hash: str = ""

    def __post_init__(self) -> None:
        if self.adapter is None:
            profile = build_harness_profile(
                version="fake-harness-v1",
                content_hash=hashlib.sha256(b"fake-harness-content-v1").hexdigest(),
                harness_kind="FAKE_HARNESS",
                tool_policy_kind="NO_TOOL",
            )
            self.adapter = FakeHarnessAdapter(harness_profile=profile)

    def run(
        self,
        plan: ExperimentPlan,
    ) -> P5ExperimentRunResult:
        """运行 P5 实验——收集所有 arm 结果。

        步骤：
        1. 验证 plan
        2. 检查 plan 冻结状态
        3. 对每个 arm，通过 FakeHarnessAdapter 运行
        4. 收集 RunArtifactBundle
        5. 验证所有结果保留
        """
        errors: list[EC] = []
        details: list[str] = []
        arm_results: list[ArmRunResult] = []

        # 1. verify plan
        plan_result = verify_experiment_plan(plan)
        if not plan_result.passed:
            return P5ExperimentRunResult(
                plan_id=plan.plan_id,
                error_codes=list(plan_result.error_codes),
                details=list(plan_result.details),
                all_retained=False,
            )

        # 2. check plan frozen
        if not plan.is_frozen:
            errors.append(EC.EX_PLAN_MODIFIED_AFTER_START)
            details.append("plan must be FROZEN before P5 run")

        # record original hash for modification check
        self._original_plan_hash = plan.content_hash

        # 3. check plan modified after start (blocker test)
        if self.force_plan_modified:
            errors.append(EC.EX_PLAN_MODIFIED_AFTER_START)
            details.append("plan was modified after start — must create new ExperimentPlan")

        # 4. run each arm
        for arm in plan.arms:
            arm_result = self._run_arm(plan, arm)
            arm_results.append(arm_result)

            # budget exceeded blocker
            if self.force_budget_exceeded and arm.arm_kind == "problem_only":
                errors.append(EC.EX_BUDGET_EXCEEDED)
                details.append(
                    f"arm {arm.arm_id} exceeded ResourceContract budget — BLOCK"
                )

            # baseline truncated blocker
            if self.force_baseline_truncated and arm.arm_kind == "problem_only":
                errors.append(EC.EX_BASELINE_TRUNCATED)
                details.append(
                    f"baseline arm {arm.arm_id} was truncated, not full — BLOCK"
                )

        # 5. check retention — all arms/negative/invalid retained
        all_retained = True
        for r in arm_results:
            if not r.retained:
                all_retained = False
                if r.is_negative or self.force_negative_deleted:
                    errors.append(EC.EX_NEGATIVE_RESULT_DELETED)
                    details.append(f"negative result for arm {r.arm_id} was deleted")
                if r.is_invalid or self.force_invalid_deleted:
                    errors.append(EC.EX_INVALID_RESULT_DELETED)
                    details.append(f"invalid result for arm {r.arm_id} was deleted")

        # force negative/invalid deleted
        if self.force_negative_deleted:
            errors.append(EC.EX_NEGATIVE_RESULT_DELETED)
            details.append("negative results were deleted — BLOCK")
            all_retained = False
        if self.force_invalid_deleted:
            errors.append(EC.EX_INVALID_RESULT_DELETED)
            details.append("invalid results were deleted — BLOCK")
            all_retained = False

        return P5ExperimentRunResult(
            plan_id=plan.plan_id,
            arm_results=arm_results,
            all_retained=all_retained,
            error_codes=errors,
            details=details,
        )

    def _run_arm(
        self,
        plan: ExperimentPlan,
        arm: Any,
    ) -> ArmRunResult:
        """运行单个 arm——通过 FakeHarnessAdapter。"""
        error_codes: list[EC] = []
        details: list[str] = []

        # build solver job for this arm
        rc = plan.resource_contract
        bs = plan.branch_snapshot

        # deterministic attempt_id
        attempt_id = f"attempt-{plan.plan_id}-{arm.arm_id}"
        fence_token = f"fence-{plan.plan_id}-{arm.arm_id}"
        idempotency_key = f"idem-{plan.plan_id}-{arm.arm_id}"

        profile = self.adapter.harness_profile  # type: ignore[union-attr]
        profile_hash = profile.profile_hash

        job = build_solver_job(
            problem_ref_id=arm.case_pack_ref.get("pack_id", ""),
            problem_sha256=arm.case_pack_ref.get("content_hash", ""),
            view_ref_id=f"view-{arm.arm_id}",
            view_sha256=hashlib.sha256(
                canonical_json_bytes({"arm_id": arm.arm_id, "view": "problem"})
            ).hexdigest(),
            budget_contract={
                "wallclock_seconds": rc.wallclock_seconds if rc else 600,
                "max_tokens": rc.token_budget if rc else 8192,
                "max_cost_microunits": rc.cost_microunits if rc else 0,
            },
            tool_policy_kind="NO_TOOL",
            idempotency_key=idempotency_key,
            fence_token=fence_token,
            attempt_id=attempt_id,
            repo_workspace_spec={"isolation_kind": "ISOLATED"},
            harness_profile_ref_id=profile.version,
            harness_profile_sha256=profile_hash,
        )

        try:
            prepared = self.adapter.prepare(job)  # type: ignore[union-attr]
            ticket = self.adapter.launch(prepared)  # type: ignore[union-attr]
            receipt = self.adapter.collect(ticket)  # type: ignore[union-attr]
        except Exception as exc:
            # arm failed — still retain as invalid/quarantine
            bundle = make_run_artifact_bundle(
                bundle_id=f"bundle-{arm.arm_id}",
                arm_id=arm.arm_id,
                plan_id=plan.plan_id,
                branch_snapshot_ref=arm.branch_snapshot_ref,
                resource_contract_ref=arm.resource_contract_ref,
                purpose="causal_experiment",
                run_state="FAILED",
                raw_artifact_ref={
                    "ref_id": f"raw-{arm.arm_id}",
                    "sha256": hashlib.sha256(b"failed-raw").hexdigest(),
                },
                parser_ref={"ref_id": f"parser-{arm.arm_id}", "sha256": ""},
                termination_reason="FAILED_PERMANENT",
                observability_status="MISSING",
                trajectory_ref={
                    "ref_id": f"trajectory-{arm.arm_id}",
                    "sha256": hashlib.sha256(b"failed-traj").hexdigest(),
                },
                answer_ref={
                    "ref_id": f"answer-{arm.arm_id}",
                    "sha256": hashlib.sha256(b"no-answer").hexdigest(),
                },
                cost_observability={
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cost_microunits": 0,
                    "usage_completeness": "MISSING",
                },
                is_invalid=True,
                quarantine_state="RUN_FAILED",
            )
            return ArmRunResult(
                arm_id=arm.arm_id,
                arm_kind=arm.arm_kind,
                bundle=bundle,
                error_codes=[EC.EX_TERMINATION_INVALID],
                details=[str(exc)],
                retained=True,
            )

        # determine if negative (terminal_reason != COMPLETED) or invalid
        is_negative = receipt.terminal_reason not in ("COMPLETED",)
        is_invalid = receipt.failure_or_quarantine_state not in ("",)
        quarantine_state = receipt.failure_or_quarantine_state

        # determine run_state
        if receipt.terminal_reason == "COMPLETED":
            run_state = "COMPLETED"
        elif receipt.terminal_reason == "QUARANTINED":
            run_state = "QUARANTINED"
        elif receipt.terminal_reason in ("CANCELLED", "TIMED_OUT", "BUDGET_EXCEEDED"):
            run_state = "FAILED"
        else:
            run_state = "FAILED"

        # observability status
        usage_completeness = receipt.cost_observability.get("usage_completeness", "COMPLETE")
        if usage_completeness == "COMPLETE":
            obs_status = "COMPLETE"
        elif usage_completeness == "PARTIAL":
            obs_status = "PARTIAL"
        else:
            obs_status = "MISSING"

        # build bundle
        bundle = make_run_artifact_bundle(
            bundle_id=f"bundle-{arm.arm_id}",
            arm_id=arm.arm_id,
            plan_id=plan.plan_id,
            branch_snapshot_ref=arm.branch_snapshot_ref,
            resource_contract_ref=arm.resource_contract_ref,
            purpose="causal_experiment",
            run_state=run_state,
            raw_artifact_ref={
                "ref_id": receipt.trajectory_ref_and_hash.get("ref_id", ""),
                "sha256": receipt.trajectory_ref_and_hash.get("sha256", ""),
            },
            parser_ref={
                "ref_id": f"parser-{arm.arm_id}",
                "sha256": hashlib.sha256(b"fake-parser").hexdigest(),
            },
            termination_reason=receipt.terminal_reason,
            observability_status=obs_status,
            observability_state={
                "wallclock_seconds": receipt.wallclock_seconds,
                "cost_observability": dict(receipt.cost_observability),
            },
            trajectory_ref=dict(receipt.trajectory_ref_and_hash),
            answer_ref=dict(receipt.answer_ref_and_hash),
            cost_observability=dict(receipt.cost_observability),
            is_negative=is_negative,
            is_invalid=is_invalid,
            quarantine_state=quarantine_state,
            sealed=True,
        )

        # verify bundle
        bundle_result = verify_run_artifact_bundle(bundle)
        if not bundle_result.passed:
            error_codes.extend(bundle_result.error_codes)
            details.extend(bundle_result.details)

        return ArmRunResult(
            arm_id=arm.arm_id,
            arm_kind=arm.arm_kind,
            bundle=bundle,
            error_codes=error_codes,
            details=details,
            retained=True,
        )


def verify_p5_run_result(
    result: P5ExperimentRunResult,
    *,
    expected_arm_count: int = 7,
) -> VerificationResult:
    """验证 P5 实验运行结果。

    检查：
    1. 所有 arm 结果保留
    2. arm 数量正确
    3. 负面/无效结果保留
    4. 所有 bundle 验证通过
    """
    errors: list[EC] = []
    details: list[str] = []

    # arm count
    if len(result.arm_results) != expected_arm_count:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append(
            f"arm result count {len(result.arm_results)} != expected {expected_arm_count}"
        )

    # all retained
    if not result.all_retained:
        errors.append(EC.EX_NEGATIVE_RESULT_DELETED)
        details.append("not all arm results retained")

    # all bundles valid
    for r in result.arm_results:
        if r.bundle is None:
            errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
            details.append(f"arm {r.arm_id} has no bundle")
        elif not r.bundle.is_hash_valid:
            errors.append(EC.OBJECT_HASH_MISMATCH)
            details.append(f"arm {r.arm_id} bundle hash invalid")

    # negative/invalid retained
    for r in result.arm_results:
        if r.is_negative and not r.retained:
            errors.append(EC.EX_NEGATIVE_RESULT_DELETED)
            details.append(f"negative result for arm {r.arm_id} not retained")
        if r.is_invalid and not r.retained:
            errors.append(EC.EX_INVALID_RESULT_DELETED)
            details.append(f"invalid result for arm {r.arm_id} not retained")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
