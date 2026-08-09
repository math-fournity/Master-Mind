/-- AoPS omni_math Problem (id=004282, source=, difficulty= )
    Informal statement: For a nonnegative integer $n$ define $\operatorname{rad}(n)=1$ if $n=0$ or $n=1$, and $\operatorname{rad}(n)=p_1p_2\cdots p_k$ where $p_1<p_2<\cdots <p_k$ are all prime factors of $n$. Find all polynomials $f(x)$ with nonnegative integer coefficients such that $\operatorname{rad}(f(n))$ divides $\operatorname{rad}(f(n^{\operatorname{rad}(n)}))$ for every nonnegative integer $n$.
    Answer: f(x) = ax^m\text{ for some nonnegative integers } a \text{ and }  m
    Solution: 

To solve this problem, we need to find all polynomials \( f(x) \) with nonnegative integer coefficients such that the condition \(\operatorname{rad}(f(n))\) divides \(\operatorname{rad}(f(n^{\operatorname{rad}(n)}))\) for every nonnegative integer \( n \).

Let's start by understanding the given condition. We define:
- \(\operatorname{rad}(n)\), the "radical" of \( n \), which equals \( 1 \) if \( n=0 \) or \( n=1\), and for other \( n \), it is the product of all distinct prime factors of \( n \).

For any polynomial \( f(x) \), the condition implies:
\[
\operatorname{rad}(f(n)) \mid \operatorname{rad}(f(n^{\operatorname{rad}(n)}))
\]

### Key Insight

Observe the special role of the polynomial's structure in fulfilling the divisibility condition. Let's consider a simple polynomial of the form \( f(x) = ax^m \) where \( a \) and \( m \) are nonnegative integers.

#### Step 1: Verify for \( f(x) = ax^m \)

Assume \( f(x) = ax^m \). Then:

For any nonnegative integer \( n \):
\[
f(n) = an^m
\]
\[
f(n^{\operatorname{rad}(n)}) = a(n^{\operatorname{rad}(n)})^m = an^{m \cdot \operatorname{rad}(n)}
\]

Calculate the radicals:
\[
\operatorname{rad}(f(n)) = \operatorname{rad}(an^m) = \operatorname{rad}(a) \cdot \operatorname{rad}(n)
\]
\[
\operatorname{rad}(f(n^{\operatorname{rad}(n)})) = \operatorname{rad}\left(an^{m \cdot \operatorname{rad}(n)}\right) = \operatorname{rad}(a) \cdot \operatorname{rad}(n)
\]

Here, \(\operatorname{rad}(f(n)) = \operatorname{rad}(f(n^{\operatorname{rad}(n)}))\). Therefore, \( f(x) = ax^m \) satisfies the given divisibility condition.

#### Step 2: Consider other polynomial forms

To ensure that no other forms of \( f(x) \) satisfy the condition, consider a general polynomial \( f(x) = b_kx^k + b_{k-1}x^{k-1} + \cdots + b_1x + b_0 \) with degree \( k \geq 1 \). Assume at least two non-zero coefficients exist.

For specific values of \( n \), especially those involving prime powers and products, the expression \(\operatorname{rad}(f(n^{\operatorname{rad}(n)}))\) typically includes more, or different, prime factors than \(\operatorname{rad}(f(n))\), owing to the different forms introduced by combining terms like \( b_ix^i, b_jx^j \).

Thus, any polynomial involving multiple distinct non-zero terms will likely fail the divisibility condition for some choice of \( n \).

### Conclusion

Only polynomials of the form \( ax^m \) where \( a \) and \( m \) are nonnegative integers satisfy the requirement consistently across all nonnegative \( n \). Therefore, the set of such polynomials is:

\[
\boxed{f(x) = ax^m \text{ for some nonnegative integers } a \text{ and } m}
\]

-/
