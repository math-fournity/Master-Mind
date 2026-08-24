"""Build the zero-model POC-VMS-42 state-normalizer qualification pack.

This builder is deliberately small.  VMS-42 already owns the deterministic
state-normalization evaluator; this file freezes the next layer: a public
case manifest that future model extractors may see, plus hidden dictionaries,
acceptable sets, reference candidates and negative checks that only the
mechanical grader may see.

The builder does not write files, call models, start Devin/Solver, connect to
databases, or touch the network.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis import state_normalization as sn


PACK_SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-qualification-pack/v1"
PUBLIC_MANIFEST_SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-public-manifest/v1"
HIDDEN_MANIFEST_SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-hidden-manifest/v1"
PACK_ID = "vms42-state-normalizer-qualification-20260814"
SOURCE_FIXTURE = (
    REPO_ROOT
    / "system"
    / "tests"
    / "solve_vein_analysis"
    / "state_normalizer_fixtures"
    / "vms42_cases.json"
)
PROTOCOL_PATH = (
    REPO_ROOT
    / "docs/history/sixth-generation/rnd"
    / "381-v0-2026-08-14-POC-VMS-42-State-Normalizer资格包冻结-零模型.md"
)
PARENT_PROTOCOL_PATH = (
    REPO_ROOT
    / "docs/history/sixth-generation/rnd"
    / "380-v0-2026-08-14-POC-VMS-42-State-Normalizer预注册协议-多轴状态绑定.md"
)
FORBIDDEN_PUBLIC_KEYS = {
    "acceptable_set",
    "acceptable_set_sha256",
    "candidates",
    "dictionary",
    "dictionary_sha256",
    "expected_verdict",
    "hidden",
    "raw_axis_claims",
    "reference_candidates",
    "state_constraints",
}
EXPECTED_NONCLAIMS = (
    "DOES_NOT_AUTHORIZE_MODEL_OR_DEVIN_EXECUTION",
    "DOES_NOT_QUALIFY_ANY_STATE_EXTRACTOR_PROFILE",
    "DOES_NOT_TEST_STREAMING_OR_INCREMENTAL_NORMALIZATION",
    "DOES_NOT_PROVE_TRACE_TELL_HINT_SELECTION",
    "DOES_NOT_TOUCH_ABSORB_SIDE_CODE_OR_ASSETS",
)


class VMS42PackError(RuntimeError):
    """Fail-closed qualification pack construction or validation error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source_pack(path: Path = SOURCE_FIXTURE) -> dict[str, Any]:
    value = json.loads(path.read_text(), parse_constant=_reject_nonfinite)
    if not isinstance(value, dict):
        raise VMS42PackError("SOURCE_PACK_NOT_OBJECT", str(path))
    evaluation = sn.evaluate_state_normalization_pack(value)
    if evaluation["overall_verdict"] != "PASS":
        raise VMS42PackError("SOURCE_PACK_SELF_CHECK_FAILED", json.dumps(evaluation, ensure_ascii=False))
    return value


