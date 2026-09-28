# **The sphere packing problem in dimension 8** 

Maryna S. Viazovska 

April 5, 2017 

In this paper we prove that no packing of unit balls in Euclidean space R<sup>8</sup> has density greater than that of the _E_ 8-lattice packing. 

**Keywords:** Sphere packing, Modular forms, Fourier analysis **AMS subject classification:** 52C17, 11F03, 11F30 

## **1 Introduction** 

The sphere packing constant measures which portion of _d_ -dimensional Euclidean space can be covered by non-overlapping unit balls. More precisely, let R<sup>_d_</sup> be the Euclidean vector space equipped with distance _∥· ∥_ and Lebesgue measure Vol( _·_ ). For _x ∈_ R<sup>_d_</sup> and _r ∈_ R _>_ 0 we denote by _Bd_ ( _x, r_ ) the open ball in R<sup>_d_</sup> with center _x_ and radius _r_ . Let _X ⊂_ R<sup>_d_</sup> be a discrete set of points such that _∥x − y∥≥_ 2 for any distinct _x, y ∈ X_ . Then the union 



is a _sphere packing_ . If _X_ is a lattice in R<sup>_d_</sup> then we say that _P_ is a _lattice sphere packing_ . The _finite density_ of a packing _P_ is defined as 



We define the _density_ of a packing _P_ as the limit superior 



The number be want to know is the supremum over all possible packing densities 



1 

### called the _sphere packing constant_ . 

For which dimensions do we know the exact value of ∆ _d_ ? Trivially, in dimension 1 we have ∆1 = 1. It has long been known that a best packing in dimension 2 is the familiar hexagonal lattice packing, in which each disk is touching six others. The first proof of this result was given by A. Thue at the beginning ot twentieth century [18]. However, his proof was considered by some experts incomplete. A rigorous proof was given by L. Fejes T´oth in 1940s [10]. The density of the hexagonal lattice packing is _~~√~~_ _<u>π</u>_ 12<sup>,therefore∆2=</sup> _~~√~~_ _<u>π</u>_ 12<sup>_≈_0</sup><sup>_._90690.Thepackingproblemindimension3turned</sup> out to be more difficult. Johannes Kepler conjectured in his essay “On the six-cornered snowflake” (1611) that no arrangement of equally sized spheres filling space has density greater than _~~√~~_ _<u>π</u>_ 18<sup>.Thisdensityisattainedbytheface-centeredcubicpackingandalso</sup> by uncountably many non-lattice packings. The Kepler conjecture was famously proven by T. Hales in 1998 [11] and therefore we know that ∆3 = _~~√~~_ _<u>π</u>_ 18<sup>_≈_0</sup><sup>_._74048.In 2015 Hales</sup> and his 21 coauthors published a complete formal proof of the Kepler conjecture that can be verified by automated proof checking software. Before now, the exact values of the sphere packing constants in all dimensions greater than 3 have been unknown. A list of conjectural best packings in dimensions less than 10 can be found in [6]. Upper bounds for the sphere packing constants ∆ _d_ as _d ≤_ 36 are given in [4]. Surprisingly enough, these upper bounds and known lower bounds on ∆ _d_ are extremely close in dimensions _d_ = 8 and _d_ = 24. 

The main result of this paper is the proof that 



This is the density of the _E_ 8-lattice sphere packing. Recall that the _E_ 8-lattice Λ8 _⊂_ R<sup>8</sup> is given by 



Λ8 is the unique up to isometry positive-definite, even, unimodular lattice of rank 8. The name derives from the fact that it is the root lattice of the _E_ 8 root system. The minimal distance between two points in Λ8 is _√_ 2. The _E_ 8-lattice sphere packing is the packing of unit balls with centers at _~~√~~_ <u>12</u><sup>Λ8</sup><sup>_._Ourmainresultis</sup> 

**Theorem 1.** _No packing of unit balls in Euclidean space_ R<sup>8</sup> _has density greater than that of the E_ 8 _-lattice packing._ 

Furthermore, our proof of Theorem 1 combined with arguments given in [4, Section 8] implies that the _E_ 8-lattice sphere packing is the unique periodic packing of maximal density. 

