# Polyconvexity does not imply true-stress-true-strain monotonicity in the incompressible three-dimensional case

**arXiv ID**: 2607.06568v1
**Authors**: Dominik K. Klein, Maximilian P. Wollner, Patrizio Neff
**Published**: 2026-06-10
**Categories**: physics.class-ph, cond-mat.mtrl-sci, math-ph
**Comments**: 6 pages, 3 figures
**HTML URL**: https://arxiv.org/html/2607.06568v1

## Abstract

We study constitutive conditions of hyperelastic potentials for incompressible material behavior in three dimensions. By means of a counterexample, we show that polyconvexity does not imply true-stress-true-strain monotonicity. Thus, polyconvexity alone is not strong enough to guarantee a physically reasonable response for idealized elasticity.

## Full Text

Polyconvexity does not imply true-stress-true-strain monotonicity in the incompressible three-dimensional case

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- License: CC BY-NC-ND 4.0arXiv:2607.06568v1 [physics.class-ph] 10 Jun 2026

## Polyconvexity does not imply true-stress-true-strain monotonicity
in the incompressible three-dimensional caseDominik K. KleinCyber-Physical Simulation, Department of Mechanical Engineering, TU Darmstadt, 64293 Darmstadt, GermanyCorresponding author. E-mail addresses: klein@cps.tu-darmstadt.de, wollner@tugraz.at, patrizio.neff@uni-due.deMaximilian P. WollnerInstitute of Biomechanics, Graz University of Technology, Stremayrgasse 16/2, 8010, Graz, AustriaPatrizio NeffChair of Nonlinear Analysis and Modelling, University of Duisburg-Essen, Thea-Leymann-Straße 9, 45127, Essen, Germany(June 10, 2026)

## Zusammenfassung

We study constitutive conditions of hyperelastic potentials for incompressible material behavior in three dimensions. By means of a counterexample, we show that polyconvexity does not imply true-stress-true-strain monotonicity. Thus, polyconvexity alone is not strong enough to guarantee a physically reasonable response for idealized elasticity.

Keywords:hyperelasticity, incompressibility, constitutive inequalities, polyconvexity, true-stress-true-strain monotonicity, Hill’s inequality, Legendre-Hadamard ellipticity

## 1Introduction

We consider incompressible hyperelastic potentialsWWand the associated Cauchy stress tensor𝛔\bm{\upsigma}given byW:SL⁡(3)×\mathbb​R→\mathbb​R,(𝐅,p)↦W~​(𝐅)−p​(J−1)and𝛔=D𝐅​W~​𝐅T−p​𝐈,W:\operatorname{SL}(3)\times{\mathbb{R}}\rightarrow{\mathbb{R}}\,,\qquad(\mathbf{F},\,p)\mapsto\widetilde{W}(\mathbf{F})-p\,(J-1)\hskip 17.00024pt\text{and}\hskip 17.00024pt\bm{\upsigma}=\mathrm{D}_{\mathbf{F}}\widetilde{W}\,\mathbf{F}^{T}-p\mathbf{I}\,,(1.1)

where𝐅=D​𝝋\mathbf{F}=\mathrm{D}\bm{\varphi}is the deformation gradient derived from the deformation𝝋\bm{\varphi},ppis a Lagrange multiplier ensuring incompressibility (J=det𝐅=1J=\det\mathbf{F}=1), and𝐈\mathbf{I}is the second-order identity tensor. Here,SL(3):={𝐅∈\mathbbR3×3|det𝐅=1}\operatorname{SL}(3):=\big\{\mathbf{F}\in\allowbreak\;{\mathbb{R}}^{3\times 3}\,\rvert\,\allowbreak\det\mathbf{F}=1\big\}denotes the special linear group in three dimensions. We furthermore assume isotropy andW∈𝒞2W\in{\mathcal{C}}^{2}. One of the main challenges in material theory is the formulation of constitutive constraints imposed onWWand the investigation on how they relate to each other. Setting aside more obvious requirements such as frame indifference, we focus on the following conditions:

## Definition 1.1.

The potentialWWis polyconvex if there exists a representationW​(𝐅)=𝒫​(𝐅,Cof⁡𝐅),W(\mathbf{F})={\mathcal{P}}(\mathbf{F},\,\operatorname{Cof}\mathbf{F})\,,(1.2)

where𝒫:\mathbb​R3×3×\mathbb​R3×3→\mathbb​R{\mathcal{P}}:{\mathbb{R}}^{3\times 3}\times{\mathbb{R}}^{3\times 3}\rightarrow{\mathbb{R}}is a convex function. Note that the representation of polyconvex functions is non-unique.

## Definition 1.2.

The potentialWWis rank-one convex if it satisfiesW​(𝐅+t​𝒂⊗𝒃)≤t​W​(𝐅+𝒂⊗𝒃)+(1−t)​W​(𝐅)​∀t∈[0,1],𝒂,𝒃∈\mathbb​R3​with​𝒂⊗𝒃∈TSL⁡(3)⁡(𝐅),W(\mathbf{F}+t\,\bm{a}\otimes\bm{b})\leq t\,W(\mathbf{F}+\bm{a}\otimes\bm{b})+(1-t)\,W(\mathbf{F})\qquad\forall\,t\in[0,1],\,\bm{a},\bm{b}\in{\mathbb{R}}^{3}\qquad\text{with}\qquad\bm{a}\otimes\bm{b}\in\operatorname{T}_{\operatorname{SL}(3)}(\mathbf{F})\,,(1.3)

