"""Strict data contracts for solve-side nonlinear reasoning analysis."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import hashlib
import json
import re
from typing import Any, Iterable, Mapping


SCHEMA_VERSION = "solve-vein/reasoning-trajectory/v1"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class TrajectoryValidationError(ValueError):
    """A fail-closed validation error with a stable machine code."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


class EventKind(StrEnum):
    STATE = "STATE"
    DECISION = "DECISION"
    FAILURE = "FAILURE"
    RETURN = "RETURN"
    SYNTHESIS = "SYNTHESIS"
    CONCLUSION = "CONCLUSION"


class EventStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ABANDONED = "ABANDONED"
    CONTRADICTED = "CONTRADICTED"
    SOLVED = "SOLVED"
    UNKNOWN = "UNKNOWN"


class EdgeRelation(StrEnum):
    CONTINUE = "CONTINUE"
    REFINE = "REFINE"
    BRANCH_FROM = "BRANCH_FROM"
    CONTRADICT = "CONTRADICT"
    ABANDON = "ABANDON"
    REVISIT = "REVISIT"
    REUSE = "REUSE"
    DEPENDS_ON = "DEPENDS_ON"
    MERGE = "MERGE"
    CONCLUDE = "CONCLUDE"


class TraceFamily(StrEnum):
    LINEAR_PROGRESS = "LINEAR_PROGRESS"
    BRANCH_EXPLORATION = "BRANCH_EXPLORATION"
    FAILED_BRANCH = "FAILED_BRANCH"
    REVISIT_WITH_NEW_INFORMATION = "REVISIT_WITH_NEW_INFORMATION"
    CROSS_BRANCH_REUSE = "CROSS_BRANCH_REUSE"
    TRUE_MERGE = "TRUE_MERGE"
    RECOVERY_AFTER_CONTRADICTION = "RECOVERY_AFTER_CONTRADICTION"


@dataclass(frozen=True, slots=True)
class TrajectorySource:
    carrier: str
    source_artifact_ref: str
    source_artifact_sha256: str

    def to_dict(self) -> dict[str, str]:
        return {
            "carrier": self.carrier,
            "source_artifact_ref": self.source_artifact_ref,
            "source_artifact_sha256": self.source_artifact_sha256,
        }


@dataclass(frozen=True, slots=True)
class SourceSpan:
    start: int
    end: int
    sha256: str

    def to_dict(self) -> dict[str, Any]:
        return {"start": self.start, "end": self.end, "sha256": self.sha256}


@dataclass(frozen=True, slots=True)
class IncomingEdge:
    source_event_id: str
    relation: EdgeRelation
    evidence: str

    def to_dict(self) -> dict[str, str]:
        return {
            "source_event_id": self.source_event_id,
            "relation": self.relation.value,
            "evidence": self.evidence,
        }


@dataclass(frozen=True, slots=True)
class ReasoningEvent:
    event_id: str
    sequence_index: int
    event_kind: EventKind
    text: str
    canonical_math_state_id: str
    attributes: tuple[str, ...]
    status: EventStatus
    source_span: SourceSpan
    incoming_edges: tuple[IncomingEdge, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "sequence_index": self.sequence_index,
            "event_kind": self.event_kind.value,
            "text": self.text,
            "canonical_math_state_id": self.canonical_math_state_id,
            "attributes": list(self.attributes),
            "status": self.status.value,
            "source_span": self.source_span.to_dict(),
            "incoming_edges": [edge.to_dict() for edge in self.incoming_edges],
        }


