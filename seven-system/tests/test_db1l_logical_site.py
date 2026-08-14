"""WP-DB1L 逻辑站点只读能力报告的 golden / negative / fault injection 测试。

所有测试使用 FakeLogicalSiteAdapter——零真实数据库连接、零写入。
"""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC  # noqa: E402
from seven_system.database.environment import EXPECTED_DATABASE  # noqa: E402
from seven_system.database.errors import DatabaseConnectionError  # noqa: E402
from seven_system.database.logical_site_report import (  # noqa: E402
    DB1L_CHECK_IDS,
    DB1L_CLAIMS,
    DB1L_NONCLAIMS,
    DB1L_SIDE_EFFECT_KEYS,
    LogicalSiteReportError,
    REPORT_SCHEMA_VERSION,
    build_logical_site_report,
    verify_logical_site_report,
)
from seven_system.database.port import CollectionSnapshot, IndexSnapshot  # noqa: E402
from seven_system.database.site_adapter import (  # noqa: E402
    CatalogSnapshot,
    FakeLogicalSiteAdapter,
    SiteFingerprint,
    classify_collection,
    enumerate_collections_from_catalog,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _golden_fingerprint() -> SiteFingerprint:
    return SiteFingerprint(
        endpoint="http://localhost:8529",
        server_version="arangodb-3.12.1",
        driver_name="python-arango",
        driver_version="8.1.0",
        principal="seven-readonly-user",
    )


def _seven_v1_collections() -> tuple[CollectionSnapshot, ...]:
    """Return the canonical seven_*_v1 collection snapshots (empty indexes for simplicity)."""
    names = (
        "seven_records_v1",
        "seven_artifact_refs_v1",
        "seven_work_events_v1",
        "seven_work_items_v1",
        "seven_outbox_v1",
        "seven_alerts_v1",
        "seven_schema_migrations_v1",
    )
    return tuple(
        CollectionSnapshot(name=name, collection_type="document", indexes=())
        for name in names
    )


def _golden_catalog() -> CatalogSnapshot:
    return CatalogSnapshot(collections=_seven_v1_collections())


def _golden_adapter() -> FakeLogicalSiteAdapter:
    return FakeLogicalSiteAdapter(
        database_name_value=EXPECTED_DATABASE,
        current_database_value=EXPECTED_DATABASE,
        fingerprint=_golden_fingerprint(),
        catalog=_golden_catalog(),
        write_count_value=0,
        connect_should_fail=False,
    )


def _build_golden_report() -> dict:
    adapter = _golden_adapter()
    return build_logical_site_report(adapter)


# ---------------------------------------------------------------------------
# Golden tests
# ---------------------------------------------------------------------------

class GoldenLogicalSiteReportTests(unittest.TestCase):
    def test_golden_report_builds_and_verifies_pass(self) -> None:
        report = _build_golden_report()
        errors = verify_logical_site_report(report)
        self.assertEqual(errors, ())
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["scope"], "READONLY_LOGICAL_SITE_V2")
        self.assertEqual(report["schema_version"], REPORT_SCHEMA_VERSION)
        self.assertEqual(report["expected_database"], EXPECTED_DATABASE)
        self.assertEqual(report["database_name"], EXPECTED_DATABASE)
        self.assertEqual(report["current_database"], EXPECTED_DATABASE)
        self.assertEqual(report["write_count"], 0)
        self.assertEqual(report["blockers"], [])

    def test_golden_report_has_all_check_ids_in_canonical_order(self) -> None:
        report = _build_golden_report()
        check_ids = [c["check_id"] for c in report["checks"]]
        self.assertEqual(check_ids, list(DB1L_CHECK_IDS))
        for check in report["checks"]:
            self.assertEqual(check["verdict"], "PASS")

    def test_golden_report_claims_match_exactly(self) -> None:
        report = _build_golden_report()
        self.assertEqual(set(report["claims"]), set(DB1L_CLAIMS))
        for claim in DB1L_CLAIMS:
            self.assertIs(report["claims"][claim], True)

    def test_golden_report_nonclaims_match_exactly(self) -> None:
        report = _build_golden_report()
        self.assertEqual(set(report["explicit_nonclaims"]), set(DB1L_NONCLAIMS))

    def test_golden_report_side_effects_all_zero(self) -> None:
        report = _build_golden_report()
        self.assertEqual(set(report["side_effects"]), set(DB1L_SIDE_EFFECT_KEYS))
        for key in DB1L_SIDE_EFFECT_KEYS:
            self.assertEqual(report["side_effects"][key], 0)

    def test_golden_report_enumerates_seven_v1_collections(self) -> None:
        report = _build_golden_report()
        enum = report["seven_collection_enumeration"]
        versioned = sorted(enum["versioned_collections"])
        expected = sorted(c.name for c in _seven_v1_collections())
        self.assertEqual(versioned, expected)
        self.assertEqual(enum["unversioned_seven_collections"], [])
        self.assertEqual(enum["forbidden_collections"], [])
        self.assertEqual(enum["conflicts"], [])
        self.assertFalse(report["conflict_check"]["has_conflicts"])

    def test_golden_report_has_valid_hashes(self) -> None:
        report = _build_golden_report()
        import re
        sha256_re = re.compile(r"^[0-9a-f]{64}$")
        for key in ("database_identity_hash", "site_fingerprint_hash", "catalog_hash", "zero_write_receipt"):
            self.assertIsNotNone(
                sha256_re.match(report[key]),
                f"{key} is not a valid sha256 hex: {report[key]}",
            )

    def test_golden_report_site_fingerprint_fields_present(self) -> None:
        report = _build_golden_report()
        fp = report["site_fingerprint"]
        for key in ("endpoint", "server_version", "driver_name", "driver_version", "principal"):
            self.assertIsInstance(fp[key], str)
            self.assertTrue(fp[key])

    def test_golden_report_does_not_contain_seven_v2_collections(self) -> None:
        """DB1L golden uses v1 collections; v2 is for live state, not bootstrap."""
        report = _build_golden_report()
        for name in report["seven_collection_enumeration"]["versioned_collections"]:
            self.assertIn("_v1", name)
            self.assertNotIn("_v2", name)

    def test_golden_report_catalog_has_all_collections(self) -> None:
        report = _build_golden_report()
        catalog_names = sorted(c["name"] for c in report["catalog_snapshot"]["collections"])
        expected = sorted(c.name for c in _seven_v1_collections())
        self.assertEqual(catalog_names, expected)


