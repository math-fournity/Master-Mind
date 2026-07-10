#!/bin/bash
# auto_dispatch.sh — 自动监控 Worker 完成状态并派发下一批任务
#
# 用法：
#   ./tools/auto_dispatch.sh --max-workers 2 --batch-size 2
#   Ctrl+C 停止

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

MAX_WORKERS=2
BATCH_SIZE=2
POLL_INTERVAL=60

while [[ $# -gt 0 ]]; do
  case $1 in
    --max-workers) MAX_WORKERS="$2"; shift 2 ;;
    --batch-size)  BATCH_SIZE="$2"; shift 2 ;;
    --poll-interval) POLL_INTERVAL="$2"; shift 2 ;;
    *) shift ;;
  esac
done

log() {
  echo "[$(date '+%H:%M:%S')] $*"
}

while true; do
  # 检查 queued 任务数
  QUEUED=$(python3 -c "
import json
with open('tasks.json') as f: data = json.load(f)
print(len([t for t in data['tasks'] if t.get('status') == 'queued']))
" 2>/dev/null || echo 0)

  if [[ "$QUEUED" == "0" ]]; then
    log "没有 queued 任务了，检查是否全部完成..."
    COMPLETED=$(python3 -c "
import json
with open('tasks.json') as f: data = json.load(f)
print(len([t for t in data['tasks'] if t.get('status') == 'completed']))
" 2>/dev/null || echo 0)
    log "已完成: $COMPLETED"
    break
  fi

  # 检查运行中的 Worker
  RUNNING=$(tmux list-sessions 2>/dev/null | grep -c "^worker-" 2>/dev/null || true)
  RUNNING=${RUNNING:-0}

  # 检查是否有 devin 进程在运行
  DEVIN_RUNNING=$(ps aux | grep 'devin --permission' | grep -v grep | wc -l | tr -d ' ' || true)
  DEVIN_RUNNING=${DEVIN_RUNNING:-0}

  log "queued=$QUEUED running_workers=$RUNNING devin_procs=$DEVIN_RUNNING"

  if [[ "$DEVIN_RUNNING" == "0" ]]; then
    # 没有 devin 进程在运行
    if [[ "$RUNNING" -gt 0 ]]; then
      # Worker tmux 会话存在但 devin 进程已退出 → 任务可能完成了
      log "Devin 进程已退出，收集结果并清理..."

      # 复制 AUDIT 文件从 worktree 到主目录
      for wt in .worktrees/worker-W*; do
        [[ -d "$wt/dev-docs" ]] || continue
        for audit in "$wt"/dev-docs/AUDIT-auto.*.md; do
          [[ -f "$audit" ]] || continue
          basename=$(basename "$audit")
          if [[ ! -f "dev-docs/$basename" ]]; then
            cp "$audit" dev-docs/
            log "  复制: $basename"
          fi
        done
      done

      # 清理已完成的 Worker
      for sess in $(tmux list-sessions 2>/dev/null | grep "^worker-" | awk -F: '{print $1}'); do
        tmux kill-session -t "$sess" 2>/dev/null || true
      done

      # 清理 worktree
      git worktree prune 2>/dev/null || true
      for wt in .worktrees/worker-W*; do
        [[ -d "$wt" ]] || continue
        git worktree remove "$wt" --force 2>/dev/null || true
      done

      # 清理旧分支
      git branch | grep 'worker/' | awk '{print $1}' | while read br; do
        git branch -D "$br" 2>/dev/null || true
      done

      # 重新 lease 已释放的 leased 任务
      python3 -c "
import json
with open('tasks.json', 'r') as f: data = json.load(f)
changed = False
for t in data['tasks']:
    if t.get('status') == 'leased':
        t['status'] = 'queued'
        t['assigned_to'] = None
        changed = True
for w in data['workers'].values():
    if w.get('status') == 'busy':
        w['status'] = 'idle'
        w['current_task'] = None
if changed:
    with open('tasks.json', 'w') as f: json.dump(data, f, ensure_ascii=False, indent=2)
" 2>/dev/null || true
    fi

    # 启动下一批（无论 RUNNING 是 0 还是 >0，只要没有 devin 在跑就启动）
    if [[ "$QUEUED" -gt 0 ]]; then
      log "启动下一批 Worker..."
      ./tools/launch_workers.sh --max-workers "$MAX_WORKERS" 2>&1 | grep -E "✅|任务:|本次启动|可用槽位" || true

      # 等待 Worker 启动
      sleep 15
    fi
  fi

  sleep "$POLL_INTERVAL"
done

log "所有任务完成！"
python3 -c "
import json
from collections import Counter
with open('tasks.json') as f: data = json.load(f)
print(f'Final: {dict(Counter(t.get(\"status\") for t in data[\"tasks\"]))}')
"