def build_vms42_state_normalizer_pack(path: Path = SOURCE_FIXTURE) -> dict[str, Any]:
    source = load_source_pack(path)
    public_cases: list[dict[str, Any]] = []
    hidden_cases: list[dict[str, Any]] = []
    reference_check_rows: list[dict[str, Any]] = []
    negative_check_rows: list[dict[str, Any]] = []

    for case in _cases(source):
        case_id = _identifier(case["case_id"], "case_id")
        acceptable_set = _mapping(case["acceptable_set"], f"{case_id}.acceptable_set")
        dictionary = _mapping(case["dictionary"], f"{case_id}.dictionary")
        candidates = _list(case["candidates"], f"{case_id}.candidates")
        public_case = {
            "schema_version": PUBLIC_MANIFEST_SCHEMA_VERSION,
            "case_id": case_id,
            "expected_occurrence_ids": list(acceptable_set["expected_occurrence_ids"]),
            "required_axes": list(acceptable_set["required_axes"]),
            "legacy_projection_axes": list(acceptable_set["legacy_projection_axes"]),
            "candidate_output_schema": sn.INPUT_SCHEMA_VERSION,
            "hidden_files_forbidden": sorted(FORBIDDEN_PUBLIC_KEYS),
        }
        _assert_public_case_is_clean(public_case)
        public_cases.append(public_case)

        reference_candidates: list[dict[str, str]] = []
        negative_candidates: list[dict[str, str]] = []
        for index, spec in enumerate(candidates):
            spec_root = _mapping(spec, f"{case_id}.candidates[{index}]")
            candidate_input = _mapping(spec_root["input"], f"{case_id}.candidates[{index}].input")
            expected = _verdict(spec_root["expected_verdict"], f"{case_id}.candidates[{index}].expected_verdict")
            evaluation = sn.evaluate_state_normalization_value(candidate_input, dictionary, acceptable_set)
            observed = evaluation["overall_verdict"]
            if observed != expected:
                raise VMS42PackError("EXPECTED_VERDICT_MISMATCH", f"{case_id}:{spec_root['label']}")
            row = {
                "case_id": case_id,
                "label": _identifier(spec_root["label"], f"{case_id}.candidates[{index}].label"),
                "candidate_id": _identifier(candidate_input["candidate_id"], f"{case_id}.candidates[{index}].candidate_id"),
                "candidate_sha256": sha256_json(candidate_input),
                "expected_verdict": expected,
                "observed_verdict": observed,
                "status": "PASS",
            }
            if expected == "PASS":
                reference_candidates.append(row)
                reference_check_rows.append(row)
            else:
                negative_candidates.append(row)
                negative_check_rows.append(row)

        if not reference_candidates:
            raise VMS42PackError("REFERENCE_CANDIDATE_MISSING", case_id)
        if not negative_candidates:
            raise VMS42PackError("NEGATIVE_CANDIDATE_MISSING", case_id)
        hidden_cases.append(
            {
                "schema_version": HIDDEN_MANIFEST_SCHEMA_VERSION,
                "case_id": case_id,
                "dictionary_sha256": sha256_json(dictionary),
                "acceptable_set_sha256": sha256_json(acceptable_set),
                "reference_candidates": reference_candidates,
                "negative_candidates": negative_candidates,
            }
        )

    public_manifest = {
        "schema_version": "solve-vein/vms42-state-normalizer-public-pack/v1",
        "pack_id": PACK_ID,
        "cases": public_cases,
    }
    hidden_manifest = {
        "schema_version": "solve-vein/vms42-state-normalizer-hidden-pack/v1",
        "pack_id": PACK_ID,
        "cases": hidden_cases,
    }
    _assert_public_case_is_clean(public_manifest)
    result = {
        "schema_version": PACK_SCHEMA_VERSION,
        "pack_id": PACK_ID,
        "source_fixture_path": str(path.relative_to(REPO_ROOT)),
        "source_fixture_sha256": sha256_file(path),
        "parent_protocol_path": str(PARENT_PROTOCOL_PATH.relative_to(REPO_ROOT)),
        "parent_protocol_sha256": sha256_file(PARENT_PROTOCOL_PATH),
        "protocol_path": str(PROTOCOL_PATH.relative_to(REPO_ROOT)),
        "protocol_exists_at_build_time": PROTOCOL_PATH.exists(),
        "public_manifest": public_manifest,
        "public_manifest_sha256": sha256_json(public_manifest),
        "hidden_manifest": hidden_manifest,
        "hidden_manifest_sha256": sha256_json(hidden_manifest),
        "reference_check_rows": reference_check_rows,
        "negative_check_rows": negative_check_rows,
        "case_count": len(public_cases),
        "reference_candidate_count": len(reference_check_rows),
        "negative_candidate_count": len(negative_check_rows),
        "explicit_nonclaims": list(EXPECTED_NONCLAIMS),
        "model_calls_authorized": 0,
        "devin_sessions_authorized": 0,
        "database_calls_authorized": 0,
        "solver_calls_authorized": 0,
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
            "files_written": 0,
        },
        "overall_verdict": "PASS",
    }
    _verify_pack_summary(result)
    return result


