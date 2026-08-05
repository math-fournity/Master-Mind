"""
events: 原始/语义事件存储与checkpoint

对应131号P1-3(RawEvent)/P1-4(SemanticEvent)/P1-5(checkpoint)。

ArangoDB collections（新创建，不动旧数据，NO-10约束）：
  raw_events       - 原始事件（append-only）
  semantic_events  - 语义事件（可重抽）
  checkpoints      - 内容寻址checkpoint

架构基线：123号§17 + 127号§3 + 128号G0-1
"""

from .store import EventStore, CheckpointStore
from .migrate import create_event_collections
from .extractor import SemanticExtractor
from .capture import EventCapture

__all__ = [
    "EventStore", "CheckpointStore",
    "create_event_collections",
    "SemanticExtractor", "EventCapture",
]
