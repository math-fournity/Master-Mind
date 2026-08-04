# Sphere Packings, Lattices and Groups 核心内容

> 《Sphere Packings, Lattices and Groups》是 John Conway 和 Neil Sloane 合著的经典专著（1988年初版，1993年第二版，1999年第三版），通常简称 SPLAG。该书系统整理了球填充、格理论和相关群论的成果，是这一领域的"圣经"。Conway 和 Sloane 的工作为后来 Viazovska 在8维和24维的突破奠定了基础。

---

## 1. 球填充问题概述

### 1.1 问题陈述

**球填充问题**：在 $d$ 维欧氏空间 $\mathbb{R}^d$ 中，如何放置互不相交的单位球，使得填充密度最大？

**密度**：$\Delta = \lim_{R \to \infty} \frac{\text{球在半径 } R \text{ 球内的总体积}}{\text{半径 } R \text{ 球的体积}}$。

**格填充（lattice packing）**：球心构成一个格 $\Lambda$ 的填充。格填充密度为
$$\Delta(\Lambda) = \frac{\text{vol}(B^d)}{\text{vol}(\mathbb{R}^d/\Lambda)} = \frac{V_d}{\det(\Lambda)},$$
其中 $V_d$ 是单位球体积，$\det(\Lambda)$ 是格的基本域体积。

**一般填充**：球心不要求构成格，可以任意排列。一般填充密度 $\Delta_d \geq \Delta_d^{\text{lattice}}$。

### 1.2 已知结果

| 维数 | 最优密度 | 证明者 | 年份 |
|------|---------|--------|------|
| 1 | $1$ | 平凡 | — |
| 2 | $\frac{\pi}{2\sqrt{3}} \approx 0.9069$ | Gauss（猜想），Tóth（证明） | 1940 |
| 3 | $\frac{\pi}{3\sqrt{2}} \approx 0.7405$ | Hales（Kepler 猜想） | 1998/2014 |
| 8 | $\frac{\pi^4}{384} \approx 0.2537$ | Viazovska | 2016 |
| 24 | $\frac{\pi^{12}}{12!} \approx 0.00193$ | Viazovska 等 | 2016 |

其他维数中，最优填充密度未知，但许多维数有**最优格填充**的猜想。

### 1.3 相关问题

- **覆盖问题**：用球覆盖空间，最小化覆盖密度；
- **Kissing number**：一个球最多能"亲吻"（相切）多少个同维球？
- **Voronoi 单元**：格的 Voronoi 单元的几何；
- **格的密度上下界**：Minkowski 上界，Minkowski-Hlawka 下界。

---

## 2. E8 格

### 2.1 构造

**E8 格**是8维空间中最重要的格，与例外 Lie 代数 $E_8$ 密切相关。

**构造 1（根格）**：$E_8$ 根格由 $E_8$ 根系的 $\mathbb{Z}$-线性组合生成。$E_8$ 根系有 240 个根：
$$\Phi_{E_8} = \left\{ \pm e_i \pm e_j : i \neq j \right\} \cup \left\{ \frac{1}{2}(\pm e_1 \pm e_2 \pm \cdots \pm e_8) : \text{偶数个负号} \right\},$$
共 $112 + 128 = 240$ 个根。

**构造 2（偶坐标）**：
$$E_8 = \left\{ x \in \mathbb{Z}^8 \cup (\mathbb{Z}+\tfrac{1}{2})^8 : \sum x_i \in 2\mathbb{Z}, \, \text{所有 } x_i \text{ 同为整数或半整数} \right\}.$$

### 2.2 性质

- **偶格（even lattice）**：所有向量 $x \in E_8$ 满足 $(x,x) \in 2\mathbb{Z}$（范数为偶整数）；
- **自对偶（unimodular）**：$E_8^* = E_8$（对偶格等于自身），$\det(E_8) = 1$；
- **E8 是唯一的8维偶自对偶格**；
- **最小范数**：2（240 个最小向量，即 240 个根）；
- **Kissing number**：240（8维的最大 kissing number，由 Levenshtein 和 Odlyzko 独立证明）；
- **填充密度**：$\Delta(E_8) = \frac{\pi^4}{384} \approx 0.2537$。

### 2.3 E8 的对称群

$E_8$ 格的自同构群（保距变换群）是 **Weyl 群 $W(E_8)$**，阶为
$$|W(E_8)| = 2^{14} \cdot 3^5 \cdot 5^2 \cdot 7 = 696{,}729{,}600.$$

