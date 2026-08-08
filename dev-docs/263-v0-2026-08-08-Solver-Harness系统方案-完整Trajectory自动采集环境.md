# 263 · Solver-Harness系统方案 · 完整Trajectory自动采集环境

**日期**：2026-08-08
**状态**：方案设计（待实施）
**关联**：262号调查结果、179号三层trajectory记录方案、solver-tmux-launch元组
**前置条件**：262号调查已确认MITM代理方案技术可行

---

## 一、目标

搭建一个**完整的trajectory采集环境**，用于在tmux中启动devin cli，并自动采集AI工作过程中的所有数据：

1. **token级流式thinking**（MITM代理拦截，~0ms延迟）
2. **step级trajectory**（sessions.db轮询，~3s延迟，作为MITM的补充和兜底）
3. **tmux pipe-pane兜底记录**（终端输出全文）
4. **devin --export导出**（官方导出的conversation.json）
5. **session元信息**（run_id、model、时间戳、状态等）

**关键约束**：AI不能看到自己的运行数据——这会污染Solver的行为。数据必须放在Solver工作目录之外。

---

## 二、核心设计决策

### 2.1 目录分离（用户明确要求）

```
Solver工作目录（AI可见，AI在这里做题）:
  /data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/
  ├── AGENTS.md          (Solver角色定义)
  ├── problem.txt        (题目)
  ├── proof*.md          (AI写的证明草稿)
  └── .venv/             (AI的Python环境，可选)

Trajectory数据目录（AI不可见，harness在这里存数据）:
  /data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/
  ├── session_info.json     (run元信息)
  ├── mitm/
  │   ├── raw/              (MITM捕获的raw protobuf)
  │   │   ├── chatmsg_001_*.bin
  │   │   └── chatmsg_002_*.bin
  │   ├── capture.log       (MITM捕获日志)
  │   ├── mitm_stderr.log   (mitmdump的stderr)
  │   ├── trajectory.jsonl  (解码后的token级流式数据)
  │   └── _decoder_daemon.py (解码daemon脚本)
  ├── sessions_db/
  │   └── trajectory.jsonl  (从sessions.db提取的step级数据)
  ├── tmux/
  │   ├── tmux_pipe.log     (pipe-pane兜底记录)
  │   └── tmux.log          (tee记录)
  └── exports/
      └── conversation.json (devin --export导出)
```

**为什么分离**：
- AI在Solver工作目录中做题，如果看到trajectory数据会改变行为（比如看到自己之前的thinking会自我修正）
- trajectory数据是工程设施，不是AI的认知环境
- 同名子目录设计（`<exp-id>`）让两个目录一一对应，好查

### 2.2 MITM代理默认开启（用户明确选择）

每次启动Solver都自动起mitmproxy + 走代理，实现token级实时拦截。

**实现方式**：
- 每个实验启动独立的mitmproxy实例（在独立tmux session中）
- 端口分配：`18888 + hash(exp_id) % 100`，避免冲突
- 需要mitmproxy CA在Keychain中信任（全局，一次性配置）
- MITM失败时自动降级到只用sessions.db

### 2.3 三层数据采集（互为补充）

| 层 | 数据源 | 粒度 | 延迟 | 用途 |
|---|---|---|---|---|
| 1. MITM代理 | HTTPS流量拦截 | token级 | ~0ms | 实时thinking流、token usage统计 |
| 2. sessions.db轮询 | sessions.db | step级 | ~3s | 完整trajectory（含tool_results）、MITM兜底 |
| 3. tmux pipe-pane | 终端输出 | 行级 | ~0ms | 兜底记录、人类可读 |

**为什么三层都要**：
- MITM可能失败（CA未信任、端口冲突、protobuf解析错误）
- sessions.db轮询有~3s延迟，但数据最完整（含tool_results）
- tmux pipe-pane是最可靠的兜底，但只有终端可见内容

---

## 三、系统架构

### 3.1 组件图

```
solver-harness.py (主控脚本)
    │
    ├── cmd_launch: 启动一个实验
    │   ├── 创建Solver工作目录 + Trajectory数据目录
    │   ├── 复制AGENTS.md模板 + problem.txt
    │   ├── 写session_info.json
    │   ├── 启动mitmproxy (tmux: harness-mitm-<exp-id>)
    │   ├── 启动解码daemon (tmux: harness-decoder-<exp-id>)
    │   ├── 启动sessions.db轮询 (tmux: harness-dbmon-<exp-id>)
    │   ├── 启动devin cli (tmux: harness-<exp-id>, 走mitmproxy代理)
    │   └── 启动pipe-pane兜底
    │
    ├── cmd_status: 查看实验状态
    │   ├── session_info.json
    │   ├── tmux sessions状态
    │   └── 数据统计（各文件大小、条目数）
    │
    ├── cmd_stop: 停止实验
    │   └── 停止所有相关tmux sessions
    │
    ├── cmd_decode: 手动解码MITM raw数据
    │   └── 调用decode_connect_proto.py
    │
    └── cmd_list: 列出所有实验
        ├── Solver工作目录列表
        ├── Trajectory数据目录列表
        └── 运行中的tmux sessions
```

