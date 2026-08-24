# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2022p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2022P5.lean
- **来源**: IMO 2022 P5
- **ArangoDB progress记录_key**: 329266（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2022P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求所有正整数三元组 (a, b, p) 满足 a^p = b! + p，其中 p 是素数。
- 解答核心思路（1-2句话）：按 b 与 p 的大小关系分三种情况（b < p, p ≤ b < 2p, b ≥ 2p），利用整除性和大小估计逐步排除，最终用升幂引理（LTE）排除 p ≥ 5，只剩 p=2 和 p=3 两个解。
- 解答关键步骤列表：
  1. **Case b < p**：若 a ≤ b 则 a | b! → a | (b!+p) = a^p → a | p → a=1（因 a < p），但 1^p = 1 < b!+p，矛盾。若 a > b 则 a ≥ b+1，用二项式定理 (b+1)^p ≥ 1 + bp + b^p > b! + p（因 b! ≤ b^b ≤ b^p），矛盾。
  2. **Case p ≤ b**：p | b!（因 p ≤ b）→ p | (b!+p) = a^p → p | a（因 p 素数）。
  3. **Sub-case p ≤ b < 2p**：写 a = pc。若 c < p 则 c | a^p 且 c | b! → c | p → c=1 → a=p。若 c ≥ p 则 a ≥ p^2 → a^p ≥ p^(2p) > b!+p（用 (2p-1)! < p^(2p) 的乘积分解），矛盾。故 a = p。
  4. **a = p, p ≥ 5**：b > p（因 b=p 时 p!+p < p^p），故 (p+1)^2 | b!（因 p+1 偶数，(p+1)/2 和 p+1 都在 b! 中出现）。由 LTE：p^p ≡ p^2-1 (mod (p+1)^2)，故 (p+1)^2 | (p^2-1) = (p-1)(p+1) → (p+1) | (p-1)，矛盾。
  5. **a = p, p < 5**：p=2 → b!=2 → b=2，解 (2,2,2)；p=3 → b!=24 → b=4，解 (3,4,3)。
  6. **Case b ≥ 2p**：p^2 | (2p)! | b!（因 p!·p! | (2p)!）且 p^2 | a^p（因 p | a），故 p^2 | (a^p - b!) = p，矛盾（因 p^2 > p）。

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**每轮必须标注**：
- **question**：给AI的提示/问题（Q）
- **expected_answer**：预期回复（A）
- **situation_type**：**⚠️ 只能取以下6个值之一，禁止自创**
- **level**：**⚠️ 必须是0-1之间的浮点数**

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察方程 a^p = b! + p 的结构。等号左边是什么类型的表达式？右边呢？p 的约束条件是什么？a, b 的取值范围是什么？ | 左边是 a 的 p 次幂，右边是 b 的阶乘加素数 p。a, b 为正整数，p 为素数。需要求所有满足条件的三元组 (a, b, p)。关键观察：左边是指数形式，右边包含阶乘，两者的增长速度差异很大。 |
| 2 | 自由列举 | 0.7 | 对于方程 a^p = b! + p，你能想到哪些可能的解题方向？列出所有你能想到的方法。 | 1. 枚举小素数 p=2,3,5,7... 逐一验证；2. 模运算分析（mod p, mod (p+1) 等）；3. 利用 p | b! 的整除性；4. 大小估计比较 a^p 和 b! 的增长；5. 按 b 与 p 的大小关系分类讨论；6. 升幂引理（LTE）；7. Wilson 定理等相关数论工具。 |
| 3 | 小尝试 | 0.4 | 试着计算一些小的情形。p=2 时哪些 (a,b) 满足方程？p=3 呢？p=5 呢？ | p=2: a^2 = b!+2。b=2: a^2=4, a=2 ✓ → (2,2,2)。b=3: a^2=8, 非平方数。p=3: a^3=b!+3。b=4: a^3=27, a=3 ✓ → (3,4,3)。p=5: a^5=b!+5。b=5: a^5=125, a≈2.6 非整数。b=10: a^5=3628855, a≈20.4 非整数。看起来只有 (2,2,2) 和 (3,4,3) 两个解，但需要证明完备性。 |
| 4 | 思维操作引导 | 0.5 | 考虑 b < p 的情形。如果 b < p，你能利用 a 与 b 的大小关系导出矛盾吗？分 a ≤ b 和 a > b 两种子情况。 | 若 a ≤ b：a | b!（因 a ≤ b），又 a | a^p = b!+p，故 a | p。因 a < p（因 a ≤ b < p），故 a=1，但 1 = b!+p > 1 矛盾。若 a > b：a ≥ b+1，故 a^p ≥ (b+1)^p。由二项式定理 (b+1)^p ≥ 1+bp+b^p。而 b! ≤ b^b ≤ b^p（因 b < p），且 1+bp > p（因 b ≥ 1），故 a^p > b!+p 矛盾。因此 b < p 无解。 |
| 5 | 思维操作引导 | 0.4 | 现在 p ≤ b。利用 p | b! 这个事实，你能推出什么关于 a 的结论？ | 因 p ≤ b，故 p | b!。又 a^p = b!+p，故 p | a^p。因 p 是素数，由 p | a^p 推出 p | a。所以可以写 a = pc，其中 c 是正整数。 |
| 6 | 推进 | 0.5 | 已知 p | a，即 a = pc。在 p ≤ b < 2p 的条件下，试着确定 a 的值。考虑 c < p 和 c ≥ p 两种情况。 | 若 c < p：c | a^p（因 c | (pc)^p 中 c 的因子），且 c | b!（因 c < p ≤ b），故 c | (a^p - b!) = p。因 c < p 且 c | p，故 c=1，即 a=p。若 c ≥ p：a ≥ p^2，故 a^p ≥ p^(2p)。而 b < 2p 故 b! ≤ (2p-1)!。可以证明 (2p-1)! < p^(2p)（将 (2p-1)! 拆分为 ∏(p²-k²)·p 的形式，每项 ≤ p²），故 b!+p < p^(2p) ≤ a^p 矛盾。因此 a = p。 |
| 7 | 思维操作引导 | 0.3 | 现在 a = p，方程变为 p^p = b! + p。对于 p ≥ 5，利用升幂引理（LTE）证明不存在解。提示：考虑 (p+1)^2 整除 b! 的条件，以及 p^p - p 模 (p+1)^2 的值。 | 因 p ≥ 5 为奇素数，b > p（因 b=p 时 p!+p < p^p）。故 p+1 ≤ b，且 p+1 为偶数。在 b! 中，(p+1)/2 和 p+1 都作为因子出现（因 (p+1)/2 ≥ 3 > 0 且 p+1 ≤ b），且 2·((p+1)/2) = p+1，所以 (p+1)^2 | b!。由方程 p^p - p = b!，得 (p+1)^2 | (p^p - p)。但由 LTE/二项式展开：p^p = ((p+1)-1)^p ≡ p(p+1)(-1)^{p-1} + (-1)^p ≡ p(p+1) - 1 ≡ p^2-1 (mod (p+1)^2)（因 p 奇故 (-1)^{p-1}=1, (-1)^p=-1）。故 (p+1)^2 | (p^2-1) = (p-1)(p+1)，即 (p+1) | (p-1)，但 p+1 > p-1 > 0，矛盾。 |
| 8 | 能量传递引导 | 0.2 | 太好了！现在只需检查 p=2 和 p=3。验证这两个素数是否给出解，并确认 b ≥ 2p 的情形也被排除了。 | p=2: 2^2 = b!+2 → b!=2 → b=2。解 (2,2,2) ✓。p=3: 3^3 = b!+3 → b!=24 → b=4。解 (3,4,3) ✓。b ≥ 2p 情形：p^2 | (2p)! | b!（因 p!·p! | (2p)!）且 p^2 | a^p（因 p|a），故 p^2 | (a^p-b!) = p，但 p^2 > p（因 p ≥ 2），矛盾。故所有解为 {(2,2,2), (3,4,3)}。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1, R2, R6, R8）
- knowledge_rounds（思维操作引导的轮数）: 4（R4, R5, R7, 以及R6虽为推进但含知识引导，计入metacognitive）
- level_sum: 0.8+0.7+0.4+0.5+0.4+0.5+0.3+0.2 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R7"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（求所有满足条件的三元组，本质是刻画问题）
- structure_features: 指数Diophantine方程 a^p = b! + p，左边是幂运算，右边是阶乘加素数。关键结构在于 b 与 p 的大小关系决定了 b! 中 p 的幂次，从而决定整除链。三段式分类（b<p, p≤b<2p, b≥2p）是结构骨架。
- key_objects: ["素数 p", "正整数 a, b", "阶乘 b!", "幂 a^p", "整除关系 p|a", "升幂引理(LTE)模 (p+1)^2"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["case_split", "divisibility_analysis", "size_bounding", "lifting_the_exponent", "small_case_verification"]
- primary_pattern: case_split（三段式分类是主导思维模式）
- knowledge_required: ["素数整除性质", "阶乘的整除性（n! 包含哪些因子）", "二项式定理下界估计", "升幂引理(LTE)或等价的二项式展开模运算", "p!·p! | (2p)! 的组合恒等式"]
- key_insight: 按 b 与 p/2p 的大小关系三段分类，整除链 p|a → a=p 配合升幂引理排除 p≥5，只剩 p=2,3 两个小素数验证。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 枚举小情形+模式识别（bare AI 会枚举发现两个解但无法证明完备性）
- translation_to: 结构化分类讨论+整除链分析+升幂引理（通过 b vs p 的分类将枚举问题转化为可逐一排除的结构化证明）
- translation_type: method_translation（从枚举验证翻译为结构化排除）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["case_split_on_b_vs_p", "divisibility_chain_p_divides_a", "factorial_growth_bounding", "lifting_the_exponent_mod_p_plus_1_squared", "small_prime_verification"]
- expected_ai_method: 枚举小素数 p=2,3,5,7... 和小 b 值，发现 (2,2,2) 和 (3,4,3) 两个解，但无法证明完备性——缺少将问题结构化为分类讨论的能力，更缺少升幂引理的知识
- correct_method: 按 b 与 p/2p 三段分类，利用 p|b! → p|a 的整除链确定 a=p，再用升幂引理排除 p≥5，最后验证 p=2,3

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization / enumeration_brute_force / structural_transformation 均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——这道题的 tell（枚举→结构化分类+LTE）与已有 tell 可区分
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。当前拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs**：

1. **path_feature型**：
   - scope: 整个证明的三段式分类结构（b<p, p≤b<2p, b≥2p）
   - tell: AI枚举发现两个解后无法证明完备性——缺少将问题按 b vs p/2p 分类的结构化视角
   - hint: 按 b 与 p 的大小关系分三种情况，每种情况利用 b! 中 p 的幂次不同来建立不同的整除链
   - hint_level: 0.6
   - generalizability: high——三段式分类+整除链的模式可泛化到其他涉及阶乘和素数的Diophantine方程
   - why_not_visible_locally: 完整的三段式分类结构只有在全局视角下才可见——局部看每个case（b<p的整除矛盾、p≤b<2p的a=p确定、b≥2p的p²|p矛盾）似乎是独立的小问题，但它们共同构成一个完整的排除链，且整除链 p|a → a=p → LTE 跨越多个case才成立
   - tell_topology: {problem_type: "characterization", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
   - tell_small_concepts: ["three_way_case_split", "divisibility_chain_cross_cases", "structural_backbone"]

2. **implicit型**：
   - scope: R7的升幂引理应用——从 (p+1)^2 | b! 到 (p+1)^2 | (p^p - p) 再到矛盾
   - observation_point: R7
   - tell: AI到达 a=p 后面对 p^p = b! + p 不知道如何排除 p≥5——缺少将阶乘整除性（(p+1)^2 | b!）与模运算（p^p ≡ p²-1 mod (p+1)^2）连接的升幂引理知识
   - hint: 利用 p+1 为偶数时 (p+1)/2 和 p+1 都在 b! 中出现得到 (p+1)^2 | b!，再用二项式展开/LTE 计算 p^p mod (p+1)^2 = p²-1，导出 (p+1)|(p-1) 矛盾
   - hint_level: 0.3
   - generalizability: medium——升幂引理在素数幂模运算中的应用可泛化，但 (p+1)^2 | b! 的具体推导依赖于本题的特定结构
   - why_not_visible_locally: 阶乘整除性（(p+1)^2 | b! 当 b > p）和模运算（p^p ≡ p²-1 mod (p+1)^2）属于不同数学领域，在局部步骤中看不到它们的连接——需要同时知道"b! 中哪些因子出现"和"p^p 模 (p+1)^2 的值"才能发现矛盾，这个跨领域连接是隐含的
   - tell_topology: {problem_type: "characterization", ai_method_type: "algebraic_identity", gap_type: "knowledge_gap"}
   - tell_small_concepts: ["lifting_the_exponent", "factorial_divisibility_p_plus_1_squared", "modular_arithmetic_bridge", "binomial_expansion_mod"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI 会枚举小素数 p=2,3,5,7 和小 b 值，发现 (2,2,2) 和 (3,4,3) 两个解，但无法证明完备性。具体错误：(1) 不会想到按 b vs p/2p 三段分类；(2) 即使想到分类，也想不到用 p|b! → p|a 的整除链确定 a=p；(3) 最关键的知识瓶颈——不会用升幂引理/LTE 排除 p≥5，不知道 (p+1)^2 | b! 和 p^p ≡ p²-1 (mod (p+1)^2) 的连接。
- suitable_for_poc: ["tell_hint_validation", "knowledge_bottleneck_detection", "case_split_guidance", "lte_knowledge_injection"]
- discriminates_levels: true（这道题在枚举层面容易找到解，但完备性证明需要深层结构化思维和专业知识，能很好区分 AI 水平）

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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329266"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2022p5"
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
    '_key': '329266',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2022p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2022p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2022p5
- solution_method_type: case_analysis_with_divisibility
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，当前拓扑分类（characterization / enumeration_brute_force / structural_transformation）足够覆盖
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
