# 千禧年大奖问题 (Millennium Prize Problems)

Clay 数学研究所 (Clay Mathematics Institute) 于2000年5月24日在巴黎法兰西学院发布了七个千禧年大奖问题，每个问题悬赏 **$1,000,000**。这些问题代表了20世纪末数学中最重要的未解决问题。截至2024年，仅 Poincaré 猜想被解决（由 Grigori Perelman 于2003年证明，他拒绝领取奖金）。

---

### 1. Riemann Hypothesis (黎曼假设)

**陈述**：Riemann zeta 函数 $\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$ 的所有非平凡零点 $\rho$ 满足 $\text{Re}(\rho) = \frac{1}{2}$。即 $\zeta(s) = 0$ 且 $0 < \text{Re}(s) < 1$ 蕴含 $\text{Re}(s) = \frac{1}{2}$。

等价地，若将非平凡零点写作 $\rho = \frac{1}{2} + i\gamma$，则所有 $\gamma$ 均为实数。

**为什么难**：

Riemann zeta 函数的零点分布与素数的分布深刻相关。Riemann (1859) 在其著名论文中建立了 $\zeta(s)$ 的零点与素数计数函数 $\pi(x)$ 之间的精确联系——通过显式公式 $\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} + \cdots$，零点的实部直接决定了素数定理的误差项。如果 Riemann 假设成立，则 $|\pi(x) - \text{li}(x)| = O(\sqrt{x} \log x)$，这是最优可能的误差阶。

困难在于：$\zeta(s)$ 是一个解析函数，其零点的精确位置由超越方程决定，没有已知的代数或结构方法可以约束所有零点的实部。已有的验证（到 $T \approx 10^{13}$）都是数值的，无法推广到无穷。此外，Riemann 假设与 L-函数的一般化（广义 Riemann 假设、Dedekind zeta 函数等）构成一个庞大的猜想体系，任何单一技巧似乎都不足以攻克。

**已知进展**：
- **Hardy (1914)**：证明 $\zeta(s)$ 在临界线 $\text{Re}(s) = 1/2$ 上有无穷多零点。
- **Selberg (1942)**：证明临界线上零点占正比例（至少 $cT\log T$ 个零点在临界线上，$c > 0$）。
- **Levinson (1974)**：证明至少 1/3 的零点在临界线上。
- **Conrey (1989)**：改进到至少 2/5 的零点在临界线上。
- **Bui-Conrey-Young (2011)**：改进到至少 41% 的零点在临界线上。
- **数值验证**：Gourdon (2004) 验证了前 $10^{13}$ 个零点均在临界线上。后续验证进一步扩展。
- **Deligne (1974)**：证明 Weil 猜想，等价于有限域上 zeta 函数的 Riemann 假设——这是 Riemann 假设在函数域类比中的成功，但方法无法迁移到数域情形。
- **关联结果**：Riemann 假设蕴含大量数论结果（如素数分布的最优误差、Goldbach 的弱化版本等），许多结果已被证明"在 RH 假设下成立"。

**当前状态**：开放。被广泛认为是纯数学中最重要的未解决问题。

**相关文献**：
- B. Riemann, "Über die Anzahl der Primzahlen unter einer gegebenen Größe", 1859
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, Oxford, 2nd ed. 1986
- H. M. Edwards, *Riemann's Zeta Function*, Academic Press, 1974
- A. Ivić, *The Riemann Zeta-Function*, Wiley, 1985
- J. B. Conrey, "The Riemann Hypothesis", *Notices AMS*, 2003

---

### 2. P vs NP

**陈述**：P = NP？即：如果一个问题可以在多项式时间内验证（属于 NP），是否一定可以在多项式时间内求解（属于 P）？

形式化：设 P 为确定性图灵机在多项式时间内可判定的语言类，NP 为非确定性图灵机在多项式时间内可判定的语言类（等价地，多项式时间可验证的语言类）。是否 P = NP？

**为什么难**：

P vs NP 问题处于计算复杂性理论的核心。直观上，"验证一个解"似乎应比"找到一个解"容易得多——这正是 P ≠ NP 的直觉。但证明这一点意味着必须展示：存在某个 NP 问题，使得**任何**确定性多项式时间算法都无法解决它。这要求对"所有可能的算法"给出下界，而现有的数学工具对算法能力的下界证明极其有限。

已知的下界技术（对角化、代数方法、通信复杂性等）都存在"相对化障碍"（Baker-Gill-Solovay 1975：存在 oracle A 使 $P^A = NP^A$，也存在 oracle B 使 $P^B \neq NP^B$，因此纯对角化方法无法解决 P vs NP）。后续的"自然证明障碍"（Razborov-Rudich 1997）表明，现有的电路下界证明技术也不足以分离 P 和 NP。arithmetical hierarchy 和 Boolean circuit complexity 之间的鸿沟至今无法跨越。

NP-完全问题的存在（Cook-Levin 定理，1971）使得 P vs NP 等价于"是否存在多项式时间算法解决 SAT（或任何其他 NP-完全问题）"。尽管数十年的努力，没有任何 NP-完全问题被证明需要超多项式时间，也没有任何被找到多项式时间算法。

**已知进展**：
- **Cook-Levin (1971)**：证明 SAT 是 NP-完全的，建立 NP-完全性理论。
- **Karp (1972)**：列出21个 NP-完全问题，确立 NP-完全性的普遍性。
- **Baker-Gill-Solovay (1975)**：相对化障碍——oracle 分离。
- **Razborov (1985)**：对单调电路证明指数下界（但单调电路弱于一般电路）。
- **Razborov-Rudich (1997)**：自然证明障碍——现有电路下界方法不足以分离 P 与 NP。
- **Aaronson-Wigderson (2008)**：algebrization 屏障——第三代障碍。
- **具体问题**：某些问题如线性规划（Khachiyan 1979, Karmarkar 1984）、素性判定（AKS 2002）被证明在 P 中，但这些不是 NP-完全的。
- **近似算法与硬度**：PCP 定理 (Arora et al. 1998) 给出近似硬度结果，但与精确 P vs NP 不同。

**当前状态**：开放。普遍相信 P ≠ NP，但无证明。

**相关文献**：
- S. A. Cook, "The complexity of theorem-proving procedures", STOC 1971
- L. A. Levin, "Universal search problems", 1973
- R. M. Karp, "Reducibility among combinatorial problems", 1972
- S. Arora & B. Barak, *Computational Complexity: A Modern Approach*, Cambridge, 2009
- C. H. Papadimitriou, *Computational Complexity*, Addison-Wesley, 1994
- A. Razborov & S. Rudich, "Natural proofs", *J. Comput. System Sci.* 55 (1997)

---

### 3. Navier-Stokes 方程的存在性与光滑性

**陈述**：在 $\mathbb{R}^3$ 中，Navier-Stokes 方程
$$\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u} = -\nabla p + \nu \Delta \mathbf{u} + \mathbf{f}, \quad \nabla \cdot \mathbf{u} = 0$$
对于充分光滑的初始条件 $\mathbf{u}_0(\mathbf{x})$ 和外力 $\mathbf{f}(\mathbf{x},t)$，是否存在全局（对所有 $t > 0$）光滑解？

Clay 问题的精确陈述要求在 $\mathbb{R}^3$ 或 $\mathbb{T}^3$ 上证明（或否定）：给定光滑初始数据，存在唯一全局光滑解。

**为什么难**：

Navier-Stokes 方程描述粘性不可压缩流体的运动，是非线性偏微分方程中最重要的一类。非线性项 $(\mathbf{u} \cdot \nabla)\mathbf{u}$ 使得方程高度非线性，它可以在有限时间内将能量从大尺度转移到小尺度（湍流级联），可能导致解的奇性形成。

关键困难在于：我们不知道三维 Navier-Stokes 方程的解是否会在有限时间内出现奇性（速度或其导数变为无穷）。如果奇性形成，则光滑解在有限时间后不存在。二维情形已被完全解决（Ladyzhenskaya 1969：二维全局光滑解存在），但三维的非线性涡旋拉伸效应使得二维方法失效。

能量估计只能给出"弱解"的全局存在性（Leray 1934, Hopf 1951），但弱解的唯一性和正则性至今未解决。Serré 的部分正则性理论（1970s-80s）表明奇性集的 Hausdorff 维数很小，但不能排除奇性的存在。

**已知进展**：
- **Leray (1934)**：证明全局弱解（Leray-Hopf 解）的存在性。
- **Hopf (1951)**：在区域上证明弱解存在性。
- **Ladyzhenskaya (1969)**：二维全局光滑解。
- **Kato (1984)**：$H^s$ 空间中的局部适定性理论。
- **Scheffer (1976-1988)**：部分正则性，奇性集的维数上界。
- **Caffarelli-Kohn-Nirenberg (1982)**：CKN 部分正则性定理——奇性集的1维 Hausdorff 测度为零。这是最接近完整正则性的结果。
- **Lin (1998)**：CKN 定理的新证明和改进。
- **Tao (2019)**：对平均化的 Navier-Stokes 方程证明有限时间爆破解的存在性，暗示原始方程也可能有爆破解。
- **Escauriaza-Seregin-Šverák (2003)**：反向唯一性及其对正则性的推论。

**当前状态**：开放。是否全局光滑解存在（或是否存在有限时间爆破解）完全未知。

**相关文献**：
- J. Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace", *Acta Math.* 63 (1934)
- L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity for suitable weak solutions of the Navier-Stokes equations", *Comm. Pure Appl. Math.* 35 (1982)
- P. Constantin & C. Foias, *Navier-Stokes Equations*, U. Chicago Press, 1988
- T. Tao, "Finite time blowup of an averaged three-dimensional Navier-Stokes equation", 2019
- Clay Mathematics Institute, *Official Problem Description* (C. Fefferman)

---

### 4. Yang-Mills 存在性与质量间隙

**陈述**：证明四维时空中 Yang-Mills 理论存在一个量子场论，满足以下两条性质：
1. **存在性**：存在一个严格的数学构造（如 Wightman 公理或 Osterwalder-Schrader 公理的框架）定义非阿贝尔 Yang-Mills 场论。
2. **质量间隙**：该理论存在质量间隙 $\Delta > 0$，即谱中最低的激发态质量严格大于零（真空态与最低激发态之间存在正的能量差）。

精确陈述要求对紧致规范群 $G$（如 $SU(3)$），在四维 Minkowski 时空中构造 Yang-Mills 理论并证明质量间隙。

**为什么难**：

Yang-Mills 理论是粒子物理标准模型的基础（描述强相互作用的 QCD 基于 $SU(3)$ Yang-Mills 理论）。物理上，质量间隙对应于胶子不能自由传播（色禁闭）——这在格点规范理论的数值计算中被观测到，但缺乏严格的数学证明。

数学困难是多层次的：首先，构造性量子场论本身在四维时空中极其困难——即使是最简单的四维相互作用场论（如 $\phi^4_4$）也未被严格构造。其次，Yang-Mills 理论是非阿贝尔规范理论，其非线性结构（自相互作用规范玻色子）使得标准的微扰方法不适用于非微扰效应（如质量间隙）。第三，质量间隙是一个本质上非微扰的量——微扰论在低能区失效（红外奴役），而质量间隙恰好是低能性质。

二维和三维 Yang-Mills 理论已被严格构造（但三维的质量间隙证明也较近期），但四维的构造需要全新的数学工具。可能的途径包括：构造性场论方法、随机微分方程、或从 Seiberg-Witten 理论等对偶性中获取灵感。

**已知进展**：
- **Yang-Mills (1954)**：提出规范理论框架。
- **Wilson (1974)**：格点规范理论，数值上观测到质量间隙和色禁闭。
- **Osterwalder-Schrader (1973-1975)**：构造性场论的公理框架。
- **Balaban (1980s)**：格点 Yang-Mills 的重整化群分析，在连续极限方向有进展。
- **Magnen-Rivasseau-Sénéor (1990s)**：三维 Yang-Mills 的构造性结果。
- **Seiberg-Witten (1994)**：对偶性和拓扑不变量，为理解非微扰效应提供新工具。
- **Loll (1998)**：二维 Yang-Mills 的严格构造。
- **Chatterjee (2015)**：概率方法对 Yang-Mills 的部分结果。
- **Driver-Gabriel-Lohr (2017+)**：Yang-Mills 测度的概率构造进展。

**当前状态**：开放。距离解决尚远，可能需要全新的数学框架。

**相关文献**：
- C. N. Yang & R. L. Mills, "Conservation of isotopic spin and isotopic gauge invariance", *Phys. Rev.* 96 (1954)
- K. Osterwalder & R. Schrader, "Axioms for Euclidean Green's functions", *Comm. Math. Phys.* 31 (1973)
- A. Jaffe & E. Witten, "Quantum Yang-Mills theory", *Clay Mathematics Institute Millennium Problem Description*
- M. Creutz, *Quarks, Gluons and Lattices*, Cambridge, 1983
- E. Witten, "Some results on the mass gap", 1998

---

### 5. Birch and Swinnerton-Dyer 猜想

