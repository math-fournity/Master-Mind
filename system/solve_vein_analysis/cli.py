"""Offline CLI for the independent solve-side vein-analysis POC."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import uuid
from typing import Any, Mapping, Sequence

from . import __version__
from .integrity import implementation_tree_receipt, sha256_file
from .models import ReasoningTrajectory, TrajectoryValidationError, sha256_json
from .pipeline import analyze_incrementally, analyze_trajectory


ASSET_SCHEMA_VERSION = "solve-vein/runtime-assets/v1"
PROTECTED_ABSORB_RELATIVE_PATHS = (
    Path("assets/vein_analysis"),
    Path("tests/vein_analysis"),
)


class CliContractError(RuntimeError):
    pass


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m system.solve_vein_analysis.cli",
        description="Offline deterministic solve-side nonlinear vein analysis",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze = subparsers.add_parser("analyze", help="analyze one canonical trajectory")
    analyze.add_argument("--input", required=True, type=Path)
    analyze.add_argument("--output", required=True, type=Path)
    analyze.add_argument("--assets-dir", type=Path, default=default_assets_dir())
    analyze.add_argument("--relational-max-iterations", type=int, default=8)
    analyze.add_argument(
        "--skip-incremental-equivalence",
        action="store_true",
        help="skip the correctness-reference prefix replay (not recommended for POC evidence)",
    )

    assets = subparsers.add_parser("validate-assets", help="verify the frozen runtime assets")
    assets.add_argument("--assets-dir", type=Path, default=default_assets_dir())

    subparsers.add_parser("version", help="print the package version")
    return parser


def default_assets_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "solve_vein_analysis"


def validate_asset_manifest(assets_dir: Path) -> dict[str, Any]:
    root = _require_real_directory(assets_dir, "assets directory")
    manifest_path = root / "asset-manifest.json"
    _reject_symlink(manifest_path, "asset manifest")
    try:
        raw = manifest_path.read_text(encoding="utf-8")
        manifest = json.loads(raw, parse_constant=_reject_nonfinite)
    except (OSError, json.JSONDecodeError) as exc:
        raise CliContractError(f"cannot read asset manifest: {exc}") from exc
    if not isinstance(manifest, dict):
        raise CliContractError("asset manifest must be an object")
    expected_keys = {
        "schema_version",
        "asset_set_id",
        "live_execution_status",
        "assets",
        "explicit_nonclaims",
    }
    if set(manifest) != expected_keys:
        raise CliContractError("asset manifest top-level keys are not exact")
    if manifest["schema_version"] != ASSET_SCHEMA_VERSION:
        raise CliContractError("unsupported asset manifest schema")
    if manifest["live_execution_status"] != "NOT_TESTED":
        raise CliContractError("POC assets may not claim live execution capability")
    assets = manifest["assets"]
    if not isinstance(assets, list) or not assets:
        raise CliContractError("asset manifest assets must be a non-empty array")
    seen_paths: set[str] = set()
    for index, item in enumerate(assets):
        if not isinstance(item, dict) or set(item) != {"path", "role", "sha256"}:
            raise CliContractError(f"asset entry {index} has invalid keys")
        relative = item["path"]
        if (
            not isinstance(relative, str)
            or not relative
            or Path(relative).is_absolute()
            or ".." in Path(relative).parts
        ):
            raise CliContractError(f"asset entry {index} has unsafe path")
        if relative in seen_paths:
            raise CliContractError(f"duplicate asset path {relative!r}")
        seen_paths.add(relative)
        path = root / relative
        _reject_symlink(path, f"asset {relative}")
        if not path.is_file() or path.resolve().parent != root:
            raise CliContractError(f"asset {relative!r} is missing or outside the asset root")
        actual = sha256_file(path)
        if item["sha256"] != actual:
            raise CliContractError(
                f"asset hash mismatch for {relative}: expected {item['sha256']}, got {actual}"
            )
    return {
        "manifest": manifest,
        "manifest_path": str(manifest_path),
        "manifest_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "asset_count": len(assets),
        "verdict": "PASS",
        "live_execution": "NOT_TESTED",
    }


def analyze_to_directory(
    input_path: Path,
    output_path: Path,
    assets_dir: Path,
    *,
    relational_max_iterations: int,
    check_incremental_equivalence: bool,
) -> Mapping[str, Any]:
    input_file = _require_real_file(input_path, "trajectory input")
    output = output_path.expanduser()
    if output.exists() or output.is_symlink():
        raise CliContractError(f"output path already exists: {output}")
    output_parent = _require_real_directory(output.parent, "output parent")
    output = output_parent / output.name
    _reject_protected_output(output)

    asset_report = validate_asset_manifest(assets_dir)
    input_text = input_file.read_text(encoding="utf-8")
    trajectory = ReasoningTrajectory.from_json_text(input_text)
    started_at = _utc_now()
    batch = analyze_trajectory(
        trajectory,
        relational_max_iterations=relational_max_iterations,
    )
    incremental_journal: Mapping[str, Any] = {
        "schema_version": "solve-vein/incremental-replay/v1",
        "mode": "SKIPPED_BY_EXPLICIT_CLI_FLAG",
        "prefixes": [],
        "final_scientific_fingerprint": None,
    }
    incremental_equal: bool | None = None
    if check_incremental_equivalence:
        incremental, incremental_journal = analyze_incrementally(
            trajectory,
            relational_max_iterations=relational_max_iterations,
        )
        incremental_equal = (
            incremental.scientific_fingerprint == batch.scientific_fingerprint
        )
        if not incremental_equal:
            raise CliContractError("batch and incremental scientific fingerprints differ")

    partial = output_parent / f".{output.name}.partial-{uuid.uuid4().hex}"
    partial.mkdir(mode=0o700)
    try:
        trace_payload = {
            "schema_version": "solve-vein/traces/v1",
            "trace_ruleset_version": "solve-vein-trace-rules/0.1.0",
            "trace_count": len(batch.traces),
            "traces": [trace.to_dict() for trace in batch.traces],
        }
        audit = dict(batch.audit)
        audit["checks"] = dict(audit["checks"])
        audit["checks"]["batch_incremental_scientific_fingerprint_equal"] = incremental_equal
        if incremental_equal is False:
            audit["verdicts"] = dict(audit["verdicts"])
            audit["verdicts"]["pipeline_integrity"] = "FAIL"
        payloads: dict[str, Any] = {
            "reasoning-dag.json": batch.dag.to_dict(),
            "state-context.json": batch.state_context,
            "transition-context.json": batch.transition_context,
            "state-concepts.json": batch.state_concepts,
            "transition-concepts.json": batch.transition_concepts,
            "relational-scaling.json": batch.relational_scaling,
            "traces.json": trace_payload,
            "audit-report.json": audit,
            "incremental-replay.json": incremental_journal,
        }
        for filename, payload in payloads.items():
            _write_json_fsync(partial / filename, payload)
        output_markdown = _render_markdown(batch, audit, asset_report)
        _write_text_fsync(partial / "output.md", output_markdown)

        output_hashes = {
            path.name: sha256_file(path)
            for path in sorted(partial.iterdir())
            if path.is_file()
        }
        manifest = {
            "schema_version": "solve-vein/run-manifest/v1",
            "pipeline_version": f"solve-vein-pipeline/{__version__}",
            "implementation_tree_receipt": implementation_tree_receipt(),
            "trajectory_id": trajectory.trajectory_id,
            "problem_id": trajectory.problem_id,
            "input_path": str(input_file),
            "input_file_sha256": sha256_file(input_file),
            "canonical_trajectory_sha256": trajectory.canonical_sha256,
            "asset_manifest_path": asset_report["manifest_path"],
            "asset_manifest_sha256": asset_report["manifest_sha256"],
            "started_at": started_at,
            "completed_at": _utc_now(),
            "scientific_fingerprint": batch.scientific_fingerprint,
            "incremental_equivalence_checked": check_incremental_equivalence,
            "incremental_equivalence": incremental_equal,
            "output_sha256": output_hashes,
            "live_model_calls": 0,
            "database_connections": 0,
            "solver_launches": 0,
            "verdict": "PASS",
        }
        _write_json_fsync(partial / "run-manifest.json", manifest)
        _fsync_directory(partial)
        os.replace(partial, output)
        _fsync_directory(output_parent)
    except Exception:
        if partial.exists() and partial.parent == output_parent and partial.name.startswith(
            f".{output.name}.partial-"
        ):
            shutil.rmtree(partial)
        raise
    return manifest


def _render_markdown(batch: Any, audit: Mapping[str, Any], asset_report: Mapping[str, Any]) -> str:
    trace_families = [trace.family.value for trace in batch.traces]
    return "\n".join(
        [
            "# Solve-side nonlinear vein analysis result",
            "",
            f"- Trajectory: `{batch.trajectory.trajectory_id}`",
            f"- Problem: `{batch.trajectory.problem_id}`",
            f"- Occurrences: {len(batch.dag.nodes)}",
            f"- Typed edges: {len(batch.dag.edges)}",
            f"- Branch points: {len(batch.dag.branch_points)}",
            f"- Revisit occurrences: {len(batch.dag.revisit_events)}",
            f"- Explicit merge occurrences: {len(batch.dag.explicit_merge_events)}",
            f"- Traces: {len(batch.traces)}",
            f"- Trace families: {', '.join(trace_families) if trace_families else '(none)' }",
            f"- Scientific fingerprint: `{batch.scientific_fingerprint}`",
            f"- Runtime assets: {asset_report['verdict']} ({asset_report['asset_count']} files)",
            f"- Live extraction: {audit['verdicts']['live_extraction']}",
            "",
            "## Boundary",
            "",
            "This result starts from a canonical structured event trajectory. It does not prove",
            "that raw natural-language Solver thinking can yet be extracted with the same fidelity.",
            "It made zero model calls, zero database connections, and zero Solver launches.",
            "",
        ]
    )


def _write_json_fsync(path: Path, value: Any) -> None:
    data = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        indent=2,
    ) + "\n"
    _write_text_fsync(path, data)


def _write_text_fsync(path: Path, value: str) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    descriptor = os.open(path, flags, 0o600)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        try:
            os.close(descriptor)
        except OSError:
            pass
        raise


def _require_real_file(path: Path, label: str) -> Path:
    expanded = path.expanduser()
    _reject_symlink(expanded, label)
    if not expanded.is_file():
        raise CliContractError(f"{label} is not a file: {expanded}")
    return expanded.resolve(strict=True)


def _require_real_directory(path: Path, label: str) -> Path:
    expanded = path.expanduser()
    _reject_symlink(expanded, label)
    if not expanded.is_dir():
        raise CliContractError(f"{label} is not a directory: {expanded}")
    return expanded.resolve(strict=True)


def _reject_symlink(path: Path, label: str) -> None:
    if path.is_symlink():
        raise CliContractError(f"{label} must not be a symlink: {path}")


def _reject_protected_output(output: Path) -> None:
    system_root = Path(__file__).resolve().parents[1]
    resolved_candidate = output.parent.resolve() / output.name
    for protected_relative in PROTECTED_ABSORB_RELATIVE_PATHS:
        protected = (system_root / protected_relative).resolve()
        if resolved_candidate == protected or resolved_candidate.is_relative_to(protected):
            raise CliContractError(f"output is inside protected absorb path: {protected}")


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _reject_nonfinite(value: str) -> Any:
    raise CliContractError(f"non-finite JSON number is forbidden: {value}")


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "version":
            print(__version__)
            return 0
        if args.command == "validate-assets":
            print(json.dumps(validate_asset_manifest(args.assets_dir), indent=2, sort_keys=True))
            return 0
        if args.command == "analyze":
            result = analyze_to_directory(
                args.input,
                args.output,
                args.assets_dir,
                relational_max_iterations=args.relational_max_iterations,
                check_incremental_equivalence=not args.skip_incremental_equivalence,
            )
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0
        raise CliContractError(f"unknown command: {args.command}")
    except (CliContractError, TrajectoryValidationError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
