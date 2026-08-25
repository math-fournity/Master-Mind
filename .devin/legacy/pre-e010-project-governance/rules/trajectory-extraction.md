---
description: >
  需要获取devin cli的完整trajectory时，优先用--export的conversation.json（含reasoning_content=thinking），
  或用trajectory_extractor.py从sessions.db提取（含tool_results + 树结构）。
  trajectory = AI从头到尾的完整工作过程，包含thinking + content + tool_calls + tool_results。
  --export的conversation.json中thinking在reasoning_content字段；sessions.db中thinking在thinking.thinking字段。
  mitmproxy已废弃（2026-08-18），不再用于trajectory采集。
  WHEN to use: 需要完整重建AI工作过程、检索系统需要trajectory数据、分析AI推理链、session还在跑需要持续更新trajectory。
  WHEN NOT to use: 只需要AI的最终答案、只需要thinking不需要tool_results（用--export的conversation.json即可）。
trigger: model_decision
---

# trajectory-extraction rule

## 硬约束

**需要获取devin cli的完整trajectory时，有两个数据源，按优先级选择：**

1. **--export的conversation.json（优先）**——`devin -p --export <path>`生成，agent step的`reasoning_content`字段包含完整thinking，`tool_calls`和`observation`包含工具调用和结果。简单、clean、不需要额外脚本。
2. **sessions.db提取（需要tool_results和树结构时）**——用`xishujuzhen/trajectory_extractor.py`从sessions.db提取，thinking在`thinking.thinking`字段中，额外包含tool_results的完整输出和parent-child树结构。

**mitmproxy已废弃（2026-08-18）**——不使用mitmproxy采集trajectory。`--export`的conversation.json已包含`reasoning_content`（完整thinking），不需要MITM截获。

## 与thinking-extraction元组的关系

| 元组 | 数据源 | 数据范围 | 用途 |
|---|---|---|---|
| thinking-extraction | --export的conversation.json（优先）/ sessions.db | thinking + content + tool_calls | 分析AI为什么做不出（关注推理过程） |
| trajectory-extraction | --export的conversation.json（优先）/ sessions.db | **完整trajectory**（含tool_results + 树结构 + 增量更新） | 检索系统的基础数据、完整重建AI工作过程 |

trajectory-extraction是thinking-extraction的超集：trajectory包含thinking的所有内容，还额外包含tool_results的完整输出、parent-child树结构、增量更新能力。

## 实施规范

### 提取完整trajectory

```bash
# 按session_id提取（JSONL格式，推荐用于检索系统）
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id <session_id> -o <output.jsonl>

# 按工作目录提取
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --work-dir <work_dir> -o <output.jsonl>

# 只看摘要统计
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id <session_id> --summary

# 导出为可读Markdown
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id <session_id> --format markdown -o <output.md>
```

### 增量更新（session还在跑时）

```bash
# 第一次提取
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id <session_id> -o trajectory.jsonl

# 后续增量更新（只追加新steps）
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id <session_id> --incremental -o trajectory.jsonl
```

### Trajectory JSONL Schema

第一行：`session_meta`（session元信息 + 统计）
后续每行：一个`step`（按node_id排序，去重后）

每个step包含：
- `step_index`: 在trajectory中的序号
- `node_id` / `parent_node_id`: 树结构
- `role`: user/assistant/tool
- `content`: AI输出给用户的内容
- `thinking`: AI的完整推理过程（thinking.thinking字段）
- `tool_calls`: 工具调用列表（name, kind, title, arguments, raw_input）
- `tool_results`: 工具返回结果（status, output, meta）

## 数据源速查

trajectory有两个数据源，按优先级选择：

| 数据源 | 获取方式 | 实时性 | 数据完整性 | 用途 |
|---|---|---|---|---|
| **--export的conversation.json（优先）** | `devin -p --export <path>` | 每轮对话后实时写入 | reasoning_content（thinking）+ tool_calls + observation | 生产实验的标准数据源 |
| **sessions.db** | `trajectory_extractor.py` / `trajectory_monitor.py` | session结束后完整（或3秒轮询接近实时） | thinking.thinking + content + tool_calls + tool_results + 树结构 | 完整重建AI工作过程、检索系统索引 |

**mitmproxy已废弃（2026-08-18）**——不再用于trajectory采集。历史MITM数据（`<exp_id>/mitm/`目录）仍可查阅，但不再产生新数据。

### sessions.db数据源（事后完整提取）

| 数据 | 表 | 字段 | 说明 |
|---|---|---|---|
| session元信息 | sessions | id, title, working_directory, model, created_at | Session级别 |
| 消息树 | message_nodes | node_id, parent_node_id, chat_message, created_at | 树结构对话 |
| thinking | message_nodes.chat_message JSON | thinking.thinking | AI推理过程 |
| content | message_nodes.chat_message JSON | content | AI输出内容 |
| tool_calls | message_nodes.chat_message JSON | tool_calls[].id/name/arguments | AI调用的工具 |
| 工具输入 | tool_call_state | tool_call_json.rawInput | 工具的完整输入参数 |
| 工具输出 | tool_call_state | tool_call_update_json.content | 工具返回的结果 |
| 工具状态 | tool_call_state | tool_call_update_json.status | completed/failed |

## 关键技术细节

1. **Node去重**：sessions.db中每个assistant node出现两次（devin cli渲染机制），SDK自动去重保留第一个
2. **tool_call_id关联**：assistant的tool_calls[].id = tool node的tool_call_id = tool_call_state.tool_call_id
3. **thinking的字段位置因数据源而异**：--export的conversation.json中thinking在`reasoning_content`字段；sessions.db中thinking在`thinking.thinking`字段。两个数据源的thinking内容一致。
4. **tool_name推断**：SDK从rawInput字段推断工具名（exec/read/write/get_output/kill_shell/web_search等）
5. **增量更新**：--incremental模式读取已有JSONL的最后一个node_id，只追加新steps
