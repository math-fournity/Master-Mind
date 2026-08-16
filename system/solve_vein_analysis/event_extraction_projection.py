"""Version-2 occurrence/projection contracts for solve-side event extraction.

This module is deliberately separate from ``event_extraction_qualification``.
The v1 module is bound into the immutable VMS-41 evidence chain and must keep
its historical semantics.  V2 treats a candidate as a fine-grained occurrence
history and evaluates hidden coarse anchors through structured typed paths.
It also separates status-at-occurrence from later resolution and requires
explicit, source-backed contribution objects for every MERGE parent.

Mechanical PASS remains pending blind manual review.  No model, solver,
database, network, or filesystem mutation is performed here.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import hashlib
import json
import re
from typing import Any, Iterable, Mapping, Sequence

from .models import EdgeRelation, EventKind, TrajectorySource, canonical_json_bytes


CANDIDATE_SCHEMA_VERSION = "solve-vein/reasoning-trajectory-candidate/v2"
ACCEPTABLE_SET_SCHEMA_VERSION = "solve-vein/event-extraction-acceptable-set/v2"
PACK_SCHEMA_VERSION = "solve-vein/event-extraction-acceptable-set-pack/v2"
EVALUATION_SCHEMA_VERSION = "solve-vein/event-extraction-evaluation/v2"
RESOLVED_SCHEMA_VERSION = "solve-vein/resolved-occurrence-bundle/v2"
IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
MAX_CANDIDATE_JSON_BYTES = 4 * 1024 * 1024
MAX_EVENT_COUNT = 256
MAX_EDGE_COUNT = 2048
MAX_PATH_SEARCH_STATES = 100_000
MAX_ENUMERATED_PATHS = 4096


class ProjectionValidationError(ValueError):
    """Fail-closed candidate or protocol error with a stable machine code."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


class MechanicalVerdict(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    INVALID = "INVALID"


class ProjectionOverallStatus(StrEnum):
    PENDING_BLIND_MANUAL_AUDIT = "PENDING_BLIND_MANUAL_AUDIT"
    FAIL = "FAIL"
    INVALID = "INVALID"


class OccurrenceStatus(StrEnum):
    ACTIVE = "ACTIVE"
    TENTATIVE = "TENTATIVE"
    ESTABLISHED = "ESTABLISHED"
    SOLVED = "SOLVED"
    UNKNOWN = "UNKNOWN"


class LaterResolution(StrEnum):
    STILL_ACTIVE = "STILL_ACTIVE"
    ABANDONED = "ABANDONED"
    CONTRADICTED = "CONTRADICTED"
    SOLVED = "SOLVED"
    SUPERSEDED = "SUPERSEDED"
    UNKNOWN = "UNKNOWN"


class ContributionRole(StrEnum):
    LEMMA = "LEMMA"
    CONSTRUCTION = "CONSTRUCTION"
    CERTIFICATE = "CERTIFICATE"
    COUNTEREXAMPLE = "COUNTEREXAMPLE"
    BOUND = "BOUND"
    REPRESENTATION = "REPRESENTATION"
    OTHER = "OTHER"


@dataclass(frozen=True, slots=True)
class SpanRange:
    start: int
    end: int

    def to_dict(self) -> dict[str, int]:
        return {"start": self.start, "end": self.end}


@dataclass(frozen=True, slots=True)
class CandidateIncomingEdge:
    source_event_id: str
    relation: EdgeRelation
    evidence: str
    evidence_span: SpanRange

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_event_id": self.source_event_id,
            "relation": self.relation.value,
            "evidence": self.evidence,
            "evidence_span": self.evidence_span.to_dict(),
        }


@dataclass(frozen=True, slots=True)
class MergeContribution:
    parent_event_id: str
    contribution_role: ContributionRole
    contribution_claim: str
    evidence_span: SpanRange
    use_in_target: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "parent_event_id": self.parent_event_id,
            "contribution_role": self.contribution_role.value,
            "contribution_claim": self.contribution_claim,
            "evidence_span": self.evidence_span.to_dict(),
            "use_in_target": self.use_in_target,
        }


@dataclass(frozen=True, slots=True)
class EventOccurrenceV2:
    event_id: str
    sequence_index: int
    event_kind: EventKind
    text: str
    canonical_math_state_id: str
    attributes: tuple[str, ...]
    status_at_occurrence: OccurrenceStatus
    later_resolution: LaterResolution
    source_span: SpanRange
    incoming_edges: tuple[CandidateIncomingEdge, ...]
    merge_contributions: tuple[MergeContribution, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "sequence_index": self.sequence_index,
            "event_kind": self.event_kind.value,
            "text": self.text,
            "canonical_math_state_id": self.canonical_math_state_id,
            "attributes": list(self.attributes),
            "status_at_occurrence": self.status_at_occurrence.value,
            "later_resolution": self.later_resolution.value,
            "source_span": self.source_span.to_dict(),
            "incoming_edges": [edge.to_dict() for edge in self.incoming_edges],
            "merge_contributions": [
                contribution.to_dict() for contribution in self.merge_contributions
            ],
        }


@dataclass(frozen=True, slots=True)
class CandidateTrajectoryV2:
    trajectory_id: str
    problem_id: str
    source: TrajectorySource
    events: tuple[EventOccurrenceV2, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": CANDIDATE_SCHEMA_VERSION,
            "trajectory_id": self.trajectory_id,
            "problem_id": self.problem_id,
            "source": self.source.to_dict(),
            "events": [event.to_dict() for event in self.events],
        }

    @property
    def canonical_sha256(self) -> str:
        return hashlib.sha256(canonical_json_bytes(self.to_dict())).hexdigest()

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "CandidateTrajectoryV2":
        root = _mapping(value, "trajectory")
        _exact_keys(
            root,
            {"schema_version", "trajectory_id", "problem_id", "source", "events"},
            "trajectory",
        )
        if _string(root["schema_version"], "schema_version") != CANDIDATE_SCHEMA_VERSION:
            raise ProjectionValidationError(
                "TRAJECTORY_SCHEMA_UNSUPPORTED",
                f"expected {CANDIDATE_SCHEMA_VERSION!r}",
            )
        raw_events = _list(root["events"], "events")
        if len(raw_events) > MAX_EVENT_COUNT:
            raise ProjectionValidationError(
                "EVENT_COUNT_LIMIT_EXCEEDED",
                f"maximum {MAX_EVENT_COUNT}, got {len(raw_events)}",
            )
        events = tuple(
            _parse_event(item, index)
            for index, item in enumerate(raw_events)
        )
        if not events:
            raise ProjectionValidationError("TRAJECTORY_EMPTY", "events must not be empty")
        trajectory = cls(
            trajectory_id=_identifier(root["trajectory_id"], "trajectory_id"),
            problem_id=_identifier(root["problem_id"], "problem_id"),
            source=_parse_source(root["source"]),
            events=events,
        )
        _validate_candidate_structure(trajectory)
        return trajectory

    @classmethod
    def from_json_text(cls, text: str) -> "CandidateTrajectoryV2":
        encoded_size = len(text.encode("utf-8"))
        if encoded_size > MAX_CANDIDATE_JSON_BYTES:
            raise ProjectionValidationError(
                "CANDIDATE_JSON_SIZE_LIMIT_EXCEEDED",
                f"maximum {MAX_CANDIDATE_JSON_BYTES}, got {encoded_size}",
            )
        try:
            value = json.loads(text, parse_constant=_reject_nonfinite_json)
        except json.JSONDecodeError as exc:
            raise ProjectionValidationError("TRAJECTORY_JSON_INVALID", str(exc)) from exc
        return cls.from_dict(value)


@dataclass(frozen=True, slots=True)
class AnchorV2:
    anchor_id: str
    unique_witness_text: str
    allowed_event_kinds: tuple[EventKind, ...]
    allowed_status_at_occurrence: tuple[OccurrenceStatus, ...]
    allowed_later_resolutions: tuple[LaterResolution, ...]


@dataclass(frozen=True, slots=True)
class PathAtom:
    allowed_relations: tuple[EdgeRelation, ...]
    min_repeat: int
    max_repeat: int


@dataclass(frozen=True, slots=True)
class TypedPathPattern:
    pattern_id: str
    atoms: tuple[PathAtom, ...]
    max_hops: int


@dataclass(frozen=True, slots=True)
class TypedPathClause:
    clause_id: str
    source_anchor_id: str
    target_anchor_id: str
    required: bool
    patterns: tuple[TypedPathPattern, ...]


