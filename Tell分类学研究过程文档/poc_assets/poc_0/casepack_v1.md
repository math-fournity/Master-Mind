# POC-0 资产 · CasePack v1（冻结版）

**日期**：2026-08-17
**版本**：v1（在382号CasePack v0基础上的修订版——从Pipe 3规模化产出中精筛新题，保留v0的source_trace/metamorphic/composition）
**格式**：399号§5.1的10字段CaseCard + 399号§5.2的5否决项审查
**目标Tell家族**：局部-全局表示切换（Local Representation Switch）
**前置文档**：399号（POC-0方案）、382号（CasePack v0）、397号（简化建议）、412号（Pipe 3运行结果）
**数据来源**：ArangoDB `selection_results`集合（batch_id=selection-full1）+ 原始题库

---

## §1 冻结声明

本CasePack于2026-08-17冻结。冻结后：
- 题目角色不得变更（正迁移题不得改称假朋友题，反之亦然）
- 新增题目只能写入exclusion_log并说明排除理由
- 实验后不得追认题目角色

## §2 题包构成

| 题目类别 | 数量 | 编号 | 来源 |
|---|---:|---|---|
| source trace题 | 4道 | CC-001~CC-004 | 382号v0（历史VMS实验，359号索引P0级） |
| 正迁移题 | 6道 | CC-101~CC-106 | Pipe 3的47道YES候选题中精筛（5否决项审查） |
| 结构保持变形题 | 4道 | CC-009~CC-012 | 382号v0（基于CC-001~004构造） |
| 假朋友题 | 4道 | CC-201~CC-204 | Pipe 3的68道假朋友候选中精筛 |
| 边界题 | 2道 | CC-301~CC-302 | Pipe 3的30道边界候选中精筛 |
| 组合题 | 2道 | CC-021~CC-022 | 382号v0（人工构造） |
| **合计** | **22道** | | |

## §3 5否决项定义（399号§5.2 + 任务提示词修订）

1. **结构成立**——局部-全局表示切换确实是关键转折点（不是辅助步骤或巧合出现）
2. **bare可失败**——GLM-5.2 High bare会走错方向（有DIRECTION_ERROR记录或可预测的bare失败）
3. **泄漏安全**——Tell只给策略不给答案信息（leakage_risk=low优先，medium需审查）
4. **经典风险可控**——外壳与路线有足够新鲜度（不是训练数据中见过的经典题面）
5. **过程可观察**——thinking中能看见目标过程信号（process_signal_observability=high优先）

---

# 一、Source Trace 题（CC-001 ~ CC-004）——保留v0

> 以下4道题来自382号CasePack v0，有完整的VMS实验记录（bare失败+Tell成功对照）。
> CaseCard内容与casepack_simplified.md一致，此处不重复。

| 题号 | problem_id | 简述 | 5否决项 |
|---|---|---|---|
| CC-001 | 1631 | Mersenne型递推素数长度，k=2 | 全部通过 |
| CC-002 | 1843 | 擦去线性因子使方程无实根，2016 | 全部通过 |
| CC-003 | 1709 | t(k)最大奇因子差被4整除，a=2的幂 | 全部通过 |
| CC-004 | 1962 | 三元组ab-c等均为2的幂 | 通过（解答待完整核验） |

**详见**：`Tell分类学研究过程文档/poc_assets/poc_0/casepack_simplified.md` §一

---

# 二、正迁移题（CC-101 ~ CC-106）——从Pipe 3的47道YES精筛

> 以下6道题从Pipe 3的47道suitable=YES候选题中用5否决项精筛选出。
> 精筛原则：
> - 优先选PolyMath/Omni-MATH竞赛题（AI真正尝试了题目而非幻觉到无关领域）
> - 优先选leakage_risk=low的题
> - 覆盖不同d2子类型（mod_p_grouping/p_adic_valuation/crt/finite_field_structure）
> - 覆盖不同难度（easy/medium/hard）

---

## CC-101：polymath_00146 — 3-adic赋值着色

```yaml
CaseCard_CC101:
  case_id: CC-101
  source: pipe3_selection（batch_id=selection-full1, suitable=YES, batch=batch2, d2=p_adic_valuation）
  role: positive_transfer
  statement: |
    求最小正整数n，使得可以用n种颜色给每个正整数着色，
    且方程 w + 6x = 2y + 3z 在正整数中没有同色解
    （w,x,y,z不必互异）。
  verified_solution: |
    答案：n=4。verified。
    核心思路：用3-adic赋值v_3结合mod-3剩余分组定义4个颜色类，
    用v_3奇偶性的下降论证证明不存在同色解。
  bare_status: |
    failed（DIRECTION_ERROR）。AI探索了2-adic赋值着色（v_2 mod 2, v_2 mod 3,
    精细化的v_2+奇部mod-4着色）试图用2色完成，也测试了mod m剩余着色
    但因齐性失败——从未考虑3-adic赋值或4色。branch=root。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始讨论"3-adic"或"v_3"
    2. AI用v_3定义颜色类
    3. AI建立v_3奇偶性下降论证
    4. AI证明4色足够且3色不够
  leakage_risk: low
  frozen_role: positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 通过 | 3-adic赋值+mod-3分组是关键转折点——AI尝试2-adic失败，正确方向是3-adic |
| bare可失败 | 通过 | DIRECTION_ERROR确认——AI用2-adic替代3-adic，方向错误 |
| 泄漏安全 | 通过 | leakage_risk=low——Tell只给"切换到3-adic赋值"策略，不给具体着色方案 |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | process_signal_observability=high——v_3分析在thinking中高度可观察 |

---

## CC-102：polymath_00840 — 2-adic赋值+Fermat小定理

```yaml
CaseCard_CC102:
  case_id: CC-102
  source: pipe3_selection（batch_id=selection-full1, suitable=YES, batch=batch2, d2=p_adic_valuation）
  role: positive_transfer
  statement: |
    求所有奇数对(a,b)的和a+b，使得存在自然数c，
    让 (c^n + 1) / (2^n * a + b) 对所有自然数n为整数。
  verified_solution: |
    答案：a+b=2（即a=1,b=1）。verified。
    核心思路：用2-adic赋值v_2分析b-1迫使b=1，
    再用Fermat小定理+大素数约束a，完全避免枚举。
  bare_status: |
    failed（DIRECTION_ERROR, branch=line）。AI用逐case枚举c值
    +递推q_{n+1}的渐近增长率分析，未用p-adic赋值直接约束b。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始讨论"2-adic"或"v_2"
    2. AI用v_2分析b-1的结构
    3. AI从v_2约束推导b=1
    4. AI用Fermat小定理约束a
  leakage_risk: low
  frozen_role: positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 通过 | 2-adic赋值分析b-1是关键转折点——从枚举转向结构分析 |
| bare可失败 | 通过 | DIRECTION_ERROR确认——AI用枚举替代p-adic赋值 |
| 泄漏安全 | 通过 | leakage_risk=low——Tell只给"用v_2分析b-1"策略 |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | process_signal_observability=high——v_2分析在thinking中可观察 |

**注**：branch=line——AI的初始方向合理（分析递推）但中途未切换到p-adic赋值。测试Tell能否在中途推动表示切换。

---

## CC-103：polymath_01076 — mod 2 + mod 3的CRT组合

```yaml
CaseCard_CC103:
  case_id: CC-103
  source: pipe3_selection（batch_id=selection-full1, suitable=YES, batch=batch3, d2=crt）
  role: positive_transfer
  statement: |
    用3种颜色给整数格点着色。求最小正实数S，
    使得对任何3色着色，都存在同色格点A,B,C
    构成面积为S的三角形。
  verified_solution: |
    答案：S=3。verified。
    核心思路：用两种不同模数的着色（mod 2和mod 3）建立约束，
    mod 2给出S≥3/2，mod 3给出S≥3，组合得S=3。
    CRT风格的mod 2+mod 3组合是关键转折点。
  bare_status: |
    failed（DIRECTION_ERROR）。AI只用了一种模数着色（mod 3）得到S≥3/2，
    然后穷举尝试证明S=3/2，从未考虑第二种着色来提升下界。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始分析mod 2着色约束
    2. AI分析mod 3着色约束
    3. AI组合两个模数的约束
    4. AI从组合约束推导S=3
  leakage_risk: low
  frozen_role: positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 通过 | mod 2+mod 3的CRT组合是关键转折点——单一模数不够，需要组合 |
| bare可失败 | 通过 | DIRECTION_ERROR确认——AI只用mod 3，未考虑mod 2 |
| 泄漏安全 | 通过 | leakage_risk=low——Tell只给"考虑多种模数着色"策略 |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | process_signal_observability=high——mod 2/mod 3分析在thinking中可观察 |

**注**：本题特别适合测试CRT组合能力——Tell需要引导AI从单一模数扩展到多模数组合。

---

## CC-104：polymath_03408 — mod 500算术级数

```yaml
CaseCard_CC104:
  case_id: CC-104
  source: pipe3_selection（batch_id=selection-full1, suitable=YES, batch=extended, d2=finite_field_structure）
  role: positive_transfer
  statement: |
    将{1,2,3,...,500}排列在圆周上，使得对任意四个不同数a,b,c,d
    满足 a+b ≡ c+d (mod 500)，连接a,b和c,d的线段在圆内不相交。
    旋转相同的排列视为同一种。求排列数。
  verified_solution: |
    答案：200。verified。
    核心思路：将全局不相交条件翻译为相邻三元组的局部mod 500约束，
    推导出合法排列恰好是mod n的算术级数（线性排列多项式），
    计数为Euler函数φ(n)。φ(500)=200。
  bare_status: |
    failed（DIRECTION_ERROR）。AI通过小case枚举（n=4,n=6）猜想
    只有恒等和反转排列有效，试图证明答案为2。
    完全错过了算术级数族。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始分析相邻三元组的mod 500约束
    2. AI发现排列必须是算术级数
    3. AI推导步长k必须与n互素
    4. AI用Euler函数计数
  leakage_risk: low
  frozen_role: positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 通过 | 全局→局部mod 500约束的翻译是关键转折点 |