The paper is organized as follows. In Section 2 we explain the idea of the proof of Theorem 1 and describe the methods we use. In Section 3 we give a brief overview of the theory of modular forms. In Section 4 we construct supplementary radial functions _a_ , _b_ : R<sup>8</sup> _→ i_ R, which are eigenfunctions of the Fourier transform and have double zeroes at 

2 

almost all points of Λ8. This construction is crucial for our proof of Theorem 1. Finally, in Section 5 we complete the proof. 

## **2 Linear programming bounds** 

Our proof of Theorem 1 is based on linear programming bounds. This technique was successfully applied to obtain upper bounds in a wide range of discrete optimization problems such as error-correcting codes [7], equal weight quadrature formulas [8], and spherical codes [13, 16]. In exceptional cases linear programming bounds are optimal [5]. However, in general linear programming bounds are not sharp and it is an open question how big the errors of such bounds can be. It is known [2] that the linear programming bounds for the minimal number of points in an equal weight quadrature formula on the sphere _S_<sup>_d_</sup> are asymptotically optimal up to a constant depending on _d_ . Linear programming bounds can also be applied to the sphere packing problem. Kabatiansky and Levenshtein [13] deduced upper bounds for sphere packing from their results on spherical codes. 

In 2003 Cohn and Elkies [4] developed linear programming bounds that apply directly to sphere packings. Using their new method they improved the previously known upper bounds for the sphere packing constant in dimensions from 4 to 36. The most striking results obtained by this technique are upper bounds for dimensions 8 and 24. For example, their upper bound for ∆8 was only 1 _._ 000001 times greater than the lower bound, which is given by the density of the _E_ 8 sphere packing. This bound can be improved even further by more extensive computer computations. 

We explain the Cohn–Elkies linear programming bounds in more detail. To this end we recall a few definitions from Fourier analysis. The _Fourier transform_ of an _L_<sup>1</sup> function _f_ : R<sup>_d_</sup> _→_ C is defined as 



where _x · y_ = <u>12</u><sup>_∥x∥_2+</sup><sup><u>1</u></sup> 2<sup>_∥y∥_2</sup><sup>_−_</sup><sup><u>1</u></sup> 2<sup>_∥x−y∥_2isthestandardscalarproductinR</sup><sup>_d_.</sup> A _C_<sup>_∞_</sup> function _f_ : R<sup>_d_</sup> _→_ C is called a _Schwartz function_ if it tends to zero as _∥x∥→∞_ faster then any inverse power of _∥x∥_ , and the same holds for all partial derivatives of _f_ . The set of all Schwartz functions is called the _Schwartz space_ . The Fourier transform is an automorphism of this space. We will also need the following wider class of functions. We say that a function _f_ : R<sup>_d_</sup> _→_ C is _admissible_ if there is a constant _δ >_ 0 such that _|f_ ( _x_ ) _|_ and _|f_<sup>�</sup> ( _x_ ) _|_ are bounded above by a constant times (1 + _|x|_ )<sup>_−d−δ_</sup> . The following theorem is the key result of [4]: 

**Theorem 2.** _(Cohn, Elkies [4]) Suppose that f_ : R<sup>_d_</sup> _→_ R _is an admissible function, is not identically zero, and satisfies:_ 



3 

_and_ 



_Then the density of d-dimensional sphere packings is bounded above by_ 



Without loss of generality we can assume that a function _f_ in Theorem 2 is radial, i. e. its value at each point depends only on the distance between the point and the origin [4, p. 695]. For a radial function _f_ 0 : R<sup>_d_</sup> _→_ R we will denote by _f_ 0( _r_ ) the common value of _f_ 0 on vectors of length _r_ . Henceforth we assume _d_ = 8. The Poisson summation formula implies 



Hence, if a function _f_ satisfies conditions (1) and (2) then 



We say that an admissible function _f_ : R<sup>8</sup> _→_ R is _optimal_ if it satisfies (1), (2) and _f_ (0) _/f_<sup>�</sup> (0) = 2<sup>4</sup> . 

The main step in our proof of Theorem 1 is the explicit construction of an optimal function. It will be convenient for us to scale this function by _√_ 2. 

**Theorem 3.** _There exists a radial Schwartz function g_ : R<sup>8</sup> _→_ R _which satisfies:_ 







