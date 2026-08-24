# Devin CLI Trajectory

**Session**: quaint-tango
**Title**: 请读取当前目录下的problem.txt文件，解答其中的数学题。
**Work dir**: /data/math-agent-glm5.2-tmux-agents-dir/258-matrix-extreme-test
**Model**: glm-5-2
**Created**: 2026-08-08T05:38:27+00:00

## Statistics
- Total steps: 9
- Assistant steps: 4 (with thinking: 2)
- Tool steps: 1
- User steps: 4
- Total thinking: 118526 chars
- Total tool calls: 2
- Tool usage: {"read": 2}

---

## [0] User (node 2)
请读取当前目录下的problem.txt文件，解答其中的数学题。

---

## [1] User (node 8)
请读取当前目录下的problem.txt文件，解答其中的数学题。

---

## [2] User (node 14)
请读取当前目录下的problem.txt文件，解答其中的数学题。

---

## [3] User (node 21)
请读取当前目录下的problem.txt文件，解答其中的数学题。

---

## [4] Assistant (node 23)

**Tool calls:**
- `read` (read, Read file): {"file_path": "/data/math-agent-glm5.2-tmux-agents-dir/258-matrix-extreme-test/problem.txt"}

**Tool results:**
- [completed] 

---

## [5] Assistant (node 24)

**Tool calls:**
- `read` (read, Read file): {"file_path": "/data/math-agent-glm5.2-tmux-agents-dir/258-matrix-extreme-test/problem.txt"}

**Tool results:**
- [completed] 

---

## [6] Tool echo (node 25)
<file-view path="/data/math-agent-glm5.2-tmux-agents-dir/258-matrix-extreme-test/problem.txt" start_line="1" end_line="20" total_lines="20">
  1|你是数学大师。请解答以下数学题。
  2|
  3|题目（矩条件极差题第2问）：
  4|已知 a_1, a_2, ..., a_n 为实数，且
  5|  sum a_i = n, sum a_i^2 = 2n, sum a_i^3 = 3n。
  6|
  7|(1) 求最大的常数 C，使得对所有 n >= 4，max{a_1,...,a_n} - min{a_1,...,a_n} >= C。
  8|（第1问的答案是 C = sqrt(5)）
  9|
 10|(2) 证明存在常数 C2 > 0 使得
 11|  max{a_1,...,a_n} - min{a_1,...,a_n} >= sqrt(5) + C2 * n^(-3/2)。
 12|
 13|要求：
 14|1. 给出完

---

## [7] Assistant (node 26)

<details><summary>Thinking (59263 chars)</summary>

Let me carefully analyze this problem.

We have real numbers $a_1, a_2, \ldots, a_n$ with:
- $\sum a_i = n$
- $\sum a_i^2 = 2n$
- $\sum a_i^3 = 3n$

Part (1): The maximum of $\max - \min$ is $\sqrt{5}$, achieved in the limit as $n \to \infty$.

Part (2): Prove there exists $C_2 > 0$ such that $\max - \min \geq \sqrt{5} + C_2 \cdot n^{-3/2}$.

So we need to show that the gap $\max - \min$ is not just $\geq \sqrt{5}$, but actually $\geq \sqrt{5} + C_2 n^{-3/2}$ for some positive constant $C_2$.

Let me think about this carefully.

First, let me understand the structure. Let $M = \max a_i$ and $m = \min a_i$. We want to show $M - m \geq \sqrt{5} + C_2 n^{-3/2}$.

Let me think about what configuration achieves the minimum of $M - m$.

The moments are:
- $\bar{a} = \frac{1}{n}\sum a_i = 1$
- $\frac{1}{n}\sum a_i^2 = 2$, so variance $= 2 - 1 = 1$
- $\frac{1}{n}\sum a_i^3 = 3$, so third central moment: $\frac{1}{n}\sum (a_i - 1)^3 = \frac{1}{n}\sum a_i^3 - 3\frac{1}{n}\sum a_i^2 + 3\frac{1}{n}\sum a_i - 1 = 3 - 6 + 3 - 1 = -1$.

Wait, let me recompute. If $b_i = a_i - 1$, then:
- $\sum b_i = 0$
- $\sum b_i^2 = \sum a_i^2 - 2\sum a_i + n = 2n - 2n + n = n$
- $\sum b_i^3 = \sum a_i^3 - 3\sum a_i^2 + 3\sum a_i - n = 3n - 6n + 3n - n = -n$

So the $b_i$ have mean 0, second moment 1, third moment $-1$ (all per-element, i.e., $\frac{1}{n}\sum b_i^2 = 1$, $\frac{1}{n}\sum b_i^3 = -1$).

The skewness is $\frac{-1}{1^{3/2}} = -1$.

Now, $M - m = \max b_i - \min b_i$.

For the first part, the answer is $\sqrt{5}$. Let me think about what achieves this.

Consider a distribution that's a mixture: most values are at some point, and a few are at the extremes. In the limit $n \to \infty$, we can think of this as a probability distribution.

We want to minimize $\max - \min$ subject to:
- $E[X] = 0$ (where $X = b$)
- $E[X^2] = 1$
- $E[X^3] = -1$

The extremal distribution that minimizes the range... Let me think. The support should be on at most 3 points (by the moment problem theory, with 3 moment constraints, the extremal distribution has at most 3+1 = 4 support points, but actually for minimizing the range, it's likely 3 points: the two endpoints and possibly one interior point).

Actually, let me think about this differently. We want to minimize $M - m$ where $M = \max b_i$, $m = \min b_i$.

Let's say the support is $\{m, c, M\}$ with probabilities $p, q, r$ where $p + q + r = 1$.

Constraints:
- $pm + qc + rM = 0$
- $pm^2 + qc^2 + rM^2 = 1$
- $pm^3 + qc^3 + rM^3 = -1$

We want to minimize $M - m$.

Actually, for the continuous (limit) case, the minimum range is $\sqrt{5}$. Let me verify: if we use a 2-point distribution at $m$ and $M$ with probabilities $p$ and $r = 1-p$:
- $pm + (1-p)M = 0 \Rightarrow p = \frac{M}{M-m}$
- $pm^2 + (1-p)M^2 = 1$
- $pm^3 + (1-p)M^3 = -1$

From the first two: $p = \frac{M}{M-m}$, and $pm^2 + (1-p)M^2 = \frac{M m^2}{M-m} + \frac{-m M^2}{M-m} = \frac{Mm(m-M)}{M-m} = -Mm = 1$.

So $Mm = -1$, i.e., $m = -1/M$.

From the third: $pm^3 + (1-p)M^3 = \frac{M m^3 - m M^3}{M-m} = \frac{Mm(m^2 - M^2)}{M-m} = \frac{Mm(m-M)(m+M)}{M-m} = -Mm(m+M) = (m+M)$ (since $Mm = -1$).

So the third moment is $m + M = -1$, giving $m + M = -1$.

With $m = -1/M$: $-1/M + M = -1$, so $M^2 + M - 1 = 0$, giving $M = \frac{-1 + \sqrt{5}}{2}$ (taking positive root).

Then $m = -1/M = -\frac{2}{-1+\sqrt{5}} = -\frac{2(\sqrt{5}+1)}{4} = -\frac{\sqrt{5}+1}{2}$.

$M - m = \frac{-1+\sqrt{5}}{2} + \frac{\sqrt{5}+1}{2} = \sqrt{5}$.

So the 2-point distribution gives range $\sqrt{5}$. But can a 3-point distribution do better? Let me check.

With 3 points, we have more freedom. Let me think... Actually, with 3 moment constraints and 3 support points, we have 5 free parameters (3 locations + 2 probabilities) and 3 constraints, so 2 degrees of freedom. We want to minimize $M - m$.

Hmm, but actually the claim is that $\sqrt{5}$ is the minimum for the continuous case, and the finite-$n$ case has a correction of order $n^{-3/2}$.

Let me think about why the correction is $n^{-3/2}$.

In the finite case, we have $n$ points. The extremal configuration in the limit is a 2-point distribution: $p = \frac{M}{M-m}$ fraction at $m$ and $r = \frac{-m}{M-m}$ fraction at $M$.

With $M = \frac{\sqrt{5}-1}{2}$ and $m = -\frac{\sqrt{5}+1}{2}$:
- $p = \frac{M}{M-m} = \frac{(\sqrt{5}-1)/2}{\sqrt{5}} = \frac{\sqrt{5}-1}{2\sqrt{5}}$
- $r = \frac{-m}{M-m} = \frac{(\sqrt{5}+1)/2}{\sqrt{5}} = \frac{\sqrt{5}+1}{2\sqrt{5}}$

So $p = \frac{\sqrt{5}-1}{2\sqrt{5}} \approx \frac{1.236}{4.472} \approx 0.2764$ and $r \approx 0.7236$.

In the finite case, we need $pn$ points at $m$ and $rn$ points at $M$ (approximately). But $pn$ and $rn$ need to be integers, and the moments need to be exactly $n, 2n, 3n$.

Let me think about this more carefully. Let's say $k$ points are at $m$ and $n-k$ points are at $M$ (in the 2-point case). Then:
- $km + (n-k)M = n \Rightarrow km + (n-k)M = n$
- $km^2 + (n-k)M^2 = 2n$
- $km^3 + (n-k)M^3 = 3n$

From the first: $k(m-M) + nM = n$, so $k = \frac{n(1-M)}{M-m}$.
From the second: $k(m^2 - M^2) + nM^2 = 2n$, so $k(m-M)(m+M) = n(2 - M^2)$, so $\frac{n(1-M)}{M-m} \cdot (m-M)(m+M) = n(2-M^2)$, giving $-(1-M)(m+M) = 2 - M^2$.

So $-(m+M) + M(m+M) = 2 - M^2$, i.e., $-m - M + Mm + M^2 = 2 - M^2$, i.e., $-m - M + Mm + 2M^2 = 2$.

From the third: $k(m^3 - M^3) + nM^3 = 3n$, so $k(m-M)(m^2+mM+M^2) = n(3 - M^3)$, so $\frac{n(1-M)}{M-m}(m-M)(m^2+mM+M^2) = n(3-M^3)$, giving $-(1-M)(m^2+mM+M^2) = 3 - M^3$.

$-(m^2+mM+M^2) + M(m^2+mM+M^2) = 3 - M^3$
$-m^2 - mM - M^2 + Mm^2 + M^2m + M^3 = 3 - M^3$
$-m^2 - mM - M^2 + Mm^2 + M^2m + 2M^3 = 3$

This is getting complicated. Let me use a different approach.

Actually, for the 2-point distribution with $k$ points at $m$ and $n-k$ at $M$:

The per-element moments (dividing by $n$) are:
- $\frac{k}{n} m + (1-\frac{k}{n}) M = 1$
- $\frac{k}{n} m^2 + (1-\frac{k}{n}) M^2 = 2$
- $\frac{k}{n} m^3 + (1-\frac{k}{n}) M^3 = 3$

Let $\alpha = k/n$. Then:
- $\alpha m + (1-\alpha) M = 1$
- $\alpha m^2 + (1-\alpha) M^2 = 2$
- $\alpha m^3 + (1-\alpha) M^3 = 3$

From first two: $\alpha(m^2 - M^2) + M^2 = 2$, and $\alpha(m - M) + M = 1$, so $\alpha = \frac{1-M}{M-m}$.

$\frac{1-M}{M-m}(m^2 - M^2) + M^2 = 2$
$\frac{1-M}{M-m}(m-M)(m+M) + M^2 = 2$
$-(1-M)(m+M) + M^2 = 2$
$-m - M + Mm + M^2 + M^2 = 2$
$-m - M + Mm + 2M^2 = 2$ ... (i)

From first and third: $\alpha(m^3 - M^3) + M^3 = 3$:
$\frac{1-M}{M-m}(m-M)(m^2+mM+M^2) + M^3 = 3$
$-(1-M)(m^2+mM+M^2) + M^3 = 3$
$-m^2 - mM - M^2 + Mm^2 + mM^2 + M^3 + M^3 = 3$
$-m^2 - mM - M^2 + Mm^2 + mM^2 + 2M^3 = 3$ ... (ii)

From (i): $m(-1 + M) = 2 + M - 2M^2$, so $m = \frac{2 + M - 2M^2}{M - 1} = \frac{-(2 + M - 2M^2)}{1 - M} = \frac{2M^2 - M - 2}{1 - M}$.

Let me factor: $2M^2 - M - 2 = (2M + 1)(M - 2) + 2M - 2 + 2 = $... let me just compute. $2M^2 - M - 2$. Discriminant: $1 + 16 = 17$. Roots: $\frac{1 \pm \sqrt{17}}{4}$. So $2M^2 - M - 2 = 2(M - \frac{1+\sqrt{17}}{4})(M - \frac{1-\sqrt{17}}{4})$.

Hmm, this is getting messy. Let me try a computational approach.

Actually, let me think about this problem differently. The key insight is:

In the finite case, we can't exactly achieve the 2-point extremal distribution because $k = \alpha n$ must be an integer, and even if it is, the moments might not work out exactly. So we need to perturb.

Let me think about what happens when we use a 3-point distribution. The idea is:

1. Most points are at two values close to $m$ and $M$ (the extremal 2-point values).
2. A few points (like $O(1)$ or $O(\sqrt{n})$ points) are at a third value to adjust the moments.

Actually, let me think about the structure more carefully. The correction is $n^{-3/2}$, which suggests that the perturbation involves $O(\sqrt{n})$ points being moved, or something related to the discrete nature of the problem.

Let me think about it from the perspective of the dual problem. We want to show:

$$\max a_i - \min a_i \geq \sqrt{5} + C_2 n^{-3/2}$$

Equivalently, if $M - m < \sqrt{5} + C_2 n^{-3/2}$, we want to derive a contradiction with the moment conditions.

Let me set up the problem. Let $b_i = a_i - 1$, so $\sum b_i = 0$, $\sum b_i^2 = n$, $\sum b_i^3 = -n$.

Let $M = \max b_i$, $m = \min b_i$, $R = M - m$.

We want to show $R \geq \sqrt{5} + C_2 n^{-3/2}$.

**Approach**: Find a polynomial $P(x)$ of degree 3 such that $P(x) \leq x^3 + \alpha x^2 + \beta x + \gamma$ on $[m, M]$ (or some interval), and use the moment conditions to derive a bound on $R$.

Actually, let me think about this using the method of Lagrange multipliers / duality.

The key idea for part (1) is likely: find a cubic polynomial $p(x) = x^3 + ux^2 + vx + w$ such that $p(x) \leq 0$ for $x \in [m, M]$ when $M - m = \sqrt{5}$, and $p(x) = 0$ at $x = m$ and $x = M$. Then $\sum p(b_i) \leq 0$, but $\sum p(b_i) = \sum b_i^3 + u \sum b_i^2 + v \sum b_i + nw = -n + un + 0 + nw = n(u + w - 1)$. Setting this $\leq 0$ gives $u + w \leq 1$.

Hmm, let me think more carefully.

Actually, let me think about the dual approach for part (1) first, to understand the structure, then extend to part (2).

**Part (1) approach**: We want to show $R \geq \sqrt{5}$.

Suppose $R < \sqrt{5}$. We want to find a contradiction.

Consider the polynomial $q(x) = (x - m)(x - M)(x - c)$ for some $c$. On $[m, M]$, $(x-m)(x-M) \leq 0$, so $q(x) \leq 0$ on $[m, M]$ if $c \geq M$ or $c \leq m$ (i.e., $c$ is outside $[m, M]$), and $q(x) \geq 0$ if $c \in [m, M]$.

Actually, let me think about this differently. We want to use the fact that $\sum b_i^3 = -n$ to bound $R$.

Consider a quadratic $q(x) = (x - m)(x - M) = x^2 - (m+M)x + mM$. This is $\leq 0$ on $[m, M]$.

Now, $\sum q(b_i) = \sum b_i^2 - (m+M)\sum b_i + n \cdot mM = n + n \cdot mM = n(1 + mM)$.

Since $q(b_i) \leq 0$ for all $i$, we get $n(1 + mM) \leq 0$, so $mM \leq -1$.

Now, $R = M - m$, and $mM \leq -1$. By AM-GM or similar, $M - m \geq 2\sqrt{-mM} \geq 2$... but that only gives $R \geq 2$, not $\sqrt{5}$.

We need to use the third moment. Consider a cubic that factors through $m$ and $M$:

$p(x) = (x - m)(x - M)(x - c) = x^3 - (m+M+c)x^2 + (mM + c(m+M))x - cMm$.

On $[m, M]$, $(x-m)(x-M) \leq 0$. So $p(x) \leq 0$ on $[m, M]$ iff $x - c \geq 0$ on $[m, M]$, i.e., $c \leq m$. Or $p(x) \geq 0$ iff $c \geq M$.

Let's choose $c \leq m$ so that $p(x) \leq 0$ on $[m, M]$.

$\sum p(b_i) = \sum b_i^3 - (m+M+c)\sum b_i^2 + (mM + c(m+M))\sum b_i - ncMm$
$= -n - (m+M+c)n + 0 - ncMm$
$= -n(1 + m + M + c + cMm)$
$= -n(1 + m + M + c(1 + mM))$

Since $p(b_i) \leq 0$ for all $i$, $\sum p(b_i) \leq 0$, so $-n(1 + m + M + c(1 + mM)) \leq 0$, giving $1 + m + M + c(1 + mM) \geq 0$.

This holds for all $c \leq m$. As $c \to -\infty$:
- If $1 + mM > 0$: $c(1 + mM) \to -\infty$, so the inequality fails. But we showed $mM \leq -1$, so $1 + mM \leq 0$.
- If $1 + mM = 0$: the condition becomes $1 + m + M \geq 0$.
- If $1 + mM < 0$: $c(1 + mM) \to +\infty$ as $c \to -\infty$, so the condition is satisfied for very negative $c$. The binding constraint is at $c = m$: $1 + m + M + m(1 + mM) \geq 0$, i.e., $1 + m + M + m + m^2M \geq 0$, i.e., $1 + 2m + M + m^2 M \geq 0$.

Hmm, this is getting complicated. Let me try a different approach.

Actually, let me try the approach where we use a polynomial that touches zero at $m$ and $M$ and is non-positive on $[m, M]$.

For part (1), the extremal polynomial is likely $p(x) = (x - m)(x - M) \cdot q(x)$ where $q$ is linear, chosen so that the moment conditions give exactly $R = \sqrt{5}$.

Let me try $p(x) = (x - m)(x - M)(x - c)$ with $c$ chosen appropriately.

We have $\sum p(b_i) \leq 0$ (since $p \leq 0$ on $[m, M]$ and $c \leq m$).

$\sum p(b_i) = -n - (m+M+c)n - ncMm = -n(1 + m + M + c + cMm) = -n(1 + m + M + c(1+Mm))$

For this to be $\leq 0$: $1 + m + M + c(1 + Mm) \geq 0$.

We want to choose $c$ to get the tightest bound. Since $1 + Mm \leq 0$ (from the quadratic argument), and $c \leq m$:

If $1 + Mm < 0$, then $c(1 + Mm)$ is a decreasing function of $c$ (since $1 + Mm < 0$, larger $c$ gives more negative product). Wait no: if $1 + Mm < 0$ and $c$ is negative, then $c(1+Mm) > 0$. And as $c$ increases (towards $m$), $c(1+Mm)$ decreases. So the binding constraint is at $c = m$:

$1 + m + M + m(1 + Mm) \geq 0$
$1 + 2m + M + m^2 M \geq 0$
$1 + 2m + M(1 + m^2) \geq 0$
$M \geq -\frac{1 + 2m}{1 + m^2}$

Also, $R = M - m$, so $M = m + R$:
$m + R \geq -\frac{1 + 2m}{1 + m^2}$
$R \geq -\frac{1 + 2m}{1 + m^2} - m = \frac{-(1+2m) - m(1+m^2)}{1+m^2} = \frac{-1 - 2m - m - m^3}{1+m^2} = \frac{-1 - 3m - m^3}{1 + m^2}$

We want to minimize $R$ over $m$. Take derivative and set to 0:
$\frac{d}{dm}\frac{-1 - 3m - m^3}{1 + m^2} = \frac{(-3 - 3m^2)(1+m^2) - (-1-3m-m^3)(2m)}{(1+m^2)^2}$

Numerator: $(-3 - 3m^2)(1 + m^2) + 2m(1 + 3m + m^3)$
$= -3 - 3m^2 - 3m^2 - 3m^4 + 2m + 6m^2 + 2m^4$
$= -3 - 6m^2 - 3m^4 + 2m + 6m^2 + 2m^4$
$= -3 + 2m - m^4$
$= -(m^4 - 2m + 3)$

Hmm, $m^4 - 2m + 3 = 0$? Let me check: at $m = -1$: $1 + 2 + 3 = 6 \neq 0$. This doesn't have nice roots.

I think I'm overcomplicating this. Let me try a different approach.

Let me try the approach where we don't assume a 2-point distribution but instead use a more general polynomial.

Actually, let me reconsider. The standard approach for these moment problems is:

We want to show $R \geq \sqrt{5}$. Suppose all $b_i \in [m, M]$ with $M - m = R$. We need to find a polynomial $p(x)$ of degree $\leq 3$ such that:
1. $p(x) \leq 0$ for $x \in [m, M]$
2. $\sum p(b_i) > 0$ (using the moment conditions) when $R < \sqrt{5}$.

This gives a contradiction.

The polynomial $p(x) = (x - m)(x - M)(x - c)$ with $c \leq m$ satisfies condition 1. And:
$\sum p(b_i) = -n(1 + m + M + c(1 + Mm))$

For this to be $> 0$: $1 + m + M + c(1 + Mm) < 0$.

We want to find $c \leq m$ such that this holds, given $R < \sqrt{5}$.

Alternatively, let's use the polynomial $p(x) = (x - m)(x - M) \cdot (x - c)$ where we choose $c$ optimally.

Actually, I realize I should think about this more carefully. Let me use a slightly different approach.

Let me shift and scale. Let $b_i \in [m, M]$ with $M - m = R$. Let $t = \frac{M + m}{2}$ (midpoint) and $s = \frac{M - m}{2} = R/2$ (half-range). So $b_i \in [t - s, t + s]$.

Let $u_i = \frac{b_i - t}{s} \in [-1, 1]$. Then:
- $\sum b_i = 0 \Rightarrow \sum (t + su_i) = 0 \Rightarrow nt + s\sum u_i = 0 \Rightarrow \sum u_i = -nt/s$
- $\sum b_i^2 = n \Rightarrow \sum(t + su_i)^2 = n \Rightarrow nt^2 + 2ts\sum u_i + s^2 \sum u_i^2 = n$
- $\sum b_i^3 = -n \Rightarrow \sum(t + su_i)^3 = -n \Rightarrow nt^3 + 3t^2 s \sum u_i + 3ts^2 \sum u_i^2 + s^3 \sum u_i^3 = -n$

This is getting complicated. Let me try a computational approach to understand the problem better.

Let me use Python/SymPy to explore.

Actually, let me think about the problem from a higher level.

The key question is: why is the correction $n^{-3/2}$?

In the extremal 2-point distribution, we need $\alpha n$ points at $m$ and $(1-\alpha)n$ points at $M$, where $\alpha = \frac{\sqrt{5}-1}{2\sqrt{5}}$. Since $\alpha$ is irrational, we can't have exactly $\alpha n$ points. The rounding error is at most 1, which gives a correction of order $1/n$ to the moments. But the correction to the range is $n^{-3/2}$, which is larger than $n^{-1}$ for large $n$... wait, no, $n^{-3/2} < n^{-1}$ for large $n$. So the correction is smaller.

Hmm, actually $n^{-3/2}$ is smaller than $n^{-1}$. So the finite-$n$ correction is quite small. This suggests that the 2-point distribution with rounding is not the binding constraint; rather, there's a more subtle effect.

Let me think about this differently. Maybe the extremal configuration for finite $n$ is not a 2-point distribution but a 3-point distribution, and the third point accounts for the correction.

Let me consider the following: $k$ points at $m$, $\ell$ points at $c$ (interior), and $n - k - \ell$ points at $M$. We want to minimize $M - m$.

In the limit $n \to \infty$, the optimal is the 2-point distribution with $\ell = 0$. For finite $n$, we might need $\ell > 0$ to satisfy the moment conditions exactly.

Let me think about what happens with the 2-point distribution when $k$ is not exactly $\alpha n$.

Let $k = \lfloor \alpha n \rfloor$ (or nearby). Then with $k$ points at $m$ and $n - k$ at $M$:
- $km + (n-k)M = n$
- $km^2 + (n-k)M^2 = 2n$
- $km^3 + (n-k)M^3 = 3n$

Three equations, two unknowns ($m, M$), so the system is overdetermined. We can satisfy two of the three equations, and the third will have a residual.

From the first two equations, we can solve for $m$ and $M$ given $k$:
- $m + M = \frac{2n - km^2 - (n-k)M^2}{...}$... this is circular.

Let me use the first two equations:
$km + (n-k)M = n$ ... (1)
$km^2 + (n-k)M^2 = 2n$ ... (2)

From (1): $M = \frac{n - km}{n - k}$.
Substitute into (2): $km^2 + (n-k)\left(\frac{n-km}{n-k}\right)^2 = 2n$
$km^2 + \frac{(n-km)^2}{n-k} = 2n$
$\frac{km^2(n-k) + (n-km)^2}{n-k} = 2n$
$km^2(n-k) + n^2 - 2nkm + k^2m^2 = 2n(n-k)$
$m^2(k(n-k) + k^2) + n^2 - 2nkm = 2n^2 - 2nk$
$m^2 \cdot kn + n^2 - 2nkm = 2n^2 - 2nk$
$m^2 kn - 2nkm + n^2 - 2n^2 + 2nk = 0$
$kn \cdot m^2 - 2nkm - n^2 + 2nk = 0$
$kn \cdot m^2 - 2nkm + n(2k - n) = 0$
$km^2 - 2km + (2k - n) = 0$ (dividing by $n$)
$km^2 - 2km + 2k - n = 0$
$m = \frac{2k \pm \sqrt{4k^2 - 4k(2k-n)}}{2k} = \frac{2k \pm \sqrt{4k^2 - 8k^2 + 4kn}}{2k} = \frac{2k \pm 2\sqrt{kn - k^2}}{2k} = 1 \pm \frac{\sqrt{k(n-k)}}{k} = 1 \pm \sqrt{\frac{n-k}{k}}$

So $m = 1 - \sqrt{\frac{n-k}{k}}$ and $M = 1 + \sqrt{\frac{k}{n-k}}$ (taking $m < M$).

Then $R = M - m = \sqrt{\frac{k}{n-k}} + \sqrt{\frac{n-k}{k}} = \frac{k + (n-k)}{\sqrt{k(n-k)}} = \frac{n}{\sqrt{k(n-k)}}$.

Now check the third moment:
$km^3 + (n-k)M^3 = ?$

Let $\beta = k/n$, so $m = 1 - \sqrt{\frac{1-\beta}{\beta}}$ and $M = 1 + \sqrt{\frac{\beta}{1-\beta}}$.

$km^3 + (n-k)M^3 = n[\beta m^3 + (1-\beta) M^3]$

Let $u = \sqrt{\frac{1-\beta}{\beta}}$ and $v = \sqrt{\frac{\beta}{1-\beta}}$, so $uv = 1$, $m = 1 - u$, $M = 1 + v$.

$\beta(1-u)^3 + (1-\beta)(1+v)^3$
$= \beta(1 - 3u + 3u^2 - u^3) + (1-\beta)(1 + 3v + 3v^2 + v^3)$
$= 1 + 3[-\beta u + (1-\beta)v] + 3[\beta u^2 + (1-\beta)v^2] + [-\beta u^3 + (1-\beta)v^3]$

Now, $\beta u = \beta\sqrt{\frac{1-\beta}{\beta}} = \sqrt{\beta(1-\beta)}$ and $(1-\beta)v = (1-\beta)\sqrt{\frac{\beta}{1-\beta}} = \sqrt{\beta(1-\beta)}$. So $-\beta u + (1-\beta)v = 0$.

$\beta u^2 = \beta \cdot \frac{1-\beta}{\beta} = 1-\beta$ and $(1-\beta)v^2 = (1-\beta) \cdot \frac{\beta}{1-\beta} = \beta$. So $\beta u^2 + (1-\beta)v^2 = 1$.

$\beta u^3 = \beta \cdot \frac{(1-\beta)^{3/2}}{\beta^{3/2}} = \frac{(1-\beta)^{3/2}}{\beta^{1/2}}$ and $(1-\beta)v^3 = (1-\beta) \cdot \frac{\beta^{3/2}}{(1-\beta)^{3/2}} = \frac{\beta^{3/2}}{(1-\beta)^{1/2}}$.

So $-\beta u^3 + (1-\beta)v^3 = -\frac{(1-\beta)^{3/2}}{\beta^{1/2}} + \frac{\beta^{3/2}}{(1-\beta)^{1/2}} = \frac{-(1-\beta)^2 + \beta^2}{\beta^{1/2}(1-\beta)^{1/2}} = \frac{-(1-2\beta+\beta^2) + \beta^2}{\sqrt{\beta(1-\beta)}} = \frac{-1+2\beta}{\sqrt{\beta(1-\beta)}}$.

So the third moment sum is:
$n\left[1 + 0 + 3 + \frac{-1+2\beta}{\sqrt{\beta(1-\beta)}}\right] = n\left[4 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}\right]$

We need this to equal $3n$:
$4 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}} = 3$
$\frac{2\beta - 1}{\sqrt{\beta(1-\beta)}} = -1$
$2\beta - 1 = -\sqrt{\beta(1-\beta)}$

For this to have a solution, we need $2\beta - 1 < 0$, i.e., $\beta < 1/2$.

Squaring: $(2\beta - 1)^2 = \beta(1-\beta)$
$4\beta^2 - 4\beta + 1 = \beta - \beta^2$
$5\beta^2 - 5\beta + 1 = 0$
$\beta = \frac{5 \pm \sqrt{25 - 20}}{10} = \frac{5 \pm \sqrt{5}}{10}$

Since $\beta < 1/2$: $\beta = \frac{5 - \sqrt{5}}{10}$.

And $1 - \beta = \frac{5 + \sqrt{5}}{10}$.

$R = \frac{n}{\sqrt{k(n-k)}} = \frac{n}{n\sqrt{\beta(1-\beta)}} = \frac{1}{\sqrt{\beta(1-\beta)}}$.

$\beta(1-\beta) = \frac{(5-\sqrt{5})(5+\sqrt{5})}{100} = \frac{25 - 5}{100} = \frac{20}{100} = \frac{1}{5}$.

So $R = \frac{1}{\sqrt{1/5}} = \sqrt{5}$. 

This confirms part (1): the 2-point distribution with $\beta = \frac{5-\sqrt{5}}{10}$ gives $R = \sqrt{5}$.

Now for part (2), the key issue is that $\beta = \frac{5-\sqrt{5}}{10}$ is irrational, so $k = \beta n$ is never an integer. When $k$ is not exactly $\beta n$, the third moment condition is not satisfied, and we need to adjust.

Let me think about this. If we use a 2-point distribution with $k$ points at $m$ and $n-k$ at $M$ (satisfying the first two moment conditions), the third moment is:

$T(k) = n\left[4 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}\right]$ where $\beta = k/n$.

We need $T(k) = 3n$, i.e., $g(\beta) := 4 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}} = 3$, i.e., $\frac{2\beta - 1}{\sqrt{\beta(1-\beta)}} = -1$.

This is only satisfied at $\beta^* = \frac{5-\sqrt{5}}{10}$.

For $\beta \neq \beta^*$, $g(\beta) \neq 3$, so the third moment is not $3n$. The residual is:

$T(k) - 3n = n[g(\beta) - 3] = n \cdot h(\beta)$

where $h(\beta) = 1 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}$.

$h(\beta^*) = 0$. Let's compute $h'(\beta^*)$.

$h(\beta) = 1 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}$

Let $f(\beta) = \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}$.

$f'(\beta) = \frac{2\sqrt{\beta(1-\beta)} - (2\beta-1) \cdot \frac{1-2\beta}{2\sqrt{\beta(1-\beta)}}}{\beta(1-\beta)} = \frac{2\beta(1-\beta) - \frac{(2\beta-1)(1-2\beta)}{2}}{[\beta(1-\beta)]^{3/2}}$

$= \frac{2\beta(1-\beta) + \frac{(2\beta-1)^2}{2}}{[\beta(1-\beta)]^{3/2}} = \frac{4\beta(1-\beta) + (2\beta-1)^2}{2[\beta(1-\beta)]^{3/2}} = \frac{4\beta - 4\beta^2 + 4\beta^2 - 4\beta + 1}{2[\beta(1-\beta)]^{3/2}} = \frac{1}{2[\beta(1-\beta)]^{3/2}}$

So $f'(\beta) = \frac{1}{2[\beta(1-\beta)]^{3/2}}$.

At $\beta^*$: $\beta^*(1-\beta^*) = 1/5$, so $f'(\beta^*) = \frac{1}{2(1/5)^{3/2}} = \frac{1}{2 \cdot 5^{-3/2}} = \frac{5^{3/2}}{2} = \frac{5\sqrt{5}}{2}$.

So $h'(\beta^*) = f'(\beta^*) = \frac{5\sqrt{5}}{2}$.

Now, if $\beta = k/n$ and $k$ is the nearest integer to $\beta^* n$, then $|\beta - \beta^*| \approx \frac{1}{n}$ (the rounding error). More precisely, $|\beta - \beta^*| \leq \frac{1}{2n}$.

So $h(\beta) \approx h'(\beta^*) \cdot (\beta - \beta^*) \approx \frac{5\sqrt{5}}{2} \cdot O(1/n)$.

And $T(k) - 3n = n \cdot h(\beta) \approx \frac{5\sqrt{5}}{2} \cdot O(1) = O(1)$.

So the third moment residual is $O(1)$, not $O(n)$. This means we need to correct the third moment by $O(1)$, which can be done by moving $O(1)$ points to a third value. But this would give a correction to $R$ of order... let me think.

If we move one point from $M$ to some value $c$, the change in the third moment is $c^3 - M^3$, and we need this to be $O(1)$. So $c$ is close to $M$, with $c - M = O(1/M^2) = O(1)$. This doesn't directly change $R$ unless $c > M$ or $c < m$.

Hmm, let me think more carefully. The issue is that with a 2-point distribution, we can satisfy the first two moments exactly but the third moment is off by $O(1)$. To fix the third moment, we need to introduce a third point or adjust the existing points.

Let me consider a 3-point distribution: $k$ points at $m$, $1$ point at $c$, and $n - k - 1$ points at $M$.

The moment conditions become:
- $km + c + (n-k-1)M = n$
- $km^2 + c^2 + (n-k-1)M^2 = 2n$
- $km^3 + c^3 + (n-k-1)M^3 = 3n$

We have 3 unknowns ($m, M, c$) and 3 equations, plus $k$ is a free integer parameter. We want to minimize $M - m$.

Actually, let me think about this differently. Let me consider the general approach.

Let me use the dual/LP approach. We want to show that for any $b_1, \ldots, b_n$ with $\sum b_i = 0$, $\sum b_i^2 = n$, $\sum b_i^3 = -n$, we have $\max b_i - \min b_i \geq \sqrt{5} + C_2 n^{-3/2}$.

The approach is to find a polynomial $p(x)$ of degree 3 such that:
1. $p(x) \leq (x - m_0)(x - M_0)$ for $x \in [m, M]$ where $m_0, M_0$ are the extremal values... 

Actually, let me think about this more carefully using the polynomial method.

**Key idea**: We want to find a cubic polynomial $p(x) = x^3 + ax^2 + bx + c$ such that $p(x) \leq 0$ for all $x \in [m, M]$ (where $M - m = R$), and $\sum p(b_i) = -n + an + cn = n(a + c - 1)$. If $a + c - 1 > 0$, then $\sum p(b_i) > 0$, contradicting $p \leq 0$ on $[m, M]$.

Wait, I need to be more careful. $\sum p(b_i) = \sum b_i^3 + a \sum b_i^2 + b \sum b_i + nc = -n + an + 0 + nc = n(a + c - 1)$.

For the contradiction: if $p(x) \leq 0$ on $[m, M]$ and $a + c > 1$, then $\sum p(b_i) = n(a + c - 1) > 0$ but $\sum p(b_i) \leq 0$, contradiction.

So we need: for any $[m, M]$ with $M - m < \sqrt{5} + C_2 n^{-3/2}$, there exists a cubic $p(x) = x^3 + ax^2 + bx + c$ with $p \leq 0$ on $[m, M]$ and $a + c > 1$.

But actually, the constraint is that $p \leq 0$ on $[m, M]$ and $p$ is a cubic with leading coefficient 1. A cubic with positive leading coefficient goes to $+\infty$ as $x \to +\infty$ and $-\infty$ as $x \to -\infty$. For it to be $\leq 0$ on $[m, M]$, it needs to have roots at or outside $m$ and $M$.

The best we can do is $p(x) = (x - m)(x - M)(x - c)$ with $c \leq m$ (so that on $[m, M]$, $(x-m) \geq 0$, $(x-M) \leq 0$, $(x-c) \geq 0$, so $p \leq 0$).

$p(x) = x^3 - (m + M + c)x^2 + (mM + c(m+M))x - cmM$

So $a = -(m+M+c)$, $b = mM + c(m+M)$, $c_{\text{coeff}} = -cmM$.

$a + c_{\text{coeff}} = -(m+M+c) - cmM = -(m + M + c + cmM) = -(m + M + c(1 + mM))$.

We need $a + c_{\text{coeff}} > 1$, i.e., $-(m + M + c(1 + mM)) > 1$, i.e., $m + M + c(1 + mM) < -1$.

We want to maximize $-(m + M + c(1 + mM))$ over $c \leq m$.

If $1 + mM < 0$ (which we know is the case, since $mM \leq -1$), then $c(1 + mM)$ is maximized when $c$ is minimized (most negative). As $c \to -\infty$, $c(1+mM) \to +\infty$ (since $1 + mM < 0$), so $m + M + c(1+mM) \to -\infty$, and the condition is satisfied.

Wait, but that can't be right—if $c \to -\infty$, the condition is always satisfied, which would mean $R$ can be anything. The issue is that $p(x) = (x-m)(x-M)(x-c)$ with $c \to -\infty$ is not $\leq 0$ on $[m, M]$ in a useful way... wait, it is $\leq 0$ on $[m, M]$ for any $c \leq m$.

But the point is that we need $p \leq 0$ on $[m, M]$ AND $a + c_{\text{coeff}} > 1$. If $1 + mM < 0$, then for $c$ sufficiently negative, $a + c_{\text{coeff}} \to +\infty$, so the condition is satisfied. But this would mean any $R$ works, which is wrong.

I think the issue is that I need $p(x) \leq 0$ on $[m, M]$, but $p$ is a specific cubic (with leading coefficient 1), and the condition $a + c > 1$ depends on $m, M, c$. Let me re-examine.

Actually wait, the condition is $p(x) \leq 0$ for all $x \in [m, M]$. With $p(x) = (x-m)(x-M)(x-c)$ and $c \leq m$:
- For $x \in [m, M]$: $(x-m) \geq 0$, $(x-M) \leq 0$, $(x-c) \geq 0$ (since $c \leq m \leq x$). So $p(x) = (+)(-)(+) \leq 0$. ✓

And $a + c_{\text{coeff}} = -(m + M + c(1 + mM))$.

With $1 + mM \leq 0$ and $c \leq m$:
- If $1 + mM < 0$: as $c \to -\infty$, $c(1+mM) \to +\infty$, so $a + c_{\text{coeff}} \to -\infty$. That's bad.
- Wait, $a + c_{\text{coeff}} = -(m + M + c(1+mM))$. If $c(1+mM) \to +\infty$, then $m + M + c(1+mM) \to +\infty$, so $a + c_{\text{coeff}} \to -\infty$. So the condition $a + c_{\text{coeff}} > 1$ is NOT satisfied.

Let me redo: we need $m + M + c(1 + mM) < -1$.

With $1 + mM < 0$ and $c \leq m$ (both negative, say):
- $c(1+mM) = c \cdot (\text{negative})$. If $c < 0$, then $c(1+mM) > 0$.
- As $c$ increases (towards $m$), $c(1+mM)$ decreases (since $1+mM < 0$).
- So $m + M + c(1+mM)$ is maximized when $c$ is most negative, and minimized when $c = m$.

So the binding constraint is at $c = m$:
$m + M + m(1 + mM) = m + M + m + m^2M = 2m + M + m^2 M = 2m + M(1 + m^2)$

We need $2m + M(1 + m^2) < -1$.

With $M = m + R$:
$2m + (m+R)(1 + m^2) < -1$
$2m + m + m^3 + R + Rm^2 < -1$
$3m + m^3 + R(1 + m^2) < -1$
$R(1 + m^2) < -1 - 3m - m^3$
$R < \frac{-1 - 3m - m^3}{1 + m^2}$ (if $1 + m^2 > 0$, which it always is)

