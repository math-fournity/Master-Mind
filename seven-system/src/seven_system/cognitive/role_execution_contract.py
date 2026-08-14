"""RoleExecutionContract — 绑定角色 + profile + view + tool policy + adapter + capability。

每个机器角色 job 必须冻结一个 RoleExecutionContract，精确绑定：
- role_type_registry_ref_and_hash：引用冻结的 RoleRegistry
- role_type_id：精确角色标识
- carrier_profile_ref_and_hash：carrier profile 引用
- view_policy_ref_and_hash：view policy 引用
- tool_policy_ref_and_hash：tool policy 引用
- adapter_kind：适配器类型（FAKE / DEVIN_CLI / CODEX_EXEC / OPENAI_RESPONSES）
- vault_access_capability_ref_and_hash：Vault 访问能力引用
- output_schema_ref_and_hash：输出 schema 引用
- budget_contract_ref_and_hash：预算合同引用

硬约束：
- contract_hash = sha256(canonical_json(object with contract_hash=null))
- 未知 role、已退役 role、hash 不一致 → BLOCK
- role 没有 required profile → BLOCK
- role 没有 view policy → BLOCK
- role tool policy 允许工具（非 NO_TOOLS）→ BLOCK（认知角色默认无工具）
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    MODEL_ROLE_ADAPTER_KINDS,
    TOOL_POLICY_KINDS,
    VIEW_POLICY_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from .role_registry import RoleRegistry, RoleDefinition


_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_EXACT_ID_RE = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._:@+-]{0,254}[A-Za-z0-9])?$"
)

_CONTRACT_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-contract_hash-null)"


@dataclass(frozen=True)
class RoleExecutionContract:
    """RoleExecutionContract 数据对象。不可变。

    精确绑定角色执行所需的全部引用。
    """

    role_job_id: str
    epoch_id: str
    role_type_registry_ref_and_hash: dict[str, str]
    role_type_id: str
    carrier_profile_ref_and_hash: dict[str, str]
    view_policy_ref_and_hash: dict[str, str]
    tool_policy_ref_and_hash: dict[str, str]
    adapter_kind: str
    vault_access_capability_ref_and_hash: dict[str, str]
    output_schema_ref_and_hash: dict[str, str]
    budget_contract_ref_and_hash: dict[str, str]
    prompt_release_ref_and_hash: dict[str, str]
    idempotency_key: str
    contract_hash_algorithm: str
    contract_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "role_job_id": self.role_job_id,
            "epoch_id": self.epoch_id,
            "role_type_registry_ref_and_hash": dict(self.role_type_registry_ref_and_hash),
            "role_type_id": self.role_type_id,
            "carrier_profile_ref_and_hash": dict(self.carrier_profile_ref_and_hash),
            "view_policy_ref_and_hash": dict(self.view_policy_ref_and_hash),
            "tool_policy_ref_and_hash": dict(self.tool_policy_ref_and_hash),
            "adapter_kind": self.adapter_kind,
            "vault_access_capability_ref_and_hash": dict(self.vault_access_capability_ref_and_hash),
            "output_schema_ref_and_hash": dict(self.output_schema_ref_and_hash),
            "budget_contract_ref_and_hash": dict(self.budget_contract_ref_and_hash),
            "prompt_release_ref_and_hash": dict(self.prompt_release_ref_and_hash),
            "idempotency_key": self.idempotency_key,
            "contract_hash_algorithm": self.contract_hash_algorithm,
            "contract_hash": self.contract_hash,
        }


def _check_hash(value: str, field_name: str) -> list[tuple[EC, str]]:
    if not isinstance(value, str) or not _HASH_RE.match(value):
        return [(EC.OBJECT_HASH_MISMATCH, f"{field_name} is not a valid sha256 hash: {value!r}")]
    return []


def _check_ref_hash(obj: dict[str, Any], field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"ref_id", "sha256"}:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly ref_id and sha256"))
        return errors
    if not isinstance(obj.get("ref_id", ""), str) or not _EXACT_ID_RE.match(obj.get("ref_id", "")):
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name}.ref_id is not valid"))
    errors.extend(_check_hash(obj.get("sha256", ""), f"{field_name}.sha256"))
    return errors


def build_role_execution_contract(
    *,
    role_job_id: str,
    epoch_id: str,
    role_type_registry_ref_and_hash: dict[str, str],
    role_type_id: str,
    carrier_profile_ref_and_hash: dict[str, str],
    view_policy_ref_and_hash: dict[str, str],
    tool_policy_ref_and_hash: dict[str, str],
    adapter_kind: str,
    vault_access_capability_ref_and_hash: dict[str, str],
    output_schema_ref_and_hash: dict[str, str],
    budget_contract_ref_and_hash: dict[str, str],
    prompt_release_ref_and_hash: dict[str, str],
    idempotency_key: str,
) -> RoleExecutionContract:
    """构建 RoleExecutionContract，自动计算 contract_hash。"""
    obj = {
        "role_job_id": role_job_id,
        "epoch_id": epoch_id,
        "role_type_registry_ref_and_hash": dict(role_type_registry_ref_and_hash),
        "role_type_id": role_type_id,
        "carrier_profile_ref_and_hash": dict(carrier_profile_ref_and_hash),
        "view_policy_ref_and_hash": dict(view_policy_ref_and_hash),
        "tool_policy_ref_and_hash": dict(tool_policy_ref_and_hash),
        "adapter_kind": adapter_kind,
        "vault_access_capability_ref_and_hash": dict(vault_access_capability_ref_and_hash),
        "output_schema_ref_and_hash": dict(output_schema_ref_and_hash),
        "budget_contract_ref_and_hash": dict(budget_contract_ref_and_hash),
        "prompt_release_ref_and_hash": dict(prompt_release_ref_and_hash),
        "idempotency_key": idempotency_key,
        "contract_hash_algorithm": _CONTRACT_HASH_ALGORITHM,
        "contract_hash": None,
    }
    contract_hash = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
    return RoleExecutionContract(
        role_job_id=role_job_id,
        epoch_id=epoch_id,
        role_type_registry_ref_and_hash=dict(role_type_registry_ref_and_hash),
        role_type_id=role_type_id,
        carrier_profile_ref_and_hash=dict(carrier_profile_ref_and_hash),
        view_policy_ref_and_hash=dict(view_policy_ref_and_hash),
        tool_policy_ref_and_hash=dict(tool_policy_ref_and_hash),
        adapter_kind=adapter_kind,
        vault_access_capability_ref_and_hash=dict(vault_access_capability_ref_and_hash),
        output_schema_ref_and_hash=dict(output_schema_ref_and_hash),
        budget_contract_ref_and_hash=dict(budget_contract_ref_and_hash),
        prompt_release_ref_and_hash=dict(prompt_release_ref_and_hash),
        idempotency_key=idempotency_key,
        contract_hash_algorithm=_CONTRACT_HASH_ALGORITHM,
        contract_hash=contract_hash,
    )


def verify_role_execution_contract(
    contract: dict[str, Any] | RoleExecutionContract,
    *,
    registry: RoleRegistry | None = None,
) -> VerificationResult:
    """验证 RoleExecutionContract 的 schema + semantic 合法性。

    检查：
    1. 所有 ref_and_hash 字段结构合法
    2. adapter_kind 在允许列表中
    3. contract_hash 正确
    4. 如果提供 registry：role_type_id 存在于 registry
    5. 如果提供 registry：registry hash 匹配
    6. 如果提供 registry：role 的 view_policy_kind / tool_policy_kind 与 contract 中的 policy refs 一致
    """
    if isinstance(contract, RoleExecutionContract):
        contract = contract.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. ref_and_hash 字段
    for field_name in (
        "role_type_registry_ref_and_hash",
        "carrier_profile_ref_and_hash",
        "view_policy_ref_and_hash",
        "tool_policy_ref_and_hash",
        "vault_access_capability_ref_and_hash",
        "output_schema_ref_and_hash",
        "budget_contract_ref_and_hash",
        "prompt_release_ref_and_hash",
    ):
        for code, detail in _check_ref_hash(contract.get(field_name, {}), field_name):
            _err(code, detail)

    # 2. adapter_kind
    adapter_kind = contract.get("adapter_kind", "")
    if adapter_kind not in MODEL_ROLE_ADAPTER_KINDS:
        _err(EC.CW0_CONTRACT_ADAPTER_MISMATCH, f"invalid adapter_kind: {adapter_kind}")

    # 3. role_type_id
    role_type_id = contract.get("role_type_id", "")
    if not isinstance(role_type_id, str) or not _EXACT_ID_RE.match(role_type_id):
        _err(EC.CW0_UNKNOWN_ROLE, f"invalid role_type_id: {role_type_id!r}")

    # 4. contract_hash_algorithm
    if contract.get("contract_hash_algorithm") != _CONTRACT_HASH_ALGORITHM:
        _err(EC.CW0_CONTRACT_HASH_MISMATCH,
             f"unexpected contract_hash_algorithm: {contract.get('contract_hash_algorithm')}")

    # 5. contract_hash
    obj_for_hash = dict(contract)
    obj_for_hash["contract_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if contract.get("contract_hash") != computed_hash:
        _err(EC.CW0_CONTRACT_HASH_MISMATCH,
             f"contract_hash mismatch: expected {computed_hash}, got {contract.get('contract_hash')}")

    # 6. registry 验证
    if registry is not None:
        # registry hash 匹配
        reg_ref = contract.get("role_type_registry_ref_and_hash", {})
        if reg_ref.get("sha256") != registry.content_hash:
            _err(EC.CW0_REGISTRY_HASH_MISMATCH,
                 f"registry hash mismatch: contract has {reg_ref.get('sha256')}, "
                 f"registry has {registry.content_hash}")

        # role_type_id 存在
        role_def = registry.get_role(role_type_id)
        if role_def is None:
            _err(EC.CW0_UNKNOWN_ROLE, f"role_type_id {role_type_id} not in registry")
        else:
            # view policy 一致性：contract 的 view_policy_ref_and_hash.sha256
            # 必须与 role_def.view_policy_kind 的 hash 一致
            # 这里检查 view_policy_ref_and_hash.sha256 是 role_def.view_policy_kind 的 hash
            expected_view_hash = hashlib.sha256(
                canonical_json_bytes({"view_policy_kind": role_def.view_policy_kind})
            ).hexdigest()
            actual_view_hash = contract.get("view_policy_ref_and_hash", {}).get("sha256", "")
            if actual_view_hash != expected_view_hash:
                _err(EC.CW0_CONTRACT_VIEW_POLICY_MISMATCH,
                     f"view_policy hash mismatch: role expects {role_def.view_policy_kind} "
                     f"(hash={expected_view_hash}), contract has {actual_view_hash}")

            # tool policy 一致性
            expected_tool_hash = hashlib.sha256(
                canonical_json_bytes({"tool_policy_kind": role_def.tool_policy_kind})
            ).hexdigest()
            actual_tool_hash = contract.get("tool_policy_ref_and_hash", {}).get("sha256", "")
            if actual_tool_hash != expected_tool_hash:
                _err(EC.CW0_CONTRACT_TOOL_POLICY_MISMATCH,
                     f"tool_policy hash mismatch: role expects {role_def.tool_policy_kind} "
                     f"(hash={expected_tool_hash}), contract has {actual_tool_hash}")

            # 认知角色默认 NO_TOOLS — 如果 tool_policy 允许工具则 BLOCK
            if role_def.tool_policy_kind != "NO_TOOLS":
                _err(EC.CW0_ROLE_TOOL_POLICY_ALLOWS_TOOLS,
                     f"role {role_type_id} tool_policy_kind must be NO_TOOLS, "
                     f"got {role_def.tool_policy_kind}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )
