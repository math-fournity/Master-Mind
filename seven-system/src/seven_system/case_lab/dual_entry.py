"""DualEntry — 双入口路径（WP-CS1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 78-82 和
docs/implementation/15-work-package-implementation-contracts.md line 90：

DualEntry 提供两条进入路径：
- Natural entry: P2A/[P2B]+P3N evidence (natural problem + natural review)
- Generated entry: P3A+P3B evidence (generated problem + bare admission)

两条路径都通过 P3C 产出 CasePack。

冻结输入（blocker）：
- 自然题伪造 draft（natural case has fake QuestionDraftVersion）→ BLOCK
- 生成题缺 bare results → BLOCK
- 自然题缺 P3N review → BLOCK
- 路径不合法 → BLOCK

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    CS_ENTRY_PATHS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from .case_pack import CasePack, build_case_pack, verify_case_pack


_SCHEMA_ID = "seven/dual-entry-fixture"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "DualEntryFixture"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"


@dataclass(frozen=True)
class NaturalEntryEvidence:
    """自然题路径证据。不可变。

    字段：
    - p2a_ref_and_hash：P2A 自然题引用 {ref_id, sha256}
    - p2b_ref_and_hash：P2B 引用（可选，可为空 dict）
    - p3n_review_refs：P3N 审查引用列表
    - question_draft_ref_and_hash：QuestionDraftVersion 引用（必须真实）
    - draft_is_forged：draft 是否伪造（blocker: 必须为 False）
    """

    p2a_ref_and_hash: dict[str, str]
    p2b_ref_and_hash: dict[str, str]
    p3n_review_refs: list[dict[str, str]]
    question_draft_ref_and_hash: dict[str, str]
    draft_is_forged: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "p2a_ref_and_hash": dict(self.p2a_ref_and_hash),
            "p2b_ref_and_hash": dict(self.p2b_ref_and_hash),
            "p3n_review_refs": [dict(r) for r in self.p3n_review_refs],
            "question_draft_ref_and_hash": dict(self.question_draft_ref_and_hash),
            "draft_is_forged": self.draft_is_forged,
        }


@dataclass(frozen=True)
class GeneratedEntryEvidence:
    """生成题路径证据。不可变。

    字段：
    - p3a_ref_and_hash：P3A 生成题引用 {ref_id, sha256}
    - p3b_ref_and_hash：P3B bare admission 引用 {ref_id, sha256}
    - bare_result_refs：bare 结果引用列表
    - question_release_ref_and_hash：QuestionRelease 引用
    """

    p3a_ref_and_hash: dict[str, str]
    p3b_ref_and_hash: dict[str, str]
    bare_result_refs: list[dict[str, str]]
    question_release_ref_and_hash: dict[str, str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "p3a_ref_and_hash": dict(self.p3a_ref_and_hash),
            "p3b_ref_and_hash": dict(self.p3b_ref_and_hash),
            "bare_result_refs": [dict(r) for r in self.bare_result_refs],
            "question_release_ref_and_hash": dict(self.question_release_ref_and_hash),
        }


@dataclass(frozen=True)
class DualEntryFixture:
    """DualEntryFixture — 双入口 fixture。不可变。

    记录一条入口路径的证据和产出的 CasePack 引用。

    字段：
    - fixture_id：fixture 唯一标识
    - entry_path：入口路径（CS_ENTRY_PATHS: NATURAL / GENERATED）
    - natural_evidence：自然题证据（仅 NATURAL 路径）
    - generated_evidence：生成题证据（仅 GENERATED 路径）
    - case_pack_ref_and_hash：产出的 CasePack 引用
    """

    fixture_id: str
    entry_path: str
    natural_evidence: dict[str, Any]
    generated_evidence: dict[str, Any]
    case_pack_ref_and_hash: dict[str, str]
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    content_hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "fixture_id": self.fixture_id,
            "entry_path": self.entry_path,
            "natural_evidence": dict(self.natural_evidence),
            "generated_evidence": dict(self.generated_evidence),
            "case_pack_ref_and_hash": dict(self.case_pack_ref_and_hash),
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }


def _compute_content_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["content_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def _check_ref_hash_valid(obj: Any) -> bool:
    import re
    _hash_re = re.compile(r"^[0-9a-f]{64}$")
    return (
        isinstance(obj, dict)
        and set(obj.keys()) == {"ref_id", "sha256"}
        and isinstance(obj.get("ref_id"), str)
        and bool(obj.get("ref_id"))
        and isinstance(obj.get("sha256"), str)
        and bool(_hash_re.match(obj.get("sha256", "")))
    )


def build_natural_entry_evidence(
    *,
    p2a_ref_and_hash: dict[str, str],
    p3n_review_refs: list[dict[str, str]],
    question_draft_ref_and_hash: dict[str, str],
    p2b_ref_and_hash: dict[str, str] | None = None,
    draft_is_forged: bool = False,
) -> NaturalEntryEvidence:
    """构建自然题路径证据。"""
    return NaturalEntryEvidence(
        p2a_ref_and_hash=dict(p2a_ref_and_hash),
        p2b_ref_and_hash=dict(p2b_ref_and_hash or {}),
        p3n_review_refs=[dict(r) for r in p3n_review_refs],
        question_draft_ref_and_hash=dict(question_draft_ref_and_hash),
        draft_is_forged=draft_is_forged,
    )


def build_generated_entry_evidence(
    *,
    p3a_ref_and_hash: dict[str, str],
    p3b_ref_and_hash: dict[str, str],
    bare_result_refs: list[dict[str, str]],
    question_release_ref_and_hash: dict[str, str],
) -> GeneratedEntryEvidence:
    """构建生成题路径证据。"""
    return GeneratedEntryEvidence(
        p3a_ref_and_hash=dict(p3a_ref_and_hash),
        p3b_ref_and_hash=dict(p3b_ref_and_hash),
        bare_result_refs=[dict(r) for r in bare_result_refs],
        question_release_ref_and_hash=dict(question_release_ref_and_hash),
    )


def verify_natural_entry_evidence(
    evidence: dict[str, Any] | NaturalEntryEvidence,
) -> VerificationResult:
    """验证自然题路径证据。

    检查（blocker tests）：
    1. p2a_ref_and_hash 结构合法
    2. p3n_review_refs 非空且结构合法
    3. question_draft_ref_and_hash 结构合法
    4. draft_is_forged == False（blocker: natural case forged draft）
    """
    if isinstance(evidence, NaturalEntryEvidence):
        evidence = evidence.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if not _check_ref_hash_valid(evidence.get("p2a_ref_and_hash", {})):
        errors.append(EC.CS_EVIDENCE_REF_MISSING)
        details.append("p2a_ref_and_hash must have valid ref_id and sha256")

    p3n_refs = evidence.get("p3n_review_refs", [])
    if not isinstance(p3n_refs, list) or len(p3n_refs) == 0:
        errors.append(EC.CS_EVIDENCE_REF_MISSING)
        details.append("p3n_review_refs must be non-empty")
    else:
        for i, ref in enumerate(p3n_refs):
            if not _check_ref_hash_valid(ref):
                errors.append(EC.CS_EVIDENCE_REF_MISSING)
                details.append(f"p3n_review_refs[{i}] must have valid ref_id and sha256")

    if not _check_ref_hash_valid(evidence.get("question_draft_ref_and_hash", {})):
        errors.append(EC.CS_EVIDENCE_REF_MISSING)
        details.append("question_draft_ref_and_hash must have valid ref_id and sha256")

    # blocker: natural case forged draft
    if evidence.get("draft_is_forged") is True:
        errors.append(EC.CS_NATURAL_CASE_FORGED_DRAFT)
        details.append("draft_is_forged must be False (natural case forged draft → BLOCK)")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def verify_generated_entry_evidence(
    evidence: dict[str, Any] | GeneratedEntryEvidence,
) -> VerificationResult:
    """验证生成题路径证据。

    检查（blocker tests）：
    1. p3a_ref_and_hash 结构合法
    2. p3b_ref_and_hash 结构合法
    3. bare_result_refs 非空且结构合法
    4. question_release_ref_and_hash 结构合法
    """
    if isinstance(evidence, GeneratedEntryEvidence):
        evidence = evidence.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if not _check_ref_hash_valid(evidence.get("p3a_ref_and_hash", {})):
        errors.append(EC.CS_EVIDENCE_REF_MISSING)
        details.append("p3a_ref_and_hash must have valid ref_id and sha256")

    if not _check_ref_hash_valid(evidence.get("p3b_ref_and_hash", {})):
        errors.append(EC.CS_EVIDENCE_REF_MISSING)
        details.append("p3b_ref_and_hash must have valid ref_id and sha256")

    bare_refs = evidence.get("bare_result_refs", [])
    if not isinstance(bare_refs, list) or len(bare_refs) == 0:
        errors.append(EC.CS_EVIDENCE_REF_MISSING)
        details.append("bare_result_refs must be non-empty")
    else:
        for i, ref in enumerate(bare_refs):
            if not _check_ref_hash_valid(ref):
                errors.append(EC.CS_EVIDENCE_REF_MISSING)
                details.append(f"bare_result_refs[{i}] must have valid ref_id and sha256")

    if not _check_ref_hash_valid(evidence.get("question_release_ref_and_hash", {})):
        errors.append(EC.CS_EVIDENCE_REF_MISSING)
        details.append("question_release_ref_and_hash must have valid ref_id and sha256")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def build_dual_entry_fixture(
    *,
    fixture_id: str,
    entry_path: str,
    case_pack_ref_and_hash: dict[str, str],
    natural_evidence: dict[str, Any] | None = None,
    generated_evidence: dict[str, Any] | None = None,
) -> DualEntryFixture:
    """构建 DualEntryFixture，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "fixture_id": fixture_id,
        "entry_path": entry_path,
        "natural_evidence": dict(natural_evidence or {}),
        "generated_evidence": dict(generated_evidence or {}),
        "case_pack_ref_and_hash": dict(case_pack_ref_and_hash),
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return DualEntryFixture(
        fixture_id=fixture_id,
        entry_path=entry_path,
        natural_evidence=dict(natural_evidence or {}),
        generated_evidence=dict(generated_evidence or {}),
        case_pack_ref_and_hash=dict(case_pack_ref_and_hash),
        content_hash=content_hash,
    )


