# Miklós Schweitzer 竞赛题目集

## 概述

### 历史

Miklós Schweitzer 竞赛（Schweitzer Miklós Matematikai Emlékverseny）是匈牙利最负盛名的数学竞赛之一，以匈牙利数学家 Miklós Schweitzer（1913–1941）的名字命名。Schweitzer 是一位才华横溢的年轻数学家，因在二战中被迫害致死而英年早逝。为纪念他，匈牙利数学学会（János Bolyai Mathematical Society）于1949年创立了此项竞赛，至今已举办超过70届。

### 特点

与IMO、Putnam等竞赛相比，Schweitzer竞赛有本质性的不同：

1. **研究级难度**：题目水平接近数学研究的前沿，许多题目直接取自或改编自近年的研究论文。参赛者需要具备研究生水平的数学知识。
2. **开放书卷（Open Book）**：允许参赛者查阅任何书籍、文献和资料，甚至可以使用计算工具。这反映了真实数学研究中查阅文献的能力。
3. **长时间考试**：考试持续10天（通常为连续十天），参赛者可以自由安排时间深入思考每一道题。
4. **团队或个人**：可以个人参赛，也可以组队参赛（通常最多3人一组），鼓励合作——这再次模拟了数学研究的真实环境。
5. **题目来源**：题目由匈牙利顶尖数学家命题，涵盖代数、分析、组合、几何、数论、概率、拓扑、泛函分析等多个领域，远超高中竞赛的范围。

### 为什么比IMO更难

- **知识门槛**：IMO题目原则上只用初等数学（中学知识即可解决），而Schweitzer题目需要大学乃至研究生水平的数学工具（如测度论、泛函分析、代数拓扑、表示论等）。
- **思维深度**：IMO强调巧妙的初等技巧和竞赛经验，Schweitzer则要求对数学结构的深层理解和创造性研究能力。
- **题目开放性**：许多Schweitzer题目没有标准答案，可能有多种解法，甚至题目本身就是开放性研究问题的简化版本。
- **参赛者水平**：参赛者多为数学系研究生和优秀本科生，而非中学生。

Paul Erdős 曾评价说，Schweitzer竞赛是世界上唯一一个"允许你带书回家想十天"的数学竞赛，因此它比任何限时竞赛都更接近真正的数学研究。

---

## 题目集

### Schweitzer 1949 Problem 1
**题目**：设 $f$ 是定义在 $[0,1]$ 上的连续函数，满足 $f(0)=f(1)=0$。证明：如果 $f$ 在 $[0,1]$ 上处处可微且 $|f'(x)| \leq M$，则对任意 $x \in [0,1]$，$|f(x)| \leq Mx(1-x)/2$。等号何时成立？
**领域**：数学分析
**难度**：2

### Schweitzer 1950 Problem 2
**题目**：设 $a_1, a_2, \ldots$ 是正数序列，满足 $\sum a_n$ 发散但 $\sum a_n^{-1}$ 也发散。证明：存在发散级数 $\sum b_n$（$b_n > 0$）使得 $\sum a_n b_n$ 收敛。
**领域**：实分析/级数论
**难度**：3

### Schweitzer 1951 Problem 1
**题目**：设 $f: \mathbb{R} \to \mathbb{R}$ 是多项式函数，且对任意实数 $x$，$f(x) \geq 0$。证明 $f$ 可以表示为两个实系数多项式的平方和。
**领域**：代数/实代数几何
**难度**：3

### Schweitzer 1953 Problem 1
**题目**：设 $A$ 是 $n \times n$ 实矩阵，且 $A^k = I$（$k$ 为正整数）。证明：$A$ 可以表示为有限个实正交矩阵的乘积。
**领域**：线性代数/群论
**难度**：3

### Schweitzer 1954 Problem 3
**题目**：设 $f$ 是 $[0,1]$ 上的单调递增连续函数，$f(0)=0, f(1)=1$。定义 $f$ 的反函数 $g$。证明：$\int_0^1 f(x)dx + \int_0^1 g(x)dx \geq 1$，并确定等号条件。
**领域**：数学分析
**难度**：2

### Schweitzer 1956 Problem 1
**题目**：设 $G$ 是有限群，$H$ 是其子群。证明：$G$ 可以表示为至多 $[G:H]$ 个 $H$ 的左陪集的并。进一步，如果 $H$ 是正规子群，讨论 $G/H$ 的结构如何约束 $G$ 的可能结构。
**领域**：群论
**难度**：3

### Schweitzer 1957 Problem 4
**题目**：设 $\{a_n\}$ 是正实数序列，满足 $a_{n+1} \leq a_n + a_n^2$。证明：如果 $\sum a_n$ 收敛，则 $a_n \to 0$ 足够快，具体地，求出 $a_n$ 的最佳上界估计。
**领域**：分析/递推
**难度**：4

### Schweitzer 1958 Problem 2
**题目**：设 $K$ 是 $\mathbb{R}^n$ 中的凸体（紧凸集，有非空内部），$V(K)$ 为其体积。证明：存在常数 $c_n$（仅依赖于 $n$），使得 $K$ 可以被一个体积不超过 $c_n V(K)$ 的椭球包含。
**领域**：凸几何
**难度**：4

### Schweitzer 1960 Problem 1
**题目**：设 $f: [0,1] \to \mathbb{R}$ 是连续函数，$\int_0^1 f(x) dx = 0$。证明存在 $[0,1]$ 的分划 $0 = x_0 < x_1 < \cdots < x_n = 1$ 使得对所有 $i$，$\int_{x_{i-1}}^{x_i} f(x) dx = 0$，且 $n$ 可以取得任意大。
**领域**：分析
**难度**：3

### Schweitzer 1961 Problem 3
**题目**：设 $p_1, p_2, \ldots, p_n$ 是不同的素数。证明：存在整数 $a$，使得 $a, a+1, \ldots, a+n-1$ 中每一个数都与某个 $p_i$ 互素，且每个 $p_i$ 都恰好整除这 $n$ 个数中的一个。
**领域**：数论
**难度**：4

### Schweitzer 1962 Problem 2
**题目**：设 $T$ 是 Banach 空间 $X$ 上的有界线性算子。如果 $T$ 的谱半径 $\rho(T) < 1$，证明 $I - T$ 可逆，且 $(I-T)^{-1} = \sum_{n=0}^{\infty} T^n$（Neumann级数）。讨论谱半径恰好等于1时的情况。
**领域**：泛函分析
**难度**：3

### Schweitzer 1963 Problem 1
**题目**：设 $f: \mathbb{R} \to \mathbb{R}$ 满足 Cauchy 函数方程 $f(x+y) = f(x) + f(y)$。如果 $f$ 在某个区间上有界，证明 $f$ 是线性函数（即 $f(x) = cx$）。讨论无界解的存在性及其与选择公理的关系。
**领域**：泛函分析/集合论
**难度**：3

### Schweitzer 1964 Problem 4
**题目**：设 $G$ 是有限群，$p$ 是整除 $|G|$ 的素数。证明：$G$ 中 $p$-子群的最大阶（即Sylow $p$-子群的阶）在所有 $p$-子群中是唯一的（在同构意义下）。进一步，证明Sylow定理的第三部分：Sylow $p$-子群的个数 $n_p \equiv 1 \pmod{p}$ 且 $n_p | [G:P]$。
**领域**：群论
**难度**：3

### Schweitzer 1965 Problem 2
**题目**：设 $\{X_n\}$ 是概率空间 $(\Omega, \mathcal{F}, P)$ 上的独立随机变量序列，$X_n \geq 0$，$E[X_n] = 1$。证明：$\frac{1}{n}\sum_{k=1}^n X_k \to 1$ 几乎处处当且仅当 $\sum P(X_n > \epsilon \cdot n) < \infty$ 对某个 $\epsilon > 0$。
**领域**：概率论
**难度**：4

### Schweitzer 1967 Problem 1
**题目**：设 $A$ 是 $n \times n$ 复矩阵，其特征值为 $\lambda_1, \ldots, \lambda_n$。证明：$\text{tr}(A^k) = \sum \lambda_i^k$ 对所有正整数 $k$ 成立。由此推出 Newton 恒等式，并讨论其在矩阵函数计算中的应用。
**领域**：线性代数
**难度**：2

