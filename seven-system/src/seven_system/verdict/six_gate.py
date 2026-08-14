"""SixGateVerdict — P9 六门审计 verdict。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

SixGateVerdict 及 NOT_TESTED。每门独立评估。
NOT_TESTED 不得当作 PASS。

关键约束（blocker）：
- NOT_TESTED 当作 PASS → VR_NOT_TESTED_AS_PASS
- 门不在合法集合 → VR_GATE_INVALID
- 门不独立评估 → VR_GATE_NOT_INDEPENDENT

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    VR_GATE_KINDS,
    VR_GATE_STATUSES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/six-gate-verdict"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class GateVerdict:
    """单门 verdict。"""

    gate_kind: str  # G_P0_READINESS | G_P1_DRYRUN | ...
    status: str  # PASS | FAIL | NOT_TESTED | BLOCKED
    reason: str = ""
    evidence_refs: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "gate_kind": self.gate_kind,
            "status": self.status,
            "reason": self.reason,
            "evidence_refs": list(self.evidence_refs),
        }


@dataclass(frozen=True)
class SixGateVerdict:
    """P9 六门审计 verdict。

    六门独立评估。NOT_TESTED 不得当作 PASS。

    字段：
        verdict_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        gates: 六门 verdict
        overall_status: 综合状态（取最严状态）
        hash_algorithm: 哈希算法
        content_hash: verdict 自身内容哈希
    """

    verdict_id: str
    dag_hash: str = ""
    gates: tuple[GateVerdict, ...] = ()
    overall_status: str = "NOT_TESTED"
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "verdict_id": self.verdict_id,
            "dag_hash": self.dag_hash,
            "gates": [g.to_dict() for g in self.gates],
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

    def get_gate(self, gate_kind: str) -> GateVerdict | None:
        for g in self.gates:
            if g.gate_kind == gate_kind:
                return g
        return None


_GATE_STATUS_PRIORITY: dict[str, int] = {
    "PASS": 0,
    "NOT_TESTED": 1,
    "FAIL": 2,
    "BLOCKED": 3,
}


def _compute_gate_overall_status(gates: list[GateVerdict]) -> str:
    """综合状态取最严状态。"""
    if not gates:
        return "NOT_TESTED"
    max_priority = 0
    for g in gates:
        priority = _GATE_STATUS_PRIORITY.get(g.status, 3)
        if priority > max_priority:
            max_priority = priority
    for status, priority in _GATE_STATUS_PRIORITY.items():
        if priority == max_priority:
            return status
    return "BLOCKED"


def make_six_gate_verdict(
    *,
    verdict_id: str,
    dag_hash: str,
    gate_statuses: dict[str, str],
    gate_reasons: dict[str, str] | None = None,
    gate_evidence_refs: dict[str, list[str]] | None = None,
) -> SixGateVerdict:
    """构建 SixGateVerdict。

    六门独立评估，overall_status 取最严状态。
    """
    gate_reasons = gate_reasons or {}
    gate_evidence_refs = gate_evidence_refs or {}
    gates: list[GateVerdict] = []
    for gate_kind in sorted(VR_GATE_KINDS):
        status = gate_statuses.get(gate_kind, "NOT_TESTED")
        reason = gate_reasons.get(gate_kind, "")
        refs = tuple(gate_evidence_refs.get(gate_kind, ()))
        gates.append(
            GateVerdict(
                gate_kind=gate_kind,
                status=status,
                reason=reason,
                evidence_refs=refs,
            )
        )
    overall = _compute_gate_overall_status(gates)
    verdict = SixGateVerdict(
        verdict_id=verdict_id,
        dag_hash=dag_hash,
        gates=tuple(gates),
        overall_status=overall,
    )
    return dataclasses.replace(
        verdict, content_hash=verdict.compute_content_hash()
    )


def verify_six_gate_verdict(verdict: SixGateVerdict) -> VerificationResult:
    """验证 SixGateVerdict。

    blocker：
    - 门不在合法集合 → VR_GATE_INVALID
    - 状态不在合法集合 → VR_GATE_INVALID
    - NOT_TESTED 当作 PASS → VR_NOT_TESTED_AS_PASS
    - 门不独立 → VR_GATE_NOT_INDEPENDENT
    - overall_status 不是最严 → VR_NOT_TESTED_AS_PASS / VR_PASS_AVERAGED_FAIL
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

    # 验证六门存在且合法
    gate_kinds = {g.gate_kind for g in verdict.gates}
    if gate_kinds != VR_GATE_KINDS:
        errors.append(EC.VR_GATE_INVALID)
        details.append(
            f"gates must be exactly {sorted(VR_GATE_KINDS)}, "
            f"got {sorted(gate_kinds)}"
        )

    has_not_tested = False
    for g in verdict.gates:
        if g.gate_kind not in VR_GATE_KINDS:
            errors.append(EC.VR_GATE_INVALID)
            details.append(f"unknown gate_kind {g.gate_kind}")
        if g.status not in VR_GATE_STATUSES:
            errors.append(EC.VR_GATE_INVALID)
            details.append(
                f"unknown status {g.status} for gate {g.gate_kind}"
            )
        if g.status == "NOT_TESTED":
            has_not_tested = True

    # NOT_TESTED 当作 PASS
    if has_not_tested and verdict.overall_status == "PASS":
        errors.append(EC.VR_NOT_TESTED_AS_PASS)
        details.append(
            "overall_status is PASS but some gates are NOT_TESTED — "
            "NOT_TESTED must not be treated as PASS"
        )

    # overall_status 必须是最严状态
    expected_overall = _compute_gate_overall_status(list(verdict.gates))
    if verdict.overall_status != expected_overall:
        errors.append(EC.VR_NOT_TESTED_AS_PASS)
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
        details.append("SixGateVerdict content_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )


def check_gate_not_tested_not_pass(
    verdict: SixGateVerdict,
) -> VerificationResult:
    """检查门的 NOT_TESTED 不被当作 PASS。"""
    errors: list[EC] = []
    details: list[str] = []
    has_not_tested = any(g.status == "NOT_TESTED" for g in verdict.gates)
    if has_not_tested and verdict.overall_status == "PASS":
        errors.append(EC.VR_NOT_TESTED_AS_PASS)
        details.append(
            "NOT_TESTED gate treated as PASS in overall_status — forbidden"
        )
    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )
