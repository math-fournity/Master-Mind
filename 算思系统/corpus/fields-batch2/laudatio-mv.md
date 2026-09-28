# **The work of Maryna Viazovska** 

## **Henry Cohn** 

### **Abstract** 

On July 5th, 2022, Maryna Viazovska was awarded a Fields Medal for her solution of the sphere packing problem in eight dimensions, as well as further contributions to related extremal problems and interpolation problems in Fourier analysis. This article explains some of the ideas behind her work to a broad mathematical audience. 

### **Mathematics Subject Classification 2020** 

Primary 52C17; Secondary 11F03, 11H31 

### **Keywords** 

Sphere packing, modular forms 

> © 2022 International Mathematical Union Preliminary version, to appear in Proc. Int. Cong. Math. 2022, Vol. 1. DOI 10.4171/ICM2022/213 



**Figure 1** 

An optimal packing of cannonballs. 

### **1. Introduction** 

The sphere packing problem asks how we can fill as large a fraction of space as possible with congruent balls, if they are not allowed to overlap except tangentially.1 This problem sits at the interface between many branches of mathematics, and of science more generally, with connections ranging from materials science to information theory. Sphere packing is a natural problem in Euclidean geometry, with a simple statement, and one might expect an equally elementary and self-contained solution. Instead, the topic is dominated by unexpected connections. 

Before Viazovska’s breakthrough work, the optimal sphere packing density was known only in one, two, and three dimensions. One dimension is trivial, because intervals can tile the real line with density 1. Two dimensions is not trivial, but Thue **[26]** showed that arranging six neighbors around each disk is optimal, with density _𝜋_ /√12 = 0 _._ 9068 _. . ._ . Three dimensions was solved by Hales **[16]** via an ingenious and elaborate computer-assisted proof, which has since been formally verified **[17]** . The unsurprising answer is shown in Figure 1: optimal two-dimensional layers are nestled together as densely as possible, to achieve density _𝜋_ / ~~√~~ 18 = 0 _._ 7404 _. . ._ . 

These prior results paint a misleading picture of what happens in higher dimensions. Stacking optimal layers from the previous dimension generally produces suboptimal packings, and nobody has any idea what the densest sphere packings might be in most dimensions. We do not even know whether they should be crystalline or disordered. 

> **1** To state the problem precisely, “as large a fraction as possible” must be made precise. One way to do so is by taking a limit of the packing problem in a bounded region as its size grows relative to the sphere radius. The sphere packing problem turns out to be very robust, in the sense that just about all reasonable formulations are equivalent. 

**2 H. Cohn** 

High-dimensional packings are not merely of pure mathematical interest, but also important for practical applications, because sphere packings are error-correcting codes for a continuous communication channel (such as radio). In this model, the packing is in an abstract signal space, whose dimension is the number of measurements used to characterize the signal and is generally much larger than three. 

There does not seem to be any simple pattern in the optimal packings that persists across many dimensions, and the best upper and lower bounds known for the packing density in R<sup>_𝑑_</sup> remain exponentially far apart as _𝑑_ grows. However, a handful of dimensions stand out as special, most notably eight and twenty-four dimensions. These dimensions feature exceptional packings, namely the _𝐸_ 8 root lattice and the Leech lattice Λ24, with remarkable symmetries and numerous connections to different branches of mathematics. Thanks to Viazovska’s work **[10, 27]** , we now know that they are truly optimal. The jump from three dimensions to eight and twenty-four in the known solutions is remarkable, and it illustrates the exceptional nature of these packings. 

The _𝐸_ 8 and Leech lattices had long been viewed as the most compelling candidates for further solutions of the sphere packing problem. However, a direct geometric proof seems infeasible: it is natural to try to work with a decomposition of space into cells, but the curse of dimensionality means we are faced with an unmanageable number of potential cell shapes and ways they could adjoin each other. Perhaps there exists a proof along these lines, but nobody has found a workable approach. 

Instead, Viazovska proved the optimality of _𝐸_ 8 via a dramatic new connection to the theory of modular forms, following which she and several collaborators extended her ideas to the case of the Leech lattice: 

**Theorem 1.1** (Viazovska **[27]** ). _The 𝐸_ 8 _root lattice achieves the optimal sphere packing density in_ R<sup>8</sup> _, namely 𝜋_<sup>4</sup> /384 _._ 

**Theorem 1.2** (Cohn, Kumar, Miller, Radchenko, and Viazovska **[10]** ). _The Leech lattice_ Λ24 _achieves the optimal sphere packing density in_ R<sup>24</sup> _, namely 𝜋_<sup>12</sup> /12! _._ 

As Peter Sarnak said at the time **[19]** , her paper **[27]** is “stunningly simple, as all great things are.” This simplicity is characteristic of Viazovska’s work: she has a gift for linking concepts and posing bold conjectures, and these insights lead her to striking arguments. Her proofs engage directly with the heart of the matter, without any extraneous complications. Of course, simple is very much not the same thing as easy. What makes her work extraordinary is how different her ideas are from what came before. 

In the remainder of this article, we will examine Viazovska’s proof of the optimality of _𝐸_ 8, as well as its motivation and place in mathematics more broadly. In particular, this article can serve as an introduction and guide to Viazovska’s techniques, alongside other expositions **[6, 20]** . For background on sphere packing and lattices, see **[12, 15, 25]** . 

Of course we should keep in mind that this topic represents only one strand of Viazovska’s research. For example, **[3]** is a beautiful and decisive paper on a quite different topic. What will she be known for in twenty or thirty years? I look forward to finding out. 

**3 The work of Maryna Viazovska** 

### **2. The past** 

Before we turn to Viazovska’s proof, we will need some background. In this section, we will construct the _𝐸_ 8 lattice and explain a method for proving upper bounds for the sphere packing density. 

Sphere packings can be constructed in many ways, among which lattice packings are the simplest possibility. A _lattice packing_ of spheres centers the spheres at the points of a _lattice_ Λ in R<sup>_𝑑_</sup> , i.e., a discrete subgroup of R<sup>_𝑑_</sup> of rank _𝑑_ , or equivalently the integral span of a basis of R<sup>_𝑑_</sup> . There is no reason why an optimal sphere packing should have this algebraic structure, and for example the best sphere packing known in R<sup>10</sup> does not. However, many of the best sphere packings known in low dimensions are lattice packings. 

To form a packing from a lattice Λ, we must choose the sphere radius _𝑟_ so that neighboring spheres do not overlap. Specifically, we should take 



The volume of a sphere of radius _𝑟_ in R<sup>_𝑑_</sup> is _𝜋_<sup>_𝑑_/2</sup> _𝑟_<sup>_𝑛_</sup> /( _𝑑_ /2)!, where ( _𝑑_ /2)! means Γ( _𝑑_ /2 + 1) when _𝑑_ is odd, and the _density_ of the overall packing (i.e., the fraction of space covered by the balls) is the sphere volume times the number of spheres per unit volume in space. Let vol<sup>�</sup> R<sup>_𝑑_</sup> /Λ<sup>�</sup> denote the _covolume_ of the lattice, i.e., the volume of the quotient torus, or equivalently the absolute value of the determinant of a lattice basis. Then the number of spheres per unit volume in space is 1/vol<sup>�</sup> R<sup>_𝑑_</sup> /Λ<sup>�</sup> , and so the lattice packing density is 



One of the most remarkable lattices is the _𝐸_ 8 _root lattice_ , which originated in Lie theory but has since become widespread across mathematics. We will see below how to obtain _𝐸_ 8 as a modification of the _𝐷 𝑑_ lattice, the checkerboard lattice in _𝑑_ dimensions, which is defined by 



In other words, _𝐷 𝑑_ simply omits every other point in the cubic lattice Z<sup>_𝑑_</sup> . As a special case, _𝐷_ 3 is the face-centered cubic lattice in three dimensions, which Hales showed achieves the optimal sphere packing density **[16]** , and _𝐷_ 4 and _𝐷_ 5 are the best packings known in their dimensions. However, _𝐷 𝑑_ is not optimal beyond five dimensions. 

The problem with _𝐷 𝑑_ in higher dimensions is that its holes are too large. A _hole_ is a point in space that is a local maximum for distance from the lattice. There are two types of holes in _𝐷 𝑑_ , shallow holes at distance 1 from the lattice, such as (1 _,_ 0 _, . . . ,_ 0), and deep holes at distance ~~√~~ _𝑑_ /4 from the lattice, such as ( 2<sup><u>1</u></sup><sup>_,_</sup><sup><u>1</u></sup> 2<sup>_, . . . ,_</sup><sup><u>1</u></sup> 2<sup>).As</sup><sup>_𝑑_→∞,sodoes</sup> √︁ _𝑑_ /4, and so the deep holes become large enough to fit enormous numbers of additional spheres. In particular, _𝐷 𝑑_ cannot be optimal when _𝑑_ is large. 

When _𝑑_ = 8, something beautiful happens. The distance √︁8/4 from a deep hole to the lattice exactly equals the distance √2 between lattice points in _𝐷_ 8, and that means the deep holes are just large enough to be filled with additional spheres. If we plug these holes with spheres, then the resulting packing is the union of _𝐷_ 8 with its translate _𝐷_ 8 + (<sup><u>1</u></sup> 2<sup>_,_</sup><sup><u>1</u></sup> 2<sup>_, . . . ,_</sup><sup><u>1</u></sup> 2<sup>). It</sup> 

**4 H. Cohn** 



**Figure 2** 

A two-dimensional cross section of R<sup>8</sup> through a Coxeter plane of _𝐸_ 8, colored according to the squared distance to the nearest point in _𝐸_ 8 (dark is close) and inspired by **[22]** . 

is not hard to check that this packing is a lattice (it amounts to the fact that 2 · (<sup><u>1</u></sup> 2<sup>_,_</sup><sup><u>1</u></sup> 2<sup>_, . . . ,_</sup><sup><u>1</u></sup> 2<sup>) ∈</sup> _𝐷_ 8), which is called the _𝐸_ 8 _root lattice_ . 

The _𝐸_ 8 lattice packing has packing radius _𝑟_ = √2/2 and covolume vol<sup>�</sup> R<sup>8</sup> / _𝐸_ 8� = vol<sup>�</sup> R<sup>8</sup> / _𝐷_ 8�/2 = 1, and so it has a packing density of _𝜋_ 4/384 = 0 _._ 2536 _. . ._ . It is by no means obvious that this construction is optimal. In fact, the construction feels a little ad hoc. However, the _𝐸_ 8 lattice turns out to be far more beautiful and symmetric than its construction indicates. For example, see Figure 2 for a view of _𝐸_ 8 with 30-fold symmetry. This is a common pattern with exceptional structures in mathematics: they are typically obtained by piecing together several substructures that each have less symmetry individually. 

Now that we have the _𝐸_ 8 lattice, the next question is how we could try to obtain a matching upper bound for the sphere packing density in eight dimensions. Obtaining a matching bound seems completely infeasible in most dimensions, but in a few special dimensions bounds based on harmonic analysis work remarkably well. This idea, called the _linear programming bound_ , goes back to a fundamental paper by Delsarte **[13]** on error-correcting codes, and the corresponding bound for sphere packings was developed by Cohn and Elkies **[7]** . 

**5 The work of Maryna Viazovska** 

The linear programming bound is formulated in terms of the _Fourier transform_<sup>�</sup> _𝑓_ of an integrable function _𝑓_ : R<sup>_𝑑_</sup> → C, which we will normalize as 



where ⟨· _,_ ·⟩ is the usual inner product on R<sup>_𝑑_</sup> . Recall that the Fourier transform decomposes _𝑓_ into complex exponentials; in signal processing terms, it amounts to identifying the frequencies that occur in a signal and their relative magnitudes. This decomposition amounts to the _Fourier inversion theorem_ : if<sup>�</sup> _𝑓_ is integrable as well, then 



In other words, the Fourier transform is very nearly its own inverse, with a single sign change being the only difference. Note that<sup>�</sup> _𝑓_ is generally complex-valued, even if _𝑓_ is real-valued, but<sup>�</sup> _𝑓_ is real-valued if _𝑓_ is real-valued and an even function. 

We will also need a few types of well-behaved functions. A function _𝑓_ : R<sup>_𝑑_</sup> → R is called _rapidly decreasing_ if _𝑓_ ( _𝑥_ ) = _𝑂_<sup>�</sup> | _𝑥_ |<sup>−</sup><sup>_𝑐_�</sup> as | _𝑥_ | →∞ for every constant _𝑐>_ 0, and a _Schwartz function_ is a smooth function such that it and all its iterated partial derivatives (of every order) are rapidly decreasing. Schwartz functions are arguably the best-behaved functions in harmonic analysis. Much of what we will discuss can be generalized somewhat beyond Schwartz functions, but they are all Viazovska needed to solve the sphere packing problem. 

We can now state the linear programming bound for sphere packing: 

**Theorem 2.1** (Cohn and Elkies **[7]** ). _Let 𝑓_ : R<sup>_𝑑_</sup> → R _be an even Schwartz function and 𝑟 a positive real number. If_ 

- (1) _𝑓_ ( _𝑥_ ) ≤ 0 _for all 𝑥_ ∈ R<sup>_𝑑_</sup> _satisfying_ | _𝑥_ | ≥ _𝑟,_ 

- (2)<sup>�</sup> _𝑓_ ( _𝑦_ ) ≥ 0 _for all 𝑦_ ∈ R<sup>_𝑑_</sup> _, and_ 



_then the optimal sphere packing density in_ R<sup>_𝑑_</sup> _is at most_ vol<sup>�</sup> _𝐵𝑟_<sup>_𝑑_</sup> /2� = _𝜋𝑑_ /2( _𝑟_ /2) _𝑑_ /( _𝑑_ /2)! _._ 

This theorem produces an upper bound for the packing density from a function _𝑓_ satisfying certain inequalities, but it says nothing about how to choose _𝑓_ to optimize the bound. Numerical optimization can produce good choices for _𝑓_ , which yield the bounds shown in Figure 3. These bounds are rigorous, but it is possible that other functions may produce even better bounds. 

As one can see in Figure 3, the bounds in eight and twenty-four dimensions appear sharp. Numerical optimization will not yield an exactly sharp bound, but it seems to come as close as desired. Based on data of this sort as well as analogies with other problems in coding theory, Cohn and Elkies conjectured the existence of _magic functions 𝑓_ that would solve the sphere packing problem exactly in R<sup>8</sup> and R<sup>24</sup> , by achieving _𝑟_ = √2 and _𝑟_ = 2, respectively. Note that this is not because the bound dips lower in these dimensions, but rather because the 

**6 H. Cohn** 



<!-- Start of picture text -->
1<br>10 −1<br>10 −2<br>10 −3<br>Linear programming bound<br>10 −4 Sphere packing density<br>10 −5<br>0 4 8 12 16 20 24 28 32<br>Dimension  𝑑<br>𝑑 Sphere packing density in R<br><!-- End of picture text -->

**Figure 3** 

A plot of the numerically computed linear programming bound **[1]** and the best sphere packing density currently known **[12]** . 

optimal packings rise up to meet it. No other dimensions greater than 2 seem to have a sharp linear programming bound, and it seems unlikely that others exist, but no proof is known, and the bound has been exactly optimized only for _𝑑_ = 1, 8, and 24. 

The heart of Viazovska’s breakthrough lies in the construction of the magic functions. What should _𝑓_ look like if we are to obtain a sharp bound? There are some simple criteria, which we can obtain from the proof of Theorem 2.1. In this article we will examine a proof for just the special case of lattices, but the theorem can be proved in full generality by combining the same technique with a little additional algebra. The argument is based on the _Poisson summation formula_ , which says that if _𝑓_ : R<sup>_𝑑_</sup> → C is a Schwartz function, Λ is a lattice in R<sup>_𝑑_</sup> , and Λ<sup>∗</sup> is its _dual lattice_ (i.e., the lattice generated by the dual basis of any basis of Λ with respect to the inner product ⟨· _,_ ·⟩), then 



_Proof of Theorem_ 2.1 _for lattice packings._ The sphere packing problem is scaling-invariant, and so we can use spheres of radius _𝑟_ /2. Let Λ be any lattice packing with packing radius _𝑟_ /2, which means | _𝑥_ | ≥ _𝑟_ for _𝑥_ ∈ Λ \ {0}. If _𝑓_ satisfies the hypotheses of Theorem 2.1, then 

**7 The work of Maryna Viazovska** 



<!-- Start of picture text -->
𝑓 � 𝑓<br>√2 √4 √6 √ 8 √2 √4 √6 √8<br><!-- End of picture text -->

**Figure 4** 

