# Ramanujan 笔记中的关键恒等式分类

本文件还原 Ramanujan 三本笔记中至少 100 个重要恒等式，按类别分组。记号约定：

- $q$ 为形式变量，通常 $|q|<1$
- $(a;q)_\infty = \prod_{n=0}^{\infty}(1-aq^n)$，$(a;q)_n = \prod_{k=0}^{n-1}(1-aq^k)$
- Ramanujan 的 theta 函数记号：$f(a,b) = \sum_{n=-\infty}^{\infty} a^{n(n+1)/2} b^{n(n-1)/2}$
- $\phi(q) = f(q,q) = \sum_{n=-\infty}^{\infty} q^{n^2} = (-q;q^2)_\infty^2 (q^2;q^2)_\infty$
- $\psi(q) = f(q,q^3) = \sum_{n=0}^{\infty} q^{n(n+1)/2} = \frac{(q^2;q^2)_\infty}{(q;q^2)_\infty}$
- $f(-q) = (q;q)_\infty = \prod_{n=1}^{\infty}(1-q^n)$

---

## 一、q-级数恒等式（Rogers-Ramanujan 类型）

### [Q01] Rogers-Ramanujan 恒等式（第一式）
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n} = \frac{1}{(q;q^5)_\infty (q^4;q^5)_\infty}$$
**背景**：Ramanujan 在笔记中独立发现了此恒等式，后得知 Rogers 已于 1894 年证明。这是 Rogers-Ramanujan 恒等式中最著名的一式。
**后续**：MacMahon 给出组合解释（以 5 为模的分拆）；Baxter 在硬六边形模型中重新发现；成为 Rogers-Ramanujan 连分数的理论基础。

### [Q02] Rogers-Ramanujan 恒等式（第二式）
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2+n}}{(q;q)_n} = \frac{1}{(q^2;q^5)_\infty (q^3;q^5)_\infty}$$
**背景**：与第一式配对的第二恒等式，同样由 Rogers 首证、Ramanujan 独立发现。
**后续**：两式合起来给出 Rogers-Ramanujan 连分数的乘积展开。

### [Q03] Rogers-Ramanujan 连分数
**公式**：
$$R(q) = \frac{q^{1/5}}{1+\frac{q}{1+\frac{q^2}{1+\frac{q^3}{1+\cdots}}}} = q^{1/5} \frac{(q;q^5)_\infty (q^4;q^5)_\infty}{(q^2;q^5)_\infty (q^3;q^5)_\infty}$$
**背景**：Ramanujan 最著名的连分数之一，将连分数与无穷乘积联系起来。
**后续**：Andrews 等人研究了 $R(q)$ 在单位根处的值；$R(e^{-2\pi})$ 有优美的代数表达式。

### [Q04] Ramanujan 三重积恒等式（Jacobi 三重积的 Ramanujan 形式）
**公式**：
$$\sum_{n=-\infty}^{\infty} z^n q^{n^2} = (-zq;q^2)_\infty \left(-\frac{q}{z};q^2\right)_\infty (q^2;q^2)_\infty$$
**背景**：这是 Jacobi 三重积恒等式的 Ramanujan 记号版本，是 Ramanujan 推导大量 q-级数恒等式的基本工具。
**后续**：现代 q-级数理论的基础工具之一。

### [Q05] Ramanujan $_1\psi_1$ 求和公式
**公式**：
$$_1\psi_1\left[\begin{matrix} a \\ b \end{matrix}; q, z\right] = \sum_{n=-\infty}^{\infty} \frac{(a;q)_n}{(b;q)_n} z^n = \frac{(q, b/a, az, q/(az); q)_\infty}{(b, q/a, z, b/(az); q)_\infty}$$
**背景**：Ramanujan 笔记中最深刻的 q-级数求和公式之一，是 q-超几何级数的双边求和，推广了 Gauss 求和公式和 Jacobi 三重积。
**后续**：Hardy 认为这是 Ramanujan 最美的公式之一；Hahn、Exton 等人推广到多维情形。

### [Q06] Ramanujan q-Gauss 恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{(a;q)_n}{(q;q)_n} z^n = \frac{(az;q)_\infty}{(z;q)_\infty}$$
**背景**：q-模拟的 Gauss 二项式定理，是 q-级数理论的基本恒等式。
**后续**：Heine 的 q-超几何级数理论的基础。

### [Q07] Ramanujan 5-阶 mock theta 恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q^2)_{n+1}} = 1 + \sum_{n=1}^{\infty} \frac{q^{n^2}}{(1-q)(1-q^2)\cdots(1-q^{2n})}$$
**背景**：与 5 阶 mock theta 函数 $f_0(q)$ 相关的恒等式。
**后续**：Andrews-Hickerson 给出了完整的 5 阶 mock theta 函数理论。

### [Q08] Euler 恒等式（Ramanujan 形式）
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n(n+1)/2}}{(q;q)_n} = (q^2;q^2)_\infty \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q^2;q^2)_n}$$
**背景**：Ramanujan 对 Euler 分拆恒等式的推广形式之一。
**后续**：与奇分拆和偶分拆的枚举密切相关。

### [Q09] Ramanujan-Slater 恒等式（模 7）
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n^2} = \frac{1}{(q;q)_\infty} \sum_{n=0}^{\infty} (-1)^n q^{n(7n+1)/2}$$
**背景**：属于 Rogers-Ramanujan 类型恒等式族中模 7 的成员，Slater 系统列出了此类恒等式。
**后续**：Slater 1952 年列出了 130 多个此类恒等式。

### [Q10] Ramanujan-Slater 恒等式（模 7，第二式）
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2+2n}}{(q;q)_n^2} = \frac{1}{(q;q)_\infty} \sum_{n=0}^{\infty} (-1)^n q^{n(7n+5)/2}$$
**背景**：与 [Q09] 配对的模 7 恒等式。
**后续**：这类恒等式与 Virasoro 代数的极小模型表示相关。

### [Q11] Ramanujan-Slater 恒等式（模 11）
**公式**：
$$1 + \sum_{n=1}^{\infty} \frac{q^{n^2}}{(q;q)_n^2} = \frac{1}{(q;q)_\infty} \sum_{n=0}^{\infty} (-1)^n q^{n(11n+1)/2}(1+q^{2n+1})$$
**背景**：模 11 的 Rogers-Ramanujan 类型恒等式。
**后续**：与 11 阶 mock theta 函数有深层联系。

### [Q12] Ramanujan-Slater 恒等式（模 11，第二式）
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2+2n}}{(q;q)_n^2} = \frac{1}{(q;q)_\infty} \sum_{n=0}^{\infty} (-1)^n q^{n(11n+3)/2}(1+q^{2n+1})$$
**背景**：与 [Q11] 配对。
**后续**：Mc Laughlin 等人推广了此类恒等式。

### [Q13] Winquist 恒等式（Ramanujan 的版本）
**公式**：
$$\sum_{n=-\infty}^{\infty} (-1)^n q^{n(3n-1)/2}(1+q^n) = (q;q)_\infty$$
**背景**：与 Euler 五角数定理相关的恒等式，Ramanujan 在笔记中以不同形式出现。
**后续**：Winquist 1969 年用此证明了 Ramanujan 的 $p(11n+6) \equiv 0 \pmod{11}$。

### [Q14] Ramanujan 的 $_6\phi_5$ 求和
**公式**：
$$_6\phi_5\left[\begin{matrix} a, \sqrt{a}, -\sqrt{a}, b, c, d \\ \sqrt{a}, -\sqrt{a}, \frac{qa}{b}, \frac{qa}{c}, \frac{qa}{d} \end{matrix}; q, \frac{qa}{bcd}\right] = \frac{(qa, qa/(bc), qa/(bd), qa/(cd); q)_\infty}{(qa/b, qa/c, qa/d, qa/(bcd); q)_\infty}$$
**背景**：非常一般的 q-超几何级数求和公式，许多其他恒等式是其特例。
**后续**：Gasper 和 Rahman 的 q-超几何级数理论的核心公式。

### [Q15] Ramanujan 的 Bailey 型恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{(-1)^n q^{n^2} (q;q^2)_n}{(q^2;q^2)_n^2} = \frac{(q;q^2)_\infty}{(q^2;q^2)_\infty}$$
**背景**：Ramanujan 在第二本笔记中给出的恒等式，与 Bailey 对理论相关。
**后续**：Bailey 1949 年发展了 Bailey 对理论，Andrews 用其系统推导 Rogers-Ramanujan 类型恒等式。

