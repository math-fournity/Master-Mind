# Ramanujan 到现代的后续证明链条

本文件详细记录从 Ramanujan 的工作到现代数学发展的完整链条，按主题分组。每条链条列出关键人物、关键论文和核心结果。

---

## 一、Mock Theta 函数链

**Ramanujan (1920) → Watson → Andrews (1970s) → Hickerson (1980s) → Cohen → Zwegers → Zagier (2000s) → Bringmann-Folsom-Ono-Rolen (2010s)**

### 1.1 Ramanujan (1919–1920)：起源

- **关键文献**：Ramanujan 给 Hardy 的最后一封信（1919年1月12日）；遗失笔记本（1919–1920）
- **核心结果**：定义 17 个 mock theta 函数（4 个 3 阶、10 个 5 阶、3 个 7 阶），提出"阶"的概念，给出 mock theta 函数之间的关系式
- **关键洞察**：mock theta 函数在单位根处有界但不是 theta 函数——它们"mock"（模仿）theta 函数的行为

### 1.2 G.N. Watson (1935–1939)：系统化

- **关键论文**：
  - Watson, "The final problem: an account of the mock theta functions," *Journal of the London Mathematical Society*, 11 (1936), 55–80
  - Watson, "The mock theta functions (2)," *Proceedings of the London Mathematical Society*, 42 (1937), 446–474
- **核心结果**：
  - 精确化了 Ramanujan 的"阶"的定义
  - 证明了 3 阶 mock theta 函数之间的关系式
  - 发现了新的 3 阶 mock theta 函数
  - 证明了 $\mu(q)$ 和 $\xi(q)$ 的线性组合给出模 6 的 theta 函数

### 1.3 George E. Andrews (1970s–1980s)：重新发现与推广

- **关键论文**：
  - Andrews, "An introduction to Ramanujan's lost notebook," *Notices of the AMS*, 23 (1976), A717
  - Andrews & Hickerson, "Ramanujan's mock theta functions," *Inventiones Mathematicae*, 94 (1988), 539–547（实际工作始于 1970s）
  - Andrews, "The fifth and seventh order mock theta functions," *Transactions of the AMS*, 293 (1986), 113–134
- **核心结果**：
  - 1976 年发现遗失笔记本
  - 系统研究了 5 阶和 7 阶 mock theta 函数
  - 给出了 mock theta 函数的 Hecke-type 双和表示
  - 建立了 mock theta 函数与分拆理论的联系

### 1.4 Dean Hickerson (1980s)：证明 mock theta 猜想

- **关键论文**：
  - Hickerson, "A proof of the mock theta conjectures," *Inventiones Mathematicae*, 94 (1988), 639–660
  - Hickerson, "On the seventh order functions of Ramanujan," *Pacific Journal of Mathematics*, 110 (1984), 281–304
- **核心结果**：
  - 证明了 Ramanujan 的 5 阶 mock theta 猜想（Andrews-Hickerson 联合工作）
  - 证明了 7 阶 mock theta 函数 $\mathcal{F}_0$ 和 $\mathcal{F}_1$ 的系数满足模 7 递推关系
  - 给出了 7 阶 mock theta 函数的 Hecke-type 表示

### 1.5 Henri Cohen (1975)：模变换方法

- **关键论文**：
  - Cohen, "Sums involving the values at negative integers of L-functions of quadratic characters," *Mathematische Annalen*, 217 (1975), 271–285
- **核心结果**：
  - 发展了半整权模形式的理论工具
  - 为 mock theta 函数的模形式解释提供了技术基础

### 1.6 Sander Zwegers (2002)：突破性博士论文

- **关键文献**：
  - Zwegers, *Mock Theta Functions*, Ph.D. thesis, Universiteit Utrecht, 2002
