# Non-injective field redefinitions and quantum inequivalence in scalar theories

**arXiv ID**: 2607.18166v1
**Authors**: Bin Zhu
**Published**: 2026-07-20
**Categories**: physics.gen-ph, hep-th
**Comments**: 16 pages
**HTML URL**: https://arxiv.org/html/2607.18166v1

## Abstract

We study scalar theories obtained by pulling a free massive multiplet back through a polynomial field redefinition with constant unit Jacobian. Our main example uses the three-variable noninjective map recently announced by Alpöge. After a linear normalization, it defines a three-scalar sigma model with a flat, unit-volume field-space metric and three isolated vacua. Each vacuum is locally described by three free modes of mass m, and the exact equations of motion reduce locally on each sheet to free Klein--Gordon equations. The global theory is nevertheless not a single free theory: the field-space metric is incomplete, the number of real preimages changes across target space, and the commuting position operators have nonconstant joint spectral multiplicity. This rules out a global unitary implementation of the field redefinition and a regular Weyl exponentiation of the formal canonical momenta. We then analyze a four-scalar map with a generic quintic fiber. It exhibits the same mechanism with an additional field that controls the fiber polynomial. The two examples separate perturbative equivalence on a chosen local sheet from global quantum equivalence of the full field space.

## Full Text

Non-injective field redefinitions and quantum inequivalence in scalar theories

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.18166v1 [physics.gen-ph] 20 Jul 2026††institutetext:School of Physics, Nankai University,
Weijin Road 94, Tianjin 300071, P.R. China

## Non-injective field redefinitions and quantum inequivalence in scalar theoriesBin Zhubzhu@nankai.edu.cn

## Abstract

We study scalar theories obtained by pulling a free massive
multiplet back through a polynomial field redefinition with constant unit
Jacobian. Our main example uses the three-variable noninjective map recently
announced by Alpöge. After a linear normalization, it defines a
three-scalar sigma model with a flat, unit-volume field-space metric and three
isolated vacua. Each vacuum is locally described by three free modes of massmm, and the exact equations of motion reduce locally on each sheet to free
Klein–Gordon equations. The global theory is nevertheless not a single
free theory: the field-space metric is incomplete, the number of real
preimages changes across target space, and the commuting position operators
have nonconstant joint spectral multiplicity. This rules out a global
unitary implementation of the field redefinition and a regular Weyl
exponentiation of the formal canonical momenta. We then analyze a
four-scalar map with a generic quintic fiber. It exhibits the same mechanism
with an additional field that controls the fiber polynomial. The two
examples separate perturbative equivalence on a chosen local sheet from
global quantum equivalence of the full field space.

## Keywords:Field Redefinitions, Canonical Quantization, Sigma Models,
Vacuum Structure

## 1Introduction

Field redefinitions are normally used as local changes of coordinates on
configuration space. When the transformation is invertible, the
equivalence theorem relates the on-shell descriptions obtained before and
after the change of variablesChisholm1961;Kamefuchi1961. Modern formulations make the assumptions
behind this statement explicit, including perturbative invertibility,
boundary conditions, and the choice of observablesCriadoPerezVictoria2019;CohenLuSutherland2024;CriadoJaeckelSpannowsky2025.
The present work asks what remains true when the Jacobian is nonsingular
everywhere but the transformation is not globally one-to-one.

The closest field-theory precedent is
ref.CriadoJaeckelSpannowsky2025, which explains how a non-one-to-one
field redefinition can change the field-space domain and the set of classical
solutions. Its representative examples pass through singular loci of the
field map. The models studied here instead have a nonsingular Jacobian at
every finite field value. The obstruction therefore comes from the
multiplicity of real preimages rather than a local singularity; no global
inverse is implied. The Jacobian conjecture has
also been formulated in perturbative and combinatorial quantum field theoryAbdesselam2003;Tanasa2021. Those works use field-theory methods to
organize formal inverse problems; here a real noninjective map is used as the
field-space transformation of a scalar theory.

This question can be studied without introducing a local Jacobian anomaly.
Letℱ:ℝn⟶ℝn,detJℱ=1,\mathcal{F}:\mathbb{R}^{n}\longrightarrow\mathbb{R}^{n},\qquad\det J_{\mathcal{F}}=1,(1)

be a polynomial local diffeomorphism for which some target values have more
than one real preimage. Throughout this paper, an inverse branch means a
local inverse𝒢s:𝒱→𝒰s\mathcal{G}_{s}:\mathcal{V}\to\mathcal{U}_{s}supplied by the inverse function
theorem on a specified target patch𝒱\mathcal{V}. No global single-valued
inverse ofℱ\mathcal{F}exists, and no such object is used below. Its
nonexistence is the source of the global effect studied here.
Pulling a free massive multiplet back throughℱ\mathcal{F}produces a
nonlinear sigma model. Its field-space metric is locally Euclidean and its
volume density is one. The derivative and potential interactions are
therefore removable around any chosen vacuum. They are not removable by one
global field coordinate if different points of the original field space are
mapped to the same free-field configuration.

Our simplest realization starts from the three-variable map announced by
AlpögeAlpoge2026Map. The announcement is an algebraic result: it
gives a polynomial map with constant Jacobian and an explicit three-point
fiber. It does not specify a scalar action, particle interpretation, or
equations of motion. We supply that physics construction here. A linear
normalization gives a unit-Jacobian mapℱ3\mathcal{F}_{3}, and the pullback of
three free massive scalars has three finite vacua. The equations of motion
are exactly free in the local variables𝒬I=ℱ3I​(φ)\mathcal{Q}^{I}=\mathcal{F}_{3}^{I}(\varphi), but the global Hilbert-space
representation retains the multiplicity of the different preimages.

The quantum distinction is already visible in the commuting position
operators. On one open target region their joint spectral multiplicity is
three, while on another it is one. A standard Schrödinger coordinate
tuple has multiplicity one, so no unitary operator can implement the
noninjective redefinition globally. The same variation prevents the formal
canonical momenta from exponentiating to a regular representation of the
Weyl relations. This is a global obstruction, not a failure of the local
commutators.

We then turn to a four-scalar map whose fibers are governed by a quintic
polynomial. The fourth field is not a passive coordinate: it enters the first
two output polynomials and controls the coefficients of the fiber equation.
The resulting model has the same local free-field description and the same
global multiplicity obstruction, but a different algebraic realization. A
generic-degree-five three-scalar slice of this family is useful for comparison
and is retained in
appendixA; it is not used as the primary example.

The paper is organized as follows. Section2sets up the pullback action and the global quantum diagnostic.
Section3constructs the three-scalar model from
the Alpöge map. Section4develops the four-scalar
example. Section5compares the two mechanisms, and
section6discusses their physical interpretation. The
generic-degree-five three-scalar slice is retained in the appendix as a
useful intermediate example.