| bare可失败 | 通过 | DIRECTION_ERROR确认——AI用小case枚举猜想答案为2 |
| 泄漏安全 | 通过 | leakage_risk=low——Tell只给"将全局条件翻译为局部mod约束"策略 |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | process_signal_observability=high——mod 500分析在thinking中可观察 |

---

## CC-105：polymath_00083 — mod 16奇偶case分裂

```yaml
CaseCard_CC105:
  case_id: CC-105
  source: pipe3_selection（batch_id=selection-full1, suitable=YES, batch=batch1, d2=mod_p_grouping）
  role: positive_transfer
  statement: |
    设N为满足以下条件的函数f:Z/16Z→Z/16Z的个数：
    对所有a,b∈Z/16Z，
    f(a)²+f(b)²+f(a+b)² ≡ 1+2f(a)f(b)f(a+b) (mod 16)。
    求N除以2017的余数。
  verified_solution: |
    答案：793。verified。
    核心思路：对f(奇数)做奇偶case分裂（全偶vs全奇），
    结合多步mod 16二次剩余矛盾论证确定每个剩余类的值。
  bare_status: |
    failed（DIRECTION_ERROR）。AI按f(0)的值分类并用Chebyshev递推
    f(a+b)+f(a-b)=2f(a)f(b)参数化解，在f(0)=5,13时
    因不完整的mod 2/4/8/16 Hensel提升而卡住。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始对f(奇数)做奇偶分析
    2. AI按奇偶case分裂
    3. AI在每个case中用mod 16二次剩余论证
    4. AI确定每个剩余类的值并计数
  leakage_risk: low
  frozen_role: positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 通过 | 奇偶case分裂+mod 16二次剩余论证是关键转折点 |
| bare可失败 | 通过 | DIRECTION_ERROR确认——AI用Chebyshev递推替代奇偶case分裂 |
| 泄漏安全 | 通过 | leakage_risk=low——Tell只给"对f(奇数)做奇偶case分裂"策略 |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | process_signal_observability=high——奇偶case分裂在thinking中可观察 |

---

## CC-106：polymath_00021 — mod 10前缀和分组

```yaml
CaseCard_CC106:
  case_id: CC-106
  source: pipe3_selection（batch_id=selection-full1, suitable=YES, batch=batch1, d2=mod_p_grouping）
  role: positive_transfer
  statement: |
    3×9网格A，每格填正整数。如果一个m×n子网格的所有数之和
    是10的倍数，称为"好矩形"。不包含在任何好矩形中的1×1格
    称为"坏格"。求坏格的最大数量。
  verified_solution: |
    答案：25。verified。
    核心思路：反证法+2-band分组（第1行vs第2+3行），
    证明三个前缀和序列是mod 10的完全剩余系，
    从它们的和（5+5≡0 vs 必须为5）导出矛盾。
  bare_status: |
    failed（DIRECTION_ERROR）。AI探索了2D前缀和分解为6个行带函数，
    用Hall-Paige定理判断哪些函数是Z_10的排列，
    试图构造显式网格达到24个坏格。
  expected_decision: select
  expected_progress_signal: |
    1. AI开始分析前缀和的mod 10结构
    2. AI将行分为2-band分组
    3. AI证明前缀和序列是完全剩余系
    4. AI从剩余系性质导出矛盾
  leakage_risk: low
  frozen_role: positive_transfer
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 通过 | mod 10前缀和分组是关键转折点——从Hall-Paige定理转向mod 10剩余系 |
| bare可失败 | 通过 | DIRECTION_ERROR确认——AI用Hall-Paige定理替代mod 10分组 |
| 泄漏安全 | 通过 | leakage_risk=low——Tell只给"用mod 10前缀和分析"策略 |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | process_signal_observability=high——mod 10前缀和在thinking中可观察 |

---

# 三、结构保持变形题（CC-009 ~ CC-012）——保留v0

> 以下4道题来自382号CasePack v0，是CC-001~004的结构保持变形。
> CaseCard内容与casepack_simplified.md一致，此处不重复。

| 题号 | 基于 | 变形 | 5否决项 |
|---|---|---|---|
| CC-009 | CC-001/1631 | 底数2→3 | 待bare+解答核验 |
| CC-010 | CC-002/1843 | n=2016→2022 | 待bare+解答核验 |
| CC-011 | CC-003/1709 | 2-adic→3-adic | 待bare+解答核验 |
| CC-012 | CC-004/1962 | 2的幂→3的幂 | 待bare+解答核验 |

**详见**：`Tell分类学研究过程文档/poc_assets/poc_0/casepack_simplified.md` §三

---

# 四、假朋友题（CC-201 ~ CC-204）——从Pipe 3的68道假朋友候选精筛

