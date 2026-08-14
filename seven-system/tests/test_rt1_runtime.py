"""WP-RT1 Runtime 测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- WorkEvent append + sequence
- lease acquire/renew/release
- outbox delivery + duplicate rejection
- CommitIntent → artifact seal → DB commit → outbox ACK
- CanonicalDBReservationBackend (GV0 ReservationBackendPort)
- RuntimeReconciler CAS/DB two-sided
- Redis projection rebuild from events
- RuntimeCheckpoint + recovery
- DatabaseRuntimeCapabilityReport + ArtifactCommitReconcileCapabilityReport
- RT1 must NOT reissue SchemaStateReport

所有 blocker test 失败 → 工作包 FAIL。
SIDE_EFFECT_FREE：不接触真实 DB、Redis 或 D 盘。
"""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC
from seven_system.contracts.reservation import Allowance, ReservationBackendPort
from seven_system.hashing import canonical_json_bytes
from seven_system.runtime.work_event import (
    WorkEvent,
    WorkEventLog,
    WorkEventError,
)
from seven_system.runtime.lease_fence import (
    Lease,
    LeaseFenceManager,
    LeaseError,
)
from seven_system.runtime.outbox import (
    Outbox,
    OutboxMessage,
    OutboxError,
)
from seven_system.runtime.commit_intent import (
    RuntimeCommitIntent,
    CommitIntentStore,
    CommitIntentError,
)
from seven_system.runtime.db_reservation_backend import (
    CanonicalDBReservationBackend,
    DBReservationError,
)
from seven_system.runtime.reconcile import (
    RuntimeReconciler,
    RuntimeReconcileEntry,
    RuntimeCASRecord,
    RuntimeDBRecord,
    RuntimeIntentRecord,
)
from seven_system.runtime.redis_projection import (
    RedisProjection,
    RedisProjectionError,
)
from seven_system.runtime.checkpoint import (
    RuntimeCheckpoint,
    RuntimeRecoveryReceipt,
    CheckpointManager,
    CheckpointError,
)
from seven_system.runtime.runtime_capability_report import (
    build_database_runtime_capability_report,
    verify_database_runtime_capability_report,
    build_artifact_commit_reconcile_capability_report,
    verify_artifact_commit_reconcile_capability_report,
    CapabilityReportError,
    RUNTIME_REPORT_SCHEMA_VERSION,
    RECONCILE_REPORT_SCHEMA_VERSION,
)

_ZERO_HASH = "0" * 64
_FAKE_HASH_A = "a" * 64
_FAKE_HASH_B = "b" * 64
_FAKE_HASH_C = "c" * 64


def _sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ─── WorkEvent Golden Tests ────────────────────────────────────────────


class TestWorkEventGolden(unittest.TestCase):
    """Golden: WorkEvent append + sequence."""

    def test_append_single_event(self):
        log = WorkEventLog()
        event = WorkEvent.build(
            event_id="evt-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
        )
        log.append(event)
        self.assertEqual(log.length, 1)
        self.assertEqual(log.get_last_sequence("agg-1"), 0)

    def test_append_multiple_events_sequence(self):
        log = WorkEventLog()
        for i in range(5):
            event = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
            )
            log.append(event)
        self.assertEqual(log.length, 5)
        self.assertEqual(log.get_last_sequence("agg-1"), 4)

    def test_append_multiple_aggregates(self):
        log = WorkEventLog()
        for agg in ["agg-1", "agg-2", "agg-3"]:
            event = WorkEvent.build(
                event_id=f"evt-{agg}-0",
                aggregate_id=agg,
                sequence=0,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": "QUEUED"},
            )
            log.append(event)
        self.assertEqual(log.length, 3)
        for agg in ["agg-1", "agg-2", "agg-3"]:
            self.assertEqual(log.get_last_sequence(agg), 0)

    def test_event_to_dict(self):
        event = WorkEvent.build(
            event_id="evt-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
        )
        d = event.to_dict()
        self.assertEqual(d["event_id"], "evt-001")
        self.assertEqual(d["aggregate_id"], "agg-1")
        self.assertEqual(d["sequence"], 0)
        self.assertEqual(d["event_type"], "WORK_ITEM_STATE_CHANGED")
        self.assertEqual(d["fence_token"], 1)
        self.assertEqual(d["payload"], {"state": "QUEUED"})
        # payload_hash should be computed
        self.assertTrue(len(d["payload_hash"]) == 64)

    def test_verify_integrity_pass(self):
        log = WorkEventLog()
        for i in range(3):
            event = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
            )
            log.append(event)
        errors = log.verify_integrity()
        self.assertEqual(errors, [])

    def test_compute_log_hash_deterministic(self):
        log1 = WorkEventLog()
        log2 = WorkEventLog()
        for i in range(3):
            e1 = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            e2 = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            log1.append(e1)
            log2.append(e2)
        self.assertEqual(log1.compute_log_hash(), log2.compute_log_hash())


# ─── WorkEvent Negative Tests ──────────────────────────────────────────


class TestWorkEventNegative(unittest.TestCase):
    """Negative: duplicate event_id, sequence gap, payload hash drift."""

    def test_duplicate_event_id_rejected(self):
        log = WorkEventLog()
        e1 = WorkEvent.build(
            event_id="evt-dup",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
        )
        log.append(e1)
        e2 = WorkEvent.build(
            event_id="evt-dup",
            aggregate_id="agg-1",
            sequence=1,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "LEASED"},
        )
        with self.assertRaises(WorkEventError) as ctx:
            log.append(e2)
        self.assertEqual(ctx.exception.code, EC.WORK_EVENT_DUPLICATE_EVENT_ID)

    def test_sequence_gap_rejected(self):
        log = WorkEventLog()
        e1 = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
        )
        log.append(e1)
        # skip sequence 1, try sequence 2
        e3 = WorkEvent.build(
            event_id="evt-002",
            aggregate_id="agg-1",
            sequence=2,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "PREPARED"},
        )
        with self.assertRaises(WorkEventError) as ctx:
            log.append(e3)
        self.assertEqual(ctx.exception.code, EC.WORK_EVENT_SEQUENCE_GAP)

    def test_first_event_nonzero_sequence_rejected(self):
        log = WorkEventLog()
        event = WorkEvent.build(
            event_id="evt-001",
            aggregate_id="agg-1",
            sequence=5,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
        )
        with self.assertRaises(WorkEventError) as ctx:
            log.append(event)
        self.assertEqual(ctx.exception.code, EC.WORK_EVENT_SEQUENCE_GAP)

    def test_payload_hash_mismatch_rejected(self):
        log = WorkEventLog()
        event = WorkEvent(
            event_id="evt-001",
            aggregate_id="agg-1",
            expected_previous_sequence=-1,
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload_hash="0" * 64,  # wrong hash
            fence_token=1,
            created_at="2026-01-01T00:00:00+00:00",
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
        )
        with self.assertRaises(WorkEventError) as ctx:
            log.append(event)
        self.assertEqual(ctx.exception.code, EC.WORK_EVENT_PAYLOAD_HASH_MISMATCH)

    def test_unknown_event_type_rejected(self):
        log = WorkEventLog()
        event = WorkEvent.build(
            event_id="evt-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="UNKNOWN_TYPE",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
        )
        with self.assertRaises(WorkEventError) as ctx:
            log.append(event)
        self.assertEqual(ctx.exception.code, EC.WORK_EVENT_APPEND_ONLY_VIOLATION)

    def test_100x_redelivery_duplicate_ordinal(self):
        """100x redelivery: duplicate ordinal rejected."""
        backend = CanonicalDBReservationBackend()
        budget = {"database_writes": 1, "tokens": 100}
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget=budget,
        )
        # 100 attempts to reserve the same ordinal
        for _ in range(100):
            with self.assertRaises(DBReservationError) as ctx:
                backend.reserve(
                    permit_id="permit-1",
                    consumption_ordinal=0,
                    idempotency_key="idem-1",
                    fence_token=1,
                    expected_aggregate_revision=1,
                    reserved_budget=budget,
                )
            self.assertEqual(ctx.exception.code, EC.DUPLICATE_ORDINAL)


