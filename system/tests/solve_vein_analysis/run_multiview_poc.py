"""Run the append-once deterministic POC-VMS-40 evidence build."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import uuid
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from system.solve_vein_analysis.integrity import (
    implementation_tree_receipt,
    sha256_file,
)
from system.solve_vein_analysis.semantic_truth import (
    SemanticAcceptableSet,
    evaluate_candidate_value,
    sha256_json,
)


HERE = Path(__file__).resolve().parent
FIXTURE_PATH = HERE / "multiview_fixtures" / "vms40_cases.json"
PROTOCOL_PATH = (
    REPOSITORY_ROOT
    / "第六代系统研发过程文档"
    / "366-v0-2026-08-14-POC-VMS-40-多视图脉络真值与acceptable-set确定性协议.md"
)
APPROVED_RESULT_ROOT = Path(
    "/data/master-mind-solve-vein-data/poc-results"
)
FINAL_RESULT_DIR = APPROVED_RESULT_ROOT / "poc-vms-40-20260814"
PROTOCOL_SHA256 = (
    "8d045365b5cd14d8d98d617ddec7c6607d96aeb1e2a871216fa1c631ca1b6857"
)
EXPECTED_CASE_IDS = ("MV1", "MV2", "MV3", "MV4", "MV5", "MV6")
EXPECTED_CANDIDATE_COUNT = 26


class PocExecutionError(RuntimeError):
    """Fail-closed POC execution error."""


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def write_json(path: Path, value: Any) -> None:
    if path.exists() or path.is_symlink():
        raise PocExecutionError(f"refusing to overwrite {path}")
    path.write_bytes(canonical_json_bytes(value))


def evaluate_fixture_pack(pack: dict[str, Any]) -> dict[str, Any]:
    if set(pack) != {"schema_version", "poc_id", "protocol_sha256", "cases"}:
        raise PocExecutionError("fixture pack keys are invalid")
    if pack["schema_version"] != "solve-vein/multiview-fixture-pack/v1":
        raise PocExecutionError("fixture pack schema is invalid")
    if pack["poc_id"] != "POC-VMS-40":
        raise PocExecutionError("fixture POC identity mismatch")
    if pack["protocol_sha256"] != PROTOCOL_SHA256:
        raise PocExecutionError("fixture protocol hash mismatch")
    case_ids = [case["case_id"] for case in pack["cases"]]
    if tuple(case_ids) != EXPECTED_CASE_IDS:
        raise PocExecutionError(f"fixture case IDs are not frozen: {case_ids}")
    case_results: list[dict[str, Any]] = []
    candidate_count = 0
    mismatches: list[dict[str, str]] = []
    for case in pack["cases"]:
        acceptable = SemanticAcceptableSet.from_dict(case["acceptable_set"])
        candidate_results: list[dict[str, Any]] = []
        for spec in case["candidates"]:
            evaluation = evaluate_candidate_value(spec["candidate"], acceptable)
            observed = evaluation.overall_verdict.value
            expected = spec["expected_verdict"]
            matched = observed == expected
            if not matched:
                mismatches.append(
                    {
                        "case_id": case["case_id"],
                        "label": spec["label"],
                        "expected": expected,
                        "observed": observed,
                    }
                )
            candidate_results.append(
                {
                    "label": spec["label"],
                    "expected_verdict": expected,
                    "observed_verdict": observed,
                    "matched": matched,
                    "candidate_input_sha256": _best_effort_hash(spec["candidate"]),
                    "evaluation": evaluation.to_dict(),
                    "evaluation_sha256": evaluation.canonical_sha256,
                }
            )
            candidate_count += 1
        case_results.append(
            {
                "case_id": case["case_id"],
                "claim": case["claim"],
                "acceptable_set_sha256": acceptable.canonical_sha256,
                "candidate_results": candidate_results,
                "case_verdict": (
                    "PASS"
                    if all(item["matched"] for item in candidate_results)
                    else "FAIL"
                ),
            }
        )
    if candidate_count != EXPECTED_CANDIDATE_COUNT:
        raise PocExecutionError(
            f"expected {EXPECTED_CANDIDATE_COUNT} candidates, got {candidate_count}"
        )
    return {
        "schema_version": "solve-vein/vms40-evaluation-matrix/v1",
        "poc_id": "POC-VMS-40",
        "case_ids": list(EXPECTED_CASE_IDS),
        "case_count": len(case_results),
        "candidate_count": candidate_count,
        "case_results": case_results,
        "mismatches": mismatches,
        "all_expected_verdicts_matched": not mismatches,
        "matrix_verdict": "PASS" if not mismatches else "FAIL",
    }


def run_controlled_tests(partial_dir: Path) -> dict[str, Any]:
    command = [
        sys.executable,
        "-m",
        "unittest",
        "system.tests.solve_vein_analysis.test_semantic_truth",
        "-v",
    ]
    completed = subprocess.run(
        command,
        cwd=REPOSITORY_ROOT,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
        env={
            "PATH": os.environ.get("PATH", ""),
            "PYTHONIOENCODING": "utf-8",
            "PYTHONDONTWRITEBYTECODE": "1",
        },
    )
    stdout_path = partial_dir / "test-stdout.txt"
    stderr_path = partial_dir / "test-stderr.txt"
    stdout_path.write_text(completed.stdout)
    stderr_path.write_text(completed.stderr)
    passed = (
        completed.returncode == 0
        and "Ran 16 tests" in completed.stderr
        and completed.stderr.rstrip().endswith("OK")
    )
    return {
        "schema_version": "solve-vein/test-execution-receipt/v1",
        "command": command,
        "cwd": str(REPOSITORY_ROOT),
        "exit_code": completed.returncode,
        "expected_test_count": 16,
        "stdout_sha256": sha256_file(stdout_path),
        "stderr_sha256": sha256_file(stderr_path),
        "verdict": "PASS" if passed else "FAIL",
    }


def build_poc_bundle() -> Path:
    result_root = _validate_site()
    if FINAL_RESULT_DIR.exists() or FINAL_RESULT_DIR.is_symlink():
        raise PocExecutionError(f"append-once destination exists: {FINAL_RESULT_DIR}")
    protocol_hash = sha256_file(PROTOCOL_PATH)
    if protocol_hash != PROTOCOL_SHA256:
        raise PocExecutionError(
            f"protocol hash drift: expected={PROTOCOL_SHA256}, actual={protocol_hash}"
        )
    pack = json.loads(FIXTURE_PATH.read_text())
    if pack["protocol_sha256"] != protocol_hash:
        raise PocExecutionError("fixture does not bind the frozen protocol")
    partial_dir = result_root / (
        f".poc-vms-40-20260814.partial-{uuid.uuid4().hex}"
    )
    partial_dir.mkdir(mode=0o700)
    try:
        started_at = _now()
        matrix = evaluate_fixture_pack(pack)
        write_json(partial_dir / "evaluation-matrix.json", matrix)
        test_receipt = run_controlled_tests(partial_dir)
        write_json(partial_dir / "test-receipt.json", test_receipt)
        implementation_receipt = implementation_tree_receipt(
            extra_files=(
                Path(__file__),
                Path(__file__).with_suffix(".ref"),
                Path(__file__).with_suffix(".ai-check"),
                HERE / "test_semantic_truth.py",
                HERE / "test_semantic_truth.ref",
                HERE / "test_semantic_truth.ai-check",
                FIXTURE_PATH,
                PROTOCOL_PATH,
            )
        )
        write_json(
            partial_dir / "implementation-tree-receipt.json",
            implementation_receipt,
        )
        manifest = {
            "schema_version": "solve-vein/vms40-run-manifest/v1",
            "poc_id": "POC-VMS-40",
            "run_id": "poc-vms-40-20260814",
            "evidence_lane": "DEVELOPMENT_ONLY_DETERMINISTIC_OFFLINE",
            "started_at": started_at,
            "protocol": {
                "path": str(PROTOCOL_PATH.relative_to(REPOSITORY_ROOT)),
                "sha256": protocol_hash,
            },
            "fixture": {
                "path": str(FIXTURE_PATH.relative_to(REPOSITORY_ROOT)),
                "sha256": sha256_file(FIXTURE_PATH),
                "canonical_sha256": sha256_json(pack),
            },
            "implementation_aggregate_sha256": implementation_receipt[
                "aggregate_sha256"
            ],
            "side_effects": {
                "model_calls": 0,
                "solver_calls": 0,
                "database_connections": 0,
                "redis_connections": 0,
                "network_calls": 0,
                "protected_intake_mutations": 0,
            },
        }
        write_json(partial_dir / "run-manifest.json", manifest)
        primary_paths = sorted(
            (
                path
                for path in partial_dir.iterdir()
                if path.is_file() and path.name not in {"final-receipt.json", "COMMITTED"}
            ),
            key=lambda path: path.name,
        )
        artifacts = [
            {
                "name": path.name,
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
            for path in primary_paths
        ]
        scientific_pass = (
            matrix["matrix_verdict"] == "PASS"
            and matrix["all_expected_verdicts_matched"]
        )
        protocol_pass = test_receipt["verdict"] == "PASS"
        receipt = {
            "schema_version": "solve-vein/vms40-final-receipt/v1",
            "poc_id": "POC-VMS-40",
            "run_id": "poc-vms-40-20260814",
            "sealed_at": _now(),
            "protocol_sha256": protocol_hash,
            "artifacts": artifacts,
            "artifact_tree_sha256": _artifact_tree_hash(artifacts),
            "artifact_integrity": "PASS",
            "protocol_verdict": "PASS" if protocol_pass else "FAIL",
            "scientific_verdict": (
                "PASS_WITHIN_FROZEN_MULTIVIEW_FIXTURES"
                if scientific_pass
                else "FAIL"
            ),
            "overall_verdict": (
                "PASS_WITHIN_DETERMINISTIC_OFFLINE_SCOPE"
                if protocol_pass and scientific_pass
                else "FAIL"
            ),
            "explicit_nonclaims": [
                "does_not_qualify_any_model_role",
                "does_not_test_live_trajectory_extraction",
                "does_not_validate_tell_effectiveness",
                "does_not_implement_trace_tell_sharding",
                "does_not_connect_reasoning_or_guided_trees",
                "does_not_connect_seven_or_any_database"
            ],
        }
        write_json(partial_dir / "final-receipt.json", receipt)
        (partial_dir / "COMMITTED").write_text(
            f"final-receipt.json sha256={sha256_file(partial_dir / 'final-receipt.json')}\n"
        )
        if not protocol_pass or not scientific_pass:
            raise PocExecutionError(
                "POC produced a valid negative result; partial bundle preserved"
            )
        os.replace(partial_dir, FINAL_RESULT_DIR)
    except Exception:
        raise
    return FINAL_RESULT_DIR


def _validate_site() -> Path:
    if not APPROVED_RESULT_ROOT.is_absolute():
        raise PocExecutionError("result root must be absolute")
    result_root = APPROVED_RESULT_ROOT.resolve(strict=True)
    if result_root != APPROVED_RESULT_ROOT:
        raise PocExecutionError("result root must not resolve through a symlink")
    current = result_root
    while current != Path("/"):
        if current.is_symlink():
            raise PocExecutionError(f"symlink ancestor is forbidden: {current}")
        current = current.parent
    if result_root.stat().st_dev != Path("/data").stat().st_dev:
        raise PocExecutionError("result root is not on the approved D volume")
    return result_root


def _artifact_tree_hash(artifacts: list[dict[str, Any]]) -> str:
    payload = "".join(
        f"{item['sha256']}  {item['name']}\n" for item in artifacts
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _best_effort_hash(value: Any) -> str:
    try:
        return sha256_json(value)
    except (TypeError, ValueError):
        return hashlib.sha256(repr(value).encode("utf-8")).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


if __name__ == "__main__":
    try:
        final = build_poc_bundle()
    except PocExecutionError as exc:
        print(f"POC-VMS-40 BLOCKED: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    print(final)
