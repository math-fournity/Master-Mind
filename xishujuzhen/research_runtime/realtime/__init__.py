"""实时解析管线模块（04工作线§2.3-2.5）。

把solver-harness采集的trajectory数据实时喂给parser→retrieval→policy，
在Solver卡住时自动检索提示并注入。

组件：
- TrajectoryWatcher: 监控sessions.db，产出Round数据
- RoundBoundaryDetector: 检测轮次边界（Solver完成一轮输出）
- StallDetector: 检测卡点（STALL事件或超时无新节点）
- RealtimePipeline: 整合以上组件 + parser + retrieval + policy
- HintInjector: 通过tmux send-keys注入提示到Solver session
"""
