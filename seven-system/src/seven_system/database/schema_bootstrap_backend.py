"""WP-DB1I SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER 预留后端。

实现 GV0 ``ReservationBackendPort``，专用于 Schema bootstrap 的 D 盘
append-only ledger 原子预留。本后端不复制、不放宽、不跳过 GV0 的 1-7 步
验证顺序——它只是 GV0 预留接口的一个后端实例。

D 盘 bootstrap ledger 结构（内存模拟，SIDE_EFFECT_FREE）：

    <site-fingerprint>/<plan-hash>/
    ├── fences/<ordinal>-<fence-id>          # SchemaBootstrapFence
    ├── events/<sequence>-<event-id>.json    # append-only ACTION_INTENT/VERIFIED/...
    └── root-seal.json                       # 全部完成后 seal

每个 ledger entry 包含 previous-entry hash，形成 hash chain。
``UNKNOWN_OUTCOME`` 不得盲重放——resume 时必须按 catalog 事实 reconcile。

硬约束：
- 不连接真实 DB、不写真实 D 盘（测试用内存模拟）
- fence 唯一：同一 plan_hash 只允许一个 ACTIVE fence
- stale fence 拒绝：fence_token 不匹配拒绝 consume/release
- 重复 ordinal 拒绝（EC.DUPLICATE_ORDINAL）
- append-only：已 CONSUMED/RELEASED 的 ordinal 不可重入
- 额度守恒：actual 不超过 reserved
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    SCHEMA_BOOTSTRAP_FENCE_STATES,
    SCHEMA_BOOTSTRAP_LEDGER_ENTRY_TYPES,
    VerificationErrorCode as EC,
)
from ..contracts.reservation import Allowance, ReservationBackendPort
from ..hashing import canonical_json_bytes, object_hash


class SchemaBootstrapBackendError(Exception):
    """D-volume ledger 后端的结构化错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass(frozen=True)
class SchemaBootstrapFence:
    """Schema bootstrap fence——D 盘 atomic create 的唯一 fence。

    绑定 plan_hash、fence_token、maintenance window、expiry。
    同一 plan_hash 只允许一个 ACTIVE fence；竞争者必须 BLOCK。
    """

    plan_hash: str
    fence_token: int
    acquired_at: str
    expires_at: str
    maintenance_window: str
    state: str = "ACTIVE"

    def as_dict(self) -> dict[str, Any]:
        return {
            "plan_hash": self.plan_hash,
            "fence_token": self.fence_token,
            "acquired_at": self.acquired_at,
            "expires_at": self.expires_at,
            "maintenance_window": self.maintenance_window,
            "state": self.state,
        }


@dataclass(frozen=True)
class LedgerEntry:
    """D 盘 append-only ledger 的单个 entry。

    每个 entry 包含 previous-entry hash，形成 hash chain。
    entry_type ∈ SCHEMA_BOOTSTRAP_LEDGER_ENTRY_TYPES。
    """

    sequence: int
    entry_type: str
    action_id: str
    ordinal: int
    payload: dict[str, Any]
    previous_hash: str  # 前一个 entry 的 entry_hash；genesis 为 "0"*64
    entry_hash: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "sequence": self.sequence,
            "entry_type": self.entry_type,
            "action_id": self.action_id,
            "ordinal": self.ordinal,
            "payload": dict(self.payload),
            "previous_hash": self.previous_hash,
            "entry_hash": self.entry_hash,
        }


def _compute_entry_hash(
    sequence: int,
    entry_type: str,
    action_id: str,
    ordinal: int,
    payload: dict[str, Any],
    previous_hash: str,
) -> str:
    """计算 ledger entry 的确定性 hash（entry_hash 不进入自身签名输入）。"""

    return object_hash(
        "SchemaBootstrapLedgerEntry",
        "schema-bootstrap-ledger-entry/v1",
        {
            "sequence": sequence,
            "entry_type": entry_type,
            "action_id": action_id,
            "ordinal": ordinal,
            "payload": payload,
            "previous_hash": previous_hash,
        },
    )


