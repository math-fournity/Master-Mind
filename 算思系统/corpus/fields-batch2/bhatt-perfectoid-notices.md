# <u>I S . . .</u> ~~?~~<sup><u>WHAT</u></sup> a Perfectoid Space? 

_Bhargav Bhatt_ 

Perfectoid spaces are a class of algebro-geometric objects living in the realm of _p_ -adic geometry that were introduced by Peter Scholze [Sch12] in his Ph.D. thesis. Their definition is heavily inspired by a classical result in Galois theory (see Theorem 1) due to Fontaine and Wintenberger, and the resulting theory has already had stunning applications. 

## Motivation 

Fix a prime number _p_ , and consider the field _L_ 0 : _=_ Q _p_ of _p_ -adic numbers, as well as the field _L_ 0<sup>_♭_:</sup><sup>_=_</sup> F _p((t))_ of Laurent series over F _p_ . These fields are formally quite similar: one can represent elements in _L_ 0 as Laurent series in _p_ with integer coefficients, and a similar description applies to _L_<sup>_♭_</sup> 0<sup>with</sup><sup>_t_</sup> replacing _p_ . Of course there is no isomorphism _L_ 0 _≃ L_<sup>_♭_</sup> 0<sup>offieldsrealizingthissimilarity:</sup><sup>_L_0has</sup> characteristic 0, while _L_<sup>_♭_</sup> 0<sup>has characteristic</sup><sup>_p >_0.</sup> Nevertheless, it is a fundamental insight of [FW79] that a robust relationship between the two _does_ exist, at least after replacing _L_ 0 with the larger field _L_ : _=_ Q _p[p p_ <u>1</u><sup>_~~∞~~_</sup> _]_ : _= ∪n_ Q _p(p p_ <u>1</u><sup>_<u>n</u>_</sup> _)_ , and _L_<sup>_♭_</sup> 0<sup>withits</sup> <u>1</u> perfection _L_<sup>_♭_</sup> : _= ∪n_ F _p((t p_<sup>_<u>n</u>_</sup> _))_ . 

Theorem 1 (FW79). _The (absolute) Galois groups of L and L_<sup>_♭_</sup> _are canonically isomorphic._ 

Theorem 1 gives a correspondence between finite field extensions of _L_ and _L_<sup>_♭_</sup> which, heuristically, is established by replacing _p_ with _t_ . For example, the splitting field of _X_<sup>2</sup> _− t_ over _L_<sup>_♭_</sup> corresponds to the splitting field of _X_<sup>2</sup> _− p_ over _L_ . This mechanism 

_Bhargav Bhatt is an associate professor of mathematics at the University of Michigan. His email address is_ `bhattb@umich.edu` _._ 

DOI: http://dx.doi.org/10.1090/noti1166 

can be somewhat demystified by noticing that the <u>1 1</u> “integral” subrings Z _p[p p_<sup>_~~∞~~_</sup> _] ⊂ L_ and F _p[t p_<sup>_~~∞~~_</sup> _] ⊂ L_<sup>_♭_</sup> are related by an isomorphism of rings 



<u>1 1</u> that carries _p p_<sup>_<u>n</u>_</sup> to _t p_<sup>_<u>n</u>_</sup> . Besides its intrinsic beauty, this correspondence allows us to transport Galoistheoretic information between _L_ and _L_<sup>_♭_</sup> . 

Example 1. Certain invariants are very easy to compute for _L_<sup>_♭_</sup> on account of the Frobenius automorphism; Theorem 1 can sometimes help transfer this computation to _L_ . For example, using this strategy, one deduces that the F _p_ -cohomological dimension of the absolute Galois group of _L_ is _≤_ 1 because the corresponding assertion for _L_<sup>_♭_</sup> is classical (Hilbert). 

Recall that fields are zero-dimensional varieties from an algebro-geometric perspective. The goal of the theory of perfectoid spaces is to extend Theorem 1 to higher dimensions, i.e., to relate (certain) algebras over _L_ and _L_<sup>_♭_</sup> in a relatively lossless manner. 

