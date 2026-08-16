"""Deterministic multi-axis state normalization for solve-side trajectories.

The state normalizer is the component that prevents a single legacy
``canonical_math_state_id`` from carrying all semantic load.  It maps raw
axis-value claims to explicit canonical values and evaluates multi-axis
must-link/cannot-link/exact-value constraints.  This module is deterministic and
does not call models, solvers, databases, Redis, or the network.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.semantic_truth import StateAxis, StateConstraintKind


INPUT_SCHEMA_VERSION = "solve-vein/state-normalization-input/v1"
DICTIONARY_SCHEMA_VERSION = "solve-vein/state-normalization-dictionary/v1"
ACCEPTABLE_SET_SCHEMA_VERSION = "solve-vein/state-normalization-acceptable-set/v1"
NORMALIZED_BUNDLE_SCHEMA_VERSION = "solve-vein/state-normalized-bundle/v1"
EVALUATION_SCHEMA_VERSION = "solve-vein/state-normalization-evaluation/v1"


class StateNormalizationValidationError(ValueError):
    """A fail-closed normalization error with a stable machine code."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


class StateNormalizationVerdict(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    INVALID = "INVALID"


@dataclass(frozen=True, slots=True)
class StateValueDictionaryEntry:
    axis: StateAxis
    value_id: str
    aliases: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "axis": self.axis.value,
            "value_id": self.value_id,
            "aliases": list(self.aliases),
        }


@dataclass(frozen=True, slots=True)
class RawAxisClaim:
    occurrence_id: str
    axis: StateAxis
    raw_value: str

    def to_dict(self) -> dict[str, str]:
        return {
            "occurrence_id": self.occurrence_id,
            "axis": self.axis.value,
            "raw_value": self.raw_value,
        }


@dataclass(frozen=True, slots=True)
class NormalizedStateBinding:
    occurrence_id: str
    axis: StateAxis
    value_id: str
    raw_value: str

    def to_dict(self) -> dict[str, str]:
        return {
            "occurrence_id": self.occurrence_id,
            "axis": self.axis.value,
            "value_id": self.value_id,
            "raw_value": self.raw_value,
        }


@dataclass(frozen=True, slots=True)
class StateNormalizationInput:
    case_id: str
    candidate_id: str
    occurrence_ids: tuple[str, ...]
    raw_axis_claims: tuple[RawAxisClaim, ...]

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "StateNormalizationInput":
        root = _mapping(value, "input")
        _exact_keys(
            root,
            {
                "schema_version",
                "case_id",
                "candidate_id",
                "occurrence_ids",
                "raw_axis_claims",
            },
            "input",
        )
        _schema(root, INPUT_SCHEMA_VERSION, "input")
        occurrence_ids = _unique_identifiers(root["occurrence_ids"], "occurrence_ids")
        if not occurrence_ids:
            raise StateNormalizationValidationError("OCCURRENCE_SET_EMPTY", "no occurrence IDs")
        claims = tuple(
            _parse_raw_axis_claim(item, f"raw_axis_claims[{index}]")
            for index, item in enumerate(_list(root["raw_axis_claims"], "raw_axis_claims"))
        )
        _reject_duplicates(
            [(claim.occurrence_id, claim.axis) for claim in claims],
            "RAW_AXIS_CLAIM_DUPLICATE",
            "raw_axis_claims",
        )
        known = set(occurrence_ids)
        for claim in claims:
            if claim.occurrence_id not in known:
                raise StateNormalizationValidationError(
                    "RAW_AXIS_CLAIM_OCCURRENCE_UNKNOWN",
                    f"{claim.occurrence_id!r}",
                )
        return cls(
            case_id=_identifier(root["case_id"], "case_id"),
            candidate_id=_identifier(root["candidate_id"], "candidate_id"),
            occurrence_ids=tuple(sorted(occurrence_ids)),
            raw_axis_claims=tuple(sorted(claims, key=lambda item: (item.occurrence_id, item.axis.value))),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": INPUT_SCHEMA_VERSION,
            "case_id": self.case_id,
            "candidate_id": self.candidate_id,
            "occurrence_ids": list(self.occurrence_ids),
            "raw_axis_claims": [claim.to_dict() for claim in self.raw_axis_claims],
        }

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(self.to_dict())


