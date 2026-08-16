"""Deterministic multi-view semantic truth and acceptable-set evaluation.

This module is deliberately independent from model output quality.  It parses
strict, preregistered semantic candidates and acceptable sets, canonicalizes
order-insensitive fields, and derives the verdict mechanically.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import hashlib
import json
from typing import Any, Mapping


CANDIDATE_SCHEMA_VERSION = "solve-vein/semantic-candidate/v1"
ACCEPTABLE_SET_SCHEMA_VERSION = "solve-vein/semantic-acceptable-set/v1"
EVALUATION_SCHEMA_VERSION = "solve-vein/semantic-evaluation/v1"


class SemanticValidationError(ValueError):
    """A fail-closed validation error with a stable machine code."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


class RelationView(StrEnum):
    TEMPORAL_OCCURRENCE = "TEMPORAL_OCCURRENCE"
    CONTROL_FLOW = "CONTROL_FLOW"
    EPISTEMIC_DEPENDENCY = "EPISTEMIC_DEPENDENCY"
    SYNTHESIS = "SYNTHESIS"
    STATE_IDENTITY = "STATE_IDENTITY"


class RelationKind(StrEnum):
    NEXT = "NEXT"
    LATER_THAN = "LATER_THAN"
    CONTINUE = "CONTINUE"
    BRANCH_FROM = "BRANCH_FROM"
    RETURN_TO = "RETURN_TO"
    DEPENDS_ON = "DEPENDS_ON"
    CONTRADICTS = "CONTRADICTS"
    REUSES = "REUSES"
    MERGES = "MERGES"
    CONCLUDES_FROM = "CONCLUDES_FROM"
    SAME_ON_AXIS = "SAME_ON_AXIS"
    DIFFERENT_ON_AXIS = "DIFFERENT_ON_AXIS"
    REVISITS = "REVISITS"


RELATIONS_BY_VIEW: dict[RelationView, frozenset[RelationKind]] = {
    RelationView.TEMPORAL_OCCURRENCE: frozenset(
        {RelationKind.NEXT, RelationKind.LATER_THAN}
    ),
    RelationView.CONTROL_FLOW: frozenset(
        {
            RelationKind.CONTINUE,
            RelationKind.BRANCH_FROM,
            RelationKind.RETURN_TO,
        }
    ),
    RelationView.EPISTEMIC_DEPENDENCY: frozenset(
        {
            RelationKind.DEPENDS_ON,
            RelationKind.CONTRADICTS,
            RelationKind.REUSES,
        }
    ),
    RelationView.SYNTHESIS: frozenset(
        {RelationKind.MERGES, RelationKind.CONCLUDES_FROM}
    ),
    RelationView.STATE_IDENTITY: frozenset(
        {
            RelationKind.SAME_ON_AXIS,
            RelationKind.DIFFERENT_ON_AXIS,
            RelationKind.REVISITS,
        }
    ),
}


class StateAxis(StrEnum):
    PROBLEM_OBLIGATION = "PROBLEM_OBLIGATION"
    STRATEGY_METHOD = "STRATEGY_METHOD"
    REPRESENTATION = "REPRESENTATION"
    KNOWLEDGE_STATE = "KNOWLEDGE_STATE"
    BRANCH_LIFECYCLE = "BRANCH_LIFECYCLE"
    EPISTEMIC_VALIDITY = "EPISTEMIC_VALIDITY"
    LEGACY_CANONICAL = "LEGACY_CANONICAL"


class StateConstraintKind(StrEnum):
    MUST_LINK = "MUST_LINK"
    CANNOT_LINK = "CANNOT_LINK"
    EXACT_VALUE = "EXACT_VALUE"


class ClauseSelection(StrEnum):
    EXACTLY_ONE = "EXACTLY_ONE"
    AT_LEAST_ONE = "AT_LEAST_ONE"


class StructuralConstraintKind(StrEnum):
    MIN_DISTINCT_PARENTS = "MIN_DISTINCT_PARENTS"


class EvaluationVerdict(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    INVALID = "INVALID"


@dataclass(frozen=True, slots=True, order=True)
class SemanticRelation:
    source_occurrence_id: str
    target_occurrence_id: str
    view: RelationView
    relation: RelationKind

    def to_dict(self) -> dict[str, str]:
        return {
            "source_occurrence_id": self.source_occurrence_id,
            "target_occurrence_id": self.target_occurrence_id,
            "view": self.view.value,
            "relation": self.relation.value,
        }


@dataclass(frozen=True, slots=True, order=True)
class StateBinding:
    occurrence_id: str
    axis: StateAxis
    value_id: str

    def to_dict(self) -> dict[str, str]:
        return {
            "occurrence_id": self.occurrence_id,
            "axis": self.axis.value,
            "value_id": self.value_id,
        }


@dataclass(frozen=True, slots=True, order=True)
class LegacyStatus:
    occurrence_id: str
    status: str

    def to_dict(self) -> dict[str, str]:
        return {"occurrence_id": self.occurrence_id, "status": self.status}


@dataclass(frozen=True, slots=True)
class RelationAlternative:
    alternative_id: str
    complete_relation_set: tuple[SemanticRelation, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "alternative_id": self.alternative_id,
            "complete_relation_set": [
                relation.to_dict() for relation in sorted(self.complete_relation_set)
            ],
        }


@dataclass(frozen=True, slots=True)
class RelationClause:
    clause_id: str
    selection: ClauseSelection
    alternatives: tuple[RelationAlternative, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "clause_id": self.clause_id,
            "selection": self.selection.value,
            "alternatives": [
                alternative.to_dict()
                for alternative in sorted(
                    self.alternatives, key=lambda item: item.alternative_id
                )
            ],
        }


@dataclass(frozen=True, slots=True)
class StateConstraint:
    constraint_id: str
    kind: StateConstraintKind
    axis: StateAxis
    occurrence_ids: tuple[str, ...]
    value_id: str | None

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "constraint_id": self.constraint_id,
            "kind": self.kind.value,
            "axis": self.axis.value,
            "occurrence_ids": sorted(self.occurrence_ids),
        }
        if self.value_id is not None:
            result["value_id"] = self.value_id
        return result


