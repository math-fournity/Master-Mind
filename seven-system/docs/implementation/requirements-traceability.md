# 需求追踪矩阵

## 使用方法

本表为**跨文档、跨工作包的规定性需求族**提供稳定ID。专题文档中的局部MUST不再手写一张易漂移总表；当前快照由[`tools/generate_normative_index.py`](tools/generate_normative_index.py)机械生成[`normative-requirement-index.v1.json`](normative-requirement-index.v1.json)，以`规范文档ID + 规范文本hash + 同文重复序号`形成稳定clause ID，并映射到精确需求ID或显式`LOCAL_ONLY`。纯移动/标题调整保留ID；条款文本变化、删除或自动分类语义变化必须进入[`normative-requirement-migrations.v1.json`](normative-requirement-migrations.v1.json)，不能静默换ID。实施工作包开始时把最后一列的`NOT_IMPLEMENTED`改为精确代码/Schema/测试/运行ref；没有证据时不得删除需求或写PASS。

索引使用line-level clause group作为机械单位，忽略代码围栏；规定性作者应当优先使用“必须/不得/应当/MUST/SHOULD”等明确token。为兼容现存文本，生成器只把不属于“对应/响应/效应/相应/适应/供应/反应”等复合词的单字“应”识别为规范助动词；含混命中必须在独立ReviewRecord中纠正，不能以机器命中替代语义判断。索引证明“条款没有从追踪面消失”，不替代语义判断：新快照中每条记录均为`PENDING_INDEPENDENT_AUDIT`，未来审计者须按[`normative-requirement-review-record.v1.schema.json`](normative-requirement-review-record.v1.schema.json)逐条确认或纠正需求ID、适用WP、consumer和`LOCAL_ONLY`理由。每次修改规定性Markdown后都必须重跑生成器；source hash漂移立即使WP-DOC0回退到`IN_PROGRESS`。

### 为什么条款还需要consumer

需求ID回答“这条规则属于哪个跨文档需求族”，consumer回答“哪个工作包必须在计划和完成物证里逐条交代它”。两者不是同一件事：一条局部规则可能暂时无法安全映射到跨文档需求族，但仍不能从实施计划中消失。

生成器必须为每条clause写`consumer_wp_ids`和`consumer_assignment_basis`。精确需求条款从RequirementMatrix继承consumer；尚未独立复核的`LOCAL_ONLY`条款临时写`WP-DOC0 + DOC0_TEMPORARY_PENDING_INDEPENDENT_SEMANTIC_REVIEW`，保证文档治理有人负责且机器remainder可计算。

这个DOC0临时consumer只表示**文档治理和追踪责任**，不分配、更不证明任何运行时实现责任。任何非DOC0工作包在进入`IN_PROGRESS`前，必须引用受信任AuditAssignment下签发的`NormativeRequirementReviewRecord`，并冻结独立复核后重新分配给该工作包的精确`normative_clause_ids`；不得用DOC0 catch-all跳过自己的适用条款。

