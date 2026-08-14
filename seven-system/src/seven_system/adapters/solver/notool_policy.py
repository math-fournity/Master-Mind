"""NoToolPolicy — v1 只允许 NoTool 的工具策略（WP-SV1）。

v1 只允许 NO_TOOL policy。任何 tool event 出现在 trajectory 中 = FAIL。

NoToolPolicy 记录：
- policy_kind：NO_TOOL
- declared_tool_events：声明的 tool events（v1 必须为空）
- policy_hash：策略 hash

验证器检查：
1. policy_kind == "NO_TOOL"
2. declared_tool_events 为空
3. trajectory 中无 tool events（check_trajectory_for_tool_events）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    SV_TOOL_POLICY_KINDS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_POLICY_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-policy_hash-null)"


@dataclass(frozen=True)
class NoToolPolicy:
    """NoToolPolicy — v1 只允许 NoTool 的工具策略。"""

    policy_kind: str
    declared_tool_events: list[dict[str, Any]]
    policy_hash_algorithm: str
    policy_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "policy_kind": self.policy_kind,
            "declared_tool_events": [dict(e) for e in self.declared_tool_events],
            "policy_hash_algorithm": self.policy_hash_algorithm,
            "policy_hash": self.policy_hash,
        }


def build_notool_policy(
    *,
    declared_tool_events: list[dict[str, Any]] | None = None,
) -> NoToolPolicy:
    """构建 NoToolPolicy，自动计算 policy_hash。"""
    events = [dict(e) for e in declared_tool_events] if declared_tool_events else []

    obj = {
        "policy_kind": "NO_TOOL",
        "declared_tool_events": events,
        "policy_hash_algorithm": _POLICY_HASH_ALGORITHM,
        "policy_hash": None,
    }
    policy_hash = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

    return NoToolPolicy(
        policy_kind="NO_TOOL",
        declared_tool_events=events,
        policy_hash_algorithm=_POLICY_HASH_ALGORITHM,
        policy_hash=policy_hash,
    )


def verify_notool_policy(
    policy: NoToolPolicy | dict[str, Any],
) -> VerificationResult:
    """验证 NoToolPolicy 的 schema + semantic 合法性。

    检查（blocker: NoTool policy violation → FAIL）：
    1. policy_kind == "NO_TOOL"
    2. declared_tool_events 为空（v1 不允许任何 tool events）
    3. policy_hash 正确
    """
    if isinstance(policy, NoToolPolicy):
        policy_dict = policy.to_dict()
    else:
        policy_dict = policy

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. policy_kind
    policy_kind = policy_dict.get("policy_kind", "")
    if policy_kind not in SV_TOOL_POLICY_KINDS:
        _err(EC.SV_TOOL_POLICY_KIND_INVALID,
             f"policy_kind {policy_kind!r} not in SV_TOOL_POLICY_KINDS")
    elif policy_kind != "NO_TOOL":
        _err(EC.SV_NOTOOL_VIOLATION,
             f"v1 only allows NO_TOOL, got {policy_kind!r}")

    # 2. declared_tool_events must be empty (blocker: NoTool violation)
    events = policy_dict.get("declared_tool_events", [])
    if isinstance(events, list) and len(events) > 0:
        _err(EC.SV_NOTOOL_VIOLATION,
             f"NO_TOOL policy must have zero declared tool events, "
             f"got {len(events)}")

    # 3. policy_hash
    if policy_dict.get("policy_hash_algorithm") != _POLICY_HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"unexpected policy_hash_algorithm: "
             f"{policy_dict.get('policy_hash_algorithm')}")
    obj_for_hash = dict(policy_dict)
    obj_for_hash["policy_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if policy_dict.get("policy_hash") != computed_hash:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"policy_hash mismatch: expected {computed_hash}, "
             f"got {policy_dict.get('policy_hash')}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_trajectory_for_tool_events(
    trajectory: list[dict[str, Any]] | dict[str, Any],
) -> VerificationResult:
    """检查 trajectory 中是否有 tool events（blocker: tool event detected → FAIL）。

    trajectory 可以是 step 列表，或包含 steps 列表的 dict。
    每个 step 有 step_type 字段。step_type == "tool" 即 tool event。
    """
    errors: list[EC] = []
    details: list[str] = []

    if isinstance(trajectory, dict):
        steps = trajectory.get("steps", [])
    elif isinstance(trajectory, list):
        steps = trajectory
    else:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.SV_TOOL_EVENT_DETECTED],
            details=[f"trajectory must be a list or dict, got {type(trajectory).__name__}"],
        )

    tool_events: list[int] = []
    if isinstance(steps, list):
        for i, step in enumerate(steps):
            if isinstance(step, dict):
                step_type = step.get("step_type", "")
                if step_type == "tool":
                    tool_events.append(i)

    if tool_events:
        errors.append(EC.SV_TOOL_EVENT_DETECTED)
        details.append(
            f"tool events detected at step indices: {tool_events}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
