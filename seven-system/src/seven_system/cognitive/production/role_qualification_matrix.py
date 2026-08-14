"""RoleQualificationMatrix / RoleQualificationCell — 版本化资格矩阵。

来自 docs/implementation/05-execution-ports-and-carriers.md RoleQualificationMatrix 节
和 docs/implementation/role-qualification-matrix.v1.schema.json。

每个 cell 显式绑定：
  role_type_id × carrier_id × model_id × carrier_profile hash
  × input_view hash × view policy hash × ACL policy hash × VaultAccessCapability hash
  × tool/network/sandbox policy hash × output sensitivity/sink policy hash
  × adapter hash × parser hash × capability requirement hash
  × CANARY|PRODUCTION

cell_key 是上述字段按 Schema 顺序 canonical 化后的 SHA-256。
Schema 在所有精确字符串和 ref 处拒绝 *、?、glob 字符及 ANY/ALL/DEFAULT 哨兵。

completeness 跟踪 required/pass/not-tested/failed/extra/missing/remainder 集合。
failed 合并 PARTIAL/FAIL/BLOCKED/EXPIRED；missing 是 required 中根本没有 cell 的键；
extra 是 observed 中不在 required 的键；remainder 是 not-tested、failed、missing
与 extra 的去重并集。只有这些集合互斥/相等关系经 semantic verifier 重算、
remainder_count=0 且矩阵 hash 有效时，completeness 才可为 PASS。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    CW_CELL_STATUSES,
    CW_COMPLETENESS_KINDS,
    CW_QUALIFICATION_SCOPES,
    CW_WILDCARD_SENTINELS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
# 精确字符串：不含通配符/glob 字符，不含哨兵
_EXACT_STRING_RE = re.compile(r"^[^*?\[\]{}\r\n]+$")
_GLOB_CHARS = set("*?[]{}")

_MATRIX_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-matrix_hash-null)"
_CELL_KEY_ALGORITHM = "sha256(RFC8785-JCS-cell-fields)"


def _is_sha256(value: str) -> bool:
    return isinstance(value, str) and bool(_HASH_RE.match(value))


def _is_exact_string(value: Any) -> bool:
    """精确字符串：非空、不含 glob 字符、不是通配符哨兵。"""
    if not isinstance(value, str) or not value:
        return False
    if any(c in _GLOB_CHARS for c in value):
        return False
    if value in CW_WILDCARD_SENTINELS:
        return False
    return True


def _check_ref_hash(obj: Any, field_name: str) -> list[tuple[EC, str]]:
    """检查 ref_and_hash 结构：{"ref": str, "sha256": hash}。"""
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"ref", "sha256"}:
        errors.append(
            (EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly ref and sha256")
        )
        return errors
    ref_val = obj.get("ref", "")
    if not _is_exact_string(ref_val):
        errors.append(
            (EC.CW_MATRIX_WILDCARD_REJECTED, f"{field_name}.ref is not exact: {ref_val!r}")
        )
    sha_val = obj.get("sha256", "")
    if not _is_sha256(sha_val):
        errors.append(
            (EC.OBJECT_HASH_MISMATCH, f"{field_name}.sha256 is not a valid hash: {sha_val!r}")
        )
    return errors


# ─── RoleQualificationCell ──────────────────────────────────────────────


@dataclass(frozen=True)
class RoleQualificationCell:
    """单个资格 cell。不可变。

    精确绑定 role×carrier×model×profile×view×policy×capability×adapter×parser。
    cell_key 是上述字段按 Schema 顺序 canonical 化后的 SHA-256。
    """

    qualification_cell_id: str
    role_type_id: str
    carrier_id: str
    model_id: str
    carrier_profile_ref_and_hash: dict[str, str]
    input_view_ref_and_hash: dict[str, str]
    input_view_policy_ref_and_hash: dict[str, str]
    input_acl_policy_ref_and_hash: dict[str, str]
    vault_access_capability_ref_and_hash: dict[str, str]
    tool_network_sandbox_policy_ref_and_hash: dict[str, str]
    output_sensitivity_and_sink_policy_ref_and_hash: dict[str, str]
    prompt_release_ref_and_hash: dict[str, str]
    output_schema_ref_and_hash: dict[str, str]
    adapter_ref_and_hash: dict[str, str]
    parser_ref_and_hash: dict[str, str]
    capability_requirement_ref_and_hash: dict[str, str]
    qualification_level: str  # CANARY | PRODUCTION
    verdict: str  # NOT_TESTED | PASS | PARTIAL | FAIL | BLOCKED | EXPIRED
    capability_report_refs_and_hashes: list[dict[str, str]] = field(default_factory=list)
    evidence_bundle_refs_and_hashes: list[dict[str, str]] = field(default_factory=list)
    valid_from: str = ""
    valid_until: str | None = None
    invalidated_at: str | None = None
    invalidation_reason: str | None = None
    cell_key: str = ""
    cell_key_algorithm: str = _CELL_KEY_ALGORITHM

    def to_dict(self) -> dict[str, Any]:
        return {
            "qualification_cell_id": self.qualification_cell_id,
            "cell_key": self.cell_key,
            "role_type_id": self.role_type_id,
            "carrier_id": self.carrier_id,
            "model_id": self.model_id,
            "carrier_profile_ref_and_hash": dict(self.carrier_profile_ref_and_hash),
            "input_view_ref_and_hash": dict(self.input_view_ref_and_hash),
            "input_view_policy_ref_and_hash": dict(self.input_view_policy_ref_and_hash),
            "input_acl_policy_ref_and_hash": dict(self.input_acl_policy_ref_and_hash),
            "vault_access_capability_ref_and_hash": dict(self.vault_access_capability_ref_and_hash),
            "tool_network_sandbox_policy_ref_and_hash": dict(self.tool_network_sandbox_policy_ref_and_hash),
            "output_sensitivity_and_sink_policy_ref_and_hash": dict(self.output_sensitivity_and_sink_policy_ref_and_hash),
            "prompt_release_ref_and_hash": dict(self.prompt_release_ref_and_hash),
            "output_schema_ref_and_hash": dict(self.output_schema_ref_and_hash),
            "adapter_ref_and_hash": dict(self.adapter_ref_and_hash),
            "parser_ref_and_hash": dict(self.parser_ref_and_hash),
            "capability_requirement_ref_and_hash": dict(self.capability_requirement_ref_and_hash),
            "qualification_level": self.qualification_level,
            "verdict": self.verdict,
            "capability_report_refs_and_hashes": [dict(r) for r in self.capability_report_refs_and_hashes],
            "evidence_bundle_refs_and_hashes": [dict(r) for r in self.evidence_bundle_refs_and_hashes],
            "valid_from": self.valid_from,
            "valid_until": self.valid_until,
            "invalidated_at": self.invalidated_at,
            "invalidation_reason": self.invalidation_reason,
            "cell_key_algorithm": self.cell_key_algorithm,
        }

    @property
    def is_pass(self) -> bool:
        return self.verdict == "PASS"

    @property
    def is_production(self) -> bool:
        return self.qualification_level == "PRODUCTION"

    @property
    def is_expired(self) -> bool:
        return self.verdict == "EXPIRED"

    @property
    def is_invalidated(self) -> bool:
        return self.invalidated_at is not None

    @property
    def has_conclusion(self) -> bool:
        """cell 是否有结论（PASS / NOT_TESTED / FAILED 系列）。

        FAILED 系列包含 PARTIAL/FAIL/BLOCKED/EXPIRED。
        缺失结论 = 既非 PASS 也非 NOT_TESTED 也非 FAILED 系列。
        """
        if self.verdict == "PASS":
            return True
        if self.verdict == "NOT_TESTED":
            return True
        if self.verdict in ("PARTIAL", "FAIL", "BLOCKED", "EXPIRED"):
            return True
        return False

    @property
    def conclusion(self) -> str:
        """返回归一化结论：PASS / NOT_TESTED / FAILED。

        FAILED 合并 PARTIAL/FAIL/BLOCKED/EXPIRED。
        """
        if self.verdict == "PASS":
            return "PASS"
        if self.verdict == "NOT_TESTED":
            return "NOT_TESTED"
        if self.verdict in ("PARTIAL", "FAIL", "BLOCKED", "EXPIRED"):
            return "FAILED"
        return ""


def compute_cell_key(cell_fields: dict[str, Any]) -> str:
    """计算 cell_key：上述字段按 Schema 顺序 canonical 化后的 SHA-256。"""
    key_payload = {
        "role_type_id": cell_fields["role_type_id"],
        "carrier_id": cell_fields["carrier_id"],
        "model_id": cell_fields["model_id"],
        "carrier_profile_ref_and_hash": dict(cell_fields["carrier_profile_ref_and_hash"]),
        "input_view_ref_and_hash": dict(cell_fields["input_view_ref_and_hash"]),
        "input_view_policy_ref_and_hash": dict(cell_fields["input_view_policy_ref_and_hash"]),
        "input_acl_policy_ref_and_hash": dict(cell_fields["input_acl_policy_ref_and_hash"]),
        "vault_access_capability_ref_and_hash": dict(cell_fields["vault_access_capability_ref_and_hash"]),
        "tool_network_sandbox_policy_ref_and_hash": dict(cell_fields["tool_network_sandbox_policy_ref_and_hash"]),
        "output_sensitivity_and_sink_policy_ref_and_hash": dict(cell_fields["output_sensitivity_and_sink_policy_ref_and_hash"]),
        "prompt_release_ref_and_hash": dict(cell_fields["prompt_release_ref_and_hash"]),
        "output_schema_ref_and_hash": dict(cell_fields["output_schema_ref_and_hash"]),
        "adapter_ref_and_hash": dict(cell_fields["adapter_ref_and_hash"]),
        "parser_ref_and_hash": dict(cell_fields["parser_ref_and_hash"]),
        "capability_requirement_ref_and_hash": dict(cell_fields["capability_requirement_ref_and_hash"]),
        "qualification_level": cell_fields["qualification_level"],
    }
    return hashlib.sha256(canonical_json_bytes(key_payload)).hexdigest()


def build_role_qualification_cell(
    *,
    qualification_cell_id: str,
    role_type_id: str,
    carrier_id: str,
    model_id: str,
    carrier_profile_ref_and_hash: dict[str, str],
    input_view_ref_and_hash: dict[str, str],
    input_view_policy_ref_and_hash: dict[str, str],
    input_acl_policy_ref_and_hash: dict[str, str],
    vault_access_capability_ref_and_hash: dict[str, str],
    tool_network_sandbox_policy_ref_and_hash: dict[str, str],
    output_sensitivity_and_sink_policy_ref_and_hash: dict[str, str],
    prompt_release_ref_and_hash: dict[str, str],
    output_schema_ref_and_hash: dict[str, str],
    adapter_ref_and_hash: dict[str, str],
    parser_ref_and_hash: dict[str, str],
    capability_requirement_ref_and_hash: dict[str, str],
    qualification_level: str,
    verdict: str,
    capability_report_refs_and_hashes: list[dict[str, str]] | None = None,
    evidence_bundle_refs_and_hashes: list[dict[str, str]] | None = None,
    valid_from: str = "",
    valid_until: str | None = None,
    invalidated_at: str | None = None,
    invalidation_reason: str | None = None,
) -> RoleQualificationCell:
    """构建 RoleQualificationCell，自动计算 cell_key。"""
    fields_dict = {
        "role_type_id": role_type_id,
        "carrier_id": carrier_id,
        "model_id": model_id,
        "carrier_profile_ref_and_hash": dict(carrier_profile_ref_and_hash),
        "input_view_ref_and_hash": dict(input_view_ref_and_hash),
        "input_view_policy_ref_and_hash": dict(input_view_policy_ref_and_hash),
        "input_acl_policy_ref_and_hash": dict(input_acl_policy_ref_and_hash),
        "vault_access_capability_ref_and_hash": dict(vault_access_capability_ref_and_hash),
        "tool_network_sandbox_policy_ref_and_hash": dict(tool_network_sandbox_policy_ref_and_hash),
        "output_sensitivity_and_sink_policy_ref_and_hash": dict(output_sensitivity_and_sink_policy_ref_and_hash),
        "prompt_release_ref_and_hash": dict(prompt_release_ref_and_hash),
        "output_schema_ref_and_hash": dict(output_schema_ref_and_hash),
        "adapter_ref_and_hash": dict(adapter_ref_and_hash),
        "parser_ref_and_hash": dict(parser_ref_and_hash),
        "capability_requirement_ref_and_hash": dict(capability_requirement_ref_and_hash),
        "qualification_level": qualification_level,
    }
    cell_key = compute_cell_key(fields_dict)
    return RoleQualificationCell(
        qualification_cell_id=qualification_cell_id,
        role_type_id=role_type_id,
        carrier_id=carrier_id,
        model_id=model_id,
        carrier_profile_ref_and_hash=dict(carrier_profile_ref_and_hash),
        input_view_ref_and_hash=dict(input_view_ref_and_hash),
        input_view_policy_ref_and_hash=dict(input_view_policy_ref_and_hash),
        input_acl_policy_ref_and_hash=dict(input_acl_policy_ref_and_hash),
        vault_access_capability_ref_and_hash=dict(vault_access_capability_ref_and_hash),
        tool_network_sandbox_policy_ref_and_hash=dict(tool_network_sandbox_policy_ref_and_hash),
        output_sensitivity_and_sink_policy_ref_and_hash=dict(output_sensitivity_and_sink_policy_ref_and_hash),
        prompt_release_ref_and_hash=dict(prompt_release_ref_and_hash),
        output_schema_ref_and_hash=dict(output_schema_ref_and_hash),
        adapter_ref_and_hash=dict(adapter_ref_and_hash),
        parser_ref_and_hash=dict(parser_ref_and_hash),
        capability_requirement_ref_and_hash=dict(capability_requirement_ref_and_hash),
        qualification_level=qualification_level,
        verdict=verdict,
        capability_report_refs_and_hashes=[dict(r) for r in (capability_report_refs_and_hashes or [])],
        evidence_bundle_refs_and_hashes=[dict(r) for r in (evidence_bundle_refs_and_hashes or [])],
        valid_from=valid_from,
        valid_until=valid_until,
        invalidated_at=invalidated_at,
        invalidation_reason=invalidation_reason,
        cell_key=cell_key,
    )


def verify_role_qualification_cell(
    cell: dict[str, Any] | RoleQualificationCell,
) -> VerificationResult:
    """验证单个 RoleQualificationCell 的 schema + semantic 合法性。

    检查：
    1. 精确字符串字段不含通配符/glob/哨兵
    2. 所有 ref_and_hash 结构合法
    3. qualification_level 在合法枚举中
    4. verdict 在合法枚举中
    5. cell_key 正确
    6. PASS → capability_report_refs 非空、evidence 非空、valid_until 非空
    7. NOT_TESTED → capability_report_refs 空、evidence 空、invalidated_at null
    8. FAILED 系列 → evidence 非空
    """
    if isinstance(cell, RoleQualificationCell):
        cell = cell.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. 精确字符串字段
    for str_field in ("qualification_cell_id", "role_type_id", "carrier_id", "model_id"):
        val = cell.get(str_field, "")
        if not _is_exact_string(val):
            _err(EC.CW_MATRIX_WILDCARD_REJECTED, f"{str_field} is not exact: {val!r}")

    # 2. ref_and_hash 字段
    for ref_field in (
        "carrier_profile_ref_and_hash",
        "input_view_ref_and_hash",
        "input_view_policy_ref_and_hash",
        "input_acl_policy_ref_and_hash",
        "vault_access_capability_ref_and_hash",
        "tool_network_sandbox_policy_ref_and_hash",
        "output_sensitivity_and_sink_policy_ref_and_hash",
        "prompt_release_ref_and_hash",
        "output_schema_ref_and_hash",
        "adapter_ref_and_hash",
        "parser_ref_and_hash",
        "capability_requirement_ref_and_hash",
    ):
        for code, detail in _check_ref_hash(cell.get(ref_field, {}), ref_field):
            _err(code, detail)

    # 3. qualification_level
    ql = cell.get("qualification_level", "")
    if ql not in CW_QUALIFICATION_SCOPES:
        _err(EC.CW_QUALIFICATION_SCOPE_INVALID, f"invalid qualification_level: {ql}")

    # 4. verdict
    verdict = cell.get("verdict", "")
    if verdict not in CW_CELL_STATUSES:
        _err(EC.CW_CELL_VERDICT_INVALID, f"invalid verdict: {verdict}")

    # 5. cell_key
    stored_key = cell.get("cell_key", "")
    if not _is_sha256(stored_key):
        _err(EC.OBJECT_HASH_MISMATCH, f"cell_key is not a valid hash: {stored_key!r}")
    else:
        computed_key = compute_cell_key(cell)
        if stored_key != computed_key:
            _err(
                EC.CW_CELL_KEY_MISMATCH,
                f"cell_key mismatch: expected {computed_key}, got {stored_key}",
            )

    # 6. PASS 约束
    if verdict == "PASS":
        if not cell.get("capability_report_refs_and_hashes"):
            _err(EC.REQUIRED_FIELD_MISSING, "PASS cell requires capability_report_refs")
        if not cell.get("evidence_bundle_refs_and_hashes"):
            _err(EC.REQUIRED_FIELD_MISSING, "PASS cell requires evidence_bundle_refs")
        if not cell.get("valid_until"):
            _err(EC.REQUIRED_FIELD_MISSING, "PASS cell requires valid_until")
        if cell.get("invalidated_at") is not None:
            _err(EC.CW_CELL_INVALIDATED, "PASS cell must not be invalidated")

    # 7. NOT_TESTED 约束
    if verdict == "NOT_TESTED":
        if cell.get("capability_report_refs_and_hashes"):
            _err(EC.REQUIRED_FIELD_MISSING, "NOT_TESTED cell must have empty capability_report_refs")
        if cell.get("evidence_bundle_refs_and_hashes"):
            _err(EC.REQUIRED_FIELD_MISSING, "NOT_TESTED cell must have empty evidence_bundle_refs")
        if cell.get("invalidated_at") is not None:
            _err(EC.CW_CELL_INVALIDATED, "NOT_TESTED cell must not be invalidated")

    # 8. FAILED 系列约束
    if verdict in ("PARTIAL", "FAIL", "BLOCKED", "EXPIRED"):
        if not cell.get("evidence_bundle_refs_and_hashes"):
            _err(EC.REQUIRED_FIELD_MISSING, f"{verdict} cell requires evidence_bundle_refs")

    verdict_str = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict_str, error_codes=errors, details=details)


# ─── Completeness ───────────────────────────────────────────────────────


@dataclass
class Completeness:
    """资格矩阵的完备性跟踪。

    required/pass/not-tested/failed/extra/missing/remainder 集合。
    failed 合并 PARTIAL/FAIL/BLOCKED/EXPIRED。
    missing 是 required 中根本没有 cell 的键。
    extra 是 observed 中不在 required 的键。
    remainder 是 not-tested、failed、missing 与 extra 的去重并集。
    """

    required_cell_keys: list[str] = field(default_factory=list)
    pass_cell_keys: list[str] = field(default_factory=list)
    not_tested_cell_keys: list[str] = field(default_factory=list)
    failed_cell_keys: list[str] = field(default_factory=list)
    extra_cell_keys: list[str] = field(default_factory=list)
    missing_cell_keys: list[str] = field(default_factory=list)
    remainder_cell_keys: list[str] = field(default_factory=list)
    remainder_count: int = 0
    verdict: str = "BLOCKED"  # PASS | BLOCKED
    algorithm_ref_and_hash: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "required_cell_keys": list(self.required_cell_keys),
            "pass_cell_keys": list(self.pass_cell_keys),
            "not_tested_cell_keys": list(self.not_tested_cell_keys),
            "failed_cell_keys": list(self.failed_cell_keys),
            "extra_cell_keys": list(self.extra_cell_keys),
            "missing_cell_keys": list(self.missing_cell_keys),
            "remainder_cell_keys": list(self.remainder_cell_keys),
            "remainder_count": self.remainder_count,
            "verdict": self.verdict,
            "algorithm_ref_and_hash": dict(self.algorithm_ref_and_hash),
        }


def compute_completeness(
    *,
    required_cell_keys: list[str],
    cells: list[RoleQualificationCell],
    algorithm_ref_and_hash: dict[str, str],
) -> Completeness:
    """从 required cell keys 和实际 cells 计算完备性。

    集合关系：
    - pass = verdict == PASS 的 cell keys
    - not_tested = verdict == NOT_TESTED 的 cell keys
    - failed = verdict in (PARTIAL/FAIL/BLOCKED/EXPIRED) 的 cell keys
    - observed = pass ∪ not_tested ∪ failed
    - extra = observed - required
    - missing = required - observed
    - remainder = not_tested ∪ failed ∪ missing ∪ extra（去重）
    - remainder_count = len(remainder)
    - verdict = PASS iff remainder_count == 0 else BLOCKED
    """
    required_set = set(required_cell_keys)

    pass_keys: list[str] = []
    not_tested_keys: list[str] = []
    failed_keys: list[str] = []

    for cell in cells:
        ck = cell.cell_key
        if cell.verdict == "PASS":
            pass_keys.append(ck)
        elif cell.verdict == "NOT_TESTED":
            not_tested_keys.append(ck)
        elif cell.verdict in ("PARTIAL", "FAIL", "BLOCKED", "EXPIRED"):
            failed_keys.append(ck)

    observed_set = set(pass_keys) | set(not_tested_keys) | set(failed_keys)
    extra_set = observed_set - required_set
    missing_set = required_set - observed_set
    remainder_set = set(not_tested_keys) | set(failed_keys) | missing_set | extra_set

    remainder_count = len(remainder_set)
    verdict = "PASS" if remainder_count == 0 else "BLOCKED"

    return Completeness(
        required_cell_keys=sorted(required_set),
        pass_cell_keys=sorted(set(pass_keys)),
        not_tested_cell_keys=sorted(set(not_tested_keys)),
        failed_cell_keys=sorted(set(failed_keys)),
        extra_cell_keys=sorted(extra_set),
        missing_cell_keys=sorted(missing_set),
        remainder_cell_keys=sorted(remainder_set),
        remainder_count=remainder_count,
        verdict=verdict,
        algorithm_ref_and_hash=dict(algorithm_ref_and_hash),
    )


def verify_completeness(
    completeness: dict[str, Any] | Completeness,
) -> VerificationResult:
    """验证 completeness 的集合互斥/相等关系。

    检查：
    1. 所有集合种类在 CW_COMPLETENESS_KINDS 中
    2. pass/not_tested/failed 互斥
    3. extra = observed - required
    4. missing = required - observed
    5. remainder = not_tested ∪ failed ∪ missing ∪ extra（去重）
    6. remainder_count == len(remainder)
    7. verdict == PASS iff remainder_count == 0
    """
    if isinstance(completeness, Completeness):
        completeness = completeness.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    required = set(completeness.get("required_cell_keys", []))
    pass_keys = set(completeness.get("pass_cell_keys", []))
    not_tested = set(completeness.get("not_tested_cell_keys", []))
    failed = set(completeness.get("failed_cell_keys", []))
    extra = set(completeness.get("extra_cell_keys", []))
    missing = set(completeness.get("missing_cell_keys", []))
    remainder = set(completeness.get("remainder_cell_keys", []))
    remainder_count = completeness.get("remainder_count", -1)
    verdict = completeness.get("verdict", "")

    # 2. 互斥
    if pass_keys & not_tested:
        _err(EC.CW_COMPLETENESS_SETS_NOT_DISJOINT, "pass ∩ not_tested non-empty")
    if pass_keys & failed:
        _err(EC.CW_COMPLETENESS_SETS_NOT_DISJOINT, "pass ∩ failed non-empty")
    if not_tested & failed:
        _err(EC.CW_COMPLETENESS_SETS_NOT_DISJOINT, "not_tested ∩ failed non-empty")

    # 3. extra
    observed = pass_keys | not_tested | failed
    expected_extra = observed - required
    if extra != expected_extra:
        _err(
            EC.CW_COMPLETENESS_SETS_NOT_DISJOINT,
            f"extra mismatch: expected {sorted(expected_extra)}, got {sorted(extra)}",
        )

    # 4. missing
    expected_missing = required - observed
    if missing != expected_missing:
        _err(
            EC.CW_COMPLETENESS_SETS_NOT_DISJOINT,
            f"missing mismatch: expected {sorted(expected_missing)}, got {sorted(missing)}",
        )

    # 5. remainder
    expected_remainder = not_tested | failed | missing | extra
    if remainder != expected_remainder:
        _err(
            EC.CW_COMPLETENESS_SETS_NOT_DISJOINT,
            f"remainder mismatch: expected {sorted(expected_remainder)}, got {sorted(remainder)}",
        )

    # 6. remainder_count
    if remainder_count != len(remainder):
        _err(
            EC.CW_CELL_COMPLETENESS_REMAINDER_NONZERO,
            f"remainder_count {remainder_count} != len(remainder) {len(remainder)}",
        )

    # 7. verdict
    if verdict == "PASS":
        if remainder_count != 0:
            _err(
                EC.CW_COMPLETENESS_VERDICT_INVALID,
                f"verdict=PASS but remainder_count={remainder_count}",
            )
    elif verdict == "BLOCKED":
        if remainder_count == 0:
            _err(
                EC.CW_COMPLETENESS_VERDICT_INVALID,
                "verdict=BLOCKED but remainder_count=0",
            )
    else:
        _err(EC.CW_COMPLETENESS_VERDICT_INVALID, f"invalid completeness verdict: {verdict}")

    result_verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=result_verdict, error_codes=errors, details=details)


# ─── RoleQualificationMatrix ────────────────────────────────────────────


@dataclass
class RoleQualificationMatrix:
    """版本化资格矩阵。

    append-only：一旦构建不可修改。新版本必须创建新实例并设 supersedes_ref。
    content_hash = sha256(canonical_json(object with matrix_hash=null))。
    """

    matrix_id: str
    matrix_version: int
    role_type_registry_ref_and_hash: dict[str, str]
    runtime_manifest_ref_and_hash: dict[str, str]
    qualification_scope: str  # CANARY | PRODUCTION
    cells: tuple[RoleQualificationCell, ...]
    completeness: Completeness
    generated_at: str
    issuer_principal_id: str
    matrix_hash_algorithm: str
    matrix_hash: str
    supersedes_ref: dict[str, str] | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "matrix_id": self.matrix_id,
            "matrix_version": self.matrix_version,
            "role_type_registry_ref_and_hash": dict(self.role_type_registry_ref_and_hash),
            "runtime_manifest_ref_and_hash": dict(self.runtime_manifest_ref_and_hash),
            "qualification_scope": self.qualification_scope,
            "cells": [c.to_dict() for c in self.cells],
            "completeness": self.completeness.to_dict(),
            "generated_at": self.generated_at,
            "issuer_principal_id": self.issuer_principal_id,
            "matrix_hash_algorithm": self.matrix_hash_algorithm,
            "matrix_hash": self.matrix_hash,
            "supersedes_ref": dict(self.supersedes_ref) if self.supersedes_ref else None,
        }

    def get_cell_by_key(self, cell_key: str) -> RoleQualificationCell | None:
        """按 cell_key 查找 cell。"""
        for c in self.cells:
            if c.cell_key == cell_key:
                return c
        return None

    def get_cells_by_role(self, role_type_id: str) -> list[RoleQualificationCell]:
        """按 role_type_id 查找所有 cell。"""
        return [c for c in self.cells if c.role_type_id == role_type_id]

    def get_production_pass_cells(
        self, role_type_id: str
    ) -> list[RoleQualificationCell]:
        """获取某角色的 PRODUCTION PASS cell。"""
        return [
            c
            for c in self.cells
            if c.role_type_id == role_type_id
            and c.is_production
            and c.is_pass
            and not c.is_invalidated
        ]

    @property
    def is_production(self) -> bool:
        return self.qualification_scope == "PRODUCTION"

    @property
    def is_canary(self) -> bool:
        return self.qualification_scope == "CANARY"


def _matrix_hash_payload(matrix_dict: dict[str, Any]) -> str:
    """计算 matrix_hash。"""
    obj = dict(matrix_dict)
    obj["matrix_hash"] = None
    return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()


def build_role_qualification_matrix(
    *,
    matrix_id: str,
    matrix_version: int,
    role_type_registry_ref_and_hash: dict[str, str],
    runtime_manifest_ref_and_hash: dict[str, str],
    qualification_scope: str,
    cells: list[RoleQualificationCell],
    required_cell_keys: list[str],
    generated_at: str,
    issuer_principal_id: str,
    supersedes_ref: dict[str, str] | None = None,
    algorithm_ref_and_hash: dict[str, str] | None = None,
) -> RoleQualificationMatrix:
    """构建 RoleQualificationMatrix，自动计算 completeness 和 matrix_hash。"""
    algo_ref = algorithm_ref_and_hash or {
        "ref": "seven-completeness-algorithm-v1",
        "sha256": hashlib.sha256(b"seven-completeness-algorithm-v1").hexdigest(),
    }
    completeness = compute_completeness(
        required_cell_keys=required_cell_keys,
        cells=cells,
        algorithm_ref_and_hash=algo_ref,
    )
    matrix_dict = {
        "matrix_id": matrix_id,
        "matrix_version": matrix_version,
        "role_type_registry_ref_and_hash": dict(role_type_registry_ref_and_hash),
        "runtime_manifest_ref_and_hash": dict(runtime_manifest_ref_and_hash),
        "qualification_scope": qualification_scope,
        "cells": [c.to_dict() for c in cells],
        "completeness": completeness.to_dict(),
        "generated_at": generated_at,
        "issuer_principal_id": issuer_principal_id,
        "matrix_hash_algorithm": _MATRIX_HASH_ALGORITHM,
        "matrix_hash": None,
        "supersedes_ref": dict(supersedes_ref) if supersedes_ref else None,
    }
    matrix_hash = _matrix_hash_payload(matrix_dict)
    return RoleQualificationMatrix(
        matrix_id=matrix_id,
        matrix_version=matrix_version,
        role_type_registry_ref_and_hash=dict(role_type_registry_ref_and_hash),
        runtime_manifest_ref_and_hash=dict(runtime_manifest_ref_and_hash),
        qualification_scope=qualification_scope,
        cells=tuple(cells),
        completeness=completeness,
        generated_at=generated_at,
        issuer_principal_id=issuer_principal_id,
        matrix_hash_algorithm=_MATRIX_HASH_ALGORITHM,
        matrix_hash=matrix_hash,
        supersedes_ref=dict(supersedes_ref) if supersedes_ref else None,
    )


def verify_role_qualification_matrix(
    matrix: dict[str, Any] | RoleQualificationMatrix,
) -> VerificationResult:
    """验证 RoleQualificationMatrix 的 schema + semantic 合法性。

    检查：
    1. 精确字符串字段不含通配符
    2. ref_and_hash 结构合法
    3. qualification_scope 在合法枚举中
    4. 每个 cell 合法（verify_role_qualification_cell）
    5. cell_key 唯一
    6. completeness 合法（verify_completeness）
    7. matrix_hash 正确
    8. supersedes_ref 结构合法（如果存在）
    """
    if isinstance(matrix, RoleQualificationMatrix):
        matrix = matrix.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. 精确字符串
    for str_field in ("matrix_id", "issuer_principal_id"):
        val = matrix.get(str_field, "")
        if not _is_exact_string(val):
            _err(EC.CW_MATRIX_WILDCARD_REJECTED, f"{str_field} is not exact: {val!r}")

    # 2. ref_and_hash
    for ref_field in (
        "role_type_registry_ref_and_hash",
        "runtime_manifest_ref_and_hash",
    ):
        for code, detail in _check_ref_hash(matrix.get(ref_field, {}), ref_field):
            _err(code, detail)

    # 3. qualification_scope
    scope = matrix.get("qualification_scope", "")
    if scope not in CW_QUALIFICATION_SCOPES:
        _err(EC.CW_QUALIFICATION_SCOPE_INVALID, f"invalid qualification_scope: {scope}")

    # 4. cells
    cells = matrix.get("cells", [])
    if not isinstance(cells, list):
        _err(EC.REQUIRED_FIELD_MISSING, "cells is not a list")
    else:
        seen_keys: set[str] = set()
        for cell_dict in cells:
            cell_result = verify_role_qualification_cell(cell_dict)
            if not cell_result.passed:
                errors.extend(cell_result.error_codes)
                details.extend(cell_result.details)
            ck = cell_dict.get("cell_key", "") if isinstance(cell_dict, dict) else ""
            if ck in seen_keys:
                _err(EC.WORK_EVENT_DUPLICATE_EVENT_ID, f"duplicate cell_key: {ck}")
            seen_keys.add(ck)

    # 6. completeness
    comp_result = verify_completeness(matrix.get("completeness", {}))
    if not comp_result.passed:
        errors.extend(comp_result.error_codes)
        details.extend(comp_result.details)

    # 7. matrix_hash
    if matrix.get("matrix_hash_algorithm") != _MATRIX_HASH_ALGORITHM:
        _err(
            EC.CW_MATRIX_HASH_MISMATCH,
            f"unexpected matrix_hash_algorithm: {matrix.get('matrix_hash_algorithm')}",
        )
    computed_hash = _matrix_hash_payload(matrix)
    if matrix.get("matrix_hash") != computed_hash:
        _err(
            EC.CW_MATRIX_HASH_MISMATCH,
            f"matrix_hash mismatch: expected {computed_hash}, got {matrix.get('matrix_hash')}",
        )

    # 8. supersedes_ref
    supersedes = matrix.get("supersedes_ref")
    if supersedes is not None:
        for code, detail in _check_ref_hash(supersedes, "supersedes_ref"):
            _err(code, detail)

    result_verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=result_verdict, error_codes=errors, details=details)
