"""
matching: 模式匹配模块（261号§4.3）。

对activation-score筛出的top-K候选，逐一做LHS子图匹配+Guard条件检查。
"""

from .pattern_matcher import PatternMatcher, MatchedRule

__all__ = ["PatternMatcher", "MatchedRule"]
