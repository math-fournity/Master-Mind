"""
measurement: 进展度量原语（261号§3.4 progress-measurement）。

从dynamic-workspace的六元组状态中提取5个可测量分量，
计算进展偏序P_κ(S_t)。
"""

from .progress import ProgressVector, ProgressComparison, ProgressMeasurer

__all__ = ["ProgressVector", "ProgressComparison", "ProgressMeasurer"]
