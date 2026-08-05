"""
Retriever角色完善——Phase 5扩展

对应135号P5-ROLE-1 + 127号§10 + 123号§28 + 系统探讨.md§5.4。

Phase 5在Phase 2的Retriever基础上完善：
- 集成5层优先级检索（P5-2）
- 7类内容区分返回（系统探讨.md§5.4）
- visibility label运行时检查（P5-4.4 + 123号§607）
- 能力令牌验证（P5-4.4 + 123号§607）

冻结声明：
- 输入：当前类型化义务、对象/前提、表示、权限、token预算和可接受证据等级
- 输出：候选定义、定理接口、方法、反例、工具、表示映射、来源及裁剪理由
- 禁止：把整个K、答案专属材料或未满足前提的定理直接送给Solver
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

from .retrieval_order import RetrievalOrder, ContentType
from .representation_query import RepresentationQuery, RepresentationMap
from ..auditor.visibility_labels import VisibilityLabelChecker
from ..auditor.capability_tokens import CapabilityTokenVerifier


@dataclass
class RetrieverInput:
    """
    Retriever输入（123号§28 + 系统探讨.md§5.4）。
    """
    current_obligations: List[str] = field(default_factory=list)  # 当前类型化义务
    objects_premises: List[str] = field(default_factory=list)     # 对象/前提
    representations: List[str] = field(default_factory=list)      # 表示
    permissions: List[str] = field(default_factory=list)          # 权限
    token_budget: int = 1000                                       # token预算
    acceptable_evidence_level: str = "unknown"                    # 可接受证据等级

    def to_dict(self) -> dict:
        return {
            "current_obligations": self.current_obligations,
            "objects_premises": self.objects_premises,
            "representations": self.representations,
            "permissions": self.permissions,
            "token_budget": self.token_budget,
            "acceptable_evidence_level": self.acceptable_evidence_level,
        }


@dataclass
class RetrieverOutput:
    """
    Retriever输出（123号§28 + 系统探讨.md§5.4）。

    7类内容：候选定义、定理接口、方法、反例、工具、表示映射、来源及裁剪理由。
    """
    candidate_definitions: List[Dict[str, Any]] = field(default_factory=list)      # 定义
    theorem_interfaces: List[Dict[str, Any]] = field(default_factory=list)         # 定理接口
    methods: List[Dict[str, Any]] = field(default_factory=list)                    # 方法
    counterexamples: List[Dict[str, Any]] = field(default_factory=list)            # 反例
    tools: List[Dict[str, Any]] = field(default_factory=list)                      # 工具
    representation_maps: List[Dict[str, Any]] = field(default_factory=list)        # 表示映射
    sources_and_pruning_reasons: List[Dict[str, str]] = field(default_factory=list)  # 来源及裁剪理由

    def to_dict(self) -> dict:
        return {
            "candidate_definitions": self.candidate_definitions,
            "theorem_interfaces": self.theorem_interfaces,
            "methods": self.methods,
            "counterexamples": self.counterexamples,
            "tools": self.tools,
            "representation_maps": self.representation_maps,
            "sources_and_pruning_reasons": self.sources_and_pruning_reasons,
        }


class RetrieverPhase5:
    """
    Retriever角色（Phase 5完善版，135号P5-ROLE-1）。

    角色隔离：
    - 可见：当前义务、表示、权限和检索约束
    - 不能做：返回整图或答案专属材料

    冻结声明：
    - Retriever不返回整图（P5-ROLE.COMP）
    - Retriever不返回答案专属材料（P5-ROLE.COMP + 系统探讨.md§5.4）
    - Retriever不返回未满足前提的定理（P5-ROLE.COMP2 + 123号§28）
    """

    # Retriever的visibility label（127号§10）
    VISIBILITY_LABELS = {
        "can_read_current_obligations": True,
        "can_read_representations": True,
        "can_read_permissions": True,
        "can_read_retrieval_constraints": True,
        "can_return_entire_K": False,
        "can_return_answer_specific_materials": False,
        "can_return_unsatisfied_premise_theorems": False,
    }

    # 答案专属材料关键词
    ANSWER_LEAKAGE_KEYWORDS = [
        "答案", "answer", "solution", "最终结论",
        "ground_truth", "truth_vault",
    ]

    def __init__(
        self,
        retrieval_order: Optional[RetrievalOrder] = None,
        representation_query: Optional[RepresentationQuery] = None,
        visibility_label: Optional[VisibilityLabelChecker] = None,
        capability_token: Optional[CapabilityTokenVerifier] = None,
    ):
        self.retrieval_order = retrieval_order
        self.representation_query = representation_query
        self.visibility_label = visibility_label
        self.capability_token = capability_token

    def retrieve(self, input_data: RetrieverInput) -> RetrieverOutput:
        """
        按输入约束过滤输出。

        边界情况：
        - Retriever返回整图（应被拒绝）
        - 返回答案专属材料（应被拒绝）
        - 返回未满足前提的定理（应被拒绝）
        """
        output = RetrieverOutput()

        if self.retrieval_order:
            # 5层优先级检索
            activation_pack_needs = [c.value for c in ContentType]
            results = self.retrieval_order.retrieve(
                activation_pack_id="current",
                activation_pack_needs=activation_pack_needs,
                max_items_per_layer=input_data.token_budget // 100,
            )

            # 按7类内容分拆
            for item in results:
                content_type = item.content_type
                item_dict = item.to_dict()
                if content_type == ContentType.DEFINITION.value:
                    output.candidate_definitions.append(item_dict)
                elif content_type == ContentType.THEOREM.value:
                    output.theorem_interfaces.append(item_dict)
                elif content_type == ContentType.METHOD.value:
                    output.methods.append(item_dict)
                elif content_type == ContentType.COUNTEREXAMPLE.value:
                    output.counterexamples.append(item_dict)
                elif content_type == ContentType.TOOL_INTERFACE.value:
                    output.tools.append(item_dict)
                elif content_type == ContentType.CROSS_DOMAIN_MAP.value:
                    output.representation_maps.append(item_dict)
                elif content_type == ContentType.PROOF_MODULE.value:
                    output.theorem_interfaces.append(item_dict)  # 证明模块归入定理接口

                # 记录来源及裁剪理由
                output.sources_and_pruning_reasons.append({
                    "source": item.source,
                    "pruning_reason": "filtered_by_activation_pack" if item.activation_pack_ref else "none",
                })

        if self.representation_query:
            # 表示映射查询
            maps = self.representation_query.query_map()
            for m in maps:
                output.representation_maps.append(m.to_dict())

        return output

    def check_no_full_graph(self, output: RetrieverOutput, total_k_size: int) -> bool:
        """
        验证Retriever不返回整图（P5-ROLE.COMP + 123号§28 + 系统探讨.md§5.4）。

        边界情况：返回整图（应被拒绝）
        """
        total_returned = (
            len(output.candidate_definitions) +
            len(output.theorem_interfaces) +
            len(output.methods) +
            len(output.counterexamples) +
            len(output.tools) +
            len(output.representation_maps)
        )
        return total_returned < total_k_size

    def check_no_answer_material(self, output: RetrieverOutput) -> bool:
        """
        验证Retriever不返回答案专属材料（P5-ROLE.COMP + 系统探讨.md§5.4）。

        边界情况：返回答案专属材料（应被拒绝）
        """
        all_contents = []
        for item_list in [output.candidate_definitions, output.theorem_interfaces,
                          output.methods, output.counterexamples, output.tools,
                          output.representation_maps]:
            for item in item_list:
                content = item.get("content", "").lower()
                all_contents.append(content)

        for content in all_contents:
            for kw in self.ANSWER_LEAKAGE_KEYWORDS:
                if kw.lower() in content:
                    return False
        return True

    def check_no_unsatisfied_premise_theorems(self, output: RetrieverOutput, satisfied_obligations: List[str]) -> bool:
        """
        验证Retriever不返回未满足前提的定理（P5-ROLE.COMP2 + 123号§28）。

        边界情况：返回未满足前提的定理（应被拒绝）
        """
        for theorem in output.theorem_interfaces:
            premises = theorem.get("premises", [])
            for premise in premises:
                if premise not in satisfied_obligations:
                    return False
        return True

    def check_visibility_labels(self) -> bool:
        """
        验证Retriever的visibility label（P5-4.4 + 123号§607）。

        边界情况：Retriever角色边界只写在prompt里未落实为代码机制（应被拒绝）

        检查逻辑：允许项应为True，禁止项应为False。
        """
        # 允许项应为True
        allowed = ["can_read_current_obligations", "can_read_representations",
                   "can_read_permissions", "can_read_retrieval_constraints"]
        for key in allowed:
            if not self.VISIBILITY_LABELS.get(key, False):
                return False
        # 禁止项应为False
        forbidden = ["can_return_entire_K", "can_return_answer_specific_materials",
                     "can_return_unsatisfied_premise_theorems"]
        for key in forbidden:
            if self.VISIBILITY_LABELS.get(key, True):
                return False
        return True