_Moreover, the values g_ ( _x_ ) _and g_ �( _x_ ) _do not vanish for all vectors x with ∥x∥_<sup>2</sup> _∈/_ 2Z _>_ 0 _._ 

Theorem 2 applied to the optimal function _f_ ( _x_ ) = _g_ ( _√_ 2 _x_ ) immediately implies Theorem 1. Additionally, the function _g_ satisfies the conclusions of [4, Conjecture 8.1]. This implies the uniqueness of the densest periodic sphere packing in R<sup>8</sup> . 

Let us briefly explain our strategy for the proof of Theorem 3. First, we observe that conditions (3)–(5) imply additional properties of the function _g_ . Suppose that there exists a Schwartz function _g_ such that the conditions (3)–(5) hold. The Poisson summation formula states 



Since _∥ℓ∥≥ √_ 2 for all _ℓ ∈_ Λ8 _\{_ 0 _}_ , conditions (3) and (5) imply 



4 

On the other hand, conditions (4) and (5) imply 



Therefore, we deduce that _g_ ( _ℓ_ ) = _g_ �( _ℓ_ ) = 0 for all _ℓ ∈_ Λ8 _\{_ 0 _}_ . Moreover, the first derivatives _drd_<sup>_g_(</sup><sup>_r_)and</sup> _drd_<sup>_g_�(</sup><sup>_r_)alsovanishatallΛ8-latticepointsoflengthbiggerthan</sup> _√_ 2. We will say that _g_ and _g_ � have double zeroes at these points. This property gives us a hint on constructing the function _g_ explicitly. 

In Section 5 a function _g_ satisfying (3)–(5) is given in a closed form. Namely, it is defined as an integral transform (Laplace transform) of a _modular form_ of a certain kind. The next section is a brief introduction to the theory of modular forms. 

## **3 Modular forms** 

Let H be the upper half-plane _{z ∈_ C _|_ Im ( _z_ ) _>_ 0 _}_ . The modular group Γ(1) := PSL2(Z) acts on H by linear fractional transformations 



Let _N_ be a positive integer. The _level N principal congruence subgroup_ of Γ(1) is 



A subgroup Γ _⊂_ Γ(1) is called a _congruence subgroup_ if Γ( _N_ ) _⊂_ Γ for some _N ∈_ N. An important example of a congruence subgroup is 



Let _z ∈_ H, _k ∈_ Z, and � _ac db_ � _∈_ SL2(Z). The _automorphy factor_ of weight _k_ is defined as 



The automorphy factor satisfies the _chain rule_ 



Let _F_ be a function on H and _γ ∈_ PSL2(Z). Then the _slash operator_ acts on _F_ by 



The chain rule implies 



A _(holomorphic) modular form_ of integer weight _k_ and congruence subgroup Γ is a holomorphic function _f_ : H _→_ C such that: 

5 

1. _f |kγ_ = _f_ for all _γ ∈_ Γ and 

2. for each _α ∈_ Γ(1) the function _f |kα_ has Fourier expansion 



for some _nα ∈_ N and Fourier coefficients _cf_ ( _α, m_ ) _∈_ C. 

Let _Mk_ (Γ) be the space of modular forms of weight _k_ for the congruence subgroup Γ. A key fact in the theory of modular forms is that the spaces _Mk_ (Γ) are finite dimensional. We consider several examples of modular forms. For an even integer _k ≥_ 4 we define the _weight k Eisenstein series_ as 



Since the sum converges absolutely, it is easy to see that _Ek ∈ Mk_ (Γ(1)). The Eisenstein series possesses the Fourier expansion 



where _σk−_ 1( _n_ ) =<sup>�</sup> _d|n_<sup>_dk−_1.Inparticular,wehave</sup> 



The infinite sum (9) does not converge absolutely for _k_ = 2. On the other hand, the expression (10) converges to a holomorphic function on the upper half-plane and therefore we set 



This function is not modular, but it satisfies 



The proof of this identity can be found in [20, Section 2.3]. The weight two Eisenstein series _E_ 2 is an example of a _quasimodular form_ [20, Section 5.1]. 

6 

Another example of modular forms we consider are _theta functions_ [20, Section 3.1]. We define three theta functions (so-called “Thetanullwerte”) as 



