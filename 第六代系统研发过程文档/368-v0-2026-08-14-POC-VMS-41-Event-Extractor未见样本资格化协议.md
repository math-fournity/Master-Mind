# POC-VMS-41：Event Extractor 未见样本资格化协议

**日期**：2026-08-14  
**阶段**：`SV-S2`  
**当前状态**：`OFFLINE_IMPLEMENTATION_COMPLETE / PREEXECUTION_FREEZE_NOT_CREATED / NO_LIVE_AUTHORITY`  
**证据用途**：`COMPONENT_QUALIFICATION / DEVELOPMENT_ONLY`  
**候选载体**：Devin CLI `glm-5-2` / `GLM-5.2 High`  
**任务追踪真值源**：363号文档  

---

## 0. 协议身份与冻结边界

本文先于 VMS-41 的任何候选角色调用落盘。四case、隐藏acceptable set、严格grader、角色资产、运行器和离线负向回归现已实现；完整离线测试为112项PASS。当前仍未生成preexecution freeze manifest，**不授权启动 Devin**。

只有下列对象全部封存并由独立freeze manifest绑定后，状态才可改为`PREREGISTERED_NOT_STARTED`：

1. 四个 case 的候选可见文件与人工可见说明；
2. 候选不可见的 acceptable set；
3. 严格 parser、anchor mapper、grader 和负向回归；
4. 角色资产、task template、profile、资源与调用数；
5. preexecution freeze manifest、内容哈希、用户级Devin控制面和唯一 attempt ID；
6. README 预先登记和入题侧保护基线。

若在任意 live 调用后发现协议、gold、grader 或 fixture 必须修改，本 POC 只能封存为`INCONCLUSIVE_PROTOCOL`，另建新版本和新 attempt；不允许修改旧输入后重跑到通过。

---

## 1. 本轮只回答什么

核心问题是：

> 在不见参考答案、Tell/Hint、gold boundary 或预期边的条件下，冻结的 Devin Event Extractor profile 能否把一条非线性 Solver reasoning 分成发生顺序上的 occurrence，并可审计地识别分支、失败、折返、复用和真/假合流？

本轮只资格化以下组件主张：

- raw reasoning 字节边界与 occurrence 的忠实绑定；
- 必需 occurrence anchor 的找回；
- v1 relation 的必需、可选和禁止边；
- 真 MERGE 的多父要求与假 MERGE 拒绝；
- 失败、弃用、矛盾和不确定性保留；
- 候选输出能否被严格 Schema 与机械 grader 重放。

本轮**不**资格化：

- State Normalizer 的多轴 state binding；
- Trace Auditor；
- Codex 或其他 carrier profile；
- stream visibility、partial/retraction、reattach 或并发恢复；
- Tell选择、Hint有效性、双树、Grove、Seven、DB/Redis或Solver启动；
- `AGENTS.md`等于OS sandbox或强答案隔离。

---

## 2. 与 VMS-38/VMS-40 的证据边界

- VMS-38只证明no-sandbox + dangerous + workspace `AGENTS.md`档能完成一次文件生成调试调用；它不是角色资格。
- VMS-40只证明五层真值、多视图、多轴State、不可拆分alternative与确定性evaluator成立；它不证明模型能从raw reasoning提取正确结构。
- VMS-41使用新case和新attempt，不得把VMS-38已见输出当qualification confirmation。
- VMS-41只对`Devin CLI + glm-5-2 + High + 本轮精确角色资产/profile`给出Verdict；不外推到其他模型、Devin版本、Codex或生产ModelRolePort。

---

## 3. 案例组成与证据分区

### 3.1 四个 qualification case

| Case | 来源 | 目标结构 | 主要反例 |
|---|---|---|---|
| `V41-SYN-FALSE-MERGE` | 新人工构造，未给候选角色看过 | 弃用错误路线；独立新路线完成；不合流 | 因后文提到前路线就标MERGE |
| `V41-SYN-TRUE-MERGE` | 新人工构造，未给候选角色看过 | 奇偶引理与闭迹拼接分支被显式组合 | 单父MERGE、只记最终结论 |
| `V41-REAL-SPIRAL` | 只读历史Devin reasoning摘录 | 正向证明循环→不可微曲线→失败螺旋→减速螺旋反例 | 丢失折返；把所有螺旋尝试压成一事件 |
| `V41-REAL-BATTERY` | 只读历史Devin reasoning摘录 | 失败子问题→换成图覆盖→Turán→自适应对手→回看并合成证明 | 把长循环当线性润色；丢失自我否定 |

