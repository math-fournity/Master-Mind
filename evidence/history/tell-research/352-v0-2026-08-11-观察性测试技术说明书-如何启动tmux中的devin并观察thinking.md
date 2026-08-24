# 352号 · 观察性测试技术说明书——如何启动tmux中的devin并观察thinking

**日期**：2026-08-11
**用途**：本文档是给另一个AI（或人类操作者）的完整技术说明书。读完本文档，你就能在这台机器上启动devin cli的数学Solver实例，并实时观察AI的完整thinking过程（token级实时流式），用于观察性测试。
**前置文档**：351号（委托提示词）、350号（全面验证方案）

---

## 0. 你将能做什么

读完本文档后，你能够：

1. **启动一个数学Solver**——让GLM-5.2做一道数学题
2. **实时观察AI的thinking**——token级流式，AI思考过程中每个token实时落盘，你可以像读文章一样实时看AI怎么想
3. **事后提取完整推理过程**——session结束后提取完整的thinking+tool_calls+tool_results
4. **判断AI是否做出来了**——通过文件检查、对话状态、thinking深度等多维度判断
5. **运行观察性测试**——bare测试（不给Tell）和Tell测试（给Tell后观察AI是否能做出来）

---

## 1. 系统架构概述

### 1.1 为什么需要这套机制

我们的核心研究问题是：**Tell（非特化的思维力提示词）能否激发AI的思维能力？**

要回答这个问题，我们必须：
1. 让AI做题（bare条件下做，和Tell指导下做）
2. **观察AI的thinking过程**——不只是看最终答案，而是看AI怎么想的
3. 对比bare和Tell条件下的thinking差异——Tell是否改变了AI的思维方式

**关键需求**：我们需要token级的实时thinking数据，不是step级的事后数据。原因：
- step级数据（每步完成后才能拿到）太粗——我们看不到AI在thinking过程中的"犹豫""转向""卡住"
- token级实时数据让我们能看到AI的完整推理流——包括AI尝试了什么方向、放弃了什么方向、为什么放弃

### 1.2 Devin CLI的通信架构

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

**关键点**：
- LLM推理在云端进行，thinking内容通过HTTPS流式返回
- thinking和content是分开的field——thinking是AI的内心独白，content是AI说出来的话
- **GLM-5.2的thinking用英文，content用中文**——分析时注意语言差异

### 1.3 MITM拦截原理

在`devin acp`和云端API之间插入mitmproxy代理：

```
devin acp → HTTPS_PROXY → mitmproxy → 云端API
                              ↓
                         拦截GetChatMessage响应
                              ↓
                         解码Connect streaming protobuf
                              ↓
                         实时提取thinking/content/tool_call chunks
                              ↓
                         token级实时落盘（4个文件）
```

**关键技术点**：
1. devin cli尊重`HTTPS_PROXY`/`HTTP_PROXY`环境变量
2. TLS证书信任：需要将mitmproxy CA证书加入macOS Keychain + 设置`NODE_EXTRA_CA_CERTS`环境变量
3. Connect streaming protobuf：每个envelope是 `1 byte flags + 4 bytes length + protobuf message`
4. Protobuf字段映射（field 9 = thinking/content chunk，逐token流式）

---

## 2. 环境前置条件

### 2.1 必须已安装的软件

| 软件 | 检查命令 | 安装方式 |
|---|---|---|
| devin cli | `which devin && devin --version` | 见devin cli文档 |
| mitmproxy | `which mitmdump` | `brew install mitmproxy` |
| tmux | `which tmux` | `brew install tmux` |
| Python 3 | `python3 --version` | 系统自带或`brew install python` |
| 项目venv | `ls .venv/bin/python3` | 见项目setup |

### 2.2 必须存在的文件/目录

| 路径 | 用途 |
|---|---|
| `xishujuzhen/solver_harness/solver_harness.py` | 启动Solver的主脚本 |
| `xishujuzhen/thinking_extractor.py` | 事后提取thinking的脚本 |
| `templates/solver_agents_md.md` | Solver的AGENTS.md模板（裸跑用） |
| `templates/solver_agents_md_guided.md` | Solver的AGENTS.md模板（引导实验用） |
| `~/.mitmproxy/mitmproxy-ca-cert.pem` | mitmproxy CA证书 |
| `~/.local/share/devin/cli/sessions.db` | devin cli的session数据库 |

### 2.3 mitmproxy系统服务

mitmproxy已被制作成macOS launchd系统服务，**开机自启动**：

| 属性 | 值 |
|---|---|
| 服务Label | `com.aurolafly.mitmproxy-devin` |
| 端口 | **18889** |
| addon脚本 | `~/.mitmproxy/mitm_proto_capture.py` |
| 日志 | `~/.mitmproxy/mitm_stdout.log` + `~/.mitmproxy/mitm_stderr.log` |
| 崩溃重启 | KeepAlive.SuccessfulExit=false（非正常退出自动重启） |
| 启动时机 | RunAtLoad=true（登录时自动启动） |

**检查mitmproxy状态**：
```bash
cd ~/master-mind-glm5.2-worktree
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm status
```

预期输出：
```
mitmproxy: RUNNING (launchd system service, port: 18889)
  raw dir: /data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw
  allow-hosts: server\.self-serve\.windsurf\.com|api\.devin\.ai|static\.devin\.ai
  ...
```

如果mitmproxy没有运行，启动它：
```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm start
```

### 2.4 数据存储位置——测试目录不在repo内

**重要**：Solver的工作目录和trajectory数据目录都**不在repo内**，在`/data/`外接磁盘上。不要在repo内创建测试目录——会污染git状态。

| 路径 | 用途 | 是否在repo内 |
|---|---|---|
| `/data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/` | Solver的工作目录（AI在这里做题） | **否** |
| `/data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/` | Trajectory数据目录（thinking等） | **否** |
| `/data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/` | 共享MITM raw数据 | **否** |
| `~/master-mind-glm5.2-worktree/` | repo（系统代码、文档） | 是——但Solver不在这里工作 |

**为什么在`/data/`上**：
1. **隔离**——Solver工作目录和repo完全隔离，Solver的文件操作不会影响git状态
2. **空间**——thinking数据和tmux日志可能很大（单次实验可达数十MB），外接磁盘空间充足
3. **性能**——Solver的频繁文件读写不占用系统盘IO

### 2.5 每次测试创建独立目录——不重复使用

**铁律：每次测试都必须用新的exp-id，创建独立的工作目录和trajectory目录。不要复用已有实验的目录。**

