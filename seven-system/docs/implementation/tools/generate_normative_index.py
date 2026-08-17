#!/usr/bin/env python3
"""Generate and migration-check Seven's documentation requirement index."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
IMPLEMENTATION_DIR = HERE.parent
DOCS_DIR = IMPLEMENTATION_DIR.parent
SEVEN_ROOT = DOCS_DIR.parent
WORKSPACE_ROOT = SEVEN_ROOT.parent
OUTPUT = IMPLEMENTATION_DIR / "normative-requirement-index.v1.json"
MIGRATIONS = IMPLEMENTATION_DIR / "normative-requirement-migrations.v1.json"
GENERATOR_CONTRACT_VERSION = 3

NORMATIVE_TOKENS = (
    "必须", "不得", "禁止", "只能", "一律", "不能", "不可", "只允许",
    "应当", "应该", "不要", "需要", "要求", "允许", "可以",
    "应", "MUST", "must", "SHALL", "shall", "SHOULD", "should", "MAY", "may",
)
EXPLICIT_NORMATIVE_RE = re.compile("|".join(re.escape(token) for token in NORMATIVE_TOKENS if token != "应"))
# 单字“应”只有在它表现为中文规范助动词时才算机器边界；常见复合词的
# 末字（对应/响应/效应/相应/适应/供应/反应）必须排除。独立语义复核仍
# 是最终裁决者，机器命中不能把含混文本升级成已审条款。
SINGLE_YING_NORMATIVE_RE = re.compile(r"(?<![对响效相适供反])应(?=[\u4e00-\u9fff])")
# This exact declarative sentence was independently adjudicated as a normative
# audit-debt hand-off rule. Keep the inclusion narrow: this is not permission
# to index arbitrary descriptive prose that lacks a normative modal.
ADJUDICATED_NORMATIVE_RE = re.compile(r"^\d+\.\s*未解决审计债随最终SystemCompletionBundle交给独立审计者。$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
NON_WORD_RE = re.compile(r"[^\w\u4e00-\u9fff]+", re.UNICODE)

# Only strong semantic matches receive an exact cross-document requirement ID.
# Every other line is explicit LOCAL_ONLY; no per-file default can manufacture
# a zero classification remainder.
REQUIREMENT_RULES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("AUTH-001", re.compile(r"实施者.*AUDITED|自签|审计者.*PASS", re.I)),
    ("AUTH-002", re.compile(r"目标规范.*当前事实|当前事实.*目标规范|DESIGN_FROZEN.*NOT_IMPLEMENTED|不能.*冒充.*实现", re.I)),
    ("AUTH-003", re.compile(r"development depend|activation depend|READY_FOR_AUDIT.*开发|激活动作", re.I)),
    ("AUTH-004", re.compile(r"ExternalExecutionAuthorization|LiveRunPermit|外部副作用.*授权|permit.*预留", re.I)),
    ("PORT-001", re.compile(r"Target.?Solver.*solver_harness|DevinSolverAdapter.*harness|Solver.*只能经", re.I)),
    ("PORT-002", re.compile(r"Devin.*认知|DevinCliModelRoleAdapter|Devin.*全部机器角色", re.I)),
    ("PORT-003", re.compile(r"ModelRole.*Codex.*Devin|Codex.*Devin.*并列|统一ModelRole", re.I)),
    ("PORT-004", re.compile(r"Devin.*workspace|两个Devin|Solver.*认知.*隔离|session.*不能共享", re.I)),
    ("PORT-005", re.compile(r"阶段代码.*调用|phase.*subprocess|旁路.*provider|只提交冻结job", re.I)),
    ("PROFILE-001", re.compile(r"glm-5-2|GLM-5\.2 High|effort.*UID", re.I)),
    ("PROFILE-002", re.compile(r"RoleQualificationMatrix|每个角色.*profile|逐格.*资格|qualified.*cell", re.I)),
    ("PROFILE-003", re.compile(r"fallback|跨载体.*重跑|自动转(?:Devin|Codex)", re.I)),
    ("PROFILE-004", re.compile(r"requested.*effective|effective.*receipt|UNOBSERVABLE", re.I)),
    ("DATA-001", re.compile(r"D盘.*CAS|答案.*Vault|大对象.*D盘", re.I)),
    ("DATA-002", re.compile(r"sealed.*不可|final bundle.*改|覆盖.*artifact", re.I)),
    ("DATA-003", re.compile(r"Arango.*小|数据库.*元数据|不存.*正文", re.I)),
    ("DATA-004", re.compile(r"Redis.*投影|Redis.*重建", re.I)),
    ("DATA-005", re.compile(r"CAS.*DB.*reconcile|两阶段提交|单边提交", re.I)),
    ("DATA-006", re.compile(r"CommitIntent|CAS补DB|artifact sealed.*DB", re.I)),
    ("VLT-001", re.compile(r"Vault.*ACL|Vault.*view|Vault.*seal|越权.*Vault", re.I)),
    ("VLT-002", re.compile(r"solution-bearing|可能复述解答|request.*event.*output.*Vault", re.I)),
    ("DB-001", re.compile(r"错误DB|默认DB|ARANGO_DB|数据库身份", re.I)),
    ("DB-002", re.compile(r"StrictDatabasePort|raw client|ArangoClient.*backend", re.I)),
    ("DB-003", re.compile(r"DDL.*plan|Schema.*apply|迁移.*人门|migration.*fence", re.I)),
    ("DB-004", re.compile(r"SchemaBootstrap|bootstrap ledger|集合尚不存在", re.I)),
    ("DB-005", re.compile(r"DatabaseSchemaStateReport|DatabaseRuntimeCapabilityReport|ArtifactCommitReconcile", re.I)),
    ("DB-006", re.compile(r"ObjectPersistenceMapping|IndexAdequacy|collection.*owner.*retention", re.I)),
    ("SEC-001", re.compile(r"最小view|永久不能看到|只见statement|角色.*可见", re.I)),
    ("SEC-002", re.compile(r"solution-bearing|敏感.*sink|答案.*普通日志", re.I)),
    ("SEC-003", re.compile(r"三审|Process.*Proof.*Leakage|ProcessAudit|ProofJudgment|LeakageAudit", re.I)),
    ("HG-001", re.compile(r"ModelRole.*HumanGate|模型.*自批|不能签Gate", re.I)),
    ("HG-002", re.compile(r"Gate.*payload hash|payload.*签名|职责分离|separation.*Gate|quorum|actor.*role", re.I)),
    ("HG-003", re.compile(r"超时.*PASS|timeout.*PASS", re.I)),
    ("HG-004", re.compile(r"Ed25519|信任根|canonical签名|replay.*Gate|key.*撤销", re.I)),
    ("HG-005", re.compile(r"HUMAN_PENDING|HumanTask.*状态|人工.*等待态", re.I)),
    ("RUN-001", re.compile(r"at-least-once|idempotent fenced|重复投递|stale fence", re.I)),
    ("RUN-002", re.compile(r"unknown.start|开始状态未知|接受.*未知|不得盲重", re.I)),
    ("RUN-003", re.compile(r"retry.*科学样本|重复.*独立样本|attempt.*样本", re.I)),
    ("RUN-004", re.compile(r"carrier-global|resource pool|资源池|限流", re.I)),
    ("RUN-005", re.compile(r"停止.*dispatch|stop.*role.*Solver|停止领取", re.I)),
    ("CASE-001", re.compile(r"P2A.*P2B.*P3N.*P3C|自然题.*P3N", re.I)),
    ("CASE-002", re.compile(r"P3A.*P3B.*P3C|生成题.*P3B", re.I)),
    ("CASE-003", re.compile(r"题面.*变化.*失效|statement.*变化.*失效", re.I)),
    ("CASE-004", re.compile(r"retry.*Devin fails|生成直到失败|出题.*直到", re.I)),
    ("CASE-005", re.compile(r"calibration.*qualification|calibration.*confirmation|AuthoringEvaluationPack", re.I)),
    ("TELL-001", re.compile(r"TaxonomySnapshot|TellManifestation|TellHintRelation|Tell.*Hint.*M:N", re.I)),
    ("TELL-002", re.compile(r"Selector.*Renderer|组件.*归责|Core.*renderer", re.I)),
    ("TELL-003", re.compile(r"TellStrategyRelease.*payload|guided payload.*冻结", re.I)),
    ("SOLVER-001", re.compile(r"无工具|NoTool|tool call.*invalid|trajectory.*fail-closed", re.I)),
    ("SOLVER-002", re.compile(r"P2B.*P3B.*P5|admission.*不是P5|problem-only.*准入", re.I)),
    ("EXP-001", re.compile(r"P4.*冻结|ExperimentPlan.*sealed|preregister", re.I)),
    ("EXP-002", re.compile(r"fresh restart.*baseline|等资源.*problem-only", re.I)),
    ("EXP-003", re.compile(r"token.limit.*分层|token-limit.*分层", re.I)),
    ("AUD-001", re.compile(r"三审.*seal.*RunAudit|分别seal.*组装", re.I)),
    ("AUD-002", re.compile(r"Judge.*分歧|Aggregator.*自选|JUDGE_DISAGREEMENT", re.I)),
    ("EVID-001", re.compile(r"single episode|单episode|RunAudit.*因果", re.I)),
    ("EVID-002", re.compile(r"randomized contrast|预注册contrast.*Evidence|因果Evidence", re.I)),
    ("EVID-003", re.compile(r"missingness|multiplicity|估计器|stopping.*P4|cluster.*统计", re.I)),
    ("EVID-004", re.compile(r"EvidenceStatusRegistry|自由.*supports|机械派生", re.I)),
    ("REV-001", re.compile(r"NO_CHANGE", re.I)),
    ("REV-002", re.compile(r"fit.*regression.*prospective|证据分区", re.I)),
    ("REV-003", re.compile(r"one-shot|一次性.*holdout|看过.*消耗", re.I)),
    ("TEST-001", re.compile(r"blocker.*平均|negative tests.*先|blocker test", re.I)),
    ("TEST-002", re.compile(r"test receipt|测试收据|完整test IDs", re.I)),
    ("TEST-003", re.compile(r"故障注入|fault injection", re.I)),
    ("CLI-001", re.compile(r"CLI.*API.*业务层|幂等.*CLI|目标命令面", re.I)),
    ("CLI-002", re.compile(r"NOT_IMPLEMENTED.*fail-closed|退出码|副作用前.*BLOCK", re.I)),
    ("DONE-000", re.compile(r"CompletionBundle.*commit|自引用|implementation subject", re.I)),
    ("DONE-001", re.compile(r"Golden.?slice|自然.*生成.*P4|P4.P9.*双入口", re.I)),
    ("DONE-002", re.compile(r"remainder=0|orphan.*0|Evidence replay", re.I)),
    ("DONE-003", re.compile(r"Production.*soak|生产规模|PRODUCTION_SCALE", re.I)),
    ("EPOCH-001", re.compile(r"Epoch.*冻结|运行中.*漂移.*新建Epoch", re.I)),
    ("EPOCH-002", re.compile(r"CoverageTensor|Active Learning|跨Epoch.*重复", re.I)),
    ("EPOCH-003", re.compile(r"GlobalBudget|多Epoch|长期学习Verdict|跨Epoch预算", re.I)),
    ("INPUT-001", re.compile(r"CandidateManifest|producer bundle|生产.*写回|只读.*导入|source.*冻结", re.I)),
    ("COST-001", re.compile(r"usage.*cost|成本.*完整|cache_write_tokens|父子.*对账|budget.*enforcement", re.I)),
)

REQUIREMENT_TABLE_RE = re.compile(r"^\|\s*([A-Z]+-[0-9]{3})\s*\|.*?\|.*?\|\s*(.*?)\s*\|.*?\|$")
WP_TOKEN_RE = re.compile(r"WP-[A-Z0-9-]+")
LOCAL_ONLY_TEMPORARY_CONSUMER = "WP-DOC0"
LOCAL_ONLY_CONSUMER_BASIS = "DOC0_TEMPORARY_PENDING_INDEPENDENT_SEMANTIC_REVIEW"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def anchor_for(title: str) -> str:
    cleaned = title.replace("`", "").strip().lower()
    return NON_WORD_RE.sub("-", cleaned).strip("-") or "section"


def has_normative_token(text: str) -> bool:
    return bool(
        EXPLICIT_NORMATIVE_RE.search(text)
        or SINGLE_YING_NORMATIVE_RE.search(text)
        or ADJUDICATED_NORMATIVE_RE.search(text.strip())
    )


def source_specs() -> list[tuple[Path, str, str | None]]:
    specs: list[tuple[Path, str, str | None]] = []
    for path in IMPLEMENTATION_DIR.glob("*.md"):
        specs.append((path, path.relative_to(DOCS_DIR).as_posix(), None))
    for directory in (DOCS_DIR / "audit", DOCS_DIR / "decisions"):
        for path in directory.glob("*.md"):
            specs.append((path, path.relative_to(DOCS_DIR).as_posix(), None))
    specs.append((SEVEN_ROOT / "AGENTS.md", "../AGENTS.md", None))
    specs.append((WORKSPACE_ROOT / "AGENTS.md", "../../AGENTS.md", "### Seven System · 非特化证据工厂运行入口（2026-08-13起）"))
    return sorted(specs, key=lambda item: item[1])


def scoped_lines(path: Path, start_heading: str | None) -> tuple[list[tuple[int, str]], str]:
    lines = path.read_text().splitlines()
    if start_heading is None:
        return list(enumerate(lines, start=1)), "FULL_FILE"
    start = next((i for i, line in enumerate(lines) if line.strip() == start_heading), None)
    if start is None:
        raise RuntimeError(f"missing required scope heading in {path}: {start_heading}")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].strip() == "---"), len(lines))
    return [(i + 1, lines[i]) for i in range(start, end)], f"HEADING_SLICE:{start_heading}"


def classify(text: str) -> tuple[list[str], list[str], str | None]:
    requirement_ids = sorted({requirement_id for requirement_id, pattern in REQUIREMENT_RULES if pattern.search(text)})
    family_codes = sorted({requirement_id.split("-", 1)[0] for requirement_id in requirement_ids})
    if requirement_ids:
        return requirement_ids, family_codes, None
    return [], [], "专题文档内的局部规定性条款；须由未来审计者按source anchor复核，不自动冒充跨文档需求族。"


def load_requirement_catalog() -> tuple[dict[str, list[str]], set[str]]:
    """Load the human projection and expand only explicitly named WP-* IDs.

    Rows that still use prose aliases are rejected. This prevents a convenient
    display shorthand from becoming a second, ambiguous machine contract.
    """
    dag = json.loads((IMPLEMENTATION_DIR / "work-package-dag.v1.json").read_text())
    canonical_wps = {item["wp_id"] for item in dag["work_packages"]}
    catalog: dict[str, list[str]] = {}
    for line in (IMPLEMENTATION_DIR / "requirements-traceability.md").read_text().splitlines():
        match = REQUIREMENT_TABLE_RE.match(line)
        if not match:
            continue
        requirement_id, wp_cell = match.groups()
        wp_ids = sorted(set(WP_TOKEN_RE.findall(wp_cell)))
        unknown = sorted(set(wp_ids) - canonical_wps)
        if unknown:
            raise RuntimeError(f"unknown work package IDs for {requirement_id}: {unknown}")
        if not wp_ids:
            raise RuntimeError(f"requirement row has no explicit WP-* consumer: {requirement_id}")
        if requirement_id in catalog:
            raise RuntimeError(f"duplicate requirement ID: {requirement_id}")
        catalog[requirement_id] = wp_ids
    rule_ids = {requirement_id for requirement_id, _ in REQUIREMENT_RULES}
    if set(catalog) != rule_ids:
        raise RuntimeError(
            "requirement catalog/rule mismatch: "
            f"catalog_only={sorted(set(catalog) - rule_ids)}, "
            f"rules_only={sorted(rule_ids - set(catalog))}"
        )
    return catalog, canonical_wps


def load_migrations() -> tuple[dict[str, dict[str, object]], list[dict[str, object]], str]:
    data = json.loads(MIGRATIONS.read_text())
    mappings = data.get("mappings", [])
    by_old = {item["old_clause_id"]: item for item in mappings}
    if len(by_old) != len(mappings):
        raise RuntimeError("duplicate old_clause_id in normative migration map")
    policy_migrations = data.get("policy_migrations", [])
    policy_ids = [item["migration_id"] for item in policy_migrations]
    if len(policy_ids) != len(set(policy_ids)):
        raise RuntimeError("duplicate policy migration ID in normative migration map")
    return by_old, policy_migrations, sha256_bytes(MIGRATIONS.read_bytes())


def validate_migrations(
    migration_map: dict[str, dict[str, object]],
    removed_ids: set[str],
    semantically_changed_ids: set[str],
    new_ids: set[str],
) -> list[dict[str, object]]:
    required = removed_ids | semantically_changed_ids
    missing = sorted(required - set(migration_map))
    if missing:
        raise RuntimeError(f"unmigrated normative clauses: {missing}")
    applied: list[dict[str, object]] = []
    for old_id in sorted(required):
        item = migration_map[old_id]
        disposition = item["disposition"]
        targets = item["new_clause_ids"]
        if disposition == "RETIRED" and targets:
            raise RuntimeError(f"RETIRED migration must have no target: {old_id}")
        if disposition == "REPLACED_BY" and (not targets or old_id in targets):
            raise RuntimeError(f"REPLACED_BY requires non-self target: {old_id}")
        if disposition == "RECLASSIFIED" and len(targets) != 1:
            raise RuntimeError(f"RECLASSIFIED requires exactly one semantic successor: {old_id}")
        unknown_targets = sorted(set(targets) - new_ids)
        if unknown_targets:
            raise RuntimeError(f"migration targets do not exist for {old_id}: {unknown_targets}")
        applied.append(item)
    replacement_graph = {
        old_id: list(map(str, item["new_clause_ids"]))
        for old_id, item in migration_map.items()
        if item["disposition"] in {"REPLACED_BY", "RECLASSIFIED"}
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            raise RuntimeError(f"cycle in normative migration map at {node}")
        if node in visited:
            return
        visiting.add(node)
        for target in replacement_graph.get(node, []):
            if target in replacement_graph:
                visit(target)
        visiting.remove(node)
        visited.add(node)

    for start in replacement_graph:
        visit(start)
    return applied


def clause_id_set_sha256(clause_ids: list[str]) -> str:
    return sha256_bytes(("\n".join(sorted(clause_ids)) + "\n").encode("utf-8"))


def validate_consumer_policy_migrations(
    policy_migrations: list[dict[str, object]],
    current: dict[str, object],
    new_data: dict[str, object],
    current_index_sha256: str,
) -> list[dict[str, object]]:
    old_version = int(current.get("generator_contract_version", 0))
    new_version = int(new_data["generator_contract_version"])
    if old_version == new_version:
        return []
    old_clauses = {item["clause_id"]: item for item in current.get("clauses", [])}
    new_clauses = {item["clause_id"]: item for item in new_data["clauses"]}
    old_local_clause_ids = sorted(
        clause_id
        for clause_id, old in old_clauses.items()
        if old.get("classification") == "LOCAL_ONLY" and not old.get("consumer_wp_ids")
    )
    upgraded_common_clause_ids = sorted(
        clause_id
        for clause_id, old in old_clauses.items()
        if clause_id in new_clauses
        and old.get("classification") == "LOCAL_ONLY"
        and not old.get("consumer_wp_ids")
        and new_clauses[clause_id].get("consumer_wp_ids") == [LOCAL_ONLY_TEMPORARY_CONSUMER]
        and new_clauses[clause_id].get("consumer_assignment_basis") == LOCAL_ONLY_CONSUMER_BASIS
    )
    not_upgraded = sorted(
        clause_id
        for clause_id in set(old_local_clause_ids) & set(new_clauses)
        if clause_id not in upgraded_common_clause_ids
    )
    if not_upgraded:
        raise RuntimeError(f"LOCAL_ONLY clauses retained without the v3 consumer policy: {not_upgraded}")
    candidates = [
        item
        for item in policy_migrations
        if item.get("from_generator_contract_version") == old_version
        and item.get("to_generator_contract_version") == new_version
        and item.get("policy_area") == "LOCAL_ONLY_CONSUMER_ASSIGNMENT"
    ]
    if len(candidates) != 1:
        raise RuntimeError(
            "consumer policy upgrade requires exactly one matching policy migration: "
            f"from={old_version}:to={new_version}:found={len(candidates)}"
        )
    item = candidates[0]
    expected = {
        "old_index_sha256": current_index_sha256,
        "expected_affected_clause_count": len(old_local_clause_ids),
        "affected_old_clause_ids_sha256": clause_id_set_sha256(old_local_clause_ids),
        "new_consumer_wp_ids": [LOCAL_ONLY_TEMPORARY_CONSUMER],
        "new_consumer_assignment_basis": LOCAL_ONLY_CONSUMER_BASIS,
    }
    mismatches = {key: (item.get(key), value) for key, value in expected.items() if item.get(key) != value}
    if mismatches:
        raise RuntimeError(f"consumer policy migration mismatch: {mismatches}")
    if not old_local_clause_ids:
        raise RuntimeError("consumer policy migration matched zero clauses")
    return [item]


def build() -> dict[str, object]:
    requirement_catalog, canonical_wps = load_requirement_catalog()
    clauses: list[dict[str, object]] = []
    document_hashes: dict[str, dict[str, str]] = {}
    for path, relative, scope in source_specs():
        raw = path.read_bytes()
        indexed_lines, scope_description = scoped_lines(path, scope)
        scoped_bytes = ("\n".join(line for _, line in indexed_lines) + "\n").encode("utf-8")
        document_hashes[relative] = {
            "full_file_sha256": sha256_bytes(raw),
            "indexed_scope_sha256": sha256_bytes(scoped_bytes),
            "scope": scope_description,
        }
        heading_title = "document-root"
        heading_anchor = "document-root"
        heading_occurrences: dict[str, int] = {}
        text_occurrences: dict[str, int] = {}
        section_ordinals: dict[str, int] = {}
        in_fence = False
        for line_number, line in indexed_lines:
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            heading = HEADING_RE.match(line)
            if heading:
                heading_title = heading.group(2).strip()
                base_anchor = anchor_for(heading_title)
                heading_occurrences[base_anchor] = heading_occurrences.get(base_anchor, 0) + 1
                occurrence = heading_occurrences[base_anchor]
                heading_anchor = base_anchor if occurrence == 1 else f"{base_anchor}-{occurrence}"
                continue
            if not has_normative_token(line):
                continue
            normalized = line.strip()
            if not normalized:
                continue
            section_ordinals[heading_anchor] = section_ordinals.get(heading_anchor, 0) + 1
            text_key = sha256_bytes(normalized.encode("utf-8"))[:18]
            text_occurrences[text_key] = text_occurrences.get(text_key, 0) + 1
            doc_id = relative.removesuffix(".md").replace("../", "up__").replace("/", "__")
            requirement_ids, family_codes, local_reason = classify(normalized)
            applicable_wp_ids = sorted({wp_id for requirement_id in requirement_ids for wp_id in requirement_catalog[requirement_id]})
            if requirement_ids:
                consumer_wp_ids = applicable_wp_ids
                consumer_assignment_basis = "REQUIREMENT_CATALOG"
            else:
                # This is a temporary documentation-governance owner, not a
                # claim that WP-DOC0 implements the runtime behavior described
                # by the clause. A later non-DOC0 plan must consume an
                # independently signed ReviewRecord projection.
                consumer_wp_ids = [LOCAL_ONLY_TEMPORARY_CONSUMER]
                consumer_assignment_basis = LOCAL_ONLY_CONSUMER_BASIS
            clauses.append({
                "clause_id": f"NORM-{doc_id}-{text_key}-{text_occurrences[text_key]:02d}",
                "source_file": relative,
                "source_file_sha256": document_hashes[relative]["full_file_sha256"],
                "indexed_scope_sha256": document_hashes[relative]["indexed_scope_sha256"],
                "source_line": line_number,
                "section_title": heading_title,
                "section_anchor": heading_anchor,
                "section_clause_ordinal": section_ordinals[heading_anchor],
                "source_text": normalized,
                "requirement_ids": requirement_ids,
                "requirement_family_codes": family_codes,
                "applicable_wp_ids": applicable_wp_ids,
                "consumer_wp_ids": consumer_wp_ids,
                "consumer_assignment_basis": consumer_assignment_basis,
                "classification": "EXACT_REQUIREMENT_MAPPED" if requirement_ids else "LOCAL_ONLY",
                "local_only_reason": local_reason,
                "semantic_review_status": "PENDING_INDEPENDENT_AUDIT",
            })
    source_set = "\n".join(
        f"{key}:{value['full_file_sha256']}:{value['indexed_scope_sha256']}:{value['scope']}"
        for key, value in sorted(document_hashes.items())
    )
    observed_outside_matrix = {
        requirement_id
        for item in clauses
        if item["source_file"] != "implementation/requirements-traceability.md"
        for requirement_id in item["requirement_ids"]
    }
    unmapped_requirement_ids = sorted(set(requirement_catalog) - observed_outside_matrix)
    return {
        "schema_id": "seven/docs/normative-requirement-index",
        "schema_version": 1,
        "generator_contract_version": GENERATOR_CONTRACT_VERSION,
        "generator": "tools/generate_normative_index.py",
        "generator_sha256": sha256_bytes(Path(__file__).read_bytes()),
        "source_set_sha256": sha256_bytes(source_set.encode("utf-8")),
        "previous_index_sha256": None,
        "bootstrap_replacement": None,
        "migration_map_ref": "normative-requirement-migrations.v1.json",
        "migration_map_sha256": sha256_bytes(MIGRATIONS.read_bytes()),
        "applied_migrations": [],
        "applied_policy_migrations": [],
        "document_hashes": document_hashes,
        "normative_tokens": list(NORMATIVE_TOKENS),
        "clause_unit": "one non-code source line containing an explicit normative token, a grammatically bounded single-character 应, or an exact independently adjudicated normative sentence",
        "consumer_policy": {
            "policy_id": "LOCAL_ONLY_DOC0_TEMPORARY_CATCH_ALL_V1",
            "local_only_temporary_consumer_wp_ids": [LOCAL_ONLY_TEMPORARY_CONSUMER],
            "consumer_assignment_basis": LOCAL_ONLY_CONSUMER_BASIS,
            "requires_independent_review_record_before_non_doc0_plan": True,
            "nonclaim": "WP-DOC0 temporary consumption denotes documentation-governance and traceability responsibility only; it neither assigns nor proves runtime implementation responsibility.",
        },
        "requirement_family_codes": sorted({requirement_id.split("-", 1)[0] for requirement_id, _ in REQUIREMENT_RULES}),
        "requirement_catalog": [
            {"requirement_id": requirement_id, "applicable_wp_ids": requirement_catalog[requirement_id]}
            for requirement_id in sorted(requirement_catalog)
        ],
        "canonical_work_package_ids": sorted(canonical_wps),
        "clauses": clauses,
        "remainder": {
            "unclassified_clause_count": sum(1 for item in clauses if item["classification"] == "LOCAL_ONLY" and not item["local_only_reason"]),
            "duplicate_clause_id_count": len(clauses) - len({item["clause_id"] for item in clauses}),
            "unmigrated_previous_clause_count": 0,
            "unmapped_requirement_id_count": len(unmapped_requirement_ids),
            "unmapped_requirement_ids": unmapped_requirement_ids,
            "clause_without_consumer_count": sum(1 for item in clauses if not item["consumer_wp_ids"]),
            "local_only_without_temporary_doc0_consumer_count": sum(
                1
                for item in clauses
                if item["classification"] == "LOCAL_ONLY"
                and LOCAL_ONLY_TEMPORARY_CONSUMER not in item["consumer_wp_ids"]
            ),
            "pending_semantic_review_count": len(clauses),
        },
    }


def main() -> None:
    data = build()
    current = None
    if OUTPUT.exists():
        try:
            current = json.loads(OUTPUT.read_text())
        except (json.JSONDecodeError, OSError):
            current = None
    if current and current.get("generator_contract_version") == GENERATOR_CONTRACT_VERSION:
        if (
            current.get("source_set_sha256") == data["source_set_sha256"]
            and current.get("generator_sha256") == data["generator_sha256"]
            and current.get("migration_map_sha256") == data["migration_map_sha256"]
        ):
            print(json.dumps({"status": "ALREADY_CURRENT", "output": str(OUTPUT), "clauses": len(current["clauses"]), "remainder": current["remainder"]}, ensure_ascii=False, sort_keys=True))
            return
    if current and int(current.get("generator_contract_version", 0)) >= 2:
        old_by_id = {item["clause_id"]: item for item in current.get("clauses", [])}
        new_by_id = {item["clause_id"]: item for item in data["clauses"]}
        old_ids = set(old_by_id)
        new_ids = set(new_by_id)
        removed = old_ids - new_ids
        semantic_keys = ("classification", "requirement_ids", "requirement_family_codes", "applicable_wp_ids")
        semantically_changed = {
            clause_id
            for clause_id in old_ids & new_ids
            if any(old_by_id[clause_id].get(key) != new_by_id[clause_id].get(key) for key in semantic_keys)
        }
        migration_map, policy_migrations, migration_hash = load_migrations()
        current_index_sha256 = sha256_bytes(OUTPUT.read_bytes())
        try:
            applied = validate_migrations(migration_map, removed, semantically_changed, new_ids)
            applied_policy = validate_consumer_policy_migrations(
                policy_migrations,
                current,
                data,
                current_index_sha256,
            )
        except RuntimeError as error:
            print(json.dumps({"status": "BLOCKED_UNMIGRATED_REQUIREMENTS", "error": str(error)}, ensure_ascii=False, indent=2), file=sys.stderr)
            raise SystemExit(2) from error
        if int(current.get("generator_contract_version", 0)) == GENERATOR_CONTRACT_VERSION:
            # The migration ledger is cumulative because the repository keeps
            # one canonical index snapshot rather than an archive of every
            # same-version generator refresh. A mechanical generator refresh
            # must not erase the already adjudicated v2->v3 provenance.
            prior_clause_ids = {
                str(item["old_clause_id"])
                for item in current.get("applied_migrations", [])
            }
            missing_prior_clause_ids = sorted(prior_clause_ids - set(migration_map))
            if missing_prior_clause_ids:
                raise RuntimeError(f"previously applied migrations missing from current migration map: {missing_prior_clause_ids}")
            # If the migration map itself was corrected, refresh cumulative
            # entries from the current map. Otherwise the canonical index can
            # preserve stale targets even after the review record supersedes
            # them.
            prior_clause_migrations = {
                old_clause_id: migration_map[old_clause_id]
                for old_clause_id in prior_clause_ids
            }
            prior_clause_migrations.update({str(item["old_clause_id"]): item for item in applied})
            policy_migration_map = {str(item["migration_id"]): item for item in policy_migrations}
            prior_policy_ids = {
                str(item["migration_id"])
                for item in current.get("applied_policy_migrations", [])
            }
            missing_prior_policy_ids = sorted(prior_policy_ids - set(policy_migration_map))
            if missing_prior_policy_ids:
                raise RuntimeError(f"previously applied policy migrations missing from current migration map: {missing_prior_policy_ids}")
            prior_policy_migrations = {
                migration_id: policy_migration_map[migration_id]
                for migration_id in prior_policy_ids
            }
            prior_policy_migrations.update({str(item["migration_id"]): item for item in applied_policy})
            data["previous_index_sha256"] = current.get("previous_index_sha256") or current_index_sha256
            data["bootstrap_replacement"] = current.get("bootstrap_replacement")
            applied = [prior_clause_migrations[key] for key in sorted(prior_clause_migrations)]
            applied_policy = [prior_policy_migrations[key] for key in sorted(prior_policy_migrations)]
        else:
            data["previous_index_sha256"] = current_index_sha256
        data["migration_map_sha256"] = migration_hash
        data["applied_migrations"] = applied
        data["applied_policy_migrations"] = applied_policy
        data["remainder"]["unmigrated_previous_clause_count"] = 0
    elif current:
        # The only pre-v2 file was an uncommitted bootstrap scratch artifact.
        # Bind it for provenance, but do not pretend its unstable IDs were a
        # released contract requiring hundreds of artificial migrations.
        data["previous_index_sha256"] = sha256_bytes(OUTPUT.read_bytes())
        data["bootstrap_replacement"] = {
            "previous_generator_contract_version": current.get("generator_contract_version", 1),
            "disposition": "UNRELEASED_BOOTSTRAP_REPLACED",
            "reason": "pre-v2 index was never committed or used to sign an audited artifact"
        }
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "GENERATED", "output": str(OUTPUT), "clauses": len(data["clauses"]), "source_set_sha256": data["source_set_sha256"], "remainder": data["remainder"]}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
