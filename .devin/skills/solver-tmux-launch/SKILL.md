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
