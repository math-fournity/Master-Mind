# S4 · TellCore候选 + CaseCard + 审计索引 · 精简文档

> **筛选来源**：382号（CasePack v0候选题包，2261行）、383号（TellCore字段消融与最小充分字段集，626行）、388号（全量研究吸收审计，946行）
> **筛选日期**：2026-08-15
> **筛选标准**：见 `eight-system/docs/筛选标准与编排方案.md`

---

## 1. 三个TellCore候选的YAML定义（来源：382号 §2，L64-267）

> **保留理由**：R3（可复用工件）——3个TellCore候选的YAML定义是具体可用的数据结构，包含完整的策略内核字段。这是TellV3首套POC的核心工件。

### 1.1 候选A：模算术表示切换（Modular Representation Switch）

> 来源：382号 L70-123

```yaml
TellCoreCandidate_A:
  name: 模算术表示切换
  invariant_claim: |
    当涉及整数整除性、素性或符号的问题在自然表示下陷入困境时，
    将问题映射到Z/pZ，在有限环中分析，
    可以揭示隐藏的整除性、周期性或符号配对结构，
    将全局问题转化为模p下的局部条件。
  source_branch_events:
    - 1631: x₃≡7(mod 8) → 2是模x₃的二次剩余 → Euler准则 → x₃|y₂
    - 1843: 因子按模4分类 → 左右符号配对 → 方程无实根
  trigger_boundary:
    - 问题涉及整数的整除性、素性、符号或周期性
    - 自然表示下的分析陷入困境（枚举不收敛、符号分析太复杂）
    - 问题中存在可以取模的对象
  negative_boundary:
    - 问题核心在构造性而非分析性
    - 问题核心在几何结构而非代数结构
    - 问题已经在模算术表示下
    - 问题在自然表示下有直接的多项式时间解法
  parameter_slots:
    - p: 模数（需要根据问题结构选择）
    - objects: 取模的对象（整数序列、多项式系数、线性因子等）
    - target_structure: 在模p下寻找的结构类型（整除性/周期性/符号配对/二次剩余性）
  binding_rules:
    - 从问题的整除性/符号条件推断候选模数p
    - 将问题中的所有对象映射到Z/pZ
    - 在Z/pZ下重新表述问题目标
  internal_policy:
    - step1: 识别自然表示陷入困境的信号
    - step2: 分析问题结构，选择候选模数p
    - step3: 在Z/pZ下重新表述问题
    - step4: 在Z/pZ下寻找隐藏结构
    - step5: 将模p发现转化为原问题的解或约束
  progress_model:
    - 信号1: AI开始讨论"取模"或"模p分析"
    - 信号2: AI在模p下发现了周期性/符号配对/整除性
    - 信号3: AI将模p发现与原问题目标建立联系
  termination:
    - 成功: 模p发现直接解决原问题或给出关键约束
    - 无进展: 尝试多个模数后未发现有用结构 → 退出
    - 部分进展: 模p给出部分约束但不足以完全解决 → 标记，考虑组合
  critic:
    - 选择的模数p是否与问题结构匹配？
    - 模p下的发现是否真正对应原问题的目标？
    - 是否过早取模导致丢失了必要信息？
  composition_contract:
    - prerequisites: 无（可作为首步策略）
    - enables: p-adic赋值分析（候选B）可在此基础上深化
    - conflicts_with: 实数连续性分析（取模丢失连续性信息）
    - redundant_with: 其他模q分析（若p和q给出相同信息）
```

### 1.2 候选B：p-adic赋值表示切换（p-adic Valuation Switch）

> 来源：382号 L125-178

```yaml
TellCoreCandidate_B:
  name: p-adic赋值表示切换
  invariant_claim: |
    当问题涉及"是p的幂"或"被p^k整除"的条件，
    且自然代数变形无法约束解空间时，
    系统地使用p-adic赋值v_p可以精确度量整除性，
    揭示隐藏的幂结构，将问题转化为v_p的代数方程。
  source_branch_events:
    - 1709: t(k)最大奇因子 → 2-adic赋值分析 → 约束a的结构
    - 1962: ab-c等均为2的幂 → v_2分析 → 约束(a,b,c)的结构
  trigger_boundary:
    - 问题涉及"是p的幂"或"被p^k整除"的条件
    - 自然代数变形无法约束解空间
    - 问题中存在可以用v_p分析的对象
  negative_boundary:
    - 问题涉及"是素数"但不涉及幂次（v_p不比模p提供更多信息）
    - 问题核心在构造性而非分析性
    - 问题在自然表示下有直接解法
  parameter_slots:
    - p: 赋值的底数
    - objects: 需要计算v_p的对象
    - relations: 对象之间的代数关系（和、积、差等）
  binding_rules:
    - 从"是p的幂"条件确定赋值底数p
    - 对所有相关对象计算v_p
    - 利用v_p(ab)=v_p(a)+v_p(b)等性质建立v_p方程
  internal_policy:
    - step1: 识别"是p的幂"或"被p^k整除"的条件
    - step2: 确定赋值底数p
    - step3: 对所有相关对象计算或表达v_p
    - step4: 利用v_p的代数性质建立方程/不等式
    - step5: 从v_p约束反推原始对象的可能值
    - step6: 验证候选解是否满足原问题条件
  progress_model:
    - 信号1: AI开始计算v_p或讨论"p-adic赋值"
    - 信号2: AI建立了v_p之间的代数关系
    - 信号3: AI从v_p约束推导出了原始对象的约束
  termination:
    - 成功: v_p约束完全确定了解的结构
    - 无进展: v_p方程过于复杂无法收敛 → 退出
    - 部分进展: v_p给出部分约束 → 标记，考虑分case
  critic:
    - v_p分析是否覆盖了所有对象？
    - 是否遗漏了v_p(a+b)≥min(v_p(a),v_p(b))的等号条件？
    - v_p约束是否足以区分所有候选解？
  composition_contract:
    - prerequisites: 模算术表示切换（候选A）可作为前置粗筛
    - enables: 确定解的p-adic结构后可组合构造性Tell
    - conflicts_with: 实数大小分析（v_p不保留大小信息）
    - redundant_with: 无（v_p提供的信息与模p互补）
```

### 1.3 候选C：局部-全局表示切换（Local-Global Representation Switch）——推荐

> 来源：382号 L180-251

