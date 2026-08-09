/-- AoPS omni_math Problem (id=3872, source=imo_shortlist, difficulty=9.0 )
    Informal statement: Players $A$ and $B$ play a game on a blackboard that initially contains 2020 copies of the number 1 . In every round, player $A$ erases two numbers $x$ and $y$ from the blackboard, and then player $B$ writes one of the numbers $x+y$ and $|x-y|$ on the blackboard. The game terminates as soon as, at the end of some round, one of the following holds:
[list]
[*] $(1)$ one of the numbers on the blackboard is larger than the sum of all other numbers;
[*] $(2)$ there are only zeros on the blackboard.
[/list]
Player $B$ must then give as many cookies to player $A$ as there are numbers on the blackboard. Player $A$ wants to get as many cookies as possible, whereas player $B$ wants to give as few as possible. Determine the number of cookies that $A$ receives if both players play optimally.
    Answer: 7
    Solution: 
To solve this problem, we need to carefully analyze the game dynamics and the optimal strategies for both players, \( A \) and \( B \).

Initially, the blackboard contains 2020 copies of the number 1. The players' moves involve manipulating these numbers under certain rules:

1. Player \( A \) erases two numbers, \( x \) and \( y \).
2. Player \( B \) then writes either \( x+y \) or \( |x-y| \) back on the blackboard.

The game ends under two conditions:
- One number becomes larger than the sum
-/
