"""CostAndCoverageDelta — P9 cost 聚合和 coverage delta。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

输出 cost 和 coverage delta，以及 next eligible work/coverage cells。

关键约束（blocker）：
- cost delta 不完整 → VR_COST_DELTA_INCOMPLETE
- coverage delta 不完整 → VR_COVERAGE_DELTA_INCOMPLETE

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/cost-coverage-delta"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class CostAggregation:
    """cost 聚合——按维度汇总。"""

    tokens: int = 0
    wallclock_seconds: float = 0.0
    human_minutes: int = 0
    provider_billed_amount: int = 0  # microunits
    complete: bool = True  # usage completeness

    def to_dict(self) -> dict[str, Any]:
        return {
            "tokens": self.tokens,
            "wallclock_seconds": self.wallclock_seconds,
            "human_minutes": self.human_minutes,
            "provider_billed_amount": self.provider_billed_amount,
            "complete": self.complete,
        }


@dataclass(frozen=True)
class CoverageCell:
    """coverage cell——单个覆盖单元。"""

    cell_key: str
    covered: bool
    evidence_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "cell_key": self.cell_key,
            "covered": self.covered,
            "evidence_hash": self.evidence_hash,
        }


@dataclass(frozen=True)
class CostAndCoverageDelta:
    """P9 cost 和 coverage delta。

    字段：
        delta_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        cost_p0: P0 阶段 cost
        cost_p9: P9 阶段 cost（聚合后）
        cost_delta: cost 变化
        coverage_before: P0 之前 coverage cells
        coverage_after: P9 之后 coverage cells
        coverage_delta_covered: 新覆盖的 cell 数
        coverage_delta_uncovered: 仍未覆盖的 cell 数
        next_eligible_work_cells: 下一步 eligible work cells
        next_eligible_coverage_cells: 下一步 eligible coverage cells
        cost_complete: cost 聚合是否完整
        coverage_complete: coverage delta 是否完整
        hash_algorithm: 哈希算法
        content_hash: delta 自身内容哈希
    """

    delta_id: str
    dag_hash: str = ""
    cost_p0: CostAggregation = field(default_factory=CostAggregation)
    cost_p9: CostAggregation = field(default_factory=CostAggregation)
    cost_delta: CostAggregation = field(default_factory=CostAggregation)
    coverage_before: tuple[CoverageCell, ...] = ()
    coverage_after: tuple[CoverageCell, ...] = ()
    coverage_delta_covered: int = 0
    coverage_delta_uncovered: int = 0
    next_eligible_work_cells: tuple[str, ...] = ()
    next_eligible_coverage_cells: tuple[str, ...] = ()
    cost_complete: bool = True
    coverage_complete: bool = True
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "delta_id": self.delta_id,
            "dag_hash": self.dag_hash,
            "cost_p0": self.cost_p0.to_dict(),
            "cost_p9": self.cost_p9.to_dict(),
            "cost_delta": self.cost_delta.to_dict(),
            "coverage_before": [c.to_dict() for c in self.coverage_before],
            "coverage_after": [c.to_dict() for c in self.coverage_after],
            "coverage_delta_covered": self.coverage_delta_covered,
            "coverage_delta_uncovered": self.coverage_delta_uncovered,
            "next_eligible_work_cells": list(self.next_eligible_work_cells),
            "next_eligible_coverage_cells": list(
                self.next_eligible_coverage_cells
            ),
            "cost_complete": self.cost_complete,
            "coverage_complete": self.coverage_complete,
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


def _compute_cost_delta(
    p0: CostAggregation, p9: CostAggregation
) -> CostAggregation:
    """计算 cost delta（P9 - P0）。"""
    return CostAggregation(
        tokens=p9.tokens - p0.tokens,
        wallclock_seconds=p9.wallclock_seconds - p0.wallclock_seconds,
        human_minutes=p9.human_minutes - p0.human_minutes,
        provider_billed_amount=(
            p9.provider_billed_amount - p0.provider_billed_amount
        ),
        complete=p0.complete and p9.complete,
    )


def _compute_coverage_delta(
    before: list[CoverageCell], after: list[CoverageCell]
) -> tuple[int, int]:
    """计算 coverage delta——新覆盖数和仍未覆盖数。"""
    before_covered = {c.cell_key for c in before if c.covered}
    after_covered = {c.cell_key for c in after if c.covered}
    newly_covered = after_covered - before_covered
    still_uncovered = {
        c.cell_key for c in after if not c.covered
    }
    return len(newly_covered), len(still_uncovered)


def make_cost_and_coverage_delta(
    *,
    delta_id: str,
    dag_hash: str,
    cost_p0: CostAggregation,
    cost_p9: CostAggregation,
    coverage_before: list[CoverageCell],
    coverage_after: list[CoverageCell],
    next_eligible_work_cells: list[str] | None = None,
    next_eligible_coverage_cells: list[str] | None = None,
) -> CostAndCoverageDelta:
    """构建 CostAndCoverageDelta。"""
    cost_delta = _compute_cost_delta(cost_p0, cost_p9)
    newly_covered, still_uncovered = _compute_coverage_delta(
        coverage_before, coverage_after
    )

    # next eligible coverage cells = 仍未覆盖的 cells
    if next_eligible_coverage_cells is None:
        next_eligible_coverage_cells = sorted(
            c.cell_key for c in coverage_after if not c.covered
        )

    delta = CostAndCoverageDelta(
        delta_id=delta_id,
        dag_hash=dag_hash,
        cost_p0=cost_p0,
        cost_p9=cost_p9,
        cost_delta=cost_delta,
        coverage_before=tuple(
            sorted(coverage_before, key=lambda c: c.cell_key)
        ),
        coverage_after=tuple(
            sorted(coverage_after, key=lambda c: c.cell_key)
        ),
        coverage_delta_covered=newly_covered,
        coverage_delta_uncovered=still_uncovered,
        next_eligible_work_cells=tuple(next_eligible_work_cells or ()),
        next_eligible_coverage_cells=tuple(
            sorted(next_eligible_coverage_cells)
        ),
        cost_complete=cost_delta.complete,
        coverage_complete=len(coverage_after) > 0,
    )
    return dataclasses.replace(
        delta, content_hash=delta.compute_content_hash()
    )


def verify_cost_and_coverage_delta(
    delta: CostAndCoverageDelta,
) -> VerificationResult:
    """验证 CostAndCoverageDelta。

    blocker：
    - cost delta 不完整 → VR_COST_DELTA_INCOMPLETE
    - coverage delta 不完整 → VR_COVERAGE_DELTA_INCOMPLETE
    - content_hash 不匹配 → VR_VERDICT_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = delta.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not delta.delta_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("delta_id is empty")

    if not delta.dag_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("dag_hash is empty")

    # cost delta 完整性
    if not delta.cost_complete:
        errors.append(EC.VR_COST_DELTA_INCOMPLETE)
        details.append(
            "cost delta incomplete — usage completeness not satisfied"
        )

    # coverage delta 完整性
    if not delta.coverage_complete:
        errors.append(EC.VR_COVERAGE_DELTA_INCOMPLETE)
        details.append(
            "coverage delta incomplete — no coverage cells after P9"
        )

    # cost delta 计算一致性
    expected_delta = _compute_cost_delta(delta.cost_p0, delta.cost_p9)
    if delta.cost_delta.tokens != expected_delta.tokens:
        errors.append(EC.VR_COST_DELTA_INCOMPLETE)
        details.append(
            f"cost_delta.tokens {delta.cost_delta.tokens} != "
            f"expected {expected_delta.tokens}"
        )

    # coverage delta 计算一致性
    expected_covered, expected_uncovered = _compute_coverage_delta(
        list(delta.coverage_before), list(delta.coverage_after)
    )
    if delta.coverage_delta_covered != expected_covered:
        errors.append(EC.VR_COVERAGE_DELTA_INCOMPLETE)
        details.append(
            f"coverage_delta_covered {delta.coverage_delta_covered} != "
            f"expected {expected_covered}"
        )

    # content_hash
    if not delta.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif delta.content_hash != delta.compute_content_hash():
        errors.append(EC.VR_VERDICT_HASH_MISMATCH)
        details.append("CostAndCoverageDelta content_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )
