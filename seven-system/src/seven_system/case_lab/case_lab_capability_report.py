"""CaseLabCapabilityReport — CS1 CaseLab 能力报告（WP-CS1）。

来自 WP-CS1 work package contract：

READY_FOR_AUDIT 最低产物：
- 双入口fixture、P3C验签、角色冻结

边界：
- no P5 claim
- no confirmatory Evidence
- no live model calls
- no solver launches

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    CS_ALLOWED_OUTPUT_KINDS,
    CS_FORBIDDEN_OUTPUT_KINDS,
    CS_SIDE_EFFECT_KEYS,
    CS_CHECK_IDS,
    CS_CLAIMS,
    CS_NONCLAIMS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/case-lab-capability-report"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "CaseLabCapabilityReport"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"


@dataclass(frozen=True)
class CaseLabCapabilityReport:
    """CaseLabCapabilityReport — CS1 CaseLab 能力报告。不可变。

    报告 CS1 的能力边界：
    - side_effect_counters：所有副作用键必须为 0
    - allowed_output_kinds：CS1 允许输出的对象种类
    - forbidden_output_kinds：CS1 明确禁止输出的对象种类
    - dual_entry_fixture_support：双入口 fixture 支持
    - p3c_verification：P3C 验签能力
    - role_freezing：角色冻结能力
    - no_p5_claim：无 P5 claim
    - no_confirmatory_evidence：无 confirmatory Evidence
    """

    report_id: str
    side_effect_counters: dict[str, int]
    allowed_output_kinds: list[str]
    forbidden_output_kinds: list[str]
    dual_entry_fixture_support: bool
    p3c_verification: bool
    role_freezing: bool
    no_p5_claim: bool
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
            "dual_entry_fixture_support": self.dual_entry_fixture_support,
            "p3c_verification": self.p3c_verification,
            "role_freezing": self.role_freezing,
            "no_p5_claim": self.no_p5_claim,
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


def build_case_lab_capability_report(
    *,
    report_id: str,
) -> CaseLabCapabilityReport:
    """构建 CaseLabCapabilityReport。

    所有 side_effect_counters 初始化为 0。
    allowed/forbidden output kinds 从常量填充。
    dual_entry_fixture_support / p3c_verification / role_freezing 固定为 True。
    no_p5_claim / no_confirmatory_evidence 固定为 True。
    """
    side_effect_counters = {key: 0 for key in CS_SIDE_EFFECT_KEYS}
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "report_id": report_id,
        "side_effect_counters": side_effect_counters,
        "allowed_output_kinds": sorted(CS_ALLOWED_OUTPUT_KINDS),
        "forbidden_output_kinds": sorted(CS_FORBIDDEN_OUTPUT_KINDS),
        "dual_entry_fixture_support": True,
        "p3c_verification": True,
        "role_freezing": True,
        "no_p5_claim": True,
        "no_confirmatory_evidence": True,
        "check_ids": list(CS_CHECK_IDS),
        "claims": list(CS_CLAIMS),
        "nonclaims": list(CS_NONCLAIMS),
        "report_hash_algorithm": _HASH_ALGORITHM,
        "report_hash": None,
    }
    report_hash = _compute_report_hash(obj)
    return CaseLabCapabilityReport(
        report_id=report_id,
        side_effect_counters=side_effect_counters,
        allowed_output_kinds=sorted(CS_ALLOWED_OUTPUT_KINDS),
        forbidden_output_kinds=sorted(CS_FORBIDDEN_OUTPUT_KINDS),
        dual_entry_fixture_support=True,
        p3c_verification=True,
        role_freezing=True,
        no_p5_claim=True,
        no_confirmatory_evidence=True,
        check_ids=list(CS_CHECK_IDS),
        claims=list(CS_CLAIMS),
        nonclaims=list(CS_NONCLAIMS),
        report_hash=report_hash,
    )


def verify_case_lab_capability_report(
    report: dict[str, Any] | CaseLabCapabilityReport,
) -> VerificationResult:
    """验证 CaseLabCapabilityReport 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. report_id 非空
    3. side_effect_counters 所有键在 CS_SIDE_EFFECT_KEYS 中且值为 0
    4. dual_entry_fixture_support == True
    5. p3c_verification == True
    6. role_freezing == True
    7. no_p5_claim == True
    8. no_confirmatory_evidence == True
    9. allowed_output_kinds == CS_ALLOWED_OUTPUT_KINDS
    10. forbidden_output_kinds == CS_FORBIDDEN_OUTPUT_KINDS
    11. forbidden_output_kinds 不在 allowed_output_kinds 中
    12. claims 不含 P5 claim
    13. report_hash 正确
    """
    if isinstance(report, CaseLabCapabilityReport):
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
        for key in CS_SIDE_EFFECT_KEYS:
            val = counters.get(key)
            if val is None:
                errors.append(EC.REQUIRED_FIELD_MISSING)
                details.append(f"side_effect_counters missing key: {key}")
            elif val != 0:
                errors.append(EC.OBJECT_HASH_MISMATCH)
                details.append(f"side_effect_counters[{key}] must be 0, got {val}")
        extra = set(counters.keys()) - set(CS_SIDE_EFFECT_KEYS)
        if extra:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"side_effect_counters has extra keys: {extra}")

    # capability flags
    if report.get("dual_entry_fixture_support") is not True:
        errors.append(EC.CS_P3C_VERIFICATION_FAILED)
        details.append("dual_entry_fixture_support must be True")

    if report.get("p3c_verification") is not True:
        errors.append(EC.CS_P3C_VERIFICATION_FAILED)
        details.append("p3c_verification must be True")

    if report.get("role_freezing") is not True:
        errors.append(EC.CS_ROLE_NOT_FROZEN)
        details.append("role_freezing must be True")

    if report.get("no_p5_claim") is not True:
        errors.append(EC.CS_OUTPUT_KIND_FORBIDDEN)
        details.append("no_p5_claim must be True")

    if report.get("no_confirmatory_evidence") is not True:
        errors.append(EC.CS_OUTPUT_KIND_FORBIDDEN)
        details.append("no_confirmatory_evidence must be True")

    # allowed_output_kinds
    allowed = set(report.get("allowed_output_kinds", []))
    if allowed != set(CS_ALLOWED_OUTPUT_KINDS):
        errors.append(EC.CS_OUTPUT_KIND_FORBIDDEN)
        details.append(f"allowed_output_kinds mismatch: got {sorted(allowed)}")

    # forbidden_output_kinds
    forbidden = set(report.get("forbidden_output_kinds", []))
    if forbidden != set(CS_FORBIDDEN_OUTPUT_KINDS):
        errors.append(EC.CS_OUTPUT_KIND_FORBIDDEN)
        details.append(f"forbidden_output_kinds mismatch: got {sorted(forbidden)}")

    overlap = allowed & forbidden
    if overlap:
        errors.append(EC.CS_OUTPUT_KIND_FORBIDDEN)
        details.append(f"output kinds in both allowed and forbidden: {overlap}")

    # claims must not contain P5 claim
    claims = report.get("claims", [])
    for claim in claims:
        claim_lower = claim.lower()
        if "p5" in claim_lower and "no_p5" not in claim_lower and "not_p5" not in claim_lower:
            errors.append(EC.CS_OUTPUT_KIND_FORBIDDEN)
            details.append(f"claim contains P5 claim: {claim!r}")

    # report_hash
    if report.get("report_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"unexpected report_hash_algorithm: {report.get('report_hash_algorithm')}"
        )
    computed = _compute_report_hash(report)
    if report.get("report_hash") != computed:
        errors.append(EC.CS_CAPABILITY_HASH_MISMATCH)
        details.append(
            f"report_hash mismatch: expected {computed}, "
            f"got {report.get('report_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
