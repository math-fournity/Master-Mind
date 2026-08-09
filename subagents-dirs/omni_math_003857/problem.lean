/-- AoPS omni_math Problem (id=3857, source=imo_shortlist, difficulty=9.0 )
    Informal statement: Consider all polynomials $P(x)$ with real coefficients that have the following property: for any two real numbers $x$ and $y$ one has \[|y^2-P(x)|\le 2|x|\quad\text{if and only if}\quad |x^2-P(y)|\le 2|y|.\] Determine all possible values of $P(0)$.

[i]
    Answer: {P(0) \in (-\infty,0)\cup \{1\} }
    Solution: 
To solve the problem, we need to analyze the given condition for the polynomial \( P(x) \) with real coefficients:

\[
|y^2 - P(x)| \leq 2|x| \quad \text{if and only if} \quad |x^2 - P(y)| \leq 2|y|.
\]

We aim to find all possible values of \( P(0) \).

### Step 1: Analyze the Condition

Consider the case where \( x = 0 \). Substituting into the inequality gives:

\[
|y^2 - P(0)| \leq 0 \quad \Rightarrow \quad y^2 = P(0).
\]

This implies that \( P(0) \) must be non-negative for real \( y \).

-/
