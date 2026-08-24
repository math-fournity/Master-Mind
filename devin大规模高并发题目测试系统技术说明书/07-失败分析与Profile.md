# 07 · 失败分析与 Profile

## 7.1 13 类 Verdict 体系

系统将每次解题的终态分为 13 类 verdict，归为四大类：

### 成功类

| verdict | 定义 | 检测方法 | 处理动作 |
|---|---|---|---|
| `candidate_solved` | 检测到真实 PROOF COMPLETE + 无工具调用 | `has_real_proof()` + `check_tool_use()` | ArangoDB problem 标记 `completed` |
| `answer_leak` | AI 检测到题目泄漏答案，输出 `ANSWER LEAK DETECTED` | 文本匹配 `ANSWER LEAK DETECTED` | 计入 completed（题目问题，不是 AI 能力） |

### 模型能力失败类（Profile 数据，不重试）

| verdict | 定义 | 检测方法 | 处理动作 |
|---|---|---|---|
| `ai_gave_up` | AI 主动放弃 | 匹配 `I CANNOT SOLVE` / `无法解决` / `I give up` 等 | ArangoDB problem 标记 `failed` |
| `failed_token_limit` | 输出达到 token 上限 | 匹配 `Send a message to continue` / `Response truncated` | 标记 `failed`，记录 `truncated_stall_seconds` |
| `failed_output_limit` | 输出长度限制 | 匹配 `max output token` | 标记 `failed` |
| `failed_thinking_spin` | thinking 死循环 | 超时且 `is_thinking()` 为 True | 标记 `failed` |
| `failed_no_proof` | session 结束但无 proof 也无错误标记 | session 不存在 + 无任何标记 | 标记 `failed` |
| `failed_stall` | 卡住超过 stall_time | `time.time() - last_activity > stall_time` 且非 thinking | 标记 `failed` |
| `failed_timeout` | 超过 timeout | `elapsed > timeout` 且非 thinking | 标记 `failed`（可能是基础设施） |
| `invalid_tool_use` | 有 proof 但检测到工具调用 | `has_real_proof()` + `check_tool_use()` 为 True | 标记 `failed`（运行无效） |

### 基础设施失败类（可重试）

| verdict | 定义 | 检测方法 | 处理动作 |
|---|---|---|---|
| `failed_connection` | 网络连接错误 | 匹配 `connection error` / `ECONNREFUSED` / `fetch failed` 等 | ArangoDB problem 回退 `pending` |
| `rate_limited` | API 限流 | 匹配 `429` / `Too Many Requests` | 回退 `pending` |
| `launch_error` | 启动失败 | `launch_devin_cli()` 抛异常 | 回退 `pending` |
| `dead_session` | Devin CLI 异常退出无 proof | pipe.log 有 `DEVIN_CLI_EXITED` 但无 proof | 回退 `pending` |

### 特殊类

| verdict | 定义 | 处理动作 |
|---|---|---|
| `answer_leak_in_input` | Runner 预检发现题目文本包含答案 | 不入 running，直接标记 failed |
| `empty_problem_text` | 题目文本为空 | 不入 running，直接标记 failed |
| `export_missing` | 终态确定但 export 文件未写完 | 标记但不重新入队（避免循环） |
| `crash_recovered` | 断电恢复时 session 已不存在 | 移到 failed 队列 |

## 7.2 失败分类常量

<ref_snippet file="~/master-mind-glm5.2-worktree/xishujuzhen/solver_harness/pipe/collector.py" lines="104-112" />

```python
# 基础设施失败（重试，不计入Profile）
INFRA_FAILURES = {"failed_connection", "rate_limited", "launch_error", "dead_session"}

# 模型能力失败（Profile数据，不重试）
MODEL_FAILURES = {
    "failed_token_limit", "failed_output_limit", "ai_gave_up",
    "failed_thinking_spin", "failed_no_proof", "failed_stall",
    "invalid_tool_use",
}
```

## 7.3 检测模式详解

### PROOF COMPLETE 标记检测

<ref_snippet file="~/master-mind-glm5.2-worktree/xishujuzhen/solver_harness/pipe/collector.py" lines="49-78" />

**关键**：必须排除提示词中的 PROOF COMPLETE。提示词模式：`"❭ 请按AGENTS.md中的题目直接解答...结尾输出 ### PROOF COMPLETE"`。

`find_ai_proof_marker()` 检查标记前后 80 字符的上下文，如果包含提示词特征（`结尾输出`、`请按AGENTS`、`Pro ·`、`直接在TUI中输出证明`），则跳过。

### AI 放弃标记

<ref_snippet file="~/master-mind-glm5.2-worktree/xishujuzhen/solver_harness/pipe/collector.py" lines="80-85" />

