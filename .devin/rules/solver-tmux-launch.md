---
description: >
  启动数学大师Solver的devin cli实例时，必须用tmux启动，不能用exec后台或nohup。
  原因：tmux pipe-pane是179号方案中兜底记录devin cli trajectory的手段；
  用tmux启动可以持续观察Solver工作过程；不用tmux进程可能被杀掉导致trajectory丢失。
  WHEN to use: 通过GuidedLoop/DevinCliAdapter启动Solver的devin cli实例时。
  WHEN NOT to use: 一般命令行操作、非Solver的devin cli调用。
trigger: model_decision
---

# solver-tmux-launch rule

## 硬约束

**启动数学大师Solver的devin cli实例必须用tmux，禁止用exec后台(timeout=0)或nohup。**

## 原因

1. **审计兜底**：179号方案定义了三层trajectory记录，其中tmux pipe-pane是兜底手段。如果不用tmux启动，pipe-pane无法工作，兜底记录就断了。
2. **持续观察**：用tmux启动后，可以通过`tmux capture-pane -t <session> -p`持续观察Solver的工作过程，不需要等它结束才知道发生了什么。
3. **进程安全**：tmux session独立于Devin CLI的shell session，不会被shell session结束而杀掉。exec后台模式的进程在session结束时会被杀掉。

## 实施规范

### Solver工作目录选择

**当前模式（2026-08-07起）· tmux-agents-dir**：

每个实验在 `/data/math-agent-glm5.2-tmux-agents-dir/` 下有独立目录，命名规范 `<dev-docs编号>-<实验名>`（如 `255-poc-1`）。目录自包含，运行后保留全部记录。

**旧模式（legacy）· 三固定目录**：`/data/math-agent-glm5.2-{1,2,3}`，仍可用但已废弃。旧模式在run之间清理复用，不保留运行记录。

### 启动Solver的devin cli

**关键参数**：
- `--permission-mode dangerous`：必须加——让exec/web_search等工具自动approve。否则AI想用Python计算时被rejected，只做2步就停，无法观察真实解题能力。
- `--export <PATH>`：每轮自动导出conversation.json（含reasoning_content + tool_calls + observation）
- AGENTS.md中定义搜索纪律：不允许通过搜索获取题目答案/解答，其他内容均可搜索

```bash
# 当前模式：创建实验目录并启动
EXP_DIR="/data/math-agent-glm5.2-tmux-agents-dir/<experiment-id>"
mkdir -p ${EXP_DIR}/exports
cp templates/solver_agents_md.md ${EXP_DIR}/AGENTS.md  # 从模板复制（含搜索纪律）

# 创建tmux session运行GuidedLoop
tmux new-session -d -s solver-<run_id> ".venv/bin/python3 -c '
import sys
sys.path.insert(0, \"xishujuzhen\")
from research_runtime.runtime.guided_loop import GuidedLoop

loop = GuidedLoop(
    run_id=\"<run_id>\",
    run_dir=\"runs/<run_id>\",
    problem=\"<problem>\",
    model=\"glm-5-2\",
    max_turns=3,
    max_hints=2,
    timeout=600,
    work_dir=\"${EXP_DIR}\",
)
result = loop.run()
' 2>&1 | tee runs/<run_id>/tmux.log"
```

### 裸跑测试（不走GuidedLoop）

```bash
# 直接用devin -p测试单道题（用于baseline测试）
WORK_DIR="/data/math-agent-glm5.2-1"  # 或tmux-agents-dir下的实验目录
EXPORT_PATH="runs/<run_id>/conversation.json"

devin -p "请读取当前目录下的problem.txt文件，解答其中的数学题。" \
  --model glm-5-2 \
  --respect-workspace-trust false \
  --permission-mode dangerous \
  --export ${EXPORT_PATH}
```

**注意**：裸跑测试也必须用`--permission-mode dangerous`，否则exec被rejected，无法观察AI真实解题能力。

### 启动pipe-pane兜底记录

```bash
# 当前模式：pipe-pane写入实验目录（自包含）
tmux pipe-pane -t solver-<run_id> "cat >> ${EXP_DIR}/tmux_pipe.log"

# 旧模式：pipe-pane写入runs目录
# tmux pipe-pane -t solver-<run_id> "cat >> runs/<run_id>/tmux_pipe.log"
```

### 观察Solver工作过程

```bash
# 查看当前输出
tmux capture-pane -t solver-<run_id> -p

# 持续观察（实时）
tmux attach -t solver-<run_id>
```

### 检查session状态

```bash
tmux list-sessions | grep solver
```

### 结束session

```bash
# Solver完成后
tmux kill-session -t solver-<run_id>
```

## session命名规范

`solver-<run_id>`，例如：
- `solver-run_20260806_complex_002`
- `solver-run_20260806_guided_005`

## 与DevinCliAdapter的关系

DevinCliAdapter（`runtime/devin_cli_adapter.py`）内部调用`devin -p`，这个调用本身是在Python进程中执行的。tmux session包裹的是整个GuidedLoop Python进程，不是单个devin cli调用。这样：
- tmux记录的是GuidedLoop的全部输出（包括每个turn的日志）
- devin cli的`--export`记录的是每个turn的conversation.json
- sessions.db记录的是devin cli的完整trajectory
- 三层记录互不冲突，互为补充
