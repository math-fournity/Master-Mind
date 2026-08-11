# FCA再分析全量处理方案（6层67383题）

> 对全部67383道题目的profile做FCA再分析，用FCA先验分类学重新识别原始profile遗漏的非局部/全局tell显现。
> 本方案与`任务追踪/06-题目侧写Profile提取完整方案.md`对齐——FCA再分析在profile提取完成后进行。

---

## 一、总体架构

### 两层依赖关系

```
第一层：Profile提取（06号方案）
  原始题目 → 11步分析 → profile.json → 入库ArangoDB
  状态：Tier 1✅(452) → Tier 2进行中(3/1732) → Tier 3-5待处理

第二层：FCA再分析（本方案）
  已提取的profile → 10步SOP → FCA再分析报告 → 分类学修正
  状态：待启动（Tier 1的452个profile已就绪）
```

**关键约束**：FCA再分析只能在已提取的profile上做。Tier 2-5的题目需要先完成profile提取（06号方案），才能做FCA再分析。

### 分工

- **主agent（流程管理者）**：选择题目、构造subagent prompt、启动subagent、验证产出、执行分类学修正、git commit、更新进度
- **subagent（具体分析者）**：按10步SOP执行FCA再分析、产出报告落盘、返回执行摘要
- **逐个处理，不并发**——每道题完成并验证后再启动下一道
- **分类学修正由主agent亲自执行**——subagent只分析报告，不修正分类学

### 数据基础

- **ArangoDB** `xishujuzhen_math_glm52`，`problem_profiles`集合，`_key`=problem_id
- **`problem_extraction_progress`集合**：67838条记录，`difficulty_tier`字段标识层级
- **`subagents-dirs/{problem_id}/profile.json`**：443个Tier 1题目有文件系统profile
- **数据库备选**：所有profile都可以从数据库读取

---

## 二、6层FCA再分析规划

### 与06号方案的对齐

| 层级 | 题数 | profile提取状态 | FCA再分析状态 | FCA再分析前置条件 |
|---|---|---|---|---|
| **Tier 1** | 452 | ✅全部完成 | **可立即启动** | 无——profile已就绪 |
| **Tier 2** | 1732 | 进行中(3/1732) | 待profile提取完成 | Tier 2 profile提取完成 |
| **Tier 3** | 40717 | 待处理 | 待profile提取完成 | Tier 3 profile提取完成 |
| **Tier 4** | 14260 | 待处理 | 待profile提取完成 | Tier 4 profile提取完成 |
| **Tier 5** | 10676 | 待处理 | 待profile提取完成 | Tier 5 profile提取完成 |
| **Tier 6** | — | 暂不规划 | 暂不规划 | — |
| **合计** | **67837** | | | |

### FCA再分析优先级

FCA再分析按难度从高到低进行（和06号方案的profile提取顺序一致）：
1. **Tier 1（452题）**——最高难度，profile已就绪，**立即启动**
2. **Tier 2（1732题）**——国际顶级竞赛+TST，等profile提取完成后启动
3. **Tier 3（40717题）**——国家级竞赛，等profile提取完成后启动
4. **Tier 4（14260题）**——中等难度基准，等profile提取完成后启动
5. **Tier 5（10676题）**——初等竞赛+教材题库，等profile提取完成后启动

### 为什么从高难度到低难度

- 高难度题目的tell更丰富、更有价值——非局部tell和全局tell在高难度题中更常见
- 分类学修正主要来自高难度题——高难度题更容易暴露分类学的未覆盖情况
- 低难度题目的tell较简单——分类学在高难度题上稳定后，低难度题的FCA再分析可以更快速

---

## 三、Tier 1 FCA再分析详细方案（452题，立即启动）

### 分批策略

- 每批10题，共46批（45批×10题 + 1批×2题）
- 按domain交叉分批——每批覆盖多个domain
- 优先选global tell数较多的（更有可能发现非局部tell显现）
- 12个无`subagents-dirs`目录的早期IMO题目（从数据库读取profile）放最后2批