**原因**：
1. **session隔离**——如果在新实验的工作目录中看到上一题的problem.txt/proof.md/hint.txt，AI会被干扰
2. **数据留存**——每次测试的完整数据（thinking+proof+tmux日志）都应该留存，用于事后分析和对比。复用目录会覆盖之前的数据
3. **可追溯性**——每个实验都应该有独立的session_info.json，记录实验元信息（exp-id/session_id/时间/model等）

**正确做法**：
```bash
# 每次测试用新的exp-id
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id bare-test-001 \    # 第一次测试
  --problem-file /tmp/problem-001.txt \
  --model glm-5-2

# 第二次测试用不同的exp-id
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id bare-test-002 \    # 不是bare-test-001
  --problem-file /tmp/problem-002.txt \
  --model glm-5-2
```

**exp-id命名建议**（保证唯一性+可追溯性）：
| 场景 | 命名格式 | 示例 |
|---|---|---|
| bare测试 | `bare-<思维力>-<题号>-<run号>` | `bare-isomorphism-bridge-q1-run1` |
| Tell测试 | `tell-<思维力>-<题号>-<run号>` | `tell-isomorphism-bridge-q1-run1` |
| 交叉验证 | `xval-<思维力>-<题号>-<不匹配Tell>` | `xval-isomorphism-bridge-q1-tell-invariant` |
| 负对照 | `neg-<思维力>-<题号>-encouragement` | `neg-isomorphism-bridge-q1-encouragement` |

**已有实验的数据不要删除**——它们是研究数据，可能需要事后重新分析。如果磁盘空间不足，可以归档到冷存储，但不要直接删除。

### 2.6 yolo模式（--permission-mode dangerous）

solver-harness启动devin cli时自动添加两个关键参数：

```python
# solver_harness.py中的关键代码
devin_cmd = f"devin -p '{prompt}' --model {model} --respect-workspace-trust false --permission-mode dangerous --export {export_path}"
```

**`--permission-mode dangerous`（yolo模式）**：
- **含义**：devin cli的所有工具调用（exec/read/write/edit）自动批准，不弹出确认提示
- **为什么需要**：Solver做题时需要频繁调用exec（运行Python验证）、write（写proof.md）、read（读problem.txt）。如果每次都弹确认提示，需要人工干预，无法无人值守运行
- **风险**：AI可以执行任意命令、读写任意文件。但Solver的工作目录在`/data/`上，和repo隔离，风险可控
- **你不需要手动加这个参数**——solver-harness自动添加

**`--respect-workspace-trust false`**：
- **含义**：不要求workspace trust确认，直接在工作目录中运行
- **为什么需要**：devin cli首次进入一个工作目录时会问"是否信任这个目录"。如果要求信任确认，需要人工干预
- **你不需要手动加这个参数**——solver-harness自动添加

**这两个参数的含义是：Solver在无人值守模式下运行，所有工具调用自动批准，不需要人工干预。** 这就是为什么solver-harness是启动Solver的唯一正确方式——它自动处理了所有这些配置。

**如果你手动启动devin cli（不推荐）**，需要自己加这两个参数：
```bash
# 不推荐——请用solver-harness
HTTPS_PROXY=http://localhost:18889 \
HTTP_PROXY=http://localhost:18889 \
NODE_EXTRA_CA_CERTS=~/.mitmproxy/mitmproxy-ca-cert.pem \
devin -p "你的prompt" \
  --model glm-5-2 \
  --respect-workspace-trust false \
  --permission-mode dangerous \
  --export /path/to/export.json
```

---

## 3. 完整工作流——从启动到观察到停止

### 3.1 步骤1：确认mitmproxy运行中

```bash
cd ~/master-mind-glm5.2-worktree
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm status
```

如果输出`RUNNING`，继续下一步。如果输出`NOT RUNNING`，先启动：
```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm start
```

### 3.2 步骤2：准备题目文件

把题目写入一个文本文件。**这是铁律——`devin -p`的命令行参数有长度限制，长题目必须通过文件传递。**

```bash
# 准备题目文件
cat > /tmp/problem.txt << 'EOF'
你是数学大师。请解答以下竞赛数学题。

题目（测试题-1）：
设 $a_1, a_2, \ldots, a_n$ 是实数，满足 $\sum a_i = n$ 且 $\sum a_i^2 = 2n$。
证明：存在某个 $i$ 使得 $|a_i| \geq 2$。

要求：
1. 给出完整的解答过程
2. 最终答案用\boxed{答案}格式给出
3. 数学公式用LaTeX
4. 如果你不知道，明确说"我不知道"
5. 把证明写到proof.md文件中
EOF
```

**题目文件格式要点**：
- 开头说"你是数学大师"——让AI进入数学解题角色
- 题目用LaTeX写
- 要求中包含"把证明写到proof.md文件中"——防止AI在对话中输出长文本被截断
- 如果是Tell测试，在题目后面加上Tell（见§5）

### 3.3 步骤3：启动Solver

```bash
cd ~/master-mind-glm5.2-worktree

.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id my-test-001 \
  --problem-file /tmp/problem.txt \
  --model glm-5-2
```

**参数说明**：
| 参数 | 含义 | 示例 |
|---|---|---|
| `--exp-id` | 实验ID，用于命名目录和tmux session | `my-test-001` |
| `--problem-file` | 题目文件路径 | `/tmp/problem.txt` |
| `--model` | 模型名 | `glm-5-2` |
| `--prompt` | 自定义prompt（默认是"请读取当前目录下的problem.txt文件，解答其中的数学题。"） | 可选 |
| `--no-mitm` | 不启用MITM代理（**不要用**——会丢失thinking数据） | 不要加 |
| `--interactive` | 交互模式（支持运行时send-keys提示注入） | 见§6 |

**exp-id命名规范**：
| 场景 | 格式 | 示例 |
|---|---|---|
| 裸跑测试 | `<描述>` | `bare-test-001` |
| Tell测试 | `tell-<思维力>-<编号>` | `tell-isomorphism-bridge-001` |
| 批量测试 | `batch-<批次名>-<题号>` | `batch-imo2025-p5` |

**启动后自动完成**：
1. 创建Solver工作目录：`/data/math-agent-glm5.2-tmux-agents-dir/my-test-001/`
2. 创建Trajectory数据目录：`/data/math-agent-glm5.2-tmux-agents-trajectory/my-test-001/`
3. 复制AGENTS.md模板到Solver目录
4. 复制problem.txt到Solver目录
5. 写session_info.json
6. 启动sessions.db轮询进程（step级trajectory）
7. 启动devin cli in tmux（走mitmproxy代理）
8. 启动pipe-pane兜底记录
9. 回填devin_session_id

