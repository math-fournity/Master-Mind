"""Final zero-model reviewer + hidden-join receipt for POC-VMS-42.

This module joins a sealed reviewer judgment with a hidden-join receipt for the
same candidate bundle.  It is the last purely mechanical seam before any future
live State Normalizer extractor can be qualified.

Even when both synthetic development inputs pass, the profile remains not live
qualified.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.tests.solve_vein_analysis import vms42_state_normalizer_hidden_join as hidden_join
from system.tests.solve_vein_analysis import vms42_state_normalizer_manual_judgment_contract as manual
from system.tests.solve_vein_analysis import build_vms42_state_normalizer_pack as pack_builder


FINAL_JOIN_SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-final-reviewer-hidden-join/v1"
PROTOCOL_PATH = (
    REPO_ROOT
    / "docs/history/sixth-generation/rnd"
    / "384-v0-2026-08-14-POC-VMS-42-State-Normalizer-final-reviewer-hidden-join-零模型.md"
)


class VMS42FinalJoinError(RuntimeError):
    """Fail-closed final join error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def build_synthetic_final_join_inputs() -> dict[str, Any]:
    candidate_bundle = hidden_join.build_reference_candidate_bundle()
    reviewer_judgment = manual.build_synthetic_reviewer_judgment(candidate_bundle)
    hidden_receipt = hidden_join.hidden_join_state_normalizer_candidates(candidate_bundle)
    return {
        "candidate_bundle": candidate_bundle,
        "reviewer_judgment": reviewer_judgment,
        "hidden_join_receipt": hidden_receipt,
    }


def final_join_reviewer_and_hidden_receipts(
    *,
    candidate_bundle: Mapping[str, Any],
    reviewer_judgment: Mapping[str, Any],
    hidden_join_receipt: Mapping[str, Any],
) -> dict[str, Any]:
    bundle_hash = hidden_join.sha256_json(candidate_bundle)
    reviewer_errors = manual.validate_manual_judgment(
        reviewer_judgment,
        candidate_bundle=candidate_bundle,
    )
    if reviewer_errors:
        raise VMS42FinalJoinError("REVIEWER_JUDGMENT_INVALID", ";".join(reviewer_errors))
    hidden = _hidden_receipt(hidden_join_receipt)
    if hidden["pack_id"] != pack_builder.PACK_ID:
        raise VMS42FinalJoinError("PACK_ID_MISMATCH", str(hidden["pack_id"]))
    if hidden["candidate_bundle_sha256"] != bundle_hash:
        raise VMS42FinalJoinError("CANDIDATE_BUNDLE_HASH_MISMATCH", hidden["candidate_bundle_sha256"])
    if hidden["public_manifest_sha256"] != reviewer_judgment["public_manifest_sha256"]:
        raise VMS42FinalJoinError("PUBLIC_MANIFEST_HASH_MISMATCH", hidden["public_manifest_sha256"])

    manual_pass = reviewer_judgment["final_manual_verdict"] == "MANUAL_PASS"
    hidden_pass = hidden["overall_verdict"] == "PASS"
    final_pass = manual_pass and hidden_pass
    return {
        "schema_version": FINAL_JOIN_SCHEMA_VERSION,
        "pack_id": pack_builder.PACK_ID,
        "candidate_bundle_sha256": bundle_hash,
        "reviewer_judgment_sha256": sha256_json(reviewer_judgment),
        "hidden_join_receipt_sha256": sha256_json(hidden),
        "public_manifest_sha256": hidden["public_manifest_sha256"],
        "manual_verdict": reviewer_judgment["final_manual_verdict"],
        "hidden_join_verdict": hidden["overall_verdict"],
        "candidate_count": hidden["candidate_count"],
        "hidden_pass_count": hidden["pass_count"],
        "hidden_fail_count": hidden["fail_count"],
        "protocol_path": str(PROTOCOL_PATH.relative_to(REPO_ROOT)),
        "protocol_exists_at_build_time": PROTOCOL_PATH.exists(),
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
            "files_written": 0,
        },
        "profile_qualification_verdict": (
            "DEVELOPMENT_SYNTHETIC_FINAL_JOIN_PASS_NOT_LIVE_QUALIFIED"
            if final_pass
            else "FINAL_JOIN_FAIL_NOT_QUALIFIED"
        ),
        "overall_verdict": "PASS" if final_pass else "FAIL",
    }


def build_synthetic_final_join_receipt() -> dict[str, Any]:
    inputs = build_synthetic_final_join_inputs()
    return final_join_reviewer_and_hidden_receipts(
        candidate_bundle=inputs["candidate_bundle"],
        reviewer_judgment=inputs["reviewer_judgment"],
        hidden_join_receipt=inputs["hidden_join_receipt"],
    )


def assert_no_forbidden_imports(path: Path) -> tuple[str, ...]:
    tree = ast.parse(path.read_text())
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    forbidden = roots & {"arango", "requests", "socket", "subprocess", "urllib"}
    if forbidden:
        raise VMS42FinalJoinError("FORBIDDEN_IMPORT", ",".join(sorted(forbidden)))
    return tuple(sorted(roots))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--negative", action="store_true", help="join a hidden-failing development bundle")
    args = parser.parse_args()
    if args.negative:
        candidate_bundle = hidden_join.build_negative_candidate_bundle()
        reviewer_judgment = manual.build_synthetic_reviewer_judgment(candidate_bundle)
        hidden_receipt = hidden_join.hidden_join_state_normalizer_candidates(candidate_bundle)
        receipt = final_join_reviewer_and_hidden_receipts(
            candidate_bundle=candidate_bundle,
            reviewer_judgment=reviewer_judgment,
            hidden_join_receipt=hidden_receipt,
        )
    else:
        receipt = build_synthetic_final_join_receipt()
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _hidden_receipt(value: Mapping[str, Any]) -> Mapping[str, Any]:
    expected = {
        "schema_version",
        "pack_id",
        "candidate_bundle_sha256",
        "public_manifest_sha256",
        "hidden_manifest_sha256",
        "protocol_path",
        "protocol_exists_at_build_time",
        "candidate_count",
        "pass_count",
        "fail_count",
        "rows",
        "side_effects",
        "profile_qualification_verdict",
        "overall_verdict",
    }
    if set(value) != expected:
        raise VMS42FinalJoinError("HIDDEN_RECEIPT_KEYS_INVALID", str(sorted(set(value) ^ expected)))
    if value["schema_version"] != hidden_join.HIDDEN_JOIN_SCHEMA_VERSION:
        raise VMS42FinalJoinError("HIDDEN_RECEIPT_SCHEMA_MISMATCH", str(value["schema_version"]))
    return value


if __name__ == "__main__":
    raise SystemExit(main())