```yaml
TellCoreCandidate_C:
  name: 局部-全局表示切换
  invariant_claim: |
    当问题在全局/自然表示下陷入困境时，
    切换到局部表示（Z/pZ的模算术 或 Q_p的p-adic赋值），
    在局部表示下揭示隐藏的代数结构，
    将局部发现提升为全局结论。
    
    局部表示有两个层次：
    - 层次1（模p）：将整数映射到Z/pZ，在有限环中分析
    - 层次2（p-adic）：使用v_p精确度量整除性，在Q_p中分析
    
    层次1是层次2的特例。选择哪个层次取决于问题条件：
    - 涉及整除性/符号/周期性 → 层次1（模p）
    - 涉及"是p的幂"/"被p^k整除" → 层次2（p-adic赋值）
  source_branch_events:
    - 1631: 模8分析 + 二次剩余（层次1）
    - 1843: 模4分类 + 符号配对（层次1）
    - 1709: 2-adic赋值（层次2）
    - 1962: 2-adic赋值（层次2，但tree仍失败——说明需要操作路径）
  trigger_boundary:
    - 问题涉及整数的代数结构（整除性、素性、符号、幂、周期性）
    - 自然表示下的分析陷入困境
    - 问题中存在可以局部化的对象
  negative_boundary:
    - 问题核心在构造性而非分析性
    - 问题核心在几何结构而非代数结构
    - 问题已经在局部表示下
    - 问题在自然表示下有直接解法
    - 问题的核心困难在搜索空间大小而非结构隐藏
  parameter_slots:
    - p: 局部化的目标素数/素数幂
    - level: 局部化层次（模p 或 p-adic赋值）
    - objects: 需要局部化的对象
    - target_structure: 在局部表示下寻找的结构类型
  binding_rules:
    - 从问题条件推断局部化目标p和层次
    - 整除性/符号/周期性 → 模p（层次1）
    - "是p的幂"/"被p^k整除" → p-adic赋值（层次2）
    - 将所有相关对象映射到局部表示
  internal_policy:
    - step1: 识别自然表示陷入困境的信号
    - step2: 分析问题条件，确定局部化目标p和层次
    - step3: 将问题映射到局部表示
    - step4: 在局部表示下寻找隐藏结构
    - step5: 将局部发现提升为全局结论或约束
    - step6: 若局部发现不完全，考虑切换到更高层次或组合其他Tell
  progress_model:
    - 信号1: AI开始讨论"取模"或"p-adic赋值"
    - 信号2: AI在局部表示下发现了隐藏结构
    - 信号3: AI将局部发现与原问题目标建立联系
    - 信号4: AI成功将局部发现提升为全局结论
  termination:
    - 成功: 局部发现直接解决原问题或给出关键约束
    - 无进展: 尝试多个p或层次后未发现有用结构 → 退出
    - 部分进展: 局部发现给出部分约束 → 标记，考虑组合或分case
    - 冲突: 局部化导致丢失必要信息 → 让位给全局分析Tell
  critic:
    - 选择的p和层次是否与问题结构匹配？
    - 局部发现是否真正对应原问题的目标？
    - 是否过早局部化导致丢失了必要信息？
    - 局部发现是否足以提升为全局结论？
  composition_contract:
    - prerequisites: 无（可作为首步策略）
    - enables: 构造性Tell（在局部结构确定后构造解）
    - conflicts_with: 实数连续性分析、纯构造性分析
    - redundant_with: 其他局部化（若不同p给出相同信息）
    - handoff_rule: 若局部化给出部分约束但不足以完全解决，交给构造性Tell或case分析Tell
```

### 1.4 推荐结论

> 来源：382号 L253-267

**推荐候选C（局部-全局表示切换）**，理由：

1. **非特化程度最高**。候选A和B分别针对模p和p-adic两个具体技术，仍带有方法特化痕迹。候选C将两者统一为"局部-全局"策略，更接近372号定义的"因果充分取商"——保留下来的不是某个具体技术，而是"何时局部化、怎样局部化、怎样提升回来"的关系结构。

2. **覆盖所有source trace题**。候选A只覆盖1631/1843，候选B只覆盖1709/1962，候选C覆盖全部四道。

3. **1962的失败可以解释**。1962在tree组仍失败，是因为"给方向"（切换到p-adic）不够，AI需要更具体的操作路径（怎样系统地用v_2建立方程）。候选C的internal_policy包含了step3-step6的操作路径，而候选B的internal_policy更详细但只覆盖p-adic层次。

4. **组合接口最清晰**。候选C明确声明了与构造性Tell的互补关系——局部化确定结构后交给构造性Tell构造解。

本CasePack采纳候选C作为TellCore v0。后续POC-1（因果取商）将对TellCore v0做字段消融和最小充分字段集分析。

---

## 2. CaseCard结构模板（来源：382号，L305-386）

> **保留理由**：R3（可复用工件）——CaseCard的字段结构模板是可复用的数据结构，定义了每道测试题的完整元数据格式。

CaseCard的YAML结构包含以下字段层级：

```yaml
CaseCard_XXX:
  case_id: CC-XXX                    # 唯一标识符
  source:
    origin:                          # 来源类型（historical_bare_failure / metamorphic_variant / constructed_false_friend / boundary_variant / constructed）
    source_document:                 # 来源文档
    source_trace:                    # 原始trace文件路径
  role:
    primary_role:                    # 主角色（source_trace / positive_transfer / metamorphic / false_friend / boundary / composition）
    secondary_roles: []              # 次角色
  problem:
    statement: |                     # 完整题面
    domain:                          # 数学领域
    verified_solution: |             # 已验证解答
    verification_status:             # 核验状态（verified / partial / unverified）
  bare_baseline:
    required_for_positive:           # 是否需要bare基线
    attempts: []                     # bare尝试记录
    status:                          # 状态（failed / not_run）
    failure_mode:                    # 失败模式（route_failure / not_applicable）
    natural_wrong_path: |            # AI的自然错误路径描述
  target_tell:
    tell_family:                     # 目标Tell家族
    expected_selector_decision:      # 预期selector决策（select / reject / boundary）
    expected_runtime_action: |       # 预期运行时动作
    expected_progress_signal: |      # 预期进展信号
    expected_termination:            # 预期终止行为
  structure:
    invariant_kernel: |              # 不变量内核
    surface_features:                # 表面特征
    preserved_features:              # 保持特征
    broken_features_if_negative:     # 负例下破坏的特征
    metamorphic_relation:            # 变形关系
  controls:
    matched_false_friend:            # 配对的假朋友题
    matched_boundary_case:           # 配对的边界题
    matched_decoy:                   # 配对的decoy题
    matched_regression_case:         # 配对的回归题
  risks:
    leakage_risk:                    # 泄漏风险（low / medium / high）
    classicality_risk:               # 经典风险
    ambiguity_risk:                  # 歧义风险
    oversearch_risk:                 # 过度搜索风险
  admission:
    score_summary: |                 # 10项评分汇总（每项0-2分）
    veto_reason:                     # 否决理由（无 / 具体理由）
    frozen_role:                     # 冻结角色
  special_note: |                    # （可选）特殊说明
```

**评分维度（10项，每项0-2分）**：
1. bare基线——是否有真实bare失败记录
2. 策略中心性——目标Tell是否是低搜索成本主路
3. 过程可观察——关键认知动作在thinking中是否可观察
4. 假朋友可构造——是否能构造有效的假朋友题
5. 结构可变形——是否能构造变形题
6. 解答可核验——解答是否经过完整核验
7. 泄漏安全——Tell是否不泄漏关键lemma
8. 经典风险——题目是否有训练痕迹
9. 组合价值——是否适合测试Tell组合
10. 学习价值——失败能否直接修改TellCore字段

---

## 3. 代表性CaseCard样例（来源：382号，5张）

> **保留理由**：R3（可复用工件）——5张代表性CaseCard覆盖了全部5种角色（source_trace / boundary_case_for_direction_vs_path / false_friend / boundary / composition），展示CaseCard在不同角色下的具体填充方式。
> **选择理由**：22张CaseCard中，按角色覆盖度选取5张——CC-001（source_trace + 模p层次1）、CC-004（source_trace + 方向vs操作路径关键案例）、CC-013（false_friend）、CC-018（boundary）、CC-021（composition）。其余17张（CC-002/003/005-012/014-017/019/020/022）标注T3剔除——在POC未运行时构造的批量枚举工件，保留结构模板和代表性样例即可。

