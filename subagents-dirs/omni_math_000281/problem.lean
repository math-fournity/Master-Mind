/-- AoPS omni_math Problem (id=281, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: Let $n\geq 2$ be a given integer. Find all functions $f:\mathbb{R}\rightarrow \mathbb{R}$ such that
\[f(x-f(y))=f(x+y^n)+f(f(y)+y^n), \qquad \forall x,y \in \mathbb R.\]
    Answer: f(x) = 0 \text{ or } f(x) = -x^n
    Solution: 
Let \( n \geq 2 \) be a given integer. We aim to find all functions \( f: \mathbb{R} \rightarrow \mathbb{R} \) such that
\[
f(x - f(y)) = f(x + y^n) + f(f(y) + y^n), \quad \forall x, y \in \mathbb{R}.
\]

The solutions to this functional equation are:
1. \( f(x) = 0 \) for all \( x \in \mathbb{R} \).
2. \( f(x) = -x^n \) for all \( x \in \mathbb{R} \).

To verify, we check both functions:

1. For \( f(x) = 0 \):
\[
f(x - f(y)) = f(x - 0) = 0,
\]
\[
f(x + y^n) + f(f(y) + y^n) = 0 + 0 = 0,
\]
whi
-/
