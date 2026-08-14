# 编排、并发、失败与恢复

## 一句话结论

Seven采用`at-least-once delivery + idempotent fenced commit`，不声称exactly-once。任何调用在“是否已开始”不确定时，先reattach/reconcile或隔离，绝不能再调用一次碰运气。

## 身份层次

```text
scientific sample
└── logical WorkItem / role job
    └── physical Attempt 0..n
        └── provider process/session/request
```

retry是新的physical attempt，但沿用同一scientific sample lineage；不能当独立重复增加样本量。

## WorkItem状态

```text
QUEUED → LEASED → PREPARED → DISPATCHING
→ REQUEST_ACCEPTED / PROCESS_STARTED
→ GENERATION_STARTED
→ WRITERS_DRAINED
→ ARTIFACT_PREPARED
→ COMMIT_INTENT_RECORDED
→ ARTIFACT_SEALED
→ COMMITTING
→ COMMITTED
→ COMPLETED / SCIENTIFIC_COMPLETE / SCIENTIFIC_NEGATIVE
```

等待/恢复态：`HUMAN_PENDING / RETRY_SCHEDULED / RECONCILING`。它们都不是终态，不得在remainder检查中被当作已收口工作。

合法终态：`COMPLETED / SCIENTIFIC_COMPLETE / SCIENTIFIC_NEGATIVE / PROTOCOL_INVALID / RETRY_EXHAUSTED / QUARANTINED / BLOCKED / CANCELLED / FAILED_PERMANENT`。`COMMITTED`只说明该attempt的业务与artifact已原子关联，不自动代表科学endpoint或工作包已完成。

`WorkItemStateRegistry v1`的canonical状态全集分为：

- 可调度/所有权：`QUEUED / LEASED / PREPARED`；
- 外部执行：`DISPATCHING / REQUEST_ACCEPTED / PROCESS_STARTED / GENERATION_STARTED / SIDE_EFFECT_STARTED`；
- 人工/恢复等待：`HUMAN_PENDING / HUMAN_DECISION_RECORDED / RETRY_SCHEDULED / RECONCILING`；
- artifact/commit：`WRITERS_DRAINED / ARTIFACT_PREPARED / COMMIT_INTENT_RECORDED / ARTIFACT_SEALED / COMMITTING / COMMITTED`；
- 终态：上述九种合法终态。

不是每个kind都能进入全部状态；下表是子集约束。`REQUEST_ACCEPTED`与`PROCESS_STARTED`可以按adapter可观测性分别出现，但不可用进程fork伪造provider accepted；某边界不可观测时必须记`UNOBSERVABLE`并按该lane能力门BLOCK/降级，不能跳过证据态。

`GENERATION_STARTED`必须由首个模型event、非零generation token、partial trajectory等物证触发；不能凭进程已fork推断。

### 等待与恢复迁移

- `HUMAN_PENDING`：HumanTask已提交但quorum/有效Decision尚未形成。该状态不持有worker lease，不占用模型/Solver concurrency slot。对`HUMAN_GATE` kind，经HumanGateService验签并聚合后转`HUMAN_DECISION_RECORDED→COMMITTING`；对等待子Gate/permit的父WorkItem，子Decision已原子链接后可返回`PREPARED`再由新lease/fence继续。过期/冲突转`BLOCKED/QUARANTINED`。修改payload必须创建新WorkItem/task，不能将旧item退回去悄悄改输入。
- `RETRY_SCHEDULED`：已封存失败physical attempt，并按retry contract记录backoff、not-before、新attempt ordinal和permit剩余额度。到时后以新Attempt回到`QUEUED`；原Attempt仍保持终局物证。
- `RECONCILING`：调度停止正常dispatch，Reconciler按实体事实审核provider/CAS/DB/outbox/permit。只能转向原合法中间态、`COMMITTING`、`RETRY_SCHEDULED`或隔离/失败终态；不得直接跳到科学成功。

### 每种WorkItem kind的状态子集

| kind | 必须经过的主状态 | 允许的等待/恢复 | 允许的成功终态 |
|---|---|---|---|
| `MODEL_ROLE` | QUEUED→LEASED→PREPARED→DISPATCHING→accepted/started→artifact/intent/seal/commit | RETRY_SCHEDULED, RECONCILING | COMPLETED |
| `TARGET_SOLVER` | 上述执行链+资源/NoTool/observability裁决 | RETRY_SCHEDULED, RECONCILING | SCIENTIFIC_COMPLETE或SCIENTIFIC_NEGATIVE；协议损坏只能PROTOCOL_INVALID |
| `HUMAN_GATE` | QUEUED→HUMAN_PENDING→HUMAN_DECISION_RECORDED→COMMITTING | HUMAN_PENDING, RECONCILING | COMPLETED（Decision可为APPROVE/REJECT/REQUEST_CHANGES/QUARANTINE） |
| `DB_SCHEMA_APPLY` | QUEUED→LEASED→PREPARED→COMMIT_INTENT_RECORDED→SIDE_EFFECT_STARTED→COMMITTING | HUMAN_PENDING（permit前）, RECONCILING | COMPLETED |
| `ARTIFACT_RECONCILE` | QUEUED→LEASED→RECONCILING→COMMITTING | RECONCILING | COMPLETED |
| `AUDIT_ASSEMBLY / EVIDENCE_AGGREGATION` | QUEUED→LEASED→PREPARED→artifact/intent/seal/commit | HUMAN_PENDING（仅spec要求时）, RECONCILING | COMPLETED |
| `QUEUE_PROJECTION` | QUEUED→LEASED→PREPARED→COMMITTING | RETRY_SCHEDULED, RECONCILING | COMPLETED |