## 2Non-injective field redefinitions

## 2.1Pulling back a free massive multiplet

We work first on a fixed Euclidean backgroundhμ​νh_{\mu\nu}. Letφa​(X)\varphi^{a}(X),a=1,…,na=1,\ldots,n, be dimensionless real scalar fields and
letℱI​(φ)\mathcal{F}^{I}(\varphi)be a polynomial map satisfying
eq. (1). The target variables𝒬I​(X)=ℱI​(φ​(X))\mathcal{Q}^{I}(X)=\mathcal{F}^{I}(\varphi(X))(2)

are good local coordinates at every finite field value. For a fixed target𝒬⋆\mathcal{Q}_{\star}, we considerSn​[φ]=fϕ22​∫dd​X​h​[hμ​ν​ga​b​(φ)​∂μφa​∂νφb+m2​|ℱ​(φ)−𝒬⋆|2],\begin{split}S_{n}[\varphi]=\frac{f_{\phi}^{2}}{2}\int\mathrm{d}^{d}X\,\sqrt{h}\,\big[h^{\mu\nu}g_{ab}(\varphi)\partial_{\mu}\varphi^{a}\partial_{\nu}\varphi^{b}+m^{2}\lvert\mathcal{F}(\varphi)-\mathcal{Q}_{\star}\rvert^{2}\big],\end{split}(3)

withga​b​(φ)=∂aℱI​∂bℱI=(Jℱ𝖳​Jℱ)a​b.g_{ab}(\varphi)=\partial_{a}\mathcal{F}^{I}\,\partial_{b}\mathcal{F}^{I}=(J_{\mathcal{F}}^{\mathsf{T}}J_{\mathcal{F}})_{ab}.(4)

Heremmis the physical mass andfϕf_{\phi}sets the field-space scale.
Inddspacetime dimensions,[fϕ]=(d−2)/2[f_{\phi}]=(d-2)/2and[m]=1[m]=1. The canonically dimensioned local
fluctuations areqI=fϕ​(𝒬I−𝒬⋆I)q^{I}=f_{\phi}(\mathcal{Q}^{I}-\mathcal{Q}_{\star}^{I}).
All integer and rational coefficients insideℱ\mathcal{F}are fixed
dimensionless interaction coefficients. Once the fields are canonically
normalized, nonlinear vertices are organized by inverse powers offϕf_{\phi}.

No spacetime curvature coupling is required for the construction.
Equation (3) is already minimally covariant on a fixed
curved background. We sethμ​ν=δμ​νh_{\mu\nu}=\delta_{\mu\nu}in the explicit
calculations below. Additional terms such asℛ​|ℱ−𝒬⋆|2\mathcal{R}\lvert\mathcal{F}-\mathcal{Q}_{\star}\rvert^{2}may be added, but
they define a different model and are not needed for the global effect.

On a target patch𝒱\mathcal{V}over which a local inverse𝒢s:𝒱→𝒰s\mathcal{G}_{s}:\mathcal{V}\to\mathcal{U}_{s}has been chosen,𝒬=ℱ​(φ)\mathcal{Q}=\mathcal{F}(\varphi)is a valid local field coordinate. On the
corresponding source patch𝒰s\mathcal{U}_{s}, the action becomesSn=fϕ22​∫dd​X​h​[hμ​ν​∂μ𝒬I​∂ν𝒬I+m2​(𝒬I−𝒬⋆I)2].S_{n}=\frac{f_{\phi}^{2}}{2}\int\mathrm{d}^{d}X\,\sqrt{h}\,\left[h^{\mu\nu}\partial_{\mu}\mathcal{Q}^{I}\partial_{\nu}\mathcal{Q}^{I}+m^{2}(\mathcal{Q}^{I}-\mathcal{Q}_{\star}^{I})^{2}\right].(5)

Thus the complicated derivative and potential interactions in theφ\varphivariables are redundant in perturbation theory around a fixed
local sheet. The metric is positive and flat, anddetg=(detJℱ)2=1.\det g=(\det J_{\mathcal{F}})^{2}=1.(6)

These local statements do not imply that the full field space is Euclidean.
If(ℝn,g)(\mathbb{R}^{n},g)were complete, the local isometryℱ:(ℝn,g)→(ℝn,δ)\mathcal{F}:(\mathbb{R}^{n},g)\to(\mathbb{R}^{n},\delta)would be a covering mapdoCarmo1992. Since the target is simply connected, the covering
would be one-to-one. Any explicit collision therefore shows that the
pullback metric is geodesically incomplete.

The field equations retain the same simple local form. Varying
eq. (3) gives(Jℱ)I​a​[−∇2𝒬I+m2​(𝒬I−𝒬⋆I)]=0.(J_{\mathcal{F}})_{Ia}\left[-\nabla^{2}\mathcal{Q}^{I}+m^{2}(\mathcal{Q}^{I}-\mathcal{Q}_{\star}^{I})\right]=0.(7)

The Jacobian matrix is invertible pointwise, so(−∇2+m2)​(𝒬I−𝒬⋆I)=0.(-\nabla^{2}+m^{2})(\mathcal{Q}^{I}-\mathcal{Q}_{\star}^{I})=0.(8)

No inverse map forℱ\mathcal{F}is used in this step; multiplication by the
pointwise matrix inverseJℱ−1J_{\mathcal{F}}^{-1}is sufficient.
Every finite critical point of the potential is a preimage of𝒬⋆\mathcal{Q}_{\star}. At such a pointvsv_{s},∂a∂bV|vs=fϕ2​m2​ga​b​(vs).\left.\partial_{a}\partial_{b}V\right|_{v_{s}}=f_{\phi}^{2}m^{2}g_{ab}(v_{s}).(9)

The kinetic matrix isfϕ2​ga​b​(vs)f_{\phi}^{2}g_{ab}(v_{s}), so all local normal modes have
massmm.

For the Euclidean boundary condition𝒬−𝒬⋆→0\mathcal{Q}-\mathcal{Q}_{\star}\to 0at infinity, multiplying
eq. (8) by𝒬−𝒬⋆\mathcal{Q}-\mathcal{Q}_{\star}and integrating gives∫dd​X​[∂μ𝒬I​∂μ𝒬I+m2​(𝒬I−𝒬⋆I)2]=0.\int\mathrm{d}^{d}X\,\left[\partial_{\mu}\mathcal{Q}^{I}\partial_{\mu}\mathcal{Q}^{I}+m^{2}(\mathcal{Q}^{I}-\mathcal{Q}_{\star}^{I})^{2}\right]=0.(10)

Ordinary smooth finite-action solutions are therefore the constant vacua.
In particular, the different finite preimages are not connected by a smooth
finite-energy wall. A transition between branches would have to probe an
incomplete end of field space, where an additional boundary prescription is
needed.