### [Q16] Ramanujan 的分拆秩恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n} = \sum_{n=0}^{\infty} \frac{q^{2n^2}}{(q;q)_{2n}} + \sum_{n=0}^{\infty} \frac{q^{2n^2+2n}}{(q;q)_{2n+1}}$$
**背景**：将 Rogers-Ramanujan 恒等式拆分为偶秩和奇秩分拆。
**后续**：Atkin 的分拆秩理论的基础。

### [Q17] Ramanujan 的 Durfee 方恒等式
**公式**：
$$\frac{1}{(q;q)_\infty} = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n^2}$$
**背景**：将分拆函数的生成函数用 Durfee 方分解，是分拆理论的基本恒等式。
**后续**：Durfee 方方法成为分拆枚举的标准工具。

### [Q18] Ramanujan 的双和恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n(n+1)/2}}{(q;q)_n} = \prod_{n=1}^{\infty} \frac{1}{1-q^{2n-1}}$$
**背景**：将级数与奇数部分的乘积联系起来，等价于"奇分拆数等于自共轭分拆数"。
**后续**：Euler 分拆定理的推广。

### [Q19] Ramanujan 的 $_2\phi_1$ 变换
**公式**：
$$_2\phi_1\left[\begin{matrix} a, b \\ c \end{matrix}; q, \frac{c}{ab}\right] = \frac{(c/a, c/b; q)_\infty}{(c, c/(ab); q)_\infty} \cdot {}_2\phi_1\left[\begin{matrix} c/a, c/b \\ c \end{matrix}; q, ab\right]$$
**背景**：q-超几何级数的 Sears 变换，Ramanujan 在笔记中以隐含形式使用。
**后续**：Heine 变换的 q-模拟，现代 q-级数理论的基本工具。

### [Q20] Ramanujan 的模 5 乘积恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n} \cdot \sum_{n=0}^{\infty} \frac{q^{n^2+n}}{(q;q)_n} = \frac{1}{(q;q)_\infty} \sum_{n=-\infty}^{\infty} (-1)^n q^{n(5n+1)/2}$$
**背景**：将两个 Rogers-Ramanujan 级数的乘积与分拆函数联系起来。
**后续**：与 5 核分拆函数的枚举相关。

### [Q21] Ramanujan 的 q-Airy 恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}(-q;q^2)_n}{(q^2;q^2)_n} = \frac{(q^2;q^4)_\infty}{(q;q^2)_\infty}$$
**背景**：与 Ramanujan 的 mock theta 函数 $f(q)$ 有关的恒等式。
**后续**：与 Painlevé 方程和 q-Airy 函数有深层联系。

### [Q22] Ramanujan 的 q-Dixon 恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{(a;q)_n (b;q)_n}{(q;q)_n (abq;q)_n} (-1)^n q^{n(n-1)/2} = \frac{(a, b, q/(ab); q)_\infty}{(q/a, q/b, ab; q)_\infty}$$
**背景**：Dixon 定理的 q-模拟，Ramanujan 在笔记中给出。
**后续**：成为 q-组合恒等式的基本工具。

### [Q23] Ramanujan 的 q-Kummer 恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{1-aq^{2n}}{1-a} \frac{(b,c,d;q)_n}{(q, abq/c, abq/d;q)_n} \left(\frac{abq^2}{cd}\right)^n = \frac{(abq^2/cd, abq/c, abq/d, q, aq/cd; q)_\infty}{(abq^2/c, abq^2/d, q/c, q/d, aq; q)_\infty}$$
**背景**：Kummer 求和公式的 q-模拟，非常一般的求和公式。
**后续**：Gasper-Rahman 书中的核心公式之一。

### [Q24] Ramanujan 的模 10 恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n(2n+1)}}{(q;q^2)_{n+1}} = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q^2;q^2)_n}$$
**背景**：模 10 的 Rogers-Ramanujan 类型恒等式。
**后续**：与 5 阶 mock theta 函数的偶部分相关。

### [Q25] Ramanujan 的 Bailey 对生成恒等式
**公式**：
$$\sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n} (a;q)_n = (aq;q^2)_\infty \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q^2;q^2)_n}$$
**背景**：Ramanujan 在第二本笔记中给出的含参数恒等式，可生成多个 Rogers-Ramanujan 类型恒等式。
**后续**：Bailey 链理论的基础之一。

---

## 二、Theta 函数恒等式

### [T01] Ramanujan 的 $\phi$ 函数加法公式
**公式**：
$$\phi(q)\phi(-q) = \phi(-q^2)\phi(q^2) \cdot \frac{\phi(-q^4)}{\phi(-q^2)}$$
即 $\phi(q)\phi(-q) = \phi(-q^2)^2$（简化形式）
**背景**：Ramanujan 的 theta 函数 $\phi(q) = \sum q^{n^2}$ 的乘积关系。
**后续**：Jacobi theta 函数乘积公式的特例。

### [T02] Ramanujan 的 $\phi(q^5)$ 分解
**公式**：
$$\phi(q) = \phi(q^{25}) + 2q \frac{f(-q^{10}, -q^{15})}{f(-q^5, -q^{20})} + 2q^4 \psi(q^{25})$$
**背景**：将 $\phi(q)$ 按 $q^5$ 的幂次分解，是 5-核理论的基础。
**后续**：Atkin 用此类分解证明分拆函数的高阶同余式。

### [T03] Ramanujan 的 $\phi(q^7)$ 分解
**公式**：
$$\phi(q) = \phi(q^{49}) + 2q \frac{f(-q^{14}, -q^{21})}{f(-q^7, -q^{28})} + 2q^4 \psi(q^{49})$$
**背景**：与 [T02] 类似的模 7 分解。
**后续**：用于 $p(7n+5) \equiv 0 \pmod{7}$ 的证明。

### [T04] Ramanujan 的 $\psi$ 函数乘积公式
**公式**：
$$\psi(q) = \frac{(q^2;q^2)_\infty}{(q;q^2)_\infty}, \quad \psi(q)\psi(-q) = \psi(q^2)^2$$
**背景**：辅助 theta 函数 $\psi(q) = \sum_{n \geq 0} q^{n(n+1)/2}$ 的基本乘积关系。
**后续**：在分拆函数的 2-核理论中使用。

### [T05] Ramanujan 的 $f(a,b)$ 对称性
**公式**：
$$f(a,b) = f(b,a), \quad f(a,b) = a^{n(n+1)/2} b^{n(n-1)/2} f(a(ab)^n, b(ab)^{-n})$$
**背景**：Ramanujan 的一般 theta 函数 $f(a,b)$ 的基本对称性和变换性质。
**后续**：Berndt 在 *Notebooks* 中系统整理了这些变换。

### [T06] Ramanujan 的五重积恒等式
**公式**：
$$\prod_{n=1}^{\infty}(1-q^n)^5 = \sum_{n=-\infty}^{\infty} (-1)^{n+1}(2n+1)q^{n(3n+1)/2}$$
等价地：
$$f(-q)^5 = \sum_{n=-\infty}^{\infty} (-1)^n(2n+1)q^{n(3n+1)/2}$$
**背景**：Jacobi 五重积公式的 Ramanujan 形式，将 $(q;q)_\infty^5$ 与级数联系起来。
**后续**：Winquist 用此证明了 $p(11n+6) \equiv 0 \pmod{11}$。

### [T07] Ramanujan 的 $\phi(q)^5$ 公式
**公式**：
$$\phi(q)^5 = 1 + 5\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{(1-q^n)^2} \cdot \frac{q^n}{1-q^n} \cdot \phi(q^n)$$
**背景**：$\phi(q)$ 的五次幂的展开公式。
**后续**：与模形式的 Eisenstein 级数相关。

### [T08] Ramanujan 的 $\phi(q)^2$ 公式
**公式**：
$$\phi(q)^2 = \sum_{n=0}^{\infty} r_2(n) q^n = 1 + 4\sum_{n=0}^{\infty} \frac{(-1)^n q^{2n+1}}{1-q^{2n+1}}$$
**背景**：$\phi(q)^2$ 是两平方和表示数 $r_2(n)$ 的生成函数。
**后续**：Jacobi 两平方和定理的 theta 函数证明。

### [T09] Ramanujan 的 $\psi(q^2)$ 分解
**公式**：
$$\psi(q) = \psi(q^4) + q\psi(q^8) + q^3\psi(q^{16}) + \cdots$$
**背景**：将 $\psi(q)$ 按 2 的幂次递归分解。
**后续**：与二进制表示和 2-adic 分拆理论相关。

