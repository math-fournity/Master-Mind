"""VerdictRuleRegistry — 冻结的 Evidence status → P9 四轴 verdict 映射。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

P9 Verdict 必须从 sealed P0-P8 DAG 构建。Evidence status 到分轴 verdict
的映射是冻结的、确定性的。未知组合必须 fail-closed（返回 BLOCKED）。

关键约束（blocker）：
- 未知 verdict rule 组合不 fail-closed → VR_VERDICT_RULE_UNKNOWN_NOT_FAIL_CLOSED
- NOT_TESTED 不得映射为 PASS → VR_NOT_TESTED_AS_PASS

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EV_EVIDENCE_STATUSES,
    VR_VERDICT_AXES,
    VR_VERDICT_RULE_STATUSES,
    VR_VERDICT_STATUSES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_REGISTRY_SCHEMA_ID = "seven/verdict-rule-registry"
_REGISTRY_SCHEMA_VERSION = 1
_REGISTRY_HASH_ALGORITHM = "sha256(canonical-json-with-registry_hash-null)"


# 冻结映射：evidence_status → {axis → verdict_status}
# 这是确定性的、完整的映射。未知组合 fail-closed → BLOCKED。
#
# 规则逻辑：
# - SUPPORTS → Factory PASS, Scientific PASS, Scale NOT_TESTED
# - CONTRADICTS → Factory PASS (system complete), Scientific FAIL, Scale NOT_TESTED
# - DOES_NOT_SUPPORT → Factory PASS, Scientific FAIL, Scale NOT_TESTED
# - INCONCLUSIVE_DUE_TO_PROTOCOL → Factory PASS, Scientific NOT_TESTED, Scale NOT_TESTED
# - NOT_TESTED → Factory NOT_TESTED, Scientific NOT_TESTED, Scale NOT_TESTED
# - 未知 → BLOCKED (fail-closed)
_FROZEN_RULE_TABLE: dict[str, dict[str, str]] = {
    "SUPPORTS": {
        "FACTORY": "PASS",
        "SCIENTIFIC": "PASS",
        "SCALE": "NOT_TESTED",
    },
    "CONTRADICTS": {
        "FACTORY": "PASS",
        "SCIENTIFIC": "FAIL",
        "SCALE": "NOT_TESTED",
    },
    "DOES_NOT_SUPPORT": {
        "FACTORY": "PASS",
        "SCIENTIFIC": "FAIL",
        "SCALE": "NOT_TESTED",
    },
    "INCONCLUSIVE_DUE_TO_PROTOCOL": {
        "FACTORY": "PASS",
        "SCIENTIFIC": "NOT_TESTED",
        "SCALE": "NOT_TESTED",
    },
    "NOT_TESTED": {
        "FACTORY": "NOT_TESTED",
        "SCIENTIFIC": "NOT_TESTED",
        "SCALE": "NOT_TESTED",
    },
}


@dataclass(frozen=True)
class VerdictRuleRegistry:
    """冻结的 Evidence status → P9 四轴 verdict 映射注册表。

    字段：
        registry_id: 唯一标识
        rule_table: 冻结映射表 {evidence_status: {axis: verdict_status}}
        frozen: 是否冻结（必须 True）
        hash_algorithm: 哈希算法
        registry_hash: 注册表自身内容哈希
    """

    registry_id: str = "seven-verdict-rule-registry-v1"
    rule_table: tuple[tuple[str, tuple[tuple[str, str], ...]], ...] = ()
    frozen: bool = True
    hash_algorithm: str = _REGISTRY_HASH_ALGORITHM
    registry_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _REGISTRY_SCHEMA_ID,
            "schema_version": _REGISTRY_SCHEMA_VERSION,
            "registry_id": self.registry_id,
            "rule_table": {
                status: dict(pairs) for status, pairs in self.rule_table
            },
            "frozen": self.frozen,
            "hash_algorithm": self.hash_algorithm,
            "registry_hash": self.registry_hash,
        }

    def compute_registry_hash(self) -> str:
        d = self.to_dict()
        d["registry_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.registry_hash == self.compute_registry_hash()

    @property
    def is_frozen(self) -> bool:
        return self.frozen


def _build_rule_table_tuple() -> tuple[tuple[str, tuple[tuple[str, str], ...]], ...]:
    """将 _FROZEN_RULE_TABLE 转为不可变 tuple 形式。"""
    result: list[tuple[str, tuple[tuple[str, str], ...]]] = []
    for status in sorted(_FROZEN_RULE_TABLE):
        axis_map = _FROZEN_RULE_TABLE[status]
        pairs = tuple(sorted(axis_map.items()))
        result.append((status, pairs))
    return tuple(result)


def make_verdict_rule_registry() -> VerdictRuleRegistry:
    """构建冻结的 VerdictRuleRegistry。"""
    rule_table = _build_rule_table_tuple()
    registry = VerdictRuleRegistry(
        registry_id="seven-verdict-rule-registry-v1",
        rule_table=rule_table,
        frozen=True,
    )
    import dataclasses
    return dataclasses.replace(
        registry, registry_hash=registry.compute_registry_hash()
    )


def _get_rule_table() -> dict[str, dict[str, str]]:
    """返回可变的规则表副本。"""
    return {
        status: dict(axis_map)
        for status, axis_map in _FROZEN_RULE_TABLE.items()
    }


def lookup_verdict_rule(
    registry: VerdictRuleRegistry,
    evidence_status: str,
) -> dict[str, str]:
    """查询单个 evidence_status 的分轴 verdict 映射。

    未知组合 fail-closed → 返回全 BLOCKED。
    """
    table = registry.to_dict()["rule_table"]
    if evidence_status not in table:
        # fail-closed: 未知组合返回全 BLOCKED
        return {axis: "BLOCKED" for axis in VR_VERDICT_AXES}
    return dict(table[evidence_status])


def verify_verdict_rule_registry(
    registry: VerdictRuleRegistry,
) -> VerificationResult:
    """验证 VerdictRuleRegistry。

    blocker：
    - 未冻结 → REQUIRED_FIELD_MISSING
    - NOT_TESTED 映射为 PASS → VR_NOT_TESTED_AS_PASS
    - 未知组合不 fail-closed → VR_VERDICT_RULE_UNKNOWN_NOT_FAIL_CLOSED
    - registry_hash 不匹配 → VR_VERDICT_HASH_MISMATCH
    - 轴或状态不在合法集合 → VR_AXIS_INVALID / VR_GATE_INVALID
    """
    errors: list[EC] = []
    details: list[str] = []

    d = registry.to_dict()
    if d.get("schema_id") != _REGISTRY_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_REGISTRY_SCHEMA_ID}")

    if not registry.frozen:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("VerdictRuleRegistry must be frozen")

    table = d["rule_table"]

    # 验证每个已知 evidence_status 的映射
    for status, axis_map in table.items():
        if status not in EV_EVIDENCE_STATUSES:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"unknown evidence_status in rule table: {status}")
            continue
        for axis, verdict in axis_map.items():
            if axis not in VR_VERDICT_AXES:
                errors.append(EC.VR_AXIS_INVALID)
                details.append(f"unknown axis {axis} for status {status}")
            if verdict not in VR_VERDICT_STATUSES:
                errors.append(EC.VR_GATE_INVALID)
                details.append(
                    f"unknown verdict status {verdict} for {status}/{axis}"
                )
            # NOT_TESTED 不得映射为 PASS
            if status == "NOT_TESTED" and verdict == "PASS":
                errors.append(EC.VR_NOT_TESTED_AS_PASS)
                details.append(
                    "NOT_TESTED evidence status must not map to PASS"
                )

    # 验证 fail-closed：未知组合必须返回 BLOCKED
    unknown_result = lookup_verdict_rule(registry, "__UNKNOWN_STATUS__")
    for axis, verdict in unknown_result.items():
        if verdict != "BLOCKED":
            errors.append(EC.VR_VERDICT_RULE_UNKNOWN_NOT_FAIL_CLOSED)
            details.append(
                f"unknown evidence status must fail-closed to BLOCKED, "
                f"got {verdict} for {axis}"
            )

    # 验证所有已知 evidence_status 都在表中
    for status in EV_EVIDENCE_STATUSES:
        if status not in table:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"evidence_status {status} missing from rule table")

    # registry_hash
    if not registry.registry_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("registry_hash is empty")
    elif registry.registry_hash != registry.compute_registry_hash():
        errors.append(EC.VR_VERDICT_HASH_MISMATCH)
        details.append("VerdictRuleRegistry registry_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )


def check_not_tested_not_pass(registry: VerdictRuleRegistry) -> VerificationResult:
    """检查 NOT_TESTED 不被映射为 PASS。"""
    errors: list[EC] = []
    details: list[str] = []
    table = registry.to_dict()["rule_table"]
    not_tested_map = table.get("NOT_TESTED", {})
    for axis, verdict in not_tested_map.items():
        if verdict == "PASS":
            errors.append(EC.VR_NOT_TESTED_AS_PASS)
            details.append(
                f"NOT_TESTED maps to PASS for axis {axis} — forbidden"
            )
    verdict_result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict_result,
        error_codes=errors,
        details=details,
    )


def check_fail_closed_unknown(registry: VerdictRuleRegistry) -> VerificationResult:
    """检查未知组合 fail-closed。"""
    errors: list[EC] = []
    details: list[str] = []
    unknown_result = lookup_verdict_rule(registry, "__UNKNOWN_STATUS__")
    for axis, verdict in unknown_result.items():
        if verdict != "BLOCKED":
            errors.append(EC.VR_VERDICT_RULE_UNKNOWN_NOT_FAIL_CLOSED)
            details.append(
                f"unknown status must fail-closed to BLOCKED, "
                f"got {verdict} for {axis}"
            )
    verdict_result = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict_result,
        error_codes=errors,
        details=details,
    )