This schematic diagram, which is taken from **[6]** , shows the roots of the magic function _𝑓_ and its Fourier transform<sup>�</sup> _𝑓_ in eight dimensions. It is not a plot of the actual function, which decreases very rapidly. See Figure 5 for an actual plot. 

_𝑓_ ( _𝑥_ ) ≤ 0 for _𝑥_ ∈ Λ \ {0} and<sup>�</sup> _𝑓_ ( _𝑦_ ) ≥ 0 for all _𝑦_ , from which it follows that 



A first observation is that we can assume without loss of generality that _𝑓_ is radial, i.e., _𝑓_ ( _𝑥_ ) depends only on | _𝑥_ |. This reason is that we can replace _𝑓_ with the average of its rotations about the origin, because all the constraints are linear and rotation-invariant. One might wonder whether non-radial functions could be helpful conceptually even if they are not needed, but so far the answer appears to be no. Instead, Viazovska’s work turns out to lead to a wonderful new theory of interpolation for radial functions. We will henceforth assume _𝑓_ is radial, and when _𝑡_ ∈[0 _,_ ∞) we will write _𝑓_ ( _𝑡_ ) for the common value _𝑓_ ( _𝑥_ ) with | _𝑥_ | = _𝑡_ , as well as _𝑓_<sup>′</sup> ( _𝑡_ ) for the radial derivative. 

Now if we examine the central inequality in the proof of Theorem 2.1 for lattices, we can see when it could be sharp. To obtain a sharp bound, all of the discarded terms in the inequality must vanish: we must have _𝑓_ ( _𝑥_ ) = 0 for _𝑥_ ∈ Λ \ {0} and<sup>�</sup> _𝑓_ ( _𝑦_ ) = 0 for _𝑦_ ∈ Λ<sup>∗</sup> \ {0}. In other words, _𝑓_ must vanish on the nonzero distances between lattice points, and<sup>�</sup> _𝑓_ must vanish on the nonzero distances between dual lattice points. 

One can check directly from the construction of _𝐸_ 8 given above that _𝐸_ 8<sup>∗=</sup><sup>_𝐸_8and</sup> that the vector lengths in _𝐸_ 8 are all square roots of even integers. Furthermore, it turns out that each distance √2 _𝑛_ with _𝑛_ ≥ 0 actually occurs in _𝐸_ 8. We should therefore have _𝑟_ = ~~√~~ 2 in Theorem 2.1, and the magic function _𝑓_ should have a sign change at radius √2, followed by double roots at ~~√~~ 2 _𝑛_ for _𝑛_ ≥ 2, as indicated in Figure 4. In other words, we wish to control the behavior of _𝑓_ and<sup>�</sup> _𝑓_ to second order at these points, i.e., control both the values _𝑓_<sup>�√</sup> 2 _𝑛_<sup>�</sup> and<sup>�</sup> _𝑓_<sup>�√</sup> 2 _𝑛_<sup>�</sup> and the radial derivatives _𝑓_<sup>′�</sup><sup>~~√~~</sup> 2 _𝑛_<sup>�</sup> and<sup>�</sup> _𝑓_<sup>′�</sup><sup>~~√~~</sup> 2 _𝑛_<sup>�</sup> . How can one construct such a function _𝑓_ ? The reason this task is difficult is that it involves controlling both _𝑓_ and<sup>�</sup> _𝑓_ simultaneously. Either one is of course easy on its 

**8 H. Cohn** 







<!-- Start of picture text -->
𝑥 ↦→ 𝑓 ( 𝑥 ) 𝑥 ↦→ 𝑒 2 𝜋 | 𝑥 | | 𝑥 | 7/2 𝑓 ( 𝑥 )/300<br><!-- End of picture text -->

#### **Figure 5** 

Two plots of Viazovska’s magic function in eight dimensions. The first plot is scaled correctly, but it decreases so rapidly that the roots become invisible. The second plot introduces a rescaling to make them visible, based on the asymptotic decay rate. 

own, but handling both at once introduces profound difficulties. The underlying issue here is Heisenberg’s uncertainty principle: in loose terms, whenever you try to pin down _𝑓_ , you lose control over<sup>�</sup> _𝑓_ , and vice versa. More precisely, we run into Bourgain, Clozel, and Kahane’s uncertainty principle for controlling the signs of functions **[4, 8]** . These seemingly simple inequalities on _𝑓_ and<sup>�</sup> _𝑓_ therefore turn out to be far more subtle than they initially appear. 

When Elkies and I proposed this method in 1999, Viazovska was still in secondary school. Without realizing how profoundly difficult the remaining step was, I imagined that we had almost solved the sphere packing problem in eight and twenty-four dimensions, and our inability to find the magic functions was extremely frustrating. At first, I worried that someone else would find an easy solution and leave me feeling foolish for not doing it myself. Over time I became convinced that obtaining these functions was in fact difficult, and others also reached the same conclusion. For example, Thomas Hales has said that “I felt that it would take a Ramanujan to find it” **[19]** . Eventually, instead of worrying that someone else would solve it, I began to fear that nobody would solve it, and that I would someday die without knowing the outcome. I am grateful that Viazovska found such a satisfying and beautiful solution, and that she introduced wonderful new ideas for the mathematical community to explore. 

### **3. Modular forms** 

Viazovska’s magic function is constructed using modular forms, certain special functions that play an important role in number theory. The theory of modular forms has a reputation for being somewhat forbidding, but the basics are not so difficult, and that is all that is needed for Viazovska’s proof. We will outline the needed theory here. For a down to earth introduction to the case of SL2 (Z), see Chapter VII in **[24]** , and for more detailed and general treatments, see **[5, 14, 28]** . 

**9 The work of Maryna Viazovska** 

We begin with an example of a modular form, namely Eisenstein series. Recall that the Riemann zeta function is defined by 



when this sum converges, i.e., when Re( _𝑠_ ) _>_ 1. Here we are summing inverse powers of the arithmetic progression 1 _,_ 2 _, . . ._ , and Euler obtained an exact formula when _𝑠_ is an even integer. What if we instead wanted to sum inverse powers of a lattice in the complex plane? Setting aside the question of why we would want to do this (the result has deeper significance than one might guess), we could write the result as the _Eisenstein series_ 



for Im _𝑧>_ 0, where we are summing over the lattice { _𝑚𝑧_ + _𝑛_ : _𝑚, 𝑛_ ∈ Z}, with the exception of the point (0 _,_ 0) at which the summand blows up. Up to scaling by a complex factor, all two-dimensional lattices are of this form. 

The factor of 1/(2 _𝜁_ ( _𝑘_ )) in the definition is merely a convenient normalizing factor, which plays no essential role in the study of _𝐸𝑘_ . Unfortunately, the notation _𝐸𝑘_ conflicts with our name for the _𝐸_ 8 root lattice, but that will not cause any ambiguity in practice. 

We will restrict our attention to positive integers _𝑘_ , so that ( _𝑚𝑧_ + _𝑛_ )<sup>_𝑘_</sup> is single-valued. The series (3.1) converges absolutely when _𝑘_ ≥ 3, but just conditionally when _𝑘_ = 2. For odd _𝑘_ , the ( _𝑚, 𝑛_ ) and (− _𝑚,_ − _𝑛_ ) terms cancel and we obtain _𝐸𝑘_ ( _𝑧_ ) = 0, and so only the even cases are interesting.2 Thus, we will focus on _𝐸𝑘_ for _𝑘_ even and at least 4. 

What does an Eisenstein series look like? Figure 6 is a plot of _𝐸_ 4, in which black is zero, white is infinity, and color indicates complex phase **[21]** , with the sharp transitions in color occurring at positive real values. The fractal structure visible in this plot can be explained using two functional equations: 



These symmetries follow from rearranging the defining series (3.1) when _𝑘>_ 2, and they are the central equations in the theory of modular forms. 

The mappings _𝑧_ ↦→ _𝑧_ + 1 and _𝑧_ ↦→−1/ _𝑧_ that occur in these functional equations generate a discrete group of linear fractional transforms of the _upper half-plane_ H = { _𝑧_ ∈ C : Im _𝑧>_ 0}. To put it into a broader context of matrix groups, we can let the matrix<sup>�</sup><sup>_𝑎𝑏_</sup> _𝑐𝑑_ � act on H via 