@dataclass(frozen=True, slots=True)
class ForbiddenTypedPathClause:
    clause_id: str
    source_anchor_id: str
    target_anchor_id: str
    patterns: tuple[TypedPathPattern, ...]


@dataclass(frozen=True, slots=True)
class MergeConstraintV2:
    constraint_id: str
    target_anchor_id: str
    required_origin_anchor_ids: tuple[str, ...]
    minimum_distinct_contributions: int
    contribution_path_patterns: tuple[TypedPathPattern, ...]
    require_pairwise_incomparable: bool


@dataclass(frozen=True, slots=True)
class ExtraEventPolicy:
    allow_unanchored_events: bool
    maximum_extra_events: int
    require_unique_semantic_signature: bool
    require_nondecreasing_source_start: bool


@dataclass(frozen=True, slots=True)
class EventExtractionAcceptableSetV2:
    acceptable_set_id: str
    case_id: str
    problem_id: str
    trajectory_id: str
    source: TrajectorySource
    anchors: tuple[AnchorV2, ...]
    typed_path_clauses: tuple[TypedPathClause, ...]
    forbidden_path_clauses: tuple[ForbiddenTypedPathClause, ...]
    forbidden_relations: tuple[EdgeRelation, ...]
    merge_constraints: tuple[MergeConstraintV2, ...]
    extra_event_policy: ExtraEventPolicy

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "EventExtractionAcceptableSetV2":
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
                "anchors",
                "typed_path_clauses",
                "forbidden_path_clauses",
                "forbidden_relations",
                "merge_constraints",
                "extra_event_policy",
            },
            "acceptable_set",
        )
        if _string(root["schema_version"], "schema_version") != ACCEPTABLE_SET_SCHEMA_VERSION:
            raise ProjectionValidationError(
                "ACCEPTABLE_SET_SCHEMA_UNSUPPORTED",
                f"expected {ACCEPTABLE_SET_SCHEMA_VERSION!r}",
            )
        anchors = tuple(
            _parse_anchor(item, index)
            for index, item in enumerate(_list(root["anchors"], "anchors"))
        )
        if not anchors:
            raise ProjectionValidationError("ANCHORS_EMPTY", "anchors must not be empty")
        _reject_duplicates(
            [anchor.anchor_id for anchor in anchors], "ANCHOR_ID_DUPLICATE", "anchors"
        )
        _reject_duplicates(
            [anchor.unique_witness_text for anchor in anchors],
            "ANCHOR_WITNESS_DUPLICATE",
            "anchors",
        )
        anchor_positions = {
            anchor.anchor_id: index for index, anchor in enumerate(anchors)
        }
        typed = tuple(
            _parse_typed_path_clause(item, index)
            for index, item in enumerate(
                _list(root["typed_path_clauses"], "typed_path_clauses")
            )
        )
        forbidden_paths = tuple(
            _parse_forbidden_path_clause(item, index)
            for index, item in enumerate(
                _list(root["forbidden_path_clauses"], "forbidden_path_clauses")
            )
        )
        _reject_duplicates(
            [clause.clause_id for clause in typed],
            "TYPED_PATH_CLAUSE_ID_DUPLICATE",
            "typed_path_clauses",
        )
        _reject_duplicates(
            [clause.clause_id for clause in forbidden_paths],
            "FORBIDDEN_PATH_CLAUSE_ID_DUPLICATE",
            "forbidden_path_clauses",
        )
        merges = tuple(
            _parse_merge_constraint(item, index)
            for index, item in enumerate(
                _list(root["merge_constraints"], "merge_constraints")
            )
        )
        _reject_duplicates(
            [item.constraint_id for item in merges],
            "MERGE_CONSTRAINT_ID_DUPLICATE",
            "merge_constraints",
        )
        _reject_duplicates(
            [item.target_anchor_id for item in merges],
            "MERGE_TARGET_DUPLICATE",
            "merge_constraints",
        )
        _validate_acceptable_relations(
            anchor_positions=anchor_positions,
            typed_path_clauses=typed,
            forbidden_path_clauses=forbidden_paths,
            merge_constraints=merges,
        )
        return cls(
            acceptable_set_id=_identifier(
                root["acceptable_set_id"], "acceptable_set_id"
            ),
            case_id=_identifier(root["case_id"], "case_id"),
            problem_id=_identifier(root["problem_id"], "problem_id"),
            trajectory_id=_identifier(root["trajectory_id"], "trajectory_id"),
            source=_parse_source(root["source"]),
            anchors=anchors,
            typed_path_clauses=typed,
            forbidden_path_clauses=forbidden_paths,
            forbidden_relations=_unique_enum_list(
                EdgeRelation,
                root["forbidden_relations"],
                "forbidden_relations",
                allow_empty=True,
            ),
            merge_constraints=merges,
            extra_event_policy=_parse_extra_event_policy(root["extra_event_policy"]),
        )

    def witness_spans(self, source_bytes: bytes) -> dict[str, tuple[int, int]]:
        actual_sha = hashlib.sha256(source_bytes).hexdigest()
        if actual_sha != self.source.source_artifact_sha256:
            raise ProjectionValidationError(
                "SOURCE_BYTES_HASH_MISMATCH",
                f"expected {self.source.source_artifact_sha256}, got {actual_sha}",
            )
        spans: dict[str, tuple[int, int]] = {}
        for anchor in self.anchors:
            witness = anchor.unique_witness_text.encode("utf-8")
            first = source_bytes.find(witness)
            if first < 0:
                raise ProjectionValidationError(
                    "ANCHOR_WITNESS_MISSING", anchor.anchor_id
                )
            if source_bytes.find(witness, first + 1) >= 0:
                raise ProjectionValidationError(
                    "ANCHOR_WITNESS_NOT_UNIQUE", anchor.anchor_id
                )
            spans[anchor.anchor_id] = (first, first + len(witness))
        ordered = [spans[anchor.anchor_id][0] for anchor in self.anchors]
        if ordered != sorted(ordered) or len(ordered) != len(set(ordered)):
            raise ProjectionValidationError(
                "ANCHOR_ORDER_INVALID", "anchor order must equal source occurrence order"
            )
        return spans


@dataclass(frozen=True, slots=True)
class EventExtractionAcceptableSetPackV2:
    pack_id: str
    cases: tuple[EventExtractionAcceptableSetV2, ...]

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "EventExtractionAcceptableSetPackV2":
        root = _mapping(value, "acceptable_set_pack")
        _exact_keys(root, {"schema_version", "pack_id", "cases"}, "acceptable_set_pack")
        if _string(root["schema_version"], "schema_version") != PACK_SCHEMA_VERSION:
            raise ProjectionValidationError(
                "ACCEPTABLE_SET_PACK_SCHEMA_UNSUPPORTED",
                f"expected {PACK_SCHEMA_VERSION!r}",
            )
        cases = tuple(
            EventExtractionAcceptableSetV2.from_dict(item)
            for item in _list(root["cases"], "cases")
        )
        if not cases:
            raise ProjectionValidationError(
                "ACCEPTABLE_SET_PACK_EMPTY", "cases must not be empty"
            )
        _reject_duplicates([case.case_id for case in cases], "CASE_ID_DUPLICATE", "cases")
        _reject_duplicates(
            [case.acceptable_set_id for case in cases],
            "ACCEPTABLE_SET_ID_DUPLICATE",
            "cases",
        )
        return cls(pack_id=_identifier(root["pack_id"], "pack_id"), cases=cases)

    @classmethod
    def from_json_text(cls, text: str) -> "EventExtractionAcceptableSetPackV2":
        try:
            value = json.loads(text, parse_constant=_reject_nonfinite_json)
        except json.JSONDecodeError as exc:
            raise ProjectionValidationError(
                "ACCEPTABLE_SET_PACK_JSON_INVALID", str(exc)
            ) from exc
        return cls.from_dict(value)

    def case_by_id(self, case_id: str) -> EventExtractionAcceptableSetV2:
        matches = [case for case in self.cases if case.case_id == case_id]
        if len(matches) != 1:
            raise ProjectionValidationError(
                "CASE_ID_NOT_FOUND", f"expected one {case_id!r}, got {len(matches)}"
            )
        return matches[0]


