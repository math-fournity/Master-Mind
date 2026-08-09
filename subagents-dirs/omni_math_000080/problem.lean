/-- AoPS omni_math Problem (id=80, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: For a given positive integer $n$ and prime number $p$, find the minimum value of positive integer $m$ that satisfies the following property: for any polynomial $$f(x)=(x+a_1)(x+a_2)\ldots(x+a_n)$$ ($a_1,a_2,\ldots,a_n$ are positive integers), and for any non-negative integer $k$, there exists a non-negative integer $k'$ such that $$v_p(f(k))<v_p(f(k'))\leq v_p(f(k))+m.$$ Note: for non-zero integer $N$,$v_p(N)$ is the largest non-zero integer $t$ that satisfies $p^t\mid N$.
    Answer: n + v_p(n!)
    Solution: 
For a given positive integer \( n \) and prime number \( p \), we aim to find the minimum value of the positive integer \( m \) that satisfies the following property: for any polynomial
\[ f(x) = (x + a_1)(x + a_2) \ldots (x + a_n) \]
where \( a_1, a_2, \ldots, a_n \) are positive integers, and for any non-negative integer \( k \), there exists a non-negative integer \( k' \) such that
\[ v_p(f(k)) < v_p(f(k')) \leq v_p(f(k)) + m. \]
Here, \( v_p(N) \) denotes the largest non-negative integer \
-/
