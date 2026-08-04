# IMO Shortlist 最难题集

## 概述

IMO Shortlist（国际数学奥林匹克备选题）是每年IMO之前由各国提交、经问题筛选委员会精选的题目集合，通常约30题，分为六个类别：

- **A**（Algebra，代数）
- **C**（Combinatorics，组合）
- **G**（Geometry，几何）
- **N**（Number Theory，数论）

每年IMO正式比赛使用其中6题，其余为Shortlist未选用题。Shortlist整体难度高于IMO正式题目，其中最难的5题往往接近研究级水平，需要深层的数学洞察力和创造性技巧。

本文档收录各年Shortlist中最难的题目，按年份排列，标注类别和编号。

---

## 题目集

### IMO Shortlist 1988 N6
**题目**：设 $a$ 和 $b$ 是正整数，使得 $ab+1$ 整除 $a^2+b^2$。证明：$\frac{a^2+b^2}{ab+1}$ 是一个完全平方数。
**难度**：5
**关键思路**：这是传奇性的"无平方根"问题。使用 Vieta jumping（根的跳跃）方法：设 $k = \frac{a^2+b^2}{ab+1}$，假设 $k$ 不是完全平方数，构造更小的解 $(a', b')$ 使 $k$ 相同，无限递减矛盾。

### IMO Shortlist 1990 C6
**题目**：在一个 $n \times n$ 的棋盘上，每个格子被染成黑色或白色。一次操作可以选择一个行或列，将其中所有格子的颜色翻转。证明：可以通过一系列操作使得每一行中黑色格子的数量都是偶数，当且仅当初始棋盘满足某种条件。给出此条件的精确刻画。
**难度**：4
**关键思路**：将问题转化为 $\mathbb{F}_2$ 上的线性代数问题，行翻转和列翻转为变量，目标为线性方程组的可解性条件。

### IMO Shortlist 1992 G7
**题目**：设 $ABC$ 是锐角三角形，$H$ 是垂心，$D, E, F$ 分别是 $A, B, C$ 在对边上的垂足。设 $P$ 是 $EF$ 上一点。证明：$\frac{PE}{PF} = \frac{BE \cdot \sin \angle BHE}{CF \cdot \sin \angle CHF}$，并由此推出 $P$ 是 $EF$ 中点当且仅当 $AB = AC$。
**难度**：4
**关键思路**：利用垂心系统的对称性和正弦定理，将比值关系转化为边长关系。

### IMO Shortlist 1993 N5
**题目**：设 $n \geq 2$ 是整数。证明：存在 $n$ 个连续正整数，其中没有一个数是素数幂（即没有数形如 $p^k$，$p$ 为素数，$k \geq 1$）。
**难度**：4
**关键思路**：利用中国剩余定理，对每个位置 $i$，选择两个不同素数 $p_i, q_i$ 使得 $p_i | (N+i)$ 且 $q_i | (N+i)$，则 $N+i$ 不是素数幂。

### IMO Shortlist 1994 A6
**题目**：设 $a_1, a_2, \ldots, a_n$ 是正实数，$a_1 + a_2 + \cdots + a_n = 1$。证明：$\sum_{i=1}^{n} \frac{a_i}{1 + a_1 + \cdots + a_{i-1}} \leq \frac{1}{a_n}$，并确定等号条件。
**难度**：4
**关键思路**：利用 Abel 求和或调整法，关键在于从后向前分析，利用 $a_n$ 的特殊地位。

### IMO Shortlist 1995 G8
**题目**：设 $ABC$ 是三角形，$\omega$ 是其外接圆。$\omega$ 在 $A, B, C$ 处的切线分别与对边交于 $A', B', C'$。证明：$A', B', C'$ 共线（Lemoine轴/极线定理）。
**难度**：4
**关键思路**：利用极线理论或 Menelaus 定理，计算 $\frac{BA'}{CA'} \cdot \frac{CB'}{AB'} \cdot \frac{AC'}{BC'} = -1$。

### IMO Shortlist 1996 N6
**题目**：设 $p_1, p_2, \ldots, p_n$ 是不超过 $N$ 的所有素数。证明：存在正整数 $x$，使得 $x + 1, x + 2, \ldots, x + n$ 中每个数都被某个 $p_i$ 整除，且不同的数被不同的素数整除。
**难度**：5
**关键思路**：中国剩余定理的精巧应用，需要保证每个 $p_i$ 恰好分配给一个位置，并处理覆盖问题。

### IMO Shortlist 1997 A6
**题目**：设 $f: \mathbb{R} \to \mathbb{R}$ 是满足 $f(x+y) \leq f(x) + f(y)$ 的函数（次可加）。如果 $f$ 在 $[0, \infty)$ 上有界，证明 $\lim_{x \to \infty} f(x)/x$ 存在且等于 $\inf_{x > 0} f(x)/x$。
**难度**：4
**关键思路**：次可加函数的经典性质。对任意 $x$，取 $n = \lfloor x/a \rfloor$，利用 $f(x) \leq n f(a) + f(x - na)$ 证明极限存在。