### 3.2 真实只读来源

`V41-REAL-SPIRAL`：

```text
problem/source id: p28a94bb9038347f8b5fc
conversation.json SHA256: 8a54cfe16b9e756dc3a3e464d5416febaa68fd983c8469552631f8c83e9cff0e
exact agent reasoning UTF-8 SHA256: ebd095960ef7736a8843738c9f7816a667551c41133190111b84d2d98a085930
selector: blank-line paragraph indices 133..243 inclusive, 1-based
```

`V41-REAL-BATTERY`：

```text
problem/source id: pf3a7fa50dcf54bafbe7a
conversation.json SHA256: 495aaab620d2ae7bd1ea9e5af9d7fd7c880c1273d111387d480f1f21bc6c0c8f
exact agent reasoning UTF-8 SHA256: 6296cfe86c1e5ab8520cfec76ddebdfc6f60879273f2325f533f5f3ea3900d0b
selector: blank-line paragraph indices 145..260 inclusive, 1-based
```

提取程序必须：

1. 严格验证conversation和reasoning哈希；
2. 要求恰有一个`source=agent`且含`reasoning_content`的step；
3. 以`\n`+空白行做确定性段落分割，拒绝空段；
4. 只取冻结的1-based闭区间，用两个`\n\n`重组，结尾加一个`\n`；
5. 产生source receipt，保留原路径、哈希、选择器版本、段落数、摘录字节数和摘录哈希；
6. 不修改、移动、加锁、改权限或写入原trajectory/workspace。

### 3.3 证据用途

四case在fixture/gold冻结后是一次性`qualification` pack。它们不可再用于修改同一候选角色资产后的confirmation。若本轮失败，可以把输出转为development/regression证据，但下一版必须用新source lineage的未见pack。

---

## 4. 候选角色可见/不可见面

每case的Event Extractor任务数据面只包含：

- 短`AGENTS.md`角色合同；
- `TASK.md`中的case/problem/trajectory/source identity和exact output要求；
- `problem.md`；
- `raw_solver_trajectory.txt`；
- 严格v1 trajectory Schema与enum glossary；
- 当前workspace中的输入manifest与专用Devin config。

Devin CLI在本机真实profile中还会加载用户级`~/.config/devin/AGENTS.md`。这不是题目数据，也不能假装不存在：freeze manifest必须记录其固定的sanitized路径、字节数和SHA-256，`LaunchReceipt`与`InvocationReceipt`必须在每次调用前重验并记录同一观察。用户级或workspace级控制文件任一漂移都在启动前BLOCK。VMS-41不依赖这些控制文字提供gold、Tell或答案。

候选角色按冻结权限合同不得读取：

- acceptable set、anchor witness、gold event count、阈值、grader输出；
- 参考解、题库验证结论、后来成功trajectory；
- Tell/Hint、selector、双树或Seven状态；
- 其他case、其他attempt输出和历史VMS-38 candidate；
- repo、题海workspace/trajectory根、入题侧资产和数据库。

只把允许的任务文件复制到每attempt的独立D盘workspace。原始trajectory摘录是Solver thinking证据，不是参考解；但仍不得让候选角色通过绝对路径扩大可见面。`dangerous`没有形成OS级强隔离，因此这里的边界是“最小物化视图 + 冻结规则 + 完整tool-event审计 + 越界即隔离”，不是“物理上绝无读取能力”。tool events缺失时必须标`UNOBSERVABLE/INCONCLUSIVE_PROTOCOL`，不得推定清洁。

---

## 5. EventExtractionAcceptableSet/v1

候选仍输出`solve-vein/reasoning-trajectory/v1`。gold不强迫候选使用题目特化的event ID，而是通过候选的字节span对齐不可见anchor：

