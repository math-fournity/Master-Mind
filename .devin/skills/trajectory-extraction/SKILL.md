---
name: trajectory-extraction
description: >
  用trajectory_extractor.py从sessions.db提取devin cli的完整trajectory。
  trajectory = AI从头到尾的完整工作过程（thinking + content + tool_calls + tool_results）。
  支持JSONL/Markdown/JSON三种格式 + 增量更新。
  WHEN to use: 需要完整重建AI工作过程、检索系统需要trajectory数据、分析AI推理链、session还在跑需要持续更新。
  WHEN NOT to use: 只需要thinking不需要tool_results（用thinking_extractor.py即可）。
---

# trajectory-extraction skill

## 用途

从sessions.db提取devin cli的完整trajectory，用于：
1. 检索系统的基础数据——检索系统需要trajectory来索引AI的工作过程
2. 完整重建AI工作过程——从session开始到结束的每一步
3. 分析AI推理链——thinking + tool_calls + tool_results的完整链条
4. 持续监控——session还在跑时增量更新trajectory

## 前置条件

- devin cli session已产生数据（至少有1个assistant node）
- sessions.db存在（`~/.local/share/devin/cli/sessions.db`）

## 工作流

### 步骤1：确定session_id

```bash
# 方法A：知道session_id（从tmux session名或devin cli输出）
SESSION_ID="nova-authority"

# 方法B：知道工作目录（从实验目录路径）
WORK_DIR="/data/math-agent-glm5.2-tmux-agents-dir/<experiment-id>"

# 方法C：列出最近的session
sqlite3 ~/.local/share/devin/cli/sessions.db "SELECT id, title, working_directory, created_at FROM sessions ORDER BY created_at DESC LIMIT 10;"
```

### 步骤2：确认有trajectory数据

```bash
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id ${SESSION_ID} --summary
```

**检查**：
- `Total steps` > 0（有数据）
- `Assistant steps` > 0（有AI工作记录）
- `with thinking` > 0（有thinking数据）
- `Tool usage` 显示了工具调用分布

### 步骤3：导出trajectory

```bash
# JSONL格式（推荐用于检索系统和程序化分析）
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id ${SESSION_ID} -o runs/<run_id>/trajectory.jsonl

# Markdown格式（可读，用于人工分析）
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id ${SESSION_ID} --format markdown -o runs/<run_id>/trajectory.md

# JSON格式（完整数据，用于程序化分析）
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id ${SESSION_ID} --format json -o runs/<run_id>/trajectory.json
```

### 步骤4：增量更新（session还在跑时）

```bash
# 第一次提取
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id ${SESSION_ID} -o trajectory.jsonl

# 后续增量更新（只追加新steps，不重复session_meta）
.venv/bin/python3 xishujuzhen/trajectory_extractor.py --session-id ${SESSION_ID} --incremental -o trajectory.jsonl
```

**增量更新机制**：
- SDK读取已有JSONL的最后一个node_id
- 只提取node_id更大的新steps
- 追加到JSONL文件末尾（不重复session_meta行）

### 步骤5：分析trajectory

读trajectory.md或trajectory.jsonl，关注以下维度：

**AI的完整工作过程**：
1. **问题理解阶段**：AI如何理解题目？识别了什么数学结构？
2. **方法选择阶段**：AI选择什么方法？为什么？
3. **执行阶段**：AI执行了什么计算？工具返回了什么？
4. **验证阶段**：AI如何验证结果？是否尝试封闭形式识别？
5. **卡点阶段**：AI在哪里停下来？thinking中说了什么？

**工具使用模式**：
- exec调用次数和内容（Python计算了什么？）
- get_output调用（等待长时间计算）
- kill_shell调用（放弃了什么计算？）
- web_search调用（搜索了什么？是否违规？）

**thinking与tool_results的交叉分析**：
- AI的thinking中说了"接下来要做什么"→ 下一个tool_call是否执行了？
- tool_result返回了什么→ AI的下一个thinking如何反应？
- AI是否因为tool_result而改变方向？

## Trajectory JSONL Schema

```
第一行：session_meta
{
  "type": "session_meta",
  "session_id": "...",
  "title": "...",
  "working_directory": "...",
  "model": "...",
  "created_at": 1786165442,
  "last_activity_at": 1786167094,
  "main_chain_id": 134,
  "stats": {
    "total_steps": 115,
    "assistant_steps": 73,
    "tool_steps": 36,
    "user_steps": 6,
    "has_thinking": 46,
    "total_thinking_chars": 290338,
    "total_tool_calls": 72,
    "tool_names": {"exec": 46, "get_output": 20, ...}
  }
}

后续每行：step
{
  "type": "step",
  "step_index": 0,
  "node_id": 2,
  "parent_node_id": 1,
  "role": "user",  // user/assistant/tool
  "created_at": 1786165442,
  "content": "...",
  "thinking": "...",  // 仅assistant有
  "tool_calls": [    // 仅assistant有
    {
      "id": "chatcmpl-tool-xxx",
      "name": "exec",
      "kind": "execute",
      "title": "Ran command",
      "arguments": {...},
      "raw_input": {...}
    }
  ],
  "tool_results": [  // 仅当tool_calls非空时
    {
      "tool_call_id": "chatcmpl-tool-xxx",
      "status": "completed",
      "output": "...",
      "meta": {...}
    }
  ]
}
```

