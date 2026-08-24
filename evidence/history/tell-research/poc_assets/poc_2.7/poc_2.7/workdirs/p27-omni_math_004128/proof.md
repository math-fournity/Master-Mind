# Proof

## Problem

For each integer $k \geq 2$, determine all infinite sequences of positive integers $a_1, a_2, \ldots$ for which there exists a polynomial $P(x) = x^k + c_{k-1}x^{k-1} + \dots + c_1 x + c_0$ with non-negative integer coefficients, such that $P(a_n) = a_{n+1} a_{n+2} \cdots a_{n+k}$ for every $n \geq 1$.

## Answer

The sequences are exactly the arithmetic progressions
$$a_n = cn + d, \quad n \geq 1,$$
where $c \geq 0$ and $d \geq 1$ are integers (the case $c = 0$ gives constant sequences $a_n = d$). The corresponding polynomial is
$$P(x) = \prod_{i=1}^{k}(x + ic),$$
which equals $x^k$ when $c = 0$.

---

## Proof

### Part 1: These sequences work

Let $a_n = cn + d$ with $c \geq 0$, $d \geq 1$, and set $P(x) = \prod_{i=1}^{k}(x+ic)$. Then
$$P(a_n) = \prod_{i=1}^{k}(cn + d + ic) = \prod_{i=1}^{k}\bigl(c(n+i)+d\bigr) = \prod_{i=1}^{k} a_{n+i}.$$
The coefficients of $P$ are the elementary symmetric polynomials of $c, 2c, \ldots, kc$, which are non-negative integers. When $c = 0$, $P(x) = x^k$ and $P(d) = d^k = d^k = a_{n+1}\cdots a_{n+k}$. $\checkmark$

### Part 2: No other sequences work

Let $(a_n)$ be a sequence satisfying the condition with some polynomial $P$. We show it must be an arithmetic progression.

#### Step 1: If the sequence is bounded, it is constant.

If $a_n \leq M$ for all $n$, the state $(a_n, a_{n+1}, \ldots, a_{n+k-1})$ takes finitely many values, and $a_{n+k} = P(a_n)/(a_{n+1}\cdots a_{n+k-1})$ is determined, so the sequence is eventually periodic. If it has period $T$, then $P(a_n) = a_{n+1}\cdots a_{n+k}$ and $P(a_{n+T}) = a_{n+T+1}\cdots a_{n+T+k} = a_{n+1}\cdots a_{n+k}$, so $P(a_n) = P(a_{n+T})$. Since $P$ is strictly increasing on positive integers (all coefficients non-negative, leading coefficient positive), $a_n = a_{n+T}$, confirming periodicity.

Let $m = \min_n a_n$ and $M = \max_n a_n$, attained at indices $n_0$ and $n_1$. At $n_0$: $P(m) = a_{n_0+1}\cdots a_{n_0+k} \geq m^k$, but $P(m) = m^k + c_{k-1}m^{k-1} + \dots + c_0 \geq m^k$. At $n_1$: $P(M) = a_{n_1+1}\cdots a_{n_1+k} \leq M^k$, but $P(M) \geq M^k$. So $P(M) = M^k$, forcing all $c_i = 0$, i.e., $P(x) = x^k$. Then $a_{n+1}\cdots a_{n+k} = a_n^k$. At $n_0$ (where $a_{n_0} = m$): $m^k = a_{n_0+1}\cdots a_{n_0+k} \geq m^k$, so all $a_{n_0+i} = m$. By induction forward, all terms equal $m$. The sequence is constant. $\checkmark$

#### Step 2: In the unbounded case, $a_n \to \infty$.

Suppose $\liminf a_n = L < \infty$ with $a_{m_j} \leq L$ infinitely often. From $P(a_{m_j}) \leq P(L)$, each $a_{m_j+i} \leq P(L)$ for $i = 1, \ldots, k$. Iterating, $a_{m_j + r}$ is bounded for each fixed $r$.

