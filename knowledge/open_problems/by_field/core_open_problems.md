# 各数学领域核心开放问题

本文档按数学领域分类，列出每个领域最重要的5-10个开放问题。这些问题代表了当前数学研究的前沿边界——"什么是不知道的"。

---

## 一、代数 / 代数几何

### 1.1 Jacobian 猜想
**陈述**：设 $F: \mathbb{C}^n \to \mathbb{C}^n$ 是多项式映射，且 Jacobi 行列式 $\det(DF)$ 处处非零（常数）。则 $F$ 是否可逆（即存在多项式逆映射）？
**状态**：开放（$n \geq 2$）
**关键进展**：Keller (1939) 提出。对 $n=1$ 平凡。对 $n=2$ 有大量部分结果但未完全解决。Bass-Connell-Wright, Meng 等有重要贡献。被认为"看似简单实则极难"。

### 1.2 逆 Galois 问题
**陈述**：每个有限群是否都是 $\mathbb{Q}$ 上某个 Galois 扩张的 Galois 群？
**状态**：开放
**关键进展**：Hilbert (1892) 证明对称群和交错群。Shafarevich (1954) 证明所有可解群。Ihara, Mestre 等用模曲线方法证明许多单群。大多数单群已处理，但一般情形仍开放。

### 1.3 ABC 猜想
**陈述**：设 $a + b = c$，$\gcd(a,b) = 1$。则对任意 $\epsilon > 0$，存在 $C_\epsilon$ 使得 $c \leq C_\epsilon \cdot \text{rad}(abc)^{1+\epsilon}$。其中 $\text{rad}(n)$ 为 $n$ 的不同素因子之积。
**状态**：争议中（Mochizuki 声称证明）
**关键进展**：Oesterlé-Masser (1988) 提出。Mochizuki (2012) 发表四篇论文声称证明（Inter-universal Teichmüller Theory），但未被数学界广泛接受。2021年发表于 PRIMS 但仍有争议。若成立则蕴含 Fermat 大定理的简洁证明、Mordell 猜想的另一证明等。

### 1.4 标准猜想 (Grothendieck)
**陈述**：Grothendieck (1968) 提出关于代数闭链和上同调的六个标准猜想，涉及 Lefschetz 型算子的代数性、Hodge 猜想的变体等。
**状态**：开放
**关键进展**：与 Hodge 猜想、Tate 猜想密切相关。对有限域上的簇，标准猜想蕴含 Tate 猜想。在 Abelian 簇上有部分进展（Milne, Murty 等）。

### 1.5 Tate 猜想
**陈述**：对有限域 $\mathbb{F}_q$ 上的光滑射影簇 $X$，$l$-进上同调 $H^{2k}(X_{\bar{\mathbb{F}}_q}, \mathbb{Q}_l(k))$ 中 Frobenius 不动部分等于代数闭链类张量 $\mathbb{Q}_l$ 生成的子空间。
**状态**：开放
**关键进展**：Tate (1965) 提出。与 Hodge 猜想的有限域类比。对乘积簇、Abel 簇等有部分结果。Tate-Thomason 证明与 K-理论的 Bloch-Beilinson 猜想相关。

### 1.6 Langlands 纲领（一般情形）
**陈述**：自守表示与 Galois 表示之间的对应关系（函子性原理和 reciprocity）。一般地，每个 $n$ 维 Galois 表示是否对应某个自守表示？
**状态**：部分解决
**关键进展**：Langlands (1967) 提出纲领。Wiles (1995) 证明椭圆曲线的模性（$n=2$ 情形的关键部分）。Drinfeld (1980s), Lafforgue (2002, Fields Medal) 证明函数域上的 GL_n Langlands 对应。数域上 GL_n 的一般情形仍开放。Frenkel-Gaitsgory-Vilonen 等在几何 Langlands 方面有重大进展。

