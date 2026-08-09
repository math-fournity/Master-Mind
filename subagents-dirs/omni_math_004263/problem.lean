/-- AoPS omni_math Problem (id=004263, source=, difficulty= )
    Informal statement: Find all positive integers $ n$ such that there exists a unique integer $ a$ such that $ 0\leq a < n!$ with the following property:
\[ n!\mid a^n \plus{} 1
\]

[i]
    Answer: \text{All prime numbers or } n = 1
    Solution: 

Let us consider the problem of finding all positive integers \( n \) for which there exists a unique integer \( a \) such that \( 0 \leq a < n! \) and 

\[
n! \mid a^n + 1.
\]

### Step-by-step Solution:

1. **Understand the Divisibility Condition:**

   We require that \( a^n + 1 \equiv 0 \pmod{n!} \), meaning:

   \[
   a^n \equiv -1 \pmod{n!}.
   \]

2. **Explore Special Cases and General Patterns:**

   **Case \( n = 1 \):**

   - For \( n = 1 \), we seek \( 0 \leq a < 1! = 1 \), so \( a = 0 \).
   - Then, \( a^1 + 1 = 0^1 + 1 = 1 \equiv 0 \pmod{1} \), which holds.
  
   Hence, \( n = 1 \) is a solution.

   **Case \( n \) is a Prime:**

   - Let \( n \) be a prime number.
   - Wilson's Theorem states \( (n-1)! \equiv -1 \pmod{n} \), implying for \( a = n-1 \), we have:
     \[
     (n-1)^n = (n-1)^{n-1} \cdot (n-1) \equiv (-1)^{n-1} \cdot (n-1) \equiv -1 \equiv 0 \pmod{n}.
     \]
   - We need \( (n-1)^n + 1 \equiv 0 \pmod{n!} \).
   - Notice if \( k = n-1 \), \( (n-1)! \equiv -1 \pmod{n} \) implies:

     \[
     (n-1)^n \equiv -1 \equiv 0 \pmod{n!}.
     \]

   - Unique \( a = n-1 \) exists and satisfies the conditions for primes.

Thus, all prime numbers \( n \) also satisfy the condition as they create a unique choice for \( a = n-1 \).

3. **Check if Further Conditions Can Be Satisfied:**

   - For composite \( n \), any \( a \) less than \( n! \) that works has non-uniqueness due to additional factors canceling divisors.

4. **Conclusion:**

   By examining divisibility and uniqueness conditions, we find that:

   \[
   \boxed{\text{All prime numbers or } n = 1}
   \]

   These are the solutions where a unique \( a \) can be found satisfying the given condition.
-/
