"""
P7-MATH 数学主张标注级别。

plan行315："数学名词冒充实现：所有HoTT/拓扑/几何主张标注'语义规格/实验分析/已实现'级别。"
plan行384："POMDP、范畴、层、HoTT、TDA等只在对象和可证伪问题明确时进入；
文档必须区分'数学语义规格''首版工程表示''远期研究方向'。"

3个级别：
  1. 语义规格（只有定义，无实现）
  2. 实验分析（有实验但无生产依赖）
  3. 已实现（有实现且有生产依赖）

强制机制（P7-MATH-2）：
  标注级别必须由代码自动验证（基于3项基线比较结果），不能手动设置。
  手动覆盖时→抛ManualLabelOverrideError。
"""

from typing import Dict, Any, List, Optional
from enum import Enum


class ManualLabelOverrideError(Exception):
    """
    P7-MATH-2强制机制：手动覆盖标注级别→抛ManualLabelOverrideError。

    不只是返回False声明——是运行时强制阻断。
    """


class MathLabel(Enum):
    """3个标注级别。"""
    SEMANTIC_SPEC = "语义规格"    # 只有定义，无实现
    EXPERIMENTAL = "实验分析"      # 有实验但无生产依赖
    IMPLEMENTED = "已实现"         # 有实现且有生产依赖


class MathLabeler:
    """
    P7-MATH：数学主张标注级别。

    plan行315："所有HoTT/拓扑/几何主张标注'语义规格/实验分析/已实现'级别。"
    """

    def __init__(self):
        self._labels: Dict[str, MathLabel] = {}
        self._auto_verified: Dict[str, bool] = {}

    def auto_determine_label(
        self,
        claim_id: str,
        has_implementation: bool,
        has_experiment: bool,
        has_production_dependency: bool,
        baseline_comparison_result=None,
    ) -> MathLabel:
        """
        自动确定标注级别——基于实现状态和基线比较结果。

        P7-MATH-2：标注级别必须由代码自动验证，不能手动设置。
        """
        if has_implementation and has_production_dependency:
            # 有实现且有生产依赖→需要基线比较验证
            if baseline_comparison_result is not None:
                if baseline_comparison_result.any_gain:
                    label = MathLabel.IMPLEMENTED
                else:
                    # 无增益→降级为实验分析
                    label = MathLabel.EXPERIMENTAL
            else:
                # 无基线比较结果→不能标注为已实现
                label = MathLabel.EXPERIMENTAL
        elif has_experiment:
            label = MathLabel.EXPERIMENTAL
        else:
            label = MathLabel.SEMANTIC_SPEC

        self._labels[claim_id] = label
        self._auto_verified[claim_id] = True
        return label

    def set_label_manually(self, claim_id: str, label: MathLabel) -> Dict[str, Any]:
        """
        手动设置标注级别——抛ManualLabelOverrideError。

        强制机制（P7-MATH-2）：
        标注级别必须由代码自动验证，不能手动设置。手动覆盖时→抛ManualLabelOverrideError。
        """
        raise ManualLabelOverrideError(
            f"不能手动设置标注级别为'{label.value}'。"
            f"P7-MATH-2：标注级别必须由代码自动验证（基于3项基线比较结果），不能手动设置。"
            f"请使用auto_determine_label()方法。"
        )

    def get_label(self, claim_id: str) -> Optional[MathLabel]:
        return self._labels.get(claim_id)

    def is_auto_verified(self, claim_id: str) -> bool:
        return self._auto_verified.get(claim_id, False)

    def check_all_labeled(self, claim_ids: List[str]) -> Dict[str, Any]:
        """
        检查所有主张是否都有标注。

        plan行315："所有HoTT/拓扑/几何主张标注"——所有主张都必须有标注。
        """
        labeled = [cid for cid in claim_ids if cid in self._labels]
        unlabeled = [cid for cid in claim_ids if cid not in self._labels]
        return {
            "n_claims": len(claim_ids),
            "n_labeled": len(labeled),
            "n_unlabeled": len(unlabeled),
            "all_labeled": len(unlabeled) == 0,
            "unlabeled": unlabeled,
        }

    def check_label_consistent_with_baseline(
        self,
        claim_id: str,
        baseline_comparison_result=None,
    ) -> Dict[str, Any]:
        """
        检查标注级别与基线比较结果是否一致。

        强制机制：标注为`已实现`但3项比较无增益→降级为`实验分析`。
        """
        label = self._labels.get(claim_id)
        if label is None:
            return {"consistent": False, "reason": "未标注"}

        if label == MathLabel.IMPLEMENTED:
            if baseline_comparison_result is None or not baseline_comparison_result.any_gain:
                return {
                    "consistent": False,
                    "current_label": label.value,
                    "should_be": MathLabel.EXPERIMENTAL.value,
                    "reason": "标注为'已实现'但3项基线比较无增益→应降级为'实验分析'",
                    "needs_downgrade": True,
                }

        return {"consistent": True, "current_label": label.value}

    def check_not_fake_implementation(self, claim_id: str) -> Dict[str, Any]:
        """
        P7-MATH.COMP2：不冒充数学实现。

        plan行315："数学名词冒充实现"——所有主张必须诚实标注。
        """
        label = self._labels.get(claim_id)
        if label == MathLabel.IMPLEMENTED and not self._auto_verified.get(claim_id, False):
            return {
                "is_fake_implementation": True,
                "reason": "标注为'已实现'但未经自动验证",
                "needs_verification": True,
            }

        return {"is_fake_implementation": False, "label": label.value if label else None}