The group Γ(1) is generated by the elements _T_ = (<sup>1</sup> 0<sup>1</sup> 1<sup>) and</sup><sup>_S_=</sup> � _−_ 01 10 �. These elements act on the fourth powers of the theta functions in the following way 





and 





Moreover, these three theta functions satisfy the _Jacobi identity_ 



The theta functions _θ_ 00<sup>4</sup><sup>_, θ_</sup> 01<sup>4,and</sup><sup>_θ_</sup> 10<sup>4belongto</sup><sup>_M_2(Γ(2)).</sup> 

A _weakly-holomorphic modular form_ of integer weight _k_ and congruence subgroup Γ is a holomorphic function _f_ : H _→_ C such that: 

1. _f |kγ_ = _f_ for all _γ ∈_ Γ, 

2. for each _α ∈_ Γ(1) the function _f |kα_ has Fourier expansion 



for some _n_ 0 _∈_ Z and _nα ∈_ N. 

For an _m_ -periodic holomorphic function _f_ and _n ∈ m_<sup><u>1</u>Zwewilldenotethe</sup><sup>_n_-thFourier</sup> coefficient of _f_ by _cf_ ( _n_ ) so that 



7 

We denote the space of weakly-holomorphic modular forms of weight _k_ and group Γ by _Mk_<sup>!(Γ).Thespaces</sup><sup>_M_</sup> _k_<sup>!(Γ)areinfinitedimensional.Probablythemostfamousweakly-</sup> holomorphic modular form is the _elliptic j-invariant_ 



This function belongs to _M_ 0<sup>!(Γ(1))andhastheFourierexpansion</sup> 



where _q_ = _e_<sup>2</sup><sup>_πiz_</sup> . Using a simple computer algebra system such as PARI GP or Mathematica one can compute the first hundred terms of this Fourier expansion within a few seconds. An important question is to find an asymptotic formula for _cj_ ( _n_ ), the _n_ -th Fourier coefficient of _j_ . Using the Hardy-Ramanujan circle method [17, p. 460 – 461] or the non-holomorphic Poincar´e series [15] one can show that 



where 



and _Iα_ ( _x_ ) denotes the modified Bessel function of the first kind defined as in [1, Section 9.6]. A similar convergent asymptotic expansion holds for the Fourier coefficients of any weakly holomorphic modular form [12, p.660 – 662], [3, Propositions 1.10 and 1.12]. Such a convergent expansion implies effective estimates for the Fourier coefficients. 

For a comprehensive introduction to the theory of modular forms we refer the reader to [20] and [9]. 

## **4 Fourier eigenfunctions with double zeroes at lattice points** 

In this section we construct two radial Schwartz functions _a, b_ : R<sup>8</sup> _→ i_ R such that 





which double zeroes at all Λ8-vectors of length greater than _√_ 2. Recall that each vector of Λ8 has length _√_ 2 _n_ for some _n ∈_ N _≥_ 0. We define _a_ and _b_ so that their values are purely imaginary because this simplifies some of our computations. We will show in Section 5 that an appropriate linear combination of functions _a_ and _b_ satisfies conditions (3)–(5). 

8 

First, we will define the function _a_ . To this end we consider the following weakly holomorphic modular forms: 



The modular form _E_ 4<sup>3</sup><sup>_−E_</sup> 6<sup>2doesnotvanishintheupperhalf-plain,hence</sup><sup>_ϕ−_2and</sup><sup>_ϕ−_4</sup> have no poles in H. Analogously to (20), the Fourier coefficients of _ϕ−_ 2 and _ϕ−_ 4 satisfy 



We define 







The function _φ_ 0( _z_ ) is not modular; however the identity (12) implies the following transformation rule: 



Moreover, we have 





where _Df_ ( _z_ ) = 21 _πi dzd_<sup>_f_(</sup><sup>_z_).These identities combined with (20) and (25) give the asymp-</sup> totic formula for the Fourier coefficients _cφ−_ 4( _n_ ), _cφ−_ 2( _n_ ), and _cφ_ 0( _n_ ). The first several terms of the corresponding Fourier expansions are 





where _q_ = _e_<sup>2</sup><sup>_πiz_</sup> . For _x ∈_ R<sup>8</sup> we define 



