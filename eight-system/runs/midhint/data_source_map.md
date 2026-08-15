# 错题分析系统·数据源定位文档

> **用途**：错题分析系统需要三类数据——题目文本、标准答案、AI历史解题过程（thinking/trajectory）。本文档记录每类数据的存放位置、格式、获取方法。
>
> **维护规则**：新增题库或trajectory格式变化时，更新本文档并commit。

---

## 一、总览：三类数据的定位链

```
problem_id（ArangoDB devin_problem_runs.problem_id）
    ├── 题目文本 ← solver工作目录的AGENTS.md（或problem.txt）
    ├── 标准答案 ← 题库原始数据文件（parquet/jsonl/lean/json）
    └── AI解题过程 ← trajectory目录（exports/conversation.json等4级优先级）
```

**关键映射**：`devin_problem_runs`集合的`exp_id`字段是枢纽——
- solver工作目录 = `/data/math-agent-glm5.2-tmux-agents-dir/{exp_id}/`
- trajectory目录 = `/data/math-agent-glm5.2-tmux-agents-trajectory/{exp_id}/`

---

## 二、失败题列表：从ArangoDB获取

**集合**：`devin_problem_runs`（数据库`xishujuzhen_math_glm52`，localhost:8529，root/REDACTED-DB-PASSWORD）

**查询**：
```python
from arango import ArangoClient
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
aql = '''FOR r IN devin_problem_runs 
  FILTER r.status IN ["failed_no_proof","failed_token_limit","failed_tool_stall"]
  RETURN {problem_id: r.problem_id, exp_id: r.exp_id, status: r.status, runtime: r.runtime_seconds}'''
all_runs = list(db.aql.execute(aql))
```

**去重规则**：同一problem_id可能有多条记录（rerun），取`runtime_seconds`最大的那条——runtime最长的最可能是真正尝试过的。

**exp_id有两种格式**：
- 批量跑：`dpb-{日期}-{批次名}-{序号}-p{problem_entries_key}-g{序号}-{problem_id}`
- 单独跑：`p{16位hex}`（如`p94c2bfe7f8b344b79487`）

**devin_problem_runs的完整字段**：
```
problem_id, exp_id, batch_id, tmux_session, status, verdict,
started_at, ended_at, runtime_seconds, end_reason, model
```

**注意**：devin_problem_runs中没有`problem_text`（题目文本）——题目文本在solver工作目录的AGENTS.md中。

---

## 三、题目文本：从solver工作目录获取

**位置**：`/data/math-agent-glm5.2-tmux-agents-dir/{exp_id}/AGENTS.md`

**格式**：AGENTS.md包含解题指令+答案泄漏自检+题目内容。题目在`## Problem`节之后。

**提取方法**：
```python
import os
solver_dir = f"/data/math-agent-glm5.2-tmux-agents-dir/{exp_id}"
agents_path = os.path.join(solver_dir, "AGENTS.md")
with open(agents_path) as f:
    content = f.read()
# 题目在"## Problem"之后
if "## Problem" in content:
    problem_text = content.split("## Problem", 1)[1].strip()
```

**备选**：部分目录有`problem.txt`文件（旧格式），但大部分只有AGENTS.md。

**注意**：部分exp_id目录可能不存在（D盘未挂载时）或AGENTS.md为空（连接错误秒退的run）。

---

## 四、标准答案：从题库原始数据文件获取

### 4.1 题库总览

