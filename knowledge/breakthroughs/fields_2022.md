# 2022年菲尔兹奖得主及其工作

> 菲尔兹奖（Fields Medal）是数学界最高荣誉之一，每四年在国际数学家大会（ICM）上颁发，授予40岁以下的杰出数学家。2022年颁奖原定于在圣彼得堡举行的ICM上宣布，因俄乌战争改为线上举行。2022年的四位得主为：Hugo Duminil-Copin、James Maynard、Maryna Viazovska、June Huh。

---

## 1. Hugo Duminil-Copin（1985– ）

**机构**：日内瓦大学 / 法国高等科学研究所（IHES）

**颁奖理由**：对统计相变随机介质数学理论的深刻贡献，特别是在Ising模型和渗流理论方面。

### 1.1 研究领域概述

Duminil-Copin的工作核心在于**统计力学中的相变现象**的严格数学理论。统计力学研究由大量微观自由度组成的系统的宏观行为，相变指的是系统参数（如温度）越过某个临界值时宏观行为的突变。这类现象的严格处理极其困难，因为关键信息往往被隐藏在"临界点"附近，而临界点处传统的工具（如高温展开、低温展开）都失效。

他的主要工具是**随机簇模型（Random Cluster Model, FK表示）**，这是Fortuin与Kasteleyn在1972年提出的一种统一框架，参数为 $q \in [1,\infty)$ 的随机簇模型同时推广了：
- $q \to 1$：独立渗流（Bernoulli percolation）；
- $q = 2$：Ising模型；
- $q \geq 1$ 的一般 Potts 模型。

### 1.2 连续相变的存在性证明

**核心问题**：对于 $\mathbb{Z}^d$（$d \geq 3$）上的随机簇模型，临界点 $p_c(q)$ 处是否存在相变？更精确地，是否 $p \mapsto \theta(p)$（无穷连通分支的存在概率）在 $p_c$ 处不连续？

长期以来，即使在最经典的 Ising 模型（$q=2$）中，$d \geq 3$ 维情形下相变是连续还是不连续都是未解决的难题。二维情形由 Smirnov、Werner 等人通过共形不变性解决，但高维缺乏工具。

**Duminil-Copin 的贡献**：

1. **与 Tassion 合作（2020）**：证明了对于 $\mathbb{Z}^d$（$d \geq 2$）上 $q \geq 1$ 的随机簇模型，**预期磁化率（susceptibility）的临界指数**满足严格界。他们引入了一种新的"随机性揭示"（random-current / pivotal argument 的变体）方法，绕过了传统的反射原理限制。

2. **与 Raoufi, Tassion 合作（2019）**：证明了在 $d \geq 3$ 维中，对于 $q \geq 1$，**指数衰减在亚临界区域成立**，即当 $p < p_c(q)$ 时连通函数指数衰减。这解决了长期悬而未决的问题——此前仅有 $q=1$（Aizenman-Barsky, Menshikov）和 $q \geq 2$（通过随机簇对偶与随机电流方法）的部分结果。

3. **连续相变**：Duminil-Copin 与 Sidoravicius, Tassion 等合作，在若干模型中证明了相变的**连续性**（即 $\theta(p_c) = 0$，临界点处无穷簇不存在）。关键结果包括：
   - **Ising 模型（$q=2$）在 $d=3,4$ 维的连续性**（与 Sidoravicius, Tassion 合作）；
   - **$q \in [1,4]$ 的二维随机簇模型的连续性**（利用对偶性）。

### 1.3 Ising 模型的严格结果

Ising 模型是统计力学中最经典的模型之一，描述铁磁相变。Duminil-Copin 的关键贡献：

- **与 Gagnebin, Harutyunyan, Li, Manolescu 合作**：系统研究了 Ising 模型在 $\mathbb{Z}^d$ 上的随机电流表示（random current representation），给出了磁化强度的严格表达式和不等式。
- **随机电流方法的发展**：与 Duminil-Copin 之前的工作者（特别是 Duminil-Copin 的导师 Smirnev 以及 Werner）不同，他将随机电流方法推广到高维，得到了 Ising 模型的**磁化强度在临界点附近的行为**的精细刻画。