whereTSL⁡(3)(𝐅):={𝐇∈\mathbbR3×3|⟨𝐇,𝐅−T⟩=0}\operatorname{T}_{\operatorname{SL}(3)}(\mathbf{F}):=\big\{\mathbf{H}\in\allowbreak\;\mathbb{R}^{3\times 3}\,\rvert\,\allowbreak\bigl\langle\mathbf{H},\mathbf{F}^{-T}\bigr\rangle=0\big\}(1.4)

is the tangent space toSL⁡(3)\operatorname{SL}(3)at𝐅\mathbf{F}[6], which is equivalent to𝐅+𝒂⊗𝒃∈SL⁡(3)\mathbf{F}+\bm{a}\otimes\bm{b}\in\operatorname{SL}(3)[11, App. A]. Given sufficient differentiability, (1.3) implies the Legendre-Hadamard (LH) ellipticity condition⟨D𝐅2W(𝐅).(𝒂⊗𝒃),𝒂⊗𝒃⟩≥0∀𝒂,𝒃∈\mathbbR3,𝒂⊗𝒃∈TSL⁡(3)(𝐅),\bigl\langle\mathrm{D}^{2}_{\mathbf{F}}W(\mathbf{F}).(\bm{a}\otimes\bm{b}),\bm{a}\otimes\bm{b}\bigr\rangle\geq 0\qquad\forall\,\bm{a},\bm{b}\in{\mathbb{R}}^{3}\,,\,\,\,\bm{a}\otimes\bm{b}\in\operatorname{T}_{\operatorname{SL}(3)}(\mathbf{F})\,,(1.5)

where⟨(∙),(∙)⟩\langle(\bullet),(\bullet)\rangledenotes the inner product between two tensors of equal order and the dot in(∙).(∙)(\bullet).(\bullet)denotes the double contraction of a fourth-order tensor with a second-order tensor resulting in a second-order tensor.

## Definition 1.3.

The potentialWWfulfills the true-stress-true-strain monotonicity (TSTS-M) condition if the Cauchy stress satisfies⟨𝛔​(log⁡𝐕2)−𝛔​(log⁡𝐕1),log⁡𝐕2−log⁡𝐕1⟩>0∀𝐕1,𝐕2∈Sym++​(3),𝐕1≠𝐕2,\bigl\langle\bm{\upsigma}(\log\mathbf{V}_{2})-\bm{\upsigma}(\log\mathbf{V}_{1}),\log\mathbf{V}_{2}-\log\mathbf{V}_{1}\bigr\rangle>0\hskip 17.00024pt\forall\,\mathbf{V}_{1},\mathbf{V}_{2}\in\text{Sym}^{++}(3)\,,\,\,\,\mathbf{V}_{1}\neq\mathbf{V}_{2}\,,(1.6)

where𝐕=𝐅​𝐅T\mathbf{V}=\sqrt{\mathbf{F}\,\mathbf{F}^{T}}is the right stretch tensor andlog⁡𝐕\log\mathbf{V}denotes the Hencky strain[15,14]. Here,Sym++(3):={𝐕∈\mathbbR3×3|𝐕=𝐕T,⟨𝒂,𝐕𝒂⟩>0∀𝒂∈\mathbbR3∖{𝟎}}\text{Sym}^{++}(3):=\big\{\mathbf{V}\in{\mathbb{R}}^{3\times 3}\,\rvert\,\allowbreak\mathbf{V}=\mathbf{V}^{T},\,\langle\bm{a},\mathbf{V}\bm{a}\rangle>0\>\forall\,\bm{a}\in{\mathbb{R}}^{3}\setminus\{\mathbf{0}\}\big\}denotes the space of positive definite second-order tensors. Moreover, for incompressibility, the TSTS-M condition is equivalent to the inequality proposed by[9]reading⟨𝛕​(log⁡𝐕2)−𝛕​(log⁡𝐕1),log⁡𝐕2−log⁡𝐕1⟩>0∀𝐕1,𝐕2∈Sym++​(3),𝐕1≠𝐕2,tr⁡(log⁡𝐕i)=0,\bigl\langle\bm{\uptau}(\log\mathbf{V}_{2})-\bm{\uptau}(\log\mathbf{V}_{1}),\log\mathbf{V}_{2}-\log\mathbf{V}_{1}\bigr\rangle>0\hskip 17.00024pt\forall\,\mathbf{V}_{1},\mathbf{V}_{2}\in\text{Sym}^{++}(3)\,,\,\,\,\mathbf{V}_{1}\neq\mathbf{V}_{2}\,,\,\,\,\operatorname{tr}\left(\log{\mathbf{V}_{i}}\right)=0\,,(1.7)

with the Kirchhoff stress[19,21]𝛕=Dlog⁡𝐕​W^​(log⁡𝐕)​with​W^​(log⁡𝐕)=W​(𝐅),\bm{\uptau}=\mathrm{D}_{\log\mathbf{V}}\widehat{W}(\log\mathbf{V})\qquad\text{with}\qquad\widehat{W}(\log\mathbf{V})=W(\mathbf{F})\,,(1.8)