> 以下4道题从Pipe 3的68道false_friend_candidate=yes候选中精筛选出。
> 精筛原则：
> - 表面特征像局部-全局切换问题（涉及mod/素数/整除/多项式等）
> - 但核心结构不成立（标准解答不用Z/pZ或Q_p的表示切换）
> - 优先选PolyMath竞赛题（有verified solution）
> - leakage_risk=low

---

## CC-201：polymath_00599 — megaprime计数（表面有prime/divisibility）

```yaml
CaseCard_CC201:
  case_id: CC-201
  source: pipe3_selection（batch_id=selection-full1, false_friend_candidate=yes）
  role: false_friend
  statement: |
    一个数称为megaprime如果它本身是素数、每位数字是素数、
    且各位数字之和也是素数。设S为所有n位数且每位数字都是素数的数
    的集合。设M(n)为n位megaprime数的个数。
    已知对n=2018，M(2018) ≤ C·4^{n-3} - 3·2^{n-3}。求C。
  verified_solution: |
    答案：C=11。verified。
    核心：组合集合分组——将A∪B∪C作为整体（48·4^2015+4·2^2015），
    单独下界化D的边际贡献（5·4^2015-2^2015），
    从|S|=64·4^2015中减去得C=11。
    不是局部-全局表示切换——核心在容斥原理和集合分组。
  bare_status: 不适用（假朋友题不要求bare失败）
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 不适用 | 假朋友题——结构不成立是设计目标 |
| bare可失败 | 不适用 | 假朋友题不要求bare失败 |
| 泄漏安全 | 通过 | leakage_risk=low——不应触发目标Tell |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | 如果selector误触发，说明trigger"素数/整除性"条件过宽——可观察 |

**表面相似**：涉及素数判定、数字之和的素性、整除性条件——表面像数论/模算术问题。
**结构缺失**：核心在容斥原理和组合集合分组，不在Z/pZ或Q_p的表示切换。mod出现在计数中但不是表示切换。

---

## CC-202：polymath_00697 — 被3整除数的双色着色（表面有mod 3）

```yaml
CaseCard_CC202:
  case_id: CC-202
  source: pipe3_selection（batch_id=selection-full1, false_friend_candidate=yes）
  role: false_friend
  statement: |
    被3整除的自然数被涂成红蓝两色，满足：
    蓝色+红色=红色，蓝色×红色=蓝色。
    在546为蓝色的条件下，有多少种涂法？
  verified_solution: |
    答案：7。verified。
    核心：证明蓝色数在乘法下封闭且都被最小蓝色数整除，
    然后计数546的满足条件的因数（是3的倍数的因数）。
    不是局部-全局表示切换——核心在半群闭包和因数计数。
  bare_status: 不适用（假朋友题不要求bare失败）
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 不适用 | 假朋友题——结构不成立是设计目标 |
| bare可失败 | 不适用 | 假朋友题不要求bare失败 |
| 泄漏安全 | 通过 | leakage_risk=low |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | 如果selector误触发，说明trigger"被3整除"条件过宽——可观察 |

**表面相似**：条件涉及"被3整除"和"涂色"——表面像mod 3分组问题。
**结构缺失**：核心在半群闭包性质和因数计数，不在mod 3的表示切换。"被3整除"只是数的筛选条件，不是表示切换的目标。

---

## CC-203：polymath_01136 — 部分和mod d的鸽巢（表面有mod d）

```yaml
CaseCard_CC203:
  case_id: CC-203
  source: pipe3_selection（batch_id=selection-full1, false_friend_candidate=yes）
  role: false_friend
  statement: |
    n个球（n>3），每个球上写一个整数。求最大自然数d，
    使得对任意写在球上的数，总能找到至少4种不同方式
    选一些球使它们上面的数之和被d整除。
  verified_solution: |
    答案：d=n/4。verified。
    核心：鸽巢原理——n个数的前缀和mod d必有重复，
    再用2^n个子集分配到n/4个剩余类的计数论证。
    不是局部-全局表示切换——"mod d"只是鸽巢的工具，不是表示切换。
  bare_status: 不适用（假朋友题不要求bare失败）
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 不适用 | 假朋友题——结构不成立是设计目标 |
| bare可失败 | 不适用 | 假朋友题不要求bare失败 |
| 泄漏安全 | 通过 | leakage_risk=low |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | 如果selector误触发，说明trigger"mod d"条件过宽——可观察 |

**表面相似**：条件涉及"部分和被d整除"——表面像mod p分组问题。
**结构缺失**：核心在鸽巢原理和子集计数，不在Z/pZ的表示切换。"mod d"是鸽巢原理的工具，不是表示切换的目标。AI实际尝试了零和子集计数（Davenport常数+Z/dZ上的Fourier分析），比标准解答更接近局部-全局切换但仍不是——说明trigger需要区分"在Z/dZ上工作"和"通过Z/dZ切换表示来揭示隐藏结构"。

---

## CC-204：polymath_00824 — 集合A+B mod N²（表面有mod）

```yaml
CaseCard_CC204:
  case_id: CC-204
  source: pipe3_selection（batch_id=selection-full1, false_friend_candidate=yes）
  role: false_friend
  statement: |
    设S={0,1,...,N²-1}（N=10）。A是S中恰好N个元素的子集。
    定义A+B={a+b mod N² | a∈A, b∈B}。
    求最大整数m使得对任意A，存在B（|B|=N）使|A+B|≥m。
  verified_solution: |
    答案：m=50。verified。
    核心：概率方法——随机选B为N元素多重集，
    计算E[|A+B|]=N²[1-(1-1/N)^N]>N²/2=50。
    不是局部-全局表示切换——核心在概率方法/期望论证。
  bare_status: 不适用（假朋友题不要求bare失败）
  expected_decision: reject
  expected_progress_signal: 无——不应触发目标Tell
  leakage_risk: low
  frozen_role: false_friend
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 不适用 | 假朋友题——结构不成立是设计目标 |
| bare可失败 | 不适用 | 假朋友题不要求bare失败 |
| 泄漏安全 | 通过 | leakage_risk=low |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | 如果selector误触发，说明trigger"mod N²"条件过宽——可观察 |