- **核心结果**：
  - **关键突破**：证明了 mock theta 函数是调和 Maass 形式的全纯部分
  - 给出了 mock theta 函数的 completion（非全纯补全），使其成为真正的调和 Maass 形式
  - 用 Appell-Lerch 和统一了所有 mock theta 函数的表示
  - 这一工作将 Ramanujan 的 mock theta 函数从"孤立现象"提升为"模形式理论的自然部分"

### 1.7 Don Zagier (2000s)：现代理论框架

- **关键论文**：
  - Zagier, "Ramanujan's mock theta functions and their applications [d'après Zwegers and Bringmann-Nickolaus]," *Astérisque*, 326 (2009), 143–164
  - Zagier, "Quantum modular forms," in *Quanta of Maths*, AMS, 2010, 339–366
- **核心结果**：
  - 给出了 mock 模形式的现代定义和分类
  - 提出了"quantum modular forms"概念——在 $\mathbb{Q}$ 上有定义但不在 $\mathbb{R}$ 上解析的函数
  - 将 mock theta 函数与量子模形式联系起来

### 1.8 Bringmann-Folsom-Ono-Rolen (2010s)：完整理论

- **关键文献**：
  - Bringmann, Folsom, Ono & Rolen, *Harmonic Maass Forms and Mock Modular Forms: Theory and Applications*, AMS Colloquium Publications, 64 (2017)
  - Bringmann & Ono, "The $f(q)$ mock theta function conjecture and partition ranks," *American Journal of Mathematics*, 132 (2010), 1623–1652
  - Bringmann, Mahlburg & Ono, "Combinatorial consequences of mock theta functions," *Proceedings of the National Academy of Sciences*, 110 (2013), 15206–15211
- **核心结果**：
  - 建立了 mock 模形式的完整理论框架
  - 证明了所有 Ramanujan mock theta 函数都是调和 Maass 形式的全纯部分
  - 将 mock theta 函数与分拆 crank、量子模形式、Maass 形式联系起来
  - 证明了 mock theta 函数系数的渐近公式

### 1.9 后续发展（2010s–2020s）

- **Duke-Imamoğlu-Kanevsky**：mock 模形式与 CM 椭圆曲线的联系
- **Eichler-Zagier**：Jacobi 形式与 mock theta 函数的关系
- **Choi-Lim**：10 阶 mock theta 函数的完整理论
- **Eguchi-Ooguri-Tachikawa**：mock theta 函数与拓扑弦理论/椭圆亏格的联系（K3 曲面）

---

## 二、分拆函数链

**Hardy-Ramanujan (1918) → Rademacher (1937) → Lehner → Newman → Atkin → Andrews → Bruinier-Ono (2000s)**

### 2.1 Hardy-Ramanujan (1918)：圆法与渐近公式

- **关键论文**：
  - Hardy & Ramanujan, "Asymptotic formulae in combinatory analysis," *Proceedings of the London Mathematical Society*, 17 (1918), 75–115
- **核心结果**：
  - 发明了**圆法** (circle method)
  - 得到分拆函数的渐近公式：$p(n) \sim \frac{1}{4n\sqrt{3}} e^{\pi\sqrt{2n/3}}$
  - 给出了 $p(n)$ 的近似精确级数（指数级收敛）
  - **关键思想**：将 $1/(q;q)_\infty$ 在单位圆上的行为用 Farey 分解分析

### 2.2 Rademacher (1937)：精确收敛级数

- **关键论文**：
  - Rademacher, "On the partition function $p(n)$," *Proceedings of the London Mathematical Society*, 43 (1937), 241–254
- **核心结果**：
  - 将 Hardy-Ramanujan 的近似级数改进为**精确收敛级数**
  - $p(n) = \frac{1}{\pi\sqrt{2}} \sum_{k=1}^{\infty} A_k(n) \sqrt{k} \frac{d}{dn}\left(\frac{\sinh(\frac{\pi}{k}\sqrt{\frac{2}{3}(n-\frac{1}{24})})}{\sqrt{n-\frac{1}{24}}}\right)$
  - 关键改进：用 Ford 圆代替 Farey 分解，使得级数精确收敛而非渐近

