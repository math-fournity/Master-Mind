/-- AoPS omni_math Problem (id=003969, source=, difficulty= )
    Informal statement: Find all surjective functions $ f: \mathbb{N} \to \mathbb{N}$ such that for every $ m,n \in \mathbb{N}$ and every prime $ p,$ the number $ f(m + n)$ is divisible by $ p$ if and only if $ f(m) + f(n)$ is divisible by $ p$.

[i]Author: Mohsen Jamaali and Nima Ahmadi Pour Anari, Iran[/i]
    Answer: f(n) = n
    Solution: 

We are tasked with finding all surjective functions \( f: \mathbb{N} \to \mathbb{N} \) that satisfy the condition: for every \( m, n \in \mathbb{N} \) and every prime \( p \), the number \( f(m+n) \) is divisible by \( p \) if and only if \( f(m) + f(n) \) is divisible by \( p \).

To solve this, we consider the given condition: 

\[
p \mid f(m+n) \iff p \mid (f(m) + f(n)).
\]

Let's explore the implications of this condition:

1. **Injectivity:**  
   Assume for contradiction that \( f(a) = f(b) \) for \( a \neq b \). Then, consider \( m = a \) and \( n = 0 \):
   \[
   f(a+0) \equiv f(b+0)  \equiv f(a) + f(0) = f(b) + f(0).
   \]
   Since \( f \) is assumed to be surjective, it must be injective as well because if \( f(a) = f(b) \), any number \( c \) in the codomain cannot have two different pre-images, which would violate surjectivity.

2. **Additivity and Linear Form:**  
   For simplicity, consider \( m = n = 1 \):
   \[
   f(2) \equiv 2f(1).
   \]
   Now generalize this idea. Suppose by induction that \( f(k) = k \cdot f(1) \) holds for some \( k \). Then, for \( m = k \) and \( n = 1 \):
   \[
   f(k+1) \equiv f(k) + f(1) = kf(1) + f(1) = (k+1)f(1),
   \]
   thereby maintaining the linearity \( f(n) = nf(1) \).

3. **Scaling:**  
   Consider \( a = 1 \), then \( f(1+1)=2f(1) \) should hold. Scaling continues to suggest that \( f(n) = nf(1) \) and let's assume \( f(1) = 1 \) for surjectivity \( f(n) = n \).

4. **Testing the Condition:**  
   Given \( f(n) = n \), check the condition in both directions:
   
   - If \( n+m = kp \), then \( f(n+m) = n + m \equiv 0 \pmod{p} \).
   - If \( f(n) + f(m) = n + m = kp \), similarly \( f(n+m) = kp \equiv 0 \pmod{p} \).

The only function which satisfies all constraints and maintain surjectivity is \( f(n) = n \).

Thus, the function that satisfies the given condition is:
\[
\boxed{f(n) = n}.
\]

-/
