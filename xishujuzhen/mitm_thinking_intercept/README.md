# MITM Thinking Intercept — Token级实时Thinking拦截

## 成果

通过MITM代理拦截Devin CLI的HTTPS通信，实现了**token级实时thinking拦截**——比之前`trajectory_monitor.py`的step级实时（每步完成后才能拿到）高一个粒度。

## 原理

### Devin CLI通信架构

```
用户 → devin cli (REPL)
         ↓ spawn子进程 (stdio JSON-RPC)
       devin acp (ACP server)
         ↓ HTTPS (Connect协议 + protobuf)
       server.self-serve.windsurf.com/exa.api_server_pb.ApiServerService/GetChatMessage
         ↓ (LLM推理在云端)
       流式protobuf响应（逐token返回thinking/content/tool_call chunks）
         ↓
       devin acp接收流式chunks，通过stdio转发给devin cli
         ↓
       devin cli在内存中累积，等完整后写入sessions.db
```

### MITM拦截点

在`devin acp`和云端API之间插入mitmproxy：

```
devin acp → HTTPS_PROXY → mitmproxy → 云端API
                              ↓
                         拦截GetChatMessage响应
                              ↓
                         解码Connect streaming protobuf
                              ↓
                         实时提取thinking/content/tool_call chunks
```

### 关键技术点

1. **devin cli支持代理**：尊重`HTTPS_PROXY`/`HTTP_PROXY`环境变量（用reqwest库）
2. **TLS证书信任**：devin cli用`rustls-platform-verifier`，通过macOS Keychain验证证书。需要将mitmproxy CA加入Keychain信任：
   ```bash
   security add-trusted-cert -d -r trustRoot -k ~/Library/Keychains/login.keychain-db ~/.mitmproxy/mitmproxy-ca-cert.pem
   ```
3. **Connect streaming protobuf**：GetChatMessage响应是`application/connect+proto`格式
   - 每个envelope: 1 byte flags + 4 bytes length (big-endian) + protobuf message
   - flags bit 1 (0x02) = end-of-stream
4. **Protobuf字段映射**（通过strings分析devin二进制+decode_raw推断）：
   - field 1: message_id (string)
   - field 2: timestamp (message: sub-field 1 = seconds, sub-field 2 = nanos)
   - field 5: stop_reason (varint)
   - field 6: tool_call chunk (message)
     - sub-field 1: tool_call_id（仅首个chunk出现）
     - sub-field 2: tool_name（仅首个chunk出现）
     - sub-field 3: arguments chunk（逐token流式）
   - field 7: metadata (message: sub-field 9 = model name)
   - field 9: content/thinking chunk (string) — 逐token流式
   - field 12: sequence number (64bit)
   - field 17: session_id (string)
   - field 28: statistics (token usage等)

## 使用方法

### 1. 启动mitmproxy

```bash
# 确保mitmproxy CA证书已加入Keychain（只需一次）
security add-trusted-cert -d -r trustRoot -k ~/Library/Keychains/login.keychain-db ~/.mitmproxy/mitmproxy-ca-cert.pem

# 启动mitmdump，用proto capture addon
mitmdump --listen-port 18888 -s xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py --set ssl_insecure=true
```

### 2. 启动devin cli走代理

```bash
HTTPS_PROXY=http://localhost:18888 HTTP_PROXY=http://localhost:18888 \
  devin -p "你的prompt" --model glm-5-2 --respect-workspace-trust false --permission-mode dangerous
```

### 3. 解码捕获的数据

```bash
# 解码单个文件
python3 xishujuzhen/mitm_thinking_intercept/decode_connect_proto.py /tmp/devin_mitm_raw/chatmsg_001_*.bin --stream

# 解码目录下所有捕获文件
python3 xishujuzhen/mitm_thinking_intercept/decode_connect_proto.py /tmp/devin_mitm_raw/ --stream
```

## 文件清单

| 文件 | 用途 |
|---|---|
| `mitm_proto_capture.py` | mitmproxy addon，捕获GetChatMessage的raw protobuf响应 |
| `decode_connect_proto.py` | 解码Connect streaming protobuf，提取流式thinking/content/tool_call |
| `sample_capture/` | 样本捕获数据（矩条件极差题测试的第一个inference响应） |

## 验证结果

用矩条件极差题第2问测试，成功拦截到第一个GetChatMessage响应（5808 bytes，43个streaming messages）：

- **Thinking content**（8个token chunks拼接）: "Let me read the problem file first."
- **Tool call**: `read({"file_path": "/data/grove-agents-dir/258-mitm-matrix-test/problem.txt"})`
- **Model**: GLM-5.2 High
- **Token usage**: input_tokens + output_tokens + cached_input_tokens

## 与其他方案对比

| 方案 | 粒度 | 延迟 | 实现复杂度 | 风险 |
|---|---|---|---|---|
| `trajectory_monitor.py`（轮询sessions.db） | step级 | ~3s（每步完成后） | 低 | 无 |
| **MITM代理（本方案）** | **token级** | **~0ms（实时）** | 中 | 需信任CA证书 |
| ACP wrapper（替换devin二进制） | token级 | ~0ms | 高 | 替换全局安装 |

## 注意事项

1. **CA证书信任是全局的**：加入Keychain后，所有走mitmproxy的HTTPS都会被信任。测试结束后建议移除：
   ```bash
   security delete-certificate -c "mitmproxy" ~/Library/Keychains/login.keychain-db
   ```
2. **代理影响所有流量**：devin cli的所有HTTPS请求都走代理（包括telemetry、analytics等），可能产生大量噪声
3. **protobuf schema是逆向推断的**：字段映射通过strings分析+decode_raw推断，可能有误差。如需精确解析，需要获取正式的`.proto`文件
4. **Connect streaming vs unary**：GetChatMessage是streaming RPC（多个envelope），其他RPC（如GetUserStatus）可能是unary（单个envelope）