```python
AI_GAVE_UP_PATTERNS = [
    "I CANNOT SOLVE", "I cannot solve", "i cannot solve",
    "无法解决", "无法做出", "做不出来",
    "I give up", "i give up", "I'm unable", "无法完成",
    "### I CANNOT SOLVE THIS",
]
```

### Rate Limit 检测

<ref_snippet file="~/master-mind-glm5.2-worktree/xishujuzhen/solver_harness/pipe/collector.py" lines="86-89" />

```python
RATE_LIMIT_PATTERNS = ["rate limit", "rate_limit", "429", "Too Many Requests"]
TOKEN_LIMIT_PATTERNS = ["token limit", "context limit", "context_length", "maximum context",
                        "Response truncated", "max output token", "Send a message to continue"]
CONNECTION_PATTERNS = ["connection error", "ECONNREFUSED", "ETIMEDOUT", "socket hang up", "fetch failed"]
```

### Thinking 状态检测

<ref_snippet file="~/master-mind-glm5.2-worktree/xishujuzhen/solver_harness/pipe/collector.py" lines="154-170" />

1. 检查 devin cli 的 thinking 状态标记（`Thinking ·`、`Thinking...`、`⠐` 等）
2. 检查数学内容（LaTeX 符号、推理步骤）——≥2 个数学标记则为 thinking

## 7.4 Profile 构建（build_profile.py）

### 有效 verdict

<ref_snippet file="~/master-mind-glm5.2-worktree/xishujuzhen/solver_harness/pipe/build_profile.py" lines="38-58" />

**计入 Profile**（VALID_VERDICTS）：
- `candidate_solved` — 成功
- `ai_gave_up` — AI 主动放弃
- `failed_token_limit` — token 超限
- `failed_output_limit` — 输出长度限制
- `failed_thinking_spin` — thinking 死循环
- `failed_no_proof` — 没做完
- `failed_stall` — 卡住
- `answer_leak` — 答案泄漏（题目问题，不是 AI 能力）

**不计入 Profile**（INVALID_VERDICTS）：
- `failed_connection` / `rate_limited` / `launch_error` / `dead_session` — 基础设施失败
- `invalid_tool_use` — 运行无效
- `failed_timeout` — 超时（可能是基础设施）

### 用法

```bash
python build_profile.py --output profile.json
python build_profile.py --by-dataset   # 按数据集分组
python build_profile.py --by-tier      # 按难度分层
python build_profile.py --summary      # 汇总
```

### Profile 维度

- **按数据集** — 各数据集的 solved 率、放弃率、token_limit 率
- **按难度分层** — tier 1/2/3 的能力边界
- **按 verdict 分布** — 各类失败的比例
- **解题时间分布** — solve_time_seconds 的统计

## 7.5 失败查询工具

### query_failures.py

<ref_file file="~/master-mind-glm5.2-worktree/xishujuzhen/solver_harness/pipe/query_failures.py" />

```bash
python query_failures.py --summary              # 汇总统计
python query_failures.py --by-verdict           # 按 verdict 分类
python query_failures.py --by-dataset           # 按数据集分类
python query_failures.py --verdict failed_connection --limit 20  # 查特定 verdict
python query_failures.py --export --output failures.json         # 导出
```

### query_progress.py

查询整体进度和各数据集的完成情况。

### reclassify_failed.py

对已判定的失败进行重新分类——当检测逻辑更新后，对历史数据重新判定。

## 7.6 失败分析的数据源

失败分析需要结合三个数据源：

| 数据源 | 内容 | 查询方法 |
|---|---|---|
| ArangoDB `devin_problem_runs` | attempt 记录、verdict、审计字段 | AQL 查询 |
| Redis `math:failed` | failed 队列中的 JSON | `LRANGE` |
| 文件系统 | pane_snapshot、pipe.log、export | 按 exp_id 定位 |

### 典型查询：查某道题的所有 attempt

```python
aql = """
FOR a IN devin_problem_runs
  FILTER a.problem_id == '{problem_key}'
  SORT a.started_at ASC
  RETURN {exp_id: a.exp_id, verdict: a.verdict, runtime: a.runtime_seconds, 
          solve_time: a.solve_time_seconds, pane_snapshot: a.pane_snapshot}
"""
```

### 典型查询：查某类 verdict 的分布

```python
aql = """
FOR a IN devin_problem_runs
  FILTER a.batch_id == 'pipe-runner'
  FILTER a.verdict != null
  COLLECT verdict = a.verdict WITH COUNT INTO c
  SORT c DESC
  RETURN {verdict, count: c}
"""
```