9 

We observe that the contour integrals in (35) converge absolutely and uniformly for _x ∈_ R<sup>8</sup> . Indeed, _φ_ 0( _z_ ) = _O_ ( _e_<sup>_−_2</sup><sup>_πiz_</sup> ) as Im ( _z_ ) _→∞_ . Therefore, _a_ ( _x_ ) is well defined. Now we prove that _a_ satisfies condition (21). 

**Proposition 1.** _The function a defined by_ (35) _belongs to the Schwartz space and satisfies_ 



_Proof._ First, we prove that _a_ is a Schwartz function. From (20), (25), and (31) we deduce that the Fourier coefficients of _φ_ 0 satisfy 



Thus, there exists a positive constant _C_ such that 



We estimate the first summand in the right-hand side of (35). For _r ∈_ R _≥_ 0 we have 



where _C_ 1 and _C_ 2 are some positive constants and _Kα_ ( _x_ ) is the modified Bessel function of the second kind defined as in [1, Section 9.6]. This estimate also holds for the second and third summand in (35). For the last summand we have 



Therefore, we arrive at 



It is easy to see that the left hand side of this inequality decays faster then any inverse _<u>d</u>_<sup>_k_</sup> power of _r_ . Analogous estimates can be obtained for all derivatives _dr_<sup>_ka_(</sup><sup>_r_).</sup> 

Now we show that _a_ is an eigenfunction of the Fourier transform. We recall that the Fourier transform of a Gaussian function is 



10 

Next, we exchange the contour integration with respect to _z_ variable and Fourier transform with respect to _x_ variable in (35). This can be done, since the corresponding double integral converges absolutely. In this way we obtain 



Now we make a change of variables _w_ =<sup>_−_</sup> _z_<sup><u>1</u>.Weobtain</sup> 



Since _φ_ 0 is 1-periodic we have 



This finishes the proof of the proposition. 

Next, we check that _a_ has double zeroes at all Λ8-lattice points of length greater then _√_ 2. 

**Proposition 2.** _For r > √_ 2 _we can express a_ ( _r_ ) _in the following form_ 



11 

_Proof._ We denote the right hand side of (37) by _d_ ( _r_ ). It is easy to see that _d_ ( _r_ ) is welldefined. Indeed, from the transformation formula (29) and the expansions (34)–(32) we obtain 



Hence, the integral (37) converges absolutely for _r > √_ 2. We can write 



From (29) we deduce that if _r > √_ 2 then _φ_ 0 _−z_ <u>1</u> _z_<sup>2</sup> _e_<sup>_πir_2</sup><sup>_z_</sup> _→_ 0 as Im ( _z_ ) _→∞_ . There� � fore, we can deform the paths of integration and rewrite 



Now from (29) we find 



12 

Thus, we obtain 



This finishes the proof. 

Finally, we find another convenient integral representation for _a_ and compute values of _a_ ( _r_ ) at _r_ = 0 and _r_ = _√_ 2. 

**Proposition 3.** _For r ≥_ 0 _we have_ 



_The integral converges absolutely for all r ∈_ R _≥_ 0 _. Proof._ Suppose that _r > √_ 2. Then by Proposition 2 



From (34)–(29) we obtain 

For _r > √_ 2 we have 



Therefore, the identity (38) holds for _r > √_ 2. 

On the other hand, from the definition (35) we see that _a_ ( _r_ ) is analytic in some neighborhood of [0 _, ∞_ ). The asymptotic expansion (39) implies that the right hand side of (38) is also analytic in some neighborhood of [0 _, ∞_ ). Hence, the identity (38) holds on the whole interval [0 _, ∞_ ). This finishes the proof of the proposition. 

13 

From the identity (38) we see that the values _a_ ( _r_ ) are in _i_ R for all _r ∈_ R _≥_ 0. In particular, we have 

**Proposition 4.** _We have_ 



_Proof._ These identities follow immediately from the previous proposition. 

Now we construct function _b_ . To this end we consider the modular form 



