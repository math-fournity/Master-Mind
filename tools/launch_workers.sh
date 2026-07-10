#!/bin/bash
# launch_workers.sh — 启动并管理最多 2 个 Devin Worker (yolo 模式)
#
# 从 tasks.json 中取 queued 任务，分配给最多 2 个 Worker。
# 每个 Worker 在独立 git worktree + tmux 中运行，watchdog 自动监控。
# 限流后自动 cooldown + 重启。
#
# 用法：
#   ./tools/launch_workers.sh                    # 启动 2 个 Worker
#   ./tools/launch_workers.sh --max-workers 1    # 只启动 1 个 Worker
#   ./tools/launch_workers.sh --dry-run          # 只显示会做什么，不实际执行

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

MAX_WORKERS=2
DRY_RUN=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --max-workers) MAX_WORKERS="$2"; shift 2 ;;
    --dry-run)     DRY_RUN=true; shift ;;
    -h|--help)
      echo "用法: $0 [--max-workers N] [--dry-run]"
      echo "最多启动 2 个 Devin Worker (算上 Master 共 3 个)"
      exit 0 ;;
    *) echo "未知参数 $1" >&2; exit 1 ;;
  esac
done

# 获取 queued 的 auto.* 任务列表（优先 auto，其次 random/explore）
get_next_queued_task() {
  python3 -c "
import json, sys
with open('tasks.json') as f:
    data = json.load(f)
# 优先 auto.* 任务
for t in data['tasks']:
    if t.get('status') == 'queued' and t.get('id', '').startswith('auto.'):
        print(f\"{t['id']}\t{t.get('section_id', '')}\t{t.get('title', '')}\")
        sys.exit(0)
# 其次 random/explore
for t in data['tasks']:
    if t.get('status') == 'queued':
        print(f\"{t['id']}\t{t.get('section_id', '')}\t{t.get('title', '')}\")
        sys.exit(0)
"
}

# 获取 section 的行号范围
get_line_range() {
  local section_id="$1"
  [[ -z "$section_id" ]] && { echo ""; return; }
  python3 -c "
import json, sys
with open('dev-docs/原典/星平会海/full_path_tree.json') as f:
    tree = json.load(f)
for vol in tree['volumes']:
    for sec in vol.get('sections', []):
        if sec['id'] == '$section_id':
            print(f\"{sec['source_file']}:{sec['start_line']}:{sec['end_line']}\")
            sys.exit(0)
        for sub in sec.get('subsections', []):
            if sub['id'] == '$section_id':
                print(f\"{sec['source_file']}:{sub['start_line']}:{sub['end_line']}\")
                sys.exit(0)
"
}

# 标记任务为 leased
lease_task() {
  local task_id="$1"
  local worker_id="$2"
  python3 -c "
import json
with open('tasks.json') as f:
    data = json.load(f)
for t in data['tasks']:
    if t.get('id') == '$task_id' and t.get('status') == 'queued':
        t['status'] = 'leased'
        t['assigned_to'] = '$worker_id'
        t['updated_at'] = '2026-07-10T00:45:00'
        break
if '$worker_id' in data['workers']:
    data['workers']['$worker_id']['status'] = 'busy'
    data['workers']['$worker_id']['current_task'] = '$task_id'
with open('tasks.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
"
}

# 检查 Worker tmux 会话是否在运行
is_worker_running() {
  local session="$1"
  tmux has-session -t "$session" 2>/dev/null
}

echo "=== MOIRA Worker 启动器 (最多 $MAX_WORKERS 个 Devin Worker) ==="
echo ""

# 检查当前已运行的 worker-* 会话
RUNNING_WORKERS=$(tmux list-sessions 2>/dev/null | grep -c "^worker-" 2>/dev/null || true)
RUNNING_WORKERS=${RUNNING_WORKERS:-0}
echo "当前运行中的 Worker: $RUNNING_WORKERS"

SLOTS_AVAILABLE=$((MAX_WORKERS - RUNNING_WORKERS))
echo "可用槽位: $SLOTS_AVAILABLE"

if [[ "$SLOTS_AVAILABLE" -le 0 ]]; then
  echo "已达最大 Worker 数 ($MAX_WORKERS)，不启动新 Worker"
  exit 0
fi

# 启动 Worker
LAUNCHED=0
for i in $(seq 1 "$SLOTS_AVAILABLE"); do
  WORKER_ID="W$((i + RUNNING_WORKERS))"
  SESSION_NAME="worker-${WORKER_ID}"

  # 获取下一个 queued 任务
  TASK_LINE=$(get_next_queued_task)
  if [[ -z "$TASK_LINE" ]]; then
    echo "没有 queued 任务了"
    break
  fi

  TASK_ID=$(echo "$TASK_LINE" | cut -f1)
  SECTION_ID=$(echo "$TASK_LINE" | cut -f2)
  TASK_TITLE=$(echo "$TASK_LINE" | cut -f3)

  echo ""
  echo "[$WORKER_ID] 任务: $TASK_ID - $TASK_TITLE"
  echo "  Section: $SECTION_ID"

  # 获取行号
  LINE_INFO=$(get_line_range "$SECTION_ID")
  SOURCE_FILE=""
  START_LINE=""
  END_LINE=""
  if [[ -n "$LINE_INFO" ]]; then
    SOURCE_FILE=$(echo "$LINE_INFO" | cut -d: -f1)
    START_LINE=$(echo "$LINE_INFO" | cut -d: -f2)
    END_LINE=$(echo "$LINE_INFO" | cut -d: -f3)
    echo "  原文: $SOURCE_FILE 行 $START_LINE-$END_LINE"
  fi

  if $DRY_RUN; then
    echo "  [dry-run] 跳过实际启动"
    continue
  fi

  # Lease 任务
  lease_task "$TASK_ID" "$WORKER_ID"
  echo "  已 lease 任务 $TASK_ID → $WORKER_ID"

  # 启动 worker_v2.sh（它会创建 worktree + tmux + watchdog）
  bash "$PROJECT_DIR/tools/worker_v2.sh" \
    --worker-id "$WORKER_ID" \
    --task-id "$TASK_ID" \
    --session "$SESSION_NAME" \
    ${SECTION_ID:+--section-id "$SECTION_ID"} \
    ${START_LINE:+--start-line "$START_LINE"} \
    ${END_LINE:+--end-line "$END_LINE"}

  LAUNCHED=$((LAUNCHED + 1))
  echo "  ✅ $WORKER_ID 已启动"
done

echo ""
echo "本次启动 $LAUNCHED 个 Worker"
echo "查看 Worker: tmux list-sessions | grep worker-"
echo "查看任务状态: python3 master.py status"
