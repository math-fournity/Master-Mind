"""
验证门：F_t→V_t分离

对应132号P2-4。

123号§15冻结声明：
- 临时假设进入F_t，不进入V_t（P2-2.COMP3）
- 被拒绝路线进入D_t，不与representation共用R（P2-2.COMP4）

123号§31冻结声明：
- 只有满足该命题类型预先指定的验证门，命题才进入V_t（P2-5.COMP4）

边界情况：
- F_t内容进入V_t时无证据引用（触发R-3停止条件）
- 验证门未通过但尝试进入V_t（应被拒绝）
- V_t内容被尝试移回F_t（应被拒绝——V_t原则上单调增长）
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

from .evidence import (
    EvidenceStore, EvidenceKind, EvidencePolarity, EvidenceStatus,
    DerivedEpistemicState,
)
from .workspace_store import WorkspaceStore
from .obligation import ObligationType


# 按义务类型定义验证门（123号§23 + 127号§6）
# 每种义务类型需要不同的验证证据类型
# 注意：这里用ObligationType（127号§4的10种），不是TaskType（123号§14的9种）
OBLIGATION_TYPE_VERIFICATION_GATE: Dict[ObligationType, List[EvidenceKind]] = {
    ObligationType.PROVE: [EvidenceKind.FORMAL_PROOF, EvidenceKind.SYMBOLIC],
    ObligationType.REFUTE: [EvidenceKind.COUNTEREXAMPLE, EvidenceKind.FORMAL_PROOF],
    ObligationType.CONSTRUCT: [EvidenceKind.SYMBOLIC, EvidenceKind.NUMERICAL],
    ObligationType.COMPUTE: [EvidenceKind.NUMERICAL, EvidenceKind.SYMBOLIC],
    ObligationType.SEARCH: [EvidenceKind.LITERATURE, EvidenceKind.NUMERICAL],
    ObligationType.COMPARE: [EvidenceKind.LITERATURE, EvidenceKind.SYMBOLIC],
    ObligationType.EVALUATE: [EvidenceKind.LITERATURE, EvidenceKind.HUMAN_AUDIT],
    ObligationType.INTERFACE: [EvidenceKind.FORMAL_PROOF, EvidenceKind.SYMBOLIC],  # 跨表示运输保真
    ObligationType.VERIFICATION: [EvidenceKind.FORMAL_PROOF, EvidenceKind.COUNTEREXAMPLE],
    ObligationType.VALUE: [EvidenceKind.LITERATURE, EvidenceKind.HUMAN_AUDIT],  # 方向判断
}


class VerificationGate:
    """
    验证门：控制F_t内容进入V_t。

    冻结声明：
    - F_t内容进入V_t必须带证据引用（P2-4.COMP）
    - 只有满足验证门的命题才进入V_t（P2-5.COMP4）
    - V_t原则上单调增长（不回退到F_t）
    """

    def __init__(
        self,
        evidence_store: EvidenceStore,
        workspace_store: WorkspaceStore,
    ):
        self.evidence_store = evidence_store
        self.workspace_store = workspace_store

    def get_required_kinds(self, obl_type: ObligationType) -> List[EvidenceKind]:
        """获取义务类型对应的验证门证据类型。"""
        return OBLIGATION_TYPE_VERIFICATION_GATE.get(obl_type, [EvidenceKind.FORMAL_PROOF])

    def check_can_promote(
        self,
        claim_id: str,
        obl_type: ObligationType,
    ) -> Dict[str, Any]:
        """
        检查F_t中的候选是否可以提升到V_t。

        提升条件：
        1. 有证据引用（P2-4.COMP）
        2. 验证门通过（P2-5.COMP4）
        3. 派生认识状态不是refute_only或mixed（反驳证据不能进入V_t）
        """
        # 1. 检查证据存在
        evidence_list = self.evidence_store.get_evidence_for_claim(claim_id)
        has_evidence = len(evidence_list) > 0

        if not has_evidence:
            return {
                "can_promote": False,
                "reason": "无证据引用——F_t内容进入V_t必须带证据引用（P2-4.COMP）",
                "would_trigger_r3": True,  # 触发R-3停止条件
            }

        # 2. 检查验证门
        required_kinds = self.get_required_kinds(obl_type)
        gate = self.evidence_store.check_verification_gate(
            claim_id, required_kinds, EvidencePolarity.SUPPORT,
        )

        if not gate["gate_passed"]:
            return {
                "can_promote": False,
                "reason": f"验证门未通过——需要{required_kinds}类型的verified支持证据（P2-5.COMP4）",
                "gate_check": gate,
            }

        # 3. 检查派生认识状态
        state = self.evidence_store.compute_derived_state(claim_id)
        if state["derived_state"] in (
            DerivedEpistemicState.REFUTE_ONLY.value,
            DerivedEpistemicState.MIXED.value,
        ):
            return {
                "can_promote": False,
                "reason": f"派生认识状态为{state['derived_state']}——反驳证据存在，不能进入V_t",
                "derived_state": state,
            }

        # 全部通过
        return {
            "can_promote": True,
            "reason": "验证门通过，有支持证据，无反驳证据",
            "gate_check": gate,
            "derived_state": state,
        }

    def promote_to_v_t(
        self,
        workspace_id: str,
        claim_id: str,
        obl_type: ObligationType,
        claim_type: str = "lemma",  # premise/lemma/tool_result
    ) -> Dict[str, Any]:
        """
        将F_t中的候选提升到V_t。

        创建新的工作区快照（W_t只能由版本化Reducer派生，P2-2.COMP2）。
        """
        # 1. 检查是否可以提升
        check = self.check_can_promote(claim_id, obl_type)
        if not check["can_promote"]:
            return {
                "success": False,
                "reason": check["reason"],
                "workspace_id": None,
            }

        # 2. 读取当前工作区
        ws = self.workspace_store.read_workspace(workspace_id)
        if ws is None:
            return {
                "success": False,
                "reason": f"工作区{workspace_id}不存在",
                "workspace_id": None,
            }

        # 3. 从F_t移除，添加到V_t
        f_t = ws.get("F_t", {})
        v_t = ws.get("V_t", {})

        # 从F_t的candidates中移除
        candidates = f_t.get("candidates", [])
        if claim_id in candidates:
            candidates.remove(claim_id)
        # 从F_t的temporary_assumptions中移除
        temp_assumptions = f_t.get("temporary_assumptions", [])
        if claim_id in temp_assumptions:
            temp_assumptions.remove(claim_id)

        # 添加到V_t
        if claim_type == "premise":
            v_t.setdefault("verified_premises", []).append(claim_id)
        elif claim_type == "lemma":
            v_t.setdefault("verified_lemmas", []).append(claim_id)
        elif claim_type == "tool_result":
            v_t.setdefault("verified_tool_results", []).append(claim_id)

        # 4. 创建新工作区快照
        new_ws_id = f"{workspace_id}_promoted_{claim_id}"
        ws_dict = {
            "V_t": v_t,
            "F_t": f_t,
            "O_t": ws.get("O_t", {}),
            "R_t": ws.get("R_t", {}),
            "D_t": ws.get("D_t", {}),
            "E_t": ws.get("E_t", {}),
        }
        new_key = self.workspace_store.create_workspace_from_dict(
            new_ws_id,
            ws.get("task_id", ""),
            ws_dict,
            reducer_version="v1_promote",
        )

        # 5. 验证V_t/F_t分离
        sep = self.workspace_store.verify_w_t_separation(new_ws_id)
        if not sep.get("comp3_temp_not_in_v", True):
            return {
                "success": False,
                "reason": "V_t/F_t分离验证失败——临时假设混入V_t",
                "workspace_id": new_key,
            }

        return {
            "success": True,
            "reason": "提升成功",
            "workspace_id": new_key,
            "claim_id": claim_id,
            "claim_type": claim_type,
            "separation_check": sep,
        }
