/-- AoPS omni_math Problem (id=109, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: Find all functions $f: \mathbb{R}^2 \rightarrow \mathbb{R}$, such that
1) $f(0,x)$ is non-decreasing ;
2) for any $x,y \in \mathbb{R}$, $f(x,y)=f(y,x)$ ;
3) for any $x,y,z \in \mathbb{R}$, $(f(x,y)-f(y,z))(f(y,z)-f(z,x))(f(z,x)-f(x,y))=0$ ;
4) for any $x,y,a \in \mathbb{R}$, $f(x+a,y+a)=f(x,y)+a$ .
    Answer: f(x,y) = a + \min(x,y) \quad \text{or} \quad f(x,y) = a + \max(x,y) \quad \text{for any } a \in \mathbb{R}.
    Solution: 
Let \( f: \mathbb{R}^2 \rightarrow \mathbb{R} \) be a function satisfying the following conditions:
1. \( f(0,x) \) is non-decreasing.
2. For any \( x, y \in \mathbb{R} \), \( f(x,y) = f(y,x) \).
3. For any \( x, y, z \in \mathbb{R} \), \( (f(x,y) - f(y,z))(f(y,z) - f(z,x))(f(z,x) - f(x,y)) = 0 \).
4. For any \( x, y, a \in \mathbb{R} \), \( f(x+a, y+a) = f(x,y) + a \).

We aim to find all such functions \( f \).

First, define \( h(x) = f(0,x) \). Given that \( h(x) \) is non-decreasing, we ca
-/
