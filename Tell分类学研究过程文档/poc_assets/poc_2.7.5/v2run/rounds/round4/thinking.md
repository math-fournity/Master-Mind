Let me start by reading the analysis notes file.The file doesn't exist at that path. Let me check the working directory.The 分析笔记.md is not in the working directory. Let me look at the directory structure more carefully. There's `acp_out_r4` and `rounds` directories, and `oc_traj.py`.The 分析笔记.md is in rounds/round3/. The prompt said it's in the current working directory, but it's actually in rounds/round3/分析笔记.md. Let me read it.Now I understand the state. Let me summarize:

**Problem**: Find all positive integer triples (a,b,c) such that ab−c, bc−a, ca−b are all powers of 2.

**Conjectured solution set**: (2,2,2), (2,2,3), (2,6,11) and all permutations.

**Already closed**:
1. Two-equal cases: only (2,2,2) and (2,2,3).
2. All c-even patterns dead.
3. (O,E,O) dead.
4. Remaining: (E,E,O) solved = (2,6,11); and (O,O,O) — the only open case.

**Gaps**:
- Gap 0: Run brute force search to verify solution set.
- Gap 1: Kill (O,O,O).
- Gap 2: Write up proof.md.

My job as round 4 solver:
1. First run the brute force search (gap 0).
2. Kill (O,O,O) (gap 1).
3. Write proof.md with boxed answer.

Let me start by setting up a todo list and then doing the brute force search.

Let me think about how to kill (O,O,O).