### 3.1 CC-001：1631 Mersenne型递推素数长度（source_trace + 模p层次1）

> 来源：382号 L303-386
> **选择理由**：source trace题的典型样例——有完整bare失败记录、Tell成功记录，展示模p层次1的局部表示切换。评分全2分（除经典风险1分、组合价值1分），是强证据题的代表。

```yaml
CaseCard_CC001:
  case_id: CC-001
  source:
    origin: historical_bare_failure
    source_document: 359号索引第4.1节，283号VMS-8实验结果
    source_trace: runs/vms_poc_0/vms8_problem_files/1631_bare.txt, 1631_tree.txt, 1631_lineage.txt
  role:
    primary_role: source_trace
    secondary_roles: [positive_transfer]
  problem:
    statement: |
      对正整数a，定义x₁=a，x_{n+1}=2x_n+1。令y_n=2^{x_n}-1。
      求最大k使存在某个a，y₁,...,y_k全素数。
    domain: Algebra / Number Theory
    verified_solution: |
      答案：k=2。
      证明思路：
      1. x_n = 2^{n-1}(a+1)-1。若y_i素数则x_i必须素数。
      2. a=2时y₁=3, y₂=31素数，y₃=2047=23×89合数。k=2可达。
      3. 对奇素数a≥3：x₂=2a+1≡3(mod 4)，x₃=4a+3≡7(mod 8)。
      4. 由二次剩余理论：2是模p的二次剩余当且仅当p≡±1(mod 8)。
      5. x₃≡7≡-1(mod 8)，所以2是模x₃的二次剩余。
      6. Euler准则：2^{(x₃-1)/2}≡1(mod x₃)。
      7. (x₃-1)/2 = 2a+1 = x₂，所以x₃|2^{x₂}-1=y₂，y₂合数。矛盾。
    verification_status: verified
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-7g-v3: bare失败，无proof.md
      - VMS-8: bare失败，无proof.md
      - VMS-9: bare失败，无proof.md
    status: failed
    failure_mode: route_failure
    natural_wrong_path: |
      AI尝试枚举奇素数a并逐个验证，或使用covering system方法，
      但无法收敛到一般性证明。卡在"不知道如何处理一般奇素数a"。
  target_tell:
    tell_family: 局部表示切换（层次1：模p）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"x₃≡7(mod 8)"这一关键信号 → 切换到模8分析 →
      利用二次剩余理论 → Euler准则 → 证明y₂合数
    expected_progress_signal: |
      1. AI开始分析x₃ mod 8
      2. AI引入二次剩余/Legendre符号概念
      3. AI应用Euler准则
      4. AI建立x₃|y₂的整除关系
    expected_termination: 成功终止——Euler准则直接给出y₂合数的矛盾
  structure:
    invariant_kernel: |
      核心结构：递推序列的素性分析，关键在于模8下的二次剩余性。
      不变量：x₃≡7(mod 8) → 2是模x₃的二次剩余 → x₃|y₂。
    surface_features: Mersenne数、递推关系、素数判定
    preserved_features: 递推结构、素性条件、模分析关键转向
    broken_features_if_negative: 若递推关系改变，模8分析的结构可能不再成立
    metamorphic_relation: 递推+素性 → 模分析+二次剩余
  controls:
    matched_false_friend: CC-013（表面涉及素数但核心在构造性）
    matched_boundary_case: CC-018（改变递推使模8结构变化）
    matched_decoy: CC-016（表面涉及2的幂但核心在组合计数）
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: medium
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败，记录完整）
      策略中心性: 2分（模8+二次剩余是低搜索成本主路）
      过程可观察: 2分（模8分析、Euler准则在thinking中高度可观察）
      假朋友可构造: 2分（CC-013已构造）
      结构可变形: 2分（CC-009已构造）
      解答可核验: 2分（verified solution完整）
      泄漏安全: 2分（Tell只给"切换到模8分析"策略，不给Euler准则细节）
      经典风险: 1分（Mersenne型问题有一定训练痕迹，但具体题面不常见）
      组合价值: 1分（可测试与构造性Tell的组合）
      学习价值: 2分（失败能直接修改trigger或binding rule）
    veto_reason: 无
    frozen_role: source_trace + positive_transfer
```

### 3.2 CC-004：1962 正整数三元组ab-c等均为2的幂（source_trace + 方向vs操作路径关键案例）

> 来源：382号 L560-659
> **选择理由**：这是TellCore v0设计的关键参考案例——1962在tree组仍失败，说明"给方向"不够，需要"给操作路径"。这个失败直接指向internal_policy的必要性，是383号字段消融分析的核心证据。

```yaml
CaseCard_CC004:
  case_id: CC-004
  source:
    origin: historical_bare_failure
    source_document: 359号索引第4.1节，283号VMS-8实验结果
    source_trace: runs/vms_poc_0/vms8_problem_files/1962_bare.txt, 1962_tree.txt
  role:
    primary_role: source_trace
    secondary_roles: [boundary_case_for_direction_vs_path]
  problem:
    statement: |
      求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是2的幂。
      （2的幂是形如2^n的整数，n为非负整数。）
    domain: Number Theory
    verified_solution: |
      答案：(2,2,2), (1,1,1)等（需要完整验证）。
      证明思路：
      1. a=1时b-c和c-b都是2的幂但和为0，矛盾。所以a,b,c≥2。
      2. 设ab-c=2^u, bc-a=2^v, ca-b=2^w。
      3. 对称性：假设a≤b≤c。
      4. 情形a=b：a²-c和a(c-1)都是2的幂。
         a(c-1)是2的幂意味着a和c-1都是2的幂。
      5. 一般情形a<b<c：需要系统2-adic赋值分析。
         关键：v_2(ab-c)=u, v_2(bc-a)=v, v_2(ca-b)=w。
         利用v_2(x+y)≥min(v_2(x),v_2(b))等性质建立约束。
    verification_status: partial
  bare_baseline:
    required_for_positive: true
    attempts:
      - VMS-7g-v3: bare失败
      - VMS-8: bare失败
      - VMS-8 tree组: 仍然失败——卡在2-adic复杂计算
    status: failed
    failure_mode: route_failure
    natural_wrong_path: |
      AI尝试代数变形和枚举，陷入复杂的2-adic赋值代数无法收敛。
      即使在tree组给了T02 p-adic赋值方向后，AI仍无法完成——
      说明"给方向"不够，需要"给操作路径"。
  target_tell:
    tell_family: 局部表示切换（层次2：p-adic赋值）
    expected_selector_decision: select
    expected_runtime_action: |
      识别"代数变形无法约束"的困境信号 →
      切换到系统2-adic赋值分析 →
      对a,b,c的奇偶性分case →
      在每个case中用v_2建立方程 →
      从v_2约束反推(a,b,c)的结构
    expected_progress_signal: |
      1. AI开始系统计算v_2
      2. AI按奇偶性分case
      3. AI在每个case中建立v_2方程
      4. AI从v_2约束推导(a,b,c)的可能值
    expected_termination: |
      成功：v_2约束完全确定(a,b,c)的结构。
      部分进展：v_2约束给出部分case的解，其余case需要组合其他Tell。
      注意：本题在tree组失败的教训是——
      TellCore v0的internal_policy必须包含操作路径，
      不能只给"切换到p-adic"的方向。
  structure:
    invariant_kernel: |
      核心结构："是2的幂"条件通过v_2赋值可精确表达。
      不变量：v_2(ab-c)+v_2(bc-a)+v_2(ca-b)与a,b,c的奇偶结构相关。
    surface_features: 三元组、2的幂、对称性
    preserved_features: 2-adic赋值分析、奇偶分case
    broken_features_if_negative: 若"2的幂"改为"素数"，v_2分析不再适用
    metamorphic_relation: 代数枚举困境 → 系统2-adic赋值+分case
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: CC-018（改变"2的幂"为"素数"）
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: high
  admission:
    score_summary: |
      bare基线: 2分（真实bare失败，记录完整）
      策略中心性: 2分（2-adic赋值是主路，但需要操作路径）
      过程可观察: 2分（v_2分析在thinking中可观察）
      假朋友可构造: 2分（CC-015已构造）
      结构可变形: 2分（CC-012已构造）
      解答可核验: 1分（解答部分核验，一般情形需要完整验证）
      泄漏安全: 2分
      经典风险: 1分
      组合价值: 2分（本题特别适合测试"方向Tell vs 操作路径Tell"的层级问题）
      学习价值: 2分（tree组失败直接指向internal_policy的改进需求）
    veto_reason: 无
    frozen_role: source_trace + boundary_case_for_direction_vs_path
  special_note: |
    本题是TellCore v0设计的关键参考案例。
    VMS-8 tree组失败说明：仅给"切换到p-adic赋值"的方向不够，
    AI需要更具体的操作路径（怎样分case、怎样建立v_2方程）。
    TellCore v0候选C的internal_policy中step3-step6正是对此的回应。
    本题在POC-3（可执行）中应作为"方向Tell vs 操作路径Tell"的对照案例。
```