@dataclass(frozen=True, slots=True)
class StateValueDictionary:
    dictionary_id: str
    case_id: str
    entries: tuple[StateValueDictionaryEntry, ...]

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "StateValueDictionary":
        root = _mapping(value, "dictionary")
        _exact_keys(root, {"schema_version", "dictionary_id", "case_id", "entries"}, "dictionary")
        _schema(root, DICTIONARY_SCHEMA_VERSION, "dictionary")
        entries = tuple(
            _parse_dictionary_entry(item, f"entries[{index}]")
            for index, item in enumerate(_list(root["entries"], "entries"))
        )
        if not entries:
            raise StateNormalizationValidationError("DICTIONARY_EMPTY", "entries must not be empty")
        _reject_duplicates(
            [(entry.axis, entry.value_id) for entry in entries],
            "DICTIONARY_VALUE_DUPLICATE",
            "entries",
        )
        alias_keys: list[tuple[StateAxis, str]] = []
        for entry in entries:
            alias_keys.extend((entry.axis, _alias_key(alias)) for alias in entry.aliases)
        _reject_duplicates(alias_keys, "DICTIONARY_ALIAS_DUPLICATE", "entries.aliases")
        return cls(
            dictionary_id=_identifier(root["dictionary_id"], "dictionary_id"),
            case_id=_identifier(root["case_id"], "case_id"),
            entries=tuple(sorted(entries, key=lambda item: (item.axis.value, item.value_id))),
        )

    def lookup(self, axis: StateAxis, raw_value: str) -> str:
        key = _alias_key(raw_value)
        for entry in self.entries:
            if entry.axis is axis and key in {_alias_key(alias) for alias in entry.aliases}:
                return entry.value_id
        raise StateNormalizationValidationError(
            "DICTIONARY_ALIAS_UNKNOWN",
            f"{axis.value}:{raw_value!r}",
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": DICTIONARY_SCHEMA_VERSION,
            "dictionary_id": self.dictionary_id,
            "case_id": self.case_id,
            "entries": [entry.to_dict() for entry in self.entries],
        }

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(self.to_dict())


@dataclass(frozen=True, slots=True)
class StateNormalizationAcceptableSet:
    acceptable_set_id: str
    case_id: str
    expected_occurrence_ids: tuple[str, ...]
    required_axes: tuple[StateAxis, ...]
    state_constraints: tuple[Mapping[str, Any], ...]
    legacy_projection_axes: tuple[StateAxis, ...]

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "StateNormalizationAcceptableSet":
        root = _mapping(value, "acceptable_set")
        _exact_keys(
            root,
            {
                "schema_version",
                "acceptable_set_id",
                "case_id",
                "expected_occurrence_ids",
                "required_axes",
                "state_constraints",
                "legacy_projection_axes",
            },
            "acceptable_set",
        )
        _schema(root, ACCEPTABLE_SET_SCHEMA_VERSION, "acceptable_set")
        occurrence_ids = _unique_identifiers(root["expected_occurrence_ids"], "expected_occurrence_ids")
        axes = tuple(
            _enum(StateAxis, item, f"required_axes[{index}]")
            for index, item in enumerate(_list(root["required_axes"], "required_axes"))
        )
        if not axes:
            raise StateNormalizationValidationError("REQUIRED_AXES_EMPTY", "required axes empty")
        _reject_duplicates(axes, "REQUIRED_AXIS_DUPLICATE", "required_axes")
        constraints = tuple(
            _parse_state_constraint(item, f"state_constraints[{index}]")
            for index, item in enumerate(_list(root["state_constraints"], "state_constraints"))
        )
        _reject_duplicates(
            [constraint["constraint_id"] for constraint in constraints],
            "STATE_CONSTRAINT_ID_DUPLICATE",
            "state_constraints",
        )
        projection_axes = tuple(
            _enum(StateAxis, item, f"legacy_projection_axes[{index}]")
            for index, item in enumerate(_list(root["legacy_projection_axes"], "legacy_projection_axes"))
        )
        if not set(projection_axes).issubset(set(axes)):
            raise StateNormalizationValidationError(
                "LEGACY_PROJECTION_AXIS_NOT_REQUIRED",
                "projection axes must be a subset of required axes",
            )
        known = set(occurrence_ids)
        axis_set = set(axes)
        for constraint in constraints:
            if constraint["axis"] not in axis_set:
                raise StateNormalizationValidationError(
                    "STATE_CONSTRAINT_AXIS_NOT_REQUIRED",
                    constraint["constraint_id"],
                )
            if not set(constraint["occurrence_ids"]).issubset(known):
                raise StateNormalizationValidationError(
                    "STATE_CONSTRAINT_OCCURRENCE_UNKNOWN",
                    constraint["constraint_id"],
                )
        return cls(
            acceptable_set_id=_identifier(root["acceptable_set_id"], "acceptable_set_id"),
            case_id=_identifier(root["case_id"], "case_id"),
            expected_occurrence_ids=tuple(sorted(occurrence_ids)),
            required_axes=tuple(sorted(axes)),
            state_constraints=tuple(sorted(constraints, key=lambda item: item["constraint_id"])),
            legacy_projection_axes=tuple(sorted(projection_axes)),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": ACCEPTABLE_SET_SCHEMA_VERSION,
            "acceptable_set_id": self.acceptable_set_id,
            "case_id": self.case_id,
            "expected_occurrence_ids": list(self.expected_occurrence_ids),
            "required_axes": [axis.value for axis in self.required_axes],
            "state_constraints": [
                _constraint_to_dict(constraint) for constraint in self.state_constraints
            ],
            "legacy_projection_axes": [axis.value for axis in self.legacy_projection_axes],
        }

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(self.to_dict())


