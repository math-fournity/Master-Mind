# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2008p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2008P6.lean
- **来源**: USA 2008 P6
- **ArangoDB progress记录_key**: 329434（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2008P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：在一个数学会议上，每对数学家要么是朋友要么是陌生人。用餐时每位参与者选择两个餐厅之一。每位数学家坚持要在包含偶数个其朋友的餐厅用餐。证明：将数学家分配到两个餐厅的方式数是2的幂（即形如2^k，k为正整数）。
- 解答核心思路（1-2句话）：将餐厅分配建模为ZMod 2上的向量x，"同房间朋友数为偶数"的条件转化为图Laplacian的线性方程lap G x = degVec G，解集是ker(lap G)的陪集，故大小为2^finrank(ker(lap G))。存在性通过Laplacian的对称性+关键恒等式x^T L x = Σ deg(v)x(v)（交叉项因每条边被计两次而消去）证明degVec在range中。
- 解答关键步骤列表：
  1. 将分配建模为x: Fin n → ZMod 2，餐厅0和1
  2. 定义图Laplacian lap G: (lap G x) v = deg(v)*x v + Σ_{u~v} x u（在ZMod 2上）
  3. 证明"同房间朋友数为偶数"等价于线性方程 lap G x v = deg(v) (mod 2)
  4. 证明Laplacian对称：Σ lap G x v * y v = Σ x v * lap G y v（交换求和顺序）
  5. 关键恒等式：Σ x v * lap G x v = Σ deg(v) * x v（交叉项Σ_{v}Σ_{u~v} x v * x u = 0，因为每条边(u,v)贡献x_u*x_v + x_v*x_u = 0 in ZMod 2）
  6. 定义Tmap（kernel上的泛函），证明range(lap G) = ker(Tmap)（对称矩阵的range = kernel的正交补）
  7. degVec ∈ ker(Tmap)（由关键恒等式），故degVec ∈ range(lap G)，即存在解x0
  8. 解集 = x0 + ker(lap G)，是ker的陪集，大小 = 2^finrank(ker(lap G)) = 2^k

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 请描述这道题的结构：已知条件是什么？要证明的结论是什么？这道题属于什么数学领域？ | 已知：一个完全图（朋友/陌生人关系），n个数学家分到2个餐厅，每人要求同房间朋友数为偶数。要证：满足条件的分配方式数是2的幂。这属于组合学/图论问题，涉及计数和奇偶性。 |
| 2 | 自由列举 | 0.4 | 列出所有你可能用来攻击这道题的数学工具和方法方向，不要筛选。 | 可能方向：1) 直接组合计数 2) 归纳法 3) 生成函数 4) 线性代数（矩阵/向量空间） 5) 图论（Laplacian/邻接矩阵） 6) 模2算术 7) 对称性论证 8) 容斥原理 |
| 3 | 小尝试 | 0.3 | 试试用直接组合计数或归纳法来分析：对于小规模图（如3-4个顶点），满足条件的分配有多少种？能发现什么规律？ | 小规模尝试：对于无边的图，所有2^n种分配都满足（每人0个朋友同房间，0是偶数），结果是2^n。对于完全图K_n，每人需同房间朋友数为偶数，即同房间人数-1为偶数，所以同房间人数为奇数。这暗示结果总是2的幂，但归纳法难以处理一般图结构。直接计数对一般图太复杂。 |
| 4 | 思维操作引导 | 0.6 | 关键思维操作：将"偶数"这个条件翻译到模2的语言中。考虑用ZMod 2（即F_2）上的向量来编码分配，用线性代数来处理。具体地：令x: Fin n → ZMod 2表示分配（0=餐厅A, 1=餐厅B），"同房间朋友数为偶数"这个条件在F_2上会变成什么？ | 在F_2上，"同房间"意味着x_u = x_v，即x_u + x_v = 0。"同房间朋友数"= Σ_{u~v} [x_u = x_v] = Σ_{u~v} (1 + x_u + x_v) (mod 2)。"为偶数"即这个和在F_2上为0，即 deg(v) + Σ_{u~v} x_u + deg(v)*x_v = 0，即 deg(v)*x_v + Σ_{u~v} x_u = deg(v) (mod 2)。这恰好是图Laplacian L作用于x的方程：(Lx)_v = deg(v)。 |
| 5 | 推进 | 0.5 | 继续推进：现在条件变成了线性方程组 Lx = d（d是度数向量），在F_2上。这个方程组的解集有什么结构？如果解集非空，它的基数是多少？ | 解集是ker(L)的陪集（如果非空）。因为Lx = d的解集 = {x0 + z : z ∈ ker(L)}，其中x0是任一特解。ker(L)是F_2上的向量空间，维数设为r，则|ker(L)| = 2^r。陪集大小等于ker(L)大小，所以解集大小 = 2^r = 2^k，其中k = finrank(ker(L))。这直接给出"2的幂"的结论。 |
| 6 | 思维操作引导 | 0.7 | 还差一步：需要证明解集非空，即Lx = d有解。思维操作：利用L是对称矩阵这一性质。在F_2上，对称矩阵的range等于其kernel的正交补。尝试证明d（度数向量）正交于ker(L)，即对任意y ∈ ker(L)，Σ d_v * y_v = 0。考虑计算Σ y_v * (Ly)_v，利用y ∈ ker(L)意味着Ly = 0。 | 关键恒等式：Σ_v y_v * (Ly)_v = Σ_v deg(v)*y_v + Σ_v Σ_{u~v} y_v*y_u。交叉项Σ_v Σ_{u~v} y_v*y_u中每条边(u,v)被计两次（y_v*y_u + y_u*y_v = 2*y_u*y_v = 0 in F_2），所以交叉项=0。因此Σ y_v*(Ly)_v = Σ deg(v)*y_v。当y ∈ ker(L)时Ly=0，左边=0，所以Σ deg(v)*y_v = 0，即d正交于ker(L)。由L对称性，range(L) = ker(L)^⊥，故d ∈ range(L)，方程Lx=d有解。 |
| 7 | 能量传递引导 | 0.3 | 现在把所有部分组装起来：存在性已证，解集是ker(L)的陪集，大小为2^finrank(ker(L))。请写出完整的证明结论。 | 完整证明：1) 将分配编码为x ∈ F_2^n，条件等价于Lx = d（L是图Laplacian，d是度数向量mod 2）。2) L对称，关键恒等式x^T Lx = d^T x（交叉项因每边计两次而消去）证明d ∈ ker(L)^⊥ = range(L)，故解存在。3) 解集 = x0 + ker(L)是陪集，大小 = |ker(L)| = 2^finrank(ker(L)) = 2^k。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1,R2,R5,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R6）
- level_sum: 0.2+0.4+0.3+0.6+0.5+0.7+0.3 = 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**操作**：从题目结构中提取