Since the sequence is unbounded, there exist $n_j$ with $a_{n_j} \to \infty$. We claim $a_{n_j + 1} \to \infty$ as well. Indeed, from the ratio relation (derived in Step 3 below):
$$a_{n+k+1} = a_{n+1} \cdot \frac{P(a_{n+1})}{P(a_n)}.$$
If $a_{n_j} \to \infty$ but $a_{n_j+1} \leq L$, then $a_{n_j+k+1} \leq L \cdot P(L)/P(a_{n_j}) \to 0$, contradicting $a_{n_j+k+1} \geq 1$. So $a_{n_j+1} \to \infty$, and by induction $a_{n_j + r} \to \infty$ for every fixed $r \geq 0$.

Now suppose $a_{p} \to \infty$ but $a_{p+1} \leq L$ for some large $p$ (transition from large to small). Then $a_{p+k+1} = a_{p+1} \cdot P(a_{p+1})/P(a_p) \leq L \cdot P(L)/P(a_p)$. For $a_{p+k+1} \geq 1$, we need $P(a_p) \leq L \cdot P(L)$, so $a_p \leq P^{-1}(L \cdot P(L))$, a fixed bound. This contradicts $a_p \to \infty$. Hence no such transition exists, and $\liminf a_n = \infty$, i.e., $a_n \to \infty$.

#### Step 3: Key ratio relation

From $P(a_n) = a_{n+1}\cdots a_{n+k}$ and $P(a_{n+1}) = a_{n+2}\cdots a_{n+k+1}$, dividing:
$$\frac{P(a_{n+1})}{P(a_n)} = \frac{a_{n+k+1}}{a_{n+1}}. \tag{$\star$}$$

#### Step 4: $D_n / a_n \to 0$ where $D_n = a_{n+1} - a_n$

Since $P(a_n)/a_n^k \to 1$, we have $\prod_{i=1}^k (a_{n+i}/a_n) \to 1$. If $D_n/a_n \not\to 0$, there is a subsequence with $|D_n|/a_n \geq \epsilon > 0$, so $a_{n+1}/a_n \geq 1+\epsilon$ (or $\leq 1-\epsilon$). Then $\prod_{i=1}^k(a_{n+i}/a_n) \geq (1+\epsilon) \cdot \prod_{i=2}^k(a_{n+i}/a_n)$. For the product to tend to 1, some $a_{n+i}/a_n < 1$, but then the cumulative ratios $a_{n+i}/a_n$ would give $\prod(1 + E_{n,i}/a_n)$ with $E_{n,i} = a_{n+i} - a_n$ of order $a_n$, making the product bounded away from 1 — contradiction. So $D_n = o(a_n)$.

*(Detailed argument: if $D_n/a_n \to \delta > 0$ along a subsequence, then $a_{n+i}/a_n \to (1+\delta)^i$ (heuristically, since $D_{n+j}/a_n \to \delta$ as well by the propagation in Step 2), giving $\prod(1+\delta)^i = (1+\delta)^{k(k+1)/2} \neq 1$.)*

#### Step 5: $D_n$ is bounded

Using the exact Taylor expansion of $(\star)$ (finite since $\deg P = k$):
$$\sum_{j=1}^{k} \frac{P^{(j)}(a_n)}{j!\, P(a_n)} D_n^j = \frac{S_n}{a_n + D_n}, \qquad S_n = \sum_{i=1}^k D_{n+i}.$$

Since $P^{(j)}(a_n)/(j!\, P(a_n)) = \binom{k}{j}/a_n^j + O(1/a_n^{j+1})$, the LHS equals $\sum_{j=1}^k \binom{k}{j}(D_n/a_n)^j + O(|D_n|^k/a_n^{k+1}) = (1+D_n/a_n)^k - 1 + o(1)$.

Comparing the $1/a_n$ and $1/a_n^2$ terms (valid since $D_n/a_n \to 0$):

- **Order $1/a_n$:** $k D_n = S_n + O(D_n^2/a_n)$.
- **Order $1/a_n^2$:** $-c_{k-1} D_n + \frac{k(k-1)}{2} D_n^2 = -S_n D_n + O(D_n^2/a_n + D_n^3/a_n^2)$.

