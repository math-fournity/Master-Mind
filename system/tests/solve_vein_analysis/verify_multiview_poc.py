"""Independent read-only verifier for the sealed POC-VMS-40 bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from system.solve_vein_analysis.integrity import sha256_file


DEFAULT_BUNDLE = Path(
    "/data/master-mind-solve-vein-data/poc-results/poc-vms-40-20260814"
)
EXPECTED_FILES = {
    "COMMITTED",
    "evaluation-matrix.json",
    "final-receipt.json",
    "implementation-tree-receipt.json",
    "run-manifest.json",
    "test-receipt.json",
    "test-stderr.txt",
    "test-stdout.txt",
}


def verify_bundle(bundle_path: Path) -> dict[str, Any]:
    errors: list[str] = []
    if bundle_path.is_symlink() or not bundle_path.is_dir():
        return _result(["bundle is absent, not a directory, or a symlink"])
    actual_names = {path.name for path in bundle_path.iterdir()}
    if actual_names != EXPECTED_FILES:
        errors.append(
            f"file set mismatch: missing={sorted(EXPECTED_FILES-actual_names)}, "
            f"unknown={sorted(actual_names-EXPECTED_FILES)}"
        )
    for path in bundle_path.iterdir():
        if path.is_symlink() or not path.is_file():
            errors.append(f"non-regular artifact: {path.name}")
    receipt = _load_json(bundle_path / "final-receipt.json", errors)
    manifest = _load_json(bundle_path / "run-manifest.json", errors)
    matrix = _load_json(bundle_path / "evaluation-matrix.json", errors)
    test_receipt = _load_json(bundle_path / "test-receipt.json", errors)
    implementation = _load_json(
        bundle_path / "implementation-tree-receipt.json", errors
    )
    if errors:
        return _result(errors)

    artifact_entries = receipt.get("artifacts", [])
    expected_primary_names = EXPECTED_FILES - {"COMMITTED", "final-receipt.json"}
    entry_names = {item.get("name") for item in artifact_entries}
    if entry_names != expected_primary_names:
        errors.append("receipt artifact names do not equal primary file names")
    for entry in artifact_entries:
        path = bundle_path / entry["name"]
        if not path.is_file():
            errors.append(f"missing artifact {entry['name']}")
            continue
        if path.stat().st_size != entry["size_bytes"]:
            errors.append(f"size mismatch {entry['name']}")
        if sha256_file(path) != entry["sha256"]:
            errors.append(f"hash mismatch {entry['name']}")
    ordered = sorted(artifact_entries, key=lambda item: item["name"])
    tree_payload = "".join(
        f"{item['sha256']}  {item['name']}\n" for item in ordered
    ).encode("utf-8")
    if hashlib.sha256(tree_payload).hexdigest() != receipt.get(
        "artifact_tree_sha256"
    ):
        errors.append("artifact tree hash mismatch")
    expected_marker = (
        f"final-receipt.json sha256="
        f"{sha256_file(bundle_path / 'final-receipt.json')}\n"
    )
    if (bundle_path / "COMMITTED").read_text() != expected_marker:
        errors.append("COMMITTED marker mismatch")

    protocol = manifest.get("protocol", {})
    protocol_path = REPOSITORY_ROOT / protocol.get("path", "<missing>")
    if (
        not protocol_path.is_file()
        or sha256_file(protocol_path) != protocol.get("sha256")
        or protocol.get("sha256") != receipt.get("protocol_sha256")
    ):
        errors.append("protocol provenance mismatch")
    fixture = manifest.get("fixture", {})
    fixture_path = REPOSITORY_ROOT / fixture.get("path", "<missing>")
    if (
        not fixture_path.is_file()
        or sha256_file(fixture_path) != fixture.get("sha256")
    ):
        errors.append("fixture provenance mismatch")

    implementation_entries = implementation.get("files", [])
    for entry in implementation_entries:
        path = REPOSITORY_ROOT / entry.get("path", "<missing>")
        if (
            path.is_symlink()
            or not path.is_file()
            or sha256_file(path) != entry.get("sha256")
        ):
            errors.append(f"implementation provenance mismatch: {entry.get('path')}")
    implementation_payload = "".join(
        f"{item['sha256']}  {item['path']}\n"
        for item in implementation_entries
    ).encode("utf-8")
    if hashlib.sha256(implementation_payload).hexdigest() != implementation.get(
        "aggregate_sha256"
    ):
        errors.append("implementation aggregate mismatch")
    if implementation.get("aggregate_sha256") != manifest.get(
        "implementation_aggregate_sha256"
    ):
        errors.append("manifest implementation hash mismatch")

    if (
        matrix.get("case_ids") != ["MV1", "MV2", "MV3", "MV4", "MV5", "MV6"]
        or matrix.get("case_count") != 6
        or matrix.get("candidate_count") != 26
        or matrix.get("mismatches") != []
        or matrix.get("all_expected_verdicts_matched") is not True
        or matrix.get("matrix_verdict") != "PASS"
    ):
        errors.append("evaluation matrix semantic summary mismatch")
    if (
        test_receipt.get("expected_test_count") != 16
        or test_receipt.get("exit_code") != 0
        or test_receipt.get("verdict") != "PASS"
        or test_receipt.get("stdout_sha256")
        != sha256_file(bundle_path / "test-stdout.txt")
        or test_receipt.get("stderr_sha256")
        != sha256_file(bundle_path / "test-stderr.txt")
    ):
        errors.append("controlled test receipt mismatch")
    if manifest.get("side_effects") != {
        "database_connections": 0,
        "model_calls": 0,
        "network_calls": 0,
        "protected_intake_mutations": 0,
        "redis_connections": 0,
        "solver_calls": 0,
    }:
        errors.append("side-effect declaration mismatch")
    if (
        receipt.get("artifact_integrity") != "PASS"
        or receipt.get("protocol_verdict") != "PASS"
        or receipt.get("scientific_verdict")
        != "PASS_WITHIN_FROZEN_MULTIVIEW_FIXTURES"
        or receipt.get("overall_verdict")
        != "PASS_WITHIN_DETERMINISTIC_OFFLINE_SCOPE"
    ):
        errors.append("final verdict fields mismatch")
    return _result(errors)


def _load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot parse {path.name}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path.name} is not a JSON object")
        return {}
    return value


def _result(errors: list[str]) -> dict[str, Any]:
    return {
        "schema_version": "solve-vein/vms40-independent-verification/v1",
        "artifact_integrity": "PASS" if not errors else "FAIL",
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle", type=Path, nargs="?", default=DEFAULT_BUNDLE)
    args = parser.parse_args()
    result = verify_bundle(args.bundle)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if result["artifact_integrity"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