@dataclass(frozen=True, slots=True)
class StateNormalizedBundle:
    case_id: str
    candidate_id: str
    occurrence_ids: tuple[str, ...]
    state_bindings: tuple[NormalizedStateBinding, ...]
    legacy_projection_axes: tuple[StateAxis, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": NORMALIZED_BUNDLE_SCHEMA_VERSION,
            "case_id": self.case_id,
            "candidate_id": self.candidate_id,
            "occurrence_ids": list(self.occurrence_ids),
            "state_bindings": [binding.to_dict() for binding in self.state_bindings],
            "legacy_projection_axes": [axis.value for axis in self.legacy_projection_axes],
            "legacy_projection": self.legacy_projection(),
        }

    def binding_map(self) -> dict[tuple[str, StateAxis], str]:
        return {
            (binding.occurrence_id, binding.axis): binding.value_id
            for binding in self.state_bindings
        }

    def legacy_projection(self) -> dict[str, str]:
        bindings = self.binding_map()
        result: dict[str, str] = {}
        for occurrence_id in self.occurrence_ids:
            values = [
                bindings[(occurrence_id, axis)]
                for axis in self.legacy_projection_axes
                if (occurrence_id, axis) in bindings
            ]
            result[occurrence_id] = "::".join(values)
        return result

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(self.to_dict())


def normalize_state_claims(
    input_value: Mapping[str, Any],
    dictionary_value: Mapping[str, Any],
    *,
    legacy_projection_axes: tuple[StateAxis, ...] = (StateAxis.PROBLEM_OBLIGATION,),
) -> StateNormalizedBundle:
    source = StateNormalizationInput.from_dict(input_value)
    dictionary = StateValueDictionary.from_dict(dictionary_value)
    if source.case_id != dictionary.case_id:
        raise StateNormalizationValidationError(
            "CASE_ID_MISMATCH",
            f"input={source.case_id!r}, dictionary={dictionary.case_id!r}",
        )
    bindings = tuple(
        NormalizedStateBinding(
            occurrence_id=claim.occurrence_id,
            axis=claim.axis,
            value_id=dictionary.lookup(claim.axis, claim.raw_value),
            raw_value=claim.raw_value,
        )
        for claim in source.raw_axis_claims
    )
    return StateNormalizedBundle(
        case_id=source.case_id,
        candidate_id=source.candidate_id,
        occurrence_ids=source.occurrence_ids,
        state_bindings=tuple(sorted(bindings, key=lambda item: (item.occurrence_id, item.axis.value))),
        legacy_projection_axes=legacy_projection_axes,
    )


