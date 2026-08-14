"""ImplementationCapabilityRegistry — R5 深度补全：文档/机器真值双向对账。

文档第 10 节：
> 下列四处必须表达同一个事实：
> 1. work-package-board.md
> 2. implementation-status.md
> 3. seven.py capabilities
> 4. 真实 CLI/operator registry 和 import/call graph

建议生成机器化的 ImplementationCapabilityRegistry 或复用目标 OperatorCommandRegistry，
由 CLI 和状态文档投影共同消费。

本模块定义 ImplementationCapabilityRegistry 和一致性检查器。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


@dataclass
class CapabilityEntry:
    """单项能力记录。"""
    capability_id: str
    capability_version: str
    implementation_status: str  # NOT_IMPLEMENTED / IMPLEMENTED_PENDING_EVIDENCE / READY_FOR_AUDIT / AUDITED_PASS
    entry_point_reachable: bool
    effect_class: str  # SIDE_EFFECT_FREE / D_VOLUME_WRITE / DB_WRITE / REMOTE_MODEL / SOLVER_LAUNCH
    required_gate: str  # 无 / HumanGate / EEA / Permit
    capability_report_ref: str = ""
    capability_report_hash: str = ""
    verified_scope: str = ""
    explicit_nonclaims: list[str] = field(default_factory=list)


@dataclass
class ImplementationCapabilityRegistry:
    """ImplementationCapabilityRegistry — 机器化能力注册表。

    对每项能力至少记录：
    - capability ID/version
    - implementation status
    - 入口是否可达
    - effect class
    - 所需 Gate/Permit
    - capability report ref/hash
    - 已验证 scope
    - explicit nonclaims

    未知或列表沉默一律 NOT_IMPLEMENTED。
    """

    _capabilities: dict[str, CapabilityEntry] = field(default_factory=dict)

    def register(self, entry: CapabilityEntry) -> None:
        """注册一项能力。"""
        self._capabilities[entry.capability_id] = entry

    def get(self, capability_id: str) -> CapabilityEntry | None:
        """获取一项能力。"""
        return self._capabilities.get(capability_id)

    def all_capabilities(self) -> dict[str, CapabilityEntry]:
        """返回所有已注册能力。"""
        return dict(self._capabilities)

    def get_status(self, capability_id: str) -> str:
        """获取能力状态——未知一律 NOT_IMPLEMENTED。"""
        entry = self._capabilities.get(capability_id)
        if entry is None:
            return "NOT_IMPLEMENTED"
        return entry.implementation_status

    def is_reachable(self, capability_id: str) -> bool:
        """检查能力入口是否可达。"""
        entry = self._capabilities.get(capability_id)
        if entry is None:
            return False
        return entry.entry_point_reachable


# ─── 默认能力注册表 ─────────────────────────────────────────────────────

def create_default_registry() -> ImplementationCapabilityRegistry:
    """创建默认能力注册表——反映当前实现真值。

    未知或列表沉默一律 NOT_IMPLEMENTED。
    """
    registry = ImplementationCapabilityRegistry()

    # 已实现的能力
    registry.register(CapabilityEntry(
        capability_id="P1_DRY_RUN",
        capability_version="v0.1",
        implementation_status="IMPLEMENTED_PENDING_EVIDENCE",
        entry_point_reachable=True,
        effect_class="SIDE_EFFECT_FREE",
        required_gate="无",
        explicit_nonclaims=["不构成 live capability"],
    ))

    registry.register(CapabilityEntry(
        capability_id="COMPLETION_CONTRACT_VERIFIER",
        capability_version="v1",
        implementation_status="IMPLEMENTED_PENDING_EVIDENCE",
        entry_point_reachable=True,
        effect_class="SIDE_EFFECT_FREE",
        required_gate="无",
        explicit_nonclaims=["不构成 AUDITED_PASS"],
    ))

    registry.register(CapabilityEntry(
        capability_id="HUMAN_GATE_ED25519",
        capability_version="v1",
        implementation_status="IMPLEMENTED_PENDING_EVIDENCE",
        entry_point_reachable=True,
        effect_class="SIDE_EFFECT_FREE",
        required_gate="无",
        explicit_nonclaims=["公钥分发机制仍需外部信任根"],
    ))

    registry.register(CapabilityEntry(
        capability_id="DB1I_AUTHORIZATION_CHAIN",
        capability_version="v1",
        implementation_status="IMPLEMENTED_PENDING_EVIDENCE",
        entry_point_reachable=True,
        effect_class="SIDE_EFFECT_FREE",
        required_gate="HumanGate + EEA + Permit",
        explicit_nonclaims=["不构成 DB1I 的 AUDITED_PASS"],
    ))

    registry.register(CapabilityEntry(
        capability_id="WORK_PACKAGE_STATE_SERVICE",
        capability_version="v1",
        implementation_status="IMPLEMENTED_PENDING_EVIDENCE",
        entry_point_reachable=True,
        effect_class="SIDE_EFFECT_FREE",
        required_gate="无",
        explicit_nonclaims=["board 投影是内存状态，不持久化"],
    ))

    registry.register(CapabilityEntry(
        capability_id="ADAPTER_REGISTRY",
        capability_version="v1",
        implementation_status="IMPLEMENTED_PENDING_EVIDENCE",
        entry_point_reachable=True,
        effect_class="SIDE_EFFECT_FREE",
        required_gate="HumanGate + LiveRunPermit",
        explicit_nonclaims=["实际 adapter 代码仍为 SIDE_EFFECT_FREE mock"],
    ))

    # 未实现的能力——明确列出
    for cap_id in [
        "VLT0_D_CAS", "DB_ARANGO_LIVE", "RT_REDIS_LIVE",
        "SOLVER_HARNESS_LIVE", "MODEL_ROLE_CODEX_LIVE", "MODEL_ROLE_DEVIN_LIVE",
        "TARGET_SOLVER_PORT", "DEVIN_SOLVER_ADAPTER",
        "CASE_PACK", "EXPERIMENT_PLAN", "RUN_AUDIT", "EVIDENCE_RECORD",
        "REVISION_PROPOSAL", "PROMOTION", "ACTIVE_LEARNING",
        "AUTHORING_BAKEOFF", "WP_QA0", "WP_QA1",
    ]:
        registry.register(CapabilityEntry(
            capability_id=cap_id,
            capability_version="v0",
            implementation_status="NOT_IMPLEMENTED",
            entry_point_reachable=False,
            effect_class="SIDE_EFFECT_FREE",
            required_gate="无",
            explicit_nonclaims=["能力不存在，也没有隐藏入口"],
        ))

    return registry


# ─── 一致性检查器 ───────────────────────────────────────────────────────

@dataclass
class TruthConsistencyChecker:
    """文档/机器真值双向对账检查器。

    检查 board / implementation-status / capabilities / CLI 之间的一致性。
    """

    registry: ImplementationCapabilityRegistry

    def check_board_consistency(
        self,
        board_entries: dict[str, str],
    ) -> VerificationResult:
        """检查 board 与 registry 的一致性。

        board_entries: {wp_id: status_string}
        """
        errors: list[EC] = []
        details: list[str] = []

        for cap_id, board_status in board_entries.items():
            registry_status = self.registry.get_status(cap_id)
            if board_status != registry_status:
                # 检查是否是已知的状态映射差异
                if board_status == "IMPLEMENTED_PENDING_EVIDENCE" and registry_status == "NOT_IMPLEMENTED":
                    errors.append(EC.WP_OVERCLAIM)
                    details.append(
                        f"{cap_id}: board says IMPLEMENTED_PENDING_EVIDENCE but registry says NOT_IMPLEMENTED"
                    )
                elif board_status == "READY_FOR_AUDIT" and registry_status != "READY_FOR_AUDIT":
                    errors.append(EC.WP_OVERCLAIM)
                    details.append(
                        f"{cap_id}: board says READY_FOR_AUDIT but registry says {registry_status}"
                    )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)

    def check_capabilities_consistency(
        self,
        cli_capabilities: list[str],
    ) -> VerificationResult:
        """检查 CLI capabilities 与 registry 的一致性。

        cli_capabilities: CLI 报告的能力 ID 列表
        """
        errors: list[EC] = []
        details: list[str] = []

        registry_caps = set(self.registry.all_capabilities().keys())
        cli_caps = set(cli_capabilities)

        # CLI 报告了 registry 中不存在的能力
        for cap in cli_caps - registry_caps:
            errors.append(EC.WP_OVERCLAIM)
            details.append(f"CLI reports {cap} but registry has no such capability")

        # CLI 沉默的能力——一律 NOT_IMPLEMENTED
        for cap in registry_caps - cli_caps:
            entry = self.registry.get(cap)
            if entry and entry.implementation_status != "NOT_IMPLEMENTED":
                # 已实现但 CLI 没列出——也是不一致
                details.append(
                    f"CLI silent on {cap} (status={entry.implementation_status}) — "
                    f"silence means NOT_IMPLEMENTED"
                )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)

    def check_no_stub_as_real(
        self,
        declared_real: list[str],
    ) -> VerificationResult:
        """检查 stub/fake 没有被声明为真实能力。

        文档第 10 节：
        > fake/stub adapter存在就写真实adapter implemented
        """
        errors: list[EC] = []
        details: list[str] = []

        for cap_id in declared_real:
            entry = self.registry.get(cap_id)
            if entry and "stub" in " ".join(entry.explicit_nonclaims).lower():
                errors.append(EC.WP_OVERCLAIM)
                details.append(f"{cap_id} is declared real but is a stub/fake")

            if entry and "mock" in " ".join(entry.explicit_nonclaims).lower():
                errors.append(EC.WP_OVERCLAIM)
                details.append(f"{cap_id} is declared real but is a mock")

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)
