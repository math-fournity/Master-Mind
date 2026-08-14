"""QuestionDraftVersion — append-only 出题草案版本。

来自 docs/implementation/04-object-and-schema-catalog.md：

QuestionDraftVersion 定义：
- parent_version_ref：父版本引用（首版本为 None）
- public_statement：公开题面
- sealed_solution_refs：密封解答引用

append-only：题面变化 = 新版本（新 hash），旧版本不可修改。
题面变化失效所有下游审查/验证/发布。

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


_SCHEMA_ID = "seven/question-draft-version"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "QuestionDraftVersion"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class QuestionDraftVersion:
    """QuestionDraftVersion — append-only 出题草案版本。不可变。

    version_number 从 0 开始。parent_version_ref 为 None 表示首版本。
    public_statement 变化 = 新版本。
    """

    draft_id: str
    version_number: int
    parent_version_ref: str | None
    brief_ref_and_hash: dict[str, str]
    public_statement: str
    sealed_solution_refs: list[str]
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
            "draft_id": self.draft_id,
            "version_number": self.version_number,
            "parent_version_ref": self.parent_version_ref,
            "brief_ref_and_hash": dict(self.brief_ref_and_hash),
            "public_statement": self.public_statement,
            "sealed_solution_refs": list(self.sealed_solution_refs),
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }

    @property
    def ref_and_hash(self) -> dict[str, str]:
        return {
            "ref_id": f"{self.draft_id}@v{self.version_number}",
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


def build_question_draft_version(
    *,
    draft_id: str,
    version_number: int,
    parent_version_ref: str | None,
    brief_ref_and_hash: dict[str, str],
    public_statement: str,
    sealed_solution_refs: list[str],
) -> QuestionDraftVersion:
    """构建 QuestionDraftVersion，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "draft_id": draft_id,
        "version_number": version_number,
        "parent_version_ref": parent_version_ref,
        "brief_ref_and_hash": dict(brief_ref_and_hash),
        "public_statement": public_statement,
        "sealed_solution_refs": list(sealed_solution_refs),
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return QuestionDraftVersion(
        draft_id=draft_id,
        version_number=version_number,
        parent_version_ref=parent_version_ref,
        brief_ref_and_hash=dict(brief_ref_and_hash),
        public_statement=public_statement,
        sealed_solution_refs=list(sealed_solution_refs),
        content_hash=content_hash,
    )


def verify_question_draft_version(
    draft: dict[str, Any] | QuestionDraftVersion,
) -> VerificationResult:
    """验证 QuestionDraftVersion 的结构合法性。

    检查：
    1. schema 常量
    2. draft_id 非空
    3. version_number >= 0
    4. parent_version_ref：首版本为 None，后续版本必须引用父版本
    5. brief_ref_and_hash 结构合法
    6. public_statement 非空
    7. sealed_solution_refs 是 list
    8. content_hash 正确
    """
    if isinstance(draft, QuestionDraftVersion):
        draft = draft.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if draft.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if draft.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if draft.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not draft.get("draft_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("draft_id must not be empty")

    version_number = draft.get("version_number", -1)
    if not isinstance(version_number, int) or version_number < 0:
        errors.append(EC.QA_DRAFT_NOT_APPEND_ONLY)
        details.append(f"version_number must be >= 0, got {version_number}")

    parent_ref = draft.get("parent_version_ref")
    if version_number == 0 and parent_ref is not None:
        errors.append(EC.QA_DRAFT_NOT_APPEND_ONLY)
        details.append("first version (v0) must have parent_version_ref=None")
    if version_number and version_number > 0 and not parent_ref:
        errors.append(EC.QA_DRAFT_NOT_APPEND_ONLY)
        details.append(f"version {version_number} must have parent_version_ref")

    for code, detail in _check_ref_hash(
        draft.get("brief_ref_and_hash", {}), "brief_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)

    if not draft.get("public_statement"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("public_statement must not be empty")

    if not isinstance(draft.get("sealed_solution_refs"), list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("sealed_solution_refs must be a list")

    if draft.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {draft.get('content_hash_algorithm')}")

    computed = _compute_content_hash(draft)
    if draft.get("content_hash") != computed:
        errors.append(EC.QA_DRAFT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {draft.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
