"""Execute and evaluate the preregistered POC-VMS-32 exactly once per role."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Any, Mapping
import uuid

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.models import ReasoningTrajectory
from system.solve_vein_analysis.pipeline import analyze_trajectory
from system.solve_vein_analysis.role_runtime import (
    DevinRoleSpec,
    RoleInput,
    RoleRuntimeError,
    canonical_json_bytes,
    run_devin_role,
    sha256_file,
)


HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "live_fixtures" / "poc_vms_32"
ASSETS = REPO_ROOT / "system" / "assets" / "solve_vein_analysis"
POC32_PROTOCOL_REF = (
    "第六代系统研发过程文档/"
    "348-v0-2026-08-14-POC-VMS-32-解题侧运行资产-Devin-GLM-5.2-High实测协议.md"
)


TRAJECTORY_CONTRACT = r"""
The exact JSON object has only these fields and shapes:
{
  "schema_version": "solve-vein/reasoning-trajectory/v1",
  "trajectory_id": "poc-vms-32-calibration",
  "problem_id": "poc-vms-32-fibonacci-gcd",
  "source": {
    "carrier": "fixture",
    "source_artifact_ref": "raw_solver_trajectory.txt",
    "source_artifact_sha256": "<sha256 of the complete raw file>"
  },
  "events": [
    {
      "event_id": "e0",
      "sequence_index": 0,
      "event_kind": "STATE|DECISION|FAILURE|RETURN|SYNTHESIS|CONCLUSION",
      "text": "<concise faithful description>",
      "canonical_math_state_id": "state:<stable-slug>",
      "attributes": ["namespace:value"],
      "status": "ACTIVE|ABANDONED|CONTRADICTED|SOLVED|UNKNOWN",
      "source_span": {"start": 0, "end": 1, "sha256": "<sha256>"},
      "incoming_edges": [
        {
          "source_event_id": "e0",
          "relation": "CONTINUE|REFINE|BRANCH_FROM|CONTRADICT|ABANDON|REVISIT|REUSE|DEPENDS_ON|MERGE|CONCLUDE",
          "evidence": "<raw-grounded reason>"
        }
      ]
    }
  ]
}
Unknown keys are forbidden. start/end are zero-based UTF-8 byte offsets into the
raw file, end-exclusive and excluding the line-ending byte. source_span.sha256 is
SHA-256 of exactly raw_bytes[start:end]. Every [NN] line is one occurrence and
must map in order to e0..e9; this fixes occurrence boundaries but does not tell
you the relations or canonical state identities.
""".strip()


def _extractor_task() -> str:
    return f"""Read AGENTS.md first and obey it. Analyze problem.md and
raw_solver_trajectory.txt. Do not solve or improve the problem. The only permitted
output is reasoning-trajectory.json plus the required DONE.md. Use Python locally
if needed to compute byte offsets and SHA-256. Do not inspect any path outside this
workspace.

{TRAJECTORY_CONTRACT}
"""


def _normalizer_task() -> str:
    return f"""Read AGENTS.md first and obey it. Review problem.md,
raw_solver_trajectory.txt, and reasoning-trajectory.json. Produce only
normalized-reasoning-trajectory.json plus DONE.md. Preserve the event history and
correct only evidence-supported normalization mistakes. Do not inspect any path
outside this workspace.

The output must obey this same exact contract:
{TRAJECTORY_CONTRACT}
"""


def _auditor_task() -> str:
    return """Read AGENTS.md first and obey it. Audit candidate-traces.json against
