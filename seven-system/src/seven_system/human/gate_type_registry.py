"""GateTypeRegistry — gate type → 要求的角色/签名数/职责分离策略。

每种 gate type 冻结：
- gate_type：唯一标识
- required_roles：执行该 gate 至少需要一个什么角色的 actor
- required_signatures：需要几个不同 actor 的签名才封口
- allow_model_role：ModelRole 是否可以参与（多数 gate 禁止 ModelRole 自批）
- separation_policy：职责分离策略名

职责分离策略：
- "CREATOR_CANNOT_APPROVE"：创建 payload 的 actor 不能批准同一 payload
- "INDEPENDENT_REVIEW"：审查者必须与创建者无 context/model 关系
- "NONE"：无额外分离要求（少数内部 gate）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    HUMAN_GATE_ROLES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


# 职责分离策略枚举
SEPARATION_POLICIES: frozenset[str] = frozenset(
    {"CREATOR_CANNOT_APPROVE", "INDEPENDENT_REVIEW", "NONE"}
)


@dataclass(frozen=True)
class GateTypeSpec:
    """单个 gate type 的规格。不可变。"""

    gate_type: str
    required_roles: frozenset[str]
    required_signatures: int
    allow_model_role: bool
    separation_policy: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "gate_type": self.gate_type,
            "required_roles": sorted(self.required_roles),
            "required_signatures": self.required_signatures,
            "allow_model_role": self.allow_model_role,
            "separation_policy": self.separation_policy,
        }


class GateTypeRegistry:
    """GateTypeRegistry — gate type 注册表。

    维护 gate_type → GateTypeSpec 映射。
    支持注册、查询、角色检查。
    """

    def __init__(self) -> None:
        self._types: dict[str, GateTypeSpec] = {}

    def register(self, spec: GateTypeSpec) -> VerificationResult:
        """注册一个 gate type。

        检查：
        - gate_type 非空且唯一
        - required_roles 都是合法角色
        - required_signatures >= 1
        - separation_policy 在合法枚举中
        """
        errors: list[EC] = []
        details: list[str] = []

        if not spec.gate_type:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("gate_type must not be empty")

        invalid_roles = set(spec.required_roles) - HUMAN_GATE_ROLES
        if invalid_roles:
            errors.append(EC.GATE_REQUIRED_ROLE_MISSING)
            details.append(f"unknown required_roles: {invalid_roles}")

        if spec.required_signatures < 1:
            errors.append(EC.GATE_REQUIRED_SIGNATURES_NOT_MET)
            details.append("required_signatures must be >= 1")

        if spec.separation_policy not in SEPARATION_POLICIES:
            errors.append(EC.GATE_DUTY_CONFLICT)
            details.append(f"unknown separation_policy: {spec.separation_policy}")

        if spec.gate_type and spec.gate_type in self._types:
            errors.append(EC.GATE_TYPE_UNKNOWN)
            details.append(f"gate_type {spec.gate_type} already registered")

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        self._types[spec.gate_type] = spec
        return VerificationResult(verdict="PASS")

    def get(self, gate_type: str) -> GateTypeSpec | None:
        """获取 gate type 规格。"""
        return self._types.get(gate_type)

    def check_gate_type(self, gate_type: str) -> VerificationResult:
        """检查 gate type 是否存在。"""
        if gate_type not in self._types:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.GATE_TYPE_UNKNOWN],
                details=[f"unknown gate_type: {gate_type}"],
            )
        return VerificationResult(verdict="PASS")

    @property
    def size(self) -> int:
        return len(self._types)

    def list_types(self) -> list[GateTypeSpec]:
        return list(self._types.values())
