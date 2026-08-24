# 解答

## 答案

$$\boxed{f(n) = c \cdot v_p(n)}$$

其中 $p$ 为某个素数，$c$ 为某个正整数，$v_p(n)$ 表示 $n$ 中素因子 $p$ 的幂次（$p$-adic valuation）。

---

## 证明

### 第一步：由条件 (ii) 确定 $f$ 的结构

由 $f(xy) = f(x) + f(y)$，取 $x = y = 1$ 得 $f(1) = 2f(1)$，故 $f(1) = 0$。

对任意正整数 $n = p_1^{a_1} \cdots p_r^{a_r}$，反复应用条件 (ii) 得

$$f(n) = \sum_{i=1}^{r} a_i \, f(p_i).$$

因此 $f$ 完全由其在素数上的取值决定。令

$$S = \{p \text{ 素数} : f(p) > 0\}, \quad P = \prod_{p \in S} p.$$

由条件 (i)，$S \neq \emptyset$。对 $p \in S$，记 $c_p = f(p) > 0$。则

$$f(n) = \sum_{p \in S} v_p(n) \cdot c_p.$$

### 第二步：验证 $f = c \cdot v_p$ 满足所有条件

设 $f(n) = c \cdot v_p(n)$，其中 $p$ 为素数，$c$ 为正整数。

- 条件 (i)：$f(p) = c \neq 0$。 ✓
- 条件 (ii)：$v_p(xy) = v_p(x) + v_p(y)$，故 $f(xy) = f(x) + f(y)$。 ✓
- 条件 (iii)：取 $n = p^m$（$m = 1, 2, 3, \ldots$），有无穷多个这样的 $n$。对任意 $1 \leq k \leq p^m - 1$，写 $k = p^a \cdot u$，其中 $\gcd(u, p) = 1$，$0 \leq a \leq m - 1$。则

$$p^m - k = p^a(p^{m-a} - u).$$

由于 $m - a \geq 1$，有 $p \mid p^{m-a}$，而 $\gcd(u, p) = 1$，故 $p^{m-a} - u \equiv -u \not\equiv 0 \pmod{p}$，即 $v_p(p^{m-a} - u) = 0$。因此

$$v_p(p^m - k) = a = v_p(k),$$

从而 $f(k) = f(p^m - k)$。 ✓

### 第三步：证明 $|S| = 1$（唯一性的核心）

假设 $|S| \geq 2$。设 $n$ 为满足条件 (iii) 的一个正整数（即对一切 $1 \leq k \leq n-1$ 有 $f(k) = f(n-k)$）。

**引理 1**：$f(n-1) = 0$，即 $\gcd(n-1, P) = 1$。

*证明*：取 $k = 1$，$f(1) = 0 = f(n-1)$。故 $n - 1$ 不含 $S$ 中任何素因子。$\square$

**引理 2**：若存在 $p \in S$ 使得 $v_p(n) \geq 1$，则 $P \mid n$。

*证明*：设 $p \in S$，$v_p(n) \geq 1$。取 $a = 1$，即 $v_p(n) \geq a$。考虑 $k = p \cdot u$，其中 $\gcd(u, P) = 1$ 且 $k < n$。则

$$f(k) = v_p(k) \cdot c_p = c_p \quad (\text{因 } v_q(k) = 0, \forall q \in S, q \neq p).$$

故 $f(n - k) = c_p$。

由于 $v_p(n) \geq 1 > 0$，分两种情况：