@dataclass(frozen=True, slots=True)
class EventExtractionEvaluationV2:
    acceptable_set_id: str
    case_id: str
    candidate_sha256: str
    resolved_occurrence_sha256: str | None
    protocol_verdict: MechanicalVerdict
    artifact_verdict: MechanicalVerdict
    anchor_coverage_verdict: MechanicalVerdict
    typed_path_verdict: MechanicalVerdict
    temporal_status_verdict: MechanicalVerdict
    merge_contribution_verdict: MechanicalVerdict
    forbidden_semantics_verdict: MechanicalVerdict
    mechanical_scientific_verdict: MechanicalVerdict
    manual_semantic_audit: str
    overall_status: ProjectionOverallStatus
    event_anchor_mapping: tuple[Mapping[str, Any], ...]
    anchor_verdicts: tuple[Mapping[str, Any], ...]
    typed_path_verdicts: tuple[Mapping[str, Any], ...]
    forbidden_observations: tuple[Mapping[str, Any], ...]
    merge_constraint_verdicts: tuple[Mapping[str, Any], ...]
    metrics: Mapping[str, Any]
    errors: tuple[Mapping[str, str], ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": EVALUATION_SCHEMA_VERSION,
            "acceptable_set_id": self.acceptable_set_id,
            "case_id": self.case_id,
            "candidate_sha256": self.candidate_sha256,
            "resolved_occurrence_sha256": self.resolved_occurrence_sha256,
            "protocol_verdict": self.protocol_verdict.value,
            "artifact_verdict": self.artifact_verdict.value,
            "anchor_coverage_verdict": self.anchor_coverage_verdict.value,
            "typed_path_verdict": self.typed_path_verdict.value,
            "temporal_status_verdict": self.temporal_status_verdict.value,
            "merge_contribution_verdict": self.merge_contribution_verdict.value,
            "forbidden_semantics_verdict": self.forbidden_semantics_verdict.value,
            "mechanical_scientific_verdict": self.mechanical_scientific_verdict.value,
            "manual_semantic_audit": self.manual_semantic_audit,
            "overall_status": self.overall_status.value,
            "event_anchor_mapping": list(self.event_anchor_mapping),
            "anchor_verdicts": list(self.anchor_verdicts),
            "typed_path_verdicts": list(self.typed_path_verdicts),
            "forbidden_observations": list(self.forbidden_observations),
            "merge_constraint_verdicts": list(self.merge_constraint_verdicts),
            "metrics": dict(self.metrics),
            "errors": list(self.errors),
        }


@dataclass(frozen=True, slots=True)
class _CandidatePath:
    event_ids: tuple[str, ...]
    relations: tuple[EdgeRelation, ...]


def resolve_candidate_occurrences(
    trajectory: CandidateTrajectoryV2, source_bytes: bytes
) -> dict[str, Any]:
    """Add runner-derived hashes without changing the candidate's semantics."""

    resolved_events: list[dict[str, Any]] = []
    for event in trajectory.events:
        event_row = event.to_dict()
        event_row["source_span"] = _resolved_span(
            event.source_span, source_bytes, f"event {event.event_id}"
        )
        resolved_edges: list[dict[str, Any]] = []
        for edge in event.incoming_edges:
            edge_row = edge.to_dict()
            edge_row["evidence_span"] = _resolved_span(
                edge.evidence_span,
                source_bytes,
                f"edge {edge.source_event_id}->{event.event_id}",
            )
            resolved_edges.append(edge_row)
        event_row["incoming_edges"] = resolved_edges
        resolved_contributions: list[dict[str, Any]] = []
        for contribution in event.merge_contributions:
            row = contribution.to_dict()
            row["evidence_span"] = _resolved_span(
                contribution.evidence_span,
                source_bytes,
                f"merge contribution {contribution.parent_event_id}->{event.event_id}",
            )
            resolved_contributions.append(row)
        event_row["merge_contributions"] = resolved_contributions
        resolved_events.append(event_row)
    return {
        "schema_version": RESOLVED_SCHEMA_VERSION,
        "candidate_schema_version": CANDIDATE_SCHEMA_VERSION,
        "trajectory_id": trajectory.trajectory_id,
        "problem_id": trajectory.problem_id,
        "source": trajectory.source.to_dict(),
        "events": resolved_events,
    }


def evaluate_candidate_json_v2(
    candidate_json_text: str,
    acceptable: EventExtractionAcceptableSetV2,
    source_bytes: bytes,
) -> EventExtractionEvaluationV2:
    candidate_sha = hashlib.sha256(candidate_json_text.encode("utf-8")).hexdigest()
    try:
        witness_spans = acceptable.witness_spans(source_bytes)
    except ProjectionValidationError as exc:
        return _invalid_evaluation(
            acceptable, candidate_sha, _error(exc.code, exc.message)
        )
    try:
        trajectory = CandidateTrajectoryV2.from_json_text(candidate_json_text)
    except ProjectionValidationError as exc:
        return _invalid_evaluation(
            acceptable, candidate_sha, _error(exc.code, exc.message)
        )
    try:
        return evaluate_trajectory_v2(
            trajectory,
            acceptable,
            source_bytes,
            witness_spans=witness_spans,
            candidate_sha256=candidate_sha,
        )
    except ProjectionValidationError as exc:
        return _invalid_evaluation(
            acceptable, candidate_sha, _error(exc.code, exc.message)
        )


