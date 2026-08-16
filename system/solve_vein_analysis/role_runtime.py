"""One-shot Devin cognitive-role runner for solve-side calibration POCs.

This module is deliberately independent from the absorb-side pipeline and from
the Target Solver harness.  It is not a general production ModelRolePort.  Its
job is to make one fresh, explicitly profiled, append-once Devin CLI invocation
auditable.  A sandboxed profile and the absorb-source-compatible no-sandbox
profile remain distinct; neither is silently substituted for the other.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time
from typing import Any, Mapping, Sequence


DEVIN_MODEL_UID = "glm-5-2"
DEVIN_NORMALIZED_EFFORT = "high"
DEVIN_EFFORT_ENCODING = "model_uid"
RECEIPT_SCHEMA_VERSION = "solve-vein/devin-role-invocation-receipt/v1"
ATTEMPT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")


class RoleRuntimeError(RuntimeError):
    """Fail-closed runtime error with a stable machine code."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


@dataclass(frozen=True, slots=True)
class RoleInput:
    source_path: Path
    workspace_name: str


@dataclass(frozen=True, slots=True)
class DevinRoleSpec:
    attempt_id: str
    role: str
    role_asset_path: Path
    task_text: str
    inputs: tuple[RoleInput, ...]
    expected_output_name: str
    output_bundle: Path
    sandbox_requested: bool = True
    timeout_seconds: int = 900
    infrastructure_retry_index: int = 0
    expected_global_agents_sha256: str | None = None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _validate_workspace_name(name: str) -> None:
    candidate = Path(name)
    if (
        not name
        or candidate.is_absolute()
        or len(candidate.parts) != 1
        or name in {".", ".."}
        or name.startswith("gold")
        or name.startswith("expected")
    ):
        raise RoleRuntimeError(
            "ROLE_INPUT_NAME_FORBIDDEN",
            f"workspace input name is not a permitted flat non-gold name: {name!r}",
        )


def _validate_spec(spec: DevinRoleSpec) -> None:
    if not spec.attempt_id or not spec.role:
        raise RoleRuntimeError("ROLE_SPEC_ID_EMPTY", "attempt_id and role are required")
    if not ATTEMPT_ID_RE.fullmatch(spec.attempt_id):
        raise RoleRuntimeError(
            "ROLE_ATTEMPT_ID_INVALID", f"unsafe attempt_id: {spec.attempt_id!r}"
        )
    if spec.timeout_seconds <= 0:
        raise RoleRuntimeError("ROLE_TIMEOUT_INVALID", "timeout must be positive")
    if spec.infrastructure_retry_index not in {0, 1}:
        raise RoleRuntimeError(
            "ROLE_RETRY_INDEX_INVALID",
            "only the preregistered zero-or-one infrastructure retry is allowed",
        )
    if spec.expected_global_agents_sha256 is not None and not re.fullmatch(
        r"[0-9a-f]{64}", spec.expected_global_agents_sha256
    ):
        raise RoleRuntimeError(
            "ROLE_GLOBAL_AGENTS_HASH_INVALID",
            "expected global AGENTS hash must be lowercase SHA-256",
        )
    _validate_workspace_name(spec.expected_output_name)
    if spec.output_bundle.exists() or spec.output_bundle.is_symlink():
        raise RoleRuntimeError(
            "ROLE_OUTPUT_EXISTS", f"output bundle already exists: {spec.output_bundle}"
        )
    if not spec.role_asset_path.is_file() or spec.role_asset_path.is_symlink():
        raise RoleRuntimeError(
            "ROLE_ASSET_INVALID", f"role asset must be a regular file: {spec.role_asset_path}"
        )
    seen: set[str] = set()
    for role_input in spec.inputs:
        _validate_workspace_name(role_input.workspace_name)
        if role_input.workspace_name in seen:
            raise RoleRuntimeError(
                "ROLE_INPUT_NAME_DUPLICATE", role_input.workspace_name
            )
        seen.add(role_input.workspace_name)
        if not role_input.source_path.is_file() or role_input.source_path.is_symlink():
            raise RoleRuntimeError(
                "ROLE_INPUT_INVALID",
                f"input must be a regular file: {role_input.source_path}",
            )
    reserved = {
        "AGENTS.md",
        "TASK.md",
        "devin-config.json",
        "devin-export.json",
        "stdout.txt",
        "stderr.txt",
        "input-manifest.json",
        "catalog-snapshot.txt",
        "launch-receipt.json",
        "attempt-events.jsonl",
        "quarantine-receipt.json",
        "invocation-receipt.json",
    }
    collision = reserved & seen
    if collision:
        raise RoleRuntimeError(
            "ROLE_INPUT_RESERVED_NAME", f"reserved input names: {sorted(collision)}"
        )


