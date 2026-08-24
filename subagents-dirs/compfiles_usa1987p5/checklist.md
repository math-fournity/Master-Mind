# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1987p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1987P5.lean
- **来源**: USA 1987 P5
- **ArangoDB progress记录_key**: 329348（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1987P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：a₁,a₂,...,aₙ是0和1的序列。T是三元组(aᵢ,aⱼ,aₖ)(i<j<k)中不等于(0,1,0)或(1,0,1)的个数。f(i)=(j<i且aⱼ=aᵢ的个数)+(j>i且aⱼ≠aᵢ的个数)。证明T=Σf(i)(f(i)-1)/2。n为奇数时T的最小值是多少？
- 解答核心思路（1-2句话）：Part1将好三元组分为三类（全等A、前两等B、后两等C），每类按索引分解计数，用Vandermonde恒等式C(x+y,2)=C(x,2)+C(y,2)+xy合并为C(f(i),2)之和。Part2利用Σf(i)=C(n,2)为常数，由凸性(Cauchy-Schwarz)得下界，交替序列达到等号。
- 解答关键步骤列表：
  1. good_iff：三元组"好"⟺相邻两位有相等（x=y或y=z）
  2. 分类：tripsA(全等)、tripsB(前两等第三异)、tripsC(前异后两等)，三者不交且并集=好三元组
  3. card_tripsA = Σ C(eqBefore(k), 2)（选k前两个同值位置）
  4. card_tripsB = Σ eqBefore(j)*neqAfter(j)（j前同值×j后异值）
  5. card_tripsC = Σ C(neqAfter(i), 2)（选i后两个异值位置）
  6. Vandermonde: C(eqBefore+neqAfter, 2) = C(eqBefore,2)+C(neqAfter,2)+eqBefore*neqAfter = C(f(i),2)
  7. 求和得 T = Σ C(f(i),2) = Σ f(i)(f(i)-1)/2
  8. sum_f: Σf(i) = C(n,2)（常数，与序列无关——双计数对(i,j)）
  9. lower_bound: 由Cauchy-Schwarz, Σf(i)²≥(Σf(i))²/n，得T≥(C(n,2)²/n - C(n,2))/2
  10. n=2k+1时：T≥(2k+1)·C(k,2) = n(n-1)(n-3)/8
  11. 交替序列altSeq使f(i)=k对所有i成立，达到等号

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
| 1 | 纯元认知观察 | 0.3 | 描述题目结构：T在数什么？f(i)的两个组成部分分别是什么？你注意到T和f(i)之间可能有什么结构联系？ | T数的是非交替三元组（不是010或101的三元组）。f(i) = eqBefore(i) + neqAfter(i)，即i之前同值的位置数加上i之后异值的位置数。注意到f(i)似乎在衡量位置i与序列中其他位置的"一致性"，而T在数三元组的模式，两者可能通过某种组合恒等式联系。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的方法来建立T和ΣC(f(i),2)之间的联系。考虑：按三元组类型分类计数、按位置分解、用组合恒等式等。 | 可能方法：(a)直接枚举所有好三元组类型(000,001,011,100,110,111)逐个计数；(b)按中间元素位置分解三元组；(c)注意到"好"意味着相邻两位有相等，按哪对相邻相等分类；(d)将f(i)拆为eqBefore和neqAfter，分别看它们在三元组计数中的角色；(e)尝试小例子(n=3,4,5)验证公式。 |
| 3 | 小尝试 | 0.2 | 试着直接枚举所有好三元组类型(000,001,011,100,110,111)并逐个计算每种类型的数量。看看能否得到ΣC(f(i),2)。 | 枚举6种好三元组类型，但发现逐类型计数需要知道每种值模式在序列中出现的次数，这取决于序列的具体排列，难以直接表达为f(i)的函数。陷入case analysis的泥潭，6种情况各自需要不同的计数方式，且无法自然合并为C(f(i),2)的形式。 |
| 4 | 思维操作引导 | 0.6 | 换一种分类方式：好三元组意味着相邻两位有相等。按"哪对相邻相等"分类——(1)三值全等aᵢ=aⱼ=aₖ，(2)前两等aᵢ=aⱼ≠aₖ，(3)前异后两等aᵢ≠aⱼ=aₖ。对每个类型，用eqBefore和neqAfter表达计数。 | 类型A(全等)：以k为最大索引，选k前两个同值位置，计数=ΣC(eqBefore(k),2)。类型B(前两等第三异)：以j为中间索引，j前选一个同值、j后选一个异值，计数=ΣeqBefore(j)·neqAfter(j)。类型C(前异后两等)：以i为最小索引，i后选两个异值位置，计数=ΣC(neqAfter(i),2)。三类不交且覆盖所有好三元组。 |
| 5 | 思维操作引导 | 0.7 | 现在你有T=ΣC(eqBefore(i),2)+ΣeqBefore(i)·neqAfter(i)+ΣC(neqAfter(i),2)。注意到f(i)=eqBefore(i)+neqAfter(i)。用Vandermonde恒等式C(x+y,2)=C(x,2)+C(y,2)+xy将三项合并。 | 对每个i，C(eqBefore(i)+neqAfter(i),2) = C(eqBefore(i),2)+C(neqAfter(i),2)+eqBefore(i)·neqAfter(i) = C(f(i),2)。因此T = ΣC(f(i),2) = Σf(i)(f(i)-1)/2。Part 1完成！ |
| 6 | 推进 | 0.6 | 对于Part 2（n为奇数时T的最小值）：首先计算Σf(i)——它是否与序列无关？然后利用C(x,2)的凸性（或Cauchy-Schwarz）来得到T的下界。 | Σf(i) = ΣeqBefore(i) + ΣneqAfter(i)。通过双计数对(i,j)（i<j），每对恰好贡献1（若aᵢ=aⱼ贡献给eqBefore(j)，若aᵢ≠aⱼ贡献给neqAfter(i)），所以Σf(i)=C(n,2)，与序列无关。由Cauchy-Schwarz：Σf(i)²≥(Σf(i))²/n = C(n,2)²/n。因此T=(Σf(i)²-Σf(i))/2 ≥ (C(n,2)²/n - C(n,2))/2。n=2k+1时化简得T≥(2k+1)·C(k,2) = n(n-1)(n-3)/8。 |
| 7 | 能量传递引导 | 0.4 | 验证交替序列0,1,0,1,...是否达到等号。计算交替序列中每个位置的f(i)，确认所有f(i)相等。然后写出最终答案。 | 交替序列中位置i的eqBefore(i)=⌊i/2⌋（i之前同奇偶的位置数），neqAfter(i)=k-⌊i/2⌋（i之后异奇偶的位置数），所以f(i)=k对所有i成立。所有f(i)相等意味着Cauchy-Schwarz等号成立。T=(2k+1)·C(k,2)=n(n-1)(n-3)/8。n为奇数时T的最小值为n(n-1)(n-3)/8。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R6+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R5）
- level_sum: 0.3+0.5+0.2+0.6+0.7+0.6+0.4 = 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

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
- problem_type: `discrete_combinatorial`
- structure_features: 二元序列上的三元组计数问题，包含两部分：(1)组合恒等式证明（双计数+Vandermonde恒等式），(2)组合优化（常数和+凸性下界+等号构造）。核心结构是将三元组级别的计数翻译为索引级别的组合数求和。
- key_objects: ["0-1序列", "好三元组(非交替三元组)", "f(i)函数(eqBefore+neqAfter)", "Vandermonde恒等式C(x+y,2)", "Cauchy-Schwarz不等式", "交替序列(等号构造)"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["combinatorial_classification", "double_counting", "algebraic_identity_application", "convexity_optimization", "equality_case_verification"]
- primary_pattern: `double_counting`
- knowledge_required: ["Vandermonde恒等式C(x+y,2)=C(x,2)+C(y,2)+xy", "Cauchy-Schwarz不等式/QM-AM", "组合数C(n,2)的性质", "双计数技巧", "凸函数优化（常数和下凸函数和最小化）"]
- key_insight: 好三元组按"哪对相邻位相等"分为三类(A全等/B前两等/C后两等)，每类可按索引分解为eqBefore和neqAfter的组合，而Vandermonde恒等式C(x+y,2)=C(x,2)+C(y,2)+xy恰好将三项合并为C(f(i),2)，其中f(i)=eqBefore(i)+neqAfter(i)。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 三元组级别的枚举计数（按值模式分类好三元组）
- translation_to: 索引级别的组合恒等式（Vandermonde分解为按索引求和的C(f(i),2)）
- translation_type: `structural_transformation`（从三元组粒度的计数结构翻译为索引粒度的代数恒等式结构）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["好三元组分类", "eqBefore/neqAfter分解", "Vandermonde恒等式", "常数和不变量", "凸性下界", "交替序列等号"]
- expected_ai_method: bare AI预期会直接枚举6种好三元组值模式逐个计数，陷入case analysis泥潭，无法自然连接到f(i)的Vandermonde分解
- correct_method: 按"哪对相邻位相等"分类好三元组为三类，每类按索引分解为eqBefore/neqAfter的组合，用Vandermonde恒等式合并为C(f(i),2)；优化部分利用Σf(i)=C(n,2)常数性和Cauchy-Schwarz凸性

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。discrete_combinatorial、enumeration_brute_force、structural_transformation都已有且粒度合适。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个维度都是抽象级别，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的独特性在于"双计数+Vandermonde"的组合，但这可以通过small_concepts区分，不需要新维度。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。当前三维度+small_concepts足以区分。

**拓扑进化建议**（如有）：无。当前拓扑分类体系足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs**：

1. **path_feature型**：
   - scope: "Part 1完整证明路径——从三元组计数到C(f(i),2)求和"
   - tell: "证明需要非显然的分解路径：分类好三元组→按索引分解→Vandermonde恒等式合并。这条路径的每一步在局部视角都不明显"
   - hint: "路径是：按相邻相等分类→per-index分解为eqBefore/neqAfter组合→Vandermonde合并为C(f(i),2)"
   - hint_level: 0.7
   - generalizability: "high — Vandermonde分解模式适用于许多涉及per-element组合数求和的组合恒等式问题"
   - why_not_visible_locally: "在任何单一步骤中，三元组计数与C(f(i),2)之间的联系都不明显——需要看到从分类到per-index分解到代数恒等式的完整路径。Vandermonde恒等式作为桥梁，在三块拼图都到位之前是不可见的"

2. **implicit型**：
   - scope: "Part 2优化——Σf(i)的常数性"
   - observation_point: "R6"
   - tell: "Σf(i)=C(n,2)是与序列无关的常数——这个不变量在题目中未明说，是优化的关键"
   - hint: "双计数对(i,j)：每对恰好贡献1给Σf(i)，所以Σf(i)=C(n,2)与序列无关"
   - hint_level: 0.6
   - generalizability: "high — '常数和+凸性'是组合优化中的标准模式"
   - why_not_visible_locally: "Σf(i)的常数性是一个隐含性质，需要单独的双计数论证——从f(i)的定义本身看不出这个不变量，而且直到尝试优化时才会意识到这个不变量的重要性"

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "AI会正确枚举好三元组类型但无法连接到f(i)的Vandermonde分解。对于优化部分，AI不会意识到Σf(i)是常数，会尝试case analysis或微积分优化而非凸性论证。核心瓶颈在于Vandermonde恒等式作为知识gap，以及三元组分类方式（按相邻相等而非按值模式）作为思维gap。"
- suitable_for_poc: ["tell_extraction_from_thinking", "hint_injection_at_knowledge_bottleneck", "vandermonde_identity_as_knowledge_gap_test", "convexity_optimization_as_thinking_gap_test", "structural_transformation_gap_test"]
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
- [x] answer（proof类型填要证明的结论+最小值）
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

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 `subagents-dirs/compfiles_usa1987p5/profile.json`

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329348"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1987p5"
   - extracted_by改为"subagent"

**示例代码**：
```python
from arango import ArangoClient
from datetime import datetime, timezone
import json

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
now = datetime.now(timezone.utc).isoformat()

# 读取profile.json
with open('profile.json', 'r') as f:
    profile = json.load(f)

# 写入problem_profiles
db.collection('problem_profiles').insert(profile, overwrite=True)

# 更新problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '329348',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1987p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1987p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_usa1987p5
- solution_method_type: double_counting_with_vandermonde_and_convexity
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。当前三维度（problem_type/ai_method_type/gap_type）+ small_concepts足以覆盖此题。discrete_combinatorial/enumeration_brute_force/structural_transformation均已有且粒度合适。
- 是否遇到异常: 否。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
