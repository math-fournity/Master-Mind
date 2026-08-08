"""
checkpoint manager 原语（261号§3.5）。

用SHA-256内容哈希标识状态快照：
- 计算六元组状态的哈希（规范化JSON → SHA-256）
- 存储checkpoint快照（内存字典，不依赖ArangoDB——测试用）
- 从checkpoint恢复状态
"""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Optional, Any


@dataclass
class Checkpoint:
    """状态检查点"""
    checkpoint_id: str           # SHA-256哈希
    round_index: int             # 轮次
    six_tuple_dict: Dict         # 六元组状态的dict表示
    timestamp: str               # 创建时间戳
    metadata: Dict = field(default_factory=dict)  # 额外元数据

    def __repr__(self) -> str:
        return (
            f"Checkpoint(id={self.checkpoint_id[:12]}..., "
            f"round={self.round_index}, "
            f"timestamp={self.timestamp})"
        )


class CheckpointManager:
    """检查点管理器：内存存储，不依赖ArangoDB（测试用）。"""

    def __init__(self):
        self._checkpoints: Dict[str, Checkpoint] = {}  # id -> Checkpoint
        self._round_index: Dict[int, str] = {}         # round -> checkpoint_id

    def _normalize(self, six_tuple_dict: Dict) -> str:
        """规范化六元组dict为JSON字符串（排序key）。"""
        return json.dumps(six_tuple_dict, sort_keys=True, ensure_ascii=False)

    def _compute_hash(self, six_tuple_dict: Dict) -> str:
        """计算六元组dict的SHA-256哈希。"""
        normalized = self._normalize(six_tuple_dict)
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    def save(self, round_index: int, six_tuple_dict: Dict,
             metadata: Optional[Dict] = None) -> Checkpoint:
        """
        保存checkpoint。

        Args:
            round_index: 轮次
            six_tuple_dict: 六元组状态的dict表示（six_tuple.to_dict()）
            metadata: 额外元数据（可选）

        Returns:
            Checkpoint 对象
        """
        checkpoint_id = self._compute_hash(six_tuple_dict)
        timestamp = datetime.now(timezone.utc).isoformat()
        checkpoint = Checkpoint(
            checkpoint_id=checkpoint_id,
            round_index=round_index,
            six_tuple_dict=dict(six_tuple_dict),
            timestamp=timestamp,
            metadata=dict(metadata) if metadata else {},
        )
        self._checkpoints[checkpoint_id] = checkpoint
        self._round_index[round_index] = checkpoint_id
        return checkpoint

    def restore(self, checkpoint_id: str) -> Optional[Checkpoint]:
        """从checkpoint恢复（按id）。"""
        return self._checkpoints.get(checkpoint_id)

    def get_by_round(self, round_index: int) -> Optional[Checkpoint]:
        """按轮次获取checkpoint。"""
        checkpoint_id = self._round_index.get(round_index)
        if checkpoint_id is None:
            return None
        return self._checkpoints.get(checkpoint_id)

    def verify_integrity(self, checkpoint_id: str) -> bool:
        """
        验证checkpoint完整性（重新计算哈希对比）。

        Returns:
            True 如果存储的六元组重新计算哈希 == checkpoint_id
        """
        checkpoint = self._checkpoints.get(checkpoint_id)
        if checkpoint is None:
            return False
        recomputed = self._compute_hash(checkpoint.six_tuple_dict)
        return recomputed == checkpoint_id

    def all_ids(self) -> list:
        """返回所有checkpoint id（测试辅助）。"""
        return list(self._checkpoints.keys())

    def count(self) -> int:
        """返回checkpoint总数。"""
        return len(self._checkpoints)
