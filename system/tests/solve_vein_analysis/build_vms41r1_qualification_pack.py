"""Build and verify the frozen POC-VMS-41R1 qualification pack.

The pack is a zero-model preexecution artifact.  It contains public case
sources, hidden V2 acceptable sets, hidden reference candidates used only for
mechanical self-checks, thresholds and a manifest.  The builder reads one
real Solver export once, copies the selected excerpt into the fixture pack,
and then the generated pack is self-contained.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from typing import Any, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.event_extraction_projection import (
    EventExtractionAcceptableSetPackV2,
    evaluate_candidate_json_v2,
)
from system.solve_vein_analysis.models import canonical_json_bytes
from system.tests.solve_vein_analysis.historical_binding import (
    HistoricalBindingError,
    validate_current_or_historical_binding,
)


PACK_ID = "vms41r1-event-extractor-v2-qualification-20260814"
MANIFEST_SCHEMA = "solve-vein/vms41r1-qualification-pack-manifest/v1"
REFERENCE_CANDIDATES_SCHEMA = "solve-vein/vms41r1-reference-candidates/v1"
NEGATIVE_CHECKS_SCHEMA = "solve-vein/vms41r1-negative-checks/v1"
THRESHOLDS_SCHEMA = "solve-vein/vms41r1-qualification-thresholds/v1"
SUMMARY_SCHEMA = "solve-vein/vms41r1-qualification-pack-summary/v1"
FIXTURE_ROOT = (
    REPO_ROOT
    / "system"
    / "tests"
    / "solve_vein_analysis"
    / "qualification_fixtures"
    / "vms41r1"
)
PROTOCOL_PATH = (
    REPO_ROOT
    / "docs/history/sixth-generation/rnd"
    / "372-v0-2026-08-14-POC-VMS-41R1-未见资格包冻结协议-案例阈值与盲审流程.md"
)
PARENT_PROTOCOL_PATH = (
    REPO_ROOT
    / "docs/history/sixth-generation/rnd"
    / "371-v0-2026-08-14-POC-VMS-41R1-Event-Extractor-V2修订资格化协议.md"
)
PARENT_PROTOCOL_IDENTITY = (
    "第六代系统研发过程文档/"
    "371-v0-2026-08-14-POC-VMS-41R1-Event-Extractor-V2修订资格化协议.md"
)
PROTOCOL_IDENTITY = (
    "第六代系统研发过程文档/"
    "372-v0-2026-08-14-POC-VMS-41R1-未见资格包冻结协议-案例阈值与盲审流程.md"
)
FROZEN_PROTOCOL_BINDINGS = (
    (
        PARENT_PROTOCOL_IDENTITY,
        PARENT_PROTOCOL_PATH,
        "1170e8afcaf9351d082ecc5e1564ca0c1d09067a4e81d199e4f6e49a69a2d36f",
        13513,
    ),
    (
        PROTOCOL_IDENTITY,
        PROTOCOL_PATH,
        "e27428fe85f55acb49dbddb50316600e67c54868326749381c764ebfce15bafe",
        6688,
    ),
)
REAL_SOURCE_ID = "p48cc0b3636be4b9990a9"
REAL_SOURCE_EXPORT = (
    Path("/data/math-agent-glm5.2-tmux-agents-trajectory")
    / REAL_SOURCE_ID
    / "exports"
    / "conversation.json"
)
OLD_VMS41_SOURCE_IDS = {"p28a94bb9038347f8b5fc", "pf3a7fa50dcf54bafbe7a"}
PARAGRAPH_SPLIT_RE = re.compile(r"\n[ \t]*\n")
CASE_ORDER = (
    "V41R1-SYN-EXTRA-PATH",
    "V41R1-SYN-TEMPORAL-CORRECTION",
    "V41R1-SYN-TRUE-MERGE",
    "V41R1-SYN-REUSE-NOT-MERGE",
    "V41R1-SYN-FALSE-MERGE-GUARD",
    "V41R1-REAL-GF2-PAGODA",
)
ATTEMPT_IDS = {
    "V41R1-SYN-EXTRA-PATH": "poc-vms-41r1-syn-extra-path-a1",
    "V41R1-SYN-TEMPORAL-CORRECTION": "poc-vms-41r1-syn-temporal-correction-a1",
    "V41R1-SYN-TRUE-MERGE": "poc-vms-41r1-syn-true-merge-a1",
    "V41R1-SYN-REUSE-NOT-MERGE": "poc-vms-41r1-syn-reuse-not-merge-a1",
    "V41R1-SYN-FALSE-MERGE-GUARD": "poc-vms-41r1-syn-false-merge-guard-a1",
    "V41R1-REAL-GF2-PAGODA": "poc-vms-41r1-real-gf2-pagoda-a1",
}
EXPECTED_NONCLAIMS = (
    "DOES_NOT_AUTHORIZE_LIVE_EXECUTION",
    "DOES_NOT_QUALIFY_EVENT_EXTRACTOR_PROFILE",
    "DOES_NOT_TEST_STREAMING_EQUIVALENCE",
    "DOES_NOT_TEST_TELL_SELECTION_OR_CAUSAL_EFFECT",
    "DOES_NOT_TOUCH_ABSORB_SIDE_CODE_OR_ASSETS",
)


class VMS41R1PackError(RuntimeError):
    """Fail-closed qualification-pack construction or validation error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def frozen_protocol_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for identity, current_path, expected_sha256, expected_size in FROZEN_PROTOCOL_BINDINGS:
        try:
            validate_current_or_historical_binding(
                REPO_ROOT,
                identity,
                expected_sha256,
                expected_size=expected_size,
                current_path=current_path.relative_to(REPO_ROOT).as_posix(),
            )
        except HistoricalBindingError as exc:
            code = (
                "PROTOCOL_FILE_UNSAFE"
                if exc.code.startswith("CURRENT_PATH_") or exc.code == "PATH_INVALID"
                else "PROTOCOL_HASH_MISMATCH"
            )
            raise VMS41R1PackError(code, f"{identity}: {exc.code}") from exc
        rows.append({"path": identity, "sha256": expected_sha256})
    return rows


def canonical_bytes(value: Any) -> bytes:
    return canonical_json_bytes(value)


def source_ref(case_id: str) -> str:
    return f"fixture://vms41r1/{case_id}/raw_solver_trajectory.txt"


def source_identity(case_id: str, source: str) -> dict[str, str]:
    return {
        "carrier": "fixture",
        "source_artifact_ref": source_ref(case_id),
        "source_artifact_sha256": sha256_bytes(source.encode("utf-8")),
    }


def span(source: str, witness: str) -> dict[str, int]:
    start = source.find(witness)
    if start < 0:
        raise VMS41R1PackError("WITNESS_MISSING", witness)
    if source.find(witness, start + 1) >= 0:
        raise VMS41R1PackError("WITNESS_NOT_UNIQUE", witness)
    byte_start = len(source[:start].encode("utf-8"))
    return {"start": byte_start, "end": byte_start + len(witness.encode("utf-8"))}


