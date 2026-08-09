/-- AoPS omni_math Problem (id=3266, source=putnam, difficulty=9.0 )
    Informal statement: Find the number of ordered $64$-tuples $(x_0,x_1,\dots,x_{63})$ such that $x_0,x_1,\dots,x_{63}$ are distinct elements of $\{1,2,\dots,2017\}$ and \[ x_0 + x_1 + 2x_2 + 3x_3 + \cdots + 63 x_{63} \] is divisible by 2017.
    Answer: $\frac{2016!}{1953!}- 63! \cdot 2016$
    Solution: The desired count is $\frac{2016!}{1953!}- 63! \cdot 2016$, which we compute using the principle of inclusion-exclusion. As in A2, we use the fact that 2017 is prime; this means that we can do linear algebra over the field \mathbb{F}_{2017}. In particular, every nonzero homogeneous linear equation in $n$ variables over \mathbb{F}_{2017}$ has exactly $2017^{n-1}$ solutions. For $\pi$ a partition of $\{0,\dots,63\}$, let $|\pi|$ denote the number of distinct parts of $\pi$, Let $\pi_0$ denote the 
-/
