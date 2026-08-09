/-- AoPS omni_math Problem (id=000032, source=, difficulty= )
    Informal statement: Let $C=\{ z \in \mathbb{C} : |z|=1 \}$ be the unit circle on the complex plane. Let $z_1, z_2, \ldots, z_{240} \in C$ (not necessarily different) be $240$ complex numbers, satisfying the following two conditions:
(1) For any open arc $\Gamma$ of length $\pi$ on $C$, there are at most $200$ of $j ~(1 \le j \le 240)$ such that $z_j \in \Gamma$.
(2) For any open arc $\gamma$ of length $\pi/3$ on $C$, there are at most $120$ of  $j ~(1 \le j \le 240)$ such that $z_j \in \gamma$.

Find the maximum of $|z_1+z_2+\ldots+z_{240}|$.
    Answer: 80 + 40\sqrt{3}
    Solution: 

Let \( C = \{ z \in \mathbb{C} : |z| = 1 \} \) be the unit circle on the complex plane. Let \( z_1, z_2, \ldots, z_{240} \in C \) (not necessarily different) be 240 complex numbers satisfying the following two conditions:
1. For any open arc \(\Gamma\) of length \(\pi\) on \(C\), there are at most 200 of \( j ~(1 \le j \le 240) \) such that \( z_j \in \Gamma \).
2. For any open arc \(\gamma\) of length \(\pi/3\) on \(C\), there are at most 120 of \( j ~(1 \le j \le 240) \) such that \( z_j \in \gamma \).

We aim to find the maximum of \( |z_1 + z_2 + \ldots + z_{240}| \).

To solve this, we consider the following setup:
Let the 240 complex numbers be \( z_k = e^{i \theta_k} \) for \( k = 1, 2, \ldots, 240 \), where \( 0 \leq \theta_1 \leq \theta_2 \leq \cdots \leq \theta_{240} < 2\pi \).

We define \( \omega_k = z_k + z_{k+40} + z_{k+80} + z_{k+120} + z_{k+160} + z_{k+200} \) for \( 1 \leq k \leq 40 \). Each \( \omega_k \) sums six complex numbers spaced by \( \frac{2\pi}{6} = \frac{\pi}{3} \) radians apart.

Given the conditions:
1. For any open arc \(\Gamma\) of length \(\pi\) on the unit circle, at most 5 of \( z_i \) (where \( 1 \leq i \leq 6 \)) are on \(\Gamma\).
2. For any open arc \(\gamma\) of length \(\pi/3\) on the unit circle, at most 3 of \( z_i \) (where \( 1 \leq i \leq 6 \)) are on \(\gamma\).

We can bound the magnitude of \( \omega_k \):
\[
|\omega_k| = |z_k + z_{k+40} + z_{k+80} + z_{k+120} + z_{k+160} + z_{k+200}|.
\]

Using the properties of complex numbers on the unit circle and the given conditions, we find:
\[
|\omega_k| \leq 2 + \sqrt{3}.
\]

Thus, the sum of all \( z_i \) can be bounded by:
\[
|z_1 + z_2 + \ldots + z_{240}| = \left| \sum_{k=1}^{40} \omega_k \right| \leq 40 \times (2 + \sqrt{3}).
\]

The maximum value is achieved when the configuration of \( z_i \) is such that the sum reaches this bound. One such configuration is:
- \( z_1 = z_2 = \cdots = z_{40} = i \),
- \( z_{41} = z_{42} = \cdots = z_{80} = -i \),
- \( z_{81} = z_{82} = \cdots = z_{120} = \frac{\sqrt{3}}{2} + \frac{1}{2}i \),
- \( z_{121} = z_{122} = \cdots = z_{160} = \frac{\sqrt{3}}{2} - \frac{1}{2}i \),
- \( z_{161} = z_{162} = \cdots = z_{240} = 1 \).

In this configuration, we have:
\[
|z_1 + z_2 + \ldots + z_{240}| = 80 + 40\sqrt{3}.
\]

Therefore, the maximum of \( |z_1 + z_2 + \ldots + z_{240}| \) is:
\[
\boxed{80 + 40\sqrt{3}}.
\]
-/
