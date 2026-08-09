/-- AoPS omni_math Problem (id=004166, source=, difficulty= )
    Informal statement: Does there exist a set $M$ in usual Euclidean space such that for every plane $\lambda$ the intersection $M \cap \lambda$ is finite and nonempty ?

[i]
[hide="Remark"]I'm not sure I'm posting this in a right Forum.[/hide]
    Answer: \text{yes}
    Solution: 

To determine if there exists a set \( M \) in usual Euclidean space such that for every plane \(\lambda\), the intersection \( M \cap \lambda \) is finite and nonempty, we need to consider a construction that satisfies these conditions.

One possible approach is to construct the set \( M \) using a version of the "space-filling curve" concept, but within certain constraints. However, space-filling curves like the Peano or Hilbert curves fill an entire region and would not make the intersection with a plane finite, thus a different approach is needed.

Instead, consider the following construction:

Construct the set \( M \) by taking a dense set of points on every line parallel to one of the coordinate axes, such that these points are sparse in other coordinate directions. One way to do this is:

- For a subset of lines along the \( x\)-axis, \( y\)-axis, and \( z\)-axis (in \(\mathbb{R}^3\)), include points spaced in such a way that each point belongs to a single line only. Specifically, for each integer point on the \( x\)-axis of the form \((n, 0, 0)\), place a point \((n, \frac{1}{n}, \frac{1}{n})\).

This construction ensures:

1. **Non-empty intersection:** For any plane \(\lambda\) in \(\mathbb{R}^3\), there will be at least one axis-aligned line passing through or intersecting this plane at some point, and since we have points densely populating these lines, \( M \cap \lambda \) is nonempty.

2. **Finite intersection:** Given the specific choice of constructing sparse points only on one type of line, the intersection of any plane \(\lambda\) with these lines would result in a finite number of points on that plane. 

Thus, the set \( M \) satisfies the conditions of having finite and nonempty intersections with any plane \(\lambda\).

Therefore, it is indeed possible to construct such a set \( M \).

The existence of such a set \( M \) in usual Euclidean space is conclusively:
\[
\boxed{\text{yes}}
\]

-/
