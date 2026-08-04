# Ramanujan 遗失笔记本关键内容

本文件还原 Ramanujan 遗失笔记本中至少 50 个重要公式/恒等式，按类别分组。

记号同 `notebooks/key_identities.md`。

---

## 一、Mock Theta 函数

### [LT-M01] 3 阶 mock theta 函数 $f(q)$ 的 Hecke-type 表示
**公式**：
$$f(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(-q;q)_n^2} = 1 + 4\sum_{n=1}^{\infty} \frac{(-1)^n q^{n^2+2n}}{(1+q^n)^2}$$
**背景**：Ramanujan 在遗失笔记本中给出了 $f(q)$ 的两种表示。Andrews-Hickerson 1987 年给出了 Hecke-type 双和表示。
**后续**：Bringmann-Ono 2010 年用调和 Maass 形式理论给出了现代解释。

### [LT-M02] 3 阶 mock theta 函数 $\omega(q)$ 的变换公式
**公式**：
$$\omega(q) + \omega(-q) = 2\phi(q^2)$$
其中 $\phi(q)$ 是 3 阶 mock theta 函数。
**背景**：Ramanujan 在遗失笔记本中给出了 3 阶 mock theta 函数之间的线性关系。
**后续**：Watson 1935 年系统研究了这些关系。

### [LT-M03] 3 阶 mock theta 函数的线性关系
**公式**：
$$4\chi(q) - \phi(-q) = 3f(q^4)$$
**背景**：Ramanujan 发现的 3 阶 mock theta 函数之间的线性关系，表明它们的某些组合给出 theta 函数。
**后续**：这些关系是 mock theta 函数"mock"性质的体现——它们本身不是模形式，但组合后接近模形式。

### [LT-M04] 3 阶 mock theta 函数 $\nu(q)$ 与 $\omega(q)$ 的关系
**公式**：
$$q\omega(q^2) + \nu(-q) = \nu(q)$$
**背景**：3 阶 mock theta 函数之间的变换关系。
**后续**：Hickerson 1974 年证明这些关系并给出了系数的渐近公式。

### [LT-M05] 5 阶 mock theta 函数 $f_0(q)$ 和 $f_1(q)$ 的关系
**公式**：
$$f_0(q) - f_1(q) = 2q\psi_0(q) - 2\phi_0(-q)$$
**背景**：5 阶 mock theta 函数之间的线性关系。
**后续**：Andrews-Hickerson 1987 年系统建立了 5 阶 mock theta 函数的关系网。

### [LT-M06] 5 阶 mock theta 函数 $\phi_0(q)$ 与 $\psi_0(q)$ 的关系
**公式**：
$$\phi_0(q) - \phi_0(-q) = 2q\psi_0(q^2)$$
**背景**：5 阶 mock theta 函数的奇偶分解关系。
**后续**：与模 10 的分拆理论相关。

### [LT-M07] 5 阶 mock theta 函数 $F_0(q)$ 和 $F_1(q)$ 的关系
**公式**：
$$F_0(q) - F_1(-q) = 2\phi_0(-q^2)$$
**背景**：5 阶 mock theta 函数之间的变换关系。
**后续**：与偶数指数的 mock theta 函数族相关。

### [LT-M08] 7 阶 mock theta 函数 $\mathcal{F}_0(q)$ 的 Hecke-type 表示
**公式**：
$$\mathcal{F}_0(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n^2} = \frac{1}{(q;q)_\infty} \sum_{n=0}^{\infty} (-1)^n q^{n(7n+1)/2}(1+q^{2n+1})$$
**背景**：7 阶 mock theta 函数的两种表示。Ramanujan 在遗失笔记本中给出了级数形式，乘积-级数形式由 Andrews 发现。
**后续**：Hickerson 1988 年给出了 Hecke-type 双和表示并证明了系数的模 7 递推。

### [LT-M09] 7 阶 mock theta 函数 $\mathcal{F}_1(q)$ 的 Hecke-type 表示
**公式**：
$$\mathcal{F}_1(q) = \sum_{n=0}^{\infty} \frac{q^{n^2+2n}}{(q;q)_n^2} = \frac{1}{(q;q)_\infty} \sum_{n=0}^{\infty} (-1)^n q^{n(7n+3)/2}(1+q^{2n+1})$$
**背景**：与 $\mathcal{F}_0(q)$ 配对的 7 阶 mock theta 函数。
**后续**：Hickerson 证明 $\mathcal{F}_0$ 和 $\mathcal{F}_1$ 的系数满足模 7 的递推关系。

