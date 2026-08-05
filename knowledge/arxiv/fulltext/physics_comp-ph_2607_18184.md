# anyakrakusuma: A Python Library for Entropic Schrödinger Bridges on Idealized Geometries

**arXiv ID**: 2607.18184v1
**Authors**: Sandy Hardian Susanto Herho, Dasapta Erwin Irawan, Agus Wahyu Jatmiko, Sito Fossy Biosa, Candrasa Surya Dharma, Edi Riawan, Astyka Pamumpuni, Rendy Dwi Kartiko, Rusmawan Suwarman, Deny Juanda Puradimaja
**Published**: 2026-07-20
**Categories**: physics.comp-ph, cs.MS, math.NA, math.OC
**Comments**: 22 pages, 4 figures, 5 tables
**HTML URL**: https://arxiv.org/html/2607.18184v1

## Abstract

We present anyakrakusuma, an open-source Python library that solves the discrete static Schrödinger bridge problem, the entropically regularized counterpart of optimal transport, through a log-domain Sinkhorn--Knopp iteration and reconstructs the entropic interpolation between two empirical point clouds. The solver is paired with a diagnostic pipeline that characterizes the optimal coupling and the intermediate distributions through information-theoretic and geometric measures. We exercise the library on four idealized planar cases spanning a circle-to-circle dilation, a spiral-to-mixture fragmentation, a rigid reorientation of two moons, and a Lissajous-to-trefoil deformation. The log-domain formulation is necessary rather than merely convenient at the parameters studied, where the cost-to-regularization ratio reaches four hundred and the Gibbs kernel underflows double precision across most of its range; the iteration nonetheless attains a marginal residual of $10^{-9}$ and unit marginal fidelity in every case. Residual histories decay geometrically over approximately eight decades at per-iteration contraction factors between $0.966$ and $0.976$, which are local rates near the fixed point that lie many orders of magnitude below the worst-case Hilbert-metric bound. The covariance analysis recovers an imposed ninety-degree reorientation to within $0.07^\circ$, roughly forty times smaller than its uncertainty, across a masked interval of near-isotropy on which the principal axis is unobservable. The diagnostics are reported with explicit attention to the regimes in which each is well defined, including the differential entropy, which is meaningful only on the open interpolation interval. The presented cases are constructed rather than measured; quantitative application to empirical point clouds requires further study.

## Full Text

anyakrakusuma: A Python Library for Entropic Schrödinger Bridges on Idealized Geometries

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.18184v1 [physics.comp-ph] 20 Jul 2026

## anyakrakusuma: A Python Library for Entropic
Schrödinger Bridges on Idealized GeometriesSandy H. S. Herho1,2,3,
Dasapta E. Irawan1,∗,
Agus W. Jatmiko4,
Sito F. Biosa5,
Candrasa S. Dharma6,
Edi Riawan7,
Astyka Pamumpuni1,
Rendy D. Kartiko1,
Rusmawan Suwarman7,
and Deny J. Puradimaja1

## Abstract

We presentanyakrakusuma, an open-source Python library
that solves the discrete static Schrödinger bridge problem, the
entropically regularized counterpart of optimal transport, through a
log-domain Sinkhorn–Knopp iteration and reconstructs the entropic
interpolation between two empirical point clouds. The solver is paired with a
diagnostic pipeline that characterizes the optimal coupling and the
intermediate distributions through information-theoretic and geometric
measures. We exercise the library on four idealized planar cases spanning a
circle-to-circle dilation, a spiral-to-mixture fragmentation, a rigid
reorientation of two moons, and a Lissajous-to-trefoil deformation. The
log-domain formulation is necessary rather than merely convenient at the
parameters studied, where the cost-to-regularization ratio reaches four
hundred and the Gibbs kernel underflows double precision across most of its
range; the iteration nonetheless attains a marginal residual of10−910^{-9}and
unit marginal fidelity in every case. Residual histories decay geometrically
over approximately eight decades at per-iteration contraction factors between0.9660.966and0.9760.976, which are local rates near the fixed point that lie many
orders of magnitude below the worst-case Hilbert-metric bound. The covariance
analysis recovers an imposed ninety-degree reorientation to within0.07∘0.07^{\circ}, roughly forty times smaller than its uncertainty, across a
masked interval of near-isotropy on which the principal axis is unobservable.
The diagnostics are reported with explicit attention to the regimes in which each is well defined, including the differential entropy, which is meaningful only on the open interpolation interval. The presented cases are constructed rather than measured; quantitative application to empirical point clouds requires further study.

1Applied Geology Research Group, Bandung Institute of
Technology, Bandung, West Java 40132, Indonesia
2Department of Earth and Planetary Sciences, University of
California, Riverside, CA 92521, USA
3Center for Agrarian Studies, Bandung Institute of Technology,
Bandung, West Java 40132, Indonesia
4Headquarters of the Indonesian Air Force (Mabes TNI AU),
Cilangkap, East Jakarta 13870, Indonesia
5Department of Visual Communication Design – Animation, BINUS
University, West Jakarta 11480, Indonesia
6Indonesian Navy Hydro-Oceanography Center (Pushidrosal), Ancol
Timur, North Jakarta 14430, Indonesia
7Atmospheric Science Research Group, Bandung Institute of
Technology, Bandung, West Java 40132, Indonesia
∗Corresponding Author:dasaptaerwin@itb.ac.id

Keywords:entropic optimal transport; information-theoretic diagnostics;
log-domain Sinkhorn algorithm; Python scientific software;
Schrödinger bridge problem.

## 1Introduction

The Schrödinger bridge problem asks for the most likely evolution of a
cloud of particles between two observed distributions, given a reference
stochastic dynamics, and was posed in its original form as a question about
the statistical behavior of diffusing particles conditioned on their initial
and final states[35,36]. In modern terms the
problem is an entropy-minimizing interpolation on path space, and it is now
understood to be the stochastic, entropically regularized counterpart of the
optimal transport problem, to which it reduces in the vanishing-noise limit[28,5]. This correspondence has placed the Schrödinger
bridge at the intersection of probability, statistical mechanics, and
computational mathematics, where it supplies a principled way to connect two
empirical states through a dynamics that is neither purely deterministic nor
purely diffusive[11,41].

Interest in the problem has grown with the recognition that its discrete
static form is solved by the same matrix-scaling iteration that underlies
entropic optimal transport. The introduction of an entropic penalty renders
the transport problem strictly convex and solvable by the Sinkhorn–Knopp
iteration at a cost far below that of the underlying linear program[7,40], and the same machinery, together with its
Bregman-projection and stabilized-scaling refinements, now forms the standard
computational backbone for entropic transport[31,1,34]. The resulting framework has
been carried well beyond its origins, from the continuous-state generative
models that treat the bridge as the finite-time analogue of a diffusion[8]to applications across the physical and data sciences
where two snapshots of a system must be joined by a plausible intervening
process. The breadth of this adoption has made the quality and transparency of
the underlying solvers a matter of practical consequence.

That breadth has not been matched by a corresponding supply of reusable,
well-documented scientific software. Implementations of the entropic bridge
are frequently embedded within larger machine-learning pipelines, tuned to a
single application, and released without the archival data formats,
reproducible configurations, or standardized diagnostics that characterize
mature community codes in adjacent computational fields. A researcher who
wishes to study the bridge itself, rather than a downstream task built upon
it, is often left to reconstruct the solver and its analysis from scratch. The
absence of a purpose-built, openly documented tool for the discrete
Schrödinger bridge, coupled with information-theoretic diagnostics and
climate-and-forecast-compliant output, impedes systematic exploration,
cross-study comparison, and reproducibility in the same way that has been
noted for other idealized-modeling communities[14,27].

A productive response to this situation has been to build compact,
single-purpose solvers whose numerical core is legible and just-in-time
compiled for research-grade throughput, and to pair each with a diagnostic
layer that quantifies the organization of the solution beyond first-moment
summaries and with self-describing output that supports archival and reuse.
Idealized solvers constructed in this manner have proven effective across a
range of physical settings, including shear-driven instability[19], collective animal motion[15], nonlinear dispersive waves[22], and wave attenuation in coastal environments[16], and the same emphasis on numerical transparency
underlies reproducibility studies across computing platforms[17,18]. Information-theoretic diagnostics
in particular have repeatedly exposed organizational structure that
order-parameter or first-moment descriptions leave hidden[15,22]. The entropic Schrödinger
bridge is a natural setting for the same treatment, since its coupling and its
intermediate distributions carry precisely the kind of structure that such
diagnostics are designed to measure.

This paper presentsanyakrakusuma, an open-sourcePythonlibrary that solves the discrete static Schrödinger bridge problem through
a log-domain Sinkhorn–Knopp iteration and reconstructs the entropic
interpolation between two empirical point clouds, together with a diagnostic
pipeline that characterizes the coupling and the intermediate distributions
through information-theoretic and geometric measures. The solver and its
diagnostics are exercised on four idealized planar cases, chosen to span a
circle-to-circle dilation, a spiral-to-mixture fragmentation, a rigid
reorientation of two moons, and a Lissajous-to-trefoil deformation, which
between them probe convergence, the structure of the optimal coupling, the
evolution of the intermediate density, and the informational and geometric
descriptors of the bridge. Consistent with the aim of providing a verified
computational foundation rather than an application to measured data, the four
cases are constructed rather than observed, and the diagnostics are reported
with explicit attention to the regimes in which each is well defined. The
mathematical formulation and numerical implementation are developed first,
followed by the four demonstration cases, their diagnostic analysis, and a
discussion of the results and their limitations.

## 2Methods

## 2.1Model Description

The problem treated in this work was first formulated by Erwin Schrödinger
in two papers in the early 1930s[35,36].
Consider an ensemble of independent Brownian particles whose spatial
distribution is recorded at two distinct instants in time, and suppose that
the recorded distributions are mutually inconsistent with free diffusion.
Schrödinger’s problem is to identify the most likely evolution of the
ensemble between the two observations. Modern probabilistic and analytical
treatments have made the question precise and have shown that its resolution
coincides with the solution of an entropy-regularized version of the
Monge–Kantorovich optimal transport
problem[28,5,31]. The following
development establishes the correspondence in three stages. A path-space
formulation grounded in the relative entropy of measures reduces to a
coupling problem on the product of the endpoint spaces, and the resulting
variational problem is then cast in the finite-dimensional form that governs
the discrete computation.

Letd∈ℕd\in\mathbb{N}denote the spatial dimension andε>0\varepsilon>0a
fixed positive parameter. Consider independent particles diffusing inℝd\mathbb{R}^{d}on the unit time intervalt∈[0,1]t\in[0,1]according to the
stochastic differential equationd​Xt=ε​d​Wt,X0∼ρ0,\mathrm{d}X_{t}\;=\;\sqrt{\varepsilon}\,\mathrm{d}W_{t},\qquad X_{0}\,\sim\,\rho_{0},(1)

whereXt∈ℝdX_{t}\in\mathbb{R}^{d}is the particle position at timett,WtW_{t}is
a standarddd-dimensional Wiener process, andρ0:ℝd→ℝ≥0\rho_{0}:\mathbb{R}^{d}\to\mathbb{R}_{\geq 0}is the prescribed probability density of the initial
position. The parameterε\varepsilonplays the role of a diffusivity.
Throughout what follows,Ω:=C​([0,1];ℝd)\Omega:=C([0,1];\mathbb{R}^{d})denotes the
space of continuous pathsω:[0,1]→ℝd\omega:[0,1]\to\mathbb{R}^{d}, equipped with
the supremum norm, and𝒫​(Ω)\mathcal{P}(\Omega)denotes the Borel probability
measures onΩ\Omega. The reference path measureR∈𝒫​(Ω)R\in\mathcal{P}(\Omega)is the law of the diffusion (1), that is, the joint
distribution of the random trajectory{Xt}t∈[0,1]\{X_{t}\}_{t\in[0,1]}. For a pathω∈Ω\omega\in\Omegaand a timet∈[0,1]t\in[0,1],ωt∈ℝd\omega_{t}\in\mathbb{R}^{d}denotes the position at timett.

Suppose that at the terminal timet=1t=1a second densityρ1:ℝd→ℝ≥0\rho_{1}:\mathbb{R}^{d}\to\mathbb{R}_{\geq 0}is observed, and thatρ1\rho_{1}does not
match the one-time marginal ofX1X_{1}predicted by (1).
Schrödinger’s problem selects the path measureP⋆P^{\star}closest toRRin
relative entropy among those whose endpoint marginals are exactly(ρ0,ρ1)(\rho_{0},\rho_{1})[28,5],P⋆=arg​minP∈Π​(ρ0,ρ1)KL​(P∥R).P^{\star}\;=\;\mathop{\mathrm{arg\,min}}_{P\,\in\,\Pi(\rho_{0},\rho_{1})}\;\mathrm{KL}\!\left(P\,\|\,R\right).(2)

HereΠ​(ρ0,ρ1)⊂𝒫​(Ω)\Pi(\rho_{0},\rho_{1})\subset\mathcal{P}(\Omega)is the set of path
measures whose endpoint pushforwards match the prescribed marginals,Π​(ρ0,ρ1)={P∈𝒫​(Ω):P∘ω0−1=ρ0,P∘ω1−1=ρ1},\Pi(\rho_{0},\rho_{1})\;=\;\left\{P\in\mathcal{P}(\Omega)\,:\,P\circ\omega_{0}^{-1}=\rho_{0},\;P\circ\omega_{1}^{-1}=\rho_{1}\right\},(3)

andKL​(P∥R)\mathrm{KL}(P\,\|\,R)is the Kullback–Leibler (KL) divergence,KL​(P∥R)=∫Ωlog⁡(d​Pd​R​(ω))​dP​(ω),\mathrm{KL}\!\left(P\,\|\,R\right)\;=\;\int_{\Omega}\log\!\left(\frac{\mathrm{d}P}{\mathrm{d}R}(\omega)\right)\,\mathrm{d}P(\omega),(4)

defined wheneverPPis absolutely continuous with respect toRR, withd​P/d​R\mathrm{d}P/\mathrm{d}Rthe Radon–Nikodym derivative, and as+∞+\inftyotherwise[26]. The minimizerP⋆P^{\star}, when it exists,
admits an interpretation through the theory of large deviations as the most
likely empirical distribution of a large collection of independent
trajectories of (1), conditional on the empirical
endpoint marginals matching(ρ0,ρ1)(\rho_{0},\rho_{1})[11].

The problem stated in (2) is posed on the
infinite-dimensional path spaceΩ\Omega, and its direct discretization is
neither obvious nor efficient. A classical reduction lowers the problem to
one posed on the product of the endpoint spaces. LetR0,1∈𝒫​(ℝd×ℝd)R_{0,1}\in\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d})denote the joint law of the
endpoints(ω0,ω1)(\omega_{0},\omega_{1})underRR. For the
diffusion (1), the transition density is the Gaussian
heat kernel at time one, soR0,1R_{0,1}admits the explicit factorizationR0,1​(d​x,d​y)=ρ0​(x)​kε​(x,y)​d​x​d​y,kε​(x,y)=(2​π​ε)−d/2​exp⁡(−‖x−y‖22​ε),R_{0,1}(\mathrm{d}x,\mathrm{d}y)\;=\;\rho_{0}(x)\,k_{\varepsilon}(x,y)\,\mathrm{d}x\,\mathrm{d}y,\qquad k_{\varepsilon}(x,y)\;=\;(2\pi\varepsilon)^{-d/2}\,\exp\!\left(-\frac{\|x-y\|^{2}}{2\varepsilon}\right),(5)

wherex,y∈ℝdx,y\in\mathbb{R}^{d}are the endpoint positions,∥⋅∥\|\cdot\|denotes the Euclidean norm onℝd\mathbb{R}^{d}, andkεk_{\varepsilon}is the
density ofX1X_{1}givenX0=xX_{0}=xunder the reference dynamics. Any path
measureP∈𝒫​(Ω)P\in\mathcal{P}(\Omega)admits a unique disintegration into its
endpoint marginalπ∈𝒫​(ℝd×ℝd)\pi\in\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}),
defined byπ​(d​x,d​y)=P​(ω0∈d​x,ω1∈d​y),\pi(\mathrm{d}x,\mathrm{d}y)\;=\;P\!\left(\omega_{0}\in\mathrm{d}x,\;\omega_{1}\in\mathrm{d}y\right),(6)

together with the family of conditional path measuresPx,y(⋅)=P(⋅|ω0=x,ω1=y),(x,y)∈ℝd×ℝd.P^{x,y}(\cdot)\;=\;P\!\left(\,\cdot\;\big|\;\omega_{0}=x,\;\omega_{1}=y\right),\qquad(x,y)\in\mathbb{R}^{d}\times\mathbb{R}^{d}.(7)

The analogous disintegration ofRRproduces the conditional family{Rx,y}\{R^{x,y}\}, in whichRx,yR^{x,y}is the law of the Brownian bridge of
diffusivityε\varepsilonon[0,1][0,1]that starts atxxand ends atyy[11]. The chain rule for relative entropy then yields the
additive decomposition[28]KL​(P∥R)=KL​(π∥R0,1)+∫ℝd×ℝdKL​(Px,y∥Rx,y)​π​(d​x,d​y).\mathrm{KL}\!\left(P\,\|\,R\right)\;=\;\mathrm{KL}\!\left(\pi\,\|\,R_{0,1}\right)\;+\;\int_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\mathrm{KL}\!\left(P^{x,y}\,\|\,R^{x,y}\right)\,\pi(\mathrm{d}x,\mathrm{d}y).(8)

The two terms on the right of (8) are coupled only
through the marginalπ\pi, and the second term is minimized term by term
in(x,y)(x,y)by setting the conditional law to its reference valueP⋆,x,y=Rx,yP^{\star,x,y}=R^{x,y}. The minimization in (2)
therefore reduces to a problem for the endpoint coupling alone,π⋆=arg​minπ∈Π​(ρ0,ρ1)KL​(π∥R0,1),\pi^{\star}\;=\;\mathop{\mathrm{arg\,min}}_{\pi\,\in\,\Pi(\rho_{0},\rho_{1})}\;\mathrm{KL}\!\left(\pi\,\|\,R_{0,1}\right),(9)

whereΠ​(ρ0,ρ1)\Pi(\rho_{0},\rho_{1})now denotes the set of probability measures on
the product spaceℝd×ℝd\mathbb{R}^{d}\times\mathbb{R}^{d}whose first and second
marginals equalρ0\rho_{0}andρ1\rho_{1}, respectively. The original dynamic
problem is recovered fromπ⋆\pi^{\star}by gluing the Brownian bridge lawsRx,yR^{x,y}along the optimal endpoint coupling.

Substituting the explicit form ofR0,1R_{0,1}from (5) into the relative entropy
in (9) and discarding constants that do not depend onπ\piproducesπ⋆=arg​minπ∈Π​(ρ0,ρ1)∫ℝd×ℝd‖x−y‖22​dπ​(x,y)+ε​KL​(π∥ρ0⊗ρ1),\pi^{\star}\;=\;\mathop{\mathrm{arg\,min}}_{\pi\,\in\,\Pi(\rho_{0},\rho_{1})}\;\int_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\frac{\|x-y\|^{2}}{2}\,\mathrm{d}\pi(x,y)\;+\;\varepsilon\,\mathrm{KL}\!\left(\pi\,\|\,\rho_{0}\otimes\rho_{1}\right),(10)

whereρ0⊗ρ1\rho_{0}\otimes\rho_{1}denotes the independent product measure onℝd×ℝd\mathbb{R}^{d}\times\mathbb{R}^{d}. The functional
in (10) is the Monge–Kantorovich optimal transport
cost with quadratic ground cost, regularized by an entropic term of
strengthε\varepsilon[3,41]. Asε→0+\varepsilon\to 0^{+}, the minimizer of (10) converges to the
unregularized Wasserstein-optimal coupling, which is supported on the graph
of the Brenier map[3,30,4]. In the
opposite limitε→∞\varepsilon\to\infty, the entropic term dominates the
cost and the minimizer converges to the product measureρ0⊗ρ1\rho_{0}\otimes\rho_{1}, in which the source and target are statistically independent.

For empirical measures supported on finite point clouds, the
problem (10) becomes finite-dimensional. Letμ=∑i=1nai​δxi,ν=∑j=1mbj​δyj,\mu\;=\;\sum_{i=1}^{n}a_{i}\,\delta_{x_{i}},\qquad\nu\;=\;\sum_{j=1}^{m}b_{j}\,\delta_{y_{j}},(11)

where{xi}i=1n\{x_{i}\}_{i=1}^{n}and{yj}j=1m\{y_{j}\}_{j=1}^{m}are points inℝd\mathbb{R}^{d},δx\delta_{x}is the Dirac mass atxx, and the weight vectorsa∈ℝ>0na\in\mathbb{R}^{n}_{>0}andb∈ℝ>0mb\in\mathbb{R}^{m}_{>0}lie on the open
probability simplices, that is,∑iai=∑jbj=1\sum_{i}a_{i}=\sum_{j}b_{j}=1with all
entries positive. A coupling betweenμ\muandν\nuis represented by a
nonnegative matrixπ∈ℝ≥0n×m\pi\in\mathbb{R}^{n\times m}_{\geq 0}with entriesπi​j≥0\pi_{ij}\geq 0,i=1,…,ni=1,\ldots,n,j=1,…,mj=1,\ldots,m, interpreted as
the mass transported fromxix_{i}toyjy_{j}. Define the cost matrixC∈ℝ≥0n×mC\in\mathbb{R}^{n\times m}_{\geq 0}byCi​j=‖xi−yj‖2,C_{ij}\;=\;\|x_{i}-y_{j}\|^{2},(12)

and the transportation polytopeΠ​(a,b)={π∈ℝ≥0n×m:π​1m=a,π⊤​1n=b},\Pi(a,b)\;=\;\left\{\pi\in\mathbb{R}^{n\times m}_{\geq 0}\,:\,\pi\,\mathbf{1}_{m}=a,\;\pi^{\top}\,\mathbf{1}_{n}=b\right\},(13)

where𝟏k∈ℝk\mathbf{1}_{k}\in\mathbb{R}^{k}denotes the column vector of all
ones. The continuous problem (10) then becomes the
discrete convex programπ⋆=arg​minπ∈Π​(a,b)⟨C,π⟩F+ε​∑i=1n∑j=1mπi​j​log⁡(πi​jai​bj),\pi^{\star}\;=\;\mathop{\mathrm{arg\,min}}_{\pi\,\in\,\Pi(a,b)}\;\langle C,\pi\rangle_{F}\;+\;\varepsilon\,\sum_{i=1}^{n}\sum_{j=1}^{m}\pi_{ij}\,\log\!\left(\frac{\pi_{ij}}{a_{i}b_{j}}\right),(14)

where⟨C,π⟩F=∑i​jCi​j​πi​j\langle C,\pi\rangle_{F}=\sum_{ij}C_{ij}\,\pi_{ij}is the
Frobenius inner product ofCCandπ\pi, and the convention0​log⁡0=00\log 0=0is used. The factor of one half that appears in the quadratic cost
of (10) has been absorbed into a redefinition ofε\varepsilon, following the convention standard in the computational
entropic transport literature[31].

The convex program (14) admits a closed-form
characterization of its minimizer. Introducing Lagrange multipliersf∈ℝnf\in\mathbb{R}^{n}andg∈ℝmg\in\mathbb{R}^{m}for the row and column marginal
constraints in (13), and setting the gradient of
the Lagrangian with respect toπi​j\pi_{ij}to zero, gives the first-order
optimality conditionπi​j⋆=ai​bj​exp⁡(fi+gj−Ci​jε)=ui​Ki​j​vj,i=1,…,n,j=1,…,m,\pi^{\star}_{ij}\;=\;a_{i}\,b_{j}\,\exp\!\left(\frac{f_{i}+g_{j}-C_{ij}}{\varepsilon}\right)\;=\;u_{i}\,K_{ij}\,v_{j},\qquad i=1,\ldots,n,\;j=1,\ldots,m,(15)

where the scaling vectorsu∈ℝ>0nu\in\mathbb{R}^{n}_{>0}andv∈ℝ>0mv\in\mathbb{R}^{m}_{>0}are given byui=ai​exp⁡(fi/ε)u_{i}=a_{i}\,\exp(f_{i}/\varepsilon)andvj=bj​exp⁡(gj/ε)v_{j}=b_{j}\,\exp(g_{j}/\varepsilon), and the Gibbs kernelK∈ℝ>0n×mK\in\mathbb{R}^{n\times m}_{>0}has entriesKi​j=exp⁡(−Ci​jε).K_{ij}\;=\;\exp\!\left(-\frac{C_{ij}}{\varepsilon}\right).(16)

The matrix-scaling structureπ⋆=diag​(u)​K​diag​(v)\pi^{\star}=\mathrm{diag}(u)\,K\,\mathrm{diag}(v)has been studied since the 1960s, and the pair(u,v)(u,v)is known to exist and to be unique up to the rescaling(u,v)↦(α​u,α−1​v)(u,v)\mapsto(\alpha u,\alpha^{-1}v)forα>0\alpha>0, given that the marginal
constraints are imposed[39,40]. The discrete
scalings(u,v)(u,v)are point-cloud realizations of a pair of positive
functionsφ,ψ:ℝd×[0,1]→ℝ>0\varphi,\psi:\mathbb{R}^{d}\times[0,1]\to\mathbb{R}_{>0}that solve the coupled Schrödinger system,∂tφ​(x,t)\displaystyle\partial_{t}\varphi(x,t)\;=ε2​Δ​φ​(x,t),\displaystyle=\;\frac{\varepsilon}{2}\,\Delta\varphi(x,t),(17)∂tψ​(x,t)\displaystyle\partial_{t}\psi(x,t)\;=−ε2​Δ​ψ​(x,t),\displaystyle=\;-\frac{\varepsilon}{2}\,\Delta\psi(x,t),(18)

whereΔ=∑k=1d∂2/∂xk2\Delta=\sum_{k=1}^{d}\partial^{2}/\partial x_{k}^{2}is the Laplacian
onℝd\mathbb{R}^{d}. The intermediate-time density factors multiplicatively asρt​(x)=φ​(x,t)​ψ​(x,t)\rho_{t}(x)=\varphi(x,t)\,\psi(x,t), and the boundary conditionsφ​(⋅,0)​ψ​(⋅,0)=ρ0\varphi(\cdot,0)\,\psi(\cdot,0)=\rho_{0}andφ​(⋅,1)​ψ​(⋅,1)=ρ1\varphi(\cdot,1)\,\psi(\cdot,1)=\rho_{1}close the system at both
ends[28,5]. Equations (17)
and (18) consist of a forward heat equation forφ\varphiand a formally time-reversed heat equation forψ\psi. The
time-reversed companion distinguishes Schrödinger’s formulation from
standard parabolic theory and motivated his interest in the problem as an
analogue of quantum-mechanical probability conservation.

Reconstruction of the intermediate-time densityρt\rho_{t}fort∈(0,1)t\in(0,1)from the optimal couplingπ⋆\pi^{\star}exploits the conditional-bridge
identity established between (8)
and (9), which restores Brownian bridge dynamics on each
pair of endpoints. Conditional on(X0,X1)=(x,y)(X_{0},X_{1})=(x,y)drawn fromπ⋆\pi^{\star}, the optimal processXtX_{t}is the Brownian bridge of diffusivityε\varepsilonbetweenxxandyyon[0,1][0,1], whose marginal at timettis Gaussian,Xt|(X0=x,X1=y)∼𝒩​((1−t)​x+t​y,ε​t​(1−t)​Id),X_{t}\,\big|\,(X_{0}=x,\,X_{1}=y)\;\sim\;\mathcal{N}\!\left((1-t)\,x+t\,y,\;\varepsilon\,t(1-t)\,I_{d}\right),(19)

where𝒩​(𝝁,𝚺)\mathcal{N}(\bm{\mu},\bm{\Sigma})denotes the
multivariate normal distribution onℝd\mathbb{R}^{d}with mean vector𝝁∈ℝd\bm{\mu}\in\mathbb{R}^{d}and covariance matrix𝚺∈ℝd×d\bm{\Sigma}\in\mathbb{R}^{d\times d}, andId∈ℝd×dI_{d}\in\mathbb{R}^{d\times d}is the identity matrix[11].
Integrating (19) against the optimal coupling yields
the intermediate-time density,ρt​(z)=∫ℝd×ℝd𝒩​(z;(1−t)​x+t​y,ε​t​(1−t)​Id)​dπ⋆​(x,y),z∈ℝd,\rho_{t}(z)\;=\;\int_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\mathcal{N}\!\left(z;\;(1-t)\,x+t\,y,\;\varepsilon\,t(1-t)\,I_{d}\right)\,\mathrm{d}\pi^{\star}(x,y),\qquad z\in\mathbb{R}^{d},(20)

where𝒩​(z;𝝁,𝚺)\mathcal{N}(z;\bm{\mu},\bm{\Sigma})is the value
of the Gaussian density atzz. The varianceε​t​(1−t)\varepsilon\,t(1-t)along the bridge attains its maximumε/4\varepsilon/4att=1/2t=1/2and
vanishes at the two endpointst=0t=0andt=1t=1, so the boundary
marginalsρ0\rho_{0}andρ1\rho_{1}are recovered exactly. In the limitε→0+\varepsilon\to 0^{+}, the Gaussian kernel in (20) contracts to
a Dirac mass on the segment(1−t)​x+t​y(1-t)\,x+t\,y, and the intermediate
density reduces to theL2L^{2}-Wasserstein displacement interpolation
associated with the Brenier map[3].

Equations (1)–(20) specify the model in
full. The discrete optimal couplingπ⋆\pi^{\star}defined
in (14), the dual scaling pair(u,v)(u,v)that produces it
through (15), and the intermediate-time densityρt\rho_{t}reconstructed from (20) are the three quantities that the
formulation delivers. The parameterε\varepsilonplays a double role,
serving simultaneously as the diffusivity of the reference Brownian motion
and as the strength of the entropic regularization
in (14), with small values producing sharp couplings
that approach the unregularized optimal transport plan and large values
producing diffuse couplings that approach statistical independence between
source and target.

## 2.2Numerical Implementation

The routines that translate the discrete
formulation (14)–(20) into executable
computations are packaged as theanyakrakusumalibrary, a Python
implementation in which all inner loops are accelerated byNumbajust-in-time compilation to LLVM intermediate representation and dispatched
across CPU threads through theprangeconstruct[27], while all array storage and higher-level
operations rely onNumPy[14]. Numba compilation is
optional at import time and a pureNumPyfallback is provided for
environments in which the compiler is unavailable, at the cost of a
substantial slowdown on the inner Sinkhorn loops. All floating-point
arithmetic is performed in IEEE 754 double precision, and the just-in-time
decorators are configured with thefastmath=Trueoption, which
permits associative reordering of floating-point additions to enable
vectorization at the price of strict bitwise reproducibility across compiler
versions[13]. The associated numerical drift is not
consequential for the algorithm at hand, since the log-domain Sinkhorn
updates are themselves invariant under shifts of the potentials that far
exceed the accumulated fused-multiply-add error. The main entry point is
theSchrodingerBridgeSolverclass, which exposes the point-cloud
transport problem through asolvemethod that returns the pair(f,g)(f,g)together with the materialized plan and diagnostic quantities, and
agenerate_trajectorymethod that produces the bridge
interpolation at a uniform time grid.

The squared-Euclidean cost matrixC∈ℝ≥0n×mC\in\mathbb{R}^{n\times m}_{\geq 0}of (12) is assembled through a triply nested loop over
the source indexi∈{1,…,n}i\in\{1,\ldots,n\}, the target indexj∈{1,…,m}j\in\{1,\ldots,m\}, and the coordinate indexk∈{1,…,d}k\in\{1,\ldots,d\},Ci​j=∑k=1d(xi​k−yj​k)2,i=1,…,n,j=1,…,m,C_{ij}\;=\;\sum_{k=1}^{d}(x_{ik}-y_{jk})^{2},\qquad i=1,\ldots,n,\;j=1,\ldots,m,(21)

with the outer loop overiiparallelized throughprange. The
inner two loops are kept explicit rather than replaced by vectorized
broadcasting because Numba compiles the explicit form to tight machine code
with cache-friendly access patterns on the row-majorNumPyarrays,
avoiding the temporary allocations that a broadcasting expression would
generate. Storage forCCis preallocated as a contiguousn×mn\times mfloat64array, giving a memory footprint of8​n​m8nmbytes and a
computational cost ofO​(n​m​d)O(nmd)elementary operations for the assembly.

The Sinkhorn iterations that solve (14) are executed in
the logarithmic domain, replacing the exponential-domain scalingsuiu_{i}andvjv_{j}of (15) by the dual potentialsfi=ε​log⁡ui,gj=ε​log⁡vj,i=1,…,n,j=1,…,m.f_{i}\;=\;\varepsilon\,\log u_{i},\qquad g_{j}\;=\;\varepsilon\,\log v_{j},\qquad i=1,\ldots,n,\;j=1,\ldots,m.(22)

Working with(f,g)(f,g)rather than(u,v)(u,v)removes the risk of underflow
or overflow whenε\varepsilonis small relative to the range ofCi​jC_{ij},
a regime in which the Gibbs kernel entriesKi​j=exp⁡(−Ci​j/ε)K_{ij}=\exp(-C_{ij}/\varepsilon)of (16) can lie many decades
below the smallest representable double-precision number. The log-domain
formulation and its stabilized variants have become standard practice for
entropic transport at small regularization, both in the balanced setting
treated here[34,31]and in the more general
scaling framework developed for unbalanced and multi-marginal
extensions[6,1]. The load-bearing primitive is
the numerically stable log-sum-exp (LSE) evaluated with the max-trick,LSE​(z1,…,zL)=zmax+log​∑ℓ=1Lexp⁡(zℓ−zmax),zmax=maxℓ⁡zℓ,\mathrm{LSE}(z_{1},\ldots,z_{L})\;=\;z_{\max}\;+\;\log\sum_{\ell=1}^{L}\exp(z_{\ell}-z_{\max}),\qquad z_{\max}\;=\;\max_{\ell}z_{\ell},(23)

implemented as a self-contained Numba-compiled routine with a special-case
branch that returnszmaxz_{\max}directly whenever the maximum is infinite,
so that empty softmin evaluations do not propagateNaNthrough
the subsequent arithmetic.

In terms of(f,g)(f,g)and the KL optimality conditions
produced by (14), one full Sinkhorn sweep amounts to the
pair of updatesfi(k+1)\displaystyle f_{i}^{(k+1)}\;=ε​log⁡ai−ε​LSEj​(gj(k)−Ci​jε),i=1,…,n,\displaystyle=\;\varepsilon\,\log a_{i}\;-\;\varepsilon\,\mathrm{LSE}_{j}\!\left(\frac{g_{j}^{(k)}-C_{ij}}{\varepsilon}\right),\qquad i=1,\ldots,n,(24)gj(k+1)\displaystyle g_{j}^{(k+1)}\;=ε​log⁡bj−ε​LSEi​(fi(k+1)−Ci​jε),j=1,…,m,\displaystyle=\;\varepsilon\,\log b_{j}\;-\;\varepsilon\,\mathrm{LSE}_{i}\!\left(\frac{f_{i}^{(k+1)}-C_{ij}}{\varepsilon}\right),\qquad j=1,\ldots,m,(25)

in which the superscript denotes the iteration index and the second update
uses the freshly computedf(k+1)f^{(k+1)}rather than the stalef(k)f^{(k)},
corresponding to a Gauss–Seidel rather than a Jacobi sweep. A direct
consequence of the ordering in (24)–(25) is
that the column-marginal constraint of the transportation
polytope (13) is satisfied exactly at the end of
every sweep,∑i=1nexp⁡(fi(k+1)+gj(k+1)−Ci​jε)=bj,j=1,…,m,\sum_{i=1}^{n}\exp\!\left(\frac{f_{i}^{(k+1)}+g_{j}^{(k+1)}-C_{ij}}{\varepsilon}\right)\;=\;b_{j},\qquad j=1,\ldots,m,(26)

while the row marginal∑jπi​j(k+1)\sum_{j}\pi_{ij}^{(k+1)}deviates fromaia_{i}by an
amount that decreases monotonically as the iteration proceeds. The outer
loops in (24) and (25) are parallelized
across threads, while the inner LSE evaluation is kept serial per
thread to preserve the deterministic max-trick evaluation order, giving
each full sweep a computational cost ofO​(n​m)O(nm)elementary operations
after the cost matrix has been assembled. The
formulation (24)–(25) is the standard
log-domain Sinkhorn recursion[31,1], and it
reduces to the classical multiplicative Sinkhorn–Knopp iteration on the
scalings(u,v)(u,v)in the limit of largeε\varepsilon[39,40,23].

Both potentials are initialized to the zero vector,f(0)=0f^{(0)}=0andg(0)=0g^{(0)}=0, corresponding to the independent product couplingui(0)​vj(0)=ai​bju_{i}^{(0)}v_{j}^{(0)}=a_{i}b_{j}in (15) and offering no informative
prior to bias the iteration toward any particular transport structure. The
logarithms of the marginal weight vectors,log⁡a\log aandlog⁡b\log b, are
precomputed once at solver entry after adding a floor of10−30010^{-300}inside the logarithm to guard against strictly zero entries in
user-supplied marginals; for the default uniform weightsai=1/na_{i}=1/nandbj=1/mb_{j}=1/mthis floor is inactive. Convergence is monitored through theℓ1\ell^{1}residual of the row marginal constraint
in (13),η(k)=‖π(k)​𝟏m−a‖1=∑i=1n|∑j=1mπi​j(k)−ai|,\eta^{(k)}\;=\;\left\|\pi^{(k)}\mathbf{1}_{m}-a\right\|_{1}\;=\;\sum_{i=1}^{n}\left|\sum_{j=1}^{m}\pi_{ij}^{(k)}-a_{i}\right|,(27)

which is evaluated without materializing the plan through the log-domain
identitylog(π(k)𝟏m)i=fi(k)ε+LSEj(gj(k)−Ci​jε),i=1,…,n,\log\!\left(\pi^{(k)}\mathbf{1}_{m}\right)_{i}\;=\;\frac{f_{i}^{(k)}}{\varepsilon}\;+\;\mathrm{LSE}_{j}\!\left(\frac{g_{j}^{(k)}-C_{ij}}{\varepsilon}\right),\qquad i=1,\ldots,n,(28)

which is derived by taking the logarithm of the row sum of the Gibbs
factorization (15) and grouping the constantfi(k)/εf_{i}^{(k)}/\varepsilonoutside the LSE. The residual (27)
is evaluated at every tenth Sinkhorn sweep rather than at every sweep to
amortize the associatedO​(n​m)O(nm)cost across the intervening iterations.
The check is deliberately asymmetric, using only the row-marginal residual
rather than the sum of row and column residuals, since the column-marginal
identity (26) already holds up to floating-point
precision at the end of each sweep. The convergence properties of the
Sinkhorn recursion under mild positivity assumptions on the marginals were
established in the classical setting[39,23], and
the log-domain adaptation preserves the geometric contraction rate in the
Hilbert projective metric that underlies those results. The toleranceη(k)<10−9\eta^{(k)}<10^{-9}and the iteration cap of two thousand sweeps
adopted here are configuration-file parameters that may be adjusted at run
time.

Once the potentials(f,g)(f,g)satisfy the convergence
criterion (27), the optimal transport plan is
materialized on the exponential scale by direct evaluation ofπi​j⋆=exp⁡(fi+gj−Ci​jε),i=1,…,n,j=1,…,m,\pi^{\star}_{ij}\;=\;\exp\!\left(\frac{f_{i}+g_{j}-C_{ij}}{\varepsilon}\right),\qquad i=1,\ldots,n,\;j=1,\ldots,m,(29)

consistent with the Gibbs factorization (15) after the
change of variables (22). Materialization is performed
only once, after the iterative refinement has terminated, and the
associated loss of log-domain stability is confined to individual matrix
entries whose value is below the smallest representable positive
double-precision number and which contribute negligibly to any downstream
statistic[34]. The transport cost is computed as the
Frobenius pairing⟨C,π⋆⟩F=∑i=1n∑j=1mCi​j​πi​j⋆,\langle C,\pi^{\star}\rangle_{F}\;=\;\sum_{i=1}^{n}\sum_{j=1}^{m}C_{ij}\,\pi^{\star}_{ij},(30)

evaluated on the materialized plan, matching the
objective (14) evaluated at the optimum.

Reconstruction of the intermediate-time densityρt\rho_{t}in (20) proceeds by drawing samples from the marginal law
rather than by evaluatingρt\rho_{t}on a spatial grid, which would be
infeasible for the domain-free point-cloud data type. The Brownian-bridge
formula (19) shows that a sample fromρt\rho_{t}may
be obtained by a two-step composition: first draw endpoint indices(i,j)(i,j)from the discrete joint distribution induced byπ⋆\pi^{\star}, and then
draw the intermediate position from the conditional Gaussian law with
mean(1−t)​xi+t​yj(1-t)\,x_{i}+t\,y_{j}and covarianceε​t​(1−t)​Id\varepsilon\,t(1-t)\,I_{d}. Conditioned on the source indexii, the target indexjjis drawn
from the discrete conditional distributionℙ​(j|i)=πi​j⋆∑j′πi​j′⋆=πi​j⋆ai,\mathbb{P}(j\,|\,i)\;=\;\frac{\pi^{\star}_{ij}}{\sum_{j^{\prime}}\pi^{\star}_{ij^{\prime}}}\;=\;\frac{\pi^{\star}_{ij}}{a_{i}},(31)

where the second equality holds exactly at convergence and is the reason
that the marginal residual (27) rather than the
plan itself controls sampling fidelity. The categorical draw is executed
by inverse cumulative distribution function sampling, that is, by drawing
a uniform random variableU∼𝒰​(0,1)U\sim\mathcal{U}(0,1)and selecting the
smallest indexj⋆​(i,U)j^{\star}(i,U)for which∑j′=1j⋆πi​j′⋆ai≥U.\sum_{j^{\prime}=1}^{j^{\star}}\frac{\pi^{\star}_{ij^{\prime}}}{a_{i}}\;\geq\;U.(32)

The intermediate-time sample is thenXt,i=(1−t)​xi+t​yj⋆​(i,U)+ε​t​(1−t)​Zi,Zi∼𝒩​(0,Id),X_{t,i}\;=\;(1-t)\,x_{i}\;+\;t\,y_{j^{\star}(i,U)}\;+\;\sqrt{\varepsilon\,t(1-t)}\;Z_{i},\qquad Z_{i}\sim\mathcal{N}(0,I_{d}),(33)

with the Gaussian noise drawn coordinatewise from the standard normal
distribution provided bynp.random.randnand scaled by the bridge
standard deviationε​t​(1−t)\sqrt{\varepsilon\,t(1-t)}derived
from (19). A defensive branch reassigns the sample
toxix_{i}whenever the row sum∑jπi​j⋆\sum_{j}\pi^{\star}_{ij}falls below10−30010^{-300}, an eventuality that in practice occurs only when the
convergence tolerance has been set orders of magnitude below the
achievable double-precision floor.

Full trajectories are constructed by repeating the sampling
procedure (32)–(33) over a uniform
time gridtℓ=ℓNf−1,ℓ=0,1,…,Nf−1,t_{\ell}\;=\;\frac{\ell}{N_{f}-1},\qquad\ell=0,1,\ldots,N_{f}-1,(34)

ofNfN_{f}frames on the unit interval. Att=0t=0andt=1t=1the boundary
constraints are enforced exactly by returning the source cloudXXand the
target cloudYYrespectively, bypassing the stochastic sampling procedure
and guaranteeing that the reconstructed trajectory reproduces the
prescribed endpoints to machine precision. At interior time levels the
sampling routine is called with a per-frame random seed constructed by
adding the frame index to a user-specified base seed, which yields
independent draws fromρtℓ\rho_{t_{\ell}}across frames and produces a
visualization of marginal evolution rather than of Lagrangian particle
paths. While a pathwise construction, in which each particle is assigned
a fixed Brownian-bridge realization across all frames, would produce
smoother apparent trajectories, the marginal-sampling procedure adopted
here has the advantage that each frame is a statistically valid draw from
the correct intermediate density.

Beyond the primary transport plan and its bridge reconstruction, the
solver evaluates a small collection of diagnostic quantities at
convergence. The plan entropyH​(π⋆)=−∑i=1n∑j=1mπi​j⋆​log⁡πi​j⋆H(\pi^{\star})\;=\;-\sum_{i=1}^{n}\sum_{j=1}^{m}\pi^{\star}_{ij}\,\log\pi^{\star}_{ij}(35)

measures the effective dispersion of the coupling, evaluated with the
convention0​log⁡0=00\log 0=0and restricted in practice to entries above the
underflow floor of10−30010^{-300}. The normalized effective supportexp⁡(H​(π⋆))/(n​m)\exp(H(\pi^{\star}))/(nm)translates the entropy into a scale-free
number in(0,1](0,1]that approaches unity for a diffuse near-independent
coupling and1/max⁡(n,m)1/\max(n,m)for a permutation-like coupling that
concentrates all mass on a small subset of entries. The row and column
marginal residuals evaluated on the materialized
plan (29),rrow=maxi⁡|∑j=1mπi​j⋆−ai|,rcol=maxj⁡|∑i=1nπi​j⋆−bj|,r_{\mathrm{row}}\;=\;\max_{i}\left|\sum_{j=1}^{m}\pi^{\star}_{ij}-a_{i}\right|,\qquad r_{\mathrm{col}}\;=\;\max_{j}\left|\sum_{i=1}^{n}\pi^{\star}_{ij}-b_{j}\right|,(36)

together with the total plan mass∑i​jπi​j⋆\sum_{ij}\pi^{\star}_{ij}and theℓ1\ell^{1}residual (27) at the final iteration,
provide a consistency audit whose deviation from the theoretical values of0,0,11, and0respectively quantifies the numerical residual
accumulated during the iteration. All diagnostics, along with the
potentials, the plan, and the bridge trajectory, are written to a
self-describing NetCDF-4 file following the Climate and Forecast (CF)
conventions[33,20], withfloat32storage adopted
for the bulk quantities to keep archival footprints manageable while
retaining thefloat64working precision at run time.

## 2.3Numerical Experiments

Four demonstration cases exerciseanyakrakusumaacross a graded
sequence of source and target geometries. Each case fixes the point-cloud
size atn=m=1000n=m=1000, the spatial dimension atd=2d=2, the marginal
weights at uniform valuesai=1/na_{i}=1/nandbj=1/mb_{j}=1/m, the Sinkhorn
tolerance atη(k)<10−9\eta^{(k)}<10^{-9}, the iteration cap at two thousand
sweeps, and the base random seed at the value4242; source and target
point clouds are generated with random seeds4242and10421042respectively,
so that the two clouds are drawn from independent streams of a
reproducible pseudorandom sequence. The regularization parameterε\varepsilonand the frame countNfN_{f}are chosen case by case, and their
values are tabulated together with the source and target parametrizations
in the descriptions that follow. Although the demonstration parameters
adopt uniform marginals and a two-dimensional embedding, the underlying
routines described earlier accept nonuniform marginal weights and
arbitrary spatial dimensiondd; the built-in distribution generators and
the animation utilities ofanyakrakusuma, however, are
specialized to the two-dimensional case, so that experiments beyond the
plane require user-supplied point clouds.

## Case 1: Circle to circle.

The source distribution is the uniform measure on the unit circle,
sampled byxi=(cos⁡θi,sin⁡θi),θi=2​π​(i−1)n+φ,i=1,…,n,x_{i}\;=\;\left(\cos\theta_{i},\;\sin\theta_{i}\right),\qquad\theta_{i}\;=\;\frac{2\pi(i-1)}{n}+\varphi,\qquad i=1,\ldots,n,(37)

with a global phaseφ∼𝒰​(0,2​π/n)\varphi\sim\mathcal{U}(0,2\pi/n)drawn once at
the outset to randomize the angular offset. The target distribution is
the uniform measure on the concentric circle of radius22, sampled by
the same construction with radius rescaled from11to22and an
independent phase drawn from the same distribution. No perturbation
noise is applied at either endpoint, so the two clouds lie exactly on
their respective circles. The regularization parameter is set toε=0.02\varepsilon=0.02and the trajectory is rendered on a grid ofNf=120N_{f}=120frames. This case isolates radial rescaling in the absence of
angular reorganization and provides a baseline against which the more
complex geometries are compared.

## Case 2: Spiral to Gaussian mixture.

The source distribution is an Archimedean spiral with two full turns,
sampled byxi=ri​(cos⁡θi,sin⁡θi),θi=0.5+4​π−0.5n−1​(i−1),ri=1.5​θi4​π,x_{i}\;=\;r_{i}\left(\cos\theta_{i},\;\sin\theta_{i}\right),\qquad\theta_{i}\;=\;0.5+\frac{4\pi-0.5}{n-1}\,(i-1),\qquad r_{i}\;=\;\frac{1.5\,\theta_{i}}{4\pi},(38)

fori=1,…,ni=1,\ldots,n, with additive isotropic Gaussian perturbation of
standard deviationσsrc=0.01\sigma_{\mathrm{src}}=0.01. The target distribution
is a mixture of four Gaussian components with centers arranged uniformly
on the circle of radius1.51.5,ck=1.5​(cos⁡2​π​(k−1)4,sin⁡2​π​(k−1)4),k=1,2,3,4,c_{k}\;=\;1.5\,\left(\cos\frac{2\pi(k-1)}{4},\;\sin\frac{2\pi(k-1)}{4}\right),\qquad k=1,2,3,4,(39)

with each component contributingn/4n/4points drawn from𝒩​(ck,0.152​I2)\mathcal{N}(c_{k},0.15^{2}I_{2}). The regularization is set toε=0.05\varepsilon=0.05and the trajectory is rendered onNf=120N_{f}=120frames. This case
tests the solver on a topology-changing transition from a
one-dimensional connected support to a disconnected four-modal target.

## Case 3: Two moons to rotated two moons.

The source distribution is the two-moons configuration, an interleaved
pair of half-circles sampled byxi={(cos⁡αi,sin⁡αi)+ξi,i=1,…,⌊n/2⌋,(1−cos⁡βi,12−sin⁡βi)+ξi,i=⌊n/2⌋+1,…,n,x_{i}\;=\;\begin{cases}(\cos\alpha_{i},\;\sin\alpha_{i})+\xi_{i},&i=1,\ldots,\lfloor n/2\rfloor,\\[4.0pt]
(1-\cos\beta_{i},\;\tfrac{1}{2}-\sin\beta_{i})+\xi_{i},&i=\lfloor n/2\rfloor+1,\ldots,n,\end{cases}(40)

where the angular parametersαi∈[0,π]\alpha_{i}\in[0,\pi]andβi∈[0,π]\beta_{i}\in[0,\pi]are equispaced within their respective half of the sample andξi∼𝒩​(0,0.052​I2)\xi_{i}\sim\mathcal{N}(0,0.05^{2}I_{2})is the additive isotropic
perturbation applied independently to each point. The target
distribution is obtained by applying a rotation ofπ/2\pi/2radians about
the empirical centroidx¯=n−1​∑ixi\bar{x}=n^{-1}\sum_{i}x_{i}of a freshly drawn
two-moons cloud,yj=x¯+(cos⁡(π/2)−sin⁡(π/2)sin⁡(π/2)cos⁡(π/2))​(xj′−x¯),j=1,…,n,y_{j}\;=\;\bar{x}\;+\;\begin{pmatrix}\cos(\pi/2)&-\sin(\pi/2)\\
\sin(\pi/2)&\phantom{-}\cos(\pi/2)\end{pmatrix}(x^{\prime}_{j}-\bar{x}),\qquad j=1,\ldots,n,(41)

where{xj′}j=1n\{x^{\prime}_{j}\}_{j=1}^{n}is the fresh two-moons cloud generated with the
target random seed. The regularization is set toε=0.03\varepsilon=0.03and
the trajectory is rendered onNf=120N_{f}=120frames. This case tests the
coupling on a nontrivial angular reorganization between two clouds of
identical shape but distinct orientation.

## Case 4: Lissajous curve to trefoil projection.

The source distribution is the Lissajous curve with frequency ratio3:23{:}2and phase shiftπ/2\pi/2, scaled to unit amplitude1.51.5,xi=1.5​(sin⁡(3​ti+π/2),sin⁡(2​ti)),ti=2​π​(i−1)n,i=1,…,n,x_{i}\;=\;1.5\,\left(\sin(3t_{i}+\pi/2),\;\sin(2t_{i})\right),\qquad t_{i}\;=\;\frac{2\pi(i-1)}{n},\qquad i=1,\ldots,n,(42)

sampled uniformly in the parametert∈[0,2​π)t\in[0,2\pi). The target
distribution is the two-dimensional projection of the trefoil knot,yj=1.53​(sin⁡sj+2​sin⁡(2​sj),cos⁡sj−2​cos⁡(2​sj)),sj=2​π​(j−1)n,j=1,…,n,y_{j}\;=\;\frac{1.5}{3}\,\left(\sin s_{j}+2\sin(2s_{j}),\;\cos s_{j}-2\cos(2s_{j})\right),\qquad s_{j}\;=\;\frac{2\pi(j-1)}{n},\qquad j=1,\ldots,n,(43)

sampled uniformly in the parameters∈[0,2​π)s\in[0,2\pi). No perturbation
noise is applied to either curve. The regularization is set toε=0.04\varepsilon=0.04and the trajectory is rendered on the denser grid ofNf=150N_{f}=150frames, reflecting the greater topological complexity of the
intermediate density in the transition between the two self-intersecting
curves.

## 2.4Data Analyses

The Sinkhorn iteration history, the optimal coupling, and the bridge
trajectory stored in each NetCDF file are subjected to four independent
diagnostic analyses that quantify, respectively, the numerical convergence
of the dual iteration, the geometric content of the discrete coupling, the
spatial evolution of the intermediate density, and the informational and
structural evolution of the point cloud along the bridge. All four
analyses are implemented in Python and rely onNumPyfor array
manipulation[14],SciPyfor the kernel density
estimator, nearest-neighbor queries, and special
functions[42], andMatplotlibfor the
publication figures[21], with the NetCDF interface exposed
throughnetCDF4[33]. The four diagnostic categories
are treated in turn below.

The convergence history of the log-domain Sinkhorn iteration is recorded
by the solver every ten sweeps, so that the vector{η(kℓ)}\{\eta^{(k_{\ell})}\}of
stored marginal residuals is associated with iteration indiceskℓ=10​ℓ,ℓ=0,1,…,L−1,k_{\ell}\;=\;10\,\ell,\qquad\ell=0,1,\ldots,L-1,(44)

whereLLis the number of stored samples andη(k)\eta^{(k)}is the row
marginal violation defined in (27). Under the
contraction properties of the Sinkhorn recursion in the Hilbert
projective metric[39,23], the residual is expected
to decay geometrically, so thatlog10⁡η(k)\log_{10}\eta^{(k)}is approximately
linear inkk. A least-squares fitlog10⁡η(kℓ)≈β0+β1​kℓ,ℓ=0,1,…,L−1,\log_{10}\eta^{(k_{\ell})}\;\approx\;\beta_{0}+\beta_{1}\,k_{\ell},\qquad\ell=0,1,\ldots,L-1,(45)

is carried out over the positive-residual subset, and the per-iteration
contraction factor is reported as10β110^{\beta_{1}}. As an independent check
of the geometric-decay assumption, a per-step contraction ratior(kℓ)=(η(kℓ+1)η(kℓ))1/10,ℓ=0,1,…,L−2,r^{(k_{\ell})}\;=\;\left(\frac{\eta^{(k_{\ell+1})}}{\eta^{(k_{\ell})}}\right)^{1/10},\qquad\ell=0,1,\ldots,L-2,(46)

is computed and plotted againstkℓk_{\ell}, with the exponent1/101/10converting the between-record ratio to a per-iteration quantity. A flat
sequencer(kℓ)r^{(k_{\ell})}approximately equal to10β110^{\beta_{1}}indicates
that the geometric-decay assumption is well satisfied, while systematic
drift signals a departure from strict linearity in the log-domain. The
fit (45) is defined only when at least two
positive-residual samples are recorded, so scenarios that converge below
tolerance at the first evaluation contribute one summary line to the
report but no fitted rate.

The optimal couplingπ⋆\pi^{\star}materialized through (29)
is analyzed through the discrete conditional distribution and the
associated barycentric projection. For each source indexii, the row
conditionalP​(j|i)=πi​j⋆∑j′=1mπi​j′⋆,j=1,…,m,P(j\,|\,i)\;=\;\frac{\pi^{\star}_{ij}}{\sum_{j^{\prime}=1}^{m}\pi^{\star}_{ij^{\prime}}},\qquad j=1,\ldots,m,(47)

which coincides with the sampling distribution (31)
used in the bridge reconstruction, gives the entropic-transport analogue
of the target of a deterministic Monge map. The barycentric image ofxix_{i}under the coupling is the conditional-expectation mapT​(xi)=𝔼​[Y|X=xi]=∑j=1mP​(j|i)​yj,i=1,…,n,T(x_{i})\;=\;\mathbb{E}[Y\,|\,X=x_{i}]\;=\;\sum_{j=1}^{m}P(j\,|\,i)\,y_{j},\qquad i=1,\ldots,n,(48)

which in the deterministic limitε→0+\varepsilon\to 0^{+}approaches the
Brenier map and in the diffuse limitε→∞\varepsilon\to\inftycollapses to
the marginal mean of the target[3,31]. The
per-source dispersion of the coupling is quantified through the row
Shannon entropyHi=−∑j=1mP​(j|i)​log⁡P​(j|i),i=1,…,n,H_{i}\;=\;-\sum_{j=1}^{m}P(j\,|\,i)\,\log P(j\,|\,i),\qquad i=1,\ldots,n,(49)

with the convention0​log⁡0=00\log 0=0enforced by restricting the sum to the
positive-mass entries. The corresponding perplexityexp⁡(Hi)\exp(H_{i})is the
effective number of target points that carry nonvanishing mass fromxix_{i}, and its arithmetic mean⟨exp⁡(Hi)⟩i\langle\exp(H_{i})\rangle_{i}is reported
as a single case-level summary of the coupling’s diffuseness. A
complementary summary is the mean peak conditional probability⟨maxj⁡P​(j|i)⟩i\langle\max_{j}P(j\,|\,i)\rangle_{i}, which approaches unity for permutation-like
plans and1/m1/mfor the diffuse product coupling. The displacement
magnitude‖T​(xi)−xi‖\|T(x_{i})-x_{i}\|furnishes a scalar per-source measure of the
transport work, reported as its mean, median, and maximum across the
source cloud. When the stored plan is subsampled to ap×pp\times pretained block by the solver’s NetCDF writer, the source and target
clouds are aligned to the retained rows and columns through the same
strided index selectionιℓ=⌊ℓ​(n−1)/(p−1)⌋\iota_{\ell}=\lfloor\ell(n-1)/(p-1)\rfloorused at storage time, and the retained rows are renormalized
before the conditional (47) is formed. In this
subsampled regime the reported quantities are computed over a strided
subset rather than over the full plan and are labeled accordingly in the
diagnostic report.

The intermediate marginalsρt\rho_{t}reconstructed through the bridge
sampler are subjected to a Gaussian kernel density estimate (KDE) at five
representative interpolation times𝒯={0,0.25,0.5,0.75,1}\mathcal{T}=\{0,\,0.25,\,0.5,\,0.75,\,1\}. For a snapshot timet⋆∈𝒯t^{\star}\in\mathcal{T}, the sample
cloud is either the stored frame att⋆t^{\star}when the time grid containst⋆t^{\star}exactly, or the linear temporal interpolation between the two
straddling frames when it does not. On the resulting cloud, the density
estimate at grid pointzzisρ^t​(z)=1n​hd​∑i=1nK​(z−Xt,ih),\hat{\rho}_{t}(z)\;=\;\frac{1}{n\,h^{d}}\,\sum_{i=1}^{n}K\!\left(\frac{z-X_{t,i}}{h}\right),(50)

with an isotropic Gaussian kernelKKand bandwidthhhselected by
Scott’s rule of thumb,h=n−1/(d+4)h=n^{-1/(d+4)}[37,38],
as implemented in thescipy.stats.gaussian_kderoutine[42]. The density is evaluated on a140×140140\times 140grid spanning the joint bounding box of the source, target, and all
intermediate clouds, and is normalized to its per-panel maximum so that
the cross-time and cross-case comparison is carried out on the
scale-free fieldρt†​(z)=ρ^t​(z)/maxz⁡ρ^t​(z)\rho^{\dagger}_{t}(z)=\hat{\rho}_{t}(z)/\max_{z}\hat{\rho}_{t}(z). Three summary quantities are computed onρt†\rho^{\dagger}_{t}.
The high-density region countNreg​(t)=#​{connected components of​{z:ρt†​(z)≥0.5}},N_{\mathrm{reg}}(t)\;=\;\#\,\big\{\text{connected components of }\{z:\rho^{\dagger}_{t}(z)\geq 0.5\}\big\},(51)

formed under four-connectivity on the pixel lattice, provides a
ridge-robust replacement for the raw mode count: a ring-shaped support
counts as a single region, while spatially separated concentrations count
individually. The effective support areaAeff​(t)=exp⁡(−∑cpc​(t)​log⁡pc​(t))​Δ​x​Δ​y,pc​(t)=ρt†​(zc)∑c′ρt†​(zc′),A_{\mathrm{eff}}(t)\;=\;\exp\!\left(-\sum_{c}p_{c}(t)\,\log p_{c}(t)\right)\Delta x\,\Delta y,\qquad p_{c}(t)\;=\;\frac{\rho^{\dagger}_{t}(z_{c})}{\sum_{c^{\prime}}\rho^{\dagger}_{t}(z_{c^{\prime}})},(52)

in which the sum runs over grid cellsccwith centerzcz_{c}and areaΔ​x​Δ​y\Delta x\,\Delta y, gives a participation-based measure of the area
occupied by the density that does not degenerate for supports concentrated
near a low-dimensional manifold, in contrast to the point-mass summary
that would be given by the argmax ofρt†\rho^{\dagger}_{t}. The support
fraction|{z:ρt†​(z)≥0.03}|/(1402)|\{z:\rho^{\dagger}_{t}(z)\geq 0.03\}|/(140^{2})complements
the effective area with a simple thresholded-coverage statistic that
tracks with the visual footprint of each panel.

The bridge point cloud is further characterized at every stored frame
through the Kozachenko–Leonenkokk-nearest-neighbor estimator of the
differential entropy ofρt\rho_{t}[24,25],H^​(ρt)=−ψ​(k)+ψ​(n)+log⁡cd+dn​∑i=1nlog⁡ri​(t),\hat{H}(\rho_{t})\;=\;-\psi(k)+\psi(n)+\log c_{d}\;+\;\frac{d}{n}\sum_{i=1}^{n}\log r_{i}(t),(53)

withk=5k=5, digamma functionψ\psi, unit-ball volumecd=πd/2Γ​(d/2+1),c_{d}\;=\;\frac{\pi^{d/2}}{\Gamma(d/2+1)},(54)

andri​(t)r_{i}(t)the Euclidean distance fromXt,iX_{t,i}to itskk-th nearest
neighbor in the frame-ttcloud, computed through thescipy.spatial.cKDTreequery with a floor of10−1210^{-12}to guard
against exact-coincidence pairs. The estimator (53) is
consistent for absolutely continuous densities inℝd\mathbb{R}^{d}and
exhibitsn\sqrt{n}-convergence in the limit of large sample size; its
finite-sample behavior at the endpoint clouds, where the mass concentrates
near a lower-dimensional curve, is understood as a comparative diagnostic
rather than as an estimate of a well-defined two-dimensional differential
entropy. As a reference against which the measured value at the midpoint
of the bridge may be compared, the differential entropy of the pure
Brownian-bridge noise term of (19), whose covariance
isε​t​(1−t)​Id\varepsilon\,t(1-t)\,I_{d}, isHdiff​(t)=d2​log⁡(2​π​e​ε​t​(1−t)),H_{\mathrm{diff}}(t)\;=\;\frac{d}{2}\,\log\!\left(2\pi e\,\varepsilon\,t(1-t)\right),(55)

which att=1/2t=1/2reduces to(d/2)​log⁡(π​e​ε/2)(d/2)\log(\pi e\,\varepsilon/2)and
serves as a lower bound on the entropy that a bridge marginal must carry
whenever the endpoint contribution is negligible.

The second-moment geometry ofρt\rho_{t}is summarized through the sample
covariance matrixΣ^​(t)=1n−1​∑i=1n(Xt,i−X¯t)​(Xt,i−X¯t)⊤,X¯t=1n​∑i=1nXt,i,\hat{\Sigma}(t)\;=\;\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{t,i}-\bar{X}_{t}\right)\left(X_{t,i}-\bar{X}_{t}\right)^{\top},\qquad\bar{X}_{t}\;=\;\frac{1}{n}\sum_{i=1}^{n}X_{t,i},(56)

with eigenvaluesλmin​(t)≤λmax​(t)\lambda_{\min}(t)\leq\lambda_{\max}(t)computed
throughnumpy.linalg.eigvalsh. Three ellipse descriptors follow:
the root-mean-square (RMS) dispersionrms​(t)=tr​Σ^​(t)=λmin​(t)+λmax​(t),\mathrm{rms}(t)\;=\;\sqrt{\mathrm{tr}\,\hat{\Sigma}(t)}\;=\;\sqrt{\lambda_{\min}(t)+\lambda_{\max}(t)},(57)

the eccentricitye​(t)=1−λmin​(t)λmax​(t),e(t)\;=\;\sqrt{1-\frac{\lambda_{\min}(t)}{\lambda_{\max}(t)}},(58)

and the doubled principal-axis angleΘ​(t)=atan2⁡(2​Σ^12​(t),Σ^11​(t)−Σ^22​(t)),\Theta(t)\;=\;\operatorname{atan2}\!\left(2\,\hat{\Sigma}_{12}(t),\;\hat{\Sigma}_{11}(t)-\hat{\Sigma}_{22}(t)\right),(59)

whose halving gives the principal-axis direction moduloπ\pi. The
doubled representation removes the axis-wrap ambiguity that would
corrupt a direct estimate of the axis angle, and permits temporal
unwrapping to be performed by standard phase-unwrap onΘ​(t)\Theta(t)[29]. Because the principal-axis direction is
resolved only for anisotropic clouds, the orientation angle is
reported only at frames with eccentricity above a fixed threshold,e​(t)≥0.25e(t)\geq 0.25; below this threshold the two eigenvalues are too close for
the principal axis to be meaningfully distinguished from a random
rotation of an isotropic disk. The unwrap is applied within each
contiguous run of resolved frames but never across a masked run, since
the axis direction on the two sides of an isotropic gap can be
near-antipodal and the connecting branch is not determined by the data.

Uncertainty in the frame-wise estimates of the differential
entropy (53), the RMS dispersion (57),
the eccentricity (58), and the doubled
angle (59) is quantified through subsampling without
replacement, chosen in preference to the classical bootstrap because
resampling with replacement generates coincident particles that corrupt
the nearest-neighbor entropy throughlog⁡0\log 0singularities in therir_{i}[32,10]. For each frame,B=80B=80subsamples
of sizem=⌊0.8​n⌋m=\lfloor 0.8\,n\rfloorare drawn from the frame cloud
without replacement, each of the four descriptors is recomputed on the
subsample, and the subsample standard deviation is rescaled to the
full-sample standard deviation through then\sqrt{n}-convergence
identityσ^n=mn​σ^m,\hat{\sigma}_{n}\;=\;\sqrt{\frac{m}{n}}\;\hat{\sigma}_{m},(60)

which is the standard subsampling correction for statistics whose
asymptotic distribution is centered at a fixed limit and scales asn−1/2n^{-1/2}[32]. A ninety-five-percent confidence band is
then formed asθ^n±1.96​σ^n\hat{\theta}_{n}\pm 1.96\,\hat{\sigma}_{n}under a Gaussian
approximation for the linear descriptors. For the doubled angleΘ\Theta, whose ambient space is the unit circle, the subsample spread
is quantified through the mean resultant lengthR=|1B​∑b=1Bexp⁡(i​Θ(b))|,R\;=\;\left|\frac{1}{B}\sum_{b=1}^{B}\exp\!\left(i\,\Theta^{(b)}\right)\right|,(61)

from which the circular standard deviation follows through the standard
identityσcirc=−2​log⁡R\sigma_{\mathrm{circ}}=\sqrt{-2\log R}[29], undefined in the vanishing-RRlimit and guarded
in the implementation by a lower cutoffR>10−12R>10^{-12}. The
corresponding half-width on the axis angle, obtained after halving the
doubled representation and rescaling through (60),
is reported in degrees.

The per-case diagnostic reports collect these quantities into a fixed
plain-text layout that lists, for each of the four cases, the
convergence flag and iteration count, the log-linear contraction factor
and its per-step check, the barycentric-map summary
statistics, the KDE snapshot table with region count, effective area,
support fraction, and centroid at each of the five snapshot times, and
the frame-wise differential entropy att∈{0,1/2,1}t\in\{0,1/2,1\}together
with the net productionH^​(ρ1)−H^​(ρ0)\hat{H}(\rho_{1})-\hat{H}(\rho_{0}), the peak
entropy and its time of occurrence, the RMS dispersion at the three
canonical times together with its peak, and the axis reorientation(Θ​(1)−Θ​(0)+90∘)mod180∘−90∘(\Theta(1)-\Theta(0)+90^{\circ})\bmod 180^{\circ}-90^{\circ}folded to
the interval(−90∘,90∘](-90^{\circ},\,90^{\circ}]to remove the mod-π\piambiguity
of principal-axis directions. Each descriptor is accompanied by the mean
across frames of the ninety-five-percent half-width from the subsampling
calculation, which quantifies the average size of the uncertainty band
in the corresponding figure panel and provides a scalar summary of the
statistical resolution at which each geometric feature has been
recovered.

## 3Results

The four demonstration cases were executed under the parameter settings
specified above, each as an independent process that logged its parameters,
solver diagnostics, and a timing breakdown alongside the NetCDF archive. The
resulting archives were passed through the four diagnostic analyses without
further intervention. All values reported below are taken directly from the
run logs and the diagnostic output. Quantities are dimensionless unless a
unit is stated.

Every case satisfied the marginal-residual toleranceη(k)<10−9\eta^{(k)}<10^{-9}within the two-thousand-sweep cap, and every run reported a marginal fidelity
of1.000000001.00000000and terminated without warnings or errors. The sweep counts
at termination were11,721721,581581, and651651for cases 1 through 4
respectively, corresponding to11,7373,5959, and6666recorded residual
samples at the ten-sweep recording stride. Case 1 met the tolerance at the
first residual evaluation, at which point the residual stood atη=3.771506×10−15\eta=3.771506\times 10^{-15}, approximately seventeen times the double-precision
unit roundoff2−52≈2.220×10−162^{-52}\approx 2.220\times 10^{-16}. The log-linear fit of
equation (45) is undefined for a single recorded
sample, so no contraction factor is reported for case 1 and that case is
absent from the convergence panels. The remaining three cases entered the
iteration with residuals of order unity,η(0)=1.127457\eta^{(0)}=1.127457,0.7992010.799201,
and0.5358170.535817for cases 2, 3, and 4, and terminated at8.116460×10−108.116460\times 10^{-10},9.982731×10−109.982731\times 10^{-10}, and8.503125×10−108.503125\times 10^{-10}. The
fitted slopes were−1.071160×10−2-1.071160\times 10^{-2},−1.511440×10−2-1.511440\times 10^{-2},
and−1.171978×10−2-1.171978\times 10^{-2}decades per sweep, giving per-iteration
contraction factors10β110^{\beta_{1}}of0.9756370.975637,0.9657960.965796, and0.9733750.973375. The ordering of the contraction factors across the three fitted
cases does not follow the ordering of the regularization parameter, the
fastest contraction being recorded atε=0.03\varepsilon=0.03and the slowest atε=0.05\varepsilon=0.05. Table1collects the convergence
summary.

Figure1(a) shows the residual histories on a logarithmic
ordinate together with the fitted geometric decays. The histories are linear
over approximately eight decades in all three fitted cases, and the fitted
lines are visually indistinguishable from the data over the greater part of
that range. Figure1(b) shows the per-step contraction
ratio of equation (46). In each case the ratio rises
through a transient occupying the first several tens of sweeps and settles
onto the corresponding fitted factor within approximately one hundred sweeps,
remaining flat to within the resolution of the panel thereafter.Figure 1:Convergence of the log-domain Sinkhorn iteration for the three cases
that produced a fittable residual history. (a) Marginal constraint violationη(k)=‖π(k)​𝟏m−a‖1\eta^{(k)}=\|\pi^{(k)}\mathbf{1}_{m}-a\|_{1}against sweep index, with
the fitted geometric decays of equation (45) overlaid as
dashed lines. (b) Per-iteration contraction ratior(kℓ)r^{(k_{\ell})}of
equation (46) against sweep index, with the fitted
factor10β110^{\beta_{1}}of each case shown as a dotted horizontal line. Case 1
satisfied the convergence tolerance at the first residual evaluation and
contributes a single recorded sample, from which no rate can be fitted; it is
therefore absent from both panels.Table 1:Convergence summary of the log-domain Sinkhorn iteration. The
residualη(k)\eta^{(k)}is theℓ1\ell^{1}row-marginal violation of
equation (27), recorded every ten sweeps. The
contraction factor is10β110^{\beta_{1}}from the fit of
equation (45).Caseε\varepsilonSweepsη(0)\eta^{(0)}ηfinal\eta^{\mathrm{final}}10β110^{\beta_{1}}10.0213.7715×10−153.7715\times 10^{-15}3.7715×10−153.7715\times 10^{-15}—20.057211.1275×1001.1275\times 10^{0}8.1165×10−108.1165\times 10^{-10}0.9756430.035817.9920×10−17.9920\times 10^{-1}9.9827×10−109.9827\times 10^{-10}0.9658040.046515.3582×10−15.3582\times 10^{-1}8.5031×10−108.5031\times 10^{-10}0.97338

Turning to the converged coupling, the transport cost⟨C,π⋆⟩\langle C,\pi^{\star}\rangleof equation (30) was1.0100131.010013,0.8081370.808137,0.8662670.866267, and0.3132950.313295for cases 1 through 4. The joint plan
entropyH​(π⋆)H(\pi^{\star})of equation (35) was10.748710.7487,11.608611.6086,11.286911.2869, and10.931310.9313nats, and the effective sparsityexp⁡(H​(π⋆))/(n​m)\exp(H(\pi^{\star}))/(nm), the joint perplexity expressed as a fraction of then​mnmavailable cells, was0.0465680.046568,0.1100430.110043,0.0797720.079772, and0.0558990.055899.
The largest transport cost accompanies the largest interpolation distance and
the smallest coupling entropy accompanies the smallest regularization
parameter, with case 1 the sole exception in which the entropy is not the
largest despite the smallest cost.

The point-cloud sizen=m=1000n=m=1000exceeds the500×500500\times 500retention
limit of the NetCDF writer, so the archived plan is a strided block of the
full coupling in all four cases, and the conditional quantities that follow
are formed on that retained block after row renormalization. The mean row
entropy⟨Hi⟩i\langle H_{i}\rangle_{i}of equation (49) was3.1477653.147765,4.0080854.008085,3.6886273.688627, and3.3304343.330434nats for cases 1 through
4, with across-row standard deviations of4.15×10−44.15\times 10^{-4},0.3417700.341770,0.1939100.193910, and0.2497080.249708nats. The across-row dispersion in case 1 is
therefore smaller than in the other three cases by between two and three
orders of magnitude. The corresponding mean perplexities⟨exp⁡(Hi)⟩i\langle\exp(H_{i})\rangle_{i}were23.284023.2840,58.058458.0584,40.701540.7015, and28.914128.9141retained
target points, and the mean peak conditional probabilities⟨maxj⁡P​(j|i)⟩i\langle\max_{j}P(j\,|\,i)\rangle_{i}were0.0708530.070853,0.0478620.047862,0.0549630.054963, and0.0654830.065483.

The block-normalized plan entropies recomputed on the retained block were9.3623739.362373,10.22507110.225071,9.8983039.898303, and9.5450679.545067nats. The difference
between the stored full-plan entropy and the block value takes the values1.3862951.386295,1.3835531.383553,1.3886231.388623, and1.3862431.386243nats and agrees withlog⁡4=1.386294\log 4=1.386294to within2.8×10−32.8\times 10^{-3}nats in every case. The
barycentric displacement magnitudes‖T​(xi)−xi‖\|T(x_{i})-x_{i}\|of
equation (48) had means of0.9949940.994994,0.8190430.819043,0.8222000.822200, and0.4676560.467656, medians of0.9949940.994994,0.8289840.828984,0.8039990.803999,
and0.4763030.476303, and maxima of0.9950370.995037,1.2323091.232309,1.5405451.540545, and0.9899370.989937. In case 1 the mean, median, and maximum agree to within4.3×10−54.3\times 10^{-5}, while in the remaining cases the maximum exceeds the mean by
between0.410.41and0.720.72. Table2collects the coupling
summary.

Figure2shows the barycentric map of each case as
displacement arrows from a strided subset of ninety source points to their
conditional-mean images, overlaid on the source and target clouds. The arrows
in figure2(a) are directed radially outward and are of
visually uniform length. Those in figure2(b) converge
onto the four mixture centers, the arrow bundles originating along the turns
of the spiral and terminating in tight clusters.
Figure2(c) shows arrows of markedly heterogeneous
length and direction. Figure2(d) shows arrows directed
predominantly inward from the outer excursions of the Lissajous curve toward
the trefoil lobes.Figure 2:Barycentric projectionT​(x)=𝔼​[Y|X=x]T(x)=\mathbb{E}[Y\,|\,X=x]of the
entropic coupling, defined in equation (48) and shown
as displacement arrows from source points to their conditional-mean images.
(a) Case 1, circle to circle. (b) Case 2, spiral to Gaussian mixture. (c)
Case 3, two moons to rotated two moons. (d) Case 4, Lissajous curve to
trefoil projection. Source and target clouds are drawn as faint markers.
Arrows are shown for a strided subset of ninety source points per panel for
legibility. Becausen=1000n=1000exceeds the500×500500\times 500storage retention
limit, the map is evaluated on the retained strided block of the coupling
after row renormalization.Table 2:Transport, conditional, and barycentric summary of the optimal
coupling. The transport cost⟨C,π⋆⟩\langle C,\pi^{\star}\rangleand effective
sparsityexp⁡(H​(π⋆))/(n​m)\exp(H(\pi^{\star}))/(nm)are evaluated on the full plan; the
conditional quantities are evaluated on the retained500×500500\times 500block
after row renormalization, and the perplexity is in units of retained target
points.Caseε\varepsilon⟨C,π⋆⟩\langle C,\pi^{\star}\rangleEff. sparsity⟨Hi⟩i\langle H_{i}\rangle_{i}[nats]⟨exp⁡(Hi)⟩i\langle\exp(H_{i})\rangle_{i}⟨‖T​(x)−x‖⟩\langle\|T(x)-x\|\rangle10.021.0100130.0465683.14776523.28400.99499420.050.8081370.1100434.00808558.05840.81904330.030.8662670.0797723.68862740.70150.82220040.040.3132950.0558993.33043428.91410.467656

The bridge marginals reconstructed from these couplings were examined next
through their KDEs. The Scott bandwidth factor returned
by the estimator was0.31620.3162in all four cases, consistent withn−1/(d+4)n^{-1/(d+4)}atn=1000n=1000andd=2d=2. Of the five snapshot times𝒯={0,0.25,0.5,0.75,1}\mathcal{T}=\{0,\,0.25,\,0.5,\,0.75,\,1\}, the two endpoints coincide
with stored frames in every case, whereas the three interior times fall
between stored frames on both the120120-frame and the150150-frame grid and
were therefore obtained by linear temporal interpolation between the
straddling frames. The high-density region countNreg​(t)N_{\mathrm{reg}}(t)of
equation (51) held at unity across all five snapshots in
case 1 and at two across all five snapshots in case 3. In case 2 the count
followed the sequence1,3,4,4,41,\,3,\,4,\,4,\,4, and in case 4 the sequence2,1,1,1,12,\,1,\,1,\,1,\,1. The effective support areaAeff​(t)A_{\mathrm{eff}}(t)of
equation (52) increased monotonically in case 1 from5.650015.65001to14.5764614.57646, rose and then fell in cases 2 and 3 with maxima of8.393798.39379att=0.75t=0.75and6.180536.18053att=0.5t=0.5respectively, and
decreased monotonically in case 4 from11.2894311.28943to8.407378.40737. The support
fraction reached the saturation value1.000001.00000att=0t=0andt=0.25t=0.25in
case 4, and remained at or below0.910410.91041at every snapshot in the other
three cases.

The cloud centroid coincided with the origin to five decimal places at both
endpoints in cases 1 and 4, and departed from the origin by at most1.98×10−31.98\times 10^{-3}at the interior snapshots of case 1. In case 2 the centroid
moved from(−0.00005,−0.12400)(-0.00005,\,-0.12400)att=0t=0to(−0.00787,0.00398)(-0.00787,\,0.00398)att=1t=1. In case 3 the centroid moved from(0.50166,0.25285)(0.50166,\,0.25285)att=0t=0to(0.00000,0.00000)(0.00000,\,0.00000)att=1t=1, a net displacement of magnitude0.561780.56178, with the intermediate values decreasing approximately linearly intt. Table3collects the snapshot summary.

Figure3shows the normalized densityρt†\rho^{\dagger}_{t}as a four-by-five montage, one row per case and one column
per snapshot time. The first row shows an annulus of increasing radius and
decreasing relative thickness. The second row shows the spiral fragmenting
into four separated concentrations. The third row shows two crescent-shaped
ridges whose long axes differ in orientation between the first and the last
column. The fourth row shows four bright concentrations att=0t=0evolving
toward a three-lobed pattern att=1t=1. The spatial extent of each row is
the joint bounding box of the clouds of that case, so panel areas are not
comparable between rows.Figure 3:Gaussian kernel density estimates of the bridge marginalρt\rho_{t},
normalized to the per-panel maximum and evaluated on a140×140140\times 140grid.
Rows correspond to cases 1 through 4 from top to bottom, columns to the
snapshot timest=0t=0,0.250.25,0.50.5,0.750.75, and11from left to right.
Panels (a)–(e) show case 1, (f)–(j) case 2, (k)–(o) case 3, and (p)–(t)
case 4. Normalized density below0.030.03is rendered white. The spatial extent
of each row is the joint bounding box of the source, target, and intermediate
clouds of that case and therefore differs between rows.Table 3:Kernel density estimate summary at the five snapshot times.NregN_{\mathrm{reg}}is the high-density region count of
equation (51),AeffA_{\mathrm{eff}}the effective support
area of equation (52), and the support fraction the
proportion of the per-case panel at which the normalized density is at least0.030.03. Effective areas and support fractions are referred to the per-case
bounding box and are not comparable across cases.CasettNregN_{\mathrm{reg}}AeffA_{\mathrm{eff}}Support fractionCentroid(x¯,y¯)(\bar{x},\bar{y})10.0015.650010.38735(0.00000,0.00000)(0.00000,\,0.00000)0.2518.927570.61148(−0.00196,0.00031)(-0.00196,\,0.00031)0.50112.255400.82862(0.00017,−0.00003)(0.00017,\,-0.00003)0.75114.256600.91000(0.00170,0.00020)(0.00170,\,0.00020)1.00114.576460.91041(0.00000,0.00000)(0.00000,\,0.00000)20.0016.059070.40842(−0.00005,−0.12400)(-0.00005,\,-0.12400)0.2537.863390.53005(−0.00586,−0.09478)(-0.00586,\,-0.09478)0.5048.385750.61194(−0.01107,−0.06721)(-0.01107,\,-0.06721)0.7548.393790.63842(−0.01332,−0.02325)(-0.01332,\,-0.02325)1.0047.920230.60842(−0.00787,0.00398)(-0.00787,\,0.00398)30.0025.013340.48020(0.50166,0.25285)(0.50166,\,0.25285)0.2525.943720.57036(0.37584,0.19356)(0.37584,\,0.19356)0.5026.180530.59740(0.25089,0.12248)(0.25089,\,0.12248)0.7525.900770.56883(0.12806,0.07345)(0.12806,\,0.07345)1.0024.985730.47653(0.00000,0.00000)(0.00000,\,0.00000)40.00211.289431.00000(0.00000,0.00000)(0.00000,\,0.00000)0.25111.164931.00000(0.00194,0.00021)(0.00194,\,0.00021)0.50110.603570.99128(−0.00249,−0.00185)(-0.00249,\,-0.00185)0.7519.639790.93464(0.00168,−0.00169)(0.00168,\,-0.00169)1.0018.407370.83362(0.00000,0.00000)(0.00000,\,0.00000)

Frame-wise descriptors of the same trajectories complete the picture. The
Kozachenko–Leonenko estimator of equation (53) returnedH^​(ρ0)=−1.396695\hat{H}(\rho_{0})=-1.396695,−0.674706-0.674706,0.2589290.258929, and0.9387050.938705nats at
the source endpoint of cases 1 through 4, andH^​(ρ1)=−0.010401\hat{H}(\rho_{1})=-0.010401,0.3981660.398166,0.2448490.244849, and−0.054806-0.054806nats at the target endpoint. The
corresponding differencesH^​(ρ1)−H^​(ρ0)\hat{H}(\rho_{1})-\hat{H}(\rho_{0})were1.3862941.386294,1.0728721.072872,−0.014080-0.014080, and−0.993511-0.993511nats, the value recorded for case 1
agreeing withlog⁡4=1.386294\log 4=1.386294to six decimal places. Both endpoint clouds
of cases 1 and 4 lie on parametric curves to which no perturbation noise was
applied, as recorded by the source and target noise of0.00.0in the case 1
log, so for those two cases the endpoint estimates are formed on samples
whose support is one-dimensional and no interpretation as a two-dimensional
differential entropy is claimed here.

At the midpoint the estimator returnedH^​(ρ1/2)=1.003174\hat{H}(\rho_{1/2})=1.003174,1.3892571.389257,1.1957291.195729, and1.8646511.864651nats, exceeding the corresponding
noise-only referenceHdiff​(1/2)H_{\mathrm{diff}}(1/2)of
equation (55), which takes the values−2.460440-2.460440,−1.544150-1.544150,−2.054975-2.054975, and−1.767293-1.767293nats, by3.4636143.463614,2.9334072.933407,3.2507043.250704, and3.6319443.631944nats. The entropy attained an interior maximum in
every case, of1.0694911.069491,1.4239681.423968,1.2359891.235989, and1.9452791.945279nats,
located att=0.6303t=0.6303,0.43700.4370,0.47900.4790, and0.42280.4228respectively. The
mean across frames of the ninety-five-percent half-width onH^\hat{H}lay
between0.0299530.029953and0.0336220.033622nats in all four cases.

The RMS dispersion of equation (57) took the values1.0005001.000500,1.5012051.501205, and2.0010012.001001att=0t=0,1/21/2, and11in case 1,
increasing monotonically and departing from linearity at the midpoint by4.54×10−44.54\times 10^{-4}, which is below the mean half-width of1.574×10−31.574\times 10^{-3}for that case. In case 2 the dispersion increased monotonically from0.8756590.875659through1.1702031.170203to1.5143691.514369. In case 3 it fell from0.9983020.998302to0.9402950.940295at the midpoint before returning to0.9994360.999436, with
a recorded maximum of1.0033151.003315att=0.9832t=0.9832. In case 4 it decreased
monotonically from1.5007511.500751through1.3035081.303508to1.1185931.118593. The mean
half-widths on the dispersion ranged from1.574×10−31.574\times 10^{-3}to9.230×10−39.230\times 10^{-3}across the four cases.

The eccentricity of equation (58) remained below the
resolution thresholde=0.25e=0.25at every frame in cases 1 and 4, spanning[0.000000,0.147554][0.000000,\,0.147554]and[0.000064,0.207380][0.000064,\,0.207380]respectively, so the
principal-axis angle is reported as undefined for those two cases and no
reorientation is quoted. In case 2 the eccentricity spanned[0.042739,0.471671][0.042739,\,0.471671]and the angle was resolved at7676of120120frames, giving first
and last resolved values of−37.6281∘-37.6281^{\circ}and−59.1271∘-59.1271^{\circ}and a net
folded reorientation of−21.4990∘-21.4990^{\circ}, against a mean
ninety-five-percent half-width of12.0446∘12.0446^{\circ}. In case 3 the eccentricity
spanned[0.141166,0.883400][0.141166,\,0.883400]and the angle was resolved at114114of120120frames, giving first and last resolved values of−18.6137∘-18.6137^{\circ}and71.3167∘71.3167^{\circ}and a net folded reorientation of89.9304∘89.9304^{\circ}, against a
mean ninety-five-percent half-width of2.8204∘2.8204^{\circ}. The case 3
reorientation therefore departs from the imposed rotation of90∘90^{\circ}by0.0696∘0.0696^{\circ}, a discrepancy some forty times smaller than the mean
half-width of the estimate, whereas the case 2 reorientation is smaller in
magnitude than twice its mean half-width. Table4collects
the frame-wise summary.

Figure4shows the four frame-wise descriptors
against interpolation time together with their subsampling uncertainty bands.
Figure4(a) shows a concave profile in every case,
rising steeply away fromt=0t=0and falling steeply towardt=1t=1.
Figure4(b) shows the monotone linear profile of
case 1, the monotone increase of case 2, the shallow interior minimum of
case 3, and the monotone decrease of case 4.
Figure4(c) shows the low, flat eccentricity traces
of cases 1 and 4 alongside the pronounced interior minimum of case 3 att≈0.5t\approx 0.5. Figure4(d) shows the resolved
orientation segments, the case 3 trace being interrupted over the interval on
which its eccentricity falls below threshold and resuming approximately90∘90^{\circ}from its earlier level.Figure 4:Frame-wise descriptors of the bridge marginal against interpolation
timett. (a) Kozachenko–Leonenko differential entropyH^​(ρt)\hat{H}(\rho_{t})of
equation (53) atk=5k=5. (b) RMS dispersion of
equation (57). (c) Eccentricity of
equation (58). (d) Principal-axis orientation, reported
only at frames whose eccentricity is at least0.250.25and unwrapped within,
but never across, contiguous resolved runs. Shaded bands are the
ninety-five-percent intervals obtained by subsampling without replacement atB=80B=80replicates andm/n=0.8m/n=0.8, rescaled to full sample size through
equation (60). Cases 1 and 4 are absent from panel
(d), their eccentricity remaining below the resolution threshold at every
frame.Table 4:Frame-wise informational and geometric summary along the bridge.
Entropies are Kozachenko–Leonenko estimates of
equation (53) in nats, evaluated atk=5k=5. The
reorientation is the folded net change in principal-axis angle, quoted with
the mean ninety-five-percent half-width across resolved frames; it is
undefined for cases 1 and 4, whose eccentricity remains below the resolution
threshold at every frame. The endpoint entropies of cases 1 and 4 are
evaluated on noiseless parametric curves.Caseε\varepsilonH^​(ρ0)\hat{H}(\rho_{0})H^​(ρ1/2)\hat{H}(\rho_{1/2})H^​(ρ1)\hat{H}(\rho_{1})maxt⁡H^\max_{t}\hat{H}(tt)maxt⁡rms\max_{t}\mathrm{rms}Reorientation [deg]10.02−1.3967-1.39671.00321.0032−0.0104-0.01041.0695 (0.6303)2.0010—20.05−0.6747-0.67471.38931.38930.39820.39821.4240 (0.4370)1.5144−21.499±12.045-21.499\pm 12.04530.030.25890.25891.19571.19570.24480.24481.2360 (0.4790)1.003389.930±2.82089.930\pm 2.82040.040.93870.93871.86471.8647−0.0548-0.05481.9453 (0.4228)1.5008—

All wall-clock timings reported in this section were measured on a
single laptop, a Lenovo ThinkPad T440s (model 20AQ006HUS) with an
Intel Core i7-4600U processor (four logical cores at a maximum clock
of3.303.30GHz), running Linux Lite 6.6 (x86_64) under Linux kernel
5.15.0-185-generic, and therefore characterize the method on commodity
hardware rather than an optimized high-performance configuration. The run logs record the wall-clock cost of each case, decomposed into the
generation of the source and target clouds, solver initialization, the
Sinkhorn solve, trajectory generation, data serialization, and animation
rendering. The solve occupied2.8972.897,9.1349.134,9.1749.174, and8.2178.217seconds
for cases 1 through 4, cloud generation and serialization together remained
below0.40.4seconds in every case, and the total wall-clock time was61.34161.341,54.38354.383,59.96559.965, and75.24475.244seconds. Animation rendering
accounted for between82.5%82.5\%and91.8%91.8\%of the total in every case, so the
solver and its diagnostics constitute a minor fraction of the end-to-end
runtime. The single-sweep case 1 solve nevertheless required2.8972.897seconds,
larger than a per-sweep extrapolation from the other cases would predict,
because the just-in-time compilation of the solver kernels is performed once
per process and is charged to the first solve. Table5collects the timing breakdown.Table 5:Wall-clock timing breakdown from the run logs, in seconds. The solve
column is the log-domain Sinkhorn iteration and includes the one-time
just-in-time compilation of the solver kernels; the visualization column is
the animation rendering. The thread count was left to automatic selection in
all runs.CaseDistributionsSolver initSolveTrajectorySerializationVisualizationTotal10.0000.2482.8971.8110.08756.29661.34120.0010.0059.1340.0870.29244.86354.38330.0030.0409.1740.1050.11050.53259.96540.0000.0058.2170.1060.07666.83975.244

## 4Discussion

The four demonstration cases place the log-domain formulation in the regime
for which it was adopted. The ratiomaxi​j⁡Ci​j/ε\max_{ij}C_{ij}/\varepsilonlies
between252252and400400across the four cases, so the Gibbs kernel entriesKi​j=exp⁡(−Ci​j/ε)K_{ij}=\exp(-C_{ij}/\varepsilon)of (16) span several
hundred decades and underflow the smallest representable double-precision
number over most of their range. An exponential-domain implementation of the
Sinkhorn recursion would therefore fail outright at these settings, whereas
the potentials(f,g)(f,g)of (22) remained bounded, the
marginal residual reached10−910^{-9}, and the reported marginal fidelity was
unity to eight decimal places in every case. This behavior is consistent with
the motivation for log-domain and stabilized scaling
schemes[34,31,6].

The residual histories are geometric over approximately eight decades, in
qualitative agreement with the classical theory of the Sinkhorn recursion,
which establishes convergence and a geometric rate through the contraction
of the scaling map in the Hilbert projective
metric[39,40,12,23]. The
quantitative content of that theory is nevertheless inaccessible at the
present parameters. The Birkhoff contraction ratio associated with the
kernel (16) isκ=(η−1)/(η+1)\kappa=(\sqrt{\eta}-1)/(\sqrt{\eta}+1)withη=exp⁡(maxi​j⁡Ci​j/ε)\eta=\exp(\max_{ij}C_{ij}/\varepsilon)[12],
so that1−κ1-\kapparanges from about10−5510^{-55}to10−8710^{-87}over the
four cases. The guaranteed rate is thus numerically indistinguishable from
unity and predicts no useful decay, while the observed per-iteration factors
lie between0.9660.966and0.9760.976. The measured decay is therefore an
asymptotic local rate attained near the fixed point rather than a
realization of the worst-case bound, and the gap between the two is many
orders of magnitude. Consistent with this, the three fitted factors do not
order withε\varepsilon. Because the present design variesε\varepsilonand the source and target geometry together, and because only three cases
admit a fit, the data cannot separate the two influences, and no relation
between the contraction rate and the regularization parameter is claimed
here. A sweep inε\varepsilonat fixed geometry would be required to
address that question and is left to future work.

Case 1 warrants separate comment, since its convergence at the first
residual evaluation is a structural rather than a numerical result. The
source and target of (37) are both sampled at angles that
are equispaced up to a global phase, so the squared-distance cost satisfiesCi​j=r02+r12−2​r0​r1​cos⁡(2​π​(i−j)/n+Δ​φ)C_{ij}=r_{0}^{2}+r_{1}^{2}-2r_{0}r_{1}\cos(2\pi(i-j)/n+\Delta\varphi)and depends on the indices only through(i−j)modn(i-j)\bmod n. The cost matrix is
consequently circulant, and for a circulant cost with uniform marginals the
dual potentials that solve (14) are constant vectors,
which the updates (24)–(25) reach in a single
sweep from the zero initialization. The recorded residual of3.771506×10−153.771506\times 10^{-15}is the floating-point signature of an exactly attained solution
rather than of a rapidly converging iteration. Two independent diagnostics
corroborate the interpretation: the row entropies of the conditional
coupling have a standard deviation of4.15×10−44.15\times 10^{-4}nats across the
retained block, every row being a cyclic shift of every other, and the
barycentric displacement has mean and maximum differing by4.3×10−54.3\times 10^{-5}. Case 1 accordingly verifies that the implementation recovers the
closed-form solution where one exists, but it does not exercise the
iteration, and it should not be read as a convergence baseline.

The conditional structure of the couplings behaves broadly as the
regularization would suggest, the most diffuse coupling occurring at the
largestε\varepsilonand the sharpest at the smallest. This ordering is
carried by the effective sparsityexp⁡(H​(π⋆))/(n​m)\exp(H(\pi^{\star}))/(nm), which rises from0.0465680.046568atε=0.02\varepsilon=0.02to0.1100430.110043atε=0.05\varepsilon=0.05, and
which measures the joint perplexity of the plan as a fraction of then​mnmavailable cells. The ordering is not strict at the level of the conditional
perplexity, since case 3 atε=0.03\varepsilon=0.03carries more effective
targets per source than case 4 atε=0.04\varepsilon=0.04: the diffuseness of a
row is set byε\varepsilonrelative to the local separation of target points
rather than byε\varepsilonalone, and the four geometries differ in that
separation. The transport cost recorded in the logs is likewise geometric in
origin, being largest for case 1, whose supports are separated by a full unit
of radius, and smallest for case 4, whose interleaved lobes require the least
displacement.

Interpretation of the reported conditional quantities requires care on a
separate count. The plan is archived on a strided500×500500\times 500block of a1000×10001000\times 1000coupling, which retains one quarter of the entries. If the
retained entries are representative of the whole, the renormalized block
entropy satisfiesHblock=H​(π⋆)−log⁡4H_{\mathrm{block}}=H(\pi^{\star})-\log 4, and the
differences reported above agree withlog⁡4\log 4to within2.8×10−32.8\times 10^{-3}nats in all four cases. That agreement is an internal consistency check that
the strided block does carry a representative quarter of the mass. The same
argument applied at the level of a single row, where one half of the targets
is retained, givesHiblock=Hifull−log⁡2H_{i}^{\mathrm{block}}=H_{i}^{\mathrm{full}}-\log 2and
hence a perplexity that is understated by a factor of two. The reported
values of23.284023.2840,58.058458.0584,40.701540.7015, and28.914128.9141therefore correspond
to full-plan effective target counts of approximately46.646.6,116.1116.1,81.381.3, and57.857.8, and the reported peak conditional probabilities
correspondingly overstate the full-plan values by close to a factor of two.
The barycentric displacements are unaffected, the conditional mean over a
uniformly strided subset of a smooth conditional being unbiased. Archiving
the full plan, at a cost of8​n28n^{2}bytes, would remove the need for this
correction and is the preferable course for point-cloud sizes at which the
storage remains tractable.

The mean barycentric displacement of case 1,0.9949940.994994, falls short of the
exact radial separation of unity by0.5%0.5\%. The shortfall is not a
numerical defect but a property of the barycentric projection at finite
regularization. The conditional expectation (48)
averages the target points over an arc whose angular width is set byε\varepsilon, and the average of points on a circle over an arc of nonzero
width lies strictly inside that circle. The image radius is therefore smaller
than22, and the deficit contracts asε→0+\varepsilon\to 0^{+}, in which limit
the coupling concentrates on the graph of the Brenier map and the barycentric
projection recovers it exactly[3,30,4]. The
same mechanism underlies the difference between the barycentric map and the
sampled bridge of (33), the former reporting a
conditional mean and the latter a draw from the conditional itself.

The entropy estimates require the most careful reading of any quantity
reported here, and the endpoint values of cases 1 and 4 do not admit the
interpretation that their name suggests. The Kozachenko–Leonenko estimator
and its analysis presuppose a distribution that is absolutely continuous
with respect to Lebesgue measure onℝd\mathbb{R}^{d}, a hypothesis under which
the bias and variance have been characterized in
detail[24,9,2]. The source and target
clouds of cases 1 and 4 carry no perturbation noise, as the source and target
noise of0.00.0recorded in the case 1 log confirms, and they lie exactly on
one-dimensional parametric curves, which are Lebesgue-null in the plane. The
corresponding differential entropy is not defined, and the finite values
returned by (53) are artifacts of finite sample size. The
mechanism is explicit in the estimator: fornnpoints spread along a
rectifiable curve of lengthLL, thekk-th nearest-neighbor distances scale
asri∼L/nr_{i}\sim L/n, so that the sum in (53) contributes2​log⁡(L/n)2\log(L/n)while the digamma term contributeslog⁡n\log n, givingH^​(ρ)≈const+2​log⁡L−log⁡n\hat{H}(\rho)\approx\mathrm{const}+2\log L-\log n. Two consequences follow
and both are visible in the reported numbers. First, the estimate diverges
logarithmically as the sample grows, so the recorded value ofH^​(ρ0)=−1.396695\hat{H}(\rho_{0})=-1.396695for case 1 is a statement aboutn=1000n=1000and not about the
source distribution. Second, differencing two curve-supported estimates at
equalnncancels the sample-size term and isolates2​log⁡(L1/L0)2\log(L_{1}/L_{0}). For
case 1 both endpoints are circles of radii11and22, so the prediction is2​log⁡2=1.3862942\log 2=1.386294nats, which is precisely the recorded value ofH^​(ρ1)−H^​(ρ0)\hat{H}(\rho_{1})-\hat{H}(\rho_{0})to six decimal places. The quantity tabulated as
the net entropy production of case 1 is therefore a measurement of the ratio
of two curve lengths. The corresponding value for case 4,−0.993511-0.993511nats,
carries the same character and reflects the trefoil projection being shorter
than the Lissajous curve of equal parametric sampling. Case 3 provides the
internal control that confirms the diagnosis, its endpoints carrying additive
noise of standard deviation0.050.05and therefore being genuinely
two-dimensional: its recorded difference of−0.014080-0.014080nats is consistent
with zero, as the isometry relating its two endpoint distributions requires.
Case 2, whose source carries only a small perturbation of standard deviation0.010.01while its target is a genuine mixture of Gaussians, occupies an
intermediate position and its endpoint difference should not be interpreted
quantitatively either. The conservative reading of the present data is thatH^​(ρt)\hat{H}(\rho_{t})is informative on the open intervalt∈(0,1)t\in(0,1), where
the bridge noise of varianceε​t​(1−t)\varepsilon\,t(1-t)renders every marginal
absolutely continuous, and that the two endpoint columns should be excluded
from any comparison. Applying a small perturbation to the case 1 and case 4
generators would place all four cases on a common footing and is the natural
remedy.

Read on the open interval, the entropy profiles are consistent with the
structure of the bridge. Every case attains an interior maximum, which
follows from the bridge varianceε​t​(1−t)\varepsilon\,t(1-t)of (19) vanishing at both ends and peaking att=1/2t=1/2[11]. The measured midpoint entropies exceed the
noise-only reference (55) by between2.932.93and3.633.63nats, confirming that the marginal at the midpoint is not dominated by
the diffusive term and retains substantial geometric structure inherited from
the endpoints. The maxima are displaced fromt=1/2t=1/2in a direction that
tracks the deterministic part of the interpolation: case 3, whose endpoints
are related by an isometry, peaks att=0.4790t=0.4790, closest to the symmetric
value, whereas case 1, whose support lengthens monotonically, peaks late att=0.6303t=0.6303and case 4, whose support shortens, peaks early att=0.4228t=0.4228.
The symmetric noise contribution alone would place every maximum att=1/2t=1/2, so the displacement measures the asymmetry of the drift term.

The geometric descriptors supply the principal quantitative verification of
the pipeline. The target of case 3 is generated by rotating a two-moons cloud
throughπ/2\pi/2, and the recovered net reorientation of the covariance
principal axis is89.9304∘89.9304^{\circ}, departing from the imposed value by0.0696∘0.0696^{\circ}, roughly forty times smaller than the mean
ninety-five-percent half-width of2.8204∘2.8204^{\circ}. The recovery is achieved
across a masked interval neart=1/2t=1/2over which the cloud passes through
near-isotropy, the eccentricity falling to0.1411660.141166, and over which the
principal axis is genuinely unobservable. Declining to unwrap the angle
across that gap costs nothing here, since the two resolved segments differ by
approximately the imposed rotation, and it avoids attributing to the data a
branch choice the data do not determine[29]. The contrast with
case 2 is instructive: its net reorientation of−21.4990∘-21.4990^{\circ}is smaller
in magnitude than twice its mean half-width of12.0446∘12.0446^{\circ}and is
resolved at only7676of120120frames, so the present data do not support a
claim of net axis reorientation in that case. Cases 1 and 4 remain below the
eccentricity threshold at every frame, which is the expected behavior for a
circle and for two curves possessing rotational symmetry of order greater
than two, whose covariance is isotropic by construction.

The timing breakdown recorded in the logs situates the computational cost of
the method. The Sinkhorn solve occupied between2.8972.897and9.1749.174seconds
per case, and the generation of the distributions, the trajectory, and the
serialized archive together remained below one second in every case, so the
transport computation and its diagnostics are a minor part of the end-to-end
runtime. Animation rendering dominated the total, accounting for between82.5%82.5\%and91.8%91.8\%of the wall-clock time, which reflects a design choice
to emit a rendered interpolation film rather than a property of the solver.
The single-sweep case 1 nevertheless spent2.8972.897seconds in the solve,
because the just-in-time compilation of the numerical
kernels[27]is performed once per process and charged to the
first solve; the compiled cost per sweep, inferred from the multi-hundred
sweep cases, is on the order of ten milliseconds. Because the thread count
was left to automatic selection in every run and the bridge sampler draws its
randomness within a thread-parallel region, the timings and the sampled
trajectories are tied to the thread configuration of the host, and bitwise
reproducibility across differing thread counts is not guaranteed, in common
with the associative reordering permitted by the compiler options adopted
here[13].

Three features of the analysis limit the strength of the conclusions and are
stated here rather than left to inference. First, the case 3 target cloud has
its centroid at the origin while the source cloud has its centroid at(0.50166,0.25285)(0.50166,0.25285), so the rigid motion realized between the two clouds is a
rotation composed with a translation of magnitude0.561780.56178rather than a
rotation about a common centroid. The transport cost of0.8662670.866267and the
barycentric displacements of case 3 accordingly contain a translational
contribution and are not a pure measure of angular reorganization. The
covariance-based descriptors are translation-invariant and are unaffected, so
the recovery of the rotation angle discussed above is not compromised.
Second, the three interior snapshot times of the density montage do not
coincide with stored frames on either the120120-frame or the150150-frame grid
and are obtained by linear interpolation between straddling frames. Because
consecutive frames are independent draws from their respective marginals
rather than points of a common Lagrangian path, a weighted blend of two such
frames with weightswwand1−w1-wcarries bridge noise of variance reduced
by a factorw2+(1−w)2w^{2}+(1-w)^{2}, equal to0.50.5att=1/2t=1/2and0.6250.625att=0.25t=0.25andt=0.75t=0.75, and additionally replaces each particle’s target by a
convex combination of two independently drawn targets. The interior panels
therefore understate the dispersion ofρt\rho_{t}and are contracted slightly
toward the barycentric image. ChoosingNfN_{f}so that the snapshot times fall
on stored frames, for whichNf=121N_{f}=121suffices, would remove the artifact.
Third, the region countNreg​(t)N_{\mathrm{reg}}(t)of (51) is a
count of connected components of a fixed super-level set of a KDE
and is therefore contingent on both the level and the
bandwidth[37,38], and it is not a topological
invariant of the underlying support. Its value is interpretable where the
target possesses well-separated components, as in the sequence1,3,4,4,41,3,4,4,4of case 2, which tracks the fragmentation of a connected curve into the
four components of the mixture. It is less informative for the ridge-like
supports of cases 1 and 4. The support fraction is referred to a per-case
bounding box, saturates at unity for case 4 at the first two snapshots, and
should not be compared across cases; the effective area, which carries units
of area through the cell-area factor in (52), is the
more robust of the two coverage measures.

Several further limitations bound the scope of the present study. All four
cases fixn=m=1000n=m=1000andd=2d=2, so neither the scaling of the solver
with point-cloud size nor its behavior in higher dimensions is assessed here;
theO​(n​m)O(nm)cost per sweep and the8​n​m8nm-byte footprint of the dense cost
matrix are the binding constraints on the former. The regularization is fixed
within each case, so the entropic bias of the coupling is not resolved as a
function ofε\varepsilon. The diagnostics are computed on single
realizations at a fixed base seed, and the uncertainty bands quantify
sampling variability within a realization rather than variability across
independent runs. Finally, the four cases are constructed rather than
measured, and the extent to which the observed behavior transfers to
empirical point clouds arising in applications, where the marginals are noisy
and possibly of unequal mass, remains to be established. The unbalanced and
multi-marginal extensions of the scaling
framework[6,1]provide the natural setting in which
those questions would be posed.

## 5Conclusions

