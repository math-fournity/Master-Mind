# 系统设计原语目录

> AI数学工程系统的设计原语积累。每个原语一个文件，记录定义、来源、验证状态、使用经验、关系、开放问题。

## 为什么有这个目录

项目在20多份dev-docs的迭代中产生了大量设计原语。有些是实践中涌现的（连续发问、安全第一步、DFS引导），有些是从人类知识中选取的（范畴、偏序、形式化边界）。它们散落在各文档中，没有统一目录。

本目录把所有原语集中管理，每个带着验证状态，让设计决策基于证据而非记忆。

## 原语的三个来源面相

- **面相A · 实践涌现**：从实验和迭代中涌现的原语，带着实验证据
- **面相B · 知识选取**：从人类知识海洋中选取的原语，有数学/哲学正当性但操作化状态各不相同
- **面相3 · Pipeline网络**：把AI角色细化为Pipe（数学推理引擎/模式识别引擎/多约束求解引擎），产生的新原语

## 验证状态四等级

| 状态 | 含义 |
|---|---|
| `tested` | 在实验中被用过且有效 |
| `tested_negative` | 在实验中被用过且无效 |
| `untested` | 提出但从未测试 |
| `borrowed_unoperationalized` | 从人类知识借用但未操作化 |

**纪律**：一个原语只有在实际实验中被用过且有效时才能标 `tested`。从人类知识借用但未操作化的，必须标 `borrowed_unoperationalized`。提出但未测试的，必须标 `untested`。

## 原语索引

### 按验证状态分组

#### tested（实验验证有效）
- [continuous-questioning](continuous-questioning.md) — 连续发问：六层渐进框架，guided_001验证
- [cognitive-activation](cognitive-activation.md) — 认知激活：提问激活AI能力，guided_001数据表明（效应tested/机制untested）
- [safe-first-step](safe-first-step.md) — 安全第一步：让AI先描述形状，guided_001 Q1验证
- [base-change](base-change.md) — 换基：作为数学操作tested（guided_001中AI做了中心化），作为系统原语untested

#### tested_negative（实验验证无效）
- [non-specificity](non-specificity.md) — 非特定性：guided_001的Q3-Q4被218判定为发生了特定化（部分negative）
- [implicit-filtering](implicit-filtering.md) — 隐含筛选：218发现guided_001的Q3-Q4发生了隐含筛选

#### untested（提出未测试）
- [pipe](pipe.md) — Pipe：Pipeline网络节点，241号提出
- [dfs-guidance](dfs-guidance.md) — DFS引导：提出但guided_001没用到回溯
- [level-spectrum](level-spectrum.md) — Level连续谱：理论提出但Level值从未被实际计算
- [minimal-knowledge-transfer](minimal-knowledge-transfer.md) — 最小知识传递：guided_001声称0知识传递但有争议
- [backtrack-fresh-session](backtrack-fresh-session.md) — 回溯铁律：提出但从未实际回溯过
- [execution-contract](execution-contract.md) — 执行契约：提出但从未实际使用
- [life-death-condition](life-death-condition.md) — 生死条件：提出但从未检查过
- [math-reasoning-engine](math-reasoning-engine.md) — 数学推理引擎：作为功能tested，作为Pipe角色untested
- [pattern-recognition-engine](pattern-recognition-engine.md) — 模式识别引擎：作为功能有争议tested，作为Pipe角色untested
- [constraint-solver-engine](constraint-solver-engine.md) — 多约束求解引擎：作为功能tested，作为Pipe角色untested

#### borrowed_unoperationalized（借用未操作化）
- [formalization-boundary](formalization-boundary.md) — 形式化边界：来自数学哲学，在系统中未操作化
- [boundary-advancement](boundary-advancement.md) — 边界推进：概念清晰但未操作化
- [two-computations](two-computations.md) — 两种计算：分工清晰但未实现双计算架构
- [semantic-field](semantic-field.md) — 语义场：隐喻状态，未形式化
- [certificate](certificate.md) — 证书：结构定义清晰但证书系统未实现
- [data-pedestal](data-pedestal.md) — 数据基座：结构定义清晰但未实现
- [dual-knowledge-production](dual-knowledge-production.md) — 双重知识生产：概念清晰但两条路径都未建造
- [loop](loop.md) — 闭环：动力学定义清晰但未实现
- [situation](situation.md) — 处境：概念清晰但未结构化为系统状态
- [naturality](naturality.md) — 自然性：来自范畴论，形式化尝试未验证

### 按来源面相分组

#### 面相A · 实践涌现（238时期，8个）
- [continuous-questioning](continuous-questioning.md) — 连续发问
- [cognitive-activation](cognitive-activation.md) — 认知激活
- [non-specificity](non-specificity.md) — 非特定性
- [safe-first-step](safe-first-step.md) — 安全第一步
- [dfs-guidance](dfs-guidance.md) — DFS引导
- [level-spectrum](level-spectrum.md) — Level连续谱
- [minimal-knowledge-transfer](minimal-knowledge-transfer.md) — 最小知识传递
- [implicit-filtering](implicit-filtering.md) — 隐含筛选（危机原语）
- [backtrack-fresh-session](backtrack-fresh-session.md) — 回溯铁律

#### 面相B · 知识选取（239时期，12个）
- [formalization-boundary](formalization-boundary.md) — 形式化边界
- [boundary-advancement](boundary-advancement.md) — 边界推进
- [two-computations](two-computations.md) — 两种计算
- [semantic-field](semantic-field.md) — 语义场
- [certificate](certificate.md) — 证书
- [data-pedestal](data-pedestal.md) — 数据基座
- [dual-knowledge-production](dual-knowledge-production.md) — 双重知识生产
- [execution-contract](execution-contract.md) — 执行契约
- [loop](loop.md) — 闭环
- [situation](situation.md) — 处境
- [base-change](base-change.md) — 换基
- [naturality](naturality.md) — 自然性
- [life-death-condition](life-death-condition.md) — 生死条件

#### 面相3 · Pipeline网络（241号新增，4个）
- [pipe](pipe.md) — Pipe
- [math-reasoning-engine](math-reasoning-engine.md) — 数学推理引擎
- [pattern-recognition-engine](pattern-recognition-engine.md) — 模式识别引擎
- [constraint-solver-engine](constraint-solver-engine.md) — 多约束求解引擎

## 验证状态分布统计

| 状态 | 数量 | 占比 |
|---|---|---|
| tested | 4 | 15% |
| tested_negative | 2 | 8% |
| untested | 10 | 38% |
| borrowed_unoperationalized | 10 | 38% |

**一眼能看出的结论**：
- 238时期的原语（面相A）偏tested——实践涌现的原语有实验证据
- 239时期的原语（面相B）偏borrowed_unoperationalized——知识选取的原语有概念但未操作化
- 面相3的原语偏untested——新提出的设计尚未测试
- **76%的原语未经实验验证**（untested + borrowed_unoperationalized）——这是当前原语目录的状态

## 文件结构

每个原语文件遵循 `[_template.md](_template.md)` 的结构：
- 定义
- 来源（面相 + 出处）
- 验证状态
- 使用经验
- 关系（替代/组合/细化/tension）
- 开放问题

## 与其他系统的关系

- **dev-docs**：dev-docs是原语的来源之一，原语文件在"来源"字段引用它出处的dev-docs
- **认知图（ArangoDB）**：认知图是项目认知管理，原语目录是系统设计参考，两者独立但互相引用
- **239号技术说明书**：239是地图（概念关系和整体架构），原语目录是每个地点的详细卡片（独立深度+验证状态）