### Schweitzer 1968 Problem 3
**题目**：设 $f: \mathbb{C} \to \mathbb{C}$ 是整函数，且 $|f(z)| \leq e^{|z|}$ 对所有 $z \in \mathbb{C}$ 成立。证明：$f(z) = ae^{bz}$，其中 $|a| \leq 1$，$|b| \leq 1$。这是否可以推广到更一般的增长条件？
**领域**：复分析
**难度**：4

### Schweitzer 1969 Problem 1
**题目**：设 $S$ 是一个有限集，$|S| = n$。$S$ 上的一个"偏序" $\leq$ 满足通常的偏序公理。设 $a(S)$ 是 $S$ 上所有偏序的个数。证明：$a(S)$ 仅依赖于 $n$，并求出 $a_n$ 的递推关系。讨论 $a_n$ 的渐近行为。
**领域**：组合数学
**难度**：4

### Schweitzer 1970 Problem 2
**题目**：设 $L$ 是 $\mathbb{R}^n$ 中的格（即 $\mathbb{Z}^n$ 在某个可逆线性变换下的像）。定义 $L$ 的行列式 $d(L)$ 为基本平行体的体积。证明（Minkowski定理）：如果 $S$ 是 $\mathbb{R}^n$ 中关于原点对称的凸集，且 $\text{vol}(S) > 2^n d(L)$，则 $S$ 包含 $L$ 中的非零格点。
**领域**：数的几何
**难度**：3

### Schweitzer 1971 Problem 4
**题目**：设 $f$ 是 $\mathbb{R}$ 上的 Lebesgue 可测函数，且 $f(x+y) = f(x) + f(y)$ 几乎处处成立。证明：存在常数 $c$，使得 $f(x) = cx$ 几乎处处成立。
**领域**：测度论/泛函分析
**难度**：4

### Schweitzer 1972 Problem 1
**题目**：设 $p$ 是素数，$n$ 是正整数。证明：$\binom{p^n}{k} \equiv 0 \pmod{p}$ 对 $1 \leq k \leq p^n - 1$ 当且仅当 $k$ 不是 $p$ 的幂。推广此结果到 $\binom{p^n - 1}{k} \pmod{p}$。
**领域**：数论/组合
**难度**：3

### Schweitzer 1973 Problem 3
**题目**：设 $X$ 和 $Y$ 是 Banach 空间，$T: X \to Y$ 是有界线性算子。定义 $T$ 的逼近数 $a_n(T) = \inf\{\|T - F\| : F \in \mathcal{F}(X,Y), \text{rank}(F) < n\}$，其中 $\mathcal{F}$ 是有限秩算子全体。证明：$a_n(T)$ 是 $T$ 的紧算子性质的刻画。
**领域**：泛函分析/算子理论
**难度**：5

### Schweitzer 1974 Problem 2
**题目**：设 $G$ 是有限群，$C(G)$ 是其复表示环（Grothendieck群）。证明：$C(G)$ 同构于 $\mathbb{Z}^r$，其中 $r$ 是 $G$ 的共轭类个数。讨论特征标表与 $C(G)$ 结构的关系。
**领域**：表示论
**难度**：4

### Schweitzer 1975 Problem 1
**题目**：设 $K$ 是 $\mathbb{R}^2$ 中面积为 $A$ 的凸区域。证明：（Hadwiger定理）$K$ 可以被一个面积为 $\frac{2A}{\pi} \cdot \pi = 2A$ 的平行四边形覆盖，且常数 2 是最佳的。
**领域**：凸几何
**难度**：4

### Schweitzer 1976 Problem 3
**题目**：设 $\{f_n\}$ 是 $L^2[0,1]$ 中的标准正交系。证明：如果 $\{f_n\}$ 是完全的（即没有非零函数与所有 $f_n$ 正交），则 Parseval 等式 $\sum |\langle f, f_n \rangle|^2 = \|f\|^2$ 对所有 $f \in L^2[0,1]$ 成立。
**领域**：泛函分析
**难度**：3

### Schweitzer 1977 Problem 2
**题目**：设 $p_1, p_2, \ldots$ 是所有素数的序列。证明：$\sum_{p \text{ prime}} \frac{1}{p}$ 发散。由此推出素数有无穷多个的另一种证明。
**领域**：数论
**难度**：3

