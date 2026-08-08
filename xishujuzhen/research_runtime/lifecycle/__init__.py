"""
lifecycle: 模式生命周期管理模块（261号§4.6）。

管理模式的生命周期状态转移：
observed → candidate → intervened → validated → published → retired
"""

from .lifecycle_manager import LifecycleManager, LifecycleState

__all__ = ["LifecycleManager", "LifecycleState"]
