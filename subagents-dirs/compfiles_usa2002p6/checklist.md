# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2002p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2002P6.lean
- **来源**: USA 2002 P6
- **ArangoDB progress记录_key**: 329410（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2002P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：n×n邮票纸，每次撕出同一行或同一列中3个相邻邮票组成的块。b(n)是最小的块数，使得撕出这些块后无法再撕出任何块（极大撕裂中的最小块数）。证明存在实常数c,d使得(1/7)n²-cn ≤ b(n) ≤ (1/5)n²-dn对所有n>0成立。
- 解答核心思路（1-2句话）：下界用双重计数——2n(n-2)个可能位置每个必须被某个已撕出的块相交，每个块最多相交14个位置，得b(n)≥n(n-2)/7。上界构造周期5的相位偏移模式——行i的块从列i mod 5开始每隔5列放一个水平块，相位偏移保证竖直方向也被阻挡，密度1/5。
- 解答关键步骤列表：
  1. 定义b(n)为极大撕裂的最小块数（Nat.find）
  2. 下界：计算所有可能位置数=2n(n-2)（水平n(n-2)+竖直n(n-2)）
  3. 下界：证明每个撕出的块最多与14个位置相交（5同向+9交叉）
  4. 下界：双重计数(位置,块)对，得2n(n-2)≤14|T|，即b(n)≥n(n-2)/7
  5. 上界（小n≤5）：用trivialTearing（全竖直+底部水平），密度≤1/3但小n时足够
  6. 上界（大n≥6）：构造patTearing——行i用phase=i%5，块从列phase开始每隔5列
  7. 上界：验证极大性——水平方向周期5保证每3连续格有覆盖；竖直方向3连续行phase覆盖3个不同mod5值，任意列至少1行被覆盖
  8. 上界：计数每行≤n/5+3块，总计≤n(n/5+3)≈n²/5
  9. 取c=2/7, d=-3合并上下界

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 这个题目在问什么？b(n)的定义中，"最小"和"不可能再撕"这两个条件分别意味着什么？我们要证明什么类型的结论？ | b(n)是极大撕裂中的最小块数——极大性要求不能再撕出任何块，最小性要求在所有极大方案中块数最少。我们要证明b(n)被n²/7和n²/5渐近夹住，即存在常数c,d使得(1/7)n²-cn≤b(n)≤(1/5)n²-dn。这是一个双侧渐近界的证明。 |
| 2 | 自由列举 | 0.4 | 要同时证明上界和下界，你能想到哪些方法？分别列出适用于下界和上界的方法。 | 下界：每个撕出的块"阻挡"了一些可能位置，可以用计数论证；或者分析极大撕裂的结构性质。上界：构造一个具体的极大方案并计算其块数；或者用概率方法证明存在性。两个方向可能需要完全不同的技巧。 |
| 3 | 小尝试 | 0.3 | 对于上界，试试最简单的构造——全部用竖直块填满，密度是多少？这个密度够不够？ | 全竖直块：每列n/3个块，n列共n²/3个块。密度1/3，但1/3>1/5，不够好。需要更高效的方案。问题在于竖直块只阻挡同列的位置，没有利用交叉阻挡。 |
| 4 | 思维操作引导 | 0.5 | 对于下界，考虑所有可能的位置（水平的和竖直的），每个位置必须被某个已撕出的块"阻挡"（相交）。用双重计数：计算(位置,块)对，其中位置和块相交。每个块最多阻挡多少个位置？ | 水平位置有n(n-2)个，竖直位置有n(n-2)个，共2n(n-2)个。每个撕出的块（比如水平块在(i,j)到(i,j+2)）与同行的5个水平位置相交（起始列j-2到j+2），与3列×3行的9个竖直位置相交（列j,j+1,j+2，起始行i-2到i），共14个。所以2n(n-2)≤14|T|，即|T|≥n(n-2)/7。 |
| 5 | 推进 | 0.6 | 验证"14"这个界——一个水平块在(i,j)到(i,j+2)，它最多与多少个水平位置相交？多少个竖直位置相交？竖直块的情况对称吗？ | 水平位置：同行，起始列在j-2到j+2之间，共5个。竖直位置：列在{j,j+1,j+2}中，起始行在i-2到i之间，共3×3=9个。总计5+9=14个。竖直块由对称性也是14个（5个竖直+9个水平）。 |
| 6 | 思维操作引导 | 0.7 | 对于上界，需要密度1/5的构造。考虑每行只用水平块，块覆盖3格间隔2格（周期5）。但如何保证竖直方向也被阻挡？试试让每行的起始位置偏移1个单位（phase=i mod 5）。为什么周期必须是5而不是3？ | 行i的块从列i%5开始，每隔5列一个。每行约n/5个块。关键：phase每行偏移1，所以任意3连续行的phase覆盖3个不同mod5值。每个phase覆盖3个mod5值（phase,phase+1,phase+2），3个连续phase覆盖所有5个mod5值——任意列在3行中至少1行被覆盖，竖直块被阻挡。周期必须是5因为3格块+2格间隔=5，周期3会留下3格空隙让竖直块通过。 |
| 7 | 能量传递引导 | 0.8 | 验证这个周期5的构造是极大的，并计算总块数，完成证明。 | 极大性：水平方向每3连续格至少1个被覆盖（周期5中3被覆盖2空）；竖直方向任意3连续行×任意列，3个phase覆盖所有5个mod5值，至少1个被覆盖。总块数≤n(n/5+3)≈n²/5。结合下界n(n-2)/7≈n²/7，取c=2/7,d=-3得(1/7)n²-(2/7)n≤b(n)≤(1/5)n²+3n。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 双侧渐近界证明——下界用双重计数（每个位置必须被阻挡，每个块最多阻挡14个位置），上界用显式构造（周期5相位偏移模式）。核心结构是"极大撕裂的最小化"问题，需要分别证明下界和上界，两个方向使用完全不同的技巧。
- key_objects: ["n×n邮票网格", "1×3/3×1块（水平/竖直三连格）", "极大撕裂（maximal tearing）", "b(n)（最小极大撕裂块数）", "可能位置集合（2n(n-2)个）", "双重计数对(位置,块)", "周期5相位偏移模式", "phase=i mod 5"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["double_counting", "periodic_construction", "orientation_decomposition", "phase_shifted_pattern", "asymptotic_analysis", "two_technique_split"]
- primary_pattern: double_counting_with_periodic_construction（下界双重计数+上界周期构造的双技巧模式）
- knowledge_required: ["双重计数（double counting）", "极大匹配概念", "网格组合学", "周期模式构造", "渐近密度分析", "mod运算与相位偏移"]
- key_insight: 下界的关键是"14"界——每个块按方向分解最多相交5个同向+9个交叉位置；上界的关键是周期5的相位偏移——phase=i mod 5保证3连续行覆盖所有5个mod5值，同时阻挡水平和竖直块。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_structural_analysis（直接分析极大撕裂的结构性质，或用朴素构造如全竖直块）
- translation_to: double_counting_plus_periodic_construction（下界翻译为双重计数+方向分解，上界翻译为周期5相位偏移构造）
- translation_type: method_translation（从直接推理/朴素构造翻译到双重计数+周期构造的组合方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch}
- tell_small_concepts: ["double_counting", "14_bound", "orientation_decomposition", "period_5_pattern", "phase_shift", "maximal_tearing", "two_technique_split", "asymptotic_density", "position_block_intersection"]
- expected_ai_method: bare AI会尝试直接分析极大撕裂的结构或用朴素构造（如全竖直块密度1/3），不会想到双重计数的"14"界和周期5相位偏移构造
- correct_method: 下界用双重计数（2n(n-2)位置÷14=每块最多阻挡14个位置），上界用周期5相位偏移模式（phase=i mod 5，密度1/5）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=inequality_proof, ai_method_type=direct_calculation, gap_type=method_problem_mismatch都能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [ ] 不需要进化建议

**拓扑进化建议**（如有）：无。已有拓扑分类足够覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs详见profile.json**

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接分析极大撕裂的结构或用单一技巧处理双侧界。下界方面，AI不会想到双重计数的"14"界——按方向分解相交位置（5同向+9交叉）是非显然的组合洞察。上界方面，AI会尝试朴素构造（如全竖直块密度1/3或周期3模式），但不会想到周期5+相位偏移的构造——关键在于理解周期必须为5（3格块+2格间隔）且相位偏移保证竖直极大性。
- suitable_for_poc: ["POC-VMS-tell-detection", "POC-VMS-hint-injection", "POC-VMS-method-translation"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**完整JSON已写入** `subagents-dirs/compfiles_usa2002p6/profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 3 global pairs, answer非None, knowledge_bottleneck="R4", thinking_bottleneck="R6", per-pair拓扑存在, global pair的why_not_visible_locally非None

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2002p6
- solution_method_type: double_counting_lower_bound_with_periodic_construction_upper_bound
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（1个path_feature型 + 2个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（inequality_proof / direct_calculation / method_problem_mismatch等）足够覆盖
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