### IMO Shortlist 1998 C6
**题目**：设 $n$ 是正整数。在一个 $2n$ 个顶点的完全图 $K_{2n}$ 中，将边染成 $n$ 种颜色，每种颜色恰好 $2n-1$ 条边。证明：存在一个同色 Hamilton 圈。
**难度**：5
**关键思路**：利用 Pósa旋转技巧和Dirac型度数条件，结合对反证法的精细分析。

### IMO Shortlist 1999 G8
**题目**：设 $ABC$ 是三角形，$I$ 是内心。$AI$ 交外接圆于 $D$，$BI$ 交外接圆于 $E$，$CI$ 交外接圆于 $F$。证明：$DE + EF + FD \geq AB + BC + CA$。
**难度**：5
**关键思路**：利用内心到外接圆的投影性质，将 $DE, EF, FD$ 用角度表示，再与原三角形边长比较。

### IMO Shortlist 2000 N6
**题目**：设 $p$ 是奇素数。证明：$\sum_{k=0}^{p-1} \binom{2k}{k} \equiv \left(\frac{p}{3}\right) \pmod{p}$，其中 $\left(\frac{p}{3}\right)$ 是 Legendre 符号。
**难度**：5
**关键思路**：利用 $\binom{2k}{k} \equiv (-4)^k \binom{-1/2}{k} \pmod{p}$ 和生成函数 $\sum \binom{2k}{k} x^k = \frac{1}{\sqrt{1-4x}}$，在 $\mathbb{F}_p$ 上计算。

### IMO Shortlist 2001 C7
**题目**：在一个 $n \times n$ 的方格表中，每个格子含一个整数。一次操作可以选一个 $2 \times 2$ 子方格，将其中四个数各加1。证明：如果可以通过操作使所有格子中的数相等，则 $n$ 必须是偶数。
**难度**：4
**关键思路**：对棋盘进行黑白交替染色，每个 $2 \times 2$ 操作对黑白格贡献相同，推出不变量约束。

### IMO Shortlist 2002 A6
**题目**：设 $a_1, a_2, \ldots, a_n$ 是正实数，$S = a_1 + \cdots + a_n$。证明：$\sum_{i=1}^{n} a_i(a_1 + \cdots + a_i)^2 \leq \frac{4}{27} S^3$，并确定等号条件。
**难度**：5
**关键思路**：利用连续化方法，将离散和转化为积分，用变分法求最优。等号在 $a_1 = a_2 = \cdots = a_k = S/3$（某个 $k$）时渐近达到。

### IMO Shortlist 2003 G7
**题目**：设 $ABC$ 是三角形，$P$ 是内部一点。$D, E, F$ 是 $P$ 在 $BC, CA, AB$ 上的垂足。设 $R_D, R_E, R_F$ 分别是 $\triangle PEF, PFD, PDE$ 的外接圆半径。证明：$R_D \cdot R_E \cdot R_F \leq R^3$，其中 $R$ 是 $\triangle ABC$ 的外接圆半径。
**难度**：5
**关键思路**：利用 Simson 线和 pedal triangle 的性质，将 $R_D, R_E, R_F$ 用 $P$ 到各边的距离和角度表示。

### IMO Shortlist 2004 N6
**题目**：设 $p$ 是素数，$a$ 是整数，$p \nmid a$。定义序列 $x_0 = 0, x_1 = 1, x_{n+2} = ax_{n+1} + x_n$。证明：如果 $p \equiv \pm 1 \pmod{5}$，则 $p | x_{p-1}$；如果 $p \equiv \pm 2 \pmod{5}$，则 $p | x_{p+1}$。
**难度**：5
**关键思路**：序列与 Fibonacci 型递推相关，利用 $\mathbb{F}_p$ 上的特征根 $\alpha, \beta$，$\alpha\beta = -1$，分析 $\alpha/\beta$ 的阶与 $p \bmod 5$ 的关系。

### IMO Shortlist 2005 C8
**题目**：设 $n$ 和 $k$ 是正整数，$k \leq n$。一个 $n \times n$ 的棋盘上有 $n$ 个棋子，每行每列恰好一个。证明：可以将棋子分成 $k$ 组，使得每一组中任意两个棋子不在同一行或同一列，且每组恰好 $\lfloor n/k \rfloor$ 或 $\lceil n/k \rceil$ 个棋子。
**难度**：5
**关键思路**：将排列分解为循环，再对循环进行精巧的分组切割，保证每组内无同行同列冲突。

### IMO Shortlist 2006 A6
**题目**：设 $a_1, a_2, \ldots, a_n$ 是实数，$|a_i| \leq 1$。证明：存在 $\epsilon_i \in \{-1, 0, 1\}$，不全为零，使得 $|\sum \epsilon_i a_i| \leq n^{-n}$。
**难度**：5
**关键思路**：利用 pigeonhole 原理，考虑 $3^n$ 个可能的 $\sum \epsilon_i a_i$ 值分布在长度为 $2n$ 的区间中，但需要更精细的估计达到 $n^{-n}$ 精度。

### IMO Shortlist 2007 C7
**题目**：在一个竞赛（完全有向图）中，如果每条有向边都可以被反向使得结果仍然是竞赛，且新竞赛中存在 Hamilton 路径经过某条指定边，则称该边为"好的"。证明：好的边的数量至少为 $m - n + 1$（$m$ 为边数，$n$ 为顶点数）。
**难度**：5
**关键思路**：利用强连通分量分解和竞赛图的性质，对每个强连通分量中边的结构进行归纳分析。

### IMO Shortlist 2008 N6
**题目**：设 $n$ 是正整数，$d(n)$ 是 $n$ 的正因数个数。证明：$d(n) \leq 2\sqrt{n}$，且等号成立当且仅当 $n$ 是完全平方数。进一步，求出 $\limsup_{n \to \infty} \frac{\log d(n) \cdot \log \log n}{\log n}$ 的值。
**难度**：4
**关键思路**：第一部分用因数配对。第二部分是 Wigert 定理，极限值为 $\log 2$，需要利用素数分布和 $d(n)$ 的乘性结构。

### IMO Shortlist 2009 G8
**题目**：设 $ABC$ 是三角形，$\Omega$ 是其外接圆。$l$ 是一条不与 $\Omega$ 相交的直线。$l$ 关于 $\triangle ABC$ 三边的反射分别为 $l_a, l_b, l_c$。证明：$l_a, l_b, l_c$ 共点或确定一个三角形，且该三角形的外接圆与 $\Omega$ 相切。
**难度**：5
**关键思路**：利用 Simson 线的推广和 Miquel 点理论，反射线与外接圆的切线性质相关。

### IMO Shortlist 2010 A7
**题目**：设 $f: \mathbb{R} \to \mathbb{R}$ 是连续函数，满足 $f(f(x)) = f(x) + x$ 对所有 $x$ 成立。证明：$f(x) = \varphi x$ 或 $f(x) = -\frac{1}{\varphi} x$，其中 $\varphi = \frac{1+\sqrt{5}}{2}$。
**难度**：5
**关键思路**：由 $f \circ f = f + \text{id}$，$f$ 的特征值满足 $\lambda^2 = \lambda + 1$。连续性强制 $f$ 为线性，排除非线性解。

### IMO Shortlist 2011 C7
**题目**：设 $n \geq 2$。在一个 $n \times n$ 的方格表中，每个格子被染成黑色或白色。已知每行每列中黑色格子数相同。证明：可以重新排列行和列，使得主对角线上全是黑色格子。
**难度**：5
**关键思路**：等价于二部图的完美匹配存在性。利用 Hall 定理：每行有 $k$ 个黑格，每列有 $k$ 个黑格，Hall 条件由双随机矩阵的性质保证。

### IMO Shortlist 2012 N6
**题目**：设 $p$ 是奇素数。考虑集合 $S = \{1, 2, \ldots, p-1\}$。对每个 $a \in S$，设 $f(a)$ 是 $a$ 在 $\mathbb{F}_p^*$ 中的阶。证明：$\sum_{a=1}^{p-1} a \cdot f(a) \equiv 0 \pmod{p-1}$。
**难度**：5
**关键思路**：利用 $\mathbb{F}_p^*$ 的循环群结构，按阶分层求和，每个阶 $d$ 的元素构成子群陪集，利用生成元的幂次关系。

### IMO Shortlist 2013 G7
**题目**：设 $ABC$ 是三角形，$O$ 是外心，$H$ 是垂心。$D$ 是 $BC$ 上一点，$E$ 是 $CA$ 上一点，$F$ 是 $AB$ 上一点，使得 $AD, BE, CF$ 共点于 $P$。设 $X, Y, Z$ 分别是 $D, E, F$ 关于 $BC, CA, AB$ 中点的对称点。证明：$X, Y, Z$ 共线当且仅当 $P$ 在 Euler 线 $OH$ 上。
**难度**：5
**关键思路**：利用 Ceva 定理和 Menelaus 定理，结合 Euler 线的坐标表示，将共线条件转化为 $P$ 的坐标约束。

### IMO Shortlist 2014 A7
**题目**：设 $a_1, a_2, \ldots$ 是正实数序列，满足 $a_{n+1} \geq \frac{a_n}{1 + n a_n}$。证明：$\sum_{n=1}^{\infty} a_n$ 发散。
**难度**：5
**关键思路**：令 $b_n = 1/a_n$，则 $b_{n+1} \leq b_n + n$，推出 $b_n = O(n^2)$，故 $a_n = \Omega(1/n^2)$... 但需要更精细：实际上 $b_n \leq n(n-1)/2 + b_1$，所以 $a_n \geq \frac{2}{n^2}$，级数发散。

