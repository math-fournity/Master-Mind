"""RoleRegistry — 冻结的机器认知角色注册表。

来自 docs/implementation/05-execution-ports-and-carriers.md 的 RoleTypeRegistry。
注册表是 append-only、带 hash 的冻结对象；新增/删除/重命名角色必须生成新版本。

每个 RoleDefinition 绑定：
- role_type_id：精确角色标识
- required_profile_fields：该角色必须冻结的 carrier profile 字段
- view_policy_kind：该角色允许的 view policy（PUBLIC_ONLY / RESTRICTED_DERIVED / SOLUTION_BEARING_DERIVED）
- tool_policy_kind：该角色的 tool policy（认知角色默认 NO_TOOLS）
- description：角色职责描述

硬约束：
- 未知 role_type_id 在 prepare 前 BLOCK
- 已退役 role 不接受
- hash 不一致 BLOCK
- 不接受 ... / 自定义字符串 / ANY/ALL/DEFAULT 哨兵
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ROLE_TYPE_REGISTRY_ID,
    ROLE_TYPE_REGISTRY_SCHEMA_VERSION,
    TOOL_POLICY_KINDS,
    VIEW_POLICY_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


@dataclass(frozen=True)
class RoleDefinition:
    """单个机器认知角色定义。不可变。"""

    role_type_id: str
    required_profile_fields: tuple[str, ...]
    view_policy_kind: str
    tool_policy_kind: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "role_type_id": self.role_type_id,
            "required_profile_fields": list(self.required_profile_fields),
            "view_policy_kind": self.view_policy_kind,
            "tool_policy_kind": self.tool_policy_kind,
            "description": self.description,
        }


@dataclass
class RoleRegistry:
    """冻结的机器认知角色注册表。

    append-only：一旦冻结，不可修改。新版本必须创建新实例。
    """

    registry_id: str
    registry_version: str
    schema_version: str
    status: str  # "FROZEN"
    role_definitions: tuple[RoleDefinition, ...]
    content_hash: str = ""

    def __post_init__(self) -> None:
        if self.content_hash == "":
            self.content_hash = self._compute_hash()

    def _compute_hash(self) -> str:
        """计算注册表内容的 canonical hash。"""
        payload = {
            "registry_id": self.registry_id,
            "registry_version": self.registry_version,
            "schema_version": self.schema_version,
            "status": self.status,
            "role_types": [rd.to_dict() for rd in self.role_definitions],
        }
        return hashlib.sha256(canonical_json_bytes(payload)).hexdigest()

    @property
    def ref_and_hash(self) -> dict[str, str]:
        """返回 registry 的 ref + hash 引用。"""
        return {
            "ref_id": f"{self.registry_id}@{self.registry_version}",
            "sha256": self.content_hash,
        }

    def get_role(self, role_type_id: str) -> RoleDefinition | None:
        """查找角色定义。"""
        for rd in self.role_definitions:
            if rd.role_type_id == role_type_id:
                return rd
        return None

    def has_role(self, role_type_id: str) -> bool:
        return self.get_role(role_type_id) is not None

    def all_role_type_ids(self) -> tuple[str, ...]:
        return tuple(rd.role_type_id for rd in self.role_definitions)

    def to_dict(self) -> dict[str, Any]:
        return {
            "registry_id": self.registry_id,
            "registry_version": self.registry_version,
            "schema_version": self.schema_version,
            "status": self.status,
            "role_types": [rd.to_dict() for rd in self.role_definitions],
            "content_hash": self.content_hash,
        }


def verify_role_registry(registry: RoleRegistry) -> VerificationResult:
    """验证 RoleRegistry 的结构合法性。

    检查：
    1. registry_id / schema_version 常量
    2. status == FROZEN
    3. 每个角色定义的 view_policy_kind / tool_policy_kind 合法
    4. content_hash 正确
    5. 无重复 role_type_id
    6. role_type_id 不含 ANY/ALL/DEFAULT 哨兵
    """
    errors: list[EC] = []
    details: list[str] = []

    # 1. 常量
    if registry.registry_id != ROLE_TYPE_REGISTRY_ID:
        errors.append(EC.CW0_REGISTRY_HASH_MISMATCH)
        details.append(f"registry_id must be {ROLE_TYPE_REGISTRY_ID}")
    if registry.schema_version != ROLE_TYPE_REGISTRY_SCHEMA_VERSION:
        errors.append(EC.CW0_REGISTRY_HASH_MISMATCH)
        details.append(f"schema_version must be {ROLE_TYPE_REGISTRY_SCHEMA_VERSION}")

    # 2. status
    if registry.status != "FROZEN":
        errors.append(EC.CW0_ROLE_NOT_FROZEN)
        details.append(f"status must be FROZEN, got {registry.status}")

    # 3. 角色定义
    seen_ids: set[str] = set()
    forbidden = {"ANY", "ALL", "DEFAULT", "any", "all", "default"}
    for rd in registry.role_definitions:
        if rd.role_type_id in forbidden:
            errors.append(EC.CW0_UNKNOWN_ROLE)
            details.append(f"role_type_id is a reserved word: {rd.role_type_id}")
        if rd.role_type_id in seen_ids:
            errors.append(EC.CW0_UNKNOWN_ROLE)
            details.append(f"duplicate role_type_id: {rd.role_type_id}")
        seen_ids.add(rd.role_type_id)

        if rd.view_policy_kind not in VIEW_POLICY_KINDS:
            errors.append(EC.CW0_ROLE_MISSING_VIEW_POLICY)
            details.append(f"invalid view_policy_kind: {rd.view_policy_kind}")
        if rd.tool_policy_kind not in TOOL_POLICY_KINDS:
            errors.append(EC.CW0_ROLE_TOOL_POLICY_ALLOWS_TOOLS)
            details.append(f"invalid tool_policy_kind: {rd.tool_policy_kind}")

    # 4. content_hash
    computed = registry._compute_hash()
    if registry.content_hash != computed:
        errors.append(EC.CW0_REGISTRY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {registry.content_hash}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )


# ─── 冻结的 v1 注册表 ───────────────────────────────────────────────────
# 来自 docs/implementation/05-execution-ports-and-carriers.md

_FROZEN_ROLES_V1: tuple[RoleDefinition, ...] = (
    RoleDefinition(
        role_type_id="question_architect",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="PUBLIC_ONLY",
        tool_policy_kind="NO_TOOLS",
        description="P3A 出题链：构造数学问题草案",
    ),
    RoleDefinition(
        role_type_id="adversarial_editor",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="PUBLIC_ONLY",
        tool_policy_kind="NO_TOOLS",
        description="P3A 出题链：对抗性编辑/审稿",
    ),
    RoleDefinition(
        role_type_id="math_verifier",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="RESTRICTED_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="P3A 出题链：数学验证",
    ),
    RoleDefinition(
        role_type_id="trace_analyst",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="RESTRICTED_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="P3N：解题轨迹分析",
    ),
    RoleDefinition(
        role_type_id="solution_analyst",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="SOLUTION_BEARING_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="P3N：解答分析",
    ),
    RoleDefinition(
        role_type_id="adjudicator",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="RESTRICTED_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="P3N：裁决",
    ),
    RoleDefinition(
        role_type_id="process_auditor",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="RESTRICTED_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="P6：过程审计",
    ),
    RoleDefinition(
        role_type_id="proof_judge",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="RESTRICTED_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="P6：证明判定",
    ),
    RoleDefinition(
        role_type_id="leakage_auditor",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="RESTRICTED_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="P6：泄漏审计",
    ),
    RoleDefinition(
        role_type_id="selector",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="RESTRICTED_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="策略选择器（仅模型实现时产生 ModelRole job）",
    ),
    RoleDefinition(
        role_type_id="hint_renderer",
        required_profile_fields=(
            "carrier",
            "model_uid",
            "normalized_effort",
            "reasoning_mode",
            "orchestration_mode",
        ),
        view_policy_kind="RESTRICTED_DERIVED",
        tool_policy_kind="NO_TOOLS",
        description="提示渲染器（仅模型实现时产生 ModelRole job）",
    ),
)

ROLE_REGISTRY_FROZEN_V1: RoleRegistry = RoleRegistry(
    registry_id=ROLE_TYPE_REGISTRY_ID,
    registry_version="1.0.0",
    schema_version=ROLE_TYPE_REGISTRY_SCHEMA_VERSION,
    status="FROZEN",
    role_definitions=_FROZEN_ROLES_V1,
)