### [T10] Ramanujan 的 theta 函数模方程（5 阶）
**公式**：
$$\phi(q) = \phi(q^5) + 2q \frac{\psi(q^5)}{1 + R(q^5)^{-1}}$$
其中 $R(q)$ 是 Rogers-Ramanujan 连分数。
**背景**：将 theta 函数与 Rogers-Ramanujan 连分数联系起来的模方程。
**后续**：是 Ramanujan 模方程理论的核心之一。

### [T11] Ramanujan 的 $f(-q)$ 与 Eisenstein 级数关系
**公式**：
$$q \frac{d}{dq} \log f(-q) = -\sum_{n=1}^{\infty} \frac{nq^n}{1-q^n} = -\frac{1-E_2(q)}{24}$$
其中 $E_2(q) = 1 - 24\sum_{n=1}^{\infty} \sigma_1(n) q^n$。
**背景**：将 Dedekind eta 函数的导数与 Eisenstein 级数 $E_2$ 联系起来。
**后续**：模形式理论的基本关系。

### [T12] Ramanujan 的 $\phi(-q)$ 公式
**公式**：
$$\phi(-q) = \frac{f(-q)^2}{f(-q^2)} = (q;q)_\infty^2 / (q^2;q^2)_\infty$$
**背景**：$\phi(-q) = \sum (-1)^n q^{n^2}$ 的乘积表示。
**后续**：与模 4 的分拆理论相关。

### [T13] Ramanujan 的 theta 函数三重积（一般形式）
**公式**：
$$f(a,b) = (-a; ab)_\infty (-b; ab)_\infty (ab; ab)_\infty$$
**背景**：Jacobi 三重积恒等式的 Ramanujan 一般形式，是所有 theta 函数乘积公式的源头。
**后续**：现代 q-级数理论的基本工具。

### [T14] Ramanujan 的 $\phi(q)\phi(q^3)$ 公式
**公式**：
$$\phi(q)\phi(q^3) = \phi(q^6)\phi(q^2) + 2q\psi(q^6)\psi(q^2)$$
**背景**：两个 theta 函数乘积的分解，属于模 6 的恒等式。
**后续**：与模 6 的模方程相关。

### [T15] Ramanujan 的 $\psi(q)$ 与 $\phi(q)$ 关系
**公式**：
$$\phi(q) + \phi(-q) = 2\phi(q^4), \quad \phi(q) - \phi(-q) = 4q\psi(q^8)$$
**背景**：$\phi(q)$ 的偶奇分解，将 $\phi(q)$ 分裂为模 4 部分。
**后续**：在模方程推导中反复使用。

### [T16] Ramanujan 的 $f(-q)^3$ 公式
**公式**：
$$f(-q)^3 = \sum_{n=0}^{\infty} (-1)^n (2n+1) q^{n(n+1)/2}$$
**背景**：Jacobi 公式的 Ramanujan 形式，将 $(q;q)_\infty^3$ 与三角数级数联系起来。
**后续**：是三平方和表示数 $r_3(n)$ 的理论基础。

### [T17] Ramanujan 的 theta 函数模 3 恒等式
**公式**：
$$\phi(q)\phi(q^3) = 1 + 4\sum_{n=0}^{\infty} \frac{(-1)^n q^{2n+1}}{1+q^{2n+1}} \cdot \frac{q^{2n+1}}{1-q^{2(2n+1)}}$$
**背景**：模 3 的 theta 函数乘积展开。
**后续**：与模 3 的模形式相关。

---

## 三、模形式和 Mock Theta 函数

### [M01] 3 阶 mock theta 函数 $f(q)$
**公式**：
$$f(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(-q;q)_n^2} = 1 + 4\sum_{n=1}^{\infty} \frac{(-1)^n q^{n^2+2n}}{(1+q^n)^2}$$
**背景**：Ramanujan 在最后写给 Hardy 的信中定义的 3 阶 mock theta 函数之一。
**后续**：Andrews-Hickerson 给出了 Hecke-type 双和表示；Bringmann-Ono 用调和 Maass 形式理论解释。

### [M02] 3 阶 mock theta 函数 $\phi(q)$
**公式**：
$$\phi(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(-q;q^2)_n} = 1 + 2\sum_{n=1}^{\infty} \frac{q^{n^2}}{(1+q^{2n-1})}$$
**背景**：3 阶 mock theta 函数，注意此 $\phi(q)$ 与 theta 函数 $\phi(q)$ 记号冲突，但含义不同。
**后续**：其 shadow 是模 6 的半整权模形式。

### [M03] 3 阶 mock theta 函数 $\psi(q)$
**公式**：
$$\psi(q) = \sum_{n=1}^{\infty} \frac{q^{n^2}}{(q;q^2)_n} = \sum_{n=1}^{\infty} \frac{q^{n^2}}{(1-q)(1-q^3)\cdots(1-q^{2n-1})}$$
**背景**：3 阶 mock theta 函数。
**后续**：与 $\phi(q)$ 配对，两者之和给出模形式。

### [M04] 3 阶 mock theta 函数 $\chi(q)$
**公式**：
$$\chi(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(-q;q)_n} = 1 + \sum_{n=1}^{\infty} \frac{q^{n^2}}{(1+q)(1+q^2)\cdots(1+q^n)}$$
**背景**：3 阶 mock theta 函数。
**后续**：Watson 研究了 $\chi(q)$ 的变换性质。

### [M05] 3 阶 mock theta 函数 $\omega(q)$
**公式**：
$$\omega(q) = \sum_{n=0}^{\infty} \frac{q^{2n(n+1)}}{(q;q^2)_{n+1}^2}$$
**背景**：3 阶 mock theta 函数。
**后续**：Hickerson 证明 $\omega(q)$ 的系数满足模 4 的递推关系。

### [M06] 3 阶 mock theta 函数 $\nu(q)$
**公式**：
$$\nu(q) = \sum_{n=0}^{\infty} \frac{q^{n(n+1)}}{(-q;q^2)_{n+1}} = \sum_{n=0}^{\infty} \frac{q^{n(n+1)}}{(1+q)(1+q^3)\cdots(1+q^{2n+1})}$$
**背景**：3 阶 mock theta 函数。
**后续**：与 $\omega(q)$ 有线性关系。

### [M07] 3 阶 mock theta 函数 $\rho(q)$
**公式**：
$$\rho(q) = \sum_{n=0}^{\infty} \frac{q^{2n^2}}{(q;q^2)_{n+1}^2}$$
**背景**：3 阶 mock theta 函数。
**后续**：与 $\omega(q)$ 和 $\nu(q)$ 构成 3 阶 mock theta 函数的完整集合之一。

### [M08] 3 阶 mock theta 函数 $\mu(q)$
**公式**：
$$\mu(q) = \sum_{n=0}^{\infty} \frac{(-1)^n q^{n^2} (q;q^2)_n}{(-q;q)_{2n+1}}$$
**背景**：3 阶 mock theta 函数，Ramanujan 在信中定义。
**后续**：与 $\xi(q)$ 配对。

### [M09] 3 阶 mock theta 函数 $\xi(q)$
**公式**：
$$\xi(q) = \sum_{n=0}^{\infty} \frac{(-1)^n q^{n+1} (q;q^2)_n}{(-q;q)_{2n}}$$
**背景**：3 阶 mock theta 函数。
**后续**：Watson 证明了 $\mu(q)$ 和 $\xi(q)$ 的线性组合给出模形式。

### [M10] 5 阶 mock theta 函数 $f_0(q)$
**公式**：
$$f_0(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n}$$
**背景**：5 阶 mock theta 函数。注意形式上与 Rogers-Ramanujan 级数相似但分母不同。
**后续**：Andrews-Hickerson 1987 年系统研究了 5 阶 mock theta 函数。

### [M11] 5 阶 mock theta 函数 $f_1(q)$
**公式**：
$$f_1(q) = \sum_{n=0}^{\infty} \frac{q^{n^2+n}}{(q;q)_n}$$
**背景**：5 阶 mock theta 函数，与 $f_0(q)$ 配对。
**后续**：$f_0(q)$ 和 $f_1(q)$ 的线性组合给出 theta 函数。

### [M12] 5 阶 mock theta 函数 $\phi_0(q)$
**公式**：
$$\phi_0(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q^2)_{n+1}}$$
**背景**：5 阶 mock theta 函数。
**后续**：其系数有模 5 的渐近性质。