### 3.4 步骤4：实时观察thinking（核心！）

启动Solver后，thinking数据会**实时落盘**。有4个文件可以观察：

#### 方式1：人可阅读的连续文本（推荐——像读文章一样实时看AI思考）

```bash
# 实时观察AI的thinking——像读文章一样
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/my-test-001/mitm/thinking_readable.txt
```

**输出格式**：
```
============================================================
[04:50:39] === Thinking Round 3 START ===
============================================================
Let me analyze this problem carefully.

We have $a_1, a_2, \ldots, a_n$ real numbers with:
- $\sum a_i = n$
- $\sum a_i^2 = 2n$
...

--- [Tool Call: read] [04:50:37] ---
args: {"file_path": "/data/..."}
---

============================================================
[04:50:38] === Thinking Round 3 END ===
  thinking: 6261 chars, 1200 chunks
  tool_calls: 1
  elapsed: 28.5s
============================================================
```

**这是最直观的观察方式**——你可以看到AI的完整推理流，包括：
- AI在思考什么（thinking内容）
- AI调用了什么工具（tool_call用分隔符标记）
- 每轮thinking的起止时间和字符数
- AI的推理是连续的文本，不是碎片

#### 方式2：token级碎片流（适合调试和精确时间分析）

```bash
# 查看特定实验的thinking流（token级碎片格式）
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/my-test-001/mitm/thinking_live.txt

# 查看所有实验的thinking流（全局）
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/thinking_live.txt
```

#### 方式3：程序化读取（JSONL格式，每个chunk一行）

```bash
# 查看JSONL格式的thinking数据
cat /data/math-agent-glm5.2-tmux-agents-trajectory/my-test-001/mitm/thinking_live.jsonl
```

每行是一个JSON对象，包含timestamp/chunk_index/content。

#### 方式4：观察tmux session（看AI的终端输出）

```bash
# 查看tmux session输出（最后30行）
tmux capture-pane -t harness-my-test-001 -p | tail -30

# 持续观察（attach到tmux session）
tmux attach -t harness-my-test-001
# 退出attach：Ctrl+B然后D

# 深度观察（看最后300行，去掉ANSI噪音）
tmux capture-pane -t harness-my-test-001 -p -S -300 | grep -v '^\[' | grep -v '^$' | tail -60
```

**tmux session名规范**：`harness-<exp-id>`——如`harness-my-test-001`

### 3.5 步骤5：检查实验状态

```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py status --exp-id my-test-001
```

### 3.6 步骤6：判断AI是否做出来了

**多维度判断**：

```bash
# 1. 检查AI是否写了证明文件
ls -la /data/math-agent-glm5.2-tmux-agents-dir/my-test-001/proof*

# 2. 读证明内容
cat /data/math-agent-glm5.2-tmux-agents-dir/my-test-001/proof.md

# 3. 看对话状态——AI是否说了"证毕"或"QED"
tmux capture-pane -t harness-my-test-001 -p | grep -i "证毕\|QED\|证完"

# 4. 看thinking字符数——判断思考深度
# tmux屏幕上会显示 "Thinking · Xm Ys · (NNNNNc · ctrl+o for details)"
# NNNNNc是thinking的字符数，40k+表示深度思考
tmux capture-pane -t harness-my-test-001 -p | grep "Thinking"

# 5. 看thinking内容——AI是否卡住了
tail -100 /data/math-agent-glm5.2-tmux-agents-trajectory/my-test-001/mitm/thinking_readable.txt
```

**判断标准**：
| 信号 | 含义 |
|---|---|
| 写了proof.md且内容正确 | **做出来了** |
| 写了proof.md但内容有错 | 做了但做错了 |
| 没写proof.md但thinking超过50k字符 | 想了很多但做不出来（卡住了） |
| 没写proof.md且thinking很少 | 没认真尝试或过早放弃 |
| 调用了exec做数值验证 | 在认真尝试 |
| 不调用exec只在thinking里转 | 可能卡住了 |
| 说了"我不知道" | 明确放弃 |

### 3.7 步骤7：停止实验（自动decode-all）

```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id my-test-001
```

**自动完成**：
1. 停止该实验的tmux sessions（devin cli + db monitor，**不影响共享mitmproxy**）
2. 调用decode-all：扫描共享raw目录，通过_req文件中的work_dir匹配实验，解码分发到`<exp-id>/mitm/trajectory.jsonl`

### 3.8 步骤8：事后提取完整thinking

session结束后，可以用thinking_extractor.py提取完整的thinking数据（含tool_results）：

```bash
cd ~/master-mind-glm5.2-worktree

# 方法A：知道工作目录（推荐——最简单）
.venv/bin/python3 xishujuzhen/thinking_extractor.py \
  --work-dir /data/math-agent-glm5.2-tmux-agents-dir/my-test-001 \
  --summary

# 方法B：知道session_id
# 先从session_info.json找session_id
cat /data/math-agent-glm5.2-tmux-agents-trajectory/my-test-001/session_info.json | grep session_id
# 然后用session_id提取
.venv/bin/python3 xishujuzhen/thinking_extractor.py \
  --session-id <session_id> \
  --summary

# 方法C：列出最近的session
sqlite3 ~/.local/share/devin/cli/sessions.db \
  "SELECT id, title, working_directory, created_at FROM sessions ORDER BY created_at DESC LIMIT 10;"
```

**--summary输出示例**：
```
Session: nova-authority
Steps: 15
Steps with thinking: 12
Total thinking chars: 45230
Total content chars: 8200
Tool calls: 8
```

**检查要点**：
- `Steps with thinking` > 0（有thinking数据）
- `Total thinking chars` > 1000（thinking数据足够分析）
- 如果`Steps with thinking` = 0，可能是旧版devin cli或非GLM-5.2模型

**导出完整数据**：
```bash
# 导出为Markdown（可读，用于人工分析）
.venv/bin/python3 xishujuzhen/thinking_extractor.py \
  --work-dir /data/math-agent-glm5.2-tmux-agents-dir/my-test-001 \
  --format markdown \
  -o /tmp/my-test-001-thinking.md

# 导出为JSON（完整数据，用于程序化分析）
.venv/bin/python3 xishujuzhen/thinking_extractor.py \
  --work-dir /data/math-agent-glm5.2-tmux-agents-dir/my-test-001 \
  --format json \
  -o /tmp/my-test-001-thinking.json
```

---

## 4. 数据产物完整说明

