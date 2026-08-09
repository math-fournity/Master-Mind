/-- AoPS omni_math Problem (id=004242, source=, difficulty= )
    Informal statement: Each positive integer $a$ undergoes the following procedure in order to obtain the number $d = d\left(a\right)$:

(i) move the last digit of $a$ to the first position to obtain the numb er $b$;
(ii) square $b$ to obtain the number $c$;
(iii) move the first digit of $c$ to the end to obtain the number $d$.

(All the numbers in the problem are considered to be represented in base $10$.)  For example, for $a=2003$, we get $b=3200$, $c=10240000$, and $d = 02400001 = 2400001 = d(2003)$.)

Find all numbers $a$ for which $d\left( a\right) =a^2$.

[i]
    Answer: a = \underbrace{2\dots2}_{n \ge 0}1, \qquad a = 2, \qquad a = 3.
    Solution: 

Given the problem, we want to find all positive integers \( a \) such that the procedure outlined results in \( d(a) = a^2 \). Let's break down the steps of the procedure and solve for \( a \).

### Procedure Analysis

1. **Step (i):** Move the last digit of \( a \) to the first position to obtain the number \( b \).

   Let's represent the number \( a \) with its digits as \( a = d_1d_2\ldots d_k \). After moving the last digit to the front, we have:

   \[
   b = d_kd_1d_2\ldots d_{k-1}
   \]

2. **Step (ii):** Square \( b \) to obtain the number \( c \).

   \[
   c = b^2
   \]

3. **Step (iii):** Move the first digit of \( c \) to the end to obtain the number \( d \).

   Suppose \( c = e_1e_2\ldots e_m \). Then,

   \[
   d = e_2e_3\ldots e_me_1
   \]

### Condition

We need \( d = a^2 \).

### Finding Solutions

Let's consider possible forms of \( a \):

- When \( a \) has a single digit, the manipulation of digits will be straightforward:

  - If \( a = 2 \): 
    - \( b = 2 \)
    - \( c = 4 \) (since \( b^2 = 2^2 = 4 \))
    - \( d = 4 \). Since \( a^2 = 4 \), this is a solution.

  - If \( a = 3 \):
    - \( b = 3 \)
    - \( c = 9 \) (since \( b^2 = 3^2 = 9 \))
    - \( d = 9 \). Since \( a^2 = 9 \), this is also a solution.

- For multi-digit numbers ending with 1, let's represent \( a \) in the form:
  \[
  a = \underbrace{2\dots2}_{n \text{ times}}1
  \]

  In this form:
  - Last digit \( 1 \) moves to the front: \( b = 1\underbrace{2\dots2}_n \)
  - Squaring \( b \),
  - The number \( d \) would again align with the transformation, maintaining the \( a^2 = d \) relationship for such a form.

### Conclusion

The numbers \( a \) satisfying \( d(a) = a^2 \) are:

\[
a = \underbrace{2\dots2}_{n \ge 0}1, \quad a = 2, \quad a = 3.
\]

So, the complete set of solutions is:

\[
\boxed{a = \underbrace{2\dots2}_{n \ge 0}1, \quad a = 2, \quad a = 3.}
\]
-/
