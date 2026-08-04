# 其他近期重要数学突破（2020–2025）

> 本文档记录2020年以来数学领域的其他重要突破，包括数论、代数、几何、拓扑、数学物理以及形式化验证等方面的进展。

---

## 1. Maynard 关于 Dirichlet 素数定理的改进

### 背景

**Dirichlet 素数定理（1837）**：对于互素的正整数 $a, d$（$\gcd(a,d)=1$），算术级数 $\{a, a+d, a+2d, \ldots\}$ 中包含无穷多个素数。

更精确地，令 $\pi(x; d, a)$ 表示不超过 $x$ 且满足 $p \equiv a \pmod{d}$ 的素数个数，则
$$\pi(x; d, a) \sim \frac{1}{\varphi(d)} \cdot \frac{x}{\log x} \quad (x \to \infty, \, d \text{ 固定}).$$

**关键问题**：当 $d$ 与 $x$ 同时增长时，这个渐近式在什么范围成立？

- **Siegel-Walfisz 定理**：对 $d \leq (\log x)^A$（任意固定 $A$），渐近式成立。
- **Bombieri-Vinogradov 定理**：对"几乎所有" $d \leq x^{1/2}$，渐近式平均意义下成立。
- ** Elliott-Halberstam 猜想**：将范围推广到 $d \leq x^{1-\epsilon}$（对所有 $\epsilon > 0$）。

### Maynard 的贡献

Maynard 在**小素数在算术级数中**的问题上取得重要进展：

1. **算术级数中的小素数**：Maynard 证明了对于充分大的 $q$，存在素数 $p \equiv a \pmod{q}$ 满足
   $$p \ll q^{5.2}.$$
   这改进了之前 $q^{5.5}$ 量级的结果（Xylouris 的 $q^{5.2}$ 是 Linnik 常数的最佳无条件结果，Maynard 在不同框架下给出了新证明和改进）。

2. **几乎素数在算术级数中**：Maynard 证明了存在无穷多个 $n \equiv a \pmod{q}$ 使得 $n$ 至多有 2 个素因子（$P_2$ 数），这是陈景润型定理在算术级数中的推广。

3. **方法创新**：Maynard 将其 Maynard-Tao 多元筛法与算术级数中的分布结果结合，绕过了传统方法对 Bombieri-Vinogradov 水平的依赖。

---

## 2. Scholze-Clausen 凝聚数学（Condensed Mathematics）

### 背景

**问题**：拓扑代数结构（如拓扑向量空间、拓扑群、拓扑环）的范畴论基础存在根本困难。传统的拓扑空间范畴有良好的性质（如 Cartesian 闭性），但拓扑 Abel 群的范畴不是 Abel 范畴，这给同调代数带来了困难。

### 凝聚数学框架

**Scholze 与 Clausen（2019-2022）** 提出了**凝聚数学（Condensed Mathematics）**，用一种新的"凝聚"框架取代传统拓扑：

1. **凝聚集（Condensed Sets）**：
   - 定义：凝聚集是从**超 Stonean 紧 Hausdorff 空间**（extremally disconnected compact Hausdorff spaces）的范畴到集合的函子，满足有限极限保持性质。
   - 等价地，凝聚集是满足 sheaf 条件的预层 $F: \text{ExtrDisc}^{\text{op}} \to \text{Set}$。
   - 凝聚集范畴是**Grothendieck topos**，具有良好的范畴论性质（Abel 范畴、足够投射等）。

2. **凝聚 Abel 群**：凝聚 Abel 群范畴 $\text{Cond}(\text{Ab})$ 是一个**Grothendieck 范畴**（Abel 范畴，满足 AB5 和生成元存在），可以开展同调代数。

3. **液态向量空间（Liquid Vector Spaces）**：
   - 凝聚 Abel 群范畴虽然良好，但"太大"——包含了许多不自然的对象。
   - Scholze 引入了**液态向量空间（liquid $\mathbb{R}$-vector spaces）**的子范畴，这是"正确大小"的范畴，既保留了拓扑信息，又允许同调代数操作。
   - 关键定理：液态向量空间范畴是 Abel 范畴，且实数 $\mathbb{R}$（带通常拓扑）在其中是内射对象。

