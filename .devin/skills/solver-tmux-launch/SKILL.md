---
name: solver-tmux-launch
description: >
  通过solver-harness启动数学大师Solver的devin cli实例，自动采集完整trajectory（MITM token级+sessions.db step级+pipe-pane兜底+--export）。
  所有场景（裸跑测试、GuidedLoop引导、批量测试、DFS回溯）统一用solver-harness。
  WHEN to use: 任何需要运行Solver做题的场景。
  WHEN NOT to use: 一般命令行操作、非Solver的devin cli调用。
---

# solver-tmux-launch skill

## 硬约束

**所有场景启动Solver都必须用solver-harness，禁止手动tmux、禁止exec后台、禁止nohup。**

solver-harness自动完成：tmux启动 + mitmproxy代理 + pipe-pane兜底 + sessions.db轮询 + devin_session_id回填 + 事后批量解码。手动启动会丢失MITM token级trajectory——这是不可接受的。

## 前置条件

- mitmproxy已安装（`brew install mitmproxy`）
- mitmproxy CA证书已生成（`~/.mitmproxy/mitmproxy-ca-cert.pem`，运行过一次mitmdump即可生成）
- solver-harness脚本存在（`xishujuzhen/solver_harness/solver_harness.py`）

## NODE_EXTRA_CA_CERTS关键修复（2026-08-08验证）

**devin cli是Node.js应用，不读macOS Keychain。** 如果只把mitmproxy CA证书加入Keychain，devin cli仍然SSL验证失败——交互模式出现"Connection failed, retrying..."，Solver无法工作。

**修复**：solver-harness在启动devin cli时设置`NODE_EXTRA_CA_CERTS=~/.mitmproxy/mitmproxy-ca-cert.pem`环境变量，让Node.js直接读取CA证书。

```python
# solver_harness.py中的关键代码（mitm_enabled时）
ca_cert_path = os.path.expanduser("~/.mitmproxy/mitmproxy-ca-cert.pem")
env_prefix = (
    f"HTTPS_PROXY=http://localhost:{MITM_PORT} "
    f"HTTP_PROXY=http://localhost:{MITM_PORT} "
    f"NODE_EXTRA_CA_CERTS={ca_cert_path} "
)
```

**已验证**：mitmproxy + NODE_EXTRA_CA_CERTS + 交互模式 = Solver正常工作，mitmproxy成功截获thinking内容。

**不要删除这个环境变量**——没有它，mitmproxy+交互模式就不工作。`--no-mitm`是唯一不需要它的模式，但那样会丢失MITM trajectory。

## 完整工作流

### 步骤1：启动共享mitmproxy（全局，只需启动一次）

```bash
python3 xishujuzhen/solver_harness/solver_harness.py mitm start
```

- 固定端口18888，`--allow-hosts`限制只拦截3个devin host（不影响其他本地应用）
- CA证书自动加入Keychain信任（首次需要密码）
- tmux session名：`harness-mitmproxy`
- raw数据写入：`/data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/`

### 步骤2：启动实验

```bash
python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id <experiment-id> \
  --problem-file <problem.txt路径> \
  --model glm-5-2
```

**可选参数**：
- `--prompt "自定义prompt"`：默认是"请读取当前目录下的problem.txt文件，解答其中的数学题。"
- `--no-mitm`：不启用MITM代理（仅特殊调试场景，正常使用不要加）

自动完成：
1. 创建Solver工作目录（`/data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/`）
2. 创建Trajectory数据目录（`/data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/`）
3. 复制AGENTS.md模板到Solver目录
4. 复制problem.txt到Solver目录
5. 写session_info.json
6. 启动sessions.db轮询进程（step级trajectory）
7. 启动devin cli in tmux（走mitmproxy代理）
8. 启动pipe-pane兜底记录
9. 回填devin_session_id（从sessions.db查找）

### 步骤3：观察Solver工作过程

```bash
# 查看tmux session输出
tmux capture-pane -t harness-<exp-id> -p

# 持续观察
tmux attach -t harness-<exp-id>

# 查看实验状态
python3 xishujuzhen/solver_harness/solver_harness.py status --exp-id <exp-id>
```

