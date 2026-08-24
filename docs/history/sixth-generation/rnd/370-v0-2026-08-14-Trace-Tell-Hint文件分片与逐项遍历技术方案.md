# Trace/Tell/Hint文件分片与逐项遍历技术方案

**日期**：2026-08-14  
**状态**：`DESIGN_FROZEN / IMPLEMENTATION_PENDING`  
**路线阶段**：`SV-K1 / SV-K2`  
**计划POC**：`POC-VMS-47`（尚未预注册、尚未执行）  
**任务追踪真值源**：363号  

---

## 1. 决策

Tell、Trace和Hint的权威积累不再依赖`AGENTS.md`。

每个分片使用一个不可变的权威条目文件，负责该分片的AI按稳定顺序逐项分析；AI把每项的结果写入独立汇报流。程序从源文件重新枚举项目，以集合、顺序、hash和attempt lineage机械证明全部项目都被处理。

首版物理合同是：

```text
一个权威输入文件
  <shard_id>.items.jsonl

四个派生证据文件
  <shard_id>.analysis.jsonl
  <shard_id>.cursor.jsonl
  <shard_id>.coverage.json
  <shard_id>.completion.json
```

这仍然符合“一个文件装入该分片的所有项”：`items.jsonl`就是该分片唯一的项集真值源。其余四个文件不保存新的权威项，只保存分析、恢复、对账和完成证据。

`AGENTS.md`只保留短小控制面：角色、权限、禁止动作、输入/输出路径、Schema版本、逐项遍历规则和停止条件。它不得承载Tell/Trace全量正文，也不得作为完成性账本。

---

## 2. 为什么不能把所有内容混在一个可变文件里

如果AI一边读取一个文件、一边在同一文件中修改项、填写结果和写“已完成”，会产生五类不可审计状态：

1. 无法证明遍历期间输入集合没有变化；
2. 无法区分原始项与AI后来补出的项；
3. 进程中断后无法判断最后一项是已完成、半完成还是只移动了游标；
4. 两个worker可能覆盖同一项或漏掉某项；
5. AI可以自报“全部完成”，但程序不能重算这个结论。

所以必须采用输入/输出分离：源项集不可变，其他文件append-only或由确定性程序一次性生成。

---

## 3. Trace、Tell、Hint不是同一种积累

### 3.1 Trace账本：发生了什么

`TraceArtifact`和`TraceWindow`记录Solver实际thinking中发生的事件、状态、关系、source span和provenance。它们是事实/观察账本；后续Tell理论变化不得回写历史Trace。

### 3.2 Tell账本：如何识别和选择方向

`TellCoreVersion`、`ApplicabilityBoundaryVersion`和`TellEvidenceLink`记录可复用机制、适用边界与证据。Tell是版本化假设/策略，不是从单条Trace自动升格的事实。

一条Trace与一个Tell的匹配结果只能先成为`TraceTellMatchObservation`：

```text
MATCH | NO_MATCH | ABSTAIN | ERROR
```

只有预注册contrast或经Revision Gate确认的证据，才能更新Tell的成熟度、scope或active release。

### 3.3 Hint账本：给特定处境实际发送了什么

`HintRendererVersion`把Tell方向题目化；`HintInstance`绑定具体问题、状态、lineage、renderer、payload hash和注入位置。Hint是运行实例，不能反向冒充TellCore。

因此分片的`item_kind`至少支持：

- `trace`：分析一条Trace或TraceWindow；
- `tell`：复核一个Tell版本/边界；
- `trace_tell_pair`：判断给定Trace与Tell是否匹配；
- 后续版本可增加`hint_instance`，但不能静默改变首版Schema。

---

## 4. 总体流水线

```text
append-only registry
  ↓ freeze RegistrySnapshot
deterministic shard planner
  ↓ write immutable <shard>.items.jsonl
shard worker
  ↓ ordered per-item analysis + cursor transitions
ShardCoverageVerifier
  ↓ exact set/hash/ordinal/lineage reconciliation
ShardCompletionReceipt
  ↓ reducer
selector candidates / offline metrics / RevisionProposal draft
```

