# **PERFECTOID SPACES** 

## PETER SCHOLZE 

Abstract. We introduce a certain class of so-called perfectoid rings and spaces, which give a natural framework for Faltings’ almost purity theorem, and for which there is a natural tilting operation which exchanges characteristic 0 and characteristic _p_ . We deduce the weight-monodromy conjecture in certain cases by reduction to equal characteristic. 

# Contents 

|1.|Introduction|2|
|---|---|---|
|2.|Adic spaces|7|
|3.|Perfectoid fields|15|
|4.|Almost mathematics|18|
|5.|Perfectoid algebras|21|
|6.|Perfectoid spaces: Analytic topology|30|
|7.|Perfectoid spaces: Etale topology|39|
|8.|An example: Toric varieties|44|
|9.|The weight-monodromy conjecture|47|
|Ref|erences|50|



_Date_ : November 27, 2024. 

1 

PETER SCHOLZE 

2 

# 1. Introduction 

In commutative algebra and algebraic geometry, some of the most subtle problems arise in the context of mixed characteristic, i.e. over local fields such as Q _p_ which are of characteristic 0, but whose residue field F _p_ is of characteristic _p_ . The aim of this paper is to establish a general framework for reducing certain problems about mixed characteristic rings to problems about rings in characteristic _p_ . We will use this framework to establish a generalization of Faltings’s almost purity theorem, and new results on Deligne’s weight-monodromy conjecture. 

The basic result which we want to put into a larger context is the following canonical isomorphism of Galois groups, due to Fontaine and Wintenberger, [13]. A special case is the following result. 

**Theorem 1.1.** _The absolute Galois groups of_ Q _p_ ( _p_<sup>1</sup><sup>_/p∞_</sup> ) _and_ F _p_ (( _t_ )) _are canonically isomorphic._ 

In other words, after adjoining all _p_ -power roots of _p_ to a mixed characteristic field, it looks like an equal characteristic ring in some way. Let us first explain how one can prove this theorem. Let _K_ be the completion of Q _p_ ( _p_<sup>1</sup><sup>_/p∞_</sup> ) and let _K_<sup>_♭_</sup> be the completion of F _p_ (( _t_ ))( _t_<sup>1</sup><sup>_/p∞_</sup> ); it is enough to prove that the absolute Galois groups of _K_ and _K_<sup>_♭_</sup> are isomorphic. Let us first explain the relation between _K_ and _K_<sup>_♭_</sup> , which in vague terms consists in replacing the prime number _p_ by a formal variable _t_ . Let _K_<sup>_◦_</sup> and _K_<sup>_♭◦_</sup> be the subrings of integral elements. Then 



where the middle isomorphism sends _p_<sup>1</sup><sup>_/pn_</sup> to _t_<sup>1</sup><sup>_/pn_</sup> . Using it, one can define a continuous multiplicative, but nonadditive, map _K_<sup>_♭_</sup> _→ K_ , _x �→ x_<sup>_♯_</sup> , which sends _t_ to _p_ . On _K_<sup>_♭◦_</sup> , it is given by sending _x_ to lim _n→∞ yn_<sup>_pn_,where</sup><sup>_y_</sup> _n_<sup>_∈K◦_isanyliftoftheimageof</sup><sup>_x_1</sup><sup>_/pn_in</sup> _K_<sup>_♭◦_</sup> _/t_ = _K_<sup>_◦_</sup> _/p_ . Then one has an identification 



In order to prove the theorem, one has to construct a canonical finite extension _L_<sup>_♯_</sup> of _K_ for any finite extension _L_ of _K_<sup>_♭_</sup> . There is the following description. Say _L_ is the splitting field of a polynomial _X_<sup>_d_</sup> + _ad−_ 1 _X_<sup>_d−_1</sup> + _. . ._ + _a_ 0, which is also the splitting field of _X_<sup>_d_</sup> + _ad_<sup>1</sup><sup>_/p_</sup> _−_ 1<sup>_nXd−_1 +</sup><sup>_. . ._+</sup><sup>_a_</sup> 0<sup>1</sup><sup>_/pn_</sup> for all _n ≥_ 0. Then _L_<sup>_♯_</sup> can be defined as the splitting field of _X_<sup>_d_</sup> + ( _ad_<sup>1</sup><sup>_/p_</sup> _−_ 1<sup>_n_)</sup><sup>_♯Xd−_1 +</sup><sup>_. . ._+ (</sup><sup>_a_1</sup> 0<sup>_/pn_</sup> )<sup>_♯_</sup> for _n_ large enough: these fields stabilize as _n →∞_ . 

In fact, the same ideas work in greater generality. 

**Definition 1.2.** _A perfectoid field is a complete topological field K whose topology is induced by a nondiscrete valuation of rank_ 1 _, such that the Frobenius_ Φ _is surjective on K_<sup>_◦_</sup> _/p._ 

Here _K_<sup>_◦_</sup> _⊂ K_ denotes the set of powerbounded elements. Generalizing the example above, a construction of Fontaine associates to any perfectoid field _K_ another perfectoid field _K_<sup>_♭_</sup> of characteristic _p_ , whose underlying multiplicative monoid can be described as 



The theorem above generalizes to the following result. 

**Theorem 1.3.** _The absolute Galois groups of K and K_<sup>_♭_</sup> _are canonically isomorphic._ 

Our aim is to generalize this to a comparison of geometric objects over _K_ with geometric objects over _K_<sup>_♭_</sup> . The basic claim is the following. 

PERFECTOID SPACES 

3 

**Claim 1.4.** _The affine line_ A<sup>1</sup> _K_<sup>_♭‘isequalto’theinverselimit_lim</sup> _←−T �→T_<sup>_p_A</sup> _K_<sup>1</sup><sup>_,whereTis_</sup> _the coordinate on_ A<sup>1</sup> _._ 

One way in which this is correct is the observation that it is true on _K_<sup>_♭_</sup> -, resp. _K_ -, valued points. Moreover, for any finite extension _L_ of _K_ corresponding to an extension _L_<sup>_♭_</sup> of _K_<sup>_♭_</sup> , we have the same relation 



Looking at the example above, we see that the explicit description of the map between A<sup>1</sup> _K_<sup>_♭_and lim</sup> _←−T �→T_<sup>_p_A</sup> _K_<sup>1involves a limit procedure.For this reason, a formalization of this</sup> isomorphism has to be of an analytic nature, and we have to use some kind of rigidanalytic geometry over _K_ . We choose to work with Huber’s language of adic spaces, which reinterprets rigid-analytic varieties as certain locally ringed topological spaces. In particular, any variety _X_ over _K_ has an associated adic space _X_<sup>ad</sup> over _K_ , which in turn has an underlying topological space _|X_<sup>ad</sup> _|_ . 

**Theorem 1.5.** _There is a homeomorphism of topological spaces_ 



Note that both sides of this isomorphism can be regarded as locally ringed topological spaces. It is natural to ask whether one can compare the structure sheaves on both sides. There is the obvious obstacle that the left-hand side has a sheaf of characteristic _p_ rings, whereas the right-hand side has a sheaf of characteristic 0 rings. Fontaine’s functors make it possible to translate between the two worlds. There is the following result. 

**Definition 1.6.** _Let K be a perfectoid field. A perfectoid K-algebra is a Banach K- algebra R such that the set of powerbounded elements R_<sup>_◦_</sup> _⊂ R is bounded, and such that the Frobenius_ Φ _is surjective on R_<sup>_◦_</sup> _/p._ 

**Theorem 1.7.** _There is natural equivalence of categories, called the tilting equivalence, between the category of perfectoid K-algebras and the category of perfectoid K_<sup>_♭_</sup> _-algebras. Here a perfectoid K-algebra R is sent to the perfectoid K_<sup>_♭_</sup> _-algebra_ 



We note in particular that for perfectoid _K_ -algebras _R_ , we still have a map _R_<sup>_♭_</sup> _→ R_ , _f �→ f_<sup>_♯_</sup> . An example of a perfectoid _K_ -algebra is the algebra _R_ = _K⟨T_<sup>1</sup><sup>_/p∞_</sup> _⟩_ for which _R_<sup>_◦_</sup> = _K_<sup>_◦_</sup> _⟨T_<sup>1</sup><sup>_/p∞_</sup> _⟩_ is the _p_ -adic completion of _K_ [ _T_<sup>1</sup><sup>_/p∞_</sup> ]. This is the completion of an algebra that appears on the right-hand side of Theorem 1.5. Its tilt is given by _R_<sup>_♭_</sup> = _K_<sup>_♭_</sup> _⟨T_<sup>1</sup><sup>_/p∞_</sup> _⟩_ , which is the completed perfection of an algebra that appears on the left-hand side of Theorem 1.5. Now an affinoid perfectoid space is associated to a perfectoid affinoid _K_ -algebra, which is a pair ( _R, R_<sup>+</sup> ), where _R_ is a perfectoid _K_ -algebra, and _R_<sup>+</sup> _⊂ R_<sup>_◦_</sup> is open and integrally closed (and often _R_<sup>+</sup> = _R_<sup>_◦_</sup> ). There is a natural way to form the tilt ( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ). To such a pair ( _R, R_<sup>+</sup> ), Huber, [18], associates a space _X_ = Spa( _R, R_<sup>+</sup> ) of equivalence classes of continuous valuations _R →_ Γ _∪{_ 0 _}_ , _f �→|f_ ( _x_ ) _|_ , which are _≤_ 1 on _R_<sup>+</sup> . The topology on this space is generated by so-called rational subsets. Moreover, Huber defines presheaves _OX_ and _OX_<sup>+on</sup><sup>_X_,whoseglobalsectionsare</sup><sup>_R_,resp.</sup><sup>_R_+.</sup> 

**Theorem 1.8.** _Let_ ( _R, R_<sup>+</sup> ) _be a perfectoid affinoid K-algebra, and let X_ = Spa( _R, R_<sup>+</sup> ) _, X_<sup>_♭_</sup> = Spa( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _._ 

(i) _There is a homeomorphism X_<sup>_∼_</sup> = _X_<sup>_♭_</sup> _, given by mapping x ∈ X to the valuation x_<sup>_♭_</sup> _∈ X_<sup>_♭_</sup> _defined by |f_ ( _x_<sup>_♭_</sup> ) _|_ = _|f_<sup>_♯_</sup> ( _x_ ) _|. This homeomorphism identifies rational subsets._ 

PETER SCHOLZE 

4 

(ii) _For any rational subset U ⊂ X with tilt U_<sup>_♭_</sup> _⊂ X_<sup>_♭_</sup> _, the pair_ ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))</sup><sup>_isa_</sup> _perfectoid affinoid K-algebra with tilt_ ( _OX ♭_ ( _U_<sup>_♭_</sup> ) _, OX_<sup>+</sup><sup>_♭_(</sup><sup>_U♭_))</sup><sup>_._</sup> 

(iii) _The presheaves OX , OX_<sup>+</sup><sup>_aresheaves._</sup> 

(iv) _The cohomology group H_<sup>_i_</sup> ( _X, OX_<sup>+)</sup><sup>_is_m</sup><sup>_-torsionfori >_0</sup><sup>_._</sup> 

Here m _⊂ K_<sup>_◦_</sup> is the subset of topologically nilpotent elements. Part (iv) implies that _H_<sup>_i_</sup> ( _X, OX_ ) = 0 for _i >_ 0, which gives Tate’s acyclicity theorem in the context of perfectoid spaces. However, it says that this statement about the generic fibre extends _almost_ to the integral level, in the language of Faltings’s so-called almost mathematics. In fact, this is a general property of perfectoid objects: Many statements that are true on the generic fibre are automatically almost true on the integral level. 

Using the theorem, one can define general perfectoid spaces by gluing affinoid perfectoid spaces _X_ = Spa( _R, R_<sup>+</sup> ). We arrive at the following theorem. 

**Theorem 1.9.** _The category of perfectoid spaces over K and the category of perfectoid spaces over K_<sup>_♭_</sup> _are equivalent._ 

We denote the tilting functor by _X �→ X_<sup>_♭_</sup> . Our next aim is to define an ´etale topos of perfectoid spaces. This necessitates a generalization of Faltings’s almost purity theorem, cf. [11], [12]. 

**Theorem 1.10.** _Let R be a perfectoid K-algebra. Let S/R be finite ´etale. Then S is a perfectoid K-algebra, and S_<sup>_◦_</sup> _is almost finite ´etale over R_<sup>_◦_</sup> _._ 

In fact, as for perfectoid fields, it is easy to construct a fully faithful functor from the category of finite ´etale _R_<sup>_♭_</sup> -algebras to finite ´etale _R_ -algebras, and the problem becomes to show that this functor is essentially surjective. But locally on _X_ = Spa( _R, R_<sup>+</sup> ), the functor is essentially surjective by the result for perfectoid fields; one deduces the general case by a gluing argument. 

Using this theorem, one proves the following theorem. Here, _X_ ´et denotes the ´etale site of a perfectoid space _X_ , and we denote by _X_ ´et<sup>_∼_theassociatedtopos.</sup> 

**Theorem 1.11.** _Let X be a perfectoid space over K with tilt X_<sup>_♭_</sup> _over K_<sup>_♭_</sup> _. Then tilting induces an equivalence of sites X_ ´et<sup>_∼_</sup> = _X_ ´et<sup>_♭._</sup> 

As a concrete application of this theorem, we have the following result. Here, we use the ´etale topoi of adic spaces, which are the same as the ´etale topoi of the corresponding rigid-analytic variety. In particular, the same theorem holds for rigid-analytic varieties. 

**Theorem 1.12.** _The ´etale topos_ (P<sup>_n,_</sup> _K_<sup>ad</sup><sup>_♭_)</sup> ´et<sup>_∼is equivalent to the inverse limit_lim</sup> _←−ϕ_<sup>(P</sup> _K_<sup>_n,_ad</sup> )´et<sup>_∼._</sup> Here, one has to interpret the latter as the inverse limit of a fibred topos in an obvious way, and _ϕ_ is the map given on coordinates by _ϕ_ ( _x_ 0 : _. . ._ : _xn_ ) = ( _x_<sup>_p_</sup> 0<sup>:</sup><sup>_. . ._:</sup><sup>_x_</sup> _n_<sup>_p_).The</sup> same theorem stays true for proper toric varieties without change. We note that the theorem gives rise to a projection map 



defined on topological spaces and ´etale topoi of adic spaces, and which is given on coordinates by _π_ ( _x_ 0 : _. . ._ : _xn_ ) = ( _x_<sup>_♯_</sup> 0<sup>:</sup><sup>_. . ._:</sup><sup>_x_</sup> _n_<sup>_♯_).Inparticular,weseeagainthatthis</sup> isomorphism is of a deeply analytic and transcendental nature. 

We note that (P<sup>_n_</sup> _K_<sup>_♭_)adisitselfnotaperfectoidspace,but</sup> _←−_<sup>lim</sup> _ϕ_<sup>(P</sup> _K_<sup>_n♭_)adis,where</sup><sup>_ϕ_:</sup> P<sup>_n_</sup> _K_<sup>_♭→_P</sup><sup>_n_</sup> _K_<sup>_♭_denotesagainthe</sup><sup>_p_-thpowermaponcoordinates.However,</sup><sup>_ϕ_ispurely</sup> inseparable and hence induces an isomorphism on topological spaces and ´etale topoi, which is the reason that we have not written this inverse limit in Theorem 1.5 and Theorem 1.12. 

PERFECTOID SPACES 

5 

Finally, we apply these results to the weight-monodromy conjecture. Let us recall its formulation. Let _k_ be a local field whose residue field is of characteristic _p_ , let _Gk_ = Gal( _k/k_<sup>¯</sup> ), and let _q_ be the cardinality of the residue field of _k_ . For any finite-dimensional Q¯ _ℓ_ -representation _V_ of _Gk_ , we have the monodromy operator _N_ : _V → V_ ( _−_ 1) induced from the action of the _ℓ_ -adic inertia subgroup. It induces the monodromy filtration Fil<sup>_N_</sup> _i_<sup>_V⊂V_,</sup><sup>_i ∈_Z,characterizedbythepropertythat</sup><sup>_N_(Fil</sup> _i_<sup>_NV_)</sup><sup>_⊂_Fil</sup> _i_<sup>_N_</sup> _−_ 2<sup>_V_(</sup><sup>_−_1)forall</sup> _i ∈_ Z and gr<sup>_N_</sup> _i_<sup>_V∼_= gr</sup><sup>_N_</sup> _−i_<sup>_V_(</sup><sup>_−i_)via</sup><sup>_Ni_forall</sup><sup>_i ≥_0.</sup> 

**Conjecture 1.13** (Deligne, [9]) **.** _Let X be a proper smooth variety over k, and let V_ = _H_<sup>_i_</sup> ( _Xk_ ¯ _,_ Q<sup>¯</sup> _ℓ_ ) _. Then for all j ∈_ Z _and for any geometric Frobenius_ Φ _∈ Gk, all eigenvalues of_ Φ _on_ gr<sup>_N_</sup> _j_<sup>_VareWeilnumbersofweighti_+</sup><sup>_j,i.e.algebraicnumbersα_</sup> _such that |α|_ = _q_<sup>(</sup><sup>_i_+</sup><sup>_j_)</sup><sup>_/_2</sup> _for all complex absolute values._ 

Deligne, [10], proved this conjecture if _k_ is of characteristic _p_ , and the situation is already defined over a curve. The general weight-monodromy conjecture over fields _k_ of characteristic _p_ can be deduced from this case, as done by Terasoma, [33], and by Ito, [26]. 

In mixed characteristic, the conjecture is wide open. Introducing what is now called the Rapoport-Zink spectral sequence, Rapoport and Zink, [29], have proved the conjecture when _X_ has dimension at most 2 and _X_ has semistable reduction. They also show that in general it would follow from a suitable form of the standard conjectures, the main point being that a certain linear pairing on cohomology groups should be nondegenerate. Using de Jong’s alterations, [8], one can reduce the general case to the case of semistable reduction, and in particular the case of dimension at most 2 follows. Apart from that, other special cases are known. Notably, the case of varieties which admit _p_ -adic uniformization by Drinfeld’s upper half-space is proved by Ito, [25], by pushing through the argument of Rapoport-Zink in this special case, making use of the special nature of the components of the special fibre, which are explicit rational varieties. 

On the other hand, there is a large amount of activity that uses automorphic arguments to prove results in cases of certain Shimura varieties, notably those of type _U_ (1 _, n −_ 1) used in the book of Harris-Taylor [15]. Let us only mention the work of Taylor and Yoshida, [32], later completed by Shin, [30], and Caraiani, [6], as well as the independent work of Boyer, [4], [5]. Boyer’s results were used by Dat, [7], to handle the case of varieties which admit uniformization by a covering of Drinfeld’s upper half-space, thereby generalizing Ito’s result. 

Our last main theorem is the following. 

**Theorem 1.14.** _Let k be a local field of characteristic_ 0 _. Let X be a geometrically connected proper smooth variety over k such that X is a set-theoretic complete intersection in a projective smooth toric variety. Then the weight-monodromy conjecture is true for X._ 

Let us give a short sketch of the proof for a smooth hypersurface in _X ⊂_ P<sup>_n_</sup> , which is already a new result. We have the projection 



and we can look at the preimage _π_<sup>_−_1</sup> ( _X_ ). One has an injective map _H_<sup>_i_</sup> ( _X_ ) _→ H_<sup>_i_</sup> ( _π_<sup>_−_1</sup> ( _X_ )), and if _π_<sup>_−_1</sup> ( _X_ ) were an algebraic variety, then one could deduce the result from Deligne’s theorem in equal characteristic. However, the map _π_ is highly transcendental, and _π_<sup>_−_1</sup> ( _X_ ) will not be given by equations. In general, it will look like some sort of fractal, have infinite-dimensional cohomology, and will have infinite degree in the sense that it will meet a line in infinitely many points. As an easy example, let 



6 PETER SCHOLZE 

Then the homeomorphism 



means that _π_<sup>_−_1</sup> ( _X_ ) is topologically the inverse limit of the subvarieties 



However, we have the following crucial approximation lemma. 

**Lemma 1.15.** _Let X_<sup>˜</sup> _⊂_ (P<sup>_n_</sup> _K_<sup>)ad</sup><sup>_beasmallopenneighborhoodofthehypersurfaceX._</sup> _Then there is a hypersurface Y ⊂ π_<sup>_−_1</sup> ( _X_<sup>˜</sup> ) _._ 

The proof of this lemma is by an explicit approximation algorithm for the homogeneous polynomial defining _X_ , and is the reason that we have to restrict to complete intersections. Using a result of Huber, one finds some _X_<sup>˜</sup> such that _H_<sup>_i_</sup> ( _X_ ) = _H_<sup>_i_</sup> ( _X_<sup>˜</sup> ), and hence gets a map _H_<sup>_i_</sup> ( _X_ ) = _H_<sup>_i_</sup> ( _X_<sup>˜</sup> ) _→ H_<sup>_i_</sup> ( _Y_ ). As before, one checks that it is injective and concludes. 

After the results of this paper were first announced, Kiran Kedlaya informed us that he had obtained related results in joint work with Ruochuan Liu, [27]. In particular, in our terminology, they prove that for any perfectoid _K_ -algebra _R_ with tilt _R_<sup>_♭_</sup> , there is an equivalence between the finite ´etale _R_ -algebras and the finite ´etale _R_<sup>_♭_</sup> -algebras. However, the tilting equivalence, the generalization of Faltings’s almost purity theorem and the application to the weight-monodromy conjecture were not observed by them. This led to an exchange of ideas, with the following two influences on this paper. In the first version of this work, Theorem 1.3 was proved using a version of Faltings’s almost purity theorem for fields, proved in [14], Chapter 6, using ramification theory. Kedlaya observed that one could instead reduce to the case where _K_<sup>_♭_</sup> is algebraically closed, which gives a more elementary proof of the theorem. We include both arguments here. Secondly, a certain finiteness condition on the perfectoid _K_ -algebra was imposed at some places in the first version, a condition close to the notion of p-finiteness introduced below; in most applications known to the author, this condition is satisfied. Kedlaya made us aware of the possibility to deduce the general case by a simple limit argument. 

**Acknowledgments.** First, I want to express my deep gratitude to my advisor M. Rapoport, who suggested that I should think about the weight-monodromy conjecture, and in particular suggested that it might be possible to reduce it to the case of equal characteristic after a highly ramified base change. Next, I want to thank Gerd Faltings for a crucial remark on a first version of this paper. Moreover, I wish to thank all participants of the ARGOS seminar on perfectoid spaces at the University of Bonn in the summer term 2011, for working through an early version of this manuscript and the large number of suggestions for improvements. The same applies to Lorenzo Ramero, whom I also want to thank for his very careful reading of the manuscript. Moreover, I thank Roland Huber for answering my questions on adic spaces. Further thanks go to Ahmed Abbes, Bhargav Bhatt, Pierre Colmez, Laurent Fargues, Jean-Marc Fontaine, Ofer Gabber, Luc Illusie, Adrian Iovita, Kiran Kedlaya, Gerard Laumon, Ruochuan Liu, Wieslawa Niziol, Arthur Ogus, Martin Olsson, Bernd Sturmfels and Jared Weinstein for helpful discussions. Finally, I want to heartily thank the organizers of the CAGA lecture series at the IHES for their invitation. This work is the author’s PhD thesis at the University of Bonn, which was supported by the Hausdorff Center for Mathematics, and the thesis was finished while the author was a Clay Research Fellow. He wants to thank both institutions for their support. Moreover, parts of it were written while visiting Harvard University, the Universit´e Paris-Sud at Orsay, and the IHES, and the author wants to thank these institutions for their hospitality. 

PERFECTOID SPACES 

7 

# 2. Adic spaces 

Throughout this paper, we make use of Huber’s theory of adic spaces. For this reason, we recall some basic definitions and statements about adic spaces over nonarchimedean local fields. We also compare Huber’s theory to the more classical language of rigidanalytic geometry, and to the theory of Berkovich’s analytic spaces. The material of this section can be found in [20], [19] and [18]. 

**Definition 2.1.** _A nonarchimedean field is a topological field k whose topology is induced by a nontrivial valuation of rank_ 1 _._ 

In particular, _k_ admits a norm _| · |_ : _k →_ R _≥_ 0, and it is easy to see that _| · |_ is unique up to automorphisms _x �→ x_<sup>_α_</sup> , 0 _< α < ∞_ , of R _≥_ 0. 

Throughout, we fix a nonarchimedean field _k_ . Replacing _k_ by its completion will not change the theory, so we may and do assume that _k_ is complete. 

The idea of rigid-analytic geometry, and the closely related theories of Berkovich’s analytic spaces and Huber’s adic spaces, is to have a nonarchimedean analogue of the notion of complex analytic spaces over C. In particular, there should be a functor 

_{_ varieties _/k} →{_ adic spaces _/k}_ : _X �→ X_<sup>ad</sup> _,_ 

sending any variety over _k_ to its analytification _X_<sup>ad</sup> . Moreover, it should be possible to define subspaces of _X_<sup>ad</sup> by inequalities: For any _f ∈_ Γ( _X, OX_ ), the subset 



should make sense. In particular, any point _x ∈ X_<sup>ad</sup> should give rise to a valuation function _f �→|f_ ( _x_ ) _|_ . In classical rigid-analytic geometry, one considers only the maximal points of the scheme _X_ . Each of them gives a map Γ( _X, OX_ ) _→ k_<sup>_′_</sup> for some finite extension _k_<sup>_′_</sup> of _k_ ; composing with the unique extension of the absolute value of _k_ to _k_<sup>_′_</sup> gives a valuation on Γ( _X, OX_ ). In Berkovich’s theory, one considers norm maps Γ( _X, OX_ ) _→_ R _≥_ 0 inducing a fixed norm map on _k_ . Equivalently, one considers valuations of rank 1 on Γ( _X, OX_ ). In Huber’s theory, one allows also valuations of higher rank. 

**Definition 2.2.** _Let R be some ring. A valuation on R is given by a multiplicative map |·|_ : _R →_ Γ _∪{_ 0 _}, where_ Γ _is some totally ordered abelian group, written multiplicatively, such that |_ 0 _|_ = 0 _, |_ 1 _|_ = 1 _and |x_ + _y| ≤_ max( _|x|, |y|_ ) _for all x, y ∈ R._ 

_If R is a topological ring, then a valuation | · | on R is said to be continuous if for all γ ∈_ Γ _, the subset {x ∈ R | |x| < γ} ⊂ R is open._ 

_Remark_ 2.3 _._ The term valuation is somewhat unfortunate: If Γ = R _>_ 0, then this would usually be called a seminorm, and the term valuation would be used for (a constant multiple of) the map _x �→−_ log _|x|_ . On the other hand, the term higher-rank norm is much less commonly used than the term higher-rank valuation. For this reason, we stick with Huber’s terminology. 

_Remark_ 2.4 _._ Recall that a valuation ring is an integral domain _R_ such that for any _x̸_ = 0 in the fraction field _K_ of _R_ , at least one of _x_ and _x_<sup>_−_1</sup> is in _R_ . Any valuation _| · |_ on a field _K_ gives rise to the valuation subring _R_ = _{x | |x| ≤_ 1 _}_ . Conversely, a valuation ring _R_ gives rise to a valuation on _K_ with values in Γ = _K_<sup>_×_</sup> _/R_<sup>_×_</sup> , ordered by saying that _x ≤ y_ if _x_ = _yz_ for some _z ∈ R_ . With respect to a suitable notion of equivalence of valuations defined below, this induces a bijective correspondence between valuation subrings of _K_ and valuations on _K_ . 