**表面相似**：条件涉及"mod N²"和集合运算——表面像mod p分组问题。
**结构缺失**：核心在概率方法（期望论证），不在Z/pZ的表示切换。AI实际尝试了加法组合（CRT分解Z_100=Z_4×Z_25、Kneser定理、差集分析），比标准解答更接近局部-全局切换但仍不是——说明trigger需要区分"在Z/nZ上做组合"和"通过Z/pZ切换表示来揭示隐藏结构"。

---

# 五、边界题（CC-301 ~ CC-302）——从Pipe 3的30道边界候选精筛

> 以下2道题从Pipe 3的30道boundary_case_candidate=yes候选中精筛选出。
> 精筛原则：
> - AI已经触及局部-全局切换方向但未完成（测试"正确表示但不完整执行"边界）
> - 或AI用了正确的p-adic方向但执行错误（测试"正确方向但执行失败"边界）
> - leakage_risk=low
> - 有verified solution

---

## CC-301：polymath_00781 — AI已用F_2/Lucas但未完成

```yaml
CaseCard_CC301:
  case_id: CC-301
  source: pipe3_selection（batch_id=selection-full1, boundary_case_candidate=yes, suitable=NO）
  role: boundary
  statement: |
    对整系数多项式P(x)=a_0+a_1x+...+a_kx^k，
    令o(P)为奇系数a_i的个数。
    令Q_i(x)=(1+x)^i。给定i_1=11且11<i_2<i_3<i_4，
    求 o(Q_{i_1}+Q_{i_2}+Q_{i_3}+Q_{i_4}) 的最小可能值。
  verified_solution: |
    答案：8。verified。
    核心：用一般不等式o(ΣQ_{i_j})≥o(Q_{i_1})将问题归约到
    计算o(Q_11)=8（用Lucas定理：C(11,k)为奇当且仅当
    k的二进制是11的二进制(1011)的子集，共8个子集）。
  bare_status: |
    failed（PARTIAL_PROGRESS, branch=line）。AI已在F_2上工作，
    尝试最小化(1+x)^11+(1+x)^{i_2}+(1+x)^{i_3}+(1+x)^{i_4}
    的Hamming重量，搜索达到重量2或4的构造——
    已触及局部表示（F_2）但未发现一般不等式o(ΣQ)≥o(Q_{i_1})。
  expected_decision: boundary
  expected_progress_signal: |
    AI已在F_2上工作 → 测试Tell能否推动AI发现一般不等式
    如果Tell推动AI发现o(ΣQ)≥o(Q_{i_1})，则Tell在此边界case中有效。
    如果AI已在F_2上但Tell无法帮助发现不等式，说明Tell的"操作路径"层面需要增强。
  leakage_risk: low
  frozen_role: boundary
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 边界 | Lucas定理mod 2是关键转折点，但AI已经触及——测试Tell在"已触及但未完成"时的效果 |
| bare可失败 | 边界 | AI未完全失败（PARTIAL_PROGRESS）——测试"部分进展"时Tell的边际效用 |
| 泄漏安全 | 通过 | leakage_risk=low——Tell只给"用Lucas定理分析o(Q_11)"策略 |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | process_signal_observability=high——F_2/Lucas分析在thinking中可观察 |

**边界价值**：本题测试Tell在AI已进入局部表示但未发现关键不等式时的效果。如果Tell能推动AI发现o(ΣQ)≥o(Q_{i_1})，说明Tell的"操作路径"层面有效。如果不能，说明Tell需要更强的操作路径指引。

---

## CC-302：polymath_01064 — AI已用p-adic但执行错误

```yaml
CaseCard_CC302:
  case_id: CC-302
  source: pipe3_selection（batch_id=selection-full1, boundary_case_candidate=yes, suitable=NO）
  role: boundary
  statement: |
    对非负整数p,q,r，令f(p,q,r)=(p!)^p(q!)^q(r!)^r。
    求最小正整数n，使得对任意满足a+b+c=2020的三元组(a,b,c)
    和满足x+y+z=n的三元组(x,y,z)，f(x,y,z)被f(a,b,c)整除。
  verified_solution: |
    答案：n=6052。verified。
    核心：用v_{2017}的p-adic赋值分析，观察到最坏情况不是平衡三元组
    而是恰好一个变量刚超过2017的情形，n=6052是迫使该变量≥2020的阈值。
  bare_status: |
    failed（PARTIAL_PROGRESS, branch=line）。AI已用p-adic赋值分析
    且正确识别了ℓ=2017为约束素数，但错误地应用了凸性/Schur凸性论证
    声称平衡三元组是最坏情况，导致错误答案6050。
  expected_decision: boundary
  expected_progress_signal: |
    AI已用v_{2017} → 测试Tell能否推动AI发现最坏情况不是平衡三元组
    如果Tell推动AI检查非平衡情形，则Tell的"critic"层面有效。
    如果AI已用p-adic但Tell无法帮助发现执行错误，说明Tell的critic需要增强。
  leakage_risk: low
  frozen_role: boundary
