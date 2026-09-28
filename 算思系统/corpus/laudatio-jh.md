# **The Work of June Huh Gil Kalai** 

### **Abstract** 

June Huh found striking connections between algebraic geometry and combinatorics, solved central problems in combinatorics that had remained open for decades, and developed a theory of great importance for both fields. June Huh has been awarded the 2022 Fields Medal “for bringing the ideas of Hodge theory to combinatorics, the proof of the Dowling–Wilson conjecture for geometric lattices, the proof of the Heron–Rota–Welsh conjecture for matroids, the development of the theory of Lorentzian polynomials, and the proof of the strong Mason conjecture.” In this paper I will review some of June Huh’s contributions. 

### **Mathematics Subject Classification 2020** 

Primary 05E14; Secondary 52C35, 05B35, 05C31, 14T15, 52B40 

### **Keywords** 

Matroids, log-concavity, hard Lefschetz theorems, Hodge–Riemann relations 

> © 2022 International Mathematical Union Preliminary version, to appear in Proc. Int. Cong. Math. 2022, Vol. 1. DOI 10.4171/ICM2022/211 

June Huh has made groundbreaking contributions in combinatorics and algebraic geometry and his work established profound connections between these two areas. This paper describes some of Huh’s main achievements and gives some background, primarily on the combinatorial aspects of his work. 

The Heron–Rota–Welsh unimodality conjecture ( **[32, 56, 64]** ) asserts that the coefficients of the characteristic polynomial of a matroid form a log-concave sequence. This implies that the coefficients are unimodal. A special case of the conjecture is an earlier conjecture by Read, asserting that the coefficients of the chromatic polynomial of a graph are unimodal. In 2009 June Huh used algebraic geometry to prove Read’s unimodality conjecture **[33]** for graphs, and the more general Heron–Rota–Welsh conjecture for matroids represented over a field of characteristic 0. The case of matroids representable over a field of a non-zero characteristic and the case of general matroids remained open. In 2010 June Huh and Eric Katz **[36]** found a different algebraic-geometric approach and proved the case of matroids representable over a field of an arbitrary characteristic. Finally, in 2015 the Heron–Rota–Welsh conjecture was proved in full generality by Karim Adiprasito, June Huh, and Eric Katz **[1]** . For this purpose it was necessary to extend theorems from algebraic geometry (primarily the Hodge–Riemann relations and the hard Lefschetz theorem) to cases well beyond the scope of algebraic geometry. Huh and his coauthors developed an entirely novel theory of great interest and importance. 

June Huh and Botong Wang **[37]** used connections with algebraic geometry to prove the Dowling–Wilson conjecture. Consider a configuration P of _𝑛_ points spanning a _𝑑_ - dimensional space. Let _𝑤𝑖_ be the number of linear spaces of dimension _𝑖_ spanned by the points. 

Motzkin conjectured in his 1936 Ph.D. thesis, and proved over the reals in 1951 **[50]** , that _𝑤_ 1 ≤ _𝑤𝑑_ −1. The case of _𝑑_ = 3 (in a planar affine formulation) was proved in 1948 by de Bruĳn and Erdős, and their abstract combinatorial proof applies to every characteristic. 

The Dowling–Wilson “top heavy” conjecture **[22]** asserts that 



An extension of the Dowling–Wilson conjecture for arbitrary matroids (of rank _𝑑_ ) was proved by Tom Braden, June Huh, Jacob Matherne, Nicholas Proudfoot, and Botong Wang **[12]** . 

The Mason conjecture (on independence numbers) asserts **[45]** that the sequence of numbers of independent sets of size _𝑘_ of general matroids is log-concave and it comes in several strengths. Following Huh’s first result the conjecture was proved by Mathias Lenz **[43]** for representable real matroids and it was proved for general matroids in **[1]** . The strong Mason conjecture for arbitrary matroids was proved by June Huh, Benjamin Schröter, and Botong Wang **[38]** who relied on **[1]** . 

These works have led to further advances by several groups of researchers, and I would especially like to mention the solution of the Mihail–Vazirani conjecture on the expansion constant and rapid mixing for random walks on matroids, by Anari, Oveis Gharan, and Vinzant **[4]** , as well as the works by Brändén and Huh **[13]** on correlation inequalities for the Potts model. 

**2 G. Kalai** 

Following is the structure of this paper. In Section 1 we discuss chromatic polynomials and Read’s conjecture. In Section 2 we discuss matroids and the Heron–Rota–Welsh conjecture. In Section 3 we discuss the Dowling–Wilson conjecture. Section 4 is devoted to algebraic geometry, Hodge theory, and the Grothendieck standard conjectures. In Section 5 we discuss the Mason conjectures and some recent applications and connections. A recent review paper aimed for a general audience on Huh’s work and mathematical background was written by Andrei Okounkov **[51]** . 

### **1. Graphs, chromatic polynomials, and Read’s conjecture** 

## **1.1. The four-color conjecture and chromatic polynomials** 

A proper coloring of a graph _𝐺_ is a coloring of the vertices of _𝐺_ such that every two adjacent vertices are colored with different colors. Graph coloring is of central importance in graph theory and in graph algorithms. 

**Theorem 1** (The four-color theorem (Appel and Haken 1976)). _Every planar graph can be properly colored with 4 colors._ 

The four-color conjecture was proposed (in a dual form, for planar maps) by Francis Guthrie in 1852 and proved by Kenneth Appel and Wolfgang Haken in 1976. 

