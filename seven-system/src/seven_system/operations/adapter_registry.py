"""AdapterRegistry — R6: 真实但默认禁用的 adapter/storage/runtime 路径。

R6 整改：审计要求 adapter/storage/runtime 路径真实存在但默认禁用。
本注册表管理所有副作用端口的启用状态：
- VLT0: CompletionArtifactStore（D 盘 CAS）
- DB: ArangoDB connection
- RT: Redis projection
- Solver: TargetSolverPort（solver_harness）
- ModelRole: Codex/DevinCli adapters

默认全部 DISABLED。只有经过 HumanGate + LiveRunPermit 授权后才能 enable。
任何在 disabled 状态下的调用必须 fail-closed。

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB/D 盘/模型。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import VerificationErrorCode as EC


# 所有需要管理的副作用端口
SIDE_EFFECT_PORTS: frozenset[str] = frozenset({
    "VLT0_CAS",
    "DB_ARANGO",
    "RT_REDIS",
    "SOLVER_HARNESS",
    "MODEL_ROLE_CODEX",
    "MODEL_ROLE_DEVIN",
})


@dataclass
class AdapterRegistry:
    """AdapterRegistry — 副作用端口启用状态注册表。

    所有端口默认 DISABLED。
    只有经过 HumanGate + LiveRunPermit 授权后才能 enable。
    """

    _enabled: set[str] = field(default_factory=set)
    _enable_authorizations: dict[str, str] = field(default_factory=dict)

    def is_enabled(self, port_id: str) -> bool:
        """检查端口是否已启用。"""
        return port_id in self._enabled

    def enable(self, port_id: str, *, authorization_ref: str) -> tuple[bool, list[EC], list[str]]:
        """启用一个副作用端口。

        需要 authorization_ref（HumanGate decision + LiveRunPermit 的引用）。
        """
        errors: list[EC] = []
        details: list[str] = []

        if port_id not in SIDE_EFFECT_PORTS:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown side-effect port: {port_id}")
            return False, errors, details

        if not authorization_ref:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("authorization_ref is required to enable a side-effect port")
            return False, errors, details

        self._enabled.add(port_id)
        self._enable_authorizations[port_id] = authorization_ref
        return True, [], []

    def disable(self, port_id: str) -> tuple[bool, list[EC], list[str]]:
        """禁用一个副作用端口。"""
        errors: list[EC] = []
        details: list[str] = []

        if port_id not in SIDE_EFFECT_PORTS:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown side-effect port: {port_id}")
            return False, errors, details

        self._enabled.discard(port_id)
        self._enable_authorizations.pop(port_id, None)
        return True, [], []

    def check_enabled(self, port_id: str) -> tuple[bool, list[EC], list[str]]:
        """检查端口是否已启用，未启用则返回错误。

        所有副作用操作调用前必须调用此方法。
        """
        errors: list[EC] = []
        details: list[str] = []

        if port_id not in SIDE_EFFECT_PORTS:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown side-effect port: {port_id}")
            return False, errors, details

        if port_id not in self._enabled:
            errors.append(EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED)
            details.append(
                f"side-effect port {port_id} is DISABLED — "
                f"must be enabled via HumanGate + LiveRunPermit before use"
            )
            return False, errors, details

        return True, [], []

    def enable_authorization(self, port_id: str) -> str | None:
        """获取端口的启用授权引用。"""
        return self._enable_authorizations.get(port_id)

    def all_disabled(self) -> bool:
        """检查所有端口是否都已禁用（初始状态）。"""
        return len(self._enabled) == 0

    def enabled_ports(self) -> frozenset[str]:
        """返回所有已启用的端口。"""
        return frozenset(self._enabled)
