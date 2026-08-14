"""CAS/DB reconcile 逻辑 — 识别 live/partial/sealed/missing/conflict 状态。

Reconciler 必须识别：
- live writer 仍活
- partial 且 writer 已死
- sealed artifact、DB 未 commit
- DB 已 commit、artifact 缺失或 hash 不符
- 多个 attempt 声称同一科学样本成功
- stale fence 晚提交
- sealed 对象被外部改写

SIDE_EFFECT_FREE：不接触真实 DB。DB 侧状态作为输入传入。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import RECONCILE_STATES, VerificationErrorCode as EC
from ..storage.artifact_store import CompletionArtifactStore


@dataclass
class ReconcileEntry:
    """单个 attempt 的 reconcile 状态。"""

    attempt_id: str
    job_id: str
    state: str  # RECONCILE_STATES 中的一个
    cas_sha256: str | None = None
    db_committed: bool = False
    db_artifact_sha256: str | None = None
    writer_alive: bool = False
    has_partial: bool = False
    has_sealed: bool = False
    intent_id: str | None = None
    intent_valid: bool = False
    fence_token: int | None = None
    current_fence: int | None = None
    details: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_id": self.attempt_id,
            "job_id": self.job_id,
            "state": self.state,
            "cas_sha256": self.cas_sha256,
            "db_committed": self.db_committed,
            "db_artifact_sha256": self.db_artifact_sha256,
            "writer_alive": self.writer_alive,
            "has_partial": self.has_partial,
            "has_sealed": self.has_sealed,
            "intent_id": self.intent_id,
            "intent_valid": self.intent_valid,
            "fence_token": self.fence_token,
            "current_fence": self.current_fence,
            "details": self.details,
        }


@dataclass
class DBArtifactRecord:
    """DB 侧的 artifact 记录（作为 reconcile 输入）。"""

    attempt_id: str
    job_id: str
    committed: bool
    artifact_sha256: str | None = None
    manifest_hash: str | None = None
    fence_token: int | None = None


class ArtifactReconciler:
    """CAS/DB 双向对账。

    SIDE_EFFECT_FREE：不修改 CAS 或 DB。
    接收 CAS 侧状态（通过 ArtifactSealProtocol）和 DB 侧状态（通过 DBArtifactRecord 列表），
    输出每个 attempt 的 reconcile 状态。
    """

    def __init__(self, artifact_store: CompletionArtifactStore) -> None:
        self._store = artifact_store

    def reconcile(
        self,
        *,
        cas_attempts: dict[str, dict[str, Any]],  # attempt_id → {has_partial, has_sealed, cas_sha256, writer_alive, intent_id, intent_valid, fence_token}
        db_records: dict[str, DBArtifactRecord],  # attempt_id → DBArtifactRecord
        current_fence: int | None = None,
    ) -> list[ReconcileEntry]:
        """执行双向对账。

        对每个 attempt，识别其 reconcile 状态：
        - LIVE_WRITER_ACTIVE: CAS 有 live writer 仍活
        - PARTIAL_WRITER_DEAD: CAS 有 partial，writer 已死，未 seal
        - SEALED_DB_UNCOMMITTED: CAS 已 seal，DB 未 commit
        - DB_COMMITTED_ARTIFACT_MISSING: DB 已 commit，CAS 缺失或 hash 不符
        - SEALED_AND_COMMITTED: CAS 已 seal 且 DB 已 commit，hash 一致
        - MISSING: CAS 和 DB 都没有
        - CONFLICT: hash 不匹配或其他冲突
        """
        results: list[ReconcileEntry] = []
        all_attempt_ids = set(cas_attempts.keys()) | set(db_records.keys())

        for attempt_id in sorted(all_attempt_ids):
            cas_info = cas_attempts.get(attempt_id, {})
            db_rec = db_records.get(attempt_id)

            entry = ReconcileEntry(
                attempt_id=attempt_id,
                job_id=cas_info.get("job_id", db_rec.job_id if db_rec else ""),
                state="MISSING",
            )

            has_partial = cas_info.get("has_partial", False)
            has_sealed = cas_info.get("has_sealed", False)
            cas_sha256 = cas_info.get("cas_sha256")
            writer_alive = cas_info.get("writer_alive", False)
            intent_id = cas_info.get("intent_id")
            intent_valid = cas_info.get("intent_valid", False)
            fence_token = cas_info.get("fence_token")

            entry.has_partial = has_partial
            entry.has_sealed = has_sealed
            entry.cas_sha256 = cas_sha256
            entry.writer_alive = writer_alive
            entry.intent_id = intent_id
            entry.intent_valid = intent_valid
            entry.fence_token = fence_token
            entry.current_fence = current_fence

            db_committed = db_rec is not None and db_rec.committed
            db_sha256 = db_rec.artifact_sha256 if db_rec else None
            entry.db_committed = db_committed
            entry.db_artifact_sha256 = db_sha256

            # 判定状态
            if writer_alive and not has_sealed:
                entry.state = "LIVE_WRITER_ACTIVE"
                entry.details = "live writer still active, cannot reconcile"

            elif has_partial and not has_sealed and not writer_alive:
                entry.state = "PARTIAL_WRITER_DEAD"
                entry.details = "partial bundle exists, writer dead, needs seal or cleanup"

            elif has_sealed and not db_committed:
                # CAS sealed but DB not committed
                if intent_valid and current_fence is not None and fence_token == current_fence:
                    entry.state = "SEALED_DB_UNCOMMITTED"
                    entry.details = "CAS sealed, DB uncommitted, valid intent + fence → can reconcile"
                else:
                    entry.state = "SEALED_DB_UNCOMMITTED"
                    entry.details = "CAS sealed, DB uncommitted, intent invalid or fence stale → quarantine"

            elif db_committed and not has_sealed:
                # DB committed but CAS missing
                entry.state = "DB_COMMITTED_ARTIFACT_MISSING"
                entry.details = "DB committed but CAS artifact missing → quarantine"

            elif has_sealed and db_committed:
                # Both exist — check hash match
                if cas_sha256 == db_sha256:
                    entry.state = "SEALED_AND_COMMITTED"
                    entry.details = "CAS and DB consistent"
                else:
                    entry.state = "CONFLICT"
                    entry.details = f"hash mismatch: CAS {cas_sha256} vs DB {db_sha256}"

            elif not has_partial and not has_sealed and not db_committed:
                entry.state = "MISSING"
                entry.details = "no CAS or DB record"

            else:
                entry.state = "CONFLICT"
                entry.details = f"unexpected state: partial={has_partial}, sealed={has_sealed}, db={db_committed}"

            results.append(entry)

        return results

    @staticmethod
    def needs_recovery(entry: ReconcileEntry) -> bool:
        """判断一个 reconcile entry 是否需要 RecoveryRecord。"""
        return entry.state not in ("SEALED_AND_COMMITTED", "LIVE_WRITER_ACTIVE")

    @staticmethod
    def can_reconcile_db(entry: ReconcileEntry) -> bool:
        """判断一个 reconcile entry 是否可以安全补 DB。

        只有 SEALED_DB_UNCOMMITTED 且 intent 有效、fence 匹配时才可补。
        """
        return (
            entry.state == "SEALED_DB_UNCOMMITTED"
            and entry.intent_valid
            and entry.current_fence is not None
            and entry.fence_token == entry.current_fence
        )

    def verify_cas_artifact(self, sha256: str) -> bool:
        """验证 CAS 中的 artifact 存在且 hash 匹配。"""
        return self._store.verify(sha256)
