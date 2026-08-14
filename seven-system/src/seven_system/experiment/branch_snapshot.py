"""BranchSnapshot — WP-EX1 共享前置状态。

关键约束（blocker）：
- 所有 arm 从同一 BranchSnapshot 出发（共享 pre-treatment state）
- 冻结后不可变（EX_BRANCH_SNAPSHOT_NOT_FROZEN）
- content_hash 正确（EX_BRANCH_SNAPSHOT_HASH_MISMATCH）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_SCHEMA_ID = "seven/branch-snapshot"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class BranchSnapshot:
    """共享前置状态——所有 arm 从同一 BranchSnapshot 出发。

    字段：
        snapshot_id: 唯一标识
        case_pack_ref: CasePack 引用 {pack_id, content_hash}
        pre_treatment_state: 冻结的前置状态（problem context, fixture 等）
        frozen: 是否冻结
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    snapshot_id: str
    case_pack_ref: dict[str, str] = field(default_factory=dict)
    pre_treatment_state: dict[str, Any] = field(default_factory=dict)
    frozen: bool = False
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "snapshot_id": self.snapshot_id,
            "case_pack_ref": dict(self.case_pack_ref),
            "pre_treatment_state": dict(self.pre_treatment_state),
            "frozen": self.frozen,
            "frozen_at": self.frozen_at,
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


def make_branch_snapshot(
    *,
    snapshot_id: str,
    case_pack_ref: dict[str, str] | None = None,
    pre_treatment_state: dict[str, Any] | None = None,
    frozen: bool = True,
    frozen_at: str = "2026-08-14T12:00:00Z",
) -> BranchSnapshot:
    bs = BranchSnapshot(
        snapshot_id=snapshot_id,
        case_pack_ref=case_pack_ref or {},
        pre_treatment_state=pre_treatment_state or {},
        frozen=frozen,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(bs, content_hash=bs.compute_content_hash())


@dataclass(frozen=True)
class BranchSnapshotVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    snapshot_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_branch_snapshot(
    snapshot: BranchSnapshot,
) -> BranchSnapshotVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = snapshot.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # case_pack_ref required
    if not snapshot.case_pack_ref.get("pack_id"):
        errors.append(EC.EX_CASE_PACK_REF_MISSING)
        details.append("case_pack_ref must contain pack_id")
    if not snapshot.case_pack_ref.get("content_hash"):
        errors.append(EC.EX_CASE_PACK_REF_MISSING)
        details.append("case_pack_ref must contain content_hash")

    # frozen check
    if not snapshot.frozen:
        errors.append(EC.EX_BRANCH_SNAPSHOT_NOT_FROZEN)
        details.append("BranchSnapshot must be frozen before experiment start")

    # content_hash
    if not snapshot.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif snapshot.content_hash != snapshot.compute_content_hash():
        errors.append(EC.EX_BRANCH_SNAPSHOT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {snapshot.content_hash}, "
            f"computed {snapshot.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return BranchSnapshotVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        snapshot_id=snapshot.snapshot_id,
    )