### 1.4 随机簇模型的深入结果

- **与 Duminil-Copin, Sidoravicius, Tassion**：随机簇模型的**相变锐利性（sharpness of phase transition）**——证明了在 $d \geq 2$ 维中，对于所有 $q \geq 1$，临界点 $p_c(q)$ 处相变是锐利的，即亚临界区域指数衰减、超临界区域存在无穷簇。这是对经典 Bernoulli 渗流结果（Aizenman-Barsky, Menshikov）的巨大推广。
- **临界点的精确值**：对于二维随机簇模型，利用对偶性给出 $p_c(q) = \sqrt{q}/(1+\sqrt{q})$ 的严格证明（与 Beffara, Duminil-Copin 合作，推广了之前 $q=1,2$ 的结果）。

### 1.5 方法论意义

Duminil-Copin 的核心方法论贡献在于：**将随机电流表示（random current）与随机簇表示结合**，发展出一套处理 $q \geq 1$ 模型的统一技术。这套技术绕过了传统方法对二维结构或特殊 $q$ 值的依赖，使得高维、一般 $q$ 的严格结果成为可能。

---

## 2. James Maynard（1987– ）

**机构**：牛津大学

**颁奖理由**：对解析数论的深刻贡献，特别是在理解素数结构方面的重大进展。

### 2.1 研究领域概述

Maynard 的工作集中在**素数分布**的精细问题上，特别是关于素数间隔（gaps between primes）的问题。他的核心突破在于对 GPY 筛法（Goldston-Pintz-Yıldırım 筛法）的根本性改进。

### 2.2 Maynard-Tao 方法

**背景**：2005年，Goldston, Pintz, Yıldırım 证明了
$$\liminf_{n\to\infty} \frac{p_{n+1}-p_n}{\log p_n} = 0,$$
即素数间隔与对数尺度相比可以任意小。但他们无法证明存在无穷多对间隔有界的素数（即 $\liminf (p_{n+1}-p_n) < \infty$）。

GPY 方法的核心是利用**Erdős-Rankin 型的筛法**结合**素数定理在算术级数中的平均分布**。其关键障碍在于：GPY 方法能利用的素数分布信息受限于**Bombieri-Vinogradov 定理**的水平（模 $q$ 的平均误差项 $O(x^{1/2+\epsilon})$），而要得到有界间隔，需要超越这个水平。

**Maynard 的突破（2015）**：

Maynard（以及独立地 Tao）提出了一种全新的方法，其核心思想是**不再只寻找一对素数，而是寻找 $m$-元组中至少有两个素数**。具体地：

1. 考虑 $k$-元组 $\{n+h_1, \ldots, n+h_k\}$（admissible $k$-tuple）；
2. 用**多重 Selberg 筛法**构造权重，使得"至少两个元素为素数"的事件被放大；
3. 关键创新：使用**多个 $\theta$ 函数的线性组合**而非 GPY 中的单一 $\theta$ 函数，从而绕过了 Bombieri-Vinogradov 障碍。

**结果**：对于足够大的 $k$，存在无穷多个 $n$ 使得 $\{n+h_1,\ldots,n+h_k\}$ 中至少有两个素数。由此得到：
$$\liminf_{n\to\infty} (p_{n+1} - p_n) \leq 600.$$
（后续 Polymath8 项目将此常数优化到 246。）

**与 Zhang 的关系**：2013年张益唐率先证明了 $\liminf (p_{n+1}-p_n) < \infty$（具体上界为 70,000,000），用的是完全不同的方法（基于 Deligne 对 Weil 猜想的证明来控制模 $q$ 的分布）。Maynard-Tao 方法更简洁、更灵活，且能推广到其他问题。

### 2.3 小素数间隔的突破

Maynard 进一步改进了素数间隔的上界：