Wait, we need $R$ to satisfy this for the contradiction to work. But we're trying to show $R \geq \sqrt{5}$, so we need: if $R < \sqrt{5}$, then there exist $m, c$ such that the conditions hold.

Hmm, I think I have the logic backwards. Let me reconsider.

We want to show $R \geq \sqrt{5}$. The approach is:

Assume $R < \sqrt{5}$. We want to derive a contradiction.

For any $m$ (and $M = m + R$), if we can find $c \leq m$ such that $m + M + c(1+mM) < -1$, then we have our contradiction.

The best $c$ is $c = m$ (as argued above), giving the condition:
$2m + M(1 + m^2) < -1$

But this needs to hold for the SPECIFIC $m$ and $M$ of the given configuration. We don't get to choose $m$; it's determined by the $b_i$.

Hmm, but actually, we do get to choose the polynomial. The polynomial $p(x) = (x-m)(x-M)(x-c)$ depends on $m$ and $M$, which are the actual min and max of the $b_i$. So $m$ and $M$ are given, and we choose $c$.

So the condition for contradiction is: $2m + M(1 + m^2) < -1$ where $M = m + R$.

This is: $2m + (m+R)(1+m^2) < -1$, i.e., $R < \frac{-1 - 3m - m^3}{1 + m^2}$.

We need this to hold for the given $m$. But $m$ could be anything (subject to the moment constraints). So we need: for all valid $m$, $\sqrt{5} \leq \frac{-1 - 3m - m^3}{1 + m^2}$?

No, that's not right either. The logic is: if $R < \sqrt{5}$, then for the specific $m$ of the configuration, we need $R < \frac{-1 - 3m - m^3}{1 + m^2}$ to get a contradiction. But this might not hold for all $m$.

I think the correct approach is different. Let me reconsider.

Actually, I think the right approach is to optimize over $c$ (not just set $c = m$). The condition is:

$m + M + c(1 + mM) < -1$ for some $c \leq m$.

If $1 + mM < 0$: the LHS is minimized at $c = m$ (as argued), giving $2m + M(1+m^2) < -1$.
If $1 + mM = 0$: the condition is $m + M < -1$, and $mM = -1$.
If $1 + mM > 0$: the LHS is minimized at $c \to -\infty$, giving $-\infty < -1$, always true. But we showed $mM \leq -1$, so $1 + mM \leq 0$.

So the binding case is $1 + mM < 0$ and $c = m$, giving $2m + M(1 + m^2) < -1$.

Now, we also have the constraint from the quadratic: $\sum (b_i - m)(b_i - M) \leq 0$, giving $n(1 + mM) \leq 0$, i.e., $mM \leq -1$.

And $R = M - m$, $M = m + R$, so $m(m+R) \leq -1$, i.e., $m^2 + mR + 1 \leq 0$.

This gives $m \in \left[\frac{-R - \sqrt{R^2 - 4}}{2}, \frac{-R + \sqrt{R^2 - 4}}{2}\right]$ (requires $R \geq 2$).

Now, for the cubic condition: $2m + (m+R)(1+m^2) < -1$, i.e., $f(m) := 3m + m^3 + R(1+m^2) + 1 < 0$.

We need: for all $m$ in the valid range (from the quadratic constraint), $f(m) < 0$.

Actually, we need: there exists $m$ (the actual min of the $b_i$) such that $f(m) \geq 0$ would mean no contradiction. We want to show that for $R < \sqrt{5}$, $f(m) < 0$ for all valid $m$, giving a contradiction.

Wait, I'm confusing myself. Let me restart the logic.

We have a specific configuration $b_1, \ldots, b_n$ with specific $m = \min b_i$ and $M = \max b_i$. We want to show $R = M - m \geq \sqrt{5}$.

Assume $R < \sqrt{5}$. Then:
1. From the quadratic: $mM \leq -1$, so $m$ is in a certain range.
2. From the cubic (with $c = m$): if $2m + M(1+m^2) < -1$, i.e., $f(m) < 0$, then we have a contradiction (since $\sum p(b_i) > 0$ but $p \leq 0$ on $[m,M]$).

So we need: for all $m$ satisfying the quadratic constraint $m(m+R) \leq -1$ (with $R < \sqrt{5}$), we have $f(m) = 3m + m^3 + R(1+m^2) + 1 < 0$.

Hmm wait, but $m$ is not free—it's the actual minimum of the $b_i$. The quadratic constraint gives a necessary condition on $m$, but $m$ could be any value satisfying it. We need the cubic condition to give a contradiction for ALL possible $m$.

Actually, I realize the logic should be: we need to show that for $R < \sqrt{5}$, for EVERY valid $m$ (i.e., every $m$ with $m(m+R) \leq -1$), the cubic condition $f(m) < 0$ holds. This would mean no matter what $m$ is, we get a contradiction.

But actually, it's possible that for some $m$, $f(m) \geq 0$, meaning the cubic approach with $c = m$ doesn't give a contradiction. In that case, we might need a different $c$ or a different polynomial.

Let me just compute. We have $f(m) = m^3 + (R+3)m + Rm^2 + R + 1 = m^3 + Rm^2 + (R+3)m + (R+1)$.

Wait, let me recompute: $f(m) = 3m + m^3 + R(1+m^2) + 1 = m^3 + Rm^2 + 3m + R + 1$.

We want $f(m) < 0$ for all $m$ in the valid range.

The valid range from $m^2 + Rm + 1 \leq 0$ is $m \in \left[\frac{-R - \sqrt{R^2-4}}{2}, \frac{-R + \sqrt{R^2-4}}{2}\right]$ (for $R \geq 2$).

At the endpoints, $m^2 + Rm + 1 = 0$, so $mM = -1$ (equality in the quadratic constraint).

Let me evaluate $f$ at the endpoints. Let $m_0 = \frac{-R + \sqrt{R^2-4}}{2}$ (the upper endpoint, less negative) and $m_1 = \frac{-R - \sqrt{R^2-4}}{2}$ (the lower endpoint, more negative).

At $m_0$: $m_0^2 = -Rm_0 - 1$, so $m_0^3 = -Rm_0^2 - m_0 = -R(-Rm_0 - 1) - m_0 = R^2 m_0 + R - m_0 = (R^2-1)m_0 + R$.

$f(m_0) = (R^2-1)m_0 + R + Rm_0^2 + 3m_0 + R + 1 = (R^2-1)m_0 + R + R(-Rm_0 - 1) + 3m_0 + R + 1$
$= (R^2-1)m_0 + R - R^2 m_0 - R + 3m_0 + R + 1$
$= (R^2 - 1 - R^2 + 3)m_0 + R + 1$
$= 2m_0 + R + 1$
$= 2 \cdot \frac{-R + \sqrt{R^2-4}}{2} + R + 1$
$= -R + \sqrt{R^2-4} + R + 1$
$= \sqrt{R^2-4} + 1$

This is always $> 0$! So $f(m_0) > 0$, meaning the cubic approach with $c = m$ does NOT give a contradiction at $m = m_0$.

Hmm, so the approach with $c = m$ doesn't work at the boundary. Let me try $c < m$.

At $m = m_0$ (where $mM = -1$, i.e., $1 + mM = 0$): the condition becomes $m + M + c \cdot 0 < -1$, i.e., $m + M < -1$, i.e., $2m + R < -1$, i.e., $m < \frac{-1-R}{2}$.

$m_0 = \frac{-R + \sqrt{R^2-4}}{2}$. Is $m_0 < \frac{-1-R}{2}$? This is $\sqrt{R^2-4} < -1$, which is false (since $\sqrt{R^2-4} \geq 0$). So at $m = m_0$, the cubic condition fails for all $c$.

This means the polynomial approach with a single cubic doesn't work at the boundary $mM = -1$. We need a different approach.

Let me reconsider. Maybe we need to use a quartic polynomial, or a different type of argument.

Actually, wait. At $mM = -1$ (equality in the quadratic), the quadratic $(x-m)(x-M) \leq 0$ on $[m,M]$ and $\sum (b_i - m)(b_i - M) = 0$. This means $(b_i - m)(b_i - M) = 0$ for all $i$, i.e., every $b_i$ is either $m$ or $M$. So the configuration is a 2-point distribution!

In that case, the cubic condition is exactly the third moment condition, and we've already shown that the 2-point distribution gives $R = \sqrt{5}$ when the third moment is satisfied. So for $R < \sqrt{5}$, the 2-point distribution can't satisfy all three moments.

But the issue is: for $R < \sqrt{5}$, the quadratic constraint $mM \leq -1$ is satisfied with strict inequality for most $m$, and the cubic gives a contradiction. But at the boundary $mM = -1$, the configuration is forced to be 2-point, and the third moment gives $R = \sqrt{5}$ exactly.

So the argument for part (1) is:
- If $mM < -1$: use the cubic to get a contradiction when $R < \sqrt{5}$.
- If $mM = -1$: the configuration is 2-point, and the third moment forces $R = \sqrt{5}$.

Let me verify the first case. If $mM < -1$ (strict), then $1 + mM < 0$, and we can choose $c < m$ such that $m + M + c(1+mM) < -1$. Specifically, we need $c > \frac{-1 - m - M}{1 + mM}$ (note: $1 + mM < 0$, so dividing flips the inequality). We need $c \leq m$, so we need $\frac{-1 - m - M}{1 + mM} < m$, i.e., $-1 - m - M > m(1 + mM)$ (flipping because $1 + mM < 0$), i.e., $-1 - m - M - m - m^2 M > 0$, i.e., $-1 - 2m - M - m^2 M > 0$, i.e., $1 + 2m + M(1 + m^2) < 0$, i.e., $f(m) < 0$ (where $f$ is as before).

So we need $f(m) < 0$ for all $m$ in the interior of the valid range (where $mM < -1$).

$f(m) = m^3 + Rm^2 + (R+3)m + (R+1)$.

We showed $f(m_0) = \sqrt{R^2 - 4} + 1 > 0$ and by symmetry (or computation), $f(m_1) = -\sqrt{R^2-4} + 1$... let me check.

At $m_1 = \frac{-R - \sqrt{R^2-4}}{2}$: similarly, $m_1^2 = -Rm_1 - 1$, $m_1^3 = (R^2-1)m_1 + R$.

$f(m_1) = 2m_1 + R + 1 = 2 \cdot \frac{-R - \sqrt{R^2-4}}{2} + R + 1 = -R - \sqrt{R^2-4} + R + 1 = 1 - \sqrt{R^2-4}$.

So $f(m_1) = 1 - \sqrt{R^2 - 4}$.

For $R < \sqrt{5}$: $R^2 < 5$, $R^2 - 4 < 1$, $\sqrt{R^2-4} < 1$, so $f(m_1) > 0$.

And $f(m_0) = 1 + \sqrt{R^2-4} > 0$ always.

So $f > 0$ at both endpoints! This means the cubic approach with $c = m$ doesn't give a contradiction at either endpoint.

But wait—at the endpoints, $mM = -1$, so the configuration is 2-point, and we handle that separately. The question is whether $f < 0$ in the interior.

Let's check $f$ at the midpoint $m = -R/2$ (the center of the valid range):

$f(-R/2) = (-R/2)^3 + R(-R/2)^2 + (R+3)(-R/2) + (R+1)$
$= -R^3/8 + R^3/4 - R^2/2 - 3R/2 + R + 1$
$= R^3/8 - R^2/2 - R/2 + 1$
$= \frac{R^3 - 4R^2 - 4R + 8}{8}$

At $R = \sqrt{5}$: $R^3 = 5\sqrt{5}$, $R^2 = 5$.
$\frac{5\sqrt{5} - 20 - 4\sqrt{5} + 8}{8} = \frac{\sqrt{5} - 12}{8} \approx \frac{2.236 - 12}{8} \approx \frac{-9.764}{8} \approx -1.22 < 0$.

So at $R = \sqrt{5}$, $f(-R/2) < 0$. Good.

At $R = 2$: $\frac{8 - 16 - 8 + 8}{8} = \frac{-8}{8} = -1 < 0$.

So $f$ is negative in the interior. The issue is only at the boundary. So the argument is:

For $R < \sqrt{5}$:
- If $mM = -1$ (boundary): 2-point distribution, third moment forces $R \geq \sqrt{5}$, contradiction.
- If $mM < -1$ (interior): $f(m) < 0$ for $m$ in the interior, so the cubic gives a contradiction.

But we need to verify that $f(m) < 0$ for all $m$ in the open interval $(m_1, m_0)$ when $R < \sqrt{5}$.

$f$ is a cubic in $m$ with positive leading coefficient. $f(m_0) > 0$ and $f(m_1) > 0$ (for $R < \sqrt{5}$). So $f$ could be negative in between (if it dips below 0) or positive throughout. We need to check that $f$ is negative somewhere in the interval, and actually that it's negative for all $m$ in the interior.

Hmm, actually $f$ doesn't need to be negative for ALL $m$ in the interior. It needs to be negative for the SPECIFIC $m$ of the configuration. But we don't know $m$; we need the argument to work for all possible $m$.

Wait, but if $mM < -1$ (interior), then $m$ is in the open interval $(m_1, m_0)$, and we need $f(m) < 0$ for the contradiction. If $f(m) > 0$ for some $m$ in the interior, then for that $m$, the cubic approach doesn't give a contradiction, and we'd need a different argument.

Let me check: is $f$ negative throughout the open interval $(m_1, m_0)$ for $R < \sqrt{5}$?

$f(m_0) = 1 + \sqrt{R^2-4} > 0$ and $f(m_1) = 1 - \sqrt{R^2-4}$. For $R < \sqrt{5}$, $\sqrt{R^2-4} < 1$, so $f(m_1) > 0$.

So $f > 0$ at both endpoints. For $f$ to be negative in the interior, it must have a local min below 0 in the interval.

$f'(m) = 3m^2 + 2Rm + (R+3)$.

Discriminant: $4R^2 - 12(R+3) = 4R^2 - 12R - 36 = 4(R^2 - 3R - 9)$.

For $R = \sqrt{5} \approx 2.236$: $R^2 - 3R - 9 = 5 - 6.708 - 9 = -10.708 < 0$. So $f' > 0$ everywhere, meaning $f$ is increasing. But $f(m_0) > 0$ and $f$ is increasing, so $f > 0$ on $[m_0, \infty)$ and $f < 0$ on $(-\infty, m_0)$... wait, if $f$ is increasing and $f(m_0) > 0$, then $f < 0$ for $m < m_0$ (some $m$). But $m_1 < m_0$, and $f(m_1) > 0$, so $f > 0$ on $[m_1, m_0]$.

This means $f > 0$ on the entire valid interval! So the cubic approach with $c = m$ does NOT give a contradiction in the interior either!

I must be making an error. Let me reconsider the approach.

Hmm, maybe the issue is that I should be using a different polynomial, not just $(x-m)(x-M)(x-c)$.

Let me reconsider. The general approach is: find a polynomial $p(x) = x^3 + ax^2 + bx + d$ such that $p(x) \leq 0$ on $[m, M]$ and $a + d > 1$ (so that $\sum p(b_i) = n(a + d - 1) > 0$, contradicting $p \leq 0$).

The condition $p \leq 0$ on $[m, M]$ with $p$ a cubic and leading coefficient 1 means $p$ has roots at $m$ and $M$ (and a third root $c \leq m$), OR $p$ has a root at $m$ or $M$ but not both, etc.

Actually, $p$ doesn't need to have roots at $m$ and $M$. It just needs to be $\leq 0$ on $[m, M]$. The optimal $p$ (maximizing $a + d$) subject to $p \leq 0$ on $[m, M]$ is the one that touches 0 at the endpoints, i.e., $p(m) = p(M) = 0$.

Wait, but maybe the optimal $p$ touches 0 at one endpoint and has a double root at the other? Or touches at an interior point?

For a cubic with positive leading coefficient, to be $\leq 0$ on $[m, M]$, it must be that $p(m) \leq 0$, $p(M) \leq 0$, and $p$ doesn't go positive in between. The extremal case is $p(m) = 0$ and $p(M) = 0$ (touching at both endpoints), with the third root $c \leq m$.

But we showed this doesn't work. So maybe we need a different approach entirely.

Let me reconsider. Perhaps the right approach for part (1) is not the polynomial method but a direct argument.

Actually, let me reconsider the polynomial approach. Maybe I should use a polynomial that is $\geq 0$ on $[m, M]$ and use the moments to show $\sum p(b_i) < 0$.

Consider $q(x) = -(x-m)(x-M) = -x^2 + (m+M)x - mM \geq 0$ on $[m, M]$.

$\sum q(b_i) = -n + (m+M) \cdot 0 - n \cdot mM = -n(1 + mM) \geq 0$, so $mM \leq -1$. (Same as before.)

Now consider a cubic $r(x) = -(x-m)(x-M)(x-c)$ with $c \geq M$, so $r \geq 0$ on $[m, M]$ (since $(x-m) \geq 0$, $(x-M) \leq 0$, $(x-c) \leq 0$, so $(x-m)(x-M)(x-c) \leq 0$, and $r = -$ that $\geq 0$).

$\sum r(b_i) = -[\sum b_i^3 - (m+M+c)\sum b_i^2 + (mM + c(m+M))\sum b_i - cmM \cdot n]$
$= -[-n - (m+M+c)n + 0 - cmMn]$
$= n[1 + m + M + c + cmM]$
$= n[1 + m + M + c(1 + mM)]$

Since $r \geq 0$ on $[m, M]$, $\sum r(b_i) \geq 0$, so $1 + m + M + c(1 + mM) \geq 0$ for all $c \geq M$.

If $1 + mM < 0$: $c(1+mM)$ is decreasing in $c$, so the binding constraint is at $c = M$:
$1 + m + M + M(1 + mM) \geq 0$
$1 + m + 2M + M^2 m \geq 0$
$1 + m + 2M + m M^2 \geq 0$
$1 + m(1 + M^2) + 2M \geq 0$

With $M = m + R$:
$1 + m(1 + (m+R)^2) + 2(m+R) \geq 0$
$1 + m(1 + m^2 + 2mR + R^2) + 2m + 2R \geq 0$
$1 + m + m^3 + 2m^2R + mR^2 + 2m + 2R \geq 0$
$m^3 + 2Rm^2 + (R^2 + 3)m + (1 + 2R) \geq 0$

Let me call this $g(m) = m^3 + 2Rm^2 + (R^2+3)m + (1+2R) \geq 0$.

This must hold for the actual $m$ of the configuration. If $R < \sqrt{5}$, we want to show this fails for some $m$, giving a contradiction.

But again, $m$ is determined by the configuration, not free. We need: for $R < \sqrt{5}$, $g(m) < 0$ for all valid $m$ (in the range where $mM \leq -1$).

Let me evaluate $g$ at the endpoints $m_0, m_1$ (where $mM = -1$):

At $m_0$: $m_0^2 = -Rm_0 - 1$, $m_0^3 = (R^2-1)m_0 + R$.

$g(m_0) = (R^2-1)m_0 + R + 2R(-Rm_0 - 1) + (R^2+3)m_0 + 1 + 2R$
$= (R^2-1)m_0 + R - 2R^2 m_0 - 2R + (R^2+3)m_0 + 1 + 2R$
$= (R^2 - 1 - 2R^2 + R^2 + 3)m_0 + R - 2R + 1 + 2R$
$= 2m_0 + R + 1$
$= 2 \cdot \frac{-R + \sqrt{R^2-4}}{2} + R + 1$
$= \sqrt{R^2-4} + 1 > 0$

Same as before. And $g(m_1) = 1 - \sqrt{R^2-4}$, which is $> 0$ for $R < \sqrt{5}$.

So again, $g > 0$ at both endpoints. And $g$ is a cubic with positive leading coefficient, so it's increasing for large $m$. The question is whether $g < 0$ somewhere in the interior.

$g'(m) = 3m^2 + 4Rm + (R^2+3)$. Discriminant: $16R^2 - 12(R^2+3) = 4R^2 - 36 = 4(R^2 - 9)$. For $R < 3$ (which includes $R < \sqrt{5}$), the discriminant is negative, so $g' > 0$ always, meaning $g$ is strictly increasing.

If $g$ is strictly increasing and $g(m_1) > 0$, then $g > 0$ on $[m_1, \infty)$, including the entire valid interval. So $g(m) > 0$ for all valid $m$, and the approach doesn't give a contradiction!

This means the polynomial approach with a single cubic doesn't work for this problem. I need a different approach.

Let me reconsider. Maybe the approach for part (1) uses a different technique.

Actually, let me think about this problem from scratch. The moments are:
- $E[b] = 0$, $E[b^2] = 1$, $E[b^3] = -1$ (where $E$ denotes $\frac{1}{n}\sum$).

We want to minimize $R = \max b_i - \min b_i$.

This is an optimization problem. The dual approach would use the fact that for any polynomial $p$ of degree $\leq 3$ with $p(x) \leq 0$ on $[m, M]$:

$\sum p(b_i) \leq 0$

$\sum p(b_i) = p_3 \sum b_i^3 + p_2 \sum b_i^2 + p_1 \sum b_i + p_0 \cdot n = n(p_3 \cdot (-1) + p_2 \cdot 1 + p_1 \cdot 0 + p_0) = n(-p_3 + p_2 + p_0)$

So $-p_3 + p_2 + p_0 \leq 0$, i.e., $p_0 + p_2 \leq p_3$.

We want to find the polynomial $p$ of degree $\leq 3$ with $p \leq 0$ on $[m, M]$ that maximizes $-p_3 + p_2 + p_0$ (or equivalently, minimizes $p_3 - p_2 - p_0$). If the maximum is 0, then $R = \sqrt{5}$ is the boundary.

But we also need to optimize over $[m, M]$, i.e., over $m$ and $R = M - m$.

Actually, I think the right framework is:

For a given $R$, the minimum of $p_3 - p_2 - p_0$ over all cubics $p \leq 0$ on $[m, M]$ (with $M - m = R$, optimized over $m$) gives a bound. If this minimum is $> 0$ for $R < \sqrt{5}$, then $R \geq \sqrt{5}$.

But this is a semi-infinite optimization problem. Let me think about it differently.

Actually, I realize the issue with my previous approach: I was fixing the polynomial to be $(x-m)(x-M)(x-c)$, but the optimal polynomial might not factor through $m$ and $M$.

The optimal polynomial $p \leq 0$ on $[m, M]$ that maximizes $-p_3 + p_2 + p_0$ is found by the Chebyshev-like theory. For a cubic, the optimal $p$ touches 0 at 3 points in $[m, M]$ (or at 2 points with a double root).

Let me think about this. We want to maximize $-p_3 + p_2 + p_0$ subject to $p(x) \leq 0$ on $[m, M]$, $\deg p \leq 3$.

Equivalently, minimize $p_3 - p_2 - p_0$ subject to $p \leq 0$ on $[m, M]$.

By scaling, we can normalize. Let's set $p_3 = 1$ (since we want to minimize $p_3 - p_2 - p_0$ and making $p_3$ small helps, but $p_3$ can be negative... hmm).

Actually, the sign of $p_3$ matters. If $p_3 > 0$, then $p(x) \to +\infty$ as $x \to +\infty$, so $p$ can't be $\leq 0$ everywhere, but it can be $\leq 0$ on $[m, M]$.

If $p_3 < 0$, then $p(x) \to -\infty$ as $x \to +\infty$ and $+\infty$ as $x \to -\infty$, so $p$ can be $\leq 0$ on $[m, M]$ more easily.

We want to minimize $p_3 - p_2 - p_0$. If $p_3$ is very negative, $p_3 - p_2 - p_0$ is very negative, which is good (we want it $\leq 0$). But we need $p \leq 0$ on $[m, M]$.

Actually, I think the constraint is $-p_3 + p_2 + p_0 \leq 0$, and we want to show this holds, i.e., $p_3 \geq p_2 + p_0$. The question is whether this is possible for $R < \sqrt{5}$.

Hmm, I think I need to approach this differently. Let me think about the problem using the theory of moments and Chebyshev systems.

Actually, let me just try a direct computational approach. Let me use the substitution $b_i = 1 + c \cdot u_i$ where $u_i \in [-1, 1]$ (scaling to a standard interval) and see what the moment conditions imply.

Hmm, this is getting complicated. Let me try a different approach to the problem.

**Direct approach**: Let's think about what configurations achieve $R$ close to $\sqrt{5}$.

From the 2-point analysis, the optimal continuous distribution has:
- Fraction $\beta = \frac{5-\sqrt{5}}{10}$ at $m = 1 - \sqrt{\frac{1-\beta}{\beta}} = 1 - \sqrt{\frac{5+\sqrt{5}}{5-\sqrt{5}}} \cdot \frac{1}{\sqrt{10}}$...

Actually, let me compute the exact values. $\beta = \frac{5-\sqrt{5}}{10}$, $1-\beta = \frac{5+\sqrt{5}}{10}$.

$\frac{1-\beta}{\beta} = \frac{5+\sqrt{5}}{5-\sqrt{5}} = \frac{(5+\sqrt{5})^2}{25-5} = \frac{25+10\sqrt{5}+5}{20} = \frac{30+10\sqrt{5}}{20} = \frac{3+\sqrt{5}}{2}$.

$m = 1 - \sqrt{\frac{3+\sqrt{5}}{2}}$. Note that $\frac{3+\sqrt{5}}{2} = \left(\frac{1+\sqrt{5}}{2}\right)^2 = \phi^2$ where $\phi$ is the golden ratio. So $m = 1 - \phi = 1 - \frac{1+\sqrt{5}}{2} = \frac{1-\sqrt{5}}{2}$.

Similarly, $\frac{\beta}{1-\beta} = \frac{5-\sqrt{5}}{5+\sqrt{5}} = \frac{(5-\sqrt{5})^2}{20} = \frac{30-10\sqrt{5}}{20} = \frac{3-\sqrt{5}}{2} = \left(\frac{\sqrt{5}-1}{2}\right)^2 = \psi^2$ where $\psi = \frac{\sqrt{5}-1}{2} = 1/\phi$.

$M = 1 + \psi = 1 + \frac{\sqrt{5}-1}{2} = \frac{1+\sqrt{5}}{2} = \phi$.

So $m = \frac{1-\sqrt{5}}{2}$ and $M = \frac{1+\sqrt{5}}{2}$, and $R = M - m = \sqrt{5}$. 

Also, $m = 1 - \phi$ and $M = \phi$, so $m + M = 1$ and $mM = \phi(1-\phi) = \phi - \phi^2 = \phi - (\phi + 1) = -1$. (Using $\phi^2 = \phi + 1$.)

So the extremal 2-point distribution has $mM = -1$, $m + M = 1$, $R = \sqrt{5}$.

Now, for the finite case, we need $k = \beta n$ points at $m$ and $n - k$ at $M$. Since $\beta$ is irrational, $k$ can't be exactly $\beta n$.

Let me think about the finite case more carefully. We need to find the minimum of $R$ over all configurations $(b_1, \ldots, b_n)$ satisfying the moment conditions.

**Key insight for part (2)**: The correction is $n^{-3/2}$, which suggests a connection to the discrete nature of the problem and the rounding of $\beta n$.

Let me think about the 3-point configuration. Suppose we have $k$ points at $m$, $\ell$ points at $c$, and $n - k - \ell$ points at $M$, with $\ell$ small (like $O(1)$ or $O(\sqrt{n})$).

The moment conditions are:
- $km + \ell c + (n-k-\ell)M = n$
- $km^2 + \ell c^2 + (n-k-\ell)M^2 = 2n$
- $km^3 + \ell c^3 + (n-k-\ell)M^3 = 3n$

We want to minimize $M - m$.

In the limit, $\ell/n \to 0$, and we recover the 2-point solution. The correction comes from the $O(\ell)$ perturbation.

Let me think about this more carefully. Let me parametrize: let $k = \beta n + \delta$ where $\delta$ is an integer (the rounding error), and $\ell$ is a small number.

Actually, let me think about it differently. Let me consider the general case where the $b_i$ take values in $\{m, M\}$ plus possibly some other values, and use the moment conditions to derive the bound.

Let me use a different approach. Consider the polynomial:

$$p(x) = (x - m)(x - M) \cdot q(x)$$

where $q(x)$ is a linear function chosen to make $\sum p(b_i) = 0$ (or have a specific sign).

Actually, let me try the approach from a different angle. Let me consider the "variance" of the cubic.

We have $\sum b_i = 0$, $\sum b_i^2 = n$, $\sum b_i^3 = -n$.

Consider $\sum (b_i - m)(b_i - M) = \sum b_i^2 - (m+M)\sum b_i + n \cdot mM = n + n \cdot mM = n(1 + mM)$.

Since $(b_i - m)(b_i - M) \leq 0$ (because $b_i \in [m, M]$), we get $1 + mM \leq 0$.

Now consider $\sum (b_i - m)(b_i - M)(b_i - c)$ for some $c$. On $[m, M]$, $(b_i - m)(b_i - M) \leq 0$, so $(b_i - m)(b_i - M)(b_i - c) \leq 0$ if $b_i \geq c$ (i.e., $c \leq m$) and $\geq 0$ if $c \geq M$.

For $c \leq m$: $\sum (b_i - m)(b_i - M)(b_i - c) \leq 0$.

$\sum (b_i - m)(b_i - M)(b_i - c) = \sum [b_i^3 - (m+M+c)b_i^2 + (mM + c(m+M))b_i - cmM]$
$= -n - (m+M+c)n + 0 - cmMn$
$= -n(1 + m + M + c + cmM)$
$= -n(1 + m + M + c(1 + mM))$

So $-n(1 + m + M + c(1 + mM)) \leq 0$, giving $1 + m + M + c(1 + mM) \geq 0$ for all $c \leq m$.

Similarly, for $c \geq M$: $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$, giving $1 + m + M + c(1 + mM) \leq 0$ for all $c \geq M$.

From the first ($c \leq m$): if $1 + mM < 0$, the binding constraint is $c = m$: $1 + 2m + M + m^2 M \geq 0$, i.e., $1 + 2m + M(1 + m^2) \geq 0$.

From the second ($c \geq M$): if $1 + mM < 0$, the binding constraint is $c = M$: $1 + m + 2M + M^2 m \leq 0$, i.e., $1 + m(1 + M^2) + 2M \leq 0$.

So we have two conditions:
(A) $1 + 2m + M(1 + m^2) \geq 0$
(B) $1 + m(1 + M^2) + 2M \leq 0$

With $M = m + R$:

(A) $1 + 2m + (m+R)(1+m^2) \geq 0 \Leftrightarrow m^3 + Rm^2 + (R+3)m + (1+R) \geq 0$ (this is $g(m) \geq 0$, which we called $g$ before)

(B) $1 + m(1 + (m+R)^2) + 2(m+R) \leq 0 \Leftrightarrow m^3 + 2Rm^2 + (R^2+3)m + (1+2R) \leq 0$ (this is $-g(m) \leq 0$... wait, no.)

Hmm wait, (B) is $g(m) \leq 0$ where $g(m) = m^3 + 2Rm^2 + (R^2+3)m + (1+2R)$.

But (A) is $f(m) \geq 0$ where $f(m) = m^3 + Rm^2 + (R+3)m + (1+R)$.

Wait, I think I made an error before. Let me recompute.

(A): $1 + 2m + (m+R)(1+m^2) \geq 0$
$= 1 + 2m + m + m^3 + R + Rm^2$
$= m^3 + Rm^2 + 3m + 1 + R$
$= m^3 + Rm^2 + (R+3) \cdot \frac{3m}{R+3} + ... $

OK so (A) is $f(m) := m^3 + Rm^2 + 3m + (1+R) \geq 0$.

Hmm wait, $3m$ not $(R+3)m$. Let me recheck:
$1 + 2m + m + m^3 + R + Rm^2 = 1 + 3m + m^3 + R + Rm^2 = m^3 + Rm^2 + 3m + (1+R)$.

So $f(m) = m^3 + Rm^2 + 3m + (1 + R) \geq 0$.

(B): $1 + m(1 + (m+R)^2) + 2(m+R) \leq 0$
$= 1 + m + m(m+R)^2 + 2m + 2R$
$= 1 + 3m + 2R + m(m^2 + 2mR + R^2)$
$= 1 + 3m + 2R + m^3 + 2m^2R + mR^2$
$= m^3 + 2Rm^2 + (R^2 + 3)m + (1 + 2R) \leq 0$.

So $g(m) := m^3 + 2Rm^2 + (R^2+3)m + (1+2R) \leq 0$.

Now, note that $g(m) = f(m) + Rm^2 + R^2 m + R = f(m) + R(m^2 + Rm + 1) = f(m) + R \cdot (mM + 1)$ (since $m^2 + Rm + 1 = m^2 + (M-m)m + 1 = mM + 1$).

Since $mM + 1 \leq 0$, we have $g(m) \leq f(m)$.

So (B) $g(m) \leq 0$ is a stronger condition than (A) $f(m) \geq 0$... wait, no. (A) says $f(m) \geq 0$ and (B) says $g(m) \leq 0$. Since $g \leq f$, (B) implies $f \geq g$... hmm, this doesn't directly relate them.

Actually, $g(m) = f(m) + R(mM+1)$. Since $mM + 1 \leq 0$, $g(m) \leq f(m)$. So if $g(m) \leq 0$ and $f(m) \geq 0$, we need $g(m) \leq 0 \leq f(m)$, which is consistent since $g \leq f$.

Now, at the boundary $mM = -1$ (i.e., $m^2 + Rm + 1 = 0$): $g(m) = f(m)$. And we computed $f(m_0) = 1 + \sqrt{R^2-4}$ and $f(m_1) = 1 - \sqrt{R^2-4}$.

For $R < \sqrt{5}$: $f(m_0) > 0$ and $f(m_1) > 0$. So (A) is satisfied at both endpoints. But (B) requires $g \leq 0$, and at the endpoints $g = f > 0$, so (B) is violated!

This means: at the boundary $mM = -1$, condition (B) is violated for $R < \sqrt{5}$. This gives the contradiction!

Wait, but at $mM = -1$, the configuration is 2-point (all $b_i \in \{m, M\}$), and we already know the 2-point configuration requires $R = \sqrt{5}$. So the contradiction from (B) at $mM = -1$ is just restating this.

For the interior ($mM < -1$), we need both (A) and (B) to hold. (B) is $g(m) \leq 0$. We showed $g$ is strictly increasing (for $R < 3$) and $g(m_1) = 1 - \sqrt{R^2-4} > 0$ for $R < \sqrt{5}$. So $g(m) > 0$ for all $m \geq m_1$, including the entire valid interval. So (B) is violated everywhere in the valid interval for $R < \sqrt{5}$!

Wait, that would mean $R \geq \sqrt{5}$ for all configurations, which is part (1). Let me double-check.

$g(m) = m^3 + 2Rm^2 + (R^2+3)m + (1+2R)$.

$g'(m) = 3m^2 + 4Rm + (R^2+3)$.

Discriminant of $g'$: $16R^2 - 12(R^2+3) = 4R^2 - 36$.

For $R < 3$: discriminant $< 0$, so $g' > 0$ (since leading coefficient of $g'$ is positive), so $g$ is strictly increasing.

$g(m_1) = 1 - \sqrt{R^2 - 4}$ (computed at the boundary $mM = -1$, $m = m_1$).

For $2 \leq R < \sqrt{5}$: $0 \leq \sqrt{R^2-4} < 1$, so $g(m_1) > 0$.

Since $g$ is increasing and $g(m_1) > 0$, $g(m) > 0$ for all $m > m_1$. The valid interval is $[m_1, m_0]$ with $m_1 < m_0$, so $g(m) > 0$ for all $m \in [m_1, m_0]$.

But (B) requires $g(m) \leq 0$. So (B) is violated for all $m$ in the valid interval when $R < \sqrt{5}$.

This means: for $R < \sqrt{5}$, condition (B) is violated, which means there exists $c \geq M$ such that $\sum (b_i - m)(b_i - M)(b_i - c) < 0$. But $(b_i - m)(b_i - M)(b_i - c) \geq 0$ for $c \geq M$ and $b_i \in [m, M]$. So $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$. Contradiction!

Wait, I need to be more careful. (B) says: for all $c \geq M$, $1 + m + M + c(1+mM) \leq 0$. If this is violated, it means there exists $c \geq M$ with $1 + m + M + c(1+mM) > 0$, i.e., $\sum (b_i - m)(b_i - M)(b_i - c) = -n(1 + m + M + c(1+mM)) < 0$.

But for $c \geq M$ and $b_i \in [m, M]$: $(b_i - m) \geq 0$, $(b_i - M) \leq 0$, $(b_i - c) \leq 0$, so the product is $\geq 0$. So $\sum \geq 0$, contradiction.

So the contradiction works! For $R < \sqrt{5}$, (B) is violated, giving a contradiction. This proves $R \geq \sqrt{5}$.

Great, so part (1) is proved using condition (B). The key is that $g(m) > 0$ for all valid $m$ when $R < \sqrt{5}$, which violates the necessary condition (B).

Now for part (2), we need to show $R \geq \sqrt{5} + C_2 n^{-3/2}$.

The approach is to make the argument quantitative. In part (1), we showed $g(m) > 0$ for $R < \sqrt{5}$. For part (2), we need to show that $g(m)$ is not just $> 0$ but bounded away from 0 by some amount related to $n^{-3/2}$, when $R < \sqrt{5} + C_2 n^{-3/2}$.

But wait, the argument in part (1) is exact: $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$ for $c \geq M$, and the moment conditions give $\sum = -n(1 + m + M + c(1+mM))$. The contradiction is exact, not approximate.

For part (2), we need a more refined argument. The issue is that in part (1), we used the exact moment conditions, and the contradiction is exact. For part (2), we need to show that the contradiction has some "slack" that gives the $n^{-3/2}$ correction.

Hmm, but the argument is: $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$ (since each term is $\geq 0$), and $\sum = -n(\ldots)$. So $-n(\ldots) \geq 0$, i.e., $(\ldots) \leq 0$. This is an exact inequality, not approximate.

The key for part (2) is that we need a STRICT inequality. The sum $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$, but can it be 0? It's 0 iff each term is 0, i.e., each $b_i \in \{m, M, c\}$. If $c > M$, then $b_i = c$ is impossible (since $b_i \leq M < c$), so each $b_i \in \{m, M\}$, i.e., the configuration is 2-point.

So: if the configuration is NOT 2-point, then $\sum (b_i - m)(b_i - M)(b_i - c) > 0$ for $c > M$, giving a strict inequality $1 + m + M + c(1+mM) < 0$.

But if the configuration IS 2-point, we need a separate argument.

Let me formalize this. For $c > M$:

$\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$, with equality iff all $b_i \in \{m, M\}$ (since $c > M$ means $b_i - c < 0$ for all $i$, and $(b_i - m)(b_i - M) = 0$ iff $b_i \in \{m, M\}$).

Case 1: Configuration is 2-point ($b_i \in \{m, M\}$ for all $i$). Then $k$ points at $m$ and $n-k$ at $M$, and the moment conditions give $R = \frac{n}{\sqrt{k(n-k)}}$ and the third moment condition gives $\beta = k/n = \frac{5-\sqrt{5}}{10}$ (irrational). Since $k$ must be an integer, $\beta \neq \frac{5-\sqrt{5}}{10}$, so the third moment is not exactly $-n$. But we need the third moment to be exactly $-n$. So a 2-point configuration can't satisfy all three moment conditions (for finite $n$)!

Wait, that's a key point. A 2-point configuration has 2 free parameters ($m, M$) and 1 discrete parameter ($k$), with 3 moment conditions. The first two conditions determine $m, M$ given $k$, and the third condition determines $k$ (or rather, gives an equation for $\beta = k/n$). Since the solution $\beta^*$ is irrational, no integer $k$ satisfies it. So a 2-point configuration CANNOT satisfy all three moment conditions for finite $n$.

This means: for finite $n$, every valid configuration has at least 3 distinct values, so $\sum (b_i - m)(b_i - M)(b_i - c) > 0$ for $c > M$.

This gives a strict inequality: $1 + m + M + c(1 + mM) < 0$ for all $c > M$.

In particular, at $c = M$: $1 + m + 2M + M^2 m \leq 0$ (with equality iff 2-point, which is impossible). So $g(m) < 0$ strictly.

But how much less than 0? We need to quantify the strict inequality.

$\sum (b_i - m)(b_i - M)(b_i - c) > 0$ for $c > M$.

The sum is $-n(1 + m + M + c(1+mM))$. At $c = M$:
$\sum (b_i - m)(b_i - M)^2 = -n \cdot g(m)/n = -g(m)$... wait, let me recompute.

$\sum (b_i - m)(b_i - M)(b_i - M) = \sum (b_i - m)(b_i - M)^2$.

$= \sum [b_i^3 - (m+2M)b_i^2 + (2mM + M^2)b_i - mM^2]$
$= -n - (m+2M)n + 0 - mM^2 n$
$= -n(1 + m + 2M + mM^2)$
$= -n \cdot g(m)/n$... 

