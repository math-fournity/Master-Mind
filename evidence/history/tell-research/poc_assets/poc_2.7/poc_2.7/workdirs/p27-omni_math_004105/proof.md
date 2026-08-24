# Proof: Smallest $n$ such that each element is a sum of $k$ other distinct elements

**Problem.** Let $k \ge 2$ be an integer. Find the smallest integer $n \ge k+1$ with the property that there exists a set of $n$ distinct real numbers such that each of its elements can be written as a sum of $k$ other distinct elements of the set.

**Answer.** $\boxed{k+4}$

---

## Lower Bound: $n \ge k + 4$

We show that $n = k+1$, $n = k+2$, and $n = k+3$ are all impossible.

Let $S = \{a_1 < a_2 < \cdots < a_n\}$ and $\sigma = \sum_{i=1}^n a_i$. For each $a_j \in S$, there exist $k$ distinct elements of $S \setminus \{a_j\}$ summing to $a_j$. The remaining $n - 1 - k$ elements of $S \setminus \{a_j\}$ (the "unused" elements) sum to $\sigma - a_j - a_j = \sigma - 2a_j$.

### Case $n = k + 1$: Impossible

When $n = k+1$, the unused set is empty ($n - 1 - k = 0$), so $\sigma - 2a_j = 0$ for every $j$, meaning $a_j = \sigma/2$ for all $j$. All elements are equal, contradicting distinctness. $\square$

### Case $n = k + 2$: Impossible

When $n = k+2$, the unused set has exactly $1$ element. For each $a_j$, there exists a unique $a_{\varphi(j)} \in S \setminus \{a_j\}$ with $a_{\varphi(j)} = \sigma - 2a_j$. The map $\varphi: S \to S$ defined by $\varphi(x) = \sigma - 2x$ is injective (affine with slope $-2 \ne 0$), hence bijective on the finite set $S$, so $\varphi$ is a permutation.

The $m$-th iterate of $\varphi$ is $\varphi^{(m)}(x) = (-2)^m x + \sigma \cdot \frac{1 - (-2)^m}{3}$. For a cycle of length $m \ge 1$, we need $\varphi^{(m)}(x) = x$, which gives $[(-2)^m - 1]\left(x - \frac{\sigma}{3}\right) = 0$. Since $|(-2)^m| \ge 2 > 1$ for all $m \ge 1$, we must have $x = \sigma/3$. But then $\varphi(x) = \sigma - 2\sigma/3 = \sigma/3 = x$, meaning $x$ is a fixed point, so $\varphi(x) = x \in S \setminus \{x\}$ — a contradiction. No cycles exist, contradicting $\varphi$ being a permutation of a finite set. $\square$

### Case $n = k + 3$: Impossible

When $n = k+3$, the unused set has exactly $2$ elements. For each $a_j$, there exist two distinct elements $y, z \in S \setminus \{a_j\}$ with $y + z = \sigma - 2a_j$.

**For $a_1$ (smallest):** The pair $\{y, z\} \subseteq \{a_2, \ldots, a_{k+3}\}$, so $y + z \le a_{k+2} + a_{k+3}$ (the maximum pair sum). Thus:
$$\sigma - 2a_1 \le a_{k+2} + a_{k+3}. \quad (1)$$

**For $a_{k+3}$ (largest):** The pair $\{y, z\} \subseteq \{a_1, \ldots, a_{k+2}\}$, so $y + z \ge a_1 + a_2$ (the minimum pair sum). Thus:
$$\sigma - 2a_{k+3} \ge a_1 + a_2. \quad (2)$$

From (1): $\sigma \le 2a_1 + a_{k+2} + a_{k+3}$.

From (2): $\sigma \ge 2a_{k+3} + a_1 + a_2$.

Combining:
$$2a_{k+3} + a_1 + a_2 \le 2a_1 + a_{k+2} + a_{k+3},$$
which simplifies to:
$$a_{k+3} - a_{k+2} \le a_1 - a_2.$$

Since the elements are distinct and ordered, $a_{k+3} > a_{k+2}$ (so the left side is positive) and $a_1 < a_2$ (so the right side is negative). A positive number cannot be at most a negative number — **contradiction**. $\square$

---

## Upper Bound: Construction for $n = k + 4$

We construct a set of $k + 4$ distinct reals with the required property.

### Construction

