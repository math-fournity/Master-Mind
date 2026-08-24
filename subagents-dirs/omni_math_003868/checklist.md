# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003868
- **文件路径**: subagents-dirs/omni_math_003868/problem.lean
- **来源**: AoPS omni_math (imo)
- **ArangoDB progress记录_key**: 333747（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003868/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Find all f:(0,∞)→(0,∞) such that (f(w)²+f(x)²)/(f(y²)+f(z²)) = (w²+x²)/(y²+z²) for all positive reals w,x,y,z with wx=yz.
- 解答核心思路（1-2句话）：通过对称代换w=y,x=z发现f(x)²-f(x²)为常数（=0），得f(x²)=f(x)²；简化后令g(x)=f(x)/x，因式分解得逐点f(x)∈{x,1/x}；再用P(x,y,1,xy)证明全局一致性。
- 解答关键步骤列表：
  1. P(1,1,1,1) → f(1)=1
  2. P(a,b,a,b) → f(a)²+f(b)²=f(a²)+f(b²) → f(x²)=f(x)²
  3. 简化原方程：(f(w)²+f(x)²)/(f(y)²+f(z)²)=(w²+x²)/(y²+z²)，比值(f(a)²+f(b)²)/(a²+b²)只依赖乘积ab
  4. 令g(x)=f(x)/x，用a=b=√t和a=1两种方式表达h(t)，建立方程u²(1+x⁴)=1+x⁴u⁴
  5. 因式分解：(u²-1)(x⁴u²-1)=0 → f(x)=x或f(x)=1/x（逐点）
  6. P(x,y,1,xy)证明混合选择矛盾 → f全局为f(x)=x或f(x)=1/x

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | 描述这个函数方程的结构——已知什么，未知什么，约束条件wx=yz起什么作用？ | 识别出这是函数方程，定义域(0,∞)→(0,∞)，约束wx=yz连接分子分母的变量，需要找所有满足条件的f。分子是f(w)²+f(x)²，分母是f(y²)+f(z²)，右侧结构类似但用原始变量。 |
| 2 | 自由列举 | 0.8 | 列出所有可能的入手方向——你可以用哪些代换来简化这个方程？ | 令w=x=y=z=1；令y=z=1；令w=y且x=z；令w=x且y=z；利用wx=yz做参数化（如令y=w,z=x）；尝试f(x)=x或f(x)=1/x验证等。 |
| 3 | 小尝试 | 0.4 | 试试令w=y, x=z（即wx=yz自动满足），看看能得到什么。 | 得到(f(w)²+f(x)²)/(f(w²)+f(x²))=1，即f(w)²+f(x)²=f(w²)+f(x²)。这说明f(x)²-f(x²)是常数，但还需要确定这个常数。 |
| 4 | 思维操作引导 | 0.5 | 从f(x)²-f(x²)=常数出发，用w=x=1确定这个常数，然后利用f(x²)=f(x)²将原方程简化。 | 令x=1：f(1)²-f(1)=常数；由P(1,1,1,1)得f(1)=1，常数=0。所以f(x²)=f(x)²。原方程变为(f(w)²+f(x)²)/(f(y)²+f(z)²)=(w²+x²)/(y²+z²)，即比值(f(a)²+f(b)²)/(a²+b²)在ab=cd时相等，只依赖于乘积ab。 |
| 5 | 思维操作引导 | 0.6 | 令g(x)=f(x)/x，将简化后的方程用g表示，然后利用a=b=√t和a=1两种方式表达h(t)，建立关于g的方程并因式分解。 | h(t)=(f(√t)/√t)²=g(√t)²，又h(t)=(1+f(t)²)/(1+t²)。令t=x²得(g(x))²=(1+f(x)⁴)/(1+x⁴)。设u=g(x)，u²(1+x⁴)=1+x⁴u⁴，因式分解得(u²-1)(x⁴u²-1)=0，所以f(x)=x或f(x)=1/x。 |
| 6 | 推进 | 0.5 | 现在知道每个x处f(x)∈{x,1/x}，但f可能在不同点取不同选择。用P(x,y,1,xy)证明f必须全局一致。 | 假设f(a)=a, f(b)=1/b (b≠1)，代入P(a,b,1,ab)：LHS=(a²+1/b²)/(1+1/(a²b²))，化简后与RHS=(a²+b²)/(1+a²b²)比较，导出1=b⁴即b=1，矛盾。所以f全局为f(x)=x或f(x)=1/x。 |
| 7 | 能量传递引导 | 0.8 | 验证两个解都满足原方程，然后总结完整的解答。 | f(x)=x：LHS=(w²+x²)/(y²+z²)=RHS ✓。f(x)=1/x：LHS=(1/w²+1/x²)/(1/y²+1/z²)=(x²+w²)/(w²x²)·(y²z²)/(z²+y²)，由wx=yz得=(w²+x²)/(y²+z²) ✓。解答完整。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 函数方程，约束wx=yz连接分子分母，分子为f的平方和，分母为f在平方处的值的和，右侧为原始变量的平方和比值；f定义域和值域均为(0,∞)
- key_objects: [f:(0,∞)→(0,∞), 约束wx=yz, 比值方程(f(w)²+f(x)²)/(f(y²)+f(z²))=(w²+x²)/(y²+z²)]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [特殊化代入, 不变量识别, 变量替换降维, 因式分解分类, 全局一致性反证]
- primary_pattern: 不变量识别
- knowledge_required: [函数方程特殊值代入技巧, 多项式因式分解, 比值不变量概念, 函数方程全局一致性验证]
- key_insight: 令w=y,x=z发现f(x)²-f(x²)是不变量（常数0），从而f(x²)=f(x)²将四变量方程降维为二变量比值方程，再用g(x)=f(x)/x代换因式分解得到逐点解

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 约束比值方程（带乘积约束的四变量比值方程）
- translation_to: 逐点函数值分类+全局一致性验证（每个x处f(x)∈{x,1/x}，再证明全局一致）
- translation_type: structural_transformation（通过不变量识别将四变量约束方程转化为单变量代数方程，再通过反证法验证全局一致性）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: [不变量识别, f(x²)=f(x)², 比值依赖乘积, g(x)=f(x)/x替换, 因式分解(u²-1)(x⁴u²-1), 全局一致性反证]
- expected_ai_method: direct_manipulation（bare AI可能直接尝试各种代换但缺乏系统性的不变量识别策略）
- correct_method: 不变量识别+变量替换+因式分解（系统性地从对称代换提取不变量，降维后用g(x)替换做代数因式分解）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=direct_manipulation, gap_type=structural_transformation均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI可能能找到f(1)=1和f(x²)=f(x)²，但在从简化方程到g(x)=f(x)/x替换和因式分解这一步缺乏方向性，可能卡在代数变形中无法得到(u²-1)(x⁴u²-1)=0的因式分解；也可能在得到逐点解后忽略全局一致性验证，直接报告"f(x)=x或f(x)=1/x"而不证明混合选择不可能
- suitable_for_poc: ["tell端去特化验证", "hint端脉络注入验证", "思维操作引导效果验证"]
- discriminates_levels: True

---

## Step 9: 输出完整profile JSON [x]

完整JSON已写入 `subagents-dirs/omni_math_003868/profile.json`。所有字段已逐项检查。

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
2. 更新`problem_extraction_progress`集合中`_key="333747"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003868"
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
    '_key': '333747',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003868',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003868')
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
- problem_id: omni_math_003868
- solution_method_type: 不变量识别+变量替换+因式分解
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类够用
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
