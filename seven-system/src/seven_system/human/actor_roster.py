"""ActorRoster — 谁可以做什么。

ActorRoster 是 HumanGate 的授权基础。每个 actor 有：
- actor_id：唯一标识
- actor_type：HUMAN / MODEL_ROLE / SERVICE
- roles：该 actor 持有的角色集合
- active：是否当前活跃

Gate 决定验证时，HumanGateService 查 roster 确认 actor 存在、活跃、
持有 gate type 要求的角色。ModelRole 不能自我批准——
这是职责分离的硬约束，在 roster 层和 gate 层双重检查。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    ACTOR_TYPES,
    HUMAN_GATE_ROLES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


@dataclass(frozen=True)
class ActorRecord:
    """单个 actor 的注册记录。不可变。"""

    actor_id: str
    actor_type: str
    roles: frozenset[str]
    active: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "actor_id": self.actor_id,
            "actor_type": self.actor_type,
            "roles": sorted(self.roles),
            "active": self.active,
        }


class ActorRoster:
    """ActorRoster — actor 注册表。

    维护 actor_id → ActorRecord 映射。
    支持注册、停用、角色检查。
    所有验证返回 VerificationResult，不抛异常。
    """

    def __init__(self) -> None:
        self._actors: dict[str, ActorRecord] = {}

    def register(self, record: ActorRecord) -> VerificationResult:
        """注册一个 actor。

        检查：
        - actor_id 非空且唯一
        - actor_type 在合法枚举中
        - roles 都是合法角色
        - 不覆盖已有 actor（除非先 revoke）
        """
        errors: list[EC] = []
        details: list[str] = []

        if not record.actor_id:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("actor_id must not be empty")
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        if record.actor_type not in ACTOR_TYPES:
            errors.append(EC.ACTOR_TYPE_INVALID)
            details.append(f"unknown actor_type: {record.actor_type}")

        invalid_roles = set(record.roles) - HUMAN_GATE_ROLES
        if invalid_roles:
            errors.append(EC.ACTOR_ROLE_MISSING)
            details.append(f"unknown roles: {invalid_roles}")

        if record.actor_id in self._actors:
            errors.append(EC.ACTOR_NOT_IN_ROSTER)
            details.append(f"actor {record.actor_id} already registered")

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        self._actors[record.actor_id] = record
        return VerificationResult(verdict="PASS")

    def deactivate(self, actor_id: str) -> VerificationResult:
        """停用一个 actor（不删除，标记 active=False）。"""
        if actor_id not in self._actors:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.ACTOR_NOT_IN_ROSTER],
                details=[f"actor {actor_id} not in roster"],
            )
        old = self._actors[actor_id]
        self._actors[actor_id] = ActorRecord(
            actor_id=old.actor_id,
            actor_type=old.actor_type,
            roles=old.roles,
            active=False,
        )
        return VerificationResult(verdict="PASS")

    def get(self, actor_id: str) -> ActorRecord | None:
        """获取 actor 记录。"""
        return self._actors.get(actor_id)

    def check_actor(
        self,
        actor_id: str,
        *,
        required_roles: frozenset[str] | None = None,
    ) -> VerificationResult:
        """检查 actor 是否存在、活跃、持有要求的角色。

        这是 HumanGateService 在验证 GateDecision 时调用的核心检查。
        """
        errors: list[EC] = []
        details: list[str] = []

        record = self._actors.get(actor_id)
        if record is None:
            errors.append(EC.ACTOR_NOT_IN_ROSTER)
            details.append(f"actor {actor_id} not in roster")
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        if not record.active:
            errors.append(EC.ACTOR_INACTIVE)
            details.append(f"actor {actor_id} is not active")

        if required_roles:
            missing = required_roles - record.roles
            if missing:
                errors.append(EC.GATE_REQUIRED_ROLE_MISSING)
                details.append(
                    f"actor {actor_id} missing required roles: {missing}"
                )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)

    def is_model_role(self, actor_id: str) -> bool:
        """检查 actor 是否为 MODEL_ROLE 类型。"""
        record = self._actors.get(actor_id)
        return record is not None and record.actor_type == "MODEL_ROLE"

    @property
    def size(self) -> int:
        return len(self._actors)

    def list_actors(self) -> list[ActorRecord]:
        return list(self._actors.values())
