/-- AoPS omni_math Problem (id=3242, source=putnam, difficulty=9.0 )
    Informal statement: Let $n$ be an even positive integer. Let $p$ be a monic, real polynomial of degree $2n$; that is to say, $p(x) = x^{2n} + a_{2n-1} x^{2n-1} + \cdots + a_1 x + a_0$ for some real coefficients $a_0, \dots, a_{2n-1}$. Suppose that $p(1/k) = k^2$ for all integers $k$ such that $1 \leq |k| \leq n$. Find all other real numbers $x$ for which $p(1/x) = x^2$.
    Answer: \pm 1/n!
    Solution: The only other real numbers with this property are $\pm 1/n!$. (Note that these are indeed \emph{other} values than $\pm 1, \dots, \pm n$ because $n>1$.) Define the polynomial $q(x) = x^{2n+2}-x^{2n}p(1/x) = x^{2n+2}-(a_0x^{2n}+\cdots+a_{2n-1}x+1)$. The statement that $p(1/x)=x^2$ is equivalent (for $x\neq 0$) to the statement that $x$ is a root of $q(x)$. Thus we know that $\pm 1,\pm 2,\ldots,\pm n$ are roots of $q(x)$, and we can write \[ q(x) = (x^2+ax+b)(x^2-1)(x^2-4)\cdots (x^2-n^2) \] for 
-/