Then the matrices _𝑇_ =<sup>�1</sup> 0<sup>1</sup> 1 � and _𝑆_ = � 01 −01 � satisfy _𝑇_ · _𝑧_ = _𝑧_ + 1 and _𝑆_ · _𝑧_ = −1/ _𝑧_ , and they turn out to generate the group SL2 (Z). 

> **2** This parity phenomenon is essentially the same as in Euler’s formula for the zeta function at even integers, which can be viewed as computing<sup>�</sup> _𝑛_ ∈Z\{0}<sup>_𝑛_−</sup><sup>_𝑘_explicitly for all integers</sup> _𝑘>_ 1. 

**10 H. Cohn** 





**Figure 6** 

A plot of the Eisenstein series _𝐸_ 4 ( _𝑧_ ) for −1 ≤ Re _𝑧_ ≤ 1 and 0 _<_ Im _𝑧_ ≤ 1 (above) and the same plot overlaid with a tiling of H using fundamental domains for the action of SL2 (Z) (below). 

The _weight 𝑘 action_ of SL2(Z) on functions _𝑓_ : H → C is defined by 



for _𝛾_ =<sup>�</sup><sup>_𝑎𝑏_</sup> _𝑐𝑑_ �. In this notation, the functional equations _𝐸𝑘_ ( _𝑧_ + 1) = _𝐸𝑘_ ( _𝑧_ ) and _𝐸𝑘_ (−1/ _𝑧_ ) = _𝑧_<sup>_𝑘_</sup> _𝐸𝑘_ ( _𝑧_ ) imply that the Eisenstein series _𝐸𝑘_ satisfies _𝐸𝑘_ | _𝑘 𝛾_ = _𝐸𝑘_ for all _𝛾_ ∈ SL2(Z) when _𝑘>_ 2. 

A _modular form of weight 𝑘 for_ SL2 (Z) is a holomorphic function _𝑓_ : H → C such that _𝑓_ | _𝑘 𝛾_ = _𝑓_ for all _𝛾_ ∈ SL2 (Z) and one additional condition holds, called being holomorphic at infinity. To state this condition, note that taking _𝛾_ = _𝑇_ shows that _𝑓_ ( _𝑧_ + 1) = _𝑓_ ( _𝑧_ ), and thus we can expand _𝑓_ as a Fourier series 



**11 The work of Maryna Viazovska** 

We say _𝑓_ is _meromorphic at infinity_ if there are only finitely many nonzero coefficients _𝑎𝑛_ with _𝑛<_ 0, and _holomorphic at infinity_ if _𝑎𝑛_ = 0 for all _𝑛<_ 0. The name reflects the fact that this Fourier series governs the behavior of _𝑓_ ( _𝑧_ ) as Im _𝑧_ grows, because _𝑒_<sup>2</sup><sup>_𝜋𝑖𝑧_</sup> → 0 as Im _𝑧_ →∞. The Fourier series of a modular form is often known as its _𝑞-series_ , with _𝑞_ = _𝑒_<sup>2</sup><sup>_𝜋𝑖𝑧_</sup> . 

The normalization factor 1/(2 _𝜁_ ( _𝑘_ )) in (3.1) ensures that the _𝑞_ -series of _𝐸𝑘_ has rational coefficients, and even integral coefficients when _𝑘_ is small. For example, one can show that _𝐸_ 4( _𝑧_ ) = 1 + 240<sup>�</sup> _𝑛_ ≥1<sup>_𝜎_</sup> 3<sup>(</sup><sup>_𝑛_)</sup><sup>_𝑞𝑛_and</sup><sup>_𝐸_</sup> 6<sup>(</sup><sup>_𝑧_)= 1 −504 �</sup> _𝑛_ ≥1<sup>_𝜎_</sup> 5<sup>(</sup><sup>_𝑛_)</sup><sup>_𝑞𝑛_, where</sup><sup>_𝜎_</sup> _𝑘_<sup>(</sup><sup>_𝑛_)</sup> denotes the sum of the _𝑘_ -th powers of the divisors of _𝑛_ . 

The product of modular forms of weights _𝑘_ and _ℓ_ is a modular form of weight _𝑘_ + _ℓ_ , and modular forms therefore form a graded ring. For SL2 (Z), one can show that this ring is generated by _𝐸_ 4 and _𝐸_ 6. In other words, the vector space of modular forms of weight _𝑘_ for SL2( _𝑍_ ) is spanned by the modular forms _𝐸_ 4<sup>_𝑗𝐸_</sup> 6<sup>_ℓ_with 4</sup><sup>_𝑗_+ 6</sup><sup>_ℓ_=</sup><sup>_𝑘_.</sup> 

In addition to using Eisenstein series directly, Viazovska also uses the _modular discriminant_ Δ, which is given by 



Its key property is that it vanishes nowhere in the upper half plane, while it vanishes at infinity (in the sense that its _𝑞_ -series has no constant term). 

Turán said that special functions should instead be called useful functions, and modular forms are no exception to this principle. The reason we study modular forms is not that we have a special love for Eisenstein series, but rather that the functional equations _𝑓_ ( _𝑧_ + 1) = _𝑓_ ( _𝑧_ ) and _𝑓_ (−1/ _𝑧_ ) = _𝑧_<sup>_𝑘_</sup> _𝑓_ ( _𝑧_ ) arise far more often than one might expect. For example, the _𝐸_ 8 lattice has an important modular form associated with it, namely its _theta series_ 



where _𝑁𝑛_ = #{ _𝑥_ ∈ _𝐸_ 8 : | _𝑥_ |<sup>2</sup> = 2 _𝑛_ }. In other words, the theta series is a generating function that counts the number of vectors of each length in _𝐸_ 8. 

This theta series satisfies both functional equations: Θ _𝐸_ 8 ( _𝑧_ + 1) = Θ _𝐸_ 8 ( _𝑧_ ) follows from the definition of Θ _𝐸_ 8 as a Fourier series, while Θ _𝐸_ 8 (−1/ _𝑧_ ) = _𝑧_<sup>4</sup> Θ _𝐸_ 8 amounts to Poisson summation over _𝐸_ 8 for the complex Gaussian _𝑥_ ↦→ _𝑒_<sup>_𝜋𝑖𝑧_|</sup><sup>_𝑥_|2</sup> , which has eight-dimensional Fourier transform _𝑦_ ↦→ _𝑧_<sup>−4</sup> _𝑒_<sup>_𝜋𝑖_(−1/</sup><sup>_𝑧_) |</sup><sup>_𝑦_|2</sup> . These functional equations tell us that Θ _𝐸_ 8 is a modular form for SL2 (Z) of weight 4, and it must therefore be proportional to _𝐸_ 4. In fact, Θ _𝐸_ 8 = _𝐸_ 4, because _𝑁_ 0 = 1. Thus, we obtain the beautiful formula 240 _𝜎_ 3( _𝑛_ ) for the number of vectors in _𝐸_ 8 of squared norm 2 _𝑛_ . 

The theory of modular forms extends to other discrete groups, if one carefully defines what being holomorphic at infinity means.3 Viazovska’s proof makes use of one more group, 

> **3** If Γ is a subgroup of finite index in SL2 (Z), then the condition is that for each _𝛾_ ∈ SL2 (Z), _𝑓_ | _𝑘 𝛾_ should be holomorphic at infinity. Note that _𝑓_ | _𝑘 𝛾_ need not satisfy ( _𝑓_ | _𝑘 𝛾_ ) ( _𝑧_ + 1) = ( _𝑓_ | _𝑘 𝛾_ ) ( _𝑧_ ), but one can check that it always satisfies ( _𝑓_ | _𝑘 𝛾_ ) ( _𝑧_ + _𝑛_ ) = ( _𝑓_ | _𝑘 𝛾_ ) ( _𝑧_ ) for some positive integer _𝑛_ and thus has a Fourier expansion in _𝑒_<sup>2</sup><sup>_𝜋𝑖𝑧_/</sup><sup>_𝑛_</sup> = _𝑞_<sup>1/</sup><sup>_𝑛_</sup> . 

**12 H. Cohn** 

namely 



which has index 6 in SL2 (Z). If we let 

_𝑊_ = _𝑈_ |2 _𝑇_ , and _𝑉_ = _𝑈_ − _𝑊_ , then _𝑈_ , _𝑉_ , and _𝑊_ are modular forms of weight 2 for Γ(2) that satisfy _𝑈_ = _𝑉_ + _𝑊_ and 



These identities will play a key role in the construction of Viazovska’s magic function. It turns out that _𝑈_ and _𝑊_ generate the ring of modular forms for Γ(2), and therefore every modular form of weight 2 _𝑘_ for Γ(2) is a linear combination of _𝑈_<sup>_𝑘_</sup> , _𝑈_<sup>_𝑘_−1</sup> _𝑊_ , _𝑈_<sup>_𝑘_−2</sup> _𝑊_<sup>2</sup> , ..., _𝑊_<sup>_𝑘_</sup> . 

Because modular forms are so closely connected with lattices, it is natural to turn to modular forms when attempting to construct the magic functions. However, it is entirely unclear where we should even start, because modular forms are completely different sorts of objects from radial Schwartz functions. Figure 6 looks nothing whatsoever like Figures 4 or 5, and there is no familiar transformation that makes it look any more similar. 

### **4. Viazovska’s construction for single roots** 

The first step in Viazovska’s construction of the magic function _𝑓_ is to split _𝑓_ into eigenfunctions of the Fourier transform. Radial functions satisfy<sup>��</sup> _𝑓_ = _𝑓_ , and so we can write _𝑓_ as _𝑓_ = _𝑓_ + + _𝑓_ −, where _𝑓_ + := ( _𝑓_ +<sup>�</sup> _𝑓_ )/2 satisfies<sup>�</sup> _𝑓_ + = _𝑓_ + and _𝑓_ − := ( _𝑓_ −<sup>�</sup> _𝑓_ )/2 satisfies � _𝑓_ − = − _𝑓_ −. If _𝑓_ is the magic function in eight dimensions, then _𝑓_ and<sup>�</sup> _𝑓_ both have roots at √2 _𝑛_ for integers _𝑛_ ≥ 1, and therefore _𝑓_ + and _𝑓_ − do as well. Thus, we are looking for radial Fourier eigenfunctions with specified roots. Specifically, each of _𝑓_ ± should have a single root at √2 and double roots at √2 _𝑛_ for _𝑛_ ≥ 2. These roots turn out to provide enough information to determine _𝑓_ ± up to scaling, and they can then be combined to obtain _𝑓_ . 

Before we construct the actual magic function, it is worth examining a simpler variant as a warm-up exercise. Instead of trying to control the behavior of _𝑓_ to second order at ~~√~~ 2 _𝑛_ , we will instead control the behavior of a function _𝑔_ to first order at<sup>~~√~~</sup> _<u>𝑛</u>_ <u>. This construc-</u> tion has no known applications to sphere packing, but it is nevertheless of intrinsic interest in Fourier analysis. We will also focus on the −1 eigenfunction (i.e., the case � _𝑔_ = − _𝑔_ ) in the single-root case, for the sake of specificity. 

Viazovska found a remarkable integral transform that can construct such functions. We will write a radial function _𝑔_ : R<sup>8</sup> → C as a continuous linear combination of complex Gaussians _𝑥_ ↦→ _𝑒_<sup>_𝜋𝑖𝑧_|</sup><sup>_𝑥_|2</sup> with _𝑧_ ∈H via the contour integral 



**13 The work of Maryna Viazovska** 

where _𝜓_ is a holomorphic function on H and the contour is a semicircle centered at the origin. Under which conditions on _𝜓_ will _𝑔_ be a Fourier eigenfunction, and how can we control its values at<sup>√</sup> _<u>𝑛</u>_ <u>?</u> 

We can obtain the values _𝑔_<sup>�√</sup> _<u>𝑛</u>_<sup>�</sup> by imposing periodicity on _𝜓_ as follows. Suppose _𝜓_ ( _𝑧_ + 2) = _𝜓_ ( _𝑧_ ) for all _𝑧_ ∈H , so that _𝜓_ has a Fourier series of the form 



Then for integers _𝑛_ ≥ 0, 



by orthogonality, provided that we can interchange the sum and integral. If the Fourier expansion (4.2) has only finitely many negative terms, then _𝑔_<sup>�</sup><sup>~~√~~</sup> _<u>𝑛</u>_<sup>�</sup> will vanish for all but finitely many _𝑛_ . 

To compute the Fourier transform of _𝑔_ , we can interchange the contour integral and Fourier transform, again assuming the integral is sufficiently well behaved. Then 



because the _𝑑_ -dimensional Fourier transform of the complex Gaussian _𝑥_ ↦→ _𝑒_<sup>_𝜋𝑖𝑧_|</sup><sup>_𝑥_|2</sup> with _𝑧_ ∈H is given by _𝑦_ ↦→( _𝑖_ / _𝑧_ )<sup>_𝑑_/2</sup> _𝑒_<sup>_𝜋𝑖_(−1/</sup><sup>_𝑧_) |</sup><sup>_𝑦_|2</sup> , and _𝑑_ = 8 here. Changing variables to _𝑢_ = −1/ _𝑧_ shows that 



In other words, taking the Fourier transform of _𝑔_ amounts to replacing _𝜓_ with − _𝜓_ |−2 _𝑆_ , and we obtain � _𝑔_ = − _𝑔_ if _𝜓_ |−2 _𝑆_ = _𝜓_ . 

Let Γ be the subgroup of SL2(Z) generated by _𝑆_ and _𝑇_<sup>2</sup> , which has index 3 in SL2 (Z). Then the conditions that _𝜓_ |−2 _𝑇_<sup>2</sup> = _𝜓_ (i.e., _𝜓_ ( _𝑧_ + 2) = _𝜓_ ( _𝑧_ )) and _𝜓_ |−2 _𝑆_ = _𝜓_ mean that _𝜓_ is _weakly modular of weight_ −2 for Γ. The reason why _𝜓_ is less than a full-fledged modular form is that it is only meromorphic at infinity (this is unavoidable, since the weight is negative). We furthermore require _𝜓_ to vanish at ±1, which will be enough to justify our integral manipulations and show that _𝑔_ is a Schwartz function. In terms of Fourier series, this vanishing says that _𝜓_ |−2 _𝑇𝑆_ has no negative terms in its _𝑞_ -series, because _𝑇𝑆_ maps the cusp _𝑖_ ∞ to 1. 

We will construct an example of the form _𝜓_ = _𝜓_ 0/Δ using the Δ function from (3.2), where _𝜓_ 0 is a genuine modular form of weight 10 for Γ. Note that the denominator of Δ causes no difficulties in H , since Δ( _𝑧_ ) ≠ 0 for all _𝑧_ ∈H , and the zero of Δ at infinity will lead to a pole of _𝜓_ . 

The function _𝜓_ 0 is modular of weight 10 for Γ, and thus also for Γ(2) because Γ(2) is a subgroup of Γ. In particular, _𝜓_ 0 must be a linear combination of _𝑈_<sup>5</sup> , _𝑈_<sup>4</sup> _𝑊_ , _𝑈_<sup>3</sup> _𝑊_<sup>2</sup> , ..., _𝑊_<sup>5</sup> , because _𝑈_ and _𝑊_ generate the ring of modular forms for Γ(2). The relations (3.3) specify 

**14 H. Cohn** 

the action of _𝑆_ and _𝑇_ , and they imply that the subspace invariant under _𝑆_ is spanned by 



with _𝑞_ -expansions 



in terms of _𝑞_<sup>1/2</sup> = _𝑒_<sup>_𝜋𝑖𝑧_</sup> . Now requiring _𝜓_ to vanish at ±1 determines it up to scaling as 



which yields a radial Schwartz function _𝑔_ : R<sup>8</sup> → R such that � _𝑔_ = − _𝑔_ and 



Note that we do not have much flexibility here: the values _𝑔_ (0), _𝑔_ (1), and _𝑔_<sup>�√</sup> 2<sup>�</sup> are uniquely determined by Poisson summation over Z<sup>8</sup> and _𝐸_ 8, up to scaling. 

We can rewrite the definition of _𝑓_ in another useful form as follows. If | _𝑥_ | is large enough (in fact, | _𝑥_ |<sup>2</sup> _>_ 2 will suffice), then 



In these manipulations, the second line merely breaks the integral in two, the third line uses the fact that 



as _𝑅_ →∞ (which holds if | _𝑥_ |<sup>2</sup> is large enough), and the fourth line uses _𝜓_ ( _𝑢_ − 1) = _𝜓_ ( _𝑢_ + 1). 

In other words, _𝑔_ ( _𝑥_ ) is given by sin( _𝜋_ | _𝑥_ |<sup>2</sup> ) times the Laplace transform of _𝑡_ ↦→ _𝜓_ ( _𝑖𝑡_ + 1) evaluated at _𝜋_ | _𝑥_ |<sup>2</sup> : 