### 步骤4：停止实验（自动decode-all）

```bash
python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id <exp-id>
```

自动完成：
1. 停止该实验的tmux sessions（devin cli + db monitor，**不影响共享mitmproxy**）
2. 调用decode-all：扫描共享raw目录，通过_req文件中的work_dir匹配实验，解码分发到`<exp-id>/mitm/trajectory.jsonl`

**可选**：`--no-decode`跳过自动解码（仅特殊场景，正常使用不要加）

### 步骤5（可选）：手动decode-all和list

```bash
# 解码所有共享raw数据（按work_dir分发到各实验）
python3 xishujuzhen/solver_harness/solver_harness.py decode-all

# 列出所有实验
python3 xishujuzhen/solver_harness/solver_harness.py list

# 查看mitmproxy状态
python3 xishujuzhen/solver_harness/solver_harness.py mitm status
```

### 步骤6：停止共享mitmproxy（所有实验结束后）

```bash
python3 xishujuzhen/solver_harness/solver_harness.py mitm stop
```

## 数据产物

```
/data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/
├── session_info.json          # 实验元信息（含devin_session_id）
├── mitm/
│   └── trajectory.jsonl       # token级（MITM解码后，stop时自动生成）
├── sessions_db/
│   └── trajectory.jsonl       # step级（db monitor实时轮询）
├── tmux/
│   ├── tmux.log               # tee输出
│   └── tmux_pipe.log          # pipe-pane兜底
└── exports/
    └── conversation.json      # devin cli --export
```

## 各场景的exp-id命名规范

| 场景 | exp-id格式 | 示例 |
|---|---|---|
| 裸跑测试 | `<dev-docs编号>-<描述>` | `258-matrix-test` |
| GuidedLoop单轮 | `guided-<NNN>-turn<N>` | `guided-006-turn1` |
| 批量测试 | `batch-<批次名>-<题号>` | `batch-imo2025-p5` |
| DFS回溯 | `dfs-<run_id>-branch<N>` | `dfs-run001-branch2` |

## GuidedLoop集成

GuidedLoop引导实验也必须通过solver-harness启动。当前`launch`命令支持`--prompt`自定义prompt。

**多轮引导的两种集成方式**：

1. **每轮独立launch**（当前可用）：每轮用solver-harness launch启动新实验，exp-id带轮次后缀（如`guided-006-turn1`、`guided-006-turn2`）。每轮独立采集trajectory，stop后自动decode-all。

2. **扩展solver-harness多轮模式**（未来工作）：在solver-harness中增加`launch-guided`命令，内部管理多轮devin cli调用，共享同一个mitmproxy session。

**无论哪种方式，每轮都必须走mitmproxy代理**——这是硬约束。

## 注意事项

1. **--permission-mode dangerous自动添加**：solver-harness的launch命令已内置此参数，无需手动加
2. **题目通过文件传递**：`devin -p`只适合短指令（<200字符），长题目写入problem.txt让AI读文件（solver-harness自动复制problem.txt到Solver目录）
3. **共享mitmproxy**：全局单实例，固定18888端口，所有实验共享。stop单个实验不影响mitmproxy
4. **session命名**：solver-harness用`harness-<exp-id>`，mitmproxy用`harness-mitmproxy`，db monitor用`harness-dbmon-<exp-id>`

## 题目传递规范（铁律）

**`devin -p`只适合短指令（<200字符）。长题目必须写入文件让AI读文件。**

### 原因

`devin -p`的命令行参数有长度限制。当prompt包含完整LaTeX题目（有些题目500-900字符）加上指令模板时，总prompt超过限制后题目在中间被截断。

### 正确做法

solver-harness的`--problem-file`参数自动处理：把problem.txt复制到Solver目录，devin cli的prompt是"请读取当前目录下的problem.txt文件，解答其中的数学题。"——短指令，不会截断。

如果题目内容需要自定义格式，在传入`--problem-file`前把内容写入文件：

