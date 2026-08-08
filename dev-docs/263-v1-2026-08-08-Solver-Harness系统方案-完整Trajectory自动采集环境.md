# 263 · Solver-Harness系统方案 · 完整Trajectory自动采集环境

**日期**：2026-08-08
**状态**：方案设计完成，已确认，待实施
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

**关键约束**：
- AI不能看到自己的运行数据——这会污染Solver的行为。数据必须放在Solver工作目录之外。
- 支持多AI并发实验——多个实验可能同时运行，互不干扰。
- MITM和证书信任只影响目标devin cli，不能影响本机其他程序。

---

## 二、核心设计决策（已确认）

### 2.1 目录分离

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
  │   ├── trajectory.jsonl  (解码后的token级流式数据，由共享decoder分发)
  │   └── capture.log       (MITM捕获日志，由共享mitmproxy写入)
  ├── sessions_db/
  │   └── trajectory.jsonl  (从sessions.db提取的step级数据)
  ├── tmux/
  │   ├── tmux_pipe.log     (pipe-pane兜底记录)
  │   └── tmux.log          (tee记录)
  └── exports/
      └── conversation.json (devin --export导出)

共享MITM数据目录（所有实验共用一个mitmproxy）:
  /data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/
  ├── chatmsg_001_*.bin     (raw protobuf响应)
  ├── chatmsg_002_*.bin
  └── capture.log           (全局捕获日志)
```

**为什么分离**：
- AI在Solver工作目录中做题，如果看到trajectory数据会改变行为（比如看到自己之前的thinking会自我修正）
- trajectory数据是工程设施，不是AI的认知环境
- 同名子目录设计（`<exp-id>`）让两个目录一一对应，好查

### 2.2 全局单mitmproxy + CA永久信任 + host白名单

**设计**：所有实验共享一个mitmproxy实例（固定端口18888），不每实验启动独立实例。

**为什么全局单实例**：
- 端口只有一个，无冲突问题
- 并发实验共享同一mitmproxy，通过protobuf响应中的`session_id`（field 17）区分属于哪个实验
- 资源开销小（一个mitmproxy进程 vs N个）

**CA信任策略**：永久信任mitmproxy CA于macOS Keychain。

**为什么永久信任**：
- 并发场景下，每次信任/移除CA不可行——AI-A实验中途，AI-B操作Keychain会导致AI-A的TLS验证中断
- `security add-trusted-cert`需要密码权限，并发时多个AI同时操作Keychain有竞争
- mitmproxy CA私钥在`~/.mitmproxy/`，只有本机用户可读，不离开本机，风险可控

**host白名单限制（关键安全措施）**：

mitmproxy启动时加`--allow-hosts`参数，**只对devin相关的host做MITM解密**，其他host的HTTPS流量直接TCP透传不解密：

```bash
mitmdump --listen-port 18888 \
  --allow-hosts "server\.self-serve\.windsurf\.com|api\.devin\.ai|static\.devin\.ai" \
  -s mitm_proto_capture.py
