# mitmproxy采集接口

**前置阅读**：07-工程规格/01-系统架构总图.md
**来源**：262号、263号、266号修复更新

---

## 1. thinking流式采集架构

mitmproxy作为macOS launchd系统服务运行：
- **服务Label**：com.aurolafly.mitmproxy-devin
- **端口**：18889（18888被claude-passthrough占用）
- **addon脚本**：~/.mitmproxy/mitm_proto_capture.py（共享位置）
- **开机自启动**：RunAtLoad=true
- **崩溃自动重启**：KeepAlive.SuccessfulExit=false

## 2. responseheaders + stream callable机制

```python
# mitmproxy addon核心逻辑
def responseheaders(flow):
    """响应头到达时触发（body之前）"""
    if "GetChatMessage" in flow.request.path:
        # 设置stream callable，每个HTTP chunk到达时被调用
        flow.response.stream = parser.feed

class StreamingThinkingParser:
    def feed(self, chunk):
        """每个HTTP chunk到达时调用，实时解析Connect streaming protobuf"""
        # 1 byte flags + 4 bytes length + protobuf message
        # 每解析出field 9（thinking chunk）立即落盘
        for envelope in parse_envelopes(chunk):
            if has_field(envelope, 9):
                thinking_text = extract_field(envelope, 9)
                write_to_disk(thinking_text)
```

## 3. 四路落盘

| 位置 | 格式 | 用途 |
|---|---|---|
| _shared/mitm_raw/thinking_live.txt | token级碎片 | tail -f实时查看所有实验 |
| <exp_id>/mitm/thinking_live.txt | token级碎片 | tail -f按实验查看 |
| <exp_id>/mitm/thinking_live.jsonl | JSONL | 每个chunk一行，程序读取 |
| <exp_id>/mitm/thinking_readable.txt | 人可阅读连续文本 | tail -f读文章 |

## 4. JSONL记录类型

```json
// thinking_chunk：单个thinking token
{"type": "thinking_chunk", "timestamp": 1799697600.250, "counter": 1, "chunk_index": 0, "content": "Let me"}

// tool_call_chunk：单个tool_call chunk
{"type": "tool_call_chunk", "tool_call_id": "xxx", "name": "read", "args_chunk": "{\"file_path\":", "is_start": true}

// stream_complete：一轮thinking完成后的汇总
{"type": "stream_complete", "thinking_full": "完整thinking文本", "tool_calls": [...], "elapsed_seconds": 95.3}
```

## 5. protobuf字段映射

| field | 类型 | 含义 | 流式特点 |
|---|---|---|---|
| 1 | string | message_id | 每个envelope都有 |
| 6 | message | tool_call chunk | 逐token流式 |
| 9 | string | thinking chunk | **逐token流式** |
| 17 | string | session_id | 每个envelope都有 |
| 28 | message | statistics (token usage) | 仅最后一个envelope |

## 6. mitmproxy启动命令

```bash
mitmdump --listen-port 18889 \
  --no-http2 \
  --allow-hosts "server\.self-serve\.windsurf\.com|api\.devin\.ai|static\.devin\.ai" \
  -s mitm_proto_capture.py \
  --set ssl_insecure=true
```

- `--no-http2`：禁用HTTP/2，解决连接复用问题（266号修复）
- `--allow-hosts`：只拦截3个devin相关host
- `ssl_insecure=true`：允许SSL拦截

## 7. solver-harness集成

所有场景通过solver-harness启动devin cli，自动设置HTTPS_PROXY环境变量指向mitmproxy：

```bash
HTTPS_PROXY=http://127.0.0.1:18889 \
NODE_EXTRA_CA_CERTS=~/.mitmproxy/mitmproxy-ca-cert.pem \
devin --model glm-5-2 --export <path> -- 'prompt'
```
