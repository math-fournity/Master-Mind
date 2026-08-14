"""WP-DB1I 版本化 Schema bootstrap migration plan。

与 ``migration.py`` 的只读 ``MigrationPlan`` 不同，本模块产生
**可被 fenced apply 协议消费的确定性 DDL action plan**：

- 输入：canonical ``MigrationSpec``（来自 ``spec.py``）+ site fingerprint hash
- 输出：``SchemaBootstrapPlan``——版本化、确定性、带 plan_hash
- 每个 DDL action 有稳定 ordinal、action_id 和语义 tuple
- plan_hash 覆盖 spec_hash、site fingerprint hash、全部 actions 的有序语义

本模块不执行任何 DDL、不连接数据库、不写 D 盘。
真实 apply 由 ``schema_bootstrap.py`` 的 fenced 协议在 permit/fence 守护下执行。

SIDE_EFFECT_FREE：纯计算，无 IO。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..contracts.errors import VerificationErrorCode as EC
from ..hashing import object_hash
from .environment import EXPECTED_DATABASE
from .spec import (
    CANONICAL_MIGRATION_SPEC,
    CANONICAL_MIGRATION_SPEC_HASH,
    CollectionSpec,
    IndexSpec,
    MigrationSpec,
)


SCHEMA_BOOTSTRAP_PLAN_SCHEMA_VERSION = "seven-schema-bootstrap-plan/v1"


@dataclass(frozen=True)
class DDLAction:
    """单个确定性 DDL action。

    每个 action 有：
    - ordinal：plan 内的稳定执行顺序（从 0 起）
    - action_id：确定性 ID（action_type:collection[:index_name]）
    - action_type：CREATE_COLLECTION / CREATE_INDEX
    - collection：目标集合名
    - index：CREATE_INDEX 时的索引规格（CREATE_COLLECTION 时为 None）
    """

    ordinal: int
    action_type: str
    collection: str
    index: IndexSpec | None = None

    @property
    def action_id(self) -> str:
        if self.index is not None:
            return f"{self.action_type}:{self.collection}:{self.index.name}"
        return f"{self.action_type}:{self.collection}"

    def semantic_tuple(self) -> tuple[object, ...]:
        if self.index is not None:
            return (
                self.ordinal,
                self.action_type,
                self.collection,
                self.index.name,
                self.index.index_type,
                self.index.fields,
                self.index.unique,
                self.index.sparse,
            )
        return (self.ordinal, self.action_type, self.collection)

    def as_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "ordinal": self.ordinal,
            "action_id": self.action_id,
            "action_type": self.action_type,
            "collection": self.collection,
        }
        if self.index is not None:
            result["index"] = self.index.as_dict()
        return result


@dataclass(frozen=True)
class SchemaBootstrapPlan:
    """版本化、确定性的 Schema bootstrap plan。

    绑定：
    - schema_version（本 plan 的版本）
    - expected_database
    - spec_hash（canonical MigrationSpec 的 hash）
    - site_fingerprint_hash（目标逻辑站点指纹）
    - actions：有序 DDL action tuple
    - plan_hash：覆盖以上全部的确定性 hash
    """

    schema_version: str
    expected_database: str
    spec_hash: str
    site_fingerprint_hash: str
    actions: tuple[DDLAction, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "expected_database": self.expected_database,
            "spec_hash": self.spec_hash,
            "site_fingerprint_hash": self.site_fingerprint_hash,
            "actions": [action.as_dict() for action in self.actions],
        }

    @property
    def plan_hash(self) -> str:
        """覆盖 schema_version + expected_database + spec_hash +
        site_fingerprint_hash + 全部 actions 有序语义的确定性 hash。"""

        return object_hash(
            "SchemaBootstrapPlan",
            self.schema_version,
            {
                "expected_database": self.expected_database,
                "spec_hash": self.spec_hash,
                "site_fingerprint_hash": self.site_fingerprint_hash,
                "actions": [list(action.semantic_tuple()) for action in self.actions],
            },
        )

    @property
    def action_count(self) -> int:
        return len(self.actions)

    def action_by_ordinal(self, ordinal: int) -> DDLAction | None:
        for action in self.actions:
            if action.ordinal == ordinal:
                return action
        return None


class SchemaBootstrapPlanError(ValueError):
    """plan 构造或验证不满足 WP-DB1I。"""


def build_bootstrap_plan_actions(
    spec: MigrationSpec = CANONICAL_MIGRATION_SPEC,
) -> tuple[DDLAction, ...]:
    """从 canonical spec 生成确定性、有序的 DDL action 序列。

    顺序规则（确定性）：
    - 按 spec.collections 的固定顺序遍历
    - 每个集合先 CREATE_COLLECTION，再按 spec 中的索引顺序 CREATE_INDEX
    - ordinal 从 0 起单调递增
    """

    if spec.spec_hash != CANONICAL_MIGRATION_SPEC_HASH:
        raise SchemaBootstrapPlanError(
            "only the canonical migration spec is permitted for bootstrap"
        )
    if spec.expected_database != EXPECTED_DATABASE:
        raise SchemaBootstrapPlanError(
            "spec expected_database does not match EXPECTED_DATABASE"
        )

    actions: list[DDLAction] = []
    ordinal = 0
    for collection in spec.collections:
        actions.append(
            DDLAction(
                ordinal=ordinal,
                action_type="CREATE_COLLECTION",
                collection=collection.name,
            )
        )
        ordinal += 1
        for index in collection.indexes:
            actions.append(
                DDLAction(
                    ordinal=ordinal,
                    action_type="CREATE_INDEX",
                    collection=collection.name,
                    index=index,
                )
            )
            ordinal += 1
    return tuple(actions)


def build_schema_bootstrap_plan(
    *,
    site_fingerprint_hash: str,
    spec: MigrationSpec = CANONICAL_MIGRATION_SPEC,
) -> SchemaBootstrapPlan:
    """构造版本化 Schema bootstrap plan。

    site_fingerprint_hash 必须来自 DB1L 的 SiteFingerprint.fingerprint_hash，
    确保 plan 绑定到精确的目标逻辑站点。
    """

    if not isinstance(site_fingerprint_hash, str) or len(site_fingerprint_hash) != 64:
        raise SchemaBootstrapPlanError(
            "site_fingerprint_hash must be a 64-char hex string"
        )
    if spec.spec_hash != CANONICAL_MIGRATION_SPEC_HASH:
        raise SchemaBootstrapPlanError(
            "only the canonical migration spec is permitted for bootstrap"
        )

    actions = build_bootstrap_plan_actions(spec)
    return SchemaBootstrapPlan(
        schema_version=SCHEMA_BOOTSTRAP_PLAN_SCHEMA_VERSION,
        expected_database=EXPECTED_DATABASE,
        spec_hash=spec.spec_hash,
        site_fingerprint_hash=site_fingerprint_hash,
        actions=actions,
    )


def verify_schema_bootstrap_plan(plan: object) -> tuple[tuple[EC, str], ...]:
    """语义验证 SchemaBootstrapPlan。

    返回空 tuple 表示 plan 通过验证。
    """

    errors: list[tuple[EC, str]] = []

    if not isinstance(plan, SchemaBootstrapPlan):
        return ((EC.REQUIRED_FIELD_MISSING, "plan must be a SchemaBootstrapPlan"),)

    if plan.schema_version != SCHEMA_BOOTSTRAP_PLAN_SCHEMA_VERSION:
        errors.append(
            (
                EC.REQUIRED_FIELD_MISSING,
                f"schema_version must be {SCHEMA_BOOTSTRAP_PLAN_SCHEMA_VERSION}",
            )
        )
    if plan.expected_database != EXPECTED_DATABASE:
        errors.append(
            (
                EC.DB1I_MIGRATION_SPEC_HASH_DRIFT,
                f"expected_database must be {EXPECTED_DATABASE}",
            )
        )
    if plan.spec_hash != CANONICAL_MIGRATION_SPEC_HASH:
        errors.append(
            (
                EC.DB1I_MIGRATION_SPEC_HASH_DRIFT,
                "spec_hash must match canonical migration spec hash",
            )
        )
    if not isinstance(plan.site_fingerprint_hash, str) or len(plan.site_fingerprint_hash) != 64:
        errors.append(
            (EC.DB1I_SITE_FINGERPRINT_MISMATCH, "site_fingerprint_hash must be 64-char hex")
        )

    # 验证 actions 有序、ordinal 连续、action_id 唯一
    seen_ordinals: set[int] = set()
    seen_action_ids: set[str] = set()
    for idx, action in enumerate(plan.actions):
        if not isinstance(action, DDLAction):
            errors.append((EC.REQUIRED_FIELD_MISSING, f"action {idx} is not a DDLAction"))
            continue
        if action.ordinal != idx:
            errors.append(
                (
                    EC.DB1I_PLAN_HASH_DRIFT,
                    f"action ordinal {action.ordinal} != position {idx}",
                )
            )
        if action.ordinal in seen_ordinals:
            errors.append(
                (EC.DB1I_DUPLICATE_APPLY, f"duplicate ordinal {action.ordinal}")
            )
        seen_ordinals.add(action.ordinal)
        if action.action_id in seen_action_ids:
            errors.append(
                (EC.DB1I_DUPLICATE_APPLY, f"duplicate action_id {action.action_id}")
            )
        seen_action_ids.add(action.action_id)
        if action.action_type not in ("CREATE_COLLECTION", "CREATE_INDEX"):
            errors.append(
                (EC.REQUIRED_FIELD_MISSING, f"unknown action_type {action.action_type}")
            )
        if action.action_type == "CREATE_INDEX" and action.index is None:
            errors.append(
                (EC.REQUIRED_FIELD_MISSING, f"CREATE_INDEX action {action.ordinal} missing index")
            )

    # 验证 plan_hash 确定性（重算）
    recomputed = SchemaBootstrapPlan(
        schema_version=plan.schema_version,
        expected_database=plan.expected_database,
        spec_hash=plan.spec_hash,
        site_fingerprint_hash=plan.site_fingerprint_hash,
        actions=plan.actions,
    ).plan_hash
    if recomputed != plan.plan_hash:
        errors.append(
            (EC.DB1I_PLAN_HASH_DRIFT, "plan_hash is not deterministic")
        )

    return tuple(dict.fromkeys(errors))
