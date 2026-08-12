# Solver批量集群健康检查铁律

**触发条件**：用户说"检查进度"、"看看有没有问题"、"检查链接问题"、"检查并发"时；批量Solver集群运行时；新session接手批量系统时。

**核心约束**：检查批量集群时必须到最前线——不能只看DB status数字，必须看tmux pane内容、文件实际大小、进程实际状态。

## 三条铁律

### 铁律1：用batch_status.py，不现写脚本

```bash
set -a; source .env; set +a
.venv/bin/python xishujuzhen/solver_harness/batch_status.py status   # 总状态
.venv/bin/python xishujuzhen/solver_harness/batch_status.py active   # 活跃度
.venv/bin/python xishujuzhen/solver_harness/batch_status.py errors   # 错误分析
.venv/bin/python xishujuzhen/solver_harness/batch_status.py solved   # 已解决
.venv/bin/python xishujuzhen/solver_harness/batch_status.py feed     # feed事件
.venv/bin/python xishujuzhen/solver_harness/batch_status.py leak     # 泄漏检查
.venv/bin/python xishujuzhen/solver_harness/batch_status.py dead     # 僵尸session检测
.venv/bin/python xishujuzhen/solver_harness/batch_status.py dead --cleanup  # 自动清理僵尸session
.venv/bin/python xishujuzhen/solver_harness/batch_status.py all      # 全部（不含dead）
```

新增查询需求时更新batch_status.py，不另写脚本。

### 铁律2：DB status数字会骗人，必须到最前线

DB显示`running`不代表Solver在工作。必须验证三个层面：

1. **tmux pane内容**——`tmux capture-pane -t <session> -p`，pane空白=Devin CLI已退出（僵尸session）
2. **文件实际大小**——thinking_readable_path和tmux_pipe_path的大小，0KB=没产出
3. **idle时间真实性**——activity_signature可能因tmux_log_path变化永远在变，导致idle永远=0

### 铁律3：发现问题先修batch_status.py再修batch_problem_runner.py

检查脚本和监控代码是两层。batch_status.py是检查工具，batch_problem_runner.py是监控逻辑。发现问题后：
1. 先在batch_status.py中加检测命令（让下次能一键发现）
2. 再在batch_problem_runner.py中修监控逻辑（让monitor能自动处理）

## 并发上限经验（实测）

| 并发 | 连接错误率 | 性质 | 结论 |
|---|---|---|---|
| 10 | ~0% | 稳定 | 最安全 |
| 30 | ~6.7% | 偶发瞬时断连，Solver可恢复 | 可接受 |
| 40 | 未充分测试 | — | 需验证 |
| 60 | 51% | 致命雪崩，session直接死 | 禁止 |

**推荐并发：10-30，不超过30。**

## 已知问题清单（每次检查时对照）

1. **僵尸session**：Devin CLI退出后tmux session不消失，pane空白但tmux_running=True。已修复：observe_attempt_files中加pane_empty检测。
2. **activity_signature永远在变**：tmux_log_path被tmux自己写，导致idle永远=0，stall检测不触发。已修复：signature排除tmux_log_path和session_info_path。
3. **rate_limited误报**：RATE_LIMIT_PATTERNS匹配到"Thinking Round 1429"中的"429"。已修复：用具体模式"http 429"/"status 429"/"error 429"。
4. **failed_no_proof实为connection_error**：CONNECTION_PATTERNS没覆盖cognition.ai/errorKind。已修复：加connection error/unavailable/errorKind模式。
5. **FATE .json格式不支持**：original_index是problem_id编号不是数组索引。已修复：用original_id_in_source匹配json的id字段。
6. **monitor漏判PROOF COMPLETE**：Solver输出了但monitor还没poll到。正常——等下一轮poll会判定。
7. **答案泄漏检查的假阳性**：export/conversation.json中出现ANSWER LEAK DETECTED是指令文本本身，不是真报错。已处理：leak命令区分指令文本vs真报错。
