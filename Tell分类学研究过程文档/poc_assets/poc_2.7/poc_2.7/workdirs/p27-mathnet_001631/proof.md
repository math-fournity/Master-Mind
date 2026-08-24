# Proof

## Problem

For a positive integer $a$, define $x_1 = a$ and $x_{n+1} = 2x_n + 1$ for $n \geq 1$. Let $y_n = 2^{x_n} - 1$. Determine the largest possible $k$ such that, for some positive integer $a$, the numbers $y_1, \ldots, y_k$ are all prime.

## Answer

$$\boxed{k = 2}$$

## Proof

### Preliminaries

Solving the recurrence $x_{n+1} = 2x_n + 1$: we have $x_{n+1} + 1 = 2(x_n + 1)$, so

$$x_n = 2^{n-1}(a+1) - 1.$$

In particular:

$$x_1 = a, \quad x_2 = 2a+1, \quad x_3 = 4a+3.$$

**Key fact.** If $2^m - 1$ is prime, then $m$ must be prime. This is because if $m = rs$ with $r, s > 1$, then $2^m - 1 = (2^r)^s - 1$ is divisible by $2^r - 1 > 1$.

Therefore, for $y_n = 2^{x_n} - 1$ to be prime, $x_n$ must be prime (and $x_n \geq 2$).

### Lower bound: $k \geq 2$

Take $a = 2$. Then:

$$y_1 = 2^2 - 1 = 3 \quad (\text{prime}), \qquad y_2 = 2^5 - 1 = 31 \quad (\text{prime}).$$

So $k \geq 2$.

### Upper bound: $k \leq 2$

We show that for any positive integer $a$, the numbers $y_1, y_2, y_3$ cannot all be prime. We consider three cases based on $a \bmod 3$.

---

**Case 1: $a \equiv 0 \pmod{3}$.**

Since $x_1 = a$ must be prime (for $y_1$ to be prime), we need $a = 3$. Then:

$$x_3 = 4 \cdot 3 + 3 = 15 = 3 \times 5,$$

which is composite. Hence $y_3 = 2^{15} - 1$ is composite (since $15$ is composite). So $y_1, y_2, y_3$ are not all prime.

---

**Case 2: $a \equiv 1 \pmod{3}$.**

Then $x_2 = 2a + 1 \equiv 2 \cdot 1 + 1 = 0 \pmod{3}$, so $3 \mid x_2$.

- If $a = 1$: $y_1 = 2^1 - 1 = 1$, which is not prime.
- If $a \geq 7$ (the smallest prime $\equiv 1 \pmod{3}$): $x_2 = 2a + 1 \geq 15 > 3$, so $x_2$ is divisible by $3$ and greater than $3$, hence composite. Therefore $y_2$ is composite.

In either sub-case, $y_1, y_2, y_3$ are not all prime.

---

**Case 3: $a \equiv 2 \pmod{3}$.**

*Sub-case 3a: $a = 2$.*

$$x_3 = 4 \cdot 2 + 3 = 11, \qquad y_3 = 2^{11} - 1 = 2048 - 1 = 2047 = 23 \times 89,$$

which is composite. So $y_1, y_2, y_3$ are not all prime.

*Sub-case 3b: $a \geq 5$.*

If $y_1 = 2^a - 1$ is composite, then $k = 0$ and we are done. So assume $y_1$ is prime. Then $a$ must be prime (by the key fact), and since $a \geq 5$ is an odd prime with $a \equiv 2 \pmod{3}$, we have:

$$a \equiv 5 \pmod{6}.$$

Set $q = x_3 = 4a + 3$. We consider two sub-cases:

- **If $q$ is composite:** Then $x_3$ is composite, so $y_3 = 2^{x_3} - 1$ is composite.

- **If $q$ is prime:** Since $a \equiv 5 \pmod{6}$, write $a = 6j + 5$ for some $j \geq 0$. Then:

$$q = 4a + 3 = 4(6j + 5) + 3 = 24j + 23 \equiv 7 \pmod{8}.$$

By the **second supplement to quadratic reciprocity**, the Legendre symbol $\left(\frac{2}{q}\right) = (-1)^{(q^2-1)/8}$. Since $q \equiv 7 \equiv -1 \pmod{8}$, we have $(q^2 - 1)/8 = (49 - 1)/8 = 6$ (modulo 2, this is even), so:

$$\left(\frac{2}{q}\right) = 1.$$

By **Euler's criterion**, $2$ being a quadratic residue modulo $q$ means:

$$2^{(q-1)/2} \equiv 1 \pmod{q}.$$

Now observe that:

$$\frac{q - 1}{2} = \frac{4a + 3 - 1}{2} = \frac{4a + 2}{2} = 2a + 1 = x_2.$$

Therefore:

$$q \mid 2^{x_2} - 1 = y_2.$$

Since $a \geq 5$, we have $x_2 = 2a + 1 \geq 11$, so $y_2 = 2^{x_2} - 1 \geq 2^{11} - 1 = 2047$. Meanwhile $q = 4a + 3$. For $a = 5$: $q = 23$ and $y_2 = 2047 > 23$. For larger $a$, $y_2$ grows exponentially while $q$ grows linearly, so $y_2 > q$ always holds. Thus $q$ is a **proper** divisor of $y_2$, and $y_2$ is composite.

In both sub-cases, at least one of $y_1, y_2, y_3$ is composite.

---

### Conclusion

In all cases, $y_1, y_2, y_3$ cannot all be prime, so $k \leq 2$. Combined with the lower bound $k \geq 2$ (achieved by $a = 2$), we conclude:

$$\boxed{k = 2}.$$
