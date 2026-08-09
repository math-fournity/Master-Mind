/-- AoPS omni_math Problem (id=004021, source=, difficulty= )
    Informal statement: Find all positive integers $n$ for which all positive divisors of $n$ can be put into the cells of a rectangular table under the following constraints:
[list]
[*]each cell contains a distinct divisor;
[*]the sums of all rows are equal; and
[*]the sums of all columns are equal.
[/list]
    Answer: 1
    Solution: 

Let us find all positive integers \( n \) for which all positive divisors of \( n \) can be placed into the cells of a rectangular table such that:

1. Each cell contains a distinct divisor of \( n \).
2. The sums of all rows in the table are equal.
3. The sums of all columns in the table are equal.

Consider a positive integer \( n \) with divisors \( d_1, d_2, \ldots, d_k \). If these divisors can be arranged in a rectangular table with \( r \) rows and \( c \) columns such that each cell contains a distinct divisor, then the total number of divisors \( k \) must satisfy \( k = r \times c \).

The sum of each row would be \( S \), and the sum of each column would be \( T \). This implies that the total sum of all divisors, denoted \( \sigma(n) \), must satisfy:
\[ \sigma(n) = r \times S = c \times T. \]
Therefore, \( S = T \) must be true for the sums of the rows and columns to be equal, and thus:
\[ \sigma(n) = r \times S = c \times S. \]

Since \( rc = k \) and all divisors are used once, if we assume \( r \neq 1 \) and \( c \neq 1 \), then the table's ability to balance row sums and column sums implies that divisors have to allow for equal distribution, which is a very restrictive condition.

For nontrivial values of \( n \) with at least two distinct divisors, the structure implies more than one configurational constraint, leading us to check if there are simple cases where \( r = 1 \), \( c = k \) or vice versa, since \( \sigma(n) \) is often a unique value with limited partitioning.

Through analysis or creating exhaustive cases, we find that the only integer \( n \) which can ensure equality trivially when its divisors are structured in such a table is the simplest positive integer:

\[ n = 1. \]

This is because \( n = 1 \) has exactly one divisor, itself, and thus neither multiple rows nor columns apply. The configuration automatically satisfies the constraints by default, as there is only a single 'cell' which naturally adheres to equal sums.

Thus, the positive integer \( n \) for which all positive divisors can be arranged in such a way is:
\[ \boxed{1}. \]

-/
