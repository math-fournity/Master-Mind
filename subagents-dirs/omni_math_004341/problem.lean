/-- AoPS omni_math Problem (id=004341, source=, difficulty= )
    Informal statement: Which positive integers $n$ make the equation \[\sum_{i=1}^n \sum_{j=1}^n \left\lfloor \frac{ij}{n+1} \right\rfloor=\frac{n^2(n-1)}{4}\] true?
    Answer: n \text{ such that } n+1 \text{ is prime.}
    Solution: 

We are given the equation:

\[
\sum_{i=1}^n \sum_{j=1}^n \left\lfloor \frac{ij}{n+1} \right\rfloor = \frac{n^2(n-1)}{4}
\]

and we need to determine which positive integers \( n \) satisfy this equation. The reference answer states that \( n \) should be such that \( n+1 \) is prime. Let's explore this step-by-step to understand why this condition is necessary.

### Step 1: Analyze the Double Summation

The term \(\left\lfloor \frac{ij}{n+1} \right\rfloor\) represents the greatest integer less than or equal to \(\frac{ij}{n+1}\). For each \(i\) and \(j\), this is the number of complete cycles \(k(n+1)\) that fit into \(ij\), where \(k\) is an integer.

### Step 2: Consider the Structure

If \(n+1\) is a prime, it implies more uniform distribution among terms when calculating \(\left\lfloor \frac{ij}{n+1} \right\rfloor\). Additionally, properties of primes will ensure that the maximum value \(\frac{ij}{n+1}\) distributes symmetrically within the bounds.

### Step 3: Expected Result

Given that \(\frac{n^2(n-1)}{4}\) is the expected output of the summation on the left, this indicates a particular symmetry or regularity in \(\left\lfloor \frac{ij}{n+1} \right\rfloor\) as \( i \) and \( j \) vary.

### Step 4: Validating \( n+1 \) is Prime

The formula simplifies correctly into integers when \(n+1\) is prime. This is due to the uniformity induced in combinations of \( (i, j) \) pairs when distributed over a modulus of a prime number, ensuring symmetry in the floor function evaluations to match the right side of the equation.

Hence, after analysis, the integers \(n\) that satisfy the equation coincide with the structure where \(n+1\) is a prime number.

Thus, the positive integers \( n \) that make the equation true are:
\[
\boxed{n \text{ such that } n+1 \text{ is prime.}}
\]
-/
