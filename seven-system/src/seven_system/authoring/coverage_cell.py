"""CoverageCell — 覆盖单元。

来自 docs/implementation/04-object-and-schema-catalog.md：

CoverageCell 定义：
- math_branch：数学分支
- transfer_distance：迁移距离
- case_relationship：案例关系
- evidence_use_location：证据使用位置

冻结对象，content_hash 覆盖全部字段。变化即新对象，失效下游。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/coverage-cell"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "CoverageCell"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"


@dataclass(frozen=True)
class CoverageCell:
    """CoverageCell — 覆盖单元。不可变。"""

    cell_id: str
    math_branch: str
    transfer_distance: str
    case_relationship: str
    evidence_use_location: str
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
            "cell_id": self.cell_id,
            "math_branch": self.math_branch,
            "transfer_distance": self.transfer_distance,
            "case_relationship": self.case_relationship,
            "evidence_use_location": self.evidence_use_location,
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }

    @property
    def ref_and_hash(self) -> dict[str, str]:
        return {
            "ref_id": self.cell_id,
            "sha256": self.content_hash,
        }


def _compute_content_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["content_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def build_coverage_cell(
    *,
    cell_id: str,
    math_branch: str,
    transfer_distance: str,
    case_relationship: str,
    evidence_use_location: str,
) -> CoverageCell:
    """构建 CoverageCell，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "cell_id": cell_id,
        "math_branch": math_branch,
        "transfer_distance": transfer_distance,
        "case_relationship": case_relationship,
        "evidence_use_location": evidence_use_location,
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return CoverageCell(
        cell_id=cell_id,
        math_branch=math_branch,
        transfer_distance=transfer_distance,
        case_relationship=case_relationship,
        evidence_use_location=evidence_use_location,
        content_hash=content_hash,
    )


def verify_coverage_cell(
    cell: dict[str, Any] | CoverageCell,
) -> VerificationResult:
    """验证 CoverageCell 的结构合法性。"""
    if isinstance(cell, CoverageCell):
        cell = cell.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if cell.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if cell.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if cell.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    for fname in ("cell_id", "math_branch", "transfer_distance",
                  "case_relationship", "evidence_use_location"):
        if not cell.get(fname):
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"{fname} must not be empty")

    if cell.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {cell.get('content_hash_algorithm')}")

    computed = _compute_content_hash(cell)
    if cell.get("content_hash") != computed:
        errors.append(EC.QA_COVERAGE_CELL_CHANGED)
        details.append(
            f"content_hash mismatch: expected {computed}, got {cell.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
