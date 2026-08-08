---
description: >
  需要获取tmux中devin cli的完整trajectory时，必须用trajectory_extractor.py从sessions.db提取。
  trajectory = AI从头到尾的完整工作过程，包含thinking + content + tool_calls + tool_results。
  数据在sessions.db的message_nodes.chat_message JSON的thinking.thinking字段 + tool_call_state表。
  支持JSONL/Markdown/JSON三种格式 + 增量更新。
  WHEN to use: 需要完整重建AI工作过程、检索系统需要trajectory数据、分析AI推理链、session还在跑需要持续更新trajectory。
  WHEN NOT to use: 只需要AI的最终答案、只需要thinking不需要tool_results（用thinking_extractor.py即可）。
trigger: model_decision
---

# trajectory-extraction rule

## 硬约束

**需要获取tmux中devin cli的完整trajectory时，必须使用 `xishujuzhen/trajectory_extractor.py`。**

trajectory = AI从头到尾的完整工作过程——thinking（推理） + content（输出） + tool_calls（工具调用） + tool_results（工具结果），按时间排序，带树结构。

## 与thinking-extraction元组的关系

| 元组 | 脚本 | 数据范围 | 用途 |
|---|---|---|---|
| thinking-extraction | thinking_extractor.py | thinking + content + tool_calls | 分析AI为什么做不出（关注推理过程） |
| trajectory-extraction | trajectory_extractor.py | **完整trajectory**（含tool_results + 树结构 + 增量更新） | 检索系统的基础数据、完整重建AI工作过程 |

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
3. **thinking在thinking.thinking字段**：不是reasoning_content（那个是空的）
4. **tool_name推断**：SDK从rawInput字段推断工具名（exec/read/write/get_output/kill_shell/web_search等）
5. **增量更新**：--incremental模式读取已有JSONL的最后一个node_id，只追加新steps