# ─── Lease/Fence Golden Tests ──────────────────────────────────────────


class TestLeaseFenceGolden(unittest.TestCase):
    """Golden: lease acquire/renew/release."""

    def test_acquire_lease(self):
        mgr = LeaseFenceManager()
        lease = mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        self.assertEqual(lease.lease_id, "lease-1")
        self.assertEqual(lease.state, "ACTIVE")
        self.assertEqual(lease.fence_token, 1)

    def test_renew_lease(self):
        mgr = LeaseFenceManager()
        lease = mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        renewed = mgr.renew(
            lease_id="lease-1",
            fence_token=lease.fence_token,
            ttl_seconds=60,
            current_time="2026-01-01T00:00:30+00:00",
        )
        self.assertEqual(renewed.renew_count, 1)
        self.assertEqual(renewed.state, "ACTIVE")

    def test_release_lease(self):
        mgr = LeaseFenceManager()
        lease = mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        released = mgr.release(
            lease_id="lease-1",
            fence_token=lease.fence_token,
        )
        self.assertEqual(released.state, "RELEASED")

    def test_new_lease_supersedes_old(self):
        mgr = LeaseFenceManager()
        lease1 = mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        lease2 = mgr.acquire(
            lease_id="lease-2",
            aggregate_id="agg-1",
            holder="worker-2",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:10+00:00",
        )
        self.assertEqual(lease1.state, "SUPERSEDED")
        self.assertEqual(lease2.state, "ACTIVE")
        self.assertGreater(lease2.fence_token, lease1.fence_token)

    def test_fence_monotonic_increase(self):
        mgr = LeaseFenceManager()
        fences = []
        for i in range(5):
            lease = mgr.acquire(
                lease_id=f"lease-{i}",
                aggregate_id="agg-1",
                holder=f"worker-{i}",
                ttl_seconds=60,
                current_time="2026-01-01T00:00:00+00:00",
            )
            fences.append(lease.fence_token)
        self.assertEqual(fences, [1, 2, 3, 4, 5])

    def test_check_fence(self):
        mgr = LeaseFenceManager()
        mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        self.assertTrue(mgr.check_fence("agg-1", 1))
        self.assertFalse(mgr.check_fence("agg-1", 0))
        self.assertTrue(mgr.is_stale_fence("agg-1", 0))


# ─── Lease/Fence Negative Tests ────────────────────────────────────────


class TestLeaseFenceNegative(unittest.TestCase):
    """Negative: stale fence, renew with wrong fence, release with wrong fence."""

    def test_stale_fence_renew_rejected(self):
        mgr = LeaseFenceManager()
        lease1 = mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        mgr.acquire(
            lease_id="lease-2",
            aggregate_id="agg-1",
            holder="worker-2",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:10+00:00",
        )
        # old lease tries to renew with stale fence
        with self.assertRaises(LeaseError) as ctx:
            mgr.renew(
                lease_id="lease-1",
                fence_token=lease1.fence_token,
                ttl_seconds=60,
                current_time="2026-01-01T00:00:20+00:00",
            )
        self.assertEqual(ctx.exception.code, EC.LEASE_STALE_FENCE)

    def test_renew_wrong_fence_rejected(self):
        mgr = LeaseFenceManager()
        lease = mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        with self.assertRaises(LeaseError) as ctx:
            mgr.renew(
                lease_id="lease-1",
                fence_token=lease.fence_token + 999,
                ttl_seconds=60,
                current_time="2026-01-01T00:00:30+00:00",
            )
        self.assertEqual(ctx.exception.code, EC.LEASE_RENEW_FENCE_MISMATCH)

    def test_release_wrong_fence_rejected(self):
        mgr = LeaseFenceManager()
        mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        with self.assertRaises(LeaseError) as ctx:
            mgr.release(
                lease_id="lease-1",
                fence_token=999,
            )
        self.assertEqual(ctx.exception.code, EC.LEASE_RELEASE_FENCE_MISMATCH)

    def test_expired_lease_renew_rejected(self):
        mgr = LeaseFenceManager()
        mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        with self.assertRaises(LeaseError) as ctx:
            mgr.renew(
                lease_id="lease-1",
                fence_token=1,
                ttl_seconds=60,
                current_time="2026-01-01T01:00:00+00:00",  # 1 hour later
            )
        self.assertEqual(ctx.exception.code, EC.LEASE_EXPIRED)

    def test_lease_not_found(self):
        mgr = LeaseFenceManager()
        with self.assertRaises(LeaseError) as ctx:
            mgr.release(lease_id="nonexistent", fence_token=1)
        self.assertEqual(ctx.exception.code, EC.LEASE_NOT_FOUND)


# ─── Outbox Golden Tests ───────────────────────────────────────────────


class TestOutboxGolden(unittest.TestCase):
    """Golden: outbox delivery + ACK."""

    def test_append_outbox_message(self):
        outbox = Outbox()
        msg = outbox.append(
            message_id="msg-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"state": "QUEUED"},
        )
        self.assertEqual(msg.state, "PENDING")
        self.assertEqual(msg.unique_key, "agg-1:0")

    def test_deliver_and_ack(self):
        outbox = Outbox()
        outbox.append(
            message_id="msg-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"state": "QUEUED"},
        )
        outbox.deliver("msg-001")
        self.assertEqual(outbox.get_message("msg-001").state, "DELIVERED")
        outbox.ack("msg-001")
        self.assertEqual(outbox.get_message("msg-001").state, "ACKED")

    def test_get_unprojected(self):
        outbox = Outbox()
        outbox.append(
            message_id="msg-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
        )
        outbox.append(
            message_id="msg-002",
            aggregate_id="agg-1",
            sequence=1,
            event_type="WORK_ITEM_STATE_CHANGED",
        )
        outbox.ack("msg-001")
        unprojected = outbox.get_unprojected()
        self.assertEqual(len(unprojected), 1)
        self.assertEqual(unprojected[0].message_id, "msg-002")

    def test_compute_outbox_hash_deterministic(self):
        o1 = Outbox()
        o2 = Outbox()
        for i in range(3):
            o1.append(
                message_id=f"msg-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            o2.append(
                message_id=f"msg-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
        self.assertEqual(o1.compute_outbox_hash(), o2.compute_outbox_hash())


# ─── Outbox Negative Tests ─────────────────────────────────────────────


class TestOutboxNegative(unittest.TestCase):
    """Negative: duplicate unique key, redelivery rejected."""

    def test_duplicate_unique_key_rejected(self):
        outbox = Outbox()
        outbox.append(
            message_id="msg-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
        )
        with self.assertRaises(OutboxError) as ctx:
            outbox.append(
                message_id="msg-002",
                aggregate_id="agg-1",
                sequence=0,  # same unique_key
                event_type="WORK_ITEM_STATE_CHANGED",
            )
        self.assertEqual(ctx.exception.code, EC.OUTBOX_DUPLICATE_KEY)

    def test_redelivery_after_ack_rejected(self):
        outbox = Outbox()
        outbox.append(
            message_id="msg-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
        )
        outbox.deliver("msg-001")
        outbox.ack("msg-001")
        # second ACK rejected
        with self.assertRaises(OutboxError) as ctx:
            outbox.ack("msg-001")
        self.assertEqual(ctx.exception.code, EC.OUTBOX_REDELIVERY_REJECTED)

    def test_deliver_after_ack_rejected(self):
        outbox = Outbox()
        outbox.append(
            message_id="msg-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
        )
        outbox.deliver("msg-001")
        outbox.ack("msg-001")
        with self.assertRaises(OutboxError) as ctx:
            outbox.deliver("msg-001")
        self.assertEqual(ctx.exception.code, EC.OUTBOX_ALREADY_DELIVERED)

    def test_reject_redelivery_method(self):
        outbox = Outbox()
        outbox.append(
            message_id="msg-001",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
        )
        outbox.ack("msg-001")
        self.assertTrue(outbox.reject_redelivery("agg-1:0"))
        self.assertFalse(outbox.reject_redelivery("agg-1:999"))


# ─── CommitIntent Golden Tests ─────────────────────────────────────────


class TestCommitIntentGolden(unittest.TestCase):
    """Golden: CommitIntent record + consume."""

    def test_record_and_consume_intent(self):
        store = CommitIntentStore()
        intent = RuntimeCommitIntent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        store.record(intent)
        consumed = store.consume(
            intent_id="intent-001",
            fence_token=1,
            current_time="2026-01-01T00:30:00+00:00",
            current_fence=1,
        )
        self.assertEqual(consumed.state, "CONSUMED")

    def test_revoke_intent(self):
        store = CommitIntentStore()
        intent = RuntimeCommitIntent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        store.record(intent)
        revoked = store.revoke("intent-001")
        self.assertEqual(revoked.state, "REVOKED")

    def test_verify_intent_pass(self):
        store = CommitIntentStore()
        intent = RuntimeCommitIntent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        store.record(intent)
        errors = store.verify_intent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            target_cas_uri="cas://bundle/abc",
            permit_hash=_ZERO_HASH,
            fence_token=1,
        )
        self.assertEqual(errors, [])