**15 The work of Maryna Viazovska** 

While the original integral (4.1) converges for all _𝑥_ , this integral converges only when | _𝑥_ |<sup>2</sup> is large enough for the Gaussian factor _𝑒_<sup>−</sup><sup>_𝜋𝑡_|</sup><sup>_𝑥_|2</sup> to counteract the growth of _𝜓_ ( _𝑖𝑡_ + 1) as _𝑡_ →∞. In particular, (4.3) implies that 



as _𝑡_ →∞, which means we need | _𝑥_ |<sup>2</sup> _>_ 2. We can use this expansion to analytically continue _𝑔_ by removing the divergent terms: 



and this last formula holds regardless of | _𝑥_ |, with removable singularities at | _𝑥_ | = 0, 1, and √2. 

### **5. Viazovska’s construction for double roots** 

We are now in a position to obtain the magic function in eight dimensions. First, we will obtain the −1 eigenfunction _𝑓_ −. It is not immediately clear how to generalize the contour integral (4.1) from single to double roots, but the Laplace transform formula (4.4) generalizes elegantly. To obtain _𝑓_ −, we will look for a special function _𝜓_ such that 



when | _𝑥_ | is large enough. If we write −4 sin( _𝜋_ | _𝑥_ |<sup>2</sup> /2)<sup>2</sup> = _𝑒_<sup>−</sup><sup>_𝜋𝑖_|</sup><sup>_𝑥_|2</sup> + _𝑒_<sup>_𝜋𝑖_|</sup><sup>_𝑥_|2</sup> − 2, we find that 



We will construct a function _𝜓_ such that _𝜓_ is holomorphic on H and _𝜓_ ( _𝑧_ ) is exponentially bounded as Im _𝑧_ →∞. Under these conditions, when | _𝑥_ | is sufficiently large we can shift the contours and combine the integrals to obtain 



with the contours shown in Figure 7. This formula will be the analogue of (4.1), and it will define _𝑓_ − ( _𝑥_ ) for all _𝑥_ . 

**16 H. Cohn** 



**Figure 7** 

The contours used to obtain _𝑓_ − ( _𝑥_ ), labeled with their integrands (omitting _𝑒_<sup>_𝜋𝑖_|</sup><sup>_𝑥_|2</sup><sup>_𝑧_</sup> _𝑑𝑧_ ). 

Taking the Fourier transform amounts to replacing _𝑒_<sup>_𝜋𝑖_|</sup><sup>_𝑥_|2</sup><sup>_𝑧_</sup> with _𝑧_<sup>−4</sup> _𝑒_<sup>_𝜋𝑖_|</sup><sup>_𝑦_|2(−1/</sup><sup>_𝑧_)</sup> in the formula defining _𝑓_ −: 



We can now set _𝑢_ = −1/ _𝑧_ , which exchanges the four contours in pairs. The simplest way to obtain<sup>�</sup> _𝑓_ − = − _𝑓_ − would be if the resulting formula is exactly the negative of the formula with which we began. That amounts to the functional equations 



and 



Note that the structure of these equations reflects the integrands. 

Now the question is which sorts of functions _𝜓_ satisfy these functional equations. The simplest possibility would be some sort of modular form. The functional equations are not consistent with invariance under _𝑆_ and _𝑇_ , and so _𝜓_ cannot be modular for the full group SL2(Z). Let us suppose instead that _𝜓_ is weakly modular of weight −2 for Γ(2) (i.e., invariant under Γ(2) but only meromorphic at infinity). Then _𝜓_ |−2 _𝑇_ = _𝜓_ |−2 _𝑇_<sup>−1</sup> , because _𝑇_<sup>2</sup> ∈ Γ(2), and our functional equations become _𝜓_ |−2 _𝑇𝑆_ = − _𝜓_ |−2 _𝑇_ and _𝜓_ = _𝜓_ |−2 _𝑇_ + _𝜓_ |−2 _𝑆_ . Furthermore, the second equation implies the first, because _𝑆_<sup>2</sup> = _𝐼_ . We will therefore obtain the eigenfunction equation<sup>�</sup> _𝑓_ − = − _𝑓_ − as long as _𝜓_ is weakly modular of weight −2 for Γ(2) and satisfies _𝜓_ = _𝜓_ |−2 _𝑇_ + _𝜓_ |−2 _𝑆_ . 

**17 The work of Maryna Viazovska** 

As in the single-root case, it is natural to multiply _𝜓_ by Δ to try to eliminate a pole at infinity. Then _𝜓_ Δ will be a genuine modular form of weight 10 for Γ(2), and thus a linear combination of _𝑈_<sup>5</sup> , _𝑈_<sup>4</sup> _𝑊_ , _𝑈_<sup>3</sup> _𝑊_<sup>2</sup> , ..., _𝑊_<sup>5</sup> . One can check that the solutions of the remaining functional equation form a two-dimensional subspace, spanned by 

_𝛼_ := 2 _𝑈_<sup>4</sup> _𝑊_ − 4 _𝑈_<sup>3</sup> _𝑊_<sup>2</sup> + _𝑈_<sup>2</sup> _𝑊_<sup>3</sup> + _𝑈𝑊_<sup>4</sup> and _𝛽_ := 5 _𝑈_<sup>4</sup> _𝑊_ − 10 _𝑈_<sup>3</sup> _𝑊_<sup>2</sup> + 5 _𝑈_<sup>2</sup> _𝑊_<sup>3</sup> + _𝑊_<sup>5</sup> _,_ with 



We will take 



so that we eliminate the _𝑞_<sup>−1/2</sup> term in the _𝑞_ -series. The motivation for eliminating that term is that it prevents _𝑓_ − from having a pole at radius 1. To see why, let us analytically continue 



as in the single-root case. If _𝜓_ ( _𝑖𝑡_ ) = _𝑎_ 2 _𝑒_<sup>2</sup><sup>_𝜋𝑡_</sup> + _𝑎_ 1 _𝑒_<sup>_𝜋𝑡_</sup> + _𝑎_ 0 + · · · as _𝑡_ →∞, then 

Here the _𝑎_ 1 term has a pole unless _𝑎_ 1 = 0. For our choice of _𝜓_ , ( _𝑎_ 2 _, 𝑎_ 1 _, 𝑎_ 0) = (2 _,_ 0 _,_ 288), and thus _𝑓_ − has a single root at ~~√~~ 2 and double roots at √2 _𝑛_ for _𝑛_ ≥ 2. One can also check that _𝜓_ ( _𝑖𝑡_ ) vanishes as _𝑡_ → 0+ (equivalently, _𝜓_ |−2 _𝑆_ vanishes at infinity), which is enough for _𝑓_ − to be a Schwartz function and to justify all our integral manipulations. 

We have therefore obtained a magic eigenfunction _𝑓_ − as 



for | _𝑥_ |<sup>2</sup> _>_ 2, where 



Our scaling here does not yet match the magic function for sphere packing, but aside from that we have exactly what we need. 

Equation (5.1) implies that _𝜓_ ( _𝑖𝑡_ ) _>_ 0 for all _𝑡_ ∈(0 _,_ ∞). (Specifically, Δ( _𝑖𝑡_ ) _>_ 0 thanks to its product formula, _𝑊_ ( _𝑖𝑡_ ) _>_ 0 since it is the fourth power of a real quantity, and 5 _𝑈_ ( _𝑖𝑡_ )<sup>2</sup> − 5 _𝑈_ ( _𝑖𝑡_ ) _𝑊_ ( _𝑖𝑡_ ) + 2 _𝑊_ ( _𝑖𝑡_ )<sup>2</sup> _>_ 0 since it is a positive-definite quadratic form.) It follows that _𝑓_ − never changes sign beyond radius √2, in accordance with our expectations. However, note that our eigenfunction is positive beyond radius ~~√~~ 2, and so we will have to correct its sign later to match the magic function. 

All that remains is to construct a magic eigenfunction _𝑓_ + and take a suitable linear combination of _𝑓_ + and _𝑓_ − to obtain _𝑓_ . Constructing _𝑓_ + is very much like constructing _𝑓_ −. If we define _𝑓_ + for | _𝑥_ | sufficiently large by 



**18 H. Cohn** 

for some holomorphic function _𝜙_ : H → C, then the eigenfunction equation<sup>�</sup> _𝑓_ + = _𝑓_ + will follow from the functional equations 