```python
# 准备problem.txt
problem_file = "/tmp/problem.txt"
with open(problem_file, "w") as f:
    f.write(f"""你是数学大师。请解答以下竞赛数学题。

题目（{pid}）：
{problem_text}

要求：
1. 给出完整的解答过程
2. 最终答案用\\boxed{{答案}}格式给出
3. 数学公式用LaTeX
4. 如果你不知道，明确说"我不知道"
""")

# 用solver-harness启动
subprocess.run([
    "python3", "xishujuzhen/solver_harness/solver_harness.py",
    "launch",
    "--exp-id", exp_id,
    "--problem-file", problem_file,
    "--model", "glm-5-2",
])
```

### hint传递（GuidedLoop多轮）

多turn引导时，hint也写入文件，用`--prompt`指定读hint文件：

```bash
python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id guided-006-turn2 \
  --problem-file /tmp/hint.txt \
  --prompt "请读取当前目录下的problem.txt文件，这是对你上一轮解答的提示，请继续解答。" \
  --model glm-5-2
```

### 批量测试中的清理

每道题运行前必须清理work_dir下的problem.txt/hint.txt，防止下一题读到上一题的文件（session隔离铁律，见`batch-test-session-isolation` rule）。solver-harness每次launch创建独立exp-id目录，天然隔离。

## 对话导出规范（--export）

solver-harness自动添加`--export`参数，导出到`<exp-id>/exports/conversation.json`。

### 三层trajectory记录

| 记录手段 | 层次 | 说明 | 自动采集 |
|---|---|---|---|
| MITM（solver-harness专属） | 网络层 | raw protobuf解码，token级thinking+tool_calls。截获所有ApiServerService API（不只是GetChatMessage） | ✅ stop时自动decode-all |
| `--export` | devin cli原生 | 结构化JSON，每轮自动导出，包含完整对话内容 | ✅ launch时自动添加 |
| `pipe-pane` | tmux兜底 | 纯文本terminal输出，捕获所有屏幕内容包括非对话部分 | ✅ launch时自动启动 |

三者互补：MITM提供token级流式数据，`--export`提供结构化数据，`pipe-pane`提供完整terminal记录。

### MITM数据产物

```
/data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/mitm/
├── thinking_live.jsonl          # 流式实时thinking（每个chunk一行，JSONL格式）
├── thinking_live.txt            # 流式实时thinking（人类可读，可tail -f）
└── trajectory.jsonl             # stop时decode-all生成的完整trajectory

/data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/
├── thinking_live.txt            # 所有实验的thinking流（可tail -f实时查看）
├── capture.log                  # 截获日志（每个文件的URL/大小/时间）
├── api_log.txt                  # 所有API调用记录（URL/状态/大小/时间）
├── chatmsg_NNN_HHMMSS.bin       # raw protobuf响应
└── chatmsg_NNN_HHMMSS_req.bin   # raw protobuf请求
```

### 流式实时thinking机制（2026-08-08建立）

**核心原理**：mitmproxy的`responseheaders` hook在响应头到达时（body之前）触发，设置`flow.response.stream = callable`。之后每个HTTP chunk到达时，callable被调用，实时解析Connect streaming protobuf，每解析出一个thinking chunk（field 9）立即落盘。

**这是真正的流式实时处理**——不需要等响应完成，Solver思考过程中每个token实时写入文件。

**三路落盘**：
1. `_shared/mitm_raw/thinking_live.txt`：所有实验的thinking流（可`tail -f`实时查看）
2. `<exp_id>/mitm/thinking_live.txt`：按实验隔离的人类可读格式（可`tail -f`）
3. `<exp_id>/mitm/thinking_live.jsonl`：JSONL格式，每个chunk一行（含timestamp/chunk_index/content）

**验证数据**：120秒内11,397行txt + 10,971行jsonl，chunk粒度1-7字符/token，毫秒级时间戳。

**mitmproxy截获范围**：所有`ApiServerService` API（GetChatMessage/GetCliModelConfigs/GetUserStatus等），排除seat_management和product_analytics。GetChatMessage走流式处理，其他API走完整响应处理。
