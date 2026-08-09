/-- AoPS omni_math Problem (id=3218, source=putnam, difficulty=9.0 )
    Informal statement: Denote by $\mathbb{Z}^2$ the set of all points $(x,y)$ in the plane with integer coordinates. For each integer $n \geq 0$, let $P_n$ be the subset of $\mathbb{Z}^2$ consisting of the point $(0,0)$ together with all points $(x,y)$ such that $x^2 + y^2 = 2^k$ for some integer $k \leq n$. Determine, as a function of $n$, the number of four-point subsets of $P_n$ whose elements are the vertices of a square.
    Answer: 5n+1
    Solution: The answer is $5n+1$.

We first determine the set $P_n$. Let $Q_n$ be the set of points in $\mathbb{Z}^2$ of the form $(0, \pm 2^k)$ or $(\pm 2^k, 0)$ for some $k \leq n$. Let $R_n$ be the set of points in $\mathbb{Z}^2$ of the form $(\pm 2^k, \pm 2^k)$ for some $k \leq n$ (the two signs being chosen independently). We prove by induction on $n$ that \[ P_n = \{(0,0)\} \cup Q_{\lfloor n/2 \rfloor} \cup R_{\lfloor (n-1)/2 \rfloor}. \] We take as base cases the straightforward computations \begin{a
-/
