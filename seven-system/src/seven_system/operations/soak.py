"""SoakTestRunner — 长时间 soak 测试。

来自 WP-OP1：soak、连续执行、资源监控、崩溃检测、恢复验证。

关键约束（blocker）：
- soak 崩溃未恢复 → OP_SOAK_CRASH_NOT_RECOVERED
- soak 状态不在 OP_SOAK_STATES → OP_SOAK_STATE_INVALID

SIDE_EFFECT_FREE：用确定性场景模拟 soak。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    OP_SOAK_STATES,
    VerificationErrorCode as EC,
)


class SoakTestError(Exception):
    """Soak test 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class SoakTick:
    """单个 soak tick 记录。"""

    tick: int
    state: str
    resource_usage: dict[str, float] = field(default_factory=dict)
    event: str = "TICK"  # TICK / CRASH / RECOVER / COMPLETE

    def to_dict(self) -> dict[str, Any]:
        return {
            "tick": self.tick,
            "state": self.state,
            "resource_usage": dict(self.resource_usage),
            "event": self.event,
        }


@dataclass
class SoakTestReport:
    """Soak test 报告。"""

    report_id: str
    total_ticks: int
    crashes: int
    recoveries: int
    completed: bool
    final_state: str
    ticks: list[SoakTick] = field(default_factory=list)
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_id": self.report_id,
            "total_ticks": self.total_ticks,
            "crashes": self.crashes,
            "recoveries": self.recoveries,
            "completed": self.completed,
            "final_state": self.final_state,
            "ticks": [t.to_dict() for t in self.ticks],
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


class SoakTestRunner:
    """Soak test 运行器。

    用确定性场景模拟 soak：连续 tick、注入崩溃、验证恢复。
    每个 crash 必须有对应 recovery，否则 OP_SOAK_CRASH_NOT_RECOVERED。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    def __init__(self) -> None:
        self._state: str = "IDLE"
        self._ticks: list[SoakTick] = []
        self._current_tick: int = 0
        self._crashes: int = 0
        self._recoveries: int = 0
        self._unrecovered_crash: bool = False

    @property
    def state(self) -> str:
        return self._state

    @property
    def ticks(self) -> list[SoakTick]:
        return list(self._ticks)

    @property
    def total_ticks(self) -> int:
        return len(self._ticks)

    @property
    def crashes(self) -> int:
        return self._crashes

    @property
    def recoveries(self) -> int:
        return self._recoveries

    def start(self) -> None:
        """开始 soak test。"""
        if self._state != "IDLE":
            raise SoakTestError(
                EC.OP_SOAK_STATE_INVALID,
                f"cannot start from state {self._state}",
            )
        self._state = "RUNNING"

    def tick(
        self,
        *,
        resource_usage: dict[str, float] | None = None,
    ) -> SoakTick:
        """执行一个 soak tick。"""
        if self._state not in ("RUNNING", "RECOVERED"):
            raise SoakTestError(
                EC.OP_SOAK_STATE_INVALID,
                f"cannot tick from state {self._state}",
            )
        if self._state == "RECOVERED":
            self._state = "RUNNING"
        t = SoakTick(
            tick=self._current_tick,
            state=self._state,
            resource_usage=resource_usage or {"cpu": 0.5, "mem": 0.3},
            event="TICK",
        )
        self._ticks.append(t)
        self._current_tick += 1
        return t

    def inject_crash(self) -> SoakTick:
        """注入崩溃。"""
        if self._state != "RUNNING":
            raise SoakTestError(
                EC.OP_SOAK_STATE_INVALID,
                f"cannot crash from state {self._state}",
            )
        self._state = "CRASHED"
        self._crashes += 1
        self._unrecovered_crash = True
        t = SoakTick(
            tick=self._current_tick,
            state=self._state,
            event="CRASH",
        )
        self._ticks.append(t)
        self._current_tick += 1
        return t

    def recover(self) -> SoakTick:
        """从崩溃恢复。"""
        if self._state != "CRASHED":
            raise SoakTestError(
                EC.OP_SOAK_STATE_INVALID,
                f"cannot recover from state {self._state}",
            )
        self._state = "RECOVERING"
        t = SoakTick(
            tick=self._current_tick,
            state=self._state,
            event="RECOVER",
        )
        self._ticks.append(t)
        self._current_tick += 1
        self._state = "RECOVERED"
        self._recoveries += 1
        self._unrecovered_crash = False
        return t

    def complete(self) -> SoakTick:
        """完成 soak test。"""
        if self._unrecovered_crash:
            raise SoakTestError(
                EC.OP_SOAK_CRASH_NOT_RECOVERED,
                "cannot complete with unrecovered crash",
            )
        if self._state not in ("RUNNING", "RECOVERED"):
            raise SoakTestError(
                EC.OP_SOAK_STATE_INVALID,
                f"cannot complete from state {self._state}",
            )
        self._state = "COMPLETED"
        t = SoakTick(
            tick=self._current_tick,
            state=self._state,
            event="COMPLETE",
        )
        self._ticks.append(t)
        self._current_tick += 1
        return t

    def build_report(self, report_id: str) -> SoakTestReport:
        """构建 soak test 报告。"""
        report = SoakTestReport(
            report_id=report_id,
            total_ticks=self.total_ticks,
            crashes=self._crashes,
            recoveries=self._recoveries,
            completed=(self._state == "COMPLETED"),
            final_state=self._state,
            ticks=list(self._ticks),
        )
        report.content_hash = report.compute_content_hash()
        return report

    def verify_crash_recovery(self) -> list[tuple[EC, str]]:
        """验证所有崩溃都已恢复。"""
        errors: list[tuple[EC, str]] = []
        if self._unrecovered_crash:
            errors.append((
                EC.OP_SOAK_CRASH_NOT_RECOVERED,
                "unrecovered crash detected",
            ))
        if self._crashes != self._recoveries:
            errors.append((
                EC.OP_SOAK_CRASH_NOT_RECOVERED,
                f"crashes {self._crashes} != recoveries "
                f"{self._recoveries}",
            ))
        # 验证每个 CRASH 后都有 RECOVER
        crash_ticks = [
            t for t in self._ticks if t.event == "CRASH"
        ]
        recover_ticks = [
            t for t in self._ticks if t.event == "RECOVER"
        ]
        if len(crash_ticks) != len(recover_ticks):
            errors.append((
                EC.OP_SOAK_CRASH_NOT_RECOVERED,
                f"crash events {len(crash_ticks)} != recover events "
                f"{len(recover_ticks)}",
            ))
        return errors

    def verify_continuous_execution(self) -> list[tuple[EC, str]]:
        """验证连续执行（tick 序列连续无 gap）。"""
        errors: list[tuple[EC, str]] = []
        for i, t in enumerate(self._ticks):
            if t.tick != i:
                errors.append((
                    EC.OP_SOAK_STATE_INVALID,
                    f"tick gap: expected {i}, got {t.tick}",
                ))
        return errors

    def verify_state(self) -> list[tuple[EC, str]]:
        """验证 soak 状态合法。"""
        errors: list[tuple[EC, str]] = []
        if self._state not in OP_SOAK_STATES:
            errors.append((
                EC.OP_SOAK_STATE_INVALID,
                f"state {self._state!r} invalid",
            ))
        for t in self._ticks:
            if t.state not in OP_SOAK_STATES:
                errors.append((
                    EC.OP_SOAK_STATE_INVALID,
                    f"tick {t.tick} state {t.state!r} invalid",
                ))
        return errors
