# SMALL GAPS BETWEEN PRIMES 

## JAMES MAYNARD 

Abstract. We introduce a refinement of the GPY sieve method for studying prime k-tuples and small gaps between primes. This refinement avoids previous limitations of the method, and allows us to show that for each k, the prime k-tuples conjecture holds for a positive proportion of admissible k-tuples. In particular, lim infn(pn+m − pn) < ∞ for every integer m. We also show that lim inf(pn+1 − pn) ≤ 600, and, if we assume the Elliott-Halberstam conjecture, that lim infn(pn+1 − pn) ≤ 12 and lim infn(pn+2 − pn) ≤ 600. 

# 1. Introduction 

We say that a set H = {h1, . . . , hk} of distinct non-negative integers is ‘admissible’ if, for every prime p, there is an integer ap such that ap � h (mod p) for all h ∈H. We are interested in the following conjecture. 

Conjecture (Prime k-tuples conjecture). Let H = {h1, . . . , hk} be admissible. Then there are infinitely many integers n such that all of n + h1, . . . , n + hk are prime. 

When k > 1 no case of the prime k-tuples conjecture is currently known. Work on approximations to the prime k-tuples conjecture has been very successful in showing the existence of small gaps between primes, however. In their celebrated paper [5], Goldston, Pintz and Yıldırım introduced a new method for counting tuples of primes, and this allowed them to show that 





thereby establishing for the first time the existence of infinitely many bounded gaps between primes. Moreover, it follows from Zhang’s theorem the that number of admissible sets of size 2 contained in [1, x]<sup>2</sup> which satisfy the prime 2-tuples conjecture is ≫ x<sup>2</sup> for large x. Thus, in this sense, a positive proportion of admissible sets of size 2 satisfy the prime 2-tuples conjecture. The recent polymath project [7] has succeeded in reducing the bound (1.2) to 4680, by optimizing Zhang’s arguments and introducing several new refinements. 

The above results have used the ‘GPY method’ to study prime tuples and small gaps between primes, and this method relies heavily on the distribution of primes in arithmetic progressions. Given θ > 0, we say the primes have ‘level of distribution θ’<sup>1</sup> if, for every A > 0, we have 



> 1We note that different authors have given slightly different names or definitions to this concept. For the purposes of this paper, (1.3) will be our definition of the primes having level of distribution θ. 

1 

2 

JAMES MAYNARD 

The Bombieri-Vinogradov theorem establishes that the primes have level of distribution θ for every θ < 1/2, and Elliott and Halberstam [1] conjectured that this could be extended to every θ < 1. Friedlander and Granville [2] have shown that (1.3) cannot hold with x<sup>θ</sup> replaced with x/(log x)<sup>B</sup> for any fixed B, and so the Elliott-Halberstam conjecture is essentially the strongest possible result of this type. 

The original work of Goldston, Pintz and Yıldırım showed the existence of bounded gaps between primes if (1.3) holds for some θ > 1/2. Moreover, under the Elliott-Halberstam conjecture one had lim infn(pn+1 − pn) ≤ 16. The key breakthrough of Zhang’s work was in establishing that a slightly weakened form of (1.3) holds for some θ > 1/2. 

If one looks for bounded length intervals containing two or more primes, then the GPY method fails to prove such strong results. Unconditionally we are only able to improve upon the trivial bound from the prime number theorem by a constant factor [4], and even assuming the Elliott-Halberstam conjecture, the best available result [5] is 



The aim of this paper is to introduce a refinement of the GPY method which removes the barrier of θ = 1/2 to establishing bounded gaps between primes, and allows us to show the existence of arbitrarily many primes in bounded length intervals. This answers the second and third questions posed in [5] on extensions of the GPY method (the first having been answered by Zhang’s result). Our new method also has the benefit that it produces numerically superior results to previous approaches. 

Theorem 1.1. Let m ∈ N. We have 



Terence Tao (private communication) has independently proven Theorem 1.1 (with a slightly weaker bound) at much the same time. He uses a similar method; the steps are more-or-less the same but the calculations are done differently. We will indicate some of the differences in our proofs as we go along. 

We see that the bound in Theorem 1.1 is quite far from the conjectural bound of approximately m log m predicted by the prime m-tuples conjecture. 

Our proof naturally generalizes (but with a weaker upper bound) to many subsequences of the primes which have a level of distribution θ > 0. For example, we can show corresponding results where the primes are contained in short intervals [N, N + N<sup>7/12+ǫ</sup> ] for any ǫ > 0 or in an arithmetic progression modulo q ≪ (log N)<sup>A</sup> . In particular, our method gives results for simultaneously prime values of linear functions, which might have specific interest. Given k distinct linear functions Li(n) = ain + bi (1 ≤ i ≤ k) with positive integer coefficients such that the product function Π(n) =<sup>�k</sup> i=1<sup>Li(n) has no fixed prime divisor, the method presented here</sup> shows that there are infinitely many integers n such that at least (1/4 + ok→∞(1)) log k of the Li(n) are prime. 

Theorem 1.2. Let m ∈ N. Let r ∈ N be sufficiently large depending on m, and let A = {a1, a2, . . . , ar} be a set of r distinct integers. Then we have 



Thus a positive proportion of admissible m-tuples satisfy the prime m-tuples conjecture for every m, in an appropriate sense. 

SMALL GAPS BETWEEN PRIMES 

3 

Theorem 1.3. We have 



We emphasize that the above result does not incorporate any of the technology used by Zhang to establish the existence of bounded gaps between primes. The proof is essentially elementary, relying only on the Bombieri-Vinogradov theorem. Naturally, if we assume that the primes have a higher level of distribution, then we can obtain stronger results. 

Theorem 1.4. Assume that the primes have level of distribution θ for every θ < 1. Then 



Although the constant 12 of Theorem 1.4 appears to be optimal with our method in its current form, the constant 600 appearing in Theorem 1.3 and Theorem 1.4 is certainly not optimal. By performing further numerical calculations our method could produce a better bound, and also most of the ideas of Zhang’s work (and the refinements produced by the polymath project) should be able to be combined with this method to reduce the constant further. We comment that the assumption of the Elliott-Halberstam conjecture allows us to improve the bound on Theorem 1.1 to O(m<sup>3</sup> e<sup>2m</sup> ). 

# 2. An improved GPY sieve method 

