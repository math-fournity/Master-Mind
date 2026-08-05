"""
state_reducer模块：事件→状态

对应132号P2-2—P2-9 + P2-CODE-1。

模块结构：
- q0.py: Q_0任务实例化（P2-1）
- workspace_store.py: 工作区读写（P2-2）
- obligation.py: 义务图构建+超边存储（P2-3）
- verification_gate.py: F_t→V_t验证门（P2-4）
- evidence.py: 证据状态模型+冲突状态（P2-5）
- reducer.py: StateReducer + 多观察者重建（P2-6）
- progress.py: 进展偏序+状态等价（P2-9）
- migrate.py: Phase 2 ArangoDB migration
"""

from .q0 import create_q0_ramsey, Q0_RAMSEY
