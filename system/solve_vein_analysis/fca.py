"""Deterministic Formal Concept Analysis primitives for the solve-side POC."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any, Iterable, Mapping

from .models import sha256_json


class FormalContextError(ValueError):
    """Raised when a formal context violates its data contract."""


@dataclass(frozen=True, slots=True)
class FormalContext:
    """A finite binary formal context K=(G, M, I)."""

    context_id: str
    objects: tuple[str, ...]
    attributes: tuple[str, ...]
    incidence: Mapping[str, frozenset[str]]

    def __post_init__(self) -> None:
        if not self.context_id:
            raise FormalContextError("context_id must not be empty")
        if not self.objects:
            raise FormalContextError("objects must not be empty")
        if len(self.objects) != len(set(self.objects)):
            raise FormalContextError("objects must be unique")
        if tuple(sorted(self.objects)) != self.objects:
            raise FormalContextError("objects must use canonical sorted order")
        if len(self.attributes) != len(set(self.attributes)):
            raise FormalContextError("attributes must be unique")
        if tuple(sorted(self.attributes)) != self.attributes:
            raise FormalContextError("attributes must use canonical sorted order")
        if set(self.incidence) != set(self.objects):
            raise FormalContextError("incidence keys must equal the object set")
        allowed = set(self.attributes)
        for object_id, object_attributes in self.incidence.items():
            unknown = set(object_attributes) - allowed
            if unknown:
                raise FormalContextError(
                    f"object {object_id!r} has unknown attributes {sorted(unknown)!r}"
                )

    @classmethod
    def from_incidence(
        cls,
        context_id: str,
        incidence: Mapping[str, Iterable[str]],
    ) -> "FormalContext":
        objects = tuple(sorted(incidence))
        normalized = {
            object_id: frozenset(str(attribute) for attribute in incidence[object_id])
            for object_id in objects
        }
        attributes = tuple(sorted({item for values in normalized.values() for item in values}))
        return cls(context_id, objects, attributes, normalized)

    def object_prime(self, object_subset: Iterable[str]) -> frozenset[str]:
        """Return all attributes common to every object in ``object_subset``."""

        selected = frozenset(object_subset)
        unknown = selected - set(self.objects)
        if unknown:
            raise FormalContextError(f"unknown objects: {sorted(unknown)!r}")
        if not selected:
            return frozenset(self.attributes)
        iterator = iter(sorted(selected))
        shared = set(self.incidence[next(iterator)])
        for object_id in iterator:
            shared.intersection_update(self.incidence[object_id])
        return frozenset(shared)

    def attribute_prime(self, attribute_subset: Iterable[str]) -> frozenset[str]:
        """Return all objects that have every selected attribute."""

        selected = frozenset(attribute_subset)
        unknown = selected - set(self.attributes)
        if unknown:
            raise FormalContextError(f"unknown attributes: {sorted(unknown)!r}")
        return frozenset(
            object_id
            for object_id in self.objects
            if selected.issubset(self.incidence[object_id])
        )

    def closure(self, attribute_subset: Iterable[str]) -> frozenset[str]:
        selected = frozenset(attribute_subset)
        return self.object_prime(self.attribute_prime(selected))

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": "solve-vein/formal-context/v1",
            "context_id": self.context_id,
            "objects": list(self.objects),
            "attributes": list(self.attributes),
            "incidence": {
                object_id: sorted(self.incidence[object_id]) for object_id in self.objects
            },
            "context_sha256": self.canonical_sha256,
        }

    @property
    def canonical_sha256(self) -> str:
        return sha256_json(
            {
                "context_id": self.context_id,
                "objects": list(self.objects),
                "attributes": list(self.attributes),
                "incidence": {
                    object_id: sorted(self.incidence[object_id]) for object_id in self.objects
                },
            }
        )


@dataclass(frozen=True, slots=True)
class FormalConcept:
    extent: tuple[str, ...]
    intent: tuple[str, ...]
    fingerprint: str

    @classmethod
    def from_intent(cls, context: FormalContext, intent: Iterable[str]) -> "FormalConcept":
        closed_intent = tuple(sorted(context.closure(intent)))
        extent = tuple(sorted(context.attribute_prime(closed_intent)))
        fingerprint = sha256_json({"extent": extent, "intent": closed_intent})
        return cls(extent=extent, intent=closed_intent, fingerprint=fingerprint)

    def to_dict(self) -> dict[str, Any]:
        return {
            "extent": list(self.extent),
            "intent": list(self.intent),
            "fingerprint": self.fingerprint,
        }


def enumerate_closed_intents_next_closure(context: FormalContext) -> tuple[frozenset[str], ...]:
    """Enumerate every closed intent in deterministic lectic order.

    This is a direct finite implementation of Ganter's Next Closure scheme.
    It is intentionally paired with an independent brute-force oracle in the
    POC test suite.
    """

    ordered_attributes = context.attributes
    current = context.closure(())
    result: list[frozenset[str]] = [current]
    seen = {current}

    while current != frozenset(ordered_attributes):
        next_intent: frozenset[str] | None = None
        for index in range(len(ordered_attributes) - 1, -1, -1):
            attribute = ordered_attributes[index]
            if attribute in current:
                continue
            prefix = {ordered_attributes[j] for j in range(index) if ordered_attributes[j] in current}
            candidate = context.closure(prefix | {attribute})
            is_lectic_successor = all(
                ordered_attributes[j] not in candidate or ordered_attributes[j] in current
                for j in range(index)
            )
            if is_lectic_successor:
                next_intent = candidate
                break
        if next_intent is None:
            raise FormalContextError("Next Closure could not find a successor")
        if next_intent in seen:
            raise FormalContextError("Next Closure repeated a closed intent")
        result.append(next_intent)
        seen.add(next_intent)
        current = next_intent

    return tuple(result)


def enumerate_closed_intents_bruteforce(
    context: FormalContext,
    *,
    maximum_object_count: int = 20,
) -> tuple[frozenset[str], ...]:
    """Independent small-context oracle used only for validation.

    Every closed intent is the intersection of the attribute sets of an object
    subset (including the empty subset, whose shared set is all attributes).
    Enumerating object subsets is independent from Next Closure and is much
    cheaper for the POC contexts, which have fewer occurrences than attributes.
    """

    if len(context.objects) > maximum_object_count:
        raise FormalContextError(
            f"brute-force oracle is limited to {maximum_object_count} objects"
        )
    closed: set[frozenset[str]] = set()
    objects = context.objects
    for size in range(len(objects) + 1):
        for subset in combinations(objects, size):
            closed.add(context.object_prime(subset))
    return tuple(sorted(closed, key=lambda item: (len(item), tuple(sorted(item)))))


def enumerate_concepts(context: FormalContext) -> tuple[FormalConcept, ...]:
    return tuple(
        FormalConcept.from_intent(context, intent)
        for intent in enumerate_closed_intents_next_closure(context)
    )


def validate_next_closure_against_bruteforce(context: FormalContext) -> dict[str, Any]:
    next_closure = enumerate_closed_intents_next_closure(context)
    brute_force = enumerate_closed_intents_bruteforce(context)
    next_set = {frozenset(item) for item in next_closure}
    brute_set = {frozenset(item) for item in brute_force}
    missing = brute_set - next_set
    unexpected = next_set - brute_set
    return {
        "next_closure_count": len(next_closure),
        "bruteforce_count": len(brute_force),
        "equal": not missing and not unexpected,
        "missing": [sorted(item) for item in sorted(missing, key=lambda x: (len(x), sorted(x)))],
        "unexpected": [
            sorted(item) for item in sorted(unexpected, key=lambda x: (len(x), sorted(x)))
        ],
    }


def object_concept_classes(
    context: FormalContext,
    concepts: Iterable[FormalConcept] | None = None,
) -> dict[str, str]:
    """Map each object to a stable ID for its object-generated concept extent."""

    del concepts  # The mapping is computed directly from the closure contract.
    result: dict[str, str] = {}
    for object_id in context.objects:
        intent = context.closure(context.incidence[object_id])
        extent = tuple(sorted(context.attribute_prime(intent)))
        result[object_id] = f"oc_{sha256_json({'extent': extent})[:12]}"
    return result


def concepts_to_dict(
    context: FormalContext,
    concepts: Iterable[FormalConcept],
    *,
    validation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    concept_list = tuple(concepts)
    payload: dict[str, Any] = {
        "schema_version": "solve-vein/formal-concepts/v1",
        "context_id": context.context_id,
        "context_sha256": context.canonical_sha256,
        "concept_count": len(concept_list),
        "concepts": [concept.to_dict() for concept in concept_list],
    }
    if validation is not None:
        payload["small_context_oracle"] = dict(validation)
    payload["concept_set_sha256"] = sha256_json(payload["concepts"])
    return payload