## 注意事项

1. **Node去重**：sessions.db中每个assistant node出现两次（devin cli渲染机制），SDK自动去重
2. **thinking是英文的**：GLM-5.2的thinking用英文，content用中文
3. **tool_results有截断**：SDK截断长tool结果到10000字符
4. **session可以还在跑**：增量更新模式支持session运行中持续提取
5. **JSONL是流式格式**：每行一个JSON对象，适合增量追加和流式处理

## 与检索系统的关系

trajectory是检索系统工作的基础数据：
- 检索系统索引trajectory中的thinking和tool_results
- 当AI遇到新问题时，检索系统从历史trajectory中找相似的推理模式
- trajectory的树结构（parent_node_id）保留了AI的推理路径——不只是线性序列

## 与solver-tmux-launch元组的关系

```
solver-tmux-launch启动Solver → Solver做题产生trajectory数据
    ↓
    ├─ sessions.db（事后完整提取）→ trajectory_extractor.py → JSONL
    └─ MITM（实时截获）→ decode-all → trajectory.jsonl（token级thinking）
    ↓
检索系统索引trajectory → 当AI遇到新问题时检索相似推理模式
    ↓
thinking-extraction（子集）→ 分析AI为什么做不出（关注thinking）
```

## MITM流式实时thinking截获（2026-08-08建立）

solver-harness通过mitmproxy截获devin cli的API响应，实现**token级实时**thinking采集——Solver思考过程中每个token立即落盘。

### 核心机制：responseheaders + stream callable

```
devin cli → HTTPS_PROXY=localhost:18889 → mitmproxy → server.self-serve.windsurf.com
    ↓
responseheaders hook（响应头到达时，body之前）
    ↓ 设置 flow.response.stream = parser.feed
    ↓
每个HTTP chunk到达时 → parser.feed(chunk) 被调用
    ↓ StreamingThinkingParser实时解析Connect streaming protobuf
    ↓ 每解析出一个field 9（thinking chunk）立即写入3个位置：
    ├─ _shared/mitm_raw/thinking_live.txt（全局，可tail -f）
    ├─ <exp_id>/mitm/thinking_live.txt（按实验，可tail -f）
    └─ <exp_id>/mitm/thinking_live.jsonl（JSONL，每个chunk一行）
    ↓
流结束时 → parser.feed(b"") 被调用 → 写stream_complete汇总记录
```

### 关键修复：NODE_EXTRA_CA_CERTS

devin cli是Node.js应用，不读macOS Keychain。必须设置`NODE_EXTRA_CA_CERTS=~/.mitmproxy/mitmproxy-ca-cert.pem`环境变量，否则交互模式SSL验证失败。solver-harness已内置此修复（见solver-tmux-launch元组）。

### 实时查看

```bash
# 实时查看所有实验的thinking流
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/thinking_live.txt

# 实时查看特定实验
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/mitm/thinking_live.txt

# 程序化读取
cat /data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/mitm/thinking_live.jsonl
```

### JSONL记录类型

- `thinking_chunk`：单个thinking token（含timestamp/counter/chunk_index/content）
- `tool_call_chunk`：单个tool_call chunk（含tool_call_id/name/args_chunk/is_start）
- `stream_complete`：一轮thinking完成后的汇总（含thinking_full完整文本/tool_calls列表/elapsed_seconds）

### 事后解码

```bash
# 实时解码单个bin文件（事后分析）
python3 xishujuzhen/mitm_thinking_intercept/decode_connect_proto.py <file.bin> --stream

# 批量解码所有raw数据（按work_dir分发到各实验）
python3 xishujuzhen/solver_harness/solver_harness.py decode-all
```

### 验证结果（2026-08-08）

- 120秒内11,397行txt + 10,971行jsonl
- chunk粒度1-7字符/token（如`+T`、`+(k`、`+approx`）
- 毫秒级时间戳（04:22:13.250 → 04:22:13.447）
- 第二轮thinking：12,865个chunks在2分钟内实时落盘
- mitmproxy截获的thinking与sessions.db完全一致——两个数据源互补