| ID | 需求摘要 | 规范 | 工作包 | 代码/Schema/测试/证据 |
|---|---|---|---|---|
| AUTH-001 | 实施者不能自签AUDITED_PASS | 01 | WP-DOC0 | NOT_IMPLEMENTED AuditRecord |
| AUTH-002 | 目标规范与当前事实分轴 | 01 | WP-DOC0 | implementation-status |
| AUTH-003 | 无副作用development dependency与live activation dependency分开 | 01/03 | WP-DOC0 / WP-VLT0 / WP-HG0 / WP-CW0 / WP-CW-D1 / WP-CW-C1 / WP-QA0 / WP-DB1L / WP-DB1I / WP-RT1 / WP-SV1 / WP-IN1 / WP-TX1 / WP-CW1 / WP-QA1 / WP-CS1 / WP-ST1 / WP-EX1 / WP-AU1 / WP-EV1 / WP-RV1 / WP-VR1 / WP-GA1 / WP-OP1 | NOT_IMPLEMENTED WorkPackagePlan |
| AUTH-004 | 外部副作用必须消费父级EEA、不可扩权LiveRunPermit并原子预留/消费 | 07/13 | WP-HG0 / WP-RT1 / WP-CW-D1 / WP-CW-C1 / WP-QA0 / WP-DB1L / WP-DB1I / WP-SV1 / WP-CW1 / WP-QA1 / WP-CS1 / WP-EX1 / WP-AU1 / WP-RV1 / WP-OP1 | NOT_IMPLEMENTED |
| PORT-001 | TargetSolver只经solver_harness | 05 | WP-SV1 | NOT_IMPLEMENTED |
| PORT-002 | Devin可经ModelRole执行全部机器认知角色 | 05/ADR-001 | WP-CW-D1/WP-CW1 | NOT_IMPLEMENTED |
| PORT-003 | Codex与Devin使用统一ModelRole合同 | 05 | WP-CW0/WP-CW-C1/WP-CW-D1 | NOT_IMPLEMENTED |
| PORT-004 | 两个Devin adapter不共享workspace/session/config/receipt | 05 | WP-CW-D1/WP-SV1 | NOT_IMPLEMENTED |
| PORT-005 | phase代码不得直接调用provider CLI | 05 | WP-CW0 | NOT_IMPLEMENTED static test |
| PROFILE-001 | Devin精确请求`glm-5-2`、effort=high由UID编码 | 05 | WP-CW-D1 | NOT_IMPLEMENTED capability |
| PROFILE-002 | 每角色+精确profile+view/tool policy独立能力报告 | 05 | WP-CW-D1/WP-CW-C1/WP-CW1 | NOT_IMPLEMENTED RoleQualificationMatrix |
| PROFILE-003 | dispatch后禁止隐式跨载体fallback | 05/08 | WP-CW0 | NOT_IMPLEMENTED |
| PROFILE-004 | requested/effective/unobservable分开 | 05 | WP-CW0 | NOT_IMPLEMENTED |
| DATA-001 | 大对象在D盘CAS，答案/holdout在Vault | 06 | WP-VLT0 | NOT_IMPLEMENTED |
| DATA-002 | sealed artifact不可修改 | 06 | WP-VLT0 | NOT_IMPLEMENTED |
| DATA-003 | Arango只存小元数据/事件/ref | 06 | WP-DB1I | NOT_IMPLEMENTED |
| DATA-004 | Redis只是可重建投影 | 06/08 | WP-RT1/WP-OP1 | NOT_IMPLEMENTED |
| DATA-005 | CAS/DB两阶段提交可reconcile | 06/08 | WP-VLT0/WP-RT1 | NOT_IMPLEMENTED |
| DATA-006 | CAS补DB必须有durable CommitIntent、有效fence、匹配attempt和未撤销授权 | 06/08 | WP-RT1 | NOT_IMPLEMENTED |
| VLT-001 | Vault对象、view、ACL、access ledger和seal不可旁路 | 06/07 | WP-VLT0 | NOT_IMPLEMENTED |
| VLT-002 | solution-bearing request/raw event/output全部进入受限Vault | 05/07 | WP-VLT0 / WP-CW0 / WP-CW-D1 / WP-CW-C1 / WP-CW1 / WP-AU1 | NOT_IMPLEMENTED |
| DB-001 | 精确数据库身份，禁止默认DB | 06 | WP-DB1L | NOT_IMPLEMENTED |
| DB-002 | 只有StrictDatabasePort批准backend可用raw client | 06 | WP-DB1L / WP-DB1I | NOT_IMPLEMENTED |
| DB-003 | DDL必须计划hash+人门+fence+ledger | 06 | WP-DB1I | NOT_IMPLEMENTED |
| DB-004 | Schema未存在时先用D盘append-only bootstrap ledger并在建库后导入锚 | 06 | WP-DB1I | NOT_IMPLEMENTED |
| DB-005 | P0分别验证logical site、schema state、runtime DB与artifact reconcile能力 | 04/06/09 | WP-DB1L/WP-DB1I/WP-RT1 | NOT_IMPLEMENTED |
| DB-006 | 每个canonical对象有collection/key/index/transaction/sensitivity/owner/retention映射 | 04/06/15 | WP-DB1I/WP-RT1 | NOT_IMPLEMENTED |
| SEC-001 | 所有角色最小view | 07 | WP-VLT0/WP-CW1/WP-SV1 | NOT_IMPLEMENTED |
| SEC-002 | solution-bearing request/event/output进入Vault | 05/07 | WP-VLT0/WP-CW-D1/WP-CW-C1 | NOT_IMPLEMENTED |
| SEC-003 | Process/Proof/Leakage三审物理盲化 | 07/09 | WP-AU1 | NOT_IMPLEMENTED |
| HG-001 | ModelRole不能签HumanGate | 07 | WP-HG0 | NOT_IMPLEMENTED |
| HG-002 | Gate签名覆盖payload hash并满足职责分离 | 07 | WP-HG0 | NOT_IMPLEMENTED |
| HG-003 | 超时不默认PASS | 07 | WP-HG0 | NOT_IMPLEMENTED |
| HG-004 | HumanGate签名有canonical bytes、算法allowlist、信任根、轮换/撤销和防重放 | 07 | WP-HG0 | NOT_IMPLEMENTED |
| HG-005 | HumanTask等待态与Gate决定/过期跃迁闭合 | 07/08 | WP-HG0/WP-RT1 | NOT_IMPLEMENTED |
| RUN-001 | at-least-once + idempotent fenced commit | 08 | WP-RT1 | NOT_IMPLEMENTED |
| RUN-002 | generation start未知时quarantine不重呼 | 08 | WP-CW0/WP-SV1 | NOT_IMPLEMENTED |
| RUN-003 | retry不算独立科学样本 | 08/09 | WP-RT1/WP-EX1 | NOT_IMPLEMENTED |
| RUN-004 | carrier和role pool分别限流 | 08 | WP-CW1/WP-OP1 | NOT_IMPLEMENTED |
| RUN-005 | stop覆盖所有role和Solver dispatch | 08 | WP-RT1/WP-OP1 | NOT_IMPLEMENTED |
| CASE-001 | 自然题P2A/[P2B]→P3N→P3C | 09 | WP-IN1/WP-CS1 | NOT_IMPLEMENTED |
| CASE-002 | 生成题P3A→P3B→P3C | 09 | WP-QA0/WP-QA1/WP-CS1 | NOT_IMPLEMENTED |
| CASE-003 | 题面变化使旧核验/bare失效 | 04/09 | WP-QA0/WP-CS1 | NOT_IMPLEMENTED |
| CASE-004 | 禁止authoring retry until Devin fails | 09 | WP-QA0/WP-QA1 | NOT_IMPLEMENTED |
| CASE-005 | calibration与qualification/confirmation隔离 | 09 | WP-QA0 | NOT_IMPLEMENTED |
| TELL-001 | Taxonomy snapshot、TellCore、boundary、Tell↔Hint M:N和manifestation分层 | 04/03 | WP-TX1 | NOT_IMPLEMENTED |
| TELL-002 | Selector/Renderer/Binding/Injection/Critic组件版本与归责分离 | 03/09 | WP-ST1 | NOT_IMPLEMENTED |
| TELL-003 | P5 guided payload只由冻结TellStrategyRelease产生并留receipt | 09 | WP-ST1/WP-EX1 | NOT_IMPLEMENTED |
| SOLVER-001 | TargetSolver物理无工具、观测fail-closed | 09 | WP-SV1 | NOT_IMPLEMENTED |
| SOLVER-002 | P2B/P3B只是problem-only准入，不是P5 | 09 | WP-CS1/WP-QA1 | NOT_IMPLEMENTED |
| EXP-001 | P4前冻结arms/contrast/resource/stop/blind | 09 | WP-EX1 | NOT_IMPLEMENTED |
| EXP-002 | fresh restart problem-only为主资源baseline | 09 | WP-EX1 | NOT_IMPLEMENTED |
| EXP-003 | token-limit单独分层 | 09 | WP-EX1 | NOT_IMPLEMENTED |
| AUD-001 | 三审分别seal后才组装RunAudit | 09 | WP-AU1 | NOT_IMPLEMENTED |
| AUD-002 | Judge分歧、缺失、污染和升级规则预注册，Aggregator不得自选结论 | 14 | WP-AU1 | NOT_IMPLEMENTED |
| EVID-001 | 单episode不能产生因果supports | 09 | WP-EV1 | NOT_IMPLEMENTED |
| EVID-002 | 因果Evidence只来自预注册contrast | 09 | WP-EV1 | NOT_IMPLEMENTED |
| EVID-003 | cluster、missingness、multiplicity、stopping和估计器在P4冻结 | 14 | WP-EV1 | NOT_IMPLEMENTED |
| EVID-004 | Evidence status由版本化规则机械派生，不能自由写supports | 14 | WP-EV1 | NOT_IMPLEMENTED |
| REV-001 | 允许合法NO_CHANGE | 09 | WP-RV1 | NOT_IMPLEMENTED |
| REV-002 | fit/regression/prospective用途隔离 | 09 | WP-RV1 | NOT_IMPLEMENTED |
| REV-003 | prospective one-shot，查看后立即消耗 | 09 | WP-RV1 | NOT_IMPLEMENTED |
| TEST-001 | blocker tests优先，不能被confidence平均抵消 | 10 | WP-DOC0 / WP-VLT0 / WP-HG0 / WP-CW0 / WP-CW-D1 / WP-CW-C1 / WP-QA0 / WP-DB1L / WP-DB1I / WP-RT1 / WP-SV1 / WP-IN1 / WP-TX1 / WP-CW1 / WP-QA1 / WP-CS1 / WP-ST1 / WP-EX1 / WP-AU1 / WP-EV1 / WP-RV1 / WP-VR1 / WP-GA1 / WP-OP1 | NOT_IMPLEMENTED |
| TEST-002 | 测试收据绑定源码树和完整test IDs | 10/12 | WP-DOC0 / WP-VLT0 / WP-HG0 / WP-CW0 / WP-CW-D1 / WP-CW-C1 / WP-QA0 / WP-DB1L / WP-DB1I / WP-RT1 / WP-SV1 / WP-IN1 / WP-TX1 / WP-CW1 / WP-QA1 / WP-CS1 / WP-ST1 / WP-EX1 / WP-AU1 / WP-EV1 / WP-RV1 / WP-VR1 / WP-GA1 / WP-OP1 | NOT_IMPLEMENTED |
| TEST-003 | 每个外部边界必须故障注入 | 10 | WP-VLT0 / WP-HG0 / WP-CW-D1 / WP-CW-C1 / WP-QA0 / WP-DB1L / WP-DB1I / WP-RT1 / WP-SV1 / WP-CW1 / WP-QA1 / WP-CS1 / WP-EX1 / WP-AU1 / WP-RV1 / WP-OP1 | NOT_IMPLEMENTED |
| CLI-001 | 目标CLI/API/worker共用业务层、幂等键、fence、授权和receipt，登记入口remainder=0 | 13 | WP-DOC0 / WP-RT1 / WP-DB1I / WP-CW1 / WP-SV1 / WP-OP1 | NOT_IMPLEMENTED |
| CLI-002 | NOT_IMPLEMENTED命令在副作用前fail-closed，退出码语义稳定 | 13 | WP-DOC0 / WP-RT1 / WP-DB1I / WP-CW1 / WP-SV1 / WP-OP1 | NOT_IMPLEMENTED |
| DONE-000 | CompletionBundle绑定先提交的implementation subject commit，不自引用 | 11/12 | WP-DOC0 / WP-VLT0 / WP-HG0 / WP-CW0 / WP-CW-D1 / WP-CW-C1 / WP-QA0 / WP-DB1L / WP-DB1I / WP-RT1 / WP-SV1 / WP-IN1 / WP-TX1 / WP-CW1 / WP-QA1 / WP-CS1 / WP-ST1 / WP-EX1 / WP-AU1 / WP-EV1 / WP-RV1 / WP-VR1 / WP-GA1 / WP-OP1 | NOT_IMPLEMENTED |
| DONE-001 | Golden slice需自然/生成双入口与P4–P9 | 02 | WP-VR1 | NOT_IMPLEMENTED |
| DONE-002 | Evidence replay/orphan remainder=0 | 02/12 | WP-VR1 | NOT_IMPLEMENTED |
| DONE-003 | Production scale另需soak和恢复矩阵 | 02 | WP-OP1 | NOT_IMPLEMENTED |
| EPOCH-001 | 每Epoch冻结release/profile/budget/holdout，运行中漂移则seal并新建Epoch | 14 | WP-OP1 | NOT_IMPLEMENTED |
| EPOCH-002 | Active Learning按冻结CoverageTensor规则选择，跨Epoch防重复与holdout重用 | 14 | WP-OP1 | NOT_IMPLEMENTED |
| EPOCH-003 | 多Epoch有全局预算、kill-switch、pause/resume/seal与长期学习Verdict | 14 | WP-OP1 | NOT_IMPLEMENTED |
| INPUT-001 | CandidateManifest只读导入冻结producer bundle并禁止生产回写 | 03/15 | WP-IN1 | NOT_IMPLEMENTED |
| COST-001 | usage/cost/缓存写/父子调用必须完整、可对账，预算不可观测时fail-closed | 05/10/14 | WP-CW0 / WP-CW-D1 / WP-CW-C1 / WP-CW1 / WP-OP1 | NOT_IMPLEMENTED |