## Perfectoid Spaces 

Fix _L_ and _L_<sup>_♭_</sup> as in the previous section. To introduce perfectoid spaces over these fields, it will be useful to recall some additional structures on _L_ and _L_<sup>_♭_</sup> . Specifically, note that both _L_ and _L_<sup>_♭_</sup> are equipped with natural norms given by the _p_ -adic and _t_ -adic metrics respectively. As our subsequent constructions involve various limiting operations (such as the extraction of arbitrary _p_ -power roots), it is convenient to cast all constructions in a slightly more analytic framework. We will thus pass from _L_ to its _p_ -adic completion _K_ , and _L_<sup>_♭_</sup> to its _t_ -adic 

1082 

Notices of the AMS 

Volume 61, Number 9 

completion _K_<sup>_♭_</sup> ; the analogue of Theorem 1 holds for _K_ and _K_<sup>_♭_</sup> as completions do not change Galois groups. The basic definition is: 

Definition 1. A _perfectoid K-algebra A_ is a Banach _K_ -algebra such that the subring _A_<sup>_◦_</sup> of powerbounded elements is open and bounded, and the Frobenius endomorphism is surjective on _A_<sup>_◦_</sup> _/p_ ; one similarly defines _perfectoid K_<sup>_♭_</sup> _-algebras_ . 

To unravel this definition, let us study some examples. The simplest example of such an algebra is _K_ itself. Indeed, the norm on _K_ endows _K_ with a Banach algebra structure. The subring _K_<sup>_◦_</sup> is 

� <u>1</u> the _p_ -adic completion Z _p[p p_<sup>_~~∞~~_</sup> _]_ and is thus open and bounded in the ( _p_ -adic) topology on _K_ ; the Frobenius on _K_<sup>_◦_</sup> _/p_ is surjective by construction. This example corresponds to a “point” in the world of perfectoid _K_ -spaces. The next simplest example is that of a “line”: 

Example 2. Consider the _p_ -adically complete _K_<sup>_◦_</sup> - � <u>1</u> algebra _A_<sup>_′_</sup> : _= K_<sup>_◦_</sup> _[X p_<sup>_~~∞~~_</sup> _]_ , and let _A_ : _= A_<sup>_′_</sup> _[ p_<sup>1</sup><sup>_]_.Then</sup> one can endow _A_ with a natural Banach _K_ -algebra structure such that _A_<sup>_◦_</sup> _= A_<sup>_′_</sup> is open and bounded. Moreover, as we have already extracted arbitrary _p_ -power roots of _X_ , the Frobenius on _A_<sup>_◦_</sup> _/p_ is surjective, so _A_ is a perfectoid _K_ -algebra; this algebra <u>1 1</u> is often denoted _K⟨X p_<sup>_~~∞~~_</sup> _⟩_ . Similarly, _A_<sup>_♭_</sup> : _= K_<sup>_♭_</sup> _⟨X p_<sup>_~~∞~~_</sup> _⟩_ is a perfectoid _K_<sup>_♭_</sup> -algebra. 

It is also easy to build examples in characteristic 

_p_ : 

Example 3. Let _A_ 0 be any _K_<sup>_♭,◦_</sup> algebra. Extracting _p_ -power roots of all elements in _A_ (i.e., passing to the perfection) gives a new _K_<sup>_♭,◦_</sup> -algebra _A_ 0 _,_ perf. This leads to the _K_<sup>_♭_</sup> -algebra _A_ : _= A_<sup>�</sup> 0 _,_ perf _[_<sup>1</sup> _t_<sup>_]_by inverting</sup> _t_ in the _t_ -adic completion. One may endow _A_ with a natural Banach _K_<sup>_♭_</sup> -algebra structure to make it perfectoid. For example, applying this procedure to _A_ 0 : _= K_<sup>_♭,◦_</sup> _[X]_ produces _A_<sup>_♭_</sup> from Example 2. 