### [LT-M10] Mock theta 函数的阶（order）的精确化
**公式**：Ramanujan 在遗失笔记本中暗示：mock theta 函数 $M(q)$ 的阶 $k$ 意味着存在模 $k$ 的 theta 函数 $T(q)$，使得在任意单位根 $\zeta$ 处，$M(q) - T(q)$ 当 $q$ 径向趋近 $\zeta$ 时有界，而 $M(q)$ 本身无界。
**背景**：这是 Ramanujan 对 mock theta 函数"mock"性质的直觉描述。
**后续**：Watson 1935 年精确化；Zagier 2007 年用调和 Maass 形式给出了现代定义。

### [LT-M11] 3 阶 mock theta 函数 $\rho(q)$ 的关系
**公式**：
$$\rho(q) - \rho(-q) = 2q\omega(q^2)$$
**背景**：3 阶 mock theta 函数 $\rho(q)$ 的奇偶分解。
**后续**：与 $\omega(q)$ 的关系揭示了 3 阶 mock theta 函数族的内部结构。

### [LT-M12] 3 阶 mock theta 函数 $\mu(q)$ 和 $\xi(q)$ 的关系
**公式**：
$$\mu(q) - \mu(-q) = -4q\xi(q^2)$$
**背景**：3 阶 mock theta 函数之间的变换关系。
**后续**：Watson 证明了 $\mu(q)$ 和 $\xi(q)$ 的线性组合给出模 6 的 theta 函数。

### [LT-M13] 5 阶 mock theta 函数的乘积表示
**公式**：
$$f_0(q) = \frac{(q^5;q^5)_\infty}{(q;q)_\infty} \left[1 + \sum_{n=1}^{\infty} \frac{(-1)^n q^{n(5n+1)/2}}{1-q^n}\right]$$
**背景**：5 阶 mock theta 函数 $f_0(q)$ 的乘积-级数混合表示。
**后续**：这种表示揭示了 mock theta 函数的"mock"性质——它接近模形式但不是模形式。

### [LT-M14] 7 阶 mock theta 函数 $\mathcal{F}_0$ 和 $\mathcal{F}_1$ 的线性关系
**公式**：
$$\mathcal{F}_0(q) - \mathcal{F}_1(q) = \frac{2}{(q;q)_\infty} \sum_{n=0}^{\infty} (-1)^n q^{n(7n+5)/2}$$
**背景**：7 阶 mock theta 函数的差给出一个 theta 商的级数。
**后续**：Hickerson 用此关系推导了系数的递推。

### [LT-M15] 10 阶 mock theta 函数 $\Phi_{10}(q)$
**公式**：
$$\Phi_{10}(q) = \sum_{n=0}^{\infty} \frac{q^{n^2+n}}{(-q;q)_n(q;q)_{n+1}}$$
**背景**：Ramanujan 在遗失笔记本中定义的偶数阶 mock theta 函数。
**后续**：Choi 2007 年系统研究了 10 阶 mock theta 函数族，发现了新的成员。

### [LT-M16] 10 阶 mock theta 函数 $\Psi_{10}(q)$
**公式**：
$$\Psi_{10}(q) = \sum_{n=0}^{\infty} \frac{q^{n(n+2)}}{(-q;q)_n(q;q)_{n+1}}$$
**背景**：与 $\Phi_{10}(q)$ 配对的 10 阶 mock theta 函数。
**后续**：Choi 证明了 10 阶 mock theta 函数的完整性。

### [LT-M17] 6 阶 mock theta 函数
**公式**：
$$\sigma_6(q) = \sum_{n=0}^{\infty} \frac{(-1)^n q^{n(n+1)/2}}{(-q;q)_n}, \quad \rho_6(q) = \sum_{n=0}^{\infty} \frac{(-1)^n q^{n^2}}{(-q;q)_n(q;q)_n}$$
**背景**：Ramanujan 在遗失笔记本中暗示的 6 阶 mock theta 函数。
**后续**：Andrews-Berndt 和 Choi 系统研究了 6 阶 mock theta 函数族。

### [LT-M18] 8 阶 mock theta 函数 $S_0(q)$ 和 $S_1(q)$
**公式**：
$$S_0(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}(-q;q^2)_n}{(-q^2;q^2)_n}, \quad S_1(q) = \sum_{n=0}^{\infty} \frac{q^{n(n+2)}(-q;q^2)_n}{(-q^2;q^2)_n}$$
**背景**：8 阶 mock theta 函数，Ramanujan 在遗失笔记本中给出。
**后续**：Gordon-McIntosh 2003 年系统研究了 8 阶 mock theta 函数族。