**陈述**：设 $E$ 是有理数域 $\mathbb{Q}$ 上的椭圆曲线。BSD 猜想将 $E$ 的 Mordell-Weil 群 $E(\mathbb{Q})$ 的秩 $\text{rank}(E(\mathbb{Q}))$ 与其 $L$-函数 $L(E, s)$ 在 $s = 1$ 处的解析行为联系起来。

具体地，BSD 猜想断言：
$$\text{ord}_{s=1} L(E, s) = \text{rank}(E(\mathbb{Q}))$$

即 $L(E, s)$ 在 $s = 1$ 处的零点阶数等于 $E(\mathbb{Q})$ 的秩。

更强的版本（BSD 精确公式）给出 $L(E, s)$ 在 $s = 1$ 处的 Taylor 展开首项系数的精确公式，涉及 $E$ 的 Tamagawa 数、Tate-Shafarevich 群等。

**为什么难**：

BSD 猜想连接了椭圆曲线的两个看似无关的方面：算术方面（Mordell-Weil 群的结构，即有理点的数量）和分析方面（$L$-函数的解析性质）。这种"算术-分析"对应是现代数论的核心主题之一（与 Langlands 纲领一脉相承），但具体的精确对应极难证明。

困难在于：$L(E, s)$ 在 $s = 1$ 处的行为由解析延拓决定，而 $L(E, s)$ 原始定义仅在 $\text{Re}(s) > 3/2$ 收敛。解析延拓到 $s = 1$ 的存在性本身依赖深奥的结果（Wiles-Taylor-Breuil-Conrad-Diamond 2001：模性定理，证明所有 $\mathbb{Q}$ 上椭圆曲线是模的）。在此基础上，BSD 猜想进一步要求零点阶数与算术秩精确匹配——这需要一种尚未发现的"算术-分析"桥梁。

Tate-Shafarevich 群 $\text{Sha}(E)$ 的有限性也是 BSD 公式的一部分，但 $\text{Sha}(E)$ 的有限性本身就是一个独立的著名未解决问题。

**已知进展**：
- **Coates-Wiles (1977)**：对有复乘的椭圆曲线，若 $L(E,1) \neq 0$ 则 $\text{rank}(E(\mathbb{Q})) = 0$（BSD 猜想的一个方向，秩0情形）。
- **Gross-Zagier (1986)**：Heegner 点公式，将 $L'(E,1)$ 与 Heegner 点的高度联系起来，处理秩1情形。
- **Kolyvagin (1989-1990)**：Euler 系方法，证明若 $\text{ord}_{s=1} L(E,s) \leq 1$ 则 BSD 猜想成立（即解析秩 $\leq 1$ 蕴含算术秩等于解析秩，且 $\text{Sha}$ 有限）。
- **Wiles et al. (1995-2001)**：模性定理——所有 $\mathbb{Q}$ 上椭圆曲线是模的，保证 $L(E,s)$ 可以整体解析延拓。
- **Skinner-Urban (2014)**：对某些情形证明 $L(E,1) \neq 0 \Rightarrow \text{rank} = 0$ 的推广。
- **Zhang (2001-2004)**：Gross-Zagier 公式的推广。
- **Bertolini-Darmon (2005+)**：Iwasawa 理论方法对 BSD 的部分进展。
- **当前**：BSD 猜想对解析秩 $\leq 1$ 的情形已基本证明（Kolyvagin + Gross-Zagier + 模性定理），但对解析秩 $\geq 2$ 的情形几乎完全开放。

**当前状态**：开放。秩 $\leq 1$ 情形已证明，一般情形（特别是高秩）完全开放。

**相关文献**：
- B. J. Birch & H. P. F. Swinnerton-Dyer, "Notes on elliptic curves II", *J. reine angew. Math.* 218 (1965)
- J. Coates & A. Wiles, "On the conjecture of Birch and Swinnerton-Dyer", *Invent. Math.* 39 (1977)
- B. Gross & D. Zagier, "Heegner points and derivatives of L-series", *Invent. Math.* 84 (1986)
- V. Kolyvagin, "Finiteness of E(Q) and Sha(E,Q) for a subclass of Weil curves", *Izv. Akad. Nauk SSSR* 52 (1988)
- A. Wiles, "Modular elliptic curves and Fermat's Last Theorem", *Ann. Math.* 141 (1995)

---

### 6. Hodge 猜想

**陈述**：设 $X$ 是复射影流形（即非奇异的复射影代数簇）。设 $H^{p,q}(X)$ 是 $X$ 的 Hodge 分解中 $(p,q)$ 型的 Hodge 类。设 $H^{2k}(X, \mathbb{Q}) \cap H^{k,k}(X)$ 是有理 Hodge 类（即 $(k,k)$ 型且为有系数 $\mathbb{Q}$ 的上同调类）。