| 题库 | problem_id前缀 | 失败题数 | 有解答 | 数据格式 | 解答字段 | 位置 |
|---|---|---|---|---|---|---|
| PolyMath | `polymath_` | 4709 | ✅ | parquet | `solution` | `/data/math-manify/raw_downloads/PolyMath/` |
| DeepMath-103K | `deepmath_103k_` | 710 | ✅ | parquet | `r1_solution_1` | `/data/math-manify/raw_downloads/DeepMath-103K/` |
| ODA-Math-460k | `oda_math_460k_` | 398 | ✅ | parquet | `response` | `/data/math-manify/raw_downloads/ODA-Math-460k/` |
| compfiles | `compfiles_` | 184 | ✅ | lean文件 | lean proof | `knowledge/problem_banks/compfiles/Compfiles/` |
| Omni-MATH-2 | `omni_math_` | 91 | ✅ | jsonl | `solution` | `/data/math-manify/raw_downloads/Omni-MATH-2/` |
| fate | `fate_` | 69 | ❌ | json | formal_statement(Lean) | `knowledge/problem_banks/fate/` |
| AIME 2024 | `aime_2024_` | 13 | ✅ | jsonl | `solution` | `knowledge/problem_banks/aops_instruct/eval/data/aime24/` |
| AMO-Bench | `amo_bench_` | 5 | ✅ | parquet | `solution` | `/data/math-manify/raw_downloads/AMO-Bench/` |
| OlympiadBench | `mathnet_` | 2 | ✅ | json | `solution` | `knowledge/problem_banks/aops_instruct/eval/data/olympiadbench/test.json` |
| mathnet | `mathnet_` | 2 | ❓ | 未知 | 未知 | `knowledge/problem_banks/mathnet/` |

**总计**：6181失败题，6110有标准解答（98%），69无解答（fate，只有Lean formal statement）。

### 4.2 各题库的id映射规则

**PolyMath**：`polymath_{id:05d}` → parquet中的`id`字段（整数）
- 数据文件：`/data/math-manify/raw_downloads/PolyMath/data/train-00000-of-00001.parquet`
- 也有`normal/`（id 0-5896）和`revised/`（id 10000-15192）两个子目录
- `data/`是合并版（11090行），但id不连续——有gap
- **注意**：部分polymath题的id在parquet中找不到（1564道not_found）——可能id映射规则不是简单的整数对应，需要进一步调查

**DeepMath-103K**：`deepmath_103k_{id:08d}` → 按行索引（没有id字段）
- 数据文件：`/data/math-manify/raw_downloads/DeepMath-103K/data/train-00000-of-00010.parquet`（10个文件）
- 行索引跨文件连续：file 0的行0-10302，file 1的行10303-20605，...
- `deepmath_103k_00000688` → 第688行 → file 0的第688行
- **注意**：DeepMath的`r1_solution_1`是AI生成的解答（r1模型），不是人类专家解答——质量可能参差不齐

**ODA-Math-460k**：`oda_math_460k_{id:08d}` → parquet中的`id`字段（整数）
- 数据文件：`/data/math-manify/raw_downloads/ODA-Math-460k/data/train-00000-of-00004.parquet`（5个文件）
- `response`字段是AI生成的解答——质量可能参差不齐

**Omni-MATH-2**：`omni_math_{id:06d}` → jsonl中的`id`字段（整数）
- 数据文件：`/data/math-manify/raw_downloads/Omni-MATH-2/Omni-Math-2.jsonl`（4428行）
- `solution`字段是人类专家解答——质量高

**OlympiadBench**：`mathnet_{id:06d}` → json中的`id`字段（整数）
- 数据文件：`knowledge/problem_banks/aops_instruct/eval/data/olympiadbench/test.json`
- `solution`字段是列表（需要join），`final_answer`字段是答案
- **注意**：`mathnet_`前缀的题只有2道失败，但之前分析过的19道题中很多是`mathnet_`前缀——这些是历史bare retest的题

**compfiles**：`compfiles_{竞赛名}{年份}p{题号}` → lean文件
- 目录：`knowledge/problem_banks/compfiles/Compfiles/`
- 文件名：如`IMO1963P6.lean`、`USA1989P5.lean`、`Bulgaria1998P6.lean`
- 解答是lean formal proof——需要理解Lean才能提取关键转折点
- **注意**：lean proof不是人类可读的数学推理过程，用于错题分析时可能需要额外翻译

**AIME 2024**：`aime_2024_{题号:04d}` → jsonl中的行索引
- 数据文件：`knowledge/problem_banks/aops_instruct/eval/data/aime24/test.jsonl`
- `aime_2024_0012` → 第12题 → 行索引11（从0开始）

**AMO-Bench**：`amo_bench_{id:08d}` → parquet中的`question_id`字段
- 数据文件：`/data/math-manify/raw_downloads/AMO-Bench/data/test-00000-of-00001.parquet`
- `prompt`字段是题目，`solution`字段是解答

