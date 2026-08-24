# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2009p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2009P6.lean
- **来源**: USA 2009 P6
- **ArangoDB progress记录_key**: 329437（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2009P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let $s_1, s_2, s_3, \ldots$ be an infinite, nonconstant sequence of rational numbers. Suppose $t_1, t_2, t_3, \ldots$ is also an infinite, nonconstant sequence of rationals with $(s_i - s_j)(t_i - t_j) \in \mathbb{Z}$ for all $i, j$. Prove there exists rational $r$ such that $(s_i - s_j)r \in \mathbb{Z}$ and $(t_i - t_j)/r \in \mathbb{Z}$ for all $i, j$.
- 解答核心思路（1-2句话）：通过归一化将问题化简为 $s_a = t_a = 0, s_b = 1, t_b = N$ 的情形，用 p-adic 赋值引理证明所有 $t_i$ 是整数，取 $d = \gcd(t_i)$，再用 p-adic 赋值界证明 $s_i \cdot d$ 是整数，最后缩放回原序列。
- 解答关键步骤列表：
  1. 找到 $a, b$ 使 $(s_a - s_b)(t_a - t_b) \neq 0$（利用非恒常性）
  2. 归一化：令 $w = s_b - s_a$，$s'_i = (s_i - s_a)/w$，$t'_i = (t_i - t_a) \cdot w$，则 $s'_a = t'_a = 0$，$s'_b = 1$，$t'_b = N$（非零整数）
  3. 证明 $s'_i t'_i \in \mathbb{Z}$（取 $j = a$）
  4. 证明交叉项 $s'_i t'_j + s'_j t'_i \in \mathbb{Z}$（代数恒等式）
  5. 证明 $N s'_i + t'_i \in \mathbb{Z}$（取 $j = b$）
  6. 关键引理：若 $ab \in \mathbb{Z}$ 且 $na + b \in \mathbb{Z}$（$n \neq 0$），则 $b \in \mathbb{Z}$（p-adic 赋值证明）
  7. 用引理证明所有 $t'_i \in \mathbb{Z}$
  8. 取 $d = \gcd$ of all $t'_i$，证明 $d$ 的每个 p-adic 赋值在某非零 $t'_j$ 处取到
  9. 赋值界：对每个素数 $p$，用 $s'_i t'_j + s'_j t'_i \in \mathbb{Z}$ 证明 $v_p(s'_i) \geq -v_p(d)$
  10. 故 $s'_i \cdot d \in \mathbb{Z}$，$t'_i / d \in \mathbb{Z}$
  11. 缩放回原序列：$r = d / w$

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
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知条件是什么？要证明什么？$(s_i - s_j)(t_i - t_j) \in \mathbb{Z}$ 对所有 $i,j$ 成立意味着什么？ | 题目给出两个无穷非恒常有理数序列 $s_i, t_i$，条件是任意两项差的乘积为整数。需要证明存在一个有理数 $r$ 使得 $(s_i-s_j)r$ 和 $(t_i-t_j)/r$ 都是整数。条件意味着两个序列的"差"在某种意义上互为倒数关系——一个序列的差"吸收"了另一个序列差的分母。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的方法来找到这个有理数 $r$。考虑：直接构造、p-adic赋值、归一化、gcd论证、代数恒等式等方向。 | 可能方向：(1) 直接从某个差值构造 $r$；(2) 用 p-adic 赋值分析整性条件；(3) 归一化序列简化问题；(4) 取某个序列的 gcd 作为 $r$；(5) 用代数恒等式提取交叉项信息；(6) 利用非恒常性找到关键指标对。 |
| 3 | 小尝试 | 0.3 | 尝试直接令 $r = s_a - s_b$（某对差的值）。这对所有 $i,j$ 都成立吗？什么会出错？ | 令 $r = s_a - s_b$，则 $(s_i - s_j)r = (s_i-s_j)(s_a-s_b)$ 不一定是整数——条件只保证 $(s_i-s_j)(t_i-t_j)$ 是整数，不保证差与差的乘积为整数。问题在于 $r$ 需要同时对 $s$-差提供整性（乘以 $r$）和对 $t$-差提供整性（除以 $r$），单一差值无法同时满足。 |
| 4 | 思维操作引导 | 0.4 | 利用非恒常性找到指标 $a,b$ 使 $(s_a-s_b)(t_a-t_b) \neq 0$。然后做归一化变换：令 $w = s_b - s_a$，$s'_i = (s_i - s_a)/w$，$t'_i = (t_i - t_a) \cdot w$。验证归一化后 $s'_a = t'_a = 0$，$s'_b = 1$，$t'_b = N$（非零整数），且整性条件保持。 | 非恒常性保证存在 $a,b$ 使乘积非零。归一化后：$s'_a = 0$（因为 $s_a - s_a = 0$），$s'_b = (s_b-s_a)/w = 1$，$t'_a = 0$，$t'_b = (t_b-t_a) \cdot w = (s_b-s_a)(t_b-t_a) = N \in \mathbb{Z} \setminus \{0\}$。整性条件保持因为 $(s'_i - s'_j)(t'_i - t'_j) = (s_i-s_j)(t_i-t_j)$（$w$ 和 $1/w$ 抵消）。问题归约为：$s'_a = t'_a = 0$，$s'_b = 1$，$t'_b = N$ 的情形。 |
| 5 | 推进 | 0.5 | 在归一化后的设定中（$s'_a = 0, t'_a = 0, s'_b = 1, t'_b = N$），从整性条件推导：取 $j = a$ 能得到什么？取 $j = b$ 能得到什么？能否推出 $s'_i t'_i$ 和 $N s'_i + t'_i$ 都是整数？ | 取 $j = a$：$(s'_i - 0)(t'_i - 0) = s'_i t'_i \in \mathbb{Z}$。取 $j = b$：$(s'_i - 1)(t'_i - N) \in \mathbb{Z}$，展开得 $s'_i t'_i - N s'_i - t'_i + N \in \mathbb{Z}$，因 $s'_i t'_i$ 和 $N$ 都是整数，故 $N s'_i + t'_i \in \mathbb{Z}$。另外交叉项 $s'_i t'_j + s'_j t'_i = s'_i t'_i + s'_j t'_j - (s'_i - s'_j)(t'_i - t'_j) \in \mathbb{Z}$。 |
| 6 | 思维操作引导 | 0.6 | 现在已知 $s'_i t'_i \in \mathbb{Z}$ 和 $N s'_i + t'_i \in \mathbb{Z}$（$N \neq 0$）。用 p-adic 赋值证明关键引理：若 $ab \in \mathbb{Z}$ 且 $na+b \in \mathbb{Z}$（$n \neq 0$），则 $b \in \mathbb{Z}$。然后推出所有 $t'_i \in \mathbb{Z}$，取 $d = \gcd(t'_i)$，用赋值界证明 $s'_i \cdot d \in \mathbb{Z}$。 | 关键引理证明：反设 $b \notin \mathbb{Z}$，则存在素数 $p$ 使 $v_p(b) < 0$。由 $na + b \in \mathbb{Z}$ 知 $v_p(na) = v_p(b)$（因为 $v_p(b) < 0 \leq v_p(\text{整数})$，加法中较小赋值主导）。由 $na = (na+b) - b$ 且 $v_p(na) = v_p(b) < 0$，推出 $v_p(a) = v_p(b) - v_p(n) < 0$。但 $ab \in \mathbb{Z}$ 要求 $v_p(a) + v_p(b) \geq 0$，矛盾。故 $t'_i \in \mathbb{Z}$。取 $d = \gcd$，对每个素数 $p$ 找 $j$ 使 $v_p(t'_j) = v_p(d)$，用交叉项 $s'_i t'_j + s'_j t'_i \in \mathbb{Z}$ 推出 $v_p(s'_i) \geq -v_p(d)$，故 $s'_i d \in \mathbb{Z}$。 |
| 7 | 能量传递引导 | 0.7 | 你已经在归一化设定中证明了 $r' = d$ 满足 $s'_i d \in \mathbb{Z}$ 和 $t'_i / d \in \mathbb{Z}$。现在撤销归一化：$r = d/w$（$w = s_b - s_a$）。验证 $(s_i - s_j) \cdot (d/w) = (s'_i - s'_j) \cdot d \in \mathbb{Z}$ 且 $(t_i - t_j)/(d/w) = (t'_i - t'_j)/d \in \mathbb{Z}$。完成证明。 | $(s_i - s_j) \cdot (d/w) = ((s_i - s_a) - (s_j - s_a)) \cdot d / w = (s'_i - s'_j) \cdot d \in \mathbb{Z}$。$(t_i - t_j) / (d/w) = ((t_i - t_a) - (t_j - t_a)) \cdot w / d = (t'_i - t'_j) / d \in \mathbb{Z}$。故 $r = d/w$ 即为所求，证明完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1纯元认知观察 + R2自由列举 + R5推进 + R7能量传递引导）
- knowledge_rounds（思维操作引导的轮数）: 2（R4 + R6）
- level_sum: 0.3 + 0.5 + 0.3 + 0.4 + 0.5 + 0.6 + 0.7 = 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
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
- problem_type: structural_existence
- structure_features: 两个无穷非恒常有理数序列，逐对差乘积为整数的条件，需要找到单一有理数 r 同时分离两个序列差的整性（乘以 r 使 s-差为整数，除以 r 使 t-差为整数）
- key_objects: 有理数序列、p-adic 赋值、整数序列的 gcd、归一化变换、整性条件

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["归一化（将问题化简到规范形式）", "p-adic 赋值分析（将整性问题转化为局部赋值界）", "gcd 论证（取整数序列的最大公因数作为缩放因子）", "代数恒等式提取（从乘积条件提取交叉项信息）", "反证法（p-adic 赋值引理的证明）"]
- primary_pattern: p-adic 赋值分析（将整性问题分解到每个素数的局部赋值，是整个证明的核心引擎）
- knowledge_required: ["p-adic 赋值的基本性质（乘法、加法中的赋值行为）", "有理数整性的 p-adic 判据（v_p(x) >= 0 对所有素数 p 等价于 x 为整数）", "无穷整数序列 gcd 的存在性（反单调自然数列稳定）", "归一化变换保持整性条件"]
- key_insight: 归一化使所有 t_i 变为整数（通过 p-adic 赋值引理），然后取 d = gcd(t_i)，用交叉项的整性条件对每个素数建立 v_p(s_i) >= -v_p(d) 的赋值界，从而 d 同时满足两个方向的整性要求。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接代数操作（对有理数序列的乘积条件做代数展开和恒等变形）
- translation_to: p-adic 赋值语言（将整性问题分解为每个素数处的局部赋值界，用局部-全局原理）
- translation_type: method_translation（从全局代数方法翻译到局部 p-adic 赋值方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: method_translation}
- tell_small_concepts: ["p-adic 赋值", "归一化", "整数序列 gcd", "整性判据", "非恒常序列", "缩放因子", "交叉项", "赋值界"]
- expected_ai_method: direct_manipulation——bare AI 会尝试直接从序列差构造 r，或用代数恒等式直接推导，不会想到用 p-adic 赋值将整性问题分解到局部
- correct_method: p-adic 赋值分析——归一化后用 p-adic 赋值引理证明 t_i 为整数，取 gcd，再用赋值界证明 s_i*d 为整数

