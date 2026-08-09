/-- AoPS omni_math Problem (id=004155, source=, difficulty= )
    Informal statement: Determine the largest integer $N$ for which there exists a table $T$ of integers with $N$ rows and $100$ columns that has the following properties:
$\text{(i)}$ Every row contains the numbers $1$, $2$, $\ldots$, $100$ in some order.
$\text{(ii)}$ For any two distinct rows $r$ and $s$, there is a column $c$ such that $|T(r,c) - T(s, c)|\geq 2$. (Here $T(r,c)$ is the entry in row $r$ and column $c$.)
    Answer: N=\frac{(2M)!}{2^M}
    Solution: 

To solve the problem, we need to determine the largest integer \( N \) for which a table \( T \) with \( N \) rows and 100 columns can be established under the given conditions. The conditions are: 

1. Each row contains a permutation of the numbers \( 1, 2, \ldots, 100 \).

2. For any two distinct rows \( r \) and \( s \), there exists at least one column \( c \) such that the absolute difference between the entries in this column, \( |T(r, c) - T(s, c)| \), is at least 2.

This setup ensures that no two rows are "too similar" in any column.

### Step-by-step Solution

1. **Understanding Permutations and Differences:**

   Since each row is a permutation of the numbers \( 1 \) to \( 100 \), each contains exactly one occurrence of each number from this set. Thus, if we think of two rows, their difference in any column must result from differences in the numbers themselves.

2. **Constructing a Valid Table:**

   We want to find the largest \( N \) such that the condition (ii) is fulfilled. For two rows, the condition means that we should find at least one column where the numbers differ by at least 2.

3. **Using Orthogonal Arrays:**

   This situation can be related to orthogonal arrays, specifically known as \( M(2^m) \)-arrays, where orthogonal arrays of strength 2 are constructions that provide \( N \) permutations of a set under certain constraints.

   For our problem, we observe that any choice of column index both \( r \) and \( s \) corresponds to a set partition that must be unique regarding occurrence within a column. The extremal cases that satisfy this condition can be mapped back to construction principles of these orthogonal arrays.

4. **Leveraging Known Results:**

   The construction leads us to consider permutations referenced from orthogonal arrays and Finite Projective Planes. Given the permutation of each row that forms a Latin square, it's known that for such a square with side length \( m \), there can be at most \( \frac{(2m)!}{2^m} \) such permutations ensuring unique differences. 

5. **Determining N:**

   Since each number \( 1 \) to \( 100 \) must appear exactly once per column in each permutation, and using the maximum number of possible arrangements, the largest possible \( N \) is:
   \[
   N = \frac{(2M)!}{2^M}
   \]
   where \( M = \frac{100}{2} = 50 \), aligning this problem with the theory of design matrices and permutation handling.

Thus, the largest number of rows \( N \) possible in such a table \( T \) adhering to these conditions is expressed as:
\[
\boxed{\frac{(2M)!}{2^M}}
\]
-/