Hmm, $g(m) = m^3 + 2Rm^2 + (R^2+3)m + (1+2R)$. With $M = m + R$:
$1 + m + 2M + mM^2 = 1 + m + 2(m+R) + m(m+R)^2 = 1 + 3m + 2R + m^3 + 2m^2R + mR^2 = g(m)$.

So $\sum (b_i - m)(b_i - M)^2 = -n \cdot g(m)$.

Since each term $(b_i - m)(b_i - M)^2 \geq 0$ (as $b_i \geq m$ and $(b_i - M)^2 \geq 0$), and the sum is $> 0$ (since not all $b_i \in \{m, M\}$), we get $g(m) < 0$.

Now, $\sum (b_i - m)(b_i - M)^2 > 0$. How large is this sum?

Each term is $(b_i - m)(b_i - M)^2$. For $b_i = m$ or $b_i = M$, the term is 0. For $b_i$ strictly between $m$ and $M$, the term is positive. For $b_i$ outside $[m, M]$... but $b_i \in [m

</details>

---

## [8] Assistant (node 27)

<details><summary>Thinking (59263 chars)</summary>

Let me carefully analyze this problem.

We have real numbers $a_1, a_2, \ldots, a_n$ with:
- $\sum a_i = n$
- $\sum a_i^2 = 2n$
- $\sum a_i^3 = 3n$

Part (1): The maximum of $\max - \min$ is $\sqrt{5}$, achieved in the limit as $n \to \infty$.

Part (2): Prove there exists $C_2 > 0$ such that $\max - \min \geq \sqrt{5} + C_2 \cdot n^{-3/2}$.

So we need to show that the gap $\max - \min$ is not just $\geq \sqrt{5}$, but actually $\geq \sqrt{5} + C_2 n^{-3/2}$ for some positive constant $C_2$.

Let me think about this carefully.

First, let me understand the structure. Let $M = \max a_i$ and $m = \min a_i$. We want to show $M - m \geq \sqrt{5} + C_2 n^{-3/2}$.

Let me think about what configuration achieves the minimum of $M - m$.

The moments are:
- $\bar{a} = \frac{1}{n}\sum a_i = 1$
- $\frac{1}{n}\sum a_i^2 = 2$, so variance $= 2 - 1 = 1$
- $\frac{1}{n}\sum a_i^3 = 3$, so third central moment: $\frac{1}{n}\sum (a_i - 1)^3 = \frac{1}{n}\sum a_i^3 - 3\frac{1}{n}\sum a_i^2 + 3\frac{1}{n}\sum a_i - 1 = 3 - 6 + 3 - 1 = -1$.

Wait, let me recompute. If $b_i = a_i - 1$, then:
- $\sum b_i = 0$
- $\sum b_i^2 = \sum a_i^2 - 2\sum a_i + n = 2n - 2n + n = n$
- $\sum b_i^3 = \sum a_i^3 - 3\sum a_i^2 + 3\sum a_i - n = 3n - 6n + 3n - n = -n$

So the $b_i$ have mean 0, second moment 1, third moment $-1$ (all per-element, i.e., $\frac{1}{n}\sum b_i^2 = 1$, $\frac{1}{n}\sum b_i^3 = -1$).

The skewness is $\frac{-1}{1^{3/2}} = -1$.

Now, $M - m = \max b_i - \min b_i$.

For the first part, the answer is $\sqrt{5}$. Let me think about what achieves this.

Consider a distribution that's a mixture: most values are at some point, and a few are at the extremes. In the limit $n \to \infty$, we can think of this as a probability distribution.

We want to minimize $\max - \min$ subject to:
- $E[X] = 0$ (where $X = b$)
- $E[X^2] = 1$
- $E[X^3] = -1$

The extremal distribution that minimizes the range... Let me think. The support should be on at most 3 points (by the moment problem theory, with 3 moment constraints, the extremal distribution has at most 3+1 = 4 support points, but actually for minimizing the range, it's likely 3 points: the two endpoints and possibly one interior point).

Actually, let me think about this differently. We want to minimize $M - m$ where $M = \max b_i$, $m = \min b_i$.

Let's say the support is $\{m, c, M\}$ with probabilities $p, q, r$ where $p + q + r = 1$.

Constraints:
- $pm + qc + rM = 0$
- $pm^2 + qc^2 + rM^2 = 1$
- $pm^3 + qc^3 + rM^3 = -1$

We want to minimize $M - m$.

Actually, for the continuous (limit) case, the minimum range is $\sqrt{5}$. Let me verify: if we use a 2-point distribution at $m$ and $M$ with probabilities $p$ and $r = 1-p$:
- $pm + (1-p)M = 0 \Rightarrow p = \frac{M}{M-m}$
- $pm^2 + (1-p)M^2 = 1$
- $pm^3 + (1-p)M^3 = -1$

From the first two: $p = \frac{M}{M-m}$, and $pm^2 + (1-p)M^2 = \frac{M m^2}{M-m} + \frac{-m M^2}{M-m} = \frac{Mm(m-M)}{M-m} = -Mm = 1$.

So $Mm = -1$, i.e., $m = -1/M$.

From the third: $pm^3 + (1-p)M^3 = \frac{M m^3 - m M^3}{M-m} = \frac{Mm(m^2 - M^2)}{M-m} = \frac{Mm(m-M)(m+M)}{M-m} = -Mm(m+M) = (m+M)$ (since $Mm = -1$).

So the third moment is $m + M = -1$, giving $m + M = -1$.

With $m = -1/M$: $-1/M + M = -1$, so $M^2 + M - 1 = 0$, giving $M = \frac{-1 + \sqrt{5}}{2}$ (taking positive root).

Then $m = -1/M = -\frac{2}{-1+\sqrt{5}} = -\frac{2(\sqrt{5}+1)}{4} = -\frac{\sqrt{5}+1}{2}$.

$M - m = \frac{-1+\sqrt{5}}{2} + \frac{\sqrt{5}+1}{2} = \sqrt{5}$.

So the 2-point distribution gives range $\sqrt{5}$. But can a 3-point distribution do better? Let me check.

With 3 points, we have more freedom. Let me think... Actually, with 3 moment constraints and 3 support points, we have 5 free parameters (3 locations + 2 probabilities) and 3 constraints, so 2 degrees of freedom. We want to minimize $M - m$.

Hmm, but actually the claim is that $\sqrt{5}$ is the minimum for the continuous case, and the finite-$n$ case has a correction of order $n^{-3/2}$.

Let me think about why the correction is $n^{-3/2}$.

In the finite case, we have $n$ points. The extremal configuration in the limit is a 2-point distribution: $p = \frac{M}{M-m}$ fraction at $m$ and $r = \frac{-m}{M-m}$ fraction at $M$.

With $M = \frac{\sqrt{5}-1}{2}$ and $m = -\frac{\sqrt{5}+1}{2}$:
- $p = \frac{M}{M-m} = \frac{(\sqrt{5}-1)/2}{\sqrt{5}} = \frac{\sqrt{5}-1}{2\sqrt{5}}$
- $r = \frac{-m}{M-m} = \frac{(\sqrt{5}+1)/2}{\sqrt{5}} = \frac{\sqrt{5}+1}{2\sqrt{5}}$

So $p = \frac{\sqrt{5}-1}{2\sqrt{5}} \approx \frac{1.236}{4.472} \approx 0.2764$ and $r \approx 0.7236$.

In the finite case, we need $pn$ points at $m$ and $rn$ points at $M$ (approximately). But $pn$ and $rn$ need to be integers, and the moments need to be exactly $n, 2n, 3n$.

Let me think about this more carefully. Let's say $k$ points are at $m$ and $n-k$ points are at $M$ (in the 2-point case). Then:
- $km + (n-k)M = n \Rightarrow km + (n-k)M = n$
- $km^2 + (n-k)M^2 = 2n$
- $km^3 + (n-k)M^3 = 3n$

From the first: $k(m-M) + nM = n$, so $k = \frac{n(1-M)}{M-m}$.
From the second: $k(m^2 - M^2) + nM^2 = 2n$, so $k(m-M)(m+M) = n(2 - M^2)$, so $\frac{n(1-M)}{M-m} \cdot (m-M)(m+M) = n(2-M^2)$, giving $-(1-M)(m+M) = 2 - M^2$.

So $-(m+M) + M(m+M) = 2 - M^2$, i.e., $-m - M + Mm + M^2 = 2 - M^2$, i.e., $-m - M + Mm + 2M^2 = 2$.

From the third: $k(m^3 - M^3) + nM^3 = 3n$, so $k(m-M)(m^2+mM+M^2) = n(3 - M^3)$, so $\frac{n(1-M)}{M-m}(m-M)(m^2+mM+M^2) = n(3-M^3)$, giving $-(1-M)(m^2+mM+M^2) = 3 - M^3$.

$-(m^2+mM+M^2) + M(m^2+mM+M^2) = 3 - M^3$
$-m^2 - mM - M^2 + Mm^2 + M^2m + M^3 = 3 - M^3$
$-m^2 - mM - M^2 + Mm^2 + M^2m + 2M^3 = 3$

This is getting complicated. Let me use a different approach.

Actually, for the 2-point distribution with $k$ points at $m$ and $n-k$ at $M$:

The per-element moments (dividing by $n$) are:
- $\frac{k}{n} m + (1-\frac{k}{n}) M = 1$
- $\frac{k}{n} m^2 + (1-\frac{k}{n}) M^2 = 2$
- $\frac{k}{n} m^3 + (1-\frac{k}{n}) M^3 = 3$

Let $\alpha = k/n$. Then:
- $\alpha m + (1-\alpha) M = 1$
- $\alpha m^2 + (1-\alpha) M^2 = 2$
- $\alpha m^3 + (1-\alpha) M^3 = 3$

From first two: $\alpha(m^2 - M^2) + M^2 = 2$, and $\alpha(m - M) + M = 1$, so $\alpha = \frac{1-M}{M-m}$.

$\frac{1-M}{M-m}(m^2 - M^2) + M^2 = 2$
$\frac{1-M}{M-m}(m-M)(m+M) + M^2 = 2$
$-(1-M)(m+M) + M^2 = 2$
$-m - M + Mm + M^2 + M^2 = 2$
$-m - M + Mm + 2M^2 = 2$ ... (i)

From first and third: $\alpha(m^3 - M^3) + M^3 = 3$:
$\frac{1-M}{M-m}(m-M)(m^2+mM+M^2) + M^3 = 3$
$-(1-M)(m^2+mM+M^2) + M^3 = 3$
$-m^2 - mM - M^2 + Mm^2 + mM^2 + M^3 + M^3 = 3$
$-m^2 - mM - M^2 + Mm^2 + mM^2 + 2M^3 = 3$ ... (ii)

From (i): $m(-1 + M) = 2 + M - 2M^2$, so $m = \frac{2 + M - 2M^2}{M - 1} = \frac{-(2 + M - 2M^2)}{1 - M} = \frac{2M^2 - M - 2}{1 - M}$.

Let me factor: $2M^2 - M - 2 = (2M + 1)(M - 2) + 2M - 2 + 2 = $... let me just compute. $2M^2 - M - 2$. Discriminant: $1 + 16 = 17$. Roots: $\frac{1 \pm \sqrt{17}}{4}$. So $2M^2 - M - 2 = 2(M - \frac{1+\sqrt{17}}{4})(M - \frac{1-\sqrt{17}}{4})$.

Hmm, this is getting messy. Let me try a computational approach.

Actually, let me think about this problem differently. The key insight is:

In the finite case, we can't exactly achieve the 2-point extremal distribution because $k = \alpha n$ must be an integer, and even if it is, the moments might not work out exactly. So we need to perturb.

Let me think about what happens when we use a 3-point distribution. The idea is:

1. Most points are at two values close to $m$ and $M$ (the extremal 2-point values).
2. A few points (like $O(1)$ or $O(\sqrt{n})$ points) are at a third value to adjust the moments.

Actually, let me think about the structure more carefully. The correction is $n^{-3/2}$, which suggests that the perturbation involves $O(\sqrt{n})$ points being moved, or something related to the discrete nature of the problem.

Let me think about it from the perspective of the dual problem. We want to show:

$$\max a_i - \min a_i \geq \sqrt{5} + C_2 n^{-3/2}$$

Equivalently, if $M - m < \sqrt{5} + C_2 n^{-3/2}$, we want to derive a contradiction with the moment conditions.

Let me set up the problem. Let $b_i = a_i - 1$, so $\sum b_i = 0$, $\sum b_i^2 = n$, $\sum b_i^3 = -n$.

Let $M = \max b_i$, $m = \min b_i$, $R = M - m$.

We want to show $R \geq \sqrt{5} + C_2 n^{-3/2}$.

**Approach**: Find a polynomial $P(x)$ of degree 3 such that $P(x) \leq x^3 + \alpha x^2 + \beta x + \gamma$ on $[m, M]$ (or some interval), and use the moment conditions to derive a bound on $R$.

Actually, let me think about this using the method of Lagrange multipliers / duality.

The key idea for part (1) is likely: find a cubic polynomial $p(x) = x^3 + ux^2 + vx + w$ such that $p(x) \leq 0$ for $x \in [m, M]$ when $M - m = \sqrt{5}$, and $p(x) = 0$ at $x = m$ and $x = M$. Then $\sum p(b_i) \leq 0$, but $\sum p(b_i) = \sum b_i^3 + u \sum b_i^2 + v \sum b_i + nw = -n + un + 0 + nw = n(u + w - 1)$. Setting this $\leq 0$ gives $u + w \leq 1$.

Hmm, let me think more carefully.

Actually, let me think about the dual approach for part (1) first, to understand the structure, then extend to part (2).

**Part (1) approach**: We want to show $R \geq \sqrt{5}$.

Suppose $R < \sqrt{5}$. We want to find a contradiction.

Consider the polynomial $q(x) = (x - m)(x - M)(x - c)$ for some $c$. On $[m, M]$, $(x-m)(x-M) \leq 0$, so $q(x) \leq 0$ on $[m, M]$ if $c \geq M$ or $c \leq m$ (i.e., $c$ is outside $[m, M]$), and $q(x) \geq 0$ if $c \in [m, M]$.

Actually, let me think about this differently. We want to use the fact that $\sum b_i^3 = -n$ to bound $R$.

Consider a quadratic $q(x) = (x - m)(x - M) = x^2 - (m+M)x + mM$. This is $\leq 0$ on $[m, M]$.

Now, $\sum q(b_i) = \sum b_i^2 - (m+M)\sum b_i + n \cdot mM = n + n \cdot mM = n(1 + mM)$.

Since $q(b_i) \leq 0$ for all $i$, we get $n(1 + mM) \leq 0$, so $mM \leq -1$.

Now, $R = M - m$, and $mM \leq -1$. By AM-GM or similar, $M - m \geq 2\sqrt{-mM} \geq 2$... but that only gives $R \geq 2$, not $\sqrt{5}$.

We need to use the third moment. Consider a cubic that factors through $m$ and $M$:

$p(x) = (x - m)(x - M)(x - c) = x^3 - (m+M+c)x^2 + (mM + c(m+M))x - cMm$.

On $[m, M]$, $(x-m)(x-M) \leq 0$. So $p(x) \leq 0$ on $[m, M]$ iff $x - c \geq 0$ on $[m, M]$, i.e., $c \leq m$. Or $p(x) \geq 0$ iff $c \geq M$.

Let's choose $c \leq m$ so that $p(x) \leq 0$ on $[m, M]$.

$\sum p(b_i) = \sum b_i^3 - (m+M+c)\sum b_i^2 + (mM + c(m+M))\sum b_i - ncMm$
$= -n - (m+M+c)n + 0 - ncMm$
$= -n(1 + m + M + c + cMm)$
$= -n(1 + m + M + c(1 + mM))$

Since $p(b_i) \leq 0$ for all $i$, $\sum p(b_i) \leq 0$, so $-n(1 + m + M + c(1 + mM)) \leq 0$, giving $1 + m + M + c(1 + mM) \geq 0$.

This holds for all $c \leq m$. As $c \to -\infty$:
- If $1 + mM > 0$: $c(1 + mM) \to -\infty$, so the inequality fails. But we showed $mM \leq -1$, so $1 + mM \leq 0$.
- If $1 + mM = 0$: the condition becomes $1 + m + M \geq 0$.
- If $1 + mM < 0$: $c(1 + mM) \to +\infty$ as $c \to -\infty$, so the condition is satisfied for very negative $c$. The binding constraint is at $c = m$: $1 + m + M + m(1 + mM) \geq 0$, i.e., $1 + m + M + m + m^2M \geq 0$, i.e., $1 + 2m + M + m^2 M \geq 0$.

Hmm, this is getting complicated. Let me try a different approach.

Actually, let me try the approach where we use a polynomial that touches zero at $m$ and $M$ and is non-positive on $[m, M]$.

For part (1), the extremal polynomial is likely $p(x) = (x - m)(x - M) \cdot q(x)$ where $q$ is linear, chosen so that the moment conditions give exactly $R = \sqrt{5}$.

Let me try $p(x) = (x - m)(x - M)(x - c)$ with $c$ chosen appropriately.

We have $\sum p(b_i) \leq 0$ (since $p \leq 0$ on $[m, M]$ and $c \leq m$).

$\sum p(b_i) = -n - (m+M+c)n - ncMm = -n(1 + m + M + c + cMm) = -n(1 + m + M + c(1+Mm))$

For this to be $\leq 0$: $1 + m + M + c(1 + Mm) \geq 0$.

We want to choose $c$ to get the tightest bound. Since $1 + Mm \leq 0$ (from the quadratic argument), and $c \leq m$:

If $1 + Mm < 0$, then $c(1 + Mm)$ is a decreasing function of $c$ (since $1 + Mm < 0$, larger $c$ gives more negative product). Wait no: if $1 + Mm < 0$ and $c$ is negative, then $c(1+Mm) > 0$. And as $c$ increases (towards $m$), $c(1+Mm)$ decreases. So the binding constraint is at $c = m$:

$1 + m + M + m(1 + Mm) \geq 0$
$1 + 2m + M + m^2 M \geq 0$
$1 + 2m + M(1 + m^2) \geq 0$
$M \geq -\frac{1 + 2m}{1 + m^2}$

Also, $R = M - m$, so $M = m + R$:
$m + R \geq -\frac{1 + 2m}{1 + m^2}$
$R \geq -\frac{1 + 2m}{1 + m^2} - m = \frac{-(1+2m) - m(1+m^2)}{1+m^2} = \frac{-1 - 2m - m - m^3}{1+m^2} = \frac{-1 - 3m - m^3}{1 + m^2}$

We want to minimize $R$ over $m$. Take derivative and set to 0:
$\frac{d}{dm}\frac{-1 - 3m - m^3}{1 + m^2} = \frac{(-3 - 3m^2)(1+m^2) - (-1-3m-m^3)(2m)}{(1+m^2)^2}$

Numerator: $(-3 - 3m^2)(1 + m^2) + 2m(1 + 3m + m^3)$
$= -3 - 3m^2 - 3m^2 - 3m^4 + 2m + 6m^2 + 2m^4$
$= -3 - 6m^2 - 3m^4 + 2m + 6m^2 + 2m^4$
$= -3 + 2m - m^4$
$= -(m^4 - 2m + 3)$

Hmm, $m^4 - 2m + 3 = 0$? Let me check: at $m = -1$: $1 + 2 + 3 = 6 \neq 0$. This doesn't have nice roots.

I think I'm overcomplicating this. Let me try a different approach.

Let me try the approach where we don't assume a 2-point distribution but instead use a more general polynomial.

Actually, let me reconsider. The standard approach for these moment problems is:

We want to show $R \geq \sqrt{5}$. Suppose all $b_i \in [m, M]$ with $M - m = R$. We need to find a polynomial $p(x)$ of degree $\leq 3$ such that:
1. $p(x) \leq 0$ for $x \in [m, M]$
2. $\sum p(b_i) > 0$ (using the moment conditions) when $R < \sqrt{5}$.

This gives a contradiction.

The polynomial $p(x) = (x - m)(x - M)(x - c)$ with $c \leq m$ satisfies condition 1. And:
$\sum p(b_i) = -n(1 + m + M + c(1 + Mm))$

For this to be $> 0$: $1 + m + M + c(1 + Mm) < 0$.

We want to find $c \leq m$ such that this holds, given $R < \sqrt{5}$.

Alternatively, let's use the polynomial $p(x) = (x - m)(x - M) \cdot (x - c)$ where we choose $c$ optimally.

Actually, I realize I should think about this more carefully. Let me use a slightly different approach.

Let me shift and scale. Let $b_i \in [m, M]$ with $M - m = R$. Let $t = \frac{M + m}{2}$ (midpoint) and $s = \frac{M - m}{2} = R/2$ (half-range). So $b_i \in [t - s, t + s]$.

Let $u_i = \frac{b_i - t}{s} \in [-1, 1]$. Then:
- $\sum b_i = 0 \Rightarrow \sum (t + su_i) = 0 \Rightarrow nt + s\sum u_i = 0 \Rightarrow \sum u_i = -nt/s$
- $\sum b_i^2 = n \Rightarrow \sum(t + su_i)^2 = n \Rightarrow nt^2 + 2ts\sum u_i + s^2 \sum u_i^2 = n$
- $\sum b_i^3 = -n \Rightarrow \sum(t + su_i)^3 = -n \Rightarrow nt^3 + 3t^2 s \sum u_i + 3ts^2 \sum u_i^2 + s^3 \sum u_i^3 = -n$

This is getting complicated. Let me try a computational approach to understand the problem better.

Let me use Python/SymPy to explore.

Actually, let me think about the problem from a higher level.

The key question is: why is the correction $n^{-3/2}$?

In the extremal 2-point distribution, we need $\alpha n$ points at $m$ and $(1-\alpha)n$ points at $M$, where $\alpha = \frac{\sqrt{5}-1}{2\sqrt{5}}$. Since $\alpha$ is irrational, we can't have exactly $\alpha n$ points. The rounding error is at most 1, which gives a correction of order $1/n$ to the moments. But the correction to the range is $n^{-3/2}$, which is larger than $n^{-1}$ for large $n$... wait, no, $n^{-3/2} < n^{-1}$ for large $n$. So the correction is smaller.

Hmm, actually $n^{-3/2}$ is smaller than $n^{-1}$. So the finite-$n$ correction is quite small. This suggests that the 2-point distribution with rounding is not the binding constraint; rather, there's a more subtle effect.

Let me think about this differently. Maybe the extremal configuration for finite $n$ is not a 2-point distribution but a 3-point distribution, and the third point accounts for the correction.

Let me consider the following: $k$ points at $m$, $\ell$ points at $c$ (interior), and $n - k - \ell$ points at $M$. We want to minimize $M - m$.

In the limit $n \to \infty$, the optimal is the 2-point distribution with $\ell = 0$. For finite $n$, we might need $\ell > 0$ to satisfy the moment conditions exactly.

Let me think about what happens with the 2-point distribution when $k$ is not exactly $\alpha n$.

Let $k = \lfloor \alpha n \rfloor$ (or nearby). Then with $k$ points at $m$ and $n - k$ at $M$:
- $km + (n-k)M = n$
- $km^2 + (n-k)M^2 = 2n$
- $km^3 + (n-k)M^3 = 3n$

Three equations, two unknowns ($m, M$), so the system is overdetermined. We can satisfy two of the three equations, and the third will have a residual.

From the first two equations, we can solve for $m$ and $M$ given $k$:
- $m + M = \frac{2n - km^2 - (n-k)M^2}{...}$... this is circular.

Let me use the first two equations:
$km + (n-k)M = n$ ... (1)
$km^2 + (n-k)M^2 = 2n$ ... (2)

From (1): $M = \frac{n - km}{n - k}$.
Substitute into (2): $km^2 + (n-k)\left(\frac{n-km}{n-k}\right)^2 = 2n$
$km^2 + \frac{(n-km)^2}{n-k} = 2n$
$\frac{km^2(n-k) + (n-km)^2}{n-k} = 2n$
$km^2(n-k) + n^2 - 2nkm + k^2m^2 = 2n(n-k)$
$m^2(k(n-k) + k^2) + n^2 - 2nkm = 2n^2 - 2nk$
$m^2 \cdot kn + n^2 - 2nkm = 2n^2 - 2nk$
$m^2 kn - 2nkm + n^2 - 2n^2 + 2nk = 0$
$kn \cdot m^2 - 2nkm - n^2 + 2nk = 0$
$kn \cdot m^2 - 2nkm + n(2k - n) = 0$
$km^2 - 2km + (2k - n) = 0$ (dividing by $n$)
$km^2 - 2km + 2k - n = 0$
$m = \frac{2k \pm \sqrt{4k^2 - 4k(2k-n)}}{2k} = \frac{2k \pm \sqrt{4k^2 - 8k^2 + 4kn}}{2k} = \frac{2k \pm 2\sqrt{kn - k^2}}{2k} = 1 \pm \frac{\sqrt{k(n-k)}}{k} = 1 \pm \sqrt{\frac{n-k}{k}}$

So $m = 1 - \sqrt{\frac{n-k}{k}}$ and $M = 1 + \sqrt{\frac{k}{n-k}}$ (taking $m < M$).

Then $R = M - m = \sqrt{\frac{k}{n-k}} + \sqrt{\frac{n-k}{k}} = \frac{k + (n-k)}{\sqrt{k(n-k)}} = \frac{n}{\sqrt{k(n-k)}}$.

Now check the third moment:
$km^3 + (n-k)M^3 = ?$

Let $\beta = k/n$, so $m = 1 - \sqrt{\frac{1-\beta}{\beta}}$ and $M = 1 + \sqrt{\frac{\beta}{1-\beta}}$.

$km^3 + (n-k)M^3 = n[\beta m^3 + (1-\beta) M^3]$

Let $u = \sqrt{\frac{1-\beta}{\beta}}$ and $v = \sqrt{\frac{\beta}{1-\beta}}$, so $uv = 1$, $m = 1 - u$, $M = 1 + v$.

$\beta(1-u)^3 + (1-\beta)(1+v)^3$
$= \beta(1 - 3u + 3u^2 - u^3) + (1-\beta)(1 + 3v + 3v^2 + v^3)$
$= 1 + 3[-\beta u + (1-\beta)v] + 3[\beta u^2 + (1-\beta)v^2] + [-\beta u^3 + (1-\beta)v^3]$

Now, $\beta u = \beta\sqrt{\frac{1-\beta}{\beta}} = \sqrt{\beta(1-\beta)}$ and $(1-\beta)v = (1-\beta)\sqrt{\frac{\beta}{1-\beta}} = \sqrt{\beta(1-\beta)}$. So $-\beta u + (1-\beta)v = 0$.

$\beta u^2 = \beta \cdot \frac{1-\beta}{\beta} = 1-\beta$ and $(1-\beta)v^2 = (1-\beta) \cdot \frac{\beta}{1-\beta} = \beta$. So $\beta u^2 + (1-\beta)v^2 = 1$.

$\beta u^3 = \beta \cdot \frac{(1-\beta)^{3/2}}{\beta^{3/2}} = \frac{(1-\beta)^{3/2}}{\beta^{1/2}}$ and $(1-\beta)v^3 = (1-\beta) \cdot \frac{\beta^{3/2}}{(1-\beta)^{3/2}} = \frac{\beta^{3/2}}{(1-\beta)^{1/2}}$.

So $-\beta u^3 + (1-\beta)v^3 = -\frac{(1-\beta)^{3/2}}{\beta^{1/2}} + \frac{\beta^{3/2}}{(1-\beta)^{1/2}} = \frac{-(1-\beta)^2 + \beta^2}{\beta^{1/2}(1-\beta)^{1/2}} = \frac{-(1-2\beta+\beta^2) + \beta^2}{\sqrt{\beta(1-\beta)}} = \frac{-1+2\beta}{\sqrt{\beta(1-\beta)}}$.

So the third moment sum is:
$n\left[1 + 0 + 3 + \frac{-1+2\beta}{\sqrt{\beta(1-\beta)}}\right] = n\left[4 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}\right]$

We need this to equal $3n$:
$4 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}} = 3$
$\frac{2\beta - 1}{\sqrt{\beta(1-\beta)}} = -1$
$2\beta - 1 = -\sqrt{\beta(1-\beta)}$

