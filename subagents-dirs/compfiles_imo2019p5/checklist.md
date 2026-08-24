# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2019p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2019P5.lean
- **来源**: IMO 2019 P5
- **ArangoDB progress记录_key**: 329252（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2019P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：n个硬币排成一行，每个正面或反面。操作：如果有k>0个正面，翻转第k个硬币；否则停止。证明过程总终止，并求所有2^n个初始配置的平均步数。
- 解答核心思路（1-2句话）：构造势函数meas=2*weightedSum-numHeads^2（weightedSum为正面硬币1-based位置之和，numHeads为正面数量），证明它非负且每步恰好减少1，因此等于步数L(c)。再用线性期望计算平均步数=n(n+1)/4。
- 解答关键步骤列表：
  1. 定义numHeads（正面数量）、weightedSum（正面位置加权和）、meas=2*weightedSum-numHeads^2
  2. 证明组合不等式：k个正面位置之和≥k(k+1)/2（用orderEmbOfFin）
  3. 由此推出meas≥0（非负性）
  4. 证明meas=0当且仅当numHeads=0（全反面=终止状态）
  5. 证明每步meas恰好减少1（分析翻转第k个硬币对weightedSum和numHeads的影响）
  6. 由归纳得meas(step^m c)=meas c - m，故L(c)=meas(c)=步数
  7. 计算sum(L(c))：用线性期望分别计算E[weightedSum]和E[numHeads^2]
  8. E[weightedSum]=2^(n-1)*T（T=n(n+1)/2），E[numHeads^2]=n*2^(n-1)+n(n-1)*2^(n-2)
  9. 最终：4*sum(L)=2^n*n*(n+1)，平均步数=n(n+1)/4

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
| 1 | 纯元认知观察 | 0.3 | 描述这个问题的结构：操作规则是什么？终止条件是什么？需要证明什么和计算什么？ | n个硬币排成一行，每个正面或反面。操作：若有k>0个正面，翻转第k个硬币。需证明过程总终止，并求所有2^n个初始配置的平均步数。 |
| 2 | 自由列举 | 0.4 | 列出所有可能用来证明终止性和计算平均步数的方向 | (1)直接模拟小例子找规律(2)寻找递减的不变量/势函数(3)分析操作对状态的影响(4)用概率/期望的线性性质(5)建立递推关系 |
| 3 | 小尝试 | 0.2 | 试一个方向：直接模拟n=1,2,3的小例子，看看步数有什么规律 | n=1: 平均0.5=1*2/4; n=2: 四种配置步数各异，平均1.5=2*3/4; n=3: 平均3=3*4/4。猜测平均步数=n(n+1)/4，但证明终止性需要更深的结构。 |
| 4 | 思维操作引导 | 0.6 | 为了证明终止性，考虑寻找一个势函数(measure)使其在每步恰好减少1。这个measure应该与正面硬币的位置和数量有关。尝试构造这样的measure。 | 考虑weightedSum=正面硬币位置之和，numHeads=正面数量。尝试measure=2*weightedSum-numHeads^2。需要验证它非负且每步减少1。 |
| 5 | 思维操作引导 | 0.5 | 验证measure=2*weightedSum-numHeads^2的非负性。提示：k个正面的位置之和至少为多少？ | k个正面硬币的1-based位置之和至少为1+2+...+k=k(k+1)/2。因此2*weightedSum>=k(k+1)>=k^2，所以measure>=0。 |
| 6 | 推进 | 0.4 | 验证measure在每步恰好减少1。考虑翻转第k个硬币(k=numHeads)时，weightedSum和numHeads如何变化？ | 翻转第k个硬币：若正面→反面，numHeads减1，weightedSum减k；若反面→正面，numHeads增1，weightedSum增k。两种情况下measure都减少1。 |
| 7 | 能量传递引导 | 0.5 | 现在measure=L(c)=步数。计算所有2^n个配置的L(c)之和，利用线性期望的性质分别计算weightedSum和numHeads^2的期望。 | E[weightedSum]=n(n+1)/4(每个位置以1/2概率为正面)，E[numHeads^2]=n(n+1)/4(用Var+Mean^2)。所以E[L]=2*n(n+1)/4-n(n+1)/4=n(n+1)/4。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.9
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
- problem_type: discrete_combinatorial
- structure_features: 离散状态空间上的确定性过程，操作规则依赖当前状态（正面数量k决定翻转第k个硬币），需证明终止性并计算平均步数。核心是构造势函数证明终止性，再利用线性期望计算平均值。
- key_objects: 硬币配置(Fin n → Bool), 正面数量(numHeads), 加权位置和(weightedSum), 势函数(meas=2*weightedSum-numHeads^2), 步数函数L, 翻转操作step

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["势函数/不变量构造", "小例子枚举找规律", "线性期望分解", "组合不等式估计", "归纳法"]
- primary_pattern: 势函数构造
- knowledge_required: ["势函数/不变量方法", "线性期望性质", "组合不等式(排序不等式)", "归纳法", "概率论基础(独立事件的期望)"]
- key_insight: 构造势函数meas=2*weightedSum-numHeads^2，它非负且每步恰好减少1，因此等于步数L(c)，再用线性期望分别计算各分量的期望

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接模拟/枚举（小例子的经验观察）
- translation_to: 势函数/不变量分析（代数结构构造）
- translation_type: method_translation（从经验枚举翻译到代数不变量构造）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: enumeration_brute_force, gap_type: method_translation}
- tell_small_concepts: ["势函数", "不变量", "线性期望", "组合不等式", "加权位置和", "正面数量", "终止性", "平均步数"]
- expected_ai_method: 直接模拟小例子找规律，尝试用递推关系或枚举法解决问题，但难以构造出正确的势函数
- correct_method: 构造势函数meas=2*weightedSum-numHeads^2证明终止性和步数，再用线性期望计算平均值

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以，discrete_combinatorial/enumeration_brute_force/method_translation均已有
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部pairs详见profile.json中的tell_hint_pairs字段**

**全局pairs详见profile.json中的global_tell_hint_pairs字段**

全局pair摘要：
1. path_feature型：势函数meas=2*weightedSum-numHeads^2的构造——从"每步减少1"反推特定代数结构，局部视角不可见
2. path_feature型：组合不等式k(k+1)/2的运用——从排序角度理解非负性，纯代数操作中不可见
3. implicit型：线性期望分解策略——meas的线性结构蕴含分量独立计算，局部步骤中不可见

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "marginal"
- bare_ai_error_prediction: AI可能从小例子正确猜到平均步数=n(n+1)/4，但在证明终止性时可能尝试错误的势函数（如只用weightedSum或只用numHeads），无法找到每步恰好减少1的measure。也可能尝试直接归纳证明终止性而不构造势函数。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-bottleneck-identification"]
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
2. 更新`problem_extraction_progress`集合中`_key="329252"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2019p5"
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
    '_key': '329252',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2019p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2019p5')
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
- problem_id: compfiles_imo2019p5
- solution_method_type: potential_function_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（2个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类（discrete_combinatorial / enumeration_brute_force / method_translation等）完全够用
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