### 阶段划分

| 阶段 | 批次 | 题数 | 累计 | 检查点 |
|---|---|---|---|---|
| 阶段1 | 批01-05 | 50 | 50 | 阶段性总结：格化思考的普适价值评估 |
| 阶段2 | 批06-10 | 50 | 100 | 阶段性总结：分类学稳定性评估 |
| 阶段3 | 批11-20 | 100 | 200 | 阶段性总结：中期评估 |
| 阶段4 | 批21-30 | 100 | 300 | 阶段性总结 |
| 阶段5 | 批31-46 | 152 | 452 | 最终汇总：Tier 1完整FCA再分析报告 |

### 阶段1的5批（50题）

批01-05的题目在每批开始前由主agent从数据库生成，按以下规则：
1. 排除已完成的题目
2. 按domain交叉分批（每批覆盖至少4个不同domain）
3. 优先选global tell数较多的
4. 确保前50题覆盖全部6个归一化domain

### 批01的10题（已明确）

| 序 | problem_id | domain | tell | global | 题目摘要 | 有目录 |
|---|---|---|---|---|---|---|
| 1 | compfiles_imo1985p6 | analysis | 8 | 2 | 构造序列x_n | Y |
| 2 | compfiles_imo1979p6 | combinatorics | 7 | 3 | 八边形青蛙跳跃 | Y |
| 3 | fate_000255 | algebra | 7 | 3 | #G=396则G非单群 | Y |
| 4 | compfiles_imo1993p6 | general | 8 | 3 | 圆环上n盏灯 | Y |
| 5 | compfiles_imo1991p5 | geometry | 7 | 2 | 三角形内点P | Y |
| 6 | fate_000268 | number_theory | 8 | 3 | √((2+√2)(3+√3))扩域 | Y |
| 7 | compfiles_imo2014p5 | combinatorics | 7 | 3 | Cape Town银行硬币 | Y |
| 8 | compfiles_imo1996p6 | general | 8 | 3 | p+q<n正整数 | Y |
| 9 | compfiles_imo1976p6 | algebra | 7 | 3 | 递推序列u_n | Y |
| 10 | compfiles_imo1992p6 | number_theory | 7 | 3 | S(n)求和函数 | Y |

---

## 四、Tier 2-5 FCA再分析方案（待profile提取完成后启动）

### 启动条件

每个Tier的FCA再分析在该Tier的profile提取完成后启动。profile提取进度见`任务追踪/06-题目侧写Profile提取完整方案.md`。

### Tier 2（1732题）

- profile提取进行中（3/1732）
- profile提取完成后，FCA再分析分173批（每批10题）
- 预期分类学已从Tier 1稳定——Tier 2的FCA再分析修正频率应很低

### Tier 3（40717题）

- profile提取待处理
- profile提取完成后，FCA再分析分4072批（每批10题）
- 数量大——需要评估是否值得全量做，还是抽样做

### Tier 4（14260题）

- profile提取待处理
- profile提取完成后，FCA再分析分1426批（每批10题）

### Tier 5（10676题）

- profile提取待处理
- profile提取完成后，FCA再分析分1068批（每批10题）

### Tier 3-5的抽样策略

Tier 3-5题量大（65653题），全量FCA再分析成本高。在Tier 1和Tier 2的FCA再分析完成后，评估是否需要全量：
- 如果Tier 1+2的FCA再分析已经让分类学稳定（修正频率趋近0）→ Tier 3-5可以抽样做（每层抽100题）
- 如果分类学仍在修正 → Tier 3-5需要全量做以继续暴露问题
- 低难度题目的tell较简单——分类学在高难度题上稳定后，低难度题的FCA再分析价值可能下降

---

## 五、处理流程（每道题）

