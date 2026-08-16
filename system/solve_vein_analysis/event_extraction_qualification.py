"""Fail-closed qualification contracts for solve-side event extraction.

The candidate model emits the existing ``ReasoningTrajectory/v1`` object.  It
never sees the acceptable set in this module's caller.  The deterministic
grader aligns candidate events to hidden semantic anchors through unique UTF-8
witness spans, then checks source fidelity, event labels, allowed edges, and
true-merge parent cardinality.  A mechanical PASS intentionally remains
``PENDING_MANUAL_AUDIT``; this module cannot self-certify semantic fidelity.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import hashlib
import json
import re
from typing import Any, Mapping

from .models import (
    EdgeRelation,
    EventKind,
    EventStatus,
    ReasoningTrajectory,
    TrajectorySource,
    TrajectoryValidationError,
)


PACK_SCHEMA_VERSION = "solve-vein/event-extraction-acceptable-set-pack/v1"
ACCEPTABLE_SET_SCHEMA_VERSION = "solve-vein/event-extraction-acceptable-set/v1"
EVALUATION_SCHEMA_VERSION = "solve-vein/event-extraction-evaluation/v1"
IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class QualificationValidationError(ValueError):
    """Fail-closed protocol or acceptable-set error with a stable code."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


class MechanicalVerdict(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    INVALID = "INVALID"


class OverallQualificationStatus(StrEnum):
    PENDING_MANUAL_AUDIT = "PENDING_MANUAL_AUDIT"
    FAIL = "FAIL"
    INVALID = "INVALID"


@dataclass(frozen=True, slots=True)
class Anchor:
    anchor_id: str
    unique_witness_text: str
    allowed_event_kinds: tuple[EventKind, ...]
    allowed_statuses: tuple[EventStatus, ...]


@dataclass(frozen=True, slots=True)
class EdgeClause:
    clause_id: str
    source_anchor_id: str
    target_anchor_id: str
    allowed_relations: tuple[EdgeRelation, ...]
    required: bool


@dataclass(frozen=True, slots=True)
class ForbiddenEdge:
    source_anchor_id: str
    target_anchor_id: str
    forbidden_relations: tuple[EdgeRelation, ...]


@dataclass(frozen=True, slots=True)
class MergeConstraint:
    target_anchor_id: str
    minimum_distinct_parent_anchors: int
    required_parent_anchor_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class EventExtractionAcceptableSet:
    acceptable_set_id: str
    case_id: str
    problem_id: str
    trajectory_id: str
    source: TrajectorySource
    expected_event_count: int
    anchors: tuple[Anchor, ...]
    edge_clauses: tuple[EdgeClause, ...]
    forbidden_relations: tuple[EdgeRelation, ...]
    forbidden_edges: tuple[ForbiddenEdge, ...]
    merge_constraints: tuple[MergeConstraint, ...]

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "EventExtractionAcceptableSet":
        root = _mapping(value, "acceptable_set")
        _exact_keys(
            root,
            {
                "schema_version",
                "acceptable_set_id",
                "case_id",
                "problem_id",
                "trajectory_id",
                "source",
                "expected_event_count",
                "anchors",
                "edge_clauses",
                "forbidden_relations",
                "forbidden_edges",
                "merge_constraints",
            },
            "acceptable_set",
        )
        if _string(root["schema_version"], "schema_version") != ACCEPTABLE_SET_SCHEMA_VERSION:
            raise QualificationValidationError(
                "ACCEPTABLE_SET_SCHEMA_UNSUPPORTED",
                f"expected {ACCEPTABLE_SET_SCHEMA_VERSION!r}",
            )
        expected_event_count = _integer(
            root["expected_event_count"], "expected_event_count"
        )
        if expected_event_count <= 0:
            raise QualificationValidationError(
                "EXPECTED_EVENT_COUNT_INVALID", "expected_event_count must be positive"
            )
        anchors = tuple(
            _parse_anchor(item, index)
            for index, item in enumerate(_list(root["anchors"], "anchors"))
        )
        if len(anchors) != expected_event_count:
            raise QualificationValidationError(
                "ANCHOR_EVENT_COUNT_MISMATCH",
                f"expected {expected_event_count} anchors, got {len(anchors)}",
            )
        _reject_duplicates(
            [anchor.anchor_id for anchor in anchors], "ANCHOR_ID_DUPLICATE", "anchors"
        )
        _reject_duplicates(
            [anchor.unique_witness_text for anchor in anchors],
            "ANCHOR_WITNESS_DUPLICATE",
            "anchors",
        )
        anchor_ids = {anchor.anchor_id for anchor in anchors}
        anchor_positions = {
            anchor.anchor_id: index for index, anchor in enumerate(anchors)
        }
        edge_clauses = tuple(
            _parse_edge_clause(item, index)
            for index, item in enumerate(
                _list(root["edge_clauses"], "edge_clauses")
            )
        )
        _reject_duplicates(
            [clause.clause_id for clause in edge_clauses],
            "EDGE_CLAUSE_ID_DUPLICATE",
            "edge_clauses",
        )
        forbidden_relations = _unique_enum_list(
            EdgeRelation,
            root["forbidden_relations"],
            "forbidden_relations",
            allow_empty=True,
        )
        forbidden_edges = tuple(
            _parse_forbidden_edge(item, index)
            for index, item in enumerate(
                _list(root["forbidden_edges"], "forbidden_edges")
            )
        )
        merge_constraints = tuple(
            _parse_merge_constraint(item, index)
            for index, item in enumerate(
                _list(root["merge_constraints"], "merge_constraints")
            )
        )
        _validate_relation_contract(
            anchors=anchors,
            anchor_ids=anchor_ids,
            anchor_positions=anchor_positions,
            edge_clauses=edge_clauses,
            forbidden_relations=forbidden_relations,
            forbidden_edges=forbidden_edges,
            merge_constraints=merge_constraints,
        )
        return cls(
            acceptable_set_id=_identifier(
                root["acceptable_set_id"], "acceptable_set_id"
            ),
            case_id=_identifier(root["case_id"], "case_id"),
            problem_id=_identifier(root["problem_id"], "problem_id"),
            trajectory_id=_identifier(root["trajectory_id"], "trajectory_id"),
            source=_parse_source(root["source"]),
            expected_event_count=expected_event_count,
            anchors=anchors,
            edge_clauses=edge_clauses,
            forbidden_relations=forbidden_relations,
            forbidden_edges=forbidden_edges,
            merge_constraints=merge_constraints,
        )

    def witness_spans(self, source_bytes: bytes) -> dict[str, tuple[int, int]]:
        actual_sha = hashlib.sha256(source_bytes).hexdigest()
        if actual_sha != self.source.source_artifact_sha256:
            raise QualificationValidationError(
                "SOURCE_BYTES_HASH_MISMATCH",
                f"expected {self.source.source_artifact_sha256}, got {actual_sha}",
            )
        spans: dict[str, tuple[int, int]] = {}
        for anchor in self.anchors:
            witness = anchor.unique_witness_text.encode("utf-8")
            first = source_bytes.find(witness)
            if first < 0:
                raise QualificationValidationError(
                    "ANCHOR_WITNESS_MISSING", anchor.anchor_id
                )
            if source_bytes.find(witness, first + 1) >= 0:
                raise QualificationValidationError(
                    "ANCHOR_WITNESS_NOT_UNIQUE", anchor.anchor_id
                )
            spans[anchor.anchor_id] = (first, first + len(witness))
        ordered = [spans[anchor.anchor_id][0] for anchor in self.anchors]
        if ordered != sorted(ordered) or len(ordered) != len(set(ordered)):
            raise QualificationValidationError(
                "ANCHOR_ORDER_INVALID", "anchor order must equal source occurrence order"
            )
        return spans


@dataclass(frozen=True, slots=True)
class EventExtractionAcceptableSetPack:
    pack_id: str
    cases: tuple[EventExtractionAcceptableSet, ...]

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "EventExtractionAcceptableSetPack":
        root = _mapping(value, "acceptable_set_pack")
        _exact_keys(root, {"schema_version", "pack_id", "cases"}, "acceptable_set_pack")
        if _string(root["schema_version"], "schema_version") != PACK_SCHEMA_VERSION:
            raise QualificationValidationError(
                "ACCEPTABLE_SET_PACK_SCHEMA_UNSUPPORTED",
                f"expected {PACK_SCHEMA_VERSION!r}",
            )
        cases = tuple(
            EventExtractionAcceptableSet.from_dict(item)
            for item in _list(root["cases"], "cases")
        )
        if not cases:
            raise QualificationValidationError(
                "ACCEPTABLE_SET_PACK_EMPTY", "cases must not be empty"
            )
        _reject_duplicates(
            [case.case_id for case in cases], "CASE_ID_DUPLICATE", "cases"
        )
        _reject_duplicates(
            [case.acceptable_set_id for case in cases],
            "ACCEPTABLE_SET_ID_DUPLICATE",
            "cases",
        )
        return cls(pack_id=_identifier(root["pack_id"], "pack_id"), cases=cases)

    @classmethod
    def from_json_text(cls, text: str) -> "EventExtractionAcceptableSetPack":
        try:
            value = json.loads(text, parse_constant=_reject_nonfinite_json)
        except json.JSONDecodeError as exc:
            raise QualificationValidationError(
                "ACCEPTABLE_SET_PACK_JSON_INVALID", str(exc)
            ) from exc
        return cls.from_dict(value)

    def case_by_id(self, case_id: str) -> EventExtractionAcceptableSet:
        matches = [case for case in self.cases if case.case_id == case_id]
        if len(matches) != 1:
            raise QualificationValidationError(
                "CASE_ID_NOT_FOUND", f"expected one {case_id!r}, got {len(matches)}"
            )
        return matches[0]


@dataclass(frozen=True, slots=True)
class EventExtractionEvaluation:
    acceptable_set_id: str
    case_id: str
    candidate_sha256: str
    protocol_verdict: MechanicalVerdict
    artifact_verdict: MechanicalVerdict
    mechanical_scientific_verdict: MechanicalVerdict
    manual_semantic_audit: str
    overall_status: OverallQualificationStatus
    event_anchor_mapping: tuple[Mapping[str, Any], ...]
    anchor_verdicts: tuple[Mapping[str, Any], ...]
    edge_clause_verdicts: tuple[Mapping[str, Any], ...]
    forbidden_edge_observations: tuple[Mapping[str, Any], ...]
    merge_constraint_verdicts: tuple[Mapping[str, Any], ...]
    metrics: Mapping[str, Any]
    errors: tuple[Mapping[str, str], ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": EVALUATION_SCHEMA_VERSION,
            "acceptable_set_id": self.acceptable_set_id,
            "case_id": self.case_id,
            "candidate_sha256": self.candidate_sha256,
            "protocol_verdict": self.protocol_verdict.value,
            "artifact_verdict": self.artifact_verdict.value,
            "mechanical_scientific_verdict": self.mechanical_scientific_verdict.value,
            "manual_semantic_audit": self.manual_semantic_audit,
            "overall_status": self.overall_status.value,
            "event_anchor_mapping": list(self.event_anchor_mapping),
            "anchor_verdicts": list(self.anchor_verdicts),
            "edge_clause_verdicts": list(self.edge_clause_verdicts),
            "forbidden_edge_observations": list(self.forbidden_edge_observations),
            "merge_constraint_verdicts": list(self.merge_constraint_verdicts),
            "metrics": dict(self.metrics),
            "errors": list(self.errors),
        }


def evaluate_candidate_json(
    candidate_json_text: str,
    acceptable: EventExtractionAcceptableSet,
    source_bytes: bytes,
) -> EventExtractionEvaluation:
    """Parse and mechanically evaluate one candidate without fabricating PASS."""

    candidate_sha = hashlib.sha256(candidate_json_text.encode("utf-8")).hexdigest()
    try:
        witness_spans = acceptable.witness_spans(source_bytes)
    except QualificationValidationError as exc:
        return _invalid_evaluation(
            acceptable,
            candidate_sha,
            "INVALID",
            _error(exc.code, exc.message),
        )
    try:
        trajectory = ReasoningTrajectory.from_json_text(candidate_json_text)
    except TrajectoryValidationError as exc:
        return _invalid_evaluation(
            acceptable,
            candidate_sha,
            "PASS",
            _error(exc.code, exc.message),
        )
    return evaluate_trajectory(
        trajectory,
        acceptable,
        source_bytes,
        witness_spans=witness_spans,
        candidate_sha256=candidate_sha,
    )


def evaluate_trajectory(
    trajectory: ReasoningTrajectory,
    acceptable: EventExtractionAcceptableSet,
    source_bytes: bytes,
    *,
    witness_spans: Mapping[str, tuple[int, int]] | None = None,
    candidate_sha256: str | None = None,
) -> EventExtractionEvaluation:
    """Evaluate one already-parsed trajectory against a hidden acceptable set."""

    spans = dict(witness_spans or acceptable.witness_spans(source_bytes))
    candidate_sha = candidate_sha256 or trajectory.canonical_sha256
    errors: list[dict[str, str]] = []
    artifact_errors: list[dict[str, str]] = []
    scientific_errors: list[dict[str, str]] = []

    if trajectory.problem_id != acceptable.problem_id:
        scientific_errors.append(
            _error(
                "PROBLEM_ID_MISMATCH",
                f"expected {acceptable.problem_id!r}, got {trajectory.problem_id!r}",
            )
        )
    if trajectory.trajectory_id != acceptable.trajectory_id:
        scientific_errors.append(
            _error(
                "TRAJECTORY_ID_MISMATCH",
                f"expected {acceptable.trajectory_id!r}, got {trajectory.trajectory_id!r}",
            )
        )
    if trajectory.source != acceptable.source:
        artifact_errors.append(
            _error("SOURCE_IDENTITY_MISMATCH", "candidate source does not match task")
        )
    if len(trajectory.events) != acceptable.expected_event_count:
        scientific_errors.append(
            _error(
                "EVENT_COUNT_MISMATCH",
                f"expected {acceptable.expected_event_count}, got {len(trajectory.events)}",
            )
        )

    mapping: dict[str, str] = {}
    anchor_to_events: dict[str, list[str]] = {
        anchor.anchor_id: [] for anchor in acceptable.anchors
    }
    mapping_rows: list[dict[str, Any]] = []
    previous_end = -1
    for event in trajectory.events:
        start = event.source_span.start
        end = event.source_span.end
        if end > len(source_bytes):
            artifact_errors.append(
                _error(
                    "SOURCE_SPAN_OUT_OF_BOUNDS",
                    f"{event.event_id}: {start}:{end} exceeds {len(source_bytes)}",
                )
            )
            continue
        if start < previous_end:
            artifact_errors.append(
                _error(
                    "SOURCE_SPAN_OVERLAP_OR_REORDER",
                    f"{event.event_id}: start {start} precedes previous end {previous_end}",
                )
            )
        previous_end = max(previous_end, end)
        observed_span_sha = hashlib.sha256(source_bytes[start:end]).hexdigest()
        if observed_span_sha != event.source_span.sha256:
            artifact_errors.append(
                _error(
                    "SOURCE_SPAN_HASH_MISMATCH",
                    f"{event.event_id}: expected {event.source_span.sha256}, got {observed_span_sha}",
                )
            )
        contained = [
            anchor_id
            for anchor_id, (witness_start, witness_end) in spans.items()
            if start <= witness_start and witness_end <= end
        ]
        if len(contained) != 1:
            scientific_errors.append(
                _error(
                    "EVENT_ANCHOR_CARDINALITY_INVALID",
                    f"{event.event_id}: expected one anchor, got {contained!r}",
                )
            )
            continue
        anchor_id = contained[0]
        mapping[event.event_id] = anchor_id
        anchor_to_events[anchor_id].append(event.event_id)
        mapping_rows.append(
            {
                "event_id": event.event_id,
                "anchor_id": anchor_id,
                "source_span": {"start": start, "end": end},
            }
        )

    anchor_specs = {anchor.anchor_id: anchor for anchor in acceptable.anchors}
    event_specs = {event.event_id: event for event in trajectory.events}
    anchor_verdicts: list[dict[str, Any]] = []
    for anchor in acceptable.anchors:
        event_ids = anchor_to_events[anchor.anchor_id]
        row: dict[str, Any] = {
            "anchor_id": anchor.anchor_id,
            "event_ids": list(event_ids),
            "status": "PASS",
        }
        if len(event_ids) != 1:
            row["status"] = "FAIL"
            scientific_errors.append(
                _error(
                    "ANCHOR_EVENT_CARDINALITY_INVALID",
                    f"{anchor.anchor_id}: expected one event, got {event_ids!r}",
                )
            )
        else:
            event = event_specs[event_ids[0]]
            row.update(
                {"event_kind": event.event_kind.value, "event_status": event.status.value}
            )
            if event.event_kind not in anchor.allowed_event_kinds:
                row["status"] = "FAIL"
                scientific_errors.append(
                    _error(
                        "ANCHOR_EVENT_KIND_UNACCEPTABLE",
                        f"{anchor.anchor_id}: {event.event_kind.value}",
                    )
                )
            if event.status not in anchor.allowed_statuses:
                row["status"] = "FAIL"
                scientific_errors.append(
                    _error(
                        "ANCHOR_EVENT_STATUS_UNACCEPTABLE",
                        f"{anchor.anchor_id}: {event.status.value}",
                    )
                )
        anchor_verdicts.append(row)

    candidate_edges: list[tuple[str, str, EdgeRelation, str, str]] = []
    for target_event in trajectory.events:
        target_anchor = mapping.get(target_event.event_id)
        for incoming in target_event.incoming_edges:
            source_anchor = mapping.get(incoming.source_event_id)
            if source_anchor is None or target_anchor is None:
                scientific_errors.append(
                    _error(
                        "EDGE_ANCHOR_MAPPING_UNAVAILABLE",
                        f"{incoming.source_event_id}->{target_event.event_id}",
                    )
                )
                continue
            candidate_edges.append(
                (
                    source_anchor,
                    target_anchor,
                    incoming.relation,
                    incoming.source_event_id,
                    target_event.event_id,
                )
            )

    forbidden_rows: list[dict[str, Any]] = []
    forbidden_global = set(acceptable.forbidden_relations)
    forbidden_exact = {
        (item.source_anchor_id, item.target_anchor_id, relation)
        for item in acceptable.forbidden_edges
        for relation in item.forbidden_relations
    }
    forbidden_identities: set[tuple[str, str, EdgeRelation]] = set()
    for source, target, relation, source_event, target_event in candidate_edges:
        if relation in forbidden_global or (source, target, relation) in forbidden_exact:
            forbidden_identities.add((source, target, relation))
            forbidden_rows.append(
                {
                    "source_anchor_id": source,
                    "target_anchor_id": target,
                    "relation": relation.value,
                    "source_event_id": source_event,
                    "target_event_id": target_event,
                    "status": "FAIL",
                }
            )
            scientific_errors.append(
                _error(
                    "FORBIDDEN_EDGE_OBSERVED",
                    f"{source}->{target}:{relation.value}",
                )
            )

    edge_clause_rows: list[dict[str, Any]] = []
    matched_candidate_edges: set[tuple[str, str, EdgeRelation]] = set()
    for clause in acceptable.edge_clauses:
        observed = sorted(
            {
                relation.value
                for source, target, relation, _, _ in candidate_edges
                if source == clause.source_anchor_id
                and target == clause.target_anchor_id
                and relation in clause.allowed_relations
                and (source, target, relation) not in forbidden_identities
            }
        )
        for relation_name in observed:
            matched_candidate_edges.add(
                (
                    clause.source_anchor_id,
                    clause.target_anchor_id,
                    EdgeRelation(relation_name),
                )
            )
        status = "PASS" if observed or not clause.required else "FAIL"
        edge_clause_rows.append(
            {
                "clause_id": clause.clause_id,
                "required": clause.required,
                "observed_relations": observed,
                "status": status,
            }
        )
        if status == "FAIL":
            scientific_errors.append(
                _error("REQUIRED_EDGE_MISSING", clause.clause_id)
            )

    unmatched = sorted(
        {
            (source, target, relation.value)
            for source, target, relation, _, _ in candidate_edges
            if (source, target, relation) not in matched_candidate_edges
            and (source, target, relation) not in forbidden_identities
        }
    )
    for source, target, relation in unmatched:
        scientific_errors.append(
            _error("UNMATCHED_EDGE", f"{source}->{target}:{relation}")
        )

    merge_parents: dict[str, set[str]] = {}
    for source, target, relation, _, _ in candidate_edges:
        if relation is EdgeRelation.MERGE:
            merge_parents.setdefault(target, set()).add(source)
    merge_rows: list[dict[str, Any]] = []
    explicitly_constrained = {
        constraint.target_anchor_id for constraint in acceptable.merge_constraints
    }
    for target, parents in sorted(merge_parents.items()):
        if target not in explicitly_constrained:
            status = "PASS" if len(parents) >= 2 else "FAIL"
            merge_rows.append(
                {
                    "constraint_id": f"automatic-merge-{target}",
                    "target_anchor_id": target,
                    "distinct_parent_anchor_ids": sorted(parents),
                    "minimum": 2,
                    "required_parent_anchor_ids": [],
                    "status": status,
                }
            )
            if status == "FAIL":
                scientific_errors.append(
                    _error("MERGE_PARENT_CARDINALITY_INVALID", target)
                )
    for constraint in acceptable.merge_constraints:
        parents = merge_parents.get(constraint.target_anchor_id, set())
        required = set(constraint.required_parent_anchor_ids)
        status = (
            "PASS"
            if len(parents) >= constraint.minimum_distinct_parent_anchors
            and required.issubset(parents)
            else "FAIL"
        )
        merge_rows.append(
            {
                "constraint_id": f"merge-{constraint.target_anchor_id}",
                "target_anchor_id": constraint.target_anchor_id,
                "distinct_parent_anchor_ids": sorted(parents),
                "minimum": constraint.minimum_distinct_parent_anchors,
                "required_parent_anchor_ids": sorted(required),
                "status": status,
            }
        )
        if status == "FAIL":
            scientific_errors.append(
                _error("MERGE_CONSTRAINT_UNSATISFIED", constraint.target_anchor_id)
            )

    errors.extend(artifact_errors)
    errors.extend(scientific_errors)
    artifact_verdict = (
        MechanicalVerdict.FAIL if artifact_errors else MechanicalVerdict.PASS
    )
    scientific_verdict = (
        MechanicalVerdict.FAIL if scientific_errors else MechanicalVerdict.PASS
    )
    overall = (
        OverallQualificationStatus.PENDING_MANUAL_AUDIT
        if not errors
        else OverallQualificationStatus.FAIL
    )
    metrics = {
        "expected_event_count": acceptable.expected_event_count,
        "observed_event_count": len(trajectory.events),
        "expected_anchor_count": len(acceptable.anchors),
        "mapped_anchor_count": sum(
            1 for event_ids in anchor_to_events.values() if len(event_ids) == 1
        ),
        "required_edge_clause_count": sum(
            1 for clause in acceptable.edge_clauses if clause.required
        ),
        "required_edge_clause_pass_count": sum(
            1
            for row in edge_clause_rows
            if row["required"] and row["status"] == "PASS"
        ),
        "forbidden_edge_count": len(forbidden_rows),
        "unmatched_edge_count": len(unmatched),
        "manual_semantic_audit_complete": False,
    }
    return EventExtractionEvaluation(
        acceptable_set_id=acceptable.acceptable_set_id,
        case_id=acceptable.case_id,
        candidate_sha256=candidate_sha,
        protocol_verdict=MechanicalVerdict.PASS,
        artifact_verdict=artifact_verdict,
        mechanical_scientific_verdict=scientific_verdict,
        manual_semantic_audit="PENDING",
        overall_status=overall,
        event_anchor_mapping=tuple(mapping_rows),
        anchor_verdicts=tuple(anchor_verdicts),
        edge_clause_verdicts=tuple(edge_clause_rows),
        forbidden_edge_observations=tuple(forbidden_rows),
        merge_constraint_verdicts=tuple(merge_rows),
        metrics=metrics,
        errors=tuple(errors),
    )


def _invalid_evaluation(
    acceptable: EventExtractionAcceptableSet,
    candidate_sha256: str,
    protocol_status: str,
    error: Mapping[str, str],
) -> EventExtractionEvaluation:
    return EventExtractionEvaluation(
        acceptable_set_id=acceptable.acceptable_set_id,
        case_id=acceptable.case_id,
        candidate_sha256=candidate_sha256,
        protocol_verdict=MechanicalVerdict(protocol_status),
        artifact_verdict=MechanicalVerdict.INVALID,
        mechanical_scientific_verdict=MechanicalVerdict.INVALID,
        manual_semantic_audit="NOT_REACHED",
        overall_status=OverallQualificationStatus.INVALID,
        event_anchor_mapping=(),
        anchor_verdicts=(),
        edge_clause_verdicts=(),
        forbidden_edge_observations=(),
        merge_constraint_verdicts=(),
        metrics={
            "expected_event_count": acceptable.expected_event_count,
            "observed_event_count": None,
            "manual_semantic_audit_complete": False,
        },
        errors=(error,),
    )


def _parse_anchor(value: Any, index: int) -> Anchor:
    path = f"anchors[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "anchor_id",
            "unique_witness_text",
            "allowed_event_kinds",
            "allowed_statuses",
        },
        path,
    )
    return Anchor(
        anchor_id=_identifier(item["anchor_id"], f"{path}.anchor_id"),
        unique_witness_text=_string(
            item["unique_witness_text"], f"{path}.unique_witness_text"
        ),
        allowed_event_kinds=_unique_enum_list(
            EventKind, item["allowed_event_kinds"], f"{path}.allowed_event_kinds"
        ),
        allowed_statuses=_unique_enum_list(
            EventStatus, item["allowed_statuses"], f"{path}.allowed_statuses"
        ),
    )


