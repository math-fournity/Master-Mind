/-- AoPS omni_math Problem (id=004157, source=, difficulty= )
    Informal statement: 2500 chess kings have to be placed on a $100 \times 100$ chessboard so that

[b](i)[/b] no king can capture any other one (i.e. no two kings are placed in two squares sharing a common vertex);
[b](ii)[/b] each row and each column contains exactly 25 kings.

Find the number of such arrangements. (Two arrangements differing by rotation or symmetry are supposed to be different.)

[i]
    Answer: 2
    Solution: 

Let us consider a \(100 \times 100\) chessboard and the placement of 2500 kings such that:

1. No king can capture another king, meaning no two kings can be placed on squares that share a common vertex.
2. Each row and each column contains exactly 25 kings.

The primary challenge is to ensure that each king is placed such that it cannot capture another, which implies that no two kings can be adjacent either horizontally, vertically, or diagonally.

### Strategy to Solve the Problem

To achieve this, we need to consider the arrangement of kings in specific patterns. An effective strategy is alternating the placement of kings, akin to a checkerboard pattern but adapted to the constraints given.

#### Step 1: Analyze the Pattern Layout

To satisfy condition (i) of no two kings sharing a common vertex, we need a pattern where each king is surrounded by non-attacking positions. The board is too large to compute manually, so a systematic pattern approach is needed.

#### Step 2: Using a Checkerboard-Like Pattern

We divide the \(100 \times 100\) board into blocks. Since each row and column must exactly contain 25 kings, one feasible pattern is:

- Divide the board into \(4 \times 4\) blocks, each containing 4 squares blocked out.
- Each block can be seen as a mini-checkerboard where two kings are placed on opposite corners of a \(2 \times 2\) segment of the \(4 \times 4\) block.

#### Step 3: Ensure 25 Kings per Row/Column

A checkerboard pattern ensures that exactly half the cells in a row or column can be filled with kings, which aligns well with the 25 kings per row/column requirement on a \(100\) cell row or column:

- Place kings in alternating positions such that no two kings are adjacent or diagonal to one another.
- First, consider one complete set pattern spanning \(50\) rows/columns, then replicate by considering a complementary pattern for the remaining \(50\).

By developing this kind of alternating row pattern, and carefully managing the intersections of rows and columns, we achieve the desired distribution.

### Conclusion

After experimentation and application of the above idea:

- We find that it is possible to achieve the desired configuration through these systematic alternating strategies.
- Arranging the board as two parts with respect to the layout ensures consistency with constraints.

Ultimately, considering symmetries and rotations didn't yield additional unique arrangements beyond these constructions.

The number of distinct arrangements satisfying the conditions (considering rotations and reflections as different) results in:
\[
\boxed{2}
\]

-/