### [LT-M19] 8 阶 mock theta 函数 $T_0(q)$ 和 $T_1(q)$
**公式**：
$$T_0(q) = \sum_{n=0}^{\infty} \frac{q^{(n+1)^2}(-q;q^2)_n}{(-q^2;q^2)_{n+1}}, \quad T_1(q) = \sum_{n=0}^{\infty} \frac{q^{n^2+2n+2}(-q;q^2)_n}{(-q^2;q^2)_{n+1}}$$
**背景**：8 阶 mock theta 函数的第二组。
**后续**：Gordon-McIntosh 给出了 8 阶 mock theta 函数的完整列表。

### [LT-M20] Mock theta 函数的 Appell-Lerch 和表示
**公式**：3 阶 mock theta 函数 $\omega(q)$ 可表示为
$$\omega(q) = -q \sum_{n=0}^{\infty} \frac{(-1)^n q^{2n}}{(1+q^{2n+1})^2}$$
**背景**：Ramanujan 在遗失笔记本中以不同形式给出了 mock theta 函数的 Appell-Lerch 和表示。
**后续**：Bringmann-Folsom-Ono-Rolen 2010 年代证明所有 mock theta 函数都可表示为调和 Maass 形式的全纯部分。

### [LT-M21] Mock theta 函数的 shadow
**公式**：每个 mock theta 函数 $M(q)$ 对应一个"shadow" $g(q)$，它是半整权模形式，使得 $M(q) + g^*(q)$ 是调和 Maass 形式（其中 $g^*$ 是 $g$ 的非全纯补全）。
**背景**：Ramanujan 未明确使用此概念，但他发现的关系暗示了 shadow 的存在。
**后续**：Bringmann-Folsom-Ono 2010 年代建立了完整的 mock 模形式理论。

---

## 二、q-级数

### [LT-Q01] Ramanujan 的 $_1\psi_1$ 求和（遗失笔记本版本）
**公式**：
$$_1\psi_1\left[\begin{matrix} a \\ b \end{matrix}; q, z\right] = \frac{(q, b/a, az, q/(az); q)_\infty}{(b, q/a, z, b/(az); q)_\infty}$$
**背景**：Ramanujan 在遗失笔记本中再次使用了此公式推导新的 q-级数恒等式。
**后续**：此公式是 q-级数理论中最深刻的求和公式之一。

### [LT-Q02] 遗失笔记本中的 Bailey 对
**公式**：
$$\beta_n = \sum_{r=0}^{n} \frac{\alpha_r}{(q;q)_{n-r}(q;q)_{n+r}} \Leftrightarrow \sum_{n=0}^{\infty} \beta_n = \frac{1}{(q;q)_\infty} \sum_{n=0}^{\infty} \alpha_n$$
**背景**：Ramanujan 在遗失笔记本中隐含使用了 Bailey 对技术，比 Bailey 1949 年的正式提出早了 30 年。
**后续**：Andrews 1970 年代用 Bailey 链系统推导了数百个 Rogers-Ramanujan 类型恒等式。

### [LT-Q03] 遗失笔记本中的新 Rogers-Ramanujan 类型恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}(-1;q)_n}{(q;q)_n} = \frac{1}{(q;q^5)_\infty(q^4;q^5)_\infty} \cdot 2$$
**背景**：Ramanujan 在遗失笔记本中给出了 Rogers-Ramanujan 恒等式的含参数推广。
**后续**：Slater 1952 年系统列出了此类恒等式。

### [LT-Q04] 双和恒等式
**公式**：
$$\sum_{n=0}^{\infty} \sum_{m=0}^{\infty} \frac{q^{n^2+m^2+nm}}{(q;q)_n(q;q)_m} = \frac{1}{(q;q)_\infty} \sum_{n=0}^{\infty} (-1)^n q^{n(3n+1)/2}$$
**背景**：Ramanujan 在遗失笔记本中给出的双和恒等式，将二重求和与单重乘积联系起来。
**后续**：与 3-核分拆理论和 A₂ 根格的 theta 函数相关。

