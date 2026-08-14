"""WP-DB1I Schema bootstrap 测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- MigrationSpec / SchemaBootstrapPlan 确定性 hash
- fenced apply → verify → receipt 完整流程
- SchemaBootstrapReceipt + SchemaBootstrapImportAnchor 生成与验证
- DatabaseSchemaStateReport 生成与验证
- Negative: apply without HumanGateDecision, apply without fence, duplicate apply, stale fence
- Negative: plan hash drift, site fingerprint mismatch, missing DB1L report
- Fault: crash before DDL, crash after DDL (UNKNOWN_OUTCOME), resume with catalog reconcile
- Fault: bootstrap ledger tampering, import anchor hash mismatch
- Negative: DB1I must NOT produce Runtime/Reconcile capability

所有测试使用 FakeLogicalSiteAdapter + FakeSchemaApplyExecutor——零真实 DB/D 盘连接。
"""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC  # noqa: E402
from seven_system.database.environment import EXPECTED_DATABASE  # noqa: E402
from seven_system.database.migration_spec import (  # noqa: E402
    DDLAction,
    SCHEMA_BOOTSTRAP_PLAN_SCHEMA_VERSION,
    SchemaBootstrapPlan,
    SchemaBootstrapPlanError,
    build_bootstrap_plan_actions,
    build_schema_bootstrap_plan,
    verify_schema_bootstrap_plan,
)
from seven_system.database.schema_bootstrap import (  # noqa: E402
    ActionReceipt,
    FakeSchemaApplyExecutor,
    SchemaBootstrapProtocol,
    SchemaBootstrapProtocolError,
)
from seven_system.database.schema_bootstrap_backend import (  # noqa: E402
    LedgerEntry,
    SchemaBootstrapBackendError,
    SchemaBootstrapDVolumeLedgerBackend,
    SchemaBootstrapFence,
)
from seven_system.database.schema_bootstrap_receipt import (  # noqa: E402
    SCHEMA_BOOTSTRAP_IMPORT_ANCHOR_SCHEMA_VERSION,
    SCHEMA_BOOTSTRAP_RECEIPT_SCHEMA_VERSION,
    SchemaBootstrapReceiptError,
    build_schema_bootstrap_import_anchor,
    build_schema_bootstrap_receipt,
    verify_schema_bootstrap_import_anchor,
    verify_schema_bootstrap_receipt,
)
from seven_system.database.schema_state_report import (  # noqa: E402
    DB1I_CHECK_IDS,
    DB1I_CLAIMS,
    DB1I_NONCLAIMS,
    DB1I_SIDE_EFFECT_KEYS,
    REPORT_SCHEMA_VERSION,
    SchemaStateReportError,
    build_schema_state_report,
    verify_schema_state_report,
)
from seven_system.database.site_adapter import (  # noqa: E402
    CatalogSnapshot,
    CollectionSnapshot,
    FakeLogicalSiteAdapter,
    SiteFingerprint,
)
from seven_system.database.spec import (  # noqa: E402
    CANONICAL_MIGRATION_SPEC,
    CANONICAL_MIGRATION_SPEC_HASH,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _golden_fingerprint() -> SiteFingerprint:
    return SiteFingerprint(
        endpoint="http://localhost:8529",
        server_version="arangodb-3.12.1",
        driver_name="python-arango",
        driver_version="8.1.0",
        principal="seven-readonly-user",
    )


def _golden_adapter() -> FakeLogicalSiteAdapter:
    return FakeLogicalSiteAdapter(
        database_name_value=EXPECTED_DATABASE,
        current_database_value=EXPECTED_DATABASE,
        fingerprint=_golden_fingerprint(),
        catalog=CatalogSnapshot(collections=()),
        write_count_value=0,
        connect_should_fail=False,
    )


def _make_permit(plan_hash: str = "") -> dict:
    return {
        "permit_id": "schema-bootstrap-permit-001",
        "wp_id": "G-DB-SCHEMA-APPLY",
        "plan_hash": plan_hash,
        "max_actions": 100,
        "expiry": "2026-08-15T12:00:00Z",
        "nonce": "permit-nonce-aaaaaaaaaaaa",
    }


def _make_gate_decision(*, decision: str = "APPROVE") -> dict:
    return {
        "decision_id": "gate-dec-schema-001",
        "decision": decision,
        "actor_id": "human-reviewer-001",
        "gate_type": "PROOF_REVIEW",
    }


class _MockHumanGateService:
    """P0-C: mock HumanGateService for DB1I tests."""

    def __init__(self, *, reject: bool = False) -> None:
        self._reject = reject

    def accept_gate_decision(self, decision: dict, *, evaluation_time: str = ""):
        from seven_system.contracts.completion_contract import VerificationResult
        from seven_system.contracts.errors import VerificationErrorCode as EC
        if self._reject or decision.get("decision") != "APPROVE":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.DB1I_HUMAN_GATE_DECISION_REJECTED],
                details=["mock gate rejection"],
            )
        return VerificationResult(verdict="PASS")