Hodge 猜想断言：$H^{2k}(X, \mathbb{Q}) \cap H^{k,k}(X)$ 中的每一个类都是 $\mathbb{Q}$ 上代数闭链类的 $\mathbb{Q}$-线性组合。即每个有理 Hodge 类都是代数闭链（余维数 $k$ 的代数子簇）的上同调类的有理线性组合。

形式化：$\text{Hdg}^k(X) \otimes \mathbb{Q} = \text{cl}(\text{Z}^k(X)) \otimes \mathbb{Q}$，其中 $\text{Hdg}^k(X)$ 是 Hodge 类群，$\text{Z}^k(X)$ 是余维数 $k$ 的代数闭链群。

**为什么难**：

Hodge 猜想是代数几何与复几何之间最深刻的桥梁之一。它断言：上同调中的"拓扑-解析"信息（Hodge 类）完全来自"代数-几何"信息（代数闭链）。换言之，Hodge 结构中由调和形式定义的类，是否都可以由代数子簇给出？

困难在于：Hodge 类是由 Hodge 分解（依赖复结构）定义的，而代数闭链是由代数子簇定义的——两者来自完全不同的数学结构。在低维情形（如 $k=1$，即除子情形），Lefschetz $(1,1)$-定理（1924）给出了肯定回答。但对 $k \geq 2$，一般情形完全开放。

Hodge 猜想的困难还在于：它涉及"有理"系数——从 $\mathbb{Z}$ 到 $\mathbb{Q}$ 的推广是非平凡的。Atiyah-Hirzebruch 给出了反例表明整数版本的 Hodge 猜想不成立（存在 Hodge 类不是整系数代数闭链的整数线性组合）。因此猜想的精确表述（有理线性组合）至关重要。

此外，Grothendieck 曾提出"代数 Hodge 猜想"（对代数等价闭链），这与原始 Hodge 猜想不同，且部分情形有反例（Clemens, Voisin 等），使得问题更加微妙。

**已知进展**：
- **Lefschetz (1924)**：$(1,1)$-定理——$k=1$ 情形成立（Hodge 猜想对除子类成立）。
- **Hodge (1950)**：提出一般猜想。
- **Grothendieck (1969)**：标准猜想与 Hodge 猜想的关系；提出代数 Hodge 猜想。
- **Zucker (1977)**：某些曲面情形的验证。
- **Voisin (2002-2010)**：构造反例否定某些强化的 Hodge 猜想变体（如代数 Hodge 猜想对某些 Calabi-Yau 不成立）。
- **Clemens (1983)**：某些曲面上的反例（对变体形式）。
- **Totaro (2016)**：对某些情形的否定结果和精确分析。
- **当前**：$k=1$ 完全解决（Lefschetz）。对 $k \geq 2$，仅有零散的正面和反面结果，一般情形完全开放。Abel 簇上的 Hodge 猜想也有部分进展（Mattuck, Tankeev 等）。

**当前状态**：开放。$k=1$ 已解决，一般情形开放。

**相关文献**：
- W. V. D. Hodge, "The topological invariants of a Kähler manifold", 1950
- S. Lefschetz, *L'analysis situs et la géométrie algébrique*, Gauthier-Villars, 1924
- A. Grothendieck, "Standard conjectures on algebraic cycles", *Algebraic Geometry*, Bombay Colloq., 1968
- C. Voisin, *Hodge Theory and Complex Algebraic Geometry*, I & II, Cambridge, 2002/2003
- P. Deligne, "Théorie de Hodge II", *Publ. Math. IHÉS* 40 (1971)

---

### 7. Poincaré 猜想 (已解决)

**陈述**：每个单连通的紧致三维流形同胚于三维球面 $S^3$。

等价地：每个单连通的紧致三维流形（无边）是三维球面。

更一般地，$n$ 维 Poincaré 猜想断言每个同伦等价于 $S^n$ 的紧致 $n$-流形同胚于 $S^n$。$n \geq 5$ 由 Smale (1961) 证明，$n=4$ 由 Freedman (1982) 证明，$n=3$ 由 Perelman (2003) 证明。

**为什么难**（历史背景）：

三维流形的拓扑极其丰富和复杂。Poincaré 在1904年提出此问题（他最初在1900年提出了一个错误版本，用同调代替同伦，但自己找到了反例——Poincaré 同调球面）。三维的特殊困难在于：三维流形既没有高维流形的"足够空间"来执行 Whitney 技巧（$n \geq 5$），也没有四维的 Freedman 重嵌入技术的特殊结构。

