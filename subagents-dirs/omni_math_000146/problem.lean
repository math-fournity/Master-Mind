/-- AoPS omni_math Problem (id=146, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: For positive integer $k>1$, let $f(k)$ be the number of ways of factoring $k$ into product of positive integers greater than $1$ (The order of factors are not countered, for example $f(12)=4$, as $12$ can be factored in these $4$ ways: $12,2\cdot 6,3\cdot 4, 2\cdot 2\cdot 3$.
Prove: If $n$ is a positive integer greater than $1$, $p$ is a prime factor of $n$, then $f(n)\leq \frac{n}{p}$
    Answer: \frac{n}{p}
    Solution: 
For a positive integer \( k > 1 \), let \( f(k) \) represent the number of ways to factor \( k \) into a product of positive integers greater than 1. For example, \( f(12) = 4 \) because 12 can be factored in these 4 ways: \( 12 \), \( 2 \cdot 6 \), \( 3 \cdot 4 \), and \( 2 \cdot 2 \cdot 3 \).

We aim to prove that if \( n \) is a positive integer greater than 1 and \( p \) is a prime factor of \( n \), then \( f(n) \leq \frac{n}{p} \).

We proceed by using strong induction. The base case is c
-/
