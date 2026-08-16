"""Operator CLI for preregistered solve-vein tmux debug canaries."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.role_runtime import DevinRoleSpec, RoleInput, sha256_file
from system.solve_vein_analysis.tmux_runtime import (
    abort_tmux_debug_role,
    finalize_tmux_debug_role,
    load_tmux_debug_handle,
    send_tmux_debug_keys,
    snapshot_tmux_debug_role,
    start_tmux_debug_role,
)
from system.tests.solve_vein_analysis.run_live_poc import (
    ASSETS,
    FIXTURES,
    _extractor_task,
    _load_preexecution_freeze_manifest,
)


APPROVED_DATA_ROOT = Path("/data/master-mind-solve-vein-data")
POC_RESULTS_ROOT = APPROVED_DATA_ROOT / "poc-results"
D_VOLUME_README_SHA256 = "fee07273d29357edf9b3f46c05ea6f9b8651d2180e8c6593345f85621347820a"
DATA_ROOT_README_SHA256 = "43730e88ad9715ff7f584227b0bf8ca0c923dd6b888c041c744ff01ce8fce473"


def _emit(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2))


def _validate_approved_data_root(output: Path) -> dict[str, Any]:
    volume = Path("/data")
    if not os.path.ismount(volume):
        raise RuntimeError("D volume is not mounted")
    for path in (volume, APPROVED_DATA_ROOT, POC_RESULTS_ROOT):
        if not path.is_dir() or path.is_symlink():
            raise RuntimeError(f"approved data path is invalid: {path}")
    if output == POC_RESULTS_ROOT or POC_RESULTS_ROOT not in output.parents:
        raise RuntimeError(f"output must be a child of {POC_RESULTS_ROOT}")
    volume_readme = volume / "README.md"
    root_readme = APPROVED_DATA_ROOT / "README.md"
    if sha256_file(volume_readme) != D_VOLUME_README_SHA256:
        raise RuntimeError("D volume README hash differs from the frozen site profile")
    if sha256_file(root_readme) != DATA_ROOT_README_SHA256:
        raise RuntimeError("solve-vein data-root README hash differs from the frozen site profile")
    device_ids = {
        os.stat(volume).st_dev,
        os.stat(APPROVED_DATA_ROOT).st_dev,
        os.stat(POC_RESULTS_ROOT).st_dev,
    }
    if len(device_ids) != 1:
        raise RuntimeError("approved roots are not on one device")
    return {
        "volume": str(volume),
        "data_root": str(APPROVED_DATA_ROOT),
        "device_id": next(iter(device_ids)),
        "volume_readme_sha256": D_VOLUME_README_SHA256,
        "data_root_readme_sha256": DATA_ROOT_README_SHA256,
    }


def _validate_attempt_id(poc_id: str, attempt_id: str) -> None:
    expected_attempt_id = f"{poc_id.lower()}-extractor-tmux-a1"
    if attempt_id != expected_attempt_id:
        raise RuntimeError(
            "attempt ID must bind the POC identity exactly: "
            f"expected {expected_attempt_id!r}"
        )


def _start(arguments: argparse.Namespace) -> int:
    freeze = Path(arguments.freeze).resolve(strict=True)
    freeze_value = _load_preexecution_freeze_manifest(freeze, arguments.poc_id)
    _validate_attempt_id(arguments.poc_id, arguments.attempt_id)
    output = Path(arguments.output).resolve(strict=False)
    site_profile = _validate_approved_data_root(output)
    spec = DevinRoleSpec(
        attempt_id=arguments.attempt_id,
        role="reasoning_event_extractor",
        role_asset_path=ASSETS / "AGENTS_event_extractor.md",
        task_text=_extractor_task()
        + "\nAfter writing the exact output and DONE marker, stop working. "
        "Do not issue /exit yourself.\n",
        inputs=(
            RoleInput(FIXTURES / "problem.md", "problem.md"),
            RoleInput(
                FIXTURES / "raw_solver_trajectory.txt",
                "raw_solver_trajectory.txt",
            ),
        ),
        expected_output_name="reasoning-trajectory.json",
        output_bundle=output,
        sandbox_requested=False,
        infrastructure_retry_index=0,
    )
    handle = start_tmux_debug_role(spec)
    target = handle.live_bundle / "preexecution-freeze-manifest.json"
    shutil.copyfile(freeze, target, follow_symlinks=False)
    target.chmod(0o600)
    snapshot = snapshot_tmux_debug_role(handle)
    launch = json.loads(
        (handle.live_bundle / "tmux-debug-launch-receipt.json").read_text()
    )
    _emit(
        {
            "poc_id": arguments.poc_id,
            "operation": "STARTED",
            "live_bundle": str(handle.live_bundle),
            "output_bundle": str(handle.output_bundle),
            "freeze_manifest_sha256": sha256_file(target),
            "site_profile": site_profile,
            "attach_argv": launch["attach_argv"],
            "initial_snapshot": snapshot,
        }
    )
    return 0


def _snapshot(arguments: argparse.Namespace) -> int:
    handle = load_tmux_debug_handle(Path(arguments.live_bundle))
    _emit(snapshot_tmux_debug_role(handle))
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
    handle = load_tmux_debug_handle(Path(arguments.live_bundle))
    _emit(finalize_tmux_debug_role(handle))
    return 0


def _abort(arguments: argparse.Namespace) -> int:
    handle = load_tmux_debug_handle(Path(arguments.live_bundle))
    _emit(
        abort_tmux_debug_role(
            handle,
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
    start.add_argument("--output", required=True)
    start.add_argument("--freeze", required=True)
    start.add_argument("--attempt-id", required=True)
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
