"""Run the sealed one-shot POC-VMS-41 Event Extractor qualification pack.

The CLI entry is intentionally strict: it consumes one frozen manifest, uses
the approved D-volume result root, launches each preregistered attempt at most
once, delays hidden-gold grading until every model call has terminated, and
seals both successful and negative scientific outcomes.  It never connects a
database, Redis, Seven, or the Target Solver harness.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
from typing import Any, Mapping


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from system.solve_vein_analysis.event_extraction_qualification import (
    EventExtractionAcceptableSetPack,
    MechanicalVerdict,
    OverallQualificationStatus,
    evaluate_candidate_json,
)
from system.solve_vein_analysis.role_runtime import (
    DEVIN_MODEL_UID,
    DevinRoleSpec,
    RoleInput,
    RoleRuntimeError,
    canonical_json_bytes,
    run_devin_role,
    sha256_file,
)


POC_ID = "POC-VMS-41"
RUN_ID = "poc-vms-41-event-extractor-qualification-20260814"
HERE = Path(__file__).resolve().parent
DEFAULT_FREEZE = HERE / "live_fixtures" / "poc_vms_41.freeze.json"
APPROVED_VOLUME = Path("/data")
APPROVED_DATA_ROOT = Path("/data/master-mind-solve-vein-data")
APPROVED_RESULTS_ROOT = APPROVED_DATA_ROOT / "poc-results"
DEFAULT_FINAL_ROOT = APPROVED_RESULTS_ROOT / RUN_ID
DEFAULT_PARTIAL_ROOT = APPROVED_RESULTS_ROOT / f".{RUN_ID}.partial"
CASE_DIRS = {
    "V41-SYN-FALSE-MERGE": "syn_false_merge",
    "V41-SYN-TRUE-MERGE": "syn_true_merge",
    "V41-REAL-SPIRAL": "real_spiral",
    "V41-REAL-BATTERY": "real_battery",
}
EXPECTED_CASE_IDS = tuple(CASE_DIRS)
ALLOWED_READ_NAMES = {
    "AGENTS.md",
    "TASK.md",
    "problem.md",
    "raw_solver_trajectory.txt",
    "reasoning-trajectory-v1.md",
    "input-manifest.json",
    "devin-config.json",
}
ALLOWED_WRITE_NAMES = {"reasoning-trajectory.json", "DONE.md"}
RUNNER_OWNED_NAMES = {
    "AGENTS.md",
    "TASK.md",
    "problem.md",
    "raw_solver_trajectory.txt",
    "reasoning-trajectory-v1.md",
    "input-manifest.json",
    "devin-config.json",
    "catalog-snapshot.txt",
    "launch-receipt.json",
    "attempt-events.jsonl",
    "stdout.txt",
    "stderr.txt",
    "devin-export.json",
    "invocation-receipt.json",
    "reasoning-trajectory.json",
    "DONE.md",
}
FORBIDDEN_EXEC_TOKENS = (
    "curl ",
    "wget ",
    "ssh ",
    "git ",
    "devin ",
    "codex ",
    "rm -rf",
    "nc ",
    "netcat ",
)
ABSOLUTE_PATH_RE = re.compile(r"/(?:[^\s'\";|&<>]+)")


class QualificationRunError(RuntimeError):
    """Fail-closed VMS-41 orchestration error."""


def qualification_test_source_files() -> tuple[Path, ...]:
    """Return the deterministic source set covered by the pre-live test gate."""

    package_files = list(
        (REPOSITORY_ROOT / "system/solve_vein_analysis").glob("*.py")
    )
    test_root = REPOSITORY_ROOT / "system/tests/solve_vein_analysis"
    test_files = list(test_root.glob("test_*.py"))
    support_names = (
        "build_vms41_qualification_pack.py",
        "freeze_event_extractor_qualification.py",
        "run_event_extractor_qualification.py",
        "verify_event_extractor_qualification.py",
    )
    support_files = [test_root / name for name in support_names]
    files = sorted({path for path in package_files + test_files + support_files})
    missing = [path for path in files if not path.is_file() or path.is_symlink()]
    if missing:
        raise QualificationRunError(
            f"qualification test source is absent or unsafe: {missing}"
        )
    return tuple(files)


def test_source_tree_sha256() -> str:
    payload = "".join(
        f"{sha256_file(path)}  {path.relative_to(REPOSITORY_ROOT).as_posix()}\n"
        for path in qualification_test_source_files()
    ).encode("utf-8")
    return _sha256_bytes(payload)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _write_once(path: Path, payload: bytes) -> None:
    if path.exists() or path.is_symlink():
        raise QualificationRunError(f"append-once destination exists: {path}")
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(descriptor, payload)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write_json_once(path: Path, value: Any) -> None:
    _write_once(path, canonical_json_bytes(value))


def _append_jsonl(path: Path, value: Mapping[str, Any]) -> None:
    payload = canonical_json_bytes(dict(value))
    descriptor = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o600)
    try:
        os.write(descriptor, payload)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _load_object(path: Path, label: str) -> dict[str, Any]:
    if not path.is_file() or path.is_symlink():
        raise QualificationRunError(f"{label} is absent, unsafe, or not a file: {path}")
    try:
        value = json.loads(path.read_text(), parse_constant=_reject_nonfinite)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise QualificationRunError(f"{label} is invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise QualificationRunError(f"{label} must be an object")
    return value


def _reject_nonfinite(value: str) -> Any:
    raise QualificationRunError(f"non-finite JSON number: {value}")


def _exact_keys(value: Mapping[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        raise QualificationRunError(
            f"{label} keys mismatch: missing={sorted(expected-actual)}, "
            f"unknown={sorted(actual-expected)}"
        )


def validate_freeze_manifest(path: Path) -> dict[str, Any]:
    manifest = _load_object(path, "freeze manifest")
    _exact_keys(
        manifest,
        {
            "schema_version",
            "poc_id",
            "run_id",
            "protocol",
            "acceptable_set_pack",
            "frozen_files",
            "case_specs",
            "runtime_profile",
            "resource_contract",
            "attempt_ids",
            "output_root",
            "test_gate",
            "side_effect_authorization",
        },
        "freeze manifest",
    )
    if manifest["schema_version"] != "solve-vein/vms41-preexecution-freeze/v1":
        raise QualificationRunError("freeze schema mismatch")
    if manifest["poc_id"] != POC_ID or manifest["run_id"] != RUN_ID:
        raise QualificationRunError("freeze POC/run identity mismatch")
    if manifest["output_root"] != str(DEFAULT_FINAL_ROOT):
        raise QualificationRunError("freeze output root mismatch")
    runtime_profile = manifest["runtime_profile"]
    if not isinstance(runtime_profile, dict):
        raise QualificationRunError("runtime_profile must be an object")
    _exact_keys(
        runtime_profile,
        {
            "carrier",
            "role",
            "model_uid",
            "normalized_effort",
            "effort_encoding",
            "orchestration_mode",
            "fresh_session",
            "resume_allowed",
            "sandbox_requested",
            "permission_mode",
            "asset_release_path",
            "resolved_binary_path",
            "resolved_binary_sha256",
            "cli_version",
            "catalog_snapshot_sha256",
            "global_agents_path",
            "global_agents_sha256",
            "global_agents_size_bytes",
        },
        "runtime_profile",
    )
    if runtime_profile["carrier"] != "devin_cli":
        raise QualificationRunError("freeze carrier mismatch")
    if runtime_profile["role"] != "REASONING_EVENT_EXTRACTOR":
        raise QualificationRunError("freeze role mismatch")
    if runtime_profile["model_uid"] != DEVIN_MODEL_UID:
        raise QualificationRunError("freeze model UID mismatch")
    if runtime_profile["normalized_effort"] != "high":
        raise QualificationRunError("freeze normalized effort mismatch")
    if runtime_profile["effort_encoding"] != "model_uid":
        raise QualificationRunError("freeze effort encoding mismatch")
    if runtime_profile["orchestration_mode"] != "fresh_single_agent_one_shot":
        raise QualificationRunError("freeze orchestration mode mismatch")
    if runtime_profile["fresh_session"] is not True:
        raise QualificationRunError("VMS-41 requires a fresh session")
    if runtime_profile["resume_allowed"] is not False:
        raise QualificationRunError("VMS-41 forbids resume")
    if runtime_profile["sandbox_requested"] is not False:
        raise QualificationRunError("VMS-41 requires the frozen no-sandbox profile")
    if runtime_profile["permission_mode"] != "dangerous":
        raise QualificationRunError("VMS-41 permission profile mismatch")
    for hash_field in (
        "resolved_binary_sha256",
        "catalog_snapshot_sha256",
        "global_agents_sha256",
    ):
        if not re.fullmatch(r"[0-9a-f]{64}", str(runtime_profile[hash_field])):
            raise QualificationRunError(f"invalid runtime hash: {hash_field}")
    if (
        not isinstance(runtime_profile["global_agents_size_bytes"], int)
        or isinstance(runtime_profile["global_agents_size_bytes"], bool)
        or runtime_profile["global_agents_size_bytes"] <= 0
    ):
        raise QualificationRunError("global AGENTS size must be positive")
    if manifest["resource_contract"] != {
        "case_attempts": 1,
        "concurrency": 1,
        "infrastructure_retries": 0,
        "scientific_retries": 0,
        "timeout_seconds_per_case": 900,
    }:
        raise QualificationRunError("resource contract is not the preregistered one")
    if manifest["side_effect_authorization"] != {
        "devin_role_attempts_authorized": 4,
        "database_connections": 0,
        "network_calls_by_candidate": 0,
        "redis_connections": 0,
        "solver_calls": 0,
        "subagent_calls": 0,
    }:
        raise QualificationRunError("side-effect contract mismatch")
    attempt_ids = manifest["attempt_ids"]
    if not isinstance(attempt_ids, dict) or set(attempt_ids) != set(EXPECTED_CASE_IDS):
        raise QualificationRunError("attempt ID map does not cover the frozen cases")
    if len(set(attempt_ids.values())) != len(EXPECTED_CASE_IDS):
        raise QualificationRunError("attempt IDs must be unique")
    case_specs = manifest["case_specs"]
    if not isinstance(case_specs, list) or tuple(
        item.get("case_id") for item in case_specs if isinstance(item, dict)
    ) != EXPECTED_CASE_IDS:
        raise QualificationRunError("case spec order mismatch")
    frozen_files = manifest["frozen_files"]
    if not isinstance(frozen_files, list) or not frozen_files:
        raise QualificationRunError("frozen file inventory is empty")
    observed_paths: set[str] = set()
    for index, row in enumerate(frozen_files):
        if not isinstance(row, dict) or set(row) != {"path", "sha256"}:
            raise QualificationRunError(f"frozen_files[{index}] is malformed")
        relative = row["path"]
        if not isinstance(relative, str) or relative in observed_paths:
            raise QualificationRunError(f"duplicate/invalid frozen path: {relative!r}")
        observed_paths.add(relative)
        target = REPOSITORY_ROOT / relative
        if target.is_symlink() or not target.is_file():
            raise QualificationRunError(f"frozen file absent or unsafe: {relative}")
        if sha256_file(target) != row["sha256"]:
            raise QualificationRunError(f"frozen file hash drift: {relative}")
    for binding_name in ("protocol", "acceptable_set_pack"):
        binding = manifest[binding_name]
        if not isinstance(binding, dict) or set(binding) != {"path", "sha256"}:
            raise QualificationRunError(f"{binding_name} binding is malformed")
        target = REPOSITORY_ROOT / binding["path"]
        if target.is_symlink() or not target.is_file() or sha256_file(target) != binding["sha256"]:
            raise QualificationRunError(f"{binding_name} binding drift")
    acceptable_pack = EventExtractionAcceptableSetPack.from_json_text(
        (REPOSITORY_ROOT / manifest["acceptable_set_pack"]["path"]).read_text()
    )
    for index, row in enumerate(case_specs):
        if not isinstance(row, dict):
            raise QualificationRunError(f"case_specs[{index}] must be an object")
        _exact_keys(
            row,
            {
                "case_id",
                "fixture_dir",
                "acceptable_set_id",
                "problem_path",
                "problem_sha256",
                "raw_path",
                "raw_sha256",
                "source_receipt_path",
                "source_receipt_sha256",
            },
            f"case_specs[{index}]",
        )
        acceptable = acceptable_pack.case_by_id(row["case_id"])
        if row["acceptable_set_id"] != acceptable.acceptable_set_id:
            raise QualificationRunError(f"acceptable-set identity drift: {row['case_id']}")
        if row["fixture_dir"] != CASE_DIRS[row["case_id"]]:
            raise QualificationRunError(f"fixture directory drift: {row['case_id']}")
        for path_field, hash_field in (
            ("problem_path", "problem_sha256"),
            ("raw_path", "raw_sha256"),
        ):
            target = REPOSITORY_ROOT / row[path_field]
            if (
                target.is_symlink()
                or not target.is_file()
                or sha256_file(target) != row[hash_field]
            ):
                raise QualificationRunError(
                    f"case file binding drift: {row['case_id']}:{path_field}"
                )
        if row["raw_sha256"] != acceptable.source.source_artifact_sha256:
            raise QualificationRunError(f"case raw/gold hash drift: {row['case_id']}")
        receipt_path = row["source_receipt_path"]
        receipt_hash = row["source_receipt_sha256"]
        if (receipt_path is None) != (receipt_hash is None):
            raise QualificationRunError(f"source receipt pair mismatch: {row['case_id']}")
        if receipt_path is not None:
            target = REPOSITORY_ROOT / receipt_path
            if (
                target.is_symlink()
                or not target.is_file()
                or sha256_file(target) != receipt_hash
            ):
                raise QualificationRunError(f"source receipt drift: {row['case_id']}")
    binary = Path(runtime_profile["resolved_binary_path"]).resolve(strict=True)
    if str(binary) != runtime_profile["resolved_binary_path"]:
        raise QualificationRunError("resolved Devin binary path is not canonical")
    if sha256_file(binary) != runtime_profile["resolved_binary_sha256"]:
        raise QualificationRunError("resolved Devin binary hash drift")
    home = os.environ.get("HOME")
    global_agents = (
        Path(home) / ".config" / "devin" / "AGENTS.md" if home else None
    )
    if (
        global_agents is None
        or global_agents.is_symlink()
        or not global_agents.is_file()
        or sha256_file(global_agents) != runtime_profile["global_agents_sha256"]
        or global_agents.stat().st_size
        != runtime_profile["global_agents_size_bytes"]
    ):
        raise QualificationRunError("user-level Devin AGENTS control surface drift")
    if runtime_profile["global_agents_path"] != "~/.config/devin/AGENTS.md":
        raise QualificationRunError("global AGENTS sanitized locator mismatch")
    test_gate = manifest["test_gate"]
    if not isinstance(test_gate, dict):
        raise QualificationRunError("test_gate must be an object")
    _exact_keys(
        test_gate,
        {
            "runner",
            "python_executable",
            "python_executable_sha256",
            "python_version",
            "test_ids",
            "tests_run",
            "failures",
            "errors",
            "skipped",
            "successful",
            "test_source_tree_sha256",
            "protected_absorb_baseline_path",
            "protected_absorb_baseline_sha256",
            "protected_absorb_file_count",
            "verdict",
        },
        "test_gate",
    )
    test_ids = test_gate["test_ids"]
    if (
        test_gate["runner"] != "python_unittest_in_process"
        or not isinstance(test_ids, list)
        or not test_ids
        or any(not isinstance(item, str) or not item for item in test_ids)
        or len(test_ids) != len(set(test_ids))
        or test_gate["tests_run"] != len(test_ids)
        or test_gate["failures"] != 0
        or test_gate["errors"] != 0
        or test_gate["skipped"] != 0
        or test_gate["successful"] is not True
        or test_gate["verdict"] != "PASS"
    ):
        raise QualificationRunError("controlled test gate did not PASS exactly")
    if not re.fullmatch(r"[0-9a-f]{64}", str(test_gate["test_source_tree_sha256"])):
        raise QualificationRunError("controlled test source tree hash is invalid")
    if test_gate["test_source_tree_sha256"] != test_source_tree_sha256():
        raise QualificationRunError("controlled test source tree drift")
    python_binary = Path(test_gate["python_executable"]).resolve(strict=True)
    if (
        str(python_binary) != test_gate["python_executable"]
        or sha256_file(python_binary) != test_gate["python_executable_sha256"]
    ):
        raise QualificationRunError("controlled Python identity drift")
    baseline_path = REPOSITORY_ROOT / test_gate["protected_absorb_baseline_path"]
    if (
        baseline_path.is_symlink()
        or not baseline_path.is_file()
        or sha256_file(baseline_path)
        != test_gate["protected_absorb_baseline_sha256"]
        or test_gate["protected_absorb_file_count"] != 161
    ):
        raise QualificationRunError("protected absorb baseline binding drift")
    return manifest


def render_task(template_text: str, values: Mapping[str, str]) -> str:
    rendered = template_text
    expected_tokens = {f"{{{{{name}}}}}" for name in values}
    observed_tokens = set(re.findall(r"\{\{[A-Z0-9_]+\}\}", template_text))
    if observed_tokens != expected_tokens:
        raise QualificationRunError(
            f"task template placeholders mismatch: expected={sorted(expected_tokens)}, "
            f"observed={sorted(observed_tokens)}"
        )
    for name, value in values.items():
        token = f"{{{{{name}}}}}"
        if rendered.count(token) != 1:
            raise QualificationRunError(f"task token must occur exactly once: {token}")
        rendered = rendered.replace(token, value)
    if re.search(r"\{\{[A-Z0-9_]+\}\}", rendered):
        raise QualificationRunError("unrendered task token remains")
    return rendered


def audit_tool_boundary(
    export_path: Path,
    attempt_bundle: Path,
    attempt_id: str,
    *,
    historical_attempt_bundle: Path | None = None,
) -> dict[str, Any]:
    errors: list[str] = []
    calls: list[dict[str, Any]] = []
    if not export_path.is_file() or export_path.is_symlink():
        return {
            "schema_version": "solve-vein/vms41-tool-boundary-audit/v1",
            "attempt_id": attempt_id,
            "tool_call_count": 0,
            "verdict": "UNOBSERVABLE",
            "errors": ["export is absent or unsafe"],
            "calls": [],
        }
    try:
        document = json.loads(export_path.read_text())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return {
            "schema_version": "solve-vein/vms41-tool-boundary-audit/v1",
            "attempt_id": attempt_id,
            "tool_call_count": 0,
            "verdict": "UNOBSERVABLE",
            "errors": [f"invalid export: {exc}"],
            "calls": [],
        }
    steps = document.get("steps") if isinstance(document, dict) else None
    if not isinstance(steps, list):
        errors.append("ATIF steps are absent")
        steps = []
    source_bundle = historical_attempt_bundle or attempt_bundle
    historical_workspace = source_bundle.parent / (
        f".{source_bundle.name}.partial-{attempt_id}"
    )
    permitted_roots = (
        attempt_bundle.resolve(strict=False),
        historical_workspace.resolve(strict=False),
    )

    def permitted_path(raw: str, allowed_names: set[str]) -> bool:
        path = Path(raw)
        if path.is_absolute():
            absolute = path.resolve(strict=False)
            for root in permitted_roots:
                try:
                    relative = absolute.relative_to(root)
                except ValueError:
                    continue
                return len(relative.parts) == 1 and relative.name in allowed_names
            return False
        return len(path.parts) == 1 and path.name in allowed_names

    for step_index, step in enumerate(steps):
        if not isinstance(step, dict):
            continue
        tool_calls = step.get("tool_calls", [])
        if not isinstance(tool_calls, list):
            errors.append(f"steps[{step_index}].tool_calls is not a list")
            continue
        for call_index, call in enumerate(tool_calls):
            if not isinstance(call, dict):
                errors.append(f"tool call {step_index}:{call_index} is not an object")
                continue
            name = call.get("function_name")
            arguments = call.get("arguments")
            row = {
                "step_index": step_index,
                "call_index": call_index,
                "function_name": name,
                "status": "PASS",
            }
            if not isinstance(arguments, dict) or name not in {"read", "write", "exec"}:
                row["status"] = "FAIL"
                errors.append(f"unsupported tool call {step_index}:{call_index}:{name!r}")
                calls.append(row)
                continue
            if name in {"read", "write"}:
                raw_path = arguments.get("file_path")
                names = ALLOWED_READ_NAMES if name == "read" else ALLOWED_WRITE_NAMES
                if not isinstance(raw_path, str) or not permitted_path(raw_path, names):
                    row["status"] = "FAIL"
                    errors.append(f"forbidden {name} path at {step_index}:{call_index}")
            else:
                command = arguments.get("command")
                if not isinstance(command, str):
                    row["status"] = "FAIL"
                    errors.append(f"exec command missing at {step_index}:{call_index}")
                else:
                    lowered = command.lower()
                    if any(token in lowered for token in FORBIDDEN_EXEC_TOKENS):
                        row["status"] = "FAIL"
                        errors.append(f"forbidden exec token at {step_index}:{call_index}")
                    for raw_path in ABSOLUTE_PATH_RE.findall(command):
                        absolute = Path(raw_path).resolve(strict=False)
                        if not any(
                            absolute == root or root in absolute.parents
                            for root in permitted_roots
                        ):
                            row["status"] = "FAIL"
                            errors.append(
                                f"external absolute path in exec at {step_index}:{call_index}"
                            )
                            break
            calls.append(row)
    if not calls:
        errors.append("no tool events are observable in the ATIF export")
    return {
        "schema_version": "solve-vein/vms41-tool-boundary-audit/v1",
        "attempt_id": attempt_id,
        "tool_call_count": len(calls),
        "verdict": (
            "UNOBSERVABLE"
            if errors == ["no tool events are observable in the ATIF export"]
            else "PASS"
            if not errors
            else "FAIL"
        ),
        "errors": errors,
        "calls": calls,
    }


def verify_attempt_file_set(bundle: Path) -> dict[str, Any]:
    errors: list[str] = []
    if not bundle.is_dir() or bundle.is_symlink():
        errors.append("attempt bundle absent, unsafe, or not a directory")
        observed_names: set[str] = set()
    else:
        observed_names = {path.name for path in bundle.iterdir()}
        for path in bundle.iterdir():
            if path.is_symlink() or not path.is_file():
                errors.append(f"non-regular attempt artifact: {path.name}")
    unknown = observed_names - RUNNER_OWNED_NAMES
    missing_runtime = {
        "AGENTS.md",
        "TASK.md",
        "problem.md",
        "raw_solver_trajectory.txt",
        "reasoning-trajectory-v1.md",
        "input-manifest.json",
        "devin-config.json",
        "catalog-snapshot.txt",
        "launch-receipt.json",
        "attempt-events.jsonl",
        "stdout.txt",
        "stderr.txt",
        "devin-export.json",
        "invocation-receipt.json",
    } - observed_names
    if unknown:
        errors.append(f"unknown attempt artifacts: {sorted(unknown)}")
    if missing_runtime:
        errors.append(f"missing runtime artifacts: {sorted(missing_runtime)}")
    return {
        "schema_version": "solve-vein/vms41-attempt-file-set-audit/v1",
        "observed_names": sorted(observed_names),
        "unknown_names": sorted(unknown),
        "missing_runtime_names": sorted(missing_runtime),
        "verdict": "PASS" if not errors else "FAIL",
        "errors": errors,
    }


def execute_qualification(
    freeze_path: Path,
    *,
    final_root: Path = DEFAULT_FINAL_ROOT,
    partial_root: Path = DEFAULT_PARTIAL_ROOT,
    explicit_binary: Path | None = None,
    enforce_production_site: bool = True,
) -> Path:
    manifest = validate_freeze_manifest(freeze_path)
    if enforce_production_site:
        _validate_production_site(final_root, partial_root)
    if final_root.exists() or final_root.is_symlink():
        raise QualificationRunError(f"final result already exists: {final_root}")
    if partial_root.is_symlink():
        raise QualificationRunError(f"partial root is a symlink: {partial_root}")
    if not partial_root.exists():
        partial_root.mkdir(mode=0o700, parents=False)
        (partial_root / "attempts").mkdir(mode=0o700)
        _write_json_once(
            partial_root / "orchestrator-manifest.json",
            {
                "schema_version": "solve-vein/vms41-orchestrator-manifest/v1",
                "poc_id": POC_ID,
                "run_id": RUN_ID,
                "started_at": _now(),
                "freeze_manifest_sha256": sha256_file(freeze_path),
                "case_ids": list(EXPECTED_CASE_IDS),
                "hidden_grading_deferred_until_all_calls_terminal": True,
            },
        )
        shutil.copyfile(
            freeze_path,
            partial_root / "preexecution-freeze-manifest.json",
            follow_symlinks=False,
        )
        (partial_root / "preexecution-freeze-manifest.json").chmod(0o600)
    else:
        _validate_resumable_partial(partial_root, freeze_path)
    event_log = partial_root / "orchestrator-events.jsonl"
    acceptable_binding = manifest["acceptable_set_pack"]
    acceptable_pack = EventExtractionAcceptableSetPack.from_json_text(
        (REPOSITORY_ROOT / acceptable_binding["path"]).read_text()
    )
    asset_release = REPOSITORY_ROOT / manifest["runtime_profile"]["asset_release_path"]
    role_asset = asset_release / "AGENTS_event_extractor.md"
    task_template = (asset_release / "TASK_event_extractor.template.md").read_text()
    schema_path = asset_release / "reasoning-trajectory-v1.md"
    fixture_root = HERE / "qualification_fixtures" / "vms41"

    for case_id in EXPECTED_CASE_IDS:
        attempt_id = manifest["attempt_ids"][case_id]
        attempt_bundle = partial_root / "attempts" / attempt_id
        interrupted_partial = attempt_bundle.parent / (
            f".{attempt_bundle.name}.partial-{attempt_id}"
        )
        if interrupted_partial.exists() or interrupted_partial.is_symlink():
            raise QualificationRunError(
                f"attempt requires reconciliation and must not relaunch: {attempt_id}"
            )
        if attempt_bundle.exists():
            _validate_existing_attempt(attempt_bundle, attempt_id)
            continue
        acceptable = acceptable_pack.case_by_id(case_id)
        case_dir = fixture_root / CASE_DIRS[case_id]
        task_text = render_task(
            task_template,
            {
                "ATTEMPT_ID": attempt_id,
                "CASE_ID": case_id,
                "TRAJECTORY_ID": acceptable.trajectory_id,
                "PROBLEM_ID": acceptable.problem_id,
                "SOURCE_SHA256": acceptable.source.source_artifact_sha256,
            },
        )
        _append_jsonl(
            event_log,
            {
                "schema_version": "solve-vein/vms41-orchestrator-event/v1",
                "event": "CASE_LAUNCHING",
                "case_id": case_id,
                "attempt_id": attempt_id,
                "observed_at": _now(),
            },
        )
        try:
            receipt = run_devin_role(
                DevinRoleSpec(
                    attempt_id=attempt_id,
                    role="REASONING_EVENT_EXTRACTOR",
                    role_asset_path=role_asset,
                    task_text=task_text,
                    inputs=(
                        RoleInput(case_dir / "problem.md", "problem.md"),
                        RoleInput(
                            case_dir / "raw_solver_trajectory.txt",
                            "raw_solver_trajectory.txt",
                        ),
                        RoleInput(schema_path, "reasoning-trajectory-v1.md"),
                    ),
                    expected_output_name="reasoning-trajectory.json",
                    output_bundle=attempt_bundle,
                    sandbox_requested=False,
                    timeout_seconds=manifest["resource_contract"][
                        "timeout_seconds_per_case"
                    ],
                    infrastructure_retry_index=0,
                    expected_global_agents_sha256=manifest["runtime_profile"][
                        "global_agents_sha256"
                    ],
                ),
                explicit_binary=explicit_binary,
            )
        except RoleRuntimeError as exc:
            _append_jsonl(
                event_log,
                {
                    "schema_version": "solve-vein/vms41-orchestrator-event/v1",
                    "event": "CASE_QUARANTINED",
                    "case_id": case_id,
                    "attempt_id": attempt_id,
                    "observed_at": _now(),
                    "error_code": exc.code,
                },
            )
            raise QualificationRunError(str(exc)) from exc
        _append_jsonl(
            event_log,
            {
                "schema_version": "solve-vein/vms41-orchestrator-event/v1",
                "event": "CASE_TERMINAL",
                "case_id": case_id,
                "attempt_id": attempt_id,
                "observed_at": _now(),
                "invocation_receipt_sha256": sha256_file(
                    attempt_bundle / "invocation-receipt.json"
                ),
                "exit_code": receipt["exit_code"],
            },
        )
        if _invocation_protocol_errors(receipt, manifest):
            break

    terminal_case_ids = [
        case_id
        for case_id in EXPECTED_CASE_IDS
        if (partial_root / "attempts" / manifest["attempt_ids"][case_id]).is_dir()
    ]
    case_results: list[dict[str, Any]] = []
    all_calls_terminal = tuple(terminal_case_ids) == EXPECTED_CASE_IDS
    if all_calls_terminal:
        for case_id in EXPECTED_CASE_IDS:
            acceptable = acceptable_pack.case_by_id(case_id)
            attempt_id = manifest["attempt_ids"][case_id]
            attempt_bundle = partial_root / "attempts" / attempt_id
            receipt = _load_object(
                attempt_bundle / "invocation-receipt.json", "invocation receipt"
            )
            raw = (attempt_bundle / "raw_solver_trajectory.txt").read_bytes()
            candidate_path = attempt_bundle / "reasoning-trajectory.json"
            candidate_text = candidate_path.read_text() if candidate_path.is_file() else ""
            evaluation = evaluate_candidate_json(candidate_text, acceptable, raw)
            tool_audit = audit_tool_boundary(
                attempt_bundle / "devin-export.json", attempt_bundle, attempt_id
            )
            file_set_audit = verify_attempt_file_set(attempt_bundle)
            protocol_errors = _invocation_protocol_errors(receipt, manifest)
            if tool_audit["verdict"] != "PASS":
                protocol_errors.append("tool boundary audit did not PASS")
            if file_set_audit["verdict"] != "PASS":
                protocol_errors.append("attempt file set audit did not PASS")
            case_status = (
                "INCONCLUSIVE_PROTOCOL"
                if protocol_errors
                else "PENDING_MANUAL_AUDIT"
                if evaluation.overall_status
                is OverallQualificationStatus.PENDING_MANUAL_AUDIT
                else "FAIL"
            )
            result = {
                "schema_version": "solve-vein/vms41-case-result/v1",
                "case_id": case_id,
                "attempt_id": attempt_id,
                "invocation_receipt_sha256": sha256_file(
                    attempt_bundle / "invocation-receipt.json"
                ),
                "tool_boundary_audit": tool_audit,
                "attempt_file_set_audit": file_set_audit,
                "mechanical_evaluation": evaluation.to_dict(),
                "protocol_errors": protocol_errors,
                "manual_semantic_audit": "PENDING",
                "case_status": case_status,
            }
            result_path = partial_root / "evaluations" / f"{case_id}.json"
            _write_or_verify_json(result_path, result)
            case_results.append(result)

    aggregate_status = (
        "INCONCLUSIVE_PROTOCOL"
        if not all_calls_terminal
        or any(result["case_status"] == "INCONCLUSIVE_PROTOCOL" for result in case_results)
        else "PENDING_MANUAL_AUDIT"
        if all(result["case_status"] == "PENDING_MANUAL_AUDIT" for result in case_results)
        else "FAIL"
    )
    aggregate = {
        "schema_version": "solve-vein/vms41-live-aggregate/v1",
        "poc_id": POC_ID,
        "run_id": RUN_ID,
        "case_ids": list(EXPECTED_CASE_IDS),
        "terminal_case_ids": terminal_case_ids,
        "case_results": [
            {
                "case_id": result["case_id"],
                "attempt_id": result["attempt_id"],
                "case_status": result["case_status"],
                "mechanical_scientific_verdict": result["mechanical_evaluation"][
                    "mechanical_scientific_verdict"
                ],
            }
            for result in case_results
        ],
        "manual_semantic_audit": "PENDING" if all_calls_terminal else "NOT_REACHED",
        "component_qualification": "NOT_YET_DECIDABLE",
        "overall_status": aggregate_status,
        "explicit_nonclaims": [
            "mechanical_pass_is_not_component_qualification",
            "does_not_qualify_state_normalizer_or_trace_auditor",
            "does_not_test_streaming_recovery_or_concurrency",
            "does_not_validate_tell_hint_or_two_tree_effects",
            "does_not_connect_database_redis_seven_or_target_solver",
        ],
    }
    _write_or_verify_json(partial_root / "live-aggregate.json", aggregate)
    _seal_root(partial_root, final_root, freeze_path, aggregate_status)
    return final_root


def _invocation_protocol_errors(
    receipt: Mapping[str, Any], manifest: Mapping[str, Any]
) -> list[str]:
    errors: list[str] = []
    profile = manifest["runtime_profile"]
    if receipt.get("exit_code") != 0:
        errors.append("Devin exit code is not zero")
    if receipt.get("timed_out") is not False:
        errors.append("Devin attempt timed out")
    if receipt.get("retry_count") != 0:
        errors.append("retry count is not zero")
    if receipt.get("requested_model_uid") != profile["model_uid"]:
        errors.append("requested model drift")
    if receipt.get("model_observability_verdict") != "MATCH":
        errors.append("effective generation model is not an exact observable match")
    if receipt.get("resolved_binary_sha256") != profile["resolved_binary_sha256"]:
        errors.append("resolved Devin binary drift")
    if receipt.get("cli_version") != profile["cli_version"]:
        errors.append("Devin version drift")
    if receipt.get("model_catalog_snapshot_sha256") != profile["catalog_snapshot_sha256"]:
        errors.append("model catalog drift")
    if receipt.get("sandbox_requested") is not False:
        errors.append("sandbox profile drift")
    if receipt.get("permission_mode") != "dangerous":
        errors.append("permission mode drift")
    global_agents = receipt.get("global_control_surface")
    if not isinstance(global_agents, dict):
        errors.append("global control surface is unobservable")
    else:
        if global_agents.get("path") != profile["global_agents_path"]:
            errors.append("global AGENTS path drift")
        if global_agents.get("sha256") != profile["global_agents_sha256"]:
            errors.append("global AGENTS hash drift")
        if global_agents.get("size_bytes") != profile["global_agents_size_bytes"]:
            errors.append("global AGENTS size drift")
    if receipt.get("request_accepted_observability") != "OBSERVED_POSTHOC":
        errors.append("request acceptance is unobservable")
    if receipt.get("generation_started_observability") != "OBSERVED_POSTHOC":
        errors.append("generation start is unobservable")
    if not receipt.get("output_sha256"):
        errors.append("candidate output is absent")
    if receipt.get("done_marker_content_valid") is not True:
        errors.append("DONE marker is absent or invalid")
    if not receipt.get("export_sha256"):
        errors.append("ATIF export is absent")
    return errors


def _validate_existing_attempt(bundle: Path, attempt_id: str) -> None:
    receipt = _load_object(bundle / "invocation-receipt.json", "existing invocation receipt")
    if receipt.get("attempt_id") != attempt_id:
        raise QualificationRunError(f"existing attempt identity mismatch: {attempt_id}")


def _validate_resumable_partial(partial_root: Path, freeze_path: Path) -> None:
    if not partial_root.is_dir():
        raise QualificationRunError("partial root is not a directory")
    orchestrator = _load_object(
        partial_root / "orchestrator-manifest.json", "orchestrator manifest"
    )
    if orchestrator.get("freeze_manifest_sha256") != sha256_file(freeze_path):
        raise QualificationRunError("partial root belongs to another freeze manifest")
    copied = partial_root / "preexecution-freeze-manifest.json"
    if not copied.is_file() or sha256_file(copied) != sha256_file(freeze_path):
        raise QualificationRunError("partial root freeze copy drift")


def _write_or_verify_json(path: Path, value: Any) -> None:
    payload = canonical_json_bytes(value)
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file() or path.read_bytes() != payload:
            raise QualificationRunError(f"existing derived artifact differs: {path}")
        return
    _write_once(path, payload)


def _seal_root(
    partial_root: Path,
    final_root: Path,
    freeze_path: Path,
    aggregate_status: str,
) -> None:
    if final_root.exists() or final_root.is_symlink():
        raise QualificationRunError(f"final root already exists: {final_root}")
    artifact_rows: list[dict[str, Any]] = []
    for path in sorted(partial_root.rglob("*")):
        if path.is_symlink():
            raise QualificationRunError(f"symlink cannot be sealed: {path}")
        if path.is_file() and path.name not in {"final-receipt.json", "COMMITTED"}:
            artifact_rows.append(
                {
                    "path": path.relative_to(partial_root).as_posix(),
                    "size_bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    tree_payload = "".join(
        f"{row['sha256']}  {row['path']}\n" for row in artifact_rows
    ).encode()
    receipt = {
        "schema_version": "solve-vein/vms41-final-receipt/v1",
        "poc_id": POC_ID,
        "run_id": RUN_ID,
        "sealed_at": _now(),
        "freeze_manifest_sha256": sha256_file(freeze_path),
        "artifacts": artifact_rows,
        "artifact_tree_sha256": _sha256_bytes(tree_payload),
        "artifact_integrity": "PASS",
        "live_attempt_status": aggregate_status,
        "manual_semantic_audit": "PENDING",
        "component_qualification": "NOT_YET_DECIDABLE",
    }
    _write_json_once(partial_root / "final-receipt.json", receipt)
    _write_once(
        partial_root / "COMMITTED",
        (
            "final-receipt.json SHA256="
            + sha256_file(partial_root / "final-receipt.json")
            + "\n"
        ).encode(),
    )
    os.replace(partial_root, final_root)


def _validate_production_site(final_root: Path, partial_root: Path) -> None:
    if final_root != DEFAULT_FINAL_ROOT or partial_root != DEFAULT_PARTIAL_ROOT:
        raise QualificationRunError("production CLI cannot redirect the frozen result roots")
    if not os.path.ismount(APPROVED_VOLUME):
        raise QualificationRunError("D volume is not mounted")
    for path in (APPROVED_VOLUME, APPROVED_DATA_ROOT, APPROVED_RESULTS_ROOT):
        if not path.is_dir() or path.is_symlink():
            raise QualificationRunError(f"approved path missing or unsafe: {path}")
    if APPROVED_RESULTS_ROOT.stat().st_dev != APPROVED_VOLUME.stat().st_dev:
        raise QualificationRunError("result root is not on the D volume device")
    resolved = APPROVED_RESULTS_ROOT.resolve(strict=True)
    if resolved != APPROVED_RESULTS_ROOT:
        raise QualificationRunError("result root resolves through a symlink")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--freeze", type=Path, default=DEFAULT_FREEZE)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="consume the four one-shot model attempts; omitted means preflight only",
    )
    args = parser.parse_args()
    manifest = validate_freeze_manifest(args.freeze)
    if not args.execute:
        print(
            json.dumps(
                {
                    "poc_id": manifest["poc_id"],
                    "run_id": manifest["run_id"],
                    "freeze_manifest_sha256": sha256_file(args.freeze),
                    "verdict": "PREFLIGHT_PASS_NO_MODEL_CALL",
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    final_root = execute_qualification(args.freeze)
    print(final_root)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QualificationRunError as exc:
        print(f"VMS41_RUN_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