### 3.3 CC-013：假朋友——递推序列收敛性（false_friend）

> 来源：382号 L1320-1396
> **选择理由**：假朋友题的典型样例——表面相似度极强（递推关系与1631完全相同），但核心结构完全不同（级数收敛性 vs 素性判定）。展示false_friend角色的CaseCard填充方式。
> **注意**：388号审计发现CC-013的verified_solution有数学错误（声称S=1/(a+1)不成立），已标记为 `quarantined_math_error`。此处保留原CaseCard结构，但数学解答部分不可信。

```yaml
CaseCard_CC013:
  case_id: CC-013
  source:
    origin: constructed_false_friend
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: false_friend
    secondary_roles: []
  problem:
    statement: |
      对正整数a，定义序列x₁=a，x_{n+1}=2x_n+1。
      令S_n = Σ_{i=1}^{n} 1/x_i。
      证明：对所有正整数a，序列S_n收敛，
      并求lim_{n→∞} S_n的值。
    domain: Analysis / Sequences
    verified_solution: |
      【注意：388号审计发现此解答有数学错误，标为quarantined_math_error】
      原文声称答案：S = 1/(a+1)。
      388号指出：当a=1时，仅第一项S₁=1就已经大于声称的极限1/2。
      级数确实因指数增长而收敛，但文档给出的精确值与telescoping未被证明，且为错。
    verification_status: quarantined_math_error  # 原标verified，388号审计降级
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用（假朋友题不要求bare失败）
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: reject
    expected_runtime_action: |
      理想selector应reject——
      本题表面涉及递推序列（与1631表面相似），
      但核心在级数收敛性（实分析），不在整除性/素性。
      模p分析不直接适用于收敛性问题。
    expected_progress_signal: 无——不应触发目标Tell
    expected_termination: 不适用——不应触发
  structure:
    invariant_kernel: |
      表面相似：递推序列x_{n+1}=2x_n+1（与1631完全相同）。
      结构缺失：核心在级数收敛性，不在素性/整除性。
      模p分析不适用——收敛性是实分析概念，不是代数概念。
    surface_features: 递推序列、2x_n+1（与1631相同的递推）
    preserved_features: 无——核心结构完全不同
    broken_features_if_negative: 素性条件被替换为收敛性条件
    metamorphic_relation: 无——表面相似但结构不同
  controls:
    matched_false_friend: 本身即为假朋友题
    matched_boundary_case: CC-018
    matched_decoy: CC-016
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: low
    oversearch_risk: low
  admission:
    score_summary: |
      假朋友可构造: 2分（表面相似度强，结构差异清楚）
      解答可核验: 2分  # 388号审计后降级——实际有数学错误
      学习价值: 2分（如果selector误触发，说明trigger过宽——需要收紧"整除性/素性"条件）
    veto_reason: 无
    frozen_role: false_friend
  special_note: |
    本题的表面相似度很强——递推关系与1631完全相同。
    但核心结构完全不同——1631的核心在素性判定（模p分析适用），
    本题的核心在级数收敛性（模p分析不适用）。
    如果selector对本题select，说明trigger的"整除性/素性"条件不够严格。
    【388号审计补充：本题数学解答有错误，应进入quarantined_math_error，
    不得继续标verified。但假朋友的结构设计（表面相似/结构不同）仍然有效。】
```

### 3.4 CC-018：边界——1962变体"2的幂"改为"素数"（boundary）

> 来源：382号 L1674-1750
> **选择理由**：边界题的典型样例——与1962只差一个关键条件（"2的幂"→"素数"），破坏了p-adic赋值分析的适用性。展示boundary角色的CaseCard填充方式，以及selector应给出boundary决策而非select/reject的预期。

```yaml
CaseCard_CC018:
  case_id: CC-018
  source:
    origin: boundary_variant
    source_document: 本文件（382号）首次构造
    source_trace: 基于CC-004(1962)构造
  role:
    primary_role: boundary
    secondary_roles: []
  problem:
    statement: |
      求所有正整数三元组(a,b,c)，使ab-c, bc-a, ca-b都是素数。
    domain: Number Theory
    verified_solution: |
      预期分析：
      1. 与1962的结构相同，但"2的幂"被替换为"素数"。
      2. p-adic赋值分析不再直接适用——
         素数条件不能用v_p精确表达（素数不是p^k形式）。
      3. 需要完全不同的方法——可能利用素数的分布性质或大小约束。
      4. 预期答案可能非常有限或无解。
    verification_status: unverified
  bare_baseline:
    required_for_positive: false
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: 不适用
  target_tell:
    tell_family: 局部表示切换
    expected_selector_decision: boundary
    expected_runtime_action: |
      理想selector应标为boundary——
      本题与1962结构几乎相同（只改一个条件），
      但"素数"条件使p-adic赋值分析不再直接适用。
      selector应识别：结构相似但关键条件改变，触发边界。
    expected_progress_signal: |
      如果AI尝试p-adic分析但发现不适用，这是正确的边界行为。
      如果AI强行使用p-adic分析并陷入困境，说明termination机制需要改进。
    expected_termination: |
      理想行为：AI尝试p-adic分析 → 发现"素数"条件不适用 → 退出或让位。
      或者：selector直接标为boundary，不触发目标Tell。
  structure:
    invariant_kernel: |
      与1962的唯一差异："2的幂"→"素数"。
      这个改变破坏了p-adic赋值分析的适用性——
      v_p(素数)要么是0（p≠该素数）要么是1（p=该素数），
      不提供足够信息来建立v_p方程。
    surface_features: 三元组、素数条件
    preserved_features: 三元组结构、对称性
    broken_features_if_negative: "2的幂"→"素数"破坏p-adic适用性
    metamorphic_relation: 无——关键条件改变使目标Tell不适用
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: 本身即为边界题
    matched_decoy: CC-016
    matched_regression_case: 不适用
  risks:
    leakage_risk: low
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: medium
  admission:
    score_summary: |
      策略中心性: 0-1分（p-adic不直接适用，但模p分析可能有弱关联）
      学习价值: 2分（测试selector的boundary决策和AI的termination行为）
    veto_reason: 无
    frozen_role: boundary
  special_note: |
    本题是1962的边界变体——只改一个关键条件（"2的幂"→"素数"）。
    测试两个能力：
    1. selector能否识别边界（标为boundary而非select/reject）
    2. AI在尝试p-adic分析后发现不适用时能否正确退出
    如果selector强行select且AI无法退出，说明termination机制需要改进。
```

