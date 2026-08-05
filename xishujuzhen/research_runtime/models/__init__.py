"""
models: 123号v1定义的类型化对象——Task/Workspace/RunState

对应127号Schema冻结文档§1(Task)/§2(Workspace)/§3(Event)的类型定义。
Phase 1只定义类型，不实现状态归约（State Reducer在Phase 2创建）。

架构基线：123号§14(Task) + §15(Workspace) + §17(Event) + 127号§1/§2/§3
"""

from .task import Task, TaskType
from .workspace import Workspace, RunState
from .event import RawEvent, SemanticEvent, EventFactory

__all__ = [
    "Task", "TaskType",
    "Workspace", "RunState",
    "RawEvent", "SemanticEvent", "EventFactory",
]
