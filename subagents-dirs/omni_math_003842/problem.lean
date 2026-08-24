/-- AoPS omni_math Problem (id=003842, source=, difficulty= )
    Informal statement: Let $n$ be a positive integer. A sequence of $n$ positive integers (not necessarily distinct) is called [b]full[/b] if it satisfies the following condition: for each positive integer $k\geq2$, if the number $k$ appears in the sequence then so does the number $k-1$, and moreover the first occurrence of $k-1$ comes before the last occurrence of $k$. For each $n$, how many full sequences are there ?
    Answer: n!
    Solution: 

To solve this problem, we need to determine how many sequences of length \( n \) consisting of positive integers are considered "full" according to the defined condition. The condition implies a hierarchical appearance of integers in the sequence, such that if an integer \( k \) appears, then \( k-1 \) must also appear before the last occurrence of \( k \).

We can approach the problem inductively:

1. **Base Case:** For \( n = 1 \), the only sequence is \([1]\), which trivially satisfies the condition as there are no integers \( k \geq 2 \).

2. **Inductive Step:** Assume that for some \( n \), all sequences of positive integers of length \( n \) are full. Now consider sequences of length \( n+1 \).

   To form a full sequence of length \( n+1 \), consider placing the number \( n+1 \) in the sequence. According to the condition, for any occurrence of \( n+1 \), an \( n \) must appear before the last occurrence of \( n+1 \). The rest of the sequence before placing \( n+1 \) can be any full sequence of length \( n \).

   We can insert \( n+1 \) at any position in the sequence of length \( n \), resulting in \( (n+1)! \) permutations of sequences.

Thus, each choice of ordering for the integers from \( 1 \) through \( n \) is independent in a full sequence, therefore we have \( n! \) full sequences for any positive integer \( n \).

Hence, the number of full sequences of length \( n \) is:
\[
\boxed{n!}
\]
\
-/
