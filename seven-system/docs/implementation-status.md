# 实现状态

## 一句话结论

Seven System v0.1.0 是一个可运行、可测试的 P0 + P1 scaffold 控制面，不是387号完整P1，更不是已完成的非特化实验平台。

## 已实现

| 能力 | 入口 | 结果 |
|---|---|---|
| 配置读取 | `preflight` | 先执行`runtime-config.schema.json`并拒绝未知字段，再进行语义校验；不读取密钥 |
| fail-closed preflight | `preflight` | 检查 D 盘、README、数据根、DB 名、Harness、目录隔离、工具策略与能力报告 |
| RuntimeManifest | `init-epoch` | 冻结 Epoch、真实源码树哈希、卷/README指纹、路径、输入空位和实现边界；返回成功前完成双轴自验 |
| 编排文件集 | `init-epoch` | 生成 phase plan、runbook、logging contract、scenario matrix、checkpoint、evidence index、verdict、summary |
| 幂等提交 | `dry-run` | 相同内容只提交一次；重复投递返回已有提交 |
| 冲突拒绝 | `dry-run` | 相同路径出现不同内容时拒绝覆盖 |
| P1 scaffold Gate | `dry-run` | 追加GateDecision、后续checkpoint、P1 scaffold verdict；一致的PASS或FAIL都是可重放终态 |
| 完整性验证 | `validate-epoch` / `status` | 执行本版Schema子集、两级逐文件索引、交叉hash与Epoch外local receipt；完整性和当前resume兼容性分轴 |

## 明确未实现

以下能力不存在，也没有隐藏入口：

- 数据库 migration、事务、CAS、outbox、lease/fencing；
- Redis 队列或分布式 worker；
- 387号完整P1的lease/fencing/outbox、崩溃恢复、重复投递和Redis重建矩阵；
- 真实 Devin Solver dispatch；
- provider/工具表面层面的无工具强制；
- 对现有 `trajectory.jsonl` 的 fail-closed 工具审计；
- CandidateManifest/BareBaseline/CasePack/ExperimentPlan 导入；
- D 盘 CAS 的 live→partial→seal；
- 答案/holdout Vault；
- Process/Proof/Leakage 三种盲化视图和 Judge；
- RunAudit、contrast、EvidenceRecord；
- RevisionProposal、prospective holdout、Promotion；
- 自动出题、Selector、分类学迁移、Active Learning；
- 多 Tell 组合和跨 Epoch 持续学习；
- Artifact GC、删除、清空队列或生产 pipe 回写。
- 签名、WORM或外部DB anchoring；当前local receipt只保证Seven API下append-once。

## 为什么 live 模式必然 BLOCKED

现有高并发系统的无工具规则主要靠 Prompt 和事后检查，但当前检查链存在 fail-open 风险：Harness 产出的是 `trajectory.jsonl`，历史 Collector 却查找不存在时会被当成“没有工具”的 `*.db`。此外，Harness 会二次包装 AGENTS，且 CLI 仍运行在 dangerous permission 模式。

因此本版 live preflight 无条件增加 `live_execution_implementation=BLOCK`。这不是否定现有题海数据价值，而是拒绝把“没有观测到工具”误写成“工具能力已被物理关闭”。

## 下一批工作包

1. D 盘 README 与数据根批准。
2. Strict DB port：expected DB fail-closed、显式 migration、唯一索引、ledger/outbox/CAS。
3. Harness adapter：单次 canonical prompt、结构化 argv、`trajectory.jsonl` fail-closed 审计、能力报告。
4. 物理答案 Vault 与三类最小权限 view。
5. 只读 CandidateManifest exporter；不写生产 pipe。
6. P2-P4 冻结对象导入后，再进入第一个单 Solver P5 工作包。