and 



These are the same functional equations as we required for _𝜓_ , except for a factor of −1. 

A little manipulation using ( _𝑆𝑇_ )<sup>3</sup> = _𝐼_ shows that the first functional equation is equivalent to _𝜙_ |−2 _𝑆𝑇_ = _𝜙_ |−2 _𝑆_ . Thus, if we set _𝜒_ := _𝜙_ |−2 _𝑆_ , then _𝜒_ must be invariant under _𝑇_ . However, the second functional equation is more subtle. A short calculation shows that if _𝜒_ |0 _𝑆_ = _𝜒_ (equivalently, ( _𝜒_ |−2 _𝑆_ )( _𝑧_ ) = _𝑧_<sup>2</sup> _𝜒_ ( _𝑧_ )), then the second functional equation holds. In other words, it is enough for _𝜒_ to be weakly modular of weight 0 for SL2(Z). However, such functions turn out not to be sufficient to obtain _𝑓_ +. If one tries to solve for undetermined coefficients to construct _𝑓_ +, as in the _𝑓_ − case, one finds that there is no solution with the needed properties. 

Instead, we can use _quasimodular forms_ , not just modular forms. Recall that the Eisenstein series _𝐸_ 2 was not a modular form of weight 2, because conditional convergence interfered with the series manipulations needed to prove modularity. If we let 



then _𝐸_ 2 turns out to satisfy 



with the 6 _𝑖_ /( _𝜋𝑧_ ) term amounting to the deviation from modularity. A _quasimodular form of weight 𝑘 and depth ℓ_ for SL2 (Z) is a sum _𝑓𝑘_ + _𝑓𝑘_ −2 _𝐸_ 2 + · · · + _𝑓𝑘_ − _ℓ 𝐸_ 2<sup>_ℓ_, where each</sup><sup>_𝑓𝑗_is a</sup> modular form of weight _𝑘_ − 2 _𝑗_ . 

Instead of just a weakly modular form of weight 0, one can check that the function _𝜒_ can be a weakly quasimodular form of weight 0 and depth 2 for SL2(Z). Now we have enough flexibility to construct _𝑓_ +, and calculations much like those in the _𝑓_ − case lead to 



up to scaling. See Figure 8 for plots of the quasimodular forms that yield _𝑓_ − and _𝑓_ +. 

Now that we have obtained both magic eigenfunctions, we can construct the magic function _𝑓_ as a linear combination of them. First, we rescale _𝜙_ so that _𝑓_ +(0) = 1, and then we rescale _𝜓_ so that _𝑓_ −<sup>′</sup> �√2<sup>�</sup> = _𝑓_ +<sup>′</sup> �√2<sup>�</sup> , to obtain a double root at √2 for<sup>�</sup> _𝑓_ . Using these scalings, the eight-dimensional magic function is given by 



for | _𝑥_ |<sup>2</sup> _>_ 2, and the eigenfunction property implies that 



**19 The work of Maryna Viazovska** 





**Figure 8** 

Plots of _𝜓_ ( _𝑧_ )Δ( _𝑧_ ) (above) and ( _𝜑_ |−2 _𝑆_ ) ( _𝑧_ )Δ( _𝑧_ ) (below) for −1 ≤ Re _𝑧_ ≤ 1 and 0 _<_ Im _𝑧_ ≤ 1. 

for all _𝑦_ ≠ 0 (this integral turns out to converge whenever | _𝑦_ | _>_ 0, because the exponential growth in _𝜙_ ( _𝑖𝑡_ ) and _𝜓_ ( _𝑖𝑡_ ) as _𝑡_ →∞ cancels). 

The final step in the proof of Theorem 1.1 is to check the inequalities that are needed for Theorem 2.1, namely _𝑓_ ( _𝑥_ ) ≤ 0 for | _𝑥_ | ≥ 2 and<sup>�</sup> _𝑓_ ( _𝑦_ ) ≥ 0 for all _𝑦_ , to make sure there are no unexpected sign changes between the roots √2 _𝑛_ . In principle that might seem difficult, because integral transforms of quasimodular forms could be complicated. However, these inequalities hold for the simplest reason one could hope for: 



for all _𝑡>_ 0. In other words, the desired inequalities hold directly at the level of the quasimodular forms themselves. This can be checked rigorously in any of several ways. For example, one can use asymptotics to check the inequalities as _𝑡_ → 0 or _𝑡_ →∞, and then use interval arithmetic to verify them on the remaining bounded interval. 

**20 H. Cohn** 

Overall, this proof feels like a miracle. Everything falls beautifully into place, with Viazovska’s constructions having just enough flexibility to complete the proof in a unique way. What I find most impressive is the number of ingenious ideas required for the full proof. The single-root construction is itself remarkable, generalizing it to _𝑓_ − is even more so, and still more ideas are required for _𝑓_ +. Viazovska is a master of special functions, whose work would surely have excited Jacobi and Ramanujan. 

### **6. Interpolation and consequences** 

Along the way to proving the optimality of _𝐸_ 8, Viazovska made the bold conjecture that the magic function is uniquely determined by its required roots, and that more generally a radial Schwartz function on R<sup>8</sup> is uniquely determined by its values and radial derivatives at the radii √2 _𝑛_ and those of its Fourier transform. It is far from obvious that it is possible in principle to reconstruct a radial Schwartz function from discrete data of this sort. 

Radchenko and Viazovska took a major step in this direction by proving a onedimensional analogue for first-order interpolation, and the second-order theorem was proved by Cohn, Kumar, Miller, Radchenko, and Viazovska. 

**Theorem 6.1** (Radchenko and Viazovska **[23]** ). _There exist Schwartz functions 𝑎𝑛_ : R → R _such that for every Schwartz function 𝑓_ : R → R _and 𝑥_ ∈ R _,_ 



**Theorem 6.2** (Cohn, Kumar, Miller, Radchenko, and Viazovska **[11]** ). _Let_ ( _𝑑, 𝑛_ 0) _be_ (8 _,_ 1) _or_ (24 _,_ 2) _. Then every radial Schwartz function 𝑓_ : R<sup>_𝑑_</sup> → R _is uniquely determined by the values 𝑓_<sup>�√</sup> 2 _𝑛_<sup>�</sup> _, 𝑓_<sup>′�√</sup> 2 _𝑛_<sup>�</sup> _,_<sup>�</sup> _𝑓_<sup>�</sup><sup>~~√~~</sup> 2 _𝑛_<sup>�</sup> _, and_<sup>�</sup> _𝑓_<sup>′�√</sup> 2 _𝑛_<sup>�</sup> _for integers 𝑛_ ≥ _𝑛_ 0 _. Specifically, there exists an interpolation basis 𝑎𝑛, 𝑏𝑛 for 𝑛_ ≥ _𝑛_ 0 _such that for every radial Schwartz function 𝑓 and 𝑥_ ∈ R<sup>_𝑑_</sup> _,_ 



The proofs construct the interpolation bases explicitly, by combining Viazovska’s integral transform techniques with broader classes of special functions. 

One consequence of radial Fourier interpolation is a stronger optimality theorem for _𝐸_ 8 and the Leech lattice. Instead of just taking into account local interactions between particles, as in the sphere packing problem, one can study optimization problems with longrange interactions. For example, one could ask for the ground state of particles interacting via an inverse power law. Cohn and Kumar **[9]** formulated a broad notion of optimality, called _universal optimality_ , and radial Fourier interpolation yields corresponding magic functions: 

**Theorem 6.3** (Cohn, Kumar, Miller, Radchenko, and Viazovska **[11]** ). _The 𝐸_ 8 _root lattice and the Leech lattice are universally optimal in_ R<sup>8</sup> _and_ R<sup>24</sup> _, respectively._ 

**21 The work of Maryna Viazovska** 

### **7. The future** 

Although Viazovska’s work has settled several major questions, much remains to be understood. For example, the theory of interpolation for radial Schwartz functions is rapidly developing, with noteworthy connections to uniqueness theory for the Klein-Gordon equation **[2]** . 

One puzzling issue is two dimensions. While the two-dimensional sphere packing problem can be settled by elementary geometry, universal optimality remains a tantalizing conjecture. There seems to be a magic function for _𝑑_ = 2 in Theorem 2.1, with _𝑟_ = (4/3)<sup>1/4</sup> ; no proof is known, but numerical computations agree with the optimal packing density in R<sup>2</sup> to over one thousand decimal places. Furthermore, analogous magic functions seem to exist for universal optimality in R<sup>2</sup> . However, it is unclear what sort of function space might allow a suitable interpolation theory (see Section 7 in **[11]** ). 

