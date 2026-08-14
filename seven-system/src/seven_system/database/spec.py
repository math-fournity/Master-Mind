"""Seven v1 的 canonical collection/index/migration spec。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..hashing import object_hash
from .environment import EXPECTED_DATABASE
from .errors import CollectionNotAllowedError


MIGRATION_SPEC_SCHEMA_VERSION = "seven-database-migration-spec/v1"


@dataclass(frozen=True)
class IndexSpec:
    name: str
    fields: tuple[str, ...]
    index_type: str = "persistent"
    unique: bool = True
    sparse: bool = False

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "type": self.index_type,
            "fields": list(self.fields),
            "unique": self.unique,
            "sparse": self.sparse,
        }


@dataclass(frozen=True)
class CollectionSpec:
    name: str
    collection_type: str
    indexes: tuple[IndexSpec, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "collection_type": self.collection_type,
            "indexes": [index.as_dict() for index in self.indexes],
        }


@dataclass(frozen=True)
class MigrationSpec:
    schema_version: str
    expected_database: str
    collections: tuple[CollectionSpec, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "expected_database": self.expected_database,
            "collections": [collection.as_dict() for collection in self.collections],
        }

    @property
    def spec_hash(self) -> str:
        return object_hash(
            "SevenDatabaseMigrationSpec", self.schema_version, self.as_dict()
        )


# 顺序是 migration 的稳定执行顺序，也是 hash 的一部分。
CANONICAL_MIGRATION_SPEC = MigrationSpec(
    schema_version=MIGRATION_SPEC_SCHEMA_VERSION,
    expected_database=EXPECTED_DATABASE,
    collections=(
        CollectionSpec(
            "seven_records_v1",
            "document",
            (
                IndexSpec(
                    "ux_records_type_content_hash",
                    ("record_type", "content_hash"),
                ),
                IndexSpec(
                    "ux_records_type_logical_revision",
                    ("record_type", "logical_id", "revision"),
                ),
            ),
        ),
        CollectionSpec(
            "seven_artifact_refs_v1",
            "document",
            (
                IndexSpec("ux_artifact_refs_content_hash", ("content_hash",)),
                IndexSpec("ux_artifact_refs_cas_uri", ("cas_uri",)),
            ),
        ),
        CollectionSpec(
            "seven_work_events_v1",
            "document",
            (
                IndexSpec("ux_work_events_event_id", ("event_id",)),
                IndexSpec(
                    "ux_work_events_aggregate_sequence",
                    ("aggregate_id", "event_sequence"),
                ),
            ),
        ),
        CollectionSpec(
            "seven_work_items_v1",
            "document",
            (
                IndexSpec(
                    "ux_work_items_stage_idempotency",
                    ("stage", "idempotency_key"),
                ),
                IndexSpec(
                    "ux_work_items_execution_attempt",
                    ("execution_attempt_id",),
                    sparse=True,
                ),
            ),
        ),
        CollectionSpec(
            "seven_outbox_v1",
            "document",
            (
                IndexSpec("ux_outbox_unique_key", ("outbox_unique_key",)),
                IndexSpec(
                    "ux_outbox_aggregate_revision",
                    ("aggregate_id", "aggregate_revision", "event_type"),
                ),
            ),
        ),
        CollectionSpec(
            "seven_alerts_v1",
            "document",
            (IndexSpec("ux_alerts_dedupe_key", ("dedupe_key",), sparse=True),),
        ),
        CollectionSpec(
            "seven_schema_migrations_v1",
            "document",
            (
                IndexSpec("ux_schema_migrations_migration_id", ("migration_id",)),
                IndexSpec("ux_schema_migrations_plan_hash", ("plan_hash",)),
            ),
        ),
    ),
)

ALLOWED_COLLECTIONS = frozenset(
    collection.name for collection in CANONICAL_MIGRATION_SPEC.collections
)
CANONICAL_MIGRATION_SPEC_HASH = CANONICAL_MIGRATION_SPEC.spec_hash


def validate_collection_name(name: object) -> str:
    """拒绝 Unicode confusable、控制字符及任何非固定 v1 名称。"""

    if (
        not isinstance(name, str)
        or not name.isascii()
        or name not in ALLOWED_COLLECTIONS
    ):
        raise CollectionNotAllowedError()
    return name