**已有ai_method_type值**（优先使用）：
- `enumeration_brute_force` ✅ 抽象
- `continuous_analytic` ✅ 抽象
- `direct_calculation` ✅ 抽象
- `logical_deduction` ✅ 抽象
- `case_by_case` ✅ 抽象
- `algebraic_identity` ✅ 中等
- `equation_solving` ✅ 抽象
- `direct_manipulation` ✅ 抽象
- **❌ 不要用太长太具体的值**

**已有gap_type值**（优先使用）：
- `method_problem_mismatch` ✅ 抽象
- `knowledge_gap` ✅ 抽象
- `structural_transformation` ✅ 中等
- `search_space_estimation` ✅ 中等
- `method_translation` ✅ 中等
- `global_sorting` ⚠️ 偏具体
- **❌ 不要用太具体的值**

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。structural_existence / direct_manipulation / method_translation 均为已有值，且准确描述了这道题的结构。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。三个维度都是中等偏抽象的粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的 tell 特征（从全局代数到局部 p-adic 赋值的方法翻译）可以被 method_translation 充分描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。当前拓扑分类体系完全适用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**⚠️ 每个tell_hint_pair必须包含以下所有字段**：
- `qa_round`: int（对应QA序列的第几轮）
- `tell`: string（AI在这个位置的状态/分叉信号）
- `hint`: string（给AI的提示方向）
- `hint_level`: float（**⚠️ 0-1浮点数，禁止1-4整数**）
- `situation_type`: string（**⚠️ 只能取6个规范值之一**）
- `is_knowledge_bottleneck`: boolean（这轮是否是纯知识瓶颈）
- `tell_topology`: object（**⚠️ 每个pair都要有，不能全用profile级拓扑**）
  - `{problem_type, ai_method_type, gap_type}`
  - **不同轮次的pair可能有不同的拓扑**——比如R1是`(inequality_proof, direct_calculation, method_problem_mismatch)`，R2是`(structural_existence, case_by_case, structural_transformation)`
  - `is_knowledge_bottleneck=True`的pair，`gap_type`应该用`knowledge_gap`
