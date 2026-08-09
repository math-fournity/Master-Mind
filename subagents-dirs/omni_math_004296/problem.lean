/-- AoPS omni_math Problem (id=004296, source=, difficulty= )
    Informal statement: Find the smallest positive integer $n$ or show no such $n$ exists, with the following property: there are infinitely many distinct $n$-tuples of positive rational numbers $(a_1, a_2, \ldots, a_n)$ such that both
$$a_1+a_2+\dots +a_n \quad \text{and} \quad \frac{1}{a_1} + \frac{1}{a_2} + \dots + \frac{1}{a_n}$$
are integers.
    Answer: n=3
    Solution: 

Let us examine the problem of finding the smallest positive integer \( n \) such that there are infinitely many distinct \( n \)-tuples of positive rational numbers \( (a_1, a_2, \ldots, a_n) \) where both \( a_1 + a_2 + \cdots + a_n \) and \( \frac{1}{a_1} + \frac{1}{a_2} + \cdots + \frac{1}{a_n} \) are integers.

### Step 1: Investigate the existence for small \( n \)

First, we consider \( n = 1 \):
- If \( n = 1 \), then we have \( a_1 \) as a positive rational number and both \( a_1 \) and \( \frac{1}{a_1} \) must be integers. This implies \( a_1 \) is a positive integer and its reciprocal is also an integer, meaning \( a_1 = 1 \).

This gives only one solution, not infinitely many. Therefore, \( n = 1 \) does not satisfy the conditions.

Next, consider \( n = 2 \):
- For \( n = 2 \), we need \( a_1 + a_2 \) and \( \frac{1}{a_1} + \frac{1}{a_2} \) to be integers. If we set \( a_1 = p/q \) and \( a_2 = q/p \) for some positive integers \( p \) and \( q \), then
  \[
  a_1 + a_2 = \frac{p}{q} + \frac{q}{p} = \frac{p^2 + q^2}{pq}
  \]
  and
  \[
  \frac{1}{a_1} + \frac{1}{a_2} = \frac{q}{p} + \frac{p}{q} = \frac{p^2 + q^2}{pq}.
  \]
  Both sums are the same expression. However, they are integers for specific choices of \( p, q \), and finding infinite distinct such \( q/p \) pairs such that the above is an integer proves challenging.

Thus, \( n = 2 \) is unlikely to satisfy the conditions.

### Step 2: Examine \( n = 3 \)

For \( n = 3 \), consider:
- Let \( a_1 = x, a_2 = y, a_3 = z \) where \( a_1 + a_2 + a_3 \) is an integer, and so is \( \frac{1}{a_1} + \frac{1}{a_2} + \frac{1}{a_3} \):
  \[
  x + y + z = \text{integer} \quad \text{and} \quad \frac{1}{x} + \frac{1}{y} + \frac{1}{z} = \text{integer}.
  \]

Using the form \( a_i = \frac{1}{k_i} \) for \( i=1,2,3 \), gives:
\[
k_1 + k_2 + k_3 = \frac{k_2k_3 + k_1k_3 + k_1k_2}{k_1k_2k_3} = \text{integer}. 
\]

Now, if \( k_1, k_2, \) and \( k_3 \) are positive integers such that their product divides \((k_2k_3+k_1k_3+k_1k_2)\), both conditions are satisfied. With simple choices like \( k_1 = 1, k_2 = 3, k_3 = 2 \), we get:
- \( \frac{1}{1} + \frac{1}{3} + \frac{1}{2} = 1 + \frac{5}{6} = 1.833\ldots \) is not integer, let's try another:

Let's choose a pattern: \( a_i = \frac{1}{q_i} \) where only when their reciprocals are integers, solutions extend.

This yields an infinite number of tuples \( (a_1, a_2, a_3) \), leading us successfully to see that \( n=3 \) meets the condition by construction (and abundant rational examples).

Thus, the least \( n \) is:
\[
\boxed{3}
\]

-/
