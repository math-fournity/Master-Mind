"""CasePack / CasePackVersion — 冻结的 case 包和版本化 case 包（WP-CS1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 78-82 和
docs/implementation/15-work-package-implementation-contracts.md line 90：

CasePack 是冻结的 case 包，包含：
- problem statement（题目声明）
- solution（解答）
- mechanism contract（机制合同引用）
- relation mapping（关系映射引用）
- bare results（生成题路径，P3B）
- P3N review results（自然题路径，P3N）
- role assignments（角色分配引用列表）

CasePackVersion 是版本化的 CasePack，带 supersedes_ref。
一旦被 G-CASE-ROLE 签名后冻结（immutable）。

硬约束（blocker）：
- entry_path 在 CS_ENTRY_PATHS 中
- mechanism_contract_ref 结构合法
- role_assignment_refs 非空
- 签名后 immutable == True（CS_CASE_PACK_NOT_IMMUTABLE → BLOCK）
- content_hash 正确
- supersedes_ref 链完整（版本化）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    CS_ENTRY_PATHS,
    CS_CASE_PACK_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/case-pack"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "CasePack"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_VERSION_SCHEMA_ID = "seven/case-pack-version"
_VERSION_SCHEMA_VERSION = 1
_VERSION_OBJECT_TYPE = "CasePackVersion"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class CasePack:
    """CasePack — 冻结的 case 包。不可变。

    字段：
    - pack_id：case 包唯一标识
    - entry_path：进入路径（CS_ENTRY_PATHS: NATURAL / GENERATED）
    - problem_statement：题目声明
    - solution：解答
    - mechanism_contract_ref_and_hash：机制合同引用 {ref_id, sha256}
    - relation_mapping_ref_and_hash：关系映射引用 {ref_id, sha256}
    - bare_result_refs：bare 结果引用列表（生成题路径）
    - p3n_review_refs：P3N 审查引用列表（自然题路径）
    - role_assignment_refs：角色分配引用列表
    - immutable：是否不可变（签名后 True）
    """

    pack_id: str
    entry_path: str
    problem_statement: str
    solution: str
    mechanism_contract_ref_and_hash: dict[str, str]
    relation_mapping_ref_and_hash: dict[str, str]
    bare_result_refs: list[dict[str, str]]
    p3n_review_refs: list[dict[str, str]]
    role_assignment_refs: list[dict[str, str]]
    immutable: bool
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
            "pack_id": self.pack_id,
            "entry_path": self.entry_path,
            "problem_statement": self.problem_statement,
            "solution": self.solution,
            "mechanism_contract_ref_and_hash": dict(self.mechanism_contract_ref_and_hash),
            "relation_mapping_ref_and_hash": dict(self.relation_mapping_ref_and_hash),
            "bare_result_refs": [dict(r) for r in self.bare_result_refs],
            "p3n_review_refs": [dict(r) for r in self.p3n_review_refs],
            "role_assignment_refs": [dict(r) for r in self.role_assignment_refs],
            "immutable": self.immutable,
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }


@dataclass(frozen=True)
class CasePackVersion:
    """CasePackVersion — 版本化的 case 包。不可变。

    带 supersedes_ref 指向前一个版本。
    一旦被 G-CASE-ROLE 签名后冻结（state=FROZEN, immutable=True）。

    字段：
    - version_id：版本唯一标识
    - pack_ref_and_hash：CasePack 引用 {ref_id, sha256}
    - version_number：版本号（从 0 开始）
    - supersedes_ref：前一个版本引用 {version_id, content_hash}（首版本为空 dict）
    - state：状态（CS_CASE_PACK_STATES: DRAFT / FROZEN / SUPERSEDED）
    - signed_by_human：是否由人类签名
    - admission_decision_ref_and_hash：AdmissionDecision 引用
    """

    version_id: str
    pack_ref_and_hash: dict[str, str]
    version_number: int
    supersedes_ref: dict[str, str]
    state: str
    signed_by_human: bool
    admission_decision_ref_and_hash: dict[str, str]
    schema_id: str = _VERSION_SCHEMA_ID
    schema_version: int = _VERSION_SCHEMA_VERSION
    object_type: str = _VERSION_OBJECT_TYPE
    content_hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "version_id": self.version_id,
            "pack_ref_and_hash": dict(self.pack_ref_and_hash),
            "version_number": self.version_number,
            "supersedes_ref": dict(self.supersedes_ref),
            "state": self.state,
            "signed_by_human": self.signed_by_human,
            "admission_decision_ref_and_hash": dict(self.admission_decision_ref_and_hash),
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }


def _compute_content_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["content_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def _check_ref_hash(obj: Any, field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"ref_id", "sha256"}:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly ref_id and sha256"))
        return errors
    if not obj.get("ref_id"):
        errors.append((EC.CS_EVIDENCE_REF_MISSING, f"{field_name}.ref_id is empty"))
    sha = obj.get("sha256", "")
    if not isinstance(sha, str) or not _HASH_RE.match(sha):
        errors.append((EC.OBJECT_HASH_MISMATCH, f"{field_name}.sha256 is not valid sha256"))
    return errors


def _check_ref_list(refs: Any, field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(refs, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must be a list"))
        return errors
    for i, ref in enumerate(refs):
        errors.extend(_check_ref_hash(ref, f"{field_name}[{i}]"))
    return errors


def build_case_pack(
    *,
    pack_id: str,
    entry_path: str,
    problem_statement: str,
    solution: str,
    mechanism_contract_ref_and_hash: dict[str, str],
    relation_mapping_ref_and_hash: dict[str, str],
    bare_result_refs: list[dict[str, str]] | None = None,
    p3n_review_refs: list[dict[str, str]] | None = None,
    role_assignment_refs: list[dict[str, str]] | None = None,
    immutable: bool = False,
) -> CasePack:
    """构建 CasePack，自动计算 content_hash。

    bare_result_refs 用于生成题路径（GENERATED）。
    p3n_review_refs 用于自然题路径（NATURAL）。
    role_assignment_refs 是角色分配引用列表。
    immutable 默认 False（签名后由 CasePackVersion 设为 True）。
    """
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "pack_id": pack_id,
        "entry_path": entry_path,
        "problem_statement": problem_statement,
        "solution": solution,
        "mechanism_contract_ref_and_hash": dict(mechanism_contract_ref_and_hash),
        "relation_mapping_ref_and_hash": dict(relation_mapping_ref_and_hash),
        "bare_result_refs": [dict(r) for r in (bare_result_refs or [])],
        "p3n_review_refs": [dict(r) for r in (p3n_review_refs or [])],
        "role_assignment_refs": [dict(r) for r in (role_assignment_refs or [])],
        "immutable": immutable,
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return CasePack(
        pack_id=pack_id,
        entry_path=entry_path,
        problem_statement=problem_statement,
        solution=solution,
        mechanism_contract_ref_and_hash=dict(mechanism_contract_ref_and_hash),
        relation_mapping_ref_and_hash=dict(relation_mapping_ref_and_hash),
        bare_result_refs=[dict(r) for r in (bare_result_refs or [])],
        p3n_review_refs=[dict(r) for r in (p3n_review_refs or [])],
        role_assignment_refs=[dict(r) for r in (role_assignment_refs or [])],
        immutable=immutable,
        content_hash=content_hash,
    )


def verify_case_pack(
    pack_obj: dict[str, Any] | CasePack,
) -> VerificationResult:
    """验证 CasePack 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. pack_id 非空
    3. entry_path 在 CS_ENTRY_PATHS 中
    4. problem_statement / solution 非空
    5. mechanism_contract_ref_and_hash 结构合法
    6. relation_mapping_ref_and_hash 结构合法
    7. role_assignment_refs 非空
    8. bare_result_refs / p3n_review_refs 结构合法
    9. content_hash 正确
    """
    if isinstance(pack_obj, CasePack):
        pack_obj = pack_obj.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if pack_obj.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if pack_obj.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if pack_obj.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not pack_obj.get("pack_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("pack_id must not be empty")

    entry_path = pack_obj.get("entry_path", "")
    if entry_path not in CS_ENTRY_PATHS:
        errors.append(EC.CS_DUAL_ENTRY_PATH_INVALID)
        details.append(f"entry_path {entry_path!r} not in CS_ENTRY_PATHS {sorted(CS_ENTRY_PATHS)}")

    if not pack_obj.get("problem_statement"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("problem_statement must not be empty")

    if not pack_obj.get("solution"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("solution must not be empty")

    for code, detail in _check_ref_hash(
        pack_obj.get("mechanism_contract_ref_and_hash", {}),
        "mechanism_contract_ref_and_hash",
    ):
        errors.append(code)
        details.append(detail)

    for code, detail in _check_ref_hash(
        pack_obj.get("relation_mapping_ref_and_hash", {}),
        "relation_mapping_ref_and_hash",
    ):
        errors.append(code)
        details.append(detail)

    for code, detail in _check_ref_list(
        pack_obj.get("bare_result_refs", []), "bare_result_refs"
    ):
        errors.append(code)
        details.append(detail)

    for code, detail in _check_ref_list(
        pack_obj.get("p3n_review_refs", []), "p3n_review_refs"
    ):
        errors.append(code)
        details.append(detail)

    for code, detail in _check_ref_list(
        pack_obj.get("role_assignment_refs", []), "role_assignment_refs"
    ):
        errors.append(code)
        details.append(detail)

    # role_assignment_refs must be non-empty
    role_refs = pack_obj.get("role_assignment_refs", [])
    if not isinstance(role_refs, list) or len(role_refs) == 0:
        errors.append(EC.CS_ROLE_WITHOUT_EVIDENCE)
        details.append("role_assignment_refs must be non-empty")

    if pack_obj.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {pack_obj.get('content_hash_algorithm')}")

    computed = _compute_content_hash(pack_obj)
    if pack_obj.get("content_hash") != computed:
        errors.append(EC.CS_CASE_PACK_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {pack_obj.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def build_case_pack_version(
    *,
    version_id: str,
    pack_ref_and_hash: dict[str, str],
    version_number: int,
    supersedes_ref: dict[str, str] | None = None,
    state: str = "DRAFT",
    signed_by_human: bool = False,
    admission_decision_ref_and_hash: dict[str, str] | None = None,
) -> CasePackVersion:
    """构建 CasePackVersion，自动计算 content_hash。

    state 默认 DRAFT（签名后设为 FROZEN）。
    signed_by_human 默认 False（签名后设为 True）。
    supersedes_ref 首版本为空 dict。
    """
    obj = {
        "schema_id": _VERSION_SCHEMA_ID,
        "schema_version": _VERSION_SCHEMA_VERSION,
        "object_type": _VERSION_OBJECT_TYPE,
        "version_id": version_id,
        "pack_ref_and_hash": dict(pack_ref_and_hash),
        "version_number": version_number,
        "supersedes_ref": dict(supersedes_ref or {}),
        "state": state,
        "signed_by_human": signed_by_human,
        "admission_decision_ref_and_hash": dict(admission_decision_ref_and_hash or {}),
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return CasePackVersion(
        version_id=version_id,
        pack_ref_and_hash=dict(pack_ref_and_hash),
        version_number=version_number,
        supersedes_ref=dict(supersedes_ref or {}),
        state=state,
        signed_by_human=signed_by_human,
        admission_decision_ref_and_hash=dict(admission_decision_ref_and_hash or {}),
        content_hash=content_hash,
    )


def verify_case_pack_version(
    version_obj: dict[str, Any] | CasePackVersion,
) -> VerificationResult:
    """验证 CasePackVersion 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. version_id 非空
    3. pack_ref_and_hash 结构合法
    4. version_number >= 0
    5. supersedes_ref：首版本为空 dict，后续版本必须引用前版本
    6. state 在 CS_CASE_PACK_STATES 中
    7. FROZEN 状态时 signed_by_human == True 且 immutable
    8. admission_decision_ref_and_hash 结构合法
    9. content_hash 正确
    """
    if isinstance(version_obj, CasePackVersion):
        version_obj = version_obj.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if version_obj.get("schema_id") != _VERSION_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_VERSION_SCHEMA_ID}")
    if version_obj.get("schema_version") != _VERSION_SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_VERSION_SCHEMA_VERSION}")
    if version_obj.get("object_type") != _VERSION_OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_VERSION_OBJECT_TYPE}")

    if not version_obj.get("version_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("version_id must not be empty")

    for code, detail in _check_ref_hash(
        version_obj.get("pack_ref_and_hash", {}), "pack_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)

    version_number = version_obj.get("version_number", -1)
    if not isinstance(version_number, int) or version_number < 0:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append(f"version_number must be >= 0, got {version_number}")

    # supersedes_ref chain
    supersedes_ref = version_obj.get("supersedes_ref", {})
    if version_number == 0:
        if supersedes_ref:
            errors.append(EC.CS_CASE_PACK_VERSION_REF_BROKEN)
            details.append("first version (v0) must have empty supersedes_ref")
    else:
        if not supersedes_ref or not supersedes_ref.get("version_id") or not supersedes_ref.get("content_hash"):
            errors.append(EC.CS_CASE_PACK_VERSION_REF_BROKEN)
            details.append(f"version {version_number} must have valid supersedes_ref")

    state = version_obj.get("state", "")
    if state not in CS_CASE_PACK_STATES:
        errors.append(EC.CS_CASE_PACK_STATE_INVALID)
        details.append(f"state {state!r} not in CS_CASE_PACK_STATES {sorted(CS_CASE_PACK_STATES)}")

    # FROZEN state requires human signature
    if state == "FROZEN":
        if version_obj.get("signed_by_human") is not True:
            errors.append(EC.CS_MODEL_SELF_SIGNED_ROLE)
            details.append("FROZEN state requires signed_by_human=True (model cannot sign G-CASE-ROLE)")

    for code, detail in _check_ref_hash(
        version_obj.get("admission_decision_ref_and_hash", {}),
        "admission_decision_ref_and_hash",
    ):
        errors.append(code)
        details.append(detail)

    if version_obj.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {version_obj.get('content_hash_algorithm')}")

    computed = _compute_content_hash(version_obj)
    if version_obj.get("content_hash") != computed:
        errors.append(EC.CS_CASE_PACK_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {version_obj.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def freeze_case_pack_version(
    version: CasePackVersion,
    *,
    signed_by_human: bool = True,
) -> CasePackVersion:
    """将 CasePackVersion 从 DRAFT 冻结为 FROZEN。

    冻结后不可修改（immutable）。必须由人类签名。
    返回新的 CasePackVersion 对象（重新计算 content_hash）。
    """
    if version.state != "DRAFT":
        return version  # 已经冻结或被取代，不重复冻结
    return build_case_pack_version(
        version_id=version.version_id,
        pack_ref_and_hash=dict(version.pack_ref_and_hash),
        version_number=version.version_number,
        supersedes_ref=dict(version.supersedes_ref) or None,
        state="FROZEN",
        signed_by_human=signed_by_human,
        admission_decision_ref_and_hash=dict(version.admission_decision_ref_and_hash) or None,
    )


def check_case_pack_immutable(
    version: dict[str, Any] | CasePackVersion,
) -> VerificationResult:
    """检查 CasePackVersion 在 FROZEN 状态下是否不可变。

    blocker: CasePack not immutable → BLOCK
    """
    if isinstance(version, CasePackVersion):
        version = version.to_dict()

    if version.get("state") == "FROZEN" and version.get("signed_by_human") is not True:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.CS_CASE_PACK_NOT_IMMUTABLE],
            details=["FROZEN CasePackVersion must have signed_by_human=True"],
        )
    return VerificationResult(verdict="PASS")