If _|·|_ : _R →_ Γ _∪{_ 0 _}_ is a valuation on _R_ , let Γ _|·| ⊂_ Γ denote the subgroup generated by all _|x|_ , _x ∈ R_ , which are nonzero. The set supp( _| · |_ ) = _{x ∈ R | |x|_ = 0 _}_ is a prime ideal of _R_ called the support of _| · |_ . Let _K_ be the quotient field of _R/_ supp( _| · |_ ). Then the 

PETER SCHOLZE 

8 

valuation factors as a composite _R → K →_ Γ _∪{_ 0 _}_ . Let _R_ ( _| · |_ ) _⊂ K_ be the valuation subring, i.e. _R_ ( _| · |_ ) = _{x ∈ K | |x| ≤_ 1 _}_ . 

**Definition 2.5.** _Two valuations | · |, | · |_<sup>_′_</sup> _are called equivalent if the following equivalent conditions are satisfied._ 

(i) _There is an isomorphism of totally ordered groups α_ : Γ _|·|_<sup>_∼_</sup> = Γ _|·|′ such that |·|_<sup>_′_</sup> = _α◦|·|._ 

(ii) _The supports_ supp( _| · |_ ) = supp( _| · |_<sup>_′_</sup> ) _and valuation rings R_ ( _| · |_ ) = _R_ ( _| · |_<sup>_′_</sup> ) _agree._ 

(iii) _For all a, b ∈ R, |a| ≥|b| if and only if |a|_<sup>_′_</sup> _≥|b|_<sup>_′_</sup> _._ 

In [18], Huber defines spaces of (continuous) valuations in great generality. Let us specialize to the case of interest to us. 

**Definition 2.6.** (i) _A Tate k-algebra is a topological k-algebra R for which there exists a subring R_ 0 _⊂ R such that aR_ 0 _, a ∈ k_<sup>_×_</sup> _, forms a basis of open neighborhoods of_ 0 _. A subset M ⊂ R is called bounded if M ⊂ aR_ 0 _for some a ∈ k_<sup>_×_</sup> _. An element x ∈ R is called power-bounded if {x_<sup>_n_</sup> _| n ≥_ 0 _} ⊂ R is bounded. Let R_<sup>_◦_</sup> _⊂ R denote the subring of powerbounded elements._ 

(ii) _An affinoid k-algebra is a pair_ ( _R, R_<sup>+</sup> ) _consisting of a Tate k-algebra R and an open and integrally closed subring R_<sup>+</sup> _⊂ R_<sup>_◦_</sup> _._ 

(iii) _An affinoid k-algebra_ ( _R, R_<sup>+</sup> ) _is said to be of topologically finite type (tft for short) if R is a quotient of k⟨T_ 1 _, . . . , Tn⟩ for some n, and R_<sup>+</sup> = _R_<sup>_◦_</sup> _._ 

Here, 



is the ring of convergent power series on the ball given by _|T_ 1 _|, . . . , |Tn| ≤_ 1. Often, only affinoid _k_ -algebras of tft are considered; however, this paper will show that other classes of affinoid _k_ -algebras are of interest as well. We also note that any Tate _k_ -algebra _R_ , resp. affinoid _k_ -algebra ( _R, R_<sup>+</sup> ), admits the completion _R_<sup>ˆ</sup> , resp. ( _R,_<sup>ˆ</sup> _R_<sup>ˆ+</sup> ), which is again a Tate, resp. affinoid, _k_ -algebra. Everything depends only on the completion, so one may assume that ( _R, R_<sup>+</sup> ) is complete in the following. 

**Definition 2.7.** _Let_ ( _R, R_<sup>+</sup> ) _be an affinoid k-algebra. Let_ 

_X_ = Spa( _R, R_<sup>+</sup> ) = _{| · |_ : _R →_ Γ _∪{_ 0 _}_ continuous valuation _| ∀f ∈ R_<sup>+</sup> : _|f | ≤_ 1 _}/_<sup>_∼_</sup> = _. For any x ∈ X, write f �→|f_ ( _x_ ) _| for the corresponding valuation on R. We equip X with the topology which has the open subsets_ 



_called rational subsets, as basis for the topology, where f_ 1 _, . . . , fn ∈ R generate R as an ideal and g ∈ R._ 

_Remark_ 2.8 _._ Let _ϖ ∈ k_ be topologically nilpotent, i.e. _|ϖ| <_ 1. Then to _f_ 1 _, . . . , fn_ one can add _fn_ +1 = _ϖ_<sup>_N_</sup> for some big integer _N_ without changing the rational subspace. Indeed, there are elements _h_ 1 _, . . . , hn ∈ R_ such that<sup>�</sup> _hifi_ = 1. Multiplying by _ϖ_<sup>_N_</sup> for _N_ sufficiently large, we have _ϖ_<sup>_N_</sup> _hi ∈ R_<sup>+</sup> , as _R_<sup>+</sup> _⊂ R_ is open. Now for any _x ∈ U_ (<sup>_<u>f</u>_</sup><sup><u>1</u></sup><sup>_<u>,...</u>_</sup> _g_<sup>_<u>,fn</u>_</sup> ), we have 



as desired. In particular, we see that on rational subsets, _|g_ ( _x_ ) _|_ is nonzero, and bounded from below. 

PERFECTOID SPACES 

9 

The topological spaces Spa( _R, R_<sup>+</sup> ) have some special properties reminiscent of the properties of Spec( _A_ ) for a ring _A_ . In fact, let us recall the following result of Hochster, [17]. 

**Definition/Proposition 2.9.** _A topological space X is called spectral if it satisfies the following equivalent properties._ 

- (i) _There is some ring A such that X_<sup>_∼_</sup> = Spec( _A_ ) _._ 

(ii) _One can write X as an inverse limit of finite T_ 0 _spaces._ 

(iii) _The space X is quasicompact, has a basis of quasicompact open subsets stable under finite intersections, and every irreducible closed subset has a unique generic point._ 

In particular, spectral spaces are quasicompact, quasiseparated and _T_ 0. Recall that a topological space _X_ is called quasiseparated if the intersection of any two quasicompact open subsets is again quasicompact. In the following we will often abbreviate quasicompact, resp. quasiseparated, as qc, resp. qs. 

**Proposition 2.10** ([18, Theorem 3.5]) **.** _For any affinoid k-algebra_ ( _R, R_<sup>+</sup> ) _, the space_ Spa( _R, R_<sup>+</sup> ) _is spectral. The rational subsets form a basis of quasicompact open subsets stable under finite intersections._ 

**Proposition 2.11** ([18, Proposition 3.9]) **.** _Let_ ( _R, R_<sup>+</sup> ) _be an affinoid k-algebra with completion_ ( _R,_<sup>ˆ</sup> _R_<sup>ˆ+</sup> ) _. Then_ Spa( _R, R_<sup>+</sup> )<sup>_∼_</sup> = Spa( _R,_<sup>ˆ</sup> _R_<sup>ˆ+</sup> ) _, identifying rational subsets._ 

Moreover, the space Spa( _R, R_<sup>+</sup> ) is large enough to capture important properties. 

**Proposition 2.12.** _Let_ ( _R, R_<sup>+</sup> ) _be an affinoid k-algebra, X_ = Spa( _R, R_<sup>+</sup> ) _._ (i) _If X_ = _∅, then R_<sup>ˆ</sup> = 0 _._ 

(ii) _Let f ∈ R be such that |f_ ( _x_ ) _|̸_ = 0 _for all x ∈ X. If R is complete, then f is invertible._ (iii) _Let f ∈ R be such that |f_ ( _x_ ) _| ≤_ 1 _for all x ∈ X. Then f ∈ R_<sup>+</sup> _._ 

_Proof._ Part (i) is [18], Proposition 3.6 (i). Part (ii) is [19], Lemma 1.4, and part (iii) follows from [18], Lemma 3.3 (i). □ 

We want to endow _X_ = Spa( _R, R_<sup>+</sup> ) with a structure sheaf _OX_ . The construction is as follows. 

**Definition 2.13.** _Let_ ( _R, R_<sup>+</sup> ) _be an affinoid k-algebra, and let U_ = _U_ (<sup>_<u>f</u>_</sup><sup><u>1</u></sup><sup>_<u>,...</u>_</sup> _g_<sup>_<u>,fn</u>_</sup> ) _⊂ X_ = Spa( _R, R_<sup>+</sup> ) _be a rational subset. Choose some R_ 0 _⊂ R such that aR_ 0 _, a ∈ k_<sup>_×_</sup> _, is a basis of open neighborhoods of_ 0 _in R. Consider the subalgebra R_ [<sup>_<u>f</u>_</sup> _g_<sup><u>1</u></sup><sup>_, . . . ,_</sup><sup>_<u>f</u>_</sup> _g_<sup>_<u>n</u>_]</sup><sup>_ofR_[</sup><sup>_g−_1]</sup><sup>_,and_</sup> _equip it with the topology making aR_ 0[<sup>_<u>f</u>_</sup> _g_<sup><u>1</u></sup><sup>_, . . . ,_</sup><sup>_<u>f</u>_</sup> _g_<sup>_<u>n</u>_]</sup><sup>_,a ∈k×,abasisofopenneighborhoods_</sup> _of_ 0 _. Let B ⊂ R_ [<sup>_<u>f</u>_</sup> _g_<sup><u>1</u></sup><sup>_, . . . ,_</sup><sup>_<u>f</u>_</sup> _g_<sup>_<u>n</u>_]</sup><sup>_betheintegralclosureofR_+[</sup><sup>_<u>f</u>_</sup> _g_<sup><u>1</u></sup><sup>_, . . . ,_</sup><sup>_<u>f</u>_</sup> _g_<sup>_<u>n</u>_]</sup><sup>_inR_[</sup><sup>_<u>f</u>_</sup> _g_<sup><u>1</u></sup><sup>_, . . . ,_</sup><sup>_<u>f</u>_</sup> _g_<sup>_<u>n</u>_]</sup><sup>_._</sup> _Then_ ( _R_ [<sup>_<u>f</u>_</sup> _g_<sup><u>1</u></sup><sup>_, . . . ,_</sup><sup>_<u>f</u>_</sup> _g_<sup>_<u>n</u>_]</sup><sup>_, B_)</sup><sup>_is an affinoid k-algebra.Let_(</sup><sup>_R⟨_</sup><sup>_<u>f</u>_</sup> _g_<sup><u>1</u></sup><sup>_, . . . ,_</sup><sup>_<u>f</u>_</sup> _g_<sup>_<u>n</u>⟩,B_ˆ)</sup><sup>_be its completion._</sup> 

Obviously, 



factors over the open subset _U ⊂ X_ . 

**Proposition 2.14** ([19, Proposition 1.3]) **.** _In the situation of the definition, the following universal property is satisfied. For every complete affinoid k-algebra_ ( _S, S_<sup>+</sup> ) _with a map_ ( _R, R_<sup>+</sup> ) _→_ ( _S, S_<sup>+</sup> ) _such that the induced map_ Spa( _S, S_<sup>+</sup> ) _→_ Spa( _R, R_<sup>+</sup> ) _factors over U , there is a unique map_ 



_making the obvious diagram commute._ 

10 

PETER SCHOLZE 



The idea is that since _f_ 1 _, . . . , fn_ generate _R_ , not all _|fi_ ( _x_ ) _|_ = 0 for _x ∈ U_ ; in particular, _|g_ ( _x_ ) _|̸_ = 0 for all _x ∈ U_ . This implies that _g_ is invertible in _S_ in the situation of the proposition. Moreover, _|_ (<sup>_<u>f</u>_</sup> _g_<sup>_<u>i</u>_)(</sup><sup>_x_)</sup><sup>_| ≤_1forall</sup><sup>_x ∈U_,whichmeansthat</sup><sup>_<u>f</u>_</sup> _g_<sup>_<u>i</u>∈S_+.</sup> We define presheaves _OX_ and _OX_<sup>+on</sup><sup>_X_asaboveonrationalsubsets,andforgeneral</sup> open _U ⊂ X_ by requiring 



and similarly for _OX_<sup>+.</sup> 

**Proposition 2.15** ([19, Lemma 1.5, Proposition 1.6]) **.** _For any x ∈ X, the valuation f �→|f_ ( _x_ ) _| extends to the stalk OX,x, and_ 

_OX,x_<sup>+=</sup><sup>_{f∈OX,x| |f_(</sup><sup>_x_)</sup><sup>_| ≤_1</sup><sup>_}._</sup> 

_The ring OX,x is a local ring with maximal ideal given by {f | |f_ ( _x_ ) _|_ = 0 _}. The ring OX,x_<sup>+</sup><sup>_isalocalringwithmaximalidealgivenby{f||f_(</sup><sup>_x_)</sup><sup>_|<_1</sup><sup>_}.Moreover,forany_</sup> _open subset U ⊂ X,_ 

_OX_<sup>+(</sup><sup>_U_) =</sup><sup>_{f∈OX_(</sup><sup>_U_)</sup><sup>_| ∀x ∈U_:</sup><sup>_|f_(</sup><sup>_x_)</sup><sup>_| ≤_1</sup><sup>_}._</sup> 

_If U ⊂ X is rational, then U_<sup>_∼_</sup> = Spa( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))</sup><sup>_compatiblewithrationalsubsets,_</sup> _the presheaves OX and OX_<sup>+</sup><sup>_,andthevaluationsatallx ∈U._</sup> 

Unfortunately, it is not in general known<sup>1</sup> that _OX_ is sheaf. We note that the proposition ensures that _OX_<sup>+is a sheaf if</sup><sup>_OX_is.The basic problem is that completion behaves</sup> in general badly for nonnoetherian rings. 

**Definition 2.16.** _A Tate k-algebra R is called strongly noetherian if_ 



_is noetherian for all n ≥_ 0 _._ 

For example, if _R_ is of tft, then _R_ is strongly noetherian. 

**Theorem 2.17** ([19, Theorem 2.2]) **.** _If_ ( _R, R_<sup>+</sup> ) _is an affinoid k-algebra such that R is strongly noetherian, then OX is a sheaf._ 

Later, we will show that this theorem is true under the assumption that _R_ is a perfectoid _k_ -algebra. We define perfectoid _k_ -algebras later; let us only remark that except for trivial examples, they are huge and in particular not strongly noetherian. 

Finally, we can define the category of adic spaces over _k_ . Namely, consider the category ( _V_ ) of triples ( _X, OX ,_ ( _|·_ ( _x_ ) _| | x ∈ X_ )) consisting of a locally ringed topological space ( _X, OX_ ), where _OX_ is a sheaf of complete topological _k_ -algebras, and a continuous valuation _f �→|f_ ( _x_ ) _|_ on _OX,x_ for every _x ∈ X_ . Morphisms are given by morphisms of locally ringed topological spaces which are continuous _k_ -algebra morphisms on _OX_ , and compatible with the valuations in the obvious sense. 

Any affinoid _k_ -algebra ( _R, R_<sup>+</sup> ) for which _OX_ is a sheaf gives rise to such a triple ( _X, OX ,_ ( _| ·_ ( _x_ ) _| | x ∈ X_ )). Call an object of ( _V_ ) isomorphic to such a triple an affinoid adic space. 

1and probably not true 

PERFECTOID SPACES 

11 

**Definition 2.18.** _An adic space over k is an object_ ( _X, OX ,_ ( _| ·_ ( _x_ ) _| | x ∈ X_ )) _of_ ( _V_ ) _that is locally on X an affinoid adic space._ 

**Proposition 2.19** ([19, Proposition 2.1 (ii)]) **.** _For any affinoid k-algebra_ ( _R, R_<sup>+</sup> ) _with X_ = Spa( _R, R_<sup>+</sup> ) _such that OX is a sheaf, and any adic space Y over k, we have_ 

Hom( _Y, X_ ) = Hom(( _R,_<sup>ˆ</sup> _R_<sup>ˆ+</sup> ) _,_ ( _OY_ ( _Y_ ) _, OY_<sup>+(</sup><sup>_Y_)))</sup><sup>_._</sup> 

_Here, the latter set denotes the set of continuous k-algebra morphisms R_<sup>ˆ</sup> _→OY_ ( _Y_ ) _such that R_<sup>ˆ+</sup> _is mapped into OY_<sup>+(</sup><sup>_Y_)</sup><sup>_._</sup> 

In particular, the category of complete affinoid _k_ -algebras for which the structure presheaf is a sheaf is equivalent to the category of affinoid adic spaces over _k_ . 

For the rest of this section, let us discuss an example, and explain the relation to rigid-analytic varieties, [31], and Berkovich’s analytic spaces, [1]. 

_Example_ 2.20 _._ Assume that _k_ is complete and algebraically closed. Let _R_ = _k⟨T ⟩_ , _R_<sup>+</sup> = _R_<sup>_◦_</sup> = _k_<sup>_◦_</sup> _⟨T ⟩_ the subspace of power series with coefficients in _k_<sup>_◦_</sup> . Then ( _R, R_<sup>+</sup> ) is an affinoid _k_ -algebra of tft. We want to describe the topological space _X_ = Spa( _R, R_<sup>+</sup> ). For convenience, let us fix the norm _| · |_ : _k →_ R _≥_ 0. Then there are in general points of 5 different types, of which the first four are already present in Berkovich’s theory. 

(1) The classical points: Let _x ∈ k_<sup>_◦_</sup> , i.e. _x ∈ k_ with _|x| ≤_ 1. Then for any _f ∈ k⟨T ⟩_ , we can evaluate _f_ at _x_ to get a map _R → k_ , _f_ =<sup>�</sup> _anT_<sup>_n_</sup> _�→_<sup>�</sup> _anx_<sup>_n_</sup> . Composing with the norm on _k_ , one gets a valuation _f �→|f_ ( _x_ ) _|_ on _R_ , which is obviously continuous and _≤_ 1 for all _f ∈ R_<sup>+</sup> . 

(2), (3) The rays of the tree: Let 0 _≤ r ≤_ 1 be some real number, and _x ∈ k_<sup>_◦_</sup> . Then 



defines another continuous valuation on _R_ which is _≤_ 1 for all _f ∈ R_<sup>+</sup> . It depends only on the disk _D_ ( _x, r_ ) = _{y ∈ k_<sup>_◦_</sup> _| |y − x| ≤ r}_ . If _r_ = 0, then it agrees with the classical point corresponding to _x_ . For _r_ = 1, the disk _D_ ( _x,_ 1) is independent of _x ∈ k_<sup>_◦_</sup> , and the corresponding valuation is called the Gaußpoint. 

If _r ∈|k_<sup>_×_</sup> _|_ , then the point is said to be of type (2), otherwise of type (3). Note that a branching occurs at a point corresponding to the disk _D_ ( _x, r_ ) if and only if _r ∈|k_<sup>_×_</sup> _|_ , i.e. a branching occurs precisely at the points of type (2). 

(4) Dead ends of the tree: Let _D_ 1 _⊃ D_ 2 _⊃ . . ._ be a sequence of disks with<sup>�</sup> _Di_ = _∅_ . 

Such families exist if _k_ is not spherically complete, e.g. if _k_ = C _p_ . Then 



PETER SCHOLZE 

12 

defines a valuation on _R_ , which again is _≤_ 1 for all _f ∈ R_<sup>+</sup> . 

(5) Finally, there are some valuations of rank 2 which are only seen in the adic space. Let us first give an example, before giving the general classification. Consider the totally ordered abelian group Γ = R _>_ 0 _× γ_<sup>Z</sup> , where we require that _r < γ <_ 1 for all real numbers _r <_ 1. It is easily seen that there is a unique such ordering. Then 



defines a rank-2-valuation on _R_ . This is similar to cases (2), (3), but with the variable _r_ infinitesimally close to 1. One may check that this point only depends on the disc _D_ ( _x, <_ 1) = _{y ∈ k_<sup>_◦_</sup> _| |y − x| <_ 1 _}_ . 

Similarly, take any _x ∈ k_<sup>_◦_</sup> , some real number 0 _< r <_ 1 and choose a sign ? _∈{<, >}_ . Consider the totally ordered abelian group Γ? _r_ = R _>_ 0 _× γ_<sup>Z</sup> , where _r_<sup>_′_</sup> _< γ < r_ for all real numbers _r_<sup>_′_</sup> _< r_ if ? = _<_ , and _r_<sup>_′_</sup> _> γ > r_ for all real numbers _r_<sup>_′_</sup> _> r_ if ? = _>_ . Then 



defines a rank 2-valuation on _R_ . If ? = _<_ , then it depends only on _D_ ( _x, < r_ ) = _{y ∈ k_<sup>_◦_</sup> _| |y − x| < r}_ . If ? = _>_ , then it depends only on _D_ ( _x, r_ ). 

One checks that if _r̸ ∈|k_<sup>_×_</sup> _|_ , then these points are all equivalent to the corresponding point of type (3). However, at each branching point, i.e. point of type (2), this gives exactly one additional point for each ray starting from this point. 

All points except those of type (2) are closed. Let _κ_ be the residue field of _k_ . Then the closure of the Gaußpoint is exactly the Gaußpoint together with the points of type (5) around it, and is homeomorphic to A<sup>1</sup> _κ_<sup>,withtheGaußpointasthegenericpoint.At</sup> the other points of type (2), one gets P<sup>1</sup> _κ_<sup>.</sup> 

We note that in case (5), one could define a similar valuation 



with _γ_ having the property that _r > γ >_ 1 for all _r >_ 1. This valuation would still be continuous, but it takes the value _γ >_ 1 on _T ∈ R_<sup>+</sup> . This shows the relevance of the requirement _|f_ ( _x_ ) _| ≤_ 1 for all _f ∈ R_<sup>+</sup> , which is automatic for rank-1-valuations. 

**Theorem 2.21** ([20, (1.1.11)]) **.** _There is a fully faithful functor_ 

_r_ : _{_ rigid _−_ analytic varieties _/k} →{_ adic spaces _/k}_ : _X �→ X_<sup>ad</sup> 

_sending_ Sp( _R_ ) _to_ Spa( _R, R_<sup>+</sup> ) _for any affinoid k-algebra_ ( _R, R_<sup>+</sup> ) _of tft. It induces an equivalence_ 

_{_ qs rigid _−_ analytic varieties _/k}_<sup>_∼_</sup> = _{_ qs adic spaces locally of finite type _/k} ,_ 

_where an adic space over k is called locally of finite type if it is locally of the form_ Spa( _R, R_<sup>+</sup> ) _, where_ ( _R, R_<sup>+</sup> ) _is of tft. Let X be a rigid-analytic variety over k with corresponding adic space X_<sup>ad</sup> _. As any classical point defines an adic point, we have X ⊂ X_<sup>ad</sup> _. If X is quasiseparated, then mapping a quasicompact open subset U ⊂ X_<sup>ad</sup> _to U ∩ X defines a bijection_ 

_{_ qc admissible opens in _X}_<sup>_∼_</sup> = _{_ qc opens in _X_<sup>ad</sup> _} ,_ 

_the inverse of which is denoted U �→ U_<sup>˜</sup> _. Under this bijection a family of quasicompact admissible opens Ui ⊂ X forms an admissible cover if and only if the corresponding subsets U_<sup>˜</sup> _i ⊂ X_<sup>ad</sup> _cover X_<sup>ad</sup> _._ 

_In particular, for any rigid-analytic variety X, the topos of sheaves on the Grothendieck site associated to X is equivalent to the category of sheaves on the sober topological space X_<sup>ad</sup> _._ 

PERFECTOID SPACES 

13 

We recall that for abstract reasons, there is up to equivalence at most one sober topological space with the last property in the theorem. This gives the topological space underlying the adic space a natural interpretation. 

In the example _X_ = Sp( _k⟨T ⟩_ ) discussed above, a typical example of a non-admissible cover is the cover of _{x | |x| ≤_ 1 _}_ as 



In the adic world, one can see this non-admissibility as being caused by the point of type (5) which gives _|x|_ a value _γ <_ 1 bigger than any _r <_ 1. 

Moreover, adic spaces behave well with respect to formal models. In fact, one can define adic spaces in greater generality so as to include locally noetherian formal schemes as a full subcategory, but we will not need this more general theory here. 

**Theorem 2.22.** _Let_ X _be some admissible formal scheme over k_<sup>_◦_</sup> _, let X be its generic fibre in the sense of Raynaud, and let X_<sup>ad</sup> _be the associated adic space. Then there is a continuous specialization map_ 

sp : _X_<sup>ad</sup> _→_ X _,_ 

_extending to a morphism of locally ringed topological spaces_ ( _X_<sup>ad</sup> _, OX_<sup>+ad)</sup><sup>_→_(X</sup><sup>_, O_X)</sup><sup>_._</sup> 

_Now assume that X is a fixed quasicompact quasiseparated adic space locally of finite type over k. By Raynaud, there exist formal models_ X _for X, unique up to admissible blowup. Then there is a homeomorphism_ 



_where_ X _runs over formal models of X, extending to an isomorphism of locally ringed topological spaces_ ( _X, OX_<sup>+)</sup><sup>_∼_= lim</sup> _←−_ X<sup>(X</sup><sup>_, O_X)</sup><sup>_,wheretheright-handsideistheinverselimit_</sup> _in the category of locally ringed topological spaces._ 

_Proof._ It is an easy exercise to deduce this from the previous theorem and the results of [3], Section 4, and [19], Section 4. □ 

In the example, one can start with X = Spf( _k_<sup>_◦_</sup> _⟨T ⟩_ ) as a formal model; this gives A<sup>1</sup> _κ_ as underlying topological space. After that, one can perform iterated blowups at closed points. This introduces additional P<sup>1</sup> _κ_<sup>’s;the strict transform of each component survives</sup> in the inverse limit and gives the closure of a point of type (2). Note that the point of type (2) is given as the preimage of the generic point of the component in the formal model. 

We note that in order to get continuity of sp, it is necessary to use nonstrict equalities in the definition of open subsets. 

Now, let us state the following theorem about the comparison of Berkovich’s analytic spaces and Huber’s adic spaces. For this, we need to recall the following definition: 

**Definition 2.23.** _An adic space X over k is called taut if it is quasiseparated and for every quasicompact open subset U ⊂ X, the closure U of U in X is still quasicompact._ 

PETER SCHOLZE 

14 

Most natural adic spaces are taut, e.g. all affinoid adic spaces, or more generally all qcqs adic spaces, and also all adic spaces associated to separated schemes of finite type over _k_ . However, in recent work of Hellmann, [16], studying an analogue of RapoportZink period domains in the context of deformations of Galois representations, it was found that the weakly admissible locus is in general a nontaut adic space. 

We note that one can also define taut rigid-analytic varieties, and that one gets an equivalence of categories between the category of taut rigid-analytic varieties over _k_ and taut adic spaces locally of finite type over _k_ . Hence the first equivalence in the following theorem could be stated without reference to adic spaces. 

**Theorem 2.24** ([20, Proposition 8.3.1, Lemma 8.1.8]) **.** _There is an equivalence of categories_ 