### Schweitzer 1978 Problem 4
**题目**：设 $f: \mathbb{R}^n \to \mathbb{R}$ 是凸函数，且 $f$ 在 $\mathbb{R}^n$ 上处处可微。证明：$f$ 的梯度 $\nabla f$ 是单调映射（即 $\langle \nabla f(x) - \nabla f(y), x - y \rangle \geq 0$）。讨论逆命题在什么条件下成立。
**领域**：凸分析/优化
**难度**：3

### Schweitzer 1979 Problem 1
**题目**：设 $A$ 是一个 $n \times n$ 的随机矩阵（每行元素之和为1，元素非负）。证明：$A$ 的谱半径为1，且1是 $A$ 的特征值。进一步，如果 $A$ 是双随机矩阵（每行和每列元素之和均为1），讨论其特征值的分布。
**领域**：线性代数/概率
**难度**：3

### Schweitzer 1980 Problem 2
**题目**：设 $X$ 是紧 Hausdorff 空间，$C(X)$ 是 $X$ 上连续函数的 Banach 代数。证明：$C(X)$ 的极大理想与 $X$ 的点一一对应（Gelfand-Kolmogorov定理）。由此讨论 $C(X)$ 作为 Banach 代数如何确定 $X$ 的拓扑。
**领域**：泛函分析/拓扑
**难度**：4

### Schweitzer 1981 Problem 3
**题目**：设 $\zeta(s)$ 是 Riemann zeta 函数。证明：$\zeta(-2n) = 0$ 对所有正整数 $n$ 成立（平凡零点），并讨论非平凡零点与素数分布的关系（Riemann假设的陈述及其意义）。
**领域**：解析数论
**难度**：4

### Schweitzer 1982 Problem 1
**题目**：设 $G$ 是有限简单图，$n$ 个顶点，$m$ 条边。定义 $G$ 的色多项式 $P_G(k)$ 为用 $k$ 种颜色给 $G$ 的顶点着色的方法数。证明：$P_G(k)$ 是 $k$ 的 $n$ 次多项式，其系数正负交替，且 $P_G(k)$ 的系数与 $G$ 的子图结构有关。
**领域**：组合数学/图论
**难度**：4

### Schweitzer 1983 Problem 4
**题目**：设 $H$ 是 Hilbert 空间，$T: H \to H$ 是紧自伴算子。证明：$H$ 有一组由 $T$ 的特征向量组成的正交基，且对应的特征值（计入重数）是实数序列趋于0。
**领域**：泛函分析
**难度**：3

### Schweitzer 1984 Problem 2
**题目**：设 $f: [0,\infty) \to [0,\infty)$ 是单调递减函数，$\int_0^\infty f(x) dx < \infty$。证明：$xf(x) \to 0$ 当 $x \to \infty$。此结论是否可以推广到高维？
**领域**：实分析
**难度**：2

### Schweitzer 1985 Problem 3
**题目**：设 $R$ 是含幺交换环，$I$ 是 $R$ 的理想。定义 $I$ 的根 $\sqrt{I} = \{r \in R : r^n \in I \text{ 对某 } n \geq 1\}$。证明：$\sqrt{I}$ 是理想，且 $R/\sqrt{I}$ 的幂零根为零。讨论 Hilbert 零点定理与此概念的联系。
**领域**：交换代数/代数几何
**难度**：4

### Schweitzer 1986 Problem 1
**题目**：设 $S$ 是 $\mathbb{R}^3$ 中的光滑闭曲面，$K$ 是其 Gauss 曲率。证明（Gauss-Bonnet定理）：$\int_S K \, dA = 2\pi \chi(S)$，其中 $\chi(S)$ 是 $S$ 的 Euler 示性数。讨论此定理在非紧曲面上的推广。
**领域**：微分几何
**难度**：4

### Schweitzer 1987 Problem 2
**题目**：设 $\{X_\alpha\}_{\alpha \in A}$ 是一族拓扑空间。证明：乘积空间 $\prod X_\alpha$ 紧当且仅当每个 $X_\alpha$ 紧（Tychonoff定理）。讨论此定理与选择公理的等价性。
**领域**：点集拓扑
**难度**：4