**产出**：
- problem_type: `structural_existence`
- structure_features: 图论计数问题，奇偶性约束（同房间朋友数为偶数），通过翻译到F_2上的线性代数来揭示解集的向量空间陪集结构，从而得出计数结果为2的幂。核心结构是"组合条件→线性方程组→陪集→2的幂"的翻译链。
- key_objects: 友谊图G（SimpleGraph），房间分配向量x ∈ F_2^n，图Laplacian L（ZMod 2上的线性映射），度数向量d（mod 2），ker(L)（Laplacian的核），解集（ker(L)的陪集）

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["组合-代数翻译", "结构识别（陪集结构）", "对称性利用", "代数恒等式（交叉项消去）", "存在性通过正交性论证"]
- primary_pattern: 组合-代数翻译（将组合计数问题翻译为F_2上的线性代数问题，揭示解集的向量空间陪集结构）
- knowledge_required: ["图论：Laplacian矩阵、邻接关系、度数", "有限域上的线性代数：F_2向量空间、核、陪集、秩", "对称矩阵性质：range = kernel的正交补", "模2算术：ZMod 2上的运算", "线性方程组解的结构：解集=特解+核"]
- key_insight: "偶数个同房间朋友"这个组合条件在F_2上恰好是图Laplacian的线性方程Lx=d，解集是ker(L)的陪集，大小自动为2的幂——关键转折是将奇偶性条件翻译为线性代数语言。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 组合/图论语言（朋友关系图、餐厅分配、奇偶性约束"同房间朋友数为偶数"）
- translation_to: F_2上的线性代数语言（分配向量x ∈ F_2^n、图Laplacian线性映射L、度数向量d、线性方程Lx=d、核与陪集结构、正交补）
- translation_type: domain_translation（跨领域翻译：组合计数→有限域线性代数，通过将奇偶条件编码为模2线性方程实现）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: ["偶数条件", "模2编码", "图Laplacian", "线性方程组", "核与陪集", "对称矩阵", "正交补", "交叉项消去", "2的幂"]
- expected_ai_method: bare AI会尝试直接组合计数或对顶点数归纳，试图找到递推关系或模式，但无法处理一般图结构。可能尝试分类讨论图的类型，但不会想到将奇偶条件翻译为F_2上的线性方程。
- correct_method: 将奇偶条件翻译为F_2上图Laplacian的线性方程Lx=d，识别解集为ker(L)的陪集（大小=2^finrank(ker(L))），利用L的对称性和关键恒等式x^T Lx = d^T x（交叉项模2消去）证明存在性。

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。structural_existence（证明解集有向量空间陪集结构）、enumeration_brute_force（bare AI会尝试直接计数）、method_translation（需要从组合翻译到线性代数）都归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个维度的值都是中等抽象粒度，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心tell是"组合条件可以翻译为线性代数"，method_translation准确捕捉了这个gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类完全适用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对图论计数问题，尚未识别问题结构，处于初始状态 | 描述题目结构，识别已知/未知/所属领域 | 0.2 | 纯元认知观察 | false | {structural_existence, enumeration_brute_force, method_problem_mismatch} | ["图论计数", "奇偶约束", "2的幂"] |
| 2 | AI列出了多种方法但无优先级，不知道哪个方向正确 | 列出所有可能方向，不筛选 | 0.4 | 自由列举 | false | {structural_existence, enumeration_brute_force, method_translation} | ["方法列举", "线性代数", "模2算术", "图Laplacian"] |
| 3 | AI尝试直接计数/归纳，小规模发现2的幂模式但无法推广到一般图 | 试直接计数/归纳方向（可能走错） | 0.3 | 小尝试 | false | {structural_existence, enumeration_brute_force, method_problem_mismatch} | ["直接计数", "归纳法", "小规模验证", "一般图困难"] |
| 4 | AI卡在组合方法上，需要关键翻译操作——将偶数条件翻译到F_2 | 将"偶数"翻译到模2语言，用F_2向量编码分配 | 0.6 | 思维操作引导 | true | {structural_existence, enumeration_brute_force, knowledge_gap} | ["模2编码", "F_2向量", "图Laplacian", "线性方程"] |
| 5 | AI已建立线性方程Lx=d，需要识别解集的陪集结构 | 分析线性方程组解集的结构和基数 | 0.5 | 推进 | false | {structural_existence, equation_solving, structural_transformation} | ["线性方程组", "核与陪集", "向量空间维数", "2的幂"] |
| 6 | AI需证明解集非空，需利用L对称性和关键恒等式——最难思维步骤 | 利用L对称性，证明d正交于ker(L)，用关键恒等式 | 0.7 | 思维操作引导 | false | {structural_existence, algebraic_identity, method_translation} | ["对称矩阵", "正交补", "交叉项消去", "关键恒等式", "存在性证明"] |
| 7 | AI已掌握所有部分，需组装完整证明 | 组装所有部分，写出完整证明结论 | 0.3 | 能量传递引导 | false | {structural_existence, logical_deduction, method_translation} | ["完整证明", "陪集结构", "2的幂", "存在性+计数"] |

