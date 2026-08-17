from __future__ import annotations

import json
import base64
import copy
import hashlib
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch
from typing import Any


def build_site(tmp_path: Path, *, mode: str = "dry_run") -> tuple[Path, dict]:
    repository_root = tmp_path / "repo" / "seven-system"
    asset_root = repository_root / "assets" / "solver"
    asset_root.mkdir(parents=True)
    (asset_root / "AGENTS.md").write_text(
        "不要使用任何工具\n### PROOF COMPLETE\n### I CANNOT SOLVE THIS\n",
        encoding="utf-8",
    )

    volume_root = tmp_path / "volume"
    volume_root.mkdir()
    (volume_root / "README.md").write_text("test volume\n", encoding="utf-8")
    data_root = volume_root / "seven-system-data"
    data_root.mkdir()
    solver_work_root = data_root / "solver-work"
    trajectory_root = data_root / "trajectory"
    solver_work_root.mkdir()
    trajectory_root.mkdir()

    harness = tmp_path / "solver_harness.py"
    harness.write_text("# fixture\n", encoding="utf-8")

    payload = {
        "schema_version": "seven-config/v1",
        "system_id": "seven-system",
        "mode": mode,
        "repository_root": str(repository_root),
        "storage": {
            "volume_root": str(volume_root),
            "data_root": str(data_root),
            "minimum_free_bytes": 0,
            "require_volume_readme": True,
        },
        "database": {
            "expected_database": "xishujuzhen_math_glm52",
            "adapter_contract": "seven-database-port/v1",
            "allow_writes": False,
            "capability_report": None,
        },
        "control": {"redis_namespace": "evidence:seven:test:"},
        "solver": {
            "harness_path": str(harness),
            "work_root": str(solver_work_root),
            "trajectory_root": str(trajectory_root),
            "tool_policy": "forbid_all",
            "launch_interval_seconds": 3,
            "max_concurrency": 2,
            "allow_live_dispatch": False,
            "safe_launch_capability_report": None,
            "no_tool_capability_report": None,
        },
        "answers": {
            "vault_root": str(data_root / "vault"),
            "capability_report": None,
        },
    }
    config_path = tmp_path / "runtime.json"
    config_path.write_text(json.dumps(payload), encoding="utf-8")
    return config_path, payload


@contextmanager
def patched_site(payload: dict):
    with patch(
        "seven_system.preflight.ACTUAL_REPOSITORY_ROOT",
        Path(payload["repository_root"]),
    ), patch("seven_system.preflight.os.path.ismount", return_value=True):
        yield


def write_pass_capability(
    path: Path, name: str, *, subject_hash: str = "0" * 64
) -> None:
    required_claims = {
        "database": [
            "expected_database_fail_closed",
            "reads_have_no_schema_side_effects",
            "cas_and_unique_indexes_verified",
        ],
        "safe_launch": [
            "structured_argv_or_readonly_prompt_file",
            "single_canonical_prompt_render",
            "launch_receipt_is_persisted",
        ],
        "no_tool": [
            "tool_surface_removed_or_empty_registry",
            "missing_observation_fails_closed",
            "all_terminal_states_are_audited",
            "solver_has_no_db_or_vault_credentials",
        ],
        "answer_isolation": [
            "solver_cannot_access_vault",
            "role_views_are_minimum_privilege",
            "access_is_append_only_audited",
        ],
    }
    path.write_text(
        json.dumps(
            {
                "schema_version": "capability-report/v1",
                "capability": name,
                "verdict": "PASS",
                "generated_at": "2026-08-13T00:00:00Z",
                "subject_hash": subject_hash,
                "checks": [{"check_id": "fixture", "verdict": "PASS"}],
                "claims": {claim: True for claim in required_claims[name]},
            }
        ),
        encoding="utf-8",
    )


NORMATIVE_REVIEW_DOMAIN = "seven.normative-requirement-review-record.v1"


def build_normative_review_record(index: dict[str, Any], *, index_path: Path, index_sha256: str) -> dict[str, Any]:
    """Build an unsigned full-coverage NormativeRequirementReviewRecord fixture."""

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
                    "reason": "fixture confirms existing exact mapping",
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
                    "reason": "fixture keeps local-only clause under documentation governance",
                }
            )

    return {
        "schema_id": "seven/docs/normative-requirement-review-record",
        "schema_version": 1,
        "index_ref_and_hash": {"ref": str(index_path), "sha256": index_sha256},
        "audit_assignment_ref_and_hash": {"ref": "audit-assignment.json", "sha256": "2" * 64},
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
            "domain_separator": NORMATIVE_REVIEW_DOMAIN,
            "signer_actor_id": "reviewer-unit",
            "key_id": "reviewer-key-unit",
            "signed_payload_sha256": None,
            "signature_base64": None,
        },
    }


def sign_normative_review_record(record: dict[str, Any], private_key: Any) -> dict[str, Any]:
    """Sign a NormativeRequirementReviewRecord fixture with the canonical domain."""

    from seven_system.human.signature_verifier import compute_signed_bytes

    signed = copy.deepcopy(record)
    signed_bytes = compute_signed_bytes(
        signed,
        NORMATIVE_REVIEW_DOMAIN.encode("utf-8"),
        signature_field_path="signature_envelope.signature_base64",
        envelope_hash_field_path="signature_envelope.signed_payload_sha256",
        top_hash_field=None,
        self_hash_field=None,
    )
    signed["signature_envelope"]["signed_payload_sha256"] = hashlib.sha256(signed_bytes).hexdigest()
    signed["signature_envelope"]["signature_base64"] = base64.b64encode(private_key.sign(signed_bytes)).decode("ascii")
    return signed


def normative_review_keypair() -> tuple[Any, bytes]:
    """Return a fresh Ed25519 private key and raw public key bytes."""

    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

    private_key = Ed25519PrivateKey.generate()
    public_key_bytes = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
    return private_key, public_key_bytes


def write_signed_normative_review_fixture(
    path: Path,
    *,
    index_path: Path,
    mutate: Any | None = None,
) -> tuple[str, bytes, dict[str, Any]]:
    """Write a signed full-index review fixture and return ``(sha, public_key, record)``."""

    index = json.loads(index_path.read_text(encoding="utf-8"))
    index_sha = hashlib.sha256(index_path.read_bytes()).hexdigest()
    private_key, public_key_bytes = normative_review_keypair()
    record = build_normative_review_record(index, index_path=index_path, index_sha256=index_sha)
    if mutate is not None:
        mutate(record)
    signed = sign_normative_review_record(record, private_key)
    path.write_text(json.dumps(signed, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return hashlib.sha256(path.read_bytes()).hexdigest(), public_key_bytes, signed
