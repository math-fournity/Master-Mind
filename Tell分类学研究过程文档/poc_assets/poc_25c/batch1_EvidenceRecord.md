# POC-2.5c Batch-1 EvidenceRecord（2026-08-22）

**实验**：候选Ⅰ（实例检验纪律）Mid-Hint单臂试点，12题×T/C双臂=24 devin cli调用（glm-5-2, dangerous, 禁工具思考模式，同日并发4交错启动）
**机械收取**：batch1_mechanical_results.json（判定v2：agent消息含PROOF COMPLETE≥500B；截断指纹comp=25000校准自历史样本）
**标注**：A轮=annotation_A.yaml（主控）；B轮待独立复核者

---

## §1 主指标（判据口径修正案版）

| 臂 | COMPLETED | TRUNCATED | 其他 |
|---|---|---|---|
| T（Hint注入） | **4/12** | 8/12 | 0 |
| C（bare对照） | **4/12** | 8/12 | 0 |

配对计分：**T_WIN=3（1678/1747/2077），C_WIN=3（6253/6809/19730），双成=1（12700），双败=5**

**工程门槛判定：未达成。** T≥8/12✗（实4）；C=0/12✗（实4）。且配对计分完全对称——本样本内Hint无可检出的净效应。

## §2 方向使用度（A轮，待B轮仲裁）

- 全体T组8/12显示实例检验行为；T组COMPLETED题中3/4
- 直接证据：6253__T thinking显式引用提示原文（"verify with the strategy hint"）
- 关键观察：使用行为与结局解耦——高使用run仍截断（19730/17608），低使用run可完成（12700）
- 揭示：Hint改变了过程形态（行为证据充分）但没有改变结局分布（净效应零）

## §3 成本指标（数据受限）

| 配对 | T tokens | C tokens |
|---|---|---|
| 12700（双成） | 14658 | 13197 |
| 完成run合计 | 61575（均值15394） | 41793（均值13931，其中19730仅1650） |

历史成本对照不可靠：rounds_log中R1/R2 token字段大量缺失（stall/dead_session路径），§3成本指标无法按原定义计算。今日观察：完成的C臂平均成本不高于T臂，"Hint省token"假设在本批无支撑。

## §4 池污染警报（§3条款触发）

**C组解出率4/12≈33%**，远超设计预期的≈0%。设计原文："若C组意外解出率高说明选题池被环境演进污染"。三个C完成经数学实质核验全部正确（9/No/2均与参考答案一致）。

根因分析（两条非互斥）：
1. **模型演进**：续传池的bare失败记录产生于更早的glm-5.2 serving；今日devin cli报"You are powered by GLM-5.2 High"，能力可能上调。
2. **投递差异**：历史round1经AGENTS.md规则通道投递（混入项目级规则上下文）；本次为干净user消息直投，可能更利于聚焦。

## §5 结论三选一（design §6口径）

判定：**介于"仅缩短效应"与"无效应"之间，且选题池前提失效**——
- 弱因果贡献成立？✗（门槛未达）
- 仅缩短效应？弱信号（无系统证据）
- 无效应？本样本点估计为零，但n=12且使用度数据显示过程确被改变

**批次定性：按§3污染条款，本批对"原始弱因果问题"（能否0轮救活截断题）不具备结论资格；作为"Hint行为效应"的首批观察数据有效。**

## §6 资产索引

| 资产 | 位置 |
|---|---|
| 运行现场（24 run导出+meta） | /data/math-agent-glm5.2-tmux-agents-dir/poc25c-batch1/ |
| 机械判定 | batch1_mechanical_results.json + run_scripts/collect_poc25c.py |
| A轮标注+证据抽取 | annotation_A.yaml + annotation_A_evidence.md |
| prompt副本+锚点 | batch1_prompts/（repo审计副本） |
| 驱动日志 | run_scripts/poc25c_driver.log |
