---
name: solver-tmux-launch
description: >
  启动数学大师Solver的devin cli实例。两种路径：裸跑测试用solver-harness（推荐，自动采集MITM trajectory），GuidedLoop引导用手动tmux启动。
  WHEN to use: 需要运行Solver做题时（裸跑测试或GuidedLoop引导）。
  WHEN NOT to use: 一般命令行操作、非Solver的devin cli调用。
---

# solver-tmux-launch skill

## 两种启动路径

| 场景 | 路径 | 工具 | trajectory采集 |
|---|---|---|---|
| 裸跑测试（直接让AI做题） | A | solver-harness | MITM token级 + sessions.db step级 + pipe-pane兜底 + --export |
| GuidedLoop引导（多轮提示） | B | 手动tmux | pipe-pane兜底 + --export（无MITM） |

---

## 路径A：裸跑测试（solver-harness）

### 何时用

- baseline测试（测AI裸能力）
- 单道题测试
- 需要完整trajectory采集（含token级thinking）的所有场景

### 前置条件

- mitmproxy已安装（`brew install mitmproxy`）
- mitmproxy CA证书已生成（`~/.mitmproxy/mitmproxy-ca-cert.pem`，运行过一次mitmdump即可生成）
- solver-harness脚本存在（`xishujuzhen/solver_harness/solver_harness.py`）

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

### 步骤5（可选）：手动decode-all

```bash
# 解码所有共享raw数据（按work_dir分发到各实验）
python3 xishujuzhen/solver_harness/solver_harness.py decode-all

# 列出所有实验
python3 xishujuzhen/solver_harness/solver_harness.py list
```

### 步骤6：停止共享mitmproxy（所有实验结束后）

```bash
python3 xishujuzhen/solver_harness/solver_harness.py mitm stop
```

### 数据产物

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

---

## 路径B：GuidedLoop引导（手动tmux）

### 何时用

- GuidedLoop多轮引导实验
- DFS回溯实验
- 需要Python进程控制devin cli调用序列的场景

### 步骤1：准备run目录

```bash
RUN_ID="run_20260806_<描述>"
mkdir -p runs/${RUN_ID}
```

### 步骤2：选择Solver工作目录

在`/data/math-agent-glm5.2-tmux-agents-dir/`下创建实验目录：

```bash
EXP_DIR="/data/math-agent-glm5.2-tmux-agents-dir/<experiment-id>"
mkdir -p ${EXP_DIR}/exports
cp templates/solver_agents_md.md ${EXP_DIR}/AGENTS.md
```

### 步骤3：用tmux启动GuidedLoop

```bash
tmux new-session -d -s solver-${RUN_ID} ".venv/bin/python3 -c '
import sys
sys.path.insert(0, \"xishujuzhen\")
from research_runtime.runtime.guided_loop import GuidedLoop

loop = GuidedLoop(
    run_id=\"${RUN_ID}\",
    run_dir=\"runs/${RUN_ID}\",
    problem=\"<问题文本>\",
    model=\"glm-5-2\",
    max_turns=3,
    max_hints=2,
    timeout=600,
    work_dir=\"${EXP_DIR}\",
)
result = loop.run()
print()
print(f\"turns={result.n_turns} hints={result.n_hints} completed={result.completed} session={result.session_id}\")
' 2>&1 | tee runs/${RUN_ID}/tmux.log"
```

### 步骤4：启动pipe-pane兜底记录

```bash
tmux pipe-pane -t solver-${RUN_ID} "cat >> ${EXP_DIR}/tmux_pipe.log"
```

### 步骤5：观察Solver工作过程

```bash
tmux capture-pane -t solver-${RUN_ID} -p
tmux attach -t solver-${RUN_ID}
```

### 步骤6：结束后清理

```bash
tmux kill-session -t solver-${RUN_ID}
```

---

## 通用注意事项

1. **--permission-mode dangerous必须加**：否则exec/web_search被rejected，AI只做2步就停，无法观察真实解题能力
2. **题目通过文件传递**：`devin -p`只适合短指令（<200字符），长题目写入problem.txt让AI读文件
3. **pipe-pane必须启动**：179号方案三层trajectory记录的兜底层
4. **不要用exec后台**：exec的timeout=0后台模式不是tmux，进程会被杀掉
5. **session命名**：solver-harness用`harness-<exp-id>`，手动GuidedLoop用`solver-<run_id>`
6. **solver-harness的共享mitmproxy**：全局单实例，固定18888端口，所有实验共享。stop单个实验不影响mitmproxy

## 题目传递规范（铁律）

**`devin -p`只适合短指令（<200字符）。长题目必须写入文件让AI读文件。**

### 原因

`devin -p`的命令行参数有长度限制。当prompt包含完整LaTeX题目（有些题目500-900字符）加上指令模板时，总prompt超过限制后题目在中间被截断。

### 正确做法

```python
# 1. 把完整题目+指令写入work_dir下的problem.txt
problem_file = os.path.join(work_dir, "problem.txt")
with open(problem_file, "w") as f:
    f.write(f"""你是数学大师。请解答以下竞赛数学题。

题目（{pid}）：
{problem_text}

要求：
1. 给出完整的解答过程
2. 最终答案用\\boxed{{答案}}格式给出
3. 数学公式用LaTeX
4. 如果你不知道，明确说"我不知道"
5. 可以搜索任何内容，但不允许通过搜索获取这道题的答案或解答（不能搜题目原文/题号）
""")

# 2. devin -p只传短指令："请读取当前目录下的problem.txt并解答"
cmd = ["devin", "-p", "请读取当前目录下的problem.txt文件，解答其中的数学题。", "--model", model, ...]

# 3. 运行前清理problem.txt（session隔离铁律）
# 4. 运行后清理problem.txt
```

### hint传递同理

多turn引导时，hint也写入文件：
```python
hint_file = os.path.join(work_dir, "hint.txt")
with open(hint_file, "w") as f:
    f.write(hint_text)
cmd = ["devin", "-p", "请读取当前目录下的hint.txt文件，这是对你上一轮解答的提示，请继续解答。", ...]
```

### 批量测试中的清理

每道题运行前必须清理work_dir下的problem.txt/hint.txt，防止下一题读到上一题的文件（session隔离铁律，见`batch-test-session-isolation` rule）。

## 对话导出规范（--export）

**devin cli支持`--export <PATH>`参数，在每轮对话后自动导出对话记录到JSON文件。**

### 与pipe-pane的关系

| 记录手段 | 层次 | 说明 |
|---|---|---|
| `--export` | devin cli原生 | 结构化JSON，每轮自动导出，包含完整对话内容 |
| `pipe-pane` | tmux兜底 | 纯文本terminal输出，捕获所有屏幕内容包括非对话部分 |
| MITM（solver-harness专属） | 网络层 | raw protobuf解码，token级thinking+tool_calls |

三者互补：`--export`提供结构化数据，`pipe-pane`提供完整terminal记录，MITM提供token级流式数据。
