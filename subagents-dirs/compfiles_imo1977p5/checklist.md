# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1977p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1977P5.lean
- **来源**: IMO 1977 P5
- **ArangoDB progress记录_key**: 329084（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1977P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设a,b为自然数。a²+b²除以a+b得余数r和商q。求所有使q²+r=1977的(a,b)对。
- 解答核心思路（1-2句话）：利用除法恒等式a²+b²=q(a+b)+r与约束q²+r=1977消去r，界定q=44,r=41，配方得(a-22)²+(b-22)²=1009，利用1009=15²+28²（素数≡1 mod 4的唯一二平方和表示）求解。
- 解答关键步骤列表：
  1. 由q²+r=1977得r=1977-q²
  2. 由除法恒等式a²+b²=q(a+b)+r消去r
  3. 界定q≤44（因q²≤1977）
  4. 利用(a+b)²≤2(a²+b²)和r<a+b证明q>43，故q=44,r=41
  5. 代入得a²+b²=44(a+b)+41
  6. 配方：(a-22)²+(b-22)²=1009
  7. 1009是素数且≡1(mod 4)，唯一表示为15²+28²
  8. |a-22|,|b-22|∈{15,28}，得四组解(7,50),(37,50),(50,7),(50,37)

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**每轮必须标注**：
- **question**：给AI的提示/问题（Q）
- **expected_answer**：预期回复（A）
- **situation_type**：**⚠️ 只能取以下6个值之一，禁止自创**：
  - `纯元认知观察`——让AI描述题目结构、识别已知/未知
  - `自由列举`——让AI列出所有可能方向
  - `小尝试`——让AI试一个方向（可能走错的）
  - `思维操作引导`——给AI具体的思维操作指令
  - `推进`——让AI继续推进当前方向
  - `能量传递引导`——给AI信心/能量，收尾
- **level**：**⚠️ 必须是0-1之间的浮点数**（0=完全具体，1=完全抽象。禁止用1-4整数）

**QA序列设计原则**：
1. 第1轮通常是`纯元认知观察`——让AI描述题目结构
2. 第2轮通常是`自由列举`——让AI列出所有可能方向
3. 第3轮通常是`小尝试`——让AI试一个可能走错的方向
4. 中间几轮根据情况用`思维操作引导`或`推进`
5. 最后一轮通常是`能量传递引导`——收尾

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：有哪些已知量、哪些未知量？它们之间通过什么关系连接？ | 已知：a,b∈ℕ；a²+b²除以a+b得商q余r；约束q²+r=1977。未知：所有(a,b)对。连接关系：除法恒等式a²+b²=q(a+b)+r将(a,b)与(q,r)绑定，再通过q²+r=1977约束。本质是两个方程（除法恒等式+约束）四个未知数(a,b,q,r)的系统。 |
| 2 | 自由列举 | 0.7 | 列出你能想到的所有可能解题方向，不用判断哪个最好。 | ①直接枚举(a,b)对检查q²+r=1977；②固定q求r再反推(a,b)；③消去r用q²+r=1977代入除法恒等式；④利用不等式界定q的范围；⑤配方/代数变形；⑥数论工具（整除性、模运算）；⑨利用a²+b²的结构性质。 |
| 3 | 小尝试 | 0.4 | 试试方向①：直接枚举(a,b)对。这个方向可行吗？ | 不可行。a,b是任意自然数，搜索空间无限。即使有界估计，a+b可能很大，枚举量巨大。需要先通过约束缩小范围。 |
| 4 | 思维操作引导 | 0.5 | 执行方向③：用r=1977-q²代入除法恒等式a²+b²=q(a+b)+r，消去r后得到什么？ | 代入得a²+b²=q(a+b)+(1977-q²)=q(a+b)-q²+1977。整理得a²+b²-q(a+b)+q²=1977。这是一个关于(a,b,q)的方程，r被消去了。现在只需处理三个未知数。 |
| 5 | 推进 | 0.4 | 继续推进：从q²≤1977能得到q的上界。再利用r=1977-q²≥0和r<a+b，结合(a+b)²≤2(a²+b²)，能否把q锁定到一个值？ | q²≤1977→q≤44。若q≤43，则r=1977-q²≥1977-1849=128。又r<a+b且a²+b²=q(a+b)+r≤44(a+b)+(a+b)=45(a+b)，故(a+b)²≤2·45(a+b)→a+b<90，于是r<90。但r≥128>90矛盾。故q>43，结合q≤44得q=44，r=41。 |
| 6 | 思维操作引导 | 0.5 | 现在q=44,r=41，方程变为a²+b²=44(a+b)+41。执行配方操作：把a和b的二次项配成完全平方。 | a²-44a+b²-44b=41→(a-22)²+(b-22)²=41+22²+22²=41+484+484=1009。所以(a-22)²+(b-22)²=1009。问题转化为：把1009表示为两个完全平方数之和。 |
| 7 | 能量传递引导 | 0.6 | 你已经把问题转化成了"将1009表示为两个平方数之和"。这是一个经典数论问题！1009是素数且≡1(mod 4)，费马定理保证它可以唯一表示为两个平方数之和。找到这个表示，你就完成了！ | 1009=15²+28²=225+784=1009。由素数≡1(mod 4)的二平方和唯一性，|a-22|和|b-22|只能是{15,28}的排列。故(a,b)∈{(7,50),(37,50),(50,7),(50,37)}。验证：如a-22=15→a=37, b-22=28→b=50。四组解全部验证通过。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R5,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R6）
- level_sum: 0.8+0.7+0.4+0.5+0.4+0.5+0.6 = 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R7（需要知道费马二平方和定理：素数p≡1(mod 4)可唯一表示为两个平方数之和）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6（配方操作——将a²+b²=44(a+b)+41识别为可配方的二次型是关键转折点）