- **$\liminf (p_{n+1}-p_n) \leq 246$**（与 Polymath8b 合作）；
- **Erdős 猜想的进展**：Erdős 曾猜想 $\liminf (p_{n+1}-p_n) / \log p_n \to 0$ 的各种强化形式。Maynard 证明了对于任意 $m$，
  $$\liminf_{n\to\infty} (p_{n+m} - p_n) \leq C_m,$$
  即存在无穷多组 $m+1$ 个素数落在长度有界的区间内。

### 2.4 Linnik 问题的进展

**Linnik 问题**：给定两个互素的正整数 $a, d$，问存在多小的素数 $p \equiv a \pmod{d}$？Linnik 证明了存在常数 $L$ 使得 $p \leq d^L$。

Maynard 在**小素数在算术级数中**的问题上取得突破：

- **与最大素因子相关**：证明了在算术级数 $a \pmod{q}$ 中，存在素数 $p \leq q^{5.2}$（改进了之前 $q^{5.5}$ 量级的结果，向 Linnik 猜想的 $q^{1+\epsilon}$ 迈进）。
- **几乎素数在算术级数中**：证明了存在无穷多 $n$ 使得 $n$ 在给定算术级数中且 $n$ 有至多 2 个素因子（$P_2$），这是陈景润型结果在算术级数中的推广。

### 2.5 其他重要贡献

- **Duffin-Schaeffer 猜想**（与 Koukoulopoulos 合作，2019）：证明了有理数逼近的 Duffin-Schaeffer 猜想，这是丢番图逼近中长达80年的核心问题。他们用全新的图论/概率方法取代了传统的覆盖引理。
- **缺失数字的素数**：证明了存在无穷多素数其十进制表示中不包含某个给定数字（如不含数字 7 的素数有无穷多个）。

---

## 3. Maryna Viazovska（1984– ）

**机构**：洛桑联邦理工学院（EPFL）

**颁奖理由**：证明了8维和24维中球填充问题的最优解，以及相关极值问题和傅里叶分析中问题的深刻贡献。

### 3.1 球填充问题

**问题**：在 $\mathbb{R}^d$ 中，如何用不相交的单位球填充空间，使得填充密度最大？设最大密度为 $\Delta_d$。

- $d=1$：$\Delta_1 = 1$（平凡）；
- $d=2$：$\Delta_2 = \frac{\pi}{2\sqrt{3}}$（高斯，1831；严格证明由 Tóth, 1940）；
- $d=3$：$\Delta_3 = \frac{\pi}{3\sqrt{2}}$（Kepler 猜想，Hales, 1998-2014，Flyspeck 项目形式化验证）；
- $d \geq 4$：长期未知。

### 3.2 Cohn-Elkies 方法

2001年，Cohn 与 Elkies 提出了一种基于**傅里叶分析**的上界方法：

**定理（Cohn-Elkies）**：若存在 Schwartz 函数 $f: \mathbb{R}^d \to \mathbb{R}$ 满足：
1. $f(0) = \hat{f}(0) = 1$（归一化）；
2. $f(x) \leq 0$ 对 $|x| \geq r$（实空间衰减条件）；
3. $\hat{f}(t) \geq 0$ 对所有 $t$（傅里叶空间非负条件）；

则球填充密度 $\Delta_d \leq f(0) / r^d \cdot \text{vol}(B^d)$。

在 $d=8$ 和 $d=24$ 中，Cohn-Elkies 给出的上界与已知的格填充密度**数值上吻合到15位有效数字**，强烈暗示这些格就是最优解，但无法严格证明。

### 3.3 Viazovska 的突破

**8维（2016）**：Viazovska 构造了一个满足 Cohn-Elkies 条件的函数 $f$，其对应的密度上界恰好等于 $E_8$ 格的填充密度 $\Delta_8 = \frac{\pi^4}{384} \approx 0.25367$。

**关键创新**：她使用了**模形式（modular forms）**。具体地：

1. $E_8$ 格的 theta 函数 $\Theta_{E_8}(\tau) = \sum_{x \in E_8} q^{(x,x)/2}$ 是 $SL_2(\mathbb{Z})$ 上权 4 的模形式，等于 Eisenstein 级数 $E_4(\tau)$。

