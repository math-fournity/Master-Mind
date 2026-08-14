"""WorkPackageStateService — R5: DAG 依赖强制执行与 board 投影。

R5 整改：审计发现 22 个工作包曾被越级标为 IMPLEMENTED_PENDING_EVIDENCE，
但 development dependency 未满足（GV0 未到 READY_FOR_AUDIT）。
本服务根据 canonical DAG 强制执行：
1. 工作包只能从 NOT_STARTED → IN_PROGRESS（不能越级）
2. 进入 IN_PROGRESS 前，所有 development_dependencies 必须处于
   READY_FOR_AUDIT 或 AUDITED_PASS 状态
3. 进入 READY_FOR_AUDIT 前，工作包必须处于 IN_PROGRESS
4. 进入 AUDITED_PASS 前，工作包必须处于 READY_FOR_AUDIT 且有 AuditRecord

board 投影：从 WP 状态集合生成 board 视图，确保 board 与实际状态一致。

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB/D 盘/模型。
"""

from __future__ import annotations

import json
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


@dataclass
class WorkPackageStateService:
    """WorkPackageStateService — DAG 依赖强制执行器。

    持有：
    - dag_path: canonical DAG 路径
    - wp_states: wp_id → 当前状态
    - _dag: 加载的 DAG（lazy）
    """

    dag_path: Path
    wp_states: dict[str, str] = field(default_factory=dict)
    _dag: dict[str, Any] | None = None
    _dag_index: dict[str, dict[str, Any]] = field(default_factory=dict)

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

    def get_state(self, wp_id: str) -> str:
        """获取 WP 当前状态。默认 NOT_STARTED。"""
        return self.wp_states.get(wp_id, "NOT_STARTED")

    def can_start(self, wp_id: str) -> tuple[bool, list[EC], list[str]]:
        """检查 WP 是否可以开始（NOT_STARTED → IN_PROGRESS）。

        检查：
        1. WP 存在于 DAG
        2. 当前状态为 NOT_STARTED 或 READY
        3. 所有 development_dependencies 处于 READY_FOR_AUDIT 或 AUDITED_PASS
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

        return len(errors) == 0, errors, details

    def start(self, wp_id: str) -> tuple[bool, list[EC], list[str]]:
        """开始一个 WP（NOT_STARTED → IN_PROGRESS）。

        如果依赖不满足，拒绝并返回错误。
        """
        ok, errors, details = self.can_start(wp_id)
        if not ok:
            return False, errors, details

        self.wp_states[wp_id] = "IN_PROGRESS"
        return True, [], []

    def transition(self, wp_id: str, new_state: str) -> tuple[bool, list[EC], list[str]]:
        """转换 WP 状态。

        检查：
        1. WP 存在
        2. new_state 是合法状态
        3. 当前状态 → new_state 是合法转换
        4. 如果是 IN_PROGRESS，检查 development dependencies
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

        self.wp_states[wp_id] = new_state
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
