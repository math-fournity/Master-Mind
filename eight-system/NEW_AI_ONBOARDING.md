# Eight System · 新AI入口文档

> **用途**：本文档是给新AI（Devin/Claude/GPT/另一个GLM-5.2 session）的入口文档。读完本文档后，按§4的阅读顺序读5份文档，即可获得完整认知并开始执行POC。
> **与351号的区别**：351号委托时传递了理论但没有传递实现约束，导致外部AI产出过度设计（371号迁移工程+372号帕累托前沿）。本文档**同时传递理论、实现约束和过度设计防护**。

---

## 1. 我们在做什么（3句话）

我们在做一个AI数学系统，核心是：**从推理AI的thinking中提取思维模式（trace），去特化成非特化提示词（Tell），用Tell引导新AI走新分支。**

当前阶段是**实验验证**：用一个叫TellCore v0的Tell（局部-全局表示切换，7个字段），在数学竞赛题上做R/L/D/LD四组对照实验，验证Tell的因果效应。

Phase 0已在1631题上完成——发现TellCore v0的价值是"认知支架"（lineage提供推理锚点），不是"token效率"或"信息传递"。

---

## 2. "中"的guardrail（过度设计防护，5句话）

**非特化研究本身存在一条钟形曲线**——理论复杂度和实践指导力呈钟形关系。峰值在345-347号（钟形曲线+三步法+形态修正），371/372号越过峰值（迁移工程+帕累托前沿，逻辑正确但不可操作）。

**你必须在峰值范围内工作**：
- ✅ 用345-347号的钟形曲线+三步法+形态修正
- ✅ 用352号的三个独立指标（近迁移/远迁移/误触发），但不合成综合效用
- ❌ 不要引入11变量模型、八契约、13条学术路线、帕累托前沿、概念格
- ❌ 不要扩展理论——先跑通已冻结的POC，再谈理论扩展
- ❌ 不要在1道题4次运行的实验规模上设计9维偏序

**详见**：`docs/钟形曲线到帕累托前沿的演化分析.md`

---

## 3. 当前状态

| 阶段 | 状态 | 产出 |
|---|---|---|
| Phase 0（1631题） | ✅ 完成 | R/L/D/LD四组对照 + continue实验 |
| Step 4（continue实验） | ✅ 完成 | L在continue后立即输出proof（thinking中已完成），D/R失败 |
| 假说 | ✅ 修正 | token efficiency → cognitive scaffold（认知支架） |
| §3方案缩减 | ✅ 完成 | 九个可→三个可，8维向量→T1/T2例子 |
| Step 5预注册 | ✅ DRAFT | Phase 1：1843/1709/1962跨题泛化验证 |
| Step 6预注册 | ✅ DRAFT | Lineage分解：L1结论/L2推导过程/L3完整 |
| Step 7预注册 | ✅ DRAFT | Phase 2：false_friend/boundary题Selector验证 |

**核心假说**：lineage提供"认知支架"（推理锚点），direction提供"工具提示"（route finding）。L在thinking中完成证明但hit token limit，LD在token预算内完成proof输出。

**关键预测**：1962是TellCore v0的适用边界——1962的瓶颈是操作路径不是工具方向，L/D/LD可能都失败。

---

## 4. 阅读顺序（6份文档，按顺序读）

### 第1步：理解全局（读1份）

**`README.md`**（157行）——文档索引、目录结构、文档关系图、核心发现、当前状态。读完后你知道有哪些文档、它们之间的关系、我们到了哪里。

### 第2步：理解方案（读1份）

**`docs/非特化方案-v1.md`**（613行）——核心方案文档。重点读：
- §2.3-2.6：钟形曲线+三步法+形态修正（这是"中"的峰值）
- §3.1：因果充分的取商（已缩减为"三个可"）
- §4.1：TellCore v0的字段消融核心发现
- §8.5：修正后的实现顺序（每个Step标注了验证的峰值维度）

### 第2.5步：理解工作方式（读1份，2026-08-16新增）

**`docs/两棵树实现时机与基本实践方式.md`**——两条用户确认的治理决策：①不实现两棵树，但实验记录必须树形化可回填（毕业条件已写明）；②每轮研究必须是核心循环的一次真实旋转（真实跑→读tell→给hint→接脉络→看结果，五个动作亲手完整执行，不得简化成模板拼接或静态Hint属性研究）。**这决定你执行任何Step时的动作标准。**

### 第3步：理解"中"的定位（读1份）

**`docs/钟形曲线到帕累托前沿的演化分析.md`**（572行）——为什么345-347号是峰值、371/372号越过峰值、应该取的"中"是什么。**这份文档是你的guardrail——它告诉你不要做什么。**

### 第4步：理解Phase 0结果（读2份）

**`runs/phase0/experiment_report.md`**（117行）——Phase 0的4组结果和contrast计算。

**`runs/phase0/experiment_report_step4.md`**（164行）——continue实验结果和钟形曲线实证补充（分层峰值：认知维度vs执行维度）。

### 第5步：理解你的任务（读1-3份，取决于你执行哪个Step）

**`runs/phase1/preregistration.md`**（123行）——Step 5：1843/1709/1962跨题泛化验证。

