# 解题侧非线性脉络分析模块

**模块**：`system/solve_vein_analysis/`  
**确定性核心版本**：`0.1.0`  
**当前状态**：离线结构 POC 已通过；VMS-40已把单Gold升级为五层真值、多视图relation、多轴state与AcceptableSet并完成6 case/26 candidate确定性验证；VMS-41四个真实role attempt已全部消费并封存，artifact/replay链PASS但冻结机械结果0/4、协议`INCONCLUSIVE_PROTOCOL`，当前Event Extractor profile仍为`NOT_QUALIFIED`；事后诊断只用于failure localization。VMS-41R1的独立V2 occurrence/projection evaluator和pre/post inventory+结构化file-event联合审计已实现；不可变开发校准包含13个candidate+6个file-effect场景并19/19逐轴一致；全新未见qualification pack包含6个case、6个hidden reference candidate和4个negative mutation，已完成零模型自检并冻结；0.4.1角色资产、`poc_vms_41r1.freeze.json`零模型preexecution freeze、live runner shell、不可消费LiveRunPermit/盲审包计划、sealed manual judgment合同、hidden join simulator、fake materializer、final qualification join receipt和临时append-only写包dry-run也已冻结。VMS-42 State Normalizer离线核心、零模型资格包、hidden join、reviewer judgment合同、final receipt、unseen qualification extension与DAG writeback sidecar已新增：2个case/4个candidate证明多轴绑定、legacy projection不吞轴和fail-closed反例，资格包证明public/hidden分离、2个reference/2个negative重放和零副作用receipt，hidden join证明candidate bundle经hidden dictionary/acceptable评分、negative保留和development-only非资格化边界，reviewer judgment合同证明public/candidate bundle盲审对象、hidden未见attestation与六轴Verdict一致性，final receipt证明manual/hidden任一FAIL都保留为final FAIL且双PASS仍不资格化，unseen extension新增2个case/4个candidate并机械证明新旧case/candidate ID不重叠、expected drift拒绝和public/hidden隔离，DAG sidecar证明PASS normalized bundle可以按DAG event_id/topological order生成不可变annotation bundle且不改写DAG。VMS-43 Trace Auditor结构审计已新增：synthetic complex DAG覆盖branch、failure、revisit、merge和recovery，缺少必需family时输出科学FAIL，state sidecar hash/order不一致时fail-closed。当前295项全量测试PASS（2026-08-24实跑）；上述机械合同最高仍不超过`PENDING_BLIND_MANUAL_AUDIT`/`LIVE_NOT_AUTHORIZED`，live角色资格实验仍未授权。VMS-39冻结profile下effective root `AGENTS.md`上限为16,384 bytes，Tell/Trace已移出控制面；流式抽取、生产接入和规模性能仍未测试
**理论来源**：第六代研发文档 344 号  
**实施与边界来源**：第六代研发文档 345 号  
**POC 协议与结果**：第六代研发文档 346—387 号

---

## 1. 先说结论

这个模块不是现有入题侧 `system/vein_analysis.py` 的改写版，也不调用它。它是解题侧独立模块，解决的是另一类输入：Solver 在解题过程中发生的分叉、失败、折返、复用和多支合流。

当前 `0.1.0` 已经能对一个严格结构化的 `ReasoningTrajectory` 完成：

1. 构造保留全部发生关系的有向无环图；
2. 分开构造状态 FCA 上下文和转移 FCA 上下文；
3. 用 Next Closure 枚举形式概念，并用独立穷举 oracle 对账；
4. 进行带边来源的 RCA-style 关系尺度迭代；
5. 识别七类过程 trace；
6. 验证批处理与逐事件重放的最终科学指纹一致；
7. 生成原子封存、哈希可核对的离线结果目录。

实验性前端已经能以独立工作目录调用 Devin CLI，并让三个认知角色写出候选 JSON；POC-VMS-35 证明了去掉额外 Devin sandbox 后，入题侧既有的“模型直接写文件 + 进程退出后封存 export”合同可以在解题侧复现。这个结果不等于三个角色已经合格：同一实跑还暴露了 gold 语义、总体裁决策略和 DONE 语法问题，机械总判定为 `INCONCLUSIVE_PROTOCOL`。

