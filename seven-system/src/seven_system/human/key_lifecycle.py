"""KeyRegistry — 签名密钥生命周期管理。

每个 HumanGateKeyRecord 包含：
- key_id：唯一标识
- actor_id：密钥绑定的 actor
- public_key_sha256：公钥 hash
- eligible_roles：该密钥可用于签名的角色
- valid_from / valid_to：有效期
- status：ACTIVE / REVOKED / EXPIRED / PENDING
- provisioning_ref：provisioning 决定引用
- rotation_predecessor：轮换前驱 key_id
- revocation_ref：撤销记录引用

生命周期：
1. Provision：独立 provisioning actor 注册公钥与 actor/role 绑定
2. Rotate：新 key 建新 Record 并引用 predecessor；旧 key 保留验历史签名
3. Revoke：记录 effective time、reason、scope；effective time 后的签名拒绝
4. Expire：签名接受时同时检查 key 有效期

硬约束：
- 私钥不进 Git/DB/Redis/普通 D 盘/模型 workspace
- 模型或实施者写入一个 Base64 字符串不等于拥有有效签名
- 不得由待审对象的作者自我授权 provision

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    HUMAN_GATE_ROLES,
    KEY_STATUSES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..contracts.security_contract import _check_canonical_utc


_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_ID_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9._:@+-]{0,254}[A-Za-z0-9])?$")


@dataclass(frozen=True)
class KeyRecord:
    """单个签名密钥的注册记录。不可变。"""

    key_id: str
    actor_id: str
    public_key_sha256: str
    eligible_roles: frozenset[str]
    valid_from: str
    valid_to: str
    status: str
    provisioning_ref: str
    rotation_predecessor: str | None
    revocation_ref: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "key_id": self.key_id,
            "actor_id": self.actor_id,
            "public_key_sha256": self.public_key_sha256,
            "eligible_roles": sorted(self.eligible_roles),
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
            "status": self.status,
            "provisioning_ref": self.provisioning_ref,
            "rotation_predecessor": self.rotation_predecessor,
            "revocation_ref": self.revocation_ref,
        }


class KeyRegistry:
    """KeyRegistry — 签名密钥生命周期注册表。

    维护 key_id → KeyRecord 映射。
    支持注册（provision）、撤销（revoke）、过期检查、验证时查询。
    """

    def __init__(self) -> None:
        self._keys: dict[str, KeyRecord] = {}
        self._public_keys: dict[str, bytes] = {}  # P0-B: key_id → raw public key bytes

    def store_public_key(self, key_id: str, public_key_bytes: bytes) -> None:
        """P0-B: 存储密钥的原始公钥字节，用于真实 Ed25519 验签。"""
        self._public_keys[key_id] = public_key_bytes

    def get_public_key(self, key_id: str) -> bytes | None:
        """P0-B: 获取密钥的原始公钥字节。"""
        return self._public_keys.get(key_id)

    def provision(
        self,
        *,
        key_id: str,
        actor_id: str,
        public_key_sha256: str,
        eligible_roles: frozenset[str],
        valid_from: str,
        valid_to: str,
        provisioning_ref: str,
        rotation_predecessor: str | None = None,
    ) -> VerificationResult:
        """注册一个新签名密钥。

        检查：
        - key_id 非空且唯一
        - actor_id 非空
        - public_key_sha256 是合法 sha256
        - eligible_roles 都是合法角色
        - valid_from / valid_to 为 canonical UTC 且 from < to
        - provisioning_ref 非空（不得自我授权）
        - rotation_predecessor 如存在必须在 registry 中
        """
        errors: list[EC] = []
        details: list[str] = []

        if not key_id or not _ID_RE.match(key_id):
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"invalid key_id: {key_id!r}")

        if not actor_id:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("actor_id must not be empty")

        if not isinstance(public_key_sha256, str) or not _HASH_RE.match(public_key_sha256):
            errors.append(EC.OBJECT_HASH_MISMATCH)
            details.append(f"invalid public_key_sha256: {public_key_sha256!r}")
        elif public_key_sha256 == "0" * 64:
            # P0-B: 全0公钥 hash 必须拒绝（不能用作占位符）
            errors.append(EC.OBJECT_HASH_MISMATCH)
            details.append("public_key_sha256 must not be all-zero")

        invalid_roles = set(eligible_roles) - HUMAN_GATE_ROLES
        if invalid_roles:
            errors.append(EC.KEY_ROLE_NOT_ELIGIBLE)
            details.append(f"unknown eligible_roles: {invalid_roles}")

        if not _check_canonical_utc(valid_from):
            errors.append(EC.TIME_NOT_CANONICAL_UTC)
            details.append(f"valid_from not canonical UTC: {valid_from!r}")
        if not _check_canonical_utc(valid_to):
            errors.append(EC.TIME_NOT_CANONICAL_UTC)
            details.append(f"valid_to not canonical UTC: {valid_to!r}")
        if _check_canonical_utc(valid_from) and _check_canonical_utc(valid_to):
            if valid_from >= valid_to:
                errors.append(EC.TIME_WINDOW_INVALID)
                details.append(f"valid_from {valid_from} >= valid_to {valid_to}")

        if not provisioning_ref:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("provisioning_ref must not be empty (no self-authorization)")

        if key_id in self._keys:
            errors.append(EC.KEY_NOT_REGISTERED)
            details.append(f"key {key_id} already registered")

        if rotation_predecessor is not None:
            if rotation_predecessor not in self._keys:
                errors.append(EC.KEY_NOT_REGISTERED)
                details.append(f"rotation_predecessor {rotation_predecessor} not found")

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        record = KeyRecord(
            key_id=key_id,
            actor_id=actor_id,
            public_key_sha256=public_key_sha256,
            eligible_roles=frozenset(eligible_roles),
            valid_from=valid_from,
            valid_to=valid_to,
            status="ACTIVE",
            provisioning_ref=provisioning_ref,
            rotation_predecessor=rotation_predecessor,
            revocation_ref=None,
        )
        self._keys[key_id] = record
        return VerificationResult(verdict="PASS")

    def revoke(
        self,
        key_id: str,
        *,
        revocation_ref: str,
    ) -> VerificationResult:
        """撤销一个签名密钥。

        检查：
        - key_id 存在
        - key 当前状态为 ACTIVE
        - revocation_ref 非空
        """
        errors: list[EC] = []
        details: list[str] = []

        record = self._keys.get(key_id)
        if record is None:
            errors.append(EC.KEY_NOT_REGISTERED)
            details.append(f"key {key_id} not found")
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        if record.status == "REVOKED":
            errors.append(EC.KEY_REVOKED)
            details.append(f"key {key_id} already revoked")

        if not revocation_ref:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("revocation_ref must not be empty")

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        self._keys[key_id] = KeyRecord(
            key_id=record.key_id,
            actor_id=record.actor_id,
            public_key_sha256=record.public_key_sha256,
            eligible_roles=record.eligible_roles,
            valid_from=record.valid_from,
            valid_to=record.valid_to,
            status="REVOKED",
            provisioning_ref=record.provisioning_ref,
            rotation_predecessor=record.rotation_predecessor,
            revocation_ref=revocation_ref,
        )
        return VerificationResult(verdict="PASS")

    def get(self, key_id: str) -> KeyRecord | None:
        """获取 key 记录。"""
        return self._keys.get(key_id)

    def check_key(
        self,
        key_id: str,
        *,
        expected_actor_id: str | None = None,
        required_role: str | None = None,
        evaluation_time: str,
    ) -> VerificationResult:
        """验证签名密钥在指定时间点是否有效。

        检查：
        - key 存在
        - key 状态为 ACTIVE
        - evaluation_time 在 [valid_from, valid_to) 内
        - expected_actor_id 匹配（如提供）
        - required_role 在 eligible_roles 中（如提供）
        """
        errors: list[EC] = []
        details: list[str] = []

        record = self._keys.get(key_id)
        if record is None:
            errors.append(EC.KEY_NOT_REGISTERED)
            details.append(f"key {key_id} not found")
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)

        if record.status == "REVOKED":
            errors.append(EC.KEY_REVOKED)
            details.append(f"key {key_id} is revoked")

        if record.status == "EXPIRED":
            errors.append(EC.KEY_EXPIRED)
            details.append(f"key {key_id} is expired")

        if record.status == "PENDING":
            errors.append(EC.KEY_NOT_YET_VALID)
            details.append(f"key {key_id} is pending")

        # 时间窗检查
        if _check_canonical_utc(evaluation_time):
            if evaluation_time < record.valid_from:
                errors.append(EC.KEY_NOT_YET_VALID)
                details.append(
                    f"evaluation_time {evaluation_time} < valid_from {record.valid_from}"
                )
            if evaluation_time >= record.valid_to:
                errors.append(EC.KEY_EXPIRED)
                details.append(
                    f"evaluation_time {evaluation_time} >= valid_to {record.valid_to}"
                )

        if expected_actor_id is not None and record.actor_id != expected_actor_id:
            errors.append(EC.KEY_ACTOR_MISMATCH)
            details.append(
                f"key {key_id} bound to actor {record.actor_id}, "
                f"not {expected_actor_id}"
            )

        if required_role is not None and required_role not in record.eligible_roles:
            errors.append(EC.KEY_ROLE_NOT_ELIGIBLE)
            details.append(
                f"key {key_id} not eligible for role {required_role}, "
                f"has {sorted(record.eligible_roles)}"
            )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)

    @property
    def size(self) -> int:
        return len(self._keys)

    def list_keys(self) -> list[KeyRecord]:
        return list(self._keys.values())
