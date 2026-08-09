/-- AoPS omni_math Problem (id=004184, source=, difficulty= )
    Informal statement: Let $ T$ denote the set of all ordered triples $ (p,q,r)$ of nonnegative integers. Find all functions $ f: T \rightarrow \mathbb{R}$ satisfying
\[ f(p,q,r) = \begin{cases} 0 & \text{if} \; pqr = 0, \\
1 + \frac{1}{6}(f(p + 1,q - 1,r) + f(p - 1,q + 1,r) & \\
+ f(p - 1,q,r + 1) + f(p + 1,q,r - 1) & \\
 + f(p,q + 1,r - 1) + f(p,q - 1,r + 1)) & \text{otherwise} \end{cases}
\]
for all nonnegative integers $ p$, $ q$, $ r$.
    Answer: {f(x,y,z)=\frac{3xyz}{x+y+z}}
    Solution: 

Given the set \( T\) of all ordered triples \( (p,q,r)\) of nonnegative integers, we need to find all functions \( f: T \rightarrow \mathbb{R} \) that satisfy the following conditions:

\[
f(p,q,r) = 
\begin{cases} 
0 & \text{if } pqr = 0, \\
1 + \frac{1}{6}(f(p + 1,q - 1,r) + f(p - 1,q + 1,r) \\
\quad + f(p - 1,q,r + 1) + f(p + 1,q,r - 1) \\
\quad + f(p,q + 1,r - 1) + f(p,q - 1,r + 1)) & \text{otherwise}.
\end{cases}
\]

### Step-by-Step Solution

1. **Initial Condition**: 
   - If any of \( p, q, \) or \( r \) is zero, then \( f(p, q, r) = 0 \). This establishes that the function evaluates to zero when any product factor is zero.

2. **Recursive Condition**:
   - For \( p, q, r > 0 \), the function is recursively defined as the average of six specific functional values plus one.

3. **Assumption and Derivation**:
   - Consider a candidate function in the form of \( f(p, q, r) = \frac{3pqr}{p+q+r} \). Let's verify if this satisfies both the base and recursive conditions.

4. **Verification (Base Case)**:
   - If any of \( p, q, \) or \( r \) is zero, \( f(p, q, r) = \frac{3 \times 0}{p + q + r} = 0 \), which matches the initial condition.

5. **Verification (Recursive Case)**:
   - Substitute \( f(p, q, r) = \frac{3pqr}{p+q+r} \) into the recursive equation and check consistency:
     \[
     f(p, q, r) = 1 + \frac{1}{6} \left( \frac{3(p+1)(q-1)r}{p+q+r} + \frac{3(p-1)(q+1)r}{p+q+r} + \cdots \right)
     \]
   - Simplifying each component and verifying reveals that this function indeed satisfies the condition due to symmetry and linearity of the recursive formula.

6. **Conclusion**: 
   - The function \( f(p, q, r) = \frac{3pqr}{p+q+r} \) satisfies the recursive functional conditions outlined in the problem.

Thus, the function \( f \) that satisfies the conditions is:

\[
\boxed{f(p,q,r) = \frac{3pqr}{p+q+r}}
\]
```
-/
