# Proof: Largest $m$ for which the necklace coloring is impossible

**Problem.** Let $n \geq 3$ be fixed. There are $m \geq n+1$ beads on a circular necklace. We wish to paint the beads using $n$ colors, such that among any $n+1$ consecutive beads every color appears at least once. Find the largest value of $m$ for which this task is **not** possible.

**Answer:** $\boxed{n^2 - n - 1}$.

---

## Step 1: Reformulation via gap condition

**Claim.** The condition "every window of $n+1$ consecutive beads contains all $n$ colors" is equivalent to: **for each color, the gap between consecutive occurrences (number of beads strictly between them) is at most $n$.**

*Proof.* For a fixed color $j$, suppose two consecutive occurrences are at positions $p$ and $q$ (cyclically), with $q - p - 1$ beads between them. A window of $n+1$ consecutive beads entirely within the gap (excluding both $p$ and $q$) exists if and only if $q - p - 1 \geq n+1$, i.e., the gap $\geq n+1$. Such a window would miss color $j$. Conversely, if every gap is $\leq n$, then no window of $n+1$ can fit entirely within a gap, so every window contains color $j$. Applying this to all colors gives the equivalence. $\square$

## Step 2: Counting argument (impossibility for $m = n^2 - n - 1$)

For color $j$ appearing $k_j$ times, there are $k_j$ gaps (cyclically), each at most $n$, summing to $m - k_j$. Thus:
$$m - k_j \leq k_j \cdot n \implies k_j \geq \frac{m}{n+1} \implies k_j \geq \left\lceil \frac{m}{n+1} \right\rceil.$$

Summing over all $n$ colors:
$$m = \sum_{j=1}^{n} k_j \geq n \left\lceil \frac{m}{n+1} \right\rceil. \tag{$\star$}$$

Write $m = q(n+1) + r$ with $0 \leq r \leq n$.

- If $r = 0$: $\lceil m/(n+1) \rceil = q$, and $(\star)$ becomes $q(n+1) \geq nq$, i.e., $q \geq 0$. Always satisfied.
- If $r > 0$: $\lceil m/(n+1) \rceil = q+1$, and $(\star)$ becomes $q(n+1)+r \geq n(q+1) = nq + n$, i.e., $q + r \geq n$.

**The counting condition fails when $r > 0$ and $q + r \leq n - 1$.**

To find the largest such $m$: we maximize $m = q(n+1) + r$ subject to $q \geq 0$, $1 \leq r \leq n$, and $q + r \leq n - 1$. Since $m = qn + (q + r)$ and $q + r \leq n-1$, we have $m \leq qn + n - 1$. To maximize, take $q$ as large as possible: $q \leq n - 1 - r \leq n - 2$ (since $r \geq 1$). Setting $q = n-2, r = 1$:
$$m = (n-2)(n+1) + 1 = n^2 - n - 1.$$

**For $m = n^2 - n - 1$:** $q = n-2$, $r = 1$, $q + r = n - 1 \leq n - 1$. Each color requires at least $q + 1 = n - 1$ appearances, so the total is at least $n(n-1) = n^2 - n > n^2 - n - 1 = m$. **Contradiction.** No valid coloring exists. $\square$

## Step 3: Construction for all $m \geq n^2 - n$

We show that for every $m \geq n^2 - n$, a valid coloring exists.

Write $m = nq + r$ with $0 \leq r < n$. Since $m \geq n(n-1)$, we have $q \geq n - 1$.

**Construction.** Build the sequence from $q$ blocks, where each block is $1, 2, \ldots, n$. After each of the **first $r$ blocks**, insert one extra bead $X_i$ (of any color). The sequence is:
$$\underbrace{1, 2, \ldots, n, X_1}_{\text{block 1 + extra}}, \underbrace{1, 2, \ldots, n, X_2}_{\text{block 2 + extra}}, \ldots, \underbrace{1, 2, \ldots, n, X_r}_{\text{block } r \text{ + extra}}, \underbrace{1, 2, \ldots, n}_{\text{block } r+1}, \ldots, \underbrace{1, 2, \ldots, n}_{\text{block } q}$$

Total length: $r(n+1) + (q - r)n = qn + r = m$. ✓

The extra beads $X_1, \ldots, X_r$ can be **any** colors (e.g., all color 1).

**Verification.** We check that every window of $n+1$ consecutive beads contains all $n$ colors. We consider all possible window positions:

**Case 1: Window spans an insertion point $X_i$ (between block $i$ and block $i+1$, for $1 \leq i \leq r$).**

The beads around $X_i$ are $\ldots, n-1, n, X_i, 1, 2, \ldots$. A window of $n+1$ containing $X_i$ includes $k$ beads from the end of block $i$ (colors $n-k+1, \ldots, n$), the bead $X_i$, and $n-k$ beads from the start of block $i+1$ (colors $1, \ldots, n-k$), for some $0 \leq k \leq n$. The color set is:
$$\{n-k+1, \ldots, n\} \cup \{X_i\} \cup \{1, \ldots, n-k\} = \{1, \ldots, n\}. \quad \checkmark$$

**Case 2: Window spans a block boundary without an insertion point (between block $i$ and block $i+1$ for $r < i < q$).**

The transition is $\ldots, n, 1, 2, \ldots$. A window of $n+1$ spanning this boundary has $k$ beads from the end of block $i$ (colors $n-k+1, \ldots, n$) and $n+1-k$ beads from the start of block $i+1$ (colors $1, \ldots, n+1-k$). The color set is:
$$\{n-k+1, \ldots, n\} \cup \{1, \ldots, n+1-k\} = \{1, \ldots, n\}. \quad \checkmark$$

**Case 3: Window spans two consecutive insertion points $X_i$ and $X_{i+1}$.**

The distance between $X_i$ and $X_{i+1}$ is exactly $n+1$ (one full block of $n$ beads plus $X_{i+1}$). A window of $n+1$ starting at $X_i$ ends at $X_{i+1}$, containing $X_i, 1, 2, \ldots, n, X_{i+1}$. The color set includes $\{1, \ldots, n\}$. $\checkmark$

Any other window containing both insertion points also contains a full block $1, 2, \ldots, n$ between them. $\checkmark$

**Case 4: Window spans the wrap-around (end of block $q$ to start of block $1$).**

Block $q$ ends with color $n$ and block $1$ starts with color $1$. A window of $n+1$ spanning the wrap-around has $k$ beads from the end of block $q$ (colors $n-k+1, \ldots, n$) and $n+1-k$ beads from the start of the sequence.

- If $k \geq 1$: the first $n+1-k \leq n$ beads of the sequence are $1, 2, \ldots, n+1-k$. Color set: $\{n-k+1, \ldots, n\} \cup \{1, \ldots, n+1-k\} = \{1, \ldots, n\}$. $\checkmark$
- If $k = 0$: the window is the first $n+1$ beads: $1, 2, \ldots, n, X_1$. Color set: $\{1, \ldots, n\}$. $\checkmark$

**All cases are covered**, so the construction yields a valid coloring for every $m \geq n^2 - n$. $\square$

## Step 4: Conclusion

- **$m = n^2 - n - 1$ is impossible** (Step 2: counting argument).
- **All $m \geq n^2 - n$ are possible** (Step 3: explicit construction).

Therefore, the largest value of $m$ for which the task is not possible is:

$$\boxed{n^2 - n - 1}.$$