Let $m = \lfloor k/2 \rfloor + 2$ (so $m \ge 3$ for $k \ge 2$).

- **Even $k$:** $S = \{-m, -(m-1), \ldots, -1, 1, \ldots, m-1, m\}$, with $|S| = 2m = k + 4$.
- **Odd $k$:** $S = \{-m, -(m-1), \ldots, -1, 0, 1, \ldots, m-1, m\}$, with $|S| = 2m + 1 = k + 4$.

In both cases, $S$ is symmetric about $0$ (i.e., $x \in S \iff -x \in S$), so $\sum_{x \in S} x = 0$.

### Key Reduction

For $x \in S$, we need $x = $ (sum of $k$ distinct elements of $S \setminus \{x\}$). Since $\sum(S \setminus \{x\}) = -x$, the $n - 1 - k = 3$ unused elements sum to $-x - x = -2x$.

**Thus the condition reduces to:** For each $x \in S$, there exist $3$ distinct elements of $S \setminus \{x\}$ summing to $-2x$.

By the symmetry of $S$, it suffices to verify this for $x \ge 0$ (the case $x < 0$ follows by negating all elements in the decomposition).

### Verification

**Case $x = 0$ (odd $k$ only):** Need $3$ distinct elements of $S \setminus \{0\}$ summing to $0$. Take $m, -(m-1), -1$:
$$m + (-(m-1)) + (-1) = m - m + 1 - 1 = 0. \checkmark$$
These are distinct for $m \ge 3$.

**Case $x = 1$:** Need $3$ distinct elements of $S \setminus \{1\}$ summing to $-2$. Take $-m, m-1, -1$:
$$(-m) + (m-1) + (-1) = -2. \checkmark$$
These are distinct and in $S \setminus \{1\}$ for $m \ge 3$ (since $-m \ne m-1$, $-m \ne -1$ as $m \ge 3$, and $m-1 \ne -1$ as $m \ge 3$; also $m - 1 \ne 1$ as $m \ne 2$).

**Case $x = j$ for $2 \le j \le m - 1$:**

- **Subcase $m \ne 2j$:** Take $-m, m-j, -j$:
$$(-m) + (m - j) + (-j) = -2j. \checkmark$$
These are distinct: $-m \ne m-j$ (since $j \ne 2m$), $-m \ne -j$ (since $m \ne j$), $m-j \ne -j$ (since $m \ne 0$). They are in $S \setminus \{j\}$: $-m \ne j$ (since $m, j > 0$), $m - j \ne j$ (since $m \ne 2j$), $-j \ne j$ (since $j \ne 0$). Also $1 \le m - j \le m - 2 < m$ and $m - j \ge 1$, so $m - j \in S$; and $-j \in S$.

- **Subcase $m = 2j$ (so $j \ge 2$, $m \ge 4$):** Take $-m, j+1, -(j+1)$:
$$(-m) + (j+1) + (-(j+1)) = -m = -2j. \checkmark$$
These are distinct (since $m \ge 4$, $j+1 \ne -m$, $j+1 \ne -(j+1)$, $-m \ne -(j+1)$ as $m \ne j+1$ i.e. $2j \ne j+1$ i.e. $j \ne 1$). They are in $S \setminus \{j\}$: $j+1 \le m = 2j$ and $j+1 \ge 3$, so $j+1 \in S$; $-(j+1) \ge -m$ and $-(j+1) \le -3$, so $-(j+1) \in S$; none equals $j$ (since $j+1 \ne j$, $-(j+1) \ne j$, $-m = -2j \ne j$).

**Case $x = m$:** Need $3$ distinct elements of $S \setminus \{m\}$ summing to $-2m$. Take $-m, -(m-1), -1$:
$$(-m) + (-(m-1)) + (-1) = -2m. \checkmark$$
These are distinct for $m \ge 3$ (since $m \ne m-1$, $m \ne 1$, $m-1 \ne 1$ i.e. $m \ne 2$). They are all in $S \setminus \{m\}$ (all negative, so $\ne m > 0$).

### Conclusion of verification

All cases are covered, so the construction works for every $k \ge 2$.

---

## Summary

- **Lower bound:** $n \ge k + 4$ because $n = k+1$, $k+2$, $k+3$ are all impossible.
- **Upper bound:** $n = k + 4$ is achieved by the symmetric construction above.

Therefore, the smallest such $n$ is $\boxed{k + 4}$.