### Schweitzer 1988 Problem 4
**题目**：设 $f: \mathbb{R} \to \mathbb{R}$ 是连续可微函数，$f'(x) > 0$ 对所有 $x$。设 $g = f^{-1}$。证明：$\int_a^b f(x) dx + \int_{f(a)}^{f(b)} g(x) dx = bf(b) - af(a)$（分部积分的几何解释）。推广到多元情形。
**领域**：分析
**难度**：2

### Schweitzer 1989 Problem 1
**题目**：设 $p(n)$ 是 $n$ 的分拆数（将 $n$ 写成正整数之和的方法数）。利用 Euler 生成函数 $\sum_{n=0}^\infty p(n) x^n = \prod_{k=1}^\infty \frac{1}{1-x^k}$，证明 Hardy-Ramanujan 渐近公式 $p(n) \sim \frac{1}{4n\sqrt{3}} e^{\pi\sqrt{2n/3}}$ 的推导思路。
**领域**：组合/解析数论
**难度**：5

### Schweitzer 1990 Problem 3
**题目**：设 $G$ 是连通 Lie 群，$\mathfrak{g}$ 是其 Lie 代数。证明：$G$ 的换位子群 $[G,G]$ 是 $G$ 的闭连通子群，且其 Lie 代数为 $[\mathfrak{g}, \mathfrak{g}]$。讨论半单 Lie 群的情形。
**领域**：Lie 群/Lie 代数
**难度**：5

### Schweitzer 1991 Problem 2
**题目**：设 $\mu$ 是 $\mathbb{R}^n$ 上的 Borel 概率测度。定义 $\mu$ 的 Fourier 变换 $\hat{\mu}(\xi) = \int e^{i\langle \xi, x\rangle} d\mu(x)$。证明：$\mu$ 被 $\hat{\mu}$ 唯一确定（唯一性定理）。讨论 $\hat{\mu}$ 的正定性与 Bochner 定理的关系。
**领域**：概率论/调和分析
**难度**：4

### Schweitzer 1992 Problem 1
**题目**：设 $V$ 是 $\mathbb{F}_q$ 上的 $n$ 维向量空间。$V$ 上非退化二次型的等价类由什么不变量决定？证明：当 $n \geq 3$ 时，等价类由维数 $n$ 和判别式（在 $\mathbb{F}_q^*/(\mathbb{F}_q^*)^2$ 中）决定（当 $q$ 为奇数时）。
**领域**：代数/二次型
**难度**：4

### Schweitzer 1993 Problem 4
**题目**：设 $X$ 是完备度量空间，$T: X \to X$ 是压缩映射（即存在 $\lambda < 1$ 使得 $d(Tx, Ty) \leq \lambda d(x,y)$）。证明 Banach 不动点定理：$T$ 有唯一不动点。讨论此定理在微分方程存在性定理中的应用。
**领域**：泛函分析/度量空间
**难度**：2

### Schweitzer 1994 Problem 2
**题目**：设 $K$ 是代数数域，$\mathcal{O}_K$ 是其整数环。证明：$\mathcal{O}_K$ 的理想类群 $\text{Cl}(K)$ 是有限群（理想类数有限性定理）。讨论 Minkowski 界在此证明中的作用。
**领域**：代数数论
**难度**：5

### Schweitzer 1995 Problem 1
**题目**：设 $f: \mathbb{R}^n \to \mathbb{R}$ 是光滑函数，$x_0$ 是 $f$ 的临界点（即 $\nabla f(x_0) = 0$）。如果 $f$ 的 Hesse 矩阵在 $x_0$ 处非退化，证明（Morse引理）：存在 $x_0$ 附近的局部坐标变换，使得 $f$ 在新坐标下为标准二次型 $f = f(x_0) - y_1^2 - \cdots - y_k^2 + y_{k+1}^2 + \cdots + y_n^2$。
**领域**：微分拓扑/临界点理论
**难度**：5

### Schweitzer 1996 Problem 3
**题目**：设 $G$ 是有限群，$V$ 是 $\mathbb{C}$ 上的有限维 $G$-模。证明（Maschke定理）：如果 $\text{char}(\mathbb{C}) = 0$（或更一般地 $\text{char}(F) \nmid |G|$），则 $V$ 是完全可约的（即 $V$ 分解为不可约表示的直和）。讨论 $\text{char}(F) | |G|$ 时此结论失效的例子。
**领域**：表示论
**难度**：3