它现在仍不能声称：能从任意自然语言 thinking 自动、无损地生成正确的结构化轨迹；能把 tmux 中看到的 thinking spin 当成完整、稳定、可确认性使用的推理记录；能连接数据库；能实时接入正在做题的 Solver；能支撑生产规模。

---

## 2. 与入题侧的隔离边界

### 2.1 不允许修改或复用的对象

本模块不修改、导入或覆盖：

- `system/vein_analysis.py` 及同名 `.ref`、`.ai-check`；
- `system/process_absorb.py`、`system/enter.py`；
- `system/assets/vein_analysis/`；
- `system/tests/vein_analysis/`；
- 现有入题侧运行目录和历史产物；
- 入题侧 `AGENTS.md` 运行资产。

### 2.2 独立命名空间

| 类型 | 解题侧位置 |
|---|---|
| 代码 | `system/solve_vein_analysis/` |
| 运行资产 | `system/assets/solve_vein_analysis/` |
| 测试与夹具 | `system/tests/solve_vein_analysis/` |
| 大型运行物证 | `/data/master-mind-solve-vein-data/` |
| 模块说明 | `system/docs/solve_vein_analysis.md` |
| 操作手册 | `system/docs/solve_vein_analysis_runbook.md` |

隔离不是临时约定，而是回归测试的一部分：测试会解析本包的 import AST，阻止对入题侧模块的依赖。

交互tmux运行还增加物理隔离：live workspace必须在批准的D盘专属根，不能放在repo内。VMS-36因repo级Read deny拒绝自身workspace；VMS-37虽改到D盘，又被`Read(/Volumes/**)`拒绝。两次都是自己的配置矛盾，不是D盘或tmux失效。现行候选合同是no-sandbox + `dangerous`，把可读、可写、禁止动作冻结到本attempt的`AGENTS.md`中，并审计export/tool events；不再以会伤及自身workspace的整卷deny代替角色边界。

Devin还会加载用户级`~/.config/devin/AGENTS.md`。它属于候选模型真实可见的控制面，不能从实验描述中省略：确认性运行的freeze、launch receipt和invocation receipt都必须记录其sanitized locator、字节数与SHA-256，并在启动前重验。`dangerous`只解除Devin自身权限确认，不构成操作系统隔离；若export缺少tool event，工具边界只能记为`UNOBSERVABLE`，不能因为“没看到调用”而推断零调用。

---

## 3. 为什么不能继续使用线性脉络

入题侧面对的是已经整理成稿的解答。即使证明在创作时有探索，输入到入题管线中的成品通常是一条线性叙述。

解题侧面对的是发生史：

```text
根状态
├─ 分支 A → 矛盾/放弃
│             └─ 带着新信息折返到旧数学状态
├─ 分支 B → 得到引理 B
└─ 分支 C → 得到引理 C
               B + C → 合流状态 → 结论
```

把它压成列表会把“前后相邻”误写成“因果相承”；把它强制变成树则无法保留一个合流节点的多个父输入。因此，模块的真值层必须是带类型边的事件 DAG，而不是列表或树。

---

## 4. 三个必须分开的数学对象

### 4.1 事件 DAG：发生事实

事件 DAG 记录某个 Solver 运行中实际发生了哪些推理事件，以及事件之间的显式关系。节点身份是“这一次出现”，不是抽象数学状态。

### 4.2 观察/分区层：用什么粒度看发生史

同一事件 DAG 可以按局部步骤、策略片段、失败—恢复段、全局骨架等不同粒度观察。该层回答“怎样看”，不能覆盖“发生了什么”。

### 4.3 FCA 概念格：对象—属性闭包

FCA 的对象分别是状态 occurrence 或 transition；属性是冻结、带命名空间的描述。概念格回答哪些对象共享哪些闭合属性。它不是事件 DAG 的替代品，也不是时间顺序本身。

关系尺度把边的邻接信息转成来源可追踪的关系属性，从而允许 FCA 观察“某类状态通过某类边连接到某类状态”。当前实现是有限的存在量词尺度，明确标为 RCA-style，而不是完整 Multi-FCA/RCA 实现。

---

## 5. 核心数据合同

### 5.1 `ReasoningTrajectory`

顶层对象严格只允许五个字段：

