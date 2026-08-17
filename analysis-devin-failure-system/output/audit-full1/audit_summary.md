# audit-full1 审计总结

> **生成时间**：2026-08-17 04:30 UTC
> **审计批次**：audit-full1
> **总题数**：1521
> **审计目标**：对解题系统中运行错误的1521个题目，审计其分析结果的质量

---

## 1. 当前进度

| 状态 | 数量 | 说明 |
|---|---|---|
| completed | 1385 | 已完成审计，结果已收集到audit_results集合 |
| prepared | 135 | 重新入队中（原failed_stall/rate_limited），并发1运行中 |
| running | 1 | 正在审计 |
| **总计** | **1521** | |

**1385个completed的审计结果可直接用于后续选题工作。** 135个prepared正在重跑中。

---

## 2. 审计结果分布（1384个已收集）

| audit_status | 数量 | 占比 | 说明 |
|---|---|---|---|
| **PASS_SELECTABLE** | **721** | **52.1%** | **可进入选题池**——d1=DIRECTION_ERROR/PARTIAL_PROGRESS + 全检查通过 |
| PASS | 358 | 25.9% | 通过但不可选题——d1=CONNECTION_ERROR/TOKEN_LIMIT |
| FAIL_INCOMPLETE | 133 | 9.6% | 数据不完整（字段为null或过短） |
| FAIL_CONTENT_CORRUPT | 113 | 8.2% | 内容损坏（XML标签泄漏等） |
| FAIL_PARSE_ERROR | 40 | 2.9% | d1为null或无效值 |
| PASS_NOT_SELECTABLE | 15 | 1.1% | 通过但D检查失败（动词/数学术语不足） |
| FAIL_INCONSISTENT | 4 | 0.3% | d1/d2内部不一致 |
| no_output | 1 | 0.1% | session无输出 |

### 2.1 后处理修正

以下后处理已在audit_result_collector.py中实现：

1. **D1动词列表扩展**：原动词列表过窄（10个词），导致DIRECTION_ERROR题被误判PASS_NOT_SELECTABLE。扩展后含"misread/misinterpreted/began/proceeded"等，修正后升级为PASS_SELECTABLE。
2. **PASS_SELECTABLE定义扩展**：原定义只限d1=DIRECTION_ERROR，扩展后d1=PARTIAL_PROGRESS + D全PASS也升级为PASS_SELECTABLE。

### 2.2 选题可用结果

**721个PASS_SELECTABLE**是选题的核心输入。这些题目的分析结果：
- d1=DIRECTION_ERROR或PARTIAL_PROGRESS（AI走错方向或部分进展）
- A-E全检查通过
- D1-D4操作性格检查通过（解释含动作动词+数学术语）
- 适合用于提取tell信号和构建选题池

---

## 3. 已处理/未处理边界

### 3.1 已处理

- ✅ 1385个审计完成，结果已收集到audit_results集合
- ✅ 后处理修正（D1动词列表+PASS_SELECTABLE定义）已应用
- ✅ Rate limit根因已分析，自动暂停机制已实现
- ✅ 145个failed_stall已重新入队
- ✅ 48个历史alert已处理并标记fixed

### 3.2 未处理（正在运行）

- ⏳ 135个prepared任务在并发1下重跑中（预计2小时完成）
- ⏳ 重跑完成后需要再次运行audit_result_collector收集新结果

### 3.3 已知未修复的问题

1. **stall检测无法识别静默卡住**：devin cli在API不可用时可能不输出错误信息，导致stall检测无法区分"AI在思考"和"API卡住"
2. **RATE_LIMIT_PATTERNS可能不完整**：非标准错误信息无法被检测到
3. **15个PASS_NOT_SELECTABLE**：这些题的分析结果通过基础检查但D检查失败，不进入选题池。如果需要扩大选题池，可以人工review这些题

---

## 4. 未来AI接手指南

### 4.1 如果审计还在运行

```bash
# 检查状态
./analysis-devin-failure-system/scripts/monitor_check.sh audit-full1

# 如果launcher NOT RUNNING但prepared>0，重启launcher
tmux new-session -d -s audit-launcher "cd ~/master-mind-glm5.2-worktree && .venv/bin/python3 analysis-devin-failure-system/run_audit_pipeline.py --batch-id audit-full1 --step launch --concurrency 1 2>&1 | tee /tmp/audit-full1-launch.log; sleep 999999"
```

### 4.2 如果审计已全部完成

```bash
# 确认状态
.venv/bin/python3 -c "
import sys; sys.path.insert(0, 'analysis-devin-failure-system')
from src.db_schema import connect_db
db = connect_db()
aql = 'FOR run IN audit_runs FILTER run.batch_id == @bid COLLECT status = run.status WITH COUNT INTO c RETURN {status, count: c}'
for r in db.aql.execute(aql, bind_vars={'bid': 'audit-full1'}, ttl=60):
    print(f'{r[\"status\"]}: {r[\"count\"]}')
"
# 应该看到 completed: 1521, 其他都是0

# 收集审计结果
cd analysis-devin-failure-system && ../.venv/bin/python3 -m src.audit_result_collector --batch-id audit-full1

# 然后用721个PASS_SELECTABLE做选题
```

### 4.3 选题工作

选题只用audit_status=PASS_SELECTABLE的结果（721个）。查询：

```python
aql = "FOR r IN audit_results FILTER r.batch_id == 'audit-full1' FILTER r.audit_status == 'PASS_SELECTABLE' RETURN r"
```

---

## 5. 相关文件

| 文件 | 说明 |
|---|---|
| `dev-docs/388号` | Rate limit根因分析与处理记录 |
| `.devin/rules/audit-pipeline-rate-limit.md` | Rate limit防护规则 |
| `.devin/rules/pipeline-monitor-sop.md` | Monitor Pipe监控SOP |
| `analysis-devin-failure-system/scripts/monitor_check.sh` | 标准化检查脚本 |
| `analysis-devin-failure-system/src/audit_launcher.py` | 审计launcher（含rate limit自动暂停） |
| `analysis-devin-failure-system/src/audit_result_collector.py` | 审计结果收集器（含后处理修正） |
| `analysis-devin-failure-system/output/audit-full1/audit_results_summary.json` | 审计结果摘要 |