### 3.5 CC-021：组合——局部表示切换+构造性Tell（composition）

> 来源：382号 L1915-2001
> **选择理由**：组合题的典型样例——展示顺序依赖组合（局部表示切换先给出结构约束，构造性Tell在约束内构造解）。展示composition角色的CaseCard填充方式。

```yaml
CaseCard_CC021:
  case_id: CC-021
  source:
    origin: constructed
    source_document: 本文件（382号）首次构造
    source_trace: 无
  role:
    primary_role: composition
    secondary_roles: []
  problem:
    statement: |
      求所有正整数n，使得存在正整数a₁,a₂,...,a_n满足：
      (1) a₁+a₂+...+a_n = 2n
      (2) 对每个i，a_i | 2n
      (3) 对每对i≠j，a_i - a_j 是2的幂（可为负，即|a_i-a_j|是2的幂）
    domain: Number Theory / Construction
    verified_solution: |
      预期分析：
      1. 条件(3)涉及"差是2的幂"——表面像p-adic赋值问题。
      2. 但核心难点是构造性——需要构造满足所有条件的序列。
      3. 策略：先用p-adic赋值分析约束a_i的结构（局部表示切换），
         再用构造性Tell构造具体序列。
      4. 这是顺序依赖组合——局部表示切换先于构造性Tell。
    verification_status: unverified
  bare_baseline:
    required_for_positive: true
    attempts: []
    status: not_run
    failure_mode: not_applicable
    natural_wrong_path: |
      预测AI可能尝试直接构造，忽略p-adic结构分析，
      导致构造空间过大无法收敛。
  target_tell:
    tell_family: 局部表示切换 + 构造性Tell（顺序依赖）
    expected_selector_decision: select（局部表示切换作为前置）
    expected_runtime_action: |
      步骤1（局部表示切换）：分析a_i的2-adic结构 →
      利用"差是2的幂"条件约束a_i的v_2值 →
      约束a_i的可能形式。
      步骤2（构造性Tell）：在约束范围内构造具体序列 →
      验证满足所有条件。
    expected_progress_signal: |
      1. AI开始v_2分析a_i结构
      2. AI从v_2约束推导a_i的可能形式
      3. AI在约束范围内开始构造
      4. AI验证构造满足所有条件
    expected_termination: |
      成功：v_2约束+构造共同给出完整解。
      部分进展：v_2约束给出结构但构造失败 → 标记，需要更强的构造性Tell。
  structure:
    invariant_kernel: |
      核心结构：先分析后构造。
      局部表示切换提供结构约束，构造性Tell在约束内构造。
    surface_features: 2的幂条件、求和条件、整除条件
    preserved_features: p-adic结构分析+构造的组合
    broken_features_if_negative: 无
    metamorphic_relation: 分析+构造的组合
  controls:
    matched_false_friend: CC-015
    matched_boundary_case: CC-018
    matched_decoy: CC-016
    matched_regression_case: 本题在Tell修订后作为回归题重跑
  risks:
    leakage_risk: medium
    classicality_risk: low
    ambiguity_risk: medium
    oversearch_risk: medium
  admission:
    score_summary: |
      bare基线: 0分
      策略中心性: 2分（p-adic+构造的组合是主路）
      过程可观察: 2分
      组合价值: 2分（明确的顺序依赖组合）
      解答可核验: 0分
      泄漏安全: 1分
      学习价值: 2分
    veto_reason: bare基线和解答核验都需要后续验证
    frozen_role: composition
  special_note: |
    本题测试POC-5（可组合）——
    局部表示切换（分析结构）→ 构造性Tell（在约束内构造）。
    顺序依赖：构造性Tell依赖局部表示切换先给出结构约束。
    如果AI跳过p-adic分析直接构造，说明组合调度失败。
```

---

## 4. TellCore字段消融与最小充分字段集（来源：383号，全文626行）

> **保留理由**：R3（可复用工件）——字段消融方法和最小充分字段集结论是TellCore结构分析的核心产出，可直接用于后续POC设计。

### 4.1 消融方法

> 来源：383号 L28-43

对TellCore v0候选C的每个字段做消融分析：

```text
对每个字段 F：
  问1：删除F后，TellCore是否仍可在新题上执行？
  问2：删除F后，TellCore是否仍能解释迁移？
  问3：删除F后，替换表面外壳后是否保持作用？
  问4：删除F后，改变关键结构后是否应拒绝？
  问5：删除F后，是否能解释正例和负例的差异？
  
  若全部"是" → F非必要
  若有"否" → F必要或重要
```

### 4.2 12字段逐项消融结论

> 来源：383号 L66-264

| 编号 | 字段 | 类型 | 判定 | 关键理由 |
|---|---|---|---|---|
| F1 | name | 元数据 | **非必要** | 标识符，不参与执行、选择或归责 |
| F2 | invariant_claim | 核心主张 | **必要** | 因果解释的核心——解释"为什么局部化有效"和"什么时候局部化不适用" |
| F3 | source_branch_events | 历史证据（输入） | **非必要（运行时）** | 是POC-1的输入（从trace提取TellCore时使用），不是运行时字段 |
| F4 | trigger_boundary | 触发条件 | **必要** | "可选择"门的核心——没有它，selector无法知道何时选这个Tell |
| F5 | negative_boundary | 负触发条件 | **必要** | "可选择"门的另一半——没有它，selector无法知道何时拒绝这个Tell |
| F6 | parameter_slots | 参数槽 | **必要**（p+level+objects）；**重要**（target_structure） | AI不知道要绑定什么到新题上 |
| F7 | binding_rules | 绑定规则 | **重要** | 可从trigger_boundary和parameter_slots部分推断，但显式规则显著提高绑定准确性 |
| F8 | internal_policy | 内部策略（6步） | **必要**（step2-5）；**重要**（step1+step6） | 1962的失败证明：方向Tell不够，需要操作路径Tell |
| F9 | progress_model | 进展模型 | **必要** | "可终止"和"可归责"两门的基础 |
| F10 | termination | 终止条件 | **必要** | "可终止"门的直接载体 |
| F11 | critic | 自检 | **重要** | 不是首次执行的必要条件，但是"可持续学习"门和复杂假朋友拒绝的必要条件 |
| F12 | composition_contract | 组合接口 | **重要（对POC-5）** | 对POC-1和POC-3不直接影响，对POC-5是必要条件 |