since𝛕=𝛔\bm{\uptau}=\bm{\upsigma}fordet𝐅=1\det\mathbf{F}=1[27,1]. Making use of the reduced representationW^redinc​(log⁡λ1,log⁡λ2):=Ψ​(λ1,λ2,1/(λ1​λ2))=Ψ​(λ1,λ2,λ3)=W​(𝐅),\widehat{W}_{\text{red}}^{\text{inc}}(\log\lambda_{1},\log\lambda_{2}):=\Psi(\lambda_{1},\lambda_{2},1/(\lambda_{1}\lambda_{2}))=\Psi(\lambda_{1},\lambda_{2},\lambda_{3})=W(\mathbf{F})\,,(1.9)

convexity ofW^redinc\widehat{W}_{\text{red}}^{\text{inc}}in(log⁡λ1,log⁡λ2)(\log\lambda_{1},\log\lambda_{2})can be derived as a sufficient and necessary condition for Hill’s inequality in the incompressible case[1, App. D.3].

Polyconvexity is linked to existence theorems in finite elasticity theory[2,3]. LH-ellipticity, from a physical perspective, guarantees the existence of real-valued wave speeds for solutions of the governing equations of finite elasticity theory[28]. Moreover, it is commonly employed to ensure a stable and robust behavior when applying a constitutive model in numerical applications such as the finite element method[23], see also[12, Sect. 1.1]. On the other hand, the TSTS-M condition can be seen as the multiaxial analogue of the notion that the Cauchy stress must be increasing with increasing Hencky strain, which seems a reasonable requirement for a purely elastic material law. Moreover, TSTS-M ensures that the tangent operator in a hypoelastic formulation is positive definite, i.e.,⟨Dlog⁡𝐕𝛔(log𝐕).𝐇,𝐇⟩>0∀𝐇∈\mathbbR3×3∖{𝟎},\bigl\langle\mathrm{D}_{\log\mathbf{V}}\bm{\upsigma}(\log\mathbf{V}).\mathbf{H},\mathbf{H}\bigr\rangle>0\qquad\forall\,\mathbf{H}\in{\mathbb{R}}^{3\times 3}\setminus\{\mathbf{0}\}\,,(1.10)

and it supports a local existence proof of rate-form equilibrium, even without LH-ellipticity[17,20].Abbildung 1:Overview of various constitutive constraints and their relation in isotropic incompressible hyperelasticity.

In the following, we consider two parameterizations for polyconvex potentials:

## Theorem 1.4.

[2, Thm. 5.1]providessufficient but not necessaryconditions for polyconvexity. For this, we considerW​(𝐅)=g​(\varkappaλ)​with​\varkappaλ=(λ1,λ2,λ3,λ2​λ3,λ1​λ3,λ1​λ2)​and​g~​(λ1,λ2,λ3)=g​(\varkappaλ),W(\mathbf{F})=g(\bm{\varkappa}_{\lambda})\qquad\text{with}\qquad\bm{\varkappa}_{\lambda}=(\lambda_{1},\,\lambda_{2},\,\lambda_{3},\,\lambda_{2}\lambda_{3},\,\lambda_{1}\lambda_{3},\,\lambda_{1}\lambda_{2})\qquad\text{and}\qquad\widetilde{g}(\lambda_{1},\,\lambda_{2},\,\lambda_{3})=g(\bm{\varkappa}_{\lambda})\,,(1.11)

where the principal stretchesλi\lambda_{i}are the singular values of𝐅\mathbf{F}andλi​λj\lambda_{i}\lambda_{j}are the singular values ofCof⁡𝐅\operatorname{Cof}\mathbf{F}. Polyconvexity is fulfilled if (i)ggis convex and monotonically increasing and (ii)g~\widetilde{g}satisfies the permutation invariance111For Ball’s original proof, a stricter permutation invariance is required, i.e., it must be independently hold for the first three and the second three arguments ofgg. However,[7, Sect. 3.3]recently showed that the relaxed permutation invariance in (1.12) is also sufficient.g~​(λ1,λ2,λ3)=g~​(λ1,λ3,λ2)=g~​(λ2,λ1,λ3)=g~​(λ2,λ3,λ1)=g~​(λ3,λ1,λ2)=g~​(λ3,λ2,λ1).\widetilde{g}(\lambda_{1},\,\lambda_{2},\,\lambda_{3})=\widetilde{g}(\lambda_{1},\,\lambda_{3},\,\lambda_{2})=\widetilde{g}(\lambda_{2},\,\lambda_{1},\,\lambda_{3})=\widetilde{g}(\lambda_{2},\,\lambda_{3},\,\lambda_{1})=\widetilde{g}(\lambda_{3},\,\lambda_{1},\,\lambda_{2})=\widetilde{g}(\lambda_{3},\,\lambda_{2},\,\lambda_{1})\,.(1.12)

## Theorem 1.5.

[25]providesufficient and necessaryconditions for polyconvexity in terms of the signed singular valuesνi\nu_{i}of𝐅\mathbf{F}and the signed singular valuesνi​νj\nu_{i}\nu_{j}ofCof⁡𝐅\operatorname{Cof}\mathbf{F}.222Sufficient and necessary conditions for polyconvexity of isotropic potentials were also established in earlier works[13,22], for instance,[5]proposed conditions similar to Theorem1.5for the two-dimensional case, referred to asdiagonal polyconvexity.For this, we considerW​(𝐅)=h​(\varkappaν)​with​\varkappaν=(ν1,ν2,ν3,ν2​ν3,ν1​ν3,ν1​ν2)​and​h~​(ν1,ν2,ν3)=h​(\varkappaν).W(\mathbf{F})=h(\bm{\varkappa}_{\nu})\qquad\text{with}\qquad\bm{\varkappa}_{\nu}=(\nu_{1},\,\nu_{2},\,\nu_{3},\,\nu_{2}\nu_{3},\,\nu_{1}\nu_{3},\,\nu_{1}\nu_{2})\qquad\text{and}\qquad\widetilde{h}(\nu_{1},\,\nu_{2},\,\nu_{3})=h(\bm{\varkappa}_{\nu})\,.(1.13)

