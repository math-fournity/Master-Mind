"""ExperimentArm — WP-EX1 单个实验对比臂。

关键约束（blocker）：
- arm_kind 在 EX_ARM_KINDS 中（EX_ARM_KIND_INVALID）
- 必须引用 CasePack（EX_CASE_PACK_REF_MISSING）
- 必须引用 StrategyRelease（EX_STRATEGY_RELEASE_REF_MISSING）
- 必须引用 ArmPayload（EX_ARM_REF_MISSING）
- 必须引用 ResourceContract（EX_RESOURCE_CONTRACT_NOT_FROZEN）
- 必须有 randomization assignment

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EX_ARM_KINDS,
    VerificationErrorCode as EC,
)


_SCHEMA_ID = "seven/experiment-arm"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class ExperimentArm:
    """单个实验对比臂。

    字段：
        arm_id: 唯一标识
        arm_kind: 臂种类（EX_ARM_KINDS: problem_only/lineage/direction/...）
        case_pack_ref: CasePack 引用 {pack_id, content_hash}
        strategy_release_ref: TellStrategyRelease 引用 {release_id, content_hash}
        arm_payload_ref: ArmPayload 引用 {arm_id, content_hash}
        resource_contract_ref: ResourceContract 引用 {contract_id, content_hash}
        branch_snapshot_ref: BranchSnapshot 引用 {snapshot_id, content_hash}
        randomization_assignment: 随机化分配位置（block position）
        content_hash: 内容哈希
    """

    arm_id: str
    arm_kind: str
    case_pack_ref: dict[str, str] = field(default_factory=dict)
    strategy_release_ref: dict[str, str] = field(default_factory=dict)
    arm_payload_ref: dict[str, str] = field(default_factory=dict)
    resource_contract_ref: dict[str, str] = field(default_factory=dict)
    branch_snapshot_ref: dict[str, str] = field(default_factory=dict)
    randomization_assignment: int = -1
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "arm_id": self.arm_id,
            "arm_kind": self.arm_kind,
            "case_pack_ref": dict(self.case_pack_ref),
            "strategy_release_ref": dict(self.strategy_release_ref),
            "arm_payload_ref": dict(self.arm_payload_ref),
            "resource_contract_ref": dict(self.resource_contract_ref),
            "branch_snapshot_ref": dict(self.branch_snapshot_ref),
            "randomization_assignment": self.randomization_assignment,
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


def make_experiment_arm(
    *,
    arm_id: str,
    arm_kind: str,
    case_pack_ref: dict[str, str] | None = None,
    strategy_release_ref: dict[str, str] | None = None,
    arm_payload_ref: dict[str, str] | None = None,
    resource_contract_ref: dict[str, str] | None = None,
    branch_snapshot_ref: dict[str, str] | None = None,
    randomization_assignment: int = -1,
) -> ExperimentArm:
    arm = ExperimentArm(
        arm_id=arm_id,
        arm_kind=arm_kind,
        case_pack_ref=case_pack_ref or {},
        strategy_release_ref=strategy_release_ref or {},
        arm_payload_ref=arm_payload_ref or {},
        resource_contract_ref=resource_contract_ref or {},
        branch_snapshot_ref=branch_snapshot_ref or {},
        randomization_assignment=randomization_assignment,
    )
    return dataclasses.replace(arm, content_hash=arm.compute_content_hash())


@dataclass(frozen=True)
class ExperimentArmVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    arm_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_experiment_arm(
    arm: ExperimentArm,
) -> ExperimentArmVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = arm.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # arm_kind valid
    if arm.arm_kind not in EX_ARM_KINDS:
        errors.append(EC.EX_ARM_KIND_INVALID)
        details.append(
            f"arm_kind '{arm.arm_kind}' not in {sorted(EX_ARM_KINDS)}"
        )

    # case_pack_ref required
    if not arm.case_pack_ref.get("pack_id"):
        errors.append(EC.EX_CASE_PACK_REF_MISSING)
        details.append("case_pack_ref must contain pack_id")
    if not arm.case_pack_ref.get("content_hash"):
        errors.append(EC.EX_CASE_PACK_REF_MISSING)
        details.append("case_pack_ref must contain content_hash")

    # strategy_release_ref required
    if not arm.strategy_release_ref.get("release_id"):
        errors.append(EC.EX_STRATEGY_RELEASE_REF_MISSING)
        details.append("strategy_release_ref must contain release_id")
    if not arm.strategy_release_ref.get("content_hash"):
        errors.append(EC.EX_STRATEGY_RELEASE_REF_MISSING)
        details.append("strategy_release_ref must contain content_hash")

    # arm_payload_ref required
    if not arm.arm_payload_ref.get("arm_id"):
        errors.append(EC.EX_ARM_REF_MISSING)
        details.append("arm_payload_ref must contain arm_id")
    if not arm.arm_payload_ref.get("content_hash"):
        errors.append(EC.EX_ARM_REF_MISSING)
        details.append("arm_payload_ref must contain content_hash")

    # resource_contract_ref required
    if not arm.resource_contract_ref.get("contract_id"):
        errors.append(EC.EX_RESOURCE_CONTRACT_NOT_FROZEN)
        details.append("resource_contract_ref must contain contract_id")
    if not arm.resource_contract_ref.get("content_hash"):
        errors.append(EC.EX_RESOURCE_CONTRACT_NOT_FROZEN)
        details.append("resource_contract_ref must contain content_hash")

    # branch_snapshot_ref required
    if not arm.branch_snapshot_ref.get("snapshot_id"):
        errors.append(EC.EX_BRANCH_SNAPSHOT_NOT_FROZEN)
        details.append("branch_snapshot_ref must contain snapshot_id")
    if not arm.branch_snapshot_ref.get("content_hash"):
        errors.append(EC.EX_BRANCH_SNAPSHOT_NOT_FROZEN)
        details.append("branch_snapshot_ref must contain content_hash")

    # randomization_assignment
    if arm.randomization_assignment < 0:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("randomization_assignment must be >= 0")

    # content_hash
    if not arm.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif arm.content_hash != arm.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {arm.content_hash}, "
            f"computed {arm.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return ExperimentArmVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        arm_id=arm.arm_id,
    )
