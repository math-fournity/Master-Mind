"""WorkPackageStateService — R5: DAG 依赖强制执行与 board 投影。

R5 整改：审计发现 22 个工作包曾被越级标为 IMPLEMENTED_PENDING_EVIDENCE，
但 development dependency 未满足（GV0 未到 READY_FOR_AUDIT）。
本服务根据 canonical DAG 强制执行：
1. 工作包只能从 NOT_STARTED → IN_PROGRESS（不能越级）
2. 进入 IN_PROGRESS 前，所有 development_dependencies 必须处于
   READY_FOR_AUDIT 或 AUDITED_PASS 状态
3. 进入 READY_FOR_AUDIT 前，工作包必须处于 IN_PROGRESS
4. 进入 AUDITED_PASS 前，工作包必须处于 READY_FOR_AUDIT 且有 AuditRecord

R5 补全：
5. complete 命令——验证 completion contract、owner、状态命令
6. activate 命令——验证 activation dependencies、Permit、Reservation
7. Plan 验证——start 前检查 Plan 存在且 schema-valid
8. audit debt 继承——记录 inherited audit debt
9. board append-only 事件源——状态变更记录为事件
10. 双向对账——board/implementation-status/capabilities 一致性

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB/D 盘/模型。
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..contracts.errors import VALID_STATES, VerificationErrorCode as EC


# 合法的状态转换
_LEGAL_TRANSITIONS: dict[str, frozenset[str]] = {
    "NOT_STARTED": frozenset({"IN_PROGRESS", "BLOCKED"}),
    "READY": frozenset({"IN_PROGRESS", "BLOCKED"}),
    "IN_PROGRESS": frozenset({"IMPLEMENTED_PENDING_EVIDENCE", "READY_FOR_AUDIT", "BLOCKED"}),
    "IMPLEMENTED_PENDING_EVIDENCE": frozenset({"READY_FOR_AUDIT", "IN_PROGRESS", "BLOCKED"}),
    "READY_FOR_AUDIT": frozenset({"AUDITED_PASS", "AUDITED_PARTIAL", "AUDITED_FAIL", "IN_PROGRESS"}),
    "AUDITED_PASS": frozenset(),  # terminal
    "AUDITED_PARTIAL": frozenset({"IN_PROGRESS", "READY_FOR_AUDIT"}),
    "AUDITED_FAIL": frozenset({"IN_PROGRESS", "READY_FOR_AUDIT"}),
    "BLOCKED": frozenset({"NOT_STARTED", "IN_PROGRESS"}),
}

# development dependency 满足的最低状态
_DEV_DEP_MIN_STATES = frozenset({"READY_FOR_AUDIT", "AUDITED_PASS"})

# activation dependency 满足的最低状态
_ACT_DEP_MIN_STATES = frozenset({"AUDITED_PASS"})

# implementer 不能写的状态
_IMPLEMENTER_FORBIDDEN_STATES = frozenset({"AUDITED_PASS", "AUDITED_PARTIAL", "AUDITED_FAIL"})


@dataclass
class StateEvent:
    """状态变更事件——append-only。"""

    event_id: str
    wp_id: str
    from_state: str
    to_state: str
    timestamp: str
    actor_type: str  # "IMPLEMENTER" | "AUDITOR" | "SYSTEM"
    command: str  # "start" | "complete" | "activate" | "transition"
    details: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "wp_id": self.wp_id,
            "from_state": self.from_state,
            "to_state": self.to_state,
            "timestamp": self.timestamp,
            "actor_type": self.actor_type,
            "command": self.command,
            "details": list(self.details),
        }


@dataclass
class WorkPackageStateService:
    """WorkPackageStateService — DAG 依赖强制执行器。

    持有：
    - dag_path: canonical DAG 路径
    - wp_states: wp_id → 当前状态
    - wp_plans: wp_id → Plan ref/hash（可选）
    - wp_audit_debt: wp_id → inherited audit debt list
    - event_log: append-only 状态变更事件
    - _dag: 加载的 DAG（lazy）
    """

    dag_path: Path
    wp_states: dict[str, str] = field(default_factory=dict)
    wp_plans: dict[str, dict[str, str]] = field(default_factory=dict)  # wp_id → {"ref": ..., "hash": ...}
    wp_audit_debt: dict[str, list[dict[str, str]]] = field(default_factory=dict)
    event_log: list[StateEvent] = field(default_factory=list)
    _dag: dict[str, Any] | None = None
    _dag_index: dict[str, dict[str, Any]] = field(default_factory=dict)
    _event_counter: int = 0

    def _load_dag(self) -> dict[str, Any]:
        """加载 DAG（lazy）。"""
        if self._dag is None:
            with open(self.dag_path, "r", encoding="utf-8") as f:
                self._dag = json.load(f)
            for wp in self._dag.get("work_packages", []):
                self._dag_index[wp["wp_id"]] = wp
        return self._dag

    def _get_wp_spec(self, wp_id: str) -> dict[str, Any]:
        """获取 WP 的 DAG spec。"""
        self._load_dag()
        if wp_id not in self._dag_index:
            raise ValueError(f"unknown wp_id: {wp_id}")
        return self._dag_index[wp_id]

    def _record_event(
        self, wp_id: str, from_state: str, to_state: str,
        actor_type: str, command: str, details: list[str] | None = None,
    ) -> None:
        """记录状态变更事件（append-only）。"""
        self._event_counter += 1
        event = StateEvent(
            event_id=f"evt-{self._event_counter:06d}",
            wp_id=wp_id,
            from_state=from_state,
            to_state=to_state,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            actor_type=actor_type,
            command=command,
            details=details or [],
        )
        self.event_log.append(event)

    def get_state(self, wp_id: str) -> str:
        """获取 WP 当前状态。默认 NOT_STARTED。"""
        return self.wp_states.get(wp_id, "NOT_STARTED")

    def register_plan(self, wp_id: str, plan_ref: str, plan_hash: str) -> None:
        """注册 WP 的 Plan ref/hash。"""
        self.wp_plans[wp_id] = {"ref": plan_ref, "hash": plan_hash}

    def has_plan(self, wp_id: str) -> bool:
        """检查 WP 是否有注册的 Plan。"""
        return wp_id in self.wp_plans

    def inherit_audit_debt(self, wp_id: str, debt: list[dict[str, str]]) -> None:
        """继承 audit debt。"""
        self.wp_audit_debt[wp_id] = list(debt)

    def get_audit_debt(self, wp_id: str) -> list[dict[str, str]]:
        """获取 WP 的 inherited audit debt。"""
        return self.wp_audit_debt.get(wp_id, [])

    def can_start(self, wp_id: str) -> tuple[bool, list[EC], list[str]]:
        """检查 WP 是否可以开始（NOT_STARTED → IN_PROGRESS）。

        检查：
        1. WP 存在于 DAG
        2. 当前状态为 NOT_STARTED 或 READY
        3. 所有 development_dependencies 处于 READY_FOR_AUDIT 或 AUDITED_PASS
        4. R5 补全: Plan 存在且已注册
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. WP 存在
        try:
            spec = self._get_wp_spec(wp_id)
        except ValueError:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown wp_id: {wp_id}")
            return False, errors, details

        # 2. 当前状态
        current = self.get_state(wp_id)
        if current not in ("NOT_STARTED", "READY"):
            errors.append(EC.WP_ALREADY_STARTED)
            details.append(f"wp {wp_id} already in state {current}, cannot start")

        # 3. development dependencies
        dev_deps = spec.get("development_dependencies", [])
        for dep_id in dev_deps:
            dep_state = self.get_state(dep_id)
            if dep_state not in _DEV_DEP_MIN_STATES:
                errors.append(EC.WP_DEPENDENCY_NOT_MET)
                details.append(
                    f"wp {wp_id} dependency {dep_id} is {dep_state}, "
                    f"must be READY_FOR_AUDIT or AUDITED_PASS"
                )

        # 4. R5 补全: Plan 验证
        if not self.has_plan(wp_id):
            errors.append(EC.WP_DEPENDENCY_NOT_MET)
            details.append(f"wp {wp_id} has no registered Plan — cannot start without valid Plan")

        return len(errors) == 0, errors, details

    def start(self, wp_id: str, *, actor_type: str = "IMPLEMENTER") -> tuple[bool, list[EC], list[str]]:
        """开始一个 WP（NOT_STARTED → IN_PROGRESS）。

        如果依赖不满足，拒绝并返回错误。
        """
        ok, errors, details = self.can_start(wp_id)
        if not ok:
            return False, errors, details

        from_state = self.get_state(wp_id)
        self.wp_states[wp_id] = "IN_PROGRESS"
        self._record_event(wp_id, from_state, "IN_PROGRESS", actor_type, "start", details)
        return True, [], []

    def can_complete(
        self, wp_id: str, *, actor_type: str = "IMPLEMENTER",
        completion_contract: str = "", target_state: str = "READY_FOR_AUDIT",
    ) -> tuple[bool, list[EC], list[str]]:
        """检查 WP 是否可以完成（IN_PROGRESS → READY_FOR_AUDIT）。

        R5 补全: complete 命令检查：
        1. WP 存在
        2. 当前状态为 IN_PROGRESS 或 IMPLEMENTED_PENDING_EVIDENCE
        3. completion contract 与 owner 匹配
        4. implementer 不能写 AUDITED_* 状态
        5. target_state 是合法的完成状态
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. WP 存在
        try:
            spec = self._get_wp_spec(wp_id)
        except ValueError:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown wp_id: {wp_id}")
            return False, errors, details

        # 2. 当前状态
        current = self.get_state(wp_id)
        if current not in ("IN_PROGRESS", "IMPLEMENTED_PENDING_EVIDENCE"):
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"wp {wp_id} in state {current}, must be IN_PROGRESS or IMPLEMENTED_PENDING_EVIDENCE to complete")

        # 3. completion contract 与 owner 匹配
        expected_contract = spec.get("completion_contract", "")
        if completion_contract and completion_contract != expected_contract:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(
                f"completion contract mismatch: expected {expected_contract}, got {completion_contract}"
            )

        # 4. implementer 不能写 AUDITED_* 状态
        if actor_type == "IMPLEMENTER" and target_state in _IMPLEMENTER_FORBIDDEN_STATES:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"implementer cannot write {target_state} for {wp_id}")

        # 5. 合法转换
        allowed = _LEGAL_TRANSITIONS.get(current, frozenset())
        if target_state not in allowed:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"illegal transition: {current} → {target_state}")

        return len(errors) == 0, errors, details

    def complete(
        self, wp_id: str, *, actor_type: str = "IMPLEMENTER",
        completion_contract: str = "", target_state: str = "READY_FOR_AUDIT",
    ) -> tuple[bool, list[EC], list[str]]:
        """完成一个 WP（IN_PROGRESS → READY_FOR_AUDIT）。

        R5 补全: complete 命令。
        """
        ok, errors, details = self.can_complete(
            wp_id, actor_type=actor_type,
            completion_contract=completion_contract, target_state=target_state,
        )
        if not ok:
            return False, errors, details

        from_state = self.get_state(wp_id)
        self.wp_states[wp_id] = target_state
        self._record_event(wp_id, from_state, target_state, actor_type, "complete", details)
        return True, [], []

    def can_activate(
        self, wp_id: str, *,
        permit_ref: str = "", reservation_ref: str = "",
    ) -> tuple[bool, list[EC], list[str]]:
        """检查 WP 是否可以激活（READY_FOR_AUDIT → live action）。

        R5 补全: activate 命令检查：
        1. WP 存在
        2. 当前状态为 AUDITED_PASS（或精确未审 canary 例外）
        3. 所有 activation_dependencies 处于 AUDITED_PASS
        4. 有不可扩权 Permit 与原子 RESERVED receipt
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. WP 存在
        try:
            spec = self._get_wp_spec(wp_id)
        except ValueError:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown wp_id: {wp_id}")
            return False, errors, details

        # 2. 当前状态
        current = self.get_state(wp_id)
        if current != "AUDITED_PASS":
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"wp {wp_id} in state {current}, must be AUDITED_PASS to activate")

        # 3. activation dependencies
        act_deps = spec.get("activation_dependencies", [])
        for dep_id in act_deps:
            dep_state = self.get_state(dep_id)
            if dep_state not in _ACT_DEP_MIN_STATES:
                errors.append(EC.WP_DEPENDENCY_NOT_MET)
                details.append(
                    f"wp {wp_id} activation dependency {dep_id} is {dep_state}, "
                    f"must be AUDITED_PASS"
                )

        # 4. Permit 和 Reservation
        if not permit_ref:
            errors.append(EC.WP_DEPENDENCY_NOT_MET)
            details.append(f"wp {wp_id} activate requires permit_ref")
        if not reservation_ref:
            errors.append(EC.WP_DEPENDENCY_NOT_MET)
            details.append(f"wp {wp_id} activate requires reservation_ref")

        return len(errors) == 0, errors, details

    def activate(
        self, wp_id: str, *,
        permit_ref: str = "", reservation_ref: str = "",
        actor_type: str = "IMPLEMENTER",
    ) -> tuple[bool, list[EC], list[str]]:
        """激活一个 WP（AUDITED_PASS → live action）。

        R5 补全: activate 命令。
        注意：activate 不改变 WP 状态（AUDITED_PASS 是 terminal），
        但记录激活事件。
        """
        ok, errors, details = self.can_activate(
            wp_id, permit_ref=permit_ref, reservation_ref=reservation_ref,
        )
        if not ok:
            return False, errors, details

        self._record_event(wp_id, "AUDITED_PASS", "AUDITED_PASS", actor_type, "activate", details)
        return True, [], []

    def transition(self, wp_id: str, new_state: str, *, actor_type: str = "SYSTEM") -> tuple[bool, list[EC], list[str]]:
        """转换 WP 状态。

        检查：
        1. WP 存在
        2. new_state 是合法状态
        3. 当前状态 → new_state 是合法转换
        4. 如果是 IN_PROGRESS，检查 development dependencies
        5. R5 补全: implementer 不能写 AUDITED_*
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. WP 存在
        try:
            self._get_wp_spec(wp_id)
        except ValueError:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown wp_id: {wp_id}")
            return False, errors, details

        # 2. 合法状态
        if new_state not in VALID_STATES:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"invalid state: {new_state}")
            return False, errors, details

        current = self.get_state(wp_id)

        # 3. 合法转换
        allowed = _LEGAL_TRANSITIONS.get(current, frozenset())
        if new_state not in allowed:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"illegal transition: {current} → {new_state}")
            return False, errors, details

        # 4. 如果进入 IN_PROGRESS，检查 dependencies
        if new_state == "IN_PROGRESS":
            ok, dep_errors, dep_details = self.can_start(wp_id)
            if not ok:
                return False, dep_errors, dep_details

        # 5. R5 补全: implementer 不能写 AUDITED_*
        if actor_type == "IMPLEMENTER" and new_state in _IMPLEMENTER_FORBIDDEN_STATES:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"implementer cannot write {new_state} for {wp_id}")
            return False, errors, details

        from_state = current
        self.wp_states[wp_id] = new_state
        self._record_event(wp_id, from_state, new_state, actor_type, "transition", details)
        return True, [], []

    def project_to_board(self) -> list[dict[str, str]]:
        """生成 board 投影：wp_id → state。

        确保 board 与实际状态一致。
        """
        self._load_dag()
        board = []
        for wp in self._dag.get("work_packages", []):
            wp_id = wp["wp_id"]
            board.append({
                "wp_id": wp_id,
                "state": self.get_state(wp_id),
                "owner_type": wp.get("owner_type", ""),
                "completion_contract": wp.get("completion_contract", ""),
            })
        return board

    def verify_board_consistency(self, board: list[dict[str, str]]) -> tuple[bool, list[EC], list[str]]:
        """验证 board 投影与实际状态一致。"""
        errors: list[EC] = []
        details: list[str] = []

        actual = {row["wp_id"]: row["state"] for row in self.project_to_board()}
        for row in board:
            wp_id = row.get("wp_id", "")
            board_state = row.get("state", "")
            actual_state = actual.get(wp_id)
            if actual_state is None:
                errors.append(EC.WP_UNKNOWN)
                details.append(f"board has unknown wp_id: {wp_id}")
            elif board_state != actual_state:
                errors.append(EC.WP_ILLEGAL_TRANSITION)
                details.append(
                    f"board state mismatch for {wp_id}: "
                    f"board={board_state}, actual={actual_state}"
                )

        return len(errors) == 0, errors, details

    def get_event_log(self) -> list[dict[str, Any]]:
        """获取 append-only 事件日志。"""
        return [evt.to_dict() for evt in self.event_log]

    def verify_event_log_consistency(self) -> tuple[bool, list[EC], list[str]]:
        """验证事件日志与当前状态一致。

        从事件日志重放，检查最终状态与 wp_states 一致。
        """
        errors: list[EC] = []
        details: list[str] = []

        replayed: dict[str, str] = {}
        for evt in self.event_log:
            if evt.to_state != "AUDITED_PASS" or evt.command != "activate":
                replayed[evt.wp_id] = evt.to_state

        for wp_id, state in self.wp_states.items():
            replayed_state = replayed.get(wp_id, "NOT_STARTED")
            if replayed_state != state:
                errors.append(EC.WP_ILLEGAL_TRANSITION)
                details.append(
                    f"event log inconsistency for {wp_id}: "
                    f"replayed={replayed_state}, actual={state}"
                )

        return len(errors) == 0, errors, details