def _parse_edge_clause(value: Any, index: int) -> EdgeClause:
    path = f"edge_clauses[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "clause_id",
            "source_anchor_id",
            "target_anchor_id",
            "allowed_relations",
            "required",
        },
        path,
    )
    return EdgeClause(
        clause_id=_identifier(item["clause_id"], f"{path}.clause_id"),
        source_anchor_id=_identifier(
            item["source_anchor_id"], f"{path}.source_anchor_id"
        ),
        target_anchor_id=_identifier(
            item["target_anchor_id"], f"{path}.target_anchor_id"
        ),
        allowed_relations=_unique_enum_list(
            EdgeRelation, item["allowed_relations"], f"{path}.allowed_relations"
        ),
        required=_boolean(item["required"], f"{path}.required"),
    )


def _parse_forbidden_edge(value: Any, index: int) -> ForbiddenEdge:
    path = f"forbidden_edges[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {"source_anchor_id", "target_anchor_id", "forbidden_relations"},
        path,
    )
    return ForbiddenEdge(
        source_anchor_id=_identifier(
            item["source_anchor_id"], f"{path}.source_anchor_id"
        ),
        target_anchor_id=_identifier(
            item["target_anchor_id"], f"{path}.target_anchor_id"
        ),
        forbidden_relations=_unique_enum_list(
            EdgeRelation,
            item["forbidden_relations"],
            f"{path}.forbidden_relations",
        ),
    )


