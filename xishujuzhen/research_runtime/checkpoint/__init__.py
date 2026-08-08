"""
checkpoint: 状态检查点原语（261号§3.5）。

用SHA-256内容哈希标识状态快照：
- 计算六元组状态的哈希（规范化JSON → SHA-256）
- 存储checkpoint快照（内存字典，不依赖ArangoDB——测试用）
- 从checkpoint恢复状态
"""

from .manager import Checkpoint, CheckpointManager

__all__ = ["Checkpoint", "CheckpointManager"]
