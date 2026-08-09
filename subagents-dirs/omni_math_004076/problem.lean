/-- AoPS omni_math Problem (id=004076, source=, difficulty= )
    Informal statement: Determine the least real number $M$ such that the inequality \[|ab(a^{2}-b^{2})+bc(b^{2}-c^{2})+ca(c^{2}-a^{2})| \leq M(a^{2}+b^{2}+c^{2})^{2}\] holds for all real numbers $a$, $b$ and $c$.
    Answer: M=\frac 9{16\sqrt 2}
    Solution: 

To find the least real number \( M \) such that the inequality 

\[
|ab(a^{2}-b^{2})+bc(b^{2}-c^{2})+ca(c^{2}-a^{2})| \leq M(a^{2}+b^{2}+c^{2})^{2}
\]

holds for all real numbers \( a, b, \) and \( c \), we proceed as follows:

### Step 1: Expression Expansion

First, expand the left-hand side of the equation:

\[
ab(a^2 - b^2) + bc(b^2 - c^2) + ca(c^2 - a^2).
\]

This can be written as 

\[
ab(a + b)(a - b) + bc(b + c)(b - c) + ca(c + a)(c - a).
\]

### Step 2: Symmetric Properties

Since the expression is symmetric in all its components, we suspect that the maximum value will occur when the variables are related in a symmetric way, such as when \( a = b = c \) or their permutations.

### Step 3: Special Case Consideration

Consider the special case when \( a = b = c = 1 \):

\[
ab(a^2 - b^2) + bc(b^2 - c^2) + ca(c^2 - a^2) = 0.
\]

Thus, if \( a = b = c \), the left-hand side equals zero, which trivially satisfies the inequality for any \( M \).

### Step 4: Numerical Trials

For a non-trivial case, let us assume specific values such as \( a = 1, b = 1, \) and \( c = 0 \):

\[
ab(a^2 - b^2) + bc(b^2 - c^2) + ca(c^2 - a^2) = 1 \times 1(1^2 - 1^2) + 1 \times 0(1^2 - 0^2) + 0 \times 1(0^2 - 1^2) = 0.
\]

Thus, specific test values give zero, which also trivially satisfies the inequality.

To determine \( M \), take a case when \( a = \sqrt{2}, b = \sqrt{2}, c = 0 \):

\[
ab(a^2 - b^2) = 2(2 - 2) = 0.
\]

### Step 5: Variational Method and Estimation

Finally, for extreme values or using variational methods, the real number value \( M \) becomes the bounding constant whereby, through algebraic or inequality methods, calculation provides us the condition

\[
M = \frac{9}{16\sqrt{2}}.
\]

Hence, the minimum value of \( M \) that satisfies the inequality for all real numbers \( a, b, \) and \( c \) is 

\[
\boxed{\frac{9}{16\sqrt{2}}}.
\]


-/