We first give an explanation of the key idea behind our new approach. The basic idea of the GPY method is, for a fixed admissible set H = {h1, . . . , hk}, to consider the sum 



Here χP is the characteristic function of the primes, ρ > 0 and wn are non-negative weights. If we can show that S (N, ρ) > 0 then at least one term in the sum over n must have a positive contribution. By the non-negativity of wn, this means that there must be some integer n ∈ [N, 2N] such that at least ⌊ρ + 1⌋ of the n + hi are prime. (Here ⌊x⌋ denotes the largest integer less than or equal to x.) Thus if S (N, ρ) > 0 for all large N, there are infinitely many integers n for which at least ⌊ρ + 1⌋ of the n + hi are prime (and so there are infinitely many bounded length intervals containing ⌊ρ + 1⌋ primes). 

The weights wn are typically chosen to mimic Selberg sieve weights. Estimating (2.1) can be interpreted as a ‘k-dimensional’ sieve problem. The standard Selberg k-dimensional weights (which can be shown to be essentially optimal in other contexts) are 



With this choice we find that we just fail to prove the existence of bounded gaps between primes if we assume the Elliott-Halberstam conjecture. The key new idea in the paper of Goldston, Pintz and Yıldırım [5] was to consider more general sieve weights of the form 

(2.3) λd = µ(d)F(log R/d), 

for a suitable smooth function F. Goldston, Pintz and Yıldırım chose F(x) = x<sup>k+l</sup> for suitable l ∈ N, which has been shown to be essentially optimal when k is large. This allows us to gain a factor of approximately 2 for large k over the previous choice of sieve weights. As a result we 

4 JAMES MAYNARD 

just fail to prove bounded gaps using the fact that the primes have exponent of distribution θ for any θ < 1/2, but succeed in doing so if we assume they have level of distribution θ > 1/2. The new ingredient in our method is to consider a more general form of the sieve weights 



Using such weights with λd1,...,dk is the key feature of our method. It allows us to improve on the previous choice of sieve weights by an arbitrarily large factor, provided that k is sufficiently large. It is the extra flexibility gained by allowing the weights to depend on the divisors of each factor individually which gives this improvement. 

The idea to use such weights is not entirely new. Selberg [8, Page 245] suggested the possible use of similar weights in his work on approximations to the twin prime problem, and Goldston and Yıldırım [6] considered similar weights in earlier work on the GPY method, but with the support restricted to di < R<sup>1/k</sup> for all i. 

We comment that our choice of λd1,...,dk will look like 



for a suitable smooth function f . For our precise choice of λd1,...,dk (given in Proposition 4.1) we find it convenient to give a slightly different form of λd1,...,dk, but weights of the form (2.5) should produce essentially the same results. 

# 3. Notation 

We shall view k as a fixed integer, and H = {h1, . . . , hk} as a fixed admissible set. In particular, any constants implied by the asymptotic notation o, O or ≪ may depend on k and H. We will let N denote a large integer, and all asymptotic notation should be interpreted as referring to the limit N →∞. 

All sums, products and suprema will be assumed to be taken over variables lying in the natural numbers N = {1, 2, . . . } unless specified otherwise. The exception to this is when sums or products are over a variable p, which instead will be assumed to lie in the prime numbers P = {2, 3, . . ., }. 

Throughout the paper, ϕ will denote the Euler totient function, τr(n) the number of ways of writing n as a product of r natural numbers and µ the Moebius function. We will let ǫ be a fixed positive real number, and we may assume without further comment that ǫ is sufficiently small at various stages of our argument. We let pn denote the n<sup>th</sup> prime, and #A denote the number of elements of a finite set A. We use ⌊x⌋ to denote the largest integer n ≤ x, and ⌈x⌉ the smallest integer n ≥ x. We let (a, b) be the greatest common divisor of integers a and b. Finally, [a, b] will denote the closed interval on the real line with endpoints a and b, except for in Section 5 where it will denote the least common multiple of integers a and b instead. 



We will find it convenient to choose our weights wn to be zero unless n lies in a fixed residue class v0 (mod W), where W =<sup>�</sup> p≤D0<sup>p. This is a technical modification which removes some</sup> minor complications in dealing with the effect of small prime factors. The precise choice of D0 is unimportant, but it will suffice to choose 



5 

SMALL GAPS BETWEEN PRIMES 

so certainly W ≪ (log log N)<sup>2</sup> by the prime number theorem. By the Chinese remainder theorem, we can choose v0 such that v0 + hi is coprime to W for each i since H is admissible. When n ≡ v0 (mod W), we choose our weights wn of the form (2.4). We now wish to estimate the sums 



We evaluate these sums using the following proposition. 

Proposition 4.1. Let the primes have exponent of distribution θ > 0, and let R = N<sup>θ/2−δ</sup> for some small fixed δ > 0. Let λd1,...,dk be defined in terms of a fixed smooth function F by 



whenever (<sup>�k</sup> i=1<sup>di, W)=1,andletλd</sup> 1<sup>,...,d</sup> k<sup>=0otherwise.Moreover,letFbe supported on</sup> Rk = {(x1, . . . , xk) ∈ [0, 1]<sup>k</sup> :<sup>�k</sup> i=1<sup>xi≤1}.Then we have</sup> 



provided Ik(F) � 0 and Jk<sup>(m)(F) �0 for each m, where</sup> 



We recall that if S 2 is large compared to S 1, then using the GPY method we can show that there are infinitely many integers n such that several of the n + hi are prime. The following proposition makes this precise. 

Proposition 4.2. Let the primes have level of distribution θ > 0. Let δ > 0 and H = {h1, . . . , hk} be an admissible set. Let Ik(F) and Jk<sup>(m)(F)begivenasinProposition4.1,</sup> and let Sk denote the set of Riemann-integrable functions F : [0, 1]<sup>k</sup> → R supported on Rk = {(x1, . . . , xk) ∈ [0, 1]<sup>k</sup> :<sup>�k</sup> i=1<sup>xi≤1} with Ik(F) �0 andJ</sup> k<sup>(m)(F) �0 for each m.Let</sup> 



Then there are infinitely many integers n such that at least rk of the n + hi (1 ≤ i ≤ k) are prime. In particular, lim infn(pn+rk−1 − pn) ≤ max1≤i, j≤k(hi − h j). 

6 

