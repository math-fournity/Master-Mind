/-- AoPS omni_math Problem (id=3236, source=putnam, difficulty=9.0 )
    Informal statement: Let $n$ be a positive integer. What is the largest $k$ for which there exist $n \times n$ matrices $M_1, \dots, M_k$ and $N_1, \dots, N_k$ with real entries such that for all $i$ and $j$, the matrix product $M_i N_j$ has a zero entry somewhere on its diagonal if and only if $i \neq j$?
    Answer: n^n
    Solution: The largest such $k$ is $n^n$. We first show that this value can be achieved by an explicit construction. Let $e_1,\dots,e_n$ be the standard basis of $\RR^n$. For $i_1,\dots,i_n \in \{1,\dots,n\}$, let $M_{i_1,\dots,i_n}$ be the matrix with row vectors $e_{i_1},\dots,e_{i_n}$, and let $N_{i_1,\dots,i_n}$ be the transpose of $M_{i_1,\dots,i_n}$. Then $M_{i_1,\dots,i_n} N_{j_1,\dots,j_n}$ has $k$-th diagonal entry $e_{i_k} \cdot e_{j_k}$, proving the claim. We next show that for any families of m
-/
