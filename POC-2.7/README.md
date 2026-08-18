# POC-2.7 截断vs思维错误——系统运行与检查指南

**方案文档**：`Tell分类学研究过程文档/415-v0-2026-08-18-POC-2.7-截断vs思维错误.md`
**进度报告**：`POC-2.7/POC-2.7-001-完整进度报告.md`
**审计SOP**：`POC-2.7/POC-2.7-002-方案文档与执行记录差异审计SOP.md`

**核心问题**：在续传机制下，被Pipe 1判定为"方向错误"（DIRECTION_ERROR）的948道题，有多少是真正的思维错误，有多少只是被截断的thinking spin？

**通过标准**（415号§7.1）：948道题中COMPLETED≥50% → 续传能解决至少一半的DIRECTION_ERROR题。

---

## 系统架构——Pipe 4（续传Pipe）+ Monitor Pipe

POC-2.7的批量续传采用错题分析系统的Pipe 4实现（独立自包含模式），配合Monitor Pipe设计范式（详见`MonitorPipe.md`）。

### 三层架构

| 层 | 文件 | 用途 |
|---|---|---|
| 规范层 | `analysis-devin-failure-system/specs/p27_monitor_spec.md` (242行) | 检查规范——A类自动检查(9项)/B类续传质量检查(7项)/C类AI review抽样(5项) |
| 执行层 | `analysis-devin-failure-system/src/monitor_continuation.py` (748行) | Monitor Pipe守护进程——按规范执行16项检查，写alert到DB |
| 查询层 | `analysis-devin-failure-system/scripts/monitor_check_continuation.sh` (241行) | 检查脚本——Master AI每次检查都调用，输出6项检查+行动清单 |

### Pipe 4的8个核心文件

| 文件 | 用途 |
|---|---|
| `src/continuation_config.py` | 配置常量（路径/DB/并发/阈值/Redis前缀`p27:`/tmux前缀`p27-`） |
| `src/continuation_db_schema.py` | ArangoDB集合定义（`p27_continuation_runs`/`p27_continuation_batches`等） |
| `src/continuation_redis_queue.py` | Redis队列操作（`p27:pending`/`p27:completed`/`p27:failed`） |
| `src/continuation_collector.py` | 数据收集——从problem_list.json加载919道题+创建run记录 |
| `src/continuation_feeder.py` | 入Redis队列 |
| `src/continuation_launcher.py` | **核心**——并发启动devin cli+stall/rate_limit/zombie检测+多轮续传 |
| `src/continuation_result_collector.py` | 结果收集+通过率判定+Markdown汇总 |
| `run_continuation_pipeline.py` | 端到端入口（collect→feed→launch→collect-results） |

---

## 运行方法

### 前置条件

```bash
# 1. ArangoDB运行中
docker ps | grep arangodb || docker start arangodb

# 2. D盘已挂载（原始做题的export和题目文件在D盘）
ls /data/math-agent-glm5.2-tmux-agents-trajectory/ | head -3

# 3. problem_list.json已导出（919道有export的DIRECTION_ERROR题）
ls "Tell分类学研究过程文档/poc_assets/poc_2.7/poc_2.7/problem_list.json"
# 如果不存在，先导出：
# .venv/bin/python3 "Tell分类学研究过程文档/poc_assets/poc_2.7/batch_continue_948.py" export-list
```

### 启动全量续传（919题）

```bash
cd ~/master-mind-glm5.2-worktree/analysis-devin-failure-system

# 端到端启动（collect→feed→launch一步到位）
# 并发5（保守，v2方案约8天）
.venv/bin/python3 run_continuation_pipeline.py \
  --batch-id p27-full \
  --step all \
  --concurrency 5 \
  --max-rounds 5 \
  --method v2

# 或分步执行：
# .venv/bin/python3 run_continuation_pipeline.py --batch-id p27-full --step collect
# .venv/bin/python3 run_continuation_pipeline.py --batch-id p27-full --step feed
# .venv/bin/python3 run_continuation_pipeline.py --batch-id p27-full --step launch --concurrency 5
```

### 启动Monitor Pipe（独立tmux session）

```bash
# Monitor Pipe在独立tmux session中运行，每2分钟检查一轮
tmux new-session -d -s monitor-p27 \
  "cd ~/master-mind-glm5.2-worktree/analysis-devin-failure-system && \
   ~/master-mind-glm5.2-worktree/.venv/bin/python3 -m src.monitor_continuation \
     --batch-id p27-full --interval 120 --concurrency 5"
```

### 小批量测试（10题）

```bash
cd ~/master-mind-glm5.2-worktree/analysis-devin-failure-system
.venv/bin/python3 run_continuation_pipeline.py \
  --batch-id p27-test --step all --limit 10 --concurrency 5 --max-rounds 5 --method v2

# 启动Monitor Pipe监控小批量
tmux new-session -d -s monitor-p27-test \
  "cd ~/master-mind-glm5.2-worktree/analysis-devin-failure-system && \
   ~/master-mind-glm5.2-worktree/.venv/bin/python3 -m src.monitor_continuation \
     --batch-id p27-test --interval 60 --concurrency 5"
```

---

## 检查方法

### 标准化检查（Master AI每次检查都调用此脚本）