def verify_dual_entry_fixture(
    fixture_obj: dict[str, Any] | DualEntryFixture,
) -> VerificationResult:
    """验证 DualEntryFixture 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. fixture_id 非空
    3. entry_path 在 CS_ENTRY_PATHS 中
    4. NATURAL 路径：natural_evidence 非空且通过验证
    5. GENERATED 路径：generated_evidence 非空且通过验证
    6. case_pack_ref_and_hash 结构合法
    7. content_hash 正确
    """
    if isinstance(fixture_obj, DualEntryFixture):
        fixture_obj = fixture_obj.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if fixture_obj.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if fixture_obj.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if fixture_obj.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not fixture_obj.get("fixture_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("fixture_id must not be empty")

    entry_path = fixture_obj.get("entry_path", "")
    if entry_path not in CS_ENTRY_PATHS:
        errors.append(EC.CS_DUAL_ENTRY_PATH_INVALID)
        details.append(f"entry_path {entry_path!r} not in CS_ENTRY_PATHS {sorted(CS_ENTRY_PATHS)}")

    # NATURAL path: verify natural evidence
    if entry_path == "NATURAL":
        nat_ev = fixture_obj.get("natural_evidence", {})
        if not nat_ev:
            errors.append(EC.CS_EVIDENCE_REF_MISSING)
            details.append("NATURAL path requires natural_evidence")
        else:
            nat_result = verify_natural_entry_evidence(nat_ev)
            if not nat_result.passed:
                errors.extend(nat_result.error_codes)
                details.extend(nat_result.details)

    # GENERATED path: verify generated evidence
    if entry_path == "GENERATED":
        gen_ev = fixture_obj.get("generated_evidence", {})
        if not gen_ev:
            errors.append(EC.CS_EVIDENCE_REF_MISSING)
            details.append("GENERATED path requires generated_evidence")
        else:
            gen_result = verify_generated_entry_evidence(gen_ev)
            if not gen_result.passed:
                errors.extend(gen_result.error_codes)
                details.extend(gen_result.details)

    if not _check_ref_hash_valid(fixture_obj.get("case_pack_ref_and_hash", {})):
        errors.append(EC.CS_EVIDENCE_REF_MISSING)
        details.append("case_pack_ref_and_hash must have valid ref_id and sha256")

    if fixture_obj.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {fixture_obj.get('content_hash_algorithm')}")

    computed = _compute_content_hash(fixture_obj)
    if fixture_obj.get("content_hash") != computed:
        errors.append(EC.CS_CASE_PACK_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {fixture_obj.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


class DualEntry:
    """DualEntry — 双入口路径编排器。

    提供两条入口路径：
    - natural_entry(): P2A/[P2B]+P3N → CasePack
    - generated_entry(): P3A+P3B → CasePack

    两条路径都产出 CasePack，通过 P3C 后由 HumanGate 签名。
    """

    def __init__(self) -> None:
        self._fixtures: list[DualEntryFixture] = []

    def natural_entry(
        self,
        *,
        fixture_id: str,
        pack_id: str,
        problem_statement: str,
        solution: str,
        mechanism_contract_ref_and_hash: dict[str, str],
        relation_mapping_ref_and_hash: dict[str, str],
        role_assignment_refs: list[dict[str, str]],
        p2a_ref_and_hash: dict[str, str],
        p3n_review_refs: list[dict[str, str]],
        question_draft_ref_and_hash: dict[str, str],
        p2b_ref_and_hash: dict[str, str] | None = None,
        draft_is_forged: bool = False,
    ) -> tuple[CasePack | None, DualEntryFixture | None, VerificationResult]:
        """自然题入口路径：P2A/[P2B]+P3N → CasePack。

        流程：
        1. 构建自然题证据
        2. 验证证据（blocker: forged draft, missing P3N, missing P2A）
        3. 构建 CasePack（entry_path=NATURAL, p3n_review_refs）
        4. 验证 CasePack
        5. 构建 DualEntryFixture
        """
        evidence = build_natural_entry_evidence(
            p2a_ref_and_hash=p2a_ref_and_hash,
            p3n_review_refs=p3n_review_refs,
            question_draft_ref_and_hash=question_draft_ref_and_hash,
            p2b_ref_and_hash=p2b_ref_and_hash,
            draft_is_forged=draft_is_forged,
        )

        ev_result = verify_natural_entry_evidence(evidence)
        if not ev_result.passed:
            return None, None, ev_result

        pack = build_case_pack(
            pack_id=pack_id,
            entry_path="NATURAL",
            problem_statement=problem_statement,
            solution=solution,
            mechanism_contract_ref_and_hash=mechanism_contract_ref_and_hash,
            relation_mapping_ref_and_hash=relation_mapping_ref_and_hash,
            p3n_review_refs=p3n_review_refs,
            role_assignment_refs=role_assignment_refs,
        )

        pack_result = verify_case_pack(pack)
        if not pack_result.passed:
            return None, None, pack_result

        fixture = build_dual_entry_fixture(
            fixture_id=fixture_id,
            entry_path="NATURAL",
            case_pack_ref_and_hash=pack.ref_and_hash if hasattr(pack, "ref_and_hash") else {
                "ref_id": pack.pack_id,
                "sha256": pack.content_hash,
            },
            natural_evidence=evidence.to_dict(),
        )

        fixture_result = verify_dual_entry_fixture(fixture)
        if not fixture_result.passed:
            return None, None, fixture_result

        self._fixtures.append(fixture)
        return pack, fixture, VerificationResult(verdict="PASS")

    def generated_entry(
        self,
        *,
        fixture_id: str,
        pack_id: str,
        problem_statement: str,
        solution: str,
        mechanism_contract_ref_and_hash: dict[str, str],
        relation_mapping_ref_and_hash: dict[str, str],
        role_assignment_refs: list[dict[str, str]],
        p3a_ref_and_hash: dict[str, str],
        p3b_ref_and_hash: dict[str, str],
        bare_result_refs: list[dict[str, str]],
        question_release_ref_and_hash: dict[str, str],
    ) -> tuple[CasePack | None, DualEntryFixture | None, VerificationResult]:
        """生成题入口路径：P3A+P3B → CasePack。

        流程：
        1. 构建生成题证据
        2. 验证证据（blocker: missing P3A, missing P3B, missing bare results）
        3. 构建 CasePack（entry_path=GENERATED, bare_result_refs）
        4. 验证 CasePack
        5. 构建 DualEntryFixture
        """
        evidence = build_generated_entry_evidence(
            p3a_ref_and_hash=p3a_ref_and_hash,
            p3b_ref_and_hash=p3b_ref_and_hash,
            bare_result_refs=bare_result_refs,
            question_release_ref_and_hash=question_release_ref_and_hash,
        )

        ev_result = verify_generated_entry_evidence(evidence)
        if not ev_result.passed:
            return None, None, ev_result

        pack = build_case_pack(
            pack_id=pack_id,
            entry_path="GENERATED",
            problem_statement=problem_statement,
            solution=solution,
            mechanism_contract_ref_and_hash=mechanism_contract_ref_and_hash,
            relation_mapping_ref_and_hash=relation_mapping_ref_and_hash,
            bare_result_refs=bare_result_refs,
            role_assignment_refs=role_assignment_refs,
        )

        pack_result = verify_case_pack(pack)
        if not pack_result.passed:
            return None, None, pack_result

        fixture = build_dual_entry_fixture(
            fixture_id=fixture_id,
            entry_path="GENERATED",
            case_pack_ref_and_hash={
                "ref_id": pack.pack_id,
                "sha256": pack.content_hash,
            },
            generated_evidence=evidence.to_dict(),
        )

        fixture_result = verify_dual_entry_fixture(fixture)
        if not fixture_result.passed:
            return None, None, fixture_result

        self._fixtures.append(fixture)
        return pack, fixture, VerificationResult(verdict="PASS")

    @property
    def fixtures(self) -> list[DualEntryFixture]:
        return list(self._fixtures)