- `tell_small_concepts`: array[string]（**⚠️ 每个pair都要有**，是这个tell特有的小概念信号词）

**同时提取全局(tell, hint)对**：
- `scope_type`: "path_feature"（路径特征型）或 "implicit"（蕴含型）
- `scope`: 具体范围描述
- `observation_point`: 蕴含型填Q编号，路径特征型填null
- `tell`: 全局tell
- `hint`: 全局hint
- `hint_level`: float（0-1）
- `generalizability`: "high/medium/low + 泛化描述"
- `why_not_visible_locally`: **必填字段，不能为None**。path_feature型和implicit型都要填。path_feature型填"完整路径特征为什么在局部视角看不到"；implicit型填"这个蕴含信息为什么在局部步骤中不可见"
- `tell_topology`: object（**⚠️ 每个全局pair也要有**）
- `tell_small_concepts`: array[string]（**⚠️ 每个全局pair也要有**）

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部(tell, hint)对详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到题目结构但未识别逐对差乘积条件的关键约束——对所有i,j成立的强度 | 描述题目结构：已知条件、目标、$(s_i-s_j)(t_i-t_j)\in\mathbb{Z}$对所有i,j意味着什么 | 0.3 | 纯元认知观察 | false | {structural_existence, direct_manipulation, method_problem_mismatch} | ["逐对差乘积整性", "非恒常序列", "缩放因子r"] |
| 2 | AI列出方向但可能遗漏p-adic赋值和归一化这两个关键方向 | 列出所有可能方法：直接构造、p-adic赋值、归一化、gcd、代数恒等式 | 0.5 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["直接构造", "p-adic赋值", "归一化", "gcd", "代数恒等式"] |
| 3 | AI尝试直接令r为某个差值，未意识到单一差值无法同时满足两个方向的整性 | 尝试令r=s_a-s_b，验证是否对所有i,j成立，分析什么出错 | 0.3 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["单一差值", "所有对约束", "双向整性"] |
| 4 | AI困于直接方法，未想到归一化可大幅简化问题 | 找a,b使乘积非零，做归一化变换使s'_a=t'_a=0, s'_b=1, t'_b=N | 0.4 | 思维操作引导 | false | {structural_existence, direct_manipulation, structural_transformation} | ["归一化", "平移缩放", "规范形式", "非零乘积"] |
| 5 | AI已归一化但未从j=a和j=b推导出关键整性事实 | 从归一化设定推导：取j=a得s'_it'_i∈Z，取j=b得Ns'_i+t'_i∈Z，交叉项也是整数 | 0.5 | 推进 | false | {structural_existence, algebraic_identity, method_translation} | ["s_it_i整性", "Ns_i+t_i整性", "交叉项", "代数恒等式"] |
| 6 | AI知道s'_it'_i和Ns'_i+t'_i都是整数但未想到用p-adic赋值引理证明t'_i为整数，也未想到取gcd并用赋值界 | 用p-adic赋值证明关键引理（ab∈Z且na+b∈Z则b∈Z），推出t'_i∈Z，取d=gcd，用赋值界证明s'_i·d∈Z | 0.6 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["p-adic赋值引理", "整数序列gcd", "最小赋值", "赋值界"] |
| 7 | AI已有归一化结果但需撤销归一化得到原始序列的r | 撤销归一化：r=d/w，验证两个方向的整性，完成证明 | 0.7 | 能量传递引导 | false | {structural_existence, direct_manipulation, method_translation} | ["撤销归一化", "缩放回原序列", "最终结论"] |

