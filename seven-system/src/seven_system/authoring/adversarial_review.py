"""AdversarialReview — 题面对抗性审查。

来自 docs/implementation/04-object-and-schema-catalog.md：

AdversarialReview 是 statement-only attack review。
引用 QuestionDraftVersion 的 hash。与 VerificationDossier 独立。

审查种类 = ADVERSARIAL_REVIEW。

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


_SCHEMA_ID = "seven/adversarial-review"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "AdversarialReview"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"
_REVIEW_KIND = "ADVERSARIAL_REVIEW"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class AdversarialReview:
    """AdversarialReview — 题面对抗性审查。不可变。

    statement-only：只审查公开题面，不审查解答。
    引用 QuestionDraftVersion 的 content_hash。
    """

    review_id: str
    draft_ref_and_hash: dict[str, str]
    review_kind: str
    verdict: str  # PASS / FAIL / REQUEST_CHANGES
    attack_surface: str
    findings: list[str]
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
            "draft_ref_and_hash": dict(self.draft_ref_and_hash),
            "review_kind": self.review_kind,
            "verdict": self.verdict,
            "attack_surface": self.attack_surface,
            "findings": list(self.findings),
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


def build_adversarial_review(
    *,
    review_id: str,
    draft_ref_and_hash: dict[str, str],
    verdict: str,
    attack_surface: str,
    findings: list[str],
) -> AdversarialReview:
    """构建 AdversarialReview，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "review_id": review_id,
        "draft_ref_and_hash": dict(draft_ref_and_hash),
        "review_kind": _REVIEW_KIND,
        "verdict": verdict,
        "attack_surface": attack_surface,
        "findings": list(findings),
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return AdversarialReview(
        review_id=review_id,
        draft_ref_and_hash=dict(draft_ref_and_hash),
        review_kind=_REVIEW_KIND,
        verdict=verdict,
        attack_surface=attack_surface,
        findings=list(findings),
        content_hash=content_hash,
    )


def verify_adversarial_review(
    review: dict[str, Any] | AdversarialReview,
) -> VerificationResult:
    """验证 AdversarialReview 的结构合法性。"""
    if isinstance(review, AdversarialReview):
        review = review.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if review.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if review.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if review.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not review.get("review_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("review_id must not be empty")

    review_kind = review.get("review_kind", "")
    if review_kind not in QA_REVIEW_KINDS:
        errors.append(EC.QA_REVIEW_KIND_UNKNOWN)
        details.append(f"review_kind must be in {QA_REVIEW_KINDS}, got {review_kind!r}")
    if review_kind != _REVIEW_KIND:
        errors.append(EC.QA_REVIEW_KIND_UNKNOWN)
        details.append(f"review_kind must be {_REVIEW_KIND}, got {review_kind!r}")

    for code, detail in _check_ref_hash(
        review.get("draft_ref_and_hash", {}), "draft_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)

    verdict_val = review.get("verdict", "")
    if verdict_val not in ("PASS", "FAIL", "REQUEST_CHANGES"):
        errors.append(EC.STATE_COMMAND_REJECTED)
        details.append(f"invalid verdict: {verdict_val!r}")

    if not review.get("attack_surface"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("attack_surface must not be empty")

    if not isinstance(review.get("findings"), list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("findings must be a list")

    if review.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {review.get('content_hash_algorithm')}")

    computed = _compute_content_hash(review)
    if review.get("content_hash") != computed:
        errors.append(EC.QA_REVIEW_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {review.get('content_hash')}"
        )

    verdict_result = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict_result, error_codes=errors, details=details)
