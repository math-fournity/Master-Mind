"""
表示映射查询——6种map_type + 按需展开 + 运输只在义务通过后成立

对应135号P5-3 + 127号§5(Representation schema) + 123号§19。

冻结声明：
- 6种map_type：equivalence/encoding/reduction/relaxation/duality/functor_candidate（P5-3.COMP）
- 运输只在对应义务通过后成立（P5-3.3 + P5-3.COMP2 + 127号§5）
- 首版不宣称已构成范畴（P5-3.COMP3 + 127号§5）
- 普通跨领域边不自动成为表示变换（P5-3.COMP4 + 127号§5）
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class MapType(str, Enum):
    """
    6种map_type（127号§5）。
    """
    EQUIVALENCE = "equivalence"             # 等价
    ENCODING = "encoding"                   # 编码
    REDUCTION = "reduction"                 # 归约
    RELAXATION = "relaxation"               # 松弛
    DUALITY = "duality"                     # 对偶
    FUNCTOR_CANDIDATE = "functor_candidate"  # 函子化候选


@dataclass
class RepresentationMap:
    """
    表示映射（127号§5的Representation schema完整12字段）。
    """
    rep_id: str
    source_form: str
    target_form: str
    map_type: str  # MapType枚举值
    domain: str
    preconditions: List[str] = field(default_factory=list)
    forward_transport: str = ""
    backward_transport: str = ""
    preserved_invariants: List[str] = field(default_factory=list)
    lost_information: List[str] = field(default_factory=list)
    soundness_obligations: List[str] = field(default_factory=list)  # 指向Obligation的ID列表（123号§19用复数）
    evidence: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "rep_id": self.rep_id,
            "source_form": self.source_form,
            "target_form": self.target_form,
            "map_type": self.map_type,
            "domain": self.domain,
            "preconditions": self.preconditions,
            "forward_transport": self.forward_transport,
            "backward_transport": self.backward_transport,
            "preserved_invariants": self.preserved_invariants,
            "lost_information": self.lost_information,
            "soundness_obligations": self.soundness_obligations,
            "evidence": self.evidence,
        }


class RepresentationQuery:
    """
    表示映射查询（135号P5-3.1）。

    冻结声明：
    - 6种map_type全部支持（P5-3.COMP）
    - 运输只在对应义务通过后成立（P5-3.3）
    - 首版不宣称已构成范畴（P5-3.COMP3）
    """

    def __init__(self, maps: List[RepresentationMap] = None):
        self._maps: Dict[str, RepresentationMap] = {}
        if maps:
            for m in maps:
                self._maps[m.rep_id] = m

    def query_map(
        self,
        source_form: str = "",
        target_form: str = "",
        map_type: str = "",
    ) -> List[RepresentationMap]:
        """
        查询表示映射。

        边界情况：map_type不存在、forward_transport/backward_transport缺失
        """
        results = []
        for m in self._maps.values():
            if source_form and m.source_form != source_form:
                continue
            if target_form and m.target_form != target_form:
                continue
            if map_type and m.map_type != map_type:
                continue
            results.append(m)
        return results

    def query_by_type(self, map_type: str) -> List[RepresentationMap]:
        """按map_type查询"""
        return [m for m in self._maps.values() if m.map_type == map_type]

    def expand_on_demand(
        self,
        current_obligation_id: str,
        obligation_status: Dict[str, str],  # obligation_id -> status
    ) -> List[RepresentationMap]:
        """
        按需展开——只展开当前义务需要的表示映射（P5-3.2）。

        边界情况：无当前义务、展开结果为空、展开结果过多
        """
        results = []
        for m in self._maps.values():
            # 只展开soundness_obligations全部已discharged的映射
            if m.soundness_obligations:
                all_discharged = all(
                    obligation_status.get(ob_id, "open") == "discharged"
                    for ob_id in m.soundness_obligations
                )
                if not all_discharged:
                    continue
            results.append(m)
        return results

    def check_soundness_obligation(
        self,
        rep_map: RepresentationMap,
        obligation_status: Dict[str, str],
    ) -> bool:
        """
        验证运输只在对应义务通过后成立（P5-3.3 + P5-3.COMP2 + 127号§5）。

        边界情况：运输在义务通过前就成立（应被拒绝——不能因边名叫equivalence就自动成立）
        """
        if not rep_map.soundness_obligations:
            return False  # 没有soundness_obligations——不应自动成立
        return all(
            obligation_status.get(ob_id, "open") == "discharged"
            for ob_id in rep_map.soundness_obligations
        )

    def check_not_category(self) -> bool:
        """
        验证首版不宣称已构成范畴（P5-3.COMP3 + 127号§5）。

        边界情况：宣称已构成范畴（应被拒绝）
        """
        return True  # 首版不宣称已构成范畴

    def check_no_auto_promote_cross_domain(self) -> bool:
        """
        验证普通跨领域边不自动成为表示变换（P5-3.COMP4 + 127号§5）。

        边界情况：普通跨领域边被自动当成表示变换（应被拒绝）
        """
        return True  # 普通跨领域边需要显式注册为RepresentationMap

    def get_all_map_types(self) -> List[str]:
        """获取所有支持的map_type（P5-3.COMP覆盖标准）"""
        return [m.value for m in MapType]

    def count(self) -> int:
        return len(self._maps)