JAMES MAYNARD 

Proof of Proposition 4.2. We let S = S 2 − ρS 1, and recall that from Section 2 that if we can show S > 0 for all large N, then there are infinitely many integers n such that at least ⌊ρ + 1⌋ of the n + hi are prime. 

We put R = N<sup>θ/2−δ</sup> for a small δ > 0. By the definition of Mk, we can choose F0 ∈Sk such that<sup>�k</sup> m=1<sup>J</sup> k<sup>(m)(F0)>(Mk −δ)Ik(F0)>0.SinceF0is Riemann-integrable, there is a smooth</sup> function F1 such that<sup>�k</sup> m=1<sup>J</sup> k<sup>(m)(F1)>(Mk−2δ)Ik(F1)>0.UsingProposition 4.1,we can</sup> then choose λd1,...,dk such that 



If ρ = θMk/2 − ǫ then, by choosing δ suitably small (depending on ǫ), we see that S > 0 for all large N. Thus there are infinitely many integers n for which at least ⌊ρ + 1⌋ of the n + hi are prime. Since ⌊ρ + 1⌋ = ⌈θMk/2⌉ if ǫ is suitably small, we obtain Proposition 4.2. □ 

Thus, if the primes have a fixed level of distribution θ, to show the existence of many of the n + hi being prime for infinitely many n ∈ N we only require a suitable lower bound for Mk. The following proposition establishes such a bound for different values of k. 

Proposition 4.3. Let k ∈ N, and Mk be as given by Proposition 4.2. Then 

- (1) We have M5 > 2. 

- (2) We have M105 > 4. 

- (3) If k is sufficiently large, we have Mk > log k − 2 log log k − 2. 

We now prove Theorems 1.1, 1.2, 1.3 and 1.4 from Propositions 4.2 and 4.3. 

First we consider Theorem 1.3. We take k = 105. By Proposition 4.3, we have M105 > 4. By the Bombieri-Vinogradov theorem, the primes have level of distribution θ = 1/2 − ǫ for every ǫ > 0. Thus, if we take ǫ sufficiently small, we have θM105/2 > 1. Therefore, by Proposition 4.2, we have lim inf(pn+1 − pn) ≤ max1≤i, j≤105(hi − h j) for any admissible set H = {h1, . . . , h105}. By computations performed by Thomas Engelsma (unpublished), we can choose<sup>2</sup> H such that 0 ≤ h1 < . . . < h105 and h105 − h1 = 600. This gives Theorem 1.3. 

If we assume the Elliott-Halberstam conjecture then the primes have level of distribution θ = 1 − ǫ. First we take k = 105, and see that θM105/2 > 2 for ǫ sufficiently small (since M105 > 4). Therefore, by Proposition 4.2, lim infn(pn+2 − pn) ≤ max1≤i, j≤105(hi − h j). Thus, choosing the same admissible set H as above, we see lim infn(pn+2 − pn) ≤ 600 under the Elliott-Halberstam conjecture. 

Next we take k = 5 and H = {0, 2, 6, 8, 12}, with θ = 1 − ǫ again. By Proposition 4.3 we have M5 > 2, and so θM5/2 > 1 for ǫ sufficiently small. Thus, by Proposition 4.2, lim infn(pn+1 − pn) ≤ 12 under the Elliott-Halberstam conjecture. This completes the proof of Theorem 1.4. 

> 2Explicitly, we can take H = {0, 10, 12, 24, 28, 30, 34, 42, 48, 52, 54, 64, 70, 72, 78, 82, 90, 94, 100, 112, 114, 118, 120, 124, 132, 138, 148, 154, 168, 174, 178, 180, 184, 190, 192, 202, 204, 208, 220, 222, 232, 234, 250, 252, 258, 262, 264, 268, 280, 288, 294, 300, 310, 322, 324, 328, 330, 334, 342, 352, 358, 360, 364, 372, 378, 384, 390, 394, 400, 402, 408, 412, 418, 420, 430, 432, 442, 444, 450, 454, 462, 468, 472, 478, 484, 490, 492, 498, 504, 510, 528, 532, 534, 538, 544, 558, 562, 570, 574, 580, 582, 588, 594, 598, 600}. This set was obtained from the website http://math.mit.edu/˜primegaps/ maintained by Andrew Sutherland. 

SMALL GAPS BETWEEN PRIMES 

7 

Finally, we consider the case when k is large. For the rest of this section, any constants implied by asymptotic notation will be independent of k. By the Bombieri-Vinogradov theorem, we can take θ = 1/2 − ǫ. Thus, by Proposition 4.3, we have for k sufficiently large 



We choose ǫ = 1/k, and see that θMk/2 > m if k ≥ Cm<sup>2</sup> e<sup>4m</sup> for some absolute constant C (independent of m and k). Thus, for any admissible set H = {h1, . . . , hk} with k ≥ Cm<sup>2</sup> e<sup>4m</sup> , at least m + 1 of the n + hi must be prime for infinitely many integers n. We can choose our set H to be the set {pπ(k)+1, . . . , pπ(k)+k} of the first k primes which are greater than k. This is admissible, since no element is a multiple of a prime less than k (and there are k elements, so it cannot cover all residue classes modulo any prime greater than k.) This set has diameter pπ(k)+k − pπ(k)+1 ≪ k log k. Thus lim infn(pn+m − pn) ≪ k log k ≪ m<sup>3</sup> e<sup>4m</sup> if we take k = ⌈Cm<sup>2</sup> e<sup>4m</sup> ⌉. This gives Theorem 1.1. 

We can now establish Theorem 1.2 by a simple counting argument. Given m, we let k = ⌈Cm<sup>2</sup> e<sup>4m</sup> ⌉ as above. Therefore if {h1, . . . , hk} is admissible, then there exists a subset {h<sup>′</sup> 1<sup>, . . . , h</sup> m<sup>′} ⊆{h1, . . . , hk} with the property that there are infinitely many integers n for which</sup> all of the n + h<sup>′</sup> i<sup>are prime (1 ≤i ≤m).</sup> 

