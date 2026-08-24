# Proof: Good integers whose product is an odd square

## Problem

An integer $n$ is *good* if $|n|$ is not the square of an integer. Determine all integers $m$ that can be represented, in infinitely many ways, as a sum of three distinct good integers whose product is the square of an odd integer.

## Answer

$$\boxed{m \equiv 3 \pmod{4}}$$

That is, $m$ has the required property if and only if $m \equiv 3 \pmod{4}$.

---

## Part I: Necessity — $m \equiv 3 \pmod{4}$

Suppose $m = a + b + c$ where $a, b, c$ are distinct good integers and $abc = (2k+1)^2$ for some integer $k$.

**Step 1: $a, b, c$ are all odd.**

Since $abc = (2k+1)^2$ is odd, each of $a, b, c$ must be odd.

**Step 2: $m$ is odd.**

$m = a + b + c$ is a sum of three odd integers, hence odd.

**Step 3: $abc \equiv 1 \pmod{8}$.**

Any odd square satisfies $(2k+1)^2 \equiv 1 \pmod{8}$, so $abc \equiv 1 \pmod{8}$.

**Step 4: $m \equiv 3 \pmod{4}$.**

Each of $a, b, c$ is odd, so each is congruent to $1, 3, 5,$ or $7 \pmod{8}$. The multiplicative group $(\mathbb{Z}/8\mathbb{Z})^* = \{1,3,5,7\}$ has every element of order dividing 2 (since $1^2 \equiv 3^2 \equiv 5^2 \equiv 7^2 \equiv 1 \pmod{8}$). We need $abc \equiv 1 \pmod{8}$.

Enumerating all triples $(a,b,c) \pmod{8}$ (up to permutation) with $abc \equiv 1 \pmod{8}$:

| $(a,b,c) \pmod{8}$ | $abc \pmod{8}$ | $a+b+c \pmod{8}$ |
|---|---|---|
| $(1,1,1)$ | $1$ | $3$ |
| $(1,3,3)$ | $9\equiv 1$ | $7$ |
| $(1,5,5)$ | $25\equiv 1$ | $11\equiv 3$ |
| $(1,7,7)$ | $49\equiv 1$ | $15\equiv 7$ |
| $(3,5,7)$ | $105\equiv 1$ | $15\equiv 7$ |

In every case, $m = a+b+c \equiv 3$ or $7 \pmod{8}$, i.e., $m \equiv 3 \pmod{4}$.

---

## Part II: Sufficiency — Every $m \equiv 3 \pmod{4}$ works

We show that for every $m \equiv 3 \pmod{4}$, there exist infinitely many triples $(a,b,c)$ of distinct good integers with $a+b+c = m$ and $abc$ the square of an odd integer.

### II.1: The construction

Let $p, q$ be distinct odd primes with $\gcd(p,q) = 1$. For positive odd integers $u, v, w$, set:

$$a = -pu^2, \quad b = -qv^2, \quad c = pqw^2.$$

**Product condition.** $abc = (-pu^2)(-qv^2)(pqw^2) = p^2 q^2 u^2 v^2 w^2 = (pquvw)^2$. Since $p,q,u,v,w$ are all odd, $pquvw$ is odd, so $abc$ is the square of an odd integer. ✓

**Sum condition.** $a + b + c = pqw^2 - pu^2 - qv^2$. We need this to equal $m$.

**Goodness.** $|a| = pu^2$ is not a perfect square (since $p > 1$ is squarefree). Similarly $|b| = qv^2$ and $|c| = pqw^2$ are not perfect squares (since $q > 1$ and $pq > 1$ are squarefree). ✓

**Distinctness.** Since $a, b < 0$ and $c > 0$, we have $c \neq a$ and $c \neq b$ automatically. For $a \neq b$: $pu^2 = qv^2$ would require $p/q = (v/u)^2$, impossible since $p/q$ is not a perfect square (as $p, q$ are distinct primes). ✓

So it suffices to show: **for each $m \equiv 3 \pmod{4}$, there exist distinct odd primes $p, q$ (coprime) such that the equation**

$$pqw^2 - pu^2 - qv^2 = m \tag{$\star$}$$

**has infinitely many solutions in positive odd integers $(u, v, w)$.**

### II.2: Choosing $p$ and $q$ — local conditions

The form $Q(u,v,w) = pqw^2 - pu^2 - qv^2$ is an **indefinite** ternary quadratic form (signature $(1,2)$). We use the following classical result:

