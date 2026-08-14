"""WP-VR1 P9 Verdict/Replay — 分轴 Verdict、checkpoint、replay/remainder。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P9 节和
docs/implementation/15-work-package-implementation-contracts.md WP-VR1：

P9 输出：
- Factory/Scientific/Scale 分轴 Machine Verdict
- SixGateVerdict 及 NOT_TESTED
- Human-readable Summary
- RuntimeCheckpoint
- EvidenceIndex/DAG
- cost 和 coverage delta
- next eligible work/coverage cells

Evidence replay 必须证明所有 planned 对象、attempt、artifact、audit、Gate
和 evidence 有且仅有合法归宿（remainder=0）。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from .rule_registry import (
    VerdictRuleRegistry,
    make_verdict_rule_registry,
    lookup_verdict_rule,
    verify_verdict_rule_registry,
    check_not_tested_not_pass as check_registry_not_tested_not_pass,
    check_fail_closed_unknown,
)
from .machine_verdict import (
    AxisVerdict,
    MachineVerdict,
    make_machine_verdict,
    verify_machine_verdict,
    check_no_pass_averaged_fail,
    check_not_tested_not_pass as check_verdict_not_tested_not_pass,
)
from .six_gate import (
    GateVerdict,
    SixGateVerdict,
    make_six_gate_verdict,
    verify_six_gate_verdict,
    check_gate_not_tested_not_pass,
)
from .evidence_index import (
    EvidenceEntry,
    EvidenceIndex,
    make_evidence_index,
    verify_evidence_index,
    check_evidence_index_in_p9,
    check_retraceable,
)
from .checkpoint import (
    VerdictCheckpoint,
    make_verdict_checkpoint,
    verify_verdict_checkpoint,
    verify_checkpoint_against_hashes,
    CHECKPOINT_STATES,
)
from .replay import (
    ReplayObject,
    ReplayResult,
    EvidenceReplay,
    make_evidence_replay,
    verify_evidence_replay,
    check_no_orphans,
    WorkPackageCompletion,
    CompletionContractRemainder,
    make_completion_contract_remainder,
    verify_completion_contract_remainder,
    PhaseSealStatus,
    FullChainRemainder,
    make_full_chain_remainder,
    verify_full_chain_remainder,
)
from .cost_coverage import (
    CostAggregation,
    CoverageCell,
    CostAndCoverageDelta,
    make_cost_and_coverage_delta,
    verify_cost_and_coverage_delta,
)
from .summary import (
    HumanReadableSummary,
    make_human_readable_summary,
    verify_human_readable_summary,
)
from .builder import (
    SealedDAG,
    VerdictBuilder,
    VerdictBuildResult,
)
from .capability_report import (
    VerdictCapabilityReportError,
    build_verdict_capability_report,
    verify_verdict_capability_report,
    VERDICT_REPORT_SCHEMA_VERSION,
    VERDICT_REPORT_SCOPE,
)

__all__ = [
    # rule_registry
    "VerdictRuleRegistry",
    "make_verdict_rule_registry",
    "lookup_verdict_rule",
    "verify_verdict_rule_registry",
    "check_registry_not_tested_not_pass",
    "check_fail_closed_unknown",
    # machine_verdict
    "AxisVerdict",
    "MachineVerdict",
    "make_machine_verdict",
    "verify_machine_verdict",
    "check_no_pass_averaged_fail",
    "check_verdict_not_tested_not_pass",
    # six_gate
    "GateVerdict",
    "SixGateVerdict",
    "make_six_gate_verdict",
    "verify_six_gate_verdict",
    "check_gate_not_tested_not_pass",
    # evidence_index
    "EvidenceEntry",
    "EvidenceIndex",
    "make_evidence_index",
    "verify_evidence_index",
    "check_evidence_index_in_p9",
    "check_retraceable",
    # checkpoint
    "VerdictCheckpoint",
    "make_verdict_checkpoint",
    "verify_verdict_checkpoint",
    "verify_checkpoint_against_hashes",
    "CHECKPOINT_STATES",
    # replay
    "ReplayObject",
    "ReplayResult",
    "EvidenceReplay",
    "make_evidence_replay",
    "verify_evidence_replay",
    "check_no_orphans",
    "WorkPackageCompletion",
    "CompletionContractRemainder",
    "make_completion_contract_remainder",
    "verify_completion_contract_remainder",
    "PhaseSealStatus",
    "FullChainRemainder",
    "make_full_chain_remainder",
    "verify_full_chain_remainder",
    # cost_coverage
    "CostAggregation",
    "CoverageCell",
    "CostAndCoverageDelta",
    "make_cost_and_coverage_delta",
    "verify_cost_and_coverage_delta",
    # summary
    "HumanReadableSummary",
    "make_human_readable_summary",
    "verify_human_readable_summary",
    # builder
    "SealedDAG",
    "VerdictBuilder",
    "VerdictBuildResult",
    # capability_report
    "VerdictCapabilityReportError",
    "build_verdict_capability_report",
    "verify_verdict_capability_report",
    "VERDICT_REPORT_SCHEMA_VERSION",
    "VERDICT_REPORT_SCOPE",
]
