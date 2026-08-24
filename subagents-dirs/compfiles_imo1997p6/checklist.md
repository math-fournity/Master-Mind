# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1997p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1997P6.lean
- **来源**: IMO 1997 P6
- **ArangoDB progress记录_key**: 329162（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Imo1997P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：对每个正整数n，f(n)表示将n表示为2的非负整数次幂之和的方式数（顺序不同视为同一种）。例如f(4)=4，因为4=4=2+2=2+1+1=1+1+1+1。证明对所有整数n≥3，2^(n²/4) < f(2^n) < 2^(n²/2)。
- 解答核心思路（1-2句话）：通过奇偶性建立f的递推关系f(2m+1)=f(2m), f(2m+2)=f(2m+1)+f(m+1)，导出求和公式f(2N)=Σf(i)；上界用f(2m)<(m+1)f(m)配平方归纳，下界用配对不等式f(k)+f(2r+1-k)≥2f(r)配四次方两步归纳。
- 解答关键步骤列表：
  1. 建立递推：奇数必须含1（去掉得f(2m+1)=f(2m)）；偶数2m+2要么含1（去掉得f(2m+1)的表示）要么不含1（全部除以2得f(m+1)的表示），故f(2m+2)=f(2m+1)+f(m+1)
  2. 迭代递推得求和公式：f(2N) = Σ_{i=0}^{N} f(i)
  3. 单调性：f单调非降
  4. 上界引擎：f(2m) < (m+1)·f(m)（因f(0)=1<f(m)使严格），平方归纳：(f(2^n))² ≤ 2^(n²)，关键不等式(2^n+1)² ≤ 2^(2n+1)
  5. 下界配对：f(k)+f(2r+1-k)关于k单调非增，每对≥2f(r)，故Σ_{i=1}^{2r} f(i) ≥ 2r·f(r)
  6. 下界两步递推：f(2^(n+1)) > 2^n·f(2^(n-1))
  7. 下界四次方归纳：(f(2^n))^4 > 2^(n²)，关键恒等式4(n+2)+(n+1)²=(n+3)²
  8. 取四次方根和平方根得最终不等式

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：f(n)是什么函数？我们要证明什么？已知条件和目标之间有什么gap？ | f(n)是二进制分拆函数（将n表示为2的幂之和的方式数，不计顺序）。要证2^(n²/4)<f(2^n)<2^(n²/2)，即f(2^n)被夹在两个关于n²的指数之间。gap在于f没有显式公式，需要找到间接估计方法。 |
| 2 | 自由列举 | 0.7 | 列出所有你能想到的估计f(2^n)的方法方向。 | 直接计算小值找规律；找递推关系；生成函数方法；直接对不等式做归纳；利用分拆函数的已知渐近公式；利用f的单调性。 |
| 3 | 小尝试 | 0.4 | 试着计算f(2^n)的小值（n=1,2,3,4），看看能否猜出公式或规律。 | f(1)=1, f(2)=2, f(4)=4, f(8)=10, f(16)=36。没有明显的闭式公式。增长速度远快于多项式但被指数n²/2控制。直接计算无法给出一般界。 |
| 4 | 思维操作引导 | 0.5 | 考虑f的奇偶性：表示一个奇数时必须含1，表示一个偶数时可以分两种情况（含1或不含1）。由此推导f的递推关系。 | 奇数2m+1必须含1，去掉一个1得2m的表示，故f(2m+1)=f(2m)。偶数2m+2：含1则去掉1得2m+1的表示；不含1则所有summand都是偶数，全部除以2得m+1的表示。故f(2m+2)=f(2m+1)+f(m+1)。 |
| 5 | 推进 | 0.6 | 从递推关系f(2m+2)=f(2m+1)+f(m+1)和f(2m+1)=f(2m)出发，推导f(2N)的求和公式，然后利用单调性建立上界。 | 迭代得f(2N)=Σ_{i=0}^{N}f(i)。因f单调非降，f(2N)<(N+1)f(N)（因f(0)=1<f(N)使严格）。对上界做平方归纳：(f(2^n))²≤2^(n²)，关键步骤(2^n+1)²≤2^(2n+1)。 |
| 6 | 思维操作引导 | 0.5 | 对于下界，考虑将求和Σ_{i=1}^{2r}f(i)中的项配对：f(k)与f(2r+1-k)。利用单调性和递推关系，证明每对之和≥2f(r)。 | 配对f(k)+f(2r+1-k)：当k从1到r时，这对值非增（由递推和单调性可证），且最大对f(r)+f(r+1)≥2f(r)（因f(r+1)≥f(r)）。故每对≥2f(r)，Σ≥2r·f(r)。由此得两步递推f(2^(n+1))>2^n·f(2^(n-1))。 |
| 7 | 能量传递引导 | 0.7 | 现在你有了两步递推f(2^(n+1))>2^n·f(2^(n-1))。用四次方做强归纳（注意4(n+2)+(n+1)²=(n+3)²），结合上界的平方归纳，完成证明。 | 下界：(f(2^n))^4>2^(n²)由强归纳，基础n=1,2,3验证，归纳步用两步递推四次方+恒等式4(n+2)+(n+1)²=(n+3)²。上界：(f(2^n))²<2^(n²)对n≥3。取四次方根和平方根得2^(n²/4)<f(2^n)<2^(n²/2)。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4（找到奇偶性递推关系是纯知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6（配对技巧是思维/insight瓶颈）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 二进制分拆函数f(n)在2的幂次处取值的双向指数夹逼。核心结构是：无显式公式的计数函数→通过递推转化为求和→通过配对/单调性建立递推不等式→通过策略性归纳（不同次方）完成夹逼。上下界使用不同的归纳策略（平方vs四次方）。
- key_objects: ["二进制分拆函数f(n)", "递推关系f(2m+1)=f(2m), f(2m+2)=f(2m+1)+f(m+1)", "求和公式f(2N)=Σf(i)", "配对不等式f(k)+f(2r+1-k)≥2f(r)", "平方归纳(上界)", "四次方两步归纳(下界)"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["parity_decomposition（奇偶性分解建立递推）", "recursive_structure_finding（从计数问题提取递推结构）", "sum_formula_derivation（从递推迭代出求和公式）", "pairing_symmetry（对称配对建立下界）", "strategic_induction_exponent（选择策略性归纳次方使归纳闭合）", "two_track_strategy（上下界分别用不同归纳策略）"]
- primary_pattern: recursive_structure_finding（整个证明的基础是找到并利用f的递推结构）
- knowledge_required: ["二进制分拆函数的定义与性质", "奇偶性导致的递推关系", "从递推迭代求和公式", "分拆函数单调性", "配对对称不等式", "强归纳与策略性归纳次方选择", "代数恒等式4(n+2)+(n+1)²=(n+3)²"]
- key_insight: 二进制分拆函数满足奇偶递推f(2m+1)=f(2m)和f(2m+2)=f(2m+1)+f(m+1)，由此得f(2N)=Σf(i)；上界用f(2m)<(m+1)f(m)配平方归纳，下界用配对不等式f(k)+f(2r+1-k)≥2f(r)配四次方两步归纳——关键是上下界需要不同的归纳次方才能使归纳步闭合。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 组合计数（直接枚举分拆方式，试图找闭式公式或规律）
- translation_to: 递推代数操作（递推关系→求和公式→单调性/配对不等式→策略性归纳）
- translation_type: method_translation（从直接的组合计数方法翻译为递推+归纳的代数方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["二进制分拆", "奇偶递推", "求和公式", "配对不等式", "平方归纳", "四次方两步归纳", "单调性", "策略性归纳次方"]
- expected_ai_method: bare AI会直接计算f(2^n)的小值试图找规律或闭式公式，然后尝试对不等式直接做归纳，但缺少递推关系这个关键中间结构
- correct_method: 通过奇偶性建立递推→迭代出求和公式→上界用单调性+平方归纳，下界用配对对称+四次方两步归纳

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type=inequality_proof、ai_method_type=direct_calculation、gap_type=structural_transformation都能归入已有拓扑类别
- [x] 粒度是否一致——标注值和已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。这道题的特殊性在于"上下界需要不同的归纳策略"，但这属于gap_type=structural_transformation的范畴，不需要新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，现有拓扑分类足够

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| R | tell | hint | hint_level | situation_type | is_kb | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到计数函数的指数夹逼问题但未识别递推结构 | 描述题目结构：f(n)是什么，要证什么，gap在哪 | 0.8 | 纯元认知观察 | false | {inequality_proof, direct_calculation, method_problem_mismatch} | ["二进制分拆", "指数夹逼", "无显式公式"] |
| 2 | AI列举方向但未优先考虑递推方法 | 列出所有估计f(2^n)的方法方向 | 0.7 | 自由列举 | false | {inequality_proof, enumeration_brute_force, search_space_estimation} | ["递推关系", "生成函数", "直接归纳", "渐近公式"] |
| 3 | AI计算小值f(1)=1,f(2)=2,f(4)=4,f(8)=10但找不到闭式 | 计算f(2^n)小值看能否猜出公式 | 0.4 | 小尝试 | false | {inequality_proof, direct_calculation, method_problem_mismatch} | ["小值计算", "闭式公式", "增长速度"] |
| 4 | AI未考虑用奇偶性分解建立递推 | 考虑奇偶性：奇数必含1，偶数分含1/不含1两种情况，推导递推 | 0.5 | 思维操作引导 | true | {inequality_proof, direct_manipulation, knowledge_gap} | ["奇偶递推", "含1不含1分类", "halving操作"] |
| 5 | AI有递推但未迭代出求和公式和上界 | 从递推迭代求和公式f(2N)=Σf(i)，用单调性建上界 | 0.6 | 推进 | false | {inequality_proof, algebraic_identity, method_translation} | ["求和公式", "单调性", "平方归纳", "(2^n+1)²≤2^(2n+1)"] |
| 6 | AI有求和公式但未尝试对称配对 | 将Σ中项配对f(k)与f(2r+1-k)，证每对≥2f(r) | 0.5 | 思维操作引导 | true | {inequality_proof, direct_manipulation, structural_transformation} | ["配对对称", "非增序列", "2f(r)下界", "两步递推"] |
| 7 | AI有两条递推但未选择正确归纳次方 | 用四次方做强归纳(4(n+2)+(n+1)²=(n+3)²)，结合平方归纳完成 | 0.7 | 能量传递引导 | false | {inequality_proof, algebraic_identity, method_translation} | ["四次方归纳", "平方归纳", "代数恒等式", "强归纳"] |

**全局tell_hint_pairs详情**：

| scope_type | scope | obs_pt | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|
| path_feature | 整个证明路径（从题目到最终夹逼） | null | 上下界需要完全不同的归纳策略：上界用平方归纳（一步递推f(2^(n+1))~f(2^n)），下界用四次方两步归纳（两步递推f(2^(n+1))~f(2^(n-1))） | 在建立递推后，分别对上下界选择使归纳步闭合的归纳次方——上界平方因一步递推，下界四次方因两步递推 | 0.7 | high——任何需要双向夹逼且上下界结构不同的问题都需要此策略 | 在单步视角中只能看到一条递推不等式，无法判断该用几次方归纳；需要同时看到递推的"步长"（一步vs两步）和归纳闭合条件才能选择正确次方 | {inequality_proof, algebraic_identity, structural_transformation} | ["平方归纳", "四次方归纳", "一步递推", "两步递推", "归纳闭合"] |
| implicit | R7的归纳次方选择 | R7 | 四次方的选择不是任意的，而是由两步递推f(2^(n+1))>2^n·f(2^(n-1))的结构决定的：四次方使归纳步中4(n+2)+(n+1)²=(n+3)²恰好闭合 | 选择归纳次方时，分析递推的步长（跨几步）和指数增长率，使归纳步的代数恒等式闭合 | 0.6 | medium——适用于递推+归纳结合的问题，但具体次方取决于递推结构 | 在R7局部只看到"用四次方归纳"，但看不到为什么是四次方而非其他次方——这个why来自R6的两步递推结构和归纳闭合的代数要求，是跨步骤的蕴含信息 | {inequality_proof, algebraic_identity, method_translation} | ["归纳次方选择", "两步递推", "代数恒等式闭合", "步长分析"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会直接计算f(2^n)的小值(f(1)=1,f(2)=2,f(4)=4,f(8)=10,f(16)=36)，找不到闭式公式后尝试对不等式直接做归纳。即使偶然发现递推关系，也极可能错过配对技巧（下界的关键步骤）和策略性归纳次方选择（四次方vs平方的区分）。这道题是IMO历史上最难的题目之一，bare AI几乎不可能在无引导下完成。
- suitable_for_poc: ["tell端形式化过滤POC——递推结构识别vs直接计算的拓扑区分", "hint端脉络注入POC——递推关系+配对技巧的逐步注入", "知识瓶颈POC——R4奇偶递推和R6配对技巧的知识注入效果", "跨步骤蕴含信息POC——归纳次方选择的implicit tell验证"]
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

**产出**：profile.json已写入，所有字段完整验证通过（answer非None，why_not_visible_locally非None，situation_type规范，hint_level为0-1浮点数，每个pair含tell_topology和tell_small_concepts）

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
2. 更新`problem_extraction_progress`集合中`_key="329162"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1997p6"
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
    '_key': '329162',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1997p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1997p6')
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
- problem_id: compfiles_imo1997p6
- solution_method_type: recurrence_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有拓扑分类足够
- 是否遇到异常: 否

**操作**：向Master Agent报告

**汇报内容**：
- problem_id:
- solution_method_type:
- 局部(tell,hint)对数量:
- 全局(tell,hint)对数量:
- 是否发现新维度:
- **拓扑分类是否有进化建议**:
- 是否遇到异常:

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
