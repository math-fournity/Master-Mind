/-- AoPS omni_math Problem (id=003993, source=, difficulty= )
    Informal statement: Determine the greatest positive integer $k$ that satisfies the following property: The set of positive integers can be partitioned into $k$ subsets $A_1, A_2, \ldots, A_k$ such that for all integers $n \geq 15$ and all $i \in \{1, 2, \ldots, k\}$ there exist two distinct elements of $A_i$ whose sum is $n.$

[i]
    Answer: 3
    Solution: 

To find the greatest positive integer \( k \) that satisfies the partition property, we must ensure that the positive integers can be divided into \( k \) subsets \( A_1, A_2, \ldots, A_k \) such that for all integers \( n \geq 15 \) and for each \( i \in \{1, 2, \ldots, k\} \), there are two distinct elements in \( A_i \) whose sum is \( n \).

Let's analyze the problem:

1. **Understanding the Partition Requirement**:
   - Each subset \( A_i \) should contain two distinct elements whose sum equals \( n \) for every \( n \geq 15 \).
   - This requires diversity in each subset so that various sums \( n \) can be obtained by choosing two elements from any subset.

2. **Finding Constraints on \( k \)**:
   - If \( k \) is too large, it might not be possible to achieve the necessary sums with the limited numbers available in smaller subsets.
   - If the number of subsets \( k \) is small enough, each subset can incorporate a sufficient range of numbers to meet the summing requirement.

3. **Demonstrating a Working Value of \( k \)**:
   - For \( k = 3 \), consider three subsets: 
     \[
     A_1 = \{ 1, 4, 7, 10, \ldots \} = \{ 1 + 3t \mid t \in \mathbb{Z}^+ \},
     \]
     \[
     A_2 = \{ 2, 5, 8, 11, \ldots \} = \{ 2 + 3t \mid t \in \mathbb{Z}^+ \},
     \]
     \[
     A_3 = \{ 3, 6, 9, 12, \ldots \} = \{ 3 + 3t \mid t \in \mathbb{Z}^+ \}.
     \]
   - These sets distribute the positive integers cyclically into three groups based on their remainder modulo 3.
   - For any integer \( n \geq 15 \), it can be verified that there exist two numbers in each subset whose sum equals \( n \). For instance:
     - Choose distinct integers \( a = 3m + r \) and \( b = 3n + r \) with \( r = 1, 2, 3 \) for subsets \( A_1, A_2, \) and \( A_3 \), respectively.

4. **Proving \( k > 3 \) Does Not Work**:
   - Suppose \( k = 4 \). Then we would need to find a regular way to partition the integers into four subsets while maintaining the sum property for each subset.
   - However, constructing such a distribution generally fails for larger \( k \) because the need to utilize higher integers to achieve every possible sum \( n \geq 15 \) becomes impractical.

Therefore, the largest value of \( k \) that permits the construction of such a partition is:

\[
\boxed{3}
\]
This solution satisfies the conditions of the problem, ensuring that every required sum can be found by adding two distinct elements from each subset of the partition.
-/
