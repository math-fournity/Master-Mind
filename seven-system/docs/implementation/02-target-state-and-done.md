# 目标系统与 Definition of Done

## 一句话结论

完整 Seven System 不是“能调用几个模型”的脚本，而是一条可以把冻结失败题或受控生成题，经过准入、预注册实验、三审、对照聚合和人门，变成可重放 EvidenceRecord 的证据生产线。

## 最终用户能做什么

一个操作者应能：

1. 导入冻结的自然bare候选，或提交一个受控出题brief；
2. 选择已经通过能力门的Codex或Devin认知profile承担出题/核验/审计；
3. 让目标Solver只经Devin Harness执行公平的bare/guided/control实验；
4. 在任何阶段暂停、查看物证、恢复或安全隔离；
5. 得到过程、证明、泄漏三种独立审计；
6. 得到contrast级EvidenceRecord，而不是一段“看起来成功”的故事；
7. 经人工 Gate决定NO_CHANGE、修订、发布、限制或拒绝；
8. 从最终Verdict反查全部输入、版本、调用、成本、失败与恢复事件。

## 完整逻辑组件

| 组件 | 最终职责 |
|---|---|
| Snapshot/Intake | 只读导入题海与第六代系统的冻结bundle |
| CaseLab | 自然题机制审查、受控出题、数学核验、角色冻结 |
| Role Runtime | Devin/Codex认知adapter、Target Solver adapter、人工任务与Gate |
| Orchestrator | WorkItem、随机化、资源、lease/fence、停止和恢复 |
| CAS/Vault | 大对象、答案、holdout、最小授权view和两阶段seal |
| Audit Plane | Process、Proof、Leakage三路独立审计 |
| Evidence Plane | RunAudit、contrast、EvidenceRecord、证据谱系 |
| Revision/Governance | NO_CHANGE、候选修订、prospective、active pointer和回滚 |
| Operations | 队列投影、背压、告警、checkpoint、reconcile和成本 |

## 三个完成状态

### `SYSTEM_CANDIDATE_READY_FOR_EXTERNAL_AUDIT`

这是实施AI能够自行交付的最高状态：全部目标代码、Schema、测试、操作手册和CompletionBundle已经存在；在逐项外部副作用授权下，至少一条真实golden-slice candidate run已经执行并封存。它明确表示**尚未独立验收**，运行产物不能自动写成科学Evidence或active release。

### `FACTORY_GOLDEN_SLICE_AUDITED`

这是“系统真的可以工作”的第一条完成门，必须同时满足：

- 真实D盘CAS/Vault和逻辑DB事件账可用；
- HumanTask/HumanGate具备身份、职责分离与验签；
- `DevinCliModelRoleAdapter(glm-5-2 High)`与一个Codex adapter均完成精确profile资格验证；
- golden slice中每个adapter至少完成预注册的代表性真实角色调用，且公共`ModelRolePort`在合同层可路由全部机器角色；未测试的`role × profile`单元仍为BLOCKED，不能由代表性调用继承PASS；
- Target Solver只经Harness，NoTool/SafeLaunch/AnswerIsolation/Harness资源能力PASS；
- 一条自然题准入路径和一条生成题准入路径闭合；
- 一个Case完成P4–P9并形成contrast EvidenceRecord；
- 三审分离、人工Gate和答案隔离没有越权；
- 至少一次故障注入后恢复成功；
- Evidence replay与orphan/remainder检查为0；
- 独立审计PASS。

### `PRODUCTION_SCALE_AUDITED`

在前者之上还必须满足：

- 多worker、各carrier资源池和Redis投影持续运行；
- 每个生产启用的`role × carrier profile × view/tool policy`单元都有独立CapabilityReport，Devin“可承载全部机器角色”的架构能力不被误写成所有单元天然PASS；
- 预注册的并发、背压、cost和backlog阈值通过soak；
- D盘、DB、Redis、provider、worker和HumanGate故障矩阵通过；
- pause/stop/resume/reconcile在真实状态下可重复；
- 多Epoch连续运行无丢任务、双提交、孤儿artifact或证据覆盖；
- 值班操作手册由非开发者按文档复现；
- 再次独立审计PASS。

## 科学完成不是工程完成

工程和科学必须分轴：

```yaml
factory_pipeline: PASS | PARTIAL | FAIL | BLOCKED
scientific_hypothesis: SUPPORTS | CONTRADICTS | DOES_NOT_SUPPORT | INCONCLUSIVE | NOT_TESTED
```

工厂正确地产出“Tell没有增益”仍然可以是工程PASS。为了让验收好看而把科学FAIL改写成基础设施FAIL，或过滤负题，都是审计失败。

## 明确不属于DONE

- CLI可以运行；
- 两个adapter可以import；
- 某次模型输出了一道题；
- Devin碰巧没做出一道题；
- 一次guided运行成功；
- unit test全绿但没有真实能力收据；
- dry-run P1 scaffold通过；
- 一个漂亮episode出现目标题词；
- Golden Slice通过但没有生产soak。

## 最终验收物证

最终至少提交：

- 冻结源码commit/tree hash与全部Schema hash；
- RuntimeManifest、CapabilityReports和HumanGate readiness；
- 两个认知adapter及Target Solver的真实调用收据；
- 自然/生成两条Case路径artifact；
- ExperimentPlan、资源/随机化记录和P5全部arm；
- 三审、RunAudit、contrast EvidenceRecord；
- 故障注入、恢复、checkpoint和EvidenceIndex；
- `ImplementationCompletionBundle`集合；
- 独立`SystemAuditRecord`与最终Verdict；
- 明确nonclaims和未覆盖CoverageCell。