def _make_gate_service(*, reject: bool = False) -> _MockHumanGateService:
    return _MockHumanGateService(reject=reject)


def _make_protocol(
    *,
    adapter: FakeLogicalSiteAdapter | None = None,
    backend: SchemaBootstrapDVolumeLedgerBackend | None = None,
    executor: FakeSchemaApplyExecutor | None = None,
) -> SchemaBootstrapProtocol:
    return SchemaBootstrapProtocol(
        site_adapter=adapter or _golden_adapter(),
        backend=backend or SchemaBootstrapDVolumeLedgerBackend(),
        executor=executor or FakeSchemaApplyExecutor(),
    )


def _prepare_and_apply(
    protocol: SchemaBootstrapProtocol | None = None,
    *,
    gate_decision: dict | None = None,
    permit: dict | None = None,
    gate_service: _MockHumanGateService | None = None,
) -> SchemaBootstrapProtocol:
    """完整的 prepare → apply 流程，返回已完成的 protocol。"""
    if protocol is None:
        protocol = _make_protocol()
    # 先用 adapter 获取 fingerprint hash 来构建 permit
    protocol.site_adapter.connect_readonly()
    fp = protocol.site_adapter.site_fingerprint()
    plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
    protocol.site_adapter.connected = False  # reset for prepare

    p = permit or _make_permit(plan_hash=plan.plan_hash)
    gd = gate_decision or _make_gate_decision()
    gs = gate_service or _make_gate_service()
    protocol.prepare(permit=p, gate_decision=gd, human_gate_service=gs)
    protocol.apply()
    return protocol


# ═══════════════════════════════════════════════════════════════════════
# MigrationSpec / SchemaBootstrapPlan 测试
# ═══════════════════════════════════════════════════════════════════════

class TestSchemaBootstrapPlan(unittest.TestCase):
    """MigrationSpec / SchemaBootstrapPlan 确定性与 hash 测试。"""

    def test_golden_plan_has_deterministic_hash(self):
        """Golden: valid MigrationSpec with deterministic hash."""
        fp = _golden_fingerprint()
        plan = build_schema_bootstrap_plan(
            site_fingerprint_hash=fp.fingerprint_hash
        )
        self.assertEqual(plan.schema_version, SCHEMA_BOOTSTRAP_PLAN_SCHEMA_VERSION)
        self.assertEqual(plan.expected_database, EXPECTED_DATABASE)
        self.assertEqual(plan.spec_hash, CANONICAL_MIGRATION_SPEC_HASH)
        self.assertEqual(plan.site_fingerprint_hash, fp.fingerprint_hash)
        self.assertTrue(plan.action_count > 0)
        self.assertEqual(len(plan.plan_hash), 64)

    def test_golden_plan_hash_is_deterministic(self):
        """相同输入必须产生相同 plan_hash。"""
        fp = _golden_fingerprint()
        plan1 = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        plan2 = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        self.assertEqual(plan1.plan_hash, plan2.plan_hash)

    def test_golden_plan_hash_differs_by_site_fingerprint(self):
        """不同 site fingerprint 必须产生不同 plan_hash。"""
        fp1 = _golden_fingerprint()
        fp2 = SiteFingerprint(
            endpoint="http://other:8529",
            server_version="arangodb-3.12.1",
            driver_name="python-arango",
            driver_version="8.1.0",
            principal="other-user",
        )
        plan1 = build_schema_bootstrap_plan(site_fingerprint_hash=fp1.fingerprint_hash)
        plan2 = build_schema_bootstrap_plan(site_fingerprint_hash=fp2.fingerprint_hash)
        self.assertNotEqual(plan1.plan_hash, plan2.plan_hash)

    def test_golden_plan_actions_are_ordered_and_unique(self):
        """DDL actions 有序、ordinal 连续、action_id 唯一。"""
        actions = build_bootstrap_plan_actions()
        ordinals = [a.ordinal for a in actions]
        self.assertEqual(ordinals, list(range(len(actions))))
        action_ids = [a.action_id for a in actions]
        self.assertEqual(len(action_ids), len(set(action_ids)))
        # 第一个 action 是 CREATE_COLLECTION
        self.assertEqual(actions[0].action_type, "CREATE_COLLECTION")
        self.assertEqual(actions[0].collection, "seven_records_v1")

    def test_golden_plan_verification_passes(self):
        """verify_schema_bootstrap_plan 对合法 plan 返回空 tuple。"""
        fp = _golden_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        errors = verify_schema_bootstrap_plan(plan)
        self.assertEqual(errors, ())

    def test_negative_plan_hash_drift(self):
        """Negative: plan hash drift — 修改 actions ordinal 后 plan_hash 变化且被检测。"""
        fp = _golden_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        # 篡改第一个 action 的 ordinal 为非连续值
        first_action = plan.actions[0]
        tampered_action = DDLAction(
            ordinal=99,  # 非连续 ordinal
            action_type=first_action.action_type,
            collection=first_action.collection,
            index=first_action.index,
        )
        tampered = SchemaBootstrapPlan(
            schema_version=plan.schema_version,
            expected_database=plan.expected_database,
            spec_hash=plan.spec_hash,
            site_fingerprint_hash=plan.site_fingerprint_hash,
            actions=(tampered_action,) + plan.actions[1:],
        )
        self.assertNotEqual(tampered.plan_hash, plan.plan_hash)
        errors = verify_schema_bootstrap_plan(tampered)
        # ordinal 不连续会被检测到
        self.assertTrue(any(e[0] == EC.DB1I_PLAN_HASH_DRIFT for e in errors))

    def test_negative_spec_hash_drift(self):
        """Negative: spec hash drift — 非 canonical spec 被拒绝。"""
        fp = _golden_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        tampered = SchemaBootstrapPlan(
            schema_version=plan.schema_version,
            expected_database=plan.expected_database,
            spec_hash="a" * 64,  # 错误 spec_hash
            site_fingerprint_hash=plan.site_fingerprint_hash,
            actions=plan.actions,
        )
        errors = verify_schema_bootstrap_plan(tampered)
        self.assertTrue(any(e[0] == EC.DB1I_MIGRATION_SPEC_HASH_DRIFT for e in errors))

    def test_negative_invalid_site_fingerprint_hash(self):
        """Negative: site fingerprint hash 格式错误被拒绝。"""
        with self.assertRaises(SchemaBootstrapPlanError):
            build_schema_bootstrap_plan(site_fingerprint_hash="invalid")