每次实验产生的数据：

```
/data/math-agent-glm5.2-tmux-agents-trajectory/my-test-001/
├── session_info.json          # 实验元信息（含devin_session_id）
├── mitm/
│   ├── thinking_readable.txt  # ★人可阅读的连续文本（实时拼接，可tail -f读文章）
│   ├── thinking_live.jsonl    # 流式实时thinking（每个chunk一行，JSONL格式）
│   ├── thinking_live.txt      # 流式实时thinking（token级碎片，可tail -f）
│   └── trajectory.jsonl       # stop时decode-all生成的完整trajectory
├── sessions_db/
│   └── trajectory.jsonl       # step级（db monitor实时轮询）
├── tmux/
│   ├── tmux.log               # tee输出
│   └── tmux_pipe.log          # pipe-pane兜底
└── exports/
    └── conversation.json      # devin cli --export

/data/math-agent-glm5.2-tmux-agents-dir/my-test-001/
├── AGENTS.md                  # Solver的角色定义（从模板复制）
├── problem.txt                # 题目文件
├── proof.md                   # AI写的证明（如果做出来了）
└── ...                        # AI可能创建的其他文件
```

**三层trajectory记录对比**：
| 记录手段 | 层次 | 说明 | 自动采集 |
|---|---|---|---|
| MITM | 网络层 | raw protobuf解码，token级thinking+tool_calls | stop时自动decode-all |
| --export | devin cli原生 | 结构化JSON，每轮自动导出 | launch时自动添加 |
| pipe-pane | tmux兜底 | 纯文本terminal输出 | launch时自动启动 |

**MITM vs sessions.db的thinking数据**：
- MITM：token级实时，thinking+tool_calls，**无tool_results**
- sessions.db：step级事后，thinking+content+tool_calls+**tool_results**
- 两者获取的thinking内容完全一致（已验证2026-08-08）

### 4.1 三种trajectory的详细对比——格式、内容、用途

上表列了三种trajectory的概要，但另一个AI需要更详细的说明才能正确使用它们。以下是每种trajectory的完整说明。

#### trajectory-1：MITM trajectory.jsonl（网络层解码产物）

**位置**：`<exp-id>/mitm/trajectory.jsonl`
**生成时机**：`stop`命令时自动decode-all生成（不是实时的——实时数据在thinking_live.txt/jsonl中）
**格式**：JSONL，每行一个JSON对象
**内容**：每个GetChatMessage响应解码后的完整数据

```json
{
  "source_file": "chatmsg_009_052008_742041.bin",   // raw protobuf文件名
  "session_id": "0d8e0864-...",                       // devin session_id
  "matched_exp": "ab-253-A2",                         // 匹配到的实验
  "decoded_at": 1786181825.923052,                    // 解码时间戳
  "total_messages": 42,                               // 这个响应中的总message数
  "content_thinking": "Let me read the problem.txt file.",  // thinking内容（拼接后）
  "content_chunks_count": 8,                          // thinking的chunk数
  "tool_calls": {                                     // tool调用
    "chatcmpl-tool-8b405c98f3b2d2c0": {
      "name": "read",
      "args": "{\"file_path\": \"/data/.../problem.txt\"}"
    }
  }
}
```

**包含什么**：thinking内容（拼接后）+ tool_calls（工具名+参数）
**不包含什么**：tool_results（工具返回结果）、content（AI说出来的话，部分版本可能包含）
**用途**：token级thinking分析——看AI每个推理步骤在想什么
**注意**：同一个response可能被decode多次（每次decode-all都会追加），分析时需要按decoded_at去重或取最新

#### trajectory-2：sessions_db trajectory.jsonl（数据库轮询产物）

**位置**：`<exp-id>/sessions_db/trajectory.jsonl`
**生成时机**：db monitor实时轮询sessions.db写入（每3秒轮询一次，每步完成后才能拿到）
**格式**：JSONL，每行一个step
**内容**：完整的step级数据——thinking + content + tool_calls + **tool_results**

```json
{"type": "step", "node_id": 14, "parent_node_id": 13, "role": "user", "content": "请读取当前目录下的problem.txt文件，解答其中的数学题。", "thinking": "", "tool_calls": [], "created_at": 1786193087}
{"type": "step", "node_id": 23, "parent_node_id": 22, "role": "assistant", "content": "", "thinking": "Let me read the problem.txt file.", "tool_calls": [{"id": "chatcmpl-tool-9d208fbb...", "name": "read", "arguments": {"file_path": "/data/.../problem.txt"}, "index": 0, "kind": "function"}], "created_at": 1786193144}
{"type": "step", "node_id": 25, "parent_node_id": 24, "role": "tool", "content": "<file-view path=\"/data/.../problem.txt\">...</file-view>", "thinking": "", "tool_calls": [], "created_at": 1786193144}
```

**包含什么**：
- `role: "user"`行——用户消息（content是用户输入）
- `role: "assistant"`行——AI回复（thinking是内心独白，content是说出来的话，tool_calls是工具调用）
- `role: "tool"`行——工具返回结果（content是工具输出）← **这是MITM数据没有的**

**不包含什么**：token级流式数据（只有step级完整数据）
**用途**：**最完整的trajectory**——包含thinking+content+tool_calls+tool_results，适合事后完整分析
**注意**：每个node可能出现两次（渲染重复），分析时需要按node_id去重

#### trajectory-3：exports conversation.json（devin cli原生导出）

**位置**：`<exp-id>/exports/conversation.json`
**生成时机**：devin cli自动导出（每轮自动写入，launch时通过`--export`参数指定路径）
**格式**：JSON（不是JSONL——整个文件是一个JSON对象）
**内容**：devin cli原生的结构化对话记录

```json
{
  "schema_version": "ATIF-v1.7",
  "session_id": "energetic-action",
  "agent": {
    "name": "devin",
    "version": "3000.3.27",
    "model_name": "GLM-5.2",
    "extra": {
      "backend": "Windsurf",
      "permission_mode": "Bypass"
    }
  },
  "steps": [
    {
      "step_id": 1,
      "timestamp": "2026-08-08T14:21:48.434226+00:00",
      "source": "system",
      "message": "You are Devin, an interactive command line agent...",
      "extra": {"telemetry": {"source": "sysprompt", "operation": "normal"}}
    },
    {
      "step_id": 4,
      "timestamp": "...",
      "source": "user",
      "message": "请读取当前目录下的problem.txt文件，解答其中的数学题。"
    },
    {
      "step_id": 5,
      "timestamp": "...",
      "source": "assistant",
      "message": "...",
      "thinking": "...",
      "tool_calls": [...]
    }
  ]
}
```