```
主agent：
  1. 从check list模板建立TODO List（铁律0）
  2. 从prompt模板构造subagent prompt（填入problem_id和产出路径）
  3. 启动subagent（profile选subagent_general）
  4. 等待subagent返回
  5. 用产出验证check list验证产出（铁律0.5）
  6. 如果V-0到V-2不通过 → 重新启动subagent
  7. 如果V-3不通过 → 重新启动subagent
  8. 如果发现分类学问题 → 主agent亲自执行修正流程（7条铁律）
  9. 更新进度跟踪表
  10. git commit（每题或每批commit一次）

subagent：
  步骤0：加载V6提示词全文
  步骤1：读原始profile（文件系统优先，数据库备选）
  步骤2-9：按10步SOP执行FCA再分析
  产出报告落盘到指定路径
  返回执行摘要
```

---

## 六、产出文件命名规范

### 单题产出

`FCA学习笔记/reanalysis/{problem_id}-FCA再分析.md`

### 批次检查点记录

`FCA学习笔记/reanalysis/batch-{tier}-{NN}-checkpoint.md`（tier=T1/T2/T3/T4/T5，NN=批次号）

### 阶段性总结

`FCA学习笔记/reanalysis/phase-{tier}-{N}-summary.md`（N=阶段号）

### Tier最终汇总

`FCA学习笔记/reanalysis/tier-{tier}-final-summary.md`

### 全量最终汇总

`FCA学习笔记/reanalysis/grand-final-summary.md`——全部完成的最终汇总

---

## 七、分类学修正策略

### 修正触发

subagent在步骤9检查分类学问题。如果发现：
1. 分类学无法覆盖某道题的某个tell → 标注"发现分类学问题"
2. FCA理论审查发现分类学不自洽 → 标注"发现分类学问题"

### 修正执行

- **由主agent亲自执行**——不委托subagent
- **按7条铁律执行**——明面版本历史、四要素记录、覆盖性检查、版本总表、文件结构完整、关联文件同步、Schema同步
- **批量合并**——同一批中多个subagent报告分类学问题，主agent合并统一修正

### 修正频率预期

| 阶段 | 预期修正频率 | 原因 |
|---|---|---|
| Tier 1阶段1（前50题） | 较多 | 新题目暴露未覆盖的情况 |
| Tier 1阶段2-3（50-200题） | 下降 | 分类学逐渐稳定 |
| Tier 1阶段4-5（200-452题） | 很少 | 分类学已基本稳定 |
| Tier 2（1732题） | 极少 | 分类学已从Tier 1稳定 |
| Tier 3-5 | 趋近0 | 分类学完全稳定 |

---

## 八、进度跟踪

### Tier 1进度表

| 阶段 | 批次 | 题数 | 累计 | 状态 | 分类学修正次数 |
|---|---|---|---|---|---|
| 阶段1 | 批01-05 | 50 | 50 | 待处理 | - |
| 阶段2 | 批06-10 | 50 | 100 | 待处理 | - |
| 阶段3 | 批11-20 | 100 | 200 | 待处理 | - |
| 阶段4 | 批21-30 | 100 | 300 | 待处理 | - |
| 阶段5 | 批31-46 | 152 | 452 | 待处理 | - |

### 全量进度表

| Tier | 题数 | profile提取 | FCA再分析 | FCA再分析进度 |
|---|---|---|---|---|
| Tier 1 | 452 | ✅完成 | 可立即启动 | 0/452 |
| Tier 2 | 1732 | 进行中(3) | 待提取完成 | 0/1732 |
| Tier 3 | 40717 | 待处理 | 待提取完成 | 0/40717 |
| Tier 4 | 14260 | 待处理 | 待提取完成 | 0/14260 |
| Tier 5 | 10676 | 待处理 | 待提取完成 | 0/10676 |
| **合计** | **67837** | | | **0/67837** |

### 恢复机制