这是8维中最大的有限反射群。

### 2.4 Theta 函数

$E_8$ 格的 theta 函数是权 4 的模形式：
$$\Theta_{E_8}(\tau) = \sum_{x \in E_8} q^{(x,x)/2} = E_4(\tau) = 1 + 240q + 2160q^2 + \cdots,$$
其中 $E_4(\tau)$ 是 Eisenstein 级数。这个模形式性质是 Viazovska 证明的关键。

---

## 3. Leech 格

### 3.1 构造

**Leech 格** $\Lambda_{24}$ 是24维空间中最著名的格，由 John Leech（1967）发现。

**构造（基于 Golay 码）**：利用**二元 Golay 码**（$[24, 12, 8]$ 码）构造：
$$\Lambda_{24} = \frac{1}{\sqrt{2}} \left\{ \text{特定规则下的 } \mathbb{Z}^{24} \text{ 和半整数向量} \right\}.$$

具体地，Leech 格可以通过以下方式构造：
1. 取 $\mathbb{R}^{24}$ 中的向量，坐标全为整数或全为半整数；
2. 整数向量：坐标之和为偶数，且模 2 的模式属于 Golay 码；
3. 半整数向量：坐标之和为偶数，且模 2 的模式属于 Golay 码的陪集。

### 3.2 性质

- **偶格**：所有 $(x,x) \in 2\mathbb{Z}$；
- **自对偶**：$\Lambda_{24}^* = \Lambda_{24}$，$\det = 1$；
- **Leech 格是唯一的24维偶自对偶无向量格（even unimodular lattice with no vectors of norm 2）**；
- **最小范数**：4（196560 个最小向量）；
- **Kissing number**：196560（24维的最大 kissing number，由 Levenshtein 和 Odlyzko 证明）；
- **填充密度**：$\Delta(\Lambda_{24}) = \frac{\pi^{12}}{12!} \approx 0.00193$。

### 3.3 Leech 格的对称群

Leech 格的自同构群 $Co_0 = \text{Aut}(\Lambda_{24})$（Conway 群），阶为
$$|Co_0| = 2^{22} \cdot 3^9 \cdot 5^4 \cdot 7^2 \cdot 11 \cdot 13 \cdot 23 \approx 8.3 \times 10^{18}.$$

其商群 $Co_1 = Co_0 / \{\pm 1\}$ 是**散在单群（sporadic simple group）**之一——**Conway 群 $Co_1$**。此外还有 $Co_2, Co_3$ 等子群。

**Conway 的贡献**：Conway 在研究 Leech 格的对称性时发现了这些散在单群，这是有限单群分类的重要部分。

### 3.4 Theta 函数

Leech 格的 theta 函数是权 12 的模形式：
$$\Theta_{\Lambda_{24}}(\tau) = E_{12}(\tau) - \frac{432000}{691} \Delta(\tau) = 1 + 196560q^2 + 16773120q^3 + \cdots,$$
其中 $E_{12}$ 是 Eisenstein 级数，$\Delta(\tau) = \eta(\tau)^{24}$ 是判别式模形式。

注意：$\Theta_{\Lambda_{24}}$ 的 $q^1$ 系数为 0（无范数 2 的向量），这是 Leech 格的特征性质。

---

## 4. Conway-Sloane 的工作

### 4.1 SPLAG 的核心内容

SPLAG 系统整理了：

1. **格的分类和构造**：
   - 低维格的分类（1-8维）；
   - 重要格的构造（$E_8$, $\Lambda_{24}$, Barnes-Wall 格等）；
   - 根格 $A_n, D_n, E_6, E_7, E_8$ 的详细研究。

2. **球填充和覆盖**：
   - 各维数的最优格填充；
   - Minkowski 理论和几何数论；
   - 覆盖密度和 Voronoi 单元。

3. **Kissing number**：
   - 各维数的 kissing number；
   - 与格的最小向量的关系。

4. **码与格的联系**：
   - 编码理论中的码与格的对应；
   - Golay 码与 Leech 格；
   - Reed-Muller 码与 Barnes-Wall 格。

5. **群论**：
   - 格的自同构群；
   - Conway 群、Monster 群等散在单群；
   - Moonshine 现象。

### 4.2 重要概念

