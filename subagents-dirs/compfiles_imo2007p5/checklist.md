# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2007p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2007P5.lean
- **来源**: IMO 2007 P5
- **ArangoDB progress记录_key**: 329202（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2007P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设a, b为正整数。证明：若4ab-1整除(4a²-1)²，则a=b。
- 解答核心思路（1-2句话）：将问题推广为n>1的一般情形（n·a·b-1 | (n·a²-1)² ⟹ a=b），用无穷递降法证明——假设a≠b则a<b或b<a，递降引理保证存在更小的正整数c满足同样的整除条件，无穷递降矛盾。
- 解答关键步骤列表：
  1. 对称引理（bad_symm）：n·a·b-1 | (n·a²-1)² 蕴含 n·b·a-1 | (n·b²-1)²，利用模运算和代数变形
  2. 递降引理（bad_exists_descent）：若a<b且n·a·b-1 | (n·a²-1)²，令t=n·a，将整除商k写成k=t·c-1的形式（通过模t分析），再证0<c<a
  3. 无穷递降原理（nat_pred_descent）：若∀k, P(k)→∃m<k, P(m)，则∀k, ¬P(k)
  4. 综合（generalized_imo2007_p5）：定义P(k)=(0<k ∧ ∃m, k<m ∧ n·k·m-1 | (n·k²-1)²)，由递降引理P(k)→∃m<k, P(m)，由无穷递降¬P(k)对所有k成立；假设a≠b则a<b或b<a，分别导出P(a)或P(b)，矛盾
  5. 特化（imo2007_p5）：取n=4应用推广定理

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：已知条件是什么形式？要证明什么？条件中的"4"和"-1"有什么结构特征？ | 已知：4ab-1 | (4a²-1)²，要证a=b。条件左边是线性形式nab-1（n=4），右边是(na²-1)²。注意到4a²-1=(2a-1)(2a+1)，而4ab-1无法简单分解。关键结构：除数和被除数都有"-1"的形式，且都含因子"4"。 |
| 2 | 自由列举 | 0.7 | 列出你可能用来处理这个"整除条件蕴含等式"问题的所有方法方向。 | 方向包括：(1)直接代数变形——展开(4a²-1)²试图因式分解；(2)模运算——对4ab-1取模分析；(3)Vieta跳跃/无穷递降——构造更小解导出矛盾；(4)推广——将4替换为一般n>1；(5)数论函数分析——分析gcd结构；(6)反证法——假设a≠b分a<b和a>b两种情况。 |
| 3 | 小尝试 | 0.4 | 试着直接展开(4a²-1)²=(16a⁴-8a²+1)，看看能否用4ab-1去除得到有用的信息。 | (16a⁴-8a²+1)/(4ab-1) = k为正整数。直接做多项式除法：16a⁴÷(4ab)≈4a³/b，余项复杂，难以直接因式分解。当b远大于a时商的结构不清晰。直接代数变形似乎走不通——需要更结构化的方法。 |
| 4 | 思维操作引导 | 0.5 | 做一个推广操作：将题目中的"4"替换为一般整数n>1，考虑命题"若nab-1 | (na²-1)²则a=b"。思考：这个推广是否使问题更容易处理？推广后条件的形式有什么新的对称性？ | 推广后形式更统一：nab-1 | (na²-1)²。关键观察：条件关于a和b有潜在对称性——如果交换a和b，条件变为nab-1 | (nb²-1)²，除数不变但被除数变了。需要证明这个对称性：nab-1 | (na²-1)² 蕴含 nab-1 | (nb²-1)²。这可以通过模运算验证。 |
| 5 | 思维操作引导 | 0.5 | 现在用无穷递降的思路：假设a≠b，不妨设a<b。能否从(nab-1) | (na²-1)²构造出一个更小的正整数c<a，使得nca-1 | (nc²-1)²？如果能，这就形成递降。 | 设k=(na²-1)²/(nab-1)为正整数。令t=na。则nab-1=tb-1，na²-1=ta-1。条件是(tb-1) | (ta-1)²，即k=(ta-1)²/(tb-1)。对t取模：ta-1≡-1(mod t)，tb-1≡-1(mod t)，所以k≡(-1)²/(-1)≡-1≡t-1(mod t)，即k=t·c-1对某个整数c成立。需要进一步证明0<c<a。 |
| 6 | 推进 | 0.3 | 继续推进：验证0<c<a。利用k=tc-1=(na)c-1和k=(ta-1)²/(tb-1)，通过大小估计来界定c的范围。 | 由k=(ta-1)²/(tb-1)和k=tc-1：tc-1=(ta-1)²/(tb-1)。因为a<b，所以ta-1<tb-1，因此k=(ta-1)²/(tb-1)<ta-1<ta，从而tc-1<ta即c<a。又因为k>0所以tc-1>0即c>0。因此0<c<a，递降成立：从(a,b)得到(c,a)满足同样的整除条件且c<a。 |
| 7 | 能量传递引导 | 0.6 | 现在把所有部分组装起来：对称性+递降+良序原理。你已经有所有零件了，完成最终证明。 | 假设a≠b，不妨设a<b。由递降引理，存在c满足0<c<a且nca-1|(nc²-1)²。定义P(k)=∃m>k使nkm-1|(nk²-1)²，则P(a)成立且P(a)→∃c<a使P(c)，由良序原理无穷递降矛盾。对称性处理b<a的情形。因此a=b。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.4+0.5+0.5+0.3+0.6 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

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
- problem_type: characterization（刻画满足整除条件的解——只有a=b）
- structure_features: 整除条件nab-1 | (na²-1)²在形式上关于a,b不对称（a平方、b线性），但结论a=b对称；常数4可推广为任意n>1；证明核心是无穷递降——从(a,b)构造更小的(c,a)满足同样条件
- key_objects: 正整数a,b；整除关系nab-1 | (na²-1)²；商k=(na²-1)²/(nab-1)；递降参数c；模参数t=na

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["推广化归（将4推广为n>1）", "对称性利用（整除条件关于a,b的对称性）", "无穷递降（构造更小解导出矛盾）", "模运算提取结构（对t=na取模提取商k的形式k=tc-1）", "大小估计（通过不等式界定递降参数c的范围）", "反证法（假设a≠b分两种情况）"]
- primary_pattern: 无穷递降（infinite descent）
- knowledge_required: ["整除与模运算基本性质", "无穷递降原理/良序原理", "Vieta跳跃技巧", "不等式估计"]
- key_insight: 对t=na取模发现商k≡-1(mod t)，即k=tc-1，从而从(a,b)的整除条件中提取出更小的c<a满足同样的整除条件，形成无穷递降

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接整除/代数变形（在原始形式4ab-1 | (4a²-1)²上做多项式运算）
- translation_to: 模运算+无穷递降（对t=na取模提取商的结构，转化为递降问题）
- translation_type: method_translation（从直接计算方法翻译到结构化数论方法——模运算提取结构+递降框架）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["整除条件", "模运算提取商结构", "无穷递降", "对称性", "推广n>1", "递降参数c", "良序原理"]
- expected_ai_method: bare AI会在原始形式4ab-1 | (4a²-1)²上做直接代数变形——展开多项式、尝试因式分解、枚举小例子找规律，但无法发现模运算提取商结构这一关键步骤
- correct_method: 推广为n>1的一般形式，对t=na取模发现商k=tc-1，构造无穷递降，用良序原理导出矛盾

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，characterization/direct_calculation/method_translation均已存在且适用
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，三个维度都是中等偏抽象粒度
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够，无需新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

