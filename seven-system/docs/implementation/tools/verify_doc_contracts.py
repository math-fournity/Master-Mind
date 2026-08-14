#!/usr/bin/env python3
"""Fail-closed verifier for Seven's documentation work package (WP-DOC0)."""

from __future__ import annotations

import hashlib
import importlib.util
import importlib.metadata
import json
import copy
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import jsonschema


HERE = Path(__file__).resolve().parent
IMPL = HERE.parent
DOCS = IMPL.parent
SEVEN = DOCS.parent
WORKSPACE = SEVEN.parent
DAG_PATH = IMPL / "work-package-dag.v1.json"
BOARD_PATH = IMPL / "work-package-board.md"
DAG_DOC = IMPL / "03-work-package-dag.md"
INDEX_PATH = IMPL / "normative-requirement-index.v1.json"
PLAN_PATH = IMPL / "wp-doc0-plan.v1.json"
HASH_RE = re.compile(r"^[0-9a-f]{64}$")
CANONICAL_UTC_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,9})?Z$")
FORMAT_CHECKER = jsonschema.FormatChecker()
DOC0_VERIFICATION_IDS = (
    "DOC0-LINKS",
    "DOC0-DAG",
    "DOC0-NORMATIVE-INDEX",
    "DOC0-SCHEMA-META",
    "DOC0-SCHEMA-STRICT",
    "DOC0-SECURITY-NEGATIVE-VECTORS",
    "DOC0-RECEIPT-SELF-SCHEMA",
    "DOC0-OVERCLAIM",
    "DOC0-DIFF-CHECK",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json_sha256(value: object) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def ref_hash(path: Path, reference: str | None = None) -> dict[str, str]:
    return {"ref": reference or path.relative_to(IMPL).as_posix(), "sha256": sha256(path)}


def canonical_utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def parse_canonical_utc(value: object) -> datetime:
    text = str(value)
    if not CANONICAL_UTC_RE.fullmatch(text):
        raise ValueError(f"not canonical UTC RFC3339: {text}")
    parsed = datetime.fromisoformat(text[:-1] + "+00:00")
    if parsed.utcoffset() is None or parsed.utcoffset().total_seconds() != 0:
        raise ValueError(f"not UTC: {text}")
    return parsed


@FORMAT_CHECKER.checks("date-time", raises=(TypeError, ValueError))
def is_canonical_utc_rfc3339(value: object) -> bool:
    parse_canonical_utc(value)
    return True


def git_output(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=WORKSPACE,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()


def current_implementation_subject() -> dict[str, object]:
    commit = git_output("rev-parse", "HEAD")
    tree = git_output("rev-parse", "HEAD^{tree}")
    clean = not bool(git_output("status", "--porcelain", "--untracked-files=normal"))
    return {
        "commit": commit,
        "tree": tree,
        "working_tree_clean": clean,
        "source_relation": "COMMITTED_TREE" if clean else "WORKING_TREE_SNAPSHOT_OVER_BASELINE",
    }


def load_json(path: Path) -> object:
    return json.loads(path.read_text())


def validate_instance(instance_path: Path, schema_path: Path, errors: list[str]) -> None:
    try:
        instance = load_json(instance_path)
        schema = load_json(schema_path)
        findings = sorted(jsonschema.Draft202012Validator(schema, format_checker=FORMAT_CHECKER).iter_errors(instance), key=lambda item: list(item.path))
        errors.extend(f"schema:{instance_path.name}:{'/'.join(map(str, finding.path))}:{finding.message}" for finding in findings)
    except Exception as error:  # fail closed, including malformed Schema
        errors.append(f"schema:{instance_path.name}:{type(error).__name__}:{error}")


def schema_errors(schema_name: str, instance: object) -> list[jsonschema.ValidationError]:
    schema = load_json(IMPL / schema_name)
    return list(jsonschema.Draft202012Validator(schema, format_checker=FORMAT_CHECKER).iter_errors(instance))


def verify_all_schema_contracts(errors: list[str]) -> int:
    schema_paths = sorted(IMPL.glob("*.schema.json"))

    def walk(node: object, source: str, path: str) -> None:
        if isinstance(node, dict):
            if node.get("type") == "object" and node.get("additionalProperties") is not False:
                errors.append(f"schema-strict:{source}:{path}:object_without_additionalProperties_false")
            for key, value in node.items():
                walk(value, source, f"{path}/{key}")
        elif isinstance(node, list):
            for index, value in enumerate(node):
                walk(value, source, f"{path}/{index}")

    for path in schema_paths:
        try:
            schema = load_json(path)
            jsonschema.Draft202012Validator.check_schema(schema)
            walk(schema, path.name, "$")
        except Exception as error:
            errors.append(f"schema-meta:{path.name}:{type(error).__name__}:{error}")
    return len(schema_paths)


def edge_set(nodes: list[dict[str, object]], field: str, errors: list[str]) -> set[tuple[str, str]]:
    ids = [str(item["wp_id"]) for item in nodes]
    known = set(ids)
    if len(ids) != len(known):
        errors.append("dag:duplicate_wp_id")
    edges: set[tuple[str, str]] = set()
    for item in nodes:
        target = str(item["wp_id"])
        for source in item[field]:
            source = str(source)
            if source not in known:
                errors.append(f"dag:{field}:unknown_dependency:{target}:{source}")
            if source == target:
                errors.append(f"dag:{field}:self_dependency:{target}")
            edges.add((source, target))
    return edges


def assert_acyclic(ids: set[str], edges: set[tuple[str, str]], label: str, errors: list[str]) -> None:
    outgoing = {node: set() for node in ids}
    indegree = {node: 0 for node in ids}
    for source, target in edges:
        if source in ids and target in ids and target not in outgoing[source]:
            outgoing[source].add(target)
            indegree[target] += 1
    queue = sorted(node for node, degree in indegree.items() if degree == 0)
    visited: list[str] = []
    while queue:
        node = queue.pop(0)
        visited.append(node)
        for target in sorted(outgoing[node]):
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
                queue.sort()
    if len(visited) != len(ids):
        errors.append(f"dag:{label}:cycle:{sorted(ids - set(visited))}")


def parse_board(errors: list[str]) -> dict[str, tuple[set[str], set[str]]]:
    result: dict[str, tuple[set[str], set[str]]] = {}
    for line in BOARD_PATH.read_text().splitlines():
        if not line.startswith("| WP-"):
            continue
        cells = [cell.strip().replace("`", "") for cell in line.strip().strip("|").split("|")]
        if len(cells) != 5:
            errors.append(f"board:bad_column_count:{line}")
            continue
        wp_id, _, development, activation, _ = cells
        def deps(value: str) -> set[str]:
            if value == "无":
                return set()
            values = {part.strip() for part in value.split("、") if part.strip()}
            if any(not part.startswith("WP-") for part in values):
                errors.append(f"board:noncanonical_dependency:{wp_id}:{value}")
            return values
        if wp_id in result:
            errors.append(f"board:duplicate_wp:{wp_id}")
        result[wp_id] = (deps(development), deps(activation))
    return result


def parse_mermaid(errors: list[str]) -> set[tuple[str, str]]:
    text = DAG_DOC.read_text()
    try:
        block = text.split("```mermaid", 1)[1].split("```", 1)[0]
    except IndexError:
        errors.append("mermaid:missing_block")
        return set()
    aliases: dict[str, str] = {}
    for line in block.splitlines():
        for alias, wp_id in re.findall(r'\b([A-Za-z0-9_]+)\["(WP-[A-Z0-9-]+)(?:\s[^\"]*)?"\]', line):
            aliases[alias] = wp_id
    edges: set[tuple[str, str]] = set()
    for line in block.splitlines():
        match = re.search(r'^\s*([A-Za-z0-9_]+)(?:\[.*?\])?\s*-->\s*([A-Za-z0-9_]+)', line)
        if not match:
            continue
        source_alias, target_alias = match.groups()
        if source_alias not in aliases or target_alias not in aliases:
            errors.append(f"mermaid:unknown_alias:{source_alias}:{target_alias}")
            continue
        edges.add((aliases[source_alias], aliases[target_alias]))
    return edges


def verify_links_and_fences(errors: list[str]) -> tuple[int, int]:
    markdown_files = sorted((IMPL).glob("*.md")) + sorted((DOCS / "audit").glob("*.md")) + sorted((DOCS / "decisions").glob("*.md"))
    link_count = 0
    for path in markdown_files:
        text = path.read_text()
        if sum(1 for line in text.splitlines() if line.lstrip().startswith("```")) % 2:
            errors.append(f"markdown:unbalanced_fence:{path.relative_to(DOCS)}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            link_count += 1
            if not (path.parent / clean).resolve().exists():
                errors.append(f"markdown:broken_link:{path.relative_to(DOCS)}:{target}")
    return len(markdown_files), link_count


def verify_plan(dag_hash: str, index: dict[str, object], errors: list[str]) -> tuple[int, int, int]:
    validate_instance(PLAN_PATH, IMPL / "work-package-plan.v1.schema.json", errors)
    plan = load_json(PLAN_PATH)
    if plan["canonical_dag"]["sha256"] != dag_hash:
        errors.append("plan:canonical_dag_hash_mismatch")
    index_hash = sha256(INDEX_PATH)
    expected_index_ref = {"ref": INDEX_PATH.name, "sha256": index_hash}
    if plan.get("normative_index_ref_and_hash") != expected_index_ref:
        errors.append("plan:normative_index_ref_or_hash_mismatch")
    wp_id = str(plan["wp_id"])
    expected_clause_ids = {
        str(item["clause_id"])
        for item in index.get("clauses", [])
        if wp_id in item.get("consumer_wp_ids", [])
    }
    planned_clause_ids = set(map(str, plan.get("normative_clause_ids", [])))
    missing = sorted(expected_clause_ids - planned_clause_ids)
    extra = sorted(planned_clause_ids - expected_clause_ids)
    if missing:
        errors.append(f"plan:normative_clause_ids_missing:{missing}")
    if extra:
        errors.append(f"plan:normative_clause_ids_extra:{extra}")
    expected_requirement_ids = {
        str(item["requirement_id"])
        for item in index.get("requirement_catalog", [])
        if wp_id in item.get("applicable_wp_ids", [])
    }
    planned_requirement_ids = set(map(str, plan.get("requirement_ids", [])))
    if planned_requirement_ids != expected_requirement_ids:
        errors.append(
            "plan:requirement_ids_mismatch:"
            f"missing={sorted(expected_requirement_ids-planned_requirement_ids)}:"
            f"extra={sorted(planned_requirement_ids-expected_requirement_ids)}"
        )
    clauses_by_id = {str(item["clause_id"]): item for item in index.get("clauses", [])}
    expected_spec_refs = sorted(
        {
            (
                str(clauses_by_id[clause_id]["source_file"]),
                str(clauses_by_id[clause_id]["source_file_sha256"]),
            )
            for clause_id in expected_clause_ids
        }
    )
    actual_spec_refs = sorted((str(item["ref"]), str(item["sha256"])) for item in plan.get("normative_spec_refs_and_hashes", []))
    if actual_spec_refs != expected_spec_refs:
        errors.append("plan:normative_spec_refs_and_hashes_mismatch")
    actual = plan["plan_hash"]
    copy = dict(plan)
    copy["plan_hash"] = None
    expected = hashlib.sha256(json.dumps(copy, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if actual != expected:
        errors.append(f"plan:self_hash_mismatch:{actual}:{expected}")
    return len(planned_clause_ids), len(missing), len(extra)


def verify_normative_index(errors: list[str]) -> tuple[dict[str, object], int, int]:
    validate_instance(INDEX_PATH, IMPL / "normative-requirement-index.v1.schema.json", errors)
    spec = importlib.util.spec_from_file_location("normative_generator", HERE / "generate_normative_index.py")
    if spec is None or spec.loader is None:
        errors.append("normative:cannot_load_generator")
        return {}, 0, 0
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    expected = module.build()
    actual = load_json(INDEX_PATH)
    stable_fields = (
        "generator_contract_version", "generator", "generator_sha256", "source_set_sha256",
        "document_hashes", "normative_tokens", "clause_unit", "consumer_policy",
        "requirement_family_codes", "requirement_catalog", "canonical_work_package_ids",
        "clauses", "remainder",
    )
    for field in stable_fields:
        if actual.get(field) != expected.get(field):
            errors.append(f"normative:stale_or_modified:{field}")
    remainder = actual.get("remainder", {})
    for key in ("unclassified_clause_count", "duplicate_clause_id_count", "unmigrated_previous_clause_count", "unmapped_requirement_id_count", "clause_without_consumer_count", "local_only_without_temporary_doc0_consumer_count"):
        if remainder.get(key) != 0:
            errors.append(f"normative:structural_remainder_nonzero:{key}:{remainder.get(key)}")
    canonical_wps = set(map(str, actual.get("canonical_work_package_ids", [])))
    for item in actual.get("clauses", []):
        consumers = set(map(str, item.get("consumer_wp_ids", [])))
        unknown = sorted(consumers - canonical_wps)
        if unknown:
            errors.append(f"normative:unknown_clause_consumers:{item.get('clause_id')}:{unknown}")
        if item.get("classification") == "LOCAL_ONLY":
            if consumers != {"WP-DOC0"} or item.get("consumer_assignment_basis") != "DOC0_TEMPORARY_PENDING_INDEPENDENT_SEMANTIC_REVIEW":
                errors.append(f"normative:local_only_consumer_policy_mismatch:{item.get('clause_id')}")
        elif consumers != set(map(str, item.get("applicable_wp_ids", []))):
            errors.append(f"normative:exact_clause_consumer_mismatch:{item.get('clause_id')}")
    migration_path = IMPL / "normative-requirement-migrations.v1.json"
    if actual.get("migration_map_ref") != migration_path.name:
        errors.append("normative:migration_map_ref_mismatch")
    if actual.get("migration_map_sha256") != sha256(migration_path):
        errors.append("normative:migration_map_hash_mismatch")
    migration_map = load_json(migration_path)
    clause_migration_items = migration_map.get("mappings", [])
    clause_migrations = {
        str(item["old_clause_id"]): item
        for item in clause_migration_items
    }
    if len(clause_migrations) != len(clause_migration_items):
        errors.append("normative:duplicate_migration_map_old_clause_id")
    applied_clause_migrations = actual.get("applied_migrations", [])
    applied_old_ids = [str(item.get("old_clause_id")) for item in applied_clause_migrations]
    if len(applied_old_ids) != len(set(applied_old_ids)):
        errors.append("normative:duplicate_applied_clause_migration")
    current_clause_ids = {str(item["clause_id"]) for item in actual.get("clauses", [])}
    for item in applied_clause_migrations:
        old_id = str(item.get("old_clause_id"))
        if clause_migrations.get(old_id) != item:
            errors.append(f"normative:applied_clause_migration_not_exact_map_entry:{old_id}")
        unknown_targets = sorted(set(map(str, item.get("new_clause_ids", []))) - current_clause_ids)
        if unknown_targets:
            errors.append(f"normative:applied_clause_migration_target_missing:{old_id}:{unknown_targets}")
    policy_migration_items = migration_map.get("policy_migrations", [])
    policy_migrations = {
        str(item["migration_id"]): item
        for item in policy_migration_items
    }
    if len(policy_migrations) != len(policy_migration_items):
        errors.append("normative:duplicate_policy_migration_id")
    applied_policy_migrations = actual.get("applied_policy_migrations", [])
    applied_policy_ids = [str(item.get("migration_id")) for item in applied_policy_migrations]
    if len(applied_policy_ids) != len(set(applied_policy_ids)):
        errors.append("normative:duplicate_applied_policy_migration")
    for item in applied_policy_migrations:
        migration_id = str(item.get("migration_id"))
        if policy_migrations.get(migration_id) != item:
            errors.append(f"normative:applied_policy_migration_not_exact_map_entry:{migration_id}")
    if actual.get("generator_contract_version") == 3:
        expected_policy_id = "LOCAL-ONLY-CONSUMER-V2-TO-V3"
        if applied_policy_ids != [expected_policy_id]:
            errors.append(f"normative:v3_policy_migration_ledger_mismatch:{applied_policy_ids}")
        elif actual.get("previous_index_sha256") != policy_migrations[expected_policy_id]["old_index_sha256"]:
            errors.append("normative:v3_previous_index_hash_mismatch")
    return actual, len(actual.get("clauses", [])), int(remainder.get("pending_semantic_review_count", 0))


def audit_assignment_semantic_errors(assignment: dict[str, object]) -> list[str]:
    findings: list[str] = []
    envelope = assignment["signature_envelope"]
    assert isinstance(envelope, dict)
    if assignment["owner_actor_id"] == assignment["auditor_principal_id"]:
        findings.append("owner_and_auditor_must_differ")
    if envelope["signer_actor_id"] != assignment["owner_actor_id"]:
        findings.append("assignment_must_be_signed_by_owner")
    if envelope["signed_bytes_hash"] != assignment["signed_bytes_hash"]:
        findings.append("signed_bytes_hash_mismatch")
    root = assignment["externally_pinned_trust_root"]
    roster = assignment["actor_roster_ref_and_hash"]
    policy = assignment["human_gate_policy_ref_and_hash"]
    algorithms = assignment["signature_algorithm_registry_ref_and_hash"]
    assert all(isinstance(item, dict) for item in (root, roster, policy, algorithms))
    if envelope["trust_root_hash"] != root["sha256"]:
        findings.append("trust_root_hash_mismatch")
    if envelope["actor_roster_hash"] != roster["sha256"]:
        findings.append("actor_roster_hash_mismatch")
    if envelope["policy_hash"] != policy["sha256"]:
        findings.append("policy_hash_mismatch")
    if envelope["signature_algorithm_registry_hash"] != algorithms["sha256"]:
        findings.append("algorithm_registry_hash_mismatch")
    try:
        issued = parse_canonical_utc(assignment["issued_at"])
        not_before = parse_canonical_utc(assignment["not_before"])
        expires = parse_canonical_utc(assignment["expires_at"])
        if not (issued <= not_before < expires):
            findings.append("invalid_assignment_time_order")
    except (TypeError, ValueError):
        findings.append("invalid_assignment_rfc3339_timestamp")
    return findings


def audit_record_semantic_errors(record: dict[str, object], assignment: dict[str, object]) -> list[str]:
    findings: list[str] = []
    if record["wp_id"] != assignment["target_work_package_id"]:
        findings.append("work_package_mismatch")
    if record["auditor_principal_id"] != assignment["auditor_principal_id"]:
        findings.append("auditor_mismatch")
    if record["audited_subject"] != assignment["subject_commit_and_tree"]:
        findings.append("subject_mismatch")
    if record["audited_bundle_ref_and_hash"] != assignment["completion_bundle_ref_and_hash"]:
        findings.append("bundle_mismatch")
    if record["evidence_index_commit_if_any"] != assignment["evidence_index_commit_if_any"]:
        findings.append("index_commit_mismatch")
    assignment_ref = record["audit_assignment_ref_and_hash"]
    assert isinstance(assignment_ref, dict)
    if assignment_ref["sha256"] != assignment["assignment_hash"]:
        findings.append("assignment_hash_mismatch")
    external_root = record["externally_observed_pinned_trust_root"]
    assignment_root = assignment["externally_pinned_trust_root"]
    assert isinstance(external_root, dict) and isinstance(assignment_root, dict)
    if external_root["trust_root_hash"] != assignment_root["sha256"]:
        findings.append("external_root_mismatch")
    owner_channel = assignment["owner_repo_external_channel"]
    assert isinstance(owner_channel, dict)
    if external_root["source_channel_id"] != owner_channel["channel_id"]:
        findings.append("external_root_channel_mismatch")
    envelope = record["signature_envelope"]
    assert isinstance(envelope, dict)
    if envelope["signer_principal_id"] != record["auditor_principal_id"]:
        findings.append("record_must_be_signed_by_assigned_auditor")
    if envelope["signed_bytes_hash"] != record["signed_bytes_hash"]:
        findings.append("record_signed_bytes_hash_mismatch")
    assigned_key = assignment["auditor_attestation_public_key"]
    assert isinstance(assigned_key, dict)
    if record["auditor_attestation_key_id"] != assigned_key["key_id"]:
        findings.append("auditor_attestation_key_id_mismatch")
    if record["auditor_attestation_public_key_hash"] != assigned_key["public_key_sha256"]:
        findings.append("auditor_attestation_public_key_hash_mismatch")
    if envelope["key_id"] != assigned_key["key_id"]:
        findings.append("signature_key_id_mismatch")
    required_specs = assignment["required_audit_plan_and_spec_refs_and_hashes"]
    if record["audit_plan_and_spec_refs_and_hashes"] != required_specs:
        findings.append("audit_plan_and_spec_scope_mismatch")
    allowed_scope = assignment["allowed_audit_scope"]
    assert isinstance(allowed_scope, dict)
    allowed_axes = set(map(str, allowed_scope["allowed_audit_axes"]))
    finding_items = record["findings"]
    assert isinstance(finding_items, list)
    finding_ids = [str(item["finding_id"]) for item in finding_items]
    if len(finding_ids) != len(set(finding_ids)):
        findings.append("duplicate_finding_id")
    known_finding_ids = set(finding_ids)
    axis_verdicts = record["axis_verdicts"]
    assert isinstance(axis_verdicts, dict)
    pass_like = {"AUDITED_PASS", "SUPPORTS"}
    for axis in ("implementation", "factory", "scientific", "production_scale"):
        axis_record = axis_verdicts[axis]
        assert isinstance(axis_record, dict)
        expected_ids = {
            str(item["finding_id"])
            for item in finding_items
            if axis in set(map(str, item["affected_axes"]))
        }
        actual_ids = set(map(str, axis_record["finding_ids"]))
        if actual_ids != expected_ids:
            findings.append(
                f"axis_finding_closure_mismatch:{axis}:"
                f"missing={sorted(expected_ids-actual_ids)}:extra={sorted(actual_ids-expected_ids)}"
            )
        if actual_ids - known_finding_ids:
            findings.append(f"axis_unknown_finding_ids:{axis}:{sorted(actual_ids-known_finding_ids)}")
        verdict = str(axis_record["verdict"])
        evidence_refs = axis_record["evidence_refs"]
        reason = axis_record["scope_reason_if_not_tested"]
        if axis not in allowed_axes and verdict != "NOT_TESTED":
            findings.append(f"axis_outside_assignment_scope_was_tested:{axis}")
        if verdict == "NOT_TESTED":
            if not isinstance(reason, str) or not reason.strip():
                findings.append(f"not_tested_axis_missing_scope_reason:{axis}")
            if evidence_refs:
                findings.append(f"not_tested_axis_has_evidence:{axis}")
            if expected_ids:
                findings.append(f"not_tested_axis_has_findings:{axis}")
        else:
            if reason is not None:
                findings.append(f"tested_axis_has_scope_reason:{axis}")
            if not evidence_refs and not expected_ids:
                findings.append(f"tested_axis_without_evidence_or_finding:{axis}")
        unresolved_p0 = any(
            item["severity"] == "P0"
            and item["status"] != "RESOLVED_BY_AUDITED_SUBJECT"
            and axis in item["affected_axes"]
            for item in finding_items
        )
        if unresolved_p0 and verdict in pass_like:
            findings.append(f"unresolved_p0_with_pass_like_verdict:{axis}")
    implementation_verdict = str(axis_verdicts["implementation"]["verdict"])
    if implementation_verdict == "AUDITED_PASS" and (record["traceability_remainder"] != 0 or record["orphan_remainder"] != 0):
        findings.append("implementation_pass_with_nonzero_remainder")
    try:
        created = parse_canonical_utc(record["created_at"])
        observed = parse_canonical_utc(external_root["observed_at"])
        not_before = parse_canonical_utc(assignment["not_before"])
        expires = parse_canonical_utc(assignment["expires_at"])
        if not (not_before <= observed <= created < expires):
            findings.append("record_or_root_observation_outside_assignment_window")
    except (TypeError, ValueError):
        findings.append("invalid_record_rfc3339_timestamp")
    return findings


def self_hash(value: dict[str, object], field: str) -> str:
    candidate = copy.deepcopy(value)
    candidate[field] = None
    return canonical_json_sha256(candidate)


BUDGET_DIMENSIONS = (
    "invocations",
    "solver_launches",
    "database_writes",
    "redis_writes",
    "d_volume_writes",
    "human_gate_commits",
    "active_release_changes",
    "tokens",
    "cost_microunits",
)


def vault_access_capability_semantic_errors(capability: dict[str, object]) -> list[str]:
    findings: list[str] = []
    principal = capability["principal"]
    issuer = capability["issuer"]
    envelope = capability["signature_envelope"]
    root = capability["externally_pinned_trust_root"]
    registry = capability["issuer_key_registry_ref_and_hash"]
    assert all(isinstance(item, dict) for item in (principal, issuer, envelope, root, registry))
    if envelope["signed_bytes_hash"] != capability["signed_bytes_hash"]:
        findings.append("vault_signed_bytes_hash_mismatch")
    if envelope["signer_principal_id"] != issuer["issuer_principal_id"]:
        findings.append("vault_issuer_principal_mismatch")
    if envelope["key_id"] != issuer["issuer_key_id"]:
        findings.append("vault_issuer_key_mismatch")
    if envelope["trust_root_hash"] != root["sha256"]:
        findings.append("vault_trust_root_mismatch")
    if envelope["issuer_key_registry_hash"] != registry["sha256"]:
        findings.append("vault_key_registry_mismatch")
    if principal["principal_type"] == "TARGET_SOLVER":
        if principal["target_solver_contract_sha256"] is None or principal["execution_attempt_id"] is None:
            findings.append("target_solver_identity_incomplete")
        object_binding = capability["object_binding"]
        assert isinstance(object_binding, dict)
        if object_binding["sensitivity"] in {"SOLUTION_BEARING", "HOLDOUT_BEARING"}:
            findings.append("target_solver_sensitive_source_forbidden")
    try:
        issued = parse_canonical_utc(capability["issued_at"])
        not_before = parse_canonical_utc(capability["not_before"])
        expires = parse_canonical_utc(capability["expires_at"])
        if not (issued <= not_before < expires):
            findings.append("vault_invalid_time_order")
    except (TypeError, ValueError):
        findings.append("vault_invalid_rfc3339_timestamp")
    return findings


def external_execution_authorization_semantic_errors(authorization: dict[str, object]) -> list[str]:
    findings: list[str] = []
    envelope = authorization["signature_envelope"]
    root = authorization["externally_pinned_trust_root"]
    roster = authorization["actor_roster_ref_and_hash"]
    policy = authorization["human_gate_policy_ref_and_hash"]
    algorithms = authorization["signature_algorithm_registry_ref_and_hash"]
    assert all(isinstance(item, dict) for item in (envelope, root, roster, policy, algorithms))
    if envelope["signed_bytes_hash"] != authorization["signed_bytes_hash"]:
        findings.append("authorization_signed_bytes_hash_mismatch")
    if envelope["signer_actor_id"] != authorization["issuer_actor_id"]:
        findings.append("authorization_issuer_actor_mismatch")
    if envelope["key_id"] != authorization["issuer_key_id"]:
        findings.append("authorization_issuer_key_mismatch")
    if envelope["trust_root_hash"] != root["sha256"]:
        findings.append("authorization_trust_root_mismatch")
    if envelope["actor_roster_hash"] != roster["sha256"]:
        findings.append("authorization_actor_roster_mismatch")
    if envelope["policy_hash"] != policy["sha256"]:
        findings.append("authorization_policy_mismatch")
    if envelope["signature_algorithm_registry_hash"] != algorithms["sha256"]:
        findings.append("authorization_algorithm_registry_mismatch")
    scopes = authorization["action_scopes"]
    assert isinstance(scopes, list)
    scope_ids = [str(item["scope_id"]) for item in scopes]
    scope_hashes = [str(item["scope_hash"]) for item in scopes]
    if len(scope_ids) != len(set(scope_ids)):
        findings.append("duplicate_authorization_scope_id")
    if len(scope_hashes) != len(set(scope_hashes)):
        findings.append("duplicate_authorization_scope_hash")
    try:
        issued = parse_canonical_utc(authorization["issued_at"])
        not_before = parse_canonical_utc(authorization["not_before"])
        expires = parse_canonical_utc(authorization["expires_at"])
        if not (issued <= not_before < expires):
            findings.append("authorization_invalid_time_order")
    except (TypeError, ValueError):
        findings.append("authorization_invalid_rfc3339_timestamp")
    return findings


def live_run_permit_semantic_errors(
    permit: dict[str, object],
    authorization: dict[str, object],
) -> list[str]:
    findings: list[str] = []
    if permit["parent_authorization_id"] != authorization["authorization_id"]:
        findings.append("permit_parent_authorization_id_mismatch")
    if permit["parent_authorization_signed_bytes_hash"] != authorization["signed_bytes_hash"]:
        findings.append("permit_parent_signed_bytes_hash_mismatch")
    if permit["authorization_mode"] != authorization["authorization_mode"]:
        findings.append("permit_authorization_mode_mismatch")
    if permit["wp_id"] not in authorization["subject_work_package_ids"]:
        findings.append("permit_work_package_outside_parent")
    if permit["epoch_id_if_any"] != authorization["epoch_id_if_any"]:
        findings.append("permit_epoch_mismatch")
    if permit["run_id_if_any"] != authorization["run_id_if_any"]:
        findings.append("permit_run_mismatch")
    for field in (
        "externally_pinned_trust_root",
        "actor_roster_ref_and_hash",
        "human_gate_policy_ref_and_hash",
        "signature_algorithm_registry_ref_and_hash",
        "revocation_policy_ref_and_hash",
    ):
        if permit[field] != authorization[field]:
            findings.append(f"permit_parent_security_binding_mismatch:{field}")
    envelope = permit["signature_envelope"]
    root = permit["externally_pinned_trust_root"]
    roster = permit["actor_roster_ref_and_hash"]
    policy = permit["human_gate_policy_ref_and_hash"]
    algorithms = permit["signature_algorithm_registry_ref_and_hash"]
    assert all(isinstance(item, dict) for item in (envelope, root, roster, policy, algorithms))
    if envelope["signed_bytes_hash"] != permit["signed_bytes_hash"]:
        findings.append("permit_signed_bytes_hash_mismatch")
    if envelope["signer_actor_id"] != permit["issuer_actor_id"]:
        findings.append("permit_issuer_actor_mismatch")
    if envelope["key_id"] != permit["issuer_key_id"]:
        findings.append("permit_issuer_key_mismatch")
    if envelope["trust_root_hash"] != root["sha256"]:
        findings.append("permit_trust_root_mismatch")
    if envelope["actor_roster_hash"] != roster["sha256"]:
        findings.append("permit_actor_roster_mismatch")
    if envelope["policy_hash"] != policy["sha256"]:
        findings.append("permit_policy_mismatch")
    if envelope["signature_algorithm_registry_hash"] != algorithms["sha256"]:
        findings.append("permit_algorithm_registry_mismatch")
    parent_scopes = authorization["action_scopes"]
    assert isinstance(parent_scopes, list)
    scopes_by_pair: dict[tuple[str, str], list[dict[str, object]]] = {}
    for scope in parent_scopes:
        assert isinstance(scope, dict)
        pair = (str(scope["scope_id"]), str(scope["scope_hash"]))
        scopes_by_pair.setdefault(pair, []).append(scope)
    action_units = permit["action_units"]
    assert isinstance(action_units, list)
    ordinals = [int(item["consumption_ordinal"]) for item in action_units]
    if len(ordinals) != len(set(ordinals)):
        findings.append("duplicate_permit_consumption_ordinal")
    aggregate_by_scope: dict[tuple[str, str], dict[str, int]] = {}
    for unit in action_units:
        assert isinstance(unit, dict)
        pair = (str(unit["parent_action_scope_id"]), str(unit["parent_action_scope_hash"]))
        matches = scopes_by_pair.get(pair, [])
        if len(matches) != 1:
            findings.append(f"permit_parent_scope_match_count:{pair}:{len(matches)}")
            continue
        scope = matches[0]
        for field in ("action_kind", "authorization_action_registry_entry_ref_and_hash"):
            if unit[field] != scope[field]:
                findings.append(f"permit_unit_scope_mismatch:{field}:{unit['consumption_ordinal']}")
        profile = unit["carrier_profile_or_solver_contract_hash_if_any"]
        allowed_profiles = set(scope["allowed_carrier_profile_hashes"]) | set(scope["allowed_role_or_solver_contract_hashes"])
        if profile is not None and profile not in allowed_profiles:
            findings.append(f"permit_profile_outside_parent:{unit['consumption_ordinal']}")
        allowed_inputs = {str(item["input_hash"]) for item in scope["allowed_inputs"]}
        if unit["input_hash"] not in allowed_inputs:
            findings.append(f"permit_input_outside_parent:{unit['consumption_ordinal']}")
        if unit["required_output_sink_and_acl_hash_if_any"] != scope["required_output_sink_and_acl_hash_if_any"]:
            findings.append(f"permit_sink_outside_parent:{unit['consumption_ordinal']}")
        unit_budget = unit["unit_budget"]
        scope_budget = scope["budget"]
        assert isinstance(unit_budget, dict) and isinstance(scope_budget, dict)
        if unit_budget["currency"] != scope_budget["currency"]:
            findings.append(f"permit_currency_mismatch:{unit['consumption_ordinal']}")
        totals = aggregate_by_scope.setdefault(pair, {dimension: 0 for dimension in BUDGET_DIMENSIONS})
        for dimension in BUDGET_DIMENSIONS:
            unit_value = int(unit_budget[f"max_{dimension}"])
            if unit_value > int(scope_budget[f"max_{dimension}"]):
                findings.append(f"permit_unit_budget_exceeds_parent:{dimension}:{unit['consumption_ordinal']}")
            totals[dimension] += unit_value
    for pair, totals in aggregate_by_scope.items():
        matches = scopes_by_pair.get(pair, [])
        if len(matches) != 1:
            continue
        scope_budget = matches[0]["budget"]
        assert isinstance(scope_budget, dict)
        for dimension, total in totals.items():
            if total > int(scope_budget[f"max_{dimension}"]):
                findings.append(f"permit_aggregate_budget_exceeds_parent:{dimension}:{pair}")
    try:
        parent_not_before = parse_canonical_utc(authorization["not_before"])
        parent_expires = parse_canonical_utc(authorization["expires_at"])
        issued = parse_canonical_utc(permit["issued_at"])
        not_before = parse_canonical_utc(permit["not_before"])
        expires = parse_canonical_utc(permit["expires_at"])
        if not (parent_not_before <= issued <= not_before < expires <= parent_expires):
            findings.append("permit_time_not_parent_subset")
    except (TypeError, ValueError):
        findings.append("permit_invalid_rfc3339_timestamp")
    return findings


def authorization_consumption_receipt_semantic_errors(
    receipt: dict[str, object],
    permit: dict[str, object],
    authorization: dict[str, object],
) -> list[str]:
    findings: list[str] = []
    if receipt["parent_authorization_id"] != authorization["authorization_id"]:
        findings.append("receipt_parent_authorization_id_mismatch")
    if receipt["permit_id"] != permit["permit_id"]:
        findings.append("receipt_permit_id_mismatch")
    action_units = permit["action_units"]
    assert isinstance(action_units, list)
    matches = [unit for unit in action_units if unit["consumption_ordinal"] == receipt["consumption_ordinal"]]
    if len(matches) != 1:
        findings.append(f"receipt_permit_ordinal_match_count:{len(matches)}")
    else:
        unit = matches[0]
        for field in (
            "parent_action_scope_id",
            "parent_action_scope_hash",
            "action_kind",
            "authorization_action_registry_entry_ref_and_hash",
            "job_id",
            "attempt_id",
            "input_hash",
            "carrier_profile_or_solver_contract_hash_if_any",
            "target_binding_hash",
            "required_output_sink_and_acl_hash_if_any",
            "idempotency_key",
        ):
            if receipt[field] != unit[field]:
                findings.append(f"receipt_action_unit_binding_mismatch:{field}")
        unit_budget = unit["unit_budget"]
        reserved = receipt["reserved_unit_budget"]
        assert isinstance(unit_budget, dict) and isinstance(reserved, dict)
        if reserved["currency"] != unit_budget["currency"]:
            findings.append("receipt_reserved_currency_mismatch")
        for dimension in BUDGET_DIMENSIONS:
            if int(reserved[dimension]) != int(unit_budget[f"max_{dimension}"]):
                findings.append(f"receipt_reserved_budget_mismatch:{dimension}")
    reserved = receipt["reserved_unit_budget"]
    actual = receipt["actual_side_effects"]
    held = receipt["held_allowance"]
    released = receipt["released_allowance"]
    remaining = receipt["remaining_allowance"]
    assert all(isinstance(item, dict) for item in (reserved, actual, held, released, remaining))
    currencies = {str(item["currency"]) for item in (reserved, actual, held, released, remaining)}
    if len(currencies) != 1:
        findings.append("receipt_currency_mismatch")
    for dimension in BUDGET_DIMENSIONS:
        if int(reserved[dimension]) != int(actual[dimension]) + int(held[dimension]) + int(released[dimension]):
            findings.append(f"receipt_allowance_not_conserved:{dimension}")
    if receipt["state_revision"] == 0 and receipt["previous_receipt_ref_and_hash_if_any"] is not None:
        findings.append("receipt_initial_revision_has_previous")
    if receipt["state_revision"] > 0 and receipt["previous_receipt_ref_and_hash_if_any"] is None:
        findings.append("receipt_later_revision_missing_previous")
    attestation = receipt["service_attestation"]
    root = receipt["externally_pinned_trust_root"]
    registry = receipt["service_attestation_key_registry_ref_and_hash"]
    assert all(isinstance(item, dict) for item in (attestation, root, registry))
    if attestation["attested_bytes_hash"] != receipt["attested_bytes_hash"]:
        findings.append("receipt_attested_bytes_hash_mismatch")
    if attestation["trust_root_hash"] != root["sha256"]:
        findings.append("receipt_trust_root_mismatch")
    if attestation["service_attestation_key_registry_hash"] != registry["sha256"]:
        findings.append("receipt_key_registry_mismatch")
    try:
        reserved_at = parse_canonical_utc(receipt["reserved_at"])
        recorded_at = parse_canonical_utc(receipt["status_recorded_at"])
        terminal = receipt["terminal_at_if_any"]
        if recorded_at < reserved_at:
            findings.append("receipt_status_before_reservation")
        if terminal is not None and parse_canonical_utc(terminal) < recorded_at:
            findings.append("receipt_terminal_before_status")
    except (TypeError, ValueError):
        findings.append("receipt_invalid_rfc3339_timestamp")
    return findings


def expected_spec_refs(index: dict[str, object]) -> list[dict[str, str]]:
    document_hashes = index["document_hashes"]
    assert isinstance(document_hashes, dict)
    return [
        {"ref": str(reference), "sha256": str(metadata["full_file_sha256"])}
        for reference, metadata in sorted(document_hashes.items())
    ]


def expected_schema_refs() -> list[dict[str, str]]:
    return [ref_hash(path) for path in sorted(IMPL.glob("*.schema.json"))]


def doc_contract_receipt_semantic_errors(
    receipt: dict[str, object],
    expected_counts: dict[str, int],
    index: dict[str, object],
) -> list[str]:
    findings: list[str] = []
    subject = receipt["implementation_subject"]
    assert isinstance(subject, dict)
    actual_subject = current_implementation_subject()
    if subject != actual_subject:
        findings.append("doc_receipt_subject_mismatch")
    expected_refs = {
        "normative_index_ref_and_hash": ref_hash(INDEX_PATH),
        "canonical_dag_ref_and_hash": ref_hash(DAG_PATH),
        "work_package_plan_ref_and_hash": ref_hash(PLAN_PATH),
        "migration_map_ref_and_hash": ref_hash(IMPL / "normative-requirement-migrations.v1.json"),
        "checker_ref_and_hash": ref_hash(Path(__file__)),
        "dependency_lock_ref_and_hash": ref_hash(IMPL / "requirements-docs.txt"),
    }
    for field, expected in expected_refs.items():
        if receipt[field] != expected:
            findings.append(f"doc_receipt_ref_mismatch:{field}")
    if receipt["checked_source_set_sha256"] != index["source_set_sha256"]:
        findings.append("doc_receipt_source_set_mismatch")
    if receipt["spec_refs_and_hashes"] != expected_spec_refs(index):
        findings.append("doc_receipt_spec_set_mismatch")
    if receipt["schema_refs_and_hashes"] != expected_schema_refs():
        findings.append("doc_receipt_schema_set_mismatch")
    if set(map(str, receipt["verification_ids"])) != set(DOC0_VERIFICATION_IDS):
        findings.append("doc_receipt_verification_ids_mismatch")
    if receipt["counts"] != expected_counts:
        findings.append("doc_receipt_counts_mismatch")
    try:
        started = parse_canonical_utc(receipt["started_at"])
        completed = parse_canonical_utc(receipt["completed_at"])
        if completed <= started:
            findings.append("doc_receipt_nonpositive_duration")
    except (TypeError, ValueError):
        findings.append("doc_receipt_invalid_rfc3339_timestamp")
    output = receipt["output_binding"]
    assert isinstance(output, dict)
    expected_output = canonical_json_sha256(
        {"verdict": receipt["verdict"], "counts": receipt["counts"], "errors": receipt["errors"]}
    )
    if output["sha256"] != expected_output:
        findings.append("doc_receipt_output_hash_mismatch")
    if receipt["receipt_hash"] != self_hash(receipt, "receipt_hash"):
        findings.append("doc_receipt_self_hash_mismatch")
    if receipt["verdict"] == "PASS" and receipt["errors"]:
        findings.append("doc_receipt_pass_with_errors")
    if receipt["verdict"] == "FAIL" and not receipt["errors"]:
        findings.append("doc_receipt_fail_without_errors")
    return findings


def doc0_test_receipt_semantic_errors(
    receipt: dict[str, object],
    plan: dict[str, object],
    index: dict[str, object],
) -> list[str]:
    findings: list[str] = []
    if receipt["checked_source_set_sha256"] != index["source_set_sha256"]:
        findings.append("doc0_test_source_set_mismatch")
    if receipt["normative_index_ref_and_hash"] != ref_hash(INDEX_PATH):
        findings.append("doc0_test_index_ref_mismatch")
    if receipt["work_package_plan_ref_and_hash"] != ref_hash(PLAN_PATH):
        findings.append("doc0_test_plan_ref_mismatch")
    if receipt["dependency_lock_ref_and_hash"] != ref_hash(IMPL / "requirements-docs.txt"):
        findings.append("doc0_test_dependency_lock_mismatch")
    expected_sources = expected_spec_refs(index) + expected_schema_refs()
    if receipt["schema_and_spec_refs_and_hashes"] != expected_sources:
        findings.append("doc0_test_schema_and_spec_set_mismatch")
    commands = receipt["commands"]
    assert isinstance(commands, list)
    command_ids = [str(command["command_id"]) for command in commands]
    if len(command_ids) != len(set(command_ids)):
        findings.append("doc0_test_duplicate_command_id")
    all_test_ids: list[str] = []
    completed_times: list[datetime] = []
    command_passes: list[bool] = []
    for command in commands:
        summary = command["test_summary"]
        assert isinstance(summary, dict)
        test_ids = list(map(str, command["test_ids"]))
        all_test_ids.extend(test_ids)
        if summary["executed"] != summary["passed"] + summary["failed"] + summary["errors"]:
            findings.append(f"doc0_test_executed_arithmetic:{command['command_id']}")
        if summary["discovered"] != summary["executed"] + summary["skipped"]:
            findings.append(f"doc0_test_discovered_arithmetic:{command['command_id']}")
        computed_pass = (
            command["exit_code"] == 0
            and summary["executed"] > 0
            and summary["passed"] > 0
            and summary["failed"] == 0
            and summary["errors"] == 0
        )
        if (command["verdict"] == "PASS") != computed_pass:
            findings.append(f"doc0_test_command_verdict_mismatch:{command['command_id']}")
        command_passes.append(computed_pass)
        try:
            started = parse_canonical_utc(command["started_at"])
            completed = parse_canonical_utc(command["completed_at"])
            if completed <= started:
                findings.append(f"doc0_test_nonpositive_duration:{command['command_id']}")
            completed_times.append(completed)
        except (TypeError, ValueError):
            findings.append(f"doc0_test_invalid_rfc3339_timestamp:{command['command_id']}")
    if len(all_test_ids) != len(set(all_test_ids)):
        findings.append("doc0_test_duplicate_test_id_across_commands")
    if set(all_test_ids) != set(map(str, plan["test_plan_ids"])):
        findings.append("doc0_test_plan_test_ids_mismatch")
    computed_aggregate_pass = bool(commands) and all(command_passes)
    if (receipt["aggregate_verdict"] == "PASS") != computed_aggregate_pass:
        findings.append("doc0_test_aggregate_verdict_mismatch")
    try:
        created = parse_canonical_utc(receipt["created_at"])
        if completed_times and created < max(completed_times):
            findings.append("doc0_test_receipt_created_before_completion")
    except (TypeError, ValueError):
        findings.append("doc0_test_invalid_created_at")
    if receipt["receipt_hash"] != self_hash(receipt, "receipt_hash"):
        findings.append("doc0_test_self_hash_mismatch")
    return findings


def valid_vault_access_capability_fixture() -> dict[str, object]:
    h = "0" * 64
    sig = "A" * 86 + "=="
    opaque = lambda name: {"ref_id": name, "sha256": h}
    principal = {
        "principal_id": "target-solver-1",
        "principal_type": "TARGET_SOLVER",
        "role_type_id": None,
        "carrier_profile_sha256": None,
        "target_solver_contract_sha256": h,
        "execution_attempt_id": "solver-attempt-1",
    }
    capability: dict[str, object] = {
        "schema_id": "seven/vault-access-capability",
        "schema_version": 1,
        "object_type": "VaultAccessCapability",
        "capability_id": "vault-capability-1",
        "principal": principal,
        "operation": "READ_DERIVED_VIEW",
        "object_binding": {"object_id": "problem-view-source", "object_sha256": h, "sensitivity": "RESTRICTED"},
        "view_binding": {"view_id": "solver-view-1", "view_sha256": h, "view_policy_sha256": h},
        "sink_binding": {"sink_id": "solver-input-1", "sink_kind": "EPHEMERAL_MODEL_INPUT", "sink_policy_sha256": h},
        "access_policy_ref_and_hash": opaque("vault-access-policy-1"),
        "deny_by_default": True,
        "raw_vault_path_disclosure": False,
        "issued_at": "2026-08-14T00:00:00Z",
        "not_before": "2026-08-14T00:00:01Z",
        "expires_at": "2026-08-14T01:00:00Z",
        "nonce": "vault-nonce-00000001",
        "issuer": {"issuer_principal_id": "vault-service", "issuer_key_id": "vault-key-1", "issuer_public_key_sha256": h},
        "revocation": {"revocable": True, "revocation_handle": "vault-revocation-1", "status_at_issue": "ACTIVE", "registry_ref_and_hash": opaque("vault-revocation-registry")},
        "externally_pinned_trust_root": {"object_id": "vault-trust-root", "sha256": h},
        "issuer_key_registry_ref_and_hash": opaque("vault-key-registry"),
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-vault-access-capability/v1\u0000",
        "signed_bytes_hash": h,
        "signature_envelope": {
            "algorithm": "Ed25519",
            "key_id": "vault-key-1",
            "signer_principal_id": "vault-service",
            "signature_encoding": "base64",
            "signature_b64": sig,
            "signed_bytes_hash": h,
            "trust_root_hash": h,
            "issuer_key_registry_hash": h,
        },
        "capability_hash_algorithm": "sha256(RFC8785-JCS-object-with-capability_hash-null)",
        "capability_hash": h,
    }
    return capability


def valid_view_derivation_fixture(capability: dict[str, object]) -> dict[str, object]:
    h = "0" * 64
    sig = "A" * 86 + "=="
    opaque = lambda name: {"ref_id": name, "sha256": h}
    derivation: dict[str, object] = {
        "schema_id": "seven/view-derivation",
        "schema_version": 1,
        "object_type": "ViewDerivation",
        "derivation_id": "view-derivation-1",
        "capability_ref_and_hash": opaque("vault-capability-1"),
        "access_decision_ref_and_hash": opaque("access-decision-1"),
        "principal": copy.deepcopy(capability["principal"]),
        "operation": "READ_DERIVED_VIEW",
        "source_object": copy.deepcopy(capability["object_binding"]),
        "derived_view": copy.deepcopy(capability["view_binding"]),
        "sink_binding": copy.deepcopy(capability["sink_binding"]),
        "view_policy_ref_and_hash": opaque("view-policy-1"),
        "derivation_rule_ref_and_hash": opaque("derivation-rule-1"),
        "generator_ref_and_hash": opaque("view-generator-1"),
        "redaction_manifest_ref_and_hash": opaque("redaction-manifest-1"),
        "sink_write_receipt_ref_and_hash": opaque("sink-write-1"),
        "revocation_check": {
            "revocation_handle": "vault-revocation-1",
            "status": "ACTIVE",
            "registry_ref_and_hash": opaque("vault-revocation-registry"),
            "checked_at": "2026-08-14T00:00:02Z",
            "revocation_record_ref_and_hash": None,
        },
        "nonce": "view-nonce-000000001",
        "deny_by_default": True,
        "raw_vault_path_disclosed": False,
        "model_delivery": {
            "delivery_mode": "OPAQUE_HANDLE_AND_DERIVED_BYTES",
            "delivered_view_binding_source": "TOP_LEVEL_DERIVED_VIEW",
            "raw_vault_locator_exposed": False,
            "capability_token_exposed": False,
        },
        "derived_at": "2026-08-14T00:00:03Z",
        "issuer": {"issuer_principal_id": "vault-service", "issuer_key_id": "vault-key-1", "issuer_public_key_sha256": h},
        "externally_pinned_trust_root": {"object_id": "vault-trust-root", "sha256": h},
        "issuer_key_registry_ref_and_hash": opaque("vault-key-registry"),
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-view-derivation/v1\u0000",
        "signed_bytes_hash": h,
        "signature_envelope": {
            "algorithm": "Ed25519", "key_id": "vault-key-1", "signer_principal_id": "vault-service",
            "signature_encoding": "base64", "signature_b64": sig, "signed_bytes_hash": h,
            "trust_root_hash": h, "issuer_key_registry_hash": h,
        },
        "derivation_hash_algorithm": "sha256(RFC8785-JCS-object-with-derivation_hash-null)",
        "derivation_hash": h,
    }
    return derivation


def valid_authorization_chain_fixtures() -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    h = "0" * 64
    sig = "A" * 86 + "=="
    ref = lambda name: {"ref": name, "sha256": h}
    zero_max_budget = {
        "max_invocations": 0, "max_solver_launches": 0, "max_database_writes": 0,
        "max_redis_writes": 0, "max_d_volume_writes": 0, "max_human_gate_commits": 0,
        "max_active_release_changes": 0, "max_tokens": 0, "max_cost_microunits": 0, "currency": "USD",
    }
    scope_budget = dict(zero_max_budget)
    scope_budget.update({"max_invocations": 1, "max_tokens": 100})
    scope = {
        "scope_id": "authoring-scope-1",
        "scope_hash_algorithm": "sha256(RFC8785-JCS-action-scope-with-scope_hash-null)",
        "scope_hash": h,
        "action_kind": "MODEL_ROLE_INVOKE",
        "authorization_action_registry_entry_ref_and_hash": ref("model-role-invoke"),
        "target_site_hash_if_any": h,
        "target_database_identity_hash_if_any": None,
        "target_redis_namespace_hash_if_any": None,
        "target_release_or_pointer_hash_if_any": None,
        "allowed_carrier_profile_hashes": [h],
        "allowed_role_or_solver_contract_hashes": [],
        "allowed_inputs": [{"input_hash": h, "sensitivity": "restricted"}],
        "required_output_sink_and_acl_hash_if_any": h,
        "budget": scope_budget,
    }
    security_refs = {
        "externally_pinned_trust_root": {"object_id": "human-gate-root", "sha256": h},
        "actor_roster_ref_and_hash": ref("actor-roster"),
        "human_gate_policy_ref_and_hash": ref("human-gate-policy"),
        "signature_algorithm_registry_ref_and_hash": ref("signature-algorithms"),
        "revocation_policy_ref_and_hash": ref("revocation-policy"),
    }
    authorization: dict[str, object] = {
        "schema_id": "seven/external-execution-authorization",
        "schema_version": 1,
        "authorization_id": "authorization-1",
        "authorization_mode": "UNAUDITED_AUTHORIZED_CANARY",
        "subject_work_package_ids": ["WP-CW-D1"],
        "subject_completion_bundle_refs_and_hashes": [ref("cw-d1-bundle")],
        "activation_audit_record_refs_and_hashes": [],
        "unaudited_dependency_bundle_refs_and_hashes": [ref("cw0-bundle")],
        "epoch_id_if_any": "epoch-1",
        "run_id_if_any": "run-1",
        "authorization_action_registry_ref_and_hash": ref("authorization-action-registry"),
        "action_scopes": [scope],
        **copy.deepcopy(security_refs),
        "stop_conditions": ["stop after one invocation"],
        "issuer_actor_id": "site-owner",
        "issuer_key_id": "owner-key-1",
        "issued_at": "2026-08-14T00:00:00Z",
        "not_before": "2026-08-14T00:00:01Z",
        "expires_at": "2026-08-14T02:00:00Z",
        "nonce": "authorization-nonce-0001",
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-external-execution-authorization/v1\u0000",
        "signed_bytes_hash": h,
        "signature_envelope": {
            "algorithm": "Ed25519", "key_id": "owner-key-1", "signer_actor_id": "site-owner",
            "signature_encoding": "base64", "signature_b64": sig, "signed_bytes_hash": h,
            "trust_root_hash": h, "actor_roster_hash": h, "policy_hash": h,
            "signature_algorithm_registry_hash": h,
        },
        "authorization_hash_algorithm": "sha256(RFC8785-JCS-object-with-authorization_hash-null)",
        "authorization_hash": h,
    }
    unit_budget = dict(scope_budget)
    action_unit = {
        "consumption_ordinal": 0,
        "parent_action_scope_id": "authoring-scope-1",
        "parent_action_scope_hash": h,
        "action_kind": "MODEL_ROLE_INVOKE",
        "authorization_action_registry_entry_ref_and_hash": ref("model-role-invoke"),
        "job_id": "job-1",
        "attempt_id": "attempt-1",
        "input_hash": h,
        "carrier_profile_or_solver_contract_hash_if_any": h,
        "target_binding_hash": h,
        "required_output_sink_and_acl_hash_if_any": h,
        "idempotency_key": "idempotency-key-0001",
        "unit_budget": unit_budget,
    }
    permit: dict[str, object] = {
        "schema_id": "seven/live-run-permit",
        "schema_version": 1,
        "permit_id": "permit-1",
        "parent_authorization_id": "authorization-1",
        "parent_authorization_ref_and_hash": ref("authorization-1"),
        "parent_authorization_signed_bytes_hash": h,
        "parent_subset_verification_contract_ref_and_hash": ref("subset-verifier"),
        "authorization_mode": "UNAUDITED_AUTHORIZED_CANARY",
        "wp_id": "WP-CW-D1",
        "epoch_id_if_any": "epoch-1",
        "run_id_if_any": "run-1",
        "action_units": [action_unit],
        "required_reservation_backend": "DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER",
        **copy.deepcopy(security_refs),
        "issuer_actor_id": "site-owner",
        "issuer_key_id": "owner-key-1",
        "issued_at": "2026-08-14T00:00:01Z",
        "not_before": "2026-08-14T00:00:02Z",
        "expires_at": "2026-08-14T01:00:00Z",
        "nonce": "permit-nonce-00000001",
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-live-run-permit/v1\u0000",
        "signed_bytes_hash": h,
        "signature_envelope": {
            "algorithm": "Ed25519", "key_id": "owner-key-1", "signer_actor_id": "site-owner",
            "signature_encoding": "base64", "signature_b64": sig, "signed_bytes_hash": h,
            "trust_root_hash": h, "actor_roster_hash": h, "policy_hash": h,
            "signature_algorithm_registry_hash": h,
        },
        "permit_hash_algorithm": "sha256(RFC8785-JCS-object-with-permit_hash-null)",
        "permit_hash": h,
    }
    zero_allowance = {
        "invocations": 0, "solver_launches": 0, "database_writes": 0, "redis_writes": 0,
        "d_volume_writes": 0, "human_gate_commits": 0, "active_release_changes": 0,
        "tokens": 0, "cost_microunits": 0, "currency": "USD",
    }
    reserved_allowance = dict(zero_allowance)
    reserved_allowance.update({"invocations": 1, "tokens": 100})
    receipt: dict[str, object] = {
        "schema_id": "seven/authorization-consumption-receipt",
        "schema_version": 1,
        "receipt_id": "consumption-receipt-1",
        "logical_consumption_id": "logical-consumption-1",
        "state_revision": 0,
        "previous_receipt_ref_and_hash_if_any": None,
        "parent_authorization_id": "authorization-1",
        "parent_authorization_ref_and_hash": ref("authorization-1"),
        "permit_id": "permit-1",
        "permit_ref_and_hash": ref("permit-1"),
        **{key: copy.deepcopy(value) for key, value in action_unit.items() if key != "unit_budget"},
        "aggregate_id": "authorization-scope-aggregate-1",
        "expected_aggregate_revision": 0,
        "fence_token": 1,
        "reservation_backend": "DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER",
        "status": "RESERVED",
        "reserved_at": "2026-08-14T00:00:03Z",
        "status_recorded_at": "2026-08-14T00:00:04Z",
        "terminal_at_if_any": None,
        "external_start_observation": "NOT_OBSERVED",
        "start_observation_evidence_refs": [],
        "proof_not_started_refs": [],
        "reservation_transaction_receipt_ref_and_hash": ref("reservation-transaction-1"),
        "reserved_unit_budget": reserved_allowance,
        "actual_side_effects": copy.deepcopy(zero_allowance),
        "held_allowance": copy.deepcopy(reserved_allowance),
        "released_allowance": copy.deepcopy(zero_allowance),
        "remaining_allowance": copy.deepcopy(zero_allowance),
        "recovery_decision_ref_and_hash_if_any": None,
        "externally_pinned_trust_root": {"object_id": "human-gate-root", "sha256": h},
        "service_attestation_key_registry_ref_and_hash": ref("service-attestation-keys"),
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "attestation_domain": "seven-authorization-consumption-receipt/v1\u0000",
        "attested_bytes_hash": h,
        "service_attestation": {
            "algorithm": "Ed25519", "key_id": "reservation-service-key", "service_principal_id": "reservation-service",
            "signature_encoding": "base64", "signature_b64": sig, "attested_bytes_hash": h,
            "trust_root_hash": h, "service_attestation_key_registry_hash": h,
        },
        "receipt_hash_algorithm": "sha256(RFC8785-JCS-object-with-receipt_hash-null)",
        "receipt_hash": h,
    }
    return authorization, permit, receipt


def verify_security_schema_vectors(errors: list[str]) -> tuple[int, int]:
    h = "0" * 64
    c = "0" * 40
    sig = "A" * 86 + "=="
    ref = lambda name: {"ref": name, "sha256": h}

    operator_registry = {
        "schema_id": "seven/operator-command-registry",
        "schema_version": 1,
        "registry_id": "negative-external-side-effect",
        "entries": [{
            "command_id": "model.run",
            "surface_bindings": ["seven model run"],
            "command_schema_ref_and_hash": ref("command-schema"),
            "application_service_and_method": "ModelService.run",
            "final_ports": ["ModelRolePort"],
            "effect_class": "EXTERNAL_SIDE_EFFECT",
            "authorization_contract": {
                "requires_external_execution_authorization": False,
                "requires_live_run_permit": False,
                "required_action_kind": None,
                "authorization_action_registry_entry_ref_and_hash": None,
                "requires_human_gate_decision": False,
            },
            "idempotency_and_fence_contract": {
                "request_id_required": True,
                "expected_input_hash_required": True,
                "expected_revision_or_fence_required": False,
                "reservation_and_dispatch_atomic": False,
                "duplicate_identical_behavior": "RETURN_EXISTING_RESULT",
                "duplicate_conflicting_behavior": "CONFLICT_OR_QUARANTINE",
                "unknown_start_behavior": "NOT_APPLICABLE",
            },
            "safety_semantics_if_any": None,
            "receipt_types": ["AI_INVOCATION_RECEIPT"],
            "allowed_exit_codes": [0, 3, 4],
            "introduced_in": "v1",
            "deprecated_in": None,
        }],
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "registry_hash_algorithm": "sha256(RFC8785-JCS-object-with-registry_hash-null)",
        "registry_hash": h,
    }
    if not schema_errors("operator-command-registry.v1.schema.json", operator_registry):
        errors.append("security-vector:external_side_effect_without_permit_was_accepted")

    live_plan = copy.deepcopy(load_json(PLAN_PATH))
    live_plan["wp_id"] = "WP-CW-D1"
    live_plan["execution_mode"] = "AUTHORIZED_LIVE_CANARY"
    live_plan["normative_review_record_ref_and_hash"] = ref("normative-review")
    live_plan["side_effect_budget"]["remote_model_calls"] = 1
    if not schema_errors("work-package-plan.v1.schema.json", live_plan):
        errors.append("security-vector:live_plan_without_authorization_chain_was_accepted")

    bundle = {
        "schema_id": "seven/implementation-completion-bundle", "schema_version": 1,
        "bundle_id": "bundle-1", "wp_id": "WP-CW0", "implementation_attempt_id": "attempt-1",
        "status": "READY_FOR_AUDIT", "baseline": {"commit": c, "tree": c},
        "implementation_subject": {"commit": c, "tree": c}, "spec_refs_and_hashes": [ref("spec")],
        "requirement_coverage": [{"requirement_id": "AUTH-001", "normative_clause_ids": ["NORM-x"], "code_refs": [], "schema_refs": [], "test_receipts": [ref("test")], "runtime_evidence_refs": [], "status": "COVERED"}],
        "modified_files": [], "schema_ids_and_hashes": [], "code_entrypoints": [], "state_transitions_implemented": [],
        "test_receipts": [ref("test")], "fault_injection_receipts": [], "capability_reports": [], "live_run_receipts": [], "artifact_refs": [],
        "external_side_effect_counts": {"database_connections": 0, "database_reads": 0, "database_writes": 0, "redis_connections": 0, "redis_reads": 0, "redis_writes": 0, "d_volume_writes": 0, "model_invocations_by_profile": {}, "solver_launches": 0, "human_gate_decisions": 0},
        "claims": [], "nonclaims": ["not audited"], "known_limitations": [], "protocol_deviations": [], "unresolved_findings": [], "inherited_audit_debt": [], "recovery_notes": [],
        "audit_replay_commands": [["python", "verify.py"]], "created_at": "2026-08-14T00:00:00Z", "creator": "implementer", "bundle_hash": h,
    }
    if schema_errors("implementation-completion-bundle.v1.schema.json", bundle):
        errors.append("security-vector:valid_implementation_bundle_rejected")
    ga1_bundle = copy.deepcopy(bundle)
    ga1_bundle["wp_id"] = "WP-GA1"
    if not schema_errors("implementation-completion-bundle.v1.schema.json", ga1_bundle):
        errors.append("security-vector:ga1_implementation_bundle_was_accepted")

    assignment = {
        "schema_id": "seven/audit-assignment", "schema_version": 1, "assignment_id": "assignment-1",
        "owner_actor_id": "owner", "owner_repo_external_channel": {"channel_id": "owner-channel", "channel_kind": "HUMAN_VERIFIED_OUT_OF_BAND", "observation_instructions_ref_and_hash": ref("instructions")},
        "externally_pinned_trust_root": {"object_id": "root", "sha256": h}, "actor_roster_ref_and_hash": ref("roster"),
        "human_gate_policy_ref_and_hash": ref("policy"), "signature_algorithm_registry_ref_and_hash": ref("algorithms"),
        "auditor_principal_id": "auditor", "auditor_attestation_public_key": {"key_id": "auditor-key", "algorithm": "Ed25519", "public_key_encoding": "raw-32-byte-base64", "public_key_b64": "A" * 43 + "=", "public_key_sha256": h},
        "target_work_package_id": "WP-DOC0", "subject_commit_and_tree": {"commit": c, "tree": c},
        "completion_bundle_ref_and_hash": ref("bundle"), "evidence_index_commit_if_any": None,
        "independence_and_separation_policy_ref_and_hash": ref("separation"), "allowed_audit_scope": {"allowed_audit_axes": ["implementation"], "allowed_audit_actions": ["READ_ARTIFACTS"], "allowed_external_side_effects": [], "requires_separate_external_execution_authorization": True},
        "required_audit_plan_and_spec_refs_and_hashes": [ref("audit-plan")], "issued_at": "2026-08-14T00:00:00Z", "not_before": "2026-08-14T00:00:01Z", "expires_at": "2026-08-15T00:00:00Z", "nonce": "nonce-0000000001",
        "canonicalizer_profile": "RFC8785_JCS_UTF8", "signature_domain": "seven-audit-assignment/v1\u0000", "signed_bytes_hash": h,
        "signature_envelope": {"algorithm": "Ed25519", "key_id": "owner-key", "signer_actor_id": "owner", "signature_encoding": "base64", "signature_b64": sig, "signed_bytes_hash": h, "trust_root_hash": h, "actor_roster_hash": h, "policy_hash": h, "signature_algorithm_registry_hash": h},
        "assignment_hash_algorithm": "sha256(RFC8785-JCS-object-with-assignment_hash-null)", "assignment_hash": h,
    }
    if schema_errors("audit-assignment.v1.schema.json", assignment) or audit_assignment_semantic_errors(assignment):
        errors.append("security-vector:valid_audit_assignment_rejected")
    malicious_assignment = copy.deepcopy(assignment)
    malicious_assignment["auditor_principal_id"] = "owner"
    if not audit_assignment_semantic_errors(malicious_assignment):
        errors.append("security-vector:self_assigned_auditor_was_accepted")

    record = {
        "schema_id": "seven/audit-record", "schema_version": 1, "audit_id": "audit-1", "wp_id": "WP-DOC0",
        "audit_assignment_ref_and_hash": ref("assignment"), "assignment_verification_receipt_ref_and_hash": ref("assignment-verification"),
        "audited_bundle_ref_and_hash": ref("bundle"), "audited_subject": {"commit": c, "tree": c}, "evidence_index_commit_if_any": None,
        "externally_observed_pinned_trust_root": {"trust_root_hash": h, "source_channel_id": "owner-channel", "observed_at": "2026-08-14T00:00:02Z", "observation_receipt_ref_and_hash": ref("root-observation")},
        "runtime_manifest_trust_root_hash": h, "audit_plan_and_spec_refs_and_hashes": [ref("audit-plan")],
        "auditor_principal_id": "auditor", "auditor_attestation_key_id": "auditor-key", "auditor_attestation_public_key_hash": h, "auditor_session_attestation_ref_and_hash": ref("session-attestation"),
        "independence_evidence": [ref("independence")], "findings": [], "replayed_test_receipts": [ref("test")], "external_execution_receipts": [],
        "traceability_remainder": 0, "orphan_remainder": 0, "claims_confirmed": [], "claims_rejected": [], "nonclaims_checked": ["not audited by implementer"],
        "axis_verdicts": {
            "implementation": {"verdict": "AUDITED_PASS", "finding_ids": [], "evidence_refs": [ref("test")], "scope_reason_if_not_tested": None},
            "factory": {"verdict": "NOT_TESTED", "finding_ids": [], "evidence_refs": [], "scope_reason_if_not_tested": "not in scope"},
            "scientific": {"verdict": "NOT_TESTED", "finding_ids": [], "evidence_refs": [], "scope_reason_if_not_tested": "not in scope"},
            "production_scale": {"verdict": "NOT_TESTED", "finding_ids": [], "evidence_refs": [], "scope_reason_if_not_tested": "not in scope"},
        },
        "scope_limits": ["implementation only"], "followups": [], "state_transition_effect": "NONE_UNTIL_HUMAN_GATE_SERVICE_ACCEPTS",
        "created_at": "2026-08-14T00:10:00Z", "canonicalizer_profile": "RFC8785_JCS_UTF8", "signature_domain": "seven-audit-record/v1\u0000", "signed_bytes_hash": h,
        "signature_envelope": {"algorithm": "Ed25519", "key_id": "auditor-key", "signer_principal_id": "auditor", "signature_encoding": "base64", "signature_b64": sig, "signed_bytes_hash": h},
        "audit_record_hash_algorithm": "sha256(RFC8785-JCS-object-with-audit_record_hash-null)", "audit_record_hash": h,
    }
    if schema_errors("audit-record.v1.schema.json", record) or audit_record_semantic_errors(record, assignment):
        errors.append("security-vector:valid_audit_record_rejected")
    wrong_record = copy.deepcopy(record)
    wrong_record["auditor_principal_id"] = "implementer"
    if not audit_record_semantic_errors(wrong_record, assignment):
        errors.append("security-vector:wrong_auditor_record_was_accepted")

    wrong_key = copy.deepcopy(record)
    wrong_key["auditor_attestation_key_id"] = "different-key"
    if not audit_record_semantic_errors(wrong_key, assignment):
        errors.append("audit-vector:wrong_attestation_key_was_accepted")

    wrong_specs = copy.deepcopy(record)
    wrong_specs["audit_plan_and_spec_refs_and_hashes"] = [ref("different-plan")]
    if not audit_record_semantic_errors(wrong_specs, assignment):
        errors.append("audit-vector:assignment_plan_scope_mismatch_was_accepted")

    out_of_scope = copy.deepcopy(record)
    out_of_scope["axis_verdicts"]["factory"] = {
        "verdict": "AUDITED_PASS", "finding_ids": [], "evidence_refs": [ref("factory")], "scope_reason_if_not_tested": None,
    }
    if not audit_record_semantic_errors(out_of_scope, assignment):
        errors.append("audit-vector:out_of_scope_axis_pass_was_accepted")

    open_p0 = copy.deepcopy(record)
    open_p0["findings"] = [{
        "finding_id": "F-P0", "finding_kind": "SECURITY", "severity": "P0", "status": "OPEN",
        "affected_axes": ["implementation"], "requirement_ids": ["AUTH-001"],
        "summary": "unresolved blocker", "evidence_refs": [ref("p0")],
    }]
    open_p0["axis_verdicts"]["implementation"]["finding_ids"] = ["F-P0"]
    if not audit_record_semantic_errors(open_p0, assignment):
        errors.append("audit-vector:open_p0_with_pass_was_accepted")

    missing_closure = copy.deepcopy(record)
    missing_closure["findings"] = [{
        "finding_id": "F-P1", "finding_kind": "TRACEABILITY", "severity": "P1", "status": "OPEN",
        "affected_axes": ["implementation"], "requirement_ids": ["AUTH-001"],
        "summary": "missing axis link", "evidence_refs": [ref("p1")],
    }]
    if not audit_record_semantic_errors(missing_closure, assignment):
        errors.append("audit-vector:missing_finding_axis_closure_was_accepted")

    not_tested_with_evidence = copy.deepcopy(record)
    not_tested_with_evidence["axis_verdicts"]["scientific"]["evidence_refs"] = [ref("science")]
    if not audit_record_semantic_errors(not_tested_with_evidence, assignment):
        errors.append("audit-vector:not_tested_axis_with_evidence_was_accepted")

    invalid_time = copy.deepcopy(record)
    invalid_time["created_at"] = "2026-08-14T00:10:00+00:00"
    if not audit_record_semantic_errors(invalid_time, assignment):
        errors.append("audit-vector:noncanonical_record_timestamp_was_accepted")

    vault = valid_vault_access_capability_fixture()
    if schema_errors("vault-access-capability.v1.schema.json", vault) or vault_access_capability_semantic_errors(vault):
        errors.append("security-vector:valid_target_solver_vault_capability_rejected")

    solver_without_contract = copy.deepcopy(vault)
    solver_without_contract["principal"]["target_solver_contract_sha256"] = None
    if not schema_errors("vault-access-capability.v1.schema.json", solver_without_contract):
        errors.append("security-vector:target_solver_without_contract_was_accepted")

    solver_reads_solution = copy.deepcopy(vault)
    solver_reads_solution["object_binding"]["sensitivity"] = "SOLUTION_BEARING"
    if not schema_errors("vault-access-capability.v1.schema.json", solver_reads_solution):
        errors.append("security-vector:target_solver_solution_access_was_accepted")

    vault_signature_drift = copy.deepcopy(vault)
    vault_signature_drift["signature_envelope"]["signed_bytes_hash"] = "f" * 64
    if not vault_access_capability_semantic_errors(vault_signature_drift):
        errors.append("security-vector:vault_signature_cross_binding_drift_was_accepted")

    derivation = valid_view_derivation_fixture(vault)
    if schema_errors("view-derivation.v1.schema.json", derivation):
        errors.append("security-vector:valid_view_derivation_rejected")

    view_substitution = copy.deepcopy(derivation)
    view_substitution["model_delivery"]["delivered_view_sha256"] = "f" * 64
    if not schema_errors("view-derivation.v1.schema.json", view_substitution):
        errors.append("security-vector:view_substitution_field_was_accepted")

    authorization, permit, consumption = valid_authorization_chain_fixtures()
    if schema_errors("external-execution-authorization.v1.schema.json", authorization) or external_execution_authorization_semantic_errors(authorization):
        errors.append("security-vector:valid_external_execution_authorization_rejected")

    authorization_signature_drift = copy.deepcopy(authorization)
    authorization_signature_drift["signature_envelope"]["policy_hash"] = "f" * 64
    if not external_execution_authorization_semantic_errors(authorization_signature_drift):
        errors.append("security-vector:authorization_signature_cross_binding_drift_was_accepted")

    duplicate_scope = copy.deepcopy(authorization)
    second_scope = copy.deepcopy(duplicate_scope["action_scopes"][0])
    second_scope["scope_hash"] = "f" * 64
    second_scope["action_kind"] = "TARGET_SOLVER_LAUNCH"
    duplicate_scope["action_scopes"].append(second_scope)
    if not external_execution_authorization_semantic_errors(duplicate_scope):
        errors.append("security-vector:duplicate_authorization_scope_id_was_accepted")

    if schema_errors("live-run-permit.v1.schema.json", permit) or live_run_permit_semantic_errors(permit, authorization):
        errors.append("security-vector:valid_live_run_permit_rejected")

    permit_escalation = copy.deepcopy(permit)
    permit_escalation["action_units"][0]["unit_budget"]["max_tokens"] = 101
    if not live_run_permit_semantic_errors(permit_escalation, authorization):
        errors.append("security-vector:permit_budget_escalation_was_accepted")

    duplicate_ordinal = copy.deepcopy(permit)
    second_unit = copy.deepcopy(duplicate_ordinal["action_units"][0])
    second_unit["job_id"] = "job-2"
    second_unit["attempt_id"] = "attempt-2"
    second_unit["idempotency_key"] = "idempotency-key-0002"
    duplicate_ordinal["action_units"].append(second_unit)
    if not live_run_permit_semantic_errors(duplicate_ordinal, authorization):
        errors.append("security-vector:duplicate_permit_ordinal_was_accepted")

    if schema_errors("authorization-consumption-receipt.v1.schema.json", consumption) or authorization_consumption_receipt_semantic_errors(consumption, permit, authorization):
        errors.append("security-vector:valid_authorization_consumption_receipt_rejected")

    reserved_with_side_effect = copy.deepcopy(consumption)
    reserved_with_side_effect["actual_side_effects"]["invocations"] = 1
    if not schema_errors("authorization-consumption-receipt.v1.schema.json", reserved_with_side_effect):
        errors.append("security-vector:reserved_receipt_with_side_effect_was_accepted")

    unknown_without_hold = copy.deepcopy(consumption)
    unknown_without_hold["status"] = "UNKNOWN_START_HELD"
    unknown_without_hold["external_start_observation"] = "UNKNOWN"
    unknown_without_hold["start_observation_evidence_refs"] = [ref("unknown-start")]
    unknown_without_hold["held_allowance"] = copy.deepcopy(unknown_without_hold["actual_side_effects"])
    unknown_without_hold["recovery_decision_ref_and_hash_if_any"] = ref("recovery-decision")
    if not schema_errors("authorization-consumption-receipt.v1.schema.json", unknown_without_hold):
        errors.append("security-vector:unknown_start_without_held_allowance_was_accepted")

    allowance_drift = copy.deepcopy(consumption)
    allowance_drift["held_allowance"]["tokens"] = 99
    if not authorization_consumption_receipt_semantic_errors(allowance_drift, permit, authorization):
        errors.append("security-vector:allowance_conservation_drift_was_accepted")

    receipt_binding_drift = copy.deepcopy(consumption)
    receipt_binding_drift["attempt_id"] = "different-attempt"
    if not authorization_consumption_receipt_semantic_errors(receipt_binding_drift, permit, authorization):
        errors.append("security-vector:receipt_action_unit_binding_drift_was_accepted")

    receipt_attestation_drift = copy.deepcopy(consumption)
    receipt_attestation_drift["service_attestation"]["trust_root_hash"] = "f" * 64
    if not authorization_consumption_receipt_semantic_errors(receipt_attestation_drift, permit, authorization):
        errors.append("security-vector:receipt_attestation_cross_binding_drift_was_accepted")
    return 26, 7


def valid_doc0_test_receipt(plan: dict[str, object], index: dict[str, object]) -> dict[str, object]:
    h = "0" * 64
    c = "0" * 40
    test_ids = list(map(str, plan["test_plan_ids"]))
    receipt: dict[str, object] = {
        "schema_id": "seven/docs/doc0-test-execution-receipt",
        "schema_version": 1,
        "receipt_id": "doc0-test-vector-valid",
        "wp_id": "WP-DOC0",
        "implementation_subject": {"commit": c, "tree": c, "working_tree_clean_before_tests": True, "source_relation": "COMMITTED_TREE"},
        "checked_source_set_sha256": index["source_set_sha256"],
        "normative_index_ref_and_hash": ref_hash(INDEX_PATH),
        "work_package_plan_ref_and_hash": ref_hash(PLAN_PATH),
        "dependency_lock_ref_and_hash": ref_hash(IMPL / "requirements-docs.txt"),
        "schema_and_spec_refs_and_hashes": expected_spec_refs(index) + expected_schema_refs(),
        "commands": [{
            "command_id": "all-doc0-tests",
            "test_ids": test_ids,
            "exact_argv": ["python3", "tools/verify_doc_contracts.py"],
            "cwd": str(IMPL),
            "isolated_environment_summary": "frozen offline documentation verifier fixture",
            "started_at": "2026-08-14T00:00:00Z",
            "completed_at": "2026-08-14T00:00:01Z",
            "exit_code": 0,
            "stdout_ref_and_hash": {"ref": "stdout", "sha256": h},
            "stderr_ref_and_hash": {"ref": "stderr", "sha256": h},
            "artifact_refs_and_hashes": [],
            "test_summary": {"discovered": len(test_ids), "executed": len(test_ids), "passed": len(test_ids), "failed": 0, "skipped": 0, "errors": 0},
            "verdict": "PASS",
        }],
        "aggregate_verdict": "PASS",
        "side_effect_counts": {"db_connections": 0, "db_writes": 0, "redis_connections": 0, "remote_model_calls": 0, "target_solver_launches": 0, "d_volume_writes": 0},
        "explicit_nonclaims": ["Schema fixture only; not an executed test receipt"],
        "created_at": "2026-08-14T00:00:01Z",
        "creator": "verify_doc_contracts.py fixture",
        "receipt_hash_algorithm": "sha256(canonical-json-with-receipt_hash-null)",
        "receipt_hash": h,
    }
    receipt["receipt_hash"] = self_hash(receipt, "receipt_hash")
    return receipt


def verify_receipt_schema_vectors(errors: list[str], plan: dict[str, object], index: dict[str, object]) -> tuple[int, int]:
    valid = valid_doc0_test_receipt(plan, index)
    if schema_errors("doc0-test-execution-receipt.v1.schema.json", valid) or doc0_test_receipt_semantic_errors(valid, plan, index):
        errors.append("receipt-vector:valid_doc0_test_receipt_rejected")

    failed_command_pass = copy.deepcopy(valid)
    command = failed_command_pass["commands"][0]
    command["exit_code"] = 1
    command["verdict"] = "FAIL"
    command["test_summary"] = {"discovered": 0, "executed": 0, "passed": 0, "failed": 0, "skipped": 0, "errors": 0}
    failed_command_pass["receipt_hash"] = self_hash(failed_command_pass, "receipt_hash")
    if not schema_errors("doc0-test-execution-receipt.v1.schema.json", failed_command_pass):
        errors.append("receipt-vector:aggregate_pass_over_failed_zero_test_command_schema_accepted")

    arithmetic = copy.deepcopy(valid)
    arithmetic["commands"][0]["test_summary"]["discovered"] += 1
    arithmetic["receipt_hash"] = self_hash(arithmetic, "receipt_hash")
    if not doc0_test_receipt_semantic_errors(arithmetic, plan, index):
        errors.append("receipt-vector:invalid_test_count_arithmetic_accepted")

    missing_test_id = copy.deepcopy(valid)
    missing_test_id["commands"][0]["test_ids"] = missing_test_id["commands"][0]["test_ids"][:-1]
    missing_test_id["receipt_hash"] = self_hash(missing_test_id, "receipt_hash")
    if not doc0_test_receipt_semantic_errors(missing_test_id, plan, index):
        errors.append("receipt-vector:missing_plan_test_id_accepted")

    reverse_time = copy.deepcopy(valid)
    reverse_time["commands"][0]["completed_at"] = "2026-08-13T23:59:59Z"
    reverse_time["receipt_hash"] = self_hash(reverse_time, "receipt_hash")
    if not doc0_test_receipt_semantic_errors(reverse_time, plan, index):
        errors.append("receipt-vector:reverse_command_time_accepted")

    wrong_source = copy.deepcopy(valid)
    wrong_source["checked_source_set_sha256"] = "f" * 64
    wrong_source["receipt_hash"] = self_hash(wrong_source, "receipt_hash")
    if not doc0_test_receipt_semantic_errors(wrong_source, plan, index):
        errors.append("receipt-vector:wrong_source_set_accepted")

    bad_self_hash = copy.deepcopy(valid)
    bad_self_hash["receipt_hash"] = "f" * 64
    if not doc0_test_receipt_semantic_errors(bad_self_hash, plan, index):
        errors.append("receipt-vector:bad_self_hash_accepted")

    invalid_timestamps = (
        "2026-08-14 00:00:00Z",
        "2026-08-14T00:00:00+00:00",
        "2026-02-29T00:00:00Z",
        "2026-08-14T00:00:00.1234567890Z",
        "2026-08-14T00:00:00z",
    )
    for value in invalid_timestamps:
        bad_time = copy.deepcopy(valid)
        bad_time["commands"][0]["started_at"] = value
        bad_time["receipt_hash"] = self_hash(bad_time, "receipt_hash")
        if not schema_errors("doc0-test-execution-receipt.v1.schema.json", bad_time):
            errors.append(f"rfc3339-vector:schema_accepted:{value}")
        if not doc0_test_receipt_semantic_errors(bad_time, plan, index):
            errors.append(f"rfc3339-vector:semantic_parser_accepted:{value}")
    return 6, len(invalid_timestamps)


def verify_overclaim_boundary(errors: list[str]) -> None:
    status = (DOCS / "implementation-status.md").read_text()
    board = BOARD_PATH.read_text()
    if "WP-DOC0 IN_PROGRESS" not in status:
        errors.append("overclaim:implementation_status_does_not_keep_doc0_in_progress")
    if "| WP-DOC0 | `IN_PROGRESS` |" not in board:
        errors.append("overclaim:board_does_not_keep_doc0_in_progress")


def build_doc_contract_receipt(
    errors: list[str],
    counts: dict[str, int],
    index: dict[str, object],
    started_at: str,
) -> dict[str, object]:
    completed_at = canonical_utc_now()
    verdict = "PASS" if not errors else "FAIL"
    receipt: dict[str, object] = {
        "schema_id": "seven/docs/doc-contract-verification-receipt",
        "schema_version": 1,
        "receipt_id": f"doc-contract-{str(index['source_set_sha256'])[:16]}-{completed_at}",
        "implementation_subject": current_implementation_subject(),
        "checked_source_set_sha256": index["source_set_sha256"],
        "normative_index_ref_and_hash": ref_hash(INDEX_PATH),
        "canonical_dag_ref_and_hash": ref_hash(DAG_PATH),
        "work_package_plan_ref_and_hash": ref_hash(PLAN_PATH),
        "migration_map_ref_and_hash": ref_hash(IMPL / "normative-requirement-migrations.v1.json"),
        "spec_refs_and_hashes": expected_spec_refs(index),
        "schema_refs_and_hashes": expected_schema_refs(),
        "checker_ref_and_hash": ref_hash(Path(__file__)),
        "dependency_lock_ref_and_hash": ref_hash(IMPL / "requirements-docs.txt"),
        "exact_argv": [sys.executable, *sys.argv],
        "cwd": str(Path.cwd().resolve()),
        "verification_ids": list(DOC0_VERIFICATION_IDS),
        "started_at": started_at,
        "completed_at": completed_at,
        "environment": {
            "python": sys.version.split()[0],
            "jsonschema": importlib.metadata.version("jsonschema"),
            "platform": platform.platform(),
        },
        "counts": counts,
        "output_binding": {
            "hash_algorithm": "sha256(canonical-json-of-verdict-counts-errors)",
            "sha256": canonical_json_sha256({"verdict": verdict, "counts": counts, "errors": errors}),
        },
        "verdict": verdict,
        "explicit_nonclaims": [
            "PASS does not implement runtime code",
            "PASS does not constitute independent semantic review",
            "PASS does not grant AUDITED_PASS",
            "A working-tree snapshot PASS is not a committed-subject test receipt",
        ],
        "errors": list(errors),
        "creator": "tools/verify_doc_contracts.py",
        "receipt_hash_algorithm": "sha256(canonical-json-with-receipt_hash-null)",
        "receipt_hash": "0" * 64,
    }
    receipt["receipt_hash"] = self_hash(receipt, "receipt_hash")
    return receipt


def verify_doc_contract_receipt_vectors(
    valid: dict[str, object],
    expected_counts: dict[str, int],
    index: dict[str, object],
    errors: list[str],
) -> int:
    fabricated_counts = copy.deepcopy(valid)
    fabricated_counts["counts"]["work_packages"] = 1
    fabricated_counts["output_binding"]["sha256"] = canonical_json_sha256({
        "verdict": fabricated_counts["verdict"],
        "counts": fabricated_counts["counts"],
        "errors": fabricated_counts["errors"],
    })
    fabricated_counts["receipt_hash"] = self_hash(fabricated_counts, "receipt_hash")
    if not doc_contract_receipt_semantic_errors(fabricated_counts, expected_counts, index):
        errors.append("receipt-vector:fabricated_doc_contract_counts_were_accepted")

    fabricated_source = copy.deepcopy(valid)
    fabricated_source["checked_source_set_sha256"] = "f" * 64
    fabricated_source["receipt_hash"] = self_hash(fabricated_source, "receipt_hash")
    if not doc_contract_receipt_semantic_errors(fabricated_source, expected_counts, index):
        errors.append("receipt-vector:fabricated_doc_contract_source_was_accepted")
    return 2


def main() -> int:
    started_at = canonical_utc_now()
    errors: list[str] = []
    schema_count = verify_all_schema_contracts(errors)
    validate_instance(DAG_PATH, IMPL / "work-package-dag.v1.schema.json", errors)
    dag = load_json(DAG_PATH)
    nodes = dag["work_packages"]
    ids = {item["wp_id"] for item in nodes}
    development = edge_set(nodes, "development_dependencies", errors)
    activation = edge_set(nodes, "activation_dependencies", errors)
    assert_acyclic(ids, development, "development", errors)
    assert_acyclic(ids, activation, "activation", errors)
    board = parse_board(errors)
    if set(board) != ids:
        errors.append(f"board:wp_set_mismatch:missing={sorted(ids-set(board))}:extra={sorted(set(board)-ids)}")
    for item in nodes:
        wp_id = item["wp_id"]
        if wp_id in board:
            expected_pair = (set(item["development_dependencies"]), set(item["activation_dependencies"]))
            if board[wp_id] != expected_pair:
                errors.append(f"board:dependency_mismatch:{wp_id}:{board[wp_id]}:{expected_pair}")
    mermaid = parse_mermaid(errors)
    if mermaid != development:
        errors.append(f"mermaid:development_projection_mismatch:missing={sorted(development-mermaid)}:extra={sorted(mermaid-development)}")
    dag_hash = sha256(DAG_PATH)
    validate_instance(IMPL / "normative-requirement-migrations.v1.json", IMPL / "normative-requirement-migrations.v1.schema.json", errors)
    validate_instance(IMPL / "analysis-golden-vectors.v1.json", IMPL / "analysis-golden-vectors.v1.schema.json", errors)
    index, clauses, pending_reviews = verify_normative_index(errors)
    planned_clauses, missing_planned_clauses, extra_planned_clauses = verify_plan(dag_hash, index, errors)
    plan = load_json(PLAN_PATH)
    security_vectors, audit_vectors = verify_security_schema_vectors(errors)
    receipt_vectors, rfc3339_vectors = verify_receipt_schema_vectors(errors, plan, index)
    verify_overclaim_boundary(errors)
    markdown_files, links = verify_links_and_fences(errors)
    counts = {
        "work_packages": len(ids),
        "development_edges": len(development),
        "activation_edges": len(activation),
        "schema_files": schema_count,
        "security_schema_vectors": security_vectors,
        "receipt_schema_vectors": receipt_vectors + 2,
        "audit_record_semantic_vectors": audit_vectors,
        "rfc3339_negative_vectors": rfc3339_vectors,
        "markdown_files": markdown_files,
        "relative_links": links,
        "normative_clauses": clauses,
        "planned_normative_clauses": planned_clauses,
        "plan_missing_normative_clauses": missing_planned_clauses,
        "plan_extra_normative_clauses": extra_planned_clauses,
        "pending_independent_semantic_reviews": pending_reviews,
    }
    provisional = build_doc_contract_receipt(errors, counts, index, started_at)
    verify_doc_contract_receipt_vectors(provisional, counts, index, errors)
    result = build_doc_contract_receipt(errors, counts, index, started_at)
    receipt_findings = schema_errors("doc-contract-verification-receipt.v1.schema.json", result)
    semantic_receipt_findings = doc_contract_receipt_semantic_errors(result, counts, index)
    if receipt_findings or semantic_receipt_findings:
        errors.extend(
            f"receipt-schema:{'/'.join(map(str, finding.path))}:{finding.message}"
            for finding in receipt_findings
        )
        errors.extend(f"receipt-semantic:{finding}" for finding in semantic_receipt_findings)
        result = build_doc_contract_receipt(errors, counts, index, started_at)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
