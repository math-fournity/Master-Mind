"""Replay the immutable, development-only VMS-41R1 calibration pack.

This runner performs deterministic JSON mutation, V2 evaluation and temporary
workspace file-effect scenarios.  It makes no model, Solver, database, Redis
or network call and never writes into the fixture pack.
"""

from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path, PurePosixPath
import tempfile
from typing import Any, Mapping, Sequence

from system.solve_vein_analysis.event_extraction_projection import (
    EventExtractionAcceptableSetV2,
    evaluate_candidate_json_v2,
)
from system.solve_vein_analysis.file_effect_audit import (
    FileEffectPolicy,
    FileOperation,
    audit_file_effects,
    inventory_workspace,
    parse_file_operation_event,
)
from system.solve_vein_analysis.models import canonical_json_bytes


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_FIXTURE_ROOT = (
    Path(__file__).resolve().parent
    / "qualification_fixtures"
    / "vms41r1_calibration"
)
PROTOCOL_PATH = (
    REPOSITORY_ROOT
    / "第六代系统研发过程文档"
    / "371-v0-2026-08-14-POC-VMS-41R1-Event-Extractor-V2修订资格化协议.md"
)
MANIFEST_SCHEMA = "solve-vein/vms41r1-calibration-manifest/v1"
MATRIX_SCHEMA = "solve-vein/vms41r1-calibration-matrix/v1"
RESULT_SCHEMA = "solve-vein/vms41r1-calibration-result/v1"
EXPECTED_DATA_FILES = (
    "acceptable-merge.json",
    "acceptable-reuse.json",
    "candidate-merge.json",
    "candidate-reuse.json",
    "scenario-matrix.json",
    "source.txt",
)
EXPECTED_NONCLAIMS = (
    "DOES_NOT_AUTHORIZE_LIVE_EXECUTION",
    "DOES_NOT_PROVE_STREAMING_OR_PRODUCTION_SCALE",
    "DOES_NOT_QUALIFY_ANY_MODEL_PROFILE",
    "DOES_NOT_USE_QUALIFICATION_HOLDOUT",
)


