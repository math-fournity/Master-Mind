"""
P7-1.1 类型化表示映射——127号§5 Representation schema完整实现。

127号§5冻结的12字段：
  rep_id, source_form, target_form, map_type, domain, preconditions,
  forward_transport, backward_transport, preserved_invariants,
  lost_information, soundness_obligation, evidence

map_type 6种枚举（127号§5逐字）：
  equivalence / encoding / reduction / relaxation / duality / functor_candidate

4个冻结声明（127号§5）：
  1. 运输只在对应义务通过后成立，不能因边名叫equivalence就自动成立
  2. 首版不宣称已构成范畴——升级需恒等变换+可组合边的复合+结合律+结构保持证明
  3. 只有可逆且复合封闭的子图才可称为groupoid
  4. 普通跨领域边不自动成为表示变换

母本细节补充（系统探讨.md§8.2位置一，阶段1母本回溯发现）：
  核心启发："不在当前表示中硬解，而是沿等价关系把问题运输到另一个空间"
  运输对象：定理、不变量、证明义务、解法策略（母本明确列出4个）
  跨表示映射例子（母本§8.2位置一逐字）：
    矩阵表示 ↔ 模表示
    组合表示 ↔ 拓扑表示
    整数方程 ↔ 椭圆曲线
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class MapType(Enum):
    """127号§5 map_type 6种枚举（逐字核对）。"""
    EQUIVALENCE = "equivalence"        # 等价
    ENCODING = "encoding"              # 编码
    REDUCTION = "reduction"            # 归约
    RELAXATION = "relaxation"          # 松弛
    DUALITY = "duality"                # 对偶
    FUNCTOR_CANDIDATE = "functor_candidate"  # 函子化候选

    @classmethod
    def from_string(cls, s: str) -> "MapType":
        """从字符串构造，不存在的map_type抛ValueError。"""
        for mt in cls:
            if mt.value == s:
                return mt
        raise ValueError(f"map_type不存在: {s}，合法值为 {[mt.value for mt in cls]}")


# 母本§8.2位置一的3个跨表示映射例子（逐字保留）
MOTHER_CROSS_REP_EXAMPLES = [
    {"source": "矩阵表示", "target": "模表示", "map_type": "equivalence"},
    {"source": "组合表示", "target": "拓扑表示", "map_type": "equivalence"},
    {"source": "整数方程", "target": "椭圆曲线", "map_type": "encoding"},
]


@dataclass
class RepresentationMap:
    """
    127号§5 Representation schema——12字段全部可操作。

    123号§19："首版只假设存在一个类型化表示变换图，不预先宣称它已经构成范畴。"
    母本§8.2："不在当前表示中硬解，而是沿等价关系把问题运输到另一个空间。"
    """
    rep_id: str                              # 唯一标识符
    source_form: str                         # 源表示（如"整数方程"）
    target_form: str                         # 目标表示（如"椭圆曲线"）
    map_type: MapType                        # 6种枚举之一
    domain: str                              # 数学领域
    preconditions: List[str] = field(default_factory=list)  # 前置条件
    forward_transport: str = ""              # 正向运输规则
    backward_transport: str = ""             # 逆向运输规则（可选）
    preserved_invariants: List[str] = field(default_factory=list)  # 保留量
    lost_information: List[str] = field(default_factory=list)      # 信息损失
    soundness_obligation: str = ""           # 保真义务ID（指向Obligation）
    evidence: List[str] = field(default_factory=list)              # 证据ID列表

    def __post_init__(self):
        """构造后验证——map_type必须是合法枚举。"""
        if isinstance(self.map_type, str):
            self.map_type = MapType.from_string(self.map_type)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "rep_id": self.rep_id,
            "source_form": self.source_form,
            "target_form": self.target_form,
            "map_type": self.map_type.value,
            "domain": self.domain,
            "preconditions": list(self.preconditions),
            "forward_transport": self.forward_transport,
            "backward_transport": self.backward_transport,
            "preserved_invariants": list(self.preserved_invariants),
            "lost_information": list(self.lost_information),
            "soundness_obligation": self.soundness_obligation,
            "evidence": list(self.evidence),
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "RepresentationMap":
        return cls(
            rep_id=d["rep_id"],
            source_form=d["source_form"],
            target_form=d["target_form"],
            map_type=MapType.from_string(d["map_type"]),
            domain=d["domain"],
            preconditions=d.get("preconditions", []),
            forward_transport=d.get("forward_transport", ""),
            backward_transport=d.get("backward_transport", ""),
            preserved_invariants=d.get("preserved_invariants", []),
            lost_information=d.get("lost_information", []),
            soundness_obligation=d.get("soundness_obligation", ""),
            evidence=d.get("evidence", []),
        )

    def has_forward_transport(self) -> bool:
        """检查是否有正向运输规则。"""
        return bool(self.forward_transport)

    def has_backward_transport(self) -> bool:
        """检查是否有逆向运输规则（可选）。"""
        return bool(self.backward_transport)

    def check_preconditions(self, satisfied: List[str]) -> bool:
        """检查前置条件是否全部满足。"""
        satisfied_set = set(satisfied)
        return all(p in satisfied_set for p in self.preconditions)

    def is_checkable(self) -> bool:
        """
        P7-1.3：是否为可检查的表示映射。

        123号§19："首版只实现可检查的表示映射与soundness obligation。"
        可检查 = 有forward_transport + 有soundness_obligation。
        """
        return self.has_forward_transport() and bool(self.soundness_obligation)


class RepresentationMapStore:
    """
    表示映射存储——管理多个RepresentationMap。

    127号§5冻结声明4："普通跨领域边（dg_edges中的structural_analogy等）
    不自动成为表示变换"——只有显式创建的RepresentationMap才是表示变换。
    """

    def __init__(self):
        self._maps: Dict[str, RepresentationMap] = {}

    def add(self, rep: RepresentationMap) -> None:
        if rep.rep_id in self._maps:
            raise ValueError(f"rep_id已存在: {rep.rep_id}")
        self._maps[rep.rep_id] = rep

    def get(self, rep_id: str) -> Optional[RepresentationMap]:
        return self._maps.get(rep_id)

    def find_by_forms(self, source: str, target: str) -> List[RepresentationMap]:
        """按源/目标表示查找映射。"""
        return [r for r in self._maps.values()
                if r.source_form == source and r.target_form == target]

    def find_chain(self, forms: List[str]) -> List[RepresentationMap]:
        """
        P7-1.2c：查找表示运输链条。

        forms是表示形式的序列，如["整数方程", "Frey曲线", "Galois表示", "模形式"]。
        返回连接相邻形式的映射列表。如果某环节无映射，对应位置为None。
        """
        chain = []
        for i in range(len(forms) - 1):
            maps = self.find_by_forms(forms[i], forms[i + 1])
            if maps:
                chain.append(maps[0])
            else:
                chain.append(None)  # 链条断裂
        return chain

    def check_chain_complete(self, forms: List[str]) -> Dict[str, Any]:
        """
        检查链条是否完整（无断裂）。

        边界情况：链条断裂→告警；环节顺序错误→拒绝。
        """
        chain = self.find_chain(forms)
        broken = [i for i, m in enumerate(chain) if m is None]
        return {
            "chain": chain,
            "complete": len(broken) == 0,
            "broken_indices": broken,
            "n_segments": len(chain),
        }

    def all_maps(self) -> List[RepresentationMap]:
        return list(self._maps.values())