def pattern(
    pattern_id: str,
    relations: Sequence[str],
    *,
    minimum: int = 1,
    maximum: int = 1,
    max_hops: int | None = None,
) -> dict[str, Any]:
    return {
        "pattern_id": pattern_id,
        "atoms": [
            {
                "allowed_relations": list(relations),
                "min_repeat": minimum,
                "max_repeat": maximum,
            }
        ],
        "max_hops": max_hops if max_hops is not None else maximum,
    }


def anchor(
    anchor_id: str,
    witness: str,
    kinds: Sequence[str],
    statuses: Sequence[str],
    resolutions: Sequence[str],
) -> dict[str, Any]:
    return {
        "anchor_id": anchor_id,
        "unique_witness_text": witness,
        "allowed_event_kinds": list(kinds),
        "allowed_status_at_occurrence": list(statuses),
        "allowed_later_resolutions": list(resolutions),
    }


def typed_clause(
    clause_id: str,
    source_anchor_id: str,
    target_anchor_id: str,
    relations: Sequence[str],
    *,
    required: bool = True,
    maximum: int = 1,
    max_hops: int | None = None,
) -> dict[str, Any]:
    return {
        "clause_id": clause_id,
        "source_anchor_id": source_anchor_id,
        "target_anchor_id": target_anchor_id,
        "required": required,
        "patterns": [
            pattern(
                f"PAT-{clause_id}",
                relations,
                maximum=maximum,
                max_hops=max_hops if max_hops is not None else maximum,
            )
        ],
    }


def event(
    *,
    source: str,
    event_id: str,
    index: int,
    kind: str,
    witness: str,
    state: str,
    status: str,
    resolution: str,
    incoming: Sequence[tuple[str, str, str]],
    contributions: Sequence[tuple[str, str, str, str]] = (),
) -> dict[str, Any]:
    return {
        "event_id": event_id,
        "sequence_index": index,
        "event_kind": kind,
        "text": witness,
        "canonical_math_state_id": state,
        "attributes": ["vms41r1:qualification"],
        "status_at_occurrence": status,
        "later_resolution": resolution,
        "source_span": span(source, witness),
        "incoming_edges": [
            {
                "source_event_id": parent_id,
                "relation": relation,
                "evidence": f"{relation} from {parent_id} to {event_id}",
                "evidence_span": span(source, evidence_witness),
            }
            for parent_id, relation, evidence_witness in incoming
        ],
        "merge_contributions": [
            {
                "parent_event_id": parent_id,
                "contribution_role": role,
                "contribution_claim": claim,
                "evidence_span": span(source, evidence_witness),
                "use_in_target": use,
            }
            for parent_id, role, evidence_witness, claim, use in contributions
        ],
    }


