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
# - tmux session 持久存在，AI 连接断开后不丢失工作状态
# - 可以在断线后重新 attach 恢复工作
#
# tmux 配置依赖：
# - 本脚本依赖 ~/.tmux.conf 全局配置，已包含以下易用性设置：
#   - history-limit 500000（50 万行缓冲区）
#   - mouse on（鼠标滚动）
#   - set-clipboard external + pbcopy 集成（复制到系统剪贴板）
#   - mode-keys vi（vi 复制模式：v 选择, y 复制, Enter 复制）
#   - MouseDragEnd1Pane → pbcopy（鼠标拖拽直接复制到系统剪贴板）
# - 如果 tmux 易用性有问题，先检查 ~/.tmux.conf 是否存在且包含上述配置
#
# 复制粘贴说明：
# - 鼠标拖拽选中文本 → 自动复制到系统剪贴板（pbcopy 集成）
# - Ctrl+B [ 进入 copy mode → v 选择 → y 或 Enter 复制到系统剪贴板
# - 按住 Option 键拖拽鼠标 → 绕过 tmux 鼠标拦截，用终端原生方式选择复制
# - Command+V 粘贴（终端原生粘贴，不经过 tmux）
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