```yaml
schema_version: solve-vein/event-extraction-acceptable-set/v1
acceptable_set_id:
case_id:
problem_id:
trajectory_id:
source:
  carrier:
  source_artifact_ref:
  source_artifact_sha256:
expected_event_count:
anchors:
  - anchor_id:
    unique_witness_text:
    allowed_event_kinds: []
    allowed_statuses: []
edge_clauses:
  - clause_id:
    source_anchor_id:
    target_anchor_id:
    allowed_relations: []
    required: true | false
forbidden_relations: []
forbidden_edges: []
merge_constraints:
  - target_anchor_id:
    minimum_distinct_parent_anchors:
    required_parent_anchor_ids: []
```

每个`unique_witness_text`必须在raw source中恰出现一次，只用于grader确定一个语义anchor的UTF-8字节位置，不复制到候选workspace之外的新文件，也不在TASK中提示。

一个candidate event只有在其`source_span[start:end]`包含恰一个anchor witness字节位置时才映射该anchor。同一event包含多个anchor、一个anchor被多event覆盖、有anchor未覆盖，或event不覆盖任何anchor，都是资格化FAIL。这使“分段完整”可机械检查，不依赖AI自报。

可辩护的relation投影不压成单标签：`allowed_relations`允许冻结小范围替代；候选只需命中其一。任意未列为required/optional的anchor间边都是unmatched，不得因最终结果正确而忽略。

---

## 6. 确定性 grader

grader按以下顺序fail-closed：

1. 校验case/input/asset/profile/attempt和所有哈希；
2. 严格解析v1 trajectory，拒绝未知字段、未知enum、重复ID、非连续sequence、后向边和缺父事件；
3. source carrier/ref/hash必须与冻结TASK一致；
4. 每个span必须是有界、非空、按顺序、不重叠的UTF-8字节区间，且span SHA-256等于raw字节重算值；
5. 将每event按“恰包含一个witness”映射到anchor，要求anchor与event完全一一对账；
6. 检查event kind/status acceptable set；
7. 将candidate edge经event→anchor映射后检查required/optional/forbidden/unmatched；
8. MERGE必须同时满足至少两个不同parent anchor和该case的required parent set；
9. 检查候选event text/边evidence与span的语义忠实性，本项保留为盲化人工审计，不得用最终答案正确代替；
10. 严格按第 7 节聚合，候选自写PASS、`DONE.md`或退出0都不代替grader。

grader输出`EventExtractionEvaluation/v1`，包含protocol、artifact与mechanical-scientific三轴Verdict、anchor/event映射、每clause结果、MERGE约束、语义审计状态、错误列表和证据引用。调用身份、模型、工具、资源和文件集由外层`InvocationReceipt`、`ToolBoundaryAudit`与`CaseResult`独立判定，不能塞进数学grader后用一个总分掩盖。

---

## 7. PASS / PARTIAL / FAIL / INCONCLUSIVE

### 7.1 单case机械PASS

必须全部成立：

- candidate v1严格有效；
- source identity、span boundary和span hash 100% PASS；
- event count与anchor一一映射PASS；
- 每anchor的kind/status在acceptable set内；
- required edge recall = 1.0；
- forbidden edge count = 0；
- unmatched edge count = 0；
- 真MERGE多父完整；假MERGE count = 0；
- 语义忠实性人工盲审=`PASS`；
- 无禁止信息/工作区/工具边界越界。

### 7.2 组件资格PASS

四个case必须全部单case PASS，且：

- `glm-5-2`在每个generation-bearing agent step上都可观察且一致；
- 四attempt均为fresh session，无resume/continue/fallback/科学重试；
- 任何失败、弃权或超时都保留，没有选择性删除；
- 工作区、export、receipt、candidate、grader和人工审计组成完整hash链；
- 入题侧保护基线前后一致；
- 独立复核器从原始bundle重算后也给出PASS。

### 7.3 其他Verdict

- `PARTIAL`：协议有效，部分case过门，但组件不足以资格化；
- `FAIL`：协议有效且候选稳定违反预注册核心语义；
- `INCONCLUSIVE_PROTOCOL`：哈希、资源、调用身份、可观测性、输出或审计链缺失；
- `QUARANTINED`：越界、unknown-start、模型漂移、证据冲突或不可安全重放。

