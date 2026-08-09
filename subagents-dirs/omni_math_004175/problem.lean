/-- AoPS omni_math Problem (id=004175, source=, difficulty= )
    Informal statement: Find all functions $f: \mathbb{R} \rightarrow \mathbb{R}$, satisfying \[
f(xy)(f(x) - f(y)) = (x-y)f(x)f(y)
\] for all $x,y$.
    Answer: $\boxed{f(x)=f(1)\cdot x \mid x\in S; f(x) = 0 \mid x\not\in S}$
    Solution: 

To solve the functional equation 
\[
f(xy)(f(x) - f(y)) = (x-y)f(x)f(y)
\]
for all real numbers \(x\) and \(y\), we proceed as follows:

### Step 1: Analyze the Equation

Given the equation:
\[
f(xy)(f(x) - f(y)) = (x-y)f(x)f(y)
\]
we can perform a few initial checks. First, consider \(x = y\):
\[
f(x^2)(f(x) - f(x)) = (x-x)f(x)f(x)
\]
This simplifies to \(0 = 0\), which is trivially true, but it does not provide any new information.

### Step 2: Substituting Special Values

- **Substituting \( y = 0 \):**
  \[
  f(0)(f(x) - f(0)) = xf(x)f(0)
  \]
  If \( f(0) \neq 0 \), then dividing both sides by \( f(0) \) gives:
  \[
  f(x) - f(0) = xf(x)
  \]
  Rearranging gives:
  \[
  f(x)(1-x) = f(0)
  \]
  This implies \(f(x) = \frac{f(0)}{1-x}\). However, this must hold for all \(x\), which is not possible unless \(f(x) = 0\) for all \(x\).

- **Substituting \( x = 0 \):**
  \[
  f(0)(f(0) - f(y)) = (-y)f(0)f(y)
  \]
  If \(f(0) \neq 0\), then:
  \[
  f(y) = 0 \quad \text{for all } y
  \]
  Hence, \(f(x) = 0\) is a possible solution.

### Step 3: Consider Non-zero Solutions

Assume \(f(x) \neq 0\) for some non-zero \(x\). Substituting \(y = 1\), we get:
\[
f(x)(f(x) - f(1)) = (x-1)f(x)f(1)
\]
Simplifying this gives:
\[
f(x)f(x) - f(x)f(1) = (x-1)f(x)f(1)
\]
If \( f(x) \neq 0 \), cancel \( f(x) \) from both sides:
\[
f(x) - f(1) = (x-1)f(1)
\]
Thus, 
\[
f(x) = f(1)x
\]
This implies that \(f\) is a linear function of \(x\), specifically \( f(x) = cx\) for some constant \(c\).

### Step 4: Formulate the General Solution

The general solution is:
- If \(x \in S\), where \(S\) is some subset of \(\mathbb{R}\), then \(f(x) = f(1)x\).
- If \(x \notin S\), then \(f(x) = 0\).

Putting it together, we get for some subset \(S \subseteq \mathbb{R}\),
\[
\boxed{f(x) = f(1)\cdot x \mid x \in S; \quad f(x) = 0 \mid x \notin S}
\]

This solution framework satisfies the original functional equation for any choices of sets \(S\) by considering both the zero and non-zero functional cases.
-/