# ─── CommitIntent Negative Tests ───────────────────────────────────────


class TestCommitIntentNegative(unittest.TestCase):
    """Negative: expired, revoked, stale fence, input hash drift."""

    def test_expired_intent_rejected(self):
        store = CommitIntentStore()
        intent = RuntimeCommitIntent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        store.record(intent)
        with self.assertRaises(CommitIntentError) as ctx:
            store.consume(
                intent_id="intent-001",
                fence_token=1,
                current_time="2026-01-01T02:00:00+00:00",  # after expiry
                current_fence=1,
            )
        self.assertEqual(ctx.exception.code, EC.COMMIT_INTENT_EXPIRED)

    def test_revoked_intent_consume_rejected(self):
        store = CommitIntentStore()
        intent = RuntimeCommitIntent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        store.record(intent)
        store.revoke("intent-001")
        with self.assertRaises(CommitIntentError) as ctx:
            store.consume(
                intent_id="intent-001",
                fence_token=1,
                current_time="2026-01-01T00:30:00+00:00",
                current_fence=1,
            )
        self.assertEqual(ctx.exception.code, EC.COMMIT_INTENT_ALREADY_CONSUMED)

    def test_stale_fence_consume_rejected(self):
        store = CommitIntentStore()
        intent = RuntimeCommitIntent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        store.record(intent)
        with self.assertRaises(CommitIntentError) as ctx:
            store.consume(
                intent_id="intent-001",
                fence_token=1,
                current_time="2026-01-01T00:30:00+00:00",
                current_fence=2,  # fence has moved on
            )
        self.assertEqual(ctx.exception.code, EC.COMMIT_INTENT_FENCE_STALE)

    def test_input_hash_drift_detected(self):
        store = CommitIntentStore()
        intent = RuntimeCommitIntent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        store.record(intent)
        errors = store.verify_intent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_B,  # wrong hash
            manifest_hash=_FAKE_HASH_B,
            target_cas_uri="cas://bundle/abc",
            permit_hash=_ZERO_HASH,
            fence_token=1,
        )
        self.assertTrue(any(e[0] == EC.COMMIT_INTENT_INPUT_HASH_DRIFT for e in errors))

    def test_manifest_hash_mismatch_detected(self):
        store = CommitIntentStore()
        intent = RuntimeCommitIntent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        store.record(intent)
        errors = store.verify_intent(
            intent_id="intent-001",
            job_id="job-1",
            attempt_id="attempt-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_C,  # wrong
            target_cas_uri="cas://bundle/abc",
            permit_hash=_ZERO_HASH,
            fence_token=1,
        )
        self.assertTrue(
            any(e[0] == EC.COMMIT_INTENT_MANIFEST_HASH_MISMATCH for e in errors)
        )


# ─── CanonicalDBReservationBackend Golden Tests ────────────────────────


class TestDBReservationBackendGolden(unittest.TestCase):
    """Golden: CanonicalDBReservationBackend implements ReservationBackendPort."""

    def test_backend_kind(self):
        backend = CanonicalDBReservationBackend()
        self.assertEqual(
            backend.backend_kind, "DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER"
        )

    def test_reserve_success(self):
        backend = CanonicalDBReservationBackend()
        result = backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        receipt = result["reservation_transaction_receipt"]
        self.assertEqual(receipt["status"], "RESERVED")
        self.assertEqual(receipt["backend"], "DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER")
        self.assertEqual(receipt["new_aggregate_revision"], 1)

    def test_consume_success(self):
        backend = CanonicalDBReservationBackend()
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        result = backend.consume(
            permit_id="permit-1",
            consumption_ordinal=0,
            fence_token=1,
            actual_side_effects={"database_writes": 1, "tokens": 50},
        )
        self.assertEqual(result["consumption_receipt"]["status"], "CONSUMED")

    def test_release_unused_success(self):
        backend = CanonicalDBReservationBackend()
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        result = backend.release_unused(
            permit_id="permit-1",
            consumption_ordinal=0,
            fence_token=1,
            proof_not_started_refs=[{"ref": "log:dispatch_not_started"}],
        )
        self.assertEqual(result["release_receipt"]["status"], "RELEASED_UNUSED")

    def test_get_state(self):
        backend = CanonicalDBReservationBackend()
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        state = backend.get_state(permit_id="permit-1", consumption_ordinal=0)
        self.assertIsNotNone(state)
        self.assertEqual(state["status"], "RESERVED")

    def test_expected_revision_increments(self):
        backend = CanonicalDBReservationBackend()
        for i in range(3):
            backend.reserve(
                permit_id="permit-1",
                consumption_ordinal=i,
                idempotency_key=f"idem-{i}",
                fence_token=1,
                expected_aggregate_revision=i,
                reserved_budget={"database_writes": 1, "tokens": 100},
            )
        self.assertEqual(backend.get_aggregate_revision("permit-1"), 3)

    def test_implements_reservation_backend_port(self):
        """CanonicalDBReservationBackend implements GV0 ReservationBackendPort."""
        backend = CanonicalDBReservationBackend()
        # Verify it has all required methods
        self.assertTrue(hasattr(backend, "reserve"))
        self.assertTrue(hasattr(backend, "consume"))
        self.assertTrue(hasattr(backend, "release_unused"))
        self.assertTrue(hasattr(backend, "get_state"))
        # Verify method signatures are callable
        self.assertTrue(callable(backend.reserve))
        self.assertTrue(callable(backend.consume))
        self.assertTrue(callable(backend.release_unused))
        self.assertTrue(callable(backend.get_state))