单个好看的case不能把组件标为PASS，也不能用整体成功倒推未通过的anchor/edge/MERGE。

---

## 8. 角色/profile与调用数

| 字段 | 冻结值 |
|---|---|
| port/lane | 解题侧独立cognitive role lane；绝不进Target Solver harness |
| carrier | Devin CLI，精确binary/version/hash在freeze manifest回填 |
| requested model | `glm-5-2` |
| normalized effort | `high` |
| effort encoding | `model_uid` |
| orchestration | fresh single-agent one-shot；禁subagent |
| sandbox | `false` |
| permission | `dangerous` / Bypass，权限意图由短AGENTS/TASK限定并审计tool events |
| output | `reasoning-trajectory.json` + exact `DONE.md` + raw export/stdout/stderr/receipt |
| case attempts | 4 case × 1 scientific attempt |
| scientific retry | 0 |
| infra retry | 0；若没有可信物证证明provider未接受且generation未开始，一律不重试 |
| timeout | 每case 900 seconds，精确资源在manifest回填 |
| concurrency | 1；串行消费qualification pack |
| DB / Redis / Solver / network | 0 / 0 / 0 / 0 |
| user-level control surface | `~/.config/devin/AGENTS.md`路径/字节/SHA在freeze与每attempt receipt中精确重验 |

本 POC 使用`SEALED_NONINTERACTIVE`作为确认性载体。interactive tmux只可用于不消费这四个case的development canary；不得在tmux中先看qualification case再用noninteractive重跑。

---

## 9. 可观测、失败与恢复

### 9.1 可观测物证

每attempt必须有：

- pre-generation `LaunchReceipt`，包含attempt/case/profile/input/output/fence与argv hash；
- `REQUEST_ACCEPTED`和`GENERATION_STARTED`是否可观的独立状态；
- stdout/stderr/export/ATIF、session ID、generation model UID、step/tool event、token/wallclock；
- workspace before/after manifest；
- 候选输出、DONE marker、strict parser和grader；
- 中断、timeout、cancel、seal与quarantine事件。

### 9.2 恢复规则

- 有正面物证证明provider未接受且generation未开始：本协议仍不重试，直接记`INCONCLUSIVE_PROTOCOL`；
- 已接受/已开始：只能reattach/reconcile同attempt；
- accepted/started未知：`QUARANTINED`，禁盲调；
- 输出已seal：任何同ID调用必须被拒绝；
- 科学负结果、ABSTAIN、ERROR或timeout都是终态，禁`retry until pass`。

---

## 10. 物理存储与不可变边界

小型协议、fixture、gold、grader、测试与人读结果留在repo；调用workspace和原始大物证使用：

```text
/data/master-mind-solve-vein-data/poc-results/poc-vms-41-event-extractor-qualification-20260814/
```

外层运行采用固定`.poc-vms-41-....partial`目录，单attempt采用`.attempt.partial-<attempt_id>`；两层都在同卷append-once写入后原子seal。目标已存在、受信根以下任一祖先symlink、D卷身份/空间不符，均在启动前BLOCK。异常留下partial/quarantine物证，不清理后盲重试。

禁止修改：

- `system/vein_analysis.py`；
- `system/process_absorb.py`；
- `system/assets/vein_analysis/`；
- `palyground/absorb/vein_analysis/`；
- 入题侧各管线workspace、AGENTS和运行物证；
- VMS-31—40 已封存bundle；
- 题海三个原source目录中的任何文件。

---

## 11. 实现和验证顺序

```text
368协议草案
  → 构建四case可见文件和隐藏acceptable set
  → 实现strict parser/anchor mapper/grader
  → 负向向量与fake-Devin组件测试
  → 全量回归 + 入题侧保护基线
  → 协议正文定稿
  → 单独生成freeze manifest绑定protocol与全部exact hash/attempt/resource
  → 独立只读preflight复验freeze
  → README与363/route-lock追加freeze路径和hash，但不回写本协议
  → 外部状态登记为PREREGISTERED_NOT_STARTED并精确开放一次start
  → 启动4个串行one-shot attempt
  → 严格grader并封存live bundle（最高PENDING_MANUAL_AUDIT）
  → 在独立append-only audit bundle中完成盲化语义复核
  → 聚合 + 独立只读复算；不修改已封存live bundle
  → 结果文档/README/363/模块文档/ChangeLog
```