the sealed graph/context/concept/relational files in this workspace. Do not solve
the problem and do not infer process from a final answer. Produce trace-audit.json
with exactly the top-level keys required by AGENTS.md. Each trace_verdicts item must
have exactly:
{
  "trace_id": "<candidate trace id>",
  "verdict": "PASS|FAIL|INCONCLUSIVE",
  "reasons": ["<specific structural reason>"],
  "evidence_refs": ["<event or edge id>"]
}
Every candidate trace must receive exactly one verdict. Then write DONE.md as:
trace-audit.json SHA256=<lowercase-64hex>
Do not inspect any path outside this workspace.
"""


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(), parse_constant=_reject_nonfinite)


def _reject_nonfinite(value: str) -> None:
    raise ValueError(f"non-finite JSON constant: {value}")


def _write_json(path: Path, value: Any) -> None:
    path.write_bytes(
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            indent=2,
        ).encode("utf-8")
        + b"\n"
    )
    path.chmod(0o600)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _edge_spans(trajectory: ReasoningTrajectory) -> set[tuple[int, int, str]]:
    by_id = {event.event_id: event for event in trajectory.events}
    return {
        (
            by_id[edge.source_event_id].source_span.start,
            target.source_span.start,
            edge.relation.value,
        )
        for target in trajectory.events
        for edge in target.incoming_edges
    }


def _span_hash_checks(trajectory: ReasoningTrajectory, raw: bytes) -> list[bool]:
    checks: list[bool] = []
    for event in trajectory.events:
        span = event.source_span
        checks.append(
            span.end <= len(raw)
            and hashlib.sha256(raw[span.start : span.end]).hexdigest() == span.sha256
        )
    return checks


def _receipt_protocol(
    receipt: Mapping[str, Any] | None,
    *,
    expected_sandbox_requested: bool | None = None,
) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if receipt is None:
        return False, ["invocation_receipt_missing"]
    if receipt.get("exit_code") != 0:
        errors.append("devin_exit_nonzero")
    if receipt.get("timed_out") is not False:
        errors.append("devin_timed_out")
    if receipt.get("retry_count") not in {0, 1}:
        errors.append("retry_count_outside_preregistered_limit")
    if receipt.get("model_observability_verdict") != "MATCH":
        errors.append("effective_model_not_exactly_observed")
    if not receipt.get("export_sha256"):
        errors.append("export_missing")
    if receipt.get("export_observation", {}).get("json_valid") is not True:
        errors.append("export_not_parseable_json")
    if not receipt.get("output_sha256"):
        errors.append("role_output_missing")
    if not receipt.get("done_marker_sha256"):
        errors.append("done_marker_missing")
    if receipt.get("done_marker_content_valid") is not True:
        errors.append("done_marker_does_not_commit_output_hash")
    sandbox_requested = receipt.get("sandbox_requested")
    sanitized_argv = receipt.get("sanitized_argv")
    if not isinstance(sandbox_requested, bool):
        errors.append("sandbox_request_not_observable")
    if not isinstance(sanitized_argv, list) or not all(
        isinstance(item, str) for item in sanitized_argv
    ):
        errors.append("sanitized_argv_invalid")
    else:
        if ("--sandbox" in sanitized_argv) != sandbox_requested:
            errors.append("sandbox_flag_receipt_inconsistent")
        if "--resume" in sanitized_argv or "--continue" in sanitized_argv:
            errors.append("session_reuse_flag_forbidden")
    if (
        expected_sandbox_requested is not None
        and sandbox_requested != expected_sandbox_requested
    ):
        errors.append("sandbox_profile_mismatch")
    return not errors, errors


def _observable_cooldown(seconds: int) -> None:
    remaining = seconds
    while remaining > 0:
        chunk = min(30, remaining)
        print(
            f"POC CARRIER_COOLDOWN remaining={remaining}s chunk={chunk}s",
            flush=True,
        )
        time.sleep(chunk)
        remaining -= chunk


def _load_preexecution_freeze_manifest(path: Path, poc_id: str) -> dict[str, Any]:
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"freeze manifest must be a regular file: {path}")
    value = _load_json(path)
    if not isinstance(value, dict):
        raise RuntimeError("freeze manifest must be a JSON object")
    if value.get("schema_version") != "solve-vein/preexecution-freeze-manifest/v1":
        raise RuntimeError("unsupported freeze manifest schema")
    if value.get("poc_id") != poc_id:
        raise RuntimeError(
            f"freeze manifest POC mismatch: {value.get('poc_id')!r} != {poc_id!r}"
        )
    frozen_files = value.get("frozen_files")
    if not isinstance(frozen_files, list) or not frozen_files:
        raise RuntimeError("freeze manifest frozen_files must be nonempty")
    for row in frozen_files:
        if not isinstance(row, dict) or set(row) != {"path", "sha256"}:
            raise RuntimeError("freeze manifest file row has unexpected shape")
        if not isinstance(row["path"], str) or not isinstance(row["sha256"], str):
            raise RuntimeError("freeze manifest file row types are invalid")
        source = REPO_ROOT / row["path"]
        if not source.is_file() or source.is_symlink():
            raise RuntimeError(f"frozen source is unavailable: {row['path']}")
        if sha256_file(source) != row["sha256"]:
            raise RuntimeError(f"frozen source hash mismatch: {row['path']}")
    return value


def evaluate_extractor(
    bundle: Path, *, expected_sandbox_requested: bool | None = None
) -> dict[str, Any]:
    receipt = _load_json(bundle / "invocation-receipt.json")
    protocol_ok, protocol_errors = _receipt_protocol(
        receipt, expected_sandbox_requested=expected_sandbox_requested
    )
    output_path = bundle / "reasoning-trajectory.json"
    raw = (FIXTURES / "raw_solver_trajectory.txt").read_bytes()
    gold = ReasoningTrajectory.from_json_text(
        (FIXTURES / "gold.reasoning-trajectory.json").read_text()
    )
    try:
        candidate = ReasoningTrajectory.from_json_text(output_path.read_text())
        strict_valid = True
        parse_error = None
    except Exception as exc:  # evaluator must preserve arbitrary model failures
        candidate = None
        strict_valid = False
        parse_error = f"{type(exc).__name__}: {exc}"
    if candidate is None:
        metrics = {
            "strict_schema_valid": False,
            "source_artifact_sha256_exact": False,
            "source_spans_byte_exact": False,
            "occurrence_recall": 0.0,
            "typed_edge_recall": 0.0,
            "revisit_occurrence_identity": False,
            "true_merge_two_parent_recall": 0.0,
            "false_merge_count": 0,
        }
        scientific_verdict = "FAIL"
    else:
        gold_starts = {event.source_span.start for event in gold.events}
        candidate_starts = {event.source_span.start for event in candidate.events}
        gold_edges = _edge_spans(gold)
        candidate_edges = _edge_spans(candidate)
        by_start = {event.source_span.start: event for event in candidate.events}
        root = by_start.get(0)
        revisit = by_start.get(336)
        revisit_identity = bool(
            root
            and revisit
            and root.event_id != revisit.event_id
            and root.canonical_math_state_id == revisit.canonical_math_state_id
            and (176, 336, "REVISIT") in candidate_edges
        )
        merge_sources = {
            source
            for source, target, relation in candidate_edges
            if target == 984 and relation == "MERGE"
        }
        false_merge_count = sum(
            1
            for event in candidate.events
            if event.source_span.start != 984
            and any(edge.relation.value == "MERGE" for edge in event.incoming_edges)
        )
        span_checks = _span_hash_checks(candidate, raw)
        metrics = {
            "strict_schema_valid": strict_valid,
            "source_artifact_sha256_exact": (
                candidate.source.source_artifact_sha256
                == hashlib.sha256(raw).hexdigest()
            ),
            "source_spans_byte_exact": bool(span_checks) and all(span_checks),
            "occurrence_recall": len(gold_starts & candidate_starts) / len(gold_starts),
            "typed_edge_recall": len(gold_edges & candidate_edges) / len(gold_edges),
            "revisit_occurrence_identity": revisit_identity,
            "true_merge_two_parent_recall": len({584, 839} & merge_sources) / 2,
            "false_merge_count": false_merge_count,
        }
        critical_ok = all(
            (
                metrics["strict_schema_valid"],
                metrics["source_artifact_sha256_exact"],
                metrics["source_spans_byte_exact"],
                metrics["revisit_occurrence_identity"],
                metrics["true_merge_two_parent_recall"] == 1.0,
                metrics["false_merge_count"] == 0,
            )
        )
        if critical_ok and metrics["occurrence_recall"] == 1.0 and metrics[
            "typed_edge_recall"
        ] >= 0.8:
            scientific_verdict = "PASS"
        elif strict_valid and metrics["occurrence_recall"] > 0:
            scientific_verdict = "PARTIAL"
        else:
            scientific_verdict = "FAIL"
    component_verdict = scientific_verdict if protocol_ok else "INCONCLUSIVE_PROTOCOL"
    return {
        "role": "reasoning_event_extractor",
        "receipt_ref": "reasoning_event_extractor/invocation-receipt.json",
        "receipt_sha256": sha256_file(bundle / "invocation-receipt.json"),
        "protocol_ok": protocol_ok,
        "protocol_errors": protocol_errors,
        "parse_error": parse_error,
        "metrics": metrics,
        "scientific_verdict": scientific_verdict,
        "component_verdict": component_verdict,
    }


def _normalizer_immutable_view(trajectory: ReasoningTrajectory) -> dict[str, Any]:
    return {
        "schema_version": trajectory.schema_version,
        "trajectory_id": trajectory.trajectory_id,
        "problem_id": trajectory.problem_id,
        "source": trajectory.source.to_dict(),
        "events": [
            {
                "event_id": event.event_id,
                "sequence_index": event.sequence_index,
                "event_kind": event.event_kind.value,
                "text": event.text,
                "source_span": event.source_span.to_dict(),
                "edge_sources_and_evidence": [
                    (edge.source_event_id, edge.evidence)
                    for edge in event.incoming_edges
                ],
            }
            for event in trajectory.events
        ],
    }


def evaluate_normalizer(
    bundle: Path, *, expected_sandbox_requested: bool | None = None
) -> dict[str, Any]:
    receipt = _load_json(bundle / "invocation-receipt.json")
    protocol_ok, protocol_errors = _receipt_protocol(
        receipt, expected_sandbox_requested=expected_sandbox_requested
    )
    input_trajectory = ReasoningTrajectory.from_json_text(
        (FIXTURES / "normalizer-input.reasoning-trajectory.json").read_text()
    )
    gold = ReasoningTrajectory.from_json_text(
        (FIXTURES / "gold.reasoning-trajectory.json").read_text()
    )
    output_path = bundle / "normalized-reasoning-trajectory.json"
    try:
        candidate = ReasoningTrajectory.from_json_text(output_path.read_text())
        strict_valid = True
        parse_error = None
    except Exception as exc:
        candidate = None
        strict_valid = False
        parse_error = f"{type(exc).__name__}: {exc}"
    if candidate is None:
        metrics = {
            "strict_schema_valid": False,
            "immutable_event_history_preserved": False,
            "preregistered_corrections_recall": 0.0,
            "unrelated_field_mutation_count": None,
            "invented_event_or_edge_count": None,
        }
        scientific_verdict = "FAIL"
    else:
        candidate_by_id = {event.event_id: event for event in candidate.events}
        corrected = [
            candidate_by_id.get("e2") is not None
            and candidate_by_id["e2"].status.value == "CONTRADICTED",
            candidate_by_id.get("e3") is not None
            and candidate_by_id["e3"].canonical_math_state_id
            == "state:fibonacci-gcd-goal",
            candidate_by_id.get("e7") is not None
            and any(
                edge.source_event_id == "e2" and edge.relation.value == "REUSE"
                for edge in candidate_by_id["e7"].incoming_edges
            ),
        ]
        immutable = _normalizer_immutable_view(candidate) == _normalizer_immutable_view(
            input_trajectory
        )
        exact_gold = candidate.to_dict() == gold.to_dict()
        input_edges = sum(len(event.incoming_edges) for event in input_trajectory.events)
        candidate_edges = sum(len(event.incoming_edges) for event in candidate.events)
        invented_count = abs(len(candidate.events) - len(input_trajectory.events)) + abs(
            candidate_edges - input_edges
        )
        metrics = {
            "strict_schema_valid": strict_valid,
            "immutable_event_history_preserved": immutable,
            "preregistered_corrections_recall": sum(corrected) / len(corrected),
            "unrelated_field_mutation_count": 0 if exact_gold else 1,
            "invented_event_or_edge_count": invented_count,
        }
        if all(
            (
                strict_valid,
                immutable,
                metrics["preregistered_corrections_recall"] == 1.0,
                metrics["unrelated_field_mutation_count"] == 0,
                invented_count == 0,
            )
        ):
            scientific_verdict = "PASS"
        elif strict_valid and immutable and invented_count == 0:
            scientific_verdict = "PARTIAL"
        else:
            scientific_verdict = "FAIL"
    component_verdict = scientific_verdict if protocol_ok else "INCONCLUSIVE_PROTOCOL"
    return {
        "role": "mathematical_state_normalizer",
        "receipt_ref": "mathematical_state_normalizer/invocation-receipt.json",
        "receipt_sha256": sha256_file(bundle / "invocation-receipt.json"),
        "protocol_ok": protocol_ok,
        "protocol_errors": protocol_errors,
        "parse_error": parse_error,
        "metrics": metrics,
        "scientific_verdict": scientific_verdict,
        "component_verdict": component_verdict,
    }


def evaluate_auditor(
    bundle: Path, *, expected_sandbox_requested: bool | None = None
) -> dict[str, Any]:
    receipt = _load_json(bundle / "invocation-receipt.json")
    protocol_ok, protocol_errors = _receipt_protocol(
        receipt, expected_sandbox_requested=expected_sandbox_requested
    )
    output_path = bundle / "trace-audit.json"
    allowed_top = {
        "schema_version",
        "artifact_hashes",
        "trace_verdicts",
        "protocol_violations",
        "overall_verdict",
    }
    try:
        output = _load_json(output_path)
        top_level_valid = (
            isinstance(output, dict)
            and set(output) == allowed_top
            and output.get("schema_version") == "solve-vein/trace-audit/v1"
            and isinstance(output.get("trace_verdicts"), list)
        )
        parse_error = None
    except Exception as exc:
        output = {}
        top_level_valid = False
        parse_error = f"{type(exc).__name__}: {exc}"
    verdicts: dict[str, str] = {}
    inner_valid = top_level_valid
    if top_level_valid:
        for item in output["trace_verdicts"]:
            if (
                not isinstance(item, dict)
                or set(item) != {"trace_id", "verdict", "reasons", "evidence_refs"}
                or item.get("verdict") not in {"PASS", "FAIL", "INCONCLUSIVE"}
                or not isinstance(item.get("trace_id"), str)
                or not isinstance(item.get("reasons"), list)
                or not isinstance(item.get("evidence_refs"), list)
            ):
                inner_valid = False
                continue
            verdicts[item["trace_id"]] = item["verdict"]
    valid_acceptance = verdicts.get("candidate-valid-revisit") == "PASS"
    invalid_rejection = (
        verdicts.get("candidate-invalid-single-parent-merge") == "FAIL"
    )
    metrics = {
        "top_level_contract_valid": top_level_valid and inner_valid,
        "valid_trace_acceptance": 1.0 if valid_acceptance else 0.0,
        "invalid_trace_rejection": 1.0 if invalid_rejection else 0.0,
        "fake_merge_rejected": invalid_rejection,
        "overall_verdict_exact": output.get("overall_verdict") == "FAIL",
    }
    scientific_verdict = (
        "PASS"
        if all(metrics.values())
        else "FAIL"
        if not top_level_valid or not invalid_rejection
        else "PARTIAL"
    )
    component_verdict = scientific_verdict if protocol_ok else "INCONCLUSIVE_PROTOCOL"
    return {
        "role": "process_trace_auditor",
        "receipt_ref": "process_trace_auditor/invocation-receipt.json",
        "receipt_sha256": sha256_file(bundle / "invocation-receipt.json"),
        "protocol_ok": protocol_ok,
        "protocol_errors": protocol_errors,
        "parse_error": parse_error,
        "metrics": metrics,
        "scientific_verdict": scientific_verdict,
        "component_verdict": component_verdict,
    }


def _prepare_auditor_inputs(staging: Path) -> tuple[RoleInput, ...]:
    gold = ReasoningTrajectory.from_json_text(
        (FIXTURES / "gold.reasoning-trajectory.json").read_text()
    )
    bundle = analyze_trajectory(gold)
    payloads = {
        "reasoning-dag.json": bundle.dag.to_dict(),
        "state-context.json": bundle.state_context,
        "transition-context.json": bundle.transition_context,
        "state-concepts.json": bundle.state_concepts,
        "transition-concepts.json": bundle.transition_concepts,
        "relational-scaling.json": bundle.relational_scaling,
    }
    for name, payload in payloads.items():
        _write_json(staging / name, payload)
    rules = """# Frozen trace rules\n\n- TRACE-REVISIT-001 requires two distinct occurrences with the same canonical state, a REVISIT edge, and strictly new attributes.\n- TRACE-MERGE-001 requires a SYNTHESIS target with at least two evidence-bearing MERGE parents. Ordinary linear continuation is not a merge.\n- FCA commonality is descriptive and never creates temporal or causal evidence.\n"""
    (staging / "trace-rules.md").write_text(rules)
    (staging / "trace-rules.md").chmod(0o600)
    inputs = [
        RoleInput(FIXTURES / "problem.md", "problem.md"),
        RoleInput(
            FIXTURES / "auditor-candidate-traces.json", "candidate-traces.json"
        ),
        RoleInput(staging / "trace-rules.md", "trace-rules.md"),
    ]
    inputs.extend(RoleInput(staging / name, name) for name in sorted(payloads))
    return tuple(inputs)


