"""Vault 敏感度级别与注册表。

四个级别（有序，从低到高）：
  PUBLIC           — 任何 principal 可读
  RESTRICTED       — 需要能力授权
  SOLUTION_BEARING — 包含答案，只有特定角色可派生 view
  HOLDOUT_BEARING  — 包含 holdout，最高隔离，普通 worker 永不可读

TARGET_SOLVER 只能读取 PUBLIC 或 RESTRICTED 的 derived view，
不能直接接触 SOLUTION_BEARING 或 HOLDOUT_BEARING 对象。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import SENSITIVITY_LEVELS, VerificationErrorCode as EC


class SensitivityLevel:
    """敏感度级别常量与比较逻辑。"""

    PUBLIC = "PUBLIC"
    RESTRICTED = "RESTRICTED"
    SOLUTION_BEARING = "SOLUTION_BEARING"
    HOLDOUT_BEARING = "HOLDOUT_BEARING"

    _ORDER: dict[str, int] = {
        "PUBLIC": 0,
        "RESTRICTED": 1,
        "SOLUTION_BEARING": 2,
        "HOLDOUT_BEARING": 3,
    }

    @classmethod
    def all_levels(cls) -> tuple[str, ...]:
        return SENSITIVITY_LEVELS

    @classmethod
    def is_valid(cls, level: str) -> bool:
        return level in cls._ORDER

    @classmethod
    def rank(cls, level: str) -> int:
        if level not in cls._ORDER:
            raise ValueError(f"unknown sensitivity level: {level}")
        return cls._ORDER[level]

    @classmethod
    def is_at_least(cls, level: str, threshold: str) -> bool:
        """检查 level >= threshold。"""
        return cls.rank(level) >= cls.rank(threshold)

    @classmethod
    def is_higher_than(cls, level: str, other: str) -> bool:
        """检查 level > other。"""
        return cls.rank(level) > cls.rank(other)

    @classmethod
    def solver_accessible(cls, level: str) -> bool:
        """TARGET_SOLVER 只能访问 PUBLIC 或 RESTRICTED。"""
        return level in (cls.PUBLIC, cls.RESTRICTED)


@dataclass
class VaultObjectRecord:
    """Vault 中一个对象的注册记录。"""

    object_id: str
    object_sha256: str
    sensitivity: str
    size_bytes: int = 0
    media_type: str = ""
    owner_case: str = ""
    owner_release: str = ""
    owner_invocation: str = ""
    source_artifact_ref: str = ""
    derivation_rule_ref: str = ""
    allowed_roles: list[str] = field(default_factory=list)
    purpose: str = ""
    expiry: str = ""
    revocation_handle: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "object_id": self.object_id,
            "object_sha256": self.object_sha256,
            "sensitivity": self.sensitivity,
            "size_bytes": self.size_bytes,
            "media_type": self.media_type,
            "owner_case": self.owner_case,
            "owner_release": self.owner_release,
            "owner_invocation": self.owner_invocation,
            "source_artifact_ref": self.source_artifact_ref,
            "derivation_rule_ref": self.derivation_rule_ref,
            "allowed_roles": list(self.allowed_roles),
            "purpose": self.purpose,
            "expiry": self.expiry,
            "revocation_handle": self.revocation_handle,
        }


class SensitivityRegistry:
    """Vault 对象敏感度注册表。

    SIDE_EFFECT_FREE：纯内存实现，不接触真实 D 盘或 DB。
    记录每个 Vault 对象的 object_id → sensitivity 映射，
    供 VaultBroker 在派生 view 前检查敏感度约束。
    """

    def __init__(self) -> None:
        self._objects: dict[str, VaultObjectRecord] = {}

    def register(self, record: VaultObjectRecord) -> None:
        """注册一个 Vault 对象。重复 object_id 覆盖（注册表是可变的控制面状态）。"""
        if not SensitivityLevel.is_valid(record.sensitivity):
            raise _VaultError(
                EC.VAULT_OBJECT_HASH_MISMATCH,
                f"invalid sensitivity level: {record.sensitivity}",
            )
        self._objects[record.object_id] = record

    def get(self, object_id: str) -> VaultObjectRecord | None:
        return self._objects.get(object_id)

    def get_sensitivity(self, object_id: str) -> str | None:
        record = self._objects.get(object_id)
        return record.sensitivity if record else None

    def check_solver_access(self, object_id: str) -> bool:
        """检查 TARGET_SOLVER 是否可以访问此对象的 derived view。"""
        record = self._objects.get(object_id)
        if record is None:
            return False
        return SensitivityLevel.solver_accessible(record.sensitivity)

    def check_role_access(self, object_id: str, role: str) -> bool:
        """检查指定角色是否可以访问此对象。"""
        record = self._objects.get(object_id)
        if record is None:
            return False
        if not record.allowed_roles:
            return True  # 未指定 allowed_roles = 全部允许（仍需 capability）
        return role in record.allowed_roles

    def list_objects(self) -> list[VaultObjectRecord]:
        return list(self._objects.values())

    def __len__(self) -> int:
        return len(self._objects)


class _VaultError(Exception):
    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)
