"""
retrieval: 检索管线模块（258号§3.2步骤⑧ + 261号实现路径）。

三级递进检索：种子选择 → 图遍历 → 预算剪枝。
整合activation-score和pattern-matching。
"""

from .retrieval_pipeline import RetrievalPipeline

__all__ = ["RetrievalPipeline"]