分片worker只做语义判断，不具备以下权力：

- 修改输入项；
- 删除`NO_MATCH`、`ABSTAIN`或`ERROR`；
- 自签coverage或completion；
- 更新active Tell release；
- 把episode观察写成因果`supports`；
- 重试直到得到想要的判断。

---

## 5. 权威输入：`<shard_id>.items.jsonl`

### 5.1 文件格式

UTF-8、LF、禁止BOM。第一行是header，之后每行一个item。文件封存后只读；任何字节变化都产生新`shard_id`和新hash。

Header最小字段：

```json
{
  "record_type": "SHARD_HEADER",
  "schema_version": "solve-vein/shard-items/v1",
  "shard_id": "...",
  "registry_snapshot_id": "...",
  "registry_snapshot_sha256": "...",
  "item_kind": "trace_tell_pair",
  "split_rule_id": "...",
  "split_rule_sha256": "...",
  "analysis_contract_id": "...",
  "analysis_contract_sha256": "...",
  "ordered_item_ids": ["..."],
  "item_count": 1,
  "items_payload_sha256": "...",
  "created_at": "...Z"
}
```

Item最小字段：

```json
{
  "record_type": "SHARD_ITEM",
  "schema_version": "solve-vein/shard-item/v1",
  "shard_id": "...",
  "item_id": "...",
  "ordinal": 0,
  "item_kind": "trace_tell_pair",
  "payload_ref": "...",
  "payload_sha256": "...",
  "trace_version_ref": "...",
  "tell_release_ref": "...",
  "evidence_refs": [],
  "item_sha256": "..."
}
```

Header中的ID列表、行内`item_id`与实际行序必须完全一致。重复ID、跳号、未知字段、非有限数字、软链输入、hash不一致一律BLOCK。

### 5.2 分片规则

可以按以下维度形成分片，但每次只能由版本化`split_rule`决定：

- Tell family；
- 数学分支/子分支；
- trigger特征；
- negative guard / false-friend族；
- transfer band；
- priority或成本带。

不能在看到AI输出后重新切分同一确认性批次并仍称原分片结果。派生重分片必须生成新manifest，并保留`derived_from`关系。

---

## 6. 逐项汇报：`<shard_id>.analysis.jsonl`

每个item恰有一个终态科学attempt。允许一个attempt产生多个过程事件，但最终只封存一条`PerItemAnalysisRecord`：

```json
{
  "record_type": "PER_ITEM_ANALYSIS",
  "schema_version": "solve-vein/per-item-analysis/v1",
  "shard_id": "...",
  "item_id": "...",
  "ordinal": 0,
  "attempt_lineage_id": "...",
  "worker_profile_id": "...",
  "worker_profile_sha256": "...",
  "input_item_sha256": "...",
  "decision": "MATCH",
  "matched_tell_ids": ["..."],
  "evidence_refs": ["..."],
  "reason_summary": "...",
  "alternative_interpretations": [],
  "started_at": "...Z",
  "sealed_at": "...Z",
  "record_sha256": "..."
}
```

终态枚举固定为：

```text
MATCH | NO_MATCH | ABSTAIN | ERROR
```

`ERROR`也是必须保留的终态记录；它意味着该项尚无可用语义判断，但仍证明系统没有静默跳过。是否对该项发起新attempt必须由预注册retry规则裁决，并使用新attempt ID、保留原lineage；旧记录不可覆盖。

---

## 7. 恢复journal：`<shard_id>.cursor.jsonl`

Cursor不是“当前行号”单值文件，而是append-only状态跃迁：

```text
CLAIMED → STARTED → SEALED
                 ↘ ERROR
                 ↘ UNKNOWN_START_QUARANTINED
```