```bash
cd ~/master-mind-glm5.2-worktree
bash analysis-devin-failure-system/scripts/monitor_check_continuation.sh p27-full
```

**输出6项检查**：
1. **Monitor Pipe pane输出**——最近5轮的ALERT/AI_REVIEW/status/progress
2. **alerts集合**——所有新alert的详情（按`specs/p27_monitor_spec.md` §2分类）
3. **进程状态**——launcher + monitor_continuation + p27- session数
4. **进度**——DB状态分布 + final_status分布 + 通过率
5. **续传质量汇总**——proof.md统计 + HANDOVER.md统计 + 截断模式统计
6. **通过率判定**——对照415号§7.1（COMPLETED≥50%）

**最后附8步行动清单**——提醒Master AI去检查Monitor Pipe的alerts并处理。

### 查看新alerts

```bash
cd ~/master-mind-glm5.2-worktree/analysis-devin-failure-system
.venv/bin/python3 -m src.monitor_continuation --batch-id p27-full --check-alerts
```

### 标记alert为已解决

```bash
.venv/bin/python3 -m src.monitor_continuation --batch-id p27-full --resolve-alert <alert_key>
```

### 查看Monitor Pipe的tmux pane输出

```bash
tmux capture-pane -t monitor-p27 -p -S -200 | grep -E "监控轮次|ALERT|AI_REVIEW|status|progress|final_status|pass_rate" | tail -30
```

---

## alert分类与处理（详见`specs/p27_monitor_spec.md`）

### A类自动检查（9项，脚本判定）

| alert_type | severity | 处理方法 |
|---|---|---|
| session_health | critical | launcher可能挂了→检查进程状态→重启launcher |
| queue_stalled | critical | collector没在处理→检查launcher日志 |
| rate_limit | critical | 立即降并发（修改batch.concurrency） |
| zombie_sessions | warning | 手动kill空pane session |
| export_missing | critical | 检查D盘挂载、trajectory目录可写 |
| failure_rate | warning | 检查failure_breakdown，判断AI能力问题还是基础设施问题 |
| launcher_dead | critical | 重启launcher |
| long_running | warning | 检查是否真的stall，可能需要kill后重新入队 |

### B类续传质量检查（7项，脚本判定）

| alert_type | severity | 处理方法 |
|---|---|---|
| proof_missing | critical | COMPLETED但无proof.md→重跑 |
| proof_no_boxed | warning | proof.md无boxed答案→检查是否真正完成 |
| proof_too_small | warning | proof.md太小→可能内容不完整 |
| handover_missing | critical | v2方案但无HANDOVER.md→Pipe A失败 |
| all_rounds_truncated | warning | 5轮全截断→可能是真正的思维错误 |
| status_anomaly | info | final_status分布异常→数据/机制问题 |

### C类AI review抽样（5项，需Master AI判断）

每3轮抽样2条COMPLETED结果，Master AI需检查：
- **C1. proof_quality**——proof.md的数学正确性
- **C2. proof_hallucination**——是否有幻觉
- **C3. answer_leak**——是否答案泄漏
- **C4. handover_quality**——HANDOVER.md是否准确
- **C5. continuation_direction**——续传方向是否正确

---

## 关键路径

| 路径 | 用途 |
|---|---|
| `analysis-devin-failure-system/src/continuation_*.py` | Pipe 4核心代码（8个文件） |
| `analysis-devin-failure-system/src/monitor_continuation.py` | Monitor Pipe守护进程 |
| `analysis-devin-failure-system/specs/p27_monitor_spec.md` | 检查规范（系统资产） |
| `analysis-devin-failure-system/scripts/monitor_check_continuation.sh` | 检查脚本 |
| `analysis-devin-failure-system/run_continuation_pipeline.py` | 端到端入口 |
| `Tell分类学研究过程文档/poc_assets/poc_2.7/poc_2.7/problem_list.json` | 919道题列表 |
| `Tell分类学研究过程文档/poc_assets/poc_2.7/batch_continue_948.py` | 原始批量脚本（已被Pipe 4替代） |
| ArangoDB `p27_continuation_runs`集合 | run状态记录 |
| ArangoDB `p27_continuation_batches`集合 | batch配置 |
| ArangoDB `p27_monitor_alerts`集合 | Monitor Pipe的alert |
| Redis `p27:pending`/`p27:completed`/`p27:failed` | 队列 |
| tmux `p27-{problem_id}-r{round_num}` | 每个续传run的session |
| tmux `monitor-p27` | Monitor Pipe的session |

---

## 停止系统

```bash
# 停止launcher
cd ~/master-mind-glm5.2-worktree/analysis-devin-failure-system
.venv/bin/python3 run_continuation_pipeline.py --batch-id p27-full --step stop

# 停止Monitor Pipe
tmux kill-session -t monitor-p27

# 清理残留的p27- session
tmux list-sessions | grep "^p27-" | cut -d: -f1 | xargs -I{} tmux kill-session -t {}
```

---

## 设计范式参考

- **Monitor Pipe设计范式**：`MonitorPipe.md`（项目repo根目录）——三层架构（规范层+执行层+查询层）
- **全局rule**：`~/.config/devin/rules/monitor-pipe-design-paradigm.md`——always-on
- **错题分析系统代码资产**：`MonitorPipe.md` §4/§6有完整的文件清单和行数
