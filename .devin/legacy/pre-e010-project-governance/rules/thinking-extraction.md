---
description: >
  分析AI解题过程时，优先用--export的conversation.json的reasoning_content字段（完整thinking），
  或用thinking_extractor.py从sessions.db提取（thinking在thinking.thinking字段）。
  mitmproxy已废弃（2026-08-18），不再用于thinking采集。
  thinking包含AI的完整推理链：尝试了什么、为什么失败、下一步打算做什么。
  WHEN to use: 需要分析AI为什么做不出某道题、需要理解AI的推理过程、需要提取挑战类型时。
  WHEN NOT to use: 只需要AI的最终答案而不关心过程。
trigger: model_decision
---

# thinking-extraction rule

## 硬约束

**分析AI解题过程时，必须提取完整thinking数据。** 有两个数据源，按优先级选择：

1. **--export的conversation.json（优先）**——`devin -p --export <path>`生成，agent step的`reasoning_content`字段包含完整thinking。简单、clean、不需要额外脚本。
2. **sessions.db提取（需要tool_results时）**——用`xishujuzhen/thinking_extractor.py`从sessions.db提取，thinking在`thinking.thinking`字段中，额外包含tool_results。

**mitmproxy已废弃（2026-08-18）**——不使用mitmproxy采集thinking。`--export`的conversation.json已包含`reasoning_content`（完整thinking），不需要MITM截获。

不能只看AI的content（输出给用户的内容）——content只是thinking的摘要。thinking才是AI的真实推理过程。

## 两个数据源

| 数据源 | 获取方式 | 实时性 | 数据完整性 | 用途 |
|---|---|---|---|---|
| **--export的conversation.json（优先）** | `devin -p --export <path>` | 每轮对话后实时写入 | reasoning_content（thinking）+ tool_calls + observation | 生产实验的标准数据源 |
| **sessions.db提取** | `thinking_extractor.py` | session结束后 | thinking.thinking + content + tool_calls + tool_results | 事后分析、挑战类型分析 |

**两个数据源的thinking内容一致**。--export方式更简单（不需要额外脚本）；sessions.db方式额外包含tool_results的完整输出。

## 原因

1. **thinking是AI的真实推理**：GLM-5.2的thinking字段包含AI的完整推理链（英文，平均6000+字符/步），content只是输出给用户的摘要（中文，平均50字符/步）
2. **thinking的字段位置因数据源而异**：--export的conversation.json中thinking在`reasoning_content`字段；sessions.db中thinking在`thinking.thinking`字段。两个数据源的thinking内容一致。
3. **失败分析需要thinking**：AI做不出题时，thinking中记录了"尝试了什么、为什么失败、下一步打算做什么"——这是挑战类型分析的核心数据
4. **tool_calls+tool_results是证据**：AI调用了什么工具（如Python计算）和工具返回了什么结果，是判断AI卡在哪里的关键证据

## 实施规范

### 从--export的conversation.json提取thinking

```python
import json

with open("<export_path>/conversation.json") as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]

for step in agent_steps:
    rc = step.get("reasoning_content", "")  # thinking
    tc = step.get("tool_calls", [])
    obs = step.get("observation", "")
    msg = step.get("message", "")
    # 分析rc（thinking）
```

### 从sessions.db提取thinking

```bash
# 按session_id提取
.venv/bin/python3 xishujuzhen/thinking_extractor.py --session-id <session_id> -o <output.json>

# 按工作目录提取（自动找最近的session）
.venv/bin/python3 xishujuzhen/thinking_extractor.py --work-dir <work_dir> -o <output.json>

# 只看摘要统计
.venv/bin/python3 xishujuzhen/thinking_extractor.py --session-id <session_id> --summary

# 导出为可读Markdown
.venv/bin/python3 xishujuzhen/thinking_extractor.py --session-id <session_id> --format markdown -o <output.md>
```

### 数据结构

每个step包含：
- `role`: user/assistant/tool
- `content`: AI输出给用户的内容（中文摘要）
- `thinking`: AI的完整推理过程（英文，可能为空）——sessions.db中用`thinking.thinking`字段
- `reasoning_content`: AI的完整推理过程——--export的conversation.json中用此字段
- `tool_calls`: AI调用的工具列表
- `tool_results`: 工具返回的结果

### 分析流程

1. 确认有thinking数据（--export检查`reasoning_content`非空；sessions.db用`--summary`检查`has_thinking > 0`）
2. 导出为JSON或Markdown
3. 读thinking字段，分析AI的推理链：
   - AI识别了什么数学结构？
   - AI尝试了什么方法？
   - AI在哪里卡住/走错？
   - AI的thinking中是否提到"不知道下一步该做什么"？
4. 结合tool_results看AI的计算结果：
   - AI算出了什么数值？
   - AI尝试了什么封闭形式识别（如PSLQ）？
   - 数值结果和正确答案的差距是什么？

## 与noninteractive-solver-run元组的关系

noninteractive-solver-run元组负责启动解题AI（`devin -p --export`），生成conversation.json。
thinking-extraction元组负责从conversation.json或sessions.db提取thinking数据进行分析。

两个元组的关系：
- noninteractive-solver-run：**生成**数据（启动session，产生conversation.json含reasoning_content）
- thinking-extraction：**提取分析**数据（从conversation.json提取reasoning_content，分析AI推理过程）

## 数据位置速查

| 数据 | 位置 | 字段 |
|---|---|---|
| thinking（--export） | conversation.json → steps[] → agent step | `reasoning_content` |
| thinking（sessions.db） | sessions.db → message_nodes → chat_message JSON | `thinking.thinking` |
| content | sessions.db → message_nodes → chat_message JSON | `content` |
| tool_calls | sessions.db → message_nodes → chat_message JSON | `tool_calls` |
| tool_results | sessions.db → tool_call_state | `tool_call_update_json` |
| session元信息 | sessions.db → sessions | `id, title, working_directory, model, created_at` |
