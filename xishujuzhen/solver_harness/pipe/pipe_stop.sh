#!/bin/bash
# pipe_stop.sh — 完整停止做题系统
#
# 用法:
#   bash pipe_stop.sh              # 优雅停止（保留harness session）
#   bash pipe_stop.sh --kill       # 停止并kill所有harness session

set -e

export PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

REPO=~/master-mind-glm5.2-worktree
PY=$REPO/.venv/bin/python3
export PYTHONPATH=$REPO/xishujuzhen/solver_harness/pipe

echo "=========================================="
echo "  停止做题系统"
echo "=========================================="

# === 1. 停watchdog（防止自动重启）===
echo ""
echo "[1/3] 停止launchd watchdog..."
PLIST=~/Library/LaunchAgents/com.aurolafly.pipe-watchdog.plist
launchctl unload $PLIST 2>/dev/null || true
echo "  ✅ watchdog已停止"

# === 2. 停5个pipe-*服务 ===
echo ""
echo "[2/3] 停止5个pipe-*服务..."
for svc in pipe-feeder pipe-runner pipe-collector pipe-reporter pipe-retry; do
    if tmux has-session -t $svc 2>/dev/null; then
        tmux send-keys -t $svc C-c ""
        sleep 2
        tmux kill-session -t $svc 2>/dev/null || true
        echo "  ✅ $svc 已停止"
    else
        echo "  ⏭️ $svc 不存在"
    fi
done

# === 3. harness session ===
echo ""
if [ "$1" = "--kill" ]; then
    echo "[3/3] kill所有harness session..."
    # 用pipe_control.py stop --kill-harness
    set -a; source $REPO/.env; set +a
    $PY $REPO/xishujuzhen/solver_harness/pipe/pipe_control.py stop --kill-harness 2>&1 | grep -E "killed|停止|服务" || true
    # 手动清理残留
    for s in $(tmux list-sessions 2>/dev/null | grep "harness-" | awk -F: '{print $1}'); do
        tmux kill-session -t "$s" 2>/dev/null || true
    done
    echo "  ✅ 所有harness session已kill"
else
    echo "[3/3] 保留harness session（解耦设计，它们会自然完成）"
    echo "  如需kill: bash pipe_stop.sh --kill"
fi

echo ""
echo "=========================================="
echo "  停止完成!"
echo "=========================================="
echo ""
echo "  恢复: bash $REPO/xishujuzhen/solver_harness/pipe/pipe_start.sh"
echo ""
