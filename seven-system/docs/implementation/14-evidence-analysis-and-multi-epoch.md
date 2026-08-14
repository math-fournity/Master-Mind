# P6–P9分析、Verdict与多Epoch运行合同

> **状态**：`DESIGN_FROZEN / NOT_IMPLEMENTED`。

## 一句话结论

P6审计“发生了什么”，P7用预注册随机对照判断“哪个干预造成了什么”，P8决定是否修订，P9只聚合已有真值。多Epoch调度不得回头重写任何旧对象。

## P6审计组装规则

每个Solver episode预注册Process、Proof、Leakage三个lane。三份view、角色和profile分别冻结，各自seal后才由纯程序Aggregator生成`RunAudit`。

### 单lane状态

```text
VALID
INVALID_PROTOCOL
INCONCLUSIVE
MISSING
JUDGE_DISAGREEMENT
CONTAMINATED
```

`AuditLaneStatusRegistry v1`是版本化机器artifact，不是上述自由文本列表。每个entry冻结`code / terminal / causal_priority / required_evidence / allowed_upgrade / p9_effect`；未知code或非法转换一律拒绝。优先级固定为`CONTAMINATED > INVALID_PROTOCOL > JUDGE_DISAGREEMENT/MISSING/INCONCLUSIVE > VALID`，有利lane不能平均掉更高优先级的无效状态。

- `MISSING/INVALID_PROTOCOL/CONTAMINATED`不能被填成负结果；
- 审计worker基础设施故障可作`audit_retry`，但原attempt、view和全部输出必须保留；
- 数学Judge分歧时，按AuditPlan预注册规则增加第三个独立Judge、人工专家或formal checker；没有预注册规则时保留`JUDGE_DISAGREEMENT`，禁止Aggregator自选“看起来对”的报告；
- 调整Judge数量、规则或profile会产生新AuditPlan，不得覆盖原报告。

### RunAudit因果资格

```yaml
causal_eligibility: ELIGIBLE | PROCESS_ONLY | RESULT_ONLY | CONTAMINATED | INVALID | INCONCLUSIVE
```

`ELIGIBLE`至少要求协议完整、所需lane有效、无超预注册leakage budget和blind breach。它仍只是episode观察，不是Tell因果证据。

`CausalEligibilityRegistry v1`定义总函数。对AuditPlan要求的lane：任一确认污染→`CONTAMINATED`；任一必需lane协议无效→`INVALID`；任一必需lane缺失、分歧或不可观测→`INCONCLUSIVE`；只有process有效且结果lane按计划不可评→`PROCESS_ONLY`；只有结果有效且process按计划不可评→`RESULT_ONLY`；全部必需lane有效且无blind/leakage breach→`ELIGIBLE`。除此之外不存在默认分支。semantic verifier必须枚举六种lane状态的笛卡尔积，证明每个组合恰有一个输出。

## P7预注册分析合同

### 统计单位

- 科学采样单位是`problem/source_rollout cluster`，不是child run；
- 每个cluster在主分析中权重相等，同一题额外重复不能增大样本权重；
- 随机化block、stratum、seed和analysis set（ITT/per-protocol/process-only）在P4冻结。

### AnalysisMethodRegistry v1

ExperimentPlan必须从下列版本化方法选择，禁止运行后挑有利估计器：

1. `PAIRED_CLUSTER_DIFFERENCE_V1`：在同block/cluster内先求arm endpoint差，再对cluster等权平均；
2. `STRATIFIED_CLUSTER_BOOTSTRAP_V1`：固定seed、重抽单位和次数，给出效应区间；
3. `RANDOMIZATION_INFERENCE_V1`：只在保存了完整随机化集和分配约束时使用；
4. `DESCRIPTIVE_SMALL_N_V1`：样本不足时只报每cluster结果和effect direction，不写总体显著性主张。

每个method entry必须冻结`method_id/version`、endpoint类型、cluster/block key、missingness policy、contrast方向、精确算术/舍入、CI或p-value算法、随机源、seed派生、迭代/枚举上限、tie rule和输出Schema。随机重采样统一使用语言无关的`HMAC-SHA256(seed, method_id || contrast_id || counter)`字节流并做rejection sampling；禁止依赖语言或provider默认RNG。`PAIRED_CLUSTER_DIFFERENCE_V1`中每个eligible cluster恰好等权一次；bootstrap在冻结stratum内按registry约定的order statistic给区间；randomization inference在上限内穷举，否则保存每个采样assignment hash。

