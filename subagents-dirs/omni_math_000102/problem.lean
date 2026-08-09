/-- AoPS omni_math Problem (id=102, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: Number $a$ is such that $\forall a_1, a_2, a_3, a_4 \in \mathbb{R}$, there are integers $k_1, k_2, k_3, k_4$ such that $\sum_{1 \leq i < j \leq 4} ((a_i - k_i) - (a_j - k_j))^2 \leq a$. Find the minimum of $a$.
    Answer: 1.25
    Solution: 
Let \( a \) be such that for all \( a_1, a_2, a_3, a_4 \in \mathbb{R} \), there exist integers \( k_1, k_2, k_3, k_4 \) such that
\[
\sum_{1 \leq i < j \leq 4} ((a_i - k_i) - (a_j - k_j))^2 \leq a.
\]
We aim to find the minimum value of \( a \).

Consider the numbers \( a_i = \frac{i}{4} \) for \( i = 1, 2, 3, 4 \). Let \( x_i = a_i - k_i \) be the fractional parts of \( a_i \). We can arrange \( x_i \) in increasing order and denote them by \( b_1, b_2, b_3, b_4 \). Since the fractional parts 
-/
