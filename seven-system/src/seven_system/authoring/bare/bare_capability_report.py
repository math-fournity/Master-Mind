"""BareCapabilityReport — QA1 P3B bare admission 能力报告（WP-QA1）。

来自 WP-QA1 work package contract：

READY_FOR_AUDIT 最低产物：
- 全结果收据、盲化Bakeoff-B；无P5 claim

边界：
- no P5 claim
- no Tell/Hint
- no confirmatory Evidence

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    QA1_ALLOWED_OUTPUT_KINDS,
    QA1_FORBIDDEN_OUTPUT_KINDS,
    QA1_SIDE_EFFECT_KEYS,
    QA1_CHECK_IDS,
    QA1_CLAIMS,
    QA1_NONCLAIMS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/bare-capability-report"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "BareCapabilityReport"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"


@dataclass(frozen=True)
class BareCapabilityReport:
    """BareCapabilityReport — QA1 P3B bare admission 能力报告。不可变。

    报告 QA1 的能力边界：
    - side_effect_counters：所有副作用键必须为 0
    - allowed_output_kinds：QA1 允许输出的对象种类
    - forbidden_output_kinds：QA1 明确禁止输出的对象种类
    - no_p5_claim：无 P5 claim
    - no_tell_hint：无 Tell/Hint
    - no_confirmatory_evidence：无 confirmatory Evidence
    """

    report_id: str
    side_effect_counters: dict[str, int]
    allowed_output_kinds: list[str]
    forbidden_output_kinds: list[str]
    no_p5_claim: bool
    no_tell_hint: bool
    no_confirmatory_evidence: bool
    check_ids: list[str]
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
            "no_p5_claim": self.no_p5_claim,
            "no_tell_hint": self.no_tell_hint,
            "no_confirmatory_evidence": self.no_confirmatory_evidence,
            "check_ids": list(self.check_ids),
            "claims": list(self.claims),
            "nonclaims": list(self.nonclaims),
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": self.report_hash,
        }


def _compute_report_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["report_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def build_bare_capability_report(
    *,
    report_id: str,
) -> BareCapabilityReport:
    """构建 BareCapabilityReport。

    所有 side_effect_counters 初始化为 0。
    allowed/forbidden output kinds 从常量填充。
    no_p5_claim / no_tell_hint / no_confirmatory_evidence 固定为 True。
    """
    side_effect_counters = {key: 0 for key in QA1_SIDE_EFFECT_KEYS}
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "report_id": report_id,
        "side_effect_counters": side_effect_counters,
        "allowed_output_kinds": sorted(QA1_ALLOWED_OUTPUT_KINDS),
        "forbidden_output_kinds": sorted(QA1_FORBIDDEN_OUTPUT_KINDS),
        "no_p5_claim": True,
        "no_tell_hint": True,
        "no_confirmatory_evidence": True,
        "check_ids": list(QA1_CHECK_IDS),
        "claims": list(QA1_CLAIMS),
        "nonclaims": list(QA1_NONCLAIMS),
        "report_hash_algorithm": _HASH_ALGORITHM,
        "report_hash": None,
    }
    report_hash = _compute_report_hash(obj)
    return BareCapabilityReport(
        report_id=report_id,
        side_effect_counters=side_effect_counters,
        allowed_output_kinds=sorted(QA1_ALLOWED_OUTPUT_KINDS),
        forbidden_output_kinds=sorted(QA1_FORBIDDEN_OUTPUT_KINDS),
        no_p5_claim=True,
        no_tell_hint=True,
        no_confirmatory_evidence=True,
        check_ids=list(QA1_CHECK_IDS),
        claims=list(QA1_CLAIMS),
        nonclaims=list(QA1_NONCLAIMS),
        report_hash=report_hash,
    )


def verify_bare_capability_report(
    report: dict[str, Any] | BareCapabilityReport,
) -> VerificationResult:
    """验证 BareCapabilityReport 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. report_id 非空
    3. side_effect_counters 所有键在 QA1_SIDE_EFFECT_KEYS 中且值为 0
    4. no_p5_claim == True（blocker: P5 claim in bare report）
    5. no_tell_hint == True
    6. no_confirmatory_evidence == True
    7. allowed_output_kinds == QA1_ALLOWED_OUTPUT_KINDS
    8. forbidden_output_kinds == QA1_FORBIDDEN_OUTPUT_KINDS
    9. forbidden_output_kinds 不在 allowed_output_kinds 中
    10. claims 不含 P5 claim
    11. report_hash 正确
    """
    if isinstance(report, BareCapabilityReport):
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
        for key in QA1_SIDE_EFFECT_KEYS:
            val = counters.get(key)
            if val is None:
                errors.append(EC.REQUIRED_FIELD_MISSING)
                details.append(f"side_effect_counters missing key: {key}")
            elif val != 0:
                errors.append(EC.OBJECT_HASH_MISMATCH)
                details.append(f"side_effect_counters[{key}] must be 0, got {val}")
        extra = set(counters.keys()) - set(QA1_SIDE_EFFECT_KEYS)
        if extra:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"side_effect_counters has extra keys: {extra}")

    # no_p5_claim (blocker: P5 claim in bare report)
    if report.get("no_p5_claim") is not True:
        errors.append(EC.QA1_P5_CLAIM_IN_BARE_REPORT)
        details.append("no_p5_claim must be True")

    # no_tell_hint
    if report.get("no_tell_hint") is not True:
        errors.append(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE)
        details.append("no_tell_hint must be True")

    # no_confirmatory_evidence
    if report.get("no_confirmatory_evidence") is not True:
        errors.append(EC.QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE)
        details.append("no_confirmatory_evidence must be True")

    # allowed_output_kinds
    allowed = set(report.get("allowed_output_kinds", []))
    if allowed != set(QA1_ALLOWED_OUTPUT_KINDS):
        errors.append(EC.QA1_OUTPUT_KIND_FORBIDDEN)
        details.append(f"allowed_output_kinds mismatch: got {sorted(allowed)}")

    # forbidden_output_kinds
    forbidden = set(report.get("forbidden_output_kinds", []))
    if forbidden != set(QA1_FORBIDDEN_OUTPUT_KINDS):
        errors.append(EC.QA1_OUTPUT_KIND_FORBIDDEN)
        details.append(f"forbidden_output_kinds mismatch: got {sorted(forbidden)}")

    overlap = allowed & forbidden
    if overlap:
        errors.append(EC.QA1_OUTPUT_KIND_FORBIDDEN)
        details.append(f"output kinds in both allowed and forbidden: {overlap}")

    # claims must not contain P5 claim
    claims = report.get("claims", [])
    for claim in claims:
        claim_lower = claim.lower()
        if "p5" in claim_lower and "no_p5" not in claim_lower and "not_p5" not in claim_lower:
            errors.append(EC.QA1_P5_CLAIM_IN_BARE_REPORT)
            details.append(f"claim contains P5 claim: {claim!r}")

    # report_hash
    if report.get("report_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"unexpected report_hash_algorithm: {report.get('report_hash_algorithm')}"
        )
    computed = _compute_report_hash(report)
    if report.get("report_hash") != computed:
        errors.append(EC.QA1_BARE_CAPABILITY_HASH_MISMATCH)
        details.append(
            f"report_hash mismatch: expected {computed}, "
            f"got {report.get('report_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
