---
description: >
  批量测试数学题时的session隔离铁律。
  每道题必须是全新的devin cli session，禁止跨题上下文泄漏。
  WHEN to use: 用devin cli批量测试数学题时（fate_batch_test.py / matharena_batch_test.py等）。
  WHEN NOT to use: 单题GuidedLoop（GuidedLoop有自己的session管理）、非测试场景。
trigger: model_decision
---

# batch-test-session-isolation rule

## 铁律

**每道题必须是全新的devin cli session，禁止跨题上下文泄漏。**

## 原因

批量测试数学题时，如果devin cli能读到上一道题的结果文件（solutions.json/summary.json等），
AI可能从上一题的解答中获取线索，导致测试结果不可信——测出来的"做出来了"可能是抄上一题的，
而不是真正独立思考出来的。

## 实施规范

### 1. 不在work_dir下写任何结果文件

结果文件（solutions.json/summary.json/solutions_partial.json）只写到run_dir（Master repo内的runs/目录），
**禁止写到work_dir**（/data/math-agent-glm5.2-*）。

### 2. 每道题运行前清理work_dir

每道题调用`devin -p`之前，必须：
- 删除work_dir下的solutions.json/summary.json等结果文件
- 删除work_dir下的.devin/sessions目录（如果有）
- 确保work_dir下只有AGENTS.md和题目文件

### 3. 不使用-r参数

`devin -p`每次调用默认创建新session。禁止使用`-r`/`--resume`恢复之前的session。

### 4. export路径在run_dir

`--export`路径必须指向run_dir（Master repo内），不能指向work_dir。

## 违规后果

如果违反此规则，测试结果不可信——AI可能通过读取work_dir下的文件获取上一题的解答，
导致"做出来了"的题数虚高，无法真实定位AI的能力边界。