def evaluate_normalized_bundle(
    bundle: StateNormalizedBundle,
    acceptable: StateNormalizationAcceptableSet,
) -> dict[str, Any]:
    failures: list[dict[str, str]] = []

    def fail(code: str, message: str) -> None:
        failures.append({"code": code, "message": message})

    if bundle.case_id != acceptable.case_id:
        fail("CASE_ID_MISMATCH", f"bundle={bundle.case_id!r}, acceptable={acceptable.case_id!r}")
    expected_occurrences = set(acceptable.expected_occurrence_ids)
    actual_occurrences = set(bundle.occurrence_ids)
    missing_occurrences = sorted(expected_occurrences - actual_occurrences)
    unknown_occurrences = sorted(actual_occurrences - expected_occurrences)
    if missing_occurrences or unknown_occurrences:
        fail("OCCURRENCE_SET_MISMATCH", f"missing={missing_occurrences}, unknown={unknown_occurrences}")

    binding_map = bundle.binding_map()
    expected_keys = {
        (occurrence_id, axis)
        for occurrence_id in acceptable.expected_occurrence_ids
        for axis in acceptable.required_axes
    }
    actual_keys = set(binding_map)
    missing_bindings = _binding_key_dicts(expected_keys - actual_keys)
    unexpected_bindings = _binding_key_dicts(actual_keys - expected_keys)
    if missing_bindings or unexpected_bindings:
        fail("STATE_BINDING_COVERAGE_MISMATCH", f"missing={missing_bindings}, unexpected={unexpected_bindings}")

    constraint_verdicts: list[dict[str, Any]] = []
    for constraint in acceptable.state_constraints:
        axis = constraint["axis"]
        values = [
            binding_map.get((occurrence_id, axis))
            for occurrence_id in constraint["occurrence_ids"]
        ]
        kind = constraint["kind"]
        if kind is StateConstraintKind.MUST_LINK:
            passed = None not in values and len(set(values)) == 1
        elif kind is StateConstraintKind.CANNOT_LINK:
            passed = None not in values and len(set(values)) == len(values)
        else:
            passed = None not in values and all(value == constraint["value_id"] for value in values)
        if not passed:
            fail("STATE_CONSTRAINT_UNSATISFIED", f"{constraint['constraint_id']}: values={values}")
        constraint_verdicts.append(
            {
                "constraint_id": constraint["constraint_id"],
                "kind": kind.value,
                "axis": axis.value,
                "observed_values": values,
                "status": "PASS" if passed else "FAIL",
            }
        )

    coverage = {
        "status": "PASS" if not missing_bindings and not unexpected_bindings else "FAIL",
        "missing_bindings": missing_bindings,
        "unexpected_bindings": unexpected_bindings,
    }
    verdict = StateNormalizationVerdict.PASS if not failures else StateNormalizationVerdict.FAIL
    return {
        "schema_version": EVALUATION_SCHEMA_VERSION,
        "case_id": bundle.case_id,
        "candidate_id": bundle.candidate_id,
        "canonical_input_hashes": {
            "normalized_bundle_sha256": bundle.canonical_sha256,
            "acceptable_set_sha256": acceptable.canonical_sha256,
        },
        "occurrence_verdict": {
            "status": "PASS" if not missing_occurrences and not unknown_occurrences else "FAIL",
            "missing_occurrence_ids": missing_occurrences,
            "unknown_occurrence_ids": unknown_occurrences,
        },
        "axis_coverage_verdict": coverage,
        "state_constraint_verdicts": constraint_verdicts,
        "legacy_projection": bundle.legacy_projection(),
        "errors": failures,
        "overall_verdict": verdict.value,
    }


def evaluate_state_normalization_value(
    input_value: Mapping[str, Any],
    dictionary_value: Mapping[str, Any],
    acceptable_value: Mapping[str, Any],
) -> dict[str, Any]:
    try:
        acceptable = StateNormalizationAcceptableSet.from_dict(acceptable_value)
        bundle = normalize_state_claims(
            input_value,
            dictionary_value,
            legacy_projection_axes=acceptable.legacy_projection_axes,
        )
        return evaluate_normalized_bundle(bundle, acceptable)
    except StateNormalizationValidationError as exc:
        return {
            "schema_version": EVALUATION_SCHEMA_VERSION,
            "case_id": _safe_case_id(input_value),
            "candidate_id": _safe_candidate_id(input_value),
            "canonical_input_hashes": {
                "input_sha256": _best_effort_sha256(input_value),
                "dictionary_sha256": _best_effort_sha256(dictionary_value),
                "acceptable_set_sha256": _best_effort_sha256(acceptable_value),
            },
            "occurrence_verdict": {"status": "NOT_EVALUATED"},
            "axis_coverage_verdict": {"status": "NOT_EVALUATED"},
            "state_constraint_verdicts": [],
            "legacy_projection": {},
            "errors": [{"code": exc.code, "message": exc.message}],
            "overall_verdict": StateNormalizationVerdict.INVALID.value,
        }