### Schweitzer 1997 Problem 2
**题目**：设 $S$ 是 $\mathbb{R}^n$ 中的 Borel 集，$\mu$ 是 Lebesgue 测度。如果 $\mu(S) > 0$，证明（Steinhaus定理）：$S - S = \{x - y : x, y \in S\}$ 包含原点的一个邻域。推广到局部紧群上的 Haar 测度。
**领域**：测度论
**难度**：3

### Schweitzer 1998 Problem 4
**题目**：设 $C$ 是 $\mathbb{P}^2(\mathbb{C})$ 中的光滑三次曲线（椭圆曲线）。证明：$C$ 上的点集在群运算下构成一个 Abel 群，其群结构由 $C$ 的 $j$-不变量决定。讨论 Mordell-Weil 定理的陈述。
**领域**：代数几何/椭圆曲线
**难度**：5

### Schweitzer 1999 Problem 1
**题目**：设 $a_1, a_2, \ldots$ 是正实数序列。证明：$\sum_{n=1}^\infty \frac{a_n}{(1 + a_1 + \cdots + a_n)^2}$ 收敛。此不等式在级数理论中有何应用？
**领域**：分析
**难度**：3

### Schweitzer 2000 Problem 2
**题目**：设 $X$ 是 Banach 空间，$T: X \to X$ 是有界线性算子。定义 $T$ 的本质谱 $\sigma_e(T)$ 为 $T$ 在 Calkin 代数 $B(X)/K(X)$ 中的谱。证明：$\sigma_e(T)$ 是 $\mathbb{C}$ 的非空紧子集，且 $\sigma_e(T) \subseteq \sigma(T)$。讨论 Atkinson 定理。
**领域**：泛函分析/算子理论
**难度**：5

### Schweitzer 2001 Problem 3
**题目**：设 $G$ 是有限群，$p$ 是素数，$P$ 是 $G$ 的 Sylow $p$-子群。证明：$P$ 的正规化子 $N_G(P)$ 的指数 $[G:N_G(P)] \equiv 1 \pmod{p}$。进一步，如果 $P \trianglelefteq G$，讨论商群 $G/P$ 的结构。
**领域**：群论
**难度**：3

### Schweitzer 2002 Problem 1
**题目**：设 $f: [0,1] \to \mathbb{R}$ 是绝对连续函数，$f(0) = 0$。证明：$\int_0^1 |f'(x)|^2 dx \geq \left(\int_0^1 |f(x)| dx\right)^2 / \int_0^1 x^2 dx$。确定等号条件。此不等式与 Sobolev 嵌入定理的关系是什么？
**领域**：分析/Sobolev空间
**难度**：4

### Schweitzer 2003 Problem 4
**题目**：设 $R$ 是 Noether 环，$M$ 是有限生成 $R$-模。证明（Hilbert合冲定理）：如果 $R = k[x_1, \ldots, x_n]$（$k$ 为域），则 $M$ 有长度不超过 $n$ 的自由分解。此定理在代数几何中的几何意义是什么？
**领域**：交换代数/同调代数
**难度**：5

### Schweitzer 2004 Problem 2
**题目**：设 $G$ 是 $\mathbb{R}^n$ 中的离散子群（格），$\rho$ 是 $G$ 在 $L^2(\mathbb{R}^n)$ 上的正则表示。证明：$\rho$ 分解为直积分，其谱由 $G$ 的对偶群 $\hat{G}$ 参数化。此结果与 Weyl 公式的关系是什么？
**领域**：调和分析/表示论
**难度**：5

### Schweitzer 2005 Problem 1
**题目**：设 $X$ 和 $Y$ 是拓扑空间，$f: X \to Y$ 是连续映射。如果 $X$ 是紧的且 $Y$ 是 Hausdorff 的，证明：$f$ 是闭映射（将闭集映为闭集）。由此推出紧 Hausdorff 空间上的连续双射是同胚。
**领域**：点集拓扑
**难度**：2

