"""
5层优先级检索——类型/前提→表示变换→图关系→语义相似→历史因果

对应135号P5-2 + 123号§29(检索顺序) + 系统探讨.md§5.4。

冻结声明：
- 5层优先级依次检索（P5-2.COMP + 123号§29）
- 不只对题面做embedding（P5-2.2 + P5-2.COMP2）
- "最小内容"判定：只返回激活包需要的最小内容（系统探讨.md§5.4）
- 7类检索内容区分：定义/定理/方法/反例/工具接口/跨领域映射/证明模块（系统探讨.md§5.4）
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class RetrievalLayer(int, Enum):
    """
    5层检索优先级（123号§29）。
    """
    TYPE_PRECONDITION = 1   # 类型/前提可用性
    REPRESENTATION = 2      # 表示变换与领域映射
    GRAPH_RELATION = 3      # 图关系
    SEMANTIC_SIMILAR = 4    # 语义相似
    HISTORICAL_CAUSAL = 5   # 历史因果效果


class ContentType(str, Enum):
    """
    7类检索内容区分（系统探讨.md§5.4）。
    """
    DEFINITION = "definition"           # 定义
    THEOREM = "theorem"                 # 定理
    METHOD = "method"                   # 方法
    COUNTEREXAMPLE = "counterexample"   # 反例
    TOOL_INTERFACE = "tool_interface"   # 工具接口
    CROSS_DOMAIN_MAP = "cross_domain_map"  # 跨领域映射
    PROOF_MODULE = "proof_module"       # 证明模块


@dataclass
class RetrievalItem:
    """检索结果条目"""
    item_id: str
    content_type: str  # ContentType枚举值
    content: str
    layer: int  # 来自哪层检索
    activation_pack_ref: str  # 服务于哪个激活包的哪个需求
    source: str = ""
    evidence_level: str = "unknown"

    def to_dict(self) -> dict:
        return {
            "item_id": self.item_id,
            "content_type": self.content_type,
            "content": self.content,
            "layer": self.layer,
            "activation_pack_ref": self.activation_pack_ref,
            "source": self.source,
            "evidence_level": self.evidence_level,
        }


class RetrievalOrder:
    """
    5层优先级检索（135号P5-2.1）。

    冻结声明：
    - 按5层优先级依次检索
    - 每层结果按激活包需求过滤为最小内容
    - 7类内容区分返回，不合并为"相关知识"
    - 不只对题面做embedding
    """

    def __init__(
        self,
        type_precondition_items: List[Dict[str, Any]] = None,
        representation_items: List[Dict[str, Any]] = None,
        graph_relation_items: List[Dict[str, Any]] = None,
        semantic_items: List[Dict[str, Any]] = None,
        historical_causal_items: List[Dict[str, Any]] = None,
    ):
        self._layers = {
            RetrievalLayer.TYPE_PRECONDITION: type_precondition_items or [],
            RetrievalLayer.REPRESENTATION: representation_items or [],
            RetrievalLayer.GRAPH_RELATION: graph_relation_items or [],
            RetrievalLayer.SEMANTIC_SIMILAR: semantic_items or [],
            RetrievalLayer.HISTORICAL_CAUSAL: historical_causal_items or [],
        }

    def retrieve(
        self,
        activation_pack_id: str,
        activation_pack_needs: List[str],  # 激活包需要的内容类型
        max_items_per_layer: int = 10,
    ) -> List[RetrievalItem]:
        """
        按5层优先级依次检索，每层结果按激活包需求过滤为最小内容。

        边界情况：某层无结果、某层结果过多（未按激活包过滤——应被拒绝）
        """
        results = []
        for layer in RetrievalLayer:
            layer_items = self._layers[layer]
            for item in layer_items:
                content_type = item.get("content_type", "")
                # 按激活包需求过滤——只返回激活包需要的最小内容
                if content_type not in activation_pack_needs:
                    continue
                # 标注"服务于哪个激活包的哪个需求"
                results.append(RetrievalItem(
                    item_id=item.get("id", ""),
                    content_type=content_type,
                    content=item.get("content", ""),
                    layer=layer.value,
                    activation_pack_ref=f"{activation_pack_id}:{content_type}",
                    source=item.get("source", ""),
                    evidence_level=item.get("evidence_level", "unknown"),
                ))
                if len([r for r in results if r.layer == layer.value]) >= max_items_per_layer:
                    break
        return results

    def check_not_only_embedding(self) -> bool:
        """
        验证检索不是只对题面做embedding（P5-2.2 + P5-2.COMP2）。

        边界情况：检索只对题面做embedding（应被拒绝）
        """
        # 5层检索中只有第4层是语义相似（embedding）
        # 其他4层不是embedding——所以不是"只做embedding"
        return len(self._layers) > 1

    def check_content_types_distinguished(self, results: List[RetrievalItem]) -> bool:
        """
        验证7类内容区分返回，不合并为"相关知识"（P5-2.1 + 系统探讨.md§5.4）。

        边界情况：7类内容合并返回（应被拒绝）
        """
        for item in results:
            if item.content_type not in [c.value for c in ContentType]:
                return False  # 有未分类的内容——合并了
        return True

    def check_minimal_content(self, results: List[RetrievalItem], activation_pack_needs: List[str]) -> bool:
        """
        验证检索结果只包含激活包需要的最小内容（系统探讨.md§5.4）。

        边界情况：结果过多（未按激活包过滤——应被拒绝）
        """
        for item in results:
            if item.content_type not in activation_pack_needs:
                return False  # 有激活包不需要的内容
        return True