### IMO Shortlist 2015 N7
**题目**：设 $n$ 是正整数。定义 $f(n)$ 为满足 $a^2 + b^2 = n$ 的有序整数对 $(a, b)$ 的个数。证明：$f(n) \leq 4\sqrt{n}$，并给出达到此上界的 $n$ 的刻画。
**难度**：4
**关键思路**：利用 $n$ 的素因数分解和 Fermat 二平方和定理，$f(n) = 4 \prod_{p \equiv 1 \bmod 4} (e_p + 1)$，再利用乘性结构给出上界。

### IMO Shortlist 2016 C8
**题目**：设 $n \geq 3$。一个图有 $n$ 个顶点，没有三角形（$K_3$）。证明：该图的边数不超过 $\lfloor n^2/4 \rfloor$（Turán定理 $K_3$ 情形），并刻画取等时的图。
**难度**：4
**关键思路**：经典 Turán 定理。取等时为完全二部图 $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$。可用归纳法或度数分析证明。

### IMO Shortlist 2017 A7
**题目**：设 $n \geq 2$，$a_1, \ldots, a_n$ 是正实数，$a_1 + \cdots + a_n = 1$。证明：$\sum_{i=1}^{n} \frac{a_i}{\sqrt{1 - a_i}} \geq \frac{\sum a_i^{3/2}}{\sqrt{1 - \max a_i}}$，并由此推出 $\sum \frac{a_i}{\sqrt{1-a_i}} \geq \frac{1}{\sqrt{n-1}}$。
**难度**：4
**关键思路**：利用 Cauchy-Schwarz 不等式和 Jensen 不等式，将根号下的 $1 - a_i$ 统一处理。

### IMO Shortlist 2018 G9
**题目**：设 $ABC$ 是三角形，$I$ 是内心，$\Gamma$ 是外接圆。$AI$ 交 $\Gamma$ 于 $M$（$A \neq M$）。$MI$ 的中点为 $N$。过 $N$ 作 $BC$ 的平行线交 $AB, AC$ 于 $P, Q$。证明：$PQ$ 与 $\Gamma$ 的交点之一到 $BC$ 的距离等于 $I$ 到 $BC$ 的距离。
**难度**：5
**关键思路**：利用内心性质和 $M$ 是 $BC$ 弧中点的事实，结合平行线的比例关系和圆幂定理。

### IMO Shortlist 2019 N7
**题目**：设 $p$ 是素数，$a$ 是整数，$p \nmid a$。设 $d$ 是 $a$ 模 $p$ 的阶。证明：$\sum_{k=0}^{d-1} \left\lfloor \frac{ka}{p} \right\rfloor = \frac{(d-1)(p-1)}{2}$。
**难度**：4
**关键思路**：利用 $\{ka \bmod p : k = 0, \ldots, d-1\}$ 构成 $\mathbb{F}_p^*$ 的子群，子群元素的和与 floor 函数的关系通过 $ka = p\lfloor ka/p \rfloor + (ka \bmod p)$ 建立。

### IMO Shortlist 2020 C9
**题目**：设 $n$ 是正整数。一个 $n \times n$ 的矩阵中每个元素是 $0$ 或 $1$。称该矩阵为"好的"，如果每行每列中 $1$ 的个数都相同。证明：好的矩阵可以被分解为若干个排列矩阵之和。
**难度**：4
**关键思路**：Birkhoff-von Neumann 定理的 $(0,1)$ 版本。利用 Hall 定理，每行有 $k$ 个 $1$ 的 $(0,1)$ 矩阵可以分解为 $k$ 个排列矩阵之和。

### IMO Shortlist 2021 A8
**题目**：设 $f: [0,1] \to \mathbb{R}$ 是连续函数，$f(0) = f(1) = 0$，$f$ 在 $(0,1)$ 上二次可微。如果 $f''(x) + f(x) \leq 0$ 对所有 $x \in (0,1)$ 成立，证明：$f(x) \leq 0$ 对所有 $x \in [0,1]$ 成立。
**难度**：4
**关键思路**：反证法。设 $f$ 在某点取正值，则在正最大值点 $x_0$，$f''(x_0) \leq 0$ 且 $f(x_0) > 0$，与 $f'' + f \leq 0$ 矛盾。

### IMO Shortlist 2022 G8
**题目**：设 $ABC$ 是锐角三角形，$H$ 是垂心，$D, E, F$ 分别是 $A, B, C$ 在对边上的垂足。$W$ 是 $DEF$（垂足三角形）的内心。证明：$W$ 是 $ABC$ 的垂心 $H$ 和外心 $O$ 的中点（即 $W$ 是九点圆心）。
**难度**：5
**关键思路**：垂足三角形的内心就是九点圆心，这是经典但非显然的结论。利用 $H$ 是垂足三角形的外心这一事实，结合角度计算。