@dataclass(frozen=True, slots=True)
class LegacyStatusConstraint:
    occurrence_id: str
    allowed_statuses: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "occurrence_id": self.occurrence_id,
            "allowed_statuses": sorted(self.allowed_statuses),
        }


@dataclass(frozen=True, slots=True)
class StructuralConstraint:
    constraint_id: str
    kind: StructuralConstraintKind
    target_occurrence_id: str
    view: RelationView
    relation: RelationKind
    minimum: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "constraint_id": self.constraint_id,
            "kind": self.kind.value,
            "target_occurrence_id": self.target_occurrence_id,
            "view": self.view.value,
            "relation": self.relation.value,
            "minimum": self.minimum,
        }


@dataclass(frozen=True, slots=True)
class SemanticCandidate:
    candidate_id: str
    case_id: str
    occurrence_ids: tuple[str, ...]
    relations: tuple[SemanticRelation, ...]
    state_bindings: tuple[StateBinding, ...]
    legacy_statuses: tuple[LegacyStatus, ...]

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "SemanticCandidate":
        root = _mapping(value, "candidate")
        _exact_keys(
            root,
            {
                "schema_version",
                "candidate_id",
                "case_id",
                "occurrence_ids",
                "relations",
                "state_bindings",
                "legacy_statuses",
            },
            "candidate",
        )
        _schema(root, CANDIDATE_SCHEMA_VERSION, "candidate")
        occurrence_ids = _unique_identifiers(root["occurrence_ids"], "occurrence_ids")
        relations = tuple(
            _parse_relation(item, f"relations[{index}]")
            for index, item in enumerate(_list(root["relations"], "relations"))
        )
        _reject_duplicates(relations, "RELATION_DUPLICATE", "relations")
        state_bindings = tuple(
            _parse_state_binding(item, f"state_bindings[{index}]")
            for index, item in enumerate(
                _list(root["state_bindings"], "state_bindings")
            )
        )
        binding_keys = [(item.occurrence_id, item.axis) for item in state_bindings]
        _reject_duplicates(
            binding_keys, "STATE_BINDING_DUPLICATE", "state_bindings"
        )
        legacy_statuses = tuple(
            _parse_legacy_status(item, f"legacy_statuses[{index}]")
            for index, item in enumerate(
                _list(root["legacy_statuses"], "legacy_statuses")
            )
        )
        _reject_duplicates(
            [item.occurrence_id for item in legacy_statuses],
            "LEGACY_STATUS_DUPLICATE",
            "legacy_statuses",
        )
        candidate = cls(
            candidate_id=_identifier(root["candidate_id"], "candidate_id"),
            case_id=_identifier(root["case_id"], "case_id"),
            occurrence_ids=tuple(sorted(occurrence_ids)),
            relations=tuple(sorted(relations)),
            state_bindings=tuple(sorted(state_bindings)),
            legacy_statuses=tuple(sorted(legacy_statuses)),
        )
        candidate._validate_references()
        return candidate

    def _validate_references(self) -> None:
        known = set(self.occurrence_ids)
        for relation in self.relations:
            if (
                relation.source_occurrence_id not in known
                or relation.target_occurrence_id not in known
            ):
                raise SemanticValidationError(
                    "CANDIDATE_OCCURRENCE_REFERENCE_UNKNOWN",
                    f"relation references an unknown occurrence: {relation}",
                )
            if relation.source_occurrence_id == relation.target_occurrence_id:
                raise SemanticValidationError(
                    "CANDIDATE_SELF_RELATION",
                    f"self relation is not allowed: {relation}",
                )
        for binding in self.state_bindings:
            if binding.occurrence_id not in known:
                raise SemanticValidationError(
                    "CANDIDATE_OCCURRENCE_REFERENCE_UNKNOWN",
                    f"state binding references {binding.occurrence_id!r}",
                )
        for status in self.legacy_statuses:
            if status.occurrence_id not in known:
                raise SemanticValidationError(
                    "CANDIDATE_OCCURRENCE_REFERENCE_UNKNOWN",
                    f"legacy status references {status.occurrence_id!r}",
                )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": CANDIDATE_SCHEMA_VERSION,
            "candidate_id": self.candidate_id,
            "case_id": self.case_id,
            "occurrence_ids": list(self.occurrence_ids),
            "relations": [item.to_dict() for item in self.relations],
            "state_bindings": [item.to_dict() for item in self.state_bindings],
            "legacy_statuses": [item.to_dict() for item in self.legacy_statuses],
        }

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(self.to_dict())


