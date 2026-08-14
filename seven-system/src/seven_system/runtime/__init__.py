"""WP-RT1 Runtime — WorkEvent, lease/fence, outbox, CommitIntent, reconcile.

RT1 实现：
- WorkEvent（append-only event sourcing）
- lease/fence 协议
- outbox（与状态事件同一 DB 事务）
- CommitIntent（final rename 前的 durable intent）
- artifact/DB reconcile
- GV0 canonical Arango expected-revision transaction reservation backend
- Redis rebuildable projection

RT1 消费 DB1I 的 DatabaseSchemaStateReport 作为输入，消费 VLT0 CAS/Vault 能力，
消费 GV0 verifier 接口和 ReservationBackendPort。

RT1 输出：DatabaseRuntimeCapabilityReport + ArtifactCommitReconcileCapabilityReport
+ RuntimeCheckpoint/recovery receipts。
RT1 不得重发 SchemaStateReport（那是 DB1I 的输出）。

SIDE_EFFECT_FREE：不接触真实 DB、真实 Redis 或真实 D 盘写入。
"""

from __future__ import annotations
