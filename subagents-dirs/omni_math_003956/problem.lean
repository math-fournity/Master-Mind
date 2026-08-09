/-- AoPS omni_math Problem (id=003956, source=, difficulty= )
    Informal statement: Consider those functions $ f: \mathbb{N} \mapsto \mathbb{N}$ which satisfy the condition
\[ f(m \plus{} n) \geq f(m) \plus{} f(f(n)) \minus{} 1
\]
for all $ m,n \in \mathbb{N}.$ Find all possible values of $ f(2007).$

[i]Author: Nikolai Nikolov, Bulgaria[/i]
    Answer: 1, 2, \ldots, 2008
    Solution: 

To solve the problem, we need to determine all possible values of \( f(2007) \) for functions \( f: \mathbb{N} \to \mathbb{N} \) that satisfy the given functional inequality:
\[ 
f(m + n) \geq f(m) + f(f(n)) - 1 
\]
for all \( m, n \in \mathbb{N} \).

Firstly, let's consider the functional inequality with the specific choice of \( m = 0 \):
\[ 
f(n) = f(0 + n) \geq f(0) + f(f(n)) - 1.
\]
Rearranging this gives:
\[
f(f(n)) \leq f(n) - f(0) + 1.
\]

Next, consider the case \( n = 0 \):
\[ 
f(m) = f(m + 0) \geq f(m) + f(f(0)) - 1.
\]
This simplifies to:
\[
1 \geq f(f(0)),
\]
which implies \( f(f(0)) = 1 \) since \( f : \mathbb{N} \to \mathbb{N} \).

Now, let's analyze the implications for specific values of \( n \). If we take \( f(0) \) as some constant value \( c \), we have \( f(f(0)) = f(c) \), and since \( f(f(0)) = 1 \), we conclude \( f(c) = 1 \).

Now we explore what this means for the values of \( f(2007) \). Notice from the bound \( f(f(n)) \leq f(n) - f(0) + 1 \), \( f(f(n)) = 1 \) implies that, in particular:
\[
1 \leq f(n) - c + 1 \Rightarrow f(n) \geq c \]
for all \( n \).

Now, let's reconsider the inequality condition with a general approach:
\[ 
f(m + n) \geq f(m) + f(f(n)) - 1.
\]
Using the information \( f(f(0)) = 1 \), it follows that \( f \) is non-decreasing or satisfies certain specific behavior constraining growth. Given \( n \), consider applying such functional analyses like induction or growth limit to determine specific behaviors at desired points (such as \( f(2007) \)).

Given the inequality allows each value \( f(n) \) to vary between solutions from \( 1 \) to \( n+1 \), a simple constructive verification allows us to ascertain that:
\[ 
f(f(n)) = 1 \quad \Rightarrow \quad f(n) \text{ is incrementally } \leq (n+1).
\]

As the pattern suggests across \( n = 0, 1, 2, 3, \ldots, \) accept the logical equivalence along with inequality rules, \( f(2007) \) fits:
\[ 
\text{Range: } (1, 2, \ldots, 2008).
\]

Hence, the set of all possible values of \( f(2007) \) is:
\[ 
\boxed{1, 2, \ldots, 2008}.
\]

-/
