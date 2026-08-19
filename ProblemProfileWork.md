# ProblemProfileWork.md — 题目侧写Profile提取工作

> **来源**：从 AGENTS.md 第368-441行外移（2026-08-19瘦身工程三期，392号方案）。
> **定位**：题目侧写（problem profile）提取工作的进度、方法、产出记录。系统数据基座的核心建设线。
> **加载时机**：当你要做题目侧写Profile提取工作（subagent提取profile/审计profile质量/管理Tier 2优先级）时，必须用read工具全文加载本文件。不涉及题目侧写工作时不需要读。
> **AGENTS.md索引**：AGENTS.md "外部文档索引"节有指向本文件的索引行。

---

## 题目侧写Profile提取工作（活文档 · 数据基座建设）

> **本节记录题目侧写（problem profile）提取工作的进度、方法和产出。这是系统数据基座的核心建设线。**
> **详细审计日志**：`subagents-dirs/review-log.md`（每批审计结果）
> **任务追踪文档**：`任务追踪/05-题目侧写Profiling系统.md`

### 工作方法

每道题通过subagent完成11步分析：读题目解答→QA序列分析→问题拓扑层→解答思维模式层→翻译方向层→tell拓扑层→提取(tell,hint)对→实验适用性层→输出profile JSON→入库ArangoDB→汇报。

Master Agent对每批3题做完整6-Phase审计：格式检查（situation_type/hint_level/per-pair拓扑/必填字段/QA序列结构）+数学内容审查（题目理解/解答理解/key_insight准确性/瓶颈标注合理性）+落盘audit-checklist.md。

### 数据库存储

- **ArangoDB集合**：`problem_profiles`（_key=problem_id，含完整profile JSON）
- **ArangoDB集合**：`problem_extraction_progress`（_key=数字ID，含global_sequence/extraction_status/metadata）
- **数据库**：`xishujuzhen_math_glm52`，localhost:8529

### 完成进度（截至2025-01-24）

| 层级 | 来源 | 完成数/总数 | 状态 |
|---|---|---|---|
| **Tier 1** | 高难度竞赛题（IMO/IMO SL/Putnam/China TST/FATE-X等） | **452/452** | ✅全部完成 |
| **Tier 2** | IMO Shortlist剩余+IMO剩余+Putnam剩余+IMO Longlists+China TST剩余+Balkan MO SL+China NOL+ToT+IMC+Yau+Alibaba | 3/606 | 进行中 |
| **Tier 3** | USAMO+FATE-H+HMMT系列+SMT+CMIMC+Iranian+Brazilian | 0/3127 | 待处理 |
| **Tier 4** | OlympiadBench+FATE-M+AIME 2024 | 0/860 | 待处理 |
| **Tier 5** | pascal+fermat+cayley+mathd | 0/942 | 待处理 |
| **Tier 6+** | olympiads+Hendrycks MATH+AoPS 2024等 | 0/62000+ | 暂不规划 |

**当前总进度**：455/67838（0.67%），但Tier 1高难度题已100%完成。

### Token统计

| 指标 | 数值 |
|---|---|
| profile总数 | 455 |
| 局部tell数量 | 3,192 |
| 全局tell数量 | 972 |
| tell总数 | 4,164 |
| tell字段总token | ~122K |
| 完整profile总token（含所有文本字段） | ~407K |
| 平均每profile token | ~893 |

### 质量记录

- **连续0个小问题批次**：129批（从第41批至今）
- **subagent静默失败处理**：少数题目subagent返回空结果，Master Agent手动创建profile（如omni_math_004296）
- **原解答问题处理**：部分题目原Lean解答有计算错误/不严谨/模糊/hand-wavy/事实错误，subagent在profile中重构或注明
- **空答案字段处理**：部分题目answer为空，subagent从解答中推导答案

### Tier 2后续优先级（难的先处理）

1. IMO Shortlist剩余96题（起始seq=1955）← 当前进行中
2. IMO剩余89题（起始seq=1403）
3. Putnam剩余88题（起始seq=1756）
4. IMO Longlists剩余39题（起始seq=1994）
5. China TST剩余80题（起始seq=1443）
6. Balkan MO SL剩余31题（起始seq=1862）
7. China NOL剩余35题（起始seq=1446）
8. ToT剩余54题（起始seq=1956）
9. IMC剩余67题（起始seq=1627）
10. Yau Contest剩余6题（起始seq=1630）
11. Alibaba Contest剩余21题（起始seq=1597）

### 关键文件

- `subagents-dirs/review-log.md`：完整审计日志（每批的seq范围/题目/审计结果/修复内容/数学审查结论）
- `subagents-dirs/<problem_id>/`：每题的工作目录（problem.lean/checklist.md/profile.json/audit-checklist.md）
- `subagents-dirs/audit-checklist-template.md`：审计checklist模板
- `subagents-dirs/checklist-template.md`：subagent工作checklist模板
- `scripts/prepare_subagent_dir.py`：subagent工作目录准备脚本
- `scripts/ingest_problem_extraction_progress.py`：progress记录入库脚本

---