@dataclass(frozen=True, slots=True)
class SemanticAcceptableSet:
    acceptable_set_id: str
    case_id: str
    expected_occurrence_ids: tuple[str, ...]
    required_relations: tuple[SemanticRelation, ...]
    relation_clauses: tuple[RelationClause, ...]
    optional_relations: tuple[SemanticRelation, ...]
    forbidden_relations: tuple[SemanticRelation, ...]
    required_state_axes: tuple[StateAxis, ...]
    state_constraints: tuple[StateConstraint, ...]
    legacy_status_constraints: tuple[LegacyStatusConstraint, ...]
    structural_constraints: tuple[StructuralConstraint, ...]

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "SemanticAcceptableSet":
        root = _mapping(value, "acceptable_set")
        _exact_keys(
            root,
            {
                "schema_version",
                "acceptable_set_id",
                "case_id",
                "expected_occurrence_ids",
                "required_relations",
                "relation_clauses",
                "optional_relations",
                "forbidden_relations",
                "required_state_axes",
                "state_constraints",
                "legacy_status_constraints",
                "structural_constraints",
            },
            "acceptable_set",
        )
        _schema(root, ACCEPTABLE_SET_SCHEMA_VERSION, "acceptable_set")
        expected_occurrence_ids = _unique_identifiers(
            root["expected_occurrence_ids"], "expected_occurrence_ids"
        )
        if not expected_occurrence_ids:
            raise SemanticValidationError(
                "ACCEPTABLE_SET_EMPTY", "expected_occurrence_ids must not be empty"
            )
        required = _parse_relation_list(root["required_relations"], "required_relations")
        optional = _parse_relation_list(root["optional_relations"], "optional_relations")
        forbidden = _parse_relation_list(root["forbidden_relations"], "forbidden_relations")
        clauses = tuple(
            _parse_relation_clause(item, f"relation_clauses[{index}]")
            for index, item in enumerate(
                _list(root["relation_clauses"], "relation_clauses")
            )
        )
        _reject_duplicates(
            [item.clause_id for item in clauses],
            "RELATION_CLAUSE_ID_DUPLICATE",
            "relation_clauses",
        )
        axes = tuple(
            _enum(StateAxis, item, f"required_state_axes[{index}]")
            for index, item in enumerate(
                _list(root["required_state_axes"], "required_state_axes")
            )
        )
        _reject_duplicates(
            axes, "REQUIRED_STATE_AXIS_DUPLICATE", "required_state_axes"
        )
        state_constraints = tuple(
            _parse_state_constraint(item, f"state_constraints[{index}]")
            for index, item in enumerate(
                _list(root["state_constraints"], "state_constraints")
            )
        )
        legacy_constraints = tuple(
            _parse_legacy_status_constraint(
                item, f"legacy_status_constraints[{index}]"
            )
            for index, item in enumerate(
                _list(
                    root["legacy_status_constraints"],
                    "legacy_status_constraints",
                )
            )
        )
        structural_constraints = tuple(
            _parse_structural_constraint(
                item, f"structural_constraints[{index}]"
            )
            for index, item in enumerate(
                _list(root["structural_constraints"], "structural_constraints")
            )
        )
        acceptable = cls(
            acceptable_set_id=_identifier(
                root["acceptable_set_id"], "acceptable_set_id"
            ),
            case_id=_identifier(root["case_id"], "case_id"),
            expected_occurrence_ids=tuple(sorted(expected_occurrence_ids)),
            required_relations=tuple(sorted(required)),
            relation_clauses=tuple(
                sorted(clauses, key=lambda item: item.clause_id)
            ),
            optional_relations=tuple(sorted(optional)),
            forbidden_relations=tuple(sorted(forbidden)),
            required_state_axes=tuple(sorted(axes)),
            state_constraints=tuple(
                sorted(state_constraints, key=lambda item: item.constraint_id)
            ),
            legacy_status_constraints=tuple(
                sorted(legacy_constraints, key=lambda item: item.occurrence_id)
            ),
            structural_constraints=tuple(
                sorted(structural_constraints, key=lambda item: item.constraint_id)
            ),
        )
        acceptable._validate_contract()
        return acceptable

    def _validate_contract(self) -> None:
        known = set(self.expected_occurrence_ids)
        relation_groups: list[tuple[str, set[SemanticRelation]]] = [
            ("required_relations", set(self.required_relations)),
            ("optional_relations", set(self.optional_relations)),
            ("forbidden_relations", set(self.forbidden_relations)),
        ]
        all_alternative_relations: set[SemanticRelation] = set()
        for clause in self.relation_clauses:
            if len(clause.alternatives) < 2:
                raise SemanticValidationError(
                    "RELATION_CLAUSE_TOO_SMALL",
                    f"{clause.clause_id!r} needs at least two alternatives",
                )
            clause_seen: set[SemanticRelation] = set()
            for alternative in clause.alternatives:
                if not alternative.complete_relation_set:
                    raise SemanticValidationError(
                        "RELATION_ALTERNATIVE_EMPTY",
                        f"{alternative.alternative_id!r} is empty",
                    )
                overlap = clause_seen & set(alternative.complete_relation_set)
                if overlap:
                    raise SemanticValidationError(
                        "RELATION_ALTERNATIVES_OVERLAP",
                        f"{clause.clause_id!r} alternatives overlap",
                    )
                clause_seen.update(alternative.complete_relation_set)
            overlap = all_alternative_relations & clause_seen
            if overlap:
                raise SemanticValidationError(
                    "RELATION_CLAUSES_OVERLAP",
                    f"{clause.clause_id!r} overlaps another clause",
                )
            all_alternative_relations.update(clause_seen)
        relation_groups.append(("relation_alternatives", all_alternative_relations))
        for index, (left_name, left) in enumerate(relation_groups):
            for right_name, right in relation_groups[index + 1 :]:
                if left & right:
                    raise SemanticValidationError(
                        "RELATION_CATEGORY_OVERLAP",
                        f"{left_name} overlaps {right_name}",
                    )
        every_relation = set().union(*(group for _, group in relation_groups))
        for relation in every_relation:
            if (
                relation.source_occurrence_id not in known
                or relation.target_occurrence_id not in known
            ):
                raise SemanticValidationError(
                    "ACCEPTABLE_OCCURRENCE_REFERENCE_UNKNOWN",
                    f"relation references an unknown occurrence: {relation}",
                )
            if relation.source_occurrence_id == relation.target_occurrence_id:
                raise SemanticValidationError(
                    "ACCEPTABLE_SELF_RELATION",
                    f"self relation is not allowed: {relation}",
                )
        if len({item.constraint_id for item in self.state_constraints}) != len(
            self.state_constraints
        ):
            raise SemanticValidationError(
                "STATE_CONSTRAINT_ID_DUPLICATE",
                "state constraint IDs must be unique",
            )
        required_axes = set(self.required_state_axes)
        for constraint in self.state_constraints:
            if constraint.axis not in required_axes:
                raise SemanticValidationError(
                    "STATE_CONSTRAINT_AXIS_NOT_REQUIRED",
                    f"{constraint.constraint_id!r} uses a non-required axis",
                )
            if not set(constraint.occurrence_ids).issubset(known):
                raise SemanticValidationError(
                    "ACCEPTABLE_OCCURRENCE_REFERENCE_UNKNOWN",
                    f"{constraint.constraint_id!r} references an unknown occurrence",
                )
        status_ids = [item.occurrence_id for item in self.legacy_status_constraints]
        _reject_duplicates(
            status_ids,
            "LEGACY_STATUS_CONSTRAINT_DUPLICATE",
            "legacy_status_constraints",
        )
        if not set(status_ids).issubset(known):
            raise SemanticValidationError(
                "ACCEPTABLE_OCCURRENCE_REFERENCE_UNKNOWN",
                "legacy status constraint references an unknown occurrence",
            )
        if len(
            {item.constraint_id for item in self.structural_constraints}
        ) != len(self.structural_constraints):
            raise SemanticValidationError(
                "STRUCTURAL_CONSTRAINT_ID_DUPLICATE",
                "structural constraint IDs must be unique",
            )
        for constraint in self.structural_constraints:
            if constraint.target_occurrence_id not in known:
                raise SemanticValidationError(
                    "ACCEPTABLE_OCCURRENCE_REFERENCE_UNKNOWN",
                    f"{constraint.constraint_id!r} references an unknown target",
                )

    @property
    def allowed_relations(self) -> frozenset[SemanticRelation]:
        alternatives = {
            relation
            for clause in self.relation_clauses
            for alternative in clause.alternatives
            for relation in alternative.complete_relation_set
        }
        return frozenset(
            set(self.required_relations) | set(self.optional_relations) | alternatives
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": ACCEPTABLE_SET_SCHEMA_VERSION,
            "acceptable_set_id": self.acceptable_set_id,
            "case_id": self.case_id,
            "expected_occurrence_ids": list(self.expected_occurrence_ids),
            "required_relations": [
                item.to_dict() for item in self.required_relations
            ],
            "relation_clauses": [item.to_dict() for item in self.relation_clauses],
            "optional_relations": [
                item.to_dict() for item in self.optional_relations
            ],
            "forbidden_relations": [
                item.to_dict() for item in self.forbidden_relations
            ],
            "required_state_axes": [item.value for item in self.required_state_axes],
            "state_constraints": [
                item.to_dict() for item in self.state_constraints
            ],
            "legacy_status_constraints": [
                item.to_dict() for item in self.legacy_status_constraints
            ],
            "structural_constraints": [
                item.to_dict() for item in self.structural_constraints
            ],
        }

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(self.to_dict())