Hamilton (1982) 提出了 Ricci 流方法来"光滑化"流形的度量，并提出了通过 Ricci 流将三维流形"流向"常曲率度量的纲领。但 Ricci 流可能在有限时间出现奇性（颈部收缩），Hamilton 处理了某些情形但无法完成一般情形。

**已知进展**：
- **Smale (1961)**：证明 $n \geq 5$ 的 Poincaré 猜想（高维广义 Poincaré 猜想）。Fields Medal 1966。
- **Freedman (1982)**：证明 $n=4$ 的 Poincaré 猜想。Fields Medal 1986。
- **Hamilton (1982)**：引入 Ricci 流，证明 Ricci 流在某些条件下收敛到常曲率度量。
- **Hamilton (1995)**：处理 Ricci 流的奇性（颈部收缩），但无法处理最一般的情形。
- **Perelman (2002-2003)**：在 arXiv 上发表三篇预印本：
  1. "The entropy formula for the Ricci flow and its geometric applications" (2002年11月)
  2. "Ricci flow with surgery on three-manifolds" (2003年3月)
  3. "Finite extinction time for the solutions to the Ricci flow on certain three-manifolds" (2003年7月)
  
  Perelman 引入了新的关键技术：**$W$-熵泛函**（单调性公式）、**no local collapsing 定理**（排除 Ricci 流的某些退化行为）、**Ricci 流带手术**（surgery，处理奇性后继续流动）。这些技术使得 Hamilton 的纲领得以完成。
- **验证 (2003-2006)**：Kleiner-Lott, Cao-Zhu, Morgan-Tian 等给出了 Perelman 证明的详细验证和完整写出。Morgan-Tian 的书 (2007) 和 Cao-Zhu 的书提供了完整 exposition。
- **Perelman 拒绝 Fields Medal (2006)** 和拒绝 Clay 奖金 (2010)**：Perelman 认为Hamilton 的贡献与他同等重要，且对数学界伦理有异议。

**当前状态**：**已解决**。由 Grigori Perelman 于2002-2003年证明，2006年经数学界充分验证确认。

**相关文献**：
- H. Poincaré, "Cinquième complément à l'analysis situs", *Rend. Circ. Mat. Palermo* 18 (1904)
- R. Hamilton, "Three-manifolds with positive Ricci curvature", *J. Diff. Geom.* 17 (1982)
- G. Perelman, "The entropy formula for the Ricci flow and its geometric applications", arXiv:math/0211159 (2002)
- G. Perelman, "Ricci flow with surgery on three-manifolds", arXiv:math/0303109 (2003)
- J. Morgan & G. Tian, *Ricci Flow and the Poincaré Conjecture*, AMS Clay Math. Monographs, 2007
- B. Kleiner & J. Lott, "Notes on Perelman's papers", *Geom. Topol.* 12 (2008)

---

## 总结表

| 问题 | 领域 | 状态 | 解决者 | 年份 |
|---|---|---|---|---|
| Riemann Hypothesis | 数论 / 分析 | 开放 | — | — |
| P vs NP | 计算复杂性 | 开放 | — | — |
| Navier-Stokes | PDE / 流体力学 | 开放 | — | — |
| Yang-Mills + 质量间隙 | 数学物理 / QFT | 开放 | — | — |
| Birch-Swinnerton-Dyer | 算术几何 | 开放（秩≤1已证） | — | — |
| Hodge Conjecture | 代数几何 | 开放（k=1已证） | — | — |
| Poincaré Conjecture | 拓扑 | **已解决** | Perelman | 2003 |

---

## 备注

1. **奖金**：每个问题 $1,000,000。Poincaré 猜想的奖金因 Perelman 拒绝领取而未被领取，Clay 研究所将奖金用于支持数学研究。

2. **Fields Medal 关联**：Poincaré 猜想的解决使 Perelman 获 Fields Medal 提名（2006，他拒绝）。Deligne (1978) 因证明 Weil 猜想（函数域 RH）获 Fields Medal，与 Riemann 假设相关。

3. **难度评估**：数学界普遍认为 Riemann 假设和 P vs NP 是目前纯数学和理论计算机科学中最重要且最困难的未解决问题。Yang-Mills 质量间隙可能需要全新的数学物理框架。

4. **更新时间**：本文档内容截至2024年。BSD 和 Hodge 猜想的部分进展可能已有更新。
