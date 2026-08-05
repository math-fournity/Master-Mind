"""
微包——完成一个研究动作所需的定义、接口、工具或Hint

对应135号P5-1.4 + 123号§29。

微包特点：
- 保存：完成一个研究动作所需的定义、接口、工具或Hint
- 使用方式：每轮增量注入
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class MicroPack:
    """
    微包——完成一个研究动作所需的最小数据包。

    每轮增量注入Solver上下文。
    """
    pack_id: str
    action_type: str  # define/prove/compute/search/verify/transport
    obligation_id: str  # 服务的义务ID
    items: List[Dict[str, Any]] = field(default_factory=list)  # 定义/接口/工具/Hint
    token_cost: int = 0  # token成本
    source: str = ""  # 来源

    def to_dict(self) -> dict:
        return {
            "pack_id": self.pack_id,
            "action_type": self.action_type,
            "obligation_id": self.obligation_id,
            "items": self.items,
            "token_cost": self.token_cost,
            "source": self.source,
        }


class MicroPackGenerator:
    """
    微包生成器（135号P5-1.4）。

    冻结声明：
    - 微包每轮增量注入
    - 微包只包含完成一个研究动作所需的最小内容
    """

    def __init__(self):
        self._packs: Dict[str, MicroPack] = {}

    def generate(
        self,
        pack_id: str,
        action_type: str,
        obligation_id: str,
        items: List[Dict[str, Any]],
        token_cost: int = 0,
        source: str = "",
    ) -> MicroPack:
        """
        生成微包。

        边界情况：微包为空、微包过大
        """
        pack = MicroPack(
            pack_id=pack_id,
            action_type=action_type,
            obligation_id=obligation_id,
            items=items,
            token_cost=token_cost,
            source=source,
        )
        self._packs[pack_id] = pack
        return pack

    def inject(self, workspace_id: str, pack: MicroPack) -> Dict[str, Any]:
        """将微包增量注入工作区"""
        return {
            "workspace_id": workspace_id,
            "injected_pack": pack.to_dict(),
            "injection_type": "incremental",
        }

    def get_by_id(self, pack_id: str) -> Optional[MicroPack]:
        return self._packs.get(pack_id)

    def check_no_preload_future_route(self, pack: MicroPack) -> bool:
        """
        验证微包不预载未来路线（plan第197行 + P5-EXIT-2）。

        边界情况：微包预载了未来路线（应被拒绝——每次Hint只携带完成一个研究动作所需的内容）
        """
        # 微包只应包含完成当前一个研究动作所需的内容
        # 检查items中是否有超出当前action_type的内容
        preload_keywords = ["完整解法", "complete_solution", "最终答案", "final_answer",
                           "ground_truth", "truth_vault", "完整证明路径", "complete_proof_path"]
        for item in pack.items:
            content = item.get("content", "").lower() if isinstance(item, dict) else str(item).lower()
            for kw in preload_keywords:
                if kw.lower() in content:
                    return False
        return True

    def count(self) -> int:
        return len(self._packs)