### 1.7 Birch-Swinnerton-Dyer 猜想（高秩情形）
**陈述**：见千禧年问题。BSD 猜想对解析秩 $\geq 2$ 的情形。
**状态**：开放
**关键进展**：秩 $\leq 1$ 已证（Kolyvagin, Gross-Zagier）。高秩情形几乎完全开放——甚至没有已知方法可以处理。

### 1.8 Bloch-Beilinson 猜想
**陈述**：代数簇的 Chow 群和高阶 K-群与 L-函数的特殊值之间的关系。具体地，Chow 群 $\text{CH}^k(X) \otimes \mathbb{Q}$ 的秩由 $L$-函数在特定点的零点阶数决定。
**状态**：开放
**关键进展**：Bloch (1976), Beilinson (1984) 提出一般框架。与 BSD 猜想、Hodge 猜想、Tate 猜想构成统一的猜想体系。仅有零散验证。

---

## 二、数论

### 2.1 Riemann 假设
**陈述**：见千禧年问题。$\zeta(s)$ 的非平凡零点均在 $\text{Re}(s) = 1/2$。
**状态**：开放
**关键进展**：见千禧年问题文档。

### 2.2 广义 Riemann 假设 (GRH)
**陈述**：所有 Dirichlet L-函数（及更一般的 Dedekind zeta 函数、Artin L-函数）的非平凡零点均在临界线上。
**状态**：开放
**关键进展**：与 RH 类似的部分结果。若 GRH 成立则大量数论算法可加速（如素性判定、类群计算）。

### 2.3 孪生素数猜想
**陈述**：存在无穷多对素数 $p, p+2$。
**状态**：部分解决
**关键进展**：Zhang (2013) 证明 $\liminf(p_{n+1}-p_n) < 7\times10^7$。Maynard-Tao 改进到 $\leq 246$。完整猜想（差为2）仍开放。

### 2.4 Goldbach 猜想
**陈述**：每个大于2的偶数是两个素数之和（强 Goldbach）。每个大于5的奇数是三个素数之和（弱 Goldbach）。
**状态**：弱 Goldbach 已解决，强 Goldbach 开放
**关键进展**：Vinogradov (1937) 证明弱 Goldbach 对充分大奇数成立。Helfgott (2013) 完全证明弱 Goldbach。强 Goldbach 已验证到 $4 \times 10^{18}$，但证明仍开放。Chen (1973) 证明每个充分大偶数是 $p + P_2$（$P_2$ 为至多2个素因子之积）。

### 2.5 素数间距上界 / Cramér 猜想
**陈述**：$p_{n+1} - p_n = O(\log^2 p_n)$（Cramér 猜想）。更精确地，$\limsup \frac{p_{n+1}-p_n}{\log^2 p_n} = 1$？
**状态**：开放
**关键进展**：Baker-Harman-Pintz (2001) 证明 $p_{n+1}-p_n = O(p_n^{0.525})$。Ford-Green-Konyagin-Maynard-Tao (2016) 大幅改进 $\limsup$ 的下界。Cramér 猜想本身远未达到。

### 2.6 $n^2+1$ 素数猜想 (Landau 第四问题)
**陈述**：存在无穷多形如 $n^2+1$ 的素数。
**状态**：开放
**关键进展**：Iwaniec (1978) 证明有无穷多 $n^2+1$ 至多有2个素因子。一般 Bunyakovsky 猜想/Schinzel H 猜想仍开放。

### 2.7 Collatz 猜想 (3n+1 问题)
**陈述**：对任意正整数 $n$，反复应用 $f(n) = n/2$（$n$ 偶）或 $f(n) = 3n+1$（$n$ 奇），最终到达1。
**状态**：开放
**关键进展**：已验证到 $2^{68}$（约 $2.95 \times 10^{20}$）。Tao (2019) 证明"几乎所有"初始值的轨道最终远小于初始值（弱化版本）。完整证明可能需要全新的数论工具。