For this to have a solution, we need $2\beta - 1 < 0$, i.e., $\beta < 1/2$.

Squaring: $(2\beta - 1)^2 = \beta(1-\beta)$
$4\beta^2 - 4\beta + 1 = \beta - \beta^2$
$5\beta^2 - 5\beta + 1 = 0$
$\beta = \frac{5 \pm \sqrt{25 - 20}}{10} = \frac{5 \pm \sqrt{5}}{10}$

Since $\beta < 1/2$: $\beta = \frac{5 - \sqrt{5}}{10}$.

And $1 - \beta = \frac{5 + \sqrt{5}}{10}$.

$R = \frac{n}{\sqrt{k(n-k)}} = \frac{n}{n\sqrt{\beta(1-\beta)}} = \frac{1}{\sqrt{\beta(1-\beta)}}$.

$\beta(1-\beta) = \frac{(5-\sqrt{5})(5+\sqrt{5})}{100} = \frac{25 - 5}{100} = \frac{20}{100} = \frac{1}{5}$.

So $R = \frac{1}{\sqrt{1/5}} = \sqrt{5}$. 

This confirms part (1): the 2-point distribution with $\beta = \frac{5-\sqrt{5}}{10}$ gives $R = \sqrt{5}$.

Now for part (2), the key issue is that $\beta = \frac{5-\sqrt{5}}{10}$ is irrational, so $k = \beta n$ is never an integer. When $k$ is not exactly $\beta n$, the third moment condition is not satisfied, and we need to adjust.

Let me think about this. If we use a 2-point distribution with $k$ points at $m$ and $n-k$ at $M$ (satisfying the first two moment conditions), the third moment is:

$T(k) = n\left[4 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}\right]$ where $\beta = k/n$.

We need $T(k) = 3n$, i.e., $g(\beta) := 4 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}} = 3$, i.e., $\frac{2\beta - 1}{\sqrt{\beta(1-\beta)}} = -1$.

This is only satisfied at $\beta^* = \frac{5-\sqrt{5}}{10}$.

For $\beta \neq \beta^*$, $g(\beta) \neq 3$, so the third moment is not $3n$. The residual is:

$T(k) - 3n = n[g(\beta) - 3] = n \cdot h(\beta)$

where $h(\beta) = 1 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}$.

$h(\beta^*) = 0$. Let's compute $h'(\beta^*)$.

$h(\beta) = 1 + \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}$

Let $f(\beta) = \frac{2\beta - 1}{\sqrt{\beta(1-\beta)}}$.

$f'(\beta) = \frac{2\sqrt{\beta(1-\beta)} - (2\beta-1) \cdot \frac{1-2\beta}{2\sqrt{\beta(1-\beta)}}}{\beta(1-\beta)} = \frac{2\beta(1-\beta) - \frac{(2\beta-1)(1-2\beta)}{2}}{[\beta(1-\beta)]^{3/2}}$

$= \frac{2\beta(1-\beta) + \frac{(2\beta-1)^2}{2}}{[\beta(1-\beta)]^{3/2}} = \frac{4\beta(1-\beta) + (2\beta-1)^2}{2[\beta(1-\beta)]^{3/2}} = \frac{4\beta - 4\beta^2 + 4\beta^2 - 4\beta + 1}{2[\beta(1-\beta)]^{3/2}} = \frac{1}{2[\beta(1-\beta)]^{3/2}}$

So $f'(\beta) = \frac{1}{2[\beta(1-\beta)]^{3/2}}$.

At $\beta^*$: $\beta^*(1-\beta^*) = 1/5$, so $f'(\beta^*) = \frac{1}{2(1/5)^{3/2}} = \frac{1}{2 \cdot 5^{-3/2}} = \frac{5^{3/2}}{2} = \frac{5\sqrt{5}}{2}$.

So $h'(\beta^*) = f'(\beta^*) = \frac{5\sqrt{5}}{2}$.

Now, if $\beta = k/n$ and $k$ is the nearest integer to $\beta^* n$, then $|\beta - \beta^*| \approx \frac{1}{n}$ (the rounding error). More precisely, $|\beta - \beta^*| \leq \frac{1}{2n}$.

So $h(\beta) \approx h'(\beta^*) \cdot (\beta - \beta^*) \approx \frac{5\sqrt{5}}{2} \cdot O(1/n)$.

And $T(k) - 3n = n \cdot h(\beta) \approx \frac{5\sqrt{5}}{2} \cdot O(1) = O(1)$.

So the third moment residual is $O(1)$, not $O(n)$. This means we need to correct the third moment by $O(1)$, which can be done by moving $O(1)$ points to a third value. But this would give a correction to $R$ of order... let me think.

If we move one point from $M$ to some value $c$, the change in the third moment is $c^3 - M^3$, and we need this to be $O(1)$. So $c$ is close to $M$, with $c - M = O(1/M^2) = O(1)$. This doesn't directly change $R$ unless $c > M$ or $c < m$.

Hmm, let me think more carefully. The issue is that with a 2-point distribution, we can satisfy the first two moments exactly but the third moment is off by $O(1)$. To fix the third moment, we need to introduce a third point or adjust the existing points.

Let me consider a 3-point distribution: $k$ points at $m$, $1$ point at $c$, and $n - k - 1$ points at $M$.

The moment conditions become:
- $km + c + (n-k-1)M = n$
- $km^2 + c^2 + (n-k-1)M^2 = 2n$
- $km^3 + c^3 + (n-k-1)M^3 = 3n$

We have 3 unknowns ($m, M, c$) and 3 equations, plus $k$ is a free integer parameter. We want to minimize $M - m$.

Actually, let me think about this differently. Let me consider the general approach.

Let me use the dual/LP approach. We want to show that for any $b_1, \ldots, b_n$ with $\sum b_i = 0$, $\sum b_i^2 = n$, $\sum b_i^3 = -n$, we have $\max b_i - \min b_i \geq \sqrt{5} + C_2 n^{-3/2}$.

The approach is to find a polynomial $p(x)$ of degree 3 such that:
1. $p(x) \leq (x - m_0)(x - M_0)$ for $x \in [m, M]$ where $m_0, M_0$ are the extremal values... 

Actually, let me think about this more carefully using the polynomial method.

**Key idea**: We want to find a cubic polynomial $p(x) = x^3 + ax^2 + bx + c$ such that $p(x) \leq 0$ for all $x \in [m, M]$ (where $M - m = R$), and $\sum p(b_i) = -n + an + cn = n(a + c - 1)$. If $a + c - 1 > 0$, then $\sum p(b_i) > 0$, contradicting $p \leq 0$ on $[m, M]$.

Wait, I need to be more careful. $\sum p(b_i) = \sum b_i^3 + a \sum b_i^2 + b \sum b_i + nc = -n + an + 0 + nc = n(a + c - 1)$.

For the contradiction: if $p(x) \leq 0$ on $[m, M]$ and $a + c > 1$, then $\sum p(b_i) = n(a + c - 1) > 0$ but $\sum p(b_i) \leq 0$, contradiction.

So we need: for any $[m, M]$ with $M - m < \sqrt{5} + C_2 n^{-3/2}$, there exists a cubic $p(x) = x^3 + ax^2 + bx + c$ with $p \leq 0$ on $[m, M]$ and $a + c > 1$.

But actually, the constraint is that $p \leq 0$ on $[m, M]$ and $p$ is a cubic with leading coefficient 1. A cubic with positive leading coefficient goes to $+\infty$ as $x \to +\infty$ and $-\infty$ as $x \to -\infty$. For it to be $\leq 0$ on $[m, M]$, it needs to have roots at or outside $m$ and $M$.

The best we can do is $p(x) = (x - m)(x - M)(x - c)$ with $c \leq m$ (so that on $[m, M]$, $(x-m) \geq 0$, $(x-M) \leq 0$, $(x-c) \geq 0$, so $p \leq 0$).

$p(x) = x^3 - (m + M + c)x^2 + (mM + c(m+M))x - cmM$

So $a = -(m+M+c)$, $b = mM + c(m+M)$, $c_{\text{coeff}} = -cmM$.

$a + c_{\text{coeff}} = -(m+M+c) - cmM = -(m + M + c + cmM) = -(m + M + c(1 + mM))$.

We need $a + c_{\text{coeff}} > 1$, i.e., $-(m + M + c(1 + mM)) > 1$, i.e., $m + M + c(1 + mM) < -1$.

We want to maximize $-(m + M + c(1 + mM))$ over $c \leq m$.

If $1 + mM < 0$ (which we know is the case, since $mM \leq -1$), then $c(1 + mM)$ is maximized when $c$ is minimized (most negative). As $c \to -\infty$, $c(1+mM) \to +\infty$ (since $1 + mM < 0$), so $m + M + c(1+mM) \to -\infty$, and the condition is satisfied.

Wait, but that can't be right—if $c \to -\infty$, the condition is always satisfied, which would mean $R$ can be anything. The issue is that $p(x) = (x-m)(x-M)(x-c)$ with $c \to -\infty$ is not $\leq 0$ on $[m, M]$ in a useful way... wait, it is $\leq 0$ on $[m, M]$ for any $c \leq m$.

But the point is that we need $p \leq 0$ on $[m, M]$ AND $a + c_{\text{coeff}} > 1$. If $1 + mM < 0$, then for $c$ sufficiently negative, $a + c_{\text{coeff}} \to +\infty$, so the condition is satisfied. But this would mean any $R$ works, which is wrong.

I think the issue is that I need $p(x) \leq 0$ on $[m, M]$, but $p$ is a specific cubic (with leading coefficient 1), and the condition $a + c > 1$ depends on $m, M, c$. Let me re-examine.

Actually wait, the condition is $p(x) \leq 0$ for all $x \in [m, M]$. With $p(x) = (x-m)(x-M)(x-c)$ and $c \leq m$:
- For $x \in [m, M]$: $(x-m) \geq 0$, $(x-M) \leq 0$, $(x-c) \geq 0$ (since $c \leq m \leq x$). So $p(x) = (+)(-)(+) \leq 0$. ✓

And $a + c_{\text{coeff}} = -(m + M + c(1 + mM))$.

With $1 + mM \leq 0$ and $c \leq m$:
- If $1 + mM < 0$: as $c \to -\infty$, $c(1+mM) \to +\infty$, so $a + c_{\text{coeff}} \to -\infty$. That's bad.
- Wait, $a + c_{\text{coeff}} = -(m + M + c(1+mM))$. If $c(1+mM) \to +\infty$, then $m + M + c(1+mM) \to +\infty$, so $a + c_{\text{coeff}} \to -\infty$. So the condition $a + c_{\text{coeff}} > 1$ is NOT satisfied.

Let me redo: we need $m + M + c(1 + mM) < -1$.

With $1 + mM < 0$ and $c \leq m$ (both negative, say):
- $c(1+mM) = c \cdot (\text{negative})$. If $c < 0$, then $c(1+mM) > 0$.
- As $c$ increases (towards $m$), $c(1+mM)$ decreases (since $1+mM < 0$).
- So $m + M + c(1+mM)$ is maximized when $c$ is most negative, and minimized when $c = m$.

So the binding constraint is at $c = m$:
$m + M + m(1 + mM) = m + M + m + m^2M = 2m + M + m^2 M = 2m + M(1 + m^2)$

We need $2m + M(1 + m^2) < -1$.

With $M = m + R$:
$2m + (m+R)(1 + m^2) < -1$
$2m + m + m^3 + R + Rm^2 < -1$
$3m + m^3 + R(1 + m^2) < -1$
$R(1 + m^2) < -1 - 3m - m^3$
$R < \frac{-1 - 3m - m^3}{1 + m^2}$ (if $1 + m^2 > 0$, which it always is)

Wait, we need $R$ to satisfy this for the contradiction to work. But we're trying to show $R \geq \sqrt{5}$, so we need: if $R < \sqrt{5}$, then there exist $m, c$ such that the conditions hold.

Hmm, I think I have the logic backwards. Let me reconsider.

We want to show $R \geq \sqrt{5}$. The approach is:

Assume $R < \sqrt{5}$. We want to derive a contradiction.

For any $m$ (and $M = m + R$), if we can find $c \leq m$ such that $m + M + c(1+mM) < -1$, then we have our contradiction.

The best $c$ is $c = m$ (as argued above), giving the condition:
$2m + M(1 + m^2) < -1$

But this needs to hold for the SPECIFIC $m$ and $M$ of the given configuration. We don't get to choose $m$; it's determined by the $b_i$.

Hmm, but actually, we do get to choose the polynomial. The polynomial $p(x) = (x-m)(x-M)(x-c)$ depends on $m$ and $M$, which are the actual min and max of the $b_i$. So $m$ and $M$ are given, and we choose $c$.

So the condition for contradiction is: $2m + M(1 + m^2) < -1$ where $M = m + R$.