### 4.3 最小充分字段集（7个字段）

> 来源：383号 L267-315

```yaml
TellCore_minimal:
  invariant_claim: |
    当问题在全局/自然表示下陷入困境时，
    切换到局部表示（Z/pZ或Q_p），
    在局部表示下揭示隐藏的代数结构，
    将局部发现提升为全局结论。
  trigger_boundary:
    - 问题涉及整数的代数结构（整除性、素性、符号、幂、周期性）
    - 自然表示下的分析陷入困境
    - 问题中存在可以局部化的对象
  negative_boundary:
    - 问题核心在构造性而非分析性
    - 问题核心在几何结构而非代数结构
    - 问题已经在局部表示下
    - 问题在自然表示下有直接解法
    - 问题的核心困难在搜索空间大小而非结构隐藏
  parameter_slots:
    - p: 局部化的目标素数
    - level: 模p 或 p-adic赋值
    - objects: 需要局部化的对象
  internal_policy:
    step2: 分析问题条件，确定局部化目标p和层次
    step3: 将问题映射到局部表示
    step4: 在局部表示下寻找隐藏结构
    step5: 将局部发现提升为全局结论或约束
  progress_model:
    - 信号1: AI开始讨论"取模"或"p-adic赋值"
    - 信号2: AI在局部表示下发现了隐藏结构
    - 信号3: AI将局部发现与原问题目标建立联系
    - 信号4: AI成功将局部发现提升为全局结论
  termination:
    - 成功: 局部发现直接解决原问题或给出关键约束
    - 无进展: 尝试多个p或层次后未发现有用结构 → 退出
    - 部分进展: 局部发现给出部分约束 → 标记，考虑组合或分case
    - 冲突: 局部化导致丢失必要信息 → 让位给全局分析Tell
```

### 4.4 字段分级汇总

> 来源：383号 L269-276

| 级别 | 字段 | 数量 | 说明 |
|---|---|---:|---|
| **必要** | invariant_claim, trigger_boundary, negative_boundary, parameter_slots(p+level+objects), internal_policy(step2-5), progress_model, termination | 7 | 删除任一导致TellCore无法通过至少一门审计 |
| **重要补充** | binding_rules, internal_policy(step1+step6), critic, composition_contract, parameter_slots(target_structure) | 5 | 删除导致特定POC或特定场景失败 |
| **元数据/输入** | name, source_branch_events | 2 | 不参与运行时执行 |

### 4.5 核心发现

> 来源：383号 L550-558

1. **1962的失败是TellCore设计的核心教训**：方向Tell（"切换到p-adic"）不够，需要操作路径Tell（step2-5的系统步骤）。这是因果取商最重要的发现——从4道source trace的成败差异中提取出的因果结构。

2. **最小充分字段集是7个字段**：invariant_claim、trigger_boundary、negative_boundary、parameter_slots(p+level+objects)、internal_policy(step2-5)、progress_model、termination。这7个字段是TellCore通过六门审计的最低要求。

3. **critic是假朋友拒绝的安全网**：2/5假朋友题（CC-014/017）的拒绝需要critic协同。最小充分字段集可以处理大部分场景，但完整生产级字段集更安全。

4. **TellCore v0不泄漏具体lemma**：Euler准则、Fermat小定理等具体数学工具不在TellCore中——TellCore只提供"何时用"和"怎样组织"，不替AI完成关键发现。

### 4.6 POC-1通过标准验证结果

> 来源：383号 L528-548

| 通过标准 | 结果 | 说明 |
|---|---|---|
| 1. 没有源题对象泄漏 | **PASS** | 运行时字段无源题特定信息 |
| 2. 有明确trigger和negative trigger | **PASS** | 3条正触发+5条负触发 |
| 3. 参数槽可绑定到新题对象 | **PASS（有条件）** | p的绑定需要binding_rules辅助 |
| 4. internal policy不是口号 | **PASS（待经验验证）** | 4步操作路径，但需POC-3验证 |
| 5. progress model能预测信号 | **PASS** | 4个可观察信号 |
| 6. termination能说明何时停止 | **PASS** | 4个终止条件覆盖全场景 |
| 7. 能解释假朋友不应触发 | **PASS（有条件）** | 3/5仅靠trigger，2/5需要critic |

**POC-1 verdict**：PASS（有条件）——条件1：完整生产级字段集用于POC-2~POC-8；条件2：internal_policy操作路径充分性需POC-3经验验证；条件3：CC-014和CC-017的假朋友拒绝需要selector+critic协同设计。

---

## 5. 七项重要判断（来源：388号 §3.2，L116-124）

> **保留理由**：R1（认知推进）——七项判断是对Tell分类学历史研究的核心认知总结，提出了对旧术语的拆分方案和对象边界。R3（可复用工件）——这些判断直接影响387号非特化体系的对象模型设计。

1. **旧"Tell"一词负担了至少五种不同对象，必须拆开。** `TaxonomyTerm`、`TellCore`、`TellManifestation`、`TellRecognitionRecord`、`HintInstance`不是同一个对象。

2. **v2最有价值的修正必须保留。** `local / non_local / global`是观察trace的粒度，不是TellCore固有属性，也不是root/point分叉位置；同一Core可有多个观察显现。

3. **000号四成分值得吸收，但不应整体塞进TellCore。** 分叉信号、未探索诊断和方向匹配依赖当前运行状态，应进入运行时Recognition记录；TellCore只保存跨题不变的因果内核。

4. **Tell与Hint多对多值得成为一等关系。** 当前`system/schema.py`中的`Hint.tell_id`仍是一对一外键，387号也缺显式关系对象；这会让选择、归责、版本与复用不可审计。

5. **FCA值得保留，但角色必须降准。** 它适合生成候选分类、寻找遗漏显现、组织覆盖与近邻反例；不能单独证明两个显现属于同一因果TellCore，更不能证明Hint有效。

6. **旧分类学v3只是先验ontology。** 五种段结构模式和六个domain可作为`TaxonomySnapshot v3`的候选词典，不得写成已验证的自然完备分类。

7. **旧POC与出题链留下了很好的协议资产和负证据，但没有完成非特化因果验证。** 355/357/358/363的bare淘汰、280的静态抽象Hint失败、383的文档字段消融都应进入EvidenceRecord，但证据类型不同。

---

## 6. 对387号的处置建议（来源：388号 §3.3 + §11，L126-136 + L765-803）

> **保留理由**：R4（合理工程约束）——对387号的分类学桥接修订建议是合理的工程约束，来自科学方法内在要求。R3（可复用工件）——修订建议的具体内容可直接用于387号的修订。

### 6.1 总体处置

建议对387号做一次**窄而明确的"分类学桥接修订"**，而不是重写其因果实验、三审、版本学习和运行工厂：

