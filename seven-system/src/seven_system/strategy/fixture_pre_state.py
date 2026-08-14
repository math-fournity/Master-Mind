"""FixturePreState — WP-ST1 开发/激活模式的显式前置状态。

关键约束（blocker）：
- development 模式使用显式 fixture_pre_state，不是 live Case
- activation 模式使用 CS1 Case/BranchSnapshot
- Fixture 冒充 live Case → BLOCK（ST_FIXTURE_MASQUERADE_LIVE_CASE）
- fixture_pre_state 必须引用 TellStrategyRelease by hash

SIDE_EFFECT_FREE：纯内存实现，不写 DB、不调用 live model、不启动 Solver。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ST_FIXTURE_MODES,
    VerificationErrorCode as EC,
)


_FIXTURE_SCHEMA_ID = "seven/fixture-pre-state"
_FIXTURE_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class FixturePreState:
    """显式 fixture 前置状态——development 模式的冻结输入。

    blocker: is_live_case 必须为 False。如果 fixture 冒充 live Case
    （is_live_case=True），验证器返回 ST_FIXTURE_MASQUERADE_LIVE_CASE。

    字段：
        fixture_id: 唯一标识
        mode: DEVELOPMENT / ACTIVATION（ST_FIXTURE_MODES）
        is_live_case: 是否冒充 live Case（必须 False）
        release_ref: TellStrategyRelease 引用 {release_id, content_hash}
        problem_context: 冻结的题目上下文（不是 live Case）
        branch_snapshot_ref: CS1 BranchSnapshot 引用（activation 模式）
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    fixture_id: str
    mode: str = "DEVELOPMENT"
    is_live_case: bool = False
    release_ref: dict[str, str] = field(default_factory=dict)
    problem_context: dict[str, Any] = field(default_factory=dict)
    branch_snapshot_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _FIXTURE_SCHEMA_ID,
            "schema_version": _FIXTURE_SCHEMA_VERSION,
            "fixture_id": self.fixture_id,
            "mode": self.mode,
            "is_live_case": self.is_live_case,
            "release_ref": dict(self.release_ref),
            "problem_context": dict(self.problem_context),
            "branch_snapshot_ref": dict(self.branch_snapshot_ref),
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


def make_fixture_pre_state(
    *,
    fixture_id: str,
    mode: str = "DEVELOPMENT",
    is_live_case: bool = False,
    release_ref: dict[str, str] | None = None,
    problem_context: dict[str, Any] | None = None,
    branch_snapshot_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> FixturePreState:
    fps = FixturePreState(
        fixture_id=fixture_id,
        mode=mode,
        is_live_case=is_live_case,
        release_ref=release_ref or {},
        problem_context=problem_context or {},
        branch_snapshot_ref=branch_snapshot_ref or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(fps, content_hash=fps.compute_content_hash())


@dataclass(frozen=True)
class FixturePreStateVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    fixture_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_fixture_pre_state(
    fixture: FixturePreState,
) -> FixturePreStateVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = fixture.to_dict()
    if d.get("schema_id") != _FIXTURE_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_FIXTURE_SCHEMA_ID}")

    # mode valid
    if fixture.mode not in ST_FIXTURE_MODES:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append(
            f"mode '{fixture.mode}' not in {sorted(ST_FIXTURE_MODES)}"
        )

    # blocker: fixture masquerading as live Case
    if fixture.is_live_case:
        errors.append(EC.ST_FIXTURE_MASQUERADE_LIVE_CASE)
        details.append(
            "is_live_case=True — fixture must NOT masquerade as live Case"
        )

    # release_ref required — must reference TellStrategyRelease by hash
    if not fixture.release_ref.get("release_id"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain release_id")
    if not fixture.release_ref.get("content_hash"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain content_hash")

    # activation mode requires branch_snapshot_ref
    if fixture.mode == "ACTIVATION":
        if not fixture.branch_snapshot_ref.get("case_id"):
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(
                "ACTIVATION mode requires branch_snapshot_ref with case_id"
            )

    # content_hash
    if not fixture.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif fixture.content_hash != fixture.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {fixture.content_hash}, "
            f"computed {fixture.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return FixturePreStateVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        fixture_id=fixture.fixture_id,
    )
