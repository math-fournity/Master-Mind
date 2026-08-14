"""WP-CW1 Production Cognitive Workers.

本包实现生产认知工人：
- RoleQualificationMatrix / RoleQualificationCell：版本化资格矩阵
- ProductionRoleRouter：基于资格矩阵的生产路由
- IndependenceEnforcer：作者/审稿独立性、judge 视图隔离、伪独立性检测
- P3NWorkers / P6Workers：自然题审查与独立三审工人
- WorkerCapabilityReport：COGNITIVE_WORKER 能力报告

硬约束（SIDE_EFFECT_FREE）：
- 无 DB 写入、无 live model 调用、无 Solver 启动
- 所有状态由 RT1 的 lease/fence/WorkEvent 在内存中模拟
- blocker 与故障验收：未合格格路由、同会话审稿、judge 读越权 view

来自 docs/implementation/09-phase-pipeline-p0-p9.md：
- P3N：独立 Trace/Solution 视角形成 MechanismContract、RelationMapping、
  数学核验和对抗捷径审查
- P6：三个独立审计（Process Auditor / Proof Judge / Leakage Auditor），
  各自 blinding 后 seal，再组装 RunAudit；单 episode 只陈述观察事实
"""

from __future__ import annotations