## 2.2Canonical variables and the global quantum test

The local canonical transformation follows directly from the cotangent
lift. For a field-space pointφ\varphiwith momentumπ\pi, define𝒬=ℱ​(φ),Π=Jℱ​(φ)−𝖳​π.\mathcal{Q}=\mathcal{F}(\varphi),\qquad\Pi=J_{\mathcal{F}}(\varphi)^{-\mathsf{T}}\pi.(11)

HereJℱ−𝖳J_{\mathcal{F}}^{-\mathsf{T}}is the inverse transpose of the Jacobian
matrix atφ\varphi, not the derivative of a global inverse map.
ThenΠI​d​𝒬I=πa​d​φa.\Pi_{I}\,\mathrm{d}\mathcal{Q}^{I}=\pi_{a}\,\mathrm{d}\varphi^{a}.(12)

The symplectic form is preserved on each local sheet. Distinct phase-space
points nevertheless map to the same(𝒬,Π)(\mathcal{Q},\Pi)wheneverℱ\mathcal{F}has several preimages.

The corresponding Schrödinger operators act onℋφ=L2​(ℝn,dn​φ)\mathcal{H}_{\varphi}=L^{2}(\mathbb{R}^{n},\mathrm{d}^{n}\varphi). On the common core𝒟=Cc∞​(ℝn)\mathcal{D}=C_{c}^{\infty}(\mathbb{R}^{n}), set𝒬^I=MℱI,Π^I=−i​ΔI,ΔI=(Jℱ−𝖳)I​a​∂a.\widehat{\mathcal{Q}}_{I}=M_{\mathcal{F}_{I}},\qquad\widehat{\Pi}_{I}=-\mathrm{i}\Delta_{I},\qquad\Delta_{I}=(J_{\mathcal{F}}^{-\mathsf{T}})_{Ia}\partial_{a}.(13)

The unit determinant makesJℱ−1J_{\mathcal{F}}^{-1}a polynomial matrix. With
the row convention(Jℱ)I​a=∂aℱI(J_{\mathcal{F}})_{Ia}=\partial_{a}\mathcal{F}_{I}, one has(Jℱ−1)a​I=(cof⁡Jℱ)I​adetJℱ=(cof⁡Jℱ)I​a.(J_{\mathcal{F}}^{-1})_{aI}=\frac{(\operatorname{cof}J_{\mathcal{F}})_{Ia}}{\det J_{\mathcal{F}}}=(\operatorname{cof}J_{\mathcal{F}})_{Ia}.(14)

The Piola identity then givesdiv⁡ΔI=∂a(cof⁡Jℱ)I​a=0,\operatorname{div}\Delta_{I}=\partial_{a}(\operatorname{cof}J_{\mathcal{F}})_{Ia}=0,(15)

so−i​ΔI-\mathrm{i}\Delta_{I}is symmetric on𝒟\mathcal{D}KupfermanShachar2019. The inverse Jacobian also givesΔI​ℱJ=(Jℱ−1)a​I​(Jℱ)J​a=δI​J.\Delta_{I}\mathcal{F}_{J}=(J_{\mathcal{F}}^{-1})_{aI}(J_{\mathcal{F}})_{Ja}=\delta_{IJ}.(16)

It follows that[ΔI,ΔJ][\Delta_{I},\Delta_{J}]annihilates everyℱK\mathcal{F}_{K}. Since the one-formsd​ℱK\mathrm{d}\mathcal{F}_{K}form a coframe,
the vector fields commute. Hence[𝒬^J,Π^I]=i​δI​J,[Π^I,Π^J]=0[\widehat{\mathcal{Q}}_{J},\widehat{\Pi}_{I}]=\mathrm{i}\delta_{IJ},\qquad[\widehat{\Pi}_{I},\widehat{\Pi}_{J}]=0(17)

on𝒟\mathcal{D}. These relations are formal. They do not imply essential
self-adjointness, complete momentum flows, or regular Weyl relations.

The global test uses the number of real preimages𝒩ℱ​(𝒬)=#​{φ∈ℝn:ℱ​(φ)=𝒬}.\mathcal{N}_{\mathcal{F}}(\mathcal{Q})=\#\{\varphi\in\mathbb{R}^{n}:\mathcal{F}(\varphi)=\mathcal{Q}\}.(18)

At a regular target value, this is equivalently the number of local inverse
branches above that value.
The area formula gives, for integrable test functions,∫ℝnr​(ℱ​(φ))​dn​φ=∫ℝn𝒩ℱ​(𝒬)​r​(𝒬)​dn​𝒬\int_{\mathbb{R}^{n}}r(\mathcal{F}(\varphi))\,\mathrm{d}^{n}\varphi=\int_{\mathbb{R}^{n}}\mathcal{N}_{\mathcal{F}}(\mathcal{Q})r(\mathcal{Q})\,\mathrm{d}^{n}\mathcal{Q}(19)

EvansGariepy2015. Correspondingly,L2​(ℝφn)≃∫ℝ𝒬n⊕ℂ𝒩ℱ​(𝒬)​dn​𝒬.L^{2}(\mathbb{R}^{n}_{\varphi})\simeq\int_{\mathbb{R}^{n}_{\mathcal{Q}}}^{\oplus}\mathbb{C}^{\mathcal{N}_{\mathcal{F}}(\mathcal{Q})}\,\mathrm{d}^{n}\mathcal{Q}.(20)

The usual coordinate tuple has joint spectral multiplicity one. If𝒩ℱ\mathcal{N}_{\mathcal{F}}equals three on one open set and one on another,
the tupleMℱIM_{\mathcal{F}_{I}}cannot be related to the usual coordinates by
a unitary operator. A regular representation of the finite-dimensional
Weyl relations also has constant spectral multiplicity, as follows from the
Stone–von Neumann classificationFolland1989. Nonconstant𝒩ℱ\mathcal{N}_{\mathcal{F}}therefore obstructs regular exponentiation even
though eq. (17) holds locally.

## 3Three scalar fields from the Alpöge map

## 3.1The map and our conventions

The input from ref.Alpoge2026Mapis a polynomial map, not a
three-dimensional spacetime model. We use it as a map of field space and
place the resulting scalar fields on add-dimensional Euclidean
background. This distinction is summarized in
table1.Alpöge announcementPresent paperInterpretation(x,y,z)∈ℝ3(x,y,z)\in\mathbb{R}^{3}φa​(X)=(x​(X),y​(X),z​(X))\varphi^{a}(X)=(x(X),y(X),z(X))Dimensionless field-space coordinates promoted to three real scalar fields(A,B,C)(A,B,C)ℱ3=(−A/2,B,C)\mathcal{F}_{3}=(-A/2,B,C)Linear output normalization used to set the Jacobian to+1+1detJ(A,B,C)=−2\det J_{(A,B,C)}=-2detJℱ3=1\det J_{\mathcal{F}_{3}}=1The local functional measure has unit density(−1/4,0,0)(-1/4,0,0)𝒬⋆(3)=(1/8,0,0)\mathcal{Q}_{\star}^{(3)}=(1/8,0,0)The target around which the massive potential is centeredWeighted algebraic scalingFixed coefficients in the scalar actionThe scaling is not a continuous symmetry of the massive shifted theoryTable 1:Dictionary between the announced algebraic map and the
three-scalar model used here.