4. **应用**：
   - 将**泛函分析**重新基础化：Banach 空间、Fréchet 空间、LF 空间等都可以自然地嵌入凝聚框架；
   - **$p$-adic 几何**：凝聚数学为完美空间和棱柱上同调提供了更好的代数基础；
   - **复几何**：凝聚数学有望简化复几何中的某些构造。

### 核心定理

Scholze 证明了以下关键定理（后来由 Liquid Tensor Experiment 形式化验证）：

**定理（Scholze）**：设 $S$ 是局部凸向量空间，$M$ 是液态 $\mathbb{R}$-向量空间，则
$$\text{Ext}^i_{\text{Liq}}(S, M) = 0 \quad \text{对 } i > 0$$
在特定条件下成立。特别地，$\mathbb{R}$ 在液态向量空间范畴中是内射的。

---

## 3. Liquid Tensor Experiment（液态张量实验）

### 背景

2020年12月，Peter Scholze 在博客上发布了一个**公开挑战**：他邀请数学社区用**形式化验证系统**来验证凝聚数学中的一个核心定理——即液态向量空间范畴中 $\mathbb{R}$ 的内射性（或等价地，某个 Ext 群的消没）。

Scholze 写道：

> "I think this may be my most important theorem. [...] I was never satisfied with the proofs. [...] I'd be very happy to see this proof formalized."

### 形式化验证

**Liquid Tensor Experiment** 是一个协作项目，使用 **Lean 4** 定理证明器（以及 mathlib 库）来形式化验证 Scholze 的定理。

**关键参与者**：
- **Johan Commelin**（阿姆斯特丹自由大学）：主要驱动者；
- **Adam Topaz**（阿尔伯塔大学）；
- **Patrick Massot**（巴黎萨克雷大学）；
- 以及整个 Lean mathlib 社区的贡献。

**时间线**：
- 2020年12月：Scholze 发布挑战；
- 2021年3月：核心定理被形式化验证完成；
- 2021年6月：Scholze 在博客上宣布"实验成功"；
- 2022年：完整论文发表（Commelin, Topaz 等）。

### 意义

1. **复杂现代数学的形式化**：这是首次将**前沿研究数学**（而非教科书数学）成功形式化验证的案例之一。凝聚数学涉及深层的范畴论、代数和拓扑，其形式化验证证明了现代证明助手的强大能力。

2. **证明的可信度**：Scholze 本人对该定理的证明"从未完全满意"——证明涉及大量技术性估计，人工验证容易出错。形式化验证提供了**机器检查的绝对确定性**。

3. **Lean 4 / mathlib 的里程碑**：此项目极大地推动了 Lean 4 和 mathlib 的发展，特别是凝聚数学相关的基础设施（拓扑、范畴论、同调代数）。

4. **数学实践的变化**：Scholze 的挑战开创了"重要定理公开形式化"的先例，影响了后续多个形式化项目（如 Tao 的多项式 Freiman-Ruzsa 猜想的形式化）。

### 技术细节

形式化的核心定理（简化版）：

**定理**：对于 $p$ 进数 $\mathbb{Z}_p$ 上的凝聚数学框架，有
$$\text{Ext}^1_{\text{Cond}(\text{Ab})}(\mathbb{Z}_p, \mathbb{R}) = 0,$$
其中 $\mathbb{R}$ 带有离散拓扑（或等价地，液态实向量空间的内射性）。

形式化验证确认了 Scholze 证明中**最困难的技术部分**——涉及 9-Banach 空间和某些归纳论证的正确性。

---

## 4. 2023–2025 年的其他重要进展

### 4.1 多项式 Freiman-Ruzsa 猜想（2023）

**猜想**：若 $A \subseteq \mathbb{F}_2^n$ 满足 $|A+A| \leq K|A|$（小倍加增长），则 $A$ 被包含在一个大小 $\leq f(K)|A|$ 的子群陪集中，其中 $f(K)$ 是 $K$ 的多项式。

**进展**：2023年，**Tao, Gowers, Green, Manners** 等人宣布证明了多项式 Freiman-Ruzsa 猜想（在 $\mathbb{F}_2^n$ 上）。随后该证明被 Lean 形式化验证。

### 4.2 几何 Langlands 对应的证明（2024-2025）

**背景**：几何 Langlands 纲领是 Langlands 纲领的几何化版本，由 Beilinson-Drinfeld 提出。它预测：对于代数曲线 $X$ 上的 reductive 群 $G$，存在 $G$-主丛的导出范畴与 Langlands 对偶群 ${}^L G$ 的局部系统的导出范畴之间的等价。

