"""WP-DB1I fenced Schema bootstrap apply/verify/resume 协议。

实现 docs/implementation/06-storage-database-and-eventing.md 的
"Schema bootstrap：Seven 集合尚不存在时"协议：

1. 只读 catalog 生成 deterministic plan，冻结 site/DB/principal/spec/catalog/plan hash
2. G-DB-SCHEMA-APPLY 产生 LiveRunPermit（maintenance window、max actions、expiry、nonce）
3. D 盘 atomic create 建立唯一 SchemaBootstrapFence；竞争者 BLOCK
4. 每个 DDL 前 append+fsync ACTION_INTENT，执行后 append+fsync catalog observation +
   ACTION_VERIFIED/ACTION_FAILED/UNKNOWN_OUTCOME；每个 entry 包含 previous-entry hash
5. resume 时重读整条 ledger 与实 site catalog；UNKNOWN_OUTCOME 不得盲重放 DDL，
   必须按 catalog 事实 reconcile
6. 全部 actions 验证后生成 SchemaBootstrapReceipt + root-seal
7. seven_schema_migrations_v1 可用后导入 plan/events/receipts → SchemaBootstrapImportAnchor

消费关系：
- DB1L LogicalSiteAdapter → site fingerprint
- GV0 ReservationBackendPort → SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER 原子预留
- HG0 HumanGateService → HumanGateDecision 验证
- VLT0 CAS → bootstrap ledger（D-volume ledger backend 已内含）

硬约束：
- apply 前必须有 HumanGateDecision（APPROVE）
- apply 前必须有 fence
- 重复 apply 拒绝
- stale fence 拒绝
- UNKNOWN_OUTCOME 不得盲重放
- 不得输出 DatabaseRuntimeCapabilityReport / ArtifactCommitReconcileCapabilityReport

SIDE_EFFECT_FREE：DDL 由注入的 executor 在内存中模拟，不接触真实 DB/D 盘。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Protocol

from ..contracts.errors import (
    DB1I_ALLOWED_OUTPUT_KINDS,
    DB1I_FORBIDDEN_OUTPUT_KINDS,
    SCHEMA_BOOTSTRAP_ACTION_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..hashing import object_hash
from .migration_spec import (
    DDLAction,
    SchemaBootstrapPlan,
    build_schema_bootstrap_plan,
    verify_schema_bootstrap_plan,
)
from .schema_bootstrap_backend import (
    SchemaBootstrapBackendError,
    SchemaBootstrapDVolumeLedgerBackend,
    SchemaBootstrapFence,
)
from .site_adapter import (
    CatalogSnapshot,
    CollectionSnapshot,
    FakeLogicalSiteAdapter,
    LogicalSiteAdapter,
    SiteFingerprint,
)


class SchemaApplyExecutor(Protocol):
    """DDL 执行器协议——SIDE_EFFECT_FREE 测试用内存实现。

    真实实现会通过 fenced Arango transaction 执行 DDL。
    本协议只定义接口，不定义真实 IO。
    """

    def execute_create_collection(self, collection: str, collection_type: str) -> None: ...
    def execute_create_index(
        self, collection: str, index_name: str, index_type: str,
        fields: tuple[str, ...], unique: bool, sparse: bool,
    ) -> None: ...
    def catalog_snapshot(self) -> CatalogSnapshot: ...
    def collection_exists(self, name: str) -> bool: ...
    def reset(self) -> None: ...


@dataclass
class FakeSchemaApplyExecutor:
    """内存 DDL 执行器——测试专用，不接触真实 DB。

    模拟 CREATE_COLLECTION / CREATE_INDEX 的效果，
    维护一个内存 catalog 供 verify/resume 读取。
    """

    _collections: dict[str, CollectionSnapshot] = field(default_factory=dict)

    def execute_create_collection(self, collection: str, collection_type: str) -> None:
        if collection in self._collections:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_DUPLICATE_APPLY,
                f"collection {collection} already exists",
            )
        self._collections[collection] = CollectionSnapshot(
            name=collection,
            collection_type=collection_type,
            indexes=(),
        )

    def execute_create_index(
        self, collection: str, index_name: str, index_type: str,
        fields: tuple[str, ...], unique: bool, sparse: bool,
    ) -> None:
        col = self._collections.get(collection)
        if col is None:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_RESUME_CATALOG_MISMATCH,
                f"collection {collection} does not exist for index {index_name}",
            )
        from .port import IndexSnapshot
        new_index = IndexSnapshot(
            name=index_name,
            fields=fields,
            index_type=index_type,
            unique=unique,
            sparse=sparse,
        )
        existing = col.indexes
        if any(idx.name == index_name for idx in existing):
            raise SchemaBootstrapProtocolError(
                EC.DB1I_DUPLICATE_APPLY,
                f"index {index_name} already exists on {collection}",
            )
        self._collections[collection] = CollectionSnapshot(
            name=col.name,
            collection_type=col.collection_type,
            indexes=(*existing, new_index),
        )

    def catalog_snapshot(self) -> CatalogSnapshot:
        return CatalogSnapshot(
            collections=tuple(
                self._collections[name]
                for name in sorted(self._collections)
            )
        )

    def collection_exists(self, name: str) -> bool:
        return name in self._collections

    def reset(self) -> None:
        self._collections.clear()


class SchemaBootstrapProtocolError(Exception):
    """fenced apply/verify/resume 协议的结构化错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass(frozen=True)
