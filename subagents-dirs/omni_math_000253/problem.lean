/-- AoPS omni_math Problem (id=253, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: Find out all the integer pairs $(m,n)$ such that there exist two monic polynomials $P(x)$ and $Q(x)$ ,with $\deg{P}=m$ and $\deg{Q}=n$,satisfy that $$P(Q(t))\not=Q(P(t))$$ holds for any real number $t$.
    Answer: \text{All pairs except } (1,1), (1,2k), (2k,1)
    Solution: 
To find all integer pairs \((m,n)\) such that there exist two monic polynomials \(P(x)\) and \(Q(x)\) with \(\deg{P}=m\) and \(\deg{Q}=n\) satisfying \(P(Q(t)) \neq Q(P(t))\) for any real number \(t\), we analyze the given conditions and cases.

### Analysis:
1. **Case \((m,n) = (1,1)\):**
   - If \(P(x) = x + a\) and \(Q(x) = x + b\), then \(P(Q(x)) = Q(P(x)) = x + a + b\). Thus, \(P(Q(t)) = Q(P(t))\) for any \(t\).

2. **Case \((m,n) = (2k,1)\) or \((1,2k)\):**
   - Let \(P(x) = x^m + a\) and
-/