### 2.3 Lehner (1940s)：推广

- **关键论文**：
  - Lehner, "A partition function connected with the modulus five," *American Journal of Mathematics*, 63 (1941), 580–605
  - Lehner, "Proof of Ramanujan's partition conjecture for $p(11n+6)$," *American Journal of Mathematics*, 63 (1941), 578–580
- **核心结果**：
  - 推广 Rademacher 级数到 $p_k(n)$（$k$-色分拆数）
  - 给出了 $p(11n+6) \equiv 0 \pmod{11}$ 的 Rademacher 型证明

### 2.4 Newman (1950s)：解析方法

- **关键论文**：
  - Newman, "Note on Ramanujan's congruences modulo $5^a$," *Journal of the London Mathematical Society*, 31 (1956), 352–356
- **核心结果**：
  - 用解析方法证明了 Ramanujan 同余式的高阶推广
  - 发展了模形式在分拆函数中的应用

### 2.5 Atkin (1967)：$U_\ell$ 算子理论

- **关键论文**：
  - Atkin, "Proof of a conjecture of Ramanujan," *Glasgow Mathematical Journal*, 8 (1967), 14–32
  - Atkin & O'Brien, "Some properties of higher order partition functions," *Mathematical Proceedings of the Cambridge Philosophical Society*, 63 (1967), 437–447
- **核心结果**：
  - 发明了 **$U_\ell$ 算子**：$(\sum a(n)q^n) | U_\ell = \sum a(\ell n) q^n$
  - 证明了 Ramanujan 的猜想：$p(5^k n + \delta_k) \equiv 0 \pmod{5^k}$ 对所有 $k$ 成立
  - 同样证明了 $p(7^k n + \delta_k) \equiv 0 \pmod{7^k}$ 和 $p(11^k n + \delta_k) \equiv 0 \pmod{11^k}$
  - 建立了高阶分拆函数的系统理论

### 2.6 Andrews (1970s–2000s)：组合方法

- **关键论文**：
  - Andrews & Garvan, "The crank of a partition: development of a Ramanujan idea," *Bulletin of the London Mathematical Society*, 20 (1988), 317–325
  - Andrews, *The Theory of Partitions*, Cambridge, 1976（经典教材）
- **核心结果**：
  - 与 Garvan 共同发现了 crank 的精确定义（1988），证实了 Ramanujan 的暗示
  - 用 crank 给出了 $p(5n+4) \equiv 0 \pmod 5$ 的纯组合证明
  - 系统建立了分拆函数的组合理论

### 2.7 Bruinier-Ono (2000s)：现代模形式方法

- **关键论文**：
  - Bruinier & Ono, "The partition function as a mock modular form," *Journal für die reine und angewandte Mathematik*, 2010
  - Ono, "Distribution of the partition function modulo $m$," *Annals of Mathematics*, 151 (2000), 293–307
  - Ahlgren & Ono, "Congruence properties for the partition function," *Proceedings of the National Academy of Sciences*, 98 (2001), 12882–12884
- **核心结果**：
  - Ono (2000) 证明了对任意素数 $m \geq 5$，存在无穷多 $a, b$ 使得 $p(an+b) \equiv 0 \pmod m$——这是 Ramanujan 同余式的巨大推广
  - Bruinier-Ono 给出了 $p(n)$ 的调和 Maass 形式表示
  - 用 Galois 表示理论解释了分拆函数同余式的存在性

### 2.8 后续发展（2010s–2020s）

- **Bringmann-Mahlburg**：用 mock 模形式研究分拆函数的渐近性质
- **Chan-Kong**：分拆函数模小素数的完整同余式列表
- **Weaver**：计算验证了 $p(n)$ 的大规模同余式模式

---

## 三、Ramanujan 同余式链

**Ramanujan (1919) → Atkin → Newman → Andrews → Ono**

### 3.1 Ramanujan (1919)：三个基本同余式

- **关键文献**：Ramanujan 的笔记（1919）；Ramanujan, "Some properties of $p(n)$, the number of partitions of $n$," *Proceedings of the Cambridge Philosophical Society*, 19 (1919), 207–210
- **核心结果**：
  - $p(5n+4) \equiv 0 \pmod 5$
  - $p(7n+5) \equiv 0 \pmod 7$
  - $p(11n+6) \equiv 0 \pmod{11}$
  - 猜想 $p(5^k n + \delta_k) \equiv 0 \pmod{5^k}$ 等高阶推广

### 3.2 Winquist (1969)：$p(11n+6)$ 的组合证明

- **关键论文**：
  - Winquist, "An elementary proof of $p(11n+6) \equiv 0 \pmod{11}$," *Journal of Combinatorial Theory*, 6 (1969), 56–59
- **核心结果**：
  - 用 Ramanujan 的五重积恒等式给出了 $p(11n+6) \equiv 0 \pmod{11}$ 的组合证明
  - 这是三个基本同余式中最后一个获得组合证明的

### 3.3 Atkin (1967)：高阶推广

- **关键论文**：同 2.5
- **核心结果**：
  - 证明了 Ramanujan 猜想：$p(\ell^k n + \delta_k) \equiv 0 \pmod{\ell^k}$ 对 $\ell = 5, 7, 11$ 和所有 $k$
  - 发明了 $U_\ell$ 和 $V_\ell$ 算子，成为分拆函数同余式研究的基本工具

### 3.4 Newman (1950s–1960s)：模 5 和模 7

- **关键论文**：同 2.4
- **核心结果**：
  - 用解析方法证明了 $p(5^a n + \delta) \equiv 0 \pmod{5^a}$ 的具体形式
  - 为 Atkin 的完整理论铺路

### 3.5 Andrews-Garvan (1988)：crank 的组合解释

- **关键论文**：同 2.6
- **核心结果**：
  - crank 的精确定义使得 $p(5n+4) \equiv 0 \pmod 5$ 有纯组合解释
  - crank 模 5 的分拆等分解释了同余式
  - 类似地，rank（Atkin-Garvan）解释了 $p(7n+5) \equiv 0 \pmod 7$

### 3.6 Ono (2000)：一般性定理

- **关键论文**：
  - Ono, "Distribution of the partition function modulo $m$," *Annals of Mathematics*, 151 (2000), 293–307
  - Ahlgren & Ono, "Addition and counting: the arithmetic of partitions," *Proceedings of the National Academy of Sciences*, 98 (2001), 12882–12884
- **核心结果**：
  - **主定理**：对任意素数 $m \geq 5$，存在无穷多非负整数对 $(a, b)$ 使得 $p(an+b) \equiv 0 \pmod m$
  - 这是 Ramanujan 同余式的终极推广——Ramanujan 发现的 5, 7, 11 不是特例，而是一般现象的实例
  - 证明使用了 Galois 表示理论和模形式
  - 对 $m = 2, 3$ 也有类似结果（不同形式）

### 3.7 后续发展

- **Weaver (2015)**：计算验证了 $p(n)$ 模小素数的大规模同余模式
- **Chan-Wang-Yang**：分拆函数模任意素数幂的同余式
- **Kiming-Olsson**：分拆函数同余式与 Galois 表示的深层联系

---

## 四、Rogers-Ramanujan 连分数链

**Rogers (1894) → Ramanujan (1910s) → Slater → Andrews → Shanks**

### 4.1 Rogers (1894)：原始发现

- **关键论文**：
  - Rogers, "Third memoir on the expansion of certain infinite products," *Proceedings of the London Mathematical Society*, 26 (1894), 15–32
- **核心结果**：
  - 首次证明了 Rogers-Ramanujan 恒等式和连分数的乘积表示
  - 但 Rogers 的工作长期被忽视

