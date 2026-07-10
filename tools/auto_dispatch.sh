#!/bin/bash
# auto_dispatch.sh — 自动监控 Worker 完成状态并派发下一批任务
#
# 用法：
#   ./tools/auto_dispatch.sh --max-workers 2 --poll-interval 120
#   Ctrl+C 停止
#
# 核心逻辑：
#   1. 启动一批 Worker（最多 --max-workers 个）
#   2. 每 --poll-interval 秒检查 devin 进程数
#   3. 当 devin 进程从 >0 变为 0 时，收集结果、清理、启动下一批
#   4. 重复直到没有 queued 任务

set -uo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

MAX_WORKERS=2
POLL_INTERVAL=120

while [[ $# -gt 0 ]]; do
  case $1 in
    --max-workers) MAX_WORKERS="$2"; shift 2 ;;
    --poll-interval) POLL_INTERVAL="$2"; shift 2 ;;
    *) shift ;;
  esac
done

log() {
  echo "[$(date '+%H:%M:%S')] $*"
}

count_devin() {
  local n
  n=$(ps aux 2>/dev/null | grep 'devin --permission' | grep -v grep | wc -l | tr -d ' \n')
  echo "${n:-0}"
}

count_queued() {
  local n
  n=$(python3 -c "
import json
with open('tasks.json') as f: data = json.load(f)
print(len([t for t in data['tasks'] if t.get('status') == 'queued']))
" 2>/dev/null)
  echo "${n:-0}"
}

count_completed() {
  local n
  n=$(python3 -c "
import json
with open('tasks.json') as f: data = json.load(f)
print(len([t for t in data['tasks'] if t.get('status') == 'completed']))
" 2>/dev/null)
  echo "${n:-0}"
}

cleanup_and_collect() {
  log "收集 AUDIT 文件并清理旧 Worker..."

  # 0. 杀掉所有 watchdog 进程（防止重启 devin）
  pkill -f 'tools/watchdog.sh' 2>/dev/null || true
  sleep 1

  # 0b. 杀掉所有 devin 进程
  pkill -f 'devin --permission-mode dangerous' 2>/dev/null || true
  sleep 2

  # 复制 AUDIT 文件从 worktree 到主目录
  for wt in .worktrees/worker-W*; do
    [[ -d "$wt/dev-docs" ]] || continue
    for audit in "$wt"/dev-docs/AUDIT-auto.*.md; do
      [[ -f "$audit" ]] || continue
      bn=$(basename "$audit")
      if [[ ! -f "dev-docs/$bn" ]]; then
        cp "$audit" dev-docs/
        log "  复制: $bn"
      fi
    done
  done

  # 清理 tmux 会话
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
  git branch 2>/dev/null | grep 'worker/' | awk '{print $1}' | while read br; do
    git branch -D "$br" 2>/dev/null || true
  done

  # 重置 leased 任务为 queued
  python3 -c "
import json
with open('tasks.json', 'r') as f: data = json.load(f)
changed = False
for t in data['tasks']:
    if t.get('status') == 'leased':
        t['status'] = 'queued'
        t['assigned_to'] = None
        changed = True
for w in data.get('workers', {}).values():
    if w.get('status') == 'busy':
        w['status'] = 'idle'
        w['current_task'] = None
if changed:
    with open('tasks.json', 'w') as f: json.dump(data, f, ensure_ascii=False, indent=2)
" 2>/dev/null || true
}

launch_batch() {
  local queued=$(count_queued)
  if [[ "$queued" == "0" ]]; then
    return 1
  fi

  log "启动下一批 Worker (queued=$queued)..."
  ./tools/launch_workers.sh --max-workers "$MAX_WORKERS" 2>&1 | grep -E "✅|任务:|本次启动|可用槽位|没有" || true

  # 等待 devin 进程启动
  sleep 10

  local devin=$(count_devin)
  if [[ "$devin" == "0" ]]; then
    log "警告: Worker 启动后没有 devin 进程，可能启动失败"
    sleep 5
    devin=$(count_devin)
    if [[ "$devin" == "0" ]]; then
      log "错误: 仍然没有 devin 进程，清理后重试..."
      cleanup_and_collect
      sleep 5
      return 0  # 重试
    fi
  fi

  log "Worker 已启动 (devin_procs=$devin)，等待完成..."
  return 0
}

# ===== 主循环 =====

log "=== MOIRA auto_dispatch 启动 (max_workers=$MAX_WORKERS poll=${POLL_INTERVAL}s) ==="

# 首次启动
launch_batch

while true; do
  sleep "$POLL_INTERVAL"

  queued=$(count_queued)
  devin=$(count_devin)
  completed=$(count_completed)

  log "status: queued=$queued completed=$completed devin_procs=$devin"

  if [[ "$queued" == "0" && "$devin" == "0" ]]; then
    log "所有任务完成！"
    log "最终状态: completed=$completed"
    break
  fi

  if [[ "$devin" == "0" ]]; then
    # 所有 devin 进程已退出，收集结果并启动下一批
    cleanup_and_collect
    launch_batch
  fi
done

log "=== auto_dispatch 结束 ==="