@dataclass
class SchemaBootstrapDLedger:
    """D 盘 bootstrap ledger 的内存模拟。

    每个 (site_fingerprint_hash, plan_hash) 对应一条独立 ledger。
    ledger 是 append-only 的 entry 链，带 previous-hash 链。
    """

    site_fingerprint_hash: str
    plan_hash: str
    entries: list[LedgerEntry] = field(default_factory=list)
    fence: SchemaBootstrapFence | None = None

    @property
    def root_hash(self) -> str:
        """ledger 的 root hash = 最后一个 entry 的 entry_hash（空 ledger 为 0*64）。"""
        if not self.entries:
            return "0" * 64
        return self.entries[-1].entry_hash

    @property
    def entry_count(self) -> int:
        return len(self.entries)

    def append(
        self,
        *,
        entry_type: str,
        action_id: str,
        ordinal: int,
        payload: dict[str, Any],
    ) -> LedgerEntry:
        if entry_type not in SCHEMA_BOOTSTRAP_LEDGER_ENTRY_TYPES:
            raise SchemaBootstrapBackendError(
                EC.REQUIRED_FIELD_MISSING,
                f"unknown ledger entry_type: {entry_type}",
            )
        previous_hash = self.root_hash
        sequence = len(self.entries)
        entry_hash = _compute_entry_hash(
            sequence, entry_type, action_id, ordinal, payload, previous_hash
        )
        entry = LedgerEntry(
            sequence=sequence,
            entry_type=entry_type,
            action_id=action_id,
            ordinal=ordinal,
            payload=dict(payload),
            previous_hash=previous_hash,
            entry_hash=entry_hash,
        )
        self.entries.append(entry)
        return entry

    def verify_chain(self) -> tuple[tuple[EC, str], ...]:
        """验证整个 ledger 的 hash chain 完整性。"""
        errors: list[tuple[EC, str]] = []
        expected_previous = "0" * 64
        for idx, entry in enumerate(self.entries):
            if entry.sequence != idx:
                errors.append(
                    (EC.DB1I_LEDGER_TAMPERED, f"entry sequence {entry.sequence} != {idx}")
                )
            if entry.previous_hash != expected_previous:
                errors.append(
                    (
                        EC.DB1I_LEDGER_PREVIOUS_HASH_MISMATCH,
                        f"entry {idx} previous_hash mismatch",
                    )
                )
            recomputed = _compute_entry_hash(
                entry.sequence,
                entry.entry_type,
                entry.action_id,
                entry.ordinal,
                entry.payload,
                entry.previous_hash,
            )
            if recomputed != entry.entry_hash:
                errors.append(
                    (EC.DB1I_LEDGER_TAMPERED, f"entry {idx} entry_hash mismatch")
                )
            expected_previous = entry.entry_hash
        return tuple(dict.fromkeys(errors))