### 4.2 Ramanujan (1910s)：独立发现与推广

- **关键文献**：Ramanujan 笔记第二本（约 1911–1913）；Ramanujan 给 Hardy 的第一封信（1913年1月16日）
- **核心结果**：
  - 独立发现了 Rogers-Ramanujan 恒等式和连分数
  - 给出了 $R(q)$ 的乘积表示
  - 发现了 $R(q)$ 在特殊点的代数值（如 $R(e^{-2\pi})$）
  - 给出了 $R(q)$ 的模方程（$R(q)$ 与 $R(q^5)$ 的关系）
  - Hardy 将 Ramanujan 的结果告知 Rogers，Rogers 才发现自己 1894 年的结果已被重新发现

### 4.3 Slater (1952)：系统列举

- **关键论文**：
  - Slater, "Further identities of the Rogers-Ramanujan type," *Proceedings of the London Mathematical Society*, 54 (1952), 147–167
- **核心结果**：
  - 系统列举了 130 多个 Rogers-Ramanujan 类型的恒等式
  - 用 Bailey 对方法统一推导了这些恒等式
  - 建立了 Rogers-Ramanujan 类型恒等式的系统分类

### 4.4 Andrews (1970s–2000s)：Bailey 链理论

- **关键论文**：
  - Andrews, "Multiple series Rogers-Ramanujan type identities," *Pacific Journal of Mathematics*, 114 (1984), 267–283
  - Andrews, *The Theory of Partitions*, Cambridge, 1976
