# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000302
- **文件路径**: subagents-dirs/fate_000302/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396412（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000302/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let k be a field, and set A = k[X,Y,Z]/(X²-Y², Y²-Z², XY, YZ, ZX). Show that A is Gorenstein. Lean形式化中，Gorenstein环定义为：Noetherian环在所有极大理想处的局部化都是Gorenstein局部环；Gorenstein局部环定义为：Noetherian局部环且inj.dim_R R < ∞。定理声明为 `isGorensteinRing_quot_x2_sub_y2_y2_sub_z2_xy_yz_zx`，证明为sorry（未填写）。
- 解答核心思路（1-2句话）：识别A是Artinian局部环（dim_k A = 5），利用"Artinian局部环是Gorenstein当且仅当其socle为1维"的判据，直接计算socle = (t)（t = X² = Y² = Z²）为1维，故A是Gorenstein。
- 解答关键步骤列表：
  1. 分析环的关系：X²=Y²=Z²=:t, XY=YZ=ZX=0
  2. 推导t的幂零性：tX=X³=X·Y²=(XY)Y=0, 同理tY=tZ=0, t²=X⁴=0
  3. 确定k-基{1,X,Y,Z,t}，dim_k A=5，故A是Artinian
  4. 确定A是局部环，极大理想m=(X,Y,Z)，剩余域k
  5. 计算socle：对a=α+βX+γY+δZ+εt，由X·a=αX+βt=0⇒α=β=0，Y·a=γt=0⇒γ=0，Z·a=δt=0⇒δ=0，故Soc(A)=(t)≅k为1维
  6. 应用Artinian局部环Gorenstein判据：socle 1维⇒Gorenstein
  7. A是Artinian故有唯一极大理想，故A作为环也是Gorenstein

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：环A是什么样的？需要证明什么性质？Gorenstein的定义是什么？ | A = k[X,Y,Z]/(X²-Y², Y²-Z², XY, YZ, ZX)，需证A是Gorenstein。Gorenstein环定义：Noetherian环在所有极大理想处局部化均为Gorenstein局部环；Gorenstein局部环：Noetherian局部环且inj.dim_R R < ∞。 |
| 2 | 自由列举 | 0.7 | 列出你所知道的所有证明一个环是Gorenstein的方法。 | 1) 直接计算内射维数；2) 完全交是Gorenstein；3) 对偶理论；4) Artinian局部环的socle判据；5) 局部化后在每个极大理想处验证；6) 利用正则序列。 |
| 3 | 小尝试 | 0.4 | 尝试直接计算A作为A-模的内射维数。 | 直接计算内射维数非常困难——需要构造A的内射分解，对于这个商环来说计算量巨大且难以处理。这条路看起来不太实际。 |
| 4 | 思维操作引导 | 0.5 | 仔细分析环A的结构。从关系X²=Y²=Z²和XY=YZ=ZX=0出发，推导所有乘法关系。A的k-维数是多少？A是否是Artinian？ | 令t=X²=Y²=Z²。由X²Y=X(XY)=0但X²Y=Y²·Y=Y³，故tY=0。同理tX=tZ=0。t²=X⁴=X·X³=0。k-基为{1,X,Y,Z,t}，dim_k A=5，故A是Artinian。A是局部环，极大理想m=(X,Y,Z)，剩余域k。 |
| 5 | 推进 | 0.4 | 计算A的socle，即Soc(A)={a∈A : m·a=0}。 | 对a=α+βX+γY+δZ+εt：X·a=αX+βt=0⇒α=β=0；Y·a=αY+γt=0⇒γ=0；Z·a=αZ+δt=0⇒δ=0。故Soc(A)={εt}=(t)≅k，1维。 |
| 6 | 思维操作引导 | 0.5 | 对于Artinian局部环，Gorenstein的判据是什么？用socle如何刻画？ | Artinian局部环(R,m)是Gorenstein当且仅当Soc(R)={r∈R : m·r=0}作为R/m-向量空间是1维的。 |
| 7 | 能量传递引导 | 0.3 | 将socle计算与判据结合，完成证明。 | A是Artinian局部环，m=(X,Y,Z)，Soc(A)=(t)≅k为1维。由Artinian局部环Gorenstein判据，A是Gorenstein局部环。A是Artinian故有唯一极大理想，故A作为环也是Gorenstein。□ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.4+0.5+0.4+0.5+0.3 = 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 商环结构，由多项式环模去理想得到；环的关系蕴含幂零元结构；需将抽象同调性质（Gorenstein）归结为具体线性代数计算（socle维数）
- key_objects: ["k[X,Y,Z]", "理想(X²-Y², Y²-Z², XY, YZ, ZX)", "商环A", "极大理想m=(X,Y,Z)", "socle Soc(A)", "幂零元t=X²=Y²=Z²", "内射维数"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_analysis", "criterion_translation", "explicit_computation", "synthesis"]
- primary_pattern: criterion_translation
- knowledge_required: ["Gorenstein环定义", "Artinian局部环", "socle定义与计算", "Artinian局部环Gorenstein判据", "内射维数", "局部环与极大理想"]
- key_insight: 环A是Artinian的（dim_k A=5），因此Gorenstein性质归结为socle的1维性，这是一个具体的线性代数计算

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 抽象同调代数（内射维数定义的Gorenstein性质）
- translation_to: 具体线性代数（socle维数计算）
- translation_type: abstract_to_concrete

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["Gorenstein", "socle", "Artinian局部环", "内射维数", "幂零元", "商环", "socle判据"]
- expected_ai_method: bare AI会尝试直接从Gorenstein的定义出发计算内射维数，或尝试一般性的Gorenstein判据，不识别环的Artinian结构
- correct_method: 识别A是Artinian局部环，利用socle维数判据将问题转化为具体的线性代数计算

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=direct_calculation, gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有分类体系覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs概要**：
- R1: tell=AI看到Gorenstein问题但未分析环结构, hint=描述问题结构, level=0.8, 纯元认知观察, topology=(characterization, direct_calculation, method_problem_mismatch)
- R2: tell=AI列举方法但未优先Artinian判据, hint=列出所有方法, level=0.7, 自由列举, topology=(characterization, direct_calculation, knowledge_gap)
- R3: tell=AI尝试直接计算内射维数陷入困境, hint=试直接计算, level=0.4, 小尝试, topology=(characterization, direct_calculation, method_problem_mismatch)
- R4: tell=AI未分析环的具体结构, hint=分析环关系和维数, level=0.5, 思维操作引导, topology=(characterization, direct_manipulation, structural_transformation)
- R5: tell=AI知道是Artinian但未算socle, hint=计算socle, level=0.4, 推进, topology=(characterization, direct_calculation, method_translation)
- R6: tell=AI算了socle但不知道Artinian判据, hint=回忆Artinian-Gorenstein判据, level=0.5, 思维操作引导, topology=(characterization, direct_calculation, knowledge_gap), is_knowledge_bottleneck=true
- R7: tell=AI有所有部件但需组装, hint=组装最终论证, level=0.3, 能量传递引导, topology=(characterization, logical_deduction, method_translation)

**全局pairs概要**：
- G1 (path_feature): tell=从抽象内射维数定义到具体socle计算的翻译路径, hint=识别Artinian结构后用socle判据, level=0.6
- G2 (implicit, R4): tell=关系X²=Y²=Z²=t结合XY=0迫使tY=0的推导链, hint=追踪关系后果找幂零元, level=0.5

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会尝试从Gorenstein的定义（内射维数有限）直接出发，试图构造内射分解或使用一般性同调代数工具，不识别环的Artinian结构，因此无法将问题转化为可计算的socle维数问题。可能在抽象同调代数中迷失。
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "method_translation_poc"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [ ] _key（=problem_id）
- [ ] source_id
- [ ] source_dataset
- [ ] schema_version（=3）
- [ ] problem_text
- [ ] solution_text
- [ ] solution_summary
- [ ] domain
- [ ] subfield
- [ ] answer_type
- [ ] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
- [ ] problem_type
- [ ] solution_method_type
- [ ] structure_features
- [ ] key_objects
- [ ] thinking_patterns
- [ ] primary_pattern
- [ ] knowledge_required
- [ ] key_insight
- [ ] translation_from
- [ ] translation_to
- [ ] translation_type
- [ ] tell_topology（profile级）
- [ ] tell_small_concepts（profile级）
- [ ] expected_ai_method
- [ ] correct_method
- [ ] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [ ] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [ ] bare_ai_expected
- [ ] bare_ai_error_prediction
- [ ] suitable_for_poc
- [ ] discriminates_levels
- [ ] qa_sequence（含rounds数组和stats子对象）
- [ ] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000302
- solution_method_type: structural_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有分类体系覆盖本题
- 是否遇到异常: 否

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