_sending M_ ( _R_ ) _to_ Spa( _R, R_<sup>+</sup> ) _for any affinoid k-algebra_ ( _R, R_<sup>+</sup> ) _of tft._ 

_Let X_<sup>Berk</sup> _map to X_<sup>ad</sup> _under this equivalence. Then there is an injective map of sets X_<sup>Berk</sup> _→ X_<sup>ad</sup> _, whose image is precisely the subset of rank-_ 1 _-valuations. This map is in general not continuous. It admits a continuous retraction X_<sup>ad</sup> _→ X_<sup>Berk</sup> _, which identifies X_<sup>Berk</sup> _with the maximal hausdorff quotient of X_<sup>ad</sup> _._ 

In the example above, the image of the map _X_<sup>Berk</sup> _→ X_<sup>ad</sup> consists of the points of type (1) - (4). The retraction _X_<sup>ad</sup> _→ X_<sup>Berk</sup> contracts each point of type (2) with all points of type (5) around it, mapping them to the corresponding point of type (2) in _X_<sup>Berk</sup> . For any map from _X_<sup>ad</sup> to a hausdorff topological space, any point of type (2) will have the same image as the points of type (5) around it, as they lie in its topological closure, which verifies the last assertion of the theorem in this case. 

Let us end this section by describing in more detail the fibres of the map _X_<sup>ad</sup> _→ X_<sup>Berk</sup> . In fact, this discussion is valid even for adic spaces which are not related to Berkovich spaces. As the following discussion is local, we restrict to the affinoid case. 

Let ( _R, R_<sup>+</sup> ) be an affinoid _k_ -algebra, and let _X_ = Spa( _R, R_<sup>+</sup> ). We need not assume that _OX_ is a sheaf in the following. For any _x ∈ X_ , we let _k_ ( _x_ ) be the residue field of _OX,x_ , and _k_ ( _x_ )<sup>+</sup> _⊂ k_ ( _x_ ) be the image of _OX,x_<sup>+.Wehavethefollowingcrucialproperty,</sup> surprising at first sight. 

**Proposition 2.25.** _Let ϖ ∈ k be topologically nilpotent. Then the ϖ-adic completion of OX,x_<sup>+</sup><sup>_isequaltotheϖ-adiccompletion_</sup> _k_<sup>�</sup> ( _x_ )+ _of k_ ( _x_ )+ _._ 

_Proof._ It is enough to note that kernel of the map _OX,x_<sup>+</sup><sup>_→k_(</sup><sup>_x_)+,whichisalsothe</sup> kernel of the map _OX,x → k_ ( _x_ ), is _ϖ_ -divisible. □ 

**Definition 2.26.** _An affinoid field is pair_ ( _K, K_<sup>+</sup> ) _consisting of a nonarchimedean field K and an open valuation subring K_<sup>+</sup> _⊂ K_<sup>_◦_</sup> _._ 

In other words, an affinoid field is given by a nonarchimedean field _K_ equipped with a continuous valuation (up to equivalence). In the situation above, ( _k_ ( _x_ ) _, k_ ( _x_ )<sup>+</sup> ) is an affinoid field. The completion of an affinoid field is again an affinoid field. Also note that affinoid fields for which _k ⊂ K_ are affinoid _k_ -algebras. The following description of points is immediate. 

**Proposition 2.27.** _Let_ ( _R, R_<sup>+</sup> ) _be an affinoid k-algebra. The points of_ Spa( _R, R_<sup>+</sup> ) _are in bijection with maps_ ( _R, R_<sup>+</sup> ) _→_ ( _K, K_<sup>+</sup> ) _to complete affinoid fields_ ( _K, K_<sup>+</sup> ) _such that the quotient field of the image of R in K is dense._ 

PERFECTOID SPACES 

15 

**Definition 2.28.** _For two points x, y in some topological space X, we say that x specializes to y (or y generalizes to x), written x ≻ y (or y ≺ x), if y lies in the closure {x} of x._ 

**Proposition 2.29** ([20, (1.1.6) - (1.1.10)]) **.** _Let_ ( _R, R_<sup>+</sup> ) _be an affinoid k-algebra, and let x, y ∈ X_ = Spa( _R, R_<sup>+</sup> ) _correspond to maps_ ( _R, R_<sup>+</sup> ) _→_ ( _K, K_<sup>+</sup> ) _, resp._ ( _R, R_<sup>+</sup> ) _→_ ( _L, L_<sup>+</sup> ) _. Then x ≻ y if and only if K_<sup>_∼_</sup> = _L as topological R-algebras and L_<sup>+</sup> _⊂ K_<sup>+</sup> _._ 

_For any point y ∈ X, the set {x | x ≻ y} of generalizations of y is a totally ordered chain of length exactly the rank of the valuation corresponding to y._ 

Note that in particular, for a given complete nonarchimedean field _K_ with a map _R → K_ , there is the point _x_ 0 corresponding to ( _K, K_<sup>_◦_</sup> ). This corresponds to the unique continuous rank-1-valuation on _K_ . The point _x_ 0 specializes to any other point for the same _K_ . 

# 3. Perfectoid fields 

**Definition 3.1.** _A perfectoid field is a complete nonarchimedean field K of residue characteristic p >_ 0 _whose associated rank-_ 1 _-valuation is nondiscrete, such that the Frobenius is surjective on K_<sup>_◦_</sup> _/p._ 

We note that the requirement that the valuation is nondiscrete is needed to exclude unramified extensions of Q _p_ . It has the following consequence. 

**Lemma 3.2.** _Let |·|_ : _K →_ Γ _∪{_ 0 _} be the unique rank-_ 1 _-valuation on K, where_ Γ = _|K_<sup>_×_</sup> _| is chosen minimal. Then_ Γ _is p-divisible._ 

_Proof._ As Γ _̸_ = _|p|_<sup>Z</sup> , the group Γ is generated by the set of all _|x|_ for _x ∈ K_ with _|p| < |x| ≤_ 1. For such _x_ , choose some _y_ such that _|x − y_<sup>_p_</sup> _| ≤|p|_ . Then _|y|_<sup>_p_</sup> = _|y_<sup>_p_</sup> _|_ = _|x|_ , as desired. □ 

The class of perfectoid fields naturally separates into the fields of characteristic 0 and those of characteristic _p_ . In characteristic _p_ , a perfectoid field is the same as a complete perfect nonarchimedean field. 

_Remark_ 3.3 _._ The notion of a perfectoid field is closely related to the notion of a deeply ramified field. Taking the definition of deeply ramified fields given in [14], we remark that Proposition 6.6.6 of [14] says that a perfectoid field _K_ is deeply ramified, and conversely, a complete deeply ramified field with valuation of rank 1 is a perfectoid field. 

Now we describe the process of tilting for perfectoid fields, which is a functor from the category of all perfectoid fields to the category of perfectoid fields in characteristic _p_ . 

For its first description, choose some element _ϖ ∈ K_<sup>_×_</sup> such that _|p| ≤|ϖ| <_ 1. Now consider 



where Φ denotes the Frobenius morphism _x �→ x_<sup>_p_</sup> . This gives a perfect ring of characteristic _p_ . We equip it with the inverse limit topology; note that each _K_<sup>_◦_</sup> _/ϖ_ naturally has the discrete topology. 

**Lemma 3.4.** (i) _There is a multiplicative homeomorphism_ 



_given by projection. In particular, the right-hand side is independent of ϖ. Moreover, we get a map_ 

lim _←− K_<sup>_◦_</sup> _/ϖ → K_<sup>_◦_</sup> : _x �→ x_<sup>_♯_</sup> _._ Φ 



(iii) _There is a multiplicative homeomorphism_ 



_In particular, there is a map K_<sup>_♭_</sup> _→ K, x �→ x_<sup>_♯_</sup> _. Then K_<sup>_♭_</sup> _is a perfectoid field of characteristic p, K_<sup>_♭◦_</sup> = _←−_ lim _K_<sup>_◦∼_</sup> = lim _←− K_<sup>_◦_</sup> _/ϖ , x�→x_<sup>_p_</sup> Φ 

_and the rank-_ 1 _-valuation on K_<sup>_♭_</sup> _can be defined by |x|K♭_ = _|x_<sup>_♯_</sup> _|K. We have |K_<sup>_♭×_</sup> _|_ = _|K_<sup>_×_</sup> _|. Moreover,_ 



_where_ m _, resp._ m<sup>_♭_</sup> _, is the maximal ideal of K_<sup>_◦_</sup> _, resp. K_<sup>_♭◦_</sup> _._ 

(iv) _If K is of characteristic p, then K_<sup>_♭_</sup> = _K._ 

We call _K_<sup>_♭_</sup> the tilt of _K_ . 

_Remark_ 3.5 _._ Obviously, _ϖ_<sup>_♭_</sup> in (ii) is not unique. As it is not harmful to replace _ϖ_ with an element of the same norm, we will usually redefine _ϖ_ = ( _ϖ_<sup>_♭_</sup> )<sup>_♯_</sup> , which comes equipped with a compatible system 



of _p_<sup>_n_</sup> -th roots. Conversely, _ϖ_ together with such a choice of _p_<sup>_n_</sup> -th roots gives an element _ϖ_<sup>_♭_</sup> of 



_Proof._ (i) We begin by constructing a multiplicative continuous map 



Let <u>(</u> _<u>x</u>_ 0 _,_ _<u>x</u>_ 1 _, . . ._ ) _∈_ lim _←−_ Φ<sup>_K◦/ϖ_.Chooseanylift</sup><sup>_xn∈K◦_of</sup> _<u>xn</u>_ . Then we claim that the limit 

_x_<sup>_♯_</sup> = lim _n n→∞_<sup>_xpn_</sup> 

exists and is independent of all choices. For this, it is enough to see that _xn_<sup>_pn_</sup> gives a well-defined element of _K_<sup>_◦_</sup> _/ϖ_<sup>_n_+1</sup> . But if _x_<sup>_′_</sup> _n_<sup>isasecondlift,then</sup><sup>_xn−x′_</sup> _n_<sup>isdivisibleby</sup> _ϖ_ . One checks by induction on _i_ = 0 _,_ 1 _, . . . , n_ that 



It is clear from the definition that _x �→ x_<sup>_♯_</sup> is multiplicative and continuous. Now the map _←−_ limΦ<sup>_K◦/ϖ→_lim</sup> _←−x�→x_<sup>_p K◦_givenby</sup><sup>_x�→_(</sup><sup>_x♯,_(</sup><sup>_x_1</sup><sup>_/p_)</sup><sup>_♯, . . ._)givesaninversetothe</sup> obvious projection map. (ii) Pick some element _ϖ_ 1 with _|ϖ_ 1 _|_<sup>_p_</sup> = _|ϖ|_ . Then _ϖ_ 1 defines a nonzero element of _K_<sup>_◦_</sup> _/ϖ_ . Choose any sequence 



this is possible by surjectivity of Φ on _K_<sup>_◦_</sup> _/ϖ_ . By the proof of part (i), we have _|_ ( _ϖ_<sup>_♭_</sup> )<sup>_♯_</sup> _− ϖ_ 1<sup>_p| ≤|ϖ|_2.Thisgives</sup><sup>_|_(</sup><sup>_ϖ♭_)</sup><sup>_♯|_=</sup><sup>_|ϖ|_,asdesired.</sup> 

PERFECTOID SPACES 

17 

(iii) As _x �→ x_<sup>_♯_</sup> is multiplicative, it extends to a map 



One easily checks that it is a homeomorphism; in particular _K_<sup>_♭_</sup> is a field. One also checks that the topology on _←−_ limΦ<sup>_K◦/ϖ_isinducedbythenorm</sup><sup>_x�→|x♯|_.Hencethe</sup> topology on _K_<sup>_♭_</sup> is induced by the rank-1-valuation _x �→|x_<sup>_♯_</sup> _|_ . Clearly, _K_<sup>_♭_</sup> is perfect and complete, so _K_<sup>_♭_</sup> is a perfectoid field of characteristic _p_ . One easily deduces all other claims. 



Recall that when working with adic spaces, it is important to understand the continuous valuations on _K_ . Under the process of tilting, we have the following equivalence. 

**Proposition 3.6.** _Let K be a perfectoid field with tilt K_<sup>_♭_</sup> _. Then the continuous valuations | · | of K (up to equivalence) are mapped bijectively to the continuous valuations | · |_<sup>_♭_</sup> _of K_<sup>_♭_</sup> _(up to equivalence) via |x|_<sup>_♭_</sup> = _|x_<sup>_♯_</sup> _|._ 

_Proof._ First, we check that the map _| · | �→| · |_<sup>_♭_</sup> maps valuations to valuations. All properties except _|x_ + _y|_<sup>_♭_</sup> _≤_ max( _|x|_<sup>_♭_</sup> _, |y|_<sup>_♭_</sup> ) are immediate, using that _x �→ x_<sup>_♯_</sup> is multiplicative. But 



It is clear that continuity is preserved. 

On the other hand, continuous valuations are in bijection with open valuation subrings _K_<sup>+</sup> _⊂ K_<sup>_◦_</sup> . They necessarily contain the topologically nilpotent elements m. We see that open valuation subrings _K_<sup>+</sup> _⊂ K_<sup>_◦_</sup> are in bijection with valuation subrings in _K_<sup>_◦_</sup> _/_ m = _K_<sup>_♭◦_</sup> _/_ m<sup>_♭_</sup> . This implies that one gets a bijection with continuous valuations of _K_ and continuous valuations of _K_<sup>_♭_</sup> which is easily seen to be the one described. □ 

The main theorem about tilting for perfectoid fields is the following theorem. For many fields, this was known by the classical work of Fontaine-Wintenberger. 

**Theorem 3.7.** _Let K be a perfectoid field._ 

(i) _Let L be a finite extension of K. Then L (with its natural topology as a finitedimensional K-vector space) is a perfectoid field._ 

(ii) _Let K_<sup>_♭_</sup> _be the tilt of K. Then the tilting functor L �→ L_<sup>_♭_</sup> _induces an equivalence of categories between the category of finite extensions of K and the category of finite extensions of K_<sup>_♭_</sup> _. This equivalence preserves degrees._ 

It turns out that many of the arguments will generalize directly to the context of perfectoid _K_ -algebras introduced later. For this reason, we defer the proof of this theorem. Let us only prove the following special case here. 

**Proposition 3.8.** _Let K be a perfectoid field with tilt K_<sup>_♭_</sup> _. If K_<sup>_♭_</sup> _is algebraically closed,_ 

_then K is algebraically closed._ 

_Proof._ Let _P_ ( _X_ ) = _X_<sup>_d_</sup> + _ad−_ 1 _X_<sup>_d−_1</sup> + _. . ._ + _a_ 0 _∈ K_<sup>_◦_</sup> [ _X_ ] be any monic irreducible polynomial of positive degree _d_ . Then the Newton polygon of _P_ is a line. Moreover, we may assume that the constant term of _P_ has absolute value _|a_ 0 _|_ = 1, as _|K_<sup>_×_</sup> _|_ = _|K_<sup>_♭×_</sup> _|_ is a Q-vector space. 

Now let _Q_ ( _X_ ) = _X_<sup>_d_</sup> + _bd−_ 1 _X_<sup>_d−_1</sup> + _. . ._ + _b_ 0 _∈ K_<sup>_♭◦_</sup> [ _X_ ] be any polynomial such that _P_ and _Q_ have the same image in _K_<sup>_◦_</sup> _/ϖ_ [ _X_ ] = _K_<sup>_♭◦_</sup> _/ϖ_<sup>_♭_</sup> [ _X_ ], and let _y ∈ K_<sup>_♭◦_</sup> be a root of _Q_ . 

PETER SCHOLZE 

18 

Considering _P_ ( _X_ + _y_<sup>_♯_</sup> ), we see that the constant term _P_ ( _y_<sup>_♯_</sup> ) is divisible by _ϖ_ . As it is still irreducible, its Newton polygon is a line and hence the polynomial _P_ 1( _X_ ) = _c_<sup>_−d_</sup> _P_ ( _cX_ + _y_<sup>_♯_</sup> ) has integral coefficients again, where _|c|_<sup>_d_</sup> = _|P_ ( _y_<sup>_♯_</sup> ) _| ≤|ϖ|_ . Repeating the arguments gives an algorithm converging to a root of _P_ . □ 

Our proof of Theorem 3.7 will make use of Faltings’s almost mathematics. For this reason, we recall some necessary background in the next section. 

# 4. Almost mathematics 

We will use the book of Gabber-Ramero, [14], as our basic reference. 

Fix a perfectoid field _K_ . Let m = _K_<sup>_◦◦_</sup> _⊂ K_<sup>_◦_</sup> be the subset of topologically nilpotent elements; it is also the set _{x ∈ K | |x| <_ 1 _}_ , and the unique maximal ideal of _K_<sup>_◦_</sup> . The basic idea of almost mathematics is that one neglects m-torsion everywhere. 

**Definition 4.1.** _Let M be a K_<sup>_◦_</sup> _-module. An element x ∈ M is almost zero if_ m _x_ = 0 _. The module M is almost zero if all of its elements are almost zero; equivalently,_ m _M_ = 0 _._ 

**Lemma 4.2.** _The full subcategory of almost zero objects in K_<sup>_◦_</sup> _−_ mod _is thick._ 

_Proof._ The only nontrivial part is to show that it is stable under extensions, so let 



be a short exact sequence of _K_<sup>_◦_</sup> -modules, with m _M_<sup>_′_</sup> = m _M_<sup>_′′_</sup> = 0. In general, one gets that m<sup>2</sup> _M_ = 0. But in our situation, m<sup>2</sup> = m, so _M_ is almost zero. □ 

We note that there is a sequence of localization functors 



Their composite is the functor of passing from an integral structure to its generic fibre. In this sense, the category in the middle can be seen as a slightly generic fibre, or as an almost integral structure. It will turn out that in perfectoid situations, properties and objects over the generic fibre will extend automatically to the slightly generic fibre, in other words the generic fibre almost determines the integral level. It will be easy to justify this philosophy if _K_ has characteristic _p_ , by using the following argument. Assume that some statement is true over _K_ . By using some finiteness property, it follows that there is some big _N_ such that it is true up to _ϖ_<sup>_N_</sup> -torsion. But Frobenius is bijective, hence the property stays true up to _ϖ_<sup>_N/p_</sup> -torsion. Now iterate this argument to see that it is true up to _ϖ_<sup>_N/pm_</sup> -torsion for all _m_ , i.e. almost true. 

Following these ideas, our proof of Theorem 3.7 will proceed as follows, using the subscript f´et to denote categories of finite ´etale (almost) algebras. 



Our principal aim in this section is to define all intermediate categories. 

**Definition 4.3.** _Define the category of almost K_<sup>_◦_</sup> _-modules as_ 

_K_<sup>_◦a_</sup> _−_ mod = _K_<sup>_◦_</sup> _−_ mod _/_ (m _−_ torsion) _._ 

_In particular, there is a localization functor M �→ M_<sup>_a_</sup> _from K_<sup>_◦_</sup> _−_ mod _to K_<sup>_◦a_</sup> _−_ mod _, whose kernel is exactly the thick subcategory of almost zero modules._ 

**Proposition 4.4** ([14, _§_ 2.2.2]) **.** _Let M , N be two K_<sup>_◦_</sup> _-modules. Then_ 



_In particular,_ Hom _K◦a_ ( _X, Y_ ) _has a natural structure of K_<sup>_◦_</sup> _-module for any two K_<sup>_◦a_</sup> _- modules X and Y . The module_ Hom _K◦a_ ( _X, Y_ ) _has no almost zero elements._ 

For two _K_<sup>_◦a_</sup> -modules _M_ , _N_ , we define alHom( _X, Y_ ) = Hom( _X, Y_ )<sup>_a_</sup> . 

PERFECTOID SPACES 

19 

**Proposition 4.5** ([14, _§_ 2.2.6, _§_ 2.2.12]) **.** _The category K_<sup>_◦a_</sup> _−_ mod _is an abelian tensor category, where we define kernels, cokernels and tensor products in the unique way compatible with their definition in K_<sup>_◦_</sup> _−_ mod _, e.g._ 

_M_<sup>_a_</sup> _⊗ N_<sup>_a_</sup> = ( _M ⊗ N_ )<sup>_a_</sup> 

_for any two K_<sup>_◦_</sup> _-modules M , N . For any three K_<sup>_◦a_</sup> _-modules L, M, N , there is a functorial isomorphism_ 

Hom( _L,_ alHom( _M, N_ )) = Hom( _L ⊗ M, N_ ) _._ 

This means that _K_<sup>_◦a_</sup> _−_ mod has all abstract properties of the category of modules over a ring. In particular, one can define in the usual abstract way the notion of a _K_<sup>_◦a_</sup> -algebra. For any _K_<sup>_◦a_</sup> -algebra _A_ , one also has the notion of an _A_ -module. Any _K_<sup>_◦_</sup> - algebra _R_ defines a _K_<sup>_◦a_</sup> -algebra _R_<sup>_a_</sup> , as the tensor products are compatible. Moreover, localization also gives a functor from _R_ -modules to _R_<sup>_a_</sup> -modules. For example, _K_<sup>_◦_</sup> gives the _K_<sup>_◦a_</sup> -algebra _A_ = _K_<sup>_◦a_</sup> , and then _A_ -modules are _K_<sup>_◦a_</sup> -modules, so that the terminology is consistent. 

**Proposition 4.6** ([14, Proposition 2.2.14]) **.** _There is a right adjoint_ 



_to the localization functor M �→ M_<sup>_a_</sup> _, given by the functor of almost elements_ 

_M∗_ = Hom _K◦a_ ( _K_<sup>_◦a_</sup> _, M_ ) _._ 

_The adjunction morphism_ ( _M∗_ )<sup>_a_</sup> _→ M is an isomorphism. If M is a K_<sup>_◦_</sup> _-module, then_ ( _M_<sup>_a_</sup> ) _∗_ = Hom(m _, M_ ) _._ 

If _A_ is a _K_<sup>_◦a_</sup> -algebra, then _A∗_ has a natural structure as _K_<sup>_◦_</sup> -algebra and _A_<sup>_a_</sup> _∗_<sup>=</sup><sup>_A_.</sup> In particular, any _K_<sup>_◦a_</sup> -algebra comes via localization from a _K_<sup>_◦_</sup> -algebra. Moreover, the functor _M �→ M∗_ induces a functor from _A_ -modules to _A∗_ -modules, and one sees that also all _A_ -modules come via localization from _A∗_ -modules. We note that the category of _A_ -modules is again an abelian tensor category, and all properties about the category of _K_<sup>_◦a_</sup> -modules stay true for the category of _A_ -modules. We also note that one can equivalently define _A_ -algebras as algebras over the category of _A_ -modules, or as _K_<sup>_◦a_</sup> - algebras _B_ with an algebra morphism _A → B_ . 

Finally, we need to extend some notions from commutative algebra to the almost context. 

**Definition/Proposition 4.7.** _Let A be any K_<sup>_◦a_</sup> _-algebra._ 

(i) _An A-module M is flat if the functor X �→ M ⊗A X on A-modules is exact. If R is a K_<sup>_◦_</sup> _-algebra and N is an R-module, then the R_<sup>_a_</sup> _-module N_<sup>_a_</sup> _is flat if and only if for all R-modules X and all i >_ 0 _, the module_ Tor<sup>_R_</sup> _i_<sup>(</sup><sup>_N, X_)</sup><sup>_isalmostzero._</sup> 

(ii) _An A-module M is almost projective if the functor X �→_ alHom _A_ ( _M, X_ ) _on A- modules is exact. If R is a K_<sup>_◦_</sup> _-algebra and N is an R-module, then N_<sup>_a_</sup> _is almost projective over R_<sup>_a_</sup> _if and only if for all R-modules X and all i >_ 0 _, the module_ Ext<sup>_i_</sup> _R_<sup>(</sup><sup>_N, X_)</sup> _is almost zero._ 

(iii) _If R is a K_<sup>_◦_</sup> _-algebra and N is an R-module, then M_ = _N_<sup>_a_</sup> _is said to be an almost finitely generated (resp. almost finitely presented) R_<sup>_a_</sup> _-module if and only if for all ϵ ∈_ m _, there is some finitely generated (resp. finitely presented) R-module Nϵ with a map fϵ_ : _Nϵ → N such that the kernel and cokernel of fϵ are annihilated by ϵ. We say that M is uniformly almost finitely generated if there is some integer n such that Nϵ can be chosen to be generated by n elements, for all ϵ._ 

_Proof._ For parts (i) and (ii), cf. [14], Definition 2.4.4, _§_ 2.4.10 and Remark 2.4.12 (i). For part (iii), cf. [14], Definition 2.3.8, Remark 2.3.9 (i) and Corollary 2.3.13. □ 

PETER SCHOLZE 

20 

_Remark_ 4.8 _._ In (iii), we make the implicit statement that this property depends only on the _R_<sup>_a_</sup> -module _N_<sup>_a_</sup> . There is also the categorical notion of projectivity saying that the functor _X �→_ Hom( _M, X_ ) is exact, but not even _K_<sup>_◦a_</sup> itself is projective in general: One can check that the map 

_K_<sup>_◦_</sup> = Hom( _K_<sup>_◦a_</sup> _, K_<sup>_◦a_</sup> ) _→_ Hom( _K_<sup>_◦a_</sup> _, K_<sup>_◦a_</sup> _/ϖ_ ) = Hom(m _, K_<sup>_◦_</sup> _/ϖ_ ) 

is in general not surjective, as the latter group contains sums of the form 



for arbitrary _xi ∈ K_<sup>_◦_</sup> _/ϖ_ . 

_Example_ 4.9 _._ As an example of an almost finitely presented module, consider the case that _K_ is the _p_ -adic completion of Q _p_ ( _p_<sup>1</sup><sup>_/p∞_</sup> ), _p̸_ = 2. Consider the extension _L_ = _K_ ( _p_<sup>1</sup><sup>_/_2</sup> ). Then _L_<sup>_◦a_</sup> is an almost finitely presented _K_<sup>_◦a_</sup> -module. Indeed, for any _n ≥_ 1, we have injective maps 



whose cokernel is killed by _p_<sup>1</sup><sup>_/_2</sup><sup>_pn_</sup> . In fact, in this example _L_<sup>_◦a_</sup> is even uniformly almost finitely generated. 

**Proposition 4.10** ([14, Proposition 2.4.18]) **.** _Let A be a K_<sup>_◦a_</sup> _-algebra. Then an A- module M is flat and almost finitely presented if and only if it is almost projective and almost finitely generated._ 

By abuse of notation, we call such _A_ -modules _M_ finite projective in the following, a terminology not used in [14]. If additionally, _M_ is uniformly almost finitely generated, we say that _M_ is uniformly finite projective. 

For uniformly finite projective modules, there is a good notion of rank. 

**Theorem 4.11** ([14, Proposition 4.3.27, Remark 4.3.10 (i)]) **.** _Let A be a K_<sup>_◦a_</sup> _-algebra, and let M be a uniformly finite projective A-module. Then there is a unique decomposition A_ = _A_ 0 _×A_ 1 _×· · ·×Ak such that for each i_ = 0 _, . . . , k, the Ai-module Mi_ = _M ⊗A Ai has the property that_<sup>�</sup><sup>_i_</sup> _Mi is invertible, and_<sup>�</sup><sup>_i_+1</sup> _Mi_ = 0 _. Here, an A-module L is called invertible if L ⊗A_ alHom _A_ ( _L, A_ ) = _A._ 

