"""Run the zero-model static-loader stage of POC-VMS-39.

This operator command invokes only ``devin --version`` and
``devin rules paths/list/show`` inside isolated HOME/XDG directories.  It does
not launch a Devin session or contact a model.  The result is an append-once D
volume evidence bundle; static rule display is never treated as proof of the
effective model prompt.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Iterable
import uuid

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.agents_limit import (
    CELL_SIZES,
    parse_sentinels,
    write_fixture_exclusive,
)
from system.solve_vein_analysis.role_runtime import canonical_json_bytes, sha256_file
from system.tests.solve_vein_analysis.run_live_poc import (
    _load_preexecution_freeze_manifest,
)
from system.tests.solve_vein_analysis.run_tmux_canary import (
    POC_RESULTS_ROOT,
    _validate_approved_data_root,
)


POC_ID = "POC-VMS-39"
SCHEMA_VERSION = "solve-vein/agents-static-loader-bundle/v1"
STATIC_COMMANDS: tuple[tuple[str, ...], ...] = (
    ("rules", "paths"),
    ("rules", "list"),
    ("rules", "show", "AGENTS"),
)


class StaticLoaderError(RuntimeError):
    """Fail-closed error for an invalid static-loader invocation."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _write_once(path: Path, payload: bytes) -> None:
    if path.exists() or path.is_symlink():
        raise StaticLoaderError(f"refusing to overwrite evidence: {path}")
    path.write_bytes(payload)
    path.chmod(0o600)


def _minimal_static_environment(workspace: Path) -> dict[str, str]:
    home = workspace / "isolated-home"
    xdg = workspace / "isolated-xdg"
    home.mkdir(mode=0o700)
    xdg.mkdir(mode=0o700)
    return {
        "HOME": str(home),
        "XDG_CONFIG_HOME": str(xdg),
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "LANG": "en_US.UTF-8",
        "LC_ALL": "en_US.UTF-8",
        "TERM": "dumb",
    }


def _run_command(
    *,
    binary: Path,
    arguments: tuple[str, ...],
    workspace: Path,
    environment: dict[str, str],
    evidence_dir: Path,
    label: str,
) -> dict[str, Any]:
    argv = (str(binary), *arguments)
    started_at = _utc_now()
    try:
        completed = subprocess.run(
            argv,
            cwd=workspace,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=30,
        )
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or b""
        stderr = exc.stderr or b""
        completed = subprocess.CompletedProcess(argv, 124, stdout, stderr)
        timed_out = True
    stdout_path = evidence_dir / f"{label}.stdout"
    stderr_path = evidence_dir / f"{label}.stderr"
    _write_once(stdout_path, completed.stdout)
    _write_once(stderr_path, completed.stderr)
    return {
        "label": label,
        "argv": list(argv),
        "started_at": started_at,
        "finished_at": _utc_now(),
        "exit_code": completed.returncode,
        "timed_out": timed_out,
        "stdout_ref": stdout_path.name,
        "stdout_bytes": len(completed.stdout),
        "stdout_sha256": _sha256_bytes(completed.stdout),
        "stderr_ref": stderr_path.name,
        "stderr_bytes": len(completed.stderr),
        "stderr_sha256": _sha256_bytes(completed.stderr),
    }


