/-- AoPS omni_math Problem (id=3243, source=putnam, difficulty=9.0 )
    Informal statement: Shanille O'Keal shoots free throws on a basketball court. She hits the first and misses the second, and thereafter the probability that she hits the next shot is equal to the proportion of shots she has hit so far. What is the probability she hits exactly 50 of her first 100 shots?
    Answer: \(\frac{1}{99}\)
    Solution: The probability is \(1/99\). In fact, we show by induction on \(n\) that after \(n\) shots, the probability of having made any number of shots from \(1\) to \(n-1\) is equal to \(1/(n-1)\). This is evident for \(n=2\). Given the result for \(n\), we see that the probability of making \(i\) shots after \(n+1\) attempts is \[\frac{i-1}{n} \frac{1}{n-1} + \left( 1 - \frac{i}{n} \right) \frac{1}{n-1} = \frac{(i-1) + (n-i)}{n(n-1)} = \frac{1}{n},\] as claimed.
-/