**`runs/lineage_decomp/preregistration.md`**（108行）——Step 6：Lineage分解实验。

**`runs/phase2/preregistration.md`**（146行）——Step 7：Selector验证。

---

## 5. 你的任务

**执行已冻结的POC预注册文档**。具体取决于你被分配哪个Step：

### 如果执行Step 5（Phase 1）：
1. 从283号tree组提取1843/1709/1962的lineage
2. 构造R/L/D/LD prompt文件
3. 冻结`runs/phase1/preregistration.md`（改为FROZEN状态）
4. 用solver_harness跑12次原始运行 + continue运行
5. 用contrast_calculator.py计算contrast
6. 写实验报告

### 如果执行Step 6（Lineage分解）：
1. 从Phase 0的L组lineage中分解出L1（结论）和L2（推导过程）
2. 确认L1和L2的token长度大致相同
3. 冻结`runs/lineage_decomp/preregistration.md`
4. 用solver_harness跑3组对照 + continue运行
5. 写实验报告

### 如果执行Step 7（Phase 2）：
1. 构造1-2道数学正确的false_friend题（需独立数学核验）
2. 构造1道boundary题（1962变体）
3. 实现Selector（从题目特征匹配trigger_boundary和negative_boundary）
4. 冻结`runs/phase2/preregistration.md`
5. 跑实验 + 计算Selector准确率
6. 写实验报告

---

## 6. 不要做的事（过度设计防护）

| 不要做 | 理由 | 详见 |
|---|---|---|
| 不要引入11变量模型 | 1道题4次运行无法分离11个变量的效应 | 演化分析§2.3 |
| 不要引入八契约 | 负迁移/成本/组合在当前规模不是核心 | 演化分析§2.3 |
| 不要引入帕累托前沿 | 9维偏序需要的研究规模远超当前能力 | 演化分析§2.4 |
| 不要引入13条学术路线 | 先跑通一个TellCore v0再谈理论扩展 | 演化分析§2.3 |
| 不要引入概念格/偏序 | 在当前单一TellCore v0阶段没有多个Tell可比 | 演化分析§2.4 |
| 不要扩展TellCore v0字段 | 7字段最小充分集已通过六门审计，先验证再扩展 | 方案§4.1 |
| 不要在看到结果后追加arm或修改判定标准 | 这是预注册的核心约束 | 每份预注册§停止规则 |
| 不要把Tell升级为"方法对象" | Tell是提示词，不是软件工程对象 | 演化分析§4.3 |
| 不要实现/打磨两棵树 | 树是多旋转多分支的状态机器，当前单圈实验的树是退化的；树属于第六代`system/`领地 | 两棵树实现时机与基本实践方式 |
| 不要跳过循环动作（把Hint当静态文本测） | 每轮研究必须是循环的真实旋转：真实跑→读tell→给hint→接脉络→看结果；Phase 0/1的教训 | 两棵树实现时机与基本实践方式 |

---

## 7. 实现约束（351号教训的修正）

351号委托时没有传递实现约束，导致外部AI产出过度设计。本次明确传递：

| 约束 | 值 | 理由 |
|---|---|---|
| 实验规模 | 1道题4次运行（Phase 0）→ 3道题12次运行（Phase 1） | 当前阶段的实际能力 |
| 模型 | devin cli默认模型（GLM-5.2 High） | 与Phase 0一致 |
| Token预算 | 无限制（devin cli默认） | 与Phase 0一致 |
| 工具策略 | solver_harness默认（无工具） | 与Phase 0一致 |
| 理论复杂度上限 | 345-347号+352号（钟形曲线+三步法+形态+三指标） | "中"的峰值 |
| 理论复杂度下限 | 不低于346号三步法 | 不能比峰值更简单 |

---

## 8. 关键文件位置

| 文件 | 路径 | 用途 |
|---|---|---|
| 方案文档 | `docs/非特化方案-v1.md` | 核心方案（8个部分） |
| 演化分析 | `docs/钟形曲线到帕累托前沿的演化分析.md` | "中"的guardrail |
| TellCore v0定义 | `src/tellcores/local_global_switch.yaml` | 7字段YAML |
| Phase 0预注册 | `runs/phase0/preregistration.md` | 已完成的Phase 0预注册 |
| Phase 0报告 | `runs/phase0/experiment_report.md` | Phase 0结果 |
| Step 4报告 | `runs/phase0/experiment_report_step4.md` | continue实验+钟形曲线实证补充 |
| Phase 1预注册 | `runs/phase1/preregistration.md` | Step 5预注册（DRAFT） |
| Lineage分解预注册 | `runs/lineage_decomp/preregistration.md` | Step 6预注册（DRAFT） |
| Phase 2预注册 | `runs/phase2/preregistration.md` | Step 7预注册（DRAFT） |
| contrast计算脚本 | `scripts/contrast_calculator.py` | 自动计算contrast |
| solver_harness | 项目根目录的solver_harness（详见AGENTS.md） | 启动Solver的devin cli实例 |

---

## 9. 一句话总结

**在345-347号的峰值范围内，执行已冻结的POC预注册，不要扩展理论。先跑通，再扩展。**
