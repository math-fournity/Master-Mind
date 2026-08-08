"""
gradient: 提示梯度模块（261号§4.5）。

对同一义务ID的规则按Level排列形成梯度，
从高Level（低泄漏）到低Level（高泄漏）。
当某条规则泄漏风险>0.5时，降级到更高Level（更低泄漏）的替代规则。
"""

from .hint_gradient import HintGradient

__all__ = ["HintGradient"]