Writes=1+x​ys=1+xy. The announced mapℒ=(A,B,C)\mathcal{L}=(A,B,C)isA\displaystyle A=s3​z+y2​s​(4+3​x​y),\displaystyle=s^{3}z+y^{2}s(4+3xy),(21)B\displaystyle B=y+3​x​s2​z+3​x​y2​(4+3​x​y),\displaystyle=y+3xs^{2}z+3xy^{2}(4+3xy),(22)C\displaystyle C=2​x−3​x2​y−x3​z.\displaystyle=2x-3x^{2}y-x^{3}z.(23)

Its Jacobian is−2-2. We normalize the first target coordinate and useℱ3​(x,y,z)=(−A2,B,C),detJℱ3=1.\mathcal{F}_{3}(x,y,z)=\left(-\frac{A}{2},B,C\right),\qquad\det J_{\mathcal{F}_{3}}=1.(24)

The three pointsv0=(0,0,−14),v+=(1,−32,132),v−=(−1,32,132)v_{0}=\left(0,0,-\frac{1}{4}\right),\qquad v_{+}=\left(1,-\frac{3}{2},\frac{13}{2}\right),\qquad v_{-}=\left(-1,\frac{3}{2},\frac{13}{2}\right)(25)

all map to𝒬⋆(3)=(18,0,0).\mathcal{Q}_{\star}^{(3)}=\left(\frac{1}{8},0,0\right).(26)

Since the Jacobian is nonzero at all three points, the inverse function
theorem gives disjoint source neighborhoods𝒰s∋vs\mathcal{U}_{s}\ni v_{s}and a common target neighborhood𝒱⋆(3)∋𝒬⋆(3)\mathcal{V}_{\star}^{(3)}\ni\mathcal{Q}_{\star}^{(3)}such that each restrictionℱ3|𝒰s\mathcal{F}_{3}|_{\mathcal{U}_{s}}is a diffeomorphism onto𝒱⋆(3)\mathcal{V}_{\star}^{(3)}. We denote its local inverse by𝒢s=(ℱ3|𝒰s)−1\mathcal{G}_{s}=(\mathcal{F}_{3}|_{\mathcal{U}_{s}})^{-1}. These three maps are
the local inverse branches. They cannot be combined into a global
single-valued inverse because𝒢s​(𝒬⋆(3))=vs\mathcal{G}_{s}(\mathcal{Q}_{\star}^{(3)})=v_{s}gives three different values.

The fiber equation is controlled by a cubic. For the unnormalized target(A,B,C)(A,B,C), introducePA,B,C​(T)=C​T3−2​T2+B​T−2​A.P_{A,B,C}(T)=CT^{3}-2T^{2}+BT-2A.(27)

On the chartx≠0x\neq 0,t=y+1/xt=y+1/xsatisfiesPA,B,C​(t)=0,PA,B,C′​(t)=2x.P_{A,B,C}(t)=0,\qquad P^{\prime}_{A,B,C}(t)=\frac{2}{x}.(28)

To see the reconstruction directly, substitution givesB=4​t+2x−3​C​t2,2​A=C​t3−2​t2+B​t.B=4t+\frac{2}{x}-3Ct^{2},\qquad 2A=Ct^{3}-2t^{2}+Bt.(29)

For a simple rootτ\tau, letρ=PA,B,C′​(τ)\rho=P^{\prime}_{A,B,C}(\tau). The corresponding source point isx=2ρ,y=τ−ρ2,z=54​ρ2−32​τ​ρ−C8​ρ3.x=\frac{2}{\rho},\qquad y=\tau-\frac{\rho}{2},\qquad z=\frac{5}{4}\rho^{2}-\frac{3}{2}\tau\rho-\frac{C}{8}\rho^{3}.(30)

Thus a generic target has three complex preimagesDorkyCubic2026.

The vacuum target requires one small qualification. HereC=0C=0, so the
leading cubic coefficient vanishes and thex=0x=0chart must be retained.
On that chart,B=C=0B=C=0impliesy=0y=0, whileA=−1/4A=-1/4fixesz=−1/4z=-1/4, givingv0v_{0}. On thex≠0x\neq 0chart the remaining fiber
equation is−2​T2+12=0.-2T^{2}+\frac{1}{2}=0.(31)

Its two roots reconstructv±v_{\pm}. This verifies that the three points in
eq. (25) exhaust the finite real fiber over𝒬⋆(3)\mathcal{Q}_{\star}^{(3)}.

For the quantum argument we also need a target with one real preimage.
Choose the unnormalized value(A,B,C)=(1,3,1)(A,B,C)=(1,3,1), corresponding to𝒬0(3)=(−12,3,1).\mathcal{Q}_{0}^{(3)}=\left(-\frac{1}{2},3,1\right).(32)

The fiber polynomial becomesP0(3)​(T)=T3−2​T2+3​T−2=(T−1)​(T2−T+2).P_{0}^{(3)}(T)=T^{3}-2T^{2}+3T-2=(T-1)(T^{2}-T+2).(33)

It has one real root and the exact preimageℱ3​(1,0,1)=𝒬0(3).\mathcal{F}_{3}(1,0,1)=\mathcal{Q}_{0}^{(3)}.(34)

Indeed,T=1T=1hasP0(3)⁣′​(1)=2P_{0}^{(3)\prime}(1)=2, and
eq. (30) immediately gives(x,y,z)=(1,0,1)(x,y,z)=(1,0,1).
The nonreal pair stays nonreal under a small target perturbation, so a
neighborhood𝒱0(3)\mathcal{V}_{0}^{(3)}has one real sheet.

## 3.2The three-scalar action

Substituting eqs. (21)–(23) into the general
construction gives the complete interacting actionS3=fϕ22∫ddX{14​(∂μA)2+(∂μB)2+(∂μC)2+m2[(−A2−18)2+B2+C2]}.\begin{split}S_{3}=\frac{f_{\phi}^{2}}{2}\int\mathrm{d}^{d}X\,\bigg\{&\frac{1}{4}(\partial_{\mu}A)^{2}+(\partial_{\mu}B)^{2}+(\partial_{\mu}C)^{2}\\
&+m^{2}\left[\left(-\frac{A}{2}-\frac{1}{8}\right)^{2}+B^{2}+C^{2}\right]\bigg\}.\end{split}(35)