```json
{
  "schema_version": "solve-vein/reasoning-trajectory/v1",
  "trajectory_id": "trajectory-id",
  "problem_id": "problem-id",
  "source": {
    "carrier": "fixture",
    "source_artifact_ref": "opaque/source/ref",
    "source_artifact_sha256": "64-lowercase-hex"
  },
  "events": []
}
```

`source.carrier` 当前只允许：`fixture`、`devin_cli`、`codex_exec`、`imported`。允许某个 carrier 名称不等于对应 live adapter 已经通过能力门。

### 5.2 `ReasoningEvent`

```json
{
  "event_id": "e3",
  "sequence_index": 3,
  "event_kind": "RETURN",
  "text": "Solver 再次考察先前状态，并带入新约束。",
  "canonical_math_state_id": "state_modular_constraint",
  "attributes": [
    "action:revisit",
    "knowledge:new_constraint",
    "representation:modular"
  ],
  "status": "ACTIVE",
  "source_span": {
    "start": 320,
    "end": 470,
    "sha256": "64-lowercase-hex"
  },
  "incoming_edges": [
    {
      "source_event_id": "e2",
      "relation": "REVISIT",
      "evidence": "explicit return after contradiction"
    }
  ]
}
```

### 5.3 occurrence 与 canonical state

- `event_id`：一次出现的不可复用身份；
- `canonical_math_state_id`：可在多个 occurrence 间相同的抽象数学状态。

折返必须创建新事件。若直接把旧节点连回去，会制造时间环并丢失“带着什么新信息回来”。

### 5.4 枚举

事件类型：

```text
STATE | DECISION | FAILURE | RETURN | SYNTHESIS | CONCLUSION
```

状态：

```text
ACTIVE | ABANDONED | CONTRADICTED | SOLVED | UNKNOWN
```

边关系：

```text
CONTINUE | REFINE | BRANCH_FROM | CONTRADICT | ABANDON |
REVISIT | REUSE | DEPENDS_ON | MERGE | CONCLUDE
```

任何未知字段、未知枚举、非有限 JSON 数、bool 冒充 int、重复 ID、缺失父边、指向未来/自身的边都会 fail-closed。属性数组和同一 occurrence 的入边数组在解析时按稳定键规范化，因此仅改变这两个无语义数组的排列不会改变 canonical trajectory 或科学指纹；事件数组的时序顺序则绝不重排。

---

## 6. 管线

完整管线分成认知前端与确定性后端，二者不能用一次 PASS 互相替代：

```text
冻结 raw Solver artifact
  ↓ Event Extractor（候选事件、span、边）
候选 ReasoningTrajectory
  ↓ State Normalizer（状态身份/状态/关系的受限修订）
规范化 ReasoningTrajectory
  ↓ Trace Auditor（独立审计，不替后端算法做决定）
角色输出与调用收据
  ↓ 严格 parser / source-span / gold-or-acceptable-set / protocol gate
可受理 ReasoningTrajectory
```

只有越过前端资格门的轨迹，才允许进入下面的确定性后端：

```text
冻结 ReasoningTrajectory
  ↓ 严格解析与发生顺序验证
ReasoningDag
  ├─→ state FormalContext ─→ Next Closure ─→ state concepts
  ├─→ transition FormalContext ─→ Next Closure ─→ transition concepts
  ├─→ RCA-style relational scaling ─→ fixed point + provenance
  ├─→ deterministic trace rules
  ├─→ flattened/tree comparison projections
  └─→ incremental prefix replay
         ↓
  AnalysisBundle + AuditReport + scientific fingerprint
```

### 6.1 图构造

每个非根事件至少有一个入边；所有入边的源 occurrence 必须已经发生。含 `MERGE` 的目标必须有至少两个不同的语义父输入，语义父输入包括 `MERGE`、`REUSE`、`DEPENDS_ON`。

### 6.2 两个 FCA 上下文

状态上下文对象是 `event_id`，主要属性来自：

- 事件的显式 namespaced attributes；
- `event_kind`；
- `status`。

`canonical_math_state_id` 在当前版本中刻意作为身份关系留在 DAG/折返规则中，不进入 FCA 属性。否则每个具体状态 ID 会污染本应可泛化的概念内涵。根、分叉、折返和合流身份也由图层负责，不在基础状态上下文里重复编码；关系尺度会通过有来源的边属性把必要结构带入后续概念。

