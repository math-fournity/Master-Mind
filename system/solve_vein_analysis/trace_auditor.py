"""Zero-model structural Trace Auditor for solve-side reasoning DAGs.

This module audits already-structured reasoning graphs.  It does not extract
events from natural language and does not judge mathematical correctness.  Its
job is narrower: verify that nonlinear trace evidence such as branches,
failures, revisits and merges is mechanically present in a DAG, and optionally
verify that a State Normalizer sidecar is hash/order compatible with that DAG.

No model, Devin session, Solver, database, Redis, network, or file write is
performed.
"""

from __future__ import annotations

import argparse
import ast
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis import state_normalized_dag as snd


TRACE_AUDIT_SCHEMA_VERSION = "solve-vein/trace-audit/v1"
TRACE_AUDITOR_PROTOCOL_PATH = (
    REPO_ROOT
    / "docs/history/sixth-generation/rnd"
    / "387-v0-2026-08-14-POC-VMS-43-Trace-Auditor结构审计-零模型.md"
)

TRACE_FAMILIES = (
    "LINEAR_PROGRESS",
    "BRANCH_EXPLORATION",
    "FAILED_BRANCH",
    "REVISIT_WITH_NEW_INFORMATION",
    "CROSS_BRANCH_REUSE",
    "TRUE_MERGE",
    "RECOVERY_AFTER_CONTRADICTION",
)
PROGRESS_RELATIONS = {"CONTINUE", "REFINE", "CONCLUDE"}
MERGE_INPUT_RELATIONS = {"MERGE", "REUSE", "DEPENDS_ON"}


class TraceAuditError(RuntimeError):
    """Fail-closed Trace Auditor error."""

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


def audit_reasoning_trace(
    *,
    dag: Mapping[str, Any],
    state_annotation_bundle: Mapping[str, Any] | None = None,
    required_trace_families: tuple[str, ...] = (),
) -> dict[str, Any]:
    dag_root = _dag(dag)
    nodes = _node_index(dag_root)
    edges = _edge_index(dag_root, nodes)
    outgoing, incoming = _adjacency(edges)
    observations = _trace_family_observations(dag_root, nodes, edges, outgoing, incoming)
    sidecar = _sidecar_status(dag_root, state_annotation_bundle)
    required = _required_family_verdict(required_trace_families, observations)
    overall = "PASS" if required["status"] == "PASS" else "FAIL"
    receipt = {
        "schema_version": TRACE_AUDIT_SCHEMA_VERSION,
        "protocol_path": str(TRACE_AUDITOR_PROTOCOL_PATH.relative_to(REPO_ROOT)),
        "protocol_exists_at_build_time": TRACE_AUDITOR_PROTOCOL_PATH.exists(),
        "dag_sha256": sha256_json(dag_root),
        "state_annotation_bundle_sha256": sidecar["bundle_sha256"],
        "node_count": len(nodes),
        "edge_count": len(edges),
        "branch_point_count": len(dag_root["branch_points"]),
        "revisit_event_count": len(dag_root["revisit_events"]),
        "explicit_merge_event_count": len(dag_root["explicit_merge_events"]),
        "trace_family_observations": observations,
        "observed_trace_families": [
            family for family in TRACE_FAMILIES if observations[family]["status"] == "OBSERVED"
        ],
        "required_trace_family_verdict": required,
        "state_sidecar_verdict": sidecar,
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
            "files_written": 0,
        },
        "overall_verdict": overall,
    }
    _verify_receipt(receipt)
    return receipt


