"""Operator CLI for preregistered POC-VMS-39 AGENTS visibility cells.

The runner reuses the independent solve-side tmux debug runtime.  It never
reads a problem, solution, Trace, Tell, Seven state, database, or Redis.  The
primary endpoint is exact AGENTS-byte visibility in the sealed ATIF export;
the model-written sentinel report is only a secondary endpoint.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sys
import tempfile
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.agents_limit import (
    AGENTS_VISIBILITY_REPORT_SCHEMA_VERSION,
    CELL_SIZES,
    fixture_manifest,
    grade_agents_visibility,
    write_fixture_exclusive,
)
from system.solve_vein_analysis.role_runtime import (
    DevinRoleSpec,
    RoleRuntimeError,
    canonical_json_bytes,
    sha256_file,
)
from system.solve_vein_analysis.tmux_runtime import (
    TmuxDebugHandle,
    abort_tmux_debug_role,
    finalize_tmux_debug_role,
    load_tmux_debug_handle,
    send_tmux_debug_keys,
    snapshot_tmux_debug_role,
    start_tmux_debug_role,
)
from system.tests.solve_vein_analysis.run_live_poc import (
    _load_preexecution_freeze_manifest,
)
from system.tests.solve_vein_analysis.run_tmux_canary import (
    _validate_approved_data_root,
)


POC_ID = "POC-VMS-39"
EXPECTED_OUTPUT_NAME = "agents-visibility-report.json"
GRADER_REPORT_NAME = "agents-visibility-grader-report.json"


def _emit(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2))


def expected_attempt_id(cell_id: str) -> str:
    if cell_id not in CELL_SIZES:
        raise RuntimeError(f"unknown VMS-39 cell: {cell_id!r}")
    return f"poc-vms-39-{cell_id.lower()}-tmux-a1"


def validate_attempt_id(cell_id: str, attempt_id: str) -> None:
    expected = expected_attempt_id(cell_id)
    if attempt_id != expected:
        raise RuntimeError(
            "attempt ID must bind the POC cell exactly: "
            f"expected {expected!r}, received {attempt_id!r}"
        )


def task_text(cell_id: str) -> str:
    if cell_id not in CELL_SIZES:
        raise RuntimeError(f"unknown VMS-39 cell: {cell_id!r}")
    return f"""Use only the rule content that was already loaded into your context at
session start. Do NOT open, read, grep, list, inspect, or execute AGENTS.md.
Do not access any path outside this workspace and do not call another AI.

Write exactly one JSON object to {EXPECTED_OUTPUT_NAME} with this shape and no
unknown keys:
{{
  "schema_version": "{AGENTS_VISIBILITY_REPORT_SCHEMA_VERSION}",
  "cell_id": "{cell_id}",
  "sentinels": [
    {{"name": "<every loaded AGENTS_SENTINEL name>", "value": "<its value>"}}
  ]
}}

