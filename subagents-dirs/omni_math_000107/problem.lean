/-- AoPS omni_math Problem (id=107, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: Let $a, b, c, p, q, r$ be positive integers with $p, q, r \ge 2$. Denote
\[Q=\{(x, y, z)\in \mathbb{Z}^3 : 0 \le x \le a, 0 \le y \le b , 0 \le z \le c \}. \]
Initially, some pieces are put on the each point in $Q$, with a total of $M$ pieces. Then, one can perform the following three types of operations repeatedly:
(1) Remove $p$ pieces on $(x, y, z)$ and place a piece on $(x-1, y, z)$ ;
(2) Remove $q$ pieces on $(x, y, z)$ and place a piece on $(x, y-1, z)$ ;
(3) Remove $r$ pieces on $(x, y, z)$ and place a piece on $(x, y, z-1)$.

Find the smallest positive integer $M$ such that one can always perform a sequence of operations, making a piece placed on $(0,0,0)$, no matter how the pieces are distributed initially.
    Answer: p^a q^b r^c
    Solution: 
Let \(a, b, c, p, q, r\) be positive integers with \(p, q, r \ge 2\). Denote
\[ Q = \{(x, y, z) \in \mathbb{Z}^3 : 0 \le x \le a, 0 \le y \le b, 0 \le z \le c\}. \]
Initially, some pieces are placed on each point in \(Q\), with a total of \(M\) pieces. The following three types of operations can be performed repeatedly:
1. Remove \(p\) pieces from \((x, y, z)\) and place a piece on \((x-1, y, z)\);
2. Remove \(q\) pieces from \((x, y, z)\) and place a piece on \((x, y-1, z)\);
3. Remove \(r\) p
-/