There are also remarkable connections with conformal field theory and quantum gravity **[18]** . When _𝑑_ is even, the linear programming bound for the sphere packing density in R<sup>_𝑑_</sup> turns out to be equivalent to the spinless modular bootstrap bound for the spectral gap in a theory of _𝑑_ /2 free bosons, and the conformal bootstrap program generalizes it to a family of related bounds. How these more general bounds might relate to discrete geometry remains a mystery. 

### **References** 

- **[1]** N. Afkhami-Jeddi, H. Cohn, T. Hartman, D. de Laat, and A. Tajdini, _Highdimensional sphere packing and the modular bootstrap_ , J. High Energy Phys. **2020** (2020), no. 12, Paper No. 066, 44 pp. arXiv:2006.02560 doi:10.1007/jhep12(2020)066 

- **[2]** A. Bakan, H. Hedenmalm, A. Montes-Rodríguez, D. Radchenko, and M. Viazovska, _Fourier uniqueness in even dimensions_ , Proc. Natl. Acad. Sci. USA **118** (2021), no. 15, Paper No. 2023227118, 4 pp. doi:10.1073/pnas.2023227118 

- **[3]** A. Bondarenko, D. Radchenko, and M. Viazovska, _Optimal asymptotic bounds for spherical designs_ , Ann. of Math. (2) **178** (2013), no. 2, 443–452. arXiv:1009.4407 doi:10.4007/annals.2013.178.2.2 

- **[4]** J. Bourgain, L. Clozel, and J.-P. Kahane, _Principe d’Heisenberg et fonctions positives_ , Ann. Inst. Fourier (Grenoble) **60** (2010), no. 4, 1215–1232. arXiv:0811.4360 doi:10.5802/aif.2552 

- **[5]** H. Cohen and F. Strömberg, _Modular Forms: A Classical Approach_ , Graduate Studies in Mathematics **179** , American Mathematical Society, Providence, RI, 2017. 

- **[6]** H. Cohn, _A conceptual breakthrough in sphere packing_ , Notices Amer. Math. Soc. **64** (2017), no. 2, 102–115. arXiv:1611.01685 doi:10.1090/noti1474 

- **[7]** H. Cohn and N. Elkies, _New upper bounds on sphere packings I_ , Ann. of Math. (2) **157** (2003), no. 2, 689–714. arXiv:math/0110009 

**22 H. Cohn** 

||doi:10.4007/annals.2003.157.689|
|---|---|
|**[8]**|H. Cohn and F. Gonçalves,_An optimal uncertainty principle in twelve dimensions_<br>_via modular forms_, Invent. Math.**217**(2019), no. 3, 799–831. arXiv:1712.04438<br>doi:10.1007/s00222-019-00875-4|
|**[9]**|H. Cohn and A. Kumar,_Universally optimal distribution of points on spheres_, J.<br>Amer. Math. Soc.**20**(2007), no. 1, 99–148. arXiv:math/0607446<br>doi:10.1090/S0894-0347-06-00546-7|
|**[10]**|H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska,_The sphere_<br>_packing problem in dimension_24, Ann. of Math. (2)**185**(2017), no. 3, 1017–<br>1033. arXiv:1603.06518doi:10.4007/annals.2017.185.3.8|
|**[11]**|H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska,_Universal_<br>_optimality of the 𝐸_8_and Leech lattices and interpolation formulas_, Annals of<br>Mathematics, to appear. arXiv:1902.05438|
|**[12]**|J. H. Conway and N. J. A. Sloane,_Sphere Packings, Lattices and Groups_, third<br>edition, Grundlehren der Mathematischen Wissenschaften**290**, Springer-Verlag,<br>New York, 1999. doi:10.1007/978-1-4757-6568-7|
|**[13]**|P. Delsarte,_Bounds for unrestricted codes, by linear programming_, Philips Res.<br>Rep.**27**(1972), 272–289.|
|**[14]**|F. Diamond and J. Shurman,_A First Course in Modular Forms_, Graduate Texts<br>in Mathematics**228**, Springer-Verlag, New York, 2005. doi:10.1007/978-0-387-<br>27226-9|
|**[15]**|W. Ebeling,_Lattices and Codes: A Course Partially Based on Lectures by_<br>_Friedrich Hirzebruch_, third edition, Advanced Lectures in Mathematics. Springer<br>Spektrum, Wiesbaden, 2013. doi:10.1007/978-3-658-00360-9|
|**[16]**|T. C. Hales,_A proof of the Kepler conjecture_, Ann. of Math. (2)**162**(2005), no. 3,<br>1065–1185. doi:10.4007/annals.2005.162.1065|
|**[17]**|T. Hales, M. Adams, G. Bauer, T. D. Dang, J. Harrison, L. T. Hoang, C. Kaliszyk,<br>V. Magron, S. McLaughlin, T. T. Nguyen, Q. T. Nguyen, T. Nipkow, S. Obua,<br>J. Pleso, J. Rute, A. Solovyev, T. H. A. Ta, N. T. Tran, T. D. Trieu, J. Urban,<br>K. Vu, and R. Zumkeller,_A formal proof of the Kepler conjecture_, Forum Math.<br>Pi**5**(2017), e2, 29 pp. arXiv:1501.02155doi:10.1017/fmp.2017.1|
|**[18]**|T. Hartman, D. Mazáč, and L. Rastelli,_Sphere packing and quantum gravity_, J.<br>High Energy Phys.**2019**(2019), no. 12, 048, 66 pp. arXiv:1905.01319<br>doi:10.1007/jhep12(2019)048|
|**[19]**|E. Klarreich,_Sphere packing solved in higher dimensions_, Quanta Magazine,<br>March 30, 2016.https://www.quantamagazine.org/sphere-packing-solved-in-<br>higher-dimensions-20160330/|
|**[20]**|D. de Laat and F. Vallentin,_A breakthrough in sphere packing: the search for_<br>_magic functions_, Nieuw Arch. Wiskd. (5)**17**(2016), no. 3, 184–192.<br>arXiv:1607.02111|



**23 The work of Maryna Viazovska** 

- **[21]** D. Lowry-Duda, _Visualizing modular forms_ , in _Arithmetic Geometry, Number Theory, and Computation_ (J. S. Balakrishnan, N. Elkies, B. Hassett, B. Poonen, A. V. Sutherland, and J. Voight, eds.), Simons Symposia, Springer, 2021. arXiv:2002.05234 doi:10.1007/978-3-030-80914-0_19 

- **[22]** D. Madore, _Sections du diagramme de Voronoï du réseau 𝐸_ 8, David Madore’s WebLog, April 9, 2017. http://www.madore.org/~david/weblog/d.2017-04-09.2433.html 

- **[23]** D. Radchenko and M. Viazovska, _Fourier interpolation on the real line_ , Publ. Math. Inst. Hautes Études Sci. **129** (2019), 51–81. arXiv:1701.00265 doi:10.1007/s10240-018-0101-z 

- **[24]** J.-P. Serre, _A Course in Arithmetic_ , Graduate Texts in Mathematics **7** , SpringerVerlag, New York-Heidelberg, 1973. doi:10.1007/978-1-4684-9884-4 

- **[25]** T. M. Thompson, _From Error-correcting Codes through Sphere Packings to Simple Groups_ , Carus Mathematical Monographs **21** , Mathematical Association of America, Washington, DC, 1983. 

- **[26]** A. Thue, _Om nogle geometrisk-taltheoretiske Theoremer_ , Forhandlingerne ved de Skandinaviske Naturforskeres **14** (1892), 352–353. 

- **[27]** M. S. Viazovska, _The sphere packing problem in dimension_ 8, Ann. of Math. (2) **185** (2017), no. 3, 991–1015. arXiv:1603.04246 doi:10.4007/annals.2017.185.3.7 

- **[28]** D. Zagier, _Elliptic modular forms and their applications_ , in _The 1–2–3 of Modular Forms_ (K. Ranestad, ed.), pp. 1–103, Universitext, Springer, Berlin, 2008. doi:10.1007/978-3-540-74119-0_1 

### **Henry Cohn** 

Microsoft Research New England, One Memorial Drive, Cambridge, MA 02140, USA, cohn@microsoft.com 

**24 H. Cohn** 

