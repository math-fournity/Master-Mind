"""CaseRole — P3C 冻结的角色分配（WP-CS1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 78-82：

HumanGate signs AdmissionDecision and CasePackVersion, freezing
positive/false-friend/boundary/unrelated 角色。

CaseRole 是单个角色的冻结分配：
- positive: target mechanism present
- false_friend: looks like target but isn't
- boundary: edge case
- unrelated: no target mechanism

每个角色有 hash-bound evidence refs——角色分配必须有证据引用，
无证据的角色分配 → BLOCK (CS_ROLE_WITHOUT_EVIDENCE)。

硬约束（blocker）：
- role 必须在 CS_CASE_ROLES 中
- evidence_refs 非空（role without evidence → BLOCK）
- 每个 evidence_ref 是 {ref_id, sha256} 结构
- signed_by_human 必须为 True（model 不能签 G-CASE-ROLE）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    CS_CASE_ROLES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/case-role"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "CaseRole"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class CaseRole:
    """CaseRole — P3C 冻结的角色分配。不可变。

    字段：
    - role_id：角色分配唯一标识
    - case_pack_ref_id：关联的 CasePack ID
    - role：角色种类（CS_CASE_ROLES）
    - evidence_refs：证据引用列表，每个为 {ref_id, sha256}
    - signed_by_human：是否由人类签名（model 不能签 G-CASE-ROLE）
    - description：角色描述
    """

    role_id: str
    case_pack_ref_id: str
    role: str
    evidence_refs: list[dict[str, str]]
    signed_by_human: bool
    description: str
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
            "role_id": self.role_id,
            "case_pack_ref_id": self.case_pack_ref_id,
            "role": self.role,
            "evidence_refs": [dict(r) for r in self.evidence_refs],
            "signed_by_human": self.signed_by_human,
            "description": self.description,
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


def build_case_role(
    *,
    role_id: str,
    case_pack_ref_id: str,
    role: str,
    evidence_refs: list[dict[str, str]],
    signed_by_human: bool,
    description: str = "",
) -> CaseRole:
    """构建 CaseRole，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "role_id": role_id,
        "case_pack_ref_id": case_pack_ref_id,
        "role": role,
        "evidence_refs": [dict(r) for r in evidence_refs],
        "signed_by_human": signed_by_human,
        "description": description,
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return CaseRole(
        role_id=role_id,
        case_pack_ref_id=case_pack_ref_id,
        role=role,
        evidence_refs=[dict(r) for r in evidence_refs],
        signed_by_human=signed_by_human,
        description=description,
        content_hash=content_hash,
    )


def verify_case_role(
    role_obj: dict[str, Any] | CaseRole,
) -> VerificationResult:
    """验证 CaseRole 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. role_id 非空
    3. case_pack_ref_id 非空
    4. role 在 CS_CASE_ROLES 中
    5. evidence_refs 非空（role without evidence → BLOCK）
    6. 每个 evidence_ref 结构合法（ref_id + sha256）
    7. signed_by_human == True（model 不能签 G-CASE-ROLE）
    8. content_hash 正确
    """
    if isinstance(role_obj, CaseRole):
        role_obj = role_obj.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if role_obj.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if role_obj.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if role_obj.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not role_obj.get("role_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("role_id must not be empty")

    if not role_obj.get("case_pack_ref_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("case_pack_ref_id must not be empty")

    role_value = role_obj.get("role", "")
    if role_value not in CS_CASE_ROLES:
        errors.append(EC.CS_CASE_ROLE_INVALID)
        details.append(f"role {role_value!r} not in CS_CASE_ROLES {sorted(CS_CASE_ROLES)}")

    # evidence_refs (blocker: role without evidence)
    evidence_refs = role_obj.get("evidence_refs", [])
    if not isinstance(evidence_refs, list) or len(evidence_refs) == 0:
        errors.append(EC.CS_ROLE_WITHOUT_EVIDENCE)
        details.append("evidence_refs must be non-empty (role without evidence → BLOCK)")
    else:
        for i, ref in enumerate(evidence_refs):
            for code, detail in _check_ref_hash(ref, f"evidence_refs[{i}]"):
                errors.append(code)
                details.append(detail)

    # signed_by_human (blocker: model self-signing role)
    if role_obj.get("signed_by_human") is not True:
        errors.append(EC.CS_MODEL_SELF_SIGNED_ROLE)
        details.append("signed_by_human must be True (model cannot sign G-CASE-ROLE)")

    # content_hash
    if role_obj.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {role_obj.get('content_hash_algorithm')}")

    computed = _compute_content_hash(role_obj)
    if role_obj.get("content_hash") != computed:
        errors.append(EC.CS_CASE_PACK_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {role_obj.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
