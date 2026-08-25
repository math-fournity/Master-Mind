---
name: thinking-extraction
description: >
  从devin cli提取完整推理过程（thinking）。两个数据源：
  1. --export的conversation.json（优先）——reasoning_content字段包含完整thinking
  2. sessions.db事后提取——thinking_extractor.py从thinking.thinking字段提取
  mitmproxy已废弃（2026-08-18），不再用于thinking采集。
  WHEN to use: 需要分析AI为什么做不出某道题、需要理解AI的推理过程、需要提取挑战类型时。
  WHEN NOT to use: 只需要AI的最终答案而不关心过程。
---

# thinking-extraction skill

## 两个数据源

| 数据源 | 获取方式 | 实时性 | 数据完整性 | 用途 |
|---|---|---|---|---|
| **--export的conversation.json（优先）** | `devin -p --export <path>` | 每轮对话后实时写入 | reasoning_content（thinking）+ tool_calls + observation | 生产实验的标准数据源 |
| **sessions.db事后提取** | `thinking_extractor.py` | session结束后 | thinking.thinking + content + tool_calls + tool_results | 事后分析、挑战类型分析 |

**两个数据源的thinking内容一致**。--export方式更简单（不需要额外脚本）；sessions.db方式额外包含tool_results的完整输出。

**mitmproxy已废弃（2026-08-18）**——不再用于thinking采集。`--export`的conversation.json已包含`reasoning_content`（完整thinking），不需要MITM截获。

## 方式1：从--export的conversation.json提取（优先）

### 前置条件

- devin cli session已用`--export`运行，conversation.json已生成

### 工作流

#### 步骤1：读取conversation.json

```python
import json

with open("<export_path>/conversation.json") as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]

# 检查数据完整性
for i, step in enumerate(agent_steps):
    rc = step.get("reasoning_content", "")
    tc = step.get("tool_calls", [])
    obs = step.get("observation", "")
    msg = step.get("message", "")
    print(f"step[{i}]: reasoning={len(str(rc))}chars, "
          f"tool_calls={len(tc)}items, "
          f"observation={len(str(obs))}chars, "
          f"message={len(str(msg))}chars")
```

#### 步骤2：提取thinking

```python
for step in agent_steps:
    rc = step.get("reasoning_content", "")  # thinking
    # rc就是AI的完整推理过程
```

#### 步骤3：分析thinking

读`reasoning_content`字段，关注以下维度：

**AI的数学识别**：
- AI识别了什么数学结构？
- AI是否识别了正确的数学领域？

**AI的方法尝试**：
- AI尝试了什么方法？
- AI尝试了几个不同的方法？

**AI的卡点**：
- AI在哪里停下来？
- AI的thinking中是否提到"不知道下一步该做什么"？
- AI是否意识到自己卡住了？

## 方式2：从sessions.db提取（需要tool_results时）

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
- AI识别了什么数学结构？
- AI是否识别了正确的数学领域？

**AI的方法尝试**：
- AI尝试了什么方法？（如数值计算、符号计算、PSLQ封闭形式识别）
- AI尝试了几个不同的方法？

**AI的卡点**：
- AI在哪里停下来？
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
4. **session必须已结束**：session还在跑时sessions.db数据不完整
5. **tool_results有截断**：SDK截断长tool结果到5000字符，完整结果在sessions.db中
6. **字段位置因数据源而异**：--export用`reasoning_content`，sessions.db用`thinking.thinking`

## 与noninteractive-solver-run元组的关系

```
noninteractive-solver-run启动Solver（devin -p --export）
    ↓
    ├─ --export的conversation.json（reasoning_content=thinking，优先）
    └─ sessions.db事后提取 → thinking.json/md（含tool_results）
    ↓
thinking-extraction → 分析thinking，判断挑战类型
    ↓
POC-VMS虚拟挑战构造 → 用挑战类型指导虚拟群论挑战生成
```

## 与258号挑战类型分析的关系

258号方案要求分析25道题的AI response，判断AI为什么做不出。本skill提供提取AI完整推理过程的手段——258号分析的输入数据由本skill生成。