Finally, we need the notion of ´etale morphisms. 

**Definition 4.12.** _Let A be a K_<sup>_◦a_</sup> _-algebra, and let B be an A-algebra. Let µ_ : _B ⊗A B → B denote the multiplication morphism._ 

(i) _The morphism A → B is said to be unramified if there is some element e ∈_ ( _B ⊗A B_ ) _∗ such that e_<sup>2</sup> = _e, µ_ ( _e_ ) = 1 _and xe_ = 0 _for all x ∈_ ker( _µ_ ) _∗._ 

(ii) _The morphism A → B is said to be ´etale if it is unramified and B is a flat A-module._ 

We note that the definition of unramified morphisms basically says that the diagonal morphism _µ_ : _B ⊗A B → B_ is a closed immersion in the geometric picture. 

In the following, we will be particularly interested in almost finitely presented ´etale maps. 

**Definition 4.13.** _A morphism A → B of K_<sup>_◦a_</sup> _-algebras is said to be finite ´etale if it is ´etale and B is an almost finitely presented A-module. Write A_ f´et _for the category of finite ´etale A-algebras._ 

We note that in this case _B_ is a finite projective _A_ -module. Also, this terminology is not used in [14], but we feel that it is the appropriate almost analogue of finite ´etale covers. 

There is an equivalent characterization of finite ´etale morphisms in terms of trace morphisms. If _A_ is any _K_<sup>_◦a_</sup> -algebra, and _P_ is some finite projective _A_ -module, we define 

PERFECTOID SPACES 21 

_P_<sup>_∗_</sup> = alHom( _P, A_ ), which is a finite projective _A_ -module again. Moreover, _P_<sup>_∗∗∼_</sup> = _P_ canonically, and there is an isomorphism 



In particular, one gets a trace morphism tr _P/A_ : End( _P_ )<sup>_a_</sup> _→ A_ . 

**Definition 4.14.** _Let A be a K_<sup>_◦a_</sup> _-algebra, and let B be an A-algebra such that B is a finite projective A-module. Then we define the trace form as the bilinear form_ 



_given by the composition of µ_ : _B ⊗A B → B and the map B → A sending any b ∈ B to the trace of the endomorphism b_<sup>_′_</sup> _�→ bb_<sup>_′_</sup> _of B._ 

_Remark_ 4.15 _._ We should remark that the latter definition does not literally make sense, as one can not talk about an element _b_ of some almost object _B_ : There is no underlying set. However, one can define a map _B∗ →_ End _A∗_ ( _B∗_ ) in the way described, and we are considering the corresponding map of almost objects _B →_ End _A∗_ ( _B∗_ )<sup>_a_</sup> = End _A_ ( _B_ )<sup>_a_</sup> . 

**Theorem 4.16** ([14, Theorem 4.1.14]) **.** _In the situation of the definition, the morphism A → B is finite ´etale if and only if the trace map is a perfect pairing, i.e. induces an isomorphism B_<sup>_∼_</sup> = _B_<sup>_∗_</sup> _._ 

An important property is that finite ´etale covers lift uniquely over nilpotents. 

**Theorem 4.17.** _Let A be a K_<sup>_◦a_</sup> _-algebra. Assume that A is flat over K_<sup>_◦a_</sup> _and ϖ-adically complete, i.e._ 



_Then the functor B �→ B ⊗A A/ϖ induces an equivalence of categories A_ f´et<sup>_∼_</sup> = ( _A/ϖ_ )f´et _. Any B ∈ A_ f´et _is again flat over K_<sup>_◦a_</sup> _and ϖ-adically complete. Moreover, B is a uniformly finite projective A-module if and only if B ⊗A A/ϖ is a uniformly finite projective A/ϖ-module._ 

_Proof._ The first part follows from [14], Theorem 5.3.27. The rest is easy. □ 

Recall that we wanted to prove the string of equivalences 



The identification in the middle is tautological as _K_<sup>_◦_</sup> _/ϖ_ = _K_<sup>_♭◦_</sup> _/ϖ_<sup>_♭_</sup> , and the corresponding almost settings agree. The previous theorem shows that the inner two functors are equivalences. For the other two equivalences, we feel that it is more convenient to study them in the more general setup of perfectoid _K_ -algebras. 



Fix a perfectoid field _K_ . 

**Definition 5.1.** (i) _A perfectoid K-algebra is a Banach K-algebra R such that the subset R_<sup>_◦_</sup> _⊂ R of powerbounded elements is open and bounded, and the Frobenius morphism_ Φ : _R_<sup>_◦_</sup> _/ϖ → R_<sup>_◦_</sup> _/ϖ is surjective. Morphisms between perfectoid K-algebras are the continuous morphisms of K-algebras._ 

(ii) _A perfectoid K_<sup>_◦a_</sup> _-algebra is a ϖ-adically complete flat K_<sup>_◦a_</sup> _-algebra A on which Frobenius induces an isomorphism_ 



_Morphisms between perfectoid K_<sup>_◦a_</sup> _-algebras are the morphisms of K_<sup>_◦a_</sup> _-algebras._ 

PETER SCHOLZE 

22 

(iii) _A perfectoid K_<sup>_◦a_</sup> _/ϖ-algebra is a flat K_<sup>_◦a_</sup> _/ϖ-algebra A on which Frobenius induces an isomorphism_ 



_Morphisms are the morphisms of K_<sup>_◦a_</sup> _/ϖ-algebras._ 

Let _K−_ Perf denote the category of perfectoid _K_ -algebras, and similarly for _K_<sup>_◦a_</sup> _−_ Perf, ... . Let _K_<sup>_♭_</sup> be the tilt of _K_ . Then the main theorem of this section is the following. **Theorem 5.2.** _The categories of perfectoid K-algebras and perfectoid K_<sup>_♭_</sup> _-algebras are equivalent. In fact, we have the following series of equivalences of categories._ 

_K −_ Perf<sup>_∼_</sup> = _K_<sup>_◦a_</sup> _−_ Perf<sup>_∼_</sup> = ( _K_<sup>_◦a_</sup> _/ϖ_ ) _−_ Perf = ( _K_<sup>_♭◦a_</sup> _/ϖ_<sup>_♭_</sup> ) _−_ Perf<sup>_∼_</sup> = _K_<sup>_♭◦a_</sup> _−_ Perf<sup>_∼_</sup> = _K_<sup>_♭_</sup> _−_ Perf 

In other words, a perfectoid _K_ -algebra, which is an object over the generic fibre, has a canonical extension to the almost integral level as a perfectoid _K_<sup>_◦a_</sup> -algebra, and perfectoid _K_<sup>_◦a_</sup> -algebras are determined by their reduction modulo _ϖ_ . 

The following lemma expresses the conditions imposed on a perfectoid _K_<sup>_◦a_</sup> -algebra in terms of classical commutative algebra. 

**Lemma 5.3.** _Let M be a K_<sup>_◦a_</sup> _-module._ 

(i) _The module M is flat over K_<sup>_◦a_</sup> _if and only if M∗ is flat over K_<sup>_◦_</sup> _if and only if M∗ has no ϖ-torsion._ 

(ii) _If N is a flat K_<sup>_◦_</sup> _-module and M_ = _N_<sup>_a_</sup> _, then M is flat over K_<sup>_◦a_</sup> _and we have M∗_ = _{x ∈ N_ [ _ϖ_<sup><u>1</u>]</sup><sup>_| ∀ϵ ∈_m :</sup><sup>_ϵx ∈N}._</sup> 

(iii) _If M is flat over K_<sup>_◦a_</sup> _, then for all x ∈ K_<sup>_◦_</sup> _, we have_ ( _xM_ ) _∗_ = _xM∗. Moreover, M∗/xM∗ ⊂_ ( _M/xM_ ) _∗, and for all ϵ ∈_ m _the image of_ ( _M/xϵM_ ) _∗ in_ ( _M/xM_ ) _∗ is equal to M∗/xM∗._ 

(iv) _If M is flat over K_<sup>_◦a_</sup> _, then M is ϖ-adically complete if and only if M∗ is ϖ-adically complete._ 

_Remark_ 5.4 _._ The non-surjectivity in (iii) is due to elements as in Remark 4.8. 

_Proof._ (i) By definition, _M_ is a flat _K_<sup>_◦a_</sup> -module if and only if all Tor<sup>_K_</sup> _i_<sup>_◦_</sup> ( _M∗, N_ ) are almost zero for all _i >_ 0 and all _K_<sup>_◦_</sup> -modules _N_ . Hence if _M∗_ is a flat _K_<sup>_◦_</sup> -module, then _M_ is a flat _K_<sup>_◦a_</sup> -module. Conversely, choosing _N_ = _K_<sup>_◦_</sup> _/ϖ_ and _i_ = 1, we find that the kernel of multiplication by _ϖ_ on _M∗_ is almost zero. But 



does not have nontrivial almost zero elements, hence has no _ϖ_ -torsion. But a _K_<sup>_◦_</sup> -module _N_ is flat if and only if it has no _ϖ_ -torsion. 

(ii) We have 



As _N_ is flat over _K_<sup>_◦_</sup> , we can write the last term as the subset of those _x ∈_ Hom _K_ ( _K, N_ [ _ϖ_<sup><u>1</u>]) =</sup> _N_ [ _ϖ_<sup><u>1</u>]satisfyingtheconditionthatforall</sup><sup>_ϵ ∈_m,wehave</sup><sup>_ϵx ∈N_.</sup> 

(iii) Note that ( _xM∗_ )<sup>_a_</sup> = _xM_ , and _xM∗_ is a flat _K_<sup>_◦_</sup> -module. Hence 



Now using that _∗_ is left-exact (since right-adjoint to _M �→ M_<sup>_a_</sup> ), we get the inclusion _M∗/xM∗ ⊂_ ( _M/xM_ ) _∗_ . If _m ∈_ ( _M/xM_ ) _∗_ lifts to _m_ ˜ _∈_ ( _M/xϵM_ ) _∗_ , then evaluate _m_ ˜ _∈_ Hom(m _, M∗/xϵM∗_ ) on _ϵ_ . This gives an element _n_ = _m_ ˜ ( _ϵ_ ) _∈ M∗/xϵM∗_ , which we lift to _n_ ˜ _∈ M∗_ . One checks that _n_ ˜ is divisible by _ϵ_ : It suffices to check that _δn_ ˜ is divisible by _ϵ_ for any _δ ∈_ m. But _δn_ = _δ_ ˜ _m_ ( _ϵ_ ) = _ϵm_ ˜ ( _δ_ ) lies in _ϵM∗/xϵM∗_ , hence _δn_ ˜ _∈ ϵM∗_ . 

PERFECTOID SPACES 

23 

Then _m_ 1 =<sup>_<u>n</u>_˜</sup> _ϵ_<sup>_∈M∗_isthedesiredliftof</sup><sup>_m ∈_(</sup><sup>_M/xM_)</sup><sup>_∗_:Multiplicationby</sup><sup>_ϵ_induces</sup> an injection ( _M/xM_ ) _∗ →_ ( _M/xϵM_ ) _∗_ , because _∗_ is left-exact, and the images agree: _n_ ˜ maps to _ϵm_ = _m_ ˜ ( _ϵ_ ) = _n_ in ( _M/xϵM_ ) _∗_ . 

(iv) The functors _M �→ M∗_ and _N �→ N_<sup>_a_</sup> between the category of _K_<sup>_◦a_</sup> -modules and the category of _K_<sup>_◦_</sup> -modules admit left adjoints, given by _N �→ N_<sup>_a_</sup> and _M �→ M_ ! = m _⊗ M∗_ , respectively, and hence commute with inverse limits. Now if _M_ is _ϖ_ -adically complete, then 



using part (iii) in the last equality, hence _M∗_ is _ϖ_ -adically complete. Conversely, if _M∗_ is _ϖ_ -adically complete, then 



**Proposition 5.5.** _Let R be a perfectoid K-algebra. Then_ Φ _induces an isomorphism R_<sup>_◦_</sup> _/ϖ_<sup>1</sup><sup>_/p∼_</sup> = _R_<sup>_◦_</sup> _/ϖ, and A_ = _R_<sup>_◦a_</sup> _is a perfectoid K_<sup>_◦a_</sup> _-algebra._ 

_Proof._ By assumption, Φ is surjective. Injectivity is clear: If _x ∈ R_<sup>_◦_</sup> is such that _x_<sup>_p_</sup> _/ϖ_ is powerbounded, then _x/ϖ_<sup>1</sup><sup>_/p_</sup> is powerbounded. Obviously, _R_<sup>_◦_</sup> is _ϖ_ -adically complete and flat over _K_<sup>_◦_</sup> ; now the previous lemma shows that _R_<sup>_◦a_</sup> is _ϖ_ -adically complete and flat over _K_<sup>_◦a_</sup> . □ 

**Lemma 5.6.** _Let A be a perfectoid K_<sup>_◦a_</sup> _-algebra, and let R_ = _A∗_ [ _ϖ_<sup>_−_1</sup> ] _. Equip R with the Banach K-algebra structure making A∗ open and bounded. Then A∗_ = _R_<sup>_◦_</sup> _is the set of power-bounded elements, R is perfectoid, and_ 



_Proof._ By definition, Φ is an isomorphism _A/ϖ_<sup>1</sup><sup>_/p∼_</sup> = _A/ϖ_ , hence Φ is an almost isomorphism _A∗/ϖ_<sup>1</sup><sup>_/p_</sup> _→ A∗/ϖ_ . It is injective: If _x ∈ A∗_ and _x_<sup>_p_</sup> _∈ ϖA∗_ , then for all _ϵ ∈_ m, _ϵx ∈ ϖ_<sup>1</sup><sup>_/p_</sup> _A∗_ by almost injectivity, hence _x ∈_ ( _ϖ_<sup>1</sup><sup>_/p_</sup> _A_ ) _∗_ = _ϖ_<sup>1</sup><sup>_/p_</sup> _A∗_ . 

**Lemma 5.7.** _Assume that x ∈ R satisfies x_<sup>_p_</sup> _∈ A∗. Then x ∈ A∗._ 

<u>1</u> _Proof._ Injectivity of Φ says that if _y ∈ A∗_ satisfies _y_<sup>_p_</sup> _∈ ϖA∗_ , then _y ∈ ϖ p A∗_ . There is _<u>k</u>_ some positive integer _k_ such that _y_ = _ϖ p x ∈ A∗_ , and as long as _k ≥_ 1, _y_<sup>_p_</sup> _∈ ϖA∗_ , so <u>1</u> _<u>k−</u>_ <u>1</u> that _y ∈ ϖ p A∗_ . Because _A∗_ has no _ϖ_ -torsion, we get _ϖ p x ∈ A∗_ . By induction, we get the result. □ 

Obviously, _A∗_ consists of power-bounded elements. Now assume that _x ∈ R_ is powerbounded. Then _ϵx_ is topologically nilpotent for all _ϵ ∈_ m. In particular, ( _ϵx_ )<sup>_pN_</sup> _∈ A∗_ for _N_ sufficiently large. By the last lemma, this implies _ϵx ∈ A∗_ . This is true for all _ϵ ∈_ m, so that by Lemma 5.3 (ii), we have _x ∈ A∗_ . 

Next, Φ is surjective: It is almost surjective, hence it suffices to show that the composition _A∗/ϖ_<sup>1</sup><sup>_/p_</sup> _→ A∗/ϖ → A∗/_ m is surjective. Let _x ∈ A∗_ . By almost surjectivity, _ϖ_<sup>1</sup><sup>_/p_</sup> _x ≡ y_<sup>_p_</sup> modulo _ϖA∗_ , for some _y ∈ A∗_ . Let _z_ = _ϖ_<sup>1</sup> _<u>y</u>_<sup>_/p_2.Thisimplies</sup><sup>_zp≡x_modulo</sup> _ϖ_<sup>(</sup><sup>_p−_1)</sup><sup>_/p_</sup> _A∗_ , in particular _z_<sup>_p_</sup> _∈ A∗_ . By the lemma, also _z ∈ A∗_ . As _x ≡ z_<sup>_p_</sup> modulo _ϖ_<sup>(</sup><sup>_p−_1)</sup><sup>_/p_</sup> _A∗_ , in particular modulo m _A∗_ , this gives the desired surjectivity. Finally, we see that _R_ is Banach _K_ -algebra such that _R_<sup>_◦_</sup> = _A∗_ is open and bounded, and such that Φ is surjective on _R_<sup>_◦_</sup> _/ϖ_ = _A∗/ϖ_ . This means that _R_ is perfectoid, as desired. □ 

In particular, we get the desired equivalence _K_<sup>_◦a_</sup> _−_ Perf<sup>_∼_</sup> = _K −_ Perf. Let us note some further propositions. 

**Proposition 5.8.** _Let R be a perfectoid K-algebra. Then R is reduced._ 

PETER SCHOLZE 

24 

_Proof._ Assume 0 _̸_ = _x ∈ R_ is nilpotent. Then _Kx ⊂ R_<sup>_◦_</sup> , contradicting the condition that _R_<sup>_◦_</sup> is bounded. □ 

If _K_ has characteristic _p_ , being perfectoid is basically the same as being perfect. 

**Proposition 5.9.** _Let K be of characteristic p, and let R be a Banach K-algebra such that the set of powerbounded elements R_<sup>_◦_</sup> _⊂ R is open and bounded. Then R is perfectoid if and only if R is perfect._ 

_Proof._ Assume _R_ is perfect. Then also _R_<sup>_◦_</sup> is perfect, as an element _x_ is powerbounded if and only if _x_<sup>_p_</sup> is powerbounded. In particular, Φ : _R_<sup>_◦_</sup> _/ϖ → R_<sup>_◦_</sup> _/ϖ_ is surjective. 

Now assume that _R_ is perfectoid, hence by Proposition 5.5, Φ induces an isomorphism <u>1</u> _R_<sup>_◦_</sup> _/ϖ p ∼_ = _R_<sup>_◦_</sup> _/ϖ_ . By successive approximation, we see that _R_<sup>_◦_</sup> is perfect, and then that _R_ is perfect. □ 

In order to finish the proof of Theorem 5.2, it suffices to prove the following result. **Theorem 5.10.** _The functor A �→ A_ = _A/ϖ induces an equivalence of categories K_<sup>_◦a_</sup> _−_ Perf<sup>_∼_</sup> = ( _K_<sup>_◦a_</sup> _/ϖ_ ) _−_ Perf _._ 

In other words, we have to prove that a perfectoid _K_<sup>_◦a_</sup> _/ϖ_ -algebra admits a unique deformation to _K_<sup>_◦a_</sup> . For this, we will use the theory of the cotangent complex. Let us briefly recall it here. 

In classical commutative algebra, the definition of the cotangent complex is due to Quillen, [28], and its theory was globalized on toposes and applied to deformation problems by Illusie, [22], [23]. To any morphism _R → S_ of rings, one associates a complex L _S/R ∈ D_<sup>_≤_0</sup> ( _S_ ), where _D_ ( _S_ ) is the derived category of the category of _S_ -modules, and _D_<sup>_≤_0</sup> ( _S_ ) _⊂ D_ ( _S_ ) denotes the full subcategory of objects which have trivial cohomology in positive degrees. The cohomology in degree 0 of L _S/R_ is given by Ω<sup>1</sup> _S/R_<sup>,andforany</sup> morphisms _R → S → T_ of rings, there is a triangle in _D_ ( _T_ ): 



extending the short exact sequence 



Let us briefly recall the construction. First, one uses the Dold-Kan equivalence to reinterpret _D_<sup>_≤_0</sup> ( _S_ ) as the category of simplicial _S_ -modules modulo weak equivalence. Now one takes a simplicial resolution _S•_ of the _R_ -algebra _S_ by free _R_ -algebras. Then one defines L _S/R_ as the object of _D_<sup>_≤_0</sup> ( _S_ ) associated to the simplicial _S_ -module Ω<sup>1</sup> _S•/R_<sup>_⊗S•S_.</sup> 

Just as under certain favorable assumptions, one can describe many deformation problems in terms of tangent or normal bundles, it turns out that in complete generality, one can describe them via the cotangent complex. In special cases, this gives back the classical results, as e.g. if _R → S_ is a smooth morphism, then L _S/R_ is concentrated in degree 0, and is given by the cotangent bundle. 

Specifically, we will need the following results. Fix some ring _R_ with an ideal _I ⊂ R_ such that _I_<sup>2</sup> = 0. Moreover, fix a flat _R_ 0 = _R/I_ -algebra _S_ 0. We are interested in the obstruction towards deforming _S_ 0 to a flat _R_ -algebra _S_ . 

**Theorem 5.11** ([22, III.2.1.2.3], [14, Proposition 3.2.9]) **.** _There is an obstruction class in_ Ext<sup>2</sup> (L _S_ 0 _/R_ 0 _, S_ 0 _⊗R_ 0 _I_ ) _which vanishes precisely when there exists a flat R-algebra S such that S ⊗R R_ 0 = _S_ 0 _. If there exists such a deformation, then the set of all isomorphism classes of such deformations forms a torsor under_ Ext<sup>1</sup> (L _S_ 0 _/R_ 0 _, S_ 0 _⊗R_ 0 _I_ ) _, and every deformation has automorphism group_ Hom(L _S_ 0 _/R_ 0 _, S_ 0 _⊗R_ 0 _I_ ) _._ 

PERFECTOID SPACES 

25 

Here, a deformation comes with the isomorphism _S ⊗R R_ 0<sup>_∼_</sup> = _S_ 0, and isomorphisms of deformations are required to act trivially on _S ⊗R R_ 0 = _S_ 0. 

Now assume that one has two flat _R_ -algebras _S_ , _S_<sup>_′_</sup> with reduction _S_ 0, _S_ 0<sup>_′_to</sup><sup>_R_0, and a</sup> morphism _f_ 0 : _S_ 0 _→ S_ 0<sup>_′_.We are interested in the obstruction to lifting</sup><sup>_f_0to a morphism</sup> _f_ : _S → S_<sup>_′_</sup> . 

**Theorem 5.12** ([22, III.2.2.2], [14, Proposition 3.2.16]) **.** _There is an obstruction class in_ Ext<sup>1</sup> (L _S_ 0 _/R_ 0 _, S_ 0<sup>_′⊗R_</sup> 0<sup>_I_)</sup><sup>_whichvanishespreciselywhenthereexistsanextensionoff_0</sup> _to f_ : _S → S_<sup>_′_</sup> _. If there exists such a lift, then the set of all lifts forms a torsor under_ Hom(L _S_ 0 _/R_ 0 _, S_ 0<sup>_′⊗R_</sup> 0<sup>_I_)</sup><sup>_._</sup> 

We will need the following criterion for the vanishing of the cotangent complex. This appears as Lemma 6.5.13 i) in [14]. 

**Proposition 5.13.** (i) _Let R be a perfect_ F _p-algebra. Then_ L _R/_ F _p_<sup>_∼_</sup> = 0 _._ 

(ii) _Let R → S be a morphism of_ F _p-algebras. Let R_ (Φ) _be the ring R with the R-algebra structure via_ Φ : _R → R, and define S_ (Φ) _similarly. Assume that the relative Frobenius_ Φ _S/R induces an isomorphism_ 



_in D_ ( _R_ ) _. Then_ L _S/R_<sup>_∼_</sup> = 0 _._ 

_Remark_ 5.14 _._ Of course, (i) is a special case of (ii), and we will only need part (ii). However, we feel that (i) is an interesting statement that does not seem to be very well-known. It allows one to define the ring of Witt vectors _W_ ( _R_ ) of _R_ simply by saying that it is the unique deformation of _R_ to a flat _p_ -adically complete Z _p_ -algebra. Also note that it is clear that Ω<sup>1</sup> _R/_ F _p_<sup>=0inpart(i):Any</sup><sup>_x∈R_canbewrittenas</sup><sup>_yp_,and</sup> then _dx_ = _dy_<sup>_p_</sup> = _py_<sup>_p−_1</sup> _dy_ = 0. This identity is at the heart of this proposition. 

_Proof._ We sketch the proof of part (ii), cf. proof of Lemma 6.5.13 i) in [14]. Let _S_<sup>_•_</sup> be a simplicial resolution of _S_ by free _R_ -algebras. We have the relative Frobenius map 



Note that identifying _S_<sup>_k_</sup> with a polynomial algebra _R_ [ _X_ 1 _, X_ 2 _, . . ._ ], the relative Frobenius map Φ _Sk/R_ is given by the _R_ (Φ)-algebra map sending _Xi �→ Xi_<sup>_p_.</sup> 

The assumption says that Φ _S•/R_ induces a quasiisomorphism of simplicial _R_ (Φ)algebras. This implies that Φ _S•/R_ gives an isomorphism 



On the other hand, the explicit description shows that the map induced by Φ _Sk/R_ on differentials will map _dXi_ to _dXi_<sup>_p_=0,andhenceisthezeromap.Thisshowsthat</sup> L _S_ (Φ) _/R_ (Φ)<sup>_∼_</sup> = 0, and we may identify this with L _S/R_ . □ 

In their book [14], Gabber and Ramero generalize the theory of the cotangent complex to the almost context. Specifically, they show that if _R → S_ is a morphism of _K_<sup>_◦_</sup> - algebras, then L<sup>_a_</sup> _S/R_<sup>as an element of</sup><sup>_D_(</sup><sup>_Sa_), the derived category of</sup><sup>_Sa_-modules, depends</sup> only the morphism _R_<sup>_a_</sup> _→ S_<sup>_a_</sup> of almost _K_<sup>_◦_</sup> -algebras. This allows one to define L<sup>_a_</sup> _B/A_<sup>_∈_</sup> _D_<sup>_≤_0</sup> ( _B_ ) for any morphism _A → B_ of _K_<sup>_◦a_</sup> -algebras. With this modification, the previous theorems stay true in the almost world without change. 

_Remark_ 5.15 _._ In fact, the cotangent complex L _B/A_ is defined as an object of a derived category of modules over an actual ring in [14], but for our purposes it is enough to consider its almost version L<sup>_a_</sup> _B/A_<sup>.</sup> 

**Corollary 5.16.** _Let A be a perfectoid K_<sup>_◦a_</sup> _/ϖ-algebra. Then_ ~~L~~<sup>_a_</sup> _A/_ ( _K_<sup>_◦a_</sup> _/ϖ_ )<sup>_∼_= 0</sup><sup>_._</sup> 

PETER SCHOLZE 

26 

_Proof._ This follows from the almost version of Proposition 5.13, which can be proved in the same way. Alternatively, argue with _B_ = ( _A × K_<sup>_◦a_</sup> _/ϖ_ )!!, which is a flat _K_<sup>_◦_</sup> _/ϖ_ - algebra such that _B/ϖ_<sup>1</sup><sup>_/p∼_</sup> = _B_ via Φ. Here, we use the functor _C �→ C_ !! from [14], _§_ 2.2.25. □ 

Now we can prove Theorem 5.10. 

