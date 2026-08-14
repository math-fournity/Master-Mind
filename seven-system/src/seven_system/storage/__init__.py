"""Storage 子包：CompletionArtifactStore 和底层 append-once 原语。

GV0 复用并硬化 v0.1 的 append-once artifact-store 代码为最小
CompletionArtifactStore，用于保存 GV0 自身及后续普通工作包的
CompletionBundle。WP-VLT0 随后复用并扩展同一 CAS 核心。

本 __init__ 同时 re-export 原 storage.py 模块的公共 API，
保持向后兼容（epoch.py 等已有消费者不破坏）。
"""

# Re-export from the original storage module (now at storage/_legacy.py)
# The original storage.py was renamed to _legacy.py inside this package.
from ._legacy import (
    ContentConflictError,
    commit_json_once,
    commit_text_once,
    read_json,
)

from .artifact_store import (
    CompletionArtifactStore,
    ArtifactRef,
)
from .artifact_seal import (
    ArtifactSealProtocol,
    CommitIntent,
    ArtifactManifest,
)
from .reconcile import (
    ArtifactReconciler,
    ReconcileEntry,
    DBArtifactRecord,
)

__all__ = [
    "ContentConflictError",
    "commit_json_once",
    "commit_text_once",
    "read_json",
    "CompletionArtifactStore",
    "ArtifactRef",
    "ArtifactSealProtocol",
    "CommitIntent",
    "ArtifactManifest",
    "ArtifactReconciler",
    "ReconcileEntry",
    "DBArtifactRecord",
]
