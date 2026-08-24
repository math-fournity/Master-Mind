# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: matharena_MathArena_smt_2025_0052
- **文件路径**: subagents-dirs/matharena_MathArena_smt_2025_0052/problem.lean
- **来源**: MathArena MathArena_smt_2025
- **ArangoDB progress记录_key**: 329855（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/matharena_MathArena_smt_2025_0052/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let f(x)=4x+a, g(x)=6x+b, h(x)=9x+c. S(a,b,c)是3^20个由f,g,h组合20次形成的函数集合，R(a,b,c)是S中不同函数的个数。求R(a,b,c)的最小值。
- 解答核心思路（1-2句话）：组合的斜率只取决于每个函数使用的次数（与顺序无关），用素因子分解4=2^2, 6=2·3, 9=3^2得斜率为2^p·3^(40-p)，p取0到40共41个不同值。a=b=c=0时同斜率函数重合，达到最小值41。
- 解答关键步骤列表：
  1. 观察斜率是各函数斜率的乘积，与顺序无关
  2. 素因子分解：4=2^2, 6=2·3, 9=3^2
  3. 斜率 = 2^(2k1+k2)·3^(k2+2k3)，令p=2k1+k2, q=k2+2k3
  4. p+q=40，p取0到40所有整数值，共41个不同斜率
  5. 不同斜率的函数总是不同的，故|R(a,b,c)|≥41
  6. a=b=c=0时所有同斜率函数重合，|R|=41，达到最小

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
| 1 | 纯元认知观察 | 0.3 | 描述题目结构：关键对象是什么，什么使两个组合相等，要求最小化什么 | S(a,b,c)有3^20个函数，R(a,b,c)计不同函数个数，求最小值。两个组合相等当且仅当斜率和常数项都相同 |
| 2 | 自由列举 | 0.4 | 列出理解"两个组合何时相同"的所有可能方向 | 计算组合、分析斜率（乘积）、分析常数项、试小情形、素因子分解、找特殊a,b,c |
| 3 | 小尝试 | 0.2 | 试算2次组合的斜率，注意什么 | f∘g和g∘f斜率都是24（4*6=6*4），斜率是乘积与顺序无关，但常数项不同 |
| 4 | 思维操作引导 | 0.6 | 用素因子分解表示斜率：4=2^2, 6=2·3, 9=3^2，k1+k2+k3=20 | 斜率=2^(2k1+k2)·3^(k2+2k3)，令p=2k1+k2, q=k2+2k3 |
| 5 | 思维操作引导 | 0.7 | p和q的关系？多少个不同斜率？证明0到40都可达 | p+q=40，p取0..40共41个不同斜率（唯一分解定理） |
| 6 | 推进 | 0.5 | 何时同斜率函数重合？什么a,b,c使|R|最小 | a=b=c=0时所有函数为x→(斜率)x，同斜率重合，|R|=41 |
| 7 | 能量传递引导 | 0.3 | 验证41是下界：证明|R(a,b,c)|≥41对所有a,b,c | 不同斜率→不同线性函数→总是不同，41个不同斜率→|R|≥41，a=b=c=0取等 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5

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
- structure_features: 线性函数组合，斜率是各函数斜率的乘积（与顺序无关），常数项与顺序有关。素因子分解4=2^2, 6=2·3, 9=3^2将斜率族压缩为一参数族2^p·3^(40-p)
- key_objects: 线性函数f,g,h; 组合集合S(a,b,c); 不同函数计数R(a,b,c); 斜率乘积; 素因子分解2^p·3^q

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [structural_reduction, prime_factorization, extremal_principle, small_case_analysis]
- primary_pattern: structural_reduction（将3^20组合计数问题归约为41个不同斜率的计数）
- knowledge_required: [线性函数组合, 素因子分解, 唯一分解定理, 极值原理]
- key_insight: 斜率只取决于各函数使用次数（与顺序无关），4=2^2, 6=2·3, 9=3^2使斜率族为一参数族2^p·3^(40-p)，共41个不同值，既是不同斜率数也是|R|的最小值

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 组合枚举（直接计算3^20个组合函数）
- translation_to: 斜率计数（通过素因子分解将问题归约为计数不同斜率）
- translation_type: structural_reduction（结构归约：从巨大的组合空间归约到一参数斜率族）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: [prime_factorization_of_slopes, order_independence, exponent_constraint_p+q=40, minimum_at_a=b=c=0]
- expected_ai_method: enumeration_brute_force — AI可能尝试枚举或直接计算3^20个组合函数，迷失在巨大搜索空间中
- correct_method: structural_reduction — 将问题从计数不同组合归约为计数不同斜率（通过素因子分解），然后取a=b=c=0达到最小值

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial, ai_method_type=enumeration_brute_force, gap_type=structural_transformation均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [ ] 无需进化建议

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
- bare_ai_expected: fail
- bare_ai_error_prediction: AI可能尝试枚举或直接计算3^20个组合函数，迷失在巨大搜索空间中。或者分析常数项而未认识到斜率归约，或未使用素因子分解计数不同斜率。也可能未意识到a=b=c=0达到最小值。
- suitable_for_poc: [POC-VMS-hint-injection, POC-VMS-tell-detection]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: matharena_MathArena_smt_2025_0052
- solution_method_type: structural_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类足够
- 是否遇到异常: 否（题目Lean文件中informal_statement被截断，但结合Answer=41可完整重建问题和解答）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
