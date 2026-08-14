"""CommitIntent — final rename 前的 durable intent。

CommitIntent 在 final artifact rename 前用有效 fence 与当前 permit 持久化，
至少绑定 job、attempt、input hashes、manifest hash、预期 terminal、
目标 CAS URI、authorization/permit hash 和 expiry。

协议：
1. record(intent) → 持久化 CommitIntent（状态 PENDING）
2. consume(intent_id, fence_token, current_time) → 消费 intent（状态 CONSUMED）
3. revoke(intent_id) → 撤销 intent（状态 REVOKED）
4. verify(intent, job/attempt/input/manifest/CAS/permit/fence) → 逐字段验证

不变量：
- intent 在 seal/commit 前必须存在且 PENDING
- fence_token 必须是当前有效 fence
- expiry 未过期
- permit 未撤销
- input_hash / manifest_hash 不可漂移

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    COMMIT_INTENT_STATES,
    VerificationErrorCode as EC,
)


class CommitIntentError(Exception):
    """CommitIntent 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class RuntimeCommitIntent:
    """Durable CommitIntent — 在 final rename 前持久化。

    绑定 job、attempt、input hashes、manifest hash、
    预期 terminal、目标 CAS URI、authorization/permit hash 和 expiry。
    """

    intent_id: str
    job_id: str
    attempt_id: str
    input_hash: str
    manifest_hash: str
    expected_terminal: str
    target_cas_uri: str
    authorization_hash: str
    permit_hash: str
    fence_token: int
    expiry: str
    created_at: str
    state: str = "PENDING"  # PENDING / CONSUMED / REVOKED / EXPIRED

    def to_dict(self) -> dict[str, Any]:
        return {
            "intent_id": self.intent_id,
            "job_id": self.job_id,
            "attempt_id": self.attempt_id,
            "input_hash": self.input_hash,
            "manifest_hash": self.manifest_hash,
            "expected_terminal": self.expected_terminal,
            "target_cas_uri": self.target_cas_uri,
            "authorization_hash": self.authorization_hash,
            "permit_hash": self.permit_hash,
            "fence_token": self.fence_token,
            "expiry": self.expiry,
            "created_at": self.created_at,
            "state": self.state,
        }

    @property
    def is_pending(self) -> bool:
        return self.state == "PENDING"

    @property
    def is_consumed(self) -> bool:
        return self.state == "CONSUMED"

    @property
    def is_revoked(self) -> bool:
        return self.state == "REVOKED"

    def is_expired(self, current_time: str) -> bool:
        return current_time >= self.expiry