def run_static_loader(
    *,
    devin_binary: Path,
    output_bundle: Path,
    protocol_path: Path,
    freeze_path: Path,
    cell_ids: Iterable[str] = CELL_SIZES,
) -> dict[str, Any]:
    """Execute and seal one static-loader evidence bundle.

    This function is filesystem-generic for deterministic tests.  The CLI adds
    the approved D-volume preflight before calling it.
    """

    selected = tuple(cell_ids)
    if not selected or len(set(selected)) != len(selected):
        raise StaticLoaderError("cell list must be non-empty and unique")
    if any(cell_id not in CELL_SIZES for cell_id in selected):
        raise StaticLoaderError("cell list contains an unknown fixture")
    if output_bundle.exists() or output_bundle.is_symlink():
        raise StaticLoaderError(f"output already exists: {output_bundle}")
    if not protocol_path.is_file() or protocol_path.is_symlink():
        raise StaticLoaderError("protocol must be a regular file")
    if not freeze_path.is_file() or freeze_path.is_symlink():
        raise StaticLoaderError("freeze manifest must be a regular file")
    resolved_binary = devin_binary.resolve(strict=True)
    if not resolved_binary.is_file():
        raise StaticLoaderError("Devin executable does not resolve to a file")

    output_bundle.parent.mkdir(parents=True, exist_ok=True)
    staging = output_bundle.parent / (
        f".{output_bundle.name}.partial-{uuid.uuid4().hex}"
    )
    staging.mkdir(mode=0o700)
    rows: list[dict[str, Any]] = []
    try:
        version_workspace = staging / "version"
        version_workspace.mkdir(mode=0o700)
        version_environment = _minimal_static_environment(version_workspace)
        version = _run_command(
            binary=resolved_binary,
            arguments=("--version",),
            workspace=version_workspace,
            environment=version_environment,
            evidence_dir=version_workspace,
            label="devin-version",
        )

        for cell_id in selected:
            cell_root = staging / cell_id
            cell_root.mkdir(mode=0o700)
            workspace = cell_root / "workspace"
            evidence_dir = cell_root / "evidence"
            workspace.mkdir(mode=0o700)
            evidence_dir.mkdir(mode=0o700)
            fixture = write_fixture_exclusive(cell_id, workspace / "AGENTS.md")
            fixture["fixture_ref"] = "workspace/AGENTS.md"
            del fixture["path"]
            environment = _minimal_static_environment(workspace)
            commands: list[dict[str, Any]] = []
            raw_outputs: dict[str, bytes] = {}
            for arguments in STATIC_COMMANDS:
                label = "-".join(arguments)
                command = _run_command(
                    binary=resolved_binary,
                    arguments=arguments,
                    workspace=workspace,
                    environment=environment,
                    evidence_dir=evidence_dir,
                    label=label,
                )
                commands.append(command)
                raw_outputs[label] = (evidence_dir / command["stdout_ref"]).read_bytes()

            runtime_side_effect_files: list[dict[str, Any]] = []
            for path in sorted(workspace.rglob("*")):
                if not path.is_file() or path == workspace / "AGENTS.md":
                    continue
                if path.is_symlink():
                    raise StaticLoaderError(f"runtime emitted an unsafe symlink: {path}")
                runtime_side_effect_files.append(
                    {
                        "ref": str(path.relative_to(workspace)),
                        "bytes": path.stat().st_size,
                        "sha256": sha256_file(path),
                    }
                )

            fixture_bytes = (workspace / "AGENTS.md").read_bytes()
            show_bytes = raw_outputs["rules-show-AGENTS"]
            sentinels = parse_sentinels(fixture_bytes)
            sentinel_matches = [
                {
                    "name": row["name"],
                    "value": row["value"],
                    "present_in_show": (
                        f"{row['name']}={row['value']}".encode("ascii") in show_bytes
                    ),
                }
                for row in sentinels
            ]
            all_commands_zero = all(
                row["exit_code"] == 0 and not row["timed_out"] for row in commands
            )
            full_exact = fixture_bytes in show_bytes
            primary_status = (
                "STATIC_SHOW_FULL_EXACT"
                if all_commands_zero and full_exact
                else "STATIC_VIEW_INSUFFICIENT"
            )
            rows.append(
                {
                    "cell_id": cell_id,
                    "fixture": fixture,
                    "isolated_environment_keys": sorted(environment),
                    "commands": commands,
                    "runtime_side_effect_files": runtime_side_effect_files,
                    "remote_config_revalidation_observed": any(
                        b"remote config revalidation" in path.read_bytes()
                        for path in workspace.rglob("*.log")
                        if path.is_file() and not path.is_symlink()
                    ),
                    "full_fixture_exact_substring_in_show": full_exact,
                    "sentinel_matches": sentinel_matches,
                    "primary_status": primary_status,
                    "explicit_nonclaim": (
                        "Static rule display does not prove effective model-prompt injection."
                    ),
                }
            )

        overall = (
            "STATIC_SHOW_FULL_EXACT_ALL_CELLS"
            if version["exit_code"] == 0
            and all(row["primary_status"] == "STATIC_SHOW_FULL_EXACT" for row in rows)
            else "STATIC_VIEW_INSUFFICIENT_OR_COMMAND_FAILURE"
        )
        receipt: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "poc_id": POC_ID,
            "stage": "A_ZERO_MODEL_STATIC_LOADER",
            "created_at": _utc_now(),
            "devin_binary_requested": str(devin_binary),
            "devin_binary_resolved": str(resolved_binary),
            "devin_binary_sha256": sha256_file(resolved_binary),
            "version_command": version,
            "protocol_ref": str(protocol_path),
            "protocol_sha256": sha256_file(protocol_path),
            "freeze_ref": str(freeze_path),
            "freeze_sha256": sha256_file(freeze_path),
            "runner_ref": str(Path(__file__).resolve()),
            "runner_sha256": sha256_file(Path(__file__).resolve()),
            "cells": rows,
            "overall_status": overall,
            "model_invocations": 0,
            "solver_invocations": 0,
            "database_connections": 0,
            "redis_connections": 0,
            "effective_prompt_claim": "NOT_TESTED_BY_STATIC_STAGE",
        }
        receipt["receipt_sha256"] = _sha256_bytes(canonical_json_bytes(receipt))
        _write_once(staging / "static-loader-receipt.json", canonical_json_bytes(receipt))
        staging.rename(output_bundle)
        return receipt
    except Exception:
        quarantine = staging.with_name(staging.name.replace(".partial-", ".quarantine-"))
        if staging.exists():
            staging.rename(quarantine)
        raise


