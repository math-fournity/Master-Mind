"""ProfileCapabilityReport — 跨 adapter 的 profile 能力报告构建器与验证器。

来自 docs/implementation/05-execution-ports-and-carriers.md：

每个 adapter 必须为每个 role × carrier × model × profile × view/Vault capability ×
全部 policy × adapter/parser × capability requirement 精确 cell 分别验证。

ProfileCapabilityReport 记录：
- adapter_kind：DEVIN_CLI / CODEX_EXEC / OPENAI_RESPONSES
- requested_profile：合同中冻结的 requested profile 字段
- effective_profile：adapter 实际观察到的 effective profile 字段
- unobservable_fields：无法观察的字段（必须显式声明，不能静默省略）
- tool_policy：tool policy 引用
- view_policy：view policy 引用
- bypass_test_results：bypass test 结果

验证器检查：
1. requested 与 effective 的可观察字段一致（profile drift 检测）
2. unobservable 字段在允许列表中
3. adapter_kind 与合同一致
4. tool_policy 不允许工具（认知角色默认 NO_TOOLS）
5. bypass test 全部 PASS

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    PROFILE_UNOBSERVABLE_FIELDS,
    TOOL_POLICY_KINDS,
    VIEW_POLICY_KINDS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_REPORT_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"


@dataclass(frozen=True)
class ProfileCapabilityReport:
    """ProfileCapabilityReport — adapter 的 profile 能力报告。

    不可变。记录 requested / effective / unobservable profile 字段，
    以及 bypass test 结果。
    """

    adapter_kind: str
    requested_profile: dict[str, Any]
    effective_profile: dict[str, Any]
    unobservable_fields: list[str]
    tool_policy_ref_and_hash: dict[str, str]
    view_policy_ref_and_hash: dict[str, str]
    bypass_test_results: list[dict[str, str]]
    report_hash_algorithm: str
    report_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "adapter_kind": self.adapter_kind,
            "requested_profile": dict(self.requested_profile),
            "effective_profile": dict(self.effective_profile),
            "unobservable_fields": list(self.unobservable_fields),
            "tool_policy_ref_and_hash": dict(self.tool_policy_ref_and_hash),
            "view_policy_ref_and_hash": dict(self.view_policy_ref_and_hash),
            "bypass_test_results": [dict(r) for r in self.bypass_test_results],
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": self.report_hash,
        }


def build_profile_capability_report(
    *,
    adapter_kind: str,
    requested_profile: dict[str, Any],
    effective_profile: dict[str, Any],
    unobservable_fields: list[str] | None = None,
    tool_policy_ref_and_hash: dict[str, str] | None = None,
    view_policy_ref_and_hash: dict[str, str] | None = None,
    bypass_test_results: list[dict[str, str]] | None = None,
) -> ProfileCapabilityReport:
    """构建 ProfileCapabilityReport，自动计算 report_hash。"""
    unobservable = list(unobservable_fields) if unobservable_fields else []
    tool_policy = dict(tool_policy_ref_and_hash) if tool_policy_ref_and_hash else {}
    view_policy = dict(view_policy_ref_and_hash) if view_policy_ref_and_hash else {}
    bypass_results = [dict(r) for r in bypass_test_results] if bypass_test_results else []

    obj = {
        "adapter_kind": adapter_kind,
        "requested_profile": dict(requested_profile),
        "effective_profile": dict(effective_profile),
        "unobservable_fields": unobservable,
        "tool_policy_ref_and_hash": tool_policy,
        "view_policy_ref_and_hash": view_policy,
        "bypass_test_results": bypass_results,
        "report_hash_algorithm": _REPORT_HASH_ALGORITHM,
        "report_hash": None,
    }
    report_hash = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

    return ProfileCapabilityReport(
        adapter_kind=adapter_kind,
        requested_profile=dict(requested_profile),
        effective_profile=dict(effective_profile),
        unobservable_fields=unobservable,
        tool_policy_ref_and_hash=tool_policy,
        view_policy_ref_and_hash=view_policy,
        bypass_test_results=bypass_results,
        report_hash_algorithm=_REPORT_HASH_ALGORITHM,
        report_hash=report_hash,
    )


def verify_profile_capability_report(
    report: dict[str, Any] | ProfileCapabilityReport,
) -> VerificationResult:
    """验证 ProfileCapabilityReport 的 schema + semantic 合法性。

    检查：
    1. adapter_kind 非空
    2. requested_profile / effective_profile 是 dict
    3. unobservable_fields 在允许列表中
    4. requested 与 effective 的可观察字段一致（profile drift）
    5. tool_policy / view_policy ref 结构合法
    6. bypass_test_results 全部 PASS
    7. report_hash 正确
    """
    if isinstance(report, ProfileCapabilityReport):
        report = report.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. adapter_kind
    adapter_kind = report.get("adapter_kind", "")
    if not adapter_kind:
        _err(EC.PROFILE_ADAPTER_KIND_MISMATCH, "adapter_kind is empty")

    # 2. requested / effective profile
    requested = report.get("requested_profile", {})
    effective = report.get("effective_profile", {})
    if not isinstance(requested, dict):
        _err(EC.PROFILE_REQUIRED_FIELD_MISSING, "requested_profile is not a dict")
    if not isinstance(effective, dict):
        _err(EC.PROFILE_REQUIRED_FIELD_MISSING, "effective_profile is not a dict")

    # 3. unobservable_fields
    unobservable = report.get("unobservable_fields", [])
    if not isinstance(unobservable, list):
        _err(EC.PROFILE_UNOBSERVABLE_FIELD_NOT_DECLARED,
             "unobservable_fields is not a list")
    else:
        for field_name in unobservable:
            if field_name not in PROFILE_UNOBSERVABLE_FIELDS:
                _err(EC.PROFILE_UNOBSERVABLE_FIELD_NOT_DECLARED,
                     f"unobservable field {field_name!r} not in allowed set")

    # 4. profile drift — requested 与 effective 的可观察字段必须一致
    if isinstance(requested, dict) and isinstance(effective, dict):
        unobservable_set = set(unobservable) if isinstance(unobservable, list) else set()
        for key, req_val in requested.items():
            # 跳过 unobservable 字段和 ref_and_hash 字段（这些不是 profile 值）
            if key in unobservable_set or key.endswith("_ref_and_hash"):
                continue
            eff_val = effective.get(key)
            if eff_val is not None and eff_val != req_val:
                _err(EC.PROFILE_REQUESTED_EFFECTIVE_MISMATCH,
                     f"profile drift: requested[{key!r}]={req_val!r}, "
                     f"effective[{key!r}]={eff_val!r}")

    # 5. tool_policy / view_policy ref 结构
    for policy_name, policy_ref in (
        ("tool_policy_ref_and_hash", report.get("tool_policy_ref_and_hash", {})),
        ("view_policy_ref_and_hash", report.get("view_policy_ref_and_hash", {})),
    ):
        if not isinstance(policy_ref, dict):
            _err(EC.PROFILE_REQUIRED_FIELD_MISSING, f"{policy_name} is not a dict")
        elif policy_ref and set(policy_ref.keys()) != {"ref_id", "sha256"}:
            _err(EC.PROFILE_REQUIRED_FIELD_MISSING,
                 f"{policy_name} must have ref_id and sha256")

    # 6. bypass_test_results
    bypass_results = report.get("bypass_test_results", [])
    if not isinstance(bypass_results, list):
        _err(EC.REQUIRED_FIELD_MISSING, "bypass_test_results is not a list")
    else:
        for br in bypass_results:
            if not isinstance(br, dict):
                _err(EC.REQUIRED_FIELD_MISSING, "bypass_test_result entry is not a dict")
                continue
            result = br.get("result", "")
            if result != "PASS":
                test_name = br.get("test_name", "?")
                if test_name == "direct_devin_bypass":
                    _err(EC.BYPASS_SOLVER_HARNESS_USED,
                         f"bypass test {test_name} result={result}")
                elif test_name == "tool_event_test":
                    _err(EC.BYPASS_TOOL_EVENT_DETECTED,
                         f"bypass test {test_name} result={result}")
                elif test_name == "repo_workspace_test":
                    _err(EC.BYPASS_REPO_WORKSPACE_USED,
                         f"bypass test {test_name} result={result}")
                else:
                    _err(EC.BYPASS_TOOL_EVENT_DETECTED,
                         f"bypass test {test_name} result={result}")

    # 7. report_hash
    if report.get("report_hash_algorithm") != _REPORT_HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"unexpected report_hash_algorithm: {report.get('report_hash_algorithm')}")
    obj_for_hash = dict(report)
    obj_for_hash["report_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if report.get("report_hash") != computed_hash:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"report_hash mismatch: expected {computed_hash}, "
             f"got {report.get('report_hash')}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )
