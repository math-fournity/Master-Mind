# Exact Results for the Symmetric Dyson Exclusion Process

**arXiv ID**: 2607.28807v1
**Authors**: Ali Zahra, Jerome Dubail, Gunter M. Schutz
**Published**: 2026-07-30
**Categories**: cond-mat.stat-mech, math-ph
**HTML URL**: https://arxiv.org/html/2607.28807v1

## Abstract

The symmetric Dyson exclusion process (SDEP) is an exclusion process on the lattice with a long-range logarithmic Coulomb-type interaction. It appears in several equivalent forms: as symmetric random walkers conditioned, in the Doob-transform sense, not to collide; as the maximal-activity limit of a conditioned SSEP; and as a ground-state transform of the spin- 1/2 XX chain. In this work, we exploit this latter representation to obtain exact evolution formulas from deterministic initial configurations. The resulting determinantal kernel is expressed through a finite interpolation expression in terms of Lagrange polynomials, leading to explicit density evolution in finite and infinite lattices. For the melting of a densely packed block, we show that the full hierarchy of density moments is governed by a finite-dimensional polynomial algebra, and we identify Catalan numbers in the leading time coefficients. We also derive the Euler-scale density profile and the arctic curve separating frozen and liquid regions, and show that they coincide with conjectured hydrodynamic results obtained in a previous work.

## Full Text

Exact Results for the Symmetric Dyson Exclusion Process

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
- 
- 
- 
- 
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2607.28807v1 [cond-mat.stat-mech] 30 Jul 2026

## Exact Results for the Symmetric Dyson Exclusion ProcessA. ZahraLaboratoire de Physique et Chimie Théoriques, Université de Lorraine, Nancy, FranceJ. DubailCentre Européen de Sciences Quantiques and ISIS (UMR 7006), Université de Strasbourg and CNRS, Strasbourg, FranceG. M. SchützCentro de Análise Matemática, Geometria e Sistemas Dinâmicos, Departamento de Matemática, Instituto Superior Técnico, Universidade de Lisboa, Lisbon, Portugal

## Abstract

The symmetric Dyson exclusion process (SDEP) is an exclusion process on the
lattice with a long-range logarithmic Coulomb-type interaction. It appears in
several equivalent forms: as symmetric random walkers conditioned, in the
Doob-transform sense, not to collide; as the maximal-activity limit of a
conditioned SSEP; and as a ground-state transform of the spin- 1/2 XX
chain. In this work, we
exploit this latter representation to obtain exact evolution formulas from
deterministic initial configurations. The resulting determinantal kernel
is expressed through a finite interpolation
expression in terms of Lagrange polynomials, leading to explicit density
evolution in finite and infinite lattices. For the melting of a densely packed
block, we show that the full hierarchy of density moments is governed by a
finite-dimensional polynomial algebra, and we identify Catalan numbers in the
leading time coefficients. We also derive the Euler-scale density profile and
the arctic curve separating frozen and liquid regions, and show that they coincide with conjectured hydrodynamic results obtained in a previous work.

## 
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
- 
- 
- 
- 
- 
- 
- 
- 
- 

## 1Introduction

Interacting particle systems provide some of the most successful microscopic
models of nonequilibrium statistical mechanics, and the exclusion process is
their paradigm[1,2,3]. For systems with
short-range interactions, the passage from the microscopic stochastic dynamics
to a deterministic macroscopic description is by now well understood: under
diffusive scaling the coarse-grained density obeys a closed hydrodynamic
equation—the heat equation for the symmetric simple exclusion process
(SSEP)—as a consequence of the law of large numbers together with local
stationarity[1,2]. In one dimension, integrability
sharpens this picture considerably: for the asymmetric exclusion process the
master equation can be solved exactly[4,5], and the
resulting determinantal, free-fermion structure underlies precise results on
current statistics, Kardar–Parisi–Zhang fluctuations, and limit
shapes[6,7,8].

This well-developed picture relies crucially on the interactions being
short-ranged. For particle systems with long-range interactions, exact results
are scarce, and even the notion of a local current as a function of the local
density becomes
questionable[9,10,11,12,13].
A tractable and paradigmatic member of this class is the symmetric Dyson
exclusion process (SDEP): a gas of particles hopping on a ring under exclusion,
with nearest-neighbour rates carrying a long-range, logarithmic (Coulomb-type)
interaction.
The SDEP arises in several seemingly unrelated contexts. It was introduced as
a model of vicinal surfaces[14], and it also admits an
interpretation as free symmetric walkers conditioned, in the Doob-transform
sense, never to collide. It appears when the SSEP is conditioned on an
atypically large activity[15,16]; in the limit
of maximal activity, this conditioning generates precisely the logarithmic
interaction. Its invariant measure is the discrete circular Dyson log-gas,
namely the lattice analogue of the CUE eigenangle distribution[17]. The model is also closely tied to the Calogero–Sutherland
system[18,19,20].

The structural fact that makes the SDEP solvable is that its generator is the
ground-state (Doob) transform of the spin-12\tfrac{1}{2}XX quantum chain, a
free-fermion model[21,22]. In a companion
paper[23]we exploited this mapping to argue that, under
ballistic (Eulerian) scaling, the SDEP is governed by a closed butnon-localhydrodynamic equation whose current depends on the entire
density profile through a Hilbert transform.
This non-local equation is equivalent to a local two-field complex Hopf
(inviscid Burgers) system of the type arising in free-fermion imaginary-time
hydrodynamics and limit-shape problems[24,25,46], and it predicts limit shapes
and arctic curves that were confirmed by Monte-Carlo simulation.
The real-time dynamics of lattice free fermions launched from zero-entropy
states, including compact-block or double-domain-wall initial conditions, has
itself been studied extensively[26,27,28,29,45].
In the present work we use the free-fermion mapping not as a route to a
macroscopic conjecture, but as a tool for derivingexactresults, both at
finite size and in scaling limits. Our starting point is a dictionary that
expresses any equal-time SDEP observable, evolved from a deterministic initial
configuration, as a free-fermion matrix element taken between the XX ground state
and that configuration. Since both states are Slater determinants, Wick’s
theorem applies and all correlations are determinantal; the relevant kernel is,
however, generically non-Hermitian, because it arises from a mixed matrix element
rather than from an ordinary quantum expectation. Evaluating this kernel for
deterministic initial data reduces to a trigonometric Lagrange interpolation
problem, which we solve in closed form. From this single input we obtain exact
finite-volume and infinite-volume formulas for the density profile at all times;
a universal finite-dimensional algebra for the density moments of arbitrary
deterministic finite configurations, whose highest-time coefficients have
Catalan asymptotics; an exact finite representation of the melting of densely
packed blocks and their enhanced one-body spreading; and a rigorous
steepest-descent analysis of the Euler-scaling limit that
yields the emergent limit shape and the boundary—the arctic curve—separating
the frozen regions, where the density is0or11, from the liquid region.

These results connect the SDEP to several active lines of research. The
determinantal correlations place it within the theory of determinantal point
processes that has proved so powerful for exclusion processes and random
matrices. The emergent limit shapes and arctic curves are of the kind familiar
from dimer coverings, the six-vertex model, and random tilings, where they are
analysed through complex Burgers equations and inhomogeneous free-field
techniques[25,30,31,32,33,34,46].
The block profiles we compute are close relatives of the emptiness formation
probability and the full counting statistics of the XX
chain[24,35,36,37].
Finally, in the low-density limit our lattice results reduce to those of the
continuous Dyson gas of Brownian particles with logarithmic
repulsion[38,39,40,41],
the hard-core constraintρ≤1\rho\leq 1being the essential lattice feature absent in
the continuum.

The paper is organised as follows.
Section2recalls the definition of the SDEP—its
hopping rates and generator, the mapping to the XX chain by the ground-state
transform, and the reversible Dyson measure—and fixes the notation used
throughout. Section2.4establishes the dictionary
between SDEP observables and free-fermion matrix elements and the resulting
determinantal structure. Section3evaluates the
mixed correlation kernel for deterministic initial configurations in closed form.
Section4derives the exact density-evolution
formulas in finite and infinite volume. Section5develops the universal polynomial moment algebra for deterministic initial data,
derives the first two moment identities, and specializes the general density
formula to obtain a finite representation and explicit centered moments for a
compact block.
Section6derives the Euler-scale limit shape
and the associated arctic curve.

## 2The SDEP and the XX ground-state transform

We recall the definition of the symmetric Dyson exclusion process (SDEP), following[23]. The process is defined on the discrete torus𝕋L=ℤ/L​ℤ\mathbb{T}_{L}=\mathbb{Z}/L\mathbb{Z}, withL≥2L\geq 2, in a sector with a fixed
numberNNof particles,1≤N≤L1\leq N\leq L. Configurations are exclusion
configurations: each site contains at most one particle. We write a configuration
as the ordered set of occupied sitesη={x1<⋯<xN}⊂{1,…,L},\eta=\{x_{1}<\cdots<x_{N}\}\subset\{1,\ldots,L\},

with the usual periodic identification.

The dynamics consists of nearest-neighbour jumps. A particle atxix_{i}can move
toxi±1x_{i}\pm 1if the target site is empty; otherwise the move is forbidden. The
rate of an allowed jump isci±​(η)=w​∏j≠isin⁡(π​(xi±1−xj)L)sin⁡(π​(xi−xj)L),c_{i}^{\pm}(\eta)=w\prod_{j\neq i}\frac{\sin\left(\frac{\pi(x_{i}\pm 1-x_{j})}{L}\right)}{\sin\left(\frac{\pi(x_{i}-x_{j})}{L}\right)},(2.1)

wherew>0w>0fixes the microscopic time scale. Thus the motion is local in
space, since particles only jump to neighbouring sites, but the jump rates are
non-local: the rate of a given particle depends on the positions of all the
others.

A useful way to write the rates is in terms of the positive functionΦN​(x1,…,xN)=∏1≤i<j≤Nsin⁡(π​(xj−xi)L),1≤x1<⋯<xN≤L.\Phi_{N}(x_{1},\ldots,x_{N})=\prod_{1\leq i<j\leq N}\sin\left(\frac{\pi(x_{j}-x_{i})}{L}\right),\qquad 1\leq x_{1}<\cdots<x_{N}\leq L.(2.2)

Indeed, ifηx,y\eta^{x,y}denotes the configuration obtained fromη\etaby
moving a particle fromxxto an empty neighbouring sitey=x±1y=x\pm 1, then
(2.1) can be written equivalently asc​(η,ηx,y)=w​ΦN​(ηx,y)ΦN​(η),y=x±1.c(\eta,\eta^{x,y})=w\,\frac{\Phi_{N}(\eta^{x,y})}{\Phi_{N}(\eta)},\qquad y=x\pm 1.(2.3)

This ratio form is independent of the chosen ordering convention and makes the
positivity of the allowed jump rates manifest.

## Remark 2.1.

The ratio form (2.3) shows that the SDEP can be viewed
as a Doob transform of free walkers killed at collisions. Indeed, start fromNNindependent continuous-time symmetric random walkers on𝕋L\mathbb{T}_{L},
each jumping to each nearest neighbour with rateww, and kill the process
when two particles occupy the same site. The functionΦN\Phi_{N}vanishes on
the collision boundary and is the positive ground state of the killed process.
The Doob transform byΦN\Phi_{N}changes the free jump rate (w) intow​ΦN​(ηx,y)ΦN​(η),w\frac{\Phi_{N}(\eta^{x,y})}{\Phi_{N}(\eta)},

which is exactly the SDEP rate. Thus the SDEP may be interpreted as the infinite-horizon conditioning of free
walkers to avoid collisions, or equivalently as the associated (Q)-process.
This is the lattice circular analogue of the classical construction of
non-colliding Brownian motions via Doob transforms and
Karlin–McGregor determinants; see, for example,[42,43,44].

## 2.1The Markov generator

Formally, the SDEP is the continuous-time Markov process on the configuration
spaceΩL,N={η∈{0,1}𝕋L:∑x∈𝕋Lηx=N}\Omega_{L,N}=\left\{\eta\in\{0,1\}^{\mathbb{T}_{L}}:\sum_{x\in\mathbb{T}_{L}}\eta_{x}=N\right\}

whose generator acts on functionsf:ΩL,N→ℝf:\Omega_{L,N}\to\mathbb{R}by(ℒL,NSDEP​f)​(η)=∑x∈𝕋Ly=x±1c​(η,ηx,y)​[f​(ηx,y)−f​(η)],(\mathcal{L}_{L,N}^{\mathrm{SDEP}}f)(\eta)=\sum_{\begin{subarray}{c}x\in\mathbb{T}_{L}\\
y=x\pm 1\end{subarray}}c(\eta,\eta^{x,y})\left[f(\eta^{x,y})-f(\eta)\right],(2.4)

with the rates (2.3). Every result below is obtained by
analysing this generator, and the essential tool is its exact mapping to free
fermions, which we describe next.

## 2.2Free-fermion representation

Letcx,cx†c_{x},c_{x}^{\dagger}be canonical fermionic annihilation and creation
operators on𝕋L\mathbb{T}_{L}, and letHLX​X=−w​∑x=1L(cx+1†​cx+cx†​cx+1)H_{L}^{XX}=-w\sum_{x=1}^{L}\left(c_{x+1}^{\dagger}c_{x}+c_{x}^{\dagger}c_{x+1}\right)(2.5)

be the free-fermion XX Hamiltonian, obtained from the spin-12\tfrac{1}{2}XX chain
by a Jordan–Wigner transformation. In theNN-particle sector the
single-particle momenta run over𝒦L,N={2​πL​(m+θN):m=0,…,L−1},θN∈{0,12},\mathcal{K}_{L,N}=\left\{\frac{2\pi}{L}(m+\theta_{N}):m=0,\ldots,L-1\right\},\qquad\theta_{N}\in\{0,\tfrac{1}{2}\},

whereθN\theta_{N}keeps track of the fermionic boundary condition
induced by the Jordan–Wigner transformation. For oddNN, one hasθN=0\theta_{N}=0, corresponding to periodic boundary conditions,cL+1=c1,c_{L+1}=c_{1},whereas for evenNN, one hasθN=12\theta_{N}=\frac{1}{2}, corresponding to
antiperiodic boundary conditions,cL+1=−c1.c_{L+1}=-c_{1}..
The single-particle dispersion isε​(k)=−2​w​cos⁡k.\varepsilon(k)=-2w\cos k.(2.6)

TheNN-particle ground state|GSN⟩|\mathrm{GS}_{N}\rangleis obtained by filling
theNNmomenta closest to0. In the position basis|x1,…,xN⟩=cx1†​⋯​cxN†​|0⟩|x_{1},\ldots,x_{N}\rangle=c_{x_{1}}^{\dagger}\cdots c_{x_{N}}^{\dagger}|0\rangleits wave
function is the Vandermonde determinantdet(ei​ka​xb)a,b=1N\det(e^{ik_{a}x_{b}})_{a,b=1}^{N}, which up
to an overall phase is precisely the positive function (2.2):⟨x1,…,xN|GSN⟩=1ZL,N​ΦN​(x1,…,xN).\langle x_{1},\ldots,x_{N}|\mathrm{GS}_{N}\rangle=\frac{1}{\sqrt{Z_{L,N}}}\,\Phi_{N}(x_{1},\ldots,x_{N}).(2.7)

Summing theNNlowest energies yields the ground-state energyEL,N=−2​w​sin⁡(π​N/L)sin⁡(π/L).E_{L,N}=-2w\,\frac{\sin(\pi N/L)}{\sin(\pi/L)}.(2.8)

The identity (2.7) is what links the two models. SinceΦN>0\Phi_{N}>0andHL,NX​X​ΦN=EL,N​ΦNH_{L,N}^{XX}\Phi_{N}=E_{L,N}\Phi_{N}, conjugatingHL,NX​XH_{L,N}^{XX}by the diagonal multiplication operator(Φ^N​f)​(η)=ΦN​(η)​f​(η)(\widehat{\Phi}_{N}f)(\eta)=\Phi_{N}(\eta)f(\eta)produces a Markov generator,
namely the ground-state (Doob) transformℒL,NSDEP=−Φ^N−1​(HL,NX​X−EL,N)​Φ^N,\mathcal{L}_{L,N}^{\mathrm{SDEP}}=-\widehat{\Phi}_{N}^{-1}\left(H_{L,N}^{XX}-E_{L,N}\right)\widehat{\Phi}_{N},(2.9)

equivalentlyHL,NX​X=EL,N−Φ^N​ℒL,NSDEP​Φ^N−1.H_{L,N}^{XX}=E_{L,N}-\widehat{\Phi}_{N}\mathcal{L}_{L,N}^{\mathrm{SDEP}}\widehat{\Phi}_{N}^{-1}.(2.10)

Indeed, the off-diagonal element ofHLX​XH_{L}^{XX}between two configurations
related by an allowed jump is−w-w, so−ΦN​(η)−1​Hη,η′X​X​ΦN​(η′)=w​ΦN​(η′)/ΦN​(η)-\Phi_{N}(\eta)^{-1}H^{XX}_{\eta,\eta^{\prime}}\Phi_{N}(\eta^{\prime})=w\,\Phi_{N}(\eta^{\prime})/\Phi_{N}(\eta)recovers the rate (2.3), while the eigenvalue equation
fixes the diagonal part so that the escape rates are those of a genuine Markov
generator. Through (2.9), the SDEP semigroupet​ℒL,NSDEPe^{t\mathcal{L}_{L,N}^{\mathrm{SDEP}}}is conjugate to the free-fermion
evolutione−t​(HL,NX​X−EL,N)e^{-t(H_{L,N}^{XX}-E_{L,N})}, whose single-particle dynamics is
carried by the propagatorpt(L,N)​(x)=1L​∑k∈𝒦L,Ne−i​k​x​et​ε​(k),p_{t}^{(L,N)}(x)=\frac{1}{L}\sum_{k\in\mathcal{K}_{L,N}}e^{-ikx}\,e^{t\varepsilon(k)},(2.11)

the superscriptNNrecording only the boundary-condition sector.

## 2.3Invariant measure

BecauseΦN\Phi_{N}is the ground-state wave function
(2.7), its squared amplitude defines a natural
probability measure onΩL,N\Omega_{L,N},πL,N​(η)=1ZL,N​ΦN​(η)2,\pi_{L,N}(\eta)=\frac{1}{Z_{L,N}}\,\Phi_{N}(\eta)^{2},(2.12)

with normalizationZL,NZ_{L,N}. This is the discrete circular Dyson measure: it
describesNNparticles on the ring with logarithmic repulsion−2​∑1≤i<j≤Nlog⁡|sin⁡(π​(xj−xi)L)|,-2\sum_{1\leq i<j\leq N}\log\left|\sin\left(\frac{\pi(x_{j}-x_{i})}{L}\right)\right|,

and coincides with the distribution of eigenvalue angles of random unitary
matrices undergoing Dyson’s Brownian motion.

The measure (2.12) is reversible for the SDEP. Indeed, for any
allowed jumpη→ηx,y\eta\to\eta^{x,y},πL,N​(η)​c​(η,ηx,y)=wZL,N​ΦN​(η)​ΦN​(ηx,y)\pi_{L,N}(\eta)\,c(\eta,\eta^{x,y})=\frac{w}{Z_{L,N}}\,\Phi_{N}(\eta)\,\Phi_{N}(\eta^{x,y})

is symmetric underη↔ηx,y\eta\leftrightarrow\eta^{x,y}, so detailed balanceπL,N​(η)​c​(η,η′)=πL,N​(η′)​c​(η′,η)\pi_{L,N}(\eta)\,c(\eta,\eta^{\prime})=\pi_{L,N}(\eta^{\prime})\,c(\eta^{\prime},\eta)(2.13)

holds andπL,N\pi_{L,N}is stationary. Equivalently, reversibility reflects the
Hermiticity ofHL,NX​XH_{L,N}^{XX}: the transform (2.9) makesℒL,NSDEP\mathcal{L}_{L,N}^{\mathrm{SDEP}}self-adjoint inL2​(πL,N)L^{2}(\pi_{L,N}).

The ground-state transform is the mechanism behind all the exact formulas of the
following sections. Through it, time-dependent SDEP observables map to
free-fermion matrix elements between the XX ground state|GSN⟩|\mathrm{GS}_{N}\rangleand the initial configuration, evolved with the
propagator (2.11). We make this dictionary precise in
the next section.

## 2.4Observable dictionary between SDEP and free-fermions

The ground-state transform does more than identify the SDEP generator with the
XX Hamiltonian. It also gives a dictionary between observables of the classical
exclusion process and matrix elements of free fermions. We record this
dictionary before turning to explicit formulas.

LetF:ΩL,N→ℝF:\Omega_{L,N}\to\mathbb{R}be a classical observable. We associate withFFthe diagonal operatorF^\widehat{F}on theNN-particle fermionic Fock
space byF^​|η⟩=F​(η)​|η⟩.\widehat{F}|\eta\rangle=F(\eta)|\eta\rangle.

In particular,ηx⟷cx†​cx,\eta_{x}\quad\longleftrightarrow\quad c_{x}^{\dagger}c_{x},

and, for distinct sitesx1,…,xmx_{1},\ldots,x_{m},ηx1​⋯​ηxm⟷cx1†​cx1​⋯​cxm†​cxm.\eta_{x_{1}}\cdots\eta_{x_{m}}\quad\longleftrightarrow\quad c_{x_{1}}^{\dagger}c_{x_{1}}\cdots c_{x_{m}}^{\dagger}c_{x_{m}}.

For a set of occupied sitesS={x1<⋯<xN}⊂𝕋L,S=\{x_{1}<\cdots<x_{N}\}\subset\mathbb{T}_{L},

we denote by|S⟩:=cx1†​⋯​cxN†​|0⟩|S\rangle:=c_{x_{1}}^{\dagger}\cdots c_{x_{N}}^{\dagger}|0\rangle

the corresponding fermionic occupation-basis state.

## Proposition 2.2.

Let the SDEP start from a deterministic configurationS∈ΩL,NS\in\Omega_{L,N}. Then, for every observableF:ΩL,N→ℝF:\Omega_{L,N}\to\mathbb{R},𝔼S​[F​(η​(t))]=⟨GSN|et​HL,NX​X​F^​e−t​HL,NX​X|S⟩⟨GSN|S⟩.\mathbb{E}_{S}[F(\eta(t))]=\frac{\langle\mathrm{GS}_{N}|e^{tH^{XX}_{L,N}}\widehat{F}e^{-tH^{XX}_{L,N}}|S\rangle}{\langle\mathrm{GS}_{N}|S\rangle}.(2.14)

## Proof.

The ground-state transform giveset​ℒL,NSDEP=Φ^N−1​e−t​(HL,NX​X−EL,N)​Φ^N.e^{t\mathcal{L}^{\mathrm{SDEP}}_{L,N}}=\widehat{\Phi}_{N}^{-1}e^{-t(H^{XX}_{L,N}-E_{L,N})}\widehat{\Phi}_{N}.

SinceFFis diagonal,F^\widehat{F}commutes withΦ^N\widehat{\Phi}_{N}. Using
that⟨GSN|η⟩=ZL,N−1/2​ΦN​(η),\langle\mathrm{GS}_{N}|\eta\rangle=Z_{L,N}^{-1/2}\Phi_{N}(\eta),

and that the ground-state energy cancels between numerator and denominator, one
obtains (2.14).
∎

For the density, Proposition2.2givesρS​(x,t)=𝔼S​[ηx​(t)]=⟨GSN|et​HL,NX​X​cx†​cx​e−t​HL,NX​X|S⟩⟨GSN|S⟩.\rho_{S}(x,t)=\mathbb{E}_{S}[\eta_{x}(t)]=\frac{\langle\mathrm{GS}_{N}|e^{tH^{XX}_{L,N}}c_{x}^{\dagger}c_{x}e^{-tH^{XX}_{L,N}}|S\rangle}{\langle\mathrm{GS}_{N}|S\rangle}.(2.15)

Thus a classical density is converted into a free-fermion two-point function,
but with a mixed matrix element: the left state is the XX ground state, whereas
the right state is the deterministic configurationSS.

More generally, define the time-dependent (mixed) kernelKtS​(x,y)=⟨GSN|et​HL,NX​X​cx†​cy​e−t​HL,NX​X|S⟩⟨GSN|S⟩.K_{t}^{S}(x,y)=\frac{\langle\mathrm{GS}_{N}|e^{tH^{XX}_{L,N}}c_{x}^{\dagger}c_{y}e^{-tH^{XX}_{L,N}}|S\rangle}{\langle\mathrm{GS}_{N}|S\rangle}.(2.16)

ThenρS​(x,t)=KtS​(x,x).\rho_{S}(x,t)=K_{t}^{S}(x,x).

SinceHL,NX​XH^{XX}_{L,N}is quadratic and both⟨GSN|\langle\mathrm{GS}_{N}|and|S⟩|S\rangleare Slater states, Wick
factorization holds. Therefore, for distinct sitesx1,…,xmx_{1},\ldots,x_{m},𝔼S​[∏a=1mηxa​(t)]=det[KtS​(xa,xb)]a,b=1m.\mathbb{E}_{S}\left[\prod_{a=1}^{m}\eta_{x_{a}}(t)\right]=\det\left[K_{t}^{S}(x_{a},x_{b})\right]_{a,b=1}^{m}.(2.17)

Thus, at each fixed time, the SDEP started from a deterministic configuration is
described by a determinantal kernel, although this kernel is in general
non-Hermitian because it comes from a mixed matrix element rather than from an
ordinary quantum expectation.

Finally, using the free-fermion evolution,et​HL,NX​X​cx†​e−t​HL,NX​X=∑u∈𝕋Lpt(L,N)​(x−u)​cu†,e^{tH^{XX}_{L,N}}c_{x}^{\dagger}e^{-tH^{XX}_{L,N}}=\sum_{u\in\mathbb{T}_{L}}p_{t}^{(L,N)}(x-u)c_{u}^{\dagger},

andet​HL,NX​X​cy​e−t​HL,NX​X=∑v∈𝕋Lp−t(L,N)​(v−y)​cv,e^{tH^{XX}_{L,N}}c_{y}e^{-tH^{XX}_{L,N}}=\sum_{v\in\mathbb{T}_{L}}p_{-t}^{(L,N)}(v-y)c_{v},

the kernel becomesKtS​(x,y)=∑u,v∈𝕋Lpt(L,N)​(x−u)​p−t(L,N)​(v−y)​K0S​(u,v),K_{t}^{S}(x,y)=\sum_{u,v\in\mathbb{T}_{L}}p_{t}^{(L,N)}(x-u)p_{-t}^{(L,N)}(v-y)K^{S}_{0}(u,v),(2.18)

whereK0S​(u,v)=⟨GSN|cu†​cv|S⟩⟨GSN|S⟩.K^{S}_{0}(u,v)=\frac{\langle\mathrm{GS}_{N}|c_{u}^{\dagger}c_{v}|S\rangle}{\langle\mathrm{GS}_{N}|S\rangle}.(2.19)

The next section evaluatesK0S​(u,v)K^{S}_{0}(u,v)explicitly for deterministic
configurations.

## 3Correlations with deterministic configurations

It remains to evaluate the initial kernelK0S​(x,y)=⟨GSN|cx†​cy|S⟩⟨GSN|S⟩K^{S}_{0}(x,y)=\frac{\langle\mathrm{GS}_{N}|c_{x}^{\dagger}c_{y}|S\rangle}{\langle\mathrm{GS}_{N}|S\rangle}

for deterministic configurationsSS. This is the only model-specific input
needed in the kernel evolution formula (2.18). We first
derive the exact finite-volume expression on the torus and then take its
infinite-volume limit at fixed particle number.

## 3.1Finite-volume mixed kernel

LetS⊂𝕋LS\subset\mathbb{T}_{L}be a deterministic set ofNNoccupied sites.
The initial mixed kernel is given by a trigonometric Lagrange interpolation
formula.

## Proposition 3.1.

Forx,y∈𝕋Lx,y\in\mathbb{T}_{L}, one hasK0S​(x,y)={∏z∈S∖{y}sin⁡(πL​(x−z))sin⁡(πL​(y−z)),y∈S,0,y∉S.K^{S}_{0}(x,y)=\begin{cases}\displaystyle\prod_{z\in S\setminus\{y\}}\frac{\sin\left(\frac{\pi}{L}(x-z)\right)}{\sin\left(\frac{\pi}{L}(y-z)\right)},&y\in S,\\[13.99995pt]
0,&y\notin S.\end{cases}(3.1)

Notice that the right-hand side is the trigonometric Lagrange interpolation
polynomial associated with the setSS. In particular, for fixedy∈Sy\in S,
the functionx⟼K0S​(x,y)x\longmapsto K^{S}_{0}(x,y)

equals11atx=yx=yand vanishes at all other points ofSS. ThusK0S​(x,y)=δx,y,x,y∈S.K^{S}_{0}(x,y)=\delta_{x,y},\qquad x,y\in S.

Away from the initially occupied sites, however,K0S​(x,y)K^{S}_{0}(x,y)is nonlocal. This
nonlocal interpolation structure is the source of the explicit formulas below.

## Proof.

Let the occupied sites ofSSbes1,…,sNs_{1},\ldots,s_{N}. The XX ground state is a
Slater determinant built from theNNlowest momenta. We write these momenta
aska=2​πL​(a−N+12),a=1,…,N,k_{a}=\frac{2\pi}{L}\left(a-\frac{N+1}{2}\right),\qquad a=1,\ldots,N,

up to the harmless choice of boundary-condition convention. Define theN×NN\times NmatrixVα​a=e−i​ka​sα,α,a=1,…,N.V_{\alpha a}=e^{-ik_{a}s_{\alpha}},\qquad\alpha,a=1,\ldots,N.

The overlap⟨GSN|S⟩\langle\mathrm{GS}_{N}|S\rangleis proportional todetV\det V.

Fory∈Sy\in S, sayy=sβy=s_{\beta}, we first compute the vectorua​(y):=⟨GSN|c†​(ka)​cy|S⟩⟨GSN|S⟩.u_{a}(y):=\frac{\langle\mathrm{GS}_{N}|c^{\dagger}(k_{a})c_{y}|S\rangle}{\langle\mathrm{GS}_{N}|S\rangle}.

Usingcsα†=1L​∑a=1Ne−i​ka​sα​c†​(ka)+modes outside the filled Fermi sea,c_{s_{\alpha}}^{\dagger}=\frac{1}{\sqrt{L}}\sum_{a=1}^{N}e^{-ik_{a}s_{\alpha}}c^{\dagger}(k_{a})+\text{modes outside the filled Fermi sea},

and using the canonical anticommutation relations inside the matrix element, we
obtain∑a=1NVα​a​ua​(y)=L​δα,β.\sum_{a=1}^{N}V_{\alpha a}u_{a}(y)=\sqrt{L}\,\delta_{\alpha,\beta}.

Thusua​(y)u_{a}(y)is determined by the inverse of the Vandermonde-type matrixVV.

It remains to write this inverse explicitly. Introduce the trigonometric
Lagrange functionℒy​(x)=∏z∈S∖{y}sin⁡(πL​(x−z))sin⁡(πL​(y−z)).\mathcal{L}_{y}(x)=\prod_{z\in S\setminus\{y\}}\frac{\sin\left(\frac{\pi}{L}(x-z)\right)}{\sin\left(\frac{\pi}{L}(y-z)\right)}.

It satisfiesℒy​(z)=δy,z,z∈S.\mathcal{L}_{y}(z)=\delta_{y,z},\qquad z\in S.

Moreover, as a function ofe2​π​i​x/Le^{2\pi ix/L}, it is a Laurent polynomial with
Fourier modes contained in the Fermi sea of theNN-particle ground state.
Therefore its Fourier coefficients are precisely the entries of the inverse ofVV. Consequently,⟨GSN|cx†​cy|S⟩⟨GSN|S⟩=ℒy​(x),y∈S.\frac{\langle\mathrm{GS}_{N}|c_{x}^{\dagger}c_{y}|S\rangle}{\langle\mathrm{GS}_{N}|S\rangle}=\mathcal{L}_{y}(x),\qquad y\in S.

Ify∉Sy\notin S, thency​|S⟩=0c_{y}|S\rangle=0, and the matrix element vanishes. This
proves (3.1).
∎

## 3.2Infinite-volume limit

We shall often use Proposition3.1in
the regime whereL→∞L\to\inftywhile the number of particlesNNremains
fixed. In this limit, the torus becomes the infinite latticeℤ\mathbb{Z}, andsin⁡(πL​(x−z))∼πL​(x−z).\sin\left(\frac{\pi}{L}(x-z)\right)\sim\frac{\pi}{L}(x-z).

Therefore, for a deterministic setS⊂ℤS\subset\mathbb{Z}with|S|=N|S|=N, the
mixed correlation becomesK0S​(x,y)={∏z∈S∖{y}x−zy−z,y∈S,0,y∉S.K_{0}^{S}(x,y)=\begin{cases}\displaystyle\prod_{z\in S\setminus\{y\}}\frac{x-z}{y-z},&y\in S,\\[11.99998pt]
0,&y\notin S.\end{cases}(3.2)

This is the ordinary Lagrange interpolation formula on the lattice.
In particular, for the block initial conditionSN={1,2,…,N},S_{N}=\{1,2,\ldots,N\},(3.3)

one obtainsK0SN​(x,y)={∏j=1j≠yNx−jy−j,y∈{1,…,N},0,y∉{1,…,N}.K_{0}^{S_{N}}(x,y)=\begin{cases}\displaystyle\prod_{\begin{subarray}{c}j=1\\
j\neq y\end{subarray}}^{N}\frac{x-j}{y-j},&y\in\{1,\ldots,N\},\\[11.99998pt]
0,&y\notin\{1,\ldots,N\}.\end{cases}(3.4)

Formula (3.4) will be used in
Section5to specialize the general density evolution
to a compact block and to derive a genuinely finite representation of the
resulting melting profile.

## 4Exact density evolution

By Proposition2.2, the density is the diagonal
part of the time-dependent kernel:ρS​(x,t)=KtS​(x,x).\rho_{S}(x,t)=K_{t}^{S}(x,x).

Using the free-fermion evolution formula (2.18), we obtain
the following exact expression.

## 4.1The finite-volume formula

Using the free-fermion kernelpt(L,N)p_{t}^{(L,N)}defined in
(2.11), yields the following result for evolution of the density profile in finite volume.

## Theorem 4.1.

LetS⊂𝕋LS\subset\mathbb{T}_{L}be a deterministicNN-particle configuration.
Then the SDEP density at timettisρS​(x,t)=∑u,v∈𝕋Lpt(L,N)​(x−u)​p−t(L,N)​(v−x)​K0S​(u,v),\rho_{S}(x,t)=\sum_{u,v\in\mathbb{T}_{L}}p_{t}^{(L,N)}(x-u)\,p_{-t}^{(L,N)}(v-x)\,K^{S}_{0}(u,v),(4.1)

whereK0S​(u,v)=⟨GSN|cu†​cv|S⟩⟨GSN|S⟩K^{S}_{0}(u,v)=\frac{\langle\mathrm{GS}_{N}|c_{u}^{\dagger}c_{v}|S\rangle}{\langle\mathrm{GS}_{N}|S\rangle}

is the mixed correlation from
Proposition3.1. Equivalently,ρS​(x,t)=∑v∈S∑u∈𝕋Lpt(L,N)​(x−u)​p−t(L,N)​(v−x)​∏z∈S∖{v}sin⁡(πL​(u−z))sin⁡(πL​(v−z)).\rho_{S}(x,t)=\sum_{v\in S}\sum_{u\in\mathbb{T}_{L}}p_{t}^{(L,N)}(x-u)\,p_{-t}^{(L,N)}(v-x)\,\prod_{z\in S\setminus\{v\}}\frac{\sin\left(\frac{\pi}{L}(u-z)\right)}{\sin\left(\frac{\pi}{L}(v-z)\right)}.(4.2)

Several elementary checks are immediate. Att=0t=0,p0(L,N)​(x)=δx,0,p_{0}^{(L,N)}(x)=\delta_{x,0},

and henceρS​(x,0)=K0S​(x,x)=𝟏{x∈S}.\rho_{S}(x,0)=K_{0}^{S}(x,x)=\mathbf{1}_{\{x\in S\}}.

Moreover, the total mass is conserved. Indeed,∑x∈𝕋Lpt(L,N)​(x−u)​p−t(L,N)​(v−x)=δu,v,\sum_{x\in\mathbb{T}_{L}}p_{t}^{(L,N)}(x-u)p_{-t}^{(L,N)}(v-x)=\delta_{u,v},

and therefore∑x∈𝕋LρS​(x,t)=∑u∈𝕋LK0S​(u,u)=N.\sum_{x\in\mathbb{T}_{L}}\rho_{S}(x,t)=\sum_{u\in\mathbb{T}_{L}}K_{0}^{S}(u,u)=N.

## 4.2Infinite-volume formula

We shall also need the infinite-volume version of
Theorem4.1. LetS⊂ℤS\subset\mathbb{Z}be a finite
set with|S|=N|S|=N. In the limitL→∞L\to\infty, the kernel
(2.11) becomespt​(x)=∫−ππd​k2​π​e−i​k​x​e−2​w​t​cos⁡k=Ix​(−2​w​t),p_{t}(x)=\int_{-\pi}^{\pi}\frac{dk}{2\pi}e^{-ikx}e^{-2wt\cos k}=I_{x}(-2wt),(4.3)

whereIxI_{x}is the modified Bessel function of the first kind. Thusp−t​(x)=Ix​(2​w​t).p_{-t}(x)=I_{x}(2wt).

The density onℤ\mathbb{Z}is thereforeρS​(x,t)=∑u∈ℤ∑v∈SIx−u​(−2​w​t)​Iv−x​(2​w​t)​∏z∈S∖{v}u−zv−z.\rho_{S}(x,t)=\sum_{u\in\mathbb{Z}}\sum_{v\in S}I_{x-u}(-2wt)\,I_{v-x}(2wt)\,\prod_{z\in S\setminus\{v\}}\frac{u-z}{v-z}.(4.4)

SinceIv−x=Ix−vI_{v-x}=I_{x-v}, this may also be written asρS​(x,t)=∑u∈ℤ∑v∈SIx−u​(−2​w​t)​Ix−v​(2​w​t)​∏z∈S∖{v}u−zv−z.\rho_{S}(x,t)=\sum_{u\in\mathbb{Z}}\sum_{v\in S}I_{x-u}(-2wt)\,I_{x-v}(2wt)\,\prod_{z\in S\setminus\{v\}}\frac{u-z}{v-z}.(4.5)

Equations (4.4) and
(4.5) are exact for every finite
timettand every finite deterministic setSS. They are the
infinite-volume analogues of the finite-torus formula
(4.2).

## 5Moment identities and block melting

We now investigate the evolution of the spatial moments of the density profile
for the infinite-volume SDEP.

LetX1​(t)<⋯<XN​(t)X_{1}(t)<\cdots<X_{N}(t)

denote the particle positions at physical timettfor the process started
from the deterministic configurationSS, and let𝔼S\mathbb{E}_{S}denote the
corresponding expectation. For every nonnegative integernn, define thenn-th moment of the density profile byμnS​(t):=∑x∈ℤxn​ρS​(x,t).\mu_{n}^{S}(t):=\sum_{x\in\mathbb{Z}}x^{n}\rho_{S}(x,t).(5.1)

Equivalently,μnS​(t)=𝔼S​[∑i=1NXi​(t)n].\mu_{n}^{S}(t)=\mathbb{E}_{S}\left[\sum_{i=1}^{N}X_{i}(t)^{n}\right].(5.2)

The zeroth moment satisfiesμ0S​(t)=N\mu_{0}^{S}(t)=N

and expresses conservation of the total number of particles. The first
moment determines the mean position of the particle cloud, whereas the second
and higher moments describe its spreading and provide increasingly detailed
information about the shape of the density profile.

Although the exact density formula obtained in the previous section is
explicit, computing (5.1) directly leads to
infinite sums involving modified Bessel functions. One of the main purposes
of this section is to show that the complete moment hierarchy admits a much
simpler finite-dimensional algebraic representation. More precisely, the
time dependence of the moments will be encoded by an operator substitutionX⟼X+s​DX\longmapsto X+sD

acting on the space of polynomials of degree strictly smaller thanNN, whereXXandDDwill be defined below. This
representation separates the evolution dynamics from the dependence on the
initial configuration and implies, in particular, that every moment is a
polynomial in time of bounded degree.

We first establish this representation for an arbitrary deterministic initial
setSSand derive the resulting identities for the first two moments. We
then study the highest-time coefficient of the even moments and show that it
is independent of the detailed geometry of the initial configuration. Its
large-NNbehavior is governed by the Catalan numbers. Finally, we specialize the general results to the compact blockSNS_{N}defined in (3.3), for which we obtain a finite
representation of the exact melting profile and explicit formulas for the
first few centered even moments.

It is convenient throughout this section to introduce the dimensionless times=2​w​t.s=2wt.(5.3)

We writeρS​(x,s)\rho_{S}(x,s)andμnS​(s)\mu_{n}^{S}(s)for the density and its moments at the
physical timet=s/(2​w)t=s/(2w).

The infinite-volume jump rates areci+​(x1,…,xN)=w​∏j≠ixi+1−xjxi−xj,ci−​(x1,…,xN)=w​∏j≠ixi−1−xjxi−xj.c_{i}^{+}(x_{1},\ldots,x_{N})=w\prod_{j\neq i}\frac{x_{i}+1-x_{j}}{x_{i}-x_{j}},\qquad c_{i}^{-}(x_{1},\ldots,x_{N})=w\prod_{j\neq i}\frac{x_{i}-1-x_{j}}{x_{i}-x_{j}}.(5.4)

A jump onto an occupied site has rate zero, as is already encoded in
(5.4). Indeed, ifxi+1=xjx_{i}+1=x_{j}orxi−1=xjx_{i}-1=x_{j}for
somej≠ij\neq i, then the corresponding product contains a vanishing factor.

## 5.1Polynomial moment algebra

LetS={a1,…,aN}⊂ℤS=\{a_{1},\ldots,a_{N}\}\subset\mathbb{Z}

be an arbitrary deterministic initial configuration, and let𝒱N=ℂ<N​[x]\mathcal{V}_{N}=\mathbb{C}_{<N}[x]

be the space of polynomials of degree strictly smaller thanNN. Fora∈Sa\in S, define the Lagrange basis polynomialℓa​(x)=∏b∈Sb≠ax−ba−b,\ell_{a}(x)=\prod_{\begin{subarray}{c}b\in S\\
b\neq a\end{subarray}}\frac{x-b}{a-b},(5.5)

and the interpolation map(PS​f)​(x)=∑a∈Sf​(a)​ℓa​(x).(P_{S}f)(x)=\sum_{a\in S}f(a)\ell_{a}(x).(5.6)

PSP_{S}is a projector on𝒱N\mathcal{V}_{N}, i.e.PS​f∈𝒱NP_{S}f\in\mathcal{V}_{N}, it acts as the identity on𝒱N\mathcal{V}_{N}.

Introduce the shift operator(T​f)​(x)=f​(x+1),(Tf)(x)=f(x+1),

and the operatorsB=T+T−12,D=T−T−12,(X​f)​(x)=x​f​(x).B=\frac{T+T^{-1}}{2},\qquad D=\frac{T-T^{-1}}{2},\qquad(Xf)(x)=xf(x).(5.7)

They satisfy[B,X]=D,[D,X]=B,[B,D]=0,B2−D2=1.[B,X]=D,\qquad[D,X]=B,\qquad[B,D]=0,\qquad B^{2}-D^{2}=1.(5.8)

These relations are standard in finite operator calculus. In this
terminology,DDis the central-difference delta operator andB=[D,X]B=[D,X]

is its Pincherle derivative[47,48].
Equivalently, the operatorsX,B,DX,B,Dform a realization of the complexified1+11+1-dimensional Poincaré algebra, with quadratic CasimirB2−D2=1B^{2}-D^{2}=1. The new ingredient below is their finite-dimensional
compression by the interpolation projectorPSP_{S}, which encodes the
deterministic initial configuration.
The commutation relations above imply the following exact conjugation identity,
which is the algebraic origin of the substitutionX↦X+s​DX\mapsto X+sD.

## Lemma 5.1.

For everys∈ℝs\in\mathbb{R},es​B​X​e−s​B=X+s​D.e^{sB}Xe^{-sB}=X+sD.(5.9)

## Proof.

DefineF​(s)=es​B​X​e−s​B.F(s)=e^{sB}Xe^{-sB}.

Differentiating with respect tossgivesF′​(s)=es​B​[B,X]​e−s​B=es​B​D​e−s​B.F^{\prime}(s)=e^{sB}[B,X]e^{-sB}=e^{sB}De^{-sB}.

Since[B,D]=0[B,D]=0, the operatorDDcommutes withes​Be^{sB}, and henceF′​(s)=D.F^{\prime}(s)=D.

Together with the initial conditionF​(0)=X,F(0)=X,

this yieldsF​(s)=X+s​D,F(s)=X+sD,

which proves (5.9).
∎

Letes​B​(x,y)e^{sB}(x,y)denote the kernel ofes​Be^{sB}with respect to the canonical
basis of delta functionsδyy∈ℤ{\delta_{y}}_{y\in\mathbb{Z}}, namelyes​B​(x,y)=(es​B​δy)​(x).e^{sB}(x,y)=\bigl(e^{sB}\delta_{y}\bigr)(x).

This kernel can be written in terms of the modified Bessel function as follows:

## Lemma 5.2.

For everys∈ℝs\in\mathbb{R}, the integral kernel ofe−s​Be^{-sB}is(e−s​B)​(x,u)=Ix−u​(−s),\left(e^{-sB}\right)(x,u)=I_{x-u}(-s),

whereInI_{n}denotes the modified Bessel function of the first kind.
Equivalently, for every functionfffor which the sum is well defined,(e−s​B​f)​(x)=∑u∈ℤIx−u​(−s)​f​(u).\left(e^{-sB}f\right)(x)=\sum_{u\in\mathbb{Z}}I_{x-u}(-s)f(u).(5.10)

## Proof.

Under the Fourier transformf^​(k)=∑x∈ℤf​(x)​e−i​k​x,k∈[−π,π],\widehat{f}(k)=\sum_{x\in\mathbb{Z}}f(x)e^{-ikx},\qquad k\in[-\pi,\pi],

the operatorBBacts by multiplication bycos⁡k\cos k:B​f^​(k)=cos⁡(k)​f^​(k).\widehat{Bf}(k)=\cos(k)\widehat{f}(k).

Therefore,e−s​B​f^​(k)=e−s​cos⁡k​f^​(k).\widehat{e^{-sB}f}(k)=e^{-s\cos k}\widehat{f}(k).

Taking the inverse Fourier transform gives(e−s​B​f)​(x)=∑u∈ℤ[∫−ππd​k2​π,ei​k​(x−u)​e−s​cos⁡k]​f​(u).\left(e^{-sB}f\right)(x)=\sum_{u\in\mathbb{Z}}\left[\int_{-\pi}^{\pi}\frac{\mathrm{d}k}{2\pi},e^{ik(x-u)}e^{-s\cos k}\right]f(u).

Using the integral representationIn​(z)=∫−ππd​k2​π,ei​k​n​ez​cos⁡k,I_{n}(z)=\int_{-\pi}^{\pi}\frac{\mathrm{d}k}{2\pi},e^{ikn}e^{z\cos k},

the quantity in brackets isIx−u​(−s)I_{x-u}(-s). This proves
(5.10).
∎

## Theorem 5.3(polynomial representation of the moments).

For every deterministic finite setS⊂ℤS\subset\mathbb{Z}, with|S|=N|S|=N, and
everyn≥0n\geq 0,μnS​(s)=∑a∈S[(X+s​D)n​ℓa]​(a)=Tr𝒱N⁡[PS​(X+s​D)n].\mu_{n}^{S}(s)=\sum_{a\in S}\left[(X+sD)^{n}\ell_{a}\right](a)=\operatorname{Tr}_{\mathcal{V}_{N}}\left[P_{S}(X+sD)^{n}\right].(5.11)

Consequently,μnS​(s)\mu_{n}^{S}(s)is a polynomial inssof degree at most⌊n/2⌋\lfloor n/2\rfloor.

## Proof.

The exact infinite-volume density formula
(4.5) can be written asρS​(x,s)=∑a∈SIx−a​(s)​(e−s​B​ℓa)​(x),\rho_{S}(x,s)=\sum_{a\in S}I_{x-a}(s)\left(e^{-sB}\ell_{a}\right)(x),(5.12)

because the kernel ofe−s​Be^{-sB}isIx−u​(−s)I_{x-u}(-s). ThereforeμnS​(s)\displaystyle\mu_{n}^{S}(s)=∑a∈S∑x∈ℤIa−x​(s)​xn​(e−s​B​ℓa)​(x)\displaystyle=\sum_{a\in S}\sum_{x\in\mathbb{Z}}I_{a-x}(s)x^{n}\left(e^{-sB}\ell_{a}\right)(x)=∑a∈S[es​B​Xn​e−s​B​ℓa]​(a).\displaystyle=\sum_{a\in S}\left[e^{sB}X^{n}e^{-sB}\ell_{a}\right](a).

Using (5.9),es​B​Xn​e−s​B=(X+s​D)n,e^{sB}X^{n}e^{-sB}=(X+sD)^{n},

which proves the first equality in
(5.11).

To obtain the trace formula, use the Lagrange basis{ℓa:a∈S}\{\ell_{a}:a\in S\}of𝒱N\mathcal{V}_{N}. For any polynomialgg, the
coefficient ofℓa\ell_{a}inPS​gP_{S}gisg​(a)g(a). Hence the trace ofPS​(X+s​D)nP_{S}(X+sD)^{n}on𝒱N\mathcal{V}_{N}is precisely the finite sum in the first
part of (5.11).

Finally, expand(X+s​D)n(X+sD)^{n}as a non-commutative polynomial. The coefficient
ofsks^{k}is a sum of words containingkklettersDDandn−kn-klettersXX. On polynomials,XXraises the degree by one, whereasDDlowers it by at least one. Ifk>n/2k>n/2, every such word strictly lowers
polynomial degree. Its image already belongs to𝒱N\mathcal{V}_{N}, soPSP_{S}does not change it, and its matrix in the monomial basis is strictly lower
triangular. Its trace therefore vanishes. This proves the degree bound.
∎

Explicit examples on how to use this theorem to compute the moments will be given in section5.4.

## 5.2Universal first and second moments

We next derive the first two moment identities directly from the jump rates.
The following interpolation lemma replaces the shifted identities by a single
formula valid for an arbitrary displacement.

## Lemma 5.4.

Letx1<⋯<xNx_{1}<\cdots<x_{N}, letℓi​(z)=∏j≠iz−xjxi−xj,e1=∑i=1Nxi,\ell_{i}(z)=\prod_{j\neq i}\frac{z-x_{j}}{x_{i}-x_{j}},\qquad e_{1}=\sum_{i=1}^{N}x_{i},

and leta≠0a\neq 0. Then∑i=1Nℓi​(xi+a)=N,\sum_{i=1}^{N}\ell_{i}(x_{i}+a)=N,(5.13)

and∑i=1Nxi​ℓi​(xi+a)=e1+(N2)​a.\sum_{i=1}^{N}x_{i}\ell_{i}(x_{i}+a)=e_{1}+\binom{N}{2}a.(5.14)

## Proof.

The caseN=1N=1is immediate. AssumeN≥2N\geq 2, and setQ​(z)=∏i=1N(z−xi)=zN−e1​zN−1+⋯Q(z)=\prod_{i=1}^{N}(z-x_{i})=z^{N}-e_{1}z^{N-1}+\cdots

andRa​(z)=Q​(z+a)−Q​(z)a.R_{a}(z)=\frac{Q(z+a)-Q(z)}{a}.

The polynomialRaR_{a}has degree at mostN−1N-1, andRa​(xi)=Q​(xi+a)a=Q′​(xi)​ℓi​(xi+a).R_{a}(x_{i})=\frac{Q(x_{i}+a)}{a}=Q^{\prime}(x_{i})\ell_{i}(x_{i}+a).

InterpolatingRaR_{a}at the nodesxix_{i}givesRa​(z)=∑i=1NQ′​(xi)​ℓi​(xi+a)​ℓi​(z).R_{a}(z)=\sum_{i=1}^{N}Q^{\prime}(x_{i})\ell_{i}(x_{i}+a)\ell_{i}(z).

Moreover,ℓi​(z)=zN−1+(xi−e1)​zN−2+⋯Q′​(xi).\ell_{i}(z)=\frac{z^{N-1}+(x_{i}-e_{1})z^{N-2}+\cdots}{Q^{\prime}(x_{i})}.

Comparing the coefficients ofzN−1z^{N-1}yields
(5.13). Comparing those ofzN−2z^{N-2}, and
using[zN−2]​Ra​(z)=(N2)​a−(N−1)​e1,[z^{N-2}]R_{a}(z)=\binom{N}{2}a-(N-1)e_{1},

yields (5.14).
∎

A first consequence is that the total right and left jump rates are
configuration independent:∑i=1Nci+​(x)=w​N,∑i=1Nci−​(x)=w​N.\sum_{i=1}^{N}c_{i}^{+}(x)=wN,\qquad\sum_{i=1}^{N}c_{i}^{-}(x)=wN.(5.15)

In particular, the total jump rate is2​w​N2wN, so the finite-particle process
is non-explosive.

## Theorem 5.5.

For every deterministic finite initial configurationS⊂ℤS\subset\mathbb{Z}, with|S|=N|S|=N, the first two density moments satisfyμ1S​(t)=μ1S​(0),\mu_{1}^{S}(t)=\mu_{1}^{S}(0),(5.16)

andμ2S​(t)=μ2S​(0)+2​w​N2​t.\mu_{2}^{S}(t)=\mu_{2}^{S}(0)+2wN^{2}t.(5.17)

## Proof.

LetF1​(x)=∑i=1Nxi,F2​(x)=∑i=1Nxi2.F_{1}(x)=\sum_{i=1}^{N}x_{i},\qquad F_{2}(x)=\sum_{i=1}^{N}x_{i}^{2}.

Sinceci±​(x)=w​ℓi​(xi±1)c_{i}^{\pm}(x)=w\ell_{i}(x_{i}\pm 1), Lemma5.4gives(ℒ​F1)​(x)\displaystyle(\mathcal{L}F_{1})(x)=w​∑i=1N[ℓi​(xi+1)−ℓi​(xi−1)]=0.\displaystyle=w\sum_{i=1}^{N}\left[\ell_{i}(x_{i}+1)-\ell_{i}(x_{i}-1)\right]=0.

This proves (5.16).

For the second moment,(ℒ​F2)​(x)=w​∑i=1N[(2​xi+1)​ℓi​(xi+1)+(−2​xi+1)​ℓi​(xi−1)].\displaystyle(\mathcal{L}F_{2})(x)=w\sum_{i=1}^{N}\bigl[(2x_{i}+1)\ell_{i}(x_{i}+1)+(-2x_{i}+1)\ell_{i}(x_{i}-1)\bigr].

Using (5.13) and
(5.14) witha=1a=1anda=−1a=-1, the sum in
brackets is2​[∑ixi​ℓi​(xi+1)−∑ixi​ℓi​(xi−1)]+∑i[ℓi​(xi+1)+ℓi​(xi−1)]\displaystyle 2\left[\sum_{i}x_{i}\ell_{i}(x_{i}+1)-\sum_{i}x_{i}\ell_{i}(x_{i}-1)\right]+\sum_{i}\left[\ell_{i}(x_{i}+1)+\ell_{i}(x_{i}-1)\right]=2​N​(N−1)+2​N=2​N2.\displaystyle\hskip 56.9055pt=2N(N-1)+2N=2N^{2}.

Thereforeℒ​F2=2​w​N2\mathcal{L}F_{2}=2wN^{2}. Taking expectations and integrating in
time proves (5.17).
∎

The random total positionF1​(t)=∑i=1NXi​(t)F_{1}(t)=\sum_{i=1}^{N}X_{i}(t)

is therefore a martingale, not a pathwise constant. Since each jump changes it
by±1\pm 1, while the total jump rate is2​w​N2wN, its predictable quadratic
variation is2​w​N​t2wNt. For a deterministic initial configuration,Var⁡F1​(t)=2​w​N​t,Var⁡(F1​(t)N)=2​w​tN.\operatorname{Var}F_{1}(t)=2wNt,\qquad\operatorname{Var}\left(\frac{F_{1}(t)}{N}\right)=\frac{2wt}{N}.(5.18)

Thus the expected center of mass is conserved, whereas the random center of
mass diffuses.

## 5.3Exact density profile for a compact block

We now specialize the general infinite-volume density formula to the compact
blockSNS_{N}defined in (3.3). Forv∈SNv\in S_{N},
the corresponding Lagrange polynomial isℓv​(u)=∏j=1j≠vNu−jv−j=(−1)N−v(v−1)!​(N−v)!​∏j=1j≠vN(u−j).\ell_{v}(u)=\prod_{\begin{subarray}{c}j=1\\
j\neq v\end{subarray}}^{N}\frac{u-j}{v-j}=\frac{(-1)^{N-v}}{(v-1)!(N-v)!}\prod_{\begin{subarray}{c}j=1\\
j\neq v\end{subarray}}^{N}(u-j).(5.19)

Specializing
(4.5) toS=SNS=S_{N}, and writings=2​w​ts=2wt, givesρN​(x,s)=∑u∈ℤIx−u​(−s)​∑v=1NIx−v​(s)​ℓv​(u).\rho_{N}(x,s)=\sum_{u\in\mathbb{Z}}I_{x-u}(-s)\sum_{v=1}^{N}I_{x-v}(s)\ell_{v}(u).(5.20)

## Remark 5.6.

SinceIx−u​(−s)I_{x-u}(-s)is the kernel ofe−s​Be^{-sB}, equation
(5.20) may equivalently be written asρN​(x,s)=∑v=1NIx−v​(s)​(e−s​B​ℓv)​(x).\rho_{N}(x,s)=\sum_{v=1}^{N}I_{x-v}(s)\bigl(e^{-sB}\ell_{v}\bigr)(x).

Moreover, becauseB−1B-1lowers polynomial degree by at least two anddeg⁡ℓv=N−1\deg\ell_{v}=N-1, the exponential truncates:ρN​(x,s)=e−s​∑v=1NIx−v​(s)​∑k=0⌊(N−1)/2⌋(−s)kk!​[(B−1)k​ℓv]​(x).\rho_{N}(x,s)=e^{-s}\sum_{v=1}^{N}I_{x-v}(s)\sum_{k=0}^{\lfloor(N-1)/2\rfloor}\frac{(-s)^{k}}{k!}\bigl[(B-1)^{k}\ell_{v}\bigr](x).

Thus, the infinite convolution in (5.20) admits a
finite algebraic representation.

## Remark 5.7.

For the blockSN={1,…,N}S_{N}=\{1,\ldots,N\}, Theorem5.5implies that the mean position of the normalized density profile is conserved
and equal tox¯N=N+12.\bar{x}_{N}=\frac{N+1}{2}.

Its variance is thereforeσN2​(t):=1N​∑x∈ℤ(x−x¯N)2​ρN​(x,t)=N2−112+2​w​N​t.\sigma_{N}^{2}(t):=\frac{1}{N}\sum_{x\in\mathbb{Z}}(x-\bar{x}_{N})^{2}\rho_{N}(x,t)=\frac{N^{2}-1}{12}+2wNt.(5.21)

Thus, the squared width grows linearly at ratedd​t​σN2​(t)=2​w​N.\frac{d}{dt}\sigma_{N}^{2}(t)=2wN.

This describes the spreading of the normalized one-point density and should
not be confused with the fluctuations of the random center of mass, whose
diffusion coefficient isw/Nw/N.

## 5.4Explicit centered moments

The block is invariant under reflection aboutx¯N=N+12.\bar{x}_{N}=\frac{N+1}{2}.

We therefore introduce the centered momentsμn(N)​(s)=∑x∈ℤ(x−x¯N)n​ρN​(x,s).\mu_{n}^{(N)}(s)=\sum_{x\in\mathbb{Z}}(x-\bar{x}_{N})^{n}\rho_{N}(x,s).(5.22)

All odd centered moments vanish. This definition applies to both even and oddNN; for evenNN, the translated lattice consists of half-integers.
Theorem5.3applies without change after
translation, withXXreplaced by multiplication by the centered coordinate.

For the second moment,(X+s​D)2=X2+s​(X​D+D​X)+s2​D2.(X+sD)^{2}=X^{2}+s(XD+DX)+s^{2}D^{2}.

The operatorD2D^{2}strictly lowers degree and has zero trace. Moreover,D​xm=m​xm−1+terms of degree at most​m−3,Dx^{m}=mx^{m-1}+\text{terms of degree at most }m-3,

so the diagonal coefficients ofX​DXDandD​XDXonxmx^{m}aremmandm+1m+1, respectively. HenceTr𝒱N⁡(X​D+D​X)=∑m=0N−1(2​m+1)=N2.\operatorname{Tr}_{\mathcal{V}_{N}}(XD+DX)=\sum_{m=0}^{N-1}(2m+1)=N^{2}.

Together with the initial centered moment, this givesμ2(N)​(s)=N​(N2−1)12+N2​s.\mu_{2}^{(N)}(s)=\frac{N(N^{2}-1)}{12}+N^{2}s.(5.23)

The next two even moments areμ4(N)​(s)=\displaystyle\mu_{4}^{(N)}(s)={}N​(3​N4−10​N2+7)240+N2​(N2+1)2​s+N​(2​N2+1)​s2,\displaystyle\frac{N(3N^{4}-10N^{2}+7)}{240}+\frac{N^{2}(N^{2}+1)}{2}s+N(2N^{2}+1)s^{2},(5.24)

andμ6(N)​(s)=\displaystyle\mu_{6}^{(N)}(s)={}N​(N2−1)​(3​N4−18​N2+31)1344\displaystyle\frac{N(N^{2}-1)(3N^{4}-18N^{2}+31)}{1344}(5.25)+N2​(N2+3)​(3​N2+1)16​s\displaystyle+\frac{N^{2}(N^{2}+3)(3N^{2}+1)}{16}s+N​(9​N4+40​N2+11)4​s2+5​N2​(N2+2)​s3.\displaystyle+\frac{N(9N^{4}+40N^{2}+11)}{4}s^{2}+5N^{2}(N^{2}+2)s^{3}.

These expressions follow by expanding the finite-dimensional trace in
(5.11). In particular,[s]​μ2(N)​(s)=N2,[s2]​μ4(N)​(s)=2​N3+N,[s3]​μ6(N)​(s)=5​N4+10​N2.[s]\mu_{2}^{(N)}(s)=N^{2},\qquad[s^{2}]\mu_{4}^{(N)}(s)=2N^{3}+N,\qquad[s^{3}]\mu_{6}^{(N)}(s)=5N^{4}+10N^{2}.(5.26)

The coefficients1,2,51,2,5are the leading large-NNcoefficients of these
highest-time terms, rather than the exact coefficients themselves.

## 5.5Universal leading coefficients and Catalan numbers

In the following proposition, we show that for the even moments, the coefficient of the maximal power of time
depends only on the number of particles and not on their initial positions. In addition, these coefficients are given by the Catalan numbers.

## Proposition 5.8.

LetS⊂ℤS\subset\mathbb{Z}be any deterministic set with|S|=N|S|=N. For fixedr≥1r\geq 1, the coefficientκr,N:=[sr]​μ2​rS​(s)\kappa_{r,N}:=[s^{r}]\mu_{2r}^{S}(s)

is independent ofSS, andκr,N=Cr​Nr+1+Or​(Nr−1),Cr=1r+1​(2​rr).\kappa_{r,N}=C_{r}N^{r+1}+O_{r}(N^{r-1}),\qquad C_{r}=\frac{1}{r+1}\binom{2r}{r}.(5.27)

## Proof.

By Theorem5.3, the coefficient ofsrs^{r}is a sum over all balanced words of length2​r2r, containingrrlettersXXandrrlettersDD. Let𝒲r\mathcal{W}_{r}denote this set.
A balanced word maps every monomialxmx^{m}, withm<Nm<N, to a polynomial of
degree at mostmm. Its image therefore belongs to𝒱N\mathcal{V}_{N}, andPSP_{S}acts as the identity. Consequently,κr,N=∑W∈𝒲rTr𝒱N⁡W,\kappa_{r,N}=\sum_{W\in\mathcal{W}_{r}}\operatorname{Tr}_{\mathcal{V}_{N}}W,(5.28)

which proves thatκr,N\kappa_{r,N}is independent ofSS.

Write a word in application order asW=A2​r​⋯​A1,Ap∈{X,D},W=A_{2r}\cdots A_{1},\qquad A_{p}\in\{X,D\},

withA1A_{1}acting first. Associate withWWa path with an up step forXXand a down step forDD. Leth1​(W),…,hr​(W)h_{1}(W),\ldots,h_{r}(W)be the heights immediately before the successive down
steps. SinceD​xm=m​xm−1+terms of degree at most​m−3,Dx^{m}=mx^{m-1}+\text{terms of degree at most }m-3,

only the leading part of everyDDcan contribute to the coefficient ofxmx^{m}inW​xmWx^{m}. Therefore the diagonal coefficient is exactly[xm]​W​xm=∏q=1r(m+hq​(W)).[x^{m}]Wx^{m}=\prod_{q=1}^{r}\bigl(m+h_{q}(W)\bigr).(5.29)

LetW←W^{\leftarrow}be the reversed word. A down step of heighthhinWWcorresponds to a down step of height1−h1-hinW←W^{\leftarrow}. Since reversal is an involution of𝒲r\mathcal{W}_{r},∑W∈𝒲r∑q=1r(hq​(W)−12)=0.\sum_{W\in\mathcal{W}_{r}}\sum_{q=1}^{r}\left(h_{q}(W)-\frac{1}{2}\right)=0.(5.30)

Expanding the exact product (5.29) aroundm+12m+\tfrac{1}{2}, and then summing over all words, gives∑W∈𝒲r∏q=1r(m+hq​(W))=(2​rr)​(m+12)r+Qr−2​(m),\sum_{W\in\mathcal{W}_{r}}\prod_{q=1}^{r}\bigl(m+h_{q}(W)\bigr)=\binom{2r}{r}\left(m+\frac{1}{2}\right)^{r}+Q_{r-2}(m),

whereQr−2Q_{r-2}is a polynomial of degree at mostr−2r-2(and is absent
whenr=1r=1). Henceκr,N=(2​rr)​∑m=0N−1(m+12)r+Or​(Nr−1).\kappa_{r,N}=\binom{2r}{r}\sum_{m=0}^{N-1}\left(m+\frac{1}{2}\right)^{r}+O_{r}(N^{r-1}).

The midpoint power sum satisfies∑m=0N−1(m+12)r=Nr+1r+1+Or​(Nr−1),\sum_{m=0}^{N-1}\left(m+\frac{1}{2}\right)^{r}=\frac{N^{r+1}}{r+1}+O_{r}(N^{r-1}),

with no term of orderNrN^{r}. This proves
(5.27).
∎

The appearance of Catalan numbers is, in fact, natural. In[23], it was shown that, after the appropriate
large-time rescaling, the density profile converges to a semicircle law.
The even moments of the semicircle distribution are precisely the Catalan
numbers, up to the normalization fixed by its support. This is also consistent
with the random-matrix interpretation of the model. Indeed, for a fixed number
of particles evolving on an infinite lattice, the density becomes dilute at
large times. In this regime, the lattice constraint becomes asymptotically
irrelevant, and the system is expected to recover the behavior of the
continuous Dyson gas.Figure 1:Euler-scale melting of the blockSN={1,…,N}S_{N}=\{1,\dots,N\}, withξ=x/N\xi=x/N,τ=t/N\tau=t/Nandw=12w=\tfrac{1}{2}.Left:phase diagram in the(ξ,τ)(\xi,\tau)plane; colour is the limiting
densityρ=1π​arg⁡u​(ξ,τ)\rho=\tfrac{1}{\pi}\arg u(\xi,\tau)(Theorem6.2),
and the red arctic curve∂ℒ\partial\mathcal{L}separates the liquid region0<ρ<10<\rho<1from the frozen phasesρ=0\rho=0(empty) andρ=1\rho=1(full). The full
tongue closes at the cusp(12,14)(\tfrac{1}{2},\tfrac{1}{4});Right:density profiles at different times. Solid curves
are the limit shape1π​arg⁡u​(ξ,τ)\tfrac{1}{\pi}\arg u(\xi,\tau); symbols are the exact
finite-lattice result (5.20) atN=20N=20.

## 6Euler-scale limit and arctic curve of a single initial block

The large-scale behavior of the SDEP was conjectured in[23]by solving the corresponding Euler-scale
conservation law. In particular, the melting of a single particle block was
studied, and the limiting density profile was expressed in terms of the roots
of a cubic equation. The nature of these roots distinguishes the liquid and
frozen regions. In this section, we recover these results directly from the
exact block-melting formula derived above, by means of a steepest-descent
analysis. The resulting phase diagram and representative density profiles are shown in
Figure1.

We fix the microscopic timescale by settingw=12,w=\frac{1}{2},

so that the scaled time2​w​t2wtcoincides with the physical timett. We
consider the Euler scalingxN=⌊ξ​N⌋,tN=τ​N,ξ∈ℝ,τ>0.x_{N}=\lfloor\xi N\rfloor,\qquad t_{N}=\tau N,\qquad\xi\in\mathbb{R},\quad\tau>0.(6.1)

For(ξ,τ)∈ℝ×(0,∞)(\xi,\tau)\in\mathbb{R}\times(0,\infty), consider the cubic equationτ​a3+(2−2​ξ−τ)​a2+(2​ξ−τ)​a+τ=0.\tau a^{3}+(2-2\xi-\tau)a^{2}+(2\xi-\tau)a+\tau=0.(6.2)

## Definition 6.1(Liquid region).

Letℒ⊂ℝ×(0,∞)\mathcal{L}\subset\mathbb{R}\times(0,\infty)be the set of points(ξ,τ)(\xi,\tau)for which (6.2) has exactly one real root and
one non-real conjugate pair. We denote byu​(ξ,τ)u(\xi,\tau)the root in the upper
half-plane and takearg⁡u​(ξ,τ)∈(0,π).\arg u(\xi,\tau)\in(0,\pi).

We can now state the main result of this section.

## Theorem 6.2(Euler-scale block profile).

LetxN=⌊ξ​N⌋x_{N}=\lfloor\xi N\rfloorandtN=τ​Nt_{N}=\tau N. If(ξ,τ)∈ℒ(\xi,\tau)\in\mathcal{L}, thenlimN→∞ρN​(xN,tN)=arg⁡u​(ξ,τ)π,\lim_{N\to\infty}\rho_{N}(x_{N},t_{N})=\frac{\arg u(\xi,\tau)}{\pi},(6.3)

whereu​(ξ,τ)u(\xi,\tau)is the upper-half-plane root of
(6.2). The convergence is uniform for(ξ,τ)(\xi,\tau)in compact subsets ofℒ\mathcal{L}.

The arctic curve is the boundary∂ℒ\partial\mathcal{L}, along which two roots
of (6.2) coalesce. Equivalently, it is given by the vanishing
of the discriminant of the cubic:(2​ξ−1)4+(4​τ2−20​τ−2)​(2​ξ−1)2−64​τ3+48​τ2−12​τ+1=0.(2\xi-1)^{4}+\bigl(4\tau^{2}-20\tau-2\bigr)(2\xi-1)^{2}-64\tau^{3}+48\tau^{2}-12\tau+1=0.(6.4)

Equation (6.4) coincides with the arctic-curve
equation obtained from the hydrodynamic description in[23], after shifting the spatial coordinate byξ↦ξ−12\xi\mapsto\xi-\frac{1}{2}to account for the different position of the
initial block. Indeed, the block considered here occupiesSN={1,…,N}S_{N}=\{1,\ldots,N\}, whereas the block in[23]is centered at the origin. The large-τ\taulimit provides a further connection with the moment analysis of the
preceding section. In this regime, the arctic boundary satisfies|ξ−12|∼2​τ,\left|\xi-\frac{1}{2}\right|\sim 2\sqrt{\tau},

and the Euler-scale density approaches the expanding semicircle profileρ​(ξ,τ)∼12​π​τ​4​τ−(ξ−12)2​1{|ξ−12|<2​τ}.\rho(\xi,\tau)\sim\frac{1}{2\pi\tau}\sqrt{4\tau-\left(\xi-\frac{1}{2}\right)^{2}}\,\mathbf{1}_{\{|\xi-\frac{1}{2}|<2\sqrt{\tau}\}}.

Equivalently,τ​ρ​(12+τ​u,τ)⟶12​π​4−u2​1{|u|<2}.\sqrt{\tau}\,\rho\left(\frac{1}{2}+\sqrt{\tau}\,u,\tau\right)\longrightarrow\frac{1}{2\pi}\sqrt{4-u^{2}}\,\mathbf{1}_{\{|u|<2\}}.

The even moments of this limiting distribution are the Catalan numbers:∫−22u2​r​4−u22​π​𝑑u=Cr.\int_{-2}^{2}u^{2r}\frac{\sqrt{4-u^{2}}}{2\pi}\,du=C_{r}.

This agrees with Proposition5.8: settingt=N​τt=N\tauandw=12w=\frac{1}{2}, its leading contribution givesμ2​rSN​(N​τ)N2​r+1∼Cr​τr.\frac{\mu_{2r}^{S_{N}}(N\tau)}{N^{2r+1}}\sim C_{r}\tau^{r}.

Thus, the universal Catalan coefficients found algebraically in the
preceding section are the moment signature of the semicircle profile
emerging from the Euler-scale solution.

## 6.1Proof of Theorem6.2

We begin by deriving an exact double-contour representation of the density.

## 6.1.1Exact double-contour representation

The exact block formula (5.20) readsρN​(x,t)=∑x′∈ℤIx−x′​(−t)​∑y=1NIx−y​(t)​∏j=1j≠yNx′−jy−j.\rho_{N}(x,t)=\sum_{x^{\prime}\in\mathbb{Z}}I_{x-x^{\prime}}(-t)\sum_{y=1}^{N}I_{x-y}(t)\prod_{\begin{subarray}{c}j=1\\
j\neq y\end{subarray}}^{N}\frac{x^{\prime}-j}{y-j}.(6.5)

We use the conventionIn​(t)=∫−ππd​q2​π​exp⁡{t​cos⁡q+i​n​q}.I_{n}(t)=\int_{-\pi}^{\pi}\frac{dq}{2\pi}\exp\{t\cos q+inq\}.(6.6)

To account for the shiftxN−1x_{N}-1appearing in the contour representation,
we setξN=xN−1N.\xi_{N}=\frac{x_{N}-1}{N}.

Fixx∈ℤx\in\mathbb{Z}andt≥0t\geq 0, and setf​(y)=Ix−y​(t),y∈SN.f(y)=I_{x-y}(t),\qquad y\in S_{N}.

LetPN−1P_{N-1}be the unique polynomial of degree at mostN−1N-1that
interpolatesffonSNS_{N}. Equivalently,PN−1​(X)=∑y=1Nf​(y)​ℓy​(X),P_{N-1}(X)=\sum_{y=1}^{N}f(y)\ell_{y}(X),

whereℓy\ell_{y}is the block Lagrange polynomial defined in
(5.19). Therefore,
(6.5) can be written asρN​(x,t)=∑x′∈ℤIx−x′​(−t)​PN−1​(x′).\rho_{N}(x,t)=\sum_{x^{\prime}\in\mathbb{Z}}I_{x-x^{\prime}}(-t)P_{N-1}(x^{\prime}).(6.7)

For consecutive nodes one has the Newton interpolation formulaPN−1​(X)=∑k=0N−1(X−1k)​(Δk​f)​(1),Δ​f​(y)=f​(y+1)−f​(y).P_{N-1}(X)=\sum_{k=0}^{N-1}\binom{X-1}{k}(\Delta^{k}f)(1),\qquad\Delta f(y)=f(y+1)-f(y).(6.8)

## Lemma 6.3(Exact double-contour formula).

Let0<r<10<r<1. For everyx∈ℤx\in\mathbb{Z}andt≥0t\geq 0,ρN​(x,t)\displaystyle\rho_{N}(x,t)=∮|ω|=1d​ω2​π​i​ω​ω−(x−1)​exp⁡{t2​(ω+ω−1)}\displaystyle=\oint_{|\omega|=1}\frac{d\omega}{2\pi i\,\omega}\omega^{-(x-1)}\exp\left\{\frac{t}{2}\left(\omega+\omega^{-1}\right)\right\}×12​π​i​∮|z−1|=rzx−1​exp⁡{−t2​(z+z−1)}z−ω​[1−(ω−1z−1)N]​𝑑z.\displaystyle\quad\times\frac{1}{2\pi i}\oint_{|z-1|=r}\frac{z^{x-1}\exp\left\{-\frac{t}{2}\left(z+z^{-1}\right)\right\}}{z-\omega}\left[1-\left(\frac{\omega-1}{z-1}\right)^{N}\right]dz.(6.9)

Both contours are positively oriented. The apparent pole atz=ωz=\omegais
removable when the two contours meet.

## Proof.

From (6.8),ρN​(x,t)=∑k=0N−1(Δk​f)​(1)​∑x′∈ℤIx−x′​(−t)​(x′−1k).\rho_{N}(x,t)=\sum_{k=0}^{N-1}(\Delta^{k}f)(1)\sum_{x^{\prime}\in\mathbb{Z}}I_{x-x^{\prime}}(-t)\binom{x^{\prime}-1}{k}.

The coefficient representation(mk)=12​π​i​∮|z−1|=rzm(z−1)k+1​𝑑z\binom{m}{k}=\frac{1}{2\pi i}\oint_{|z-1|=r}\frac{z^{m}}{(z-1)^{k+1}}\,dz

gives, using the two-sided generating function for the modified Bessel
functions,∑x′∈ℤIx−x′​(−t)​(x′−1k)=12​π​i​∮|z−1|=rzx−1​exp⁡{−t2​(z+z−1)}(z−1)k+1​𝑑z.\sum_{x^{\prime}\in\mathbb{Z}}I_{x-x^{\prime}}(-t)\binom{x^{\prime}-1}{k}=\frac{1}{2\pi i}\oint_{|z-1|=r}\frac{z^{x-1}\exp\left\{-\frac{t}{2}(z+z^{-1})\right\}}{(z-1)^{k+1}}\,dz.(6.10)

On the other hand, the Fourier representation
(6.6) gives(Δk​f)​(1)=∫−ππd​p2​π​exp⁡{t​cos⁡p+i​(x−1)​p}​(e−i​p−1)k.(\Delta^{k}f)(1)=\int_{-\pi}^{\pi}\frac{dp}{2\pi}\exp\{t\cos p+i(x-1)p\}(e^{-ip}-1)^{k}.

Puttingω=e−i​p\omega=e^{-ip}, this becomes an integral over the positively
oriented unit circle:(Δk​f)​(1)=∮|ω|=1d​ω2​π​i​ω​ω−(x−1)​exp⁡{t2​(ω+ω−1)}​(ω−1)k.(\Delta^{k}f)(1)=\oint_{|\omega|=1}\frac{d\omega}{2\pi i\,\omega}\omega^{-(x-1)}\exp\left\{\frac{t}{2}(\omega+\omega^{-1})\right\}(\omega-1)^{k}.

Inserting this and (6.10), the finite sum overkkis geometric:∑k=0N−1(ω−1)k(z−1)k+1=1z−ω​[1−(ω−1z−1)N].\sum_{k=0}^{N-1}\frac{(\omega-1)^{k}}{(z-1)^{k+1}}=\frac{1}{z-\omega}\left[1-\left(\frac{\omega-1}{z-1}\right)^{N}\right].

This proves (6.9).
∎

The first term in the square brackets in
(6.9) will cancel against a residue contribution
from the second term. This leaves a representation involving a single phase.
WriteρN=IN(A)−IN(B)\rho_{N}=I_{N}^{(A)}-I_{N}^{(B)}, whereIN(A)I_{N}^{(A)}is the contribution of11andIN(B)I_{N}^{(B)}is the contribution of((ω−1)/(z−1))N((\omega-1)/(z-1))^{N}. For fixedω\omega, the pole atz=ωz=\omegainIN(A)I_{N}^{(A)}contributes precisely whenω\omegalies inside the circle|z−1|=r|z-1|=r. The same pole appears inIN(B)I_{N}^{(B)}, with the same residue.
Consequently these two contributions cancel, and one obtainsρN​(x,t)=−KN​(x,t),\rho_{N}(x,t)=-K_{N}(x,t),(6.11)

whereKN​(x,t)\displaystyle K_{N}(x,t)=∮Γωd​ω2​π​i​1ω​ω−(x−1)​exp⁡{t2​(ω+ω−1)}​(ω−1)N\displaystyle=\oint_{\Gamma_{\omega}}\frac{d\omega}{2\pi i}\frac{1}{\omega}\omega^{-(x-1)}\exp\left\{\frac{t}{2}\left(\omega+\omega^{-1}\right)\right\}(\omega-1)^{N}×12​π​i​∮Γzzx−1​exp⁡{−t2​(z+z−1)}(z−ω)​(z−1)N​𝑑z.\displaystyle\quad\times\frac{1}{2\pi i}\oint_{\Gamma_{z}}\frac{z^{x-1}\exp\left\{-\frac{t}{2}\left(z+z^{-1}\right)\right\}}{(z-\omega)(z-1)^{N}}\,dz.(6.12)

HereΓω\Gamma_{\omega}is a positively oriented contour around0,Γz\Gamma_{z}is a positively oriented contour around11, and the two contours
are disjoint. The deformation of theω\omega-contour away from the point11is harmless because the factor(ω−1)N​Resz=1[zx−1​exp⁡{−t2​(z+z−1)}(z−ω)​(z−1)N](\omega-1)^{N}\operatorname*{Res}_{z=1}\left[\frac{z^{x-1}\exp\{-\frac{t}{2}(z+z^{-1})\}}{(z-\omega)(z-1)^{N}}\right]

is holomorphic inω\omeganear11. Indeed, writingz=1+ζz=1+\zetaandω=1+u\omega=1+u, the coefficient ofζN−1\zeta^{N-1}inuN/(ζ−u)u^{N}/(\zeta-u)is a polynomial inuu.

Under the scaling (6.1), define the finite-NNphaseΨN​(a)=τ2​(a+a−1)−ξN​log⁡a+log⁡(a−1),\Psi_{N}(a)=\frac{\tau}{2}\left(a+a^{-1}\right)-\xi_{N}\log a+\log(a-1),(6.13)

and the limiting phaseΨξ,τ​(a)=τ2​(a+a−1)−ξ​log⁡a+log⁡(a−1).\Psi_{\xi,\tau}(a)=\frac{\tau}{2}\left(a+a^{-1}\right)-\xi\log a+\log(a-1).(6.14)

The logarithms are chosen continuously along each contour segment. Since the
integrands contain only integer powers, the expressions are single-valued; the
real part ofΨξ,τ\Psi_{\xi,\tau}is independent of these choices. With this
notation, (6.12) becomesKN​(xN,tN)=∮Γωd​ω2​π​i​eN​ΨN​(ω)​12​π​i​∮Γze−N​ΨN​(z)ω​(z−ω)​𝑑z.K_{N}(x_{N},t_{N})=\oint_{\Gamma_{\omega}}\frac{d\omega}{2\pi i}e^{N\Psi_{N}(\omega)}\frac{1}{2\pi i}\oint_{\Gamma_{z}}\frac{e^{-N\Psi_{N}(z)}}{\omega(z-\omega)}\,dz.(6.15)

## 6.1.2Critical points and steepest-descent contours

The critical points of the limiting phase satisfyΨξ,τ′​(a)=τ2​(1−a−2)−ξa+1a−1=0.\Psi^{\prime}_{\xi,\tau}(a)=\frac{\tau}{2}\left(1-a^{-2}\right)-\frac{\xi}{a}+\frac{1}{a-1}=0.

After clearing denominators, this is precisely the cubic equation
(6.2) introduced above. Thus, for(ξ,τ)∈ℒ(\xi,\tau)\in\mathcal{L}, the phase has one real critical point and the
non-real conjugate pairu​(ξ,τ),u​(ξ,τ)¯.u(\xi,\tau),\qquad\overline{u(\xi,\tau)}.

The contour deformation underlying the asymptotic analysis is illustrated in Figure2.
For(ξ,τ)∈ℒ(\xi,\tau)\in\mathcal{L}, the two non-real critical points are
non-degenerate. On compact subsets ofℒ\mathcal{L}, the saddles remain a
positive distance away from each other and from the singularities0and11. The following standard steepest-descent statement is the analytic input
needed below.

## Lemma 6.4.

LetD⋐ℒD\Subset\mathcal{L}. Uniformly for(ξ,τ)∈D(\xi,\tau)\in D, the contoursΓω\Gamma_{\omega}andΓz\Gamma_{z}in (6.15) can be
deformed to contoursΓ~ω\widetilde{\Gamma}_{\omega}andΓ~z\widetilde{\Gamma}_{z}with the following properties.
There is an oriented curveΣ\Sigma, fromu​(ξ,τ)¯\overline{u(\xi,\tau)}tou​(ξ,τ)u(\xi,\tau), along which the two deformed contours cross once. After the
crossing contribution alongΣ\Sigmais removed, the remaining double integralK~N\widetilde{K}_{N}satisfiesK~N=O​(N−1/2)\widetilde{K}_{N}=O(N^{-1/2})(6.16)

uniformly for(ξ,τ)∈D(\xi,\tau)\in D.

## Proof.

This is the usual two-contour steepest-descent construction for a pair of
conjugate non-degenerate saddles. Thezz-contour is deformed through the
saddles along steepest-ascent directions forℜ⁡Ψξ,τ\Re\Psi_{\xi,\tau}, while theω\omega-contour is deformed through the same saddles along steepest-descent
directions. The two deformed contours cross along the level lineΣ\Sigmaconnectingu¯\bar{u}touu. SinceD⋐ℒD\Subset\mathcal{L}, the saddles are
uniformly non-degenerate and stay away from0and11, so the contours and
all estimates can be chosen uniformly in(ξ,τ)∈D(\xi,\tau)\in D.

Away from small neighborhoods of the saddles there is a uniformδ>0\delta>0such thatℜ⁡(Ψξ,τ​(ω)−Ψξ,τ​(z))≤−δ.\Re\bigl(\Psi_{\xi,\tau}(\omega)-\Psi_{\xi,\tau}(z)\bigr)\leq-\delta.

Those parts of the double integral are exponentially small. Near each saddle,
a quadratic expansion gives, in suitable local coordinates,ℜ⁡(Ψξ,τ​(ω)−Ψξ,τ​(z))≤−c​(|ω−u|2+|z−u|2),\Re\bigl(\Psi_{\xi,\tau}(\omega)-\Psi_{\xi,\tau}(z)\bigr)\leq-c\bigl(|\omega-u|^{2}+|z-u|^{2}\bigr),

and similarly nearu¯\bar{u}, withc>0c>0uniform onDD. After the pole
crossing atz=ωz=\omegahas been extracted, the remaining local integral is
bounded by the corresponding Gaussian estimate, giving (6.16).
The replacement ofΨN\Psi_{N}byΨξ,τ\Psi_{\xi,\tau}changes these estimates only
byo​(1)o(1), uniformly onDD, because(ξN,τ)→(ξ,τ)(\xi_{N},\tau)\to(\xi,\tau).
∎

## 6.1.3Completion of the proof

## Proof of Theorem6.2.

Start from the exact representation (6.15).

Start from the exact representation (6.15). Deform the
two contours as in Lemma6.4. During this
deformation, the pole atz=ωz=\omegais crossed once along the curveΣ\Sigma. WithΣ\Sigmaoriented fromu¯\bar{u}touu, the residue of1/[ω​(z−ω)]1/[\omega(z-\omega)]givesK~N=KN+∫Σd​ω2​π​i​ω.\widetilde{K}_{N}=K_{N}+\int_{\Sigma}\frac{d\omega}{2\pi i\,\omega}.(6.17)

Along the crossing term the exponential factors cancel, sinceeN​ΨN​(ω)​e−N​ΨN​(ω)=1e^{N\Psi_{N}(\omega)}e^{-N\Psi_{N}(\omega)}=1.

The curveΣ\Sigmais chosen with zero winding around the origin, so∫Σd​ω2​π​i​ω=arg⁡u​(ξ,τ)π.\int_{\Sigma}\frac{d\omega}{2\pi i\,\omega}=\frac{\arg u(\xi,\tau)}{\pi}.(6.18)

Indeed, any continuous branch of the logarithm alongΣ\Sigmahas endpoint
arguments−arg⁡u-\arg uandarg⁡u\arg u. Lemma6.4therefore impliesK~N→0\widetilde{K}_{N}\to 0, uniformly on compact subsets ofℒ\mathcal{L}. HenceKN⟶−arg⁡u​(ξ,τ)π.K_{N}\longrightarrow-\frac{\arg u(\xi,\tau)}{\pi}.

Together withρN=−KN\rho_{N}=-K_{N}, as given by
(6.11), this proves
(6.3).
∎

## Remark 6.5(Frozen regions).

At the boundary ofℒ\mathcal{L}, the conjugate pair of roots collides on the
real axis. When the limiting root lies on the positive real axis, the anglearg⁡u\arg utends to0, and the limiting density tends to0. When it lies
on the negative real axis,arg⁡u\arg utends toπ\pi, and the limiting density
tends to11. These are the two frozen phases adjacent to the liquid region.Figure 2:Steepest-descent geometry for the phaseΨξ,τ\Psi_{\xi,\tau}, shown for a
representative point(ξ,τ)(\xi,\tau)in the liquid region. Left: level
curves ofℜ⁡Ψξ,τ\Re\Psi_{\xi,\tau}. The thick purple curve is the equal-height
locus through the relevant critical point, while dashed curves indicate
ascent and descent directions. Right: deformation of the original contours
to the steepest-descent contoursΓ~ω\widetilde{\Gamma}_{\omega}andΓ~z\widetilde{\Gamma}_{z}. The Euler-scale density is produced by the crossing
of these deformed contours.

## 7Conclusion

We have shown that the relaxation of the SDEP from deterministic initial
conditions can be described explicitly by combining the Doob-transform structure
of the process with the free-fermion representation of the XX chain. This leads
to a mixed determinantal kernel and reduces the computation of the density to a
finite interpolation problem. For arbitrary deterministic finite initial conditions, the resulting formulas
give a closed finite-dimensional algebra for all one-body density moments and a
universal Catalan pattern in their highest-time coefficients. For block initial
conditions, they additionally give a genuinely finite representation of the
melting profile and an enhanced one-body spreading coefficient.

A main outcome of the analysis is the derivation of the Euler-scale profile for
the evolution of a single block. This profile agrees with the one predicted by
the conjectured hydrodynamic description of Ref.[23]. The present work
, therefore, provides an exact microscopic verification of that hydrodynamic
picture in a non-trivial deterministic setting.

It would be interesting to
extend the method developed here to arbitrary deterministic initial conditions,
where the interpolation kernel is still explicit, but the asymptotic analysis is
expected to be more involved.
Another natural direction is the study of fluctuations around the deterministic hydrodynamic profile. In the liquid bulk, the dilute regime connects the SDEP to the continuous Dyson gas and to the non-local macroscopic fluctuation theory developed in[40]. Its saddle-point action can be related, up to boundary terms, to an imaginary-time hydrodynamic action, providing a possible route to density and current large deviations. A natural next step is to extend this approach to the lattice regime, where finite-density effects can no longer be neglected.

## Acknowledgments

A.Z. thanks Dmitry Gangardt, Yasser Bezzaz, and Maksims Arzamasovs for
helpful discussions and for their hospitality at the University of
Birmingham. This work was funded by the ANR-PRME Uniopen project
(ANR-22-CE30-0004-01) and by FCT (Portugal) through project
UIDB/04459/2020 (doi:10.54499/UIDB/04459/2020) and grants
2020.03953.CEECIND and 2022.09232.PTDC.

## References
- [1]H. Spohn,Large Scale Dynamics of Interacting Particles,
Springer, Berlin/Heidelberg (1991),
doi:10.1007/978-3-642-84371-6.
- [2]C. Kipnis and C. Landim,Scaling Limits of Interacting Particle Systems,
Grundlehren der mathematischen Wissenschaften320, Springer,
Berlin/Heidelberg (1999),
doi:10.1007/978-3-662-03752-2.
- [3]T. M. Liggett,Continuous Time Markov Processes: An Introduction,
Graduate Studies in Mathematics113, American Mathematical Society,
Providence, RI (2010),
doi:10.1090/gsm/113.
- [4]G. M. Schütz,Exact solution of the master equation for the asymmetric exclusion
process,
J. Stat. Phys.88, 427 (1997),
doi:10.1007/BF02508478.
- [5]G. M. Schütz,Exactly Solvable Models for Many-Body Systems Far from Equilibrium,
inPhase Transitions and Critical Phenomena, vol. 19, Academic Press,
London (2001),
doi:10.1016/S1062-7901(01)80015-X.
- [6]K. Johansson,Shape fluctuations and random matrices,
Commun. Math. Phys.209, 437 (2000).
- [7]A. Borodin, P. L. Ferrari, M. Prähofer and T. Sasamoto,Fluctuation properties of the TASEP with periodic initial configuration,
J. Stat. Phys.129, 1055 (2007),
doi:10.1007/s10955-007-9383-0.
- [8]T. Imamura, M. Mucciconi and T. Sasamoto,New approach to KPZ models through free fermions at positive temperature,
J. Math. Phys.64, 083301 (2023),
doi:10.1063/5.0089778.
- [9]P. L. Garrido, J. L. Lebowitz, C. Maes and H. Spohn,Long-range correlations for conservative dynamics,
Phys. Rev. A42, 1954 (1990),
doi:10.1103/PhysRevA.42.1954.
- [10]T. M. Liggett,Long-range exclusion processes,
Ann. Probab.8, 861 (1980),
doi:10.1214/aop/1176994618.
- [11]E. D. Andjel and H. Guiol,Long-range exclusion processes, generator and invariant measures,
Ann. Probab.33, 2314 (2005),
doi:10.1214/009117905000000486.
- [12]P. Gonçalves and M. Jara,Density fluctuations for exclusion processes with long jumps,
Probab. Theory Relat. Fields170, 311 (2018),
doi:10.1007/s00440-017-0758-0.
- [13]V. Belitsky, N. P. N. Ngoc and G. M. Schütz,Asymmetric exclusion process with long-range interactions,
arXiv:2409.05017 (2024),
doi:10.48550/arXiv.2409.05017.
- [14]H. Spohn,Bosonization, vicinal surfaces, and hydrodynamic fluctuation theory,
Phys. Rev. E60, 6411 (1999),
doi:10.1103/PhysRevE.60.6411.
- [15]V. Popkov, D. Simon and G. M. Schütz,ASEP on a ring conditioned on enhanced flux,
J. Stat. Mech. P10007 (2010),
doi:10.1088/1742-5468/2010/10/P10007.
- [16]G. M. Schütz,The space-time structure of extreme current and activity events in the
ASEP,
inNonlinear Mathematical Physics and Natural Hazards, Springer Proc.
Phys.163, 13 (2015),
doi:10.1007/978-3-319-14328-6_2.
- [17]F. J. Dyson,A Brownian-motion model for the eigenvalues of a random matrix,
J. Math. Phys.3, 1191 (1962),
doi:10.1063/1.1703862.
- [18]F. Calogero,Ground state of a one-dimensionalNN-body system,
J. Math. Phys.10, 2197 (1969),
doi:10.1063/1.1664821.
- [19]B. Sutherland,Exact results for a quantum many-body problem in one dimension. II,
Phys. Rev. A5, 1372 (1972),
doi:10.1103/PhysRevA.5.1372.
- [20]A. G. Abanov, E. Bettelheim and P. Wiegmann,Integrable hydrodynamics of Calogero–Sutherland model: bidirectional
Benjamin–Ono equation,
J. Phys. A: Math. Theor.42, 135201 (2009),
doi:10.1088/1751-8113/42/13/135201.
- [21]E. Lieb, T. Schultz and D. Mattis,Two soluble models of an antiferromagnetic chain,
Ann. Phys.16, 407 (1961),
doi:10.1016/0003-4916(61)90115-4.
- [22]T. Niemeijer,Some exact calculations on a chain of spins1/21/2,
Physica36, 377 (1967),
doi:10.1016/0031-8914(67)90235-2.
- [23]A. Zahra, J. Dubail and G. M. Schütz,Emergent hydrodynamics in an exclusion process with long-range
interactions,
arXiv:2508.09879 (2025),
doi:10.48550/arXiv.2508.09879.
- [24]A. G. Abanov,Hydrodynamics of correlated systems,
inApplications of Random Matrices in Physics, NATO Sci. Ser. II221, 139, Springer, Dordrecht (2006),
doi:10.1007/1-4020-4531-X_5.
- [25]R. Kenyon and A. Okounkov,Limit shapes and the complex Burgers equation,
Acta Math.199, 263 (2007),
doi:10.1007/s11511-007-0021-0.
- [26]T. Antal, Z. Rácz, A. Rákos and G. M. Schütz,Transport in the XX chain at zero temperature: emergence of flat
magnetization profiles,
Phys. Rev. E59, 4912 (1999),
doi:10.1103/PhysRevE.59.4912.
- [27]E. Bettelheim, A. G. Abanov and P. Wiegmann,Orthogonality catastrophe and shock waves in a nonequilibrium Fermi gas,
Phys. Rev. Lett.97, 246402 (2006),
doi:10.1103/PhysRevLett.97.246402.
- [28]P. Ruggiero, Y. Brun and J. Dubail,Conformal field theory on top of a breathing one-dimensional gas of hard
core bosons,
SciPost Phys.6, 051 (2019),
doi:10.21468/SciPostPhys.6.4.051.
- [29]S. Scopa, P. Calabrese and J. Dubail,Exact entanglement growth of a one-dimensional hard-core quantum gas
during a free expansion,
J. Phys. A: Math. Theor.54, 404002 (2021),
doi:10.1088/1751-8121/ac20ee.
- [30]N. Allegra, J. Dubail, J.-M. Stéphan and J. Viti,Inhomogeneous field theory inside the arctic circle,
J. Stat. Mech. 053108 (2016),
doi:10.1088/1742-5468/2016/05/053108.
- [31]V. Gorin,Lectures on Random Lozenge Tilings,
Cambridge Studies in Advanced Mathematics193, Cambridge University
Press (2021),
doi:10.1017/9781108921183.
- [32]F. Colomo and A. G. Pronko,The arctic curve of the domain-wall six-vertex model,
J. Stat. Phys.138, 662 (2010),
doi:10.1007/s10955-009-9902-2.
- [33]J.-M. Stéphan,Extreme boundary conditions and random tilings,
SciPost Phys. Lect. Notes26(2021),
doi:10.21468/SciPostPhysLectNotes.26.
- [34]P. Di Francesco and E. Guitter,The arctic curve for Aztec rectangles with defects via the tangent
method,
J. Stat. Phys.176, 624 (2019),
doi:10.1007/s10955-019-02315-2.
- [35]A. G. Abanov and F. Franchini,Emptiness formation probability for the anisotropic XY spin chain in a
magnetic field,
Phys. Lett. A316, 342 (2003),
doi:10.1016/j.physleta.2003.07.009.
- [36]J.-M. Stéphan,Emptiness formation probability, Toeplitz determinants, and conformal
field theory,
J. Stat. Mech. P05010 (2014),
doi:10.1088/1742-5468/2014/05/P05010.
- [37]J. S. Pallister, S. H. Pickering, D. M. Gangardt and A. G. Abanov,Phase transitions in full counting statistics of free fermions and
directed polymers,
Phys. Rev. Research7, L022008 (2025),
doi:10.1103/PhysRevResearch.7.L022008.
- [38]S. Andraus and M. Katori,Characterizations of the hydrodynamic limit of the Dyson model,
arXiv:1602.00449 (2016),
doi:10.48550/arXiv.1602.00449.
- [39]R. Dandekar, P. L. Krapivsky and K. Mallick,Dynamical fluctuations in the Riesz gas,
Phys. Rev. E107, 044129 (2023),
doi:10.1103/PhysRevE.107.044129.
- [40]R. Dandekar, P. L. Krapivsky and K. Mallick,Current fluctuations in the Dyson gas,
Phys. Rev. E110, 064153 (2024),
doi:10.1103/PhysRevE.110.064153.
- [41]P. L. Krapivsky and K. Mallick,Expansion into the vacuum of stochastic gases with long-range
interactions,
Phys. Rev. E111, 064109 (2025),
doi:10.1103/PhysRevE.111.064109.
- [42]J. L. Doob,Conditional Brownian motion and the boundary limits of harmonic
functions,
Bull. Soc. Math. France85, 431–458 (1957),
doi:10.24033/bsmf.1494.
- [43]S. Karlin and J. McGregor,Coincidence properties of birth and death processes,
Pacific J. Math.9, 1109–1140 (1959),
doi:10.2140/pjm.1959.9.1109.
- [44]M. Katori and H. Tanemura,Noncolliding Brownian motion and determinantal processes,
J. Stat. Phys.129, 1233–1277 (2007),
doi:10.1007/s10955-007-9421-y.
- [45]S. Scopa, P. Calabrese and J. Dubail,Exact hydrodynamic solution of a double domain wall melting in the
spin-1/21/2XXZ model,
SciPost Phys.12, 207 (2022),
doi:10.21468/SciPostPhys.12.6.207.
- [46]J. S. Pallister, D. M. Gangardt and A. G. Abanov,Limit shape phase transitions: a merger of arctic circles,
J. Phys. A: Math. Theor.55, 304001 (2022),
doi:10.1088/1751-8121/ac79ad.
- [47]G.-C. Rota, D. Kahaner and A. Odlyzko,On the foundations of combinatorial theory. VIII. Finite operator
calculus,
J. Math. Anal. Appl.42, 684–760 (1973).doi:10.1016/0022-247X(73)90172-8.
- [48]A. Dimakis, F. Müller-Hoissen and T. Striker,Umbral calculus, discretization, and quantum mechanics on a lattice,
J. Phys. A: Math. Gen.29, 6861–6876 (1996).doi:10.1088/0305-4470/29/21/017.

## 


- 


Major funding support from