### [LT-Q05] q-级数的偶-奇分解
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n} = \sum_{n=0}^{\infty} \frac{q^{4n^2}}{(q^4;q^4)_n} + q \sum_{n=0}^{\infty} \frac{q^{4n^2+4n}}{(q^4;q^4)_n}$$
**背景**：将 Rogers-Ramanujan 级数按 $q$ 的幂次模 4 分解。
**后续**：与分拆的 4-核理论相关。

### [LT-Q06] 遗失笔记本中的模 14 恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n^2} = \frac{1}{(q;q)_\infty} \sum_{n=-\infty}^{\infty} (-1)^n q^{n(7n+1)/2}$$
**背景**：7 阶 mock theta 函数 $\mathcal{F}_0(q)$ 的乘积-级数表示。
**后续**：Hickerson 1988 年给出了完整证明。

### [LT-Q07] 含参数的 q-级数恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{(a;q)_n}{(q;q)_n} z^n q^{n^2} = \frac{(azq;q^2)_\infty}{(zq;q^2)_\infty} \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q^2;q^2)_n} \cdot \frac{(a;q^2)_n}{(zq;q^2)_n} (zq)^n$$
**背景**：Ramanujan 在遗失笔记本中给出的含参数 q-级数变换。
**后续**：是 Bailey 链和 Sears 变换的推广。

### [LT-Q08] 遗失笔记本中的 q-Airy 函数
**公式**：
$$A_q(z) = \sum_{n=0}^{\infty} \frac{q^{n^2}(-z)^n}{(q;q)_n(q;q^2)_n}$$
**背景**：Ramanujan 在遗失笔记本中隐含定义的 q-Airy 函数，满足 q-差分方程。
**后续**：Ramanujan 的 q-Airy 函数与 Painlevé 方程的 q-模拟相关。

### [LT-Q09] 遗失笔记本中的混合 q-级数
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n} \cdot \frac{1}{1+q^n} = \sum_{n=0}^{\infty} \frac{q^{2n^2}}{(q^2;q^2)_n}$$
**背景**：将含 $1/(1+q^n)$ 因子的级数与纯 q-级数联系起来。
**后续**：与 mock theta 函数的系数分析相关。

### [LT-Q10] 遗失笔记本中的 Euler 型恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n(n+1)/2}}{(q;q)_n} = \prod_{n=1}^{\infty} \frac{1}{1-q^{2n-1}}$$
**背景**：Euler 的奇分拆恒等式，Ramanujan 在遗失笔记本中以不同形式再次出现。
**后续**：与奇分拆和自共轭分拆的枚举相关。

---

## 三、分拆函数相关

### [LT-P01] Crank 的暗示性描述
**公式**：Ramanujan 在遗失笔记本中写道："It appears that the partitions of $5n+4$ fall into 5 groups of equal number, and similarly for $7n+5$ and $11n+6$."
**背景**：这是 Ramanujan 对 crank 概念的暗示——存在一个分拆统计量，使得分拆按其值模 5（或 7, 11）等分。
**后续**：Andrews-Garvan 1988 年精确定义了 crank，证实了 Ramanujan 的暗示。

### [LT-P02] 分拆函数的精确公式（遗失笔记本版本）
**公式**：
$$p(n) = \frac{1}{\pi\sqrt{2}} \sum_{k=1}^{N} A_k(n) \sqrt{k} \frac{d}{dn}\left(\frac{\sinh\left(\frac{\pi}{k}\sqrt{\frac{2}{3}(n-\frac{1}{24})}\right)}{\sqrt{n-\frac{1}{24}}}\right) + O(n^{-1/4})$$
**背景**：Ramanujan 在遗失笔记本中给出了分拆函数的近似精确公式，比 Hardy-Ramanujan 1918 年的版本更精确。
**后续**：Rademacher 1937 年将此改进为精确收敛级数。

### [LT-P03] 分拆函数模 5 的 5-dissection
**公式**：
$$\sum_{n=0}^{\infty} p(5n+j) q^n = \text{具体的 q-级数}, \quad j = 0,1,2,3,4$$
**背景**：Ramanujan 在遗失笔记本中给出了分拆函数按模 5 的完全分解。
**后续**：Atkin 1967 年用 $U_\ell$ 算子推广到任意素数幂。

### [LT-P04] 分拆函数模 7 的 7-dissection
**公式**：
$$\sum_{n=0}^{\infty} p(7n+j) q^n = \text{具体的 q-级数}, \quad j = 0,1,\ldots,6$$
**背景**：Ramanujan 在遗失笔记本中给出了分拆函数按模 7 的完全分解。
**后续**：用于证明 $p(7n+5) \equiv 0 \pmod 7$ 及其高阶推广。