This is: $2m + (m+R)(1+m^2) < -1$, i.e., $R < \frac{-1 - 3m - m^3}{1 + m^2}$.

We need this to hold for the given $m$. But $m$ could be anything (subject to the moment constraints). So we need: for all valid $m$, $\sqrt{5} \leq \frac{-1 - 3m - m^3}{1 + m^2}$?

No, that's not right either. The logic is: if $R < \sqrt{5}$, then for the specific $m$ of the configuration, we need $R < \frac{-1 - 3m - m^3}{1 + m^2}$ to get a contradiction. But this might not hold for all $m$.

I think the correct approach is different. Let me reconsider.

Actually, I think the right approach is to optimize over $c$ (not just set $c = m$). The condition is:

$m + M + c(1 + mM) < -1$ for some $c \leq m$.

If $1 + mM < 0$: the LHS is minimized at $c = m$ (as argued), giving $2m + M(1+m^2) < -1$.
If $1 + mM = 0$: the condition is $m + M < -1$, and $mM = -1$.
If $1 + mM > 0$: the LHS is minimized at $c \to -\infty$, giving $-\infty < -1$, always true. But we showed $mM \leq -1$, so $1 + mM \leq 0$.

So the binding case is $1 + mM < 0$ and $c = m$, giving $2m + M(1 + m^2) < -1$.

Now, we also have the constraint from the quadratic: $\sum (b_i - m)(b_i - M) \leq 0$, giving $n(1 + mM) \leq 0$, i.e., $mM \leq -1$.

And $R = M - m$, $M = m + R$, so $m(m+R) \leq -1$, i.e., $m^2 + mR + 1 \leq 0$.

This gives $m \in \left[\frac{-R - \sqrt{R^2 - 4}}{2}, \frac{-R + \sqrt{R^2 - 4}}{2}\right]$ (requires $R \geq 2$).

Now, for the cubic condition: $2m + (m+R)(1+m^2) < -1$, i.e., $f(m) := 3m + m^3 + R(1+m^2) + 1 < 0$.

We need: for all $m$ in the valid range (from the quadratic constraint), $f(m) < 0$.

Actually, we need: there exists $m$ (the actual min of the $b_i$) such that $f(m) \geq 0$ would mean no contradiction. We want to show that for $R < \sqrt{5}$, $f(m) < 0$ for all valid $m$, giving a contradiction.

Wait, I'm confusing myself. Let me restart the logic.

We have a specific configuration $b_1, \ldots, b_n$ with specific $m = \min b_i$ and $M = \max b_i$. We want to show $R = M - m \geq \sqrt{5}$.

Assume $R < \sqrt{5}$. Then:
1. From the quadratic: $mM \leq -1$, so $m$ is in a certain range.
2. From the cubic (with $c = m$): if $2m + M(1+m^2) < -1$, i.e., $f(m) < 0$, then we have a contradiction (since $\sum p(b_i) > 0$ but $p \leq 0$ on $[m,M]$).

So we need: for all $m$ satisfying the quadratic constraint $m(m+R) \leq -1$ (with $R < \sqrt{5}$), we have $f(m) = 3m + m^3 + R(1+m^2) + 1 < 0$.

Hmm wait, but $m$ is not free—it's the actual minimum of the $b_i$. The quadratic constraint gives a necessary condition on $m$, but $m$ could be any value satisfying it. We need the cubic condition to give a contradiction for ALL possible $m$.

Actually, I realize the logic should be: we need to show that for $R < \sqrt{5}$, for EVERY valid $m$ (i.e., every $m$ with $m(m+R) \leq -1$), the cubic condition $f(m) < 0$ holds. This would mean no matter what $m$ is, we get a contradiction.

But actually, it's possible that for some $m$, $f(m) \geq 0$, meaning the cubic approach with $c = m$ doesn't give a contradiction. In that case, we might need a different $c$ or a different polynomial.

Let me just compute. We have $f(m) = m^3 + (R+3)m + Rm^2 + R + 1 = m^3 + Rm^2 + (R+3)m + (R+1)$.

Wait, let me recompute: $f(m) = 3m + m^3 + R(1+m^2) + 1 = m^3 + Rm^2 + 3m + R + 1$.

We want $f(m) < 0$ for all $m$ in the valid range.

The valid range from $m^2 + Rm + 1 \leq 0$ is $m \in \left[\frac{-R - \sqrt{R^2-4}}{2}, \frac{-R + \sqrt{R^2-4}}{2}\right]$ (for $R \geq 2$).

At the endpoints, $m^2 + Rm + 1 = 0$, so $mM = -1$ (equality in the quadratic constraint).

Let me evaluate $f$ at the endpoints. Let $m_0 = \frac{-R + \sqrt{R^2-4}}{2}$ (the upper endpoint, less negative) and $m_1 = \frac{-R - \sqrt{R^2-4}}{2}$ (the lower endpoint, more negative).

At $m_0$: $m_0^2 = -Rm_0 - 1$, so $m_0^3 = -Rm_0^2 - m_0 = -R(-Rm_0 - 1) - m_0 = R^2 m_0 + R - m_0 = (R^2-1)m_0 + R$.

$f(m_0) = (R^2-1)m_0 + R + Rm_0^2 + 3m_0 + R + 1 = (R^2-1)m_0 + R + R(-Rm_0 - 1) + 3m_0 + R + 1$
$= (R^2-1)m_0 + R - R^2 m_0 - R + 3m_0 + R + 1$
$= (R^2 - 1 - R^2 + 3)m_0 + R + 1$
$= 2m_0 + R + 1$
$= 2 \cdot \frac{-R + \sqrt{R^2-4}}{2} + R + 1$
$= -R + \sqrt{R^2-4} + R + 1$
$= \sqrt{R^2-4} + 1$

This is always $> 0$! So $f(m_0) > 0$, meaning the cubic approach with $c = m$ does NOT give a contradiction at $m = m_0$.

Hmm, so the approach with $c = m$ doesn't work at the boundary. Let me try $c < m$.

At $m = m_0$ (where $mM = -1$, i.e., $1 + mM = 0$): the condition becomes $m + M + c \cdot 0 < -1$, i.e., $m + M < -1$, i.e., $2m + R < -1$, i.e., $m < \frac{-1-R}{2}$.

$m_0 = \frac{-R + \sqrt{R^2-4}}{2}$. Is $m_0 < \frac{-1-R}{2}$? This is $\sqrt{R^2-4} < -1$, which is false (since $\sqrt{R^2-4} \geq 0$). So at $m = m_0$, the cubic condition fails for all $c$.

This means the polynomial approach with a single cubic doesn't work at the boundary $mM = -1$. We need a different approach.

Let me reconsider. Maybe we need to use a quartic polynomial, or a different type of argument.

Actually, wait. At $mM = -1$ (equality in the quadratic), the quadratic $(x-m)(x-M) \leq 0$ on $[m,M]$ and $\sum (b_i - m)(b_i - M) = 0$. This means $(b_i - m)(b_i - M) = 0$ for all $i$, i.e., every $b_i$ is either $m$ or $M$. So the configuration is a 2-point distribution!

In that case, the cubic condition is exactly the third moment condition, and we've already shown that the 2-point distribution gives $R = \sqrt{5}$ when the third moment is satisfied. So for $R < \sqrt{5}$, the 2-point distribution can't satisfy all three moments.

But the issue is: for $R < \sqrt{5}$, the quadratic constraint $mM \leq -1$ is satisfied with strict inequality for most $m$, and the cubic gives a contradiction. But at the boundary $mM = -1$, the configuration is forced to be 2-point, and the third moment gives $R = \sqrt{5}$ exactly.

So the argument for part (1) is:
- If $mM < -1$: use the cubic to get a contradiction when $R < \sqrt{5}$.
- If $mM = -1$: the configuration is 2-point, and the third moment forces $R = \sqrt{5}$.

Let me verify the first case. If $mM < -1$ (strict), then $1 + mM < 0$, and we can choose $c < m$ such that $m + M + c(1+mM) < -1$. Specifically, we need $c > \frac{-1 - m - M}{1 + mM}$ (note: $1 + mM < 0$, so dividing flips the inequality). We need $c \leq m$, so we need $\frac{-1 - m - M}{1 + mM} < m$, i.e., $-1 - m - M > m(1 + mM)$ (flipping because $1 + mM < 0$), i.e., $-1 - m - M - m - m^2 M > 0$, i.e., $-1 - 2m - M - m^2 M > 0$, i.e., $1 + 2m + M(1 + m^2) < 0$, i.e., $f(m) < 0$ (where $f$ is as before).

So we need $f(m) < 0$ for all $m$ in the interior of the valid range (where $mM < -1$).

$f(m) = m^3 + Rm^2 + (R+3)m + (R+1)$.

We showed $f(m_0) = \sqrt{R^2 - 4} + 1 > 0$ and by symmetry (or computation), $f(m_1) = -\sqrt{R^2-4} + 1$... let me check.

At $m_1 = \frac{-R - \sqrt{R^2-4}}{2}$: similarly, $m_1^2 = -Rm_1 - 1$, $m_1^3 = (R^2-1)m_1 + R$.

$f(m_1) = 2m_1 + R + 1 = 2 \cdot \frac{-R - \sqrt{R^2-4}}{2} + R + 1 = -R - \sqrt{R^2-4} + R + 1 = 1 - \sqrt{R^2-4}$.

So $f(m_1) = 1 - \sqrt{R^2 - 4}$.

For $R < \sqrt{5}$: $R^2 < 5$, $R^2 - 4 < 1$, $\sqrt{R^2-4} < 1$, so $f(m_1) > 0$.

And $f(m_0) = 1 + \sqrt{R^2-4} > 0$ always.

So $f > 0$ at both endpoints! This means the cubic approach with $c = m$ doesn't give a contradiction at either endpoint.

But wait—at the endpoints, $mM = -1$, so the configuration is 2-point, and we handle that separately. The question is whether $f < 0$ in the interior.

Let's check $f$ at the midpoint $m = -R/2$ (the center of the valid range):

$f(-R/2) = (-R/2)^3 + R(-R/2)^2 + (R+3)(-R/2) + (R+1)$
$= -R^3/8 + R^3/4 - R^2/2 - 3R/2 + R + 1$
$= R^3/8 - R^2/2 - R/2 + 1$
$= \frac{R^3 - 4R^2 - 4R + 8}{8}$

At $R = \sqrt{5}$: $R^3 = 5\sqrt{5}$, $R^2 = 5$.
$\frac{5\sqrt{5} - 20 - 4\sqrt{5} + 8}{8} = \frac{\sqrt{5} - 12}{8} \approx \frac{2.236 - 12}{8} \approx \frac{-9.764}{8} \approx -1.22 < 0$.

So at $R = \sqrt{5}$, $f(-R/2) < 0$. Good.

At $R = 2$: $\frac{8 - 16 - 8 + 8}{8} = \frac{-8}{8} = -1 < 0$.

So $f$ is negative in the interior. The issue is only at the boundary. So the argument is:

For $R < \sqrt{5}$:
- If $mM = -1$ (boundary): 2-point distribution, third moment forces $R \geq \sqrt{5}$, contradiction.
- If $mM < -1$ (interior): $f(m) < 0$ for $m$ in the interior, so the cubic gives a contradiction.

But we need to verify that $f(m) < 0$ for all $m$ in the open interval $(m_1, m_0)$ when $R < \sqrt{5}$.

$f$ is a cubic in $m$ with positive leading coefficient. $f(m_0) > 0$ and $f(m_1) > 0$ (for $R < \sqrt{5}$). So $f$ could be negative in between (if it dips below 0) or positive throughout. We need to check that $f$ is negative somewhere in the interval, and actually that it's negative for all $m$ in the interior.

Hmm, actually $f$ doesn't need to be negative for ALL $m$ in the interior. It needs to be negative for the SPECIFIC $m$ of the configuration. But we don't know $m$; we need the argument to work for all possible $m$.

Wait, but if $mM < -1$ (interior), then $m$ is in the open interval $(m_1, m_0)$, and we need $f(m) < 0$ for the contradiction. If $f(m) > 0$ for some $m$ in the interior, then for that $m$, the cubic approach doesn't give a contradiction, and we'd need a different argument.

Let me check: is $f$ negative throughout the open interval $(m_1, m_0)$ for $R < \sqrt{5}$?

$f(m_0) = 1 + \sqrt{R^2-4} > 0$ and $f(m_1) = 1 - \sqrt{R^2-4}$. For $R < \sqrt{5}$, $\sqrt{R^2-4} < 1$, so $f(m_1) > 0$.

So $f > 0$ at both endpoints. For $f$ to be negative in the interior, it must have a local min below 0 in the interval.

$f'(m) = 3m^2 + 2Rm + (R+3)$.

Discriminant: $4R^2 - 12(R+3) = 4R^2 - 12R - 36 = 4(R^2 - 3R - 9)$.

For $R = \sqrt{5} \approx 2.236$: $R^2 - 3R - 9 = 5 - 6.708 - 9 = -10.708 < 0$. So $f' > 0$ everywhere, meaning $f$ is increasing. But $f(m_0) > 0$ and $f$ is increasing, so $f > 0$ on $[m_0, \infty)$ and $f < 0$ on $(-\infty, m_0)$... wait, if $f$ is increasing and $f(m_0) > 0$, then $f < 0$ for $m < m_0$ (some $m$). But $m_1 < m_0$, and $f(m_1) > 0$, so $f > 0$ on $[m_1, m_0]$.

This means $f > 0$ on the entire valid interval! So the cubic approach with $c = m$ does NOT give a contradiction in the interior either!

I must be making an error. Let me reconsider the approach.

Hmm, maybe the issue is that I should be using a different polynomial, not just $(x-m)(x-M)(x-c)$.

Let me reconsider. The general approach is: find a polynomial $p(x) = x^3 + ax^2 + bx + d$ such that $p(x) \leq 0$ on $[m, M]$ and $a + d > 1$ (so that $\sum p(b_i) = n(a + d - 1) > 0$, contradicting $p \leq 0$).

The condition $p \leq 0$ on $[m, M]$ with $p$ a cubic and leading coefficient 1 means $p$ has roots at $m$ and $M$ (and a third root $c \leq m$), OR $p$ has a root at $m$ or $M$ but not both, etc.

Actually, $p$ doesn't need to have roots at $m$ and $M$. It just needs to be $\leq 0$ on $[m, M]$. The optimal $p$ (maximizing $a + d$) subject to $p \leq 0$ on $[m, M]$ is the one that touches 0 at the endpoints, i.e., $p(m) = p(M) = 0$.

Wait, but maybe the optimal $p$ touches 0 at one endpoint and has a double root at the other? Or touches at an interior point?

For a cubic with positive leading coefficient, to be $\leq 0$ on $[m, M]$, it must be that $p(m) \leq 0$, $p(M) \leq 0$, and $p$ doesn't go positive in between. The extremal case is $p(m) = 0$ and $p(M) = 0$ (touching at both endpoints), with the third root $c \leq m$.

But we showed this doesn't work. So maybe we need a different approach entirely.

Let me reconsider. Perhaps the right approach for part (1) is not the polynomial method but a direct argument.

Actually, let me reconsider the polynomial approach. Maybe I should use a polynomial that is $\geq 0$ on $[m, M]$ and use the moments to show $\sum p(b_i) < 0$.

Consider $q(x) = -(x-m)(x-M) = -x^2 + (m+M)x - mM \geq 0$ on $[m, M]$.

$\sum q(b_i) = -n + (m+M) \cdot 0 - n \cdot mM = -n(1 + mM) \geq 0$, so $mM \leq -1$. (Same as before.)

Now consider a cubic $r(x) = -(x-m)(x-M)(x-c)$ with $c \geq M$, so $r \geq 0$ on $[m, M]$ (since $(x-m) \geq 0$, $(x-M) \leq 0$, $(x-c) \leq 0$, so $(x-m)(x-M)(x-c) \leq 0$, and $r = -$ that $\geq 0$).

$\sum r(b_i) = -[\sum b_i^3 - (m+M+c)\sum b_i^2 + (mM + c(m+M))\sum b_i - cmM \cdot n]$
$= -[-n - (m+M+c)n + 0 - cmMn]$
$= n[1 + m + M + c + cmM]$
$= n[1 + m + M + c(1 + mM)]$

Since $r \geq 0$ on $[m, M]$, $\sum r(b_i) \geq 0$, so $1 + m + M + c(1 + mM) \geq 0$ for all $c \geq M$.

If $1 + mM < 0$: $c(1+mM)$ is decreasing in $c$, so the binding constraint is at $c = M$:
$1 + m + M + M(1 + mM) \geq 0$
$1 + m + 2M + M^2 m \geq 0$
$1 + m + 2M + m M^2 \geq 0$
$1 + m(1 + M^2) + 2M \geq 0$

With $M = m + R$:
$1 + m(1 + (m+R)^2) + 2(m+R) \geq 0$
$1 + m(1 + m^2 + 2mR + R^2) + 2m + 2R \geq 0$
$1 + m + m^3 + 2m^2R + mR^2 + 2m + 2R \geq 0$
$m^3 + 2Rm^2 + (R^2 + 3)m + (1 + 2R) \geq 0$

Let me call this $g(m) = m^3 + 2Rm^2 + (R^2+3)m + (1+2R) \geq 0$.

This must hold for the actual $m$ of the configuration. If $R < \sqrt{5}$, we want to show this fails for some $m$, giving a contradiction.

But again, $m$ is determined by the configuration, not free. We need: for $R < \sqrt{5}$, $g(m) < 0$ for all valid $m$ (in the range where $mM \leq -1$).

Let me evaluate $g$ at the endpoints $m_0, m_1$ (where $mM = -1$):

At $m_0$: $m_0^2 = -Rm_0 - 1$, $m_0^3 = (R^2-1)m_0 + R$.

$g(m_0) = (R^2-1)m_0 + R + 2R(-Rm_0 - 1) + (R^2+3)m_0 + 1 + 2R$
$= (R^2-1)m_0 + R - 2R^2 m_0 - 2R + (R^2+3)m_0 + 1 + 2R$
$= (R^2 - 1 - 2R^2 + R^2 + 3)m_0 + R - 2R + 1 + 2R$
$= 2m_0 + R + 1$
$= 2 \cdot \frac{-R + \sqrt{R^2-4}}{2} + R + 1$
$= \sqrt{R^2-4} + 1 > 0$

Same as before. And $g(m_1) = 1 - \sqrt{R^2-4}$, which is $> 0$ for $R < \sqrt{5}$.

So again, $g > 0$ at both endpoints. And $g$ is a cubic with positive leading coefficient, so it's increasing for large $m$. The question is whether $g < 0$ somewhere in the interior.

$g'(m) = 3m^2 + 4Rm + (R^2+3)$. Discriminant: $16R^2 - 12(R^2+3) = 4R^2 - 36 = 4(R^2 - 9)$. For $R < 3$ (which includes $R < \sqrt{5}$), the discriminant is negative, so $g' > 0$ always, meaning $g$ is strictly increasing.

If $g$ is strictly increasing and $g(m_1) > 0$, then $g > 0$ on $[m_1, \infty)$, including the entire valid interval. So $g(m) > 0$ for all valid $m$, and the approach doesn't give a contradiction!

This means the polynomial approach with a single cubic doesn't work for this problem. I need a different approach.

Let me reconsider. Maybe the approach for part (1) uses a different technique.

Actually, let me think about this problem from scratch. The moments are:
- $E[b] = 0$, $E[b^2] = 1$, $E[b^3] = -1$ (where $E$ denotes $\frac{1}{n}\sum$).

We want to minimize $R = \max b_i - \min b_i$.

This is an optimization problem. The dual approach would use the fact that for any polynomial $p$ of degree $\leq 3$ with $p(x) \leq 0$ on $[m, M]$:

$\sum p(b_i) \leq 0$

$\sum p(b_i) = p_3 \sum b_i^3 + p_2 \sum b_i^2 + p_1 \sum b_i + p_0 \cdot n = n(p_3 \cdot (-1) + p_2 \cdot 1 + p_1 \cdot 0 + p_0) = n(-p_3 + p_2 + p_0)$

So $-p_3 + p_2 + p_0 \leq 0$, i.e., $p_0 + p_2 \leq p_3$.

We want to find the polynomial $p$ of degree $\leq 3$ with $p \leq 0$ on $[m, M]$ that maximizes $-p_3 + p_2 + p_0$ (or equivalently, minimizes $p_3 - p_2 - p_0$). If the maximum is 0, then $R = \sqrt{5}$ is the boundary.