### 2.8 abc 猜想
**陈述**：见代数几何部分。
**状态**：争议中
**关键进展**：Mochizuki 的 IUT 理论。

### 2.9 虚部为零的 Dirichlet L-函数
**陈述**：是否存在 Dirichlet L-函数 $L(s, \chi)$ 在 $s = 1/2$ 处有 Siegel 零点？
**状态**：开放
**关键进展**：Siegel 零点的存在性影响大量数论结果。若不存在 Siegel 零点，则许多结果可以无条件化。Goldfeld, Gross-Zagier 的工作与此相关。

### 2.10 类数问题
**陈述**：虚二次域 $\mathbb{Q}(\sqrt{-d})$ 的类数 $h(-d)$ 的分布。Gauss 类数猜想：对每个 $h$，只有有限多 $d$ 使 $h(-d) = h$。
**状态**：已解决
**关键进展**：Goldfeld (1976), Gross-Zagier (1983) 给出有效下界。Heegner (1952), Stark (1967) 解决 $h=1$ 的情形。Baker-Stark 解决 $h=2$。一般情形由 Goldfeld-Gross-Zagier 的方法解决。

---

## 三、分析 / PDE

### 3.1 Navier-Stokes 全局正则性
**陈述**：见千禧年问题。
**状态**：开放

### 3.2 Euler 方程的全局正则性
**陈述**：三维 Euler 方程对光滑初始数据是否存在全局光滑解？或是否存在有限时间爆破解？
**状态**：开放
**关键进展**：二维全局存在。三维：Kiselev-Sverák (2014) 构造梯度爆解。Elgindi (2019+) 构造 $C^\alpha$ 初值的爆破解。光滑初值的爆破仍开放。

### 3.3 Yang-Mills 方程的全局适定性
**陈述**：四维 Yang-Mills 方程的全局适定性（经典解的存在性和唯一性）。
**状态**：部分解决
**关键进展**：Uhlenbeck (1982), Taubes 等的工作。与千禧年 Yang-Mills 质量间隙问题相关。

### 3.4 KdV 和非线性 Schrödinger 方程的长时间行为
**陈述**：非线性色散方程的解的长时间渐近行为。Soliton 分解猜想。
**状态**：部分解决
**关键进展**：Deift-Zhou (1993) 的非线性驻相法。Inverse scattering 的严格化。对 KdV 有完整理论。一般 NLS 的 soliton 分解仍部分开放。

### 3.5 Schrödinger 方程的 Strichartz 估计最优性
**陈述**：Strichartz 估计中的端点情形是否成立？最优常数如何？
**状态**：部分解决
**关键进展**：Keel-Tao (1998) 给出端点估计的完整理论。某些临界情形仍开放。

### 3.6 椭圆方程的正则性
**陈述**：非散度型椭圆方程 $a^{ij}(x) \partial_{ij} u = f$ 的解的正则性。$C^{1,\alpha}$ 正则性是否成立？
**状态**：部分解决
**关键进展**：De Giorgi (1957), Nash (1958) 证明 $C^\alpha$ 正则性。Nirenberg, Krylov-Safonov 等推广。$C^{1,\alpha}$ 的精确范围仍部分开放。

### 3.7 Monge-Ampère 方程的正则性
**陈述**：Monge-Ampère 方程 $\det(D^2 u) = f$ 的解的正则性。光滑解的存在条件？
**状态**：部分解决
**关键进展**：Caffarelli (1990s) 的正则性理论。De Philippis-Figalli-Savin 等的近期工作。$W^{2,1}$ 估计等。

### 3.8 波动方程的散射
**陈述**：非线性波动方程的散射（解在 $t \to \infty$ 时趋近自由解）的条件。
**状态**：部分解决
**关键进展**：Morawetz 估计。Kenig-Merle (2006-2008) 的 concentration-compactness/rigidity 方法。对3D cubic NLS 等有完整散射理论。