2. Viazovska 将问题转化为构造一个特殊的**插值问题**：寻找满足特定边界条件的整函数，使得其 Fourier 变换具有非负性。

3. 她利用了**$E_8$ 格的自对偶性**和模形式的性质，构造出函数
   $$f(r) = \sum_{n=0}^{\infty} a_n \left(\frac{r}{\sqrt{2n}}\right)^4 J_4(\pi r \sqrt{2n})^2 \cdot (\text{修正项}),$$
   其中 $J_4$ 是 Bessel 函数，$a_n$ 由模形式的 Fourier 系数决定。

4. 核心难点在于证明 $\hat{f}(t) \geq 0$。Viazovska 通过巧妙的**模形式变换公式**和**Laplace 变换**技术完成了这一证明。

**24维（2016，与 Cohn, Kumar, Miller, Radchenko 合作）**：将上述方法推广到 Leech 格 $\Lambda_{24}$。Leech 格的 theta 函数涉及权 12 的模形式，技术难度更大。他们构造了相应的函数，证明了 $\Delta_{24} = \frac{\pi^{12}}{12!} \approx 0.001929$。

### 3.4 与 Cohn-Elkies 方法的联系

Viazovska 的方法本质上是**找到了 Cohn-Elkies 框架中的最优函数**。关键洞察是：

- 在 $d=8, 24$ 中，最优函数不是"普通"的 Schwartz 函数，而是由**模形式系数驱动的特殊构造**；
- $d=8$ 和 $d=24$ 的特殊性在于：$E_8$ 和 $\Lambda_{24}$ 是**偶自对偶格**，其 theta 函数是模形式，这提供了构造所需的代数结构；
- 其他维度（如 $d=4$）没有对应的偶自对偶格，因此这种方法无法直接推广。

### 3.5 后续工作

- **通用最优性**：Viazovska 与合作者进一步研究了**球填充的局部最优性**和**universal optima**（在所有完全单调势能函数下都最优的构型）。
- **设计理论**：将模形式方法与组合设计理论联系。

---

## 4. June Huh（1983– ）

**机构**：普林斯顿高等研究院（IAS）

**颁奖理由**：将代数几何中的 Hodge 理论引入组合学，证明了 Dowling-Wilson 几何格猜想和 Rota 猜想。

### 4.1 研究领域概述

Huh 的核心贡献在于**在组合学中建立类似代数几何中 Hodge 理论的结构**。代数几何中的 Hodge 理论将拓扑（上同调）与分析（调和形式）通过 Hodge 分解联系起来，是现代几何的核心工具。Huh 发现组合学中的许多长期猜想本质上是"Hodge 型"的，可以用代数几何的方法解决。

### 4.2 Read 猜想

**Read 猜想（1968）**：图的色多项式 $\chi_G(t)$ 的系数序列是**单峰的（unimodal）**，即系数先增后减。

更精确地，设 $\chi_G(t) = \sum_{k=0}^{n} a_k t^k$，则存在 $k^*$ 使得 $|a_0| \leq |a_1| \leq \cdots \leq |a_{k^*}| \geq \cdots \geq |a_n|$。

**Huh 的证明（2012）**：

Huh 通过将图与代数簇联系起来解决此问题。关键步骤：

1. 对于图 $G$，考虑其关联的**图超平面配置（graphical arrangement）**，即超平面 $x_i - x_j = 0$（对每条边 $\{i,j\}$）在 $\mathbb{C}^n$ 中的布置。

2. 色多项式 $\chi_G(t)$ 等于该超平面配置的**特征多项式** $\chi_{\mathcal{A}}(t)$。

3. 超平面配置的补集 $M(\mathcal{A}) = \mathbb{C}^n \setminus \bigcup \mathcal{A}$ 的上同调环 $H^*(M(\mathcal{A}))$ 具有类似 Hodge 结构的性质。

