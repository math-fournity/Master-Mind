# Proof: CC-105 / polymath_00083

## Problem

Find the number $N$ of functions $f: \mathbb{Z}/16\mathbb{Z} \to \mathbb{Z}/16\mathbb{Z}$ satisfying
$$f(a)^2 + f(b)^2 + f(a+b)^2 \equiv 1 + 2f(a)f(b)f(a+b) \pmod{16}$$
for all $a, b \in \mathbb{Z}/16\mathbb{Z}$, and compute $N \bmod 2017$.

## Step 1: Reformulation

The equation $x^2 + y^2 + z^2 = 1 + 2xyz$ can be rewritten as:
$$(z - xy)^2 = (x^2 - 1)(y^2 - 1).$$

Setting $g(a) = f(a)^2 - 1 \pmod{16}$, the functional equation becomes:
$$(f(a+b) - f(a)f(b))^2 \equiv g(a) \cdot g(b) \pmod{16}. \tag{$\star$}$$

## Step 2: Determining $f(0)$

Setting $a = b = 0$ in $(\star)$: $(f(0) - f(0)^2)^2 \equiv g(0)^2 \pmod{16}$, which simplifies to $(f(0)-1)^2(2f(0)+1) \equiv 0 \pmod{16}$. Since $2f(0)+1$ is odd, we need $(f(0)-1)^2 \equiv 0 \pmod{16}$, giving $f(0) \equiv 1 \pmod{4}$, i.e., $f(0) \in \{1, 5, 9, 13\}$.

## Step 3: Equivalence of $f(0)=1$ and $f(0)=9$; $f(0)=5$ and $f(0)=13$

For any pair $(a,b)$, the equation involves $f(0)$ only through $f(0)^2$ and $2f(0)$ (when $a=0$, $b=0$, or $a+b \equiv 0$). Since $1^2 \equiv 9^2 \equiv 1 \pmod{16}$ and $2 \cdot 1 \equiv 2 \cdot 9 \equiv 2 \pmod{16}$, replacing $f(0)=1$ with $f(0)=9$ yields identical equations. Thus $N_9 = N_1$.

Similarly, $5^2 \equiv 13^2 \equiv 9 \pmod{16}$ and $2 \cdot 5 \equiv 2 \cdot 13 \equiv 10 \pmod{16}$, so $N_{13} = N_5$.

Therefore $N = 2N_1 + 2N_5$ where $N_c$ denotes the count with $f(0) = c$.

## Step 4: Possible values of $g(a)$

The quadratic residues mod 16 are $\{0, 1, 4, 9\}$, so $f(a)^2 \in \{0, 1, 4, 9\}$ and:
$$g(a) = f(a)^2 - 1 \in \{15, 0, 3, 8\} \pmod{16}.$$

For $(\star)$ to have solutions, $g(a)g(b)$ must be a quadratic residue mod 16. Computing products:
- $15 \times 3 = 45 \equiv 13$ ✗ &ensp;|&ensp; $15 \times 8 = 120 \equiv 8$ ✗ &ensp;|&ensp; $3 \times 8 = 24 \equiv 8$ ✗
- $15 \times 15 = 225 \equiv 1$ ✓ &ensp;|&ensp; $3 \times 3 = 9$ ✓ &ensp;|&ensp; $8 \times 8 = 64 \equiv 0$ ✓
- $0 \times \text{anything} = 0$ ✓

**Cross-type pairs are incompatible.** Therefore, all nonzero values of $g$ must be the same. This gives four cases:

- **Case A:** $g \equiv 0$ everywhere ($f(a)^2 \equiv 1$, so $f(a) \in \{1,7,9,15\}$).
- **Case B:** $g \in \{0, 15\}$ with $15$ appearing ($f(a)^2 \in \{0,1\}$, $f(a) \in \{0,1,4,7,8,9,12,15\}$).
- **Case C:** $g \in \{0, 3\}$ with $3$ appearing ($f(a)^2 \in \{1,4\}$, $f(a) \in \{1,2,6,7,9,10,14,15\}$).
- **Case D:** $g \in \{0, 8\}$ with $8$ appearing ($f(a)$ odd, $f(a) \in \{1,3,5,7,9,11,13,15\}$).

These are exhaustive and mutually exclusive (as a partition: $A$, $B \setminus A$, $C \setminus A$, $D \setminus A$).

## Step 5: Case A ($g \equiv 0$, $f(0) = 1$)