**fate**：`fate_{id:06d}` → json中的`id`字段
- 数据文件：`knowledge/problem_banks/fate/fate_batch_1.json`（70道）
- **无人类解答**——只有`formal_statement`（Lean形式化命题），不适合做错题分析

### 4.3 标准答案获取脚本

已有脚本：`eight-system/scripts/midhint/full_analysis.py`中的`match_problem_to_solution()`函数

```python
# 用法示例
from full_analysis import (
    load_polymath, load_deepmath, load_oda_math, 
    load_omni_math, load_olympiadbench, load_aime, load_amo_bench,
    match_problem_to_solution
)

polymath = load_polymath()
deepmath = load_deepmath()
# ... 加载所有题库

sol_data, source = match_problem_to_solution(
    "polymath_01687", polymath, deepmath, oda_math, omni_math, olympiadbench, aime, amo_bench
)
if sol_data:
    print(sol_data['problem'])   # 题目文本
    print(sol_data['solution'])  # 标准解答
    print(sol_data['answer'])    # 最终答案
```

### 4.4 已知问题

1. **PolyMath 1564道not_found**：`polymath_{id:05d}`的id映射可能不是简单的整数对应。需要调查problem_extraction_progress集合或原始录入脚本确认正确的映射规则。

2. **DeepMath/ODA-Math的解答质量**：这两个题库的解答字段（`r1_solution_1`/`response`）是AI生成的，不是人类专家解答。用于错题分析时，"标准解答"本身可能有误——需要交叉验证或只用于提取关键技巧名。

3. **compfiles的lean proof**：Lean形式化证明不是人类可读的推理过程。用于错题分析时，可能需要先用AI将lean proof翻译成自然语言推理，或者用compfiles网站上的非形式化解答。

4. **"congruen"关键词歧义**：`congruen`同时匹配"congruent mod p"（同余）和"congruent triangle"（几何全等）。关键词匹配方法不可靠——这正是需要用AI做分析的原因。

---

## 五、AI解题过程（thinking/trajectory）：从trajectory目录获取

### 5.1 目录位置

**trajectory目录**：`/data/math-agent-glm5.2-tmux-agents-trajectory/{exp_id}/`

### 5.2 目录结构

```
{exp_id}/
├── session_info.json          # session元信息（session_id, model, work_dir等）
├── sessions_db/
│   └── trajectory.jsonl       # sessions.db导出的step级trajectory
├── mitm/                      # MITM代理截获的实时数据（最完整）
│   ├── thinking_live.jsonl    # 流式thinking（JSON格式，每个token一条）
│   ├── thinking_live.txt      # 流式thinking（纯文本，拼接后）
│   ├── thinking_readable.txt  # 可读格式thinking（去重后）
│   └── trajectory.jsonl       # MITM截获的完整trajectory
├── exports/
│   └── conversation.json      # devin cli --export导出的对话（含reasoning_content）
├── collector/
│   ├── pane_snapshot.txt      # tmux pane快照（原始）
│   └── pane_snapshot_clean.txt # tmux pane快照（清洗后）
└── tmux/
    ├── tmux.log               # tmux日志
    └── tmux_pipe.log          # tmux pipe-pane输出（兜底）
```

### 5.3 thinking文本的4级优先级

不同run的trajectory目录结构不同——有的有mitm/，有的没有；有的有exports/，有的只有sessions_db/。获取thinking文本时按以下优先级尝试：

| 优先级 | 文件 | 格式 | 说明 |
|---|---|---|---|
| 1 | `mitm/thinking_readable.txt` | 纯文本 | MITM截获的可读格式，最完整。但部分run没有MITM（--no-mitm启动） |
| 2 | `sessions_db/trajectory.jsonl` | JSONL | sessions.db导出的step级数据。每行一个step，`thinking`字段是推理内容。需要去重（同一thinking可能出现在多个step中） |
| 3 | `exports/conversation.json` | JSON | devin cli --export导出。`steps`数组中每个step有`reasoning_content`字段 |
| 4 | `collector/pane_snapshot_clean.txt` | 纯文本 | tmux pane快照，兜底数据源。内容可能不完整 |