Recall from algebraic geometry that affine varieties are completely described by their rings of functions, while varieties are built by glueing affine varieties together. The situation with perfectoid _K_ - spaces is analogous: the “affine” objects correspond to perfectoid _K_ -algebras, while perfectoid _K_ -spaces are built by glueing these “affine” objects together. Actually, to retain the analytic flavor of Definition 1, this glueing is carried out in the world of rigid analytic geometry (incarnated through Huber’s adic spaces [Hub96]). We will ignore this technical, but absolutely crucial, point here, and assume that the notion of a perfectoid _K_ -space, built by glueing together “spectra” of perfectoid _K_ -algebras, has been defined. The main theorem concerning these objects is: 

Theorem 2 (Sch12, Theorems 1.9 and 1.11). _The categories of perfectoid K-spaces and perfectoid K_<sup>_♭_</sup> _- spaces are canonically identified; this identification preserves the étale topology._ 

To describe this equivalence, observe that (1) gives a formula describing _K_<sup>_♭_</sup> in terms of _K_ : 



where the limit is along the Frobenius maps on _K_<sup>_◦_</sup> _/p_ , and _t ∈_ lim _K_<sup>_◦_</sup> _/p_ is the _p_ -power compatible <u>1</u> system _(p p_<sup>_<u>n</u>_</sup> _)_ . The identification in Theorem 2 is given by exactly the same formula (for affines): one sends a perfectoid _K_ -algebra _A_ to the perfectoid _K_<sup>_♭_</sup> -algebra 



The association _A_ � _A_<sup>_♭_</sup> is called _tilting_ , while the inverse is called _untilting_ ; the nomenclature suggests viewing these operations as carrying us between the two ends of the following picture, resulting from (2): 



We have already encountered some examples of tilting earlier in this note: 

Example 4. The field _K_<sup>_♭_</sup> is the tilt of _K_ , as explained above, which clarifies the notation. Similarly, in Example 2, the ring _A_<sup>_♭_</sup> is the tilt of _A_ . 

A more “global” example of tilting is given by: 

Example 5. Fix an integer _n_ . Globalizing Example 3 leads to a perfectoid _K_<sup>_♭_</sup> -space P _K_<sup>_n♭_</sup> _,_ perf<sup>obtained</sup> as the perfection of projective space P _K_<sup>_n♭_over</sup><sup>_K♭_.</sup> Its untilt is (roughly) given by P _K,_<sup>_n_</sup> perf<sup>:</sup><sup>_=_lim P</sup> _K_<sup>_n_,</sup> where the transition maps raise all homogeneous coordinates to the _p_ -th power. 

The preservation of the étale topology under tilting is a deep result: it is a simultaneous generalization of Theorem 1 and of Faltings’s “almost purity theorem,” the key ingredient of his fundamental work in _p_ -adic Hodge theory, which began in [Fal88] and allowed him to prove various conjectures of Fontaine. 

Theorem 2 leads to the following picture summarizing the relationship of perfectoid spaces to 

October 2014 

Notices of the AMS 

1083 

classical algebraic geometry: 



Here the horizontal arrows come from Theorem 2, and the right vertical arrow is the globalization of Example 3. The mysterious dotted arrow Ψ is, in fact, nonexistent: there is no natural way to attach a perfectoid _K_ -space to an algebraic _K_ -variety. This apparent asymmetry can be explained by noticing that there is a _canonical_ procedure for extracting all _p_ -th roots in characteristic _p_ (namely, taking the perfection), while there is no analogous construction in characteristic 0. Instead, given an algebraic _K_ -variety _X_ , each time one can _somehow_ construct a related perfectoid _K_ -space Ψ _(X)_ , one learns a wealth of new information about _X_ . We discuss some examples of this phenomenon in the section entitled “Examples and Applications.” 

_Remark_ 1 _._ In [Sch12], one finds a slightly more general version of the theory sketched here: the field _K_ above is simply an example of a _perfectoid field_ . For any such _K_ , there is a tilt _K_<sup>_♭_</sup> in characteristic _p_ , and an analogous theory of perfectoid spaces over these fields (including, in particular, Theorem 2). An important example is _K =_ C _p_ (the completed algebraic closure of Q _p_ ) whose tilt _K_<sup>_♭_</sup> is the completed algebraic closure of F _p((t))_ . 