### [M13] 5 阶 mock theta 函数 $\psi_0(q)$
**公式**：
$$\psi_0(q) = \sum_{n=1}^{\infty} \frac{q^{n(n+1)/2}}{(q;q^2)_n}$$
**背景**：5 阶 mock theta 函数。
**后续**：与 $\phi_0(q)$ 配对。

### [M14] 5 阶 mock theta 函数 $F_0(q)$
**公式**：
$$F_0(q) = \sum_{n=0}^{\infty} \frac{q^{2n^2}}{(q;q^2)_{n+1}}$$
**背景**：5 阶 mock theta 函数，涉及偶数指数。
**后续**：与 $F_1(q)$ 配对。

### [M15] 5 阶 mock theta 函数 $F_1(q)$
**公式**：
$$F_1(q) = \sum_{n=0}^{\infty} \frac{q^{2n^2+2n}}{(q;q^2)_{n+1}}$$
**背景**：5 阶 mock theta 函数。
**后续**：Andrews-Hickerson 给出了 $F_0, F_1$ 的 Hecke-type 表示。

### [M16] 7 阶 mock theta 函数 $\mathcal{F}_0(q)$
**公式**：
$$\mathcal{F}_0(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}}{(q;q)_n^2}$$
**背景**：7 阶 mock theta 函数，Ramanujan 在信中给出。
**后续**：Hickerson 1988 年证明其系数满足模 7 的递推关系。

### [M17] 7 阶 mock theta 函数 $\mathcal{F}_1(q)$
**公式**：
$$\mathcal{F}_1(q) = \sum_{n=0}^{\infty} \frac{q^{n^2+2n}}{(q;q)_n^2}$$
**背景**：7 阶 mock theta 函数，与 $\mathcal{F}_0(q)$ 配对。
**后续**：Hickerson 的工作使 7 阶 mock theta 函数理论趋于完整。

### [M18] Mock theta 函数的阶（order）的定义
**公式**：Mock theta 函数 $f(q)$ 的"阶" $k$ 定义为：存在一个模 $k$ 的 theta 函数（权 1/2 的模形式）$g(q)$，使得在单位根 $\zeta$ 处 $f(q) - g(q)$ 有界（当 $q \to \zeta$ 径向趋近时）。
**背景**：Ramanujan 在给 Hardy 的最后一封信中用此概念区分不同 mock theta 函数，但未给出严格定义。Watson 1935 年给出了精确化。
**后续**：Zagier 2007 年给出了 mock theta 函数的现代定义（mock 模形式 = holomorphic part of harmonic Maass form），将"阶"与 level 联系起来。

### [M19] Ramanujan 的 10 阶 mock theta 函数
**公式**：
$$\Phi_{10}(q) = \sum_{n=0}^{\infty} \frac{q^{n^2+n}}{(-q;q)_n(q;q)_{n+1}}$$
**背景**：Ramanujan 在信中提到的偶数阶 mock theta 函数。
**后续**：Choi 推广了 10 阶 mock theta 函数族。

### [M20] Ramanujan 的 6 阶 mock theta 函数
**公式**：
$$\sigma_6(q) = \sum_{n=0}^{\infty} \frac{(-1)^n q^{n(n+1)/2}}{(-q;q)_n}$$
**背景**：6 阶 mock theta 函数，由 Andrews 和 Berndt 从笔记中整理。
**后续**：Berndt 与 Choi 系统研究了 6、8、10 阶 mock theta 函数。

### [M21] Ramanujan 的 8 阶 mock theta 函数
**公式**：
$$S_0(q) = \sum_{n=0}^{\infty} \frac{q^{n^2}(-q;q^2)_n}{(-q^2;q^2)_n}$$
**背景**：8 阶 mock theta 函数。
**后续**：Gordon-McIntosh 系统研究了 8 阶 mock theta 函数族。

### [M22] Ramanujan 的混合 mock theta 函数
**公式**：
$$M(q) = \frac{1}{(q;q)_\infty} \sum_{n=-\infty}^{\infty} (-1)^n q^{n(3n+1)/2} \cdot \frac{1}{1+q^n}$$
**背景**：Ramanujan 在笔记中给出的混合型 mock theta 函数，结合了 theta 函数和 mock theta 函数的特征。
**后续**：Bringmann-Folsom-Ono 系统研究了此类混合对象。

---

## 四、分拆函数恒等式

### [P01] 分拆函数同余式 $p(5n+4) \equiv 0 \pmod{5}$
**公式**：
$$\sum_{n=0}^{\infty} p(5n+4) q^n = 5 \frac{(q^5;q^5)_\infty^5}{(q;q)_\infty^6}$$
**背景**：Ramanujan 最著名的分拆函数同余式之一，1919 年发现。
**后续**：Atkin 推广到 $p(5^k n + \delta_k) \equiv 0 \pmod{5^k}$。

### [P02] 分拆函数同余式 $p(7n+5) \equiv 0 \pmod{7}$
**公式**：
$$\sum_{n=0}^{\infty} p(7n+5) q^n = 7 \frac{(q^7;q^7)_\infty^3}{(q;q)_\infty^4} + 49q \frac{(q^7;q^7)_\infty^7}{(q;q)_\infty^8}$$
**背景**：Ramanujan 第二个著名同余式。
**后续**：Atkin 推广到 $p(7^k n + \delta_k) \equiv 0 \pmod{7^k}$。

### [P03] 分拆函数同余式 $p(11n+6) \equiv 0 \pmod{11}$
**公式**：
$$\sum_{n=0}^{\infty} p(11n+6) q^n = 11 \frac{(q^{11};q^{11})_\infty^2}{(q;q)_\infty^3} + 121q \frac{(q^{11};q^{11})_\infty^4}{(q;q)_\infty^4} + \cdots$$
**背景**：Ramanujan 第三个著名同余式，证明最为困难。
**后续**：Atkin 推广到 $p(11^k n + \delta_k) \equiv 0 \pmod{11^k}$；Winquist 给出了基于五重积的证明。

### [P04] 分拆函数的生成函数
**公式**：
$$\sum_{n=0}^{\infty} p(n) q^n = \frac{1}{(q;q)_\infty} = \prod_{n=1}^{\infty} \frac{1}{1-q^n}$$
**背景**：Euler 的经典结果，Ramanujan 以此为出发点发展了整个分拆理论。
**后续**：这是整个分拆函数理论的基石。

### [P05] Hardy-Ramanujan 渐近公式
**公式**：
$$p(n) \sim \frac{1}{4n\sqrt{3}} \exp\left(\pi \sqrt{\frac{2n}{3}}\right) \quad (n \to \infty)$$
**背景**：1918 年 Hardy 和 Ramanujan 用圆法得到的分拆函数渐近公式，是解析数论的里程碑。
**后续**：Rademacher 1937 年改进为精确收敛级数。

### [P06] Rademacher 级数（Ramanujan 的预示）
**公式**：
$$p(n) = \frac{1}{\pi\sqrt{2}} \sum_{k=1}^{\infty} A_k(n) \sqrt{k} \frac{d}{dn}\left(\frac{\sinh\left(\frac{\pi}{k}\sqrt{\frac{2}{3}(n-\frac{1}{24})}\right)}{\sqrt{n-\frac{1}{24}}}\right)$$
其中 $A_k(n) = \sum_{0 \leq h < k, \gcd(h,k)=1} e^{\pi i s(h,k) - 2\pi i nh/k}$，$s(h,k)$ 是 Dedekind 和。
**背景**：Ramanujan 的方法被 Rademacher 改进为精确收敛的级数。Ramanujan 原始方法中已包含此级数的雏形。
**后续**：Selberg 给出了简化证明；Bruinier-Ono 给出了基于调和 Maass 形式的现代版本。

### [P07] Ramanujan 的 $p(n)$ 生成函数的 5-核分解
**公式**：
$$\frac{1}{(q;q)_\infty} = \frac{(q^5;q^5)_\infty^4}{(q;q)_\infty^5} \cdot \left[\frac{(q;q)_\infty^5}{(q^5;q^5)_\infty}\right]$$
其中方括号内可用 Ramanujan 的五重积展开。
**背景**：将分拆生成函数按 5-核分解，是证明 $p(5n+4) \equiv 0 \pmod 5$ 的关键。
**后续**：Atkin 的 $U_\ell$ 算子理论的基础。

### [P08] Ramanujan 的 $p(5^2 n + 24) \equiv 0 \pmod{25}$
**公式**：
$$p(25n+24) \equiv 0 \pmod{25}$$
**背景**：Ramanujan 预言了 $p(5^k n + \delta_k) \equiv 0 \pmod{5^k}$ 对所有 $k$ 成立。
**后续**：Atkin 1967 年用 $U_\ell$ 算子证明了对所有素数幂 $\ell^k$ 的推广。