**全局pairs详情**：

**Global pair 1 (path_feature)**:
- scope_type: "path_feature"
- scope: "整个证明路径：从组合条件到F_2线性代数翻译到陪集结构到存在性证明"
- observation_point: null
- tell: 完整路径特征是"组合条件→F_2线性方程→陪集结构→2的幂"，这个翻译链在局部视角中不可见
- hint: 识别核心是跨领域翻译——将组合计数翻译为有限域线性代数，解集的向量空间结构自动给出2的幂
- hint_level: 0.7
- generalizability: "high - 任何涉及奇偶性约束的计数问题都可以尝试翻译到F_2上的线性代数"
- why_not_visible_locally: "在局部视角中，AI看到的是'描述题目'、'列举方法'、'尝试计数'、'翻译到F_2'等独立步骤。每一步的局部视角无法看到完整的翻译链——只有从全局视角才能看到'组合条件→线性方程→陪集→2的幂'这条路径是一个连贯的翻译操作。特别是R3的小尝试会让AI陷入组合计数的局部困境，看不到需要跳出组合领域。"
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: ["组合-代数翻译", "F_2线性方程", "陪集结构", "2的幂", "翻译链"]

**Global pair 2 (implicit)**:
- scope_type: "implicit"
- scope: "存在性证明中的关键恒等式：交叉项模2消去"
- observation_point: "R6"
- tell: 关键恒等式x^T Lx = d^T x中交叉项=0是因为每条边被计两次（y_v*y_u + y_u*y_v = 0 in F_2），这个图结构性质在局部步骤中不可见
- hint: 注意Laplacian对称性使每条无向边在二次型中被计两次，模2下自动消去，这是连接度数向量和Laplacian的桥梁
- hint_level: 0.8
- generalizability: "medium - 对称矩阵在F_2上的二次型性质可推广，但'每条边计两次'是图特有的结构"
- why_not_visible_locally: "在R6的局部步骤中，AI看到的是'计算Σ y_v*(Ly)_v并展开'，但'交叉项为什么消去'这个关键洞察依赖于对图结构（无向边=对称性）和模2算术（2=0）的联合理解。局部步骤只展示了代数运算，不直接揭示'每条边计两次'这个图论结构性质是消去的根本原因。"
- tell_topology: {problem_type: structural_existence, ai_method_type: algebraic_identity, gap_type: knowledge_gap}
- tell_small_concepts: ["交叉项消去", "每条边计两次", "无向图对称性", "模2消去", "二次型"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "bare AI大概率会尝试直接组合计数或归纳法，在小规模图上验证2的幂模式，但无法推广到一般图。关键错误是看不到将奇偶条件翻译为F_2线性代数的可能性——这是一个非显然的跨领域翻译。即使AI想到了线性代数，也可能不知道如何将'同房间朋友数为偶数'编码为Laplacian方程，更难以想到用对称矩阵的range=kernel正交补来证明存在性。"
- suitable_for_poc: ["tell端验证：测试系统能否从AI的thinking中识别出'卡在组合方法上'的分叉信号，并在R4位置注入F_2翻译方向", "hint端验证：测试F_2线性代数翻译方向的脉络注入能否引导AI走出组合计数困境", "知识瓶颈测试：R4是纯知识瓶颈（F_2线性代数+图Laplacian），适合测试知识注入的有效性", "思维瓶颈测试：R6是思维瓶颈（交叉项消去的洞察），适合测试思维操作引导的有效性"]
- discriminates_levels: true

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
- [x] answer（proof类型填要证明的结论）
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
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R6"为字符串类型）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 `subagents-dirs/compfiles_usa2008p6/profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: compfiles_usa2008p6, 7 local pairs, 2 global pairs, knowledge_bottleneck="R4", thinking_bottleneck="R6", answer非None, 所有global pair的why_not_visible_locally非None

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2008p6
- solution_method_type: linear_algebra_over_finite_field
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无。现有拓扑分类（structural_existence + enumeration_brute_force + method_translation）完全适用。
- 是否遇到异常: 无。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
