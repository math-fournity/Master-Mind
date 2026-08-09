/-- AoPS omni_math Problem (id=004176, source=, difficulty= )
    Informal statement: A square $ (n \minus{} 1) \times (n \minus{} 1)$ is divided into $ (n \minus{} 1)^2$ unit squares in the usual manner. Each of the $ n^2$ vertices of these squares is to be coloured red or blue. Find the number of different colourings such that each unit square has exactly two red vertices. (Two colouring schemse are regarded as different if at least one vertex is coloured differently in the two schemes.)
    Answer: $ 2^{n+1}-2$
    Solution: 

To solve the problem, we need to consider how we can distribute the colors such that each unit square in the \((n-1) \times (n-1)\) grid has exactly two red vertices. Each unit square is defined by its four vertices, and we need each four-vertex set to have exactly two vertices colored red.

The key observation here is that for each unit square on the grid, the configuration where exactly two of the four corner vertices are red could be one of the following:
1. Two opposite corners are red, and the other two opposite corners are blue.
2. Two adjacent corners are red, and the two remaining corners are blue. 

However, since each vertex belongs to multiple unit squares, these choices must be consistent across shared vertices. Upon deeper scrutiny, we recognize that no consistent way exists using adjacent pairs exclusively. What emerges indeed is an insight based on larger symmetric layouts of the entire grid rather than focusing on individual squares.

A global symmetry can guide us: the entire \( n \times n \) grid's four sides can each be assigned a block of red or blue colors; from such assignments globally dictated, units are painted locally within squares.

Let's examine the corners of the large square grid:
1. The entire grid can be divided into diagonal strips such that each diagonal parallel to the main diagonal either is consistently colored red or blue.
2. The opposite corners on a unit square can be paired such that diagonal symmetry across the grid dictates available choices.

The number of colorings with two vertices of each unit square \( \left((n-1) \times (n-1)\right) \) red therefore reduces to combinations fitting diagonal selections.

1. For any given row or column, two separate rows (or two separate columns) can dictate alternation without repeating a unit-placed pattern.
2. Simplifying further, each row and column determines one half of the diagonal content orientation over successive permutations,
3. Red-blue swap per diagonally placed sequence allows exactly one redundant pairing when considered globally (caused redundant pair at square).
4. Add permutations \(2^{n+1}\) with symmetric exchange, deduct the two globally non-working overstretching repeats: \(2\).

Thus, the total count of distinct vertex colorings is:
\[
\boxed{2^{n+1} - 2}
\]
This represents complete flexibility with symmetry reduction constraints on the overall grid, minus redundancy of reverse entire mirror-based scheme.
-/