# ---------------------------------------------------------------------------
# Negative tests — database identity
# ---------------------------------------------------------------------------

class NegativeDatabaseIdentityTests(unittest.TestCase):
    def test_wrong_database_name_fails_verification(self) -> None:
        report = _build_golden_report()
        report["database_name"] = "wrong-database"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.SITE_DATABASE_NAME_MISMATCH, codes)

    def test_wrong_expected_database_fails_verification(self) -> None:
        report = _build_golden_report()
        report["expected_database"] = "some-other-db"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.SITE_DATABASE_NAME_MISMATCH, codes)

    def test_current_database_mismatch_fails_verification(self) -> None:
        report = _build_golden_report()
        report["current_database"] = "not-the-expected-db"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.SITE_CURRENT_DATABASE_MISMATCH, codes)

    def test_default_database_rejected(self) -> None:
        for default_name in ("_system", "", "default"):
            with self.subTest(default_name=default_name):
                report = _build_golden_report()
                report["current_database"] = default_name
                errors = verify_logical_site_report(report)
                codes = {e[0] for e in errors}
                self.assertIn(EC.SITE_DEFAULT_DATABASE_REJECTED, codes)

    def test_builder_rejects_wrong_database_name(self) -> None:
        adapter = _golden_adapter()
        adapter.database_name_value = "wrong-database"
        with self.assertRaises(LogicalSiteReportError):
            build_logical_site_report(adapter)

    def test_builder_rejects_wrong_current_database(self) -> None:
        adapter = _golden_adapter()
        adapter.current_database_value = "_system"
        with self.assertRaises(LogicalSiteReportError):
            build_logical_site_report(adapter)


# ---------------------------------------------------------------------------
# Negative tests — collection conflicts
# ---------------------------------------------------------------------------

