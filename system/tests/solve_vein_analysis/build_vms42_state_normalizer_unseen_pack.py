"""Build the zero-model POC-VMS-42 unseen qualification extension.

The original VMS-42 qualification pack proves the pack/hidden/reviewer/final
receipt seams on the preregistered fixture.  This extension adds a second,
disjoint fixture set and proves that the pack machinery can admit new
State-Normalizer cases without reusing the original case or candidate IDs.

No model, Devin session, Solver, database, Redis, network, or file write is
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

from system.tests.solve_vein_analysis import build_vms42_state_normalizer_pack as pack_builder


UNSEEN_EXTENSION_SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-unseen-extension/v1"
UNSEEN_PACK_ID = "vms42-state-normalizer-unseen-qualification-extension-20260814"
BASE_FIXTURE = (
    REPO_ROOT
    / "system"
    / "tests"
    / "solve_vein_analysis"
    / "state_normalizer_fixtures"
    / "vms42_cases.json"
)
UNSEEN_FIXTURE = (
    REPO_ROOT
    / "system"
    / "tests"
    / "solve_vein_analysis"
    / "state_normalizer_fixtures"
    / "vms42_unseen_cases.json"
)
PROTOCOL_PATH = (
    REPO_ROOT
    / "第六代系统研发过程文档"
    / "385-v0-2026-08-14-POC-VMS-42-State-Normalizer-unseen-qualification-extension-零模型.md"
)
PARENT_PROTOCOLS = (
    "380-v0-2026-08-14-POC-VMS-42-State-Normalizer预注册协议-多轴状态绑定.md",
    "381-v0-2026-08-14-POC-VMS-42-State-Normalizer资格包冻结-零模型.md",
    "382-v0-2026-08-14-POC-VMS-42-State-Normalizer-hidden-join-零模型.md",
    "383-v0-2026-08-14-POC-VMS-42-State-Normalizer-reviewer-judgment-零模型.md",
    "384-v0-2026-08-14-POC-VMS-42-State-Normalizer-final-reviewer-hidden-join-零模型.md",
)
EXPECTED_NONCLAIMS = (
    "DOES_NOT_USE_MODEL_OUTPUT",
    "DOES_NOT_QUALIFY_STATE_EXTRACTOR_PROFILE",
    "DOES_NOT_AUTHORIZE_LIVE_EXECUTION",
    "DOES_NOT_PROVE_STREAMING_OR_INCREMENTAL_NORMALIZATION",
    "DOES_NOT_WRITE_STATE_NORMALIZED_BUNDLE_TO_DAG",
    "DOES_NOT_TOUCH_ABSORB_SIDE_CODE_OR_ASSETS",
)


class VMS42UnseenPackError(RuntimeError):
    """Fail-closed unseen-pack construction error."""

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


def build_vms42_unseen_qualification_extension(
    *,
    base_fixture: Path = BASE_FIXTURE,
    unseen_fixture: Path = UNSEEN_FIXTURE,
) -> dict[str, Any]:
    base_fixture = base_fixture.resolve()
    unseen_fixture = unseen_fixture.resolve()
    base_source = pack_builder.load_source_pack(base_fixture)
    unseen_source = pack_builder.load_source_pack(unseen_fixture)
    base_case_ids = _case_ids(base_source)
    unseen_case_ids = _case_ids(unseen_source)
    overlap = sorted(base_case_ids & unseen_case_ids)
    if overlap:
        raise VMS42UnseenPackError("CASE_ID_OVERLAP_WITH_BASE_FIXTURE", ",".join(overlap))
    base_candidate_ids = _candidate_ids(base_source)
    unseen_candidate_ids = _candidate_ids(unseen_source)
    candidate_overlap = sorted(base_candidate_ids & unseen_candidate_ids)
    if candidate_overlap:
        raise VMS42UnseenPackError("CANDIDATE_ID_OVERLAP_WITH_BASE_FIXTURE", ",".join(candidate_overlap))

    raw_unseen_pack = pack_builder.build_vms42_state_normalizer_pack(unseen_fixture)
    public_manifest = _rewrite_pack_id(raw_unseen_pack["public_manifest"])
    hidden_manifest = _rewrite_pack_id(raw_unseen_pack["hidden_manifest"])
    result = {
        "schema_version": UNSEEN_EXTENSION_SCHEMA_VERSION,
        "extension_id": UNSEEN_PACK_ID,
        "base_fixture_path": str(base_fixture.relative_to(REPO_ROOT)),
        "base_fixture_sha256": sha256_file(base_fixture),
        "unseen_fixture_path": str(unseen_fixture.relative_to(REPO_ROOT)),
        "unseen_fixture_sha256": sha256_file(unseen_fixture),
        "base_case_ids": sorted(base_case_ids),
        "unseen_case_ids": sorted(unseen_case_ids),
        "base_candidate_ids_sha256": sha256_json(sorted(base_candidate_ids)),
        "unseen_candidate_ids_sha256": sha256_json(sorted(unseen_candidate_ids)),
        "parent_protocols": _parent_protocol_refs(),
        "protocol_path": str(PROTOCOL_PATH.relative_to(REPO_ROOT)),
        "protocol_exists_at_build_time": PROTOCOL_PATH.exists(),
        "public_manifest": public_manifest,
        "public_manifest_sha256": sha256_json(public_manifest),
        "hidden_manifest": hidden_manifest,
        "hidden_manifest_sha256": sha256_json(hidden_manifest),
        "reference_check_rows": raw_unseen_pack["reference_check_rows"],
        "negative_check_rows": raw_unseen_pack["negative_check_rows"],
        "case_count": raw_unseen_pack["case_count"],
        "reference_candidate_count": raw_unseen_pack["reference_candidate_count"],
        "negative_candidate_count": raw_unseen_pack["negative_candidate_count"],
        "explicit_nonclaims": list(EXPECTED_NONCLAIMS),
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
            "files_written": 0,
        },
        "profile_qualification_verdict": "DEVELOPMENT_UNSEEN_EXTENSION_PACK_PASS_NOT_LIVE_QUALIFIED",
        "overall_verdict": "PASS",
    }
    _verify_extension_summary(result)
    return result


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
        raise VMS42UnseenPackError("FORBIDDEN_IMPORT", ",".join(sorted(forbidden)))
    return tuple(sorted(roots))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-fixture", type=Path, default=BASE_FIXTURE)
    parser.add_argument("--unseen-fixture", type=Path, default=UNSEEN_FIXTURE)
    args = parser.parse_args()
    result = build_vms42_unseen_qualification_extension(
        base_fixture=args.base_fixture,
        unseen_fixture=args.unseen_fixture,
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _parent_protocol_refs() -> list[dict[str, str]]:
    refs: list[dict[str, str]] = []
    for name in PARENT_PROTOCOLS:
        path = REPO_ROOT / "第六代系统研发过程文档" / name
        refs.append(
            {
                "path": str(path.relative_to(REPO_ROOT)),
                "sha256": sha256_file(path),
            }
        )
    return refs


def _case_ids(source: Mapping[str, Any]) -> set[str]:
    return {str(case["case_id"]) for case in _cases(source)}


def _candidate_ids(source: Mapping[str, Any]) -> set[str]:
    ids: set[str] = set()
    for case in _cases(source):
        for candidate in _list(case["candidates"], f"{case['case_id']}.candidates"):
            root = _mapping(candidate, "candidate")
            ids.add(str(_mapping(root["input"], "candidate.input")["candidate_id"]))
    return ids


def _rewrite_pack_id(manifest: Mapping[str, Any]) -> dict[str, Any]:
    value = deepcopy(dict(manifest))
    value["pack_id"] = UNSEEN_PACK_ID
    return value


def _verify_extension_summary(value: Mapping[str, Any]) -> None:
    if value["schema_version"] != UNSEEN_EXTENSION_SCHEMA_VERSION:
        raise VMS42UnseenPackError("SCHEMA_VERSION_MISMATCH", str(value["schema_version"]))
    if value["overall_verdict"] != "PASS":
        raise VMS42UnseenPackError("OVERALL_VERDICT_NOT_PASS", str(value["overall_verdict"]))
    if any(value["side_effects"][key] != 0 for key in value["side_effects"]):
        raise VMS42UnseenPackError("SIDE_EFFECTS_NONZERO", json.dumps(value["side_effects"], sort_keys=True))
    if set(value["base_case_ids"]) & set(value["unseen_case_ids"]):
        raise VMS42UnseenPackError("CASE_ID_OVERLAP_IN_SUMMARY", "")
    if value["public_manifest"]["pack_id"] != UNSEEN_PACK_ID:
        raise VMS42UnseenPackError("PUBLIC_PACK_ID_MISMATCH", str(value["public_manifest"]["pack_id"]))
    if value["hidden_manifest"]["pack_id"] != UNSEEN_PACK_ID:
        raise VMS42UnseenPackError("HIDDEN_PACK_ID_MISMATCH", str(value["hidden_manifest"]["pack_id"]))
    if value["public_manifest_sha256"] != sha256_json(value["public_manifest"]):
        raise VMS42UnseenPackError("PUBLIC_MANIFEST_HASH_MISMATCH", "")
    if value["hidden_manifest_sha256"] != sha256_json(value["hidden_manifest"]):
        raise VMS42UnseenPackError("HIDDEN_MANIFEST_HASH_MISMATCH", "")
    public_cases = {case["case_id"] for case in value["public_manifest"]["cases"]}
    hidden_cases = {case["case_id"] for case in value["hidden_manifest"]["cases"]}
    if public_cases != hidden_cases or public_cases != set(value["unseen_case_ids"]):
        raise VMS42UnseenPackError("CASE_SET_MISMATCH", f"{public_cases} {hidden_cases}")
    if value["reference_candidate_count"] != len(value["reference_check_rows"]):
        raise VMS42UnseenPackError("REFERENCE_COUNT_MISMATCH", str(value["reference_candidate_count"]))
    if value["negative_candidate_count"] != len(value["negative_check_rows"]):
        raise VMS42UnseenPackError("NEGATIVE_COUNT_MISMATCH", str(value["negative_candidate_count"]))
    if value["reference_candidate_count"] < value["case_count"]:
        raise VMS42UnseenPackError("REFERENCE_COVERAGE_INSUFFICIENT", str(value["reference_candidate_count"]))
    if value["negative_candidate_count"] < value["case_count"]:
        raise VMS42UnseenPackError("NEGATIVE_COVERAGE_INSUFFICIENT", str(value["negative_candidate_count"]))


def _cases(source: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    cases = source.get("cases")
    if not isinstance(cases, list):
        raise VMS42UnseenPackError("CASES_NOT_LIST", "cases")
    return [_mapping(case, f"cases[{index}]") for index, case in enumerate(cases)]


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise VMS42UnseenPackError("EXPECTED_OBJECT", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise VMS42UnseenPackError("EXPECTED_LIST", path)
    return value


if __name__ == "__main__":
    raise SystemExit(main())