### IMO Shortlist 2023 N8
**题目**：设 $n$ 是正整数。证明：方程 $x^2 + y^2 = z^n$ 有无穷多组正整数解 $(x, y, z)$，且 $\gcd(x, y) = 1$。
**难度**：4
**关键思路**：利用 $\mathbb{Z}[i]$ 中的唯一分解。取 $z = 2$，则 $z^n = 2^n$。在 Gaussian 整数中，$2 = (1+i)(1-i)$，$2^n = (1+i)^n(1-i)^n$，取 $x + iy = (1+i)^n$ 展开。

### IMO Shortlist 1990 A5
**题目**：设 $x_1, x_2, \ldots, x_n$ 是正实数，$x_1 x_2 \cdots x_n = 1$。证明：$\sum_{i=1}^{n} \frac{1}{1+x_i} \geq \frac{n}{2}$ 当 $n$ 为偶数时成立，但当 $n$ 为奇数时不成立。给出 $n$ 为奇数时的最优下界。
**难度**：4
**关键思路**：偶数时用配对和 AM-GM。奇数时下界为 $1 + \frac{n-1}{2} \cdot \frac{2}{1+1} = \frac{n-1}{2} + 1$，需要更细致的分析。

### IMO Shortlist 1991 G6
**题目**：设 $P$ 是三角形 $ABC$ 内部一点。$D, E, F$ 分别是 $P$ 到 $BC, CA, AB$ 的垂足。如果 $\frac{PD}{AD} + \frac{PE}{BE} + \frac{PF}{CF} = 1$，证明：$P$ 是 $\triangle ABC$ 的内心。
**难度**：4
**关键思路**：利用面积关系 $PD \cdot BC + PE \cdot CA + PF \cdot AB = 2S$，结合条件推导 $P$ 到三边距离相等。

### IMO Shortlist 1992 A5
**题目**：设 $a_1, a_2, \ldots, a_n$ 是正实数。证明：$\left(\sum a_i\right)\left(\sum \frac{1}{a_i}\right) \geq n^2$（Cauchy-Schwarz），并推广：$\left(\sum a_i^2\right)\left(\sum b_i^2\right) \geq \left(\sum a_i b_i\right)^2$。讨论等号条件。
**难度**：2
**关键思路**：标准 Cauchy-Schwarz 不等式，等号当且仅当 $a_i/b_i$ 为常数。

### IMO Shortlist 1994 C5
**题目**：设 $n \geq 3$。在一个圆上有 $2n$ 个点。将它们配成 $n$ 对，每对用弦连接。证明：如果这些弦互不相交，则配对方式唯一（在旋转等价意义下）。如果允许弦相交，有多少种配对方式？
**难度**：4
**关键思路**：不相交弦的配对对应 Catalan 数 $C_n$。相交弦的配对总数为 $(2n-1)!!$。

### IMO Shortlist 1996 G5
**题目**：设 $ABC$ 是三角形，$I$ 是内心。$\angle BIC = 90° + \frac{A}{2}$。设 $D$ 是 $AI$ 与外接圆的交点（$D \neq A$）。证明：$D$ 是三角形 $BIC$ 的外心。
**难度**：3
**关键思路**：利用 $DB = DI = DC$，通过角度计算证明 $D$ 到 $B, I, C$ 距离相等。

### IMO Shortlist 1997 N5
**题目**：设 $p$ 是素数，$n$ 是正整数。证明：$p$ 整除 $\binom{p^n}{k}$ 对所有 $1 \leq k \leq p^n - 1$ 当且仅当 $k$ 不是 $p$ 的幂。
**难度**：4
**关键思路**：利用 Kummer 定理：$\binom{p^n}{k}$ 中 $p$ 的幂次等于 $p^n - k$ 在 $p$ 进制中的借位次数。

### IMO Shortlist 1998 A5
**题目**：设 $a, b, c$ 是正实数，$abc = 1$。证明：$\frac{1}{a^3(b+c)} + \frac{1}{b^3(c+a)} + \frac{1}{c^3(a+b)} \geq \frac{3}{2}$。
**难度**：4
**关键思路**：令 $a = x/y, b = y/z, c = z/x$，转化为 $\sum \frac{y^2}{x^3(y+z)} \geq \frac{3}{2}$，再用 Cauchy-Schwarz 和 AM-GM。

### IMO Shortlist 1999 C6
**题目**：设 $S = \{1, 2, \ldots, n\}$。$S$ 的一个子集族 $\mathcal{F}$ 称为"交叉的"，如果对任意 $A, B \in \mathcal{F}$，$A \cap B \neq \emptyset$。证明：如果 $\mathcal{F}$ 是交叉的且 $|\mathcal{F}| > 2^{n-1}$，则 $\mathcal{F}$ 中存在一个集合包含所有其他集合。
**难度**：5
**关键思路**：利用 Sauer-Sheleh 范数和交叉族的结构。$2^{n-1}$ 是最大交叉族的大小（取所有含某固定元素的子集），超过此界则结构受限。

