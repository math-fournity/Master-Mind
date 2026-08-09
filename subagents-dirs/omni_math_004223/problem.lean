/-- AoPS omni_math Problem (id=004223, source=, difficulty= )
    Informal statement: Find all triplets of positive integers $ (a,m,n)$ such that  $ a^m \plus{} 1 \mid (a \plus{} 1)^n$.
    Answer: {(a,1,n),(1,m,n)} \text{ and }{(2,3,n)\text{ where }n>1}
    Solution: 

To find all triplets of positive integers \((a, m, n)\) such that \(a^m + 1 \mid (a + 1)^n\), we need to analyze the divisibility condition \(a^m + 1 \mid (a + 1)^n\). This condition suggests that \((a + 1)^n = k(a^m + 1)\) for some integer \(k\).

**Step 1: Analyze cases where \(m = 1\):**

If \(m = 1\), then the divisibility condition becomes:
\[
a + 1 \mid (a + 1)^n
\]
which is true for all \(n\) since \((a + 1)\) clearly divides \((a + 1)^n\). Thus, for \(m = 1\), any triplet \((a, 1, n)\) satisfies the condition.

**Step 2: Analyze cases where \(a = 1\):**

If \(a = 1\), the condition becomes:
\[
1^m + 1 = 2 \mid (1 + 1)^n = 2^n
\]
This is true for all \(m\) and \(n\) since \(2\) divides any power of \(2\). Thus, for \(a = 1\), the triplet \((1, m, n)\) is always a solution.

**Step 3: Try specific values for \(a\) and analyze**

Consider \(a = 2\):
- The condition becomes:
  \[
  2^m + 1 \mid 3^n
  \]
  We need to find when this divisibility holds true.

  - If \(m = 3\), then \(2^3 + 1 = 9\), and we need \(9 \mid 3^n\). Notice \(9 = 3^2\), hence \(n \geq 2\) for divisibility since \(3^n\) must be at least a multiple of \(9\).

Thus, we find the specific triplet \((2, 3, n)\) for \(n > 1\).

**Conclusion:**

After analyzing the various cases as demonstrated, we identify the following triplets as solutions to the given divisibility condition:

- \((a, 1, n)\) for any positive \(a\) and \(n\).
- \((1, m, n)\) for any positive \(m\) and \(n\).
- \((2, 3, n)\) for any \(n > 1\).

Therefore, the complete set of solutions is:
\[
\boxed{\{(a, 1, n), (1, m, n), (2, 3, n) \text{ where } n > 1\}}
\]

-/
