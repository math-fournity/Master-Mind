"""CanonicalDBReservationBackend — GV0 canonical Arango expected-revision transaction.

RT1 拥有 SecurityContractVerifier 唯一的 canonical Arango expected-revision
transaction reservation backend（DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER）。

实现 GV0 ReservationBackendPort 接口：
- reserve: 原子预留一个 action ordinal
- consume: 消耗一个已预留的 ordinal
- release_unused: 释放一个已预留但未实际执行的 ordinal
- get_state: 查询某个 ordinal 的当前状态

与 GV0 SideEffectFreeReferenceBackend 的区别：
- 使用 expected-revision transaction 语义
- 模拟 Arango DB 的 atomic document update with revision check
- 同时管理 WorkEvent、outbox 和 permit consumption 的原子事务

不变量（不得复制、放宽或跳过 GV0 的 1-7 步验证顺序）：
1. 重复 ordinal 必须拒绝（EC.DUPLICATE_ORDINAL）
2. stale fence 必须拒绝（EC.STALE_FENCE）
3. 预留不原子必须拒绝（EC.RESERVATION_NOT_ATOMIC）
4. actual_side_effects 不能超过预留额度（EC.ALLOWANCE_NOT_CONSERVED）
5. release 必须有 proof_not_started_refs（EC.RELEASE_WITHOUT_PROOF）

SIDE_EFFECT_FREE：纯内存模拟 Arango DB 事务。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    ALLOWANCE_FIELDS,
    CONSUMPTION_STATUSES,
    VerificationErrorCode as EC,
)
from ..contracts.reservation import Allowance, ReservationBackendPort


class DBReservationError(Exception):
    """CanonicalDBReservationBackend 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class DBTransaction:
    """模拟 Arango DB 的 expected-revision transaction。"""

    transaction_id: str
    permit_id: str
    consumption_ordinal: int
    expected_revision: int
    fence_token: int
    operations: list[dict[str, Any]] = field(default_factory=list)
    committed: bool = False
    rolled_back: bool = False