@dataclass(frozen=True, slots=True)
class ReasoningTrajectory:
    schema_version: str
    trajectory_id: str
    problem_id: str
    source: TrajectorySource
    events: tuple[ReasoningEvent, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "trajectory_id": self.trajectory_id,
            "problem_id": self.problem_id,
            "source": self.source.to_dict(),
            "events": [event.to_dict() for event in self.events],
        }

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(self.to_dict())

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "ReasoningTrajectory":
        root = _require_mapping(value, "trajectory")
        _require_exact_keys(
            root,
            {"schema_version", "trajectory_id", "problem_id", "source", "events"},
            "trajectory",
        )
        schema_version = _require_string(root["schema_version"], "schema_version")
        if schema_version != SCHEMA_VERSION:
            raise TrajectoryValidationError(
                "TRAJECTORY_SCHEMA_UNSUPPORTED",
                f"expected {SCHEMA_VERSION!r}, got {schema_version!r}",
            )
        trajectory_id = _require_identifier(root["trajectory_id"], "trajectory_id")
        problem_id = _require_identifier(root["problem_id"], "problem_id")
        source = _parse_source(root["source"])
        raw_events = _require_list(root["events"], "events")
        if not raw_events:
            raise TrajectoryValidationError("TRAJECTORY_EMPTY", "events must not be empty")
        events = tuple(_parse_event(item, index) for index, item in enumerate(raw_events))
        trajectory = cls(
            schema_version=schema_version,
            trajectory_id=trajectory_id,
            problem_id=problem_id,
            source=source,
            events=events,
        )
        validate_trajectory(trajectory)
        return trajectory

    @classmethod
    def from_json_text(cls, text: str) -> "ReasoningTrajectory":
        try:
            value = json.loads(text, parse_constant=_reject_nonfinite_json)
        except (json.JSONDecodeError, TrajectoryValidationError) as exc:
            if isinstance(exc, TrajectoryValidationError):
                raise
            raise TrajectoryValidationError("TRAJECTORY_JSON_INVALID", str(exc)) from exc
        return cls.from_dict(value)


@dataclass(frozen=True, slots=True)
class GraphEdge:
    edge_id: str
    source_event_id: str
    target_event_id: str
    relation: EdgeRelation
    evidence: str

    def to_dict(self) -> dict[str, str]:
        return {
            "edge_id": self.edge_id,
            "source_event_id": self.source_event_id,
            "target_event_id": self.target_event_id,
            "relation": self.relation.value,
            "evidence": self.evidence,
        }


@dataclass(frozen=True, slots=True)
class ReasoningDag:
    nodes: tuple[ReasoningEvent, ...]
    edges: tuple[GraphEdge, ...]
    topological_order: tuple[str, ...]
    root_event_id: str
    branch_points: tuple[str, ...]
    revisit_events: tuple[str, ...]
    explicit_merge_events: tuple[str, ...]
    unreachable_event_ids: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": "solve-vein/reasoning-dag/v1",
            "nodes": [node.to_dict() for node in self.nodes],
            "edges": [edge.to_dict() for edge in self.edges],
            "topological_order": list(self.topological_order),
            "root_event_id": self.root_event_id,
            "branch_points": list(self.branch_points),
            "revisit_events": list(self.revisit_events),
            "explicit_merge_events": list(self.explicit_merge_events),
            "unreachable_event_ids": list(self.unreachable_event_ids),
            "acyclic": True,
        }


@dataclass(frozen=True, slots=True)
class TraceRecord:
    trace_id: str
    family: TraceFamily
    event_ids: tuple[str, ...]
    edge_ids: tuple[str, ...]
    shared_intent: tuple[str, ...]
    evidence: str
    rule_id: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "family": self.family.value,
            "event_ids": list(self.event_ids),
            "edge_ids": list(self.edge_ids),
            "shared_intent": list(self.shared_intent),
            "evidence": self.evidence,
            "rule_id": self.rule_id,
        }


@dataclass(frozen=True, slots=True)
class AnalysisBundle:
    trajectory: ReasoningTrajectory
    dag: ReasoningDag
    state_context: Mapping[str, Any]
    transition_context: Mapping[str, Any]
    state_concepts: Mapping[str, Any]
    transition_concepts: Mapping[str, Any]
    relational_scaling: Mapping[str, Any]
    traces: tuple[TraceRecord, ...]
    scientific_fingerprint: str
    audit: Mapping[str, Any]


