"""Attach State Normalizer bindings to a reasoning DAG as an immutable sidecar.

The reasoning DAG remains the source-of-fact trajectory graph.  This module
does not mutate DAG nodes.  It validates a PASS state-normalization evaluation
and emits a state-annotation bundle keyed by DAG event IDs.

No model, Devin session, Solver, database, Redis, network, or file write is
performed.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis import state_normalization as sn


STATE_NORMALIZED_DAG_SCHEMA_VERSION = "solve-vein/state-normalized-dag-annotation-bundle/v1"
PROTOCOL_PATH = (
    REPO_ROOT
    / "docs/history/sixth-generation/rnd"
    / "386-v0-2026-08-14-POC-VMS-42-State-Normalizer-DAG-writeback-sidecar-零模型.md"
)
UNSEEN_FIXTURE = (
    REPO_ROOT
    / "system"
    / "tests"
    / "solve_vein_analysis"
    / "state_normalizer_fixtures"
    / "vms42_unseen_cases.json"
)


class StateNormalizedDagError(RuntimeError):
    """Fail-closed state-normalized DAG annotation error."""

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


def annotate_dag_with_normalized_state(
    *,
    dag: Mapping[str, Any],
    normalized_bundle: Mapping[str, Any],
    evaluation: Mapping[str, Any],
) -> dict[str, Any]:
    dag_root = _dag(dag)
    bundle = _normalized_bundle(normalized_bundle)
    eval_root = _evaluation(evaluation, expected_bundle_sha=sha256_json(bundle))
    event_index = _event_index(dag_root)
    occurrence_ids = _unique_strings(bundle["occurrence_ids"], "normalized_bundle.occurrence_ids")
    unknown = sorted(set(occurrence_ids) - set(event_index))
    if unknown:
        raise StateNormalizedDagError("NORMALIZED_OCCURRENCE_NOT_IN_DAG", ",".join(unknown))
    binding_map = _binding_map(bundle["state_bindings"], set(occurrence_ids))
    legacy_projection = _mapping(bundle["legacy_projection"], "normalized_bundle.legacy_projection")
    annotations: list[dict[str, Any]] = []
    for event_id in dag_root["topological_order"]:
        if event_id not in set(occurrence_ids):
            continue
        event = event_index[event_id]
        axis_bindings = [
            {
                "axis": axis,
                "value_id": value,
                "raw_value": raw_value,
            }
            for axis, value, raw_value in binding_map[event_id]
        ]
        annotations.append(
            {
                "event_id": event_id,
                "sequence_index": event["sequence_index"],
                "canonical_math_state_id": event["canonical_math_state_id"],
                "event_status": event["status"],
                "axis_bindings": axis_bindings,
                "axis_binding_count": len(axis_bindings),
                "legacy_projection": _string(legacy_projection.get(event_id, ""), f"legacy_projection.{event_id}"),
                "annotation_sha256": sha256_json(
                    {
                        "event_id": event_id,
                        "axis_bindings": axis_bindings,
                        "legacy_projection": legacy_projection.get(event_id, ""),
                    }
                ),
            }
        )
    result = {
        "schema_version": STATE_NORMALIZED_DAG_SCHEMA_VERSION,
        "case_id": bundle["case_id"],
        "candidate_id": bundle["candidate_id"],
        "dag_sha256": sha256_json(dag_root),
        "normalized_bundle_sha256": sha256_json(bundle),
        "evaluation_sha256": sha256_json(eval_root),
        "protocol_path": str(PROTOCOL_PATH.relative_to(REPO_ROOT)),
        "protocol_exists_at_build_time": PROTOCOL_PATH.exists(),
        "annotated_occurrence_ids": occurrence_ids,
        "topological_annotation_order": [row["event_id"] for row in annotations],
        "annotation_count": len(annotations),
        "annotations": annotations,
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
            "files_written": 0,
        },
        "overall_verdict": "PASS",
    }
    _verify_annotation_bundle(result)
    return result


def build_demo_unseen_annotation_bundle() -> dict[str, Any]:
    source = json.loads(UNSEEN_FIXTURE.read_text(), parse_constant=_reject_nonfinite)
    case = _mapping(source["cases"][0], "case")
    candidate = _mapping(case["candidates"][0], "candidate")
    normalized = sn.normalize_state_claims(
        candidate["input"],
        case["dictionary"],
        legacy_projection_axes=sn.StateNormalizationAcceptableSet.from_dict(
            case["acceptable_set"]
        ).legacy_projection_axes,
    ).to_dict()
    evaluation = sn.evaluate_state_normalization_value(
        candidate["input"], case["dictionary"], case["acceptable_set"]
    )
    dag = _demo_dag_for_occurrences(candidate["input"]["occurrence_ids"])
    return annotate_dag_with_normalized_state(
        dag=dag,
        normalized_bundle=normalized,
        evaluation=evaluation,
    )


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
        raise StateNormalizedDagError("FORBIDDEN_IMPORT", ",".join(sorted(forbidden)))
    return tuple(sorted(roots))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo-unseen", action="store_true", help="emit a synthetic unseen sidecar receipt")
    args = parser.parse_args()
    if not args.demo_unseen:
        parser.error("--demo-unseen is required for the zero-model CLI demo")
    print(json.dumps(build_demo_unseen_annotation_bundle(), ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _verify_annotation_bundle(value: Mapping[str, Any]) -> None:
    if value["schema_version"] != STATE_NORMALIZED_DAG_SCHEMA_VERSION:
        raise StateNormalizedDagError("ANNOTATION_SCHEMA_MISMATCH", str(value["schema_version"]))
    if value["overall_verdict"] != "PASS":
        raise StateNormalizedDagError("ANNOTATION_VERDICT_NOT_PASS", str(value["overall_verdict"]))
    if value["annotation_count"] != len(value["annotations"]):
        raise StateNormalizedDagError("ANNOTATION_COUNT_MISMATCH", str(value["annotation_count"]))
    if value["topological_annotation_order"] != [row["event_id"] for row in value["annotations"]]:
        raise StateNormalizedDagError("ANNOTATION_ORDER_MISMATCH", "")
    if set(value["annotated_occurrence_ids"]) != set(value["topological_annotation_order"]):
        raise StateNormalizedDagError("ANNOTATED_OCCURRENCE_SET_MISMATCH", "")
    if any(value["side_effects"][key] != 0 for key in value["side_effects"]):
        raise StateNormalizedDagError("SIDE_EFFECTS_NONZERO", json.dumps(value["side_effects"], sort_keys=True))


def _dag(value: Mapping[str, Any]) -> Mapping[str, Any]:
    root = _mapping(value, "dag")
    expected = {
        "schema_version",
        "nodes",
        "edges",
        "topological_order",
        "root_event_id",
        "branch_points",
        "revisit_events",
        "explicit_merge_events",
        "unreachable_event_ids",
        "acyclic",
    }
    if set(root) != expected:
        raise StateNormalizedDagError("DAG_KEYS_INVALID", str(sorted(set(root) ^ expected)))
    if root["schema_version"] != "solve-vein/reasoning-dag/v1":
        raise StateNormalizedDagError("DAG_SCHEMA_MISMATCH", str(root["schema_version"]))
    if root["acyclic"] is not True:
        raise StateNormalizedDagError("DAG_NOT_ACYCLIC", str(root["acyclic"]))
    event_index = _event_index(root)
    order = _unique_strings(root["topological_order"], "dag.topological_order")
    if set(order) != set(event_index):
        raise StateNormalizedDagError("DAG_TOPOLOGICAL_ORDER_SET_MISMATCH", "")
    return root


def _event_index(dag: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    nodes = _list(dag["nodes"], "dag.nodes")
    result: dict[str, Mapping[str, Any]] = {}
    for index, raw in enumerate(nodes):
        node = _mapping(raw, f"dag.nodes[{index}]")
        for key in ("event_id", "sequence_index", "canonical_math_state_id", "status"):
            if key not in node:
                raise StateNormalizedDagError("DAG_NODE_KEY_MISSING", f"{index}:{key}")
        event_id = _string(node["event_id"], f"dag.nodes[{index}].event_id")
        if event_id in result:
            raise StateNormalizedDagError("DAG_EVENT_ID_DUPLICATE", event_id)
        result[event_id] = node
    if not result:
        raise StateNormalizedDagError("DAG_NODES_EMPTY", "dag.nodes")
    return result


def _normalized_bundle(value: Mapping[str, Any]) -> Mapping[str, Any]:
    root = _mapping(value, "normalized_bundle")
    expected = {
        "schema_version",
        "case_id",
        "candidate_id",
        "occurrence_ids",
        "state_bindings",
        "legacy_projection_axes",
        "legacy_projection",
    }
    if set(root) != expected:
        raise StateNormalizedDagError("NORMALIZED_BUNDLE_KEYS_INVALID", str(sorted(set(root) ^ expected)))
    if root["schema_version"] != sn.NORMALIZED_BUNDLE_SCHEMA_VERSION:
        raise StateNormalizedDagError("NORMALIZED_BUNDLE_SCHEMA_MISMATCH", str(root["schema_version"]))
    return root


def _evaluation(value: Mapping[str, Any], *, expected_bundle_sha: str) -> Mapping[str, Any]:
    root = _mapping(value, "evaluation")
    if root.get("schema_version") != sn.EVALUATION_SCHEMA_VERSION:
        raise StateNormalizedDagError("EVALUATION_SCHEMA_MISMATCH", str(root.get("schema_version")))
    if root.get("overall_verdict") != "PASS":
        raise StateNormalizedDagError("EVALUATION_NOT_PASS", str(root.get("overall_verdict")))
    hashes = _mapping(root.get("canonical_input_hashes"), "evaluation.canonical_input_hashes")
    if hashes.get("normalized_bundle_sha256") != expected_bundle_sha:
        raise StateNormalizedDagError("NORMALIZED_BUNDLE_HASH_MISMATCH", str(hashes.get("normalized_bundle_sha256")))
    return root


def _binding_map(bindings_value: Any, occurrence_ids: set[str]) -> dict[str, list[tuple[str, str, str]]]:
    bindings = _list(bindings_value, "normalized_bundle.state_bindings")
    result: dict[str, list[tuple[str, str, str]]] = {occurrence_id: [] for occurrence_id in occurrence_ids}
    seen: set[tuple[str, str]] = set()
    for index, raw in enumerate(bindings):
        item = _mapping(raw, f"state_bindings[{index}]")
        expected = {"occurrence_id", "axis", "value_id", "raw_value"}
        if set(item) != expected:
            raise StateNormalizedDagError("STATE_BINDING_KEYS_INVALID", str(index))
        occurrence_id = _string(item["occurrence_id"], f"state_bindings[{index}].occurrence_id")
        axis = _string(item["axis"], f"state_bindings[{index}].axis")
        key = (occurrence_id, axis)
        if occurrence_id not in occurrence_ids:
            raise StateNormalizedDagError("STATE_BINDING_OCCURRENCE_UNKNOWN", occurrence_id)
        if key in seen:
            raise StateNormalizedDagError("STATE_BINDING_DUPLICATE", f"{occurrence_id}:{axis}")
        seen.add(key)
        result[occurrence_id].append(
            (
                axis,
                _string(item["value_id"], f"state_bindings[{index}].value_id"),
                _string(item["raw_value"], f"state_bindings[{index}].raw_value"),
            )
        )
    for occurrence_id, rows in result.items():
        if not rows:
            raise StateNormalizedDagError("STATE_BINDINGS_MISSING_FOR_OCCURRENCE", occurrence_id)
        rows.sort(key=lambda item: item[0])
    return result


def _demo_dag_for_occurrences(occurrence_ids: list[str]) -> dict[str, Any]:
    nodes = []
    edges = []
    for index, event_id in enumerate(occurrence_ids):
        nodes.append(
            {
                "event_id": event_id,
                "sequence_index": index,
                "event_kind": "STATE",
                "text": f"demo state {event_id}",
                "canonical_math_state_id": "demo-state",
                "attributes": [],
                "status": "ACTIVE",
                "source_span": {"start": index, "end": index + 1, "sha256": "0" * 64},
                "incoming_edges": (
                    []
                    if index == 0
                    else [
                        {
                            "source_event_id": occurrence_ids[index - 1],
                            "relation": "CONTINUE",
                            "evidence": "demo",
                        }
                    ]
                ),
            }
        )
        if index > 0:
            edges.append(
                {
                    "edge_id": f"edge-{occurrence_ids[index - 1]}-{event_id}",
                    "source_event_id": occurrence_ids[index - 1],
                    "target_event_id": event_id,
                    "relation": "CONTINUE",
                    "evidence": "demo",
                }
            )
    return {
        "schema_version": "solve-vein/reasoning-dag/v1",
        "nodes": nodes,
        "edges": edges,
        "topological_order": list(occurrence_ids),
        "root_event_id": occurrence_ids[0],
        "branch_points": [],
        "revisit_events": [],
        "explicit_merge_events": [],
        "unreachable_event_ids": [],
        "acyclic": True,
    }


def _unique_strings(value: Any, path: str) -> list[str]:
    items = [_string(item, f"{path}[{index}]") for index, item in enumerate(_list(value, path))]
    if len(items) != len(set(items)):
        raise StateNormalizedDagError("DUPLICATE_STRING", path)
    return sorted(items)


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise StateNormalizedDagError("EXPECTED_OBJECT", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise StateNormalizedDagError("EXPECTED_LIST", path)
    return value


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str):
        raise StateNormalizedDagError("EXPECTED_STRING", path)
    return value


def _reject_nonfinite(value: str) -> None:
    raise ValueError(f"nonfinite JSON constant forbidden: {value}")


if __name__ == "__main__":
    raise SystemExit(main())
