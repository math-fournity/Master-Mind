# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2010p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2010P5.lean
- **来源**: USA 2010 P5
- **ArangoDB progress记录_key**: 329440（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2010P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let $q = \frac{3p-5}{2}$ where $p$ is an odd prime, and let $S_q = \frac{1}{2\cdot3\cdot4} + \frac{1}{5\cdot6\cdot7} + \cdots + \frac{1}{q\cdot(q+1)\cdot(q+2)}$. Prove that if $\frac{1}{p} - 2S_q = \frac{m}{n}$ for integers $m$ and $n$, then $m-n$ is divisible by $p$.
- 解答核心思路（1-2句话）：用部分分式分解将$2S_q$转化为调和级数，再围绕$p=2t+1$做对称配对提取$p$因子，最后用$p$的素性证明分母$V$与$p$互质，从而得出$p \mid (m-n)$。
- 解答关键步骤列表：
  1. 参数化：$p=2t+1$（$t\geq1$），$q=3t-1$，求和指标$k=3i+2$（$i\in[0,t)$）
  2. 部分分式分解：$\frac{2}{k(k+1)(k+2)} = \frac{1}{k} - \frac{2}{k+1} + \frac{1}{k+2}$，当$k=3i+2$时化为$(\frac{1}{3i+2}+\frac{1}{3i+3}+\frac{1}{3i+4}) - \frac{1}{i+1}$
  3. 重标号：$\sum_{i=0}^{t-1}(\frac{1}{3i+2}+\frac{1}{3i+3}+\frac{1}{3i+4}) = \sum_{j=2}^{3t+1}\frac{1}{j}$（连续整数调和和）
  4. 调和和拆分：$H_{3t+1} = \sum_{i=0}^{t-1}\frac{1}{i+1} + \sum_{j=t+1}^{3t+1}\frac{1}{j}$
  5. 对称配对：中间和$\sum_{j=t+1}^{3t+1}\frac{1}{j}$围绕$2t+1=p$对称配对，每对$\frac{1}{p-i}+\frac{1}{p+i}=\frac{2p}{p^2-i^2}$
  6. 主恒等式：$\frac{1}{p} - 2S_q = 1 - 2p\sum_{i=0}^{t-1}\frac{1}{p^2-(i+1)^2}$
  7. 写成单分数：$\frac{1}{p}-2S_q = \frac{V-2pU}{V}$，其中$V=\prod_{i=0}^{t-1}(p^2-(i+1)^2)$
  8. 关键同余：$V-2pU \equiv V \pmod{p}$
  9. 证明$p\nmid V$：每个因子$p^2-(i+1)^2$不被$p$整除（因$0<i+1<p$且$p$素）
  10. 结论：由$(V-2pU)n=mV$和$V-2pU\equiv V\pmod{p}$得$p\mid(m-n)V$，再由$p\nmid V$和$p$素得$p\mid(m-n)$

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：$S_q$的求和指标是什么模式？$q$和$p$之间有什么关系？需要证明什么？ | $S_q$的指标是$k=2,5,8,\ldots,q$，即$k\equiv2\pmod{3}$。$q=(3p-5)/2$，$p$是奇素数。需证：若$\frac{1}{p}-2S_q=\frac{m}{n}$则$p\mid(m-n)$。这是一个数论整除性证明题。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用来处理这个求和与整除性证明的方法 | 部分分式分解、望远镜求和、模运算、直接计算、归纳法、生成函数、调和级数性质、对称性配对 |
| 3 | 小尝试 | 0.5 | 试试直接对$S_q$做模$p$运算或直接通分计算，看看会遇到什么困难 | 直接通分计算分母太复杂，模运算在有理数上不好直接操作。困难在于$S_q$是有理数的和，需要先找到统一的代数结构。 |
| 4 | 思维操作引导 | 0.3 | 对$\frac{1}{k(k+1)(k+2)}$做部分分式分解，并注意$k=3i+2$时三项连续整数$3i+2,3i+3,3i+4$的结构 | $\frac{2}{k(k+1)(k+2)}=\frac{1}{k}-\frac{2}{k+1}+\frac{1}{k+2}$。当$k=3i+2$时，$2S_q=\sum_{i=0}^{t-1}[(\frac{1}{3i+2}+\frac{1}{3i+3}+\frac{1}{3i+4})-\frac{1}{i+1}]$，其中$p=2t+1$。 |
| 5 | 推进 | 0.4 | 将$\sum(\frac{1}{3i+2}+\frac{1}{3i+3}+\frac{1}{3i+4})$重标号为连续调和和，然后寻找围绕$p=2t+1$的对称配对结构 | 重标号后$\sum_{i=0}^{t-1}(\frac{1}{3i+2}+\frac{1}{3i+3}+\frac{1}{3i+4})=\sum_{j=2}^{3t+1}\frac{1}{j}$。拆分调和和后，中间部分$\sum_{j=t+1}^{3t+1}\frac{1}{j}$可围绕$2t+1=p$对称配对：$\frac{1}{p-i}+\frac{1}{p+i}=\frac{2p}{p^2-i^2}$。 |
| 6 | 思维操作引导 | 0.3 | 现在有$\frac{1}{p}-2S_q=1-2p\sum\frac{1}{p^2-(i+1)^2}$。将求和写成单分数$\frac{U}{V}$，分析$V-2pU$模$p$的余数，并用$p$的素性证明$p\nmid V$ | 令$V=\prod(p^2-(i+1)^2)$，则$\frac{1}{p}-2S_q=\frac{V-2pU}{V}$。关键：$V-2pU\equiv V\pmod{p}$。因$0<i+1<p$且$p$素，每个因子$p^2-(i+1)^2$不被$p$整除，故$p\nmid V$。 |
| 7 | 能量传递引导 | 0.6 | 把所有步骤串起来完成证明：从$\frac{V-2pU}{V}=\frac{m}{n}$出发，利用同余和互质性推出$p\mid(m-n)$ | 交叉相乘得$(V-2pU)n=mV$。由$V-2pU\equiv V\pmod{p}$得$n(V-2pU-V)\equiv0\pmod{p}$，即$-2pUn\equiv(m-n)V\pmod{p}$。左端$\equiv0$，故$p\mid(m-n)V$。由$p\nmid V$和$p$素得$p\mid(m-n)$。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: constraint_satisfaction
- structure_features: 求和指标为模3余2的等差数列，部分分式分解后产生调和级数，对称配对围绕素数中心提取因子，整除性通过同余和互质性传递
- key_objects: 奇素数p, 求和S_q, 部分分式分解, 调和级数, 对称配对, 素性互质, 整除性传递

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["partial_fraction_decomposition", "reindexing_and_telescoping", "symmetric_pairing", "factor_extraction", "coprimality_argument"]
- primary_pattern: symmetric_pairing
- knowledge_required: ["部分分式分解1/(k(k+1)(k+2))", "调和级数重标号", "对称配对技术", "素数与整除性性质", "有理数表示为分数"]
- key_insight: 将调和级数项围绕素数p对称配对，每对提取出p因子，使分子模p同余于分母V，再用p∤V完成整除性传递

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct_sum_computation（直接求和计算）
- translation_to: partial_fraction_and_symmetric_pairing（部分分式分解+对称配对+互质性论证）
- translation_type: structural_transformation（将求和结构通过部分分式和重标号转化为可配对的调和级数结构）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["partial_fraction", "harmonic_sum", "symmetric_pairing", "prime_coprimality", "divisibility_transfer"]
- expected_ai_method: direct_calculation（bare AI会尝试直接计算求和或用模运算，不识别需要部分分式和对称配对的结构变换）
- correct_method: partial_fraction_decomposition with symmetric pairing and coprimality argument

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——constraint_satisfaction + direct_calculation + structural_transformation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新拓扑维度——三个维度足够区分
- 拓扑进化建议：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到倒数乘积求和与整除性声明，但未识别指标模式和p-q关系 | 描述结构：指标模式k≡2(mod3)，q=(3p-5)/2，p奇素数，需证p|(m-n) | 0.8 | 纯元认知观察 | false | {constraint_satisfaction, direct_calculation, structural_transformation} | [sum_structure, index_pattern, divisibility_target] |
| 2 | AI列出方法但未将部分分式识别为关键工具 | 列出所有方法：部分分式、望远镜、模运算、直接计算、归纳、对称配对 | 0.7 | 自由列举 | false | {constraint_satisfaction, enumeration_brute_force, method_problem_mismatch} | [approach_enumeration, partial_fraction_awareness] |
| 3 | AI尝试直接计算或模运算，陷入复杂代数 | 试直接通分或模p运算，观察困难 | 0.5 | 小尝试 | false | {constraint_satisfaction, direct_calculation, method_problem_mismatch} | [direct_computation, modular_arithmetic_limitation] |
| 4 | AI识别需要分解但不知道1/(k(k+1)(k+2))的部分分式恒等式 | 应用部分分式：2/(k(k+1)(k+2))=1/k-2/(k+1)+1/(k+2)，注意k=3i+2时连续三项结构 | 0.3 | 思维操作引导 | true | {constraint_satisfaction, algebraic_identity, knowledge_gap} | [partial_fraction_decomposition, telescoping_identity] |
| 5 | AI已分解求和但未看到重标号后的对称配对结构 | 重标号为连续调和和，围绕p=2t+1寻找对称配对 | 0.4 | 推进 | false | {constraint_satisfaction, direct_manipulation, structural_transformation} | [harmonic_sum_reindexing, symmetric_pairing, center_extraction] |
| 6 | AI有表达式1-2p·Σ1/(p²-i²)但未看到如何用素性完成证明 | 写成单分数(V-2pU)/V，分析V-2pU≡V(mod p)，用素性证p∤V | 0.3 | 思维操作引导 | true | {constraint_satisfaction, logical_deduction, knowledge_gap} | [single_fraction, modular_congruence, prime_coprimality, divisibility_transfer] |
| 7 | AI有所有部件，需组装最终论证 | 串联：部分分式→重标号→对称配对→因子提取→互质性→整除性结论 | 0.6 | 能量传递引导 | false | {constraint_satisfaction, logical_deduction, method_translation} | [argument_assembly, proof_completion] |