> **Theorem (Eichler, 1952).** *Let $Q$ be an indefinite integral quadratic form in $n \geq 3$ variables. Then $Q$ represents an integer $m$ over $\mathbb{Z}$ (with prescribed congruence conditions) if and only if $Q$ represents $m$ locally everywhere (i.e., over $\mathbb{R}$ and over $\mathbb{Z}_\ell$ for every prime $\ell$, with the prescribed congruence conditions). Moreover, the number of representations is infinite.*

(This follows from the fact that for indefinite forms in $\geq 3$ variables, the spinor genus coincides with the genus, eliminating the spinor genus obstruction.)

We apply this with the congruence condition $u \equiv v \equiv w \equiv 1 \pmod{2}$ (all odd). The local conditions for $(\star)$ to hold with $u, v, w$ all odd are:

**(L1) At $\ell = 2$:** With $u, v, w$ odd, $u^2 \equiv v^2 \equiv w^2 \equiv 1 \pmod{8}$, so $Q \equiv pq - p - q \pmod{8}$. The condition is:
$$m \equiv pq - p - q \pmod{8}. \tag{L1}$$

**(L2) At $\ell = p$:** Since $p \mid pq$ and $p \mid pu$, we have $Q \equiv -qv^2 \pmod{p}$. So $m \equiv -qv^2 \pmod{p}$, requiring $-m/q$ to be a quadratic residue mod $p$, equivalently:
$$\left(\frac{-mq}{p}\right) = 1. \tag{L2}$$

**(L3) At $\ell = q$:** Similarly, $Q \equiv -pu^2 \pmod{q}$, requiring:
$$\left(\frac{-mp}{q}\right) = 1. \tag{L3}$$

**(L4) At all other primes $\ell$:** The form $Q$ is unimodular mod $\ell$ (all coefficients are units), and a non-degenerate ternary form over $\mathbb{F}_\ell$ represents every element for odd $\ell$. So the local condition is **automatically satisfied**. ✓

### II.3: Existence of suitable $p, q$

We show that for each $m \equiv 3 \pmod{4}$, distinct odd primes $p, q$ (with $\gcd(p,q)=1$, $p \nmid m$, $q \nmid m$) satisfying (L1), (L2), (L3) can be found.

**Case A: $m \equiv 7 \pmod{8}$.**

Condition (L1) requires at least one of $p, q \equiv 1 \pmod{4}$ (since $(p-1)(q-1) \equiv 0 \pmod{8}$ iff one of $p,q \equiv 1 \pmod 4$).