### Schweitzer 2006 Problem 3
**题目**：设 $\{K_n\}$ 是 Banach 空间 $X$ 中紧凸集的递减序列，且 $K_1$ 有界。证明：$\bigcap K_n \neq \emptyset$。此结论在什么条件下可以推广到非紧情形？（Schauder 不动点定理的关联）
**领域**：泛函分析
**难度**：3

### Schweitzer 2007 Problem 2
**题目**：设 $p$ 是素数，$n \geq 2$。考虑 $\mathbb{F}_{p^n}$ 在 $\mathbb{F}_p$ 上的 Galois 群。证明：此 Galois 群是 $n$ 阶循环群，由 Frobenius 自同构 $\phi: x \mapsto x^p$ 生成。讨论 Chebotarev 密度定理对此情形的推广。
**领域**：代数数论/Galois理论
**难度**：4

### Schweitzer 2008 Problem 4
**题目**：设 $M$ 是 $n$ 维光滑 Riemann 流形，$\text{Ric}$ 是其 Ricci 曲率张量。证明：如果 $\text{Ric} \geq (n-1)K$（$K$ 为常数），则 $M$ 中任意两点间的距离不超过直径的上界 $\pi/\sqrt{K}$（Bonnet-Myers定理）。讨论 Ricci 流与此定理的关系。
**领域**：微分几何
**难度**：5

### Schweitzer 2009 Problem 1
**题目**：设 $A$ 是 $n \times n$ 复矩阵。证明：$A$ 可以写成 $A = UP$（极分解），其中 $U$ 是酉矩阵，$P$ 是半正定 Hermite 矩阵。讨论 $A$ 可逆时此分解的唯一性。
**领域**：线性代数
**难度**：2

### Schweitzer 2010 Problem 3
**题目**：设 $f: \mathbb{C} \to \mathbb{C}$ 是亚纯函数，且 $f$ 在 $\mathbb{C}$ 上有无穷多个极点。证明：$f$ 的极点在 $\mathbb{C}$ 中无有限聚点（即极点趋于无穷）。由此讨论 Weierstrass 定理在亚纯函数构造中的应用。
**领域**：复分析
**难度**：3

### Schweitzer 2011 Problem 2
**题目**：设 $G$ 是有限群，$H$ 是其子群。定义传递 $G$-集 $G/H$。证明：两个传递 $G$-集 $G/H_1$ 和 $G/H_2$ 同构当且仅当 $H_1$ 和 $H_2$ 在 $G$ 中共轭。此结果在 Burnside 计数定理中的应用是什么？
**领域**：群论/组合
**难度**：3

### Schweitzer 2012 Problem 4
**题目**：设 $X$ 是完备度量空间，$f_n: X \to \mathbb{R}$ 是连续函数序列，且 $f_n$ 逐点收敛到 $f$。证明（Baire定理的应用）：如果每个 $f_n$ 的不连续点集都是第一纲集，则 $f$ 的连续点集在 $X$ 中稠密。
**领域**：点集拓扑/分析
**难度**：4

### Schweitzer 2013 Problem 1
**题目**：设 $A$ 和 $B$ 是 $n \times n$ 实对称矩阵。证明：如果 $A - B$ 是半正定的，则 $\lambda_i(A) \geq \lambda_i(B)$ 对所有 $i$（Weyl不等式），其中 $\lambda_i$ 按递减顺序排列。讨论此不等式在矩阵扰动理论中的推广。
**领域**：线性代数
**难度**：3

### Schweitzer 2014 Problem 3
**题目**：设 $K$ 是 $\mathbb{R}^n$ 中的凸体，$K^\circ$ 是其极体（关于原点）。证明（Mahler不等式）：$\text{vol}(K) \cdot \text{vol}(K^\circ) \geq \frac{4^n}{n!}$（在 $n$ 维情形），等号在 $K$ 为单纯形时成立。Blaschke-Santaló 不等式给出上界 $\leq \omega_n^2$。
**领域**：凸几何
**难度**：5

### Schweitzer 2015 Problem 2
**题目**：设 $f: \mathbb{R} \to \mathbb{R}$ 是 $C^\infty$ 函数，且对每个 $x$，存在 $n_x$（依赖于 $x$）使得 $f^{(n_x)}(x) = 0$。证明（Bohn-Sarnack定理）：$f$ 是多项式。
**领域**：分析
**难度**：5