We let A2 denote the set formed by starting with the given set A = {a1, . . . , ar}, and for each prime p ≤ k in turn removing all elements of the residue class modulo p which contains the fewest integers. We see that #A2 ≥ r<sup>�</sup> p≤k<sup>(1 −1/p)≫</sup> m<sup>r.Moreover, any subset of A</sup> 2 of size k must be admissible, since it cannot cover all residue classes modulo p for any prime p ≤ k. We let s = #A2, and since r is taken sufficiently large in terms of m, we may assume that s > k. We see there are �ks� sets H ⊆A2 of size k. Each of these is admissible, and so contains at least one subset {h<sup>′</sup> 1<sup>, . . . , h</sup> m<sup>′}⊆A2whichsatisfiestheprimem-tuplesconjecture.Any</sup> admissible set B ⊆A2 of size m is contained in �ks−−mm� sets H ⊆A2 of size k. Thus there are at least �ks��ks−−mm�−1 ≫m sm ≫m rm admissible sets B ⊆A2 of size m which satisfy the prime m-tuples conjecture. Since there are �mr � ≤ r<sup>m</sup> sets {h1, . . . , hm} ⊆A, Theorem 1.2 holds. We are left to establish Propositions 4.1 and 4.3. 

# 5. Selberg sieve manipulations 

In this section we perform initial manipulations towards establishing Proposition 4.1. These arguments are multidimensional generalizations of the sieve arguments of [3]. In particular, our approach is based on the elementary combinatorial ideas of Selberg. The aim is to introduce a change of variables to rewrite our sums S 1 and S 2 in a simpler form. 

Throughout the rest of the paper we assume that the primes have a fixed level of distribution θ, and R = N<sup>θ/2−δ</sup> . We restrict the support of λd1,...,dk to tuples for which the product d =<sup>�k</sup> i=1<sup>di</sup> is less than R and also satisfies (d, W) = 1 and µ(d)<sup>2</sup> = 1. We note that the condition µ(d)<sup>2</sup> = 1 implies that (di, d j) = 1 for all i � j. 

Lemma 5.1. Let 



8 

JAMES MAYNARD 



Proof. We expand out the square, and swap the order of summation to give 



We recall that here, and throughout this section, we are using [a, b] to denote the least common multiple of a and b. 

By the Chinese remainder theorem, the inner sum can be written as a sum over a single residue class modulo q = W<sup>�k</sup> i=1<sup>[di, ei], provided that the integers W, [d1, e1], . . . , [dk, ek] are</sup> pairwise coprime. In this case the inner sum is N/q + O(1). If the integers are not pairwise coprime then the inner sum is empty. This gives 



where<sup>�′</sup> is used to denote the restriction that we require W, [d1, e1], . . . , [dk, ek] to be pairwise coprime. To ease notation we will put λmax = supd1,...,dk |λd1,...,dk|. We now see that since λd1,...,dk is non-zero only when<sup>�k</sup> i=1<sup>di< R, the error term contributes</sup> 



which will be negligible. 

In the main sum we wish to remove the dependencies between the di and the e j variables. We use the identity 



to rewrite the main term as 



We recall that λd1,...,dk is supported on integers d1, . . . , dk with (di, W) = 1 for each i and (di, d j) = 1 for all i � j. Thus we may drop the requirement that W is coprime to each of the [di, ei] from the summation, since these terms have no contribution. Similarly, we may drop the requirement that the di variables are all pairwise coprime, and the requirement that the ei variables are all pairwise coprime. Thus the only remaining restriction coming from the pairwise coprimality of W, [d1, e1], . . . , [dk, ek] is that (di, e j) = 1 for all i � j. 

SMALL GAPS BETWEEN PRIMES 

9 

We can remove the requirement that (di, e j) = 1 by multiplying our expression by<sup>�</sup> si, j|di,e j<sup>µ(s</sup> i, j<sup>).</sup> We do this for all i, j with i � j. This transforms the main term to 



We can restrict the si, j to be coprime to ui and u j, because terms with si, j not coprime to ui or u j make no contribution to our sum. This is because λd1,...,dk = 0 unless (di, d j) = 1. Similarly we can further restrict our sum so that si, j is coprime to si,a and sb, j for all a � j and b � i. We denote the summation over s1,2, . . . , sk,k−1 with these restrictions by<sup>�∗</sup> . 

We now introduce a change of variables to make the estimation of the sum more straightforward. We let 



This change is invertible. For d1, . . . , dk with<sup>�k</sup> i=1<sup>disquare-free we find that</sup> 





Thus any choice of yr1,...,rk supported on r1, . . . , rk, with the product r =<sup>�k</sup> i=1<sup>risquare-free</sup> and satisfying r < R and (r, W) = 1, will give a suitable choice of λd1,...,dk. We let ymax = supr1,...,rk |yr1,...,rk|. Now, since d/ϕ(d) =<sup>�</sup> e|d<sup>1/ϕ(e)for square-freed,we findby takingr′=</sup> �ki=1<sup>ri/di that</sup> 





10 

JAMES MAYNARD 

In the last line we have taken u = dr<sup>′</sup> , and used the fact τk(dr<sup>′</sup> ) ≥ τk(r<sup>′</sup> ). Hence the error term O(λ<sup>2</sup> max<sup>R2(log N)2k) is of size O(y2</sup> max<sup>R2(log N)4k).</sup> Substituting our change of variables (5.7) into the main term (5.6), and using the above estimate for the error term, we obtain 



where a j = u j �i� j<sup>s</sup> j,i<sup>andb</sup> j<sup>=u</sup> j �i� j<sup>s</sup> i, j<sup>.Inthese expressions we have used the factthat</sup> we have restricted si, j to be coprime to the other terms in the expression for ai and b j. For the same reason we may rewrite µ(a j) as µ(u j)<sup>�</sup> i� j<sup>µ(s</sup> i, j<sup>), and similarly for ϕ(a</sup> j<sup>), µ(b</sup> j<sup>) and</sup> ϕ(b j). This gives us 



We see that there is no contribution from si, j with (si, j, W) � 1 because of the restricted support of y. Thus we only need to consider si, j = 1 or si, j > D0. The contribution when si, j > D0 is 



Thus we may restrict our attention to the case when si, j = 1 ∀i � j. This gives 



We recall that R<sup>2</sup> = N<sup>θ−2δ</sup> ≤ N<sup>1−2δ</sup> and W ≪ N<sup>δ</sup> , and so the first error term dominates. This gives the result. □ 

We now consider S 2. We write S 2 =<sup>�k</sup> m=1<sup>S (</sup> 2<sup>m), where</sup> 



