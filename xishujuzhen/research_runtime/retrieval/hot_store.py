"""
热层存储——Q_0、W_t充分快照、关键事件、开放义务、最小证据

对应135号P5-1.3 + 123号§29 + 系统探讨.md§11.5。

热层特点：
- 保存：Q_0、W_t充分快照、关键事件、开放义务、最小证据
- 使用方式：Solver当前工作台
- 实时更新
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class HotEntry:
    """热层条目"""
    workspace_id: str
    q0: str  # 原题
    w_t_snapshot: Dict[str, Any]  # W_t充分快照（8字段，见StateSnapshot）
    key_events: List[Dict[str, Any]] = field(default_factory=list)  # 关键事件
    open_obligations: List[str] = field(default_factory=list)  # 开放义务ID
    minimal_evidence: List[str] = field(default_factory=list)  # 最小证据ID
    timestamp: str = ""

    def to_dict(self) -> dict:
        return {
            "workspace_id": self.workspace_id,
            "q0": self.q0,
            "w_t_snapshot": self.w_t_snapshot,
            "key_events": self.key_events,
            "open_obligations": self.open_obligations,
            "minimal_evidence": self.minimal_evidence,
            "timestamp": self.timestamp,
        }


class HotStore:
    """
    热层存储（135号P5-1.3）。

    冻结声明：
    - 热层是Solver当前工作台，实时更新
    - 热层只保存充分快照，不保存全部历史（R-6风险防线）
    """

    def __init__(self):
        self._workspaces: Dict[str, HotEntry] = {}

    def update(self, entry: HotEntry) -> str:
        """更新热层（实时更新Solver当前工作台）"""
        self._workspaces[entry.workspace_id] = entry
        return entry.workspace_id

    def get_current(self, workspace_id: str) -> Optional[HotEntry]:
        """
        获取当前工作台状态。

        边界情况：热层过大、热层数据过期
        """
        return self._workspaces.get(workspace_id)

    def get_open_obligations(self, workspace_id: str) -> List[str]:
        entry = self._workspaces.get(workspace_id)
        return entry.open_obligations if entry else []

    def count(self) -> int:
        return len(self._workspaces)
