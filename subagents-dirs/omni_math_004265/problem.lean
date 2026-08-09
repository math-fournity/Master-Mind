/-- AoPS omni_math Problem (id=004265, source=, difficulty= )
    Informal statement: Find all positive integers $n$ for which there exists a polynomial $P(x) \in \mathbb{Z}[x]$ such that for every positive integer $m\geq 1$, the numbers $P^m(1), \ldots, P^m(n)$ leave exactly $\lceil n/2^m\rceil$ distinct remainders when divided by $n$. (Here, $P^m$ means $P$ applied $m$ times.)

[i]
    Answer: \text{ prime } n \text{ and }n=2^k
    Solution: 

Consider the problem of finding all positive integers \( n \) such that there exists a polynomial \( P(x) \in \mathbb{Z}[x] \) meeting the specified condition: for every positive integer \( m \geq 1 \), the sequence \( P^m(1), P^m(2), \ldots, P^m(n) \) produces exactly \(\left\lceil \frac{n}{2^m} \right\rceil\) distinct remainders when divided by \( n \). Here, \( P^m \) denotes \( P \) iterated \( m \) times.

### Step 1: Analyze the Condition

For a given \( n \), the problem requires that the application of the polynomial \( P \), repeated \( m \) times, transforms \( 1, 2, \ldots, n \) into numbers producing specified distinct residues modulo \( n \).

### Step 2: Consider the Case where \( n \) is a Prime

1. If \( n \) is a prime, then the polynomial \( P \) might simplify structuring on \( \mathbb{Z}/n\mathbb{Z} \), potentially allowing \( P(x) \equiv x^k \mod n \) to have the necessary property of splitting the image set into exactly \(\left\lceil \frac{n}{2^m} \right\rceil\) different values for any iteration \( m \).
2. Since \( n \) is prime, every non-zero residue in \( \mathbb{Z}/n\mathbb{Z} \) can appear up to \( n - 1 \) times. Such behavior aligns well with producing the required distinct remainders when compiled and reduced by powers of 2, as shown by ceiling divisions.

### Step 3: Consider the Case where \( n = 2^k \)

1. If \( n = 2^k \), the binary division by powers of 2 simplifies to subsequent fixed factors. It allows \( P(x) \equiv x+c \) (a constant polynomial) to iterate in a manner that naturally breaks into \(\left\lceil \frac{2^k}{2^m} \right\rceil\), simplifying into manageable binary expression splits.
2. Each iteration \( m \) reduces the effective set size by half, aligning adequately with the required number of distinct residues.

### Conclusion

Analyzing both scenarios, it becomes evident that only when \( n \) is either a prime number or a power of 2 can the polynomial \( P(x) \) be constructed to satisfy the designated residue conditions for all \( m \geq 1 \).

Thus, the set of all positive integers \( n \) fulfilling the condition are:
\[
\boxed{\text{prime } n \text{ and } n = 2^k}
\]
-/