**获取脚本**：`eight-system/scripts/midhint/full_analysis.py`中的`get_thinking_text()`函数

```python
from full_analysis import get_thinking_text

thinking = get_thinking_text("dpb-20260812-021956-tier123-landscape-scan-01-p329031-g000003-compfiles_imo1963p6")
if thinking:
    print(f"Thinking length: {len(thinking)} chars")
```

### 5.4 trajectory.jsonl的格式

**sessions_db/trajectory.jsonl**（最通用的数据源）：
```json
{
  "type": "step",
  "node_id": 8,
  "parent_node_id": 7,
  "role": "user|assistant",
  "content": "消息内容",
  "thinking": "推理内容（assistant的thinking）",
  "tool_calls": [],
  "created_at": 1786658644
}
```

**exports/conversation.json**（devin cli --export格式）：
```json
{
  "steps": [
    {
      "source": "user|agent|system",
      "message": "消息内容",
      "reasoning_content": "推理内容（agent的thinking）",
      "tool_calls": [...]
    }
  ]
}
```

### 5.5 已知问题

1. **部分run没有thinking数据**：6181道失败题中，127道没有thinking文件（2%）。这些通常是连接错误秒退的run——`runtime_seconds`很短（如9秒），`pane_snapshot_clean.txt`内容是`Error: Agent error: Connection error`。

2. **部分run的thinking很短**：有些run的thinking只有几百字符——AI可能刚开头就遇到了错误或超时。这些run不适合做错题分析（AI没有真正尝试解题）。

3. **MITM数据不一定有**：部分run是用`--no-mitm`启动的，没有`mitm/`目录。这些run只能用`sessions_db/`或`exports/`作为数据源。

4. **conversation.json的reasoning_content可能为空**：部分run的`exports/conversation.json`存在但`reasoning_content`字段为空——可能是模型不支持thinking或导出时没有捕获thinking。

---

## 六、完整的数据获取流程

### 6.1 从problem_id到完整数据

```python
import os, json, re
from arango import ArangoClient

# 1. 从DB获取exp_id
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
aql = 'FOR r IN devin_problem_runs FILTER r.problem_id == @pid SORT r.runtime_seconds DESC LIMIT 1 RETURN r'
bind = {'pid': 'polymath_01687'}
run = list(db.aql.execute(aql, bind_vars=bind))[0]
exp_id = run['exp_id']

# 2. 获取题目文本（从solver工作目录的AGENTS.md）
solver_dir = f"/data/math-agent-glm5.2-tmux-agents-dir/{exp_id}"
with open(os.path.join(solver_dir, "AGENTS.md")) as f:
    content = f.read()
problem_text = content.split("## Problem", 1)[1].strip() if "## Problem" in content else ""

# 3. 获取标准答案（从题库原始数据文件）
from full_analysis import match_problem_to_solution, load_polymath, load_deepmath, ...
polymath = load_polymath()
# ... 加载所有题库
sol_data, source = match_problem_to_solution("polymath_01687", polymath, ...)
standard_solution = sol_data['solution'] if sol_data else ""

# 4. 获取AI解题过程（从trajectory目录）
from full_analysis import get_thinking_text
thinking = get_thinking_text(exp_id)
```

### 6.2 批量获取所有失败题的数据

已有脚本：`eight-system/scripts/midhint/full_analysis.py --phase map`

该脚本会：
1. 从DB获取所有失败题（去重取runtime最长的）
2. 加载所有题库数据
3. 对每道题匹配标准解答
4. 检查trajectory目录是否有thinking数据
5. 输出`eight-system/runs/midhint/full_mapping.json`

**当前结果**（2026-08-15）：
- 6181失败题
- 4364有标准解答
- 6054有thinking数据
- 4325有both

---

## 七、用AI做错题分析的方案

### 7.1 为什么不能用关键词匹配

之前用关键词匹配（检查标准解答中是否含"mod 4"/"valuation"等关键词，再检查thinking中是否含同样的关键词）来判定DIRECTION_ERROR vs TOKEN_LIMIT。这种方法不可靠：

