"""
冷层来源注册——记录论文/教材的版本、许可证和撤稿状态

对应135号P5-1.5 + R-15风险防线（来源许可证/版本漂移）+ 128号§2 R-15。

R-15风险：原始来源许可证、版本和撤稿状态变化。
"""

from dataclasses import dataclass, field
from typing import Dict, Optional, List
from datetime import datetime


@dataclass
class SourceRecord:
    """来源注册记录"""
    source_id: str
    title: str
    version: str
    license: str  # 许可证类型（如CC-BY/MIT/proprietary）
    retracted: bool = False  # 是否已撤稿
    retraction_reason: str = ""
    registered_at: str = ""
    last_checked: str = ""

    def to_dict(self) -> dict:
        return {
            "source_id": self.source_id,
            "title": self.title,
            "version": self.version,
            "license": self.license,
            "retracted": self.retracted,
            "retraction_reason": self.retraction_reason,
            "registered_at": self.registered_at,
            "last_checked": self.last_checked,
        }


class SourceRegistry:
    """
    冷层来源注册（135号P5-1.5）。

    R-15风险防线：来源许可证/版本漂移。

    冻结声明：
    - 记录论文/教材的版本、许可证和撤稿状态
    - 已撤稿的来源不应继续使用
    """

    def __init__(self):
        self._sources: Dict[str, SourceRecord] = {}

    def register(self, record: SourceRecord) -> str:
        """
        注册来源。

        边界情况：来源无版本信息
        """
        if not record.version:
            record.version = "unknown"
        if not record.registered_at:
            record.registered_at = datetime.now().isoformat()
        self._sources[record.source_id] = record
        return record.source_id

    def check_status(self, source_id: str) -> Optional[SourceRecord]:
        """
        检查来源状态——版本/许可证/撤稿。

        边界情况：来源已撤稿但仍在使用（应被拒绝）
        """
        return self._sources.get(source_id)

    def is_retracted(self, source_id: str) -> bool:
        """检查来源是否已撤稿"""
        record = self._sources.get(source_id)
        return record.retracted if record else False

    def check_not_using_retracted(self, source_ids: List[str]) -> bool:
        """
        验证没有使用已撤稿的来源（R-15风险防线）。

        边界情况：来源已撤稿但仍在使用（应被拒绝）
        """
        for sid in source_ids:
            if self.is_retracted(sid):
                return False
        return True

    def update_retraction(self, source_id: str, retracted: bool, reason: str = ""):
        """更新撤稿状态"""
        record = self._sources.get(source_id)
        if record:
            record.retracted = retracted
            record.retraction_reason = reason
            record.last_checked = datetime.now().isoformat()

    def count(self) -> int:
        return len(self._sources)
