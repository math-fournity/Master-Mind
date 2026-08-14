"""AuthoringRoleRouter — 角色路由器。

来自 docs/implementation/09-phase-pipeline-p0-p9.md：

"Each role can be executed by any adapter that passes that role's capability gate.
Role routing and profile are pre-frozen."

角色路由：question_architect / adversarial_editor / math_verifier → 合格的 adapter profile。
不合格角色 = BLOCK（QA_UNQUALIFIED_ROLE_ROUTED）。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    QA_AUTHORING_ROLES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


@dataclass
class RoleRoutingEntry:
    """单个角色 → adapter profile 的冻结路由条目。"""

    role_type_id: str
    adapter_kind: str
    profile_ref_and_hash: dict[str, str]
    qualified: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "role_type_id": self.role_type_id,
            "adapter_kind": self.adapter_kind,
            "profile_ref_and_hash": dict(self.profile_ref_and_hash),
            "qualified": self.qualified,
        }


@dataclass
class AuthoringRoleRouter:
    """AuthoringRoleRouter — 预冻结的角色路由器。

    维护 role_type_id → RoleRoutingEntry 映射。
    路由前检查角色是否在 QA_AUTHORING_ROLES 中。
    不合格角色 = BLOCK。
    """

    routings: dict[str, RoleRoutingEntry] = field(default_factory=dict)
    frozen: bool = False

    def register(self, entry: RoleRoutingEntry) -> VerificationResult:
        """注册一个角色路由条目。冻结后不可修改。"""
        if self.frozen:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_ROLE_ROUTING_NOT_FROZEN],
                details=["router is frozen, cannot register new routing"],
            )
        if entry.role_type_id not in QA_AUTHORING_ROLES:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_UNQUALIFIED_ROLE_ROUTED],
                details=[f"role_type_id {entry.role_type_id!r} not in {QA_AUTHORING_ROLES}"],
            )
        if entry.role_type_id in self.routings:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_ROLE_ROUTING_NOT_FROZEN],
                details=[f"role_type_id {entry.role_type_id} already routed"],
            )
        self.routings[entry.role_type_id] = entry
        return VerificationResult(verdict="PASS")

    def freeze(self) -> VerificationResult:
        """冻结路由表。冻结后不可修改。"""
        # 检查所有出题角色都有路由
        missing = QA_AUTHORING_ROLES - set(self.routings.keys())
        if missing:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_UNQUALIFIED_ROLE_ROUTED],
                details=[f"missing routing for roles: {missing}"],
            )
        # 检查所有路由都合格
        for role_id, entry in self.routings.items():
            if not entry.qualified:
                return VerificationResult(
                    verdict="FAIL",
                    error_codes=[EC.QA_UNQUALIFIED_ROLE_ROUTED],
                    details=[f"role {role_id} routed to unqualified adapter"],
                )
        self.frozen = True
        return VerificationResult(verdict="PASS")

    def route(self, role_type_id: str) -> VerificationResult:
        """路由角色到 adapter profile。

        检查：
        1. 路由表已冻结
        2. 角色在 QA_AUTHORING_ROLES 中
        3. 角色有路由条目
        4. 路由条目合格
        """
        if not self.frozen:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_ROLE_ROUTING_NOT_FROZEN],
                details=["router is not frozen"],
            )
        if role_type_id not in QA_AUTHORING_ROLES:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_UNQUALIFIED_ROLE_ROUTED],
                details=[f"role_type_id {role_type_id!r} not in {QA_AUTHORING_ROLES}"],
            )
        entry = self.routings.get(role_type_id)
        if entry is None:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_UNQUALIFIED_ROLE_ROUTED],
                details=[f"no routing for role_type_id {role_type_id}"],
            )
        if not entry.qualified:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_UNQUALIFIED_ROLE_ROUTED],
                details=[f"role {role_type_id} routed to unqualified adapter"],
            )
        return VerificationResult(verdict="PASS")

    def get_routing(self, role_type_id: str) -> RoleRoutingEntry | None:
        return self.routings.get(role_type_id)
