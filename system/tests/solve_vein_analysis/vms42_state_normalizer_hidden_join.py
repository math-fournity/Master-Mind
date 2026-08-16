"""Zero-model hidden join for POC-VMS-42 state-normalizer candidates.

Future model extractors should only produce a candidate bundle containing
``StateNormalizationInput`` objects.  This module simulates the hidden grader:
it receives the candidate bundle, loads the hidden dictionary/acceptable sets
from the frozen VMS-42 fixture, evaluates each candidate, and emits a receipt.

No model, Devin session, Solver, database, Redis, network or file write is
performed.
"""

from __future__ import annotations

import argparse
import ast
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis import state_normalization as sn
from system.tests.solve_vein_analysis import build_vms42_state_normalizer_pack as pack_builder


CANDIDATE_BUNDLE_SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-candidate-bundle/v1"
HIDDEN_JOIN_SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-hidden-join/v1"
PROTOCOL_PATH = (
    REPO_ROOT
    / "第六代系统研发过程文档"
    / "382-v0-2026-08-14-POC-VMS-42-State-Normalizer-hidden-join-零模型.md"
)
FORBIDDEN_CANDIDATE_BUNDLE_KEYS = {
    "acceptable_set",
    "acceptable_set_sha256",
    "dictionary",
    "dictionary_sha256",
    "expected_verdict",
    "hidden",
    "reference_candidates",
    "state_constraints",
}


class VMS42HiddenJoinError(RuntimeError):
    """Fail-closed hidden-join error."""

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


def build_reference_candidate_bundle() -> dict[str, Any]:
    """Build a development-only candidate bundle from hidden PASS references."""

    pack = pack_builder.build_vms42_state_normalizer_pack()
    source = pack_builder.load_source_pack()
    pass_candidates: list[dict[str, Any]] = []
    for case in source["cases"]:
        case_id = _identifier(case["case_id"], "case_id")
        for candidate in case["candidates"]:
            if candidate["expected_verdict"] == "PASS":
                candidate_input = deepcopy(candidate["input"])
                pass_candidates.append(
                    {
                        "case_id": case_id,
                        "candidate_id": candidate_input["candidate_id"],
                        "candidate_input": candidate_input,
                        "candidate_input_sha256": sha256_json(candidate_input),
                    }
                )
    return {
        "schema_version": CANDIDATE_BUNDLE_SCHEMA_VERSION,
        "pack_id": pack_builder.PACK_ID,
        "public_manifest_sha256": pack["public_manifest_sha256"],
        "candidate_source": "REFERENCE_PASS_CANDIDATES_DEVELOPMENT_ONLY",
        "candidates": pass_candidates,
        "explicit_nonclaims": [
            "DOES_NOT_USE_MODEL_OUTPUT",
            "DOES_NOT_QUALIFY_STATE_EXTRACTOR_PROFILE",
            "DOES_NOT_AUTHORIZE_LIVE_EXECUTION",
        ],
    }


def build_negative_candidate_bundle() -> dict[str, Any]:
    """Build a development-only bundle from hidden non-PASS candidates."""

    pack = pack_builder.build_vms42_state_normalizer_pack()
    source = pack_builder.load_source_pack()
    candidates: list[dict[str, Any]] = []
    for case in source["cases"]:
        case_id = _identifier(case["case_id"], "case_id")
        for candidate in case["candidates"]:
            if candidate["expected_verdict"] != "PASS":
                candidate_input = deepcopy(candidate["input"])
                candidates.append(
                    {
                        "case_id": case_id,
                        "candidate_id": candidate_input["candidate_id"],
                        "candidate_input": candidate_input,
                        "candidate_input_sha256": sha256_json(candidate_input),
                    }
                )
    return {
        "schema_version": CANDIDATE_BUNDLE_SCHEMA_VERSION,
        "pack_id": pack_builder.PACK_ID,
        "public_manifest_sha256": pack["public_manifest_sha256"],
        "candidate_source": "NEGATIVE_CANDIDATES_DEVELOPMENT_ONLY",
        "candidates": candidates,
        "explicit_nonclaims": [
            "DOES_NOT_USE_MODEL_OUTPUT",
            "DOES_NOT_QUALIFY_STATE_EXTRACTOR_PROFILE",
            "DOES_NOT_AUTHORIZE_LIVE_EXECUTION",
        ],
    }


