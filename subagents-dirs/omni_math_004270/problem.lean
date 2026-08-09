/-- AoPS omni_math Problem (id=004270, source=, difficulty= )
    Informal statement: Let $ n > 1$ be an integer. Find all sequences $ a_1, a_2, \ldots a_{n^2 \plus{} n}$ satisfying the following conditions:
\[ \text{ (a) } a_i \in \left\{0,1\right\} \text{ for all } 1 \leq i \leq n^2 \plus{} n;
\]

\[ \text{ (b) } a_{i \plus{} 1} \plus{} a_{i \plus{} 2} \plus{} \ldots \plus{} a_{i \plus{} n} < a_{i \plus{} n \plus{} 1} \plus{} a_{i \plus{} n \plus{} 2} \plus{} \ldots \plus{} a_{i \plus{} 2n} \text{ for all } 0 \leq i \leq n^2 \minus{} n.
\]
[i]Author: Dusan Dukic, Serbia[/i]
    Answer: \[
a_{u+vn} = 
\begin{cases} 
0, & u+v \le n, \\ 
1, & u+v \ge n+1 
\end{cases} 
\quad \text{for all } 1 \le u \le n \text{ and } 0 \le v \le n.
\]
\[
\text{The terms can be arranged into blocks of length } n \text{ as}
\]
\[
\underbrace{(0 \cdots 0)}_{n} \underbrace{(0 \cdots 0 \ 1)}_{n-1} \underbrace{(0 \cdots 0 \ 1 \ 1)}_{n-2} \cdots \underbrace{(0 \cdots 0 \ 1 \cdots 1)}_{n-v} \underbrace{(0 \ 1 \cdots 1)}_{v} \cdots \underbrace{(0 \ 1 \cdots 1)}_{n-1} \underbrace{(1 \cdots 1)}_{n}.
\]
    Solution: 

To construct sequences that satisfy these conditions, let's explore the structure of sequences in terms of segments or blocks of length \( n \):

For a sequence \( a_1, a_2, \ldots, a_{n^2 + n} \), consider representing it as composed of blocks of length \( n \):
- Sequence indices are split such that each \( a_{u+vn} \) corresponds to a position in the grid where \( 1 \le u \le n \) and \( 0 \le v \le n \).

Given these indices, analyze the sequence condition \( (b) \), where parts of the sequence need to obey the inequality regarding the sum of segments of length \( n \):
- Consider two consecutive segments of the sequence from elements \( i+1 \) to \( i+2n \). The sum of the first \( n \) elements in a segment (i.e., \( a_{i+1} + \ldots + a_{i+n} \)) must be less than the sum of the next \( n \) elements (i.e., \( a_{i+n+1} + \ldots + a_{i+2n} \)).

### Construction of Sequence

One valid sequence configuration is as follows: 
1. For each \( u+v \leq n \), set \( a_{u+vn} = 0 \),
2. For each \( u+v \geq n+1 \), set \( a_{u+vn} = 1 \).

These result in arranging the sequence into blocks:
- The first block contains only zeros: \( (0, 0, \ldots, 0) \) of length \( n \).
- The second block shifts one zero to the left, and so on, increasing the number of 1's till the block is entirely filled with 1's at the last possible block, resulting in:
  - \( (0, \ldots, 0, 1), (0, \ldots, 0, 1, 1), \ldots, (1, 1, \ldots, 1) \).

The sequence's layout can be seen as:
\[
\underbrace{(0 \cdots 0)}_{n} \underbrace{(0 \cdots 0 \ 1)}_{n-1} \underbrace{(0 \cdots 0 \ 1 \ 1)}_{n-2} \cdots \underbrace{(0 \cdots 0 \ 1 \cdots 1)}_{n-v} \underbrace{(0 \ 1 \cdots 1)}_{v} \cdots \underbrace{(0 \ 1 \cdots 1)}_{n-1} \underbrace{(1 \cdots 1)}_{n}.
\]

This block arrangement ensures the given inequality condition (b) is satisfied for all valid indices, maintaining the property that the sum of any segment of zeros followed by fewer number of ones will always be less than the adjacent segment with more ones, as implied by the inequality specified.

### Conclusion

Thus, the sequences satisfying the given conditions can be explicitly formulated as follows based on the above configuration:
\[
a_{u+vn} = 
\begin{cases} 
0, & u+v \le n, \\ 
1, & u+v \ge n+1 
\end{cases} 
\text{ for all } 1 \le u \le n \text{ and } 0 \le v \le n.
\]

This completes the construction and solution for the given problem. 
\[
\boxed{\text{Sequence as described is valid for given conditions.}}
\]
-/
