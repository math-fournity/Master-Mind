"""ProspectiveEvaluation — 一次性 prospective 确认。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P8 节：

one-time prospective confirmation of candidate. Cannot reuse already-viewed
holdout.

关键约束（blocker）：
- prospective 必须一次性 → RV_PROSPECTIVE_NOT_ONE_TIME
- 不得复用已 viewed holdout → RV_PROSPECTIVE_REUSES_HOLDOUT
- state 不在 RV_PROSPECTIVE_STATES → RV_PROSPECTIVE_STATE_INVALID
- content_hash 不匹配 → RV_PROSPECTIVE_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    RV_PROSPECTIVE_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/prospective-evaluation"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class ProspectiveEvaluation:
    """一次性 prospective 确认 candidate。不得复用已 viewed holdout。

    字段：
        prospective_id: 唯一标识
        candidate_release_hash: 引用的 CandidateRelease content_hash
        holdout_view_ref: 使用的 holdout view 引用 {view_id, holdout_id}
        state: 状态（RV_PROSPECTIVE_STATES）
        one_time: 是否一次性（必须 True）
        reused_viewed_holdout: 是否复用已 viewed holdout（必须 False）
        confirmed: 是否确认
        evaluated_at: 评估时间
        hash_algorithm: 哈希算法
        content_hash: 内容哈希
    """

    prospective_id: str
    candidate_release_hash: str = ""
    holdout_view_ref: dict[str, str] = field(default_factory=dict)
    state: str = "PENDING"
    one_time: bool = True
    reused_viewed_holdout: bool = False
    confirmed: bool = False
    evaluated_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "prospective_id": self.prospective_id,
            "candidate_release_hash": self.candidate_release_hash,
            "holdout_view_ref": dict(self.holdout_view_ref),
            "state": self.state,
            "one_time": self.one_time,
            "reused_viewed_holdout": self.reused_viewed_holdout,
            "confirmed": self.confirmed,
            "evaluated_at": self.evaluated_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


@dataclass(frozen=True)
class ProspectiveEvaluationVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    prospective_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def make_prospective_evaluation(
    *,
    prospective_id: str,
    candidate_release_hash: str,
    holdout_view_ref: dict[str, str],
    confirmed: bool = False,
    reused_viewed_holdout: bool = False,
    evaluated_at: str | None = None,
) -> ProspectiveEvaluation:
    """构建 ProspectiveEvaluation。

    one_time 强制为 True。state 根据 confirmed 派生。
    """
    evaluated_at = evaluated_at or datetime.now(timezone.utc).isoformat()
    state = "CONFIRMED" if confirmed else ("REJECTED" if reused_viewed_holdout else "PENDING")
    pe = ProspectiveEvaluation(
        prospective_id=prospective_id,
        candidate_release_hash=candidate_release_hash,
        holdout_view_ref=dict(holdout_view_ref),
        state=state,
        one_time=True,
        reused_viewed_holdout=reused_viewed_holdout,
        confirmed=confirmed,
        evaluated_at=evaluated_at,
    )
    return dataclasses.replace(pe, content_hash=pe.compute_content_hash())


def verify_prospective_evaluation(
    pe: ProspectiveEvaluation,
) -> ProspectiveEvaluationVerificationResult:
    """验证 ProspectiveEvaluation。

    blocker：
    - 非一次性 → RV_PROSPECTIVE_NOT_ONE_TIME
    - 复用已 viewed holdout → RV_PROSPECTIVE_REUSES_HOLDOUT
    - state 不合法 → RV_PROSPECTIVE_STATE_INVALID
    - content_hash 不匹配 → RV_PROSPECTIVE_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = pe.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not pe.prospective_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("prospective_id is empty")

    if not pe.candidate_release_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("candidate_release_hash is empty")

    if not pe.holdout_view_ref:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("holdout_view_ref is empty")

    # state 合法性
    if pe.state not in RV_PROSPECTIVE_STATES:
        errors.append(EC.RV_PROSPECTIVE_STATE_INVALID)
        details.append(f"state {pe.state!r} not in RV_PROSPECTIVE_STATES")

    # 一次性约束
    if not pe.one_time:
        errors.append(EC.RV_PROSPECTIVE_NOT_ONE_TIME)
        details.append("ProspectiveEvaluation must be one-time")

    # 不得复用已 viewed holdout
    if pe.reused_viewed_holdout:
        errors.append(EC.RV_PROSPECTIVE_REUSES_HOLDOUT)
        details.append("ProspectiveEvaluation must not reuse already-viewed holdout")

    # content_hash
    if not pe.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif pe.content_hash != pe.compute_content_hash():
        errors.append(EC.RV_PROSPECTIVE_HASH_MISMATCH)
        details.append("ProspectiveEvaluation content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return ProspectiveEvaluationVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        prospective_id=pe.prospective_id,
    )


def check_prospective_one_time(pe: ProspectiveEvaluation) -> VerificationResult:
    """检查 prospective 必须一次性。"""
    errors: list[EC] = []
    details: list[str] = []
    if not pe.one_time:
        errors.append(EC.RV_PROSPECTIVE_NOT_ONE_TIME)
        details.append("ProspectiveEvaluation must be one-time")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_prospective_no_reuse_viewed_holdout(
    pe: ProspectiveEvaluation,
    *,
    viewed_holdout_ids: set[str] | None = None,
) -> VerificationResult:
    """检查 prospective 不得复用已 viewed holdout。

    viewed_holdout_ids: 已 viewed 的 holdout ID 集合（来自 HoldoutConsumption）。
    """
    errors: list[EC] = []
    details: list[str] = []
    if pe.reused_viewed_holdout:
        errors.append(EC.RV_PROSPECTIVE_REUSES_HOLDOUT)
        details.append("ProspectiveEvaluation explicitly reuses viewed holdout")
    if viewed_holdout_ids is not None and pe.holdout_view_ref:
        holdout_id = pe.holdout_view_ref.get("holdout_id", "")
        if holdout_id in viewed_holdout_ids:
            errors.append(EC.RV_PROSPECTIVE_REUSES_HOLDOUT)
            details.append(f"holdout {holdout_id!r} already viewed — cannot reuse")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
