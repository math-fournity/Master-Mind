"""Lease/Fence 协议 — at-least-once delivery + idempotent fenced commit。

lease 续期和 commit 都带 fence。新 worker 取得更高 fence 后，
旧 worker 的 cancel、artifact link、DB commit 和 queue ACK 全部拒绝。

协议：
1. acquire(aggregate_id, holder, ttl) → Lease（fence_token 单调递增）
2. renew(lease_id, fence_token, ttl) → 续期（fence 必须匹配）
3. release(lease_id, fence_token) → 释放（fence 必须匹配）
4. stale fence 检测：任何操作带旧 fence_token 都被拒绝

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..contracts.errors import LEASE_STATES, VerificationErrorCode as EC


class LeaseError(Exception):
    """Lease/Fence 协议错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class Lease:
    """单个 lease 的状态。"""

    lease_id: str
    aggregate_id: str
    holder: str
    fence_token: int
    acquired_at: str
    expires_at: str
    state: str = "ACTIVE"
    renew_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "lease_id": self.lease_id,
            "aggregate_id": self.aggregate_id,
            "holder": self.holder,
            "fence_token": self.fence_token,
            "acquired_at": self.acquired_at,
            "expires_at": self.expires_at,
            "state": self.state,
            "renew_count": self.renew_count,
        }

    @property
    def is_active(self) -> bool:
        return self.state == "ACTIVE"

    def is_expired(self, current_time: str) -> bool:
        return current_time >= self.expires_at


class LeaseFenceManager:
    """Lease/Fence 协议管理器。

    维护每个 aggregate 的 lease 链和 fence token 单调递增。
    新 lease 获得更高 fence，旧 lease 被自动 superseded。
    """

    def __init__(self) -> None:
        self._leases: dict[str, Lease] = {}  # lease_id → Lease
        self._aggregate_leases: dict[str, list[str]] = {}  # aggregate_id → [lease_id]
        self._aggregate_fence: dict[str, int] = {}  # aggregate_id → current fence
        self._next_fence: int = 1

    @property
    def leases(self) -> list[Lease]:
        return list(self._leases.values())

    def acquire(
        self,
        *,
        lease_id: str,
        aggregate_id: str,
        holder: str,
        ttl_seconds: int,
        current_time: str | None = None,
    ) -> Lease:
        """获取一个新 lease。

        新 lease 自动获得比当前 fence 更高的 fence_token。
        如果有旧 lease 仍 ACTIVE，旧 lease 被 superseded。
        """
        if lease_id in self._leases:
            raise LeaseError(
                EC.LEASE_ALREADY_HELD,
                f"lease_id {lease_id} already exists",
            )

        now = current_time or datetime.now(timezone.utc).isoformat()
        # 计算 expiry
        parsed = datetime.fromisoformat(now.replace("Z", "+00:00"))
        from datetime import timedelta

        expires = (parsed + timedelta(seconds=ttl_seconds)).isoformat()

        # 分配 fence_token（单调递增）
        current_fence = self._aggregate_fence.get(aggregate_id, 0)
        new_fence = current_fence + 1

        # supersed 旧 lease
        for old_lease_id in self._aggregate_leases.get(aggregate_id, []):
            old_lease = self._leases.get(old_lease_id)
            if old_lease and old_lease.state == "ACTIVE":
                old_lease.state = "SUPERSEDED"

        lease = Lease(
            lease_id=lease_id,
            aggregate_id=aggregate_id,
            holder=holder,
            fence_token=new_fence,
            acquired_at=now,
            expires_at=expires,
            state="ACTIVE",
        )
        self._leases[lease_id] = lease
        self._aggregate_leases.setdefault(aggregate_id, []).append(lease_id)
        self._aggregate_fence[aggregate_id] = new_fence
        return lease

    def renew(
        self,
        *,
        lease_id: str,
        fence_token: int,
        ttl_seconds: int,
        current_time: str | None = None,
    ) -> Lease:
        """续期一个 lease。

        fence_token 必须匹配。lease 必须仍 ACTIVE 且未过期。
        """
        lease = self._leases.get(lease_id)
        if lease is None:
            raise LeaseError(
                EC.LEASE_NOT_FOUND,
                f"lease {lease_id} not found",
            )

        if lease.fence_token != fence_token:
            raise LeaseError(
                EC.LEASE_RENEW_FENCE_MISMATCH,
                f"fence mismatch: lease has {lease.fence_token}, "
                f"request has {fence_token}",
            )

        if lease.state != "ACTIVE":
            raise LeaseError(
                EC.LEASE_STALE_FENCE,
                f"lease {lease_id} is {lease.state}, cannot renew",
            )

        now = current_time or datetime.now(timezone.utc).isoformat()
        if lease.is_expired(now):
            lease.state = "EXPIRED"
            raise LeaseError(
                EC.LEASE_EXPIRED,
                f"lease {lease_id} expired at {lease.expires_at}",
            )

        # 续期
        parsed = datetime.fromisoformat(now.replace("Z", "+00:00"))
        from datetime import timedelta

        lease.expires_at = (
            parsed + timedelta(seconds=ttl_seconds)
        ).isoformat()
        lease.renew_count += 1
        lease.state = "RENEWED"
        # 保持 ACTIVE 语义（RENEWED 表示续过但仍活）
        lease.state = "ACTIVE"
        return lease

    def release(
        self,
        *,
        lease_id: str,
        fence_token: int,
    ) -> Lease:
        """释放一个 lease。

        fence_token 必须匹配。
        """
        lease = self._leases.get(lease_id)
        if lease is None:
            raise LeaseError(
                EC.LEASE_NOT_FOUND,
                f"lease {lease_id} not found",
            )

        if lease.fence_token != fence_token:
            raise LeaseError(
                EC.LEASE_RELEASE_FENCE_MISMATCH,
                f"fence mismatch: lease has {lease.fence_token}, "
                f"request has {fence_token}",
            )

        if lease.state not in ("ACTIVE", "RENEWED"):
            raise LeaseError(
                EC.LEASE_STALE_FENCE,
                f"lease {lease_id} is {lease.state}, cannot release",
            )

        lease.state = "RELEASED"
        return lease

    def check_fence(self, aggregate_id: str, fence_token: int) -> bool:
        """检查 fence_token 是否是当前有效 fence。

        用于 commit/outbox 等操作前的 fence 验证。
        """
        current = self._aggregate_fence.get(aggregate_id, 0)
        return fence_token == current

    def is_stale_fence(self, aggregate_id: str, fence_token: int) -> bool:
        """检查 fence_token 是否已过期（比当前 fence 低）。"""
        current = self._aggregate_fence.get(aggregate_id, 0)
        return fence_token < current

    def get_current_fence(self, aggregate_id: str) -> int:
        """获取当前有效 fence_token。"""
        return self._aggregate_fence.get(aggregate_id, 0)

    def get_lease(self, lease_id: str) -> Lease | None:
        return self._leases.get(lease_id)

    def expire_stale(self, current_time: str) -> list[str]:
        """过期所有已超时的 ACTIVE lease，返回过期的 lease_id 列表。"""
        expired: list[str] = []
        for lease in self._leases.values():
            if lease.state == "ACTIVE" and lease.is_expired(current_time):
                lease.state = "EXPIRED"
                expired.append(lease.lease_id)
        return expired