@dataclass(frozen=True, slots=True)
class SemanticEvaluation:
    candidate_id: str
    acceptable_set_id: str
    canonical_input_hashes: Mapping[str, str]
    occurrence_verdict: Mapping[str, Any]
    required_relation_verdict: Mapping[str, Any]
    relation_clause_verdicts: tuple[Mapping[str, Any], ...]
    optional_relation_observations: tuple[Mapping[str, Any], ...]
    forbidden_relation_verdict: Mapping[str, Any]
    unmatched_relation_verdict: Mapping[str, Any]
    state_constraint_verdicts: tuple[Mapping[str, Any], ...]
    legacy_status_verdicts: tuple[Mapping[str, Any], ...]
    structural_constraint_verdicts: tuple[Mapping[str, Any], ...]
    per_view_coverage: Mapping[str, Any]
    errors: tuple[Mapping[str, str], ...]
    overall_verdict: EvaluationVerdict

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": EVALUATION_SCHEMA_VERSION,
            "candidate_id": self.candidate_id,
            "acceptable_set_id": self.acceptable_set_id,
            "canonical_input_hashes": dict(self.canonical_input_hashes),
            "occurrence_verdict": dict(self.occurrence_verdict),
            "required_relation_verdict": dict(self.required_relation_verdict),
            "relation_clause_verdicts": [
                dict(item) for item in self.relation_clause_verdicts
            ],
            "optional_relation_observations": [
                dict(item) for item in self.optional_relation_observations
            ],
            "forbidden_relation_verdict": dict(self.forbidden_relation_verdict),
            "unmatched_relation_verdict": dict(self.unmatched_relation_verdict),
            "state_constraint_verdicts": [
                dict(item) for item in self.state_constraint_verdicts
            ],
            "legacy_status_verdicts": [
                dict(item) for item in self.legacy_status_verdicts
            ],
            "structural_constraint_verdicts": [
                dict(item) for item in self.structural_constraint_verdicts
            ],
            "per_view_coverage": dict(self.per_view_coverage),
            "errors": [dict(item) for item in self.errors],
            "overall_verdict": self.overall_verdict.value,
        }

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(self.to_dict())


