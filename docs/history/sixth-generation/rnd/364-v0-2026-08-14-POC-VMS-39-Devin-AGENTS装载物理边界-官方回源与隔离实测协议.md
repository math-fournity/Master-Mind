# POC-VMS-39：Devin CLI `AGENTS.md`装载物理边界——官方回源与隔离实测协议

**日期**：2026-08-14  
**状态**：`PREREGISTERED_NOT_STARTED`  
**路线阶段**：`SV-R0`  
**证据用途**：工程物理边界；不评价数学能力  
**执行载体**：Devin CLI `3000.4.25 (7e8e528a)`，`glm-5-2` / GLM-5.2 High  
**任务真值源**：363号  
**证据索引**：`system/tests/solve_vein_analysis/README.md`
**冻结清单**：`system/tests/solve_vein_analysis/live_fixtures/poc_vms_39.freeze.json`  
**fixture manifest SHA-256**：`0e0efbf56df0ffedc9b9fef7568e43c018ea08c3ff92011ccafedcd27e2c0bbc`

---

## 1. 问题与待检验主张

用户提出：Devin CLI的`AGENTS.md`可能“最多加载16K”。当前没有资格把这句话解释为16 KiB、16,000 bytes、16K characters或16K tokens。

本POC分开检验：

1. 文件发现层是否读到规则文件；
2. rule loader是否截断内容；
3. effective system message是否包含完整内容；
4. 模型是否能复述不同位置的sentinel；
5. 超限时的行为是拒绝、告警、截断、摘要还是不可观察；
6. 根规则、local规则和嵌套规则的加载时机是否与官方说明一致。

冻结假设：

- `H16`：当前CLI在不晚于16 KiB处截断单个`AGENTS.md`；
- `HFULL`：当前CLI没有16 KiB单文件硬截断，至少在本协议最大测试尺寸内完整注入；
- `HOTHER`：存在不同单位、合并预算、上下文预算、规则数量或模式依赖的限制。

本POC可以反驳`H16`并给出观察下界，但若在最大测试尺寸仍未失败，只能报告“至少完整到X bytes”，不能声称无限。

---

## 2. 官方与本机一手证据快照

### 2.1 官方资料

已回源：