**全局(tell, hint)对详情**：

**Global 1 (path_feature)**:
- scope_type: path_feature
- scope: 从归一化到p-adic赋值到gcd的完整证明路径
- observation_point: null
- tell: 证明需要一条非显然的路径：归一化→用p-adic引理证明t_i为整数→取gcd→用赋值界证明s_i·d为整数→缩放回原序列。没有任何单一步骤能揭示这条完整路径。
- hint: 关键结构洞察是归一化将问题转化为整数序列问题，使gcd和p-adic赋值变得可用。完整路径：归一化、证明t_i整性、取gcd、建立s_i赋值界、缩放回原序列。
- hint_level: 0.8
- generalizability: high——归一化后使用局部工具（p-adic赋值）的模式适用于许多数论存在性问题
- why_not_visible_locally: 完整路径需要看到归一化会使t_i变为整数（需要知道p-adic引理），而p-adic引理的应用又需要知道gcd的p-adic赋值会界住s_i。每一步的目的只有从终点回看才清楚——局部视角下无法预见归一化为何有用、为何要证明t_i整性、为何取gcd。
- tell_topology: {structural_existence, direct_manipulation, method_translation}
- tell_small_concepts: ["归一化", "p-adic赋值", "gcd", "整性引理", "赋值界", "缩放回原序列"]