def evaluate_state_normalization_pack(pack_value: Mapping[str, Any]) -> dict[str, Any]:
    root = _mapping(pack_value, "pack")
    _exact_keys(root, {"schema_version", "pack_id", "cases"}, "pack")
    _schema(root, "solve-vein/state-normalization-pack/v1", "pack")
    rows: list[dict[str, Any]] = []
    for case in _list(root["cases"], "cases"):
        case_root = _mapping(case, "case")
        _exact_keys(case_root, {"case_id", "dictionary", "acceptable_set", "candidates"}, "case")
        for spec in _list(case_root["candidates"], f"{case_root.get('case_id', '<unknown>')}.candidates"):
            spec_root = _mapping(spec, "candidate_spec")
            _exact_keys(spec_root, {"label", "input", "expected_verdict"}, "candidate_spec")
            evaluation = evaluate_state_normalization_value(
                spec_root["input"], case_root["dictionary"], case_root["acceptable_set"]
            )
            rows.append(
                {
                    "case_id": case_root["case_id"],
                    "label": spec_root["label"],
                    "expected_verdict": spec_root["expected_verdict"],
                    "observed_verdict": evaluation["overall_verdict"],
                    "status": (
                        "PASS"
                        if evaluation["overall_verdict"] == spec_root["expected_verdict"]
                        else "FAIL"
                    ),
                    "evaluation": evaluation,
                }
            )
    return {
        "schema_version": "solve-vein/state-normalization-pack-evaluation/v1",
        "pack_id": root["pack_id"],
        "case_count": len(root["cases"]),
        "candidate_count": len(rows),
        "mismatch_count": sum(1 for row in rows if row["status"] != "PASS"),
        "rows": rows,
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "solver_calls": 0,
        },
        "overall_verdict": "PASS" if all(row["status"] == "PASS" for row in rows) else "FAIL",
    }