But we also need to optimize over $[m, M]$, i.e., over $m$ and $R = M - m$.

Actually, I think the right framework is:

For a given $R$, the minimum of $p_3 - p_2 - p_0$ over all cubics $p \leq 0$ on $[m, M]$ (with $M - m = R$, optimized over $m$) gives a bound. If this minimum is $> 0$ for $R < \sqrt{5}$, then $R \geq \sqrt{5}$.

But this is a semi-infinite optimization problem. Let me think about it differently.

Actually, I realize the issue with my previous approach: I was fixing the polynomial to be $(x-m)(x-M)(x-c)$, but the optimal polynomial might not factor through $m$ and $M$.

The optimal polynomial $p \leq 0$ on $[m, M]$ that maximizes $-p_3 + p_2 + p_0$ is found by the Chebyshev-like theory. For a cubic, the optimal $p$ touches 0 at 3 points in $[m, M]$ (or at 2 points with a double root).

Let me think about this. We want to maximize $-p_3 + p_2 + p_0$ subject to $p(x) \leq 0$ on $[m, M]$, $\deg p \leq 3$.

Equivalently, minimize $p_3 - p_2 - p_0$ subject to $p \leq 0$ on $[m, M]$.

By scaling, we can normalize. Let's set $p_3 = 1$ (since we want to minimize $p_3 - p_2 - p_0$ and making $p_3$ small helps, but $p_3$ can be negative... hmm).

Actually, the sign of $p_3$ matters. If $p_3 > 0$, then $p(x) \to +\infty$ as $x \to +\infty$, so $p$ can't be $\leq 0$ everywhere, but it can be $\leq 0$ on $[m, M]$.

If $p_3 < 0$, then $p(x) \to -\infty$ as $x \to +\infty$ and $+\infty$ as $x \to -\infty$, so $p$ can be $\leq 0$ on $[m, M]$ more easily.

We want to minimize $p_3 - p_2 - p_0$. If $p_3$ is very negative, $p_3 - p_2 - p_0$ is very negative, which is good (we want it $\leq 0$). But we need $p \leq 0$ on $[m, M]$.

Actually, I think the constraint is $-p_3 + p_2 + p_0 \leq 0$, and we want to show this holds, i.e., $p_3 \geq p_2 + p_0$. The question is whether this is possible for $R < \sqrt{5}$.

Hmm, I think I need to approach this differently. Let me think about the problem using the theory of moments and Chebyshev systems.

Actually, let me just try a direct computational approach. Let me use the substitution $b_i = 1 + c \cdot u_i$ where $u_i \in [-1, 1]$ (scaling to a standard interval) and see what the moment conditions imply.

Hmm, this is getting complicated. Let me try a different approach to the problem.

**Direct approach**: Let's think about what configurations achieve $R$ close to $\sqrt{5}$.

From the 2-point analysis, the optimal continuous distribution has:
- Fraction $\beta = \frac{5-\sqrt{5}}{10}$ at $m = 1 - \sqrt{\frac{1-\beta}{\beta}} = 1 - \sqrt{\frac{5+\sqrt{5}}{5-\sqrt{5}}} \cdot \frac{1}{\sqrt{10}}$...

Actually, let me compute the exact values. $\beta = \frac{5-\sqrt{5}}{10}$, $1-\beta = \frac{5+\sqrt{5}}{10}$.

$\frac{1-\beta}{\beta} = \frac{5+\sqrt{5}}{5-\sqrt{5}} = \frac{(5+\sqrt{5})^2}{25-5} = \frac{25+10\sqrt{5}+5}{20} = \frac{30+10\sqrt{5}}{20} = \frac{3+\sqrt{5}}{2}$.

$m = 1 - \sqrt{\frac{3+\sqrt{5}}{2}}$. Note that $\frac{3+\sqrt{5}}{2} = \left(\frac{1+\sqrt{5}}{2}\right)^2 = \phi^2$ where $\phi$ is the golden ratio. So $m = 1 - \phi = 1 - \frac{1+\sqrt{5}}{2} = \frac{1-\sqrt{5}}{2}$.

Similarly, $\frac{\beta}{1-\beta} = \frac{5-\sqrt{5}}{5+\sqrt{5}} = \frac{(5-\sqrt{5})^2}{20} = \frac{30-10\sqrt{5}}{20} = \frac{3-\sqrt{5}}{2} = \left(\frac{\sqrt{5}-1}{2}\right)^2 = \psi^2$ where $\psi = \frac{\sqrt{5}-1}{2} = 1/\phi$.

$M = 1 + \psi = 1 + \frac{\sqrt{5}-1}{2} = \frac{1+\sqrt{5}}{2} = \phi$.

So $m = \frac{1-\sqrt{5}}{2}$ and $M = \frac{1+\sqrt{5}}{2}$, and $R = M - m = \sqrt{5}$. 

Also, $m = 1 - \phi$ and $M = \phi$, so $m + M = 1$ and $mM = \phi(1-\phi) = \phi - \phi^2 = \phi - (\phi + 1) = -1$. (Using $\phi^2 = \phi + 1$.)

So the extremal 2-point distribution has $mM = -1$, $m + M = 1$, $R = \sqrt{5}$.

Now, for the finite case, we need $k = \beta n$ points at $m$ and $n - k$ at $M$. Since $\beta$ is irrational, $k$ can't be exactly $\beta n$.

Let me think about the finite case more carefully. We need to find the minimum of $R$ over all configurations $(b_1, \ldots, b_n)$ satisfying the moment conditions.

**Key insight for part (2)**: The correction is $n^{-3/2}$, which suggests a connection to the discrete nature of the problem and the rounding of $\beta n$.

Let me think about the 3-point configuration. Suppose we have $k$ points at $m$, $\ell$ points at $c$, and $n - k - \ell$ points at $M$, with $\ell$ small (like $O(1)$ or $O(\sqrt{n})$).

The moment conditions are:
- $km + \ell c + (n-k-\ell)M = n$
- $km^2 + \ell c^2 + (n-k-\ell)M^2 = 2n$
- $km^3 + \ell c^3 + (n-k-\ell)M^3 = 3n$

We want to minimize $M - m$.

In the limit, $\ell/n \to 0$, and we recover the 2-point solution. The correction comes from the $O(\ell)$ perturbation.

Let me think about this more carefully. Let me parametrize: let $k = \beta n + \delta$ where $\delta$ is an integer (the rounding error), and $\ell$ is a small number.

Actually, let me think about it differently. Let me consider the general case where the $b_i$ take values in $\{m, M\}$ plus possibly some other values, and use the moment conditions to derive the bound.

Let me use a different approach. Consider the polynomial:

$$p(x) = (x - m)(x - M) \cdot q(x)$$

where $q(x)$ is a linear function chosen to make $\sum p(b_i) = 0$ (or have a specific sign).

Actually, let me try the approach from a different angle. Let me consider the "variance" of the cubic.

We have $\sum b_i = 0$, $\sum b_i^2 = n$, $\sum b_i^3 = -n$.

Consider $\sum (b_i - m)(b_i - M) = \sum b_i^2 - (m+M)\sum b_i + n \cdot mM = n + n \cdot mM = n(1 + mM)$.

Since $(b_i - m)(b_i - M) \leq 0$ (because $b_i \in [m, M]$), we get $1 + mM \leq 0$.

Now consider $\sum (b_i - m)(b_i - M)(b_i - c)$ for some $c$. On $[m, M]$, $(b_i - m)(b_i - M) \leq 0$, so $(b_i - m)(b_i - M)(b_i - c) \leq 0$ if $b_i \geq c$ (i.e., $c \leq m$) and $\geq 0$ if $c \geq M$.

For $c \leq m$: $\sum (b_i - m)(b_i - M)(b_i - c) \leq 0$.

$\sum (b_i - m)(b_i - M)(b_i - c) = \sum [b_i^3 - (m+M+c)b_i^2 + (mM + c(m+M))b_i - cmM]$
$= -n - (m+M+c)n + 0 - cmMn$
$= -n(1 + m + M + c + cmM)$
$= -n(1 + m + M + c(1 + mM))$

So $-n(1 + m + M + c(1 + mM)) \leq 0$, giving $1 + m + M + c(1 + mM) \geq 0$ for all $c \leq m$.

Similarly, for $c \geq M$: $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$, giving $1 + m + M + c(1 + mM) \leq 0$ for all $c \geq M$.

From the first ($c \leq m$): if $1 + mM < 0$, the binding constraint is $c = m$: $1 + 2m + M + m^2 M \geq 0$, i.e., $1 + 2m + M(1 + m^2) \geq 0$.

From the second ($c \geq M$): if $1 + mM < 0$, the binding constraint is $c = M$: $1 + m + 2M + M^2 m \leq 0$, i.e., $1 + m(1 + M^2) + 2M \leq 0$.

So we have two conditions:
(A) $1 + 2m + M(1 + m^2) \geq 0$
(B) $1 + m(1 + M^2) + 2M \leq 0$

With $M = m + R$:

(A) $1 + 2m + (m+R)(1+m^2) \geq 0 \Leftrightarrow m^3 + Rm^2 + (R+3)m + (1+R) \geq 0$ (this is $g(m) \geq 0$, which we called $g$ before)

(B) $1 + m(1 + (m+R)^2) + 2(m+R) \leq 0 \Leftrightarrow m^3 + 2Rm^2 + (R^2+3)m + (1+2R) \leq 0$ (this is $-g(m) \leq 0$... wait, no.)

Hmm wait, (B) is $g(m) \leq 0$ where $g(m) = m^3 + 2Rm^2 + (R^2+3)m + (1+2R)$.

But (A) is $f(m) \geq 0$ where $f(m) = m^3 + Rm^2 + (R+3)m + (1+R)$.

Wait, I think I made an error before. Let me recompute.

(A): $1 + 2m + (m+R)(1+m^2) \geq 0$
$= 1 + 2m + m + m^3 + R + Rm^2$
$= m^3 + Rm^2 + 3m + 1 + R$
$= m^3 + Rm^2 + (R+3) \cdot \frac{3m}{R+3} + ... $

OK so (A) is $f(m) := m^3 + Rm^2 + 3m + (1+R) \geq 0$.

Hmm wait, $3m$ not $(R+3)m$. Let me recheck:
$1 + 2m + m + m^3 + R + Rm^2 = 1 + 3m + m^3 + R + Rm^2 = m^3 + Rm^2 + 3m + (1+R)$.

So $f(m) = m^3 + Rm^2 + 3m + (1 + R) \geq 0$.

(B): $1 + m(1 + (m+R)^2) + 2(m+R) \leq 0$
$= 1 + m + m(m+R)^2 + 2m + 2R$
$= 1 + 3m + 2R + m(m^2 + 2mR + R^2)$
$= 1 + 3m + 2R + m^3 + 2m^2R + mR^2$
$= m^3 + 2Rm^2 + (R^2 + 3)m + (1 + 2R) \leq 0$.

So $g(m) := m^3 + 2Rm^2 + (R^2+3)m + (1+2R) \leq 0$.

Now, note that $g(m) = f(m) + Rm^2 + R^2 m + R = f(m) + R(m^2 + Rm + 1) = f(m) + R \cdot (mM + 1)$ (since $m^2 + Rm + 1 = m^2 + (M-m)m + 1 = mM + 1$).

Since $mM + 1 \leq 0$, we have $g(m) \leq f(m)$.

So (B) $g(m) \leq 0$ is a stronger condition than (A) $f(m) \geq 0$... wait, no. (A) says $f(m) \geq 0$ and (B) says $g(m) \leq 0$. Since $g \leq f$, (B) implies $f \geq g$... hmm, this doesn't directly relate them.

Actually, $g(m) = f(m) + R(mM+1)$. Since $mM + 1 \leq 0$, $g(m) \leq f(m)$. So if $g(m) \leq 0$ and $f(m) \geq 0$, we need $g(m) \leq 0 \leq f(m)$, which is consistent since $g \leq f$.

Now, at the boundary $mM = -1$ (i.e., $m^2 + Rm + 1 = 0$): $g(m) = f(m)$. And we computed $f(m_0) = 1 + \sqrt{R^2-4}$ and $f(m_1) = 1 - \sqrt{R^2-4}$.

For $R < \sqrt{5}$: $f(m_0) > 0$ and $f(m_1) > 0$. So (A) is satisfied at both endpoints. But (B) requires $g \leq 0$, and at the endpoints $g = f > 0$, so (B) is violated!

This means: at the boundary $mM = -1$, condition (B) is violated for $R < \sqrt{5}$. This gives the contradiction!

Wait, but at $mM = -1$, the configuration is 2-point (all $b_i \in \{m, M\}$), and we already know the 2-point configuration requires $R = \sqrt{5}$. So the contradiction from (B) at $mM = -1$ is just restating this.

For the interior ($mM < -1$), we need both (A) and (B) to hold. (B) is $g(m) \leq 0$. We showed $g$ is strictly increasing (for $R < 3$) and $g(m_1) = 1 - \sqrt{R^2-4} > 0$ for $R < \sqrt{5}$. So $g(m) > 0$ for all $m \geq m_1$, including the entire valid interval. So (B) is violated everywhere in the valid interval for $R < \sqrt{5}$!

Wait, that would mean $R \geq \sqrt{5}$ for all configurations, which is part (1). Let me double-check.

$g(m) = m^3 + 2Rm^2 + (R^2+3)m + (1+2R)$.

$g'(m) = 3m^2 + 4Rm + (R^2+3)$.

Discriminant of $g'$: $16R^2 - 12(R^2+3) = 4R^2 - 36$.

For $R < 3$: discriminant $< 0$, so $g' > 0$ (since leading coefficient of $g'$ is positive), so $g$ is strictly increasing.

$g(m_1) = 1 - \sqrt{R^2 - 4}$ (computed at the boundary $mM = -1$, $m = m_1$).

For $2 \leq R < \sqrt{5}$: $0 \leq \sqrt{R^2-4} < 1$, so $g(m_1) > 0$.

Since $g$ is increasing and $g(m_1) > 0$, $g(m) > 0$ for all $m > m_1$. The valid interval is $[m_1, m_0]$ with $m_1 < m_0$, so $g(m) > 0$ for all $m \in [m_1, m_0]$.

But (B) requires $g(m) \leq 0$. So (B) is violated for all $m$ in the valid interval when $R < \sqrt{5}$.

This means: for $R < \sqrt{5}$, condition (B) is violated, which means there exists $c \geq M$ such that $\sum (b_i - m)(b_i - M)(b_i - c) < 0$. But $(b_i - m)(b_i - M)(b_i - c) \geq 0$ for $c \geq M$ and $b_i \in [m, M]$. So $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$. Contradiction!

Wait, I need to be more careful. (B) says: for all $c \geq M$, $1 + m + M + c(1+mM) \leq 0$. If this is violated, it means there exists $c \geq M$ with $1 + m + M + c(1+mM) > 0$, i.e., $\sum (b_i - m)(b_i - M)(b_i - c) = -n(1 + m + M + c(1+mM)) < 0$.

But for $c \geq M$ and $b_i \in [m, M]$: $(b_i - m) \geq 0$, $(b_i - M) \leq 0$, $(b_i - c) \leq 0$, so the product is $\geq 0$. So $\sum \geq 0$, contradiction.

So the contradiction works! For $R < \sqrt{5}$, (B) is violated, giving a contradiction. This proves $R \geq \sqrt{5}$.

Great, so part (1) is proved using condition (B). The key is that $g(m) > 0$ for all valid $m$ when $R < \sqrt{5}$, which violates the necessary condition (B).

Now for part (2), we need to show $R \geq \sqrt{5} + C_2 n^{-3/2}$.

The approach is to make the argument quantitative. In part (1), we showed $g(m) > 0$ for $R < \sqrt{5}$. For part (2), we need to show that $g(m)$ is not just $> 0$ but bounded away from 0 by some amount related to $n^{-3/2}$, when $R < \sqrt{5} + C_2 n^{-3/2}$.

But wait, the argument in part (1) is exact: $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$ for $c \geq M$, and the moment conditions give $\sum = -n(1 + m + M + c(1+mM))$. The contradiction is exact, not approximate.

For part (2), we need a more refined argument. The issue is that in part (1), we used the exact moment conditions, and the contradiction is exact. For part (2), we need to show that the contradiction has some "slack" that gives the $n^{-3/2}$ correction.

Hmm, but the argument is: $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$ (since each term is $\geq 0$), and $\sum = -n(\ldots)$. So $-n(\ldots) \geq 0$, i.e., $(\ldots) \leq 0$. This is an exact inequality, not approximate.

The key for part (2) is that we need a STRICT inequality. The sum $\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$, but can it be 0? It's 0 iff each term is 0, i.e., each $b_i \in \{m, M, c\}$. If $c > M$, then $b_i = c$ is impossible (since $b_i \leq M < c$), so each $b_i \in \{m, M\}$, i.e., the configuration is 2-point.

So: if the configuration is NOT 2-point, then $\sum (b_i - m)(b_i - M)(b_i - c) > 0$ for $c > M$, giving a strict inequality $1 + m + M + c(1+mM) < 0$.

But if the configuration IS 2-point, we need a separate argument.

Let me formalize this. For $c > M$:

$\sum (b_i - m)(b_i - M)(b_i - c) \geq 0$, with equality iff all $b_i \in \{m, M\}$ (since $c > M$ means $b_i - c < 0$ for all $i$, and $(b_i - m)(b_i - M) = 0$ iff $b_i \in \{m, M\}$).

Case 1: Configuration is 2-point ($b_i \in \{m, M\}$ for all $i$). Then $k$ points at $m$ and $n-k$ at $M$, and the moment conditions give $R = \frac{n}{\sqrt{k(n-k)}}$ and the third moment condition gives $\beta = k/n = \frac{5-\sqrt{5}}{10}$ (irrational). Since $k$ must be an integer, $\beta \neq \frac{5-\sqrt{5}}{10}$, so the third moment is not exactly $-n$. But we need the third moment to be exactly $-n$. So a 2-point configuration can't satisfy all three moment conditions (for finite $n$)!

Wait, that's a key point. A 2-point configuration has 2 free parameters ($m, M$) and 1 discrete parameter ($k$), with 3 moment conditions. The first two conditions determine $m, M$ given $k$, and the third condition determines $k$ (or rather, gives an equation for $\beta = k/n$). Since the solution $\beta^*$ is irrational, no integer $k$ satisfies it. So a 2-point configuration CANNOT satisfy all three moment conditions for finite $n$.

This means: for finite $n$, every valid configuration has at least 3 distinct values, so $\sum (b_i - m)(b_i - M)(b_i - c) > 0$ for $c > M$.

This gives a strict inequality: $1 + m + M + c(1 + mM) < 0$ for all $c > M$.

In particular, at $c = M$: $1 + m + 2M + M^2 m \leq 0$ (with equality iff 2-point, which is impossible). So $g(m) < 0$ strictly.

But how much less than 0? We need to quantify the strict inequality.

$\sum (b_i - m)(b_i - M)(b_i - c) > 0$ for $c > M$.

The sum is $-n(1 + m + M + c(1+mM))$. At $c = M$:
$\sum (b_i - m)(b_i - M)^2 = -n \cdot g(m)/n = -g(m)$... wait, let me recompute.

$\sum (b_i - m)(b_i - M)(b_i - M) = \sum (b_i - m)(b_i - M)^2$.

$= \sum [b_i^3 - (m+2M)b_i^2 + (2mM + M^2)b_i - mM^2]$
$= -n - (m+2M)n + 0 - mM^2 n$
$= -n(1 + m + 2M + mM^2)$
$= -n \cdot g(m)/n$... 

Hmm, $g(m) = m^3 + 2Rm^2 + (R^2+3)m + (1+2R)$. With $M = m + R$:
$1 + m + 2M + mM^2 = 1 + m + 2(m+R) + m(m+R)^2 = 1 + 3m + 2R + m^3 + 2m^2R + mR^2 = g(m)$.

So $\sum (b_i - m)(b_i - M)^2 = -n \cdot g(m)$.

Since each term $(b_i - m)(b_i - M)^2 \geq 0$ (as $b_i \geq m$ and $(b_i - M)^2 \geq 0$), and the sum is $> 0$ (since not all $b_i \in \{m, M\}$), we get $g(m) < 0$.

Now, $\sum (b_i - m)(b_i - M)^2 > 0$. How large is this sum?

Each term is $(b_i - m)(b_i - M)^2$. For $b_i = m$ or $b_i = M$, the term is 0. For $b_i$ strictly between $m$ and $M$, the term is positive. For $b_i$ outside $[m, M]$... but $b_i \in [m

</details>
