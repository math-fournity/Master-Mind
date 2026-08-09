/-- AoPS omni_math Problem (id=003988, source=, difficulty= )
    Informal statement: Determine all functions $f: \mathbb{Z}\to\mathbb{Z}$ satisfying \[f\big(f(m)+n\big)+f(m)=f(n)+f(3m)+2014\] for all integers $m$ and $n$.

[i]
    Answer: f(m) = 2m + 1007
    Solution: 

To determine all functions \( f: \mathbb{Z} \to \mathbb{Z} \) satisfying the functional equation:

\[
f\big(f(m) + n\big) + f(m) = f(n) + f(3m) + 2014
\]

for all integers \( m \) and \( n \), we begin by analyzing the given equation:

First, set \( n = 0 \) in the equation:

\[
f\big(f(m)\big) + f(m) = f(0) + f(3m) + 2014
\]

This can be rewritten as:

\[
f\big(f(m)\big) = f(3m) + 2014 - f(m) + f(0)
\]

Next, set \( m = 0 \):

\[
f\big(f(0) + n\big) + f(0) = f(n) + f(0) + 2014
\]

Simplifying gives:

\[
f\big(f(0) + n\big) = f(n) + 2014
\]

Let \( c = f(0) \). Then we have:

\[
f(c + n) = f(n) + 2014
\]

This equation implies that the function \( f \) is linear. Suppose \( f(n) = an + b \) for constants \( a \) and \( b \). We will determine these constants.

Plug \( f(n) = an + b \) into the function equation for some \( m \) and arbitrary \( n \):

\[
f(f(m) + n) = a(f(m) + n) + b = a(am + b + n) + b = a^2m + ab + an + b
\]

Therefore, the left-hand side becomes:

\[
f(f(m) + n) + f(m) = a^2m + ab + an + b + am + b = a^2m + am + an + 2b + ab
\]

The right-hand side is:

\[
f(n) + f(3m) + 2014 = an + (3am + b) + 2014 = an + 3am + b + 2014
\]

Equating both sides, we get:

\[
a^2m + am + an + 2b + ab = an + 3am + b + 2014
\]

Cancelling terms gives:

\[
a^2m + am + 2b + ab = 3am + b + 2014
\]

Simplifying further, we equate coefficients of terms involving \( m \):

- \( a^2 + a = 3a \) gives \( a^2 + a - 3a = 0 \) or \( a(a - 2) = 0 \)

Thus, \( a = 0 \) or \( a = 2 \).

### Case 1: \( a = 0 \)

Then \( f(n) = b \). Substituting into the original equation, we find contradictions as it does not satisfy \( a^2m + am + 2b + ab = 3am + b + 2014 \).

### Case 2: \( a = 2 \)

Then \( f(n) = 2n + b \). Substituting this back:

- For coefficients of \( m \), \( a^2 + a = 4 \), consistent.
- Coefficients of constants: \( 2b = b + 2014 \).

Solving \( 2b = b + 2014 \), we find \( b = 2014 \).

Thus, the function is:

\[
f(m) = 2m + 2014
\]

Checking: Substitute \( f(m) = 2m + 2014 \) into the equation, both sides simplify identically. Hence, \( f(m) = 2m + 2014 \) satisfies the equation.

The solution is:

\[
\boxed{2m + 1007}
\]
-/