## Remainder规则

未来机器检查必须报告：

- 没有代码/Schema/测试/证据映射的MUST；
- 没有需求来源的production代码；
- 没有consumer的Schema/字段；
- 没有receipt的外部调用；
- 没有父hash的派生artifact；
- 没有合法terminal的WorkItem；
- 没有Gate的受控跃迁。

机器检查同时报告：跨文档需求族未映射数、无需求族/LOCAL_ONLY理由的条款数、待独立语义复核数，以及WorkPackagePlan未消费的`requirement_ids + normative_clause_ids`数。生成器的结构remainder为0只允许`READY_FOR_AUDIT`；只有受信任AuditAssignment下的ReviewRecord逐条覆盖且审计remainder=0，工作包才可能`AUDITED_PASS`。任一适用remainder非0，最高只能`AUDITED_PARTIAL`。

每份WorkPackagePlan必须绑定精确NormativeRequirementIndex ref/hash和已签NormativeRequirementReviewRecord ref/hash，并只从已验证review decisions中选取`consumer_wp_ids`包含本工作包的全部clause ID写入`normative_clause_ids`。checker以`review-expected - planned`和`planned - review-expected`分别计算missing/extra；任一非零都必须阻断`IN_PROGRESS`或后续receipt PASS，不能用自由文本scope或index里的临时consumer分配替代独立语义复核记录。
