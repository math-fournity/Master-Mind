"""QuestionRelease — 不可变的发布题目。

来自 docs/implementation/04-object-and-schema-catalog.md：

QuestionRelease 是 immutable question statement signed by G-Q-RELEASE。
引用通过了 AdversarialReview 和 VerificationDossier 的 QuestionDraftVersion。
发布后不可修改。

硬约束：
- 必须引用同时通过两种审查的 draft
- 必须有 G-Q-RELEASE gate 签名
- 发布后不可修改（immutable）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    QA_GATE_TYPE_Q_RELEASE,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/question-release"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "QuestionRelease"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class QuestionRelease:
    """QuestionRelease — 不可变的发布题目。不可变。

    引用 QuestionDraftVersion 的 content_hash。
    引用 AdversarialReview 和 VerificationDossier 的 content_hash。
    包含 G-Q-RELEASE gate decision 引用。
    发布后不可修改。
    """

    release_id: str
    draft_ref_and_hash: dict[str, str]
    adversarial_review_ref_and_hash: dict[str, str]
    verification_dossier_ref_and_hash: dict[str, str]
    gate_decision_ref_and_hash: dict[str, str]
    gate_type: str
    public_statement: str
    immutable: bool
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
            "release_id": self.release_id,
            "draft_ref_and_hash": dict(self.draft_ref_and_hash),
            "adversarial_review_ref_and_hash": dict(self.adversarial_review_ref_and_hash),
            "verification_dossier_ref_and_hash": dict(self.verification_dossier_ref_and_hash),
            "gate_decision_ref_and_hash": dict(self.gate_decision_ref_and_hash),
            "gate_type": self.gate_type,
            "public_statement": self.public_statement,
            "immutable": self.immutable,
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
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name}.ref_id is empty"))
    sha = obj.get("sha256", "")
    if not isinstance(sha, str) or not _HASH_RE.match(sha):
        errors.append((EC.OBJECT_HASH_MISMATCH, f"{field_name}.sha256 is not valid sha256"))
    return errors


def build_question_release(
    *,
    release_id: str,
    draft_ref_and_hash: dict[str, str],
    adversarial_review_ref_and_hash: dict[str, str],
    verification_dossier_ref_and_hash: dict[str, str],
    gate_decision_ref_and_hash: dict[str, str],
    public_statement: str,
) -> QuestionRelease:
    """构建 QuestionRelease，自动计算 content_hash。

    gate_type 固定为 G-Q-RELEASE。immutable 固定为 True。
    """
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "release_id": release_id,
        "draft_ref_and_hash": dict(draft_ref_and_hash),
        "adversarial_review_ref_and_hash": dict(adversarial_review_ref_and_hash),
        "verification_dossier_ref_and_hash": dict(verification_dossier_ref_and_hash),
        "gate_decision_ref_and_hash": dict(gate_decision_ref_and_hash),
        "gate_type": QA_GATE_TYPE_Q_RELEASE,
        "public_statement": public_statement,
        "immutable": True,
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return QuestionRelease(
        release_id=release_id,
        draft_ref_and_hash=dict(draft_ref_and_hash),
        adversarial_review_ref_and_hash=dict(adversarial_review_ref_and_hash),
        verification_dossier_ref_and_hash=dict(verification_dossier_ref_and_hash),
        gate_decision_ref_and_hash=dict(gate_decision_ref_and_hash),
        gate_type=QA_GATE_TYPE_Q_RELEASE,
        public_statement=public_statement,
        immutable=True,
        content_hash=content_hash,
    )


def verify_question_release(
    release: dict[str, Any] | QuestionRelease,
) -> VerificationResult:
    """验证 QuestionRelease 的结构合法性。

    检查：
    1. schema 常量
    2. release_id 非空
    3. draft / adversarial_review / verification_dossier / gate_decision ref 结构合法
    4. gate_type == G-Q-RELEASE
    5. immutable == True（发布后不可修改）
    6. public_statement 非空
    7. content_hash 正确
    """
    if isinstance(release, QuestionRelease):
        release = release.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if release.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if release.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if release.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not release.get("release_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("release_id must not be empty")

    for fname in (
        "draft_ref_and_hash",
        "adversarial_review_ref_and_hash",
        "verification_dossier_ref_and_hash",
        "gate_decision_ref_and_hash",
    ):
        for code, detail in _check_ref_hash(release.get(fname, {}), fname):
            errors.append(code)
            details.append(detail)

    if release.get("gate_type") != QA_GATE_TYPE_Q_RELEASE:
        errors.append(EC.QA_GATE_NOT_SIGNED)
        details.append(f"gate_type must be {QA_GATE_TYPE_Q_RELEASE}, got {release.get('gate_type')!r}")

    if release.get("immutable") is not True:
        errors.append(EC.QA_RELEASE_NOT_IMMUTABLE)
        details.append("immutable must be True for released questions")

    if not release.get("public_statement"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("public_statement must not be empty")

    if release.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {release.get('content_hash_algorithm')}")

    computed = _compute_content_hash(release)
    if release.get("content_hash") != computed:
        errors.append(EC.QA_RELEASE_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {release.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
