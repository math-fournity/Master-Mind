"""Deterministic graph, FCA, relational-scaling, and trace pipeline."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import replace
from time import perf_counter
from typing import Any, Iterable, Mapping, Sequence

from .fca import (
    FormalContext,
    concepts_to_dict,
    enumerate_concepts,
    object_concept_classes,
    validate_next_closure_against_bruteforce,
)
from .models import (
    AnalysisBundle,
    EdgeRelation,
    EventKind,
    EventStatus,
    GraphEdge,
    ReasoningDag,
    ReasoningEvent,
    ReasoningTrajectory,
    TraceFamily,
    TraceRecord,
    TrajectoryValidationError,
    canonical_json_bytes,
    sha256_json,
)


PIPELINE_VERSION = "solve-vein-pipeline/0.1.0"
TRACE_RULESET_VERSION = "solve-vein-trace-rules/0.1.0"
RELATIONAL_SCALING_VERSION = "solve-vein-rca-style/0.1.0"

PROGRESS_RELATIONS = frozenset(
    {EdgeRelation.CONTINUE, EdgeRelation.REFINE, EdgeRelation.CONCLUDE}
)
BRANCH_PROPAGATION_RELATIONS = frozenset(
    {
        EdgeRelation.CONTINUE,
        EdgeRelation.REFINE,
        EdgeRelation.CONTRADICT,
        EdgeRelation.ABANDON,
        EdgeRelation.REVISIT,
        EdgeRelation.CONCLUDE,
    }
)
MERGE_INPUT_RELATIONS = frozenset(
    {EdgeRelation.MERGE, EdgeRelation.REUSE, EdgeRelation.DEPENDS_ON}
)


def analyze_trajectory(
    trajectory: ReasoningTrajectory,
    *,
    relational_max_iterations: int = 8,
) -> AnalysisBundle:
    """Run the full deterministic analysis over a validated trajectory."""

    total_started = perf_counter()
    stage_started = total_started
    dag = build_reasoning_dag(trajectory)
    graph_seconds = perf_counter() - stage_started

    stage_started = perf_counter()
    state_context = build_state_context(dag)
    transition_context = build_transition_context(dag)
    context_seconds = perf_counter() - stage_started

    stage_started = perf_counter()
    state_concepts = enumerate_concepts(state_context)
    transition_concepts = enumerate_concepts(transition_context)
    state_oracle = validate_next_closure_against_bruteforce(state_context)
    transition_oracle = validate_next_closure_against_bruteforce(transition_context)
    if not state_oracle["equal"] or not transition_oracle["equal"]:
        raise TrajectoryValidationError(
            "FCA_ORACLE_MISMATCH",
            "Next Closure does not equal the independent brute-force oracle",
        )
    base_fca_seconds = perf_counter() - stage_started

    stage_started = perf_counter()
    relational = relational_scale_states(
        state_context,
        dag,
        maximum_iterations=relational_max_iterations,
    )
    relational_seconds = perf_counter() - stage_started

    stage_started = perf_counter()
    traces = extract_traces(dag, state_context)
    trace_seconds = perf_counter() - stage_started

    state_context_payload = state_context.to_dict()
    transition_context_payload = transition_context.to_dict()
    state_concept_payload = concepts_to_dict(
        state_context, state_concepts, validation=state_oracle
    )
    transition_concept_payload = concepts_to_dict(
        transition_context, transition_concepts, validation=transition_oracle
    )
    trace_payload = [trace.to_dict() for trace in traces]
    scientific_payload = {
        "pipeline_version": PIPELINE_VERSION,
        "trace_ruleset_version": TRACE_RULESET_VERSION,
        "trajectory_sha256": trajectory.canonical_sha256,
        "dag": dag.to_dict(),
        "state_context": state_context_payload,
        "transition_context": transition_context_payload,
        "state_concepts": state_concept_payload,
        "transition_concepts": transition_concept_payload,
        "relational_scaling": relational,
        "traces": trace_payload,
    }
    scientific_fingerprint = sha256_json(scientific_payload)
    total_seconds = perf_counter() - total_started
    audit = {
        "schema_version": "solve-vein/audit-report/v1",
        "pipeline_version": PIPELINE_VERSION,
        "trajectory_sha256": trajectory.canonical_sha256,
        "scientific_fingerprint": scientific_fingerprint,
        "checks": {
            "trajectory_valid": True,
            "dag_acyclic": True,
            "unreachable_event_count": len(dag.unreachable_event_ids),
            "edge_evidence_complete": all(bool(edge.evidence) for edge in dag.edges),
            "state_next_closure_equals_bruteforce": state_oracle["equal"],
            "transition_next_closure_equals_bruteforce": transition_oracle["equal"],
            "relational_fixed_point_reached": relational["fixed_point_reached"],
        },
        "verdicts": {
            "pipeline_integrity": "PASS",
            "graph_fidelity": "PASS",
            "fca_closure_correctness": "PASS",
            "relational_scaling": (
                "PASS" if relational["fixed_point_reached"] else "PARTIAL"
            ),
            "live_extraction": "NOT_TESTED",
        },
        "explicit_nonclaims": [
            "does_not_prove_raw_natural_language_trajectory_extraction",
            "does_not_verify_source_span_bytes_against_the_raw_source_artifact",
            "does_not_implement_full_multi_fca_or_complete_rca",
            "does_not_prove_large_scale_performance",
            "does_not_connect_to_solver_database_or_tell_library",
        ],
        "descriptive_cost": {
            "occurrence_count": len(dag.nodes),
            "edge_count": len(dag.edges),
            "state_attribute_count": len(state_context.attributes),
            "transition_attribute_count": len(transition_context.attributes),
            "state_concept_count": len(state_concepts),
            "transition_concept_count": len(transition_concepts),
            "relational_final_concept_count": relational["final_concepts"][
                "concept_count"
            ],
            "relational_iterations": relational["iterations_run"],
            "scientific_payload_bytes": len(canonical_json_bytes(scientific_payload)),
            "wallclock_seconds": {
                "graph": graph_seconds,
                "contexts": context_seconds,
                "base_fca_and_oracle": base_fca_seconds,
                "relational_scaling": relational_seconds,
                "trace_extraction": trace_seconds,
                "total": total_seconds,
            },
            "interpretation": "DESCRIPTIVE_ONLY_NOT_A_SCALE_CLAIM",
        },
    }
    return AnalysisBundle(
        trajectory=trajectory,
        dag=dag,
        state_context=state_context_payload,
        transition_context=transition_context_payload,
        state_concepts=state_concept_payload,
        transition_concepts=transition_concept_payload,
        relational_scaling=relational,
        traces=traces,
        scientific_fingerprint=scientific_fingerprint,
        audit=audit,
    )


def analyze_incrementally(
    trajectory: ReasoningTrajectory,
    *,
    relational_max_iterations: int = 8,
) -> tuple[AnalysisBundle, Mapping[str, Any]]:
    """Replay events one by one, validating every prefix, then analyze the final prefix.

    This is a semantic reference implementation, not an optimized incremental FCA
    algorithm.  It establishes batch/stream equivalence before any optimized update
    algorithm is allowed to replace it.
    """

    prefix_fingerprints: list[dict[str, Any]] = []
    final_bundle: AnalysisBundle | None = None
    for event_count in range(1, len(trajectory.events) + 1):
        prefix = replace(trajectory, events=trajectory.events[:event_count])
        # Construction through the strict parser is intentionally repeated so a
        # hand-built in-memory object cannot bypass prefix validation.
        validated_prefix = ReasoningTrajectory.from_dict(prefix.to_dict())
        prefix_bundle = analyze_trajectory(
            validated_prefix,
            relational_max_iterations=relational_max_iterations,
        )
        prefix_fingerprints.append(
            {
                "event_count": event_count,
                "last_event_id": validated_prefix.events[-1].event_id,
                "scientific_fingerprint": prefix_bundle.scientific_fingerprint,
            }
        )
        final_bundle = prefix_bundle
    if final_bundle is None:  # Defensive; empty trajectories are rejected earlier.
        raise TrajectoryValidationError("TRAJECTORY_EMPTY", "no incremental result")
    journal = {
        "schema_version": "solve-vein/incremental-replay/v1",
        "mode": "correctness_reference_full_prefix_recompute",
        "prefixes": prefix_fingerprints,
        "final_scientific_fingerprint": final_bundle.scientific_fingerprint,
    }
    return final_bundle, journal


def build_reasoning_dag(trajectory: ReasoningTrajectory) -> ReasoningDag:
    event_by_id = {event.event_id: event for event in trajectory.events}
    edges: list[GraphEdge] = []
    for target in trajectory.events:
        ordered_incoming = sorted(
            target.incoming_edges,
            key=lambda edge: (edge.source_event_id, edge.relation.value, edge.evidence),
        )
        semantic_merge_inputs = [
            edge for edge in ordered_incoming if edge.relation in MERGE_INPUT_RELATIONS
        ]
        if any(edge.relation == EdgeRelation.MERGE for edge in ordered_incoming):
            if len({edge.source_event_id for edge in semantic_merge_inputs}) < 2:
                raise TrajectoryValidationError(
                    "MERGE_PARENT_INSUFFICIENT",
                    f"event {target.event_id!r} marks MERGE without two semantic parents",
                )
        for incoming in ordered_incoming:
            identity = {
                "source": incoming.source_event_id,
                "target": target.event_id,
                "relation": incoming.relation.value,
            }
            edges.append(
                GraphEdge(
                    edge_id=f"edge_{sha256_json(identity)[:16]}",
                    source_event_id=incoming.source_event_id,
                    target_event_id=target.event_id,
                    relation=incoming.relation,
                    evidence=incoming.evidence,
                )
            )
    edges.sort(
        key=lambda edge: (
            event_by_id[edge.target_event_id].sequence_index,
            event_by_id[edge.source_event_id].sequence_index,
            edge.relation.value,
        )
    )

    outgoing: dict[str, list[GraphEdge]] = defaultdict(list)
    incoming_by_target: dict[str, list[GraphEdge]] = defaultdict(list)
    for edge in edges:
        outgoing[edge.source_event_id].append(edge)
        incoming_by_target[edge.target_event_id].append(edge)

    branch_points = tuple(
        sorted(
            (
                event_id
                for event_id, event_edges in outgoing.items()
                if len(
                    {
                        edge.target_event_id
                        for edge in event_edges
                        if edge.relation == EdgeRelation.BRANCH_FROM
                    }
                )
                >= 2
            ),
            key=lambda event_id: event_by_id[event_id].sequence_index,
        )
    )
    revisit_events = tuple(
        event.event_id
        for event in trajectory.events
        if any(edge.relation == EdgeRelation.REVISIT for edge in incoming_by_target[event.event_id])
    )
    explicit_merge_events = tuple(
        event.event_id
        for event in trajectory.events
        if len(
            {
                edge.source_event_id
                for edge in incoming_by_target[event.event_id]
                if edge.relation in MERGE_INPUT_RELATIONS
            }
        )
        >= 2
    )

    root = trajectory.events[0].event_id
    reachable = {root}
    queue: deque[str] = deque([root])
    while queue:
        source = queue.popleft()
        for edge in outgoing[source]:
            if edge.target_event_id not in reachable:
                reachable.add(edge.target_event_id)
                queue.append(edge.target_event_id)
    unreachable = tuple(event_id for event_id in event_by_id if event_id not in reachable)
    if unreachable:
        raise TrajectoryValidationError(
            "DAG_UNREACHABLE_EVENT", f"unreachable events: {list(unreachable)!r}"
        )

    return ReasoningDag(
        nodes=trajectory.events,
        edges=tuple(edges),
        topological_order=tuple(event.event_id for event in trajectory.events),
        root_event_id=root,
        branch_points=branch_points,
        revisit_events=revisit_events,
        explicit_merge_events=explicit_merge_events,
        unreachable_event_ids=unreachable,
    )


def build_state_context(dag: ReasoningDag) -> FormalContext:
    incidence: dict[str, set[str]] = {}
    for event in dag.nodes:
        # canonical_math_state_id is deliberately not an FCA attribute.  It is an
        # identity relation used by revisit logic, not a generalizable property.
        incidence[event.event_id] = {
            *event.attributes,
            f"kind:{event.event_kind.value.lower()}",
            f"status:{event.status.value.lower()}",
        }
    return FormalContext.from_incidence("state-context", incidence)


def build_transition_context(dag: ReasoningDag) -> FormalContext:
    event_by_id = {event.event_id: event for event in dag.nodes}
    incidence: dict[str, set[str]] = {}
    for edge in dag.edges:
        source = event_by_id[edge.source_event_id]
        target = event_by_id[edge.target_event_id]
        incidence[edge.edge_id] = {
            f"relation:{edge.relation.value.lower()}",
            f"source_kind:{source.event_kind.value.lower()}",
            f"target_kind:{target.event_kind.value.lower()}",
            f"source_status:{source.status.value.lower()}",
            f"target_status:{target.status.value.lower()}",
        }
    if not incidence:
        # A one-event trajectory is valid at the trajectory layer, but an empty
        # transition context is not useful to this POC and would violate the
        # context contract.
        incidence["edge:none"] = {"relation:none"}
    return FormalContext.from_incidence("transition-context", incidence)


def relational_scale_states(
    base_context: FormalContext,
    dag: ReasoningDag,
    *,
    maximum_iterations: int,
) -> dict[str, Any]:
    if maximum_iterations < 1:
        raise ValueError("maximum_iterations must be positive")
    base_incidence = {
        object_id: set(base_context.incidence[object_id]) for object_id in base_context.objects
    }
    current_context = base_context
    previous_relational: dict[str, tuple[str, ...]] | None = None
    rounds: list[dict[str, Any]] = []
    fixed_point = False

    for iteration in range(maximum_iterations):
        concepts = enumerate_concepts(current_context)
        classes = object_concept_classes(current_context, concepts)
        relational: dict[str, set[str]] = {object_id: set() for object_id in base_context.objects}
        provenance: list[dict[str, str]] = []
        for edge in dag.edges:
            out_attribute = (
                f"rel_out:{edge.relation.value.lower()}:{classes[edge.target_event_id]}"
            )
            in_attribute = (
                f"rel_in:{edge.relation.value.lower()}:{classes[edge.source_event_id]}"
            )
            relational[edge.source_event_id].add(out_attribute)
            relational[edge.target_event_id].add(in_attribute)
            provenance.extend(
                [
                    {
                        "object_id": edge.source_event_id,
                        "attribute": out_attribute,
                        "edge_id": edge.edge_id,
                        "quantifier": "exists_outgoing",
                    },
                    {
                        "object_id": edge.target_event_id,
                        "attribute": in_attribute,
                        "edge_id": edge.edge_id,
                        "quantifier": "exists_incoming",
                    },
                ]
            )
        normalized_relational = {
            object_id: tuple(sorted(attributes))
            for object_id, attributes in sorted(relational.items())
        }
        next_incidence = {
            object_id: base_incidence[object_id] | set(normalized_relational[object_id])
            for object_id in base_context.objects
        }
        next_context = FormalContext.from_incidence(
            f"state-context-relational-{iteration + 1}", next_incidence
        )
        rounds.append(
            {
                "iteration": iteration + 1,
                "input_context_sha256": current_context.canonical_sha256,
                "object_concept_classes": dict(sorted(classes.items())),
                "relational_attributes": normalized_relational,
                "relational_attribute_sha256": sha256_json(normalized_relational),
                "provenance": sorted(
                    provenance,
                    key=lambda item: (item["object_id"], item["attribute"], item["edge_id"]),
                ),
                "output_context_sha256": next_context.canonical_sha256,
            }
        )
        if previous_relational == normalized_relational:
            current_context = next_context
            fixed_point = True
            break
        previous_relational = normalized_relational
        current_context = next_context

    final_concepts = enumerate_concepts(current_context)
    oracle: Mapping[str, Any] | None = None
    if len(current_context.objects) <= 20:
        oracle = validate_next_closure_against_bruteforce(current_context)
        if not oracle["equal"]:
            raise TrajectoryValidationError(
                "RELATIONAL_FCA_ORACLE_MISMATCH", "relational context closure mismatch"
            )
    return {
        "schema_version": "solve-vein/relational-scaling/v1",
        "algorithm_version": RELATIONAL_SCALING_VERSION,
        "maximum_iterations": maximum_iterations,
        "iterations_run": len(rounds),
        "fixed_point_reached": fixed_point,
        "rounds": rounds,
        "final_context": current_context.to_dict(),
        "final_concepts": concepts_to_dict(
            current_context, final_concepts, validation=oracle
        ),
        "explicit_nonclaim": "RCA_STYLE_EXISTENTIAL_SCALING_NOT_FULL_MULTI_FCA",
    }


def extract_traces(dag: ReasoningDag, state_context: FormalContext) -> tuple[TraceRecord, ...]:
    event_by_id = {event.event_id: event for event in dag.nodes}
    edge_by_id = {edge.edge_id: edge for edge in dag.edges}
    outgoing: dict[str, list[GraphEdge]] = defaultdict(list)
    incoming: dict[str, list[GraphEdge]] = defaultdict(list)
    for edge in dag.edges:
        outgoing[edge.source_event_id].append(edge)
        incoming[edge.target_event_id].append(edge)
    for collection in (*outgoing.values(), *incoming.values()):
        collection.sort(
            key=lambda edge: (
                event_by_id[edge.target_event_id].sequence_index,
                event_by_id[edge.source_event_id].sequence_index,
                edge.relation.value,
                edge.edge_id,
            )
        )

    branch_tokens = _compute_branch_tokens(dag)
    traces: list[TraceRecord] = []

    # Maximal unambiguous progress chains.
    progress_incoming_count = {
        event.event_id: sum(edge.relation in PROGRESS_RELATIONS for edge in incoming[event.event_id])
        for event in dag.nodes
    }
    for event in dag.nodes:
        progress_out = [edge for edge in outgoing[event.event_id] if edge.relation in PROGRESS_RELATIONS]
        if not progress_out:
            continue
        if progress_incoming_count[event.event_id] == 1:
            continue
        chain_events = [event.event_id]
        chain_edges: list[str] = []
        current_id = event.event_id
        seen = {current_id}
        while True:
            candidates = [
                edge for edge in outgoing[current_id] if edge.relation in PROGRESS_RELATIONS
            ]
            if len(candidates) != 1:
                break
            edge = candidates[0]
            if progress_incoming_count[edge.target_event_id] != 1:
                break
            if edge.target_event_id in seen:
                break
            chain_edges.append(edge.edge_id)
            chain_events.append(edge.target_event_id)
            seen.add(edge.target_event_id)
            current_id = edge.target_event_id
        if len(chain_edges) >= 2:
            traces.append(
                _make_trace(
                    TraceFamily.LINEAR_PROGRESS,
                    chain_events,
                    chain_edges,
                    state_context,
                    "unambiguous progress chain of length >= 2",
                    "TRACE-LINEAR-001",
                )
            )

    for branch_point in dag.branch_points:
        branch_edges = [
            edge
            for edge in outgoing[branch_point]
            if edge.relation == EdgeRelation.BRANCH_FROM
        ]
        traces.append(
            _make_trace(
                TraceFamily.BRANCH_EXPLORATION,
                [branch_point, *(edge.target_event_id for edge in branch_edges)],
                [edge.edge_id for edge in branch_edges],
                state_context,
                f"{len(branch_edges)} explicit branches from {branch_point}",
                "TRACE-BRANCH-001",
            )
        )

    for event in dag.nodes:
        failure_edges = [
            edge
            for edge in incoming[event.event_id]
            if edge.relation in {EdgeRelation.CONTRADICT, EdgeRelation.ABANDON}
        ]
        if (
            event.event_kind == EventKind.FAILURE
            or event.status in {EventStatus.ABANDONED, EventStatus.CONTRADICTED}
            or failure_edges
        ):
            traces.append(
                _make_trace(
                    TraceFamily.FAILED_BRANCH,
                    [event.event_id],
                    [edge.edge_id for edge in failure_edges],
                    state_context,
                    f"event status={event.status.value}, kind={event.event_kind.value}",
                    "TRACE-FAILURE-001",
                )
            )

    earlier_by_canonical: dict[str, list[ReasoningEvent]] = defaultdict(list)
    for event in dag.nodes:
        revisit_edges = [
            edge for edge in incoming[event.event_id] if edge.relation == EdgeRelation.REVISIT
        ]
        if revisit_edges:
            candidates = earlier_by_canonical[event.canonical_math_state_id]
            if candidates:
                previous = candidates[-1]
                if set(event.attributes) > set(previous.attributes):
                    traces.append(
                        _make_trace(
                            TraceFamily.REVISIT_WITH_NEW_INFORMATION,
                            [previous.event_id, event.event_id],
                            [edge.edge_id for edge in revisit_edges],
                            state_context,
                            "same canonical state revisited with a strict attribute increase",
                            "TRACE-REVISIT-001",
                        )
                    )
            for edge in revisit_edges:
                source = event_by_id[edge.source_event_id]
                if source.event_kind == EventKind.FAILURE or source.status in {
                    EventStatus.ABANDONED,
                    EventStatus.CONTRADICTED,
                }:
                    traces.append(
                        _make_trace(
                            TraceFamily.RECOVERY_AFTER_CONTRADICTION,
                            [source.event_id, event.event_id],
                            [edge.edge_id],
                            state_context,
                            "a contradicted/abandoned occurrence is followed by a revisit",
                            "TRACE-RECOVERY-001",
                        )
                    )
        earlier_by_canonical[event.canonical_math_state_id].append(event)

    for edge in dag.edges:
        if edge.relation not in {EdgeRelation.REUSE, EdgeRelation.DEPENDS_ON}:
            continue
        source_tokens = branch_tokens[edge.source_event_id]
        target_tokens = branch_tokens[edge.target_event_id]
        if source_tokens and target_tokens and source_tokens.isdisjoint(target_tokens):
            traces.append(
                _make_trace(
                    TraceFamily.CROSS_BRANCH_REUSE,
                    [edge.source_event_id, edge.target_event_id],
                    [edge.edge_id],
                    state_context,
                    f"cross-branch {edge.relation.value.lower()} from {sorted(source_tokens)} "
                    f"to {sorted(target_tokens)}",
                    "TRACE-REUSE-001",
                )
            )

    for target_id in dag.explicit_merge_events:
        merge_edges = [
            edge for edge in incoming[target_id] if edge.relation in MERGE_INPUT_RELATIONS
        ]
        source_tokens = {
            token for edge in merge_edges for token in branch_tokens[edge.source_event_id]
        }
        explicit_merge_edge_count = sum(
            edge.relation == EdgeRelation.MERGE for edge in merge_edges
        )
        if len(source_tokens) >= 2 or explicit_merge_edge_count >= 2:
            traces.append(
                _make_trace(
                    TraceFamily.TRUE_MERGE,
                    [*(edge.source_event_id for edge in merge_edges), target_id],
                    [edge.edge_id for edge in merge_edges],
                    state_context,
                    f"{len(merge_edges)} semantic parents from {len(source_tokens)} branch tokens",
                    "TRACE-MERGE-001",
                )
            )

    # Deduplicate by the full evidence identity, then assign deterministic order.
    unique: dict[tuple[Any, ...], TraceRecord] = {}
    for trace in traces:
        identity = (trace.family.value, trace.event_ids, trace.edge_ids, trace.rule_id)
        unique[identity] = trace
    return tuple(
        unique[key]
        for key in sorted(
            unique,
            key=lambda item: (item[0], item[1], item[2], item[3]),
        )
    )


def project_flattened_edges(dag: ReasoningDag) -> tuple[GraphEdge, ...]:
    """Mechanical sequence projection used only as a comparison arm."""

    result: list[GraphEdge] = []
    for previous, current in zip(dag.nodes, dag.nodes[1:], strict=False):
        identity = {
            "source": previous.event_id,
            "target": current.event_id,
            "relation": EdgeRelation.CONTINUE.value,
            "projection": "flattened",
        }
        result.append(
            GraphEdge(
                edge_id=f"flat_{sha256_json(identity)[:16]}",
                source_event_id=previous.event_id,
                target_event_id=current.event_id,
                relation=EdgeRelation.CONTINUE,
                evidence="mechanical chronological flattening",
            )
        )
    return tuple(result)


def project_tree_edges(dag: ReasoningDag) -> tuple[GraphEdge, ...]:
    """Keep exactly one incoming edge per non-root occurrence."""

    priority = {
        EdgeRelation.CONTINUE: 0,
        EdgeRelation.REFINE: 1,
        EdgeRelation.BRANCH_FROM: 2,
        EdgeRelation.CONCLUDE: 3,
        EdgeRelation.REVISIT: 4,
        EdgeRelation.CONTRADICT: 5,
        EdgeRelation.ABANDON: 6,
        EdgeRelation.REUSE: 7,
        EdgeRelation.DEPENDS_ON: 8,
        EdgeRelation.MERGE: 9,
    }
    incoming: dict[str, list[GraphEdge]] = defaultdict(list)
    for edge in dag.edges:
        incoming[edge.target_event_id].append(edge)
    result: list[GraphEdge] = []
    for event in dag.nodes[1:]:
        selected = min(
            incoming[event.event_id],
            key=lambda edge: (priority[edge.relation], edge.source_event_id, edge.edge_id),
        )
        result.append(selected)
    return tuple(result)


def _compute_branch_tokens(dag: ReasoningDag) -> dict[str, frozenset[str]]:
    tokens: dict[str, set[str]] = {event.event_id: set() for event in dag.nodes}
    outgoing: dict[str, list[GraphEdge]] = defaultdict(list)
    for edge in dag.edges:
        outgoing[edge.source_event_id].append(edge)
        if edge.relation == EdgeRelation.BRANCH_FROM:
            tokens[edge.target_event_id].add(
                f"branch:{edge.source_event_id}->{edge.target_event_id}"
            )
    changed = True
    while changed:
        changed = False
        for source_id in dag.topological_order:
            for edge in outgoing[source_id]:
                if edge.relation not in BRANCH_PROPAGATION_RELATIONS:
                    continue
                before = len(tokens[edge.target_event_id])
                tokens[edge.target_event_id].update(tokens[source_id])
                changed = changed or len(tokens[edge.target_event_id]) != before
    return {event_id: frozenset(values) for event_id, values in tokens.items()}


def _make_trace(
    family: TraceFamily,
    event_ids: Iterable[str],
    edge_ids: Iterable[str],
    state_context: FormalContext,
    evidence: str,
    rule_id: str,
) -> TraceRecord:
    canonical_events = tuple(dict.fromkeys(event_ids))
    canonical_edges = tuple(dict.fromkeys(edge_ids))
    shared_intent = tuple(sorted(state_context.object_prime(canonical_events)))
    identity = {
        "family": family.value,
        "event_ids": canonical_events,
        "edge_ids": canonical_edges,
        "rule_id": rule_id,
    }
    return TraceRecord(
        trace_id=f"trace_{sha256_json(identity)[:16]}",
        family=family,
        event_ids=canonical_events,
        edge_ids=canonical_edges,
        shared_intent=shared_intent,
        evidence=evidence,
        rule_id=rule_id,
    )


def edge_identity_set(edges: Sequence[GraphEdge]) -> set[tuple[str, str, str]]:
    return {
        (edge.source_event_id, edge.target_event_id, edge.relation.value) for edge in edges
    }
