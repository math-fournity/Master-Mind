# 另一位AI的逐工作包实现手册

## 一句话结论

每次只实现一个依赖已满足的工作包，先冻结需求和负向测试，再写最小闭环；完成后只标`READY_FOR_AUDIT`并提交，不替未来审计者宣布PASS。

## 开工前

1. 确认工作目录、分支和`git status`；保留不属于本工作的用户改动。
2. 完整读取根/Seven `AGENTS.md`、实现入口、当前状态、工作包DAG和对应审计文档。
3. 从`work-package-board.md`选择第一个READY项。无副作用开发依赖在上游`READY_FOR_AUDIT`后可满足，但必须记录`inherited_audit_debt`；任何激活动作仍要求适用上游`AUDITED_PASS`。若是未审canary，不能用一句“用户同意”替代机器授权对象：还必须由父级`ExternalExecutionAuthorization`、其不可扩权`LiveRunPermit`和原子`AuthorizationConsumptionReceipt(RESERVED)`共同精确覆盖，并标记`UNAUDITED_AUTHORIZED_CANARY`。
4. 按`work-package-plan.v1.schema.json`生成并验证`WorkPackagePlan`，冻结baseline commit/tree、canonical DAG、需求/clause scope、spec/Schema/input hashes、允许文件、测试、站点配置和授权边界；除历史DOC0 bootstrap plan外，每个新Plan必须显式选择`SIDE_EFFECT_FREE`或`AUTHORIZED_LIVE_CANARY`。前者授权refs为null且预算全零，后者三个授权refs完整且至少一项预算为正；没有Plan不得写`IN_PROGRESS`。
5. 在看板写`IN_PROGRESS`、实施者、开始时间、attempt ID和stop condition。
6. 若需要新权限、真实写库、付费模型调用、生产Solver或HumanGate，Plan必须是`AUTHORIZED_LIVE_CANARY`，并同时验证父级EEA、不可扩权LiveRunPermit和原子`AuthorizationConsumptionReceipt(RESERVED)`；缺任一项就写BLOCKED并停止。Devin/Codex认知adapter的首个真实canary还必须等待DB1I v2/等价SchemaState、RT1 DatabaseRuntime/Artifact Reconcile以及VLT0/HG0激活条件，禁止以“QA0离线”名义走file-only调用旁路。
7. 若本包会修改规定性文档，先记录旧`NormativeRequirementIndex` hash；完成时重跑生成器并验证新source hashes与remainder，禁止手改生成JSON。

## 设计检查点

写代码前必须回答：

- 目标和非目标是否唯一？
- 允许修改哪些模块，哪些外部系统只读？
- 对外端口和对象Schema是什么？
- 状态机、幂等键、fence和terminal状态是什么？
- 敏感view落哪里，谁永久不可见？
- 什么算provider accepted/generation started？
- 哪些失败能retry，哪些必须quarantine？
- unit/component/integration/fault/live分别如何证明？
- CompletionBundle需要哪些artifact？

答不出来就先修规定性文档，不要边编码边发明协议。

## 实施顺序

1. 更新或新增Schema及semantic verifier测试；
2. 先写blocker/negative tests；
3. 实现纯数据对象和状态机；
4. 实现fake/in-memory adapter；
5. 实现真实边界adapter；
6. 接CLI，但默认仍fail-closed；
7. 加integration和fault injection；
8. 仅在授权后跑最小live canary；
9. 收集receipt/capability/evidence；
10. 更新状态、操作手册、Schema索引和实现映射。

不要从CLI命令直接开始。没有对象、状态、错误和证据合同的CLI只是不可审计旁路。

## 建议代码边界

目标目录可按职责演进：

```text
src/seven_system/
├── contracts/             领域对象与semantic verifier
├── runtime/               WorkItem/Event/lease/fence/outbox/reconcile
├── storage/               CAS/Vault/view/seal
├── database/              Strict port/site/plan/apply（唯一Arango backend）
├── adapters/
│   ├── solver/            DevinSolverAdapter，唯一solver_harness调用点
│   ├── model_role/        Devin/Codex/fake adapters
│   └── intake/            只读producer adapters
├── human/                 HumanTask和HumanGate
├── caselab/               P2/P3
├── experiments/           P4/P5
├── audits/                P6及blinding
├── evidence/              P7
├── revision/              P8
├── verdict/               P9
└── operations/            CLI、checkpoint、alerts、projection
```

目录名可在工作包中细化，但外部CLI/DB/Vault/HumanGate旁路禁令不能改变。

## 代码和Schema同步

每次新增对象：