---

## 四、拓扑

### 4.1 4维光滑 Poincaré 猜想
**陈述**：见 Smale 问题 S3。同伦4维球面是否微分同胚于 $S^4$？
**状态**：开放
**关键进展**：Freedman (1982) 证明拓扑版本。光滑版本完全开放。Donaldson, Seiberg-Witten 不变量未能区分。

### 4.2 4维流形的光滑分类
**陈述**：4维光滑流形的完整分类。
**状态**：开放
**关键进展**：Donaldson (1983), Seiberg-Witten (1994) 不变量。Freedman 的拓扑分类。光滑分类远未完成——甚至 $\mathbb{R}^4$ 有不可数多光滑结构。

### 4.3 光滑结构的存在性
**陈述**：哪些拓扑4维流形允许光滑结构？哪些不允许？
**状态**：部分解决
**关键进展**：Freedman 的 E8 流形不允许光滑结构（Donaldson）。Rohlin 定理的约束。许多4维流形的光滑结构问题仍开放。

### 4.4 纽结的完整分类
**陈述**：是否存在完整的纽结不变量（能区分所有不同纽结）？
**状态**：开放
**关键进展**：Jones 多项式 (1984), HOMFLY, Khovanov 同调 (2000) 都不能完全区分。Vassiliev 不变量。量子不变量。完整分类仍开放。

### 4.5 高维流形的分类
**陈述**：$n \geq 5$ 维紧致流形的分类（surgery 理论的完整实现）。
**状态**：部分解决
**关键进展**：Smale, Wall, Kirby-Siebenmann 的 surgery 理论。分类在原则上可计算但实际极其复杂。L-群的计算（Novikov 等）。

### 4.6 虚 Hodge-Tate 猜想 / p-adic Hodge 理论
**陈述**：$p$-进表示的 Hodge-Tate 分解的推广。
**状态**：部分解决
**关键进展**：Faltings (1980s), Fontaine 等建立 $p$-adic Hodge 理论。与代数拓扑的深联系。

### 4.7 同伦群的计算
**陈述**：球面同伦群 $\pi_k(S^n)$ 的完整计算。
**状态**：部分解决
**关键进展**：Serre, Toda, Ravenel 等的系统计算。稳定同伦群通过 Adams 谱序列、Adams-Novikov 谱序列计算。已知到约100维。一般计算极其困难。

### 4.8 稳定同伦群的模式
**陈述**：球面稳定同伦群的模式（如 chromatic filtration）的完整理解。
**状态**：部分解决
**关键进展**：Ravenel 猜想（部分由 Devinatz-Hopkins-Smith 证明）。Chromatic 同伦论。Morava K-理论。一般模式仍部分开放。

---

## 五、几何

### 5.1 Willmore 猜想
**陈述**：$\mathbb{R}^3$ 中亏格1的紧致曲面的 Willmore 能量 $\int H^2 dA \geq 2\pi^2$？Clifford 环面达到最小值。
**状态**：**已解决**（2012）
**关键进展**：Marques-Neves (2012) 用 min-max 方法证明。这是近年来几何测度论的重大成就。

### 5.2 Lawson 猜想
**陈述**：$S^3$ 中极小嵌入环面是否等距于 Clifford 环面？
**状态**：**已解决**（2012）
**关键进展**：Brendle (2012) 证明。与 Willmore 猜想相关。

### 5.3 Yau 猜想（极小超曲面）
**陈述**：每个紧致黎曼流形是否包含无穷多嵌入极小超曲面？
**状态**：**已解决**（2017-2018）
**关键进展**：Marques-Neves (2017) 用 min-max 方法证明（维度 $\geq 3$）。Song (2018) 处理二维情形。

