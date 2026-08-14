"""Critic — WP-ST1 评估注入结果。

关键约束（blocker）：
- Critic 使用 TX1 的 CriticContract 定义评估标准
- Critic 评估注入结果：helped / hurt / neutral
- Critic 必须有 injection（ST_CRITIC_WITHOUT_INJECTION）
- CriticDecision 记录评估结果
- 组件版本必须与 release 锁定的版本一致（ST_COMPONENT_DRIFT）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ST_CRITIC_DECISIONS,
    VerificationErrorCode as EC,
)


_CRITIC_SCHEMA_ID = "seven/critic-decision"
_CRITIC_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class CriticDecision:
    """Critic 评估决策——记录注入结果评估。

    字段：
        critic_id: 唯一标识
        release_ref: TellStrategyRelease 引用
        injection_receipt_id: 上游 InjectionReceipt ID（必须非空）
        critic_contract_ref: CriticContract 引用 {contract_id, content_hash}
        verdict: 评估结论（ST_CRITIC_DECISIONS: HELPED/HURT/NEUTRAL）
        evidence: 评估证据列表
        reasoning: 评估推理
        component_version: critic 组件版本
        content_hash: 内容哈希
    """

    critic_id: str
    release_ref: dict[str, str] = field(default_factory=dict)
    injection_receipt_id: str = ""
    critic_contract_ref: dict[str, str] = field(default_factory=dict)
    verdict: str = "NEUTRAL"
    evidence: tuple[dict[str, Any], ...] = ()
    reasoning: str = ""
    component_version: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _CRITIC_SCHEMA_ID,
            "schema_version": _CRITIC_SCHEMA_VERSION,
            "critic_id": self.critic_id,
            "release_ref": dict(self.release_ref),
            "injection_receipt_id": self.injection_receipt_id,
            "critic_contract_ref": dict(self.critic_contract_ref),
            "verdict": self.verdict,
            "evidence": [dict(e) for e in self.evidence],
            "reasoning": self.reasoning,
            "component_version": self.component_version,
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


def make_critic_decision(
    *,
    critic_id: str,
    release_ref: dict[str, str] | None = None,
    injection_receipt_id: str = "",
    critic_contract_ref: dict[str, str] | None = None,
    verdict: str = "NEUTRAL",
    evidence: tuple[dict[str, Any], ...] = (),
    reasoning: str = "",
    component_version: str = "",
    frozen_at: str = "",
) -> CriticDecision:
    c = CriticDecision(
        critic_id=critic_id,
        release_ref=release_ref or {},
        injection_receipt_id=injection_receipt_id,
        critic_contract_ref=critic_contract_ref or {},
        verdict=verdict,
        evidence=evidence,
        reasoning=reasoning,
        component_version=component_version,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(c, content_hash=c.compute_content_hash())


@dataclass(frozen=True)
class CriticDecisionVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    critic_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_critic_decision(
    decision: CriticDecision,
    *,
    expected_release_hash: str | None = None,
    expected_component_version: str | None = None,
    expected_contract_hash: str | None = None,
) -> CriticDecisionVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = decision.to_dict()
    if d.get("schema_id") != _CRITIC_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_CRITIC_SCHEMA_ID}")

    # release_ref required
    if not decision.release_ref.get("release_id"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain release_id")
    if not decision.release_ref.get("content_hash"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain content_hash")

    if expected_release_hash is not None:
        if decision.release_ref.get("content_hash") != expected_release_hash:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"release_ref content_hash mismatch: claims "
                f"{decision.release_ref.get('content_hash')}, "
                f"expected {expected_release_hash}"
            )

    # blocker: critic without injection
    if not decision.injection_receipt_id:
        errors.append(EC.ST_CRITIC_WITHOUT_INJECTION)
        details.append(
            "injection_receipt_id is empty — critic requires an injection"
        )

    # critic_contract_ref required
    if not decision.critic_contract_ref.get("contract_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("critic_contract_ref must contain contract_id")
    if not decision.critic_contract_ref.get("content_hash"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("critic_contract_ref must contain content_hash")

    if expected_contract_hash is not None:
        if decision.critic_contract_ref.get("content_hash") != expected_contract_hash:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"critic_contract_ref content_hash mismatch: claims "
                f"{decision.critic_contract_ref.get('content_hash')}, "
                f"expected {expected_contract_hash}"
            )

    # verdict valid
    if decision.verdict not in ST_CRITIC_DECISIONS:
        errors.append(EC.ST_CRITIC_VERDICT_INVALID)
        details.append(
            f"verdict '{decision.verdict}' not in "
            f"{sorted(ST_CRITIC_DECISIONS)}"
        )

    # component version drift
    if expected_component_version is not None:
        if decision.component_version != expected_component_version:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"component_version drift: claims "
                f"{decision.component_version}, expected "
                f"{expected_component_version}"
            )

    # content_hash
    if not decision.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif decision.content_hash != decision.compute_content_hash():
        errors.append(EC.ST_CRITIC_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {decision.content_hash}, "
            f"computed {decision.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return CriticDecisionVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        critic_id=decision.critic_id,
    )


class Critic:
    """Critic — 评估注入结果。

    纯程序实现：给定 injection + verdict，产出 CriticDecision。
    """

    def __init__(self, *, component_version: str = "st1-critic-v1") -> None:
        self.component_version = component_version

    def evaluate(
        self,
        *,
        critic_id: str,
        release_ref: dict[str, str],
        injection_receipt_id: str,
        critic_contract_ref: dict[str, str],
        verdict: str = "NEUTRAL",
        evidence: tuple[dict[str, Any], ...] = (),
        reasoning: str = "",
        frozen_at: str = "",
    ) -> CriticDecision:
        return make_critic_decision(
            critic_id=critic_id,
            release_ref=release_ref,
            injection_receipt_id=injection_receipt_id,
            critic_contract_ref=critic_contract_ref,
            verdict=verdict,
            evidence=evidence,
            reasoning=reasoning,
            component_version=self.component_version,
            frozen_at=frozen_at,
        )
