"""WP-AU1 P6 Independent Audits — 盲化 Broker、三审、RunAudit。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P6 节和
docs/implementation/14-evidence-analysis-and-multi-epoch.md：

Blinding Broker 生成三个 view；qualified ModelRole adapter 可用 Devin 或 Codex
承担审计角色，但必须满足独立性和最小权限。

1. Process Auditor：trigger→binding→action→progress→termination 与 first divergence
2. Proof Judge：数学正确性与完备性
3. Leakage Auditor：完整 Solver payload 与 solution information atoms

分别 seal 后组装 RunAudit。单 episode 只陈述观察事实。

Judge 分歧、缺失、污染、升级和因果资格的机器规则见 14-evidence-analysis-and-multi-epoch.md；
未预注册的分歧不得由 Aggregator 自行裁决。

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB/Redis/D 盘/Solver/模型。
"""

from __future__ import annotations