**Global 2 (implicit)**:
- scope_type: implicit
- scope: r = gcd(t_i) 的选择隐含在整性结构中
- observation_point: R6
- tell: r的存在性等价于找到一个有理数同时"吸收"s-差的分母和"提供"t-差的分子。归一化后t_i为整数，其gcd d恰好满足这个双重角色——d整除每个t_i故(t_i-t_j)/d为整数，p-adic赋值界保证s_i·d为整数。
- hint: 一旦所有t_i为整数，其gcd d整除每个t_i，故(t_i-t_j)/d为整数。p-adic赋值界表明s_i·d也是整数。所以r=d就是答案（归一化设定中）。
- hint_level: 0.7
- generalizability: medium——gcd作为缩放因子的思路适用于整性分离问题
- why_not_visible_locally: gcd(t_i)与s_i·d整性之间的联系只有在证明t_i为整数并建立p-adic赋值界之后才可见。在这些步骤之前，gcd不会作为r的自然候选出现——因为t_i还不是整数，gcd无定义。
- tell_topology: {structural_existence, logical_deduction, structural_transformation}
- tell_small_concepts: ["gcd作为缩放因子", "整性分离", "p-adic赋值界", "双向整性"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI 会尝试直接代数操作——从 $(s_i-s_j)(t_i-t_j) \in \mathbb{Z}$ 出发尝试构造 r，可能尝试 r = 某个特定差值或尝试用代数恒等式直接推导。不会想到归一化变换，更不会想到用 p-adic 赋值将整性问题分解到每个素数。即使想到取 gcd，也会因为 t_i 不是整数而卡住——不会先证明 t_i 的整性。核心错误是缺少"归一化→证明整性→取gcd→赋值界"这条完整路径的视野。
- suitable_for_poc: ["hint_injection_poc", "tell_detection_poc", "knowledge_bottleneck_poc"]
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

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329437"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2009p6"
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
    '_key': '329437',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2009p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2009p6')
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
- problem_id: compfiles_usa2009p6
- solution_method_type: p_adic_valuation_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。当前拓扑分类体系（structural_existence / direct_manipulation / method_translation）完全适用，粒度一致，无需新增维度。
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