### 3.2 数据流

```
                    ┌─────────────────────────────────────────┐
                    │  cloud API (server.self-serve.windsurf)  │
                    └────────────┬────────────────────────────┘
                                 │ HTTPS (Connect+protobuf)
                                 ▼
                    ┌─────────────────────────────┐
                    │  mitmproxy (port 18xxx)      │
                    │  addon: mitm_proto_capture   │
                    └────────────┬────────────────┘
                                 │ raw .bin files
                                 ▼
                    ┌─────────────────────────────┐
                    │  mitm/raw/                   │
                    │  chatmsg_001_*.bin           │
                    └────────────┬────────────────┘
                                 │ decoder daemon (每2s轮询)
                                 ▼
                    ┌─────────────────────────────┐
                    │  mitm/trajectory.jsonl       │ (token级)
                    └─────────────────────────────┘

                    ┌─────────────────────────────┐
                    │  devin cli (走代理)          │
                    │  --export conversation.json  │
                    └────────────┬────────────────┘
                                 │
                    ┌────────────┼────────────────┐
                    │            │                │
                    ▼            ▼                ▼
              sessions.db    exports/         tmux pipe-pane
                    │            │                │
                    │            ▼                ▼
                    │    exports/           tmux/tmux_pipe.log
                    │    conversation.json  (兜底记录)
                    │
                    ▼
              sessions_db轮询 (每3s)
                    │
                    ▼
              sessions_db/trajectory.jsonl (step级)
```

### 3.3 tmux sessions

每个实验启动4个tmux sessions：

| tmux session | 用途 | 生命周期 |
|---|---|---|
| `harness-<exp-id>` | devin cli主进程 | 实验运行期间 |
| `harness-mitm-<exp-id>` | mitmproxy实例 | 实验运行期间 |
| `harness-decoder-<exp-id>` | 解码daemon（raw→jsonl） | 实验运行期间 |
| `harness-dbmon-<exp-id>` | sessions.db轮询 | 实验运行期间 |

---

## 四、组件设计

### 4.1 solver-harness.py（主控脚本）

**位置**：`xishujuzhen/solver_harness/solver_harness.py`

**命令**：
```bash
# 启动一个实验
python3 solver_harness.py launch \
  --exp-id 258-matrix-test \
  --problem-file problem.txt \
  --model glm-5-2

# 查看状态
python3 solver_harness.py status --exp-id 258-matrix-test

# 停止
python3 solver_harness.py stop --exp-id 258-matrix-test

# 手动解码MITM raw数据
python3 solver_harness.py decode --exp-id 258-matrix-test

# 列出所有实验
python3 solver_harness.py list
```

**已有初版代码**（`xishujuzhen/solver_harness/solver_harness.py`），需根据本方案完善。

### 4.2 MITM组件（复用已有）

| 组件 | 位置 | 状态 |
|---|---|---|
| mitmproxy addon | `xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py` | ✅ 已有 |
| protobuf解码器 | `xishujuzhen/mitm_thinking_intercept/decode_connect_proto.py` | ✅ 已有 |

### 4.3 sessions.db轮询组件（复用已有）

| 组件 | 位置 | 状态 |
|---|---|---|
| trajectory_monitor.py | `xishujuzhen/trajectory_monitor.py` | ✅ 已有 |

### 4.4 解码daemon（新增）

**职责**：每2秒扫描`mitm/raw/`目录，有新`.bin`文件时自动解码追加到`mitm/trajectory.jsonl`。

**实现方式**：solver-harness启动时动态生成daemon脚本到`mitm/_decoder_daemon.py`，在独立tmux session中运行。

---

## 五、数据格式

### 5.1 session_info.json

```json
{
  "exp_id": "258-matrix-test",
  "model": "glm-5-2",
  "prompt": "请读取当前目录下的problem.txt文件，解答其中的数学题。",
  "problem_file": "problem.txt",
  "solver_dir": "/data/math-agent-glm5.2-tmux-agents-dir/258-matrix-test",
  "trajectory_dir": "/data/math-agent-glm5.2-tmux-agents-trajectory/258-matrix-test",
  "tmux_session": "harness-258-matrix-test",
  "mitm_port": 18912,
  "mitm_enabled": true,
  "start_timestamp": "2026-08-08T02:15:00Z",
  "status": "running|stopped|completed"
}
```

