# system/docs/ —— system的完整内部认知文档

system/docs/承载理解system中任意模块所需的**所有内部认知**，不只是模块设计说明书。包括三个层次：

1. **系统级认知**——理解任何模块都需要的前置认知（根本认知、四Pipe架构、设计原则、验证历史）
2. **跨模块认知**——跨模块的"晾衣架"和知识层（研发文档索引、代码映射、POC清单、术语映射）
3. **模块级认知**——模块设计说明书（接口、架构、数据流、设计决策）

## 文档清单

| 文档 | 模块 | 状态 | 说明 |
|---|---|---|---|
| `architecture.md` | 系统架构 | ✅ 已写 | 四个Pipe+两个过程+设计原则（解放思想/反射）+提示词设计认知+VMS-28验证历史+根本认知 |
| `references.md` | 研发文档索引 | ✅ 已写 | 研发过程文档清单（303-372号）+代码元素到研发文档的映射+POC验证清单+三个核心问题 |
| `schema.md` | 数据结构 | ✅ 已写 | 25个dataclass+FCA术语映射（双轨术语330号）+核心数据结构详解 |
| `vein_analysis.md` | 脉络分析 | ✅ 已写 | 三阶段架构：格化→程序枚举→综合分析+文件拆分流程控制 |
| `solve_vein_analysis.md` | 解题侧非线性脉络分析 | 🟡 核心PASS/前端未资格化 | 独立事件DAG、FCA/RCA-style后端；VMS-40离线PASS；VMS-41封存为INCONCLUSIVE/NOT_QUALIFIED；VMS-41R1零模型链已闭合；VMS-42 State Normalizer链与VMS-43 Trace Auditor结构审计已实现；live仍未授权 |
| `solve_vein_analysis_runbook.md` | 解题侧脉络运行手册 | ✅ 已同步 | 资产校验、293项测试、历史POC、VMS-39控制面边界、VMS-40确定性bundle、VMS-41只读复核、VMS-41R1零模型链、VMS-42 State Normalizer链与VMS-43 Trace Auditor复验 |
| `process_absorb.md` | 解答吸收 | 待写 | 入题侧——从外部解答提炼tell/hint |
| `process_solve.md` | 解题引导 | 待写 | 解题侧——引导树展开 |
| `db.md` | 数据库 | 待写 | ArangoDB封装、集合定义、problem_entries抓手 |

解题侧非线性脉络分析、Trace/Tell/Hint、推理树、引导树、Seven模拟接入和全链路golden slice的当前任务状态不在本目录复制维护；唯一追踪入口是`第六代系统研发过程文档/363-v0-2026-08-14-解题侧非线性脉络分析后续路线图-阶段门与任务追踪.md`。全部自动测试与POC物证从`system/tests/solve_vein_analysis/README.md`进入。

## 写入规则

1. **按模块组织**——每个模块一个 `.md` 文件，文件名和模块名一致
2. **内容标准**——见 `system/README.md` 中"文档内容标准"
3. **同步更新**——模块代码变更时，同步更新对应的模块文档
4. **.ref引用**——模块的 `.ref` 文件引用对应的模块文档路径
