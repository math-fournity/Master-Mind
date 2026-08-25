---
description: >
  数据库-文件双向可追溯性铁律。任何向数据库写入记录且同时产出物理文件时；
  声称"X完成"或"数据已入库"时；设计或修改任何涉及DB记录+文件产出的系统模块时。
  WHEN to use: always-on——任何涉及DB记录+物理文件的操作。
  WHEN NOT to use: 纯文件操作（无DB记录）；纯DB操作（无物理文件）。
trigger: always_on
---

# 数据库-文件双向可追溯性铁律

**触发条件**：always-on——任何向数据库写入记录且同时产出物理文件时；声称"X完成"或"数据已入库"时；设计或修改任何涉及DB记录+文件产出的系统模块时。

## 核心约束

**数据库记录和物理文件之间必须可双向追溯——从DB记录出发能找到所有相关物理文件，从物理文件能回查DB记录。声称"数据已入库"前，必须做remainder=0验证。**

这不是"要保留痕迹"的要求（那是`six-trace-preservation.md`的职责），而是"保留后要验证可顺藤摸瓜"的要求。前者是保留维度，本规则是验证维度。

## 三条铁律

### 铁律1：DB记录的paths字段必须完整指向所有物理文件

任何写入数据库的记录，如果该记录关联物理文件，则记录中必须包含完整的路径字段，使得从该记录出发能定位到每一个关联文件。

**反模式**：mitm目录下有4个文件（thinking_live.jsonl / thinking_live.txt / thinking_readable.txt / trajectory.jsonl），但DB记录的paths字段只记录了thinking_readable_path。其他3个文件"存在但DB中找不到"。

**正确模式**：paths字段包含所有实际会产出的文件路径。如果某个路径在特定条件下不产出（如failed题无proof.md），该路径字段仍保留但文件不存在是expected missing。

**检查方法**：列出该记录关联的物理目录中的所有文件，逐个确认DB记录中有对应的路径字段。

### 铁律2：不存在的路径不能留在DB中

DB记录中的路径字段必须指向实际存在（或预期会存在）的文件。指向不存在的文件且不属于expected missing的路径，是DB污染——必须修复（补充正确路径或置null）。

**反模式**：paths字段中有`mitm_raw_dir`指向`mitm/raw/`子目录，但该子目录从未被创建。从DB出发查找时遇到"断链"。

**正确模式**：如果某个路径在实践中不产出，从paths字段中删除它或置null。ArangoDB的`update`是merge不会删除字段——需要显式置null。

### 铁律3：声称"X完成"前必须做remainder=0验证

声称"数据已入库"、"文件已落盘"、"记录完整"之前，必须执行可审计性验证：从DB出发，逐个检查所有paths字段指向的文件是否实际存在。只有unexpected missing=0时才能声称完成。

**验证脚本模板**（见skill）：从DB读取所有记录 → 遍历每个记录的paths字段 → 检查文件存在性 → 区分expected missing（如failed题无proof）和unexpected missing → 输出VERDICT: PASS/FAIL。

## 和其他规则的关系

- **`six-trace-preservation.md`**：前者要求"运行时要落盘+产物要能追溯到上下文"（保留维度），本规则要求"保留后要验证DB和文件可双向追溯"（验证维度）。互补不重复。
- **`six-run-id-naming.md`**：数字ID命名是可追溯性的前提——目录名含数字ID才能从文件回查DB。本规则是six-run-id-naming的验证层。
- **`six-dual-check-mechanism.md`**：双重检查机制要求"代码能保证的用代码检查"。本规则的remainder=0验证就是代码可执行的检查。
- **AGENTS.md可审计性纪律**："声称X完成前必须有remainder=0证明"——本规则是这条纪律在DB-文件层面的具体化。

## Skill

`~/.config/devin/skills/db-file-traceability/SKILL.md`——提供remainder=0验证的脚本模板、expected missing的判定规则、修复gap的操作流程。

## 来源

用户原话（2026-08-12）："你要把这个任何时候，数据库和数据都可以被'顺藤摸瓜'做成元组啊，做成AI的工作意识啊。"

触发场景：362号实施报告完成后，用户问"相关的全部trajectory和统计分析信息，都入库了吗？都是可再次通过数据库记录顺藤摸瓜找到的吗？"——验证发现3个gap（mitm子文件路径不全、审稿notes没落盘、mitm_raw_dir指向不存在的目录），修复后206个文件全部可追溯。