### 局部tell_hint_pairs

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对整除条件蕴含等式的问题，尚未识别出条件的结构特征（nab-1形式的线性/平方不对称性） | 观察条件的形式结构，识别"4"和"-1"的模式，注意除数和被除数的形式 | 0.8 | 纯元认知观察 | false | {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"method_problem_mismatch"} | ["整除条件形式","nab-1结构","不对称性"] |
| 2 | AI列出了多个方向但不知道哪个有效，特别是没有自然想到无穷递降 | 列出所有可能方向，包括Vieta跳跃/无穷递降/推广 | 0.7 | 自由列举 | false | {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"search_space_estimation"} | ["方法枚举","Vieta跳跃","无穷递降","推广"] |
| 3 | AI尝试直接代数变形但陷入多项式除法的复杂性，无法提取有用结构 | 试直接展开和除法，发现走不通，需要更结构化的方法 | 0.4 | 小尝试 | false | {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"method_problem_mismatch"} | ["多项式展开","因式分解","直接除法失效"] |
| 4 | AI在直接变形失败后，没有想到推广化归——将4替换为n>1使结构更清晰 | 做推广操作，将4替换为一般n>1，观察条件关于a,b的对称性 | 0.5 | 思维操作引导 | false | {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"structural_transformation"} | ["推广化归","n>1一般化","对称性观察"] |
| 5 | AI推广后看到了对称性，但没有想到用无穷递降——关键思维瓶颈 | 用无穷递降思路，从(a,b)构造更小的c，对t=na取模提取商的结构 | 0.5 | 思维操作引导 | false | {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"method_translation"} | ["无穷递降","构造更小解","模运算","t=na"] |
| 6 | AI已得到k=tc-1但需要验证0<c<a——需要具体的大小估计技巧 | 用大小估计验证0<c<a：由a<b得k<(ta-1)<ta从而c<a，由k>0得c>0 | 0.3 | 推进 | true | {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"knowledge_gap"} | ["大小估计","不等式界定","c<a验证","k的范围"] |
| 7 | AI有所有零件但需要组装成完整证明——对称性+递降+良序原理的组合 | 组装所有部分：对称性处理b<a情形，递降+良序原理导出矛盾 | 0.6 | 能量传递引导 | false | {problem_type:"characterization", ai_method_type:"logical_deduction", gap_type:"method_translation"} | ["对称性","良序原理","反证法","组装证明"] |

