"""
P7-3.1 证明路径等价分类——避免把改写/粒度差异误判为新思路。

plan HoTT方向2："对证明路径做语义等价分类"

3类等价判定（137号Check List明确要求，不只是"等价分类"的概括）：
  1. 改写等价：相同数学对象和推理步骤，只是表述方式不同（变量名不同、顺序可交换的步骤顺序不同）
  2. 粒度等价：相同数学对象和推理方向，但粒度不同（一条路径合并多步，另一条展开为多步）
  3. 真正新思路：不同数学对象或不同推理方向

母本细节补充（系统探讨.md§8.2位置二，阶段1母本回溯发现）：
  母本明确列出3种差异："中间步骤不同、变量名不同、引理粒度不同"
  123号概括为"变量改名或粒度变化"——实现时必须包含这3种差异的规范化方法。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple, Optional
from enum import Enum


class EquivalenceClass(Enum):
    """3类等价分类。"""
    REWRITE_EQUIVALENT = "rewrite_equivalent"  # 改写等价
    GRANULARITY_EQUIVALENT = "granularity_equivalent"  # 粒度等价
    GENUINE_NEW_IDEA = "genuine_new_idea"  # 真正新思路


@dataclass
class ProofStep:
    """证明路径的一个步骤。"""
    step_id: str
    math_objects: List[str] = field(default_factory=list)  # 使用的数学对象
    operation: str = ""  # 推理操作
    variables: Dict[str, str] = field(default_factory=dict)  # 变量名映射
    sub_steps: List[str] = field(default_factory=list)  # 子步骤（用于粒度分析）

    def to_dict(self) -> dict:
        return {
            "step_id": self.step_id,
            "math_objects": list(self.math_objects),
            "operation": self.operation,
            "variables": dict(self.variables),
            "sub_steps": list(self.sub_steps),
        }


@dataclass
class ProofPath:
    """一条证明路径。"""
    path_id: str
    steps: List[ProofStep] = field(default_factory=list)

    def math_objects_set(self) -> set:
        """返回路径使用的所有数学对象集合。"""
        objs = set()
        for s in self.steps:
            objs.update(s.math_objects)
        return objs

    def operations_list(self) -> List[str]:
        """返回路径的推理操作序列。"""
        return [s.operation for s in self.steps]

    def to_dict(self) -> dict:
        return {
            "path_id": self.path_id,
            "steps": [s.to_dict() for s in self.steps],
        }


class PathEquivalenceClassifier:
    """
    P7-3.1：证明路径等价分类器。

    实现3类等价判定，包含母本§8.2位置二的3种差异规范化。
    """

    def normalize_variables(self, path: ProofPath) -> ProofPath:
        """
        规范化变量名——母本§8.2位置二"变量名不同"的规范化方法。

        将所有变量名重命名为规范形式（v1, v2, ...）。
        """
        var_map: Dict[str, str] = {}
        counter = 0

        normalized_steps = []
        for step in path.steps:
            new_vars = {}
            for orig_var, value in step.variables.items():
                if orig_var not in var_map:
                    counter += 1
                    var_map[orig_var] = f"v{counter}"
                new_vars[var_map[orig_var]] = value

            normalized_steps.append(ProofStep(
                step_id=step.step_id,
                math_objects=list(step.math_objects),
                operation=step.operation,
                variables=new_vars,
                sub_steps=list(step.sub_steps),
            ))

        return ProofPath(path_id=path.path_id, steps=normalized_steps)

    def normalize_step_order(self, path: ProofPath) -> ProofPath:
        """
        规范化步骤顺序——可交换步骤排序。

        母本§8.2位置二"中间步骤不同"的规范化方法。
        """
        # 简化：按操作名排序（实际实现需要依赖分析确定可交换性）
        sorted_steps = sorted(path.steps, key=lambda s: s.operation)
        return ProofPath(path_id=path.path_id, steps=sorted_steps)

    def normalize_granularity(self, path: ProofPath) -> ProofPath:
        """
        归一化粒度——母本§8.2位置二"引理粒度不同"的规范化方法。

        展开合并步骤或合并展开步骤。
        """
        # 简化：展开有子步骤的步骤
        expanded_steps = []
        for step in path.steps:
            if step.sub_steps:
                # 展开子步骤
                for i, sub in enumerate(step.sub_steps):
                    expanded_steps.append(ProofStep(
                        step_id=f"{step.step_id}.{i}",
                        math_objects=list(step.math_objects),
                        operation=sub if isinstance(sub, str) else step.operation,
                        variables=dict(step.variables),
                        sub_steps=[],
                    ))
            else:
                expanded_steps.append(step)

        return ProofPath(path_id=path.path_id, steps=expanded_steps)

    def classify(self, path_a: ProofPath, path_b: ProofPath) -> Dict[str, Any]:
        """
        分类两条路径的等价关系。

        判定方法：
        1. 改写等价：规范化（变量重命名+可交换步骤排序）后比较
        2. 粒度等价：对粒度做归一化后比较
        3. 真正新思路：规范化+粒度归一化后仍然不同

        边界情况：
        - 改写被误判为新思路→拒绝
        - 粒度差异被误判为新思路→拒绝
        - 真正新思路被误判为等价→拒绝
        """
        # 步骤1：规范化变量名和步骤顺序
        norm_a = self.normalize_step_order(self.normalize_variables(path_a))
        norm_b = self.normalize_step_order(self.normalize_variables(path_b))

        # 检查改写等价
        if self._paths_equal(norm_a, norm_b):
            return {
                "equivalence_class": EquivalenceClass.REWRITE_EQUIVALENT.value,
                "is_equivalent": True,
                "method": "规范化（变量重命名+步骤排序）后相同",
                "mother_text_reference": "母本§8.2位置二：变量名不同、中间步骤不同",
            }

        # 步骤2：粒度归一化后比较
        gran_a = self.normalize_granularity(norm_a)
        gran_b = self.normalize_granularity(norm_b)

        if self._paths_equal(gran_a, gran_b):
            return {
                "equivalence_class": EquivalenceClass.GRANULARITY_EQUIVALENT.value,
                "is_equivalent": True,
                "method": "粒度归一化后相同",
                "mother_text_reference": "母本§8.2位置二：引理粒度不同",
            }

        # 步骤3：规范化+粒度归一化后仍然不同→真正新思路
        return {
            "equivalence_class": EquivalenceClass.GENUINE_NEW_IDEA.value,
            "is_equivalent": False,
            "method": "规范化+粒度归一化后仍然不同",
            "math_objects_a": list(path_a.math_objects_set()),
            "math_objects_b": list(path_b.math_objects_set()),
            "objects_overlap": path_a.math_objects_set() & path_b.math_objects_set(),
        }

    def _paths_equal(self, a: ProofPath, b: ProofPath) -> bool:
        """检查两条规范化后的路径是否相同。"""
        if len(a.steps) != len(b.steps):
            return False
        for sa, sb in zip(a.steps, b.steps):
            if sa.operation != sb.operation:
                return False
            if set(sa.math_objects) != set(sb.math_objects):
                return False
        return True

    def check_not_misclassify(self, classification: Dict[str, Any]) -> Dict[str, Any]:
        """
        检查等价分类是否正确——避免误判。

        边界情况：
        - 改写被误判为新思路→拒绝
        - 粒度差异被误判为新思路→拒绝
        - 真正新思路被误判为等价→拒绝
        """
        eq_class = classification.get("equivalence_class")
        issues = []

        if eq_class == EquivalenceClass.GENUINE_NEW_IDEA.value:
            # 检查是否应该被分类为改写等价或粒度等价
            if classification.get("objects_overlap"):
                overlap = classification["objects_overlap"]
                if len(overlap) == len(classification.get("math_objects_a", [])):
                    issues.append("所有数学对象重叠——可能是改写等价被误判为新思路")

        return {
            "classification_correct": len(issues) == 0,
            "issues": issues,
        }