```

### 5否决项审查

| 否决项 | 结果 | 说明 |
|---|---|---|
| 结构成立 | 边界 | v_{2017}的p-adic赋值是关键转折点，但AI已用——测试Tell在"已用但执行错误"时的效果 |
| bare可失败 | 边界 | AI未完全失败（PARTIAL_PROGRESS，得到6050接近6052）——测试"接近但错误"时Tell的边际效用 |
| 泄漏安全 | 通过 | leakage_risk=low——Tell只给"检查非平衡三元组是否更坏"策略 |
| 经典风险可控 | 通过 | 竞赛题面足够新鲜 |
| 过程可观察 | 通过 | process_signal_observability=high——v_{2017}分析在thinking中可观察 |

**边界价值**：本题测试Tell在AI已用正确p-adic方向但执行错误时的效果。如果Tell的critic能推动AI检查非平衡情形，说明critic有效。如果不能，说明critic需要更强的"执行验证"指引。

---

# 六、组合题（CC-021 ~ CC-022）——保留v0

> 以下2道题来自382号CasePack v0，测试局部表示切换与其他Tell的组合。
> CaseCard内容与casepack_simplified.md一致，此处不重复。

| 题号 | 组合类型 | 5否决项 |
|---|---|---|
| CC-021 | 局部表示切换+构造性Tell（顺序依赖） | 待bare+解答核验+泄漏确认 |
| CC-022 | 模p分析+模q分析（互补协同） | 待bare+解答核验 |

**详见**：`Tell分类学研究过程文档/poc_assets/poc_0/casepack_simplified.md` §六

---

# 七、Exclusion Log（被排除的题+排除原因）

## 7.1 从47道YES候选中排除的41道

排除原因分类：

### 7.1.1 否决项1不通过——局部-全局切换不是关键转折点（太trivial）

| problem_id | 排除原因 |
|---|---|
| oda_math_460k_00064801 | "227n被15整除"——只是基本整除规则，不是表示切换 |
| oda_math_460k_00062677 | "数字根"——只是n mod 9的已知技巧，太trivial |
| oda_math_460k_00063281 | "P(c)被101整除，暴力检查"——只是mod 101暴力枚举，不是表示切换 |
| deepmath_103k_00008329 | "环同态计数到F_2[x]/..."——有限域只是背景设定，不是关键转折点 |
| deepmath_103k_00008548 | "Z[x]中的极大理想"——交换代数，不是局部-全局切换 |
| deepmath_103k_00030623 | "Z_7[x]/(x²-6)可逆性"——只是mod 7基本计算，不是表示切换 |

### 7.1.2 否决项2不通过——AI幻觉到完全无关领域（不是数学方向错误）

| problem_id | AI幻觉方向 |
|---|---|
| oda_math_460k_00054685 | Einstein场方程/Yang-Mills |
| oda_math_460k_00059280 | 3-free排列 |
| deepmath_103k_00028372 | Γ(cot(e^{-x²})+1)幂级数 |
| deepmath_103k_00003175 | C∞函数/Taylor级数发散 |
| deepmath_103k_00009181 | 代数几何/约化群作用 |
| deepmath_103k_00016766 | 双曲环面自同构 |
| deepmath_103k_00030415 | 连续性/可数选择公理 |
| oda_math_460k_00000663 | 三角形垂心/内切圆 |
| deepmath_103k_00002386 | 概率论/特征函数收敛 |
| deepmath_103k_00018140 | Jacobi形式 |
| deepmath_103k_00020347 | 微分拓扑/不可定向流形 |
| deepmath_103k_00021048 | Hamel基/不可测集 |
| deepmath_103k_00031509 | 无关数论问题 |
| omni_math_003900 | 无关除数函数问题 |
| omni_math_000324 | e的偏和分母 |
| omni_math_000096 | 无关泛函方程 |
| omni_math_003964 | 无关Mersenne数floor函数 |
| deepmath_103k_00000973 | 有限域多项式GCD（AI幻觉） |
| deepmath_103k_00017608 | 椭圆曲线2-isogeny下降（AI幻觉） |

> **注**：这些题的AI"失败"不是数学方向错误而是幻觉到完全无关的问题。
> 对这些题，Tell（局部-全局切换）不会有因果作用——因为AI根本没在做这道题。
> 保留CC-101~106是因为那些题的AI真正尝试了题目但走了错误的数学方向。

### 7.1.3 否决项3不通过——泄漏风险medium（降低优先级）

| problem_id | leakage_risk | 说明 |
|---|---|---|
| deepmath_103k_00021333 | medium | mod 2 parity——提示"用mod 2"可能过于接近答案 |
| oda_math_460k_00045721 | medium | 2^n mod 7——提示"用mod 7"可能泄漏乘法阶 |
| oda_math_460k_00051954 | medium | mod-3 grouping——提示"用mod 3"可能过于直接 |
| polymath_00072 | medium | 棋盘parity——提示"用parity coloring"可能过于直接 |
| polymath_01187 | medium | mod-4-sum——提示"用mod 4分组"可能过于直接 |
| oda_math_460k_00065150 | medium | 乘法阶——提示"用乘法阶"可能泄漏周期 |
| deepmath_103k_00020347 | medium | F_p^×循环群——提示"用循环群结构"可能过于直接 |
| deepmath_103k_00030623 | medium | Z_7商环——提示"用Z_7"可能过于直接 |

### 7.1.4 否决项4不通过——经典风险（题面太常见）

| problem_id | 说明 |
|---|---|
| deepmath_103k_00002261 | "二项式系数全奇"——Lucas定理经典应用，训练痕迹强 |

### 7.1.5 备选题（通过5否决项但未入选，因名额限制）

以下题通过5否决项但未入选正迁移题（已选6道），作为备选：

| problem_id | d2子类型 | leak | diff | 备选理由 |
|---|---|---|---|---|
| polymath_00871 | mod_p_grouping | low | easy | branch=line，mod 3分组 |
| polymath_01763 | multi_step_mod_p | low | medium | 模算术tiling |
| polymath_02641 | mod_p_non_obvious | low | medium | mod 5鸽巢 |
| polymath_03303 | mod_p_non_obvious | low | medium | 素因子分解 |
| omni_math_004105 | mod_p_grouping | low | easy | parity mod 2 |
| omni_math_000114 | multi_step_mod_p | low | medium | Fermat小定理 |
| omni_math_004190 | finite_field_structure | low | hard | (Z/pZ)*博弈 |

---

## 7.2 从68道假朋友候选中排除的64道

排除原因：表面特征与局部-全局切换不够相似（如纯分析/几何/组合问题），或leakage_risk=medium。

---

## 7.3 从30道边界候选中排除的28道

排除原因：边界特征不够清晰，或AI未触及局部-全局切换方向（不是真正的边界case），或leakage_risk=medium。

---

## 7.4 389号题目纠错记录检查

**polymath_00995**（标准答案3800有误，正确答案5048）——已检查，polymath_00995不在47道YES候选中，不在68道假朋友候选中，不在30道边界候选中。无需处理。

---

# 八、5否决项审查汇总

## 8.1 新选题（CC-101~106, CC-201~204, CC-301~302）汇总

| 题号 | 结构成立 | bare可失败 | 泄漏安全 | 经典风险 | 过程可观察 | 总体 |
|---|---|---|---|---|---|---|
| CC-101 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-102 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-103 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-104 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-105 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-106 | ✅ | ✅ | ✅ | ✅ | ✅ | **全部通过** |
| CC-201 | N/A | N/A | ✅ | ✅ | ✅ | 假朋友通过 |
| CC-202 | N/A | N/A | ✅ | ✅ | ✅ | 假朋友通过 |
| CC-203 | N/A | N/A | ✅ | ✅ | ✅ | 假朋友通过 |
| CC-204 | N/A | N/A | ✅ | ✅ | ✅ | 假朋友通过 |
| CC-301 | 边界 | 边界 | ✅ | ✅ | ✅ | 边界通过 |
| CC-302 | 边界 | 边界 | ✅ | ✅ | ✅ | 边界通过 |

## 8.2 保留v0题（CC-001~004, CC-009~012, CC-021~022）汇总

| 题号 | 总体 | 说明 |
|---|---|---|
| CC-001~003 | 全部通过 | 强证据题，VMS实验记录完整 |
| CC-004 | 通过（解答待核验） | source trace + boundary_case_for_direction_vs_path |
| CC-009~012 | 待bare+解答核验 | 变形题，解答未核验 |
| CC-021~022 | 待bare+解答核验 | 组合题，解答未核验 |

## 8.3 可立即用于POC的题（5否决项全部通过或仅不适用项）

- **CC-001, CC-002, CC-003, CC-007(v0)**：全部通过——强证据题
- **CC-101~CC-106**：全部通过——6道新正迁移题，从Pipe 3精筛
- **CC-201~CC-204**：假朋友题全部通过——4道新假朋友，从Pipe 3精筛
- **CC-301~CC-302**：边界题全部通过——2道新边界，从Pipe 3精筛
- **CC-004**：通过（解答待完整核验）——source trace题

## 8.4 需要后续验证才能使用的题

- **需bare+解答核验**：CC-009~012（变形题）, CC-021~022（组合题）

---

# 九、与v0的差异说明

| 维度 | v0（382号） | v1（本文档） |
|---|---|---|
| 正迁移题 | 4道（CC-005~008），3道历史+1道构造 | 6道（CC-101~106），全部从Pipe 3精筛 |
| 假朋友题 | 5道（CC-013~017），全部人工构造 | 4道（CC-201~204），全部从Pipe 3精筛 |
| 边界题 | 3道（CC-018~020），全部人工构造 | 2道（CC-301~302），全部从Pipe 3精筛 |
| source trace | 4道（CC-001~004） | 4道（CC-001~004），保留v0 |
| 变形题 | 4道（CC-009~012） | 4道（CC-009~012），保留v0 |
| 组合题 | 2道（CC-021~022） | 2道（CC-021~022），保留v0 |
| **总计** | 22道 | 22道 |

**v1的改进**：
1. **正迁移题从Pipe 3规模化产出中精筛**——不再依赖人工构造，有真实的DIRECTION_ERROR记录和Pipe 3的6项预评数据
2. **假朋友题从Pipe 3的语义判断中精筛**——不再人工构造，有真实的false_friend_candidate标注和标准解答
3. **边界题从Pipe 3的边界候选中精筛**——不再人工构造，有真实的boundary_case_candidate标注和AI的PARTIAL_PROGRESS记录
4. **覆盖更多d2子类型**——v0主要覆盖mod_p_grouping和p_adic_valuation，v1新增crt和finite_field_structure
5. **保留v0的source trace/变形/组合**——这些有独特的VMS实验记录和结构关系，Pipe 3无法替代

---

# 十、数据来源与可追溯性

## 10.1 Pipe 3产出查询

```python
# 从ArangoDB获取Pipe 3产出
import sys; sys.path.insert(0, 'analysis-devin-failure-system')
from src.db_schema import connect_db
db = connect_db()
# 获取47道YES候选题
aql = 'FOR r IN selection_results FILTER r.batch_id == "selection-full1" FILTER r.suitable == "YES" RETURN r'
yes_candidates = list(db.aql.execute(aql, ttl=120))
# 获取68道假朋友候选
aql = 'FOR r IN selection_results FILTER r.batch_id == "selection-full1" FILTER r.false_friend_candidate == "yes" RETURN r'
false_friends = list(db.aql.execute(aql, ttl=120))
# 获取30道边界候选
aql = 'FOR r IN selection_results FILTER r.batch_id == "selection-full1" FILTER r.boundary_case_candidate == "yes" RETURN r'
boundary_cases = list(db.aql.execute(aql, ttl=120))
```

## 10.2 题面和标准解答来源

题面和标准解答从原始题库获取（DATASET_PATHS配置）：
- PolyMath: `/data/math-manify/raw_downloads/PolyMath/data/train-00000-of-00001.parquet`
- Omni-MATH: `/data/math-manify/raw_downloads/Omni-MATH-2/Omni-Math-2.jsonl`

## 10.3 完整数据文件

`analysis-devin-failure-system/output/poc0_candidates_full.json`（1704 KB）——包含145道候选题的完整数据（Pipe 3产出+题面+标准解答+6项POC准备数据）。

## 10.4 获取脚本

`analysis-devin-failure-system/scripts/fetch_poc0_candidates.py`——从ArangoDB获取Pipe 3产出
`analysis-devin-failure-system/scripts/fetch_poc0_with_problems.py`——合并原始题库题面和解答

---

# 十一、Solver模型

```text
主模型：glm-5.2-high
Solver：通过 solver_harness.py launch 启动
```

---

# 十二、通过标准检查（399号§7）

| 标准 | 状态 |
|---|---|
| 每道正迁移题有bare失败或明确准入理由 | ✅ CC-101~106全部有DIRECTION_ERROR记录 |
| 每道假朋友题说明"为什么表面相似、为什么结构不应触发" | ✅ CC-201~204每道有表面相似+结构缺失说明 |
| 每道边界题只改变一个关键条件 | ✅ CC-301~302每道说明边界特征（AI已触及但未完成/已用但执行错误） |
| 每道题都预注册预期触发/不触发/弃权 | ✅ expected_decision字段已填写 |
| 写明哪些题来自历史记录，哪些是新构造 | ✅ source trace/变形/组合来自v0，正迁移/假朋友/边界来自Pipe 3 |
| 写明禁止在实验后移动题目类别 | ✅ frozen_role字段已冻结，§1冻结声明已写明 |
