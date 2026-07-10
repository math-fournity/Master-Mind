#!/bin/bash
# watchdog.sh — 监控 tmux 中的 Devin Worker 进程
#
# 功能：
#   1. 检测 Worker tmux 会话是否退出
#   2. 如果退出码非0，检查是否是限流（rate limit）
#   3. 如果是限流，等待 cooldown 后自动重启 Worker 并发"继续"
#   4. 如果是非限流错误，记录日志并 re-queue 任务
#   5. 如果退出码0（正常完成），标记任务完成
#
# 用法：
#   ./tools/watchdog.sh --session worker-W1 --task-id auto.40 --worker-id W1
#   ./tools/watchdog.sh --session worker-W1 --task-id auto.40 --worker-id W1 --max-retries 5 --cooldown 1800

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

# 默认参数
SESSION_NAME=""
TASK_ID=""
WORKER_ID=""
MAX_RETRIES=5
COOLDOWN=1800          # 30 分钟（限流通常说 28-30 分钟重置）
POLL_INTERVAL=30       # 每 30 秒检查一次 tmux 会话状态
RATE_LIMIT_PATTERN="rate.limit\|Reached overall message rate limit\|limit will reset"

# 解析参数
while [[ $# -gt 0 ]]; do
  case $1 in
    --session)      SESSION_NAME="$2"; shift 2 ;;
    --task-id)      TASK_ID="$2"; shift 2 ;;
    --worker-id)    WORKER_ID="$2"; shift 2 ;;
    --max-retries)  MAX_RETRIES="$2"; shift 2 ;;
    --cooldown)     COOLDOWN="$2"; shift 2 ;;
    --poll-interval) POLL_INTERVAL="$2"; shift 2 ;;
    -h|--help)
      echo "用法: $0 --session <tmux会话> --task-id <任务ID> --worker-id <WorkerID>"
      echo ""
      echo "参数:"
      echo "  --session       tmux 会话名 (如 worker-W1)"
      echo "  --task-id       任务 ID (如 auto.40)"
      echo "  --worker-id     Worker ID (如 W1)"
      echo "  --max-retries   最大重试次数 (默认 5)"
      echo "  --cooldown      限流后等待秒数 (默认 1800 = 30分钟)"
      echo "  --poll-interval 检查间隔秒数 (默认 30)"
      exit 0 ;;
    *) echo "错误: 未知参数 $1" >&2; exit 1 ;;
  esac
done

[[ -z "$SESSION_NAME" || -z "$TASK_ID" || -z "$WORKER_ID" ]] && {
  echo "错误: 必须指定 --session, --task-id, --worker-id" >&2; exit 1; }

LOG_DIR="$PROJECT_DIR/runtime/watchdog_logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/${SESSION_NAME}_${TASK_ID}.log"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] [watchdog:$WORKER_ID] $*" | tee -a "$LOG_FILE"
}

# 捕获 tmux pane 内容到临时文件
capture_pane() {
  local tmpfile
  tmpfile=$(mktemp)
  tmux capture-pane -t "$SESSION_NAME" -p -S -1000 > "$tmpfile" 2>/dev/null || true
  echo "$tmpfile"
}

# 检查 pane 内容是否包含限流信息
check_rate_limited() {
  local pane_file="$1"
  grep -iE "$RATE_LIMIT_PATTERN" "$pane_file" >/dev/null 2>&1
}

# 重启 Worker（发"继续"让 Devin 恢复工作）
restart_worker() {
  local retry_num="$1"
  log "重启 Worker (重试 $retry_num/$MAX_RETRIES)"

  # 重新启动 worker_v2.sh（它会重新创建 worktree 并启动 devin）
  # 但这次用 --resume 方式：如果 worktree 已存在，直接在里面发"继续"
  local worktree_path="$PROJECT_DIR/.worktrees/${SESSION_NAME}"

  if [[ -d "$worktree_path" ]]; then
    # worktree 已存在，在 tmux 里启动 devin 并发"继续"
    tmux new-session -d -s "$SESSION_NAME" -c "$worktree_path" \
      "devin --permission-mode dangerous --prompt-file /dev/stdin <<'PROMPT'
继续之前被限流中断的工作。你的任务ID是 $TASK_ID。请检查已有的工作成果，继续完成未完成的部分。
PROMPT"
    log "已在 worktree $worktree_path 中重启 devin 并发'继续'"
  else
    # worktree 不存在，从头启动
    log "worktree 不存在，从头启动 worker"
    bash "$PROJECT_DIR/tools/worker_v2.sh" \
      --worker-id "$WORKER_ID" \
      --task-id "$TASK_ID" \
      --session "$SESSION_NAME"
  fi
}

