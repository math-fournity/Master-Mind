/-- AoPS omni_math Problem (id=386, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: Let $k$ be a fixed even positive integer, $N$ is the product of $k$ distinct primes $p_1,...,p_k$, $a,b$ are two positive integers, $a,b\leq N$. Denote 
$S_1=\{d|$ $d|N, a\leq d\leq b, d$ has even number of prime factors$\}$,
$S_2=\{d|$ $d|N, a\leq d\leq b, d$ has odd number of prime factors$\}$,
Prove: $|S_1|-|S_2|\leq C^{\frac{k}{2}}_k$
    Answer: \binom{k}{k/2}
    Solution: 
Let \( k \) be a fixed even positive integer, and let \( N \) be the product of \( k \) distinct primes \( p_1, p_2, \ldots, p_k \). Let \( a \) and \( b \) be two positive integers such that \( a, b \leq N \). Define the sets:
\[
S_1 = \{ d \mid d \mid N, a \leq d \leq b, \text{ and } d \text{ has an even number of prime factors} \},
\]
\[
S_2 = \{ d \mid d \mid N, a \leq d \leq b, \text{ and } d \text{ has an odd number of prime factors} \}.
\]

We aim to prove that:
\[
|S_1| - |S_2| \leq \bi
-/
