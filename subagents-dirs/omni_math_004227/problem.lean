/-- AoPS omni_math Problem (id=004227, source=, difficulty= )
    Informal statement: Let $n$ be a positive integer. A [i]Nordic[/i] square is an $n \times n$ board containing all the integers from $1$ to $n^2$ so that each cell contains exactly one number. Two different cells are considered adjacent if they share a common side. Every cell that is adjacent only to cells containing larger numbers is called a [i]valley[/i]. An [i]uphill path[/i] is a sequence of one or more cells such that:

(i) the first cell in the sequence is a valley,

(ii) each subsequent cell in the sequence is adjacent to the previous cell, and

(iii) the numbers written in the cells in the sequence are in increasing order.

Find, as a function of $n$, the smallest possible total number of uphill paths in a Nordic square.

Author: Nikola Petrovi?
    Answer: 2n(n - 1) + 1
    Solution: 

To solve the problem of finding the smallest possible total number of uphill paths in a Nordic square, we begin by understanding the structure and constraints involved:

Firstly, consider an \( n \times n \) board containing all integers from \( 1 \) to \( n^2 \), where each integer appears exactly once in a unique cell. The task involves defining specific terms like valleys and uphill paths, which guide the construction of these paths:

1. **Valley Definition**: A cell in the Nordic square is a valley if it is adjacent only to cells containing larger numbers.

2. **Uphill Path Definition**: An uphill path starts from a valley and follows a sequence of cells where each subsequent cell is adjacent to the previous one, and the numbers are strictly increasing.

Given these definitions, the objective is to determine the smallest possible total number of such uphill paths.

### Strategy:

To minimize the count of uphill paths, observe that each path begins at a valley, and valleys are critical starting points. Here’s a strategic way to approach it:

- **Grid Arrangement**: Arrange numbers in an ordered pattern to minimize valleys. One optimal way is to place numbers in increasing order along each row, filling the board left to right and top to bottom.

- **Valleys Identification**: In such an arrangement, only edge cells (first column, first row, last row, or last column) could potentially be valleys, as they are the ones more likely to be surrounded by neighbors with larger values. However, a row or column filling pattern effectively manages these conditions by minimizing such valleys on the edges.

- **Count of Paths**: When optimal ordering is used, it can be derived:
  - Each interior of the grid \( (n-1) \text{ by } (n-1) \) doesn't contribute any valley since the numbers increase logically.
  - The edges contribute limited paths due to the restricted number of smaller neighbors.
  
  Thus, the key takeaway is that only edge conditions effectively define the number of valleys and, subsequently, the paths. Careful placement ensures minimized valleys.

### Calculation:
- Considering the strategic arrangement, the edges (where valleys occur) are minimized. With this approach:
  - Each side (or edge) potentially contributes up to \( n-1 \) paths.
  - The strategic setup leads to each edge contributing exactly one valley with a possible path per possible connection.

Given this understanding, the calculated minimum number of uphill paths is realized by the expression:

\[
\boxed{2n(n - 1) + 1}
\]

This expression effectively reflects the contribution from each boundary of the Nordic square, aligning perfectly with the structure constraints.
-/
