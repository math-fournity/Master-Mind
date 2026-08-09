/-- AoPS omni_math Problem (id=3825, source=imo_shortlist, difficulty=9.0 )
    Informal statement: The leader of an IMO team chooses positive integers $n$ and $k$ with $n > k$, and announces them to the deputy leader and a contestant. The leader then secretly tells the deputy leader an $n$-digit binary string, and the deputy leader writes down all $n$-digit binary strings which differ from the leader’s in exactly $k$ positions. (For example, if $n = 3$ and $k = 1$, and if the leader chooses $101$, the deputy leader would write down $001, 111$ and $100$.) The contestant is allowed to look at the strings written by the deputy leader and guess the leader’s string. What is the minimum number of guesses (in terms of $n$ and $k$) needed to guarantee the correct answer?
    Answer: 2 \text{ if } n = 2k, \text{ and } 1 \text{ otherwise}
    Solution: 
To solve this problem, we need to determine the minimum number of guesses a contestant needs to guarantee correctly identifying the leader’s \( n \)-digit binary string, given the constraints on how the strings can differ.

### Explanation

1. **Binary Strings and Hamming Distance**: 
   The problem involves binary strings of length \( n \) and the concept of Hamming distance, which measures the number of positions at which two strings differ. Specifically, the deputy leader lists all binary st
-/