class CommitIntentStore:
    """CommitIntent 持久化存储（内存模拟）。

    管理 CommitIntent 的生命周期：record → consume / revoke / expire。
    """

    def __init__(self) -> None:
        self._intents: dict[str, RuntimeCommitIntent] = {}

    @property
    def intents(self) -> list[RuntimeCommitIntent]:
        return list(self._intents.values())

    def record(self, intent: RuntimeCommitIntent) -> RuntimeCommitIntent:
        """记录一个新 CommitIntent。"""
        if intent.intent_id in self._intents:
            raise CommitIntentError(
                EC.COMMIT_INTENT_ALREADY_CONSUMED,
                f"intent {intent.intent_id} already exists",
            )
        if intent.state not in ("PENDING",):
            raise CommitIntentError(
                EC.COMMIT_INTENT_ALREADY_CONSUMED,
                f"new intent must be PENDING, got {intent.state}",
            )
        self._intents[intent.intent_id] = intent
        return intent

    def consume(
        self,
        *,
        intent_id: str,
        fence_token: int,
        current_time: str,
        current_fence: int,
    ) -> RuntimeCommitIntent:
        """消费一个 CommitIntent。

        验证：
        1. intent 存在
        2. intent 状态为 PENDING
        3. fence_token 匹配
        4. fence_token 是当前有效 fence
        5. 未过期
        """
        intent = self._intents.get(intent_id)
        if intent is None:
            raise CommitIntentError(
                EC.SEAL_COMMIT_INTENT_MISSING,
                f"intent {intent_id} not found",
            )

        if intent.state != "PENDING":
            raise CommitIntentError(
                EC.COMMIT_INTENT_ALREADY_CONSUMED,
                f"intent {intent_id} is {intent.state}, cannot consume",
            )

        if intent.fence_token != fence_token:
            raise CommitIntentError(
                EC.COMMIT_INTENT_FENCE_STALE,
                f"fence mismatch: intent has {intent.fence_token}, "
                f"request has {fence_token}",
            )

        if intent.fence_token != current_fence:
            raise CommitIntentError(
                EC.COMMIT_INTENT_FENCE_STALE,
                f"intent fence {intent.fence_token} != "
                f"current fence {current_fence}",
            )

        if intent.is_expired(current_time):
            intent.state = "EXPIRED"
            raise CommitIntentError(
                EC.COMMIT_INTENT_EXPIRED,
                f"intent {intent_id} expired at {intent.expiry}",
            )

        intent.state = "CONSUMED"
        return intent

    def revoke(self, intent_id: str) -> RuntimeCommitIntent:
        """撤销一个 CommitIntent。"""
        intent = self._intents.get(intent_id)
        if intent is None:
            raise CommitIntentError(
                EC.SEAL_COMMIT_INTENT_MISSING,
                f"intent {intent_id} not found",
            )
        if intent.state == "CONSUMED":
            raise CommitIntentError(
                EC.COMMIT_INTENT_ALREADY_CONSUMED,
                f"intent {intent_id} already consumed, cannot revoke",
            )
        intent.state = "REVOKED"
        return intent

    def expire(self, intent_id: str, current_time: str) -> RuntimeCommitIntent:
        """过期一个 CommitIntent。"""
        intent = self._intents.get(intent_id)
        if intent is None:
            raise CommitIntentError(
                EC.SEAL_COMMIT_INTENT_MISSING,
                f"intent {intent_id} not found",
            )
        if intent.is_expired(current_time) and intent.state == "PENDING":
            intent.state = "EXPIRED"
        return intent

    def get(self, intent_id: str) -> RuntimeCommitIntent | None:
        return self._intents.get(intent_id)

    def verify_intent(
        self,
        *,
        intent_id: str,
        job_id: str,
        attempt_id: str,
        input_hash: str,
        manifest_hash: str,
        target_cas_uri: str,
        permit_hash: str,
        fence_token: int,
    ) -> list[tuple[EC, str]]:
        """逐字段验证 CommitIntent。

        用于 reconcile 时验证 sealed bundle 与 intent 的字段匹配。
        """
        errors: list[tuple[EC, str]] = []
        intent = self._intents.get(intent_id)
        if intent is None:
            errors.append(
                (EC.SEAL_COMMIT_INTENT_MISSING, f"intent {intent_id} not found")
            )
            return errors

        if intent.job_id != job_id:
            errors.append(
                (
                    EC.COMMIT_INTENT_INPUT_HASH_DRIFT,
                    f"job_id mismatch: intent={intent.job_id}, actual={job_id}",
                )
            )

        if intent.attempt_id != attempt_id:
            errors.append(
                (
                    EC.COMMIT_INTENT_INPUT_HASH_DRIFT,
                    f"attempt_id mismatch: intent={intent.attempt_id}, "
                    f"actual={attempt_id}",
                )
            )

        if intent.input_hash != input_hash:
            errors.append(
                (
                    EC.COMMIT_INTENT_INPUT_HASH_DRIFT,
                    f"input_hash mismatch: intent={intent.input_hash}, "
                    f"actual={input_hash}",
                )
            )

        if intent.manifest_hash != manifest_hash:
            errors.append(
                (
                    EC.COMMIT_INTENT_MANIFEST_HASH_MISMATCH,
                    f"manifest_hash mismatch: intent={intent.manifest_hash}, "
                    f"actual={manifest_hash}",
                )
            )

        if intent.target_cas_uri != target_cas_uri:
            errors.append(
                (
                    EC.COMMIT_INTENT_INPUT_HASH_DRIFT,
                    f"target_cas_uri mismatch: intent={intent.target_cas_uri}, "
                    f"actual={target_cas_uri}",
                )
            )

        if intent.permit_hash != permit_hash:
            errors.append(
                (
                    EC.COMMIT_INTENT_PERMIT_REVOKED,
                    f"permit_hash mismatch: intent={intent.permit_hash}, "
                    f"actual={permit_hash}",
                )
            )

        if intent.fence_token != fence_token:
            errors.append(
                (
                    EC.COMMIT_INTENT_FENCE_STALE,
                    f"fence_token mismatch: intent={intent.fence_token}, "
                    f"actual={fence_token}",
                )
            )

        return errors
