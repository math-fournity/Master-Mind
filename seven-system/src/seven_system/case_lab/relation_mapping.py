"""RelationMapping — case 与 taxonomy 的关系映射（WP-CS1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 78-82 和
docs/implementation/15-work-package-implementation-contracts.md line 90：

RelationMapping 映射 case 与 taxonomy 的关系：
- 哪些 Tell cores 相关
- 哪些 boundaries 相关
- 哪些 hints 相关

硬约束（blocker）：
- taxonomy_snapshot_ref 必须存在且结构合法
- tell_core_refs / boundary_refs / hint_refs 各为 list of {ref_id, sha256}
- 至少有一个关系引用（空映射 → BLOCK）
- content_hash 正确

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/relation-mapping"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "RelationMapping"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class RelationMapping:
    """RelationMapping — case 与 taxonomy 的关系映射。不可变。

    字段：
    - mapping_id：映射唯一标识
    - case_pack_ref_id：关联的 CasePack ID
    - taxonomy_snapshot_ref_and_hash：分类学快照引用 {ref_id, sha256}
    - tell_core_refs：相关 TellCore 引用列表
    - boundary_refs：相关 ApplicabilityBoundary 引用列表
    - hint_refs：相关 Hint 引用列表
    """

    mapping_id: str
    case_pack_ref_id: str
    taxonomy_snapshot_ref_and_hash: dict[str, str]
    tell_core_refs: list[dict[str, str]]
    boundary_refs: list[dict[str, str]]
    hint_refs: list[dict[str, str]]
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
            "mapping_id": self.mapping_id,
            "case_pack_ref_id": self.case_pack_ref_id,
            "taxonomy_snapshot_ref_and_hash": dict(self.taxonomy_snapshot_ref_and_hash),
            "tell_core_refs": [dict(r) for r in self.tell_core_refs],
            "boundary_refs": [dict(r) for r in self.boundary_refs],
            "hint_refs": [dict(r) for r in self.hint_refs],
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


def _check_ref_list(
    refs: Any, field_name: str
) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(refs, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must be a list"))
        return errors
    for i, ref in enumerate(refs):
        errors.extend(_check_ref_hash(ref, f"{field_name}[{i}]"))
    return errors


def build_relation_mapping(
    *,
    mapping_id: str,
    case_pack_ref_id: str,
    taxonomy_snapshot_ref_and_hash: dict[str, str],
    tell_core_refs: list[dict[str, str]],
    boundary_refs: list[dict[str, str]],
    hint_refs: list[dict[str, str]],
) -> RelationMapping:
    """构建 RelationMapping，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "mapping_id": mapping_id,
        "case_pack_ref_id": case_pack_ref_id,
        "taxonomy_snapshot_ref_and_hash": dict(taxonomy_snapshot_ref_and_hash),
        "tell_core_refs": [dict(r) for r in tell_core_refs],
        "boundary_refs": [dict(r) for r in boundary_refs],
        "hint_refs": [dict(r) for r in hint_refs],
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return RelationMapping(
        mapping_id=mapping_id,
        case_pack_ref_id=case_pack_ref_id,
        taxonomy_snapshot_ref_and_hash=dict(taxonomy_snapshot_ref_and_hash),
        tell_core_refs=[dict(r) for r in tell_core_refs],
        boundary_refs=[dict(r) for r in boundary_refs],
        hint_refs=[dict(r) for r in hint_refs],
        content_hash=content_hash,
    )


def verify_relation_mapping(
    mapping_obj: dict[str, Any] | RelationMapping,
) -> VerificationResult:
    """验证 RelationMapping 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. mapping_id 非空
    3. case_pack_ref_id 非空
    4. taxonomy_snapshot_ref_and_hash 结构合法
    5. tell_core_refs / boundary_refs / hint_refs 各为 list of {ref_id, sha256}
    6. 至少有一个关系引用（空映射 → BLOCK）
    7. content_hash 正确
    """
    if isinstance(mapping_obj, RelationMapping):
        mapping_obj = mapping_obj.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if mapping_obj.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if mapping_obj.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if mapping_obj.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not mapping_obj.get("mapping_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("mapping_id must not be empty")

    if not mapping_obj.get("case_pack_ref_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("case_pack_ref_id must not be empty")

    for code, detail in _check_ref_hash(
        mapping_obj.get("taxonomy_snapshot_ref_and_hash", {}),
        "taxonomy_snapshot_ref_and_hash",
    ):
        errors.append(code)
        details.append(detail)

    for code, detail in _check_ref_list(
        mapping_obj.get("tell_core_refs", []), "tell_core_refs"
    ):
        errors.append(code)
        details.append(detail)

    for code, detail in _check_ref_list(
        mapping_obj.get("boundary_refs", []), "boundary_refs"
    ):
        errors.append(code)
        details.append(detail)

    for code, detail in _check_ref_list(
        mapping_obj.get("hint_refs", []), "hint_refs"
    ):
        errors.append(code)
        details.append(detail)

    # At least one relation ref required
    tell_refs = mapping_obj.get("tell_core_refs", [])
    boundary_refs = mapping_obj.get("boundary_refs", [])
    hint_refs = mapping_obj.get("hint_refs", [])
    total_refs = 0
    if isinstance(tell_refs, list):
        total_refs += len(tell_refs)
    if isinstance(boundary_refs, list):
        total_refs += len(boundary_refs)
    if isinstance(hint_refs, list):
        total_refs += len(hint_refs)
    if total_refs == 0:
        errors.append(EC.CS_RELATION_MAPPING_INVALID)
        details.append("at least one relation ref required (empty mapping → BLOCK)")

    if mapping_obj.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {mapping_obj.get('content_hash_algorithm')}")

    computed = _compute_content_hash(mapping_obj)
    if mapping_obj.get("content_hash") != computed:
        errors.append(EC.CS_CASE_PACK_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {mapping_obj.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