**进展**：2024年，**Dennis Gaitsgory** 及合作者（Arinkin, Frenkel, Kazhdan, Rozenblyum, Varshavsky 等）发布了完整证明的系列论文。这是21世纪数学最重大的成就之一。

### 4.3 Kakeya 猜想的进展

**猜想**：在 $\mathbb{R}^n$ 中，包含每个方向单位线段的集合（Kakeya 集）的 Hausdorff 维数为 $n$。

**进展**：
- **2024年**：**Guth, Wang, Zhang** 在三维 Kakeya 猜想上取得重大进展，证明了三维 Kakeya 集的 Hausdorff 维数严格大于 $5/2 + \epsilon$（改进了之前的 $5/2$ 下界）。
- 这是继 Wolff, Katz, Tao 等人工作后的重大推进。

### 4.4 Cap Set 问题的后续

**背景**：2016年，Croot-Lev-Pach 和 Ellenberg-Gijswijt 用多项式方法证明了 cap set 问题——$\mathbb{F}_3^n$ 中不含算术级数的最大子集大小为 $O(2.756^n)$。

**近期进展**：多项式方法被推广到各种组合问题，包括：
- **sunflower 猜想**的突破（Alweiss, Lovett, Wu, Zhang, 2019-2020）；
- **矩阵乘法指数**的改进。

### 4.5 3x+1 猜想（Collatz 猜想）的部分结果

**进展**：**Terence Tao（2019）** 证明了"几乎所有"自然数在 Collatz 迭代下最终达到 1——更精确地，证明了对于充分大的 $N$，Collatz 迭代将 $N$ 减小到 $N^{0.5-\epsilon}$ 以下。这是对 Collatz 猜想的重大推进，虽然完整猜想仍远未解决。

### 4.6 量子唯一遍历（QUE）的进展

**进展**：在负曲率曲面上，Laplace 算子特征函数的 $L^2$ 质量等分布问题（量子唯一遍历猜想）取得新进展，特别是 **Dyatlov-Jin** 在某些双曲曲面上的突破。

### 4.7 棱柱上同调（Prismatic Cohomology）的发展

**Bhatt-Scholze（2019-2022）** 的棱柱上同调理论持续发展：
- 统一了 crystalline、de Rham、Hodge-Tate 等 $p$-adic 上同调理论；
- **2023-2024年**：在棱柱上同调框架下证明了多个新结果，包括 $p$-adic Hodge 理论中的计算性突破。

### 4.8 ABC 猜想的状态

**注**：Mochizuki（望月）的 inter-universal Teichmüller 理论声称证明了 ABC 猜想，但该证明**未被数学界广泛接受**。2021年，Mochizuki 的论文在 PRIMS 发表，但 Scholze 和 Stix 在2018年指出了他们认为的漏洞，至今争议未解决。ABC 猜想仍应视为**未解决**。

### 4.9 Lean / mathlib 生态系统的爆发

2020-2025年间，Lean 4 和 mathlib 经历了爆发式增长：
- **多项式 Freiman-Ruzsa 猜想**的形式化（Tao 等，2023）；
- **Liquid Tensor Experiment**（2021）；
- 大量本科和研究生数学被形式化（代数几何、微分几何、数论等）；
- **AI 辅助形式化**：2024年，Google DeepMind 的 AlphaProof 系统在 IMO 中达到银牌水平，展示了 AI 辅助形式化证明的潜力。

---

## 参考文献

- Maynard. *Primes in arithmetic progressions to large moduli I: Fixed residue classes*. 2020.
- Clausen, Scholze. *Condensed Mathematics*. Lecture notes, 2019-2022.
- Scholze. *Liquid tensor experiment*. Blog post, December 2020.
- Commelin, Topaz et al. *The liquid tensor experiment*. 2021.
- Gaitsgory et al. *Proof of the geometric Langlands conjecture*. Series of preprints, 2024.
- Guth, Wang, Zhang. *On the Kakeya conjecture in three dimensions*. 2024.
- Tao. *Almost all Collatz orbits attain almost bounded values*. 2019.
- Bhatt, Scholze. *Prisms and prismatic cohomology*. Annals of Mathematics, 2022.