1. 定义Schema ID/version；
2. 添加Schema loader/validator；
3. 添加semantic verifier；
4. 添加合法/缺字段/未知字段/跨字段攻击fixture；
5. 更新Schema README和对象目录；
6. 生成对象时保存Schema/hash；
7. consumer先验证再读取；
8. 旧对象迁移只新增版本/assessment，不原地改写。

## 外部执行同步

每个真实adapter都必须先实现：

- CapabilityReport builder+independent verifier；
- binary/adapter/source/profile绑定；
- structured argv或API request；
- request/raw event/output的正确sink；
- accepted/started物证；
- timeout/cancel/reattach/reconcile；
- usage/cost/termination收据；
- exact role/view/tool policy测试；
- bypass static test。

只有Capability PASS并被RoleExecutionContract精确引用后，adapter才可进入对应live lane。

认知adapter的fake和protocol stub可以在`SIDE_EFFECT_FREE`计划下开发；任何真实Devin/Codex请求只能在`AUTHORIZED_LIVE_CANARY`计划下运行，并复用RT1的WorkEvent、permit reservation、artifact commit和reconcile链。QA0“不启动Target Solver、不写Redis投影”不等于“不使用canonical DB runtime”。

## 测试和自检

至少运行：

```text
schema tests
unit tests
contract/component tests
security/blocker tests
fault-injection tests
full existing regression
diff/format/static bypass checks
```

需要live canary时，必须把调用次数、profile、预算、输入敏感性、输出sink和停止条件写入授权对象。禁止“顺便多试几次”。

## 完成与交接

1. 更新实现文档、`implementation-status.md`和operations；operations只加入已经验证可运行的命令；
2. 运行全套回归与文档链接/Schema检查；
3. 显式路径`git add`、检查cached diff并提交**implementation subject commit**；未经用户授权不push；
4. 在该精确commit/tree上生成绑定测试收据；若需要修代码，产生新subject commit并重来；
5. 在D盘CAS外部生成`ImplementationCompletionBundle`，不得把它写进自身绑定的tree；仅WP-DOC0在VLT0尚未实现时可使用12号定义的Git bootstrap record，并且之后必须导入CAS；
6. 若改过规定性文档，重跑并验证`docs/implementation/tools/generate_normative_index.py`；把看板改为`READY_FOR_AUDIT`，可用第二个evidence-index commit只记录bundle ref/hash；
7. 下游无副作用开发可按依赖开放，但所有激活路径继续阻塞并继承审计债；
8. 交接写清subject commit、bundle、可选index commit、claims/nonclaims、授权未用部分、失败物证和审计复跑命令。

## 自动连续推进规则

另一位AI可以在以下条件全部满足时继续下一个工作包的**开发部分**：

- 当前工作包已`READY_FOR_AUDIT`且CompletionBundle完整；
- 下一个工作包的development dependencies都达到`READY_FOR_AUDIT`；
- 将所有尚未独立审计的依赖写入`inherited_audit_debt`；
- 下一动作不需要新的外部权限/费用/写入/生产运行；
- 没有用户新消息、P0/P1 finding或资源告警；
- 看板明确标READY。

若下一动作需要真实DB、模型、Solver、正式HumanGate或canonical运行，则必须另查activation dependencies和逐次授权。实施AI最终可以交付`SYSTEM_CANDIDATE_READY_FOR_EXTERNAL_AUDIT`，但不能自写`FACTORY_GOLDEN_SLICE_AUDITED`或`PRODUCTION_SCALE_AUDITED`。

## 禁止反模式

- 一次同时实现多个工作包，导致无法归责；
- 直接把387字段复制成代码而不做semantic verifier；
- 用当前交互AI手工完成本该由系统执行的流程；
- hard-code测试输出或让builder自报PASS；
- retry until solved/desired/Devin fails；
- 调试时放宽答案、DB、tool或Gate权限，完成后忘记恢复；
- 修改绑定历史报告的源码却继续引用旧report；
- 把自己写的CompletionBundle当独立审计结论。

## 实施AI最终交接格式

```markdown
## 工作包
WP-ID / spec hash / baseline → final commit

## 实现
文件、接口、Schema、状态迁移

## 验证
命令、测试数、fault cases、live receipts

## Claims / Nonclaims
精确列出

## 外部副作用
DB/Redis/D/模型/Solver/人工Gate逐项计数

## 已知问题与阻塞
Finding、风险、解除条件

## CompletionBundle
路径、hash、状态=READY_FOR_AUDIT

## 独立审计复跑
入口、命令、期望结果
```
