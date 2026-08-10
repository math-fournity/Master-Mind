# 第六代AI数学系统架构（six/）

本目录是第六代AI数学系统的形式化架构代码。

## 文件结构

```
six/
├── __init__.py    # 包初始化，导出所有公共接口
├── types.py       # 所有数据结构（dataclass定义）
├── pipes.py       # 四个Pipe函数 + 步骤5分叉函数
├── loops.py       # 两个完整流程函数 + 辅助函数
└── README.md      # 本文件
```

## 四个Pipe

| Pipe | 函数 | AI名 | 职责 |
|---|---|---|---|
| Pipe 0 | `pipe_0_solver()` | Solver AI | 推理探索，产生thinking/trajectory |
| Pipe 1 | `pipe_1_parser()` | Parser AI | 提取格化全Level Trace（步骤1-3）+ 步骤5存档/建立新tell |
| Pipe 2 | `pipe_2_telling()` | Telling AI | 并发trace→tell匹配（步骤4） |
| Pipe 3 | `pipe_3_guide()` | Guide AI | 引导树填充，启动新Solver AI |

## 两个过程

| 过程 | 流程函数 | 说明 |
|---|---|---|
| 过程A | `grove_core_loop()` | Grove核心循环——分析推理AI上下文 |
| 过程B | `tell_library_growth_loop()` | tell库增长循环——分析外部解答记录 |

## 步骤差异

| 步骤 | 过程A | 过程B | 是否相同 |
|---|---|---|---|
| 步骤1：分析脉络 | 从Thinking分析，可能有分叉（树/DAG） | 从SolutionRecord分析，通常线性 | 相似但不完全相同 |
| 步骤2：格化脉络 | 在有分叉的脉络上格化，多分支分别格化 | 在线性脉络上格化 | 相似但不完全相同 |
| 步骤3：识别trace | 分叉位置本身可能是trace | 不需要考虑分叉位置 | 相似但不完全相同 |
| 步骤4：Telling AI | 拿着trace找tell | 拿着trace找tell | 完全相同 |
| 步骤5：分叉 | 取hint填引导树 / 存档孤悬trace | 确认匹配 / 建立新(tell,hint) | 不同 |

## 当前状态

所有Pipe函数和流程函数目前只有签名和docstring，实现待POC验证后填充。

POC验证方案见：`第六代系统研发过程文档/317-v0-2026-08-10-第六代系统POC验证方案-大量POC的设计.md`

## 来源文档

- 319号：形式化定义（本目录的源文档）
- 318号：Pipe命名与AI命名
- 316号：理想化工作过程
- 315号：完整工作流+完备性检查
- 314号：三个必须着力解决的问题
- 311号：并发Telling AI方案
- 304号：FCA与工程方案对应
