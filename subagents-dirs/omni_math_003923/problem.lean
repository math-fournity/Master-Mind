/-- AoPS omni_math Problem (id=003923, source=, difficulty= )
    Informal statement: Call admissible a set $A$ of integers that has the following property:
If $x,y \in A$ (possibly $x=y$) then $x^2+kxy+y^2 \in A$ for every integer $k$.
Determine all pairs $m,n$ of nonzero integers such that the only admissible set containing both $m$ and $n$ is the set of all integers.

[i]
    Answer: \text{All pairs } (m, n) \text{ of nonzero integers such that } \gcd(m, n) = 1.
    Solution: 

To solve the problem, we aim to determine all pairs \((m,n)\) of nonzero integers such that the only admissible set containing both \(m\) and \(n\) is the set of all integers. According to the problem statement, a set \(A\) of integers is admissible if whenever \(x\) and \(y\) are in \(A\), \(x^2 + kxy + y^2\) is also in \(A\) for every integer \(k\).

### Step-by-Step Analysis

**1. Definition of Admissible Set**

Given the definition, for any integers \(x, y \in A\), the expression \(x^2 + kxy + y^2\) must also be in \(A\) for any integer \(k\). Notably, choosing specific values for \(k\) yields several important cases:

- When \(k = 0\), this yields \(x^2 + y^2 \in A\).
- When \(k = 1\), we obtain \(x^2 + xy + y^2 \in A\).

**2. Exploring Consequences**

We compute some values to understand the closure of \(A\) under these conditions:

- Starting with elements \(m\) and \(n\) in \(A\):
  - Using the condition \(k = 0\), both \(m^2 + n^2\) and \(n^2 + m^2 = 2n^2\) must be in \(A\).
  - Utilizing \(k = -1\), we derive:
    \[
    m^2 - mn + n^2 \in A.
    \]

- If we choose \(k\) such that the expression includes forms like Euclidean algorithms, this could result in generating 1 if \(m\) and \(n\) are coprime:

  - Particularly, repeated applications will eventually include elements such as the greatest common divisor of \(m\) and \(n\).

**3. Condition for Admissibility**

The minimal condition for a set containing \(m\) and \(n\) to be closed under these operations is \(\gcd(m, n) = 1\). This means:

- With \(\gcd(m,n) = 1\), elliptic stepping continually reduces combinations of \((m, n)\) down to \(\gcd(m,n)\).
- Hence, this process can eventually generate any integer, showing \(A\) must be the set of all integers.

**4. Conclusion**

The problem therefore reduces to determining when any elements \(m\) and \(n\) can generate the full set of integers. This happens precisely when:

\[
\gcd(m, n) = 1.
\]

Thus, the set of pairs \((m, n)\) such that the only admissible set containing both \(m\) and \(n\) is the set of all integers is exactly those pairs for which \(\gcd(m, n) = 1\). Consequently, the answer is:

\[
\boxed{\text{All pairs } (m, n) \text{ of nonzero integers such that } \gcd(m, n) = 1.}
\]

-/
