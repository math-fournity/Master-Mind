---
description: >
  分析AI解题过程时，必须用thinking_extractor.py从sessions.db提取完整thinking数据，
  或用mitmproxy实时截获thinking（通过decode_connect_proto.py解码）。
  thinking数据在chat_message JSON的thinking.thinking字段中（不是reasoning_content），
  或在mitmproxy截获的protobuf field 9中。
  包含AI的完整推理链：尝试了什么、为什么失败、下一步打算做什么。
  WHEN to use: 需要分析AI为什么做不出某道题、需要理解AI的推理过程、需要提取挑战类型时、需要实时监控AI thinking时。
  WHEN NOT to use: 只需要AI的最终答案而不关心过程。
trigger: model_decision
---

# thinking-extraction rule

## 硬约束

**分析AI解题过程时，必须使用 `xishujuzhen/thinking_extractor.py` 提取完整thinking数据。**

**需要实时监控AI thinking时，使用mitmproxy截获+`decode_connect_proto.py`解码。**

不能只看AI的content（输出给用户的内容）——content只是thinking的摘要。thinking才是AI的真实推理过程。

## 两种获取方式

| 方式 | 工具 | 实时性 | 数据完整性 | 适用场景 |
|---|---|---|---|---|
| **MITM流式实时截获** | `mitmproxy` responseheaders+stream callable | **token级实时**（思考过程中每个token立即落盘） | token级thinking + tool_calls（无tool_results） | 实时监控、流式分析、RealtimePipeline |
| **sessions.db提取** | `thinking_extractor.py` | session结束后 | thinking + content + tool_calls + tool_results | 事后分析、挑战类型分析 |

**MITM流式实时截获**是核心机制：mitmproxy的`responseheaders` hook在响应头到达时设置`flow.response.stream = callable`，每个HTTP chunk到达时callable被调用，实时解析Connect streaming protobuf，每解析出一个thinking chunk（field 9）立即写入4个位置：
1. `_shared/mitm_raw/thinking_live.txt`（token级碎片，可`tail -f`实时查看）
2. `<exp_id>/mitm/thinking_live.txt`（按实验隔离，token级碎片，可`tail -f`）
3. `<exp_id>/mitm/thinking_live.jsonl`（JSONL格式，每个chunk一行）
4. `<exp_id>/mitm/thinking_readable.txt`（**人可阅读的连续文本**——thinking实时拼接追加，tool_call用分隔符标记，可`tail -f`读文章）

两种方式获取的thinking内容完全一致（已验证2026-08-08）。MITM方式在Solver思考过程中实时落盘（不需要等响应完成）；sessions.db方式在session结束后提供完整数据。

## 原因

1. **thinking是AI的真实推理**：GLM-5.2的thinking字段包含AI的完整推理链（英文，平均6000+字符/步），content只是输出给用户的摘要（中文，平均50字符/步）
2. **reasoning_content是空的**：sessions.db中`reasoning_content`字段为空，thinking数据在`thinking.thinking`字段中——用错字段会拿到空数据
3. **失败分析需要thinking**：AI做不出题时，thinking中记录了"尝试了什么、为什么失败、下一步打算做什么"——这是挑战类型分析的核心数据
4. **tool_calls+tool_results是证据**：AI调用了什么工具（如Python计算）和工具返回了什么结果，是判断AI卡在哪里的关键证据

## 实施规范

### 提取thinking数据

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
- `thinking`: AI的完整推理过程（英文，可能为空）
- `tool_calls`: AI调用的工具列表
- `tool_results`: 工具返回的结果

### 分析流程

1. 用`--summary`确认session有thinking数据（`has_thinking > 0`）
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

## 与solver-tmux-launch元组的关系

solver-tmux-launch元组负责启动Solver的devin cli实例并记录trajectory（tmux pipe-pane + --export）。
thinking-extraction元组负责从sessions.db提取trajectory中的thinking数据进行分析。

两个元组的关系：
- solver-tmux-launch：**生成**数据（启动session，产生thinking数据）
- thinking-extraction：**提取分析**数据（从sessions.db提取thinking，分析AI推理过程）

## 数据位置速查

| 数据 | 位置 | 字段 |
|---|---|---|
| thinking（sessions.db） | sessions.db → message_nodes → chat_message JSON | `thinking.thinking` |
| thinking（MITM实时） | `_shared/mitm_raw/chatmsg_NNN_*.bin` → decode后 | protobuf field 9（content_thinking） |
| content | sessions.db → message_nodes → chat_message JSON | `content` |
| tool_calls | sessions.db → message_nodes → chat_message JSON | `tool_calls` |
| tool_calls（MITM实时） | `_shared/mitm_raw/chatmsg_NNN_*.bin` → decode后 | protobuf field 6 |
| tool_results | sessions.db → tool_call_state | `tool_call_update_json` |
| session元信息 | sessions.db → sessions | `id, title, working_directory, model, created_at` |
| --export JSON | 运行时指定路径 | `steps[].reasoning_content`（导出时映射了thinking→reasoning_content） |
| API调用日志 | `_shared/mitm_raw/api_log.txt` | URL/状态/大小/时间 |
| flow文件 | `_shared/mitm_flows.mitm` | 可用`mitmdump -r`回放 |