### [P09] Ramanujan 的 crank 概念
**公式**：Ramanujan 在笔记中暗示存在一个分拆统计量 $\text{crank}(\lambda)$，使得分拆按 crank 值模 5 的类恰好解释 $p(5n+4) \equiv 0 \pmod 5$。
**背景**：Ramanujan 在 1919 年的笔记中提到了 crank 的存在，但未给出定义。
**后续**：Andrews 和 Garvan 1988 年发现了 crank 的精确定义：$\text{crank}(\lambda) = $ 最大部分 $-$ 部分数（当最大部分 $\neq$ 部分数时），否则为最大部分数 $-$ 最小重复部分数。

### [P10] Ramanujan 的 $t(n)$ 同余式
**公式**：设 $t(n)$ 为 $n$ 的三角数分拆数（即 $n$ 的分拆中 Durfee 方恰好为 $k \times k$ 且 $n - k^2$ 为三角数的分拆数），则
$$t(5n+4) \equiv 0 \pmod 5$$
**背景**：Ramanujan 在第三本笔记中研究了一类与分拆相关的函数的同余式。
**后续**：Kim 推广了此类结果。

### [P11] Ramanujan 的分拆函数模 2 同余式
**公式**：
$$p(2n) \equiv p(2n+1) \pmod{2}$$
等价地，$p(n)$ 模 2 的序列满足某种对称性。
**背景**：Ramanujan 注意到分拆函数模 2 的模式。
**后续**：Ono 2000 年证明了分拆函数模任意素数 $m$ 存在无穷多同余式。

### [P12] Ramanujan 的 $p(n)$ 模 13 同余式
**公式**：
$$p(13n+6) \equiv 0 \pmod{13}$$
**背景**：Ramanujan 在笔记中暗示了此同余式但未明确写出。后来被确认为 Ramanujan 类型的同余式。
**后续**：Ono 证明了对任意与 1 互素的 $m$，存在无穷多 $a, b$ 使得 $p(an+b) \equiv 0 \pmod m$。

### [P13] Ramanujan 的 $p(n)$ 的 5-核生成函数
**公式**：
$$\sum_{n=0}^{\infty} p(5n+4) q^n = 5 \prod_{n=1}^{\infty} \frac{(1-q^{5n})^5}{(1-q^n)^6}$$
**背景**：这是 [P01] 的精确生成函数形式，直接给出 $p(5n+4) \equiv 0 \pmod 5$。
**后续**：此公式的结构启发了 Ramanujan 对 $p(7n+5)$ 和 $p(11n+6)$ 的类似分析。

### [P14] Ramanujan 的分拆函数的 5-dissection
**公式**：
$$\frac{1}{(q;q)_\infty} = \frac{(q^5;q^5)_\infty^4}{(q;q)_\infty^5} \left[\frac{1}{(q^5;q^5)_\infty} + q \cdot R_1(q^5) + q^2 \cdot R_2(q^5) + q^3 \cdot R_3(q^5) + q^4 \cdot R_4(q^5)\right]$$
其中 $R_i$ 是具体的 q-级数。
**背景**：将分拆生成函数按 $q$ 的幂次模 5 分解。
**后续**：Atkin 的 $U$-算子和 $V$-算子理论的模型。

### [P15] Ramanujan 的 $p(n)$ 精确公式（预示）
**公式**：Ramanujan 给出了 $p(n)$ 的近似公式
$$p(n) \approx \frac{1}{4n\sqrt{3}} \left(e^{\pi\sqrt{2n/3}} - e^{-\pi\sqrt{2n/3}}\right)$$
并指出可以加上更多项以获得精确值。
**背景**：这是 Hardy-Ramanujan 圆法的直接产物，第一项已给出极好的近似。
**后续**：Rademacher 将此发展为精确收敛级数。

### [P16] Ramanujan 的分拆函数与 Eisenstein 级数关系
**公式**：
$$\sum_{n=1}^{\infty} p(n) q^n = \frac{1}{(q;q)_\infty}, \quad q\frac{d}{dq}\log\frac{1}{(q;q)_\infty} = \sum_{n=1}^{\infty} \sigma_1(n) q^n$$
**背景**：将分拆函数的对数导数与除数函数 $\sigma_1(n)$ 联系起来。
**后续**：这是模形式理论中 $E_2$ 与 eta 函数关系的基础。

### [P17] Ramanujan 的 $p(n)$ 模 3 同余式
**公式**：
$$p(3n) \equiv 0 \pmod{3} \quad \text{当 } n \not\equiv 0 \pmod{3}$$
更精确地，$p(3n) \equiv (-1)^n \pmod 3$ 当 $n$ 为某些特定值。
**背景**：Ramanujan 研究了分拆函数模小素数的模式。
**后续**：Atkin 给出了模 3 的完整理论。

---

## 五、连分数恒等式

### [C01] Rogers-Ramanujan 连分数的乘积表示
**公式**：
$$R(q) = q^{1/5} \frac{(q;q^5)_\infty (q^4;q^5)_\infty}{(q^2;q^5)_\infty (q^3;q^5)_\infty}$$
**背景**：Ramanujan 发现了 Rogers-Ramanujan 连分数的无穷乘积表示，这是连分数与乘积之间的深刻联系。
**后续**：此公式由 Rogers 首证，Ramanujan 独立发现并推广。

### [C02] Rogers-Ramanujan 连分数在 $q = e^{-2\pi}$ 处的值
**公式**：
$$R(e^{-2\pi}) = \sqrt{\frac{5+\sqrt{5}}{2}} - \frac{\sqrt{5}+1}{2}$$
**背景**：Ramanujan 在信中给出了 $R(q)$ 在特殊点的代数值，这些值涉及黄金比例。
**后续**：Andrews-Berndt 系统研究了 $R(q)$ 在各种单位根处的值。

### [C03] Ramanujan-Göllnitz-Gordon 连分数
**公式**：
$$H(q) = \frac{q^{1/2}}{1+q+\frac{q^2}{1+q^3+\frac{q^4}{1+q^5+\cdots}}}$$
**背景**：Ramanujan 在第二本笔记中研究的连分数，与 8 阶 mock theta 函数相关。
**后续**：Göllnitz 和 Gordon 独立研究了此连分数并给出了分拆解释。

### [C04] Ramanujan 的三次连分数
**公式**：
$$G(q) = \frac{q^{1/3}}{1+q+q^2+\frac{q^3}{1+q^3+q^6+\frac{q^6}{1+q^6+q^{12}+\cdots}}}$$
**背景**：Ramanujan 研究的三次连分数，与模 3 的理论相关。
**后续**：Berndt 等人研究了 $G(q)$ 的变换性质。

### [C05] Ramanujan 连分数的模方程
**公式**：若 $R(q)$ 为 Rogers-Ramanujan 连分数，则
$$\frac{1}{R(q)^5} - 11 - R(q)^5 = \frac{f(-q)^6}{q \cdot f(-q^5)^6}$$
**背景**：将 Rogers-Ramanujan 连分数与 eta 函数联系起来的恒等式。
**后续**：此公式是推导 $R(q)$ 的模方程的基础。

### [C06] Ramanujan 的 $R(q)$ 与 $R(q^5)$ 的关系
**公式**：
$$R(q) = R(q^5) \cdot \frac{1 + q R(q^5)^{-1}}{1 + q R(q^5)}$$
**背景**：Rogers-Ramanujan 连分数的五阶变换公式。
**后续**：此类变换公式是 Ramanujan 模方程理论的核心。

### [C07] Ramanujan 的双连分数恒等式
**公式**：
$$\frac{1}{1+\frac{a}{1+\frac{a^2}{1+\cdots}}} \cdot \frac{1}{1+\frac{b}{1+\frac{b^2}{1+\cdots}}} = \frac{1}{1+\frac{a+b}{1+\frac{ab(a+b)}{1+\cdots}}}$$
（当 $a, b$ 满足特定关系时）
**背景**：Ramanujan 在第一本笔记中给出的连分数乘积恒等式。
**后续**：与多重连分数和 q-连分数理论相关。

### [C08] Ramanujan 的 $e$ 的连分数
**公式**：
$$e = 2 + \frac{1}{1+\frac{1}{2+\frac{1}{1+\frac{1}{1+\frac{1}{4+\cdots}}}}}$$
更一般地，Ramanujan 给出了 $e^{1/n}$ 的连分数展开。
**背景**：Ramanujan 对 $e$ 和指数函数的连分数展开有深入研究。
**后续**：Perron 在其连分数专著中收录了 Ramanujan 的多个连分数公式。