每条跃迁绑定`shard_id/item_id/ordinal/attempt_id/fence_token/previous_event_hash/event_hash/time/evidence_ref`。旧fence不得提交或取消新attempt。

恢复时：

1. 从items重新枚举expected IDs；
2. 读取所有sealed analysis records；
3. 重放cursor事件；
4. 对`REQUEST_ACCEPTED/GENERATION_STARTED`未知的attempt先reattach/reconcile；
5. 无法证明provider未接受时不得盲重呼；
6. coverage仍由最终集合对账决定，不由最后一个cursor offset决定。

---

## 8. 覆盖证明：`<shard_id>.coverage.json`

`ShardCoverageVerifier`必须独立读取输入和分析文件，重算：

```text
expected_ids = ordered IDs from items.jsonl
reported_ids = sealed item IDs from analysis.jsonl

set(expected_ids) == set(reported_ids)
len(expected_ids) == len(reported_ids)
missing_ids == []
duplicate_ids == []
unknown_ids == []
ordinal_mismatches == []
item_hash_mismatches == []
lineage_conflicts == []
```

此外必须验证：

- 每个item只有一个当前有效终态attempt；
- `ABSTAIN`和`ERROR`没有被过滤；
- input snapshot与analysis contract未漂移；
- source/view/答案ACL符合角色合同；
- 结果文件没有软链或目录逃逸；
- 统计只从逐项记录重算，不能接受AI自报总数。

Coverage Verdict至少分：

```text
PASS | FAIL | INCONCLUSIVE_PROTOCOL
```

`PASS`只表示遍历与物证完整，不表示每项判断数学上正确，也不表示Tell selector有效。

---

## 9. 完成收据：`<shard_id>.completion.json`

只有coverage PASS后，机械sealer才可签发completion。收据至少绑定：

- items/analysis/cursor/coverage各自SHA-256；
- 输入与结果artifact tree；
- expected/reported/terminal outcome计数；
- worker profile、adapter与模型有效身份集合；
- attempt lineage root；
- coverage verifier版本/hash；
- protocol deviations；
- completion verdict与明确非主张；
- append-once commit marker。

AI写在自然语言报告中的“所有项目均已遍历”不能替代completion receipt。

---

## 10. Worker如何轮询

### 10.1 小分片

一个fresh session可按ordinal顺序处理完整小分片，但`max_items_per_session`必须预注册。每项都立即写独立结果和cursor事件；不能等全部分析完后只写一份总结。

### 10.2 大分片

超过上限时滚动fresh session。滚动只改变carrier/session，不改变分片ID、项顺序或科学lineage。新session从机械恢复器给出的下一未封存项开始，不依赖上一AI的自然语言记忆。

### 10.3 并行

首版优先“一分片一worker、分片内串行”。后续并发必须使用lease/fence/CAS；同一item重复dispatch只允许一个终态提交。不同分片可以并行，但共享carrier-global limiter，且不能饿死Solver或Judge池。

### 10.4 提示词与AGENTS

短控制面只告诉worker：

- 读取哪个items文件；
- 当前被授权处理哪些ordinal；
- 输出Schema和目标目录；
- 禁止修改输入、越界读取、调用子AI、改Git/DB；
- `MATCH/NO_MATCH/ABSTAIN/ERROR`语义；
- 每项完成后必须写记录，遇错也不得跳过；
- DONE只表示worker停止，不表示coverage PASS。

Tell/Trace正文通过显式文件输入或逐项渲染payload交给worker，不占用`AGENTS.md`的16,384-byte有效控制面预算。

---

## 11. 文件、D盘与数据库的分工

### 11.1 D盘/CAS

大Trace、分片、模型raw events、分析记录和completion bundle进入解题侧批准的D盘数据根，以内容hash寻址。repo只保存Schema、代码、小型fixture、manifest和人读文档。

### 11.2 ArangoDB

数据库未来只保存小型元数据、版本关系、状态、索引字段和artifact ref/hash，不存大段raw thinking或整份模型export。

