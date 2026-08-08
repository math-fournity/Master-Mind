# 262 · Devin CLI Trajectory数据源调查 + MITM Thinking拦截验证

**日期**：2026-08-08
**状态**：调查完成，已验证
**关联**：179号三层trajectory记录方案、solver-tmux-launch元组、trajectory-extraction元组

---

## 一、调查动机

用户观察到AI有时"卡在thinking中"不产出任何输出。需要搞清楚：

1. AI的thinking数据**是否实时落盘**？还是累积在内存中等step完成后才写入？
2. 如果是后者，能否在thinking过程中**实时拦截**thinking数据？
3. "卡在thinking"的**根因**是什么？

---

## 二、调查结论总览

| 问题 | 结论 | 证据 |
|---|---|---|
| thinking是否实时落盘？ | **否**。thinking在云端API服务器生成，devin cli等完整HTTP响应后才写入sessions.db | 监控实验：60秒内max_node在18秒不变（AI thinking中）→ 跳变（thinking完成写入） |
| 能否实时拦截thinking？ | **能**。通过MITM代理拦截HTTPS通信，解码Connect streaming protobuf | 成功拦截矩条件极差题测试的第一个inference响应，提取出token级thinking |
| "卡在thinking"根因 | **AI hit max output token limit**。thinking把output token额度用完，导致没有content/tool_call输出 | tmux输出：`warning: response truncated (model hit max output token limit)`；59,263字符thinking但0 content 0 tool_calls |

---

## 三、Devin CLI通信架构（调查确认）

```
用户 → devin cli (REPL, ACP client)
         ↓ spawn子进程 (stdio JSON-RPC)
       devin acp (ACP server)
         ↓ HTTPS (Connect协议 + protobuf)
       server.self-serve.windsurf.com/exa.api_server_pb.ApiServerService/GetChatMessage
         ↓ (LLM推理在云端发生)
       流式protobuf响应（逐token返回thinking/content/tool_call chunks）
         ↓
       devin acp接收流式chunks，通过stdio转发给devin cli
         ↓
       devin cli在内存中累积，等完整response后写入sessions.db
```

### 关键发现

1. **thinking是流式传输到本地的**——从devin二进制strings中确认了`LoadedThinkingTokenContent`、`TokenContentComplete`、`ContentChunk`、`cognition.ai/partialContent`、`cognition.ai/streamingMessageId`等流式协议字段
2. **devin cli在内存中累积流式tokens**，等完整response后才写入sessions.db——所以sessions.db只有step级数据，没有token级流式数据
3. **流式数据经过了本地进程**，只是没有被落盘——这是MITM拦截的基础

---

## 四、sessions.db Schema（完整映射）

### 4.1 关键表

| 表 | 用途 | 关键字段 |
|---|---|---|
| `sessions` | session元信息 | id, title, working_directory, created_at, last_activity_at |
| `message_nodes` | 消息树（parent_node_id形成树结构） | node_id, session_id, parent_node_id, chat_message (JSON), created_at |
| `tool_call_state` | 工具调用的输入和输出 | tool_call_id, session_id, tool_call_json (含rawInput), tool_call_update_json (含content/output) |

### 4.2 chat_message JSON结构

```json
{
  "role": "assistant|user|tool|system",
  "content": "AI输出的文本内容",
  "thinking": {
    "thinking": "AI的完整thinking文本（不是reasoning_content）"
  },
  "tool_calls": [
    {
      "id": "tool_call_id",
      "name": "工具名",
      "arguments": "工具参数JSON"
    }
  ],
  "tool_call_id": "如果是tool角色消息，对应的tool_call_id",
  "reasoning_content": "（存在但不是thinking，是另一种reasoning）"
}
```

**关键**：thinking在`thinking.thinking`字段，**不是**`reasoning_content`。assistant nodes会出现两次（重复），提取时需去重。

---

## 五、MITM代理拦截方案（验证成功）

### 5.1 技术发现链

| 发现 | 验证方法 |
|---|---|
| devin cli支持`HTTPS_PROXY`环境变量 | `strings $(which devin) \| grep HTTP_PROXY` → 找到reqwest库的proxy支持 |
| devin cli用`rustls-platform-verifier`验证TLS | `strings` → 找到`rustls_platform_verifier::verification::apple`；日志报`failed to verify TLS certificate: invalid peer certificate: UnknownIssuer` |
| 需要把mitmproxy CA加入macOS Keychain信任 | `security add-trusted-cert -d -r trustRoot -k ~/Library/Keychains/login.keychain-db ~/.mitmproxy/mitmproxy-ca-cert.pem` |
| GetChatMessage用Connect协议+protobuf | 响应content-type: `application/connect+proto` |
| Connect streaming格式 | 每个envelope: 1 byte flags + 4 bytes length (big-endian) + protobuf message；flags bit 1 (0x02) = end-of-stream |