class CalibrationError(RuntimeError):
    """A fail-closed calibration pack, scenario or mutation error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_calibration_pack(fixture_root: Path = DEFAULT_FIXTURE_ROOT) -> dict[str, Any]:
    root = Path(fixture_root)
    if root.is_symlink() or not root.is_dir():
        raise CalibrationError("FIXTURE_ROOT_UNSAFE", str(root))
    manifest_path = root / "pack-manifest.json"
    manifest = _load_json(manifest_path, "manifest")
    _exact_keys(
        manifest,
        {
            "schema_version",
            "pack_id",
            "evidence_lane",
            "protocol",
            "files",
            "scenario_counts",
            "explicit_nonclaims",
        },
        "manifest",
    )
    if manifest["schema_version"] != MANIFEST_SCHEMA:
        raise CalibrationError("MANIFEST_SCHEMA_UNSUPPORTED", repr(manifest["schema_version"]))
    if manifest["evidence_lane"] != "DEVELOPMENT_ONLY":
        raise CalibrationError("EVIDENCE_LANE_INVALID", repr(manifest["evidence_lane"]))
    pack_id = _identifier(manifest["pack_id"], "manifest.pack_id")
    nonclaims = _sorted_unique_strings(
        manifest["explicit_nonclaims"], "manifest.explicit_nonclaims"
    )
    if nonclaims != EXPECTED_NONCLAIMS:
        raise CalibrationError(
            "EXPLICIT_NONCLAIMS_INVALID",
            f"expected={EXPECTED_NONCLAIMS!r}, actual={nonclaims!r}",
        )
    protocol = _mapping(manifest["protocol"], "manifest.protocol")
    _exact_keys(protocol, {"path", "sha256"}, "manifest.protocol")
    if protocol["path"] != str(PROTOCOL_PATH.relative_to(REPOSITORY_ROOT)):
        raise CalibrationError("PROTOCOL_PATH_MISMATCH", repr(protocol["path"]))
    if sha256_file(PROTOCOL_PATH) != protocol["sha256"]:
        raise CalibrationError("PROTOCOL_HASH_MISMATCH", str(protocol["sha256"]))

    file_rows = _list(manifest["files"], "manifest.files")
    paths: list[str] = []
    for index, raw_row in enumerate(file_rows):
        row = _mapping(raw_row, f"manifest.files[{index}]")
        _exact_keys(row, {"path", "bytes", "sha256"}, f"manifest.files[{index}]")
        relative = _canonical_relative_path(row["path"], f"manifest.files[{index}].path")
        paths.append(relative)
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise CalibrationError("MANIFEST_MEMBER_UNSAFE", relative)
        payload = path.read_bytes()
        if len(payload) != _integer(row["bytes"], f"manifest.files[{index}].bytes"):
            raise CalibrationError("MANIFEST_MEMBER_SIZE_MISMATCH", relative)
        expected_sha256 = _sha256(row["sha256"], f"manifest.files[{index}].sha256")
        if hashlib.sha256(payload).hexdigest() != expected_sha256:
            raise CalibrationError("MANIFEST_MEMBER_HASH_MISMATCH", relative)
    if tuple(paths) != EXPECTED_DATA_FILES:
        raise CalibrationError("MANIFEST_FILE_ORDER_INVALID", repr(paths))
    actual_files = tuple(
        sorted(
            path.name
            for path in root.iterdir()
            if path.is_file() and not path.is_symlink()
        )
    )
    expected_files = tuple(sorted((*EXPECTED_DATA_FILES, "pack-manifest.json")))
    if actual_files != expected_files:
        raise CalibrationError(
            "FIXTURE_FILE_SET_INVALID",
            f"expected={expected_files!r}, actual={actual_files!r}",
        )
    if any(path.is_symlink() or not path.is_file() for path in root.iterdir()):
        raise CalibrationError("FIXTURE_NONREGULAR_MEMBER", str(root))

    source = (root / "source.txt").read_bytes()
    matrix = _load_json(root / "scenario-matrix.json", "scenario_matrix")
    _validate_matrix_shape(matrix)
    if matrix["pack_id"] != pack_id:
        raise CalibrationError(
            "MATRIX_PACK_ID_MISMATCH",
            f"manifest={pack_id!r}, matrix={matrix['pack_id']!r}",
        )
    counts = _mapping(manifest["scenario_counts"], "manifest.scenario_counts")
    _exact_keys(counts, {"candidate", "file_effect", "total"}, "manifest.scenario_counts")
    observed_candidate = len(matrix["candidate_scenarios"])
    observed_file = len(matrix["file_effect_scenarios"])
    expected_counts = {
        "candidate": observed_candidate,
        "file_effect": observed_file,
        "total": observed_candidate + observed_file,
    }
    if counts != expected_counts:
        raise CalibrationError(
            "SCENARIO_COUNT_MISMATCH",
            f"expected={counts!r}, observed={expected_counts!r}",
        )
    bases = {
        name: _load_json(root / name, name)
        for name in (
            "acceptable-merge.json",
            "acceptable-reuse.json",
            "candidate-merge.json",
            "candidate-reuse.json",
        )
    }
    for name in ("acceptable-merge.json", "acceptable-reuse.json"):
        EventExtractionAcceptableSetV2.from_dict(bases[name])
    return {
        "root": root,
        "manifest": manifest,
        "manifest_sha256": sha256_file(manifest_path),
        "source": source,
        "matrix": matrix,
        "bases": bases,
    }


def apply_frozen_mutations(value: Any, mutations: Sequence[Any]) -> Any:
    result = deepcopy(value)
    for index, raw_mutation in enumerate(mutations):
        mutation = _mapping(raw_mutation, f"mutations[{index}]")
        operation = mutation.get("op")
        if operation == "replace":
            _exact_keys(mutation, {"op", "path", "value"}, f"mutations[{index}]")
        elif operation == "remove":
            _exact_keys(mutation, {"op", "path"}, f"mutations[{index}]")
        else:
            raise CalibrationError("MUTATION_OPERATION_INVALID", repr(operation))
        tokens = _parse_pointer(mutation["path"], f"mutations[{index}].path")
        parent, final = _resolve_parent(result, tokens, f"mutations[{index}]")
        if isinstance(parent, list):
            position = _array_index(final, len(parent), f"mutations[{index}]")
            if operation == "replace":
                parent[position] = deepcopy(mutation["value"])
            else:
                parent.pop(position)
        elif isinstance(parent, dict):
            if final not in parent:
                raise CalibrationError("MUTATION_TARGET_MISSING", mutation["path"])
            if operation == "replace":
                parent[final] = deepcopy(mutation["value"])
            else:
                del parent[final]
        else:
            raise CalibrationError("MUTATION_PARENT_NOT_CONTAINER", mutation["path"])
    return result


def run_calibration_pack(fixture_root: Path = DEFAULT_FIXTURE_ROOT) -> dict[str, Any]:
    pack = load_calibration_pack(fixture_root)
    source: bytes = pack["source"]
    candidate_results: list[dict[str, Any]] = []
    file_results: list[dict[str, Any]] = []
    mismatches: list[dict[str, str]] = []

    for scenario in pack["matrix"]["candidate_scenarios"]:
        candidate_base_name = scenario["candidate_base"]
        acceptable_base_name = scenario["acceptable_base"]
        candidate = apply_frozen_mutations(
            pack["bases"][candidate_base_name], scenario["candidate_mutations"]
        )
        acceptable_value = apply_frozen_mutations(
            pack["bases"][acceptable_base_name], scenario["acceptable_mutations"]
        )
        acceptable = EventExtractionAcceptableSetV2.from_dict(acceptable_value)
        candidate_text = json.dumps(
            candidate,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        evaluation = evaluate_candidate_json_v2(candidate_text, acceptable, source)
        observed = _candidate_projection(evaluation.to_dict())
        expected = scenario["expected"]
        matched = observed == expected
        if not matched:
            mismatches.append(
                {
                    "scenario_id": scenario["scenario_id"],
                    "kind": "candidate",
                    "expected_sha256": _sha256_json(expected),
                    "observed_sha256": _sha256_json(observed),
                }
            )
        candidate_results.append(
            {
                "scenario_id": scenario["scenario_id"],
                "case_role": scenario["case_role"],
                "candidate_base_sha256": _sha256_json(
                    pack["bases"][candidate_base_name]
                ),
                "acceptable_base_sha256": _sha256_json(
                    pack["bases"][acceptable_base_name]
                ),
                "candidate_mutations_sha256": _sha256_json(
                    scenario["candidate_mutations"]
                ),
                "acceptable_mutations_sha256": _sha256_json(
                    scenario["acceptable_mutations"]
                ),
                "materialized_candidate_sha256": _sha256_json(candidate),
                "materialized_acceptable_sha256": _sha256_json(acceptable_value),
                "evaluation_sha256": _sha256_json(evaluation.to_dict()),
                "expected": expected,
                "observed": observed,
                "matched": matched,
            }
        )

    for scenario in pack["matrix"]["file_effect_scenarios"]:
        result = _run_file_effect_scenario(scenario)
        expected = scenario["expected"]
        observed = {
            "verdict": result["verdict"],
            "error_codes": sorted({item["code"] for item in result["errors"]}),
            "transient_event_paths": result["transient_event_paths"],
            "unexplained_residual_changes": result["unexplained_residual_changes"],
        }
        matched = observed == expected
        if not matched:
            mismatches.append(
                {
                    "scenario_id": scenario["scenario_id"],
                    "kind": "file_effect",
                    "expected_sha256": _sha256_json(expected),
                    "observed_sha256": _sha256_json(observed),
                }
            )
        file_results.append(
            {
                "scenario_id": scenario["scenario_id"],
                "scenario_sha256": _sha256_json(scenario),
                "evaluation_sha256": _sha256_json(result),
                "expected": expected,
                "observed": observed,
                "matched": matched,
            }
        )

    return {
        "schema_version": RESULT_SCHEMA,
        "pack_id": pack["manifest"]["pack_id"],
        "evidence_lane": "DEVELOPMENT_ONLY",
        "manifest_sha256": pack["manifest_sha256"],
        "candidate_scenario_count": len(candidate_results),
        "file_effect_scenario_count": len(file_results),
        "candidate_results": candidate_results,
        "file_effect_results": file_results,
        "mismatches": mismatches,
        "all_expected_verdicts_matched": not mismatches,
        "verdict": "PASS" if not mismatches else "FAIL",
        "explicit_nonclaims": pack["manifest"]["explicit_nonclaims"],
    }


def _candidate_projection(evaluation: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "protocol_verdict": evaluation["protocol_verdict"],
        "artifact_verdict": evaluation["artifact_verdict"],
        "anchor_coverage_verdict": evaluation["anchor_coverage_verdict"],
        "typed_path_verdict": evaluation["typed_path_verdict"],
        "temporal_status_verdict": evaluation["temporal_status_verdict"],
        "merge_contribution_verdict": evaluation["merge_contribution_verdict"],
        "forbidden_semantics_verdict": evaluation["forbidden_semantics_verdict"],
        "mechanical_scientific_verdict": evaluation["mechanical_scientific_verdict"],
        "overall_status": evaluation["overall_status"],
        "error_codes": sorted({item["code"] for item in evaluation["errors"]}),
    }


def _run_file_effect_scenario(scenario: Mapping[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="vms41r1-calibration-") as temporary:
        temp_root = Path(temporary)
        workspace = temp_root / "workspace"
        workspace.mkdir()
        for row in scenario["before_files"]:
            path = workspace / _canonical_relative_path(row["path"], "before_files.path")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(row["content"])
        before = inventory_workspace(
            workspace,
            inventory_id=f"{scenario['scenario_id']}-before",
            workspace_id=scenario["scenario_id"],
        )
        for action in scenario["actions"]:
            _apply_file_action(action, workspace=workspace, temp_root=temp_root)
        after = inventory_workspace(
            workspace,
            inventory_id=f"{scenario['scenario_id']}-after",
            workspace_id=scenario["scenario_id"],
        )
        events = tuple(
            parse_file_operation_event(value, workspace_root=workspace)
            for value in scenario["events"]
        )
        policy_value = scenario["policy"]
        policy = FileEffectPolicy.create(
            policy_id=policy_value["policy_id"],
            allowed_created_paths=policy_value["allowed_created_paths"],
            allowed_modified_paths=policy_value["allowed_modified_paths"],
            allowed_deleted_paths=policy_value["allowed_deleted_paths"],
            allowed_operation_paths=policy_value["allowed_operation_paths"],
            allow_preexisting_symlinks=policy_value["allow_preexisting_symlinks"],
        )
        return audit_file_effects(
            before=before,
            after=after,
            events=events,
            event_observability=scenario["event_observability"],
            observability_evidence_ref=scenario["observability_evidence_ref"],
            observability_evidence_sha256=scenario["observability_evidence_sha256"],
            policy=policy,
        ).to_dict()


def _apply_file_action(
    action: Mapping[str, Any], *, workspace: Path, temp_root: Path
) -> None:
    operation = action["op"]
    relative = _canonical_relative_path(action["path"], "action.path")
    path = workspace / relative
    if operation == "create":
        _exact_keys(action, {"op", "path", "content"}, "action")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x") as stream:
            stream.write(action["content"])
    elif operation == "write":
        _exact_keys(action, {"op", "path", "content"}, "action")
        if not path.is_file() or path.is_symlink():
            raise CalibrationError("FILE_ACTION_TARGET_INVALID", relative)
        path.write_text(action["content"])
    elif operation == "delete":
        _exact_keys(action, {"op", "path"}, "action")
        path.unlink()
    elif operation == "symlink":
        _exact_keys(action, {"op", "path", "target", "target_content"}, "action")
        target_raw = _canonical_relative_path(action["target"], "action.target")
        target = temp_root / target_raw
        if target == workspace or workspace in target.parents:
            raise CalibrationError("SYMLINK_TARGET_MUST_BE_OUTSIDE_WORKSPACE", target_raw)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(action["target_content"])
        path.symlink_to(target)
    else:
        raise CalibrationError("FILE_ACTION_OPERATION_INVALID", repr(operation))


def _validate_matrix_shape(matrix: Mapping[str, Any]) -> None:
    _exact_keys(
        matrix,
        {
            "schema_version",
            "pack_id",
            "candidate_scenarios",
            "file_effect_scenarios",
        },
        "scenario_matrix",
    )
    if matrix["schema_version"] != MATRIX_SCHEMA:
        raise CalibrationError("MATRIX_SCHEMA_UNSUPPORTED", repr(matrix["schema_version"]))
    candidate_ids: list[str] = []
    for index, value in enumerate(_list(matrix["candidate_scenarios"], "candidate_scenarios")):
        row = _mapping(value, f"candidate_scenarios[{index}]")
        _exact_keys(
            row,
            {
                "scenario_id",
                "case_role",
                "candidate_base",
                "acceptable_base",
                "candidate_mutations",
                "acceptable_mutations",
                "expected",
            },
            f"candidate_scenarios[{index}]",
        )
        candidate_ids.append(_identifier(row["scenario_id"], "scenario_id"))
        if row["candidate_base"] not in {"candidate-merge.json", "candidate-reuse.json"}:
            raise CalibrationError("CANDIDATE_BASE_INVALID", repr(row["candidate_base"]))
        if row["acceptable_base"] not in {"acceptable-merge.json", "acceptable-reuse.json"}:
            raise CalibrationError("ACCEPTABLE_BASE_INVALID", repr(row["acceptable_base"]))
        _list(row["candidate_mutations"], "candidate_mutations")
        _list(row["acceptable_mutations"], "acceptable_mutations")
        _validate_expected_candidate(row["expected"])
    file_ids: list[str] = []
    for index, value in enumerate(_list(matrix["file_effect_scenarios"], "file_effect_scenarios")):
        row = _mapping(value, f"file_effect_scenarios[{index}]")
        _exact_keys(
            row,
            {
                "scenario_id",
                "before_files",
                "actions",
                "events",
                "event_observability",
                "observability_evidence_ref",
                "observability_evidence_sha256",
                "policy",
                "expected",
            },
            f"file_effect_scenarios[{index}]",
        )
        file_ids.append(_identifier(row["scenario_id"], "scenario_id"))
        for field in ("before_files", "actions", "events"):
            _list(row[field], field)
        _validate_policy_shape(row["policy"])
        _validate_expected_file(row["expected"])
    all_ids = candidate_ids + file_ids
    if len(all_ids) != len(set(all_ids)):
        raise CalibrationError("SCENARIO_ID_DUPLICATE", repr(all_ids))


def _validate_expected_candidate(value: Any) -> None:
    row = _mapping(value, "expected_candidate")
    _exact_keys(
        row,
        {
            "protocol_verdict",
            "artifact_verdict",
            "anchor_coverage_verdict",
            "typed_path_verdict",
            "temporal_status_verdict",
            "merge_contribution_verdict",
            "forbidden_semantics_verdict",
            "mechanical_scientific_verdict",
            "overall_status",
            "error_codes",
        },
        "expected_candidate",
    )
    _sorted_unique_strings(row["error_codes"], "expected_candidate.error_codes")


def _validate_expected_file(value: Any) -> None:
    row = _mapping(value, "expected_file")
    _exact_keys(
        row,
        {
            "verdict",
            "error_codes",
            "transient_event_paths",
            "unexplained_residual_changes",
        },
        "expected_file",
    )
    for field in ("error_codes", "transient_event_paths", "unexplained_residual_changes"):
        _sorted_unique_strings(row[field], f"expected_file.{field}")


def _validate_policy_shape(value: Any) -> None:
    row = _mapping(value, "policy")
    _exact_keys(
        row,
        {
            "policy_id",
            "allowed_created_paths",
            "allowed_modified_paths",
            "allowed_deleted_paths",
            "allowed_operation_paths",
            "allow_preexisting_symlinks",
        },
        "policy",
    )


def _parse_pointer(value: Any, path: str) -> tuple[str, ...]:
    raw = _string(value, path)
    if not raw.startswith("/") or raw == "/" or raw.endswith("/"):
        raise CalibrationError("JSON_POINTER_INVALID", raw)
    encoded = raw.split("/")[1:]
    if any(not token for token in encoded):
        raise CalibrationError("JSON_POINTER_EMPTY_SEGMENT", raw)
    decoded: list[str] = []
    for token in encoded:
        index = 0
        output = ""
        while index < len(token):
            if token[index] != "~":
                output += token[index]
                index += 1
                continue
            if index + 1 >= len(token) or token[index + 1] not in {"0", "1"}:
                raise CalibrationError("JSON_POINTER_ESCAPE_INVALID", raw)
            output += "~" if token[index + 1] == "0" else "/"
            index += 2
        if output in {"", "..", "-"}:
            raise CalibrationError("JSON_POINTER_SEGMENT_INVALID", raw)
        decoded.append(output)
    reencoded = "/" + "/".join(
        token.replace("~", "~0").replace("/", "~1") for token in decoded
    )
    if reencoded != raw:
        raise CalibrationError("JSON_POINTER_NONCANONICAL", raw)
    return tuple(decoded)


def _resolve_parent(value: Any, tokens: Sequence[str], path: str) -> tuple[Any, str]:
    current = value
    for token in tokens[:-1]:
        if isinstance(current, list):
            current = current[_array_index(token, len(current), path)]
        elif isinstance(current, dict):
            if token not in current:
                raise CalibrationError("MUTATION_TARGET_MISSING", "/".join(tokens))
            current = current[token]
        else:
            raise CalibrationError("MUTATION_PARENT_NOT_CONTAINER", "/".join(tokens))
    return current, tokens[-1]


def _array_index(token: str, length: int, path: str) -> int:
    if not token.isdigit() or (len(token) > 1 and token.startswith("0")):
        raise CalibrationError("JSON_POINTER_ARRAY_INDEX_INVALID", f"{path}:{token}")
    value = int(token)
    if value < 0 or value >= length:
        raise CalibrationError("JSON_POINTER_ARRAY_INDEX_OUT_OF_RANGE", f"{path}:{token}")
    return value


def _canonical_relative_path(value: Any, path: str) -> str:
    raw = _string(value, path)
    pure = PurePosixPath(raw)
    if pure.is_absolute() or raw == "." or ".." in pure.parts or pure.as_posix() != raw:
        raise CalibrationError("RELATIVE_PATH_INVALID", f"{path}:{raw!r}")
    return raw


def _load_json(path: Path, label: str) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise CalibrationError("JSON_FILE_UNSAFE", str(path))
    try:
        value = json.loads(path.read_text(), parse_constant=_reject_nonfinite)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CalibrationError("JSON_INVALID", f"{label}:{exc}") from exc
    return dict(_mapping(value, label))


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
        raise CalibrationError("TYPE_OBJECT_REQUIRED", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise CalibrationError("TYPE_ARRAY_REQUIRED", path)
    return value


def _exact_keys(value: Mapping[str, Any], expected: set[str], path: str) -> None:
    actual = set(value)
    if actual != expected:
        raise CalibrationError(
            "OBJECT_KEYS_INVALID",
            f"{path}:missing={sorted(expected-actual)!r},unknown={sorted(actual-expected)!r}",
        )


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str):
        raise CalibrationError("TYPE_STRING_REQUIRED", path)
    return value


def _sha256(value: Any, path: str) -> str:
    raw = _string(value, path)
    if len(raw) != 64 or any(character not in "0123456789abcdef" for character in raw):
        raise CalibrationError("SHA256_INVALID", f"{path}:{raw!r}")
    return raw


def _identifier(value: Any, path: str) -> str:
    raw = _string(value, path)
    if not raw or any(character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.:-" for character in raw):
        raise CalibrationError("IDENTIFIER_INVALID", f"{path}:{raw!r}")
    return raw


def _integer(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise CalibrationError("TYPE_NONNEGATIVE_INTEGER_REQUIRED", path)
    return value


def _sorted_unique_strings(value: Any, path: str) -> tuple[str, ...]:
    rows = _list(value, path)
    if not all(isinstance(item, str) for item in rows):
        raise CalibrationError("STRING_ARRAY_INVALID", path)
    if rows != sorted(set(rows)):
        raise CalibrationError("STRING_ARRAY_NOT_SORTED_UNIQUE", path)
    return tuple(rows)


def _sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _reject_nonfinite(value: str) -> None:
    raise CalibrationError("JSON_NONFINITE_NUMBER", value)


def main() -> int:
    result = run_calibration_pack()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
