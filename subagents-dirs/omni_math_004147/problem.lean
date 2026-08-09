/-- AoPS omni_math Problem (id=004147, source=, difficulty= )
    Informal statement: Let $\mathbb R$ be the set of real numbers. We denote by $\mathcal F$ the set of all functions $f\colon\mathbb R\to\mathbb R$ such that
$$f(x + f(y)) = f(x) + f(y)$$
for every $x,y\in\mathbb R$ Find all rational numbers $q$ such that for every function $f\in\mathcal F$, there exists some $z\in\mathbb R$ satisfying $f(z)=qz$.
    Answer: \frac{n+1}{n}, \text {for any nonzero integer } n
    Solution: 

Let \( \mathcal{F} \) be the set of all functions \( f: \mathbb{R} \to \mathbb{R} \) satisfying the functional equation:

\[
f(x + f(y)) = f(x) + f(y)
\]

for every \( x, y \in \mathbb{R} \). We are tasked with finding all rational numbers \( q \) such that for every function \( f \in \mathcal{F} \), there exists some \( z \in \mathbb{R} \) satisfying \( f(z) = qz \).

### Step-by-step Solution

1. **Initial Observations:**
   - Substitute \( x = 0 \) in the functional equation:
     \[
     f(f(y)) = f(0) + f(y)
     \]
   - Let \( f(0) = c \), then we have:
     \[
     f(f(y)) = c + f(y)
     \]

2. **Simplifying the Condition:**
   - Substitute \( y = 0 \) in the original equation:
     \[
     f(x + c) = f(x) + c
     \]

3. **Investigate Linearity:**
   - Assume a special case where \( f \) is linear, i.e., \( f(x) = mx \) for some constant \( m \).
   - Then, substituting in the original equation:
     \[
     f(x + f(y)) = m(x + my) = mx + m^2y
     \]
     and
     \[
     f(x) + f(y) = mx + my
     \]
   - For the original functional equation to hold, \( m^2 = m \), giving us \( m = 0 \) or \( m = 1 \).

4. **General Solution and Rational Constraints:**
   - Consider \( f(x) = \frac{n+1}{n}x \) for any nonzero integer \( n \).
   - Verify \( f(x + f(y)) = f(x) + f(y) \):
     \[
     f(x + f(y)) = f\left(x + \frac{n+1}{n}y\right) = \frac{n+1}{n}\left(x + \frac{n+1}{n}y\right) = \frac{n+1}{n}x + \frac{(n+1)^2}{n^2}y
     \]
     and
     \[
     f(x) + f(y) = \frac{n+1}{n}x + \frac{n+1}{n}y
     \]
   - These functions satisfy the condition and demonstrate that the rational numbers satisfying the property are:
     \[
     \boxed{\frac{n+1}{n} \text{, for any nonzero integer } n}
     \]

The values of \( q \) that satisfy the condition for every \( f \in \mathcal{F} \) are indeed \( \frac{n+1}{n} \) where \( n \) is any nonzero integer.
-/
