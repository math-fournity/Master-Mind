"""Seal and verify the cross-cell live evidence summary for POC-VMS-39.

This program never launches Devin.  It reads the already sealed, one-attempt
cell bundles, hashes every source file, checks the preregistered stopping rule,
and creates one append-once aggregate receipt on the approved D-volume root.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping
import uuid

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.role_runtime import canonical_json_bytes, sha256_file
from system.tests.solve_vein_analysis.run_tmux_canary import (
    POC_RESULTS_ROOT,
    _validate_approved_data_root,
)


POC_ID = "POC-VMS-39"
SCHEMA_VERSION = "solve-vein/agents-live-aggregate-receipt/v1"
EXECUTED_CELLS = ("A16M1", "A16", "A16P1", "A32")
STOPPED_CELLS = ("A64", "A128", "A256")


class LiveAggregateError(RuntimeError):
    """Fail-closed error for an inconsistent or mutable evidence set."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _read_json(path: Path) -> dict[str, Any]:
    if not path.is_file() or path.is_symlink():
        raise LiveAggregateError(f"JSON evidence must be a regular file: {path}")
    try:
        value = json.loads(path.read_text())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise LiveAggregateError(f"invalid JSON evidence {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise LiveAggregateError(f"JSON evidence must be an object: {path}")
    return value


def _tree_manifest(root: Path) -> tuple[list[dict[str, Any]], str]:
    if not root.is_dir() or root.is_symlink():
        raise LiveAggregateError(f"evidence bundle must be a real directory: {root}")
    rows: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise LiveAggregateError(f"evidence bundle contains symlink: {path}")
        if path.is_file():
            rows.append(
                {
                    "ref": str(path.relative_to(root)),
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    if not rows:
        raise LiveAggregateError(f"evidence bundle contains no files: {root}")
    return rows, _sha256_bytes(canonical_json_bytes(rows))


def _freeze_contract(freeze_path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    freeze = _read_json(freeze_path)
    if freeze.get("poc_id") != POC_ID:
        raise LiveAggregateError("freeze manifest has wrong poc_id")
    attempts = freeze.get("planned_attempts")
    fixtures = freeze.get("fixture_contract", {}).get("cells")
    if not isinstance(attempts, list) or not isinstance(fixtures, list):
        raise LiveAggregateError("freeze manifest lacks attempts or fixture cells")
    attempt_map = {
        row.get("cell_id"): row
        for row in attempts
        if isinstance(row, dict) and isinstance(row.get("cell_id"), str)
    }
    fixture_map = {
        row.get("cell_id"): row
        for row in fixtures
        if isinstance(row, dict) and isinstance(row.get("cell_id"), str)
    }
    if set(attempt_map) != set(EXECUTED_CELLS + STOPPED_CELLS):
        raise LiveAggregateError("freeze manifest cell set drift")
    if set(fixture_map) != set(EXECUTED_CELLS + STOPPED_CELLS):
        raise LiveAggregateError("freeze fixture cell set drift")
    return attempt_map, fixture_map


def _inspect_cell(
    *,
    cell_id: str,
    bundle: Path,
    expected_attempt: Mapping[str, Any],
    expected_fixture: Mapping[str, Any],
) -> dict[str, Any]:
    if bundle.name != expected_attempt.get("final_bundle"):
        raise LiveAggregateError(f"{cell_id} final bundle name drift")
    tree, tree_hash = _tree_manifest(bundle)
    fixture_manifest = _read_json(bundle / "agents-fixture-manifest.json")
    cells = fixture_manifest.get("cells")
    if not isinstance(cells, list) or len(cells) != 1 or not isinstance(cells[0], dict):
        raise LiveAggregateError(f"{cell_id} fixture manifest must contain one cell")
    fixture = cells[0]
    agents = bundle / "workspace" / "AGENTS.md"
    if (
        fixture.get("cell_id") != cell_id
        or fixture.get("exact_bytes") != expected_fixture.get("exact_bytes")
        or fixture.get("sha256") != expected_fixture.get("sha256")
        or not agents.is_file()
        or agents.is_symlink()
        or agents.stat().st_size != expected_fixture.get("exact_bytes")
        or sha256_file(agents) != expected_fixture.get("sha256")
    ):
        raise LiveAggregateError(f"{cell_id} fixture identity mismatch")

    grader_path = bundle / "workspace" / "agents-visibility-grader-report.json"
    receipt_path = bundle / "tmux-debug-final-receipt.json"
    export_path = bundle / "workspace" / "devin-export.json"
    output_path = bundle / "workspace" / "agents-visibility-report.json"
    grader = _read_json(grader_path)
    receipt = _read_json(receipt_path)
    if receipt.get("attempt_id") != expected_attempt.get("attempt_id"):
        raise LiveAggregateError(f"{cell_id} attempt identity mismatch")
    if receipt.get("pane_dead_status") != 0 or receipt.get("intervention_count") != 1:
        raise LiveAggregateError(f"{cell_id} exit/intervention contract failed")
    if receipt.get("observed_generation_model_uids") != ["glm-5-2"]:
        raise LiveAggregateError(f"{cell_id} effective model mismatch")
    if (
        receipt.get("export_sha256") != sha256_file(export_path)
        or receipt.get("output_sha256") != sha256_file(output_path)
        or grader.get("export_sha256") != sha256_file(export_path)
        or grader.get("agents_sha256") != sha256_file(agents)
    ):
        raise LiveAggregateError(f"{cell_id} receipt-to-artifact hash mismatch")
    export_bytes = export_path.read_bytes()
    truncation_marker = b"Rule content truncated to 16384 bytes" in export_bytes
    model_report = grader.get("model_report")
    if not isinstance(model_report, dict) or model_report.get("status") != "VALID":
        raise LiveAggregateError(f"{cell_id} model report is not valid")
    return {
        "cell_id": cell_id,
        "attempt_id": expected_attempt["attempt_id"],
        "bundle": str(bundle),
        "exact_bytes": expected_fixture["exact_bytes"],
        "fixture_sha256": expected_fixture["sha256"],
        "primary_status": grader.get("primary_status"),
        "longest_exact_prefix_bytes": grader.get("longest_exact_prefix_bytes"),
        "full_exact_system_message_indexes": grader.get(
            "full_exact_system_message_indexes"
        ),
        "truncation_marker_16384_observed": truncation_marker,
        "model_report": model_report,
        "effective_model_uids": receipt["observed_generation_model_uids"],
        "pane_dead_status": receipt["pane_dead_status"],
        "intervention_count": receipt["intervention_count"],
        "grader_report_sha256": sha256_file(grader_path),
        "final_receipt_sha256": sha256_file(receipt_path),
        "export_sha256": sha256_file(export_path),
        "output_sha256": sha256_file(output_path),
        "source_file_count": len(tree),
        "source_file_manifest": tree,
        "source_tree_sha256": tree_hash,
    }


def _derive_boundary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_cell = {row["cell_id"]: row for row in rows}
    if set(by_cell) != set(EXECUTED_CELLS):
        raise LiveAggregateError("executed cell set is incomplete")
    exact_low = all(
        by_cell[cell]["primary_status"] == "FULL_EXACT_SINGLE_MESSAGE"
        for cell in ("A16M1", "A16")
    )
    boundary_break = (
        by_cell["A16P1"]["primary_status"] == "PREFIX_TRUNCATED_AT_16383"
        and by_cell["A16P1"]["truncation_marker_16384_observed"]
        and by_cell["A32"]["primary_status"] == "PREFIX_TRUNCATED_AT_16384"
        and by_cell["A32"]["longest_exact_prefix_bytes"] == 16_384
        and by_cell["A32"]["truncation_marker_16384_observed"]
    )
    runtime_clean = all(
        row["pane_dead_status"] == 0
        and row["intervention_count"] == 1
        and row["effective_model_uids"] == ["glm-5-2"]
        for row in rows
    )
    supported = exact_low and boundary_break and runtime_clean
    return {
        "verdict": (
            "SUPPORTS_EXACT_16384_BYTE_EFFECTIVE_RULE_LIMIT_WITHIN_FROZEN_PROFILE"
            if supported
            else "INCONCLUSIVE_LIVE_BOUNDARY"
        ),
        "observed_loader_cap_bytes": 16_384 if supported else None,
        "largest_full_exact_cell_bytes": 16_384 if exact_low else None,
        "smallest_observed_truncated_cell_bytes": 16_385 if boundary_break else None,
        "runtime_contract_clean": runtime_clean,
        "scope": {
            "devin_cli_version": "3000.4.25 (7e8e528a)",
            "model_uid": "glm-5-2",
            "execution_mode": "INTERACTIVE_TMUX_DEBUG",
            "evidence_lane": "DEVELOPMENT_ONLY",
        },
        "explicit_nonclaims": [
            "does_not_establish_the_limit_for_other_devin_versions_profiles_or_platforms",
            "does_not_make_agents_md_a_tell_or_trace_database",
            "does_not_qualify_any_scientific_role_or_tell_effect",
            "does_not_turn_static_256k_visibility_into_effective_model_visibility",
        ],
    }


def seal_live_aggregate(
    *,
    bundles: Mapping[str, Path],
    results_root: Path,
    protocol_path: Path,
    freeze_path: Path,
    output_bundle: Path,
) -> dict[str, Any]:
    if set(bundles) != set(EXECUTED_CELLS):
        raise LiveAggregateError("exactly four preregistered live bundles are required")
    if output_bundle.exists() or output_bundle.is_symlink():
        raise LiveAggregateError(f"aggregate output already exists: {output_bundle}")
    if not protocol_path.is_file() or protocol_path.is_symlink():
        raise LiveAggregateError("protocol must be a regular file")
    attempt_map, fixture_map = _freeze_contract(freeze_path)
    rows = [
        _inspect_cell(
            cell_id=cell,
            bundle=bundles[cell],
            expected_attempt=attempt_map[cell],
            expected_fixture=fixture_map[cell],
        )
        for cell in EXECUTED_CELLS
    ]
    stopped: list[dict[str, Any]] = []
    for cell in STOPPED_CELLS:
        expected_name = attempt_map[cell]["final_bundle"]
        final_path = results_root / expected_name
        partials = sorted(
            str(path) for path in results_root.glob(f".{expected_name}*")
        )
        if final_path.exists() or final_path.is_symlink() or partials:
            raise LiveAggregateError(f"{cell} was not allowed after stopping rule")
        stopped.append(
            {
                "cell_id": cell,
                "attempt_id": attempt_map[cell]["attempt_id"],
                "status": "NOT_RUN_BY_PREREGISTERED_STOPPING_RULE",
                "reason": "A16P1_OR_A32_INCOMPLETE",
            }
        )
    receipt: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "poc_id": POC_ID,
        "created_at": _utc_now(),
        "protocol_ref": str(protocol_path),
        "protocol_sha256": sha256_file(protocol_path),
        "freeze_ref": str(freeze_path),
        "freeze_sha256": sha256_file(freeze_path),
        "executed_cells": rows,
        "not_executed_cells": stopped,
        "boundary": _derive_boundary(rows),
        "source_bundles_modified": False,
        "aggregator_ref": str(Path(__file__).resolve()),
        "aggregator_sha256": sha256_file(Path(__file__).resolve()),
    }
    receipt["receipt_sha256"] = _sha256_bytes(canonical_json_bytes(receipt))
    output_bundle.parent.mkdir(parents=True, exist_ok=True)
    staging = output_bundle.parent / f".{output_bundle.name}.partial-{uuid.uuid4().hex}"
    staging.mkdir(mode=0o700)
    try:
        target = staging / "live-aggregate-receipt.json"
        target.write_bytes(canonical_json_bytes(receipt))
        target.chmod(0o600)
        staging.rename(output_bundle)
    except Exception:
        quarantine = staging.with_name(staging.name.replace(".partial-", ".quarantine-"))
        if staging.exists():
            staging.rename(quarantine)
        raise
    return receipt


def verify_live_aggregate(bundle: Path) -> dict[str, Any]:
    receipt_path = bundle / "live-aggregate-receipt.json"
    receipt = _read_json(receipt_path)
    stored_hash = receipt.pop("receipt_sha256", None)
    errors: list[str] = []
    if stored_hash != _sha256_bytes(canonical_json_bytes(receipt)):
        errors.append("receipt_sha256_mismatch")
    for row in receipt.get("executed_cells", []):
        if not isinstance(row, dict):
            errors.append("invalid_executed_cell_row")
            continue
        source = Path(str(row.get("bundle")))
        try:
            files, tree_hash = _tree_manifest(source)
        except LiveAggregateError as exc:
            errors.append(str(exc))
            continue
        if tree_hash != row.get("source_tree_sha256") or len(files) != row.get(
            "source_file_count"
        ):
            errors.append(f"source_tree_mismatch:{row.get('cell_id')}")
    return {
        "schema_version": "solve-vein/agents-live-aggregate-verification/v1",
        "bundle": str(bundle),
        "artifact_integrity": "PASS" if not errors else "FAIL",
        "errors": errors,
        "receipt_file_sha256": sha256_file(receipt_path),
        "receipt_sha256_verified": not errors or "receipt_sha256_mismatch" not in errors,
    }


def _parse_bundle(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("bundle must be CELL=/absolute/path")
    cell, raw_path = value.split("=", 1)
    if cell not in EXECUTED_CELLS:
        raise argparse.ArgumentTypeError(f"unexpected live cell: {cell}")
    return cell, Path(raw_path).resolve(strict=True)


def _seal(arguments: argparse.Namespace) -> int:
    output = Path(arguments.output).resolve(strict=False)
    _validate_approved_data_root(output)
    if output.parent != POC_RESULTS_ROOT:
        raise LiveAggregateError(f"output must be a direct child of {POC_RESULTS_ROOT}")
    parsed = [_parse_bundle(value) for value in arguments.bundle]
    bundles = dict(parsed)
    if len(parsed) != len(bundles):
        raise LiveAggregateError("duplicate --bundle cell")
    receipt = seal_live_aggregate(
        bundles=bundles,
        results_root=POC_RESULTS_ROOT,
        protocol_path=Path(arguments.protocol).resolve(strict=True),
        freeze_path=Path(arguments.freeze).resolve(strict=True),
        output_bundle=output,
    )
    print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if receipt["boundary"]["verdict"].startswith("SUPPORTS_") else 3


def _verify(arguments: argparse.Namespace) -> int:
    result = verify_live_aggregate(Path(arguments.bundle).resolve(strict=True))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["artifact_integrity"] == "PASS" else 3


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(required=True)
    seal = commands.add_parser("seal")
    seal.add_argument("--bundle", action="append", required=True)
    seal.add_argument("--protocol", required=True)
    seal.add_argument("--freeze", required=True)
    seal.add_argument("--output", required=True)
    seal.set_defaults(function=_seal)
    verify = commands.add_parser("verify")
    verify.add_argument("--bundle", required=True)
    verify.set_defaults(function=_verify)
    return root


def main() -> int:
    arguments = parser().parse_args()
    return int(arguments.function(arguments))


if __name__ == "__main__":
    raise SystemExit(main())
