"""HumanReadableSummary — P9 verdict 的人类可读摘要。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

Human-readable Summary of P9 verdict.

关键约束（blocker）：
- summary 无效 → VR_SUMMARY_INVALID

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
from .machine_verdict import MachineVerdict
from .six_gate import SixGateVerdict


_SCHEMA_ID = "seven/human-readable-summary"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class HumanReadableSummary:
    """P9 verdict 的人类可读摘要。

    字段：
        summary_id: 唯一标识
        dag_hash: sealed P0-P8 DAG hash
        verdict_hash: MachineVerdict content_hash
        title: 摘要标题
        overall_verdict: 综合判定
        factory_status: Factory 轴状态
        scientific_status: Scientific 轴状态
        scale_status: Scale 轴状态
        gate_summary: 六门摘要
        remainder_summary: remainder 摘要
        cost_summary: cost 摘要
        coverage_summary: coverage 摘要
        next_steps: 下一步建议
        full_text: 完整人类可读文本
        hash_algorithm: 哈希算法
        content_hash: summary 自身内容哈希
    """

    summary_id: str
    dag_hash: str = ""
    verdict_hash: str = ""
    title: str = ""
    overall_verdict: str = ""
    factory_status: str = ""
    scientific_status: str = ""
    scale_status: str = ""
    gate_summary: str = ""
    remainder_summary: str = ""
    cost_summary: str = ""
    coverage_summary: str = ""
    next_steps: tuple[str, ...] = ()
    full_text: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "summary_id": self.summary_id,
            "dag_hash": self.dag_hash,
            "verdict_hash": self.verdict_hash,
            "title": self.title,
            "overall_verdict": self.overall_verdict,
            "factory_status": self.factory_status,
            "scientific_status": self.scientific_status,
            "scale_status": self.scale_status,
            "gate_summary": self.gate_summary,
            "remainder_summary": self.remainder_summary,
            "cost_summary": self.cost_summary,
            "coverage_summary": self.coverage_summary,
            "next_steps": list(self.next_steps),
            "full_text": self.full_text,
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


def _build_full_text(
    title: str,
    overall_verdict: str,
    factory_status: str,
    scientific_status: str,
    scale_status: str,
    gate_summary: str,
    remainder_summary: str,
    cost_summary: str,
    coverage_summary: str,
    next_steps: list[str],
) -> str:
    """构建完整人类可读文本。"""
    lines = [
        f"# {title}",
        "",
        f"Overall Verdict: {overall_verdict}",
        "",
        "## Axis Verdicts",
        f"- Factory (system completeness): {factory_status}",
        f"- Scientific (evidence quality): {scientific_status}",
        f"- Scale (production readiness): {scale_status}",
        "",
        "## Six Gate Verdict",
        gate_summary,
        "",
        "## Remainder",
        remainder_summary,
        "",
        "## Cost",
        cost_summary,
        "",
        "## Coverage",
        coverage_summary,
        "",
        "## Next Steps",
    ]
    for i, step in enumerate(next_steps, 1):
        lines.append(f"{i}. {step}")
    return "\n".join(lines)


def make_human_readable_summary(
    *,
    summary_id: str,
    dag_hash: str,
    verdict: MachineVerdict,
    gate_verdict: SixGateVerdict,
    completion_remainder_zero: bool,
    full_chain_remainder_zero: bool,
    cost_summary: str = "",
    coverage_summary: str = "",
    next_steps: list[str] | None = None,
) -> HumanReadableSummary:
    """构建 HumanReadableSummary。"""
    factory = verdict.get_axis("FACTORY")
    scientific = verdict.get_axis("SCIENTIFIC")
    scale = verdict.get_axis("SCALE")

    factory_status = factory.status if factory else "NOT_TESTED"
    scientific_status = scientific.status if scientific else "NOT_TESTED"
    scale_status = scale.status if scale else "NOT_TESTED"

    # gate summary
    gate_lines = []
    for g in gate_verdict.gates:
        gate_lines.append(f"- {g.gate_kind}: {g.status}")
    gate_summary_text = "\n".join(gate_lines)

    # remainder summary
    cc_status = "remainder=0" if completion_remainder_zero else "remainder!=0"
    fc_status = "remainder=0" if full_chain_remainder_zero else "remainder!=0"
    remainder_text = (
        f"Completion Contract: {cc_status}\n"
        f"Full Chain: {fc_status}"
    )

    next_steps = next_steps or []
    title = f"P9 Verdict Summary — {verdict.verdict_id}"
    full_text = _build_full_text(
        title,
        verdict.overall_status,
        factory_status,
        scientific_status,
        scale_status,
        gate_summary_text,
        remainder_text,
        cost_summary,
        coverage_summary,
        next_steps,
    )

    summary = HumanReadableSummary(
        summary_id=summary_id,
        dag_hash=dag_hash,
        verdict_hash=verdict.content_hash,
        title=title,
        overall_verdict=verdict.overall_status,
        factory_status=factory_status,
        scientific_status=scientific_status,
        scale_status=scale_status,
        gate_summary=gate_summary_text,
        remainder_summary=remainder_text,
        cost_summary=cost_summary,
        coverage_summary=coverage_summary,
        next_steps=tuple(next_steps),
        full_text=full_text,
    )
    return dataclasses.replace(
        summary, content_hash=summary.compute_content_hash()
    )


def verify_human_readable_summary(
    summary: HumanReadableSummary,
) -> VerificationResult:
    """验证 HumanReadableSummary。

    blocker：
    - summary 无效 → VR_SUMMARY_INVALID
    - content_hash 不匹配 → VR_VERDICT_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = summary.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not summary.summary_id:
        errors.append(EC.VR_SUMMARY_INVALID)
        details.append("summary_id is empty")

    if not summary.dag_hash:
        errors.append(EC.VR_SUMMARY_INVALID)
        details.append("dag_hash is empty")

    if not summary.verdict_hash:
        errors.append(EC.VR_SUMMARY_INVALID)
        details.append("verdict_hash is empty")

    if not summary.title:
        errors.append(EC.VR_SUMMARY_INVALID)
        details.append("title is empty")

    if not summary.overall_verdict:
        errors.append(EC.VR_SUMMARY_INVALID)
        details.append("overall_verdict is empty")

    if not summary.full_text:
        errors.append(EC.VR_SUMMARY_INVALID)
        details.append("full_text is empty")

    # overall_verdict 必须是合法状态
    if summary.overall_verdict not in ("PASS", "FAIL", "NOT_TESTED", "BLOCKED"):
        errors.append(EC.VR_SUMMARY_INVALID)
        details.append(
            f"overall_verdict {summary.overall_verdict} is not a valid status"
        )

    # content_hash
    if not summary.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif summary.content_hash != summary.compute_content_hash():
        errors.append(EC.VR_VERDICT_HASH_MISMATCH)
        details.append("HumanReadableSummary content_hash mismatch")

    result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=result,
        error_codes=errors,
        details=details,
    )
