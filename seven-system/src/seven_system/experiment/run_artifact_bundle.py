"""RunArtifactBundle — WP-EX1 每个 arm 的密封产物包。

关键约束（blocker）：
- 每个 arm 一个 sealed bundle（EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE）
- purpose=causal_experiment 必须引用 arm, ExperimentPlan, BranchSnapshot, ResourceContract
- raw artifact, parser, termination, hash, observability state 齐全
- termination reason 在 EX_TERMINATION_REASONS 中（EX_TERMINATION_INVALID）
- observability status 在 EX_OBSERVABILITY_STATUSES 中（EX_OBSERVABILITY_INCOMPLETE）
- quarantine 状态合法（EX_QUARANTINE_INVALID）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EX_OBSERVABILITY_STATUSES,
    EX_PURPOSE_KINDS,
    EX_RUN_STATES,
    EX_TERMINATION_REASONS,
    VerificationErrorCode as EC,
)


_SCHEMA_ID = "seven/run-artifact-bundle"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class RunArtifactBundle:
    """密封产物包——每个 arm 一个。

    字段：
        bundle_id: 唯一标识
        arm_id: 对应的 ExperimentArm ID
        plan_id: 对应的 ExperimentPlan ID
        branch_snapshot_ref: BranchSnapshot 引用 {snapshot_id, content_hash}
        resource_contract_ref: ResourceContract 引用 {contract_id, content_hash}
        purpose: 用途（EX_PURPOSE_KINDS: causal_experiment/bare_baseline/calibration）
        run_state: run 状态（EX_RUN_STATES）
        raw_artifact_ref: 原始产物引用 {ref_id, sha256}
        parser_ref: parser 引用 {ref_id, sha256}
        termination_reason: 终止原因（EX_TERMINATION_REASONS）
        observability_status: 可观察性状态（EX_OBSERVABILITY_STATUSES）
        observability_state: 可观察性详细状态
        trajectory_ref: trajectory 引用 {ref_id, sha256}
        answer_ref: answer 引用 {ref_id, sha256}
        cost_observability: 成本可观察性
        is_negative: 是否为负面结果
        is_invalid: 是否为无效结果
        quarantine_state: 隔离状态（空字符串表示无隔离）
        sealed: 是否已密封
        content_hash: 内容哈希
    """

    bundle_id: str
    arm_id: str
    plan_id: str
    branch_snapshot_ref: dict[str, str] = field(default_factory=dict)
    resource_contract_ref: dict[str, str] = field(default_factory=dict)
    purpose: str = "causal_experiment"
    run_state: str = "COMPLETED"
    raw_artifact_ref: dict[str, str] = field(default_factory=dict)
    parser_ref: dict[str, str] = field(default_factory=dict)
    termination_reason: str = "COMPLETED"
    observability_status: str = "COMPLETE"
    observability_state: dict[str, Any] = field(default_factory=dict)
    trajectory_ref: dict[str, str] = field(default_factory=dict)
    answer_ref: dict[str, str] = field(default_factory=dict)
    cost_observability: dict[str, Any] = field(default_factory=dict)
    is_negative: bool = False
    is_invalid: bool = False
    quarantine_state: str = ""
    sealed: bool = True
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "bundle_id": self.bundle_id,
            "arm_id": self.arm_id,
            "plan_id": self.plan_id,
            "branch_snapshot_ref": dict(self.branch_snapshot_ref),
            "resource_contract_ref": dict(self.resource_contract_ref),
            "purpose": self.purpose,
            "run_state": self.run_state,
            "raw_artifact_ref": dict(self.raw_artifact_ref),
            "parser_ref": dict(self.parser_ref),
            "termination_reason": self.termination_reason,
            "observability_status": self.observability_status,
            "observability_state": dict(self.observability_state),
            "trajectory_ref": dict(self.trajectory_ref),
            "answer_ref": dict(self.answer_ref),
            "cost_observability": dict(self.cost_observability),
            "is_negative": self.is_negative,
            "is_invalid": self.is_invalid,
            "quarantine_state": self.quarantine_state,
            "sealed": self.sealed,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


def make_run_artifact_bundle(
    *,
    bundle_id: str,
    arm_id: str,
    plan_id: str,
    branch_snapshot_ref: dict[str, str] | None = None,
    resource_contract_ref: dict[str, str] | None = None,
    purpose: str = "causal_experiment",
    run_state: str = "COMPLETED",
    raw_artifact_ref: dict[str, str] | None = None,
    parser_ref: dict[str, str] | None = None,
    termination_reason: str = "COMPLETED",
    observability_status: str = "COMPLETE",
    observability_state: dict[str, Any] | None = None,
    trajectory_ref: dict[str, str] | None = None,
    answer_ref: dict[str, str] | None = None,
    cost_observability: dict[str, Any] | None = None,
    is_negative: bool = False,
    is_invalid: bool = False,
    quarantine_state: str = "",
    sealed: bool = True,
) -> RunArtifactBundle:
    bundle = RunArtifactBundle(
        bundle_id=bundle_id,
        arm_id=arm_id,
        plan_id=plan_id,
        branch_snapshot_ref=branch_snapshot_ref or {},
        resource_contract_ref=resource_contract_ref or {},
        purpose=purpose,
        run_state=run_state,
        raw_artifact_ref=raw_artifact_ref or {},
        parser_ref=parser_ref or {},
        termination_reason=termination_reason,
        observability_status=observability_status,
        observability_state=observability_state or {},
        trajectory_ref=trajectory_ref or {},
        answer_ref=answer_ref or {},
        cost_observability=cost_observability or {},
        is_negative=is_negative,
        is_invalid=is_invalid,
        quarantine_state=quarantine_state,
        sealed=sealed,
    )
    return dataclasses.replace(bundle, content_hash=bundle.compute_content_hash())


@dataclass(frozen=True)
class RunArtifactBundleVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    bundle_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_run_artifact_bundle(
    bundle: RunArtifactBundle,
) -> RunArtifactBundleVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = bundle.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # arm_id required
    if not bundle.arm_id:
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("arm_id is empty")

    # plan_id required
    if not bundle.plan_id:
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("plan_id is empty")

    # purpose valid
    if bundle.purpose not in EX_PURPOSE_KINDS:
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append(
            f"purpose '{bundle.purpose}' not in {sorted(EX_PURPOSE_KINDS)}"
        )

    # purpose=causal_experiment must reference arm, plan, branch, resource
    if bundle.purpose == "causal_experiment":
        if not bundle.arm_id:
            errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
            details.append("causal_experiment purpose requires arm_id")
        if not bundle.plan_id:
            errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
            details.append("causal_experiment purpose requires plan_id")
        if not bundle.branch_snapshot_ref.get("snapshot_id"):
            errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
            details.append("causal_experiment purpose requires branch_snapshot_ref.snapshot_id")
        if not bundle.branch_snapshot_ref.get("content_hash"):
            errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
            details.append("causal_experiment purpose requires branch_snapshot_ref.content_hash")
        if not bundle.resource_contract_ref.get("contract_id"):
            errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
            details.append("causal_experiment purpose requires resource_contract_ref.contract_id")
        if not bundle.resource_contract_ref.get("content_hash"):
            errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
            details.append("causal_experiment purpose requires resource_contract_ref.content_hash")

    # run_state valid
    if bundle.run_state not in EX_RUN_STATES:
        errors.append(EC.EX_RUN_STATE_INVALID)
        details.append(
            f"run_state '{bundle.run_state}' not in {sorted(EX_RUN_STATES)}"
        )

    # raw_artifact_ref required
    if not bundle.raw_artifact_ref.get("ref_id"):
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("raw_artifact_ref must contain ref_id")
    if not bundle.raw_artifact_ref.get("sha256"):
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("raw_artifact_ref must contain sha256")

    # parser_ref required
    if not bundle.parser_ref.get("ref_id"):
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("parser_ref must contain ref_id")

    # trajectory_ref required
    if not bundle.trajectory_ref.get("ref_id"):
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("trajectory_ref must contain ref_id")
    if not bundle.trajectory_ref.get("sha256"):
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("trajectory_ref must contain sha256")

    # answer_ref required
    if not bundle.answer_ref.get("ref_id"):
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("answer_ref must contain ref_id")
    if not bundle.answer_ref.get("sha256"):
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("answer_ref must contain sha256")

    # termination_reason valid
    if bundle.termination_reason not in EX_TERMINATION_REASONS:
        errors.append(EC.EX_TERMINATION_INVALID)
        details.append(
            f"termination_reason '{bundle.termination_reason}' not in "
            f"{sorted(EX_TERMINATION_REASONS)}"
        )

    # observability_status valid
    if bundle.observability_status not in EX_OBSERVABILITY_STATUSES:
        errors.append(EC.EX_OBSERVABILITY_INCOMPLETE)
        details.append(
            f"observability_status '{bundle.observability_status}' not in "
            f"{sorted(EX_OBSERVABILITY_STATUSES)}"
        )

    # quarantine state valid — if non-empty, run_state must be QUARANTINED or INVALID
    if bundle.quarantine_state:
        if bundle.run_state not in ("QUARANTINED", "INVALID", "FAILED"):
            errors.append(EC.EX_QUARANTINE_INVALID)
            details.append(
                f"quarantine_state set but run_state is {bundle.run_state} — "
                f"must be QUARANTINED, INVALID, or FAILED"
            )

    # sealed check
    if not bundle.sealed:
        errors.append(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE)
        details.append("bundle must be sealed")

    # content_hash
    if not bundle.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif bundle.content_hash != bundle.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {bundle.content_hash}, "
            f"computed {bundle.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return RunArtifactBundleVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        bundle_id=bundle.bundle_id,
    )