The derivative interactions come from the three polynomial composites(A,B,C)(A,B,C). The potential contains the corresponding nonderivative
interactions. Their relative coefficients are fixed by the unit-Jacobian
map; the independent physical parameters of this minimal model arefϕf_{\phi}andmm.

The original fields do not represent three decoupled particle species.
They are nonlinear coordinates on one flat target field space. Algebraically,x​yxycontrols the shape variabless,xxsets the scale that appears in
the reconstruction relationP′​(t)=2/xP^{\prime}(t)=2/x, andzzsupplies the direction
that is linear in the map. The propagating normal modes near a vacuum are
the three combinationsqI=fϕ​[ℱ3I​(φ)−𝒬⋆(3)​I],q^{I}=f_{\phi}\left[\mathcal{F}_{3}^{I}(\varphi)-\mathcal{Q}_{\star}^{(3)I}\right],(36)

notx,y,zx,y,zseparately.

The algebraic map is covariant under(x,y,z)⟶(λ​x,λ−1​y,λ−2​z),(A,B,C)⟶(λ−2​A,λ−1​B,λ​C).(x,y,z)\longrightarrow(\lambda x,\lambda^{-1}y,\lambda^{-2}z),\qquad(A,B,C)\longrightarrow(\lambda^{-2}A,\lambda^{-1}B,\lambda C).(37)

The Euclidean target metric and the shifted massive potential break this
continuous scaling. Theλ=−1\lambda=-1transformation remains an exactℤ2\mathbb{Z}_{2}symmetry:(x,y,z)⟶(−x,−y,z),(A,B,C)⟶(A,−B,−C).(x,y,z)\longrightarrow(-x,-y,z),\qquad(A,B,C)\longrightarrow(A,-B,-C).(38)

It fixesv0v_{0}and exchangesv+v_{+}withv−v_{-}.

The action has exactly the three vacua in
eq. (25). Atv0v_{0}, for example,Jℱ3​(v0)=(00−1/2−3/410200),g(3)​(v0)=(73/16−3/40−3/410001/4),J_{\mathcal{F}_{3}}(v_{0})=\begin{pmatrix}0&0&-1/2\\
-3/4&1&0\\
2&0&0\end{pmatrix},\qquad g^{(3)}(v_{0})=\begin{pmatrix}73/16&-3/4&0\\
-3/4&1&0\\
0&0&1/4\end{pmatrix},(39)

anddetg(3)​(v0)=1\det g^{(3)}(v_{0})=1. Equation
(9) then gives three modes of massmm.
The same conclusion holds atv±v_{\pm}, despite the less diagonal coordinate
matrices there.

The exact equations of motion are(−∂2+m2)​[ℱ3I​(φ)−𝒬⋆(3)​I]=0.(-\partial^{2}+m^{2})\left[\mathcal{F}_{3}^{I}(\varphi)-\mathcal{Q}_{\star}^{(3)I}\right]=0.(40)

Small Lorentzian excitations are therefore ordinary massive waves on each
local sheet. With Euclidean finite-action boundary conditions, the only
smooth solutions are the three constant vacua. The model has no smooth
finite-energy wall connecting them at finite field values.

## 3.3Global quantum structure

The three vacua have the same local perturbative physics, but they do not
collapse to one global Schrödinger representation. On𝒱⋆(3)\mathcal{V}_{\star}^{(3)}, the position tupleMℱ3IM_{\mathcal{F}_{3}^{I}}has joint spectral multiplicity three. On𝒱0(3)\mathcal{V}_{0}^{(3)}, it has multiplicity one. Therefore no unitary
operator onL2​(ℝ3)L^{2}(\mathbb{R}^{3})can satisfyU​MφI​U−1=Mℱ3I​(φ)(I=1,2,3).UM_{\varphi^{I}}U^{-1}=M_{\mathcal{F}_{3}^{I}(\varphi)}\qquad(I=1,2,3).(41)

The same variation in multiplicity rules out strongly continuous momentum
groups satisfying the Weyl relations with these position operators.

This statement does not modify the branchwise equivalence theorem. On each
sheet, the formal momentaΠ^I=−i​(Jℱ3−𝖳)I​a​∂a\widehat{\Pi}_{I}=-\mathrm{i}(J_{\mathcal{F}_{3}}^{-\mathsf{T}})_{Ia}\partial_{a}(42)

are symmetric onCc∞​(ℝ3)C_{c}^{\infty}(\mathbb{R}^{3})and satisfy the canonical commutators.
The obstruction appears only when one asks for a single self-adjoint,
regular, global realization that covers both the one-sheeted and
three-sheeted target regions.

## 4A four-scalar model

## 4.1The polynomial map and its fibers

We now promote the constant parameter in the Jacobian-neutral rational frame
of ref.DorkyFamily2026to a fourth scalarww, producing a map
whose generic fiber is quintic. An independent weighted-lift construction
realizing every generic fiber degree at least three was given in
ref.Gallagher2026. Defineσ=1+x​y,u=σ​(1−x2​z),η=y−x​z−x2​y​z,\sigma=1+xy,\qquad u=\sigma(1-x^{2}z),\qquad\eta=y-xz-x^{2}yz,(43)

so thatu=1+x​ηu=1+x\eta, and seta=\displaystyle a={}σ​(y2−σ2​z)+12​σ2​η2​(9+w−4​w​u),\displaystyle\sigma(y^{2}-\sigma^{2}z)+\frac{1}{2}\sigma^{2}\eta^{2}(9+w-4wu),(44)b=\displaystyle b={}−2​y+x​σ​η2​(12+2​w−5​w​u),\displaystyle-2y+x\sigma\eta^{2}(12+2w-5wu),(45)c=\displaystyle c={}x−x3​z.\displaystyle x-x^{3}z.(46)

The unnormalized and normalized maps areG4=(a,b,c,w),ℱ4=(−a2,b,c,w).G_{4}=(a,b,c,w),\qquad\mathcal{F}_{4}=\left(-\frac{a}{2},b,c,w\right).(47)

A direct calculation givesdetJG4=−2,detJℱ4=1.\det J_{G_{4}}=-2,\qquad\det J_{\mathcal{F}_{4}}=1.(48)

The constant determinant is transparent in a rational frame. Onx≠0x\neq 0introducet=y+1x,r=2x,gW​(U)=−3​U2+8​U−5+W​(U−1)3,t=y+\frac{1}{x},\qquad r=\frac{2}{x},\qquad g_{W}(U)=-3U^{2}+8U-5+W(U-1)^{3},(49)