1. **"congruen"歧义**：同时匹配"congruent mod p"（同余）和"congruent triangle"（几何全等）
2. **"valuation"歧义**：同时匹配"p-adic valuation"（赋值）和"evaluation"（求值）的子串
3. **"mod 4"出现一次不代表方向对了**：AI可能在无关上下文中提到mod 4，但没有真正使用mod 4分析
4. **无法区分连接错误和方向错误**：连接错误秒退的run，thinking中没有关键词，会被误判为DIRECTION_ERROR

### 7.2 用devin cli做AI分析的方案

**核心思路**：和解题系统一样——构造AGENTS.md，让devin cli在不调用任何工具的情况下，通过分析AGENTS.md中的内容输出分析结果。

**AGENTS.md内容**：
1. 分析任务说明（两个维度的判定标准）
2. 题目文本
3. 标准解答
4. AI的thinking过程
5. 输出格式要求（JSON + ### ANALYSIS COMPLETE）

**启动方式**：
```bash
# 创建工作目录
mkdir -p /data/math-agent-glm5.2-tmux-agents-dir/midhint-analysis-{problem_id}

# 写入AGENTS.md（包含标准解答+thinking+分析任务）
# ... 用Python脚本构造AGENTS.md

# 用tmux启动devin cli
tmux new-session -d -s midhint-analysis-{problem_id} \
  "cd /data/math-agent-glm5.2-tmux-agents-dir/midhint-analysis-{problem_id} && \
   devin --permission-mode dangerous --respect-workspace-trust false -- \
   '请按AGENTS.md中的分析任务执行分析。直接在TUI中输出分析结果，不要写任何文件，结尾输出 ### ANALYSIS COMPLETE' \
   2>&1 | tee /data/math-agent-glm5.2-tmux-agents-trajectory/midhint-analysis-{problem_id}-tmux.log"
```

**并发**：多道题可以并发启动多个tmux session，每个session分析一道题。

**结果收集**：从tmux pane或--export导出的conversation.json中提取分析结果（JSON格式）。

### 7.3 分析维度

**维度1：方向出错 vs token不够 vs 连接错误**
- DIRECTION_ERROR：AI的thinking走了错误方向，没有使用标准解答的关键方法
- TOKEN_LIMIT：AI的thinking在正确方向上，但token用尽没完成
- CONNECTION_ERROR：AI没有真正尝试（连接错误、秒退、thinking极短无数学内容）

**维度2：卡点类型**（仅DIRECTION_ERROR的题）
- mod_p_grouping：mod p分组/同余（p显然）
- mod_p_non_obvious：mod p同余（p不显然）
- quadratic_residue_euler：二次剩余+Euler准则
- lte_lemma：Lifting The Exponent lemma
- p_adic_valuation：p-adic赋值
- multi_step_mod_p：多步mod p推导
- crt：中国剩余定理
- other：其他

---

## 八、文件索引

| 文件 | 用途 |
|---|---|
| `eight-system/scripts/midhint/full_analysis.py` | 完整梳理脚本（映射+关键词分析） |
| `eight-system/runs/midhint/full_mapping.json` | problem_id → 标准解答+thinking的映射 |
| `eight-system/runs/midhint/full_analysis_results.json` | 关键词分析结果（131 DIRECTION_ERROR） |
| `eight-system/scripts/midhint/analyze_failure.py` | 早期单题分析脚本 |
| `eight-system/runs/midhint/failure_analysis_results.json` | 早期19道题的分析结果 |
| `eight-system/runs/midhint/preregistration.md` | Mid-Hint实验预注册方案 |
| 本文档 | 数据源定位文档 |

---

## 九、待解决问题

1. **PolyMath 1564道not_found**：需要调查正确的id映射规则
2. **DeepMath/ODA-Math解答质量**：AI生成的解答可能不可靠，需要交叉验证
3. **compfiles的lean proof翻译**：需要将lean proof翻译成自然语言推理才能做错题分析
4. **并发分析的AGENTS.md模板**：需要制作标准化的AGENTS.md模板，用于并发启动devin cli做分析
5. **分析结果收集脚本**：需要写脚本从tmux pane或conversation.json中提取分析结果