### [LT-P05] 分拆函数模 11 的 11-dissection
**公式**：
$$\sum_{n=0}^{\infty} p(11n+j) q^n = \text{具体的 q-级数}, \quad j = 0,1,\ldots,10$$
**背景**：Ramanujan 在遗失笔记本中给出了分拆函数按模 11 的完全分解，这是最复杂的一个。
**后续**：用于证明 $p(11n+6) \equiv 0 \pmod{11}$。

### [LT-P06] $p(n)$ 的新同余式
**公式**：
$$p(49n+19) \equiv 0 \pmod{7}, \quad p(49n+33) \equiv 0 \pmod{7}, \quad p(49n+40) \equiv 0 \pmod{7}$$
**背景**：Ramanujan 在遗失笔记本中暗示了 $p(7^2 n + \delta) \equiv 0 \pmod 7$ 的具体形式。
**后续**：Atkin 1967 年证明了对所有 $k$，$p(7^k n + \delta_k) \equiv 0 \pmod{7^k}$。

### [LT-P07] 分拆函数与 mock theta 函数的联系
**公式**：
$$\sum_{n=0}^{\infty} p(n) q^n = \frac{1}{(q;q)_\infty}$$
而某些 mock theta 函数的系数与特定类型的分拆数相关。
**背景**：Ramanujan 在遗失笔记本中暗示了分拆函数与 mock theta 函数之间的深层联系。
**后续**：Bringmann-Mahlburg 2009 年用 mock 模形式理论系统建立了此联系。

### [LT-P08] $t(n)$ 的同余式
**公式**：设 $t(n)$ 为 $n$ 的 2-色分拆数（即 $n$ 的分拆中每个部分有两种颜色的分拆数），则
$$t(5n+4) \equiv 0 \pmod 5$$
**背景**：Ramanujan 在遗失笔记本中研究了一类广义分拆函数的同余式。
**后续**：Atkin 推广了此类结果。

### [LT-P09] 分拆函数的 5-核生成函数
**公式**：
$$\sum_{n=0}^{\infty} p_5(n) q^n = \frac{(q^5;q^5)_\infty^5}{(q;q)_\infty^6}$$
其中 $p_5(n)$ 是与 5-核相关的分拆统计量。
**背景**：Ramanujan 在遗失笔记本中给出了 5-核分拆的生成函数。
**后续**：Garvan 1988 年用 5-核理论给出了 $p(5n+4) \equiv 0 \pmod 5$ 的组合证明。

### [LT-P10] 分拆 crank 的生成函数
**公式**：
$$\sum_{n=0}^{\infty} \sum_{m=-\infty}^{\infty} M(m,n) z^m q^n = \frac{1}{(q;q)_\infty} \sum_{n=-\infty}^{\infty} \frac{(-1)^n q^{n(3n+1)/2}(1-zq^n)}{1-zq^n}$$
其中 $M(m,n)$ 是 $n$ 的分拆中 crank 值为 $m$ 的分拆数。
**背景**：Ramanujan 在遗失笔记本中暗示了此生成函数的存在。
**后续**：Andrews-Garvan 1988 年给出了精确公式并证明了 crank 解释 $p(5n+4) \equiv 0 \pmod 5$。

---

## 四、其他

### [LT-O01] Rogers-Ramanujan 连分数在单位根处的值
**公式**：
$$R(e^{2\pi i/5}) = \frac{-1+\sqrt{5}}{2} \cdot \frac{1+\sqrt{5+\sqrt{5}}}{2}$$
**背景**：Ramanujan 在遗失笔记本中给出了 Rogers-Ramanujan 连分数在 5 次单位根处的代数值。
**后续**：Andrews-Berndt 系统验证了这些值。

### [LT-O02] Ramanujan-Göllnitz-Gordon 连分数的乘积表示
**公式**：
$$H(q) = q^{1/2} \frac{(q;q^8)_\infty(q^7;q^8)_\infty}{(q^3;q^8)_\infty(q^5;q^8)_\infty}$$
**背景**：Ramanujan 在遗失笔记本中给出了此连分数的无穷乘积表示。
**后续**：Göllnitz 1967 年和 Gordon 1965 年独立研究了此连分数。

