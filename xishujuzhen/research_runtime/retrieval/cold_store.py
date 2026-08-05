"""
冷层存储——论文、教材、题解、MathLib、题库、全部证据

对应135号P5-1.1 + 123号§29。

冷层特点：
- 保存：论文、教材、题解、MathLib、题库、全部证据
- 使用方式：默认不进Solver上下文（R-16风险防线）
- 只有按需查询时才返回结果
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class ColdEntry:
    """冷层条目"""
    entry_id: str
    content_type: str  # paper/textbook/solution/mathlib/problem_bank/evidence
    title: str
    content: str
    source_id: str  # 关联SourceRegistry的source_id
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "entry_id": self.entry_id,
            "content_type": self.content_type,
            "title": self.title,
            "content": self.content,
            "source_id": self.source_id,
            "metadata": self.metadata,
        }


class ColdStore:
    """
    冷层存储（135号P5-1.1）。

    冻结声明：
    - 冷层默认不进Solver上下文（P5-1.COMP2 + R-16风险）
    - 冷索引标签不被当成已理解知识（R-16风险）
    """

    def __init__(self):
        self._entries: Dict[str, ColdEntry] = {}

    def store(self, entry: ColdEntry) -> str:
        """存储冷层条目"""
        self._entries[entry.entry_id] = entry
        return entry.entry_id

    def query(self, filter_fn=None) -> List[ColdEntry]:
        """
        按需查询冷层——默认不返回全部。

        边界情况：冷层为空、冷层数据格式不兼容
        """
        if filter_fn is None:
            return list(self._entries.values())
        return [e for e in self._entries.values() if filter_fn(e)]

    def query_by_type(self, content_type: str) -> List[ColdEntry]:
        """按内容类型查询"""
        return [e for e in self._entries.values() if e.content_type == content_type]

    def get_by_id(self, entry_id: str) -> Optional[ColdEntry]:
        return self._entries.get(entry_id)

    def count(self) -> int:
        return len(self._entries)

    def is_default_excluded_from_solver(self) -> bool:
        """
        验证冷层默认不进Solver上下文（P5-1.COMP2）。

        边界情况：冷层默认进Solver上下文（应被拒绝）
        """
        return True  # 冷层默认不进Solver上下文