For a graph _𝐺_ , let _𝜒𝐺_ ( _𝑘_ ) be the number of proper colorings of _𝐺_ with _𝑘_ colors. _𝜒𝐺_ ( _𝑘_ ) is called the chromatic polynomial of the graph _𝐺_ . Chromatic polynomials were introduced by George Birkhoff for planar maps as a possible tool for the study of the four-color conjecture. Later Hassler Whitney extended the definition to general graphs. William Tutte found a far-reaching generalization, now called the Tutte polynomial and also introduced the related Tutte–Grothendieck invariants for graphs, which can be seen as an early bridge between graph theory and algebraic geometry. A starting point of Tutte’s work is the deletioncontraction operations. For a graph _𝐺_ and an edge _𝑒_ of _𝐺_ , let _𝐺_ \ _𝑒_ denote the graph obtained by deleting the edge _𝑒_ , and _𝐺_ / _𝑒_ denote the graph obtained by contracting the edge _𝑒_ , that is, by merging its two vertices to a single vertex adjacent to neighbors of both. A fundamental relation for chromatic polynomials is 



This relation gives an easy inductive proof of the fact that the chromatic polynomial is indeed a polynomial. A graph _𝐻_ is called a minor of a graph _𝐺_ if it can be obtained from _𝐺_ by a sequence of deletions and contractions. Richard Stanley proved **[59]** that _𝜒𝐺_ (−1) equals the number of acyclic orientations of _𝐺_ . 

## **1.2. Read’s conjecture** 

In 1968 Ronald Read proposed the following conjecture. Suppose that 



then, the sequence _𝑎_ 0 _, 𝑎_ 1 _, . . . , 𝑎𝑛_ is unimodal. 

**3 The Work of June Huh** 

A much more general conjecture was posed a short time later by Andrew Heron, Gian-Carlo Rota, and Dominic Welsh. They also conjectured a stronger statement, namely, that the sequence of coefficients is actually log-concave: 



**Theorem 2** (June Huh **[33]** ). _The coefficients of the chromatic polynomial 𝜒𝐺_ ( _𝑥_ ) _of every graph 𝐺 are log-concave._ 

The unimodality and log-concavity of sequences arising in combinatorics and algebra have been studied by many researchers and in this context I would like to refer the reader to the survey articles **[15,16,62]** . A stronger property than log concavity of the coefficients of real polynomials is that of having only real roots. This is not the case for chromatic polynomials of graphs in general (but the location of the roots is still a fascinating topic). Unimodality of the numbers of elements according to their heights in general graded posets is also related to the important “Sperner property” of posets. We note that there are cases where unimodality was expected but failed, e.g., unimodality of face numbers of polytopes **[11]** , and of Young lattices **[63]** . 

I first heard about Huh’s startling proof of the Read conjecture from a 2011 paper by Jiří Matoušek **[46]** who regarded this result, among a few other results, as the beginning of a new era in discrete geometry and wrote: 

_“To me, 2010 looks as annus mirabilis, a miraculous year, in several areas of my mathematical interests. Below I list seven highlights and breakthroughs, mostly in discrete geometry, hoping to share some of my wonder and pleasure with the readers.”_ 

Huh’s proof relied on connections of the problem to singularities of local analytic functions and ultimately to mixed multiplicities of certain ideals. In his proof Huh related the coefficients of the chromatic polynomial to the Milnor numbers of a complex hyperplane arrangement associated with the graph _𝐺_ and, as we discuss in the next section, his proof extends to arbitrary complex hyperplane arrangements. Huh’s connection between chromatic polynomials of graphs and algebraic geometry was, on the one hand, a complete surprise but, on the other hand, it tied in with several developments in and around algebraic combinatorics dating to the mid-1970s. Huh’s subsequent discoveries where he further applied algebraic geometry and especially Hodge theory to combinatorics, beautifully combined new and old ideas. 

### **2. Matroids and the Heron–Rota–Welsh conjecture** 

## **2.1. Matroids** 

Let _𝑋_ = { _𝑥_ 1 _, 𝑥_ 2 _, . . . , 𝑥𝑛_ } be a set of points in some vector space. We can associate 

with _𝑋_ : 

**4 G. Kalai** 

- The set of linearly independent subsets of _𝑋_ . 

- The set of bases of _𝑋_ (a base is a maximal independent set). 

- The set of circuits of _𝑋_ (a circuit is a minimal dependent set). 

- The set of flats of _𝑋_ (a flat is a subset that is closed under linear combination). 

- The rank function that associates to a subset _𝑌_ of _𝑋_ the dimension of the vector space spanned by _𝑌_ . 

Matroids were introduced by Hassler Whitney **[66]** as a generalization of configurations of points in linear spaces or as an abstraction of the notion of linear dependence. Matroid theory is an example of both a highly successful abstraction and a source of very useful and explicit examples. Matroid theory has various connections to the theory of algorithms and mathematical optimization, and also to mathematical logic. 

Each of the five notions we mentioned above, independent sets, bases, circuits, flats, and rank functions, give rise to an axiomatic definition of matroids (and all these axiomatic definitions are equivalent). The definition of matroids based on independent sets is given by the following properties: 

- (1) Subsets of independent sets are themselves independent. 

- (2) For every subset _𝑌_ of _𝑋_ , all maximal independent subsets of Y have the same cardinality. 

The first property means that the set of independent sets is an abstract simplicial complex while the second property asserts that for every subset _𝑌_ of the ground set _𝑋_ , the induced complex on _𝑌_ is pure. 

For an abstract simplicial complex _𝐾_ on a ground set _𝑋_ , we can define its dual (also called its blocker) by 

_𝐾_<sup>∗</sup> = { _𝑆_ ⊂ _𝑋_ : _𝑋_ \ _𝑆_ ⊄ _𝑀_ } _._ 

If _𝑀_ is a matroid we can define its dual as the matroid whose independent set complex is the dual of the independent set complex of _𝑀_ . 

## **2.2. From graphs to matroids** 

Let _𝐺_ be a (connected) graph on _𝑛_ vertices { _𝑣_ 1 _, 𝑣_ 2 _, . . . , 𝑣𝑛_ }, and suppose that _𝑒_ 1 _, 𝑒_ 2 _, . . . , 𝑒𝑛_ is the standard basis in an _𝑛_ -dimensional vector space over a field _𝐹_ . We associate to every edge _𝑒_ = { _𝑣𝑖, 𝑣 𝑗_ } _, 𝑖< 𝑗_ the vector _𝑒𝑖_ − _𝑒 𝑗_ . Remarkably we get the same matroid for every field we start with. This matroid is called the graphic matroid associated with _𝐺_ . It is easy to see that in this case, bases correspond to spanning trees, circuits correspond to simple cycles, independent sets correspond to spanning forests, and the rank function for subgraph _𝐻_ that corresponds to a set of edges is _𝑛_ minus the number of the connected components of _𝐻_ . 

**5 The Work of June Huh** 



**Figure 1** 

Important classes of matroids. Right: Matroids also provide an abstraction of the notion of algebraic dependence. The large and mysterious class of algebraic matroids consists of matroids that can be represented by algebraic dependence relations over some field. Left: Tutte characterized graphic matroids in terms of forbidden minors. Regular matroids are those matroids that can be represented over every field, and Paul Seymour **[58]** developed a structure theory for this class. Jim Geelen, Bert Gerards, and Geoff Whittle (see **[28]** ) have recently proved that matroids represented over every field are characterized by a finite list of forbidden minors. 

If _𝑀_ is a graphic matroid, the dual matroid need not be graphic. However, for planar graphs the dual matroid is the matroid associated to the dual graph. The notion of deletion and contraction extend from graph theory to matroid theory. (Indeed, these two operations are dual under matroid duality.) 

## **2.3. Rank functions, characteristic polynomials, and the Heron–Rota–Welsh conjecture** 

The rank function of a matroid associates a nonnegative integer _𝑟_ ( _𝑌_ ) to every subset _𝑌_ ⊂ _𝑋_ , with the following properties: 

(i) _𝑟_ (∅) = 0, 

(ii) _𝑟_ ( _𝐴_ ∪ _𝐵_ ) ≤ _𝑟_ ( _𝐴_ ) + _𝑟_ ( _𝐵_ ) − _𝑟_ ( _𝐴_ ∩ _𝐵_ ), 

(iii) _𝑟_ ( _𝐴_ ) ≤ _𝑟_ ( _𝐴_ ∪{ _𝑏_ }) ≤ _𝑟_ ( _𝐴_ ) + 1 _._ 

The characteristic function of a matroid _𝑀_ with ground set _𝑋_ is defined as follows: 



When _𝑀_ is a graphic matroid for the graph _𝐺_ , then _𝜒𝑀_ ( _𝜆_ ) is the chromatic polynomial of _𝐺_ . 

**Theorem 3** (Adiprasito, Huh, and Katz **[1]** ). _The coefficients of the characteristic polynomial of a matroid 𝑀 are log-concave._ 

**6 G. Kalai** 

June Huh **[33]** proved the results for matroids (regarded as hyperplane arrangements) representable over a field of characteristic 0 and, as we mentioned above, the proof uses the Milnor numbers of the arrangement. The proof by Huh and Katz **[36]** for the case of an arbitrary characteristic relied on the intersection theory of “wonderful compactification” defined by Corrado De Concini and Claudio Procesi **[21]** for complements of hyperplane arrangements combined with an inequality of Askold Khovanskii and Bernard Teissier. 

Adiprasito, Huh, and Katz **[1]** proved the full result. This requires far-reaching extensions of results from algebraic geometry to cohomology rings of algebraic varieties that do not exist. Here is the description of one of the early steps in the argument: the original definition of De Concini and Procesi of the “wonderful compactification” applied to realizable matroids, but Feichtner and Yuzvinsky defined in 2004 **[25]** a commutative ring associated to an arbitrary matroid that specializes to the cohomology ring of a wonderful compactification in the realizable case. 

Let me quote from **[1]** : “After the completion of **[36]** , it was gradually realized that the validity of the Hodge–Riemann relations for the Chow ring of _𝑀_ is a vital ingredient for the proof of the log-concavity conjectures. While the Chow ring of _𝑀_ could be defined for arbitrary [matroid] _𝑀_ , it was unclear how to formulate and prove the Hodge–Riemann relations. From the point of view of **[25]** , the ring _𝐴_<sup>∗</sup> ( _𝑀_ )R is the Chow ring of a smooth, but noncompact toric variety _𝑋_ (Σ _𝑀_ ), and there is no obvious way to reduce to the classical case of projective varieties.” 

We will discuss some of the algebraic geometry aspects in Section 4. We note that the algebraic results of **[1]** actually apply to more general geometric objects well beyond matroids. 

### **3. The Dowling–Wilson conjecture** 

## **3.1. Background: Theorems by de Bruĳn–Erdős, Motzkin, Greene, and Ryser’s linear algebraic proof** 

**Theorem 4.** _A set of 𝑛 points in the plane not all on the same line determines at least 𝑛 lines._ 

Here we say that a configuration of points determines a line _ℓ_ if the line contains two (distinct) points from the configuration. 

**Proof:** The Gallai–Sylvester theorem asserts that there exists a line that contains precisely two points of the configuration. The theorem now follows by induction when you delete one of these two points from the configuration. □ 

The assertion of the Gallai–Sylvester theorem does not apply over characteristic two as seen by the Fano plane, nor does it apply for the complex plane. By contrast, the proof by Nicolaas de Bruĳn and Paul Erdős uses an abstract combinatorial reasoning that is based only on the very first axiom of Euclid: “Every two points span a unique line”. An algebraic proof of the theorem was given by Herbert Ryser **[54]** . 

**Ryser’s proof:** Consider the 0-1 _incidence matrix_ with rows corresponding to points in the configuration and columns to lines determined by these points. Suppose that the 

**7 The Work of June Huh** 



**Figure 2** 

Important examples of matroids. From left to right: The Fano matroid, the Vámos matroid, and the non-Pappus matroid. The points of the Fano plane violate the Gallai–Sylvester theorem, hence it is not representable over the reals. As a matter of fact, the Fano matroid is representable over a field _𝐹_ if and only the characteristic of _𝐹_ is 2. The Vámos matroid is not algebraic. Pappus ancient theorem implies that the non-Pappus matroid is not representable over any field. Bernt Lindström proved that it is algebraic. Picture credit: Wikipedia and the “matroid union” blog. 

columns of the incidence matrix are _𝑐_ 1 _, 𝑐_ 2 _, . . . , 𝑐𝑚_ . Note that the inner product of every two distinct rows is one. Write _𝑏𝑖_ = _< 𝑐𝑖, 𝑐𝑖 >_ for the number of points on the _𝑖_ th line ( _𝑏𝑖 >_ 1). Suppose that 



We write 



It follows that the rows are linearly independent and therefore we must have _𝑚_ ≤ _𝑛_ . □ 

Ryser’s proof was a starting point for many algebraic proofs in combinatorics. We leave it as an exercise to show that it implies that there is bĳection _𝜓_ ( _𝑝_ ) from points to lines such that _𝑝_ ∈ _𝜓_ ( _𝑝_ ). 

Theodore Motzkin considered the theorem in higher dimensions. He conjectured (already in his 1936 thesis) that _𝑛_ points in a _𝑑_ dimensional space that affinely span the space span at least _𝑛_ hyperplanes. Motzkin himself proved the result as well as an extension of the Gallai-Sylvester theorem for configurations in higher-dimensional real vector spaces **[50]** . Curtis Greene **[30]** proved a stronger theorem: there is a one-to-one map _𝜓_ from every point _𝑝_ to a hyperplane containing _𝑝_ . 

Let us now move to matroids of rank _𝑑_ . (Note that affine dependence of points in a _𝑑_ -dimensional vector space describe a matroid of rank _𝑑_ + 1.) In 1974 Thomas Dowling and Richard Wilson conjectured that 



**8 G. Kalai** 

This conjecture is referred to as the _top-heavy conjecture_ . 

## **3.2. The proof of the Dowling–Wilson conjecture** 

**Theorem 5** (Braden, Huh, Matherne, Proudfoot, and Wang 2020 **[12]** ). _Let 𝑀 be a matroid, and let_ L<sup>_𝑘_</sup> ( _𝑀_ ) _denote the set of 𝑘-flats of 𝑀; then, for any 𝑘, 𝑗, 𝑘_ ≤ _𝑗_ ≤ _𝑟𝑎𝑛𝑘_ ( _𝑀_ ) − _𝑘,_ 

- (1) _The cardinality of_ L<sup>_𝑘_</sup> ( _𝑀_ ) _is at most the cardinality of_ L<sup>_𝑗_</sup> ( _𝑀_ ) 

- (2) _There is an injective map 𝜓 from_ L<sup>_𝑘_</sup> ( _𝑀_ ) _to_ L<sup>_𝑗_</sup> ( _𝑀_ ) _, satisfying 𝐹_ ⊂ _𝜓_ ( _𝐹_ ) 

An additional result from the same paper asserts that if Γ is any group acting on _𝑀_ , 

then 

- (3) There is an injective map _𝜓_ from QL<sup>_𝑘_</sup> ( _𝑀_ ) to L<sup>_𝑗_</sup> ( _𝑀_ ), of permutation representation of Γ. 

The case of representable matroids was proved earlier by Huh and Wang 2017 **[37]** . The paper **[12]** also gives consequences for Kazhdan–Lusztig polynomials of matroids (introduced by Elias and Proudfoot). 

We note that it is still an outstanding open question (even for representable matroids) that the sequence _𝑤_ 1 _, 𝑤_ 2 _, . . . , 𝑤𝑛_ is log-concave. It is not even known for rank-3 matroids that 



and this is referred to as the “point-lines-planes” conjecture. A stronger form of this conjecture (due to Mason) asserts that 



In 1982 Paul Seymour **[57]** proved this conjecture for matroids having no five points on a line. 

### **4. The connection with Hodge theory and algebraic geometry** 

## **4.1. Three fundamental ideas and other ingredients from the proof of the Heron–Rota–Welsh conjecture** 

_“I like the solution even more than the problem.”_ 

June Huh at a lecture at ICERM, 2015. 

In his 2015 lecture at ICERM (see also **[35]** ), June Huh explained three fundamental ideas that were used in the proof of the general Heron–Rota–Welsh conjecture. 

- (1) The idea of Bernd Sturmfels that a matroid can be viewed as a tropical linear space. 

**9 The Work of June Huh** 

Indeed, tropical geometry provided both a necessary framework and insights into the solution. Briefly, tropical mathematics replaces traditional addition with the operation of “taking the minimum,” and multiplication with ordinary addition. This idea arose in several areas of mathematics and in physics and it played an important role in enumerative algebraic geometry. (For more details, see **[35]** and Section 5.4 and appendix C of **[51]** .) 

- (2) The idea of Richard Stanley that a polarized Hodge structure on the cohomology of projective toric varieties produces important combinatorial inequalities. 

Here the main example was the _𝑔_ -theorem for convex polytopes where Stanley used the hard Lefschetz theorem for the cohomology ring. Another notable example was Stanley’s proof of the Erdős–Moser conjecture. 

- (3) The idea of Peter McMullen that the _𝑔_ -conjecture can be proved entirely within the realm of convex polytope theory using the “flip connectivity” of simplicial polytopes of a given dimension. 

Any two simplicial polytopes are connected by a sequence of “flips” (also known as “Pachner moves”) and McMullen proved that the validity of the hard Lefschetz theorem and the Hodge–Riemann relations are preserved under flips. 

In the same lecture, June Huh mentioned quite a few more ideas by many people working in algebraic combinatorics and in algebraic geometry that play a role in the proof. We already mentioned Tessier, Khovanskii, De Concini and Procesi, and Fleischer and Yuzvinsky, and Huh mentioned also Federico Ardila and Caroline Klivans ( **[6]** ), Angela Gibney and Diane Maclagan ( **[29]** ), Kalle Karu **[41]** , and William Fulton and Robert MacPherson **[26, 27]** . Of course, the proof involved a large number of additional original (at times crazy) ideas by Adiprasito, Huh, and Katz themselves. 

## **4.2. Poincaré duality, the hard Lefschetz theorem, and the Hodge–Riemann relations** 

Hodge theory gives rise to three conjectures (PD), (HL), and (HR), referred to as the standard conjectures, for certain algebras associated with geometric and combinatorial objects. 

- (PD) stands for the Poincaré duality, and it asserts that certain vector spaces _𝐴𝑖_ and _𝐴𝑑_ − _𝑖_ are dual (and thus have the same dimension). 

- (HD) stands for hard Lefschetz theorem and it asserts that certain linear maps _𝜙𝑘_ from _𝐴𝑘_ to _𝐴𝑘_ + 1 have the property that their composition from _𝐴𝑖_ all the way to _𝐴𝑑_ − _𝑖_ is an injection. 

- (HR) stands for the Hodge–Riemann relations. (PD) and (HD) imply that a certain bilinear form is nondegenerate and (HR) is a stronger statement that this form is definite. 

**10 G. Kalai** 

For the case of smooth projective algebraic variety _𝑀_ , we can consider its cohomology ring _𝐴𝑖_ = _𝐻_<sup>2</sup><sup>_𝑖_</sup> ( _𝑀_ ). (For the case of singular algebraic varieties, that come into play in the strongest versions of the Dowling–Wilson conjecture, we need to use intersection cohomology.) 

In **[34]** June Huh considered five examples (we are somewhat imprecise here): the cohomology of a compact Kähler manifold, the ring of algebraic cycles modulo homological equivalence on a smooth projective variety, McMullen’s algebra generated by the Minkowski summands of a simple convex polytope, the combinatorial intersection cohomology of a convex polytope, the reduced Soergel bimodule of a Coxeter group element, and the Chow ring of a matroid. The only case among these examples where the standard conjectures are not known is in their original appearance in Grothendieck’s work **[31]** toward the Weil conjectures. The example of Soergel bimodules is related to the celebrated 2014 solution of the Kazhdan– Lusztig conjecture for general Coxeter groups by Ben Elias and Geordie Williamson **[23]** . While it may be premature to expect it, it is not premature to hope that some connections will be found between the combinatorial appearances of the standard conjectures and their appearances in representation theory and number theory. 

**Remarks:** 1) The proof of the Heron–Rota–Welsh conjecture by June Huh and his collaborators largely exploits “positivity,” namely the Hodge–Riemann relations. For another central problem in algebraic combinatorics, the “g-conjecture for spheres,” positivity is no longer available, and remarkable techniques to replace it and thus prove the conjecture were recently developed first by Adiprasito **[2]** (the “Hall-Laman property”), subsequently by Stavros Argyrios Papadakis and Vasiliki Petrotou **[53]** (the “anisotropy property”), and ultimately by Adiprasito, Papadakis, and Petrotou **[3]** . (See also Kalle Karu and Elizabeth Xiao **[42]** for a simplified proof.) 

2) The work of Karu ( **[41]** ) on a hard Lefshetz theorem for general polytopes, of Elias and Williamson **[23]** on the Kazhdan–Lusztig conjecture, and of Braden, Huh, Matherne, Proudfoot, and Wang **[12]** on the Dowling–Wilson conjecture rely on (HL) and (HR), not for (combinatorial extensions of) the ordinary homology but for (combinatorial extensions of) Goresky and MacPherson’s intersection homology. 

### **5. The strong Mason conjecture (on independence numbers), and related developments and applications** 

## **5.1. Mason conjecture, regular strength, strong, and ultra-strong** 

Let _𝑀_ be an _𝑛_ -element matroid and let _𝑖𝑘_ ( _𝑀_ ) denote the number of independent sets of _𝑀_ of size _𝑘_ . The Mason conjecture **[45]** comes in several strengths. 

The Mason conjecture: 



**11 The Work of June Huh** 

The strong Mason conjecture: 



The ultra-strong Mason conjecture: 



Mathias Lenz showed **[43]** how to derive the Mason conjecture for representable matroids, based on the work of Huh and Katz. Adiprasito, Huh, and Katz showed how to derive the Mason conjecture from their Hodge theory techniques and Huh, Schröter, and Wang extended these techniques to prove the strong Mason conjecture. The ultra-strong conjecture was proved in parallel by direct combinatorial reasoning by Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant **[5]** and based on Hodge theory by Brändén and Huh **[13, 14]** . 

June Huh’s results of the past decade have led to much further research on the unimodality and log-concavity of various sequences arising in combinatorics. In some cases new combinatorial proofs were found. Let me refer the reader to recent papers by Swee Hong Chan and Igor Pak **[19, 20]** . 

## **5.2. The Mihail–Vazirani conjecture** 

For a matroid _𝑀_ on a ground set _𝑋_ , consider a graph whose vertices are all bases of the matroids and two bases are adjacent if their symmetric difference has two elements. Milena Mihail and Umesh Vazirani conjectured that for every set _𝑌_ of vertices in this graph, the number of edges between _𝑌_ to its complement _𝑌_<sup>¯</sup> is at least min(| _𝑌_ || _, 𝑌_<sup>¯</sup> |). 

If _𝑀_ consists of the elements of the standard basis in R<sup>_𝑑_</sup> and their negatives, then the graph we obtain is the graph of the discrete _𝑛_ -dimensional discrete cube and the assertion of the Mihail–Vazirani conjecture is a well-known isoperimetric inequality of the discrete cube. 

In a pioneering 1992 paper, Tomás Feder and Milena Mihail **[24]** proved the conjecture for balanced matroids. In 2018 Nima Anari, Shayan Oveis Gharan, and Cynthia Vinzant **[4]** proved the Mihail–Vazirani conjecture. Their proof relied on the Adiprasito–Huh–Katz paper although gradually they were able to find elementary proofs not depending on Hodge theory of crucial inequalities they needed. Their result leads to a polynomial-time algorithm to approximate the number of bases in a matroid. 

### **Conclusion** 

June Huh found striking connections between algebraic geometry and combinatorics, solved central problems in combinatorics that had remained open for decades, and developed a theory of great importance for both fields. In my review, I naturally concentrated on the combinatorial side of the story. I did not describe in this review the connection 

**12 G. Kalai** 

with tropical geometry, a major area both in algebraic combinatorics and algebraic geometry. The reader is also referred to Huh’s papers to learn about the theory of Lorentzian polynomials developed by June Huh and his coauthors. 

It is a great pleasure to congratulate June Huh for his spectacular achievements. 

### **Funding** 

Supported by ERC grant 834735 and by an ISF grant 2669/21. 

### **References** 

|**[1]**|Karim Adiprasito, June Huh, and Eric Katz, Hodge theory for combinatorial<br>geometries,_Annals of Mathematics_188 (2018), 381–452|
|---|---|
|**[2]**|Karim Adiprasito, Combinatorial Lefschetz theorems beyond positivity, arXiv:1812.10454.|
|**[3]**|Karim Adiprasito, Stavros Argyrios Papadakis, and Vasiliki Petrotou, Anisotropy,<br>biased pairings, and the Lefschetz property for pseudomanifolds and cycles,<br>arXiv:2101.07245.|
|**[4]**|Nima Anari, Shayan Oveis Gharan, and Cynthia Vinzant, Log-concave polyno-<br>mials, entropy, and a deterministic approximation algorithm for counting bases<br>of matroids,_Duke Mathematics Journal_170 (2021), 3459–3504. (Preliminary<br>version, FOCS 2018.)|
|**[5]**|Nima Anari, Shayan Oveis Gharan, Kuikui Liu, and Cynthia Vinzant, Log-<br>concave polynomials III: Mason’s ultra-log-concavity conjecture for independent<br>sets of matroids, 2018, arXiv:1811.01600.|
|**[6]**|Federico Ardila and Caroline Klivans, The Bergman complex of a matroid and<br>phylogenetic trees,_Journal of Combinatorial Theory Series B_96 (2006), 38–49|
|**[7]**|Federico Ardila, Graham Denham, and June Huh, Lagrangian geometry of<br>matroids,_Journal of the American Mathematical Society_, 2022.|
|**[8]**|Kenneth Appel and Wolfgang Haken, Every planar map is four-colorable,_Con-_<br>_temporary Mathematics_, vol. 98, with the collaboration of John Koch, Providence,<br>RI: American Mathematical Society, 1985.|
|**[9]**|Gottfried Barthel, Jean-Paul Brasselet, Karl-Heinz Fieseler, and Ludger Kaup,<br>Combinatorial duality and intersection product: A direct approach._Tohoku Mathe-_<br>_matics Journal_, 57 (2005), 273–292.|
|**[10]**|Louis J. Billera and Carl W. Lee, A proof of the sufficiency of McMullen’s con-<br>ditions for f -vectors of simplicial convex polytopes._Journal of Combinatorial_<br>_Theory Series A_, 31 (1981), 237–255.|
|**[11]**|Anders Björner, The unimodality conjecture for convex polytopes,_Bulletin of the_<br>_American Mathematical Society_4 (1981), 187–188.|
|**[12]**|Tom Braden, June Huh, Jacob P. Matherne, Nicholas Proudfoot, Botong Wang,<br>Singular Hodge theory for combinatorial geometries, arXiv:2010.06088.|
|**[13]**|Petter Brändén and June Huh, Hodge–Riemann relations for Potts model partition<br>functions, 2018, arXiv:1811.01696.|



**13 The Work of June Huh** 

|**[14]**<br>**[15]**|Petter Brändén and June Huh, Lorentzian polynomials, 2019, arXiv:1902.03719.<br>Francesco Brenti, Unimodal, log-concave and Pólya frequency sequences in Com-<br>binatorics,_Memoirs of the American Mathematical Society,_413, 1989.|
|---|---|
|**[16]**|Francesco Brenti, Log-concave and unimodal sequences in algebra, combina-<br>torics, and geometry: An update,_Jerusalem Combinatorics ’93_(Hélène Barcelo<br>and Gil Kalai (eds.)), 71–89,_Contemporary Mathematics_178, Providence, RI:<br>American Mathematical Society, 1994.|
|**[17]**|Paul Bressler and Valery A. Lunts, Hard Lefschetz theorem and Hodge–Riemann<br>relations for intersection cohomology of nonrational polytopes,_Indiana University_<br>_Mathematics Journal_54 (2005), 263–307.|
|**[18]**|George Birkhoff, A determinant formula for the number of ways of coloring a<br>map,_Annals of Mathematics_14 (1912), 42–46|
|**[19]**|Swee Hong Chan and Igor Pak, Log-concave poset inequalities, arXiv:2110.10740.|
|**[20]**|Swee Hong Chan and Igor Pak, Introduction to the combinatorial atlas,<br>arXiv:2203.01533.|
|**[21]**|Corrado De Concini and Claudio Procesi, Wonderful models of subspace arrange-<br>ments,_Selecta Mathematica_12 (1995), 459–494. 36–70.|
|**[22]**|Thomas Dowling and Richard Wilson, Whitney number inequalities for geometric<br>lattices._Proceedings of the American Mathematical Society_47 (1975), 504–512.|
|**[23]**|Ben Elias and Geordie Williamson, The Hodge theory of Soergel bimodules,<br>_Annals of Mathematics_180 (2014), 1089–1136.|
|**[24]**|Tomás Feder and Milena Mihail, Balanced matroids. In:_Proc. 24th Annual ACM_<br>_Symposium on Theory of Computing_, ACM Press, 26–38 (1992).|
|**[25]**|Eva Maria Feichtner and Sergey Yuzvinsky, Chow rings of toric varieties defined<br>by atomic lattices,_Inventiones Mathematicae_155 (2004), 515–536|
|**[26]**|William Fulton, Robert MacPherson, Frank Sottile, and Bernd Sturmfels, Inter-<br>section theory on spherical varieties,_Journal of Algebraic Geometry_4 (1995),<br>181–193.|
|**[27]**|William Fulton and Bernd Sturmfels, Intersection theory on toric varieties,<br>_Topology_36 (1997), 335–353.|
|**[28]**|Jim Geelen, Bert Gerards, and Geoff Whittle, Solving Rota’s conjecture,_Notices_<br>_of the American Mathematical Society_61 (2014), 736–743.|
|**[29]**|Angela Gibney and Diane Maclagan, Lower and upper bounds on nef cones,_Inter-_<br>_national Mathematics Research Notices_14 (2012), 3224–3255.|
|**[30]**|Curtis Greene, A rank inequality for finite geometric lattices._Journal Combinato-_<br>_rial Theory_9 (1970), 357–364.|
|**[31]**|Alexander Grothendieck, Standard conjectures on algebraic cycles, in_Algebraic_<br>_Geometry_, 193–199, Oxford University Press, 1969.|
|**[32]**|Andrew Heron, Matroid polynomials,_Combinatorics (Proceedings of the Con-_<br>_ference on Combinatorial Mathematics, Mathematics Institute)_, Oxford, 1972),<br>164–202.|



**14 G. Kalai** 

|**[33]**|June Huh, Milnor numbers of projective hypersurfaces and the chromatic polyno-<br>mial of graphs,_Journal of the American Mathematical Society_25 (2012), 907–<br>927.|
|---|---|
|**[34]**|June Huh, Combinatorial applications of the Hodge–Riemann relations, in_Pro-_<br>_ceedings of the International Congress of Mathematicians, Vol. IV. Invited lec-_<br>_tures_. World Scientific Publishers, Hackensack, NJ, (2018), 3093–3111.|
|**[35]**|June Huh, Tropical geometry of matroids,_Current Developments in Mathematics_<br>_2016_, 1–46, International Press (2018).|
|**[36]**|June Huh and Eric Katz, Log-concavity of characteristic polynomials and the<br>Bergman fan of matroids,_Mathematische Annalen_354 (2012), 1103–1116.|
|**[37]**|June Huh and Botong Wang, Enumeration of points, lines, planes, etc.,_Acta_<br>_Mathematica_218 (2017), 297–317.|
|**[38]**|June Huh, Benjamin Schröter, and Botong Wang, Correlation bounds for fields<br>and matroids,_Journal of the European Mathematical Society_24 (2022), 1335–<br>1351.|
|**[39]**|Jeff Kahn and Michael Neiman, Negative correlation and log-concavity,_Random_<br>_Structures and Algorithms_37 (2010), 367–388.|
|**[40]**|Yahya Ould Hamidoune and Isabelle Salaün, On the independence numbers of a<br>matroid,_Journal of Combinatorial Theory Series B_47 (1989), 146–152.|
|**[41]**|Kalle Karu, Hard Lefschetz theorem for nonrational polytopes,_Inventiones Math-_<br>_ematicae_, 157 (2004), 419–447.|
|**[42]**|Kalle Karu and Elizabeth Xiao, On the anisotropy theorem of Papadakis and<br>Petrotou, arXiv:2204.07758.|
|**[43]**|Matthias Lenz, The _𝑓_-vector of a representable-matroid complex is log-concave,<br>_Advances in Applied Mathematics_51 (2013), 543–545.|
|**[44]**|Laszlo Lovász, Matroid matching and some applications,_Journal of Combinato-_<br>_rial Theory (Ser. B)_28 (1980), 208–236.|
|**[45]**|John Mason, Matroids: unimodal conjectures and Motzkin’s theorem, In:_Combi-_<br>_natorics (Proceedings of the Conference on Combinatorial Mathematics, Mathe-_<br>_matics Institute, 1972)_, Oxford, 207–220.|
|**[46]**|Jiří Matoušek, The dawn of an algebraic era in discrete geometry? In_Proceedings_<br>_of the 27th European Workshop on Computational Geometry (EuroCG’11)_, 2011.|
|**[47]**|Peter McMullen, The numbers of faces of simplicial polytopes,_Israel Journal of_<br>_Mathematics_, 9 (1971), 559–570.|
|**[48]**|Peter McMullen, On simple polytopes,_Inventiones mathematicae_113 (1993),<br>419–444.|
|**[49]**|Peter McMullen, Weights on polytopes,_Discrete and Computational Geometry_15<br>(1996), 363–388.|
|**[50]**|Theodore Motzkin, The lines and planes connecting the points of a finite set,<br>_Transactions of the American Mathematical Society_70 (1951), 451–464.|
|**[51]**|Andrei Okounkov, Combinatorial geometry takes the lead. In_Proceedings of the_<br>_International Congress of Mathematicians_2022.|



**15 The Work of June Huh** 

|**[52]**|James Oxley,_Matroid theory_, Oxford Graduate Texts in Mathematics. Oxford<br>University Press, Oxford, 2011.|
|---|---|
|**[53]**|Stavros Argyrios Papadakis and Vasiliki Petrotou, The characteristic 2 anisotrop-<br>icity of simplicial spheres, arXiv:2012.09815.|
|**[54]**|Herbert J. Ryser, An extension of a theorem of de Bruĳn and Erdős on combinato-<br>rial designs,_Journal of Algebra_10 (1968), 246–261.|
|**[55]**|Ronald Read, An introduction to chromatic polynomials,_Journal of Combinato-_<br>_rial Theory_4 (1968), 52–71.|
|**[56]**|Gian-Carlo Rota, Combinatorial theory, old and new, in_Actes du Congress Inter-_<br>_national des Mathématicians_(Nice ,1970), Tome 3, Gauthier-Villars, Paris, 1971,<br>pp. 229–233.|
|**[57]**|Paul D. Seymour, On the points-lines-planes conjecture,_Journal of Combinatorial_<br>_Theory Series B_33 (1982), 17–26.|
|**[58]**|Paul D. Seymour, Decomposition of regular matroids,_Journal of Combinatorial_<br>_Theory, Series B_28 (1980), 305–359.|
|**[59]**|Richard P. Stanley, Acyclic orientations of graphs,_Discrete Mathematics_5 (1973),<br>171–178.|
|**[60]**|Richard P. Stanley, The number of faces of a simplicial convex polytope,_Advances_<br>_in Mathematics_35 (1980), 236–238.|
|**[61]**|Richard P. Stanley, Combinatorial applications of the hard Lefschetz theorem, in<br>_Proceedings of the International Congress of Mathematicians_, Vols. 1, 2 (Warsaw,<br>1983), PWN, Warsaw, 1984, pp. 447–453.|
|**[62]**|R. Stanley, Log-concave and unimodal sequences in algebra, combinatorics, and<br>geometry, in_Graph Theory and its Applications: East and West_(Jinan, 1986),<br>500–535, New York (1989).|
|**[63]**|Dennis Stanton, Unimodality and Young’s lattice._Journal of Combinatorial_<br>_theory Series A_54 (1990), 41–53.|
|**[64]**|Dominic Welsh, Combinatorial problems in matroid theory, In_Combinatorial_<br>_Mathematics and its Applications_(Oxford, 1969) pp. 291–306, Academic Press,<br>London, 1971.|
|**[65]**|Dominic Welsh,_Matroid Theory_, London Mathematical Society Monographs 8,<br>Academic Press, London, 1976.|
|**[66]**|Hassler Whitney, On the abstract properties of linear dependence,_American_<br>_Journal of Mathematics_57 (1935), 509–533.|



### **Gil Kalai** 

Hebrew University of Jerusalem and Reichman University, kalai@math.huji.ac.il 

**16 G. Kalai** 