### [C09] Ramanujan 的 $\pi$ 的连分数
**公式**：
$$\frac{4}{\pi} = 1 + \frac{1^2}{2+\frac{3^2}{2+\frac{5^2}{2+\frac{7^2}{2+\cdots}}}}$$
**背景**：Ramanujan 给出的 $\pi$ 的连分数表示，与奇数平方相关。
**后续**：此连分数与 Bauer-Muir 变换和 Stern-Stolz 定理相关。

### [C10] Ramanujan 的一般连分数变换
**公式**：设
$$F(a,b,\lambda) = \frac{a}{1+\frac{b\lambda}{1+\frac{b\lambda^2}{1+\frac{a\lambda^3}{1+\cdots}}}}$$
则 $F(a,b,\lambda) = F(b,a,\lambda)$ 当 $a\lambda = b$ 时。
**背景**：Ramanujan 的一般连分数对称性定理，是连分数理论中的深刻结果。
**后续**：Berndt 在 *Notebooks* 中验证并推广了此结果。

### [C11] Ramanujan 的连分数与椭圆积分关系
**公式**：
$$R(q) = q^{1/5} \exp\left(-\sum_{n=1}^{\infty} \frac{(-1)^n L(n)}{n} q^n\right)$$
其中 $L(n)$ 是 Dirichlet L-函数。
**背景**：将 Rogers-Ramanujan 连分数与 Dirichlet L-函数联系起来。
**后续**：与模形式的对数导数相关。

---

## 六、代数恒等式和根式

### [A01] Ramanujan 的嵌套根式
**公式**：
$$\sqrt[3]{\sqrt[3]{2}-1} = \sqrt[3]{\frac{1}{9}} - \sqrt[3]{\frac{2}{9}} + \sqrt[3]{\frac{4}{9}}$$
**背景**：Ramanujan 在笔记中给出的优美嵌套根式恒等式，展示了立方根之间的代数关系。
**后续**：此类恒等式与三次域的类域论相关。

### [A02] Ramanujan 的根式恒等式（5 次方）
**公式**：
$$\sqrt[5]{\sqrt[5]{\frac{1}{2}} - \sqrt[5]{\frac{1}{8}}} = \sqrt[5]{\frac{1}{32}} + \sqrt[5]{\frac{1}{16}} - \sqrt[5]{\frac{1}{2}}$$
**背景**：Ramanujan 给出的 5 次根式的代数恒等式。
**后续**：与 5 次域和正二十面体对称性相关。

### [A03] Ramanujan 的 $\pi$ 的级数公式
**公式**：
$$\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)!(1103+26390n)}{(n!)^4 396^{4n}}$$
**背景**：Ramanujan 最著名的公式之一，每项给出约 8 位有效数字。1914 年在剑桥期间发表。
**后续**：Chudnovsky 兄弟和 Borwein 兄弟推广了此类公式，用于计算 $\pi$ 的数万亿位。

### [A04] Ramanujan 的 $\pi$ 级数（模 7 版本）
**公式**：
$$\frac{1}{\pi} = \frac{3\sqrt{3}}{2} \sum_{n=0}^{\infty} \frac{(3n)!(2n)!}{(n!)^5} \frac{(6n+1)}{(4/3)^{3n}}$$
**背景**：Ramanujan 给出的另一个 $\pi$ 的快速收敛级数。
**后续**：Borwein 兄弟系统分类了此类级数。

### [A05] Ramanujan 的 3-7-15 恒等式
**公式**：
$$\left(\sqrt[3]{\frac{1}{2}(7+\sqrt{5})} - \sqrt[3]{\frac{1}{2}(7-\sqrt{5})}\right)^3 = 3\sqrt[3]{\frac{1}{2}(7+\sqrt{5})} - 3\sqrt[3]{\frac{1}{2}(7-\sqrt{5})} - 5$$
**背景**：Ramanujan 的嵌套立方根恒等式，展示了代数数的深层关系。
**后续**：与三次方程的根式解相关。

### [A06] Ramanujan 的完全对称三次恒等式
**公式**：若 $\alpha, \beta, \gamma$ 满足 $\alpha+\beta+\gamma=0$ 且 $\alpha\beta\gamma = \delta$，则
$$(\alpha^{1/3}+\beta^{1/3}+\gamma^{1/3})^3 = 3(\alpha^{1/3}\beta^{1/3}+\beta^{1/3}\gamma^{1/3}+\gamma^{1/3}\alpha^{1/3}) + 3\delta^{1/3}$$
**背景**：Ramanujan 给出的对称三次根式恒等式。
**后续**：Berndt 在 *Notebooks* 中验证了此恒等式。

### [A07] Ramanujan 的椭圆模方程（5 阶）
**公式**：设 $K(k)$ 为第一类完全椭圆积分，$k, l$ 为模，若
$$n = \frac{K'(k)^2}{K(k)^2} = 5 \frac{K'(l)^2}{K(l)^2}$$
则 $k$ 和 $l$ 之间存在一个 5 次代数关系（模方程）。
**背景**：Ramanujan 系统研究了各阶模方程，5 阶模方程是他最深入研究的之一。
**后续**：Ramanujan 的模方程是计算 $\pi$ 级数的理论基础。

### [A08] Ramanujan 的 5 阶模方程显式形式
**公式**：
$$(\alpha\beta)^{1/2} + ((1-\alpha)(1-\beta))^{1/2} + 2\left[16\alpha\beta(1-\alpha)(1-\beta)\right]^{1/6} = 1$$
其中 $\alpha = k^2, \beta = l^2$ 且 $K'(l)/K(l) = 5 K'(k)/K(k)$。
**背景**：5 阶模方程的显式代数关系。
**后续**：Berndt-Bhargava 在 1990 年代系统验证了 Ramanujan 的模方程。

### [A09] Ramanujan 的代数恒等式（4 次方）
**公式**：
$$(a+b+c+d)^4 = a^4+b^4+c^4+d^4 + 4(a+b)(a+c)(a+d)(b+c)(b+d)(c+d) \cdot \frac{1}{(a+b+c+d)^2}$$
（当 $a+b+c+d \neq 0$ 时）
**背景**：Ramanujan 在笔记中给出的对称四次恒等式。
**后续**：与 Euler 四次恒等式和 Waring 问题相关。

### [A10] Ramanujan 的 $1/\pi$ 的一般公式
**公式**：
$$\frac{1}{\pi} = \sum_{n=0}^{\infty} \frac{(a)_n (b)_n (c)_n}{(d)_n (e)_n n!} (A + Bn) z^n$$
其中参数 $a, b, c, d, e, A, B, z$ 满足特定的超几何关系。
**背景**：Ramanujan 给出了 17 个此类公式，涉及不同的超几何级数参数。
**后续**：Borwein-Borwein 和 Chudnovsky 系统推导了此类公式的理论基础。

---

## 七、级数求和公式

### [S01] Ramanujan 的 $\sum 1/n^2$ 类恒等式
**公式**：
$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$$
Ramanujan 在笔记中给出了此经典结果的多个推广。
**背景**：Basel 问题的 Ramanujan 推广。
**后续**：Ramanujan 推广到 $\sum 1/\sinh^2(n\pi)$ 等双曲函数级数。

### [S02] Ramanujan 的双曲级数求和
**公式**：
$$\sum_{n=1}^{\infty} \frac{1}{\sinh^2(n\pi)} = \frac{1}{6} - \frac{1}{2\pi}$$
**背景**：Ramanujan 将经典级数 $\sum 1/n^2 = \pi^2/6$ 推广到双曲函数。
**后续**：与模形式的特殊值相关。

### [S03] Ramanujan 的 $\coth$ 级数
**公式**：
$$\sum_{n=1}^{\infty} \frac{n}{e^{2\pi n}-1} = \frac{1}{24} - \frac{1}{8\pi}$$
**背景**：与 Eisenstein 级数 $E_2$ 在 $q = e^{-2\pi}$ 处的值相关。
**后续**：模形式特殊值的计算。

### [S04] Ramanujan 的 $\sigma_1$ 级数
**公式**：
$$\sum_{n=1}^{\infty} \frac{n^3}{e^{2\pi n}-1} = \frac{1}{240} - \frac{3}{16\pi^2} \cdot \frac{\Gamma(1/4)^8}{(2\pi)^6}$$
**背景**：与 Eisenstein 级数 $E_4$ 的特殊值相关。
**后续**：与椭圆函数和模形式的特殊值计算相关。

