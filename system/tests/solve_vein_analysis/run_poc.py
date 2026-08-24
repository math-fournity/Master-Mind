"""Run the preregistered POC-VMS-31 fixture matrix and emit a sealed report."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import sys
import uuid
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.integrity import implementation_tree_receipt, sha256_file
from system.solve_vein_analysis.models import ReasoningTrajectory
from system.solve_vein_analysis.pipeline import (
    PIPELINE_VERSION,
    RELATIONAL_SCALING_VERSION,
    TRACE_RULESET_VERSION,
    analyze_incrementally,
    analyze_trajectory,
    edge_identity_set,
    project_flattened_edges,
    project_tree_edges,
)


HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
PROTOCOL_REF = (
    "docs/history/sixth-generation/rnd/"
    "346-v0-2026-08-14-POC-VMS-31-非线性脉络FCA-RCA对照实验协议.md"
)
CASE_SLUGS = (
    "c1_linear",
    "c2_branch",
    "c3_revisit",
    "c4_merge",
    "c5_composite",
)


def evaluate_case(case_slug: str) -> dict[str, Any]:
    trajectory_path = FIXTURES / f"{case_slug}.trajectory.json"
    expected_path = FIXTURES / f"{case_slug}.expected.json"
    trajectory = ReasoningTrajectory.from_dict(json.loads(trajectory_path.read_text()))
    expected = json.loads(expected_path.read_text())
    batch = analyze_trajectory(trajectory)
    incremental, journal = analyze_incrementally(trajectory)

    full_edges = edge_identity_set(batch.dag.edges)
    gold_edges = {tuple(item) for item in expected["gold_edges"]}
    flattened_edges = edge_identity_set(project_flattened_edges(batch.dag))
    tree_edges = edge_identity_set(project_tree_edges(batch.dag))
    trace_families = {trace.family.value for trace in batch.traces}
    required = set(expected["required_trace_families"])
    forbidden = set(expected["forbidden_trace_families"])
    event_by_id = {event.event_id: event for event in batch.dag.nodes}
    edge_ids = {edge.edge_id for edge in batch.dag.edges}
    event_ids = set(event_by_id)

    revisit_checks = []
    for earlier_id, later_id in expected["revisit_pairs"]:
        later_has_revisit = any(
            edge.target_event_id == later_id and edge.relation.value == "REVISIT"
            for edge in batch.dag.edges
        )
        revisit_checks.append(
            earlier_id != later_id
            and event_by_id[earlier_id].canonical_math_state_id
            == event_by_id[later_id].canonical_math_state_id
            and later_has_revisit
        )
    revisit_identity_recall = (
        sum(revisit_checks) / len(revisit_checks) if revisit_checks else 1.0
    )

    merge_parent_checks: list[bool] = []
    for target_id, parents in expected["merge_parents"].items():
        actual_parents = {
            edge.source_event_id
            for edge in batch.dag.edges
            if edge.target_event_id == target_id and edge.relation.value == "MERGE"
        }
        merge_parent_checks.extend(parent in actual_parents for parent in parents)
    merge_parent_recall = (
        sum(merge_parent_checks) / len(merge_parent_checks)
        if merge_parent_checks
        else 1.0
    )
    expected_merge_targets = set(expected["merge_parents"])
    false_merge_count = len(
        set(batch.dag.explicit_merge_events) - expected_merge_targets
    )
    trace_evidence_valid = all(
        set(trace.event_ids).issubset(event_ids)
        and set(trace.edge_ids).issubset(edge_ids)
        for trace in batch.traces
    )

    exact_graph = full_edges == gold_edges
    trace_contract = required.issubset(trace_families) and forbidden.isdisjoint(
        trace_families
    )
    batch_incremental = (
        batch.scientific_fingerprint == incremental.scientific_fingerprint
        and journal["final_scientific_fingerprint"] == batch.scientific_fingerprint
    )
    closure_oracles = (
        batch.state_concepts["small_context_oracle"]["equal"]
        and batch.transition_concepts["small_context_oracle"]["equal"]
        and batch.relational_scaling["final_concepts"]["small_context_oracle"]["equal"]
    )
    required_trace_recall = (
        len(required & trace_families) / len(required) if required else 1.0
    )
    forbidden_false_positive_count = len(forbidden & trace_families)
    case_pass = all(
        (
            exact_graph,
            trace_contract,
            batch_incremental,
            closure_oracles,
            batch.relational_scaling["fixed_point_reached"],
            revisit_identity_recall == 1.0,
            merge_parent_recall == 1.0,
            false_merge_count == 0,
            trace_evidence_valid,
            not batch.dag.unreachable_event_ids,
        )
    )
    return {
        "case_id": expected["case_id"],
        "trajectory_file": str(trajectory_path.relative_to(HERE.parents[2])),
        "trajectory_sha256": sha256_file(trajectory_path),
        "expected_file": str(expected_path.relative_to(HERE.parents[2])),
        "expected_sha256": sha256_file(expected_path),
        "occurrence_count": len(batch.dag.nodes),
        "gold_edge_count": len(gold_edges),
        "full_dag_edge_count": len(full_edges),
        "typed_edge_recall": len(full_edges & gold_edges) / len(gold_edges),
        "revisit_identity_recall": revisit_identity_recall,
        "merge_parent_recall": merge_parent_recall,
        "false_merge_count": false_merge_count,
        "unreachable_occurrence_count": len(batch.dag.unreachable_event_ids),
        "flattened_exact_edge_recall": len(gold_edges & flattened_edges) / len(gold_edges),
        "tree_exact_edge_recall": len(gold_edges & tree_edges) / len(gold_edges),
        "detected_trace_families": sorted(trace_families),
        "required_trace_families": sorted(required),
        "required_trace_recall": required_trace_recall,
        "forbidden_trace_false_positive_count": forbidden_false_positive_count,
        "trace_evidence_precision": 1.0 if trace_evidence_valid else 0.0,
        "checks": {
            "exact_graph_identity": exact_graph,
            "trace_contract": trace_contract,
            "batch_incremental_equivalence": batch_incremental,
            "next_closure_oracles": closure_oracles,
            "relational_fixed_point": batch.relational_scaling["fixed_point_reached"],
            "revisit_identity": revisit_identity_recall == 1.0,
            "merge_parent_identity": merge_parent_recall == 1.0,
            "false_merge_absent": false_merge_count == 0,
            "trace_evidence_references_exist": trace_evidence_valid,
            "all_occurrences_reachable": not batch.dag.unreachable_event_ids,
        },
        "relational_iterations": batch.relational_scaling["iterations_run"],
        "descriptive_cost": batch.audit["descriptive_cost"],
        "scientific_fingerprint": batch.scientific_fingerprint,
        "verdict": "PASS" if case_pass else "FAIL",
    }


def build_report() -> dict[str, Any]:
    cases = [evaluate_case(case_slug) for case_slug in CASE_SLUGS]
    pass_count = sum(case["verdict"] == "PASS" for case in cases)
    non_linear_cases = [case for case in cases if case["case_id"] != "C1_LINEAR"]
    tree_losses = [
        1.0 - case["tree_exact_edge_recall"] for case in non_linear_cases
    ]
    flattened_losses = [
        1.0 - case["flattened_exact_edge_recall"] for case in non_linear_cases
    ]
    verdict = "PASS" if pass_count == len(cases) else "FAIL"
    return {
        "schema_version": "solve-vein/poc-vms-31-report/v1",
        "poc_id": "POC-VMS-31",
        "protocol_ref": PROTOCOL_REF,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "execution_mode": "OFFLINE_CANONICAL_TRAJECTORY_FIXTURES",
        "implementation": {
            "pipeline_version": PIPELINE_VERSION,
            "trace_ruleset_version": TRACE_RULESET_VERSION,
            "relational_scaling_version": RELATIONAL_SCALING_VERSION,
            "tree_receipt": implementation_tree_receipt(
                extra_files=(Path(__file__).resolve(),)
            ),
        },
        "cases": cases,
        "summary": {
            "case_count": len(cases),
            "pass_count": pass_count,
            "exact_graph_pass_count": sum(
                case["checks"]["exact_graph_identity"] for case in cases
            ),
            "batch_incremental_pass_count": sum(
                case["checks"]["batch_incremental_equivalence"] for case in cases
            ),
            "tree_information_loss_case_count_non_linear": sum(
                loss > 0 for loss in tree_losses
            ),
            "maximum_tree_information_loss_non_linear": max(tree_losses),
            "mean_tree_information_loss_non_linear": sum(tree_losses) / len(tree_losses),
            "flattened_information_loss_case_count_non_linear": sum(
                loss > 0 for loss in flattened_losses
            ),
            "minimum_flattened_information_loss_non_linear": min(flattened_losses),
            "mean_flattened_information_loss_non_linear": (
                sum(flattened_losses) / len(flattened_losses)
            ),
            "live_model_calls": 0,
            "database_connections": 0,
            "solver_launches": 0,
        },
        "claims": {
            "canonical_graph_reconstruction": "SUPPORTED_WITHIN_FIXTURE_SCOPE",
            "fca_closure_correctness": "SUPPORTED_WITHIN_SMALL_CONTEXT_SCOPE",
            "batch_incremental_semantic_equivalence": "SUPPORTED_WITHIN_FIXTURE_SCOPE",
            "tree_and_flattened_projection_loss": "OBSERVED_ON_NON_LINEAR_FIXTURES",
            "raw_thinking_extraction": "NOT_TESTED",
            "live_solver_integration": "NOT_TESTED",
            "large_scale_performance": "NOT_TESTED",
            "full_rca_or_multi_fca": "NOT_CLAIMED",
        },
        "verdict": verdict,
    }


def write_report(output: Path, report: dict[str, Any]) -> None:
    if output.exists() or output.is_symlink():
        raise RuntimeError(f"output already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    partial = output.parent / f".{output.name}.partial-{uuid.uuid4().hex}"
    partial.mkdir(mode=0o700)
    try:
        json_path = partial / "poc-report.json"
        markdown_path = partial / "poc-report.md"
        json_path.write_text(
            json.dumps(report, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True)
            + "\n"
        )
        markdown_path.write_text(render_markdown(report))
        manifest = {
            "schema_version": "solve-vein/poc-result-manifest/v1",
            "poc_report_sha256": sha256_file(json_path),
            "markdown_report_sha256": sha256_file(markdown_path),
            "verdict": report["verdict"],
        }
        (partial / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True)
            + "\n"
        )
        for path in partial.iterdir():
            with path.open("rb") as handle:
                os.fsync(handle.fileno())
        directory_fd = os.open(partial, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        os.replace(partial, output)
        parent_fd = os.open(output.parent, os.O_RDONLY)
        try:
            os.fsync(parent_fd)
        finally:
            os.close(parent_fd)
    except Exception:
        if partial.exists():
            shutil.rmtree(partial)
        raise


def render_markdown(report: dict[str, Any]) -> str:
    rows = [
        "# POC-VMS-31 machine result",
        "",
        f"Overall verdict: **{report['verdict']}**",
        "",
        "| Case | DAG | traces | batch=incremental | tree recall | flat recall |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for case in report["cases"]:
        rows.append(
            "| {case_id} | {dag} | {traces} | {incremental} | {tree:.3f} | {flat:.3f} |".format(
                case_id=case["case_id"],
                dag="PASS" if case["checks"]["exact_graph_identity"] else "FAIL",
                traces="PASS" if case["checks"]["trace_contract"] else "FAIL",
                incremental=(
                    "PASS" if case["checks"]["batch_incremental_equivalence"] else "FAIL"
                ),
                tree=case["tree_exact_edge_recall"],
                flat=case["flattened_exact_edge_recall"],
            )
        )
    rows.extend(
        [
            "",
            "This POC starts from frozen structured event trajectories. Raw Solver-thinking",
            "extraction, live model execution, database integration, and large-scale",
            "performance remain NOT_TESTED.",
            "",
        ]
    )
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        report = build_report()
        write_report(args.output, report)
        print(json.dumps({"output": str(args.output), "verdict": report["verdict"]}))
        return 0 if report["verdict"] == "PASS" else 1
    except (OSError, RuntimeError, ValueError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