We now estimate S 2<sup>(m)</sup> in a similar way to our treatment of S 1. Lemma 5.2. Let 



where g is the totally multiplicative function defined on primes by g(p) = p − 2. Let ymax<sup>(m)=</sup> supr1,...,rk |y<sup>(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>|.Then for any fixed A > 0 we have</sup> 



SMALL GAPS BETWEEN PRIMES 

11 

Proof. We first expand out the square and swap the order of summation to give 



As with S 1, the inner sum can be written as a sum over a single residue class modulo q = W<sup>�k</sup> i=1<sup>[di, ei], provided that W, [d1, e1], . . . , [dk, ek] are pairwise coprime.The integer n + hm</sup> will lie in a residue class coprime to the modulus if and only if dm = em = 1. In this case the inner sum will contribute XN/ϕ(q) + O(E(N, q)), where 







If either one pair of W, [d1, e1], . . . , [dk, ek] share a common factor, or if either dm or em are not 1, then the contribution of the inner sum is zero. Thus we obtain 



where we have written q = W<sup>�k</sup> i=1<sup>[di, ei].</sup> 

We first deal with the contribution from the error terms. From the support of λd1,...,dk, we see that we only need to consider square-free q with q < R<sup>2</sup> W. Given a square-free integer r, there are at most τ3k(r) choices of d1, . . . , dk, e1, . . . , ek for which W<sup>�k</sup> i=1<sup>[di, ei]=r.We also</sup> recall from (5.9) that λmax ≪ ymax(log R)<sup>k</sup> . Thus the error term contributes 



By Cauchy-Schwarz, the trivial bound E(N, q) ≪ N/ϕ(q), and our hypothesis that the primes have level of distribution θ, this contributes for any fixed A > 0 



We now concentrate on the main sum. As in the treatment of S 1 in the proof of Lemma 5.1, we rewrite the conditions (di, e j) = 1 by multiplying our expression by<sup>�</sup> si, j|di,e j<sup>µ(s</sup> i, j<sup>).Again</sup> we may restrict si, j to be coprime to ui, u j, si,a and sb, j for all a � j and b � i. We denote the summation subject to these restrictions by<sup>�∗</sup> . We also split the ϕ([di, ei]) terms by using the equation (valid for square-free di, ei) 





12 

JAMES MAYNARD 

where g is the totally multiplicative function defined on primes by g(p) = p − 2. This gives us a main term of 



We have now separated the dependencies between the e and d variables, so again we make a substitution. We let 





We note y<sup>(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>= 0 unless r</sup> m<sup>= 1.Substituting this into (5.22), we obtain a main term of</sup> 



where a j = u j �i� j<sup>s</sup> j,i<sup>and b</sup> j<sup>=u</sup> j �i� j<sup>s</sup> i, j<sup>for each 1≤j≤k.As before, we have replaced</sup> µ(a j) with µ(u j)<sup>�</sup> i� j<sup>µ(s</sup> j,i<sup>) (and similarly for g(a</sup> j<sup>), µ(b</sup> j<sup>) and g(b</sup> j<sup>)).This is valid since terms</sup> with a j or b j not square-free make no contribution. 

We see the contribution from si, j � 1 is of size 



Thus we find that 



Finally, by the prime number theorem, XN = N/ log N + O(N/(log N)<sup>2</sup> ). This error term contributes 



which can be absorbed into the first error term of (5.26). This completes the proof. 

□ 

Remark. In our proof of Lemma 5.2 we only really require λd1,...,dk to be supported on d1, . . . , dk satisfying<sup>�</sup> i� j<sup>d</sup> i<sup>< R for allj instead of �</sup> i<sup>k</sup> =1<sup>di< R.For k ≥3, the numerical benefit of this</sup> extension is small and so we do not consider it further. 

Remark. As our result relies on the Bombieri-Vinogradov theorem, the implied constant in the error term is not effectively computable. However, if we restrict the λd1,...,dk to be supported on di which are coprime to the largest prime factor of a possible exceptional modulus of a 

SMALL GAPS BETWEEN PRIMES 

13 

primitive character then we can make this error term (and all others in this paper) effective at the cost of a negligible error. 

We now relate our new variables y<sup>(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>to the y</sup> r1,...,rk<sup>variables from S</sup> 1<sup>.</sup> 

Lemma 5.3. If rm = 1 then 



Proof. We assume throughout the proof that rm = 1. We first substitute our expression (5.8) into the definition (5.23). This gives 



We swap the summation of the d and a variables to give 



We can now evaluate the sum over d1, . . . , dk explicitly. This gives 



We see that from the support of ya1,...,ak that we may restrict the summation over a j to (a j, W) = 1. Thus either a j = r j or a j > D0r j. For j � m, the total contribution from a j � r j is 



Thus we find that the main contribution is when a j = r j for all j � m. We have 



We note that g(p)p/ϕ(p)<sup>2</sup> = 1 + O(p<sup>−2</sup> ). Thus, since the contribution is zero unless<sup>�k</sup> i=1<sup>riis</sup> coprime to W, we see that the product in the above expression may be replaced by 1 +O(D<sup>−</sup> 0<sup>1).</sup> This gives the result. □ 

14 

JAMES MAYNARD 

# 6. Smooth choice of y 

We now choose suitable values for our y variables, and complete the proof of Proposition 4.1. 

We first give some comments to motivate our choice of the y variables, which we believe should be close to optimal. We wish to choose y so as to maximize the ratio of the main terms of S 2 and S 1. If we use Lagrangian multipliers to maximize this ratio (treating all error terms as zero) we arrive at the condition that 



for some fixed constant λ. The y terms are supported on integers free of small prime factors, and for most integers r free of small prime factors we have g(r) ≈ ϕ(r) ≈ r, and so the above condition reduces to 



This condition looks smooth (it has no dependence on the prime factorization of the ri), and should be able to be satisfied if yr1,...,rk is a smooth function of the ri variables. Motivated by the above, when the product r =<sup>�k</sup> i=1<sup>risatisfies (r, W) = 1 and µ(r)2= 1 we choose</sup> 



for some smooth function F : R<sup>k</sup> → R, supported on Rk = {(x1, . . . , xk) ∈ [0, 1]<sup>k</sup> :<sup>�k</sup> i=1<sup>xi≤</sup> 1}. As previously required, we set yr1,...,rk = 0 if the product r is either not coprime to W or is not square-free. With this choice of y, we can obtain suitable asymptotic estimates for S 1 and S 2. 

We will use the following Lemma to estimate our sums S 1 and S 2 with this choice of y. 

Lemma 6.1. Let A1, A2, L > 0. Let γ be a multiplicative function satisfying 



and 



for any 2 ≤ w ≤ z. Let g be the totally multiplicative function defined on primes by g(p) = γ(p)/(p−γ(p)). Finally, let G : [0, 1] → R be smooth, and let Gmax = supt∈[0,1](|G(t)|+|G<sup>′</sup> (t)|). Then 



where 



Here the constant implied by the ‘O’ term is independent of G and L. 

Proof. This is [3, Lemma 4], with κ = 1 and slight changes to the notation. 



15 

SMALL GAPS BETWEEN PRIMES 

We now finish our estimations of S 1 and S 2<sup>(m), completing the proof of Proposition 4.1.We</sup> first estimate S 1. 

Lemma 6.2. Let yr1,...,rk be given in terms of a smooth function F by (6.3), with F supported on Rk = {(x1, . . . , xk) ∈ [0, 1]<sup>k</sup> :<sup>�k</sup> i=1<sup>xi≤1}.Let</sup> 

Then we have 



where 



Proof. We substitute our choice (6.3) of y into our expression of S 1 in terms of yr1,...,rk given by Lemma 5.1. This gives 



We note that two integers a and b with (a, W) = (b, W) = 1 but (a, b) � 1 must have a common prime factor which is greater than D0. Thus we can drop the requirement that (ui, u j) = 1, at the cost of an error of size 





Thus we are left to evaluate the sum 



We can now estimate this sum by k applications of Lemma 6.1, dealing with the sum over each ui in turn. For each application we take 







16 JAMES MAYNARD 

and A1 and A2 fixed constants of suitable size. This gives 



(6.9) 

We now combine (6.9) with (6.4) and (6.5) to obtain the result. 

Lemma 6.3. Let yr1,...,rk, F and Fmax be as described in Lemma 6.2. Then we have 

where 



Proof. The estimation of S 2<sup>(m)</sup> is similar to the estimation of S 1. We first estimate y<sup>(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>.We</sup> recall that y<sup>(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>=0unlessr</sup> m<sup>=1andr=�</sup> i<sup>k</sup> =1<sup>risatisfies(r, W)=1andµ(r)2=1,in</sup> which case y<sup>(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>is given in terms of y</sup> r1,...,rk<sup>by Lemma 5.3.We first concentrate on this case</sup> when y<sup>(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>�0.We substitute our choice(6.3) ofyinto ourexpression fromLemma 5.3.</sup> This gives 



We can see from this that y<sup>(</sup> max<sup>m)≪ϕ(W)F</sup> max<sup>(log R)/W.We nowestimate the sum over uin</sup> (6.10). We apply Lemma 6.1 with 



and with A1, A2 suitable fixed constants. This gives us 





where 



Thus we have shown that if rm = 1 and r =<sup>�k</sup> i=1<sup>risatisfies(r, W)=1andµ(r)2=1then</sup> y<sup>(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>is given by (6.13), and otherwise y(</sup> r<sup>m</sup> 1,...,<sup>)</sup> rk<sup>= 0.We now substitute this into our expression</sup> 

SMALL GAPS BETWEEN PRIMES 

17 

from Lemma 5.2, namely 



We remove the condition that (ri, r j) = 1 in the same way we did when considering S 1. Instead of (6.5), this introduces an error which is of size 

(6.17) 



We estimate this by applying Lemma 6.1 to each summation variable in turn. In each case we take 



and A1, A2 suitable fixed constants. This gives 



as required. 

□ 

Remark. If F(t1, . . . , tk) = G(<sup>�k</sup> i=1<sup>ti) for some function G, then Ik(F) andJ</sup> k<sup>(m)(F) simplify to</sup> Ik(F) = �01<sup>G(t)2tk−1dt/(k −1)! and J</sup> k<sup>(m)(F) =</sup> �01<sup>(</sup> �t 1<sup>G(v)dv)2tk−2dt/(k −2)! for each m, which</sup> is equivalent to the results obtained using the original GPY method using weights given by (2.3). 

Remark. Tao gives an alternative approach to arrive at his equivalent of Proposition 4.1. His approach is to define λd1,...,dk in terms of a suitable smooth function f (t1, . . . , tk) as in (2.5). He then estimates the corresponding sums directly using Fourier integrals. This is somewhat 

18 

JAMES MAYNARD 

similar to the original paper of Goldston, Pintz and Yıldırım [5]. Our function F corresponds to f (t1, . . . , tk) differentiated with respect to each coordinate. 

7. Choice of smooth weight for large k 

In this section we establish part (3) of Proposition 4.3. Our argument here is closely related to that of Tao, who uses a probability theory proof. 

We let Sk denote the set of Riemann-integrable functions F : [0, 1]<sup>k</sup> → R supported on Rk = {(x1, . . . , xk) ∈ [0, 1]<sup>k</sup> :<sup>�k</sup> i=1<sup>xi≤1}withIk(F)�0andJ</sup> k<sup>(m)(F)�0foreachm.We</sup> would like to obtain a lower bound for 



Remark. Let Lk denote the linear operator defined by 



whenever (u1, . . . , uk) ∈Rk, and zero otherwise. We expect that if F maximizes the ratio �km=1<sup>J</sup> k<sup>(m)(F)/Ik(F),thenFisaneigenfunction forLk,andthe correspondingeigenvalue is</sup> the value of ratio at F. Unfortunately the author has not been able to solve the eigenvalue equation for Lk when k > 2. 

We obtain a lower bound for Mk by constructing a function F = Fk which makes the ratio �km=1<sup>J</sup> k<sup>(m)(F)/Ik(F) large provided k is large.We choose Fto be of the form</sup> 



for some smooth function g : [0, ∞] → R, supported on [0, T ]. We see that with this choice F is symmetric, and so Jk<sup>(m)(F) is independent of m. Thus we only need to consider Jk=J</sup> k<sup>(1)(F).</sup> Similarly we write Ik = Ik(F). 

The key observation is that if the center of mass �0∞<sup>ug(u)2du/</sup> �0∞<sup>g(u)2du of g2is strictly</sup> less than 1, then for large k we expect that the constraints<sup>�k</sup> i=1<sup>ti≤1tobeabletobe</sup> dropped at the cost of only a small error. This is because (by concentration of measure) the main contribution to the unrestricted integrals Ik<sup>′=</sup> �0∞<sup>· · ·</sup> �0∞ �ki=1<sup>g(kti)2dt1 . . . dtkand</sup> Jk<sup>′=</sup> �0∞<sup>· · ·</sup> �0∞<sup>(</sup> �0∞ �ki=1<sup>g(kti)dt1)2dt2 . . . dtk should come primarily from when �</sup> i<sup>k</sup> =1<sup>ti is close</sup> to the center of mass. Therefore we would expect the contribution when<sup>�k</sup> i=1<sup>ti>1tobe</sup> small if the center of mass is less than 1, and so Ik and Jk are well approximated by Ik<sup>′andJ</sup> k<sup>′</sup> in this case. 

To ease notation we let γ = �u≥0<sup>g(u)2du, and restrict our attention to g such that γ > 0.We</sup> have 



We now consider Jk. Since squares are non-negative, we obtain a lower bound for Jk if we restrict the outer integral to<sup>�k</sup> i=2<sup>ti<1 −T/k.This has the advantage that, by the support of</sup> 

SMALL GAPS BETWEEN PRIMES 

19 

g, there are no further restrictions on the inner integral. Thus 



We write the right hand side of (7.5) as Jk<sup>′−Ek, where</sup> 



First we wish to show the error integral Ek is small. We do this by comparison with a second moment. We expect the bound (7.13) for Ek to be small if the center of mass of g<sup>2</sup> is strictly less than (k − T )/(k − 1). Therefore we introduce the restriction on g that 



To simplify notation, we put η = (k − T )/(k − 1) − µ > 0. If<sup>�k</sup> i=2<sup>ui>k −Tthen �k</sup> i=2<sup>ui></sup> (k − 1)(µ + η), and so we have 



Since the right hand side of (7.9) is non-negative for all ui, we obtain an upper bound for Ek if we multiply the integrand by η<sup>−2</sup> (<sup>�k</sup> i=2<sup>ui/(k −1) −µ)2, and then drop the requirement that</sup> �ki=1<sup>ui> k −T.This gives us</sup> 



We expand out the inner square. All the terms which are not of the form u<sup>2</sup> j<sup>we can calculate</sup> explicitly as an expression in µ and γ. We find 



20 

JAMES MAYNARD 

For the u<sup>2</sup> j<sup>terms we see that u2</sup> j<sup>g(u j)2≤Tu jg(u j)2 from the support of g.Thus</sup> 



This gives 



Since (k − 1)η<sup>2</sup> ≥ k(1 − T/k − µ)<sup>2</sup> and µ ≤ 1, we find that putting together (7.4), (7.5), (7.6) and (7.13), we obtain 



To maximize our lower bound (7.14), we wish to maximize �0T<sup>g(u)dusubjecttothecon-</sup> straints that �0T<sup>g(u)2du = γ and</sup> �0T<sup>ug(u)2du = µγ.Thus we wish to maximize the expression</sup> 





with respect to α, β and the function g. By the Euler-Lagrange equation, this occurs when ∂∂g<sup>(g(t) −αg(t)2 −βtg(t)2) = 0 for all t∈[0, T].Thus we see that</sup> 



Since the ratio we wish to maximize is unaffected if we multiply g by a positive constant, we restrict our attention to functions g is of the form 1/(1 + At) for t ∈ [0, T ] and for some constant A > 0. With this choice of g we find that 



We choose T such that 1 + AT = e<sup>A</sup> (which is close to optimal). With this choice we find that µ = 1/(1 − e<sup>−A</sup> ) − A<sup>−1</sup> and T ≤ e<sup>A</sup> /A. Thus 1 − T/k − µ ≥ A<sup>−1</sup> (1 − A/(e<sup>A</sup> − 1) − e<sup>A</sup> /k). Substituting (7.17) into (7.14), and then using these expressions, we find that 



provided the right hand side is positive. Finally, we choose A = log k − 2 log log k > 0. For k sufficiently large we have 



when k is sufficiently large. 

SMALL GAPS BETWEEN PRIMES 

21 

8. Choice of weight for small k 

In this section we establish parts (1) and (2) of Proposition 4.3. In order to get a suitable lower bound for Mk when k is small, we will consider approximations to the optimal function F of the form 



for polynomials P. By the symmetry of<sup>�k</sup> m=1<sup>J</sup> k<sup>(m)(F)andIk(F),werestrictourattention</sup> to polynomials which are symmetric functions of t1, . . . , tk. (If F satisfies LkF = λF then Fσ = F(σ(t1), . . . , σ(tk)) also satisfies this for every permutation σ of t1, . . . , tk. Thus the symmetric function which is the average of Fσ over all such permutations would satisfy this eigenfunction equation, and so we expect there to be an optimal function which is symmetric.) Any such polynomial can be written as a polynomial expression in the power sum polynomials P j =<sup>�</sup> i<sup>k</sup> =1<sup>t j</sup> i<sup>.</sup> 



where 



is a polynomial of degree b which depends only on b and j. 

Proof. We first show by induction on k that 



We consider the integration with respect to t1. The limits of integration are 0 and 1 −<sup>�k</sup> i=2<sup>ti</sup> for (t2, . . . , tk) ∈Rk−1. By substituting v = t1/(1 −<sup>�k</sup> i=2<sup>ti) we find</sup> 



Here we used the beta function identity �01<sup>ta(1 −t)bdt = a!b!/(a + b + 1)! in the last line.We</sup> now see (8.2) follows by induction. 

By the binomial theorem, 





22 

JAMES MAYNARD 

Thus, applying (8.2), we obtain 



For computations b will be small, and so we find it convenient to split the summation depending on how many of the bi are non-zero. Given an integer r, there are �kr� ways of choosing r of b1, . . . , bk to be non-zero. Thus 



This gives the result. 



It is straightforward to extend Lemma 8.1 to more general combinations of the symmetric power polynomials. In this paper we will concentrate on the case when P is a polynomial expression in only P1 and P2 for simplicity. We comment the polynomials Gb, j are not problematic to calculate numerically for small values of b. We now use Lemma 8.1 to obtain a manageable expression for Ik(F) and Jk<sup>(m)(F) with this choice of P.</sup> 

Lemma 8.2. Let F be given in terms of a polynomial P by (8.1). Let P be given in terms of a polynomial expression in the symmetric power polynomials P1 =<sup>�k</sup> i=1<sup>tiand P2=�k</sup> i=1<sup>t</sup> i<sup>2by</sup> P =<sup>�d</sup> i=1<sup>ai(1 −P1)biPc</sup> 2<sup>ifor constants ai∈R and non-negative integers bi, ci.Then for each</sup> 1 ≤ m ≤ k we have 



where 



and where G is the polynomial given by Lemma 8.1. 

Proof. We first consider Ik(F). We have, using Lemma 8.1, 



SMALL GAPS BETWEEN PRIMES 

23 

We now consider Jk<sup>(m)(F).Since F is symmetric in t1, . . . , tk we see that J</sup> k<sup>(m)(F) is independent</sup> of m, and so it suffices to only consider Jk<sup>(1)(F).We have</sup> 





Combining (8.9) and (8.10) gives the result. 

□ 

We see from Lemma 8.2 that Ik(F) and<sup>�k</sup> m=1<sup>J</sup> k<sup>(m)(F)canbothbeexpressedasquadratic</sup> forms in the coefficients a = (a1, . . . , ad) of P. Moreover, these will be positive definite real quadratic forms. Thus in particular we find that 



for two rational symmetric positive definite matrices A1, A2, which can be calculated explicitly in terms of k for any choice of the exponents bi, ci. Maximizing expressions of this form has a known solution. 

Lemma 8.3. Let A1, A2 be real, symmetric positive definite matrices. Then 



is maximized when a is an eigenvector of A<sup>−</sup> 1<sup>1A2correspondingtothelargesteigenvalueof</sup> A<sup>−</sup> 1<sup>1A2.The value of the ratio at its maximum is this largest eigenvalue.</sup> 

Proof. We see that multiplying a by a non-zero scalar doesn’t change the ratio, so we may assume without loss of generality that a<sup>T</sup> A1a = 1. By the theory of Lagrangian multipliers, a<sup>T</sup> A2a is maximized subject to a<sup>T</sup> A1a = 1 when 

(8.12) L(a, λ) = a<sup>T</sup> A2a − λ(a<sup>T</sup> A1a − 1) 

24 JAMES MAYNARD 

is stationary. This occurs when (using the symmetricity of A1, A2) 



It then is clear that a<sup>T</sup> A1a = λ<sup>−1</sup> a<sup>T</sup> A2a. □ 

Proof of parts (1) and (2) of Proposition 4.3. To establish Proposition 4.3 we rely on some computer calculation to calculate a lower bound for Mk. We let F be given in terms of a polynomial P by (8.1). We let P be given by a polynomial expression in P1 =<sup>�k</sup> i=1<sup>tiand</sup> P2 =<sup>�k</sup> i=1<sup>t</sup> i<sup>2whichisalinearcombinationofallmonomials(1−P1)bPc</sup> 2<sup>withb+2c≤</sup> 11. There are 42 such monomials, and with k = 105 we can calculate the 42 × 42 rational symmetric matrices A1 and A2 corresponding to the coefficients of the quadratic forms Ik(F) and<sup>�k</sup> m=1<sup>J</sup> k<sup>(m)(F).We then find3 that the largest eigenvalue of A</sup> 1<sup>−1A2 is</sup> 

(8.15) λ ≈ 4.0020697 . . . > 4. 

Thus M105 > 4. This verifies part (2) of Proposition 4.3. We comment that by taking a rational approximation to the corresponding eigenvector, we can verify this lower bound by calculating the ratio<sup>�k</sup> m=1<sup>J</sup> k<sup>(m)(F)/Ik(F) using only exact arithmetic.</sup> For part (1) of Proposition 4.3, we take k = 5 and 



# 9. Acknowledgements 

The author would like to thank Andrew Granville, Roger Heath-Brown, Dimitris Koukoulopoulos and Terence Tao for many useful conversations and suggestions. 

The work leading to this paper was started whilst the author was a D.Phil student at Oxford and funded by the EPSRC (Doctoral Training Grant EP/P505216/1), and was finished when the author was a CRM-ISM postdoctoral fellow at the Universit´e de Montr´eal. 

# References 

- [1] P. D. T. A. Elliott and H. Halberstam. A conjecture in prime number theory. In Symposia Mathematica, Vol. IV (INDAM, Rome, 1968/69), pages 59–72. Academic Press, London, 1970. 

- [2] J. Friedlander and A. Granville. Limitations to the equi-distribution of primes. I. Ann. of Math. (2), 129(2):363–382, 1989. 

- [3] D. A. Goldston, S. W. Graham, J. Pintz, and C. Y. Yıldırım. Small gaps between products of two primes. Proc. Lond. Math. Soc. (3), 98(3):741–774, 2009. 

- [4] D. A. Goldston, J. Pintz, and C. Y. Yıldırım. Primes in tuples. III. On the difference pn+ν − pn. Funct. Approx. Comment. Math., 35:79–89, 2006. 

- [5] D. A. Goldston, J. Pintz, and C. Y. Yıldırım. Primes in tuples. I. Ann. of Math. (2), 170(2):819–862, 2009. 

> 3An ancillary Mathematica R⃝ file detailing these computations is available alongside this paper at www.arxiv.org. 

SMALL GAPS BETWEEN PRIMES 25 

- [6] D. A. Goldston and C. Y. Yıldırım. Higher correlations of divisor sums related to primes. III. Small gaps between primes. Proc. Lond. Math. Soc. (3), 95(3):653–686, 2007. 

- [7] D. H. J. Polymath. A new bound for gaps between primes. Preprint. 

- [8] A. Selberg. Collected papers. Vol. II. Springer-Verlag, Berlin, 1991. With a foreword by K. Chandrasekharan. 

- [9] Y. Zhang. Bounded gaps between primes. Ann. of Math.(2), to appear. 

- Centre de recherches mathematiques´ , Universite´ de Montreal´ , Pavillon Andre´-Aisenstadt, 2920 Chemin 

- de la tour, Room 5357, Montreal´ (Quebec´ ) H3T 1J4 

   - E-mail address: maynardj@dms.umontreal.ca 

