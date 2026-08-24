"""DOC0 bootstrap evidence assembler tests.

The assembler is a side-effect-free guardrail: it prevents two useful receipts
from being hand-stitched into a DOC0 completion record when their subject,
plan, index, verdict, or zero-side-effect claims do not agree.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import jsonschema


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.hashing import canonical_json_bytes
from seven_system.operations.doc0_bootstrap_evidence import (
    Doc0BootstrapEvidenceError,
    ZERO_DOC0_SIDE_EFFECT_COUNTS,
    build_doc0_bootstrap_completion_record,
)


COMMIT = "a" * 40
TREE = "b" * 40
PLAN_REF = {"ref": "wp-doc0-plan.v1.json", "sha256": "1" * 64}
INDEX_REF = {"ref": "normative-requirement-index.v1.json", "sha256": "2" * 64}
DOC_CONTRACT_REF = {"ref": "evidence/wp-doc0/doc-contract.json", "sha256": "3" * 64}
TEST_RECEIPT_REF = {"ref": "evidence/wp-doc0/doc0-tests.json", "sha256": "4" * 64}


def _doc_contract_receipt() -> dict:
    return {
        "schema_id": "seven/docs/doc-contract-verification-receipt",
        "implementation_subject": {
            "commit": COMMIT,
            "tree": TREE,
            "working_tree_clean": True,
            "source_relation": "COMMITTED_TREE",
        },
        "work_package_plan_ref_and_hash": dict(PLAN_REF),
        "normative_index_ref_and_hash": dict(INDEX_REF),
        "verdict": "PASS",
        "errors": [],
    }


def _doc0_test_receipt() -> dict:
    return {
        "schema_id": "seven/docs/doc0-test-execution-receipt",
        "wp_id": "WP-DOC0",
        "implementation_subject": {
            "commit": COMMIT,
            "tree": TREE,
            "working_tree_clean_before_tests": True,
            "source_relation": "COMMITTED_TREE",
        },
        "work_package_plan_ref_and_hash": dict(PLAN_REF),
        "normative_index_ref_and_hash": dict(INDEX_REF),
        "aggregate_verdict": "PASS",
        "side_effect_counts": dict(ZERO_DOC0_SIDE_EFFECT_COUNTS),
    }


def _build_record(
    doc_contract_receipt: dict | None = None,
    doc0_test_receipt: dict | None = None,
) -> dict:
    return build_doc0_bootstrap_completion_record(
        record_id="wp-doc0-bootstrap-unit-001",
        doc_contract_receipt=doc_contract_receipt or _doc_contract_receipt(),
        doc_contract_receipt_ref_and_hash=dict(DOC_CONTRACT_REF),
        doc0_test_receipt=doc0_test_receipt or _doc0_test_receipt(),
        doc0_test_receipt_ref_and_hash=dict(TEST_RECEIPT_REF),
        created_at="2026-08-14T20:12:00Z",
        creator="unit-test",
    )


class TestDoc0BootstrapEvidenceAssembler(unittest.TestCase):
    def test_builds_schema_valid_record(self) -> None:
        record = _build_record()
        schema = json.loads(
            (SYSTEM_ROOT / "docs" / "implementation" / "doc-bootstrap-completion-record.v1.schema.json").read_text()
        )
        errors = list(
            jsonschema.Draft202012Validator(
                schema, format_checker=jsonschema.FormatChecker()
            ).iter_errors(record)
        )
        self.assertEqual(errors, [])
        self.assertEqual(record["implementation_subject"], {"commit": COMMIT, "tree": TREE})
        self.assertEqual(record["side_effect_counts"], ZERO_DOC0_SIDE_EFFECT_COUNTS)

        expected_hash_payload = dict(record)
        expected_hash_payload["record_hash"] = None
        expected_hash = hashlib.sha256(canonical_json_bytes(expected_hash_payload)).hexdigest()
        self.assertEqual(record["record_hash"], expected_hash)

    def test_rejects_dirty_doc_contract_receipt(self) -> None:
        receipt = _doc_contract_receipt()
        receipt["implementation_subject"]["working_tree_clean"] = False
        receipt["implementation_subject"]["source_relation"] = "WORKING_TREE_SNAPSHOT_OVER_BASELINE"
        with self.assertRaisesRegex(Doc0BootstrapEvidenceError, "clean committed tree"):
            _build_record(doc_contract_receipt=receipt)

    def test_rejects_plan_mismatch(self) -> None:
        receipt = _doc0_test_receipt()
        receipt["work_package_plan_ref_and_hash"] = {"ref": "wp-doc0-plan.v1.json", "sha256": "9" * 64}
        with self.assertRaisesRegex(Doc0BootstrapEvidenceError, "plan refs differ"):
            _build_record(doc0_test_receipt=receipt)

    def test_rejects_nonzero_side_effect_counts(self) -> None:
        receipt = _doc0_test_receipt()
        receipt["side_effect_counts"]["remote_model_calls"] = 1
        with self.assertRaisesRegex(Doc0BootstrapEvidenceError, "nonzero side effects"):
            _build_record(doc0_test_receipt=receipt)

    def test_rejects_failing_receipt(self) -> None:
        receipt = _doc_contract_receipt()
        receipt["verdict"] = "FAIL"
        receipt["errors"] = ["unit-failure"]
        with self.assertRaisesRegex(Doc0BootstrapEvidenceError, "not PASS"):
            _build_record(doc_contract_receipt=receipt)


class TestDoc0BootstrapRecordTool(unittest.TestCase):
    def test_tool_prints_schema_valid_record(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            doc_contract = tmp / "doc-contract.json"
            doc_tests = tmp / "doc-tests.json"
            doc_contract.write_text(json.dumps(_doc_contract_receipt(), sort_keys=True))
            doc_tests.write_text(json.dumps(_doc0_test_receipt(), sort_keys=True))

            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "docs" / "implementation" / "tools" / "build_doc0_bootstrap_record.py"),
                    "--record-id",
                    "wp-doc0-bootstrap-tool-001",
                    "--doc-contract-receipt",
                    str(doc_contract),
                    "--doc-contract-ref",
                    "evidence/wp-doc0/doc-contract.json",
                    "--doc0-test-receipt",
                    str(doc_tests),
                    "--doc0-test-ref",
                    "evidence/wp-doc0/doc-tests.json",
                    "--created-at",
                    "2026-08-14T20:30:00Z",
                    "--creator",
                    "unit-test-tool",
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            record = json.loads(result.stdout)
            schema = json.loads(
                (SYSTEM_ROOT / "docs" / "implementation" / "doc-bootstrap-completion-record.v1.schema.json").read_text()
            )
            errors = list(
                jsonschema.Draft202012Validator(
                    schema, format_checker=jsonschema.FormatChecker()
                ).iter_errors(record)
            )
            self.assertEqual(errors, [])

    def test_tool_returns_3_for_dirty_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            dirty = _doc_contract_receipt()
            dirty["implementation_subject"]["working_tree_clean"] = False
            dirty["implementation_subject"]["source_relation"] = "WORKING_TREE_SNAPSHOT_OVER_BASELINE"
            doc_contract = tmp / "doc-contract.json"
            doc_tests = tmp / "doc-tests.json"
            doc_contract.write_text(json.dumps(dirty, sort_keys=True))
            doc_tests.write_text(json.dumps(_doc0_test_receipt(), sort_keys=True))

            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "docs" / "implementation" / "tools" / "build_doc0_bootstrap_record.py"),
                    "--record-id",
                    "wp-doc0-bootstrap-tool-002",
                    "--doc-contract-receipt",
                    str(doc_contract),
                    "--doc-contract-ref",
                    "evidence/wp-doc0/doc-contract.json",
                    "--doc0-test-receipt",
                    str(doc_tests),
                    "--doc0-test-ref",
                    "evidence/wp-doc0/doc-tests.json",
                    "--created-at",
                    "2026-08-14T20:30:00Z",
                    "--creator",
                    "unit-test-tool",
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 3)
            self.assertEqual(result.stdout, "")
            self.assertIn("clean committed tree", result.stderr)


if __name__ == "__main__":
    unittest.main()
