"""Observable tmux debug runtime for solve-side Devin cognitive roles.

This module deliberately does not replace the sealed non-interactive runner.
It materializes the same frozen role view, starts the interactive Devin TUI in
an isolated tmux server, and records health/pane snapshots.  Any key input is an
explicit debug intervention and is never hidden from the receipt.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from typing import Any, Mapping, Sequence
import uuid

from .role_runtime import (
    DEVIN_EFFORT_ENCODING,
    DEVIN_MODEL_UID,
    DEVIN_NORMALIZED_EFFORT,
    DevinRoleSpec,
    RoleRuntimeError,
    _file_manifest,
    _minimal_environment,
    _run_preflight_command,
    _validate_spec,
    _write_bytes,
    canonical_json_bytes,
    inspect_export,
    prepare_workspace,
    resolve_devin_binary,
    sha256_file,
    sha256_json,
)


TMUX_DEBUG_CONTROL_SCHEMA = "solve-vein/tmux-debug-control/v1"
TMUX_DEBUG_LAUNCH_SCHEMA = "solve-vein/tmux-debug-launch-receipt/v1"
TMUX_DEBUG_SNAPSHOT_SCHEMA = "solve-vein/tmux-debug-health-snapshot/v1"
TMUX_DEBUG_INTERVENTION_SCHEMA = "solve-vein/tmux-debug-intervention/v1"
TMUX_DEBUG_FINAL_SCHEMA = "solve-vein/tmux-debug-final-receipt/v1"
TMUX_DEBUG_ABORT_SCHEMA = "solve-vein/tmux-debug-abort-receipt/v1"
_SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]{0,47}$")


@dataclass(frozen=True, slots=True)
class TmuxDebugHandle:
    attempt_id: str
    live_bundle: Path
    output_bundle: Path
    workspace: Path
    socket_name: str
    session_name: str


def load_tmux_debug_handle(live_bundle: Path) -> TmuxDebugHandle:
    """Reconstruct a handle from a previously committed live control record."""

    if not live_bundle.is_dir() or live_bundle.is_symlink():
        raise RoleRuntimeError("TMUX_LIVE_BUNDLE_INVALID", str(live_bundle))
    control_path = live_bundle / "tmux-debug-control.json"
    if not control_path.is_file() or control_path.is_symlink():
        raise RoleRuntimeError("TMUX_CONTROL_MISSING", str(control_path))
    try:
        control = json.loads(control_path.read_text())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RoleRuntimeError("TMUX_CONTROL_INVALID", str(exc)) from exc
    required = {
        "attempt_id",
        "socket_name",
        "session_name",
        "output_bundle",
        "workspace_ref",
    }
    if not isinstance(control, dict) or not required <= set(control):
        raise RoleRuntimeError("TMUX_CONTROL_INVALID", "required fields are missing")
    if control["workspace_ref"] != "workspace":
        raise RoleRuntimeError("TMUX_CONTROL_INVALID", "workspace_ref must be workspace")
    output_bundle = Path(control["output_bundle"])
    if not output_bundle.is_absolute():
        raise RoleRuntimeError("TMUX_CONTROL_INVALID", "output_bundle must be absolute")
    return TmuxDebugHandle(
        attempt_id=str(control["attempt_id"]),
        live_bundle=live_bundle,
        output_bundle=output_bundle,
        workspace=live_bundle / "workspace",
        socket_name=str(control["socket_name"]),
        session_name=str(control["session_name"]),
    )


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _resolve_tmux_binary(explicit_binary: Path | None = None) -> Path:
    candidate = str(explicit_binary) if explicit_binary else shutil.which("tmux")
    if not candidate:
        raise RoleRuntimeError("TMUX_BINARY_MISSING", "tmux not found on PATH")
    resolved = Path(candidate).resolve(strict=True)
    if not resolved.is_file():
        raise RoleRuntimeError("TMUX_BINARY_INVALID", str(resolved))
    return resolved


def _safe_slug(prefix: str, attempt_id: str) -> str:
    normalized = re.sub(r"[^a-z0-9_-]+", "-", attempt_id.lower()).strip("-_")
    normalized = normalized[:24] or "attempt"
    suffix = uuid.uuid4().hex[:10]
    value = f"{prefix}-{normalized}-{suffix}"
    if not _SLUG.fullmatch(value):
        raise RoleRuntimeError("TMUX_SLUG_INVALID", value)
    return value


def _tmux(
    tmux_binary: Path,
    socket_name: str,
    arguments: Sequence[str],
    *,
    env: Mapping[str, str],
    timeout_seconds: int = 30,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(tmux_binary), "-L", socket_name, *arguments],
        check=False,
        capture_output=True,
        text=True,
        env=dict(env),
        timeout=timeout_seconds,
    )


def start_tmux_debug_role(
    spec: DevinRoleSpec,
    *,
    explicit_devin_binary: Path | None = None,
    explicit_tmux_binary: Path | None = None,
) -> TmuxDebugHandle:
    """Start one fresh interactive debug role without shell interpolation."""

    _validate_spec(spec)
    if spec.sandbox_requested:
        raise RoleRuntimeError(
            "TMUX_DEBUG_PROFILE_MISMATCH",
            "the source-compatible interactive debug profile requires sandbox=false",
        )
    devin_binary = resolve_devin_binary(explicit_devin_binary)
    tmux_binary = _resolve_tmux_binary(explicit_tmux_binary)
    env = _minimal_environment(False)
    version = _run_preflight_command((str(devin_binary), "--version"), env)
    if version.returncode != 0:
        raise RoleRuntimeError("DEVIN_VERSION_FAILED", version.stderr.strip())
    catalog = _run_preflight_command((str(devin_binary), "models", "list"), env)
    if catalog.returncode != 0:
        raise RoleRuntimeError("DEVIN_CATALOG_FAILED", catalog.stderr.strip())
    if DEVIN_MODEL_UID not in catalog.stdout or "GLM-5.2 High" not in catalog.stdout:
        raise RoleRuntimeError(
            "DEVIN_MODEL_CATALOG_MISMATCH",
            f"catalog does not expose {DEVIN_MODEL_UID!r} as GLM-5.2 High",
        )

    spec.output_bundle.parent.mkdir(parents=True, exist_ok=True)
    live_bundle = spec.output_bundle.parent / (
        f".{spec.output_bundle.name}.tmux-live-{uuid.uuid4().hex}"
    )
    if live_bundle.exists() or live_bundle.is_symlink():
        raise RoleRuntimeError("TMUX_LIVE_BUNDLE_EXISTS", str(live_bundle))
    live_bundle.mkdir(mode=0o700)
    workspace = live_bundle / "workspace"
    try:
        input_manifest = prepare_workspace(spec, workspace)
        _write_bytes(
            workspace / "catalog-snapshot.txt", catalog.stdout.encode("utf-8")
        )
        before_manifest = _file_manifest(workspace)
        socket_name = _safe_slug("svsock", spec.attempt_id)
        session_name = _safe_slug("svdebug", spec.attempt_id)
        export_path = workspace / "devin-export.json"
        devin_argv = [
            str(devin_binary),
            "--config",
            str(workspace / "devin-config.json"),
            "--permission-mode",
            "dangerous",
            "--model",
            DEVIN_MODEL_UID,
            "--export",
            str(export_path),
            "--respect-workspace-trust",
            "false",
            "--prompt-file",
            str(workspace / "TASK.md"),
        ]
        sanitized_argv = [
            "devin",
            "--config",
            "devin-config.json",
            "--permission-mode",
            "dangerous",
            "--model",
            DEVIN_MODEL_UID,
            "--export",
            "devin-export.json",
            "--respect-workspace-trust",
            "false",
            "--prompt-file",
            "TASK.md",
        ]
        intent = {
            "schema_version": TMUX_DEBUG_CONTROL_SCHEMA,
            "attempt_id": spec.attempt_id,
            "role": spec.role,
            "state": "STARTING",
            "started_at": _utc_now(),
            "socket_name": socket_name,
            "session_name": session_name,
            "workspace_ref": "workspace",
            "output_bundle": str(spec.output_bundle.resolve(strict=False)),
            "expected_output_name": spec.expected_output_name,
            "input_manifest_sha256": sha256_json(input_manifest),
            "workspace_manifest_before_sha256": sha256_json(before_manifest),
            "sanitized_argv": sanitized_argv,
            "sandbox_requested": False,
            "permission_mode": "dangerous",
            "human_intervention": "NONE",
            "evidence_lane": "DEVELOPMENT_ONLY",
        }
        _write_bytes(
            live_bundle / "tmux-debug-control.json", canonical_json_bytes(intent)
        )
        tmux_env_arguments: list[str] = []
        for name, value in sorted(env.items()):
            tmux_env_arguments.extend(("-e", f"{name}={value}"))
        launch_arguments = [
            "new-session",
            "-d",
            "-s",
            session_name,
            "-c",
            str(workspace),
            "-x",
            "160",
            "-y",
            "50",
            *tmux_env_arguments,
            *devin_argv,
            ";",
            "set-option",
            "-t",
            session_name,
            "remain-on-exit",
            "on",
        ]
        launched = _tmux(
            tmux_binary,
            socket_name,
            launch_arguments,
            env=env,
        )
        launch_receipt = {
            "schema_version": TMUX_DEBUG_LAUNCH_SCHEMA,
            "attempt_id": spec.attempt_id,
            "role": spec.role,
            "launched_at": _utc_now(),
            "launch_exit_code": launched.returncode,
            "launch_stdout": launched.stdout,
            "launch_stderr": launched.stderr,
            "socket_name": socket_name,
            "session_name": session_name,
            "attach_argv": [
                "tmux",
                "-L",
                socket_name,
                "attach-session",
                "-t",
                session_name,
            ],
            "sanitized_devin_argv": sanitized_argv,
            "resolved_devin_binary_path": str(devin_binary),
            "resolved_devin_binary_sha256": sha256_file(devin_binary),
            "resolved_tmux_binary_path": str(tmux_binary),
            "resolved_tmux_binary_sha256": sha256_file(tmux_binary),
            "cli_version": version.stdout.strip() or version.stderr.strip(),
            "requested_model_uid": DEVIN_MODEL_UID,
            "normalized_effort": DEVIN_NORMALIZED_EFFORT,
            "effort_encoding": DEVIN_EFFORT_ENCODING,
            "model_catalog_snapshot_sha256": sha256_file(
                workspace / "catalog-snapshot.txt"
            ),
            "shell_interpolation_used": False,
        }
        _write_bytes(
            live_bundle / "tmux-debug-launch-receipt.json",
            canonical_json_bytes(launch_receipt),
        )
        if launched.returncode != 0:
            raise RoleRuntimeError("TMUX_LAUNCH_FAILED", launched.stderr.strip())
        return TmuxDebugHandle(
            attempt_id=spec.attempt_id,
            live_bundle=live_bundle,
            output_bundle=spec.output_bundle,
            workspace=workspace,
            socket_name=socket_name,
            session_name=session_name,
        )
    except Exception:
        if live_bundle.exists():
            shutil.rmtree(live_bundle)
        raise


def snapshot_tmux_debug_role(
    handle: TmuxDebugHandle,
    *,
    explicit_tmux_binary: Path | None = None,
) -> dict[str, Any]:
    """Append one machine health snapshot and a pane capture if available."""

    tmux_binary = _resolve_tmux_binary(explicit_tmux_binary)
    env = _minimal_environment(False)
    snapshots = handle.live_bundle / "health-snapshots"
    captures = handle.live_bundle / "pane-captures"
    snapshots.mkdir(mode=0o700, exist_ok=True)
    captures.mkdir(mode=0o700, exist_ok=True)
    sequence = len(list(snapshots.glob("*.json")))
    sequence_name = f"{sequence:06d}"
    pane_format = "#{pane_dead}\t#{pane_dead_status}\t#{pane_pid}\t#{pane_current_command}"
    pane = _tmux(
        tmux_binary,
        handle.socket_name,
        ("list-panes", "-t", handle.session_name, "-F", pane_format),
        env=env,
    )
    session_present = pane.returncode == 0
    pane_dead: bool | None = None
    pane_dead_status: int | None = None
    pane_pid: int | None = None
    pane_command: str | None = None
    capture_ref: str | None = None
    capture_sha256: str | None = None
    if session_present:
        fields = pane.stdout.strip().split("\t")
        if len(fields) == 4:
            pane_dead = fields[0] == "1"
            pane_dead_status = int(fields[1]) if fields[1].lstrip("-").isdigit() else None
            pane_pid = int(fields[2]) if fields[2].isdigit() else None
            pane_command = fields[3] or None
        capture = _tmux(
            tmux_binary,
            handle.socket_name,
            (
                "capture-pane",
                "-p",
                "-J",
                "-S",
                "-2000",
                "-t",
                handle.session_name,
            ),
            env=env,
        )
        if capture.returncode == 0:
            capture_path = captures / f"{sequence_name}.txt"
            _write_bytes(capture_path, capture.stdout.encode("utf-8"))
            capture_ref = capture_path.relative_to(handle.live_bundle).as_posix()
            capture_sha256 = sha256_file(capture_path)
    output_name = json.loads(
        (handle.live_bundle / "tmux-debug-control.json").read_text()
    )["expected_output_name"]
    output_present = (handle.workspace / output_name).is_file()
    done_present = (handle.workspace / "DONE.md").is_file()
    export_path = handle.workspace / "devin-export.json"
    export_observation = inspect_export(export_path)
    if not session_present:
        state = "SESSION_MISSING"
    elif pane_dead:
        state = "PROCESS_EXITED"
    elif done_present:
        state = "DONE_WAITING_EXIT"
    else:
        state = "RUNNING"
    snapshot = {
        "schema_version": TMUX_DEBUG_SNAPSHOT_SCHEMA,
        "attempt_id": handle.attempt_id,
        "sequence": sequence,
        "observed_at": _utc_now(),
        "session_present": session_present,
        "pane_dead": pane_dead,
        "pane_dead_status": pane_dead_status,
        "pane_pid": pane_pid,
        "pane_current_command": pane_command,
        "output_candidate_present": output_present,
        "done_candidate_present": done_present,
        "export_candidate_present": export_path.is_file(),
        "export_json_valid": export_observation["json_valid"],
        "capture_ref": capture_ref,
        "capture_sha256": capture_sha256,
        "state": state,
    }
    _write_bytes(
        snapshots / f"{sequence_name}.json", canonical_json_bytes(snapshot)
    )
    return snapshot


def send_tmux_debug_keys(
    handle: TmuxDebugHandle,
    keys: Sequence[str],
    *,
    actor: str,
    reason: str,
    explicit_tmux_binary: Path | None = None,
) -> dict[str, Any]:
    """Send explicit debug keys and append an intervention record.

    This function never makes the run confirmatory.  It records the key names,
    not inferred intent, and rejects free-form shell or command strings.
    """

    allowed = {"C-c", "C-d", "Enter", "/exit", "/quit"}
    if not keys or any(key not in allowed for key in keys):
        raise RoleRuntimeError("TMUX_DEBUG_KEY_FORBIDDEN", repr(tuple(keys)))
    if not actor.strip() or not reason.strip():
        raise RoleRuntimeError(
            "TMUX_DEBUG_INTERVENTION_UNATTRIBUTED", "actor and reason are required"
        )
    tmux_binary = _resolve_tmux_binary(explicit_tmux_binary)
    env = _minimal_environment(False)
    results: list[subprocess.CompletedProcess[str]] = []
    for key in keys:
        if key in {"/exit", "/quit"}:
            arguments = ("send-keys", "-t", handle.session_name, "-l", key)
        else:
            arguments = ("send-keys", "-t", handle.session_name, key)
        results.append(
            _tmux(
                tmux_binary,
                handle.socket_name,
                arguments,
                env=env,
            )
        )
    first_failure = next((item for item in results if item.returncode != 0), None)
    combined_stdout = "".join(item.stdout for item in results)
    combined_stderr = "".join(item.stderr for item in results)
    interventions = handle.live_bundle / "interventions"
    interventions.mkdir(mode=0o700, exist_ok=True)
    sequence = len(list(interventions.glob("*.json")))
    record = {
        "schema_version": TMUX_DEBUG_INTERVENTION_SCHEMA,
        "attempt_id": handle.attempt_id,
        "sequence": sequence,
        "recorded_at": _utc_now(),
        "actor": actor,
        "reason": reason,
        "keys": list(keys),
        "tmux_exit_codes": [item.returncode for item in results],
        "tmux_stdout": combined_stdout,
        "tmux_stderr": combined_stderr,
        "evidence_lane_after_intervention": "DEVELOPMENT_ONLY",
    }
    _write_bytes(
        interventions / f"{sequence:06d}.json", canonical_json_bytes(record)
    )
    if first_failure is not None:
        raise RoleRuntimeError("TMUX_SEND_KEYS_FAILED", combined_stderr.strip())
    return record


def finalize_tmux_debug_role(
    handle: TmuxDebugHandle,
    *,
    explicit_tmux_binary: Path | None = None,
) -> dict[str, Any]:
    """Seal a debug bundle only after the interactive process has exited."""

    snapshot = snapshot_tmux_debug_role(
        handle, explicit_tmux_binary=explicit_tmux_binary
    )
    if snapshot["session_present"] and snapshot["pane_dead"] is not True:
        raise RoleRuntimeError(
            "TMUX_DEBUG_STILL_RUNNING", "graceful exit is required before seal"
        )
    control = json.loads(
        (handle.live_bundle / "tmux-debug-control.json").read_text()
    )
    output_path = handle.workspace / control["expected_output_name"]
    done_path = handle.workspace / "DONE.md"
    export_path = handle.workspace / "devin-export.json"
    output_sha256 = sha256_file(output_path) if output_path.is_file() else None
    done_marker_content_valid = False
    if done_path.is_file() and output_sha256 is not None:
        try:
            done_marker_content_valid = done_path.read_text().strip() == (
                f"{control['expected_output_name']} SHA256={output_sha256}"
            )
        except UnicodeDecodeError:
            done_marker_content_valid = False
    export_observation = inspect_export(export_path)
    interventions = sorted((handle.live_bundle / "interventions").glob("*.json"))
    final_receipt = {
        "schema_version": TMUX_DEBUG_FINAL_SCHEMA,
        "attempt_id": handle.attempt_id,
        "role": control["role"],
        "sealed_at": _utc_now(),
        "execution_mode": "INTERACTIVE_TMUX_DEBUG",
        "evidence_lane": "DEVELOPMENT_ONLY",
        "session_name": handle.session_name,
        "socket_name": handle.socket_name,
        "pane_dead_status": snapshot["pane_dead_status"],
        "requested_model_uid": DEVIN_MODEL_UID,
        "observed_generation_model_uids": export_observation[
            "observed_generation_model_uids"
        ],
        "model_observability_verdict": (
            "MATCH"
            if export_observation["observed_generation_model_uids"]
            == [DEVIN_MODEL_UID]
            else "UNOBSERVABLE"
            if not export_observation["observed_generation_model_uids"]
            else "MISMATCH"
        ),
        "output_ref": (
            f"workspace/{control['expected_output_name']}"
            if output_path.is_file()
            else None
        ),
        "output_sha256": output_sha256,
        "done_marker_ref": "workspace/DONE.md" if done_path.is_file() else None,
        "done_marker_sha256": sha256_file(done_path) if done_path.is_file() else None,
        "done_marker_content_valid": done_marker_content_valid,
        "export_ref": "workspace/devin-export.json" if export_path.is_file() else None,
        "export_sha256": sha256_file(export_path) if export_path.is_file() else None,
        "export_observation": export_observation,
        "intervention_count": len(interventions),
        "human_intervention": "INPUT_SENT" if interventions else "NONE",
        "workspace_manifest_after_sha256": sha256_json(
            _file_manifest(handle.workspace)
        ),
    }
    _write_bytes(
        handle.live_bundle / "tmux-debug-final-receipt.json",
        canonical_json_bytes(final_receipt),
    )
    tmux_binary = _resolve_tmux_binary(explicit_tmux_binary)
    env = _minimal_environment(False)
    _tmux(
        tmux_binary,
        handle.socket_name,
        ("kill-server",),
        env=env,
    )
    os.replace(handle.live_bundle, handle.output_bundle)
    return final_receipt


def abort_tmux_debug_role(
    handle: TmuxDebugHandle,
    *,
    actor: str,
    reason: str,
    explicit_tmux_binary: Path | None = None,
) -> dict[str, Any]:
    """Preserve and seal a failed debug attempt after an explicit kill-server.

    Abort is a development cleanup path, not a successful finalize. It keeps
    every file produced so far and records the operator, reason, final observed
    state, and the destructive tmux cleanup action before the atomic rename.
    """

    if not actor.strip() or not reason.strip():
        raise RoleRuntimeError(
            "TMUX_DEBUG_ABORT_UNATTRIBUTED", "actor and reason are required"
        )
    if handle.output_bundle.exists() or handle.output_bundle.is_symlink():
        raise RoleRuntimeError("ROLE_OUTPUT_EXISTS", str(handle.output_bundle))
    snapshot = snapshot_tmux_debug_role(
        handle, explicit_tmux_binary=explicit_tmux_binary
    )
    tmux_binary = _resolve_tmux_binary(explicit_tmux_binary)
    env = _minimal_environment(False)
    killed = _tmux(
        tmux_binary,
        handle.socket_name,
        ("kill-server",),
        env=env,
    )
    record = {
        "schema_version": TMUX_DEBUG_ABORT_SCHEMA,
        "attempt_id": handle.attempt_id,
        "aborted_at": _utc_now(),
        "actor": actor,
        "reason": reason,
        "pre_abort_snapshot_ref": (
            f"health-snapshots/{snapshot['sequence']:06d}.json"
        ),
        "pre_abort_state": snapshot["state"],
        "kill_action": "TMUX_PRIVATE_SERVER_KILL",
        "kill_exit_code": killed.returncode,
        "kill_stdout": killed.stdout,
        "kill_stderr": killed.stderr,
        "execution_mode": "INTERACTIVE_TMUX_DEBUG",
        "evidence_lane": "DEVELOPMENT_ONLY",
        "terminal_status": "ABORTED",
    }
    _write_bytes(
        handle.live_bundle / "tmux-debug-abort-receipt.json",
        canonical_json_bytes(record),
    )
    os.replace(handle.live_bundle, handle.output_bundle)
    return record