def candidate(case_id: str, source: str, events: Sequence[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": "solve-vein/reasoning-trajectory-candidate/v2",
        "trajectory_id": f"trajectory-{case_id.lower()}",
        "problem_id": f"problem-{case_id.lower()}",
        "source": source_identity(case_id, source),
        "events": list(events),
    }


def acceptable(
    *,
    case_id: str,
    source: str,
    anchors: Sequence[dict[str, Any]],
    typed_paths: Sequence[dict[str, Any]],
    forbidden_paths: Sequence[dict[str, Any]] = (),
    forbidden_relations: Sequence[str] = (),
    merge_constraints: Sequence[dict[str, Any]] = (),
    maximum_extra_events: int = 2,
) -> dict[str, Any]:
    return {
        "schema_version": "solve-vein/event-extraction-acceptable-set/v2",
        "acceptable_set_id": f"acceptable-{case_id.lower()}",
        "case_id": case_id,
        "problem_id": f"problem-{case_id.lower()}",
        "trajectory_id": f"trajectory-{case_id.lower()}",
        "source": source_identity(case_id, source),
        "anchors": list(anchors),
        "typed_path_clauses": list(typed_paths),
        "forbidden_path_clauses": list(forbidden_paths),
        "forbidden_relations": list(forbidden_relations),
        "merge_constraints": list(merge_constraints),
        "extra_event_policy": {
            "allow_unanchored_events": True,
            "maximum_extra_events": maximum_extra_events,
            "require_unique_semantic_signature": True,
            "require_nondecreasing_source_start": True,
        },
    }


def merge_constraint(
    constraint_id: str,
    target_anchor_id: str,
    origin_anchor_ids: Sequence[str],
    *,
    require_pairwise_incomparable: bool = True,
) -> dict[str, Any]:
    return {
        "constraint_id": constraint_id,
        "target_anchor_id": target_anchor_id,
        "required_origin_anchor_ids": list(origin_anchor_ids),
        "minimum_distinct_contributions": len(origin_anchor_ids),
        "contribution_path_patterns": [
            pattern(
                f"PAT-{constraint_id}-CONTRIB",
                ["CONTINUE", "REFINE", "REVISIT", "REUSE", "DEPENDS_ON"],
                maximum=3,
                max_hops=3,
            )
        ],
        "require_pairwise_incomparable": require_pairwise_incomparable,
    }


def public_problem(case_id: str, title: str) -> str:
    return (
        f"# {case_id}\n\n"
        f"{title}\n\n"
        "This is a solve-side reasoning-trajectory extraction qualification case. "
        "Extract the occurrence DAG from the raw solver trajectory. Do not solve "
        "the mathematical problem and do not infer hidden acceptable anchors.\n"
    )


def build_synthetic_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []

    source = (
        "ROOT: Begin with invariant I.\n"
        "EXTRA: Normalize notation into local coordinates.\n"
        "LOCAL: Apply the local-coordinate lemma.\n"
        "GLOBAL: Translate the lemma back to invariant I.\n"
        "END: Conclude the target statement.\n"
    )
    cid = "V41R1-SYN-EXTRA-PATH"
    cases.append(
        {
            "case_id": cid,
            "source_type": "synthetic",
            "case_role": "positive",
            "evidence_lineage_group_id": "vms41r1-synthetic-extra-path",
            "coverage_tags": ["legal_extra_event", "typed_path_quotient"],
            "problem": public_problem(cid, "Synthetic extra occurrence between anchors."),
            "source": source,
            "acceptable": acceptable(
                case_id=cid,
                source=source,
                anchors=[
                    anchor("A-ROOT", "ROOT: Begin with invariant I.", ["STATE"], ["ACTIVE"], ["STILL_ACTIVE"]),
                    anchor("A-LOCAL", "LOCAL: Apply the local-coordinate lemma.", ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-GLOBAL", "GLOBAL: Translate the lemma back to invariant I.", ["RETURN"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-END", "END: Conclude the target statement.", ["CONCLUSION"], ["SOLVED"], ["SOLVED"]),
                ],
                typed_paths=[
                    typed_clause("P-ROOT-LOCAL", "A-ROOT", "A-LOCAL", ["CONTINUE", "REFINE"], maximum=2, max_hops=2),
                    typed_clause("P-LOCAL-GLOBAL", "A-LOCAL", "A-GLOBAL", ["REFINE"]),
                    typed_clause("P-GLOBAL-END", "A-GLOBAL", "A-END", ["CONCLUDE"]),
                ],
            ),
            "reference_candidate": candidate(
                cid,
                source,
                [
                    event(source=source, event_id="E-ROOT", index=0, kind="STATE", witness="ROOT: Begin with invariant I.", state="root", status="ACTIVE", resolution="STILL_ACTIVE", incoming=[]),
                    event(source=source, event_id="E-EXTRA", index=1, kind="STATE", witness="EXTRA: Normalize notation into local coordinates.", state="normalization", status="ACTIVE", resolution="STILL_ACTIVE", incoming=[("E-ROOT", "CONTINUE", "EXTRA: Normalize notation into local coordinates.")]),
                    event(source=source, event_id="E-LOCAL", index=2, kind="DECISION", witness="LOCAL: Apply the local-coordinate lemma.", state="local-lemma", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-EXTRA", "REFINE", "LOCAL: Apply the local-coordinate lemma.")]),
                    event(source=source, event_id="E-GLOBAL", index=3, kind="RETURN", witness="GLOBAL: Translate the lemma back to invariant I.", state="global-return", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-LOCAL", "REFINE", "GLOBAL: Translate the lemma back to invariant I.")]),
                    event(source=source, event_id="E-END", index=4, kind="CONCLUSION", witness="END: Conclude the target statement.", state="done", status="SOLVED", resolution="SOLVED", incoming=[("E-GLOBAL", "CONCLUDE", "END: Conclude the target statement.")]),
                ],
            ),
        }
    )

    source = (
        "START: Try a parity invariant.\n"
        "GUESS: The parity invariant should be enough.\n"
        "COUNTER: A small configuration contradicts the parity-only claim.\n"
        "REPAIR: Replace it with a signed invariant.\n"
        "END: Finish using the repaired invariant.\n"
    )
    cid = "V41R1-SYN-TEMPORAL-CORRECTION"
    cases.append(
        {
            "case_id": cid,
            "source_type": "synthetic",
            "case_role": "positive_boundary",
            "evidence_lineage_group_id": "vms41r1-synthetic-temporal-correction",
            "coverage_tags": ["temporal_status", "later_resolution"],
            "problem": public_problem(cid, "Synthetic temporal correction case."),
            "source": source,
            "acceptable": acceptable(
                case_id=cid,
                source=source,
                anchors=[
                    anchor("A-START", "START: Try a parity invariant.", ["STATE"], ["ACTIVE"], ["STILL_ACTIVE"]),
                    anchor("A-GUESS", "GUESS: The parity invariant should be enough.", ["DECISION"], ["TENTATIVE"], ["CONTRADICTED"]),
                    anchor("A-COUNTER", "COUNTER: A small configuration contradicts the parity-only claim.", ["FAILURE"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-REPAIR", "REPAIR: Replace it with a signed invariant.", ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-END", "END: Finish using the repaired invariant.", ["CONCLUSION"], ["SOLVED"], ["SOLVED"]),
                ],
                typed_paths=[
                    typed_clause("P-START-GUESS", "A-START", "A-GUESS", ["REFINE"]),
                    typed_clause("P-GUESS-COUNTER", "A-GUESS", "A-COUNTER", ["CONTRADICT"]),
                    typed_clause("P-COUNTER-REPAIR", "A-COUNTER", "A-REPAIR", ["REFINE", "REVISIT"], maximum=2, max_hops=2),
                    typed_clause("P-REPAIR-END", "A-REPAIR", "A-END", ["CONCLUDE"]),
                ],
            ),
            "reference_candidate": candidate(
                cid,
                source,
                [
                    event(source=source, event_id="E-START", index=0, kind="STATE", witness="START: Try a parity invariant.", state="parity-start", status="ACTIVE", resolution="STILL_ACTIVE", incoming=[]),
                    event(source=source, event_id="E-GUESS", index=1, kind="DECISION", witness="GUESS: The parity invariant should be enough.", state="parity-guess", status="TENTATIVE", resolution="CONTRADICTED", incoming=[("E-START", "REFINE", "GUESS: The parity invariant should be enough.")]),
                    event(source=source, event_id="E-COUNTER", index=2, kind="FAILURE", witness="COUNTER: A small configuration contradicts the parity-only claim.", state="counterexample", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-GUESS", "CONTRADICT", "COUNTER: A small configuration contradicts the parity-only claim.")]),
                    event(source=source, event_id="E-REPAIR", index=3, kind="DECISION", witness="REPAIR: Replace it with a signed invariant.", state="signed-invariant", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-COUNTER", "REFINE", "REPAIR: Replace it with a signed invariant.")]),
                    event(source=source, event_id="E-END", index=4, kind="CONCLUSION", witness="END: Finish using the repaired invariant.", state="done", status="SOLVED", resolution="SOLVED", incoming=[("E-REPAIR", "CONCLUDE", "END: Finish using the repaired invariant.")]),
                ],
            ),
        }
    )

    source = (
        "ROOT: Set up the target.\n"
        "LEFT: Derive the modular obstruction.\n"
        "RIGHT: Construct the extremal witness.\n"
        "MERGE: Combine the obstruction and witness.\n"
        "END: Obtain the theorem.\n"
    )
    cid = "V41R1-SYN-TRUE-MERGE"
    cases.append(
        {
            "case_id": cid,
            "source_type": "synthetic",
            "case_role": "positive",
            "evidence_lineage_group_id": "vms41r1-synthetic-true-merge",
            "coverage_tags": ["true_merge", "injective_frontier"],
            "problem": public_problem(cid, "Synthetic independent-frontier merge case."),
            "source": source,
            "acceptable": acceptable(
                case_id=cid,
                source=source,
                anchors=[
                    anchor("A-ROOT", "ROOT: Set up the target.", ["STATE"], ["ACTIVE"], ["STILL_ACTIVE"]),
                    anchor("A-LEFT", "LEFT: Derive the modular obstruction.", ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-RIGHT", "RIGHT: Construct the extremal witness.", ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-MERGE", "MERGE: Combine the obstruction and witness.", ["SYNTHESIS"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-END", "END: Obtain the theorem.", ["CONCLUSION"], ["SOLVED"], ["SOLVED"]),
                ],
                typed_paths=[
                    typed_clause("P-ROOT-LEFT", "A-ROOT", "A-LEFT", ["REFINE"]),
                    typed_clause("P-ROOT-RIGHT", "A-ROOT", "A-RIGHT", ["BRANCH_FROM"]),
                    typed_clause("P-LEFT-MERGE", "A-LEFT", "A-MERGE", ["MERGE"]),
                    typed_clause("P-RIGHT-MERGE", "A-RIGHT", "A-MERGE", ["MERGE"]),
                    typed_clause("P-MERGE-END", "A-MERGE", "A-END", ["CONCLUDE"]),
                ],
                merge_constraints=[
                    merge_constraint("M-TRUE-FRONTIER", "A-MERGE", ["A-LEFT", "A-RIGHT"])
                ],
            ),
            "reference_candidate": candidate(
                cid,
                source,
                [
                    event(source=source, event_id="E-ROOT", index=0, kind="STATE", witness="ROOT: Set up the target.", state="root", status="ACTIVE", resolution="STILL_ACTIVE", incoming=[]),
                    event(source=source, event_id="E-LEFT", index=1, kind="DECISION", witness="LEFT: Derive the modular obstruction.", state="left", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-ROOT", "REFINE", "LEFT: Derive the modular obstruction.")]),
                    event(source=source, event_id="E-RIGHT", index=2, kind="DECISION", witness="RIGHT: Construct the extremal witness.", state="right", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-ROOT", "BRANCH_FROM", "RIGHT: Construct the extremal witness.")]),
                    event(source=source, event_id="E-MERGE", index=3, kind="SYNTHESIS", witness="MERGE: Combine the obstruction and witness.", state="merge", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-LEFT", "MERGE", "MERGE: Combine the obstruction and witness."), ("E-RIGHT", "MERGE", "MERGE: Combine the obstruction and witness.")], contributions=[("E-LEFT", "LEMMA", "LEFT: Derive the modular obstruction.", "modular obstruction", "use obstruction to rule out forbidden cases"), ("E-RIGHT", "CONSTRUCTION", "RIGHT: Construct the extremal witness.", "extremal witness", "use witness to show sharpness")]),
                    event(source=source, event_id="E-END", index=4, kind="CONCLUSION", witness="END: Obtain the theorem.", state="done", status="SOLVED", resolution="SOLVED", incoming=[("E-MERGE", "CONCLUDE", "END: Obtain the theorem.")]),
                ],
            ),
        }
    )

    source = (
        "ROOT: State the recurrence.\n"
        "LEMMA: Prove the recurrence is monotone.\n"
        "REUSE: Apply the monotone lemma in the boundary case.\n"
        "END: Close the boundary argument.\n"
    )
    cid = "V41R1-SYN-REUSE-NOT-MERGE"
    cases.append(
        {
            "case_id": cid,
            "source_type": "synthetic",
            "case_role": "negative_boundary",
            "evidence_lineage_group_id": "vms41r1-synthetic-reuse-not-merge",
            "coverage_tags": ["reuse_not_merge", "forbidden_merge"],
            "problem": public_problem(cid, "Synthetic reuse without merge case."),
            "source": source,
            "acceptable": acceptable(
                case_id=cid,
                source=source,
                anchors=[
                    anchor("A-ROOT", "ROOT: State the recurrence.", ["STATE"], ["ACTIVE"], ["STILL_ACTIVE"]),
                    anchor("A-LEMMA", "LEMMA: Prove the recurrence is monotone.", ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-REUSE", "REUSE: Apply the monotone lemma in the boundary case.", ["RETURN"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-END", "END: Close the boundary argument.", ["CONCLUSION"], ["SOLVED"], ["SOLVED"]),
                ],
                typed_paths=[
                    typed_clause("P-ROOT-LEMMA", "A-ROOT", "A-LEMMA", ["REFINE"]),
                    typed_clause("P-LEMMA-REUSE", "A-LEMMA", "A-REUSE", ["REUSE"]),
                    typed_clause("P-REUSE-END", "A-REUSE", "A-END", ["CONCLUDE"]),
                ],
                forbidden_relations=["MERGE"],
            ),
            "reference_candidate": candidate(
                cid,
                source,
                [
                    event(source=source, event_id="E-ROOT", index=0, kind="STATE", witness="ROOT: State the recurrence.", state="root", status="ACTIVE", resolution="STILL_ACTIVE", incoming=[]),
                    event(source=source, event_id="E-LEMMA", index=1, kind="DECISION", witness="LEMMA: Prove the recurrence is monotone.", state="lemma", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-ROOT", "REFINE", "LEMMA: Prove the recurrence is monotone.")]),
                    event(source=source, event_id="E-REUSE", index=2, kind="RETURN", witness="REUSE: Apply the monotone lemma in the boundary case.", state="reuse", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-LEMMA", "REUSE", "REUSE: Apply the monotone lemma in the boundary case.")]),
                    event(source=source, event_id="E-END", index=3, kind="CONCLUSION", witness="END: Close the boundary argument.", state="done", status="SOLVED", resolution="SOLVED", incoming=[("E-REUSE", "CONCLUDE", "END: Close the boundary argument.")]),
                ],
            ),
        }
    )

    source = (
        "ROOT: Start the same estimate.\n"
        "LEMMA: Prove the estimate for the first interval.\n"
        "RESTATED: Restate the same estimate for the next line.\n"
        "USE: Use the estimate once.\n"
        "END: Finish without independent synthesis.\n"
    )
    cid = "V41R1-SYN-FALSE-MERGE-GUARD"
    cases.append(
        {
            "case_id": cid,
            "source_type": "synthetic",
            "case_role": "negative_boundary",
            "evidence_lineage_group_id": "vms41r1-synthetic-false-merge-guard",
            "coverage_tags": ["false_merge", "ancestor_chain_guard"],
            "problem": public_problem(cid, "Synthetic false merge guard case."),
            "source": source,
            "acceptable": acceptable(
                case_id=cid,
                source=source,
                anchors=[
                    anchor("A-ROOT", "ROOT: Start the same estimate.", ["STATE"], ["ACTIVE"], ["STILL_ACTIVE"]),
                    anchor("A-LEMMA", "LEMMA: Prove the estimate for the first interval.", ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-RESTATED", "RESTATED: Restate the same estimate for the next line.", ["RETURN"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-USE", "USE: Use the estimate once.", ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                    anchor("A-END", "END: Finish without independent synthesis.", ["CONCLUSION"], ["SOLVED"], ["SOLVED"]),
                ],
                typed_paths=[
                    typed_clause("P-ROOT-LEMMA", "A-ROOT", "A-LEMMA", ["REFINE"]),
                    typed_clause("P-LEMMA-RESTATED", "A-LEMMA", "A-RESTATED", ["REUSE"]),
                    typed_clause("P-RESTATED-USE", "A-RESTATED", "A-USE", ["DEPENDS_ON"]),
                    typed_clause("P-USE-END", "A-USE", "A-END", ["CONCLUDE"]),
                ],
                forbidden_relations=["MERGE"],
            ),
            "reference_candidate": candidate(
                cid,
                source,
                [
                    event(source=source, event_id="E-ROOT", index=0, kind="STATE", witness="ROOT: Start the same estimate.", state="root", status="ACTIVE", resolution="STILL_ACTIVE", incoming=[]),
                    event(source=source, event_id="E-LEMMA", index=1, kind="DECISION", witness="LEMMA: Prove the estimate for the first interval.", state="lemma", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-ROOT", "REFINE", "LEMMA: Prove the estimate for the first interval.")]),
                    event(source=source, event_id="E-RESTATED", index=2, kind="RETURN", witness="RESTATED: Restate the same estimate for the next line.", state="restated", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-LEMMA", "REUSE", "RESTATED: Restate the same estimate for the next line.")]),
                    event(source=source, event_id="E-USE", index=3, kind="DECISION", witness="USE: Use the estimate once.", state="use", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-RESTATED", "DEPENDS_ON", "USE: Use the estimate once.")]),
                    event(source=source, event_id="E-END", index=4, kind="CONCLUSION", witness="END: Finish without independent synthesis.", state="done", status="SOLVED", resolution="SOLVED", incoming=[("E-USE", "CONCLUDE", "END: Finish without independent synthesis.")]),
                ],
            ),
        }
    )
    return cases


def extract_real_source() -> tuple[str, dict[str, Any]]:
    if REAL_SOURCE_ID in OLD_VMS41_SOURCE_IDS:
        raise VMS41R1PackError("REAL_SOURCE_REUSES_VMS41", REAL_SOURCE_ID)
    if REAL_SOURCE_EXPORT.is_symlink() or not REAL_SOURCE_EXPORT.is_file():
        raise VMS41R1PackError("REAL_SOURCE_EXPORT_MISSING", str(REAL_SOURCE_EXPORT))
    payload = REAL_SOURCE_EXPORT.read_bytes()
    try:
        document = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise VMS41R1PackError("REAL_SOURCE_JSON_INVALID", str(exc)) from exc
    reasoning_blocks = [
        step.get("reasoning_content")
        for step in document.get("steps", [])
        if isinstance(step, dict)
        and step.get("source") == "agent"
        and isinstance(step.get("reasoning_content"), str)
    ]
    if len(reasoning_blocks) != 1:
        raise VMS41R1PackError("REAL_SOURCE_REASONING_CARDINALITY", str(len(reasoning_blocks)))
    reasoning = reasoning_blocks[0]
    paragraphs = [part.strip() for part in PARAGRAPH_SPLIT_RE.split(reasoning) if part.strip()]
    selected_numbers = list(range(20, 33)) + list(range(45, 56)) + list(range(124, 136))
    if max(selected_numbers) > len(paragraphs):
        raise VMS41R1PackError("REAL_SOURCE_PARAGRAPH_RANGE_INVALID", str(len(paragraphs)))
    selected = "\n\n".join(paragraphs[index - 1] for index in selected_numbers) + "\n"
    receipt = {
        "schema_version": "solve-vein/vms41r1-real-source-receipt/v1",
        "source_id": REAL_SOURCE_ID,
        "source_conversation_path": str(REAL_SOURCE_EXPORT),
        "source_conversation_sha256": sha256_bytes(payload),
        "source_reasoning_sha256": sha256_bytes(reasoning.encode("utf-8")),
        "source_reasoning_paragraph_count": len(paragraphs),
        "selector": {
            "kind": "blank_line_paragraph_number_set",
            "paragraph_numbers_1_based": selected_numbers,
            "split_regex": PARAGRAPH_SPLIT_RE.pattern,
            "strip_each_paragraph": True,
            "joiner": "\\n\\n",
            "terminal_newline": True,
        },
        "selected_sha256": sha256_bytes(selected.encode("utf-8")),
        "excluded_vms41_source_ids": sorted(OLD_VMS41_SOURCE_IDS),
        "source_mutations": 0,
    }
    return selected, receipt


def build_real_case() -> dict[str, Any]:
    source, receipt = extract_real_source()
    cid = "V41R1-REAL-GF2-PAGODA"
    fib_fail = "So S is not invariant under left moves. Hmm."
    gf2 = "Actually, I recall now: the key insight for 1D peg solitaire is to work over GF(2)"
    pagoda = "So the Fibonacci sum S = Σ_{peg at k} F_k is non-increasing"
    foldback = "Actually, let me reconsider the GF(2) approach but more carefully, combined with reachability."
    dual = "Consider the dual: a vector w = (w_1,...,w_n) is in V^⊥"
    return {
        "case_id": cid,
        "source_type": "real_solver_raw",
        "case_role": "positive",
        "evidence_lineage_group_id": f"vms41r1-real-{REAL_SOURCE_ID}",
        "coverage_tags": ["real_solver_raw", "foldback_fusion", "true_merge"],
        "problem": public_problem(cid, "Real Solver GF(2) plus pagoda fold-back case."),
        "source": source,
        "source_receipt": receipt,
        "acceptable": acceptable(
            case_id=cid,
            source=source,
            anchors=[
                anchor("A-FIB-FAIL", fib_fail, ["FAILURE"], ["ESTABLISHED"], ["SOLVED"]),
                anchor("A-GF2", gf2, ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                anchor("A-PAGODA", pagoda, ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
                anchor("A-FOLD-BACK", foldback, ["SYNTHESIS"], ["TENTATIVE"], ["SOLVED"]),
                anchor("A-DUAL", dual, ["DECISION"], ["ESTABLISHED"], ["SOLVED"]),
            ],
            typed_paths=[
                typed_clause("P-FIB-GF2", "A-FIB-FAIL", "A-GF2", ["REVISIT", "BRANCH_FROM"], maximum=2, max_hops=2),
                typed_clause("P-FIB-PAGODA", "A-FIB-FAIL", "A-PAGODA", ["REVISIT", "REFINE"], maximum=2, max_hops=2),
                typed_clause("P-GF2-FOLD", "A-GF2", "A-FOLD-BACK", ["MERGE"]),
                typed_clause("P-PAGODA-FOLD", "A-PAGODA", "A-FOLD-BACK", ["MERGE"]),
                typed_clause("P-FOLD-DUAL", "A-FOLD-BACK", "A-DUAL", ["REFINE"]),
            ],
            merge_constraints=[
                merge_constraint("M-GF2-PAGODA-FOLD", "A-FOLD-BACK", ["A-GF2", "A-PAGODA"])
            ],
            maximum_extra_events=4,
        ),
        "reference_candidate": candidate(
            cid,
            source,
            [
                event(source=source, event_id="E-FIB-FAIL", index=0, kind="FAILURE", witness=fib_fail, state="fibonacci-left-fail", status="ESTABLISHED", resolution="SOLVED", incoming=[]),
                event(source=source, event_id="E-GF2", index=1, kind="DECISION", witness=gf2, state="gf2-reachability", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-FIB-FAIL", "REVISIT", gf2)]),
                event(source=source, event_id="E-PAGODA", index=2, kind="DECISION", witness=pagoda, state="pagoda-monotonicity", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-FIB-FAIL", "REFINE", pagoda)]),
                event(source=source, event_id="E-FOLD-BACK", index=3, kind="SYNTHESIS", witness=foldback, state="gf2-pagoda-fusion", status="TENTATIVE", resolution="SOLVED", incoming=[("E-GF2", "MERGE", foldback), ("E-PAGODA", "MERGE", foldback)], contributions=[("E-GF2", "REPRESENTATION", gf2, "GF(2) reachability space", "use linear span to describe possible endpoints"), ("E-PAGODA", "BOUND", pagoda, "pagoda monotonicity", "use monotonicity to filter algebraic endpoints")]),
                event(source=source, event_id="E-DUAL", index=4, kind="DECISION", witness=dual, state="dual-recurrence", status="ESTABLISHED", resolution="SOLVED", incoming=[("E-FOLD-BACK", "REFINE", dual)]),
            ],
        ),
    }


def build_cases() -> list[dict[str, Any]]:
    cases = build_synthetic_cases() + [build_real_case()]
    actual_order = tuple(case["case_id"] for case in cases)
    if actual_order != CASE_ORDER:
        raise VMS41R1PackError("CASE_ORDER_INVALID", repr(actual_order))
    return cases


def thresholds() -> dict[str, Any]:
    return {
        "schema_version": THRESHOLDS_SCHEMA,
        "pack_id": PACK_ID,
        "case_count": 6,
        "reference_candidate_count": 6,
        "future_profile_pass_thresholds": {
            "artifact_protocol_cases": "6/6",
            "anchor_coverage_cases": "6/6",
            "typed_path_cases": "6/6",
            "temporal_status_cases": "6/6",
            "merge_and_forbidden_cases": "all_relevant_cases_pass",
            "blind_manual_audit": "at_least_5_of_6_accept_and_no_high_severity_source_fidelity_failure",
            "file_effect": "no_confirmed_forbidden_effect",
        },
        "live_authorization": "NOT_AUTHORIZED_BY_THIS_FILE",
    }


def blind_review_rubric() -> str:
    return """# VMS-41R1 Blind Review Rubric

The reviewer sees only the public raw trajectory, a candidate occurrence DAG,
source spans and this rubric.  Do not request or inspect acceptable-sets.json,
reference-candidates.json, mechanical error summaries or aggregate results.

Judgment fields:

- source_fidelity: ACCEPT | REJECT | AMBIGUOUS
- occurrence_granularity: ACCEPT | REJECT | AMBIGUOUS
- temporal_status: ACCEPT | REJECT | AMBIGUOUS
- branch_and_merge_semantics: ACCEPT | REJECT | AMBIGUOUS
- high_severity_failure: true | false
- notes

A candidate may include source-backed extra occurrences.  Reject only when an
extra occurrence is duplicated, rhetorical-only, unsupported by the source or
used to fabricate a merge/frontier that did not occur.
"""


def negative_checks() -> dict[str, Any]:
    return {
        "schema_version": NEGATIVE_CHECKS_SCHEMA,
        "pack_id": PACK_ID,
        "checks": [
            {
                "check_id": "N01-temporal-hindsight",
                "case_id": "V41R1-SYN-TEMPORAL-CORRECTION",
                "mutation": {
                    "op": "replace",
                    "path": "/events/1/status_at_occurrence",
                    "value": "ESTABLISHED",
                },
                "expected_overall_status": "FAIL",
                "expected_axis": "temporal_status_verdict",
            },
            {
                "check_id": "N02-reuse-as-merge",
                "case_id": "V41R1-SYN-REUSE-NOT-MERGE",
                "mutation": {
                    "op": "replace",
                    "path": "/events/2/incoming_edges/0/relation",
                    "value": "MERGE",
                },
                "expected_overall_status": "INVALID",
                "expected_axis": "protocol_verdict",
            },
            {
                "check_id": "N03-real-foldback-missing-merge-parent",
                "case_id": "V41R1-REAL-GF2-PAGODA",
                "mutation": {
                    "op": "remove",
                    "path": "/events/3/merge_contributions/1",
                },
                "expected_overall_status": "INVALID",
                "expected_axis": "protocol_verdict",
            },
            {
                "check_id": "N04-source-span-drift",
                "case_id": "V41R1-SYN-EXTRA-PATH",
                "mutation": {
                    "op": "replace",
                    "path": "/events/2/source_span/start",
                    "value": 0,
                },
                "expected_overall_status": "INVALID",
                "expected_axis": "protocol_verdict",
            },
        ],
    }


def apply_pointer_mutation(value: Any, mutation: Mapping[str, Any]) -> Any:
    cloned = json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))
    if set(mutation) != {"op", "path", "value"} and set(mutation) != {"op", "path"}:
        raise VMS41R1PackError("NEGATIVE_MUTATION_KEYS_INVALID", repr(sorted(mutation)))
    op = mutation["op"]
    tokens = _parse_json_pointer(str(mutation["path"]))
    parent = cloned
    for token in tokens[:-1]:
        parent = _resolve_token(parent, token)
    final = tokens[-1]
    if isinstance(parent, list):
        index = _array_index(final, len(parent))
        if op == "replace":
            parent[index] = mutation["value"]
        elif op == "remove":
            parent.pop(index)
        else:
            raise VMS41R1PackError("NEGATIVE_MUTATION_OP_INVALID", repr(op))
    elif isinstance(parent, dict):
        if final not in parent:
            raise VMS41R1PackError("NEGATIVE_MUTATION_TARGET_MISSING", str(mutation["path"]))
        if op == "replace":
            parent[final] = mutation["value"]
        elif op == "remove":
            del parent[final]
        else:
            raise VMS41R1PackError("NEGATIVE_MUTATION_OP_INVALID", repr(op))
    else:
        raise VMS41R1PackError("NEGATIVE_MUTATION_PARENT_INVALID", str(mutation["path"]))
    return cloned


def _parse_json_pointer(pointer: str) -> list[str]:
    if not pointer.startswith("/") or pointer == "/":
        raise VMS41R1PackError("JSON_POINTER_INVALID", pointer)
    tokens = pointer[1:].split("/")
    if any(token in {"", ".", "..", "-"} for token in tokens):
        raise VMS41R1PackError("JSON_POINTER_INVALID", pointer)
    return [token.replace("~1", "/").replace("~0", "~") for token in tokens]


def _resolve_token(value: Any, token: str) -> Any:
    if isinstance(value, list):
        return value[_array_index(token, len(value))]
    if isinstance(value, dict) and token in value:
        return value[token]
    raise VMS41R1PackError("JSON_POINTER_TARGET_MISSING", token)


def _array_index(token: str, length: int) -> int:
    if not re.fullmatch(r"0|[1-9][0-9]*", token):
        raise VMS41R1PackError("JSON_POINTER_ARRAY_INDEX_INVALID", token)
    index = int(token)
    if index >= length:
        raise VMS41R1PackError("JSON_POINTER_ARRAY_INDEX_OUT_OF_RANGE", token)
    return index


def evaluate_reference_cases(
    acceptable_pack: Mapping[str, Any],
    reference_candidates: Mapping[str, Any],
    sources: Mapping[str, str],
    checks: Mapping[str, Any],
) -> dict[str, Any]:
    pack = EventExtractionAcceptableSetPackV2.from_dict(acceptable_pack)
    candidate_rows = []
    for case in pack.cases:
        candidate_value = reference_candidates["candidates"][case.case_id]
        candidate_text = json.dumps(
            candidate_value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        evaluation = evaluate_candidate_json_v2(
            candidate_text, case, sources[case.case_id].encode("utf-8")
        )
        candidate_rows.append(
            {
                "case_id": case.case_id,
                "candidate_sha256": sha256_bytes(candidate_text.encode("utf-8")),
                "overall_status": evaluation.overall_status.value,
                "mechanical_scientific_verdict": evaluation.mechanical_scientific_verdict.value,
                "evaluation_sha256": sha256_bytes(canonical_bytes(evaluation.to_dict())),
            }
        )
    negative_rows = []
    candidates = reference_candidates["candidates"]
    case_by_id = {case.case_id: case for case in pack.cases}
    for check in checks["checks"]:
        mutated = apply_pointer_mutation(
            candidates[check["case_id"]], check["mutation"]
        )
        candidate_text = json.dumps(
            mutated,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        evaluation = evaluate_candidate_json_v2(
            candidate_text,
            case_by_id[check["case_id"]],
            sources[check["case_id"]].encode("utf-8"),
        )
        axis = check["expected_axis"]
        row = {
            "check_id": check["check_id"],
            "case_id": check["case_id"],
            "observed_overall_status": evaluation.overall_status.value,
            "observed_axis_verdict": evaluation.to_dict()[axis],
            "expected_overall_status": check["expected_overall_status"],
            "expected_axis": axis,
        }
        row["matched"] = (
            row["observed_overall_status"] == row["expected_overall_status"]
            and row["observed_axis_verdict"] != "PASS"
        )
        negative_rows.append(row)
    return {
        "schema_version": SUMMARY_SCHEMA,
        "pack_id": PACK_ID,
        "case_count": len(candidate_rows),
        "reference_candidate_count": len(candidate_rows),
        "reference_candidate_rows": candidate_rows,
        "negative_check_rows": negative_rows,
        "verdict": (
            "PASS"
            if all(row["overall_status"] == "PENDING_BLIND_MANUAL_AUDIT" for row in candidate_rows)
            and all(row["mechanical_scientific_verdict"] == "PASS" for row in candidate_rows)
            and all(row["matched"] for row in negative_rows)
            else "FAIL"
        ),
        "model_calls": 0,
        "database_calls": 0,
        "solver_calls": 0,
    }


def build_pack_objects() -> dict[str, Any]:
    cases = build_cases()
    sources = {case["case_id"]: case["source"] for case in cases}
    acceptable_pack = {
        "schema_version": "solve-vein/event-extraction-acceptable-set-pack/v2",
        "pack_id": PACK_ID,
        "cases": [case["acceptable"] for case in cases],
    }
    reference_candidates = {
        "schema_version": REFERENCE_CANDIDATES_SCHEMA,
        "pack_id": PACK_ID,
        "evidence_lane": "HIDDEN_SELF_CHECK_ONLY",
        "candidates": {
            case["case_id"]: case["reference_candidate"] for case in cases
        },
        "explicit_nonclaims": [
            "REFERENCE_CANDIDATES_ARE_NOT_MODEL_OUTPUTS",
            "REFERENCE_CANDIDATES_MUST_NOT_ENTER_CANDIDATE_PROMPTS",
        ],
    }
    checks = negative_checks()
    summary = evaluate_reference_cases(acceptable_pack, reference_candidates, sources, checks)
    if summary["verdict"] != "PASS":
        raise VMS41R1PackError("REFERENCE_SELF_CHECK_FAILED", repr(summary))
    return {
        "cases": cases,
        "sources": sources,
        "acceptable_pack": acceptable_pack,
        "reference_candidates": reference_candidates,
        "negative_checks": checks,
        "thresholds": thresholds(),
        "summary": summary,
    }


def write_pack(root: Path = FIXTURE_ROOT) -> dict[str, Any]:
    if root.exists() or root.is_symlink():
        raise VMS41R1PackError("DESTINATION_EXISTS", str(root))
    objects = build_pack_objects()
    with tempfile.TemporaryDirectory(prefix=".vms41r1-build-", dir=root.parent) as temporary:
        temp_root = Path(temporary) / root.name
        temp_root.mkdir(mode=0o700)
        _write_text(temp_root / "blind-review-rubric.md", blind_review_rubric())
        _write_json(temp_root / "acceptable-sets.json", objects["acceptable_pack"])
        _write_json(temp_root / "reference-candidates.json", objects["reference_candidates"])
        _write_json(temp_root / "negative-checks.json", objects["negative_checks"])
        _write_json(temp_root / "thresholds.json", objects["thresholds"])
        _write_json(temp_root / "reference-self-check-summary.json", objects["summary"])
        for case in objects["cases"]:
            case_root = temp_root / case["case_id"]
            case_root.mkdir(mode=0o700)
            _write_text(case_root / "problem.md", case["problem"])
            _write_text(case_root / "raw_solver_trajectory.txt", case["source"])
            receipt = case.get("source_receipt") or {
                "schema_version": "solve-vein/vms41r1-synthetic-source-receipt/v1",
                "case_id": case["case_id"],
                "source_type": case["source_type"],
                "source_mutations": 0,
                "source_sha256": sha256_bytes(case["source"].encode("utf-8")),
            }
            _write_json(case_root / "source-receipt.json", receipt)
            _write_json(
                case_root / "input-manifest.json",
                {
                    "schema_version": "solve-vein/vms41r1-public-case-input/v1",
                    "pack_id": PACK_ID,
                    "case_id": case["case_id"],
                    "public_files": [
                        "problem.md",
                        "raw_solver_trajectory.txt",
                        "input-manifest.json",
                    ],
                    "hidden_files_forbidden": [
                        "acceptable-sets.json",
                        "reference-candidates.json",
                        "negative-checks.json",
                    ],
                },
            )
        manifest = build_manifest(temp_root, objects)
        _write_json(temp_root / "pack-manifest.json", manifest)
        os.replace(temp_root, root)
    return load_vms41r1_qualification_pack(root)


def _write_json(path: Path, value: Any) -> None:
    _write_bytes(path, canonical_bytes(value))


def _write_text(path: Path, value: str) -> None:
    _write_bytes(path, value.encode("utf-8"))


def _write_bytes(path: Path, payload: bytes) -> None:
    if path.exists() or path.is_symlink():
        raise VMS41R1PackError("WRITE_DESTINATION_EXISTS", str(path))
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    path.write_bytes(payload)
    path.chmod(0o600)


def build_manifest(root: Path, objects: Mapping[str, Any]) -> dict[str, Any]:
    file_rows = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        visibility = "hidden"
        if relative.endswith("/problem.md") or relative.endswith("/raw_solver_trajectory.txt") or relative.endswith("/input-manifest.json"):
            visibility = "public"
        file_rows.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "visibility": visibility,
            }
        )
    case_specs = []
    for case in objects["cases"]:
        case_id = case["case_id"]
        case_specs.append(
            {
                "case_id": case_id,
                "source_type": case["source_type"],
                "case_role": case["case_role"],
                "evidence_lineage_group_id": case["evidence_lineage_group_id"],
                "coverage_tags": case["coverage_tags"],
                "attempt_id": ATTEMPT_IDS[case_id],
                "public_files": [
                    f"{case_id}/problem.md",
                    f"{case_id}/raw_solver_trajectory.txt",
                    f"{case_id}/input-manifest.json",
                ],
            }
        )
    return {
        "schema_version": MANIFEST_SCHEMA,
        "pack_id": PACK_ID,
        "evidence_lane": "QUALIFICATION_HOLDOUT_PREEXECUTION",
        "case_order": list(CASE_ORDER),
        "protocols": frozen_protocol_rows(),
        "files": file_rows,
        "case_specs": case_specs,
        "thresholds_path": "thresholds.json",
        "thresholds_sha256": sha256_file(root / "thresholds.json"),
        "reference_self_check_path": "reference-self-check-summary.json",
        "reference_self_check_sha256": sha256_file(root / "reference-self-check-summary.json"),
        "attempt_ids": ATTEMPT_IDS,
        "explicit_nonclaims": list(EXPECTED_NONCLAIMS),
        "model_calls_authorized": 0,
        "database_calls_authorized": 0,
        "solver_calls_authorized": 0,
    }


def load_vms41r1_qualification_pack(root: Path = FIXTURE_ROOT) -> dict[str, Any]:
    if root.is_symlink() or not root.is_dir():
        raise VMS41R1PackError("PACK_ROOT_UNSAFE", str(root))
    manifest = _load_json(root / "pack-manifest.json")
    _require_keys(
        manifest,
        {
            "schema_version",
            "pack_id",
            "evidence_lane",
            "case_order",
            "protocols",
            "files",
            "case_specs",
            "thresholds_path",
            "thresholds_sha256",
            "reference_self_check_path",
            "reference_self_check_sha256",
            "attempt_ids",
            "explicit_nonclaims",
            "model_calls_authorized",
            "database_calls_authorized",
            "solver_calls_authorized",
        },
        "manifest",
    )
    if manifest["schema_version"] != MANIFEST_SCHEMA:
        raise VMS41R1PackError("MANIFEST_SCHEMA_UNSUPPORTED", repr(manifest["schema_version"]))
    if manifest["pack_id"] != PACK_ID:
        raise VMS41R1PackError("MANIFEST_PACK_ID_INVALID", repr(manifest["pack_id"]))
    if tuple(manifest["case_order"]) != CASE_ORDER:
        raise VMS41R1PackError("MANIFEST_CASE_ORDER_INVALID", repr(manifest["case_order"]))
    if manifest["explicit_nonclaims"] != list(EXPECTED_NONCLAIMS):
        raise VMS41R1PackError("MANIFEST_NONCLAIMS_INVALID", repr(manifest["explicit_nonclaims"]))
    if manifest["model_calls_authorized"] != 0 or manifest["database_calls_authorized"] != 0 or manifest["solver_calls_authorized"] != 0:
        raise VMS41R1PackError("MANIFEST_SIDE_EFFECT_AUTH_INVALID", "nonzero side effect authorization")
    listed_paths = []
    for row in manifest["files"]:
        _require_keys(row, {"path", "bytes", "sha256", "visibility"}, "manifest.files[]")
        relative = _safe_relative(row["path"])
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise VMS41R1PackError("MANIFEST_MEMBER_UNSAFE", relative)
        payload = path.read_bytes()
        if len(payload) != row["bytes"]:
            raise VMS41R1PackError("MANIFEST_MEMBER_SIZE_MISMATCH", relative)
        if sha256_bytes(payload) != row["sha256"]:
            raise VMS41R1PackError("MANIFEST_MEMBER_HASH_MISMATCH", relative)
        if row["visibility"] not in {"public", "hidden"}:
            raise VMS41R1PackError("MANIFEST_VISIBILITY_INVALID", relative)
        listed_paths.append(relative)
    actual_paths = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and not path.is_symlink()
    )
    expected_paths = sorted([*listed_paths, "pack-manifest.json"])
    if actual_paths != expected_paths:
        raise VMS41R1PackError(
            "PACK_FILE_SET_INVALID",
            f"expected={expected_paths!r}, actual={actual_paths!r}",
        )
    if any(path.is_symlink() for path in root.rglob("*")):
        raise VMS41R1PackError("PACK_SYMLINK_MEMBER", str(root))
    protocols = manifest["protocols"]
    if not isinstance(protocols, list) or len(protocols) != len(FROZEN_PROTOCOL_BINDINGS):
        raise VMS41R1PackError("PROTOCOL_SET_MISMATCH", repr(protocols))
    for protocol, binding in zip(protocols, FROZEN_PROTOCOL_BINDINGS, strict=True):
        _require_keys(protocol, {"path", "sha256"}, "manifest.protocols[]")
        identity, current_path, expected_sha256, expected_size = binding
        if protocol["path"] != identity:
            raise VMS41R1PackError("PROTOCOL_PATH_MISMATCH", repr(protocol["path"]))
        if protocol["sha256"] != expected_sha256:
            raise VMS41R1PackError("PROTOCOL_HASH_MISMATCH", protocol["path"])
        try:
            validate_current_or_historical_binding(
                REPO_ROOT,
                identity,
                expected_sha256,
                expected_size=expected_size,
                current_path=current_path.relative_to(REPO_ROOT).as_posix(),
            )
        except HistoricalBindingError as exc:
            code = (
                "PROTOCOL_FILE_UNSAFE"
                if exc.code.startswith("CURRENT_PATH_") or exc.code == "PATH_INVALID"
                else "PROTOCOL_HASH_MISMATCH"
            )
            raise VMS41R1PackError(code, f"{identity}: {exc.code}") from exc
    acceptable_pack = _load_json(root / "acceptable-sets.json")
    reference_candidates = _load_json(root / "reference-candidates.json")
    checks = _load_json(root / "negative-checks.json")
    thresholds_value = _load_json(root / "thresholds.json")
    if thresholds_value["schema_version"] != THRESHOLDS_SCHEMA:
        raise VMS41R1PackError("THRESHOLDS_SCHEMA_INVALID", repr(thresholds_value.get("schema_version")))
    sources = {
        case_id: (root / case_id / "raw_solver_trajectory.txt").read_text()
        for case_id in CASE_ORDER
    }
    summary = evaluate_reference_cases(
        acceptable_pack, reference_candidates, sources, checks
    )
    stored_summary = _load_json(root / "reference-self-check-summary.json")
    if stored_summary != summary:
        raise VMS41R1PackError("REFERENCE_SELF_CHECK_REPLAY_MISMATCH", "summary drift")
    if summary["verdict"] != "PASS":
        raise VMS41R1PackError("REFERENCE_SELF_CHECK_NOT_PASS", repr(summary))
    return {
        "schema_version": "solve-vein/vms41r1-loaded-qualification-pack/v1",
        "pack_id": PACK_ID,
        "manifest_sha256": sha256_file(root / "pack-manifest.json"),
        "case_count": len(CASE_ORDER),
        "reference_candidate_count": len(reference_candidates["candidates"]),
        "negative_check_count": len(checks["checks"]),
        "summary": summary,
        "model_calls_authorized": 0,
        "database_calls_authorized": 0,
        "solver_calls_authorized": 0,
    }


def _load_json(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise VMS41R1PackError("JSON_FILE_UNSAFE", str(path))
    try:
        value = json.loads(path.read_text(), parse_constant=_reject_nonfinite)
    except json.JSONDecodeError as exc:
        raise VMS41R1PackError("JSON_INVALID", f"{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise VMS41R1PackError("JSON_ROOT_NOT_OBJECT", str(path))
    return value


def _reject_nonfinite(value: str) -> Any:
    raise VMS41R1PackError("JSON_NONFINITE", value)


def _require_keys(value: Mapping[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        raise VMS41R1PackError(
            "KEY_SET_INVALID",
            f"{label}: missing={sorted(expected - actual)}, unknown={sorted(actual - expected)}",
        )


def _safe_relative(value: Any) -> str:
    if not isinstance(value, str) or not value or value.startswith("/") or ".." in value.split("/"):
        raise VMS41R1PackError("RELATIVE_PATH_INVALID", repr(value))
    return value


def main() -> int:
    if FIXTURE_ROOT.exists():
        result = load_vms41r1_qualification_pack(FIXTURE_ROOT)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    result = write_pack(FIXTURE_ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except VMS41R1PackError as exc:
        print(f"VMS41R1_PACK_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
