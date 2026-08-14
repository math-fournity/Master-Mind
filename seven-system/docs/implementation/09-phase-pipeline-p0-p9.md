# P0–P9完整阶段管线

## 一句话结论

Seven有两条Case入口，但进入P4后共享同一条预注册实验—三审—证据—修订—Verdict管线。任何Gate失败都保留物证并停止，不能靠人工复制输出跨过去。

## 总体DAG

```text
自然题：P2A → [P2B] → P3N ┐
                               ├→ P3C → P4 → P5 → P6 → P7 → P8 → P9
生成题：P3A → P3B ──────────┘
```

## P0 Preflight

**目标**：证明本Epoch所有实际依赖能力和治理前置可用。

至少检查：

- RuntimeManifest和源码/Schema/profile hashes；
- DatabaseLogicalSite、DatabaseSchemaState、DatabaseRuntime、ArtifactCommitReconcile、CAS/Vault、Harness资源、NoTool、SafeLaunch、AnswerIsolation；
- 每个将被调用的CognitiveWorker `role × carrier profile × view/tool policy`资格格和对应CapabilityReport；
- HumanGate policy、actor roster、职责分离、验签readiness，以及从被审repo/DB/CompletionBundle之外取得的站点owner pinned trust-root hash；
- D盘、路径、空间、密钥边界、holdout和成本预算；
- 本Epoch每类真实DB/模型/Solver/Human动作的有效`ExternalExecutionAuthorization`，以及逐run不可扩权`LiveRunPermit`、可用consumption ordinal、原子reserve/consume能力和剩余额度；
- 当前数据库Schema满足实际live对象的唯一性、事务与防重放要求；仅有现存`seven_*_v1` scaffold/离线映射时，HumanGate、外部模型、Solver、Redis写、canonical Epoch和active release全部保持`BLOCKED`，直至隔离的`seven_*_v2`或更高版本原子Schema通过`DatabaseSchemaStateReport`；不得用题海/`system/`集合或无版本集合充当“等价结构”。

缺任一适用项即`BLOCKED`，不得进入live阶段。

P0不得把“上游已`AUDITED_PASS`”误当成外部执行授权，也不得把“用户给了EEA”误当成已获得可消费permit。前者解决依赖可信度，后者只给出上限；每次副作用仍必须由精确LiveRunPermit的一个原子预留ordinal承载。独立审计运行自身若需要真实DB、provider或Solver，同样适用该规则，并须在`AuditAssignment`中预先允许对应scope。

## P1 Canonical Dry Run

**目标**：不调用真实模型/Solver，使用fake adapters演练DAG、Schema、幂等、lease/fence、artifact提交、Gate、stop和recovery。

PASS要求：重复delivery无重复副作用；每个失败状态可重放；权限拒绝生效；remainder=0。当前v0.1 scaffold不等于本阶段完成。

## P2A Discovery Evidence Audit

自然题入口。按problem聚合历史attempt，核对题面版本、模型/资源、trajectory、NoTool/observability、proof/result和duplicate lineage。

输出CandidateManifest和HistoricalBareEvidenceAssessment。历史失败只可用于发现；物证不够时进入P2B，不得直接冒充确认性baseline。

## P2B Current Bare Qualification

对不可变自然题运行当前protocol的problem-only bare。无Tell、无Hint，不属于P5。

输出：`RunArtifactBundle(purpose=intake_bare)`、BareBaseline、BareQualificationResult。一次失败不是稳定bare失败，资格按预注册repeat和problem级分布判定。

## P3N Natural Case Review

独立Trace/Solution视角形成MechanismContract、RelationMapping、数学核验和对抗捷径审查。自然题不伪造AuthoringBrief/QuestionDraftVersion。

## P3A Authoring & Question Release

受控生成入口：

```text
MechanismContract + CoverageCell
→ AuthoringBrief
→ qualified Devin/Codex Question Architect
→ QuestionDraftVersion
→ statement-only Adversarial Editor
→ independent Math Verifier
→ Human G-Q-RELEASE
→ immutable QuestionRelease
```

每个角色都可由任一通过该角色能力门的adapter执行；角色路由和profile预先冻结。题面变化使全部下游审查失效。

## P3B Generated Bare Admission

只把QuestionRelease公开题面交给TargetSolverPort做problem-only bare。没有Tell/Hint，不属于P5。成功/失败都保留，禁止修改题面或继续生成直到失败。

输出：RunArtifactBundle、BareBaseline、BareQualificationResult。

## P3C Case Role Freeze

合并自然题`P2A/[P2B]+P3N`或生成题`P3A+P3B`物证。HumanGate签发AdmissionDecision和CasePackVersion，冻结positive/false-friend/boundary/unrelated等角色。

模型只能给建议，不能签G-CASE-ROLE。`admitted_for_process_only`不得进入结果层确认性claim。

## P4 Preregister

冻结：

- TaxonomySnapshot、TellCore、TellStrategyRelease及所有组件hash；
- arms、contrasts、randomization block/seed；
- BranchSnapshot与ResourceContract；
- solver/model/profile、重复和停止；
- blind views、endpoints、成本和统计；
- technical failure处理；
- audit roles和independence。

计划开始后修改任一项必须新建ExperimentPlan。

## P5 Target Solver Experiment