def evaluate_trajectory_v2(
    trajectory: CandidateTrajectoryV2,
    acceptable: EventExtractionAcceptableSetV2,
    source_bytes: bytes,
    *,
    witness_spans: Mapping[str, tuple[int, int]] | None = None,
    candidate_sha256: str | None = None,
) -> EventExtractionEvaluationV2:
    spans = dict(witness_spans or acceptable.witness_spans(source_bytes))
    candidate_sha = candidate_sha256 or trajectory.canonical_sha256
    artifact_errors: list[dict[str, str]] = []
    anchor_errors: list[dict[str, str]] = []
    path_errors: list[dict[str, str]] = []
    temporal_errors: list[dict[str, str]] = []
    merge_errors: list[dict[str, str]] = []
    forbidden_errors: list[dict[str, str]] = []

    if trajectory.problem_id != acceptable.problem_id:
        anchor_errors.append(
            _error(
                "PROBLEM_ID_MISMATCH",
                f"expected {acceptable.problem_id!r}, got {trajectory.problem_id!r}",
            )
        )
    if trajectory.trajectory_id != acceptable.trajectory_id:
        anchor_errors.append(
            _error(
                "TRAJECTORY_ID_MISMATCH",
                f"expected {acceptable.trajectory_id!r}, got {trajectory.trajectory_id!r}",
            )
        )
    if trajectory.source != acceptable.source:
        artifact_errors.append(
            _error("SOURCE_IDENTITY_MISMATCH", "candidate source does not match task")
        )

    resolved: dict[str, Any] | None = None
    try:
        resolved = resolve_candidate_occurrences(trajectory, source_bytes)
    except ProjectionValidationError as exc:
        artifact_errors.append(_error(exc.code, exc.message))
    resolved_sha = (
        hashlib.sha256(canonical_json_bytes(resolved)).hexdigest()
        if resolved is not None
        else None
    )

    mapping: dict[str, str] = {}
    anchor_to_events: dict[str, list[str]] = {
        anchor.anchor_id: [] for anchor in acceptable.anchors
    }
    mapping_rows: list[dict[str, Any]] = []
    extra_event_ids: list[str] = []
    for event in trajectory.events:
        contained = [
            anchor_id
            for anchor_id, (witness_start, witness_end) in spans.items()
            if event.source_span.start <= witness_start
            and witness_end <= event.source_span.end
        ]
        if len(contained) > 1:
            anchor_errors.append(
                _error(
                    "EVENT_SWALLOWS_MULTIPLE_ANCHORS",
                    f"{event.event_id}: {contained!r}",
                )
            )
            mapping_rows.append(
                {
                    "event_id": event.event_id,
                    "anchor_id": None,
                    "classification": "MULTIPLE_ANCHORS",
                }
            )
            continue
        if not contained:
            extra_event_ids.append(event.event_id)
            mapping_rows.append(
                {
                    "event_id": event.event_id,
                    "anchor_id": None,
                    "classification": "EXTRA_SOURCE_BACKED_OCCURRENCE",
                }
            )
            continue
        anchor_id = contained[0]
        mapping[event.event_id] = anchor_id
        anchor_to_events[anchor_id].append(event.event_id)
        mapping_rows.append(
            {
                "event_id": event.event_id,
                "anchor_id": anchor_id,
                "classification": "ANCHOR_OCCURRENCE",
            }
        )

    if extra_event_ids and not acceptable.extra_event_policy.allow_unanchored_events:
        anchor_errors.append(
            _error("EXTRA_EVENTS_FORBIDDEN", repr(extra_event_ids))
        )
    if len(extra_event_ids) > acceptable.extra_event_policy.maximum_extra_events:
        anchor_errors.append(
            _error(
                "EXTRA_EVENT_LIMIT_EXCEEDED",
                f"maximum {acceptable.extra_event_policy.maximum_extra_events}, got {len(extra_event_ids)}",
            )
        )

    event_by_id = {event.event_id: event for event in trajectory.events}
    anchor_verdicts: list[dict[str, Any]] = []
    for anchor in acceptable.anchors:
        event_ids = anchor_to_events[anchor.anchor_id]
        row: dict[str, Any] = {
            "anchor_id": anchor.anchor_id,
            "event_ids": list(event_ids),
            "coverage_status": "PASS",
            "temporal_status": "PASS",
        }
        if len(event_ids) != 1:
            row["coverage_status"] = "FAIL"
            anchor_errors.append(
                _error(
                    "ANCHOR_EVENT_CARDINALITY_INVALID",
                    f"{anchor.anchor_id}: expected one event, got {event_ids!r}",
                )
            )
        else:
            event = event_by_id[event_ids[0]]
            row.update(
                {
                    "event_kind": event.event_kind.value,
                    "status_at_occurrence": event.status_at_occurrence.value,
                    "later_resolution": event.later_resolution.value,
                }
            )
            if event.event_kind not in anchor.allowed_event_kinds:
                row["coverage_status"] = "FAIL"
                anchor_errors.append(
                    _error(
                        "ANCHOR_EVENT_KIND_UNACCEPTABLE",
                        f"{anchor.anchor_id}: {event.event_kind.value}",
                    )
                )
            if event.status_at_occurrence not in anchor.allowed_status_at_occurrence:
                row["temporal_status"] = "FAIL"
                temporal_errors.append(
                    _error(
                        "STATUS_AT_OCCURRENCE_UNACCEPTABLE",
                        f"{anchor.anchor_id}: {event.status_at_occurrence.value}",
                    )
                )
            if event.later_resolution not in anchor.allowed_later_resolutions:
                row["temporal_status"] = "FAIL"
                temporal_errors.append(
                    _error(
                        "LATER_RESOLUTION_UNACCEPTABLE",
                        f"{anchor.anchor_id}: {event.later_resolution.value}",
                    )
                )
        anchor_verdicts.append(row)

    adjacency = _build_adjacency(trajectory)
    typed_rows: list[dict[str, Any]] = []
    matched_edge_identities: set[tuple[str, str, EdgeRelation]] = set()
    for clause in acceptable.typed_path_clauses:
        source_event = _single_anchor_event(anchor_to_events, clause.source_anchor_id)
        target_event = _single_anchor_event(anchor_to_events, clause.target_anchor_id)
        selected: tuple[_CandidatePath, TypedPathPattern] | None = None
        if source_event is not None and target_event is not None:
            for path in _enumerate_paths(
                source_event,
                target_event,
                adjacency,
                max_hops=max(pattern.max_hops for pattern in clause.patterns),
            ):
                pattern = next(
                    (
                        item
                        for item in clause.patterns
                        if _pattern_matches(path.relations, item)
                    ),
                    None,
                )
                if pattern is not None:
                    selected = (path, pattern)
                    break
        status = "PASS" if selected is not None or not clause.required else "FAIL"
        row: dict[str, Any] = {
            "clause_id": clause.clause_id,
            "required": clause.required,
            "source_anchor_id": clause.source_anchor_id,
            "target_anchor_id": clause.target_anchor_id,
            "status": status,
            "matched_pattern_id": None,
            "event_path": [],
            "relation_sequence": [],
            "collapsed_event_ids": [],
        }
        if selected is not None:
            path, pattern = selected
            row.update(
                {
                    "matched_pattern_id": pattern.pattern_id,
                    "event_path": list(path.event_ids),
                    "relation_sequence": [item.value for item in path.relations],
                    "collapsed_event_ids": list(path.event_ids[1:-1]),
                }
            )
            matched_edge_identities.update(
                (path.event_ids[index], path.event_ids[index + 1], relation)
                for index, relation in enumerate(path.relations)
            )
        if status == "FAIL":
            path_errors.append(_error("REQUIRED_TYPED_PATH_MISSING", clause.clause_id))
        typed_rows.append(row)

    forbidden_rows: list[dict[str, Any]] = []
    forbidden_relations = set(acceptable.forbidden_relations)
    for target in trajectory.events:
        for edge in target.incoming_edges:
            if edge.relation in forbidden_relations:
                forbidden_rows.append(
                    {
                        "kind": "GLOBAL_RELATION",
                        "source_event_id": edge.source_event_id,
                        "target_event_id": target.event_id,
                        "relation": edge.relation.value,
                        "status": "FAIL",
                    }
                )
                forbidden_errors.append(
                    _error(
                        "FORBIDDEN_RELATION_OBSERVED",
                        f"{edge.source_event_id}->{target.event_id}:{edge.relation.value}",
                    )
                )
    for clause in acceptable.forbidden_path_clauses:
        source_event = _single_anchor_event(anchor_to_events, clause.source_anchor_id)
        target_event = _single_anchor_event(anchor_to_events, clause.target_anchor_id)
        if source_event is None or target_event is None:
            continue
        observed: tuple[_CandidatePath, TypedPathPattern] | None = None
        for path in _enumerate_paths(
            source_event,
            target_event,
            adjacency,
            max_hops=max(pattern.max_hops for pattern in clause.patterns),
        ):
            pattern = next(
                (
                    item
                    for item in clause.patterns
                    if _pattern_matches(path.relations, item)
                ),
                None,
            )
            if pattern is not None:
                observed = (path, pattern)
                break
        if observed is not None:
            path, pattern = observed
            forbidden_rows.append(
                {
                    "kind": "FORBIDDEN_TYPED_PATH",
                    "clause_id": clause.clause_id,
                    "matched_pattern_id": pattern.pattern_id,
                    "event_path": list(path.event_ids),
                    "relation_sequence": [item.value for item in path.relations],
                    "status": "FAIL",
                }
            )
            forbidden_errors.append(
                _error("FORBIDDEN_TYPED_PATH_OBSERVED", clause.clause_id)
            )

    merge_rows, merge_failures = _evaluate_merge_constraints(
        trajectory=trajectory,
        acceptable=acceptable,
        anchor_to_events=anchor_to_events,
        adjacency=adjacency,
        source_bytes=source_bytes,
    )
    merge_errors.extend(merge_failures)

    artifact_verdict = _axis_verdict(artifact_errors)
    anchor_verdict = _axis_verdict(anchor_errors)
    path_verdict = _axis_verdict(path_errors)
    temporal_verdict = _axis_verdict(temporal_errors)
    merge_verdict = _axis_verdict(merge_errors)
    forbidden_verdict = _axis_verdict(forbidden_errors)
    scientific_errors = (
        anchor_errors
        + path_errors
        + temporal_errors
        + merge_errors
        + forbidden_errors
    )
    scientific_verdict = _axis_verdict(scientific_errors)
    all_errors = artifact_errors + scientific_errors
    overall = (
        ProjectionOverallStatus.PENDING_BLIND_MANUAL_AUDIT
        if not all_errors
        else ProjectionOverallStatus.FAIL
    )
    total_edges = sum(len(event.incoming_edges) for event in trajectory.events)
    metrics = {
        "observed_event_count": len(trajectory.events),
        "expected_anchor_count": len(acceptable.anchors),
        "mapped_anchor_count": sum(
            1 for values in anchor_to_events.values() if len(values) == 1
        ),
        "extra_event_count": len(extra_event_ids),
        "required_typed_path_count": sum(
            1 for clause in acceptable.typed_path_clauses if clause.required
        ),
        "required_typed_path_pass_count": sum(
            1 for row in typed_rows if row["required"] and row["status"] == "PASS"
        ),
        "forbidden_observation_count": len(forbidden_rows),
        "merge_constraint_count": len(acceptable.merge_constraints),
        "merge_constraint_pass_count": sum(
            1 for row in merge_rows if row["status"] == "PASS"
        ),
        "candidate_edge_count": total_edges,
        "projected_edge_count": len(matched_edge_identities),
        "manual_semantic_audit_complete": False,
    }
    return EventExtractionEvaluationV2(
        acceptable_set_id=acceptable.acceptable_set_id,
        case_id=acceptable.case_id,
        candidate_sha256=candidate_sha,
        resolved_occurrence_sha256=resolved_sha,
        protocol_verdict=MechanicalVerdict.PASS,
        artifact_verdict=artifact_verdict,
        anchor_coverage_verdict=anchor_verdict,
        typed_path_verdict=path_verdict,
        temporal_status_verdict=temporal_verdict,
        merge_contribution_verdict=merge_verdict,
        forbidden_semantics_verdict=forbidden_verdict,
        mechanical_scientific_verdict=scientific_verdict,
        manual_semantic_audit="PENDING",
        overall_status=overall,
        event_anchor_mapping=tuple(mapping_rows),
        anchor_verdicts=tuple(anchor_verdicts),
        typed_path_verdicts=tuple(typed_rows),
        forbidden_observations=tuple(forbidden_rows),
        merge_constraint_verdicts=tuple(merge_rows),
        metrics=metrics,
        errors=tuple(all_errors),
    )


