# Solver Harness 操作手册

> 本文件记录 solver harness 系统的正确操作流程，特别是停止流程。
> 实际代码在 `xishujuzhen/solver_harness/pipe/` 下。

---

## 停止系统：必须用 pipe_stop.sh，不要直接 kill tmux session

### 教训（2026-08-18）

曾经犯过的错误：直接 `tmux kill-session -t pipe-runner` 等逐个 kill pipe-* session。

**为什么错了**：

1. pipe 系统的 5 个服务（feeder/runner/collector/reporter/retry）都包在
   `while true; do ...; sleep 5; done` 无限循环里——直接 kill python 进程，
   5 秒后会被重启。必须 kill 整个 tmux session 才能真正停止。
2. 但直接 kill tmux session 绕过了 `pipe_stop.sh` 的设计——
   **collector 被一起 kill 了**，导致正在跑的 solver 跑完后没有服务判定终态，
   status 卡在 `running`，需要下次启动时 `recover_from_crash.py` 处理。

### 正确的停止流程（两步优雅停止）

```bash
# 第一步：优雅停止——停 feeder/runner/reporter/retry/monitor，保留 collector
bash xishujuzhen/solver_harness/pipe/pipe_stop.sh

# 第二步：等 running=0 后收尾——停 collector + watchdog
bash xishujuzhen/solver_harness/pipe/pipe_stop.sh --finish
```

**为什么分两步**：collector 被停后，正在做的题完成后没有服务判定终态，
status 卡在 running。保留 collector 直到所有题自然完成，才是优雅停止。

### pipe_stop.sh 的 4 种模式

| 模式 | 命令 | 行为 | 适用场景 |
|---|---|---|---|
| 优雅停止（默认） | `pipe_stop.sh` | 停 feeder/runner/reporter/retry/monitor，保留 collector | 正常停止，想让正在跑的题自然完成并正确判定终态 |
| 收尾 | `pipe_stop.sh --finish` | 检查 running=0 后停 collector + watchdog | 优雅停止后的第二步 |
| 立即停止 | `pipe_stop.sh --force` | 停所有服务（含 collector），harness session 自然完成 | 紧急停止，不在意终态判定（下次启动时 recover 处理） |
| 强制 kill | `pipe_stop.sh --kill` | 停所有服务 + kill 所有 harness session | 立即中断所有正在做的题 |

### 选择指南

- **正常情况**：用两步优雅停止（默认 + --finish）
- **紧急情况但不想丢题**：用 --force（harness session 自然完成，终态下次 recover）
- **紧急情况且愿意丢题**：用 --kill（强制中断所有题）

### 绝对不要做的

- **不要直接 `tmux kill-session -t pipe-*`**——绕过了 pipe_stop.sh 的设计，
  collector 会被误杀，导致正在跑的题终态无法判定
- **不要只 kill python 进程**——外层 `while true` 循环会 5 秒后重启它
- **不要 kill harness-p* session**（除非用 --kill 模式）——
  这些是正在做题的 solver，应该让它们自然完成
- **不要在有 launchd watchdog 时只 kill tmux session**——
  watchdog 会在 30 秒内把所有被 kill 的 session 重新拉起。
  必须先 `launchctl unload plist` 停 watchdog，再 `pipe_stop.sh`

### launchd watchdog（2026-08-18 已移除）

曾经有 launchd watchdog（`com.aurolafly.pipe-watchdog.plist`）自动守护
5 个 pipe session，死了就重启。2026-08-18 用户决定 solver 系统不进入 launchd：

- plist 文件已删除（`~/Library/LaunchAgents/com.aurolafly.pipe-watchdog.plist`）
- `pipe_start.sh` 第 6 步已改为不安装 launchd
- 如需 watchdog，手动运行：`bash pipe_watchdog.sh`（前台运行，Ctrl-C 停止）

---

## 启动系统

```bash
bash xishujuzhen/solver_harness/pipe/pipe_start.sh
```

---

## 系统架构简述

pipe 系统由 5 个 tmux session 组成，各自独立运行：

| session | 脚本 | 职责 |
|---|---|---|
| pipe-feeder | `feeder.py` | 从题库喂题到 pending 队列（低水位补充） |
| pipe-runner | `runner.py` | 从 pending 取题，启动 devin cli solver（harness-p* session） |
| pipe-collector | `collector.py` | 监控 running 题的终态，判定 solved/failed |
| pipe-reporter | `reporter.py` | 定期输出统计报告 |
| pipe-retry | `retry_infrastructure.py` | 重试基础设施失败的题（不重试模型能力失败） |

每个 session 内部是 `while true; do python xxx.py; sleep 5; done` 循环——
脚本退出后自动重启。`pipe_stop.sh` 通过 `tmux send-keys C-c` 发送 SIGINT，
触发 `graceful_shutdown.py` 的优雅退出机制（设置 stop_flag，完成当前操作后退出），
然后 kill tmux session 防止 while true 重启。

harness-p* session 是 runner 启动的独立 solver session（每个题一个），
它们不受 pipe-* session 控制，自然完成后由 collector 判定终态。
