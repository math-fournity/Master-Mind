/-- AoPS omni_math Problem (id=004127, source=, difficulty= )
    Informal statement: Let $n\ge 3$ be a fixed integer. There are $m\ge n+1$ beads on a circular necklace. You wish to paint the beads using $n$ colors, such that among any $n+1$ consecutive beads every color appears at least once. Find the largest value of $m$ for which this task is $\emph{not}$ possible.

[i]Carl Schildkraut, USA[/i]
    Answer: $\boxed{n^2-n-1}$
    Solution: 

Let \( n \geq 3 \) be a fixed integer. We need to find the largest number \( m \) for which it is not possible to paint \( m \) beads on a circular necklace using \( n \) colors such that each color appears at least once among any \( n+1 \) consecutive beads.

### Analysis

1. **Understanding the Problem:**

   Given \( m \) beads and \( n \) colors, the condition is that in any segment of \( n+1 \) consecutive beads, each of the \( n \) colors must appear at least once.
   
   We are seeking the largest \( m \) such that this condition cannot be satisfied.

2. **Pattern Exploration:**

   If we imagine arranging \( n+1 \) beads consecutively in a valid way, each subset of \( n+1 \) beads must exhaust all \( n \) colors at least once. 
   
   Suppose you try to construct such a sequence that wraps around the circle of beads, large enough that fulfilling the requirement cannot be guaranteed.

3. **Conceiving a Counterexample:**

   Assume \( m = n^2 - n - 1 \). We will denote the beads as positions \( 0, 1, 2, \ldots, n^2 - n - 2 \). 

   To paint the beads, first consider a hypothetical repeating cycle of length \( n \) (making use of all colors), repeating around until it fills \( n^2 - n - 1 \) positions exactly.

   \[
   \text{Cycle}: (C_1, C_2, \ldots, C_n)
   \]

   Now we note that, because the number of beads minus the number of colors \( n+1 \) (when considering one additional cycle bead space) does not sufficiently allow for coverage by distinct cycles, we are always missing coverage at \( n^2 - n - 1 + n = n^2 - 1 \) which is one more bead when closed in a necklace fashion. 

4. **Verification by Overshadowing Requirement:**

   Let’s test if it is actually possible with \( m = n^2 - n \):

   If \( m = n^2-n \), consider that any setup you make inherently leaves a gap at some point due to the principle of covering \( n+1 \) beads (by symmetry and counting argument, this is best described as creating an incomplete residue class partition under modulus \( n \), yielding a surplus **one less** than completing the cycle when \( n+1 \) is distributed).

### Conclusion

Through combinatorics and consequences of \( m = n^2 - n - 1 \) as number of beads, such a coloring following the constraints cannot exist, therefore the largest such value of \( m \) for which the task is not possible is:

\[
\boxed{n^2-n-1}
\]

Thus, placing \( n^2 - n - 1 \) beads in circular fashion does not allow any \( n+1 \) to have all colors without duplicating elements mid-cycle, lacking exhaustiveness.
-/
