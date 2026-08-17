# system/ —— AI数学系统的物理实现

`system/` 是整个AI数学系统的物理实现代码。不是用来描述系统的，而是未来真正可以工作的系统代码。

## 目录结构

```
system/
├── README.md                      ← 本文件——目录规范和使用方法
├── docs/                          ← 系统设计说明书（按模块组织）
├── schema.py                      ← 数据结构定义（Problem/Tell/Trace/TreeState等）
├── db.py                          ← 数据库操作（ArangoDB封装）
├── db_schema.py                   ← 数据库集合定义和阶段配置
├── log.py                         ← 日志模块（341号——滚动日志1MB×500）
├── vein_analysis.py               ← 脉络分析（格化→程序枚举→综合分析，三阶段架构）
├── solve_vein_analysis/            ← 解题侧非线性脉络分析（独立事件DAG+FCA/RCA-style POC）
├── verify_lattice_completeness.py ← 闭元素枚举+三层验证（阶段1.5程序枚举）
├── process_absorb.py              ← 解答吸收过程（入题侧）
├── process_solve.py                ← 解题引导过程（解题侧）
├── enter.py                       ← 入题入口脚本
├── solve.py                       ← 解题入口脚本
├── assets/                        ← 运行时资产（AGENTS模板——运行时复制到工作目录）
├── tests/                         ← 测试资产（POC验证脚本、基线数据、历史运行归档）
└── run_*.py                       ← 运行脚本（特定题目的测试运行）
```

解题侧的全部测试和POC必须从`system/tests/solve_vein_analysis/README.md`进入；该索引连接协议、结果、repo/D盘物证、Verdict与阶段门。**当前总任务追踪以391号新方案为准**（`第六代系统研发过程文档/391-v0-2026-08-16-解题侧脉络分析新工作方案-取代363号路线图.md`——363号及route-lock已于2026-08-16标记SUPERSEDED，资格链冻结，勿再按其指针推进）。

## docs/ —— system的完整内部认知文档

`system/docs/` 承载理解system中任意模块所需的**所有内部认知**，不只是模块设计说明书。包括三个层次：

1. **系统级认知**——理解任何模块都需要的前置认知（根本认知、四Pipe架构、设计原则、验证历史）
2. **跨模块认知**——跨模块的"晾衣架"和知识层（研发文档索引、代码映射、POC清单、术语映射）
3. **模块级认知**——模块设计说明书（接口、架构、数据流、设计决策）

### 目录规范

```
system/docs/
├── README.md                    ← docs目录索引
├── vein_analysis.md             ← 脉络分析模块设计说明书
├── solve_vein_analysis.md       ← 解题侧非线性脉络分析模块说明
├── solve_vein_analysis_runbook.md ← 解题侧离线核心+Devin认知角色/tmux调试运行手册
├── process_absorb.md            ← 解答吸收过程设计说明书
├── process_solve.md             ← 解题引导过程设计说明书
├── db.md                        ← 数据库设计说明书
├── schema.md                    ← 数据结构设计说明书
└── ...
```

### 文档内容标准

每个模块文档必须包含：

1. **模块定位**——这个模块在系统中做什么，和其他模块的关系
2. **架构设计**——模块内部的架构（如三阶段架构），关键设计决策
3. **接口定义**——对外暴露的函数/类，输入输出
4. **数据流**——数据从哪里来，经过什么处理，到哪里去
5. **数据库记录**——模块创建/更新哪些数据库集合
6. **关键设计决策**——为什么这样设计，考虑过什么替代方案
7. **待实现/待决策**——TODO和待决策的问题

### 与其他文档目录的关系

| 目录 | 性质 | 内容 |
|---|---|---|
| `system/docs/` | **系统设计说明书** | 按模块组织的正式设计文档——系统"怎么实现的" |
| `第六代系统技术说明书/` | 技术说明书 | 系统级的技术规格——系统"应该做什么" |
| `第六代系统研发过程文档/` | 研发过程文档 | 设计思想的来源——研发过程中的思考、争论、方案演进 |
| `Tell分类学研究过程文档/` | 分类学研究 | Tell分类学的迭代审计记录 |

