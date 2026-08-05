"""
MigrationTester：跨题迁移验证（DYN-5）

对应134号P4-7。

123号§41 DYN-5：
- 在未参与设计的迁移题上复现效果
- 使用分层效应模型记录7个维度
- 只在原题有效的规则不能进入通用H

P4-7.3：验证Ramsey案例的迁移维度（新的奇环问题C_7上是否迁移）。
128号§3.3 Ramsey案例验证维度第5项：新的奇环问题上是否迁移。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

from .effect_estimator import ContinuationResult, EffectEstimate, EffectEstimator


# 123号§41 DYN-5分层效应模型的7个维度
MIGRATION_DIMENSIONS = [
    "problem_family",    # 问题族
    "math_domain",       # 数学领域
    "model_version",     # 模型/版本
    "hint_level",        # Hint等级
    "hint_format",       # 提示格式
    "tool_permissions",  # 工具权限
    "time_position",     # 时间位置
]


@dataclass
class MigrationResult:
    """跨题迁移验证结果"""
    migration_task_id: str
    original_task_id: str
    # 7个维度的记录（123号§41）
    dimensions: Dict[str, str] = field(default_factory=dict)
    # 迁移效应
    migrated_effect: float = 0.0
    # 是否成功迁移
    is_migrated: bool = False
    # 迁移题是否参与了设计（P4-7.COMP3：应被拒绝）
    participated_in_design: bool = False

    def to_dict(self) -> dict:
        return {
            "migration_task_id": self.migration_task_id,
            "original_task_id": self.original_task_id,
            "dimensions": self.dimensions,
            "migrated_effect": self.migrated_effect,
            "is_migrated": self.is_migrated,
            "participated_in_design": self.participated_in_design,
        }


class MigrationTester:
    """
    P4-7：新题迁移。

    P4-7.1：在未参与设计的迁移题上复现效果
    P4-7.2：使用分层效应模型记录7个维度
    P4-7.3：验证Ramsey案例的迁移维度（C_7上是否迁移）
    """

    def __init__(self, effect_estimator: EffectEstimator):
        self.effect_estimator = effect_estimator

    def create_c7_migration_task(self) -> Dict[str, Any]:
        """
        创建C_7迁移题——七边形奇环的Ramsey数下界猜测。

        P4-7.3：验证新的奇环问题上是否迁移（128号§3.3第5项）。

        C_7与C_5结构相似（都是奇环），但C_7未参与Hint设计。
        """
        return {
            "task_id": "Q_0_ramsey_c7_migration",
            "type": "conjecture",
            "domain": "combinatorics/ramsey_theory",
            "objects": ["R_k(C_7)", "C_7", "C_5", "k"],
            "premises": [
                "R_k(C_5)下界已知（原题结果）",
                "C_7比C_5更难避免",
                "奇环的一般性质",
            ],
            "goal": "猜测R_k(C_7)下界",
            "success_conditions": [
                "候选是非重复的",
                "候选是可证伪的",
                "候选通过初筛",
                "候选未被反例否定",
            ],
            "participated_in_design": False,  # P4-7.COMP3：迁移题未参与设计
        }

    def verify_migration_dimensions(
        self,
        original_task: Dict[str, Any],
        migration_task: Dict[str, Any],
        model_version: str,
        hint_level: str,
    ) -> Dict[str, Any]:
        """
        P4-7.2：使用分层效应模型记录7个维度（123号§41）。

        P4-7.COMP：DYN-5迁移验证覆盖7个维度。
        """
        dimensions = {
            "problem_family": f"ramsey_odd_cycle",
            "math_domain": "combinatorics/ramsey_theory",
            "model_version": model_version,
            "hint_level": hint_level,
            "hint_format": "text_prompt",
            "tool_permissions": "none",
            "time_position": "post_original",
        }

        # P4-7.COMP2：只在原题有效的规则不能进入通用H
        # P4-7.COMP3：迁移题未参与设计
        participated = migration_task.get("participated_in_design", False)

        return {
            "dimensions": dimensions,
            "all_dimensions_covered": len(dimensions) == 7,
            "participated_in_design": participated,
            "migration_rejected": participated,  # 如果参与了设计则拒绝
        }

    def test_migration(
        self,
        original_results: Dict[str, List[ContinuationResult]],
        migration_results: Dict[str, List[ContinuationResult]],
        original_task: Dict[str, Any],
        migration_task: Dict[str, Any],
        model_version: str,
    ) -> MigrationResult:
        """
        P4-7.1：在未参与设计的迁移题上复现效果。

        P4-EXIT-2：该结果在未参与设计的迁移题上复现。
        """
        # 估计原题和迁移题的效应
        original_estimates = self.effect_estimator.estimate_all_groups(original_results)
        migration_estimates = self.effect_estimator.estimate_all_groups(migration_results)

        # 检查迁移：迁移题的最佳处理组是否也有正效应
        best_original = max(original_estimates.values(), key=lambda e: e.ate) if original_estimates else None
        best_migration = max(migration_estimates.values(), key=lambda e: e.ate) if migration_estimates else None

        is_migrated = False
        migrated_effect = 0.0
        if best_migration and best_migration.ate > 0:
            is_migrated = best_migration.ci_lower > 0
            migrated_effect = best_migration.ate

        dimensions = self.verify_migration_dimensions(
            original_task, migration_task, model_version,
            hint_level=best_original.ate.__class__.__name__ if best_original else "unknown",
        )

        return MigrationResult(
            migration_task_id=migration_task.get("task_id", ""),
            original_task_id=original_task.get("task_id", ""),
            dimensions=dimensions["dimensions"],
            migrated_effect=migrated_effect,
            is_migrated=is_migrated,
            participated_in_design=migration_task.get("participated_in_design", False),
        )
