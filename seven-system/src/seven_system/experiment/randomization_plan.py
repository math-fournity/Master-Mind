"""RandomizationPlan — WP-EX1 冻结随机化 block/seed。

关键约束（blocker）：
- 冻结的 randomization block/seed
- 确定性重放：相同 seed → 相同 assignment（EX_RANDOMIZATION_NOT_REPLAYABLE）
- block_size 必须 > 0（EX_RANDOMIZATION_BLOCK_INVALID）
- seed 非空（EX_RANDOMIZATION_SEED_INVALID）

SIDE_EFFECT_FREE：纯内存实现，使用确定性 PRNG（Python random.Random with seed）。
"""

from __future__ import annotations

import dataclasses
import hashlib
import random
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_SCHEMA_ID = "seven/randomization-plan"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class RandomizationPlan:
    """冻结随机化 block/seed——确定性重放。

    字段：
        plan_id: 唯一标识
        seed: 随机种子（确定性重放的关键）
        block_size: block 大小（arm 数量）
        arm_order: 冻结的 arm 分配顺序（由 seed 确定）
        frozen: 是否冻结
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    plan_id: str
    seed: int = 0
    block_size: int = 0
    arm_order: tuple[str, ...] = ()
    frozen: bool = False
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "plan_id": self.plan_id,
            "seed": self.seed,
            "block_size": self.block_size,
            "arm_order": list(self.arm_order),
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

    def replay_assignment(self) -> dict[str, int]:
        """重放 arm 分配——返回 {arm_kind: block_position}。

        确定性：相同 seed + 相同 arm_order → 相同 assignment。
        """
        return {arm: pos for pos, arm in enumerate(self.arm_order)}


def _generate_arm_order(seed: int, arm_kinds: list[str]) -> tuple[str, ...]:
    """用 seed 确定性生成 arm 分配顺序。"""
    rng = random.Random(seed)
    shuffled = list(arm_kinds)
    rng.shuffle(shuffled)
    return tuple(shuffled)


def make_randomization_plan(
    *,
    plan_id: str,
    seed: int,
    arm_kinds: list[str],
    frozen: bool = True,
    frozen_at: str = "2026-08-14T12:00:00Z",
) -> RandomizationPlan:
    arm_order = _generate_arm_order(seed, arm_kinds)
    rp = RandomizationPlan(
        plan_id=plan_id,
        seed=seed,
        block_size=len(arm_kinds),
        arm_order=arm_order,
        frozen=frozen,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(rp, content_hash=rp.compute_content_hash())


@dataclass(frozen=True)
class RandomizationPlanVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    plan_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_randomization_plan(
    plan: RandomizationPlan,
) -> RandomizationPlanVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = plan.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # seed
    if not isinstance(plan.seed, int):
        errors.append(EC.EX_RANDOMIZATION_SEED_INVALID)
        details.append("seed must be an int")
    # seed can be 0 — that's a valid seed

    # block_size
    if plan.block_size <= 0:
        errors.append(EC.EX_RANDOMIZATION_BLOCK_INVALID)
        details.append(f"block_size must be > 0, got {plan.block_size}")

    # arm_order
    if not plan.arm_order:
        errors.append(EC.EX_RANDOMIZATION_BLOCK_INVALID)
        details.append("arm_order is empty")

    # deterministic replay check
    if plan.arm_order:
        replayed = _generate_arm_order(plan.seed, list(plan.arm_order))
        # replaying with the same seed and same input list should produce same order
        # but we need to check against the original arm_kinds (sorted)
        # Actually we check: same seed → same assignment
        expected_order = _generate_arm_order(plan.seed, sorted(plan.arm_order))
        if tuple(expected_order) != plan.arm_order:
            errors.append(EC.EX_RANDOMIZATION_NOT_REPLAYABLE)
            details.append(
                f"arm_order not replayable from seed {plan.seed}: "
                f"expected {expected_order}, got {list(plan.arm_order)}"
            )

    # frozen check
    if not plan.frozen:
        errors.append(EC.EX_RANDOMIZATION_NOT_REPLAYABLE)
        details.append("RandomizationPlan must be frozen")

    # content_hash
    if not plan.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif plan.content_hash != plan.compute_content_hash():
        errors.append(EC.EX_RANDOMIZATION_NOT_REPLAYABLE)
        details.append(
            f"content_hash mismatch: claims {plan.content_hash}, "
            f"computed {plan.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return RandomizationPlanVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        plan_id=plan.plan_id,
    )


def replay_randomization(
    seed: int,
    arm_kinds: list[str],
) -> tuple[str, ...]:
    """从 seed 确定性重放 arm 分配顺序。

    相同 seed + 相同 arm_kinds（排序后）→ 相同 arm_order。
    """
    sorted_kinds = sorted(arm_kinds)
    return _generate_arm_order(seed, sorted_kinds)