# 标记任务完成
complete_task() {
  log "任务 $TASK_ID 正常完成"
  python3 master.py complete --task-id "$TASK_ID" --worker-id "$WORKER_ID" --result "PASS" 2>/dev/null || true
}

# Re-queue 任务
requeue_task() {
  local reason="$1"
  log "任务 $TASK_ID re-queue: $reason"
  python3 -c "
import json
with open('tasks.json', 'r') as f:
    data = json.load(f)
for t in data['tasks']:
    if t.get('id') == '$TASK_ID' and t.get('status') == 'leased':
        t['status'] = 'queued'
        t['assigned_to'] = None
        t['updated_at'] = '2026-07-10T00:40:00'
        break
# Free worker
if '$WORKER_ID' in data['workers']:
    data['workers']['$WORKER_ID']['status'] = 'idle'
    data['workers']['$WORKER_ID']['current_task'] = None
with open('tasks.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
" 2>/dev/null || true
}

# ===== 主循环 =====
RETRY_COUNT=0

log "watchdog 启动: session=$SESSION_NAME task=$TASK_ID worker=$WORKER_ID"
log "max_retries=$MAX_RETRIES cooldown=${COOLDOWN}s poll_interval=${POLL_INTERVAL}s"

while true; do
  # 检查 tmux 会话是否存在
  if ! tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
    log "tmux 会话 $SESSION_NAME 已退出"

    # 会话已结束，检查任务状态
    TASK_STATUS=$(python3 -c "
import json
with open('tasks.json') as f:
    data = json.load(f)
for t in data['tasks']:
    if t.get('id') == '$TASK_ID':
        print(t.get('status', 'unknown'))
        break
" 2>/dev/null || echo "error")

    log "任务状态: $TASK_STATUS"

    if [[ "$TASK_STATUS" == "completed" ]]; then
      log "任务已完成，watchdog 退出"
      exit 0
    fi

    # 任务未完成，检查是否限流
    # 注意：tmux 会话已退出，无法 capture-pane
    # 检查最近的 launcher log
    LATEST_LOG=$(ls -t "$PROJECT_DIR/runtime/launcher_logs/"*.json 2>/dev/null | head -1)
    if [[ -n "$LATEST_LOG" ]]; then
      log "检查 launcher log: $LATEST_LOG"
    fi

    # 由于无法从已退出的 tmux 获取输出，检查 transcript 文件
    TRANSCRIPT_FILE="$PROJECT_DIR/runtime/transcripts/${SESSION_NAME}_${TASK_ID}.devin.atif.json"
    if [[ -f "$TRANSCRIPT_FILE" ]]; then
      if grep -iE "$RATE_LIMIT_PATTERN" "$TRANSCRIPT_FILE" >/dev/null 2>&1; then
        log "检测到限流！"
        IS_RATE_LIMITED=1
      else
        IS_RATE_LIMITED=0
      fi
    else
      log "无 transcript 文件，假设非限流退出"
      IS_RATE_LIMITED=0
    fi

    if [[ "$IS_RATE_LIMITED" == "1" ]]; then
      RETRY_COUNT=$((RETRY_COUNT + 1))
      if [[ "$RETRY_COUNT" -gt "$MAX_RETRIES" ]]; then
        log "超过最大重试次数 ($MAX_RETRIES)，re-queue 任务"
        requeue_task "rate limit exceeded max retries"
        exit 1
      fi

      log "等待 cooldown ${COOLDOWN}s 后重启..."
      sleep "$COOLDOWN"

      log "cooldown 结束，重启 Worker"
      restart_worker "$RETRY_COUNT"
      # 等待新会话启动
      sleep 5
      continue
    else
      # 非限流退出，检查任务是否已完成
      if [[ "$TASK_STATUS" == "completed" ]]; then
        complete_task
        exit 0
      else
        log "非限流异常退出，re-queue 任务"
        requeue_task "non-rate-limit exit"
        exit 1
      fi
    fi
  fi

  # tmux 会话仍然存在，检查 pane 输出是否有限流迹象
  PANE_FILE=$(capture_pane)
  if check_rate_limited "$PANE_FILE"; then
    log "检测到 pane 中有限流迹象，但会话仍在运行 — 等待自愈"
    # Devin 可能会自己等待并重试，先观察
  fi
  rm -f "$PANE_FILE"

  sleep "$POLL_INTERVAL"
done
