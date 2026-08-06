#!/bin/bash
# enter-master.sh —— 重新进入已运行的 Master tmux session

TMUX_SESSION="master-math"

if ! tmux has-session -t "${TMUX_SESSION}" 2>/dev/null; then
    echo "Master tmux session 不存在，请先运行 ./scripts/start-master.sh" >&2
    exit 1
fi

exec tmux attach -t "${TMUX_SESSION}"