### 5.4 Ricci 流的收敛性
**陈述**：Ricci 流在哪些条件下收敛到 Ricci 平坦度量或 Einstein 度量？
**状态**：部分解决
**关键进展**：Hamilton, Perelman 的工作。Bamler (2017+) 的近期突破——Ricci 流在非塌缩条件下的收敛性。

### 5.5 均值曲率流的奇性
**陈述**：均值曲率流的奇性分类。哪些奇性可以手术后继续流动？
**状态**：部分解决
**关键进展**：Huisken, Colding-Minicozzi 的工作。奇性分类（Type I, Type II）。Brendle-Huisken 的某些情形。完整手术理论仍开放。

### 5.6 Kähler-Ricci 流
**陈述**：Kähler-Ricci 流的全局收敛性。在 Fano 流形上的收敛条件。
**状态**：部分解决
**关键进展**：Cao (1992), Tian-Zhu, Phong-Song-Sturm 等。Perelman 的工作。Fano 情形与 K-稳定性的联系（Tian, Donaldson）。

### 5.7 SYZ 猜想 (Strominger-Yau-Zaslow)
**陈述**：Calabi-Yau 流形的镜像对称可以通过特殊 Lagrangian 环面纤维（Toric 对偶）来解释。
**状态**：部分解决
**关键进展**：SYZ (1996) 提出。Gross-Wilson, Ruan, Castaño-Bernard-Matessi 等的部分验证。完整严格证明仍开放。与镜像对称的数学基础相关。

### 5.8 Penrose 不等式
**陈述**：渐近平直 Riemannian 3-流形中，ADM 质量 $m \geq \sqrt{A/16\pi}$，其中 $A$ 为外视界面积。
**状态**：**已解决**（Riemannian 情形）
**关键进展**：Huisken-Ilmanen (2001) 证明单连通情形。Bray (2001) 证明一般情形。Lorentzian 情形（原始 Penrose 猜想）仍开放。

### 5.9 正质量定理的高维推广
**陈述**：正质量定理在所有维度的证明。
**状态**：已解决
**关键进展**：Schoen-Yau (1979) 在 $n \leq 7$ 证明。Witten (1981) 用旋量方法证明（所有维度，spin 情形）。最近 Schoen-Yau (2017) 推广到所有维度。

### 5.10 弱 Pinching 猜想
**陈述**：截面曲率满足 $0 < K_{\min} \geq \delta K_{\max}$（$\delta$ 依赖维数）的紧致流形是否微分同胚于球面？
**状态**：部分解决
**关键进展**：球面定理（Rauch-Berger-Klingenberg）：$\delta = 1/4$ 蕴含同胚于球面或 RP^n。Brendle-Schoen (2007) 用 Ricci 流证明 $\delta = 1/4$ 蕴含微分同胚（微分球面定理）。

---

## 六、组合

### 6.1 Ramsey 数 $R(5,5)$ 和 $R(6,6)$
**陈述**：见 Erdős 问题。$R(5,5)$ 的精确值？
**状态**：开放（$43 \leq R(5,5) \leq 48$）
**关键进展**：见 Erdős 问题文档。

### 6.2 Erdős 不同距离问题
**陈述**：见 Erdős 问题 E063。$n$ 个点确定的最少不同距离数。
**状态**：基本解决
**关键进展**：Guth-Katz (2015) 证明 $d(n) \geq cn/\log n$。精确渐近仍开放。

### 6.3 Hadwiger 猜想
**陈述**：色数为 $k$ 的图是否总有 $K_k$ 子式（minor）？
**状态**：部分解决
**关键进展**：Hadwiger (1943) 提出。$k \leq 6$ 已证（$k=5,6$ 由 Robertson-Sanders-Seymour-Thomas 证明，与四色定理等价）。$k=7$ 及以上开放。Wagner 猜想（已由 Robertson-Seymour 的图子式定理解决）相关但不同。