**全局pairs**：

1. path_feature型：
- scope: "从求和到整除性的完整解答路径"
- observation_point: null
- tell: "解答需要非显然的链条：部分分式→调和级数重标号→围绕p对称配对→互质性→整除性。没有任何单一步骤揭示完整路径。"
- hint: "关键结构洞察是：求和经部分分式分解后变为调和级数，可围绕素数p对称配对提取p因子"
- hint_level: 0.7
- generalizability: "high - 围绕素数中心的对称配对技术可推广到许多涉及调和级数的整除性问题"
- why_not_visible_locally: "对称配对结构只在部分分式分解和重标号两步变换后才出现。从原始求和1/(k(k+1)(k+2))中完全看不出围绕p的对称性。"
- tell_topology: {constraint_satisfaction, direct_calculation, structural_transformation}
- tell_small_concepts: [partial_fraction_chain, symmetric_pairing_emergence, multi_step_transformation]

2. implicit型：
- scope: "同余V-2pU≡V(mod p)及其在整除性传递中的角色"
- observation_point: "R6"
- tell: "表达式V-2pU有隐藏同余：模p等于V。这在结构中隐含但只在写成单分数后才可见。"
- hint: "当有(V-2pU)/V=m/n时，交叉相乘并利用同余V-2pU≡V(mod p)将整除性从分子传递到m-n"
- hint_level: 0.5
- generalizability: "medium - 提取因子并利用互质性的同余技巧在数论中常见但特定于此问题结构"
- why_not_visible_locally: "同余V-2pU≡V(mod p)只在将求和写成以V为分母的单分数后才可见。在此之前，模结构隐藏在倒数之和中。"
- tell_topology: {constraint_satisfaction, logical_deduction, knowledge_gap}
- tell_small_concepts: [congruence_extraction, coprimality_transfer, modular_arithmetic_hidden]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试直接计算求和或用模运算处理，不识别需要部分分式分解和对称配对的结构变换。会在代数运算中迷失，无法发现围绕p的对称配对结构，也无法将整除性论证组织成同余+互质的形式。"
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-path-injection"]
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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329440"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2010p5"
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
    '_key': '329440',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2010p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2010p5')
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
- problem_id: compfiles_usa2010p5
- solution_method_type: partial_fraction_decomposition
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类足够
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