Substituting $S_n = kD_n + O(D_n^2/a_n)$ into the second equation:
$$D_n\!\left(-c_{k-1} + \tfrac{k(k+1)}{2}\, D_n\right) = O(D_n^2/a_n).$$

If $D_n$ were unbounded, the LHS grows like $D_n^2$ (since $D_n \to \pm\infty$ makes $\frac{k(k+1)}{2}D_n$ dominate), while the RHS is $O(D_n^2/a_n) = o(D_n^2)$. Dividing by $D_n \neq 0$: $\left|-c_{k-1} + \frac{k(k+1)}{2}D_n\right| = O(D_n/a_n) = o(1)$, but the LHS $\to \infty$. **Contradiction.** So $D_n$ is bounded.

#### Step 6: $D_n$ is eventually constant

Since $D_n$ is bounded, $D_n^2/a_n \to 0$, so the errors vanish. Both $kD_n - S_n$ and $D_n(-c_{k-1} + \frac{k(k+1)}{2}D_n)$ are **integers** (since $D_n, S_n, c_{k-1}$ are integers and $k(k+1)/2$ is an integer) that are $o(1)$, hence **exactly zero** for large $n$:

$$k D_n = S_n = \sum_{i=1}^k D_{n+i}, \qquad D_n\!\left(-c_{k-1} + \tfrac{k(k+1)}{2}\,D_n\right) = 0.$$

Set $c := \frac{2\,c_{k-1}}{k(k+1)}$. For large $n$, each $D_n \in \{0, c\}$.

- If $c_{k-1} = 0$: $c = 0$, so $D_n = 0$ for large $n$ — the sequence is eventually constant, hence constant (Step 1). This is the bounded case.
- If $c_{k-1} > 0$: $c > 0$. From $kD_n = \sum D_{n+i}$ with each $D_{n+i} \in \{0, c\}$: if $D_n = 0$ then all $D_{n+i} = 0$ (sum is 0), and by induction all subsequent $D_m = 0$ — eventually constant, contradicting unboundedness. So $D_n = c$ for all large $n$.

Thus $a_n = cn + d$ for all $n \geq N$ (some $N$, some constant $d$), with $c = \frac{2c_{k-1}}{k(k+1)}$ a positive integer.

#### Step 7: $P(x) = \prod_{i=1}^k (x + ic)$ and backwards propagation

For $n \geq N$: $P(a_n) = \prod_{i=1}^k a_{n+i} = \prod_{i=1}^k (cn + d + ic) = \prod_{i=1}^k (a_n + ic)$. So $P(x) = \prod_{i=1}^k(x + ic)$ as polynomials (they agree on infinitely many values $a_n \to \infty$).

Now propagate backwards. For $n = N-1$: $\prod_{i=1}^k(a_{N-1} + ic) = P(a_{N-1}) = \prod_{i=1}^k a_{N-1+i} = \prod_{i=1}^k(c(N-1+i)+d) = \prod_{i=1}^k(c(N-1)+d+ic)$. The function $f(x) = \prod_{i=1}^k(x+ic)$ is strictly increasing for $x > 0$ (all $ic \geq 0$, at least one $> 0$ since $c \geq 1$), so $a_{N-1} = c(N-1)+d$. By induction, $a_n = cn + d$ for all $n \geq 1$.

Since $a_n \geq 1$ for all $n \geq 1$ and $a_1 = c + d$, we need $c + d \geq 1$, i.e., $c \geq 0, d \geq 1$ (if $c = 0$) or $c \geq 1, d \geq 0$ (if $c \geq 1$). Equivalently: $c \geq 0$, $d \geq 1$ when $c = 0$; $c \geq 1$, $d \geq 0$ when $c \geq 1$. $\blacksquare$

---

## Summary

$$\boxed{a_n = cn + d \text{ for integers } c \geq 0,\ d \geq 1 \text{ (if } c=0\text{), or } c \geq 1,\ d \geq 0 \text{ (if } c \geq 1\text{)}, \text{ with } P(x) = \prod_{i=1}^{k}(x+ic).}$$

Equivalently, all arithmetic progressions $a_n = cn + d$ of positive integers with common difference $c \geq 0$ (including constant sequences when $c = 0$).
