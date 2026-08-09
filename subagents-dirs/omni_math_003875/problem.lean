/-- AoPS omni_math Problem (id=3875, source=imo, difficulty=9.0 )
    Informal statement: Find all integers $n$ for which each cell of $n \times n$ table can be filled with one of the letters $I,M$ and $O$ in such a way that:
[LIST]
[*] in each row and each column, one third of the entries are $I$, one third are $M$ and one third are $O$; and?[/*]
[*]in any diagonal, if the number of entries on the diagonal is a multiple of three, then one third of the entries are $I$, one third are $M$ and one third are $O$.[/*]
[/LIST]
[b]Note.[/b] The rows and columns of an $n \times n$ table are each labelled $1$ to $n$ in a natural order. Thus each cell corresponds to a pair of positive integer $(i,j)$ with $1 \le i,j \le n$. For $n>1$, the table has $4n-2$ diagonals of two types. A diagonal of first type consists all cells $(i,j)$  for which $i+j$ is a constant, and the diagonal of this second type consists all cells $(i,j)$ for which $i-j$ is constant.
    Answer: 9k \text{ for any positive integer } k.
    Solution: 
To solve the problem, we need to find all integers \( n \) such that an \( n \times n \) table can be filled with the letters \( I, M, O \) while satisfying the given conditions:

1. Each row and each column contains exactly one-third of \( I \)'s, \( M \)'s, and \( O \)'s.
2. For any diagonal whose length is a multiple of three, one-third of its entries must be \( I \)'s, one-third \( M \)'s, and one-third \( O \)'s.

### Analysis

1. **Row and Column Condition:**
   - Each row and column must
-/
