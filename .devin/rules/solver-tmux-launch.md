---
description: >
  启动数学大师Solver的devin cli实例时，必须通过solver-harness启动，不能用exec后台(timeout=0)或nohup或手动tmux。
  原因：solver-harness自动完成tmux启动+mitmproxy代理+pipe-pane兜底+sessions.db轮询+事后批量解码，
  手动启动会丢失MITM token级trajectory。任何时候启动Solver都必须用solver-harness——裸跑测试、
  GuidedLoop引导、批量测试、DFS回溯实验，无一例外。
  mitmproxy已制作为launchd系统服务（com.aurolafly.mitmproxy-devin），开机自启动，端口18889，
  两个AI共享不冲突。addon脚本在~/.mitmproxy/mitm_proto_capture.py（共享位置）。
  WHEN to use: 任何启动Solver的devin cli实例的场景。
  WHEN NOT to use: 一般命令行操作、非Solver的devin cli调用。
trigger: model_decision
---

# solver-tmux-launch rule

## 硬约束

**启动数学大师Solver的devin cli实例必须通过solver-harness，禁止手动tmux启动、禁止exec后台(timeout=0)、禁止nohup。**

**适用所有场景**：裸跑测试、GuidedLoop引导、批量测试、DFS回溯实验——无一例外。任何场景下启动Solver都必须走solver-harness，确保MITM token级trajectory采集。

## mitmproxy系统服务（2026-08-08建立）

mitmproxy已制作为macOS launchd系统服务，**开机自启动，两个AI共享，不冲突**：

| 属性 | 值 |
|---|---|
| 服务Label | `com.aurolafly.mitmproxy-devin` |
| plist路径 | `~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist` |
| 端口 | **18889**（注意：不是18888，18888被claude-passthrough占用） |
| addon脚本 | `~/.mitmproxy/mitm_proto_capture.py`（共享位置，两个AI共用） |
| 日志 | `~/.mitmproxy/mitm_stdout.log` + `~/.mitmproxy/mitm_stderr.log` |
| 崩溃重启 | `KeepAlive.SuccessfulExit=false`（非正常退出自动重启） |
| 启动时机 | `RunAtLoad=true`（登录时自动启动） |

**管理命令**：
```bash
# 查看状态
launchctl list | grep mitmproxy
python3 xishujuzhen/solver_harness/solver_harness.py mitm status

# 手动启动（如果服务未运行）
launchctl load ~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist

# 手动停止
launchctl unload ~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist

# 崩溃后检查日志
cat ~/.mitmproxy/mitm_stderr.log
```

**addon脚本同步**：当`xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py`更新后，需要同步到共享位置：
```bash
cp xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py ~/.mitmproxy/mitm_proto_capture.py
launchctl unload ~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist
launchctl load ~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist
```

solver-harness的`mitm start`命令会优先检测launchd服务是否运行，如果未运行则尝试`launchctl load`启动它；如果plist不存在则fallback到tmux启动。

## 原因

1. **MITM流式实时trajectory采集（最关键）**：solver-harness通过mitmproxy的`responseheaders` hook + `flow.response.stream = callable`实现token级实时thinking截获。Solver思考过程中每个token立即落盘到4个位置（共享txt + 实验txt + 实验jsonl + 实验readable txt）。手动启动无法采集MITM数据——这是solver-harness存在的核心价值。mitmproxy作为launchd系统服务运行，两个AI共享同一实例，不会互相冲突。
2. **NODE_EXTRA_CA_CERTS关键修复**：devin cli是Node.js应用，不读macOS Keychain，必须通过`NODE_EXTRA_CA_CERTS=~/.mitmproxy/mitmproxy-ca-cert.pem`环境变量指向mitmproxy CA证书，否则交互模式SSL验证失败（"Connection failed, retrying..."）。solver-harness已内置此修复。
3. **`--no-http2`关键修复**：mitmproxy必须加`--no-http2`参数禁用HTTP/2。HTTP/2的连接复用机制在流式响应结束后状态异常，导致第二轮请求无法通过代理发送（266号报告中的"第二轮Connection failed"问题）。强制HTTP/1.1后连接管理可靠，多轮交互正常。launchd plist和tmux fallback都已内置此修复。
4. **审计兜底**：solver-harness自动启动pipe-pane（tmux兜底记录），无需手动启动。
5. **持续观察**：solver-harness用tmux启动，可通过`tmux capture-pane -t harness-<exp-id> -p`持续观察Solver工作过程。
6. **进程安全**：tmux session独立于Devin CLI的shell session，不会被shell session结束而杀掉。
7. **自动回填+db monitor**：solver-harness先回填devin_session_id（等session出现在sessions.db中），再启动db monitor（3秒轮询step级trajectory实时落盘到`sessions_db/trajectory.jsonl`）。顺序很重要——如果db monitor在session出现之前启动，会找不到session而退出。

## 实施规范

### 所有场景统一用solver-harness

```bash
# 1. mitmproxy已作为系统服务自启动——通常不需要手动启动
#    如果需要确认状态：
python3 xishujuzhen/solver_harness/solver_harness.py mitm status

# 2. 启动实验（裸跑测试、GuidedLoop、批量测试都一样）
python3 xishujuzhen/solver_harness/solver_harness.py launch \
  --exp-id <experiment-id> \
  --problem-file <problem.txt路径> \
  --model glm-5-2

# 3. 观察
python3 xishujuzhen/solver_harness/solver_harness.py status --exp-id <experiment-id>
tmux capture-pane -t harness-<experiment-id> -p

# 4. 停止（自动decode-all，不影响共享mitmproxy系统服务）
python3 xishujuzhen/solver_harness/solver_harness.py stop --exp-id <experiment-id>

# 5. 所有实验结束后——不需要停mitmproxy（系统服务常驻）
#    如确需停止：launchctl unload ~/Library/LaunchAgents/com.aurolafly.mitmproxy-devin.plist
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