def _verify_pack_summary(value: Mapping[str, Any]) -> None:
    if value["schema_version"] != PACK_SCHEMA_VERSION:
        raise VMS42PackError("PACK_SCHEMA_MISMATCH", str(value.get("schema_version")))
    if value["overall_verdict"] != "PASS":
        raise VMS42PackError("PACK_VERDICT_NOT_PASS", str(value["overall_verdict"]))
    if any(value["side_effects"][key] != 0 for key in value["side_effects"]):
        raise VMS42PackError("SIDE_EFFECTS_NONZERO", json.dumps(value["side_effects"], sort_keys=True))
    if value["public_manifest_sha256"] != sha256_json(value["public_manifest"]):
        raise VMS42PackError("PUBLIC_MANIFEST_HASH_MISMATCH", "")
    if value["hidden_manifest_sha256"] != sha256_json(value["hidden_manifest"]):
        raise VMS42PackError("HIDDEN_MANIFEST_HASH_MISMATCH", "")
    for public_case in value["public_manifest"]["cases"]:
        _assert_public_case_is_clean(public_case)
    expected_cases = {case["case_id"] for case in value["public_manifest"]["cases"]}
    hidden_cases = {case["case_id"] for case in value["hidden_manifest"]["cases"]}
    if expected_cases != hidden_cases:
        raise VMS42PackError("PUBLIC_HIDDEN_CASE_SET_MISMATCH", f"{expected_cases} != {hidden_cases}")
    if value["case_count"] != len(expected_cases):
        raise VMS42PackError("CASE_COUNT_MISMATCH", str(value["case_count"]))
    if value["reference_candidate_count"] != len(value["reference_check_rows"]):
        raise VMS42PackError("REFERENCE_COUNT_MISMATCH", str(value["reference_candidate_count"]))
    if value["negative_candidate_count"] != len(value["negative_check_rows"]):
        raise VMS42PackError("NEGATIVE_COUNT_MISMATCH", str(value["negative_candidate_count"]))


def assert_no_forbidden_imports(path: Path) -> tuple[str, ...]:
    tree = ast.parse(path.read_text())
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    forbidden = roots & {"arango", "requests", "socket", "subprocess", "urllib"}
    if forbidden:
        raise VMS42PackError("FORBIDDEN_IMPORT", ",".join(sorted(forbidden)))
    return tuple(sorted(roots))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-pack", type=Path, default=SOURCE_FIXTURE)
    args = parser.parse_args()
    result = build_vms42_state_normalizer_pack(args.source_pack)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _cases(source: Mapping[str, Any]) -> Sequence[Mapping[str, Any]]:
    if source.get("schema_version") != "solve-vein/state-normalization-pack/v1":
        raise VMS42PackError("SOURCE_PACK_SCHEMA_MISMATCH", str(source.get("schema_version")))
    cases = _list(source.get("cases"), "cases")
    if not cases:
        raise VMS42PackError("SOURCE_CASES_EMPTY", "cases")
    return tuple(_mapping(case, f"cases[{index}]") for index, case in enumerate(cases))


def _assert_public_case_is_clean(value: Mapping[str, Any]) -> None:
    present = sorted(FORBIDDEN_PUBLIC_KEYS & set(_walk_keys(value)))
    if present:
        raise VMS42PackError("PUBLIC_MANIFEST_LEAKS_HIDDEN_KEY", ",".join(present))


def _walk_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, Mapping):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(_walk_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(_walk_keys(child))
    return keys


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise VMS42PackError("EXPECTED_OBJECT", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise VMS42PackError("EXPECTED_LIST", path)
    return value


def _identifier(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise VMS42PackError("EXPECTED_IDENTIFIER", path)
    return value


def _verdict(value: Any, path: str) -> str:
    if value not in {"PASS", "FAIL", "INVALID"}:
        raise VMS42PackError("EXPECTED_VERDICT", path)
    return str(value)


def _reject_nonfinite(value: str) -> None:
    raise ValueError(f"nonfinite JSON constant forbidden: {value}")


if __name__ == "__main__":
    raise SystemExit(main())
