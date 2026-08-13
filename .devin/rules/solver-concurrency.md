# Solver AI 并发约束

**硬约束**：runner启动devin cli时**每3秒启动1个，不可改**。并发数通过Redis实时调整，推荐50-60。

## 铁律：3秒启动间隔不可改

**runner.py第333行的`time.sleep(3)`是铁律，不可修改。**

- 每个devin cli启动后固定等3秒再启动下一个
- 这是防止API rate limit的关键——并行启动60个session会导致58/60个遇到rate limit
- 3秒间隔意味着：填满60并发需要180秒（3分钟），填满80并发需要240秒（4分钟）
- **恢复慢是正常的**——collector清理完积压session后，runner按3秒间隔逐步填充，不是bug

## 并发上限经验（管道化系统实测，2026-08-13）

> 旧batch系统（batch_problem_runner）的并发经验已过时——60并发51%雪崩是旧系统的数据，
> 管道化系统架构不同（独立tmux session+collector轮询+3秒间隔启动），已验证60并发稳定运行。

| 并发 | 吞吐 | solved率 | dead率 | rate limit | 结论 |
|---|---|---|---|---|---|
| 40 | 257题/时 | 56% | 23% | 0 | 稳定，但吞吐低 |
| 50 | 360题/时 | 63% | 11% | 0 | 稳定 |
| 60 | 465题/时 | 65% | 9% | 0 | **最优** |
| 80 | 待观察 | — | — | — | 待验证 |
| 100 | 729题/时 | 62% | 6% | 15个 | 吞吐最高但触发限流 |

**推荐并发：50-60。60并发是最优平衡点（吞吐高+无限流+solved率最高）。**

## 并发调整

通过Redis实时调整，不需要重启runner：
```
PYTHONPATH=xishujuzhen/solver_harness/pipe .venv/bin/python3 -c "
from redis_queue import get_redis
r = get_redis()
r.set('math:config:concurrency', 60)
"
```

runner每轮poll从Redis读取`math:config:concurrency`，实时生效。

## 检查并发数

```bash
# Redis中的并发设定值
PYTHONPATH=xishujuzhen/solver_harness/pipe .venv/bin/python3 -c "from redis_queue import get_redis; r=get_redis(); print(r.get('math:config:concurrency'))"

# 实际running数
PYTHONPATH=xishujuzhen/solver_harness/pipe .venv/bin/python3 -c "from redis_queue import get_redis; r=get_redis(); print(r.hlen('math:running'))"

# tmux session数
tmux list-sessions | grep "harness-" | grep -v dbmon | wc -l
```

## 适用于

- 所有通过 `solver-harness launch` 启动的 Solver AI
- 管道化系统（feeder/runner/collector/reporter/retry五服务）
- 树生长引擎（tree_engine.py）——静态编排和动态编排都适用
- A/B 对照实验
