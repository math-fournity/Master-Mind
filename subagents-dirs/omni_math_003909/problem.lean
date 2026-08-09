/-- AoPS omni_math Problem (id=003909, source=, difficulty= )
    Informal statement: Find all positive integers $n>2$ such that 
$$ n! \mid \prod_{ p<q\le n, p,q \, \text{primes}} (p+q)$$
    Answer: 7
    Solution: 

We are tasked with finding all positive integers \( n > 2 \) such that:

\[
n! \mid \prod_{p < q \le n, p, q \, \text{primes}} (p+q)
\]

To solve this problem, we need to analyze the divisibility of the factorial \( n! \) by the product of sums of distinct prime numbers less than or equal to \( n \).

### Step 1: Understanding the Condition

The expression \( \prod_{p < q \le n, p, q \, \text{primes}} (p+q) \) represents the product of sums of all pairs of prime numbers \((p,q)\) where both \( p \) and \( q \) are primes and \( p < q \le n \). We need to check when \( n! \) divides this product.

### Step 2: Analyzing Example Cases

Let's initially try to get a sense of what's going on by considering small values of \( n \):

1. **For \( n = 3 \):**  
   \[
   \text{Primes} = \{2, 3\}
   \]
   Possible pairs \((p,q)\) with \( p < q \): \((2,3)\).  
   Product: \( (2+3) = 5 \).  
   Check divisibility: \( 3! = 6 \) does not divide 5.  

2. **For \( n = 4 \):**  
   \[
   \text{Primes} = \{2, 3\}
   \]
   Possible pairs \((p,q)\) with \( p < q \): retains \((2,3)\).  
   Product: \( (2+3) = 5 \).  
   Check divisibility: \( 4! = 24 \) does not divide 5.  

3. **For \( n = 5 \):**  
   \[
   \text{Primes} = \{2, 3, 5\}
   \]
   Possible pairs: \((2,3), (2,5), (3,5)\).  
   Product: \( (2+3) \times (2+5) \times (3+5) = 5 \times 7 \times 8 = 280 \).  
   Check divisibility: \( 5! = 120 \) divides 280.  

4. **For \( n = 6 \):**   
   \[
   \text{Primes} = \{2, 3, 5\}
   \]
   Retains same pairs as \( n = 5 \).  
   Product: Still \( 280 \).  
   Check divisibility: \( 6! = 720 \) does not divide 280.  

5. **For \( n = 7 \):**  
   \[
   \text{Primes} = \{2, 3, 5, 7\}
   \]
   Possible pairs: \((2,3), (2,5), (2,7), (3,5), (3,7), (5,7)\).  
   Product:   
   \[
   (2+3)(2+5)(2+7)(3+5)(3+7)(5+7) = 5 \times 7 \times 9 \times 8 \times 10 \times 12
   \]

   Calculate the product:  
   \[
   5 \times 7 \times 9 \times 8 \times 10 \times 12 = 302400
   \]

   Check divisibility: \( 7! = 5040 \) divides 302400.  

### Conclusion

After examining the pattern, we find that for \( n = 7 \), the factorial \( n! \) divides the given product of sums of pairs of primes. Thus, the only positive integer \( n > 2 \) for which the condition holds is:

\[
\boxed{7}
\]

-/