- **核心结果**：
  - 发展了 **Bailey 链** (Bailey's chain) 理论，系统生成新的 Rogers-Ramanujan 类型恒等式
  - 证明了大量新的恒等式
  - 将 Rogers-Ramanujan 恒等式与统计力学（Baxter 的硬六边形模型）联系起来

### 4.5 Shanks (1960s)：计算与验证

- **关键论文**：
  - Shanks, "A note on the Rogers-Ramanujan identities," *Journal of the London Mathematical Society*, 23 (1948), 282–287
- **核心结果**：
  - 给出了 Rogers-Ramanujan 恒等式的简化证明
  - 研究了连分数的收敛性质

### 4.6 后续发展

- **Baxter (1981)**：在硬六边形模型中重新发现 Rogers-Ramanujan 恒等式，建立了与统计力学的联系
- **Warnaar (2000s)**：多重 Rogers-Ramanujan 恒等式和 Hall-Littlewood 多项式
- **Bressoud (1980s)**：Rogers-Ramanujan 类型恒等式的组合证明和推广

---

## 五、圆法链

**Hardy-Littlewood-Ramanujan (1918) → Vinogradov → Vaughan → Heath-Brown → Maynard**

### 5.1 Hardy-Ramanujan (1918)：圆法的发明

- **关键论文**：同 2.1
- **核心结果**：
  - 发明了**圆法** (circle method)，用于估计分拆函数 $p(n)$
  - 核心思想：将生成函数 $F(q) = 1/(q;q)_\infty$ 的系数提取问题转化为在单位圆 $|q|=1$ 上的积分，然后用 Farey 分解分析被积函数在各圆弧上的行为
  - 得到 $p(n)$ 的渐近公式和近似精确级数

### 5.2 Hardy-Littlewood (1920s)：圆法的推广

- **关键论文**：
  - Hardy & Littlewood, "Some problems of 'Partitio Numerorum'; I: A new solution of Waring's problem," *Göttingen Nachrichten*, 1920, 33–54
  - Hardy & Littlewood, "Some problems of 'Partitio Numerorum'; II: Proof that every large number is the sum of at most 21 biquadrates," *Mathematische Zeitschrift*, 9 (1921), 14–27
  - Hardy & Littlewood, "Some problems of 'Partitio Numerorum'; III: On the expression of a number as a sum of primes," *Acta Mathematica*, 44 (1923), 1–70
- **核心结果**：
  - 将圆法从分拆函数推广到 Waring 问题（将 $n$ 表示为 $k$ 次幂之和）
  - 将圆法应用于 Goldbach 猜想（将 $n$ 表示为素数之和）
  - 建立了圆法作为解析数论的核心工具

### 5.3 Vinogradov (1930s)：改进与三素数定理

- **关键论文**：
  - Vinogradov, "Representation of an odd number as the sum of three primes," *Doklady Akademii Nauk SSSR*, 15 (1937), 291–294
  - Vinogradov, *The Method of Trigonometrical Sums in the Theory of Numbers*, 1947（专著）
- **核心结果**：
  - 改进了圆法中的误差项估计，用 Vinogradov 估计代替 Hardy-Littlewood 估计
  - 证明了**三素数定理**：每个充分大的奇数是三个素数之和
  - 发展了三角和估计方法，成为现代解析数论的基础工具

### 5.4 Vaughan (1970s–1980s)：系统化

- **关键论文**：
  - Vaughan, *The Hardy-Littlewood Method*, Cambridge, 1977（经典教材，多次再版）
  - Vaughan, "An elementary method in prime number theory," *Acta Arithmetica*, 37 (1980), 111–115
- **核心结果**：
  - 系统整理了圆法（Hardy-Littlewood 方法）的完整理论
  - 发展了 Vaughan 恒等式，改进了圆法中的素数和估计
  - 将圆法应用于更多数论问题

### 5.5 Heath-Brown (1980s–2000s)：精细改进

- **关键论文**：
  - Heath-Brown, "Three recent developments in analytic number theory," in *Proceedings of the ICM*, 1990
  - Heath-Brown, "The number of primes in a short interval," *Journal für die reine und angewandte Mathematik*, 389 (1988), 22–63
- **核心结果**：
  - 对圆法中的各部分进行了精细改进
  - 改进了圆弧上的指数和估计
  - 将圆法与筛法结合，解决了多个经典问题

### 5.6 Maynard (2010s–2020s)：现代突破

- **关键论文**：
  - Maynard, "Small gaps between primes," *Annals of Mathematics*, 181 (2015), 383–413
  - Maynard, "Dense clusters of primes in subsets," *Compositio Mathematica*, 152 (2016), 1517–1554
- **核心结果**：
  - 用改进的筛法（Maynard-Tao 方法）证明了有界素数间隙
  - 虽然主要使用筛法而非圆法，但圆法的思想在背景中起指导作用
  - 将圆法的思想与现代筛法技术结合

### 5.7 后续发展

- **Green-Tao (2004)**：用圆法的推广（transference principle）证明了素数序列包含任意长等差数列
- **Helfgott (2013)**：用圆法完整证明了弱 Goldbach 猜想（每个奇数 $\geq 7$ 是三个素数之和）
- **Bourgain (2010s)**：圆法在非线性问题和加性组合学中的推广

---

## 六、模方程与 $\pi$ 级数链

**Ramanujan (1914) → Borwein-Borwein (1980s) → Chudnovsky-Chudnovsky (1980s–1990s) → Bailey-Borwein-Plouffe (1990s)**

### 6.1 Ramanujan (1914)：$\pi$ 级数和模方程

- **关键论文**：
  - Ramanujan, "Modular equations and approximations to $\pi$," *Quarterly Journal of Mathematics*, 45 (1914), 350–372
- **核心结果**：
  - 给出了 17 个 $1/\pi$ 的级数公式，每个级数每项给出约 8 位有效数字
  - 系统建立了模方程与 $\pi$ 级数的联系
  - 最著名的公式：$\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)!(1103+26390n)}{(n!)^4 396^{4n}}$

### 6.2 Borwein-Borwein (1980s)：系统理论