_Proof._ ( _of Theorem 5.10_ ) Let _A_ be a perfectoid _K_<sup>_◦a_</sup> _/ϖ_ -algebra. We see inductively that all obstructions and ambiguities in lifting inductively to a flat ( _K_<sup>_◦_</sup> _/ϖ_<sup>_n_</sup> )<sup>_a_</sup> -algebra _An_ vanish: All groups occuring can be expressed in terms of the cotangent complex by the theorems above, so that it suffices to show that ~~L~~ _A_<sup>_a_</sup> _n/_ ( _K_<sup>_◦_</sup> _/ϖ_<sup>_n_</sup> )<sup>_a_= 0.ButbyTheorem</sup> 2.5.36 of [14], the short exact sequence 



induces after tensoring with ~~L~~ _An/_ ( _K_<sup>_◦_</sup> _/ϖ_<sup>_n_</sup> )<sup>_a_atriangle</sup> 



and the claim follows by induction. 

This gives a unique system of flat ( _K_<sup>_◦_</sup> _/ϖ_<sup>_n_</sup> )<sup>_a_</sup> -algebras _An_ with isomorphisms 



Let _A_ be their inverse limit. Then _A_ is _ϖ_ -adically complete with _A/ϖ_<sup>_n_</sup> _A_ = _An_ . This shows that _A_ is perfectoid, and we get an equivalence between perfectoid _K_<sup>_◦a_</sup> -algebras and perfectoid _K_<sup>_◦a_</sup> _/ϖ_ -algebras, as desired. □ 

In particular, we also arrive at the tilting equivalence, _K −_ Perf<sup>_∼_</sup> = _K_<sup>_♭_</sup> _−_ Perf. We want to compare this with Fontaine’s construction. Let _R_ be a perfectoid _K_ -algebra, with _A_ = _R_<sup>_◦a_</sup> . Define 



which we regard as a _K_<sup>_♭◦a_</sup> -algebra via 



and set _R_<sup>_♭_</sup> = _A_<sup>_♭_</sup> _∗_<sup>[(</sup><sup>_ϖ♭_)</sup><sup>_−_1].</sup> 

**Proposition 5.17.** _This defines a perfectoid K_<sup>_♭_</sup> _-algebra R_<sup>_♭_</sup> _with corresponding perfectoid K_<sup>_♭◦a_</sup> _-algebra A_<sup>_♭_</sup> _, and R_<sup>_♭_</sup> _is the tilt of R. Moreover,_ 



_In particular, we have a continuous multiplicative map R_<sup>_♭_</sup> _→ R, x �→ x_<sup>_♯_</sup> _._ 

_Remark_ 5.18 _._ It follows that the tilting functor is independent of the choice of _ϖ_ and _ϖ_<sup>_♭_</sup> . We note that this explicit description comes from the fact that the lifting from perfectoid _K_<sup>_♭◦a_</sup> _/ϖ_<sup>_♭_</sup> -algebras to perfectoid _K_<sup>_♭◦a_</sup> -algebras can be made explicit by means of the inverse limit over the Frobenius. 

_Proof._ First, we have 



PERFECTOID SPACES 

27 

because _∗_ commutes with inverse limits and using Lemma 5.3 (iii). Note that the image of Φ : ( _A/ϖ_ ) _∗ →_ ( _A/ϖ_ ) _∗_ is _A∗/ϖ_ , because it factors over ( _A/ϖ_<sup>1</sup><sup>_/p_</sup> ) _∗_ , and the image of the projection ( _A/ϖ_ ) _∗ →_ ( _A/ϖ_<sup>1</sup><sup>_/p_</sup> ) _∗_ is _A∗/ϖ_<sup>1</sup><sup>_/p_</sup> . But 



as in the proof of Lemma 3.4 (i). 

This shows that _A_<sup>_♭_</sup> _∗_<sup>isa</sup><sup>_ϖ♭_-adicallycompleteflat</sup><sup>_K♭◦_-algebra.Moreover,theprojec-</sup> tion _x �→ x_<sup>_♯_</sup> of _A_<sup>_♭_</sup> _∗_<sup>ontothefirstcomponent</sup><sup>_x♯∈A∗_inducesanisomorphism</sup> 



because of Lemma 5.6. Therefore _A_<sup>_♭_</sup> is a perfectoid _K_<sup>_♭◦a_</sup> -algebra. 

To see that _R_<sup>_♭_</sup> is the tilt of _R_ , we go through all equivalences. Indeed, _R_ has corresponding perfectoid _K_<sup>_◦a_</sup> -algebra _A_ , which reduces to the perfectoid _K_<sup>_◦a_</sup> _/ϖ_ -algebra _A/ϖ_ , which is the same as the perfectoid _K_<sup>_♭◦a_</sup> _/ϖ_<sup>_♭_</sup> -algebra _A_<sup>_♭_</sup> _/ϖ_<sup>_♭_</sup> , which lifts to the perfectoid _K_<sup>_♭◦a_</sup> -algebra _A_<sup>_♭_</sup> , which in turn gives rise to _R_<sup>_♭_</sup> . □ 

_Remark_ 5.19 _._ In fact, one can write down the functors in both directions. From characteristic 0 to characteristic _p_ , we have already given the explicit functor. The converse functor is given by _R_ = _W_ ( _R_<sup>_♭◦_</sup> ) _⊗W_ ( _K♭◦_ ) _K_ , using the usual map _θ_ : _W_ ( _K_<sup>_♭◦_</sup> ) _→ K_ . We leave it as an exercise to the reader to give a direct proof of the theorem via this description, cf. [27]. This avoids the use of almost mathematics in the proof of the tilting equivalence. We stress however that in our proof we never need to talk about big rings like _W_ ( _R_<sup>_♭◦_</sup> ), and that the point of view of the given proof will be useful in later arguments. 

Let us give a prototypical example for the tilting process. 

# **Proposition 5.20.** _Let_ 



� _Proof._ One checks that _R_<sup>_◦_</sup> = _K_<sup>_◦_</sup> [ _T_ 1<sup>1</sup><sup>_/p∞_</sup> _, . . . , Tn_<sup>1</sup><sup>_/p∞_</sup> ], which is _ϖ_ -adically complete and flat over _K_<sup>_◦_</sup> . Moreover, it reduces to _R_<sup>_◦_</sup> _/ϖ_ = _K_<sup>_◦_</sup> _/ϖ_ [ _T_ 1<sup>1</sup><sup>_/p∞_</sup> _, . . . , Tn_<sup>1</sup><sup>_/p∞_</sup> ], on which Frobenius is surjective. This shows that _R_ is a perfectoid _K_ -algebra. To see that its tilt has the desired form, we only have to check that _R_<sup>_◦_</sup> _/ϖ_ = _R_<sup>_♭◦_</sup> _/ϖ_<sup>_♭_</sup> , by the proof of the tilting equivalence. But this is obvious. □ 

We note that under the process of tilting, perfectoid fields are identified. 

**Lemma 5.21.** _Let R be a perfectoid K-algebra with tilt R_<sup>_♭_</sup> _. Then R is a perfectoid field if and only if R_<sup>_♭_</sup> _is a perfectoid field._ 

_Proof._ Note that _R_ is a perfectoid field if and only if it is a nonarchimedean field, i.e. its topology is induced by a rank-1-valuation. This valuation is necessarily given by the spectral norm 



- on _R_ . It is easy to check that for _x ∈ R_<sup>_♭_</sup> , we have _||x||R♭_ = _||x_<sup>_♯_</sup> _||R_ . In particular, if _|| · ||R_ is multiplicative, then so is _|| · ||R♭_ , i.e. if _R_ is a perfectoid field, then so is _R_<sup>_♭_</sup> . 

- Conversely, assume that _R_<sup>_♭_</sup> is a perfectoid field. We have to check that the spectral 

- norm _|| · ||R_ on _R_ is multiplicative. Let _x, y ∈ R_ ; after multiplication by elements of _K_ , we may assume _x, y ∈ R_<sup>_◦_</sup> , but not in _ϖ_<sup>1</sup><sup>_/p_</sup> _R_<sup>_◦_</sup> . We want to see that _||x||R||y||R_ = _||xy||R_ . 

PETER SCHOLZE 

28 

But we can find _x_<sup>_♭_</sup> _, y_<sup>_♭_</sup> _∈ R_<sup>_♭◦_</sup> with _x −_ ( _x_<sup>_♭_</sup> )<sup>_♯_</sup> _, y −_ ( _y_<sup>_♭_</sup> )<sup>_♯_</sup> _∈ ϖR_<sup>_◦_</sup> . Then _||x||R_ = _||x_<sup>_♭_</sup> _||R♭_ , _||y||R_ = _||y_<sup>_♭_</sup> _||R♭_ and _||xy||R_ = _||x_<sup>_♭_</sup> _y_<sup>_♭_</sup> _||R♭_ , and we get the claim. 

To see that _R_ is a field, choose _x_ such that _x ∈ R_<sup>_◦_</sup> , but not in _ϖR_<sup>_◦_</sup> , and take _x_<sup>_♭_</sup> as before. Then by multiplicativity of _||·||R_ , _||_ 1 _−_ ( _xx_<sup>_♭_</sup> )<sup>_♯||R<_1,and hence</sup> ( _xx_<sup>_♭_</sup> )<sup>_♯_is invertible,</sup> and then also _x_ . □ 

Finally, let us discuss finite ´etale covers of perfectoid algebras, and finish the proof of Theorem 3.7. 

**Proposition 5.22.** _Let A be a perfectoid K_<sup>_◦a_</sup> _/ϖ-algebra, and let B be a finite ´etale A-algebra. Then B is a perfectoid K_<sup>_◦a_</sup> _/ϖ-algebra._ 

_Proof._ Obviously, _B_ is flat. The statement about Frobenius follows from Theorem 3.5.13 ii) of [14]. □ 

In particular, Theorem 4.17 provides us with the following commutative diagram, where _R_ , _A_ , _A_ , _A_<sup>_♭_</sup> and _R_<sup>_♭_</sup> form a sequence of rings under the tilting procedure. 



It follows from this diagram that the functors _A_ f´et _→ R_ f´et and _A_<sup>_♭_</sup> f´et<sup>_→R_</sup> f´et<sup>_♭_are</sup> fully faithful. A main theorem is that both of them are equivalences: This amounts to Faltings’s almost purity theorem. At this point, we will prove this only in characteristic _p_ . 

**Proposition 5.23.** _Let K be of characteristic p, let R be a perfectoid K-algebra, and let S/R be finite ´etale. Then S is perfectoid and S_<sup>_◦a_</sup> _is finite ´etale over R_<sup>_◦a_</sup> _. Moreover, S_<sup>_◦a_</sup> _is a uniformly finite projective R_<sup>_◦a_</sup> _-module._ 

_Remark_ 5.24 _._ We need to define the topology on _S_ here. Recall that if _A_ is any ring with _t ∈ A_ not a zero-divisor, then any finitely generated _A_ [ _t_<sup>_−_1</sup> ]-module _M_ carries a canonical topology, which gives any finitely generated _A_ -submodule of _M_ the _t_ -adic topology. Any morphism of finitely generated _A_ [ _t_<sup>_−_1</sup> ]-modules is continuous for this topology, cf. [14], Definition 5.4.10 and 5.4.11. If _A_ is complete and _M_ is projective, then _M_ is complete, as one checks by writing _M_ as a direct summand of a finitely generated free _A_ -module. In particular, if _R_ is a perfectoid _K_ -algebra and _S/R_ a finite ´etale cover, then _S_ has a canonical topology for which it is complete. 

_Proof._ This follows from Theorem 3.5.28 of [14]. Let us recall the argument. Note that _S_ is a perfect Banach _K_ -algebra. We claim that it is perfectoid. Let _S_ 0 _⊂ S_ be some finitely generated _R_<sup>_◦_</sup> -subalgebra with _S_ 0 _⊗ K_ = _S_ . Let _S_ 0<sup>_⊥⊂S_bedefinedasthesetof</sup> all _x ∈ S_ such that _tS/R_ ( _x, S_ 0) _⊂ R_<sup>_◦_</sup> , using the perfect trace form pairing 

_tS/R_ : _S ⊗R S → R_ ; 

then _S_ 0 and _S_ 0<sup>_⊥_areopenandbounded.Let</sup><sup>_Y_betheintegralclosureof</sup><sup>_R◦_in</sup><sup>_S_.Then</sup> _S_ 0 _⊂ Y ⊂ S_ 0<sup>_⊥_:Indeed,theelementsof</sup><sup>_S_0areclearlyintegralover</sup><sup>_R◦_,andwehave</sup> _tS/R_ ( _Y, Y_ ) _⊂ R_<sup>_◦_</sup> . It follows that _Y_ is open and bounded. As _S_<sup>_◦a_</sup> = _Y_<sup>_a_</sup> , it follows that _S_<sup>_◦_</sup> is open and bounded, as desired. 

Next, we want to check that _S_<sup>_◦a_</sup> is a uniformly finite projective _R_<sup>_◦a_</sup> -module. For this, it is enough to prove that there is some _n_ such that for any _ϵ ∈_ m, there are maps _S_<sup>_◦_</sup> _→ R_<sup>_◦n_</sup> and _R_<sup>_◦n_</sup> _→ S_<sup>_◦_</sup> whose composite is multiplication by _ϵ_ . 

Let _e ∈ S ⊗R S_ be the idempotent showing that _S_ is unramified over _R_ . Then _ϖ_<sup>_N_</sup> _e_ is in the image of _S_<sup>_◦_</sup> _⊗R◦ S_<sup>_◦_</sup> in _S ⊗R S_ for some _N_ . Write _ϖ_<sup>_N_</sup> _e_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_xi⊗yi_.As</sup> 

PERFECTOID SPACES 

29 

Frobenius is bijective, we have _ϖ_<sup>_N/pm_</sup> _e_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_x_1</sup> _i_<sup>_/pm_</sup> _⊗ yi_<sup>1</sup><sup>_/pm_</sup> for all _m_ . In particular, for any _ϵ ∈_ m, we can write _ϵe_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ai ⊗bi_forcertain</sup><sup>_ai, bi∈S◦_,dependingon</sup><sup>_ϵ_.</sup> We get the map _S_<sup>_◦_</sup> _→ R_<sup>_◦n_</sup> , 



and the map _R_<sup>_◦n_</sup> _→ S_<sup>_◦_</sup> , 



One easily checks that their composite is multiplication by _ϵ_ , giving the claim. 

It remains to see that _S_<sup>_◦a_</sup> is an unramified _R_<sup>_◦a_</sup> -algebra. But this follows from the previous arguments, which show that _e_ defines an almost element of _S_<sup>_◦a_</sup> _⊗R◦a S_<sup>_◦a_</sup> with the desired properties. □ 

It follows that the diagram above extends as follows. 



Moreover, using Theorem 4.17, it follows that all finite ´etale algebras over _A_ , _A_ or _A_<sup>_♭_</sup> are uniformly almost finitely presented. Let us summarize the discussion. 

**Theorem 5.25.** _Let R be a perfectoid K-algebra with tilt R_<sup>_♭_</sup> _. There is a fully faithful functor from R_ f´et<sup>_♭toR_f´et</sup><sup>_inversetothetiltingfunctor._</sup> _The essential image of this functor consists of the finite ´etale covers S of R, for which S (with its natural topology) is perfectoid and S_<sup>_◦a_</sup> _is finite ´etale over R_<sup>_◦a_</sup> _. In this case, S_<sup>_◦a_</sup> _is a uniformly finite projective R_<sup>_◦a_</sup> _-module._ 

In particular, we see that the fully faithful functor _R_ f´et<sup>_♭�→R_f´etpreserves degrees.We</sup> will later prove that this is an equivalence in general. For now, we prove that it is an equivalence for perfectoid fields, i.e. we finish the proof of Theorem 3.7. 

_Proof._ ( _of Theorem 3.7_ ) Let _K_ be a perfectoid field with tilt _K_<sup>_♭_</sup> . Using the previous theorem, it is enough to show that the fully faithful functor _K_ f´et<sup>_♭→K_f´etisanequiva-</sup> lence. 

_Proof using ramification theory._ Proposition 6.6.2 (cf. its proof) and Proposition 6.6.6 of [14] show that for any finite extension _L_ of _K_ , the extension _L_<sup>_◦a_</sup> _/K_<sup>_◦a_</sup> is ´etale. Moreover, it is finite projective by Proposition 6.3.6 of [14], giving the desired result. 

_Proof reducing to the case where K_<sup>_♭_</sup> _is algebraically closed._ Let _M_ = _K_<sup><u>�</u></sup><sup>_♭_</sup> be the completion of an algebraic closure of _K_<sup>_♭_</sup> . Clearly, _M_ is complete and perfect, i.e. _M_ is perfectoid. Let _M_<sup>_♯_</sup> be the untilt of _M_ . Then by Lemma 5.21 and Proposition 3.8, _M_<sup>_♯_</sup> is an algebraically closed perfectoid field containing _K_ . Any finite extension _L ⊂ M_ of _K_<sup>_♭_</sup> gives the untilt _L_<sup>_♯_</sup> _⊂ M_<sup>_♯_</sup> , a finite extension of _K_ . It is easy to see that the union _N_ =<sup>�</sup> _L_<sup>_L♯⊂M♯_isadensesubfield.NowKrasner’slemmaimpliesthat</sup><sup>_N_is</sup> algebraically closed. Hence any finite extension _F_ of _K_ is contained in _N_ ; this means that there is some Galois extension _L_ of _K_<sup>_♭_</sup> such that _F_ is contained in _L_<sup>_♯_</sup> . Note that _L_<sup>_♯_</sup> is still Galois, as the functor _L �→ L_<sup>_♯_</sup> preserves degrees and automorphisms. In particular, _F_ is given by some subgroup _H_ of Gal( _L_<sup>_♯_</sup> _/K_ ) = Gal( _L/K_<sup>_♭_</sup> ), which gives the desired finite extension _F_<sup>_♭_</sup> = _L_<sup>_H_</sup> of _K_<sup>_♭_</sup> that untilts to _F_ : The equivalence of categories shows that ( _F_<sup>_♭_</sup> )<sup>_♯_</sup> _⊂_ ( _L_<sup>_♯_</sup> )<sup>_H_</sup> = _F_ , and as they have the same degree, they are equal. □ 

PETER SCHOLZE 

30 

# 6. Perfectoid spaces: Analytic topology 

In the following, we are interested in the adic spaces associated to perfectoid algebras. Specifically, note that perfectoid _K_ -algebras are Tate, and we will look at the following type of affinoid _K_ -algebras. 

**Definition 6.1.** _A perfectoid affinoid K-algebra is an affinoid K-algebra_ ( _R, R_<sup>+</sup> ) _such that R is a perfectoid K-algebra._ 

We note that in this case m _R_<sup>_◦_</sup> _⊂ R_<sup>+</sup> _⊂ R_<sup>_◦_</sup> , because all topologically nilpotent elements lie in _R_<sup>+</sup> , as _R_<sup>+</sup> is integrally closed. In particular, _R_<sup>+</sup> is almost equal to _R_<sup>_◦_</sup> . 

**Lemma 6.2.** _The categories of perfectoid affinoid K-algebras and perfectoid affinoid K_<sup>_♭_</sup> _-algebras are equivalent. If_ ( _R, R_<sup>+</sup> ) _maps to_ ( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _under this equivalence, then x �→ x_<sup>_♯_</sup> _induces an isomorphism R_<sup>_♭_+</sup> _/ϖ_<sup>_♭∼_</sup> = _R_<sup>+</sup> _/ϖ. Also R_<sup>_♭_+</sup> = lim _←−x�→x_<sup>_p R_+</sup><sup>_._</sup> 

_Proof._ Giving an open integrally closed subring of _R_<sup>_◦_</sup> is equivalent to giving an integrally closed subring of _R_<sup>_◦_</sup> _/_ m. This description is compatible with tilting. One easily checks the last identities. □ 

It turns out that also in this case, the presheaf _OX_ is a sheaf. In fact, the main theorem of this section is the following. 

**Theorem 6.3.** _Let_ ( _R, R_<sup>+</sup> ) _be a perfectoid affinoid K-algebra, and let X_ = Spa( _R, R_<sup>+</sup> ) _with associated presheaves OX , OX_<sup>+</sup><sup>_.Also,let_(</sup><sup>_R♭, R♭_+)</sup><sup>_bethetiltgivenbyLemma6.2,_</sup> _and let X_<sup>_♭_</sup> = Spa( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _etc. ._ 

(i) _We have a homeomorphism X_<sup>_∼_</sup> = _X_<sup>_♭_</sup> _, given by mapping x ∈ X to the valuation x_<sup>_♭_</sup> _∈ X_<sup>_♭_</sup> _defined by |f_ ( _x_<sup>_♭_</sup> ) _|_ = _|f_<sup>_♯_</sup> ( _x_ ) _|. This homeomorphism identifies rational subsets._ 

(ii) _For any rational subset U ⊂ X with tilt U_<sup>_♭_</sup> _⊂ X_<sup>_♭_</sup> _, the complete affinoid K-algebra_ ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))</sup><sup>_isperfectoid,withtilt_(</sup><sup>_O_</sup> _X_<sup>_♭_(</sup><sup>_U♭_)</sup><sup>_, O_</sup> _X_<sup>+</sup><sup>_♭_(</sup><sup>_U♭_))</sup><sup>_._</sup> 

(iii) _The presheaves OX , OX ♭ are sheaves._ 

(iv) _The cohomology group H_<sup>_i_</sup> ( _X, OX_<sup>+)</sup><sup>_is_m</sup><sup>_-torsionfori >_0</sup><sup>_._</sup> 

We remark that we did not assume that _R_<sup>+</sup> is a _K_<sup>_◦_</sup> -algebra, although this is satisfied in all examples of interest to us. For this reason, it does not literally make sense to use the language of almost mathematics in the context of _OX_<sup>+.Inthefollowing,thereader</sup> may safely assume that _R_<sup>+</sup> is a _K_<sup>_◦_</sup> -algebra, which avoids some small extra twists. 

Let us give an outline of the proof. First, we show that the map _X → X_<sup>_♭_</sup> is continuous. Next, we prove a slightly weaker version of (ii), and give an explicit description of the perfectoid _K_<sup>_◦a_</sup> -algebra associated to _OX_ ( _U_ ). This will be used to prove a crucial approximation lemma, dealing with the problem that the map _g �→ g_<sup>_♯_</sup> is far from being surjective. Nonetheless, it turns out that one can approximate any function _f ∈ R_ by a function of the form _g_<sup>_♯_</sup> such that the maps _x �→|f_ ( _x_ ) _|_ and _x �→|g_<sup>_♯_</sup> ( _x_ ) _|_ are identical except maybe at points _x_ where both of them are very small. It is then easy to deduce part (i), and also part (ii). We note that the same approximation lemma will be used later in the proof of the weight-monodromy conjecture for complete intersections. 

It remains to prove that _OX_ is a sheaf with vanishing higher cohomology, and that the vanishing even extends to the almost integral level. The proof proceeds in several steps. First, we prove it in the case that _K_ is of characteristic _p_ and ( _R, R_<sup>+</sup> ) is the completed perfection of an affinoid _K_ -algebra of tft. In that case, it is easy to deduce the result from Tate’s acyclicity theorem. Again, the direct limit over the Frobenius extends the vanishing of cohomology to the almost integral level. Next, we do the general characteristic _p_ case by writing an arbitrary perfectoid affinoid _K_ -algebra ( _R, R_<sup>+</sup> ) as the completed direct limit of algebras of the previous form. Finally, we deduce the case 

PERFECTOID SPACES 

31 

where _K_ has characteristic 0 by using the result in characteristic _p_ , making use of parts (i) and (ii) already proved. 

_Proof._ First, we check that the map _X → X_<sup>_♭_</sup> is well-defined and continuous: To check welldefinedness, we have to see that it maps valuations to valuations. This was already verified in the proof of Proposition 3.6. 

Moreover, the map _X → X_<sup>_♭_</sup> is continuous, because the preimage of the rational subset <u>1</u><sup>_<u>,...,f</u>_</sup> _n_<sup>_♯_</sup> _U_ (<sup>_<u>f</u>_</sup><sup><u>1</u></sup><sup>_<u>,...</u>_</sup> _g_<sup>_<u>,fn</u>_</sup> ) is given by _U_ (<sup>_<u>f</u>♯_</sup> _g_<sup>_♯_</sup> ), assuming as in Remark 2.8 that _fn_ is a power of _ϖ_<sup>_♭_</sup> to ensure that _f_ 1<sup>_♯, . . . , f_</sup> _n_<sup>_♯_stillgenerate</sup><sup>_R_.</sup> We have the following description of _OX_ . 

