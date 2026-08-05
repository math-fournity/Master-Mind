"""
温层存储——类型过滤、表示映射、语义检索、图扩展、证据排序

对应135号P5-1.2 + 123号§29。

温层特点：
- 保存：类型过滤、表示映射、语义检索、图扩展、证据排序
- 使用方式：按当前义务查询
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class WarmEntry:
    """温层条目"""
    entry_id: str
    content_type: str  # type_filter/representation_map/semantic_index/graph_extension/evidence_ranking
    content: str
    obligation_refs: List[str] = field(default_factory=list)  # 关联的义务ID
    representation_refs: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "entry_id": self.entry_id,
            "content_type": self.content_type,
            "content": self.content,
            "obligation_refs": self.obligation_refs,
            "representation_refs": self.representation_refs,
            "metadata": self.metadata,
        }


class WarmStore:
    """
    温层存储（135号P5-1.2）。

    冻结声明：
    - 温层按当前义务查询，不是返回全部
    """

    def __init__(self):
        self._entries: Dict[str, WarmEntry] = {}

    def store(self, entry: WarmEntry) -> str:
        self._entries[entry.entry_id] = entry
        return entry.entry_id

    def query_by_obligation(self, obligation_id: str) -> List[WarmEntry]:
        """
        按当前义务查询温层。

        边界情况：温层为空、温层查询无结果
        """
        return [e for e in self._entries.values() if obligation_id in e.obligation_refs]

    def query_by_representation(self, representation_id: str) -> List[WarmEntry]:
        return [e for e in self._entries.values() if representation_id in e.representation_refs]

    def query_by_type(self, content_type: str) -> List[WarmEntry]:
        return [e for e in self._entries.values() if e.content_type == content_type]

    def get_by_id(self, entry_id: str) -> Optional[WarmEntry]:
        return self._entries.get(entry_id)

    def count(self) -> int:
        return len(self._entries)
