"""ResourceContract — WP-EX1 等资源合同。

关键约束（blocker）：
- 所有 arm 必须有对等资源预算（EX_ARMS_NOT_EQUAL_RESOURCE）
- token budget, wallclock budget, tool budget, call budget
- Distractor 不对等 = blocker（EX1 在实验层强制）
- 冻结后不可变（EX_RESOURCE_CONTRACT_NOT_FROZEN）
- content_hash 正确（EX_RESOURCE_CONTRACT_HASH_MISMATCH）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_SCHEMA_ID = "seven/resource-contract"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"

# 必需的预算字段
_REQUIRED_BUDGET_FIELDS = (
    "token_budget",
    "wallclock_seconds",
    "tool_budget",
    "call_budget",
    "cost_microunits",
)


@dataclass(frozen=True)
class ResourceContract:
    """等资源合同——所有 arm 必须共享同一 ResourceContract。

    字段：
        contract_id: 唯一标识
        token_budget: token 预算上限
        wallclock_seconds: 墙钟预算（秒）
        tool_budget: 工具调用预算上限
        call_budget: 模型调用预算上限
        cost_microunits: 成本预算（微单位）
        frozen: 是否冻结
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    contract_id: str
    token_budget: int = 0
    wallclock_seconds: int = 0
    tool_budget: int = 0
    call_budget: int = 0
    cost_microunits: int = 0
    frozen: bool = False
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "contract_id": self.contract_id,
            "token_budget": self.token_budget,
            "wallclock_seconds": self.wallclock_seconds,
            "tool_budget": self.tool_budget,
            "call_budget": self.call_budget,
            "cost_microunits": self.cost_microunits,
            "frozen": self.frozen,
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def budget_dict(self) -> dict[str, int]:
        return {
            "token_budget": self.token_budget,
            "wallclock_seconds": self.wallclock_seconds,
            "tool_budget": self.tool_budget,
            "call_budget": self.call_budget,
            "cost_microunits": self.cost_microunits,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


def make_resource_contract(
    *,
    contract_id: str,
    token_budget: int = 8192,
    wallclock_seconds: int = 600,
    tool_budget: int = 0,
    call_budget: int = 1,
    cost_microunits: int = 0,
    frozen: bool = True,
    frozen_at: str = "2026-08-14T12:00:00Z",
) -> ResourceContract:
    rc = ResourceContract(
        contract_id=contract_id,
        token_budget=token_budget,
        wallclock_seconds=wallclock_seconds,
        tool_budget=tool_budget,
        call_budget=call_budget,
        cost_microunits=cost_microunits,
        frozen=frozen,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(rc, content_hash=rc.compute_content_hash())


@dataclass(frozen=True)
class ResourceContractVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    contract_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_resource_contract(
    contract: ResourceContract,
) -> ResourceContractVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = contract.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # 必需预算字段
    for fname in _REQUIRED_BUDGET_FIELDS:
        val = d.get(fname)
        if not isinstance(val, int) or val < 0:
            errors.append(EC.EX_RESOURCE_BUDGET_INVALID)
            details.append(f"{fname} must be a non-negative int, got {val!r}")

    # 冻结检查
    if not contract.frozen:
        errors.append(EC.EX_RESOURCE_CONTRACT_NOT_FROZEN)
        details.append("ResourceContract must be frozen before experiment start")

    # content_hash
    if not contract.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif contract.content_hash != contract.compute_content_hash():
        errors.append(EC.EX_RESOURCE_CONTRACT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {contract.content_hash}, "
            f"computed {contract.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return ResourceContractVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        contract_id=contract.contract_id,
    )


def contracts_equal(
    a: ResourceContract,
    b: ResourceContract,
) -> bool:
    """检查两个 ResourceContract 的预算是否对等。"""
    return a.budget_dict() == b.budget_dict()