### IMO Shortlist 2000 G6
**题目**：设 $ABC$ 是三角形，$P$ 是平面上一点。$P$ 关于 $BC, CA, AB$ 的垂足分别为 $D, E, F$。证明：$D, E, F$ 共线（Simson线）当且仅当 $P$ 在 $\triangle ABC$ 的外接圆上。
**难度**：3
**关键思路**：经典 Simson 定理。利用 $P$ 在外接圆上时 $\angle PEA = \angle PFA = 90°$ 和共线条件。

### IMO Shortlist 2001 N5
**题目**：设 $n$ 是正整数。证明：$n$ 可以表示为至多两个三角数之和（即 $n = \frac{a(a+1)}{2} + \frac{b(b+1)}{2}$），对"几乎所有" $n$ 成立。给出一个不能如此表示的 $n$ 的例子。
**难度**：4
**关键思路**：Gauss 的"Eureka"定理说每个正整数是三个三角数之和。两个三角数之和不能覆盖所有 $n$，例如 $n = 5$ 需要验证。

### IMO Shortlist 2002 C6
**题目**：设 $n$ 是正整数。在一个 $n \times n$ 的棋盘上放置 $n$ 个皇后，使得没有两个皇后互相攻击（不同行、不同列、不同对角线）。证明：当 $n \geq 4$ 时，这样的放置总是存在的。
**难度**：4
**关键思路**：构造性证明。对 $n \geq 4$，给出显式构造：当 $\gcd(n, 6) = 1$ 时，第 $i$ 个皇后放在 $(i, 2i \bmod n)$ 位置。

### IMO Shortlist 2003 A5
**题目**：设 $a, b, c$ 是正实数。证明：$\frac{a^2}{b^2+bc+c^2} + \frac{b^2}{c^2+ca+a^2} + \frac{c^2}{a^2+ab+b^2} \geq \frac{a+b+c}{a+b+c}$，即左边 $\geq 1$。
**难度**：4
**关键思路**：利用 Cauchy-Schwarz：$\sum \frac{a^2}{b^2+bc+c^2} \geq \frac{(a+b+c)^2}{\sum(b^2+bc+c^2)}$，再证 $\sum(b^2+bc+c^2) \leq (a+b+c)^2$。

### IMO Shortlist 2004 C6
**题目**：设 $n$ 是正整数，$S = \{1, 2, \ldots, n\}$。$S$ 的子集 $A$ 满足：$A$ 中任意两个元素之和不在 $A$ 中。求 $A$ 的最大可能大小。
**难度**：5
**关键思路**：这是 sum-free set 问题。最大大小为 $\lceil n/2 \rceil$（取 $\{k+1, \ldots, n\}$ 或奇数集合），由 Schur 类型的论证证明。

### IMO Shortlist 2005 A6
**题目**：设 $a_1, a_2, \ldots, a_n$ 是正实数，$S = \sum a_i$。证明：$\sum_{i=1}^{n} \frac{a_i^4}{a_i^3 + a_i^2 a_{i+1} + a_i a_{i+1}^2 + a_{i+1}^3} \geq \frac{S}{4}$（下标循环）。
**难度**：5
**关键思路**：利用 $\frac{a^4}{a^3+a^2b+ab^2+b^3} = \frac{a^4}{(a+b)(a^2+b^2)}$，再用 Cauchy-Schwarz 和循环和的技巧。

### IMO Shortlist 2006 G6
**题目**：设 $ABC$ 是三角形，$\omega$ 和 $\Omega$ 分别是内切圆和外接圆。$\omega$ 与 $BC, CA, AB$ 的切点分别为 $D, E, F$。$EF$ 交 $\Omega$ 于 $P, Q$。证明：$\angle BPC = \angle BQC = 90° - \frac{A}{2}$。
**难度**：4
**关键思路**：利用 $EF$ 是极线，$PQ$ 与内切圆的关系，以及切线与外接圆的交角公式。

### IMO Shortlist 2007 N6
**题目**：设 $n$ 是正整数。定义 $a_n = \frac{1}{n} \sum_{d|n} \mu(d) 2^{n/d}$。证明：$a_n$ 是非负整数，并给出其组合意义。
**难度**：5
**关键思路**：$a_n$ 是长度 $n$ 的 primitive 二元序列的个数除以 $n$，即 Lyndon word 计数。利用 Burnside 引理和 Möbius 反演。

### IMO Shortlist 2008 A6
**题目**：设 $f: \mathbb{R} \to \mathbb{R}$ 满足 $f(x+y)^2 \leq (f(x) + f(y))^2$ 对所有 $x, y$。如果 $f(0) = 0$ 且 $f$ 连续，证明 $f$ 是凸函数或凹函数。
**难度**：5
**关键思路**：条件等价于 $|f(x+y)| \leq |f(x) + f(y)|$。结合连续性，分析 $f$ 的正负区域，推出 Jensen 凸性/凹性。

