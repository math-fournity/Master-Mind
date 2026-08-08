---
name: solver-tmux-launch
description: >
  用tmux启动数学大师Solver的devin cli实例（GuidedLoop），并启动pipe-pane兜底记录。
  包含启动、观察、检查、结束的完整工作流。
  WHEN to use: 需要运行GuidedLoop生成新run时。
  WHEN NOT to use: 一般命令行操作、非Solver的devin cli调用。
---

# solver-tmux-launch skill

## 用途

用tmux启动GuidedLoop，确保：
1. 进程在tmux中运行，不会被shell session结束而杀掉
2. pipe-pane兜底记录可用
3. 可以持续观察Solver工作过程

## 工作流

### 步骤1：准备run目录

```bash
RUN_ID="run_20260806_<描述>"
mkdir -p runs/${RUN_ID}
```

### 步骤2：选择Solver工作目录

三个可用目录，选一个未被占用的：
- `/data/math-agent-glm5.2-1`
- `/data/math-agent-glm5.2-2`
- `/data/math-agent-glm5.2-3`

检查占用：`tmux list-sessions | grep solver`

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
    work_dir=\"/data/math-agent-glm5.2-<n>\",
)
result = loop.run()
print()
print(f\"turns={result.n_turns} hints={result.n_hints} completed={result.completed} session={result.session_id}\")
' 2>&1 | tee runs/${RUN_ID}/tmux.log"
```

### 步骤4：启动pipe-pane兜底记录

```bash
tmux pipe-pane -t solver-${RUN_ID} "cat >> runs/${RUN_ID}/tmux_pipe.log"
```

### 步骤5：观察Solver工作过程

```bash
# 查看当前输出
tmux capture-pane -t solver-${RUN_ID} -p

# 持续观察
tmux attach -t solver-${RUN_ID}
```

### 步骤6：检查是否完成

```bash
# 检查session是否还在
tmux list-sessions | grep solver-${RUN_ID}

# 检查结果文件是否生成
ls runs/${RUN_ID}/guided_loop_result.json
```

### 步骤7：结束后清理

```bash
# Solver完成后
tmux kill-session -t solver-${RUN_ID}
```

## 注意事项

1. **超时设置**：复杂问题用timeout=600（10分钟），简单问题用300
2. **工作目录不冲突**：同时运行多个run时用不同的math-agent-glm5.2-*目录
3. **pipe-pane必须启动**：这是179号方案三层trajectory记录的兜底层
4. **不要用exec后台**：exec的timeout=0后台模式不是tmux，进程会被杀掉
5. **session命名**：`solver-<run_id>`，便于识别和管理
6. **题目通过文件传递，不用-p传长文本**：见下方"题目传递规范"
7. **--permission-mode dangerous必须加**：否则exec/web_search被rejected，AI只做2步就停，无法观察真实解题能力。搜索纪律在AGENTS.md中定义（允许搜通用数学知识，禁止搜题目答案）

## 题目传递规范（铁律）

**`devin -p`只适合短指令（<200字符）。长题目必须写入文件让AI读文件。**

### 原因

`devin -p`的命令行参数有长度限制。当prompt包含完整LaTeX题目（有些题目500-900字符）加上指令模板时，总prompt超过限制后题目在中间被截断，AI收到的题目不完整，直接说"题目被截断了"无法作答。

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

### 用法

```bash
# 交互式模式带导出
devin --model glm-5-2 --export /path/to/export.json

# -p模式也支持
devin -p "prompt" --model glm-5-2 --export /path/to/export.json
```

### 何时使用

1. **GuidedLoop / DFS引导实验**：每个分支的session必须带`--export`，导出文件存放在`runs/<run_id>/exports/session_<timestamp>.json`
2. **批量测试**：每道题的run带`--export`，便于事后审计对话过程
3. **需要trajectory记录的所有场景**：`--export`是devin cli原生支持的对话记录手段，和pipe-pane兜底记录互补

### 与pipe-pane的关系

| 记录手段 | 层次 | 说明 |
|---|---|---|
| `--export` | devin cli原生 | 结构化JSON，每轮自动导出，包含完整对话内容 |
| `pipe-pane` | tmux兜底 | 纯文本terminal输出，捕获所有屏幕内容包括非对话部分 |

两者互补：`--export`提供结构化数据，`pipe-pane`提供完整terminal记录。

### DFS引导中的使用（214号8.9节）

DFS回溯时每条分支启动新session，每个session使用独立的export文件：

```python
export_path = f"{EXPORT_DIR}/session_{int(time.time())}.json"
cmd = f"devin --model glm-5-2 --export {export_path}"
# 启动新tmux session
tmux new-session -d -s guided-exp-1 "cd {work_dir} && {cmd}"
```

回溯后重放Q序列时，新session使用新的export文件，不会和旧分支的导出混淆。
