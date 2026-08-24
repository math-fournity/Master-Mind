# 03-Pipe-1-选择Telling-AI实例

**前置阅读**：02-trace端/02-Pipe-0-粗domain分类.md
**关联文件**：02-trace端/04-Pipe-2-并发Telling-AI.md、07-工程规格/03-Pipe-1接口定义.md
**来源**：311号§3.3、337号（分类学是排除机制）、338号（高Level概念的存储和使用方式）、第五代说明书02-04

---

## §1 Pipe 1在第六代中的角色

从"缩小tell范围"变为"选择启动哪些区的Telling AI实例"。

---

## §2 第五代Pipe 1的问题

用拓扑匹配从10万级tell缩小到数百候选，是硬约束因为单AI上下文放不下。

---

## §3 Pipe 1新角色的定义

用domain分类结果确定启动哪些区的Telling AI。

---

## §4 Pipe 1新接口

输入domain分类结果（如"数论+代数"），输出Telling AI实例列表（如["Telling_AI_数论", "Telling_AI_代数"]）。

---

## §5 Pipe 1作为排除机制

### §5.1 选择即排除

Pipe 1选择Telling AI实例的本质是排除——从所有Telling AI实例中排除不相关的，保留相关的（337号）。

排除的依据是domain分类结果——如果domain分类为"数论+代数"，则排除"几何""组合"的Telling AI，保留"数论""代数"的Telling AI。

### §5.2 跨域Telling AI的排除规则

"跨域"Telling AI（承载高Level概念如"同构之桥"的Telling AI）的排除规则特殊——它不完全依赖domain分类，还依赖trace是否显示跨域需求。

- 如果domain分类结果中包含"跨域" → 跨域Telling AI被保留
- 如果domain分类结果中不包含"跨域"，但trace显示AI在某个domain内打转未突破 → 跨域Telling AI仍然被保留（因为可能需要跨域提示）
- 如果domain分类结果中不包含"跨域"，且trace没有显示跨域需求 → 跨域Telling AI被排除

### §5.3 高Level Telling AI的启动

高Level概念（如"同构之桥"）有专门的Telling AI实例——从高Level AGENTS.md目录启动的devin cli（338号）。高Level Telling AI和低Level Telling AI一样，由Pipe 1选择是否启动。

---

## §6 为什么这个角色变化可行

并发Telling AI方案中，不需要缩小tell范围到单AI上下文，只需要选择启动哪些区的Telling AI。

---

## §7 和第五代Pipe 1的对比

从"缩小tell范围"到"选择Telling AI实例"，从"硬约束"到"轻量选择"。

---

## §8 待后续完善的内容

1. domain索引的具体实现——ArangoDB中的分区配置
2. 跨域Telling AI的排除规则的形式化——如何判断"trace显示AI在某个domain内打转未突破"
3. 多个高Level Telling AI的选择——如果系统有多个高Level概念（同构之桥、构造-分析-排除等），Pipe 1如何选择启动哪些高Level Telling AI
