Let me start by reading the analysis notes file.The file isn't found. Let me check the working directory.The `分析笔记.md` isn't in the working directory root, but the latest round (round5) has one: `/private/tmp/p275-1962-v2/rounds/round5/分析笔记.md`. The prompt says it's in the current working directory, but actually it seems the latest observer's notes are in rounds/round5/分析笔记.md. Let me read that. Also there might be a 工作笔记.md somewhere — let me check. The find output doesn't show a 工作笔记.md. So I need to create one in the current working directory presumably.

Let me read the round5 分析笔记.md first.The analysis notes say the math is fully closed: 8 parity cases all closed. The remaining task is to write proof.md, referencing:

1. Equal-coordinates case: only (2,2,2) and (2,2,3) — from R3笔记§一1
2. EEE lemma — R3笔记§一2 + a=2 supplement
3. Five parity kills — §2.2
4. EEO theorem — R3笔记§2.1 (need to copy verbatim)
5. OOO theorem — §2.3 five steps

I need to read the R3 notes to get the details for the equal-coordinate case, EEE lemma, and EEO theorem. Let me read rounds/round3/分析笔记.md.Now I have all the material I need. The math is fully closed according to the notes. My job:

1. Write 工作笔记.md (four sections: confirmed conclusions / currently doing / dead ends / next steps) — update as I go.
2. Verify the key steps independently (the notes recommend self-check of EEO step 2 Case analysis and OOO step 4 equality conditions).
3. Write proof.md with the complete proof, ending with \boxed{...}.

Let me first do some independent verification:

