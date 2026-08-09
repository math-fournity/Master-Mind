/-- AoPS omni_math Problem (id=155, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: Proof that
$$ \sum_{m=1}^n5^{\omega (m)} \le \sum_{k=1}^n\lfloor \frac{n}{k} \rfloor \tau (k)^2  \le \sum_{m=1}^n5^{\Omega (m)} .$$
    Answer: \sum_{m=1}^n 5^{\omega(m)} \le \sum_{k=1}^n \left\lfloor \frac{n}{k} \right\rfloor \tau(k)^2 \le \sum_{m=1}^n 5^{\Omega(m)}
    Solution: 
To prove the inequality
\[
\sum_{m=1}^n 5^{\omega(m)} \le \sum_{k=1}^n \left\lfloor \frac{n}{k} \right\rfloor \tau(k)^2 \le \sum_{m=1}^n 5^{\Omega(m)},
\]
we define the following functions:
\[
\chi(n) = 3^{\omega(n)}, \quad \phi(n) = \sum_{d \mid n} \tau(d), \quad \psi(n) = 3^{\Omega(n)}.
\]

We claim that:
\[
\chi(n) \leq \phi(n) \leq \psi(n).
\]

**Proof:**

Since all functions \(\chi\), \(\phi\), and \(\psi\) are multiplicative, it suffices to check the inequality for prime powers \(p^k\).


-/
