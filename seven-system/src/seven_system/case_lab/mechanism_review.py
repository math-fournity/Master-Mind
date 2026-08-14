"""MechanismReview — 机制合同审查（WP-CS1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 78-82 和
docs/implementation/15-work-package-implementation-contracts.md line 90：

MechanismReview 审查 case 的机制合同。验证机制被正确识别和界定。

审查种类（CS_MECHANISM_REVIEW_KINDS）：
- IDENTIFICATION: 机制识别审查
- BOUNDARY_CHECK: 机制边界审查
- COMPLETENESS: 机制完备性审查

硬约束（blocker）：
- mechanism_contract_ref 必须存在且结构合法
- review_kind 在 CS_MECHANISM_REVIEW_KINDS 中
- verdict 为 PASS/FAIL/INCONCLUSIVE
- 审查必须引用 mechanism contract by hash

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    CS_MECHANISM_REVIEW_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/mechanism-review"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "MechanismReview"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")

_REVIEW_VERDICTS: frozenset[str] = frozenset({"PASS", "FAIL", "INCONCLUSIVE"})


@dataclass(frozen=True)
class MechanismReview:
    """MechanismReview — 机制合同审查。不可变。

    字段：
    - review_id：审查唯一标识
    - case_pack_ref_id：关联的 CasePack ID
    - mechanism_contract_ref_and_hash：机制合同引用 {ref_id, sha256}
    - review_kind：审查种类（CS_MECHANISM_REVIEW_KINDS）
    - verdict：审查结论（PASS/FAIL/INCONCLUSIVE）
    - findings：审查发现列表
    - reviewer_role：审查者角色
    """

    review_id: str
    case_pack_ref_id: str
    mechanism_contract_ref_and_hash: dict[str, str]
    review_kind: str
    verdict: str
    findings: list[str]
    reviewer_role: str
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    content_hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "review_id": self.review_id,
            "case_pack_ref_id": self.case_pack_ref_id,
            "mechanism_contract_ref_and_hash": dict(self.mechanism_contract_ref_and_hash),
            "review_kind": self.review_kind,
            "verdict": self.verdict,
            "findings": list(self.findings),
            "reviewer_role": self.reviewer_role,
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }


def _compute_content_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["content_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def _check_ref_hash(obj: Any, field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"ref_id", "sha256"}:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly ref_id and sha256"))
        return errors
    if not obj.get("ref_id"):
        errors.append((EC.CS_EVIDENCE_REF_MISSING, f"{field_name}.ref_id is empty"))
    sha = obj.get("sha256", "")
    if not isinstance(sha, str) or not _HASH_RE.match(sha):
        errors.append((EC.OBJECT_HASH_MISMATCH, f"{field_name}.sha256 is not valid sha256"))
    return errors


def build_mechanism_review(
    *,
    review_id: str,
    case_pack_ref_id: str,
    mechanism_contract_ref_and_hash: dict[str, str],
    review_kind: str,
    verdict: str,
    findings: list[str],
    reviewer_role: str,
) -> MechanismReview:
    """构建 MechanismReview，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "review_id": review_id,
        "case_pack_ref_id": case_pack_ref_id,
        "mechanism_contract_ref_and_hash": dict(mechanism_contract_ref_and_hash),
        "review_kind": review_kind,
        "verdict": verdict,
        "findings": list(findings),
        "reviewer_role": reviewer_role,
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return MechanismReview(
        review_id=review_id,
        case_pack_ref_id=case_pack_ref_id,
        mechanism_contract_ref_and_hash=dict(mechanism_contract_ref_and_hash),
        review_kind=review_kind,
        verdict=verdict,
        findings=list(findings),
        reviewer_role=reviewer_role,
        content_hash=content_hash,
    )


def verify_mechanism_review(
    review_obj: dict[str, Any] | MechanismReview,
) -> VerificationResult:
    """验证 MechanismReview 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. review_id 非空
    3. case_pack_ref_id 非空
    4. mechanism_contract_ref_and_hash 结构合法
    5. review_kind 在 CS_MECHANISM_REVIEW_KINDS 中
    6. verdict 在 {PASS, FAIL, INCONCLUSIVE} 中
    7. findings 是 list
    8. reviewer_role 非空
    9. content_hash 正确
    """
    if isinstance(review_obj, MechanismReview):
        review_obj = review_obj.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if review_obj.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if review_obj.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if review_obj.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not review_obj.get("review_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("review_id must not be empty")

    if not review_obj.get("case_pack_ref_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("case_pack_ref_id must not be empty")

    for code, detail in _check_ref_hash(
        review_obj.get("mechanism_contract_ref_and_hash", {}),
        "mechanism_contract_ref_and_hash",
    ):
        errors.append(code)
        details.append(detail)

    review_kind = review_obj.get("review_kind", "")
    if review_kind not in CS_MECHANISM_REVIEW_KINDS:
        errors.append(EC.CS_MECHANISM_REVIEW_FAILED)
        details.append(
            f"review_kind {review_kind!r} not in CS_MECHANISM_REVIEW_KINDS "
            f"{sorted(CS_MECHANISM_REVIEW_KINDS)}"
        )

    verdict_value = review_obj.get("verdict", "")
    if verdict_value not in _REVIEW_VERDICTS:
        errors.append(EC.CS_MECHANISM_REVIEW_FAILED)
        details.append(f"verdict {verdict_value!r} not in {sorted(_REVIEW_VERDICTS)}")

    if not isinstance(review_obj.get("findings"), list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("findings must be a list")

    if not review_obj.get("reviewer_role"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("reviewer_role must not be empty")

    if review_obj.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {review_obj.get('content_hash_algorithm')}")

    computed = _compute_content_hash(review_obj)
    if review_obj.get("content_hash") != computed:
        errors.append(EC.CS_CASE_PACK_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {review_obj.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