def dedicated_devin_config() -> dict[str, Any]:
    """Return the no-sandbox dangerous profile for a dedicated role workspace.

    Path authority is stated by the frozen role AGENTS.md and audited from the
    resulting tool events.  Do not add a volume-wide Read deny here: doing so
    also denies the role's own workspace when that workspace is on the approved
    D-volume runtime root (POC-VMS-37).
    """

    return {
        "version": 1,
        "auto_update": False,
        "subagents_enabled": False,
        "read_config_from": {"cursor": False, "windsurf": False, "claude": False},
        "agent": {
            "model": DEVIN_MODEL_UID,
            "thinking": {"mode": "show_full_thinking"},
        },
        "permissions": {
            "allow": [
                "Read(**)",
                "Write(**)",
                "Exec(python3 *)",
                "Exec(shasum *)",
            ],
            "ask": [],
            "deny": [
                "Exec(devin *)",
                "Exec(codex *)",
                "Exec(curl *)",
                "Exec(wget *)",
                "Exec(ssh *)",
                "Exec(git *)",
                "Exec(rm -rf *)",
            ],
        },
        "shell": {"setup_complete": True},
        "show_path": False,
    }


def _minimal_environment(sandbox_requested: bool = True) -> dict[str, str]:
    permitted = ("HOME", "PATH", "SHELL", "TMPDIR", "LANG", "LC_ALL")
    env = {name: os.environ[name] for name in permitted if name in os.environ}
    env.update(
        {
            "DEVIN_MODEL": DEVIN_MODEL_UID,
            "DEVIN_PERMISSION_MODE": "dangerous",
            "DEVIN_SANDBOX": "true" if sandbox_requested else "false",
            "NO_COLOR": "1",
            "TERM": "dumb",
        }
    )
    return env


def inspect_global_control_surface(env: Mapping[str, str]) -> dict[str, Any]:
    """Observe the Devin user-level AGENTS file that remains in model context.

    The qualification runtime deliberately preserves the operator's real HOME
    because that is the profile under test.  The user-level rule file is thus
    part of the frozen control surface, not an invisible or answer-bearing
    input.  Only its sanitized locator, size, and hash enter public receipts.
    """

    home = env.get("HOME")
    if not home:
        return {
            "path": "~/.config/devin/AGENTS.md",
            "present": False,
            "size_bytes": None,
            "sha256": None,
        }
    path = Path(home) / ".config" / "devin" / "AGENTS.md"
    if path.is_symlink() or not path.is_file():
        return {
            "path": "~/.config/devin/AGENTS.md",
            "present": False,
            "size_bytes": None,
            "sha256": None,
        }
    return {
        "path": "~/.config/devin/AGENTS.md",
        "present": True,
        "size_bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def _file_manifest(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise RoleRuntimeError(
                "ROLE_WORKSPACE_SYMLINK", f"symlink is forbidden: {path}"
            )
        if path.is_file():
            result[path.relative_to(root).as_posix()] = sha256_file(path)
    return result


def _write_bytes(path: Path, payload: bytes, mode: int = 0o600) -> None:
    if path.exists() or path.is_symlink():
        raise RoleRuntimeError("ROLE_FILE_EXISTS", str(path))
    path.write_bytes(payload)
    path.chmod(mode)