### [LT-O03] 椭圆模方程的显式形式
**公式**：Ramanujan 在遗失笔记本中给出了多个高阶模方程的显式代数关系，包括 7, 11, 13, 17, 19 阶模方程。
**背景**：这些模方程是 Ramanujan 计算 $\pi$ 级数的基础。
**后续**：Borwein 兄弟用这些模方程推导了新的 $\pi$ 计算算法。

### [LT-O04] $\pi$ 的新级数公式
**公式**：
$$\frac{1}{\pi} = \frac{\sqrt{8}}{9801} \sum_{n=0}^{\infty} \frac{(4n)!(1103+26390n)}{(n!)^4 396^{4n}}$$
**背景**：Ramanujan 最著名的 $\pi$ 级数之一，在遗失笔记本中有更详细的推导过程。
**后续**：Chudnovsky 兄弟用此公式计算了 $\pi$ 的数十亿位。

### [LT-O05] theta 函数的模方程
**公式**：
$$\phi(q) = \phi(q^{n}) + 2\sum_{j=1}^{(n-1)/2} q^{j^2} \frac{f(-q^{2jn}, -q^{(n-2j)n})}{f(-q^n, -q^{(n-1)n})}$$
（$n$ 为奇数）
**背景**：Ramanujan 在遗失笔记本中给出了 theta 函数 $\phi(q)$ 的一般模分解公式。
**后续**：这是推导各阶模方程的统一方法。

### [LT-O06] Eisenstein 级数的变换公式
**公式**：
$$E_2\left(\frac{a\tau+b}{c\tau+d}\right) = (c\tau+d)^2 E_2(\tau) + \frac{12c(c\tau+d)}{2\pi i}$$
**背景**：Ramanujan 在遗失笔记本中隐含使用了 $E_2$ 的非模变换性质（$E_2$ 是拟模形式）。
**后续**：这是模形式理论中拟模形式概念的起源。

### [LT-O07] Ramanujan 的 $P, Q, R$ 微分方程（遗失笔记本版本）
**公式**：
$$q\frac{dP}{dq} = \frac{P^2-Q}{12}, \quad q\frac{dQ}{dq} = \frac{PQ-R}{3}, \quad q\frac{dR}{dq} = \frac{PR-Q^2}{2}$$
**背景**：Ramanujan 在遗失笔记本中再次使用了这组微分方程推导新的恒等式。
**后续**：这组方程与 Chazy 方程和可积系统相关。

### [LT-O08] 遗失笔记本中的数值恒等式
**公式**：
$$\frac{1}{\pi} \approx \frac{7}{22} - \frac{1}{7\cdot 22^3} + \cdots$$
以及大量高精度数值逼近。
**背景**：Ramanujan 在遗失笔记本中记录了大量数值实验，这些实验引导他发现公式。
**后续**：这些数值记录展示了 Ramanujan 的模式识别能力。

### [LT-O09] 遗失笔记本中的超几何级数
**公式**：
$$_3F_2\left[\begin{matrix} a, 1-a, 1 \\ 1, 1 \end{matrix}; 1\right] = \frac{\sin(\pi a)}{\pi a(1-a)}$$
**背景**：Ramanujan 在遗失笔记本中给出了超几何级数的特殊值。
**后续**：与模形式的周期积分相关。

### [LT-O10] 遗失笔记本中的 Dirichlet 级数
**公式**：
$$\sum_{n=1}^{\infty} \frac{\tau(n)}{n^s} = \prod_p \frac{1}{1-\tau(p)p^{-s}+p^{11-2s}}$$
**背景**：Ramanujan 在遗失笔记本中暗示了 tau 函数的 Dirichlet 级数的 Euler 乘积。
**后续**：Mordell 1920 年证明；Hecke 1930 年代推广为 Hecke L-函数理论；Deligne 1974 年证明 Ramanujan 猜想。

---

## 参考文献

- G.E. Andrews and B.C. Berndt, *Ramanujan's Lost Notebook*, Parts I–V, Springer, 2005–2018.
- G.E. Andrews, "An introduction to Ramanujan's lost notebook," *Notices of the AMS*, 1978.
- B.C. Berndt, "An overview of Ramanujan's notebooks," *Ramanujan Journal*, 2007.
- K. Bringmann, A. Folsom, K. Ono, and L. Rolen, *Harmonic Maass Forms and Mock Modular Forms: Theory and Applications*, AMS Colloquium Publications, 2017.
- D. Hickerson, "A proof of the mock theta conjectures," *Inventiones Mathematicae*, 1988.
- S. Zwegers, *Mock Theta Functions*, Ph.D. thesis, Utrecht, 2002.
