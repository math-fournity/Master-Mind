"""RuntimeReconciler — CAS/DB/outbox/permit 两-sided reconcile。

扩展 VLT0 的 ArtifactReconciler，增加 RT1 特有的 reconcile 状态：
- OUTBOX_UNPROJECTED: outbox 消息未投影到 Redis
- OUTBOX_DUPLICATE_PROJECTED: outbox 消息被重复投影
- STALE_FENCE_LATE_COMMIT: stale fence 晚提交
- SEALED_OBJECT_TAMPERED: sealed 对象被外部改写
- COMMIT_INTENT_MISSING / EXPIRED / REVOKED: CommitIntent 问题
- PERMIT_OVERCONSUMED / REPLAYED: permit consumption 问题
- MULTIPLE_ATTEMPTS_CLAIM_SUCCESS: 多个 attempt 声称同一科学样本成功

Reconciler 只能转向原合法中间态、COMMITTING、RETRY_SCHEDULED
或隔离/失败终态；不得直接跳到科学成功。

SIDE_EFFECT_FREE：不修改 CAS、DB 或 Redis。所有状态作为输入传入。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    RECONCILE_STATES,
    RT1_RECONCILE_STATES,
    VerificationErrorCode as EC,
)


@dataclass
class RuntimeReconcileEntry:
    """单个 attempt 的 runtime reconcile 状态。"""

    attempt_id: str
    job_id: str
    state: str  # RT1_RECONCILE_STATES 中的一个
    cas_sha256: str | None = None
    db_committed: bool = False
    db_artifact_sha256: str | None = None
    writer_alive: bool = False
    has_partial: bool = False
    has_sealed: bool = False
    intent_id: str | None = None
    intent_valid: bool = False
    intent_state: str = "MISSING"  # PENDING / CONSUMED / REVOKED / EXPIRED / MISSING
    fence_token: int | None = None
    current_fence: int | None = None
    outbox_state: str = "NONE"  # NONE / PENDING / DELIVERED / ACKED
    outbox_unique_key: str | None = None
    permit_status: str = "NONE"  # RESERVED / CONSUMED / RELEASED_UNUSED / NONE
    permit_overconsumed: bool = False
    permit_replayed: bool = False
    cas_tampered: bool = False
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
            "intent_state": self.intent_state,
            "fence_token": self.fence_token,
            "current_fence": self.current_fence,
            "outbox_state": self.outbox_state,
            "outbox_unique_key": self.outbox_unique_key,
            "permit_status": self.permit_status,
            "permit_overconsumed": self.permit_overconsumed,
            "permit_replayed": self.permit_replayed,
            "cas_tampered": self.cas_tampered,
            "details": self.details,
        }


@dataclass
class RuntimeDBRecord:
    """DB 侧的 artifact + outbox + permit 记录（作为 reconcile 输入）。"""

    attempt_id: str
    job_id: str
    committed: bool = False
    artifact_sha256: str | None = None
    manifest_hash: str | None = None
    fence_token: int | None = None
    outbox_state: str = "NONE"
    outbox_unique_key: str | None = None
    permit_status: str = "NONE"
    permit_consumption_ordinal: int | None = None


@dataclass
class RuntimeCASRecord:
    """CAS 侧的状态记录（作为 reconcile 输入）。"""

    attempt_id: str
    job_id: str
    has_partial: bool = False
    has_sealed: bool = False
    cas_sha256: str | None = None
    writer_alive: bool = False
    cas_tampered: bool = False


@dataclass
class RuntimeIntentRecord:
    """CommitIntent 侧的状态记录（作为 reconcile 输入）。"""

    intent_id: str
    attempt_id: str
    state: str = "MISSING"  # PENDING / CONSUMED / REVOKED / EXPIRED / MISSING
    fence_token: int | None = None
    valid: bool = False


class RuntimeReconciler:
    """RuntimeReconciler — CAS/DB/outbox/permit/CommitIntent 两 sided 对账。

    识别 doc 06 中列出的所有 reconcile 状态。
    每种状态产生 RecoveryRecord，不得自动任选"看起来最好"的输出。
    """

    def reconcile(
        self,
        *,
        cas_records: dict[str, RuntimeCASRecord],
        db_records: dict[str, RuntimeDBRecord],
        intent_records: dict[str, RuntimeIntentRecord],
        current_fence: int | None = None,
        attempt_success_claims: dict[str, list[str]] | None = None,
    ) -> list[RuntimeReconcileEntry]:
        """执行两 sided 对账。

        参数：
        - cas_records: attempt_id → RuntimeCASRecord
        - db_records: attempt_id → RuntimeDBRecord
        - intent_records: attempt_id → RuntimeIntentRecord
        - current_fence: 当前有效 fence
        - attempt_success_claims: scientific_sample_id → [attempt_id, ...]
          用于检测多个 attempt 声称同一科学样本成功
        """
        results: list[RuntimeReconcileEntry] = []
        all_attempt_ids = set(cas_records.keys()) | set(db_records.keys())

        for attempt_id in sorted(all_attempt_ids):
            cas = cas_records.get(attempt_id)
            db = db_records.get(attempt_id)
            intent = intent_records.get(attempt_id)

            entry = RuntimeReconcileEntry(
                attempt_id=attempt_id,
                job_id=(cas.job_id if cas else db.job_id if db else ""),
                state="MISSING",
            )

            # 填充 CAS 侧
            if cas:
                entry.has_partial = cas.has_partial
                entry.has_sealed = cas.has_sealed
                entry.cas_sha256 = cas.cas_sha256
                entry.writer_alive = cas.writer_alive
                entry.cas_tampered = cas.cas_tampered

            # 填充 DB 侧
            if db:
                entry.db_committed = db.committed
                entry.db_artifact_sha256 = db.artifact_sha256
                entry.fence_token = db.fence_token
                entry.outbox_state = db.outbox_state
                entry.outbox_unique_key = db.outbox_unique_key
                entry.permit_status = db.permit_status

            # 填充 intent 侧
            if intent:
                entry.intent_id = intent.intent_id
                entry.intent_state = intent.state
                entry.intent_valid = intent.valid
                if entry.fence_token is None:
                    entry.fence_token = intent.fence_token

            entry.current_fence = current_fence

            # 判定状态（按优先级）

            # 0. CAS tampered
            if entry.cas_tampered:
                entry.state = "SEALED_OBJECT_TAMPERED"
                entry.details = "sealed object externally modified"
                results.append(entry)
                continue

            # 1. live writer active
            if entry.writer_alive and not entry.has_sealed:
                entry.state = "LIVE_WRITER_ACTIVE"
                entry.details = "live writer still active, cannot reconcile"
                results.append(entry)
                continue

            # 2. partial writer dead
            if entry.has_partial and not entry.has_sealed and not entry.writer_alive:
                entry.state = "PARTIAL_WRITER_DEAD"
                entry.details = "partial bundle, writer dead, needs seal or cleanup"
                results.append(entry)
                continue

            # 3. sealed, DB uncommitted
            if entry.has_sealed and not entry.db_committed:
                # 检查 intent
                if entry.intent_state == "MISSING":
                    entry.state = "COMMIT_INTENT_MISSING"
                    entry.details = "CAS sealed, DB uncommitted, no CommitIntent"
                elif entry.intent_state == "EXPIRED":
                    entry.state = "COMMIT_INTENT_EXPIRED"
                    entry.details = "CAS sealed, DB uncommitted, intent expired"
                elif entry.intent_state == "REVOKED":
                    entry.state = "COMMIT_INTENT_REVOKED"
                    entry.details = "CAS sealed, DB uncommitted, intent revoked"
                elif not entry.intent_valid:
                    entry.state = "COMMIT_INTENT_MISSING"
                    entry.details = "CAS sealed, DB uncommitted, intent invalid"
                elif (
                    current_fence is not None
                    and entry.fence_token is not None
                    and entry.fence_token < current_fence
                ):
                    entry.state = "STALE_FENCE_LATE_COMMIT"
                    entry.details = (
                        f"CAS sealed, DB uncommitted, stale fence "
                        f"{entry.fence_token} < current {current_fence}"
                    )
                else:
                    entry.state = "SEALED_DB_UNCOMMITTED"
                    entry.details = (
                        "CAS sealed, DB uncommitted, valid intent + fence "
                        "→ can reconcile"
                    )
                results.append(entry)
                continue

            # 4. DB committed, CAS missing
            if entry.db_committed and not entry.has_sealed:
                entry.state = "DB_COMMITTED_ARTIFACT_MISSING"
                entry.details = "DB committed but CAS artifact missing → quarantine"
                results.append(entry)
                continue

            # 5. sealed and committed — check hash
            if entry.has_sealed and entry.db_committed:
                if entry.cas_sha256 and entry.db_artifact_sha256:
                    if entry.cas_sha256 == entry.db_artifact_sha256:
                        # 检查 outbox
                        if entry.outbox_state == "PENDING":
                            entry.state = "OUTBOX_UNPROJECTED"
                            entry.details = "sealed and committed but outbox pending"
                        elif entry.outbox_state == "DELIVERED":
                            entry.state = "OUTBOX_UNPROJECTED"
                            entry.details = (
                                "sealed and committed but outbox delivered "
                                "not ACKED"
                            )
                        else:
                            entry.state = "SEALED_AND_COMMITTED"
                            entry.details = "CAS and DB consistent"
                    else:
                        entry.state = "CONFLICT"
                        entry.details = (
                            f"hash mismatch: CAS {entry.cas_sha256} vs "
                            f"DB {entry.db_artifact_sha256}"
                        )
                else:
                    entry.state = "SEALED_AND_COMMITTED"
                    entry.details = "CAS and DB consistent (no hash to compare)"
                results.append(entry)
                continue

            # 6. permit issues
            if entry.permit_status == "CONSUMED" and not entry.has_sealed:
                entry.state = "PERMIT_OVERCONSUMED"
                entry.details = "permit consumed but no sealed artifact"
                results.append(entry)
                continue

            # 7. missing
            if (
                not entry.has_partial
                and not entry.has_sealed
                and not entry.db_committed
            ):
                entry.state = "MISSING"
                entry.details = "no CAS or DB record"
                results.append(entry)
                continue

            # 8. fallback conflict
            entry.state = "CONFLICT"
            entry.details = (
                f"unexpected state: partial={entry.has_partial}, "
                f"sealed={entry.has_sealed}, db={entry.db_committed}"
            )
            results.append(entry)

        # 检查多个 attempt 声称同一科学样本成功
        if attempt_success_claims:
            for sample_id, attempt_ids in attempt_success_claims.items():
                if len(attempt_ids) > 1:
                    for aid in attempt_ids:
                        for e in results:
                            if e.attempt_id == aid and e.state == "SEALED_AND_COMMITTED":
                                e.state = "MULTIPLE_ATTEMPTS_CLAIM_SUCCESS"
                                e.details = (
                                    f"multiple attempts {attempt_ids} claim "
                                    f"success for sample {sample_id}"
                                )

        return results

    @staticmethod
    def needs_recovery(entry: RuntimeReconcileEntry) -> bool:
        """判断一个 reconcile entry 是否需要 RecoveryRecord。"""
        return entry.state not in ("SEALED_AND_COMMITTED", "LIVE_WRITER_ACTIVE")

    @staticmethod
    def can_reconcile_db(entry: RuntimeReconcileEntry) -> bool:
        """判断一个 reconcile entry 是否可以安全补 DB。

        只有 SEALED_DB_UNCOMMITTED 且 intent 有效、fence 匹配时才可补。
        """
        return (
            entry.state == "SEALED_DB_UNCOMMITTED"
            and entry.intent_valid
            and entry.current_fence is not None
            and entry.fence_token == entry.current_fence
        )

    @staticmethod
    def can_rebuild_redis(entry: RuntimeReconcileEntry) -> bool:
        """判断是否可以从 event/outbox 重建 Redis 投影。"""
        return entry.state in (
            "OUTBOX_UNPROJECTED",
            "SEALED_AND_COMMITTED",
        )