**Lemma 6.4.** _Let U_ = _U_ (<sup>_<u>f</u>_</sup><sup><u>1</u></sup><sup>_<u>,...</u>_</sup> _g_<sup>_<u>,fn</u>_</sup> ) _⊂_ Spa( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _be rational, with preimage U_<sup>_♯_</sup> _⊂_ Spa( _R, R_<sup>+</sup> ) _. Assume that all fi, g ∈ R_<sup>_♭◦_</sup> _and that fn_ = _ϖ_<sup>_♭N_</sup> _for some N ; this is always possible without changing the rational subspace._ 

(i) _Consider the ϖ-adic completion_ 





(iii) _The tilt of OX_ ( _U_<sup>_♯_</sup> ) _is given by OX ♭_ ( _U_ ) _._ 

_Proof._ (i), ( _K_ of characteristic _p_ ) Assume that _K_ has characteristic _p_ , and identify _K_<sup>_♭_</sup> = _K_ ; the general case is dealt with below. We see from the definition that 



is flat over _K_<sup>_◦_</sup> and _ϖ_ -adically complete. 

We want to show that modulo _ϖ_ , Frobenius is almost surjective with kernel almost generated by _ϖ_<sup>1</sup><sup>_/p_</sup> . We have a surjection 



Its kernel contains the ideal _I_ generated by all _Ti_<sup>1</sup><sup>_/pm_</sup> _g_<sup>1</sup><sup>_/pm_</sup> _− fi_<sup>1</sup><sup>_/pm_</sup> . We claim that the induced morphism 



is an almost isomorphism. Indeed, it is an isomorphism after inverting _ϖ_ , because this also inverts _g_ . If _f_ lies in the kernel of this map, there is some _k_ with _ϖ_<sup>_k_</sup> _f ∈ I_ . But then ( _ϖ_<sup>_k/pm_</sup> _f_ )<sup>_pm_</sup> _∈ I_ , and because _I_ is perfect, also _ϖ_<sup>_k/pm_</sup> _f ∈ I_ . This gives the desired statement. 

32 

PETER SCHOLZE 

Reducing modulo _ϖ_ , we have an almost isomorphism 



From the definition of _I_ , it is immediate that Frobenius gives an isomorphism _R_<sup>_◦_</sup> [ _T_ 1<sup>1</sup><sup>_/p∞_</sup> _, . . . , Tn_<sup>1</sup><sup>_/p∞_</sup> ] _/_ ( _I, ϖ_<sup>1</sup><sup>_/p_</sup> )<sup>_∼_</sup> = _R_<sup>_◦_</sup> [ _T_ 1<sup>1</sup><sup>_/p∞_</sup> _, . . . , Tn_<sup>1</sup><sup>_/p∞_</sup> ] _/_ ( _I, ϖ_ ) _._ 

This finally shows that 

is a perfectoid _K_<sup>_◦a_</sup> -algebra, giving part (i) in characteristic _p_ . (i) _⇒_ (ii), (General _K_ ) We show that in general, (i) implies (ii). Note that _R_<sup>_◦_</sup> _⊂ R_ is open and bounded, hence we may choose _R_ 0 = _R_<sup>_◦_</sup> in Definition 2.13. We have the inclusions 



Moreover, we claim that 

Indeed, <u>1</u> _<u>n</u> g_<sup>_♯_=</sup><sup>_ϖ−N_</sup><sup>_<u>f</u>_</sup> _g_<sup>_♯♯_,andanyelementontheleft-handsidecanbewrittenasasumof</sup> terms on the right-hand side with coefficients in ( _g_<sup>_♯_</sup> <u>1)</u><sup>_nR◦_.</sup> 

Now we may pass to the _ϖ_ -adic completion and get inclusions 



Thus it follows from part (i) that 



is perfectoid, with corresponding perfectoid _K_<sup>_◦a_</sup> -algebra. (i), (iii), (General _K_ ) Again, we see from the definition that 



is flat over _K_<sup>_◦_</sup> and _ϖ_ -adically complete. We have to show that modulo _ϖ_ , Frobenius is almost surjective with kernel almost generated by _ϖ_<sup>1</sup><sup>_/p_</sup> . We still have the map 



where _I_ is the ideal generated by all _Ti_<sup>1</sup><sup>_/pm_</sup> ( _g_<sup>1</sup><sup>_/pm_</sup> )<sup>_♯_</sup> _−_ ( _fi_<sup>1</sup><sup>_/pm_</sup> )<sup>_♯_</sup> . Also, we may apply our results for the tilted situation. In particular, we know that ( _OX ♭_ ( _U_ ) _, OX_<sup>+</sup><sup>_♭_(</sup><sup>_U_))isa</sup> perfectoid affinoid _K_<sup>_♭_</sup> -algebra. Let ( _S, S_<sup>+</sup> ) be its tilt. Then Spa( _S, S_<sup>+</sup> ) _→ X_ factors over _U_<sup>_♯_</sup> , and hence we get a map ( _OX_ ( _U_<sup>_♯_</sup> ) _, OX_<sup>+(</sup><sup>_U♯_))</sup><sup>_→_(</sup><sup>_S, S_+).Thecompositemap</sup> 



PERFECTOID SPACES 

33 

is a map of perfectoid _K_<sup>_◦a_</sup> -algebras, which is the tilt of the composite map 



where _I_<sup>_♭_</sup> is the corresponding ideal which occurs in the tilted situation. Note that _R_<sup>_♭◦_</sup> _⟨T_ 1<sup>1</sup><sup>_/p∞_</sup> _, . . . , Tn_<sup>1</sup><sup>_/p∞_</sup> _⟩/_ ( _I_<sup>_♭_</sup> _, ϖ_<sup>_♭_</sup> ) = _R_<sup>_◦_</sup> _⟨T_ 1<sup>1</sup><sup>_/p∞_</sup> _, . . . , Tn_<sup>1</sup><sup>_/p∞_</sup> _⟩/_ ( _I, ϖ_ ) 

from the explicit description. Since 



is an isomorphism, so is the composite map 



as it identifies with the previous map under tilting. The first map being surjective, it follows that both maps are isomorphisms. In particular, 



This gives part (i), and hence part (ii), and then the latter isomorphism gives part (iii). 



We need an approximation lemma. 

**Lemma 6.5.** _Let R_ = _K⟨T_ 0<sup>1</sup><sup>_/p∞_</sup> _, . . . , Tn_<sup>1</sup><sup>_/p∞_</sup> _⟩. Let f ∈ R_<sup>_◦_</sup> _be a homogeneous element of degree d ∈_ Z[ _p_<sup><u>1</u>]</sup><sup>_.Thenforanyrationalnumberc≥_0</sup><sup>_andanyϵ>_0</sup><sup>_,thereexistsan_</sup> _element_ 



_homogeneous of degree d such that for all x ∈ X_ = Spa( _R, R_<sup>_◦_</sup> ) _, we have_ 



_Remark_ 6.6 _._ Note that for _ϵ <_ 1, the given estimate says in particular that for all _x ∈ X_ = Spa( _R, R_<sup>_◦_</sup> ), we have 



_Proof._ We fix _ϵ >_ 0, and assume _ϵ <_ 1 and _ϵ ∈_ Z[ _p_<sup><u>1</u>].Wealsofix</sup><sup>_f_.Thenweprove</sup> inductively that for any _c_ one can find some _ϵ_ ( _c_ ) _>_ 0 and some 



homogeneous of degree _d_ such that for all _x ∈ X_ = Spa( _R, R_<sup>_◦_</sup> ), we have 



We will need _ϵ_ ( _c_ ), as each induction step will lose some small constant because of some almost mathematics involved. Now we argue by induction, increasing from _c_ to _c_<sup>_′_</sup> = _c_ + _a_ , where 0 _< a < ϵ_ is some fixed rational number in Z[ _p_<sup><u>1</u>].Thecase</sup><sup>_c_= 0isobvious:One</sup> may take _ϵ_ (0) = _ϵ_ . We are free to replace _ϵ_ ( _c_ ) by something smaller, so without loss of generality, we assume _ϵ_ ( _c_ ) _≤ ϵ − a_ and _ϵ_ ( _c_ ) _∈_ Z[ _p_<sup><u>1</u>].</sup> 

Let _X_ = Spa( _R, R_<sup>+</sup> ), where _R_<sup>+</sup> = _R_<sup>_◦_</sup> = _K_<sup>_◦_</sup> _⟨T_ 0<sup>1</sup><sup>_/p∞_</sup> _, . . . , Tn_<sup>1</sup><sup>_/p∞_</sup> _⟩_ . Let _Uc ⊂ X_<sup>_♭_</sup> = Spa( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) be the rational subset given by _|gc_ ( _x_ ) _| ≤|ϖ_<sup>_♭_</sup> _|_<sup>_c_</sup> . Its preimage _Uc_<sup>_♯⊂X_is</sup> given by _|f_ ( _x_ ) _| ≤|ϖ|_<sup>_c_</sup> . The condition implies that 



PETER SCHOLZE 

34 

The previous lemma shows that 



But _h_ is a homogeneous element, so that _h_ lies almost in the _ϖ_ -adic completion of 



This shows that we can find elements _ri ∈ R_<sup>+</sup> homogeneous of degree _d − di_ , such that _ri →_ 0, with 



where we choose some 0 _< ϵ_ ( _c_<sup>_′_</sup> ) _< ϵ_ ( _c_ ), _ϵ_ ( _c_<sup>_′_</sup> ) _∈_ Z[ _p_<sup><u>1</u>].Choose</sup><sup>_si∈R♭_+homogeneousof</sup> degree _d − di_ , _si →_ 0, such that _ϖ_ divides _ri − s_<sup>_♯_</sup> _i_<sup>.Nowset</sup> 



We claim that for all _x ∈ X_ , we have 



Assume first that _|f_ ( _x_ ) _| > |ϖ|_<sup>_c_</sup> . Then we have _|gc_<sup>_♯_(</sup><sup>_x_)</sup><sup>_|_=</sup><sup>_|f_(</sup><sup>_x_)</sup><sup>_|>|ϖ|c_.Itisenoughto</sup> show that 



Neglecting _|s_<sup>_♯_</sup> _i_<sup>(</sup><sup>_x_)</sup><sup>_|≤_1,theleft-handsideismaximalwhen</sup><sup>_i_=1,inwhichcaseit</sup> evaluates to the right-hand side, so that we get the desired estimate. 

Now we are left with the case _|f_ ( _x_ ) _| ≤|ϖ|_<sup>_c_</sup> . We claim that in fact 



in this case, which is clearly enough. For this, it is enough to see that _f − gc_<sup>_♯′_isan</sup> element of _ϖ_<sup>_c_+1</sup> _OX_ ( _Uc_<sup>_♯_)</sup><sup>_◦_,because</sup><sup>_c_+ 1</sup><sup>_> c′_+ 1</sup><sup>_−ϵ_+</sup><sup>_ϵ_(</sup><sup>_c′_).Butwehave</sup> 



with all terms being in _OX ♭_ ( _Uc_ )<sup>_◦_</sup> . Hence we get that 

in _OX_ ( _Uc_<sup>_♯_)</sup><sup>_◦_,modulo</sup><sup>_ϖ_.Multiplyingby</sup><sup>_ϖc_,thisrewritesas</sup> 



modulo _ϖ_<sup>_c_+1</sup> . This gives the desired estimate. 

□ 

**Corollary 6.7.** _Let_ ( _R, R_<sup>+</sup> ) _be a perfectoid affinoid K-algebra, with tilt_ ( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _, and let X_ = Spa( _R, R_<sup>+</sup> ) _, X_<sup>_♭_</sup> = Spa( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _._ 

PERFECTOID SPACES 

35 

(i) _For any f ∈ R and any c ≥_ 0 _, ϵ >_ 0 _, there exists gc,ϵ ∈ R_<sup>_♭_</sup> _such that for all x ∈ X, we have_ 

_|f_ ( _x_ ) _− gc,ϵ_<sup>_♯_(</sup><sup>_x_)</sup><sup>_| ≤|ϖ|_1</sup><sup>_−ϵ_max(</sup><sup>_|f_(</sup><sup>_x_)</sup><sup>_|, |ϖ|c_)</sup><sup>_._</sup> 

(ii) _For any x ∈ X, the completed residue field k_<sup>�</sup> ( _x_ ) _is a perfectoid field._ 

(iii) _The morphism X → X_<sup>_♭_</sup> _induces a homeomorphism, identifying rational subsets._ 

_Proof._ (i) As any maximal point of Spa( _R, R_<sup>+</sup> ) is contained in Spa( _R, R_<sup>_◦_</sup> ), and it is enough to check the inequality at maximal points after increasing _ϵ_ slightly, it is enough to prove this if _R_<sup>+</sup> = _R_<sup>_◦_</sup> . At the expense of enlarging _c_ , we may assume that _f ∈ R_<sup>_◦_</sup> , and also assume that _c_ is an integer. Further, we can write _f_ = _g_ 0<sup>_♯_+</sup><sup>_ϖg_</sup> 1<sup>_♯_+</sup><sup>_. . ._+</sup><sup>_ϖcg_</sup> _c_<sup>_♯_+</sup> _ϖ_<sup>_c_+1</sup> _fc_ +1 for certain _g_ 0 _, . . . , gc ∈ R_<sup>_♭◦_</sup> and _fc_ +1 _∈ R_<sup>_◦_</sup> . We can assume _fc_ +1 = 0. Now we have the map 



sending _Ti_<sup>1</sup><sup>_/pm_</sup> to ( _gi_<sup>1</sup><sup>_/pm_</sup> )<sup>_♯_</sup> , and _f_ is the image of _T_ 0 + _ϖT_ 1 + _. . ._ + _ϖ_<sup>_c_</sup> _Tc_ , to which we may apply Lemma 6.5. 

(ii), ( _K_ of characteristic _p_ ) In this case, we know that _OX_ ( _U_ )<sup>_◦a_</sup> is perfectoid for any rational subset _U_ . It follows that the _ϖ_ -adic completion of _OX,x_<sup>_◦a_isaperfectoid</sup><sup>_K◦a_-</sup> algebra, hence _k_<sup>�</sup> ( _x_ ) is a perfectoid _K_ -algebra. As it is also a nonarchimedean field, the result follows. 

(iii) First, part (i) immediately implies that any rational subset of _X_ is the preimage of a rational subset of _X_<sup>_♭_</sup> . Because _X_ is _T_ 0, this implies that the map is injective. Now any _x ∈ X_<sup>_♭_</sup> factors as a composite _R_<sup>_♭_</sup> _→ k_<sup>�</sup> ( _x_ ) _→_ Γ _∪{_ 0 _}_ . As _k_<sup>�</sup> ( _x_ ) is perfectoid, we may untilt to a perfectoid field over _K_ , and we may also untilt the valuation by Proposition 3.6. This shows that the map is surjective, giving part (iii). Now part (ii) follows in general with the same proof. 

□ 

For any subset _M ⊂ X_ , we write _M_<sup>_♭_</sup> _⊂ X_<sup>_♭_</sup> for the corresponding subset of _X_<sup>_♭_</sup> . 

**Corollary 6.8.** _Let_ ( _R, R_<sup>+</sup> ) _be a perfectoid affinoid K-algebra, with tilt_ ( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _, and let X_ = Spa( _R, R_<sup>+</sup> ) _, X_<sup>_♭_</sup> = Spa( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _. Then for all rational U ⊂ X, the pair_ ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))</sup><sup>_isaperfectoidaffinoidK-algebrawithtilt_(</sup><sup>_O_</sup> _X_<sup>_♭_(</sup><sup>_U♭_)</sup><sup>_, O_</sup> _X_<sup>+</sup><sup>_♭_(</sup><sup>_U♭_))</sup><sup>_._</sup> 

_Proof._ Corollary 6.7 (iii) and Lemma 6.4 (ii) show that ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))isaperfectoid</sup> affinoid _K_ -algebra. It can be characterized by the universal property of Proposition 2.14 among all perfectoid affinoid _K_ -algebras, and tilting this universal property shows that its tilt has the analogous universal property characterizing ( _OX ♭_ ( _U_<sup>_♭_</sup> ) _, OX_<sup>+</sup><sup>_♭_(</sup><sup>_U♭_))among</sup> all perfectoid affinoid _K_<sup>_♭_</sup> -algebras. □ 

At this point, we have proved parts (i) and (ii) of Theorem 6.3. 

To prove the sheaf properties, we start in characteristic _p_ , with a certain class of perfectoid rings which are particularly easy to access. 

**Definition 6.9.** _Assume K is of characteristic p. Then a perfectoid affinoid K-algebra_ ( _R, R_<sup>+</sup> ) _is said to be p-finite if there exists a reduced affinoid K-algebra_ ( _S, S_<sup>+</sup> ) _of topologically finite type such that_ ( _R, R_<sup>+</sup> ) _is the completed perfection of_ ( _S, S_<sup>+</sup> ) _, i.e. R_<sup>+</sup> _is the ϖ-adic completion of_ lim _−→_ Φ<sup>_S_+</sup><sup>_andR_=</sup><sup>_R_+[</sup><sup>_ϖ−_1]</sup><sup>_._</sup> 

At this point, let us recall some facts about reduced affinoid _K_ -algebras of topologically finite type. 

**Proposition 6.10.** _Let_ ( _S, S_<sup>+</sup> ) _be a reduced affinoid K-algebra of topologically finite type, and let X_ = Spa( _S, S_<sup>+</sup> ) _._ 

PETER SCHOLZE 

36 

- (i) _The subset S_<sup>+</sup> = _S_<sup>_◦_</sup> _⊂ S is open and bounded._ 

(ii) _For any rational subset U ⊂ X, the affinoid K-algebra_ ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))</sup><sup>_isreduced_</sup> _and of topologically finite type._ 

(iii) _For any covering X_ =<sup>�</sup> _Ui by finitely many rational subsets Ui ⊂ X, each cohomology group of the complex_ 



_is annihilated by some power of ϖ._ 

_Proof._ Using [19], Proposition 4.3 and its proof, one sees that all statements are readily translated into the classical language of rigid geometry, and we use results from the book of Bosch-G¨untzer-Remmert, [2]. Part (i) is precisely their 6.2.4 Theorem 1, and part (ii) is 7.3.2 Corollary 10. 

Moreover, Tate’s acyclicity theorem, 8.2.1 Theorem 1 in [2], says that 



is exact. Then ker _di_ is a closed subspace of a _K_ -Banach space, hence itself a _K_ -Banach space, and _di−_ 1 is a surjection onto ker _di_ . By Banach’s open mapping theorem, the map _di−_ 1 is an open map to ker _di_ . This says that the subspace and quotient topologies on ker _di_ = im _di−_ 1 coincide. Now consider the sequence 



By parts (i) and (ii), the quotient topology on im _di−_ 1 has _ϖ_<sup>_n_</sup> im _d_<sup>_◦_</sup> _i−_ 1<sup>,</sup><sup>_n ∈_Z,asabasis</sup> of open neighborhoods of 0, and the subspace topology of ker _di_ has _ϖ_<sup>_n_</sup> ker _d_<sup>_◦_</sup> _i_<sup>,</sup><sup>_n ∈_Z,as</sup> a basis of open neighborhoods of 0. That they agree precisely amounts to saying that the cohomology group is annihilated by some power of _ϖ_ . □ 

**Proposition 6.11.** _Assume that K is of characteristic p, and that_ ( _R, R_<sup>+</sup> ) _is p-finite, given as the completed perfection of a reduced affinoid K-algebra_ ( _S, S_<sup>+</sup> ) _of topologically finite type._ 

(i) _The map X_ = Spa( _R, R_<sup>+</sup> )<sup>_∼_</sup> = _Y_ = Spa( _S, S_<sup>+</sup> ) _is a homeomorphism identifying rational subspaces._ 

(ii) _For any U ⊂ X rational, corresponding to V ⊂ Y , the perfectoid affinoid K-algebra_ ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))</sup><sup>_isequaltothecompletedperfectionof_(</sup><sup>_OY_(</sup><sup>_V_)</sup><sup>_, O_</sup> _Y_<sup>+(</sup><sup>_V_))</sup><sup>_._</sup> 

(iii) _For any covering X_ =<sup>�</sup> _i_<sup>_Uibyrationalsubsets,thesequence_</sup> 



_is exact. In particular, OX is a sheaf, and H_<sup>_i_</sup> ( _X, OX_<sup>_◦a_) = 0</sup><sup>_fori >_0</sup><sup>_._</sup> 

_Remark_ 6.12 _._ The last assertion is equivalent to the assertion that _H_<sup>_i_</sup> ( _X, OX_<sup>+)isanni-</sup> hilated by m. 

_Proof._ (i) Going to the perfection does not change the associated adic space and rational subspaces, and going to the completion does not by Proposition 2.11. 

(ii) The completed perfection of ( _OY_ ( _V_ ) _, OY_<sup>+(</sup><sup>_V_))isaperfectoidaffinoid</sup><sup>_K_-algebra.It</sup> has the universal property defining ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))amongallperfectoidaffinoid</sup><sup>_K_-</sup> algebras. 

PERFECTOID SPACES 

37 

(iii) Note that the corresponding sequence for _Y_ is exact up to some _ϖ_ -power. Hence after taking the perfection, it is almost exact, and stays so after completion. 

□ 

**Lemma 6.13.** _Assume K is of characteristic p._ 

(i) _Any perfectoid affinoid K-algebra_ ( _R, R_<sup>+</sup> ) _for which R_<sup>+</sup> _is a K_<sup>_◦_</sup> _-algebra is the completion of a filtered direct limit of p-finite perfectoid affinoid K-algebras_ ( _Ri, Ri_<sup>+)</sup><sup>_._</sup> (ii) _This induces a homeomorphism_ Spa( _R, R_<sup>+</sup> )<sup>_∼_</sup> = lim _←−_<sup>Spa(</sup><sup>_Ri, R_</sup> _i_<sup>+)</sup><sup>_,andeachrational_</sup> _U ⊂ X_ = Spa( _R, R_<sup>+</sup> ) _comes as the preimage of some rational Ui ⊂ Xi_ = Spa( _Ri, Ri_<sup>+)</sup><sup>_._</sup> (iii) _In this case_ ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))</sup><sup>_isequaltothecompletionofthefiltereddirectlimitof_</sup> _the_ ( _OXj_ ( _Uj_ ) _, OX_<sup>+</sup> _j_<sup>(</sup><sup>_Uj_))</sup><sup>_,whereUjisthepreimageofUiinXjforj≥i._</sup> 

(iv) _If Ui ⊂ Xi is some quasicompact open subset containing the image of X, then there is some j such that the image of Xj is contained in Ui._ 

_Proof._ (i) For any finite subset _I ⊂ R_<sup>+</sup> , we have the _K_ -subalgebra _SI ⊂ R_ given as the image of _K⟨Ti|i ∈ I⟩→ R_ . Then _SI_ is a reduced quotient of _K⟨Ti|i ∈ I⟩_ , and we give _SI_ the quotient topology. Let _SI_<sup>+</sup><sup>_⊂SI_bethesetofpower-boundedelements;itisalsothe</sup> set of elements integral over _K_<sup>_◦_</sup> _⟨Ti|i ∈ I⟩_ by [31], Theorem 5.2. In particular, _SI_<sup>+</sup><sup>_⊂R_+.</sup> We caution the reader that _SI_<sup>+isingeneralnotthepreimageof</sup><sup>_R_+in</sup><sup>_SI_.</sup> 

Now let ( _RI , RI_<sup>+)bethecompletedperfectionof(</sup><sup>_SI, S_</sup> _I_<sup>+),i.e.</sup><sup>_R_</sup> _I_<sup>+isthe</sup><sup>_ϖ_-adiccom-</sup> pletion of _−→_ limΦ<sup>_S_</sup> _I_<sup>+,and</sup><sup>_RI_=</sup><sup>_R_</sup> _I_<sup>+[</sup><sup>_ϖ−_1].Wegetaninducedmap(</sup><sup>_RI, R_</sup> _I_<sup>+)</sup><sup>_→_(</sup><sup>_R, R_+),</sup> and ( _RI , RI_<sup>+)isap-finiteperfectoidaffinoid</sup><sup>_K_-algebra.</sup> We claim that _R_<sup>+</sup> _/ϖ_<sup>_n_</sup> = lim _−→I_<sup>_R_</sup> _I_<sup>+</sup><sup>_/ϖn_.Indeed, the map is clearly surjective.It is also injective, since if</sup><sup>_f_1</sup><sup>_, f_2</sup><sup>_∈R_</sup> _I_<sup>+</sup> satisfy _f_ 1 _− f_ 2 = _ϖ_<sup>_n_</sup> _g_ for some _g ∈ R_<sup>+</sup> , then for some larger _J ⊃ I_ containing _g_ , also _f_ 1 _− f_ 2 _∈ ϖ_<sup>_n_</sup> _RJ_<sup>+.Thisshowsthat</sup><sup>_R_+isthecompleteddirectlimitofthe</sup><sup>_R_</sup> _I_<sup>+,i.e.</sup> ( _R, R_<sup>+</sup> ) is the completed direct limit of the ( _RI , RI_<sup>+).</sup> (ii) Let ( _L, L_<sup>+</sup> ) be the direct limit of the ( _RI , RI_<sup>+),equippedwiththe</sup><sup>_ϖ_-adictopology.</sup> Then one checks by hand that Spa( _L, L_<sup>+</sup> )<sup>_∼_</sup> = lim _←−_<sup>Spa(</sup><sup>_Ri, R_</sup> _i_<sup>+),compatiblewithratio-</sup> nal subspaces. But then the same thing holds true for the completed direct limit by Proposition 2.11. 

(iii) The completion of the direct limit of the ( _OXj_ ( _Uj_ ) _, OX_<sup>+</sup> _j_<sup>(</sup><sup>_Uj_))isaperfectoidaffinoid</sup> _K_ -algebra, and it satisfies the universal property describing ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_)).</sup> 

(iv) This is an abstract property of spectral spaces and spectral maps. Let _Ai_ be the closed complement of _Ui_ , and for any _j ≥ i_ , let _Aj_ be the preimage of _Ai_ in _Xj_ . Then the _Aj_ are constructible subsets of _Xj_ , hence spectral, and the transition maps between the _Aj_ are spectral. If one gives the _Aj_ the constructible topology, they are compact topological spaces, and the transition maps are continuous. If their inverse limit is zero, then one of them has to be zero. 



**Proposition 6.14.** _Let K be of any characteristic, and let_ ( _R, R_<sup>+</sup> ) _be a perfectoid affinoid K-algebra, X_ = Spa( _R, R_<sup>+</sup> ) _. For any covering X_ =<sup>�</sup> _i_<sup>_Uibyfinitelymany_</sup> _rational subsets, the sequence_ 



_is exact. In particular, OX is a sheaf, and H_<sup>_i_</sup> ( _X, OX_<sup>_◦a_) = 0</sup><sup>_fori >_0</sup><sup>_._</sup> 

_Proof._ Assume first that _K_ has characteristic _p_ . We may replace _K_ by a perfectoid subfield, such as the _ϖ_ -adic completion of F _p_ (( _ϖ_ ))( _ϖ_<sup>1</sup><sup>_/p∞_</sup> ); this ensures that for any perfectoid affinoid _K_ -algebra ( _R, R_<sup>+</sup> ), the ring _R_<sup>+</sup> is a _K_<sup>_◦_</sup> -algebra. Then use Lemma 

PETER SCHOLZE 

38 

6.13 to write _X_ = Spa( _R, R_<sup>+</sup> )<sup>_∼_</sup> = lim _←−_<sup>_Xi_= Spa(</sup><sup>_Ri, R_</sup> _i_<sup>+) as an inverse limit, with (</sup><sup>_Ri, R_</sup> _i_<sup>+)</sup> p-finite. Any rational subspace comes from a finite level, and a cover by finitely many rational subspaces is the pullback of a cover by finitely many rational subspaces on a finite level. Hence the almost exactness of the sequence follows by taking the completion of the direct limit of the corresponding statement for _Xi_ , which is given by Proposition 6.11. The rest follows as before. In characteristic 0, first use the exactness of the tilted sequence, then reduce modulo _ϖ_<sup>_♭_</sup> (which is still exact by flatness), and then remark that this is just the original sequence reduced modulo _ϖ_ . As this is exact, the original sequence is exact, by flatness and completeness. Again, we also get the other statements. □ This finishes the proof of Theorem 6.3. □ 

We see that to any perfectoid affinoid _K_ -algebra ( _R, R_<sup>+</sup> ), we have associated an affinoid adic space _X_ = Spa( _R, R_<sup>+</sup> ). We call these spaces affinoid perfectoid spaces. 

**Definition 6.15.** _A perfectoid space is an adic space over K that is locally isomorphic to an affinoid perfectoid space. Morphisms between perfectoid spaces are the morphisms of adic spaces._ 

# The process of tilting glues. 

**Definition 6.16.** _We say that a perfectoid space X_<sup>_♭_</sup> _over K_<sup>_♭_</sup> _is the tilt of a perfectoid space X over K if there is a functorial isomorphism_ Hom(Spa( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _, X_<sup>_♭_</sup> ) = Hom(Spa( _R, R_<sup>+</sup> ) _, X_ ) _for all perfectoid affinoid K-algebras_ ( _R, R_<sup>+</sup> ) _with tilt_ ( _R_<sup>_♭_</sup> _, R_<sup>_♭_+</sup> ) _._ **Proposition 6.17.** _Any perfectoid space X over K admits a tilt X_<sup>_♭_</sup> _, unique up to unique isomorphism. This induces an equivalence between the category of perfectoid spaces over K and the category of perfectoid spaces over K_<sup>_♭_</sup> _. The underlying topological spaces of X and X_<sup>_♭_</sup> _are naturally identified. A perfectoid space X is affinoid perfectoid if and only if its tilt X_<sup>_♭_</sup> _is affinoid perfectoid. Finally, for any affinoid perfectoid subspace U ⊂ X, the pair_ ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_))</sup><sup>_isaperfectoidaffinoidK-algebrawithtilt_(</sup><sup>_O_</sup> _X_<sup>_♭_(</sup><sup>_U♭_)</sup><sup>_, O_</sup> _X_<sup>+</sup><sup>_♭_(</sup><sup>_U♭_))</sup><sup>_._</sup> 