def _evaluate_merge_constraints(
    *,
    trajectory: CandidateTrajectoryV2,
    acceptable: EventExtractionAcceptableSetV2,
    anchor_to_events: Mapping[str, list[str]],
    adjacency: Mapping[str, tuple[tuple[str, EdgeRelation], ...]],
    source_bytes: bytes,
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    event_by_id = {event.event_id: event for event in trajectory.events}
    constraint_by_target_event: dict[str, MergeConstraintV2] = {}
    rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    for constraint in acceptable.merge_constraints:
        target_event_id = _single_anchor_event(
            anchor_to_events, constraint.target_anchor_id
        )
        if target_event_id is not None:
            constraint_by_target_event[target_event_id] = constraint

    for event in trajectory.events:
        merge_parent_ids = tuple(
            sorted(
                edge.source_event_id
                for edge in event.incoming_edges
                if edge.relation is EdgeRelation.MERGE
            )
        )
        if not merge_parent_ids:
            continue
        constraint = constraint_by_target_event.get(event.event_id)
        if constraint is None:
            rows.append(
                {
                    "constraint_id": None,
                    "target_event_id": event.event_id,
                    "merge_parent_event_ids": list(merge_parent_ids),
                    "status": "FAIL",
                    "reason": "UNCONSTRAINED_MERGE",
                }
            )
            errors.append(_error("UNCONSTRAINED_MERGE", event.event_id))
            continue
        origin_candidates: dict[str, list[str]] = {}
        for origin_anchor in constraint.required_origin_anchor_ids:
            origin_event = _single_anchor_event(anchor_to_events, origin_anchor)
            candidate_parents: list[str] = []
            if origin_event is not None:
                for parent_event in merge_parent_ids:
                    if origin_event == parent_event:
                        candidate_parents.append(parent_event)
                        continue
                    paths = _enumerate_paths(
                        origin_event,
                        parent_event,
                        adjacency,
                        max_hops=max(
                            pattern.max_hops
                            for pattern in constraint.contribution_path_patterns
                        ),
                        exclude_relations={EdgeRelation.MERGE},
                    )
                    if any(
                        _pattern_matches(path.relations, pattern)
                        for path in paths
                        for pattern in constraint.contribution_path_patterns
                    ):
                        candidate_parents.append(parent_event)
            origin_candidates[origin_anchor] = sorted(set(candidate_parents))
        assignment = _injective_assignment(origin_candidates)
        incomparable = _pairwise_incomparable(
            merge_parent_ids, adjacency, exclude_relations={EdgeRelation.MERGE}
        )
        contribution_spans_valid = True
        for contribution in event.merge_contributions:
            parent = event_by_id[contribution.parent_event_id]
            span = contribution.evidence_span
            if not (
                parent.source_span.start <= span.start
                and span.end <= parent.source_span.end
                and 0 <= span.start < span.end <= len(source_bytes)
            ):
                contribution_spans_valid = False
        status = (
            "PASS"
            if len(merge_parent_ids) >= constraint.minimum_distinct_contributions
            and assignment is not None
            and contribution_spans_valid
            and (
                incomparable
                if constraint.require_pairwise_incomparable
                else True
            )
            else "FAIL"
        )
        row = {
            "constraint_id": constraint.constraint_id,
            "target_anchor_id": constraint.target_anchor_id,
            "target_event_id": event.event_id,
            "merge_parent_event_ids": list(merge_parent_ids),
            "minimum_distinct_contributions": constraint.minimum_distinct_contributions,
            "origin_parent_assignment": assignment,
            "origin_candidates": origin_candidates,
            "pairwise_incomparable": incomparable,
            "pairwise_incomparable_required": constraint.require_pairwise_incomparable,
            "contribution_spans_valid": contribution_spans_valid,
            "status": status,
        }
        rows.append(row)
        if status == "FAIL":
            errors.append(
                _error("MERGE_CONTRIBUTION_CONSTRAINT_UNSATISFIED", constraint.constraint_id)
            )

    constrained_target_events = set(constraint_by_target_event)
    observed_target_events = {
        event.event_id
        for event in trajectory.events
        if any(edge.relation is EdgeRelation.MERGE for edge in event.incoming_edges)
    }
    for target_event_id in sorted(constrained_target_events - observed_target_events):
        constraint = constraint_by_target_event[target_event_id]
        rows.append(
            {
                "constraint_id": constraint.constraint_id,
                "target_anchor_id": constraint.target_anchor_id,
                "target_event_id": target_event_id,
                "merge_parent_event_ids": [],
                "status": "FAIL",
                "reason": "REQUIRED_MERGE_ABSENT",
            }
        )
        errors.append(_error("REQUIRED_MERGE_ABSENT", constraint.constraint_id))
    rows.sort(key=lambda row: (str(row.get("constraint_id")), row["target_event_id"]))
    return rows, errors


def _injective_assignment(
    origin_candidates: Mapping[str, Sequence[str]],
) -> dict[str, str] | None:
    origins = sorted(origin_candidates, key=lambda item: (len(origin_candidates[item]), item))

    def search(index: int, used: set[str], result: dict[str, str]) -> dict[str, str] | None:
        if index == len(origins):
            return dict(sorted(result.items()))
        origin = origins[index]
        for parent in origin_candidates[origin]:
            if parent in used:
                continue
            used.add(parent)
            result[origin] = parent
            found = search(index + 1, used, result)
            if found is not None:
                return found
            result.pop(origin)
            used.remove(parent)
        return None

    return search(0, set(), {})


def _pairwise_incomparable(
    event_ids: Sequence[str],
    adjacency: Mapping[str, tuple[tuple[str, EdgeRelation], ...]],
    *,
    exclude_relations: set[EdgeRelation],
) -> bool:
    for index, left in enumerate(event_ids):
        for right in event_ids[index + 1 :]:
            if _has_path(left, right, adjacency, exclude_relations=exclude_relations):
                return False
            if _has_path(right, left, adjacency, exclude_relations=exclude_relations):
                return False
    return True


def _has_path(
    source: str,
    target: str,
    adjacency: Mapping[str, tuple[tuple[str, EdgeRelation], ...]],
    *,
    exclude_relations: set[EdgeRelation],
) -> bool:
    stack = [source]
    seen = {source}
    while stack:
        current = stack.pop()
        for next_event, relation in adjacency.get(current, ()):
            if relation in exclude_relations:
                continue
            if next_event == target:
                return True
            if next_event not in seen:
                seen.add(next_event)
                stack.append(next_event)
    return False


def _enumerate_paths(
    source: str,
    target: str,
    adjacency: Mapping[str, tuple[tuple[str, EdgeRelation], ...]],
    *,
    max_hops: int,
    exclude_relations: set[EdgeRelation] | None = None,
    max_search_states: int = MAX_PATH_SEARCH_STATES,
    max_enumerated_paths: int = MAX_ENUMERATED_PATHS,
) -> tuple[_CandidatePath, ...]:
    excluded = exclude_relations or set()
    paths: list[_CandidatePath] = []
    search_states = 0

    def visit(
        current: str,
        event_ids: tuple[str, ...],
        relations: tuple[EdgeRelation, ...],
    ) -> None:
        nonlocal search_states
        search_states += 1
        if search_states > max_search_states:
            raise ProjectionValidationError(
                "PATH_SEARCH_BUDGET_EXCEEDED",
                f"maximum states {max_search_states}",
            )
        if len(relations) > max_hops:
            return
        if current == target:
            paths.append(_CandidatePath(event_ids=event_ids, relations=relations))
            if len(paths) > max_enumerated_paths:
                raise ProjectionValidationError(
                    "PATH_ENUMERATION_LIMIT_EXCEEDED",
                    f"maximum paths {max_enumerated_paths}",
                )
            return
        if len(relations) == max_hops:
            return
        for next_event, relation in adjacency.get(current, ()):
            if relation in excluded or next_event in event_ids:
                continue
            visit(next_event, event_ids + (next_event,), relations + (relation,))

    visit(source, (source,), ())
    return tuple(
        sorted(
            paths,
            key=lambda path: (
                len(path.relations),
                tuple(item.value for item in path.relations),
                path.event_ids,
            ),
        )
    )


def _pattern_matches(
    relations: Sequence[EdgeRelation], pattern: TypedPathPattern
) -> bool:
    if len(relations) > pattern.max_hops:
        return False

    def match(atom_index: int, relation_index: int) -> bool:
        if atom_index == len(pattern.atoms):
            return relation_index == len(relations)
        atom = pattern.atoms[atom_index]
        maximum = min(atom.max_repeat, len(relations) - relation_index)
        for count in range(atom.min_repeat, maximum + 1):
            segment = relations[relation_index : relation_index + count]
            if all(item in atom.allowed_relations for item in segment) and match(
                atom_index + 1, relation_index + count
            ):
                return True
        return False

    return match(0, 0)


def _build_adjacency(
    trajectory: CandidateTrajectoryV2,
) -> dict[str, tuple[tuple[str, EdgeRelation], ...]]:
    mutable: dict[str, list[tuple[str, EdgeRelation]]] = {
        event.event_id: [] for event in trajectory.events
    }
    for target in trajectory.events:
        for edge in target.incoming_edges:
            mutable[edge.source_event_id].append((target.event_id, edge.relation))
    return {
        key: tuple(sorted(value, key=lambda item: (item[0], item[1].value)))
        for key, value in mutable.items()
    }


def _single_anchor_event(
    anchor_to_events: Mapping[str, list[str]], anchor_id: str
) -> str | None:
    events = anchor_to_events.get(anchor_id, [])
    return events[0] if len(events) == 1 else None


def _invalid_evaluation(
    acceptable: EventExtractionAcceptableSetV2,
    candidate_sha256: str,
    error: Mapping[str, str],
) -> EventExtractionEvaluationV2:
    return EventExtractionEvaluationV2(
        acceptable_set_id=acceptable.acceptable_set_id,
        case_id=acceptable.case_id,
        candidate_sha256=candidate_sha256,
        resolved_occurrence_sha256=None,
        protocol_verdict=MechanicalVerdict.INVALID,
        artifact_verdict=MechanicalVerdict.INVALID,
        anchor_coverage_verdict=MechanicalVerdict.INVALID,
        typed_path_verdict=MechanicalVerdict.INVALID,
        temporal_status_verdict=MechanicalVerdict.INVALID,
        merge_contribution_verdict=MechanicalVerdict.INVALID,
        forbidden_semantics_verdict=MechanicalVerdict.INVALID,
        mechanical_scientific_verdict=MechanicalVerdict.INVALID,
        manual_semantic_audit="NOT_REACHED",
        overall_status=ProjectionOverallStatus.INVALID,
        event_anchor_mapping=(),
        anchor_verdicts=(),
        typed_path_verdicts=(),
        forbidden_observations=(),
        merge_constraint_verdicts=(),
        metrics={"manual_semantic_audit_complete": False},
        errors=(error,),
    )


def _parse_event(value: Any, index: int) -> EventOccurrenceV2:
    path = f"events[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "event_id",
            "sequence_index",
            "event_kind",
            "text",
            "canonical_math_state_id",
            "attributes",
            "status_at_occurrence",
            "later_resolution",
            "source_span",
            "incoming_edges",
            "merge_contributions",
        },
        path,
    )
    return EventOccurrenceV2(
        event_id=_identifier(item["event_id"], f"{path}.event_id"),
        sequence_index=_integer(item["sequence_index"], f"{path}.sequence_index"),
        event_kind=_enum(EventKind, item["event_kind"], f"{path}.event_kind"),
        text=_nonempty_string(item["text"], f"{path}.text"),
        canonical_math_state_id=_identifier(
            item["canonical_math_state_id"], f"{path}.canonical_math_state_id"
        ),
        attributes=_unique_string_tuple(item["attributes"], f"{path}.attributes"),
        status_at_occurrence=_enum(
            OccurrenceStatus,
            item["status_at_occurrence"],
            f"{path}.status_at_occurrence",
        ),
        later_resolution=_enum(
            LaterResolution, item["later_resolution"], f"{path}.later_resolution"
        ),
        source_span=_parse_span(item["source_span"], f"{path}.source_span"),
        incoming_edges=tuple(
            _parse_incoming_edge(edge, path, edge_index)
            for edge_index, edge in enumerate(
                _list(item["incoming_edges"], f"{path}.incoming_edges")
            )
        ),
        merge_contributions=tuple(
            _parse_merge_contribution(contribution, path, contribution_index)
            for contribution_index, contribution in enumerate(
                _list(item["merge_contributions"], f"{path}.merge_contributions")
            )
        ),
    )


