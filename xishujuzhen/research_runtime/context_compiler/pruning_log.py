"""
裁剪清单——记录哪些内容被裁剪、为什么裁剪

对应135号P5-7.1 + 123号§50。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class PruningRecord:
    """裁剪记录"""
    content_id: str
    reason: str  # 裁剪原因
    pruned_at: str = ""
    original_size: int = 0  # 原始大小
    pruned_size: int = 0    # 裁剪后大小

    def to_dict(self) -> dict:
        return {
            "content_id": self.content_id,
            "reason": self.reason,
            "pruned_at": self.pruned_at,
            "original_size": self.original_size,
            "pruned_size": self.pruned_size,
        }


class PruningLog:
    """
    裁剪清单（135号P5-7.1）。

    冻结声明：
    - 记录哪些内容被裁剪、为什么裁剪
    """

    def __init__(self):
        self._records: List[PruningRecord] = []

    def log(self, content_id: str, reason: str, original_size: int = 0, pruned_size: int = 0) -> PruningRecord:
        """
        记录裁剪。

        边界情况：无裁剪、裁剪原因不明确
        """
        record = PruningRecord(
            content_id=content_id,
            reason=reason,
            pruned_at=datetime.now().isoformat(),
            original_size=original_size,
            pruned_size=pruned_size,
        )
        self._records.append(record)
        return record

    def get_all(self) -> List[PruningRecord]:
        return list(self._records)

    def get_by_content(self, content_id: str) -> Optional[PruningRecord]:
        for r in self._records:
            if r.content_id == content_id:
                return r
        return None

    def count(self) -> int:
        return len(self._records)

    def check_reasons_clear(self) -> bool:
        """
        验证裁剪原因明确。

        边界情况：裁剪原因不明确
        """
        return all(r.reason for r in self._records)
