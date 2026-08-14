"""WP-QA0 Controlled Dual-Carrier Authoring — P3A 出题链。

本子包实现 P3A 出题链的全部对象和状态机：

对象目录（来自 04-object-and-schema-catalog.md）：
- MechanismContract：冻结机制定义（core + boundary），content_hash 覆盖
- CoverageCell：数学分支/迁移距离/案例关系/证据使用位置
- AuthoringBrief：受控生成目标/禁止捷径/预算，引用 MechanismContract + CoverageCell
- QuestionDraftVersion：append-only 草案，题面变化 = 新版本
- AdversarialReview：题面对抗性审查（statement-only），独立于 VerificationDossier
- VerificationDossier：数学正确性验证，独立于 AdversarialReview
- QuestionRelease：不可变发布题目，G-Q-RELEASE 签名，需两种审查都通过
- AuthoringEvaluationPack：冻结评估包（校准/资格/blinding/metrics/stop/forbidden lane）
- AuthoringBootstrapInputPack：HumanGate 批准的启动包，不依赖 CasePack

状态机与编排：
- AuthoringStateChain：P3A 状态机 brief→architect→draft→editor→verifier→gate→release
- AuthoringRoleRouter：预冻结角色路由，不合格角色 = BLOCK

Bakeoff-A：
- BakeoffAScoring：盲评评分（作者身份隐去，无 bare 指标，无 Solver）

能力与失效：
- AuthoringCapabilityReport：QA0 能力报告（无 Solver/Redis/bare）
- InvalidationPropagation：题面变化 → 下游全部失效

硬约束（blocker）：
- 未签 bootstrap 输入 → BLOCK
- file-only live 旁路（无 canonical DB/CAS）→ BLOCK
- 缺任一 canonical report → BLOCK
- 修题不失效 → BLOCK
- 作者泄漏 → BLOCK
- bare 指标偷入 → BLOCK
- retry-until-desired → BLOCK
- 不合格角色路由 → BLOCK

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB/D 盘/模型。
状态：IMPLEMENTED_PENDING_EVIDENCE
"""

from .mechanism_contract import (
    MechanismContract,
    build_mechanism_contract,
    verify_mechanism_contract,
)
from .coverage_cell import (
    CoverageCell,
    build_coverage_cell,
    verify_coverage_cell,
)
from .authoring_brief import (
    AuthoringBrief,
    build_authoring_brief,
    verify_authoring_brief,
)
from .question_draft import (
    QuestionDraftVersion,
    build_question_draft_version,
    verify_question_draft_version,
)
from .adversarial_review import (
    AdversarialReview,
    build_adversarial_review,
    verify_adversarial_review,
)
from .verification_dossier import (
    VerificationDossier,
    build_verification_dossier,
    verify_verification_dossier,
)
from .question_release import (
    QuestionRelease,
    build_question_release,
    verify_question_release,
)
from .evaluation_pack import (
    AuthoringEvaluationPack,
    build_authoring_evaluation_pack,
    verify_authoring_evaluation_pack,
)
from .bootstrap_input import (
    AuthoringBootstrapInputPack,
    build_authoring_bootstrap_input_pack,
    verify_authoring_bootstrap_input_pack,
)
from .state_chain import (
    AuthoringStateChain,
    AuthoringRoleExecutor,
)
from .role_router import (
    AuthoringRoleRouter,
    RoleRoutingEntry,
)
from .bakeoff_a import (
    BakeoffAScoring,
    BakeoffASubmission,
    BakeoffAScoringReport,
    verify_bakeoff_a_scoring_report,
)
from .capability_report import (
    AuthoringCapabilityReport,
    build_authoring_capability_report,
    verify_authoring_capability_report,
)
from .invalidation import (
    InvalidationPropagation,
    InvalidationRecord,
)

__all__ = [
    "MechanismContract",
    "build_mechanism_contract",
    "verify_mechanism_contract",
    "CoverageCell",
    "build_coverage_cell",
    "verify_coverage_cell",
    "AuthoringBrief",
    "build_authoring_brief",
    "verify_authoring_brief",
    "QuestionDraftVersion",
    "build_question_draft_version",
    "verify_question_draft_version",
    "AdversarialReview",
    "build_adversarial_review",
    "verify_adversarial_review",
    "VerificationDossier",
    "build_verification_dossier",
    "verify_verification_dossier",
    "QuestionRelease",
    "build_question_release",
    "verify_question_release",
    "AuthoringEvaluationPack",
    "build_authoring_evaluation_pack",
    "verify_authoring_evaluation_pack",
    "AuthoringBootstrapInputPack",
    "build_authoring_bootstrap_input_pack",
    "verify_authoring_bootstrap_input_pack",
    "AuthoringStateChain",
    "AuthoringRoleExecutor",
    "AuthoringRoleRouter",
    "RoleRoutingEntry",
    "BakeoffAScoring",
    "BakeoffASubmission",
    "BakeoffAScoringReport",
    "verify_bakeoff_a_scoring_report",
    "AuthoringCapabilityReport",
    "build_authoring_capability_report",
    "verify_authoring_capability_report",
    "InvalidationPropagation",
    "InvalidationRecord",
]
