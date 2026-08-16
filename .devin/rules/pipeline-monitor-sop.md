# Rule: pipeline-monitor-sop

## 触发条件
运行任何Pipe（Pipe 1分析/Pipe 2审计/Pipe 3选题）时，必须启动Monitor Pipe并行监控。

## 核心约束
1. **禁止启动Pipe后干等**——Pipe运行时，Monitor Pipe必须并行运行，自动检查健康状态
2. **Monitor Pipe发现问题→alert→AI recheck→修复**——自动检查发现数量类问题，AI recheck语义类问题
3. **每轮检查必须包含产出内容验证**——不只看数量（completed=N），要看内容（审计判定是否正确）
4. **发现提示词设计缺陷时立即停Pipe、修正模板、重新生成AGENTS.md、重新运行**

## Monitor Pipe的7个自动检查
1. session_health: tmux session数 vs 并发数
2. queue_progress: Redis队列pending是否在减少
3. output_existence: completed的run是否有输出文件
4. parse_success_rate: XML解析成功率
5. status_consistency: audit_status vs check_results一致性
6. d_check_misapplication: D检查对错误d1类型执行
7. failure_rate: 失败率过高

## AI recheck的3个语义检查
1. C2/C3语义判断是否正确（d1_exp是否真的匹配d1标签）
2. 审计AI是否有明显误判
3. 审计标准本身是否合理（如D1的动词列表是否完整）

## 工作流
1. 启动Pipe（launcher在tmux中运行）
2. 启动Monitor Pipe（在tmux中运行，interval=300s）
3. Monitor Pipe每5分钟自动检查，发现问题→写alert到monitor_alerts集合
4. **AI定期用标准化脚本检查**（`./scripts/monitor_check.sh <batch_id>`）——禁止inline编写检查命令
5. AI recheck flagged items，修复问题，标记alert为fixed
6. Pipe完成后，Monitor Pipe自动退出

## 标准化检查脚本

**脚本路径**：`analysis-devin-failure-system/scripts/monitor_check.sh`

**用法**：`./scripts/monitor_check.sh <batch_id> [monitor_tmux_session]`

**输出4项检查**：
1. **Monitor Pipe pane输出**——最近5轮的轮次、ALERT、AI_REVIEW抽样结果、状态报告
2. **alerts集合**——新alert（通过`--check-alerts`）
3. **进程状态**——launcher和monitor_pipe进程是否在运行、CPU/ELAPSED/STAT、tmux au-sessions数量
4. **进度**——DB状态分布、总完成数、失败数、失败率（>10%自动WARNING）

**为什么标准化**：避免每次监控时inline编写检查命令——inline编写容易遗漏检查项（如只看alerts不看pane输出、只看进度不看进程状态），标准化后每次检查都包含全部4项。

## 反模式
- 启动Pipe后只看数量不看内容（completed=N就认为正常）
- Monitor Pipe发现alert后不处理（alert堆积不解决）
- 修正提示词后不重新生成AGENTS.md（旧AGENTS.md还在用旧模板）
