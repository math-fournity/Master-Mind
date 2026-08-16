"""Fake live bundle and blind-review package materializer for VMS-41R1.

This module materializes no files by default.  It derives deterministic manifests
from frozen public case inputs and hidden reference candidates used strictly as
fake candidate outputs.  The goal is to prove future blind-review package shape
and file separation without starting Devin or creating a real live bundle.
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
from system.tests.solve_vein_analysis.build_vms41r1_live_permit_review_plan import (
    build_plan,
)


SCHEMA_VERSION = "solve-vein/vms41r1-fake-live-bundle-materializer/v1"
VISIBLE_REVIEW_FILES = (
    "problem.md",
    "raw_solver_trajectory.txt",
    "reasoning-trajectory-candidate-v2.json",
    "DONE.md",
    "candidate-output-manifest.json",
)
FORBIDDEN_HIDDEN_FILES = (
    "acceptable-sets.json",
    "reference-candidates.json",
    "negative-checks.json",
    "thresholds.json",
    "blind-review-rubric.md",
)


class VMS41R1FakeBundleError(RuntimeError):
    """Fail-closed fake bundle materializer error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def _load_json(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise VMS41R1FakeBundleError("UNSAFE_JSON", str(path))
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise VMS41R1FakeBundleError("JSON_NOT_OBJECT", str(path))
    return value


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _candidate_bytes(candidate: Mapping[str, Any]) -> bytes:
    return json.dumps(
        candidate,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _planned_case_map() -> dict[str, dict[str, Any]]:
    plan = build_plan()
    return {
        row["case_id"]: row
        for row in plan["blind_review_plan"]["case_plans"]
    }


def build_fake_materialization_plan(
    *,
    candidate_overrides: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    manifest = _load_json(FIXTURE_ROOT / "pack-manifest.json")
    reference_candidates = _load_json(FIXTURE_ROOT / "reference-candidates.json")
    planned = _planned_case_map()
    if set(planned) != set(CASE_ORDER):
        raise VMS41R1FakeBundleError("PLANNED_CASES_INVALID", str(sorted(planned)))
    candidates = dict(reference_candidates["candidates"])
    if candidate_overrides:
        candidates.update(candidate_overrides)

    rows: list[dict[str, Any]] = []
    for case_id in CASE_ORDER:
        attempt_id = manifest["attempt_ids"][case_id]
        planned_row = planned[case_id]
        if planned_row["attempt_id"] != attempt_id:
            raise VMS41R1FakeBundleError("ATTEMPT_ID_MISMATCH", case_id)
        case_root = FIXTURE_ROOT / case_id
        public_inputs = {
            "problem.md": (case_root / "problem.md").read_bytes(),
            "raw_solver_trajectory.txt": (case_root / "raw_solver_trajectory.txt").read_bytes(),
        }
        candidate_payload = _candidate_bytes(candidates[case_id])
        done_text = (
            "output=reasoning-trajectory-candidate-v2.json\n"
            f"sha256={_sha256_bytes(candidate_payload)}\n"
        ).encode("utf-8")
        output_manifest = {
            "schema_version": "solve-vein/vms41r1-fake-candidate-output-manifest/v1",
            "case_id": case_id,
            "attempt_id": attempt_id,
            "candidate_output_sha256": _sha256_bytes(candidate_payload),
            "done_sha256": _sha256_bytes(done_text),
            "source": "HIDDEN_REFERENCE_CANDIDATE_AS_FAKE_LIVE_OUTPUT",
            "explicit_nonclaims": [
                "not_a_real_devin_output",
                "not_a_live_attempt",
            ],
        }
        output_manifest_bytes = json.dumps(
            output_manifest,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
        review_files = {
            "problem.md": _sha256_bytes(public_inputs["problem.md"]),
            "raw_solver_trajectory.txt": _sha256_bytes(public_inputs["raw_solver_trajectory.txt"]),
            "reasoning-trajectory-candidate-v2.json": _sha256_bytes(candidate_payload),
            "DONE.md": _sha256_bytes(done_text),
            "candidate-output-manifest.json": _sha256_bytes(output_manifest_bytes),
        }
        if set(review_files) != set(VISIBLE_REVIEW_FILES):
            raise VMS41R1FakeBundleError("VISIBLE_FILES_MISMATCH", case_id)
        rows.append(
            {
                "case_id": case_id,
                "attempt_id": attempt_id,
                "fake_live_bundle_status": "PLANNED_NOT_WRITTEN",
                "blind_review_package_status": "PLANNED_NOT_WRITTEN",
                "reviewer_visible_files": review_files,
                "forbidden_hidden_files": list(FORBIDDEN_HIDDEN_FILES),
                "hidden_files_exposed": [],
                "candidate_output_source": "HIDDEN_REFERENCE_CANDIDATE_AS_FAKE_LIVE_OUTPUT",
                "candidate_output_sha256": _sha256_bytes(candidate_payload),
                "candidate_output_manifest_sha256": _sha256_bytes(output_manifest_bytes),
            }
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "materializer_status": "PLAN_ONLY_NO_FILES_WRITTEN",
        "case_count": len(rows),
        "case_rows": rows,
        "fake_live_output_count": len(rows),
        "blind_review_package_count": len(rows),
        "hidden_public_split_verdict": (
            "PASS"
            if all(not row["hidden_files_exposed"] for row in rows)
            else "FAIL"
        ),
        "side_effects": {
            "files_written": 0,
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
        },
        "explicit_nonclaims": [
            "does_not_create_real_live_bundle",
            "does_not_create_real_blind_review_package",
            "does_not_use_real_devin_output",
            "does_not_authorize_live_execution",
            "does_not_qualify_event_extractor_profile",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(json.dumps(build_fake_materialization_plan(), ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, VMS41R1FakeBundleError) as exc:
        print(f"VMS41R1_FAKE_BUNDLE_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