def _parse_incoming_edge(value: Any, event_path: str, index: int) -> CandidateIncomingEdge:
    path = f"{event_path}.incoming_edges[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item, {"source_event_id", "relation", "evidence", "evidence_span"}, path
    )
    return CandidateIncomingEdge(
        source_event_id=_identifier(item["source_event_id"], f"{path}.source_event_id"),
        relation=_enum(EdgeRelation, item["relation"], f"{path}.relation"),
        evidence=_nonempty_string(item["evidence"], f"{path}.evidence"),
        evidence_span=_parse_span(item["evidence_span"], f"{path}.evidence_span"),
    )


def _parse_merge_contribution(
    value: Any, event_path: str, index: int
) -> MergeContribution:
    path = f"{event_path}.merge_contributions[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "parent_event_id",
            "contribution_role",
            "contribution_claim",
            "evidence_span",
            "use_in_target",
        },
        path,
    )
    return MergeContribution(
        parent_event_id=_identifier(item["parent_event_id"], f"{path}.parent_event_id"),
        contribution_role=_enum(
            ContributionRole, item["contribution_role"], f"{path}.contribution_role"
        ),
        contribution_claim=_nonempty_string(
            item["contribution_claim"], f"{path}.contribution_claim"
        ),
        evidence_span=_parse_span(item["evidence_span"], f"{path}.evidence_span"),
        use_in_target=_nonempty_string(item["use_in_target"], f"{path}.use_in_target"),
    )