转移上下文对象是 `edge_id`，主要属性来自：

- relation 类型；
- 源/目标事件类型；
- 源/目标状态。

首版没有把源/目标的全部显式属性复制到每一条转移上，也没有把“是否跨 canonical state”作为二值属性；这些是后续 schema 版本的候选，不得在当前结果中假装已经实现。

两个上下文不能混成一个：状态相似性和转移相似性是不同的问题。

### 6.3 FCA 正确性对账

生产算法使用 Next Closure。POC 的小上下文还枚举所有对象子集；每个闭意图都可写成某个对象子集的公共属性交，因此这个算法构成独立 oracle。两边闭意图集合不相等时，整个分析失败。

穷举 oracle 限制为最多 20 个对象，超过阈值会拒绝，而不是静默指数爆炸。

### 6.4 RCA-style 关系尺度

每轮：

1. 计算当前状态上下文中的 object-concept class；
2. 对每条图边生成 `exists_outgoing` 和 `exists_incoming` 关系属性；
3. 每个关系属性记录产生它的 `edge_id`；
4. 以“本轮关系属性与上一轮完全一致”为不动点条件；
5. 达到最大轮数仍未稳定则结果为 `PARTIAL`。

POC 五组轨迹均在第二轮达到稳定。

### 6.5 trace 规则

| trace family | 机械判据摘要 |
|---|---|
| `LINEAR_PROGRESS` | 至少两条无歧义的连续推进边 |
| `BRANCH_EXPLORATION` | 一个 occurrence 有多个显式 `BRANCH_FROM` 子支 |
| `FAILED_BRANCH` | failure kind、失败状态或矛盾/放弃边 |
| `REVISIT_WITH_NEW_INFORMATION` | 同一 canonical state 的新 occurrence，属性严格增加且有 `REVISIT` |
| `RECOVERY_AFTER_CONTRADICTION` | 从失败/矛盾 occurrence 进入新的折返 occurrence |
| `CROSS_BRANCH_REUSE` | 不同分支 token 间发生 `REUSE`/`DEPENDS_ON` |
| `TRUE_MERGE` | 多个分支或多个显式 `MERGE` 父输入进入同一 occurrence |

每条 trace 必须保存准确 event IDs、edge IDs、共享闭意图和冻结规则 ID。事件 ID 按发生顺序保留，不按字符串字典序重排。出现方向词但没有结构证据，不会生成 trace。

---

## 7. 批处理与增量语义

`analyze_incrementally()` 当前是正确性参考实现：每加入一个事件，就对整个前缀重新运行严格解析和完整分析。它不声称具备增量 FCA 的性能优势。

它的作用是先冻结语义：最终前缀的科学指纹必须与一次性批处理完全相同。未来优化为真正的增量算法时，必须继续满足这个等价合同。

科学指纹只包含科学对象和算法版本，不包含运行时间、绝对路径等非科学字段。

---

## 8. 输出对象

一次 CLI 分析成功后原子封存以下文件：

| 文件 | 内容 |
|---|---|
| `reasoning-dag.json` | 节点、类型边、拓扑顺序、分叉/折返/合流索引 |
| `state-context.json` | 状态 FCA 形式上下文 |
| `transition-context.json` | 转移 FCA 形式上下文 |
| `state-concepts.json` | 状态概念及小上下文 oracle 对账 |
| `transition-concepts.json` | 转移概念及 oracle 对账 |
| `relational-scaling.json` | 关系尺度轮次、不动点和边级 provenance |
| `traces.json` | 规则化 trace 列表 |
| `audit-report.json` | 完整性、FCA、关系尺度和 live 状态 verdict |
| `incremental-replay.json` | 每个前缀科学指纹 |
| `output.md` | 人读摘要 |
| `run-manifest.json` | 输入、精确实现树、资产、输出哈希和副作用计数 |

CLI 拒绝覆盖已有目录；先写权限为 `0700` 的新 partial 目录，完成写入与 fsync 后再原子改名。`integrity.py` 将包内全部 `.py/.ref/.ai-check` 逐文件哈希，并把规范排序后的聚合收据放入 run manifest。当前输出 manifest 固定记录零模型调用、零数据库连接、零 Solver 启动。

