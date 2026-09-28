"""
P7-7.3/P7-8.3/P7-EXIT-1b 3基线比较维度量化。

123号§44："HoTT/高阶路径的DYN-7实验必须和普通类型化表示图基线比较：
若不能更好地减少重复证明类、验证运输一致性或提高跨表示迁移，
就保持为理论说明，不进入生产依赖。"

3个基线比较维度（123号§44逐字）：
  1. 减少重复证明类
  2. 验证运输一致性
  3. 提高跨表示迁移

强制机制：
  无增益但标注为`已实现`→标注降级为`实验分析`。
  3项比较中无任何一项有可测量增益→抛ExitGateFailureError。
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


class ExitGateFailureError(Exception):
    """
    P7-EXIT-1强制机制：3项比较中无任何一项有可测量增益→抛ExitGateFailureError。
    """


class LabelDowngradeWarning(Exception):
    """
    P7-EXIT-2强制机制：标注为`已实现`但3项比较无增益→降级为`实验分析`。
    """


class StopConditionTriggeredError(Exception):
    """
    P7-STOP-1强制机制：3项基线比较中无任何一项有可测量增益→抛StopConditionTriggeredError。
    """


@dataclass
class BaselineComparisonResult:
    """基线比较结果——3个维度。"""
    # 维度1：减少重复证明类
    redundant_proofs_baseline: int = 0
    redundant_proofs_method: int = 0
    # 维度2：验证运输一致性
    transport_consistency_baseline: float = 0.0
    transport_consistency_method: float = 0.0
    # 维度3：提高跨表示迁移
    cross_rep_migration_baseline: float = 0.0
    cross_rep_migration_method: float = 0.0

    @property
    def dim1_gain(self) -> float:
        """维度1增益：减少的重复证明类数量（正=好）。"""
        return float(self.redundant_proofs_baseline - self.redundant_proofs_method)

    @property
    def dim2_gain(self) -> float:
        """维度2增益：运输一致性提升（正=好）。"""
        return self.transport_consistency_method - self.transport_consistency_baseline

    @property
    def dim3_gain(self) -> float:
        """维度3增益：跨表示迁移提升（正=好）。"""
        return self.cross_rep_migration_method - self.cross_rep_migration_baseline

    @property
    def n_dimensions_with_gain(self) -> int:
        """有增益的维度数。"""
        return sum(1 for g in [self.dim1_gain, self.dim2_gain, self.dim3_gain] if g > 0)

    @property
    def any_gain(self) -> bool:
        """是否有任何一项有可测量增益。"""
        return self.n_dimensions_with_gain > 0

    def to_dict(self) -> dict:
        return {
            "dim1_redundant_proofs": {
                "baseline": self.redundant_proofs_baseline,
                "method": self.redundant_proofs_method,
                "gain": self.dim1_gain,
                "has_gain": self.dim1_gain > 0,
            },
            "dim2_transport_consistency": {
                "baseline": self.transport_consistency_baseline,
                "method": self.transport_consistency_method,
                "gain": self.dim2_gain,
                "has_gain": self.dim2_gain > 0,
            },
            "dim3_cross_rep_migration": {
                "baseline": self.cross_rep_migration_baseline,
                "method": self.cross_rep_migration_method,
                "gain": self.dim3_gain,
                "has_gain": self.dim3_gain > 0,
            },
            "n_dimensions_with_gain": self.n_dimensions_with_gain,
            "any_gain": self.any_gain,
        }


class BaselineComparator:
    """
    P7-7.3/P7-8.3/P7-EXIT-1b：3基线比较维度量化。

    123号§44："若不能更好地减少重复证明类、验证运输一致性或提高跨表示迁移，
    就保持为理论说明，不进入生产依赖。"
    """

    def compare(
        self,
        redundant_proofs_baseline: int,
        redundant_proofs_method: int,
        transport_consistency_baseline: float,
        transport_consistency_method: float,
        cross_rep_migration_baseline: float,
        cross_rep_migration_method: float,
    ) -> BaselineComparisonResult:
        """执行3维度基线比较。"""
        return BaselineComparisonResult(
            redundant_proofs_baseline=redundant_proofs_baseline,
            redundant_proofs_method=redundant_proofs_method,
            transport_consistency_baseline=transport_consistency_baseline,
            transport_consistency_method=transport_consistency_method,
            cross_rep_migration_baseline=cross_rep_migration_baseline,
            cross_rep_migration_method=cross_rep_migration_method,
        )

    def assert_exit_gate(self, result: BaselineComparisonResult) -> Dict[str, Any]:
        """
        P7-EXIT-1：出口门验证——3项比较中无任何一项有可测量增益→抛ExitGateFailureError。

        强制机制：不只是返回False声明——是运行时强制阻断。
        """
        if not result.any_gain:
            raise ExitGateFailureError(
                f"出口门失败：3项基线比较中无任何一项有可测量增益。"
                f"123号§44：若不能更好地减少重复证明类、验证运输一致性或提高跨表示迁移，"
                f"就保持为理论说明，不进入生产依赖。"
                f"当前增益: dim1={result.dim1_gain}, dim2={result.dim2_gain}, dim3={result.dim3_gain}"
            )

        return {
            "exit_gate_passed": True,
            "n_dimensions_with_gain": result.n_dimensions_with_gain,
            "result": result.to_dict(),
        }

    def check_label_downgrade(self, result: BaselineComparisonResult, current_label: str) -> Dict[str, Any]:
        """
        P7-EXIT-2：标注级别降级检查。

        强制机制：标注为`已实现`但3项比较无增益→降级为`实验分析`。
        """
        if current_label == "已实现" and not result.any_gain:
            return {
                "label_downgraded": True,
                "original_label": "已实现",
                "downgraded_label": "实验分析",
                "reason": "3项基线比较无增益——不能标注为'已实现'",
                "warning": "LabelDowngradeWarning: 标注降级为'实验分析'",
            }

        return {
            "label_downgraded": False,
            "current_label": current_label,
            "label_valid": True,
        }

    def assert_stop_condition(self, result: BaselineComparisonResult) -> Dict[str, Any]:
        """
        P7-STOP-1：停止条件检查——3项基线比较中无任何一项有可测量增益→抛StopConditionTriggeredError。
        """
        if not result.any_gain:
            raise StopConditionTriggeredError(
                f"停止条件触发：3项基线比较中无任何一项有可测量增益。"
                f"应停止当前方法的生产依赖。"
            )

        return {
            "stop_condition_not_triggered": True,
            "n_dimensions_with_gain": result.n_dimensions_with_gain,
        }

    def all_dimensions_quantified(self, result: BaselineComparisonResult) -> Dict[str, Any]:
        """
        P7-EXIT-1b：3个基线比较维度全部量化。

        验证3个维度都有具体的数值（不只是定性描述）。
        """
        dim1_quantified = (
            result.redundant_proofs_baseline is not None
            and result.redundant_proofs_method is not None
        )
        dim2_quantified = (
            result.transport_consistency_baseline is not None
            and result.transport_consistency_method is not None
        )
        dim3_quantified = (
            result.cross_rep_migration_baseline is not None
            and result.cross_rep_migration_method is not None
        )

        return {
            "dim1_quantified": dim1_quantified,
            "dim2_quantified": dim2_quantified,
            "dim3_quantified": dim3_quantified,
            "all_3_quantified": dim1_quantified and dim2_quantified and dim3_quantified,
        }
