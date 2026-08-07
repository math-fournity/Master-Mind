# 概念框架目录

> 理解AI数学工程系统的视角。不是构造系统的积木（那是 `../primitives/`），是透过它看系统的镜头。

## 为什么有这个目录

项目在20多份dev-docs的迭代中产生了大量概念——形式化边界、两种计算、闭环、处境等。它们不是操作（你不能"执行形式化边界"），也不是结构（你不能"放置一个闭环"），但它们指导了原语的设计。

这个目录把概念框架集中管理。每个概念记录它指导了什么原语、它的适用边界、它在文档中的演化过程。

## 概念框架 vs 原语

| | 原语（primitives/） | 概念框架（concepts/） |
|---|---|---|
| 是什么 | 构造系统的积木 | 理解系统的视角 |
| 能不能执行/放置 | 能 | 不能 |
| 能不能验证 | 能 | 不能——用"适用边界"替代 |
| 关系字段 | 组合关系（操作/结构层面） | 演化（概念深化过程） |
| 更新频率 | 随实验更新 | 随理念突破更新 |

## 概念索引（7个）

| 概念 | 一句话 | 指导了什么 |
|---|---|---|
| [formalization-boundary](formalization-boundary.md) | 数学知识有可形式化/不可形式化的本质分界 | two-computations分工、certificate结构、data-pedestal设计 |
| [two-computations](two-computations.md) | 经典计算处理边界以内，AI计算处理边界以外 | constraint-solver-engine角色、cognitive-activation问题域 |
| [dual-knowledge-production](dual-knowledge-production.md) | 语料→训练路径+抽取路径 | data-pedestal设计 |
| [boundary-advancement](boundary-advancement.md) | 闭环=边界推进过程 | loop动力学描述、certificate增长语义 |
| [loop](loop.md) | 闭环动力学：AI感知→压缩→经典计算验证→回流 | execution-contract协议、certificate产生时机 |
| [situation](situation.md) | 处境是会生长的完整状态 | execution-contract处境字段、loop状态更新 |
| [level-spectrum](level-spectrum.md) | 思维模式↔知识的连续谱 | minimal-knowledge-transfer形式化、dfs-guidance评估函数 |

## 文件格式

每个概念文件遵循：定义 / 来源 / 指导了什么 / 适用边界 / 演化 / 开放问题
