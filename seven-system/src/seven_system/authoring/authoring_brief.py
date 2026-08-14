"""AuthoringBrief — 出题简报。

来自 docs/implementation/04-object-and-schema-catalog.md：

AuthoringBrief 定义：
- controlled_generation_target：受控生成目标
- forbidden_shortcuts：禁止的捷径
- budget：预算

引用 MechanismContract + CoverageCell 的 hash。
brief hash 不匹配 = QA_BRIEF_HASH_MISMATCH。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/authoring-brief"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "AuthoringBrief"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class AuthoringBrief:
    """AuthoringBrief — 出题简报。不可变。

    引用 MechanismContract 和 CoverageCell 的 content_hash。
    """

    brief_id: str
    mechanism_contract_ref_and_hash: dict[str, str]
    coverage_cell_ref_and_hash: dict[str, str]
    controlled_generation_target: str
    forbidden_shortcuts: list[str]
    budget: dict[str, Any]
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
            "brief_id": self.brief_id,
            "mechanism_contract_ref_and_hash": dict(self.mechanism_contract_ref_and_hash),
            "coverage_cell_ref_and_hash": dict(self.coverage_cell_ref_and_hash),
            "controlled_generation_target": self.controlled_generation_target,
            "forbidden_shortcuts": list(self.forbidden_shortcuts),
            "budget": dict(self.budget),
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }

    @property
    def ref_and_hash(self) -> dict[str, str]:
        return {
            "ref_id": self.brief_id,
            "sha256": self.content_hash,
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
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name}.ref_id is empty"))
    sha = obj.get("sha256", "")
    if not isinstance(sha, str) or not _HASH_RE.match(sha):
        errors.append((EC.OBJECT_HASH_MISMATCH, f"{field_name}.sha256 is not valid sha256"))
    return errors


def build_authoring_brief(
    *,
    brief_id: str,
    mechanism_contract_ref_and_hash: dict[str, str],
    coverage_cell_ref_and_hash: dict[str, str],
    controlled_generation_target: str,
    forbidden_shortcuts: list[str],
    budget: dict[str, Any],
) -> AuthoringBrief:
    """构建 AuthoringBrief，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "brief_id": brief_id,
        "mechanism_contract_ref_and_hash": dict(mechanism_contract_ref_and_hash),
        "coverage_cell_ref_and_hash": dict(coverage_cell_ref_and_hash),
        "controlled_generation_target": controlled_generation_target,
        "forbidden_shortcuts": list(forbidden_shortcuts),
        "budget": dict(budget),
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return AuthoringBrief(
        brief_id=brief_id,
        mechanism_contract_ref_and_hash=dict(mechanism_contract_ref_and_hash),
        coverage_cell_ref_and_hash=dict(coverage_cell_ref_and_hash),
        controlled_generation_target=controlled_generation_target,
        forbidden_shortcuts=list(forbidden_shortcuts),
        budget=dict(budget),
        content_hash=content_hash,
    )


def verify_authoring_brief(
    brief: dict[str, Any] | AuthoringBrief,
) -> VerificationResult:
    """验证 AuthoringBrief 的结构合法性。"""
    if isinstance(brief, AuthoringBrief):
        brief = brief.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if brief.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if brief.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if brief.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not brief.get("brief_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("brief_id must not be empty")
    if not brief.get("controlled_generation_target"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("controlled_generation_target must not be empty")

    for code, detail in _check_ref_hash(
        brief.get("mechanism_contract_ref_and_hash", {}), "mechanism_contract_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)
    for code, detail in _check_ref_hash(
        brief.get("coverage_cell_ref_and_hash", {}), "coverage_cell_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)

    if not isinstance(brief.get("forbidden_shortcuts"), list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("forbidden_shortcuts must be a list")
    if not isinstance(brief.get("budget"), dict):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("budget must be a dict")

    if brief.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {brief.get('content_hash_algorithm')}")

    computed = _compute_content_hash(brief)
    if brief.get("content_hash") != computed:
        errors.append(EC.QA_BRIEF_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {brief.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