def evaluate_candidate(
    candidate: SemanticCandidate,
    acceptable: SemanticAcceptableSet,
) -> SemanticEvaluation:
    """Evaluate a parsed candidate against a parsed preregistered acceptable set."""

    failures: list[dict[str, str]] = []

    def check(condition: bool, code: str, message: str) -> bool:
        if not condition:
            failures.append({"code": code, "message": message})
        return condition

    check(
        candidate.case_id == acceptable.case_id,
        "CASE_ID_MISMATCH",
        f"candidate={candidate.case_id!r}, acceptable={acceptable.case_id!r}",
    )
    expected_occurrences = set(acceptable.expected_occurrence_ids)
    actual_occurrences = set(candidate.occurrence_ids)
    missing_occurrences = sorted(expected_occurrences - actual_occurrences)
    unknown_occurrences = sorted(actual_occurrences - expected_occurrences)
    occurrence_pass = check(
        not missing_occurrences and not unknown_occurrences,
        "OCCURRENCE_SET_MISMATCH",
        f"missing={missing_occurrences}, unknown={unknown_occurrences}",
    )
    occurrence_verdict = {
        "status": "PASS" if occurrence_pass else "FAIL",
        "missing_occurrence_ids": missing_occurrences,
        "unknown_occurrence_ids": unknown_occurrences,
    }

    actual_relations = set(candidate.relations)
    required_relations = set(acceptable.required_relations)
    missing_required = sorted(required_relations - actual_relations)
    required_pass = check(
        not missing_required,
        "REQUIRED_RELATION_MISSING",
        f"missing={_relations_to_dicts(missing_required)}",
    )
    required_relation_verdict = {
        "status": "PASS" if required_pass else "FAIL",
        "missing": _relations_to_dicts(missing_required),
    }

    clause_verdicts: list[dict[str, Any]] = []
    selected_relations: set[SemanticRelation] = set()
    for clause in acceptable.relation_clauses:
        completed: list[str] = []
        partial: list[str] = []
        for alternative in clause.alternatives:
            alternative_set = set(alternative.complete_relation_set)
            intersection = actual_relations & alternative_set
            if intersection == alternative_set:
                completed.append(alternative.alternative_id)
                selected_relations.update(alternative_set)
            elif intersection:
                partial.append(alternative.alternative_id)
        selection_pass = (
            len(completed) == 1
            if clause.selection is ClauseSelection.EXACTLY_ONE
            else len(completed) >= 1
        )
        clause_pass = selection_pass and not partial
        check(
            clause_pass,
            "RELATION_CLAUSE_UNSATISFIED",
            (
                f"{clause.clause_id!r}: completed={completed}, "
                f"partial={partial}, selection={clause.selection.value}"
            ),
        )
        clause_verdicts.append(
            {
                "clause_id": clause.clause_id,
                "selection": clause.selection.value,
                "completed_alternative_ids": completed,
                "partial_alternative_ids": partial,
                "status": "PASS" if clause_pass else "FAIL",
            }
        )

    forbidden_present = sorted(
        actual_relations & set(acceptable.forbidden_relations)
    )
    forbidden_pass = check(
        not forbidden_present,
        "FORBIDDEN_RELATION_PRESENT",
        f"present={_relations_to_dicts(forbidden_present)}",
    )
    forbidden_verdict = {
        "status": "PASS" if forbidden_pass else "FAIL",
        "present": _relations_to_dicts(forbidden_present),
    }

    unmatched = sorted(actual_relations - set(acceptable.allowed_relations))
    unmatched_pass = check(
        not unmatched,
        "UNMATCHED_RELATION_PRESENT",
        f"unmatched={_relations_to_dicts(unmatched)}",
    )
    unmatched_verdict = {
        "status": "PASS" if unmatched_pass else "FAIL",
        "relations": _relations_to_dicts(unmatched),
    }
    optional_observations = tuple(
        {
            "relation": relation.to_dict(),
            "observed": relation in actual_relations,
        }
        for relation in acceptable.optional_relations
    )

    binding_map = {
        (item.occurrence_id, item.axis): item.value_id
        for item in candidate.state_bindings
    }
    expected_binding_keys = {
        (occurrence_id, axis)
        for occurrence_id in acceptable.expected_occurrence_ids
        for axis in acceptable.required_state_axes
    }
    actual_binding_keys = set(binding_map)
    missing_bindings = sorted(
        (
            {"occurrence_id": occurrence_id, "axis": axis.value}
            for occurrence_id, axis in expected_binding_keys - actual_binding_keys
        ),
        key=lambda item: (item["occurrence_id"], item["axis"]),
    )
    unexpected_bindings = sorted(
        (
            {"occurrence_id": occurrence_id, "axis": axis.value}
            for occurrence_id, axis in actual_binding_keys - expected_binding_keys
        ),
        key=lambda item: (item["occurrence_id"], item["axis"]),
    )
    check(
        not missing_bindings and not unexpected_bindings,
        "STATE_BINDING_COVERAGE_MISMATCH",
        f"missing={missing_bindings}, unexpected={unexpected_bindings}",
    )
    state_verdicts: list[dict[str, Any]] = [
        {
            "constraint_id": "__required_axis_coverage__",
            "status": (
                "PASS"
                if not missing_bindings and not unexpected_bindings
                else "FAIL"
            ),
            "missing_bindings": missing_bindings,
            "unexpected_bindings": unexpected_bindings,
        }
    ]
    for constraint in acceptable.state_constraints:
        values = [
            binding_map.get((occurrence_id, constraint.axis))
            for occurrence_id in constraint.occurrence_ids
        ]
        if constraint.kind is StateConstraintKind.MUST_LINK:
            state_pass = None not in values and len(set(values)) == 1
        elif constraint.kind is StateConstraintKind.CANNOT_LINK:
            state_pass = None not in values and len(set(values)) == len(values)
        else:
            state_pass = None not in values and all(
                value == constraint.value_id for value in values
            )
        check(
            state_pass,
            "STATE_CONSTRAINT_UNSATISFIED",
            f"{constraint.constraint_id!r}: values={values}",
        )
        state_verdicts.append(
            {
                "constraint_id": constraint.constraint_id,
                "status": "PASS" if state_pass else "FAIL",
                "observed_values": values,
            }
        )

    status_map = {
        item.occurrence_id: item.status for item in candidate.legacy_statuses
    }
    expected_status_ids = {
        item.occurrence_id for item in acceptable.legacy_status_constraints
    }
    unexpected_status_ids = sorted(set(status_map) - expected_status_ids)
    if unexpected_status_ids:
        check(
            False,
            "LEGACY_STATUS_UNEXPECTED",
            f"occurrences={unexpected_status_ids}",
        )
    legacy_verdicts: list[dict[str, Any]] = []
    for constraint in acceptable.legacy_status_constraints:
        observed = status_map.get(constraint.occurrence_id)
        status_pass = observed in set(constraint.allowed_statuses)
        check(
            status_pass,
            "LEGACY_STATUS_UNACCEPTABLE",
            (
                f"{constraint.occurrence_id!r}: observed={observed!r}, "
                f"allowed={constraint.allowed_statuses}"
            ),
        )
        legacy_verdicts.append(
            {
                "occurrence_id": constraint.occurrence_id,
                "observed_status": observed,
                "allowed_statuses": list(constraint.allowed_statuses),
                "status": "PASS" if status_pass else "FAIL",
            }
        )

    structural_verdicts: list[dict[str, Any]] = []
    for constraint in acceptable.structural_constraints:
        parents = {
            relation.source_occurrence_id
            for relation in actual_relations
            if relation.target_occurrence_id == constraint.target_occurrence_id
            and relation.view is constraint.view
            and relation.relation is constraint.relation
        }
        structural_pass = len(parents) >= constraint.minimum
        check(
            structural_pass,
            "STRUCTURAL_CONSTRAINT_UNSATISFIED",
            (
                f"{constraint.constraint_id!r}: parents={sorted(parents)}, "
                f"minimum={constraint.minimum}"
            ),
        )
        structural_verdicts.append(
            {
                "constraint_id": constraint.constraint_id,
                "distinct_parent_ids": sorted(parents),
                "minimum": constraint.minimum,
                "status": "PASS" if structural_pass else "FAIL",
            }
        )

    per_view = _per_view_coverage(candidate, acceptable, selected_relations)
    overall = EvaluationVerdict.PASS if not failures else EvaluationVerdict.FAIL
    return SemanticEvaluation(
        candidate_id=candidate.candidate_id,
        acceptable_set_id=acceptable.acceptable_set_id,
        canonical_input_hashes={
            "candidate_sha256": candidate.canonical_sha256,
            "acceptable_set_sha256": acceptable.canonical_sha256,
        },
        occurrence_verdict=occurrence_verdict,
        required_relation_verdict=required_relation_verdict,
        relation_clause_verdicts=tuple(clause_verdicts),
        optional_relation_observations=optional_observations,
        forbidden_relation_verdict=forbidden_verdict,
        unmatched_relation_verdict=unmatched_verdict,
        state_constraint_verdicts=tuple(state_verdicts),
        legacy_status_verdicts=tuple(legacy_verdicts),
        structural_constraint_verdicts=tuple(structural_verdicts),
        per_view_coverage=per_view,
        errors=tuple(failures),
        overall_verdict=overall,
    )


