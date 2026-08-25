---
description: >
  研发资产管理规则。339号方案落实——从文件版本追踪的痛苦中提炼的研发资产管理规范。
  管理run_manifest.json、提示词版本、AGENTS模板、代码版本等研发资产。
  WHEN to use: 管理研发资产（run_manifest、提示词版本、AGENTS模板、代码版本）时。
  WHEN NOT to use: 不涉及研发资产管理的一般编码。
trigger: model_decision
---

# 研发资产管理规则

> 339号方案落实——从文件版本追踪的痛苦中提炼的研发资产管理规范

## 运行资产

### run_manifest.json

每次运行必须生成`run_manifest.json`，记录本次运行使用的所有资产版本：

- 提示词文件（v5_grading.md / v7_grading.md / v8_grading.md / v10_grading.md / synthesis.md）
- AGENTS模板（AGENTS_V5.md / AGENTS_V7.md / AGENTS_V8.md / AGENTS_V10.md / AGENTS_synthesis.md）
- step要求文件（v8_step1/2_requirements.md / synthesis_step1-4_requirements.md）
- 代码版本（vein_analysis.py / verify_lattice_completeness.py的md5）
- git commit hash + git branch

**实现**：`vein_analysis.py`的`_write_run_manifest()`函数在`vein_analysis_three_phase()`开始时自动调用。

**回头审计时**：直接读run_manifest.json，不需要md5对比git历史。`git show <commit>:<文件路径>`可以查看当时的文件内容。

### 自动归档

运行结束后自动归档到`system/tests/vein_analysis/runs/{run_id:04d}/`：

- 各V的segments.json/formal_context.json/key_entities.json
- 各V的closed_elements.json
- 综合分析的output.json/output.md/comparison.json/closed_element_traces.json/content_based_traces.json
- run_manifest.json

**实现**：`vein_analysis.py`的`_archive_run()`函数在`vein_analysis_three_phase()`结束时自动调用。

**归档目录是权威的**——palyground的工作目录是运行时的工作区，归档目录是审计时的权威来源。

## 目录命名

### 规范

- **正式运行**：`{run_id:04d}_{problem_id}`——如`0011_imo2009p6`
- **单独测试**：`{run_id:04d}_{problem_id}_{test_type}`——test_type只能是`synthtest`/`v8test`等预定义值
- **不允许无run_id的目录**——早期`imo2009p6`是历史遗留，不再新增

### 历史遗留

以下目录是历史遗留，不清理、不重命名，但不再新增同类：

- `imo2009p6`（无run_id，早期三阶段架构调试）
- `0008_imo2009p6_v8test`（有后缀，V8方案D测试）

## 数据库记录

### problem_entries集合

每次运行必须写`problem_entries`集合，包含字段：

- `run_id`——入题序号（必填）
- `problem_id`——题目ID（必填）
- `status`——completed/interrupted/failed/running（必填）
- `manifest_path`——run_manifest.json路径（339号新增）
- `archive_path`——归档目录路径（339号新增）
- `git_commit`——运行时的git commit hash（339号新增）
- `phases`——各阶段状态（339号新增）

### 中断的运行

中断的运行必须标记为`interrupted`（不是`running`）。

**实现**：TODO——目前中断的运行仍然是`running`状态，需要加清理逻辑。优先级低，不影响新运行。

### 单独测试

单独测试（如0010的综合分析4阶段拆分测试）也要写数据库，`run_id`字段标注为test。

**实现**：TODO——目前单独测试不走`vein_analysis_three_phase()`，不写数据库。优先级低，因为单独测试的资产已经在run_manifest.json中记录。

## 审计流程

### 改进后（339号方案落实后）

1. 从数据库查run_id → 直接得到`manifest_path`和`archive_path`
2. 读run_manifest.json → 直接得到所有文件版本、md5、git commit
3. `git show <commit>:<文件路径>` → 查看当时的文件内容

**从5步缩减到3步，且每步都是确定性的（不需要推断）。**

### 改进前（338号的痛苦流程，仅作参考）

1. 从文件系统找运行目录
2. 从数据库找run_id
3. 用md5对比工作目录中的prompt.md和git历史中各commit版本
4. 从git log时间线推断vein_analysis.py版本
5. 手动整理成表格
