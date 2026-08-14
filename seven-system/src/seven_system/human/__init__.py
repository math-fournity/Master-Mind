"""WP-HG0 HumanGate 子包：人工门控与签名验证。

消费 GV0 CompletionContractVerifier（不复制、不重写局部放宽版）。
本包实现：

- ActorRoster：actor_id → actor_type/roles/active 状态映射
- GateTypeRegistry：gate type → required roles / required signatures / separation policy
- KeyRegistry：签名密钥生命周期（注册→轮换→撤销→过期）
- HumanTask / HumanTaskPort：人工任务创建、分配、完成
- GateDecision：签名后的门控决定对象（payload hash + actor + signature envelope）
- HumanGateService：编排门控决定验证（验签、撤销、replay、职责分离、GV0 消费）

硬约束：
- ModelRole 不能自我批准（职责分离）
- Gate 决定必须签名（结构检查，与 SecurityContractVerifier 一致）
- 消费 GV0 CompletionContractVerifier 做状态命令验证，不复制
- SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB/D 盘/模型
"""

from .actor_roster import ActorRoster, ActorRecord
from .gate_type_registry import GateTypeRegistry, GateTypeSpec
from .key_lifecycle import KeyRegistry, KeyRecord
from .gate_decision import GateDecision, verify_gate_decision
from .human_task import HumanTask, HumanTaskPort, FakeHumanTaskPort
from .human_gate import HumanGateService

__all__ = [
    "ActorRoster",
    "ActorRecord",
    "GateTypeRegistry",
    "GateTypeSpec",
    "KeyRegistry",
    "KeyRecord",
    "GateDecision",
    "verify_gate_decision",
    "HumanTask",
    "HumanTaskPort",
    "FakeHumanTaskPort",
    "HumanGateService",
]