**演进关系**：研发过程文档中的设计决策 → 沉淀到技术说明书 → 由 `system/` 物理实现 → 实现细节记录在 `system/docs/`

### .ref 文件关系

`system/` 中每个 `.py` 代码文件的 `.ref` 文件，可以引用 `system/docs/` 中的模块文档。例如 `vein_analysis.ref` 中可以写：
```
system/docs/vein_analysis.md
```

这样理解某个模块时，先读 `.ref` 找到对应的模块文档，再读文档理解设计。

## 入题侧与解题侧脉络分析的边界

- `system/vein_analysis.py` 与 `system/assets/vein_analysis/` 属于既有入题侧管线；
- `system/solve_vein_analysis/` 与 `system/assets/solve_vein_analysis/` 属于独立解题侧实验管线；
- 后者不得通过 import、复制运行资产或共享工作目录来修改前者；
- 解题侧确定性核心已完成结构化轨迹后的离线 POC；独立 Devin 文件写入 POC 和 tmux 交互调试档已进入开发性实测，但角色资格、流式抽取与 `process_solve.py` 接入仍未通过。
- 解题侧tmux live workspace与较大POC物证使用独立D盘根`/data/master-mind-solve-vein-data/`；不得借用Seven、题海Solver或入题侧运行目录，也不得fallback到repo/Home/`/tmp`。
- 解题侧Devin认知角色的当前候选执行档是no-sandbox + `dangerous`；其工作区权限由冻结的角色`AGENTS.md`/`TASK.md`约束并用原始tool events审计。VMS-38已支持这个`INTERACTIVE_TMUX_DEBUG`执行合同：D盘workspace、严格输出/DONE、exact model、边界内工具调用、唯一退出和exit 0成立；它仍是`DEVELOPMENT_ONLY`，不等于强隔离或角色资格PASS。历史receipt的ATIF计数错误已在运行后解析器中修正，但不得回写历史bundle。
- VMS-41四个串行one-shot attempt已经全部消费并封存，artifact/replay链PASS，但冻结机械结果为0/4、协议`INCONCLUSIVE_PROTOCOL`，当前Event Extractor profile仍为`NOT_QUALIFIED`。事后诊断因先见机械结果而明确是`BREACHED_BEFORE_MANUAL_AUDIT / FAILURE_LOCALIZATION_ONLY`；其独立D盘audit bundle已封存，原四ID绝对不得重跑。VMS-41R1的独立V2 occurrence/projection evaluator、联合file-effect auditor与19场景不可变开发校准包已通过；全新未见qualification pack、阈值、盲审rubric、attempt IDs、0.4.1角色资产、零模型preexecution freeze、live runner shell、不可消费LiveRunPermit/盲审包计划、sealed manual judgment合同、hidden join simulator、fake materializer、final qualification join receipt和临时append-only写包dry-run已冻结。VMS-42 State Normalizer离线核心、零模型资格包、hidden join、reviewer judgment合同、final reviewer+hidden-join receipt、unseen qualification extension与DAG writeback sidecar已新增；VMS-43 Trace Auditor结构审计已新增。当前全量293项回归PASS。以上仍不资格化模型；live资格实验仍需新的明确人签LiveRunPermit。
- Trace/Tell积累采用独立、内容寻址的分片文件；AI按稳定item ID逐项分析，程序以append-only cursor和`missing=duplicate=unknown=0`对账证明遍历完成。`AGENTS.md`只承载短遍历协议、权限与Schema指针，不承载Tell/Trace全量内容。

## 代码规范

### .ref 文件规则

`system/` 中每个 `.py` 代码文件必须有一个同名的 `.ref` 文件（如 `schema.py` → `schema.ref`）。`.ref` 文件内容是相对 repo 根目录的文档路径列表——理解该模块需要参考的文档。代码文件和 `.ref` 文件必须同步更新。详见 `.devin/rules/system-ref-sync.md`。

### .ai-check 文件规则

`system/` 中每个 `.py` 代码文件必须有一个同名的 `.ai-check` 文件。详见 `.devin/rules/six-dual-check-mechanism.md`。