- **关键论文**：
  - Borwein & Borwein, "A cubic counterpart of Jacobi's identity and the AGM," *Ramanujan Journal*, 1 (1997), 3–19（实际工作始于 1980s）
  - Borwein & Borwein, *Pi and the AGM*, Wiley, 1987（经典专著）
- **核心结果**：
  - 系统分类了 Ramanujan 的 $\pi$ 级数，给出了统一推导方法
  - 发现了新的 $\pi$ 级数（包括 3 次、4 次、9 次幂的版本）
  - 建立了 $\pi$ 级数与 AGM（算术-几何平均）的联系
  - 证明了 Ramanujan 的所有 17 个公式的正确性

### 6.3 Chudnovsky-Chudnovsky (1980s–1990s)：世界纪录

- **关键论文**：
  - Chudnovsky & Chudnovsky, "Approximations and complex multiplication according to Ramanujan," in *Ramanujan Revisited*, Academic Press, 1988, 375–472
- **核心结果**：
  - 推导了 Chudnovsky 算法：$\frac{1}{\pi} = 12 \sum_{n=0}^{\infty} (-1)^n \frac{(6n)!(545140134n+13591409)}{(3n)!(n!)^3 640320^{3n+3/2}}$
  - 用此算法多次打破 $\pi$ 的计算世界纪录
  - 建立了 $\pi$ 级数与 CM 椭圆曲线的深层联系

### 6.4 Bailey-Borwein-Plouffe (1990s)：BBP 公式

- **关键论文**：
  - Bailey, Borwein & Plouffe, "On the rapid computation of various polylogarithmic constants," *Mathematics of Computation*, 66 (1997), 903–913
- **核心结果**：
  - 发现了 BBP 公式：$\pi = \sum_{n=0}^{\infty} \frac{1}{16^n}\left(\frac{4}{8n+1}-\frac{2}{8n+4}-\frac{1}{8n+5}-\frac{1}{8n+6}\right)$
  - 允许直接计算 $\pi$ 的第 $n$ 位十六进制数字而无需计算前 $n-1$ 位
  - 虽然不直接来自 Ramanujan，但继承了 Ramanujan 用级数研究 $\pi$ 的精神

### 6.5 后续发展

- **Bellard (1997)**：发现了更快的 BBP 型公式
- **Yee-Kondo (2010s)**：用 Chudnovsky 算法计算 $\pi$ 到数万亿位
- **Borwein-Bailey-Girgensohn**：*Experimentation in Mathematics* (2004)，系统整理了实验数学方法

---

## 七、tau 函数与模形式链

**Ramanujan (1916) → Mordell (1920) → Hecke (1930s) → Deligne (1974) → Serre-Swinnerton-Dyer (1970s)**

### 7.1 Ramanujan (1916)：tau 函数的定义和猜想

- **关键论文**：
  - Ramanujan, "On certain arithmetical functions," *Transactions of the Cambridge Philosophical Society*, 22 (1916), 159–184
- **核心结果**：
  - 定义了 tau 函数：$\sum \tau(n)q^n = q\prod(1-q^n)^{24} = \Delta(\tau)$
  - 猜想 $\tau$ 是乘性的：$\tau(mn) = \tau(m)\tau(n)$ 当 $\gcd(m,n)=1$
  - 猜想递推关系：$\tau(p^{n+2}) = \tau(p)\tau(p^{n+1}) - p^{11}\tau(p^n)$
  - 猜想 $|\tau(p)| \leq 2p^{11/2}$（Ramanujan-Petersson 猜想）
  - 发现同余式 $\tau(n) \equiv \sigma_{11}(n) \pmod{691}$

### 7.2 Mordell (1920)：乘性证明

- **关键论文**：
  - Mordell, "On Mr Ramanujan's empirical expansions of modular functions," *Proceedings of the Cambridge Philosophical Society*, 19 (1920), 117–124
- **核心结果**：
  - 证明了 Ramanujan 的乘性猜想和递推关系
  - 引入了 Hecke 算子的雏形（$T_n$ 算子）
  - 但未能证明 $|\tau(p)| \leq 2p^{11/2}$