def _parse_merge_constraint(value: Any, index: int) -> MergeConstraint:
    path = f"merge_constraints[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "target_anchor_id",
            "minimum_distinct_parent_anchors",
            "required_parent_anchor_ids",
        },
        path,
    )
    minimum = _integer(
        item["minimum_distinct_parent_anchors"],
        f"{path}.minimum_distinct_parent_anchors",
    )
    if minimum < 2:
        raise QualificationValidationError(
            "MERGE_MINIMUM_INVALID", f"{path} minimum must be at least two"
        )
    parents = tuple(
        _identifier(parent, f"{path}.required_parent_anchor_ids[{parent_index}]")
        for parent_index, parent in enumerate(
            _list(item["required_parent_anchor_ids"], f"{path}.required_parent_anchor_ids")
        )
    )
    _reject_duplicates(
        list(parents), "MERGE_REQUIRED_PARENT_DUPLICATE", path
    )
    return MergeConstraint(
        target_anchor_id=_identifier(
            item["target_anchor_id"], f"{path}.target_anchor_id"
        ),
        minimum_distinct_parent_anchors=minimum,
        required_parent_anchor_ids=tuple(sorted(parents)),
    )


def _validate_relation_contract(
    *,
    anchors: tuple[Anchor, ...],
    anchor_ids: set[str],
    anchor_positions: Mapping[str, int],
    edge_clauses: tuple[EdgeClause, ...],
    forbidden_relations: tuple[EdgeRelation, ...],
    forbidden_edges: tuple[ForbiddenEdge, ...],
    merge_constraints: tuple[MergeConstraint, ...],
) -> None:
    del anchors
    relation_assignments: set[tuple[str, str, EdgeRelation]] = set()
    forbidden_global = set(forbidden_relations)
    for clause in edge_clauses:
        _validate_forward_anchor_pair(
            clause.source_anchor_id,
            clause.target_anchor_id,
            anchor_ids,
            anchor_positions,
            clause.clause_id,
        )
        for relation in clause.allowed_relations:
            identity = (
                clause.source_anchor_id,
                clause.target_anchor_id,
                relation,
            )
            if identity in relation_assignments:
                raise QualificationValidationError(
                    "EDGE_RELATION_ASSIGNMENT_DUPLICATE", repr(identity)
                )
            if relation in forbidden_global:
                raise QualificationValidationError(
                    "EDGE_RELATION_FORBIDDEN_AND_ALLOWED", repr(identity)
                )
            relation_assignments.add(identity)
    forbidden_assignments: set[tuple[str, str, EdgeRelation]] = set()
    for item in forbidden_edges:
        _validate_forward_anchor_pair(
            item.source_anchor_id,
            item.target_anchor_id,
            anchor_ids,
            anchor_positions,
            "forbidden_edge",
        )
        for relation in item.forbidden_relations:
            identity = (item.source_anchor_id, item.target_anchor_id, relation)
            if identity in relation_assignments:
                raise QualificationValidationError(
                    "EDGE_RELATION_FORBIDDEN_AND_ALLOWED", repr(identity)
                )
            if identity in forbidden_assignments:
                raise QualificationValidationError(
                    "FORBIDDEN_EDGE_DUPLICATE", repr(identity)
                )
            forbidden_assignments.add(identity)
    constraint_targets: set[str] = set()
    for constraint in merge_constraints:
        if constraint.target_anchor_id not in anchor_ids:
            raise QualificationValidationError(
                "MERGE_TARGET_UNKNOWN", constraint.target_anchor_id
            )
        if constraint.target_anchor_id in constraint_targets:
            raise QualificationValidationError(
                "MERGE_CONSTRAINT_TARGET_DUPLICATE", constraint.target_anchor_id
            )
        constraint_targets.add(constraint.target_anchor_id)
        for parent in constraint.required_parent_anchor_ids:
            _validate_forward_anchor_pair(
                parent,
                constraint.target_anchor_id,
                anchor_ids,
                anchor_positions,
                "merge_constraint",
            )
            if (parent, constraint.target_anchor_id, EdgeRelation.MERGE) not in relation_assignments:
                raise QualificationValidationError(
                    "MERGE_REQUIRED_PARENT_NOT_ALLOWED",
                    f"{parent}->{constraint.target_anchor_id}",
                )