Setup: WLOG a ≤ b ≤ c, all odd, ≥ 2 (all odd means ≥ 3). x < z < y strictly (since all distinct; if two equal we've solved). We have:

- ab − c = 2^x
- bc − a = 2^y
- ca − b = 2^z

with x ≤ z ≤ y and in the all-distinct case x < z < y.

Key identities:
(1) (b−a)(c+1) = 2^y − 2^z
(2) (c−b)(a+1) = 2^z − 2^x
(3) (c−a)(b+1) = 2^y − 2^x

With A = v₂(a+1), B = v₂(b+1), C = v₂(c+1):
- v₂(b−a) = z − C... wait let me recheck. 

From (1): 2^y − 2^z = 2^z(2^(y−z) − 1). Since y > z, 2^(y−z) − 1 is odd, so v₂(LHS) = z. Thus v₂((b−a)(c+1)) = z, i.e., v₂(b−a) + C = z, so v₂(b−a) = z − C.

From (2): 2^z − 2^x = 2^x(2^(z−x) − 1), odd part odd, v₂ = x. So v₂(c−b) + A = x, i.e., v₂(c−b) = x − A.

From (3): v₂(c−a) + B = x, i.e., v₂(c−a) = x − B.

In (O,O,O): a,b,c odd ⟹ b−a, c−b, c−a are even. So v₂(b−a) ≥ 1 ⟹ z ≥ C+1, v₂(c−b) ≥ 1 ⟹ x ≥ A+1, v₂(c−a) ≥ 1 ⟹ x ≥ B+1. Hmm wait, the notes say "x≥max(A,B)≥1, z≥C". Let me redo: b−a even requires z−C ≥ 1? Actually b−a could be even; since a,b odd, b−a is even, so v₂(b−a) ≥ 1, hence z − C ≥ 1, i.e., z ≥ C + 1 > C. Similarly c−b even ⟹ x − A ≥ 1 ⟹ x > A, and x > B.

So x ≥ max(A,B) + 1, z ≥ C + 1.

Hmm wait, actually that's slightly different from what the note says ("z≥C" vs my "z ≥ C+1"). The note says x≥max(A,B)≥1 and z≥C. My computation gives stronger: z > C and x > max(A,B). Fine, either way.

Also parity: ab − c where a,b,c odd: ab odd, minus c odd gives even. OK consistent.

Now the divisibility conditions: from (2), (c−b)(a+1) = 2^x(2^(z−x)−1). Write a+1 = 2^A · a' with a' odd. Then a' | 2^(z−x) − 1 (after dividing out). Similarly (c+1)/2^C | 2^(y−z) − 1 and (b+1)/2^B | 2^(y−x) − 1.

The size chain: bc − a = 2^y and ab − c = 2^x. So 2^(y−x) = (bc − a)/(ab − c). Note bc − a > ab − c iff b(c−a)... wait: bc − a − (ab − c) = b(c−a) + (c − a)·... let me compute: bc − a − ab + c = c(b+1) − a(b+1) = (c−a)(b+1) > 0. Yes matches identity (3).

So T₁ := 2^(y−x) = (bc−a)/(ab−c).

Approach ideas for killing (O,O,O):

Idea A (mod 3 analysis): Powers of 2 mod 3 alternate: 2^k ≡ 1 if k even, 2 ≡ −1 if k odd. For odd a,b,c: consider mod 4 first. ab − c mod 4: depends on residues.

Actually, let's think about mod 8 or mod 4 constraints. If a,b,c odd:
- ab ≡ 1 mod 8 if a ≡ b mod 8 both odd... no: odd squares ≡ 1 mod 8. ab mod 8 ∈ {1,3,5,7}.
- 2^x mod anything: if x ≥ 3, 2^x ≡ 0 mod 8.

Case x ≥ 3: ab ≡ c mod 8, bc ≡ a mod 8, ca ≡ b mod 8. Multiply all three: (abc)² ≡ abc mod 64? Hmm, careful: multiplying congruences mod 8: (ab)(bc)(ca) ≡ abc mod 8, i.e., (abc)² ≡ abc mod 8. Since abc is odd, this says abc ≡ 0 or 1 mod 8, so abc ≡ 1 mod 8.

So if x,y,z ≥ 3, then abc ≡ 1 mod 8. That's possible (e.g. 3·3·3=27≡3 mod 8 no; 3·5·7=105≡1 yes).

Alternatively divide: from ab ≡ c and bc ≡ a mod 8: multiply first by b: ab² ≡ bc ≡ a mod 8 ⟹ a(b²−1) ≡ 0 mod 8, which holds automatically since b² ≡ 1 mod 8. No info.

Hmm. What about using the identities more cleverly?

Idea B (the "x=0 forced" approach — reverse thinking from gap 1 item 4): Show that in the all-distinct case, x = 0 must hold. Then (O,O,O) dies since it needs x ≥ max(A,B)+1 ≥ 2 (A,B ≥ 1 since a,b odd means a+1, b+1 even). Wait, actually in (O,O,O), x > max(A,B) ≥ 1, so x ≥ 2. So proving "all distinct ⟹ x=0" would kill it. But is that provable? In (E,E,O), x=0 came from c−b being odd (parity argument). In (O,O,O) everything is even differences...

Hmm, let me think about the structure differently.

Let me think again about the fundamental equations:
- c = ab − 2^x
- Also ca − b = 2^z ⟹ (ab − 2^x)a − b = 2^z ⟹ a²b − b − a·2^x = 2^z ⟹ b(a² − 1) = 2^z + a·2^x = 2^x(2^(z−x) + a).
- Similarly from bc − a = 2^y: b(ab − 2^x) − a = 2^y ⟹ ab² − a·2^x − a = 2^y ⟹ a(b² − 1) = 2^y + 2^x = 2^x(2^(y−x) + 1).

Oh nice! These are strong exact equations:

(Equation I): b(a² − 1) = 2^x(2^(z−x) + a)
(Equation II): a(b² − 1) = 2^x(2^(y−x) + 1)

Wait let me double check Equation II: bc − a = 2^y with c = ab − 2^x: b(ab − 2^x) − a = ab² − b·2^x − a. So 2^y = ab² − a − 2^x b, i.e., a(b² − 1) = 2^y + 2^x b = 2^x(2^(y−x) + b). Hmm, I made an arithmetic error. Let me redo:

bc − a = 2^y. c = ab − 2^x. So b(ab − 2^x) − a = 2^y ⟹ ab² − 2^x b − a = 2^y ⟹ a(b² − 1) = 2^y + 2^x b = 2^x(2^(y−x) + b).

Similarly ca − b = 2^z: (ab − 2^x)a − b = a²b − 2^x a − b = 2^z ⟹ b(a² − 1) = 2^z + 2^x a = 2^x(2^(z−x) + a). ✓.

And symmetric versions: from ca−b=2^z, solve for c: c = (2^z + b)/a. From bc − a = 2^y: c = (2^y + a)/b.

So we get the beautiful pair:
- a(b² − 1) = 2^x(2^(y−x) + b) ... (II)
- b(a² − 1) = 2^x(2^(z−x) + a) ... (I)

In (O,O,O): a, b odd ⟹ a² − 1 ≡ (a−1)(a+1), divisible by 8. So LHS of (I): b(a²−1) has v₂ ≥ 3. RHS: 2^x · (odd + odd) = 2^x · even. Hmm, 2^(z−x) + a: z−x ≥ 1 (since x<z), so 2^(z−x) even, a odd, sum odd! So RHS has v₂ exactly x. Therefore **v₂(b(a²−1)) = x**, i.e., **x = v₂(a²−1)** (since b odd).

Similarly in (II): 2^(y−x) + b is even + odd = odd, so **v₂(a(b²−1)) = x**, i.e., **x = v₂(b²−1)**.

Wow, this is very clean. In (O,O,O):
- x = v₂(a² − 1) = v₂(b² − 1).

For odd n, v₂(n² − 1) = v₂(n−1) + v₂(n+1). And v₂(n−1) + v₂(n+1) = 1 + 2·[something]... Known fact: for odd n, one of n−1, n+1 is divisible by 4 and the other only by 2. So v₂(n²−1) = v₂(divisible-by-4 one) + 1.

So x = v₂(a²−1) means: x = v₂(a−1) + v₂(a+1). And recall from earlier: v₂(c−a) = x − B where B = v₂(b+1), and v₂(c−b) = x − A.

Hmm interesting. Now also we can derive similar equations eliminating other variables:

From ca − b = 2^z and bc − a = 2^y: c(ba...) hmm. Let me do: subtract? Actually let me eliminate b: from ab − c = 2^x ⟹ b = (2^x + c)/a. Plug into bc − a = 2^y: c(2^x+c)/a − a = 2^y ⟹ c·2^x + c² − a² = 2^y a ⟹ c² − a² + 2^x c = 2^y a. Hmm not as clean.

Better: use pairs symmetric in structure. General principle: substituting c = ab − 2^x into the other two gives (I) and (II). Substituting b = (2^z + a)/c into others... Let me instead directly write all three:

From each equation solve for the third variable:
- c = ab − 2^x
- a = bc − 2^y... no wait, a = bc − 2^y? bc − a = 2^y ⟹ a = bc − 2^y. 
- b = ca − 2^z.

Substituting b = ca − 2^z into ab − c = 2^x: a(ca − 2^z) − c = 2^x ⟹ a²c − c − a·2^z = 2^x ⟹ c(a² − 1) = 2^x + 2^z a = 2^x(1 + 2^(z−x) a).
Substituting into bc − a: (ca − 2^z)c − a = ac² − 2^z c − a = 2^y ⟹ c² − a·2^z − a = ... hmm: a(c² − 1) = 2^y + 2^z c = 2^z(2^(y−z) + c).

So:
- c(a² − 1) = 2^x(1 + 2^(z−x) a) ... (III)
- a(c² − 1) = 2^z(2^(y−z) + c) ... (IV)

In (O,O,O): a,c odd ⟹ a²−1 ≡ 8 | ..., c odd. 1 + 2^(z−x)·a: z−x ≥ 1 so even·odd + 1 = odd. So v₂(RHS of III) = x, giving **v₂(a² − 1) = x** (consistent with before, good—wait, (III) says c(a²−1) = 2^x(1 + 2^(z−x)a), v₂ LHS = v₂(a²−1) = x ✓ same as (I) gave. Good consistency.)

And (IV): a(c²−1) = 2^z(2^(y−z) + c). 2^(y−z) even, c odd ⟹ sum odd. So **v₂(c² − 1) = z**.

Similarly substituting around for b: from ab − c = 2^x ⟹ a = (2^x + c)/b... let me just get the b-analogue: substitute a = (2^x + c)/b into ca − b: c(2^x + c)/b − b = 2^z ⟹ 2^x c + c² − b² = 2^z b ⟹ b² − ... hmm sign: b² = c² + 2^x c − 2^z b ⟹ messy. Try: substitute c = bc − 2^y... i.e., a = bc − 2^y into ab − c: (bc − 2^y)b − c = 2^x ⟹ b²c − c − 2^y b = 2^x ⟹ c(b² − 1) = 2^x + 2^y b = 2^x(1 + 2^(y−x) b). And into ca − b: (bc − 2^y)c − b = 2^z ⟹ bc² − b − 2^y c = 2^z ⟹ b(c² − 1) = 2^z + 2^y c = 2^z(1 + 2^(y−z) c).

So:
- c(b² − 1) = 2^x(1 + 2^(y−x) b) ⟹ v₂(b² − 1) = x (since 1 + even·odd = odd). Consistent with (II). ✓
- b(c² − 1) = 2^z(1 + 2^(y−z) c) ⟹ **v₂(c² − 1) = z**. ✓ consistent with (IV).

Great, so in (O,O,O) we have the clean result:

**(P1)** x = v₂(a²−1) = v₂(b²−1), and z = v₂(c²−1).

For odd n: v₂(n²−1) = v₂(n−1) + v₂(n+1). Define s(n) := v₂(n²−1) ≥ 3 for odd n.

So x = s(a) = s(b), z = s(c).

Interesting! Now recall earlier relations: v₂(b−a) = z − C = s(c) − v₂(c+1) = [v₂(c−1)] . Because s(c) − v₂(c+1) = v₂(c−1). So **v₂(b − a) = v₂(c − 1)**!

Similarly v₂(c−b) = x − A = s(a) − v₂(a+1) = v₂(a−1). So **v₂(c − b) = v₂(a − 1)**.

And v₂(c−a) = x − B = s(a) − v₂(b+1)... wait that mixes a and b. Hold on: v₂(c−a) = x − B comes from identity (3): (c−a)(b+1) = 2^y − 2^x, v₂ = x. So v₂(c−a) = x − B = s(a) − v₂(b+1)? No wait, x = s(a) = s(b). Hmm, x = v₂(a²−1) AND x = v₂(b²−1). So v₂(c−a) = s(b) − v₂(b+1) = v₂(b−1). Or equally = s(a) − v₂(a+1) = v₂(a−1). Both must be equal: v₂(b−1) = v₂(a−1)?? But wait, that's forced: v₂(c−a) equals both v₂(a−1) and v₂(b−1), so v₂(a−1) = v₂(b−1) =: m.

Hmm wait, but that seems too strong. Let me double check with actual numbers... but we have no known (O,O,O) solutions (conjecturally none exist). Let me sanity check the derivation on the known (E,E,O) solution (2,6,11): there x=0. v₂(a²−1)=v₂(3)=0 ✓. v₂(b²−1)=v₂(35)=0 ✓. z=v₂(c²−1)=v₂(120)=3 ✓ (2^z=ca−b=22−6=16, z=4!). Wait: ca − b = 11·2 − 6 = 16 = 2^4, so z = 4. But v₂(121−1)=v₂(120)=3. Contradiction?!

Hold on. Let me recheck. In deriving z = v₂(c²−1), I used b(c²−1) = 2^z(1 + 2^(y−z)c) with the claim 1 + 2^(y−z)c is odd. That requires y − z ≥ 1, true here (y=6? bc−a = 66−2=64, y=6; z=4; y−z=2). Then 1 + 4·11 = 45, odd ✓. So v₂(b(c²−1)) = v₂(6·120) = 1 + 3 = 4 ✓ = z. Oh but b is even here! v₂(b) = 1 contributes. In (O,O,O), b odd, so v₂(b(c²−1)) = v₂(c²−1) = z ✓. In (E,E,O), v₂(b) + v₂(c²−1) = z. Fine, no contradiction—the formula z = v₂(c²−1) holds only when b is odd, which is exactly case (O,O,O). Good.

Similarly x = v₂(a²−1) required b odd (for (I)) and a odd (for (II)). Both hold in (O,O,O). ✓

So in (O,O,O):
- x = v₂(a²−1) = v₂(b²−1)
- z = v₂(c²−1)
- v₂(b−a) = z − C = v₂(c−1)
- v₂(c−b) = x − A = v₂(a−1)
- v₂(c−a) = x − B = v₂(b−1)

Wait, I need to recompute v₂(c−a). Identity (3): (c−a)(b+1) = 2^y − 2^x. v₂(RHS) = x since y > x. So v₂(c−a) + B = x ⟹ v₂(c−a) = x − B. With x = v₂(b²−1) = v₂(b−1) + B, we get v₂(c−a) = v₂(b−1). Also with x = v₂(a²−1): v₂(c−a) = x − B... hmm this uses B = v₂(b+1), so v₂(c−a) = v₂(a²−1) − v₂(b+1). Not as clean. Let me just be careful:

x = v₂(a²−1) = v₂(b²−1). B = v₂(b+1). v₂(c−a) = x − B = v₂(b²−1) − v₂(b+1) = v₂(b−1). 

So v₂(c−a) = v₂(b−1) exactly.

Also v₂(c−b) = x − A where A = v₂(a+1): = v₂(a²−1) − v₂(a+1) = v₂(a−1). So v₂(c−b) = v₂(a−1).

And v₂(b−a) = z − C = v₂(c²−1) − v₂(c+1) = v₂(c−1). So v₂(b−a) = v₂(c−1).

Beautiful. Now, since c > b > a (strict, as x<z<y forces strict ordering... wait does it? x<z<y was derived assuming all distinct; two equal already handled. In all-distict case, x<z<y strictly and correspondingly a<b<c strictly? Let me confirm: if a=b then two equal case. So a<b<c.)

Now here's something: v₂(b−a) = v₂(c−1) and v₂(c−a) = v₂(b−1) and v₂(c−b) = v₂(a−1).

Since a<b<c, we have b−a < c−a and c−b < c−a. Also v₂(b−a) ≤ log₂(b−a) etc.

Hmm, let me think about whether x = v₂(a²−1) = v₂(b²−1) leads anywhere. 

Note v₂(a²−1) = v₂(b²−1) with a < b both odd. E.g., a=3: s=3; b=5: s=v₂(24)=3. a=3,b=13: v₂(168)=3. Many possibilities.

Alternative approach: use the exact equations (I) and (II) with the now-known valuations to extract exact factorizations.

(I): b(a−1)(a+1) = 2^x (2^(z−x) + a), with v₂(a−1) = m_a⁻, v₂(a+1) = m_a⁺, m_a⁻ + m_a⁺ = x.

Write a−1 = 2^(m⁻) u, a+1 = 2^(m⁺) w, u,w odd. Then b·u·w = (2^(z−x) + a) / [2^(x − m⁻ − m⁺)] = 2^(z−x) + a (since x = m⁻+m⁺ exactly!). So:

**b·u·w = 2^(z−x) + a**, i.e., dividing: b(a²−1)/2^x = 2^(z−x) + a. But that's just (I) restated: (a²−1)/2^x · b = 2^(z−x) + a. Yes trivially. OK so the content is just (I) itself with the valuation fact making things integral. Fine.

Let me look at (I): b(a²−1) = 2^x(2^(z−x) + a) ⟹ 2^(z−x) = b(a²−1)/2^x − a = b·[(a²−1)/2^x] − a. Let k := (a²−1)/2^x = (a²−1)/s(a) — this is an odd number, specifically k = u·w where u=(a−1)/2^{m⁻}, w=(a+1)/2^{m⁺}.

So 2^(z−x) = bk − a. Similarly from (II): 2^(y−x) = a·ℓ − b where ℓ := (b²−1)/2^x (odd).

And z−x ≥ 1, y−x ≥ z−x+1... wait actually y−x > z−x ≥ 1.

Hmm, so: 2^(z−x) + a = bk where k = (a²−1)/2^x odd ≥ 1.

If k = 1: a² − 1 = 2^x. Odd a: (a−1)(a+1) consecutive even numbers differing by 2, both powers-of-2 times... a−1=2, a+1=4 ⟹ a=3, x=3. So a=3, x=3, and then 2^(z−x) = b − 3 ⟹ b = 3 + 2^(z−3). Also need v₂(b²−1) = 3.

Then continue with (II): 2^(y−x) = aℓ − b = 3ℓ − b where ℓ = (b²−1)/8.

Hmm, let me try to find a general kill. Let me think about inequalities.

Actually, maybe better: think mod small numbers on the original system. All of ab−c, bc−a, ca−b are powers of 2, i.e., ≡ 0 mod 2^min. In particular each is even (in (O,O,O) they're all even, indeed divisible by 4? x ≥ max(A,B)+1 ≥ 2 since A,B ≥ 1. Actually x ≥ 2, z ≥ 2, y ≥ 3.)

Mod 4: ab ≡ c, bc ≡ a, ca ≡ b (mod 4) if x,z,y ≥ 2. Multiply: (abc)² ≡ abc mod 4 ⟹ abc ≡ 1 mod 4 (abc odd). So a ≡ b ≡ c ≡ 1 mod 4 or exactly two of them ≡ 3 mod 4... products: abc ≡ 1 mod 4 happens iff number of factors ≡3 mod 4 is even (0 or 2).

Also from ab ≡ c mod 4: if a ≡ b ≡ 1, c ≡ 1. If a≡1,b≡3 ⟹ c≡3. If a≡3,b≡3 ⟹ c≡1. Combined with abc≡1: consistent automatically. So mod 4 gives: c ≡ ab, a ≡ bc, b ≡ ca mod 4. These imply: a ≡ bc ≡ b(ca) ≡ b·b·(ab)... let me verify consistency: a ≡ bc and c ≡ ab ⟹ a ≡ b(ab) = ab² ≡ a·b³... hmm mod 4, b² ≡ 1 always (b odd), so a ≡ b·c, c ≡ ab ⟹ a ≡ b·(ab) = a·b² ≡ a ✓. No new info. Mod 8 might give more when x,z ≥ 3.

If x ≥ 3: ab ≡ c mod 8. If z ≥ 3: ca ≡ b mod 8. If y ≥ 3: bc ≡ a mod 8.

Sub-case: suppose x, z, y all ≥ 3. Then ab ≡ c, bc ≡ a, ca ≡ b mod 8. Multiplying: (abc)² ≡ abc mod 8 ⟹ abc ≡ 1 mod 8 (odd). Possible. Divide ab≡c by ca≡b: b/c ≡ c/b mod 8 ⟹ b² ≡ c² mod 8 ⟹ automatic (both ≡1). Hmm mod 8 all odd squares are 1, so these give: ab ≡ c means... a,b odd: ab ≡ c mod 8 constrains. E.g., a=3,b=3: ab=9≡1 ⟹ c≡1 mod 8.

This line gives existence of many residue combos; not obviously contradictory. Need something sharper.

Sharper idea: use (P1) plus the original size relations.

We know: 2^x = ab − c. With x = v₂(a²−1) = v₂(b²−1) ≥ 3.

So ab − c = v₂-value-ish: c = ab − 2^x. Since c > b: ab − 2^x > b ⟹ b(a−1) > 2^x.

Also ca − b = 2^z = 2^(v₂(c²−1)): c(a−1) = ... wait ca − b = 2^z ⟹ c = (2^z + b)/a.

Combine: ab − 2^x = (2^z+b)/a ⟹ a²b − 2^x a = 2^z + b ⟹ b(a²−1) = 2^z + 2^x a — same as (I). Circular, fine.

Let me try yet another angle: the quotient structure. Define D₁ = 2^(y−z) = (bc−a)/(ca−b). Compute: bc − a vs ca − b. Hmm.

D₁ = (bc−a)/(ca−b) = 2^(y−z) =: T₁ ≥ 4 (since y−z ≥ 2? y−z ≥ 1; actually y>z strictly so y−z≥1, T₁ ≥ 2).

T₁(bc − a) = ca − b ⟹ T₁bc − T₁a = ca − b ⟹ c(T₁b − a) = T₁a − b ⟹

**c = (T₁a − b)/(T₁b − a)**.

Since c > 0 and numerator T₁a − b > 0 needed: b < T₁ a. Also denominator positive: T₁ b > a, auto.

c ≥ b+2 (both odd, c>b): (T₁a − b)/(T₁b − a) ≥ b + 2.

Hmm wait but earlier (from R1/R2 notes) the ratio was c = b(T₂a+1)/(T₂+a) with T₂ = 2^(z−x). Let me recompute mine: T₁(bc−a) = ca−b ⟹ T₁bc − T₁a − ca + b = 0 ⟹ c(T₁b − a) = T₁a − b ⟹ c = (T₁a−b)/(T₁b−a). Check with (2,6,11)-type... those aren't OOO. Let me check dimension: T₁ large ⟹ c → a/b · ... hmm as T₁→∞, c → a/b < 1?? That can't be right. As T₁→∞: numerator ~T₁a, denominator ~T₁b, ratio → a/b < 1. But c ≥ 1. So T₁ bounded! Indeed c ≥ b forces (T₁a−b) ≥ b(T₁b−a) ⟹ T₁a − b ≥ T₁b² − ab ⟹ T₁(a − b²) + ab − b ≥ 0 ⟹ since a < b² (as b ≥ 3, a < b... wait a<b so a−b² <0 strongly), T₁ ≤ (ab−b)/(b²−a) = b(a−1)/(b²−a).

So **T₁ = 2^(y−z) ≤ b(a−1)/(b²−a) < b(a−1)/(b²−b) = (a−1)/(b−1) < 1**??? Wait that gives T₁ < 1, impossible!! Let me recheck!!

Hmm wait, that can't be right. Let me recompute. c ≥ b: (T₁a − b)/(T₁b − a) ≥ b.

Need denominator positive first: T₁b − a > 0. OK assume.

T₁a − b ≥ b(T₁b − a) = T₁b² − ab ⟹ T₁a − T₁b² ≥ b − ab = b(1−a) ⟹ T₁(a − b²) ≥ b(1−a) ⟹ multiply by −1: T₁(b² − a) ≤ b(a−1) ⟹ T₁ ≤ b(a−1)/(b²−a).

Since a < b: b² − a > b² − b = b(b−1), so T₁ < b(a−1)/(b(b−1)) = (a−1)/(b−1) < 1 since a < b. Contradiction!

That suggests (O,O,O) is IMPOSSIBLE immediately?! But wait, this same argument should apply to any all-distinct configuration... including (E,E,O)=(2,6,11)! There T₁ = 2^(y−z) = 2^(6−4) = 4. Check: b=6, a=2: T₁ ≤ b(a−1)/(b²−a) = 6·1/34 < 1. But T₁ = 4?! Contradiction — so I made an algebra error somewhere!

Let me recheck: T₁ = 2^(y−z). y corresponds to bc−a = 64, y=6. z: ca−b = 16, z=4. So T₁ = 2² = 4. Formula c = (T₁a − b)/(T₁b − a): (4·2 − 6)/(4·6 − 2) = 2/22 = 1/11 ≠ 11. WRONG. So my derivation of c = (T₁a−b)/(T₁b−a) is wrong. Let me redo:

T₁ = 2^(y−z) = (bc−a)/(ca−b). Cross-multiplying: T₁(ca − b) = bc − a. (Not the other way!) Since (bc−a) = T₁·(ca−b).

T₁·ca − T₁·b = bc − a ⟹ c(T₁a − b) = T₁b − a ⟹ **c = (T₁b − a)/(T₁a − b)**.

Check: (4·6 − 2)/(4·2 − 6) = 22/2 = 11 ✓. 

Now redo the inequality: c ≥ b: (T₁b − a)/(T₁a − b) ≥ b. Numerator positive: T₁b > a ✓ auto. Denominator positive: T₁a − b > 0 required (else c ≤ 0 or undefined; c>0 needs numerator,denominator same sign; numerator >0 since T₁b ≥ 2b > a... T₁≥1... T₁ ≥ 2 in our case, b > a so T₁b > a definitely; so denominator must be > 0 too).

T₁b − a ≥ b(T₁a − b) = T₁ab − b² ⟹ T₁b − T₁ab ≥ a − b² ⟹ T₁b(1 − a) ≥ a − b² ⟹ multiply −1: T₁b(a−1) ≤ b² − a ⟹ **T₁ ≤ (b² − a)/(b(a−1))**.

Check (2,6,11): (36−2)/(6·1) = 34/6 ≈ 5.67 ≥ 4 ✓ consistent.

So in general (any all-distinct triple): 2^(y−z) ≤ (b²−a)/(b(a−1)).

Similarly by symmetry (reversing roles), define T₂ = 2^(z−x) = (ca−b)/(ab−c): cross-multiply: T₂(ab−c) = ca−b ⟹ T₂ab − T₂c = ca − b ⟹ c(T₂+a) = T₂ab + b = b(T₂a + 1) ⟹ **c = b(T₂a+1)/(T₂+a)** ✓ (matches notes).

c ≥ b ⟹ (T₂a+1) ≥ (T₂+a) ⟹ ... wait c/b = (T₂a+1)/(T₂+a) ≥ 1 ⟺ T₂a + 1 ≥ T₂ + a ⟺ T₂(a−1) ≥ a−1 ⟺ T₂ ≥ 1 ✓ auto. And c ≤ ? upper bound on T₂ from c ≤ ... hmm c can be huge here? c = b(T₂a+1)/(T₂+a) → ba·b/a... as T₂→∞, c → ba/b·(a/a)... limit: b·T₂a/T₂ = ab. Interesting: c < ab always (consistent with c = ab − 2^x < ab ✓).

OK so now combine the two bounds. In (O,O,O): T₁ = 2^(y−z) ≥ 2, T₂ = 2^(z−x) ≥ 2.

Bound 1: T₁ ≤ (b²−a)/(b(a−1)).

Hmm, when is (b²−a)/(b(a−1)) ≥ 2? ⟺ b² − a ≥ 2ab − 2a ⟺ b² − 2ab + a ≥ 0 ⟺ b(b−2a) + a ≥ 0. If b ≥ 2a: auto true. If b < 2a: b(b−2a) + a ≥ 0 ⟺ a ≥ b(2a−b) ⟺ ... e.g. b close to a: b = a+ε. Roughly need a ≥ ~b·a ⟺ false unless... a ≥ 2ab − b² ⟺ b² ≥ 2ab − a ⟺ b² − 2ab + a ≥ 0. For a=3,b=5: 25−30+3=−2 <0 ⟹ bound < 2 ⟹ contradiction already! Interesting. For a=3, b=3: excluded (a<b). a=3,b=7: 49−42+3=10 ≥0 fine.

So (O,O,O) with a<b≤2a-ish narrow window gets killed by T₁ ≥ 2 alone. Specifically T₁ ≥ 2 requires b² − a ≥ 2b(a−1), i.e., b² − 2ab + 2a − a ≥ 0, b² −2ab + a ≥ 0. Solve for b: b ≥ a + √(a²−a) ≈ 2a − 1/2. So roughly b ≳ 2a. Precisely: b² − 2ab + a ≥ 0 ⟺ (b − a)² ≥ a² − a = a(a−1) ⟺ b − a ≥ √(a(a−1)), i.e., b ≥ a + ⌈√(a(a−1))⌉. For a ≥ 2, √(a(a−1)) is between a−1 and a. So condition ⟺ b − a ≥ a ⟺ b ≥ 2a. Let me verify: (b−a)² ≥ a(a−1). If b−a = a−1: (a−1)² vs a²−a: a²−2a+1 vs a²−a ⟺ −2a+1 vs −a ⟹ (a−1)² < a²−a. So indeed need b−a ≥ a, i.e., **b ≥ 2a**.

So from T₁ ≥ 2: b ≥ 2a. 

Now similarly, can we get an upper bound involving T₂ that conflicts? T₂ = 2^(z−x) and c = b(T₂a+1)/(T₂+a). Also y−z: T₁ relates b and c... hmm.

Use the other substitution: from bc − a = 2^y and ab − c = 2^x: T₃ = 2^(y−x) = T₁T₂ = (bc−a)/(ab−c). Cross: T₃(ab−c) = bc−a ⟹ T₃ab − T₃c = bc − a ⟹ c(T₃ + b) = T₃ab + a ⟹ c = a(T₃b+1)/(T₃+b).

c ≥ b: a(T₃b+1) ≥ b(T₃+b) ⟹ T₃ab + a ≥ T₃b + b² ⟹ T₃b(a−1) ≥ b² − a ⟹ T₃ ≥ (b²−a)/(b(a−1)).

But T₃ = T₁T₂ and T₁ ≤ (b²−a)/(b(a−1)). So T₂ ≥ T₃/T₁ ≥ [(b²−a)/(b(a−1))] / [(b²−a)/(b(a−1))] = 1. Trivial. Hmm.

OK here's another thought. Use the *exact* equation c = b(T₂a+1)/(T₂+a) together with integrality/divisibility: gcd(T₂+a, T₂a+1) = gcd(T₂+a, T₂a+1 − a(T₂+a)) = gcd(T₂+a, 1 − a²) = gcd(T₂+a, a²−1). Notes had this: gcd divides a²−1 = (a−1)(a+1). And T₂+a ≥ a+2 (T₂ ≥ 2, a ≥ 3). Hmm.

Divisibility: (T₂+a) | b(T₂a+1). Let g = gcd(T₂+a, T₂a+1) | a²−1. So (T₂+a)/g | b.

In (O,O,O): b < c and c = b(T₂a+1)/(T₂+a) ⟹ (T₂a+1)/(T₂+a) > 1 fine.

Hmm, let me think about combining with the P1 valuation results. We had:

x = v₂(a²−1) = v₂(b²−1), z = v₂(c²−1), v₂(b−a) = v₂(c−1), v₂(c−b) = v₂(a−1), v₂(c−a) = v₂(b−1).

Now here's a thought: consider the equation 2^x = ab − c mod higher powers. We know ab ≡ c mod 2^x but NOT mod 2^(x+1) (since ab − c = 2^x exactly). 

Similarly ca ≡ b mod 2^z exactly, bc ≡ a mod 2^y exactly.

Consider ab ≡ c (mod 2^x). Multiply by c: abc ≡ c² (mod 2^x·c?) no—mod 2^x: abc ≡ c². Also ca ≡ b mod 2^z with z > x: so mod 2^x: ca ≡ b. Multiply by b: abc ≡ b² mod 2^x. So c² ≡ b² mod 2^x ⟹ (c−b)(c+b) ≡ 0 mod 2^x. v₂(c−b) = v₂(a−1), v₂(c+b) = v₂(... ) c+b even; v₂(c+b) = v₂(c−b) typically? For odd c,b: v₂(c+b) = v₂(c−b) iff... one of them has extra. Standard: of the two numbers c−b, c+b, v₂ values: v₂(c−b) + v₂(c+b) = v₂(c²−b²) = v₂((c²−1)−(b²−1)). We know v₂(c²−1) = z, v₂(b²−1) = x < z. So v₂(c² − b²) = x (subtracting a number with lower valuation dominates: v₂(X−Y) = min(v₂X, v₂Y) when unequal). So v₂(c²−b²) = x. And (c−b)(c+b): v₂(c−b) = v₂(a−1) =: α⁻. So v₂(c+b) = x − α⁻.

Consistency: c−b and c+b both even; their valuations α⁻ and x−α⁻. One of c±b has v₂ = 1 exactly (standard fact for odd c,b: v₂(c−b) ≠ v₂(c+b), min = 1). So {α⁻, x−α⁻} = {1, something}. Either way min(α⁻, x−α⁻) = 1.

So either v₂(c−b) = 1 or v₂(c+b) = 1, and correspondingly the other is x − 1.

Case (i): v₂(c−b) = 1, v₂(c+b) = x−1. Then α⁻ = v₂(a−1) = 1.
Case (ii): v₂(c−b) = x−1, v₂(c+b) = 1. Then α⁻ = x−1.

By symmetry between a and... hmm wait, similar relations hold for pairs (a,b): ab ≡ c mod 2^x and bc ≡ a mod 2^y, y > x: mod 2^x: bc ≡ a; multiply by a: abc ≡ a². And ab ≡ c multiply by c: abc ≡ c². So a² ≡ c² mod 2^x ⟹ (a−c)(a+c) ≡ 0 mod 2^x: v₂(c−a) + v₂(c+a) = x (since v₂(c²−a²) = v₂((c²−1)−(a²−1)) = min(z, x) = x). v₂(c−a) = v₂(b−1) =: β⁻. So v₂(c+a) = x − β⁻, and again min(β⁻, x−β⁻) = 1.

And pair (a,b) via bc≡a (mod 2^y) and ca≡b (mod 2^z): mod 2^z: bc ≡ a; ×a: abc ≡ a². ca ≡ b; ×b: abc ≡ b². So a² ≡ b² mod 2^z: v₂(a²−b²) ≥ z. But v₂(a²−b²) = v₂((a²−1)−(b²−1)) = min(x,x) = x (equal valuations! v₂(a²−1) = v₂(b²−1) = x, difference could be higher). Indeed v₂(a²−b²) = x + v₂(u−w) where a²−1 = 2^x u, b²−1 = 2^x w, u,w odd. Need ≥ z. OK: v₂((a−b)(a+b)) ≥ z. v₂(b−a) = v₂(c−1) =: γ⁻. So v₂(a+b) ≥ z − γ⁻. Also standard min fact: min(v₂(a−b), v₂(a+b)) = 1. So γ⁻ = 1 or v₂(a+b) = 1 & ...

Hmm, this is getting complicated but rich. Let me organize. Denote:
- α⁻ = v₂(a−1), α⁺ = v₂(a+1), α⁻+α⁺ = x (one of them is 1)
- β⁻ = v₂(b−1), β⁺ = v₂(b+1), β⁻+β⁺ = x (one is 1)
- γ⁻ = v₂(c−1), γ⁺ = v₂(c+1), γ⁻+γ⁺ = z (one is 1)

Relations derived:
(R1) v₂(b−a) = γ⁻ [from v₂(b−a) = z − C]
(R2) v₂(c−b) = α⁻
(R3) v₂(c−a) = β⁻
(R4) v₂(b²−a²) = x + v₂(u−w) ≥ z where u,w odd — gives v₂(a+b) ≥ z − γ⁻.
(R5) v₂(c²−b²) = x, split as v₂(c−b)+v₂(c+b) = α⁻ + v₂(c+b) = x ⟹ v₂(c+b) = x − α⁻.
(R6) v₂(c²−a²) = x, split: β⁻ + v₂(c+a) = x ⟹ v₂(c+a) = x − β⁻.

Standard facts: min(v₂(b−a), v₂(a+b)) = 1; min(v₂(c−b), v₂(c+b)) = 1; min(v₂(c−a), v₂(c+a)) = 1.

From (R5)&standard: min(α⁻, x−α⁻) = 1 ⟹ α⁻ = 1 or α⁻ = x−1.
From (R6)&standard: β⁻ = 1 or β⁻ = x−1.

Also α⁺ = x − α⁻ ∈ {x−1, 1}: so a ≡ ±... : α⁻ = 1 means a ≡ 1 mod 4? No: v₂(a−1)=1 ⟺ a ≡ 3 mod 4. α⁻ = x−1, α⁺=1 ⟺ a ≡ 1 mod 4.

Similarly for b. And for c: γ⁻ = 1 or γ⁻ = z−1.

Now use (R1): v₂(b−a) = γ⁻. And min(v₂(b−a), v₂(a+b)) = 1.

Case A: γ⁻ = 1. Then v₂(b−a) = 1, v₂(a+b) = x−1 (from R4 chain? no wait). Hmm (R4): v₂(a+b) ≥ z − γ⁻ = z − 1. But also min(v₂(b−a), v₂(a+b)) = 1: v₂(b−a) = γ⁻ = 1 ✓ consistent, v₂(a+b) arbitrary ≥ 1. And v₂(a+b) ≥ z−1 ≥ 1 fine. Hmm OK.

But wait: v₂(a+b) ≥ z−1 and v₂(a²−b²) = v₂(a−b)+v₂(a+b) = 1 + v₂(a+b) ≥ z. But also v₂(a²−b²) = x + v₂(u−w) where u = (a²−1)/2^x, w = (b²−1)/2^x odd. Fine.

Hmm, but here's a tension: v₂(a+b) ≥ z − 1 and x = α⁻+α⁺ ≤ ... no direct tension yet. Let me get sizes: a+b < 2b, so v₂(a+b) ≤ log₂(a+b) < log₂ 2b. And z = v₂(c²−1) = γ⁻+γ⁺ ≤ 1 + log₂((c+1)/2) roughly z ≤ log₂(c+1). Sizes don't clash.

Let me go back to exact equations and try to squeeze with the valuation facts. 

Exact equations in (O,O,O):
(I): b(a²−1) = 2^x(2^(z−x) + a) ⟹ divide both sides by 2^x: b·u·w' ... let me define U_a := (a²−1)/2^x = odd. Then:

b·U_a = 2^(z−x) + a ... (I')
a·U_b = 2^(y−x) + b ... (II') where U_b = (b²−1)/2^x odd.

From (I'): 2^(z−x) = b·U_a − a. Since z > x, LHS even... wait z−x ≥ 1 so LHS even, but RHS = b·U_a − a = odd·odd − odd = even ✓.

Size: 2^(z−x) = b·U_a − a ≥ b·U_a − b = b(U_a − 1)... hmm if U_a ≥ 3 then 2^(z−x) ≥ 2b... but also 2^(z−x) < ... hmm what's an upper bound? z−x relates to c: 2^(z−x) = (ca−b)/(ab−c)·... wait no, T₂ = 2^(z−x) = (ca−b)/(ab−c). Upper bound: ca−b < ca, ab−c > ab − ab = ... hmm ab − c ≥ 2^x. T₂ = (ca−b)/2^x < ca/2^x. Not obviously useful.

Better: T₂ = 2^(z−x) = b·U_a − a and also from c = b(T₂a+1)/(T₂+a).

Let me also write the analogous exact eq for c: (IV'): a·U_c' ... from a(c²−1) = 2^z(2^(y−z)+c): a·U_c = 2^(y−z) + c where U_c := (c²−1)/2^z odd. So:

a·U_c = 2^(y−z) + c ... (IV') and b·U_c = 2^(y−z) + ... wait earlier: b(c²−1) = 2^z(1 + 2^(y−z)c) ⟹ b·U_c = 1 + 2^(y−z)c ... hmm that one has the form 1 + T₁c not T₁ + c. Let me recheck. Earlier I derived: "b(c² − 1) = 2^z + 2^y c ⟹ b(c²−1) = 2^z(1 + 2^(y−z)c)". Check with substitution method: a = bc − 2^y into ca − b: (bc−2^y)c − b = 2^z ⟹ bc² − 2^yc − b = 2^z ⟹ b(c²−1) = 2^z + 2^y c ✓. And a(c²−1) = 2^z(2^(y−z) + c) came from c-substitution... let me recheck (IV): substituting b = ca − 2^z into bc − a = 2^y: (ca − 2^z)c − a = 2^y ⟹ ac² − 2^zc − a = 2^y ⟹ a(c²−1) = 2^y + 2^z c = 2^z(2^(y−z) + c) ✓.

So:
(IV') a·U_c = 2^(y−z) + c, with U_c = (c²−1)/2^z odd.
(V') b·U_c = 1 + 2^(y−z)·c.

Both hold. Subtract or compare: from (IV'): 2^(y−z) = a·U_c − c. Plug into (V'): b·U_c = 1 + c(a·U_c − c) = 1 + ac·U_c − c² ⟹ U_c(ac − b) = c² − 1·... wait: b U_c − ac U_c = 1 − c² ⟹ U_c(b − ac) = 1 − c² ⟹ U_c(ac − b) = c² − 1. But U_c = (c²−1)/2^z, so this says (c²−1)(ac−b)/2^z = c²−1 ⟹ ac − b = 2^z. Which is just the original equation ✓ circular. OK.

Fine. Let me take stock and think about what kills (O,O,O).

Current facts: b ≥ 2a (from T₁ ≥ 2). Also c = ab − 2^x and c ≡ ... hmm.

Another key relation: 2^x = ab − c > ab − c... and c > b: 2^x < ab − b = b(a−1) ⟹ 2^x < b(a−1). Also x = v₂(a²−1) = v₂(b²−1).

Also 2^z = ca − b > ca − c = c(a−1) ≥ c... wait c(a−1) with a ≥ 3: ≥ 2c. So 2^z ≥ 2c + something: 2^z = ca − b > ca − c = c(a−1) ≥ 2c.

And z = v₂(c²−1) = γ⁻+γ⁺ ≤ 1 + log₂(c+1) — no wait, γ⁻+γ⁺: one of them is 1, the other ≤ log₂(c+1) − 1. So z ≤ log₂(c+1) ⟹ 2^z ≤ c+1. But we just showed 2^z = ca − b > c(a−1) ≥ 2c for a ≥ 3. So 2^z > 2c but 2^z ≤ c + 1. CONTRADICTION!!! 

Wait, seriously? Let me double-check: z = v₂(c²−1). c odd. c² − 1 = (c−1)(c+1). v₂ = γ⁻ + γ⁺. One of c−1, c+1 divisible by 4, other by exactly 2. So min(γ⁻,γ⁺) = 1, and max(γ⁻,γ⁺) ≤ log₂(c+1) (since 2^max | c+1 or | c−1 ≤ c+1). So z = 1 + max ≤ 1 + log₂(c+1) ⟹ 2^z ≤ 2(c+1). Hmm, factor 2: 2^z = 2·2^max·... let me redo: 2^(z−1) = 2^max divides c+1 (or c−1), so 2^(z−1) ≤ c+1 ⟹ 2^z ≤ 2c + 2.

And 2^z = ca − b. With a ≥ 3, b > a: ca − b ≥ 3c − b. Is 3c − b > 2c + 2? ⟺ c > b + 2 ⟺ c ≥ b + 2 (odd ints). TRUE since c > b, both odd!

So 2^z = ca − b ≥ 3c − b ≥ c + (c − b) ≥ c + 2. And 2^z ≤ 2c + 2. So c + 2 ≤ 2^z ≤ 2c + 2. Hmm not immediately contradictory. Let me be more careful.

Actually wait: I should double check whether z = v₂(c²−1) really holds. From b(c²−1) = 2^z(1 + 2^(y−z)c): y−z ≥ 1 ⟹ 2^(y−z)c even ⟹ (1 + ...) odd ⟹ v₂(b(c²−1)) = z. b odd ⟹ v₂(c²−1) = z. ✓✓.

So: 2^z = ca − b and 2^z = 2^z obviously... the constraint is z = v₂(c²−1) ⟹ 2^z ≤ 2(c+1)... wait more precisely: v₂(c²−1) = z means 2^z | c²−1 and 2^(z+1) ∤ c²−1. c² − 1 = (c−1)(c+1) < (c+1)² ⟹ 2^z < (c+1)² trivial. Sharper: 2^z | (c−1)(c+1) with gcd(c−1, c+1) = 2. So 2^(z−1) | lcm-ish... precisely: writing c−1 = 2^γ⁻u, c+1 = 2^γ⁺w: 2^z = 2^(γ⁻+γ⁺) and 2^max(γ⁻,γ⁺) | c+1 (the bigger power divides whichever has the max exponent, and that number is ≤ c+1). max ≥ z/2... that's weak. Use: min = 1, so max = z − 1, and 2^(z−1) | (c±1), so 2^(z−1) ≤ c+1 ⟹ **2^z ≤ 2(c+1) = 2c + 2**.

Combined with 2^z = ca − b ≥ 3c − b and b ≤ c − 2: 2^z ≥ 3c − (c−2) = 2c + 2.

So **2c + 2 ≤ 2^z ≤ 2c + 2 ⟹ 2^z = 2c + 2 EXACTLY**, forcing equality everywhere: b = c − 2 AND a = 3 AND 2^z = 2c+2 with... wait let me recompute the chain. 2^z = ca − b. Lower bounds used: a ≥ 3 and b ≤ c−2. Equality throughout: a = 3, b = c − 2, and 2^z = 3c − (c−2) = 2c + 2 ✓ consistent.

Also need: 2^(z−1) = c+1 divides... 2^z = 2c+2 = 2(c+1) ⟹ z − 1 = v₂(c+1) = γ⁺ and γ⁻ = 1: c ≡ 3 mod 4. And c + 1 = 2^(z−1) EXACTLY (not just divisibility—we have 2^(z−1) = c+1 from equality). So c = 2^(z−1) − 1.

And b = c − 2 = 2^(z−1) − 3, a = 3.

Now check remaining conditions: x = v₂(a²−1) = v₂(9−1) = v₂(8) = 3. So x = 3: ab − c = 2^3 = 8. But ab − c = 3(2^(z−1) − 3) − (2^(z−1) − 1) = 3·2^(z−1) − 9 − 2^(z−1) + 1 = 2·2^(z−1) − 8 = 2^z − 8. Set = 8: 2^z = 16 ⟹ z = 4 ⟹ c = 2³ − 1 = 7, b = 5.

Check: (a,b,c) = (3,5,7): ab − c = 15−7 = 8 ✓ = 2³. bc − a = 35 − 3 = 32 = 2⁵ ✓!! ca − b = 21 − 5 = 16 = 2⁴ ✓!!!

WAIT. (3,5,7) IS A SOLUTION?! Let me verify once more:
- ab − c = 3·5 − 7 = 15 − 7 = 8 = 2³ ✓
- bc − a = 5·7 − 3 = 35 − 3 = 32 = 2⁵ ✓
- ca − b = 7·3 − 5 = 21 − 5 = 16 = 2⁴ ✓

OH MY GOD. (3,5,7) is a solution and it's (O,O,O)!! The conjectured solution set from previous rounds is INCOMPLETE! This is why brute force mattered (Gap 0)!

Hmm wait, but the notes said machine checks were done... "R3机核：a,b<400 内 (E,E,O) 形状解仅 (2,6,11)" — only EEO shapes were checked, not OOO. And Gap 0 asked for full brute force which was never done. Wow.

So the answer includes (3,5,7) and its permutations. Are there MORE (O,O,O) solutions? My chain above derived that IF (O,O,O) all-distinct solution exists THEN (a,b,c) = (3,5,7) exactly (under WLOG a<b<c). Let me double check the chain for soundness, since it produced equality-forcing.

Chain recap for (O,O,O), a<b<c, all odd ≥ 3:
1. x<z<y strict (two-equal cases fully resolved separately — need to make sure that resolution covers odd case too: yes, it was parity-free algebra).
2. x = v₂(a²−1) = v₂(b²−1), z = v₂(c²−1). [from b(a²−1) = 2^x(2^(z−x)+a) etc. — verified]
3. 2^z = ca − b.
4. z = v₂(c²−1) ⟹ 2^(z−1) | c+1 or c−1 ⟹ 2^(z−1) ≤ c+1 ⟹ 2^z ≤ 2c+2. [KEY: uses min(γ⁻,γ⁺)=1, standard for odd c]
5. 2^z = ca − b ≥ 3c − b ≥ 3c − (c−2) = 2c+2. [uses a ≥ 3, b ≤ c−2 since distinct odds]
6. ⟹ 2^z = 2c+2, a = 3, b = c−2, c+1 = 2^(z−1).
7. x = v₂(a²−1) = 3 ⟹ ab − c = 8 ⟹ (with a=3,b=c−2): 2c − 8 = 8... 

hold on step 7: ab − c = 3(c−2) − c = 2c − 6. Wait recompute: 3(c−2) − c = 3c − 6 − c = 2c − 6. Earlier I wrote 2^z − 8; let me recheck: with c = 2^(z−1) − 1: ab − c = 2c − 6 = 2(2^(z−1) −1) − 6 = 2^z − 2 − 6 = 2^z − 8. And ab − c = 2^x = 8 (x = 3). So 2^z = 16, z = 4, c = 7, b = 5 ✓. Both computations agree: 2c−6 = 8 ⟹ c = 7 ✓.

8. Verify (3,5,7) works ✓.

But WAIT — I should double-check step 4's sharpness: z = γ⁻ + γ⁺, min = 1, so max = z−1, and the number among c±1 carrying valuation z−1 satisfies 2^(z−1) | c±1 ⟹ c±1 ≥ 2^(z−1) ⟹ c+1 > c−1 ≥ 2^(z−1) ⟹ 2^z ≤ 2(c+1). ✓. Equality in step 5&6 forces: 2^z = 2c+2 = ca − b with a = 3, b = c−2. Also from 2^(z−1) = c+1 exactly (since 2^z = 2c+2). ✓.

Also should double check x = v₂(a²−1) = v₂(b²−1) derivation once more, and that x ≥ 1 stuff. In (O,O,O): from b(a²−1) = 2^x(2^(z−x) + a): z−x ≥ 1 ⟹ second factor odd; b odd; a²−1 has v₂ = x. YES.

Hmm wait, one more check on step 2: I claimed v₂(2^(z−x) + a) = 0. 2^(z−x) is even (z>x), a odd, sum odd ✓. And for (II'): a(b²−1) = 2^x(2^(y−x)+b): y > x ⟹ even + odd = odd ⟹ v₂(b²−1) = x ✓.

And z: from b(c²−1) = 2^z(1 + 2^(y−z)c) [derived via a = bc − 2^y substituted into ca − b]. Let me re-verify that substitution super carefully:
a = bc − 2^y. ca − b = c(bc − 2^y) − b = bc² − 2^y c − b = 2^z. So b c² − b = 2^z + 2^y c ⟹ b(c² − 1) = 2^z + 2^y c = 2^z(1 + 2^(y−z) c) ✓. y > z ⟹ 2^(y−z) even ⟹ (1 + even·c) = odd ✓. b odd ⟹ v₂(c²−1) = z ✓.

So (O,O,O) all-distinct ⟹ unique solution (3,5,7) up to permutation. FANTASTIC. The proof is quite short!

But hold on — what about (O,O,O) with two coordinates equal? Already covered: two-equal analysis gave only (2,2,2),(2,2,3)-perms, which aren't OOO. ✓. And all-distinct is forced otherwise.

Hmm wait, also need to double check the claim x < z < y in all-distinct case and a < b < c. The ordering lemma: x ≤ z ≤ y with equality conditions tied to coordinate equality: ca−b − (ab−c) = (c−b)(a+1): zero iff c = b. bc−a − (ca−b) = (b−a)(c+1): zero iff b = a. So in all-distinct: x < z < y strictly ✓, and WLOG a ≤ b ≤ c with all-distinct ⟹ a<b<c ✓.

Now — CRUCIAL — does the discovery of (3,5,7) break anything downstream? The final solution set is {(2,2,2), (2,2,3), (2,6,11), (3,5,7)} + permutations. Need to make sure the (E,E,O) analysis didn't rely on "no OOO exists" anywhere — reviewing section 2.1: it's self-contained (doesn't reference OOO). ✓. And the c-even lemma, (O,E,O) kill: independent ✓.

But wait, now I'm worried: are there even MORE solutions that previous rounds' framework missed? The parity case analysis: every triple falls into one of the 8 parity patterns. Killed: all c-even patterns (4), (O,E,O). Solved: (E,E,O) ⟹ (2,6,11); two-equal ⟹ (2,2,2),(2,2,3); (O,O,O) ⟹ (3,5,7) [just now]. Patterns: (E,E,E),(O,O,E),(E,O,E),(O,E,E) die by c-even lemma ✓. (O,E,O) dies ✓. (E,E,O) done ✓. (O,O,O) done ✓. Two-equal handled globally (before pattern split) ✓. Coordinate = 1 impossible ✓. That's exhaustive coverage!

Hmm wait, actually one subtlety: the two-equal analysis — did it assume anything about which coordinates? "a=b", "b=c" cases under WLOG a≤b≤c cover all two-equal configs (a=c impossible with a≤b≤c unless all equal). ✓.

Also the parity patterns assumed a≤b≤c WLOG — fine by symmetry.

Now let me also double-check the (E,E,O) theorem quickly since I'll reproduce it in proof.md... Actually the notes say it was assembled and verified by R3 observer with machine spot-checks. I'll re-verify key steps myself during write-up, and ALSO run the brute force (Gap 0) to confirm the complete solution set numerically. That's essential now.

Brute force plan: enumerate 2 ≤ a ≤ b ≤ c ≤ N (N = 2000 or higher), check all three are powers of 2. Also handle potential solutions where c > 2000 while a,b small? For verification purposes N=2000 fine; maybe push to 5000 for safety. Powers of 2 grow fast so solutions are sparse; expected finite set. Also asymmetric search: since conditions symmetric, enumerate ordered a≤b≤c.

Additionally, targeted parametric checks: e.g., for the EEO family, c = ab−1 forced; scan a,b up to big bounds checking the two power conditions — cheap and covers large ground beyond 2000. Similarly for OOO my proof says only (3,5,7). Could also scan "two-equal" families. But main brute force + EEO parametric sweep gives strong numerical confidence.

Let me also double check the claim in step 5: b ≤ c−2 because b<c both odd ⟹ c−b ≥ 2 ✓. a ≥ 3 since a odd ≥ 2 ⟹ a ≥ 3 ✓. ca − b ≥ 3c − b: since a ≥ 3 ✓.

Equality analysis: 2c+2 ≤ 2^z ≤ 2c+2. Lower bound chain: 2^z = ca − b ≥ 3c − b ≥ 3c − (c−2). Second inequality equality iff b = c−2; first iff a = 3. Upper bound 2^z ≤ 2(c+1) equality iff... 2^(z−1) ≤ c+1 with equality iff c+1 = 2^(z−1) exactly (and the max-valuation side is c+1, γ⁺ = z−1, γ⁻=1). Since overall equality holds: a=3, b=c−2, c+1=2^(z−1). ✓.

Then x = v₂(a²−1) = v₂(8) = 3. ab − c = 2^x = 8: 3b − (b+2) = 2b − 2 = 8 ⟹ b = 5, c = 7. ✓ (matches direct: 2c−6 = 8 ⟹ c=7.)

All consistent: unique OOO solution (3,5,7) up to permutation.

Hmm hold on, wait. I want to double-check x=v₂(a²−1) is used correctly at the end. x = 3 requires... x was DEFINED by ab−c = 2^x. We derived x = v₂(a²−1) = v₂(b²−1) as a consequence. With a=3: v₂(8)=3. With b=5: v₂(24)=3 ✓ consistent. Then ab−c = 15−7 = 8 = 2³ ✓. 

Also verify y: bc−a = 35−3 = 32, y=5. And y−z = 1: T₁ = 2. Earlier bound: T₁ ≤ (b²−a)/(b(a−1)) = (25−3)/(5·2) = 22/10 = 2.2, and T₁ = 2 ✓ tight-ish. Fun. And b ≥ 2a: 5 ≥ 6? NO! b=5 < 2a=6!! Wait, earlier I derived from T₁ ≥ 2 that b ≥ 2a. But (3,5,7) has b=5 < 6=2a. Contradiction with my own lemma?! Let me recheck THAT derivation, because if it's wrong I need to worry about other places.

Earlier: "c ≥ b: (T₁b − a)/(T₁a − b) ≥ b ⟹ ... ⟹ T₁ ≤ (b² − a)/(b(a−1)). Then T₁ ≥ 2 requires (b²−a)/(b(a−1)) ≥ 2 ⟺ b² − a ≥ 2ab − 2a ⟺ b² − 2ab + a ≥ 0 ⟺ (b−a)² ≥ a² − a." Check (3,5,7): b²−2ab+a = 25 − 30 + 3 = −2 < 0 ⟹ bound says T₁ < 2. But actual T₁ = 2. So the bound T₁ ≤ (b²−a)/(b(a−1)) must be violated or mis-derived. Direct: (b²−a)/(b(a−1)) = 22/10 = 2.2 ≥ 2. Hmm so bound gives T₁ ≤ 2.2, and T₁ = 2 ≤ 2.2 ✓ FINE. My "⟺ b ≥ 2a" step: b²−2ab+a ≥ 0. At (a,b)=(3,5): −2 < 0 ⟹ bound < 2?? But 22/10 = 2.2 ≥ 2. Let me recompute: b² − a ≥ 2b(a−1) ⟺ 25 − 3 ≥ 2·5·2 ⟺ 22 ≥ 20 ✓ TRUE. Expand: b² − a − 2ab + 2b ≥ 0 ⟺ b² − 2ab + 2b − a ≥ 0. I previously wrote "b² − 2ab + a ≥ 0" — WRONG expansion (dropped the 2b, kept a). Correct: b² − 2ab + 2b − a ≥ 0 ⟺ b(b − 2a + 2) ≥ a. At (3,5): 5(5−6+2)=5 ≥ 3 ✓. OK so the correct necessary condition from T₁≥2 is b(b−2a+2) ≥ a, which (3,5,7) satisfies. Phew — no inconsistency; that preliminary "b ≥ 2a" claim was just wrong (bad expansion), but luckily I never used it in the final chain. The final kill chain doesn't use it. Good.

Double-check the final chain doesn't use the wrong lemma: steps 1–8 above use only: strict inequalities, valuation identities, 2^z = ca−b, and v₂(c²−1) = z. Clean. 

Now, additional due diligence on step 2 (x = v₂(a²−1)): derivation b(a²−1) = 2^x(2^(z−x) + a) came from substituting c = ab − 2^x into ca − b = 2^z: ca − b = (ab − 2^x)a − b = a²b − 2^xa − b ⟹ a²b − b = 2^z + 2^x a ⟹ b(a²−1) = 2^x(a + 2^(z−x)) ✓.

Everything checks. Also note: this SAME technique — what does it give in (E,E,O)? There b even so v₂(b(a²−1)) = v₂(a²−1) + 0... a even ⟹ a²−1 odd ⟹ v₂ = 0 = x ✓ consistent (x=0 there). And c even cases: died anyway. And (O,E,O): a,c odd b even: from b(a²−1) = 2^x(2^(z−x)+a): v₂(a²−1) = x ✓ (matches R2's x=A? hmm, R2 said x = A = v₂(a+1). v₂(a²−1) = v₂(a−1)+v₂(a+1). For odd a, both ≥ 1. Hmm, x = A vs x = v₂(a²−1) — both can't... wait (O,E,O): a odd, b even, c odd. My formula: x = v₂(a²−1)? But R2 said x = A. Contradiction? Let me recheck: in (O,E,O), is z > x? Ordering x<z<y needs all-distinct — (O,E,O) solutions would be all-distinct? Not necessarily but the killed case assumed... hmm. Actually wait, in (O,E,O) with all distinct, x<z<y. Then my derivation applies: b(a²−1) = 2^x(2^(z−x)+a) with z−x ≥ 1, b even, a odd: v₂(LHS) = 0 + v₂(a²−1) = v₂(a²−1); RHS: x + 0. So x = v₂(a²−1) ≥ 3? But R2 claims x = A = v₂(a+1). Both can't hold generally... e.g. a=3: v₂(a²−1)=3, A=2. Hmm, but R2's derivation: "a,c 奇 b 偶时，由恒等式(2)取v₂得 x=A": identity (2): (c−b)(a+1) = 2^z − 2^x. v₂(RHS): z−x ≥ 1 ⟹ v₂ = x. v₂(LHS) = v₂(c−b) + A. c odd, b even ⟹ c−b ODD ⟹ v₂ = 0 ⟹ x = A. Hmm! So x = A from identity (2), and x = v₂(a²−1) from my substitution. Then v₂(a²−1) = v₂(a+1) = A ⟹ v₂(a−1) = 0?? But a odd ⟹ a−1 even ⟹ v₂(a−1) ≥ 1. CONTRADICTION ⟹ (O,E,O) impossible! 

Whoa — so my substitution identity gives an EVEN SIMPLER kill of (O,E,O) than R2's squeezing argument. Nice cross-validation of both. (R2's squeeze kill stands on its own; mine is a bonus consistency check. Actually let me double check my version once more: (O,E,O): b even. Substitution c = ab − 2^x into ca − b: ca − b = a(ab−2^x) − b = a²b − 2^x a − b. So b(a² − 1) = 2^z + 2^x a. v₂(LHS) = v₂(b) + v₂(a²−1) ≥ 1 + 3 = 4 (b even, a odd ≥ 3 ⟹ v₂(a²−1) ≥ 3). RHS: 2^x(2^(z−x)·... wait: 2^z + 2^x a = 2^x(2^(z−x) + a), odd second factor ⟹ v₂ = x. So x = v₂(b) + v₂(a²−1) ≥ 4. Meanwhile identity (2) gives x = A = v₂(a+1) ≤ log₂(a+1). Hmm, that's not instantly contradictory... wait where did I get v₂(a−1) ≥ 1 forcing contradiction: x = A and x = v₂(b) + v₂(a²−1) = v₂(b) + v₂(a−1) + A ⟹ v₂(b) + v₂(a−1) = 0. But v₂(a−1) ≥ 1 (a odd). CONTRADICTION ✓. Yes! Clean kill. Great, consistent with (O,E,O) being dead.)

Similarly for (E,... hmm what about using this identity in (O,O,E) etc.? Those die by c-even lemma anyway.

Alright. Now let me also re-examine: does the problem allow 2^0 = 1, i.e., value 1 allowed — yes "允许 2⁰=1". Our found solutions: values 8,32,16 (all ≥ 8), 2,2,1 for (2,2,3): ab−c = 4−3 = 1 = 2^0 ✓, (2,2,2): all 2. (2,6,11): ab−c = 12−11 = 1, bc−a = 64, ca−b = 16. ✓.

Could there be solutions with some coordinate = 1? R1: no (shown). ✓.

Now the FULL solution set: (2,2,2), (2,2,3)×3 perms, (2,6,11)×6 perms, (3,5,7)×6 perms. Total 1 + 3 + 6 + 6 = 16 ordered triples.

Before writing the proof, RUN THE BRUTE FORCE (Gap 0) — now doubly important given the conjecture was WRONG. Let me write the code.

Plan:
```python
def is_pow2(n): return n > 0 and (n & (n-1)) == 0
sols = []
N = 3000
for a in range(2, N+1):
    for b in range(a, N+1):
        # early termination? c up to N
        for c in range(b, N+1):
            if is_pow2(a*b-c) and is_pow2(b*c-a) and is_pow2(c*a-b):
                sols.append((a,b,c))
```
This is O(N³) = 2.7e10 — too slow in Python. Optimize: iterate a,b; compute c from ab − c = 2^x: c = ab − 2^x for candidate powers 2^x < ab with c ≥ b and c ≤ N. For each (a,b), loop over powers of two 1..ab: ~log₂(ab) ≈ 22 candidates. Total ~N²·22 ≈ 2e8 — still slowish in pure Python but OK-ish (~minutes). Better: for each a,b compute c candidates and test other two conditions. Let me also do a smarter approach: iterate a,b, for each power p = 2^x with 1 ≤ p < ab, c = ab − p; if c ≥ b: check bc − a and ca − b powers of two. Also cap c ≤ N (or allow c unbounded? c = ab − p < ab ≤ N² — allowing larger c finds solutions with c > N; the two extra conditions are cheap to test, so just test all c = ab−p ≥ b without cap! That extends coverage massively: a,b ≤ 2000, c up to 4e6.) 

Even better coverage: for a,b up to say 5000, all powers p < ab: tests ~5000²/2 · 24 ≈ 3e8 power-checks... too slow pure Python. Use numpy? Or restrict smartly: bc − a = 2^y ⟹ b(ab − p) − a = 2^y ⟹ 2^y = ab² − bp − a. Condition: is power of 2. And ca − b = a(ab−p) − b = a²b − ap − b power of 2. Just compute both and test. Bit tricks fast. Let's do a,b ≤ 3000 fully (≈ 3000²/2 · log₂(9e6)≈23 ⟹ ~1e8 inner ops — Python maybe 100–200s; acceptable, or trim with numpy vectorization over p).

Actually simpler: vectorize over p with numpy per (a,b) pair? Overhead per pair high. Alternative: loop a; for each a, loop b; inner over powers. Fine, let's just run with a reasonable bound like a,b ≤ 2000 (covers c < 4·10⁶ implicitly) and time it. Plus separately: parametric EEO scan (c = ab−1, a,b ≤ 10^6, both even, check 2 conds) — cheap-ish with number theory shortcuts (needs a²b−a−b and ab²−a−b powers of 2; just loop a even ≤ 20000, b even > a, break early when values exceed... no upper bound on b though. Hmm: for fixed a, as b grows, 2^z = b(a²−1) − a grows; require power of 2: b = (2^z + a)/(a²−1) — enumerate z up to 60: b determined! So EEO scan: for each even a ≤ 10⁶ (or beyond?), for each z ≤ 80: b = (2^z + a)/(a²−1) if integer, even, > a: then check y-condition. That's 500k × 80 = 4e7 — ok-ish; trim a to ≤ 10⁵. Similar parametric scans possible for OOO: from my proof it's unique, but numerically: for odd a, b: c = ab − 2^x... same generic scan covers it.

Honestly the (a,b) ≤ 2000 generic scan + EEO parametric scan + trust-in-proof is plenty. Also do a "two-equal" parametric check trivially covered by theory.

Also worth verifying: permutations count and that sorted tuples found match exactly {(2,2,2),(2,2,3),(2,6,11),(3,5,7)}.

Let me now also think ahead: the proof.md structure.

# Proof outline

**Answer**: all permutations of (2,2,2), (2,2,3), (2,6,11), (3,5,7).

**Step 0**: Preliminaries.
- Symmetry: WLOG a ≤ b ≤ c.
- No coordinate = 1: if a = 1: ab − c = b − c and bc − a = bc − 1... wait R1's argument: b−c and c−b both powers of 2 — where does c−b appear? If a=1: ab−c = b−c ≤ 0 unless b>c contradicting order... hmm under WLOG a≤b≤c, a=1: b−c ≤ 0, power of 2 ⟹ b−c = 0 ⟹ b = c. Then bc−a = b²−1 and ca−b = b−b = 0. 0 is not a power of 2 (positive). Actually ca − b = b·1... wait ca − b = c·a − b = b·1 − b = 0 ✗. So a=1 impossible. Even simpler: ca − b = 0. ✓. (Or R1's argument without WLOG: a=1 ⟹ ab−c = b−c, ca−b = c−b; both must be powers of 2, one is negation of other, both positive impossible.) Use the WLOG-friendly version: a=1 ⟹ ca−b = c−b = 0 (since b≤c... wait need b=c then 0 not power of 2; if b<c then ca−b<0). Either way dead. ✓
- a,b,c ≥ 2.
- Ordering lemma: x ≤ z ≤ y; strict iff coordinates distinct: ab−c vs ca−b: ca−b−(ab−c) = (c−b)(a+1) ≥ 0; bc−a − (ca−b) = (b−a)(c+1) ≥ 0. So x ≤ z ≤ y, equalities ⟺ b=c, a=b resp.

**Step 1**: Two equal coordinates.
- a=b: (given in notes, reverify): a(c−1) = 2^y (from bc−a = ac−a = a(c−1) and ca−b = ac−a same). So a = 2^u, c−1 = 2^v. ab−c = a² − c = 2^x: a² − c = 2^u·2^u − (2^v+1) = 2^(2u) − 2^v − 1. If v ≥ 1: odd ⟹ x = 0 ⟹ 2^(2u) − 2^v − 1 = 1 ⟹ 2^v(2^(2u−v) − 1) = 2 ⟹ v=1, 2u−v = 2 ⟹ u... wait: 2^v(2^(2u−v) −1) = 2 with v ≥ 1 ⟹ v = 1 and 2^(2u−1) − 1 = 1 ⟹ 2u−1 = 1 ⟹ u = 1 ⟹ a = 2, c = 3 ⟹ (2,2,3). If v = 0: c = 2 = b = a? c ≥ b = a ⟹ c = 2 ⟹ (2,2,2) (then check: works). ✓
- b=c: b(a−1) = 2^x ⟹ b = 2^t, a−1 = 2^s. If s = 0: a = 2, ab−c = 2b − b = b = 2^x ✓ any t?? wait: ab − c = 2b − b = b = 2^t ✓ automatically power of 2! And bc − a = b² − 2 = 2^(2t) − 2 must be power of 2: 2(2^(2t−1) − 1): t = 1 ⟹ 2 ✓ (b=2, (2,2,2)); t ≥ 2 ⟹ odd factor > 1 ✗. So (2,2,2). If s ≥ 1: a odd. Then bc − a = b² − a odd ⟹ y = 0 ⟹ b² − a = 1 ⟹ a = b² − 1 = 2^(2t) − 1. But also a − 1 = 2^s ⟹ 2^(2t) − 2 = 2^s ⟹ 2(2^(2t−1) −1) = 2^s ⟹ 2t−1 = 1 ⟹ t=1, s=1: a = 3, b = 2 ⟹ (3,2,2)~(2,2,3) ✓. Wait but check ab − c: 3·2 − 2 = 4 = 2² ✓ and bc−a = 4−3 = 1 ✓ ca−b = 6−2 = 4 ✓. 

  Hmm wait, in s≥1 branch: y=0 gives b² − a = 1 directly; combined with a−1 = 2^s: b² − 2 = 2^s. b = 2^t: 2^(2t) − 2 = 2^s ⟹ s=1, t=1 ⟹ a=3,b=2,c=2. But wait — need a ≤ b ≤ c: (3,2,2) violates WLOG ordering! Under WLOG a≤b≤c with b=c, a ≤ b. a = 3 > b = 2 violates. Hmm! But the case analysis "b=c under WLOG a≤b≤c" means a ≤ b = c. The sub-case found a=3,b=2 contradicts a≤b — meaning within WLOG, s≥1 branch gives nothing?! But (2,2,3) IS a solution with b=c? No: (2,2,3) sorted is a=2,b=2,c=3 — that's a=b case. Under WLOG, b=c case with a<b=c: solutions would need... (3,2,2) sorted becomes (2,3,2)? No—sorted order (2,2,3). Hmm, (3,2,2) as an unordered triple IS {2,2,3}. Under WLOG it appears as (2,2,3) i.e. in the a=b case. So in the b=c branch under WLOG a<b=c strictly... the s≥1 subcase yields a = b²−1 ≥ ... with a ≤ b: b² − 1 ≤ b impossible. So nothing — but my derivation above got a=3 > b=2, violating a≤b, correctly signaling no valid WLOG solution in that branch. To present cleanly: handle two-equal WITHOUT WLOG ordering subtleties by noting: if any two coordinates equal, by symmetry take a=b (permute). Then only a=b case needed! Since the condition is fully symmetric, "some two equal" ⟹ permute so that the equal pair is (a,b). Then solve a=b ⟹ (2,2,k) forms: (2,2,2),(2,2,3). Clean. ✓ (The b=c work in notes was redundant-but-harmless; I'll present the symmetric shortcut but keep a remark.)

  Actually hold on: with a=b, I should NOT assume c ≥ a... under WLOG it holds anyway. Fine: permute so equal pair is (a,b) and keep WLOG c largest — consistent since permutation can place the odd one out last. ✓

**Step 2**: Parity pattern elimination. All-distinct remains (Step 1 handled ties). Patterns by parity of (a,b,c) (sorted):
- c even ⟹ dead: c even ⟹ C = v₂(c+1) = 0. From identity (1): (b−a)(c+1) = 2^y − 2^z = 2^z(2^(y−z)−1), v₂ = z (y>z). So v₂(b−a) = z ⟹ 2^z | b−a. But 2^z = ca − b ≥ ... need 2^z > |b−a| = b−a: 2^z = ca − b. If a ≥ 3: ca − b ≥ 3c − b > c ≥ b > b − a? Hmm: 3c − b vs b − a: 3c − b − (b−a) = 3c + a − 2b ≥ 3c + a − 2c = c + a > 0 ✓ (using b ≤ c). So 2^z > b − a ⟹ contradiction with 2^z | b−a unless b−a = 0 — excluded (distinct). If a = 2: 2^z = 2c − b > b − 2 ⟺ 2c − b > b − 2 ⟺ 2c + 2 > 2b ⟺ c + 1 > b ✓ true. ✓ Dead. (Matches notes; note y>z needed — all-distinct ✓.)
  
  Wait, notes' version: "2ᶻ=ca−b≥b(a−1)>b>b−a（a≥3 时；a=2 时 2ᶻ=2c−b>b 亦然）". ca ≥ b·a only if c ≥ b ✓: ca − b ≥ ab − b = b(a−1) > b > b−a for a ≥ 3 ✓ cleaner. Use that.

- (O,E,O) [a odd, b even, c odd]: dead. Present BOTH kills? Use the slick one: identity (2): (c−b)(a+1) = 2^z − 2^x; c−b odd (c odd, b even), so v₂(LHS) = v₂(a+1) = A; RHS v₂ = x (y>... need z > x ✓ distinct) ⟹ x = A. Substitution: c = ab − 2^x into ca − b = 2^z: b(a²−1) = 2^x(2^(z−x) + a); v₂(LHS) = v₂(a²−1) (b even) = v₂(a−1) + A ≥ 1 + A; RHS: x + 0 = A (second factor odd: 2^(z−x) even + a odd). ⟹ v₂(a−1) = 0, contra a odd ⟹ v₂(a−1) ≥ 1. Dead. ✓ (Slicker than R2's squeeze; I'll include R2's squeeze as alternative remark or just use mine. Mine relies on identity (2) + substitution identity — both already in toolkit. Good.)
  
  Hmm wait, double check v₂(2^(z−x) + a) odd: z > x in all-distinct ✓. And v₂(RHS) = x + v₂(2^(z−x)+a) = x + 0 ✓. And v₂(LHS): b even ⟹ ≥ 1... total: v₂(b) + v₂(a²−1). So x = v₂(b) + v₂(a−1) + A. And x = A ⟹ v₂(b) + v₂(a−1) = 0. But b even ⟹ v₂(b) ≥ 1. Even stronger/simpler — contradiction right there! Don't even need a odd. ✓✓ 

- Remaining all-distinct patterns: (E,E,O) and (O,O,O). (Patterns (E,O,?): (E,O,E) has c even dead; (O,E,O) dead; so yes only EE0, OOO remain among distinct-parity triples. Enumerate 8 patterns: EEE✗(c even), EEO ✓open, EOE ✗, OEE ✗, EOO: c odd! (E,O,O) — wait did we handle (E,O,O)?? Patterns: (a,b,c) parities. c even: EEE, OOE, EOE, OEE — all dead ✓. c odd: EEO, OOO, EOO, OEO. EOO: a even, b,c odd. OEO: dead above. Did anyone kill EOO?! Notes say "(E,E,O) 和 (O,O,O)" survive — implying EOO was handled... but where? Hmm! Notes section 一.4: "幸存模式只剩两个：(E,E,O)（a,b 偶 c 奇）和 (O,O,O)." But (E,O,O) = a even, b odd, c odd — is it dead? Let me think: it's NOT covered by c-even lemma (c odd here), not (O,E,O)... 

  Hmm wait — maybe by symmetry? NO — the parity pattern isn't permuted when we sort! Sorting fixes positions. Hmm, but wait: is EOO actually possible? Let me attack it directly with my substitution identity: b even? No wait EOO: a even, b odd, c odd. Substitute c = ab − 2^x into ca − b: b(a² − 1) = 2^x(2^(z−x) + a). LHS: b odd, a even ⟹ a² − 1 odd ⟹ v₂(LHS) = 0. RHS: x + v₂(2^(z−x) + a) = x + 0 (even + even = even!! a even here!). Hmm: 2^(z−x) even, a even ⟹ sum even ⟹ v₂ ≥ 1 ⟹ RHS v₂ = x + v₂(2^(z−x)+a) ≥ x + 1. So 0 ≥ x + 1 ⟹ x < 0. CONTRADICTION! EOO dead instantly! 

  Wait let me double-check: a even ⟹ ab even, ab − c = 2^x with c odd ⟹ 2^x odd ⟹ x = 0! Even simpler: x = 0 in EOO. Then z > x = 1... z ≥ 1: ca − b even ✓. Substitution: b(a²−1) = 2^z + 2^x a = 2^z + 2a·... x=0: b(a²−1) = 2^z(1 + 2^(z−... hmm let me redo: b(a²−1) = 2^z + 2^x a = 2^z + a (x=0). LHS odd·odd = odd. RHS: 2^z even (z ≥ 1) + a even = even. Odd = even CONTRADICTION. ✓ Dead, trivially.

  So EOO dies in one line. Why didn't notes mention it? Possibly R2 killed it and notes compressed... The notes' dead-list mentions "(O,E,O)" explicitly and "c偶的全部四种模式". EOO unaccounted — POSSIBLE GAP IN NOTES' CASE COVERAGE CLAIM. My substitution handles it. Let me also double check via the identity-(1)-style reasoning... whatever, the substitution argument is solid: a even, b odd, c odd, x = 0 (since ab−c = even−odd = odd = 2^x ⟹ x=0). Then from ca − b = 2^z: substitute c = ab − 1 (x=0): ca − b = a(ab−1) − b = a²b − a − b = 2^z. LHS: a²b even, −a even, −b odd ⟹ odd. But 2^z with z ≥ 1 is even (z ≥ 1 because ca − b = c·a − b = odd·even − odd = even, and it's positive... could ca−b = ... it's ≥ 2^z ≥ 2 > 0 ✓ even ⟹ z ≥ 1 ⟹ 2^z even). Odd = even. DEAD ✓.

  Hmm wait, but actually I realize I should double-check the claim "notes survived only EE0/OOO" — maybe they considered EOO inside some other argument. Doesn't matter: my proof will cover ALL patterns explicitly. Full coverage list for all-distinct: EEE, EOE, OEE, OOE (c even) dead; EOO dead (odd=even); OEO dead (v₂ contradiction); EEO ⟹ (2,6,11); OOO ⟹ (3,5,7). COMPLETE.

**Step 3**: (E,E,O) ⟹ (2,6,11). Reuse notes' 2.1 (reverified): a,b even, c odd ⟹ x = v₂(c−b) + A, c−b odd (odd−even), A = 0 ⟹ x = 0 ⟹ c = ab − 1. Then:
  - 2^z = ca − b = a(ab−1) − b = a²b − a − b = b(a²−1) − a; 2^y = ab² − a − b = a(b²−1) − b.
  - Sum: 2^y + 2^z = ab² + a²b − 2a − 2b = (a+b)(ab − 2) ✓ [check: (a+b)(ab−2) = a²b + ab² − 2a − 2b ✓].
  - v₂(LHS) = z (T := 2^(y−z) ≥ 2 ⟹ T+1 odd). v₂((a+b)(ab−2)) = v₂(a+b) + 1 (ab ≡ 0 mod 4 since both even ⟹ ab − 2 ≡ 2 mod 4). ⟹ z = v₂(a+b) + 1.
  - Difference: 2^y − 2^z = (b−a)(c+1) = ab(b−a). v₂ = z + ... T − 1 odd ⟹ v₂(2^z(T−1)) = z. So z = v₂(ab(b−a)) = v₂(a) + v₂(b) + v₂(b−a).
  - p := v₂(a), q := v₂(b). If p < q: v₂(b−a) = p, v₂(a+b) = p ⟹ z = 2p + q and z = p + 1 ⟹ 2p + q = p + 1 ⟹ p + q = 1: impossible (p,q ≥ 1). Wait notes said "p+q+v₂(b−a)=v₂(a+b)+1 ⟹ 若 p<q 则两 v₂ 相等 = p ⟹ 2p+q=1 不可能". Hmm: p + q + p = p + 1 ⟹ 2p + q = 1?? p+q+p = p+1 ⟹ p + q = 1. Notes wrote 2p + q = 1 — hmm: p + q + v₂(b−a) with v₂(b−a) = p: total 2p + q. Set equal v₂(a+b) + 1 = p + 1: 2p + q = p + 1 ⟹ p + q = 1. Notes wrote "2p+q=1" which looks like a typo for p+q=1 (or they defined differently); either way impossible since p,q ≥ 1. ✓ (p=q=1 would give 2 ≠ 1.)
  - So p = q =: p₀. Write a = 2^p α, b = 2^p β, α < β odd.
  - z = v₂(a+b) + 1 = p + v₂(α+β) + 1. Also 2^z = a²b − a − b = 2^(3p)α²β − 2^p(α+β) = 2^p(2^(2p)α²β − (α+β)).
    - If v₂(α+β) =: v < 2p: v₂(factor) = p + v ⟹ z = 2p + v... wait v₂(2^p·X) = p + v₂(X); X = 2^(2p)α²β − (α+β): if v < 2p: X = 2^v(2^(2p−v)α²β − (α+β)/2^v) = 2^v(even... 2^(2p−v)α²β even since 2p−v ≥ 1; (α+β)/2^v odd) ⟹ bracket odd ⟹ v₂(X) = v ⟹ z = p + v ≠ p + v + 1 = v₂(a+b)+1. Contra ✓.
    - If v > 2p: X = 2^(2p)α²β − 2^v·odd' = 2^(2p)(α²β − 2^(v−2p)odd') ⟹ even − odd = odd ⟹ v₂(X) = 2p ⟹ z = 3p. But also z = p + v + 1 > p + 2p + 1 = 3p + 1 > 3p. Contra ✓.
    - So v = 2p exactly: α + β = 2^(2p)γ, γ odd; X = 2^(2p)(α²β − γ) ⟹ z = p + 2p = 3p... 
    
    wait: v₂(X) = 2p + v₂(α²β − γ). Hmm, need care: X = 2^(2p)(α²β − γ) exactly? X = 2^(2p)α²β − (α+β) = 2^(2p)α²β − 2^(2p)γ = 2^(2p)(α²β − γ) ✓ exact. So z = p + 2p + v₂(α²β − γ) = 3p + v₂(α²β − γ). And z = p + v + 1 = 3p + 1. ⟹ **v₂(α²β − γ) = 1**. Hmm — notes claim α²β − γ = 2 exactly. From v₂ = 1 we only get 2 | (α²β−γ), 4 ∤. Where does "= 2" come from? Notes: "现在用精确方程：2ᶻ=2^(3p)(α²β−γ) 结合 z=3p+1 立刻强制 (★) α²β−γ=2". That's wrong as stated?! Unless... hmm. Wait — maybe they use 2^z = 2^(3p)(α²β − γ) and z = 3p + 1 ⟹ α²β − γ = 2^(z−3p) = 2^1 = 2. OH RIGHT: 2^z EQUALS 2^(3p)(α²β−γ) as NUMBERS (exact equation, not valuation). So α²β − γ = 2^(z−3p) = 2^(3p+1−3p) = 2. ✓✓ Exact. Good — (★) holds: α²β − γ = 2.
    - Similarly 2^y = a b² − a − b: ab² = 2^(3p)αβ²; a+b = 2^p(α+β) = 2^(3p)γ·... wait 2^y = ab² − a − b = 2^(3p)αβ² − 2^p(α+β) = 2^(3p)αβ² − 2^(3p)γ = 2^(3p)(αβ² − γ) [using α+β = 2^(2p)γ]. And y = z + (y−z) with 2^(y−z) = T₁ ≥ 2... exact: y − z = d₁ ≥ 1 ⟹ 2^y = 2^(3p+1+d₁) ⟹ αβ² − γ = 2^(d₁+1) ✓ (★★).
  - Size finish: β = (γ+2)/α² ⟹ α³ < α²β = γ + 2 (α<β ⟹ α² < αβ ≤ α²β... careful: α < β ⟹ α² < αβ and αβ < β² hmm. α²β > α³ ⟺ α²β/α² = β > α ✓). So α³ ≤ γ + 1 (integers: α³ < γ+2 ⟹ α³ ≤ γ+1) ✓.
    - α + β = 2^(2p)γ ≥ 4γ (p ≥ 1). β = (γ+2)/α² ≤ γ + 2 (α² ≥ 1). So α = 2^(2p)γ − β ≥ 4γ − (γ+2) = 3γ − 2 ✓.
    - γ ≥ 3: α ≥ 3γ−2 ≥ 7 and α³ ≤ γ+1 ⟹ α ≤ (γ+1)^(1/3). Need 3γ−2 > (γ+1)^(1/3) for γ ≥ 3: at γ=3: 7 > 4^(1/3)≈1.59 ✓; monotonic ✓. Contradiction ✓.
    - γ = 1: α + β = 4 (p=1; p≥2 would need α+β = 16·odd... wait γ=1, α+β = 2^(2p)). α²β = 3 ⟹ (α,β) = (1,3): α²β = 3 ✓. Then α + β = 4 = 2^(2p) ⟹ p = 1. (a,b) = (2,6), c = 11 ✓.
    - γ odd, γ ≥ 5 covered by γ ≥ 3 case. What about γ = 2? γ odd required ✓ (γ = (α+β)/2^(2p), α+β even, γ odd by def since v = 2p exact... γ := (α+β)/2^(2p) is odd ✓).
    
  So (E,E,O) all-distinct ⟹ (2,6,11) ✓. (Notes' step-3 inequality "α≥4γ−(γ+2)" uses β ≤ γ+2: β = (γ+2)/α² and α² ≥ 1 ⟹ β ≤ γ+2 ✓.)

**Step 4**: (O,O,O) ⟹ (3,5,7) — MY NEW RESULT (chain above).

**Step 5**: Verify all four sorted triples; box the answer.

Also mention brute-force verification numerics.

One more sanity issue in Step 4: I use x = v₂(a²−1) AND the relation 2^z ≤ 2(c+1) from z = v₂(c²−1). Both derivations need y > z and z > x (strict) ✓ all-distinct. Also need b odd for v₂(b(c²−1)) = v₂(c²−1) ✓ OOO. Also the substitution identities require c = ab − 2^x which is definitional ✓.

Also potential edge: in Step 4 equality cascade, after getting 2^z = 2c+2, a=3, b=c−2: I should double-check that b stays > a i.e. c − 2 > 3 ⟹ c > 5: c = 7 ✓ consistent (no other c since 2^z = 2c+2 and x-force gives c=7 uniquely). Actually the uniqueness came from ab − c = 2^x = 8. Let me re-derive x=3: x = v₂(a²−1) = v₂(3²−1) = v₂(8) = 3 ✓. ab − c = 3(c−2) − c = 2c − 6 = 8 ⟹ c = 7 ✓. Unique. Then MUST verify (3,5,7) satisfies all three (done ✓).

Edge concern: in the equality cascade, we concluded a = 3 from 2^z = ca − b ≥ 3c − b — equality requires a = 3 ✓ (a odd ≥ 3). And b = c − 2 from b ≤ c − 2 ✓. And 2^z = 2(c+1) from upper bound: 2^(z−1) ≤ c+1 with equality ⟹ c+1 = 2^(z−1) ✓. But hold on — upper bound derivation: 2^(z−1) | (c−1 or c+1); if 2^(z−1) | c−1 then 2^(z−1) ≤ c−1 < c+1, strict. Overall 2^(z−1) ≤ c+1 always ✓. Equality 2^z = 2(c+1) forces 2^(z−1) = c+1 ✓ fine.

Everything solid. NOW: also reconcile — does (3,5,7) slip past any earlier "lemma" incorrectly claiming death? E.g., notes claimed size-chain kills OOO except Mersenne overlap. Whatever — those weren't proofs. Also the "比值公式" c = b(T₂a+1)/(T₂+a): check (3,5,7): T₂ = 2^(z−x) = 2^(4−3) = 2: c = 5(2·3+1)/(2+3) = 5·7/5 = 7 ✓.

Let me also reconsider whether x<z<y strict truly holds for (3,5,7): x=3 < z=4 < y=5 ✓.

Now, brute force code. Also verify no other solutions with a,b ≤ 1500 say (c unbounded via c = ab − 2^x construction... but careful: constructing c from the FIRST equation only — any true solution must have c = ab − 2^x for some x ≥ 0 with 2^x < ab, so scanning (a,b,power) catches ALL solutions with a,b in range regardless of c size ✓).

Efficiency: a ≤ b ≤ 1600: pairs ≈ 1.28M; each ~up to 22 powers (powers < ab ≤ 2.56M ⟹ ≤ 22). Inner work: compute c, filter c ≥ b, two power-checks. ≈ 2.8e7 iterations of light work — Python fine (~30–60s). Push to a,b ≤ 2500 (~5e7... maybe 2–4 min). Start with 2000. Also add numpy variant? Keep simple, measure.

Additional deep sweeps:
- EEO parametric: for even a up to 10⁶, z up to 84: b = (2^z + a)/(a² − 1) integer, even, > a, then c = ab − 1, check 2^y = a(b²−1) − b power of 2. Cost: sum over a of 84 ⟹ 4.2e7 divisions — heavy-ish pure Python; restrict a ≤ 2·10⁵ or vectorize. Actually smarter: for fixed a, need a² − 1 | 2^z + a. Meh, just loop with early skips: a even, a²−1 odd divisor... fine, do a ≤ 10⁵ (8.4e6 iters, OK).
- OOO parametric: for odd a, b: c = ab − 2^x... generic scan already covers a,b ≤ 2000; param deeper: for odd a ≤ 10⁵, odd... c determined by x: skip — proof is solid; generic scan suffices numerically.
- Two-equal parametric: trivial, covered.

Also quick independent check of EVERY found solution + permutations count = 16.

Let me write and run the code now. Then write 工作笔记.md updates progressively (per instructions: after each reasoning block, update working notes FIRST). I've already done major blocks: (1) read notes; (2) discovered (3,5,7) + full OOO kill; (3) EOO kill + OEO alt kill. I should write 工作笔记.md NOW before running experiments, then run brute force, then finalize proof.md.

Let me create 工作笔记.md with the four sections.

Then brute force, then proof.md.

One more consideration: the task says 分析笔记.md is in current directory but it's actually at rounds/round3/分析笔记.md — noted (matches R3 observer's environment note). I copied... no, I read it directly. Fine.

Also: "每完成一个推理块，立即追加写入工作笔记.md" — will do. And final deliverable proof.md with \boxed{...}.

Anti-cheating: I have not searched the web; all derivation is local + Python numeric checks. Numeric brute force is explicitly sanctioned (缺口0). No cheating risk declaration needed (no external solution content contacted). I'll state tools used honestly in proof.md preamble.

Let me now write 工作笔记.md.

Structure:
```
# 工作笔记.md · 轮次4·解题者

## 一、已确认结论
1. (O,O,O) 被杀：全异 (O,O,O) 唯一解 (3,5,7)。猜想解集不完整！
   [full chain]
2. 新增一击必杀：(E,O,O) 死（奇=偶矛盾）
3. (O,E,O) 替代证法（更短）
4. 解集更新：{(2,2,2),(2,2,3),(2,6,11),(3,5,7)} 全置换，共 16 个有序三元组。

## 二、正在做
- 缺口0 暴力搜索验证中。

## 三、死路记录
- （继承 R3 清单全部条目）
- 本轮新增死路：无（新增的都是活路/杀招）。备注：我中途把 T₁ 约束错误展开成 b≥2a（正确为 b(b−2a+2)≥a），已弃用，未进入最终证明。
- R3 笔记 §2.1 中"2p+q=1 不可能"应为 p+q=1 不可能（笔误不影响结论）。

## 四、下一步
- 跑暴力搜索核对四元解集；
- 写 proof.md（结构：WLOG/坐标≥2 → 两相等 → c偶四模式+EOO+OEO 三连杀 → EEO 定理 → OOO 定理 → 验证与装箱）。
```

Then run code. Then proof.md.

Actually wait, I want to double-check the (E,O,O) kill once more very carefully since notes never mentioned it — is (E,O,O) really forced x=0? a even, b odd, c odd: ab − c = even − odd = odd. Positive power of 2 and odd ⟹ = 1 ⟹ x = 0 ✓. Then ca − b = 2^z: c·a − b = odd·even − odd = even − odd = odd. So 2^z odd ⟹ z = 0!! But z ≥ x = 0 and strict z > x in all-distinct... wait all-distinct gives x < z. z = 0 = x contradiction ALREADY. Even simpler!! ca − b is ODD (even·odd − odd), so 2^z is odd, z = 0, but x < z requires z ≥ 1. DEAD. Beautiful — one line: parity of ca−b is odd ⟹ z=0=x contra strictness.

Hmm wait but hold on: ca − b odd ⟹ 2^z = 1 ⟹ ca − b = 1 ⟹ z = 0. And x = 0. x < z fails. But wait — is x < z guaranteed? Only in all-distinct case ✓ (we're in all-distinct after step 1). But actually also check bc − a: odd·odd − even = odd − even = odd ⟹ y = 0 too! So all of x=y=z=0: ab−c = bc−a = ca−b = 1. Then ab−c = ca−b ⟹ b(a−c) = c − b·... ab − c = ca − b ⟹ ab − ca = c − b ⟹ a(b−c) = c−b = −(b−c) ⟹ (a+1)(b−c) = 0 ⟹ b = c. Contradiction with distinct. DEAD ✓ multiple ways.

So (E,O,O): ab−c odd ⟹ x=0; bc−a odd ⟹ y=0; ca−b odd ⟹ z=0; but x<y<z... x<z<y strict ⟹ contradiction immediately. ONE LINE. 

Similarly sanity: (O,O,O) all three expressions even ✓ consistent. (E,E,O): ab−c even−odd=odd ⟹ x=0 ✓ (matches known x=0!), bc−a: odd... b even c odd: bc even − a even = even ⟹ y ≥ 1 ✓, ca−b: odd·even − even = even ⟹ z ≥ 1 ✓. Good: x=0<z<y consistent.

(O,E,O): ab−c: odd·even − odd = odd ⟹ x = 0!! Wait — that contradicts my earlier statement that (O,E,O) needs x = A ≥ 1... Let me recheck: a odd, b even: ab even; ab − c = even − odd = odd ⟹ x = 0. Then z > x = 0: ca − b = odd − even = odd ⟹ z = 0 TOO. CONTRADICTION INSTANTLY. WHAT?! (O,E,O) dies in TWO LINES by pure parity!? Then R2's elaborate squeeze was unnecessary?! Let me recheck: (O,E,O) = a odd, b even, c odd. ab − c: a·b = odd·even = even. even − c = even − odd = odd ✓. So ab − c odd ⟹ = 1, x = 0. ca − b: c·a = odd·odd = odd; odd − b = odd − even = odd ⟹ z = 0. But x < z strict (distinct coords) ⟹ 0 < 0 false. DEAD. ✓✓ 

Wow. OK so R2's squeeze kill was correct but heavy machinery; parity alone does it. (Unless x<z<y strictness... yes all-distinct established. And if not distinct, step 1 handled.) Good — simpler is better; I'll present parity kills prominently. But note: my earlier "substitution" kill of OEO also valid; parity kill is cleaner.

Recheck (E,E,O) x=0 consistent: x=0, z ≥ 1, y ≥ z... fine ✓.
Recheck (O,O,O): all even ✓ no instant kill ✓.
Recheck c-even patterns with parity lens: (E,E,E): all even ✓ no kill; killed by 2^z|b−a lemma ✓. (O,O,E): ab−c = odd−even = odd ⟹ x=0; bc−a = odd·odd... b odd c even: bc even − a odd = odd ⟹ y = 0; but x<y strict ⟹ dead INSTANTLY too! (E,O,E): ab−c = even−odd = odd ⟹ x = 0; ca−b = odd−odd... c even a even: ca even − b odd = odd ⟹ z = 0 < ... x<z dead ✓ instantly. (O,E,E): ab − c = even − even = even; bc − a = even·even... b even c even: bc even − a odd = odd ⟹ y = 0; but y is the MAXIMUM ⟹ x<z<y<...y=0 impossible ✓ instantly dead. (E,E,E) is the only c-even pattern needing the real lemma ✓ (all three expressions even).

So updated kill map (all-distinct):
- (E,E,E): needs v₂ lemma (c even) ✓
- (E,E,O): open ⟹ (2,6,11)
- (E,O,E): parity instant kill (x=z=0)
- (E,O,O): parity instant kill (x=y=z=0)
- (O,E,E): parity instant kill (y=0 max)
- (O,E,O): parity instant kill (x=z=0)
- (O,O,E): parity instant kill (x=y=0)
- (O,O,O): needs my new argument ⟹ (3,5,7)

VERY clean now. The whole proof structure:
0. WLOG, no-1, ordering lemma, two-equal done.
1. Parity dispatch: 5 of 8 patterns die instantly (all except EEE, EEO, OOO).
2. (E,E,E) dies by 2^z | (b−a) > 0 size lemma.
3. (E,E,O) ⟹ (2,6,11) [R1/R2/R3 chain].
4. (O,O,O) ⟹ (3,5,7) [NEW].

Beautiful. Let me also double check (E,E,E) lemma needs y > z (strict) ✓ all-distinct, and a ≥ 3 for size (a even ≥ 2; a=2 handled separately as in notes: 2^z = 2c − b > b − 2 > b − a = b − 2 hmm: b − a = b − 2 and 2c − b vs b − 2: 2c − b − (b−2) = 2c − 2b + 2 = 2(c−b+1) ≥ 2·3 = 6 > 0 ✓ since c > b ⟹ c − b ≥ 2 ⟹ 2(c−b+1) ≥ 6. So 2^z > b − a ✓.) For a ≥ 4 (even): 2^z = ca − b ≥ ab − b = b(a−1) ≥ 3b > b − a ✓.

Wait a ≥ 4 even: a−1 ≥ 3 ✓. a=2 separate ✓. Good.

Hmm, actually also for (O,O,E): x = 0, y = 0: but x < y strict needed... all-distinct gives x < z < y so y=0 impossible ✓ dead.

Now also — IMPORTANT — recheck the two-equal case conclusion under the lens of (3,5,7) discovery: no interference ✓.

AND: could there be all-distinct solutions where some expression equals... all powers ≥ 1 ✓ handled.

Potential remaining worry: the problem says "正整数三元组" — positive integers, order matters? "找出所有正整数三元组 (a,b,c)" — typically unordered-up-to-permutation presentation "及它们的全部置换". We'll present sorted representatives + note permutations. Total 16 ordered triples (1+3+6+6).

Now let me also prepare the brute force to ALSO test a,b ranges beyond 2000 via the parametric constructions, and validate counts.

Code sketch:

```python
import sys

def pow2(n):
    return n > 0 and (n & (n - 1)) == 0

sol = []
LIM = 2000
for a in range(2, LIM+1):
    ab_base = a*a  # b starts at a
    for b in range(a, LIM+1):
        ab = a*b
        p = 1
        while p < ab:
            c = ab - p
            if c >= b:
                if pow2(b*c - a) and pow2(c*a - b):
                    sol.append((a,b,c))
            p <<= 1
print(sol)
```

Wait — subtle: scanning p over ALL powers < ab with c = ab − p ≥ b: this enumerates every candidate satisfying first equation. Every true solution (a,b,c) sorted has ab − c = 2^x < ab ✓ and c ≥ b ✓. Complete for a,b ≤ LIM, ANY c. 

Estimated ops: pairs (a≤b≤2000): ~2×10⁶; powers per pair ~ log₂(ab) ≤ 22, avg maybe 19 ⟹ ~3.8×10⁷ inner iterations, each: subtraction, comparison, sometimes two pow2 calls. Python: ~1–2 minutes. Acceptable. Maybe use PyPy-style micro-opt: precompute nothing special. Fine.

Then parametric EEO deep scan:
```python
# EEO: c = ab - 1, a even <= A_LIM, find b even > a: 2^z = b(a^2-1) - a power of 2, then check y-cond
found_eeo = []
for a in range(2, 200001, 2):
    m = a*a - 1
    # b = (2^z + a)/m
    z = 1
    pz = 2
    while pz.bit_length() < 90:
        num = pz + a
        if num % m == 0:
            b = num // m
            if b > a and b % 2 == 0:
                c = a*b - 1
                if pow2(a*b*b - a - b):
                    found_eeo.append((a,b,c))
        pz <<= 1
```
Hmm z from 1..89 ⟹ 100000 × 89 ≈ 9e6 iterations OK. But actually for a ≥ 4, m = a²−1 > a+... 2^z + a ≥ 2^z; b > a needs 2^z > a·m ≈ a³ ⟹ z > 3log₂a; loop fine anyway.

Hmm wait, but actually for EEO we also need x=0 i.e. c=ab−1 forced — yes shown. And b even, a even, α,β... whatever, scan is safe.

OOO deep parametric: for odd a ≤ A_LIM, odd b: c = ab − 2^x... that's the generic scan restricted; deeper: for odd a ≤ 10⁵ and each x with 2^x < a² (b ≥ a): b = (2^x + c)/a unknown c... two unknowns; instead use 2^z = b(a²−1) − 2^x a + ... hmm from b(a²−1) = 2^z + 2^x a: for odd a, x = v₂(a²−1) FORCED (my theorem!): so 2^z = b(a²−1) − 2^x a with x = v₂(a²−1): for each odd a ≤ 10⁵: x known; b = (2^z + 2^x·a)/(a²−1) for z > x: enumerate z up to 90: b integer odd > a ⟹ then check remaining conds (y power of 2, and x=v₂(b²−1)). Cheap: 10⁵ × ~60 = 6e6·(bigint div) — okay maybe a ≤ 3·10⁴. This numerically confirms OOO uniqueness beyond generic scan range. 

Also two-equal parametric trivial: a=b=2^u, c=2^v+1, check a²−c power: covered by generic scan anyway (a=b ≤ 2000).

Alright, run generic scan first.

After that, write proof.md. Length target: complete but tight. Include:
- 作弊风险声明? Required ONLY if contacted external content. I didn't search. State: "本证明全程未使用外部搜索；数值实验为本目录内 Python。" Maybe include a short "工具与合规声明" noting no external sources contacted, hence no cheat-risk declaration triggered. Good transparency.

- Sections:
  1. 记号与初等归约 (WLOG, ≥2, ordering, x≤z≤y, strictness)
  2. 两相等情形
  3. 奇偶模式总dispatch（含 EEE 引理）
  4. (E,E,O) 定理
  5. (O,O,O) 定理 (NEW)
  6. 数值验证附录
  7. 结论 \boxed{}

Let me make sure every step in sections 4–5 is airtight when written.

Section 1 details:
- If some coord = 1, say a (after permute min): a=1 ⟹ ca − b = c − b ≤ 0 (as b ≤ c); power of 2 positive ⟹ c > b impossible ⟹ c = b ⟹ ca − b = 0 ∉ powers. So all ≥ 2. (Careful: powers of 2 here are 2^x ≥ 1 > 0 ✓.)
- Ordering lemma: x ≤ z ≤ y; equalities ⟺ b=c, a=b resp. Proof: differences (c−b)(a+1) ≥ 0, (b−a)(c+1) ≥ 0 ✓. Corollary: distinct coords ⟺ x < z < y.
- Distinctness from here (step 2 handled ties): a < b < c.

Section 2 (ties): permute equal pair to (a,b) [symmetry], WLOG c ≥ a: a=b ⟹ bc−a = ca−b ⟹ y = z... anyway: a(c−1) = 2^y ⟹ a = 2^u, c − 1 = 2^v. ab − c = 2^(2u) − 2^v − 1 = 2^x. v ≥ 1: LHS odd ⟹ x = 0 ⟹ 2^(2u) − 2^v = 2 ⟹ 2^v(2^(2u−v) − 1) = 2 ⟹ v = 1 ∧ 2u − 1 = 1... wait 2^v(2^(2u−v)−1) = 2: since second factor odd ≥ 1: v = 1, 2^(2u−1) − 1 = 1 ⟹ 2u − 1 = 1 ⟹ u = 1 ⟹ a = 2, c = 3: (2,2,3) ✓ (c=3 ≥ a=2 ✓). v = 0: c = 2 ≤ b = a ⟹ a = b = 2 (ordering) ⟹ (2,2,2) ✓. Done.

Hmm wait v=0 case: c = 2^0 + 1 = 2; b = a ≤ c = 2 and a ≥ 2 ⟹ a = 2 ✓ (2,2,2).

Section 3: parity dispatch table with one-line kills + EEE lemma:
- Table: for each pattern list parities of (ab−c, bc−a, ca−b) and which of x,y,z become 0, conclude.
  - EEE: all even — no parity kill ⟹ lemma below.
  - EEO: (odd, even, even): x=0 only — survives ⟹ section 4.
  - EOE: (odd, even, odd): x=0 ∧ z=0 contra x<z. dead.
  - EOO: (odd, odd, odd): x=y=z=0 contra x<z<y. dead. [also direct: all three odd ⟹ all = 1 ⟹ b=c via ab−c=ca−b... the x<z<y contradiction suffices]
  - OEE: (even, odd, even): y=0 contra y max. dead.
  - OEO: (odd, odd, odd)?? wait recompute: a odd b even c odd: ab − c = even − odd = odd; bc − a = even·