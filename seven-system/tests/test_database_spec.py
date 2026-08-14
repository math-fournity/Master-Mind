from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.database.capability import (  # noqa: E402
    DATABASE_CAPABILITY_CHECK_IDS,
    DATABASE_SITE_CHECK_IDS,
    DATABASE_SITE_CAPABILITY_CHECK_IDS,
    STRICT_DATABASE_CONTRACT_CHECK_IDS,
    DatabaseSiteCapabilitySubject,
    StrictDatabaseContractSubject,
)
from seven_system.database.spec import (  # noqa: E402
    ALLOWED_COLLECTIONS,
    CANONICAL_MIGRATION_SPEC,
    CANONICAL_MIGRATION_SPEC_HASH,
)


class DatabaseSpecTests(unittest.TestCase):
    def test_collection_allowlist_is_exact_and_versioned(self) -> None:
        self.assertEqual(
            ALLOWED_COLLECTIONS,
            {
                "seven_records_v1",
                "seven_artifact_refs_v1",
                "seven_work_events_v1",
                "seven_work_items_v1",
                "seven_outbox_v1",
                "seven_alerts_v1",
                "seven_schema_migrations_v1",
            },
        )
        self.assertTrue(all(name.isascii() and name.startswith("seven_") for name in ALLOWED_COLLECTIONS))

    def test_index_semantics_are_explicit_unique_and_auditable(self) -> None:
        index_by_name = {
            index.name: index
            for collection in CANONICAL_MIGRATION_SPEC.collections
            for index in collection.indexes
        }
        self.assertEqual(
            set(index_by_name),
            {
                "ux_records_type_content_hash",
                "ux_records_type_logical_revision",
                "ux_artifact_refs_content_hash",
                "ux_artifact_refs_cas_uri",
                "ux_work_events_event_id",
                "ux_work_events_aggregate_sequence",
                "ux_work_items_stage_idempotency",
                "ux_work_items_execution_attempt",
                "ux_outbox_unique_key",
                "ux_outbox_aggregate_revision",
                "ux_alerts_dedupe_key",
                "ux_schema_migrations_migration_id",
                "ux_schema_migrations_plan_hash",
            },
        )
        self.assertEqual(
            {name: index.fields for name, index in index_by_name.items()},
            {
                "ux_records_type_content_hash": ("record_type", "content_hash"),
                "ux_records_type_logical_revision": (
                    "record_type",
                    "logical_id",
                    "revision",
                ),
                "ux_artifact_refs_content_hash": ("content_hash",),
                "ux_artifact_refs_cas_uri": ("cas_uri",),
                "ux_work_events_event_id": ("event_id",),
                "ux_work_events_aggregate_sequence": (
                    "aggregate_id",
                    "event_sequence",
                ),
                "ux_work_items_stage_idempotency": (
                    "stage",
                    "idempotency_key",
                ),
                "ux_work_items_execution_attempt": ("execution_attempt_id",),
                "ux_outbox_unique_key": ("outbox_unique_key",),
                "ux_outbox_aggregate_revision": (
                    "aggregate_id",
                    "aggregate_revision",
                    "event_type",
                ),
                "ux_alerts_dedupe_key": ("dedupe_key",),
                "ux_schema_migrations_migration_id": ("migration_id",),
                "ux_schema_migrations_plan_hash": ("plan_hash",),
            },
        )
        self.assertEqual(
            index_by_name["ux_work_events_aggregate_sequence"].fields,
            ("aggregate_id", "event_sequence"),
        )
        self.assertEqual(
            index_by_name["ux_records_type_logical_revision"].fields,
            ("record_type", "logical_id", "revision"),
        )
        self.assertEqual(
            index_by_name["ux_work_items_stage_idempotency"].fields,
            ("stage", "idempotency_key"),
        )
        self.assertEqual(
            index_by_name["ux_outbox_aggregate_revision"].fields,
            ("aggregate_id", "aggregate_revision", "event_type"),
        )
        self.assertTrue(all(index.index_type == "persistent" for index in index_by_name.values()))
        self.assertTrue(all(index.unique for index in index_by_name.values()))
        self.assertTrue(index_by_name["ux_work_items_execution_attempt"].sparse)
        self.assertTrue(index_by_name["ux_alerts_dedupe_key"].sparse)
        self.assertTrue(
            all(
                not index.sparse
                for name, index in index_by_name.items()
                if name
                not in {
                    "ux_work_items_execution_attempt",
                    "ux_alerts_dedupe_key",
                }
            )
        )

    def test_migration_spec_is_json_serializable_and_hash_stable(self) -> None:
        rendered = json.dumps(
            CANONICAL_MIGRATION_SPEC.as_dict(),
            ensure_ascii=False,
            sort_keys=True,
        )
        self.assertIn("seven_records_v1", rendered)
        self.assertEqual(
            CANONICAL_MIGRATION_SPEC_HASH,
            CANONICAL_MIGRATION_SPEC.spec_hash,
        )
        self.assertIsNotNone(re.fullmatch(r"[0-9a-f]{64}", CANONICAL_MIGRATION_SPEC_HASH))

    def test_offline_contract_and_site_capability_subjects_are_separate(self) -> None:
        self.assertIn(
            "database.site.physical_storage.binding_verified",
            DATABASE_SITE_CHECK_IDS,
        )
        self.assertEqual(DATABASE_SITE_CHECK_IDS, DATABASE_SITE_CAPABILITY_CHECK_IDS)
        self.assertTrue(
            set(DATABASE_SITE_CHECK_IDS).issubset(DATABASE_CAPABILITY_CHECK_IDS)
        )
        contract = StrictDatabaseContractSubject(
            implementation_sha256="1" * 64,
        )
        self.assertNotIn("physical_storage", json.dumps(contract.as_dict()))
        self.assertEqual(
            contract.as_dict()["required_check_ids"],
            list(STRICT_DATABASE_CONTRACT_CHECK_IDS),
        )
        with self.assertRaises(TypeError):
            DatabaseSiteCapabilitySubject(  # type: ignore[call-arg]
                strict_contract_subject_hash=contract.subject_hash,
                database_catalog_evidence_sha256="2" * 64,
            )
        site = DatabaseSiteCapabilitySubject(
            strict_contract_subject_hash=contract.subject_hash,
            database_catalog_evidence_sha256="2" * 64,
            physical_storage_evidence_sha256="3" * 64,
        )
        self.assertNotEqual(contract.subject_hash, site.subject_hash)

if __name__ == "__main__":
    unittest.main()
