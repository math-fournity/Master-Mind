/-- AoPS omni_math Problem (id=3535, source=putnam, difficulty=9.0 )
    Informal statement: Fix an integer \(b \geq 2\). Let \(f(1) = 1\), \(f(2) = 2\), and for each \(n \geq 3\), define \(f(n) = n f(d)\), where \(d\) is the number of base-\(b\) digits of \(n\). For which values of \(b\) does \(\sum_{n=1}^\infty \frac{1}{f(n)}\) converge?
    Answer: Converges for \(b=2\); diverges for \(b \geq 3\)
    Solution: The sum converges for \(b=2\) and diverges for \(b \geq 3\). We first consider \(b \geq 3\). Suppose the sum converges; then the fact that \(f(n) = n f(d)\) whenever \(b^{d-1} \leq n \leq b^{d} - 1\) yields \[\sum_{n=1}^\infty \frac{1}{f(n)} = \sum_{d=1}^\infty \frac{1}{f(d)} \sum_{n=b^{d-1}}^{b^d - 1} \frac{1}{n}.\] However, by comparing the integral of \(1/x\) with a Riemann sum, we see that \[\sum_{n=b^{d-1}}^{b^d - 1} \frac{1}{n} > \int_{b^{d-1}}^{b^d} \frac{dx}{x} = \log (b^d) - \log (b^{d-
-/
