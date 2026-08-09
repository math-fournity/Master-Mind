/-- AoPS omni_math Problem (id=133, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: For a rational point (x,y), if xy is an integer that divided by 2 but not 3, color (x,y) red, if xy is an integer that divided by 3 but not 2, color (x,y) blue. Determine whether there is a line segment in the plane such that it contains exactly 2017 blue points and 58 red points.
    Answer: \text{Yes}
    Solution: 
Consider the line \( y = ax + b \) where \( b = 2 \) and \( a = p_1 p_2 \cdots p_m \) for primes \( p_1, p_2, \ldots, p_m \) that will be chosen appropriately. We need to ensure that for a rational point \( (x, y) \), \( xy = z \in \mathbb{Z} \) such that \( 1 + az \) is a perfect square.

We construct the primes \( p_1, p_2, \ldots, p_m \) such that \( p_i > 2017^{2017} \) and for all \( 1 \le j \le m-1 \),
\[
3 \prod_{k \ne j, 1 \le k \le m} p_k \equiv 2 \pmod{p_j}.
\]
This can be achieved by
-/