每个kind的完整allowed-transition table是`ProtocolRegistrySnapshot`的一部分。未知kind/state/event、跨越必经态、HumanTask仍未决定却标terminal，或非科学kind写`SCIENTIFIC_COMPLETE`都必须fail-closed。

## 幂等键与fence

幂等键至少绑定：

- Epoch/plan/role/case；
- input view hash；
- carrier profile或Solver resource contract hash；
- prompt/output schema/tool policy hash；
- arm/branch snapshot；
- scientific repeat ordinal。

lease续期和commit都带fence。新worker取得更高fence后，旧worker的cancel、artifact link、DB commit和queue ACK全部拒绝。

任何真实外部副作用还必须绑定`LiveRunPermit`和它的额度预留。`DISPATCHING`或`SIDE_EFFECT_STARTED`前，调度器在同一expected-revision transaction中append预留事件、创建`AuthorizationConsumptionReceipt(status=RESERVED)`并扣减可用额度。未知启动时receipt转`UNKNOWN_START_HELD`，不得释放后重调。

## 恢复规则

| 观察到的物理事实 | 决策 |
|---|---|
| provider/session仍活 | reattach或续lease，不重启 |
| 有可信正证据证明provider未接受请求且generation未开始 | 可按预注册infra retry创建新attempt |
| 接受/开始状态未知 | WorkItem转`RECONCILING`且permit receipt转`UNKNOWN_START_HELD`；无法对账时WorkItem终结为`QUARANTINED` |
| generation已开始后超时/截断 | 保存有效终止；按科学计划决定是否有下一repeat |
| partial存在、writer死 | 校验并恢复seal，或保留partial隔离 |
| artifact sealed、DB未commit | 转`RECONCILING`；仅在下方CommitIntent/fence/job/input/terminal/permit全门PASS时补交 |
| DB terminal、artifact缺失/错hash | quarantine |
| Redis丢失 | 从DB event/outbox重建 |
| 多attempt声称成功 | 冲突隔离，不自动任选 |
| HUMAN_PENDING时收到合法决定 | 验签/职责分离/冲突策略PASS后记录Decision并续转，不重建原payload |
| permit过期/撤销/额度不足 | 停止新dispatch；in-flight按revocation policy drain或quarantine |
| CAS sealed、DB缺失 | 只有durable CommitIntent+valid fence+matching job/attempt/input/manifest+合法terminal+未撤销permit全部PASS才补交，否则quarantine |

## Retry分类

- `infra_retry`：有可信正证据证明发生在provider未接受且generation未开始之前；“没有接受证据”本身不满足该条件；
- `planned_scientific_repeat`：ExperimentPlan预注册的独立repeat；
- `audit_retry`：报告格式/审计worker基础设施失败，但保留原audit attempt；
- `forbidden_retry`：retry until solved、retry until desired verdict、authoring until Devin fails、未知启动重呼。

`RETRYABLE_INFRA`是attempt分类，不是WorkItem终态。只有retry policy、预算、permit剩余额度和not-before均合法时，父WorkItem才进入`RETRY_SCHEDULED`；否则进入`RETRY_EXHAUSTED/BLOCKED/QUARANTINED`之一。

`UNKNOWN_START_QUARANTINED`同样只能作为physical Attempt的termination classification，不能写进`WorkItemStateRegistry`。它对应的逻辑WorkItem先进入`RECONCILING`；只有reconcile无法证明可reattach或未开始时才进入canonical `QUARANTINED`终态。

## 资源池

至少分：

```text
devin_author_pool
codex_author_pool
review_pool
judge_pool
solver_pool
human_queue
```

另设carrier-global limiter：例如Devin Solver与Devin认知worker共享后端账户/限额，但各自保留不同科学预算和启动策略。

每池冻结：max in-flight、launch interval、token/cost/wallclock、timeout、backlog、最大草稿/修订、retry和stop。Manifest冻结算法和上限；动态downshift写WorkEvent并按concurrency cohort分析。

历史Solver的3秒间隔/60并发只是站点经验。Devin认知角色从1并发资格测试起，不继承Solver常数。

## 背压与停止

任一项触发停止领取新任务：

- 总预算/统计停止规则完成；
- D盘/DB/Vault/queue tripwire；
- capability/profile漂移；
- authorization/permit/trust-root过期、撤销或额度tripwire；
- judge/review/human backlog超限；
- blind/leak/tool/view violation；
- error/rate-limit/unknown-start超过阈值；
- 用户停止。

停止顺序：停止全部新role和Solver dispatch → drain/冻结在途writer → checkpoint → reconcile清单 → 释放可安全释放的lease → 保留告警与物证。

## 故障矩阵

必须覆盖：

- dispatch前、accepted后、generation中、输出解析前后崩溃；
- provider ID未落盘；
- cancel丢失/晚到；
- worker断电、lease过期、stale fence；
- partial/fsync/rename/DB commit/outbox/ACK各边界；
- D盘掉线/满、DB中断/错误DB、Redis全丢；
- model UID/effort漂移、工具越权、output schema错误；
- 人工Gate超时、签名无效；
- duplicate message和重复启动；
- cost/usage不可观察、parent-child双计。
- HUMAN_PENDING被误当终态、决定到达与timeout竞态、多签冲突和payload version改写；
- RETRY_SCHEDULED时重用旧attempt/permit ordinal，或RECONCILING直跳科学成功；
- permit reserve后崩溃、unknown-start额度释放、撤销与drain竞态；
- 无CommitIntent/stale fence/错input/非法terminal的CAS补DB请求。

每种故障都要有预期terminal状态、允许的恢复动作、禁止动作和required evidence。