def _validate_candidate_structure(trajectory: CandidateTrajectoryV2) -> None:
    event_ids = [event.event_id for event in trajectory.events]
    _reject_duplicates(event_ids, "EVENT_ID_DUPLICATE", "events")
    indexes = [event.sequence_index for event in trajectory.events]
    if indexes != list(range(len(indexes))):
        raise ProjectionValidationError(
            "SEQUENCE_INDEX_INVALID",
            f"expected 0..{len(indexes) - 1}, got {indexes!r}",
        )
    positions = {event.event_id: event.sequence_index for event in trajectory.events}
    edge_count = sum(len(event.incoming_edges) for event in trajectory.events)
    if edge_count > MAX_EDGE_COUNT:
        raise ProjectionValidationError(
            "EDGE_COUNT_LIMIT_EXCEEDED",
            f"maximum {MAX_EDGE_COUNT}, got {edge_count}",
        )
    starts = [event.source_span.start for event in trajectory.events]
    if starts != sorted(starts):
        raise ProjectionValidationError(
            "SOURCE_START_ORDER_INVALID", f"event starts are not nondecreasing: {starts!r}"
        )
    signatures = [
        (
            event.source_span.start,
            event.source_span.end,
            event.event_kind.value,
            event.canonical_math_state_id,
        )
        for event in trajectory.events
    ]
    if len(signatures) != len(set(signatures)):
        raise ProjectionValidationError(
            "EVENT_SEMANTIC_SIGNATURE_DUPLICATE",
            "events repeat span/kind/canonical-state identity",
        )
    for event in trajectory.events:
        if event.sequence_index == 0 and event.incoming_edges:
            raise ProjectionValidationError(
                "ROOT_HAS_INCOMING_EDGE", event.event_id
            )
        if event.sequence_index > 0 and not event.incoming_edges:
            raise ProjectionValidationError(
                "NON_ROOT_WITHOUT_PARENT", event.event_id
            )
        identities: set[tuple[str, EdgeRelation]] = set()
        for edge in event.incoming_edges:
            source_position = positions.get(edge.source_event_id)
            if source_position is None:
                raise ProjectionValidationError(
                    "PARENT_EVENT_MISSING", edge.source_event_id
                )
            if source_position >= event.sequence_index:
                raise ProjectionValidationError(
                    "NON_FORWARD_EDGE", f"{edge.source_event_id}->{event.event_id}"
                )
            identity = (edge.source_event_id, edge.relation)
            if identity in identities:
                raise ProjectionValidationError(
                    "INCOMING_EDGE_DUPLICATE", repr(identity)
                )
            identities.add(identity)
        merge_parents = {
            edge.source_event_id
            for edge in event.incoming_edges
            if edge.relation is EdgeRelation.MERGE
        }
        contribution_parents = {
            contribution.parent_event_id for contribution in event.merge_contributions
        }
        if len(event.merge_contributions) != len(contribution_parents):
            raise ProjectionValidationError(
                "MERGE_CONTRIBUTION_PARENT_DUPLICATE", event.event_id
            )
        if merge_parents:
            if len(merge_parents) < 2:
                raise ProjectionValidationError(
                    "MERGE_PARENT_CARDINALITY_INVALID", event.event_id
                )
            if merge_parents != contribution_parents:
                raise ProjectionValidationError(
                    "MERGE_CONTRIBUTION_PARENT_SET_MISMATCH",
                    f"{event.event_id}: edges={sorted(merge_parents)!r}, contributions={sorted(contribution_parents)!r}",
                )
        elif event.merge_contributions:
            raise ProjectionValidationError(
                "CONTRIBUTIONS_WITHOUT_MERGE", event.event_id
            )


def _parse_anchor(value: Any, index: int) -> AnchorV2:
    path = f"anchors[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "anchor_id",
            "unique_witness_text",
            "allowed_event_kinds",
            "allowed_status_at_occurrence",
            "allowed_later_resolutions",
        },
        path,
    )
    return AnchorV2(
        anchor_id=_identifier(item["anchor_id"], f"{path}.anchor_id"),
        unique_witness_text=_nonempty_string(
            item["unique_witness_text"], f"{path}.unique_witness_text"
        ),
        allowed_event_kinds=_unique_enum_list(
            EventKind, item["allowed_event_kinds"], f"{path}.allowed_event_kinds"
        ),
        allowed_status_at_occurrence=_unique_enum_list(
            OccurrenceStatus,
            item["allowed_status_at_occurrence"],
            f"{path}.allowed_status_at_occurrence",
        ),
        allowed_later_resolutions=_unique_enum_list(
            LaterResolution,
            item["allowed_later_resolutions"],
            f"{path}.allowed_later_resolutions",
        ),
    )


def _parse_typed_path_clause(value: Any, index: int) -> TypedPathClause:
    path = f"typed_path_clauses[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {"clause_id", "source_anchor_id", "target_anchor_id", "required", "patterns"},
        path,
    )
    return TypedPathClause(
        clause_id=_identifier(item["clause_id"], f"{path}.clause_id"),
        source_anchor_id=_identifier(
            item["source_anchor_id"], f"{path}.source_anchor_id"
        ),
        target_anchor_id=_identifier(
            item["target_anchor_id"], f"{path}.target_anchor_id"
        ),
        required=_boolean(item["required"], f"{path}.required"),
        patterns=_parse_patterns(item["patterns"], f"{path}.patterns"),
    )


def _parse_forbidden_path_clause(value: Any, index: int) -> ForbiddenTypedPathClause:
    path = f"forbidden_path_clauses[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {"clause_id", "source_anchor_id", "target_anchor_id", "patterns"},
        path,
    )
    return ForbiddenTypedPathClause(
        clause_id=_identifier(item["clause_id"], f"{path}.clause_id"),
        source_anchor_id=_identifier(
            item["source_anchor_id"], f"{path}.source_anchor_id"
        ),
        target_anchor_id=_identifier(
            item["target_anchor_id"], f"{path}.target_anchor_id"
        ),
        patterns=_parse_patterns(item["patterns"], f"{path}.patterns"),
    )


def _parse_patterns(value: Any, path: str) -> tuple[TypedPathPattern, ...]:
    raw = _list(value, path)
    if not raw:
        raise ProjectionValidationError("PATH_PATTERNS_EMPTY", path)
    patterns: list[TypedPathPattern] = []
    for index, value_item in enumerate(raw):
        item_path = f"{path}[{index}]"
        item = _mapping(value_item, item_path)
        _exact_keys(item, {"pattern_id", "atoms", "max_hops"}, item_path)
        atoms = tuple(
            _parse_path_atom(atom, item_path, atom_index)
            for atom_index, atom in enumerate(_list(item["atoms"], f"{item_path}.atoms"))
        )
        if not atoms:
            raise ProjectionValidationError("PATH_ATOMS_EMPTY", item_path)
        max_hops = _integer(item["max_hops"], f"{item_path}.max_hops")
        if max_hops <= 0 or max_hops > 32:
            raise ProjectionValidationError(
                "PATH_MAX_HOPS_INVALID", f"{item_path}: {max_hops}"
            )
        if sum(atom.min_repeat for atom in atoms) > max_hops:
            raise ProjectionValidationError(
                "PATH_PATTERN_MIN_EXCEEDS_MAX_HOPS", item_path
            )
        patterns.append(
            TypedPathPattern(
                pattern_id=_identifier(item["pattern_id"], f"{item_path}.pattern_id"),
                atoms=atoms,
                max_hops=max_hops,
            )
        )
    _reject_duplicates(
        [pattern.pattern_id for pattern in patterns],
        "PATH_PATTERN_ID_DUPLICATE",
        path,
    )
    return tuple(patterns)


def _parse_path_atom(value: Any, pattern_path: str, index: int) -> PathAtom:
    path = f"{pattern_path}.atoms[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item, {"allowed_relations", "min_repeat", "max_repeat"}, path
    )
    minimum = _integer(item["min_repeat"], f"{path}.min_repeat")
    maximum = _integer(item["max_repeat"], f"{path}.max_repeat")
    if minimum < 0 or maximum < minimum or maximum > 32:
        raise ProjectionValidationError(
            "PATH_REPEAT_RANGE_INVALID", f"{path}: {minimum}..{maximum}"
        )
    return PathAtom(
        allowed_relations=_unique_enum_list(
            EdgeRelation, item["allowed_relations"], f"{path}.allowed_relations"
        ),
        min_repeat=minimum,
        max_repeat=maximum,
    )


def _parse_merge_constraint(value: Any, index: int) -> MergeConstraintV2:
    path = f"merge_constraints[{index}]"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "constraint_id",
            "target_anchor_id",
            "required_origin_anchor_ids",
            "minimum_distinct_contributions",
            "contribution_path_patterns",
            "require_pairwise_incomparable",
        },
        path,
    )
    origins = tuple(
        _identifier(origin, f"{path}.required_origin_anchor_ids[{origin_index}]")
        for origin_index, origin in enumerate(
            _list(item["required_origin_anchor_ids"], f"{path}.required_origin_anchor_ids")
        )
    )
    _reject_duplicates(list(origins), "MERGE_ORIGIN_DUPLICATE", path)
    if len(origins) < 2:
        raise ProjectionValidationError(
            "MERGE_ORIGIN_CARDINALITY_INVALID", path
        )
    minimum = _integer(
        item["minimum_distinct_contributions"],
        f"{path}.minimum_distinct_contributions",
    )
    if minimum < 2 or minimum > len(origins):
        raise ProjectionValidationError(
            "MERGE_CONTRIBUTION_MINIMUM_INVALID", f"{path}: {minimum}"
        )
    return MergeConstraintV2(
        constraint_id=_identifier(item["constraint_id"], f"{path}.constraint_id"),
        target_anchor_id=_identifier(
            item["target_anchor_id"], f"{path}.target_anchor_id"
        ),
        required_origin_anchor_ids=origins,
        minimum_distinct_contributions=minimum,
        contribution_path_patterns=_parse_patterns(
            item["contribution_path_patterns"], f"{path}.contribution_path_patterns"
        ),
        require_pairwise_incomparable=_boolean(
            item["require_pairwise_incomparable"],
            f"{path}.require_pairwise_incomparable",
        ),
    )


