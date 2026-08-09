/-- AoPS omni_math Problem (id=003989, source=, difficulty= )
    Informal statement: Let $\mathbb{R}^+$ denote the set of positive real numbers. Find all functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ such that for each $x \in \mathbb{R}^+$, there is exactly one $y \in \mathbb{R}^+$ satisfying $$xf(y)+yf(x) \leq 2$$
    Answer: f(x) = \frac{1}{x}
    Solution: 

To solve the given functional equation problem, we must find all functions \( f: \mathbb{R}^+ \to \mathbb{R}^+ \) such that for each \( x \in \mathbb{R}^+ \), there is exactly one \( y \in \mathbb{R}^+ \) satisfying

\[
xf(y) + yf(x) \leq 2.
\]

### Step 1: Analyze the Condition

Given the condition \( xf(y) + yf(x) \leq 2 \), this must be true for exactly one \( y \) for each \( x \).

### Step 2: Find a Candidate Function

Assume \( f(x) = \frac{1}{x} \).

Substitute this into the inequality condition:

\[
xf(y) + yf(x) = x \cdot \frac{1}{y} + y \cdot \frac{1}{x} = \frac{x}{y} + \frac{y}{x}.
\]

We seek \( y \) such that:

\[
\frac{x}{y} + \frac{y}{x} \leq 2.
\]

### Step 3: Simplify the Expression

The inequality \( \frac{x}{y} + \frac{y}{x} \leq 2 \) can be rearranged and simplified:

Multiplying through by \( xy \) gives

\[
x^2 + y^2 \leq 2xy.
\]

This simplifies to:

\[
(x-y)^2 \leq 0.
\]

Hence, we deduce that \( x = y \).

### Step 4: Verify Uniqueness

Since we have \( (x-y)^2 \leq 0 \), it implies \( x = y \) is the only solution permissible.

This verifies that for each \( x \), the solution for \( y \) is unique, and thus the function \( f(x) = \frac{1}{x} \) satisfies the condition exactly for one \( y = x \).

### Conclusion

The function that meets the problem’s condition is

\[
f(x) = \frac{1}{x}.
\]

Therefore, the solution to the problem is:

\[
\boxed{f(x) = \frac{1}{x}}.
\]


-/