可执行参考artifact `analysis-golden-vectors.v1.json`至少覆盖：手算两cluster paired mean；首批bootstrap索引；invalid/missing不得填0；同source-rollout重复不得双计；相同p值按canonical `contrast_id`打破Holm排序。实现者和审计者必须复现全部中间值与最终值后才能启用method。

二元成功、process chain、成本、negative transfer和选择/拒绝率分别是endpoint，不能用一个加权总分抵消某一安全门FAIL。

### 缺失与协议失效

- 科学负结果进入ITT失败分子；
- 预注册拒绝/abstain是policy结果，不是missing；
- 基础设施invalid、观测不足、泄漏污染分别记数，不填0或当失败；
- 按arm报告missing/invalid/contamination率。若超过ExperimentPlan阈值或在arm间不平衡，主contrast为`INCONCLUSIVE_DUE_TO_PROTOCOL`；
- 停止后仍按冻结analysis set分析已纳入cluster，不删除不利结果。

### 多contrast与停止

P4必须冻结一个primary contrast或层级顺序。多个同级确认性contrast使用冻结的Holm等多重性规则；探索性contrast明标`EXPLORATORY`。停止规则只能是预注册样本上限、资源上限、安全tripwire或序贯规则；不能“跑到显著”。

`MultiplicityRuleRegistry v1`要求P5前冻结有限confirmatory family和canonical contrast IDs。`HOLM_V1`按`(raw_p, contrast_id)`排序，以十进制有理数比较第`i`项与`alpha/(m-i+1)`；探索性contrast永不进入family。`StoppingRuleRegistry v1`冻结`maximum_clusters`、资源上限、安全tripwire、允许的序贯边界、look schedule和动作。缺规则、计划外查看或看结果后扩样，使确认性结果成为`INCONCLUSIVE_DUE_TO_PROTOCOL`。

## EvidenceStatusRegistry v1

| 状态 | 机器条件 |
|---|---|
| `SUPPORTS` | primary contrast、协议可用、effect方向/门槛满足、无超限泄漏；scope限于实际覆盖 |
| `CONTRADICTS` | 协议可用且预注册主张的方向/安全界被反驳 |
| `DOES_NOT_SUPPORT` | episode成功但off-mechanism、只复述术语，或目标claim无合格contrast |
| `INCONCLUSIVE_DUE_TO_PROTOCOL` | 资源、blind、missing、leakage、观测或计划漂移阻止解释 |
| `NOT_TESTED` | 没有执行对应计划 |

Evidence Assembler不接受自由文本状态；它从冻结claim规则、contrast result和audit eligibility机械派生，并保留alternative explanations和scope limit。

## P8修订输入边界

P8先对`Core / applicability boundary / selector / renderer / injection / critic / model-resource / no-change`做失败定位。只有冻结`RevisionProposal`才能消耗新prospective pack；`NoChangeDecision`不创建candidate、不解封holdout。一次前瞻循环只支持`single_cycle_revision_learnability`，不支持长期持续学习PASS。

## P9 Verdict聚合

Verdict Builder只读sealed对象，根据`VerdictRuleRegistry v1`聚合：

```yaml
factory_pipeline: PASS | PARTIAL | FAIL | BLOCKED | INCONCLUSIVE_DUE_TO_PROTOCOL
scientific_hypothesis: SUPPORTS | CONTRADICTS | DOES_NOT_SUPPORT | INCONCLUSIVE | NOT_TESTED
six_gates:
  selectable: PASS | PARTIAL | FAIL | NOT_TESTED | INCONCLUSIVE_DUE_TO_PROTOCOL | NOT_APPLICABLE
  executable: PASS | PARTIAL | FAIL | NOT_TESTED | INCONCLUSIVE_DUE_TO_PROTOCOL | NOT_APPLICABLE
  terminable: PASS | PARTIAL | FAIL | NOT_TESTED | INCONCLUSIVE_DUE_TO_PROTOCOL | NOT_APPLICABLE
  composable: PASS | PARTIAL | FAIL | NOT_TESTED | INCONCLUSIVE_DUE_TO_PROTOCOL | NOT_APPLICABLE
  attributable: PASS | PARTIAL | FAIL | NOT_TESTED | INCONCLUSIVE_DUE_TO_PROTOCOL | NOT_APPLICABLE
  longitudinal_continual_learning: PASS | PARTIAL | FAIL | NOT_TESTED | INCONCLUSIVE_DUE_TO_PROTOCOL | NOT_APPLICABLE
single_cycle_revision_learnability: PASS | PARTIAL | FAIL | NOT_TESTED | INCONCLUSIVE_DUE_TO_PROTOCOL
production_scale: PASS | PARTIAL | FAIL | NOT_TESTED | BLOCKED
```