Polyconvexity is fulfilled if and only if (i)hhis convex, (ii)h~\widetilde{h}isΠ3\Pi_{3}-invariant, which includes the six permutations introduced in (1.12) and the four symmetriesh~​(ν1,ν2,ν3)=h~​(−ν1,−ν2,ν3)=h~​(−ν1,ν2,−ν3)=h~​(ν1,−ν2,−ν3),\displaystyle\widetilde{h}(\nu_{1},\,\nu_{2},\,\nu_{3})=\widetilde{h}(-\nu_{1},\,-\nu_{2},\,\nu_{3})=\widetilde{h}(-\nu_{1},\,\nu_{2},\,-\nu_{3})=\widetilde{h}(\nu_{1},\,-\nu_{2},\,-\nu_{3})\,,(1.14)

and (iii)hhis lower semi-continuous.

The following relations are well-established for incompressible hyperelasticity in three dimensions:
- –

Rank-one convexity does not imply polyconvexity[4].
- –

TSTS-M does not imply polyconvexity or rank-one convexity[27, Sect. 3.3].
- –

Polyconvexity implies rank-one convexity[4]. Moreover, we recently showed that the polyconvex parameterization by Ball, cf. Theorem1.4, implies TSTS-M[27, Sect. 3.1.4].Abbildung 2:Visualization of the softplus function𝒮​𝒫​(x)\mathcal{SP}(x)employed for the potential in (2.1). The stress response of the potential, cf. (2.5) and (2.7), depends on the sigmoid function𝒮​ℳ​(x)=Dx​𝒮​𝒫​(x)\mathcal{SM}(x)=\mathrm{D}_{x}\mathcal{SP}(x), which is the first derivative of the softplus function.

Above introduced conditions are of particular interest for one of the main open problems of material theory, often referred to as Truesdell’s Hauptproblem[24]: If we disregard any inelastic effects such as fatigue, softening, or plasticity, what set of constitutive constraints is required to represent idealized elasticity? Setting aside obvious requirements such as frame indifference, one approach could be the combination of polyconvexity (and thus LH-ellipticity) in combination with TSTS-M[26,15]. Together, these ensure a monotonically increasing Cauchy stress response for load scenarios where we would expect such a behavior, notably for uniaxial tension, equibiaxial tension, and simple shear. While additional constraints might be required to represent idealized elasticity333We recently raised the question whether for idealized elasticity, in addition to TSTS-M which restricts the slope of the Cauchy stress, an additional constraint on the curvature of the Cauchy stress might be required[27, Sect. 5.4]., the aforementioned conditions already go a long way towards this goal. In incompressibility, we recently showed that Ball’s sufficient conditions for polyconvexity also imply TSTS-M[27, Sect. 3.1.4], which applies to a variety of models based on principal stretches and models based on the main invariants of the right Cauchy-Green tensor𝐂=𝐅T​𝐅\mathbf{C}=\mathbf{F}^{T}\mathbf{F}. However, the parameterization of Ball is only sufficient but not necessary for polyconvexity. Therefore, in the incompressible three-dimensional case, it remains unclear whether polyconvexity in general implies TSTS-M.444In the three-dimensional compressible case, polyconvexity does not imply TSTS-M[26], while in the incompressible two-dimensional case, polyconvexity does imply TSTS-M[8]. However, the transition between two and three dimensions or compressibility and incompressibility entails some theoretical nuances, requiring independent investigations for each setting. Thus, it remained an open problem whether polyconvexity or rank-one convexity imply TSTS-M in the incompressible three-dimensional case.In this contribution, we address this and show the following:
- –

Polyconvexity does not imply TSTS-M in the incompressible three-dimensional case.

For this, we provide a counterexample which is polyconvex but does not satisfy TSTS-M, making use of the sufficient and necessary conditions for polyconvexity proposed by[25].555The construction of such a counterexample was part of a series of challenges posed by Patrizio Neff. In particular, he still offers a prize money of 500€ for the construction of a compressible energy that simultaneously satisfies polyconvexity (or rank-one convexity) and TSTS-M for all deformation states[16].Since polyconvexity implies rank-one convexity, our counterexample also establishes the following result:
- –

Rank-one convexity does not imply TSTS-M in the incompressible three-dimensional case.

Overall, our work completes the investigation of the relationships between the above introduced constitutive conditions, cf. Fig.1.Abbildung 3:Evaluation of the potential in (2.1) with parameters(a,b,c)=(−5,−14,−22)(a,\,b,\,c)=(-5,\,-14,\,-22). The potential is polyconvex but violates TSTS-M[18]. This counterexample shows that polyconvexity does not imply TSTS-M in the incompressible three-dimensional case.

## 2A counterexample

