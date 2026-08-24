# Proof: All polynomials $P(x)$ of odd degree $d$ with integer coefficients satisfying the given property

## Answer

The polynomials satisfying the condition are exactly:

$$\boxed{P(x) = c(qx - p)^d}$$

where $c$ is a nonzero integer, $p, q$ are integers with $q > 0$ and $\gcd(p, q) = 1$.

---

## Proof

### Part 1: Sufficiency — $P(x) = c(qx - p)^d$ satisfies the condition

Let $P(x) = c(qx - p)^d$ with $c \neq 0$, $q > 0$, $\gcd(p,q) = 1$, and $d$ odd. For any positive integer $n$, choose $x_i = N + i$ for $i = 1, \ldots, n$, where $N$ is a sufficiently large positive integer with $qN - p > 0$.

**Ratio is a $d$-th power of a rational:**

$$\frac{P(x_i)}{P(x_j)} = \frac{c(q(N+i) - p)^d}{c(q(N+j) - p)^d} = \left(\frac{qN - p + qi}{qN - p + qj}\right)^d$$

This is the $d$-th power of the rational $\frac{qN - p + qi}{qN - p + qj}$. ✓

**Ratio lies in $(1/2, 2)$:**

$$\frac{P(x_i)}{P(x_j)} = \left(1 + \frac{q(i-j)}{qN - p + qj}\right)^d \longrightarrow 1 \quad \text{as } N \to \infty$$

For sufficiently large $N$, all ratios are in $(1/2, 2)$. ✓

**Same sign:** Since $d$ is odd and $qx_i - p > 0$ for all $i$, all $P(x_i) = c(qx_i - p)^d$ have the sign of $c$. ✓

### Part 2: Necessity — If $P$ satisfies the condition, then $P(x) = c(qx - p)^d$

Assume $P(x) = a_d x^d + a_{d-1} x^{d-1} + \cdots + a_0$ with $a_d \neq 0$, $d$ odd, and $P$ satisfies the condition for all $n$. WLOG $a_d > 0$ (replace $P$ by $-P$ if needed; since $d$ is odd, ratios are unchanged).

#### Step 1: Reduction to $P(x_i) = \lambda y_i^d$

The condition that $P(x_i)/P(x_j)$ is a $d$-th power of a rational for all $i, j$ means that for every prime $p$, the $p$-adic valuations $v_p(P(x_i))$ are all congruent modulo $d$. Equivalently, there exists a $d$-th-power-free integer $\lambda$ and integers $y_1, \ldots, y_n$ such that:

$$P(x_i) = \lambda \, y_i^d \quad \text{for all } i$$

(That the $y_i$ are integers, not just rationals: if $P(x_i) = \lambda q_i^d$ with $q_i = a_i/b_i$ in lowest terms, then $b_i^d \mid \lambda$. Since $\lambda$ is $d$-th-power-free, $v_p(\lambda) < d$ for all $p$, forcing $v_p(b_i) = 0$, so $b_i = 1$.)

The condition $1/2 < P(x_i)/P(x_j) < 2$ means all $|P(x_i)|$ are within a factor of 2. Since $P$ has odd degree with $a_d > 0$, for large $x$, $P(x) > 0$ and $P$ is eventually increasing. So for large $x_i$, all $P(x_i) > 0$ and the $x_i$ lie in an interval $[X, X + \Delta]$ where $\Delta \approx X(2^{1/d} - 1) \sim X \ln 2 / d$.

#### Step 2: Asymptotic expansion of $y = (P(x)/\lambda)^{1/d}$

Define the **center** of $P$ as $r = -\frac{a_{d-1}}{d \cdot a_d}$ (a rational number). Write:

$$P(x) = a_d(x - r)^d + Q(x)$$

where $Q(x)$ is a polynomial of degree $\leq d - 2$. If $Q \equiv 0$, then $P(x) = a_d(x - r)^d$, which is of the desired form. So assume $Q \neq 0$.

Set $\alpha = (a_d / \lambda)^{1/d}$ (a positive real number). For large $x$:

$$y = \left(\frac{P(x)}{\lambda}\right)^{1/d} = \alpha(x - r)\left(1 + \frac{Q(x)}{a_d(x-r)^d}\right)^{1/d}$$

$$= \alpha(x - r) + \frac{\alpha \, Q(x)}{d \cdot a_d \, (x - r)^{d-1}} + O\!\left(\frac{1}{x^{d+1}}\right)$$

Since $Q$ has degree $\leq d - 2$, the term $Q(x)/(x-r)^{d-1} = O(1/x)$, so:

$$y = \alpha(x - r) + \frac{C}{x - r} + O\!\left(\frac{1}{(x-r)^2}\right) \tag{$\star$}$$

where $C = \frac{\alpha \, q}{d \cdot a_d}$ and $q \neq 0$ is the leading coefficient of $Q$ in its expansion around $r$. (If $\deg Q < d - 2$, then $C = 0$ but the next term is $O(1/(x-r)^k)$ for some $k \geq 2$; the argument below applies *a fortiori*.)

**Key consequence of $(\star)$:** The values $y_i$ are **not** exactly linear in $x_i$; there is a nonzero correction term $C/(x_i - r)$.

#### Step 3: All $y_i$ are approximately collinear

