#!/bin/bash
# stop-master.sh —— 停止 Master 的 tmux session
#
# Master 是一个 Devin session，运行在 tmux 中。
# 停止 Master = 关闭 tmux session。
# tmux kill-session 会发送 SIGHUP 给 tmux 中的进程，devin CLI 会退出。

set -euo pipefail

TMUX_SESSION="master-math"

if tmux has-session -t "${TMUX_SESSION}" 2>/dev/null; then
    echo "停止 tmux session: ${TMUX_SESSION}..."
    tmux kill-session -t "${TMUX_SESSION}" || true
    echo "Master 已停止。"
else
    echo "Master tmux session 不存在。"
fi