class NegativeCollectionConflictTests(unittest.TestCase):
    def test_math_collection_reuse_detected(self) -> None:
        cols = _seven_v1_collections()
        bad_col = CollectionSnapshot(name="math_problems", collection_type="document", indexes=())
        catalog = CatalogSnapshot(collections=cols + (bad_col,))
        adapter = _golden_adapter()
        adapter.catalog = catalog
        with self.assertRaises(LogicalSiteReportError) as raised:
            build_logical_site_report(adapter)
        self.assertIn("CATALOG_MATH_SYSTEM_COLLECTION_REUSE", str(raised.exception))

    def test_system_collection_reuse_detected(self) -> None:
        cols = _seven_v1_collections()
        bad_col = CollectionSnapshot(name="system_users", collection_type="document", indexes=())
        catalog = CatalogSnapshot(collections=cols + (bad_col,))
        adapter = _golden_adapter()
        adapter.catalog = catalog
        with self.assertRaises(LogicalSiteReportError) as raised:
            build_logical_site_report(adapter)
        self.assertIn("CATALOG_MATH_SYSTEM_COLLECTION_REUSE", str(raised.exception))

    def test_unversioned_seven_collection_detected(self) -> None:
        cols = _seven_v1_collections()
        bad_col = CollectionSnapshot(name="seven_records", collection_type="document", indexes=())
        catalog = CatalogSnapshot(collections=cols + (bad_col,))
        adapter = _golden_adapter()
        adapter.catalog = catalog
        with self.assertRaises(LogicalSiteReportError) as raised:
            build_logical_site_report(adapter)
        self.assertIn("CATALOG_COLLECTION_NOT_VERSIONED", str(raised.exception))

    def test_verifier_detects_math_collection_in_catalog(self) -> None:
        report = _build_golden_report()
        report["catalog_snapshot"]["collections"].append({
            "name": "math_questions",
            "collection_type": "document",
            "indexes": [],
        })
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.CATALOG_MATH_SYSTEM_COLLECTION_REUSE, codes)

    def test_verifier_detects_unversioned_seven_collection(self) -> None:
        report = _build_golden_report()
        report["catalog_snapshot"]["collections"].append({
            "name": "seven_data",
            "collection_type": "document",
            "indexes": [],
        })
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.CATALOG_COLLECTION_NOT_VERSIONED, codes)

    def test_verifier_detects_extra_non_seven_collection_in_seven_namespace(self) -> None:
        """A collection that starts with seven_ but is not versioned is a conflict."""
        report = _build_golden_report()
        report["catalog_snapshot"]["collections"].append({
            "name": "seven_custom",
            "collection_type": "document",
            "indexes": [],
        })
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.CATALOG_COLLECTION_NOT_VERSIONED, codes)


# ---------------------------------------------------------------------------
# Negative tests — write detection
# ---------------------------------------------------------------------------

class NegativeWriteDetectionTests(unittest.TestCase):
    def test_write_count_positive_fails_verification(self) -> None:
        report = _build_golden_report()
        report["write_count"] = 1
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.DB1L_WRITE_DETECTED, codes)

    def test_write_count_positive_in_side_effects_fails(self) -> None:
        report = _build_golden_report()
        report["side_effects"]["database_writes"] = 1
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.DB1L_WRITE_DETECTED, codes)

    def test_builder_rejects_adapter_with_writes(self) -> None:
        adapter = _golden_adapter()
        adapter.write_count_value = 1
        with self.assertRaises(LogicalSiteReportError) as raised:
            build_logical_site_report(adapter)
        self.assertIn("DB1L_WRITE_DETECTED", str(raised.exception))

    def test_missing_zero_write_receipt_fails(self) -> None:
        report = _build_golden_report()
        report["zero_write_receipt"] = "not-a-hash"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.DB1L_ZERO_WRITE_EVIDENCE_MISSING, codes)


# ---------------------------------------------------------------------------
# Negative tests — missing fields / catalog
# ---------------------------------------------------------------------------

