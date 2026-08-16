"""Create the append-once preexecution freeze for POC-VMS-41.

This command performs only local deterministic tests and Devin CLI identity /
catalog preflight commands.  It does not start a Devin session, call a model,
connect a database or Redis, invoke the Target Solver, or write outside the
three declared live-fixture artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import unittest
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.event_extraction_qualification import (
    EventExtractionAcceptableSetPack,
)
from system.solve_vein_analysis.role_runtime import (
    DEVIN_EFFORT_ENCODING,
    DEVIN_MODEL_UID,
    DEVIN_NORMALIZED_EFFORT,
    canonical_json_bytes,
    resolve_devin_binary,
    sha256_file,
)
from system.tests.solve_vein_analysis.run_event_extractor_qualification import (
    CASE_DIRS,
    DEFAULT_FINAL_ROOT,
    DEFAULT_PARTIAL_ROOT,
    EXPECTED_CASE_IDS,
    POC_ID,
    RUN_ID,
    _validate_production_site,
    qualification_test_source_files,
    test_source_tree_sha256,
)


HERE = Path(__file__).resolve().parent
LIVE_FIXTURES = HERE / "live_fixtures"
PROTOCOL = (
    REPO_ROOT
    / "第六代系统研发过程文档"
    / "368-v0-2026-08-14-POC-VMS-41-Event-Extractor未见样本资格化协议.md"
)
FIXTURE_ROOT = HERE / "qualification_fixtures/vms41"
ACCEPTABLE_SET = FIXTURE_ROOT / "acceptable-sets.json"
ASSET_ROOT = REPO_ROOT / "system/assets/solve_vein_analysis/releases/0.4.0"
BASELINE = HERE / "protected_absorb_baseline.sha256"
CATALOG_TARGET = LIVE_FIXTURES / "poc_vms_41.model-catalog.txt"
TEST_GATE_TARGET = LIVE_FIXTURES / "poc_vms_41.test-gate.json"
FREEZE_TARGET = LIVE_FIXTURES / "poc_vms_41.freeze.json"
MINIMUM_FREE_BYTES = 2 * 1024 * 1024 * 1024


class FreezeError(RuntimeError):
    """Fail-closed freeze construction error."""


def _flatten_tests(suite: unittest.TestSuite) -> Iterable[unittest.TestCase]:
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from _flatten_tests(item)
        else:
            yield item


def run_controlled_test_gate() -> dict[str, Any]:
    loader = unittest.TestLoader()
    try:
        # Match the canonical command documented in the test README.  Passing
        # ``top_level_dir`` makes Python 3.14 require this deliberately
        # non-package fixture directory to be importable and fails before a
        # single test is run.
        suite = loader.discover(str(HERE), pattern="test_*.py")
    except (ImportError, OSError) as exc:
        raise FreezeError(f"controlled test discovery failed: {exc}") from exc
    test_ids = [test.id() for test in _flatten_tests(suite)]
    if not test_ids or len(test_ids) != len(set(test_ids)):
        raise FreezeError("controlled test IDs are empty or duplicated")
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=1).run(suite)
    receipt = {
        "runner": "python_unittest_in_process",
        "python_executable": str(Path(sys.executable).resolve(strict=True)),
        "python_executable_sha256": sha256_file(
            Path(sys.executable).resolve(strict=True)
        ),
        "python_version": sys.version,
        "test_ids": test_ids,
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped),
        "successful": result.wasSuccessful(),
        "test_source_tree_sha256": test_source_tree_sha256(),
        "protected_absorb_baseline_path": BASELINE.relative_to(REPO_ROOT).as_posix(),
        "protected_absorb_baseline_sha256": sha256_file(BASELINE),
        "protected_absorb_file_count": len(BASELINE.read_text().splitlines()),
        "verdict": "PASS" if result.wasSuccessful() and not result.skipped else "FAIL",
    }
    if (
        receipt["tests_run"] != len(test_ids)
        or receipt["failures"]
        or receipt["errors"]
        or receipt["skipped"]
        or receipt["protected_absorb_file_count"] != 161
        or receipt["verdict"] != "PASS"
    ):
        raise FreezeError(
            "controlled tests did not pass exactly:\n" + stream.getvalue()
        )
    return receipt


def _minimal_preflight_environment() -> dict[str, str]:
    allowed = ("HOME", "PATH", "SHELL", "TMPDIR", "LANG", "LC_ALL")
    return {name: os.environ[name] for name in allowed if name in os.environ}


def inspect_devin_profile(binary: Path) -> tuple[str, bytes]:
    env = _minimal_preflight_environment()
    version = subprocess.run(
        [str(binary), "--version"],
        check=False,
        capture_output=True,
        text=True,
        timeout=60,
        env=env,
    )
    if version.returncode != 0:
        raise FreezeError(f"Devin version preflight failed: {version.stderr.strip()}")
    catalog = subprocess.run(
        [str(binary), "models", "list"],
        check=False,
        capture_output=True,
        text=True,
        timeout=60,
        env=env,
    )
    if catalog.returncode != 0:
        raise FreezeError(f"Devin catalog preflight failed: {catalog.stderr.strip()}")
    if DEVIN_MODEL_UID not in catalog.stdout or "GLM-5.2 High" not in catalog.stdout:
        raise FreezeError("Devin catalog does not expose the exact GLM-5.2 High UID")
    return version.stdout.strip() or version.stderr.strip(), catalog.stdout.encode("utf-8")


def _case_specs(pack: EventExtractionAcceptableSetPack) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for acceptable in pack.cases:
        fixture_dir = FIXTURE_ROOT / CASE_DIRS[acceptable.case_id]
        problem = fixture_dir / "problem.md"
        raw = fixture_dir / "raw_solver_trajectory.txt"
        receipt = fixture_dir / "source-receipt.json"
        rows.append(
            {
                "case_id": acceptable.case_id,
                "fixture_dir": CASE_DIRS[acceptable.case_id],
                "acceptable_set_id": acceptable.acceptable_set_id,
                "problem_path": problem.relative_to(REPO_ROOT).as_posix(),
                "problem_sha256": sha256_file(problem),
                "raw_path": raw.relative_to(REPO_ROOT).as_posix(),
                "raw_sha256": sha256_file(raw),
                "source_receipt_path": (
                    receipt.relative_to(REPO_ROOT).as_posix()
                    if receipt.is_file()
                    else None
                ),
                "source_receipt_sha256": sha256_file(receipt) if receipt.is_file() else None,
            }
        )
    if tuple(row["case_id"] for row in rows) != EXPECTED_CASE_IDS:
        raise FreezeError("acceptable-set case order drift")
    return rows


def _frozen_file_paths() -> tuple[Path, ...]:
    paths: set[Path] = {PROTOCOL, ACCEPTABLE_SET, BASELINE, TEST_GATE_TARGET, CATALOG_TARGET}
    for root in (
        REPO_ROOT / "system/solve_vein_analysis",
        HERE,
        FIXTURE_ROOT,
        ASSET_ROOT,
    ):
        for path in root.rglob("*"):
            if path.is_file() and not path.is_symlink():
                if "__pycache__" in path.parts or "poc_results" in path.parts:
                    continue
                if root == HERE and not (
                    path in qualification_test_source_files()
                    or path.suffix in {".ref", ".ai-check"}
                    and path.with_suffix(".py") in qualification_test_source_files()
                    or path == BASELINE
                    or path in {TEST_GATE_TARGET, CATALOG_TARGET}
                ):
                    continue
                paths.add(path)
    missing = [path for path in paths if path.is_symlink() or not path.is_file()]
    if missing:
        raise FreezeError(f"frozen source absent or unsafe: {missing}")
    return tuple(sorted(paths))


def build_manifest(
    *,
    binary: Path,
    cli_version: str,
    catalog_bytes: bytes,
    test_gate: dict[str, Any],
) -> dict[str, Any]:
    home = os.environ.get("HOME")
    global_agents = (
        Path(home) / ".config/devin/AGENTS.md" if home else Path("/missing")
    )
    if global_agents.is_symlink() or not global_agents.is_file():
        raise FreezeError("user-level Devin AGENTS is absent or unsafe")
    pack = EventExtractionAcceptableSetPack.from_json_text(ACCEPTABLE_SET.read_text())
    return {
        "schema_version": "solve-vein/vms41-preexecution-freeze/v1",
        "poc_id": POC_ID,
        "run_id": RUN_ID,
        "protocol": {
            "path": PROTOCOL.relative_to(REPO_ROOT).as_posix(),
            "sha256": sha256_file(PROTOCOL),
        },
        "acceptable_set_pack": {
            "path": ACCEPTABLE_SET.relative_to(REPO_ROOT).as_posix(),
            "sha256": sha256_file(ACCEPTABLE_SET),
        },
        "frozen_files": [
            {
                "path": path.relative_to(REPO_ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
            for path in _frozen_file_paths()
        ],
        "case_specs": _case_specs(pack),
        "runtime_profile": {
            "carrier": "devin_cli",
            "role": "REASONING_EVENT_EXTRACTOR",
            "model_uid": DEVIN_MODEL_UID,
            "normalized_effort": DEVIN_NORMALIZED_EFFORT,
            "effort_encoding": DEVIN_EFFORT_ENCODING,
            "orchestration_mode": "fresh_single_agent_one_shot",
            "fresh_session": True,
            "resume_allowed": False,
            "sandbox_requested": False,
            "permission_mode": "dangerous",
            "asset_release_path": ASSET_ROOT.relative_to(REPO_ROOT).as_posix(),
            "resolved_binary_path": str(binary),
            "resolved_binary_sha256": sha256_file(binary),
            "cli_version": cli_version,
            "catalog_snapshot_sha256": hashlib.sha256(catalog_bytes).hexdigest(),
            "global_agents_path": "~/.config/devin/AGENTS.md",
            "global_agents_sha256": sha256_file(global_agents),
            "global_agents_size_bytes": global_agents.stat().st_size,
        },
        "resource_contract": {
            "case_attempts": 1,
            "concurrency": 1,
            "infrastructure_retries": 0,
            "scientific_retries": 0,
            "timeout_seconds_per_case": 900,
        },
        "attempt_ids": {
            "V41-SYN-FALSE-MERGE": "poc-vms-41-syn-false-merge-a1",
            "V41-SYN-TRUE-MERGE": "poc-vms-41-syn-true-merge-a1",
            "V41-REAL-SPIRAL": "poc-vms-41-real-spiral-a1",
            "V41-REAL-BATTERY": "poc-vms-41-real-battery-a1",
        },
        "output_root": str(DEFAULT_FINAL_ROOT),
        "test_gate": test_gate,
        "side_effect_authorization": {
            "devin_role_attempts_authorized": 4,
            "database_connections": 0,
            "network_calls_by_candidate": 0,
            "redis_connections": 0,
            "solver_calls": 0,
            "subagent_calls": 0,
        },
    }


def _write_or_verify(path: Path, payload: bytes) -> None:
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file() or path.read_bytes() != payload:
            raise FreezeError(f"append-once artifact differs: {path}")
        return
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(descriptor, payload)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def freeze(explicit_binary: Path | None = None) -> dict[str, Any]:
    _validate_production_site(DEFAULT_FINAL_ROOT, DEFAULT_PARTIAL_ROOT)
    if DEFAULT_FINAL_ROOT.exists() or DEFAULT_FINAL_ROOT.is_symlink():
        raise FreezeError("VMS-41 final live result already exists")
    if DEFAULT_PARTIAL_ROOT.exists() or DEFAULT_PARTIAL_ROOT.is_symlink():
        raise FreezeError("VMS-41 partial live result requires reconciliation")
    if shutil.disk_usage(DEFAULT_FINAL_ROOT.parent).free < MINIMUM_FREE_BYTES:
        raise FreezeError("approved D result root has less than 2 GiB free")
    binary = resolve_devin_binary(explicit_binary)
    cli_version, catalog_bytes = inspect_devin_profile(binary)
    test_gate = run_controlled_test_gate()
    _write_or_verify(CATALOG_TARGET, catalog_bytes)
    _write_or_verify(TEST_GATE_TARGET, canonical_json_bytes(test_gate))
    manifest = build_manifest(
        binary=binary,
        cli_version=cli_version,
        catalog_bytes=catalog_bytes,
        test_gate=test_gate,
    )
    _write_or_verify(FREEZE_TARGET, canonical_json_bytes(manifest))
    return {
        "schema_version": "solve-vein/vms41-freeze-operation/v1",
        "operation": "FROZEN",
        "freeze_path": str(FREEZE_TARGET),
        "freeze_sha256": sha256_file(FREEZE_TARGET),
        "test_count": test_gate["tests_run"],
        "protected_absorb_file_count": test_gate["protected_absorb_file_count"],
        "model_calls": 0,
        "platform": platform.platform(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--devin-binary", type=Path)
    args = parser.parse_args()
    result = freeze(args.devin_binary)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FreezeError, OSError, subprocess.SubprocessError) as exc:
        print(f"VMS41_FREEZE_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