如果session压缩或中断，恢复方式：
1. 读取本方案的进度表，找到当前Tier和批次
2. 读取`FCA学习笔记/reanalysis/`目录，看哪些题已完成
3. 从下一个未完成的题继续

---

## 九、阶段性总结内容

### 每50题（Tier 1阶段1-2）

1. 格化思考的普适价值——50题中有多少题发现了原始profile遗漏的非局部/全局tell显现？
2. 分类学稳定性——50题中分类学修正了几次？修正频率是否在下降？
3. 新发现tell显现的统计——总共发现了多少个？按domain/观察Level/段结构模式分布如何？
4. 典型case——最有价值的trace和最有代表性的分类学修正
5. 是否继续——格化思考是否有普适价值？

### Tier 1最终汇总（452题完成后）

1. 全量统计——452题中新发现的tell显现总数及分布
2. 分类学最终版本——经过452题迭代修正后的最终版本
3. 格化思考的价值评估——在多少比例的题目中发现了遗漏？
4. 分类学修正全历史——从v1到最终版本的所有修正记录
5. 对Tier 2-5的启示——是否值得继续？是否可以抽样？

### 全量最终汇总（全部完成后）

1. 67837题的完整FCA再分析统计
2. 分类学的最终最终版本
3. 格化思考在不同难度Tier的价值差异
4. 对第六代系统的完整启示

---

## 十、风险和应对

| 风险 | 应对 |
|---|---|
| subagent产出质量不稳定 | 产出验证check list（铁律0.5）把关，不通过则重做 |
| 分类学修正频繁导致进度慢 | 前期预期修正较多，中期下降，后期稳定 |
| session压缩导致进度丢失 | 进度表在本文件中，恢复机制见§8 |
| Tier 3-5题量太大（65653题） | Tier 1+2完成后评估是否抽样 |
| profile提取进度阻塞FCA再分析 | Tier 1已就绪可立即启动；Tier 2-5等提取完成 |
| subagent上下文不够 | subagent用subagent_general profile，有独立上下文窗口 |

---

## 十一、关键文件索引

| 文件 | 用途 |
|---|---|
| `FCA学习笔记/fca-reanalysis-full-plan.md`（本文件） | 全量处理方案 |
| `FCA学习笔记/fca-reanalysis-checklist.md` | 执行check list模板（铁律0） |
| `FCA学习笔记/fca-reanalysis-subagent-prompt-template.md` | subagent prompt模板（铁律-1） |
| `FCA学习笔记/fca-reanalysis-output-verification-checklist.md` | 产出验证check list（铁律0.5） |
| `FCA学习笔记/08-先验Tell分类学.md` | 完整分类学（v3）+版本历史 |
| `第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/v6.md` | V6提示词（subagent步骤0加载） |
| `.devin/rules/tell-taxonomy-iteration-audit.md` | 铁律-1/0/0.5 + 10步SOP + 7条版本化审计铁律 |
| `任务追踪/06-题目侧写Profile提取完整方案.md` | profile提取6层方案（FCA再分析的前置条件） |

---

## 十二、批01进度跟踪

| 序 | problem_id | 状态 | 产出文件 | 分类学问题 | 完成时间 |
|---|---|---|---|---|---|
| 1 | compfiles_imo1985p6 | 待处理 | - | - | - |
| 2 | compfiles_imo1979p6 | 待处理 | - | - | - |
| 3 | fate_000255 | 待处理 | - | - | - |
| 4 | compfiles_imo1993p6 | 待处理 | - | - | - |
| 5 | compfiles_imo1991p5 | 待处理 | - | - | - |
| 6 | fate_000268 | 待处理 | - | - | - |
| 7 | compfiles_imo2014p5 | 待处理 | - | - | - |
| 8 | compfiles_imo1996p6 | 待处理 | - | - | - |
| 9 | compfiles_imo1976p6 | 待处理 | - | - | - |
| 10 | compfiles_imo1992p6 | 待处理 | - | - | - |
