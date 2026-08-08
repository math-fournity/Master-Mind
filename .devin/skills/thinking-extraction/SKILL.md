---
name: thinking-extraction
description: >
  从devin cli提取完整推理过程（thinking）。两种方式：
  1. MITM流式实时截获——Solver思考过程中每个token实时落盘（mitmproxy responseheaders+stream callable）
  2. sessions.db事后提取——session结束后完整提取（thinking_extractor.py）
  WHEN to use: 需要分析AI为什么做不出某道题、需要理解AI的推理过程、需要提取挑战类型时、需要实时监控AI thinking时。
  WHEN NOT to use: 只需要AI的最终答案而不关心过程。
---

# thinking-extraction skill

## 两种获取方式

| 方式 | 工具 | 实时性 | 数据完整性 | 适用场景 |
|---|---|---|---|---|
| **MITM流式实时截获** | mitmproxy（自动，solver-harness启动时） | **token级实时**（思考过程中每个token立即落盘） | token级thinking + tool_calls | 实时监控、流式分析、RealtimePipeline |
| **sessions.db事后提取** | `thinking_extractor.py` | session结束后 | thinking + content + tool_calls + tool_results | 事后分析、挑战类型分析 |

两种方式获取的thinking内容完全一致（已验证2026-08-08）。MITM方式在Solver思考过程中实时落盘；sessions.db方式在session结束后提供完整数据（含tool_results）。

## 方式1：MITM流式实时截获（自动，无需手动操作）

solver-harness启动Solver时自动启用mitmproxy代理。核心机制：

1. mitmproxy的`responseheaders` hook在响应头到达时（body之前）触发
2. 设置`flow.response.stream = callable`
3. 每个HTTP chunk到达时callable被调用，`StreamingThinkingParser`实时解析Connect streaming protobuf
4. 每解析出一个thinking chunk（field 9）立即写入3个位置

### 实时查看thinking

```bash
# 查看所有实验的thinking流（实时）
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/thinking_live.txt

# 查看特定实验的thinking流（实时）
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/mitm/thinking_live.txt

# 程序化读取（JSONL格式，每个chunk一行）
cat /data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/mitm/thinking_live.jsonl
```

### JSONL格式

每行一个JSON对象，`type`字段区分记录类型：
- `thinking_chunk`：单个thinking chunk（含timestamp/counter/chunk_index/content）
- `tool_call_chunk`：单个tool_call chunk（含tool_call_id/name/args_chunk/is_start）
- `stream_complete`：一轮thinking完成后的汇总（含thinking_full完整文本/tool_calls列表/elapsed_seconds）

### 验证数据（2026-08-08）

- 120秒内11,397行txt + 10,971行jsonl
- chunk粒度1-7字符/token（如`+T`、`+(k`、`+approx`）
- 毫秒级时间戳（04:22:13.250 → 04:22:13.447）
- 第二轮thinking：12,865个chunks在2分钟内实时落盘

## 方式2：sessions.db事后提取

### 前置条件

- devin cli session已结束（或至少有足够的steps）
- sessions.db存在（`~/.local/share/devin/cli/sessions.db`）

### 工作流

#### 步骤1：确定session_id

```bash
# 方法A：知道session_id（从tmux session名或devin cli输出）
SESSION_ID="nova-authority"

# 方法B：知道工作目录（从实验目录路径）
WORK_DIR="/data/math-agent-glm5.2-tmux-agents-dir/<experiment-id>"

# 方法C：列出最近的session
sqlite3 ~/.local/share/devin/cli/sessions.db "SELECT id, title, working_directory, created_at FROM sessions ORDER BY created_at DESC LIMIT 10;"
```

#### 步骤2：确认有thinking数据

```bash
.venv/bin/python3 xishujuzhen/thinking_extractor.py --session-id ${SESSION_ID} --summary
# 或
.venv/bin/python3 xishujuzhen/thinking_extractor.py --work-dir ${WORK_DIR} --summary
```

**检查**：
- `Steps with thinking` > 0（有thinking数据）
- `Total thinking chars` > 1000（thinking数据足够分析）
- 如果`Steps with thinking` = 0，可能是旧版devin cli或非GLM-5.2模型

#### 步骤3：导出thinking数据

```bash
# 导出为JSON（完整数据，用于程序化分析）
.venv/bin/python3 xishujuzhen/thinking_extractor.py --session-id ${SESSION_ID} -o runs/<run_id>/thinking.json

# 导出为Markdown（可读，用于人工分析）
.venv/bin/python3 xishujuzhen/thinking_extractor.py --session-id ${SESSION_ID} --format markdown -o runs/<run_id>/thinking.md
```

#### 步骤4：分析thinking

读thinking.md或thinking.json，关注以下维度：

**AI的数学识别**：
- AI识别了什么数学结构？（如"这是关于badly approximable数的问题"）
- AI是否识别了正确的数学领域？

**AI的方法尝试**：
- AI尝试了什么方法？（如数值计算、符号计算、PSLQ封闭形式识别）
- AI尝试了几个不同的方法？

**AI的卡点**：
- AI在哪里停下来？（如"PSLQ找不到关系"、"精度不够"）
- AI的thinking中是否提到"不知道下一步该做什么"？
- AI是否意识到自己卡住了？

**AI的计算结果**：
- AI算出了什么数值？
- 数值和正确答案的差距是什么？
- AI是否尝试了从数值到封闭形式的转换？

**AI的工具使用**：
- AI调用了什么工具？（exec/web_search/read/write）
- 工具返回了什么结果？
- AI是否因为工具结果而改变方向？

#### 步骤5：提取挑战类型

基于thinking分析，判断这道题对AI的挑战类型：

| 挑战类型 | thinking中的特征 |
|---|---|
| 跨概念推理跳跃 | AI知道A和B但thinking中不知道A→B的路径 |
| 需要非显然构造 | AI的thinking中尝试了直接方法但失败，没有想到构造辅助对象 |
| 多约束联合 | AI的thinking中能处理单个约束但联合时卡住 |
| 领域识别错误 | AI的thinking中用了错误领域的方法 |
| 计算复杂度 | AI知道方法但thinking中提到"计算太复杂/太慢" |
| 封闭形式识别 | AI算出了数值但PSLQ/其他方法找不到封闭形式 |
| 证明结构缺失 | AI的thinking中有思路但无法组织成完整证明 |

## 注意事项

1. **thinking是英文的**：GLM-5.2的thinking用英文，content用中文——分析时注意语言差异
2. **node去重**：sessions.db中每个node出现两次（渲染重复），SDK已自动去重
3. **thinking可能为空**：不是每个assistant step都有thinking（如纯tool_call的step可能没有thinking）
4. **session必须已结束**：session还在跑时sessions.db数据不完整，但MITM流式数据是实时的
5. **tool_results有截断**：SDK截断长tool结果到5000字符，完整结果在sessions.db中
6. **MITM数据无tool_results**：MITM只截获thinking+tool_calls，tool_results在sessions.db中

## 与258号挑战类型分析的关系

258号方案要求分析25道题的AI response，判断AI为什么做不出。本skill提供提取AI完整推理过程的手段——258号分析的输入数据由本skill生成。

流程：
```
solver-tmux-launch启动Solver → Solver做题产生thinking数据
    ↓
    ├─ MITM流式实时截获 → thinking_live.jsonl（实时落盘，可tail -f）
    └─ sessions.db事后提取 → thinking.json/md（完整数据，含tool_results）
    ↓
258号挑战类型分析 → 分析thinking，判断挑战类型
    ↓
POC-VMS虚拟挑战构造 → 用挑战类型指导虚拟群论挑战生成
```