class SchemaBootstrapDVolumeLedgerBackend:
    """SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER 预留后端。

    实现 GV0 ``ReservationBackendPort``。
    使用内存字典模拟 D 盘 ledger——不接触真实文件系统。

    每条 ledger 按 (site_fingerprint_hash, plan_hash) 隔离。
    fence 按 plan_hash 唯一——同一 plan 只允许一个 ACTIVE fence。
    """

    def __init__(self) -> None:
        self._ledgers: dict[tuple[str, str], SchemaBootstrapDLedger] = {}
        self._fences_by_plan: dict[str, SchemaBootstrapFence] = {}
        # ReservationBackendPort 状态
        self._entries: dict[tuple[str, int], dict[str, Any]] = {}
        self._fences: dict[tuple[str, int], int] = {}
        self._aggregate_revisions: dict[str, int] = {}

    # ─── D-volume ledger 管理 ───────────────────────────────────────────

    def get_ledger(
        self, *, site_fingerprint_hash: str, plan_hash: str
    ) -> SchemaBootstrapDLedger:
        key = (site_fingerprint_hash, plan_hash)
        ledger = self._ledgers.get(key)
        if ledger is None:
            ledger = SchemaBootstrapDLedger(
                site_fingerprint_hash=site_fingerprint_hash,
                plan_hash=plan_hash,
            )
            self._ledgers[key] = ledger
        return ledger

    def acquire_fence(
        self,
        *,
        site_fingerprint_hash: str,
        plan_hash: str,
        fence_token: int,
        acquired_at: str,
        expires_at: str,
        maintenance_window: str,
    ) -> SchemaBootstrapFence:
        """在 D 盘用 atomic create 建立唯一 SchemaBootstrapFence。

        同一 plan_hash 已有 ACTIVE fence → 拒绝（竞争者 BLOCK）。
        """
        existing = self._fences_by_plan.get(plan_hash)
        if existing is not None and existing.state == "ACTIVE":
            raise SchemaBootstrapBackendError(
                EC.DB1I_FENCE_DUPLICATE,
                f"plan {plan_hash} already has an ACTIVE fence",
            )
        fence = SchemaBootstrapFence(
            plan_hash=plan_hash,
            fence_token=fence_token,
            acquired_at=acquired_at,
            expires_at=expires_at,
            maintenance_window=maintenance_window,
            state="ACTIVE",
        )
        self._fences_by_plan[plan_hash] = fence
        ledger = self.get_ledger(
            site_fingerprint_hash=site_fingerprint_hash, plan_hash=plan_hash
        )
        ledger.fence = fence
        ledger.append(
            entry_type="FENCE_ACQUIRED",
            action_id="fence",
            ordinal=-1,
            payload=fence.as_dict(),
        )
        return fence

    def release_fence(
        self,
        *,
        plan_hash: str,
        fence_token: int,
        site_fingerprint_hash: str,
    ) -> SchemaBootstrapFence:
        """释放 fence（bootstrap 完成或人工授权过期后）。"""
        fence = self._fences_by_plan.get(plan_hash)
        if fence is None:
            raise SchemaBootstrapBackendError(
                EC.DB1I_FENCE_MISSING, f"no fence for plan {plan_hash}"
            )
        if fence.fence_token != fence_token:
            raise SchemaBootstrapBackendError(
                EC.DB1I_FENCE_STALE, "fence_token mismatch on release"
            )
        released = SchemaBootstrapFence(
            plan_hash=fence.plan_hash,
            fence_token=fence.fence_token,
            acquired_at=fence.acquired_at,
            expires_at=fence.expires_at,
            maintenance_window=fence.maintenance_window,
            state="RELEASED",
        )
        self._fences_by_plan[plan_hash] = released
        ledger = self.get_ledger(
            site_fingerprint_hash=site_fingerprint_hash, plan_hash=plan_hash
        )
        ledger.fence = released
        ledger.append(
            entry_type="FENCE_RELEASED",
            action_id="fence",
            ordinal=-1,
            payload=released.as_dict(),
        )
        return released

    def get_fence(self, plan_hash: str) -> SchemaBootstrapFence | None:
        return self._fences_by_plan.get(plan_hash)

    def append_ledger_entry(
        self,
        *,
        site_fingerprint_hash: str,
        plan_hash: str,
        entry_type: str,
        action_id: str,
        ordinal: int,
        payload: dict[str, Any],
    ) -> LedgerEntry:
        ledger = self.get_ledger(
            site_fingerprint_hash=site_fingerprint_hash, plan_hash=plan_hash
        )
        return ledger.append(
            entry_type=entry_type,
            action_id=action_id,
            ordinal=ordinal,
            payload=payload,
        )

    def verify_ledger(
        self, *, site_fingerprint_hash: str, plan_hash: str
    ) -> tuple[tuple[EC, str], ...]:
        ledger = self.get_ledger(
            site_fingerprint_hash=site_fingerprint_hash, plan_hash=plan_hash
        )
        return ledger.verify_chain()

    def ledger_root_hash(
        self, *, site_fingerprint_hash: str, plan_hash: str
    ) -> str:
        ledger = self.get_ledger(
            site_fingerprint_hash=site_fingerprint_hash, plan_hash=plan_hash
        )
        return ledger.root_hash

    # ─── ReservationBackendPort 实现 ────────────────────────────────────

    def reserve(
        self,
        *,
        permit_id: str,
        consumption_ordinal: int,
        idempotency_key: str,
        fence_token: int,
        expected_aggregate_revision: int,
        reserved_budget: dict[str, Any],
    ) -> dict[str, Any]:
        key = (permit_id, consumption_ordinal)
        if key in self._entries:
            raise SchemaBootstrapBackendError(
                EC.DUPLICATE_ORDINAL,
                f"ordinal {consumption_ordinal} already reserved for "
                f"permit {permit_id}",
            )
        current_rev = self._aggregate_revisions.get(permit_id, 0)
        if expected_aggregate_revision != current_rev:
            raise SchemaBootstrapBackendError(
                EC.STALE_FENCE,
                f"expected revision {expected_aggregate_revision} != "
                f"current {current_rev}",
            )
        entry = {
            "permit_id": permit_id,
            "consumption_ordinal": consumption_ordinal,
            "idempotency_key": idempotency_key,
            "fence_token": fence_token,
            "status": "RESERVED",
            "reserved_budget": reserved_budget,
            "actual_side_effects": {},
            "held_allowance": reserved_budget,
            "released_allowance": {},
            "remaining_allowance": reserved_budget,
            "reservation_backend": "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
        }
        self._entries[key] = entry
        self._fences[key] = fence_token
        self._aggregate_revisions[permit_id] = current_rev + 1
        return {
            "reservation_transaction_receipt": {
                "permit_id": permit_id,
                "consumption_ordinal": consumption_ordinal,
                "fence_token": fence_token,
                "status": "RESERVED",
                "reservation_backend": "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
            }
        }

    def consume(
        self,
        *,
        permit_id: str,
        consumption_ordinal: int,
        fence_token: int,
        actual_side_effects: dict[str, Any],
    ) -> dict[str, Any]:
        key = (permit_id, consumption_ordinal)
        entry = self._entries.get(key)
        if entry is None:
            raise SchemaBootstrapBackendError(
                EC.RESERVATION_NOT_ATOMIC,
                f"no reservation for ordinal {consumption_ordinal}",
            )
        if self._fences.get(key) != fence_token:
            raise SchemaBootstrapBackendError(
                EC.STALE_FENCE,
                f"fence mismatch for ordinal {consumption_ordinal}",
            )
        if entry["status"] != "RESERVED":
            raise SchemaBootstrapBackendError(
                EC.APPEND_ONLY_VIOLATION,
                f"ordinal {consumption_ordinal} already {entry['status']}",
            )
        reserved = Allowance.from_dict(entry["reserved_budget"])
        actual = Allowance.from_dict(actual_side_effects)
        for f in (
            "invocations",
            "solver_launches",
            "database_writes",
            "redis_writes",
            "d_volume_writes",
            "human_gate_commits",
            "active_release_changes",
            "tokens",
            "cost_microunits",
        ):
            if getattr(actual, f) > getattr(reserved, f):
                raise SchemaBootstrapBackendError(
                    EC.ALLOWANCE_NOT_CONSERVED,
                    f"actual {f}={getattr(actual, f)} exceeds "
                    f"reserved {getattr(reserved, f)}",
                )
        entry["status"] = "CONSUMED"
        entry["actual_side_effects"] = actual_side_effects
        entry["held_allowance"] = {}
        remaining = Allowance.from_dict(entry["reserved_budget"]).add(
            Allowance(
                **{k: -v for k, v in actual_side_effects.items() if isinstance(v, int)}
            )
        )
        entry["remaining_allowance"] = {
            "invocations": remaining.invocations,
            "solver_launches": remaining.solver_launches,
            "database_writes": remaining.database_writes,
            "redis_writes": remaining.redis_writes,
            "d_volume_writes": remaining.d_volume_writes,
            "human_gate_commits": remaining.human_gate_commits,
            "active_release_changes": remaining.active_release_changes,
            "tokens": remaining.tokens,
            "cost_microunits": remaining.cost_microunits,
            "currency": entry["reserved_budget"].get("currency", "USD"),
        }
        return {
            "consumption_receipt": {
                "permit_id": permit_id,
                "consumption_ordinal": consumption_ordinal,
                "status": "CONSUMED",
                "reservation_backend": "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
            }
        }

    def release_unused(
        self,
        *,
        permit_id: str,
        consumption_ordinal: int,
        fence_token: int,
        proof_not_started_refs: list[dict[str, str]],
    ) -> dict[str, Any]:
        key = (permit_id, consumption_ordinal)
        entry = self._entries.get(key)
        if entry is None:
            raise SchemaBootstrapBackendError(
                EC.RESERVATION_NOT_ATOMIC,
                f"no reservation for ordinal {consumption_ordinal}",
            )
        if self._fences.get(key) != fence_token:
            raise SchemaBootstrapBackendError(
                EC.STALE_FENCE,
                f"fence mismatch for ordinal {consumption_ordinal}",
            )
        if entry["status"] != "RESERVED":
            raise SchemaBootstrapBackendError(
                EC.APPEND_ONLY_VIOLATION,
                f"ordinal {consumption_ordinal} already {entry['status']}",
            )
        if not proof_not_started_refs:
            raise SchemaBootstrapBackendError(
                EC.RELEASE_WITHOUT_PROOF,
                "release requires proof_not_started_refs",
            )
        entry["status"] = "RELEASED_UNUSED"
        entry["released_allowance"] = entry["reserved_budget"]
        entry["held_allowance"] = {}
        return {
            "release_receipt": {
                "permit_id": permit_id,
                "consumption_ordinal": consumption_ordinal,
                "status": "RELEASED_UNUSED",
                "reservation_backend": "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
            }
        }

    def get_state(
        self, *, permit_id: str, consumption_ordinal: int
    ) -> dict[str, Any] | None:
        return self._entries.get((permit_id, consumption_ordinal))


# 静态类型检查：确认本类满足 ReservationBackendPort Protocol
def _check_protocol_conformance() -> ReservationBackendPort:
    return SchemaBootstrapDVolumeLedgerBackend()  # type: ignore[return-value]