# ─── CanonicalDBReservationBackend Negative Tests ──────────────────────


class TestDBReservationBackendNegative(unittest.TestCase):
    """Negative: duplicate ordinal, stale fence, allowance not conserved."""

    def test_duplicate_ordinal_rejected(self):
        backend = CanonicalDBReservationBackend()
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        with self.assertRaises(DBReservationError) as ctx:
            backend.reserve(
                permit_id="permit-1",
                consumption_ordinal=0,
                idempotency_key="idem-1",
                fence_token=1,
                expected_aggregate_revision=1,
                reserved_budget={"database_writes": 1, "tokens": 100},
            )
        self.assertEqual(ctx.exception.code, EC.DUPLICATE_ORDINAL)

    def test_stale_fence_rejected(self):
        backend = CanonicalDBReservationBackend()
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        # wrong expected revision
        with self.assertRaises(DBReservationError) as ctx:
            backend.reserve(
                permit_id="permit-1",
                consumption_ordinal=1,
                idempotency_key="idem-2",
                fence_token=1,
                expected_aggregate_revision=99,  # wrong
                reserved_budget={"database_writes": 1, "tokens": 100},
            )
        self.assertEqual(ctx.exception.code, EC.STALE_FENCE)

    def test_allowance_not_conserved(self):
        backend = CanonicalDBReservationBackend()
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        with self.assertRaises(DBReservationError) as ctx:
            backend.consume(
                permit_id="permit-1",
                consumption_ordinal=0,
                fence_token=1,
                actual_side_effects={
                    "database_writes": 2,  # exceeds reserved
                    "tokens": 50,
                },
            )
        self.assertEqual(ctx.exception.code, EC.ALLOWANCE_NOT_CONSERVED)

    def test_consume_fence_mismatch(self):
        backend = CanonicalDBReservationBackend()
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        with self.assertRaises(DBReservationError) as ctx:
            backend.consume(
                permit_id="permit-1",
                consumption_ordinal=0,
                fence_token=999,  # wrong
                actual_side_effects={"database_writes": 1, "tokens": 50},
            )
        self.assertEqual(ctx.exception.code, EC.STALE_FENCE)

    def test_release_without_proof_rejected(self):
        backend = CanonicalDBReservationBackend()
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        with self.assertRaises(DBReservationError) as ctx:
            backend.release_unused(
                permit_id="permit-1",
                consumption_ordinal=0,
                fence_token=1,
                proof_not_started_refs=[],  # empty
            )
        self.assertEqual(ctx.exception.code, EC.RELEASE_WITHOUT_PROOF)


# ─── RuntimeReconciler Tests ───────────────────────────────────────────


class TestRuntimeReconciler(unittest.TestCase):
    """Golden + Negative: RuntimeReconciler CAS/DB two-sided."""

    def test_sealed_and_committed_consistent(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=True,
                    artifact_sha256=_FAKE_HASH_A,
                    outbox_state="ACKED",
                )
            },
            intent_records={
                "att-1": RuntimeIntentRecord(
                    intent_id="intent-1",
                    attempt_id="att-1",
                    state="CONSUMED",
                    valid=True,
                    fence_token=1,
                )
            },
            current_fence=1,
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].state, "SEALED_AND_COMMITTED")

    def test_sealed_db_uncommitted_can_reconcile(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=False,
                )
            },
            intent_records={
                "att-1": RuntimeIntentRecord(
                    intent_id="intent-1",
                    attempt_id="att-1",
                    state="PENDING",
                    valid=True,
                    fence_token=1,
                )
            },
            current_fence=1,
        )
        self.assertEqual(results[0].state, "SEALED_DB_UNCOMMITTED")
        self.assertTrue(RuntimeReconciler.can_reconcile_db(results[0]))

    def test_sealed_db_uncommitted_stale_fence(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=False,
                    fence_token=1,
                )
            },
            intent_records={
                "att-1": RuntimeIntentRecord(
                    intent_id="intent-1",
                    attempt_id="att-1",
                    state="PENDING",
                    valid=True,
                    fence_token=1,
                )
            },
            current_fence=5,  # fence has moved on
        )
        self.assertEqual(results[0].state, "STALE_FENCE_LATE_COMMIT")
        self.assertFalse(RuntimeReconciler.can_reconcile_db(results[0]))

    def test_db_committed_artifact_missing(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={},
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=True,
                    artifact_sha256=_FAKE_HASH_A,
                )
            },
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(results[0].state, "DB_COMMITTED_ARTIFACT_MISSING")

    def test_hash_mismatch_conflict(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=True,
                    artifact_sha256=_FAKE_HASH_B,  # different
                    outbox_state="ACKED",
                )
            },
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(results[0].state, "CONFLICT")

    def test_live_writer_active(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_partial=True,
                    writer_alive=True,
                )
            },
            db_records={},
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(results[0].state, "LIVE_WRITER_ACTIVE")

    def test_partial_writer_dead(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_partial=True,
                    writer_alive=False,
                )
            },
            db_records={},
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(results[0].state, "PARTIAL_WRITER_DEAD")

    def test_missing(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={},
            db_records={},
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(len(results), 0)

    def test_commit_intent_missing(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=False,
                )
            },
            intent_records={},  # no intent
            current_fence=1,
        )
        self.assertEqual(results[0].state, "COMMIT_INTENT_MISSING")

    def test_commit_intent_expired(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=False,
                )
            },
            intent_records={
                "att-1": RuntimeIntentRecord(
                    intent_id="intent-1",
                    attempt_id="att-1",
                    state="EXPIRED",
                    valid=False,
                    fence_token=1,
                )
            },
            current_fence=1,
        )
        self.assertEqual(results[0].state, "COMMIT_INTENT_EXPIRED")

    def test_sealed_object_tampered(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                    cas_tampered=True,
                )
            },
            db_records={},
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(results[0].state, "SEALED_OBJECT_TAMPERED")

    def test_outbox_unprojected(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=True,
                    artifact_sha256=_FAKE_HASH_A,
                    outbox_state="PENDING",  # not ACKED
                )
            },
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(results[0].state, "OUTBOX_UNPROJECTED")

    def test_multiple_attempts_claim_success(self):
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                ),
                "att-2": RuntimeCASRecord(
                    attempt_id="att-2",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_B,
                ),
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=True,
                    artifact_sha256=_FAKE_HASH_A,
                    outbox_state="ACKED",
                ),
                "att-2": RuntimeDBRecord(
                    attempt_id="att-2",
                    job_id="job-1",
                    committed=True,
                    artifact_sha256=_FAKE_HASH_B,
                    outbox_state="ACKED",
                ),
            },
            intent_records={},
            current_fence=1,
            attempt_success_claims={"sample-1": ["att-1", "att-2"]},
        )
        for r in results:
            self.assertEqual(r.state, "MULTIPLE_ATTEMPTS_CLAIM_SUCCESS")

    def test_needs_recovery(self):
        self.assertTrue(
            RuntimeReconciler.needs_recovery(
                RuntimeReconcileEntry(
                    attempt_id="a", job_id="j", state="CONFLICT"
                )
            )
        )
        self.assertFalse(
            RuntimeReconciler.needs_recovery(
                RuntimeReconcileEntry(
                    attempt_id="a", job_id="j", state="SEALED_AND_COMMITTED"
                )
            )
        )

    def test_cas_single_side_only(self):
        """Negative: CAS sealed but DB missing (single-side)."""
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={},  # DB has no record
            intent_records={
                "att-1": RuntimeIntentRecord(
                    intent_id="intent-1",
                    attempt_id="att-1",
                    state="PENDING",
                    valid=True,
                    fence_token=1,
                )
            },
            current_fence=1,
        )
        self.assertEqual(results[0].state, "SEALED_DB_UNCOMMITTED")

    def test_db_single_side_only(self):
        """Negative: DB committed but CAS missing (single-side)."""
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={},  # CAS has no record
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=True,
                    artifact_sha256=_FAKE_HASH_A,
                )
            },
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(results[0].state, "DB_COMMITTED_ARTIFACT_MISSING")


