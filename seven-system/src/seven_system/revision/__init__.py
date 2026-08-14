"""WP-RV1 P8 NO_CHANGE/Revision — failure localization / NoChangeDecision /
RevisionProposal / HoldoutConsumption / CandidateRelease / ProspectiveEvaluation /
RevisionPolicy / EvidenceImmutability / RevisionCapabilityReport.

本包实现 RV1 工作包（P8 NO_CHANGE/Revision）：
- ProvenanceSnapshot: P8 开始时对 sealed P7 EvidenceRecord 集合冻结的只读快照
- FailureLocalization: 第一独立故障定位（哪一层出错），引用 EvidenceRecord by hash
- NoChangeDecision: 签名决定无需修订，不解封 holdout
- RevisionProposal: 受控修订提案，fit/regression 计划、candidate freeze、一次性 prospective、两 HumanGate
- HoldoutConsumption: holdout 消费追踪（viewed 立即 consumed，fit≠confirmation）
- CandidateRelease: 冻结 candidate（不得自批）
- ProspectiveEvaluation: 一次性 prospective 确认（不得复用已 viewed holdout）
- RevisionPolicy: 冻结的修订策略
- EvidenceImmutability: 旧证据不得修改
- RevisionCapabilityReport: P8 修订能力报告

关键约束（blocker）：
- SIDE_EFFECT_FREE：不写 DB、不写 Redis、不写 D 盘、不调用 live model、不启动真实 Solver
- P8 读取 ProvenanceSnapshot，不读取尚未生成的最终 EvidenceIndex（P9 才生成）
- 同一证据不得同时用作 fit 和 confirmation（fit=confirmation → BLOCK）
- viewed holdout 立即 consumed，不得反复偷看
- 单例 split（同一 case 既作 fit 又作 test）→ BLOCK
- candidate 不得自批
- 旧证据不得修改（ProvenanceSnapshot 只读）
- NoChangeDecision 不解封 holdout
- RevisionProposal 需要两个 HumanGate 批准
- 状态：IMPLEMENTED_PENDING_EVIDENCE
"""

from __future__ import annotations

from .provenance import (
    ProvenanceSnapshot,
    ProvenanceSnapshotVerificationResult,
    make_provenance_snapshot,
    verify_provenance_snapshot,
    check_provenance_readonly,
    check_no_evidence_index_in_provenance,
)
from .localization import (
    FailureLocalization,
    FailureLocalizationVerificationResult,
    make_failure_localization,
    verify_failure_localization,
)
from .no_change import (
    NoChangeDecision,
    NoChangeDecisionVerificationResult,
    make_no_change_decision,
    verify_no_change_decision,
    check_nochange_does_not_unseal_holdout,
)
from .revision_proposal import (
    RevisionProposal,
    RevisionProposalVerificationResult,
    make_revision_proposal,
    verify_revision_proposal,
    check_revision_two_human_gates,
)
from .holdout import (
    HoldoutView,
    HoldoutConsumption,
    HoldoutConsumptionVerificationResult,
    make_holdout_consumption,
    verify_holdout_consumption,
    record_holdout_view,
    check_fit_not_confirmation,
    check_no_repeated_peek,
    check_no_single_case_split,
)
from .candidate import (
    CandidateRelease,
    CandidateReleaseVerificationResult,
    make_candidate_release,
    verify_candidate_release,
    check_candidate_not_self_approved,
)
from .prospective import (
    ProspectiveEvaluation,
    ProspectiveEvaluationVerificationResult,
    make_prospective_evaluation,
    verify_prospective_evaluation,
    check_prospective_one_time,
    check_prospective_no_reuse_viewed_holdout,
)
from .policy import (
    RevisionPolicy,
    RevisionPolicyVerificationResult,
    make_revision_policy,
    verify_revision_policy,
)
from .immutability import (
    check_old_evidence_not_modified,
    check_evidence_immutability,
)
from .capability_report import (
    RevisionCapabilityReportError,
    build_revision_capability_report,
    verify_revision_capability_report,
    REVISION_REPORT_SCHEMA_VERSION,
    REVISION_REPORT_SCOPE,
)
from .boundary import (
    check_no_evidence_index_in_p8,
    check_p8_output_boundary,
)

__all__ = [
    # provenance
    "ProvenanceSnapshot",
    "ProvenanceSnapshotVerificationResult",
    "make_provenance_snapshot",
    "verify_provenance_snapshot",
    "check_provenance_readonly",
    "check_no_evidence_index_in_provenance",
    # localization
    "FailureLocalization",
    "FailureLocalizationVerificationResult",
    "make_failure_localization",
    "verify_failure_localization",
    # no change
    "NoChangeDecision",
    "NoChangeDecisionVerificationResult",
    "make_no_change_decision",
    "verify_no_change_decision",
    "check_nochange_does_not_unseal_holdout",
    # revision proposal
    "RevisionProposal",
    "RevisionProposalVerificationResult",
    "make_revision_proposal",
    "verify_revision_proposal",
    "check_revision_two_human_gates",
    # holdout
    "HoldoutView",
    "HoldoutConsumption",
    "HoldoutConsumptionVerificationResult",
    "make_holdout_consumption",
    "verify_holdout_consumption",
    "record_holdout_view",
    "check_fit_not_confirmation",
    "check_no_repeated_peek",
    "check_no_single_case_split",
    # candidate
    "CandidateRelease",
    "CandidateReleaseVerificationResult",
    "make_candidate_release",
    "verify_candidate_release",
    "check_candidate_not_self_approved",
    # prospective
    "ProspectiveEvaluation",
    "ProspectiveEvaluationVerificationResult",
    "make_prospective_evaluation",
    "verify_prospective_evaluation",
    "check_prospective_one_time",
    "check_prospective_no_reuse_viewed_holdout",
    # policy
    "RevisionPolicy",
    "RevisionPolicyVerificationResult",
    "make_revision_policy",
    "verify_revision_policy",
    # immutability
    "check_old_evidence_not_modified",
    "check_evidence_immutability",
    # capability report
    "RevisionCapabilityReportError",
    "build_revision_capability_report",
    "verify_revision_capability_report",
    "REVISION_REPORT_SCHEMA_VERSION",
    "REVISION_REPORT_SCOPE",
    # boundary
    "check_no_evidence_index_in_p8",
    "check_p8_output_boundary",
]