andh​(T,C,W)=T2​gW​(C​T)h(T,C,W)=T^{2}g_{W}(CT). Substitution givesb=r−∂Th​(t,c,w),2​a=h​(t,c,w)+t​b.b=r-\partial_{T}h(t,c,w),\qquad 2a=h(t,c,w)+tb.(50)

The two Jacobian factors arer/2r/2and−2​x-2x, whose product is−2-2. Since the final expressions are polynomial, the identity extends
throughx=0x=0.

For a target(A,B,C,W)(A,B,C,W)ofG4G_{4}, the fiber polynomial isPA,B,C,W​(T)=h​(T,C,W)+B​T−2​A.P_{A,B,C,W}(T)=h(T,C,W)+BT-2A.(51)

At a preimage,P​(t)=0,P′​(t)=2x.P(t)=0,\qquad P^{\prime}(t)=\frac{2}{x}.(52)

A simple rootτ\tau, withρ=P′​(τ)\rho=P^{\prime}(\tau), reconstructsx=2ρ,y=τ−ρ2,z=x−Cx3,w=W.x=\frac{2}{\rho},\qquad y=\tau-\frac{\rho}{2},\qquad z=\frac{x-C}{x^{3}},\qquad w=W.(53)

ForC​W≠0CW\neq 0, the fiber equation is generically of degree five.

The normalized target𝒬⋆(4)=(−4,16,1,−3)\mathcal{Q}_{\star}^{(4)}=(-4,16,1,-3)(54)

corresponds to(A,B,C,W)=(8,16,1,−3)(A,B,C,W)=(8,16,1,-3). Its fiber polynomial factors asP⋆(4)​(T)=−3​T5+6​T4−T3−2​T2+16​T−16=−(T−1)​(T−2)​(3​T3+3​T2+4​T+8).\begin{split}P_{\star}^{(4)}(T)&=-3T^{5}+6T^{4}-T^{3}-2T^{2}+16T-16\\
&=-(T-1)(T-2)(3T^{3}+3T^{2}+4T+8).\end{split}(55)

The cubic factor is strictly increasing because its derivative is9​T2+6​T+4>09T^{2}+6T+4>0. The fiber therefore contains three real points and one
nonreal conjugate pair. Two real preimages areq1=(19,−8,−648,−3),q2=(−126,28,18252,−3).q_{1}=\left(\frac{1}{9},-8,-648,-3\right),\qquad q_{2}=\left(-\frac{1}{26},28,18252,-3\right).(56)

These points follow fromP⋆(4)′​(1)=18,P⋆(4)′​(2)=−52.{P_{\star}^{(4)}}^{\prime}(1)=18,\qquad{P_{\star}^{(4)}}^{\prime}(2)=-52.(57)

The third real root is the unique solutionα≃−1.403615886831572\alpha\simeq-1.403615886831572of3​α3+3​α2+4​α+8=0.3\alpha^{3}+3\alpha^{2}+4\alpha+8=0.(58)

Writingx3=2/P⋆(4)′​(α)x_{3}=2/{P_{\star}^{(4)}}^{\prime}(\alpha), its preimage isq3=(x3,α−P⋆(4)′​(α)2,x3−1x33,−3).q_{3}=\left(x_{3},\,\alpha-\frac{{P_{\star}^{(4)}}^{\prime}(\alpha)}{2},\,\frac{x_{3}-1}{x_{3}^{3}},\,-3\right).(59)

All five roots are simple, so the three real preimages extend to a common
three-sheeted target neighborhood𝒱⋆(4)\mathcal{V}_{\star}^{(4)}.

The comparison target𝒬0(4)=(0,6,1,1)\mathcal{Q}_{0}^{(4)}=(0,6,1,1)(60)

has the unique real preimageq0=(13,−3,−18,1).q_{0}=\left(\frac{1}{3},-3,-18,1\right).(61)

For this target the fiber polynomial isP0(4)​(T)=T5−6​T4+11​T3−6​T2+6​T.P_{0}^{(4)}(T)=T^{5}-6T^{4}+11T^{3}-6T^{2}+6T.(62)

Its derivative obeysP0(4)′​(T)=5​T4−24​T3+33​T2−12​T+6=5​(T2−125​T+310)2+65​(T−2)2+34>0.\begin{split}{P_{0}^{(4)}}^{\prime}(T)&=5T^{4}-24T^{3}+33T^{2}-12T+6\\
&=5\left(T^{2}-\frac{12}{5}T+\frac{3}{10}\right)^{2}+\frac{6}{5}(T-2)^{2}+\frac{3}{4}>0.\end{split}(63)

Strict positivity persists under a small target perturbation, giving an open
one-sheeted neighborhood𝒱0(4)\mathcal{V}_{0}^{(4)}.

## 4.2Four fields and the extra coordinate

The four-scalar action is then=4n=4case of
eq. (3),S4=fϕ22​∫dd​X​[(Jℱ4𝖳​Jℱ4)a​b​∂μϕa​∂μϕb+m2​|ℱ4​(ϕ)−𝒬⋆(4)|2],\begin{split}S_{4}=\frac{f_{\phi}^{2}}{2}\int\mathrm{d}^{d}X\,\big[(J_{\mathcal{F}_{4}}^{\mathsf{T}}J_{\mathcal{F}_{4}})_{ab}\partial_{\mu}\phi^{a}\partial_{\mu}\phi^{b}+m^{2}\lvert\mathcal{F}_{4}(\phi)-\mathcal{Q}_{\star}^{(4)}\rvert^{2}\big],\end{split}(64)

whereϕ=(x,y,z,w)\phi=(x,y,z,w). The fourth output isww, butwwalso
appears inaaandbb. It is therefore not a decoupled spectator.
Changing its target value changesgWg_{W}and hence the quintic fiber
polynomial seen by the other three fields.

The potential has exactly three real vacua over𝒬⋆(4)\mathcal{Q}_{\star}^{(4)}. Near each one, the four combinationsqI=fϕ​[ℱ4I​(ϕ)−𝒬⋆(4)​I]q^{I}=f_{\phi}\left[\mathcal{F}_{4}^{I}(\phi)-\mathcal{Q}_{\star}^{(4)I}\right](65)

are free fields of massmm. The exact equations are(−∂2+m2)​[ℱ4I​(ϕ)−𝒬⋆(4)​I]=0.(-\partial^{2}+m^{2})\left[\mathcal{F}_{4}^{I}(\phi)-\mathcal{Q}_{\star}^{(4)I}\right]=0.(66)

The field-space metric is flat with unit determinant but incomplete, as the
three-point fiber makes global completeness impossible.

The quantum result follows without a new operator calculation. The
position tuple has multiplicity three on𝒱⋆(4)\mathcal{V}_{\star}^{(4)}and one on𝒱0(4)\mathcal{V}_{0}^{(4)}. It is not unitarily equivalent to the ordinary
four-coordinate Schrödinger tuple, and the formal momenta cannot generate
a regular Weyl representation with these positions. The fourth field
changes the algebraic family but not the spectral mechanism.

