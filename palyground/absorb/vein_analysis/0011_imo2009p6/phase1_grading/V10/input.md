**题目**：

Let a₁, a₂, ..., aₙ be distinct positive integers and let M be a set of n-1 positive integers not containing s = a₁ + a₂ + ... + aₙ. A grasshopper is to jump along the real axis, starting at the point 0 and making n jumps to the right with lengths a₁, a₂, ..., aₙ in some order. Prove that the order can be chosen in such a way that the grasshopper never lands on any point in M.

**解答**：

WLOG sort a₁ < a₂ < ... < aₙ (by applying a permutation). Let x = a₁ + ... + a_{n-1} (sum of all but the largest element). We proceed by strong induction on n.

Three cases based on the position of M's elements relative to x:

Case 1 (x ∈ M and ∃ y ∈ M with y > x): Then n ≥ 3. Among the n-1 small elements, define 'bad' index i if x - aᵢ ∈ M or s - aᵢ ∈ M. The map from bad indices to M\{x} is injective (x - aᵢ maps to M\{x} since x ∈ M and aᵢ > 0; s - aᵢ > x so maps to M∩(x,∞)). Since |M\{x}| = n-2, there are at most n-2 bad indices among n-1 total, so at least one good index r exists with x - aᵣ ∉ M and s - aᵣ ∉ M. Let t = x - aᵣ, M' = M ∩ (-∞, t]. Then |M'| ≤ n-3 (since both x and y are excluded from M'). Apply induction to the n-2 remaining elements (excluding aᵣ and aₙ) with M', getting permutation p'. Construct the full permutation: place p' first, then aᵣ, then aₙ (with a swap to put aₙ second-to-last). All prefix sums before aᵣ are ≤ t and avoid M'; the sum up to aᵣ is s - aₙ = s - aᵣ - (sum of rest) which avoids M by choice of r; the final sum is s ∉ M.

Case 2 (x ∉ M and ∃ y ∈ M with y > x): Then |M ∩ (-∞, x]| ≤ n-2. Let M' = M ∩ (-∞, x]. Apply induction to a₁,...,a_{n-1} with M' (sum = x ∉ M'). If M' is empty, use identity. Otherwise get permutation p', extend by placing aₙ last. All prefix sums of first n-1 jumps are ≤ x and avoid M'; the final sum is s ∉ M.

Case 3 (all m ∈ M satisfy m ≤ x): Let z = max(M), M' = M\{z}. Apply induction to a₁,...,a_{n-1} with M' (|M'| = n-2). Get permutation p'. If some prefix sum of p' equals z at position k, swap position k with the last position: place aₙ at position k (jumping over z since aₙ > a_{p'(k)}), and place a_{p'(k)} last. If no prefix sum equals z, p' already avoids all of M (since M = M' ∪ {z} and z is never hit).

The general case (unsorted a) is reduced to the sorted case by composing with the sorting permutation.