### 6.4 List coloring / Reed 猜想
**陈述**：图的列表色数 $\text{ch}(G) \leq \Delta(G) + 1$？更一般地，$\text{ch}(G) \leq \lceil(\Delta(G)+1+\omega(G))/2\rceil$？（Reed 猜想）
**状态**：部分解决
**关键进展**：Borodin, Erdős-Rubin-Taylor 等。Reed (1998) 的猜想。Havet 等的部分结果。

### 6.5 Sidorenko 猜想
**陈述**：见 Erdős 问题 E129。对每个二部图 $H$，$t_H(G) \geq t_{K_2}(G)^{e(H)}$。
**状态**：部分解决
**关键进展**：对树、偶圈等已证。一般情形开放。

### 6.6 容许集 / cap set 问题
**陈述**：$\mathbb{F}_3^n$ 中不含算术_progression（即 $x+y+z=0$ 的非平凡解）的最大子集大小？
**状态**：部分解决
**关键进展**：Croot-Lev-Pach (2016), Ellenberg-Gijswijt (2016) 证明上界 $O(2.756^n)$，大幅改进。下界约 $2.217^n$。精确渐近仍开放。

### 6.7 sunflower 猜想
**陈述**：见 Erdős 问题 E096。
**状态**：基本解决
**关键进展**：Alweiss-Lovett-Wu-Zhang (2020), Rao (2023)。

### 6.8 Lovász $\theta$ 函数与色数
**陈述**：Lovász $\theta$ 函数与色数、团数的关系的精确化。
**状态**：部分解决
**关键进展**：Lovász (1979) 的 $\theta$ 函数。$\theta(\bar{G})$ 介于 $\omega(G)$ 和 $\chi(G)$ 之间。精确关系仍部分开放。

### 6.9 组合设计的存在性
**陈述**：各种组合设计（Steiner 系统、$t$-设计等）的存在条件。
**状态**：部分解决
**关键进展**：Keevash (2014) 证明对足够大的 $n$，$t$-设计存在。Wilson (1970s) 的渐近理论。具体小参数仍需计算。

### 6.10 加性组合的 Polynomial Freiman-Ruzsa 猜想
**陈述**：若 $A \subseteq \mathbb{F}_2^n$ 满足 $|A+A| \leq K|A|$，则 $A$ 是否被包含在 $K^{O(1)}$ 维仿射子空间的 $K^{O(1)}$ 倍平移中？
**状态**：部分解决
**关键进展**：Freiman (1973), Ruzsa (1999) 的原始结果。Green-Tao (2010) 的近似。最近有重大进展（2023年，Tao 等人声称完整证明 PFR 猜想）。

---

## 七、概率 / 动力系统

### 7.1 自回避行走的连接常数
**陈述**：$\mathbb{Z}^d$ 上长度 $n$ 的自回避行走数 $c_n$ 的渐近行为。$c_n \sim A \mu^n n^{\gamma-1}$？连接常数 $\mu$ 的精确值？
**状态**：部分解决
**关键进展**：Hammersley-Morton (1954)。$\mu$ 的数值估计。$\mathbb{Z}^d$（$d \geq 5$）由 Hara-Slade (1990s) 用 lace expansion 证明。$d=2,3,4$ 仍开放。$d=2$ 的精确 $\mu$ 值由 Duminil-Copin-Smirnov (2012) 在六角格上证明。

### 7.2 KPZ 普适类
**陈述**：KPZ (Kardar-Parisi-Zhang) 方程的普适性——哪些随机增长模型属于 KPZ 普适类？精确的分布性质？
**状态**：部分解决
**关键进展**：Johansson (2000), Sasamoto-Spohn (2010), Amir-Corwin-Quastel (2011) 证明 TASEP 等模型属于 KPZ 类。Tracy-Widom 分布的出现。一般普适性证明仍开放。

