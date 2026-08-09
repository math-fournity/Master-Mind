/-- AoPS omni_math Problem (id=3861, source=imo_shortlist, difficulty=9.0 )
    Informal statement: Find all functions $f:\mathbb Z_{>0}\to \mathbb Z_{>0}$ such that $a+f(b)$ divides $a^2+bf(a)$ for all positive integers $a$ and $b$ with $a+b>2019$.
    Answer: f(a) = ka \text{ for any positive integer } a \text{ and some positive integer } k.
    Solution: 
To solve the given problem, we need to find all functions \( f: \mathbb{Z}_{>0} \to \mathbb{Z}_{>0} \) such that for all positive integers \( a \) and \( b \) with \( a+b > 2019 \), the expression \( a + f(b) \) divides \( a^2 + bf(a) \).

Let's first rewrite the divisibility condition:

\[
a + f(b) \mid a^2 + bf(a)
\]

This means that there is an integer \( k \) such that:

\[
a^2 + bf(a) = k(a + f(b))
\]

which can be rearranged as:

\[
a^2 + bf(a) = ka + kf(b)
\]

Rearranging gives:

\[
a^2 
-/