Write $r = s/t$ in lowest terms ($t > 0$, $\gcd(s, t) = 1$). Define the integer coordinates:

$$U_i = t \, x_i - s, \qquad V_i = t \, y_i$$

Then $U_i, V_i$ are integers, and from $(\star)$:

$$V_i = \alpha \, U_i + \frac{K}{U_i} + O\!\left(\frac{1}{U_i^2}\right) \tag{$\star\star$}$$

where $K = C \, t^2 \neq 0$ is a constant depending on $P$ and $\lambda$ (but bounded uniformly: $|K| \leq \frac{|q| \, t^2}{d \, |a_d|^{(d-1)/d}}$ since $|\alpha| \leq |a_d|^{1/d}$ for $|\lambda| \geq 1$).

For each pair $(i, j)$ with $U_i \neq U_j$, define the **slope**:

$$\rho_{ij} = \frac{V_i - V_j}{U_i - U_j}$$

From $(\star\star)$:

$$\rho_{ij} = \alpha + \frac{K(1/U_i - 1/U_j)}{U_i - U_j} + O\!\left(\frac{1}{U_0^2 \, |U_i - U_j|}\right) = \alpha - \frac{K}{U_i \, U_j} + O\!\left(\frac{1}{U_0^2 \, |U_i - U_j|}\right)$$

where $U_0 \sim tX$ is the scale of the $U_i$. Since $|U_i - U_j| \geq 1$ and $U_i, U_j \sim U_0$:

$$\left|\rho_{ij} - \left(\alpha - \frac{K}{U_0^2}\right)\right| = O\!\left(\frac{1}{U_0^2}\right) \tag{$\dagger$}$$

with the implicit constant depending only on $P$ (not on $\lambda$ or $X$).

**The $\rho_{ij}$ are rationals with bounded denominators** (dividing $|U_i - U_j| \leq \Delta_U \sim U_0 \ln 2 / d$). Two distinct rationals $a/b, c/d$ with $|b|, |d| \leq \Delta_U$ satisfy $|a/b - c/d| \geq 1/\Delta_U^2$. By $(\dagger)$, all $\rho_{ij}$ lie in an interval of length $O(1/U_0^2)$. So the number of **distinct** values of $\rho_{ij}$ is:

$$S \leq \frac{O(1/U_0^2)}{1/\Delta_U^2} + 1 = O\!\left(\frac{\Delta_U^2}{U_0^2}\right) + 1 = O\!\left(\frac{(\ln 2)^2}{d^2}\right) + 1 =: S_0$$

where $S_0$ is a **constant depending only on $P$ and $d$** (not on $n$, $\lambda$, or $X$).

#### Step 4: Ramsey argument — finding $d+1$ collinear points

Color each edge $(i, j)$ of the complete graph $K_n$ by the value $\rho_{ij}$. There are at most $S_0$ colors. By **Ramsey's theorem**, if $n \geq R_{S_0}(d+1)$ (a constant depending only on $P$ and $d$), there exists a monochromatic clique $T \subseteq \{1, \ldots, n\}$ of size $|T| = d + 1$.

For all $i, j \in T$, $\rho_{ij} = \rho$ (a fixed rational). This means:

$$\frac{V_i - V_j}{U_i - U_j} = \rho \quad \Longrightarrow \quad V_i - \rho \, U_i = \text{const} \quad \text{for all } i \in T$$

So all $d + 1$ points $(U_i, V_i)$ for $i \in T$ lie on the line $V = \rho \, U + \sigma$. Translating back:

$$y_i = \frac{\rho}{t} \, x_i + \sigma' \quad \text{for all } i \in T$$

for some rational $\sigma'$. That is, $y_i = A \, x_i + B$ for rationals $A, B$ and all $i \in T$.

#### Step 5: Conclusion

For $i \in T$ (with $|T| = d + 1$):

$$P(x_i) = \lambda \, y_i^d = \lambda (A \, x_i + B)^d$$

Both $P(x)$ and $\lambda(Ax + B)^d$ are polynomials of degree $d$ that agree at $d + 1$ distinct points. Therefore:

$$P(x) = \lambda(Ax + B)^d \quad \text{as polynomials}$$

This means $P$ is a perfect $d$-th power of a linear polynomial. Since $P$ has integer coefficients, we can write $P(x) = c(qx - p)^d$ for integers $c \neq 0$, $p$, $q$ with $q > 0$ and $\gcd(p, q) = 1$.

**Contradiction:** We assumed $Q \neq 0$ (i.e., $P$ is not of the form $c(qx-p)^d$), but derived that $P$ must be of this form. So the condition fails for $n \geq R_{S_0}(d+1) + 1$ when $P$ is not of the required form.

Since the condition must hold for **all** $n$, we conclude $P(x) = c(qx - p)^d$. $\blacksquare$

---

### Remark on the case $d = 1$

For $d = 1$, every rational is a 1st power, so condition (2) is automatic. Condition (1) is satisfied by any linear polynomial $P(x) = ax + b$ ($a \neq 0$) by taking $x_i$ close together. Every such polynomial is of the form $c(qx - p)^1$ with $c = a/q$, where $-b/a = p/q$ in lowest terms (and $q \mid a$ ensures integer coefficients). So the answer is consistent across all odd $d$.