### 5.2 Protobuf字段映射（逆向推断）

通过`strings $(which devin)`分析二进制中的proto字段名 + `protoc --decode_raw`解码raw bytes推断：

| field | 类型 | 含义 | 流式特点 |
|---|---|---|---|
| 1 | string | message_id | 每个envelope都有 |
| 2 | message | timestamp (sub-field 1=seconds, sub-field 2=nanos) | 每个envelope都有 |
| 5 | varint | stop_reason | 仅最后一个envelope |
| 6 | message | tool_call chunk | sub-field 1=tool_call_id（仅首个chunk）, sub-field 2=tool_name（仅首个chunk）, sub-field 3=arguments chunk（逐token流式） |
| 7 | message | metadata (sub-field 9=model name) | 每个envelope都有 |
| 9 | string | content/thinking chunk | **逐token流式**——这是thinking/content文本 |
| 12 | 64bit | sequence number | 每个envelope都有 |
| 17 | string | session_id | 每个envelope都有 |
| 28 | message | statistics (token usage) | 仅最后一个envelope |

### 5.3 验证结果

用矩条件极差题第2问测试，成功拦截到第一个GetChatMessage响应（5808 bytes, 43个streaming messages）：

- **Thinking content**（8个token chunks拼接）: "Let me read the problem file first."
- **Tool call**: `read({"file_path": "/data/math-agent-glm5.2-tmux-agents-dir/258-mitm-matrix-test/problem.txt"})`
- **Model**: GLM-5.2 High
- **Token usage**: input_tokens + output_tokens + cached_input_tokens

### 5.4 注意事项

1. **CA证书信任是全局的**：加入Keychain后，所有走mitmproxy的HTTPS都会被信任。测试结束后建议移除
2. **代理影响所有流量**：devin cli的所有HTTPS请求都走代理（包括telemetry、analytics等），产生噪声
3. **protobuf schema是逆向推断的**：字段映射可能有误差。如需精确解析，需要正式的`.proto`文件
4. **Connect streaming vs unary**：GetChatMessage是streaming RPC（多个envelope），其他RPC（如GetUserStatus）可能是unary（单个envelope）

---

## 六、已形成的代码和工具

### 6.1 trajectory提取工具（基于sessions.db，step级）

| 文件 | 用途 | 粒度 |
|---|---|---|
| `xishujuzhen/trajectory_extractor.py` | 完整trajectory提取（post-analysis） | step级 |
| `xishujuzhen/trajectory_monitor.py` | 实时监控sessions.db，新step出现时提取 | step级（~3s延迟） |
| `xishujuzhen/thinking_extractor.py` | 简化版thinking提取 | step级 |

### 6.2 MITM thinking拦截工具（基于MITM代理，token级）

| 文件 | 用途 | 粒度 |
|---|---|---|
| `xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py` | mitmproxy addon，捕获GetChatMessage raw bytes | token级（~0ms延迟） |
| `xishujuzhen/mitm_thinking_intercept/decode_connect_proto.py` | 解码Connect streaming protobuf | token级 |
| `xishujuzhen/mitm_thinking_intercept/sample_capture/` | 样本捕获数据 | — |
| `xishujuzhen/mitm_thinking_intercept/README.md` | MITM方案完整文档 | — |

### 6.3 对应的元组（rule + skill）

| 元组 | rule | skill |
|---|---|---|
| trajectory-extraction | `.devin/rules/trajectory-extraction.md` | `.devin/skills/trajectory-extraction/SKILL.md` |
| thinking-extraction | `.devin/rules/thinking-extraction.md` | `.devin/skills/thinking-extraction/SKILL.md` |
| solver-tmux-launch | `.devin/rules/solver-tmux-launch.md` | `.devin/skills/solver-tmux-launch/SKILL.md` |

---

## 七、"卡在thinking"现象详解

### 7.1 测试案例

矩条件极差题第(2)问：
> 证明存在常数 C2 > 0 使得 max{a_1,...,a_n} - min{a_1,...,a_n} >= sqrt(5) + C2 * n^(-3/2)

### 7.2 失败模式