class NegativeMissingFieldTests(unittest.TestCase):
    def test_missing_catalog_fails(self) -> None:
        report = _build_golden_report()
        report["catalog_snapshot"] = None
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.CATALOG_MISSING, codes)

    def test_missing_catalog_hash_fails(self) -> None:
        report = _build_golden_report()
        report["catalog_hash"] = ""
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.CATALOG_MISSING, codes)

    def test_missing_enumeration_fails(self) -> None:
        report = _build_golden_report()
        report["seven_collection_enumeration"] = None
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_missing_site_fingerprint_fails(self) -> None:
        report = _build_golden_report()
        report["site_fingerprint"] = None
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.SITE_FINGERPRINT_MISMATCH, codes)

    def test_empty_fingerprint_field_fails(self) -> None:
        report = _build_golden_report()
        report["site_fingerprint"]["endpoint"] = ""
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.SITE_FINGERPRINT_MISMATCH, codes)

    def test_wrong_schema_version_fails(self) -> None:
        report = _build_golden_report()
        report["schema_version"] = "wrong-version"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_wrong_verdict_fails(self) -> None:
        report = _build_golden_report()
        report["verdict"] = "FAIL"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_non_empty_blockers_fails(self) -> None:
        report = _build_golden_report()
        report["blockers"] = ["something"]
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_wrong_claims_set_fails(self) -> None:
        report = _build_golden_report()
        report["claims"]["extra_claim"] = True
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_claim_value_not_true_fails(self) -> None:
        report = _build_golden_report()
        first_claim = DB1L_CLAIMS[0]
        report["claims"][first_claim] = False
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_wrong_nonclaims_fails(self) -> None:
        report = _build_golden_report()
        report["explicit_nonclaims"] = ["wrong"]
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_check_ids_out_of_order_fails(self) -> None:
        report = _build_golden_report()
        report["checks"] = list(reversed(report["checks"]))
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_check_with_fail_verdict_fails(self) -> None:
        report = _build_golden_report()
        report["checks"][0]["verdict"] = "FAIL"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)


# ---------------------------------------------------------------------------
# Fault injection tests
# ---------------------------------------------------------------------------

class FaultInjectionTests(unittest.TestCase):
    def test_connection_failure_raises_connection_error(self) -> None:
        adapter = _golden_adapter()
        adapter.connect_should_fail = True
        with self.assertRaises(DatabaseConnectionError):
            build_logical_site_report(adapter)

    def test_catalog_drift_versioned_in_enum_but_not_in_catalog(self) -> None:
        report = _build_golden_report()
        # Add a versioned collection to enumeration but not to catalog
        report["seven_collection_enumeration"]["versioned_collections"].append(
            "seven_ghost_v1"
        )
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.CATALOG_DRIFT, codes)

    def test_catalog_drift_conflict_check_mismatches_enumeration(self) -> None:
        report = _build_golden_report()
        report["conflict_check"]["has_conflicts"] = True
        report["conflict_check"]["conflicts"] = ["fake:conflict"]
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.CATALOG_DRIFT, codes)

    def test_fingerprint_hash_format_validation(self) -> None:
        """A site_fingerprint_hash with invalid format is rejected."""
        report = _build_golden_report()
        report["site_fingerprint_hash"] = "not-a-hash"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.SITE_FINGERPRINT_MISMATCH, codes)

    def test_fingerprint_field_mismatch_detected(self) -> None:
        report = _build_golden_report()
        report["site_fingerprint"]["driver_name"] = ""
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.SITE_FINGERPRINT_MISMATCH, codes)

    def test_not_connected_adapter_raises(self) -> None:
        adapter = FakeLogicalSiteAdapter(
            database_name_value=EXPECTED_DATABASE,
            current_database_value=EXPECTED_DATABASE,
            fingerprint=_golden_fingerprint(),
            catalog=_golden_catalog(),
        )
        # Don't call connect_readonly — but build_logical_site_report calls it
        # So we test the adapter directly
        with self.assertRaises(DatabaseConnectionError):
            adapter.current_database()
        with self.assertRaises(DatabaseConnectionError):
            adapter.site_fingerprint()
        with self.assertRaises(DatabaseConnectionError):
            adapter.catalog_snapshot()
        with self.assertRaises(DatabaseConnectionError):
            adapter.enumerate_seven_collections()

    def test_database_identity_hash_format_validation(self) -> None:
        report = _build_golden_report()
        report["database_identity_hash"] = "not-a-hash"
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)

    def test_side_effects_wrong_set_fails(self) -> None:
        report = _build_golden_report()
        report["side_effects"]["extra_key"] = 0
        errors = verify_logical_site_report(report)
        codes = {e[0] for e in errors}
        self.assertIn(EC.REQUIRED_FIELD_MISSING, codes)


# ---------------------------------------------------------------------------
# Unit tests for site_adapter helpers
# ---------------------------------------------------------------------------