def hidden_join_state_normalizer_candidates(
    candidate_bundle: Mapping[str, Any],
    *,
    source_pack: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    bundle = _candidate_bundle(candidate_bundle)
    pack = pack_builder.build_vms42_state_normalizer_pack()
    if bundle["pack_id"] != pack_builder.PACK_ID:
        raise VMS42HiddenJoinError("PACK_ID_MISMATCH", str(bundle["pack_id"]))
    if bundle["public_manifest_sha256"] != pack["public_manifest_sha256"]:
        raise VMS42HiddenJoinError("PUBLIC_MANIFEST_HASH_MISMATCH", str(bundle["public_manifest_sha256"]))
    _assert_candidate_bundle_has_no_hidden_gold(bundle)

    source = source_pack if source_pack is not None else pack_builder.load_source_pack()
    cases = {_identifier(case["case_id"], "case_id"): case for case in source["cases"]}
    rows: list[dict[str, Any]] = []
    for candidate in bundle["candidates"]:
        candidate_case = _identifier(candidate["case_id"], "candidate.case_id")
        if candidate_case not in cases:
            raise VMS42HiddenJoinError("CANDIDATE_CASE_UNKNOWN", candidate_case)
        candidate_input = _mapping(candidate["candidate_input"], "candidate_input")
        observed_hash = sha256_json(candidate_input)
        if observed_hash != candidate["candidate_input_sha256"]:
            raise VMS42HiddenJoinError("CANDIDATE_INPUT_HASH_MISMATCH", str(candidate["candidate_id"]))
        case = cases[candidate_case]
        evaluation = sn.evaluate_state_normalization_value(
            candidate_input,
            case["dictionary"],
            case["acceptable_set"],
        )
        rows.append(
            {
                "case_id": candidate_case,
                "candidate_id": candidate["candidate_id"],
                "candidate_input_sha256": observed_hash,
                "observed_verdict": evaluation["overall_verdict"],
                "status": "PASS" if evaluation["overall_verdict"] == "PASS" else "FAIL",
                "evaluation_sha256": sha256_json(evaluation),
            }
        )
    all_pass = all(row["status"] == "PASS" for row in rows)
    return {
        "schema_version": HIDDEN_JOIN_SCHEMA_VERSION,
        "pack_id": pack_builder.PACK_ID,
        "candidate_bundle_sha256": sha256_json(bundle),
        "public_manifest_sha256": pack["public_manifest_sha256"],
        "hidden_manifest_sha256": pack["hidden_manifest_sha256"],
        "protocol_path": str(PROTOCOL_PATH.relative_to(REPO_ROOT)),
        "protocol_exists_at_build_time": PROTOCOL_PATH.exists(),
        "candidate_count": len(rows),
        "pass_count": sum(1 for row in rows if row["status"] == "PASS"),
        "fail_count": sum(1 for row in rows if row["status"] != "PASS"),
        "rows": rows,
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
            "files_written": 0,
        },
        "profile_qualification_verdict": (
            "DEVELOPMENT_REFERENCE_JOIN_PASS_NOT_LIVE_QUALIFIED"
            if all_pass
            else "JOIN_FAIL_NOT_QUALIFIED"
        ),
        "overall_verdict": "PASS" if all_pass else "FAIL",
    }


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
        raise VMS42HiddenJoinError("FORBIDDEN_IMPORT", ",".join(sorted(forbidden)))
    return tuple(sorted(roots))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--negative", action="store_true", help="emit a negative development bundle receipt")
    args = parser.parse_args()
    bundle = build_negative_candidate_bundle() if args.negative else build_reference_candidate_bundle()
    receipt = hidden_join_state_normalizer_candidates(bundle)
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _candidate_bundle(value: Mapping[str, Any]) -> Mapping[str, Any]:
    item = _mapping(value, "candidate_bundle")
    expected = {
        "schema_version",
        "pack_id",
        "public_manifest_sha256",
        "candidate_source",
        "candidates",
        "explicit_nonclaims",
    }
    if set(item) != expected:
        raise VMS42HiddenJoinError("CANDIDATE_BUNDLE_KEYS_INVALID", str(sorted(set(item) ^ expected)))
    if item["schema_version"] != CANDIDATE_BUNDLE_SCHEMA_VERSION:
        raise VMS42HiddenJoinError("CANDIDATE_BUNDLE_SCHEMA_MISMATCH", str(item["schema_version"]))
    candidates = _list(item["candidates"], "candidates")
    if not candidates:
        raise VMS42HiddenJoinError("CANDIDATES_EMPTY", "candidates")
    seen: set[tuple[str, str]] = set()
    for index, candidate in enumerate(candidates):
        candidate_root = _mapping(candidate, f"candidates[{index}]")
        candidate_expected = {"case_id", "candidate_id", "candidate_input", "candidate_input_sha256"}
        if set(candidate_root) != candidate_expected:
            raise VMS42HiddenJoinError("CANDIDATE_KEYS_INVALID", str(index))
        pair = (
            _identifier(candidate_root["case_id"], "candidate.case_id"),
            _identifier(candidate_root["candidate_id"], "candidate.candidate_id"),
        )
        if pair in seen:
            raise VMS42HiddenJoinError("CANDIDATE_DUPLICATE", str(pair))
        seen.add(pair)
    return item


def _assert_candidate_bundle_has_no_hidden_gold(value: Mapping[str, Any]) -> None:
    present = sorted(FORBIDDEN_CANDIDATE_BUNDLE_KEYS & set(_walk_keys(value)))
    if present:
        raise VMS42HiddenJoinError("CANDIDATE_BUNDLE_LEAKS_HIDDEN_KEY", ",".join(present))


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
        raise VMS42HiddenJoinError("EXPECTED_OBJECT", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise VMS42HiddenJoinError("EXPECTED_LIST", path)
    return value


def _identifier(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise VMS42HiddenJoinError("EXPECTED_IDENTIFIER", path)
    return value


if __name__ == "__main__":
    raise SystemExit(main())