### 7.3 Navier-Stokes 的随机版本
**陈述**：随机 Navier-Stokes 方程（加噪声）的全局适定性。
**状态**：部分解决
**关键进展**：Da Prato-Debussche (2003), Flandoli-Romito 等的工作。噪声可以正则化解。某些情形的全局适定性已证。

### 7.4 Ruelle-Pollicott 共振
**陈述**：双曲动力系统的 Ruelle-Pollicott 共振（转移算子的谱）的精确结构。
**状态**：部分解决
**关键进展**：Ruelle (1986), Pollicott (1985)。Dyatlov-Zworski (2010s) 的近期突破——与散射共振的关系。

### 7.5 遍历假设的验证
**陈述**：哪些物理系统的遍历假设成立？特别是硬球气体模型的遍历性。
**状态**：开放
**关键进展**：Sinai (1960s-70s) 证明 Sinai 台球的遍历性。硬球气体的遍历性长期开放。Simányi 的部分结果。

### 7.6 KAM 理论的有效性边界
**陈述**：见 Arnold 问题 A001。KAM 环面在何种扰动水平下被破坏？
**状态**：部分解决
**关键进展**：数值证据表明 KAM 环面在有限扰动后碎裂。精确阈值与 Greene 准则等。

### 7.7 Arnold 扩散的速率
**陈述**：见 Arnold 问题 A004。Arnold 扩散的时间尺度。
**状态**：部分解决
**关键进展**：扩散时间估计为指数级 $\sim e^{1/\epsilon^\alpha}$。精确指数 $\alpha$ 仍部分开放。

### 7.8 随机矩阵的普适性
**陈述**：随机矩阵特征值统计的普适性——哪些分布类具有相同的局部统计？
**状态**：部分解决
**关键进展**：Erdős-Yau (2010s) 证明 Wigner 矩阵的普适性（edge 和 bulk）。Tao-Vu 的 universality 结果。一般系综的完整普适性仍部分开放。

### 7.9 SLE (Schramm-Loewner Evolution) 的严格化
**陈述**：SLE 与格点模型的严格对应。如 Ising 模型的界面收敛到 SLE(3)。
**状态**：部分解决
**关键进展**：Smirnov (2001, Fields Medal 2010) 证明 Ising 模型界面收敛到 SLE(3)。Chelkak-Smirnov (2012) 等。一般格点模型的严格化仍部分开放。

### 7.10 量子唯一遍历性 (QUE)
**陈述**：负曲率流形上 Laplacian 特征函数在 $L^2$ 意义下是否遍历分布？（量子遍历性）
**状态**：部分解决
**关键进展**：Shnirelman (1974), Colin de Verdière, Zelditch 证明量子遍历性（密度1）。Rudnick-Sarnak (1994) 提出量子唯一遍历性（QUE）。Lindenstrauss (2006, Fields Medal) 证明算术曲面的 QUE。一般情形仍开放。

---

## 八、逻辑 / 计算

### 8.1 P vs NP
**陈述**：见千禧年问题。
**状态**：开放

### 8.2 NP vs coNP
**陈述**：NP = coNP？即每个补问题在 NP 中的问题是否也在 NP 中？
**状态**：开放
**关键进展**：若 NP ≠ coNP 则 P ≠ NP。TAUT（重言式问题）是否在 NP 中是关键。与证明复杂性相关。

### 8.3 P vs BPP
**陈述**：随机化计算是否比确定性计算更强大？P = BPP？
**状态**：部分解决（在假设下）
**关键进展**：Impagliazzo-Wigderson (1997) 证明若存在需要指数大小电路的问题则 P = BPP（去随机化）。一般情形仍开放。

### 8.4 Unique Games 猜想
**陈述**：Khot (2002) 提出的 Unique Games 猜想：对每个 $\epsilon > 0$，存在 $k$ 使得 Unique Games 问题（给定约束图，每条边约束是双射）难以区分"满足 $(1-\epsilon)$ 比例约束"和"满足 $\epsilon$ 比例约束"。
**状态**：开放
**关键进展**：蕴含大量最优不可近似性结果。Arora-Barak-Steurer (2010) 给出 Subexponential 时间算法（对某些情形）。2023年有重大进展——有研究者声称否定 Unique Games 猜想（通过近似算法），但仍在验证中。