def _render_report_markdown(report: Mapping[str, Any]) -> str:
    lines = [
        f"# {report['poc_id']} result",
        "",
        f"- Overall verdict: **{report['overall_verdict']}**",
        f"- Carrier: `{report['carrier_profile']['carrier']}`",
        f"- Model: `{report['carrier_profile']['requested_model_uid']}`",
        f"- Normalized effort: `{report['carrier_profile']['normalized_effort']}`",
        f"- Sandbox requested: `{report['carrier_profile']['sandbox_requested']}`",
        "- Scientific attempts per role: `1`",
        "- Database connections: `0`",
        "- Solver launches: `0`",
        "",
        "## Components",
        "",
    ]
    for component in report["components"]:
        lines.extend(
            [
                f"### {component['role']}",
                "",
                f"- Component verdict: `{component['component_verdict']}`",
                f"- Scientific verdict: `{component['scientific_verdict']}`",
                f"- Protocol OK: `{component['protocol_ok']}`",
                f"- Metrics: `{json.dumps(component['metrics'], sort_keys=True)}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Boundary",
            "",
            "This is one calibration case per component. It does not establish production,",
            "streaming, cross-domain, Solver-integration, Tell/Hint-effect, or Codex capability.",
            "",
        ]
    )
    return "\n".join(lines)


