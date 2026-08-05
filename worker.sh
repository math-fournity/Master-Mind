#!/bin/bash
# Worker Agent 启动脚本
# 在tmux中启动 opencode 或 Devin CLI 来执行任务

set -e

# 默认参数
WORKER_ID=""
TASK_ID=""
SESSION_NAME=""
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
START_LINE=""
END_LINE=""
SECTION_ID=""
AGENT_PROVIDER="${MOIRA_AGENT_PROVIDER:-opencode}"

# 解析命令行参数
while [[ $# -gt 0 ]]; do
  case $1 in
    --worker-id)
      WORKER_ID="$2"
      shift 2
      ;;
    --task-id)
      TASK_ID="$2"
      shift 2
      ;;
    --session)
      SESSION_NAME="$2"
      shift 2
      ;;
    --start-line)
      START_LINE="$2"
      shift 2
      ;;
    --end-line)
      END_LINE="$2"
      shift 2
      ;;
    --section-id)
      SECTION_ID="$2"
      shift 2
      ;;
    --provider)
      AGENT_PROVIDER="$2"
      shift 2
      ;;
    -h|--help)
      echo "用法: $0 --worker-id <WORKER_ID> --task-id <TASK_ID> [--session <SESSION_NAME>] [--start-line <LINE>] [--end-line <LINE>] [--section-id <ID>] [--provider opencode|devin]"
      echo ""
      echo "参数:"
      echo "  --worker-id    Worker ID (W1, W2, ...)"
      echo "  --task-id      任务ID"
      echo "  --session      tmux会话名 (可选，默认: worker-<WORKER_ID>)"
      echo "  --start-line   起始行号 (可选)"
      echo "  --end-line     结束行号 (可选)"
      echo "  --section-id   Section ID (可选)"
      echo "  --provider     Agent provider: opencode 或 devin (默认: MOIRA_AGENT_PROVIDER 或 opencode)"
      echo ""
      echo "示例:"
      echo "  $0 --worker-id W1 --task-id 20.4"
      echo "  $0 --worker-id W1 --task-id 20.4 --start-line 1 --end-line 130 --section-id 卷一/星曜躔度歌"
      echo "  $0 --provider devin --worker-id W1 --task-id 20.4"
      exit 0
      ;;
    *)
      echo "错误: 未知参数 $1" >&2
      exit 1
      ;;
  esac
done

# 检查必需参数
if [ -z "$WORKER_ID" ]; then
  echo "错误: 必须指定 --worker-id" >&2
  exit 1
fi

if [ -z "$TASK_ID" ]; then
  echo "错误: 必须指定 --task-id" >&2
  exit 1
fi

case "$AGENT_PROVIDER" in
  opencode|devin)
    ;;
  *)
    echo "错误: --provider 只支持 opencode 或 devin" >&2
    exit 1
    ;;
esac

# 设置默认会话名
if [ -z "$SESSION_NAME" ]; then
  SESSION_NAME="worker-${WORKER_ID}"
fi

# 检查tmux是否可用
if ! command -v tmux &> /dev/null; then
  echo "错误: tmux 未安装" >&2
  exit 1
fi

# 检查 agent provider 是否可用
if ! command -v "$AGENT_PROVIDER" &> /dev/null; then
  echo "错误: $AGENT_PROVIDER 未安装或不在 PATH 中" >&2
  exit 1
fi

# 检查是否已经有同名会话
if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
  echo "错误: tmux会话 $SESSION_NAME 已存在" >&2
  echo "请先运行: tmux kill-session -t $SESSION_NAME" >&2
  exit 1
fi

# 读取任务信息
TASK_INFO=$(python3 -c "
import json
with open('tasks.json', 'r') as f:
    data = json.load(f)
for task in data['tasks']:
    if task['id'] == '$TASK_ID':
        print(json.dumps(task, ensure_ascii=False))
        break
else:
    print('{}')
")

if [ "$TASK_INFO" = "{}" ]; then
  echo "错误: 找不到任务 $TASK_ID" >&2
  exit 1
fi

# 提取任务标题
TASK_TITLE=$(echo "$TASK_INFO" | python3 -c "import sys, json; print(json.load(sys.stdin).get('title', '未知任务'))")

echo "启动 Worker $WORKER_ID"
echo "任务: $TASK_ID - $TASK_TITLE"
echo "会话: $SESSION_NAME"
echo "Provider: $AGENT_PROVIDER"

if [ -n "$START_LINE" ] && [ -n "$END_LINE" ]; then
  echo "行范围: $START_LINE-$END_LINE"
fi

if [ -n "$SECTION_ID" ]; then
  echo "Section: $SECTION_ID"
fi

echo ""

# 构建提示词（使用新的思维力内化提示词），并保存成证据文件
PROMPT_DIR="$PROJECT_DIR/runtime/prompts"
TRANSCRIPT_DIR="$PROJECT_DIR/runtime/transcripts"
mkdir -p "$PROMPT_DIR" "$TRANSCRIPT_DIR"

SAFE_SESSION=$(echo "$SESSION_NAME" | tr -c '[:alnum:]_.-' '_')
SAFE_TASK=$(echo "$TASK_ID" | tr -c '[:alnum:]_.-' '_')
PROMPT_FILE="$PROMPT_DIR/${SAFE_SESSION}_${SAFE_TASK}.md"
EXPORT_FILE="$TRANSCRIPT_DIR/${SAFE_SESSION}_${SAFE_TASK}.${AGENT_PROVIDER}.atif.json"

python3 worker_prompt.py --task-id "$TASK_ID" --task-title "$TASK_TITLE" ${SECTION_ID:+--section-id "$SECTION_ID"} ${START_LINE:+--start-line "$START_LINE"} ${END_LINE:+--end-line "$END_LINE"} > "$PROMPT_FILE"

# 在tmux中启动 agent provider。真正的 provider 差异由 tools/agent_launcher.py 处理。
echo "在tmux中启动 $AGENT_PROVIDER..."
LAUNCH_CMD=(
  python3 tools/agent_launcher.py
  --role worker
  --provider "$AGENT_PROVIDER"
  --prompt-file "$PROMPT_FILE"
  --export-file "$EXPORT_FILE"
)
tmux new-session -d -s "$SESSION_NAME" -c "$PROJECT_DIR" \
  "$(printf '%q ' "${LAUNCH_CMD[@]}")"

echo "✅ Worker $WORKER_ID 已启动"
echo "Prompt: $PROMPT_FILE"
echo "Transcript: $EXPORT_FILE"
echo ""
echo "查看会话: tmux attach -t $SESSION_NAME"
echo "分离会话: Ctrl+B 然后 D"
echo "终止会话: tmux kill-session -t $SESSION_NAME"