class SiteAdapterHelperTests(unittest.TestCase):
    def test_classify_versioned_collection(self) -> None:
        self.assertEqual(classify_collection("seven_records_v1"), "versioned")
        self.assertEqual(classify_collection("seven_outbox_v2"), "versioned")
        self.assertEqual(classify_collection("seven_work_events_v10"), "versioned")

    def test_classify_unversioned_seven_collection(self) -> None:
        self.assertEqual(classify_collection("seven_records"), "unversioned_seven")
        self.assertEqual(classify_collection("seven_data"), "unversioned_seven")
        self.assertEqual(classify_collection("seven_v1"), "unversioned_seven")

    def test_classify_forbidden_collection(self) -> None:
        self.assertEqual(classify_collection("math_problems"), "forbidden")
        self.assertEqual(classify_collection("system_users"), "forbidden")

    def test_classify_other_collection(self) -> None:
        self.assertEqual(classify_collection("foo"), "other")
        self.assertEqual(classify_collection("_key"), "other")

    def test_enumerate_collections_from_catalog_golden(self) -> None:
        catalog = _golden_catalog()
        enum = enumerate_collections_from_catalog(catalog)
        self.assertEqual(len(enum.versioned_collections), 7)
        self.assertEqual(enum.unversioned_seven_collections, ())
        self.assertEqual(enum.forbidden_collections, ())
        self.assertEqual(enum.conflicts, ())

    def test_enumerate_collections_with_conflicts(self) -> None:
        cols = _seven_v1_collections()
        bad_cols = (
            CollectionSnapshot(name="seven_bad", collection_type="document", indexes=()),
            CollectionSnapshot(name="math_problems", collection_type="document", indexes=()),
        )
        catalog = CatalogSnapshot(collections=cols + bad_cols)
        enum = enumerate_collections_from_catalog(catalog)
        self.assertIn("seven_bad", enum.unversioned_seven_collections)
        self.assertIn("math_problems", enum.forbidden_collections)
        self.assertIn("unversioned:seven_bad", enum.conflicts)
        self.assertIn("forbidden:math_problems", enum.conflicts)

    def test_site_fingerprint_hash_is_deterministic(self) -> None:
        fp1 = _golden_fingerprint()
        fp2 = _golden_fingerprint()
        self.assertEqual(fp1.fingerprint_hash, fp2.fingerprint_hash)

    def test_site_fingerprint_hash_changes_with_fields(self) -> None:
        fp1 = _golden_fingerprint()
        fp2 = SiteFingerprint(
            endpoint="http://other:8529",
            server_version="arangodb-3.12.1",
            driver_name="python-arango",
            driver_version="8.1.0",
            principal="seven-readonly-user",
        )
        self.assertNotEqual(fp1.fingerprint_hash, fp2.fingerprint_hash)

    def test_catalog_hash_is_deterministic(self) -> None:
        c1 = _golden_catalog()
        c2 = _golden_catalog()
        self.assertEqual(c1.catalog_hash, c2.catalog_hash)

    def test_catalog_hash_changes_with_collections(self) -> None:
        c1 = _golden_catalog()
        extra = (CollectionSnapshot(name="seven_extra_v1", collection_type="document", indexes=()),)
        c2 = CatalogSnapshot(collections=_seven_v1_collections() + extra)
        self.assertNotEqual(c1.catalog_hash, c2.catalog_hash)

    def test_fake_adapter_write_count_defaults_to_zero(self) -> None:
        adapter = FakeLogicalSiteAdapter()
        self.assertEqual(adapter.write_count, 0)

    def test_fake_adapter_connect_sets_connected(self) -> None:
        adapter = FakeLogicalSiteAdapter()
        adapter.connect_readonly()
        self.assertTrue(adapter.connected)


# ---------------------------------------------------------------------------
# Report immutability / caller cannot inject
# ---------------------------------------------------------------------------

class ReportIntegrityTests(unittest.TestCase):
    def test_report_is_json_serializable(self) -> None:
        import json
        report = _build_golden_report()
        serialized = json.dumps(report)
        restored = json.loads(serialized)
        self.assertEqual(verify_logical_site_report(restored), ())

    def test_deep_copy_of_report_still_verifies(self) -> None:
        report = _build_golden_report()
        copied = copy.deepcopy(report)
        self.assertEqual(verify_logical_site_report(copied), ())

    def test_report_does_not_contain_password_or_secrets(self) -> None:
        report = _build_golden_report()
        serialized = str(report)
        self.assertNotIn("password", serialized.lower())
        self.assertNotIn("secret", serialized.lower())
        self.assertNotIn("credential", serialized.lower())


if __name__ == "__main__":
    unittest.main()
