/-- AoPS omni_math Problem (id=004138, source=, difficulty= )
    Informal statement: For any positive integer $k$, denote the sum of digits of $k$ in its decimal representation by $S(k)$. Find all polynomials $P(x)$ with integer coefficients such that for any positive integer $n \geq 2016$, the integer $P(n)$ is positive and $$S(P(n)) = P(S(n)).$$

[i]
    Answer: P(x)=c\text{ where } c\in\{1,...,9\}\text{ as well as } P(x) = x
    Solution: 

We are asked to find all polynomials \( P(x) \) with integer coefficients such that for any positive integer \( n \geq 2016 \), the following condition holds:
\[
S(P(n)) = P(S(n)),
\]
where \( S(k) \) denotes the sum of the digits of the integer \( k \).

### Step 1: Analyzing the Condition

Firstly, we observe the property:
\[
S(P(n)) = P(S(n)).
\]
This condition suggests a relationship between the polynomial evaluated at a number \( n \) and evaluated at the sum of its digits.

### Step 2: Testing Simple Polynomials

A natural starting point is to check simple polynomials, such as constant polynomials and linear polynomials.

#### Case 1: Constant Polynomial \( P(x) = c \)

If \( P(x) = c \), then:
- \( S(P(n)) = S(c) = c \) (since \( c \in \{1, 2, \ldots, 9\} \) for \( S(c) = c \)).
- \( P(S(n)) = c \).

In this case, if \( c \) is a single-digit integer (1 to 9), both sides of the equation match, i.e., \( S(P(n)) = P(S(n)) \). Therefore, polynomials of the form \( P(x) = c \) where \( c \in \{1, \ldots, 9\} \) satisfy the condition.

#### Case 2: Linear Polynomial \( P(x) = x \)

Consider \( P(x) = x \):
- \( S(P(n)) = S(n) \).
- \( P(S(n)) = S(n) \).

Clearly, the equation holds as \( S(n) = S(n) \). Therefore, \( P(x) = x \) satisfies the condition.

### Step 3: Excluding Higher-Degree Polynomials

For a polynomial of degree 2 or higher such as \( P(x) = ax^2 + bx + c \):
- The value \( P(n) \) grows as \( n^2 \), which means \( S(P(n)) \) could significantly differ from a simple expression like \( P(S(n)) \) in terms of complexity and digit count.
- It is unlikely that \( S(P(n)) = P(S(n)) \) can hold universally for all \( n \geq 2016 \) due to this disparity in growth rates and digit sums unless \( P(x) = x \).

### Conclusion

The polynomials satisfying the given condition are constants within the range where their digit sum equals themselves and the identity polynomial, specifically:
\[
P(x) = c, \quad c \in \{1, \ldots, 9\}
\]
and
\[
P(x) = x.
\]

Thus, the set of all such polynomials is:
\[
\boxed{P(x) = c \quad (c \in \{1, \ldots, 9\}) \quad \text{and} \quad P(x) = x}.
\]

-/
