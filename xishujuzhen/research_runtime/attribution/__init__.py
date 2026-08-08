"""
attribution: 增益归因模块（261号§4.9）。

记录提示链（Q1→Q2→...→Q10），
对每轮的进展增量归因给该轮发送的Q，
并对归因结果做反事实估计。
"""

from .gain_attribution import GainAttribution, GainRecord

__all__ = ["GainAttribution", "GainRecord"]