def validate_trajectory(trajectory: ReasoningTrajectory) -> None:
    event_ids = [event.event_id for event in trajectory.events]
    if len(event_ids) != len(set(event_ids)):
        raise TrajectoryValidationError("EVENT_ID_DUPLICATE", "event_id values must be unique")
    indexes = [event.sequence_index for event in trajectory.events]
    if indexes != list(range(len(indexes))):
        raise TrajectoryValidationError(
            "SEQUENCE_INDEX_INVALID",
            f"sequence indexes must be exactly 0..{len(indexes) - 1}, got {indexes!r}",
        )

    positions = {event.event_id: event.sequence_index for event in trajectory.events}
    for event in trajectory.events:
        if event.sequence_index == 0 and event.incoming_edges:
            raise TrajectoryValidationError(
                "ROOT_HAS_INCOMING_EDGE", f"root event {event.event_id!r} has incoming edges"
            )
        if event.sequence_index > 0 and not event.incoming_edges:
            raise TrajectoryValidationError(
                "NON_ROOT_WITHOUT_PARENT", f"event {event.event_id!r} has no incoming edge"
            )
        seen_incoming: set[tuple[str, EdgeRelation]] = set()
        for incoming in event.incoming_edges:
            source_position = positions.get(incoming.source_event_id)
            if source_position is None:
                raise TrajectoryValidationError(
                    "PARENT_EVENT_MISSING",
                    f"event {event.event_id!r} references unknown parent {incoming.source_event_id!r}",
                )
            if source_position >= event.sequence_index:
                raise TrajectoryValidationError(
                    "NON_FORWARD_EDGE",
                    f"edge {incoming.source_event_id!r}->{event.event_id!r} is not forward in time",
                )
            identity = (incoming.source_event_id, incoming.relation)
            if identity in seen_incoming:
                raise TrajectoryValidationError(
                    "INCOMING_EDGE_DUPLICATE",
                    f"event {event.event_id!r} repeats {identity!r}",
                )
            seen_incoming.add(identity)


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def unique_sorted(values: Iterable[str]) -> tuple[str, ...]:
    return tuple(sorted(set(values)))


def _parse_source(value: Any) -> TrajectorySource:
    source = _require_mapping(value, "source")
    _require_exact_keys(
        source,
        {"carrier", "source_artifact_ref", "source_artifact_sha256"},
        "source",
    )
    carrier = _require_string(source["carrier"], "source.carrier")
    if carrier not in {"fixture", "devin_cli", "codex_exec", "imported"}:
        raise TrajectoryValidationError("SOURCE_CARRIER_INVALID", f"unsupported carrier {carrier!r}")
    artifact_ref = _require_string(source["source_artifact_ref"], "source.source_artifact_ref")
    artifact_sha = _require_sha256(
        source["source_artifact_sha256"], "source.source_artifact_sha256"
    )
    return TrajectorySource(carrier, artifact_ref, artifact_sha)


def _parse_event(value: Any, list_index: int) -> ReasoningEvent:
    path = f"events[{list_index}]"
    event = _require_mapping(value, path)
    _require_exact_keys(
        event,
        {
            "event_id",
            "sequence_index",
            "event_kind",
            "text",
            "canonical_math_state_id",
            "attributes",
            "status",
            "source_span",
            "incoming_edges",
        },
        path,
    )
    event_id = _require_identifier(event["event_id"], f"{path}.event_id")
    sequence_index = _require_integer(event["sequence_index"], f"{path}.sequence_index")
    if sequence_index < 0:
        raise TrajectoryValidationError("SEQUENCE_INDEX_NEGATIVE", f"{path}.sequence_index")
    event_kind = _parse_enum(EventKind, event["event_kind"], f"{path}.event_kind")
    text = _require_string(event["text"], f"{path}.text")
    canonical_state = _require_identifier(
        event["canonical_math_state_id"], f"{path}.canonical_math_state_id"
    )
    raw_attributes = _require_list(event["attributes"], f"{path}.attributes")
    attributes = tuple(
        sorted(
            _require_attribute(attribute, f"{path}.attributes[{index}]")
            for index, attribute in enumerate(raw_attributes)
        )
    )
    if len(attributes) != len(set(attributes)):
        raise TrajectoryValidationError(
            "ATTRIBUTE_DUPLICATE", f"{path}.attributes contains duplicates"
        )
    status = _parse_enum(EventStatus, event["status"], f"{path}.status")
    source_span = _parse_source_span(event["source_span"], f"{path}.source_span")
    incoming_list = _require_list(event["incoming_edges"], f"{path}.incoming_edges")
    incoming_edges = tuple(
        sorted(
            (
                _parse_incoming_edge(item, f"{path}.incoming_edges[{index}]")
                for index, item in enumerate(incoming_list)
            ),
            key=lambda edge: (edge.source_event_id, edge.relation.value, edge.evidence),
        )
    )
    return ReasoningEvent(
        event_id=event_id,
        sequence_index=sequence_index,
        event_kind=event_kind,
        text=text,
        canonical_math_state_id=canonical_state,
        attributes=attributes,
        status=status,
        source_span=source_span,
        incoming_edges=incoming_edges,
    )


