---
description: >
  启动数学大师Solver的devin cli实例时，必须用tmux启动，不能用exec后台(timeout=0)或nohup。
  原因：tmux pipe-pane是179号方案中兜底记录devin cli trajectory的手段；
  用tmux启动可以持续观察Solver工作过程；不用tmux进程可能被杀掉导致trajectory丢失。
  WHEN to use: 通过GuidedLoop/DevinCliAdapter启动Solver，或裸跑测试时。
  WHEN NOT to use: 一般命令行操作、非Solver的devin cli调用。
trigger: model_decision
---

# solver-tmux-launch rule

## 硬约束

**启动数学大师Solver的devin cli实例必须用tmux，不能用exec后台(timeout=0)或nohup。**

## 两种启动路径（按场景选择）

### 路径A：裸跑测试 → 用solver-harness（推荐）

**裸跑测试**（不走GuidedLoop，直接让AI做题）**必须用solver-harness**，不要手动启动tmux。

solver-harness自动完成：tmux启动 + mitmproxy代理 + pipe-pane兜底 + sessions.db轮询 + devin_session_id回填 + 事后批量解码。手动启动会丢失MITM token级trajectory。

```bash
# 启动mitmproxy（全局共享，只需启动一次）
python3 xishujuzhen/solver_harness/solver_harness.py mitm start

# 启动实验
python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id <experiment-id> \
  --problem-file <problem.txt路径> \
  --model glm-5-2

# 查看状态
python3 xishujuzhen/solver_harness/solver_harness.py status --exp-id <experiment-id>

# 停止实验（自动decode-all）
python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id <experiment-id>
```

详见skill: `solver-tmux-launch`的"裸跑测试（solver-harness）"章节。

### 路径B：GuidedLoop引导 → 手动tmux启动（暂不集成solver-harness）

**GuidedLoop引导实验**目前仍用手动tmux启动，因为solver-harness和GuidedLoop的集成已确认独立使用（先验证裸跑trajectory采集可靠，再考虑集成）。

手动启动流程见skill: `solver-tmux-launch`的"GuidedLoop引导（手动tmux）"章节。

## 原因

1. **审计兜底**：179号方案定义了三层trajectory记录，其中tmux pipe-pane是兜底手段。solver-harness自动启动pipe-pane；手动启动GuidedLoop时需手动启动pipe-pane。
2. **持续观察**：用tmux启动后，可以通过`tmux capture-pane -t <session> -p`持续观察Solver的工作过程。
3. **进程安全**：tmux session独立于Devin CLI的shell session，不会被shell session结束而杀掉。
4. **MITM trajectory采集（solver-harness专属）**：solver-harness通过mitmproxy代理捕获GetChatMessage的raw protobuf响应，解码出token级thinking+tool_calls数据。手动启动无法采集MITM数据。

## Solver工作目录

**solver-harness模式**：自动创建`/data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/`，自动复制AGENTS.md模板和problem.txt。

**手动GuidedLoop模式**：在`/data/math-agent-glm5.2-tmux-agents-dir/`下手动创建实验目录，或用旧三固定目录`/data/math-agent-glm5.2-{1,2,3}`（已废弃）。