**壳层（Shell）**：格中范数为 $2n$ 的向量集合。$E_8$ 和 $\Lambda_{24}$ 的壳层结构极其丰富，与有限群、设计理论等有深刻联系。

**设计（Design）**：Leech 格的壳层支撑了**组合设计**——例如，196560 个最小向量在适当投影下给出 5-$(24, 8, 1)$ 设计（Witt 设计）。

**Magic configurations**：Conway-Sloane 研究了格中的特殊构型，如"深洞（deep holes）"和"浅洞（shallow holes）"。

### 4.3 Conway-Sloane 的具体贡献

1. **深洞理论**：Conway-Sloane 证明了 Leech 格的深洞恰好对应于**Niemeier 格**（24维的其余23个偶自对偶格），建立了 Leech 格与其他 Niemeier 格的深刻联系。

2. **格的层（layers）**：系统研究了格的层结构和壳层计数。

3. **Voronoi 单元**：研究了重要格的 Voronoi 单元几何。

4. **低维格的分类**：整理了低维（特别是 $d \leq 8$）的最优格。

---

## 5. 与 Viazovska 工作的联系

### 5.1 Viazovska 的突破

2016年，Viazovska（以及合作者 Cohn, Kumar, Miller, Radchenko）证明了 $E_8$（8维）和 $\Lambda_{24}$（24维）是**最优球填充**——不仅是最优格填充，而是所有填充中的最优。

### 5.2 关键联系

Viazovska 的证明**直接依赖于 $E_8$ 和 $\Lambda_{24}$ 的模形式性质**，而这些性质在 SPLAG 中有详细记录：

1. **Theta 函数作为模形式**：$E_8$ 的 theta 函数是 $E_4$（权 4），$\Lambda_{24}$ 的 theta 函数是权 12 模形式。这些是 Viazovska 构造最优 Cohn-Elkies 函数的输入。

2. **偶自对偶性**：$E_8$ 和 $\Lambda_{24}$ 是偶自对偶格，这保证了它们的 theta 函数是 $SL_2(\mathbb{Z})$ 的模形式（而非子群）。这是8维和24维"特殊"的根源。

3. **最小向量**：240（$E_8$）和 196560（$\Lambda_{24}$）个最小向量的结构在 Viazovska 的插值构造中起关键作用。

### 5.3 SPLAG 的奠基作用

SPLAG 为 Viazovska 的工作提供了：
- **格的完整描述**：$E_8$ 和 $\Lambda_{24}$ 的构造、性质、theta 函数；
- **模形式联系**：theta 函数与模形式的关系在 SPLAG 中有记录；
- **直觉和背景**：SPLAG 中关于8维和24维"特殊性"的大量证据（kissing number 的最优性、深洞理论等）为 Viazovska 的突破提供了方向。

### 5.4 Cohn-Elkies 上界

Cohn-Elkies（2001）的傅里叶上界方法在 $d=8, 24$ 中给出的数值上界与 $E_8$, $\Lambda_{24}$ 的密度吻合到15位有效数字。SPLAG 中记录的这些格的性质使得 Viazovska 能够**精确构造**达到此上界的函数。

---

## 6. 其他重要格

### 6.1 Barnes-Wall 格

$BW_{16}$（16维）等，与 Reed-Muller 码相关。

### 6.2 Niemeier 格

24维的**24个偶自对偶格**（Niemeier 格），其中 23 个有根（最小范数 2），只有 Leech 格无根。Conway-Sloane 的深洞理论将它们统一。

### 6.3 Coxeter-Todd 格

$K_{12}$（12维），与复反射群相关。

### 6.4 laminated 格

$\Lambda_d$（$d$ 维 laminated 格），通过"层叠"构造，在低维中给出最优格填充。

---

## 参考文献

- Conway, Sloane. *Sphere Packings, Lattices and Groups*. Springer, 3rd ed., 1999. (GTM 290)
- Leech. *Notes on sphere packings*. Canadian J. Math., 1967.
- Cohn, Elkies. *New upper bounds on sphere packings I*. Annals of Math., 2003.
- Viazovska. *The sphere packing problem in dimension 8*. Annals of Math., 2017.
- Cohn, Kumar, Miller, Radchenko, Viazovska. *The sphere packing problem in dimension 24*. Annals of Math., 2017.
- Thompson. *Finite groups of sphere packings*. 1983.
- Ebeling. *Lattices and Codes*. Vieweg, 2002.
