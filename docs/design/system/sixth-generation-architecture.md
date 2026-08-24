# 第六代系统当前架构

**状态**：current
**设计对象**：本分支当前实现及其明确目标边界
**非声明**：本文不声称完整 Grove 系统已经可运行。

## 当前组件

| 组件 | 责任 | 当前状态 | 禁止推断 |
|---|---|---|---|
| `system/schema.py` | legacy 四 Pipe 领域类型 | implemented-unverified | 类型存在不等于 Pipe 已实现 |
| `system/vein_analysis.py` | absorb 侧三阶段脉络编排、Prompt 资产、DB/run 记录 | implemented, current live unverified | 不支持 solve mode；不证明模型质量 |
| `system/process_absorb.py` | absorb 目标流程骨架 | partial | Trace 匹配、Tell 沉淀、存储仍未实现 |
| `system/process_solve.py` | Grove/解题引导目标流程骨架 | partial | Solver、匹配、Hint、Guide、tree 均未实现 |
| `system/db.py` | ArangoDB 读写适配器 | implemented-unverified | 未核当前 live schema/data |
| `system/solve_vein_analysis/` | 结构化轨迹的独立离线 DAG/FCA/RCA-style/Trace 分析 | verified offline | 不连接 legacy schema、DB、Solver 或 Tell library |
| solve-side role/qualification tools | Devin/tmux、资格包、审计、State Normalizer、Trace Auditor | development/offline verified | `dangerous` 不是隔离证明；live 未授权 |
| `system/tests/solve_vein_analysis/` | 离线合同、fixtures、失败和冻结证据 | 294 PASS in current environment | 不证明模型和端到端能力 |

## 当前可执行流

### Solve-side 离线流

`ReasoningTrajectory` -> strict validation -> `ReasoningDag` -> state/transition FCA -> RCA-style relational
scaling -> deterministic TraceRecord -> audit/fingerprint -> atomic CLI output directory。

该流已由当前 294 项测试覆盖。输入必须已经是结构化事件轨迹；raw natural-language extraction 是明确
nonclaim，`live_extraction=NOT_TESTED`。

### Absorb 侧三阶段流

`SolutionRecord` -> V5/V7/V8/V10 并发格化 -> 程序枚举 -> synthesis -> legacy `AnalysisOutput`。

这条代码会使用 tmux/Devin、工作目录、ArangoDB 和归档写入；本次重建没有授权执行。流程之后的
Trace 匹配和 Tell 沉淀是 stub，因此 `absorb()` 不是完整可运行入口。

### 当前不存在的端到端流

`solve.py` 和 `enter.py` 都在加载阶段或后续阶段抛 `NotImplementedError`。完整的
Solver -> Trace -> Tell -> Hint -> Guide -> tree 循环只是 target state。

## 目标架构

目标仍采用四个逻辑责任：Solver、Parser、Telling、Guide，并由解答吸收补充 Tell/Hint 知识。
但目标模块只能在当前需求、接口和证据闭合后逐步接入；不得直接把历史 Seven/Eight/analysis 代码
复制进 `system/`。

优先顺序：

1. 冻结 current contracts 和结构化轨迹输入边界。
2. 统一 Trace 两类合同或定义显式 adapter。
3. 实现并验证 Tell/Hint registry 与匹配。
4. 实现 Guide/tree persistence 和失败恢复。
5. 只有在用户授权后进行 live role qualification。
6. 端到端 golden slice 通过后才可声称 Grove 闭环实现。

## 失败与隔离边界

- legacy absorb 运行会触及 DB、tmux、Devin 和 repo/D 盘文件；默认不运行。
- solve-side deterministic modules 默认不得连接模型、DB、网络或 Solver。
- runtime role assets 必须与项目治理 `AGENTS.md` 隔离；Prompt 文本不能证明角色行为发生。
- historical attempt ID、sealed bundle 和失败证据不可覆盖或重跑。
- 大数据和大 run body 只保留 D 盘实物及 Git 指针。

## 当前/目标判定

当前架构的中心不是“四 Pipe 已完成”，而是“一个部分实现的 legacy 目标骨架，加一个经离线验证的
独立 solve-side 分析核心”。后续实现和目录迁移都必须保持这个事实，不得用理想图覆盖当前缺口。