`VerdictRuleRegistry v1`实现claim级总映射：`SUPPORTS→SUPPORTS`、`CONTRADICTS→CONTRADICTS`、`DOES_NOT_SUPPORT→DOES_NOT_SUPPORT`、`INCONCLUSIVE_DUE_TO_PROTOCOL→INCONCLUSIVE`、`NOT_TESTED→NOT_TESTED`。off-mechanism成功既不是理论反证，也不是协议失败，禁止丢掉`DOES_NOT_SUPPORT`。多primary claims的优先级和聚合必须预注册；冲突状态保留逐claim map，summary默认`INCONCLUSIVE`，不能投票成PASS。Factory、Scientific、Six-Gate、Revision和Scale五个轴分别计算；每条规则绑定输入Schema hash和golden vectors，未知组合直接BLOCK。

任一安全/协议门FAIL不能被其他PASS平均。单Tell首期golden slice的组合门为`NOT_TESTED`，总结果最高是Six-gate PARTIAL；只有真实第二TellCore和组合矩阵才可升级。

## 多Epoch与Active Learning

### Epoch冻结

每个Epoch只绑定一组精确源码/Schema/registry/Tell releases、carrier profiles、CapabilityReports、CasePack、随机化、预算、价格快照、人门roster、stop规则和holdout分区。Epoch中不切换active release或版本；发现漂移则停机、seal、新建Epoch。

### CoverageTensor选择

Scheduler从冻结candidate pool按预注册priority rule选择下一格：未覆盖、证据不确定、边界/假朋友风险、负迁移价值、成本和数学分支平衡。规则、特征和权重都版本化；不允许看结果后手工把“有趣题”插队成确认样本。

`EpochSelectionRecord`还必须冻结`candidate_pool_ref/hash`、选择前CoverageTensor hash、每个候选的feature vector和排除理由、有理数权重、filter顺序、预算快照、deterministic tie seed、canonical cell ID排序和完整rank list。并列项按`sha256(selection_seed || canonical_cell_id)`升序打破；snapshot后手工插入只能进入新的探索pool，不能进入本轮确认pool。相同输入重放必须得到字节级相同排名。

### 跨Epoch资源与停止

- 同时有per-Epoch和program-global预算，全部provider、Solver、人工和存储成本记账；
- 全局kill-switch优先于任何新Epoch；
- 未完成Epoch保留为`PAUSED/BLOCKED/QUARANTINED`，不回滚删除；
- 同一evidence-lineage group不得在不同Epoch重复计为独立样本；
- 已解封holdout永久标记consumed；下一版修订必须用新prospective pack；
- 连续多Epoch的长期学习主张同时检查回归、灾难遗忘、漂移重验和negative transfer。

### 生产调度产物

`EpochSelectionRecord`、`CoverageTensorSnapshot/Delta`、`GlobalBudgetLedger`、`ActiveReleasePointerSnapshot`、`EpochSealRecord`、`CrossEpochDuplicateAssessment`和`LongitudinalLearningVerdict`都是append-only对象。`WP-OP1`的PASS必须证明至少一次create→run→pause/resume→seal→next-Epoch循环，且remainder=0。

独立审计必须双向重放：从选中cell反查精确input pool/tensor/budget，再从冻结输入前向算出相同rank；同时证明已消费holdout和duplicate lineage group不能重新进入后续确认pool。Active pointer变更、pause后的resume及next-Epoch创建与其他外部副作用相同，必须消费EEA→LiveRunPermit→原子额度预留链。
