"""Seven System adapters — provider-specific 认知角色适配器。

本包实现 ModelRolePort 协议的具体 provider adapter：
- DevinCliModelRoleAdapter（WP-CW-D1）：Devin CLI 认知角色适配器
- CodexExecModelRoleAdapter（WP-CW-C1）：Codex CLI exec 认知角色适配器

硬约束（AGENTS.md rule 4）：
- Devin CLI 不专属于 Solver；认知角色统一经 provider-neutral ModelRolePort
- DevinCliModelRoleAdapter 不得复用 Solver 的 port、workspace、session、AGENTS、
  能力报告、收据或资源池
- 人工复核/人门分别走未来 HumanTaskPort/HumanGateService；禁止阶段代码旁路调用任何 CLI

当前状态：SIDE_EFFECT_FREE / IMPLEMENTED_PENDING_EVIDENCE
- 协议 stub、profile 解析、capability report builder、parser 已实现
- live canary 被 DB1I SchemaState / RT1 Runtime/Reconcile / VLT0 / HG0 激活依赖阻塞
- 不调用任何真实 Devin CLI / Codex CLI / DB / D-volume
"""