预备集合/对象包括：

- registry snapshot；
- shard manifest；
- item identity与payload ref；
- attempt/cursor event；
- coverage/completion receipt ref；
- Trace↔Tell observation；
- Tell evidence/revision lineage。

本设计不授权当前连接或写库。Schema plan、只读catalog、受控migration、人工Gate和rollback须在后续独立阶段完成。

---

## 12. 与Selector、Tell学习和Seven的关系

逐项遍历的输出首先是观察账本。Reducer可以生成：

- selector离线precision/recall/calibration候选；
- false-friend/negative boundary统计；
- Tell split/merge/expand/narrow候选；
- 未覆盖CoverageCell；
- RevisionProposal草稿。

Reducer不得自动改TellCore或active pointer。确认性Tell证据必须来自预注册randomized contrast；同一个用于发现/拟合的分片不能再充当prospective confirmation。

Seven对接时，导出的是冻结`RegistrySnapshot + ShardCompletionReceipt + PerItemAnalysisRecord refs`，不是可变工作目录，也不是AGENTS文本。Seven只消费带版本和hash的bundle。

---

## 13. POC-VMS-47最小矩阵

VMS-47在预注册前至少准备：

1. 一个`trace`分片；
2. 一个`trace_tell_pair`分片，含MATCH、NO_MATCH、ABSTAIN和故障项；
3. 至少一次中断后fresh session恢复；
4. duplicate、missing、unknown、item tamper、ordinal drift、cursor EOF但coverage不全等负例；
5. 同一run ID重启与软链逃逸拒绝；
6. AI自报“完成”但漏项时机械FAIL；
7. 全项含ERROR仍能coverage PASS，但科学可用率单独下降；
8. 一个小分片由Devin `glm-5-2` High遍历；后续可用Codex独立profile作载体对照，二者不共享attempt；
9. 零DB/Redis/Solver的file-only首轮；
10. README登记、freeze、raw receipts、coverage和completion全部可只读重放。

首轮PASS最多支持：

```text
FILE_SHARD_ENUMERATION_AND_COVERAGE_CONTRACT = PASS
```

它不自动支持：

```text
TRACE_TELL_MATCHING_ACCURACY = PASS
SELECTOR_END_TO_END_VALUE = PASS
TELL_CAUSAL_EFFECT = PASS
PRODUCTION_SCALE = PASS
```

---

## 14. 实施顺序

1. 定义严格JSON Schema与canonical hashing；
2. 实现不可变items writer/reader；
3. 实现append-only analysis/cursor ledger；
4. 实现coverage verifier与completion sealer；
5. 用fake worker完成缺失/重复/篡改/恢复矩阵；
6. 在测试README登记并预注册VMS-47；
7. 冻结小型未见分片后才进行一次性模型canary；
8. 审计通过后再接registry reducer与数据库adapter；
9. 最后接入推理树/引导树和Seven冻结bundle。

---

## 15. 不变量

```text
AGENTS_IS_CONTROL_PLANE_ONLY
ITEMS_FILE_IS_THE_ONLY_AUTHORITATIVE_SHARD_POPULATION
INPUT_AND_OUTPUT_ARE_PHYSICALLY_SEPARATE
AI_CANNOT_SELF_SIGN_COVERAGE_OR_COMPLETION
ABSTAIN_AND_ERROR_ARE_NEVER_DROPPED
CURSOR_EOF_DOES_NOT_IMPLY_COMPLETION
EVERY_ITEM_HAS_STABLE_ID_ORDINAL_HASH_AND_LINEAGE
NO_RETRY_UNTIL_MATCH_OR_PASS
TRACE_FACTS_ARE_NOT_REWRITTEN_BY_TELL_REVISIONS
TELL_REVISIONS_REQUIRE_EVIDENCE_AND_GATE
HINT_INSTANCES_NEVER_REPLACE_TELLCORE_IDENTITY
```

