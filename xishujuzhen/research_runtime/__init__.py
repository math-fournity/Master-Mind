"""
research_runtime: 数学大师系统新运行时包

按123号§54和plan要求，按Phase入口门递进创建。
Phase 1首次创建此包（NO-9约束：不在Phase 0一次性搭空框架）。

模块结构（按Phase递进创建）：
  models/         - 任务/工作区/义务类型定义（Phase 1）
  events/         - 原始/语义事件与checkpoint（Phase 1）
  state_reducer/  - 事件→状态（Phase 2）
  verification/   - 工具路由与证据状态模型（Phase 2）
  heuristics/     - 类型化时序模式—动作规则（Phase 3）
  experiments/    - 同可观测checkpoint分层随机实验（Phase 4）
  policy/         - 受约束动作选择（Phase 4）
  retrieval/      - 状态驱动检索（Phase 5）
  context_compiler/ - 微包编译（Phase 5）
  runtime/        - 在线循环（Phase 6）

架构基线：123号v1 §32(12步运行时) + §54(按Phase建立独立运行时包)
"""

__version__ = "0.1.0"