The invariant hyperplanew=−3w=-3gives a separate three-scalar map of
generic degree five. It retains useful exact information about the
four-field family, including the same three real vacua, and coincides with
the explicit generic-degree-five member of the three-variable family in
ref.DorkyFamily2026. Because it is not the minimal three-scalar
example, we keep the calculation in appendixA.

## 5Comparing the three- and four-scalar models

The two examples are summarized in table2. Their
polynomial degrees and target values differ, but their physical
interpretation is the same.ModelGeneric complex fiberThree-sheet targetOne-sheet targetℱ3\mathcal{F}_{3}33(1/8,0,0)(1/8,0,0)(−1/2,3,1)(-1/2,3,1)ℱ4\mathcal{F}_{4}55(−4,16,1,−3)(-4,16,1,-3)(0,6,1,1)(0,6,1,1)Table 2:Algebraic data used to diagnose the global quantum structure. The
sheet numbers in the last two columns count real preimages, equivalently
local inverse branches, on small open neighborhoods of the displayed targets.

Three ingredients are common. First,detJℱ=1\det J_{\mathcal{F}}=1removes any
local measure density and makes the formal momenta symmetric through the
Piola identity. Second, the map is nonproper. Real branches can escape to
field-space infinity while their images remain finite, so the number of
real preimages can change without a critical point. Third, the
pullback metric is flat but incomplete. The same incomplete end appears
geometrically in the sigma model and spectrally in the failure of complete
momentum flows.

The area formula also explains the branch factor in the functional
integral. If a connected spacetime configuration is restricted to a commonkk-sheeted target neighborhood, continuity makes the local-sheet label
constant on spacetime. The smooth branch-restricted path integral is then a
sum ofkkidentical free sectors, not a local factor independently chosen
at every spacetime point. A global path integral must additionally specify
what happens when fields approach the incomplete ends.

The pullback operator makes the surviving global relation explicit:Cℱ:L2​(ℝ𝒬n)⟶L2​(ℝφn),(Cℱ​ψ)​(φ)=ψ​(ℱ​(φ)).C_{\mathcal{F}}:L^{2}(\mathbb{R}^{n}_{\mathcal{Q}})\longrightarrow L^{2}(\mathbb{R}^{n}_{\varphi}),\qquad(C_{\mathcal{F}}\psi)(\varphi)=\psi(\mathcal{F}(\varphi)).(67)

The area formula givesCℱ†​Cℱ=M𝒩ℱ.C_{\mathcal{F}}^{\dagger}C_{\mathcal{F}}=M_{\mathcal{N}_{\mathcal{F}}}.(68)

On a three-sheeted region its range is the diagonal subspace(ψ,ψ,ψ)(\psi,\psi,\psi)of the multiplicity-three spectral fiber. The operator
is an intertwiner, but it is neither onto nor unitary.

The additionalwwfield inℱ4\mathcal{F}_{4}changes the fiber polynomial
from cubic to quintic and promotes a coefficient of the three-variable
family to a dynamical field. It does not remove the branchwise free
description. This comparison indicates that the quantum obstruction is
controlled by preimage multiplicity rather than by the number of
fields or the degree of a particular polynomial presentation.

## 6Discussion and outlook

The three-scalar model provides the shortest physical realization of the
global issue. Its local Lagrangian looks highly interacting in the(x,y,z)(x,y,z)coordinates, yet every perturbative sector is exactly a free
massive triplet. The nontrivial information lies in the way the local
coordinate patches fit together. Three finite vacua are three preimages of
the same target configuration, each defining a local inverse branch, and the
preimage count changes elsewhere in target space.

This does not conflict with the equivalence theorem. That theorem applies
after one chooses an invertible local redefinition and compatible
asymptotic data. It does not identify several distinct local inverse
branches with a single field coordinate. Likewise, the formal canonical
commutators are correct on their test-function domain. Their global
exponentiation fails because a regular Weyl representation cannot carry a
position tuple whose spectral multiplicity changes from one open set to
another.

The four-scalar model shows that the same physics survives when the fiber
equation is quintic and one coefficient becomes a field. Thew=−3w=-3slice
in appendixAprovides a useful intermediate
example, but the Alpöge map remains the simpler starting point for the
three-scalar theory.

Several questions require additional input rather than further local
algebra. A nonperturbative path integral must choose boundary conditions at
the incomplete ends of field space. Observables may be restricted to be
branch-blind, or the local-sheet label may be treated as additional global
data. Interacting target potentialsV​(𝒬)V(\mathcal{Q})can also be pulled
back, preserving the same local geometry while changing the spectrum and
classical solutions. These choices determine a quantum completion; the
unit Jacobian alone does not.

## Appendix AA generic-degree-five three-scalar slice

This appendix retains the former three-scalar specialization of the
four-field map. It is the invariant slicew=−3w=-3, and the resulting
generic-degree-five map is the explicit degree-five member of the public
construction in ref.DorkyFamily2026. The example is useful because
its three real vacua coincide with the first three coordinates of the
four-field vacua and because all relevant spectral statements can be checked
within three variables.

Definef5:ℝ3⟶ℝ3,f5​(x,y,z)=(−a52,b5,c5),f_{5}:\mathbb{R}^{3}\longrightarrow\mathbb{R}^{3},\qquad f_{5}(x,y,z)=\left(-\frac{a_{5}}{2},b_{5},c_{5}\right),(69)

whereσ,u,η\sigma,u,\etaare given in
eq. (43) anda5\displaystyle a_{5}=σ​(y2−σ2​z)+3​σ2​η2​(1+2​u),\displaystyle=\sigma(y^{2}-\sigma^{2}z)+3\sigma^{2}\eta^{2}(1+2u),(70)b5\displaystyle b_{5}=−2​y+3​x​σ​η2​(2+5​u),\displaystyle=-2y+3x\sigma\eta^{2}(2+5u),(71)c5\displaystyle c_{5}=x−x3​z.\displaystyle=x-x^{3}z.(72)

The block form ofJℱ4J_{\mathcal{F}_{4}}at fixedwwgivesdetJf5=1.\det J_{f_{5}}=1.(73)

For the targetq⋆(5)=(−4,16,1),q_{\star}^{(5)}=(-4,16,1),(74)

