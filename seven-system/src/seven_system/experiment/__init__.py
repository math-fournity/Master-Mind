"""WP-EX1 P4/P5 Experiment — ExperimentPlan / ResourceContract / BranchSnapshot /
RandomizationPlan / ExperimentArm / ContrastSpec / P5ExperimentRunner /
RunArtifactBundle / ExperimentCapabilityReport.

本包实现 EX1 工作包：
- ResourceContract: 等资源合同（所有 arm 对等预算）
- BranchSnapshot: 共享前置状态（所有 arm 从同一 snapshot 出发）
- RandomizationPlan: 冻结随机化 block/seed（确定性重放）
- ExperimentArm: 单个实验对比臂
- ContrastSpec: 冻结对比规格（P4 预注册）
- ExperimentPlan: 冻结 P4 实验计划（不可变，启动后修改需新 plan）
- RunArtifactBundle: 每个 arm 的密封产物包
- P5ExperimentRunner: P5 实验运行器（使用 FakeHarnessAdapter）
- ExperimentCapabilityReport: P4/P5 实验能力报告

关键约束：
- SIDE_EFFECT_FREE：不写 DB、不写 Redis、不写 D 盘、不调用 live model、不启动真实 Solver
- Plan 冻结后不可变，启动后修改必须创建新 ExperimentPlan
- 所有 arm 必须等资源（EX_ARMS_NOT_EQUAL_RESOURCE）
- 所有 arm 必须共享 BranchSnapshot
- 随机化确定性重放（相同 seed → 相同 assignment）
- 所有 arms/negative/invalid 结果保留
- 预算超限 → BLOCK
- 原截断 bare baseline → BLOCK
- 对比必须预注册
"""

from .resource_contract import (
    ResourceContract,
    make_resource_contract,
    ResourceContractVerificationResult,
    verify_resource_contract,
    contracts_equal,
)
from .branch_snapshot import (
    BranchSnapshot,
    make_branch_snapshot,
    BranchSnapshotVerificationResult,
    verify_branch_snapshot,
)
from .randomization_plan import (
    RandomizationPlan,
    make_randomization_plan,
    RandomizationPlanVerificationResult,
    verify_randomization_plan,
    replay_randomization,
)
from .experiment_arm import (
    ExperimentArm,
    make_experiment_arm,
    ExperimentArmVerificationResult,
    verify_experiment_arm,
)
from .contrast_spec import (
    ContrastSpec,
    make_contrast_spec,
    ContrastSpecVerificationResult,
    verify_contrast_spec,
)
from .experiment_plan import (
    ExperimentPlan,
    make_experiment_plan,
    ExperimentPlanVerificationResult,
    verify_experiment_plan,
    check_plan_modified_after_start,
)
from .run_artifact_bundle import (
    RunArtifactBundle,
    make_run_artifact_bundle,
    RunArtifactBundleVerificationResult,
    verify_run_artifact_bundle,
)
from .p5_runner import (
    P5ExperimentRunner,
    P5ExperimentRunResult,
    ArmRunResult,
    verify_p5_run_result,
)
from .capability_report import (
    ExperimentCapabilityReport,
    build_experiment_capability_report,
    verify_experiment_capability_report,
    ExperimentCapabilityReportError,
    EXPERIMENT_REPORT_SCHEMA_VERSION,
)

__all__ = [
    # resource contract
    "ResourceContract",
    "make_resource_contract",
    "ResourceContractVerificationResult",
    "verify_resource_contract",
    "contracts_equal",
    # branch snapshot
    "BranchSnapshot",
    "make_branch_snapshot",
    "BranchSnapshotVerificationResult",
    "verify_branch_snapshot",
    # randomization plan
    "RandomizationPlan",
    "make_randomization_plan",
    "RandomizationPlanVerificationResult",
    "verify_randomization_plan",
    "replay_randomization",
    # experiment arm
    "ExperimentArm",
    "make_experiment_arm",
    "ExperimentArmVerificationResult",
    "verify_experiment_arm",
    # contrast spec
    "ContrastSpec",
    "make_contrast_spec",
    "ContrastSpecVerificationResult",
    "verify_contrast_spec",
    # experiment plan
    "ExperimentPlan",
    "make_experiment_plan",
    "ExperimentPlanVerificationResult",
    "verify_experiment_plan",
    "check_plan_modified_after_start",
    # run artifact bundle
    "RunArtifactBundle",
    "make_run_artifact_bundle",
    "RunArtifactBundleVerificationResult",
    "verify_run_artifact_bundle",
    # p5 runner
    "P5ExperimentRunner",
    "P5ExperimentRunResult",
    "ArmRunResult",
    "verify_p5_run_result",
    # capability report
    "ExperimentCapabilityReport",
    "build_experiment_capability_report",
    "verify_experiment_capability_report",
    "ExperimentCapabilityReportError",
    "EXPERIMENT_REPORT_SCHEMA_VERSION",
]