Report each sentinel that is actually available in your already-loaded rules.
Do not guess a missing value. Preserve the rule order. After writing the JSON,
compute its SHA-256 with shasum and write exactly:
{EXPECTED_OUTPUT_NAME} SHA256=<digest>
to DONE.md. Then stop working and wait; do not issue /exit yourself.
"""


def build_spec(
    *,
    cell_id: str,
    attempt_id: str,
    fixture_path: Path,
    output_bundle: Path,
) -> DevinRoleSpec:
    validate_attempt_id(cell_id, attempt_id)
    if not fixture_path.is_file() or fixture_path.is_symlink():
        raise RuntimeError(f"fixture must be a regular file: {fixture_path}")
    if fixture_path.stat().st_size != CELL_SIZES[cell_id]:
        raise RuntimeError("fixture byte size does not match the cell contract")
    return DevinRoleSpec(
        attempt_id=attempt_id,
        role="agents_rule_visibility_probe",
        role_asset_path=fixture_path,
        task_text=task_text(cell_id),
        inputs=(),
        expected_output_name=EXPECTED_OUTPUT_NAME,
        output_bundle=output_bundle,
        sandbox_requested=False,
        infrastructure_retry_index=0,
    )


def write_grader_report_before_seal(handle: TmuxDebugHandle) -> dict[str, Any]:
    """Grade the exited live workspace before the generic runtime seals it."""

    report_path = handle.workspace / GRADER_REPORT_NAME
    if report_path.exists() or report_path.is_symlink():
        raise RoleRuntimeError(
            "VMS39_GRADER_REPORT_EXISTS", f"refusing to overwrite {report_path}"
        )
    report = grade_agents_visibility(
        handle.workspace / "AGENTS.md",
        handle.workspace / "devin-export.json",
        handle.workspace / EXPECTED_OUTPUT_NAME,
    )
    report_path.write_bytes(canonical_json_bytes(report))
    report_path.chmod(0o600)
    return report


def finalize_agents_limit_attempt(
    handle: TmuxDebugHandle,
    *,
    explicit_tmux_binary: Path | None = None,
) -> dict[str, Any]:
    snapshot = snapshot_tmux_debug_role(
        handle, explicit_tmux_binary=explicit_tmux_binary
    )
    if snapshot["session_present"] and snapshot["pane_dead"] is not True:
        raise RoleRuntimeError(
            "TMUX_DEBUG_STILL_RUNNING", "graceful exit is required before grading"
        )
    grader = write_grader_report_before_seal(handle)
    runtime = finalize_tmux_debug_role(
        handle, explicit_tmux_binary=explicit_tmux_binary
    )
    return {
        "operation": "FINALIZED",
        "attempt_id": handle.attempt_id,
        "output_bundle": str(handle.output_bundle),
        "grader_report_ref": f"workspace/{GRADER_REPORT_NAME}",
        "grader_report_sha256": sha256_file(
            handle.output_bundle / "workspace" / GRADER_REPORT_NAME
        ),
        "primary_status": grader["primary_status"],
        "model_report": grader["model_report"],
        "runtime_receipt": runtime,
    }


def _start(arguments: argparse.Namespace) -> int:
    if arguments.poc_id != POC_ID:
        raise RuntimeError(f"poc-id must be exactly {POC_ID}")
    validate_attempt_id(arguments.cell, arguments.attempt_id)
    freeze = Path(arguments.freeze).resolve(strict=True)
    _load_preexecution_freeze_manifest(freeze, POC_ID)
    output = Path(arguments.output).resolve(strict=False)
    site_profile = _validate_approved_data_root(output)
    handle: TmuxDebugHandle | None = None
    try:
        with tempfile.TemporaryDirectory(prefix="poc-vms-39-fixture-") as temporary:
            fixture_path = Path(temporary) / "AGENTS.md"
            fixture_row = write_fixture_exclusive(arguments.cell, fixture_path)
            spec = build_spec(
                cell_id=arguments.cell,
                attempt_id=arguments.attempt_id,
                fixture_path=fixture_path,
                output_bundle=output,
            )
            handle = start_tmux_debug_role(spec)
        freeze_target = handle.live_bundle / "preexecution-freeze-manifest.json"
        shutil.copyfile(freeze, freeze_target, follow_symlinks=False)
        freeze_target.chmod(0o600)
        fixture_manifest_path = handle.live_bundle / "agents-fixture-manifest.json"
        fixture_manifest_path.write_bytes(
            canonical_json_bytes(fixture_manifest((arguments.cell,)))
        )
        fixture_manifest_path.chmod(0o600)
        snapshot = snapshot_tmux_debug_role(handle)
    except Exception:
        if handle is not None and handle.live_bundle.exists():
            abort_tmux_debug_role(
                handle,
                actor="run_agents_limit_poc",
                reason="post-launch setup failed; preserve the consumed attempt",
            )
        raise
    launch = json.loads(
        (handle.live_bundle / "tmux-debug-launch-receipt.json").read_text()
    )
    _emit(
        {
            "poc_id": POC_ID,
            "cell_id": arguments.cell,
            "operation": "STARTED",
            "live_bundle": str(handle.live_bundle),
            "output_bundle": str(handle.output_bundle),
            "attempt_id": arguments.attempt_id,
            "fixture": fixture_row,
            "freeze_manifest_sha256": sha256_file(freeze_target),
            "fixture_manifest_sha256": sha256_file(fixture_manifest_path),
            "site_profile": site_profile,
            "attach_argv": launch["attach_argv"],
            "initial_snapshot": snapshot,
        }
    )
    return 0


def _snapshot(arguments: argparse.Namespace) -> int:
    _emit(snapshot_tmux_debug_role(load_tmux_debug_handle(Path(arguments.live_bundle))))
    return 0


def _exit(arguments: argparse.Namespace) -> int:
    handle = load_tmux_debug_handle(Path(arguments.live_bundle))
    _emit(
        send_tmux_debug_keys(
            handle,
            ("/exit", "Enter"),
            actor=arguments.actor,
            reason=arguments.reason,
        )
    )
    return 0


def _finalize(arguments: argparse.Namespace) -> int:
    _emit(finalize_agents_limit_attempt(load_tmux_debug_handle(Path(arguments.live_bundle))))
    return 0


def _abort(arguments: argparse.Namespace) -> int:
    _emit(
        abort_tmux_debug_role(
            load_tmux_debug_handle(Path(arguments.live_bundle)),
            actor=arguments.actor,
            reason=arguments.reason,
        )
    )
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)
    start = commands.add_parser("start")
    start.add_argument("--poc-id", required=True)
    start.add_argument("--cell", required=True, choices=tuple(CELL_SIZES))
    start.add_argument("--attempt-id", required=True)
    start.add_argument("--freeze", required=True)
    start.add_argument("--output", required=True)
    start.set_defaults(function=_start)
    snapshot = commands.add_parser("snapshot")
    snapshot.add_argument("--live-bundle", required=True)
    snapshot.set_defaults(function=_snapshot)
    exit_command = commands.add_parser("exit")
    exit_command.add_argument("--live-bundle", required=True)
    exit_command.add_argument("--actor", required=True)
    exit_command.add_argument("--reason", required=True)
    exit_command.set_defaults(function=_exit)
    finalize = commands.add_parser("finalize")
    finalize.add_argument("--live-bundle", required=True)
    finalize.set_defaults(function=_finalize)
    abort = commands.add_parser("abort")
    abort.add_argument("--live-bundle", required=True)
    abort.add_argument("--actor", required=True)
    abort.add_argument("--reason", required=True)
    abort.set_defaults(function=_abort)
    return root


def main() -> int:
    arguments = parser().parse_args()
    return int(arguments.function(arguments))


if __name__ == "__main__":
    raise SystemExit(main())