Let us consider the isotropic incompressible potentialψ​(ν1,ν2,ν3)=ϕ​(ν1,ν2,ν3)+ϕ​(−ν1,−ν2,ν3)+ϕ​(ν1,−ν2,−ν3)+ϕ​(−ν1,ν2,−ν3)+const.,\displaystyle\psi(\nu_{1},\nu_{2},\nu_{3})=\phi(\nu_{1},\nu_{2},\nu_{3})+\phi(-\nu_{1},-\nu_{2},\nu_{3})+\phi(\nu_{1},-\nu_{2},-\nu_{3})+\phi(-\nu_{1},\nu_{2},-\nu_{3})+\text{const.}\,,(2.1)

based on the softplus function𝒮​𝒫​(x)=log⁡(1+exp⁡x)\mathcal{SP}(x)=\log(1+\exp x), which we visualize in Fig.2(a), withϕ​(ν1,ν2,ν3)=𝒮​𝒫​(θ​(\varkappaν))​and​θ​(\varkappaν)=a​(ν1+ν2+ν3)+b​(ν1​ν2+ν2​ν3+ν3​ν1)+c,\phi(\nu_{1},\nu_{2},\nu_{3})=\mathcal{SP}(\theta(\bm{\varkappa}_{\nu}))\qquad\text{and}\qquad\theta(\bm{\varkappa}_{\nu})=a\,(\nu_{1}+\nu_{2}+\nu_{3})+b\,(\nu_{1}\nu_{2}+\nu_{2}\nu_{3}+\nu_{3}\nu_{1})+c\,,(2.2)

wherea,b,c∈\mathbb​Ra,b,c\in\mathbb{R}are material parameters.666The structure of the potential in (2.1) closely resembles constitutive models based on neural networks, which are often based on linear transformations and the softplus function[27].

## Theorem 2.1.

The potentialψ\psiin (2.1) is polyconvex for all choices ofa,b,c∈\mathbb​Ra,b,c\in{\mathbb{R}}.

## Beweis.

The potentialψ\psisatisfies the following sufficient and necessary conditions for polyconvexity, cf.[7, Cor. 2]and Theorem1.5:
- (i)

The potentialψ\psiis convex in\varkappaν=(ν1,ν2,ν3,ν2​ν3,ν1​ν3,ν1​ν2)\bm{\varkappa}_{\nu}=(\nu_{1},\,\nu_{2},\,\nu_{3},\,\nu_{2}\nu_{3},\,\nu_{1}\nu_{3},\,\nu_{1}\nu_{2})for any choice ofa,b,c∈\mathbb​Ra,b,c\in{\mathbb{R}}. This can be seen as follows: The functionθ\theta, defined in (2.2), is linear in\varkappaν\bm{\varkappa}_{\nu}. Since the softplus function𝒮​𝒫​(x)=log⁡(1+exp⁡x)\mathcal{SP}(x)=\log(1+\exp x)is convex, it follows that𝒮​𝒫​(θ​(\varkappaν))\mathcal{SP}(\theta(\bm{\varkappa}_{\nu}))is also convex. Then, notice thatψ\psiis a simple sum of functions of the form𝒮​𝒫​(θ​(\varkappaν))\mathcal{SP}(\theta(\bm{\varkappa}_{\nu})), albeit with a change of sign in the arguments. But these sign reversals leave the linearity ofθ\thetauntouched, hence each summand remains convex following the argument above.
- (ii)

The functionψ\psiobeysΠ​(3)\Pi(3)-invariance, since it is invariant under permutation of its arguments and satisfies the symmetries introduced in (1.14) by construction.
- (iii)

The strain-energy functionψ\psiis continuous and therefore lower semi-continuous.

∎

An alternative, more direct proof can be achieved through[25, Prop. 5.2], cf. also[7, Sect. 3.2.2].

As a sanity check, we may verify the monotonicity of the true-shear-stress response given the potential in (2.1) in simple shear, as required by rank-one convexity. For simple shear along𝒆1\bm{e}_{1}-𝒆2\bm{e}_{2}in an underlying Cartesian coordinate system, the deformation gradient𝐅ss\mathbf{F}_{\mathrm{ss}}and the true shear stressτ\tauare given by[𝐅ss]=𝐈+γ​𝒆1⊗𝒆2​and​τ=⟨𝛔ss,𝒆1⊗𝒆2⟩,[\mathbf{F}_{\mathrm{ss}}]=\mathbf{I}+\gamma\,\bm{e}_{1}\otimes\bm{e}_{2}\qquad\text{and}\qquad\tau=\bigl\langle\bm{\upsigma}_{\mathrm{ss}},\bm{e}_{1}\otimes\bm{e}_{2}\big\rangle\,,(2.3)

whereγ∈\mathbb​R\gamma\in{\mathbb{R}}is the amount of shear and𝛔ss\bm{\upsigma}_{\mathrm{ss}}denotes the Cauchy stress tensor resulting from the elastic law given𝐅ss\mathbf{F}_{\mathrm{ss}}. Then, if the potential is polyconvex (or rank-one convex),τ\tauis monotonically increasing inγ\gamma[26, Prop. 5.13]. In the following, we employ the material parameters777For ease of exposition, we omit any units.(a,b,c)=(−5,−14,−22),(a,\,b,\,c)=(-5,\,-14,\,-22)\,,(2.4)

for which the true shear stress given (2.1) can be calculated as[10]τ​(γ)=(ν12ν12+1​Dν1​ψ−ν22ν22+1​Dν2​ψ)|ν1=(γ+4+γ2)/2ν2=2/(γ+4+γ2)ν3=1=19​γ4+γ2(𝒮ℳ(194+γ2−41)+𝒮ℳ(194+γ2+41)−1)+9(𝒮ℳ(9γ−3)+𝒮ℳ(9γ+3)−1),\begin{split}\tau(\gamma)&=\biggl(\frac{\nu_{1}^{2}}{\nu_{1}^{2}+1}\,\mathrm{D}_{\nu_{1}}{\psi}-\frac{\nu_{2}^{2}}{\nu_{2}^{2}+1}\,\mathrm{D}_{\nu_{2}}{\psi}\biggr)\Bigg|_{\begin{subarray}{l}\nu_{1}=\big(\gamma+\sqrt{4+\gamma^{2}}\big)/2\\
\nu_{2}=2/\big(\gamma+\sqrt{4+\gamma^{2}}\big)\\
\nu_{3}=1\end{subarray}}\\
&=\frac{19\,\gamma}{\sqrt{4+\gamma^{2}}}\biggl(\mathcal{SM}\Bigl(19\sqrt{4+\gamma^{2}}-41\Bigr)+\mathcal{SM}\Bigl(19\sqrt{4+\gamma^{2}}+41\Bigl)-1\biggr)\\
&\hphantom{=}\>+9\Bigl(\mathcal{SM}\bigl(9\,\gamma-3\bigr)+\mathcal{SM}\bigl(9\,\gamma+3\bigl)-1\Bigr)\,,\end{split}(2.5)

where the sigmoid function𝒮​ℳ​(x)=Dx​𝒮​𝒫​(x)=exp⁡x/(1+exp⁡x)\mathcal{SM}(x)=\mathrm{D}_{x}\mathcal{SP}(x)=\exp x/(1+\exp x)denotes the first derivative of the softplus function, visualized in in Fig.2(b). As expected, the true shear stress of (2.1) is monotonic, which we visualize in Fig.3(a). Notably, the shear stress has an asymptote atτ=28\tau=28, which can be seen by evaluating (2.5) for largeγ\gamma, where𝒮​ℳ​(x)→1\mathcal{SM}(x)\rightarrow 1asx→∞x\rightarrow\infty, see also Fig.2(b).

## Theorem 2.2.

The potentialψ\psiin (2.1) violates TSTS-M in uniaxial tension for the material parameters defined in (2.4).

## Beweis.

For uniaxial tension along𝒆1\bm{e}_{1}of an underlying Cartesian coordinate system, the deformation gradient𝐅ux\mathbf{F}_{\mathrm{ux}}and the Cauchy stress𝛔ux\bm{\upsigma}_{\mathrm{ux}}are given by[𝐅ux]=diag⁡(λ,λ−1/2,λ−1/2)​and​[𝛔ux]=diag⁡(σ,0,0),[\mathbf{F}_{\mathrm{ux}}]=\operatorname{diag}\bigl(\lambda,\,\lambda^{-1/2},\,\lambda^{-1/2}\bigr)\qquad\text{and}\qquad[\bm{\upsigma}_{\mathrm{ux}}]=\operatorname{diag}(\sigma,\,0,\,0)\,,(2.6)

whereλ>1\lambda>1andσ\sigmadenote the stretch and Cauchy stress in tensile direction, respectively. Then, if the TSTS-M condition is fulfilled,σ\sigmais strictly monotonically increasing inλ\lambda[20]. The Cauchy stress of the potential in (2.1) can be calculated in closed form, such thatσ​(λ)=(λ​Dν1​ψ~−1λ​Dν3​ψ~)|ν1=λν2=λ−1/2ν3=λ−1/2=(10​λ−28λ)​𝒮​ℳ​(5​λ+14λ−22)−1λ​(λ+1)​(5​λ−14)​(λ−λ+1)​𝒮​ℳ​(−5​λ−14λ−22+10λ+28​λ)−1λ​(λ−1)​(5​λ+14)​(λ+λ+1)​𝒮​ℳ​(−5​λ−14λ−22−10λ−28​λ).\begin{split}\sigma(\lambda)&=\biggl(\lambda\,\mathrm{D}_{\nu_{1}}\widetilde{\psi}-\frac{1}{\sqrt{\lambda}}\,\mathrm{D}_{\nu_{3}}\widetilde{\psi}\biggr)\Bigg|_{\begin{subarray}{l}\nu_{1}=\lambda\\
\nu_{2}=\lambda^{-1/2}\\
\nu_{3}=\lambda^{-1/2}\end{subarray}}\\
&=\Bigl(10\lambda-\frac{28}{\lambda}\Bigr)\,\mathcal{SM}\Bigl(5\lambda+\frac{14}{\lambda}-22\Bigr)\\
&\hphantom{=}\>-\frac{1}{\lambda}\Bigl(\sqrt{\lambda}+1\Bigr)\Bigl(5\sqrt{\lambda}-14\Bigr)\Bigl(\lambda-\sqrt{\lambda}+1\Bigr)\,\mathcal{SM}\biggl(-5\lambda-\frac{14}{\lambda}-22+\frac{10}{\sqrt{\lambda}}+28\sqrt{\lambda}\biggr)\\
&\hphantom{=}\>-\frac{1}{\lambda}\Bigl(\sqrt{\lambda}-1\Bigr)\Bigl(5\sqrt{\lambda}+14\Bigr)\Bigl(\lambda+\sqrt{\lambda}+1\Bigr)\,\mathcal{SM}\biggl(-5\lambda-\frac{14}{\lambda}-22-\frac{10}{\sqrt{\lambda}}-28\sqrt{\lambda}\biggr)\,.\end{split}(2.7)

