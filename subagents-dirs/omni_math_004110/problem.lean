/-- AoPS omni_math Problem (id=004110, source=, difficulty= )
    Informal statement: Find all function $f:\mathbb{R}\rightarrow\mathbb{R}$ such that for all $x,y\in\mathbb{R}$ the following equality holds \[
f(\left\lfloor x\right\rfloor y)=f(x)\left\lfloor f(y)\right\rfloor \] where $\left\lfloor a\right\rfloor $ is greatest integer not greater than $a.$

[i]
    Answer: f(x)=0\forall x\in\mathbb{R},f(x)=c\forall x\in\mathbb{R}, 1\leq c<2
    Solution: 

To solve the functional equation 
\[
f(\left\lfloor x\right\rfloor y) = f(x) \left\lfloor f(y) \right\rfloor
\]
for all \( x, y \in \mathbb{R} \), where \( \left\lfloor a \right\rfloor \) denotes the greatest integer not greater than \( a \), we proceed as follows:

### Step 1: Analyze the Equation for \( x = 0 \)

Substitute \( x = 0 \) into the equation:
\[
f(\left\lfloor 0 \right\rfloor y) = f(0) \left\lfloor f(y) \right\rfloor.
\]
Since \( \left\lfloor 0 \right\rfloor = 0 \), we have:
\[
f(0) = f(0) \left\lfloor f(y) \right\rfloor.
\]
This equation implies that either \( f(0) = 0 \) or \( \left\lfloor f(y) \right\rfloor = 1 \) for all \( y \).

### Step 2: Consider the Case \( f(0) = 0 \)

If \( f(0) = 0 \), the equation becomes:
\[
f(\left\lfloor x\right\rfloor y) = f(x) \left\lfloor f(y) \right\rfloor.
\]
Substituting \( y = 1 \) gives:
\[
f(\left\lfloor x \right\rfloor) = f(x) \left\lfloor f(1) \right\rfloor.
\]
If \( \left\lfloor f(1) \right\rfloor = 0 \), then \( f(x) = 0 \) for all \( x \), which is one possible solution. Thus, \( f(x) = 0 \quad \forall x \in \mathbb{R} \).

### Step 3: Consider the Case \( \left\lfloor f(y) \right\rfloor = 1 \)

If \( \left\lfloor f(y) \right\rfloor = 1 \) for all \( y \), then:
\[
1 \le f(y) < 2 \text{ for all } y.
\]
In this case, the original equation simplifies to:
\[
f(\left\lfloor x \right\rfloor y) = f(x).
\]
For all \( y \neq 0 \), choosing \( x = 0 \) gives:
\[
f(0) = f(0) \quad \text{trivial identity}.
\]
For specific \( y \) values like \( y = n \in \mathbb{Z} \), if \( 1 \leq f(n) < 2 \), and considering continuity or piecewise constant functions, one possible solution is that \( f(x) = c \quad \forall x \in \mathbb{R} \), where \( 1 \leq c < 2 \).

### Conclusion

Therefore, the functions \( f: \mathbb{R} \rightarrow \mathbb{R} \) that satisfy the given functional equation are:
\[
\boxed{f(x) = 0 \quad \forall x \in \mathbb{R}, \quad f(x) = c \quad \forall x \in \mathbb{R}, \text{ where } 1 \leq c < 2}.
\]
-/
