"""NormativeRequirementReviewRecord semantic verifier tests."""

from __future__ import annotations

import base64
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.normative_review_record import (
    verify_normative_requirement_review_record_file,
)
from seven_system.human.signature_verifier import compute_signed_bytes


INDEX_PATH = SYSTEM_ROOT / "docs" / "implementation" / "normative-requirement-index.v1.json"
DOMAIN = "seven.normative-requirement-review-record.v1"


def _ref(name: str, fill: str = "1") -> dict[str, str]:
    return {"ref": name, "sha256": fill * 64}


def _record_for_index(index: dict[str, Any], *, index_sha256: str) -> dict[str, Any]:
    decisions = []
    for clause in index["clauses"]:
        requirement_ids = list(clause.get("requirement_ids", []))
        if requirement_ids:
            decisions.append(
                {
                    "clause_id": clause["clause_id"],
                    "decision": "CONFIRMED_EXACT",
                    "requirement_ids": requirement_ids,
                    "applicable_wp_ids": list(clause["applicable_wp_ids"]),
                    "consumer_wp_ids": list(clause["consumer_wp_ids"]),
                    "consumer_assignment_basis": "INDEPENDENT_SEMANTIC_REVIEW",
                    "reason": "unit fixture confirms existing exact mapping",
                }
            )
        else:
            decisions.append(
                {
                    "clause_id": clause["clause_id"],
                    "decision": "CONFIRMED_LOCAL_ONLY",
                    "requirement_ids": [],
                    "applicable_wp_ids": ["WP-DOC0"],
                    "consumer_wp_ids": ["WP-DOC0"],
                    "consumer_assignment_basis": "INDEPENDENT_SEMANTIC_REVIEW",
                    "reason": "unit fixture keeps local-only clause under documentation governance",
                }
            )

    return {
        "schema_id": "seven/docs/normative-requirement-review-record",
        "schema_version": 1,
        "index_ref_and_hash": {"ref": str(INDEX_PATH), "sha256": index_sha256},
        "audit_assignment_ref_and_hash": _ref("audit-assignment.json", "2"),
        "reviewer_actor_id": "reviewer-unit",
        "reviewed_consumer_policy_id": index["consumer_policy"]["policy_id"],
        "temporary_doc0_consumer_nonclaim_acknowledged": True,
        "decisions": decisions,
        "remainder": {
            "unreviewed_clause_count": 0,
            "duplicate_clause_decision_count": 0,
            "unknown_requirement_count": 0,
            "unknown_work_package_count": 0,
            "consumer_unassigned_count": 0,
            "unconsumed_clause_count": 0,
            "reclassification_required_count": 0,
            "invalid_clause_count": 0,
        },
        "signature_envelope": {
            "algorithm": "Ed25519",
            "domain_separator": DOMAIN,
            "signer_actor_id": "reviewer-unit",
            "key_id": "reviewer-key-unit",
            "signed_payload_sha256": None,
            "signature_base64": None,
        },
    }


def _sign_record(record: dict[str, Any], private_key: Any) -> dict[str, Any]:
    signed = copy.deepcopy(record)
    signed_bytes = compute_signed_bytes(
        signed,
        DOMAIN.encode("utf-8"),
        signature_field_path="signature_envelope.signature_base64",
        envelope_hash_field_path="signature_envelope.signed_payload_sha256",
        top_hash_field=None,
        self_hash_field=None,
    )
    signature = private_key.sign(signed_bytes)
    signed["signature_envelope"]["signed_payload_sha256"] = hashlib.sha256(signed_bytes).hexdigest()
    signed["signature_envelope"]["signature_base64"] = base64.b64encode(signature).decode("ascii")
    return signed


def _keypair() -> tuple[Any, bytes]:
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

    private_key = Ed25519PrivateKey.generate()
    public_key_bytes = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
    return private_key, public_key_bytes


def _write_json(path: Path, payload: dict[str, Any]) -> str:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return hashlib.sha256(path.read_bytes()).hexdigest()


