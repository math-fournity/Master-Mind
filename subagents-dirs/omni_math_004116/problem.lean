/-- AoPS omni_math Problem (id=004116, source=, difficulty= )
    Informal statement: Find all polynomials $P(x)$ of odd degree $d$ and with integer coefficients satisfying the following property: for each positive integer $n$, there exists $n$ positive integers $x_1, x_2, \ldots, x_n$ such that $\frac12 < \frac{P(x_i)}{P(x_j)} < 2$ and $\frac{P(x_i)}{P(x_j)}$ is the $d$-th power of a rational number for every pair of indices $i$ and $j$ with $1 \leq i, j \leq n$.
    Answer: P(x) = a(rx + s)^d \ \text{where} \ a, r, s \ \text{are integers with} \ a \neq 0, r \geq 1 \ \text{and} \ (r, s) = 1.
    Solution: 

To solve this problem, we are tasked with finding all polynomials \( P(x) \) of odd degree \( d \) with integer coefficients satisfying a specific condition. The condition states that for each positive integer \( n \), there exist \( n \) positive integers \( x_1, x_2, \ldots, x_n \) such that the ratio \( \frac{P(x_i)}{P(x_j)} \) lies strictly between \(\frac{1}{2}\) and \(2\) and is a \(d\)-th power of a rational number for every pair of indices \( i, j \).

### Analysis

1. **Polynomial Structure:**

   Since \( P(x) \) is of odd degree \( d \), we express it in the form:
   \[
   P(x) = a_d x^d + a_{d-1} x^{d-1} + \cdots + a_1 x + a_0
   \]

   The degree \( d \) being odd ensures that the leading coefficient \( a_d \neq 0 \).

2. **Condition on Ratios:**

   The condition that \(\frac{1}{2} < \frac{P(x_i)}{P(x_j)} < 2\) and \(\frac{P(x_i)}{P(x_j)}\) is a \(d\)-th power indicates certain divisibility and growth controls on \( P(x) \). Rewriting this condition implies:
   
   \[
   P(x_i) = \left(\frac{p}{q}\right)^d P(x_j)
   \]

   where \(\left(\frac{p}{q}\right)\) is a reduced rational number and \((p/q)^d\) indicates that the ratio is indeed a \(d\)-th power.

3. **Implications on Form:**

   For the above to hold for arbitrary \( n \), particularly as \( n\) grows, implies that the polynomial \( P(x) \) must retain a consistent ratio property. This strongly suggests a form based on scaled and shifted integer variables.

4. **Determining the Polynomial:**

   A suitable candidate satisfying these conditions is:
   \[
   P(x) = a(rx + s)^d
   \]

   Here, \( a, r, s \) are integers, with \( a \neq 0 \), \( r \geq 1 \), and \( (r, s) = 1\) ensuring that the transformation and scaling do not introduce any non-integer terms or additional roots that disrupt the integer coefficient condition.

### Validation:

- **Integer Coefficients:** 
  By the form \( (rx+s)^d\), expansion ensures integer coefficients since \(r\) and \(s\) are integer and relatively prime.

- **Degree Check:** 
   The degree of \( P(x) \) remains \(d\) as desired.

- **Condition Satisfaction:**
   For \( \frac{P(x_i)}{P(x_j)} = \left(\frac{rx_i+s}{rx_j+s}\right)^d \), the ratios naturally scale as \(d\)-th powers of rational numbers, which also lie in the (1/2, 2) interval for sufficiently close choices of \( x_i \) and \( x_j \).

With these considerations, we conclude that the polynomials satisfying all conditions are indeed of the form:
\[
P(x) = a(rx + s)^d
\]
where \( a, r, s \) are integers with \( a \neq 0 \), \( r \geq 1 \), and \( (r, s) = 1 \).

### Final Answer:
\[
\boxed{P(x) = a(rx + s)^d \text{ where } a, r, s \text{ are integers with } a \neq 0, r \geq 1 \text{ and } (r, s) = 1.}
\]
-/