---

## 9. 运行时认知资产与双运行档

`system/assets/solve_vein_analysis/` 中有三个未来角色资产：

1. `AGENTS_event_extractor.md`：原始 trajectory → 事件候选；
2. `AGENTS_state_normalizer.md`：occurrence 与 canonical state 对齐；
3. `AGENTS_trace_auditor.md`：盲审结构与 trace 证据。

`asset-manifest.json`是当前活跃资产集的内容寻址清单。历史资产在`releases/`中按版本保留：`0.1.x`是最初文件写入档，`0.2.0`是暂停的response-only备选，当前候选`0.3.0`是用户批准的no-sandbox + dangerous/YOLO + workspace AGENTS权限档。这些版本的运行证据只追加在独立POC结果和调用收据中，不会回写历史结论。`0.3.0` manifest保留运行前的`live_execution_status=NOT_TESTED`历史声明；后来的VMS-38结果由362号和D盘append-only bundle单独支持`INTERACTIVE_TMUX_DEBUG`执行合同，不资格化角色，也不回写冻结manifest。

Devin 运行分成两个严格不同的档位：

| 档位 | 用途 | 观察与干预 | 证据用途 |
|---|---|---|---|
| `SEALED_NONINTERACTIVE` | 冻结实验、可复现实跑 | 不允许人工输入；进程自然退出后统一收集 stdout/stderr/export | 可进入后续资格审查，但仍须完整协议门 |
| `INTERACTIVE_TMUX_DEBUG` | POC、调试、观察 thinking spin 和 TUI 状态 | 私有 tmux socket/session；可追加 pane/health snapshot；任何按键必须记录 | 默认且永久是 `DEVELOPMENT_ONLY`，不得冒充确认性样本 |

两个档位共享角色语义合同，但不共享运行收据。交互档有四条硬边界：

1. Devin 命令通过 tmux 的多参数接口直接传递，题面和 prompt 不插入 shell 字符串；
2. 每次 attempt 使用独立 socket、session、workspace、config 和 export；
3. 看到 `DONE.md` 只表示候选输出出现，不能立即 kill；必须等待/促成 Devin 正常退出后再封存 export；
4. `/exit`、`C-c` 等所有输入均生成 intervention record，并使证据保持开发用途。

未来无论载体是 Devin GLM-5.2 High 还是 Codex，都必须经独立 ModelRolePort 能力门、独立视图和调用收据，不能因为 prompt 已存在或某次文件写入成功就宣告角色可运行。

---

## 10. 测试与已知边界

自动测试位于 `system/tests/solve_vein_analysis/`。确定性 POC fixture 覆盖：

- C1 线性推进；
- C2 分叉与失败；
- C3 折返并增加知识；
- C4 跨分支复用和真合流；
- C5 复合轨迹。

POC-VMS-31 支持的结论仅限：在这五组冻结结构化轨迹上，DAG 重构、规则 trace、FCA 闭包和批/增量等价均通过；列表/树投影对指定复杂关系有可测信息损失。

后续 Devin 运行实验的当前证据边界：

| POC | 结果 | 可以支持 | 不可以支持 |
|---|---|---|---|
| VMS-32 | `INCONCLUSIVE_PROTOCOL` | sandbox/权限/载体限流是实在前置问题 | 角色无效或 Devin 不可用 |
| VMS-33 | `INCONCLUSIVE_PROTOCOL` | 仅改启动器仍不能恢复自主文件写入 | sandbox 是唯一原因 |
| VMS-34 | `PAUSED_BEFORE_LIVE_CALLS` | 机械响应协议可作为备选设计 | 任一 live 能力 |
| VMS-35 | 总体 `INCONCLUSIVE_PROTOCOL` | 三个 GLM-5.2 High 调用均写出 JSON 且 export 可解析；源文件写入合同得到本轮支持 | 三角色科学资格、强隔离、流式接入 |
| VMS-36 | `INCONCLUSIVE_PROTOCOL / ABORTED` | tmux实时pane/Thinking/tool失败可见，private session与exact model/export可审计 | 当前tmux workspace可完成任务、角色资格 |
| VMS-37 | `INCONCLUSIVE_PROTOCOL / ABORTED` | D盘站点、tmux、dangerous和exact model/export可用；`Read(/Volumes/**)`为自己的协议矛盾 | D盘不可用、dangerous无效、角色资格 |
| VMS-38 | `SUPPORTED_WITHIN_DEBUG_CANARY / DEVELOPMENT_ONLY`；事后科学投影`PARTIAL` | dangerous+AGENTS档在D盘workspace完成严格输出、DONE、exact model、原始tool boundary、唯一退出和exit 0；10/10 occurrence与真合流通过 | 角色资格、AGENTS等同OS sandbox、生产数学质量；旧gold下typed-edge recall仅9/13；历史receipt的0/15 ATIF摘要不可用 |
| VMS-39 | `SUPPORTED_WITHIN_FROZEN_PROFILE / DEVELOPMENT_ONLY` | effective控制面16,384 bytes精确边界 | 其他版本/模式边界、Tell/Trace容量 |
| VMS-40 | `PASS_WITHIN_DETERMINISTIC_OFFLINE_SCOPE / DEVELOPMENT_ONLY` | 多视图、多轴State、AcceptableSet、机械Evaluator | 任何模型角色资格或live extraction |

