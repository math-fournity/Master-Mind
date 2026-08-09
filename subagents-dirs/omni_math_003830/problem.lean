/-- AoPS omni_math Problem (id=3830, source=imo, difficulty=9.0 )
    Informal statement: A [i]site[/i] is any point $(x, y)$ in the plane such that $x$ and $y$ are both positive integers less than or equal to 20.

Initially, each of the 400 sites is unoccupied. Amy and Ben take turns placing stones with Amy going first. On her turn, Amy places a new red stone on an unoccupied site such that the distance between any two sites occupied by red stones is not equal to $\sqrt{5}$. On his turn, Ben places a new blue stone on any unoccupied site. (A site occupied by a blue stone is allowed to be at any distance from any other occupied site.) They stop as soon as a player cannot place a stone.

Find the greatest $K$ such that Amy can ensure that she places at least $K$ red stones, no matter how Ben places his blue stones.

[i]
    Answer: 100
    Solution: 
Let us consider the problem where Amy and Ben take turns placing stones on a 20x20 grid consisting of sites \((x, y)\) where \(x\) and \(y\) are integers between 1 and 20 inclusive. Amy's condition for placing a red stone is that the distance between any two red stones is not equal to \(\sqrt{5}\). This occurs specifically when the coordinates of two stones differ by 2 in one coordinate and 1 in the other, which are equivalent to the vector differences \((\pm 2, \pm 1)\) or \((\pm 1, \pm 2)\).

-/
