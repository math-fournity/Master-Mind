/-- AoPS omni_math Problem (id=004361, source=, difficulty= )
    Informal statement: Can there be drawn on a circle of radius $1$ a number of $1975$ distinct points, so that the distance (measured on the chord) between any two points (from the considered points) is a rational number?
    Answer: \text{yes}
    Solution: 

We are asked whether it is possible to draw \(1975\) distinct points on a circle of radius \(1\) such that the chord distance between any two points is a rational number.

### Key Observations

1. **Chord Distance Formula**: For a circle of radius \(1\), the chord distance \(d\) between two points subtending an angle \(\theta\) at the center is given by:
   \[
   d = 2 \sin\left(\frac{\theta}{2}\right).
   \]
   We need this distance to be rational for any pair of chosen points.

2. **Rational \(\sin\) values**: The value \( \sin(\frac{\theta}{2}) \) must be a rational number divided by 2 for the chord distance to be rational. This occurs when \(\theta\) is such that \(\sin \theta\) is rational.

3. **Vertices of Regular Polygons**: On a unit circle, regular polygons can help maintain rational sine values. Specifically, if the circle is divided such that the central angle \(\theta = \frac{2\pi}{n}\) for integer \(n\) where \(\sin \theta\) is rational, then vertices of such regular polygons can be potential points.

### Chebyshev Polynomials to Ensure Rational Sine

Chebyshev polynomials, \(T_n(x)\), preserve the property:
- \( T_k(\cos \theta) = \cos(k \theta) \).

Thus, for an integer \(k\), if \(\cos \theta\) is rational (hence \(\sin \theta\) can be calculated from it), then \(T_k(\cos \theta)\) remains rational, maintaining the rationality of all involved sine values for angles that are integer multiples of \(\theta\).

### Selecting Points

To ensure every pair of the \(1975\) points has a chord distance that is rational, the points can be aligned with the vertices of a regular polygon that obeys the rational sine condition.

- **nineteenth roots of unity**: The angles of \(\frac{2\pi k}{1975}\) for \(k = 0, 1, 2, \ldots, 1974\) on a circle generate points of a regular 1975-gon on the circle. 

Since these points are symmetrically distributed and use regular divisions based on integer multiples of mainly ensured rational sine values, all resulting chord lengths for these combinations of points fulfill the condition of being a rational distance.

### Conclusion

Yes, it is indeed possible to draw \(1975\) distinct points on a circle of radius \(1\), such that the chord distance between any two points is a rational number. This arrangement leverages the geometric and algebraic properties of the unit circle and sine rationality.

Thus, the final answer is:
\[
\boxed{\text{yes}}
\]

-/