def _append_event(path: Path, event: Mapping[str, Any]) -> None:
    """Durably append one canonical event without rewriting prior events."""

    payload = canonical_json_bytes(dict(event))
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
    descriptor = os.open(path, flags, 0o600)
    try:
        os.write(descriptor, payload)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _reject_symlink_ancestors(path: Path) -> None:
    """Reject a symlink at the nearest existing destination ancestor.

    The generic role runner cannot declare macOS system aliases such as
    ``/var -> /private/var`` untrusted.  A caller that owns a stricter storage
    root (VMS-41 uses the D-volume root) must additionally enforce containment
    from that trusted root downwards.
    """

    current = path.absolute()
    while not current.exists() and current.parent != current:
        current = current.parent
    if current.is_symlink():
        raise RoleRuntimeError(
            "ROLE_OUTPUT_ANCESTOR_SYMLINK", f"symlink ancestor: {current}"
        )


def _copy_regular_file(source: Path, destination: Path) -> None:
    if destination.exists() or destination.is_symlink():
        raise RoleRuntimeError("ROLE_FILE_EXISTS", str(destination))
    shutil.copyfile(source, destination, follow_symlinks=False)
    destination.chmod(0o600)


def prepare_workspace(spec: DevinRoleSpec, workspace: Path) -> dict[str, Any]:
    """Materialize only the role's permitted view into an empty workspace."""

    _validate_spec(spec)
    workspace.mkdir(mode=0o700, parents=False, exist_ok=False)
    _copy_regular_file(spec.role_asset_path, workspace / "AGENTS.md")
    _write_bytes(workspace / "TASK.md", spec.task_text.encode("utf-8"))
    _write_bytes(
        workspace / "devin-config.json", canonical_json_bytes(dedicated_devin_config())
    )
    input_rows: list[dict[str, str]] = []
    for role_input in spec.inputs:
        target = workspace / role_input.workspace_name
        _copy_regular_file(role_input.source_path, target)
        input_rows.append(
            {
                "workspace_name": role_input.workspace_name,
                "sha256": sha256_file(target),
            }
        )
    manifest = {
        "schema_version": "solve-vein/role-input-manifest/v1",
        "attempt_id": spec.attempt_id,
        "role": spec.role,
        "role_asset_sha256": sha256_file(workspace / "AGENTS.md"),
        "task_sha256": sha256_file(workspace / "TASK.md"),
        "config_sha256": sha256_file(workspace / "devin-config.json"),
        "inputs": sorted(input_rows, key=lambda row: row["workspace_name"]),
        "expected_output_name": spec.expected_output_name,
        "forbidden_name_prefixes": ["gold", "expected"],
    }
    _write_bytes(workspace / "input-manifest.json", canonical_json_bytes(manifest))
    return manifest


def resolve_devin_binary(explicit_binary: Path | None = None) -> Path:
    candidate = str(explicit_binary) if explicit_binary else shutil.which("devin")
    if not candidate:
        raise RoleRuntimeError("DEVIN_BINARY_MISSING", "devin not found on PATH")
    resolved = Path(candidate).resolve(strict=True)
    if not resolved.is_file():
        raise RoleRuntimeError("DEVIN_BINARY_INVALID", str(resolved))
    return resolved


def _run_preflight_command(
    argv: Sequence[str], env: Mapping[str, str], timeout_seconds: int = 60
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(argv),
        check=False,
        capture_output=True,
        text=True,
        env=dict(env),
        timeout=timeout_seconds,
    )


