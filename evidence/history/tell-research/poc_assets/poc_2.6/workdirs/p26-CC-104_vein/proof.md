# CC-104 / polymath_03408 解答

## 题目

将 $\{1,2,3,\ldots,500\}$ 排列在圆周上，使得对任意四个不同数 $a,b,c,d$ 满足 $a+b \equiv c+d \pmod{500}$，连接 $a,b$ 和 $c,d$ 的线段在圆内不相交。旋转相同的排列视为同一种。求排列数。

## 记号与化归

将 $\{1,\ldots,500\}$ 视为 $\mathbb{Z}_{500}$（其中 $500 \equiv 0$），记 $n = 500$。

设排列为 $\pi$：位置 $i$ 上放数 $\pi(i)$，$i \in \mathbb{Z}_n$。记 $\operatorname{pos}(k) = \pi^{-1}(k)$ 为数 $k$ 所在位置。

**非交叉条件**：对每个和类 $s \in \mathbb{Z}_n$，所有满足 $a + b \equiv s \pmod{n}$ 的对 $\{a, b\}$（$a \neq b$）对应的弦 $\{\operatorname{pos}(a), \operatorname{pos}(b)\}$ 两两不相交。

## 核心引理：三连续位置强制等差

**引理**。若排列满足非交叉条件，则对任意三个连续位置 $i, i+1, i+2 \pmod{n}$，其上的数 $a = \pi(i)$, $b = \pi(i+1)$, $c = \pi(i+2)$ 满足
$$
a + c \equiv 2b \pmod{n}.
$$

**证明**。反设 $a + c \not\equiv 2b \pmod{n}$。令 $e = a + c - b \pmod{n}$。

**$e$ 与 $a, b, c$ 互异**：
- $e = a \iff c = b$，矛盾（$\pi$ 是排列，$b, c$ 在不同位置）。
- $e = c \iff a = b$，矛盾。
- $e = b \iff a + c = 2b$，与反设矛盾。

故 $a, b, c, e$ 四数互异。

**同一和类**：$a + c \equiv e + b \pmod{n}$（因为 $e + b = a + c$），所以对 $\{a, c\}$ 与 $\{e, b\}$ 属于同一和类 $s = a + c$。

**弦相交**：弦 $\{a, c\}$ 连接位置 $i$ 和 $i+2$。弦 $\{e, b\}$ 连接位置 $\operatorname{pos}(e)$ 和 $i+1$。

弦 $\{i, i+2\}$ 将圆分为两段弧：
- 短弧：$\{i,\, i+1,\, i+2\}$（仅含位置 $i+1$ 作为内部点）。
- 长弧：其余所有位置。

两条弦相交当且仅当一条弦的两端点分属不同弧。由于 $i+1$ 在短弧内部，而 $\operatorname{pos}(e) \notin \{i, i+1, i+2\}$（因为 $e \neq a, b, c$），所以 $\operatorname{pos}(e)$ 在长弧内部。因此弦 $\{\operatorname{pos}(e),\, i+1\}$ 与弦 $\{i,\, i+2\}$ **相交**。

这与非交叉条件矛盾。故 $a + c \equiv 2b \pmod{n}$。$\blacksquare$

## 排列必为等差数列

由引理，任意三个连续位置上的数成等差（模 $n$）。设 $\pi(0) = a_0$, $\pi(1) = a_0 + d$，则由归纳法：
$$
\pi(k) = a_0 + kd \pmod{n}, \quad k = 0, 1, \ldots, n-1.
$$

**$\pi$ 是排列 $\iff$ $\gcd(d, n) = 1$**：映射 $k \mapsto a_0 + kd \pmod{n}$ 是 $\mathbb{Z}_n$ 上的双射当且仅当 $d$ 是 $\mathbb{Z}_n$ 的可逆元，即 $\gcd(d, n) = 1$。

因此，满足条件的排列（在固定旋转下）恰好由 $d \in \mathbb{Z}_n^*$ 参数化，共 $\varphi(n)$ 个。

## 等差数列确实满足非交叉条件

**验证**。设 $\pi(k) = a_0 + kd \pmod{n}$，$\gcd(d, n) = 1$。对和类 $s$，对 $\{a, s-a\}$ 所在位置为
$$
\operatorname{pos}(a) = d^{-1}(a - a_0), \quad \operatorname{pos}(s-a) = d^{-1}(s - a - a_0).
$$
两位置之和为 $d^{-1}(s - 2a_0) \pmod{n}$，这是不依赖于 $a$ 的常数。

**关键事实**：在自然循环序 $0, 1, \ldots, n-1$ 中，所有满足 $p + q \equiv S \pmod{n}$ 的对 $\{p, q\}$（$p \neq q$）两两不相交。

*证明关键事实*：对 $\{p, S-p\}$ 和 $\{q, S-q\}$，它们都关于"轴" $S/2$（和 $S/2 + n/2$）对称。在循环序中，这些对按到轴的距离排列，形成嵌套结构（laminar family），因此两两不相交。具体地，若 $p, q$ 在轴的同一侧且 $p$ 更靠近轴，则 $\{q, S-q\}$ 被 $\{p, S-p\}$ 包含（嵌套），不相交。若 $p, q$ 在轴的异侧，则两对分别在圆的不同半圆内，也不相交。

因此，等差排列 $\pi(k) = a_0 + kd$ 满足非交叉条件。$\blacksquare$

## 计数

旋转等价：固定 $\pi(0) = 0$（即 $a_0 = 0$），排列由 $d$ 唯一确定，$\gcd(d, 500) = 1$。

$$
\varphi(500) = \varphi(2^2 \cdot 5^3) = 500 \cdot \left(1 - \frac{1}{2}\right) \cdot \left(1 - \frac{1}{5}\right) = 500 \cdot \frac{1}{2} \cdot \frac{4}{5} = 200.
$$

## 最终答案

$$\boxed{200}$$