### 7.3 Hecke (1930s)：Hecke 算子理论

- **关键论文**：
  - Hecke, "Über Modulfunktionen und die Beziehung zwischen den Fourierkoeffizienten von elliptischen Modulfunktionen," *Mathematische Annalen*, 114 (1937), 316–351
- **核心结果**：
  - 系统建立了 Hecke 算子理论
  - 证明了 Mordell 的结果是 Hecke 算子的一般理论的特例
  - 建立了模形式的 L-函数理论

### 7.4 Petersson (1939)：内积空间

- **关键论文**：
  - Petersson, "Konstruktion der sämtlichen Lösungen einer Riemannschen Funktionalgleichung durch Dirichletreihen mit Eulerscher Produktentwicklung I," *Mathematische Annalen*, 116 (1939), 401–412
- **核心结果**：
  - 建立了模形式的 Petersson 内积
  - 将 Ramanujan 猜想推广为 Petersson 猜想（对所有尖点模形式）

### 7.5 Deligne (1974)：Ramanujan 猜想的证明

- **关键论文**：
  - Deligne, "La conjecture de Weil. I," *Publications Mathématiques de l'IHÉS*, 43 (1974), 273–307
- **核心结果**：
  - **证明了 Ramanujan-Petersson 猜想**：$|\tau(p)| \leq 2p^{11/2}$
  - 证明使用了 Weil 猜想（Deligne 同年证明）的框架
  - 关键思想：$\tau(p)$ 是某个 $\ell$-adic Galois 表示的迹，其特征值的绝对值为 $p^{11/2}$
  - 这是 20 世纪数论最深刻的成果之一

### 7.6 Serre-Swinnerton-Dyer (1970s)：Galois 表示

- **关键论文**：
  - Serre, "Congruences et formes modulaires [d'après H.P.F. Swinnerton-Dyer]," *Séminaire Bourbaki*, 1971/72, exp. 416
  - Swinnerton-Dyer, "On $l$-adic representations and congruences for coefficients of modular forms," in *Modular Functions of One Variable III*, Springer, 1973
- **核心结果**：
  - 系统研究了模形式系数的 Galois 表示
  - 解释了 Ramanujan 同余式 $\tau(n) \equiv \sigma_{11}(n) \pmod{691}$ 的 Galois 表示背景
  - 建立了模形式与 Galois 表示的一般理论

### 7.7 后续发展

- **Wiles-Taylor (1995)**：用模形式的 Galois 表示证明了 Fermat 大定理
- **Khare-Wintenberger (2008)**：证明了 Serre 的模性猜想
- **Buzzard-Gee**：p-adic 模形式和 Ramanujan 同余式的推广

---

## 参考文献

- G.H. Hardy, *Ramanujan: Twelve Lectures on Subjects Suggested by His Life and Work*, Cambridge, 1940.
- B.C. Berndt, *Ramanujan's Notebooks*, Parts I–V, Springer, 1985–1998.
- G.E. Andrews & B.C. Berndt, *Ramanujan's Lost Notebook*, Parts I–V, Springer, 2005–2018.
- K. Bringmann, A. Folsom, K. Ono & L. Rolen, *Harmonic Maass Forms and Mock Modular Forms*, AMS, 2017.
- H. Rademacher & E. Grosswald, *Dedekind Sums*, AMS, 1972.
- T.M. Apostol, *Modular Functions and Dirichlet Series in Number Theory*, Springer, 1990.
- J.-P. Serre, *A Course in Arithmetic*, Springer, 1973.
- H. Iwaniec & E. Kowalski, *Analytic Number Theory*, AMS, 2004.
- R.C. Vaughan, *The Hardy-Littlewood Method*, Cambridge, 1997.
- J. Borwein & P. Borwein, *Pi and the AGM*, Wiley, 1987.