A numerical analysis reveals that the Cauchy stress of (2.1) is not monotonically increasing for some stretches, e.g.,σ​(1.5)≈14.5>σ​(2.5)≈12.3.\sigma(1.5)\approx 14.5>\sigma(2.5)\approx 12.3\,.(2.8)

Hence, TSTS-M is not fulfilled.

Alternatively, a loss of TSTS-M can be shown by inspecting the potential (2.1) through the reduced representationW^redinc\widehat{W}_{\mathrm{red}}^{\mathrm{inc}}in (1.9) forlog⁡λ1=log⁡λ\log\lambda_{1}=\log\lambdaandlog⁡λ2=−log⁡λ/2\log\lambda_{2}=-\log\lambda/2which reveals a lack of convexity. We provide a visualization of both approaches in Fig.3(b,c). As expected, the conditions are violated for the same interval of stretch valuesλ\lambda.
∎

## Corollary 2.3.

Polyconvexity does not imply TSTS-M in the incompressible three-dimensional case. This follows from our counterexample of a potential that is polyconvex but does not satisfsy TSTS-M, cf. Theorems2.1and2.2.

## Corollary 2.4.

Rank-one convexity does not imply TSTS-M in the incompressible three-dimensional case. This follows from Corollary2.3and the observation that polyconvexity implies rank-one convexity.

## 3Conclusion

We recently showed that Ball’s sufficient conditions for polyconvexity imply TSTS-M in the incompressible three-dimensional case[27, Prop. 3.3], which raised the question whether this implication also holds for general polyconvex parameterizations[27, Sect. 3.4]. As shown in the present work, the answer is no: In the three-dimensional incompressible case, polyconvexity does not imply TSTS-M and polyconvexity alone is not sufficient to guarantee a physically reasonable response for idealized elastic materials.

CRediT authorship contribution statementDominik K. Klein:Conceptualization, Formal analysis, Visualization, Writing – original draft, Writing – review and editing.Maximilian P. Wollner:Conceptualization, Formal analysis, Writing – review and editing.Patrizio Neff:Conceptualization, Writing – original draft, Writing – review and editing.
Conflict of interestThe authors declare that they have no conflict of interest.
AcknowledgmentsWe want to acknowledge that, independently of our work and roughly at the same time, Gian-Luca Geuken found a similar counterexample. Moreover, we want to thank him and David Wiedemann for helpful comments on the manuscript. Dominik K. Klein acknowledges the financial support provided by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation, project number 492770117) and the Graduate School of Computational Engineering at TU Darmstadt.
Data availabilityThe authors have no data to share.

