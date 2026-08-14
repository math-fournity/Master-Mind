"""RevisionPolicy — 冻结的修订策略。

来自 docs/implementation/15-work-package-implementation-contracts.md WP-RV1：

冻结输入: sealed P7 EvidenceRecord集合、ProvenanceSnapshot、Revision policy

关键约束（blocker）：
- RevisionPolicy 必须冻结 → RV_REVISION_POLICY_NOT_FROZEN
- content_hash 不匹配 → RV_REVISION_POLICY_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_SCHEMA_ID = "seven/revision-policy"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class RevisionPolicy:
    """冻结的修订策略——何时允许修订、需要什么证据、holdout 如何消费、需要几个 HumanGate。

    字段：
        policy_id: 唯一标识
        frozen: 是否已冻结（必须 True）
        frozen_at: 冻结时间
        requires_two_human_gates: 是否需要两个 HumanGate 批准（必须 True）
        holdout_viewed_immediately_consumed: viewed holdout 是否立即 consumed（必须 True）
        fit_not_confirmation: fit≠confirmation（必须 True）
        no_single_case_split: 禁止单例 split（必须 True）
        candidate_not_self_approved: candidate 不得自批（必须 True）
        prospective_one_time: prospective 一次性（必须 True）
        old_evidence_not_modified: 旧证据不得修改（必须 True）
        no_evidence_index_in_p8: P8 不读取 EvidenceIndex（必须 True）
        hash_algorithm: 哈希算法
        content_hash: 内容哈希
    """

    policy_id: str
    frozen: bool = False
    frozen_at: str = ""
    requires_two_human_gates: bool = True
    holdout_viewed_immediately_consumed: bool = True
    fit_not_confirmation: bool = True
    no_single_case_split: bool = True
    candidate_not_self_approved: bool = True
    prospective_one_time: bool = True
    old_evidence_not_modified: bool = True
    no_evidence_index_in_p8: bool = True
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "policy_id": self.policy_id,
            "frozen": self.frozen,
            "frozen_at": self.frozen_at,
            "requires_two_human_gates": self.requires_two_human_gates,
            "holdout_viewed_immediately_consumed": self.holdout_viewed_immediately_consumed,
            "fit_not_confirmation": self.fit_not_confirmation,
            "no_single_case_split": self.no_single_case_split,
            "candidate_not_self_approved": self.candidate_not_self_approved,
            "prospective_one_time": self.prospective_one_time,
            "old_evidence_not_modified": self.old_evidence_not_modified,
            "no_evidence_index_in_p8": self.no_evidence_index_in_p8,
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
class RevisionPolicyVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    policy_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def make_revision_policy(
    *,
    policy_id: str,
    frozen: bool = True,
    frozen_at: str | None = None,
) -> RevisionPolicy:
    """构建 RevisionPolicy。所有约束标志默认为 True。"""
    frozen_at = frozen_at or datetime.now(timezone.utc).isoformat()
    policy = RevisionPolicy(
        policy_id=policy_id,
        frozen=frozen,
        frozen_at=frozen_at if frozen else "",
    )
    return dataclasses.replace(policy, content_hash=policy.compute_content_hash())


def verify_revision_policy(
    policy: RevisionPolicy,
) -> RevisionPolicyVerificationResult:
    """验证 RevisionPolicy。

    blocker：
    - 未冻结 → RV_REVISION_POLICY_NOT_FROZEN
    - 任一约束标志不为 True → 对应 blocker
    - content_hash 不匹配 → RV_REVISION_POLICY_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = policy.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not policy.policy_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("policy_id is empty")

    # 冻结约束
    if not policy.frozen:
        errors.append(EC.RV_REVISION_POLICY_NOT_FROZEN)
        details.append("RevisionPolicy must be frozen")

    # 约束标志
    if not policy.requires_two_human_gates:
        errors.append(EC.RV_REVISION_WITHOUT_TWO_GATES)
        details.append("requires_two_human_gates must be True")
    if not policy.holdout_viewed_immediately_consumed:
        errors.append(EC.RV_HOLDOUT_REPEATED_PEEK)
        details.append("holdout_viewed_immediately_consumed must be True")
    if not policy.fit_not_confirmation:
        errors.append(EC.RV_FIT_EQUALS_CONFIRMATION)
        details.append("fit_not_confirmation must be True")
    if not policy.no_single_case_split:
        errors.append(EC.RV_SINGLE_CASE_SPLIT)
        details.append("no_single_case_split must be True")
    if not policy.candidate_not_self_approved:
        errors.append(EC.RV_CANDIDATE_SELF_APPROVED)
        details.append("candidate_not_self_approved must be True")
    if not policy.prospective_one_time:
        errors.append(EC.RV_PROSPECTIVE_NOT_ONE_TIME)
        details.append("prospective_one_time must be True")
    if not policy.old_evidence_not_modified:
        errors.append(EC.RV_OLD_EVIDENCE_MODIFIED)
        details.append("old_evidence_not_modified must be True")
    if not policy.no_evidence_index_in_p8:
        errors.append(EC.RV_EVIDENCE_INDEX_READ_IN_P8)
        details.append("no_evidence_index_in_p8 must be True")

    # content_hash
    if not policy.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif policy.content_hash != policy.compute_content_hash():
        errors.append(EC.RV_REVISION_POLICY_HASH_MISMATCH)
        details.append("RevisionPolicy content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return RevisionPolicyVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        policy_id=policy.policy_id,
    )
