"""WP-CS1 CaseLab Dual-Entry & P3C — case pack / admission / role freeze.

本包实现 P3C case role freeze 的全部对象：

对象目录：
- CaseRole：P3C 冻结的角色分配（positive/false-friend/boundary/unrelated）
- MechanismReview：机制合同审查
- RelationMapping：case 与 taxonomy 的关系映射
- CasePack：冻结的 case 包（problem/solution/mechanism/relation/roles）
- CasePackVersion：版本化的 case pack（supersedes_ref, immutable after signing）
- AdmissionDecision：HumanGate 签名的 case 入实验决定
- DualEntryFixture：双入口 fixture
- P3CVerificationReport：P3C 验签报告
- CaseLabCapabilityReport：CS1 能力报告

Pipeline：
- DualEntry：双入口路径编排器
  - natural_entry(): P2A/[P2B]+P3N → CasePack
  - generated_entry(): P3A+P3B → CasePack
- P3CVerifier：P3C case role freeze 验签器

硬约束（blocker）：
- Natural case forging draft → BLOCK
- Model self-signing role → BLOCK
- process-only entering result layer → BLOCK
- Missing evidence refs → BLOCK
- Hash mismatch in case pack → BLOCK
- Unsigned AdmissionDecision → BLOCK
- Role assignment without evidence → BLOCK

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB / model / solver_harness。
状态：IMPLEMENTED_PENDING_EVIDENCE
"""

from .case_role import (
    CaseRole,
    build_case_role,
    verify_case_role,
)
from .mechanism_review import (
    MechanismReview,
    build_mechanism_review,
    verify_mechanism_review,
)
from .relation_mapping import (
    RelationMapping,
    build_relation_mapping,
    verify_relation_mapping,
)
from .case_pack import (
    CasePack,
    CasePackVersion,
    build_case_pack,
    verify_case_pack,
    build_case_pack_version,
    verify_case_pack_version,
    freeze_case_pack_version,
    check_case_pack_immutable,
)
from .admission_decision import (
    AdmissionDecision,
    build_admission_decision,
    verify_admission_decision,
    check_process_only_not_in_result_layer,
)
from .dual_entry import (
    NaturalEntryEvidence,
    GeneratedEntryEvidence,
    DualEntryFixture,
    DualEntry,
    build_natural_entry_evidence,
    build_generated_entry_evidence,
    verify_natural_entry_evidence,
    verify_generated_entry_evidence,
    build_dual_entry_fixture,
    verify_dual_entry_fixture,
)
from .p3c_verifier import (
    P3CVerifier,
    P3CVerificationReport,
    check_natural_case_not_forged_draft,
    check_model_not_self_signing_role,
    check_process_only_excluded_from_result,
)
from .case_lab_capability_report import (
    CaseLabCapabilityReport,
    build_case_lab_capability_report,
    verify_case_lab_capability_report,
)

__all__ = [
    # CaseRole
    "CaseRole",
    "build_case_role",
    "verify_case_role",
    # MechanismReview
    "MechanismReview",
    "build_mechanism_review",
    "verify_mechanism_review",
    # RelationMapping
    "RelationMapping",
    "build_relation_mapping",
    "verify_relation_mapping",
    # CasePack / CasePackVersion
    "CasePack",
    "CasePackVersion",
    "build_case_pack",
    "verify_case_pack",
    "build_case_pack_version",
    "verify_case_pack_version",
    "freeze_case_pack_version",
    "check_case_pack_immutable",
    # AdmissionDecision
    "AdmissionDecision",
    "build_admission_decision",
    "verify_admission_decision",
    "check_process_only_not_in_result_layer",
    # DualEntry
    "NaturalEntryEvidence",
    "GeneratedEntryEvidence",
    "DualEntryFixture",
    "DualEntry",
    "build_natural_entry_evidence",
    "build_generated_entry_evidence",
    "verify_natural_entry_evidence",
    "verify_generated_entry_evidence",
    "build_dual_entry_fixture",
    "verify_dual_entry_fixture",
    # P3CVerifier
    "P3CVerifier",
    "P3CVerificationReport",
    "check_natural_case_not_forged_draft",
    "check_model_not_self_signing_role",
    "check_process_only_excluded_from_result",
    # CaseLabCapabilityReport
    "CaseLabCapabilityReport",
    "build_case_lab_capability_report",
    "verify_case_lab_capability_report",
]
