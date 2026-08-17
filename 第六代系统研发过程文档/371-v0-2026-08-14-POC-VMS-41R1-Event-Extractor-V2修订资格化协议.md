# POC-VMS-41R1：Event Extractor V2修订资格化协议

**日期**：2026-08-14  
**阶段**：`SV-S2.7`  
**状态**：`CALIBRATION_PACK_COMPLETE / QUALIFICATION_PACK_PENDING / LIVE_NOT_AUTHORIZED`  
**前序失败证据**：VMS-41（368—369号）  
**任务追踪**：363号  

---

## 1. 目的

VMS-41没有资格化Event Extractor，同时证明旧资格合同把一个coarse observation view误当成唯一occurrence history。本协议为新版本冻结五项修订：

1. occurrence history与observation projection分离；
2. 不再冻结唯一event count；
3. anchor关系通过受限typed path/quotient判定，不要求直接邻接；
4. `status_at_occurrence`与`later_resolution`分离；
5. MERGE必须给出可审计的贡献对象和provenance frontier；
6. 文件权限改由pre/post目录快照与结构化文件事件联合判定，不再扫描命令字符串中的slash。

VMS-41的四个case、候选输出和人工诊断只能作为development/regression材料，不能进入VMS-41R1确认性holdout。

---

## 2. 主张与非主张

若未来全部Gate通过，本POC最多支持：

```text
EVENT_EXTRACTOR_V2_PROFILE_QUALIFIED_WITHIN_FROZEN_CASE_SCOPE
OCCURRENCE_PROJECTION_CONTRACT_EXECUTABLE
TYPED_PATH_AND_MERGE_CONTRIBUTION_GRADER_REPLAYABLE
```

它不支持：

```text
MODEL_GLOBAL_EVENT_EXTRACTION_CAPABILITY
ALL_MATHEMATICAL_DOMAINS
STREAMING_EQUIVALENCE
STATE_NORMALIZER_OR_TRACE_AUDITOR_QUALIFICATION
TELL_SELECTION_OR_CAUSAL_EFFECT
PRODUCTION_SCALE
```

---

## 3. 新对象层次

```text
Raw Solver Artifact
  ↓ candidate EventOccurrenceV2（发生史，允许细粒度事件）
ResolvedOccurrenceBundle（runner补span hash与source binding）
  ↓ hidden anchors + TypedPathClause
ObservationProjection（coarse anchor quotient）
  ↓ merge/status/forbidden/mechanical checks
EventExtractionEvaluationV2
  ↓ 独立盲审
ProfileQualificationDecision
```

Candidate不能输出Verdict、projection PASS或qualification字段。

---

## 4. Candidate Schema V2

Candidate顶层固定：

```yaml
schema_version: solve-vein/reasoning-trajectory-candidate/v2
trajectory_id:
problem_id:
source:
  carrier:
  source_artifact_ref:
  source_artifact_sha256:
events: []
```

每个事件：

```yaml
event_id:
sequence_index:
event_kind:
text:
canonical_math_state_id:
attributes: []
status_at_occurrence: ACTIVE | TENTATIVE | ESTABLISHED | SOLVED | UNKNOWN
later_resolution: STILL_ACTIVE | ABANDONED | CONTRADICTED | SOLVED | SUPERSEDED | UNKNOWN
source_span: {start:, end:}
incoming_edges:
  - source_event_id:
    relation:
    evidence:
    evidence_span: {start:, end:}
merge_contributions:
  - parent_event_id:
    contribution_role: LEMMA | CONSTRUCTION | CERTIFICATE | COUNTEREXAMPLE | BOUND | REPRESENTATION | OTHER
    contribution_claim:
    evidence_span: {start:, end:}
    use_in_target:
```

候选不再计算span hash。Runner从冻结raw bytes重算event/evidence/contribution span hash，避免模型为计算hash创建临时脚本。

任何`MERGE`目标必须满足：

- 至少两个不同MERGE父事件；
- `merge_contributions`与MERGE父ID集合完全相等；
- 每项有非空claim、use-in-target与有效source span；
- 非MERGE事件的`merge_contributions=[]`。

---

## 5. AcceptableSet V2

V2不含`expected_event_count`。它冻结：

- 必需anchor及唯一witness；
- anchor允许的event kind；
- `status_at_occurrence`和`later_resolution`各自允许集合；
- required/optional typed path；
- forbidden typed path/global relation；
- MERGE contribution constraint；
- extra-event机械门；
- 独立人工审计rubric。

### 5.1 Anchor映射

每个必需anchor必须恰好映射到一个candidate event；一个candidate event不得吞并两个anchor。没有anchor的candidate event是extra occurrence，不自动FAIL，但必须：

