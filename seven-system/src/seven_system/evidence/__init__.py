"""WP-EV1 P7 Contrast Evidence — ContrastAggregator / EvidenceRecord /
AnalysisMethodRegistry / MultiplicityRuleRegistry / StoppingRuleRegistry /
EvidenceStatusRegistry / MissingnessReport / CostDimension / EvidenceSeal /
EvidenceCapabilityReport.

本包实现 EV1 工作包（P7 Contrast Evidence）：
- AnalysisMethodRegistry: 冻结 P7 估计器注册表（P4 冻结，禁止运行后换）
- MultiplicityRuleRegistry: 冻结多重性规则注册表（primary/Holm/exploratory）
- StoppingRuleRegistry: 冻结停止规则注册表（禁止 run until significant）
- EvidenceStatusRegistry: 冻结 Evidence status 注册表（5 个 status 机械派生）
- MissingnessReport: 缺失报告（invalid 不得填 0）
- CostDimension: 成本维度（provider_billed_amount UNOBSERVABLE 时不填值）
- EvidenceRecord: 对比级证据记录（只有 contrast 级可写 supports/contradicts）
- ContrastAggregator: 按预注册 contrast 聚合 P5 arm 结果 + P6 RunAudits
- EvidenceSeal: P7 seal over EvidenceRecord 集合（root hash + seal hash）
- EvidenceCapabilityReport: P7 能力报告

关键约束：
- SIDE_EFFECT_FREE：不写 DB、不写 Redis、不写 D 盘、不调用 live model、不启动真实 Solver
- 只有 contrast 级 EvidenceRecord 可对 Tell causal claim 写 supports/contradicts
- Case-family 层只能聚合既有 contrast records 扩展 scope，不能创建新 causal claim
- invalid 结果不得填 0
- 同一 cluster 不得双计
- 单 episode 不得用作 causal claim support
- 估计器必须从 P4 冻结 registry 选择，运行后不得换
- P7 不生成 EvidenceIndex 或 ProvenanceSnapshot（P8/P9 才生成）
- 状态：IMPLEMENTED_PENDING_EVIDENCE
"""

from __future__ import annotations

from .registries import (
    AnalysisMethodEntry,
    AnalysisMethodRegistry,
    MultiplicityRuleEntry,
    MultiplicityRuleRegistry,
    StoppingRuleEntry,
    StoppingRuleRegistry,
    EvidenceStatusEntry,
    EvidenceStatusRegistry,
    build_default_analysis_method_registry,
    build_default_multiplicity_rule_registry,
    build_default_stopping_rule_registry,
    build_default_evidence_status_registry,
    verify_analysis_method_registry,
    verify_multiplicity_rule_registry,
    verify_stopping_rule_registry,
    verify_evidence_status_registry,
    check_estimator_in_registry,
    check_estimator_not_swapped,
    check_multiplicity_rule_in_registry,
    check_exploratory_not_in_family,
    check_stopping_rule_in_registry,
    check_no_run_until_significant,
    check_evidence_status_valid,
)
from .missingness_and_cost import (
    MissingnessEntry,
    MissingnessReport,
    CostDimension,
    make_missingness_report,
    verify_missingness_report,
    check_invalid_not_filled_zero,
    make_cost_dimension,
    verify_cost_dimension,
    check_cost_completeness,
)
from .evidence_record import (
    ArmEvidenceInput,
    EstimatorOutput,
    EvidenceRecord,
    EvidenceRecordVerificationResult,
    make_evidence_record,
    verify_evidence_record,
    ContrastAggregator,
    check_episode_not_used_as_support,
    check_cluster_not_double_counted,
)
from .seal_and_report import (
    EvidenceSeal,
    EvidenceSealVerificationResult,
    make_evidence_seal,
    verify_evidence_seal,
    compute_root_hash,
    compute_seal_hash,
    check_no_evidence_index_in_p7,
    check_no_provenance_snapshot_in_p7,
    check_p7_output_boundary,
    EvidenceCapabilityReportError,
    build_evidence_capability_report,
    verify_evidence_capability_report,
    EVIDENCE_REPORT_SCHEMA_VERSION,
    EVIDENCE_REPORT_SCOPE,
)

__all__ = [
    # registries
    "AnalysisMethodEntry",
    "AnalysisMethodRegistry",
    "MultiplicityRuleEntry",
    "MultiplicityRuleRegistry",
    "StoppingRuleEntry",
    "StoppingRuleRegistry",
    "EvidenceStatusEntry",
    "EvidenceStatusRegistry",
    "build_default_analysis_method_registry",
    "build_default_multiplicity_rule_registry",
    "build_default_stopping_rule_registry",
    "build_default_evidence_status_registry",
    "verify_analysis_method_registry",
    "verify_multiplicity_rule_registry",
    "verify_stopping_rule_registry",
    "verify_evidence_status_registry",
    "check_estimator_in_registry",
    "check_estimator_not_swapped",
    "check_multiplicity_rule_in_registry",
    "check_exploratory_not_in_family",
    "check_stopping_rule_in_registry",
    "check_no_run_until_significant",
    "check_evidence_status_valid",
    # missingness and cost
    "MissingnessEntry",
    "MissingnessReport",
    "CostDimension",
    "make_missingness_report",
    "verify_missingness_report",
    "check_invalid_not_filled_zero",
    "make_cost_dimension",
    "verify_cost_dimension",
    "check_cost_completeness",
    # evidence record
    "ArmEvidenceInput",
    "EstimatorOutput",
    "EvidenceRecord",
    "EvidenceRecordVerificationResult",
    "make_evidence_record",
    "verify_evidence_record",
    "ContrastAggregator",
    "check_episode_not_used_as_support",
    "check_cluster_not_double_counted",
    # seal and report
    "EvidenceSeal",
    "EvidenceSealVerificationResult",
    "make_evidence_seal",
    "verify_evidence_seal",
    "compute_root_hash",
    "compute_seal_hash",
    "check_no_evidence_index_in_p7",
    "check_no_provenance_snapshot_in_p7",
    "check_p7_output_boundary",
    "EvidenceCapabilityReportError",
    "build_evidence_capability_report",
    "verify_evidence_capability_report",
    "EVIDENCE_REPORT_SCHEMA_VERSION",
    "EVIDENCE_REPORT_SCOPE",
]
