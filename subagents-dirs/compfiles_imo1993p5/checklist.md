# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1993p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1993P5.lean
- **来源**: IMO 1993 P5
- **ArangoDB progress记录_key**: 329145（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1993P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Does there exist a function f: ℕ → ℕ such that (i) f(1) = 2, (ii) f(f(n)) = f(n) + n for all n ∈ ℕ, (iii) f(n+1) > f(n) for all n ∈ ℕ (strictly increasing)?
- 解答核心思路（1-2句话）：Yes. Define f(n) = round(φn) where φ = (1+√5)/2 is the golden ratio. The key is that φ² = φ + 1 mirrors the functional equation f(f(n)) = f(n) + n, and rounding errors cancel to give exact integer equality.
- 解答关键步骤列表：
  1. Recognize that if f(n) ≈ φn, then f(f(n)) ≈ φ²n = (φ+1)n = φn + n = f(n) + n, using φ² = φ + 1
  2. Define f(n) = round(φn) = Int.natAbs(round(φ·n)) to map ℕ → ℕ
  3. Prove f(1) = 2: round(φ) = 2 since 2 < √5 < 3 implies φ ∈ (2, 2.5)
  4. Prove f(f(n)) = f(n) + n: Show |f(f(n)) - (f(n) + n)| < 1 by decomposing error as [f(f(n)) - φ·f(n)] + (φ-1)·[f(n) - φn], each bounded by 1/2, total < 1. Since both sides are integers, difference must be 0.
  5. Prove f strictly increasing: φ > 1 ensures round(φ(n+1)) > round(φn)

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：有哪些条件？哪个条件是核心结构约束？ | 三个条件：(i) f(1)=2 初始条件，(ii) f(f(n))=f(n)+n 自引用泛函方程，(iii) f严格递增。核心结构约束是(ii)，因为它涉及f的自复合，是定义f本质行为的关键。(iii)是辅助约束，(i)是边界条件。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的构造方向：线性函数、递归构造、连分数、数论方法等 | 1) 线性函数 f(n)=an+b；2) 递归构造：从f(1)=2出发逐步定义；3) 分段线性；4) 利用Beatty序列；5) 连分数相关构造；6) 枚举小值找规律 |
| 3 | 小尝试 | 0.4 | 试线性函数 f(n)=an+b。代入f(f(n))=f(n)+n，看能得到什么方程？ | f(f(n))=a(an+b)+b=a²n+ab+b。需要等于(an+b)+n=(a+1)n+b。所以a²=a+1且ab=0。由f(1)=2得a+b=2。若b=0则a=2但4≠3。若a=0则b=2但0≠1。线性函数在整数上不行，但a²=a+1的解是φ=(1+√5)/2（黄金比例）！ |
| 4 | 思维操作引导 | 0.5 | a²=a+1的解是黄金比例φ。虽然φ是无理数，但f(n)=round(φn)可以将实数映射到自然数。思考：rounding的误差是多少？如何利用这个误差？ | round(x)的误差≤1/2，即|round(φn)-φn|≤1/2。关键问题：f(f(n))中两次rounding的误差能否抵消？需要分析复合rounding的误差传播。 |
| 5 | 推进 | 0.3 | 计算f(f(n))-(f(n)+n)的误差分解。提示：利用φ²=φ+1将误差拆分为两项 | f(f(n))-(f(n)+n) = [f(f(n))-φ·f(n)] + (φ-1)·[f(n)-φn]。第一项是round(φ·f(n))的误差≤1/2，第二项是(φ-1)乘以round(φn)的误差≤(φ-1)/2。总和≤1/2+(φ-1)/2=φ/2<1（因为φ<2）。 |
| 6 | 思维操作引导 | 0.4 | 你已经得到|f(f(n))-(f(n)+n)|<1。f(f(n))和f(n)+n都是什么类型的数？由此能得出什么结论？ | 两者都是自然数（整数），所以它们的差是整数。一个绝对值小于1的整数只能是0。因此f(f(n))=f(n)+n对所有n成立。 |
| 7 | 能量传递引导 | 0.6 | 验证剩余两个条件：f(1)=2和f严格递增。你已经有完整的工具了。 | f(1)=round(φ)=round(1.618...)=2 ✓。严格递增：φ>1所以φ(n+1)>φn+1，round(φ(n+1))≥round(φn)+1>round(φn) ✓。三个条件全部满足，存在性得证。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.4+0.5+0.3+0.4+0.6 = 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R3（识别a²=a+1为黄金比例方程）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5（误差分解利用φ²=φ+1）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 自引用泛函方程 f(f(n))=f(n)+n（f的自复合），单调性约束，初始条件，需要构造性证明存在性
- key_objects: [f: ℕ → ℕ, 黄金比例 φ=(1+√5)/2, rounding函数 round(φn), 泛函方程 f(f(n))=f(n)+n, 特征方程 a²=a+1]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["continuous_approximation", "algebraic_characterization", "rounding_error_analysis", "integer_uniqueness"]
- primary_pattern: continuous_approximation（用连续函数φn逼近离散函数，再处理离散化误差）
- knowledge_required: ["黄金比例方程 φ²=φ+1", "rounding/floor函数及其误差界", "Beatty序列", "泛函方程", "整数唯一性论证"]
- key_insight: 泛函方程f(f(n))=f(n)+n的代数结构与φ²=φ+1同构，因此f(n)=round(φn)满足方程——两次rounding的误差通过φ²=φ+1分解后总和<1，而整数差<1必为0

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 连续实值函数 f(n)=φn（实数域上的线性函数）
- translation_to: 离散自然数函数 f(n)=round(φn)（自然数域上的取整函数）
- translation_type: continuous_to_discrete_rounding（连续到离散的取整翻译，核心是误差控制使泛函方程在离散域精确成立）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["golden ratio", "functional equation self-composition", "rounding error cancellation", "characteristic equation a²=a+1", "integer uniqueness", "Beatty sequence"]
- expected_ai_method: direct_manipulation（bare AI会尝试从f(1)=2出发递归构造，或枚举小值找规律，但不会识别泛函方程与黄金比例的代数同构）
- correct_method: continuous_analytic（用连续函数φn逼近，再通过rounding和误差分析实现离散化）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type=structural_existence、ai_method_type=direct_manipulation、gap_type=method_translation均可归入已有拓扑类别
- [x] 粒度是否一致——标注值与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无。已有拓扑分类足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详见profile.json中的tell_hint_pairs字段**

