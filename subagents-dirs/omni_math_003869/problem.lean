/-- AoPS omni_math Problem (id=3869, source=imo_shortlist, difficulty=9.0 )
    Informal statement: Let $\mathbb{Z} _{>0}$ be the set of positive integers. Find all functions  $f: \mathbb{Z} _{>0}\rightarrow \mathbb{Z} _{>0}$ such that 
\[ m^2 + f(n) \mid mf(m) +n \]
for all positive integers $m$ and $n$.
    Answer: f(n) = n
    Solution: 
Consider the function \( f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0} \) such that for all positive integers \( m \) and \( n \),

\[
m^2 + f(n) \mid mf(m) + n.
\]

We aim to find all possible functions \( f \) that satisfy this condition.

### Step 1: Initial Substitution

First, substitute \( m = n \) in the given divisibility condition:

\[
n^2 + f(n) \mid n f(n) + n.
\]

This implies:

\[
n^2 + f(n) \mid n f(n) + n - n^2 - f(n).
\]

Rearranging gives:

\[
n^2 + f(n) \mid n (f(n) - n) + (1
-/