class CanonicalDBReservationBackend:
    """Canonical Arango expected-revision transaction reservation backend.

    实现 GV0 ReservationBackendPort。
    模拟 Arango DB 的 atomic document update with revision check。

    每个 permit_id 对应一个 aggregate，有单调递增的 revision。
    reserve 操作检查 expected_aggregate_revision == current_revision，
    成功后 revision +1（模拟 Arango _rev 递增）。
    """

    BACKEND_KIND = "DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER"

    def __init__(self) -> None:
        self._entries: dict[tuple[str, int], dict[str, Any]] = {}
        self._fences: dict[tuple[str, int], int] = {}
        self._aggregate_revisions: dict[str, int] = {}
        self._transactions: dict[str, DBTransaction] = {}
        self._next_tx_id: int = 0

    def _new_transaction_id(self) -> str:
        self._next_tx_id += 1
        return f"db-tx-{self._next_tx_id:08d}"

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
        """原子预留一个 action ordinal。

        使用 expected-revision transaction：
        1. 检查 ordinal 未被预留
        2. 检查 expected_aggregate_revision == current_revision
        3. 原子写入 reservation entry + revision bump
        4. 返回 reservation_transaction_receipt
        """
        key = (permit_id, consumption_ordinal)

        # 1. 重复 ordinal 检查
        if key in self._entries:
            raise DBReservationError(
                EC.DUPLICATE_ORDINAL,
                f"ordinal {consumption_ordinal} already reserved for "
                f"permit {permit_id}",
            )

        # 2. expected-revision 检查
        current_rev = self._aggregate_revisions.get(permit_id, 0)
        if expected_aggregate_revision != current_rev:
            raise DBReservationError(
                EC.STALE_FENCE,
                f"expected revision {expected_aggregate_revision} != "
                f"current {current_rev} for permit {permit_id}",
            )

        # 3. 原子事务
        tx_id = self._new_transaction_id()
        tx = DBTransaction(
            transaction_id=tx_id,
            permit_id=permit_id,
            consumption_ordinal=consumption_ordinal,
            expected_revision=expected_aggregate_revision,
            fence_token=fence_token,
        )
        tx.operations.append(
            {
                "op": "INSERT",
                "collection": "seven_consumption_v2",
                "document": {
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
                },
            }
        )
        tx.operations.append(
            {
                "op": "UPDATE",
                "collection": "seven_aggregate_state_v2",
                "document": {"permit_id": permit_id},
                "expected_revision": expected_aggregate_revision,
            }
        )

        # 模拟原子 commit
        entry = {
            "permit_id": permit_id,
            "consumption_ordinal": consumption_ordinal,
            "idempotency_key": idempotency_key,
            "fence_token": fence_token,
            "status": "RESERVED",
            "reserved_budget": reserved_budget,
            "actual_side_effects": {},
            "held_allowance": dict(reserved_budget),
            "released_allowance": {},
            "remaining_allowance": dict(reserved_budget),
            "transaction_id": tx_id,
        }
        self._entries[key] = entry
        self._fences[key] = fence_token
        self._aggregate_revisions[permit_id] = current_rev + 1
        tx.committed = True
        self._transactions[tx_id] = tx

        return {
            "reservation_transaction_receipt": {
                "permit_id": permit_id,
                "consumption_ordinal": consumption_ordinal,
                "fence_token": fence_token,
                "status": "RESERVED",
                "transaction_id": tx_id,
                "backend": self.BACKEND_KIND,
                "new_aggregate_revision": current_rev + 1,
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
        """消耗一个已预留的 ordinal。

        验证：
        1. reservation 存在
        2. fence_token 匹配
        3. status 为 RESERVED
        4. actual_side_effects 不超过 reserved_budget
        """
        key = (permit_id, consumption_ordinal)
        entry = self._entries.get(key)
        if entry is None:
            raise DBReservationError(
                EC.RESERVATION_NOT_ATOMIC,
                f"no reservation for ordinal {consumption_ordinal}",
            )

        if self._fences.get(key) != fence_token:
            raise DBReservationError(
                EC.STALE_FENCE,
                f"fence mismatch for ordinal {consumption_ordinal}",
            )

        if entry["status"] != "RESERVED":
            raise DBReservationError(
                EC.APPEND_ONLY_VIOLATION,
                f"ordinal {consumption_ordinal} already {entry['status']}",
            )

        # 验证 actual 不超过 reserved
        reserved = Allowance.from_dict(entry["reserved_budget"])
        actual = Allowance.from_dict(actual_side_effects)
        for f in ALLOWANCE_FIELDS:
            if getattr(actual, f) > getattr(reserved, f):
                raise DBReservationError(
                    EC.ALLOWANCE_NOT_CONSERVED,
                    f"actual {f}={getattr(actual, f)} exceeds "
                    f"reserved {getattr(reserved, f)}",
                )

        # 原子事务
        tx_id = self._new_transaction_id()
        tx = DBTransaction(
            transaction_id=tx_id,
            permit_id=permit_id,
            consumption_ordinal=consumption_ordinal,
            expected_revision=self._aggregate_revisions.get(permit_id, 0),
            fence_token=fence_token,
        )
        tx.operations.append(
            {
                "op": "UPDATE",
                "collection": "seven_consumption_v2",
                "document": {
                    "permit_id": permit_id,
                    "consumption_ordinal": consumption_ordinal,
                    "status": "CONSUMED",
                    "actual_side_effects": actual_side_effects,
                },
            }
        )

        entry["status"] = "CONSUMED"
        entry["actual_side_effects"] = dict(actual_side_effects)
        entry["held_allowance"] = {}

        # 计算 remaining
        remaining = Allowance.from_dict(entry["reserved_budget"]).add(
            Allowance(
                **{
                    k: -v
                    for k, v in actual_side_effects.items()
                    if isinstance(v, int) and k in ALLOWANCE_FIELDS
                }
            )
        )
        entry["remaining_allowance"] = {
            f: getattr(remaining, f) for f in ALLOWANCE_FIELDS
        }
        entry["remaining_allowance"]["currency"] = entry["reserved_budget"].get(
            "currency", "USD"
        )

        tx.committed = True
        self._transactions[tx_id] = tx

        return {
            "consumption_receipt": {
                "permit_id": permit_id,
                "consumption_ordinal": consumption_ordinal,
                "status": "CONSUMED",
                "transaction_id": tx_id,
                "backend": self.BACKEND_KIND,
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
        """释放一个已预留但未实际执行的 ordinal。

        必须有 proof_not_started_refs 证明未开始。
        """
        key = (permit_id, consumption_ordinal)
        entry = self._entries.get(key)
        if entry is None:
            raise DBReservationError(
                EC.RESERVATION_NOT_ATOMIC,
                f"no reservation for ordinal {consumption_ordinal}",
            )

        if self._fences.get(key) != fence_token:
            raise DBReservationError(
                EC.STALE_FENCE,
                f"fence mismatch for ordinal {consumption_ordinal}",
            )

        if entry["status"] != "RESERVED":
            raise DBReservationError(
                EC.APPEND_ONLY_VIOLATION,
                f"ordinal {consumption_ordinal} already {entry['status']}",
            )

        if not proof_not_started_refs:
            raise DBReservationError(
                EC.RELEASE_WITHOUT_PROOF,
                f"release requires proof_not_started_refs",
            )

        entry["status"] = "RELEASED_UNUSED"
        entry["released_allowance"] = dict(entry["reserved_budget"])
        entry["held_allowance"] = {}

        return {
            "release_receipt": {
                "permit_id": permit_id,
                "consumption_ordinal": consumption_ordinal,
                "status": "RELEASED_UNUSED",
                "backend": self.BACKEND_KIND,
            }
        }

    def get_state(
        self, *, permit_id: str, consumption_ordinal: int
    ) -> dict[str, Any] | None:
        """查询某个 ordinal 的当前状态。"""
        entry = self._entries.get((permit_id, consumption_ordinal))
        if entry is None:
            return None
        return dict(entry)

    def get_aggregate_revision(self, permit_id: str) -> int:
        """获取当前 aggregate revision。"""
        return self._aggregate_revisions.get(permit_id, 0)

    @property
    def transactions(self) -> list[DBTransaction]:
        return list(self._transactions.values())

    @property
    def backend_kind(self) -> str:
        return self.BACKEND_KIND