_Proof._ This is a formal consequence of Theorem 5.2, Theorem 6.3 and Proposition 2.19. Note that to any open _U ⊂ X_ , one gets an associated perfectoid space with underlying topological space _U_ by restricting the structure sheaf and valuations to _U_ , and hence its global sections are ( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_)),sothatif</sup><sup>_U_isaffinoid,then</sup> _U_ = Spa( _OX_ ( _U_ ) _, OX_<sup>+(</sup><sup>_U_)).Thisgivesthelastpartoftheproposition.</sup> □ 

Let us finish this section by noting one way in which perfectoid spaces behave better than adic spaces (cf. Proposition 1.2.2 of [20]). 

**Proposition 6.18.** _If X → Y ← Z are perfectoid spaces over K, then the fibre product X ×Y Z exists in the category of adic spaces over K, and is a perfectoid space._ 

_Proof._ As usual, one reduces to the affine case, _X_ = Spa( _A, A_<sup>+</sup> ), _Y_ = Spa( _B, B_<sup>+</sup> ) and _Z_ = Spa( _C, C_<sup>+</sup> ), and we want to construct _W_ = _X ×Y Z_ . This is given by _W_ = Spa( _D, D_<sup>+</sup> ), where _D_ is the completion of _A ⊗B C_ , and _D_<sup>+</sup> is the completion � of the integral closure of the image of _A_<sup>+</sup> _⊗B_ + _C_<sup>+</sup> in _D_ . Note that _A_<sup>_◦a_</sup> _⊗B◦a C_<sup>_◦a_</sup> is a perfectoid _K_<sup>_◦a_</sup> -algebra: It is enough to check that _A_<sup>_◦a_</sup> _⊗B◦a C_<sup>_◦a_</sup> _/ϖ_ is flat over _K_<sup>_◦a_</sup> _/ϖ_ , hence one reduces to characteristic _p_ . Here, it is enough to check that _A_<sup>_◦a_</sup> _⊗B◦a C_<sup>_◦a_</sup> is _ϖ_ -torsion free; but if _ϖf_ = 0, then _ϖ_<sup>1</sup><sup>_/p_</sup> _f_<sup>1</sup><sup>_/p_</sup> = 0 by perfectness, hence _ϖ_<sup>1</sup><sup>_/p_</sup> _f_ = 0. Continuing gives the result. In particular, ( _D, D_<sup>+</sup> ) is a perfectoid affinoid _K_ -algebra. One immediately checks that it satisfies the desired universal property. □ 

PERFECTOID SPACES 

39 

# 7. Perfectoid spaces: Etale topology 

In this section, we use the term locally noetherian adic space over _k_ for the adic spaces over _k_ considered in [20], i.e. they are locally of the form Spa( _A, A_<sup>+</sup> ), were _A_ is a strongly noetherian Tate _k_ -algebra. If additionally, they are quasicompact and quasiseparated, we call them noetherian adic spaces. 

Although perfectoid rings are always reduced, and hence a definition involving lifting of nilpotents is not possible, there is a good notion of ´etale morphisms. In the following definition, _k_ can be an arbitrary nonarchimedean field. 

**Definition 7.1.** (i) _A morphism_ ( _R, R_<sup>+</sup> ) _→_ ( _S, S_<sup>+</sup> ) _of affinoid k-algebras is called finite ´etale if S is a finite ´etale R-algebra with the induced topology, and S_<sup>+</sup> _is the integral closure of R_<sup>+</sup> _in S._ 

(ii) _A morphism f_ : _X → Y of adic spaces over k is called finite ´etale if there is a cover of Y by open affinoids V ⊂ Y such that the preimage U_ = _f_<sup>_−_1</sup> ( _V_ ) _is affinoid, and the associated morphism of affinoid k-algebras_ 



_is finite ´etale._ 

(iii) _A morphism f_ : _X → Y of adic spaces over k is called ´etale if for any point x ∈ X there are open neighborhoods U and V of x and f_ ( _x_ ) _and a commutative diagram_ 



_where j is an open embedding and p is finite ´etale._ 

For locally noetherian adic spaces over _k_ , this recovers the usual notions, by Example 1.6.6 ii) and Lemma 2.2.8 of [20], respectively. We will see that these notions are useful in the case of perfectoid spaces, and will not use them otherwise. However, we will temporarily need a stronger notion of ´etale morphisms for perfectoid spaces. After proving the almost purity theorem, we will see that there is no difference. In the following let _K_ be a perfectoid field again. 

**Definition 7.2.** (i) _A morphism_ ( _R, R_<sup>+</sup> ) _→_ ( _S, S_<sup>+</sup> ) _of perfectoid affinoid K-algebras is called strongly finite ´etale if it is finite ´etale and additionally S_<sup>_◦a_</sup> _is a finite ´etale R_<sup>_◦a_</sup> _-algebra._ 

(ii) _A morphism f_ : _X → Y of perfectoid spaces over K is called strongly finite ´etale if there is a cover of Y by open affinoid perfectoids V ⊂ Y such that the preimage U_ = _f_<sup>_−_1</sup> ( _V_ ) _is affinoid perfectoid, and the associated morphism of perfectoid affinoid K-algebras_ 



_is strongly finite ´etale._ 

(iii) _A morphism f_ : _X → Y of perfectoid spaces over K is called strongly ´etale if for any point x ∈ X there are open neighborhoods U and V of x and f_ ( _x_ ) _and a commutative diagram_ 



_where j is an open embedding and p is strongly finite ´etale._ 

PETER SCHOLZE 

40 

From the definitions, Proposition 6.17, and Theorem 5.25, we see that _f_ : _X → Y_ is strongly finite ´etale, resp. strongly ´etale, if and only if the tilt _f_<sup>_♭_</sup> : _X_<sup>_♭_</sup> _→ Y_<sup>_♭_</sup> is strongly finite ´etale, resp. strongly ´etale. Moreover, in characteristic _p_ , anything (finite) ´etale is also strongly (finite) ´etale. 

**Lemma 7.3.** (i) _Let f_ : _X → Y be a strongly finite ´etale, resp. strongly ´etale, morphism of perfectoid spaces and let g_ : _Z → Y be an arbitrary morphism of perfectoid spaces. Then X ×Y Z → Z is a strongly finite ´etale, resp. strongly ´etale, morphism of perfectoid spaces. Moreover, the map of underlying topological spaces |X ×Z Y | →|X| ×|Z| |Y | is surjective._ 

(ii) _If in (i), all spaces X_ = Spa( _A, A_<sup>+</sup> ) _, Y_ = Spa( _B, B_<sup>+</sup> ) _and Z_ = Spa( _C, C_<sup>+</sup> ) _are affinoid, with_ ( _A, A_<sup>+</sup> ) _strongly finite ´etale over_ ( _B, B_<sup>+</sup> ) _, then X ×Y Z_ = Spa( _D, D_<sup>+</sup> ) _, where D_ = _A ⊗B C and D_<sup>+</sup> _is the integral closure of C_<sup>+</sup> _in D, and_ ( _D, D_<sup>+</sup> ) _is strongly finite ´etale over_ ( _C, C_<sup>+</sup> ) _._ 

(iii) _Assume that K is of characteristic p. If f_ : _X → Y is a finite ´etale, resp. ´etale, morphism of adic spaces over k and g_ : _Z → Y is a map from a perfectoid space Z to Y , then the fibre product X ×Y Z exists in the category of adic spaces over K, is a perfectoid space, and the projection X ×Y Z → Z is finite ´etale, resp. ´etale. Moreover, the map of underlying topological spaces |X ×Z Y | →|X| ×|Z| |Y | is surjective._ 

(iv) _Assume that in the situation of (iii), all spaces X_ = Spa( _A, A_<sup>+</sup> ) _, Y_ = Spa( _B, B_<sup>+</sup> ) _and Z_ = Spa( _C, C_<sup>+</sup> ) _are affinoid, with_ ( _A, A_<sup>+</sup> ) _finite ´etale over_ ( _B, B_<sup>+</sup> ) _, then X ×Y Z_ = Spa( _D, D_<sup>+</sup> ) _, where D_ = _A ⊗B C, D_<sup>+</sup> _is the integral closure of C_<sup>+</sup> _in D and_ ( _D, D_<sup>+</sup> ) _is finite ´etale over_ ( _C, C_<sup>+</sup> ) _._ 

_Proof._ (ii) As _A⊗BC_ is finite projective over _C_ , it is already complete. One easily deduces the universal property. Also, _D_<sup>_◦a_</sup> is finite ´etale over _C_<sup>_◦a_</sup> , as base-change preserves finite ´etale morphisms. 

(i) Applying the definition of a strongly finite ´etale map, one reduces the statement about strongly finite ´etale maps to the situation handled in part (ii). Now the statement for strongly ´etale maps follows, because fibre products obviously preserve open embeddings. The surjectivity statement follows from the argument of [19], proof of Lemma 3.9 (i). 

(iv) Proposition 5.23 shows that _D_ = _A ⊗B C_ is perfectoid. Therefore Spa( _D, D_<sup>+</sup> ) is a perfectoid space. One easily checks the universal property. 

(iii) The finite ´etale case reduces to the situation considered in part (iv). Again, it is trivial to handle open embeddings, giving also the ´etale case. Surjectivity is proved as before. 

□ 

Let us recall the following statement about henselian rings. 

**Proposition 7.4.** _Let A be a flat K_<sup>_◦_</sup> _-algebra such that A is henselian along_ ( _ϖ_ ) _. Then the categories of finite ´etale A_ [ _ϖ_<sup>_−_1</sup> ] _and finite ´etale A_<sup>ˆ</sup> [ _ϖ_<sup>_−_1</sup> ] _-algebras are equivalent, where A_<sup>ˆ</sup> _is the ϖ-adic completion of A._ 

_Proof._ See e.g. [14], Proposition 5.4.53. □ 

We recall that _ϖ_ -adically complete algebras _A_ are henselian along ( _ϖ_ ), and that if _Ai_ is a direct system of _K_<sup>_◦_</sup> -algebras henselian along ( _ϖ_ ), then so is the direct limit _−→_ lim<sup>_Ai_.</sup> In particular, we get the following lemma. 

**Lemma 7.5.** (i) _Let Ai be a filtered direct system of complete flat K_<sup>_◦_</sup> _-algebras, and let A be the completion of the direct limit, which is again a complete flat K_<sup>_◦_</sup> _-algebra. Then we have an equivalence of categories_ 



PERFECTOID SPACES 

41 

_In particular, if Ri is a filtered direct system of perfectoid K-algebras and R is the completion of their direct limit, then R_ f´et<sup>_∼_</sup> = 2 _−_ lim _−→_<sup>(</sup><sup>_Ri_)f´et</sup><sup>_._</sup> 

(ii) _Assume that K has characteristic p, and let_ ( _R, R_<sup>+</sup> ) _be a p-finite perfectoid affinoid K-algebra, given as the completed perfection of the reduced affinoid K-algebra_ ( _S, S_<sup>+</sup> ) _of topologically finite type. Then R_ f´et<sup>_∼_</sup> = _S_ f´et _._ 

_Proof._ (i) Because finite ´etale covers, and morphisms between these, are finitely presented objects, we have 

(lim _−→_<sup>_Ai_[</sup><sup>_ϖ−_1])f´et</sup><sup>_∼_= 2</sup><sup>_−_lim</sup> _−→_<sup>_Ai_[</sup><sup>_ϖ−_1]f´et</sup><sup>_._</sup> 

On the other hand, _−→_ lim<sup>_Ai_ishenselianalong(</sup><sup>_ϖ_),hencetheleft-handsideagreeswith</sup> _A_ [ _ϖ_<sup>_−_1</sup> ]f´et by Proposition 7.4. (ii) From part (i), we know that 







**Proposition 7.6.** _If f_ : _X → Y is a strongly finite ´etale morphism of perfectoid spaces, then for any open affinoid perfectoid V ⊂ Y , its preimage U is affinoid perfectoid, and_ 



_is strongly finite ´etale._ 

_Proof._ Tilting the situation and using Theorem 5.25, we immediately reduce to the case that _K_ is of characteristic _p_ . Again, we replace _K_ by a perfectoid subfield to ensure that _R_<sup>+</sup> is a _K_<sup>_◦_</sup> -algebra in all cases. 

We may assume _Y_ = _V_ = Spa( _R, R_<sup>+</sup> ) is affinoid. Writing ( _R, R_<sup>+</sup> ) as the completion of the direct limit of p-finite perfectoid affinoid _K_ -algebras ( _Ri, Ri_<sup>+)asinLemma6.13,</sup> we see that _Y_ is already defined as a finite ´etale cover of some _Yi_ = Spa( _Ri, Ri_<sup>+):Indeed,</sup> there are finitely many rational subsets of _Y_ over which we have a finite ´etale cover; by Lemma 7.5 (i), these are defined over a finite level, and because _Y_ is quasi-separated, also the gluing data over intersections (as well as the cocycle condition) are defined over a finite level. Hence by Lemma 7.3 (ii), we are reduced to the case that ( _R, R_<sup>+</sup> ) is p-finite, given as the completed perfection of ( _S, S_<sup>+</sup> ). But then _X_ is already defined as a finite ´etale cover of _Z_ = Spa( _S, S_<sup>+</sup> ) by similar reasoning using Lemma 7.5 (ii), and we conclude by using the result for locally noetherian adic spaces, cf. [20], Example 1.6.6 (ii), and Lemma 7.3 (iv). □ 

Using Proposition 5.23, this shows that if _K_ is of characteristic _p_ , then the finite ´etale covers of an affinoid perfectoid space _X_ = Spa( _R, R_<sup>+</sup> ) are the same as the finite ´etale covers of _R_ . 

The same method also proves the following proposition. 

**Proposition 7.7.** _Assume that K is of characteristic p. Let f_ : _X → Y be an ´etale map of perfectoid spaces. Then for any x ∈ X, there exist affinoid perfectoid neighborhoods x ∈ U ⊂ X, f_ ( _U_ ) _⊂ V ⊂ Y , and an ´etale morphism of affinoid noetherian adic spaces U_<sup>0</sup> _→ V_<sup>0</sup> _over K, such that U_ = _U_<sup>0</sup> _×V_ 0 _V ._ 

_Proof._ We may assume that _X_ and _Y_ affinoid perfectoid, and that _X_ is a rational subdomain of a finite ´etale cover of _Y_ . Then one reduces to the p-finite case by the same argument as above, and hence to noetherian adic spaces. □ 

PETER SCHOLZE 

42 

**Corollary 7.8.** _Strongly ´etale maps of perfectoid spaces are open. If f_ : _X → Y and g_ : _Y → Z are strongly (finite) ´etale morphisms of perfectoid spaces, then the composite g ◦ f is strongly (finite) ´etale._ 

_Proof._ We may assume that _K_ has characteristic _p_ . The first part follows directly from the previous proposition and the result for locally noetherian adic spaces, cf. [20], Proposition 1.7.8. For the second part, argue as in the previous proposition for both _f_ and _g_ to reduce to the analogous result for locally noetherian adic spaces, [20], Proposition 1.6.7 (ii). □ 

The following theorem gives a strong form of Faltings’s almost purity theorem. 

**Theorem 7.9.** _Let_ ( _R, R_<sup>+</sup> ) _be a perfectoid affinoid K-algebra, and let X_ = Spa( _R, R_<sup>+</sup> ) _with tilt X_<sup>_♭_</sup> _._ 

(i) _For any open affinoid perfectoid subspace U ⊂ X, we have a fully faithful functor from the category of strongly finite ´etale covers of U to the category of finite ´etale covers of OX_ ( _U_ ) _, given by taking global sections._ 

(ii) _For any U , this functor is an equivalence of categories._ 

(iii) _For any finite ´etale cover S/R, S is perfectoid and S_<sup>_◦a_</sup> _is finite ´etale over R_<sup>_◦a_</sup> _. Moreover, S_<sup>_◦a_</sup> _is a uniformly almost finitely generated R_<sup>_◦a_</sup> _-module._ 

_Proof._ (i) By Proposition 7.6 and Theorem 5.25, the perfectoid spaces strongly finite ´etale over _U_ are the same as the finite ´etale _OX_ ( _U_ )<sup>_◦a_</sup> -algebras, which are a full subcategory of the finite ´etale _OX_ ( _U_ )-algebras. 

(ii) We may assume that _U_ = _X_ . Fix a finite ´etale _R_ -algebra _S_ . First we check that for any _x ∈ X_ , we can find an affinoid perfectoid neighborhood _x ∈ U ⊂ X_ and a strongly finite ´etale cover _V → U_ which gives via (i) the finite ´etale algebra _OX_ ( _U_ ) _⊗R S_ over _OX_ ( _U_ ). 

As a first step, note that we have an equivalence of categories between the direct limit of the category of finite ´etale _OX_ ( _U_ )-algebras over all affinoid perfectoid neighborhoods _U_ of _x_ and the category of finite ´etale covers of the completion _k_<sup>�</sup> ( _x_ ) of the residue field at _x_ , by Lemma 7.5 (i). The latter is a perfectoid field. 

By Theorem 3.7, the categories _k_<sup>�</sup> ( _x_ )f´et and _k_<sup>�</sup> ( _x_<sup>_♭_</sup> )f´et are equivalent, where _k_ ( _x_<sup>_♭_</sup> ) is the residue field of _X_<sup>_♭_</sup> at the point _x_<sup>_♭_</sup> corresponding to _x_ . Combining, we see that 



In particular, we can find _V_<sup>_♭_</sup> finite ´etale over _U_<sup>_♭_</sup> for some _U_ such that the pullbacks of _S_ to _k_<sup>�</sup> ( _x_ ) resp. of the global sections of _V_<sup>_♭_</sup> to _k_<sup>�</sup> ( _x_<sup>_♭_</sup> ) are tilts; but then, they are already identified over some smaller neighborhood. Shrinking _U_ , we untilt to get the desired strongly finite ´etale _V → U_ . This shows that there is a cover _X_ =<sup>�</sup> _Ui_ by finitely many rational subsets and strongly finite ´etale maps _Vi → Ui_ such that the global sections of _Vi_ are _Si_ = _OX_ ( _Ui_ ) _⊗R S_ . Let _Si_<sup>+betheintegralclosureof</sup><sup>_O_</sup> _X_<sup>+(</sup><sup>_Ui_)in</sup><sup>_Si_;then</sup><sup>_Vi_= Spa(</sup><sup>_Si, S_</sup> _i_<sup>+).</sup> 

By Lemma 7.3 (ii), the pullback of _Vi_ to some affinoid perfectoid _U_<sup>_′_</sup> _⊂ Ui_ has the same description, involving _OX_ ( _U_<sup>_′_</sup> ) _⊗R S_ , and hence the _Vi_ glue to some perfectoid space _Y_ over _X_ , and _Y → X_ is strongly finite ´etale. By Proposition 7.6, _Y_ is affinoid perfectoid, i.e. _Y_ = Spa( _A, A_<sup>+</sup> ), with ( _A, A_<sup>+</sup> ) an affinoid perfectoid _K_ -algebra. It suffices to show that _A_ = _S_ . But the sheaf property of _OY_ gives us an exact sequence 



PERFECTOID SPACES 

43 

On the other hand, the sheaf property for _OX_ gives an exact sequence 



Because _S_ is flat over _R_ , tensoring is exact, and the first sequence is identified with the second sequence after _⊗RS_ . Therefore _A_ = _S_ , as desired. 

(iii) This is a formal consequence of part (ii), Proposition 7.6 and Theorem 5.25. 



We see in particular that any (finite) ´etale morphism of perfectoid spaces is strongly (finite) ´etale. Now one can also pullback ´etale maps between adic spaces in characteristic 0. 

**Proposition 7.10.** _Parts (iii) and (iv) of Lemma 7.3 stay true in characteristic_ 0 _._ 

_Proof._ The same proof as for Lemma 7.3 works, using Theorem 7.9 (iii). □ 

Finally, we can define the ´etale site of a perfectoid space. 

**Definition 7.11.** _Let X be a perfectoid space. Then the ´etale site of X is the category X_ ´et _of perfectoid spaces which are ´etale over X, and coverings are given by topological coverings. The associated topos is denoted X_ ´et<sup>_∼._</sup> 

The previous results show that all conditions on a site are satisfied, and that a morphism _f_ : _X → Y_ of perfectoid spaces induces a morphism of sites _X_ ´et _→ Y_ ´et. Also, a morphism _f_ : _X → Y_ from a perfectoid space _X_ to a locally noetherian adic space _Y_ induces a morphism of sites _X_ ´et _→ Y_ ´et. 

After these preparations, we get the technical main result. 

**Theorem 7.12.** _Let X be a perfectoid space over K with tilt X_<sup>_♭_</sup> _over K_<sup>_♭_</sup> _. Then the tilting operation induces an isomorphism of sites X_ ´et<sup>_∼_</sup> = _X_ ´et<sup>_♭.Thisisomorphismisfunc-_</sup> _torial in X._ 

_Proof._ This is immediate. □ 

The almost vanishing of cohomology proved in Proposition 6.14 extends to the ´etale topology. **Proposition 7.13.** _For any perfectoid space X over K, the sheaf U �→OU_ ( _U_ ) _is a sheaf OX on X_ ´et _, and H_<sup>_i_</sup> ( _X_ ´et _, OX_<sup>_◦a_) = 0</sup><sup>_fori >_0</sup><sup>_ifXisaffinoidperfectoid._</sup> 

_Proof._ It suffices to check exactness of 



for any covering of an affinoid perfectoid _X_ by finitely many ´etale _Ui → X_ given as rational subsets of finite ´etale maps to rational subsets of _X_ . Under tilting, this reduces to the assertion in characteristic _p_ , and then to the assertion for p-finite ( _R, R_<sup>+</sup> ). In that case, one uses that the analogous sequence for noetherian adic spaces is exact up to a bounded _ϖ_ -power, and hence after taking the perfection almost exact. □ 

To make use of the ´etale site of a perfectoid space, we have to compare the ´etale sites of perfectoid spaces with those of locally noetherian adic spaces. This is possible under a certain assumption, cf. Section 2.4 of [20] for an analogous result. 

**Definition 7.14.** _Let X be a perfectoid space. Further, let Xi, i ∈ I, be a filtered inverse system of noetherian adic spaces over K, and let ϕi_ : _X → Xi, i ∈ I, be a map to the inverse system._ 

PETER SCHOLZE 

44 

_Then we write X ∼_ lim _←−_<sup>_Xiifthemappingofunderlyingtopologicalspaces|X|→_</sup> lim _←−_<sup>_|Xi|isahomeomorphism,andforanyx∈Xwithimagesxi∈Xi,themapof_</sup> _residue fields_ 



_has dense image._ 

_Remark_ 7.15 _._ We recall that by assumption all _Xi_ are qcqs. If _X ∼_ lim _←−_<sup>_Xi_,then</sup><sup>_|X|_is</sup> an inverse limit of spectral spaces with spectral transition maps, hence spectral, and in particular qcqs again. 

**Proposition 7.16.** _Let the situation be as in Definition 7.14, and let Y → Xi be an ´etale morphism of noetherian adic spaces. Then Y ×Xi X ∼_ lim _←−j≥i_<sup>_Y×XiXj._</sup> 

_Proof._ The same proof as for Remark 2.4.3 of [20] works. In particular, we note that in Definition 7.14, if _|X| →_ lim _←−_<sup>_|Xi|_isbijectiveandtheconditiononresiduefieldsis</sup> satisfied, then already _X ∼_ lim _←−_<sup>_Xi_,i.e.</sup><sup>_|X| →_lim</sup> _←−_<sup>_|Xi|_isahomeomorphism.</sup> □ With this definition, we have the following analogue of Proposition 2.4.4 of [20]. **Theorem 7.17.** _Let the situation be as in Definition 7.14. Then X_ ´et<sup>_∼isaprojective_</sup> _limit of the fibred topos_ ( _Xi,_<sup>_∼_</sup> ´et<sup>)</sup><sup>_i._</sup> 

_Proof._ The same proof as for Proposition 2.4.4 of [20] works, except that one uses that any ´etale morphism factors locally as the composite of an open immersion and a finite ´etale map instead of appealing to Corollary 1.7.3 of [20] on the top of page 128. The latter kind of morphisms can be descended to a finite level because of Lemma 7.5. □ 

As in [20], Corollary 2.4.6, this gives the following corollary. 

**Corollary 7.18.** _Let the situation be as in Definition 7.14, and let Fi be a sheaf of abelian groups on Xi,_ ´et _, with preimages Fj on Xj,_ ´et _for j ≥ i and F on X_ ´et _. Then the natural mapping_ 



_is bijective for all n ≥_ 0 _._ □ 

In some cases, one can even say more. 

**Corollary 7.19.** _Assume that in the situation of Definition 7.14 all transition maps Xj → Xi induce purely inseparable extensions on completed residue fields and homeomorphisms |Xj| →|Xi|. Then X_ ´et<sup>_∼isequivalenttoX_</sup> _i,_<sup>_∼_</sup> ´et<sup>_foranyi._</sup> 

_Proof._ Use the remark after Proposition 2.3.7 of [20]. □ 



Let us recall the definition of a toric variety, valid over any field _k_ . 

**Definition 8.1.** _A toric variety over k is a normal separated scheme X of finite type over k with an action of a split torus T_<sup>_∼_</sup> = G<sup>_k_</sup> _m_<sup>_onXandapointx∈X_(</sup><sup>_k_)</sup><sup>_withtrivial_</sup> _stabilizer in T , such that the T -orbit T_<sup>_∼_</sup> = _Tx_ = _U ⊂ X of x is open and dense._ 

We recall that toric varieties may be described in terms of fans. 

**Definition 8.2.** _Let N be a free abelian group of finite rank._ 

(i) _A strongly convex polyhedral cone σ in N ⊗_ R _is a subset of the form σ_ = R _≥_ 0 _x_ 1 + _. . ._ + R _≥_ 0 _xn for certain x_ 1 _, . . . , xn ∈ N , subject to the condition that σ contains no line through the origin._ 

PERFECTOID SPACES 

45 

(ii) _A fan_ Σ _in N ⊗_ R _is a nonempty finite collection of strongly convex polyhedral cones stable under taking faces, and such that the intersection of any two cones in_ Σ _is a face of both of them._ 

Let _M_ = Hom( _N,_ Z) be the dual lattice. To any strongly convex polyhedral cone _σ ⊂ N ⊗_ R, one gets the dual _σ_<sup>_∨_</sup> _⊂ M ⊗_ R, and we associate to _σ_ the variety 



We denote the function on _Uσ_ corresponding to _u ∈ σ_<sup>_∨_</sup> _∩ M_ by _χ_<sup>_u_</sup> . If _τ_ is a face of _σ_ , then _σ_<sup>_∨_</sup> _⊂ τ_<sup>_∨_</sup> , inducing an open immersion _Uτ → Uσ_ . These maps allow us to glue a variety _X_ Σ associated to any fan Σ. Note that _T_ = _U{_ 0 _}_ = Spec _k_ [ _M_ ] is a torus, which acts on _X_ Σ with open dense orbit _U{_ 0 _} ⊂ X_ Σ. Also _T_ has the base point 1 _∈ T_ , giving a point _x ∈ X_ ( _k_ ), making _X_ Σ a toric variety. Let us recall the classification of toric varieties. 

