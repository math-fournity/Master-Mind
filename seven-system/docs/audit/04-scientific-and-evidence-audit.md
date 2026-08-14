# 科学协议、三审与证据重放审计

## Case入口

审计自然题是否真实走`P2A/[P2B]+P3N`，生成题是否真实走`P3A+P3B`；不得伪造自然题Authoring链或在生成题看到bare结果后改题。

核对：

- QuestionDraft版本和失效关系；
- calibration/qualification/confirmation分区；
- 所有失败草稿与成本；
- bare结果未被选择性删除；
- AdmissionDecision只在P3C由人门产生；
- Case角色包含正例、false-friend、boundary/unrelated或明确缺口。

## 实验协议

- TaxonomySnapshot、TellCore、TellStrategyRelease和全部组件hash在P4前冻结；
- oracle执行、automatic selector、renderer与Core证据没有互相冒充；
- TellManifestation/术语命中没有被当成目标动作或Core因果身份；
- Tell↔Hint M:N、trigger/guard/binding/progress/termination和版本继承可重放；
- ExperimentPlan在任何P5启动前sealed；
- main baseline是等资源fresh restart problem-only；
- arm调用数、output ceiling、tool权限和retry policy一致；
- lineage/direction/operation/critic/position的contrast没有被多改因素混淆；
- token-limit分层；
- problem/source cluster统计；
- selector abstain和错选按ITT保留；
- distractor与负例存在。

## 三审

检查三类view、mask、报告seal顺序和独立性。重点识别：

- Hint复述被当作target action；
- 注入前已走正确路线；
- restart/更多token/tool result造成first divergence；
- 正确proof走替代路线却归给Tell；
- lineage/Hint泄漏关键lemma；
- progress只是换符号或重复陈述；
- final answer事后合理化当作thinking过程。

## Evidence层级

- RunArtifact：物理事实；
- RunAudit：episode观察；
- EvidenceRecord：预注册contrast；
- CaseFamily aggregation：多个contrast的scope迁移；
- Revision/Promotion：prospective和人门。

审计禁止任何单episode直接写Tell因果supports。

## Evidence replay

从最终Verdict反向遍历：

```text
Verdict
→ EvidenceRecord / ProspectiveEvaluation
→ RunAudits / randomized contrasts
→ three sealed audits
→ RunArtifactBundles / InvocationReceipts
→ ExperimentPlan / CasePack / Releases
→ RuntimeManifest / CapabilityReports / source bundles
```

同时正向遍历所有planned对象，确认都有合法终态。两向集合差即remainder。

## P6 registry与因果资格重算

审计者从原始三lane报告重新加载`AuditLaneStatusRegistry`和`CausalEligibilityRegistry`，不得信任RunAudit里预填的状态。必须：

- 枚举所有启用lane状态组合，证明registry是总函数且每组恰有一个输出；
- 删除/复制/交换任一lane、制造blind breach、污染、missing和Judge disagreement，验证precedence与升级路径fail-closed；
- 核对增加第三Judge/人工/formal checker只能由原AuditPlan预注册规则触发；
- 证明episode状态只能生成RunAudit观察，不能直接生成因果EvidenceRecord。

## P7估计器与EvidenceStatus重算

审计者从sealed RunAudit和P4计划独立重算cluster、contrast、missingness、multiplicity、stopping和EvidenceStatus：

1. 使用[`analysis-golden-vectors.v1.json`](../implementation/analysis-golden-vectors.v1.json)先资格化审计实现；
2. 核对AnalysisMethod/Multiplicity/Stopping registry的精确版本、参数、HMAC随机流、seed、tie和rounding；
3. 对真实输入重算每个cluster中间量、effect、interval/p-value、Holm顺序与最终状态；
4. 突变删除/复制run、改arm、把invalid填0、改estimator、改停止look或改primary claim，验证assembler拒绝；
5. 检查`SUPPORTS / CONTRADICTS / DOES_NOT_SUPPORT / INCONCLUSIVE_DUE_TO_PROTOCOL / NOT_TESTED`均能机械到达，未知状态不能落入默认PASS。

## P8/P9总映射

Audit必须验证P8读取的是sealed P7 EvidenceRecord集合与`ProvenanceSnapshot`，不是尚未产生的最终EvidenceIndex。`VerdictRuleRegistry`从每个claim的EvidenceStatus到`scientific_hypothesis`必须是总函数，尤其保留`DOES_NOT_SUPPORT`；Factory、Scientific、Six-Gate、single-cycle revision和Production Scale分别重算，禁止平均、投票或用NOT_TESTED补PASS。

对NO_CHANGE与revision分别故障注入：重复解封holdout、fit/confirmation复用、candidate自批、旧Evidence改外键、回归失败仍promotion都必须BLOCK。最终EvidenceIndex只由P9生成，并能双向覆盖全部P0–P8对象。

## 多Epoch与Active Learning审计

对每个`EpochSelectionRecord`做双向确定性重放：

- 反向找到candidate-pool hash、选择前CoverageTensor、每个feature/exclusion、权重、预算、tie seed和规则版本；
- 前向使用相同filter、HMAC/tie算法计算完整rank，结果必须字节相同；
- 把新候选事后插入、修改权重/seed、重复lineage或已消费holdout重新放回，scheduler必须拒绝确认性lane；
- 核对per-Epoch与global budget、active pointer、pause/resume、seal和next-Epoch全部append-only；
- `resume`、next-Epoch和active release动作逐项追到父级EEA、LiveRunPermit和原子消费收据；
- 重放`create→run→pause/resume→seal→next`，确认旧Epoch版本不漂移、跨Epochduplicate和holdout remainder均为0。

## 科学与工程分轴

报告必须允许：

- Factory PASS + Tell CONTRADICTS；
- Factory PASS + Scientific INCONCLUSIVE；
- Factory FAIL/BLOCKED + Scientific NOT_EVALUABLE；
- Process chain PASS + proof FAIL；
- proof PASS + off-mechanism does_not_support；
- false-friend适当拒绝 + no proof，作为selector/termination正证据。

不能为了宣称系统成功而过滤负科学结果，也不能把协议损坏伪装成科学反例。
