"""MechanismContract — 冻结的机制定义。

来自 docs/implementation/04-object-and-schema-catalog.md：

MechanismContract 是 P3A 出题链的根冻结对象。它定义数学机制的核心和边界。
任何变化都会使 content_hash 改变，从而失效所有下游引用。

硬约束：
- content_hash = sha256(canonical_json(object with content_hash=null))
- 一旦冻结，不可修改；修改 = 新对象（新 hash）
- 下游对象通过 content_hash 引用，hash 不一致即 BLOCK

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/mechanism-contract"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "MechanismContract"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class MechanismContract:
    """MechanismContract — 冻结的机制定义。不可变。

    定义数学机制的核心（core）和边界（boundary）。
    content_hash 覆盖全部字段；变化即新对象。
    """

    mechanism_id: str
    core: str
    boundary: str
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    content_hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "mechanism_id": self.mechanism_id,
            "core": self.core,
            "boundary": self.boundary,
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }

    @property
    def ref_and_hash(self) -> dict[str, str]:
        return {
            "ref_id": self.mechanism_id,
            "sha256": self.content_hash,
        }


def _compute_content_hash(obj: dict[str, Any]) -> str:
    """计算 content_hash = sha256(canonical_json(object with content_hash=null))。"""
    o = dict(obj)
    o["content_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def build_mechanism_contract(
    *,
    mechanism_id: str,
    core: str,
    boundary: str,
) -> MechanismContract:
    """构建 MechanismContract，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "mechanism_id": mechanism_id,
        "core": core,
        "boundary": boundary,
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return MechanismContract(
        mechanism_id=mechanism_id,
        core=core,
        boundary=boundary,
        content_hash=content_hash,
    )


def verify_mechanism_contract(
    contract: dict[str, Any] | MechanismContract,
) -> VerificationResult:
    """验证 MechanismContract 的结构合法性。

    检查：
    1. schema_id / schema_version / object_type 常量
    2. mechanism_id 非空
    3. core / boundary 非空
    4. content_hash_algorithm 正确
    5. content_hash 正确（重算）
    """
    if isinstance(contract, MechanismContract):
        contract = contract.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if contract.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if contract.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if contract.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not contract.get("mechanism_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("mechanism_id must not be empty")
    if not contract.get("core"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("core must not be empty")
    if not contract.get("boundary"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("boundary must not be empty")

    if contract.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {contract.get('content_hash_algorithm')}")

    computed = _compute_content_hash(contract)
    if contract.get("content_hash") != computed:
        errors.append(EC.QA_MECHANISM_CONTRACT_CHANGED)
        details.append(
            f"content_hash mismatch: expected {computed}, got {contract.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