class TestNormativeReviewRecordVerifier(unittest.TestCase):
    def setUp(self) -> None:
        self.index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        self.index_sha = hashlib.sha256(INDEX_PATH.read_bytes()).hexdigest()
        self.private_key, self.public_key_bytes = _keypair()

    def _signed_record(
        self,
        mutate: Callable[[dict[str, Any]], None] | None = None,
        *,
        private_key: Any | None = None,
    ) -> dict[str, Any]:
        record = _record_for_index(self.index, index_sha256=self.index_sha)
        if mutate is not None:
            mutate(record)
        return _sign_record(record, private_key or self.private_key)

    def _verify_record(self, record: dict[str, Any], *, public_key_bytes: bytes | None = None) -> tuple[Any, str]:
        with tempfile.TemporaryDirectory() as tmpdir:
            record_path = Path(tmpdir) / "review.json"
            record_sha = _write_json(record_path, record)
            result = verify_normative_requirement_review_record_file(
                record_path=record_path,
                normative_index_path=INDEX_PATH,
                public_key_bytes=public_key_bytes or self.public_key_bytes,
                expected_index_sha256=self.index_sha,
                expected_record_sha256=record_sha,
            )
            return result, record_sha

    def test_full_signed_review_record_passes(self) -> None:
        result, _ = self._verify_record(self._signed_record())
        self.assertTrue(result.passed, result.details)
        self.assertEqual(result.reviewed_clause_count, len(self.index["clauses"]))
        self.assertEqual(result.index_clause_count, len(self.index["clauses"]))

    def test_cli_verifies_full_signed_record(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            record_path = Path(tmpdir) / "review.json"
            record_sha = _write_json(record_path, self._signed_record())
            result = subprocess.run(
                [
                    sys.executable,
                    str(SYSTEM_ROOT / "scripts" / "seven.py"),
                    "verify-normative-review-record",
                    "--record",
                    str(record_path),
                    "--normative-index",
                    str(INDEX_PATH),
                    "--public-key-hex",
                    self.public_key_bytes.hex(),
                    "--expected-index-sha256",
                    self.index_sha,
                    "--expected-record-sha256",
                    record_sha,
                ],
                cwd=SYSTEM_ROOT.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["verdict"], "PASS")
            self.assertEqual(payload["reviewed_clause_count"], len(self.index["clauses"]))

    def test_missing_clause_is_rejected(self) -> None:
        def mutate(record: dict[str, Any]) -> None:
            record["decisions"] = record["decisions"][:-1]

        result, _ = self._verify_record(self._signed_record(mutate))
        self.assertFalse(result.passed)
        self.assertIn("REVIEW_REMAINDER_NONZERO", result.error_codes)
        self.assertIn("REMAINDER_MISMATCH", result.error_codes)

    def test_duplicate_clause_is_rejected(self) -> None:
        def mutate(record: dict[str, Any]) -> None:
            record["decisions"].append(copy.deepcopy(record["decisions"][0]))

        result, _ = self._verify_record(self._signed_record(mutate))
        self.assertFalse(result.passed)
        self.assertIn("REVIEW_REMAINDER_NONZERO", result.error_codes)

    def test_unknown_requirement_is_rejected(self) -> None:
        def mutate(record: dict[str, Any]) -> None:
            for decision in record["decisions"]:
                if decision["decision"] == "CONFIRMED_EXACT":
                    decision["requirement_ids"].append("ZZZ-999")
                    return

        result, _ = self._verify_record(self._signed_record(mutate))
        self.assertFalse(result.passed)
        self.assertIn("REVIEW_REMAINDER_NONZERO", result.error_codes)

    def test_unknown_work_package_is_rejected(self) -> None:
        def mutate(record: dict[str, Any]) -> None:
            record["decisions"][0]["consumer_wp_ids"].append("WP-DOESNOTEXIST")

        result, _ = self._verify_record(self._signed_record(mutate))
        self.assertFalse(result.passed)
        self.assertIn("REVIEW_REMAINDER_NONZERO", result.error_codes)

    def test_reclassify_required_is_rejected_as_unresolved(self) -> None:
        def mutate(record: dict[str, Any]) -> None:
            record["decisions"][0]["decision"] = "RECLASSIFY_REQUIRED"
            record["decisions"][0]["requirement_ids"] = []

        result, _ = self._verify_record(self._signed_record(mutate))
        self.assertFalse(result.passed)
        self.assertIn("REVIEW_REMAINDER_NONZERO", result.error_codes)

    def test_wrong_index_hash_is_rejected(self) -> None:
        def mutate(record: dict[str, Any]) -> None:
            record["index_ref_and_hash"]["sha256"] = "0" * 64

        result, _ = self._verify_record(self._signed_record(mutate))
        self.assertFalse(result.passed)
        self.assertIn("INDEX_BINDING_MISMATCH", result.error_codes)

    def test_wrong_public_key_is_rejected(self) -> None:
        _, wrong_public_key_bytes = _keypair()
        result, _ = self._verify_record(self._signed_record(), public_key_bytes=wrong_public_key_bytes)
        self.assertFalse(result.passed)
        self.assertIn("SIGNED_OBJECT_INVALID", result.error_codes)

    def test_record_hash_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            record_path = Path(tmpdir) / "review.json"
            _write_json(record_path, self._signed_record())
            result = verify_normative_requirement_review_record_file(
                record_path=record_path,
                normative_index_path=INDEX_PATH,
                public_key_bytes=self.public_key_bytes,
                expected_index_sha256=self.index_sha,
                expected_record_sha256="0" * 64,
            )
            self.assertFalse(result.passed)
            self.assertIn("RECORD_HASH_MISMATCH", result.error_codes)


if __name__ == "__main__":
    unittest.main()
