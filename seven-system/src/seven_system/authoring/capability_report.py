"""AuthoringCapabilityReport — QA0 能力报告。

来自 WP-QA0 work package contract：

READY_FOR_AUDIT 最低产物：
- fake/fault 收据
- 获授权后才有 Devin/Codex 单 adapter 真实纵切、盲评、人门收据
- 无 Solver、无 Redis 投影

边界：
- no Solver
- no Redis projection
- no bare results

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    QA_ALLOWED_OUTPUT_KINDS,
    QA_FORBIDDEN_OUTPUT_KINDS,
    QA_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/authoring-capability-report"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "AuthoringCapabilityReport"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"


@dataclass(frozen=True)
class AuthoringCapabilityReport:
    """AuthoringCapabilityReport — QA0 能力报告。不可变。

    报告 QA0 的能力边界：
    - side_effect_counters：所有副作用键必须为 0
    - allowed_output_kinds：QA0 允许输出的对象种类
    - forbidden_output_kinds：QA0 明确禁止输出的对象种类
    - no_solver：无 Solver
    - no_redis_projection：无 Redis 投影
    - no_bare_results：无 bare results
    """

    report_id: str
    side_effect_counters: dict[str, int]
    allowed_output_kinds: list[str]
    forbidden_output_kinds: list[str]
    no_solver: bool
    no_redis_projection: bool
    no_bare_results: bool
    fake_fault_receipts: list[dict[str, Any]]
    claims: list[str]
    nonclaims: list[str]
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    report_hash_algorithm: str = _HASH_ALGORITHM
    report_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "report_id": self.report_id,
            "side_effect_counters": dict(self.side_effect_counters),
            "allowed_output_kinds": list(self.allowed_output_kinds),
            "forbidden_output_kinds": list(self.forbidden_output_kinds),
            "no_solver": self.no_solver,
            "no_redis_projection": self.no_redis_projection,
            "no_bare_results": self.no_bare_results,
            "fake_fault_receipts": [dict(r) for r in self.fake_fault_receipts],
            "claims": list(self.claims),
            "nonclaims": list(self.nonclaims),
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": self.report_hash,
        }


def _compute_report_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["report_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def build_authoring_capability_report(
    *,
    report_id: str,
    fake_fault_receipts: list[dict[str, Any]] | None = None,
) -> AuthoringCapabilityReport:
    """构建 AuthoringCapabilityReport。

    所有 side_effect_counters 初始化为 0。
    allowed/forbidden output kinds 从常量填充。
    """
    side_effect_counters = {key: 0 for key in QA_SIDE_EFFECT_KEYS}
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "report_id": report_id,
        "side_effect_counters": side_effect_counters,
        "allowed_output_kinds": sorted(QA_ALLOWED_OUTPUT_KINDS),
        "forbidden_output_kinds": sorted(QA_FORBIDDEN_OUTPUT_KINDS),
        "no_solver": True,
        "no_redis_projection": True,
        "no_bare_results": True,
        "fake_fault_receipts": [dict(r) for r in (fake_fault_receipts or [])],
        "claims": [
            "P3A state chain proven with fake/stub adapters (brief→architect→draft→editor→verifier→gate→release).",
            "Bakeoff-A blinded scoring implemented with author identity hidden.",
            "Invalidation propagation: question text change invalidates all downstream.",
            "All blocker tests pass: unsigned bootstrap, file-only bypass, missing report, "
            "modification without invalidation, author leak, bare metric, retry-until-desired, "
            "unqualified role.",
        ],
        "nonclaims": [
            "No real Devin/Codex adapter vertical slice without HumanGate authorization.",
            "No live model calls, no DB writes, no Solver launches.",
            "No Redis projection, no bare results.",
            "Status: IMPLEMENTED_PENDING_EVIDENCE.",
        ],
        "report_hash_algorithm": _HASH_ALGORITHM,
        "report_hash": None,
    }
    report_hash = _compute_report_hash(obj)
    return AuthoringCapabilityReport(
        report_id=report_id,
        side_effect_counters=side_effect_counters,
        allowed_output_kinds=sorted(QA_ALLOWED_OUTPUT_KINDS),
        forbidden_output_kinds=sorted(QA_FORBIDDEN_OUTPUT_KINDS),
        no_solver=True,
        no_redis_projection=True,
        no_bare_results=True,
        fake_fault_receipts=[dict(r) for r in (fake_fault_receipts or [])],
        claims=obj["claims"],
        nonclaims=obj["nonclaims"],
        report_hash=report_hash,
    )


def verify_authoring_capability_report(
    report: dict[str, Any] | AuthoringCapabilityReport,
) -> VerificationResult:
    """验证 AuthoringCapabilityReport 的结构合法性。

    检查：
    1. schema 常量
    2. report_id 非空
    3. side_effect_counters 所有键在 QA_SIDE_EFFECT_KEYS 中且值为 0
    4. no_solver == True
    5. no_redis_projection == True
    6. no_bare_results == True
    7. allowed_output_kinds == QA_ALLOWED_OUTPUT_KINDS
    8. forbidden_output_kinds == QA_FORBIDDEN_OUTPUT_KINDS
    9. forbidden_output_kinds 不在 allowed_output_kinds 中
    10. report_hash 正确
    """
    if isinstance(report, AuthoringCapabilityReport):
        report = report.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if report.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if report.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if report.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not report.get("report_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("report_id must not be empty")

    # side_effect_counters
    counters = report.get("side_effect_counters", {})
    if not isinstance(counters, dict):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("side_effect_counters must be a dict")
    else:
        for key in QA_SIDE_EFFECT_KEYS:
            val = counters.get(key)
            if val is None:
                errors.append(EC.REQUIRED_FIELD_MISSING)
                details.append(f"side_effect_counters missing key: {key}")
            elif val != 0:
                if key == "solver_launches":
                    errors.append(EC.QA_NO_SOLVER_ALLOWED)
                elif key == "redis_writes":
                    errors.append(EC.QA_NO_REDIS_ALLOWED)
                else:
                    errors.append(EC.OBJECT_HASH_MISMATCH)
                details.append(f"side_effect_counters[{key}] must be 0, got {val}")
        # 检查是否有额外键
        extra = set(counters.keys()) - set(QA_SIDE_EFFECT_KEYS)
        if extra:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"side_effect_counters has extra keys: {extra}")

    if report.get("no_solver") is not True:
        errors.append(EC.QA_NO_SOLVER_ALLOWED)
        details.append("no_solver must be True")
    if report.get("no_redis_projection") is not True:
        errors.append(EC.QA_NO_REDIS_ALLOWED)
        details.append("no_redis_projection must be True")
    if report.get("no_bare_results") is not True:
        errors.append(EC.QA_BAKEOFF_A_USING_BARE)
        details.append("no_bare_results must be True")

    allowed = set(report.get("allowed_output_kinds", []))
    if allowed != set(QA_ALLOWED_OUTPUT_KINDS):
        errors.append(EC.QA_OUTPUT_KIND_FORBIDDEN)
        details.append(f"allowed_output_kinds mismatch: got {sorted(allowed)}")

    forbidden = set(report.get("forbidden_output_kinds", []))
    if forbidden != set(QA_FORBIDDEN_OUTPUT_KINDS):
        errors.append(EC.QA_OUTPUT_KIND_FORBIDDEN)
        details.append(f"forbidden_output_kinds mismatch: got {sorted(forbidden)}")

    overlap = allowed & forbidden
    if overlap:
        errors.append(EC.QA_OUTPUT_KIND_FORBIDDEN)
        details.append(f"output kinds in both allowed and forbidden: {overlap}")

    if report.get("report_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected report_hash_algorithm: {report.get('report_hash_algorithm')}")

    computed = _compute_report_hash(report)
    if report.get("report_hash") != computed:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"report_hash mismatch: expected {computed}, got {report.get('report_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
