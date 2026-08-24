# 第六代系统当前精确合同

**状态**：current
**验证时间**：2026-08-24
**边界**：只冻结当前代码可支持的合同；未实现接口保留为显式缺口。

## Legacy 领域和入口合同

| 接口 | 输入 | 输出 | 当前行为 |
|---|---|---|---|
| `enter.load_solution_records(path)` | 文件或目录路径 | `list[SolutionRecord]` | 始终 `NotImplementedError` |
| `process_absorb.absorb(records, library)` | 已构造解答记录和 Tell 库路径 | 新 Tell 列表 | 可进入 vein analysis，随后在匹配/沉淀 stub 失败 |
| `solve.load_problem(path)` | JSON 路径 | `Problem` | 始终 `NotImplementedError` |
| `process_solve.solve(problem, library)` | Problem 和 Tell 库路径 | `TreeState` | 首次 `inference_explore()` 即失败 |
| `vein_analysis_three_phase(input)` | `AnalysisInput(process="absorb")` | `AnalysisOutput` | 有实现；`process="solve"` 明确失败 |

未实现函数包括：absorb/solve 两侧 `trace_match`、`knowledge_deposit`、orphan trace 存取、Tell
存储、`inference_explore`、`direction_extract`、`guide_expand`。未来实现不得静默改变
`system/schema.py` 的语义；需要版本或 adapter 决策。

## Absorb 侧脉络合同

当前 active Prompt versions 是 `V5/V7/V8/V10`。代码从提示词积累目录和
`system/assets/vein_analysis/` 复制运行资产，生成独立 workdir，记录 manifest，并对 V10 输出运行
`verify_lattice_completeness.py`。V9 是历史 Prompt 资产，不是当前 `PROMPT_VERSIONS` 成员。

该合同具有外部副作用：创建工作目录、启动 tmux/Devin、写 ArangoDB 记录和归档测试产物。它不是
本次可安全执行的纯函数，也没有当前分支 live PASS。

## Solve-side 结构化轨迹合同

公共入口由 `system.solve_vein_analysis.__init__` 暴露：

- `ReasoningTrajectory.from_dict()` 执行 strict、exact-key、fail-closed 解析；
- `analyze_trajectory()` 返回 `AnalysisBundle`；
- `analyze_incrementally()` 对每个前缀重放，并返回最终 bundle 与 replay journal；
- pipeline version、trace ruleset 和 RCA-style version 当前均为 `0.1.0`。

主要不变量：

- DAG 边必须按 occurrence 时间向前；revisit 用新 occurrence 表示，不能制造 cycle。
- state 和 transition FCA context 分离。
- Next Closure 必须等于独立 brute-force oracle，否则整个分析失败。
- relational scaling 只声明 RCA-style；未到 fixed point 时状态为 PARTIAL。
- Trace 必须引用具体 event/edge/rule。
- scientific fingerprint 不含时间戳和输出路径。
- explicit nonclaims 包括 raw 抽取、source span raw 验证、完整 Multi-FCA、规模性能和 DB/Tell 接入。

## CLI 文件合同

`python -m system.solve_vein_analysis.cli analyze` 接收一个严格结构化轨迹文件、全新输出路径和已
验证 asset manifest。CLI：

- 拒绝 symlink、已有输出和 absorb-side 保护路径；
- 在同级 partial 目录中用 exclusive create 写文件并 fsync；
- 默认比较 batch/incremental scientific fingerprint；
- 成功后原子 rename；失败时不保留 sealed output；
- manifest 明确记录 model calls、DB connections、Solver launches 全为 0。

## State Normalizer 合同

`state_normalization.py` 在无模型调用下把 raw axis alias 映射到显式 canonical value，保持 problem、
strategy、representation、knowledge、lifecycle 和 legacy 轴独立。它要求完整 occurrence x required-axis
coverage，并 fail-closed 校验 MUST_LINK、CANNOT_LINK、EXACT_VALUE、重复项、schema drift 和非有限数。

`state_normalized_dag.py` 只生成 sidecar；它要求 PASS evaluation、exact bundle hash、event 存在和
topological order，不改写原 DAG。

## Trace Auditor 合同

`trace_auditor.py` 只审计已结构化 `ReasoningDag`，观察 branch/failure/revisit/reuse/merge/recovery
family。缺失必需 family 是 scientific FAIL；malformed DAG、未知端点、重复 edge、sidecar hash/order
不一致均 fail-closed。它不负责自然语言抽取，也不证明数学语义正确。

## 当前验证

命令：`PYTHONPATH=. python3 -m pytest system/tests/solve_vein_analysis`
结果：295 passed，1 warning，Python 3.14.6，pytest 9.1.1，darwin。
警告：`test_source_tree_sha256` 返回字符串而不是 `None`；本次断言仍通过，但应作为测试质量债务。
