# 第六代系统当前概念

**状态**：current
**事实边界**：稳定语义来自当前用户裁定和代码；历史来源只解释概念演进。

## 概念状态表

| 概念 | 当前含义 | 当前实现状态 |
|---|---|---|
| Problem | 题目标识、文本、可选 domain/answer | `system.schema.Problem` 已定义 |
| Vein | 从解答或推理轨迹分析出的段、分支和结构 | absorb 侧已实现；solve 侧 legacy schema 模式未实现 |
| Trace | 从脉络或结构化 DAG 中识别的可引用模式 | 两套当前代码合同并存，见下文 |
| Tell | 对可分叉但未分叉信号的标准化描述 | 类型已定义；匹配、registry 和沉淀未实现 |
| Hint | 给新推理分支的方向，不是替原 AI 解题 | 类型已定义；Guide/runtime 未实现 |
| Grove | Trace/Tell/Hint 驱动引导树和推理树生长的目标循环 | 设计概念，当前没有闭环实现 |
| VMS | VMS-28 至 VMS-43 的实验和验证编号谱系 | 证据/历史概念，不是一个 runtime module |
| FCA/RCA-style | 对闭包、概念和关系缩放的数学/工程工具 | 两条实现路径，边界不同 |

## Trace 的两个代码合同

当前 repo 不能把两类 Trace 合并成一个已经统一的类型：

1. `system.schema.Trace` 属于原四 Pipe 目标架构，字段包括 level、local/non-local/global、描述和来源段。
   absorb 侧 `vein_analysis.py` 会产出此类型；solve 侧调用路径尚未实现。
2. `system.solve_vein_analysis.models.TraceRecord` 属于独立 solve-side 离线分析，从严格
   `ReasoningDag` 规则生成 branch/failure/revisit/reuse/merge/recovery 等 trace family，并引用具体
   event/edge/rule。它不等价于 Tell，也不连接 tell library。

未来统一必须先定义转换合同并用测试证明；当前 canonical 文档只保留两者的明确边界。

## Tell 与 Hint

当前稳定语义来自 `system/schema.py` 和已抽取到本文的历史根定义；原文件由
`pre-sixth-gen-current-repo-2026-08-24:000-v0-2026-08-08-引导树闭环-识别端结构定义.md` 恢复：

- Tell 是观察侧信号，描述推理在哪个位置可以分叉但没有分叉。
- Hint 是注入给新 Solver 分支的方向。
- Hint 的作用不是让原 AI 在卡点继续，而是在根或路径节点开启新边。
- Tell/Hint 是概念和数据类型，不是已交付能力。`trace_match()`、`knowledge_deposit()`、
  `direction_extract()`、`guide_expand()` 均未实现。

Tell 分类学和后期非特化 POC 含大量候选定义。只有经当前代码、测试、用户裁定或后续证据支持的
结论才可进入本文；其余内容保留在历史抽取账本。

## FCA、RCA 与格

当前有两条不同实现：

- absorb 侧 `verify_lattice_completeness.py` 用 Next Closure 等程序检查 AI 产出的形式上下文和
  闭元素，服务 `vein_analysis.py` 的 V5/V7/V8/V10 三阶段编排。
- solve-side `fca.py` 对结构化 DAG 的 state/transition context 枚举概念，并用独立 brute-force
  oracle 对照；`pipeline.py` 的 relational scaling 明确标记为 RCA-style，不声称完整 Multi-FCA。

FCA 不能替代时间、因果或关系边；代码中的 explicit nonclaims 是当前合同的一部分。

## Grove 和两棵树

Grove 是当前目标架构，不是当前实现状态。目标循环是：Solver 产生轨迹，Parser 识别 Trace，
Telling 将 Trace 与 Tell 匹配，Guide 将 Hint 变成引导树新边，再启动新的 Solver 分支。

当前实际缺口包括 Solver runtime、solve-mode vein analysis、Trace/Tell registry、Tell 匹配、Hint
选择、Guide 展开、tree persistence、停机和端到端证据。因此任何“第六代已形成 Grove 闭环”的
说法都不成立。

## 概念来源与替代

- 303-309 号文档：Trace/Tell/Hint 与从提取到查询的思想来源。
- 318/319 号文档：四 Pipe 和形式化目标架构。
- 343 号及 commit `38d46d3`：`six/` 合并进 `system/`。
- 391 号及 commit `7392235`：取代 363，冻结旧资格链并转向真实数据 golden slice。
- `system/` 代码和当前测试：决定当前实现与验证，不由上述历史文档反向覆盖。
