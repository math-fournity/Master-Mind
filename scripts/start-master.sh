#!/bin/bash
# start-master.sh —— 一键启动 Master Agent 的 Devin session
#
# 行为：
# 1. 用户到 Master 目录运行本脚本
# 2. 创建 tmux session "master-math"
# 3. 在 tmux 中启动 devin CLI（工作目录为 Master 目录）
# 4. devin 启动时，.devin/hooks.v1.json 的 SessionStart hook 注入工作系统认知
# 5. attach 到 tmux session，让用户进入
#
# 为什么用 tmux：
# - Supervisor Agent 通过 tmux 监控 Master（tmux capture-pane 读取输出）
# - Supervisor 通过 tmux send-keys 给 Master 发送反思提示
# - tmux session 持久存在，AI 连接断开后不丢失工作状态
#
# 停止方式：
# - 按 Ctrl+C 退出 devin CLI（tmux session 保留）
# - 或关闭 tmux session: ./scripts/stop-master.sh

set -euo pipefail

MASTER_DIR="~/master-mind-glm5.2-worktree"
TMUX_SESSION="master-math"

cd "${MASTER_DIR}"

# 检查 tmux 是否安装
if ! command -v tmux &>/dev/null; then
    echo "错误：未找到 tmux，请先安装 tmux。" >&2
    exit 1
fi

# 检查 devin 是否安装
if ! command -v devin &>/dev/null; then
    echo "错误：未找到 devin CLI，请先安装。" >&2
    exit 1
fi

# 如果 session 已存在，直接 attach
if tmux has-session -t "${TMUX_SESSION}" 2>/dev/null; then
    echo "Master tmux session 已存在，attach 中..."
    exec tmux attach -t "${TMUX_SESSION}"
fi

# 创建 tmux session
tmux new-session -d -s "${TMUX_SESSION}" -c "${MASTER_DIR}"

# 在 tmux pane 0 中启动 devin CLI
# devin 会读取 .devin/hooks.v1.json，SessionStart hook 注入工作系统认知
tmux send-keys -t "${TMUX_SESSION}:0.0" "cd ${MASTER_DIR} && devin" Enter

# 等待 devin 启动
sleep 2

# attach 到 session
exec tmux attach -t "${TMUX_SESSION}"