## Examples and Applications 

The theory of perfectoid spaces is rather young, but already extremely potent: each class of examples discovered so far has led to powerful and deep theorems in arithmetic geometry. We give a summary of some such examples next, with notation as in the previous section. 

_•_ Given a hypersurface _H ⊂_ P _K_<sup>_n_,onecancon-</sup> struct a perfectoid space _Uϵ_ which, essentially, is the tubular neighborhood of radius _ϵ_ around the inverse image of _H_ under P _K,_<sup>_n_</sup> perf<sup>_→_P</sup> _K_<sup>_n_,following</sup> the notation in Example 5. Using _Uϵ_ and Theorem 2, Scholze proved Deligne’s weight-monodromy conjecture for smooth _H_ in [Sch12] by reducing it to the analogous statement for a smooth hypersurface _H_<sup>_′_</sup> over the characteristic _p_ field _K_<sup>_♭_</sup> (as the latter was proven by Deligne en route to the Weil conjectures). 

torsion in the cohomology of locally symmetric varieties”), Scholze showed that _Ag(p_<sup>_∞_</sup> _)_ is a wellbehaved object: it is naturally a perfectoid _K_ -space. In fact, he deduced a similar statement for any Shimura variety (of Hodge type) with full level structure at _p_ . Using these spaces, he proved the following two results, which outwardly have nothing to do with perfectoid spaces (or even local fields): (a) a cohomological vanishing conjecture of Calegari and Emerton for Shimura varieties over C is true (much in the spirit of Example 1), and (b) one can attach Galois representations to _torsion_ classes in the cohomology of locally symmetric spaces, which builds on recent work of Harris-LanTaylor-Thorne, and represents a significant step forward in the Langlands program. 

_•_ We end by touching on a theme that was largely skirted in the previous section. Namely, as perfectoid spaces live in the world of analytic geometry, they actually help study classical rigidanalytic spaces, not merely algebraic varieties (as in the previous two examples). In his “ _p_ -adic Hodge theory for rigid-analytic varieties” paper, Scholze pursues this idea to extend the foundational results in _p_ -adic Hodge theory, such as Faltings’s work mentioned above, to the setting of rigidanalytic spaces over Q _p_ ; such an extension was conjectured many decades ago by Tate in his epochmaking paper “ _p_ -divisible groups.” The essential ingredient of Scholze’s approach is the remarkable observation that _every_ classical rigid-analytic space over Q _p_ is locally perfectoid, in a suitable sense. 

The power of perfectoid spaces is only beginning to be exploited, and more applications will surely arise! 

## References 

- [Fal88] Gerd Faltings, _p_ -adic Hodge theory, _J. Amer. Math. Soc._ 1(1) (1988), 255–299. 

- [FW79] Jean-Marc Fontaine and Jean-Pierre Wintenberger, Extensions algébrique et corps des normes des extensions APF des corps locaux, _C. R. Acad. Sci. Paris Sér. A–B_ 288(8) (1979), A441–A444. 

- [Hub96] Roland Huber, Étale cohomology of rigid analytic varieties and adic spaces, _Aspects of Mathematics_ , E30, Friedr. Vieweg & Sohn, Braunschweig, 1996. 

- [Sch12] Peter Scholze, Perfectoid spaces, _Publ. Math. Inst. Hautes Études Sci._ 116 (2012), 245–313. 

_•_ Given a positive integer _g_ , one may consider the moduli space _Ag(p_<sup>_∞_</sup> _)_ parameterizing abelian varieties _A_ over _K_ equipped with a trivialization _φ_ : Z<sup>_⊕_</sup> _p_<sup>2</sup><sup>_g_</sup> _≃ Tp(A)_ of their _p_ -adic Tate modules. This space is rather large and pathological from the viewpoint of classical algebraic geometry. Nevertheless, in a recent preprint (titled “On 

1084 

Notices of the AMS 

Volume 61, Number 9 