- AI读了题目后thinking了**59,263字符**
- 然后**hit max output token limit**
- tmux输出：`warning: response truncated (model hit max output token limit)`
- AI**没有输出任何content，没有调用任何工具，直接停止**
- thinking结尾在分析`sum (b_i - m)(b_i - M)^2 > 0`的界时被截断

### 7.3 根因

AI想得太多，thinking把output token额度全部用完，导致没有任何content输出。这验证了用户的预测：AI会卡死在thinking环节。

---

## 八、粒度对比

| 方案 | 粒度 | 延迟 | 实现复杂度 | 风险 |
|---|---|---|---|---|
| `trajectory_monitor.py`（轮询sessions.db） | step级 | ~3s（每步完成后） | 低 | 无 |
| **MITM代理** | **token级** | **~0ms（实时）** | 中 | 需信任CA证书 |
| ACP wrapper（替换devin二进制） | token级 | ~0ms | 高 | 替换全局安装 |
| lldb内存dump | token级 | ~0ms | 高 | 需禁SIP，fragile |

---

## 九、下一步：solver-harness系统

本调查确认了技术可行性。下一步是搭建**solver-harness**——一个完整的trajectory采集环境，在tmux中启动devin cli并自动采集所有数据。方案见263号文档。

---

## 十、流式实时thinking落盘验证（2026-08-08更新）

### 10.1 从"响应完成后解码"到"token级流式实时"

初始方案用mitmproxy的`response` hook在HTTP响应完成后解码thinking——这不是真正的实时，因为要等整个响应体到达。

**改进方案**：用mitmproxy的`responseheaders` hook + `flow.response.stream = callable`：
- `responseheaders`在响应头到达时触发（body之前）
- 设置`flow.response.stream = parser.feed`后，每个HTTP chunk到达时callable被调用
- `StreamingThinkingParser`实时解析Connect streaming protobuf
- 每解析出一个field 9（thinking chunk）立即落盘——**不需要等响应完成**

### 10.2 三路落盘

| 位置 | 格式 | 用途 |
|---|---|---|
| `_shared/mitm_raw/thinking_live.txt` | 人类可读 | `tail -f`实时查看所有实验 |
| `<exp_id>/mitm/thinking_live.txt` | 人类可读 | `tail -f`按实验查看 |
| `<exp_id>/mitm/thinking_live.jsonl` | JSONL | 每个chunk一行，程序读取 |

### 10.3 JSONL记录类型

- `thinking_chunk`：单个thinking token（含timestamp/counter/chunk_index/content）
- `tool_call_chunk`：单个tool_call chunk（含tool_call_id/name/args_chunk/is_start）
- `stream_complete`：一轮thinking完成后的汇总（含thinking_full完整文本/tool_calls列表/elapsed_seconds）

### 10.4 端到端验证数据

- **5秒时**：thinking_live.txt已有227行——实时落盘启动
- **每5秒持续增长**：+227 → +497 → +307 → +604...
- **120秒时**：11,397行txt + 10,971行jsonl
- **chunk粒度**：1-7字符/token（如`+T`、`+(k`、`+approx`）
- **时间戳精度**：毫秒级（04:22:13.250 → 04:22:13.447）
- **第二轮thinking**：12,865个chunks在2分钟内实时落盘

### 10.5 db monitor启动顺序修复

同时修复了db monitor的启动顺序问题：
- **原问题**：db monitor在devin cli启动前就启动了，`trajectory_monitor.py`找不到session就`sys.exit(1)`退出
- **修复**：将`start_db_monitor`从步骤6移到步骤9（在`backfill_devin_session_id`之后）
- **效果**：db monitor现在能正确找到session，3秒轮询step级trajectory实时落盘到`sessions_db/trajectory.jsonl`

### 10.6 粒度对比（更新）

| 方案 | 粒度 | 延迟 | 实现复杂度 | 风险 | 状态 |
|---|---|---|---|---|---|
| **MITM流式（responseheaders+stream）** | **token级** | **~0ms（实时）** | 中 | 需信任CA证书+NODE_EXTRA_CA_CERTS | ✅已验证 |
| MITM响应完成后解码（response hook） | step级 | 响应完成后 | 低 | 同上 | ✅已弃用 |
| `trajectory_monitor.py`（轮询sessions.db） | step级 | ~3s | 低 | 无 | ✅已修复 |
| ACP wrapper（替换devin二进制） | token级 | ~0ms | 高 | 替换全局安装 | 未实现 |
| lldb内存dump | token级 | ~0ms | 高 | 需禁SIP | 未实现 |