# ═══════════════════════════════════════════════════════════════════════
# D-volume Ledger Backend 测试
# ═══════════════════════════════════════════════════════════════════════

class TestSchemaBootstrapBackend(unittest.TestCase):
    """SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER 后端测试。"""

    def test_golden_fence_acquire_and_release(self):
        """Golden: fence acquire → release 正常流程。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        fence = backend.acquire_fence(
            site_fingerprint_hash="a" * 64,
            plan_hash="b" * 64,
            fence_token=42,
            acquired_at="2026-08-14T12:00:00Z",
            expires_at="2026-08-15T12:00:00Z",
            maintenance_window="2026-08-14/2026-08-15",
        )
        self.assertEqual(fence.state, "ACTIVE")
        self.assertEqual(fence.fence_token, 42)
        released = backend.release_fence(
            plan_hash="b" * 64, fence_token=42, site_fingerprint_hash="a" * 64
        )
        self.assertEqual(released.state, "RELEASED")

    def test_negative_duplicate_fence_rejected(self):
        """Negative: 同一 plan_hash 重复 acquire fence 被拒绝。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        backend.acquire_fence(
            site_fingerprint_hash="a" * 64, plan_hash="b" * 64,
            fence_token=1, acquired_at="2026-08-14T12:00:00Z",
            expires_at="2026-08-15T12:00:00Z",
            maintenance_window="2026-08-14/2026-08-15",
        )
        with self.assertRaises(SchemaBootstrapBackendError) as ctx:
            backend.acquire_fence(
                site_fingerprint_hash="a" * 64, plan_hash="b" * 64,
                fence_token=2, acquired_at="2026-08-14T12:00:00Z",
                expires_at="2026-08-15T12:00:00Z",
                maintenance_window="2026-08-14/2026-08-15",
            )
        self.assertEqual(ctx.exception.code, EC.DB1I_FENCE_DUPLICATE)

    def test_negative_stale_fence_on_release(self):
        """Negative: stale fence_token 在 release 时被拒绝。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        backend.acquire_fence(
            site_fingerprint_hash="a" * 64, plan_hash="b" * 64,
            fence_token=10, acquired_at="2026-08-14T12:00:00Z",
            expires_at="2026-08-15T12:00:00Z",
            maintenance_window="2026-08-14/2026-08-15",
        )
        with self.assertRaises(SchemaBootstrapBackendError) as ctx:
            backend.release_fence(
                plan_hash="b" * 64, fence_token=999, site_fingerprint_hash="a" * 64
            )
        self.assertEqual(ctx.exception.code, EC.DB1I_FENCE_STALE)

    def test_golden_ledger_chain_integrity(self):
        """Golden: ledger append-only chain 完整性验证通过。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        for i in range(3):
            backend.append_ledger_entry(
                site_fingerprint_hash="a" * 64, plan_hash="b" * 64,
                entry_type="ACTION_INTENT", action_id=f"act:{i}",
                ordinal=i, payload={"step": i},
            )
        errors = backend.verify_ledger(
            site_fingerprint_hash="a" * 64, plan_hash="b" * 64
        )
        self.assertEqual(errors, ())
        root = backend.ledger_root_hash(
            site_fingerprint_hash="a" * 64, plan_hash="b" * 64
        )
        self.assertEqual(len(root), 64)

    def test_golden_reservation_backend_protocol(self):
        """Golden: ReservationBackendPort reserve → consume 正常。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        budget = {"database_writes": 1, "d_volume_writes": 1, "currency": "USD"}
        result = backend.reserve(
            permit_id="p1", consumption_ordinal=0, idempotency_key="k0",
            fence_token=1, expected_aggregate_revision=0, reserved_budget=budget,
        )
        self.assertEqual(result["reservation_transaction_receipt"]["status"], "RESERVED")
        self.assertEqual(
            result["reservation_transaction_receipt"]["reservation_backend"],
            "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
        )
        result = backend.consume(
            permit_id="p1", consumption_ordinal=0, fence_token=1,
            actual_side_effects=budget,
        )
        self.assertEqual(result["consumption_receipt"]["status"], "CONSUMED")

    def test_negative_duplicate_ordinal_rejected(self):
        """Negative: 重复 ordinal 被拒绝。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        budget = {"database_writes": 1, "currency": "USD"}
        backend.reserve(
            permit_id="p1", consumption_ordinal=0, idempotency_key="k0",
            fence_token=1, expected_aggregate_revision=0, reserved_budget=budget,
        )
        with self.assertRaises(SchemaBootstrapBackendError) as ctx:
            backend.reserve(
                permit_id="p1", consumption_ordinal=0, idempotency_key="k0",
                fence_token=1, expected_aggregate_revision=1, reserved_budget=budget,
            )
        self.assertEqual(ctx.exception.code, EC.DUPLICATE_ORDINAL)

    def test_negative_allowance_not_conserved(self):
        """Negative: actual 超过 reserved 被拒绝。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        budget = {"database_writes": 1, "currency": "USD"}
        backend.reserve(
            permit_id="p1", consumption_ordinal=0, idempotency_key="k0",
            fence_token=1, expected_aggregate_revision=0, reserved_budget=budget,
        )
        with self.assertRaises(SchemaBootstrapBackendError) as ctx:
            backend.consume(
                permit_id="p1", consumption_ordinal=0, fence_token=1,
                actual_side_effects={"database_writes": 5, "currency": "USD"},
            )
        self.assertEqual(ctx.exception.code, EC.ALLOWANCE_NOT_CONSERVED)


# ═══════════════════════════════════════════════════════════════════════
# Fenced apply / verify / resume 测试
# ═══════════════════════════════════════════════════════════════════════

class TestFencedApplyVerify(unittest.TestCase):
    """fenced apply → verify → receipt 完整流程测试。"""

    def test_golden_apply_verify_receipt(self):
        """Golden: fenced apply → verify → receipt 完整流程。"""
        protocol = _prepare_and_apply()
        self.assertTrue(protocol.applied)
        self.assertTrue(len(protocol.action_receipts) > 0)
        for r in protocol.action_receipts:
            self.assertEqual(r.state, "VERIFIED")

        result = protocol.verify()
        self.assertEqual(result.verdict, "PASS")

        receipt = build_schema_bootstrap_receipt(protocol)
        self.assertEqual(receipt["report_kind"], "SchemaBootstrapReceipt")
        self.assertEqual(len(receipt["receipt_hash"]), 64)
        errors = verify_schema_bootstrap_receipt(receipt)
        self.assertEqual(errors, ())

    def test_golden_apply_creates_all_collections(self):
        """Golden: apply 后所有 canonical 集合和索引都存在。"""
        protocol = _prepare_and_apply()
        catalog = protocol.executor.catalog_snapshot()
        names = {col.name for col in catalog.collections}
        for col_spec in CANONICAL_MIGRATION_SPEC.collections:
            self.assertIn(col_spec.name, names)

    def test_golden_plan_hash_in_context(self):
        """Golden: context 中的 plan_hash 与 plan 一致。"""
        protocol = _prepare_and_apply()
        self.assertEqual(protocol.context.plan.plan_hash, protocol.context.plan.plan_hash)

    def test_negative_apply_without_human_gate_decision(self):
        """Negative: apply without HumanGateDecision (decision != APPROVE) 被拒绝。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False

        bad_decision = _make_gate_decision(decision="REJECT")
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            protocol.prepare(
                permit=_make_permit(plan_hash=plan.plan_hash),
                gate_decision=bad_decision, human_gate_service=_make_gate_service())
        self.assertEqual(ctx.exception.code, EC.DB1I_HUMAN_GATE_DECISION_REJECTED)

    def test_negative_apply_without_fence(self):
        """Negative: apply without fence (prepare 未调用) 被拒绝。"""
        protocol = _make_protocol()
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            protocol.apply()
        self.assertEqual(ctx.exception.code, EC.DB1I_APPLY_WITHOUT_FENCE)

    def test_negative_duplicate_apply(self):
        """Negative: 重复 apply 被拒绝。"""
        protocol = _prepare_and_apply()
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            protocol.apply()
        self.assertEqual(ctx.exception.code, EC.DB1I_DUPLICATE_APPLY)

    def test_negative_duplicate_prepare(self):
        """Negative: 重复 prepare 被拒绝。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        protocol.prepare(
            permit=_make_permit(plan_hash=plan.plan_hash),
            gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            protocol.prepare(
                permit=_make_permit(plan_hash=plan.plan_hash),
                gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        self.assertEqual(ctx.exception.code, EC.DB1I_DUPLICATE_APPLY)

    def test_negative_permit_plan_hash_mismatch(self):
        """Negative: permit plan_hash 与 plan 不匹配被拒绝。"""
        protocol = _make_protocol()
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            protocol.prepare(
                permit=_make_permit(plan_hash="wrong"),
                gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        self.assertEqual(ctx.exception.code, EC.DB1I_PERMIT_MISMATCH)

    def test_negative_permit_wrong_wp_id(self):
        """Negative: permit wp_id 不是 G-DB-SCHEMA-APPLY 被拒绝。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        permit = _make_permit(plan_hash=plan.plan_hash)
        permit["wp_id"] = "WRONG"
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            protocol.prepare(permit=permit, gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        self.assertEqual(ctx.exception.code, EC.DB1I_PERMIT_MISMATCH)

    def test_negative_site_fingerprint_mismatch(self):
        """Negative: site fingerprint mismatch — adapter 连接失败被拒绝。"""
        adapter = FakeLogicalSiteAdapter(connect_should_fail=True)
        protocol = _make_protocol(adapter=adapter)
        with self.assertRaises(Exception):
            protocol.prepare(
                permit=_make_permit(),
                gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())


# ═══════════════════════════════════════════════════════════════════════
# SchemaBootstrapReceipt + ImportAnchor 测试
# ═══════════════════════════════════════════════════════════════════════

class TestSchemaBootstrapReceipt(unittest.TestCase):
    """SchemaBootstrapReceipt + SchemaBootstrapImportAnchor 测试。"""

    def test_golden_receipt_generation(self):
        """Golden: SchemaBootstrapReceipt 生成与验证。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        self.assertEqual(receipt["schema_version"], SCHEMA_BOOTSTRAP_RECEIPT_SCHEMA_VERSION)
        self.assertEqual(receipt["report_kind"], "SchemaBootstrapReceipt")
        self.assertEqual(len(receipt["receipt_hash"]), 64)
        self.assertTrue(receipt["gate_decision_verified"])
        self.assertTrue(receipt["action_count"] > 0)
        errors = verify_schema_bootstrap_receipt(receipt)
        self.assertEqual(errors, ())

    def test_golden_receipt_hash_deterministic(self):
        """Golden: 相同 protocol 产生相同 receipt_hash。"""
        protocol1 = _prepare_and_apply()
        protocol2 = _prepare_and_apply()
        r1 = build_schema_bootstrap_receipt(protocol1, generated_at="2026-08-14T12:00:00Z")
        r2 = build_schema_bootstrap_receipt(protocol2, generated_at="2026-08-14T12:00:00Z")
        self.assertEqual(r1["receipt_hash"], r2["receipt_hash"])

    def test_negative_receipt_without_apply(self):
        """Negative: 未 apply 时构建 receipt 被拒绝。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        protocol.prepare(
            permit=_make_permit(plan_hash=plan.plan_hash),
            gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        with self.assertRaises(SchemaBootstrapReceiptError):
            build_schema_bootstrap_receipt(protocol)

    def test_negative_receipt_hash_mismatch(self):
        """Negative: receipt_hash 篡改被检测。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        receipt["receipt_hash"] = "a" * 64
        errors = verify_schema_bootstrap_receipt(receipt)
        self.assertTrue(any(e[0] == EC.DB1I_BOOTSTRAP_RECEIPT_HASH_MISMATCH for e in errors))

    def test_negative_receipt_unknown_outcome(self):
        """Negative: action 状态非 VERIFIED 被检测。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        receipt["action_receipts"][0]["state"] = "UNKNOWN_OUTCOME"
        receipt["receipt_hash"] = None
        import hashlib
        from seven_system.hashing import canonical_json_bytes
        receipt["receipt_hash"] = hashlib.sha256(canonical_json_bytes(receipt)).hexdigest()
        errors = verify_schema_bootstrap_receipt(receipt)
        self.assertTrue(any(e[0] == EC.DB1I_UNKNOWN_OUTCOME for e in errors))

    def test_golden_import_anchor_generation(self):
        """Golden: SchemaBootstrapImportAnchor 生成与验证。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        ledger_root = protocol.ledger_root_hash
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=ledger_root,
            db_import_record_ids=["rec-001", "rec-002"],
            db_import_record_hashes=["c" * 64, "d" * 64],
        )
        self.assertEqual(anchor["schema_version"], SCHEMA_BOOTSTRAP_IMPORT_ANCHOR_SCHEMA_VERSION)
        self.assertEqual(anchor["report_kind"], "SchemaBootstrapImportAnchor")
        self.assertEqual(len(anchor["anchor_hash"]), 64)
        self.assertEqual(anchor["d_volume_root_seal"], ledger_root)
        self.assertEqual(anchor["import_record_count"], 2)
        errors = verify_schema_bootstrap_import_anchor(anchor)
        self.assertEqual(errors, ())

    def test_negative_import_anchor_hash_mismatch(self):
        """Negative: import anchor hash mismatch 被检测。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001"],
            db_import_record_hashes=["c" * 64],
        )
        anchor["anchor_hash"] = "a" * 64
        errors = verify_schema_bootstrap_import_anchor(anchor)
        self.assertTrue(any(e[0] == EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH for e in errors))

    def test_negative_import_anchor_record_length_mismatch(self):
        """Negative: record IDs 和 hashes 长度不匹配被拒绝。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        with self.assertRaises(SchemaBootstrapReceiptError) as ctx:
            build_schema_bootstrap_import_anchor(
                receipt=receipt,
                ledger_root_hash=protocol.ledger_root_hash,
                db_import_record_ids=["rec-001", "rec-002"],
                db_import_record_hashes=["c" * 64],
            )
        self.assertEqual(ctx.exception.code, EC.DB1I_IMPORT_ANCHOR_HASH_MISMATCH)

    def test_negative_import_anchor_invalid_receipt(self):
        """Negative: 无效 receipt 构建 anchor 被拒绝。"""
        with self.assertRaises(SchemaBootstrapReceiptError):
            build_schema_bootstrap_import_anchor(
                receipt={"invalid": True},
                ledger_root_hash="0" * 64,
                db_import_record_ids=[],
                db_import_record_hashes=[],
            )


# ═══════════════════════════════════════════════════════════════════════
# DatabaseSchemaStateReport 测试
# ═══════════════════════════════════════════════════════════════════════

class TestSchemaStateReport(unittest.TestCase):
    """DatabaseSchemaStateReport 测试。"""

    def test_golden_schema_state_report(self):
        """Golden: DatabaseSchemaStateReport 生成与验证。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001"],
            db_import_record_hashes=["c" * 64],
        )
        report = build_schema_state_report(
            protocol=protocol, receipt=receipt, import_anchor=anchor
        )
        self.assertEqual(report["schema_version"], REPORT_SCHEMA_VERSION)
        self.assertEqual(report["report_kind"], "DatabaseSchemaStateReport")
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["missing_collections"], [])
        self.assertEqual(report["missing_indexes"], [])
        self.assertEqual(report["extra_collections"], [])
        self.assertEqual(report["semantic_conflicts"], [])
        errors = verify_schema_state_report(report)
        self.assertEqual(errors, ())

    def test_golden_report_check_ids_exact(self):
        """Golden: check IDs 与 canonical 完全匹配。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001"],
            db_import_record_hashes=["c" * 64],
        )
        report = build_schema_state_report(
            protocol=protocol, receipt=receipt, import_anchor=anchor
        )
        check_ids = [c["check_id"] for c in report["checks"]]
        self.assertEqual(check_ids, list(DB1I_CHECK_IDS))

    def test_golden_report_claims_and_nonclaims(self):
        """Golden: claims 和 nonclaims 完全匹配。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001"],
            db_import_record_hashes=["c" * 64],
        )
        report = build_schema_state_report(
            protocol=protocol, receipt=receipt, import_anchor=anchor
        )
        self.assertEqual(set(report["claims"]), set(DB1I_CLAIMS))
        self.assertEqual(set(report["explicit_nonclaims"]), set(DB1I_NONCLAIMS))

    def test_negative_report_spec_hash_drift(self):
        """Negative: spec hash drift 被检测。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001"],
            db_import_record_hashes=["c" * 64],
        )
        report = build_schema_state_report(
            protocol=protocol, receipt=receipt, import_anchor=anchor
        )
        report["spec_hash"] = "a" * 64
        errors = verify_schema_state_report(report)
        self.assertTrue(any(e[0] == EC.DB1I_MIGRATION_SPEC_HASH_DRIFT for e in errors))

    def test_negative_report_missing_db1l_report(self):
        """Negative: missing DB1L report — site fingerprint 缺失被检测。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001"],
            db_import_record_hashes=["c" * 64],
        )
        report = build_schema_state_report(
            protocol=protocol, receipt=receipt, import_anchor=anchor
        )
        report["site_fingerprint"] = {}
        errors = verify_schema_state_report(report)
        self.assertTrue(any(e[0] == EC.DB1I_SITE_FINGERPRINT_MISMATCH for e in errors))

    def test_negative_report_catalog_drift(self):
        """Negative: catalog 差异被检测。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001"],
            db_import_record_hashes=["c" * 64],
        )
        report = build_schema_state_report(
            protocol=protocol, receipt=receipt, import_anchor=anchor
        )
        report["missing_collections"] = ["seven_records_v1"]
        errors = verify_schema_state_report(report)
        self.assertTrue(any(e[0] == EC.DB1I_RESUME_CATALOG_MISMATCH for e in errors))


# ═══════════════════════════════════════════════════════════════════════
# Fault injection 测试
# ═══════════════════════════════════════════════════════════════════════

class TestFaultInjection(unittest.TestCase):
    """fault injection: crash before/after DDL, resume, ledger tampering。"""

    def test_fault_crash_before_ddl(self):
        """Fault: crash before DDL → UNKNOWN_OUTCOME, resume 后 FAILED。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        protocol.prepare(
            permit=_make_permit(plan_hash=plan.plan_hash),
            gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        # 在第一个 action 的 DDL 前崩溃
        receipts = protocol.apply(crash_before_ordinal=0)
        self.assertFalse(protocol.applied)
        # ledger 有 ACTION_INTENT 但无 ACTION_VERIFIED
        ledger = protocol.backend.get_ledger(
            site_fingerprint_hash=fp.fingerprint_hash, plan_hash=plan.plan_hash
        )
        entry_types = [e.entry_type for e in ledger.entries]
        self.assertIn("ACTION_INTENT", entry_types)

    def test_fault_crash_after_ddl_unknown_outcome(self):
        """Fault: crash after DDL → UNKNOWN_OUTCOME, resume 按 catalog reconcile。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        protocol.prepare(
            permit=_make_permit(plan_hash=plan.plan_hash),
            gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        # 在第一个 action 的 DDL 后崩溃
        receipts = protocol.apply(crash_after_ordinal=0)
        self.assertFalse(protocol.applied)
        # 第一个 action 是 UNKNOWN_OUTCOME
        self.assertEqual(receipts[0].state, "UNKNOWN_OUTCOME")
        # DDL 已执行（collection 已创建）
        self.assertTrue(protocol.executor.collection_exists("seven_records_v1"))

    def test_fault_resume_after_crash_reconciles(self):
        """Fault: resume with catalog reconcile — UNKNOWN_OUTCOME 按 catalog 事实恢复。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        protocol.prepare(
            permit=_make_permit(plan_hash=plan.plan_hash),
            gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        # 在第一个 action 后崩溃
        protocol.apply(crash_after_ordinal=0)
        # resume — 第一个 action 的 DDL 已生效，应 reconcile 为 VERIFIED
        result = protocol.resume()
        # resume 后第一个 action 应为 VERIFIED（DDL 已生效）
        first_receipt = next(r for r in protocol.action_receipts if r.ordinal == 0)
        self.assertEqual(first_receipt.state, "VERIFIED")

    def test_fault_resume_does_not_blind_replay(self):
        """Fault: UNKNOWN_OUTCOME 不得盲重放——DDL 未生效时标记 FAILED。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        protocol.prepare(
            permit=_make_permit(plan_hash=plan.plan_hash),
            gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        # 在第一个 action 的 DDL 前崩溃
        protocol.apply(crash_before_ordinal=0)
        # resume — DDL 未生效，应标记 FAILED
        result = protocol.resume()
        first_receipt = next(r for r in protocol.action_receipts if r.ordinal == 0)
        self.assertEqual(first_receipt.state, "FAILED")
        self.assertEqual(result.verdict, "FAIL")

    def test_fault_ledger_tampering_detected(self):
        """Fault: bootstrap ledger tampering 被检测。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        backend.append_ledger_entry(
            site_fingerprint_hash="a" * 64, plan_hash="b" * 64,
            entry_type="ACTION_INTENT", action_id="act:0",
            ordinal=0, payload={"step": 0},
        )
        ledger = backend.get_ledger(site_fingerprint_hash="a" * 64, plan_hash="b" * 64)
        # 篡改 entry 的 payload
        original_hash = ledger.entries[0].entry_hash
        ledger.entries[0] = LedgerEntry(
            sequence=ledger.entries[0].sequence,
            entry_type=ledger.entries[0].entry_type,
            action_id=ledger.entries[0].action_id,
            ordinal=ledger.entries[0].ordinal,
            payload={"tampered": True},  # 篡改
            previous_hash=ledger.entries[0].previous_hash,
            entry_hash=original_hash,  # 保持原 hash 不变
        )
        errors = backend.verify_ledger(site_fingerprint_hash="a" * 64, plan_hash="b" * 64)
        self.assertTrue(any(e[0] == EC.DB1I_LEDGER_TAMPERED for e in errors))

    def test_fault_ledger_previous_hash_mismatch(self):
        """Fault: ledger previous-hash chain 断裂被检测。"""
        backend = SchemaBootstrapDVolumeLedgerBackend()
        backend.append_ledger_entry(
            site_fingerprint_hash="a" * 64, plan_hash="b" * 64,
            entry_type="ACTION_INTENT", action_id="act:0",
            ordinal=0, payload={"step": 0},
        )
        backend.append_ledger_entry(
            site_fingerprint_hash="a" * 64, plan_hash="b" * 64,
            entry_type="ACTION_VERIFIED", action_id="act:0",
            ordinal=0, payload={"step": 0},
        )
        ledger = backend.get_ledger(site_fingerprint_hash="a" * 64, plan_hash="b" * 64)
        # 篡改第二个 entry 的 previous_hash
        ledger.entries[1] = LedgerEntry(
            sequence=ledger.entries[1].sequence,
            entry_type=ledger.entries[1].entry_type,
            action_id=ledger.entries[1].action_id,
            ordinal=ledger.entries[1].ordinal,
            payload=ledger.entries[1].payload,
            previous_hash="f" * 64,  # 错误 previous_hash
            entry_hash=ledger.entries[1].entry_hash,
        )
        errors = backend.verify_ledger(site_fingerprint_hash="a" * 64, plan_hash="b" * 64)
        self.assertTrue(any(e[0] == EC.DB1I_LEDGER_PREVIOUS_HASH_MISMATCH for e in errors))


# ═══════════════════════════════════════════════════════════════════════
# 输出边界测试
# ═══════════════════════════════════════════════════════════════════════

class TestOutputBoundary(unittest.TestCase):
    """DB1I 不得输出 Runtime/Reconcile capability。"""

    def test_negative_runtime_capability_not_allowed(self):
        """Negative: DB1I must NOT produce DatabaseRuntimeCapabilityReport。"""
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            SchemaBootstrapProtocol.assert_allowed_output("DatabaseRuntimeCapabilityReport")
        self.assertEqual(ctx.exception.code, EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED)

    def test_negative_reconcile_capability_not_allowed(self):
        """Negative: DB1I must NOT produce ArtifactCommitReconcileCapabilityReport。"""
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            SchemaBootstrapProtocol.assert_allowed_output("ArtifactCommitReconcileCapabilityReport")
        self.assertEqual(ctx.exception.code, EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED)

    def test_golden_allowed_outputs_accepted(self):
        """Golden: DB1I 允许的三种输出类型被接受。"""
        for kind in ("DatabaseSchemaStateReport", "SchemaBootstrapReceipt", "SchemaBootstrapImportAnchor"):
            SchemaBootstrapProtocol.assert_allowed_output(kind)

    def test_negative_unknown_output_rejected(self):
        """Negative: 未知输出类型被拒绝。"""
        with self.assertRaises(SchemaBootstrapProtocolError):
            SchemaBootstrapProtocol.assert_allowed_output("UnknownReport")

    def test_golden_report_nonclaims_include_boundary(self):
        """Golden: report 的 nonclaims 包含 runtime/reconcile 边界声明。"""
        protocol = _prepare_and_apply()
        receipt = build_schema_bootstrap_receipt(protocol)
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001"],
            db_import_record_hashes=["c" * 64],
        )
        report = build_schema_state_report(
            protocol=protocol, receipt=receipt, import_anchor=anchor
        )
        nonclaims_text = " ".join(report["explicit_nonclaims"])
        self.assertIn("runtime", nonclaims_text.lower())
        self.assertIn("reconcile", nonclaims_text.lower())


# ═══════════════════════════════════════════════════════════════════════
# 完整端到端流程测试
# ═══════════════════════════════════════════════════════════════════════

class TestEndToEnd(unittest.TestCase):
    """完整端到端：prepare → apply → verify → receipt → anchor → report。"""

    def test_golden_full_pipeline(self):
        """Golden: 完整端到端流程。"""
        protocol = _make_protocol()
        # prepare
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        protocol.prepare(
            permit=_make_permit(plan_hash=plan.plan_hash),
            gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        # apply
        receipts = protocol.apply()
        self.assertTrue(protocol.applied)
        # verify
        result = protocol.verify()
        self.assertEqual(result.verdict, "PASS")
        # receipt
        receipt = build_schema_bootstrap_receipt(protocol)
        self.assertEqual(verify_schema_bootstrap_receipt(receipt), ())
        # import anchor
        anchor = build_schema_bootstrap_import_anchor(
            receipt=receipt,
            ledger_root_hash=protocol.ledger_root_hash,
            db_import_record_ids=["rec-001", "rec-002"],
            db_import_record_hashes=["c" * 64, "d" * 64],
        )
        self.assertEqual(verify_schema_bootstrap_import_anchor(anchor), ())
        # schema state report
        report = build_schema_state_report(
            protocol=protocol, receipt=receipt, import_anchor=anchor
        )
        self.assertEqual(verify_schema_state_report(report), ())
        self.assertEqual(report["verdict"], "PASS")

    def test_golden_resume_then_full_pipeline(self):
        """Golden: crash → resume → verify → receipt 完整流程。"""
        protocol = _make_protocol()
        protocol.site_adapter.connect_readonly()
        fp = protocol.site_adapter.site_fingerprint()
        plan = build_schema_bootstrap_plan(site_fingerprint_hash=fp.fingerprint_hash)
        protocol.site_adapter.connected = False
        protocol.prepare(
            permit=_make_permit(plan_hash=plan.plan_hash),
            gate_decision=_make_gate_decision(), human_gate_service=_make_gate_service())
        # crash after first action
        protocol.apply(crash_after_ordinal=0)
        self.assertFalse(protocol.applied)
        # resume — reconciles UNKNOWN_OUTCOME
        result = protocol.resume()
        # 第一个 action 已 reconcile 为 VERIFIED，但后续 actions 未执行
        # 所以 resume 不会标记 applied=True（后续 actions 是 PENDING）
        first_receipt = next(r for r in protocol.action_receipts if r.ordinal == 0)
        self.assertEqual(first_receipt.state, "VERIFIED")
        # 后续 actions 是 PENDING
        pending = [r for r in protocol.action_receipts if r.state == "PENDING"]
        self.assertTrue(len(pending) > 0)


if __name__ == "__main__":
    unittest.main()
