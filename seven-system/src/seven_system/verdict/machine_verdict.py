"""MachineVerdict — P9 分轴 Machine Verdict（Factory/Scientific/Scale）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

Factory 轴（系统完备性）和 Scientific 轴（证据质量）是分离的。
Scale 轴用于生产就绪。三轴独立评估，不得平均 PASS 和 FAIL。

关键约束（blocker）：
- PASS 平均 FAIL（factory PASS + scientific FAIL averaged to PASS）→ VR_PASS_AVERAGED_FAIL
- NOT_TESTED 当作 PASS → VR_NOT_TESTED_AS_PASS
- 轴不在合法集合 → VR_AXIS_INVALID

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
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


_SCHEMA_ID = "seven/machine-verdict"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class AxisVerdict:
    """单轴 verdict。"""

    axis: str  # FACTORY | SCIENTIFIC | SCALE
    status: str  # PASS | FAIL | NOT_TESTED | BLOCKED
    reason: str = ""
    evidence_refs: tuple[str, ...] = ()  # 引用的 evidence hash

    def to_dict(self) -> dict[str, Any]:
        return {
            "axis": self.axis,
            "status": self.status,
            "reason": self.reason,
            "evidence_refs": list(self.evidence_refs),
        }


@dataclass(frozen=True)
class MachineVerdict:
    """P9 分轴 Machine Verdict。

    Factory/Scientific/Scale 三轴独立评估。
    不得平均 PASS 和 FAIL。

    字段：
        verdict_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        axes: 三轴 verdict（FACTORY, SCIENTIFIC, SCALE）
        overall_status: 综合状态（不得是平均——取最严状态）
        hash_algorithm: 哈希算法
        content_hash: verdict 自身内容哈希
    """

    verdict_id: str
    dag_hash: str = ""
    axes: tuple[AxisVerdict, ...] = ()
    overall_status: str = "NOT_TESTED"
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "verdict_id": self.verdict_id,
            "dag_hash": self.dag_hash,
            "axes": [ax.to_dict() for ax in self.axes],
            "overall_status": self.overall_status,
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

    def get_axis(self, axis: str) -> AxisVerdict | None:
        for ax in self.axes:
            if ax.axis == axis:
                return ax
        return None


# 综合状态优先级——取最严状态，不是平均
# BLOCKED > FAIL > NOT_TESTED > PASS
_STATUS_PRIORITY: dict[str, int] = {
    "PASS": 0,
    "NOT_TESTED": 1,
    "FAIL": 2,
    "BLOCKED": 3,
}


def _compute_overall_status(axes: list[AxisVerdict]) -> str:
    """综合状态取最严状态，不是平均。"""
    if not axes:
        return "NOT_TESTED"
    # 如果任一轴 BLOCKED → BLOCKED
    # 如果任一轴 FAIL → FAIL
    # 如果任一轴 NOT_TESTED → NOT_TESTED
    # 只有全 PASS → PASS
    max_priority = 0
    for ax in axes:
        priority = _STATUS_PRIORITY.get(ax.status, 3)
        if priority > max_priority:
            max_priority = priority
    # 反查
    for status, priority in _STATUS_PRIORITY.items():
        if priority == max_priority:
            return status
    return "BLOCKED"


def make_machine_verdict(
    *,
    verdict_id: str,
    dag_hash: str,
    factory_status: str,
    scientific_status: str,
    scale_status: str,
    factory_reason: str = "",
    scientific_reason: str = "",
    scale_reason: str = "",
    factory_evidence_refs: list[str] | None = None,
    scientific_evidence_refs: list[str] | None = None,
    scale_evidence_refs: list[str] | None = None,
) -> MachineVerdict:
    """构建 MachineVerdict。

    三轴独立评估，overall_status 取最严状态（不是平均）。
    """
    axes = (
        AxisVerdict(
            axis="FACTORY",
            status=factory_status,
            reason=factory_reason,
            evidence_refs=tuple(factory_evidence_refs or ()),
        ),
        AxisVerdict(
            axis="SCIENTIFIC",
            status=scientific_status,
            reason=scientific_reason,
            evidence_refs=tuple(scientific_evidence_refs or ()),
        ),
        AxisVerdict(
            axis="SCALE",
            status=scale_status,
            reason=scale_reason,
            evidence_refs=tuple(scale_evidence_refs or ()),
        ),
    )
    overall = _compute_overall_status(list(axes))
    verdict = MachineVerdict(
        verdict_id=verdict_id,
        dag_hash=dag_hash,
        axes=axes,
        overall_status=overall,
    )
    return dataclasses.replace(
        verdict, content_hash=verdict.compute_content_hash()
    )


def verify_machine_verdict(verdict: MachineVerdict) -> VerificationResult:
    """验证 MachineVerdict。

    blocker：
    - 轴不在合法集合 → VR_AXIS_INVALID
    - 状态不在合法集合 → VR_GATE_INVALID
    - PASS 平均 FAIL → VR_PASS_AVERAGED_FAIL
    - NOT_TESTED 当作 PASS → VR_NOT_TESTED_AS_PASS
    - overall_status 不是最严状态 → VR_PASS_AVERAGED_FAIL
    - content_hash 不匹配 → VR_VERDICT_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = verdict.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not verdict.verdict_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("verdict_id is empty")

    if not verdict.dag_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("dag_hash is empty")

    # 验证三轴存在且合法
    axis_names = {ax.axis for ax in verdict.axes}
    if axis_names != VR_VERDICT_AXES:
        errors.append(EC.VR_AXIS_INVALID)
        details.append(
            f"axes must be exactly {sorted(VR_VERDICT_AXES)}, "
            f"got {sorted(axis_names)}"
        )

    has_pass = False
    has_fail = False
    has_not_tested = False

    for ax in verdict.axes:
        if ax.axis not in VR_VERDICT_AXES:
            errors.append(EC.VR_AXIS_INVALID)
            details.append(f"unknown axis {ax.axis}")
        if ax.status not in VR_VERDICT_STATUSES:
            errors.append(EC.VR_GATE_INVALID)
            details.append(
                f"unknown status {ax.status} for axis {ax.axis}"
            )
        if ax.status == "PASS":
            has_pass = True
        if ax.status == "FAIL":
            has_fail = True
        if ax.status == "NOT_TESTED":
            has_not_tested = True

    # PASS 平均 FAIL：如果某轴 PASS 某轴 FAIL，overall 不得是 PASS
    if has_pass and has_fail:
        if verdict.overall_status == "PASS":
            errors.append(EC.VR_PASS_AVERAGED_FAIL)
            details.append(
                "overall_status is PASS but some axes are FAIL — "
                "cannot average PASS with FAIL"
            )

    # NOT_TESTED 当作 PASS：如果有 NOT_TESTED 轴，overall 不得是 PASS
    if has_not_tested and verdict.overall_status == "PASS":
        errors.append(EC.VR_NOT_TESTED_AS_PASS)
        details.append(
            "overall_status is PASS but some axes are NOT_TESTED — "
            "NOT_TESTED must not be treated as PASS"
        )

    # overall_status 必须是最严状态
    expected_overall = _compute_overall_status(list(verdict.axes))
    if verdict.overall_status != expected_overall:
        errors.append(EC.VR_PASS_AVERAGED_FAIL)
        details.append(
            f"overall_status {verdict.overall_status} != "
            f"expected strictest {expected_overall}"
        )

    # content_hash
    if not verdict.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif verdict.content_hash != verdict.compute_content_hash():
        errors.append(EC.VR_VERDICT_HASH_MISMATCH)
        details.append("MachineVerdict content_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


def check_no_pass_averaged_fail(verdict: MachineVerdict) -> VerificationResult:
    """检查 PASS 不与 FAIL 平均。"""
    errors: list[EC] = []
    details: list[str] = []
    has_pass = any(ax.status == "PASS" for ax in verdict.axes)
    has_fail = any(ax.status == "FAIL" for ax in verdict.axes)
    if has_pass and has_fail and verdict.overall_status == "PASS":
        errors.append(EC.VR_PASS_AVERAGED_FAIL)
        details.append(
            "factory PASS + scientific FAIL averaged to PASS — forbidden"
        )
    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


def check_not_tested_not_pass(verdict: MachineVerdict) -> VerificationResult:
    """检查 NOT_TESTED 不被当作 PASS。"""
    errors: list[EC] = []
    details: list[str] = []
    has_not_tested = any(ax.status == "NOT_TESTED" for ax in verdict.axes)
    if has_not_tested and verdict.overall_status == "PASS":
        errors.append(EC.VR_NOT_TESTED_AS_PASS)
        details.append(
            "NOT_TESTED axis treated as PASS in overall_status — forbidden"
        )
    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )
