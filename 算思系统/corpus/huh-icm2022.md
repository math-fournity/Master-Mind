# **Combinatorics and Hodge theory** 

**June Huh** 

## **Abstract** 

I will tell two interrelated stories illustrating fruitful interactions between combinatorics and Hodge theory. The first is that of Lorentzian polynomials, based on my joint work with Petter Brändén. They link continuous convex analysis and discrete convex analysis via tropical geometry, and they reveal subtle information on graphs, convex bodies, projective varieties, Potts model partition functions, log-concave polynomials, and highest weight representations of general linear groups. The second is that of intersection cohomology of matroids, based on my joint work with Tom Braden, Jacob Matherne, Nick Proudfoot, and Botong Wang. It shows a surprising parallel between the theory of convex polytopes, Coxeter groups, and matroids. After giving an overview of the similarity, I will outline proofs of two combinatorial conjectures on matroids, the nonnegativity conjecture for their Kazhdan-Lusztig coefficients and the top-heavy conjecture for the lattice of flats. 

> © 2026 International Mathematical Union Published by EMS Press. DOI 10.4171/ICM2022/? Proc. Int. Cong. Math. 2022, Vol. ?, pp. 2–29 

## **1. Introduction** 

One may seek unity in mathematics through the eyes of _cohomology_ . Let _𝑋_ be a mathematical object of “dimension” _𝑑_ . The object may be analytic, arithmetic, geometric, or combinatorial, and the precise notion of dimension will depend on the context. Curiously, often it is possible to construct from _𝑋_ in a natural way a graded real vector space 



The new object _𝐴_ ( _𝑋_ ), called the cohomology of _𝑋_ , often encodes essential information on _𝑋_ . When two objects _𝑋_ and _𝑌_ of the same kind are related in a particular way, the relationship is often reflected on their cohomologies _𝐴_ ( _𝑋_ ) and _𝐴_ ( _𝑌_ ), and this property can be exploited to extend our understanding. Primary consumers of this viewpoint so far were topologists and geometers, and a great number of triumphs in topology and geometry are based on a construction of _𝐴_ ( _𝑋_ ) from _𝑋_ . Interestingly, sometimes, satisfactory and equally useful cohomologies exist even when _𝑋_ does not have a geometric structure in the conventional sense. In particular, when _𝑋_ is a _matroid_ , the study of _𝐴_ ( _𝑋_ ) led to proofs of a few combinatorial conjectures that were beyond reach with traditional methods **[1, 6, 12]** . 

There are a few pieces of evidence for the unity in the above context. The list is short, but the pattern is remarkable. For example, _𝐴_ ( _𝑋_ ) can be the ring of algebraic cycles modulo homological equivalence on a smooth projective variety **[36]** , the combinatorial cohomology of a convex polytope **[45]** , the Soergel bimodule of a Coxeter group element **[26]** , the Chow ring of a matroid **[1]** , the conormal Chow ring of a matroid **[6]** , or the intersection cohomology of a matroid **[12]** . In these cases, the cohomology comes equipped with a symmetric bilinear pairing _𝑃_ : _𝐴_<sup>∗</sup> ( _𝑋_ ) × _𝐴_<sup>_𝑑_−∗</sup> ( _𝑋_ ) → R and a graded linear map _𝐿_ : _𝐴_<sup>∗</sup> ( _𝑋_ ) → _𝐴_<sup>∗+1</sup> ( _𝑋_ ) that are symmetric in the sense that 



The linear map _𝐿_ is allowed to vary in a family _𝐾_ ( _𝑋_ ), a convex cone in the space of linear operators on _𝐴_ ( _𝑋_ ). Here _𝑃_ is for Poincaré, _𝐿_ is for Lefschetz, and _𝐾_ is for Kähler, who first emphasized the importance of the respective objects in topology and geometry. In good cases, _𝐴_<sup>0</sup> ( _𝑋_ ) has a distinguished generator 1, and one expects the following properties to hold for every nonnegative integer _𝑘_ ≤<sup>_<u>𝑑</u>_</sup> 2<sup>:</sup> 





is nondegenerate ( _Poincaré duality_ for _𝑋_ ). 

(2) For any _𝐿_ 1 _, . . . , 𝐿𝑑_ −2 _𝑘_ ∈ _𝐾_ ( _𝑋_ ), the linear map 



is an isomorphism ( _hard Lefschetz property_ for _𝑋_ ). 

**3 Combinatorics and Hodge theory** 





is positive definite on the kernel of the linear map 



( _Hodge–Riemann relations_ for _𝑋_ ). 

In the classical setting, _𝐴_ ( _𝑋_ ) is the cohomology of real ( _𝑘, 𝑘_ )-forms on a compact Kähler manifold, and the three statements are consequences of Hodge theory **[43, Chapter 3]** .1 All three statements are known to hold for _𝐴_ ( _𝑋_ ) listed above except the first one, which is the subject of Grothendieck’s standard conjectures on algebraic cycles **[36]** . In every case, the three statements for _𝐴_ ( _𝑋_ ) reveal a fundamental property of _𝑋_ : Weil conjectures on the number of solutions to a system of polynomial equations over finite fields when _𝑋_ is a smooth projective variety **[36, 67]** , the generalized lower bound conjecture on the number of faces when _𝑋_ is a convex polytope **[45,70]** , and Kazhdan–Lusztig’s nonnegativity conjecture when _𝑋_ is a Coxeter group element **[26]** . When _𝑋_ is a matroid, the hard Lefschetz property and the Hodge–Riemann relations for different choices of _𝐴_ ( _𝑋_ ) are used to settle Rota’s conjecture on the characteristic polynomial **[1]** , Brylawski’s and Dawson’s conjectures on the _ℎ_ -vectors of the broken circuit complex and the independence complex **[6]** , and Dowling–Wilson’s top-heavy conjecture on the number of flats **[12]** . The known proofs of the Poincaré duality, the hard Lefschetz property, and the Hodge–Riemann relations for the objects listed above have certain structural similarities, but there is no known way of deducing one from the others. Could there be a Hodge-theoretic framework general enough to explain this miraculous coincidence? 

A related goal is to produce a flexible analytic theory that would reflect certain basic features of the unified theory: If one postulates the existence of the satisfactory cohomology _𝐴_ ( _𝑋_ ), what can we say about _𝑋_ at an elementary and numerical level? This is a worthwhile question because, depending on _𝑋_ , the construction and the study of _𝐴_ ( _𝑋_ ) might be beyond the reach of our current understanding. A step in this direction is taken in a joint work with Petter Brändén on _Lorentzian polynomials_ **[17]** , where the difficult goal of finding _𝐴_ ( _𝑋_ ) is replaced by an easier goal of producing a Lorentzian polynomial from _𝑋_ . Such a Lorentzian polynomial can be used to settle and generate conjectures on various _𝑋_ (Section 2) and, sometimes, leads to a satisfactory theory of _𝐴_ ( _𝑋_ ) (Section 3). 

> **1** In **[12, 26, 36, 43, 45]** , the hard Lefschetz property and the Hodge–Riemann relations are considered only in the “unmixed” case where _𝐿_ = _𝐿𝑖_ for all _𝑖_ . According to **[18]** , this special case implies the general case stated above. 

**4 J. Huh** 

## **2. Lorentzian polynomials** 

Lorentzian polynomials link continuous convex analysis and discrete convex analysis via tropical geometry, and they reveal subtle information on graphs, convex bodies, projective varieties, Potts model partition functions, log-concave polynomials, and highest weight representations of general linear groups. Let _𝐻𝑛_<sup>_𝑑_be the space of degree</sup><sup>_𝑑_homoge-</sup> neous polynomials in _𝑛_ variables with real coefficients. The members of _𝐻𝑛_<sup>_𝑑_will be written</sup> 



where the sum is over the nonnegative integral vectors _𝛼_ ∈ Z<sup>_𝑛_</sup> ≥0<sup>with |</sup><sup>_𝛼_|1=</sup><sup>_𝑑_and</sup> 



Note that a polynomial _𝑓_ can be viewed as a function in at least two different ways. The continuous _𝑓_ is the function given by the evaluation 



and the discrete _𝑓_ is the function given by the coefficients 



Throughout we write supp( _𝑓_ ) for the _support_ of the discrete _𝑓_ , the set of monomials appearing in _𝑓_ with nonzero coefficients. The theory of Lorentzian polynomials shows that the log-concavity of the continuous _𝑓_ is related to the log-concavity of the discrete _𝑓_ in an interesting way. Before defining Lorentzian polynomials in Definition 4, we list three applications of the theory to demonstrate the usefulness and ubiquity of Lorentzian polynomials. Each item below presents an elementary statement that is difficult to prove without the Lorentzian point of view. 

**Example 1** (Analysis). Let _𝑓_ be a homogeneous polynomial of degree _𝑑_ in _𝑛_ variables with nonnegative coefficients. Such a polynomial _𝑓_ is said to be _strongly log-concave_ if, for all _𝛼_ ∈ Z<sup>_𝑛_</sup> ≥0<sup>, we have</sup> 

_𝜕_<sup>_𝛼_</sup> _𝑓 is identically zero or_ log( _𝜕_<sup>_𝛼_</sup> _𝑓_ ) _is concave on the positive orthant_ R<sup>_𝑛_</sup> _>_ 0<sup>_._</sup> 

For bivariate polynomials, one can show that _𝑓_ =<sup>�</sup><sup>_𝑑_</sup> _𝑘_ =0<sup>_𝑐𝑘𝑤_</sup> 1<sup>_𝑘𝑤_</sup> 2<sup>_𝑑_−</sup><sup>_𝑘_</sup> is strongly log-concave exactly when the sequence { _𝑐𝑘_ } has _no internal zeros_ and is _ultra log-concave_ : 



In **[17, Corollary 2.32]** , the theory of Lorentzian polynomials is used to prove the following statement: 

_The product of strongly log-concave homogeneous polynomials is strongly logconcave._ 

**5 Combinatorics and Hodge theory** 

This answers a question of Gurvits **[37, Section 4.5]** for homogeneous polynomials, and extends the following theorem of Liggett **[50, Theorem 2]** : 

_The convolution product of two ultra log-concave sequences with no internal zeros is an ultra log-concave sequence with no internal zeros._ 

The short proof in **[17]** is based on the following analytic characterization of Lorentzian polynomials **[17, Theorem 2.30]** : 

_A homogeneous polynomial with nonnegative coefficients is Lorentzian if and only if it is strongly log-concave._ 

It is interesting to compare the argument with the computational proof in **[50]** for bivariate polynomials. 

**Example 2** (Combinatorics). Let 𝒜 be a set of _𝑛_ vectors in a vector space. For any _𝑘_ , set 



For example, if 𝒜 is the set of all seven nonzero vectors in a three-dimensional vector space over the field with two elements, then there are seven dependencies among the triples shown below, and hence 





Mason’s conjecture from **[52]** predicts that, for any 𝒜 and any positive integer _𝑘_ , 



The same statement was conjectured more generally for all _matroids_ (Definition 9), and the general statement is proved in **[17, Theorem 4.14]** using the theory of Lorentzian polynomials.2 The proof is based on the Lorentzian property of the Potts model partition function for matroids introduced in **[68]** . 

> **2** Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant have independently developed methods that partly overlap with **[17]** in a series of papers **[2–4]** . They study the class of _completely log-concave polynomials_ , which agrees with the class of Lorentzian polynomials in the homogeneous case. The main overlap is an independent proof of Mason’s conjecture in **[4]** . 

**6 J. Huh** 

**Example 3** (Algebra). Schur polynomials are the characters of finite-dimensional irreducible polynomial representations of the general linear group GL _𝑛_ (C). Combinatorially, the _Schur polynomial_ of a partition _𝜆_ in _𝑛_ variables is 



where _𝐾𝜆𝛼_ is the _Kostka number_ counting Young tableaux of given shape _𝜆_ and weight _𝛼_ . Correspondingly, the irreducible representation _𝑉_ ( _𝜆_ ) of the general linear group with the highest weight _𝜆_ has the weight space decomposition 



Schur polynomials were first studied by Cauchy, who defined them as ratios of alternants. The connection to the representation theory of GL _𝑛_ (C) was found by Schur. For a gentle introduction to these remarkable polynomials, and for any undefined terms, we refer to **[31]** . 

In **[40, Theorem 2]** , the authors use the Lorentzian property for normalized Schur polynomials to show that the sequence of weight multiplicities of V( _𝜆_ ) one encounters is always log-concave if one walks in the weight diagram along any root direction _𝑒𝑖_ − _𝑒 𝑗_ . In other words, for any _𝛼_ ∈ Z<sup>_𝑛_</sup> ≥0<sup>and any</sup><sup>_𝑖,𝑗_∈[</sup><sup>_𝑛_],</sup> 



This verifies a special case of Okounkov’s conjecture from **[61, Conjecture 1]** .3 

We now define Lorentzian polynomials. As before, we write _𝐻𝑛_<sup>_𝑑_forthespaceof</sup> degree _𝑑_ homogeneous polynomials in _𝑛_ variables with real coefficients. Let _𝐿_<sup>˚2</sup> _𝑛_<sup>⊆</sup><sup>_𝐻_</sup> _𝑛_<sup>2be the</sup> open subset of quadratic forms with positive coefficients that have the _Lorentzian signature_ (+ _,_ − _, . . . ,_ −). For _𝑑_ larger than 2, we define an open subset _𝐿_<sup>˚</sup> _𝑛_<sup>_𝑑_⊆</sup><sup>_𝐻_</sup> _𝑛_<sup>_𝑑_by setting</sup> 



where _𝜕𝑖_ is the partial derivative with respect to the _𝑖_ -th variable. Thus _𝑓_ belongs to _𝐿_<sup>˚</sup> _𝑛_<sup>_𝑑_if</sup> and only if all quadratic polynomials of the form _𝜕𝑖_ 1 _𝜕𝑖_ 2 · · · _𝜕𝑖𝑑_ −2 _𝑓_ belongs to _𝐿_<sup>˚2</sup> _𝑛_<sup>.</sup> **Definition 4** (Lorentzian polynomials). The polynomials in _𝐿_<sup>˚</sup> _𝑛_<sup>_𝑑_are called</sup><sup>_strictly Lorentzian_,</sup> and the limits of strictly Lorentzian polynomials are called _Lorentzian_ . 

The prototypical examples of Lorentzian polynomials, which motivated Definition 4, are the ones obtained from the various examples of _𝐴_ ( _𝑋_ ) in Section 1 in the following way. For any linear operators _𝐿_ 1 _, . . . , 𝐿𝑑_ on _𝐴_ ( _𝑋_ ), we set 



> **3** The general conjecture is that the discrete function ( _𝜈, 𝜅, 𝜆_ ) ↦→ log _𝑐𝜅𝜆_<sup>_𝜈_is concave, where</sup> _𝑐𝜅𝜆_<sup>_𝜈_are the</sup><sup>_Littlewood-Richardson coefficients_</sup><sup>**[61, Conjecture 1]**. The conjecture holds in</sup> the “classical limit” **[61, Section 3]** , but the general case is refuted in **[19]** . 

**7 Combinatorics and Hodge theory** 

where 1 is the distinguished generator of _𝐴_<sup>0</sup> ( _𝑋_ ) defining _𝑃_ (1 _,_ −) : _𝐴_<sup>_𝑑_</sup> ( _𝑋_ ) ≃ R. **Proposition 5.** Let _𝐿_ 1 _, . . . , 𝐿𝑛_ be members of the closure _𝐾_ ( _𝑋_ ), and let _𝑓_ the polynomial 



If _𝐴_ ( _𝑋_ ) satisfies the Hodge–Riemann relations in degrees ≤ 1, then _𝑓_ is Lorentzian. 

Before deducing Proposition 5 from Theorem 12 below, we give two prominent cases. 

**Example 6** (Volume polynomials of convex bodies). For any collection of convex bodies _𝐶_ = ( _𝐶_ 1 _, . . . , 𝐶𝑛_ ) in R<sup>_𝑑_</sup> , consider the function 



where _𝑤_ 1 _𝐶_ 1 + · · · + _𝑤𝑛𝐶𝑛_ is the Minkowski sum and vol is the Euclidean volume. Minkowski showed that vol _𝐶_ ( _𝑤_ ) is a polynomial **[66, Chapter 5]** . One may approximate the convex bodies with convex polytopes to prove that vol _𝐶_ is Lorentzian. Using Proposition 5, where _𝑋_ is the Minkowski sum of the approximating convex polytopes and _𝐴_ ( _𝑋_ ) is the combinatorial cohomology in **[45]** , we get the following statement: 

_The polynomial vol𝐶_ ( _𝑤_ ) _is Lorentzian for any convex bodies 𝐶_ 1 _, . . . , 𝐶𝑛 in_ R<sup>_𝑑_</sup> _._ 

Alternatively, one can use Brunn–Minkowski theory to deduce the Lorentzian property of the volume polynomial **[17, Section 4.1]** . 

**Example 7** (Volume polynomials of projective varieties). Let _𝑋_ be a _𝑑_ -dimensional irreducible projective variety over an algebraically closed field. A Cartier divisor on _𝑋_ is said to be _nef_ if it intersects every irreducible curve in _𝑋_ nonnegatively.4 For any collection of nef divisors _𝐻_ = ( _𝐻_ 1 _, . . . , 𝐻𝑛_ ) on _𝑋_ , consider the function 



where deg is the degree map on the Chow group of 0-dimensional cycles on _𝑋_ . When _𝑋_ admits a resolution of singularities _𝑌_ , one can deduce the following statement from Proposition 5 and the Hodge–Riemann relations in degree ≤ 1 for the ring of algebraic cycles _𝐴_ ( _𝑌_ ): 

_The polynomial vol𝐻_ ( _𝑤_ ) _is Lorentzian for any nef divisors 𝐻_ 1 _, . . . , 𝐻𝑛 on 𝑋._ 

In general, one can use Bertini’s theorem to reduce the statement to the case of surfaces and apply Hodge’s index theorem **[17, Section 4.2]** . 

> **4** By Kleiman’s theorem **[47, Section 1.4]** , any nef divisor on a projective variety is a limit of ample R-divisors, which form the convex cone _𝐾_ ( _𝑋_ ) in this setting. 

**8 J. Huh** 

Next we formulate the main structural results on Lorentzian polynomials. A central definition is that of generalized permutohedra. Let _𝐸_ be a finite set, and let { _𝑒𝑖_ } _𝑖_ ∈ _𝐸_ be the standard basis of R<sup>_𝐸_</sup> . 

**Definition 8.** A _generalized permutohedron_ is a polytope in R<sup>_𝐸_</sup> all of whose edges are in the direction _𝑒𝑖_ − _𝑒 𝑗_ for some _𝑖_ and _𝑗_ in _𝐸_ . 

For example, the _standard permutohedron_ in R<sup>_𝑛_</sup> , which is the convex hull of all permutations of (1 _,_ 2 _, . . . , 𝑛_ ), and the _𝑘-th hypersimplex_ in R<sup>_𝑛_</sup> , which is the convex hull of all permutations of (1 _, . . . ,_ 1 _,_ 0 _, . . . ,_ 0), are integral generalized permutohedra. � **���** �� **���** � � **���** �� **���** � _𝑘 𝑛_ − _𝑘_ 





The above pictures show the standard permutohedron and the second hypersimplex in R<sup>4</sup> . Generalized permutohedra are precisely the translates of the base polytopes of _polymatroids_ **[24]** , and they are obtained from the standard permutohedron by moving the vertices so that all the edge directions are preserved **[63]** . They lead to the central notion of M _-convexity_ in the study of discrete convex analysis **[59]** . 

**Definition 9.** A subset _𝐽_ ⊆ Z<sup>_𝐸_</sup> ≥0<sup>is M</sup><sup>_-convex_if it is the set of all lattice points of an integral</sup> generalized permutohedron. A _matroid_ on _𝐸_ is an M-convex subset of Z<sup>_𝐸_</sup> ≥0<sup>consistingof</sup> zero-one vectors. The vectors in a matroid _𝐽_ are called _bases_ of _𝐽_ . 

A subset _𝐽_ ⊆ Z<sup>_𝐸_</sup> ≥0<sup>is M-convex exactly when it satisfies the</sup><sup>_symmetric basis exchange_</sup> _property_ **[24, 39]** : For any _𝛼, 𝛽_ ∈ _𝐽_ and an index _𝑖_ satisfying _𝛼𝑖 > 𝛽𝑖_ , there is an index _𝑗_ that satisfies 

_𝛼 𝑗 < 𝛽 𝑗_ and _𝛼_ − _𝑒𝑖_ + _𝑒 𝑗_ ∈ _𝐽_ and _𝛽_ − _𝑒 𝑗_ + _𝑒𝑖_ ∈ _𝐽._ 

In **[59, Chapter 4]** , one can find several other equivalent characterizations of M-convexity. The above definition of matroids goes back to the study of moment map images of torus orbits in Grassmannians by Gelfand, Goresky, MacPherson, and Serganova in **[33]** . For a general introduction to matroids, and for any undefined matroid terms, we refer to **[62]** . Hereafter we identify the subsets of _𝐸_ with the zero-one vectors in Z<sup>_𝐸_</sup> ≥0<sup>.</sup> 

**Example 10** (Graphic matroids). For any finite connected graph _𝐺_ with the edge set _𝐸_ , consider the set of indicator vectors 

ℬ( _𝐺_ ) ≔ { _𝑒𝐵_ | _𝐵_ is a spanning tree of _𝐺_ } ⊆ Z<sup>_𝐸_</sup> ≥0<sup>_._</sup> 

The subset ℬ( _𝐺_ ) is M-convex for any _𝐺_ . Such matroids are said to be _graphic_ . 

**9 Combinatorics and Hodge theory** 

**Example 11** (Representable matroids). For any function _𝜑_ : _𝐸_ → _𝑊_ from a finite set _𝐸_ to a vector space _𝑊_ over a field F, consider the set of indicator vectors 

ℬ( _𝜑_ ) ≔ { _𝑒𝐵_ | _𝜑_ ( _𝐵_ ) is a bases of _𝑊_ } ⊆ Z<sup>_𝐸_</sup> ≥0<sup>_._</sup> 

The subset ℬ( _𝜑_ ) is M-convex for any _𝜑_ : _𝐸_ → _𝑊_ . Such matroids are said to be _representable over_ F, and the function _𝜑_ is called a _representation over_ F. One typically requires without loss of generality that the image of _𝜑_ spans _𝑊_ . A graphic matroid is representable over every field **[62, Section 5.1]** . In general, a matroid may or may not have a representation over F: 







Among the three matroids pictured above, where the bases are given by all triples of points not on a line, the first is representable over F if and only if the characteristic of F is 2, the second is representable over F if and only if the characteristic of F is not 2, and the third is not representable over any field. 



where M _𝑛_<sup>_𝑑_⊆</sup><sup>_𝐻_</sup> _𝑛_<sup>_𝑑_isthesetofpolynomialswithnonnegativecoefficientswhosesupports</sup> are M-convex. The following characterization in **[17, Theorem 2.25]** is central to the theory of Lorentzian polynomials. 

**Theorem 12.** _𝐿𝑛_<sup>_𝑑_is the set of Lorentzian polynomials in</sup><sup>_𝐻_</sup> _𝑛_<sup>_𝑑_.</sup> 

In other words, _𝐿𝑛_<sup>_𝑑_istheclosureof</sup><sup>_𝐿_˚</sup> _𝑛_<sup>_𝑑_in</sup><sup>_𝐻_</sup> _𝑛_<sup>_𝑑_.</sup><sup>_Theorem_12</sup><sup>_makesitpossibleto_</sup> _decide whether a given polynomial is Lorentzian or not_ . For example, the following polynomials are not Lorentzian because their supports are not M-convex: 



One can also use Theorem 12 to show that a given polynomial is Lorentzian. For example, the elementary symmetric polynomial of degree _𝑑_ in _𝑛_ variables is Lorentzian because its support is M-convex and all its associated quadratic forms are 



which have exactly one positive eigenvalue _𝑛_ − _𝑑_ + 1. One can also use Theorem 12 and the relevant Hodge–Riemann relations to show that the volume polynomials in Example 6 and 

**10 J. Huh** 

Example 7 are Lorentzian. In particular, the supports of these volume polynomials must be M-convex for any collection of convex bodies and any collection of nef divisors. 

_Proof of Proposition_ 5 _._ We may suppose that _𝐿_ 1 _, . . . , 𝐿𝑛_ are members of _𝐾_ ( _𝑋_ ). Under this assumption, all the coefficients of _𝑓_ are positive by the Hodge–Riemann relations in degree 0, so the support of _𝑓_ is M-convex. Choose any _𝑑_ − 2 among the linear operators, say _𝐿_ 1 _, . . . , 𝐿𝑑_ −2, and observe that 



Thus, by Theorem 12, it is enough to observe that the symmetric bilinear pairing 



has the Lorentzian signature, where _𝐵_<sup>1</sup> ( _𝑋_ ) is the span of _𝐿_ 1 · 1 _, . . . , 𝐿𝑛_ · 1 in _𝐴_<sup>1</sup> ( _𝑋_ ). This follows from the Hodge–Riemann relations in degrees ≤ 1: For any _𝐿_ in _𝐾_ ( _𝑋_ ), the pairing is positive on _𝐿_ · 1 by the Hodge–Riemann relations in degree 0, and it is negative definite on the orthogonal complement of _𝐿_ · 1 by the Hodge–Riemann relations in degree 1. 

**Example 13.** Not all Lorentzian polynomials are volume polynomials of convex bodies. In fact, the basis generating polynomial of a matroid on [ _𝑛_ ] is the volume polynomial of _𝑛_ convex bodies precisely when the matroid is representable over every field **[17, Remark 4.3]** . For example, the elementary symmetric polynomial 



is not the volume polynomial of four convex bodies in R<sup>2</sup> because its support is not representable over the field F2. 

**Example 14.** Not all Lorentzian polynomials are volume polynomials of nef divisors on a projective variety. For example, consider the cubic polynomial 



One can use Theorem 12 to check that _𝑓_ is Lorentzian. To see that _𝑓_ is not the volume polynomial of nef divisors, one can use the _reverse Khovanskii–Teissier inequality_ **[49, Theorem 5.7]** : For any nef divisors _𝐿_ 1 _, 𝐿_ 2 _, 𝐿_ 3 on a _𝑑_ -dimensional projective variety and any _𝑘_ ≤ _𝑑_ , 



The complex analytic proof of the inequality in **[49]** relies on the Calabi–Yau theorem **[74]** . The algebraic proof of the inequality in **[44]** using Okounkov bodies works over any algebraically closed field. 

The theory of toric varieties shows that the volume polynomial of any set of convex bodies is the limit of a sequence of volume polynomials of nef divisors on projective varieties **[30, Section 5.4]** . Thus, the Lorentzian cubic _𝑓_ provides a counterexample to Gurvits’ conjecture that a strongly log-concave homogeneous polynomial in three variables with nonnegative coefficients is the volume polynomial of three convex bodies **[37, Conjecture 4.1]** . 

**11 Combinatorics and Hodge theory** 

The space of Lorentzian polynomials has numerous surprising properties. For example, writing P _𝐿_ for the image of _𝐿_ \ 0 ⊆ _𝐻𝑛_<sup>_𝑑_in the real projective space P</sup><sup>_𝐻_</sup> _𝑛_<sup>_𝑑_, one can</sup> show that 

P _𝐿𝑛_<sup>_𝑑is compact contractible subset with contractible interior_P ˚</sup><sup>_𝐿_</sup> _𝑛_<sup>_𝑑._</sup> 

The contractibility follows from the following semigroup action **[17, Theorem 2.10]** : 

_Any nonnegative linear change of coordinates preserves 𝐿𝑛_<sup>_𝑑. More generally, when_</sup> _𝑓_ ( _𝑤_ ) ∈ _𝐿𝑛_<sup>_𝑑, then𝑓_(</sup><sup>_𝐴𝑣_)∈</sup><sup>_𝐿_</sup> _𝑚_<sup>_𝑑for any 𝑛_×</sup><sup>_𝑚matrix𝐴with nonnegative entries._</sup> 

In fact, Brändén showed in **[16]** that P _𝐿𝑛_<sup>_𝑑_ishomeomorphictoaclosedEuclideanball,</sup> verifying a conjecture posed in **[17, Conjecture 2.29]** . The main feature of this _Lorentzian ball_ is the following stratification labelled by M-convex sets **[17, Theorem 3.10 and Proposition 3.25]** : 

_The set 𝐿 𝐽 of Lorentzian polynomials with support 𝐽 is nonempty if and only if 𝐽 is_ M _-convex . In this case,_ P _𝐿 𝐽 deformation retracts to the exponential generating function_<sup>�</sup> _𝛼_ ∈ _𝐽 𝛼_ <u>1!</u><sup>_𝑤𝛼._</sup> 

This supports the opinion that _matroid theory provides the correct level of generality_ . Leaving out any one matroid, say not representable over any field, will make the Lorentzian ball noncompact.5 

The connection between discrete convex analysis and Lorentzian polynomials can be strengthened as follows. For a function _𝜈_ : Z<sup>_𝑛_</sup> ≥0<sup>→R ∪{∞}, we write dom(</sup><sup>_𝜈_)⊆Z</sup><sup>_𝑛_</sup> ≥0<sup>for</sup> the subset on which _𝜈_ is finite, called the _effective domain_ of _𝜈_ . For a positive real parameter _𝑞_ , consider the exponential generating function 



By **[17, Theorem 3.14]** , the polynomial _𝑓𝑞_<sup>_𝜈_is Lorentzian for all sufficiently small</sup><sup>_𝑞_if and only</sup> if the function _𝜈_ is M _-convex_ in the sense of discrete convex analysis **[59]** : For any index _𝑖_ and any _𝛼, 𝛽_ ∈ dom( _𝜈_ ) whose _𝑖_ -th coordinates satisfy _𝛼𝑖 > 𝛽𝑖_ , there is an index _𝑗_ satisfying 

_𝛼 𝑗 < 𝛽 𝑗_ and _𝜈_ ( _𝛼_ ) + _𝜈_ ( _𝛽_ ) ≥ _𝜈_ ( _𝛼_ − _𝑒𝑖_ + _𝑒 𝑗_ ) + _𝜈_ ( _𝛽_ − _𝑒 𝑗_ + _𝑒𝑖_ ) _._ 

Considering the special case when _𝜈_ takes values in {0 _,_ ∞}, we see that _𝐽_ is an M-convex set if and only if its exponential generating function<sup>�</sup> _𝛼_ ∈ _𝐽 𝛼_ <u>1!</u><sup>_𝑤𝛼_is a Lorentzian polynomial</sup> **[17, Theorem 3.10]** . Another corollary is that a homogeneous polynomial with nonnegative coefficients is Lorentzian if the natural logarithms of its normalized coefficients form an 

> **5** Almost all matroids are not representable over any field. More precisely, the portion of matroids in Z<sup>_𝑛_</sup> ≥0<sup>that are representable over some field goes to zero as</sup><sup>_𝑛_goes to infinity</sup><sup>**[60]**.</sup> For logical discussions of the “missing axiom” of matroid theory, see **[53, 54, 73]** . 

**12 J. Huh** 

M-concave function **[17, Corollary 3.16]** . Working over the field of real Puiseux series K, we see that the tropicalization of any Lorentzian polynomial over K is an M-convex function, and that _all_ M-convex functions are limits of tropicalizations of Lorentzian polynomials over K **[17, Corollary 3.28]** . This generalizes a result of Brändén **[15]** , who showed that the tropicalization of any homogeneous stable polynomial over K is M-convex. In particular, for any matroid M with the set of bases ℬ, the _Dressian_ of all valuated matroids on M can be identified with the tropicalization of the space of Lorentzian polynomials over K with support ℬ. For example, the tropicalization of the space of multiaffine Lorentzian quadrics in five variables is the tropical Grassmannian trop Gr(2 _,_ 5), a cone ove the Petersen graph in R<sup>10</sup> /R **1** : 



The figure shows a shadow of the Lorentzian ball P _𝐿_ 5<sup>2over K, highlighting its non-convexity.</sup> We refer to **[51, Chapter 4]** for a friendly introduction to Dressians and tropical Grassmannians. 

The theory of Lorentzian polynomials is not only useful for proving conjectures but also for generating them. Once one has identified a combinatorial polynomial _𝑓_ that is either provably or conjecturally Lorentzian, it is natural to look for an algebraic object _𝐴_ ( _𝑋_ ) satisfying the Hodge–Riemann relations that explains the Lorentzian property of _𝑓_ . In good cases, one can further speculate that there is a projective variety _𝑋_ that produces _𝑓_ as a volume polynomial for some choices of nef divisors on _𝑋_ . 

One such speculation concerns the basis generating polynomial for a morphism of matroids. Let M and N be matroids on finite sets _𝐸_ and _𝐹_ . The _rank function_ of M is the function defined by 



where the maximum is taken over the set of bases of M. A _morphism 𝑔_ : M → N is a function _𝐸_ → _𝐹_ that satisfies the rank inequalities 



A function between the ground sets is a morphism if and only if the preimage of a flat is a flat (Definition 22). A subset _𝑆_ ⊆ _𝐸_ is a _basis_ of _𝑔_ if _𝑆_ is contained in a basis of M and _𝑔_ ( _𝑆_ ) contains a basis of N. For a general discussion of morphisms of matroids, we refer to **[46]** . 

In **[27, Corollary 4.6]** , the authors show that the _homogenous basis generating polynomial_ 



is Lorentzian for any morphism of matroids _𝜑_ : M → N, where ℬ( _𝑔_ ) is the set of bases of _𝑔_ . When N is the rank zero matroid on one element, one recovers the Lorentzian property of 

**13 Combinatorics and Hodge theory** 

the homogenous independent set generating polynomial of M in **[17, Section 4.3]** . Setting the variables ( _𝑤𝑖_ ) _𝑖_ ∈ _𝐸_ equal to each other, we get a bivariate Lorentzian polynomial witnessing the validity of Mason’s conjecture in Example 2. When _𝑔_ is the identity morphism, one recovers the Lorentzian property of the basis generating polynomial of a matroid **[17, Section 3.2]** . 

**Example 15** (Continued from Example 10). A homomorphism from a graph _𝐺_ 1 to a graph _𝐺_ 2 is a function from the vertex set of _𝐺_ 1 to the vertex set of _𝐺_ 2 that maps adjacent vertices to adjacent vertices. The induced map from the edge set of _𝐺_ 1 to the edge set of _𝐺_ 2 is a morphism from the graphic matroid ℬ( _𝐺_ 1) to the graphic matroid ℬ( _𝐺_ 2). Such morphisms of matroids are said to be _graphic_ . 



<!-- Start of picture text -->
1<br>1<br>3<br>1 2<br>2 3<br>2 3<br><!-- End of picture text -->

The graphic morphism of matroids depicted above has 27 bases of cardinality two, 79 bases of cardinality three, 111 bases of cardinality four, and 75 bases of cardinality five. 

**Example 16** (Continued from Example 11). Let M _𝑖_ be matroids on _𝐸𝑖_ with representations _𝜑𝑖_ : _𝐸𝑖_ → _𝑊𝑖_ over a field F. A function _𝑔_ from _𝐸_ 1 to _𝐸_ 2 is a morphism from M1 to M2 if it fits into a commutative diagram 



where _𝑊_ 1 → _𝑊_ 2 is a linear map between the vector spaces. Such morphisms of matroids are said to be _representable over_ F. A graphic morphism of matroids is representable over every field. 

Continuing Example 7, we say that a degree _𝑑_ Lorentzian polynomial _𝑓_ in variables _𝑤_ 1 _, . . . , 𝑤𝑛_ is a _volume polynomial over_ F if there are nef divisors _𝐻_ 1 _, . . . , 𝐻𝑛_ on a _𝑑_ - dimensional irreducible projective variety _𝑋_ over F that satisfy 



The following existence conjecture was made in **[27, Conjecture 5.6]** . It strengthens the Lorentzian property of the homogeneous basis generating polynomial of _𝑔_ when _𝑔_ is representable over F. 

**Conjecture 17.** If _𝑔_ is a morphism of matroids that is representable over F, then the homogenous basis generating polynomial of _𝑔_ is a volume polynomial over F. 

**14 J. Huh** 

Let M be a matroid on _𝐸_ that is representable over F. In **[5]** , the authors construct a collection of nef divisors ( _𝐿𝑖_ ) _𝑖_ ∈ _𝐸_ on an irreducible projective variety _𝑌_ over F such that 



where the first sum is over the set of bases ℬ of M. This verifies Conjecture 17 when _𝑔_ is the identity morphism. A detailed study of this _𝑌_ and its resolution of singularities in **[41]** , in turn, was used to define the _matroid intersection cohomology_ in **[12]** . It plays a central role in the resolution of two combinatorial conjectures on matroids, the top-heavy conjecture for the lattice of flats and the nonnegativity conjecture for the Kazhdan-Lusztig coefficients. We outline their proofs in Section 3. 

Another speculation on Lorentzian polynomials is based on the Lorentzian property of the _normalized Schur polynomial_ 



Here, as in Example 3, _𝜆_ is a partition and _𝐾𝜆𝛼_ are the Kostka coefficients. 

**Definition 18.** The _normalization operator_ is the linear operator N defined on the space of Laurent generating functions defined by 



For example, we have N<sup>�</sup> _𝑧_ (11− _𝑧_ ) � = _𝑒𝑧_ . 

In **[17, Proposition 4.4]** , it was observed that the _Alexandrov–Fenchel inequality_ for volume polynomials of convex bodies holds more generally for any Lorentzian polynomial in _𝑛_ variables: 

_If_<sup>�</sup> _𝛼_<sup>_𝑐_</sup> _𝛼_<sup>_<u>𝑤</u>_</sup> _𝛼_<sup>_𝛼_</sup> !<sup>_is Lorentzian, then 𝑐_2</sup> _𝛼_<sup>≥</sup><sup>_𝑐𝛼_−</sup><sup>_𝑒_</sup> _𝑖_<sup>+</sup><sup>_𝑒_</sup> _𝑗_<sup>_𝑐𝛼_+</sup><sup>_𝑒_</sup> _𝑖_<sup>−</sup><sup>_𝑒_</sup> _𝑗_<sup>_for any 𝛼and any 𝑖, 𝑗_∈[</sup><sup>_𝑛_]</sup><sup>_._</sup> 

Since the Kostka coefficients are the weight multiplicities of the finite-dimensional irreducible representation _𝑉_ ( _𝜆_ ) of GL _𝑛_ (C), the Lorentzian property of N( _𝑠𝜆_ ) thus implies 

(dim _𝑉_ ( _𝜆_ ) _𝛼_ )<sup>2</sup> ≥ dim _𝑉_ ( _𝜆_ ) _𝛼_ − _𝑒𝑖_ + _𝑒 𝑗_ dim _𝑉_ ( _𝜆_ ) _𝛼_ − _𝑒 𝑗_ + _𝑒𝑖_ for any _𝑖, 𝑗_ ∈[ _𝑛_ ]. 

Could this be a special case of a more general discrete log-concavity for weight multiplicities? 

Let Λ be the integral weight lattice of the Lie algebra 𝔰𝔩 _𝑛_ (C). For _𝜆_ ∈ Λ, write V( _𝜆_ ) for the irreducible 𝔰𝔩 _𝑛_ (C)-module with the highest weight _𝜆_ and consider its decomposition into finite-dimensional weight spaces 



We point to **[42]** for background on the representation theory of semisimple Lie algebras. The following conjecture was proposed in **[40, Section 3.1]** . 

**15 Combinatorics and Hodge theory** 

**Conjecture 19.** For any _𝜆_ ∈ Λ and any _𝛼_ ∈ Λ, we have 

(dim V( _𝜆_ ) _𝛼_ )<sup>2</sup> ≥ dim V( _𝜆_ ) _𝛼_ − _𝑒𝑖_ + _𝑒 𝑗_ dim V( _𝜆_ ) _𝛼_ − _𝑒 𝑗_ + _𝑒𝑖_ for any _𝑖, 𝑗_ ∈[ _𝑛_ ]. 

When _𝜆_ is dominant, the dimension of the weight space V( _𝜆_ ) _𝛼_ is the Kostka number _𝐾𝜆𝛼_ , and the Lorentzian property of the normalized Schur polynomial N( _𝑠𝜆_ ) implies that Conjecture 19 holds in this case. When _𝜆_ is antidominant, V( _𝜆_ ) is the _Verma module_ M( _𝜆_ ), the universal highest weight module of highest weight _𝜆_ . Using the connection between the Kostant partition function and the volumes of flow polytopes in **[8]** , one can produce Lorentzian polynomials that witness the validity of the conjecture in this case **[40, Proposition 11]** . Figure 1 illustrates some cases of Conjecture 19 when _𝜆_ is neither dominant nor antidominant. 



<!-- Start of picture text -->
1 1 1 1 1 1 1 1<br>3 3 3 3 3 3 3 2<br>6 6 6 6 6 6 5 3 e 3  − e 2<br>10 10 10 10 10 9 7 4 e 3  − e 1 e 2  − e 1<br>14 14 14 14 13 11 8 4<br>18 18 18 17 15 12 8 4<br>22 22 21 19 16 12 8 4<br>26 25 23 20 16 12 8 4<br><!-- End of picture text -->

**Figure 1** The figure shows some of the weight multiplicities of the irreducible 𝔰𝔩4 (C)-module with the highest weight −2 _𝜛_ 1 − 3 _𝜛_ 2. We start from the highlighted vertex _𝜛_ 1 − 6 _𝜛_ 2 − 3 _𝜛_ 3 and walk along negative root directions in the hyperplane spanned by _𝑒_ 2 − _𝑒_ 1 and _𝑒_ 3 − _𝑒_ 2. In the shown region, the sequence of weight multiplicities along any line is log-concave, as predicted by Conjecture 19. 

Conjecture 19 suggests the following existence statements of increasing strength. 

_There is a Lorentzian polynomial 𝑓 that implies the discrete log-concavity in Conjecture_ 19 _for given 𝜆 and 𝛼._ 

_There is a cohomology 𝐴 satisfying the Hodge–Riemann relations that implies the Lorentzian property of 𝑓 for given 𝜆 and 𝛼._ 

_There is a projective variety 𝑋 that implies the Hodge–Riemann relations of 𝐴 for given 𝜆 and 𝛼._ 

**16 J. Huh** 

We give a precise formulation of the first prediction. For _𝜆_ ∈ Λ, consider the Laurent generating function 



Note that every monomial appearing in ch _𝜆_ is a product of degree zero monomials of the form _𝑤𝑖𝑤_<sup>−1</sup> _𝑗_<sup>.</sup> 

**Conjecture 20.** N( _𝑤_<sup>_𝛿_</sup> ch _𝜆_ ( _𝑤_ 1 _, . . . , 𝑤𝑛_ )) is Lorentzian for any _𝜆_ ∈ Λ and _𝛿_ ∈ Z<sup>_𝑛_</sup> ≥0<sup>.</sup> 

Conjecture 20 holds for any _𝛿_ when _𝜆_ is either dominant or antidominant. In general, the homogeneous polynomial N( _𝑤_<sup>_𝛿_</sup> ch _𝜆_ ) can be computed using the Kazhdan–Lusztig theory **[42, Chapter 8]** . The authors of **[40]** tested Conjecture 20 for _𝜆_ = − _𝜎𝜌_ − _𝜌_ and _𝛿_ = (1 _, . . . ,_ 1), where _𝜌_ is the sum of all the fundamental weights, for all permutations _𝜎_ in _𝑆𝑛_ for _𝑛_ ≤ 6. Conjecture 19 for _𝜆_ and _𝛼_ follows from Conjecture 20 for _𝜆_ and any sufficiently large _𝛿_ . 

Similar conjectures can be made for various other polynomials appearing in representation theory and symmetric function theory. For relevant definitions, we refer to **[40, Section 3]** and references therein. 

**Conjecture 21.** The following polynomials are Lorentzian **[40, Conjectures 15,19,20,22,23]** : 

- (1) The normalized Schubert polynomial N(𝔖 _𝜎_ ) for any permutation _𝜎_ . 

- (2) The normalized skew Schur polynomial N( _𝑠𝜆_ / _𝜈_ ) for any skew partition _𝜆_ / _𝜈_ . 

- (3) The normalized Schur P-polynomial N( _𝑃𝜆_ ) for any strict partition _𝜆_ . 

- (4) The normalized key polynomial N( _𝜅 𝜇_ ) for any composition _𝜇_ . 

- (5) The normalized homogeneous Grothendieck polynomial N(𝔊<sup>�</sup> _𝜎_ ) for any permutation _𝜎_ . 

The M-convexity of the support is known for the Schubert polynomial **[29, Corollary 8]** , the skew Schur polynomial **[56, Proposition 2.9]** , the Schur P-polynomial **[56, Proposition 3.5]** , and the key polynomial **[29, Corollary 8]** . The potential validity of each of these conjectures suggests the existence of certain Hodge–Riemann relations, or perhaps more strongly, projective varieties. 

## **3. Intersection cohomology of matroids** 

The set of bases of a matroid M on a finite set _𝐸_ is a subset ℬ ⊆ 2<sup>_𝐸_</sup> that satisfies the _symmetric basis exchange property_ : For any _𝐵_ 1 _, 𝐵_ 2 ∈ ℬ and any _𝑖_ ∈ _𝐵_ 1 \ _𝐵_ 2, there is _𝑗_ ∈ _𝐵_ 2 \ _𝐵_ 1 such that 



Any two bases of M have the same cardinality _𝑑_ = rk M, called the _rank_ of M. When M has a representation _𝜑_ : _𝐸_ → _𝑊_ over a field F, the authors of **[5]** construct a collection of nef 

**17 Combinatorics and Hodge theory** 

divisors ( _𝐿𝑖_ ) _𝑖_ ∈ _𝐸_ on a _𝑑_ -dimensional irreducible projective variety _𝑌_ over F whose volume polynomial is the basis generating polynomial of M: 



The projective variety _𝑌_ , called the _matroid Schubert variety_ of _𝜑_ , is the closure of the image of the dual map _𝜑_<sup>∨</sup> : _𝑊_<sup>∨</sup> → F<sup>_𝐸_</sup> in the product of projective lines (P<sup>1</sup> )<sup>_𝐸_</sup> . In view of Proposition 5, one can say that _𝑌_ is a geometric source of the Lorentzian property of the basis generating polynomial. A detailed study of this _𝑌_ and its resolution of singularities in **[41]** was used to define the _intersection cohomology_ IH(M) of M in **[12]** . When M is not representable over any field, there is no known projective variety that explains the Lorentzian property of the basis generating polynomial of M. However, for any M, one can construct IH(M) as a graded Q-vector space equipped with a symmetric pairing _𝑃_ : IH<sup>∗</sup> (M) × IH<sup>_𝑑_−∗</sup> (M) → Q and graded linear operators _𝐿𝑖_ : IH<sup>∗</sup> (M) → IH<sup>∗+1</sup> (M) for each _𝑖_ in _𝐸_ . The main result of **[12]** is that IH(M) satisfies the Poincaré duality, the hard Lefschetz theorem, and the Hodge–Riemann relations with respect to any positive linear combination of ( _𝐿𝑖_ ) _𝑖_ ∈ _𝐸_ . When M is representable over the complex numbers, the intersection cohomology of M is the intersection cohomology of _𝑌_ with Q-coefficients. When M is representable over a finite field, the intersection cohomology of M is a rational form of the _ℓ_ - adic étale intersection cohomology of _𝑌_ for which the Hodge–Riemann relations hold.6 The existence of IH(M) plays a central role in the resolution of two combinatorial conjectures on M, the top-heavy conjecture for the lattice of flats and the nonnegativity conjecture for the Kazhdan-Lusztig coefficients. Below we outline the construction of IH(M) and explain its relation to the two conjectures. 

The _top-heavy conjecture_ was proposed by Dowling and Wilson in **[22, 23]** . It originates from the following theorem of de Bruijn and Erdős **[20]** : 

_Every finite set of points 𝐸 in a projective plane determines at least_ | _𝐸_ | _lines, unless 𝐸 is contained in a line._ 

In other words, if _𝐸_ is not contained in a line, then the number of lines in the plane containing at least two points in _𝐸_ is at least | _𝐸_ |. The result is valid for any projective plane, not necessarily Desarguesian, and in this sense the statement is purely combinatorial. The figures below depict the two possibilities when | _𝐸_ | = 4. 





> **6** Since Q _ℓ_ is not ordered, there are no Hodge–Riemann relations for the _ℓ_ -adic intersection cohomology. When M is representable over some field, we suspect that IH(M) is a Chow analogue of the intersection cohomology of _𝑋_ . 

**18 J. Huh** 

(4 points determining 6 lines) (4 points determining 4 lines) 

The following more general statement, conjectured by Motzkin in **[57]** , was subsequently proved by many in various settings: 

_Every finite set of points 𝐸 in a projective space determines at least_ | _𝐸_ | _hyperplanes, unless 𝐸 is contained in a hyperplane._ 

Motzkin proved the above for _𝐸_ in real projective spaces in **[58]** . Basterfield and Kelly **[9]** showed the statement in general, and Greene **[35]** strengthened the result by showing that there is an _order-matching_ from _𝐸_ to the set of hyperplanes determined by _𝐸_ , unless _𝐸_ is contained in a hyperplane: 

_For every point in 𝐸 one can choose a hyperplane containing the point in such a way that no hyperplane is chosen twice._ 

Mason **[52]** and Heron **[38]** obtained similar results by different methods. 

Based on these and other known results, Dowling and Wilson formulated the topheavy conjecture in the generality of matroids, in terms of their flats. 

**Definition 22.** A _flat_ of a matroid M on a finite set _𝐸_ is a subset of _𝐸_ that is maximal for its rank. 

In other words, a subset of _𝐸_ is a flat of M if the addition of any other element to the set increases its rank in M. Since the intersection of flats of M is a flat of M, the collection of all flats of M form a lattice ℒ = ℒ(M), the _lattice of flats_ of M. The lattice ℒ is graded, and the rank of a subset _𝑆_ of _𝐸_ in M is the height of the smallest flat of M containing _𝑆_ in the graded lattice ℒ. Thus, one can recover the rank function of M, and hence the set of bases ℬ of M, from the lattice of flats ℒ of M. 

We write ℒ<sup>_𝑘_</sup> for the set of rank _𝑘_ flats of M. When M has a representation _𝜑_ : _𝐸_ → _𝑊_ over a field F, we have 



When _𝜑_ injects _𝐸_ into the projective space P _𝑉_ , there are bijections 

ℒ<sup>1</sup> ≃ the set of points in _𝐸_ and ℒ<sup>2</sup> ≃ the set of lines joining points in _𝐸._ 

The top-heavy conjecture extends the relation between |ℒ<sup>1</sup> | and |ℒ<sup>2</sup> | in de Bruijn–Erdős theorem as follows. 

**Conjecture 23** (Top-heavy conjecture). Let ℒ be the lattice of flats of a rank _𝑑_ matroid. 

(1) For every nonnegative integer _𝑘_ less than<sup>_<u>𝑑</u>_</sup> 2<sup>,</sup> 



In fact, there is an injective map _𝜄_ : ℒ<sup>_𝑘_</sup> → ℒ<sup>_𝑑_−</sup><sup>_𝑘_</sup> satisfying _𝑥_ ≤ _𝜄_ ( _𝑥_ ) for all _𝑥_ . 

**19 Combinatorics and Hodge theory** 

(2) For every nonnegative integer _𝑘_ less than<sup>_<u>𝑑</u>_</sup> 2<sup>,</sup> 



In fact, there is an injective map _𝜄_ : ℒ<sup>_𝑘_</sup> → ℒ<sup>_𝑘_+1</sup> satisfying _𝑥_ ≤ _𝜄_ ( _𝑥_ ) for all _𝑥_ . 

When ℒ is a finite Boolean lattice or a finite projective geometry, Conjecture 23 is a classical result; see for example **[72, Corollary 4.8 and Exercise 4.4]** . In these self-dual cases, the second statement of Conjecture 23 says that ℒ admits order-matchings 



These order-matchings partition ℒ into |ℒ<sup>⌊</sup><sup>_<u>𝑑</u>_</sup> 2<sup>⌋</sup> | disjoint chains, and hence ℒ has the _Sperner property_ : 

_The maximal number of pairwise incomparable subsets of_ [ _𝑛_ ] _is the maximum among the binomial coefficients_<sup>�</sup><sup>_𝑛_</sup> _𝑘_ � _. Similarly, the maximal number of pairwise incomparable subspaces of_ F _𝑞_<sup>_𝑛is the maximum among the 𝑞-binomial coefficients_</sup> � _𝑛𝑘_ � _𝑞_<sup>_._</sup> 

Let M be a rank _𝑑_ matroid on a finite set _𝐸_ . The proof of Conjecture 23 in **[12]** is based on a detailed analysis of the _graded Möbius algebra_ 



The grading is defined by declaring the degree of the element _𝑦𝐹_ to be rk _𝐹_ , the rank of _𝐹_ in M. The multiplication is defined by the formula 



where ∨ stands for the join in the lattice of flats of M. Unlike its ungraded counterpart, which is isomorphic to the product of Q’s as a Q-algebra **[69, Theorem 1]** , the graded Möbius algebra has a nontrivial algebra structure. 

There is a straightforward relation between the basis generating polynomial of M and the graded Möbius algebra of M. For each _𝑖_ in _𝐸_ , we associate a degree 1 element 



Writing deg for the isomorphism H<sup>_𝑑_</sup> (M) ≃ Q with deg( _𝑦𝐸_ ) = 1, we have 



For the top-heavy conjecture, of central importance is the element _𝐿_ ≔<sup>�</sup> _𝑖_ ∈ _𝐸_<sup>_𝐿_</sup> _𝑖_<sup>.Thefol-</sup> lowing elementary statement on H(M), proposed in **[41, Conjecture 7]** , is one of the main conclusions of **[12]** . Its analogue for Weyl groups and for general Coxeter groups can be found in **[11]** and **[55]** . 

**20 J. Huh** 

**Theorem 24.** For every nonnegative integer _𝑘_ ≤<sup>_<u>𝑑</u>_</sup> 2<sup>, the multiplication map</sup> 



is injective (the _injective hard Lefschetz property_ for M). 

To deduce Conjecture 23 from Theorem 24, consider the matrix of the multiplication map with respect to the standard bases of the source and the target. Entries of this matrix are labeled by pairs of elements of ℒ , and all the entries corresponding to incomparable pairs are zero. The matrix has full rank by Theorem 24, so there is a maximal square submatrix with a nonzero determinant. In the standard expansion of this determinant, there must be a nonzero term, and the permutation corresponding to this term produces the injective map _𝜄_ in Conjecture 23. 

It seems difficult to prove Theorem 24 directly. One possible reason for this is the lack of Poincaré duality for H(M): Typically, for small _𝑘_ , a matroid has much more corank _𝑘_ flats than rank _𝑘_ flats. In known settings where the hard Lefschetz property is the main statement needed for applications **[12, 26, 45]** , it was necessary to prove Poincaré duality, the hard Lefschetz property, and the Hodge–Riemann relations together as a single package. 

The intersection cohomology IH(M) is an H(M)-module that repairs the failure of Poincaré duality of H(M) in an efficient way. The construction of IH(M) is inspired by the Kazhdan–Lusztig theory of matroids developed in **[25]** . For any flat _𝐹_ of M, we define the _localization_ of M at _𝐹_ to be the matroid M<sup>_𝐹_</sup> on the ground set _𝐹_ whose flats are the flats of M contained in _𝐹_ . Similarly, we define the _contraction_ of M at _𝐹_ to be the matroid M _𝐹_ on the ground set _𝐸_ \ _𝐹_ whose flats are _𝐺_ \ _𝐹_ for flats _𝐺_ of M containing _𝐹_ .7 According to **[14, Theorem 2.2]** , there is a unique way to assign a polynomial _𝑃_ M( _𝑡_ ) to each matroid M, called the _Kazhdan–Lusztig polynomial_ of M, subject to the following three conditions: 

- (1) If rk M = 0, then _𝑃_ M ( _𝑡_ ) is the constant polynomial 1. 

- (2) If rk M _>_ 0, then the degree of _𝑃_ M ( _𝑡_ ) is strictly less than rk M/2. 



The polynomial _𝑍_ M( _𝑡_ ), called the _𝑍-polynomial_ of M, was introduced in **[65]** using a different but equivalent definition of _𝑃_ M ( _𝑡_ ). 

**Example 25.** It is straightforward to check that the Kazhdan–Lusztig polynomial is 1 for matroids of rank at most two. Thus, when the rank of M is three, we should have 



Since the degree of _𝑃_ M ( _𝑡_ ) is at most 1, it follows that _𝑃_ M ( _𝑡_ ) = 1 + |ℒ<sup>2</sup> | _𝑡_ −|ℒ<sup>1</sup> | _𝑡_ . 

> **7** In **[25]** , as well as several other references on Kazhdan–Lusztig polynomials of matroids, the localization is denoted M _𝐹_ and the contraction is denoted M<sup>_𝐹_</sup> . Our notational choice here is consistent with **[1]** and **[12, 13]** . 

**21 Combinatorics and Hodge theory** 

**Example 26.** When the rank of M is four, computing as in Example 25, we get _𝑃_ M ( _𝑡_ ) = 1 + |ℒ<sup>3</sup> | _𝑡_ −|ℒ<sup>1</sup> | _𝑡_ . When the rank of M is five **[25, Proposition 2.16]** , we have 

_𝑃_ M( _𝑡_ ) = 1 + |ℒ<sup>4</sup> | _𝑡_ −|ℒ<sup>1</sup> | _𝑡_ + |ℒ<sup>3</sup> | _𝑡_<sup>2</sup> −|ℒ<sup>2</sup> | _𝑡_<sup>2</sup> + |ℒ<sup>1</sup><sup>_,_2</sup> | _𝑡_<sup>2</sup> −|ℒ<sup>1</sup><sup>_,_4</sup> | _𝑡_<sup>2</sup> + |ℒ<sup>2</sup><sup>_,_4</sup> | _𝑡_<sup>2</sup> −|ℒ<sup>2</sup><sup>_,_3</sup> | _𝑡_<sup>2</sup> _,_ where |ℒ<sup>_𝑖, 𝑗_</sup> | is the number of incidences between the flats of rank _𝑖_ and rank _𝑗_ . For example, if M is the uniform matroid of rank 5 on 6 elements, _𝑃_ M ( _𝑡_ ) = 1 + 9 _𝑡_ + 5 _𝑡_<sup>2</sup> . 

The following _nonnegativity conjecture_ was proposed in **[25, Conjecture 2.8]** , where it was proved for matroids representable over some field using _ℓ_ -adic étale intersection cohomology theory of **[10]** . For sparse paving matroids, a combinatorial proof of the nonnegativity was given in **[48]** . The general case of the conjecture is proved in **[12, Theorem 1.3]** using the intersection cohomology of matroids. 

**Conjecture 27** (Nonnegativity conjecture). _𝑃_ M ( _𝑡_ ) has nonnegative coefficients for any M. 

Kazhdan–Lusztig polynomials of matroids are special cases of Kazhdan–Lusztig– Stanley polynomials **[64, 71]** . Several important families of Kazhdan–Lusztig–Stanley polynomials turn out to have nonnegative coefficients, including classical Kazhdan–Lusztig polynomials associated with Bruhat intervals **[26]** and _𝑔_ -polynomials of convex polytopes **[45]** . Each of the known proofs of the nonnegativity of the three Kazhdan–Lusztig–Stanley polynomials involves numerous details that are unique to that specific case. 

The following existence result of **[12]** implies Conjecture 23 and Conjecture 27. Let _𝐾_ (M) be the open convex cone of degree 1 elements 



The elements of _𝐾_ (M) act as linear operators by multiplication on any H(M)-module. 

**Theorem 28.** There is a graded H(M)-module IH(M) and a symmetric bilinear pairing 



that satisfies the following properties for any nonnegative integer _𝑘_ ≤<sup>_<u>𝑑</u>_</sup> 2<sup>:</sup> 





is nondegenerate ( _Poincaré duality theorem_ for M). 





is an isomorphism ( _hard Lefschetz theorem_ for M). 

(3) For any _𝐿_ 0 _, 𝐿_ 1 _, . . . , 𝐿𝑑_ −2 _𝑘_ ∈ _𝐾_ ( _𝑋_ ), the symmetric bilinear form 



**J. Huh** 

**22** 

is positive definite on the kernel of the linear map 



( _Hodge–Riemann relations_ for M). 

(4) Writing IH∅ for the graded vector space IH(M) ⊗H(M) Q, we have 



( _Kazhdan–Lusztig identities_ for M). 

- (5) IH<sup>0</sup> (M) generates a submodule isomorphic to H(M) ( _Purity_ for M). 

Since injective maps restrict to injective maps, the injective hard Lefschetz property for M in Theorem 24, and hence the top-heavy conjecture for M, follows from the hard Lefschetz theorem and the purity for M. The nonnegativity conjecture for M follows from the Kazhdan–Lusztig identities for M. More generally, when a finite group Γ acts on M, one can define the _equivariant Kazhdan–Lusztig polynomial 𝑃_ M<sup>Γ(</sup><sup>_𝑡_)asin</sup><sup>**[32]**.Thisisapolynomial</sup> with coefficients in the ring of virtual representations of Γ, with the property that taking dimensions recovers the ordinary polynomial _𝑃_ M ( _𝑡_ ). The authors of **[12]** show that Γ acts naturally on IH(M) and that 



This proves the equivariant nonnegativity conjecture proposed in **[32, Conjecture 2.13]** . Conjecture 27 is the special case when Γ is trivial. 

The construction of IH(M) is inspired by geometry in the representable case. Consider the case when M has a representation _𝜑_ : _𝐸_ → _𝑊_ over C, and recall that the matroid Schubert variety _𝑌_ of _𝜑_ is the closure of _𝑊_<sup>∨</sup> in the product of projective lines (P<sup>1</sup> )<sup>_𝐸_</sup> . The additive group _𝑊_<sup>∨</sup> acts on _𝑌_ with finitely many orbits, each of which is isomorphic to an affine space. The poset of cells in this stratification of _𝑌_ is isomorphic to the poset of cells is isomorphic to the lattice of flats of M, and, in fact, the singular cohomology H<sup>2∗</sup> ( _𝑌,_ Q) is isomorphic to the graded Möbius algebra H<sup>∗</sup> (M) **[41, Theorem 14]** .8 

The Schubert variety admits a distinguished resolution of singularities _𝑓_ : _𝑋_ → _𝑌_ obtained by blowing up all the strata in the order of increasing dimension. The resulting smooth projective variety _𝑋_ is the _augmented wonderful variety_ of _𝜑_ studied in **[13]** . Adopting the computations in **[21, 28]** , one can show that its singular cohomology and Chow rings are isomorphic to the _augmented Chow ring_ 

CH(M) ≔ Q[ _𝑦𝑖, 𝑥𝐹_ | _𝑖_ is an element of _𝐸_ and _𝐹_ is a proper flat of M]/( _𝐼_ M + _𝐽_ M) _,_ 

> **8** All the cohomology rings and intersection cohomology groups of varieties in this paper vanish in odd degrees, and our isomorphisms double degrees. 

**23 Combinatorics and Hodge theory** 

where _𝐼_ M is the ideal generated by the linear forms 



and _𝐽_ M is the ideal generated by the quadratic monomials 





As expected from the identification with H<sup>2∗</sup> ( _𝑋,_ Q) in the representable case, for any M, the augmented Chow ring of M vanishes in degrees larger than _𝑑_ . Furthermore, there is a unique linear map 



where ℱ is any complete flag of proper flats of M, defining a symmetric pairing on CH(M). The main observation is that the pullback homomorphism in singular cohomology 



only depends on M and not on _𝜑_ . In terms of the graded Möbius algebra and the augmented Chow ring of M, the pullback homomorphism is given by 



Applying the decomposition theorem of Beilinson–Bernstein–Deligne–Gabber **[10]** to _𝑓_ , we find that the intersection cohomology IH<sup>∗</sup> ( _𝑌_ ) is isomorphic as a graded H<sup>∗</sup> ( _𝑌_ )-module to a direct summand of H<sup>∗</sup> ( _𝑋_ ). Furthermore, a slight extension of an argument of Ginzburg **[34]** shows that IH<sup>∗</sup> ( _𝑌_ ) is indecomposable as an H<sup>∗</sup> ( _𝑌_ )-module. This motivates the following definition. 

**Definition 29.** The intersection cohomology IH(M) of a matroid M is the unique indecomposable graded H(M)-module direct summand of CH(M) that is nonzero in degree zero. 

The above defines the intersection cohomology of M up to isomorphism of graded H(M)-modules, where the uniqueness is given by the general Krull–Schmidt theorem **[7, Theorem 1]** . The intersection cohomology inherits a symmetric pairing _𝑃_ from CH(M). In **[12]** , the authors construct a canonical submodule IH(M) ⊆ CH(M) that is preserved by all the symmetries of M. The construction of IH(M) as an explicit submodule of CH(M), or more generally the construction of the _canonical decomposition_ of CH(M) as a graded H(M)module, is essential in inductively proving Poincaré duality, the hard Lefschetz theorem, and the Hodge–Riemann relations for IH(M). 

## **Acknowledgments** 

I thank my past and current collaborators: Karim Adiprasito, Federico Ardila, Farhad Babaee, Tom Braden, Petter Brändén, Graham Denham, Chris Eur, Eric Katz, Matt Larson, Jacob Matherne, Karola Mészáros, Nick Proudfoot, Benjamin Schröter, Avery 

**24 J. Huh** 

St. Dizier, Bernd Sturmfels, and Botong Wang. It was a privilege to have connected with your minds, and I am grateful for our mathematical adventures together. 

## **Funding** 

This work was partially supported by Simons Investigator Grant and NSF Grant DMS2053308. 

## **References** 

|**[1]**|K. Adiprasito, J. Huh, and E. Katz, Hodge theory for combinatorial geometries.<br>_Ann. of Math. (2)_**188**(2018), no. 2, 381–452|
|---|---|
|**[2]**|N. Anari, S. O. Gharan, and C. Vinzant, Log-concave polynomials, I: entropy and<br>a deterministic approximation algorithm for counting bases of matroids._Duke_<br>_Math. J._**170**(2021), no. 16, 3459–3504|
|**[3]**|N. Anari, K. Liu, S. O. Gharan, and C. Vinzant, Log-concave polynomials II:<br>High-dimensional walks and an FPRAS for counting bases of a matroid. In<br>_STOC’19—Proceedings of the 51st Annual ACM SIGACT Symposium on Theory_<br>_of Computing_, pp. 1–12, ACM, New York, 2019|
|**[4]**|N. Anari, K. Liu, S. Oveis Gharan, and C. Vinzant, Log-concave polynomials<br>III: Mason’s ultra-log-concavity conjecture for independent sets of matroids.<br>arXiv:1811.01600|
|**[5]**|F. Ardila and A. Boocher, The closure of a linear space in a product of lines._J._<br>_Algebraic Combin._**43**(2016), no. 1, 199–235|
|**[6]**|F. Ardila, G. Denham, and J. Huh, Lagrangian geometry of matroids._J. Amer._<br>_Math. Soc._, to appear. DOI: https://doi.org/10.1090/jams/1009|
|**[7]**|M. Atiyah, On the Krull-Schmidt theorem with application to sheaves._Bull. Soc._<br>_Math. France_**84**(1956), 307–317|
|**[8]**|W. Baldoni and M. Vergne, Kostant partitions functions and flow polytopes.<br>_Transform. Groups_**13**(2008), no. 3-4, 447–469|
|**[9]**|J. G. Basterfield and L. M. Kelly, A characterization of sets of_𝑛_points which<br>determine_𝑛_hyperplanes._Proc. Cambridge Philos. Soc._**64**(1968), 585–588|
|**[10]**|A. A. Be˘ılinson, J. Bernstein, and P. Deligne, Faisceaux pervers. In_Analysis and_<br>_topology on singular spaces, I (Luminy, 1981)_, pp. 5–171, Astérisque 100, Soc.<br>Math. France, Paris, 1982|
|**[11]**|A. Björner and T. Ekedahl, On the shape of Bruhat intervals._Ann. of Math. (2)_<br>**170**(2009), no. 2, 799–817|
|**[12]**|T. Braden, J. Huh, J. Matherne, N. Proudfoot, and B. Wang, Singular Hodge<br>theory for combinatorial geometries. arXiv:2010.06088|
|**[13]**|T. Braden, J. Huh, J. P. Matherne, N. Proudfoot, and B. Wang, A semi-small<br>decomposition of the Chow ring of a matroid. arXiv:2002.03341|
|**[14]**|T. Braden and A. Vysogorets, Kazhdan-Lusztig polynomials of matroids under<br>deletion._Electron. J. Combin._**27**(2020), no. 1, Paper No. 1.17, 17|



**25 Combinatorics and Hodge theory** 

|**[15]**|P. Brändén, Discrete concavity and the half-plane property._SIAM J. Discrete_<br>_Math._**24**(2010), no. 3, 921–933|
|---|---|
|**[16]**|P. Brändén, Spaces of Lorentzian and real stable polynomials are Euclidean balls.<br>_Forum Math. Sigma_**9**(2021), Paper No. e73, 8|
|**[17]**|P. Brändén and J. Huh, Lorentzian polynomials._Ann. of Math. (2)_**192**(2020),<br>no. 3, 821–891|
|**[18]**|E. Cattani, Mixed Lefschetz theorems and Hodge-Riemann bilinear relations._Int._<br>_Math. Res. Not. IMRN_ (2008), no. 10, Art. ID rnn025, 20|
|**[19]**|C. Chindris, H. Derksen, and J. Weyman, Counterexamples to Okounkov’s log-<br>concavity conjecture._Compos. Math._**143**(2007), no. 6, 1545–1557|
|**[20]**|N. G. de Bruijn and P. Erdös, On a combinatorial problem._Nederl. Akad._<br>_Wetensch., Proc._**51**(1948), 1277–1279 = Indagationes Math. 10, 421–423 (1948)|
|**[21]**|C. De Concini and C. Procesi, Wonderful models of subspace arrangements.<br>_Selecta Math. (N.S.)_**1**(1995), no. 3, 459–494|
|**[22]**|T. A. Dowling and R. M. Wilson, The slimmest geometric lattices._Trans. Amer._<br>_Math. Soc._**196**(1974), 203–215|
|**[23]**|T. A. Dowling and R. M. Wilson, Whitney number inequalities for geometric lat-<br>tices._Proc. Amer. Math. Soc._**47**(1975), 504–512|
|**[24]**|J. Edmonds, Submodular functions, matroids, and certain polyhedra. In_Combina-_<br>_torial Structures and their Applications (Proc. Calgary Internat. Conf., Calgary,_<br>_Alta., 1969)_, pp. 69–87, Gordon and Breach, New York, 1970|
|**[25]**|B. Elias, N. Proudfoot, and M. Wakefield, The Kazhdan-Lusztig polynomial of a<br>matroid._Adv. Math._**299**(2016), 36–70|
|**[26]**|B. Elias and G. Williamson, The Hodge theory of Soergel bimodules._Ann. of_<br>_Math. (2)_**180**(2014), no. 3, 1089–1136|
|**[27]**|C. Eur and J. Huh, Logarithmic concavity for morphisms of matroids._Adv. Math._<br>**367**(2020), 107094, 19|
|**[28]**|E. M. Feichtner and S. Yuzvinsky, Chow rings of toric varieties defined by atomic<br>lattices._Invent. Math._**155**(2004), no. 3, 515–536|
|**[29]**|A. Fink, K. Mészáros, and A. St. Dizier, Schubert polynomials as integer point<br>transforms of generalized permutahedra._Adv. Math._**332**(2018), 465–475|
|**[30]**|W. Fulton,_Introduction to toric varieties_. Annals of Mathematics Studies 131,<br>Princeton University Press, Princeton, NJ, 1993|
|**[31]**|W. Fulton,_Young tableaux_. London Mathematical Society Student Texts 35, Cam-<br>bridge University Press, Cambridge, 1997|
|**[32]**|K. Gedeon, N. Proudfoot, and B. Young, The equivariant Kazhdan-Lusztig poly-<br>nomial of a matroid._J. Combin. Theory Ser. A_**150**(2017), 267–294|
|**[33]**|I. M. Gelfand, R. M. Goresky, R. D. MacPherson, and V. V. Serganova, Combina-<br>torial geometries, convex polyhedra, and Schubert cells._Adv. in Math._**63**(1987),<br>no. 3, 301–316|
|**[34]**<br>**26**|V. Ginsburg, Perverse sheaves andC<sup>∗</sup>-actions._J. Amer. Math. Soc._**4**(1991), no. 3,<br>483–490<br>**J. Huh**|



|**[35]**|C. Greene, A rank inequality for finite geometric lattices._J. Combinatorial Theory_<br>**9**(1970), 357–364|
|---|---|
|**[36]**|A. Grothendieck, Standard conjectures on algebraic cycles. In_Algebraic Geometry_<br>_(Internat. Colloq., Tata Inst. Fund. Res., Bombay, 1968)_, pp. 193–199, Oxford<br>Univ. Press, London, 1969|
|**[37]**|L. Gurvits, On multivariate Newton-like inequalities. In_Advances in combinato-_<br>_rial mathematics_, pp. 61–78, Springer, Berlin, 2009|
|**[38]**|A. P. Heron, A property of the hyperplanes of a matroid and an extension of Dil-<br>worth’s theorem._J. Math. Anal. Appl._**42**(1973), 119–131|
|**[39]**|J. Herzog and T. Hibi, Discrete polymatroids._J. Algebraic Combin._**16**(2002),<br>no. 3, 239–268 (2003)|
|**[40]**|J. Huh, J. Matherne, K. Mészáros, and A. St. Dizier, Logarithmic concavity<br>of Schur and related polynomials._Trans. Amer. Math. Soc._, to appear. DOI:<br>https://doi.org/10.1090/tran/8606|
|**[41]**|J. Huh and B. Wang, Enumeration of points, lines, planes, etc._Acta Math._**218**<br>(2017), no. 2, 297–317|
|**[42]**|J. E. Humphreys,_Representations of semisimple Lie algebras in the BGG cate-_<br>_gory_𝒪. Graduate Studies in Mathematics 94, American Mathematical Society,<br>Providence, RI, 2008|
|**[43]**|D. Huybrechts,_Complex geometry_. Universitext, Springer-Verlag, Berlin, 2005|
|**[44]**|C. Jiang and Z. Li, Algebraic reverse Khovanskii–Teissier inequality via Okounkov<br>bodies. arXiv:2012.02847|
|**[45]**|K. Karu, Hard Lefschetz theorem for nonrational polytopes._Invent. Math._**157**<br>(2004), no. 2, 419–447|
|**[46]**|J. P. S. Kung, Strong maps. In_Theory of matroids_, pp. 224–253, Encyclopedia<br>Math. Appl. 26, Cambridge Univ. Press, Cambridge, 1986|
|**[47]**|R. Lazarsfeld,_Positivity in algebraic geometry. I_. Ergebnisse der Mathematik und<br>ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results<br>in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in<br>Mathematics] 48, Springer-Verlag, Berlin, 2004|
|**[48]**|K. Lee, G. D. Nasr, and J. Radcliffe, A combinatorial formula for Kazhdan–<br>Lusztig polynomials of sparse paving matroids. arXiv:2002.03341|
|**[49]**|B. Lehmann and J. Xiao, Correspondences between convex geometry and com-<br>plex geometry._Épijournal Géom. Algébrique_**1**(2017), Art. 6, 29|
|**[50]**|T. M. Liggett, Ultra logconcave sequences and negative dependence._J. Combin._<br>_Theory Ser. A_**79**(1997), no. 2, 315–325|
|**[51]**|D. Maclagan and B. Sturmfels,_Introduction to tropical geometry_. Graduate<br>Studies in Mathematics 161, American Mathematical Society, Providence, RI,<br>2015|
|**[52]**|J. H. Mason, Matroids: unimodal conjectures and Motzkin’s theorem. In_Com-_<br>_binatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972)_, pp.<br>207–220, 1972|



**27 Combinatorics and Hodge theory** 

|**[53]**|D. Mayhew, M. Newman, and G. Whittle, Yes, the ‘missing axiom’ of matroid<br>theory is lost forever._Trans. Amer. Math. Soc._**370**(2018), no. 8, 5907–5929|
|---|---|
|**[54]**|D. Mayhew, G. Whittle, and M. Newman, Is the missing axiom of matroid theory<br>lost forever?_Q. J. Math._**65**(2014), no. 4, 1397–1415|
|**[55]**|G. Melvin and W. Slofstra, Soergel bimodules and the shape of Bruhat intervals.<br>2020, preprint|
|**[56]**|C. Monical, N. Tokcan, and A. Yong, Newton polytopes in algebraic combina-<br>torics._Selecta Math. (N.S.)_**25**(2019), no. 5, Paper No. 66, 37|
|**[57]**|T. Motzkin,_Beiträge zur theorie der linearen ungleichungen_. 1936|
|**[58]**|T. Motzkin, The lines and planes connecting the points of a finite set._Trans. Amer._<br>_Math. Soc._**70**(1951), 451–464|
|**[59]**|K. Murota,_Discrete convex analysis_. SIAM Monographs on Discrete Mathe-<br>matics and Applications, Society for Industrial and Applied Mathematics (SIAM),<br>Philadelphia, PA, 2003|
|**[60]**|P. Nelson, Almost all matroids are nonrepresentable._Bull. Lond. Math. Soc._**50**<br>(2018), no. 2, 245–248|
|**[61]**|A. Okounkov, Why would multiplicities be log-concave? In_The orbit method_<br>_in geometry and physics (Marseille, 2000)_, pp. 329–347, Progr. Math. 213,<br>Birkhäuser Boston, Boston, MA, 2003|
|**[62]**|J. Oxley,_Matroid theory_. Second edn., Oxford Graduate Texts in Mathematics 21,<br>Oxford University Press, Oxford, 2011|
|**[63]**|A. Postnikov, Permutohedra, associahedra, and beyond._Int. Math. Res. Not. IMRN_<br>(2009), no. 6, 1026–1106|
|**[64]**|N. Proudfoot, The algebraic geometry of Kazhdan-Lusztig-Stanley polynomials.<br>_EMS Surv. Math. Sci._**5**(2018), no. 1-2, 99–127|
|**[65]**|N. Proudfoot, Y. Xu, and B. Young, The_𝑍_-polynomial of a matroid._Electron. J._<br>_Combin._**25**(2018), no. 1, Paper 1.26, 21|
|**[66]**|R. Schneider,_Convex bodies: the Brunn-Minkowski theory_. expanded edn., Ency-<br>clopedia of Mathematics and its Applications 151, Cambridge University Press,<br>Cambridge, 2014|
|**[67]**|J.-P. Serre, Analogues kählériens de certaines conjectures de Weil._Ann. of Math._<br>_(2)_**71**(1960), 392–394|
|**[68]**|A. D. Sokal, The multivariate Tutte polynomial (alias Potts model) for graphs and<br>matroids. In_Surveys in combinatorics 2005_, pp. 173–226, London Math. Soc.<br>Lecture Note Ser. 327, Cambridge Univ. Press, Cambridge, 2005|
|**[69]**|L. Solomon, The Burnside algebra of a finite group._J. Combinatorial Theory_**2**<br>(1967), 603–615|
|**[70]**|R. P. Stanley, The number of faces of a simplicial convex polytope._Adv. in Math._<br>**35**(1980), no. 3, 236–238|
|**[71]**|R. P. Stanley, Subdivisions and local_ℎ_-vectors._J. Amer. Math. Soc._**5**(1992),<br>no. 4, 805–851|



**28 J. Huh** 

- **[72]** R. P. Stanley, _Algebraic combinatorics_ . Undergraduate Texts in Mathematics, Springer, Cham, 2018 

- **[73]** P. Vámos, The missing axiom of matroid theory is lost forever. _J. London Math. Soc. (2)_ **18** (1978), no. 3, 403–408 

- **[74]** S. T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I. _Comm. Pure Appl. Math._ **31** (1978), no. 3, 339–411 

## **June Huh** 

Fine Hall, Washington Road, Princeton NJ 08544-1000 USA, huh@princeton.edu 

**29 Combinatorics and Hodge theory** 