def _validate_forward_anchor_pair(
    source: str,
    target: str,
    anchor_ids: set[str],
    anchor_positions: Mapping[str, int],
    path: str,
) -> None:
    if source not in anchor_ids or target not in anchor_ids:
        raise QualificationValidationError(
            "EDGE_ANCHOR_UNKNOWN", f"{path}: {source}->{target}"
        )
    if anchor_positions[source] >= anchor_positions[target]:
        raise QualificationValidationError(
            "EDGE_ANCHOR_NOT_FORWARD", f"{path}: {source}->{target}"
        )


def _parse_source(value: Any) -> TrajectorySource:
    item = _mapping(value, "source")
    _exact_keys(
        item,
        {"carrier", "source_artifact_ref", "source_artifact_sha256"},
        "source",
    )
    carrier = _string(item["carrier"], "source.carrier")
    if carrier not in {"fixture", "devin_cli", "codex_exec", "imported"}:
        raise QualificationValidationError("SOURCE_CARRIER_INVALID", carrier)
    return TrajectorySource(
        carrier=carrier,
        source_artifact_ref=_string(
            item["source_artifact_ref"], "source.source_artifact_ref"
        ),
        source_artifact_sha256=_sha256(
            item["source_artifact_sha256"], "source.source_artifact_sha256"
        ),
    )