Here $g(a)g(b) = 0$ always, so $(\star)$ gives $f(a+b) \equiv f(a)f(b) \pmod{4}$.

The reduction $\bar{f}: \mathbb{Z}/16\mathbb{Z} \to \{1,3\} \pmod{4} \cong \mathbb{Z}/2\mathbb{Z}$ must be a group homomorphism. There are **2 homomorphisms** (trivial and parity). For each, $f(0)=1$ is fixed, and each of the 15 remaining values has 2 choices ($\{1,9\}$ or $\{7,15\}$ depending on the homomorphism).

$$|A| = 2 \times 2^{15} = 2^{16} = 65536.$$

## Step 6: Cases B\A and C\A ($f(0) = 1$)

Define $B_{\text{set}} = \{a : g(a) = 0\}$ and $A_{\text{set}} = \{a : g(a) \neq 0\}$. From $(\star)$:
- $A_{\text{set}} + A_{\text{set}} \subseteq B_{\text{set}}$ (nonzero $g$-values are equal, their product is a nonzero QR, forcing $f(a+b)$ to have $g = 0$)
- $A_{\text{set}} + B_{\text{set}} \subseteq A_{\text{set}}$ and $B_{\text{set}} + B_{\text{set}} \subseteq B_{\text{set}}$ (when one $g = 0$, product is 0, forcing $f(a+b) \equiv f(a)f(b) \pmod{4}$, which determines the parity of $f(a+b)$ and hence the $g$-value)

This makes $B_{\text{set}}$ a subgroup of $\mathbb{Z}/16\mathbb{Z}$ and $A_{\text{set}}$ a coset. Since $0 \in B_{\text{set}}$ and $A_{\text{set}} \neq \emptyset$, the only possibility is $B_{\text{set}} = \{\text{even elements}\}$, $A_{\text{set}} = \{\text{odd elements}\}$ (the unique index-2 subgroup).

### Case B\A: Even $a$ → $f(a) \in \{1,7,9,15\}$; Odd $a$ → $f(a) \in \{0,4,8,12\}$

**Even-even pairs:** $g = 0$ for both, so $f(a+b) \equiv f(a)f(b) \pmod{4}$ and the original equation requires $f(a)f(b)f(a+b) \equiv 1 \pmod{8}$. Both conditions reduce to: the map $m: \{\text{even elements}\} \cong \mathbb{Z}/8\mathbb{Z} \to \mathbb{Z}/2\mathbb{Z}$ defined by $m(a) = 0$ if $f(a) \equiv 1 \pmod{4}$, $m(a) = 1$ if $f(a) \equiv 3 \pmod{4}$, is a homomorphism. There are **2 such homomorphisms**. For each, $f(0) = 1$ is fixed, and the 7 nonzero even elements each have 2 choices. This gives $2 \times 2^7 = 2^8$ choices for even elements.

**Odd-involving pairs:** For $f(a), f(b) \in \{0,4,8,12\}$, we have $f(a)f(b) \equiv 0 \pmod{16}$ (since $4 \times 4 = 16 \equiv 0$, etc.). Therefore:
- Odd-odd pairs: LHS $= 0 + 0 + 1 = 1$, RHS $= 1 + 2 \cdot 0 \cdot f(a+b) = 1$. ✓ **Automatically satisfied.**
- Even-odd pairs: LHS $= 1 + 0 + 0 = 1$, RHS $= 1 + 2 \cdot f(a) \cdot 0 = 1$. ✓ **Automatically satisfied.**

So odd elements are **completely free**: each of the 8 odd elements independently chooses from $\{0,4,8,12\}$, giving $4^8 = 2^{16}$ choices.

$$|B \setminus A| = 2^8 \times 2^{16} = 2^{24} = 16777216.$$

### Case C\A: Even $a$ → $f(a) \in \{1,7,9,15\}$; Odd $a$ → $f(a) \in \{2,6,10,14\}$

The even-even analysis is identical to Case B, giving $2^8$ choices.

