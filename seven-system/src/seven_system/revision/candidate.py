"""CandidateRelease — 冻结 candidate 用于 prospective evaluation。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P8 节和
docs/implementation/15-work-package-implementation-contracts.md WP-RV1：

candidate 自批 → BLOCK（RV_CANDIDATE_SELF_APPROVED）

关键约束（blocker）：
- candidate 必须冻结 → RV_CANDIDATE_NOT_FROZEN
- candidate 不得自批 → RV_CANDIDATE_SELF_APPROVED
- state 不在 RV_CANDIDATE_STATES → RV_CANDIDATE_STATE_INVALID
- content_hash 不匹配 → RV_CANDIDATE_HASH_MISMATCH

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
    RV_CANDIDATE_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/candidate-release"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class CandidateRelease:
    """冻结 candidate 用于 prospective evaluation。不得自批。

    字段：
        candidate_id: 唯一标识
        revision_proposal_hash: 引用的 RevisionProposal content_hash
        candidate_artifact_ref: candidate artifact 引用 {artifact_id, content_hash}
        state: 状态（RV_CANDIDATE_STATES）
        frozen: 是否已冻结
        frozen_at: 冻结时间
        self_approved: 是否自批（必须 False）
        approver_actor_id: 批准者 actor ID（不得等于 candidate 创建者）
        creator_actor_id: candidate 创建者 actor ID
        hash_algorithm: 哈希算法
        content_hash: 内容哈希
    """

    candidate_id: str
    revision_proposal_hash: str = ""
    candidate_artifact_ref: dict[str, str] = field(default_factory=dict)
    state: str = "DRAFT"
    frozen: bool = False
    frozen_at: str = ""
    self_approved: bool = False
    approver_actor_id: str = ""
    creator_actor_id: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "candidate_id": self.candidate_id,
            "revision_proposal_hash": self.revision_proposal_hash,
            "candidate_artifact_ref": dict(self.candidate_artifact_ref),
            "state": self.state,
            "frozen": self.frozen,
            "frozen_at": self.frozen_at,
            "self_approved": self.self_approved,
            "approver_actor_id": self.approver_actor_id,
            "creator_actor_id": self.creator_actor_id,
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
class CandidateReleaseVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    candidate_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def make_candidate_release(
    *,
    candidate_id: str,
    revision_proposal_hash: str,
    candidate_artifact_ref: dict[str, str],
    creator_actor_id: str,
    frozen: bool = False,
    approver_actor_id: str = "",
    frozen_at: str | None = None,
) -> CandidateRelease:
    """构建 CandidateRelease。

    self_approved 自动派生：approver == creator 时为 True（blocker）。
    """
    frozen_at = frozen_at or datetime.now(timezone.utc).isoformat()
    self_approved = bool(approver_actor_id) and approver_actor_id == creator_actor_id
    state = "FROZEN" if frozen else "DRAFT"
    cand = CandidateRelease(
        candidate_id=candidate_id,
        revision_proposal_hash=revision_proposal_hash,
        candidate_artifact_ref=dict(candidate_artifact_ref),
        state=state,
        frozen=frozen,
        frozen_at=frozen_at if frozen else "",
        self_approved=self_approved,
        approver_actor_id=approver_actor_id,
        creator_actor_id=creator_actor_id,
    )
    return dataclasses.replace(cand, content_hash=cand.compute_content_hash())


def verify_candidate_release(
    cand: CandidateRelease,
) -> CandidateReleaseVerificationResult:
    """验证 CandidateRelease。

    blocker：
    - 未冻结 → RV_CANDIDATE_NOT_FROZEN
    - 自批 → RV_CANDIDATE_SELF_APPROVED
    - state 不合法 → RV_CANDIDATE_STATE_INVALID
    - content_hash 不匹配 → RV_CANDIDATE_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = cand.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not cand.candidate_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("candidate_id is empty")

    if not cand.revision_proposal_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("revision_proposal_hash is empty")

    if not cand.candidate_artifact_ref:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("candidate_artifact_ref is empty")

    # state 合法性
    if cand.state not in RV_CANDIDATE_STATES:
        errors.append(EC.RV_CANDIDATE_STATE_INVALID)
        details.append(f"state {cand.state!r} not in RV_CANDIDATE_STATES")

    # 冻结约束
    if not cand.frozen:
        errors.append(EC.RV_CANDIDATE_NOT_FROZEN)
        details.append("CandidateRelease must be frozen before prospective evaluation")

    # 自批约束
    if cand.self_approved:
        errors.append(EC.RV_CANDIDATE_SELF_APPROVED)
        details.append(
            f"CandidateRelease must not be self-approved: "
            f"approver {cand.approver_actor_id!r} == creator {cand.creator_actor_id!r}"
        )
    elif cand.approver_actor_id and cand.creator_actor_id and cand.approver_actor_id == cand.creator_actor_id:
        errors.append(EC.RV_CANDIDATE_SELF_APPROVED)
        details.append("approver_actor_id equals creator_actor_id — candidate self-approval")

    # content_hash
    if not cand.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif cand.content_hash != cand.compute_content_hash():
        errors.append(EC.RV_CANDIDATE_HASH_MISMATCH)
        details.append("CandidateRelease content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return CandidateReleaseVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        candidate_id=cand.candidate_id,
    )


def check_candidate_not_self_approved(cand: CandidateRelease) -> VerificationResult:
    """检查 candidate 不得自批。"""
    errors: list[EC] = []
    details: list[str] = []
    if cand.self_approved:
        errors.append(EC.RV_CANDIDATE_SELF_APPROVED)
        details.append("CandidateRelease must not be self-approved")
    elif cand.approver_actor_id and cand.creator_actor_id and cand.approver_actor_id == cand.creator_actor_id:
        errors.append(EC.RV_CANDIDATE_SELF_APPROVED)
        details.append("approver equals creator — candidate self-approval")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