def _unique_enum_list(
    enum_type: type[StrEnum],
    value: Any,
    path: str,
    *,
    allow_empty: bool = False,
) -> tuple[Any, ...]:
    raw_items = _list(value, path)
    if not raw_items and not allow_empty:
        raise QualificationValidationError("ENUM_LIST_EMPTY", path)
    parsed: list[Any] = []
    for index, raw in enumerate(raw_items):
        name = _string(raw, f"{path}[{index}]")
        try:
            parsed.append(enum_type(name))
        except ValueError as exc:
            raise QualificationValidationError(
                "ENUM_VALUE_INVALID", f"{path}[{index}]={name!r}"
            ) from exc
    _reject_duplicates(parsed, "ENUM_VALUE_DUPLICATE", path)
    return tuple(sorted(parsed, key=lambda item: item.value))


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or not all(isinstance(key, str) for key in value):
        raise QualificationValidationError("TYPE_MAPPING_REQUIRED", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise QualificationValidationError("TYPE_LIST_REQUIRED", path)
    return value


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise QualificationValidationError("TYPE_CANONICAL_STRING_REQUIRED", path)
    return value


def _identifier(value: Any, path: str) -> str:
    result = _string(value, path)
    if not IDENTIFIER_RE.fullmatch(result):
        raise QualificationValidationError("IDENTIFIER_INVALID", f"{path}={result!r}")
    return result


def _integer(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise QualificationValidationError("TYPE_INTEGER_REQUIRED", path)
    return value


def _boolean(value: Any, path: str) -> bool:
    if not isinstance(value, bool):
        raise QualificationValidationError("TYPE_BOOLEAN_REQUIRED", path)
    return value


def _sha256(value: Any, path: str) -> str:
    result = _string(value, path)
    if not SHA256_RE.fullmatch(result):
        raise QualificationValidationError("SHA256_INVALID", path)
    return result


def _exact_keys(value: Mapping[str, Any], expected: set[str], path: str) -> None:
    actual = set(value)
    if actual != expected:
        raise QualificationValidationError(
            "OBJECT_KEYS_INVALID",
            f"{path}: missing={sorted(expected - actual)!r}, unknown={sorted(actual - expected)!r}",
        )


def _reject_duplicates(values: list[Any], code: str, path: str) -> None:
    if len(values) != len(set(values)):
        raise QualificationValidationError(code, path)


def _error(code: str, message: str) -> dict[str, str]:
    return {"code": code, "message": message}


def _reject_nonfinite_json(value: str) -> Any:
    raise QualificationValidationError("JSON_NONFINITE_NUMBER", value)
