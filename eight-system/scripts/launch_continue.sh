#!/bin/bash
# launch_continue.sh: 为hit token limit的arm启动continue实验
# 用法: bash launch_continue.sh

set -e

WORKTREE="~/master-mind-glm5.2-worktree"
AGENTS_DIR="/data/math-agent-glm5.2-tmux-agents-dir"
TRAJECTORY_DIR="/data/math-agent-glm5.2-tmux-agents-trajectory"
MITM_PORT=18889
CA_CERT="$HOME/.mitmproxy/mitmproxy-ca-cert.pem"

# Session IDs (from sessions.db lookup)
declare -A SESSION_IDS
SESSION_IDS["1843-R"]="veiled-captain"
SESSION_IDS["1843-L"]="living-reference"
SESSION_IDS["1843-D"]="honey-click"
SESSION_IDS["1843-LD"]="living-reference"
SESSION_IDS["1709-R"]="jasper-zone"
SESSION_IDS["1709-D"]="married-vulcanodon"
SESSION_IDS["1962-R"]="standing-crab"
SESSION_IDS["1962-L"]="zesty-flier"
SESSION_IDS["1962-D"]="veil-couch"
SESSION_IDS["1962-LD"]="seemly-fiber"

# 1709-L and 1709-LD succeeded, skip continue for them

for key in "${!SESSION_IDS[@]}"; do
    prob=$(echo "$key" | cut -d- -f1)
    arm=$(echo "$key" | cut -d- -f2)
    exp_id="eight-p1-${prob}-${arm}-continue"
    sid="${SESSION_IDS[$key]}"
    sdir="${AGENTS_DIR}/eight-p1-${prob}-${arm}"
    tdir="${TRAJECTORY_DIR}/${exp_id}"
    tname="harness-${exp_id}"

    # Create trajectory dir
    mkdir -p "${tdir}/mitm" "${tdir}/tmux" "${tdir}/exports"

    # Build devin continue command
    export_path="${tdir}/exports/conversation.json"
    tmux_pipe_path="${tdir}/tmux/tmux_pipe.log"
    tmux_log_path="${tdir}/tmux/tmux.log"

    devin_cmd="devin -r ${sid} --model glm-5-2 --respect-workspace-trust false --permission-mode dangerous --export ${export_path}; echo DEVIN_CLI_EXITED code=\$?; sleep 999999"

    env_prefix="HTTPS_PROXY=http://localhost:${MITM_PORT} HTTP_PROXY=http://localhost:${MITM_PORT} NODE_EXTRA_CA_CERTS=${CA_CERT} "
    full_cmd="cd ${sdir} && ${env_prefix}${devin_cmd} 2>&1 | tee ${tmux_log_path}"

    # Launch in tmux
    tmux new-session -d -s "$tname" "$full_cmd"
    sleep 0.5
    tmux pipe-pane -t "$tname" "cat >> ${tmux_pipe_path}"

    echo "Launched continue: $exp_id (session: $sid, tmux: $tname)"
done

echo "All 10 continue experiments launched."