def inspect_export(export_path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "json_valid": False,
        "observed_generation_model_uids": [],
        "observed_agent_model_names": [],
        "session_ids": [],
        "tool_event_count": 0,
        "step_count": 0,
    }
    if not export_path.is_file() or export_path.is_symlink():
        return result
    try:
        value = json.loads(export_path.read_text())
    except (UnicodeDecodeError, json.JSONDecodeError):
        return result
    result["json_valid"] = True
    model_uids: set[str] = set()
    model_names: set[str] = set()
    session_ids: set[str] = set()
    tool_events = 0
    if isinstance(value, dict) and isinstance(value.get("steps"), list):
        # ATIF-v1.7 represents each step with ``step_id`` and ``source``.  It
        # does not use the older ``step_type``/``event_type`` keys.
        step_count = len(value["steps"])
        has_canonical_steps = True
    else:
        step_count = 0
        has_canonical_steps = False

    def visit(node: Any, *, inside_tool_collection: bool = False) -> None:
        nonlocal tool_events, step_count
        if isinstance(node, dict):
            if not has_canonical_steps and (
                "step_type" in node
                or "event_type" in node
                or ("step_id" in node and "source" in node)
            ):
                step_count += 1
            if not inside_tool_collection and (
                isinstance(node.get("tool_name"), str)
                or isinstance(node.get("function_name"), str)
            ):
                # Some older exports encode one call as a standalone object
                # instead of placing it in a tool_calls/tool_events list.
                tool_events += 1
            for key, item in node.items():
                lowered = key.lower()
                if lowered == "generation_model" and isinstance(item, str) and item:
                    model_uids.add(item)
                elif lowered == "model_name" and isinstance(item, str) and item:
                    model_names.add(item)
                elif lowered in {"session_id", "conversation_id", "thread_id"}:
                    if isinstance(item, str) and item:
                        session_ids.add(item)
                if lowered in {"tool_calls", "tool_events"}:
                    if isinstance(item, list):
                        tool_events += len(item)
                        visit(item, inside_tool_collection=True)
                    elif isinstance(item, dict):
                        tool_events += 1
                        visit(item, inside_tool_collection=True)
                    else:
                        visit(item, inside_tool_collection=True)
                else:
                    visit(item, inside_tool_collection=inside_tool_collection)
        elif isinstance(node, list):
            for item in node:
                visit(item, inside_tool_collection=inside_tool_collection)

    visit(value)
    result.update(
        {
            "observed_generation_model_uids": sorted(model_uids),
            "observed_agent_model_names": sorted(model_names),
            "session_ids": sorted(session_ids),
            "tool_event_count": tool_events,
            "step_count": step_count,
        }
    )
    return result


