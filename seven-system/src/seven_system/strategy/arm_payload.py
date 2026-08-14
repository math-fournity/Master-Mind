"""ArmPayload — WP-ST1 冻结的实验对比臂。

关键约束（blocker）：
- ArmPayload 是冻结的实验对比臂，从 TellStrategyRelease 确定性重放
- Arm kinds: PROBLEM_ONLY (baseline), LINEAGE, DIRECTION, LINEAGE_DIRECTION,
  DISTRACTOR, OPERATION_CRITIC, POSITION_NEUTRAL
- Distractor arm 必须与其他 arm 资源预算对等
  （ST_DISTRACTOR_NOT_EQUIVALENT）
- 每个 arm 是确定性重放：相同 release + 相同 arm spec → 相同 payload
  （ST_ARM_PAYLOAD_NOT_REPLAYABLE）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ST_ARM_KINDS,
    VerificationErrorCode as EC,
)


_ARM_SCHEMA_ID = "seven/arm-payload"
_ARM_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"

# 默认资源预算（所有 arm 必须对等）
_DEFAULT_BUDGET: dict[str, int] = {
    "wallclock_seconds": 600,
    "max_tokens": 8192,
    "max_cost_microunits": 0,
}


@dataclass(frozen=True)
class ArmPayload:
    """冻结的实验对比臂——从 TellStrategyRelease 确定性重放。

    字段：
        arm_id: 唯一标识
        arm_kind: 臂种类（ST_ARM_KINDS）
        release_ref: TellStrategyRelease 引用 {release_id, content_hash}
        budget_contract: 资源预算（必须与其他 arm 对等）
        hint_enabled: 是否启用 hint（PROBLEM_ONLY 为 False）
        selector_spec: selector 规格（hint_enabled=False 时为空）
        renderer_spec: renderer 规格
        binding_spec: binding 规格
        injection_spec: injection 规格
        replay_hash: 重放确定性 hash（相同输入 → 相同 hash）
        content_hash: 内容哈希
    """

    arm_id: str
    arm_kind: str
    release_ref: dict[str, str] = field(default_factory=dict)
    budget_contract: dict[str, int] = field(default_factory=lambda: dict(_DEFAULT_BUDGET))
    hint_enabled: bool = True
    selector_spec: dict[str, Any] = field(default_factory=dict)
    renderer_spec: dict[str, Any] = field(default_factory=dict)
    binding_spec: dict[str, Any] = field(default_factory=dict)
    injection_spec: dict[str, Any] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    replay_hash: str = ""
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _ARM_SCHEMA_ID,
            "schema_version": _ARM_SCHEMA_VERSION,
            "arm_id": self.arm_id,
            "arm_kind": self.arm_kind,
            "release_ref": dict(self.release_ref),
            "budget_contract": dict(self.budget_contract),
            "hint_enabled": self.hint_enabled,
            "selector_spec": dict(self.selector_spec),
            "renderer_spec": dict(self.renderer_spec),
            "binding_spec": dict(self.binding_spec),
            "injection_spec": dict(self.injection_spec),
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
            "replay_hash": self.replay_hash,
            "content_hash": self.content_hash,
        }

    def _replay_payload(self) -> dict[str, Any]:
        """重放 payload——只包含决定重放确定性的字段。"""
        return {
            "arm_kind": self.arm_kind,
            "release_ref": dict(self.release_ref),
            "budget_contract": dict(self.budget_contract),
            "hint_enabled": self.hint_enabled,
            "selector_spec": dict(self.selector_spec),
            "renderer_spec": dict(self.renderer_spec),
            "binding_spec": dict(self.binding_spec),
            "injection_spec": dict(self.injection_spec),
        }

    def compute_replay_hash(self) -> str:
        return hashlib.sha256(
            canonical_json_bytes(self._replay_payload())
        ).hexdigest()

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        d["replay_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def is_replay_hash_valid(self) -> bool:
        return self.replay_hash == self.compute_replay_hash()


def make_arm_payload(
    *,
    arm_id: str,
    arm_kind: str,
    release_ref: dict[str, str] | None = None,
    budget_contract: dict[str, int] | None = None,
    hint_enabled: bool = True,
    selector_spec: dict[str, Any] | None = None,
    renderer_spec: dict[str, Any] | None = None,
    binding_spec: dict[str, Any] | None = None,
    injection_spec: dict[str, Any] | None = None,
    frozen_at: str = "",
) -> ArmPayload:
    arm = ArmPayload(
        arm_id=arm_id,
        arm_kind=arm_kind,
        release_ref=release_ref or {},
        budget_contract=budget_contract or dict(_DEFAULT_BUDGET),
        hint_enabled=hint_enabled,
        selector_spec=selector_spec or {},
        renderer_spec=renderer_spec or {},
        binding_spec=binding_spec or {},
        injection_spec=injection_spec or {},
        frozen_at=frozen_at,
    )
    rh = arm.compute_replay_hash()
    arm = dataclasses.replace(arm, replay_hash=rh)
    return dataclasses.replace(arm, content_hash=arm.compute_content_hash())


@dataclass(frozen=True)
class ArmPayloadVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    arm_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_arm_payload(
    arm: ArmPayload,
    *,
    expected_release_hash: str | None = None,
    reference_budget: dict[str, int] | None = None,
) -> ArmPayloadVerificationResult:
    """验证 ArmPayload。

    参数：
        expected_release_hash: TellStrategyRelease content_hash
        reference_budget: 参考资源预算（用于 distractor 对等检查）
    """
    errors: list[EC] = []
    details: list[str] = []

    d = arm.to_dict()
    if d.get("schema_id") != _ARM_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_ARM_SCHEMA_ID}")

    # arm_kind valid
    if arm.arm_kind not in ST_ARM_KINDS:
        errors.append(EC.ST_ARM_KIND_INVALID)
        details.append(
            f"arm_kind '{arm.arm_kind}' not in {sorted(ST_ARM_KINDS)}"
        )

    # release_ref required
    if not arm.release_ref.get("release_id"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain release_id")
    if not arm.release_ref.get("content_hash"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain content_hash")

    if expected_release_hash is not None:
        if arm.release_ref.get("content_hash") != expected_release_hash:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"release_ref content_hash mismatch: claims "
                f"{arm.release_ref.get('content_hash')}, "
                f"expected {expected_release_hash}"
            )

    # blocker: distractor not equivalent — budget must match reference
    if arm.arm_kind == "DISTRACTOR" and reference_budget is not None:
        if arm.budget_contract != reference_budget:
            errors.append(EC.ST_DISTRACTOR_NOT_EQUIVALENT)
            details.append(
                f"distractor budget {arm.budget_contract} != reference "
                f"{reference_budget} — distractor must have equal resource budget"
            )

    # PROBLEM_ONLY must have hint_enabled=False
    if arm.arm_kind == "PROBLEM_ONLY" and arm.hint_enabled:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append(
            "PROBLEM_ONLY arm must have hint_enabled=False (baseline)"
        )

    # hint-enabled arms must have selector_spec
    if arm.hint_enabled and not arm.selector_spec:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append(
            "hint_enabled=True but selector_spec is empty"
        )

    # replay_hash
    if not arm.replay_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("replay_hash is empty")
    elif arm.replay_hash != arm.compute_replay_hash():
        errors.append(EC.ST_ARM_PAYLOAD_NOT_REPLAYABLE)
        details.append(
            f"replay_hash mismatch: claims {arm.replay_hash}, "
            f"computed {arm.compute_replay_hash()}"
        )

    # content_hash
    if not arm.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif arm.content_hash != arm.compute_content_hash():
        errors.append(EC.ST_ARM_PAYLOAD_NOT_REPLAYABLE)
        details.append(
            f"content_hash mismatch: claims {arm.content_hash}, "
            f"computed {arm.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return ArmPayloadVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        arm_id=arm.arm_id,
    )


def build_arm_payload_set(
    *,
    release_ref: dict[str, str],
    budget_contract: dict[str, int] | None = None,
    frozen_at: str = "",
) -> dict[str, ArmPayload]:
    """构建完整的 arm payload 集合——所有 7 种 arm。

    所有 arm 共享相同的 budget_contract（对等资源预算）。
    PROBLEM_ONLY 为 baseline（hint_enabled=False）。
    """
    budget = budget_contract or dict(_DEFAULT_BUDGET)
    release = release_ref

    # hint-enabled arms share a common selector/renderer/binding/injection spec
    hint_selector_spec: dict[str, Any] = {"kind": "SELECT", "candidates": ["core-1"]}
    hint_renderer_spec: dict[str, Any] = {"kind": "HINT_INSTANCE"}
    hint_binding_spec: dict[str, Any] = {
        "kind": "FULL_BINDING",
        "position": "PRE_TRACE",
        "timing": "BEFORE_SOLVE",
    }
    hint_injection_spec: dict[str, Any] = {
        "position": "PRE_TRACE",
        "policy_id": "inj-policy-1",
    }

    arms: dict[str, ArmPayload] = {}

    # PROBLEM_ONLY — baseline, no hint
    arms["PROBLEM_ONLY"] = make_arm_payload(
        arm_id="arm-problem-only",
        arm_kind="PROBLEM_ONLY",
        release_ref=release,
        budget_contract=budget,
        hint_enabled=False,
        frozen_at=frozen_at,
    )

    # LINEAGE — lineage hint only
    arms["LINEAGE"] = make_arm_payload(
        arm_id="arm-lineage",
        arm_kind="LINEAGE",
        release_ref=release,
        budget_contract=budget,
        hint_enabled=True,
        selector_spec={**hint_selector_spec, "hint_type": "lineage"},
        renderer_spec={**hint_renderer_spec, "render_type": "lineage"},
        binding_spec=hint_binding_spec,
        injection_spec=hint_injection_spec,
        frozen_at=frozen_at,
    )

    # DIRECTION — direction hint only
    arms["DIRECTION"] = make_arm_payload(
        arm_id="arm-direction",
        arm_kind="DIRECTION",
        release_ref=release,
        budget_contract=budget,
        hint_enabled=True,
        selector_spec={**hint_selector_spec, "hint_type": "direction"},
        renderer_spec={**hint_renderer_spec, "render_type": "direction"},
        binding_spec=hint_binding_spec,
        injection_spec=hint_injection_spec,
        frozen_at=frozen_at,
    )

    # LINEAGE_DIRECTION — lineage + direction
    arms["LINEAGE_DIRECTION"] = make_arm_payload(
        arm_id="arm-lineage-direction",
        arm_kind="LINEAGE_DIRECTION",
        release_ref=release,
        budget_contract=budget,
        hint_enabled=True,
        selector_spec={**hint_selector_spec, "hint_type": "lineage+direction"},
        renderer_spec={**hint_renderer_spec, "render_type": "lineage+direction"},
        binding_spec=hint_binding_spec,
        injection_spec=hint_injection_spec,
        frozen_at=frozen_at,
    )

    # DISTRACTOR — distractor hint (must have equal budget)
    arms["DISTRACTOR"] = make_arm_payload(
        arm_id="arm-distractor",
        arm_kind="DISTRACTOR",
        release_ref=release,
        budget_contract=budget,
        hint_enabled=True,
        selector_spec={**hint_selector_spec, "hint_type": "distractor"},
        renderer_spec={**hint_renderer_spec, "render_type": "distractor"},
        binding_spec=hint_binding_spec,
        injection_spec=hint_injection_spec,
        frozen_at=frozen_at,
    )

    # OPERATION_CRITIC — operation/critic hint
    arms["OPERATION_CRITIC"] = make_arm_payload(
        arm_id="arm-operation-critic",
        arm_kind="OPERATION_CRITIC",
        release_ref=release,
        budget_contract=budget,
        hint_enabled=True,
        selector_spec={**hint_selector_spec, "hint_type": "operation_critic"},
        renderer_spec={**hint_renderer_spec, "render_type": "operation_critic"},
        binding_spec=hint_binding_spec,
        injection_spec=hint_injection_spec,
        frozen_at=frozen_at,
    )

    # POSITION_NEUTRAL — position-neutral hint
    arms["POSITION_NEUTRAL"] = make_arm_payload(
        arm_id="arm-position-neutral",
        arm_kind="POSITION_NEUTRAL",
        release_ref=release,
        budget_contract=budget,
        hint_enabled=True,
        selector_spec={**hint_selector_spec, "hint_type": "position_neutral"},
        renderer_spec={**hint_renderer_spec, "render_type": "position_neutral"},
        binding_spec={**hint_binding_spec, "position": "MID_TRACE", "timing": "MID_SOLVE"},
        injection_spec={**hint_injection_spec, "position": "MID_TRACE"},
        frozen_at=frozen_at,
    )

    return arms