It is easy to see that _h ∈ M−_<sup>!</sup> 2<sup>(Γ0(2)).Indeed,firstwecheckthat</sup><sup>_h|−_2</sup><sup>_γ_=</sup><sup>_h_forall</sup> _γ ∈_ Γ0(2). Since the group Γ0(2) is generated by elements (<sup>1</sup> 2<sup>0</sup> 1<sup>)and( 1</sup> 0<sup>1</sup> 1<sup>)itsufficesto</sup> check that _h_ is invariant under their action. This follows immediately from (13)–(18) and (42). Next we analyze the poles of _h_ . It is known [14, Chapter I Lemma 4.1] that _θ_ 10 has no zeros in the upper-half plane and hence _h_ has poles only at the cusps. At the cusp _i∞_ this modular form has the Fourier expansion 



Let _I_ = (<sup>1</sup> 0<sup>0</sup> 1<sup>),</sup><sup>_T_= ( 1</sup> 0 1<sup>1),and</sup><sup>_S_=</sup> � 10 _−_ 01 � be elements of Γ(1). We define the following three functions 





More explicitly, we have 



The Fourier expansions of these functions are 

_ψI_ ( _z_ ) = _q_<sup>_−_1</sup> + 144 _−_ 5120 _q_<sup>1</sup><sup>_/_2</sup> + 70524 _q −_ 626688 _q_<sup>3</sup><sup>_/_2</sup> + 4265600 _q_<sup>2</sup> + _O_ ( _q_<sup>5</sup><sup>_/_2</sup> ) _,_ (49) _ψT_ ( _z_ ) = _q_<sup>_−_1</sup> + 144 + 5120 _q_<sup>1</sup><sup>_/_2</sup> + 70524 _q_ + 626688 _q_<sup>3</sup><sup>_/_2</sup> + 4265600 _q_<sup>2</sup> + _O_ ( _q_<sup>5</sup><sup>_/_2</sup> ) _,_ (50) _ψS_ ( _z_ ) = _−_ 10240 _q_<sup>1</sup><sup>_/_2</sup> _−_ 1253376 _q_<sup>3</sup><sup>_/_2</sup> _−_ 48328704 _q_<sup>5</sup><sup>_/_2</sup> _−_ 1059078144 _q_<sup>7</sup><sup>_/_2</sup> + _O_ ( _q_<sup>9</sup><sup>_/_2</sup> ) _._ (51) 

14 

For _x ∈_ R<sup>8</sup> define 



Now we prove that _b_ satisfies condition (22). 

**Proposition 5.** _The function b defined by_ (52) _belongs to the Schwartz space and satisfies_ 



_Proof._ Here, we repeat the arguments used in the proof of Proposition 1. First we show that _b_ is a Schwartz function. We have 



There exists a positive constant _C_ such that 



Thus, as in the proof of Proposition 1 we estimate the first summand in the left-hand side of (52) 



We combine this inequality with analogous estimates for the other three summands and obtain 



Here _C_ 1, _C_ 2, and _C_ 3 are some positive constants. Similar estimates hold for all deriva- _<u>d</u>_<sup>_k_</sup> tives _d_<sup>_k_</sup> _r_<sup>_b_(</sup><sup>_r_).</sup> 

15 

Now we prove that _b_ is an eigenfunction of the Fourier transform. We use identity (36) and interchange contour integration in _z_ and Fourier transform in _x_ . Thus we obtain 



We make the change of variables _w_ =<sup>_−_</sup> _z_<sup><u>1</u>andarriveat</sup> 



Now we observe that the definitions (43)–(45) imply 



Therefore, we arrive at 



Now from (52) we see that 



Now we regard the radial function _b_ as a function on R _≥_ 0. We check that _b_ has double roots at Λ8-points. 

**Proposition 6.** _For r > √_ 2 _function b_ ( _r_ ) _can be expressed as_ 



16 

_Proof._ We denote the right hand side of (53) by _c_ ( _r_ ). First, we check that _c_ ( _r_ ) is well-defined. We have 



Therefore, the integral (53) converges for _r > √_ 2. Then we rewrite it in the following way: 



From the Fourier expansion (49) we know that _ψI_ ( _z_ ) = _e_<sup>_−_2</sup><sup>_πiz_</sup> + _O_ (1) as Im ( _z_ ) _→∞_ . By assumption _r_<sup>2</sup> _>_ 2, hence we can deform the path of integration and write 



We have 



Next, we check that the functions _ψI , ψT_ , and _ψS_ satisfy the following identity: 



