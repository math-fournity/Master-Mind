#!/bin/bash
# POC-2.5 批量启动脚本
# 用 noninteractive-solver-run skill 的标准方案：
# devin -p --prompt-file ... --export ... 在 tmux 中运行
# export 的 reasoning_content 包含完整 thinking

PROBLEMS_DIR="/tmp/poc2.5/problems"
WORK_BASE="/tmp/poc2.5/workdirs"
TRAJ_BASE="/tmp/poc2.5/trajectories"

# 16个run（CC101-bare已经在运行，跳过）
RUNS=(
  "CC-101:bare"
  "CC-101:vein"
  "CC-101:vein_hint"
  "CC-101:hint"
  "CC-103:bare"
  "CC-103:vein"
  "CC-103:vein_hint"
  "CC-103:hint"
  "CC-104:bare"
  "CC-104:vein"
  "CC-104:vein_hint"
  "CC-104:hint"
  "CC-105:bare"
  "CC-105:vein"
  "CC-105:vein_hint"
  "CC-105:hint"
)

for entry in "${RUNS[@]}"; do
  cc_id="${entry%%:*}"
  cond="${entry##*:}"
  exp_id="p25-${cc_id}-${cond}"
  problem_file="${PROBLEMS_DIR}/${cc_id}_${cond}.txt"
  work_dir="${WORK_BASE}/${exp_id}"
  traj_dir="${TRAJ_BASE}/${exp_id}"
  export_path="${traj_dir}/exports/conversation.json"
  tmux_name="${exp_id}"

  # 跳过已运行的
  if tmux has-session -t "${tmux_name}" 2>/dev/null; then
    echo "SKIP ${exp_id} (already running)"
    continue
  fi

  # 创建目录
  mkdir -p "${work_dir}" "${traj_dir}/exports"

  # 复制problem文件
  cp "${problem_file}" "${work_dir}/input.txt"

  # 启动tmux session
  tmux new-session -d -s "${tmux_name}" \
    "cd ${work_dir} && devin -p \
      --prompt-file ${work_dir}/input.txt \
      --model glm-5-2 \
      --respect-workspace-trust false \
      --permission-mode dangerous \
      --export ${export_path}; \
      echo DEVIN_CLI_EXITED code=\$?; \
      sleep 30"

  echo "LAUNCHED ${exp_id} (tmux: ${tmux_name})"
  sleep 3  # 间隔3秒避免同时启动冲击
done

echo ""
echo "=== All launched ==="
echo "Check status: tmux list-sessions | grep p25"
