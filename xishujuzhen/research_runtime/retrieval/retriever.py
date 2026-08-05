"""
Retriever角色：不返回整图或答案专属材料

对应132号P2-ROLE-3 + 127号§10 + 123号§28。

角色隔离（127号§10）：
- 可见：当前义务、表示、权限和检索约束
- 不能做：返回整图或答案专属材料

123号§28 + 系统探讨.md§5.4：
- Retriever只提供有权限、可追溯的最小知识接口
- 不返回整图或答案专属材料
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


class RetrievalConstraint(str, Enum):
    """
    检索约束类型。
    """
    BY_OBLIGATION = "by_obligation"       # 按当前义务过滤
    BY_REPRESENTATION = "by_representation"  # 按当前表示过滤
    BY_PERMISSION = "by_permission"       # 按权限过滤
    BY_EVIDENCE_LEVEL = "by_evidence_level"  # 按证据等级过滤


@dataclass
class RetrievalRequest:
    """
    检索请求。
    """
    current_obligations: List[str] = field(default_factory=list)  # 当前义务ID列表
    current_representations: List[str] = field(default_factory=list)  # 当前表示ID列表
    permissions: List[str] = field(default_factory=list)  # 权限列表
    max_items: int = 10  # 最大返回条数（防止整图返回）
    constraints: List[RetrievalConstraint] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "current_obligations": self.current_obligations,
            "current_representations": self.current_representations,
            "permissions": self.permissions,
            "max_items": self.max_items,
            "constraints": [c.value for c in self.constraints],
        }


@dataclass
class RetrievalResult:
    """
    检索结果——最小知识接口。
    """
    items: List[Dict[str, Any]] = field(default_factory=list)
    truncated: bool = False  # 是否被截断（超过max_items）
    source: str = ""  # 来源说明
    evidence_levels: List[str] = field(default_factory=list)  # 各条目的证据等级

    def to_dict(self) -> dict:
        return {
            "items": self.items,
            "truncated": self.truncated,
            "source": self.source,
            "evidence_levels": self.evidence_levels,
        }


class Retriever:
    """
    Retriever角色（132号P2-ROLE-3）。

    角色隔离：
    - 可见：当前义务、表示、权限和检索约束
    - 不能做：返回整图或答案专属材料

    冻结声明（P2-ROLE.COMP3）：
    - Retriever不返回整图（受max_items约束）
    - Retriever不返回答案专属材料（需过滤）
    """

    # 答案专属材料关键词（用于过滤）
    ANSWER_LEAKAGE_KEYWORDS = [
        "答案", "answer", "solution", "最终结论",
        "ground_truth", "truth_vault",
    ]

    def __init__(self, knowledge_items: List[Dict[str, Any]] = None):
        """
        初始化Retriever。

        参数：
        - knowledge_items: 可检索的知识条目列表（每条至少有id/content/obligation_refs/representation_refs/permission/evidence_level字段）
        """
        self.knowledge_items = knowledge_items or []

    def retrieve(self, request: RetrievalRequest) -> RetrievalResult:
        """
        按检索约束过滤结果。

        边界情况：
        - Retriever尝试返回整图（应被拒绝——受max_items约束）
        - Retriever尝试返回答案专属材料（应被拒绝——过滤答案关键词）
        - 无匹配结果
        """
        filtered = []

        for item in self.knowledge_items:
            # 1. 按义务过滤
            if RetrievalConstraint.BY_OBLIGATION in request.constraints:
                item_obligations = item.get("obligation_refs", [])
                if not any(o in item_obligations for o in request.current_obligations):
                    continue

            # 2. 按表示过滤
            if RetrievalConstraint.BY_REPRESENTATION in request.constraints:
                item_representations = item.get("representation_refs", [])
                if not any(r in item_representations for r in request.current_representations):
                    continue

            # 3. 按权限过滤
            if RetrievalConstraint.BY_PERMISSION in request.constraints:
                item_permissions = item.get("permissions", [])
                if not any(p in item_permissions for p in request.permissions):
                    continue

            # 4. 过滤答案专属材料（P2-ROLE.COMP3）
            content = item.get("content", "").lower()
            if any(kw.lower() in content for kw in self.ANSWER_LEAKAGE_KEYWORDS):
                continue  # 跳过答案专属材料

            filtered.append(item)

        # 5. 截断——不返回整图（P2-ROLE.COMP3）
        truncated = len(filtered) > request.max_items
        if truncated:
            filtered = filtered[:request.max_items]

        return RetrievalResult(
            items=filtered,
            truncated=truncated,
            source="filtered_by_constraints",
            evidence_levels=[item.get("evidence_level", "unknown") for item in filtered],
        )

    def check_no_full_graph(self, request: RetrievalRequest) -> bool:
        """
        检查是否尝试返回整图（应被拒绝）。

        边界情况：max_items设为很大值时仍不应返回全部
        """
        result = self.retrieve(request)
        # 如果返回的条目数等于全部知识条目数，说明返回了整图
        return len(result.items) < len(self.knowledge_items)

    def check_no_answer_material(self, request: RetrievalRequest) -> bool:
        """
        检查是否返回了答案专属材料（应被拒绝）。
        """
        result = self.retrieve(request)
        for item in result.items:
            content = item.get("content", "").lower()
            if any(kw.lower() in content for kw in self.ANSWER_LEAKAGE_KEYWORDS):
                return False  # 返回了答案材料——违规
        return True