def build_demo_complex_trace_audit() -> dict[str, Any]:
    dag = _demo_complex_dag()
    return audit_reasoning_trace(
        dag=dag,
        required_trace_families=(
            "BRANCH_EXPLORATION",
            "FAILED_BRANCH",
            "REVISIT_WITH_NEW_INFORMATION",
            "TRUE_MERGE",
            "RECOVERY_AFTER_CONTRADICTION",
        ),
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
        raise TraceAuditError("FORBIDDEN_IMPORT", ",".join(sorted(forbidden)))
    return tuple(sorted(roots))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo-complex", action="store_true", help="emit a zero-model complex trace audit receipt")
    args = parser.parse_args()
    if not args.demo_complex:
        parser.error("--demo-complex is required for the zero-model CLI demo")
    print(json.dumps(build_demo_complex_trace_audit(), ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _verify_receipt(value: Mapping[str, Any]) -> None:
    if value["schema_version"] != TRACE_AUDIT_SCHEMA_VERSION:
        raise TraceAuditError("TRACE_AUDIT_SCHEMA_MISMATCH", str(value["schema_version"]))
    if value["overall_verdict"] not in {"PASS", "FAIL"}:
        raise TraceAuditError("TRACE_AUDIT_VERDICT_INVALID", str(value["overall_verdict"]))
    if any(value["side_effects"][key] != 0 for key in value["side_effects"]):
        raise TraceAuditError("SIDE_EFFECTS_NONZERO", json.dumps(value["side_effects"], sort_keys=True))
    for family in value["observed_trace_families"]:
        if family not in TRACE_FAMILIES:
            raise TraceAuditError("TRACE_FAMILY_UNKNOWN", str(family))


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
        raise TraceAuditError("DAG_KEYS_INVALID", str(sorted(set(root) ^ expected)))
    if root["schema_version"] != "solve-vein/reasoning-dag/v1":
        raise TraceAuditError("DAG_SCHEMA_MISMATCH", str(root["schema_version"]))
    if root["acyclic"] is not True:
        raise TraceAuditError("DAG_NOT_ACYCLIC", str(root["acyclic"]))
    return root


def _node_index(dag: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for index, raw in enumerate(_list(dag["nodes"], "dag.nodes")):
        node = _mapping(raw, f"dag.nodes[{index}]")
        for key in ("event_id", "sequence_index", "event_kind", "canonical_math_state_id", "attributes", "status"):
            if key not in node:
                raise TraceAuditError("DAG_NODE_KEY_MISSING", f"{index}:{key}")
        event_id = _string(node["event_id"], f"dag.nodes[{index}].event_id")
        if event_id in result:
            raise TraceAuditError("DAG_EVENT_ID_DUPLICATE", event_id)
        result[event_id] = node
    if not result:
        raise TraceAuditError("DAG_NODES_EMPTY", "dag.nodes")
    order = _string_list(dag["topological_order"], "dag.topological_order")
    if set(order) != set(result):
        raise TraceAuditError("DAG_TOPOLOGICAL_ORDER_SET_MISMATCH", "")
    if order[0] != _string(dag["root_event_id"], "dag.root_event_id"):
        raise TraceAuditError("DAG_ROOT_NOT_FIRST_IN_TOPOLOGICAL_ORDER", str(dag["root_event_id"]))
    return result


def _edge_index(
    dag: Mapping[str, Any],
    nodes: Mapping[str, Mapping[str, Any]],
) -> dict[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for index, raw in enumerate(_list(dag["edges"], "dag.edges")):
        edge = _mapping(raw, f"dag.edges[{index}]")
        for key in ("edge_id", "source_event_id", "target_event_id", "relation", "evidence"):
            if key not in edge:
                raise TraceAuditError("DAG_EDGE_KEY_MISSING", f"{index}:{key}")
        edge_id = _string(edge["edge_id"], f"dag.edges[{index}].edge_id")
        if edge_id in result:
            raise TraceAuditError("DAG_EDGE_ID_DUPLICATE", edge_id)
        source = _string(edge["source_event_id"], f"dag.edges[{index}].source_event_id")
        target = _string(edge["target_event_id"], f"dag.edges[{index}].target_event_id")
        if source not in nodes or target not in nodes:
            raise TraceAuditError("DAG_EDGE_ENDPOINT_UNKNOWN", f"{edge_id}:{source}->{target}")
        source_index = _int(nodes[source]["sequence_index"], f"nodes.{source}.sequence_index")
        target_index = _int(nodes[target]["sequence_index"], f"nodes.{target}.sequence_index")
        if source_index >= target_index:
            raise TraceAuditError("DAG_EDGE_NOT_FORWARD", f"{edge_id}:{source}->{target}")
        _string(edge["relation"], f"dag.edges[{index}].relation")
        result[edge_id] = edge
    return result


def _adjacency(edges: Mapping[str, Mapping[str, Any]]) -> tuple[dict[str, list[Mapping[str, Any]]], dict[str, list[Mapping[str, Any]]]]:
    outgoing: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    incoming: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for edge in edges.values():
        outgoing[edge["source_event_id"]].append(edge)
        incoming[edge["target_event_id"]].append(edge)
    return outgoing, incoming


def _trace_family_observations(
    dag: Mapping[str, Any],
    nodes: Mapping[str, Mapping[str, Any]],
    edges: Mapping[str, Mapping[str, Any]],
    outgoing: Mapping[str, list[Mapping[str, Any]]],
    incoming: Mapping[str, list[Mapping[str, Any]]],
) -> dict[str, dict[str, Any]]:
    result = {
        family: {
            "status": "ABSENT",
            "evidence_event_ids": [],
            "evidence_edge_ids": [],
            "rule_id": "",
        }
        for family in TRACE_FAMILIES
    }
    _observe_linear_progress(result, nodes, outgoing)
    branch_points = _string_list(dag["branch_points"], "dag.branch_points")
    if branch_points:
        branch_edges = [
            edge
            for edge in edges.values()
            if edge["source_event_id"] in branch_points and edge["relation"] == "BRANCH_FROM"
        ]
        _set_observed(result, "BRANCH_EXPLORATION", branch_points, [edge["edge_id"] for edge in branch_edges], "TRACE-AUDIT-BRANCH-001")
    failure_events = [
        event_id
        for event_id, node in nodes.items()
        if node["event_kind"] == "FAILURE" or node["status"] in {"ABANDONED", "CONTRADICTED"}
    ]
    failure_edges = [
        edge["edge_id"]
        for edge in edges.values()
        if edge["relation"] in {"CONTRADICT", "ABANDON"}
    ]
    if failure_events or failure_edges:
        _set_observed(result, "FAILED_BRANCH", failure_events, failure_edges, "TRACE-AUDIT-FAILURE-001")
    revisit_events = _string_list(dag["revisit_events"], "dag.revisit_events")
    if revisit_events:
        revisit_edges = [edge["edge_id"] for edge in edges.values() if edge["relation"] == "REVISIT"]
        _set_observed(result, "REVISIT_WITH_NEW_INFORMATION", revisit_events, revisit_edges, "TRACE-AUDIT-REVISIT-001")
    reuse_edges = [
        edge for edge in edges.values() if edge["relation"] in {"REUSE", "DEPENDS_ON"}
    ]
    if reuse_edges:
        _set_observed(
            result,
            "CROSS_BRANCH_REUSE",
            sorted({edge["source_event_id"] for edge in reuse_edges} | {edge["target_event_id"] for edge in reuse_edges}),
            [edge["edge_id"] for edge in reuse_edges],
            "TRACE-AUDIT-REUSE-001",
        )
    merge_events = _string_list(dag["explicit_merge_events"], "dag.explicit_merge_events")
    if merge_events:
        merge_edges = [
            edge["edge_id"]
            for event_id in merge_events
            for edge in incoming[event_id]
            if edge["relation"] in MERGE_INPUT_RELATIONS
        ]
        _set_observed(result, "TRUE_MERGE", merge_events, merge_edges, "TRACE-AUDIT-MERGE-001")
    recovery_edges = [
        edge
        for edge in edges.values()
        if edge["relation"] == "REVISIT"
        and nodes[edge["source_event_id"]]["status"] in {"ABANDONED", "CONTRADICTED"}
    ]
    if recovery_edges:
        _set_observed(
            result,
            "RECOVERY_AFTER_CONTRADICTION",
            sorted({edge["source_event_id"] for edge in recovery_edges} | {edge["target_event_id"] for edge in recovery_edges}),
            [edge["edge_id"] for edge in recovery_edges],
            "TRACE-AUDIT-RECOVERY-001",
        )
    return result


def _observe_linear_progress(
    result: dict[str, dict[str, Any]],
    nodes: Mapping[str, Mapping[str, Any]],
    outgoing: Mapping[str, list[Mapping[str, Any]]],
) -> None:
    order = sorted(nodes, key=lambda event_id: nodes[event_id]["sequence_index"])
    for event_id in order:
        chain_events = [event_id]
        chain_edges: list[str] = []
        current = event_id
        seen = {current}
        while True:
            candidates = [edge for edge in outgoing[current] if edge["relation"] in PROGRESS_RELATIONS]
            if len(candidates) != 1:
                break
            edge = candidates[0]
            target = _string(edge["target_event_id"], "edge.target_event_id")
            if target in seen:
                break
            chain_edges.append(_string(edge["edge_id"], "edge.edge_id"))
            chain_events.append(target)
            seen.add(target)
            current = target
        if len(chain_edges) >= 2:
            _set_observed(result, "LINEAR_PROGRESS", chain_events, chain_edges, "TRACE-AUDIT-LINEAR-001")
            return


def _set_observed(
    result: dict[str, dict[str, Any]],
    family: str,
    event_ids: list[str],
    edge_ids: list[str],
    rule_id: str,
) -> None:
    result[family] = {
        "status": "OBSERVED",
        "evidence_event_ids": sorted(set(event_ids)),
        "evidence_edge_ids": sorted(set(edge_ids)),
        "rule_id": rule_id,
    }


def _sidecar_status(dag: Mapping[str, Any], state_annotation_bundle: Mapping[str, Any] | None) -> dict[str, Any]:
    if state_annotation_bundle is None:
        return {
            "status": "NOT_PROVIDED",
            "bundle_sha256": None,
            "annotated_occurrence_count": 0,
            "missing_from_dag": [],
        }
    bundle = _mapping(state_annotation_bundle, "state_annotation_bundle")
    if bundle.get("schema_version") != snd.STATE_NORMALIZED_DAG_SCHEMA_VERSION:
        raise TraceAuditError("STATE_SIDECAR_SCHEMA_MISMATCH", str(bundle.get("schema_version")))
    if bundle.get("overall_verdict") != "PASS":
        raise TraceAuditError("STATE_SIDECAR_NOT_PASS", str(bundle.get("overall_verdict")))
    dag_sha = sha256_json(dag)
    if bundle.get("dag_sha256") != dag_sha:
        raise TraceAuditError("STATE_SIDECAR_DAG_HASH_MISMATCH", str(bundle.get("dag_sha256")))
    annotated = _string_list(bundle.get("annotated_occurrence_ids"), "state_annotation_bundle.annotated_occurrence_ids")
    order = _string_list(bundle.get("topological_annotation_order"), "state_annotation_bundle.topological_annotation_order")
    dag_order = _string_list(dag["topological_order"], "dag.topological_order")
    expected_order = [event_id for event_id in dag_order if event_id in set(annotated)]
    if order != expected_order:
        raise TraceAuditError("STATE_SIDECAR_ORDER_MISMATCH", str(order))
    missing = sorted(set(annotated) - set(dag_order))
    if missing:
        raise TraceAuditError("STATE_SIDECAR_OCCURRENCE_NOT_IN_DAG", ",".join(missing))
    return {
        "status": "PASS",
        "bundle_sha256": sha256_json(bundle),
        "annotated_occurrence_count": len(annotated),
        "missing_from_dag": [],
    }


def _required_family_verdict(
    required_trace_families: tuple[str, ...],
    observations: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    required = [_string(item, "required_trace_families[]") for item in required_trace_families]
    unknown = sorted(set(required) - set(TRACE_FAMILIES))
    if unknown:
        raise TraceAuditError("REQUIRED_TRACE_FAMILY_UNKNOWN", ",".join(unknown))
    missing = [family for family in required if observations[family]["status"] != "OBSERVED"]
    return {
        "required_trace_families": required,
        "missing_trace_families": missing,
        "status": "PASS" if not missing else "FAIL",
    }


def _demo_complex_dag() -> dict[str, Any]:
    nodes = [
        _demo_node("a0", 0, "DECISION", "root branch point", "root-state", "ACTIVE"),
        _demo_node("b1", 1, "STATE", "first branch", "branch-b", "ACTIVE"),
        _demo_node("c1", 2, "FAILURE", "contradicted branch", "branch-c", "CONTRADICTED"),
        _demo_node("d2", 3, "RETURN", "revisit after contradiction", "branch-c", "ACTIVE"),
        _demo_node("e3", 4, "SYNTHESIS", "merge repaired branch with first branch", "merged-state", "ACTIVE"),
    ]
    edges = [
        _demo_edge("edge-a0-b1", "a0", "b1", "BRANCH_FROM"),
        _demo_edge("edge-a0-c1", "a0", "c1", "BRANCH_FROM"),
        _demo_edge("edge-c1-d2", "c1", "d2", "REVISIT"),
        _demo_edge("edge-b1-e3", "b1", "e3", "MERGE"),
        _demo_edge("edge-d2-e3", "d2", "e3", "MERGE"),
    ]
    return {
        "schema_version": "solve-vein/reasoning-dag/v1",
        "nodes": nodes,
        "edges": edges,
        "topological_order": ["a0", "b1", "c1", "d2", "e3"],
        "root_event_id": "a0",
        "branch_points": ["a0"],
        "revisit_events": ["d2"],
        "explicit_merge_events": ["e3"],
        "unreachable_event_ids": [],
        "acyclic": True,
    }


def _demo_node(event_id: str, sequence_index: int, kind: str, text: str, state: str, status: str) -> dict[str, Any]:
    return {
        "event_id": event_id,
        "sequence_index": sequence_index,
        "event_kind": kind,
        "text": text,
        "canonical_math_state_id": state,
        "attributes": [f"kind:{kind.lower()}", f"status:{status.lower()}"],
        "status": status,
        "source_span": {"start": sequence_index, "end": sequence_index + 1, "sha256": "0" * 64},
        "incoming_edges": [],
    }


def _demo_edge(edge_id: str, source: str, target: str, relation: str) -> dict[str, str]:
    return {
        "edge_id": edge_id,
        "source_event_id": source,
        "target_event_id": target,
        "relation": relation,
        "evidence": "demo",
    }


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise TraceAuditError("EXPECTED_OBJECT", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise TraceAuditError("EXPECTED_LIST", path)
    return value


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value:
        raise TraceAuditError("EXPECTED_STRING", path)
    return value


def _int(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TraceAuditError("EXPECTED_INT", path)
    return value


def _string_list(value: Any, path: str) -> list[str]:
    items = [_string(item, f"{path}[{index}]") for index, item in enumerate(_list(value, path))]
    if len(items) != len(set(items)):
        raise TraceAuditError("DUPLICATE_STRING", path)
    return items


if __name__ == "__main__":
    raise SystemExit(main())