- 保留387号的TellCore / Applicability / Execution / Renderer / Selector / EvidenceRecord主架构；
- 在其前端补齐Observation、Manifestation、Recognition、Taxonomy与M:N Hint关系；
- 在其版本层补齐TaxonomySnapshot、重分类影响集和分类学修订门；
- 在实验层增加分类路由、观察不变性、高Level解释形态与动态展开的正交实验；
- 明确旧分类学只提供候选结构，不提升任何既有因果证据等级。

本审计没有直接修改387号，因为那将改变已经逐节批准的规格；应在用户批准本吸收包后另行修订。

### 6.2 推荐吸收包与优先级

**P0：先修证据污染，不改理论**

1. 隔离382号CC-013，重新核验所有标`verified`的构造题；建立独立VerificationDossier。
2. 对380号敏感凭据做轮换/脱敏，删除直接客户端示范，改为当前受控DB入口。
3. 建立v1→v2→v3分类映射，列出AGENTS/system/docs/prompt资产的漂移清单；在修完前，运行数据必须保存精确schema/hash，不能只写`taxonomy_version=v3`。
4. 将383/385/README中的POC-0/1措辞统一降级为"结构设计/候选字段审查"，不计经验PASS。
5. 把当前`Problem→SolverInput`答案能力、默认`is_verified=true`和未匹配trace直接升Tell列为Golden Slice硬blocker；在分权输入、Proof Gate和Revision Gate落地前，legacy absorb/solve路径不得生成确认性Evidence。

**P1：修订387号的分类学桥接层**

1. 新增§5对象：Snapshot、Assignment、View、Manifestation、Recognition、TellHintRelation、ExplanationBundle。
2. 展开§6的`tell_taxonomy_coordinate`，并把Assignment target与数学内容坐标分开。
3. 在§7吸收`AuthoringBlueprint`的solution/obstacle script与六角色case anatomy，并由`SearchSpaceReductionProfile`审计题目是否把开放搜索泄漏成局部补全。
4. 在§8加入E-TAX-1至E-TAX-5及`TellFunctionalType`；不改变已有Phase 0—5的主contrast，也不新增"第七门"。
5. 在§9让Process Auditor审计识别span、manifestation lineage与目标Core，不让其看Hint/arm。
6. 在§10增加TaxonomyRevisionProposal和重分类影响集；taxonomy变更不能继承Core efficacy。
7. 在§11冻结taxonomy/dictionary/relation/explanation hash，并监控classification drift。

**P2：用户批准规格后再迁移实现**

- 重构`system/schema.py`，不兼容变更必须有迁移器，不原地改旧记录；
- 修正`system/docs/schema.md`、`references.md`和AGENTS重复Schema；
- 将具体taxonomy词典移出always-on AGENTS，形成版本化机器资产；
- 为M:N关系建立join/registry，而非单外键；
- 为旧Trace/Tell记录生成migration assessment，不把重分类后的标签写回历史原件；
- 建立taxonomy sync checker与drift alert。

**P3：首批实验顺序**

```text
先做 E-TAX-1 观察不变性/显现去重
  → 再做 E-TAX-2 分类路由是否真有价值
  → 再做 E-TAX-3 Renderer形态
  → 开放方向型样本足够后做 E-TAX-4
  → M:N真实冲突case成熟后做 E-TAX-5
```

不要一开始重跑全部455/67,837个profile，也不要先把26种思维力全部词典化。先用当前golden slice的一个Tell家族和少量positive/false-friend/boundary做完整桥接。

### 6.3 最终建议

> 来源：388号 L928-946

**建议批准"P0证据修复 + P1分类学桥接修订"，暂不批准P2代码迁移。**

理由是：

1. 旧研究确实补上了387号目前最薄的一层——从trace怎样形成可审计的Tell候选；
2. 387号已经补上旧研究最缺的一层——候选怎样经过因果对照、负例、泄漏审计和版本前瞻确认；
3. 两者合流后，才能把"看见一个模式""把它分类""选中一个Core""给出一个Hint""AI因此改变路线"逐层区分；
4. 直接改代码会把当前文档中的v1/v3漂移和CC-013式错误固化进数据，因此必须先修规格和证据。

若用户批准，下一步应是：

```text
修订387号（只加分类学桥接层）
  → 对修订稿做因果一致性终审
  → 单独形成旧Schema迁移设计
  → 再决定是否实现E-TAX-1 golden slice
```

---

## 7. 54份文档归类索引（来源：388号 §12，L808-869）

> **保留理由**：R3（可复用工件）——54份文档的全量归类索引是重要的审计工件，记录了每份文档的证据性质和吸收处置，可直接用于后续研究资产的管理和回取。

### 7.1 全量目录coverage ledger（冻结语料54/54）

说明：本表的"吸收处置"是对内容的处置，不等于文件质量评级。`388`是审计产物本身，不计入审计启动时冻结的54份历史语料。

| 文件 | 证据性质 | 吸收处置 |
|---|---|---|
| 交接文档 | Handover | 主线入口；事实需回源，不作独立证据 |
| README | Index | 用作库存交叉核验；已发现原索引漏列376—380 |
| 333 | Concept | M:N、效力分账直接吸收；展开主张由340校准 |
| 334 | Hypothesis | 触发依据与pressure策略转为Selector实验 |
| 335 | Concept | 三解释面直接吸收为ExplanationBundle |
| 336 | Concept | 结构/内容分离吸收；轴/刻度/点术语校准 |
| 337 | Superseded hypothesis | 保留排除假设；拒绝"始终在场"生产规则 |
| 338 | Concept correction | 按角色载体与识别任务吸收；不固化AGENTS载体 |
| 339 | Integration plan | 只作历史计划；部分实施状态需重审 |
| 340 | Refined hypothesis | expansion_mode吸收；允许hybrid和经验修订 |
| 344 | Concept | 保留泛化候选族；废止Level重名 |
| 345 | Hypothesis | 保留TellFamily；钟形曲线降级 |
| 346 | Method proposal | 作为Core生成gate，不作有效性证据 |
| 347 | Protocol | Renderer四形态进入正交实验 |
| 348 | POC design | Case/contrast素材；未运行项不计证据 |
| 349 | Candidate inventory | 只作思维力发现集，不作自然分类或效力证据 |
| 350 | Protocol | 匹配/错配/鼓励对照、纯洁性与预注册吸收 |
| 351 | Delegation prompt | 只作任务需求来源，不作研究结果 |
| 352（观察技术） | Historical runbook | artifact思想保留；旧tmux/mitm操作废弃 |
| 352（策略审查） | Protocol review | trigger/exit/function/leakage/intensity/attribution吸收 |
| 353 | Candidate framework | 父类重组作为hypothesis，禁止直接写taxonomy validated |
| 354 | Generated cases | development素材；被后续bare结果更新 |
| 355 | Negative run evidence | 候选淘汰；支持bare admission gate |
| 356 | Case-design protocol | core/shell/decoy/lock/certificate/margin吸收 |
| 357 | Negative run evidence | 候选淘汰；记录廉价出口与阈值问题 |
| 358 | Mixed observational evidence | route/proof/output三层判定吸收 |
| 359 | Historical index | 作为发现入口；anchor随model/resource版本化 |
| 360 | Historical implementation design | 并发留证经验；旧系统不复用 |
| 361 | Implementation handoff | 资源/阶段gate经验吸收；命令已过时 |
| 362（挑战题） | Generated/planned cases | 未跑题为development；已跑题看363 |
| 362（实施报告） | Infrastructure result | 留证/并发阳性；预测失败和token-limit降级 |
| 363 | Negative run evidence | 两道新造题bare淘汰；硬化经验吸收 |
| 364 | Case-design protocol | 母题拆解与自然错路吸收 |
| 365 | Planned queue | 题源候选，不计运行证据 |
| 366 | Method proposal | Level 3—4机制抽取吸收为出题操作，不作效力证据 |
| 367 | Planned queue | 只作候选挑战池 |
| 368 | Case-design protocol | solution/obstacle script与挑战公式直接吸收 |
| 369 | Generated/planned cases | development素材，未运行 |
| 370 | Generated/planned cases | development素材，未运行 |
| 371 | Theoretical synthesis | 重要要求已大体进入372/387；不重复建栈 |
| 372 | Architecture/specification | 非特化理论主核；作为387上游规格 |
| 373 | POC protocol | 六门与CaseCard上游；未运行POC不作结果 |
| 374 | Data/provenance report | 候选追溯入口；旧失败归因需387重分层 |
| 375 | Supply strategy | 题源规划，不是Tell证据 |
| 376 | Operational data report | 候选池供给事实，不是分类学/效力证据 |
| 377 | Historical pipeline implementation | 数据可审计/恢复经验；运行架构已演进 |
| 378 | Test protocol | 完整性测试思想吸收；未执行项保持planned |
| 379 | Historical runbook | 故障/恢复经验；命令与架构不复用 |
| 380 | Data query guide | 失败流入口；敏感凭据与直接DB方式必须修复 |
| 381 | Handover | 372/373入口；旧完成度与证据等级需重校准 |
| 382 | Candidate CasePack | 角色设计可用；数学冻结被CC-013反证 |
| 383 | Design analysis | 字段假设可用；不是实跑消融或因果PASS |
| 386 | Historical index | 正交出题引用图可用；283强度按387校准 |
| 387 | Target specification | 主体保留；补分类学桥接层 |