---

## Step 3: 标注问题拓扑层 [x]

**操作**：从题目结构中提取

**要求**：
- `problem_type`：问题类型大概念。**优先使用已有值**（见下方拓扑分类体系），如需新建确保粒度一致
- `structure_features`：题目结构特征描述
- `key_objects`：核心数学对象列表

**已有problem_type值**（优先使用）：
- `structural_existence` ✅ 抽象
- `discrete_combinatorial` ✅ 抽象
- `trigonometric_identity` ✅ 中等
- `constraint_satisfaction` ✅ 中等
- `characterization` ✅ 抽象
- `inequality_proof` ✅ 中等
- `absolute_value_system` ⚠️ 偏具体
- `functional_equation_periodicity` ⚠️ 偏具体
- **❌ 不要用太具体的值**（如`word_problem_with_diophantine_constraint`是错误粒度）

**产出**：
- problem_type: constraint_satisfaction
- structure_features: 两个方程（除法恒等式+二次约束）约束四个未知数(a,b,q,r)，需消元降维后配方转化为数论表示问题。核心结构是"除法带余→二次约束→配方→二平方和表示"的转化链。
- key_objects: 自然数对(a,b)、商q、余数r、除法恒等式a²+b²=q(a+b)+r、二次约束q²+r=1977、完全平方(a-22)²+(b-22)²=1009、素数1009的二平方和表示

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [消元降维, 不等式界定, 配方转化, 数论定理应用, 穷举排除]
- primary_pattern: 配方转化（将代数约束通过配方转化为数论表示问题，是整道题的关键转折）
- knowledge_required: [带余除法恒等式, 二次不等式放缩, 完全平方配方, 费马二平方和定理（素数p≡1 mod 4可唯一表示为两平方数之和）]
- key_insight: 将a²+b²=44(a+b)+41配方为(a-22)²+(b-22)²=1009，把约束满足问题转化为经典的二平方和表示问题

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 代数约束满足（a²+b²=44(a+b)+41，在自然数中求(a,b)）
- translation_to: 数论表示问题（将1009表示为两个完全平方数之和）
- translation_type: structural_transformation（通过配方操作将代数方程的结构从"交叉项形式"变换为"距离平方和形式"，改变了问题的数学性质）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: [消元, 配方, 二平方和, 素数表示, 不等式界定, 商余恒等式]
- expected_ai_method: bare AI会尝试直接枚举(a,b)对或逐个尝试q值，不意识到需要配方转化
- correct_method: 消元→不等式界定q=44→配方→费马二平方和定理

**已有ai_method_type值**（优先使用）：
- `enumeration_brute_force` ✅ 抽象
- `continuous_analytic` ✅ 抽象
- `direct_calculation` ✅ 抽象
- `logical_deduction` ✅ 抽象
- `case_by_case` ✅ 抽象
- `algebraic_identity` ✅ 中等
- `equation_solving` ✅ 抽象
- `direct_manipulation` ✅ 抽象
- **❌ 不要用太长太具体的值**

**已有gap_type值**（优先使用）：
- `method_problem_mismatch` ✅ 抽象
- `knowledge_gap` ✅ 抽象
- `structural_transformation` ✅ 中等
- `search_space_estimation` ✅ 中等
- `method_translation` ✅ 中等
- `global_sorting` ⚠️ 偏具体
- **❌ 不要用太具体的值**

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。constraint_satisfaction + enumeration_brute_force + structural_transformation 均为已有值，且准确描述了这道题的tell：AI想枚举但问题需要配方转化。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。三个维度都是中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的tell核心是"枚举→配方转化"的gap，structural_transformation准确捕捉了这一点。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。已有拓扑分类完全够用。