- [Devin CLI Rules & AGENTS.md](https://docs.devin.ai/cli/extensibility/rules)
- [Devin AGENTS.md onboarding](https://docs.devin.ai/onboard-devin/agents-md)
- [Devin官方文档索引](https://docs.devin.ai/llms.txt)

官方当前明确：

- project-root `AGENTS.md`在session启动时自动读取；
- `AGENTS.md`是always-on规则；
- global和project规则可以同时生效；
- 子目录规则在agent访问对应目录时懒加载；
- 支持`AGENTS.local.md`、`AGENT.md`、`.windsurfrules`等；
- 官方建议Rules/AGENTS尽量短，并优先用按需Skill降低上下文与成本。

截至本协议回源，官方AGENTS页面、CLI rules页面和官方索引没有给出16K或其他数值型单文件上限。这个负结论只代表已检索的官方页面，不证明实现中不存在限制。

### 2.2 本机静态事实

| 项 | 冻结观察 |
|---|---|
| binary | `~/.local/bin/devin` |
| resolved SHA-256 | `18be04ae165c0918d163bf4454e65af8df0f94c8909c2bd8e8ae82407975d54f` |
| version | `devin 3000.4.25 (7e8e528a)` |
| model UID | `glm-5-2` |
| catalog label | `GLM-5.2 High [200K context, Free]` |
| official loader behavior | root启动加载；nested lazy |
| binary string evidence | 存在“Found … nested AGENTS.md files … loading the first …”诊断模板，但静态字符串无法恢复数值常量，也不能证明byte limit |

`devin rules --help/list/show/paths`提供规则发现观察面；模型调用的ATIF export提供effective system-message观察面。

### 2.3 既有ATIF可观测性证据

VMS-38的不可变export包含13个ATIF-v1.7 step，其中一个`source=system` message逐字包含该attempt完整`AGENTS.md`。因此本POC的主要endpoint不是“模型说它看见了什么”，而是：

```text
AGENTS.md exact bytes是否作为完整连续子串存在于ATIF system message
```

模型复述sentinel只是独立次级endpoint。

---

## 3. 永久保护边界

- 不修改或读取入题侧运行资产作为fixture；
- 不修改VMS-31—38物证；
- 新workspace只在`/data/master-mind-solve-vein-data/`批准根内；
- 不连接DB/Redis，不启动Target Solver；
- 不访问题目、答案、Tell库或Seven可变状态；
- 只调用Devin认知worker lane；
- `dangerous`只消除交互批准，不构成sandbox主张；
- 每个cell一个fresh session，零resume/continue；
- 禁止retry-until-visible；
- unknown-start必须quarantine。

---

## 4. Fixture合同

### 4.1 单文件尺寸

每个`AGENTS.md`：

- 只使用ASCII和LF，所以bytes=characters；
- 文件总尺寸精确等于cell声明；
- 由确定性generator生成；
- 至少在开头、8 KiB附近、16 KiB前后、中段和EOF前放唯一sentinel；
- padding不含`AGENTS_SENTINEL_`；
- 生成后保存SHA-256、byte count、line count和sentinel offset表；
- TASK不包含sentinel值，只描述输出规则。

sentinel格式：

```text
AGENTS_SENTINEL_<CELL>_<OFFSET>=<DETERMINISTIC_128BIT_VALUE>
```

### 4.2 冻结尺寸矩阵

| cell | exact bytes | 目的 |
|---|---:|---|
| A16M1 | 16,383 | 16 KiB边界前 |
| A16 | 16,384 | 16 KiB边界点 |
| A16P1 | 16,385 | 16 KiB边界后 |
| A32 | 32,768 | 对16 KiB主张的决定性反例cell |
| A64 | 65,536 | 观察下界扩展 |
| A128 | 131,072 | 观察下界扩展 |
| A256 | 262,144 | 本协议最大尺寸/预算停止点 |

### 4.3 嵌套/合并小矩阵

另有不调用模型的静态fixture：

- root `AGENTS.md` + `AGENTS.local.md`；
- root + child `AGENTS.md`；
- 多个child目录；
- 超过可疑数量的nested files（具体数量由静态诊断和本地规则list结果冻结后补入manifest）。

它只测discovery/list/show，不把静态结果冒充effective prompt。

---

## 5. 执行顺序与调用预算

### 5.1 Stage A：零模型静态loader

对全部尺寸运行`devin rules list/show`或等价只读命令，记录：

- exit code与stderr；
- rule identity/provider/scope；
- show输出是否完整；
- 是否出现size/count/truncation warning；
- nested发现顺序。

Stage A不得连接模型；若CLI subcommand本身触发远程推理，则立即停止并记协议偏差。

### 5.2 Stage B：最小live边界矩阵

固定顺序：`A16 → A16P1 → A32`。三者是判断16 KiB主张的必需cell。

条件扩展：

- 若A32完整：依次执行A64、A128、A256，直到首次不完整或到达预算停止点；
- 若A16P1或A32不完整：补A16M1，并停止扩大；根据三个边界cell输出范围，不在同一协议中无限二分；
- 任一cell发生unknown-start、答案/路径越界、export缺失或非基础设施协议故障，封存并停止后续live；
- 最大7个live attempts，实际可能更少；每cell一次、零重试。

全部可能被消费的attempt和最终目录在首次live前一次性冻结：

| cell | exact attempt ID | append-only final bundle |
|---|---|---|
| A16 | `poc-vms-39-a16-tmux-a1` | `poc-vms-39-a16-20260814/` |
| A16P1 | `poc-vms-39-a16p1-tmux-a1` | `poc-vms-39-a16p1-20260814/` |
| A32 | `poc-vms-39-a32-tmux-a1` | `poc-vms-39-a32-20260814/` |
| A64 | `poc-vms-39-a64-tmux-a1` | `poc-vms-39-a64-20260814/` |
| A128 | `poc-vms-39-a128-tmux-a1` | `poc-vms-39-a128-20260814/` |
| A256 | `poc-vms-39-a256-tmux-a1` | `poc-vms-39-a256-20260814/` |
| A16M1 | `poc-vms-39-a16m1-tmux-a1` | `poc-vms-39-a16m1-20260814/` |

只有条件执行规则触发时才消费对应attempt。未触发的attempt保持`NOT_RUN_BY_STOPPING_RULE`；已消费的ID无论PASS、FAIL、ABORT或INCONCLUSIVE都永久不重跑。

### 5.3 精确运行profile

| 字段 | 值 |
|---|---|
| carrier | Devin CLI；优先复用既有private tmux runtime以便观察 |
| model | `glm-5-2` |
| effort | High，由UID编码 |
| permission | `dangerous` |
| sandbox | false |
| config | 专用、无secret、关闭Cursor/Windsurf/Claude导入 |
| session | fresh；不resume、不continue |
| task | 不得用Read/Grep/Exec重读`AGENTS.md`；只允许Write严格visibility JSON并用`shasum`生成DONE，然后等待记账退出 |
| expected output | `agents-visibility-report.json`或print response的严格JSON |
| export | 每turn导出ATIF JSON |
| retry | scientific 0；infra 0（首版物理边界） |
| concurrency | 1 |

若为隔离global rule需要设置`XDG_CONFIG_HOME`，必须在fixture freeze前验证认证仍可用，并把env差异写入receipt；不得复制认证secret到workspace。

---

## 6. Endpoint与机械grader

### 6.1 Primary：effective injection

对ATIF所有`source=system` message执行byte-exact检查：

- `FULL_EXACT_SINGLE_MESSAGE`：完整AGENTS bytes连续出现一次；
- `FULL_EXACT_MULTI_MESSAGE`：内容被确定性分段但拼接后exact；
- `PREFIX_TRUNCATED_AT_N`；
- `SUFFIX_ONLY_FROM_N`；
- `TRANSFORMED_OR_PARTIAL`；
- `ABSENT`；
- `UNOBSERVABLE_EXPORT`。

记录最长共同前缀、最长共同后缀、每个sentinel是否出现、system message sizes和总prompt tokens。不得把UTF-8字符数替代bytes。

### 6.2 Secondary：model recall

严格解析模型JSON：

- reported sentinel precision/recall；
- hallucinated sentinels；
- 是否声明使用工具；
- raw tool event数量。

任何Read/Grep/Exec用于打开AGENTS都使次级endpoint`CONTAMINATED_BY_TOOL_READ`，但只要export本身完整，primary仍可判。

### 6.3 Static loader

记录规则show/list对文件的hash/size/内容完整性。如CLI只显示摘要，标`STATIC_VIEW_INSUFFICIENT`，不得据此推断截断。

---

## 7. Verdict规则

### `REFUTES_16K_FOR_FROZEN_PROFILE`

满足：A16P1或A32的primary为full exact，且version/model/profile/export/fixture全部有效。它只反驳本机该版本/profile下“16 KiB硬截断”，不证明其他版本或无限长度。

### `SUPPORTS_LIMIT_NEAR_16K_FOR_FROZEN_PROFILE`

A16M1/A16 full、A16P1/A32以稳定相同边界截断或拒绝，且不是模型上下文、export缺失、规则导入配置或fixture问题。一次随机模型不服从不能支持该结论。

### `OBSERVED_FULL_TO_<N>_BYTES`

最大已测cell primary full，但未找到失败点。报告观察下界，不声称真实maximum。

### `DIFFERENT_LIMIT_OR_MERGE_POLICY_OBSERVED`

截断/拒绝存在但不在16 KiB；报告精确观察和剩余不确定性。

### `INCONCLUSIVE_PROTOCOL`

export不可观察、配置未加载AGENTS、unknown-start、模型/profile漂移、fixture/hash不一致或其他协议缺失。

---

## 8. 对工程设计的预注册解释

用户最新决策是：Tell或Trace的积累不再依赖`AGENTS.md`，而是进入独立、内容寻址的数据文件。负责分片的AI遍历文件中每个item并产生逐项报告，但“已经遍历完”必须由程序核验，不能由AI自证：

- registry结构化保存全部Tell/Trace与Evidence；
- 冻结`TraceShard`/`TellShard`文件、snapshot hash、稳定`item_id`和顺序；
- 确定性enumerator逐项发布，AI输出逐项`MATCH | NO_MATCH | ABSTAIN | ERROR`和证据引用；
- append-only cursor保存已领取、已开始、已封存与失败状态，中断后可恢复；
- coverage verifier要求`expected_item_ids == reported_item_ids`且`missing=duplicate=unknown=0`；
- `AGENTS.md`只保留短遍历协议、权限边界、Schema指针与停止条件；
- 若primary无法观察effective rules，生产模式必须BLOCK而不是猜。

因此，VMS-39只决定**短控制协议**的可见性和安全长度余量，不再决定Tell库容量或Trace/Tell文件分片大小，也不验证Tell召回、选择正确性或数学增益。

---

## 9. 封存与审计

每cell至少封存：

- protocol/hash；
- generator/version/hash；
- exact `AGENTS.md`、TASK、config与fixture manifest；
- binary/version/catalog snapshot；
- sanitized argv和受限full argv hash；
- launch/control/health/intervention/final或abort receipt；
- stdout/stderr/export；
- primary/secondary grader report；
- protected absorb baseline；
- result document与README行。

结果文档必须单列：官方文档结论、静态loader结论、effective prompt结论、model recall结论、观察下界/失败边界、适用profile和非主张。

---

## 10. 启动门

本协议只有在以下全部完成后才从draft升为`PREREGISTERED_NOT_STARTED`：

1. deterministic fixture generator和grader有负向测试；
2. 全部cell manifest/hash冻结；
3. runner复用现有role/tmux runtime且有fake Devin测试；
4. README登记每个planned attempt；
5. 363 route lock绑定本协议和fixture hash；
6. 62项现有回归与新增测试全部PASS；
7. 入题侧保护基线不变；
8. D盘站点preflight通过；
9. 明确live cells的exact attempt IDs与零重试；
10. 本文档状态和freeze manifest同步。

在此之前不得启动任何VMS-39 Devin session。