**账本计数**：编号文档52份 + 交接文档1份 + README 1份 = 54份；已归类54份；遗漏0份；remainder=0。

### 7.2 外部核心资产回源账本

> 来源：388号 L871-886

| 资产 | 用途 | 结论 |
|---|---|---|
| 000号根定义 | Tell四成分、root/point、引导树动作 | 吸收到Recognition与Injection语义 |
| FCA 08 | v3先验taxonomy及版本史 | 作为Prior Snapshot，不作validated ontology |
| FCA 09 | 单题多Level重分析 | discovery evidence，需去重/盲化/holdout |
| taxonomy iteration audit rule | 修订覆盖与同步 | 扩展为TaxonomyRevisionProposal |
| taxonomy schema maintenance rule | 结构/内容分离 | 升级为多资产机器同步，不只AGENTS |
| AGENTS Tell Schema | 跨session认知 | 发现旧新口径并存，需迁移 |
| `system/schema.py` | 当前物化Schema | 发现Core/Recognition混合与M:N缺失 |
| `system/docs/schema.md`、`references.md` | 工程说明 | 发现v1/v3漂移 |
| 277—289历史POC | Hint/Tell早期验证 | 按280负证据、283污染性包阳性、VMS9/10机械smoke校准 |
| `dev-docs/384` | AGENTS瘦身元工程 | 编号碰撞；与Tell科学内容无关，不吸收 |
| `dev-docs/385` | TellV3历史交接 | 保留候选结构；POC-0/1完成度按本审计降级 |

### 7.3 历史证据重新定级

> 来源：388号 §9，L672-688

| 证据链 | 正确等级 | 可以支持 | 不可以支持 |
|---|---|---|---|
| 277/278 | Concept + Protocol | 同文本远迁移的强命题和A/B/C骨架 | 强命题已经成立 |
| 280 | Negative Evidence | 同一静态抽象Hint在该题包中无稳定效果 | 所有高Level解释都无效 |
| 283 | Contaminated package positive | lineage+题目化方向+近解答提示的整体包可救回部分题 | 同一具体Hint跨题、TellCore独立效应、自动选择或低泄漏 |
| VMS-9/10 | Mechanical smoke only | 两条硬编码记录上的过滤/关键词计数代码能够运行 | topology泛化识别、近邻Tell可分辨、自动大规模分类或因果适用性 |
| FCA 09单题 | Observational discovery | 多Level观察可能提高manifestation召回 | 六个新Core、分类完备或Hint有效 |
| 344—347 | Hypothesis / Protocol | 候选族、生成gate、Renderer形态值得测试 | 单峰规律或最佳Level已经证实 |
| 355/357/358/363 | Negative Case evidence | 候选题bare gate失败；路线/proof/output需分判 | 对目标题Tell的效力结论 |
| 旧十并发362报告 | Infrastructure positive + prediction negative | harness并发/留证可运行；预测失败不可靠 | 5次token-limit题稳定认知失败 |
| 374/380失败流 | Data/provenance evidence | 可追溯候选池和终止原因 | problem-level能力边界或Tell阳性 |
| 382 | Planned CasePack / math review pending | 候选角色和CaseCard结构 | 已冻结可运行的正确题包 |
| 383 | Design analysis | 字段必要性假设与后续消融计划 | 已做真实字段消融或POC-1因果PASS |
| 387 | Approved specification | 如何建立证据工厂 | 工厂已实现或Tell理论已通过 |

### 7.4 CC-013数学错误降级

> 来源：388号 §9.1，L689-707

382号把CC-013标为`verification_status: verified`，并声称递推 `x₁=a, x_{n+1}=2x_n+1` 对应的倒数和极限为`1/(a+1)`。这个结论显然不成立：当`a=1`时，仅第一项`S₁=1`就已经大于声称的极限`1/2`。级数确实因指数增长而收敛，但文档给出的精确值与所谓"telescoping"没有被证明，且为错。

影响是：

- CC-013不得继续标`verified`，应进入`quarantined_math_error`；
- 382号不能称为完成数学冻结的CasePack；
- 383号用CC-013说明negative boundary的相关段落只保留为设计直觉；
- 385/README沿用的"POC-0/1已完成、全部PASS"必须降为"候选题包与结构审查已完成，经验/数学确认未完成"；
- 387号独立VerificationDossier和CaseLab Gate 5因此得到一个真实回归样本。

这不是小错字，而是证明"题包设计者不能同时充当最终数学Judge"的直接反例。

---

## 附录：388号明确非主张

> 来源：388号 §13，L910-924

本审计不主张：

- v3五模式已经完备或具有自然唯一性；
- FCA已经找到真正的因果TellCore；
- 09号单题多发现六个显现等于多发现六个可用Tell；
- domain-first分区已证明优于其他Selector架构；
- "同构之桥"是所有数学迁移的正确统一名称；
- 高Level概念应始终注入每个Solver上下文；
- `case_source=mathematics`意味着对当前Solver有效；
- TellFamily存在固定单峰指导力曲线；
- 382/383已经完成经验POC-0/1；
- 当前387号证据工厂已经实现；
- 本审计已授权修改387、系统代码、数据库或运行Solver。
