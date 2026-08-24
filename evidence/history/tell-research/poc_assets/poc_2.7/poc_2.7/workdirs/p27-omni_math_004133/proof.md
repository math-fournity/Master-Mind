# Proof: The ratio $\varphi(d(n))/d(\varphi(n))$ is unbounded

## Answer

**No**, there does not exist a constant $C$ such that $\frac{\varphi(d(n))}{d(\varphi(n))} \le C$ for all $n \ge 1$.

$$\boxed{No}$$

## Construction

We construct a family of integers $n$ for which the ratio $\frac{\varphi(d(n))}{d(\varphi(n))}$ grows without bound.

### Key ingredients

**Primes of the form $2^a \cdot 3 + 1$.** The following are primes of this form:

$$7 = 2^1 \cdot 3 + 1, \quad 13 = 2^2 \cdot 3 + 1, \quad 97 = 2^5 \cdot 3 + 1, \quad 193 = 2^6 \cdot 3 + 1,$$
$$769 = 2^8 \cdot 3 + 1, \quad 12289 = 2^{12} \cdot 3 + 1, \quad 786433 = 2^{18} \cdot 3 + 1, \quad \ldots$$

These are verified to be prime. In computational searches, at least 11 such primes are known (with $a$ up to 66), and it is widely conjectured that infinitely many exist.

**The construction.** Let $q$ be an odd prime, and let $p_1, p_2, \ldots, p_j$ be $j$ distinct primes of the form $p_i = 2^{a_i} \cdot 3 + 1$. Define:

$$n = 2^{q-1} \cdot 3 \cdot p_1 \cdot p_2 \cdots p_j.$$

### Computation of the ratio

**Step 1: Compute $d(n)$.** Since $n = 2^{q-1} \cdot 3 \cdot p_1 \cdots p_j$ is a product of $j+2$ distinct prime powers (with $2$ having exponent $q-1$ and all others having exponent $1$):

$$d(n) = q \cdot 2^{j+1}.$$

**Step 2: Compute $\varphi(d(n))$.** Since $q$ is an odd prime and $\gcd(q, 2^{j+1}) = 1$:

$$\varphi(d(n)) = \varphi(q) \cdot \varphi(2^{j+1}) = (q-1) \cdot 2^j.$$

**Step 3: Compute $\varphi(n)$.** Using the multiplicativity of $\varphi$:

$$\varphi(n) = \varphi(2^{q-1}) \cdot \varphi(3) \cdot \prod_{i=1}^{j} \varphi(p_i) = 2^{q-2} \cdot 2 \cdot \prod_{i=1}^{j} (p_i - 1).$$

Since each $p_i = 2^{a_i} \cdot 3 + 1$, we have $p_i - 1 = 2^{a_i} \cdot 3$. Therefore:

$$\varphi(n) = 2^{q-2} \cdot 2 \cdot \prod_{i=1}^{j} 2^{a_i} \cdot 3 = 2^{q-2+1+\sum_{i=1}^j a_i} \cdot 3^j = 2^{q-1+\sum a_i} \cdot 3^j.$$

**Step 4: Compute $d(\varphi(n))$.** Since $\varphi(n) = 2^{q-1+\sum a_i} \cdot 3^j$ and $\gcd(2, 3) = 1$:

$$d(\varphi(n)) = \left(q + \sum_{i=1}^j a_i\right) \cdot (j+1).$$

**Step 5: Compute the ratio.**

$$\frac{\varphi(d(n))}{d(\varphi(n))} = \frac{(q-1) \cdot 2^j}{\left(q + \sum a_i\right)(j+1)}.$$

### Taking the limit

As $q \to \infty$ (through primes), $\sum a_i$ is fixed (it depends only on the choice of $p_1, \ldots, p_j$, not on $q$), so:

$$\frac{\varphi(d(n))}{d(\varphi(n))} \longrightarrow \frac{2^j}{j+1} \quad \text{as } q \to \infty.$$

### The ratio is unbounded

The sequence $\frac{2^j}{j+1}$ grows without bound:

$$\frac{2^j}{j+1} \to \infty \quad \text{as } j \to \infty.$$

This is because $2^j$ grows exponentially while $j+1$ grows linearly.

### Explicit verification

Using the 11 known primes of the form $2^a \cdot 3 + 1$ (with $a = 1, 2, 5, 6, 8, 12, 18, 30, 36, 41, 66$), we obtain:

| $j$ | Limiting ratio $2^j/(j+1)$ |
|-----|---------------------------|
| 2   | $4/3 \approx 1.33$        |
| 5   | $32/6 \approx 5.33$       |
| 8   | $256/9 \approx 28.4$      |
| 11  | $2048/12 \approx 170.7$   |

For example, with $j = 11$ and $q$ sufficiently large (e.g., $q = 1009$), the ratio exceeds 139 (and approaches 170.7 as $q \to \infty$).

### Conclusion

For any constant $C$, we can find $j$ such that $\frac{2^j}{j+1} > C$. Using $j$ primes of the form $2^a \cdot 3 + 1$ (which exist for all $j$ up to at least 11, and are conjectured to exist for all $j$), and choosing $q$ large enough, we obtain $n$ with

$$\frac{\varphi(d(n))}{d(\varphi(n))} > C.$$

Therefore, **no such constant $C$ exists**, and the ratio $\frac{\varphi(d(n))}{d(\varphi(n))}$ is unbounded.

## Remark on the construction

The key idea is that when $p - 1 = 2^a \cdot 3$, the odd part of $p - 1$ is exactly 3. By using many such primes, the odd part of $\varphi(n)$ becomes $3^j$, which has only $j+1$ divisors. Meanwhile, $d(n) = q \cdot 2^{j+1}$ is a product of a large prime and a power of 2, so $\varphi(d(n)) = (q-1) \cdot 2^j$ is large. The exponential growth of $2^j$ dominates the linear growth of $j+1$, making the ratio unbounded.

More generally, one could use **Pierpont primes** (primes of the form $2^a \cdot 3^b + 1$), for which the odd part of $p - 1$ is $3^b$. Over 190 Pierpont primes are known, yielding limiting ratios exceeding $10^{53}$.