4. Huh 证明了特征多项式系数的对数凹性（log-concavity）：
   $$a_k^2 \geq a_{k-1} \cdot a_{k+1} \cdot \frac{k}{k-1} \cdot \frac{n-k}{n-k+1},$$
   这比单峰性更强，直接蕴含 Read 猜想。

### 4.3 Matroid 的 Hodge 理论

**Rota 猜想（1971）**：对于任何可表示拟阵（representable matroid），其特征多项式的系数序列是对数凹的。

拟阵（matroid）是向量配置（或等价地，超平面配置）的组合抽象。Rota 猜想是 Read 猜想的极大推广。

**Huh-Katz 的工作（2012-2018）**：

1. **Huh-Katz（2012）**：对于在域 $\mathbb{F}$ 上可表示的拟阵 $M$，构造了**Chow 环 $A^*(M)$**——这是代数几何中代数簇的 Chow 环的组合类似物。

2. **Hodge-Riemann 关系的证明**：他们证明了 Chow 环 $A^*(M)$ 满足类似代数几何中 Kähler 流形的 **Hodge-Riemann 双线性关系**。具体地：
   - 存在"Kähler 类" $\ell \in A^1(M)$；
   - 对每个 $k$，Lefschetz 算子 $L^k: A^1(M) \to A^{k+1}(M)$（乘以 $\ell^k$）满足 Riemann-Hodge 关系；
   - 这给出了 $A^k(M)$ 上的正定双线性形式。

3. **对数凹性的推导**：Hodge-Riemann 关系蕴含特征多项式系数的对数凹性，从而证明了 Rota 猜想（对于可表示拟阵）。

### 4.4 更广泛的 Hodge 理论框架

**Huh-Botbol（2017）及后续**：将上述理论推广到更一般的**log-concavity 现象**：

- **Hodge 标准型猜想（Hodge standard conjecture）**在组合设置中的验证；
- **Dowling-Wilson 猜想**：几何格的 Möbius 数的绝对值序列是对数凹的；
- **Heron-Rota-Welsh 猜想**：拟阵的 $h$-向量（特征多项式系数）满足更精细的单峰性/对数凹性。

### 4.5 方法论意义

Huh 工作的深远意义在于：

1. **组合学中的 Hodge 理论**：建立了组合对象（拟阵、超平面配置）与代数几何（代数簇、Hodge 理论）之间的深刻桥梁。
2. **"无几何的 Hodge 理论"**：即使拟阵不可表示（没有对应的代数簇），Huh 等人（特别是 Adiprasito-Huh-Katz, 2018）仍然通过纯组合/代数方法建立了 Hodge-Riemann 关系，这是对"组合 Hodge 理论"的完整建立。
3. **统一了大量对数凹性猜想**：许多看似不相关的组合学猜想（Read, Rota, Heron-Rota-Welsh, Mason 等）都可以纳入这个框架。

---

## 参考文献

- Duminil-Copin, Raoufi, Tassion. *Exponential decay of connection probabilities for subcritical Voronoi percolation in $\mathbb{R}^d$*. 2019.
- Duminil-Copin, Sidoravicius, Tassion. *Continuity of the phase transition for planar random-cluster and Potts models with $1 \leq q \leq 4$*. 2015.
- Maynard. *Small gaps between primes*. Annals of Mathematics, 2015.
- Maynard. *Dense clusters of primes in subsets*. Compositio Mathematica, 2015.
- Koukoulopoulos, Maynard. *On the Duffin-Schaeffer conjecture*. Annals of Mathematics, 2020.
- Viazovska. *The sphere packing problem in dimension 8*. Annals of Mathematics, 2017.
- Cohn, Kumar, Miller, Radchenko, Viazovska. *The sphere packing problem in dimension 24*. Annals of Mathematics, 2017.
- Huh. *Milnor numbers of projective hypersurfaces and the chromatic polynomial of graphs*. JAMS, 2012.
- Huh, Katz. *Log-concavity of characteristic polynomials and the Bergman fan of matroids*. Mathematische Annalen, 2012.
- Adiprasito, Huh, Katz. *Hodge theory for combinatorial geometries*. Annals of Mathematics, 2018.