- source span在界内且非空；
- 与其他事件不具有完全相同的`span + kind + canonical state`；
- sequence与source occurrence不逆序；
- 有合法父边（root除外）；
- 人工审计确认不是修辞重复或凭空状态。

### 5.2 Typed path

每个`TypedPathClause`由一个或多个结构化pattern组成。Pattern是PathAtom序列：

```yaml
atoms:
  - allowed_relations: [CONTINUE, REFINE]
    min_repeat: 1
    max_repeat: 4
max_hops: 4
```

Evaluator枚举source-anchor event到target-anchor event之间不重复节点的有向路径，只接受与至少一个pattern完全匹配的路径。任意reachability不算PASS；超过`max_hops`、包含未允许relation或命中forbidden pattern均失败。

Projection记录：

- anchor→event映射；
- 采用的event path；
- relation sequence；
- 被折叠的extra occurrences；
- pattern ID；
- source evidence refs。

### 5.3 MERGE贡献

Hidden constraint不只数父ID。它要求：

- target anchor对应事件确有至少两个MERGE父；
- 每个required origin anchor可经允许的contribution path到达不同MERGE父；
- required origins到MERGE parents存在injective assignment；
- MERGE parents在合流前的非MERGE图上pairwise incomparable（若case要求）；
- candidate贡献对象与父事件集合一致；
- contribution evidence span真实；
- target的`use_in_target`说明如何使用各贡献。

祖先链上同一论证的两个中间节点不能仅凭两个event ID冒充独立合流。

### 5.4 资源上限

结构正确不等于可以无界搜索。V2实现对candidate JSON字节数、事件数、边数、path-search展开状态数和枚举路径数设置固定fail-closed上限；超限返回稳定`INVALID`错误码，不允许超时后把缺失路径误判为科学FAIL。当前离线实现上限为：candidate JSON 4 MiB、256个事件、2048条边、单次path query 100,000个搜索状态和4,096条已枚举路径。未来变更这些数值必须版本化并重跑校准与规模实验。

---

## 6. 状态时间语义

发生时状态与后来结局是两个不同事实：

```text
提出猜想时：status_at_occurrence=TENTATIVE
后来发现反例：later_resolution=CONTRADICTED
```

不得因后来失败，把最初事件回填成`ABANDONED`；不得因最终成功，把中间未证明步骤回填成`ESTABLISHED`。Hidden anchor分别校验这两个字段。

---

## 7. File-effect审计V2

Runner在启动前和结束后对workspace做结构化inventory：

```yaml
relative_path:
entry_type: regular_file | directory | symlink | other
size:
mode:
sha256:  # regular file
```

目录对账输出：

- created；
- modified；
- deleted；
- type_changed；
- symlink_or_escape；
- allowed/forbidden verdict。

仅比较前后快照不能发现“运行中创建、随后删除”的瞬态文件，也不能证明workspace之外没有副作用。因此Runner还必须从冻结的CLI/export/raw tool event中提取结构化文件事件：

```yaml
event_id:
operation: create | write | append | rename | delete | chmod | symlink | other
observed_path:
path_scope: workspace | approved_output | outside_workspace | unknown
provider_event_ref:
provider_event_sha256:
observability: complete | partial | unknown
```

最终`file_effect_verdict`是两个观察面的联合结果：

- pre/post inventory负责发现最终残留的created/modified/deleted/type-changed/symlink状态；
- raw结构化事件负责发现create-then-delete、rename链和workspace外尝试；
- inventory与event ledger必须互相对账；出现无法解释的残留变化或事件即FAIL；
- raw事件缺失、解析不全、path无法归一化或provider不保证事件完备时，最高只能是`PARTIAL_OBSERVABILITY`或`INCONCLUSIVE_PROTOCOL`；
- 不得从“前后快照相同”推导“运行期间没有文件副作用”。

首版Model只允许创建candidate输出；DONE、span hashes、evaluation与receipt由runner写。任何helper脚本、`/tmp`文件、rename或删除行为必须由上述联合物证发现或明确标成不可观察。数学文本中的`/2`、`/liminf`或Schema URI不会参与路径判定。

若操作系统层面无法观察workspace外effect，Verdict必须是`PARTIAL_OBSERVABILITY`或`INCONCLUSIVE_PROTOCOL`，不能声称全机零越界。

---

## 8. Qualification数据分区

```text
VMS-41 cases/output       → development + regression only
VMS-41R1 calibration     → v2 evaluator/提示词开发
VMS-41R1 qualification   → freeze后一次性解封，candidate此前不可见
future prospective       → 下一版本才可使用
```

同源改写、换壳、同raw切片共享`evidence_lineage_group_id`，不得冒充独立样本。

Qualification pack至少覆盖：

1. anchor之间有合法额外事件；
2. 发生时状态与后来结局不同；
3. 两个独立frontier真合流；
4. REUSE但不MERGE；
5. false MERGE；
6. 折返后融合旧知识与新分支；
7. 至少一个真实Solver raw trajectory；
8. source/span/未知字段/重复事件/非法路径等协议负例。