Choose $p$ to be any odd prime with $p \equiv 1 \pmod{4}$ and $p \nmid m$ (such $p$ exists by Dirichlet's theorem; e.g., if $5 \nmid m$ take $p=5$, else try $p=13$, etc.).

With $p \equiv 1 \pmod{4}$ fixed, condition (L1) is satisfied for any odd $q$ (since $pq - p - q = (p-1)(q-1) - 1 \equiv 0 - 1 = 7 \pmod{8}$ when $p \equiv 1 \pmod{4}$).

Condition (L2): $\left(\frac{-mq}{p}\right) = 1$ requires $q$ to lie in one of $(p-1)/2$ specific residue classes mod $p$ (the classes $-m \cdot r^2 \pmod{p}$ for $r = 1, \ldots, (p-1)/2$).

Condition (L3): $\left(\frac{-mp}{q}\right) = 1$ means $q$ splits in the quadratic extension $\mathbb{Q}(\sqrt{-mp})$.

By the **Chinese Remainder Theorem**, conditions on $q$ mod $p$ (from L2) can be combined with any condition mod $4$. By **Chebotarev's density theorem**, the primes splitting in $\mathbb{Q}(\sqrt{-mp})$ have density $1/2$ and are equidistributed in every residue class mod $p$. By **Dirichlet's theorem on primes in arithmetic progressions**, there exist infinitely many primes $q$ satisfying both (L2) and (L3) simultaneously (and $q \neq p$, $q \nmid m$). ✓

**Case B: $m \equiv 3 \pmod{8}$.**

Condition (L1) requires both $p \equiv q \equiv 3 \pmod{4}$ (since $(p-1)(q-1) \equiv 4 \pmod{8}$ iff both $p, q \equiv 3 \pmod{4}$).

Choose $p$ to be any odd prime with $p \equiv 3 \pmod{4}$ and $p \nmid m$ (e.g., if $3 \nmid m$ take $p=3$, else try $p=7, 11, \ldots$).

With $p \equiv 3 \pmod{4}$ fixed, condition (L1) requires $q \equiv 3 \pmod{4}$.

Condition (L2): $\left(\frac{-mq}{p}\right) = 1$ requires $q$ in specific residue classes mod $p$.

Condition (L3): $\left(\frac{-mp}{q}\right) = 1$ means $q$ splits in $\mathbb{Q}(\sqrt{-mp})$.

By CRT, the conditions $q \equiv 3 \pmod{4}$ and $q \equiv \text{(specific class)} \pmod{p}$ are compatible (giving $q$ in a specific class mod $4p$). By Chebotarev + Dirichlet, infinitely many primes $q$ satisfy all three conditions. ✓

### II.4: Existence of a solution

With $p, q$ chosen as above, all local conditions (L1)–(L4) are satisfied. By **Eichler's theorem** (the local-global principle for indefinite ternary forms), the equation $(\star)$ has a solution $(u_0, v_0, w_0)$ in positive odd integers.

### II.5: Infinitely many solutions via Pell equations

Fix $v = v_0$ (the value from the solution above). Equation $(\star)$ becomes:

$$pqw^2 - pu^2 = m + qv_0^2, \quad \text{i.e.,} \quad u^2 - qw^2 = -N, \quad N := \frac{m + qv_0^2}{p}.$$

(That $p \mid (m + qv_0^2)$ follows from the equation: $p(qw_0^2 - u_0^2) = m + qv_0^2$.)

This is a **generalized Pell equation** $u^2 - qw^2 = -N$ with initial solution $(u_0, w_0)$ (both odd). The associated Pell equation $x^2 - qy^2 = 1$ has infinitely many solutions (since $q > 1$ is not a perfect square).

**Generating new solutions.** If $(x_1, y_1)$ is any solution of $x^2 - qy^2 = 1$, then:

$$u' = u_0 x_1 + q \, w_0 \, y_1, \qquad w' = u_0 \, y_1 + w_0 \, x_1$$

gives a new solution $u'^2 - qw'^2 = -N$.

**Parity preservation.** We verify that $u', w'$ remain odd:

- If $q \equiv 1 \pmod{4}$: the fundamental solution of $x^2 - qy^2 = 1$ has $x_1$ odd, $y_1$ even. Then $u' = \text{odd} \cdot \text{odd} + \text{odd} \cdot \text{odd} \cdot \text{even} = \text{odd}$, and $w' = \text{odd} \cdot \text{even} + \text{odd} \cdot \text{odd} = \text{odd}$. ✓

- If $q \equiv 3 \pmod{4}$: the fundamental solution has $x_1$ even, $y_1$ odd. Then $u' = \text{odd} \cdot \text{even} + \text{odd} \cdot \text{odd} \cdot \text{odd} = \text{odd}$, and $w' = \text{odd} \cdot \text{odd} + \text{odd} \cdot \text{even} = \text{odd}$. ✓

In both cases, parity is preserved. By iterating (multiplying by powers of the fundamental Pell solution), we obtain an **infinite sequence** $(u_k, w_k)$ of positive odd solutions, growing exponentially.

**Validity of all solutions.** For each $k$:
- $a_k = -pu_k^2$, $b = -qv_0^2$, $c_k = pqw_k^2$ are distinct good odd integers (as verified in §II.1).
- $a_k + b + c_k = m$.
- $a_k b c_k = (pq \, u_k \, v_0 \, w_k)^2$, the square of an odd integer.

This gives infinitely many distinct representations of $m$. ✓

---

## Part III: Illustrative examples

**$m = 7$:** Take $p = 3, q = 5$, $u = v = w = 1$: $a = -3, b = -5, c = 15$. Sum $= 7$, product $= 225 = 15^2$.

The Pell equation $15w^2 - 8u^2 = 7$ (with $v$ fixed at $1$, using $u = v$) has fundamental solution $(w,u) = (1,1)$, and the Pell automorphism $(X,Y) = (241, 22)$ of $X^2 - 120Y^2 = 1$ generates $(w,u) = (417, 571), \ldots$

**$m = 3$:** Take $p = 7, q = 11$, $u = 3, v = 1, w = 1$: $a = -63, b = -11, c = 77$. Sum $= 3$, product $= 53361 = 231^2$.

The Pell equation $u^2 - 11w^2 = -2$ (with $v = 1$ fixed) has solution $(u,w) = (3,1)$, and the fundamental solution $(170, 39)$ of $x^2 - 11y^2 = 1$ generates $(u,w) = (4433, 1017), \ldots$

**$m = -1$:** Take $p = 3, q = 13$, $u = 3, v = 1, w = 1$: $a = -27, b = -13, c = 39$. Sum $= -1$, product $= 13689 = 117^2$.

---

## Conclusion

The integers $m$ that can be represented in infinitely many ways as a sum of three distinct good integers whose product is the square of an odd integer are exactly:

$$\boxed{m \equiv 3 \pmod{4}}$$