def run_devin_role(
    spec: DevinRoleSpec, *, explicit_binary: Path | None = None
) -> dict[str, Any]:
    """Run exactly one fresh Devin role attempt and seal its complete workspace.

    This function never retries.  A non-zero exit or invalid output is recorded in
    the receipt rather than silently converted into a second scientific attempt.
    """

    _validate_spec(spec)
    target_parent = spec.output_bundle.parent
    _reject_symlink_ancestors(target_parent)
    target_parent.mkdir(parents=True, exist_ok=True)
    _reject_symlink_ancestors(target_parent)
    workspace = target_parent / (
        f".{spec.output_bundle.name}.partial-{spec.attempt_id}"
    )
    if workspace.exists() or workspace.is_symlink():
        raise RoleRuntimeError(
            "ROLE_RECONCILIATION_REQUIRED",
            f"partial attempt already exists and must not be relaunched: {workspace}",
        )
    binary = resolve_devin_binary(explicit_binary)
    env = _minimal_environment(spec.sandbox_requested)
    global_control_surface = inspect_global_control_surface(env)
    if spec.expected_global_agents_sha256 is not None:
        if (
            global_control_surface["present"] is not True
            or global_control_surface["sha256"]
            != spec.expected_global_agents_sha256
        ):
            raise RoleRuntimeError(
                "ROLE_GLOBAL_AGENTS_DRIFT",
                "the visible user-level Devin AGENTS file is absent or changed",
            )
    version = _run_preflight_command((str(binary), "--version"), env)
    if version.returncode != 0:
        raise RoleRuntimeError("DEVIN_VERSION_FAILED", version.stderr.strip())
    catalog = _run_preflight_command((str(binary), "models", "list"), env)
    if catalog.returncode != 0:
        raise RoleRuntimeError("DEVIN_CATALOG_FAILED", catalog.stderr.strip())
    catalog_text = catalog.stdout
    if DEVIN_MODEL_UID not in catalog_text or "GLM-5.2 High" not in catalog_text:
        raise RoleRuntimeError(
            "DEVIN_MODEL_CATALOG_MISMATCH",
            f"catalog does not expose {DEVIN_MODEL_UID!r} as GLM-5.2 High",
        )

    started_at = ""
    ended_at = ""
    start_monotonic = 0.0
    exit_code: int | None = None
    timed_out = False
    stdout = ""
    stderr = ""
    input_manifest = prepare_workspace(spec, workspace)
    _write_bytes(workspace / "catalog-snapshot.txt", catalog_text.encode("utf-8"))
    before_manifest = _file_manifest(workspace)
    export_path = workspace / "devin-export.json"
    argv_parts = [
        str(binary),
        "--config",
        str(workspace / "devin-config.json"),
        "--permission-mode",
        "dangerous",
    ]
    if spec.sandbox_requested:
        argv_parts.append("--sandbox")
    argv_parts.extend(
        [
            "--model",
            DEVIN_MODEL_UID,
            "--export",
            str(export_path),
            "--respect-workspace-trust",
            "false",
            "--prompt-file",
            str(workspace / "TASK.md"),
            "-p",
        ]
    )
    argv = tuple(argv_parts)
    sanitized_argv = [
        "devin",
        "--config",
        "devin-config.json",
        "--permission-mode",
        "dangerous",
    ]
    if spec.sandbox_requested:
        sanitized_argv.append("--sandbox")
    sanitized_argv.extend(
        [
            "--model",
            DEVIN_MODEL_UID,
            "--export",
            "devin-export.json",
            "--respect-workspace-trust",
            "false",
            "--prompt-file",
            "TASK.md",
            "-p",
        ]
    )
    launch_receipt = {
        "schema_version": "solve-vein/devin-role-launch-receipt/v1",
        "attempt_id": spec.attempt_id,
        "role": spec.role,
        "prepared_at": _utc_now(),
        "input_manifest_sha256": sha256_json(input_manifest),
        "resolved_binary_sha256": sha256_file(binary),
        "requested_model_uid": DEVIN_MODEL_UID,
        "normalized_effort": DEVIN_NORMALIZED_EFFORT,
        "sandbox_requested": spec.sandbox_requested,
        "permission_mode": "dangerous",
        "sanitized_argv": sanitized_argv,
        "full_argv_sha256": sha256_json(list(argv)),
        "scientific_retry_index": spec.infrastructure_retry_index,
        "global_control_surface": global_control_surface,
        "launch_state": "PREPARED_NOT_YET_STARTED",
    }
    _write_bytes(
        workspace / "launch-receipt.json", canonical_json_bytes(launch_receipt)
    )
    event_log = workspace / "attempt-events.jsonl"
    _append_event(
        event_log,
        {
            "schema_version": "solve-vein/role-attempt-event/v1",
            "attempt_id": spec.attempt_id,
            "event": "PREPARED",
            "observed_at": launch_receipt["prepared_at"],
            "launch_receipt_sha256": sha256_file(
                workspace / "launch-receipt.json"
            ),
        },
    )
    started_at = _utc_now()
    start_monotonic = time.monotonic()
    try:
        process = subprocess.Popen(
            argv,
            cwd=workspace,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except OSError as exc:
        _append_event(
            event_log,
            {
                "schema_version": "solve-vein/role-attempt-event/v1",
                "attempt_id": spec.attempt_id,
                "event": "LOCAL_PROCESS_START_FAILED",
                "observed_at": _utc_now(),
                "error_type": type(exc).__name__,
            },
        )
        _write_bytes(
            workspace / "quarantine-receipt.json",
            canonical_json_bytes(
                {
                    "schema_version": "solve-vein/role-quarantine-receipt/v1",
                    "attempt_id": spec.attempt_id,
                    "reason": "LOCAL_PROCESS_START_FAILED",
                    "retry_authorized": False,
                    "partial_bundle": workspace.name,
                }
            ),
        )
        raise RoleRuntimeError("DEVIN_PROCESS_START_FAILED", str(exc)) from exc
    _append_event(
        event_log,
        {
            "schema_version": "solve-vein/role-attempt-event/v1",
            "attempt_id": spec.attempt_id,
            "event": "LOCAL_PROCESS_STARTED",
            "observed_at": _utc_now(),
            "pid": process.pid,
        },
    )
    try:
        stdout, stderr = process.communicate(timeout=spec.timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        process.terminate()
        try:
            stdout, stderr = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
    exit_code = process.returncode
    ended_at = _utc_now()
    _append_event(
        event_log,
        {
            "schema_version": "solve-vein/role-attempt-event/v1",
            "attempt_id": spec.attempt_id,
            "event": "LOCAL_PROCESS_EXITED",
            "observed_at": ended_at,
            "exit_code": exit_code,
            "timed_out": timed_out,
        },
    )
    _write_bytes(workspace / "stdout.txt", stdout.encode("utf-8"))
    _write_bytes(workspace / "stderr.txt", stderr.encode("utf-8"))
    after_manifest = _file_manifest(workspace)
    output_path = workspace / spec.expected_output_name
    done_path = workspace / "DONE.md"
    output_sha256 = sha256_file(output_path) if output_path.is_file() else None
    done_marker_content_valid = False
    if done_path.is_file() and output_sha256 is not None:
        try:
            done_marker_content_valid = done_path.read_text().strip() == (
                f"{spec.expected_output_name} SHA256={output_sha256}"
            )
        except UnicodeDecodeError:
            done_marker_content_valid = False
    export_observation = inspect_export(export_path)
    observed_uids = export_observation["observed_generation_model_uids"]
    model_observability = (
        "MATCH"
        if observed_uids == [DEVIN_MODEL_UID]
        else "UNOBSERVABLE"
        if not observed_uids
        else "MISMATCH"
    )
    request_accepted_observability = (
        "OBSERVED_POSTHOC"
        if export_observation["json_valid"]
        and export_observation["session_ids"]
        else "UNOBSERVABLE"
    )
    generation_started_observability = (
        "OBSERVED_POSTHOC" if observed_uids else "UNOBSERVABLE"
    )
    receipt = {
            "schema_version": RECEIPT_SCHEMA_VERSION,
            "attempt_id": spec.attempt_id,
            "role": spec.role,
            "input_manifest_sha256": sha256_json(input_manifest),
            "asset_sha256": input_manifest["role_asset_sha256"],
            "requested_model_uid": DEVIN_MODEL_UID,
            "normalized_effort": DEVIN_NORMALIZED_EFFORT,
            "effort_encoding": DEVIN_EFFORT_ENCODING,
            "model_catalog_snapshot_ref": "catalog-snapshot.txt",
            "model_catalog_snapshot_sha256": sha256_file(
                workspace / "catalog-snapshot.txt"
            ),
            "resolved_binary_path": str(binary),
            "resolved_binary_sha256": sha256_file(binary),
            "cli_version": version.stdout.strip() or version.stderr.strip(),
            "sanitized_argv": sanitized_argv,
            "full_argv_sha256": launch_receipt["full_argv_sha256"],
            "config_sha256": input_manifest["config_sha256"],
            "sandbox_requested": spec.sandbox_requested,
            "permission_mode": "dangerous",
            "global_control_surface": global_control_surface,
            "launch_receipt_ref": "launch-receipt.json",
            "launch_receipt_sha256": sha256_file(
                workspace / "launch-receipt.json"
            ),
            "attempt_event_log_ref": "attempt-events.jsonl",
            "attempt_event_log_sha256": sha256_file(event_log),
            "local_process_started": True,
            "request_accepted_observability": request_accepted_observability,
            "generation_started_observability": generation_started_observability,
            "workspace_manifest_before_sha256": sha256_json(before_manifest),
            "workspace_manifest_after_sha256": sha256_json(after_manifest),
            "started_at": started_at,
            "ended_at": ended_at,
            "wallclock_seconds": round(time.monotonic() - start_monotonic, 6),
            "exit_code": exit_code,
            "timed_out": timed_out,
            "stdout_sha256": sha256_file(workspace / "stdout.txt"),
            "stderr_sha256": sha256_file(workspace / "stderr.txt"),
            "export_ref": "devin-export.json" if export_path.is_file() else None,
            "export_sha256": sha256_file(export_path) if export_path.is_file() else None,
            "export_observation": export_observation,
            "model_observability_verdict": model_observability,
            "output_ref": spec.expected_output_name if output_path.is_file() else None,
            "output_sha256": output_sha256,
            "done_marker_ref": "DONE.md" if done_path.is_file() else None,
            "done_marker_sha256": sha256_file(done_path) if done_path.is_file() else None,
            "done_marker_content_valid": done_marker_content_valid,
            "retry_count": spec.infrastructure_retry_index,
            "protocol_deviations": [],
    }
    _write_bytes(
        workspace / "invocation-receipt.json", canonical_json_bytes(receipt)
    )
    os.replace(workspace, spec.output_bundle)
    return receipt