1. Machine check: brute force to confirm the four solutions (already done by R5, but I should re-run quickly myself as verification — it's cheap).
2. Verify each logical step of the proofs myself.

Let me carefully re-derive everything to make sure the proof is airtight.

**Setup**: Find all positive integer triples (a,b,c) such that ab−c, bc−a, ca−b are all powers of 2 (including 2⁰=1).

**Step 0: WLOG and basics.**
- The conditions are symmetric under permutations of (a,b,c): ab−c, bc−a, ca−b permute correspondingly. Indeed if we swap a and b: ba−c = ab−c stays; ac−b = ca−b; cb−a = bc−a. So the set {ab−c, bc−a, ca−b} is invariant. So WLOG a ≤ b ≤ c.
- Coordinates ≥ 2: Suppose a = 1. Then b·1 − c = b − c is a power of 2, and c·1 − b = c − b is also a power of 2. These are negatives of each other; both must be positive powers of 2... wait, "power of 2" — do we allow negative? No: powers of 2 are positive (2^k for k ≥ 0). So b − c ≥ 1 and c − b ≥ 1, contradiction since they're negatives. Actually b − c = −(c − b); both must be ≥ 1 > 0 — impossible. Good.
- Also note all three values ab−c etc. must be ≥ 1 (positive).

**Notation**: ab − c = 2ˣ, bc − a = 2ʸ, ca − b = 2ᶻ with x,y,z ≥ 0 integers.

**Ordering lemma** [R1]:
- ca − b − (ab − c) = ca − b − ab + c = a(c−b) + (c − b) = (c−b)(a+1) ≥ 0 since c ≥ b, a+1>0. So z-exponent value 2ᶻ ≥ 2ˣ, i.e., x ≤ z.
- bc − a − (ca − b) = bc − a − ca + b = c(b−a) + (b − a) = (b−a)(c+1) ≥ 0. So y ≥ z.
- Hence x ≤ z ≤ y.
- Equality analysis: 2ᶻ = 2ˣ iff (c−b)(a+1) = 0 iff c = b. Similarly 2ʸ = 2ᶻ iff b = a. So in the case all distinct, x < z < y strictly; and equal coordinates force corresponding exponent equalities.

Wait — careful: the note says "两两相等当且仅当坐标有相等" (pairwise equality of exponents iff coordinates have equality). Let me restate: 2ˣ = 2ᶻ ⟺ c = b; 2ᶻ = 2ʸ ⟺ a = b; 2ˣ = 2ʸ ⟺ ... 2ʸ − 2ˣ = (c−a)(b+1) [identity (3)], so 2ˣ=2ʸ ⟺ c=a. With ordering a≤b≤c, a=c forces all equal. OK.

So:
- If two or three coordinates are equal, we handle separately.
- If all distinct, then x < z < y strictly.

**Case A: some two coordinates equal.**

Sub-case a = b: Then bc − a = ac − a = a(c−1), and ca − b = ac − b = ac − a = a(c−1). Wait: bc − a with b = a gives ac − a = a(c−1). And ca − b = ca − a = a(c−1). Yes both equal. So 2ʸ = a(c−1) means a(c−1) = 2ʸ, so a = 2ᵘ and c − 1 = 2ᵛ with u+v = y (both nonneg). Then ab − c = a² − c = 2²ᵘ − 2ᵛ − 1 = 2ˣ.
  - If v ≥ 1: 2²ᵘ − 2ᵛ is even, so LHS odd, so 2ˣ = 1, x = 0: 2²ᵘ − 2ᵛ = 2, i.e., 2ᵛ(2^(2u−v) − 1) = 2. Since v≥1 and the factor (2^(2u−v) − 1) is an odd positive integer (need 2u − v ≥ 1 for it to be positive... actually need 2u ≥ v for positivity; if 2u < v then negative, not a power of 2 unless... let's just solve): 2ᵛ · odd = 2 ⟹ v = 1 and 2^(2u−v) − 1 = 1 ⟹ 2u − v = 1 ⟹ u = 1. So a = 2, c = 2¹ + 1 = 3. Triple (2,2,3). Check: ab − c = 4 − 3 = 1 ✓, bc − a = 6 − 2 = 4 ✓, ca − b = 6 − 2 = 4 ✓.
  - If v = 0: c = 2. Since a = b ≤ c = 2 and a ≥ 2, a = b = 2. Triple (2,2,2). Check: all expressions equal 2. ✓

Sub-case b = c (with a < b since all-distinct handled elsewhere; here a ≤ b = c): Then ab − c = ab − b = b(a−1) = 2ˣ, so b = 2ᵗ, a − 1 = 2ˢ (s,t ≥ 0). Note a ≥ 2 so s ≥ 0 fine; if s = 0, a = 2.
  - s = 0: a = 2, b = c = 2ᵗ. Then bc − a = 2^(2t) − 2 = 2(2^(2t−1) − 1) = 2ʸ. For t ≥ 1: 2^(2t−1) − 1 is odd, so 2ʸ = 2 · odd ⟹ y = 1 and 2^(2t−1) − 1 = 1 ⟹ t = 1 ⟹ b = c = 2: (2,2,2). If t = 0, b = 1 contradiction (b ≥ 2). Good.
  - s ≥ 1: a odd. Then bc − a = b² − a is odd (even minus odd)... wait b = c = 2ᵗ with t ≥ 1? Hmm, b = 2ᵗ and b ≥ 2 so t ≥ 1, so b even, b² even, a odd ⟹ b² − a odd ⟹ 2ʸ odd ⟹ y = 0 ⟹ b² − a = 1 ⟹ a = b² − 1 = 2^(2t) − 1. But also ab − c = b(a−1) = 2ᵗ(2^(2t) − 2) = 2^(t+1)(2^(2t−1) − 1) = 2ˣ requires 2t − 1 = 1 ⟹ t = 1. Then a = 3, b = c = 2: triple (3,2,2). Check: ab − c = 6 − 2 = 4 ✓, bc − a = 4 − 3 = 1 ✓, ca − b = 6 − 2 = 4 ✓. This is a permutation of (2,2,3).

Sub-case a = c: with a ≤ b ≤ c, a = c forces all equal — covered by a=b and b=c anyway.

Hmm wait, in sub-case a=b, I should double check the possibility u could be such that 2u − v ≤ 0. From 2ᵛ(2^(2u−v) − 1) = 2 with v ≥ 1: if 2u − v ≤ 0, then 2^(2u−v) − 1 ≤ 0, LHS ≤ 0 ≠ 2. So indeed 2u − v ≥ 1, odd factor ≥ 1. Fine. And v = 0 case: c = 2 ≥ b = a, and a ≥ 2, so a = 2. Good.

Also note: in sub-case a=b with v ≥ 1 we got c = 3 > a = 2 consistent with ordering. Good.

**Case B: all distinct.** Then x < z < y strictly.

**Step B1: parity dispatch.** Each of ab−c, bc−a, ca−b is either even (exponent ≥ 1) or odd (= 1, exponent 0). Compute parities:
- ab − c odd ⟺ ab and c have different parity.
- Let me tabulate by parity pattern of (a,b,c):

(E,E,E): ab even, c even ⟹ ab−c even. Similarly all three even. So x,z,y ≥ 1.
(E,E,O): ab−c: even − odd = odd ⟹ x = 0. bc − a: even·odd − even = even − even = even ⟹ y ≥ 1. ca − b: odd·even − even = even ⟹ z ≥ 1.
(E,O,E): ab − c: even·odd − even = even ⟹ x ≥ 1. bc − a: odd·even − odd = odd ⟹ y = 0. ca − b: even·even − even = even ⟹ z ≥ 1. But x<z<y needs y largest; y = 0 while x ≥ 1 contradicts x < y. Dead.
(E,O,O): ab − c: even − odd = odd ⟹ x = 0. bc − a: odd·odd − odd = even ⟹ y ≥ 1. ca − b: odd·odd − odd = even ⟹ z ≥ 1. All three: x=0, y,z ≥1. Need x<z<y: x=0 possible. Hmm wait, the R5 table says "(E,O,O) 死：三式全奇 ⟹ x=y=z=0". That contradicts my computation. Let me redo.

Hold on. (E,O,O): a even, b odd, c odd.
- ab − c = even·odd − odd = even − odd = odd. So x = 0.
- bc − a = odd·odd − even = odd − even = odd. So y = 0.
- ca − b = odd·even − odd = even − odd = odd. So z = 0.
All three odd! Yes — because in each product exactly one factor is odd... wait no. ab has a even so ab even; c odd ⟹ ab − c odd. bc: b,c both odd ⟹ bc odd; a even ⟹ odd − even = odd. ca: c odd, a even ⟹ ca even; b odd ⟹ even − odd = odd. Yes all three odd. So x=y=z=0, contradicting strict order x<z<y. Dead. My first pass was wrong; the note is right.

(O,E,E): a odd, b even, c even.
- ab − c: odd·even − even = even ⟹ x ≥ 1.
- bc − a: even·even − odd = odd ⟹ y = 0.
- ca − b: even·odd − even = even ⟹ z ≥ 1.
y = 0 but y should be max. Contradiction with x<z<y (x ≥ 1 > 0 = y). Dead.

(O,E,O): a odd, b even, c odd.
- ab − c: odd·even − odd = odd ⟹ x = 0.
- bc − a: even·odd − odd = odd ⟹ y = 0.
- ca − b: odd·odd − even = even ⟹ z ≥ 1.
x = z = 0 violates x < z. Dead.

(O,O,E): a,b odd, c even.
- ab − c: odd − even = odd ⟹ x = 0.
- bc − a: even − odd = odd ⟹ y = 0.
- ca − b: even − odd = odd ⟹ z = 0.
x = y = 0 violates x < y. Dead.

(E,E,E): all exponents ≥ 1. Survives to Step B2.
(E,E,O): x = 0, y,z ≥ 1. Survives (consistent with x < z < y as x=0 < z).
(O,O,O): a,b,c all odd: ab − c = odd − odd = even, similarly all even. x,y,z ≥ 1. Survives to its own theorem.

Good, matches the table.

**Step B2: kill (E,E,E) — the c-even lemma.**
If c even, then C := v₂(c+1) = 0 (c+1 odd). From identity (1): (b−a)(c+1) = 2ʸ − 2ᶻ. Hmm, the R3 note says: "c 偶 ⟹ C=0 ⟹ v₂(b−a)=z". Let me verify which identity gives that. We have identities:
(1) (b−a)(c+1) = 2ʸ − 2ᶻ
(2) (c−b)(a+1) = 2ᶻ − 2ˣ
(3) (c−a)(b+1) = 2ʸ − 2ˣ

From (1): v₂((b−a)(c+1)) = v₂(2ʸ − 2ᶻ) = z + v₂(2^(y−z) − 1) = z + 0 = z (since y > z in the all-distinct case, 2^(y−z) − 1 is odd). So v₂(b−a) + C = z; C = 0 gives v₂(b−a) = z, i.e., 2ᶻ | b − a.

But wait: b > a in all-distinct case, so b − a ≥ 1 and 2ᶻ | b−a means 2ᶻ ≤ b − a. On the other hand 2ᶻ = ca − b ≥ ... we need 2ᶻ > b − a always. 2ᶻ = ac − b. Since a ≥ 2, c ≥ b+2 (all distinct with same parity? In EEE case c ≥ b + 2 as both even; but let's do general):
- General claim: ac − b > b − a, i.e., ac + a > 2b, i.e., a(c+1) > 2b.
  - If a ≥ 3 (any parity): a(c+1) ≥ 3(b+1) = 3b + 3 > 2b. ✓.
  - If a = 2: a(c+1) = 2c + 2 vs 2b: need 2c + 2 > 2b ⟺ c > b − 1 ⟺ c ≥ b, true (strictly c > b in all-distinct). ✓.
So 2ᶻ = ac − b > b − a ≥ 2ᶻ when 2ᶻ | b−a and b−a ≥ 1... wait more precisely: 2ᶻ | (b−a) and b−a ≥ 1 implies b−a ≥ 2ᶻ. Combined with ac − b > b − a: 2ᶻ = ac − b > b − a ≥ 2ᶻ, contradiction. 

Actually hold on: the R5 version says "a≥4 用 b(a−1)>b−a；a=2 时 2ᶻ=2c−b>b−a 因 c−b≥2". Slightly different bound but same idea; mine works generally. Let me double-check a=2 case in my formulation: a(c+1) = 2(c+1) = 2c+2 > 2b ⟺ c + 1 > b ⟺ c ≥ b, and since c > b (distinct), true. And a ≥ 3: a(c+1) ≥ 3(c+1) and c ≥ b+1 ⟹ 3(c+1) ≥ 3b + 3 > 2b. ✓. Great, uniform proof.

This kills all four patterns with c even: (E,E,E), (O,O,E), (E,O,E)? Wait (E,O,E) was already killed by parity (y=0). (O,E,E) killed by parity too. So c-even lemma additionally kills (E,E,E) and (O,O,E). (O,O,E) was already killed by parity (x=y=0). So effectively this lemma is only needed for (E,E,E). Fine — still cleanest to state it once for all c-even patterns.

**Step B3: kill (O,E,O)** — already done by parity (x=z=0). The squeeze argument is optional. Parity suffices: x = z = 0 contradicts x < z. Good, simpler.

Wait, but actually I realize the parity kills handle five patterns; c-even lemma handles EEE; remaining: (E,E,O) and (O,O,O). 

**Step B4: (E,E,O) theorem.** a,b even, c odd, all distinct, a<b<c.

First: c odd. From identity (2): (c−b)(a+1) = 2ᶻ − 2ˣ. v₂: v₂(c−b) + A = z + v₂(2^(z−x) − 1) = z (since z > x). With A = v₂(a+1) = 0 (a even ⟹ a+1 odd): v₂(c−b) = z. Hmm, but the R2 reduction said "A=B=0, c−b 奇 ⟹ x=v₂(c−b)+A=0 ⟹ c=ab−1".

Hmm wait, that's a different relation. Let me recompute. Which identity involves x on the RHS with (c−b)? Identity (2): 2ᶻ − 2ˣ = (c−b)(a+1). v₂(LHS) = x + v₂(2^(z−x) − 1) = x (z > x ⟹ odd factor). So x = v₂(c−b) + v₂(a+1) = v₂(c−b) + 0. Since c odd, b even: c − b odd ⟹ v₂(c−b) = 0 ⟹ x = 0. So 2ˣ = 1: ab − c = 1 ⟹ **c = ab − 1**. ✓ matches R2.

Then:
2ᶻ = ca − b = (ab−1)a − b = a²b − a − b = b(a² − 1) − a.
2ʸ = bc − a = (ab−1)b − a = ab² − b − a = a(b² − 1) − b.

Both must be powers of 2. Note z ≥ 1 (from parity: ca−b even), y ≥ 1.

**Claim 1: v₂(a) = v₂(b) =: p.**

Sum: 2ʸ + 2ᶻ = a²b + ab² − 2a − 2b = (a+b)(ab − 2). Check: (a+b)(ab−2) = a²b + ab² − 2a − 2b ✓.
v₂(LHS): y > z ≥ 1, so 2ʸ + 2ᶻ = 2ᶻ(2^(y−z) + 1), and 2^(y−z) + 1 is odd (y−z ≥ 1). So v₂(LHS) = z.
v₂(RHS) = v₂(a+b) + v₂(ab−2). a,b even ⟹ ab ≡ 0 mod 4 ⟹ ab − 2 ≡ 2 mod 4 ⟹ v₂(ab−2) = 1. So z = v₂(a+b) + 1. (**)

Difference: 2ʸ − 2ᶻ = (b−a)(c+1) [identity (1)]. Check: c + 1 = ab. So 2ʸ − 2ᶻ = (b−a)·ab. v₂: y > z ⟹ v₂(2ʸ − 2ᶻ) = z. So z = v₂(ab) + v₂(b−a) = p + q + v₂(b−a) where p = v₂(a), q = v₂(b). (***)

From (**) and (***): p + q + v₂(b−a) = v₂(a+b) + 1.
- If p < q: v₂(b−a) = v₂(2ᵖ(2^(q−p)β − α)) where a = 2ᵖα, b = 2^q β odd parts: b − a = 2ᵖ(2^(q−p)β − α), inner is odd − odd = even? No wait: 2^(q−p)β is even (q>p), α odd ⟹ even − odd = odd. So v₂(b−a) = p. And a+b = 2ᵖ(α + 2^(q−p)β), odd + even = odd ⟹ v₂(a+b) = p. So equation: p + q + p = p + 1 ⟹ q + p = 1. But p,q ≥ 1 (a,b even), impossible.
- If p > q: symmetric, v₂(b−a) = q, v₂(a+b) = q ⟹ p + q + q = q + 1 ⟹ p = 1 − q ≤ 0, impossible.
Hence p = q. ✓

(Note: R3's note had a typo "2p+q=1"; correct is p+q=1 as fixed in §五 of R5 notes.)

**Claim 2: parametrization.** Write a = 2ᵖα, b = 2ᵖβ, α < β odd.
z = v₂(a+b) + 1 = p + v₂(α+β) + 1.
Also 2ᶻ = b(a²−1) − a = 2ᵖβ(2^(2p)α² − 1) − 2ᵖα = 2ᵖ[2^(2p)α²β − β − α] = 2ᵖ[2^(2p)α²β − (α+β)].
Let v = v₂(α+β). Bracket N = 2^(2p)α²β − (α+β).
- If v < 2p: α+β = 2ᵛγ' γ' odd, N = 2ᵛ[2^(2p−v)α²β − γ'], inner even − odd = odd ⟹ v₂(N) = v ⟹ z = p + v. But (**) gave z = p + v + 1. Contradiction.
- If v > 2p: N = 2^(2p)[α²β − 2^(v−2p)γ'], inner odd − even = odd ⟹ z = p + 2p = 3p. But z = p + v + 1 ≥ p + 2p + 2 = 3p + 2 > 3p. Contradiction. 

Hmm wait: v ≥ 2p + 1 ⟹ z = p + v + 1 ≥ 3p + 2. And computed z = 3p. Contradiction indeed. But R3's note says "括号内=偶减奇=奇" — hmm, in their notation bracket = 2^(2p)α²β − (α+β); if v > 2p, both terms divisible by 2^(2p), factoring 2^(2p): α²β − 2^(v−2p)γ' where the second term is even, first odd ⟹ odd. Yes z = 3p. Same as mine. They wrote "z=p+v+1>3p" — with v > 2p, v ≥ 2p+1, so z ≥ 3p+2 > 3p. ✓ consistent.
- So v = 2p exactly: **α + β = 2^(2p)γ, γ odd**, and then N = 2^(2p)[α²β − γ], so 2ᶻ = 2^(3p)(α²β − γ), giving z = 3p + v₂(α²β − γ). Combined with z = p + 2p + 1 = 3p + 1: v₂(α²β − γ) = 1.

Hmm, wait. R3 says "结合 z=3p+1 立刻强制 (★) α²β−γ=2（恰好等于2）". How? Let me think. We have 2ᶻ = 2^(3p)·M where M := α²β − γ must be a power of 2 times... wait no: 2ᶻ is a power of 2 and equals 2^(3p)·M, so M itself must be a power of 2, say M = 2^(z−3p), and z − 3p = 1 from above. So M = 2. Yes! Since 2ᶻ = 2^(3p)·M exactly and 2ᶻ is a pure power of 2, M = 2^(z−3p); and v₂(M) = z − 3p = 1, and M being a power of 2 with v₂ = 1 means M = 2. Clean. ✓

Similarly 2ʸ = a(b²−1) − b = 2ᵖ[2^(2p)αβ² − (α+β)] = 2^(3p)(αβ² − γ). y = z + d₁ where d₁ = y − z ≥ 1. So αβ² − γ = 2^(y−3p) = 2^(d₁+1). ✓ (★★)

Machine check with (2,6,11): a=2,b=6: p=1, α=1, β=3. α+β = 4 = 2²·1 ⟹ γ=1, 2p=2 ✓. α²β − γ = 3 − 1 = 2 ✓. αβ² − γ = 9 − 1 = 8 = 2³ ⟹ d₁ + 1 = 3, d₁ = 2, y = z + 2. Check directly: 2ᶻ = ca − b = 22 − 6 = 16, z = 4 = 3p+1 ✓. 2ʸ = 66 − 2 = 64, y = 6. d₁ = 2 ✓.

**Claim 3: size argument.**
From (★): α²β = γ + 2 ⟹ β = (γ+2)/α². α < β ⟹ α³ < α²β = γ + 2 ⟹ α³ ≤ γ + 1 (integers: α³ < γ+2 ⟹ α³ ≤ γ+1).
From α + β = 4ᵖγ ≥ 4γ (p ≥ 1) and β ≤ (γ+2)/1... hmm: β = (γ+2)/α². So α + (γ+2)/α² = 4ᵖγ ≥ 4γ ⟹ α ≥ 4γ − (γ+2)/α² ≥ 4γ − (γ+2) (since α² ≥ 1) = 3γ − 2.

Case γ ≥ 3: α ≥ 3γ−2 ≥ 7. Also α² ≤ γ + 2 (from β ≥ 1... wait, β = (γ+2)/α² ≥ 1 ⟹ α² ≤ γ+2). Hmm, R3 used α ≤ (γ+2)^{1/3}? Let me recheck: α³ ≤ γ + 1 gives α ≤ (γ+1)^{1/3}. And α ≥ 3γ − 2. For γ ≥ 3: 3γ − 2 > (γ+1)^{1/3}? At γ=3: 7 > 4^{1/3}≈1.587 ✓. Since 3γ−2 grows much faster, holds for all γ ≥ 3. Contradiction. ✓ (R3 wrote (γ+2)^{1/3}, using α³ < γ+2; same thing.)

Case γ = 1: α + β = 4ᵖ. With p ≥ 1: α + β ∈ {4, 16, 64, ...}. And α²β = 3. α,β odd positive, α < β: α=1 ⟹ β=3: α²β = 3 ✓, α+β = 4 = 4¹ ✓ p=1. α=3 ⟹ β = 3/9 not integer. Larger α no. So unique (α,β,p) = (1,3,1) ⟹ a = 2, b = 6, c = ab − 1 = 11. ✓

Wait, but should also consider: could α²β = 3 with other combos — α must divide... α² | 3 ⟹ α = 1. Yes unique.

Also need to double check that (2,6,11) satisfies everything including c > b: 11 > 6 ✓, and all three expressions powers of 2: 12−11=1, 66−2=64, 22−6=16 ✓.

Hmm, one more check on Claim 2: I assumed p ≥ 1 (a,b even ⟹ yes p,q ≥ 1). And in the sum identity, I should double-check v₂(ab − 2) = 1: a,b even ⟹ ab divisible by 4 ⟹ ab − 2 ≡ 2 (mod 4) ⟹ v₂ = 1 exactly. ✓

And the difference identity uses c + 1 = ab which came from x=0. ✓ And v₂((b−a)ab): z = p + q + v₂(b−a). ✓

One subtlety: in the case analysis of Claim 2, I should double check the v < 2p branch: N = 2^(2p)α²β − 2ᵛγ'. Factor 2ᵛ: N = 2ᵛ(2^(2p−v)α²β − γ'), with 2p − v ≥ 1 so first term even, γ' odd ⟹ inner odd ⟹ v₂(N) = v. Then z = p + v. But from (**) z = v₂(a+b)+1 = p + v + 1. Contradiction ✓.

**Step B5: (O,O,O) theorem.** a,b,c odd, distinct, a<b<c. Then x<z<y, all exponents ≥ 1.

From the substitution framework (§2.1 of R5 notes): substitute c = ab − 2ˣ into others. But there's a cleaner direct route for the specific claims used:

Claim i: z = v₂(c² − 1) — wait, R4's chain says "由 2.1 第三条：z = v₂(a(c²−1))，此处 a 奇 ⟹ z = v₂(c²−1)". Let me verify this third identity directly: a(c² − 1) = 2ʸ + 2ᶻc?

Compute: bc − a = 2ʸ and ca − b = 2ᶻ ⟹ b = ca − 2ᶻ. Substitute into bc − a: (ca − 2ᶻ)c − a = c²a − 2^(z)c − a = a(c² − 1) − 2ᶻc = 2ʸ ⟹ a(c² − 1) = 2ʸ + 2ᶻc = 2ᶻ(2^(y−z) + c). Since y > z, 2^(y−z) even, c odd ⟹ bracket odd. So z = v₂(a(c²−1)); a odd ⟹ z = v₂(c² − 1). ✓

Claim ii: 2^(z−1) ≤ c + 1, i.e., 2ᶻ ≤ 2c + 2.
c odd ⟹ c² − 1 = (c−1)(c+1). gcd(c−1, c+1) = 2. Both even; one ≡ 2 mod 4, other ≡ 0 mod 4. v₂(c²−1) = v₂(c−1) + v₂(c+1). One of them equals 1, the other is z − 1. The one carrying valuation z−1: it divides c² − 1 and is a power-of-2 divisor... more precisely, say v₂(c−1) = 1, v₂(c+1) = z−1 (or swapped). The factor with v₂ = z−1: c+1 or c−1 contains 2^(z−1), and that factor is ≤ c + 1. So 2^(z−1) ≤ c + 1. ✓

Claim iii: 2ᶻ = ca − b ≥ 2c + 2.
a ≥ 3 (odd, ≥ 2... a odd so a ≥ 3). b ≤ c − 2 (distinct odds, b < c ⟹ b ≤ c−2). So ca − b ≥ 3c − (c−2) = 2c + 2. ✓

Claims ii & iii: 2c + 2 ≤ 2ᶻ ≤ 2c + 2 ⟹ equality throughout: 2ᶻ = 2c + 2, a = 3, b = c − 2, and 2^(z−1) = c + 1.

Equality conditions: iii: ca − b = 3c − b needs a = 3 AND b = c − 2 (both inequalities tight: a = 3 and b = c − 2). ii: 2^(z−1) ≤ c+1 with the valuated factor ≤ c+1; equality 2^(z−1) = c+1 combined with total 2ᶻ = 2c+2. Actually since 2ᶻ = 2c + 2 = 2(c+1) and 2^(z−1) ≤ c+1, we get 2^(z−1) ≤ c+1 = 2^(z−1), equality. So c + 1 = 2^(z−1) exactly, i.e., c = 2^(z−1) − 1.

Claim iv: x = v₂(a² − 1). From framework first identity: b(a² − 1) = 2ᶻ + 2ˣa. Derive: c = ab − 2ˣ. Then bc − a = (ab−2ˣ)b − a = ab² − 2ˣb − a = a(b² − 1) − 2ˣb = 2ʸ ⟹ a(b²−1) = 2ʸ + 2ˣb = 2ˣ(2^(y−x) + b) ⟹ x = v₂(a(b²−1)) = v₂(b²−1) (a odd). Similarly ca − b = (ab − 2ˣ)a − b = a²b − 2ˣa − b = b(a² − 1) − 2ˣa = 2ᶻ ⟹ b(a²−1) = 2ᶻ + 2ˣa = 2ˣ(2^(z−x) + a) ⟹ x = v₂(b(a²−1)) = v₂(a² − 1) (b odd). ✓ So x = v₂(a²−1); a = 3 ⟹ x = v₂(8) = 3. So ab − c = 2³ = 8.

Then with a = 3, b = c − 2: ab − c = 3(c−2) − c = 2c − 6 = 8 ⟹ c = 7, b = 5. ✓

Verify (3,5,7): ab − c = 15 − 7 = 8 = 2³ ✓; bc − a = 35 − 3 = 32 = 2⁵ ✓; ca − b = 21 − 5 = 16 = 2⁴ ✓. Order x=3 < z=4 < y=5 ✓ consistent.

Great. Also double check claim ii edge: what if z − 1 = ... the min valuation is exactly 1: since gcd(c−1,c+1)=2, min(v₂(c−1), v₂(c+1)) = 1 exactly (one of c±1 is ≡ 2 mod 4). And max = z − 1. The factor achieving max valuation is at most c+1, and 2^(z−1) divides it, so 2^(z−1) ≤ that factor ≤ c+1. ✓

Edge case: c − 1 = 2^(z−1) itself possibly larger than c+1? No, c−1 < c+1. Either way ≤ c+1. ✓

Also confirm in OOO that a ≥ 3: a odd and a ≥ 2 (coordinates ≥2) ⟹ a ≥ 3 ✓. b ≤ c − 2: b < c both odd ⟹ differ by even ≥ 2 ✓.

Everything checks out. Now the full solution set: ordered triples up to permutation: (2,2,2), (2,2,3), (2,6,11), (3,5,7). All permutations: (2,2,2): 1; (2,2,3): 3 permutations; (2,6,11): 6; (3,5,7): 6. Total 16 ordered triples.

Let me now run machine verification to be thorough (my own quick brute force), then write 工作笔记.md and proof.md.

Plan:
1. Create todo list.
2. Run brute-force verification in Python (a,b,c range, say up to 300 for full triple enumeration with c derived? Better: enumerate 2 ≤ a ≤ b ≤ c ≤ N for N=400; that's ~10^7 iterations, fine in a few seconds with optimization. Or smarter: enumerate a,b and derive c from ab−c=2ˣ: c = ab − 2ˣ > 0 for each power 2ˣ < ab. Then check other two conditions. That covers all c implicitly! Because any solution must have ab − c a power of 2. Enumerate a ≤ b ≤ 20000 maybe. Cheap.)
3. Write 工作笔记.md progressively.
4. Write proof.md.
5. Self-check pass on the two flagged spots (EEO step 2 case analysis, OOO equality conditions) — done above, will restate in proof.

The task instructions say: append to 工作笔记.md after each reasoning block. I'll write it in stages. Also final deliverable proof.md ending with \boxed{...}.

Note about "作弊风险声明": I did not search anything external; state "无外部接触" per notes guidance.

Where should files go? Current working directory /private/tmp/p275-1962-v2/. The prompt says 完整证明写入当前目录proof.md, and 工作笔记.md in current directory too ("立即追加写入工作笔记.md").

Let me start. First todos, then brute force, writing notes along the way.Run my own independent brute-force verification (not just trusting R5's scripts): generic scan via c = ab − 2ˣ derivation, plus the two parametric deep scans.Machine verification confirms: generic scan a,b ≤ 2000 gives exactly the four solutions; EEO parametric deep scan (even a ≤ 200000) only (2,6,11); OOO odd scan only (3,5,7).

Note my OOO scan only went to b ≤ 3000, weaker than R5's a ≤ 30000 parametric scan, but that's just decoration — the proof is closed. Let me also run a slightly deeper OOO parametric scan matching R5: for odd a ≤ 30000, odd b, c derived from ab−c=2^x. Actually my scan derives c from ab−c=2^x which covers all c — that IS the right parametrization. Let me push b to 30000 to match. Actually the loop is O(B^2 log) which for B=30000 is 2.25e8·~15 — too slow in Python. R5's "参数化深扫到奇数 a≤30000" — unclear what exactly, but doesn't matter; the math is closed. I'll note my scan bounds honestly in proof.md appendix.

Actually, let me do a quick smarter OOO deep scan using the theorem structure: in any OOO solution, z = v₂(c²−1), 2^z = ca−b. For fixed odd a, b: c = ab − 2^x. That's what I did. To go deeper cheaply, use the derived necessary structure: from the proof, any OOO solution must have a=3! Because the theorem shows a=3 forced. But that's circular for verification purposes. Skip — the proof is what matters, machine is decoration.

Now write the first version of 工作笔记.md, then do the careful re-verification of the two flagged spots (which I already did in my head above — EEO step 2 case analysis and OOO equality conditions — both check out), then write proof.md.

Let me write 工作笔记.md now.Now let me do the two flagged verifications with machine assistance to be extra careful:

1. EEO step 2: the v₂ case analysis. I did it by hand above; let me verify with a quick symbolic/numeric check — e.g., for random even a,b pairs, check that the identity z = p + v₂(α+β) + 1 holds and the three cases are exhaustive and each conclusion correct.

2. OOO step 4 equality conditions: verify that the chain forces a=3, b=c−2, c+1=2^(z−1).

Actually these are pure-math checks; machine can only sanity check instances. Let me do a numeric spot-check of EEO claim structure on (2,6): already done (α=1,β=3,p=1,γ=1). And also test that no other (α,β,p) satisfies (★)(★★) with α<β odd — small enumeration.

Let me enumerate α<β odd, p≥1, γ odd with α+β=4^p·γ, α²β−γ=2, αβ²−γ=2^(d+1) for small ranges to confirm unique (1,3,1).Both flagged spots verified:
- EEO parametric system has unique solution (α,β,p)=(1,3,1) in the searched range (α<2000).
- (3,5,7) satisfies all forced structural identities: x=v₂(a²−1)=3, z=v₂(c²−1)=4, 2^z=2c+2=16, c+1=2^(z−1).

Now write proof.md. Structure per R4's plan:
1. Statement & conventions
2. WLOG + coordinates ≥ 2
3. Equal-coordinates case → (2,2,2), (2,2,3)
4. All-distinct: ordering lemma gives x<z<y; parity dispatch kills 5 patterns
5. c-even lemma kills EEE (and generally all c-even patterns)
6. EEO theorem
7. OOO theorem
8. Numerical appendix
9. Boxed answer

I need to be careful and complete in the writing. Let me draft it fully.

Also the cheating risk statement at the top: no external search, no external literature.

Let me make sure every step in my proof is airtight. Let me re-derive once more carefully as I write:

**§0 Conventions.** Powers of 2: {2^k : k ∈ Z≥0}. Positive integers.

**§1 WLOG.** The three expressions {ab−c, bc−a, ca−b} are permuted by any permutation of (a,b,c): swapping a↔b sends ab−c→ba−c (same), bc−a→ac−b=ca−b, ca−b→cb−a=bc−a. Similarly other swaps generate all of S₃. So WLOG a≤b≤c.

**§2 Coordinates ≥ 2.** Suppose a=1. Then bc−a = bc−1 ≥ ... wait, R1's argument: b−c and c−b are both powers of 2. With a=1: ab−c = b−c, ca−b = c−b. Both must be powers of 2, i.e., positive. But b−c = −(c−b), so both positive is impossible. Hence no coordinate equals 1... 

Hmm wait — actually I should double check: could b−c = 0? No, then it's 0 which is not a power of 2. Could one be positive and other negative? Negative isn't a power of two. So indeed contradiction. Hence a,b,c ≥ 2.

**§3 Notation & ordering lemma.**
ab−c=2ˣ, bc−a=2ʸ, ca−b=2ᶻ, x,y,z ≥ 0.
- 2ᶻ − 2ˣ = (ca−b) − (ab−c) = a(c−b) + (c−b) = (c−b)(a+1) ≥ 0 ⟹ x ≤ z.
- 2ʸ − 2ᶻ = (bc−a) − (ca−b) = c(b−a) + (b−a) = (b−a)(c+1) ≥ 0 ⟹ z ≤ y.
- 2ʸ − 2ˣ = (bc−a) − (ab−c) = b(c−a) + (c−a) = (c−a)(b+1) ≥ 0 ⟹ x ≤ y.
Equalities: since powers of 2 with nonneg exponents, 2ᶻ=2ˣ ⟺ z=x ⟺ (c−b)(a+1)=0 ⟺ c=b. Etc.

So:
- If a=b=c: handle.
- If exactly two equal or all equal → §4.
- If all distinct: a<b<c and x<z<y strictly.

**§4 Equal coordinates.**

Case a=b: 2ʸ = bc−a = ac−a = a(c−1) ⟹ a=2ᵘ, c−1=2ᵛ (u,v ≥ 0). Then 2ˣ = ab−c = a² − c = 2²ᵘ − 2ᵛ − 1.
  - If v ≥ 1: LHS odd ⟹ 2ˣ=1 ⟹ 2ᵛ(2^{2u−v}−1)=2. If 2u ≤ v then 2^{2u−v}−1 ≤ 0, impossible; else inner is a positive odd integer, so v=1, 2^{2u−v}−1=1 ⟹ 2u−v=1 ⟹ u=1. So a=2, c=3: (2,2,3). ✓ verified.
  - If v=0: c=2, and 2=a≤b=a≤c=2 forces a=2: (2,2,2). ✓

Case b=c (and a<b, otherwise all equal covered above): 2ˣ = ab−c = ab−b = b(a−1) ⟹ b=2ᵗ, a−1=2ˢ.
  - s=0 ⟹ a=2, b=c=2ᵗ, t≥1 (b≥2). Then 2ʸ = bc−a = 2^{2t}−2 = 2(2^{2t−1}−1). Inner odd positive (t≥1). So 2ʸ=2·odd power of 2 ⟹ inner=1 ⟹ t=1 ⟹ (2,2,2).
  - s≥1 ⟹ a odd. b=2ᵗ, t≥1 ⟹ b even. 2ʸ = b²−a even−odd=odd ⟹ 2ʸ=1 ⟹ a=b²−1=2^{2t}−1. Then 2ˣ = b(a−1) = 2ᵗ(2^{2t}−2) = 2^{t+1}(2^{2t−1}−1); inner odd ⟹ must equal 1 ⟹ 2t−1=1 ⟹ t=1 ⟹ b=c=2, a=3: (3,2,2).

Case a=c: with a≤b≤c this forces all equal — included above (a=b and b=c sub-cases cover it; when a=c and a<b... impossible under ordering unless b between: a=c means a≤b≤a so all equal).

So up to permutation: (2,2,2) and (2,2,3).

Wait, careful: in case a=b, I found (2,2,3) where c>a — consistent with a≤b≤c ✓. In case b=c, found (3,2,2) — but under our WLOG ordering a≤b≤c this would be re-labeled; the unordered triple {3,2,2} = permutation of (2,2,3) ✓. Fine.

**§5 All distinct: parity dispatch.**
x<z<y strictly. Each of x,y,z is 0 iff corresponding expression is odd (only odd power of 2 is 1=2⁰).

Table over parities of (a,b,c):
| pattern | ab−c | bc−a | ca−b | verdict |
| EEE | even | even | even | survives → §7 |
| EEO | odd (x=0) | even | even | survives → §6 |
| EOE | even | odd (y=0) | even | dead: y=0<x contradicts x<y |
| EOO | odd (x=0) | odd (y=0) | odd (z=0) | dead: x=z=0 contradicts x<z |
| OEE | even | odd (y=0) | even | dead: y=0 |
| OEO | odd (x=0) | odd (y=0) | even | dead: x=z=0 |
| OOE | odd (x=0) | odd (y=0) | odd (z=0) | dead: x=y=0 |

Wait, for EOO: ab−c: a even,b odd ⟹ ab even; c odd ⟹ odd result? even − odd = odd ✓ x=0. bc−a: b,c odd ⟹ bc odd; a even ⟹ odd − even = odd ✓ y=0. ca−b: c odd,a even ⟹ even; b odd ⟹ even − odd = odd ✓ z=0. Dead by x<z.

For OEE: ab: odd·even=even; c even ⟹ even−even=even ⟹ x≥1. bc: even·even=even; a odd ⟹ odd ⟹ y=0. ca: even·odd=even; b even ⟹ even ⟹ z≥1. y=0 < x ⟹ violates x<y... actually y should be the largest, but y=0 ≤ x. Contradiction ✓.

For OEO: ab: odd·even=even; c odd ⟹ odd ⟹ x=0. bc: even·odd=even; a odd ⟹ odd ⟹ y=0. ca: odd·odd=odd; b even ⟹ odd−even=odd?? Wait: ca odd minus b even = odd. Hmm! Let me recompute. a odd, c odd ⟹ ca odd. b even. ca − b = odd − even = odd ⟹ z = 0!

Hold on, that contradicts the table in R5 notes which says (O,E,O): x=z=0. Yes! x=0 AND z=0. Both zero. Violates strict x<z. ✓ OK so z=0 too. Good, matches "x=z=0（纯奇偶两行即杀）". My earlier quick pass said z ≥ 1 — wrong; correct is z=0. Either way it's dead because x=z=0. Let me redo carefully:

(O,E,O): a odd, b even, c odd.
- ab − c: ab even; c odd ⟹ ab − c odd ⟹ x = 0.
- bc − a: bc even; a odd ⟹ odd ⟹ y = 0.
- ca − b: ca odd; b even ⟹ odd ⟹ z = 0.
Dead via x = z = 0 < needed strict inequality. ✓

And (E,O,E): a even, b odd, c even.
- ab even; c even ⟹ even ⟹ x ≥ 1.
- bc even; a even ⟹ even ⟹ y ≥ 1?? Hmm: bc − a = even − even = even ⟹ y ≥ 1. But R5 table says "(E,O,E) 死：纯奇偶，x=z=0 违反 x<z"?? That doesn't match. Let me recompute very carefully.

(E,O,E): a even, b odd, c even.
- ab − c = (even)(odd) − even = even − even = even ⟹ x ≥ 1.
- bc − a = (odd)(even) − even = even − even = even ⟹ y ≥ 1.
- ca − b = (even)(even) − odd = even − odd = odd ⟹ z = 0.
z = 0 but x < z requires z > x ≥ 1. Contradiction ✓. Dead via z=0 being smallest while it should be middle.

Hmm so R5's table parenthetical "(E,O,E) 死：纯奇偶，x=z=0 违反 x<z" seems garbled (maybe mixed up rows), but the verdict "死" is right, and R5's §2.2 says the kill reasons were extracted from R4's thinking stream. Whatever the exact parenthetical, I've recomputed all seven myself; let me tabulate cleanly and double check each:

Notation: expression parity = parity of product minus third coordinate.

(E,E,E): all products even, subtracting even ⟹ all even. Exponents ≥1. Survive.
(E,E,O): 
 - ab−c: even − odd = odd ⟹ x=0.
 - bc−a: (even)(odd)=even; even−even=even ⟹ y≥1.
 - ca−b: (odd)(even)=even; even−even=even ⟹ z≥1.
 Survive (x=0<z consistent).
(E,O,E): computed above: x≥1, y≥1, z=0. Dead (needs x<z).
(E,O,O): x=0,y=0,z=0. Dead (needs x<z).
(O,E,E): x≥1, y=0, z≥1. Dead (needs z<y).
(O,E,O): x=0,y=0,z=0. Dead (needs x<z).
(O,O,E): ab−c: odd−even=odd ⟹ x=0. bc−a: (odd)(even)=even; even−odd=odd ⟹ y=0. ca−b: even·odd=even; even−odd=odd ⟹ z=0. Dead (x=y=0, needs x<y).
(O,O,O): all even. Survive.

Cross-check against R5 table:
- (E,O,E): 死 ✓ (my reason: z=0 violates x<z; their note says "x=z=0" — minor discrepancy in parenthetical but both die; hmm, actually wait. Their table row "(E,O,E) | 死：纯奇偶，x=z=0 违反 x<z". My computation says x≥1, z=0. Their claim x=0 is wrong per my calc? Let me triple-check (E,O,E): a even, b odd, c even. ab = even·odd = even. c = even. ab − c = even − even = EVEN. So x ≥ 1, not 0. And ca − b: c even, a even ⟹ ca even; b odd ⟹ even − odd = odd ⟹ z=0. So it's z=0 alone that kills (violates x<z since x≥1>0=z... wait we need x<z, and z=0≤x, yes violated). Also y vs z: y≥1, z=0 violates z<y too.

So the R5 parentheticals for (E,O,E) appear swapped/garbled relative to my computation, but the verdict is identical. Since I'm writing the final proof from my own recomputation (all steps re-derived above), this doesn't matter. But worth noting in 工作笔记 as a minor correction: the parenthetical kill-reasons for (E,O,E)/(O,E,E)/(O,E,O)/(O,O,E) rows in R5's table may have row-order garbling; my independent table is authoritative for proof.md.

Actually let me also double check (O,E,E): a odd, b even, c even.
- ab−c: even − even = even ⟹ x≥1.
- bc−a: even − odd = odd ⟹ y=0.
- ca−b: even − even = even ⟹ z≥1.
Kill reason: y=0 but z<y needs 0=z<y... z≥1>y=0 violates z<y ✓.

(R5's row said "(O,E,E) 死：y=0 但 y 是最大者" ✓ matches.)

(O,E,O) row in R5: "x=z=0" ✓ matches mine.
(O,O,E) row: "x=y=0 违反 x<y" ✓ matches mine ((O,O,E): x=0, y=0, z=0 — all zero actually; either way dead).

Hmm wait for (O,O,E) I got all three zero: x=0 (ab odd − c even = odd), y=0 (bc even − a odd = odd), z=0 (ca even − b odd = odd). All three zero, dead. ✓

OK. Only discrepancy: (E,O,E) row. Mine: x≥1, y≥1, z=0. R5 parenthetical: "x=z=0". Mine is right (recomputed twice). Note it in work notes.

**§6 c-even lemma (kills EEE among survivors).**
Lemma: In the all-distinct case, c cannot be even.
Proof: c even ⟹ C := v₂(c+1) = 0. Identity (1): (b−a)(c+1) = 2ʸ − 2ᶻ. Since y>z, v₂(2ʸ−2ᶻ) = z (factor 2ᶻ(2^{y−z}−1), second factor odd). Taking v₂: v₂(b−a) + C = z ⟹ 2ᶻ | b−a. As b>a, b−a ≥ 1, so b−a ≥ 2ᶻ.
On the other hand 2ᶻ = ca − b. Claim: ca − b > b − a. Equivalent to a(c+1) > 2b. If a ≥ 3: a(c+1) ≥ 3(b+1) > 2b ✓. If a = 2: 2(c+1) > 2b ⟺ c > b − 1, true since c>b ✓.
So 2ᶻ = ca−b > b−a ≥ 2ᶻ, contradiction. ∎

This kills (E,E,E) (the only surviving pattern with c even). [It also independently kills (O,O,E),(E,O,E),(O,E,E) but those are already dead.]

Wait — identity numbering: let me define identities clearly:
(I) (b−a)(c+1) = 2ʸ − 2ᶻ
(II) (c−b)(a+1) = 2ᶻ − 2ˣ
(III) (c−a)(b+1) = 2ʸ − 2ˣ

Verify (I): 2ʸ − 2ᶻ = (bc−a) − (ca−b) = bc − ca + (b − a)... compute: bc − a − ca + b = c(b−a) + (b−a) = (b−a)(c+1) ✓.
(II): 2ᶻ − 2ˣ = (ca−b) − (ab−c) = ca − ab + c − b = a(c−b) + (c−b) = (c−b)(a+1) ✓.
(III): 2ʸ − 2ˣ = (bc−a) − (ab−c) = bc − ab + c − a = b(c−a) + (c−a) = (c−a)(b+1) ✓.

Good.

**§7 (E,E,O) theorem.** a<b<c, a≡b≡0 mod 2, c odd. From identity (II) valuation: x = v₂(c−b) + v₂(a+1). c odd, b even ⟹ c−b odd ⟹ v₂(c−b)=0; a even ⟹ v₂(a+1)=0. So x=0, i.e., **c = ab − 1**. (Note c=ab−1 > b needs checking for solutions; it will follow from 2ᶻ>0: 2ᶻ = ca−b = a(ab−1)−b = a²b−a−b; positivity holds automatically for the found solution; in general if 2ᶻ≥1 then fine. Actually since we only use it to derive candidates and then verify, fine.)

Then:
2ᶻ = ca − b = a(ab−1) − b = a²b − a − b = b(a²−1) − a,
2ʸ = bc − a = b(ab−1) − a = ab² − b − a = a(b²−1) − b.

Step 1 (p:=v₂(a)=v₂(b)): 
Sum: 2ʸ + 2ᶻ = (a+b)(ab−2). [expand: a²b+ab²−2a−2b ✓]
v₂(LHS) = z since 2ʸ+2ᶻ = 2ᶻ(2^{y−z}+1) with y−z≥1 ⟹ second factor odd.
v₂(ab−2): a,b even ⟹ 4|ab ⟹ ab−2 ≡ 2 mod 4 ⟹ v₂ = 1.
So z = v₂(a+b) + 1. (*)
Diff via (I) with c+1 = ab: 2ʸ − 2ᶻ = (b−a)ab; v₂ = z (same reasoning). Write p=v₂(a), q=v₂(b): z = p+q+v₂(b−a). (**)
If p<q: v₂(b−a)=p (b−a = 2ᵖ(2^{q−p}β−α), bracket: even−odd=odd), v₂(a+b)=p (a+b=2ᵖ(α+2^{q−p}β), odd+even=odd). Then (**) & (*): p+q+p = p+1 ⟹ p+q=1, contradicting p,q≥1. p>q symmetric: q+p+q = q+1 ⟹ q+p=1 impossible. Hence p=q=:p. ✓

Step 2 (exact equations): a=2ᵖα, b=2ᵖβ, α<β odd.
From (*): z = p + v₂(α+β) + 1. (***)  [v₂(a+b)=v₂(2ᵖ(α+β))=p+v₂(α+β)]
Direct: 2ᶻ = b(a²−1) − a = 2ᵖ[β(2^{2p}α²−1) − α] = 2ᵖ[2^{2p}α²β − (α+β)]. Let v=v₂(α+β), N := 2^{2p}α²β − (α+β).
 - v<2p: N=2ᵛ(2^{2p−v}α²β − γ'), γ'=(α+β)/2ᵛ odd; inner even−odd=odd ⟹ z=p+v ≠ p+v+1=(***). Contradiction.
 - v>2p: N=2^{2p}(α²β − 2^{v−2p}γ'); inner odd−even=odd ⟹ z=3p; but (***) gives z=p+v+1 ≥ 3p+2. Contradiction.
 - Hence v=2p: α+β = 2^{2p}γ, γ odd; N = 2^{2p}(α²β−γ) ⟹ 2ᶻ = 2^{3p}(α²β−γ). As 2ᶻ is a pure power of 2, α²β−γ = 2^{z−3p}; and z=3p+1 by (***). Hence **α²β − γ = 2**. (★)
 Same with y: 2ʸ = a(b²−1) − b = 2ᵖ[2^{2p}αβ² − (α+β)] = 2^{3p}(αβ²−γ) ⟹ **αβ² − γ = 2^{y−3p}**. (★★)
 
Step 3 (size): From (★): β=(γ+2)/α². α<β ⟹ α³ < α²β = γ+2 ⟹ α³ ≤ γ+1. (i)
 From α+β = 4ᵖγ ≥ 4γ and β=(γ+2)/α² ≥ ... hmm, I want lower bound on α: α = 4ᵖγ − β ≥ 4γ − (γ+2)/α² ≥ 4γ − (γ+2) = 3γ−2. (ii) [using α²≥1]
 If γ≥3: α ≥ 3γ−2 ≥ 7 and α³ ≤ γ+1 < (3γ−2)³ — wait need contradiction: α ≥ 3γ−2 and α³ ≤ γ+1. For γ≥3: (3γ−2)³ ≤ α³ ≤ γ+1? No: α ≥ 3γ−2 ⟹ α³ ≥ (3γ−2)³. And α³ ≤ γ+1. So (3γ−2)³ ≤ γ+1. At γ=3: 343 ≤ 4 false. Since (3γ−2)³ grows much faster than γ+1, false for all γ≥3 (monotone: f(γ)=(3γ−2)³−(γ+1) increasing for γ≥1, f(3)>0). Contradiction.
 Hence γ=1 (γ odd positive). Then α²β = 3 ⟹ α=1 (α²|3 ⟹ α=1), β=3, and α+β=4=4ᵖ ⟹ p=1.
 So a=2, b=6, c=ab−1=11. Verify: ab−c=1=2⁰, bc−a=64=2⁶, ca−b=16=2⁴ ✓.

Note: in Step 3, γ can't be negative/zero; γ odd ≥ 1. ✓

**§8 (O,O,O) theorem.** a<b<c all odd, all ≥3 for a (a odd ≥2 ⟹ ≥3), b ≤ c−2, x<z<y, all exponents ≥1.

Substitution identities: from c = ab − 2ˣ:
 ca − b = a(ab−2ˣ) − b = a²b − 2ˣa − b = b(a²−1) − 2ˣa = 2ᶻ ⟹ b(a²−1) = 2ᶻ + 2ˣa = 2ˣ(2^{z−x} + a). Bracket: even + odd = odd ⟹ **x = v₂(a²−1)** (b odd).
 from b = ca − 2ᶻ: bc − a = c(ca−2ᶻ) − a = ac² − 2ᶻc − a = a(c²−1) − 2ᶻc = 2ʸ ⟹ a(c²−1) = 2ʸ + 2ᶻc = 2ᶻ(2^{y−z} + c). Bracket odd ⟹ **z = v₂(c²−1)** (a odd).

Bound 1: c odd ⟹ (c−1)(c+1)=c²−1, gcd(c−1,c+1)=2, min(v₂(c−1),v₂(c+1))=1 (one of them ≡2 mod 4). max = z−1. The factor carrying v₂=z−1 is ≤ c+1 and divisible by 2^{z−1}: **2^{z−1} ≤ c+1**, i.e., 2ᶻ ≤ 2c+2.
Bound 2: 2ᶻ = ca − b ≥ 3c − (c−2) = 2c+2.
Hence equality: **2ᶻ = 2c+2, a=3, b=c−2**, and 2^{z−1}=c+1.
Then x = v₂(a²−1) = v₂(9−1) = 3 ⟹ ab−c = 8: 3(c−2) − c = 2c−6 = 8 ⟹ c=7, b=5.
Verify (3,5,7): 8,32,16 ✓.

Equality condition rigor in Bound 2: ca − b ≥ 3c − b uses a≥3; then −b ≥ −(c−2) uses b ≤ c−2. Sum: ca − b ≥ 3c − (c−2) = 2c + 2. Equality requires a=3 and b=c−2 simultaneously ✓ (both inequalities must be tight since final values equal).

In Bound 1: 2^{z−1} ≤ (factor with valuation z−1) ≤ c+1. Combined with 2ᶻ = 2c+2 = 2(c+1): 2^{z−1} ≤ c+1 = 2^{z−1} ⟹ c+1 = 2^{z−1}. Fine (this is used only as derived structure; the actual killing comes from x=v₂(a²−1) after a=3).

**§9 Enumeration & answer.**
Ordered triples: permutations of (2,2,2) [1], (2,2,3) [3], (2,6,11) [6], (3,5,7) [6] = 16 total.

Machine appendix: generic scan a≤b≤2000 with c=ab−2ˣ derived: four reduced solutions. EEO parametric scan even a ≤ 200000: only (2,6,11). OOO scan odd a,b ≤ 3000: only (3,5,7).

Now, one more consideration on completeness of the case split: the case split is (i) some two coordinates equal (handled §4), (ii) all distinct (§5–§8). Within all-distinct: 8 parity patterns; 5 killed by parity, EEE killed by c-even lemma, EEO and OOO solved. Complete. ∎

Also, should double-check the claim "the only odd power of 2 is 2⁰=1": powers of 2 are 2^k, k≥0; odd ⟺ k=0. ✓

One more check on §4 a=b sub-case v≥1: 2²ᵘ − 2ᵛ − 1 = 2ˣ with 2ˣ=1: 2²ᵘ − 2ᵛ = 2. v≥1. Factor 2ᵛ(2^{2u−v} − 1) = 2. Need 2u−v ≥ 0 for the inner to be an integer power expression... Actually 2^{2u−v} requires 2u−v ≥ 0 to be an integer. If 2u−v < 0, then 2²ᵘ − 2ᵛ = 2ᵛ(2^{2u−v}) isn't integer-factorable that way; instead directly: 2ᵛ | 2²ᵘ requires v ≤ 2u (since 2²ᵘ − 2ᵛ = 2 > 0 and if v > 2u then 2²ᵘ − 2ᵛ < 0). So v ≤ 2u, factor valid. Inner = 2^{2u−v}−1 ≥ 0; = 0 only if u=v... 2^0−1 = 0 gives LHS 0 ≠ 2. So inner ≥ 1 odd. Product = 2 with 2ᵛ a power of 2 and inner odd positive ⟹ v=1, inner=1 ⟹ 2u−v=1 ⟹ 2u=2 ⟹ u=1. a=2¹=2, c−1=2¹⟹c=3. ✓ And ordering a≤b≤c: 2≤2≤3 ✓.

Also §4 b=c sub-case s≥1: need t ≥ 1: b = 2ᵗ ≥ 2 ⟹ t ≥ 1 ✓ (t=0 would give b=1, excluded). b² − a = 2ʸ: b even (t≥1) ⟹ b² even; a odd ⟹ difference odd ⟹ 2ʸ=1 ⟹ a = b²−1. Then ab − c = ab − b = b(a−1) = 2ᵗ(2^{2t} − 2) = 2^{t+1}(2^{2t−1} − 1). For this to be a power of 2 need 2^{2t−1}−1 = 1 (it's a positive odd integer; t≥1 ⟹ 2t−1≥1 ⟹ inner ≥ 1) ⟹ 2t−1=1 ⟹ t=1. Then b=c=2, a=3. Check ordering violated (3≤2 false) but that's fine — we're enumerating unordered patterns; the triple (a,b,c)=(3,2,2) satisfies original equations: ab−c=6−2=4 ✓, bc−a=4−3=1 ✓, ca−b=6−2=4 ✓. It's a permutation of (2,2,3) ✓.

Hmm, one subtlety: in §4 I claimed WLOG covers cases via permutations, but within the WLOG-ordered triple a≤b≤c, "a=b" and "b=c" are the only ways two coordinates coincide. When solving "a=b" I didn't use c≥b except implicitly fine; when solving "b=c" I found a=3 > b=2 violating the assumed order — meaning under WLOG that solution would present itself in the "a=b" analysis instead. To avoid confusion, better to phrase §4 without WLOG ordering: "suppose some two coordinates are equal; by symmetry suppose a=b" — solve a=b fully (getting {2,2,3} family and (2,2,2)), and that's it: any triple with two equal coordinates is a permutation of a triple with a=b. Cleanest: By symmetry reduce to a=b; solve completely. The a=b analysis gave: v=0 ⟹ c=2, a=b=2 (using only a≥2; didn't need c≥b: c−1=2⁰=1 ⟹ c=2; a=2ᵘ and a(c−1)=2ʸ... wait let me redo: a=b, a(c−1)=2ʸ ⟹ a=2ᵘ, c−1=2ᵛ. v=0 ⟹ c=2. No constraint forcing a=2 here without ordering! Let me recheck: a=b=2ᵘ, c=2. Then 2ˣ = ab−c = 2^{2u} − 2. Is that a power of 2? 2^{2u} − 2 = 2(2^{2u−1} − 1). u≥1 ⟹ inner odd ≥ 1 ⟹ power of 2 iff inner=1 iff u=1 ⟹ a=2. u=0 would mean a=1 excluded. So (2,2,2). ✓ Good — I previously used ordering but actually the equation 2ˣ=power of 2 forces it directly. Cleaner.

Similarly in a=b, v≥1 branch: got (2,2,3) with u=1. No ordering needed. ✓

So §4: by symmetry assume a=b. a(c−1)=2ʸ ⟹ a=2ᵘ, c−1=2ᵛ.
 - v=0: c=2; 2ˣ = 2^{2u}−2 = 2(2^{2u−1}−1); u≥1 (a≥2); inner odd positive ⟹ =1 ⟹ u=1 ⟹ (2,2,2).
 - v≥1: 2ˣ = 2^{2u} − 2ᵛ − 1 odd ⟹ 2ˣ=1 ⟹ 2ᵛ(2^{2u−v}−1)=2 (with v≤2u shown) ⟹ v=1, 2u−v=1 ⟹ u=1 ⟹ a=2, c=3 ⟹ (2,2,3).
Done: two-coordinate-equal ⟹ permutation of (2,2,2) or (2,2,3). All-equal (2,2,2) included.

Everything solid. Now also mention in proof that in all-distinct case a<b<c and x<z<y.

For §7 I should also verify c>b automatically: c = ab−1 with a,b ≥ 4 even (a≥2,b>a≥2 ⟹ b≥4): c = ab−1 ≥ 2b−1 > b ⟺ b > 1 ✓. Fine, automatic.

Also in §7 Step 1, note z≥1 needed? v₂(LHS)=z requires y>z (strict) ✓ given all-distinct. And (*) z = v₂(a+b)+1 ≥ 1+... fine.

Also in §7: the derivation x = v₂(c−b) + v₂(a+1) from (II): 2ᶻ − 2ˣ = 2ˣ(2^{z−x}−1), z>x ⟹ inner odd ⟹ v₂(LHS)=x. RHS v₂ = v₂(c−b)+A. ✓

Potential edge: in §7, what if z−x = 0? Can't: all distinct ⟹ strict. ✓

In §8, brackets: 2^{z−x}+a: z−x≥1 ⟹ even; a odd ⟹ sum odd ✓. 2^{y−z}+c similarly ✓.

Also §8 needs x≥1? Not really; only v₂ results used. Fine.

Now write proof.md. Include:
- 作弊风险声明 at top.
- Full proof.
- Numerical appendix.
- \boxed{...} at end.

The final boxed answer: all ordered triples: permutations of (2,2,2), (2,2,3), (2,6,11), (3,5,7) — 16 total. I'll list explicitly.

Explicit list:
(2,2,2);
(2,2,3),(2,3,2),(3,2,2);
(2,6,11),(2,11,6),(6,2,11),(6,11,2),(11,2,6),(11,6,2);
(3,5,7),(3,7,5),(5,3,7),(5,7,3),(7,3,5),(7,5,3).

Quick sanity check a couple of non-canonical permutations, e.g., (5,3,7): ab−c=15−7=8 ✓; bc−a=21−5=16 ✓; ca−b=35−3=32 ✓. Good.

Let me update 工作笔记 first (noting the (E,O,E) parenthetical correction), then write proof.md.Now write the complete proof.md.Now let me do a final independent self-check pass on the proof, especially the two flagged spots, and verify a few permutation instances numerically as a last sanity check. Also update 工作笔记.md to reflect completion.

Let me verify all 16 ordered triples numerically.All done. Let me do a final check that the files are in place.