### 5.2 mitm/trajectory.jsonl（token级，每行一个GetChatMessage响应）

```json
{
  "source_file": "chatmsg_001_020811_703943.bin",
  "decoded_at": 1799697600.0,
  "total_messages": 43,
  "content_thinking": "Let me read the problem file first.",
  "content_chunks_count": 8,
  "tool_calls": {
    "chatcmpl-tool-8a303136644d297a": {
      "name": "read",
      "args": "{\"file_path\": \"/data/.../problem.txt\"}"
    }
  }
}
```

### 5.3 sessions_db/trajectory.jsonl（step级，每行一个node）

```json
{
  "type": "step",
  "node_id": 23,
  "parent_node_id": 22,
  "role": "assistant",
  "content": "AI输出的文本",
  "thinking": "AI的完整thinking",
  "tool_calls": [...],
  "created_at": 1799697600
}
```

---

## 六、实施Check List

### 6.1 主控脚本完善

- [ ] 完善`solver_harness.py`的`cmd_launch`：目录创建 + 模板复制 + MITM启动 + 解码daemon + db轮询 + devin cli + pipe-pane
- [ ] 完善`cmd_status`：session_info + tmux状态 + 数据统计
- [ ] 完善`cmd_stop`：停止所有tmux sessions + 更新session_info
- [ ] 完善`cmd_decode`：调用decode_connect_proto.py
- [ ] 完善`cmd_list`：列出所有实验

### 6.2 解码daemon

- [ ] 实现动态生成daemon脚本的逻辑
- [ ] daemon每2秒扫描raw目录，新文件解码追加到jsonl
- [ ] daemon处理异常（解码失败时记录error到jsonl）

### 6.3 MITM端口管理

- [ ] 端口分配算法：`18888 + hash(exp_id) % 100`
- [ ] 端口冲突检测：启动前检查端口是否被占用
- [ ] MITM启动失败时的降级逻辑

### 6.4 测试

- [ ] 端到端测试：用简单题（如`n^2+2n+2`完全平方数）测试完整流程
- [ ] MITM数据验证：检查`mitm/trajectory.jsonl`是否有token级数据
- [ ] sessions.db数据验证：检查`sessions_db/trajectory.jsonl`是否有step级数据
- [ ] 兜底记录验证：检查`tmux/tmux_pipe.log`是否有终端输出

### 6.5 文档和元组

- [ ] 写solver-harness的README
- [ ] 更新solver-tmux-launch元组，指向solver-harness
- [ ] commit

---

## 七、与现有系统的关系

### 7.1 替代关系

solver-harness**替代**现有的手动启动流程（solver-tmux-launch元组中描述的手动tmux命令）。现有手动流程的痛点：
- 需要手动创建目录、复制模板、启动tmux、启动pipe-pane
- 没有MITM代理，只有step级数据
- 数据散落在实验目录内，AI可能看到

### 7.2 复用关系

solver-harness**复用**以下已有组件：
- `mitm_proto_capture.py`（MITM addon）
- `decode_connect_proto.py`（protobuf解码器）
- `trajectory_monitor.py`（sessions.db轮询）
- `templates/solver_agents_md.md`（Solver AGENTS.md模板）

### 7.3 不影响关系

solver-harness**不影响**：
- GuidedLoop（`runtime/guided_loop.py`）——GuidedLoop可以调用solver-harness启动Solver
- trajectory_extractor.py（post-analysis工具，从sessions.db提取完整trajectory）
- thinking_extractor.py（简化版thinking提取）

---

## 八、风险和缓解

| 风险 | 缓解 |
|---|---|
| mitmproxy CA信任是全局的，可能被滥用 | 测试结束后移除Keychain信任；文档中说明安全注意事项 |
| MITM端口冲突 | 端口分配算法 + 启动前检测 + 失败时降级 |
| protobuf schema是逆向推断的，可能有误差 | 保留raw bytes作为ground truth；解码失败时记录error不中断 |
| 4个tmux sessions管理复杂 | cmd_stop统一停止；cmd_status统一查看状态 |
| D盘HDD较慢 | raw数据在D盘，解码后的jsonl较小；如需更快可考虑SSD |

---

## 九、待确认问题

1. **mitmproxy CA信任**：是否接受全局Keychain信任mitmproxy CA？（测试结束后可移除）
2. **端口分配**：`18888 + hash(exp_id) % 100`是否合理？还是用固定端口+顺序分配？
3. **GuidedLoop集成**：solver-harness是否需要被GuidedLoop调用？还是独立使用？