def _parse_extra_event_policy(value: Any) -> ExtraEventPolicy:
    path = "extra_event_policy"
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "allow_unanchored_events",
            "maximum_extra_events",
            "require_unique_semantic_signature",
            "require_nondecreasing_source_start",
        },
        path,
    )
    maximum = _integer(item["maximum_extra_events"], f"{path}.maximum_extra_events")
    if maximum < 0 or maximum > 10000:
        raise ProjectionValidationError(
            "EXTRA_EVENT_MAXIMUM_INVALID", str(maximum)
        )
    require_unique = _boolean(
        item["require_unique_semantic_signature"],
        f"{path}.require_unique_semantic_signature",
    )
    require_ordered = _boolean(
        item["require_nondecreasing_source_start"],
        f"{path}.require_nondecreasing_source_start",
    )
    if not require_unique or not require_ordered:
        raise ProjectionValidationError(
            "EXTRA_EVENT_POLICY_WEAKENS_V2_INVARIANT",
            "V2 always requires unique semantic signatures and nondecreasing source starts",
        )
    return ExtraEventPolicy(
        allow_unanchored_events=_boolean(
            item["allow_unanchored_events"], f"{path}.allow_unanchored_events"
        ),
        maximum_extra_events=maximum,
        require_unique_semantic_signature=require_unique,
        require_nondecreasing_source_start=require_ordered,
    )


def _validate_acceptable_relations(
    *,
    anchor_positions: Mapping[str, int],
    typed_path_clauses: Sequence[TypedPathClause],
    forbidden_path_clauses: Sequence[ForbiddenTypedPathClause],
    merge_constraints: Sequence[MergeConstraintV2],
) -> None:
    for clause in (*typed_path_clauses, *forbidden_path_clauses):
        _validate_anchor_pair(
            clause.source_anchor_id,
            clause.target_anchor_id,
            anchor_positions,
            clause.clause_id,
        )
    for constraint in merge_constraints:
        if constraint.target_anchor_id not in anchor_positions:
            raise ProjectionValidationError(
                "MERGE_TARGET_UNKNOWN", constraint.target_anchor_id
            )
        for origin in constraint.required_origin_anchor_ids:
            _validate_anchor_pair(
                origin,
                constraint.target_anchor_id,
                anchor_positions,
                constraint.constraint_id,
            )


def _validate_anchor_pair(
    source: str,
    target: str,
    anchor_positions: Mapping[str, int],
    path: str,
) -> None:
    if source not in anchor_positions or target not in anchor_positions:
        raise ProjectionValidationError(
            "PATH_ANCHOR_UNKNOWN", f"{path}: {source}->{target}"
        )
    if anchor_positions[source] >= anchor_positions[target]:
        raise ProjectionValidationError(
            "PATH_ANCHOR_NOT_FORWARD", f"{path}: {source}->{target}"
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
        raise ProjectionValidationError("SOURCE_CARRIER_INVALID", carrier)
    return TrajectorySource(
        carrier=carrier,
        source_artifact_ref=_nonempty_string(
            item["source_artifact_ref"], "source.source_artifact_ref"
        ),
        source_artifact_sha256=_sha256(
            item["source_artifact_sha256"], "source.source_artifact_sha256"
        ),
    )


def _parse_span(value: Any, path: str) -> SpanRange:
    item = _mapping(value, path)
    _exact_keys(item, {"start", "end"}, path)
    start = _integer(item["start"], f"{path}.start")
    end = _integer(item["end"], f"{path}.end")
    if start < 0 or end <= start:
        raise ProjectionValidationError(
            "SPAN_RANGE_INVALID", f"{path}: {start}:{end}"
        )
    return SpanRange(start=start, end=end)


def _resolved_span(span: SpanRange, source_bytes: bytes, path: str) -> dict[str, Any]:
    if span.end > len(source_bytes):
        raise ProjectionValidationError(
            "SOURCE_SPAN_OUT_OF_BOUNDS",
            f"{path}: {span.start}:{span.end} exceeds {len(source_bytes)}",
        )
    payload = source_bytes[span.start : span.end]
    return {
        "start": span.start,
        "end": span.end,
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


def _unique_enum_list(
    enum_type: type[StrEnum],
    value: Any,
    path: str,
    *,
    allow_empty: bool = False,
) -> tuple[Any, ...]:
    raw = _list(value, path)
    if not raw and not allow_empty:
        raise ProjectionValidationError("ENUM_LIST_EMPTY", path)
    parsed = tuple(_enum(enum_type, item, f"{path}[{index}]") for index, item in enumerate(raw))
    _reject_duplicates(
        [item.value for item in parsed], "ENUM_LIST_DUPLICATE", path
    )
    return parsed


def _unique_string_tuple(value: Any, path: str) -> tuple[str, ...]:
    parsed = tuple(
        _nonempty_string(item, f"{path}[{index}]")
        for index, item in enumerate(_list(value, path))
    )
    _reject_duplicates(list(parsed), "STRING_LIST_DUPLICATE", path)
    return parsed


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise ProjectionValidationError("TYPE_OBJECT_REQUIRED", path)
    if not all(isinstance(key, str) for key in value):
        raise ProjectionValidationError("OBJECT_KEY_TYPE_INVALID", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise ProjectionValidationError("TYPE_ARRAY_REQUIRED", path)
    return value


def _exact_keys(value: Mapping[str, Any], expected: set[str], path: str) -> None:
    actual = set(value)
    if actual != expected:
        raise ProjectionValidationError(
            "OBJECT_KEYS_INVALID",
            f"{path}: missing={sorted(expected - actual)!r}, unknown={sorted(actual - expected)!r}",
        )


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str):
        raise ProjectionValidationError("TYPE_STRING_REQUIRED", path)
    return value


def _nonempty_string(value: Any, path: str) -> str:
    result = _string(value, path)
    if not result.strip():
        raise ProjectionValidationError("STRING_EMPTY", path)
    return result


def _identifier(value: Any, path: str) -> str:
    result = _nonempty_string(value, path)
    if IDENTIFIER_RE.fullmatch(result) is None:
        raise ProjectionValidationError("IDENTIFIER_INVALID", f"{path}: {result!r}")
    return result


def _sha256(value: Any, path: str) -> str:
    result = _string(value, path)
    if SHA256_RE.fullmatch(result) is None:
        raise ProjectionValidationError("SHA256_INVALID", path)
    return result


def _integer(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ProjectionValidationError("TYPE_INTEGER_REQUIRED", path)
    return value


def _boolean(value: Any, path: str) -> bool:
    if not isinstance(value, bool):
        raise ProjectionValidationError("TYPE_BOOLEAN_REQUIRED", path)
    return value


def _enum(enum_type: type[StrEnum], value: Any, path: str) -> Any:
    raw = _string(value, path)
    try:
        return enum_type(raw)
    except ValueError as exc:
        raise ProjectionValidationError(
            "ENUM_VALUE_INVALID", f"{path}: {raw!r}"
        ) from exc


def _reject_duplicates(values: Sequence[str], code: str, path: str) -> None:
    if len(values) != len(set(values)):
        raise ProjectionValidationError(code, path)


def _reject_nonfinite_json(value: str) -> None:
    raise ProjectionValidationError("JSON_NONFINITE_NUMBER", value)


def _axis_verdict(errors: Sequence[Mapping[str, str]]) -> MechanicalVerdict:
    return MechanicalVerdict.FAIL if errors else MechanicalVerdict.PASS


def _error(code: str, message: str) -> dict[str, str]:
    return {"code": code, "message": message}


__all__ = [
    "ACCEPTABLE_SET_SCHEMA_VERSION",
    "CANDIDATE_SCHEMA_VERSION",
    "EVALUATION_SCHEMA_VERSION",
    "PACK_SCHEMA_VERSION",
    "CandidateTrajectoryV2",
    "ContributionRole",
    "EventExtractionAcceptableSetPackV2",
    "EventExtractionAcceptableSetV2",
    "EventExtractionEvaluationV2",
    "LaterResolution",
    "MechanicalVerdict",
    "OccurrenceStatus",
    "ProjectionOverallStatus",
    "ProjectionValidationError",
    "evaluate_candidate_json_v2",
    "evaluate_trajectory_v2",
    "resolve_candidate_occurrences",
]
