from __future__ import annotations

import sys
import unittest
from dataclasses import replace
from pathlib import Path
from types import ModuleType


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.database.environment import EXPECTED_DATABASE  # noqa: E402
import seven_system.database as database_package  # noqa: E402
import seven_system.database.migration as migration_module  # noqa: E402
from seven_system.database.errors import (  # noqa: E402
    MigrationPlanMismatchError,
    SchemaConflictError,
)
from seven_system.database.migration import plan_migration  # noqa: E402
from seven_system.database.port import CollectionSnapshot, IndexSnapshot  # noqa: E402
from seven_system.database.spec import CANONICAL_MIGRATION_SPEC  # noqa: E402


class _MemoryPort:
    def __init__(self) -> None:
        self.database_name = EXPECTED_DATABASE
        self.collections: dict[str, CollectionSnapshot] = {}
        self.reads: list[str] = []

    def inspect_collection(self, name: str) -> CollectionSnapshot | None:
        self.reads.append(name)
        return self.collections.get(name)


class DatabaseMigrationTests(unittest.TestCase):
    def test_plan_is_deterministic_and_has_zero_write_side_effects(self) -> None:
        port = _MemoryPort()
        first = plan_migration(port)
        second = plan_migration(port)
        self.assertEqual(first.plan_hash, second.plan_hash)
        self.assertEqual(first.actions, second.actions)
        self.assertEqual(len(first.actions), 20)  # 7 collections + 13 indexes.
        self.assertEqual(
            [action.action for action in first.actions[:3]],
            ["CREATE_COLLECTION", "CREATE_INDEX", "CREATE_INDEX"],
        )

    def test_noncanonical_spec_is_rejected_before_read_or_write(self) -> None:
        port = _MemoryPort()
        modified = replace(
            CANONICAL_MIGRATION_SPEC,
            collections=CANONICAL_MIGRATION_SPEC.collections[:-1],
        )
        with self.assertRaises(MigrationPlanMismatchError):
            plan_migration(port, modified)
        self.assertEqual(port.reads, [])

    def test_no_runtime_apply_or_ddl_primitive_is_exposed(self) -> None:
        self.assertIsInstance(migration_module, ModuleType)
        forbidden = {
            "apply_migration",
            "_apply_migration_primitive",
            "MigrationAuthorization",
            "MigrationReceipt",
            "DatabaseMigrationPort",
        }
        self.assertTrue(all(not hasattr(migration_module, name) for name in forbidden))
        self.assertTrue(all(not hasattr(database_package, name) for name in forbidden))

    def test_conflicting_index_semantics_are_not_auto_repaired(self) -> None:
        port = _MemoryPort()
        port.collections["seven_records_v1"] = CollectionSnapshot(
            "seven_records_v1",
            "document",
            (
                IndexSnapshot(
                    "ux_records_type_content_hash",
                    ("record_type", "content_hash"),
                    "persistent",
                    False,
                    False,
                ),
            ),
        )
        with self.assertRaises(SchemaConflictError):
            plan_migration(port)

    def test_extra_persistent_index_is_schema_drift(self) -> None:
        port = _MemoryPort()
        port.collections["seven_alerts_v1"] = CollectionSnapshot(
            "seven_alerts_v1",
            "document",
            (
                IndexSnapshot(
                    "ux_alerts_dedupe_key",
                    ("dedupe_key",),
                    "persistent",
                    True,
                    True,
                ),
                IndexSnapshot(
                    "unexpected_persistent_index",
                    ("message",),
                    "persistent",
                    False,
                    False,
                ),
            ),
        )
        with self.assertRaises(SchemaConflictError) as raised:
            plan_migration(port)
        self.assertIn("outside the canonical spec", str(raised.exception))


if __name__ == "__main__":
    unittest.main()
