"""
activation: 激活分数计算模块（261号§4.2）。

从ParseResult提取7维特征向量p_t，用权重矩阵W计算稀疏激活分数 a_t = W^T · p_t，
取top-K候选规则。
"""

from .score_calculator import ActivationScoreCalculator, ScoredRule

__all__ = ["ActivationScoreCalculator", "ScoredRule"]