class ActionReceipt:
    """单个 DDL action 的执行收据。"""

    ordinal: int
    action_id: str
    action_type: str
    collection: str
    state: str  # SCHEMA_BOOTSTRAP_ACTION_STATES
    ledger_entry_hash: str
    catalog_observation_hash: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "ordinal": self.ordinal,
            "action_id": self.action_id,
            "action_type": self.action_type,
            "collection": self.collection,
            "state": self.state,
            "ledger_entry_hash": self.ledger_entry_hash,
            "catalog_observation_hash": self.catalog_observation_hash,
        }


@dataclass
class SchemaBootstrapContext:
    """fenced apply 协议的冻结输入上下文。

    所有输入在 apply 开始前冻结，不可在执行过程中修改。
    """

    plan: SchemaBootstrapPlan
    site_fingerprint: SiteFingerprint
    permit: dict[str, Any]
    gate_decision: dict[str, Any]
    gate_decision_verified: bool
    maintenance_window: str
    fence_token: int
    acquired_at: str
    expires_at: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "plan_hash": self.plan.plan_hash,
            "site_fingerprint_hash": self.site_fingerprint.fingerprint_hash,
            "permit_id": self.permit.get("permit_id", ""),
            "gate_decision_id": self.gate_decision.get("decision_id", ""),
            "gate_decision_verified": self.gate_decision_verified,
            "maintenance_window": self.maintenance_window,
            "fence_token": self.fence_token,
            "acquired_at": self.acquired_at,
            "expires_at": self.expires_at,
        }