def evaluate_candidate_value(
    candidate_value: Mapping[str, Any],
    acceptable: SemanticAcceptableSet,
) -> SemanticEvaluation:
    """Return INVALID instead of raising for a malformed candidate."""

    try:
        candidate = SemanticCandidate.from_dict(candidate_value)
    except SemanticValidationError as exc:
        candidate_id = candidate_value.get("candidate_id", "<invalid>")
        if not isinstance(candidate_id, str):
            candidate_id = "<invalid>"
        return SemanticEvaluation(
            candidate_id=candidate_id,
            acceptable_set_id=acceptable.acceptable_set_id,
            canonical_input_hashes={
                "candidate_sha256": _best_effort_sha256(candidate_value),
                "acceptable_set_sha256": acceptable.canonical_sha256,
            },
            occurrence_verdict={"status": "NOT_EVALUATED"},
            required_relation_verdict={"status": "NOT_EVALUATED"},
            relation_clause_verdicts=(),
            optional_relation_observations=(),
            forbidden_relation_verdict={"status": "NOT_EVALUATED"},
            unmatched_relation_verdict={"status": "NOT_EVALUATED"},
            state_constraint_verdicts=(),
            legacy_status_verdicts=(),
            structural_constraint_verdicts=(),
            per_view_coverage={},
            errors=({"code": exc.code, "message": exc.message},),
            overall_verdict=EvaluationVerdict.INVALID,
        )
    return evaluate_candidate(candidate, acceptable)