### [S05] Ramanujan 的交错级数求和
**公式**：
$$1 - \frac{1}{4} + \frac{1}{9} - \frac{1}{16} + \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^2} = \frac{\pi^2}{12}$$
**背景**：Ramanujan 给出了此经典结果的多个推广形式。
**后续**：与 Dirichlet eta 函数 $\eta(2) = \pi^2/12$ 相关。

### [S06] Ramanujan 的超几何级数求和
**公式**：
$$_2F_1\left[\begin{matrix} a, -a \\ 1/2 \end{matrix}; \sin^2 x\right] = \cos(2ax)$$
**背景**：超几何级数与三角函数的恒等式。
**后续**：是 Clausen 恒等式和超几何函数理论的基础。

### [S07] Ramanujan 的 $\Gamma(1/4)$ 级数
**公式**：
$$\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^4} = \frac{5\pi^4}{1536} \cdot \frac{\Gamma(1/4)^8}{\pi^6}$$
（更精确地，$\beta(4) = \frac{\psi_3(1/4)}{4^4}$ 涉及 $\Gamma(1/4)$）
**背景**：Dirichlet beta 函数在 $s=4$ 的值，Ramanujan 给出了与 $\Gamma(1/4)$ 的关系。
**后续**：与椭圆积分和模形式的特殊值相关。

### [S08] Ramanujan 的部分分式级数
**公式**：
$$\sum_{n=0}^{\infty} \frac{1}{(n+a)(n+b)} = \frac{\psi(a) - \psi(b)}{a - b}$$
其中 $\psi$ 是 digamma 函数。
**背景**：Ramanujan 系统使用了 digamma 函数的级数表示。
**后续**：在 Ramanujan 的 $\pi$ 级数推导中使用。

### [S09] Ramanujan 的 $\zeta(2k+1)$ 快速收敛级数
**公式**：
$$\zeta(3) = \frac{7\pi^3}{180} - 2\sum_{n=1}^{\infty} \frac{1}{n^3(e^{2\pi n}-1)}$$
**背景**：Ramanujan 给出了 $\zeta(2k+1)$ 的快速收敛级数表示，利用了双曲函数。
**后续**：Apéry 1978 年证明 $\zeta(3)$ 无理数时使用了相关技术。

### [S10] Ramanujan 的 $\zeta(4m+3)$ 公式
**公式**：
$$\zeta(4m+3) = \frac{2(2\pi)^{4m+3}}{(4m+2)!} \sum_{j=0}^{m+1} (-1)^{j+1} \frac{B_{2j}}{(2j)!} \frac{B_{4m+4-2j}}{(4m+4-2j)!} - 2\sum_{n=1}^{\infty} \frac{1}{n^{4m+3}(e^{2\pi n}-1)}$$
其中 $B_k$ 是 Bernoulli 数。
**背景**：Ramanujan 给出了 $\zeta(4m+3)$ 的一般公式，将 zeta 函数值与 Bernoulli 数和快速收敛级数联系起来。
**后续**：Rivoal 2002 年用此类公式证明 $\zeta(2k+1)$ 中有无穷多个无理数。

### [S11] Ramanujan 的 $\pi$ 的 Chudnovsky 型级数
**公式**：
$$\frac{1}{\pi} = 12 \sum_{n=0}^{\infty} (-1)^n \frac{(6n)!(A + Bn)}{(3n)!(n!)^3 C^{n+1/2}}$$
其中 $A, B, C$ 为特定常数。
**背景**：Ramanujan 给出的 $\pi$ 级数的一般形式，Chudnovsky 兄弟将其具体化。
**后续**：Chudnovsky 算法用于计算 $\pi$ 的世界纪录。

---

## 八、不等式和逼近

### [I01] Ramanujan 的 $\pi$ 逼近
**公式**：
$$\pi \approx \frac{9}{5} + \sqrt{\frac{9}{5}} = \frac{9}{5} + \frac{3}{\sqrt{5}} \approx 3.14164\ldots$$
**背景**：Ramanujan 给出的 $\pi$ 的简单代数逼近，精度约 $10^{-4}$。
**后续**：Ramanujan 给出了大量 $\pi$ 的有理和代数逼近。

### [I02] Ramanujan 的 $e^\pi$ 逼近
**公式**：
$$e^\pi \approx \frac{e^3 + 6e^2 + 15e + 20}{20} \approx 23.14069\ldots$$
**背景**：Ramanujan 给出的 $e^\pi$ 的有理函数逼近。
**后续**：与 $e^\pi - \pi \approx 20$ 的近似有关。

### [I03] Ramanujan 的 $e^\pi - \pi \approx 20$ 恒等式
**公式**：
$$e^\pi - \pi \approx 19.9991\ldots \approx 20$$
**背景**：Ramanujan 注意到的近似整数现象，$e^\pi - \pi$ 非常接近 20。
**后续**：此类"近整数"现象与 j-函数的特殊值和 monstrous moonshine 相关。

### [I04] Ramanujan 的 $e^{\pi\sqrt{163}}$ 近整数
**公式**：
$$e^{\pi\sqrt{163}} \approx 262537412640768743.99999999999925\ldots$$
**背景**：Ramanujan 指出 $e^{\pi\sqrt{163}}$ 非常接近一个整数。这与 $j$-函数在 $\tau = (1+\sqrt{-163})/2$ 处的值为整数 $640320^3$ 相关。
**后续**：Heegner 数 163 的理论；Conway 称此为"Ramanujan 的魔术"。

### [I05] Ramanujan 的 Stirling 级数改进
**公式**：
$$n! \approx \sqrt{\pi} \left(\frac{n}{e}\right)^n (8n^3+4n^2+n+\theta_n)^{1/6}$$
其中 $\theta_n \to 1/30$ 当 $n \to \infty$。
**背景**：Ramanujan 对 Stirling 公式的改进，给出了更精确的阶乘逼近。
**后续**：Windschitl 和 Gosper 进一步改进了此公式。

### [I06] Ramanujan 的 $\Gamma$ 函数不等式
**公式**：
$$\Gamma(x+1) \approx \sqrt{\pi} \left(\frac{x}{e}\right)^x (8x^3+4x^2+x+1/30)^{1/6}$$
**背景**：Ramanujan 给出的 Gamma 函数逼近，比 Stirling 公式更精确。
**后续**：被用于高精度数值计算。

### [I07] Ramanujan 的 $\sqrt[n]{n!}$ 逼近
**公式**：
$$\sqrt[n]{n!} \approx \frac{n}{e} + \frac{1}{2e} + \frac{1}{24en} + \cdots$$
**背景**：Ramanujan 给出的 $n!$ 的 $n$ 次根的渐近展开。
**后续**：与 Stirling 公式的对数版本相关。

### [I08] Ramanujan 的 Bernoulli 数不等式
**公式**：
$$|B_{2n}| \sim \frac{2(2n)!}{(2\pi)^{2n}} \quad (n \to \infty)$$
Ramanujan 给出了更精确的界：
$$|B_{2n}| = \frac{2(2n)!}{(2\pi)^{2n}} \left(1 + O(4^{-n})\right)$$
**背景**：Bernoulli 数的渐近行为。
**后续**：与 zeta 函数在偶数处的值相关。

### [I09] Ramanujan 的 $\pi$ 的有理逼近界
**公式**：Ramanujan 证明了存在无穷多有理数 $p/q$ 使得
$$\left|\pi - \frac{p}{q}\right| < \frac{1}{q^8}$$
（这比 Dirichlet 的 $1/q^2$ 界强得多，但比 Mahler 的结果弱。）
**背景**：Ramanujan 对 $\pi$ 的无理性度量有深入研究。
**后续**：Mahler 1953 年给出了 $\pi$ 的更精确无理性度量。

### [I10] Ramanujan 的 $n!$ 的界
**公式**：
$$\sqrt{2\pi} \, n^{n+1/2} e^{-n} < n! < \sqrt{2\pi} \, n^{n+1/2} e^{-n} \left(1 + \frac{1}{12n}\right)$$
**背景**：Ramanujan 给出的 Stirling 公式的上下界。
**后续**：Robbins 1955 年给出了类似的界，但 Ramanujan 的版本更早。

### [I11] Ramanujan 的 $\cos$ 乘积逼近
**公式**：
$$\cos x \approx 1 - \frac{4x^2}{\pi^2} \cdot \frac{1}{1+\frac{4x^2}{\pi^2-4x^2}}$$
**背景**：Ramanujan 给出的余弦函数的有理逼近。
**后续**：与 Padé 逼近和连分数逼近相关。