**包含什么**：完整的对话历史——system prompt + user消息 + assistant回复（含thinking） + tool_calls + tool_results
**不包含什么**：token级流式数据
**用途**：devin cli原生的完整对话记录，格式最规范，适合程序化分析和归档
**特点**：
- 包含system prompt（MITM和sessions_db不包含完整的system prompt）
- schema_version标记格式版本（ATIF-v1.7），便于跨版本兼容
- 每个step有明确的source（system/user/assistant/tool）和timestamp

#### 三种trajectory的选择指南

| 你要做什么 | 用哪种trajectory | 原因 |
|---|---|---|
| **实时观察AI思考** | `mitm/thinking_readable.txt` | 唯一的实时数据源，tail -f读文章 |
| **事后分析AI的完整推理** | `sessions_db/trajectory.jsonl` | 包含thinking+content+tool_calls+tool_results，最完整 |
| **程序化分析对话结构** | `exports/conversation.json` | devin cli原生格式，结构最规范，含system prompt |
| **提取纯thinking文本** | `thinking_extractor.py --work-dir <dir>` | 从sessions.db提取，自动去重，输出markdown/json |
| **看AI调用了什么工具** | `sessions_db/trajectory.jsonl` | tool_calls+tool_results都有 |
| **看工具返回了什么** | `sessions_db/trajectory.jsonl` | 唯一包含tool_results的trajectory |
| **归档完整实验记录** | `exports/conversation.json` | devin cli原生格式，最规范 |
| **精确时间分析（token级）** | `mitm/thinking_live.jsonl` | 每个chunk有毫秒级timestamp |

### 4.2 session_info.json——实验元信息

**位置**：`<exp-id>/session_info.json`
**内容**：实验的元信息，用于追溯实验配置

```json
{
  "exp_id": "vms-poc2-04-bare",
  "model": "glm-5-2",
  "prompt": "请读取当前目录下的problem.txt文件，解答其中的数学题。",
  "problem_file": "/path/to/original/problem.txt",
  "solver_dir": "/data/math-agent-glm5.2-tmux-agents-dir/vms-poc2-04-bare",
  "trajectory_dir": "/data/math-agent-glm5.2-tmux-agents-trajectory/vms-poc2-04-bare",
  "tmux_session": "harness-vms-poc2-04-bare",
  "mitm_port": 18889,
  "mitm_enabled": true,
  "devin_session_id": "energetic-action",
  "start_timestamp": "2026-08-08T14:21:48.322209+00:00",
  "status": "running",
  "interactive": false,
  "updated_at": "2026-08-08T14:21:49.492987+00:00"
}
```

**关键字段**：
- `devin_session_id`：devin cli的session ID，用于thinking_extractor.py
- `mitm_enabled`：是否启用了MITM代理（true=有token级thinking数据）
- `interactive`：是否是交互模式（true=支持运行时send-keys注入）
- `status`：实验状态（running/stopped）

### 4.3 decode-all做什么

`stop`命令时自动调用decode-all。decode-all的工作：

1. 扫描共享raw目录`/data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/`
2. 读取每个`chatmsg_NNN_HHMMSS_req.bin`（raw protobuf请求），从中提取work_dir
3. 通过work_dir匹配到对应的实验（exp-id）
4. 解码对应的`chatmsg_NNN_HHMMSS.bin`（raw protobuf响应）
5. 将解码结果分发到`<exp-id>/mitm/trajectory.jsonl`

**为什么需要decode-all**：MITM raw数据是所有实验混在一起的（共享mitmproxy），需要通过请求中的work_dir区分哪个响应属于哪个实验。

**手动触发decode-all**（如果stop时没自动解码，或需要重新解码）：
```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py decode-all
```

---

## 5. 观察性测试——bare测试 vs Tell测试

### 5.1 bare测试（不给Tell）

bare测试是所有实验的**前提条件**——如果bare AI本来就能做出来，Tell的"指导力"就是虚假的。

```bash
# 准备bare题目文件（不含任何Tell）
cat > /tmp/problem-bare.txt << 'EOF'
你是数学大师。请解答以下竞赛数学题。

题目（测试题-1）：
设 $a_1, a_2, \ldots, a_n$ 是实数，满足 $\sum a_i = n$ 且 $\sum a_i^2 = 2n$。
证明：存在某个 $i$ 使得 $|a_i| \geq 2$。

要求：
1. 给出完整的解答过程
2. 最终答案用\boxed{答案}格式给出
3. 数学公式用LaTeX
4. 如果你不知道，明确说"我不知道"
5. 把证明写到proof.md文件中
EOF

# 启动bare测试
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id bare-test-001 \
  --problem-file /tmp/problem-bare.txt \
  --model glm-5-2

# 实时观察thinking
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/bare-test-001/mitm/thinking_readable.txt
```

### 5.2 Tell测试（给Tell后观察AI是否能做出来）

Tell测试是在bare测试失败后进行的——bare做不出来，给Tell后看AI能不能做出来。

```bash
# 准备Tell题目文件（在题目后面加上Tell）
cat > /tmp/problem-tell.txt << 'EOF'
你是数学大师。请解答以下竞赛数学题。

题目（测试题-1）：
设 $a_1, a_2, \ldots, a_n$ 是实数，满足 $\sum a_i = n$ 且 $\sum a_i^2 = 2n$。
证明：存在某个 $i$ 使得 $|a_i| \geq 2$。

要求：
1. 给出完整的解答过程
2. 最终答案用\boxed{答案}格式给出
3. 数学公式用LaTeX
4. 如果你不知道，明确说"我不知道"
5. 把证明写到proof.md文件中

【思维引导】
当你面对一个需要"存在某个元素满足条件"的证明时，考虑以下思维流程：
1. 你需要证明的是什么？——存在性证明
2. 存在性证明的常见策略有哪些？——构造法、反证法、极值法
3. 这道题的条件（$\sum a_i = n$ 和 $\sum a_i^2 = 2n$）暗示了什么？
4. 如果所有 $|a_i| < 2$，会和已知条件产生什么矛盾？
5. 考虑用反证法——假设所有 $|a_i| < 2$，推导矛盾
EOF

# 启动Tell测试
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id tell-test-001 \
  --problem-file /tmp/problem-tell.txt \
  --model glm-5-2

# 实时观察thinking
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/tell-test-001/mitm/thinking_readable.txt
```

### 5.3 对比分析