This work presentedanyakrakusuma, a Python library that solves the
discrete static Schrödinger bridge problem through a log-domain
Sinkhorn–Knopp iteration and reconstructs the entropic interpolation between
two empirical point clouds, together with a diagnostic pipeline exercised on
four idealized planar cases spanning a circle-to-circle dilation, a
spiral-to-mixture fragmentation, a rigid reorientation of two moons, and a
Lissajous-to-trefoil deformation. The log-domain formulation was necessary
rather than merely convenient at the parameters studied: the
cost-to-regularization ratio reached four hundred, at which the Gibbs kernel
underflows double precision across most of its range, yet the iteration
reached a marginal residual of10−910^{-9}and unit marginal fidelity in every
case, with geometric residual decay over approximately eight decades at
per-iteration contraction factors between0.9660.966and0.9760.976. These are
local rates attained near the fixed point and lie many orders of magnitude
below the worst-case Hilbert-metric bound, which is vacuous at these settings;
the circle-to-circle case converged in a single sweep because its equispaced
angular sampling renders the cost matrix circulant, a structural exactness
that serves as a correctness check rather than a convergence baseline. The
covariance analysis recovered the imposed ninety-degree reorientation of the
two-moons case to within0.07∘0.07^{\circ}, roughly forty times smaller than the
estimator’s uncertainty and across a masked interval of near-isotropy on which
the principal axis is unobservable, which is the strongest quantitative
validation the pipeline provides.

The analysis equally delimited what the diagnostics cannot support, and these
boundaries are as much a part of the result as the recoveries: the
differential entropy is well defined only on the open interpolation interval,
the endpoint estimates of the two noiseless cases measure curve length rather
than entropy, the conditional coupling statistics carry an exact
factor-of-two offset from the subsampled plan storage, the rotation case
realizes an unintended rigid translation, and the interior density snapshots
are temporally interpolated between independently sampled frames, each with a
stated remedy in perturbing the noiseless generators, archiving the full plan,
recentering the rotated target, and aligning the frame count with the snapshot
times. Future work follows directly from these limitations: a regularization
sweep at fixed geometry would separate the influence ofε\varepsilonon the
contraction rate from that of the transport geometry, while systematic study
of the solver’s scaling with sample size and dimension, replacement of the
dense cost matrix by stabilized sparse scaling for larger
problems[34], and extension to unbalanced and multi-marginal
settings[6,1]would move the library from idealized
demonstrations toward the empirical point clouds that motivate entropic
transport in practice, with the software, configurations, and diagnostic
scripts released openly so that the present results can be reproduced and
extended.

## Acknowledgements

The authors used Claude Sonnet 5 (Anthropic, PBC) solely as a
writing-assistance tool to refine English vocabulary and grammar
during the preparation of this manuscript. All scientific content,
interpretations, analyses, conclusions, and any remaining linguistic
imperfections are the sole responsibility of the authors.

## Funding

This study was funded by the Indonesian Ministry of Education,
Culture, Research, and Technology 2026
(169/C3/DT.05.00/PL-BARU/2026).

## Author Contributions

S.H.S.H.: Conceptualization, Data curation, Formal analysis,
Investigation, Methodology, Software, Visualization, Validation,
Writing – original draft.D.E.I.: Funding acquisition,
Project administration, Supervision, Resources, Writing – review and
editing.A.W.J.: Supervision, Writing – review and editing.S.F.B.: Supervision, Writing – review and editing.C.S.D.: Supervision, Writing – review and editing.E.R.: Supervision, Writing – review and editing.A.P.: Supervision, Writing – review and editing.R.D.K.: Supervision, Writing – review and editing.R.S.: Supervision, Resources, Writing – review and editing.D.J.P.: Supervision, Resources, Writing – review and
editing.

## Data Availability

Theanyakrakusumalibrary source code is available on GitHub athttps://github.com/sandyherho/anyakrakusumaand from the Python Package Index athttps://pypi.org/project/anyakrakusuma/. The supplementary data-analysis scripts that reproduce the diagnostic metrics and figures are available athttps://github.com/sandyherho/suppl_anyakrakusuma. All supplementary outputs, comprising the raw NetCDF archives, the computed diagnostic metrics, the run logs and timing breakdowns, and all figures, are permanently archived on the Open Science Framework athttps://doi.org/10.17605/OSF.IO/VQWF4. The library, the supplementary scripts, and the archived outputs are all released under the MIT license.

## References
- [1]Benamou, J.-D.; Carlier, G.; Cuturi, M.; Nenna, L.; Peyré, G.
Iterative Bregman Projections for Regularized Transportation Problems.SIAM J. Sci. Comput.2015,37(2),
A1111–A1138.https://doi.org/10.1137/141000439.
- [2]Berrett, T.B.; Samworth, R.J.; Yuan, M. Efficient multivariate
entropy estimation viakk-nearest neighbour distances.Ann. Stat.2016,47(1), 288–318.https://doi.org/10.1214/18-AOS1688.
- [3]Brenier, Y. Polar factorization and monotone rearrangement of
vector-valued functions.Commun. Pure Appl. Math.1991,44(4),
375–417.https://doi.org/10.1002/cpa.3160440402.
- [4]Carlier, G.; Duval, V.; Peyré, G.; Schmitzer, B. Convergence of
Entropic Schemes for Optimal Transport and Gradient Flows.SIAM J. Math. Anal.2017,49(2),
1385–1418.https://doi.org/10.1137/15M1050264.
- [5]Chen, Y.; Georgiou, T.T.; Pavon, M. On the Relation Between Optimal
Transport and Schrödinger Bridges: A Stochastic Control Viewpoint.J. Optim. Theory Appl.2016,169,
671–691.https://doi.org/10.1007/s10957-015-0803-z.
- [6]Chizat, L.; Peyré, G.; Schmitzer, B.; Vialard, F.-X. Scaling
algorithms for unbalanced optimal transport problems.Math. Comp.2018,87, 2563–2609.https://doi.org/10.1090/mcom/3303.
- [7]Cuturi, M. Sinkhorn Distances: Lightspeed Computation of Optimal
Transport. InAdvances in Neural Information Processing
Systems 26 (NeurIPS 2013); Curran Associates, Inc., 2013;
pp. 2292–2300.https://proceedings.neurips.cc/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html.
- [8]De Bortoli, V.; Thornton, J.; Heng, J.; Doucet, A. Diffusion
Schrödinger Bridge with Applications to Score-Based Generative
Modeling. InAdvances in Neural Information Processing
Systems 34 (NeurIPS 2021); Curran Associates, Inc., 2021;
pp. 17695–17709.https://proceedings.neurips.cc/paper/2021/hash/940392f5f32a7ade1cc201767cf83e31-Abstract.html.
- [9]Delattre, S.; Fournier, N. On the Kozachenko–Leonenko entropy
estimator.J. Stat. Plan. Inference2017,185,
69–93.https://doi.org/10.1016/j.jspi.2017.01.004.
- [10]Efron, B.; Tibshirani, R.J.An Introduction to the
Bootstrap; Chapman & Hall/CRC: New York, NY, 1994.https://doi.org/10.1201/9780429246593.
- [11]Föllmer, H. Random fields and diffusion processes. InÉcole d’Été de Probabilités de Saint-Flour
XV–XVII, 1985–87; Hennequin, P.L., Ed.; Lecture Notes in
Mathematics, Vol. 1362; Springer: Berlin, Heidelberg, Germany, 1988;
pp. 101–203.https://doi.org/10.1007/BFb0086180.
- [12]Franklin, J.; Lorenz, J. On the scaling of multidimensional matrices.Linear Algebra Appl.1989,114–115,
717–735.https://doi.org/10.1016/0024-3795(89)90490-4.
- [13]Goldberg, D. What every computer scientist should know about
floating-point arithmetic.ACM Comput. Surv.1991,23(1), 5–48.https://doi.org/10.1145/103162.103163.
- [14]Harris, C.R.; Millman, K.J.; van der Walt, S.J.; Gommers, R.;
Virtanen, P.; Cournapeau, D.; Wieser, E.; Taylor, J.; Berg, S.;
Smith, N.J.; Kern, R.; Picus, M.; Hoyer, S.; van Kerkwijk, M.H.;
Brett, M.; Haldane, A.; del Río, J.F.; Wiebe, M.; Peterson, P.;
Gérard-Marchant, P.; Sheppard, K.; Reddy, T.; Weckesser, W.;
Abbasi, H.; Gohlke, C.; Oliphant, T.E. Array programming with NumPy.Nature2020,585, 357–362.https://doi.org/10.1038/s41586-020-2649-2.
- [15]Herho, S.H.S.; Anwar, I.P.; Khadami, F.; Handayani, A.P.;
Sujatmiko, K.A.; Kasim, K.; Suwarman, R.; Irawan, D.E.dewi-Kadita: a Python library for idealized fish schooling
simulation with entropy-based diagnostics.J. Phys. Commun.2026,10(6), 065002.https://doi.org/10.1088/2399-6528/ae7177.
- [16]Herho, S.H.S.; Anwar, I.P.; Khadami, F.; Ndruru, T.R.E.B.N.;
Suwarman, R.; Irawan, D.E.wave-attenuation-1d: An Idealized
One-Dimensional Framework for Wave Attenuation through Coastal
Vegetation using Numba-Accelerated Shallow Water Equations.J. Theor. Appl. Mech.2026,56(1), 89–102.https://doi.org/10.55787/jtams.2026.1.AI00236.
- [17]Herho, S.H.S.; Fajary, F.R.; Herho, K.E.P.; Anwar, I.P.;
Suwarman, R.; Irawan, D.E. Reappraising double pendulum dynamics
across multiple computational platforms.CLEI Electron. J.2025,28(1), 10.https://doi.org/10.19153/cleiej.28.1.10.
- [18]Herho, S.H.S.; Kaban, S.N.; Nugraha, C. OptionMC: a Python package
for Monte Carlo pricing of European options.Int. J. Data Sci.2025,6(2), 70–84.https://doi.org/10.18517/ijods.6.2.70-84.2025.
- [19]Herho, S.H.S.; Trilaksono, N.J.; Fajary, F.R.; Napitupulu, G.;
Anwar, I.P.; Khadami, F.; Irawan, D.E.kh2d-solver: a Python
library for idealized two-dimensional incompressible Kelvin–Helmholtz
instability.Appl. Comput. Mech.2025,19(2), 125–156.https://doi.org/10.24132/acm.2025.1040.
- [20]Hoyer, S.; Hamman, J.J. xarray: N-D Labeled Arrays and Datasets in
Python.J. Open Res. Softw.2017,5(1), 10.https://doi.org/10.5334/jors.148.
- [21]Hunter, J.D. Matplotlib: A 2D Graphics Environment.Comput. Sci. Eng.2007,9(3), 90–95.https://doi.org/10.1109/MCSE.2007.55.
- [22]Irawan, D.E.; Herho, S.H.S.; Pamumpuni, A.; Kartiko, R.D.;
Khadami, F.; Anwar, I.P.; Sujatmiko, K.A.; Handayani, A.P.;
Fajary, F.R.; Suwarman, R. An Open-Source Pseudo-Spectral Solver for
Idealized Korteweg–de Vries Soliton Simulations.Water2026,18(7), 779.https://doi.org/10.3390/w18070779.
- [23]Knight, P.A. The Sinkhorn–Knopp Algorithm: Convergence and
Applications.SIAM J. Matrix Anal. Appl.2008,30(1),
261–275.https://doi.org/10.1137/060659624.
- [24]Kozachenko, L.F.; Leonenko, N.N. Sample Estimate of the Entropy of a
Random Vector.Probl. Inf. Transm.1987,23(2), 95–101.
English translation of Problemy Peredachi Informatsii, 23(2), 9–16.
- [25]Kraskov, A.; Stögbauer, H.; Grassberger, P. Estimating mutual
information.Phys. Rev. E2004,69(6), 066138.https://doi.org/10.1103/PhysRevE.69.066138.
- [26]Kullback, S.; Leibler, R.A. On Information and Sufficiency.Ann. Math. Stat.1951,22(1), 79–86.https://doi.org/10.1214/aoms/1177729694.
- [27]Lam, S.K.; Pitrou, A.; Seibert, S. Numba: A LLVM-based Python JIT
compiler. InProceedings of the Second Workshop on the LLVM
Compiler Infrastructure in HPC (LLVM-HPC 2015); ACM: New York, NY,
USA, 2015; pp. 1–6.https://doi.org/10.1145/2833157.2833162.
- [28]Léonard, C. A survey of the Schrödinger problem and some of
its connections with optimal transport.Discrete Contin. Dyn. Syst.2014,34(4),
1533–1574.https://doi.org/10.3934/dcds.2014.34.1533.
- [29]Mardia, K.V.; Jupp, P.E.Directional Statistics; Wiley
Series in Probability and Statistics; John Wiley & Sons:
Chichester, UK, 2000.https://doi.org/10.1002/9780470316979.
- [30]Mikami, T. Monge’s problem with a quadratic cost by the zero-noise
limit ofhh-path processes.Probab. Theory Relat. Fields2004,129,
245–260.https://doi.org/10.1007/s00440-004-0340-4.
- [31]Peyré, G.; Cuturi, M. Computational Optimal Transport: With
Applications to Data Science.Found. Trends Mach. Learn.2019,11(5–6),
355–607.https://doi.org/10.1561/2200000073.
- [32]Politis, D.N.; Romano, J.P. Large Sample Confidence Regions Based on Subsamples under Minimal Assumptions.Ann. Stat.1994,22(4), 2031–2050.https://doi.org/10.1214/aos/1176325770.
- [33]Rew, R.K.; Davis, G.P. NetCDF: an interface for scientific data
access.IEEE Comput. Graph. Appl.1990,10(4),
76–82.https://doi.org/10.1109/38.56302.
- [34]Schmitzer, B. Stabilized Sparse Scaling Algorithms for Entropy
Regularized Transport Problems.SIAM J. Sci. Comput.2019,41(3),
A1443–A1481.https://doi.org/10.1137/16M1106018.
- [35]Schrödinger, E. Über die Umkehrung der Naturgesetze.Sitzungsber. Preuß. Akad. Wiss., Phys.-Math. Kl.1931, 144–153.
- [36]Schrödinger, E. Sur la théorie relativiste de l’électron
et l’interprétation de la mécanique quantique.Ann. Inst. Henri Poincaré1932,2(4),
269–310.
- [37]Scott, D.W. On optimal and data-based histograms.Biometrika1979,66(3), 605–610.https://doi.org/10.1093/biomet/66.3.605.
- [38]Silverman, B.W.Density Estimation for Statistics and Data
Analysis; Routledge: New York, NY, 1998.https://doi.org/10.1201/9781315140919.
- [39]Sinkhorn, R. A Relationship Between Arbitrary Positive Matrices and
Doubly Stochastic Matrices.Ann. Math. Stat.1964,35(2), 876–879.https://doi.org/10.1214/aoms/1177703591.
- [40]Sinkhorn, R.; Knopp, P. Concerning nonnegative matrices and doubly
stochastic matrices.Pac. J. Math.1967,21(2), 343–348.https://doi.org/10.2140/pjm.1967.21.343.
- [41]Villani, C.Optimal Transport: Old and New; Grundlehren der
mathematischen Wissenschaften, Vol. 338; Springer: Berlin,
Heidelberg, Germany, 2009.https://doi.org/10.1007/978-3-540-71050-9.
- [42]Virtanen, P.; Gommers, R.; Oliphant, T.E.; Haberland, M.; Reddy, T.;
Cournapeau, D.; Burovski, E.; Peterson, P.; Weckesser, W.; Bright, J.;
van der Walt, S.J.; Brett, M.; Wilson, J.; Millman, K.J.; Mayorov, N.;
Nelson, A.R.J.; Jones, E.; Kern, R.; Larson, E.; Carey, C.J.;
Polat, İ.; Feng, Y.; Moore, E.W.; VanderPlas, J.; Laxalde, D.;
Perktold, J.; Cimrman, R.; Henriksen, I.; Quintero, E.A.;
Harris, C.R.; Archibald, A.M.; Ribeiro, A.H.; Pedregosa, F.;
van Mulbregt, P. SciPy 1.0: fundamental algorithms for scientific
computing in Python.Nat. Methods2020,17, 261–272.https://doi.org/10.1038/s41592-019-0686-2.

## 


- 


Major funding support from
