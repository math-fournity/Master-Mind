"""ProofJudgment — Proof Judge 输出。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P6 节：

Proof Judge：数学正确性与完备性。

单 episode 只陈述观察事实。引用 blinded view by hash。分别 seal。

关键约束（blocker）：
- Judge 不得读取其他 Judge 的结论（AU_JUDGE_CONCLUSION_CROSS_READ）
- 引用 blinded view by hash（AU_VIEW_HASH_MISMATCH）
- 必须 sealed separately（AU_AUDIT_NOT_SEALED_SEPARATELY）
- 分歧不得由 Aggregator 自行裁决（AU_DISAGREEMENT_AUTO_RESOLVED）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_SCHEMA_ID = "seven/proof-judgment"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class ProofJudgment:
    """Proof Judge 输出——数学正确性与完备性评估。

    字段：
        judgment_id: 唯一标识
        plan_id: 对应的 AuditPlan ID
        view_ref: 引用的 blinded view {view_id, view_hash}
        math_correctness: 数学正确性评估
        completeness: 完备性评估
        observed_facts: 观察事实列表（单 episode，只陈述事实）
        conclusion: 结论（CORRECT / INCORRECT / INCOMPLETE / INCONCLUSIVE）
        lane_status: lane 终端状态
        sealed: 是否已 seal
        content_hash: 内容哈希
    """

    judgment_id: str
    plan_id: str
    view_ref: dict[str, str] = field(default_factory=dict)
    math_correctness: dict[str, Any] = field(default_factory=dict)
    completeness: dict[str, Any] = field(default_factory=dict)
    observed_facts: list[dict[str, Any]] = field(default_factory=list)
    conclusion: str = "INCONCLUSIVE"
    lane_status: str = "VALID"
    sealed: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "judgment_id": self.judgment_id,
            "plan_id": self.plan_id,
            "view_ref": dict(self.view_ref),
            "math_correctness": dict(self.math_correctness),
            "completeness": dict(self.completeness),
            "observed_facts": [dict(f) for f in self.observed_facts],
            "conclusion": self.conclusion,
            "lane_status": self.lane_status,
            "sealed": self.sealed,
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


def make_proof_judgment(
    *,
    judgment_id: str,
    plan_id: str,
    view_ref: dict[str, str],
    math_correctness: dict[str, Any] | None = None,
    completeness: dict[str, Any] | None = None,
    observed_facts: list[dict[str, Any]] | None = None,
    conclusion: str = "INCONCLUSIVE",
    lane_status: str = "VALID",
    sealed: bool = True,
) -> ProofJudgment:
    judgment = ProofJudgment(
        judgment_id=judgment_id,
        plan_id=plan_id,
        view_ref=view_ref,
        math_correctness=math_correctness or {},
        completeness=completeness or {},
        observed_facts=observed_facts or [],
        conclusion=conclusion,
        lane_status=lane_status,
        sealed=sealed,
    )
    return dataclasses.replace(judgment, content_hash=judgment.compute_content_hash())


@dataclass(frozen=True)
class ProofJudgmentVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    judgment_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def _check_cross_read(judgment: ProofJudgment, other_conclusion: str | None) -> bool:
    """检查 Judge 是否读取了其他 Judge 的结论。

    如果 judgment 的 math_correctness 或 completeness 中包含
    other_judge_conclusion 字段，则违规。
    """
    for section in (judgment.math_correctness, judgment.completeness):
        if "other_judge_conclusion" in section:
            return True
        if section.get("referenced_judgment_id"):
            return True
    if other_conclusion is not None:
        # 如果 judgment 的 conclusion 与 other 完全一致且显式引用
        if judgment.conclusion == other_conclusion and judgment.math_correctness.get(
            "copied_from_other_judge", False
        ):
            return True
    return False


def verify_proof_judgment(
    judgment: ProofJudgment,
    *,
    expected_view_hash: str | None = None,
    other_judge_conclusion: str | None = None,
) -> ProofJudgmentVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = judgment.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not judgment.judgment_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("judgment_id is empty")

    if not judgment.plan_id:
        errors.append(EC.AU_AUDIT_PLAN_REF_MISSING)
        details.append("plan_id is empty")

    # view_ref required
    if not judgment.view_ref.get("view_id"):
        errors.append(EC.AU_VIEW_REF_MISSING)
        details.append("view_ref missing view_id")
    if not judgment.view_ref.get("view_hash"):
        errors.append(EC.AU_VIEW_REF_MISSING)
        details.append("view_ref missing view_hash")

    if expected_view_hash is not None:
        if judgment.view_ref.get("view_hash") != expected_view_hash:
            errors.append(EC.AU_VIEW_HASH_MISMATCH)
            details.append(
                f"view_ref.view_hash {judgment.view_ref.get('view_hash')} != "
                f"expected {expected_view_hash}"
            )

    # Judge 不得读取其他 Judge 的结论
    if _check_cross_read(judgment, other_judge_conclusion):
        errors.append(EC.AU_JUDGE_CONCLUSION_CROSS_READ)
        details.append("judge read other judge's conclusion")

    # observed_facts 必须是观察事实
    for fact in judgment.observed_facts:
        if not isinstance(fact, dict) or not fact.get("observed", False):
            errors.append(EC.AU_OBSERVATION_NOT_FACT)
            details.append("observed_facts contains non-observed fact")
            break

    # 必须 sealed
    if not judgment.sealed:
        errors.append(EC.AU_AUDIT_NOT_SEALED_SEPARATELY)
        details.append("proof judgment must be sealed separately")

    # content_hash
    if not judgment.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif judgment.content_hash != judgment.compute_content_hash():
        errors.append(EC.AU_SEAL_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {judgment.content_hash}, "
            f"computed {judgment.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return ProofJudgmentVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        judgment_id=judgment.judgment_id,
    )