- 若 $v_p(n) > 1$（即 $v_p(n) > a = 1$）：$n - pu = p(p^{v_p(n)-1} \cdot n' - u)$，其中 $n' = n/p^{v_p(n)}$，$\gcd(n', p) = 1$。因 $v_p(n) - 1 \geq 1$，$p \mid p^{v_p(n)-1} n'$，故 $p^{v_p(n)-1} n' - u \equiv -u \pmod{p}$，$\gcd(u,p) = 1$，所以 $v_p(n - k) = 1$。

- 若 $v_p(n) = 1$（即 $v_p(n) = a = 1$）：$n - pu = p(n' - u)$，其中 $n' = n/p$，$\gcd(n', p) = 1$。$v_p(n - k) = 1 + v_p(n' - u)$。

在两种情况下，对于任意 $q \in S$，$q \neq p$：若 $q \nmid n$，则 $n \not\equiv 0 \pmod{q}$。当 $u$ 取遍与 $P$ 互素的值时（在模 $q$ 意义下取遍所有非零剩余类，只要 $n$ 足够大），存在 $u$ 使得 $n - pu \equiv 0 \pmod{q}$，即 $v_q(n - k) \geq 1$。

此时 $f(n - k) \geq c_q > 0$ 加上 $v_p(n-k) \geq 1$ 的贡献。具体地：

- 若 $v_p(n) > 1$：$v_p(n-k) = 1$，故 $f(n-k) = c_p + c_q v_q(n-k) + \cdots \geq c_p + c_q > c_p$，矛盾。
- 若 $v_p(n) = 1$：$v_p(n-k) = 1 + v_p(n' - u) \geq 1$，故 $f(n-k) = c_p(1 + v_p(n'-u)) + c_q v_q(n-k) + \cdots$。要使 $f(n-k) = c_p$，需要 $v_p(n'-u) = 0$ 且 $v_q(n-k) = 0$ 对所有 $q \neq p$。但我们已找到 $u$ 使 $v_q(n-k) \geq 1$，矛盾。

因此 $q \mid n$ 对所有 $q \in S$，$q \neq p$ 成立。结合 $v_p(n) \geq 1$，得 $P \mid n$。$\square$

**引理 3**：若 $P \mid n$，则对每个 $p \in S$ 和每个满足 $p^a < n$ 的正整数 $a$，有 $v_p(n) \geq a$。

*证明*：因 $P \mid n$，对任意 $q \in S$，$q \neq p$，有 $n \equiv 0 \pmod{q}$，而 $p^a \not\equiv 0 \pmod{q}$（因 $p \neq q$），故 $n - p^a \equiv -p^a \pmod{q}$，$v_q(n - p^a) = 0$。

取 $k = p^a$，则 $f(k) = a \cdot c_p$，故 $f(n - p^a) = a \cdot c_p$。而

$$f(n - p^a) = c_p \cdot v_p(n - p^a) + \sum_{q \neq p} c_q \underbrace{v_q(n - p^a)}_{= 0} = c_p \cdot v_p(n - p^a).$$

故 $v_p(n - p^a) = a$。

设 $b = v_p(n)$。若 $b < a$：$n - p^a = p^b(n/p^b - p^{a-b})$，其中 $\gcd(n/p^b, p) = 1$ 且 $p \mid p^{a-b}$（因 $a > b$），故 $n/p^b - p^{a-b} \equiv n/p^b \not\equiv 0 \pmod{p}$，$v_p(n - p^a) = b < a$，矛盾。

故 $v_p(n) \geq a$。$\square$

**引理 4**：若 $P \mid n$ 且 $|S| \geq 2$，则 $n$ 有上界。

*证明*：由引理 3，对每个 $p \in S$，$v_p(n) \geq A_p$，其中 $A_p = \lfloor \log_p(n-1) \rfloor$（这是满足 $p^a < n$ 的最大整数 $a$）。

故 $p^{A_p} \mid n$ 对所有 $p \in S$，从而

$$n \geq \prod_{p \in S} p^{A_p}.$$

而 $p^{A_p} \geq p^{\log_p(n-1) - 1} = \frac{n-1}{p}$，故

$$n \geq \prod_{p \in S} \frac{n-1}{p} = \frac{(n-1)^{|S|}}{\prod_{p \in S} p}.$$

当 $|S| \geq 2$ 时，$(n-1)^2 \leq n \cdot \prod_{p \in S} p$，即 $n^2 - (2 + \prod p) n + 1 \leq 0$。此不等式仅对 $n \leq \frac{(2 + \prod p) + \sqrt{(2 + \prod p)^2 - 4}}{2}$ 成立，故 $n$ 有上界 $N_1$（约等于 $\prod p + 2$）。$\square$

**引理 5**：若 $\gcd(n, P) = 1$（即对所有 $p \in S$，$v_p(n) = 0$）且 $n > P$，则矛盾。

*证明*：取 $k = P = \prod_{p \in S} p$。因 $n > P$，$k < n$。则

$$f(k) = \sum_{p \in S} c_p > 0.$$

而 $n - k \equiv n \pmod{p}$ 对每个 $p \in S$（因 $p \mid k$），且 $\gcd(n, P) = 1$ 故 $n \not\equiv 0 \pmod{p}$，从而 $v_p(n - k) = 0$ 对所有 $p \in S$。故

$$f(n - k) = 0 \neq f(k).$$

矛盾。$\square$

**综合**：设 $|S| \geq 2$。对任意满足条件 (iii) 的 $n$：

- 若 $v_p(n) \geq 1$ 对某个 $p \in S$：由引理 2，$P \mid n$；由引理 4，$n \leq N_1$。
- 若 $v_p(n) = 0$ 对所有 $p \in S$：由引理 5，$n \leq P$。

故满足条件 (iii) 的 $n$ 有上界 $\max(N_1, P)$，只有有限个。这与条件 (iii) 要求"无穷多个"矛盾。

因此 $|S| = 1$，即 $S = \{p\}$ 对某个素数 $p$，$f(n) = c \cdot v_p(n)$，$c = f(p) > 0$。

### 结论

满足全部三个条件的函数恰为

$$\boxed{f(n) = c \cdot v_p(n)}$$

其中 $p$ 为素数，$c$ 为正整数，$v_p(n)$ 为 $n$ 的 $p$-adic 赋值。
