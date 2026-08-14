"""WP-QA1 Generated Bare Admission & Bakeoff-B — P3B bare admission pipeline.

本子包实现 P3B problem-only bare admission 和 Bakeoff-B 的全部对象：

对象目录：
- BareBaseline：问题级 bare 分布，冻结 with QuestionRelease ref + hash
- BareQualificationResult：从 bare 结果得出的资格判定，引用 BareBaseline by hash
- RunArtifactBundle：P3B 运行资产包
- BakeoffBPlan：Bakeoff-B 冻结计划
- BakeoffBScoringReport：Bakeoff-B 盲评评分报告（含 bare 维度）
- BareResultRetentionRecord：bare 结果保留记录
- BareCapabilityReport：QA1 能力报告

Pipeline：
- P3BBareAdmission：QuestionRelease → TargetSolverPort (problem-only) →
  bare results → BareBaseline + BareQualificationResult

Retention：
- BareResultRetention：所有 bare 结果（成功 AND 失败）保留

硬约束（blocker）：
- Tell/Hint sneaked into bare submission → BLOCK
- Question modified after bare results → BLOCK
- Successful questions selectively deleted → BLOCK
- Retry-until-fail → BLOCK
- bare results flow back to modify question draft → BLOCK
- A/B calibration objects entering P5/P7 confirmatory Evidence → BLOCK
- Missing QuestionRelease ref → BLOCK
- P5 claim in bare capability report → BLOCK

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB / model / solver_harness。
状态：IMPLEMENTED_PENDING_EVIDENCE
"""

from .bare_baseline import (
    BareAttemptResult,
    BareBaseline,
    build_bare_baseline,
    verify_bare_baseline,
)
from .bare_qualification import (
    ProblemQualification,
    BareQualificationResult,
    build_bare_qualification_result,
    verify_bare_qualification_result,
)
from .p3b_bare_admission import (
    RunArtifactBundle,
    P3BBareAdmission,
    check_no_tell_hint_in_submission,
    check_question_not_modified_after_bare,
    check_no_successful_question_deleted,
    check_no_retry_until_fail,
    check_no_bare_result_flowback_to_draft,
)
from .bakeoff_b_plan import (
    BakeoffBPlan,
    build_bakeoff_b_plan,
    verify_bakeoff_b_plan,
)
from .bakeoff_b_scoring import (
    BakeoffBSubmission,
    BakeoffBScoringReport,
    BakeoffBScoring,
    verify_bakeoff_b_scoring_report,
    check_no_calibration_in_confirmatory_evidence,
)
from .bare_result_retention import (
    BareResultRetentionRecord,
    BareResultRetention,
    verify_bare_result_retention_record,
)
from .bare_capability_report import (
    BareCapabilityReport,
    build_bare_capability_report,
    verify_bare_capability_report,
)

__all__ = [
    # BareBaseline
    "BareAttemptResult",
    "BareBaseline",
    "build_bare_baseline",
    "verify_bare_baseline",
    # BareQualificationResult
    "ProblemQualification",
    "BareQualificationResult",
    "build_bare_qualification_result",
    "verify_bare_qualification_result",
    # P3BBareAdmission
    "RunArtifactBundle",
    "P3BBareAdmission",
    "check_no_tell_hint_in_submission",
    "check_question_not_modified_after_bare",
    "check_no_successful_question_deleted",
    "check_no_retry_until_fail",
    "check_no_bare_result_flowback_to_draft",
    # BakeoffBPlan
    "BakeoffBPlan",
    "build_bakeoff_b_plan",
    "verify_bakeoff_b_plan",
    # BakeoffBScoring
    "BakeoffBSubmission",
    "BakeoffBScoringReport",
    "BakeoffBScoring",
    "verify_bakeoff_b_scoring_report",
    "check_no_calibration_in_confirmatory_evidence",
    # BareResultRetention
    "BareResultRetentionRecord",
    "BareResultRetention",
    "verify_bare_result_retention_record",
    # BareCapabilityReport
    "BareCapabilityReport",
    "build_bare_capability_report",
    "verify_bare_capability_report",
]
