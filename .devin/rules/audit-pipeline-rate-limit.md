---
description: >
  审计Pipeline的Rate Limit防护规则。运行audit_launcher.py / run_audit_pipeline.py时。
  WHEN to use: 运行审计Pipeline（audit_launcher.py / run_audit_pipeline.py）时。
  WHEN NOT to use: 不运行审计Pipeline的日常操作。
trigger: model_decision
---

# 审计Pipeline的Rate Limit防护规则

> **触发条件**：运行audit_launcher.py / run_audit_pipeline.py时
> **核心约束**：运行审计pipeline前必须检查当前devin cli进程数，并据此设置并发

## 铁律1：运行前检查进程数

启动audit pipeline前，必须检查当前有多少个devin cli进程在运行：

```bash
ps aux | grep "devin" | grep -v grep | grep -v "monitor_pipe" | wc -l
```

| 进程数 | 建议并发 | 说明 |
|---|---|---|
| ≤3 | 3 | 可以用3并发 |
| 4-8 | 2 | 降并发到2 |
| >8 | 1 | 只能用1并发 |
| >20 | 0 | 暂不要启动，先清理进程 |

**原因**：rate limit是账户级的，跨所有CLI实例共享。24个进程+3并发audit = 触发rate limit。

## 铁律2：rate limit自动暂停

audit_launcher.py中已实现rate limit自动暂停机制：
- 检测到rate_limited时，暂停20分钟
- 暂停期间不启动新session
- 不要禁用此机制

## 铁律3：failed_stall重跑

如果出现failed_stall（session无输出被判定为stall），需要重新入队重跑：

```python
# 重置失败状态为prepared
aql = """
FOR run IN audit_runs
  FILTER run.batch_id == @bid
  FILTER run.status IN ['rate_limited', 'failed_stall', 'failed_connection', 'dead_session']
  UPDATE run WITH {status: 'prepared'} IN audit_runs
"""
# 然后重新入队prepared的任务到Redis
```

**注意**：failed_stall可能是API不可用但错误信息不含rate limit关键词导致的。重跑时如果API已恢复，通常能正常完成。

## 铁律4：选题只用completed结果

后续选题工作只用status=completed的审计结果。failed_stall/rate_limited的结果不可用——这些任务没有产出审计结果。

## 详细根因分析

见 `dev-docs/388-v0-2026-08-17-audit-full1-rate-limit根因分析与处理记录.md`