Indeed, from definitions (43)-(45) we get 



Note that _ST_<sup>2</sup> _S_ belongs to Γ0(2). Thus, since _h ∈ M−_<sup>!</sup> 2<sup>Γ0(2)weget</sup> 



Now we observe that _T_ and _STS_ ( _ST_ )<sup>_−_1</sup> are also in Γ0(2). Therefore, 



17 

Combining (56) and (57) we find 



At the end of this section we find another integral representation of _b_ ( _r_ ) for _r ∈_ R _≥_ 0 and compute special values of _b_ . 

**Proposition 7.** _For r ≥_ 0 _we have_ 



_The integral converges absolutely for all r ∈_ R _≥_ 0 _._ 

_Proof._ The proof is analogous to the proof of Proposition 3. First, suppose that _r > √_ 2. Then by Proposition 6 



From (49) we obtain 



For _r > √_ 2 we have 



Therefore, the identity (38) holds for _r > √_ 2. On the other hand, from the definition (52) we see that _b_ ( _r_ ) is analytic in some neighborhood of [0 _, ∞_ ). The asymptotic expansion (59) implies that the right hand side of (58) is also analytic in some neighborhood of [0 _, ∞_ ). Hence, the identity (58) holds on the whole interval [0 _, ∞_ ). This finishes the proof of the proposition. 

We see from (58) that _b_ ( _r_ ) _∈ i_ R far all _r ∈_ R _≥_ 0. Another immediate corollary of this proposition is 

**Proposition 8.** _We have_ 



18 

## **5 Proof of Theorem 3** 

Finally, we are ready to prove Theorem 3. 

**Theorem 4.** _The function_ 



_satisfies conditions_ (3) _–_ (5) _. Moreover, the values g_ ( _x_ ) _and g_ �( _x_ ) _do not vanish for all vectors x with ∥x∥_<sup>2</sup> _∈/_ 2Z _>_ 0 _._ 



_Proof._ First, we prove that (3) holds. By Propositions 2 and 6 we know that for _r >_ 

where 



Our goal is to show that _A_ ( _t_ ) _<_ 0 for _t ∈_ (0 _, ∞_ ) _._ The function _A_ ( _t_ ) is plotted in Figure 1. 



We observe that we can compute the values of _A_ ( _t_ ) for _t ∈_ (0 _, ∞_ ) with any given precision. Indeed, from identities (29) and (45) we obtain the following two presentations for _A_ ( _t_ ) 



19 

For an integer _n ≥_ 0 let _A_<sup>(</sup> 0<sup>_n_)</sup> and _A_<sup>(</sup> _∞_<sup>_n_)bethefunctionssuchthat</sup> 





For each _n ≥_ 0 we can compute these functions from the Fourier expansions (34)–(32), (49), and (51). For example, from (32)–(34) and (49) we compute 



From (32)–(34) and (51) we compute 



Moreover, from the convergent asymptotic expansion for the Fourier coefficients of a weakly holomorphic modular form [3, Proposition 1.12] we find that the _n_ -th Fourier coefficient _cψI_ ( _n_ ) of _ψI_ satisfies 



Similar inequalities hold for the Fourier coefficients of _ψS_ , _φ_ 0, _φ−_ 2, and _φ−_ 4: 









Therefore, we can estimate the error terms in the asymptotic expansions (63) and (64) of _A_ ( _t_ ) 



For an integer _m ≥_ 0 we set 



20 

Using interval arithmetic we check that 



Thus, we see that _A_ ( _t_ ) _<_ 0 for _t ∈_ (0 _, ∞_ ). Then identity (62) implies (3). Next, we prove (4). By Propositions 3 and 7 we know that for _r >_ 0 



where 



This function can also be written as 



Our aim is to prove that _B_ ( _t_ ) _>_ 0 for _t ∈_ (0 _, ∞_ ). A plot of _B_ ( _t_ ) is given in Figure 2. 





21 

We find 



and 



The estimates (65)–(69) imply that 

and 



Using interval arithmetic we verify that 



Now identity (70) implies (4). 

Finally, the property (5) readily follows from Proposition 4 and Proposition 8. This finishes the proof of Theorems 4 and 3. 

## **Acknowledgments** 