**拓扑进化建议**（如有）：无。已有拓扑分类体系完全覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到方程系统但未识别转化路径，倾向于直接求解 | 观察题目结构：识别已知/未知和连接关系 | 0.8 | 纯元认知观察 | false | {constraint_satisfaction, direct_calculation, method_problem_mismatch} | [方程系统, 已知未知, 除法恒等式] |
| 2 | AI列出方向时枚举排在首位，未优先考虑代数变形 | 列出所有可能方向 | 0.7 | 自由列举 | false | {constraint_satisfaction, enumeration_brute_force, search_space_estimation} | [枚举, 消元, 不等式, 配方] |
| 3 | AI尝试枚举(a,b)对，搜索空间无限 | 试试枚举方向，评估可行性 | 0.4 | 小尝试 | false | {constraint_satisfaction, enumeration_brute_force, method_problem_mismatch} | [枚举失败, 搜索空间, 无限] |
| 4 | AI未意识到可用r=1977-q²消元降维 | 执行消元：用r=1977-q²代入除法恒等式 | 0.5 | 思维操作引导 | false | {constraint_satisfaction, algebraic_identity, method_translation} | [消元, 代入, 降维, 商余恒等式] |
| 5 | AI消元后未利用不等式界定q的范围 | 利用q²≤1977和r<a+b界定q | 0.4 | 推进 | false | {constraint_satisfaction, logical_deduction, knowledge_gap} | [不等式界定, 上界, 矛盾法, 放缩] |
| 6 | AI得到q=44后未识别a²+b²=44(a+b)+41可配方 | 执行配方操作：配成完全平方 | 0.5 | 思维操作引导 | false | {constraint_satisfaction, algebraic_identity, structural_transformation} | [配方, 完全平方, 二次型, 转化] |
| 7 | AI配方后得1009但不知费马二平方和定理 | 1009是素数≡1(mod 4)，费马定理保证唯一二平方和表示 | 0.6 | 能量传递引导 | true | {constraint_satisfaction, direct_calculation, knowledge_gap} | [费马定理, 素数, mod 4, 二平方和, 唯一表示] |

**全局pairs详情**：

| scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|
| path_feature | 整个解题路径的转化链：消元→界定→配方→数论定理 | null | 问题的核心不在于枚举或直接计算，而在于通过配方将代数约束转化为数论表示问题 | 识别二次型a²+b²=44(a+b)+41可配方为(a-22)²+(b-22)²=1009，转化问题类型 | 0.7 | high——"配方转化"模式适用于所有形如x²+y²=k(x+y)+c的约束 | N/A（path_feature型） | {constraint_satisfaction, enumeration_brute_force, structural_transformation} | [配方, 转化链, 二平方和, 枚举失败] |
| implicit | R7的知识瓶颈——费马二平方和定理 | R7 | 配方后得到1009，需要知道1009是素数且≡1(mod 4)才能应用唯一表示定理 | 1009是素数且≡1(mod 4)，由费马定理可唯一表示为两个平方数之和 | 0.6 | medium——费马二平方和定理适用于所有素数p≡1(mod 4)的二平方和分解 | 从配方结果(a-22)²+(b-22)²=1009无法直接看出1009的素数性质和二平方和表示，需要外部数论知识 | {constraint_satisfaction, direct_calculation, knowledge_gap} | [费马定理, 素数, mod 4, 二平方和, 唯一表示] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接枚举(a,b)对或逐q值搜索，不识别配方的关键转折。即使消元成功，也难以同时完成不等式界定q=44和配方转化两步。最终在1009的二平方和表示处遇到知识瓶颈（费马定理）。最可能停留在枚举或部分消元阶段。
- suitable_for_poc: ["hint_injection_poc——配方转化的hint注入", "tell_detection_poc——识别AI在枚举vs配方之间的分叉信号", "knowledge_bottleneck_poc——费马二平方和定理的知识瓶颈检测"]
- discriminates_levels: true（此题需要消元+不等式界定+配方+数论定理四步组合，能有效区分AI的推理深度和知识广度）

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [x] _key（=problem_id）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer
- [x] problem_type
- [x] solution_method_type
- [x] structure_features
- [x] key_objects
- [x] thinking_patterns
- [x] primary_pattern
- [x] knowledge_required
- [x] key_insight
- [x] translation_from
- [x] translation_to
- [x] translation_type
- [x] tell_topology（profile级）
- [x] tell_small_concepts（profile级）
- [x] expected_ai_method
- [x] correct_method
- [x] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 `subagents-dirs/compfiles_imo1977p5/profile.json`

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: compfiles_imo1977p5, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1977p5
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature + 1个implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。已有拓扑分类（constraint_satisfaction / enumeration_brute_force / structural_transformation等）完全覆盖本题。
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
