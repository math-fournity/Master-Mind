/-- AoPS omni_math Problem (id=004014, source=, difficulty= )
    Informal statement: Find all functions $f$ from the set of real numbers into the set of real numbers which satisfy for all $x$, $y$ the identity \[ f\left(xf(x+y)\right) = f\left(yf(x)\right) +x^2\]

[i]
    Answer: f(x) = x \text{ for all } x \in \mathbb{R}f(x) = -x \text{ for all } x \in \mathbb{R}
    Solution: 

To solve the given functional equation, we need to find all functions \( f: \mathbb{R} \to \mathbb{R} \) that satisfy:

\[
f\left(xf(x+y)\right) = f\left(yf(x)\right) + x^2
\]

for all \( x, y \in \mathbb{R} \).

### Step 1: Investigate Specific Cases

Firstly, set \( y = 0 \) in the functional equation:

\[
f\left(x f(x)\right) = f(0) + x^2
\]

Let \( c = f(0) \). Thus, we have:

\[
f\left(x f(x)\right) = c + x^2 \tag{1}
\]

### Step 2: Consider General Properties

Next, consider setting \( x = 0 \) in the functional equation:

\[
f\left(0 \cdot f(y)\right) = f\left(y f(0)\right) + 0^2 = f\left(cy\right)
\]

Thus:

\[
f(0) = f(cy) \implies f \text{ is a constant function when } f(0) = 0. \tag{2}
\]

### Step 3: Explore Non-zero Cases

Assume \( x \neq 0 \). Combine equations from specific inputs:

**Case 1**: Let \( f(x) = x \). Substituting into the original equation gives:

\[
f\left(x(x+y)\right) = f(x^2 + xy) = f\left(yx\right) + x^2 = yx + x^2
\]

This simplifies to \( x^2 + xy = yx + x^2 \), which holds true for all \( x, y \).

**Case 2**: Let \( f(x) = -x \). Similarly, substituting gives:

\[
f\left(x(-x-y)\right) = f(-x^2 - xy) = f\left(-y(-x)\right) + x^2 = -yx + x^2
\]

Again simplifying to \( -x^2 - xy = -yx - x^2 \), holds for all \( x, y \).

From both cases, we can conclude the functions \( f(x) = x \) and \( f(x) = -x \) satisfy the equation.

### Final Conclusion

Since the cases we have investigated cover all possibilities of the functional equation and no other function types can be derived from given conditions, the functions satisfying the original equation are:

\[
f(x) = x \quad \text{for all } x \in \mathbb{R}
\]

and

\[
f(x) = -x \quad \text{for all } x \in \mathbb{R}
\]

Hence, the complete set of solutions is:

\[
\boxed{f(x) = x \text{ for all } x \in \mathbb{R} \text{ and } f(x) = -x \text{ for all } x \in \mathbb{R}}
\]


-/
