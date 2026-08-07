# 系统设计原语目录

> AI数学工程系统的设计原语——构造系统的积木。每个原语一个文件，记录定义、来源、验证状态、组合关系、开放问题。
>
> **原语 = 构造系统的积木。** 你能说"用这个"然后知道下一步做什么（操作原语），或者能把它放置到系统架构中（结构原语）。

## 目录结构

本目录分两个子目录：

- **`operational/`** — 操作原语（9个）：你能执行的动作、策略、约束、协议
- **`structural/`** — 结构原语（7个）：你能放置到架构中的组件、角色、接口

概念框架（理解系统的视角）在 `../concepts/`，性质标准与隐喻（判断标准与想象工具）在 `../criteria/`。它们不是原语，但有指导关系——原语文件中"约束于"字段引用它们。

## 原语的三个判据

一个东西是原语，当且仅当同时满足：

1. **可执行性**：对应一个可执行的操作，或一个可放置的结构元素
2. **可验证性**：能在实验中观察"用了它"和"没用它"的区别
3. **构造性**：是积木，不是地图——用来构造系统，不是用来理解系统

不满足这三个判据的，归入 concepts/（概念框架）或 criteria/（性质标准与隐喻）。

## 验证状态四等级

| 状态 | 含义 |
|---|---|
| `tested` | 在实验中被用过且有效 |
| `tested_negative` | 在实验中被用过且无效/非关键 |
| `partial` | 部分验证——效应存在但未证明核心声称 |
| `untested` | 提出但从未测试 |

**纪律**：一个原语只有在实际实验中被用过且有效时才能标 `tested`。提出但未测试的，必须标 `untested`。

## 操作原语索引（operational/，9个）

### 按验证状态分组

#### tested（实验验证有效）
- [continuous-questioning](operational/continuous-questioning.md) — 连续发问：六层渐进框架，guided_001+guided_003验证（但未证明必要性——AI裸跑就能做第一问）
- [safe-first-step](operational/safe-first-step.md) — 安全第一步：让AI先描述形状，guided_001+guided_003 Q1验证（同上局限）
- [non-specificity](operational/non-specificity.md) — 非特定性：guided_003验证纯非特定引导有效（从tested_negative升级）
- [base-change](operational/base-change.md) — 换基：作为数学操作tested（guided_001中AI做了中心化），作为系统原语untested

#### tested_negative（实验验证非关键）
- [implicit-filtering](operational/implicit-filtering.md) — 隐含筛选：218发现guided_001的Q3-Q4发生了隐含筛选，但guided_003证明它不是成功的关键因素

#### partial（部分验证）
- [minimal-knowledge-transfer](operational/minimal-knowledge-transfer.md) — 最小知识传递：guided_001声称0知识传递但有争议

#### untested（提出未测试）
- [dfs-guidance](operational/dfs-guidance.md) — DFS引导：提出但guided_001没用到回溯
- [backtrack-fresh-session](operational/backtrack-fresh-session.md) — 回溯铁律：提出但从未实际回溯过
- [execution-contract](operational/execution-contract.md) — 执行契约：提出但从未实际使用

## 结构原语索引（structural/，7个）

### 按验证状态分组

#### partial（部分验证）
- [cognitive-activation](structural/cognitive-activation.md) — 认知激活 [效应型]：效应存在（引导改变路径）但未证明激活做不出来的能力（AI裸跑就能做第一问）

#### untested（提出未测试）
- [pipe](structural/pipe.md) — Pipe：Pipeline网络节点，241号提出
- [certificate](structural/certificate.md) — 证书：结构定义清晰但证书系统未实现
- [data-pedestal](structural/data-pedestal.md) — 数据基座：结构定义清晰但未实现
- [math-reasoning-engine](structural/math-reasoning-engine.md) — 数学推理引擎：作为功能tested，作为Pipe角色untested
- [pattern-recognition-engine](structural/pattern-recognition-engine.md) — 模式识别引擎：作为功能有争议tested，作为Pipe角色untested
- [constraint-solver-engine](structural/constraint-solver-engine.md) — 多约束求解引擎：作为功能tested，作为Pipe角色untested

## 验证状态分布统计

| 层 | tested | partial | tested_negative | untested | 总计 |
|---|---|---|---|---|---|
| 操作原语 | 4 | 1 | 1 | 3 | 9 |
| 结构原语 | 0 | 1 | 0 | 6 | 7 |
| **合计** | **4** | **2** | **1** | **9** | **16** |

**一眼能看出的结论**：
- 操作原语中56%有实验证据（tested 4 + partial 1 + tested_negative 1）/ 9——实践涌现的原语有实验支撑
- 结构原语中86%是untested——架构设计尚未落地实现
- **关键缺口**：还没有在"AI裸跑做不出来"的题上验证过引导效果——第二问实验是下一步
- 概念框架和性质标准不再需要验证状态（它们在 concepts/ 和 criteria/ 中用"适用边界"替代）

## 文件结构

操作原语遵循 `_template_operational.md`，结构原语遵循 `_template_structural.md`。

## 与其他目录的关系

- **`../concepts/`**：概念框架——理解系统的视角。原语文件中"约束于"字段引用指导它的概念。
- **`../criteria/`**：性质标准与隐喻——判断原语好坏的标准。原语文件中"约束于"字段引用检查它的标准。
- **`../dev-docs/`**：时间序列工作记录。原语文件在"来源"字段引用它出处的dev-docs。
- **认知图（ArangoDB）**：项目认知管理，与原语目录独立但互相引用。
