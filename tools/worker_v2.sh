#!/bin/bash
# worker_v2.sh — Worker 启动脚本 v2 (git worktree + Devin yolo 模式)
#
# 改进：
#   1. git worktree 隔离：每个 Worker 在独立 worktree 工作，避免文件冲突
#   2. Devin yolo 模式：--permission-mode dangerous，自动批准所有操作
#   3. 最多 2 个 Devin Worker 实例（算上 Master 共 3 个）
#   4. watchdog 自动监控：限流后自动 cooldown + 重启 + 发"继续"
#
# 用法：
#   ./tools/worker_v2.sh --worker-id W1 --task-id auto.40
#   ./tools/worker_v2.sh --worker-id W1 --task-id auto.40 --section-id 卷一/星曜照宫歌/兄弟宫 --start-line 302 --end-line 303

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

# 默认参数
WORKER_ID=""
TASK_ID=""
SESSION_NAME=""
SECTION_ID=""
START_LINE=""
END_LINE=""
WORKTREE_DIR="$PROJECT_DIR/.worktrees"
BRANCH_PREFIX="worker"

# 解析参数
while [[ $# -gt 0 ]]; do
  case $1 in
    --worker-id)    WORKER_ID="$2"; shift 2 ;;
    --task-id)      TASK_ID="$2"; shift 2 ;;
    --session)      SESSION_NAME="$2"; shift 2 ;;
    --section-id)   SECTION_ID="$2"; shift 2 ;;
    --start-line)   START_LINE="$2"; shift 2 ;;
    --end-line)     END_LINE="$2"; shift 2 ;;
    --worktree-dir) WORKTREE_DIR="$2"; shift 2 ;;
    -h|--help)
      echo "用法: $0 --worker-id <WID> --task-id <TID> [选项]"
      echo ""
      echo "参数:"
      echo "  --worker-id    Worker ID (W1, W2, ...)"
      echo "  --task-id      任务 ID"
      echo "  --session      tmux 会话名 (默认: worker-<WORKER_ID>)"
      echo "  --section-id   Section ID (可选)"
      echo "  --start-line   起始行号 (可选)"
      echo "  --end-line     结束行号 (可选)"
      echo "  --worktree-dir worktree 目录 (默认: .worktrees)"
      echo ""
      echo "Devin yolo 模式: --permission-mode dangerous"
      echo "最多 2 个 Worker 实例 (算上 Master 共 3 个 Devin)"
      exit 0 ;;
    *) echo "错误: 未知参数 $1" >&2; exit 1 ;;
  esac
done

[[ -z "$WORKER_ID" || -z "$TASK_ID" ]] && {
  echo "错误: 必须指定 --worker-id 和 --task-id" >&2; exit 1; }

# 默认会话名
[[ -z "$SESSION_NAME" ]] && SESSION_NAME="worker-${WORKER_ID}"

# 可选：resume 模式（继续之前的 session）
RESUME_SESSION=""
RESUME_FLAG=""

# 解析额外参数
while [[ $# -gt 0 ]]; do
  case $1 in
    --resume)       RESUME_SESSION="$2"; RESUME_FLAG="--resume"; shift 2 ;;
    --continue)     RESUME_FLAG="--continue"; shift ;;
    *) shift ;;
  esac
done

# 检查 tmux
command -v tmux &>/dev/null || { echo "错误: tmux 未安装" >&2; exit 1; }

# 检查 devin
command -v devin &>/dev/null || { echo "错误: devin 未安装" >&2; exit 1; }

# 检查会话是否已存在
if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
  echo "错误: tmux 会话 $SESSION_NAME 已存在" >&2
  echo "请先运行: tmux kill-session -t $SESSION_NAME" >&2
  exit 1
fi

# ===== 1. 创建 git worktree =====
WORKTREE_PATH="$WORKTREE_DIR/$SESSION_NAME"
BRANCH_NAME="$BRANCH_PREFIX/$WORKER_ID/$TASK_ID"

# 确保在 main 分支上创建 worktree
CURRENT_BRANCH=$(git branch --show-current)

if [[ -d "$WORKTREE_PATH" ]]; then
  echo "worktree 已存在: $WORKTREE_PATH，复用"
  cd "$WORKTREE_PATH"
  # 拉取最新的 tasks.json 和原文文件
  git checkout main -- tasks.json dev-docs/原典/ AGENTS.md 2>/dev/null || true
else
  echo "创建 git worktree: $WORKTREE_PATH (branch: $BRANCH_NAME)"
  mkdir -p "$WORKTREE_DIR"
  git worktree add "$WORKTREE_PATH" -b "$BRANCH_NAME" main 2>/dev/null || {
    # 如果分支已存在，用 detach 方式
    git worktree add "$WORKTREE_PATH" --detach main
  }
fi

# ===== 1.5 链接必要文件到 worktree =====
# git worktree 不会复制 untracked 文件，需要手动链接
# 注意：不链接 .devin/，因为符号链接会导致 Devin workspace trust 问题
# Devin 会自动使用全局配置 (~/.config/devin/config.json)
cd "$WORKTREE_PATH"
for item in ai-runtime .venv ephe moira_extra_files; do
  if [[ -e "$PROJECT_DIR/$item" && ! -e "$WORKTREE_PATH/$item" ]]; then
    ln -s "$PROJECT_DIR/$item" "$WORKTREE_PATH/$item"
    echo "  链接: $item → $PROJECT_DIR/$item"
  fi
done

cd "$WORKTREE_PATH"

