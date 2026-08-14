# ADR-001：Devin与Codex双认知载体，Solver执行面独立

- **状态**：ACCEPTED
- **日期**：2026-08-14
- **取代**：此前“Devin只绑定目标Solver、认知角色不使用Devin”的过窄表述

## 背景

目标Solver必须继续由Devin CLI承载，以保持与题海bare基线一致。但这不意味着Devin CLI不能执行出题、审稿、数学核验、Judge或Auditor。用户明确要求Seven同时允许Devin CLI的GLM-5.2 High和Codex承担机器认知角色。

## 决策

角色与载体正交：

```text
TargetSolverPort → DevinSolverAdapter → solver_harness

ModelRolePort → DevinCliModelRoleAdapter
              → CodexExecModelRoleAdapter
              → future qualified adapters
```

Devin认知候选的本机catalog基线为：

```yaml
carrier: devin_cli
cli_version_observed: 3000.4.25 (7e8e528a)
requested_cli_model_arg: glm-5-2
catalog_display_name: GLM-5.2 High
normalized_reasoning_effort: high
effort_encoding: model_uid
```

这只是2026-08-14的只读catalog事实，不是端到端Capability PASS。CLI当前没有独立`--effort`参数；实现必须冻结models-list快照，并从export的generation model证据核对UID。若无法观察effective profile，确认性lane保持BLOCKED。

## 不变量

1. 只有Target Solver作业可以进入`solver_harness`。
2. Devin认知角色必须走`ModelRolePort`，不得复用Solver workspace/session/AGENTS/receipt/capability/resource pool。
3. Codex与Devin均不直接从phase模块调用；只允许各自批准的adapter封装外部调用。
4. 两个adapter使用相同`RoleExecutionContract`和`AIInvocationReceipt`核心Schema。
5. 每个角色、模型、effort、tool/view policy组合分别做能力探针。
6. dispatch后不自动跨载体fallback。
7. 人工Gate不由任一模型adapter调用或签发。

## 结果

- 可以逐角色选择Devin或Codex，甚至同时运行不同角色。
- Bakeoff可以选择不同角色的默认profile，不要求全局唯一赢家。
- 需要carrier级总限流；Devin Solver与Devin认知worker共享后端额度但不共享科学资源合同。
- 所有包含候选解/密封解的Devin/Codex请求、事件和输出进入受限Vault。

## 明确非主张

- 不证明Devin或Codex更会出题；
- 不证明`glm-5-2` High已能满足任一确认性角色；
- 不证明两个同模型fresh session构成异模型独立；
- 不授权当前代码调用任何远程模型。
