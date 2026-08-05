"""
auditor模块：Auditor角色——Phase 4新增启用

对应134号P4-ROLE-1。

127号§10.4-10.11 Auditor角色定义：
- 可见：冻结manifest/处理对照/输出/ground truth/证据/隔离记录（14个collection）
- 输入：冻结manifest/处理分配/所有实际Hint/提示前后事件状态/输出/ground truth/工具证据/哈希/隔离记录
- 输出：7项裁决（泄漏/越过卡点/数学进展/语言重复/副作用/归因/规则生命周期）
- 禁止：参与Hint设计或Solver答题

123号§607：角色边界必须落实为collection/visibility label/能力令牌，而不是只写在prompt里。
"""

from .auditor import Auditor, AuditVerdict, VerdictType
from .visibility_labels import VisibilityLabelChecker, VISIBILITY_MATRIX
from .capability_tokens import CapabilityToken, CapabilityTokenVerifier
from .blind_evaluator import BlindEvaluator, BlindEvalResult

__all__ = [
    "Auditor", "AuditVerdict", "VerdictType",
    "VisibilityLabelChecker", "VISIBILITY_MATRIX",
    "CapabilityToken", "CapabilityTokenVerifier",
    "BlindEvaluator", "BlindEvalResult",
]