**全局pairs详见profile.json中的global_tell_hint_pairs字段**

全局pair 1 (path_feature型):
- scope: "从题目到黄金比例构造的完整路径"
- tell: "泛函方程f(f(n))=f(n)+n的代数结构与φ²=φ+1同构，但这个连接只在尝试线性ansatz并识别特征方程后才可见"
- hint: "先试f(n)=an，推导a²=a+1，识别黄金比例，再用rounding处理离散化"
- why_not_visible_locally: "泛函方程与黄金比例的连接需要先尝试线性ansatz（在整数上失败）再识别特征方程a²=a+1为黄金比例方程。没有任何单步能揭示这个连接——它是路径级洞察，从尝试→识别→适配的序列中涌现"

全局pair 2 (implicit型):
- scope: "f(f(n))=f(n)+n的证明"
- observation_point: "R5-R6"
- tell: "两次rounding的误差通过φ²=φ+1分解后telescope，结果为整数且绝对值<1故必为0"
- hint: "用φ²=φ+1分解误差，bound总误差<1，用整数唯一性论证"
- why_not_visible_locally: "误差抵消依赖于φ²=φ+1这个特定代数恒等式来分解误差项，这在任何单步中都不可见。整数唯一性论证是独立的逻辑步骤，只有在误差bound建立后才变得相关"

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试从f(1)=2出发递归构造f(2), f(3)...，或枚举小值找规律，但不会识别泛函方程f(f(n))=f(n)+n与黄金比例方程φ²=φ+1的代数同构。可能尝试证明不存在性，或陷入无限递归构造而无法收敛到闭式表达式。"
- suitable_for_poc: ["tell_hint_injection", "topology_matching", "knowledge_gap_detection", "path_feature_retrieval"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/compfiles_imo1993p5/profile.json`

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

- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329145"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1993p5"
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
    '_key': '329145',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1993p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1993p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [ ] 成功 / [ ] 失败
- 验证结果: [ ] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo1993p5
- solution_method_type: continuous_analytic
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类足够覆盖
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