def sha256_json(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pack", type=Path, required=True)
    args = parser.parse_args()
    pack = json.loads(args.pack.read_text(), parse_constant=_reject_nonfinite)
    print(json.dumps(evaluate_state_normalization_pack(pack), ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _parse_raw_axis_claim(value: Any, path: str) -> RawAxisClaim:
    item = _mapping(value, path)
    _exact_keys(item, {"occurrence_id", "axis", "raw_value"}, path)
    return RawAxisClaim(
        occurrence_id=_identifier(item["occurrence_id"], f"{path}.occurrence_id"),
        axis=_enum(StateAxis, item["axis"], f"{path}.axis"),
        raw_value=_nonempty_string(item["raw_value"], f"{path}.raw_value"),
    )


def _parse_dictionary_entry(value: Any, path: str) -> StateValueDictionaryEntry:
    item = _mapping(value, path)
    _exact_keys(item, {"axis", "value_id", "aliases"}, path)
    aliases = tuple(
        _nonempty_string(alias, f"{path}.aliases[{index}]")
        for index, alias in enumerate(_list(item["aliases"], f"{path}.aliases"))
    )
    if not aliases:
        raise StateNormalizationValidationError("DICTIONARY_ALIASES_EMPTY", path)
    return StateValueDictionaryEntry(
        axis=_enum(StateAxis, item["axis"], f"{path}.axis"),
        value_id=_identifier(item["value_id"], f"{path}.value_id"),
        aliases=tuple(sorted(aliases)),
    )


def _parse_state_constraint(value: Any, path: str) -> dict[str, Any]:
    item = _mapping(value, path)
    _exact_keys(item, {"constraint_id", "kind", "axis", "occurrence_ids", "value_id"}, path)
    kind = _enum(StateConstraintKind, item["kind"], f"{path}.kind")
    value_id_raw = item["value_id"]
    value_id = None if value_id_raw is None else _identifier(value_id_raw, f"{path}.value_id")
    if kind is StateConstraintKind.EXACT_VALUE and value_id is None:
        raise StateNormalizationValidationError("STATE_CONSTRAINT_VALUE_REQUIRED", path)
    if kind is not StateConstraintKind.EXACT_VALUE and value_id is not None:
        raise StateNormalizationValidationError("STATE_CONSTRAINT_VALUE_FORBIDDEN", path)
    occurrence_ids = tuple(sorted(_unique_identifiers(item["occurrence_ids"], f"{path}.occurrence_ids")))
    if len(occurrence_ids) < 1:
        raise StateNormalizationValidationError("STATE_CONSTRAINT_OCCURRENCES_EMPTY", path)
    if kind in {StateConstraintKind.MUST_LINK, StateConstraintKind.CANNOT_LINK} and len(occurrence_ids) < 2:
        raise StateNormalizationValidationError("STATE_CONSTRAINT_NEEDS_PAIR", path)
    return {
        "constraint_id": _identifier(item["constraint_id"], f"{path}.constraint_id"),
        "kind": kind,
        "axis": _enum(StateAxis, item["axis"], f"{path}.axis"),
        "occurrence_ids": occurrence_ids,
        "value_id": value_id,
    }


def _constraint_to_dict(constraint: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "constraint_id": constraint["constraint_id"],
        "kind": constraint["kind"].value,
        "axis": constraint["axis"].value,
        "occurrence_ids": list(constraint["occurrence_ids"]),
        "value_id": constraint["value_id"],
    }


def _binding_key_dicts(keys: set[tuple[str, StateAxis]]) -> list[dict[str, str]]:
    return [
        {"occurrence_id": occurrence_id, "axis": axis.value}
        for occurrence_id, axis in sorted(keys, key=lambda item: (item[0], item[1].value))
    ]


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise StateNormalizationValidationError("OBJECT_EXPECTED", path)
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise StateNormalizationValidationError("ARRAY_EXPECTED", path)
    return value


def _exact_keys(value: Mapping[str, Any], expected: set[str], path: str) -> None:
    actual = set(value)
    if actual != expected:
        raise StateNormalizationValidationError(
            "OBJECT_KEYS_INVALID",
            f"{path}: missing={sorted(expected - actual)}, unknown={sorted(actual - expected)}",
        )


def _schema(value: Mapping[str, Any], expected: str, path: str) -> None:
    if value.get("schema_version") != expected:
        raise StateNormalizationValidationError(
            "SCHEMA_VERSION_UNSUPPORTED",
            f"{path}: expected {expected!r}, got {value.get('schema_version')!r}",
        )


def _identifier(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value or any(ch.isspace() for ch in value):
        raise StateNormalizationValidationError("IDENTIFIER_INVALID", path)
    return value


def _nonempty_string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise StateNormalizationValidationError("STRING_EMPTY", path)
    return value


def _unique_identifiers(value: Any, path: str) -> tuple[str, ...]:
    items = tuple(_identifier(item, f"{path}[{index}]") for index, item in enumerate(_list(value, path)))
    _reject_duplicates(items, "IDENTIFIER_DUPLICATE", path)
    return items


def _enum(enum_type: type[StrEnum], value: Any, path: str) -> Any:
    if not isinstance(value, str):
        raise StateNormalizationValidationError("ENUM_VALUE_INVALID", path)
    try:
        return enum_type(value)
    except ValueError as exc:
        raise StateNormalizationValidationError("ENUM_VALUE_INVALID", f"{path}: {value!r}") from exc


def _reject_duplicates(values: list[Any] | tuple[Any, ...], code: str, path: str) -> None:
    if len(values) != len(set(values)):
        raise StateNormalizationValidationError(code, path)


def _alias_key(value: str) -> str:
    return " ".join(value.strip().casefold().split())


def _safe_case_id(value: Mapping[str, Any]) -> str:
    case_id = value.get("case_id") if isinstance(value, Mapping) else None
    return case_id if isinstance(case_id, str) else "<invalid>"


def _safe_candidate_id(value: Mapping[str, Any]) -> str:
    candidate_id = value.get("candidate_id") if isinstance(value, Mapping) else None
    return candidate_id if isinstance(candidate_id, str) else "<invalid>"


def _best_effort_sha256(value: Any) -> str:
    try:
        return sha256_json(value)
    except (TypeError, ValueError):
        return "<unhashable>"


def _reject_nonfinite(value: str) -> None:
    raise StateNormalizationValidationError("JSON_NONFINITE", value)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, StateNormalizationValidationError) as exc:
        print(f"STATE_NORMALIZATION_ERROR: {exc}", file=__import__("sys").stderr)
        raise SystemExit(2) from exc