def _parse_source_span(value: Any, path: str) -> SourceSpan:
    span = _require_mapping(value, path)
    _require_exact_keys(span, {"start", "end", "sha256"}, path)
    start = _require_integer(span["start"], f"{path}.start")
    end = _require_integer(span["end"], f"{path}.end")
    if start < 0 or end <= start:
        raise TrajectoryValidationError(
            "SOURCE_SPAN_INVALID", f"{path} must satisfy 0 <= start < end"
        )
    sha = _require_sha256(span["sha256"], f"{path}.sha256")
    return SourceSpan(start, end, sha)


def _parse_incoming_edge(value: Any, path: str) -> IncomingEdge:
    edge = _require_mapping(value, path)
    _require_exact_keys(edge, {"source_event_id", "relation", "evidence"}, path)
    source_event_id = _require_identifier(edge["source_event_id"], f"{path}.source_event_id")
    relation = _parse_enum(EdgeRelation, edge["relation"], f"{path}.relation")
    evidence = _require_string(edge["evidence"], f"{path}.evidence")
    return IncomingEdge(source_event_id, relation, evidence)


def _parse_enum(enum_type: type[StrEnum], value: Any, path: str) -> Any:
    raw = _require_string(value, path)
    try:
        return enum_type(raw)
    except ValueError as exc:
        allowed = ", ".join(item.value for item in enum_type)
        raise TrajectoryValidationError(
            "ENUM_VALUE_INVALID", f"{path}={raw!r}; allowed: {allowed}"
        ) from exc


def _require_mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise TrajectoryValidationError("TYPE_MAPPING_REQUIRED", f"{path} must be an object")
    if not all(isinstance(key, str) for key in value):
        raise TrajectoryValidationError("OBJECT_KEY_INVALID", f"{path} has a non-string key")
    return value


def _require_list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise TrajectoryValidationError("TYPE_LIST_REQUIRED", f"{path} must be an array")
    return value


def _require_string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TrajectoryValidationError("TYPE_NONEMPTY_STRING_REQUIRED", f"{path}")
    if value != value.strip():
        raise TrajectoryValidationError("STRING_NOT_CANONICAL", f"{path} has edge whitespace")
    return value


def _require_identifier(value: Any, path: str) -> str:
    identifier = _require_string(value, path)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]*", identifier):
        raise TrajectoryValidationError("IDENTIFIER_INVALID", f"{path}={identifier!r}")
    return identifier


def _require_attribute(value: Any, path: str) -> str:
    attribute = _require_string(value, path)
    if ":" not in attribute or attribute.startswith(":") or attribute.endswith(":"):
        raise TrajectoryValidationError(
            "ATTRIBUTE_NOT_NAMESPACED", f"{path}={attribute!r} must contain namespace:value"
        )
    return attribute


def _require_integer(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TrajectoryValidationError("TYPE_INTEGER_REQUIRED", path)
    return value


def _require_sha256(value: Any, path: str) -> str:
    digest = _require_string(value, path)
    if not SHA256_RE.fullmatch(digest):
        raise TrajectoryValidationError("SHA256_INVALID", f"{path} must be lowercase 64hex")
    return digest


def _require_exact_keys(value: Mapping[str, Any], expected: set[str], path: str) -> None:
    actual = set(value)
    missing = expected - actual
    extra = actual - expected
    if missing:
        raise TrajectoryValidationError(
            "OBJECT_KEY_MISSING", f"{path} missing keys: {sorted(missing)!r}"
        )
    if extra:
        raise TrajectoryValidationError(
            "OBJECT_KEY_UNKNOWN", f"{path} has unknown keys: {sorted(extra)!r}"
        )


def _reject_nonfinite_json(value: str) -> Any:
    raise TrajectoryValidationError("JSON_NONFINITE_NUMBER", value)