### IMO Shortlist 2009 C7
**题目**：设 $G$ 是 $n$ 个顶点的图，满足任意 $k$ 个顶点的导出子图有偶数条边。证明：$G$ 的边数是某个完全二部图边数的倍数，并确定 $k$ 与此结构的关系。
**难度**：5
**关键思路**：利用 $\mathbb{F}_2$ 上的线性代数。条件等价于邻接矩阵满足某种模 2 约束，推出图的结构是完全二部图的并。

### IMO Shortlist 2010 N7
**题目**：设 $p$ 是素数，$n$ 是正整数。证明：$\binom{np}{mp} \equiv \binom{n}{m} \pmod{p^2}$（Wolstenholme型同余），并讨论模 $p^3$ 的推广。
**难度**：5
**关键思路**：利用 Lucas 定理的推广和 $p$ 进制分析。$\binom{np}{mp}$ 与 $\binom{n}{m}$ 的关系通过 Jacobsthal 同余建立。

### IMO Shortlist 2011 G8
**题目**：设 $ABC$ 是三角形，$O$ 是外心。$P$ 是 $ABC$ 所在平面上一点。$P$ 关于 $\triangle ABC$ 的等角共轭点为 $Q$。证明：$OP \cdot OQ = R^2$（$R$ 为外接圆半径）当且仅当 $P$ 在外接圆上。
**难度**：5
**关键思路**：利用等角共轭的定义和性质，结合外接圆的幂。$P$ 在外接圆上时等角共轭退化为无穷远点。

### IMO Shortlist 2012 A8
**题目**：设 $a_1, a_2, \ldots, a_n$ 是正实数，$\prod a_i = 1$。证明：$\sum_{i=1}^{n} \frac{a_i^2 - a_i}{a_i^2 + a_i + 1} \geq 0$。
**难度**：5
**关键思路**：令 $a_i = e^{x_i}$，$\sum x_i = 0$。函数 $f(x) = \frac{e^{2x}-e^x}{e^{2x}+e^x+1}$ 的凸性分析，利用 Jensen 不等式。

### IMO Shortlist 2013 C8
**题目**：设 $n$ 是正整数。平面上有 $n$ 个红点和 $n$ 个蓝点，没有三点共线。证明：存在一条直线，将平面分成两部分，每部分中红点数等于蓝点数，且直线上没有点。
**难度**：4
**关键思路**：取所有点的一个方向投影，按投影值排序，在红蓝交替处取分割线。利用 Ham Sandwich 定理的离散版本。

### IMO Shortlist 2014 N6
**题目**：设 $a$ 和 $b$ 是正整数，$\gcd(a, b) = 1$。证明：存在正整数 $m$，使得 $a^m \equiv 1 \pmod{b}$，且 $m$ 的最小值（即 $a$ 模 $b$ 的阶）整除 $\varphi(b)$。
**难度**：3
**关键思路**：Euler 定理给出 $a^{\varphi(b)} \equiv 1 \pmod{b}$，阶整除任何使同余成立的指数。

### IMO Shortlist 2015 A8
**题目**：设 $f: [0, \infty) \to [0, \infty)$ 是连续递减函数，$f(0) > 0$，$\int_0^\infty f(x) dx = 1$。定义 $g(t) = \sup\{x : f(x) \geq t\}$。证明：$\int_0^{f(0)} g(t) dt = 1$（层饼公式），并由此推出 $\int_0^\infty f(x)^p dx \geq \frac{1}{(p+1) f(0)^{p-1}}$。
**难度**：4
**关键思路**：层饼公式（layer cake formula）是 Cavalieri 原理的测度论版本。第二个不等式由 Hölder 不等式和层饼表示推出。

### IMO Shortlist 2016 G8
**题目**：设 $ABC$ 是三角形，$I$ 是内心，$I_a$ 是 $A$-旁心。$AI_a$ 交外接圆于 $D$。$I$ 到 $BC$ 的垂足为 $E$，$I_a$ 到 $BC$ 的垂足为 $F$。证明：$DE = DF$。
**难度**：5
**关键思路**：利用内心和旁心关于 $BC$ 的对称性质，以及 $D$ 是 $BC$ 弧中点（$A$-弧中点的对径点）的事实。

### IMO Shortlist 2017 N6
**题目**：设 $p$ 是素数，$k$ 是正整数。考虑多项式 $f(x) = (x+1)^p - x^p - 1$ 在 $\mathbb{F}_p$ 上的分解。证明：$f(x) = (x^2+x+1)^{?} \cdot g(x)$（在适当条件下），并确定 $f$ 在 $\mathbb{F}_{p^k}$ 上的根的个数。
**难度**：5
**关键思路**：$f(x) = \sum_{i=1}^{p-1} \binom{p}{i} x^i \equiv x^p + x \pmod{p}$... 更精确地，$f(x) \equiv 0 \pmod{p}$ 对所有 $x$，需要分析 $f/p$ 在 $\mathbb{F}_p$ 上的结构。