I thank Andriy Bondarenko for sharing his ideas, for fruitful discussions, and for his support. Also I am grateful to Danilo Radchenko for his valuable ideas and his help with numerical computations. I am most grateful to J. Kramer, J. M. Sullivan, G. M. Ziegler , and anonymous referees for their valuable comments and suggestions on the manuscript. 

## **References** 

- [1] M. Abramowitz, I. Stegun, _Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables_ , Applied Mathematics Series 55 (10th ed.), New York, USA: United States Department of Commerce, National Bureau of Standards; Dover Publications, 1964. 

- [2] A. Bondarenko, D. Radchenko, M. Viazovska, _On optimal asymptotic bounds for spherical designs_ , Annals of Math. 178 (2)(2013), pp. 443–452. 

22 

- [3] J. Bruinier, _Borcherds products on O(2,l) and Chern classes of Heegner divisors_ , Springer Lecture Notes in Mathematics 1780 (2002). 

- [4] H. Cohn, N. Elkies, _New upper bounds on sphere packings I_ , Annals of Math. 157 (2003) pp. 689–714. 

- [5] H. Cohn, A. Kumar, _Universally optimal distribution of points on spheres_ , J. Amer. Math. Soc. 20 (1) (2007), pp. 99–148. 

- [6] J. H. Conway and N. J. A. Sloane, _What Are All the Best Sphere Packings in Low Dimensions?_ , Discrete Comput. Geom. (L´aszl´o Fejes T´oth Festschrift), 13 (1995), pp. 383–403. 

- [7] P. Delsarte, _Bounds for unrestricted codes, by linear programming_ , Philips Res. Rep. 27 (1972), pp. 272–289. 

- [8] P. Delsarte, J. M. Goethals, and J. J. Seidel, _Spherical codes and designs_ , Geom. Dedicata, 6 (1977), pp. 363–388. 

- [9] F. Diamond, J. Shurman, _A First Course in Modular Forms_ , Springer New York, 2005. 

- [10] L. Fejes T´oth, _Uber_<sup>_¨_</sup> _die dichteste Kugellagerung_ , Math. Z. 48 (1943), pp. 676– 684. 

- [11] T. Hales, _A proof of the Kepler conjecture_ , Annals of Math. 162 (3) (2005), pp. 1065–1185. 

- [12] D. Hejhal, _The Selberg trace formula for_ PSL(2 _,_ R), Vol. 2, Springer Lecture Notes in Mathematics 1001 (1983). 

- [13] G. A. Kabatiansky and V. I. Levenshtein, _Bounds for packings on a sphere and in space_ , Problems of Information Transmission 14 (1978), pp. 1–17. 

- [14] D. Mumford, _Tata Lectures on Theta I_ , Birkh¨auser, 1983. 

- [15] H. Petersson, _Ueber die Entwicklungskoeffizienten der automorphen Formen_ , Acta Mathematica, Bd. 58 (1932), pp. 169–215. 

- [16] F. Pfender, G. M. Ziegler, _Kissing numbers, sphere packings, and some unexpected proofs_ , Notices of the AMS 51 (8) (2004) pp. 873–883. 

- [17] H. Rademacher and H. S. Zuckerman, _On the Fourier coefficients of certain modular forms of positive dimension_ , Annals of Math. (2) 39 (1938), pp. 433–462. 

- [18] A. Thue, _Uber_<sup>_¨_</sup> _die dichteste Zusammenstellung von kongruenten Kreisen in einer Ebene_ , Norske Vid. Selsk. Skr. No.1 (1910), pp. 1–9. 

- [19] V. A. Yudin, _Lower bounds for spherical designs_ , Izv. Ross. Akad. Nauk Ser. Mat. 61 (1997), pp. 211–233. English transl., Izv. Math. 6 (1997), pp. 673–683. 

23 

- [20] D. Zagier, _Elliptic Modular Forms and Their Applications_ , In: The 1-2-3 of Modular Forms, (K. Ranestad, ed.) Norway, Springer Universitext, 2008. 

Berlin Mathematical School Str. des 17. Juni 136 10623 Berlin and Humboldt University of Berlin Rudower Chaussee 25 12489 Berlin _Email address: viazovska@gmail.com_ 

24 