## Literatur
- [1]H. Baaser(2026)Hyperelastic stability landscape: a check for HILL stability of isotropic, incompressible hyperelasticity depending on material parameters.J. Elast.158(8),pp. 1–34.External Links:DocumentCited by:Definition 1.3,Definition 1.3.
- [2]J. M. Ball(1976)Convexity conditions and existence theorems in nonlinear elasticity.Arch. Rational Mech. Anal.63,pp. 337–403.External Links:DocumentCited by:Theorem 1.4,§1.
- [3]J. M. Ball(1977)Constitutive inequalities and existence theorems in nonlinear elastostatics.InNonlinear analysis and mechanics: Heriot-Watt Symposium,R. J. Knops (Ed.),Vol.1,pp. 187–241.Cited by:§1.
- [4]P. G. Ciarlet(1988)Mathematical elasticity volume i: three-dimensional elasticity.Studies in Mathematics and its Applications,North-Holland Publishing Company.Cited by:1st item,3rd item.
- [5]B. Dacorogna and H. Koshigoe(1993)On the different notions of convexity for rotationally invariant functions.Ann. Fac. Sci. Toulouse Math.2(2),pp. 163–184.Cited by:footnote 2.
- [6]J. E. Dunn, R. Fosdick, and Y. Zhang(2003)Rank 1 convexity for a class of incompressible elastic materials.InRational Continua, Classical and New: A collection of papers dedicated to Gianfranco Capriz on the occasion of his 75th birthday,P. Podio-Guidugli and M. Brocato (Eds.),pp. 89–96.External Links:ISBN 978-88-470-2231-7,Document,LinkCited by:Definition 1.2.
- [7]G.-L. Geuken, P. Kurzeja, D. Wiedemann, M. Zlatić, M. Čanađija, and J. Mosler(2026)Modeling isotropic polyconvex hyperelasticity by neural networks – sufficient and necessary criteria for compressible and incompressible materials.Pre-print under review.External Links:2603.27351Cited by:§2,§2,footnote 1.
- [8]I.-D. Ghiba, M. P. Wollner, and P. Neff(n.a.)Polyconvexity implies Hill’s inequality in SL(2).n.a.Note:(in preparation)Cited by:footnote 4.
- [9]R. Hill(1970)Constitutive inequalities for isotropic elastic solids under finite strain.J. Mech. Phys. Solids314,pp. 457–472.External Links:DocumentCited by:Definition 1.3.
- [10]C. O. Horgan and J. G. Murphy(2010)Simple shearing of incompressible and slightly compressible isotropic nonlinearly elastic materials.J. Elast.(98),pp. 205–221.External Links:DocumentCited by:§2.
- [11]D. K. Klein, H. Mokarram, K. Kikinov, M. Kannapinn, S. Rudykh, and A. J. Gil(2026)Neural networks meet hyperelasticity: A monotonic approach.Eur. J. Mech., A/Solids116,pp. 105900.External Links:DocumentCited by:Definition 1.2.
- [12]D. K. Klein, R. Ortigosa, H. T. Roth, K. A. Kalina, J. Martínez-Frutos, M. Kästner, and O. Weeger(2026)On limitations of polyconvexity.Pre-print under review.External Links:2605.31392Cited by:§1.
- [13]A. Mielke(2005)Necessary and sufficient conditions for polyconvexity of isotropic functions.J. Convex Anal.12(2),pp. 291–314.Cited by:footnote 2.
- [14]P. Neff, B. Eidel, and R. J. Martin(2016)Geometry of logarithmic strain measures in solid mechanics.Arch. Rational Mech. Anal.222,pp. 507–572.External Links:DocumentCited by:Definition 1.3.
- [15]P. Neff, S. Holthausen, M. V. d’Agostino, D. Bernardini, A. Sky, I.-D. Ghiba, and R. J. Martin(2025)Hypo-elasticity, Cauchy-elasticity, corotational stability and monotonicity in the logarithmic strain.J. Mech. Phys. Solids202,pp. 106074.External Links:DocumentCited by:Definition 1.3,§1.
- [16]P. Neff, N. J. Husemann, S. Holthausen, M. V. d’Agostino, D. Bernardini, A. Sky, A. S. Tchakoutio Nguetcho, I.-D. Ghiba, R. J. Martin, F. Gmeineder, S. N. Korobeynikov, and T. Blesgen(2025)Truesdell’s Hauptproblem: on constitutive stability in idealized isotropic nonlinear elasticity and a 500€ challenge.External Links:DocumentCited by:footnote 5.
- [17]P. Neff, N. J. Husemann, S. Holthausen, F. Gmeineder, and T. Blesgen(2026)Rate-form equilibrium for an isotropic Cauchy-elastic formulation.
- [24]Part I: Modeling.J. Nonlinear Sci.36(8),pp. 1–46.External Links:DocumentCited by:§1.
- [18]P. Neff, N. J. Husemann, S. N. Korobeynikov, I.-D. Ghiba, and R. J. Martin(2025)A natural requirement for objective corotational rates—on structure-preserving corotational rates.Acta. Mech.236,pp. 2657–2689.External Links:DocumentCited by:Abbildung 3,Abbildung 3.
- [19]P. Neff, K. Graban, E. Schweickert, and R. J. Martin(2019)The axiomatic introduction of arbitrary strain tensors by hans richter – a commented translation of "strain tensor, strain deviator and stress tensor for finite deformations".External Links:1909.05998Cited by:Definition 1.3.
- [20]P. Neff, N. J. Husemann, A. S. Nguetcho Tchakoutio, S. N. Korobeynikov, and R. J. Martin(2025)The corotational stability postulate: positive incremental cauchy stress moduli for diagonal, homogeneous deformations in isotropic nonlinear elasticity.Int. J. Non-Linear Mech.174,pp. 105033.External Links:ISSN 0020-7462,DocumentCited by:§1,§2.
- [21]H. Richter(1949)Verzerrungstensor, verzerrungsdeviator und spannungstensor bei endlichen formänderungen.Z. angew. Math. Mech.29(3),pp. 65–75.Cited by:Definition 1.3.
- [22]P. Rosakis(1997)Characterization of convex isotropic functions.J. Elast.49,pp. 257–267.External Links:DocumentCited by:footnote 2.
- [23]J. Schröder, P. Neff, and D. Balzani(2005)A variational approach for materially stable anisotropic hyperelasticity.Int. J. Solids Struct.42(15),pp. 4352–4371.External Links:ISSN 00207683,DocumentCited by:§1.
- [24]C. Truesdell(1956)Das ungelöste Problem der endlichen Elastizitätstheorie.Z. angew. Math. Mech.36(3),pp. 97–103.Cited by:§1.
- [25]D. Wiedemann and M. A. Peter(2026)Characterization of polyconvex isotropic functions.Calc. Var.65,pp. 115.External Links:DocumentCited by:Theorem 1.5,§1,§2.
- [26]M. P. Wollner, G. A. Holzapfel, and P. Neff(2026)In search of constitutive conditions in isotropic hyperelasticity: polyconvexity versus true-stress-true-strain monotonicity.J. Mech. Phys. Solids209,pp. 106465.External Links:DocumentCited by:§1,§2,footnote 4.
- [27]M. P. Wollner, D. K. Klein, H. Baaser, G. A. Holzapfel, and P. Neff(2026)Concurrent enforcement of polyconvexity and true-stress-true-strain monotonicity in incompressible isotropic hyperelasticity: application to neural network constitutive models.Pre-print under review.External Links:2605.20031Cited by:2nd item,3rd item,Definition 1.3,§1,§3,footnote 3,footnote 6.
- [28]L. Zee and E. R. Sternberg(1983)Ordinary and strong ellipticity in the equilibrium theory of incompressible hyperelastic solids.Arch. Ration. Mech. Anal.83,pp. 53–90.External Links:DocumentCited by:§1.

## 


- 


Major funding support from
