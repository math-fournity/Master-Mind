"""VerificationDossier — 数学正确性验证档案。

来自 docs/implementation/04-object-and-schema-catalog.md：

VerificationDossier 是 math correctness verification。
引用 QuestionDraftVersion 的 hash。与 AdversarialReview 独立。

审查种类 = MATH_VERIFICATION。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    QA_REVIEW_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/verification-dossier"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "VerificationDossier"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"
_REVIEW_KIND = "MATH_VERIFICATION"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class VerificationDossier:
    """VerificationDossier — 数学正确性验证档案。不可变。

    验证数学正确性，独立于 AdversarialReview。
    引用 QuestionDraftVersion 的 content_hash。
    """

    dossier_id: str
    draft_ref_and_hash: dict[str, str]
    review_kind: str
    verdict: str  # PASS / FAIL / REQUEST_CHANGES
    math_correct: bool
    verification_steps: list[str]
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
            "dossier_id": self.dossier_id,
            "draft_ref_and_hash": dict(self.draft_ref_and_hash),
            "review_kind": self.review_kind,
            "verdict": self.verdict,
            "math_correct": self.math_correct,
            "verification_steps": list(self.verification_steps),
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


def build_verification_dossier(
    *,
    dossier_id: str,
    draft_ref_and_hash: dict[str, str],
    verdict: str,
    math_correct: bool,
    verification_steps: list[str],
) -> VerificationDossier:
    """构建 VerificationDossier，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "dossier_id": dossier_id,
        "draft_ref_and_hash": dict(draft_ref_and_hash),
        "review_kind": _REVIEW_KIND,
        "verdict": verdict,
        "math_correct": math_correct,
        "verification_steps": list(verification_steps),
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return VerificationDossier(
        dossier_id=dossier_id,
        draft_ref_and_hash=dict(draft_ref_and_hash),
        review_kind=_REVIEW_KIND,
        verdict=verdict,
        math_correct=math_correct,
        verification_steps=list(verification_steps),
        content_hash=content_hash,
    )


def verify_verification_dossier(
    dossier: dict[str, Any] | VerificationDossier,
) -> VerificationResult:
    """验证 VerificationDossier 的结构合法性。"""
    if isinstance(dossier, VerificationDossier):
        dossier = dossier.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if dossier.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if dossier.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if dossier.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not dossier.get("dossier_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("dossier_id must not be empty")

    review_kind = dossier.get("review_kind", "")
    if review_kind not in QA_REVIEW_KINDS:
        errors.append(EC.QA_REVIEW_KIND_UNKNOWN)
        details.append(f"review_kind must be in {QA_REVIEW_KINDS}, got {review_kind!r}")
    if review_kind != _REVIEW_KIND:
        errors.append(EC.QA_REVIEW_KIND_UNKNOWN)
        details.append(f"review_kind must be {_REVIEW_KIND}, got {review_kind!r}")

    for code, detail in _check_ref_hash(
        dossier.get("draft_ref_and_hash", {}), "draft_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)

    verdict_val = dossier.get("verdict", "")
    if verdict_val not in ("PASS", "FAIL", "REQUEST_CHANGES"):
        errors.append(EC.STATE_COMMAND_REJECTED)
        details.append(f"invalid verdict: {verdict_val!r}")

    if not isinstance(dossier.get("math_correct"), bool):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("math_correct must be a bool")

    if not isinstance(dossier.get("verification_steps"), list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("verification_steps must be a list")

    if dossier.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {dossier.get('content_hash_algorithm')}")

    computed = _compute_content_hash(dossier)
    if dossier.get("content_hash") != computed:
        errors.append(EC.QA_VERIFICATION_DOSSIER_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {dossier.get('content_hash')}"
        )

    verdict_result = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict_result, error_codes=errors, details=details)
