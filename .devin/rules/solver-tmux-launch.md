---
description: >
  启动数学大师Solver的devin cli实例时，必须通过solver-harness启动，不能用exec后台(timeout=0)或nohup或手动tmux。
  原因：solver-harness自动完成tmux启动+mitmproxy代理+pipe-pane兜底+sessions.db轮询+事后批量解码，
  手动启动会丢失MITM token级trajectory。任何时候启动Solver都必须用solver-harness——裸跑测试、
  GuidedLoop引导、批量测试、DFS回溯实验，无一例外。
  WHEN to use: 任何启动Solver的devin cli实例的场景。
  WHEN NOT to use: 一般命令行操作、非Solver的devin cli调用。
trigger: model_decision
---

# solver-tmux-launch rule

## 硬约束

**启动数学大师Solver的devin cli实例必须通过solver-harness，禁止手动tmux启动、禁止exec后台(timeout=0)、禁止nohup。**

**适用所有场景**：裸跑测试、GuidedLoop引导、批量测试、DFS回溯实验——无一例外。任何场景下启动Solver都必须走solver-harness，确保MITM token级trajectory采集。

## 原因

1. **MITM trajectory采集（最关键）**：solver-harness通过mitmproxy代理捕获GetChatMessage的raw protobuf响应，解码出token级thinking+tool_calls数据。手动启动无法采集MITM数据——这是solver-harness存在的核心价值。
2. **NODE_EXTRA_CA_CERTS关键修复**：devin cli是Node.js应用，不读macOS Keychain，必须通过`NODE_EXTRA_CA_CERTS=~/.mitmproxy/mitmproxy-ca-cert.pem`环境变量指向mitmproxy CA证书，否则交互模式SSL验证失败（"Connection failed, retrying..."）。solver-harness已内置此修复。
3. **审计兜底**：solver-harness自动启动pipe-pane（tmux兜底记录），无需手动启动。
4. **持续观察**：solver-harness用tmux启动，可通过`tmux capture-pane -t harness-<exp-id> -p`持续观察Solver工作过程。
5. **进程安全**：tmux session独立于Devin CLI的shell session，不会被shell session结束而杀掉。
6. **自动回填**：solver-harness自动回填devin_session_id，自动启动sessions.db轮询，自动在stop时decode-all。

## 实施规范

### 所有场景统一用solver-harness

```bash
# 1. 启动共享mitmproxy（全局，只需启动一次）
python3 xishujuzhen/solver_harness/solver_harness.py mitm start

# 2. 启动实验（裸跑测试、GuidedLoop、批量测试都一样）
python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id <experiment-id> \
  --problem-file <problem.txt路径> \
  --model glm-5-2

# 3. 观察
python3 xishujuzhen/solver_harness/solver_harness.py status --exp-id <experiment-id>
tmux capture-pane -t harness-<experiment-id> -p

# 4. 停止（自动decode-all，不影响共享mitmproxy）
python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id <experiment-id>

# 5. 所有实验结束后停止mitmproxy
python3 xishujuzhen/solver_harness/solver_harness.py mitm stop
```

### GuidedLoop集成

GuidedLoop引导实验也必须通过solver-harness启动。当前solver-harness的`launch`命令支持`--prompt`自定义prompt，可用于GuidedLoop的单轮启动。多轮引导的集成方式：
- 每轮用solver-harness launch启动新实验（exp-id带轮次后缀，如`guided-006-turn1`）
- 或扩展solver-harness支持多轮模式（未来工作）

**无论如何集成，每轮都必须走mitmproxy代理**——这是硬约束，不可妥协。

### Solver工作目录

solver-harness自动创建`/data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/`，自动复制AGENTS.md模板和problem.txt。无需手动创建。

## 禁止的做法

- ❌ 手动`tmux new-session -d -s solver-xxx "devin -p ..."`——丢失MITM数据
- ❌ `exec`后台`timeout=0`运行devin cli——进程会被杀掉，丢失所有trajectory
- ❌ `nohup devin -p ... &`——同上
- ❌ GuidedLoop内部直接调用`devin -p`不走代理——丢失MITM数据

## 详见

skill: `solver-tmux-launch`的完整工作流和注意事项。