只由TargetSolverPort→DevinSolverAdapter→solver_harness执行。

所有guided payload只能由冻结TellStrategyRelease经Selector/Renderer/Binding/Injection链产生并留receipt。核心对照至少包括等资源fresh restart problem-only，按需要增加lineage、direction、lineage+direction、distractor、operation/critic和位置内neutral。token-limit单独分层；同一problem/source rollout按cluster处理。

科学负结果不自动重试；工具/不可观测/协议漂移分别记invalid或quarantine。

## P6 Independent Audits

Blinding Broker生成三个view；qualified ModelRole adapter可用Devin或Codex承担审计角色，但必须满足独立性和最小权限。

1. Process Auditor：trigger→binding→action→progress→termination与first divergence；
2. Proof Judge：数学正确性与完备性；
3. Leakage Auditor：完整Solver payload与solution information atoms。

分别seal后组装RunAudit。单episode只陈述观察事实。

Judge分歧、缺失、污染、升级和因果资格的机器规则见[`14-evidence-analysis-and-multi-epoch.md`](14-evidence-analysis-and-multi-epoch.md)；未预注册的分歧不得由Aggregator自行裁决。

## P7 Contrast Evidence

按预注册contrast、problem/source cluster和成本口径聚合。只有contrast级EvidenceRecord可以对Tell因果claim写supports/contradicts。Case-family层只能聚合既有contrast records扩展scope。

估计器、missingness、multiplicity、stopping和Evidence status均从`AnalysisMethodRegistry/EvidenceStatusRegistry`选择并在P4冻结，具体合同见[`14-evidence-analysis-and-multi-epoch.md`](14-evidence-analysis-and-multi-epoch.md)。

P7唯一阶段输出是sealed `EvidenceRecord`集合及其seal/root hash；它不生成`EvidenceIndex`或`ProvenanceSnapshot`。P8开始时才对该sealed集合冻结只读`ProvenanceSnapshot`，最终`EvidenceIndex`仅由P9生成。

## P8 NO_CHANGE或Revision

先独立failure localization：Core、boundary、selector、renderer、injection、critic、model/resource哪层出错。

- 无修订必要 → signed NoChangeDecision，不解封holdout；
- 需要修订 → RevisionProposal、fit/regression、candidate freeze、一次性prospective、两次HumanGate。

同一证据不能同时fit和confirmation；看过的holdout立即消耗。

## P9 Verdict与Checkpoint

输出：

- Factory/Scientific分轴Machine Verdict；
- SixGateVerdict及NOT_TESTED；
- Human-readable Summary；
- RuntimeCheckpoint；
- EvidenceIndex/DAG；
- cost和coverage delta；
- next eligible work/coverage cells。

Evidence replay必须证明所有planned对象、attempt、artifact、audit、Gate和evidence有且仅有合法归宿。

多Epoch、CoverageTensor调度、跨Epoch预算、holdout消费和长期学习主张不属于单Epoch P9；它们由WP-OP1按[`14-evidence-analysis-and-multi-epoch.md`](14-evidence-analysis-and-multi-epoch.md)另行验收。

## Authoring Evaluation A/B

作者profile选择分成没有循环依赖的两个阶段：

### `AuthoringBakeoff-A`（WP-QA0）

- 同一MechanismContract、CoverageCell、AuthoringBrief和预算；
- Devin `glm-5-2` High、Codex候选及可选其他profile分别生成；
- 隐去作者身份；
- 只评估数学正确、机制忠实、正交距离、捷径/泄漏、多样性、人工修订量和成本；
- 不启动Target Solver，不使用bare结果。

### `AuthoringBakeoff-B`（WP-QA1/P3B后）

- 只使用A阶段已经人工发布、不可变的专用calibration QuestionRelease；
- 用problem-only Target Solver准入结果增加bare维度；
- bare结果不得回流修改同一题稿或选择性删除成功题；
- A/B calibration对象都不得进入P5/P7确认性Evidence；
- 默认profile还必须在未见brief qualification pack复验；
- 可得到分角色默认，不强制全局唯一赢家。

## 阶段Gate表

| Phase | 必需核心物证 | PASS核心 | 失败动作 |
|---|---|---|---|
| P0 | Manifest/Capabilities/Human readiness/External authorizations | 全部精确绑定且适用运行时能力已验证 | BLOCKED |
| P1 | DryRun/Recovery/Idempotency | 无副作用重复、remainder=0 | 修复后新attempt |
| P2 | Candidate/Bare artifacts | problem资格可审计 | discovery-only/排除 |
| P3 | Mechanism/Question/Reviews/Gates | 题与角色冻结合法 | 补证/拒绝/quarantine |
| P4 | ExperimentPlan/Resources | 所有输入sealed | 禁止P5 |
| P5 | Solver receipts/artifacts | 协议和资源一致 | negative/invalid/quarantine |
| P6 | 三审/RunAudit | views和报告分别sealed | review/quarantine |
| P7 | sealed EvidenceRecord set | contrast和scope完整，集合seal/root hash可重算 | 禁止Revision |
| P8 | NoChange或Revision lineage | holdout/回归/人门合法 | reject/restrict/quarantine |
| P9 | Verdict/Checkpoint/Replay | DAG完整、remainder=0 | PARTIAL/FAIL/BLOCKED |