@dataclass
class SchemaBootstrapProtocol:
    """fenced Schema bootstrap apply/verify/resume 协议编排器。

    持有：
    - site_adapter: DB1L LogicalSiteAdapter（只读 site fingerprint + catalog）
    - backend: SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER 预留后端
    - executor: DDL 执行器（内存模拟）
    - applied: 是否已 apply（防重复）
    - context: 冻结的 apply 上下文
    - action_receipts: 逐 action 收据
    """

    site_adapter: LogicalSiteAdapter
    backend: SchemaBootstrapDVolumeLedgerBackend
    executor: SchemaApplyExecutor
    applied: bool = False
    context: SchemaBootstrapContext | None = None
    action_receipts: list[ActionReceipt] = field(default_factory=list)
    fence: SchemaBootstrapFence | None = None

    # ─── prepare：冻结输入 ─────────────────────────────────────────────

    def prepare(
        self,
        *,
        permit: dict[str, Any],
        gate_decision: dict[str, Any],
        human_gate_service: Any | None = None,
        evaluation_time: str = "",
        maintenance_window: str = "2026-08-14T00:00:00Z/2026-08-15T00:00:00Z",
        fence_token: int = 1,
        acquired_at: str = "2026-08-14T12:00:00Z",
        expires_at: str = "2026-08-15T12:00:00Z",
    ) -> SchemaBootstrapContext:
        """冻结 apply 输入：site fingerprint、plan、permit、gate decision。

        执行前置检查：
        1. site_adapter 连接并读取 site fingerprint
        2. 构建 bootstrap plan（绑定 site fingerprint hash）
        3. 验证 plan
        4. 验证 gate_decision（通过 HumanGateService 或结构验证）
        5. 验证 permit 绑定 plan_hash
        """

        if self.applied:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_DUPLICATE_APPLY, "protocol already applied"
            )
        if self.context is not None:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_DUPLICATE_APPLY, "protocol already prepared"
            )

        # 1. site fingerprint
        self.site_adapter.connect_readonly()
        fingerprint = self.site_adapter.site_fingerprint()

        # 2. build plan
        plan = build_schema_bootstrap_plan(
            site_fingerprint_hash=fingerprint.fingerprint_hash
        )

        # 3. verify plan
        plan_errors = verify_schema_bootstrap_plan(plan)
        if plan_errors:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_PLAN_HASH_DRIFT,
                f"plan verification failed: {plan_errors[0][1]}",
            )

        # 4. verify gate_decision
        gate_verified = False
        if human_gate_service is not None:
            result = human_gate_service.accept_gate_decision(
                gate_decision, evaluation_time=evaluation_time
            )
            if not result.passed:
                raise SchemaBootstrapProtocolError(
                    EC.DB1I_HUMAN_GATE_DECISION_REJECTED,
                    f"gate decision rejected: {result.details}",
                )
            gate_verified = True
        else:
            # 结构验证至少检查 decision == APPROVE
            if gate_decision.get("decision") != "APPROVE":
                raise SchemaBootstrapProtocolError(
                    EC.DB1I_HUMAN_GATE_DECISION_REJECTED,
                    "gate decision must be APPROVE for schema apply",
                )
            gate_verified = True

        # 5. permit 绑定 plan_hash
        permit_plan_hash = permit.get("plan_hash", "")
        if permit_plan_hash != plan.plan_hash:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_PERMIT_MISMATCH,
                f"permit plan_hash {permit_plan_hash} != plan plan_hash",
            )
        if permit.get("wp_id") != "G-DB-SCHEMA-APPLY":
            raise SchemaBootstrapProtocolError(
                EC.DB1I_PERMIT_MISMATCH,
                "permit wp_id must be G-DB-SCHEMA-APPLY",
            )

        context = SchemaBootstrapContext(
            plan=plan,
            site_fingerprint=fingerprint,
            permit=permit,
            gate_decision=gate_decision,
            gate_decision_verified=gate_verified,
            maintenance_window=maintenance_window,
            fence_token=fence_token,
            acquired_at=acquired_at,
            expires_at=expires_at,
        )
        self.context = context
        return context

    # ─── apply：fenced DDL 执行 ─────────────────────────────────────────

    def apply(
        self,
        *,
        crash_before_ordinal: int | None = None,
        crash_after_ordinal: int | None = None,
    ) -> list[ActionReceipt]:
        """执行 fenced apply 协议。

        crash_before_ordinal / crash_after_ordinal 用于 fault injection：
        - crash_before_ordinal=N：在 action N 的 DDL 执行前崩溃
          → ledger 有 ACTION_INTENT 但无 ACTION_VERIFIED → UNKNOWN_OUTCOME
        - crash_after_ordinal=N：在 action N 的 DDL 执行后崩溃
          → ledger 有 ACTION_INTENT，DDL 已执行，但无 ACTION_VERIFIED → UNKNOWN_OUTCOME

        正常流程（每个 action）：
        a. reserve ordinal via backend
        b. append ACTION_INTENT to ledger
        c. execute DDL
        d. append catalog observation + ACTION_VERIFIED
        e. consume ordinal via backend
        """

        if self.context is None:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_APPLY_WITHOUT_FENCE, "prepare() must be called before apply()"
            )
        if self.applied:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_DUPLICATE_APPLY, "protocol already applied"
            )

        ctx = self.context
        plan = ctx.plan

        # acquire fence (D-volume atomic create)
        self.fence = self.backend.acquire_fence(
            site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
            plan_hash=plan.plan_hash,
            fence_token=ctx.fence_token,
            acquired_at=ctx.acquired_at,
            expires_at=ctx.expires_at,
            maintenance_window=ctx.maintenance_window,
        )

        permit_id = ctx.permit.get("permit_id", "schema-bootstrap-permit")
        aggregate_rev = 0
        receipts: list[ActionReceipt] = []

        for action in plan.actions:
            # fault injection: crash before DDL
            if crash_before_ordinal == action.ordinal:
                # append ACTION_INTENT then crash
                self.backend.append_ledger_entry(
                    site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                    plan_hash=plan.plan_hash,
                    entry_type="ACTION_INTENT",
                    action_id=action.action_id,
                    ordinal=action.ordinal,
                    payload={"action": action.as_dict(), "crashed": True},
                )
                # 模拟崩溃：直接返回已完成的 receipts，不标记 applied
                self.action_receipts = receipts
                return receipts

            # a. reserve ordinal
            reserved_budget = {
                "invocations": 0, "solver_launches": 0,
                "database_writes": 1, "redis_writes": 0,
                "d_volume_writes": 1, "human_gate_commits": 0,
                "active_release_changes": 0, "tokens": 0,
                "cost_microunits": 0, "currency": "USD",
            }
            self.backend.reserve(
                permit_id=permit_id,
                consumption_ordinal=action.ordinal,
                idempotency_key=f"{plan.plan_hash}:{action.ordinal}",
                fence_token=ctx.fence_token,
                expected_aggregate_revision=aggregate_rev,
                reserved_budget=reserved_budget,
            )

            # b. append ACTION_INTENT
            intent_entry = self.backend.append_ledger_entry(
                site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                plan_hash=plan.plan_hash,
                entry_type="ACTION_INTENT",
                action_id=action.action_id,
                ordinal=action.ordinal,
                payload={"action": action.as_dict()},
            )

            # c. execute DDL
            if action.action_type == "CREATE_COLLECTION":
                # 从 canonical spec 查找 collection_type
                from .spec import CANONICAL_MIGRATION_SPEC
                col_spec = None
                for cs in CANONICAL_MIGRATION_SPEC.collections:
                    if cs.name == action.collection:
                        col_spec = cs
                        break
                col_type = col_spec.collection_type if col_spec else "document"
                self.executor.execute_create_collection(action.collection, col_type)
            elif action.action_type == "CREATE_INDEX":
                assert action.index is not None
                self.executor.execute_create_index(
                    action.collection,
                    action.index.name,
                    action.index.index_type,
                    action.index.fields,
                    action.index.unique,
                    action.index.sparse,
                )

            # fault injection: crash after DDL (before ACTION_VERIFIED)
            if crash_after_ordinal == action.ordinal:
                # DDL 已执行，ledger 有 ACTION_INTENT，但无 ACTION_VERIFIED
                # consume 仍标记为完成（backend 已 reserve），但状态为 UNKNOWN_OUTCOME
                self.backend.consume(
                    permit_id=permit_id,
                    consumption_ordinal=action.ordinal,
                    fence_token=ctx.fence_token,
                    actual_side_effects=reserved_budget,
                )
                self.backend.append_ledger_entry(
                    site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                    plan_hash=plan.plan_hash,
                    entry_type="UNKNOWN_OUTCOME",
                    action_id=action.action_id,
                    ordinal=action.ordinal,
                    payload={"action": action.as_dict(), "crashed_after_ddl": True},
                )
                receipts.append(ActionReceipt(
                    ordinal=action.ordinal,
                    action_id=action.action_id,
                    action_type=action.action_type,
                    collection=action.collection,
                    state="UNKNOWN_OUTCOME",
                    ledger_entry_hash=intent_entry.entry_hash,
                    catalog_observation_hash="0" * 64,
                ))
                aggregate_rev += 1
                self.action_receipts = receipts
                return receipts

            # d. catalog observation + ACTION_VERIFIED
            catalog = self.executor.catalog_snapshot()
            catalog_hash = catalog.catalog_hash
            verified_entry = self.backend.append_ledger_entry(
                site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                plan_hash=plan.plan_hash,
                entry_type="ACTION_VERIFIED",
                action_id=action.action_id,
                ordinal=action.ordinal,
                payload={
                    "action": action.as_dict(),
                    "post_catalog_hash": catalog_hash,
                },
            )

            # e. consume ordinal
            self.backend.consume(
                permit_id=permit_id,
                consumption_ordinal=action.ordinal,
                fence_token=ctx.fence_token,
                actual_side_effects=reserved_budget,
            )
            aggregate_rev += 1

            receipts.append(ActionReceipt(
                ordinal=action.ordinal,
                action_id=action.action_id,
                action_type=action.action_type,
                collection=action.collection,
                state="VERIFIED",
                ledger_entry_hash=verified_entry.entry_hash,
                catalog_observation_hash=catalog_hash,
            ))

        # release fence
        self.backend.release_fence(
            plan_hash=plan.plan_hash,
            fence_token=ctx.fence_token,
            site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
        )

        self.applied = True
        self.action_receipts = receipts
        return receipts

    # ─── verify：post-catalog 验证 ──────────────────────────────────────

    def verify(self) -> VerificationResult:
        """验证 apply 后的 catalog 与 canonical spec 一致。

        检查：
        - 所有 canonical 集合存在
        - 所有 canonical 索引存在
        - 无额外集合/索引
        - ledger chain 完整
        - 所有 action 状态为 VERIFIED
        """

        if self.context is None:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.DB1I_APPLY_WITHOUT_FENCE],
                details=["prepare() must be called before verify()"],
            )

        errors: list[EC] = []
        details: list[str] = []
        ctx = self.context
        plan = ctx.plan

        # ledger chain 验证
        ledger_errors = self.backend.verify_ledger(
            site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
            plan_hash=plan.plan_hash,
        )
        for code, detail in ledger_errors:
            errors.append(code)
            details.append(detail)

        # action 状态验证
        for receipt in self.action_receipts:
            if receipt.state != "VERIFIED":
                errors.append(EC.DB1I_UNKNOWN_OUTCOME)
                details.append(
                    f"action {receipt.action_id} state is {receipt.state}, not VERIFIED"
                )

        # catalog 验证
        catalog = self.executor.catalog_snapshot()
        from .spec import CANONICAL_MIGRATION_SPEC
        catalog_by_name = {col.name: col for col in catalog.collections}

        for col_spec in CANONICAL_MIGRATION_SPEC.collections:
            col_snap = catalog_by_name.get(col_spec.name)
            if col_snap is None:
                errors.append(EC.DB1I_RESUME_CATALOG_MISMATCH)
                details.append(f"collection {col_spec.name} missing from catalog")
                continue
            if col_snap.collection_type != col_spec.collection_type:
                errors.append(EC.DB1I_RESUME_CATALOG_MISMATCH)
                details.append(
                    f"collection {col_spec.name} type {col_snap.collection_type} "
                    f"!= {col_spec.collection_type}"
                )
            index_by_name = {idx.name: idx for idx in col_snap.indexes}
            for idx_spec in col_spec.indexes:
                idx_snap = index_by_name.get(idx_spec.name)
                if idx_snap is None:
                    errors.append(EC.DB1I_RESUME_CATALOG_MISMATCH)
                    details.append(
                        f"index {idx_spec.name} missing on {col_spec.name}"
                    )
                elif idx_snap.semantic_tuple() != (
                    idx_spec.name, idx_spec.index_type, idx_spec.fields,
                    idx_spec.unique, idx_spec.sparse,
                ):
                    errors.append(EC.DB1I_RESUME_CATALOG_MISMATCH)
                    details.append(
                        f"index {idx_spec.name} on {col_spec.name} semantic mismatch"
                    )

        # 额外集合检查
        canonical_names = {cs.name for cs in CANONICAL_MIGRATION_SPEC.collections}
        extra = set(catalog_by_name) - canonical_names
        if extra:
            errors.append(EC.DB1I_RESUME_CATALOG_MISMATCH)
            details.append(f"extra collections in catalog: {sorted(extra)}")

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(
            verdict=verdict, error_codes=errors, details=details
        )

    # ─── resume：崩溃后恢复 ─────────────────────────────────────────────

    def resume(self) -> VerificationResult:
        """崩溃后恢复——重读 ledger 与实 site catalog，reconcile UNKNOWN_OUTCOME。

        UNKNOWN_OUTCOME 不得盲重放 DDL，必须按 catalog 事实 reconcile：
        - 如果 catalog 显示 DDL 已生效 → 标记为 VERIFIED
        - 如果 catalog 显示 DDL 未生效 → 标记为 FAILED，需人工介入
        """

        if self.context is None:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.DB1I_APPLY_WITHOUT_FENCE],
                details=["prepare() must be called before resume()"],
            )

        ctx = self.context
        plan = ctx.plan
        errors: list[EC] = []
        details: list[str] = []

        # 重读 ledger
        ledger = self.backend.get_ledger(
            site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
            plan_hash=plan.plan_hash,
        )

        # 验证 ledger chain
        chain_errors = ledger.verify_chain()
        for code, detail in chain_errors:
            errors.append(code)
            details.append(detail)

        # 按 action ordinal 分组 ledger entries
        entries_by_ordinal: dict[int, list] = {}
        for entry in ledger.entries:
            if entry.ordinal >= 0:
                entries_by_ordinal.setdefault(entry.ordinal, []).append(entry)

        # 读取当前 catalog（executor 的内存状态 = 崩溃后的 site catalog）
        catalog = self.executor.catalog_snapshot()
        catalog_by_name = {col.name: col for col in catalog.collections}

        from .spec import CANONICAL_MIGRATION_SPEC
        col_specs_by_name = {cs.name: cs for cs in CANONICAL_MIGRATION_SPEC.collections}

        reconciled_receipts: list[ActionReceipt] = []
        for action in plan.actions:
            entries = entries_by_ordinal.get(action.ordinal, [])
            entry_types = [e.entry_type for e in entries]
            has_verified = "ACTION_VERIFIED" in entry_types
            has_intent = "ACTION_INTENT" in entry_types
            has_unknown = "UNKNOWN_OUTCOME" in entry_types

            if has_verified:
                # 已验证，跳过
                verified_entry = next(e for e in entries if e.entry_type == "ACTION_VERIFIED")
                reconciled_receipts.append(ActionReceipt(
                    ordinal=action.ordinal,
                    action_id=action.action_id,
                    action_type=action.action_type,
                    collection=action.collection,
                    state="VERIFIED",
                    ledger_entry_hash=verified_entry.entry_hash,
                    catalog_observation_hash=verified_entry.payload.get("post_catalog_hash", "0" * 64),
                ))
            elif has_intent or has_unknown:
                # UNKNOWN_OUTCOME — 按 catalog 事实 reconcile
                if action.action_type == "CREATE_COLLECTION":
                    if action.collection in catalog_by_name:
                        # DDL 已生效，标记 VERIFIED
                        catalog_hash = catalog.catalog_hash
                        verified_entry = self.backend.append_ledger_entry(
                            site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                            plan_hash=plan.plan_hash,
                            entry_type="ACTION_VERIFIED",
                            action_id=action.action_id,
                            ordinal=action.ordinal,
                            payload={
                                "action": action.as_dict(),
                                "post_catalog_hash": catalog_hash,
                                "reconciled_from": "UNKNOWN_OUTCOME",
                            },
                        )
                        reconciled_receipts.append(ActionReceipt(
                            ordinal=action.ordinal,
                            action_id=action.action_id,
                            action_type=action.action_type,
                            collection=action.collection,
                            state="VERIFIED",
                            ledger_entry_hash=verified_entry.entry_hash,
                            catalog_observation_hash=catalog_hash,
                        ))
                    else:
                        # DDL 未生效，标记 FAILED
                        failed_entry = self.backend.append_ledger_entry(
                            site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                            plan_hash=plan.plan_hash,
                            entry_type="ACTION_FAILED",
                            action_id=action.action_id,
                            ordinal=action.ordinal,
                            payload={
                                "action": action.as_dict(),
                                "reconciled_from": "UNKNOWN_OUTCOME",
                                "reason": "collection not found in catalog",
                            },
                        )
                        reconciled_receipts.append(ActionReceipt(
                            ordinal=action.ordinal,
                            action_id=action.action_id,
                            action_type=action.action_type,
                            collection=action.collection,
                            state="FAILED",
                            ledger_entry_hash=failed_entry.entry_hash,
                            catalog_observation_hash="0" * 64,
                        ))
                        errors.append(EC.DB1I_UNKNOWN_OUTCOME)
                        details.append(
                            f"action {action.action_id} FAILED: DDL did not take effect"
                        )
                elif action.action_type == "CREATE_INDEX":
                    assert action.index is not None
                    col = catalog_by_name.get(action.collection)
                    index_exists = (
                        col is not None
                        and any(idx.name == action.index.name for idx in col.indexes)
                    )
                    if index_exists:
                        catalog_hash = catalog.catalog_hash
                        verified_entry = self.backend.append_ledger_entry(
                            site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                            plan_hash=plan.plan_hash,
                            entry_type="ACTION_VERIFIED",
                            action_id=action.action_id,
                            ordinal=action.ordinal,
                            payload={
                                "action": action.as_dict(),
                                "post_catalog_hash": catalog_hash,
                                "reconciled_from": "UNKNOWN_OUTCOME",
                            },
                        )
                        reconciled_receipts.append(ActionReceipt(
                            ordinal=action.ordinal,
                            action_id=action.action_id,
                            action_type=action.action_type,
                            collection=action.collection,
                            state="VERIFIED",
                            ledger_entry_hash=verified_entry.entry_hash,
                            catalog_observation_hash=catalog_hash,
                        ))
                    else:
                        failed_entry = self.backend.append_ledger_entry(
                            site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                            plan_hash=plan.plan_hash,
                            entry_type="ACTION_FAILED",
                            action_id=action.action_id,
                            ordinal=action.ordinal,
                            payload={
                                "action": action.as_dict(),
                                "reconciled_from": "UNKNOWN_OUTCOME",
                                "reason": "index not found in catalog",
                            },
                        )
                        reconciled_receipts.append(ActionReceipt(
                            ordinal=action.ordinal,
                            action_id=action.action_id,
                            action_type=action.action_type,
                            collection=action.collection,
                            state="FAILED",
                            ledger_entry_hash=failed_entry.entry_hash,
                            catalog_observation_hash="0" * 64,
                        ))
                        errors.append(EC.DB1I_UNKNOWN_OUTCOME)
                        details.append(
                            f"action {action.action_id} FAILED: DDL did not take effect"
                        )
            else:
                # 未开始，标记 PENDING
                reconciled_receipts.append(ActionReceipt(
                    ordinal=action.ordinal,
                    action_id=action.action_id,
                    action_type=action.action_type,
                    collection=action.collection,
                    state="PENDING",
                    ledger_entry_hash="0" * 64,
                    catalog_observation_hash="0" * 64,
                ))

        self.action_receipts = reconciled_receipts

        # 如果全部 VERIFIED，标记 applied 并释放 fence
        all_verified = all(r.state == "VERIFIED" for r in reconciled_receipts)
        if all_verified and not errors:
            self.applied = True
            fence = self.backend.get_fence(plan.plan_hash)
            if fence is not None and fence.state == "ACTIVE":
                self.backend.release_fence(
                    plan_hash=plan.plan_hash,
                    fence_token=ctx.fence_token,
                    site_fingerprint_hash=ctx.site_fingerprint.fingerprint_hash,
                )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(
            verdict=verdict, error_codes=errors, details=details
        )

    # ─── 输出边界检查 ──────────────────────────────────────────────────

    @staticmethod
    def assert_allowed_output(output_kind: str) -> None:
        """断言输出类型在 DB1I 允许的范围内。"""
        if output_kind in DB1I_FORBIDDEN_OUTPUT_KINDS:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED,
                f"DB1I must not produce {output_kind}",
            )
        if output_kind not in DB1I_ALLOWED_OUTPUT_KINDS:
            raise SchemaBootstrapProtocolError(
                EC.DB1I_SCHEMA_STATE_REPORT_INVALID,
                f"DB1I output kind {output_kind} not allowed",
            )

    # ─── 辅助属性 ──────────────────────────────────────────────────────

    @property
    def ledger_root_hash(self) -> str:
        if self.context is None:
            return "0" * 64
        return self.backend.ledger_root_hash(
            site_fingerprint_hash=self.context.site_fingerprint.fingerprint_hash,
            plan_hash=self.context.plan.plan_hash,
        )

    @property
    def post_catalog_hash(self) -> str:
        return self.executor.catalog_snapshot().catalog_hash
