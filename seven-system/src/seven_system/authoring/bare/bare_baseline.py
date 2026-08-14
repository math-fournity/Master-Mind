"""BareBaseline — 问题级 bare 分布（WP-QA1 P3B）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 72-76：

Only give QuestionRelease public statement to TargetSolverPort for problem-only
bare. No Tell/Hint, not part of P5. Success/failure both retained, forbidden to
modify question or continue generating until failure.

BareBaseline 是问题级 bare 分布——冻结的 per-problem bare 尝试结果。
与 QuestionRelease ref + hash 绑定，发布后不可变。

硬约束：
- 必须引用 QuestionRelease（ref_id + sha256）
- 每个 problem 的 bare attempt 结果状态在 QA1_BARE_STATUSES 中
- 成功和失败都保留
- 不可修改 question
- 不可选择性删除成功题

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    QA1_BARE_STATUSES,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/bare-baseline"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "BareBaseline"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-baseline_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class BareAttemptResult:
    """单个 problem 的 bare 尝试结果。不可变。

    字段：
    - problem_ref_id：题目引用 ID（对应 QuestionRelease.release_id）
    - bare_status：bare 结果状态（PASS/FAIL/TIMEOUT/QUARANTINE）
    - attempt_ref_id：bare attempt 引用 ID
    - terminal_reason：终止原因
    - tell_hint_included：是否包含 Tell/Hint（必须为 False）
    """

    problem_ref_id: str
    bare_status: str
    attempt_ref_id: str
    terminal_reason: str
    tell_hint_included: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "problem_ref_id": self.problem_ref_id,
            "bare_status": self.bare_status,
            "attempt_ref_id": self.attempt_ref_id,
            "terminal_reason": self.terminal_reason,
            "tell_hint_included": self.tell_hint_included,
        }


@dataclass(frozen=True)
class BareBaseline:
    """BareBaseline — 问题级 bare 分布。不可变。

    与 QuestionRelease ref + hash 绑定。
    包含 per-problem bare attempt 结果列表。
    发布后不可变。
    """

    baseline_id: str
    question_release_ref_and_hash: dict[str, str]
    problem_only: bool
    no_tell_hint: bool
    all_results_retained: bool
    bare_attempt_results: list[dict[str, Any]]
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    baseline_hash_algorithm: str = _HASH_ALGORITHM
    baseline_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "baseline_id": self.baseline_id,
            "question_release_ref_and_hash": dict(self.question_release_ref_and_hash),
            "problem_only": self.problem_only,
            "no_tell_hint": self.no_tell_hint,
            "all_results_retained": self.all_results_retained,
            "bare_attempt_results": [dict(r) for r in self.bare_attempt_results],
            "baseline_hash_algorithm": self.baseline_hash_algorithm,
            "baseline_hash": self.baseline_hash,
        }


def _compute_baseline_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["baseline_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def _ref_and_hash_valid(obj: Any) -> bool:
    return (
        isinstance(obj, dict)
        and set(obj.keys()) == {"ref_id", "sha256"}
        and isinstance(obj.get("ref_id"), str)
        and bool(obj.get("ref_id"))
        and isinstance(obj.get("sha256"), str)
        and bool(_HASH_RE.match(obj.get("sha256", "")))
    )


def build_bare_baseline(
    *,
    baseline_id: str,
    question_release_ref_id: str,
    question_release_sha256: str,
    bare_attempt_results: list[BareAttemptResult],
) -> BareBaseline:
    """构建 BareBaseline，自动计算 baseline_hash。

    problem_only 固定为 True（P3B 是 problem-only bare）。
    no_tell_hint 固定为 True（bare 不含 Tell/Hint）。
    all_results_retained 固定为 True（成功和失败都保留）。
    """
    results = [r.to_dict() for r in bare_attempt_results]
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "baseline_id": baseline_id,
        "question_release_ref_and_hash": {
            "ref_id": question_release_ref_id,
            "sha256": question_release_sha256,
        },
        "problem_only": True,
        "no_tell_hint": True,
        "all_results_retained": True,
        "bare_attempt_results": results,
        "baseline_hash_algorithm": _HASH_ALGORITHM,
        "baseline_hash": None,
    }
    baseline_hash = _compute_baseline_hash(obj)
    return BareBaseline(
        baseline_id=baseline_id,
        question_release_ref_and_hash={
            "ref_id": question_release_ref_id,
            "sha256": question_release_sha256,
        },
        problem_only=True,
        no_tell_hint=True,
        all_results_retained=True,
        bare_attempt_results=results,
        baseline_hash=baseline_hash,
    )


def verify_bare_baseline(
    baseline: dict[str, Any] | BareBaseline,
) -> VerificationResult:
    """验证 BareBaseline 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. baseline_id 非空
    3. question_release_ref_and_hash 存在且结构合法（缺 ref = blocker）
    4. problem_only == True（bare 是 problem-only）
    5. no_tell_hint == True（bare 不含 Tell/Hint）
    6. all_results_retained == True（成功和失败都保留）
    7. 每个 bare_attempt_result 的 bare_status 在 QA1_BARE_STATUSES 中
    8. 每个 bare_attempt_result 的 tell_hint_included == False
    9. baseline_hash 正确
    """
    if isinstance(baseline, BareBaseline):
        baseline = baseline.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if baseline.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if baseline.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if baseline.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not baseline.get("baseline_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("baseline_id must not be empty")

    # question_release_ref_and_hash (blocker: missing ref)
    release_ref = baseline.get("question_release_ref_and_hash", {})
    if not _ref_and_hash_valid(release_ref):
        errors.append(EC.QA1_QUESTION_RELEASE_REF_MISSING)
        details.append(
            "question_release_ref_and_hash must have ref_id and sha256"
        )

    # problem_only (blocker: bare must be problem-only)
    if baseline.get("problem_only") is not True:
        errors.append(EC.QA1_BARE_NOT_PROBLEM_ONLY)
        details.append("problem_only must be True for P3B bare admission")

    # no_tell_hint (blocker: bare must not contain Tell/Hint)
    if baseline.get("no_tell_hint") is not True:
        errors.append(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE)
        details.append("no_tell_hint must be True for problem-only bare")

    # all_results_retained (blocker: success AND failure retained)
    if baseline.get("all_results_retained") is not True:
        errors.append(EC.QA1_BARE_RESULT_NOT_RETAINED)
        details.append("all_results_retained must be True")

    # bare_attempt_results
    results = baseline.get("bare_attempt_results", [])
    if not isinstance(results, list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("bare_attempt_results must be a list")
    else:
        for i, result in enumerate(results):
            if not isinstance(result, dict):
                errors.append(EC.REQUIRED_FIELD_MISSING)
                details.append(f"bare_attempt_result {i} is not a dict")
                continue
            status = result.get("bare_status", "")
            if status not in QA1_BARE_STATUSES:
                errors.append(EC.QA1_BARE_STATUS_INVALID)
                details.append(
                    f"bare_attempt_result {i}: bare_status {status!r} "
                    f"not in QA1_BARE_STATUSES"
                )
            if not result.get("problem_ref_id"):
                errors.append(EC.QA1_BARE_ATTEMPT_REF_MISSING)
                details.append(f"bare_attempt_result {i}: problem_ref_id is empty")
            if not result.get("attempt_ref_id"):
                errors.append(EC.QA1_BARE_ATTEMPT_REF_MISSING)
                details.append(f"bare_attempt_result {i}: attempt_ref_id is empty")
            # tell_hint_included must be False (blocker)
            if result.get("tell_hint_included") is not False:
                errors.append(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE)
                details.append(
                    f"bare_attempt_result {i}: tell_hint_included must be False"
                )

    # baseline_hash
    if baseline.get("baseline_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"unexpected baseline_hash_algorithm: "
            f"{baseline.get('baseline_hash_algorithm')}"
        )
    computed = _compute_baseline_hash(baseline)
    if baseline.get("baseline_hash") != computed:
        errors.append(EC.QA1_BARELINE_HASH_MISMATCH)
        details.append(
            f"baseline_hash mismatch: expected {computed}, "
            f"got {baseline.get('baseline_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
