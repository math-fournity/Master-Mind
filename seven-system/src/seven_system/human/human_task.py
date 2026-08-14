"""HumanTask / HumanTaskPort — 人工任务创建、分配、完成。

HumanTask 包含：
- task_id：唯一标识
- gate_type：关联的 gate type
- payload_ref + payload_hash：被审查的 payload 引用和 hash
- allowed_view：允许审查者看到的 view
- deadline：截止时间
- eligible_roles：哪些角色可以接这个任务
- separation_policy：职责分离策略
- required_signatures：需要几个签名
- nonce：唯一、不可预测（每个 payload version 唯一）
- status：OPEN / ASSIGNED / COMPLETED / EXPIRED / CANCELLED
- assigned_actor_id：被分配的 actor（如有）
- creator_actor_id：创建任务的 actor

HumanTaskPort 是协议接口：
- create_task：创建任务
- assign_task：分配任务给 actor
- complete_task：标记任务完成（携带 GateDecision）
- get_task：查询任务

FakeHumanTaskPort 是纯内存实现，用于 SIDE_EFFECT_FREE 测试。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Protocol

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    GATE_VERIFICATION_STATUSES,
    HUMAN_GATE_ROLES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..contracts.security_contract import _check_canonical_utc


_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_ID_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9._:@+-]{0,254}[A-Za-z0-9])?$")
_NONCE_RE = re.compile(r"^[A-Za-z0-9._:-]{16,128}$")

# HumanTask 状态枚举
TASK_STATUSES: frozenset[str] = frozenset(
    {"OPEN", "ASSIGNED", "COMPLETED", "EXPIRED", "CANCELLED"}
)


@dataclass
class HumanTask:
    """HumanTask 数据对象。可变（状态会变化）。"""

    task_id: str
    gate_type: str
    payload_ref: str
    payload_hash: str
    allowed_view: str
    deadline: str
    eligible_roles: frozenset[str]
    separation_policy: str
    required_signatures: int
    nonce: str
    creator_actor_id: str
    status: str = "OPEN"
    assigned_actor_id: str | None = None
    completed_decisions: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "gate_type": self.gate_type,
            "payload_ref": self.payload_ref,
            "payload_hash": self.payload_hash,
            "allowed_view": self.allowed_view,
            "deadline": self.deadline,
            "eligible_roles": sorted(self.eligible_roles),
            "separation_policy": self.separation_policy,
            "required_signatures": self.required_signatures,
            "nonce": self.nonce,
            "creator_actor_id": self.creator_actor_id,
            "status": self.status,
            "assigned_actor_id": self.assigned_actor_id,
            "completed_decisions": list(self.completed_decisions),
        }


class HumanTaskPort(Protocol):
    """HumanTaskPort 协议接口。

    状态服务和 HumanGateService 消费此接口，不直接接触具体实现。
    """

    def create_task(
        self,
        *,
        task_id: str,
        gate_type: str,
        payload_ref: str,
        payload_hash: str,
        allowed_view: str,
        deadline: str,
        eligible_roles: frozenset[str],
        separation_policy: str,
        required_signatures: int,
        nonce: str,
        creator_actor_id: str,
    ) -> VerificationResult:
        ...

    def assign_task(
        self,
        task_id: str,
        actor_id: str,
    ) -> VerificationResult:
        ...

    def complete_task(
        self,
        task_id: str,
        decision: dict[str, Any],
    ) -> VerificationResult:
        ...

    def get_task(self, task_id: str) -> HumanTask | None:
        ...


class FakeHumanTaskPort:
    """FakeHumanTaskPort — 纯内存 HumanTaskPort 实现。

    SIDE_EFFECT_FREE：不接触真实 DB/D 盘。
    维护 task_id → HumanTask 映射。
    """

    def __init__(self) -> None:
        self._tasks: dict[str, HumanTask] = {}

    def create_task(
        self,
        *,
        task_id: str,
        gate_type: str,
        payload_ref: str,
        payload_hash: str,
        allowed_view: str,
        deadline: str,
        eligible_roles: frozenset[str],
        separation_policy: str,
        required_signatures: int,
        nonce: str,
        creator_actor_id: str,
    ) -> VerificationResult:
        """创建一个 HumanTask。

        检查：
        - task_id 非空且唯一
        - gate_type 非空
        - payload_ref 非空、payload_hash 是合法 sha256
        - deadline 为 canonical UTC
        - eligible_roles 都是合法角色
        - required_signatures >= 1
        - nonce 格式合法
        - creator_actor_id 非空
        """
        errors: list[EC] = []
        details: list[str] = []

        if not task_id or not _ID_RE.match(task_id):
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"invalid task_id: {task_id!r}")

        if not gate_type:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("gate_type must not be empty")

        if not payload_ref:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("payload_ref must not be empty")

        if not isinstance(payload_hash, str) or not _HASH_RE.match(payload_hash):
            errors.append(EC.GATE_PAYLOAD_HASH_MISMATCH)
            details.append(f"invalid payload_hash: {payload_hash!r}")

        if not _check_canonical_utc(deadline):
            errors.append(EC.TIME_NOT_CANONICAL_UTC)
            details.append(f"deadline not canonical UTC: {deadline!r}")

        invalid_roles = set(eligible_roles) - HUMAN_GATE_ROLES
        if invalid_roles:
            errors.append(EC.ACTOR_ROLE_MISSING)
            details.append(f"unknown eligible_roles: {invalid_roles}")

        if required_signatures < 1:
            errors.append(EC.GATE_REQUIRED_SIGNATURES_NOT_MET)
            details.append("required_signatures must be >= 1")

        if not isinstance(nonce, str) or not _NONCE_RE.match(nonce):
            errors.append(EC.GATE_NONCE_INVALID)
            details.append(f"invalid nonce: {nonce!r}")

        if not creator_actor_id:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("creator_actor_id must not be empty")

        if task_id in self._tasks:
            errors.append(EC.GATE_REPLAY_DETECTED)
            details.append(f"task {task_id} already exists")

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        task = HumanTask(
            task_id=task_id,
            gate_type=gate_type,
            payload_ref=payload_ref,
            payload_hash=payload_hash,
            allowed_view=allowed_view,
            deadline=deadline,
            eligible_roles=frozenset(eligible_roles),
            separation_policy=separation_policy,
            required_signatures=required_signatures,
            nonce=nonce,
            creator_actor_id=creator_actor_id,
        )
        self._tasks[task_id] = task
        return VerificationResult(verdict="PASS")

    def assign_task(
        self,
        task_id: str,
        actor_id: str,
    ) -> VerificationResult:
        """分配任务给 actor。

        检查：
        - task 存在且状态为 OPEN
        - actor_id 非空
        """
        errors: list[EC] = []
        details: list[str] = []

        task = self._tasks.get(task_id)
        if task is None:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"task {task_id} not found")
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        if task.status != "OPEN":
            errors.append(EC.STATE_COMMAND_REJECTED)
            details.append(f"task {task_id} is not OPEN (status={task.status})")

        if not actor_id:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("actor_id must not be empty")

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        task.status = "ASSIGNED"
        task.assigned_actor_id = actor_id
        return VerificationResult(verdict="PASS")

    def complete_task(
        self,
        task_id: str,
        decision: dict[str, Any],
    ) -> VerificationResult:
        """标记任务完成（携带 GateDecision）。

        检查：
        - task 存在
        - decision.task_id == task_id
        - decision.payload_hash == task.payload_hash
        - task 状态为 ASSIGNED 或 OPEN
        """
        errors: list[EC] = []
        details: list[str] = []

        task = self._tasks.get(task_id)
        if task is None:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"task {task_id} not found")
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        if task.status in ("COMPLETED", "EXPIRED", "CANCELLED"):
            errors.append(EC.STATE_COMMAND_REJECTED)
            details.append(f"task {task_id} already {task.status}")
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        dec_task_id = decision.get("task_id", "")
        if dec_task_id != task_id:
            errors.append(EC.GATE_PAYLOAD_HASH_MISMATCH)
            details.append(f"decision.task_id {dec_task_id} != task_id {task_id}")

        dec_payload_hash = decision.get("payload_hash", "")
        if dec_payload_hash != task.payload_hash:
            errors.append(EC.GATE_PAYLOAD_HASH_MISMATCH)
            details.append(
                f"decision.payload_hash {dec_payload_hash} != task.payload_hash {task.payload_hash}"
            )

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        task.completed_decisions.append(dict(decision))
        task.status = "COMPLETED"
        return VerificationResult(verdict="PASS")

    def get_task(self, task_id: str) -> HumanTask | None:
        return self._tasks.get(task_id)

    @property
    def size(self) -> int:
        return len(self._tasks)

    def list_tasks(self) -> list[HumanTask]:
        return list(self._tasks.values())
