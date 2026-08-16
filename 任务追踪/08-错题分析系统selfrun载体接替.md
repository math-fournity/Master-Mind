# 任务追踪 08 · 错题分析系统 selfrun 载体接替

> **创建**：2026-08-16
> **工作线**：analysis-devin-failure-system（错题分析系统）——devin cli载体失效后，由ZCode主会话+subagent接替分析/审计AI角色
> **主操作手册**：`analysis-devin-failure-system/docs/selfrun-workflow.md`
> **本文档职责**：跨Session交接——接手者读完本文档+操作手册即可不问任何人继续工作

---

## §0 当前焦点

**进度游标（2026-08-16 11:00实测）**：

| 指标 | 数值 |
|---|---|
| 分析范围 | 3180 道失败题（batch `full-analysis-30c`，v2批次完全包含于其中） |
| 已完成分析（results_collected） | **1579** |
| 剩余待分析 | **1601** = polymath 1433（干净，随时可跑）+ deepmath_103k 162 + oda_math 6（后两者共168题被数据缺陷污染，先修数据） |
| 其中selfrun载体产出 | 64题（Step1: 3 + Step2: 49 + wave001: 12） |
| analysis_results 集合 | 2046 docs |
| 审计 Pipe（audit-full1） | completed 1333 / prepared 40 / **failed_stall 145（僵尸服务烧出来的，全部可被selfrun回收）** / rate_limited 2 / running 1 |
| 审计（audit-selfrun1/2） | 8/8 完成 |

**立即下一步**（按序）：
1. 放量polymath：`python -m src.selfrun_driver plan --count 24 --source polymath` → 每波派3个subagent（并发上限3）→ `sweep --ingest`
2. 每约100题：`recheck --count 5` 双盲复测，d1一致率<80%停下修规则
3. 修复 data_collector 的 deepmath/oda 题文查找（见§3.1），重建168题AGENTS.md后照常分析
4. 处置audit僵尸服务（见§3.5）并用selfrun收尾审计剩余任务

**⚠️ 后台正在发生**：devin时代的 `audit-launcher` tmux服务仍在僵尸运转（devin cli已死，session每~30秒换新、全部立即失败），把audit-full1的prepared队列烧成failed_stall。不损坏数据（输入文件都在，failed_stall可回收），但应停止：`python -m monitoring.analysis_control stop --kill-sessions`（或直接 `tmux kill-session -t audit-launcher`）。

---

## §1 已完成

| 时间 | 事项 | 产出 |
|---|---|---|
| 08-16晨 | 系统调研+方案：确认devin cli只是载体，流水线代码全部健在 | 接替方案（intake写入端+零改动复用下游） |
| 08-16 | `src/selfrun_intake.py`：validate/write_export/mark_completed/collect-delta | commit 951e34b |
| 08-16 | Step1：3题全链路验证（分析→落盘→收集→汇总→独立审计3/3过） | commit 951e34b |
| 08-16 | Step2：49题分层抽样+5题抽样审计全PASS；发现题文/thinking错位污染 | commit 8259717 |
| 08-16 | 污染根因实锤：对比solver工作目录AGENTS.md与分析AGENTS.md——solver数据完好，错在data_collector的题文查找（deepmath/oda） | 见§3.1 |
| 08-16 | 流程固化：`selfrun_driver.py`（plan/status/sweep/recheck）+ subagent规范v3；wave001十二题格式通过率100%；双盲一致率80%，两处分歧经三方盲读仲裁修正 | commit c7b4ad0 |
| 08-16 | 交接三件套落盘（本档+workflow恢复节+AGENTS.md指针） | 本次commit |

---

## §2 待办

- [ ] **放量polymath 1433题**：按§0命令节奏跑；每~100题recheck复测
- [ ] **修data_collector的deepmath/oda题文查找**（§3.1），重建168题AGENTS.md，排入分析
- [ ] **停止audit僵尸服务**（§3.5），用selfrun收尾audit-full1剩余（prepared+failed_stall≈185+）
- [ ] **834条devin旧结果污染处置**：已入库的deepmath/oda结果（devin判定60% DIRECTION_ERROR）含同类错位污染——等数据修复后由用户决定是否重分析
- [ ] 全量完成后：终局分布对比（selfrun vs devin基线）+ 汇总报告 + 最终审计批次
- [ ] 可选：audit Redis队列清理（DB状态为准，Redis在本工作流中不再使用）

---

## §3 关键决策与发现

### 3.1 题文/thinking错位污染（最重要的数据发现）

- **现象**：AGENTS.md中Problem/Standard Solution与AI thinking是两道完全不同的题。Step2抽样中24个DIRECTION_ERROR里至少14个（口径18-21个）源于此，集中在 deepmath_103k 和 oda_math_460k；polymath抽样27题零错位。
- **实锤证据链**（以deepmath_103k_00004613为例）：solver工作目录 `/data/math-agent-glm5.2-tmux-agents-dir/p71316e04bfb84df4856f/AGENTS.md` 里solver拿到的题是数论题（n^(π(2n)−π(n)) ≤ c^n），其thinking正确对应；而分析AGENTS.md里配的题是积分题（∫sinx/x^a收敛性）——**solver侧数据完好，错在data_collector从题库文件取题文/标准解答的查找环节**（load_deepmath按运行计数器idx建索引，疑似文件集/排序变化导致错位；oda同理）。
- **处置**：这是数据bug不是方法论问题——修数据，不改模板。错位题按模板规则仍判DIRECTION_ERROR（thinking与题目无交集），但科学上无意义，故修复前不跑deepmath/oda。
- devin已产出的834条deepmath/oda结果含同样污染，其60% DIRECTION_ERROR基线被抬高。

