# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000120
- **文件路径**: subagents-dirs/omni_math_000120/problem.lean
- **来源**: AoPS omni_math (china_national_olympiad)
- **ArangoDB progress记录_key**: 329991（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000120/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：定义数列(a_n),(b_n)，a_n,b_n>0，a_{n+1}=a_n - 1/(1+Σ_{i=1}^n 1/a_i)，b_{n+1}=b_n + 1/(1+Σ_{i=1}^n 1/b_i)。1) 若a_{100}b_{100}=a_{101}b_{101}，求a_1-b_1；2) 若a_{100}=b_{99}，比较a_{100}+b_{100}与a_{101}+b_{101}的大小。答案：199。
- 解答核心思路（1-2句话）：通过代数操作递推式，证明a_n是等比数列（a_{n+1}²=a_n·a_{n+2}，公比r=a₁/(1+a₁)），b_n的相邻项比值有闭式（b_{n+1}/b_n=(2n+b₁)/(2n+b₁-1)，由不变量b_n·B_n=2n+b₁-1证明）。利用条件a₁₀₀b₁₀₀=a₁₀₁b₁₀₁分解为比值乘积等于1，解得a₁-b₁=199。
- 解答关键步骤列表：
  1. 定义A_n=1+Σ_{i=1}^n 1/a_i，由递推得1/A_n=a_n-a_{n+1}，即A_n=1/(a_n-a_{n+1})
  2. 利用A_{n+1}=A_n+1/a_{n+1}和A_{n+1}=1/(a_{n+1}-a_{n+2})，交叉相乘得a_{n+1}²=a_n·a_{n+2}，故a_n等比
  3. 求出a_n公比r=a₁/(1+a₁)，故a_n=a₁·r^{n-1}
  4. 对b_n类似定义B_n=1+Σ1/b_i，由递推得B_n=1/(b_{n+1}-b_n)
  5. 猜想并归纳证明不变量b_n·B_n=2n+b₁-1，从而b_{n+1}/b_n=(2n+b₁)/(2n+b₁-1)
  6. 条件a₁₀₀b₁₀₀=a₁₀₁b₁₀₁等价于(a₁₀₁/a₁₀₀)·(b₁₀₁/b₁₀₀)=1
  7. 代入r=a₁/(1+a₁)和b₁₀₁/b₁₀₀=(200+b₁)/(199+b₁)，解方程得a₁-b₁=199

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
| 1 | 纯元认知观察 | 0.7 | 观察这道题的结构：两个递推数列a_n和b_n，一个递减一个递增，递推式中都含有倒数的部分和。条件a_{100}b_{100}=a_{101}b_{101}连接了两个数列。请描述题目的已知量、未知量和结构特征。 | 已知：两个递推数列的定义（含部分和），一个乘积条件。未知：a_1-b_1的值。结构特征：a_n递减、b_n递增，递推式中的部分和Σ1/a_i和Σ1/b_i是关键障碍——它们使得递推不是简单的线性递推。条件在n=100/101处给出，暗示需要闭式或比值关系。 |
| 2 | 自由列举 | 0.6 | 面对这种含部分和的递推数列问题，列出你能想到的所有可能攻克方向。 | 方向包括：①直接数值计算前几项找规律；②定义辅助量A_n=1+Σ1/a_i简化递推式；③寻找不变量或守恒量；④证明数列有特殊结构（等比/等差）；⑤对递推式做代数变形消去部分和；⑥利用条件a_{100}b_{100}=a_{101}b_{101}分解为比值乘积；⑦数学归纳法证明通项公式。 |
| 3 | 小尝试 | 0.3 | 试着直接计算a_n和b_n的前几项（取a_1=2, b_1=3），看看能否发现规律。 | 计算得a: 2, 4/3, 8/9,...发现a_2²=a_1·a_3=16/9，可能是等比数列，公比2/3。b: 3, 15/4, 35/8,...比值5/4, 7/6,...不是等比但比值有规律。数值尝试能发现a等比的猜想，但b的规律不够明显，且无法直接推广到n=100。 |
| 4 | 思维操作引导 | 0.2 | 定义A_n=1+Σ_{i=1}^n 1/a_i。由递推式得1/A_n=a_n-a_{n+1}，即A_n=1/(a_n-a_{n+1})。现在利用A_{n+1}=A_n+1/a_{n+1}和A_{n+1}=1/(a_{n+1}-a_{n+2})，将两个表达式联立，交叉相乘，推导三项递推关系。 | A_{n+1}=1/(a_n-a_{n+1})+1/a_{n+1}=a_n/[a_{n+1}(a_n-a_{n+1})]，又A_{n+1}=1/(a_{n+1}-a_{n+2})。联立得a_{n+1}(a_n-a_{n+1})=a_n(a_{n+1}-a_{n+2})，化简得a_{n+1}²=a_n·a_{n+2}。故a_n是等比数列！ |
| 5 | 推进 | 0.4 | 很好，a_n是等比数列。求出公比r用a_1表示，然后对b_n用类似的辅助量方法分析——定义B_n=1+Σ1/b_i，看看能否找到b_n的比值规律。 | a_n公比r=a_1/(1+a_1)。对b_n：B_n=1/(b_{n+1}-b_n)，B_{n+1}=(2b_{n+1}-b_n)/[b_{n+1}(b_{n+1}-b_n)]。b_n不是等比，但可以计算b_{n+1}/b_n=b_n+1/b_n·B_n。需要进一步找不变量。 |
| 6 | 思维操作引导 | 0.2 | 对b_n，计算b_n·B_n的前几项值（用b_1=2验证）：b_1·B_1=b_1+1, b_2·B_2=2·2+b_1-1=5。猜想b_n·B_n=2n+b_1-1，用归纳法证明，然后由此推出b_{n+1}/b_n的闭式。 | 猜想b_n·B_n=2n+b_1-1。归纳：基例b_1·B_1=b_1(1+1/b_1)=b_1+1=2·1+b_1-1✓。归纳步：若b_n·B_n=2n+b_1-1，则b_{n+1}=b_n+b_n/(2n+b_1-1)=b_n·(2n+b_1)/(2n+b_1-1)，可推出b_{n+1}·B_{n+1}=2(n+1)+b_1-1。故b_{n+1}/b_n=(2n+b_1)/(2n+b_1-1)。 |
| 7 | 能量传递引导 | 0.3 | 现在两个数列的比值都有了闭式。条件a_{100}b_{100}=a_{101}b_{101}可以分解为(a_{101}/a_{100})·(b_{101}/b_{100})=1。代入两个比值公式，解方程求a_1-b_1。你已经在正确的路上，完成最后一步！ | a_{101}/a_{100}=r=a_1/(1+a_1)，b_{101}/b_{100}=(200+b_1)/(199+b_1)。条件：[a_1/(1+a_1)]·[(200+b_1)/(199+b_1)]=1。展开：(1+a_1)(199+b_1)=a_1(200+b_1)，化简得199+b_1=a_1，即a_1-b_1=199。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 两个递推数列（一减一增），递推式中含倒数部分和，通过乘积条件在特定指标处连接，需推导闭式后求解参数关系
- key_objects: ["a_n（递减等比数列）", "b_n（递增数列，比值有闭式）", "A_n=1+Σ1/a_i（辅助量）", "B_n=1+Σ1/b_i（辅助量）", "部分和Σ1/a_i, Σ1/b_i", "乘积条件a_{100}b_{100}=a_{101}b_{101}"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["代数变形消去部分和", "等比数列识别（三项递推a_{n+1}²=a_n·a_{n+2}）", "不变量发现（b_n·B_n=2n+b₁-1）", "归纳法证明", "比值乘积分解条件"]
- primary_pattern: 代数变形消去部分和
- knowledge_required: ["等比数列判定", "递推数列与辅助量", "数学归纳法", "部分和与递推的关系", "代数恒等变形"]
- key_insight: 通过定义辅助量A_n=1+Σ1/a_i将递推式改写为A_n=1/(a_n-a_{n+1})，联立A_{n+1}的两个表达式交叉相乘得a_{n+1}²=a_n·a_{n+2}，从而识别出a_n等比；对b_n发现不变量b_n·B_n=2n+b₁-1给出比值闭式。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 含部分和的递推数列语言
- translation_to: 等比数列+比值乘积的代数方程语言
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["辅助量A_n定义", "等比数列三项判定", "不变量b_n·B_n", "比值乘积分解", "交叉相乘消部分和"]
- expected_ai_method: direct_calculation——bare AI会尝试直接计算数列项或建立方程，不会想到通过辅助量代数变形消去部分和来发现隐藏的等比结构
- correct_method: 定义辅助量A_n/B_n消去部分和，推导三项递推关系识别等比结构，发现b_n的不变量得到比值闭式，最后用比值乘积分解条件求解

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(characterization)/ai_method_type(direct_calculation)/gap_type(structural_transformation)都能归入已有的拓扑类别
- [x] 粒度是否一致——标注值和已有值的粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无

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
- bare_ai_error_prediction: bare AI会尝试直接计算数列前几项或对递推式做表面变形，但不会想到定义辅助量A_n=1+Σ1/a_i并通过联立A_{n+1}的两个表达式来消去部分和。即使数值尝试发现a_n可能等比，也无法严格证明，更无法发现b_n的不变量b_n·B_n=2n+b₁-1。最终卡在无法将条件a_{100}b_{100}=a_{101}b_{101}转化为可解的方程。
- suitable_for_poc: ["hint注入有效性验证（验证辅助量定义提示能否引导AI发现等比结构）", "tell识别验证（识别AI在递推变形处未分叉到辅助量路线的tell）", "多轮引导验证（验证7轮QA序列能否引导bare AI到达正确解答）"]
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
2. 更新`problem_extraction_progress`集合中`_key="329991"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000120"
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
    '_key': '329991',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000120',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000120')
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
- problem_id: omni_math_000120
- solution_method_type: algebraic_manipulation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类(characterization/direct_calculation/structural_transformation)足够覆盖
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