任何一个冻结门不通过，都不得跳到live。

---

## 12. 停止条件

满足任一即停止新调用：

1. 四个预注册attempt均达到终态；
2. 任一越界、模型/profile漂移、source/gold暴露或未知启动；
3. 任一入题侧基线漂移；
4. 物证根冲突、D卷失效、资源超限或无法可靠seal；
5. 发现必须改acceptable set/grader/资产才能继续。

在停止后不得用新prompt、新session或其他carrier补齐失败case。

---

## 13. 计划产物

```text
system/assets/solve_vein_analysis/releases/0.4.0/
system/solve_vein_analysis/event_extraction_qualification.py
system/solve_vein_analysis/event_extraction_qualification.ref
system/solve_vein_analysis/event_extraction_qualification.ai-check
system/tests/solve_vein_analysis/qualification_fixtures/vms41/
system/tests/solve_vein_analysis/test_event_extraction_qualification.py
system/tests/solve_vein_analysis/test_event_extraction_qualification_runtime.py
system/tests/solve_vein_analysis/run_event_extractor_qualification.py
system/tests/solve_vein_analysis/freeze_event_extractor_qualification.py
system/tests/solve_vein_analysis/verify_event_extractor_qualification.py
```

每个新`.py`必须同时有同名`.ref`和`.ai-check`。测试与POC必须由`system/tests/solve_vein_analysis/README.md`索引。

---

## 14. Exact freeze的非循环签发规则

本文不内联自己的SHA-256，也不内联尚未存在的freeze manifest哈希；否则会形成“文档内容包含自身哈希”的循环。签发顺序固定为：

1. 先完成本文、代码、资产、fixture、测试和保护基线；
2. 运行全量离线测试并生成机器TestGate receipt；
3. 由freeze脚本读取**已经不再修改**的本文，记录protocol SHA-256；
4. freeze manifest逐项绑定fixture、acceptable set、资产、grader、runner、测试、保护基线、Devin binary/version/catalog、用户级`AGENTS.md`、attempt IDs、资源合同和唯一D盘输出根；
5. README与363只追加freeze manifest的路径和哈希，不回写本文；
6. 独立preflight重新核验manifest后，才可把外部状态改为`PREREGISTERED_NOT_STARTED`。

当前manifest尚不存在，因此当前状态仍为`NO_LIVE_AUTHORITY`。本文的定稿不是permit；只有外部manifest校验PASS和route-lock明确开放一次性start，二者同时成立才授权四次串行调用。

---

## 15. 当前离线实现checkpoint

- 四case visible fixtures与隐藏acceptable-set pack：已实现；
- strict parser / witness anchor mapper / relation与MERGE grader：已实现；
- no-tool fake-Devin四case端到端运行、延迟gold、tool audit、seal与重复启动拒绝：已实现；
- 用户级Devin `AGENTS.md`可见控制面的逐attempt冻结：已实现；
- 解题侧完整离线回归：112项PASS；
- 入题侧保护清单：161文件逐哈希PASS，清单文件SHA-256=`9bb4fd2551d13f196610ddf8e203ad96b0855f3337f6c4e6502f6c764eafd6b3`；
- preexecution freeze manifest：尚未生成；
- Devin/model调用：0；
- DB/Redis/Solver/Seven调用：0。

第一次freeze命令在任何artifact写入和任何模型调用前，被Python 3.14的`unittest.discover(..., top_level_dir=...)`导入条件拒绝；该测试目录有意不是Python package，因此错误使用`top_level_dir`会报`Start directory is not importable`。三份freeze目标和D盘live/partial根均仍不存在，未消费任何attempt。实现已改为与README标准命令一致的目录发现方式，并将发现阶段的`ImportError/OSError`转换为fail-closed `FreezeError`；修订后必须重新通过112项测试，才能从零生成首次有效freeze。
