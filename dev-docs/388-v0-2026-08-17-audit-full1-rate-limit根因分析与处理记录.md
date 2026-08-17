# 388号：audit-full1 Rate Limit根因分析与处理记录

> **2026-08-16 ~ 2026-08-17，audit-full1全量审计（1521题）运行过程中的rate limit问题根因分析、处理措施、已处理/未处理边界。**
> **未来AI接手审计/选题工作时，先读本文件了解哪些问题已处理、哪些未处理。**

---

## 1. 背景

audit-full1对1521个解题失败结果做质量审计。审计由audit_launcher.py驱动，每个审计任务启动一个devin cli实例（tmux session），让审计AI检查分析结果的质量（5维度21检查项）。

审计过程中遭遇了三轮rate limit，导致大量任务失败。本文档记录根因分析和处理措施。

---

## 2. Rate Limit根因

### 2.1 错误信息

devin cli启动后立即返回：
```
Error: Agent error: Permission denied: Permission denied: Reached overall message rate limit. 
Please try again later. Your limit will reset in 20 minutes.
(trace ID: xxx)
"cognition.ai/errorKind": "internal"
"cognition.ai/retryable": true
```

### 2.2 根本原因：账户级overall message rate limit

**Rate limit是账户级别的，跨所有CLI实例共享。** 同一账户上所有devin cli进程的消息请求加在一起计算，超过rolling window限制后，所有新session被拒20分钟。

2026-08-16运行audit-full1时，系统中有**24个devin cli相关进程**在同时运行：

| 启动时间 | 数量 | 说明 |
|---|---|---|
| 8月8日 | 1 | 长期运行的devin cli |
| Mon | 6 | 4个`devin -r` + 2个`devin acp` |
| Tue | 2 | 长期运行 |
| Wed | 2 | 长期运行 |
| Thu | 1 | 长期运行 |
| 当天 | 10+ | audit pipeline + solver + 分析session + 我自己 |

这些进程即使空闲也在发送API请求（心跳/状态检查），持续消耗账户配额。audit的并发session加入后，总消息量超过限制。

### 2.3 三轮rate limit时间线

| 轮次 | 并发 | 触发时间(UTC) | rate_limited数 | 完成数 | 恢复时间 |
|---|---|---|---|---|---|
| 第1轮 | 5 | ~06:00 | 735 | 465 | 自动恢复 |
| 第2轮 | 3 | 07:27 | 344 | 800 | 07:50（22分钟） |
| 第3轮 | 1 | — | 0 | — | 未触发 |

**关键数据**：并发5时完成465个就触发；并发3时完成800个才触发；并发1时未触发。

### 2.4 zcode AI的rate limit交叉验证

2026-08-17 04:10 UTC，zcode AI（另一个CLI实例）尝试运行，4次rate_limited后turn failed退出。这进一步确认了rate limit是账户级共享的——audit pipeline在运行时，zcode AI加入后立即触发。

---

## 3. 145个failed_stall的根因

### 3.1 现象

145个session被判定为failed_stall，runtime全部是93s或103s（stall检测阈值120s），tmux.log不存在（session无任何输出）。

### 3.2 时间分布

- 09:00-09:58 UTC: 26个completed + 25个stall（约50%成功率）
- **10:00-13:58 UTC: 0个completed + 120个stall（100%失败，持续4小时）**
- 14:00-15:03 UTC: 91个completed + 0个stall（100%成功）

### 3.3 根因

10:00-14:00这4小时内，devin cli启动后无法连接API，但**错误信息不包含rate limit关键词**（rate limit / 429 / Too Many Requests），所以没有被audit_launcher的RATE_LIMIT_PATTERNS检测到。session无任何pane变化，被stall检测判定为failed_stall。

推测原因：API返回了非rate-limit的连接错误（如超时、5xx），或者devin cli在rate limit状态下静默卡住不输出错误信息。

### 3.4 处理措施

145个failed_stall + 2个rate_limited已重新入队，并发1重跑。截至2026-08-17 04:24 UTC，已完成2个，0新失败。

---

## 4. 处理措施

### 4.1 已实施的代码修正

1. **rate limit自动暂停机制**（audit_launcher.py）
   - 检测到rate_limited时，暂停20分钟（匹配错误信息中的reset时间）
   - 暂停期间不启动新session，每60秒检查一次是否恢复

2. **并发从5→3→1逐步降低**
   - 最终并发1，在24个其他devin cli进程存在的情况下不触发rate limit

3. **标准化检查脚本**（monitor_check.sh）
   - 4项检查打包成一个命令
   - 每个检查项后附带"需要检查"提示+5步行动清单

### 4.2 已知但未修复的问题

1. **stall检测无法识别静默卡住**
   - devin cli在API不可用时可能不输出错误信息，导致stall检测无法区分"AI在思考"和"API卡住"
   - 改进方向：检查devin cli进程是否在消耗CPU，或者检查进程是否在等待I/O

2. **RATE_LIMIT_PATTERNS可能不完整**
   - 当前只检测"rate limit"/"429"/"Too Many Requests"等关键词
   - 如果API返回非标准错误信息，无法被检测到
   - 改进方向：增加连接超时模式检测，或者检查devin cli进程状态

---

## 5. 已处理/未处理边界（未来AI必读）

### 5.1 已处理的审计结果（可用于后续选题）

截至2026-08-17 04:24 UTC：

| 状态 | 数量 | 说明 |
|---|---|---|
| completed | 1376 | 已完成审计，结果在audit_results集合中 |
| prepared | 145 | 重新入队中，并发1运行中 |

**1376个completed的审计结果可以直接用于后续选题工作。** 不需要等145个全部跑完。

### 5.2 审计结果的后处理修正

以下审计状态需要后处理修正（在audit_result_collector.py中已实现）：

1. **D1动词列表过窄**：d1=DIRECTION_ERROR但d1_exp中不含初始动词列表的词 → 后处理扩展动词列表后升级为PASS_SELECTABLE
2. **PASS_SELECTABLE定义不完整**：d1=PARTIAL_PROGRESS + D全PASS → 后处理升级为PASS_SELECTABLE

### 5.3 未处理的问题

1. **145个failed_stall正在重跑**：并发1运行中，预计2小时完成
2. **stall检测的静默卡住问题**：未修复，下次可能再次出现
3. **RATE_LIMIT_PATTERNS不完整**：未修复，非标准错误信息无法被检测

### 5.4 未来AI接手时的操作步骤

1. 先运行 `./analysis-devin-failure-system/scripts/monitor_check.sh audit-full1` 检查当前状态
2. 如果prepared=0且completed=1521，全量审计完成，可以开始选题
3. 如果prepared>0，审计还在运行，等完成或检查launcher是否在运行
4. 如果launcher NOT RUNNING但prepared>0，重启launcher（见rule文件）
5. 选题时只用status=completed的审计结果，不用failed_stall/rate_limited的

---

## 6. 相关文件

- 规则文件：`.devin/rules/audit-pipeline-rate-limit.md`
- 检查脚本：`analysis-devin-failure-system/scripts/monitor_check.sh`
- 自动暂停代码：`analysis-devin-failure-system/src/audit_launcher.py`（rate_limit_paused_until逻辑）
- Rate limit检测模式：`analysis-devin-failure-system/src/config.py`（RATE_LIMIT_PATTERNS）
- 监控SOP：`.devin/rules/pipeline-monitor-sop.md`