def verify_static_loader_bundle(bundle: Path) -> dict[str, Any]:
    """Verify a sealed Stage-A bundle without trusting its path metadata."""

    if not bundle.is_dir() or bundle.is_symlink():
        raise StaticLoaderError(f"bundle must be a regular directory: {bundle}")
    receipt_path = bundle / "static-loader-receipt.json"
    if not receipt_path.is_file() or receipt_path.is_symlink():
        raise StaticLoaderError("static-loader receipt is missing or unsafe")
    try:
        receipt = json.loads(receipt_path.read_text())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise StaticLoaderError(f"receipt is not valid JSON: {exc}") from exc
    if not isinstance(receipt, dict) or receipt.get("schema_version") != SCHEMA_VERSION:
        raise StaticLoaderError("receipt schema is not recognized")

    errors: list[str] = []
    warnings: list[str] = []
    unindexed_auxiliary_files: list[dict[str, Any]] = []
    expected_files = {"static-loader-receipt.json"}
    stored_receipt_hash = receipt.get("receipt_sha256")
    unsigned = dict(receipt)
    unsigned.pop("receipt_sha256", None)
    actual_receipt_hash = _sha256_bytes(canonical_json_bytes(unsigned))
    if stored_receipt_hash != actual_receipt_hash:
        errors.append("receipt_sha256_mismatch")

    def check_stream(root: Path, command: dict[str, Any], prefix: str) -> None:
        for stream in ("stdout", "stderr"):
            ref = command.get(f"{stream}_ref")
            if not isinstance(ref, str) or Path(ref).name != ref:
                errors.append(f"{prefix}:{stream}_ref_invalid")
                continue
            relative = root.relative_to(bundle) / ref
            expected_files.add(str(relative))
            path = root / ref
            if not path.is_file() or path.is_symlink():
                errors.append(f"{prefix}:{stream}_missing_or_unsafe")
                continue
            if sha256_file(path) != command.get(f"{stream}_sha256"):
                errors.append(f"{prefix}:{stream}_sha256_mismatch")
            if path.stat().st_size != command.get(f"{stream}_bytes"):
                errors.append(f"{prefix}:{stream}_size_mismatch")

    version = receipt.get("version_command")
    if not isinstance(version, dict):
        errors.append("version_command_missing")
    else:
        check_stream(bundle / "version", version, "version")

    cells = receipt.get("cells")
    if not isinstance(cells, list):
        errors.append("cells_missing")
        cells = []
    seen: set[str] = set()
    for row in cells:
        if not isinstance(row, dict) or not isinstance(row.get("cell_id"), str):
            errors.append("cell_row_invalid")
            continue
        cell_id = row["cell_id"]
        if cell_id in seen:
            errors.append(f"{cell_id}:duplicate_cell")
            continue
        seen.add(cell_id)
        cell_root = bundle / cell_id
        fixture_path = cell_root / "workspace" / "AGENTS.md"
        expected_files.add(f"{cell_id}/workspace/AGENTS.md")
        fixture = row.get("fixture")
        if not isinstance(fixture, dict):
            errors.append(f"{cell_id}:fixture_metadata_missing")
            continue
        legacy_path = fixture.get("path")
        if isinstance(legacy_path, str) and not Path(legacy_path).exists():
            warnings.append(f"{cell_id}:legacy_staging_path_is_stale")
        fixture_ref = fixture.get("fixture_ref")
        if fixture_ref is not None and fixture_ref != "workspace/AGENTS.md":
            errors.append(f"{cell_id}:fixture_ref_invalid")
        if not fixture_path.is_file() or fixture_path.is_symlink():
            errors.append(f"{cell_id}:fixture_missing_or_unsafe")
        else:
            if sha256_file(fixture_path) != fixture.get("sha256"):
                errors.append(f"{cell_id}:fixture_sha256_mismatch")
            if fixture_path.stat().st_size != fixture.get("exact_bytes"):
                errors.append(f"{cell_id}:fixture_size_mismatch")
        commands = row.get("commands")
        if not isinstance(commands, list):
            errors.append(f"{cell_id}:commands_missing")
            continue
        for command in commands:
            if not isinstance(command, dict) or not isinstance(command.get("label"), str):
                errors.append(f"{cell_id}:command_invalid")
                continue
            check_stream(
                cell_root / "evidence",
                command,
                f"{cell_id}:{command['label']}",
            )
        runtime_side_effects = row.get("runtime_side_effect_files")
        if runtime_side_effects is None:
            runtime_side_effects = []
        elif not isinstance(runtime_side_effects, list):
            errors.append(f"{cell_id}:runtime_side_effect_files_invalid")
            runtime_side_effects = []
        for artifact in runtime_side_effects:
            if not isinstance(artifact, dict) or not isinstance(artifact.get("ref"), str):
                errors.append(f"{cell_id}:runtime_side_effect_entry_invalid")
                continue
            relative = Path(artifact["ref"])
            if relative.is_absolute() or ".." in relative.parts:
                errors.append(f"{cell_id}:runtime_side_effect_ref_invalid")
                continue
            path = cell_root / "workspace" / relative
            expected_files.add(str(path.relative_to(bundle)))
            if not path.is_file() or path.is_symlink():
                errors.append(f"{cell_id}:runtime_side_effect_missing_or_unsafe:{relative}")
                continue
            if sha256_file(path) != artifact.get("sha256"):
                errors.append(f"{cell_id}:runtime_side_effect_sha256_mismatch:{relative}")
            if path.stat().st_size != artifact.get("bytes"):
                errors.append(f"{cell_id}:runtime_side_effect_size_mismatch:{relative}")
        show_path = cell_root / "evidence" / "rules-show-AGENTS.stdout"
        if fixture_path.is_file() and show_path.is_file():
            observed_full = fixture_path.read_bytes() in show_path.read_bytes()
            if observed_full != row.get("full_fixture_exact_substring_in_show"):
                errors.append(f"{cell_id}:full_exact_status_mismatch")

    actual_files: set[str] = set()
    for path in bundle.rglob("*"):
        if path.is_symlink():
            errors.append(f"unsafe_symlink:{path.relative_to(bundle)}")
        elif path.is_file():
            actual_files.add(str(path.relative_to(bundle)))
    extra_files = sorted(actual_files - expected_files)
    missing_files = sorted(expected_files - actual_files)
    for relative in extra_files:
        path = bundle / relative
        unindexed_auxiliary_files.append(
            {
                "ref": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    if extra_files:
        warnings.append(f"unindexed_auxiliary_files:{len(extra_files)}")
    if missing_files:
        errors.append(f"missing_files:{missing_files}")
    primary_integrity = "PASS" if not errors else "FAIL"
    auxiliary_integrity = "INDEXED" if not extra_files else "UNINDEXED"
    overall_integrity = (
        "PASS"
        if primary_integrity == "PASS" and auxiliary_integrity == "INDEXED"
        else "PARTIAL_UNINDEXED_AUXILIARY"
        if primary_integrity == "PASS"
        else "FAIL"
    )
    return {
        "schema_version": "solve-vein/agents-static-loader-verification/v1",
        "bundle": str(bundle),
        "artifact_integrity": overall_integrity,
        "primary_artifact_integrity": primary_integrity,
        "auxiliary_artifact_integrity": auxiliary_integrity,
        "errors": errors,
        "warnings": warnings,
        "expected_file_count": len(expected_files),
        "actual_file_count": len(actual_files),
        "unindexed_auxiliary_files": unindexed_auxiliary_files,
        "unindexed_auxiliary_manifest_sha256": _sha256_bytes(
            canonical_json_bytes(unindexed_auxiliary_files)
        ),
        "receipt_sha256_verified": stored_receipt_hash == actual_receipt_hash,
        "scientific_interpretation": "NOT_EVALUATED_BY_INTEGRITY_VERIFIER",
    }


def seal_static_loader_audit(source_bundle: Path, audit_bundle: Path) -> dict[str, Any]:
    """Seal a separate append-once audit without modifying the source bundle."""

    if audit_bundle.exists() or audit_bundle.is_symlink():
        raise StaticLoaderError(f"audit output already exists: {audit_bundle}")
    verification = verify_static_loader_bundle(source_bundle)
    source_files: list[dict[str, Any]] = []
    for path in sorted(source_bundle.rglob("*")):
        if path.is_symlink():
            raise StaticLoaderError(f"source bundle contains a symlink: {path}")
        if path.is_file():
            source_files.append(
                {
                    "ref": str(path.relative_to(source_bundle)),
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    receipt: dict[str, Any] = {
        "schema_version": "solve-vein/agents-static-loader-audit-receipt/v1",
        "created_at": _utc_now(),
        "source_bundle": str(source_bundle),
        "source_file_count": len(source_files),
        "source_file_manifest": source_files,
        "source_tree_sha256": _sha256_bytes(canonical_json_bytes(source_files)),
        "verification": verification,
        "verifier_ref": str(Path(__file__).resolve()),
        "verifier_sha256": sha256_file(Path(__file__).resolve()),
        "source_bundle_modified": False,
    }
    receipt["receipt_sha256"] = _sha256_bytes(canonical_json_bytes(receipt))
    audit_bundle.parent.mkdir(parents=True, exist_ok=True)
    staging = audit_bundle.parent / f".{audit_bundle.name}.partial-{uuid.uuid4().hex}"
    staging.mkdir(mode=0o700)
    try:
        _write_once(staging / "static-loader-audit-receipt.json", canonical_json_bytes(receipt))
        staging.rename(audit_bundle)
    except Exception:
        quarantine = staging.with_name(staging.name.replace(".partial-", ".quarantine-"))
        if staging.exists():
            staging.rename(quarantine)
        raise
    return receipt


def _run(arguments: argparse.Namespace) -> int:
    if arguments.poc_id != POC_ID:
        raise StaticLoaderError(f"poc-id must be exactly {POC_ID}")
    output = Path(arguments.output).resolve(strict=False)
    _validate_approved_data_root(output)
    if output.parent != POC_RESULTS_ROOT:
        raise StaticLoaderError(f"output must be a direct child of {POC_RESULTS_ROOT}")
    protocol = Path(arguments.protocol).resolve(strict=True)
    freeze = Path(arguments.freeze).resolve(strict=True)
    _load_preexecution_freeze_manifest(freeze, POC_ID)
    receipt = run_static_loader(
        devin_binary=Path(arguments.devin_binary),
        output_bundle=output,
        protocol_path=protocol,
        freeze_path=freeze,
    )
    print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if receipt["overall_status"] == "STATIC_SHOW_FULL_EXACT_ALL_CELLS" else 3


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument("--poc-id", required=True)
    root.add_argument("--devin-binary", required=True)
    root.add_argument("--protocol", required=True)
    root.add_argument("--freeze", required=True)
    root.add_argument("--output", required=True)
    root.set_defaults(function=_run)
    return root


def main() -> int:
    arguments = parser().parse_args()
    return int(arguments.function(arguments))


if __name__ == "__main__":
    raise SystemExit(main())