the fiber polynomial isP⋆(4)​(T)P_{\star}^{(4)}(T)in
eq. (55). Its three real preimages arev1(5)\displaystyle v_{1}^{(5)}=(19,−8,−648),\displaystyle=\left(\frac{1}{9},-8,-648\right),v2(5)\displaystyle v_{2}^{(5)}=(−126,28,18252),\displaystyle=\left(-\frac{1}{26},28,18252\right),(75)v3(5)\displaystyle v_{3}^{(5)}=(xα,α−ρα2,xα−1xα3),\displaystyle=\left(x_{\alpha},\alpha-\frac{\rho_{\alpha}}{2},\frac{x_{\alpha}-1}{x_{\alpha}^{3}}\right),xα\displaystyle x_{\alpha}=2ρα,ρα=P⋆(4)′​(α).\displaystyle=\frac{2}{\rho_{\alpha}},\qquad\rho_{\alpha}={P_{\star}^{(4)}}^{\prime}(\alpha).(76)

Numerically,v3(5)≃(−0.0183679739102,53.0389701539,164331.557504).v_{3}^{(5)}\simeq(-0.0183679739102,\,53.0389701539,\,164331.557504).(77)

The associated scalar model isS3,5=fϕ22​∫dd​X​[(Jf5𝖳​Jf5)a​b​∂μφa​∂μφb+m2​|f5​(φ)−q⋆(5)|2].S_{3,5}=\frac{f_{\phi}^{2}}{2}\int\mathrm{d}^{d}X\left[(J_{f_{5}}^{\mathsf{T}}J_{f_{5}})_{ab}\partial_{\mu}\varphi^{a}\partial_{\mu}\varphi^{b}+m^{2}\lvert f_{5}(\varphi)-q_{\star}^{(5)}\rvert^{2}\right].(78)

Its metric is positive and flat with unit determinant. The three points in
eqs. (75) and
(76) are its three vacua, and all local modes
have massmm.

At the first rational vacuum,Jf5​(v1(5))=(352−41/14580−20250−1/729),J_{f_{5}}(v_{1}^{(5)})=\begin{pmatrix}352&-4&1/1458\\
0&-2&0\\
25&0&-1/729\end{pmatrix},(79)

sog(5)​(v1(5))=(124529−1408151/729−140820−2/729151/729−2/7295/2125764),detg(5)​(v1(5))=1.g^{(5)}(v_{1}^{(5)})=\begin{pmatrix}124529&-1408&151/729\\
-1408&20&-2/729\\
151/729&-2/729&5/2125764\end{pmatrix},\qquad\det g^{(5)}(v_{1}^{(5)})=1.(80)

The anisotropic coordinate entries do not affect the physical masses,
becausef5−q⋆(5)f_{5}-q_{\star}^{(5)}supplies local normal coordinates.

The real spectral multiplicity also varies in this slice. Takeq0(5)=(0,13,−1).q_{0}^{(5)}=(0,13,-1).(81)

The corresponding fiber polynomial and derivative areP0(5)​(T)\displaystyle P_{0}^{(5)}(T)=3​T5+6​T4+T3−2​T2+13​T,\displaystyle=3T^{5}+6T^{4}+T^{3}-2T^{2}+13T,(82)P0(5)′​(T)\displaystyle{P_{0}^{(5)}}^{\prime}(T)=15​T4+24​T3+3​T2−4​T+13.\displaystyle=15T^{4}+24T^{3}+3T^{2}-4T+13.(83)

Using24​T3≥−12​T4−12​T224T^{3}\geq-12T^{4}-12T^{2}and4​|T|≤T2+44\lvert T\rvert\leq T^{2}+4, one findsP0(5)′​(T)≥3​T4−10​T2+9=3​(T2−53)2+23>0.{P_{0}^{(5)}}^{\prime}(T)\geq 3T^{4}-10T^{2}+9=3\left(T^{2}-\frac{5}{3}\right)^{2}+\frac{2}{3}>0.(84)

The unique real rootT=0T=0givesf5​(213,−132,25358)=q0(5).f_{5}\left(\frac{2}{13},-\frac{13}{2},\frac{2535}{8}\right)=q_{0}^{(5)}.(85)

Consequently the same multiplicity-three versus multiplicity-one quantum
obstruction occurs for this degree-five slice.

## Acknowledgements.OpenAI Codex was used to assist with algebraic exploration, literature
searches, drafting, and typesetting. BZ is supported by the Fundamental
Research Funds for the Central Universities (010-63263123).

## References
- (1)J. S. R. Chisholm,Change of variables in quantum field theories,Nucl. Phys.26(1961) 469–479.
- (2)S. Kamefuchi, L. O’Raifeartaigh, and A. Salam,Change of variables and
equivalence theorems in quantum field theories,Nucl. Phys.28(1961) 529–549.
- (3)J. C. Criado and M. Pérez-Victoria,Field redefinitions in effective
theories at higher orders,JHEP03(2019) 038,
[arXiv:1811.09413].
- (4)T. Cohen, X. Lu, and D. Sutherland,On amplitudes and field
redefinitions,JHEP06(2024) 149,
[arXiv:2312.06748].
- (5)J. C. Criado, J. Jaeckel, and M. Spannowsky,Field redefinitions in
classical field theory with some quantum perspectives,Phys. Rev. D111(2025), no. 7 076019, [arXiv:2408.03369].
- (6)A. Abdesselam,The Jacobian conjecture as a problem of perturbative
quantum field theory,Ann. Henri Poincaré4(2003) 199–215,
[math/0208173].
- (7)A. Tanasa,Combinatorial quantum field theory and the Jacobian
conjecture, inTranscendence in Algebra, Combinatorics, Geometry and
Number Theory, vol. 373 ofSpringer Proceedings in Mathematics &
Statistics, pp. 249–259.Springer, 2021.arXiv:2002.07453.
- (8)L. Alpöge, “Announcement of an explicit three-dimensional counterexample
to the Jacobian conjecture.”X post, 2026.Posted July 20, 2026.
- (9)M. P. do Carmo,Riemannian Geometry.Birkhäuser, Boston, 1992.
- (10)R. Kupferman and A. Shachar,A geometric perspective on the Piola
identity in Riemannian settings,J. Geom. Mech.11(2019),
no. 1 59–76, [arXiv:1805.12365].
- (11)L. C. Evans and R. F. Gariepy,Measure Theory and Fine Properties of
Functions.CRC Press, Boca Raton, revised edition ed., 2015.
- (12)G. B. Folland,Harmonic Analysis in Phase Space, vol. 122 ofAnnals
of Mathematics Studies.Princeton University Press, Princeton, 1989.
- (13)dorky, “Galois structure of the new counterexample to the Jacobian
conjecture: an explicit cubic model withS3{S}_{3}monodromy.”MathOverflow question
513387, 2026.Posted July 20, 2026.
- (14)dorky, “A Jacobian-neutral birational construction for Keller maps, with
noninjective examples of every generic degreed≥3d\geq 3.”MathOverflow question
513390, 2026.Posted July 20, 2026.
- (15)A. Gallagher, “The Jacobian counterexample, explained.”Online mathematical essay,
2026.Published July 20, 2026.

## 


- 


Major funding support from
