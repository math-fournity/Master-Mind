"""确定性、只读的 migration planning。

当前生产包故意不含任何 apply/DDL primitive。物理站点 Gate、durable migration
ledger、fence、失败恢复和人工授权尚未实现，因此 canonical plan 只能被读取和审计。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..hashing import object_hash
from .environment import EXPECTED_DATABASE
from .errors import (
    DatabaseIdentityError,
    MigrationPlanMismatchError,
    SchemaConflictError,
)
from .port import DatabaseCatalogPort, IndexSnapshot
from .spec import (
    CANONICAL_MIGRATION_SPEC,
    CANONICAL_MIGRATION_SPEC_HASH,
    CollectionSpec,
    IndexSpec,
    MigrationSpec,
    validate_collection_name,
)


MIGRATION_PLAN_SCHEMA_VERSION = "seven-database-migration-plan/v1"


@dataclass(frozen=True)
class MigrationAction:
    action: str
    collection: str
    index: IndexSpec | None = None
    collection_type: str | None = None

    def as_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "action": self.action,
            "collection": self.collection,
        }
        if self.collection_type is not None:
            result["collection_type"] = self.collection_type
        if self.index is not None:
            result["index"] = self.index.as_dict()
        return result


@dataclass(frozen=True)
class MigrationPlan:
    schema_version: str
    expected_database: str
    spec_hash: str
    catalog_hash: str
    actions: tuple[MigrationAction, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "expected_database": self.expected_database,
            "spec_hash": self.spec_hash,
            "catalog_hash": self.catalog_hash,
            "actions": [action.as_dict() for action in self.actions],
        }

    @property
    def plan_hash(self) -> str:
        return object_hash("SevenDatabaseMigrationPlan", self.schema_version, self.as_dict())


def _index_snapshot_dict(index: IndexSnapshot) -> dict[str, Any]:
    return {
        "name": index.name,
        "type": index.index_type,
        "fields": list(index.fields),
        "unique": index.unique,
        "sparse": index.sparse,
    }


def _required_index_tuple(index: IndexSpec) -> tuple[object, ...]:
    return (index.name, index.index_type, index.fields, index.unique, index.sparse)


def _inspect_collection(
    port: DatabaseCatalogPort, collection: CollectionSpec
) -> tuple[dict[str, Any], tuple[MigrationAction, ...]]:
    name = validate_collection_name(collection.name)
    snapshot = port.inspect_collection(name)
    if snapshot is None:
        actions = [
            MigrationAction(
                "CREATE_COLLECTION",
                name,
                collection_type=collection.collection_type,
            )
        ]
        actions.extend(
            MigrationAction("CREATE_INDEX", name, index=index)
            for index in collection.indexes
        )
        return {"name": name, "state": "ABSENT"}, tuple(actions)

    if snapshot.name != name or snapshot.collection_type != collection.collection_type:
        raise SchemaConflictError(
            f"collection {name} exists with non-canonical identity/type"
        )

    by_name = {index.name: index for index in snapshot.indexes}
    if len(by_name) != len(snapshot.indexes):
        raise SchemaConflictError(f"collection {name} returned duplicate index names")

    actions: list[MigrationAction] = []
    for required in collection.indexes:
        present = by_name.get(required.name)
        if present is None:
            # 相同 fields 却不同语义/名字时，不静默叠加第二个唯一索引。
            field_collisions = [
                existing
                for existing in snapshot.indexes
                if existing.index_type == required.index_type
                and existing.fields == required.fields
            ]
            if field_collisions:
                raise SchemaConflictError(
                    f"collection {name} has a non-canonical index on required fields"
                )
            actions.append(MigrationAction("CREATE_INDEX", name, index=required))
        elif present.semantic_tuple() != _required_index_tuple(required):
            raise SchemaConflictError(
                f"collection {name} index {required.name} conflicts with canonical spec"
            )

    required_names = {index.name for index in collection.indexes}
    unexpected = sorted(set(by_name) - required_names)
    if unexpected:
        raise SchemaConflictError(
            f"collection {name} has persistent indexes outside the canonical spec"
        )

    catalog = {
        "name": name,
        "state": "PRESENT",
        "collection_type": snapshot.collection_type,
        "indexes": [
            _index_snapshot_dict(index)
            for index in sorted(snapshot.indexes, key=lambda item: item.name)
        ],
    }
    return catalog, tuple(actions)


def plan_migration(
    port: DatabaseCatalogPort,
    spec: MigrationSpec = CANONICAL_MIGRATION_SPEC,
) -> MigrationPlan:
    """只读取得快照并生成 plan；绝不调用 migration primitive。"""

    if spec.spec_hash != CANONICAL_MIGRATION_SPEC_HASH:
        raise MigrationPlanMismatchError("only the canonical migration spec is permitted")
    if port.database_name != EXPECTED_DATABASE or spec.expected_database != EXPECTED_DATABASE:
        raise DatabaseIdentityError(EXPECTED_DATABASE)

    catalogs: list[dict[str, Any]] = []
    actions: list[MigrationAction] = []
    for collection in spec.collections:
        catalog, collection_actions = _inspect_collection(port, collection)
        catalogs.append(catalog)
        actions.extend(collection_actions)

    catalog_hash = object_hash(
        "SevenDatabaseCatalogSnapshot", "seven-database-catalog/v1", catalogs
    )
    return MigrationPlan(
        schema_version=MIGRATION_PLAN_SCHEMA_VERSION,
        expected_database=EXPECTED_DATABASE,
        spec_hash=spec.spec_hash,
        catalog_hash=catalog_hash,
        actions=tuple(actions),
    )