```

**为什么加host白名单**：
- 即使其他程序意外走了mitmproxy代理（环境变量泄漏），它们的HTTPS流量也不会被解密
- 缩小MITM作用范围，降低CA信任全局的安全风险
- 只拦截devin cli需要通信的3个host：
  - `server.self-serve.windsurf.com`（GetChatMessage等inference端点）
  - `api.devin.ai`（session管理）
  - `static.devin.ai`（CLI manifest）

**代理隔离**：`HTTPS_PROXY`通过环境变量传给devin cli进程，是进程级的，只影响devin cli，不影响本机其他程序。其他程序不走mitmproxy代理，不受影响。

**mitmproxy生命周期**：
- solver-harness首次launch时，如果mitmproxy未运行，则启动（tmux session `harness-mitmproxy`）
- 后续实验复用已运行的mitmproxy
- mitmproxy不随单个实验stop而停止——它是共享设施
- 提供`python3 solver_harness.py mitm stop`手动停止

### 2.3 三层数据采集（互为补充）

| 层 | 数据源 | 粒度 | 延迟 | 用途 |
|---|---|---|---|---|
| 1. MITM代理 | HTTPS流量拦截 | token级 | ~0ms | 实时thinking流、token usage统计 |
| 2. sessions.db轮询 | sessions.db | step级 | ~3s | 完整trajectory（含tool_results）、MITM兜底 |
| 3. tmux pipe-pane | 终端输出 | 行级 | ~0ms | 兜底记录、人类可读 |

**为什么三层都要**：
- MITM可能失败（CA未信任、protobuf解析错误、mitmproxy未运行）
- sessions.db轮询有~3s延迟，但数据最完整（含tool_results）
- tmux pipe-pane是最可靠的兜底，但只有终端可见内容
- 三层互为补充，任一层失败其他层仍能提供数据

### 2.4 GuidedLoop独立使用

solver-harness和GuidedLoop是两个独立工具：
- solver-harness专注trajectory采集，用于裸跑测试（baseline测试、能力边界定位）
- GuidedLoop专注引导逻辑，用于引导式实验
- 先解耦后集成——裸跑测试的trajectory采集验证可靠后，再考虑GuidedLoop集成

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
    │   ├── 确保共享mitmproxy运行（未运行则启动）
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
    │   └── 停止该实验的tmux sessions（不影响共享mitmproxy）
    │
    ├── cmd_decode: 手动解码MITM raw数据
    │   └── 调用decode_connect_proto.py
    │
    ├── cmd_list: 列出所有实验
    │   ├── Solver工作目录列表
    │   ├── Trajectory数据目录列表
    │   └── 运行中的tmux sessions
    │
    ├── cmd_mitm: 管理共享mitmproxy
    │   ├── start: 启动mitmproxy（如果未运行）
    │   ├── stop: 停止mitmproxy
    │   └── status: 查看mitmproxy状态
    │
    └── cmd_decode_all: 解码共享raw目录，按session_id分发到各实验
        └── 扫描_shared/mitm_raw/，解码每个.bin，按session_id写入对应实验的mitm/trajectory.jsonl
```

### 3.2 数据流

```
┌─────────────────────────────────────────────────────────────┐
│  共享层（所有实验共用）                                        │
│                                                              │
│         cloud API (server.self-serve.windsurf.com)           │
│                        │ HTTPS                               │
│                        ▼                                     │
│         mitmproxy (port 18888, --allow-hosts 限制)            │
│         addon: mitm_proto_capture                            │
│                        │                                     │
│                        ▼                                     │
│         _shared/mitm_raw/                                    │
│         chatmsg_001_*.bin (含session_id field 17)            │
│                        │                                     │
│                        │ cmd_decode_all                       │
│                        │ (按session_id分发)                   │
│                        ▼                                     │
│         各实验的 mitm/trajectory.jsonl (token级)              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  每实验层（独立）                                              │
│                                                              │
│  devin cli (走mitmproxy代理, HTTPS_PROXY环境变量)             │
│       │                                                      │
│       ├──→ sessions.db (全局共享)                             │
│       │        │                                             │
│       │        ▼                                             │
│       │    sessions_db轮询 (每3s, tmux: harness-dbmon-<exp>) │
│       │        │                                             │
│       │        ▼                                             │
│       │    sessions_db/trajectory.jsonl (step级)              │
│       │                                                      │
│       ├──→ exports/conversation.json (--export)              │
│       │                                                      │
│       └──→ tmux pipe-pane → tmux/tmux_pipe.log (兜底)        │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 tmux sessions

**共享tmux session**（全局，不随单个实验停止）：

| tmux session | 用途 | 生命周期 |
|---|---|---|
| `harness-mitmproxy` | 共享mitmproxy实例 | 首次launch时启动，手动stop才停止 |

**每实验tmux sessions**（实验运行期间）：

| tmux session | 用途 | 生命周期 |
|---|---|---|
| `harness-<exp-id>` | devin cli主进程 | 实验运行期间 |
| `harness-dbmon-<exp-id>` | sessions.db轮询 | 实验运行期间 |

**注意**：解码不再是实时daemon——改为`cmd_decode_all`事后批量解码（或实验结束后自动调用一次）。原因：共享mitmproxy的raw目录混合了多个实验的数据，需要按session_id分发，实时分发逻辑复杂且容易出错。事后批量解码更简单可靠。

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

# 停止实验（不影响共享mitmproxy）
python3 solver_harness.py stop --exp-id 258-matrix-test

# 列出所有实验
python3 solver_harness.py list

# 解码共享raw目录，按session_id分发到各实验
python3 solver_harness.py decode-all

# 管理共享mitmproxy
python3 solver_harness.py mitm start   # 启动mitmproxy
python3 solver_harness.py mitm stop    # 停止mitmproxy
python3 solver_harness.py mitm status  # 查看状态
```