---

## 九、其他

### [O01] Ramanujan 的 tau 函数 $\tau(n)$
**公式**：
$$\sum_{n=1}^{\infty} \tau(n) q^n = q \prod_{n=1}^{\infty}(1-q^n)^{24} = \eta(\tau)^{24}$$
其中 $q = e^{2\pi i \tau}$。
**背景**：Ramanujan 定义了 tau 函数 $\tau(n)$，即 $\Delta$ 判别式模形式的系数。
**后续**：Mordell 证明了 $\tau$ 是乘性的；Deligne 1974 年证明了 Ramanujan 猜想 $|\tau(p)| \leq 2p^{11/2}$。

### [O02] Ramanujan 的 tau 函数同余式
**公式**：
$$\tau(n) \equiv \sigma_{11}(n) \pmod{691}$$
**背景**：Ramanujan 发现的 tau 函数与除数函数之间的同余式。
**后续**：这是模形式 Galois 表示理论的起点之一。

### [O03] Ramanujan 的 tau 函数乘性
**公式**：
$$\tau(mn) = \tau(m)\tau(n) \quad \text{当 } \gcd(m,n)=1$$
$$\tau(p^{n+2}) = \tau(p)\tau(p^{n+1}) - p^{11}\tau(p^n)$$
**背景**：Ramanujan 猜想 tau 函数的乘性和递推关系。
**后续**：Mordell 1920 年证明；这是 Hecke 算子理论的起点。

### [O04] Ramanujan 的高度合成数
**公式**：Ramanujan 定义高度合成数 $N$ 为：对于所有 $M < N$，$d(M) < d(N)$，其中 $d(n)$ 是除数函数。
前几个高度合成数为：1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, ...
**背景**：Ramanujan 1915 年发表的论文系统研究了高度合成数。
**后续**：Alaoglu 和 Erdős 1944 年推广为超级高度合成数；与素数分布相关。

### [O05] Ramanujan 的高度合成数的渐近公式
**公式**：若 $N$ 为高度合成数，则
$$\log d(N) \sim \frac{\log N \cdot \log 2}{\log\log N}$$
**背景**：Ramanujan 给出了高度合成数除数个数的渐近公式。
**后续**：这是解析数论中除数函数极大值阶的经典结果。

### [O06] Ramanujan 的素数计数函数逼近
**公式**：
$$\pi(x) \sim \text{Li}(x) = \int_2^x \frac{dt}{\log t}$$
Ramanujan 给出了更精确的修正项。
**背景**：Ramanujan 在给 Hardy 的信中讨论了素数定理和 $\pi(x)$ 的逼近。
**后续**：Hardy 在 *Twelve Lectures* 中讨论了 Ramanujan 的素数工作。

### [O07] Ramanujan 的 Bernoulli 数生成函数
**公式**：
$$\frac{x}{e^x - 1} = \sum_{n=0}^{\infty} B_n \frac{x^n}{n!}$$
Ramanujan 在笔记中大量使用 Bernoulli 数，并给出了多个相关恒等式。
**背景**：Bernoulli 数在 Ramanujan 的 $\zeta$ 函数公式和 $\pi$ 级数中反复出现。
**后续**：与 Euler-Maclaurin 求和公式和模形式理论相关。

### [O08] Ramanujan 的 $\sigma_k(n)$ 恒等式
**公式**：
$$\sum_{n=1}^{\infty} \sigma_k(n) q^n = \sum_{n=1}^{\infty} \frac{n^k q^n}{1-q^n}$$
**背景**：除数函数 $\sigma_k(n) = \sum_{d|n} d^k$ 的生成函数。
**后续**：与 Eisenstein 级数 $E_{2k}$ 的关系：$E_{2k} = 1 - \frac{4k}{B_{2k}} \sum \sigma_{2k-1}(n) q^n$。

### [O09] Ramanujan 的 Jacobi 四平方和定理
**公式**：
$$\phi(q)^4 = \sum_{n=0}^{\infty} r_4(n) q^n = 1 + 8\sum_{n=1}^{\infty} \frac{(-1)^{n-1} n^3 q^n}{1-q^n}$$
即 $r_4(n) = 8\sum_{d|n, 4\nmid d} d^3$。
**背景**：Jacobi 四平方和定理的 Ramanujan theta 函数形式。
**后续**：与模 4 的表示数理论相关。

### [O10] Ramanujan 的椭圆函数恒等式
**公式**：
$$K(k) = \frac{\pi}{2} \sum_{n=0}^{\infty} \left(\frac{(2n)!}{2^{2n}(n!)^2}\right)^2 k^{2n} = \frac{\pi}{2} \, {}_2F_1\left(\frac{1}{2}, \frac{1}{2}; 1; k^2\right)$$
**背景**：第一类完全椭圆积分的超几何级数表示，Ramanujan 以此为基础发展了椭圆函数理论。
**后续**：Ramanujan 的模方程理论建立在此公式之上。

### [O11] Ramanujan 的 $K'/K$ 与 theta 函数关系
**公式**：
$$\frac{K'(k)}{K(k)} = \frac{\pi}{\log(1/q)} \quad \text{其中 } q = e^{-\pi K'(k)/K(k)}$$
等价地，$k$ 由 nome $q$ 决定：$k = \theta_2^2(q)/\theta_3^2(q)$。
**背景**：将椭圆积分比与 theta 函数的 nome 联系起来。
**后续**：这是 Ramanujan 模方程和 $\pi$ 级数推导的关键环节。

### [O12] Ramanujan 的 $n$ 的表示数 $r_s(n)$
**公式**：对于 $s$ 个平方和的表示数：
$$r_2(n) = 4\sum_{d|n} \chi_4(d), \quad r_4(n) = 8\sum_{d|n, 4\nmid d} d$$
**背景**：Ramanujan 在笔记中系统记录了各维表示数公式。
**后续**：与模形式和 theta 级数理论相关。

### [O13] Ramanujan 的 $q$-Bernoulli 数
**公式**：
$$\sum_{n=0}^{\infty} \beta_n \frac{t^n}{n!} = \frac{t}{e^t - 1} \cdot \frac{e^t - 1}{e^t - q}$$
（q-模拟的 Bernoulli 数生成函数）
**背景**：Ramanujan 在笔记中隐含使用了 Bernoulli 数的 q-模拟。
**后续**：Carlitz 1948 年系统定义了 q-Bernoulli 数。

### [O14] Ramanujan 的 $P, Q, R$ 函数
**公式**：
$$P(q) = 1 - 24\sum_{n=1}^{\infty} \sigma_1(n) q^n = E_2(q)$$
$$Q(q) = 1 + 240\sum_{n=1}^{\infty} \sigma_3(n) q^n = E_4(q)$$
$$R(q) = 1 - 504\sum_{n=1}^{\infty} \sigma_5(n) q^n = E_6(q)$$
**背景**：Ramanujan 用 $P, Q, R$ 记号表示 Eisenstein 级数 $E_2, E_4, E_6$，并发现了它们之间的微分关系。
**后续**：这是模形式理论的基础；Ramanujan 的微分方程 $q\frac{dP}{dq} = \frac{P^2-Q}{12}$ 等是模形式理论的基石。

### [O15] Ramanujan 的微分方程组
**公式**：
$$q\frac{dP}{dq} = \frac{P^2 - Q}{12}$$
$$q\frac{dQ}{dq} = \frac{PQ - R}{3}$$
$$q\frac{dR}{dq} = \frac{PR - Q^2}{2}$$
**背景**：Ramanujan 发现的 Eisenstein 级数 $E_2, E_4, E_6$ 之间的非线性微分方程组。
**后续**：这是模形式理论的核心结构之一；与 KdV 方程和可积系统有深层联系。

---

## 参考文献

- B.C. Berndt, *Ramanujan's Notebooks*, Parts I–V, Springer, 1985–1998.
- B.C. Berndt and R.A. Rankin, *Ramanujan: Letters and Commentary*, AMS, 1995.
- G.E. Andrews and B.C. Berndt, *Ramanujan's Lost Notebook*, Parts I–V, Springer, 2005–2018.
- G.H. Hardy, *Ramanujan: Twelve Lectures on Subjects Suggested by His Life and Work*, Cambridge, 1940.
- G. Gasper and M. Rahman, *Basic Hypergeometric Series*, Cambridge, 1990.
- B.C. Berndt, "An overview of Ramanujan's notebooks," *Ramanujan Journal*, 2007.
