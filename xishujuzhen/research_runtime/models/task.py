"""
Task schema: 123号§14 + 127号§1

初始任务 Q_0 = (D, Γ_0, G_0, κ, χ)
- D: 对象/表达语言 (objects)
- Γ_0: 前提 (premises)
- G_0: 目标 (goal)
- κ: 任务类型 (type)
- χ: 成功/停止条件 (success_conditions / stop_conditions)

冻结声明：Q_0在运行时保持冻结。任务类型不只是prove——不让整个系统只适配定理证明。
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


class TaskType(str, Enum):
    """123号§14定义的9种任务类型"""
    PROVE = "prove"
    REFUTE = "refute"
    CONSTRUCT = "construct"
    COMPUTE = "compute"
    CLASSIFY = "classify"
    OPTIMIZE = "optimize"
    CONJECTURE = "conjecture"
    EXPLAIN = "explain"
    VALUE = "value"


@dataclass
class Task:
    """
    127号§1 Task Schema冻结定义。
    Q_0在运行时保持冻结（127号§1冻结声明）。
    """
    task_id: str
    type: TaskType
    domain: str                          # 数学领域（如 number_theory, algebraic_geometry）
    objects: List[str]                   # 数学对象和表达语言 D
    premises: List[str]                  # 原始前提与约束 Γ_0
    goal: str                            # 目标 G_0
    success_conditions: List[str]        # 成功条件 χ_success
    stop_conditions: List[str]           # 停止条件 χ_stop
    failure_conditions: List[str] = field(default_factory=list)  # 失败条件（可选）

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "type": self.type.value,
            "domain": self.domain,
            "objects": self.objects,
            "premises": self.premises,
            "goal": self.goal,
            "success_conditions": self.success_conditions,
            "stop_conditions": self.stop_conditions,
            "failure_conditions": self.failure_conditions,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Task":
        return cls(
            task_id=d["task_id"],
            type=TaskType(d["type"]),
            domain=d["domain"],
            objects=d["objects"],
            premises=d["premises"],
            goal=d["goal"],
            success_conditions=d["success_conditions"],
            stop_conditions=d["stop_conditions"],
            failure_conditions=d.get("failure_conditions", []),
        )
