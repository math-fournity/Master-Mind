/-- AoPS omni_math Problem (id=3273, source=putnam, difficulty=9.0 )
    Informal statement: Find all functions $f$ from the interval $(1, \infty)$ to $(1, \infty)$ with the following property: if $x,y \in (1, \infty)$ and $x^2 \leq y \leq x^3$, then $(f(x))^2 \leq f(y) \leq (f(x))^3$.
    Answer: f(x) = x^c \text{ for some } c>0
    Solution: It is obvious that for any $c>0$, the function $f(x) = x^c$ has the desired property; we will prove that conversely, any function with the desired property has this form for some $c$. Define the function $g: (0, \infty) \to (0, \infty)$ given by $g(x) = \log f(e^x)$; this function has the property that if $x,y \in (0, \infty)$ and $2x \leq y \leq 3x$, then $2g(x) \leq g(y) \leq 3g(x)$. It will suffice to show that there exists $c>0$ such that $g(x) = cx$ for all $x >0$. Similarly, define the fun
-/