### 8.5 $\mathbb{Q}$ 上的 Hilbert 第十问题
**陈述**：见 Smale 问题 S4。判定 $\mathbb{Q}$ 上多项式是否有 $\mathbb{Q}$-有理根的可判定性。
**状态**：开放
**关键进展**：Poonen, Eisenträger 等的部分结果。

### 8.6 连续统假设 (CH) 的"解决"
**陈述**：Cantor 连续统假设：$2^{\aleph_0} = \aleph_1$。Gödel (1940) 证明 CH 与 ZFC 相容，Cohen (1963) 证明 $\neg$CH 与 ZFC 相容。CH 是否有"正确"的答案？
**状态**：形式上已解决（独立于 ZFC），实质上开放
**关键进展**：Woodin 的 Ω-逻辑和 Ultimate L 程序试图给出 CH 的"正确"答案。Woodin 最初倾向于 CH 为假，后转向 Ultimate L（可能蕴含 CH）。此问题涉及集合论哲学。

### 8.7 大基数公理的一致性
**陈述**：各种大基数公理（measurable, supercompact, Woodin 等）与 ZFC 的一致性。
**状态**：部分解决
**关键进展**：大基数层级与描述集合论的深刻联系。内模型理论（Steel 等）。Ultimate L 程序。

### 8.8 直觉主义与构造性数学的边界
**陈述**：哪些经典数学定理可以在构造性框架中证明？反向数学（Reverse Mathematics）的分类。
**状态**：部分解决
**关键进展**：反向数学（Friedman-Simpson）将定理按证明强度分类为五大系统。大量定理已被分类。某些定理的分类仍开放。

### 8.9 证明复杂性
**陈述**：各种证明系统（Resolution, Cutting Planes, Frege, Extended Frege 等）的证明长度下界。
**状态**：部分解决
**关键进展**：Haken (1985) 证明 Resolution 的指数下界（Pigeonhole 原理）。Cutting Planes, Frege 的下界仍部分开放。与 NP ≠ coNP 相关。

### 8.10 同伦类型论 (HoTT) 中的未解决问题
**陈述**：Voevodsky 的 Univalence 公理的形式化后果。HoTT 能否作为数学的基础？
**状态**：部分解决
**关键进展**：HoTT book (2013)。Univalence 公理。Cubical type theory。与计算机形式化数学（Lean, Coq, Agda）的交叉。许多基本问题（如 canonicity）仍有待解决。

---

## 总结

本文档列出了8个数学领域共约70个核心开放问题。这些问题代表了当前数学研究的前沿。注意：

1. **问题间的联系**：许多问题跨领域关联。如 Riemann 假设同时是数论和分析问题；BSD 猜想连接数论和代数几何；P vs NP 是逻辑和计算的交叉。

2. **统一猜想体系**：Langlands 纋领、标准猜想、Bloch-Beilinson 猜想等构成了跨领域的统一猜想体系，解决其中任何一个都可能带动多个问题的进展。

3. **新工具的需求**：许多问题（如 Riemann 假设、P vs NP、Navier-Stokes）可能需要全新的数学工具，现有方法似乎不足以攻克。

4. **更新时间**：本文档内容截至2024年。部分问题可能已有新进展。建议定期更新。

5. **参考来源**：
   - Clay Mathematics Institute, *Millennium Problems*
   - Smale, "Mathematical problems for the next century", 1998
   - Arnold, *Arnold's Problems*, Springer, 2004
   - erdosproblems.com
   - 各领域的 *Open Problems in ...* 系列丛书
   - Bourbaki seminar 系列报告