**已有初版代码**（`xishujuzhen/solver_harness/solver_harness.py`），需根据本方案重写（初版是每实验独立mitmproxy的旧设计）。

### 4.2 MITM组件（复用已有，需修改）

| 组件 | 位置 | 状态 | 需要的修改 |
|---|---|---|---|
| mitmproxy addon | `xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py` | ✅ 已有 | 无需修改（raw目录通过环境变量传入） |
| protobuf解码器 | `xishujuzhen/mitm_thinking_intercept/decode_connect_proto.py` | ✅ 已有 | 需增加session_id提取（field 17） |

**mitmproxy启动命令**（由solver-harness的`cmd_mitm start`执行）：
```bash
MITM_RAW_DIR=/data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw \
mitmdump --listen-port 18888 \
  --allow-hosts "server\.self-serve\.windsurf\.com|api\.devin\.ai|static\.devin\.ai" \
  -s xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py \
  --set ssl_insecure=true
```

### 4.3 sessions.db轮询组件（复用已有）

| 组件 | 位置 | 状态 |
|---|---|---|
| trajectory_monitor.py | `xishujuzhen/trajectory_monitor.py` | ✅ 已有，无需修改 |

### 4.4 解码分发器（新增）

**职责**：扫描`_shared/mitm_raw/`，解码每个`.bin`文件，提取protobuf中的`session_id`（field 17），把解码结果写入`session_id`对应实验的`mitm/trajectory.jsonl`。

**session_id到exp-id的映射**：通过`session_info.json`中的`devin_session_id`字段。devin cli启动后，从sessions.db中查找该实验work_dir对应的session_id，写入session_info.json。decode-all时读取所有实验的session_info.json构建映射表。