**Odd-involving pairs:** For $f(a), f(b) \in \{2,6,10,14\}$, we have $f(a)f(b) \equiv 4 \pmod{8}$ (since $2 \times 2 = 4$, $2 \times 6 = 12 \equiv 4$, $6 \times 6 = 36 \equiv 4 \pmod{8}$).
- Odd-odd pairs: LHS $= 4 + 4 + 1 = 9$, RHS $= 1 + 2 \cdot f(a)f(b) \cdot f(a+b)$. Since $f(a)f(b) \equiv 4 \pmod{8}$ and $f(a+b)$ is odd, $2 \cdot 4 \cdot (\text{odd}) \equiv 8 \pmod{16}$. RHS $= 1 + 8 = 9$. ✓ **Automatically satisfied.**
- Even-odd pairs: LHS $= 1 + 4 + 4 = 9$, RHS $= 1 + 2 \cdot f(a) \cdot f(b) \cdot f(a+b)$. Here $f(b) \cdot f(a+b) \equiv 4 \pmod{8}$ (both in $\{2,6,10,14\}$), so $2 \cdot f(a) \cdot 4 \equiv 8 \pmod{16}$ (since $f(a)$ is odd). RHS $= 1 + 8 = 9$. ✓ **Automatically satisfied.**

Odd elements are again **completely free**: $4^8 = 2^{16}$ choices.

$$|C \setminus A| = 2^8 \times 2^{16} = 2^{24} = 16777216.$$

## Step 7: Case D\A ($f(0) = 1$, all $f(a)$ odd, not all $f(a)^2 \equiv 1$)

Here $g(a) \in \{0, 8\}$ for all $a$, so $g(a)g(b) \in \{0, 64\} \equiv \{0\} \pmod{16}$ always. Thus $(\star)$ gives $f(a+b) \equiv f(a)f(b) \pmod{4}$.

Substituting $f(a+b) = f(a)f(b) + 4t$ into the original equation, the $t$-dependent terms cancel, leaving $g(a)g(b) \equiv 0 \pmod{16}$, which always holds. So the equation is **equivalent** to $f(a+b) \equiv f(a)f(b) \pmod{4}$.

Same 2 homomorphisms as Case A, but now each value has 4 choices (e.g., $\{1,5,9,13\}$ for $f(a) \equiv 1 \pmod{4}$). With $f(0) = 1$ fixed:

$$|D| = 2 \times 4^{15} = 2^{31}, \qquad |D \setminus A| = 2^{31} - 2^{16}.$$

## Step 8: Computing $N_1$

$$N_1 = |A| + |B \setminus A| + |C \setminus A| + |D \setminus A| = 2^{16} + 2^{24} + 2^{24} + (2^{31} - 2^{16}) = 2^{25} + 2^{31}.$$

## Step 9: Computing $N_5$ ($f(0) = 5$)

For $f(0) = 5$: $g(0) = 25 - 1 = 24 \equiv 8 \pmod{16}$. For $g(0) \cdot g(a)$ to be a QR mod 16 for all $a$, we need $g(a) \in \{0, 8\}$ (since $8 \times 3 = 24 \equiv 8$ ✗ and $8 \times 15 = 120 \equiv 8$ ✗). This forces all $f(a)$ to be odd, and the same analysis as Case D applies: the equation reduces to $f(a+b) \equiv f(a)f(b) \pmod{4}$.

With $f(0) = 5$ fixed and 2 homomorphisms, each with $4^{15}$ choices:

$$N_5 = 2 \times 4^{15} = 2^{31}.$$

## Step 10: Final computation

$$N = 2N_1 + 2N_5 = 2(2^{25} + 2^{31}) + 2 \cdot 2^{31} = 2^{26} + 2^{32} + 2^{32} = 2^{26} + 2^{33}.$$

Computing mod 2017 (prime):

$$2^{11} = 2048 \equiv 31 \pmod{2017}.$$

Powers of 2 mod 2017:
- $2^{16} \equiv 992$
- $2^{17} \equiv 1984 \equiv -33$
- $2^{26} \equiv 1257$
- $2^{32} \equiv 1785$
- $2^{33} \equiv 1553$

$$N \equiv 2^{26} + 2^{33} \equiv 1257 + 1553 = 2810 \equiv 2810 - 2017 = \boxed{793} \pmod{2017}.$$

## Computational Verification

- **Case A**: Exact enumeration confirms $|A| = 65536 = 2^{16}$.
- **Case B\A**: Exact enumeration (all $2^{24}$ configurations checked) confirms $|B \setminus A| = 16777216 = 2^{24}$.
- **Case C\A**: Exact enumeration confirms $|C \setminus A| = 16777216 = 2^{24}$.
- **Case D\A**: Sampling 500,000 random configurations — all satisfy the equation (0 failures).
- **$f(0) = 5, 9, 13$**: Sampling 100,000 random configurations each — all satisfy the equation (0 failures).
- **Negative test**: Random all-odd functions without the homomorphism condition — only those satisfying the homomorphism pass (confirming the homomorphism is both necessary and sufficient).