```bash
# bare测试的thinking
cat /data/math-agent-glm5.2-tmux-agents-trajectory/bare-test-001/mitm/thinking_readable.txt

# Tell测试的thinking
cat /data/math-agent-glm5.2-tmux-agents-trajectory/tell-test-001/mitm/thinking_readable.txt

# 对比两个thinking——Tell是否改变了AI的思维方式？
# 关注：
# 1. AI是否采纳了Tell中的思维流程？
# 2. AI的推理路径是否因为Tell而改变？
# 3. bare时AI卡在哪里？Tell后AI是否突破了这个卡点？
# 4. Tell是否只是提供了信息（泄漏答案），还是真正激发了思维力？
```

### 5.4 Tell的三种形态（对应351号§1.5）

**形态1：一句话指示**（适合具体概念层的思维力）
```
【思维引导】
用反证法——假设所有 $|a_i| < 2$，推导矛盾。
```

**形态2：思维流程/步骤引导式**（适合高Level思维力，如上面的例子）
```
【思维引导】
当你面对一个需要"存在某个元素满足条件"的证明时，考虑以下思维流程：
1. 你需要证明的是什么？——存在性证明
2. 存在性证明的常见策略有哪些？——构造法、反证法、极值法
3. 这道题的条件暗示了什么？
4. 如果假设反面，会产生什么矛盾？
5. 考虑用反证法
```

**形态3：抽象标签**（不应使用——指导力低）
```
【思维引导】
考虑对偶思维。
```

---

## 6. 交互模式——运行时注入Tell

如果你不想在题目文件中写Tell，而是想在AI做题过程中**观察AI卡住了再注入Tell**，用交互模式：

### 6.1 启动交互模式

```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id interactive-test-001 \
  --problem-file /tmp/problem-bare.txt \
  --model glm-5-2 \
  --interactive
```

交互模式和普通模式的区别：
- 普通模式（默认）：`devin -p '<prompt>'`——单轮模式，完成后自动退出
- 交互模式（`--interactive`）：`devin -- '<prompt>'`——不自动退出，支持运行时send-keys注入

### 6.2 观察AI的thinking

```bash
# 实时观察thinking
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/interactive-test-001/mitm/thinking_readable.txt
```

### 6.3 在AI卡住时注入Tell

当你观察到AI在thinking中反复尝试某个方向失败（无尽追逐），可以注入Tell：

```bash
# 向tmux session发送Tell
tmux send-keys -t harness-interactive-test-001 "【思维引导】当你反复试同一类方法失败时，考虑诊断这个方法本身是否有效。你当前在用什么方法？这个方法为什么走不通？有没有完全不同的方法？" Enter
```

**注意**：
- **不要在AI思考时频繁发消息**——每次消息都会打断AI的thinking，丢失推理
- 只在AI明显卡住时（如thinking停止增长、AI输出"我不知道"）才注入Tell
- 注入后等待AI重新思考，观察Tell是否改变了AI的思维方式

### 6.4 处理工具批准提示

AI调用exec/write工具时，devin cli会弹出批准提示：

```bash
# 选3（always allow in this dir）——避免后续重复批准
tmux send-keys -t harness-interactive-test-001 "3" Enter

# 对于write工具的批准提示，选2（accept edits mode）
tmux send-keys -t harness-interactive-test-001 "2" Enter
```

---

## 7. 常见问题与处理

### 7.1 Response truncated（输出被截断）

**现象**：AI在thinking阶段花40-50k字符思考，然后在output阶段一次性输出完整证明文本，达到max output token limit被截断。

**根因**：GLM-5.2倾向于"想完所有内容然后一次性输出文本"，不主动调用write/exec工具。

**处理方法**：
1. **预防**：在题目要求中明确"把证明写到proof.md文件中，不要在对话里输出证明内容"
2. **预防**：指令要简短——"只做第一问"比"两问都要做"更容易不触发截断
3. **截断后**：发"continue"可能再次截断。更好做法是杀掉session重新开始
4. **最有效**：让AI先做数值验证（exec工具），验证完后它会自然过渡到调用write工具写证明

### 7.2 Connection lost（连接中断）

**现象**：屏幕显示 `⚠︎ Connection lost, retrying...`

**影响**：thinking内容不持久化在对话历史中。connection lost时正在进行的API请求被中断，thinking内容**完全丢失**。

**处理方法**：
- 无法预防，这是API连接问题
- 重连后AI会重新思考，但推理深度可能降低
- 如果重连后thinking字符数远少于之前，考虑杀掉session重新开始

### 7.3 mitmproxy CA证书问题

**现象**：交互模式出现"Connection failed, retrying..."

**根因**：devin cli是Node.js应用，不读macOS Keychain。需要设置`NODE_EXTRA_CA_CERTS`环境变量。

**处理**：solver-harness已自动处理这个问题（启动时设置`NODE_EXTRA_CA_CERTS=~/.mitmproxy/mitmproxy-ca-cert.pem`）。如果你手动启动devin cli（不通过solver-harness），需要自己设置：

```bash
HTTPS_PROXY=http://localhost:18889 \
HTTP_PROXY=http://localhost:18889 \
NODE_EXTRA_CA_CERTS=~/.mitmproxy/mitmproxy-ca-cert.pem \
devin -p "你的prompt" --model glm-5-2 --respect-workspace-trust false --permission-mode dangerous
```

**但请不要手动启动——始终用solver-harness。**

### 7.4 thinking数据为空

**现象**：`thinking_readable.txt`为空，或`thinking_extractor.py --summary`显示`Steps with thinking: 0`

**可能原因**：
1. mitmproxy没有运行——检查`mitm status`
2. devin cli没有走代理——检查`NODE_EXTRA_CA_CERTS`是否设置
3. 使用了非GLM-5.2模型——其他模型可能没有thinking
4. session还在运行中——sessions.db数据不完整，但MITM数据应该是实时的

### 7.5 tmux session异常退出

**现象**：`tmux list-sessions`看不到`harness-<exp-id>` session

**处理**：
```bash
# 检查实验状态
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py status --exp-id my-test-001

# 如果session已退出但数据已采集，可以只做decode
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py decode-all
```

---

## 8. 批量测试——一次跑多道题

如果你要一次测试多道题（如26种思维力各5道题=130道题），用批量测试模式。

### 8.1 手动批量（简单场景）

```bash
# 循环启动多道题
for i in 1 2 3 4 5; do
  .venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
    --exp-id batch-test-${i} \
    --problem-file /tmp/problem-${i}.txt \
    --model glm-5-2
  sleep 5  # 间隔5秒，避免同时启动太多session
done

# 查看所有实验
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py list

# 逐个停止
for i in 1 2 3 4 5; do
  .venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id batch-test-${i}
done
```