# ─── Redis Projection Tests ────────────────────────────────────────────


class TestRedisProjection(unittest.TestCase):
    """Golden + Fault: Redis projection rebuild from events."""

    def test_put_and_get(self):
        proj = RedisProjection()
        proj.put(
            key="test",
            value={"state": "QUEUED"},
            source_event_id="evt-1",
            source_sequence=0,
        )
        entry = proj.get("test")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.value, {"state": "QUEUED"})

    def test_rebuild_from_events(self):
        log = WorkEventLog()
        outbox = Outbox()
        for i in range(3):
            event = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            log.append(event)
            outbox.append(
                message_id=f"msg-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
        proj = RedisProjection()
        proj_hash = proj.rebuild_from_events(event_log=log, outbox=outbox)
        self.assertEqual(proj.state, "REBUILT")
        self.assertEqual(proj.size, 6)  # 3 events + 3 outbox
        self.assertTrue(len(proj_hash) == 64)

    def test_rebuild_deterministic(self):
        log = WorkEventLog()
        outbox = Outbox()
        for i in range(3):
            event = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            log.append(event)
            outbox.append(
                message_id=f"msg-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
        proj1 = RedisProjection()
        hash1 = proj1.rebuild_from_events(event_log=log, outbox=outbox)
        proj2 = RedisProjection()
        hash2 = proj2.rebuild_from_events(event_log=log, outbox=outbox)
        self.assertEqual(hash1, hash2)

    def test_redis_full_loss_rebuild(self):
        """Fault: Redis full loss → rebuild from events."""
        log = WorkEventLog()
        outbox = Outbox()
        for i in range(5):
            event = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            log.append(event)
            outbox.append(
                message_id=f"msg-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
        proj = RedisProjection()
        original_hash = proj.rebuild_from_events(event_log=log, outbox=outbox)
        # Simulate Redis full loss
        proj.clear()
        self.assertEqual(proj.state, "LOST")
        self.assertEqual(proj.size, 0)
        # Rebuild
        rebuilt_hash = proj.rebuild_from_events(event_log=log, outbox=outbox)
        self.assertEqual(proj.state, "REBUILT")
        self.assertEqual(rebuilt_hash, original_hash)

    def test_verify_rebuild_consistency(self):
        log = WorkEventLog()
        outbox = Outbox()
        for i in range(3):
            event = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            log.append(event)
            outbox.append(
                message_id=f"msg-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
        proj = RedisProjection()
        original_hash = proj.rebuild_from_events(event_log=log, outbox=outbox)
        errors = proj.verify_rebuild(
            event_log=log, outbox=outbox, expected_hash=original_hash
        )
        self.assertEqual(errors, [])

    def test_verify_rebuild_hash_mismatch(self):
        log = WorkEventLog()
        outbox = Outbox()
        event = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        log.append(event)
        outbox.append(
            message_id="msg-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        proj = RedisProjection()
        proj.rebuild_from_events(event_log=log, outbox=outbox)
        # Verify with wrong expected hash
        errors = proj.verify_rebuild(
            event_log=log, outbox=outbox, expected_hash="0" * 64
        )
        self.assertTrue(
            any(e[0] == EC.RUNTIME_REDIS_REBUILD_HASH_MISMATCH for e in errors)
        )


# ─── Checkpoint + Recovery Tests ───────────────────────────────────────


class TestCheckpointGolden(unittest.TestCase):
    """Golden: RuntimeCheckpoint + recovery."""

    def test_create_checkpoint(self):
        mgr = CheckpointManager()
        log = WorkEventLog()
        outbox = Outbox()
        lease_mgr = LeaseFenceManager()
        event = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        log.append(event)
        outbox.append(
            message_id="msg-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        lease_mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=3600,
            current_time="2026-01-01T00:00:00+00:00",
        )
        cp = mgr.create_checkpoint(
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            aggregate_revisions={"permit-1": 1},
            created_at="2026-01-01T00:00:00+00:00",
        )
        self.assertEqual(cp.state, "RECORDED")
        self.assertEqual(cp.event_count, 1)
        self.assertEqual(cp.outbox_count, 1)
        self.assertTrue(len(cp.event_log_hash) == 64)

    def test_verify_checkpoint(self):
        mgr = CheckpointManager()
        log = WorkEventLog()
        outbox = Outbox()
        lease_mgr = LeaseFenceManager()
        event = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        log.append(event)
        outbox.append(
            message_id="msg-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        mgr.create_checkpoint(
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            aggregate_revisions={},
            created_at="2026-01-01T00:00:00+00:00",
        )
        cp = mgr.verify_checkpoint(
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
        )
        self.assertEqual(cp.state, "VERIFIED")

    def test_recover_from_checkpoint(self):
        mgr = CheckpointManager()
        log = WorkEventLog()
        outbox = Outbox()
        lease_mgr = LeaseFenceManager()
        event = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        log.append(event)
        outbox.append(
            message_id="msg-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        lease_mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=3600,
            current_time="2026-01-01T00:00:00+00:00",
        )
        mgr.create_checkpoint(
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            aggregate_revisions={"permit-1": 1},
            created_at="2026-01-01T00:00:00+00:00",
        )
        receipt = mgr.recover(
            receipt_id="rec-1",
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            current_time="2026-01-01T00:00:01+00:00",
        )
        self.assertTrue(receipt.is_recovered)
        self.assertTrue(receipt.event_log_verified)
        self.assertEqual(receipt.state, "RECOVERED")

    def test_recover_with_pending_outbox(self):
        """Recovery should redeliver pending outbox messages."""
        mgr = CheckpointManager()
        log = WorkEventLog()
        outbox = Outbox()
        lease_mgr = LeaseFenceManager()
        event = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        log.append(event)
        outbox.append(
            message_id="msg-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        mgr.create_checkpoint(
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            aggregate_revisions={},
            created_at="2026-01-01T00:00:00+00:00",
        )
        receipt = mgr.recover(
            receipt_id="rec-1",
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            current_time="2026-01-01T00:00:01+00:00",
        )
        self.assertIn("msg-000", receipt.outbox_redelivered)

    def test_recover_with_expired_lease(self):
        """Recovery should expire stale leases."""
        mgr = CheckpointManager()
        log = WorkEventLog()
        outbox = Outbox()
        lease_mgr = LeaseFenceManager()
        event = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="scheduler",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        log.append(event)
        outbox.append(
            message_id="msg-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"state": "QUEUED"},
            created_at="2026-01-01T00:00:00+00:00",
        )
        lease_mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=60,
            current_time="2026-01-01T00:00:00+00:00",
        )
        mgr.create_checkpoint(
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            aggregate_revisions={},
            created_at="2026-01-01T00:00:00+00:00",
        )
        # Recover 2 hours later (lease expired)
        receipt = mgr.recover(
            receipt_id="rec-1",
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            current_time="2026-01-01T02:00:00+00:00",
        )
        self.assertIn("lease-1", receipt.leases_expired)


# ─── Capability Report Tests ───────────────────────────────────────────


class TestDatabaseRuntimeCapabilityReport(unittest.TestCase):
    """Golden + Negative: DatabaseRuntimeCapabilityReport."""

    def _build_valid_report(self):
        return build_database_runtime_capability_report(
            site_fingerprint_hash=_FAKE_HASH_A,
            database_identity_hash=_FAKE_HASH_B,
            spec_hash=_FAKE_HASH_C,
            plan_hash=_ZERO_HASH.replace("0", "1"),
            dag_hash=_ZERO_HASH.replace("0", "2"),
            schema_state_report_hash=_ZERO_HASH.replace("0", "3"),
            probe_results=[{"probe_id": "p1", "verdict": "PASS"}],
            positive_evidence_refs=["evidence-1"],
            negative_evidence_refs=["neg-1"],
            residual_risks=["risk-1"],
            verifier_identity="rt1-verifier-v1",
            generated_at="2026-01-01T00:00:00+00:00",
        )

    def test_build_and_verify_pass(self):
        report = self._build_valid_report()
        errors = verify_database_runtime_capability_report(report)
        self.assertEqual(errors, ())

    def test_report_kind(self):
        report = self._build_valid_report()
        self.assertEqual(report["report_kind"], "DatabaseRuntimeCapabilityReport")

    def test_schema_version(self):
        report = self._build_valid_report()
        self.assertEqual(report["schema_version"], RUNTIME_REPORT_SCHEMA_VERSION)

    def test_claims_complete(self):
        report = self._build_valid_report()
        self.assertTrue(len(report["claims"]) > 0)
        self.assertTrue(all(report["claims"].values()))

    def test_side_effects_zero(self):
        report = self._build_valid_report()
        for v in report["side_effects"].values():
            self.assertEqual(v, 0)

    def test_must_not_reissue_schema_state_report(self):
        """Negative: RT1 must NOT reissue SchemaStateReport."""
        report = self._build_valid_report()
        # report_kind must not be DatabaseSchemaStateReport
        self.assertNotEqual(report["report_kind"], "DatabaseSchemaStateReport")
        # Verify a SchemaStateReport report_kind would fail
        bad_report = dict(report)
        bad_report["report_kind"] = "DatabaseSchemaStateReport"
        errors = verify_database_runtime_capability_report(bad_report)
        self.assertTrue(
            any(e[0] == EC.RUNTIME_SCHEMA_STATE_REPORT_REISSUED for e in errors)
        )

    def test_wrong_schema_version_rejected(self):
        report = self._build_valid_report()
        bad = dict(report)
        bad["schema_version"] = "wrong"
        errors = verify_database_runtime_capability_report(bad)
        self.assertTrue(len(errors) > 0)

    def test_non_pass_verdict_rejected(self):
        report = self._build_valid_report()
        bad = dict(report)
        bad["verdict"] = "FAIL"
        errors = verify_database_runtime_capability_report(bad)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_nonzero_side_effects_rejected(self):
        report = self._build_valid_report()
        bad = dict(report)
        bad["side_effects"] = dict(bad["side_effects"])
        bad["side_effects"]["database_writes"] = 1
        errors = verify_database_runtime_capability_report(bad)
        self.assertTrue(any(e[0] == EC.DB1L_WRITE_DETECTED for e in errors))

    def test_missing_checks_rejected(self):
        report = self._build_valid_report()
        bad = dict(report)
        bad["checks"] = []
        errors = verify_database_runtime_capability_report(bad)
        self.assertTrue(len(errors) > 0)

    def test_explicit_nonclaims_preserved(self):
        report = self._build_valid_report()
        self.assertTrue(len(report["explicit_nonclaims"]) > 0)


class TestArtifactCommitReconcileCapabilityReport(unittest.TestCase):
    """Golden + Negative: ArtifactCommitReconcileCapabilityReport."""

    def _build_valid_report(self):
        return build_artifact_commit_reconcile_capability_report(
            site_fingerprint_hash=_FAKE_HASH_A,
            database_identity_hash=_FAKE_HASH_B,
            spec_hash=_FAKE_HASH_C,
            plan_hash=_ZERO_HASH.replace("0", "1"),
            dag_hash=_ZERO_HASH.replace("0", "2"),
            schema_state_report_hash=_ZERO_HASH.replace("0", "3"),
            probe_results=[{"probe_id": "p1", "verdict": "PASS"}],
            positive_evidence_refs=["evidence-1"],
            negative_evidence_refs=["neg-1"],
            residual_risks=["risk-1"],
            verifier_identity="rt1-verifier-v1",
            generated_at="2026-01-01T00:00:00+00:00",
        )

    def test_build_and_verify_pass(self):
        report = self._build_valid_report()
        errors = verify_artifact_commit_reconcile_capability_report(report)
        self.assertEqual(errors, ())

    def test_report_kind(self):
        report = self._build_valid_report()
        self.assertEqual(
            report["report_kind"], "ArtifactCommitReconcileCapabilityReport"
        )

    def test_schema_version(self):
        report = self._build_valid_report()
        self.assertEqual(
            report["schema_version"], RECONCILE_REPORT_SCHEMA_VERSION
        )

    def test_must_not_reissue_schema_state_report(self):
        """Negative: RT1 must NOT reissue SchemaStateReport."""
        report = self._build_valid_report()
        self.assertNotEqual(report["report_kind"], "DatabaseSchemaStateReport")
        bad_report = dict(report)
        bad_report["report_kind"] = "DatabaseSchemaStateReport"
        errors = verify_artifact_commit_reconcile_capability_report(bad_report)
        self.assertTrue(
            any(e[0] == EC.RUNTIME_SCHEMA_STATE_REPORT_REISSUED for e in errors)
        )

    def test_wrong_schema_version_rejected(self):
        report = self._build_valid_report()
        bad = dict(report)
        bad["schema_version"] = "wrong"
        errors = verify_artifact_commit_reconcile_capability_report(bad)
        self.assertTrue(len(errors) > 0)

    def test_side_effects_zero(self):
        report = self._build_valid_report()
        for v in report["side_effects"].values():
            self.assertEqual(v, 0)


# ─── Full Pipeline: CommitIntent → seal → DB commit → outbox ACK ──────


class TestFullPipelineGolden(unittest.TestCase):
    """Golden: CommitIntent → artifact seal → DB commit → outbox ACK."""

    def test_full_commit_pipeline(self):
        """Full pipeline: intent → seal → DB commit → outbox ACK."""
        # Setup
        lease_mgr = LeaseFenceManager()
        intent_store = CommitIntentStore()
        backend = CanonicalDBReservationBackend()
        event_log = WorkEventLog()
        outbox = Outbox()

        # 1. Acquire lease
        lease = lease_mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=3600,
            current_time="2026-01-01T00:00:00+00:00",
        )
        fence = lease.fence_token

        # 2. Reserve permit
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=fence,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )

        # 3. Record CommitIntent
        intent = RuntimeCommitIntent(
            intent_id="intent-1",
            job_id="job-1",
            attempt_id="att-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=fence,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        )
        intent_store.record(intent)

        # 4. Consume CommitIntent (simulates seal)
        intent_store.consume(
            intent_id="intent-1",
            fence_token=fence,
            current_time="2026-01-01T00:30:00+00:00",
            current_fence=fence,
        )

        # 5. Append WorkEvent (COMMIT_COMPLETED)
        event = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="COMMIT_COMPLETED",
            fence_token=fence,
            actor_or_rule="worker-1",
            payload={
                "attempt_id": "att-1",
                "cas_sha256": _FAKE_HASH_A,
                "intent_id": "intent-1",
            },
            created_at="2026-01-01T00:30:00+00:00",
        )
        event_log.append(event)

        # 6. Append outbox (same transaction)
        outbox.append(
            message_id="msg-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="COMMIT_COMPLETED",
            payload={
                "attempt_id": "att-1",
                "cas_sha256": _FAKE_HASH_A,
            },
            created_at="2026-01-01T00:30:00+00:00",
        )

        # 7. Consume permit
        backend.consume(
            permit_id="permit-1",
            consumption_ordinal=0,
            fence_token=fence,
            actual_side_effects={"database_writes": 1, "tokens": 50},
        )

        # 8. Deliver and ACK outbox
        outbox.deliver("msg-000")
        outbox.ack("msg-000")

        # Verify
        self.assertEqual(event_log.length, 1)
        self.assertEqual(outbox.get_message("msg-000").state, "ACKED")
        state = backend.get_state(permit_id="permit-1", consumption_ordinal=0)
        self.assertEqual(state["status"], "CONSUMED")

    def test_full_pipeline_with_checkpoint_and_redis(self):
        """Full pipeline with checkpoint and Redis projection."""
        lease_mgr = LeaseFenceManager()
        intent_store = CommitIntentStore()
        backend = CanonicalDBReservationBackend()
        event_log = WorkEventLog()
        outbox = Outbox()
        cp_mgr = CheckpointManager()
        redis = RedisProjection()

        # Acquire lease
        lease = lease_mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=3600,
            current_time="2026-01-01T00:00:00+00:00",
        )
        fence = lease.fence_token

        # Reserve + record intent
        backend.reserve(
            permit_id="permit-1",
            consumption_ordinal=0,
            idempotency_key="idem-1",
            fence_token=fence,
            expected_aggregate_revision=0,
            reserved_budget={"database_writes": 1, "tokens": 100},
        )
        intent_store.record(RuntimeCommitIntent(
            intent_id="intent-1",
            job_id="job-1",
            attempt_id="att-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=fence,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        ))

        # Event + outbox
        event = WorkEvent.build(
            event_id="evt-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="COMMIT_COMPLETED",
            fence_token=fence,
            actor_or_rule="worker-1",
            payload={"attempt_id": "att-1"},
            created_at="2026-01-01T00:30:00+00:00",
        )
        event_log.append(event)
        outbox.append(
            message_id="msg-000",
            aggregate_id="agg-1",
            sequence=0,
            event_type="COMMIT_COMPLETED",
            payload={"attempt_id": "att-1"},
            created_at="2026-01-01T00:30:00+00:00",
        )
        outbox.ack("msg-000")

        # Build Redis projection
        redis.rebuild_from_events(event_log=event_log, outbox=outbox)
        self.assertEqual(redis.state, "REBUILT")

        # Create checkpoint
        cp = cp_mgr.create_checkpoint(
            checkpoint_id="cp-1",
            event_log=event_log,
            outbox=outbox,
            lease_manager=lease_mgr,
            aggregate_revisions={"permit-1": 1},
            created_at="2026-01-01T00:30:00+00:00",
        )
        self.assertEqual(cp.state, "RECORDED")

        # Verify checkpoint
        cp_mgr.verify_checkpoint(
            checkpoint_id="cp-1",
            event_log=event_log,
            outbox=outbox,
        )
        self.assertEqual(cp.state, "VERIFIED")

        # Simulate Redis loss and rebuild
        redis.clear()
        self.assertEqual(redis.state, "LOST")
        redis.rebuild_from_events(event_log=event_log, outbox=outbox)
        self.assertEqual(redis.state, "REBUILT")


# ─── Fault Injection Tests ─────────────────────────────────────────────


class TestFaultInjection(unittest.TestCase):
    """Fault: crash scenarios and recovery."""

    def test_crash_after_seal_before_db_commit(self):
        """Fault: crash after CAS seal before DB commit → reconcile."""
        reconciler = RuntimeReconciler()
        # CAS sealed, DB not committed, intent valid, fence matches
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=False,
                )
            },
            intent_records={
                "att-1": RuntimeIntentRecord(
                    intent_id="intent-1",
                    attempt_id="att-1",
                    state="PENDING",
                    valid=True,
                    fence_token=1,
                )
            },
            current_fence=1,
        )
        self.assertEqual(results[0].state, "SEALED_DB_UNCOMMITTED")
        # Can reconcile DB
        self.assertTrue(RuntimeReconciler.can_reconcile_db(results[0]))
        # Needs recovery
        self.assertTrue(RuntimeReconciler.needs_recovery(results[0]))

    def test_crash_after_db_commit_before_outbox(self):
        """Fault: crash after DB commit before outbox → reconcile."""
        reconciler = RuntimeReconciler()
        results = reconciler.reconcile(
            cas_records={
                "att-1": RuntimeCASRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    has_sealed=True,
                    cas_sha256=_FAKE_HASH_A,
                )
            },
            db_records={
                "att-1": RuntimeDBRecord(
                    attempt_id="att-1",
                    job_id="job-1",
                    committed=True,
                    artifact_sha256=_FAKE_HASH_A,
                    outbox_state="PENDING",  # outbox not ACKED
                )
            },
            intent_records={},
            current_fence=1,
        )
        self.assertEqual(results[0].state, "OUTBOX_UNPROJECTED")
        # Can rebuild Redis
        self.assertTrue(RuntimeReconciler.can_rebuild_redis(results[0]))

    def test_redis_full_loss_rebuild_from_events(self):
        """Fault: Redis full loss → rebuild from events."""
        log = WorkEventLog()
        outbox = Outbox()
        for i in range(5):
            event = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            log.append(event)
            outbox.append(
                message_id=f"msg-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
        proj = RedisProjection()
        original_hash = proj.rebuild_from_events(event_log=log, outbox=outbox)
        # Simulate full loss
        proj.clear()
        self.assertEqual(proj.state, "LOST")
        # Rebuild
        rebuilt_hash = proj.rebuild_from_events(event_log=log, outbox=outbox)
        self.assertEqual(rebuilt_hash, original_hash)
        self.assertEqual(proj.state, "REBUILT")

    def test_checkpoint_recovery_after_crash(self):
        """Fault: crash → checkpoint recovery."""
        mgr = CheckpointManager()
        log = WorkEventLog()
        outbox = Outbox()
        lease_mgr = LeaseFenceManager()
        for i in range(3):
            event = WorkEvent.build(
                event_id=f"evt-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=1,
                actor_or_rule="scheduler",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
            log.append(event)
            outbox.append(
                message_id=f"msg-{i:03d}",
                aggregate_id="agg-1",
                sequence=i,
                event_type="WORK_ITEM_STATE_CHANGED",
                payload={"state": f"STATE_{i}"},
                created_at="2026-01-01T00:00:00+00:00",
            )
        lease_mgr.acquire(
            lease_id="lease-1",
            aggregate_id="agg-1",
            holder="worker-1",
            ttl_seconds=3600,
            current_time="2026-01-01T00:00:00+00:00",
        )
        mgr.create_checkpoint(
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            aggregate_revisions={"permit-1": 1},
            created_at="2026-01-01T00:00:00+00:00",
        )
        # Simulate crash + recovery
        receipt = mgr.recover(
            receipt_id="rec-1",
            checkpoint_id="cp-1",
            event_log=log,
            outbox=outbox,
            lease_manager=lease_mgr,
            current_time="2026-01-01T00:00:01+00:00",
        )
        self.assertTrue(receipt.is_recovered)
        self.assertTrue(receipt.event_log_verified)
        # All 3 outbox messages should be redelivered
        self.assertEqual(len(receipt.outbox_redelivered), 3)

    def test_stale_commit_rejected(self):
        """Negative: stale commit (fence has moved) rejected."""
        store = CommitIntentStore()
        store.record(RuntimeCommitIntent(
            intent_id="intent-1",
            job_id="job-1",
            attempt_id="att-1",
            input_hash=_FAKE_HASH_A,
            manifest_hash=_FAKE_HASH_B,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://bundle/abc",
            authorization_hash=_FAKE_HASH_C,
            permit_hash=_ZERO_HASH,
            fence_token=1,
            expiry="2026-01-01T01:00:00+00:00",
            created_at="2026-01-01T00:00:00+00:00",
        ))
        # fence has moved to 2, intent has 1
        with self.assertRaises(CommitIntentError) as ctx:
            store.consume(
                intent_id="intent-1",
                fence_token=1,
                current_time="2026-01-01T00:30:00+00:00",
                current_fence=2,
            )
        self.assertEqual(ctx.exception.code, EC.COMMIT_INTENT_FENCE_STALE)


# ─── RT1 Boundary Tests ────────────────────────────────────────────────


class TestRT1Boundary(unittest.TestCase):
    """RT1 boundary: must NOT reissue SchemaStateReport."""

    def test_rt1_allowed_output_kinds(self):
        from seven_system.contracts.errors import RT1_ALLOWED_OUTPUT_KINDS
        self.assertIn("DatabaseRuntimeCapabilityReport", RT1_ALLOWED_OUTPUT_KINDS)
        self.assertIn("ArtifactCommitReconcileCapabilityReport", RT1_ALLOWED_OUTPUT_KINDS)
        self.assertIn("RuntimeCheckpoint", RT1_ALLOWED_OUTPUT_KINDS)
        self.assertIn("RuntimeRecoveryReceipt", RT1_ALLOWED_OUTPUT_KINDS)

    def test_rt1_forbidden_output_kinds(self):
        from seven_system.contracts.errors import RT1_FORBIDDEN_OUTPUT_KINDS
        self.assertIn("DatabaseSchemaStateReport", RT1_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SchemaBootstrapReceipt", RT1_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SchemaBootstrapImportAnchor", RT1_FORBIDDEN_OUTPUT_KINDS)

    def test_rt1_does_not_produce_schema_state_report(self):
        """RT1 must NOT reissue SchemaStateReport."""
        # Verify that RT1 report builders don't produce SchemaStateReport
        report = build_database_runtime_capability_report(
            site_fingerprint_hash=_FAKE_HASH_A,
            database_identity_hash=_FAKE_HASH_B,
            spec_hash=_FAKE_HASH_C,
            plan_hash=_ZERO_HASH.replace("0", "1"),
            dag_hash=_ZERO_HASH.replace("0", "2"),
            schema_state_report_hash=_ZERO_HASH.replace("0", "3"),
            probe_results=[],
            positive_evidence_refs=[],
            negative_evidence_refs=[],
            residual_risks=[],
            verifier_identity="rt1-verifier-v1",
            generated_at="2026-01-01T00:00:00+00:00",
        )
        self.assertNotEqual(report["report_kind"], "DatabaseSchemaStateReport")

        report2 = build_artifact_commit_reconcile_capability_report(
            site_fingerprint_hash=_FAKE_HASH_A,
            database_identity_hash=_FAKE_HASH_B,
            spec_hash=_FAKE_HASH_C,
            plan_hash=_ZERO_HASH.replace("0", "1"),
            dag_hash=_ZERO_HASH.replace("0", "2"),
            schema_state_report_hash=_ZERO_HASH.replace("0", "3"),
            probe_results=[],
            positive_evidence_refs=[],
            negative_evidence_refs=[],
            residual_risks=[],
            verifier_identity="rt1-verifier-v1",
            generated_at="2026-01-01T00:00:00+00:00",
        )
        self.assertNotEqual(report2["report_kind"], "DatabaseSchemaStateReport")

    def test_rt1_nonclaims_mention_schema_boundary(self):
        report = build_database_runtime_capability_report(
            site_fingerprint_hash=_FAKE_HASH_A,
            database_identity_hash=_FAKE_HASH_B,
            spec_hash=_FAKE_HASH_C,
            plan_hash=_ZERO_HASH.replace("0", "1"),
            dag_hash=_ZERO_HASH.replace("0", "2"),
            schema_state_report_hash=_ZERO_HASH.replace("0", "3"),
            probe_results=[],
            positive_evidence_refs=[],
            negative_evidence_refs=[],
            residual_risks=[],
            verifier_identity="rt1-verifier-v1",
            generated_at="2026-01-01T00:00:00+00:00",
        )
        # claims should include does_not_reissue_schema_state_report
        self.assertIn("does_not_reissue_schema_state_report", report["claims"])
        self.assertTrue(report["claims"]["does_not_reissue_schema_state_report"])


# ─── RT1 Constants Tests ───────────────────────────────────────────────


class TestRT1Constants(unittest.TestCase):
    """Verify RT1 constants are properly defined."""

    def test_work_event_types(self):
        from seven_system.contracts.errors import WORK_EVENT_TYPES
        self.assertIn("WORK_ITEM_STATE_CHANGED", WORK_EVENT_TYPES)
        self.assertIn("COMMIT_COMPLETED", WORK_EVENT_TYPES)
        self.assertIn("OUTBOX_APPENDED", WORK_EVENT_TYPES)

    def test_lease_states(self):
        from seven_system.contracts.errors import LEASE_STATES
        self.assertIn("ACTIVE", LEASE_STATES)
        self.assertIn("RELEASED", LEASE_STATES)
        self.assertIn("SUPERSEDED", LEASE_STATES)

    def test_outbox_states(self):
        from seven_system.contracts.errors import OUTBOX_STATES
        self.assertIn("PENDING", OUTBOX_STATES)
        self.assertIn("ACKED", OUTBOX_STATES)

    def test_commit_intent_states(self):
        from seven_system.contracts.errors import COMMIT_INTENT_STATES
        self.assertIn("PENDING", COMMIT_INTENT_STATES)
        self.assertIn("CONSUMED", COMMIT_INTENT_STATES)

    def test_rt1_reconcile_states(self):
        from seven_system.contracts.errors import RT1_RECONCILE_STATES
        self.assertIn("SEALED_DB_UNCOMMITTED", RT1_RECONCILE_STATES)
        self.assertIn("OUTBOX_UNPROJECTED", RT1_RECONCILE_STATES)
        self.assertIn("STALE_FENCE_LATE_COMMIT", RT1_RECONCILE_STATES)
        self.assertIn("COMMIT_INTENT_MISSING", RT1_RECONCILE_STATES)
        self.assertIn("MULTIPLE_ATTEMPTS_CLAIM_SUCCESS", RT1_RECONCILE_STATES)

    def test_runtime_checkpoint_states(self):
        from seven_system.contracts.errors import RUNTIME_CHECKPOINT_STATES
        self.assertIn("RECORDED", RUNTIME_CHECKPOINT_STATES)
        self.assertIn("VERIFIED", RUNTIME_CHECKPOINT_STATES)
        self.assertIn("RECOVERED", RUNTIME_CHECKPOINT_STATES)

    def test_redis_projection_states(self):
        from seven_system.contracts.errors import REDIS_PROJECTION_STATES
        self.assertIn("FRESH", REDIS_PROJECTION_STATES)
        self.assertIn("LOST", REDIS_PROJECTION_STATES)
        self.assertIn("REBUILT", REDIS_PROJECTION_STATES)


if __name__ == "__main__":
    unittest.main()