### 全局tell_hint_pairs

**Pair 1 (path_feature)**:
- scope_type: "path_feature"
- scope: "从直接代数变形到模运算+无穷递降的完整路径"
- observation_point: null
- tell: 整个解题路径的关键特征是"从直接计算到结构化数论方法的翻译"——直接在原始形式上做代数变形无法提取有用结构，必须通过推广+模运算+递降的组合才能到达解答
- hint: 当整除条件蕴含等式的问题中直接变形失效时，考虑推广参数+模运算提取商的结构+无穷递降
- hint_level: 0.7
- generalizability: "high — 推广+模运算提取结构+递降的模式可泛化到类似整除条件问题"
- why_not_visible_locally: "在任何一个单独的QA轮次中，AI只能看到当前步骤的困难（如多项式除法走不通、不知道如何构造更小解），但看不到完整路径需要'推广→模运算→递降→良序'四步组合的必要性。这个组合路径的特征只有在回顾整个解题过程时才显现。"
- tell_topology: {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"method_translation"}
- tell_small_concepts: ["推广化归","模运算提取商结构","无穷递降","良序原理"]

**Pair 2 (implicit)**:
- scope_type: "implicit"
- scope: "R5中模运算提取k=tc-1的步骤蕴含了递降的可能性"
- observation_point: "R5"
- tell: 在R5中，对t=na取模发现k≡-1(mod t)即k=tc-1，这一步不仅确定了商的形式，还隐含了c必须为正整数且c<a的递降结构——但这个蕴含关系在R5的局部视角中不可见，需要R6的大小估计才能确认
- hint: 模运算提取的商结构k=tc-1中隐含递降参数c，需要后续大小估计来确认递降可行性
- hint_level: 0.6
- generalizability: "medium — 模运算提取商结构蕴含递降的模式可泛化到类似的Vieta跳跃问题，但具体可行性需逐题验证"
- why_not_visible_locally: "在R5的局部步骤中，AI只看到k=tc-1这个代数结果，但c是否为正整数、是否c<a这些递降可行性条件需要R6的不等式估计才能确认。模运算提取结构'蕴含'递降可行性这一关系，在R5单独看是不可见的——它是R5和R6之间的隐含连接。"
- tell_topology: {problem_type:"characterization", ai_method_type:"direct_calculation", gap_type:"structural_transformation"}
- tell_small_concepts: ["模运算提取商结构","k=tc-1","递降可行性","隐含连接"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会在原始形式4ab-1 | (4a²-1)²上做直接代数变形或枚举小例子，无法想到推广为n>1一般形式，更无法发现对t=na取模提取商结构k=tc-1这一关键步骤，因此无法构造无穷递降。即使AI想到Vieta跳跃，也可能卡在模运算提取商结构的具体技巧上。
- suitable_for_poc: ["hint注入实验——验证'推广+模运算+递降'的脉络注入能否引导AI到达解答", "tell识别实验——验证系统能否从AI的thinking中识别出'直接变形失效'的分叉信号并匹配到'推广+递降'方向", "瓶颈定位实验——验证R5(思维瓶颈)和R6(知识瓶颈)的区分是否有效"]
- discriminates_levels: true（此题需要推广化归+模运算+无穷递降的组合思维，能有效区分有无数论竞赛经验的AI）

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
- [x] answer（"a = b（若4ab-1整除(4a²-1)²，则a=b）"）
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

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: compfiles_imo2007p5, 7 local pairs, 2 global pairs, per-pair拓扑存在, why_not_visible_locally存在, answer非None, knowledge_bottleneck="R6", thinking_bottleneck="R5"

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2007p5
- solution_method_type: infinite_descent
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类（characterization/direct_calculation/method_translation等）完全够用，粒度一致
- 是否遇到异常: 否，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