**Theorem 8.3.** _Any toric variety over k is canonically isomorphic to X_ Σ _for a unique fan_ Σ _in X∗_ ( _T_ ) _⊗_ R _._ 

We also need to recall some statements about divisors on toric varieties. 

**Definition/Proposition 8.4.** _Let {τi} ⊂_ Σ _be the_ 1 _-dimensional cones, and fix a generator vi ∈ τi ∩ N of τi ∩ N . Each τi gives rise to Uτi_<sup>_∼_</sup> = A<sup>1</sup> _×_ G _m_<sup>_k−_1</sup><sup>_,givingrisetoa_</sup> _T -invariant Weil divisor Di_ = _D_ ( _τi_ ) _on X_ Σ _, defined as the closure of {_ 0 _} ×_ G<sup>_k_</sup> _m_<sup>_−_1</sup><sup>_._</sup> 

_A T -Weil divisor is by definition an element of_<sup>�</sup> _i_<sup>Z</sup><sup>_Di.EveryWeildivisorisequiv-_</sup> _alent to a T -Weil divisor. If D_ =<sup>�</sup> _aiDi is a T -Weil divisor, then_ 



Now we adapt these definitions to the world of usual adic spaces, and to the world of perfectoid spaces. Assume first that _k_ is a complete nonarchimedean field, and let Σ be a fan as above. Then we can associate to Σ the adic space _X_ Σ<sup>adoffinitetypeover</sup><sup>_k_</sup> which is glued out of 



We note that this is not in general the adic space _X_ Σ<sup>adover</sup><sup>_k_associatedtothevariety</sup> _X_ Σ: For example, if _X_ Σ is just affine space, then _X_ Σ<sup>ad</sup> will be a closed unit ball. In general, let _X_ Σ _,k◦_ be the toric scheme over _k_<sup>_◦_</sup> associated to Σ. Let _X_<sup>ˆ</sup> Σ _,k◦_ be the formal completion of _X_ Σ _,k◦_ along its special fibre, which is an admissible formal scheme over _k_<sup>_◦_</sup> . Then _X_ Σ<sup>ad</sup> is the generic fibre _X_<sup>ˆ</sup> Σ<sup>ad</sup> _,k_<sup>_◦_associatedto</sup><sup>_X_ˆΣ</sup><sup>_,k◦_.Inparticular,if</sup><sup>_X_Σis</sup> proper, then _X_ Σ<sup>ad=</sup><sup>_X_ad</sup> Σ<sup>.</sup> 

Similarly, if _K_ is a perfectoid field, we can associate a perfectoid space _X_ Σ<sup>perf</sup> over _K_ to Σ, which is glued out of 

_Uσ_<sup>perf</sup> = Spa( _K⟨σ_<sup>_∨_</sup> _∩ M_ [ _p_<sup>_−_1</sup> ] _⟩, K_<sup>_◦_</sup> _⟨σ_<sup>_∨_</sup> _∩ M_ [ _p_<sup>_−_1</sup> ] _⟩_ ) _._ 

Note that on _X_ Σ<sup>perf</sup> , we have a sheaf _O_ ( _D_ ) for any _D ∈_<sup>�</sup> Z[ _p_<sup>_−_1</sup> ] _Di_ . Moreover, _H_<sup>0</sup> ( _X_ Σ<sup>perf</sup> _, O_ ( _D_ )) is the free Banach- _K_ -vector space with basis given by _{χ_<sup>_u_</sup> _}_ , where _u_ ranges over _u ∈ M_ [ _p_<sup>_−_1</sup> ] with _⟨u, vi⟩≥−ai_ . We have the following comparison statements. Note that any toric variety _X_ Σ comes with a map _ϕ_ : _X_ Σ _→ X_ Σ induced from multiplication by _p_ on _M_ ; the same applies to _X_ Σ<sup>ad,etc..Forclarity,weusesubscriptstodenotethefieldoverwhichweconsiderthe</sup> toric variety. 

**Theorem 8.5.** _Let K be a perfectoid field with tilt K_<sup>_♭_</sup> _._ 

PETER SCHOLZE 

46 



(ii) _The perfectoid space X_ Σ<sup>perf</sup> _,K_<sup>_canbewrittenas_</sup> 



(iii) _There is a homeomorphism of topological spaces_ 



(iv) _There is an isomorphism of ´etale topoi_ 



(v) _For any open subset U ⊂X_ Σ<sup>ad</sup> _,K_<sup>_withpreimageV⊂X_ad</sup> Σ _,K_<sup>_♭,wehaveamorphismof_</sup> _´etale topoi V_ ´et<sup>_∼→U_</sup> ´et<sup>_∼,givingacommutativediagram_</sup> 



_Proof._ This is an immediate consequence of our previous results: Part (i) can be checked on affinoid pieces, where it is an immediate generalization of Proposition 5.20. Part (ii) can be checked one affinoid pieces again, where it is easy. Then parts (iii) and (iv) follow from Theorem 7.17, Corollary 7.19 and the preservation of topological spaces and ´etale topoi under tilting. Finally, part (v) follows from Proposition 7.16, using the previous arguments. □ 

Let us denote by _π_ : _X_ Σ<sup>ad</sup> _,K_<sup>_♭→X_ad</sup> Σ _,K_<sup>theprojection,whichexistsontopological</sup> spaces and ´etale topoi. In the following, we restrict to proper smooth toric varieties for simplicity. 

**Proposition 8.6.** _Let X_ Σ _be a proper smooth toric variety. Let ℓ̸_ = _p be prime. Assume that K, and hence K_<sup>_♭_</sup> _, is algebraically closed. Then for all i ∈_ Z _, the projection map π induces an isomorphism_ 



_Proof._ This follows from part (iv) of the previous theorem combined with the observation that _ϕ_ : _X_ Σ<sup>ad</sup> _,K_<sup>_→X_</sup> Σ<sup>ad</sup> _,K_<sup>induces an isomorphism on cohomology with Z</sup><sup>_/ℓm_Z-coefficients.</sup> Using proper base change, this can be checked on _X_ Σ _,κ_ , where _κ_ is the residue field of _K_ . But here, _ϕ_ is purely inseparable, and hence induces an equivalence of ´etale topoi. □ We need the following approximation property. **Proposition 8.7.** _Assume that X_ Σ _,K is proper smooth. Let Y ⊂ X_ Σ _,K be a hypersurface. Let Y_<sup>˜</sup> _⊂ X_ Σ<sup>ad</sup> _,K_<sup>_be a small open neighborhood of Y .Then there exists a hypersurface_</sup> _Z ⊂ X_ Σ _,K♭ such that Z_<sup>ad</sup> _⊂ π_<sup>_−_1</sup> ( _Y_<sup>˜</sup> ) _. One can assume that Z is defined over a given dense subfield of K_<sup>_♭_</sup> _._ 

_Proof._ Let _D_ =<sup>�</sup> _aiDi_ be a _T_ -Weil divisor representing _Y_ . Let _f ∈ H_<sup>0</sup> ( _X_ Σ _,K, O_ ( _D_ )) be the equation with zero locus _Y_ . Consider the graded ring 



PERFECTOID SPACES 

47 

and let _R_ be its completion (with respect to the obvious _K_<sup>_◦_</sup> -submodule). Here �<sup>�</sup> denotes the Banach space direct sum. Then as in Proposition 5.20, _R_ is a perfectoid _K_ -algebra whose tilt is given by the similar construction over _K_<sup>_♭_</sup> . Note that _D_ is given combinatorially and hence transfers to _K_<sup>_♭_</sup> . 

We may assume that _Y_<sup>˜</sup> is given by 



for some _ϵ_ . In order to make sense of the inequality _|f_ ( _x_ ) _| ≤ ϵ_ , note that _X_ Σ _,K_ and _O_ ( _D_ ) have a tautological integral model over _K_<sup>_◦_</sup> (by applying the toric constructions over _K_<sup>_◦_</sup> ), which is enough to talk about absolute values: Trivialize the line bundle _O_ ( _D_ ) locally on the integral model to interpret _f_ as a function; any two different choices differ by a unit of _K_<sup>_◦_</sup> , and hence give the same absolute value. 

Now the analogue of Lemma 6.5 holds true for _R_ , with the same proof. This implies that we can find _g ∈ H_<sup>0</sup> ( _X_ Σ<sup>perf</sup> _,K_<sup>_♭, O_(</sup><sup>_D_))suchthat</sup> 



Let _k ⊂ K_<sup>_♭_</sup> be a dense subfield. Changing _g_ slightly, we can assume that 



By intersecting several hypersurfaces, one arrives at the following corollary. 

**Corollary 8.8.** _Assume that X_ Σ _,K is projective and smooth. Let Y ⊂ X_ Σ _,K be a set-theoretic complete intersection, i.e. Y is set-theoretically equal to an intersection Y_ 1 _∩. . .∩Yc of hypersurfaces Yi ⊂ X_ Σ _,K, where c is the codimension of Y . Let Y_<sup>˜</sup> _⊂ X_ Σ<sup>ad</sup> _,K be a small open neighborhood of Y . Then there exists a closed subvariety Z ⊂ X_ Σ _,K♭ such that Z_<sup>ad</sup> _⊂ π_<sup>_−_1</sup> ( _Y_<sup>˜</sup> ) _with_ dim _Z_ = dim _Y . One can assume that Z is defined over a given dense subfield of K_<sup>_♭_</sup> _._ 

_Proof._ The only nontrivial point is to check that the intersection over _K_<sup>_♭_</sup> will be nonempty; if the dimension was too large, one can also just cut by further hypersurfaces. For nonemptiness, choose an ample line bundle to define a notion of degree of subvarieties; then the degree of a complete intersection is determined combinatorially. As _Y_ has positive degree, so has the corresponding complete intersection over _K_<sup>_♭_</sup> , and in particular is nonempty. □ 

# 9. The weight-monodromy conjecture 

We first recall some facts about _ℓ_ -adic representations of the absolute Galois group _Gk_ = Gal( _k/k_<sup>¯</sup> ) of a local field _k_ of residue characteristic _p_ , cf. [24]. Let _q_ be the cardinality of the residue field of _k_ . Recall that the maximal pro- _ℓ_ -quotient of the inertia subgroup _Ik ⊂ Gk_ is given by the quotient _tℓ_ : _Ik →_ Z _ℓ_ (1), which is the inverse limit of the homomorphisms _tℓ,n_ : _Ik → µℓn_ defined by choosing a system of _ℓ_<sup>_n_</sup> -th roots _ϖ_<sup>1</sup><sup>_/ℓn_</sup> of a uniformizer _ϖ_ of _k_ , and requiring 



for all _σ ∈ Ik_ . Now recall Grothendieck’s quasi-unipotence theorem. 

PETER SCHOLZE 

48 

**Proposition 9.1.** _Let V be a finite-dimensional_ Q<sup>¯</sup> _ℓ-representation of Gk, given by a map ρ_ : _Gk →_ GL( _V_ ) _. Then there is an open subgroup I_ 1 _⊂ Ik such that for all σ ∈ I_ 1 _, the element ρ_ ( _σ_ ) _∈_ GL( _V_ ) _is unipotent, and in this case there is a unique nilpotent morphism N_ : _V → V_ ( _−_ 1) _such that for all σ ∈ I_ 1 _,_ 



We fix an isomorphism Q _ℓ_ (1)<sup>_∼_</sup> = Q _ℓ_ in order to consider _N_ as a nilpotent endomorphism of _V_ . Changing the choice of isomorphism Q _ℓ_ (1)<sup>_∼_</sup> = Q _ℓ_ replaces _N_ by a scalar multiple, which will have no effect on the following discussion. From uniqueness of _N_ , it follows that for any geometric Frobenius element Φ _∈ Gk_ , we have _N_ Φ = _q_ Φ _N_ . 

Also recall the general monodromy filtration. 

**Definition/Proposition 9.2.** _Let V be a finite-dimensional vector space over any field, and let N_ : _V → V be a nilpotent morphism. Then there is a unique separated and exhaustive increasing filtration_ Fil<sup>_N_</sup> _i_<sup>_V⊂V ,i ∈_Z</sup><sup>_,calledthemonodromyfiltration,such_</sup> _that N_ (Fil<sup>_N_</sup> _i_<sup>_V_)</sup><sup>_⊂_Fil</sup> _i_<sup>_N_</sup> _−_ 2<sup>_Vforalli ∈_Z</sup><sup>_and_gr</sup><sup>_N_</sup> _i_<sup>_V∼_= gr</sup><sup>_N_</sup> _−i_<sup>_VviaNiforalli ≥_0</sup><sup>_._</sup> 

In fact, we have the formula 



for the monodromy filtration. Now we can formulate the weight-monodromy conjecture. **Conjecture 9.3** (Deligne, [9]) **.** _Let X be a proper smooth variety over k, and let V_ = _H_<sup>_i_</sup> ( _Xk_ ¯ _,_ Q<sup>¯</sup> _ℓ_ ) _. Then for all j ∈_ Z _and for any geometric Frobenius_ Φ _∈ Gk, all eigenvalues of_ Φ _on_ gr<sup>_N_</sup> _j_<sup>_VareWeilnumbersofweighti_+</sup><sup>_j,i.e.algebraicnumbersαsuchthat_</sup> _|α|_ = _q_<sup>(</sup><sup>_i_+</sup><sup>_j_)</sup><sup>_/_2</sup> _for all complex absolute values._ 

We note that in order to prove this conjecture, one is allowed to replace _k_ by a finite extension. Using the formalism of _ζ_ - and _L_ -functions, the conjecture has the following interpretation. Let K be a global field, and let _X/_ K be a proper smooth variety. Choose some integer _i_ . Recall that the _L_ -function associated to the _i_ -th _ℓ_ -adic cohomology group _H_<sup>_i_</sup> ( _X_ ) = _H_<sup>_i_</sup> ( _X_ K¯ _,_ Q<sup>¯</sup> _ℓ_ ) of _X_ is defined as a product 



where the product runs over all places _v_ of _K_ . Let us recall the definition of the local factor at a finite prime _v_ not dividing _ℓ_ , whose local field is _k_ : 



At primes of good reduction, the Weil conjectures imply that all poles of this expression have real part 2<sup>_<u>i</u>_.Moreover, one checks in the usual way that hence the product defining</sup> _L_ ( _H_<sup>_i_</sup> ( _X_ ) _, s_ ) is absolutely convergent when the real part of _s_ is greater than 2<sup>_<u>i</u>_+1, except</sup> possibly for finitely many factors. The weight-monodromy conjecture implies that all other local factors will not have any poles of real part greater than 2<sup>_<u>i</u>_.</sup> Over equal characteristic local fields, Deligne, [10], turned this argument into a proof: 

**Theorem 9.4.** _Let C be a curve over_ F _q, x ∈ C_ (F _q_ ) _, such that k is the local field of C at x. Let X be a proper smooth scheme over C \ {x}. Then the weight-monodromy conjecture holds true for Xk_ = _X ×C\{x}_ Spec _k._ 

Let us give a brief summary of the proof. Let _f_ : _X → C \ {x}_ be the proper smooth morphism. Possibly replacing _C_ by a finite cover, we may assume that the action of _Ik_ on _V_ = _H_<sup>_i_</sup> ( _Xk_ ¯ _,_ Q<sup>¯</sup> _ℓ_ ) is unipotent. One considers the local system _R_<sup>_i_</sup> _f∗_ Q<sup>¯</sup> _ℓ_ on _C \{x}_ . By the Weil conjectures, this sheaf is pure of weight _i_ . From the formalism of _L_ -functions for sheaves over curves, one deduces semicontinuity of weights, which in this situation 

PERFECTOID SPACES 

49 

means that on the invariants _V_<sup>_Ik_</sup> of _V_ = _H_<sup>_i_</sup> ( _Xk_ ¯ _,_ Q<sup>¯</sup> _ℓ_ ), all occuring weights are _≤ i_ . A similar property holds true for all tensor powers of _V_ , and for all tensor powers of the dual _V_<sup>_∨_</sup> . Then one applies the following lemma from linear algebra, which applies for all local fields _k_ . 

**Lemma 9.5.** _Let V be an ℓ-adic representation of Gk, on which Ik acts unipotently. Then_ gr<sup>_N_</sup> _j_<sup>_Vispureofweighti_+</sup><sup>_jforallj∈_Z</sup><sup>_ifandonlyifforallj≥_0</sup><sup>_,allweights_</sup> _on_ ( _V_<sup>_⊗j_</sup> )<sup>_Ik_</sup> _are at most ij, and all weights on_ (( _V_<sup>_∨_</sup> )<sup>_⊗j_</sup> )<sup>_Ik_</sup> _are at most −ij._ 

Our main theorem is the following. 

**Theorem 9.6.** _Let k be a local field of characteristic_ 0 _. Let Y be a geometrically connected proper smooth variety over k such that Y is a set-theoretic complete intersection in a projective smooth toric variety X_ Σ _. Then the weight-monodromy conjecture is true for Y ._ 

_Proof._ Let _ϖ ∈ k_ be a uniformizer, and let _K_ be the completion of _k_ ( _ϖ_<sup>1</sup><sup>_/p∞_</sup> ); then _K_ is perfectoid. Let _K_<sup>_♭_</sup> be its tilt. Then _K_<sup>_♭_</sup> is the completed perfection of _k_<sup>_′_</sup> = F _q_ (( _t_ )), where _t_ = _ϖ_<sup>_♭_</sup> . This gives an isomorphism between the absolute Galois groups of _K_ and _k_<sup>_′_</sup> . The notion of weights and the monodromy operator _N_ is compatible with this isomorphism of Galois groups. 

By Theorem 3.6 a) of [21], there is some open neighborhood _Y_<sup>˜</sup> of _YK_<sup>adin</sup><sup>_X_</sup> Σ<sup>ad</sup> _,K_<sup>such</sup> that _Y_<sup>˜</sup> C _p_ and _Y_ C<sup>ad</sup> _p_<sup>havethesameZ</sup><sup>_/ℓ_Z-cohomology.Byinduction,theyhavethesame</sup> Z _/ℓ_<sup>_m_</sup> Z-cohomology for all _m ≥_ 1. Also recall the following comparison theorem. 

**Theorem 9.7** ([20, Theorem 3.8.1]) **.** _Let X be an algebraic variety over an algebraically closed nonarchimedean field k, with associated adic space X_<sup>ad</sup> _. Then_ 



By Corollary 8.8, there is some closed subvariety _Z ⊂ X_ Σ _,K♭_ such that _Z_<sup>ad</sup> _⊂ π_<sup>_−_1</sup> ( _Y_<sup>˜</sup> ) and dim _Z_ = dim _Y_ . Moreover, we can assume that _Z_ is defined over a global field and geometrically irreducible. Let _Z_<sup>_′_</sup> be a projective smooth alteration of _Z_ . We get a commutative diagram of ´etale topoi of adic spaces 



There is a canonical action of the absolute Galois group _G_ = _GK_ = _GK♭_ on this diagram such that all morphisms are _G_ -equivariant. Using the comparison theorem, this induces a _G_ -equivariant map 



compatible with the cup product. Formally taking the inverse limit and tensoring with Q¯ _ℓ_ , it follows that we get a _G_ -equivariant map 



**Lemma 9.8.** _For i_ = 2 dim _Y , this is an isomorphism._ 

PETER SCHOLZE 

50 

_Proof._ For all _m_ , we have a commutative diagram 



The isomorphism in the top row is from Proposition 8.6. We can pass to the inverse limit over _m_ and tensor with Q<sup>¯</sup> _ℓ_ . If 



is not an isomorphism, it is the zero map, and hence the diagram implies that the restriction map 

_H_<sup>2 dim</sup><sup>_Y_</sup> ( _X_ Σ _,_ C _♭p,_ ´et _,_ Q<sup>¯</sup> _ℓ_ ) _→ H_<sup>2 dim</sup><sup>_Y_</sup> ( _Z_ C<sup>_′♭_</sup> _p,_ ´et<sup>_,_Q¯</sup><sup>_ℓ_)</sup> is the zero map as well. But the dim _Y_ -th power of the first Chern class of an ample line bundle on _X_ Σ _,_ C _♭p_ will have nonzero image in _H_<sup>2 dim</sup><sup>_Y_</sup> ( _Z_ C<sup>_′♭_</sup> _p,_ ´et<sup>_,_Q¯</sup><sup>_ℓ_).</sup> □ 

Now the Poincar´e duality pairing implies that _H_<sup>_i_</sup> ( _Y_ C _p,_ ´et _,_ Q<sup>¯</sup> _ℓ_ ) is a direct summand of _H_<sup>_i_</sup> ( _Z_ C<sup>_′♭_</sup> _p,_ ´et<sup>_,_Q¯</sup><sup>_ℓ_).ByDeligne’stheorem,</sup><sup>_Hi_(</sup><sup>_Z_</sup> C<sup>_′♭_</sup> _p,_ ´et<sup>_,_Q¯</sup><sup>_ℓ_)satisfiestheweight-monodromy</sup> conjecture, and hence so does its direct summand _H_<sup>_i_</sup> ( _Y_ C _p,_ ´et _,_ Q<sup>¯</sup> _ℓ_ ). □ 

# References 

- [1] V. G. Berkovich. _Spectral theory and analytic geometry over non-Archimedean fields_ , volume 33 of _Mathematical Surveys and Monographs_ . American Mathematical Society, Providence, RI, 1990. 

- [2] S. Bosch, U. G¨untzer, and R. Remmert. _Non-Archimedean analysis_ , volume 261 of _Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences]_ . SpringerVerlag, Berlin, 1984. A systematic approach to rigid analytic geometry. 

- [3] S. Bosch and W. L¨utkebohmert. Formal and rigid geometry. I. Rigid spaces. _Math. Ann._ , 295(2):291– 317, 1993. 

- [4] P. Boyer. Monodromie du faisceau pervers des cycles ´evanescents de quelques vari´et´es de Shimura simples. _Invent. Math._ , 177(2):239–280, 2009. 

- [5] P. Boyer. Conjecture de monodromie-poids pour quelques vari´et´es de Shimura unitaires. _Compos. Math._ , 146(2):367–403, 2010. 

- [6] A. Caraiani. Local-global compatibility and the action of monodromy on nearby cycles. arXiv:1010.2188. 

- [7] J.-F. Dat. Th´eorie de Lubin-Tate non-ab´elienne et repr´esentations elliptiques. _Invent. Math._ , 169(1):75–152, 2007. 

- [8] A. J. de Jong. Smoothness, semi-stability and alterations. _Inst. Hautes Etudes_<sup>_´_</sup> _Sci. Publ. Math._ , (83):51–93, 1996. 

- [9] P. Deligne. Th´eorie de Hodge. I. In _Actes du Congr`es International des Math´ematiciens (Nice, 1970), Tome 1_ , pages 425–430. Gauthier-Villars, Paris, 1971. 

- [10] P. Deligne. La conjecture de Weil. II. _Inst. Hautes Etudes_<sup>_´_</sup> _Sci. Publ. Math._ , (52):137–252, 1980. 

- [11] G. Faltings. _p_ -adic Hodge theory. _J. Amer. Math. Soc._ , 1(1):255–299, 1988. 

- [12] G. Faltings. Almost ´etale extensions. _Ast´erisque_ , (279):185–270, 2002. Cohomologies _p_ -adiques et applications arithm´etiques, II. 

- [13] J.-M. Fontaine and J.-P. Wintenberger. Extensions alg´ebrique et corps des normes des extensions APF des corps locaux. _C. R. Acad. Sci. Paris S´er. A-B_ , 288(8):A441–A444, 1979. 

- [14] O. Gabber and L. Ramero. _Almost ring theory_ , volume 1800 of _Lecture Notes in Mathematics_ . Springer-Verlag, Berlin, 2003. 

- [15] M. Harris and R. Taylor. _The geometry and cohomology of some simple Shimura varieties_ , volume 151 of _Annals of Mathematics Studies_ . Princeton University Press, Princeton, NJ, 2001. With an appendix by Vladimir G. Berkovich. 

PERFECTOID SPACES 51 

- [16] E. Hellmann. On arithmetic families of filtered _ϕ_ -modules and crystalline representations. 2011. arXiv:1010.4577. 

- [17] M. Hochster. Prime ideal structure in commutative rings. _Trans. Amer. Math. Soc._ , 142:43–60, 1969. 

- [18] R. Huber. Continuous valuations. _Math. Z._ , 212(3):455–477, 1993. 

- [19] R. Huber. A generalization of formal schemes and rigid analytic varieties. _Math. Z._ , 217(4):513–551, 1994. 

- [20] R. Huber. _Etale_<sup>_´_</sup> _cohomology of rigid analytic varieties and adic spaces_ . Aspects of Mathematics, E30. Friedr. Vieweg & Sohn, Braunschweig, 1996. 

- [21] R. Huber. A finiteness result for direct image sheaves on the ´etale site of rigid analytic varieties. _J. Algebraic Geom._ , 7(2):359–403, 1998. 

- [22] L. Illusie. _Complexe cotangent et d´eformations. I_ . Lecture Notes in Mathematics, Vol. 239. SpringerVerlag, Berlin, 1971. 

- [23] L. Illusie. _Complexe cotangent et d´eformations. II_ . Lecture Notes in Mathematics, Vol. 283. SpringerVerlag, Berlin, 1972. 

- [24] L. Illusie. Autour du th´eor`eme de monodromie locale. _Ast´erisque_ , (223):9–57, 1994. P´eriodes _p_ - adiques (Bures-sur-Yvette, 1988). 

- [25] T. Ito. Weight-monodromy conjecture for _p_ -adically uniformized varieties. _Invent. Math._ , 159(3):607–656, 2005. 

- [26] T. Ito. Weight-monodromy conjecture over equal characteristic local fields. _Amer. J. Math._ , 127(3):647–658, 2005. 

- [27] K. Kedlaya and R. Liu. Relative _p_ -adic Hodge theory, I: Foundations. http://math.mit.edu/ _∼_ kedlaya/papers/relative-padic-Hodge1.pdf. 

- [28] D. Quillen. On the (co-) homology of commutative rings. In _Applications of Categorical Algebra (Proc. Sympos. Pure Math., Vol. XVII, New York, 1968)_ , pages 65–87. Amer. Math. Soc., Providence, R.I., 1970. 

- [29] M. Rapoport and T. Zink. Uber<sup>¨</sup> die lokale Zetafunktion von Shimuravariet¨aten. Monodromiefiltration und verschwindende Zyklen in ungleicher Charakteristik. _Invent. Math._ , 68(1):21–101, 1982. 

- [30] S. W. Shin. Galois representations arising from some compact Shimura varieties. _Ann. of Math. (2)_ , 173(3):1645–1741, 2011. 

- [31] J. Tate. Rigid analytic spaces. _Invent. Math._ , 12:257–289, 1971. 

- [32] R. Taylor and T. Yoshida. Compatibility of local and global Langlands correspondences. _J. Amer. Math. Soc._ , 20(2):467–493, 2007. 

- [33] T. Terasoma. Monodromy weight filtration is independent of _ℓ_ . 1998. arXiv:math/9802051. 