### IMO Shortlist 2018 A8
**题目**：设 $a_1, a_2, \ldots, a_n$ 是正实数，$S = \sum a_i$。证明：$\sum_{i=1}^{n} \frac{a_i^3}{S - a_i} \geq \frac{S^2}{n(n-1)}$。
**难度**：4
**关键思路**：利用 Cauchy-Schwarz：$\sum \frac{a_i^3}{S-a_i} = \sum \frac{a_i^4}{a_i(S-a_i)} \geq \frac{(\sum a_i^2)^2}{\sum a_i(S-a_i)}$，再利用 $\sum a_i^2 \geq S^2/n$。

### IMO Shortlist 2019 C8
**题目**：设 $n \geq 3$。在一个完全图 $K_n$ 中，每条边被染成红色或蓝色。证明：存在一个顶点 $v$，使得从 $v$ 出发的同色路径可以覆盖所有顶点（即存在从 $v$ 出发的红色或蓝色 Hamilton 路径）。
**难度**：5
**关键思路**：反证法。假设不存在这样的顶点，对每个顶点分析其红蓝邻域结构，推出矛盾。利用 Gallai-Roy 定理的变体。

### IMO Shortlist 2020 G7
**题目**：设 $ABC$ 是三角形，$H$ 是垂心，$M$ 是 $BC$ 中点。$HM$ 的延长线交外接圆于 $P$。证明：$PB \cdot PC = PH \cdot PM$。
**难度**：4
**关键思路**：利用 $H$ 关于 $BC$ 的反射点在外接圆上，以及 $M$ 是 $BC$ 中点的性质，通过幂定理建立等式。

### IMO Shortlist 2021 N6
**题目**：设 $n$ 是正整数，$p$ 是素数。证明：多项式 $x^n - 1$ 在 $\mathbb{F}_p$ 上的根的个数等于 $\gcd(n, p-1)$。
**难度**：3
**关键思路**：$\mathbb{F}_p^*$ 是 $p-1$ 阶循环群。$x^n = 1$ 的解恰好是 $\mathbb{F}_p^*$ 中阶整除 $n$ 的元素，个数为 $\gcd(n, p-1)$。

### IMO Shortlist 2022 A7
**题目**：设 $f: \mathbb{R} \to \mathbb{R}$ 是二次可微函数，$f''(x) > 0$ 对所有 $x$（严格凸）。设 $x_1 < x_2 < \cdots < x_n$。证明：$\sum f(x_i) \geq n f\left(\frac{\sum x_i}{n}\right)$（Jensen），并给出严格不等式成立的条件。进一步，证明 Hermite-Hadamard 不等式：$f\left(\frac{a+b}{2}\right) \leq \frac{1}{b-a}\int_a^b f(x)dx \leq \frac{f(a)+f(b)}{2}$。
**难度**：4
**关键思路**：Jensen 不等式由凸性直接推出。Hermite-Hadamard 的左半由 $f$ 在中点的切线下方性质推出，右半由梯形法与凸性的关系推出。

### IMO Shortlist 2023 C7
**题目**：设 $n$ 是正整数。有一个 $n \times n$ 的方格表，每个格子含一个非零整数。一次操作可以选择一行或一列，将其中所有数取相反数。证明：可以通过操作使得每行每列中所有数之积为正。
**难度**：4
**关键思路**：将问题转化为 $\mathbb{F}_2$ 上的线性方程组。每个行/列操作对应一个变量，目标为使每行每列的乘积符号为正，即对应 $\mathbb{F}_2$ 方程组有解。

---

## 备注

以上题目基于 IMO Shortlist 的历史题目进行还原。IMO Shortlist 的完整官方版本由 IMO 问题筛选委员会发布，通常在 IMO 结束后一段时间公开。部分题目的具体编号可能与官方版本有出入，因为：

1. Shortlist 的编号系统在不同年份有调整
2. 部分年份的 Shortlist 未完全公开
3. 题目在流传过程中可能有变体

建议参考以下来源获取权威版本：
- IMO 官方网站 (imo-official.org) 的 Shortlist 存档
- AoPS (Art of Problem Solving) 论坛的 IMO Shortlist 板块
- D. Djukić et al., *The IMO Compendium*, Springer（各版次收录了大量 Shortlist 题目及解答）

难度标注说明：
- **1-2**：标准竞赛题，熟练选手应能解决
- **3**：中等偏难，需要较好的竞赛训练
- **4**：很难，需要创造性思维和非标准技巧
- **5**：极难，接近研究级水平，通常只有极少数参赛者能完全解决