### 8.2 并发注意事项

- **mitmproxy是共享的**——所有实验走同一个mitmproxy（端口18889），不冲突
- **tmux session名必须唯一**——每个实验用不同的exp-id
- **工作目录是隔离的**——每个实验有独立的工作目录和trajectory目录
- **不要同时启动太多**——建议最多4个并发（GLM-5.2的API限速）

---

## 9. 完整示例——从零到完成

### 9.1 场景：测试"同构之桥"思维力

假设你要测试：GLM-5.2在bare条件下做不出来的题，给"同构之桥"Tell后能不能做出来。

```bash
# ========== 第1步：确认mitmproxy运行 ==========
cd ~/master-mind-glm5.2-worktree
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm status

# ========== 第2步：准备bare题目 ==========
cat > /tmp/problem-galois-bare.txt << 'EOF'
你是数学大师。请解答以下数学题。

题目：
证明多项式 $x^5 - 6x + 3$ 在有理数域上没有根式解。

要求：
1. 给出完整的解答过程
2. 数学公式用LaTeX
3. 如果你不知道，明确说"我不知道"
4. 把证明写到proof.md文件中
EOF

# ========== 第3步：启动bare测试 ==========
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id bare-galois-001 \
  --problem-file /tmp/problem-galois-bare.txt \
  --model glm-5-2

# ========== 第4步：实时观察bare thinking ==========
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/bare-galois-001/mitm/thinking_readable.txt

# （观察AI的thinking——看AI是否在数论/求根方法上打转，是否想到Galois理论）

# ========== 第5步：等待bare测试结束 ==========
# 检查AI是否做出来了
ls /data/math-agent-glm5.2-tmux-agents-dir/bare-galois-001/proof*
cat /data/math-agent-glm5.2-tmux-agents-dir/bare-galois-001/proof.md

# 如果bare做出来了→这道题不可用（太简单），换题
# 如果bare做不出来→继续Tell测试

# ========== 第6步：停止bare测试 ==========
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id bare-galois-001

# ========== 第7步：准备Tell题目 ==========
cat > /tmp/problem-galois-tell.txt << 'EOF'
你是数学大师。请解答以下数学题。

题目：
证明多项式 $x^5 - 6x + 3$ 在有理数域上没有根式解。

要求：
1. 给出完整的解答过程
2. 数学公式用LaTeX
3. 如果你不知道，明确说"我不知道"
4. 把证明写到proof.md文件中

【思维引导】
当你面对"多项式没有根式解"这类问题时，考虑以下思维流程：
1. 你当前在什么领域打转？——你可能在使用求根公式或数论方法
2. 这些方法为什么走不通？——五次方程一般没有根式解公式
3. 有没有完全不同的领域可以处理这个问题？——考虑代数结构
4. 多项式的根有什么代数结构？——根的置换群
5. 这个群的结构和根式可解性有什么关系？——群的可解性
6. 如何计算这个多项式的根的置换群？——Galois群
7. 如何判断Galois群是否可解？——分析群的结构
EOF

# ========== 第8步：启动Tell测试 ==========
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id tell-galois-001 \
  --problem-file /tmp/problem-galois-tell.txt \
  --model glm-5-2

# ========== 第9步：实时观察Tell thinking ==========
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/tell-galois-001/mitm/thinking_readable.txt

# （观察AI的thinking——看AI是否采纳了Tell中的思维流程，是否跨域到Galois理论）

# ========== 第10步：停止Tell测试 ==========
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id tell-galois-001

# ========== 第11步：事后提取完整thinking ==========
# bare测试的thinking
.venv/bin/python3 xishujuzhen/thinking_extractor.py \
  --work-dir /data/math-agent-glm5.2-tmux-agents-dir/bare-galois-001 \
  --format markdown \
  -o /tmp/bare-galois-thinking.md

# Tell测试的thinking
.venv/bin/python3 xishujuzhen/thinking_extractor.py \
  --work-dir /data/math-agent-glm5.2-tmux-agents-dir/tell-galois-001 \
  --format markdown \
  -o /tmp/tell-galois-thinking.md

# ========== 第12步：对比分析 ==========
# 读两个thinking文件，对比：
# 1. bare时AI在什么方向上打转？
# 2. Tell后AI是否跨域到Galois理论？
# 3. Tell是激发了思维力还是泄漏了答案？
#    - 如果AI只是照着Tell的步骤做→可能是泄漏
#    - 如果AI在Tell引导下自己探索了更多→可能是激发了思维力
```

---

## 10. 分析thinking的维度

当你拿到thinking数据后，从以下维度分析：

### 10.1 AI的数学识别

- AI识别了什么数学结构？
- AI是否识别了正确的数学领域？
- AI是否意识到这道题需要跨域？

### 10.2 AI的方法尝试

- AI尝试了什么方法？
- AI尝试了几个不同的方法？
- AI是否在错误方法上无尽追逐？

### 10.3 AI的卡点

- AI在哪里停下来？
- AI的thinking中是否提到"不知道下一步该做什么"？
- AI是否意识到自己卡住了？
- AI是否诊断了方法无效并转向？

### 10.4 AI的计算结果

- AI算出了什么数值？
- 数值和正确答案的差距是什么？
- AI是否尝试了从数值到封闭形式的转换？

### 10.5 AI的工具使用

- AI调用了什么工具？（exec/web_search/read/write）
- 工具返回了什么结果？
- AI是否因为工具结果而改变方向？

### 10.6 Tell的影响（Tell测试专有）

- AI是否采纳了Tell中的思维流程？
- AI的推理路径是否因为Tell而改变？
- bare时AI卡在哪里？Tell后AI是否突破了这个卡点？
- Tell是激发了思维力还是泄漏了答案？
  - **泄漏答案的特征**：AI只是照着Tell的步骤做，没有自己的探索
  - **激发思维力的特征**：AI在Tell引导下自己探索了更多，Tell给了方向但AI自己走了路

---

## 11. 挑战类型分类

基于thinking分析，判断这道题对AI的挑战类型：

