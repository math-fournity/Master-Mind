#!/bin/bash
# number.sh — 实时调整做题系统并发数量
#
# 用法:
#   bash number.sh 30    # 调整为30并发
#   bash number.sh 60    # 调整为60并发
#
# 原理: 写入Redis的math:config:concurrency键，
# runner在下次poll时（2-5秒内）自动读取新值，无需重启服务。
# 当前running的题不受影响，只影响后续新启动的题。

set -e
export PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

REPO=~/master-mind-glm5.2-worktree
PY=$REPO/.venv/bin/python3
export PYTHONPATH=$REPO/xishujuzhen/solver_harness/pipe

if [ -z "$1" ]; then
    echo "用法: bash number.sh <并发数>"
    echo "  bash number.sh 30    # 调整为30并发"
    echo "  bash number.sh 60    # 调整为60并发"
    exit 1
fi

CONCURRENCY=$1

if ! [[ "$CONCURRENCY" =~ ^[1-9][0-9]*$ ]]; then
    echo "❌ 并发数必须是正整数，当前输入: $CONCURRENCY"
    exit 1
fi

set -a; source $REPO/.env; set +a

$PY -c "
from redis_queue import get_redis
r = get_redis()
old = r.get('math:config:concurrency')
r.set('math:config:concurrency', $CONCURRENCY)
running = r.hlen('math:running')
print(f'并发数: {old} → {$CONCURRENCY}')
print(f'当前running: {running}')
if $CONCURRENCY > int(running) if running else 0:
    print(f'runner将逐步启动新题填充到{$CONCURRENCY}（3秒间隔，约{($CONCURRENCY - int(running)) * 3}秒填满）')
else:
    print(f'runner不再启动新题，等running自然结束到{$CONCURRENCY}以下后才开始新题')
"