# ===== 2. 生成 Worker 提示词 =====
PROMPT_DIR="$PROJECT_DIR/runtime/prompts"
TRANSCRIPT_DIR="$PROJECT_DIR/runtime/transcripts"
mkdir -p "$PROMPT_DIR" "$TRANSCRIPT_DIR"

SAFE_SESSION=$(echo "$SESSION_NAME" | tr -c '[:alnum:]_.-' '_')
SAFE_TASK=$(echo "$TASK_ID" | tr -c '[:alnum:]_.-' '_')
PROMPT_FILE="$PROMPT_DIR/${SAFE_SESSION}_${SAFE_TASK}.md"
EXPORT_FILE="$TRANSCRIPT_DIR/${SAFE_SESSION}_${SAFE_TASK}.devin.atif.json"

# 读取任务信息
TASK_INFO=$(python3 -c "
import json
with open('$PROJECT_DIR/tasks.json') as f:
    data = json.load(f)
for task in data['tasks']:
    if task['id'] == '$TASK_ID':
        print(json.dumps(task, ensure_ascii=False))
        break
else:
    print('{}')
")

[[ "$TASK_INFO" == "{}" ]] && { echo "错误: 找不到任务 $TASK_ID" >&2; exit 1; }

TASK_TITLE=$(echo "$TASK_INFO" | python3 -c "import sys, json; print(json.load(sys.stdin).get('title', '未知任务'))")

# 生成提示词
cd "$PROJECT_DIR"
python3 worker_prompt.py \
  --task-id "$TASK_ID" \
  --task-title "$TASK_TITLE" \
  ${SECTION_ID:+--section-id "$SECTION_ID"} \
  ${START_LINE:+--start-line "$START_LINE"} \
  ${END_LINE:+--end-line "$END_LINE"} \
  > "$PROMPT_FILE"

# 在提示词末尾追加 worktree 信息
cat >> "$PROMPT_FILE" << EOF

## Worktree 信息
你正在 git worktree 中工作：$WORKTREE_PATH
分支：$BRANCH_NAME
你的 AUDIT 文件产出到 dev-docs/AUDIT-${SAFE_TASK}-*.md
完成后请用 python3 master.py complete --task-id $TASK_ID --worker-id $WORKER_ID 标记完成。

## 限流恢复
如果你遇到 rate limit 错误，不要放弃。保存当前进度，等待后继续。
你的工作不会丢失——watchdog 会监控你的状态。
EOF

cd "$WORKTREE_PATH"

# ===== 3. 在 tmux 中启动 Devin (yolo 模式) =====
echo "启动 Worker $WORKER_ID"
echo "  任务: $TASK_ID - $TASK_TITLE"
echo "  会话: $SESSION_NAME"
echo "  Worktree: $WORKTREE_PATH"
echo "  模式: dangerous (yolo)"
echo "  Prompt: $PROMPT_FILE"

# Devin yolo 模式启动命令 (--print = 非交互模式，处理完 prompt 就退出)
# 不用 --config 指向项目配置，Devin 会自动读全局配置 (~/.config/devin/config.json)
# 项目级 .devin/config.json 中的 permissions 会被 --permission-mode dangerous 覆盖
#
# 注意：--print 模式是单轮的，Devin 处理完 prompt 就退出。
# 如果任务没完成，需要用 --resume <session_id> 继续。
# watchdog.sh 负责检测退出后是否需要 resume。
if [[ -n "$RESUME_SESSION" ]]; then
  # Resume 模式：继续之前的 session
  DEVIN_CMD=(
    devin
    --permission-mode dangerous
    --print
    --resume "$RESUME_SESSION"
    --export "$EXPORT_FILE"
  )
  echo "  Resume session: $RESUME_SESSION"
elif [[ "$RESUME_FLAG" == "--continue" ]]; then
  # Continue 模式：继续最近的 session
  DEVIN_CMD=(
    devin
    --permission-mode dangerous
    --print
    --continue
    --export "$EXPORT_FILE"
  )
  echo "  Continue most recent session"
else
  # 首次启动模式
  DEVIN_CMD=(
    devin
    --permission-mode dangerous
    --print
    --prompt-file "$PROMPT_FILE"
    --export "$EXPORT_FILE"
  )
fi

# 在 tmux 中启动 devin
# 设置 remain-on-exit=on，这样 devin 退出后 tmux 会话不消失，watchdog 可以检查退出状态
tmux new-session -d -s "$SESSION_NAME" -c "$WORKTREE_PATH" \
  "tmux set-option remain-on-exit on; $(printf '%q ' "${DEVIN_CMD[@]}")"

echo ""
echo "✅ Worker $WORKER_ID 已启动 (yolo 模式)"
echo "  查看会话: tmux attach -t $SESSION_NAME"
echo "  分离会话: Ctrl+B 然后 D"
echo "  终止会话: tmux kill-session -t $SESSION_NAME"
echo ""

# ===== 4. 启动 watchdog 监控 =====
echo "启动 watchdog 监控..."
bash "$PROJECT_DIR/tools/watchdog.sh" \
  --session "$SESSION_NAME" \
  --task-id "$TASK_ID" \
  --worker-id "$WORKER_ID" \
  --max-retries 5 \
  --cooldown 1800 \
  --poll-interval 30 &
WATCHDOG_PID=$!

echo "watchdog PID: $WATCHDOG_PID"
echo ""
echo "全部就绪。Worker 在 tmux 中运行，watchdog 在后台监控。"
