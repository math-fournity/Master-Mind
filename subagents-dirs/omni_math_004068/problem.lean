/-- AoPS omni_math Problem (id=004068, source=, difficulty= )
    Informal statement: Let $ n \geq 2$ be a positive integer and $ \lambda$ a positive real number. Initially there are $ n$ fleas on a horizontal line, not all at the same point. We define a move as choosing two fleas at some points $ A$ and $ B$, with $ A$ to the left of $ B$, and letting the flea from $ A$ jump over the flea from $ B$ to the point $ C$ so that $ \frac {BC}{AB} \equal{} \lambda$. 

Determine all values of $ \lambda$ such that, for any point $ M$ on the line and for any initial position of the $ n$ fleas, there exists a sequence of moves that will take them all to the position right of $ M$.
    Answer: \lambda \ge \frac{1}{n-1}
    Solution: 

Let \( n \geq 2 \) be a positive integer and \( \lambda \) a positive real number. There are \( n \) fleas on a horizontal line, and we need to find the values of \( \lambda \) for which, given any point \( M \) and any initial positions of the fleas, there is a sequence of moves that can place all fleas to the right of \( M \).

### Move Description:

A move consists of selecting two fleas located at points \( A \) and \( B \) (with \( A \) to the left of \( B \)), and moving the flea from \( A \) to a new point \( C \) such that \( \frac{BC}{AB} = \lambda \).

### Analysis:

- Assume the leftmost flea is initially at position \( x_1 \) and the rightmost flea is at position \( x_n \).
- The goal is to transform the system such that all fleas are located at some position greater than \( M \).

### Considerations:

1. **Move Effect:**
   - If a flea initially at \( A \) jumps to \( C \), then:
     \[
     C = A + \lambda(B - A) = (1 - \lambda)A + \lambda B.
     \]
   - This replaces \( A \) with a point closer to \( B \) (if \( \lambda > 0 \)).

2. **Bounding Fleas to the Right:**
   - We need each flea to eventually move past \( M \). Since fleas consecutively jump rightward, the greatest possible accumulation of fleas past \( M \) occurs when effective \(\lambda\) allows maximal stretching of intervals.

3. **Condition on \(\lambda\):**
   - Starting with fleas positioned in a finite interval covering \( x_1\) to \( x_n\), progressively applying transformations:
   - If \( \lambda \) is too small, the rightward jumps might be insufficient to clear \( M \) in finite steps.

4. **Sufficient Condition:**
   - Sufficiently large \(\lambda\) ensures that the accumulative forward motion possible among successive intervals exceeds the necessary coverage over distance \( x_n - M \).
   - Analyzing proportion:
     - For \( m \) iterations to push gaps from \( x_1 \) through to beyond \( x_n \), having \( \lambda \ge \frac{1}{n-1} \) guarantees accumulative growth beyond necessary jumps.

### Conclusion:

With the above reasoning, we conclude that the values of \( \lambda \) that ensure an eventual placement of all fleas to the right of any point \( M \), for any initial configuration of fleas, are:

\[
\boxed{\lambda \ge \frac{1}{n-1}}
\] 

This bound arises from ensuring that progressive cumulative extensions with each move can bridge the intervals ensuring encompassment reaches past any arbitrary point \( M \).
-/
