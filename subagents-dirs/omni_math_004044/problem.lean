/-- AoPS omni_math Problem (id=004044, source=, difficulty= )
    Informal statement: There are 60 empty boxes $B_1,\ldots,B_{60}$ in a row on a table and an unlimited supply of pebbles. Given a positive integer $n$, Alice and Bob play the following game.
In the first round, Alice takes $n$ pebbles and distributes them into the 60 boxes as she wishes. Each subsequent round consists of two steps:
(a) Bob chooses an integer $k$ with $1\leq k\leq 59$ and splits the boxes into the two groups $B_1,\ldots,B_k$ and $B_{k+1},\ldots,B_{60}$.
(b) Alice picks one of these two groups, adds one pebble to each box in that group, and removes one pebble from each box in the other group.
Bob wins if, at the end of any round, some box contains no pebbles. Find the smallest $n$ such that Alice can prevent Bob from winning.

[i]Czech Republic[/i]
    Answer: 960
    Solution: 
To solve this problem, we need to find the smallest integer \( n \) such that Alice can always prevent Bob from winning regardless of how the game progresses. The setup is as follows:

1. Alice and Bob are playing a game with 60 boxes, \( B_1, B_2, \ldots, B_{60} \), and an unlimited supply of pebbles.
2. In the first round, Alice places \( n \) pebbles among the 60 boxes.
3. In each round, Bob chooses an integer \( k \) (where \( 1 \leq k \leq 59 \)) and splits the boxes into two groups: \( B_1, \ldots, B_k \) and \( B_{k+1}, \ldots, B_{60} \).
4. Alice then chooses one of the two groups and adds one pebble to each box in that group while removing one pebble from each box in the other group.
5. Bob wins if, at any point during the game, any box contains no pebbles.

**Objective:** Find the minimum \( n \) such that Alice can always make sure every box contains at least one pebble throughout the game.

### Analysis
- Each round lets Alice adjust the distribution of pebbles to ensure no box ever falls to zero pebbles.
- Since Bob can split the boxes in various ways, Alice must be able to counter any strategy Bob uses to reduce any box's pebbles to zero.

### Key Insights
- Consider the worst-case scenario in which all of Bob's splits aim to minimize the number of pebbles in the more populated group.
- To ensure success, Alice needs enough initial pebbles in each box such that the difference in pebble distribution between any two boxes can always be adjusted to maintain a non-zero amount of pebbles.

### Solution Strategy
To prevent any box from ever reaching zero pebbles, it is required that Alice starts with a sufficient amount of pebbles such that no matter how Bob splits the boxes, the difference in pebble count between the fullest and emptiest box can be maintained above zero. An analysis of this logistic scenario yields the formula:

\[ 
n = 16 \times 60 = 960 
\]

This formula comes from the requirement that the potential difference, at any point, after any number of rounds, of pebbles between the fullest and emptiest box can always be moderated by Alice's actions, ensuring all boxes never reach zero pebbles. Calculations show that this constraint is sustainable starting with 960 pebbles.

### Conclusion
Thus, the smallest number of pebbles \( n \) that allows Alice to always keep at least one pebble in every box and prevent Bob from winning is:
\[
\boxed{960}
\]
-/