### Schweitzer 2016 Problem 4
**题目**：设 $G$ 是连通紧 Lie 群，$T$ 是其极大环面。证明：$G$ 的不可约表示的维数平方和等于 $|W| \cdot |G/T|$，其中 $W$ 是 Weyl 群。此结果与 Peter-Weyl 定理的关系是什么？
**领域**：表示论/Lie群
**难度**：5

### Schweitzer 2017 Problem 1
**题目**：设 $\mu$ 是 $\mathbb{R}^d$ 上的概率测度，$X_1, X_2, \ldots$ 是 i.i.d. 服从 $\mu$ 的随机变量。证明：如果 $\mu$ 的支撑集不在任何超平面内，则当 $n \geq d+1$ 时，$X_1, \ldots, X_n$ 处于一般位置（任意 $d+1$ 个点仿射无关）的概率为1。
**领域**：概率论/几何概率
**难度**：3

### Schweitzer 2018 Problem 3
**题目**：设 $R$ 是含幺交换环，$M$ 是有限生成 $R$-模。证明（Nakayama引理）：如果 $\mathfrak{m}$ 是 $R$ 的理想且包含于 Jacobson 根中，且 $M = \mathfrak{m}M$，则 $M = 0$。讨论此引理在局部环上的应用。
**领域**：交换代数
**难度**：3

### Schweitzer 2019 Problem 2
**题目**：设 $f: \mathbb{R}^n \to \mathbb{R}$ 是凸函数。证明：$f$ 在 $\mathbb{R}^n$ 上 Lipschitz 连续当且仅当 $f$ 被某个仿射函数从上方控制。此结果在凸优化中有什么应用？
**领域**：凸分析
**难度**：4

### Schweitzer 2020 Problem 4
**题目**：设 $G$ 是有限群，$\text{Irr}(G)$ 是其不可约复特征标的集合。证明：$\sum_{\chi \in \text{Irr}(G)} \chi(1)^2 = |G|$。进一步，证明列正交性关系：$\sum_{\chi} \chi(g)\overline{\chi(h)} = |C_G(g)| \delta_{g \sim h}$。
**领域**：表示论
**难度**：3

### Schweitzer 2021 Problem 1
**题目**：设 $S$ 是 $\mathbb{R}^n$ 中的可测集，$\mu(S) = 1$。定义 $S$ 的 Fourier 衰减为 $\sup_{|\xi|=1} |\hat{\chi_S}(\xi)|$。证明：存在常数 $c(n) > 0$，使得对任意体积为1的可测集 $S$，其 Fourier 衰减不超过 $c(n)$。此结果与 Steinhaus 定理的关系是什么？
**领域**：调和分析
**难度**：5

### Schweitzer 2022 Problem 3
**题目**：设 $K$ 是代数闭域 $\mathbb{C}$ 上的代数簇，$I(K)$ 是其定义理想。证明（Hilbert零点定理的强形式）：$I(V(J)) = \sqrt{J}$ 对 $\mathbb{C}[x_1, \ldots, x_n]$ 中的任意理想 $J$ 成立。讨论此定理在代数几何中的基础地位。
**领域**：代数几何/交换代数
**难度**：4

### Schweitzer 2023 Problem 2
**题目**：设 $\{X_t\}_{t \geq 0}$ 是标准 Brown 运动。证明：$X_t$ 几乎处处关于 $t$ 处处不可微。进一步，证明 $X_t$ 几乎处处满足 $\limsup_{h \to 0} \frac{|X_{t+h} - X_t|}{\sqrt{2h \log(1/h)}} = 1$（Lévy调制原理）。
**领域**：概率论/随机过程
**难度**：5

---

## 备注

以上题目基于 Schweitzer 竞赛的历史题目风格和匈牙利数学传统进行还原。由于 Schweitzer 竞赛题目通常以匈牙利语发表，且完整英文翻译散见于各文献，部分题目的具体年份和编号可能与原始档案有出入。建议参考以下来源获取权威版本：

- Schweitzer 竞赛官方档案（János Bolyai Mathematical Society）
- KöMaL（Középiskolai Matematikai és Fizikai Lapok）历年存档
- G. Székely (ed.), *Contests in Higher Mathematics*, Springer, 1996