VMS-35 还形成三个必须在新版本合同中处理的反例：

- 状态 normalizer 的 `ABANDONED` 与 gold 的 `CONTRADICTED` 在原句上存在可辩护的多视图语义，不能把单一标签当绝对真值；
- canonical state 不能只靠一个扁平 ID 承担“问题状态、策略状态、表示状态”三种等价关系；
- auditor 的逐项判定与总 verdict 之间必须由预注册机械聚合规则连接，不能在评分后补规则。

fixture 中的 `source_span.sha256` 只经过 64hex 合同验证；由于本轮没有把 raw Solver artifact 放进 POC，模块没有核对 span 字节与该哈希是否一致。这属于 raw extraction 阶段的未测试能力。

VMS-38封存后发现，旧`inspect_export()`把ATIF-v1.7的13个step误报为0，并把7次tool call双计为15。final bundle和receipt保持不可变；运行后代码已改为直接识别顶层`steps`并只计实际`tool_calls/tool_events`，新回归用ATIF-v1.7样本锁定2 step/2 call。未来run必须使用修复后的解析器，新代码不得被用于重写VMS-38历史receipt。

VMS-40已经完成第1项：366号在实现前冻结，367号记录6 case/26 candidate零mismatch、artifact integrity PASS与append-only重启拒绝。它只关闭确定性真值合同，不资格化模型角色。

下一阶段必须分开验证：

当前任务状态以`docs/history/sixth-generation/rnd/391-v0-2026-08-16-解题侧脉络分析新工作方案-取代363号路线图.md`§8为准；测试和POC物证由`system/tests/solve_vein_analysis/README.md`统一索引。363号及route-lock是SUPERSEDED冻结历史，不得继续推进其资格链。370号只冻结了文件分片与逐项遍历设计；registry、cursor、coverage和completion runtime尚未实现，不能作为当前能力。

1. 用新题/新raw trajectory验证原始 Solver thinking → `ReasoningTrajectory` 的准确率与盲审一致性；
2. normalizer/auditor各自的新资格化协议，以及live carrier能力与权限隔离；
3. streaming partial/reattach/reconcile；
4. 大轨迹上的增量性能和内存上限；
5. 对 Tell 选择与引导树生成的真实增益；
6. Trace事实账本与Tell/Hint策略账本的版本化证据关系；
7. 推理树、引导树及三个推动关系的机械闭环；
8. Seven未完成时的冻结接口模拟器、数据库Schema/计划和全链路golden slice。

---

## 11. 对外接口

```python
from system.solve_vein_analysis import (
    ReasoningTrajectory,
    analyze_trajectory,
    analyze_incrementally,
)
```

- `ReasoningTrajectory.from_dict()` / `.from_json_text()`：严格解析；
- `analyze_trajectory(trajectory)`：一次性分析；
- `analyze_incrementally(trajectory)`：返回最终 bundle 与前缀 journal；
- CLI 与 POC 命令见 `system/docs/solve_vein_analysis_runbook.md`。

当前模块不写数据库。将来接入 `process_solve.py` 时必须通过版本化 artifact/port，而不能反向导入入题侧实现或复用其可变运行目录。