**实现位置**：solver-harness.py的`cmd_decode_all`方法内，或独立脚本`xishujuzhen/solver_harness/decode_dispatcher.py`。

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
  "mitm_port": 18888,
  "mitm_enabled": true,
  "devin_session_id": null,
  "start_timestamp": "2026-08-08T02:15:00Z",
  "status": "running|stopped|completed"
}
```

**`devin_session_id`**：devin cli启动后，从sessions.db中查找该实验`work_dir`对应的session_id，回填此字段。decode-all时用此字段匹配MITM raw数据中的session_id。

### 5.2 mitm/trajectory.jsonl（token级，每行一个GetChatMessage响应）

```json
{
  "source_file": "chatmsg_001_020811_703943.bin",
  "session_id": "1dfa317e-8bb6-4668-b1be-572756774ad7",
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

### 6.1 重写主控脚本

**为什么做**：初版脚本（`solver_harness.py`）是每实验独立mitmproxy的旧设计，需要改为全局共享mitmproxy的新设计。

- [ ] 重写`cmd_mitm`（start/stop/status）：管理共享mitmproxy
- [ ] 重写`cmd_launch`：确保mitmproxy运行 → 创建目录 → 复制模板 → 写session_info → 启动db轮询 → 启动devin cli（走代理）→ 启动pipe-pane → 回填devin_session_id
- [ ] 重写`cmd_stop`：停止该实验的tmux sessions（不影响共享mitmproxy）+ 调用decode-all解码本实验数据 + 更新session_info
- [ ] 实现`cmd_decode_all`：扫描共享raw目录 → 解码 → 按session_id分发到各实验
- [ ] 完善`cmd_status`：session_info + tmux状态 + 数据统计
- [ ] 完善`cmd_list`：列出所有实验

### 6.2 修改protobuf解码器

**为什么做**：当前解码器不提取session_id（field 17），decode-all需要session_id来分发数据。

- [ ] `decode_connect_proto.py`的`extract_streaming_data`增加session_id提取
- [ ] 验证session_id正确提取（用sample_capture测试）

### 6.3 实现decode-all分发逻辑

**为什么做**：共享mitmproxy的raw目录混合了多个实验的数据，需要按session_id分发到各实验。

- [ ] 构建session_id → exp-id映射表（读所有实验的session_info.json）
- [ ] 解码每个.bin，提取session_id，写入对应实验的mitm/trajectory.jsonl
- [ ] 未匹配的session_id写入`_shared/unmatched/`目录（可能是已停止实验的数据）

### 6.4 测试

- [ ] 端到端测试：用简单题测试完整launch流程
- [ ] MITM数据验证：launch → 等AI产出 → stop → decode-all → 检查mitm/trajectory.jsonl
- [ ] sessions.db数据验证：检查sessions_db/trajectory.jsonl是否有step级数据
- [ ] 兜底记录验证：检查tmux/tmux_pipe.log是否有终端输出
- [ ] 并发测试：启动两个实验，验证数据不串

### 6.5 文档和元组

- [ ] 写solver-harness的README
- [ ] 更新solver-tmux-launch元组，指向solver-harness
- [ ] 更新263号方案文档的实现状态
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
- `decode_connect_proto.py`（protobuf解码器，需小改增加session_id提取）
- `trajectory_monitor.py`（sessions.db轮询）
- `templates/solver_agents_md.md`（Solver AGENTS.md模板）

### 7.3 不影响关系

solver-harness**不影响**：
- GuidedLoop（`runtime/guided_loop.py`）——独立工具，未来可选集成
- trajectory_extractor.py（post-analysis工具，从sessions.db提取完整trajectory）
- thinking_extractor.py（简化版thinking提取）

---

## 八、风险和缓解

| 风险 | 缓解 |
|---|---|
| mitmproxy CA信任是全局的 | `--allow-hosts`限制只拦截devin相关host；mitmproxy只在需要时启动；CA私钥在`~/.mitmproxy/`只有本机用户可读 |
| 共享mitmproxy单点故障 | mitmproxy失败时devin cli无法连接云端API——solver-harness检测mitmproxy状态，未运行时自动启动；启动失败时降级为不走代理（无MITM数据但实验仍可运行） |
| protobuf schema是逆向推断的 | 保留raw bytes作为ground truth；解码失败时记录error不中断 |
| 并发实验数据串 | decode-all按session_id分发，未匹配的写入_unmatched/供人工排查 |
| devin_session_id回填延迟 | devin cli启动后需要几秒才在sessions.db中出现——launch后轮询sessions.db，最多等30秒 |
| D盘HDD较慢 | raw数据在D盘，解码后的jsonl较小；如需更快可考虑SSD |

---

## 九、已确认的设计决策（讨论记录）

| 问题 | 决策 | 理由 |
|---|---|---|
| CA信任策略 | 永久信任 | 并发场景下每次信任/移除不可行；CA私钥不离开本机，风险可控 |
| MITM作用范围 | `--allow-hosts`限制3个devin host | 确保MITM只影响目标devin，不影响本机其他程序 |
| mitmproxy实例数 | 全局一个，固定18888 | 端口无冲突，资源开销小，并发实验通过session_id区分 |
| 解码时机 | 事后批量（cmd_decode_all） | 共享raw目录混合多实验数据，实时分发复杂易错，事后批量更可靠 |
| GuidedLoop集成 | 独立使用，不集成 | 先解耦后集成，裸跑测试优先 |