### 3.2 为什么现有流水线零改动

`conversation.json`按devin export格式写入（`steps[].source=="agent"`）→ result_collector/audit_result_collector原样读取。DB事件带`carrier="zcode-selfrun"`标记，devin产出与selfrun产出可区分可追溯。

### 3.3 insert_result是纯insert——禁止全量重跑collect

`analysis_results`的insert无upsert语义，全量重跑`collect_batch`会把已有结果翻倍。必须用`selfrun_intake collect-delta`（只处理completed未collected的run并追加快照）。

### 3.4 subagent运行参数（实测）

- **并发上限3**——每波恰好派3个agent，第4个会被"user concurrency limit exceeded"拒绝
- 每个agent连做2题：耗时4.7-7.8分钟，token 0.8-2.0M
- 判定规则版本v3（`templates/selfrun_subagent_task.md`）：TL/PP精化判据="截断那一刻答案得出来了吗？已得出（在验证它）→TL；未得出（还在找它）→PP"；d2口径="只按标准解答文本实际使用的关键步骤归类"
- QA阈值：双盲d1一致率≥80%继续放量，<80%停下修规则；分歧题走三方盲读仲裁（原始/重读/仲裁三份产物全留痕）

### 3.5 audit僵尸服务（接手时可能仍在跑）

`audit-launcher`/`audit-monitor` tmux session是devin时代服务，devin死后仍在dequeue→起session→立即失败→标failed_stall循环。停止命令见§0。failed_stall/prepared的审计任务全部可由selfrun路径回收：读audit_runs工作目录AGENTS.md→subagent产XML→`selfrun_intake ingest-audit`→`audit_result_collector --batch-id audit-full1`。

### 3.6 分工与权限边界

subagent只读任务文件指定的AGENTS.md、只写指定的输出文件（无DB权限）；主会话独占校验、落盘、写库、审计派发。审计用全新独立subagent（与分析者不同会话）。

---

## §4 Git Commit历史（selfrun线）

| commit | 内容 |
|---|---|
| `951e34b` | selfrun intake组件+工作流文档；Step1三题全链路验证通过 |
| `8259717` | Step2四十九题分层抽样全链路+五题审计全PASS；发现deepmath/oda题文-thinking错位污染 |
| `c7b4ad0` | 流程固化：任务文件化调度器+subagent规范v3（TL/PP精化判据）；wave001格式100%；双盲一致率80%+仲裁修正 |
| （本次） | 交接三件套：任务追踪08 + workflow恢复节 + AGENTS.md指针 |

devin时代相关commit（背景）：`e61810f` monitor_check标准化 / `ab384f2` rate limit根因+自动暂停 / `6c0eb09` 提示词缺陷修正 / `8e242d6` D1动词扩展后处理 / `ace64f3`+`a3d4a5e` 审计Pipe实现 / `6d25ece` d2_exp标签泄漏修复 / `d8ac318` 轮4提示词修正。

---

## §5 跨Session读取指南

**加载顺序**（新会话接手时）：
1. AGENTS.md（本repo硬约束+当前任务指针）
2. 本文档（进度游标+坑清单）
3. `analysis-devin-failure-system/docs/selfrun-workflow.md`（机制+验证记录+恢复命令）
4. 按需：`src/selfrun_driver.py` / `src/selfrun_intake.py` 源码（docstring自包含）、`templates/selfrun_subagent_task.md` v3（判定规则权威版本）

**恢复运行的精确命令**（工作目录：`analysis-devin-failure-system/`，python用repo根`.venv`）：

```bash
# 1. 看当前状态（产出缺失/待入库分布/剩余数）
python -m src.selfrun_driver status
# 2. 生成下一波任务文件（如24题polymath）
python -m src.selfrun_driver plan --count 24 --source polymath
# 3. 对每份 output/selfrun/waveNNN_agentK.md 派一个subagent，prompt只需：
#    『用Read读取<任务文件绝对路径>并严格执行其中的全部指令，完成后按其文末汇报格式汇报。』
#    每波最多3个并发
# 4. 收口：校验+入库+增量收集
python -m src.selfrun_driver sweep --ingest
# 5. 每~100题双盲复测
python -m src.selfrun_driver recheck --count 5
#    （重读产出=selfrun_check.xml，对比脚本见workflow文档）
# 6. 汇总
python -m src.aggregator --batch-id full-analysis-30c
```

**DB查询速查**：`ARANGO_DB=xishujuzhen_math_glm52`（连接经`src.db_schema.connect_db`）。按problem_id查分析结果：`FOR r IN analysis_results FILTER r.problem_id == @p RETURN r`；查selfrun产出：`FILTER r.carrier != null`（analysis_runs）；审计结果：audit_results集合按batch_id。

**产物位置**：subagent产出=各题工作目录`selfrun_output.xml`（D盘`/data/math-agent-glm5.2-tmux-agents-dir/analysis-devin-failure/<exp_id>/`）；入库export=`.../tmux-agents-trajectory/analysis-devin-failure/<exp_id>/exports/conversation.json`+`selfrun_meta.json`；波次任务文件=`output/selfrun/`。