def sha256_json(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_json_strict(text: str) -> Any:
    try:
        return json.loads(text, parse_constant=_reject_nonfinite)
    except json.JSONDecodeError as exc:
        raise SemanticValidationError("JSON_INVALID", str(exc)) from exc


def _per_view_coverage(
    candidate: SemanticCandidate,
    acceptable: SemanticAcceptableSet,
    selected_relations: set[SemanticRelation],
) -> dict[str, Any]:
    actual = set(candidate.relations)
    required_for_run = set(acceptable.required_relations) | selected_relations
    allowed = set(acceptable.allowed_relations)
    forbidden = set(acceptable.forbidden_relations)
    result: dict[str, Any] = {}
    for view in RelationView:
        view_actual = {item for item in actual if item.view is view}
        view_required = {item for item in required_for_run if item.view is view}
        view_allowed = {item for item in allowed if item.view is view}
        view_forbidden = {item for item in forbidden if item.view is view}
        result[view.value] = {
            "required_count": len(view_required),
            "allowed_count": len(view_allowed),
            "candidate_count": len(view_actual),
            "matched_required_count": len(view_actual & view_required),
            "missing_required": _relations_to_dicts(view_required - view_actual),
            "forbidden_present": _relations_to_dicts(view_actual & view_forbidden),
            "unmatched": _relations_to_dicts(view_actual - view_allowed),
        }
    return result


def _parse_relation_list(value: Any, path: str) -> tuple[SemanticRelation, ...]:
    result = tuple(
        _parse_relation(item, f"{path}[{index}]")
        for index, item in enumerate(_list(value, path))
    )
    _reject_duplicates(result, "RELATION_DUPLICATE", path)
    return result


def _parse_relation(value: Any, path: str) -> SemanticRelation:
    item = _mapping(value, path)
    _exact_keys(
        item,
        {"source_occurrence_id", "target_occurrence_id", "view", "relation"},
        path,
    )
    view = _enum(RelationView, item["view"], f"{path}.view")
    relation = _enum(RelationKind, item["relation"], f"{path}.relation")
    if relation not in RELATIONS_BY_VIEW[view]:
        raise SemanticValidationError(
            "RELATION_VIEW_KIND_MISMATCH",
            f"{path}: {relation.value} is not valid in {view.value}",
        )
    return SemanticRelation(
        source_occurrence_id=_identifier(
            item["source_occurrence_id"], f"{path}.source_occurrence_id"
        ),
        target_occurrence_id=_identifier(
            item["target_occurrence_id"], f"{path}.target_occurrence_id"
        ),
        view=view,
        relation=relation,
    )


def _parse_state_binding(value: Any, path: str) -> StateBinding:
    item = _mapping(value, path)
    _exact_keys(item, {"occurrence_id", "axis", "value_id"}, path)
    return StateBinding(
        occurrence_id=_identifier(item["occurrence_id"], f"{path}.occurrence_id"),
        axis=_enum(StateAxis, item["axis"], f"{path}.axis"),
        value_id=_identifier(item["value_id"], f"{path}.value_id"),
    )


def _parse_legacy_status(value: Any, path: str) -> LegacyStatus:
    item = _mapping(value, path)
    _exact_keys(item, {"occurrence_id", "status"}, path)
    return LegacyStatus(
        occurrence_id=_identifier(item["occurrence_id"], f"{path}.occurrence_id"),
        status=_identifier(item["status"], f"{path}.status"),
    )


def _parse_relation_clause(value: Any, path: str) -> RelationClause:
    item = _mapping(value, path)
    _exact_keys(item, {"clause_id", "selection", "alternatives"}, path)
    alternatives = tuple(
        _parse_relation_alternative(alternative, f"{path}.alternatives[{index}]")
        for index, alternative in enumerate(
            _list(item["alternatives"], f"{path}.alternatives")
        )
    )
    _reject_duplicates(
        [alternative.alternative_id for alternative in alternatives],
        "RELATION_ALTERNATIVE_ID_DUPLICATE",
        f"{path}.alternatives",
    )
    return RelationClause(
        clause_id=_identifier(item["clause_id"], f"{path}.clause_id"),
        selection=_enum(ClauseSelection, item["selection"], f"{path}.selection"),
        alternatives=tuple(
            sorted(alternatives, key=lambda alternative: alternative.alternative_id)
        ),
    )


def _parse_relation_alternative(value: Any, path: str) -> RelationAlternative:
    item = _mapping(value, path)
    _exact_keys(item, {"alternative_id", "complete_relation_set"}, path)
    return RelationAlternative(
        alternative_id=_identifier(
            item["alternative_id"], f"{path}.alternative_id"
        ),
        complete_relation_set=tuple(
            sorted(
                _parse_relation_list(
                    item["complete_relation_set"], f"{path}.complete_relation_set"
                )
            )
        ),
    )


def _parse_state_constraint(value: Any, path: str) -> StateConstraint:
    item = _mapping(value, path)
    kind = _enum(StateConstraintKind, item.get("kind"), f"{path}.kind")
    expected = {"constraint_id", "kind", "axis", "occurrence_ids"}
    if kind is StateConstraintKind.EXACT_VALUE:
        expected.add("value_id")
    _exact_keys(item, expected, path)
    occurrence_ids = _unique_identifiers(
        item["occurrence_ids"], f"{path}.occurrence_ids"
    )
    if kind is StateConstraintKind.CANNOT_LINK and len(occurrence_ids) < 2:
        raise SemanticValidationError(
            "STATE_CONSTRAINT_ARITY",
            f"{path}: CANNOT_LINK needs at least two occurrences",
        )
    if kind is StateConstraintKind.MUST_LINK and len(occurrence_ids) < 2:
        raise SemanticValidationError(
            "STATE_CONSTRAINT_ARITY",
            f"{path}: MUST_LINK needs at least two occurrences",
        )
    if kind is StateConstraintKind.EXACT_VALUE and not occurrence_ids:
        raise SemanticValidationError(
            "STATE_CONSTRAINT_ARITY",
            f"{path}: EXACT_VALUE needs at least one occurrence",
        )
    return StateConstraint(
        constraint_id=_identifier(item["constraint_id"], f"{path}.constraint_id"),
        kind=kind,
        axis=_enum(StateAxis, item["axis"], f"{path}.axis"),
        occurrence_ids=tuple(sorted(occurrence_ids)),
        value_id=(
            _identifier(item["value_id"], f"{path}.value_id")
            if kind is StateConstraintKind.EXACT_VALUE
            else None
        ),
    )


def _parse_legacy_status_constraint(
    value: Any, path: str
) -> LegacyStatusConstraint:
    item = _mapping(value, path)
    _exact_keys(item, {"occurrence_id", "allowed_statuses"}, path)
    statuses = _unique_identifiers(
        item["allowed_statuses"], f"{path}.allowed_statuses"
    )
    if not statuses:
        raise SemanticValidationError(
            "LEGACY_ALLOWED_STATUSES_EMPTY",
            f"{path}.allowed_statuses must not be empty",
        )
    return LegacyStatusConstraint(
        occurrence_id=_identifier(item["occurrence_id"], f"{path}.occurrence_id"),
        allowed_statuses=tuple(sorted(statuses)),
    )


def _parse_structural_constraint(value: Any, path: str) -> StructuralConstraint:
    item = _mapping(value, path)
    _exact_keys(
        item,
        {
            "constraint_id",
            "kind",
            "target_occurrence_id",
            "view",
            "relation",
            "minimum",
        },
        path,
    )
    kind = _enum(StructuralConstraintKind, item["kind"], f"{path}.kind")
    view = _enum(RelationView, item["view"], f"{path}.view")
    relation = _enum(RelationKind, item["relation"], f"{path}.relation")
    if relation not in RELATIONS_BY_VIEW[view]:
        raise SemanticValidationError(
            "RELATION_VIEW_KIND_MISMATCH",
            f"{path}: {relation.value} is not valid in {view.value}",
        )
    minimum = _integer(item["minimum"], f"{path}.minimum")
    if minimum < 1:
        raise SemanticValidationError(
            "STRUCTURAL_MINIMUM_INVALID", f"{path}.minimum must be positive"
        )
    return StructuralConstraint(
        constraint_id=_identifier(item["constraint_id"], f"{path}.constraint_id"),
        kind=kind,
        target_occurrence_id=_identifier(
            item["target_occurrence_id"], f"{path}.target_occurrence_id"
        ),
        view=view,
        relation=relation,
        minimum=minimum,
    )


def _relations_to_dicts(
    relations: Any,
) -> list[dict[str, str]]:
    return [item.to_dict() for item in sorted(relations)]


def _schema(root: Mapping[str, Any], expected: str, path: str) -> None:
    actual = _string(root["schema_version"], f"{path}.schema_version")
    if actual != expected:
        raise SemanticValidationError(
            "SCHEMA_VERSION_UNSUPPORTED",
            f"{path}: expected {expected!r}, got {actual!r}",
        )


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise SemanticValidationError("TYPE_OBJECT_REQUIRED", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise SemanticValidationError("TYPE_ARRAY_REQUIRED", path)
    return value


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str):
        raise SemanticValidationError("TYPE_STRING_REQUIRED", path)
    return value


def _identifier(value: Any, path: str) -> str:
    result = _string(value, path)
    if not result or result.strip() != result:
        raise SemanticValidationError(
            "IDENTIFIER_INVALID", f"{path} must be non-empty and trimmed"
        )
    return result


def _integer(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise SemanticValidationError("TYPE_INTEGER_REQUIRED", path)
    return value


def _enum(enum_type: type[StrEnum], value: Any, path: str) -> Any:
    raw = _string(value, path)
    try:
        return enum_type(raw)
    except ValueError as exc:
        raise SemanticValidationError(
            "ENUM_VALUE_INVALID", f"{path}: {raw!r}"
        ) from exc


def _exact_keys(
    value: Mapping[str, Any], expected: set[str], path: str
) -> None:
    actual = set(value)
    missing = sorted(expected - actual)
    unknown = sorted(actual - expected)
    if missing or unknown:
        raise SemanticValidationError(
            "OBJECT_KEYS_INVALID",
            f"{path}: missing={missing}, unknown={unknown}",
        )


def _unique_identifiers(value: Any, path: str) -> tuple[str, ...]:
    items = tuple(
        _identifier(item, f"{path}[{index}]")
        for index, item in enumerate(_list(value, path))
    )
    _reject_duplicates(items, "IDENTIFIER_DUPLICATE", path)
    return items


def _reject_duplicates(values: Any, code: str, path: str) -> None:
    sequence = list(values)
    if len(sequence) != len(set(sequence)):
        raise SemanticValidationError(code, path)


def _reject_nonfinite(value: str) -> None:
    raise SemanticValidationError("JSON_NONFINITE_NUMBER", value)


def _best_effort_sha256(value: Any) -> str:
    try:
        return sha256_json(value)
    except (TypeError, ValueError):
        return hashlib.sha256(repr(value).encode("utf-8")).hexdigest()
