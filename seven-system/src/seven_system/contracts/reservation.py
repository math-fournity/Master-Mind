"""ReservationBackendPort — GV0 冻结的原子预留接口。

SecurityContractVerifier 的原子预留接口由 GV0 冻结。
WP-DB1I 只实现 SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER 后端，
WP-RT1 只实现 canonical DB expected-revision transaction 后端。
任一后端不得复制、放宽或跳过 GV0 的 1-7 步验证顺序。
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Protocol

from ..hashing import canonical_json_bytes
from .errors import (
    CONSUMPTION_STATUSES,
    VerificationErrorCode as EC,
)


@dataclass(frozen=True)
class Allowance:
    """额度快照——用于守恒检查。"""

    invocations: int = 0
    solver_launches: int = 0
    database_writes: int = 0
    redis_writes: int = 0
    d_volume_writes: int = 0
    human_gate_commits: int = 0
    active_release_changes: int = 0
    tokens: int = 0
    cost_microunits: int = 0

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Allowance":
        return cls(
            invocations=d.get("invocations", 0),
            solver_launches=d.get("solver_launches", 0),
            database_writes=d.get("database_writes", 0),
            redis_writes=d.get("redis_writes", 0),
            d_volume_writes=d.get("d_volume_writes", 0),
            human_gate_commits=d.get("human_gate_commits", 0),
            active_release_changes=d.get("active_release_changes", 0),
            tokens=d.get("tokens", 0),
            cost_microunits=d.get("cost_microunits", 0),
        )

    def add(self, other: "Allowance") -> "Allowance":
        return Allowance(
            invocations=self.invocations + other.invocations,
            solver_launches=self.solver_launches + other.solver_launches,
            database_writes=self.database_writes + other.database_writes,
            redis_writes=self.redis_writes + other.redis_writes,
            d_volume_writes=self.d_volume_writes + other.d_volume_writes,
            human_gate_commits=self.human_gate_commits + other.human_gate_commits,
            active_release_changes=self.active_release_changes
            + other.active_release_changes,
            tokens=self.tokens + other.tokens,
            cost_microunits=self.cost_microunits + other.cost_microunits,
        )

    def is_zero(self) -> bool:
        return all(
            getattr(self, f) == 0
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
            )
        )

    def is_nonzero(self) -> bool:
        return not self.is_zero()


class ReservationBackendPort(Protocol):
    """原子预留后端接口（GV0 冻结）。

    实现者：
    - SIDE_EFFECT_FREE_REFERENCE: GV0 自身的 side-effect-free 参考后端
    - SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER: WP-DB1I 实现
    - DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER: WP-RT1 实现
    """

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

        返回 reservation_transaction_receipt。
        重复 ordinal 必须拒绝（EC.DUPLICATE_ORDINAL）。
        stale fence 必须拒绝（EC.STALE_FENCE）。
        预留不原子必须拒绝（EC.RESERVATION_NOT_ATOMIC）。
        """
        ...

    def consume(
        self,
        *,
        permit_id: str,
        consumption_ordinal: int,
        fence_token: int,
        actual_side_effects: dict[str, Any],
    ) -> dict[str, Any]:
        """消耗一个已预留的 ordinal。

        fence_token 必须匹配预留时的值。
        actual_side_effects 不能超过预留额度。
        """
        ...

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
        ...

    def get_state(
        self, *, permit_id: str, consumption_ordinal: int
    ) -> dict[str, Any] | None:
        """查询某个 ordinal 的当前状态。"""
        ...


class SideEffectFreeReferenceBackend:
    """GV0 的 side-effect-free 参考后端。

    使用内存字典模拟原子预留。仅用于隔离 fixture 测试，
    不用于真实 DB 或 D 盘 ledger。
    """

    def __init__(self) -> None:
        self._entries: dict[tuple[str, int], dict[str, Any]] = {}
        self._fences: dict[tuple[str, int], int] = {}
        self._aggregate_revisions: dict[str, int] = {}

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
            raise _ReservationError(
                EC.DUPLICATE_ORDINAL,
                f"ordinal {consumption_ordinal} already reserved for "
                f"permit {permit_id}",
            )
        current_rev = self._aggregate_revisions.get(permit_id, 0)
        if expected_aggregate_revision != current_rev:
            raise _ReservationError(
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
            raise _ReservationError(
                EC.RESERVATION_NOT_ATOMIC,
                f"no reservation for ordinal {consumption_ordinal}",
            )
        if self._fences.get(key) != fence_token:
            raise _ReservationError(
                EC.STALE_FENCE,
                f"fence mismatch for ordinal {consumption_ordinal}",
            )
        if entry["status"] != "RESERVED":
            raise _ReservationError(
                EC.APPEND_ONLY_VIOLATION,
                f"ordinal {consumption_ordinal} already "
                f"{entry['status']}",
            )
        # 验证 actual 不超过 reserved
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
                raise _ReservationError(
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
            raise _ReservationError(
                EC.RESERVATION_NOT_ATOMIC,
                f"no reservation for ordinal {consumption_ordinal}",
            )
        if self._fences.get(key) != fence_token:
            raise _ReservationError(
                EC.STALE_FENCE,
                f"fence mismatch for ordinal {consumption_ordinal}",
            )
        if entry["status"] != "RESERVED":
            raise _ReservationError(
                EC.APPEND_ONLY_VIOLATION,
                f"ordinal {consumption_ordinal} already "
                f"{entry['status']}",
            )
        if not proof_not_started_refs:
            raise _ReservationError(
                EC.RELEASE_WITHOUT_PROOF,
                f"release requires proof_not_started_refs",
            )
        entry["status"] = "RELEASED_UNUSED"
        entry["released_allowance"] = entry["reserved_budget"]
        entry["held_allowance"] = {}
        return {
            "release_receipt": {
                "permit_id": permit_id,
                "consumption_ordinal": consumption_ordinal,
                "status": "RELEASED_UNUSED",
            }
        }

    def get_state(
        self, *, permit_id: str, consumption_ordinal: int
    ) -> dict[str, Any] | None:
        return self._entries.get((permit_id, consumption_ordinal))


class _ReservationError(Exception):
    def __init__(self, code: VerificationErrorCode, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)