def run_poc(
    output: Path,
    *,
    poc_id: str = "POC-VMS-32",
    protocol_ref: str = POC32_PROTOCOL_REF,
    infrastructure_retry_of: str | None = None,
    inter_role_cooldown_seconds: int = 0,
    sandbox_requested: bool = True,
    preexecution_freeze_manifest: Path | None = None,
    pass_label: str = "RUNTIME_ASSET_COMPONENTS_PASS_WITHIN_SINGLE_CALIBRATION_CASE",
) -> dict[str, Any]:
    if output.exists() or output.is_symlink():
        raise RuntimeError(f"POC output already exists: {output}")
    if inter_role_cooldown_seconds < 0:
        raise RuntimeError("inter-role cooldown must be nonnegative")
    output.parent.mkdir(parents=True, exist_ok=True)
    partial = output.parent / f".{output.name}.partial-{uuid.uuid4().hex}"
    partial.mkdir(mode=0o700)
    execution_errors: list[dict[str, str]] = []
    try:
        freeze_manifest_sha256: str | None = None
        if preexecution_freeze_manifest is not None:
            freeze_value = _load_preexecution_freeze_manifest(
                preexecution_freeze_manifest, poc_id
            )
            freeze_target = partial / "preexecution-freeze-manifest.json"
            _write_json(freeze_target, freeze_value)
            freeze_manifest_sha256 = sha256_file(freeze_target)
        retry_index = 1 if infrastructure_retry_of else 0
        attempt_prefix = poc_id.lower().replace("-", "_")
        roles: list[tuple[str, DevinRoleSpec]] = [
            (
                "reasoning_event_extractor",
                DevinRoleSpec(
                    attempt_id=f"{attempt_prefix}-extractor-a1",
                    role="reasoning_event_extractor",
                    role_asset_path=ASSETS / "AGENTS_event_extractor.md",
                    task_text=_extractor_task(),
                    inputs=(
                        RoleInput(FIXTURES / "problem.md", "problem.md"),
                        RoleInput(
                            FIXTURES / "raw_solver_trajectory.txt",
                            "raw_solver_trajectory.txt",
                        ),
                    ),
                    expected_output_name="reasoning-trajectory.json",
                    output_bundle=partial / "reasoning_event_extractor",
                    sandbox_requested=sandbox_requested,
                    infrastructure_retry_index=retry_index,
                ),
            ),
            (
                "mathematical_state_normalizer",
                DevinRoleSpec(
                    attempt_id=f"{attempt_prefix}-normalizer-a1",
                    role="mathematical_state_normalizer",
                    role_asset_path=ASSETS / "AGENTS_state_normalizer.md",
                    task_text=_normalizer_task(),
                    inputs=(
                        RoleInput(FIXTURES / "problem.md", "problem.md"),
                        RoleInput(
                            FIXTURES / "raw_solver_trajectory.txt",
                            "raw_solver_trajectory.txt",
                        ),
                        RoleInput(
                            FIXTURES / "normalizer-input.reasoning-trajectory.json",
                            "reasoning-trajectory.json",
                        ),
                    ),
                    expected_output_name="normalized-reasoning-trajectory.json",
                    output_bundle=partial / "mathematical_state_normalizer",
                    sandbox_requested=sandbox_requested,
                    infrastructure_retry_index=retry_index,
                ),
            ),
        ]
        with tempfile.TemporaryDirectory(prefix="solve-vein-auditor-input-") as temp:
            auditor_inputs = _prepare_auditor_inputs(Path(temp))
            roles.append(
                (
                    "process_trace_auditor",
                    DevinRoleSpec(
                        attempt_id=f"{attempt_prefix}-auditor-a1",
                        role="process_trace_auditor",
                        role_asset_path=ASSETS / "AGENTS_trace_auditor.md",
                        task_text=_auditor_task(),
                        inputs=auditor_inputs,
                        expected_output_name="trace-audit.json",
                        output_bundle=partial / "process_trace_auditor",
                        sandbox_requested=sandbox_requested,
                        infrastructure_retry_index=retry_index,
                    ),
                )
            )
            for role_index, (role_name, spec) in enumerate(roles):
                if role_index and inter_role_cooldown_seconds:
                    _observable_cooldown(inter_role_cooldown_seconds)
                print(f"{poc_id} START {role_name}", flush=True)
                try:
                    receipt = run_devin_role(spec)
                    print(
                        f"{poc_id} END {role_name} exit={receipt['exit_code']} "
                        f"model={receipt['model_observability_verdict']}",
                        flush=True,
                    )
                except (RoleRuntimeError, OSError, subprocess.SubprocessError) as exc:
                    execution_errors.append(
                        {"role": role_name, "error": f"{type(exc).__name__}: {exc}"}
                    )
                    print(f"{poc_id} ERROR {role_name}: {exc}", flush=True)

        components: list[dict[str, Any]] = []
        evaluators = (
            ("reasoning_event_extractor", evaluate_extractor),
            ("mathematical_state_normalizer", evaluate_normalizer),
            ("process_trace_auditor", evaluate_auditor),
        )
        for role_name, evaluator in evaluators:
            bundle = partial / role_name
            if bundle.is_dir() and (bundle / "invocation-receipt.json").is_file():
                components.append(
                    evaluator(
                        bundle,
                        expected_sandbox_requested=sandbox_requested,
                    )
                )
            else:
                components.append(
                    {
                        "role": role_name,
                        "receipt_ref": None,
                        "receipt_sha256": None,
                        "protocol_ok": False,
                        "protocol_errors": ["role_bundle_missing"],
                        "parse_error": None,
                        "metrics": {},
                        "scientific_verdict": "NOT_EVALUABLE",
                        "component_verdict": "INCONCLUSIVE_PROTOCOL",
                    }
                )
        verdicts = {component["component_verdict"] for component in components}
        if "INCONCLUSIVE_PROTOCOL" in verdicts:
            overall = "INCONCLUSIVE_PROTOCOL"
        elif "FAIL" in verdicts:
            overall = "FAIL"
        elif "PARTIAL" in verdicts:
            overall = "PARTIAL"
        else:
            overall = pass_label
        report = {
            "schema_version": f"solve-vein/{poc_id.lower()}-report/v1",
            "poc_id": poc_id,
            "protocol_ref": protocol_ref,
            "generated_at": _utc_now(),
            "scope": "SINGLE_CALIBRATION_CASE_PER_COMPONENT",
            "infrastructure_retry_of": infrastructure_retry_of,
            "preexecution_freeze_manifest_ref": (
                "preexecution-freeze-manifest.json"
                if freeze_manifest_sha256 is not None
                else None
            ),
            "preexecution_freeze_manifest_sha256": freeze_manifest_sha256,
            "carrier_profile": {
                "carrier": "devin_cli",
                "requested_model_uid": "glm-5-2",
                "catalog_display_name": "GLM-5.2 High",
                "normalized_effort": "high",
                "effort_encoding": "model_uid",
                "sandbox_requested": sandbox_requested,
                "permission_mode": "dangerous",
                "output_capture": "model_writes_files",
            },
            "components": components,
            "execution_errors": execution_errors,
            "side_effect_accounting": {
                "provider_accepted_scientific_attempts": sum(
                    component["receipt_ref"] is not None for component in components
                ),
                "infrastructure_retry_index": retry_index,
                "inter_role_cooldown_seconds": inter_role_cooldown_seconds,
                "database_connections": 0,
                "redis_connections": 0,
                "solver_launches": 0,
                "absorb_side_files_modified": 0,
            },
            "explicit_nonclaims": [
                "does_not_prove_production_role_capability",
                "does_not_prove_streaming_or_large_scale_capability",
                "does_not_prove_cross_domain_generalization",
                "does_not_prove_codex_carrier_capability",
                "does_not_prove_no_sandbox_strong_isolation",
                "does_not_prove_solver_integration",
                "does_not_prove_tell_or_hint_effect",
                "does_not_authorize_absorb_side_mutation",
            ],
            "overall_verdict": overall,
        }
        _write_json(partial / "poc-report.json", report)
        (partial / "poc-report.md").write_text(_render_report_markdown(report))
        (partial / "poc-report.md").chmod(0o600)
        artifact_hashes = {
            path.relative_to(partial).as_posix(): sha256_file(path)
            for path in sorted(partial.rglob("*"))
            if path.is_file() and path.name != "manifest.json"
        }
        manifest = {
            "schema_version": f"solve-vein/{poc_id.lower()}-manifest/v1",
            "poc_id": poc_id,
            "artifact_hashes": artifact_hashes,
            "overall_verdict": overall,
        }
        _write_json(partial / "manifest.json", manifest)
        os.replace(partial, output)
        return report
    except Exception:
        if partial.exists():
            shutil.rmtree(partial)
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--infrastructure-retry-of")
    parser.add_argument("--poc-id", default="POC-VMS-32")
    parser.add_argument("--protocol-ref", default=POC32_PROTOCOL_REF)
    parser.add_argument("--inter-role-cooldown-seconds", type=int, default=0)
    parser.add_argument("--freeze-manifest", type=Path)
    parser.add_argument(
        "--no-sandbox",
        action="store_true",
        help="omit Devin --sandbox and record DEVIN_SANDBOX=false",
    )
    parser.add_argument(
        "--pass-label",
        default="RUNTIME_ASSET_COMPONENTS_PASS_WITHIN_SINGLE_CALIBRATION_CASE",
    )
    args = parser.parse_args()
    report = run_poc(
        args.output,
        poc_id=args.poc_id,
        protocol_ref=args.protocol_ref,
        infrastructure_retry_of=args.infrastructure_retry_of,
        inter_role_cooldown_seconds=args.inter_role_cooldown_seconds,
        sandbox_requested=not args.no_sandbox,
        preexecution_freeze_manifest=args.freeze_manifest,
        pass_label=args.pass_label,
    )
    print(json.dumps(report, ensure_ascii=False, allow_nan=False, indent=2))
    return 0 if report["overall_verdict"] != "INCONCLUSIVE_PROTOCOL" else 2


if __name__ == "__main__":
    raise SystemExit(main())