最终case数、exact IDs、attempt数和阈值须在preexecution freeze前另行落盘；本文件不授权当前live调用。

### 8.1 Calibration pack机器格式

Calibration不得只藏在单元测试构造函数中。首版冻结目录至少包含：

```text
vms41r1_calibration/
  source.txt
  acceptable-merge.json
  acceptable-reuse.json
  candidate-merge.json
  candidate-reuse.json
  scenario-matrix.json
  pack-manifest.json
```

`pack-manifest.json`绑定上述每个文件的相对路径、字节数、SHA-256、协议hash和pack ID；未知文件、缺文件、symlink、hash漂移与顺序漂移均FAIL。`source.txt`是唯一raw source；acceptable与candidate基准均由当前严格parser验证。

`scenario-matrix.json`不得嵌入任意Python或表达式。它只能引用一个冻结base，并使用受限JSON Pointer mutation DSL：

```yaml
op: replace | remove
path: /events/2/status_at_occurrence
value: SOLVED  # 仅replace拥有value
```

约束如下：

- JSON Pointer必须canonical，禁止空segment、`..`、负数和`-` append；
- `replace`目标必须已存在；`remove`目标必须已存在；
- mutation按数组顺序执行并写入materialized-input hash；
- runner必须保存每个场景的base hash、mutation hash、materialized candidate/acceptable hash与evaluation hash；
- 每个场景冻结逐轴expected verdict，不允许只比较一个总体PASS/FAIL；
- mismatch必须完整保留，不能让runner更新expected值；
- calibration场景全部标`DEVELOPMENT_ONLY`，永不计入VMS-41R1 qualification。

文件副作用场景也进入同一matrix，但使用独立声明式字段描述pre-state、model-window filesystem actions、provider event ledger、event observability、policy与expected verdict。所有真实动作只能发生在测试创建的临时根内；“越界”场景只构造/分类事件路径，不得真的写`/tmp`或其他批准根之外的位置。

---

## 9. 机械Gate

每case分别输出：

```text
protocol_verdict
artifact_verdict
anchor_coverage_verdict
typed_path_verdict
temporal_status_verdict
merge_contribution_verdict
forbidden_semantics_verdict
file_effect_verdict
manual_semantic_audit=PENDING
overall_status
```

机械PASS最高仍为`PENDING_BLIND_MANUAL_AUDIT`。不得由candidate、runner或同一个已看gold的Reviewer把它升级为profile PASS。

---

## 10. 人工审计与盲性

人工审计必须在Reviewer看到hidden acceptable set或机械错误摘要之前完成第一份sealed judgment。Reviewer只见：

- raw source；
- candidate occurrence DAG；
- 去掉gold结论的审计rubric；
- source span投影；
- arm/case随机代号。

随后才由Broker join机械结果。若顺序破坏，case只能用于failure localization，不能进入qualification numerator/denominator。

---

## 11. 资格门

Profile PASS至少要求：

- 所有artifact/protocol Gate PASS；
- anchor recall、typed-path recall与forbidden precision达到预注册阈值；
- temporal status无高严重度hindsight错误；
- true/false merge全部正确；
- 没有confirmed越权file effect；
- 盲人工审计达到阈值且分歧已按预注册规则处理；
- 每case仅一次科学attempt，失败与abstain完整保留；
- exact model/profile/effective UID可观察；
- final bundle、audit bundle和aggregate receipt可只读重放。

任何协议观察缺失、gold泄漏、blindness breach或unknown-start未解决，均不得计作科学FAIL或PASS。

---

## 12. 实施顺序与当前停止点

1. 新增独立v2 candidate/parser/evaluator，不修改v1历史语义；
2. 新增结构化file-effect inventory/auditor；
3. 构造calibration pack与正负candidate矩阵；
4. 运行全部离线测试并更新README；
5. 冻结全新qualification cases、Reviewer流程、阈值与attempt身份；
6. 生成preexecution freeze并做零模型preflight；
7. 只有route lock更新后才允许新的Devin one-shot；
8. 人工盲审先封存，随后机械join与aggregate。

当前已经完成第1—4步：独立V2 parser/evaluator、联合file-effect auditor、不可变calibration pack与离线runner均已落盘。Calibration冻结13个candidate场景和6个file-effect场景，19/19逐轴期望一致；26项projection、15项file-effect和12项pack/runner专项回归，共53项专项、174项解题侧全量回归通过。Calibration永久为`DEVELOPMENT_ONLY`，不资格化任何模型。停止点位于第5步；下一动作只能设计全新未见qualification pack、盲审流程、阈值和attempt身份，禁止模型、Solver、DB和Redis调用。
