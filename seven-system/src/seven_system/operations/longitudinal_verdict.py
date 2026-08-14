"""LongitudinalLearningVerdict — 跨 Epoch 长期学习结论。

来自 WP-OP1：long-term learning conclusion across Epochs。
NOT 单 Epoch verdict（那是 VR1）。

关键约束（blocker）：
- longitudinal verdict 无效 → OP_LONGITUDINAL_VERDICT_INVALID
- hash 不匹配 → OP_LONGITUDINAL_VERDICT_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存模拟。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


class LongitudinalVerdictError(Exception):
    """Longitudinal learning verdict 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class EpochLearningSummary:
    """单个 Epoch 的学习摘要。"""

    epoch_id: str
    coverage_gain: int
    evidence_count: int
    verdict: str  # PASS / FAIL / NOT_TESTED

    def to_dict(self) -> dict[str, Any]:
        return {
            "epoch_id": self.epoch_id,
            "coverage_gain": self.coverage_gain,
            "evidence_count": self.evidence_count,
            "verdict": self.verdict,
        }


@dataclass
class LongitudinalLearningVerdict:
    """跨 Epoch 长期学习结论。

    汇总多个 Epoch 的学习成果，给出长期学习结论。
    NOT 单 Epoch verdict（那是 VR1 的 MachineVerdict）。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    verdict_id: str
    epoch_summaries: list[EpochLearningSummary] = field(default_factory=list)
    total_coverage_gain: int = 0
    total_evidence: int = 0
    overall_verdict: str = "NOT_TESTED"
    learning_trend: str = "UNKNOWN"  # IMPROVING / STABLE / DECLINING / UNKNOWN
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "verdict_id": self.verdict_id,
            "epoch_summaries": [s.to_dict() for s in self.epoch_summaries],
            "total_coverage_gain": self.total_coverage_gain,
            "total_evidence": self.total_evidence,
            "overall_verdict": self.overall_verdict,
            "learning_trend": self.learning_trend,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


def build_longitudinal_learning_verdict(
    *,
    verdict_id: str,
    epoch_summaries: list[EpochLearningSummary],
) -> LongitudinalLearningVerdict:
    """构建 LongitudinalLearningVerdict。

    自动计算 total_coverage_gain、total_evidence、overall_verdict、
    learning_trend。
    """
    total_cov = sum(s.coverage_gain for s in epoch_summaries)
    total_ev = sum(s.evidence_count for s in epoch_summaries)

    # overall verdict：所有 epoch PASS → PASS，任一 FAIL → FAIL，否则 NOT_TESTED
    verdicts = [s.verdict for s in epoch_summaries]
    if not verdicts:
        overall = "NOT_TESTED"
    elif all(v == "PASS" for v in verdicts):
        overall = "PASS"
    elif any(v == "FAIL" for v in verdicts):
        overall = "FAIL"
    else:
        overall = "NOT_TESTED"

    # learning trend：比较前后 epoch 的 coverage_gain
    if len(epoch_summaries) < 2:
        trend = "UNKNOWN"
    else:
        gains = [s.coverage_gain for s in epoch_summaries]
        later = sum(gains[len(gains) // 2:])
        earlier = sum(gains[: len(gains) // 2])
        if later > earlier:
            trend = "IMPROVING"
        elif later == earlier:
            trend = "STABLE"
        else:
            trend = "DECLINING"

    verdict = LongitudinalLearningVerdict(
        verdict_id=verdict_id,
        epoch_summaries=list(epoch_summaries),
        total_coverage_gain=total_cov,
        total_evidence=total_ev,
        overall_verdict=overall,
        learning_trend=trend,
    )
    verdict.content_hash = verdict.compute_content_hash()
    return verdict


def verify_longitudinal_learning_verdict(
    verdict: LongitudinalLearningVerdict,
) -> list[tuple[EC, str]]:
    """验证 LongitudinalLearningVerdict。"""
    errors: list[tuple[EC, str]] = []
    if not verdict.verdict_id:
        errors.append((EC.OP_LONGITUDINAL_VERDICT_INVALID, "verdict_id empty"))
    if not verdict.epoch_summaries:
        errors.append((
            EC.OP_LONGITUDINAL_VERDICT_INVALID,
            "epoch_summaries empty",
        ))
    # 验证 total 一致
    expected_cov = sum(s.coverage_gain for s in verdict.epoch_summaries)
    if verdict.total_coverage_gain != expected_cov:
        errors.append((
            EC.OP_LONGITUDINAL_VERDICT_INVALID,
            f"total_coverage_gain {verdict.total_coverage_gain} != "
            f"expected {expected_cov}",
        ))
    expected_ev = sum(s.evidence_count for s in verdict.epoch_summaries)
    if verdict.total_evidence != expected_ev:
        errors.append((
            EC.OP_LONGITUDINAL_VERDICT_INVALID,
            f"total_evidence {verdict.total_evidence} != "
            f"expected {expected_ev}",
        ))
    # 验证 overall_verdict 合法
    if verdict.overall_verdict not in ("PASS", "FAIL", "NOT_TESTED"):
        errors.append((
            EC.OP_LONGITUDINAL_VERDICT_INVALID,
            f"overall_verdict {verdict.overall_verdict!r} invalid",
        ))
    # 验证 learning_trend 合法
    if verdict.learning_trend not in (
        "IMPROVING", "STABLE", "DECLINING", "UNKNOWN"
    ):
        errors.append((
            EC.OP_LONGITUDINAL_VERDICT_INVALID,
            f"learning_trend {verdict.learning_trend!r} invalid",
        ))
    # 验证 hash
    if not verdict.is_hash_valid:
        errors.append((
            EC.OP_LONGITUDINAL_VERDICT_HASH_MISMATCH,
            f"LongitudinalLearningVerdict {verdict.verdict_id} "
            f"content_hash invalid",
        ))
    # 验证每个 epoch summary
    for s in verdict.epoch_summaries:
        if not s.epoch_id:
            errors.append((
                EC.OP_LONGITUDINAL_VERDICT_INVALID,
                "epoch_summary epoch_id empty",
            ))
        if s.verdict not in ("PASS", "FAIL", "NOT_TESTED"):
            errors.append((
                EC.OP_LONGITUDINAL_VERDICT_INVALID,
                f"epoch {s.epoch_id} verdict {s.verdict!r} invalid",
            ))
    return errors
