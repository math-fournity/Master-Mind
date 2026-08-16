"""Append-only fake blind-review bundle dry-run for VMS-41R1.

This module writes fake Reviewer-visible bundles to an explicit output root.
The content is still derived from frozen public inputs and hidden reference
candidates used as fake outputs, so the receipt is development-only and must
never be used as live qualification evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.tests.solve_vein_analysis.build_vms41r1_qualification_pack import (
    CASE_ORDER,
    FIXTURE_ROOT,
)
from system.tests.solve_vein_analysis import vms41r1_fake_live_bundle_materializer as materializer


SCHEMA_VERSION = "solve-vein/vms41r1-fake-bundle-append-only-dry-run/v1"
BUNDLE_MANIFEST = "fake-bundle-manifest.json"


class VMS41R1FakeBundleDryRunError(RuntimeError):
    """Fail-closed fake bundle dry-run error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise VMS41R1FakeBundleDryRunError("UNSAFE_JSON", str(path))
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise VMS41R1FakeBundleDryRunError("JSON_NOT_OBJECT", str(path))
    return value


def _candidate_bytes(candidate: Mapping[str, Any]) -> bytes:
    return json.dumps(
        candidate,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _assert_no_symlink_ancestor(path: Path) -> None:
    current = path
    checked: list[Path] = []
    while True:
        checked.append(current)
        if current.exists() and current.is_symlink():
            raise VMS41R1FakeBundleDryRunError("SYMLINK_PATH_REJECTED", str(current))
        if current.parent == current:
            break
        current = current.parent


def _prepare_output_root(output_root: Path) -> Path:
    if output_root.exists() and output_root.is_symlink():
        raise VMS41R1FakeBundleDryRunError("SYMLINK_PATH_REJECTED", str(output_root))
    resolved = output_root.resolve()
    _assert_no_symlink_ancestor(resolved)
    try:
        resolved.relative_to(REPO_ROOT.resolve())
    except ValueError:
        pass
    else:
        raise VMS41R1FakeBundleDryRunError("REPO_OUTPUT_ROOT_REJECTED", str(output_root))
    if resolved.exists():
        if not resolved.is_dir():
            raise VMS41R1FakeBundleDryRunError("OUTPUT_ROOT_NOT_DIRECTORY", str(output_root))
        if any(resolved.iterdir()):
            raise VMS41R1FakeBundleDryRunError("OUTPUT_ROOT_NOT_EMPTY", str(output_root))
    else:
        resolved.mkdir(parents=True)
    return resolved


def _write_exclusive(path: Path, data: bytes) -> str:
    if path.exists() or path.is_symlink():
        raise VMS41R1FakeBundleDryRunError("FILE_ALREADY_EXISTS", str(path))
    with path.open("xb") as handle:
        handle.write(data)
    return _sha256_bytes(data)


def write_fake_bundle_append_only_dry_run(output_root: Path) -> dict[str, Any]:
    root = _prepare_output_root(output_root)
    manifest = _load_json(FIXTURE_ROOT / "pack-manifest.json")
    reference_candidates = _load_json(FIXTURE_ROOT / "reference-candidates.json")
    plan = materializer.build_fake_materialization_plan()
    plan_by_case = {row["case_id"]: row for row in plan["case_rows"]}

    rows: list[dict[str, Any]] = []
    files_written = 0
    for case_id in CASE_ORDER:
        case_dir = root / case_id
        if case_dir.exists() or case_dir.is_symlink():
            raise VMS41R1FakeBundleDryRunError("CASE_DIR_ALREADY_EXISTS", case_id)
        case_dir.mkdir()
        case_root = FIXTURE_ROOT / case_id
        attempt_id = manifest["attempt_ids"][case_id]
        candidate_payload = _candidate_bytes(reference_candidates["candidates"][case_id])
        done_payload = (
            "output=reasoning-trajectory-candidate-v2.json\n"
            f"sha256={_sha256_bytes(candidate_payload)}\n"
        ).encode("utf-8")
        candidate_manifest = {
            "schema_version": "solve-vein/vms41r1-fake-candidate-output-manifest/v1",
            "case_id": case_id,
            "attempt_id": attempt_id,
            "candidate_output_sha256": _sha256_bytes(candidate_payload),
            "done_sha256": _sha256_bytes(done_payload),
            "source": "HIDDEN_REFERENCE_CANDIDATE_AS_FAKE_LIVE_OUTPUT",
            "explicit_nonclaims": [
                "not_a_real_devin_output",
                "not_a_live_attempt",
            ],
        }
        file_payloads = {
            "problem.md": (case_root / "problem.md").read_bytes(),
            "raw_solver_trajectory.txt": (case_root / "raw_solver_trajectory.txt").read_bytes(),
            "reasoning-trajectory-candidate-v2.json": candidate_payload,
            "DONE.md": done_payload,
            "candidate-output-manifest.json": json.dumps(
                candidate_manifest,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            ).encode("utf-8"),
        }
        if set(file_payloads) != set(materializer.VISIBLE_REVIEW_FILES):
            raise VMS41R1FakeBundleDryRunError("VISIBLE_FILES_MISMATCH", case_id)
        file_hashes = {
            filename: _write_exclusive(case_dir / filename, payload)
            for filename, payload in file_payloads.items()
        }
        files_written += len(file_hashes)
        if file_hashes != plan_by_case[case_id]["reviewer_visible_files"]:
            raise VMS41R1FakeBundleDryRunError("PLAN_HASH_MISMATCH", case_id)
        rows.append(
            {
                "case_id": case_id,
                "attempt_id": attempt_id,
                "case_dir_name": case_id,
                "reviewer_visible_files": file_hashes,
                "forbidden_hidden_files_absent": list(materializer.FORBIDDEN_HIDDEN_FILES),
                "candidate_output_source": "HIDDEN_REFERENCE_CANDIDATE_AS_FAKE_LIVE_OUTPUT",
            }
        )

    bundle_manifest = {
        "schema_version": "solve-vein/vms41r1-fake-bundle-manifest/v1",
        "case_count": len(rows),
        "case_rows": rows,
        "explicit_nonclaims": [
            "not_a_real_live_bundle",
            "not_a_profile_qualification_bundle",
        ],
    }
    bundle_manifest_bytes = json.dumps(
        bundle_manifest,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    bundle_manifest_sha256 = _write_exclusive(root / BUNDLE_MANIFEST, bundle_manifest_bytes)
    files_written += 1
    return {
        "schema_version": SCHEMA_VERSION,
        "dry_run_status": "APPEND_ONLY_FAKE_BUNDLE_WRITTEN",
        "output_root": str(root),
        "case_count": len(rows),
        "case_rows": rows,
        "bundle_manifest": BUNDLE_MANIFEST,
        "bundle_manifest_sha256": bundle_manifest_sha256,
        "side_effects": {
            "local_files_written": files_written,
            "hidden_files_written": 0,
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
        },
        "profile_qualification_verdict": "NOT_QUALIFIED_LIVE_NOT_AUTHORIZED",
        "explicit_nonclaims": [
            "does_not_use_real_devin_output",
            "does_not_authorize_live_execution",
            "does_not_qualify_event_extractor_profile",
            "writes_only_to_explicit_output_root",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            write_fake_bundle_append_only_dry_run(args.output_root),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, VMS41R1FakeBundleDryRunError, materializer.VMS41R1FakeBundleError) as exc:
        print(f"VMS41R1_FAKE_BUNDLE_DRY_RUN_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