| 挑战类型 | thinking中的特征 |
|---|---|
| 跨概念推理跳跃 | AI知道A和B但thinking中不知道A→B的路径 |
| 需要非显然构造 | AI的thinking中尝试了直接方法但失败，没有想到构造辅助对象 |
| 多约束联合 | AI的thinking中能处理单个约束但联合时卡住 |
| 领域识别错误 | AI的thinking中用了错误领域的方法 |
| 计算复杂度 | AI知道方法但thinking中提到"计算太复杂/太慢" |
| 封闭形式识别 | AI算出了数值但PSLQ/其他方法找不到封闭形式 |
| 证明结构缺失 | AI的thinking中有思路但无法组织成完整证明 |
| 无尽追逐 | AI反复试同一类方法失败，不诊断方法无效 |
| 跨域失败 | AI在当前领域打转，不考虑跨域 |

---

## 12. 注意事项

### 12.1 thinking的语言

**GLM-5.2的thinking用英文，content用中文**——分析时注意语言差异。thinking是AI的内心独白（英文），content是AI说出来的话（中文）。

### 12.2 不要在AI思考时频繁发消息

每次消息都会打断AI的thinking，丢失推理。只在AI明显卡住时才注入Tell。

### 12.3 session隔离——每次测试创建独立目录

**每次测试都必须用新的exp-id，创建独立的工作目录和trajectory目录。不要复用已有实验的目录。** 详见§2.5。

已有实验的数据不要删除——它们是研究数据，可能需要事后重新分析。

### 12.4 测试目录不在repo内

**Solver的工作目录在`/data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/`，不在repo内。** 不要在repo内创建测试目录——会污染git状态。详见§2.4。

### 12.5 yolo模式自动启用

**solver-harness自动添加`--permission-mode dangerous`和`--respect-workspace-trust false`**——Solver在无人值守模式下运行，所有工具调用自动批准。你不需要手动加这些参数。详见§2.6。

### 12.6 始终用solver-harness

**禁止手动tmux启动、禁止exec后台、禁止nohup、禁止subprocess.run直接调用devin -p。** 手动启动会丢失MITM token级trajectory——这是不可接受的。

### 12.7 mitmproxy是共享的

所有实验走同一个mitmproxy（端口18889），不冲突。stop单个实验不影响mitmproxy系统服务。所有实验结束后才停止mitmproxy：
```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py mitm stop
```

### 12.8 protobuf schema是逆向推断的

MITM拦截的protobuf字段映射通过strings分析+decode_raw推断，可能有误差。如需精确解析，需要获取正式的`.proto`文件。但对于thinking提取来说，field 9的映射已经验证可靠。

---

## 13. 快速参考卡

### 13.1 一句话启动

```bash
cd ~/master-mind-glm5.2-worktree && \
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id <exp-id> --problem-file <problem.txt> --model glm-5-2
```

### 13.2 一句话观察

```bash
tail -f /data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/mitm/thinking_readable.txt
```

### 13.3 一句话停止

```bash
.venv/bin/python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id <exp-id>
```

### 13.4 一句话提取thinking

```bash
.venv/bin/python3 xishujuzhen/thinking_extractor.py \
  --work-dir /data/math-agent-glm5.2-tmux-agents-dir/<exp-id> \
  --format markdown -o /tmp/<exp-id>-thinking.md
```

### 13.5 一句话检查结果

```bash
cat /data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/proof.md
```

---

## 附录A：Solver的AGENTS.md模板

Solver启动时，solver-harness会自动复制AGENTS.md模板到工作目录。模板内容：

**裸跑模板**（`templates/solver_agents_md.md`）：
- 告诉AI它是数学大师Solver角色
- 允许使用exec/read/write/web_search工具
- 禁止搜索题目原文找答案（唯一禁令）
- 要求用LaTeX写证明，写到proof.md

**引导模板**（`templates/solver_agents_md_guided.md`）：
- 在裸跑模板基础上增加动态引导机制
- 要求AI每完成一个推理步骤后读hint.txt
- hint.txt是系统推送的方向提示，不是答案
- AI可以接受、修改或拒绝hint

如果你需要自定义AGENTS.md，可以修改模板文件或在启动后手动修改工作目录中的AGENTS.md。

---

## 附录B：MITM技术细节

### B.1 Connect streaming protobuf格式

GetChatMessage响应是`application/connect+proto`格式：
- 每个envelope: `1 byte flags + 4 bytes length (big-endian) + protobuf message`
- flags bit 1 (0x02) = end-of-stream

### B.2 Protobuf字段映射

| field | 含义 |
|---|---|
| 1 | message_id (string) |
| 2 | timestamp (message: sub-field 1 = seconds, sub-field 2 = nanos) |
| 5 | stop_reason (varint) |
| 6 | tool_call chunk (message) |
| 7 | metadata (message: sub-field 9 = model name) |
| 9 | **content/thinking chunk (string)** — 逐token流式 |
| 12 | sequence number (64bit) |
| 17 | session_id (string) |
| 28 | statistics (token usage等) |

### B.3 流式实时处理机制

mitmproxy的`responseheaders` hook在响应头到达时（body之前）触发，设置`flow.response.stream = callable`。之后每个HTTP chunk到达时，callable被调用，`StreamingThinkingParser`实时解析Connect streaming protobuf，每解析出一个thinking chunk（field 9）立即落盘。

**这是真正的流式实时处理**——不需要等响应完成，Solver思考过程中每个token实时写入文件。

### B.4 四路落盘

| 文件 | 格式 | 用途 |
|---|---|---|
| `_shared/mitm_raw/thinking_live.txt` | token级碎片（全局） | tail -f看所有实验 |
| `<exp_id>/mitm/thinking_live.txt` | token级碎片（按实验隔离） | tail -f看特定实验 |
| `<exp_id>/mitm/thinking_live.jsonl` | JSONL（每chunk一行JSON） | 程序读取 |
| `<exp_id>/mitm/thinking_readable.txt` | **人可阅读的连续文本** | tail -f读文章 |

---

## 如何使用本文档

**给另一个AI时**：
1. 把本文档完整发给另一个AI
2. 告诉它："请阅读这个文档，然后在这台机器上运行观察性测试"
3. 另一个AI需要ssh访问这台机器，或者直接在这台机器上运行

**另一个AI需要做的事**：
1. 按本文档的步骤启动Solver
2. 实时观察thinking
3. 判断AI是否做出来了
4. 对比bare测试和Tell测试的thinking差异
5. 分析Tell是激发了思维力还是泄漏了答案

**注意事项**：
- 另一个AI必须在这台机器上运行（mitmproxy、devin cli都安装在这台机器上）
- 另一个AI必须遵守§12的注意事项——始终用solver-harness，不要手动启动
- 如果另一个AI遇到本文档未覆盖的问题，参考`xishujuzhen/solver_harness/solver_harness.py --help`和`xishujuzhen/thinking_extractor.py --help`
