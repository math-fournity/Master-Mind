# On Computational CUDA Studies of Black Hole Shadows

**arXiv ID**: 2604.14213v1
**Authors**: S. E. Baddis, A. Belhaj, H. Belmahi, S. E. Ennadifi, M. Jemri
**Published**: 2026-04-07
**Categories**: physics.gen-ph, gr-qc, hep-th
**Comments**: 18 pages, 9 figures, 1 table, Latex, Authors are listed in alphabetical order
**HTML URL**: https://arxiv.org/html/2604.14213v1

## Abstract

Combining high-performance CUDA numerical codes with the Hamilton--Jacobi formalism, we investigate the shadows properties of rotating charged Euler--Heisenberg black holes in the presence of global monopoles. Then, we discuss the associated energy emission rate by varying the involved black hole parameters. As a result, we show that both the shadow structure and the energy emission rate depend on the global monopole parameter, the electric charge, and the rotation parameter. However, we observe that the Euler--Heisenberg nonlinear parameter does not significantly affect either the shadow or the energy emission rate. In order to reconcile the present theoretical predictions with the shadow observations reported by the Event Horizon Telescope collaboration, we employ a CUDA-based computational approach to establish strict bounds on the GM parameter, the electric charge, and the rotation parameter.

## Full Text

On Computational CUDA Studies of Black Hole Shadows

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2604.14213v1 [physics.gen-ph] 07 Apr 2026

## On Computational CUDA Studies of Black Hole ShadowsS. E. Baddis1,
A. Belhaj1,
H. Belmahi2,
S. E. Ennadifi3,
M. Jemri1
1ESMaR, Faculty of Science, Mohammed V University in Rabat, Rabat, Morocco
2National School of Applied Sciences (ENSA), Chouaib Doukkali University, El Jadida, Morocco
3LHEP-MS, Faculty of Science, Mohammed V University in Rabat, Rabat, MoroccoAuthors are listed in alphabetical order.Corresponding author: maryem.jemri@um5r.ac.ma.

## Abstract

Combining high-performance CUDA numerical codes with the Hamilton–Jacobi formalism, we investigate the shadows properties of rotating charged Euler–Heisenberg black holes in the presence of global monopoles. Then, we discuss the associated energy emission rate by varying the involved black hole parameters. As a result, we show that both the shadow structure and the energy emission rate depend on the global monopole parameter, the electric charge, and the rotation parameter. However, we observe that the Euler–Heisenberg nonlinear parameter does not significantly affect either the shadow or the energy emission rate. In order to reconcile the present theoretical predictions with
the shadow observations reported by the Event Horizon Telescope collaboration, we employ a CUDA-based computational approach
to establish strict bounds on the GM parameter, the electric charge,
and the rotation parameter.
Keywords: Euler–Heisenberg black holes with GMs, Shadows, Energy emission rate, EHT collaboration, CUDA high-performance numerical codes.

## 1Introduction

In black hole physics, a considerable interest has been devoted to the study of
thermodynamic properties. These include the entropy, the temperature, the phase
transitions, and the critical phenomena[1,2]. These studies reveal deep
connections between gravity, quantum mechanics, and statistical physics.
Consequently, black holes remain an important subject in the search for a
unified description of fundamental interactions.

Beyond thermodynamic aspects, the optical properties of black holes have
also attracted significant attention[3,4,5]. Precisely, the
propagation of light in strong gravitational fields has been widely studied
using analytical and numerical techniques. These analyses have led to observable
predictions, such as gravitational lensing and the formation of black hole
shadows. A major breakthrough has been achieved with the observations of the
Event Horizon Telescope (EHT)[6,7,8,9,10]. This collaboration has
produced the first image of the shadow of a supermassive black hole. These
observations strengthen the connection between theoretical models and
astrophysical empirical investigations.

In this regard, charged black holes have attracted remarkable interest in
recent years. In particular, those described by the Reissner–Nordström (RN) solution and its extensions have been widely investigated[11].
Studies of their shadows show that the presence of the electric charge can
introduce asymmetries compared to the shadow of a Schwarzschild black hole
with the same mass[12]. These effects may allow to estimates the
charge-to-mass ratio, although astrophysical black holes are generally
expected to have a negligible total charge. Shadow properties can also be
modified in other theoretical models. This includes scenarios of frameworks
based on the Euler-Heisenberg theory involving global monopoles (GM). The
latters are considered as relics of early-universe phase transitions, and their
presence in black hole solutions allows to study the corresponding interactions[13,14]. They result from a spontaneous global symmetry breaking
during phase transitions in the early universe. The Goldstone fields
associated with GMs exhibit a slowly decaying energy density behavior,
leading to a linear infrared divergence of the total energy. Such a large
energy distribution can produce significant gravitational effects, modifying
the spacetime geometry. Two classes of such monopoles have been broadly
explored being the ordinary global monopoles (OGM), possessing positive
kinetic energy terms, and the phantom global monopoles (PGM), which are
characterized by negative kinetic energy terms. In such cases, both the size
and the shape of the shadow can change. These studies are important because
they connect observable shadow features to the internal parameters of black
holes and provide a way to test gravitational theories beyond general
relativity.

Recently, black holes have also been studied in models involving modified
derivatives[16,15]. In particular, the Schwarzschild black holes have
been modified by introducing Dunkl derivatives. Within this framework, the
shadows of non-rotating black holes have been investigated, showing that
these modifications can affect their optical behaviors[17]. More
recently, strict constraints on the Dunkl deformation parameters have been
derived from the study of the shadows of rotating black holes in the Dunkl
spacetime, using CUDA-based numerical calculations[18]. This approach
attempts to establish a correlation with the shadow observations reported by
the EHT collaboration. It has been remarked that CUDA has proved to be a powerful platform for
general-purpose parallel computing. It leverages the massive parallelism of
NVIDIA GPUs[19,20]. By distributing computational tasks among
several multiprocessors in a continuous stream, GPUs enable efficient and
scalable computations. They also provide advanced tools which improve the
performance of the kernel and the overall efficiency of the computations. In
black hole physics, CUDA-accelerated simulations have become particularly
useful. They considerably reduce computation time, improve numerical
stability, and enable more accurate theoretical predictions[21,22].
These techniques are now widely used in studies of black hole shadows. They
also allow for detailed comparisons between theoretical models and
observational data acquired by the EHT.

The aim of this work is to provide a computational CUDA study of black H-hole shadows the shadow of rotating charged
Euler-Heisenberg black holes with GM using high-performance
parallel computations. Combining such numerical methods with the Hamilton-Jacobi formalism, we analyze the shadow of the rotating
configuration and investigate the associated energy emission rate. In order to conciliate current theoretical predictions with
the shadow observations reported by the EHT international collaboration, we explore a CUDA-based computational approach
to establish strict constraints on the GM parameterbb, the electric chargeQQ,
and the rotation parameteraa.

The organization of the paper is as follows. In Section 2, we present the
rotating charged Euler-Heisenberg black holes with the presence of GM.
Section 3 is devoted to the study of the shadow of these rotating charged
black holes using CUDA techniques. In Section 4, we numerically estimate the
energy emission rate to analyze the corresponding Hawking radiation. Section
5 connects the theoretical predictions with observational data from the EHT
collaboration through CUDA-based computations. Finally, the last section
provides some concluding remarks.

## 2CUDA computations of shadows of rotating charged Euler–Heisenberg black holes with GMs

In this section, we elaborate a CUDA study of rotating charged Euler-Heisenberg black holes
with GMs by employing the
Newman-Janis algorithm without complexification[25]. This allows the
metric to be expressed as in[26,27]. Based on such an algorithm, we
could investigate certain physical properties of the rotating version of the
charged Euler-Heisenberg black holes with GMs using CUDA computations. These GMs, being an example
of topological defects arising from the spontaneous breaking of a global
symmetryO​(3)O(3)\toU​(1)U(1), have a non-ordinary matter effect contribution
leading to a modification of the global structure of spacetime around black
holes. The key physical effect of such a GM contribution is a deficit in the
solid angle of spacetimeΔ​ΩG​M\Delta\Omega_{GM}. To unveil the corresponding
effect, one needs to introduce the scalar field responsible for the GM. In the
unit system whereG=ℏ=c=1G=\hbar=c=1, the corresponding dynamics could be
described by the total action written asS≃∫d4​x​−g​[ℛ16​π−14​Fμ​ν​Fμ​ν+b​(Fμ​ν​Fμ​ν)2+ℒG​M]S\simeq\int d^{4}x\,\sqrt{-g}\left[\frac{\mathcal{R}}{16\pi}-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}+b\left(F_{\mu\nu}F^{\mu\nu}\right)^{2}+\mathcal{L}_{GM}\right](2.1)

whereRRis the Ricci scalar andggrepresents the metric determinant. The quantity−14​(Fμ​ν)2+b​(Fμ​ν​Fμ​ν)2-\frac{1}{4}\left(F_{\mu\nu}\right)^{2}+b\left(F_{\mu\nu}F^{\mu\nu}\right)^{2}denotes the Euler–Heisenberg electrodynamics lagrangian, andℒG​M\mathcal{L}_{GM}is the GM lagrangian. The latter can be
described by the scalar lagrangian formℒG​M=12​(∂μϕa)2−λ4​((ϕa)2−η2)2+μ​ℛ​(ϕa)2\mathcal{L}_{GM}=\frac{1}{2}\left(\partial_{\mu}\phi^{a}\right)^{2}-\frac{\lambda}{4}\left(\left(\phi^{a}\right)^{2}-\eta^{2}\right)^{2}+\mu\mathcal{R}\left(\phi^{a}\right)^{2}(2.2)

whereϕa\phi^{a}(a=1,2,3a=1,2,3) is the scalar triplet field giving rise to the GM andη\etadenotes the corresponding symmetry breaking scale.λ\lambdadenotes the
self-coupling constant, andμ\muis a non-minimal coupling constant
between the scalar field and the gravity model. Owing to the fact that the curvature
termμ​ℛ​(ϕa)2\mu\mathcal{R}\left(\phi^{a}\right)^{2}slightly shifts the
scalar field vacuum expectation value, we take, for simplicity, the
potential minimum occurring at(ϕa)v​e​v2≡ξ​η2\left(\phi^{a}\right)_{vev}^{2}\equiv\xi\eta^{2}whereξ\xiis a dimensionless parameter that encodes now the
curvature effect. This vacuum geometry represents a two dimensional real sphere𝐒2\mathbf{S}^{2}manifold and the associated symmetry breaking allows topological point
defects, e.g., GMs. Physically, a typical field configuration describing a
GM could be expressed asϕa=η​h​(r)​xar,h​(r)∣r→0=0,​h​(r)∣r→+∞=1\phi^{a}=\eta h\left(r\right)\frac{x^{a}}{r},\quad h(r)\mid_{r\to 0}=0,\text{ }h(r)\mid_{r\to+\infty}=1(2.3)

where one has usedr=xa​xar=\sqrt{x^{a}x_{a}}andh​(r)h\left(r\right)is a profile
function. Far from the GM core (r≫r\ggcore size), the above field
configuration becomesϕa≃η​xar,∣ϕ∣=η\phi^{a}\simeq\eta\frac{x^{a}}{r},\quad\mid\phi\mid=\eta(2.4)

where the magnitude of the field is constant. However, its direction changes
with the position. To reveal the GM influence on black holes, one needs to
elucidate the behavior of the total energy of the GM. Such an energy, coming
mainly from the kinetic term of Eq. (2.3), diverges linearly with distance. Using the spherical coordinates, indeed, we haveEG​M=∫12​(∂μϕa)2​d3​x≃∫0R(ηr)2​(4​π​r2)​𝑑r∼4​π​η2​RE_{GM}=\int\frac{1}{2}\left(\partial_{\mu}\phi^{a}\right)^{2}d^{3}x\simeq\int_{0}^{R}\left(\frac{\eta}{r}\right)^{2}\left(4\pi r^{2}\right)dr\sim 4\pi\eta^{2}R(2.5)

whereRRrefers to distance cutoff. It is an energy distribution extension
of the GM generating an unusual gravitational field affecting the
surrounding spacetime. Considering this GM energy behavior and
solving the corresponding Einstein equations can result in a constant shift in
the metric function, giving the deficit solid angle termΔ​ΩG​M=8​π​η2​ξ.\Delta\Omega_{GM}=8\pi\eta^{2}\xi.(2.6)

This spacetime geometry modification generated by GMs affects the
metric functions of the involved black holes. Concretely, adopting the Boyer-Lindquist coordinate system, we can obtain the metric functions of the
involved black holes. Indeed, we can get the following line element for the black hole metricd​s2=(σ​(r)Σ​(r)−1)​d​t2−2​a2​σ​(r)Σ​(r)​sin2⁡θ​d​t​d​ϕ+(r2+a2+a2​σ​(r)​sin2⁡θΣ​(r))​sin2⁡θ​d​ϕ2+Σ​(r)Δ​(r)​d​r2+Σ​(r)​d​θ2,ds^{2}=\left(\frac{\sigma(r)}{\Sigma(r)}-1\right)dt^{2}-\frac{2a^{2}\sigma(r)}{\Sigma(r)}\sin^{2}\theta\,dt\,d\phi+\left(r^{2}+a^{2}+\frac{a^{2}\sigma(r)\sin^{2}\theta}{\Sigma(r)}\right)\sin^{2}\theta\,d\phi^{2}+\frac{\Sigma(r)}{\Delta(r)}dr^{2}+\Sigma(r)d\theta^{2},(2.7)

whereaais the rotating spin parameter. The corresponding metric
functions are given byΣ​(r)=r2+a2​cos2⁡θ,Δ​(r)=r2​f​(r)+a2,σ​(r)=r2−r2​f​(r)\Sigma(r)=r^{2}+a^{2}\cos^{2}\theta,\quad\Delta(r)=r^{2}f(r)+a^{2},\quad\sigma(r)=r^{2}-r^{2}f(r)

where the GM effect, e.g., the above deficit solid angle term, appears in the
metric functionf​(r)f(r)asf​(r)=1−2​Mr+Q2r2−b​Q420​r6−8​π​η2​ξ.f(r)=1-\frac{2M}{r}+\frac{Q^{2}}{r^{2}}-\frac{bQ^{4}}{20r^{6}}-8\pi\eta^{2}\xi.(2.8)

The quantitiesMMandQQdenote the total mass and the electric charge
of the black hole, respectively. The parameterbbis the
Euler-Heisenberg parameter[28]. Though it is positive in the original
Euler-Heisenberg formulation, it is significant in gravitational theories to
also consider negative values in the form of a nonlinear and independent
parameter. At this point, we would like to make a few comments. It has been
remarked that the GM term8​π​η2​ξ8\pi\eta^{2}\xiappears in optical and
thermodynamic quantities of various black hole solutions[29]. Removing
the external parameters required byb=η=ξ=0b=\eta=\xi=0, we recover to the
standard charged black hole solution[30].

Having discussed the metric function, we analyze its possible horizons using a CUDA-based numerical implementation that enables efficient parallel computation on GPUs. These horizons are determined by vanishing the radial component of the metric. To determine the existence of horizons, we implement a numerical algorithm in which the parametersξ\xi,QQandη\etaare kept fixed, whilebbvaries from0to11with a step size of0.10.1. Moreover,aaranges with the same increment. For each pair(a,b)(a,b), the horizon equation is solved numerically in order to show the presence of at least one real solution, corresponding to a physical horizon. This procedure allows one to consistently identify regions of the parameter space where the metric admits such solutions. To illustrate this scenario, Fig. (1) displays the regions in the(a,b)(a,b)parameter space where at least one real horizon exists (atξ=0.5\xi=0.5) for several values ofη\etaby considering two charge configurations:Q=0.4Q=0.4(top panel) andQ=0.9Q=0.9(bottom panel).
Figure 1:Regions in the(b,a)(b,a)–plane, where the metric admits at least
one real event horizon radius.

The figure shows that an increase in the charge value reduces the allowed
region where the black hole horizons exist. Interestingly, for the caseη=0.1\eta=0.1andξ=0.5\xi=0.5, the charge variation has no effect, and the entire
region remains allowed. On the other hand, increasingη\etasubstantially shrinks the allowed
region, which becomes very narrow in the caseη=1\eta=1. Indeed, the following optical study will be carried out by considering the
region of the moduli parameter space aligned with the allowed domain
admitting at least one real solution.

In this section, we examine the shadow of a rotating charged Euler
-Heisenberg black hole with a GM. Precisely, we analyze the effect of each
parameter on the black hole shadow. To perform this evaluation effectively,
we employ a CUDA-based numerical code which enables high-performance
parallel computations. It is recalled that CUDA is a general-purpose
parallel computing platform and programming model that leverages the
parallel computing capabilities of NVIDIA GPUs. In particular, the GPU
architecture allows workloads to be distributed among a large number of
streaming multiprocessors (SMs) in a highly parallel manner. In addition,
modern GPUs provide a variety of powerful methods and efficient tools to
further exploit this architecture. With each new generation, improvements in
CUDA core design strategies lead to increased performance and computational
efficiency. Moreover, CUDA has proven to be a powerful tool in black hole
investigations enabling efficient GPU-accelerated simulations[21,22].
This significantly reduces computation time, improves numerical stability,
and facilitates the exploration of the theoretical predictions in black hole
physics[23,24]. To start, it is denoted that the shadow of a black
hole is defined as the apparent boundary, or the critical curve, observed when
light rays asymptotically approach an unstable circular orbit known as the
photon sphere and then return toward the observer. This behavior is encoded
in the null geodesics around black holes. To study the optical properties of
the rotating black holes, it is necessary to establish specific relations using
the Hamilton-Jacobi formalism. In particular,
the separation of variables can be performed through the Carter method[31]. For such black hole solutions, the four equations of motion can be
written as followsΣ​t˙\displaystyle\Sigma\dot{t}=r2+a2Δ​[E​(r2+a2)−a​L]+a​[L−a​E​sin2⁡θ]\displaystyle=\frac{r^{2}+a^{2}}{\Delta}\left[E\left(r^{2}+a^{2}\right)-aL\right]+a\left[L-aE\sin^{2}\theta\right](2.9)(Σ​r˙)2\displaystyle(\Sigma\dot{r})^{2}=ℛ​(r)\displaystyle=\mathcal{R}(r)(2.10)(Σ​θ˙)2\displaystyle(\Sigma\dot{\theta})^{2}=Θ​(θ)\displaystyle=\Theta(\theta)(2.11)Σ​ϕ˙\displaystyle\Sigma\dot{\phi}=[L​csc2⁡θ−a​E]+aΔ​[E​(r2+a2)−a​L],\displaystyle=\left[L\csc^{2}\theta-aE\right]+\frac{a}{\Delta}\left[E\left(r^{2}+a^{2}\right)-aL\right],(2.12)

whereEEandLLare the energy and the angular momentum of the light rays,
respectively.ℛ​(r)\mathcal{R}(r)andΘ​(θ)\Theta(\theta)functions are
expressed as followsℛ​(r)\displaystyle\mathcal{R}(r)=[E​(r2+a2)−a​L]2−Δ​[𝒞+(L−a​E)2],\displaystyle=\left[E\left(r^{2}+a^{2}\right)-aL\right]^{2}-\Delta\left[\mathcal{C}+\left(L-aE\right)^{2}\right],(2.13)Θ​(θ)\displaystyle\Theta(\theta)=𝒞−(L​csc⁡θ−a​E​sin⁡θ)2+(L−a​E)2,\displaystyle=\mathcal{C}-\left(L\csc\theta-aE\sin\theta\right)^{2}+\left(L-aE\right)^{2},(2.14)

where𝒞\mathcal{C}is the Carter separation parameter. Solving the unstable
circular orbit equations, the two needed impact parameters are obtained as
followsξ\displaystyle\xi=r2​[16​a2​Δ​(r)+8​r​Δ​(r)​Δ′⁣2−r2​Δ′⁣2]a2​Δ′⁣2|r=r0,\displaystyle=\frac{r^{2}\!\left[\,16a^{2}\Delta(r)+8r\,\Delta(r)\Delta^{\prime 2}-r^{2}\Delta^{\prime 2}\right]}{a^{2}\,\Delta^{\prime 2}}\bigg|_{r=r_{0}},(2.15)Ξ\displaystyle\Xi=(r2+a2)​Δ′​(r)−4​r​Δ​(r)a​Δ′​(r)|r=r0.\displaystyle=\frac{(r^{2}+a^{2})\,\Delta^{\prime}(r)-4r\,\Delta(r)}{a\,\Delta^{\prime}(r)}\bigg|_{r=r_{0}}.(2.16)

For the rotating charged Euler–Heisenberg black holes with GMs, the
apparent shape of the black hole shadow, as observed at spatial infinity,
can be characterized by the celestial coordinates(X,Y)(X,Y)beingX\displaystyle X=limrob→+∞(−rob2​sin⁡θob​d​ϕd​r)\displaystyle=\lim_{r_{\text{ob}}\rightarrow+\infty}\left(-r_{\text{ob}}^{2}\sin\theta_{\text{ob}}\frac{d\phi}{dr}\right)Y\displaystyle Y=limrob→+∞(rob2​d​θd​r),\displaystyle=\lim_{r_{\text{ob}}\rightarrow+\infty}\left(r_{\text{ob}}^{2}\frac{d\theta}{dr}\right),

wherero​br_{ob}is the distance of the observer from the black hole. It is
denoted thatθob\theta_{\text{ob}}indicates the angle of inclination
between the line of the observer and the axis of rotation of the black hole.

To explore how each parameter affects the black hole shadow, we exploit a
numerical method to illustrate the shadow curves choosing a wide range of
values. Precisely, a CUDA-based parallel computing program is employed to
speed up the calculations[19,20]. This approach allows rapid determination of the
shadow boundaries for different parameter variations. For each illustration,
all parameters are kept fixed except the one of interest. This parameter is
incremented in steps of0.0010.001. Indeed, we solve Eqs. (2.15) and Eqs. (2.16). Then, we implement the resulting values in the shadow equation. This
process provides a precise assessment of the influence of each parameter on
the shadow geometric deformation including the size and the shape.

In Fig. (2), we illustrate the shadow appearance by examining the
effects of the chargeQQ, the rotation parameteraa, where the parameterbbis fixed at0.10.1.Figure 2:Effect of internal parameter on
shadow behavior.

As shown in the figure, the rotation parameter behaves similarly to that in
ordinary black holes, slightly reducing the size of the shadow and deforming
its shape into a D-like form. Hence, this parameter retains its role as a
deformation parameter for these black hole solutions. Concerning the charge
effect, increasing the charge reduces the shadow size without significantly
modifying its shape, in agreement with the behavior of standard charged
black holes. In the present solutions, however, the variation range of the
shadow size extends to values of about1515, unlike ordinary charged black
hole solutions where the radius does not exceed77. This feature arises
from the additional terms in the metric, in which the parameterbbis
coupled to the chargeQQ.

For the GM parameters, which are coupled, fixing one while
varying the other reveals their combined effect. Indeed, by takingξ=1\xi=1and varyingη\eta, we observe that this contribution increases the size of
the shadow.Figure 3:Effect ofη\etaon shadow
behavior.

As shown in Fig.3, interesting behaviors appear, for large values
of the rotation parametera=0.9a=0.9and small values ofη\eta, the shadow
exhibits a D-like form. Asη\etaincreases, this D-like form gradually
disappears, illustrating the interplay between the GM and the
black hole rotation. Concretely, this circularization, (or symmetry
effect) appearing asη\etagrows, is due to the fact
that the GM term8​π​η2​ξ8\pi\eta^{2}\xiaffects the geometry
globally and isotropically, by diluting the relative influence of the spin.Figure 4:Effect ofbbparameter on shadow
behavior.

We move now to consider the effect of thebbparameter. Fig. (4) depicts
the black hole shadow for positive and negative values ofbb. The results
indicate that variations in the magnitude ofbbdo not significantly alter
the shadow size. Interestingly, the
positive values ofbblead to a D-shaped shadow, whereas negative values
produce a cardioid-like configuration.

## 3Energy emission rate using CUDA computations

In this section, we employ a CUDA-based numerical method to approach the
energy emission rate associated with the rotating and the charged Euler-Heisenberg black holes with GM. By leveraging the parallelism of GPUs,
this method provides efficient and high-performance computation of effective
absorption cross sections over a wide range of parameters. To a distant
observer, the cross section for absorption at very high energies
asymptotically trends toward its geometric optical bound, being directly
linked to the size of the shadow of the black hole. In intermediate
operating conditions, the effective absorption cross-section oscillates
around a constant limit value, referred to asσlim\sigma_{\text{lim}}. It has
been established that this constant coincides with the geometric
cross-section of the photon sphere, determined by the properties of the null
geodesics[32,33,34]. Since the shadow determines the optical
appearance of the black hole, it can be treated as this limit value, which
can be used to approximateσlim\sigma_{\text{lim}}as followsσlim≃π​Rs2,\sigma_{\text{lim}}\simeq\pi R_{s}^{2},(3.1)

whereRsR_{s}is the shadow radius. Within this framework, the differential
energy emission rate takes the formd2​E​(ω)d​ω​d​t=2​π3​Rs2eω/TH−1​ω3,\frac{d^{2}E(\omega)}{d\omega\,dt}=\frac{2\pi^{3}R_{s}^{2}}{e^{\omega/T_{H}}-1}\,\omega^{3},(3.2)

whereTHT_{H}is the Hawking temperature of the black hole andω\omegais
the emission frequency. This relation establishes a clear connection between
the thermodynamic properties of the black hole and its optical features.
Indeed, this may provide a useful tool to probe the spacetime parameters
through the observational signatures. Considering the rotating metric, the
Hawking temperature of such black holes is given byTH=10​(1−8​π​η2​ξ)​r6−10​M​r5+b​Q420​π​r5​(a2+r2).T_{H}=\frac{10\left(1-8\pi\,\eta^{2}\xi\right)r^{6}-10M\,r^{5}+b\,Q^{4}}{20\pi r^{5}\left(a^{2}+r^{2}\right)}.(3.3)

To evaluate the energy emission rate for different black hole parameter
values, we perform numerical simulations using a CUDA-based program. The
corresponding code computes first the maximal shadow radius from the
obtained shadow data. Then, the horizon radius is determined by solvingΔ​(rh)=0\Delta(r_{h})=0and substituted into the Hawking temperature formula. To
assess the impact of each parameter, we vary the parameter of interest in
steps of 0.001 while keeping all others fixed. These results are then used
to generate the energy emission rate plots.

In Fig.(5), we illustrate the variation of the energy emission rate
as a function of the emission frequency. This figure represents the effects of
the electric charge and the rotation parameter on this variation. It is
clear from the figure that increasing the charge leads to a decrease in the
energy emission rate. In contrast, the presence of the rotation parameter
enhances the energy emission rate. Indeed, the charge acts as a suppressing
factor, while the GM behaves as an amplifying contribution,
which is the usual effect of these two parameters.Figure 5:Variation of the energy emission
rate as a function of the emission frequency for different values ofaaandQQ.

Fig. (6) shows the effect of the GM parameter for both small and
large values of the rotation parameter. For small rotation values, the GM parameter decreases the energy emission rate. For large values, however, the GM initially increases the energy emission rate up to a critical value, beyond which it begins to act as a
suppressing factor.Figure 6:Variation of the energy emission
rate as a function of the emission frequency for different values ofη\eta.

We now turn to the effect of the parameterbbwhere the association variation is shown in Fig. (7).
As discussed in the previous section, this parameter has no significant
impact on the shadow radius. Although the energy emission rate also depends
on the temperature, which varies with the parameterbb, the figure
indicates that, overall,bbhas a negligible effect on the energy emission
rate. This behavior holds for both negative and positive values ofbb.Figure 7:Variation of the energy emission
rate as a function of the emission frequency for different values ofbb.

## 4Constraints on black hole parameters from EHT observations using CUDA techniques

In order to establish a bridge between the theoretical predictions and the
observational data, this section provides an analysis of the shadow cast by
rotating Euler-Heisenberg black holes with GMs, in connection
with observational results reported by the EHT collaborations. Concretely,
we exploit the observational data of M87* black hole and Sagittarius A* (Sgr A*) to
constrain the parameters of such black holes[35,36,37]. The numerical
analysis is performed using a CUDA-based code developed by NVIDIA, which
leverages parallel computing on GPUs to significantly speed up the numerical
calculations required to determine the shadow of the black holes.

Roughly, the constraints can be obtained by using the fractional deviation
from the Schwarzschild black hole shadow diameter expressed byd=Rsrs​h−1,{\ d}=\frac{R_{s}}{r_{sh}}-1,(4.1)

whereRsR_{s}denotes the shadow radius,MMis the mass of the black hole, andrs​hr_{sh}denotes the Schwarzschild radius. The dimensionless quantityRs/MR_{s}/Mprovides a key observable for comparing theoretical models with empirical
measurement results. The 1-σ\sigmaand 2-σ\sigmaconfidence intervals
derived from the EHT observations are summarized in Table1.Black HoleDeviation (dd)1-σ\sigmaBounds2-σ\sigmaBoundsM87∗(EHT)−0.01−0.17+0.17-0.01^{+0.17}_{-0.17}4.26≤RsM≤6.034.26\leq\frac{R_{s}}{M}\leq 6.033.38≤RsM≤6.913.38\leq\frac{R_{s}}{M}\leq 6.91Sgr A∗(EHTVLTI{}_{\text{VLTI}})−0.08−0.09+0.09-0.08^{+0.09}_{-0.09}4.31≤RsM≤5.254.31\leq\frac{R_{s}}{M}\leq 5.253.85≤RsM≤5.723.85\leq\frac{R_{s}}{M}\leq 5.72Sgr A∗(EHTKeck{}_{\text{Keck}})−0.04−0.10+0.09-0.04^{+0.09}_{-0.10}4.47≤RsM≤5.464.47\leq\frac{R_{s}}{M}\leq 5.463.95≤RsM≤5.923.95\leq\frac{R_{s}}{M}\leq 5.92Table 1:Estimated fractional deviations and
corresponding bounds for M87∗and Sgr A∗black holes.

In what follows, we provide a numerical algorithm using CUDA-based
computations to determine the parameter pairs(η,Q)(\eta,Q)and(η,a)(\eta,a)producing the black hole shadow configurations consistent with the observational
data. Indeed, we fixξ=0.4\xi=0.4,b=0.5b=0.5, andM=1M=1throughout the
analysis. First, for each parameter combination, the maximal shadow radiusRmaxR_{\mathrm{max}}has been computed using the CUDA code, allowing a efficient
evaluation over a dense grid of values. For the(η,Q)(\eta,Q)analysis,aais
set to 0.5 whileη\etais varied from 0 to 0.25 andQQfrom 0 to 1. For
the(η,a)(\eta,a)analysis,QQis fixed whileη\etavaries from 0 to 0.25
andaafrom 0 to 1 with a step size of 0.001. For each combination of
parameters, the computed shadow radius is compared to the observational
bounds reported by the EHT collaboration. This permits to identify
the allowed regions in the parameter space satisfying the1−σ1\!-\!\sigmaand2−σ2\!-\!\sigmaconfidence intervals.Figure 8:Constraint Constraint regions in the(η,Q)(\eta,Q)plane obtained from CUDA-based simulations, showing
agreement with the EHT observations of M87∗87^{*}and Sgr A∗within1−σ1-\sigmaand2−σ2-\sigmaconfidence levels forQ=0.4Q=0.4withM=1M=1.

As illustrated in Fig. (8), the regions of the
reduced parameter space(η,a)(\eta,a)consistent with empirical observations expand for
larger values. This suggests that the black hole spacetime can effectively
reproduce the observed shadow signatures. Due to the correlation between
these parameters, one of them is set while restricting the remaining one.
Settinga=0.8a=0.8, the black hole metric allows a wide range of parameter
values that yield real and physically meaningful horizons. However, a
comparison with the EHT data shows that only certain values ofη\etacorrespond to the observed shadow sizes, as follows
- •

M87∗case:0.001≤η≤0.07,within​1−σ,0.001\leq\eta\leq 0.07,\quad\text{within }1-\sigma,0.001≤η≤0.09,within​2−σ.0.001\leq\eta\leq 0.09,\quad\text{within }2-\sigma.
- •

Sgr A∗case (EHTVLTI{}_{\text{VLTI}}) :0.001≤η≤0.05,within​1−σ,0.001\leq\eta\leq 0.05,\quad\text{within }1-\sigma,0.001≤η≤0.075,within​2−σ.0.001\leq\eta\leq 0.075,\quad\text{within }2-\sigma.
- •

Sgr A∗case (EHTKeck{}_{\text{Keck}}):0.001≤η≤0.06,within​1−σ,0.001\leq\eta\leq 0.06,\quad\text{within }1-\sigma,0.001≤η≤0.07,within​2−σ.0.001\leq\eta\leq 0.07,\quad\text{within }2-\sigma.

The results indicate that, when all other parameters are kept fixed,η\etais positive and remains below 0.1 to ensure consistency with the
observations.Figure 9:Constraint Constraint regions in the(η,Q)(\eta,Q)plane obtained from CUDA-based simulations, showing
agreement with the EHT observations of M87∗87^{*}and Sgr A∗within1−σ1-\sigmaand2−σ2-\sigmaconfidence levels fora=0.5a=0.5withM=1M=1.

Similarly, Fig. (9) shows the allowed regions in the(η,Q)(\eta,Q)plane. Larger values ofη\etaandQQcorrespond to a higher
density of points consistent with the observations, suggesting that larger
values ofQQimprove the agreement between theoretical shadow predictions
and the EHT data. TakingQ=0.4Q=0.4, the black hole metric still allows a wide
range of valid horizons. However, only specific valuesη\etacan reproduce
the observed shadows. The corresponding constraints are found to be
- •

M87∗case:0.001≤η≤0.065,within​1−σ,0.001\leq\eta\leq 0.065,\quad\text{within }1-\sigma,0.001≤η≤0.085,within​2−σ.0.001\leq\eta\leq 0.085,\quad\text{within }2-\sigma.
- •

Sgr A∗case (EHTVLTI{}_{\text{VLTI}}):0.001≤η≤0.035,within​1−σ,0.001\leq\eta\leq 0.035,\quad\text{within }1-\sigma,0.001≤η≤0.055,within​2−σ.0.001\leq\eta\leq 0.055,\quad\text{within }2-\sigma.
- •

Sgr A∗case (EHTKeck{}_{\text{Keck}}):0.001≤η≤0.045,within​1−σ,0.001\leq\eta\leq 0.045,\quad\text{within }1-\sigma,0.001≤η≤0.065,within​2−σ.0.001\leq\eta\leq 0.065,\quad\text{within }2-\sigma.

These results confirm that, when all other parameters are held constant,η\etashould remain positive and less than approximately0.10.1to be
consistent with the observations.

## 5Conclusion and open questions

In this paper, we have studied the shadow of rotating charged
Euler–Heisenberg black holes with GMs using high-performance
CUDA numerical codes. First, we have analyzed the horizon structure via the metric function, which
encodes the involved shadow properties of the solutions. Then, we have
applied the Hamilton–Jacobi formalism together with CUDA-accelerated
simulations to determine the shadow one dimensional curves and the energy emission rates by
varying the black hole parameters. More specifically, we have shown that the
parameterbbdoes not affect either the size of the shadow or the rate of energy emission. In contrast, we have observed that the rotation, the electric charge,
and the GM parameters. They have influenced both the shadow geometry
and the emission characteristics. Interestingly, for large values of the
rotation parameter and small values ofη\eta, we have observed that the
shadow exhibits a D-like form. However, we have found that this D-like form
gradually disappears asη\etaincreases, illustrating the interplay between
the GM and the black hole rotation. In fact, the rotation of
such black holes is primarily slowed down by these monopole contributions.

Finally, we have developed a CUDA-based numerical framework to constrain the
black hole parameters by establishing a direct comparison with astrophysical observations including EHT international collaboration.
Using this framework, we have shown that the GM parameterη\etamust
remain positive and below approximately0.10.1in order to match such observations.

This work raises several questions for future investigations. Specifically,
it would be interesting to study alternative optical behaviors. It could be possible to explore the effects of additional
matter fields including dark sources or modified interactions on both the shadow and the rate of
energy emission. Such studies could shed further light on the observational
signatures of non-standard gravity models.

## Acknowledgements

MJ gratefully acknowledges the financial support of the CNRST in the frame
of the PhD Associate Scholarship Program PASS.

## References
- [1]S. W. Hawking, D. N. Page,Thermodynamics of black
holes in anti-de Sitter space,Commun. Math. Phys. 87 (4) 577 (1983).
- [2]A. Belhaj, A. El Balali, W. El Hadri, E. Torrente-Lujan,On Universal Constants of AdS Black Holes from Hawking-Page Phase
Transition, Phys. Lett. B 811 135871 (2020),arXiv:2010.07837.
- [3]A. Belhaj, H. Belmahi, M. Benali, W. El Hadri, H. El Moumni, E.
Torrente-Lujan,Shadows of 5D Black Holes from string theory, Phys.
Lett. B 812 136025 (2021),arXiv:2008.13478.
- [4]A. Belhaj, H. Belmahi, M. Benali, Y. Hassouni, M. B. Sedra,Optical behaviors of black holes in Starobinsky-Bel-Robinson gravity, Gen.Rel.Grav. 55 110 (2023).
- [5]H. Belmahi,Constrained Deflection Angle and Shadows of
Rotating Black Holes in Einstein-Maxwell-scalar Theory,arXiv:2411.11622.
- [6]Event Horizon Telescope Collaboration.First M87
Event Horizon Telescope results. I. The shadow of the supermassive black hole, the Astrophysical Journal Letters, 875 1 L1 (2019).
- [7]Event Horizon Telescope Collaboration.First
Sagittarius A Event Horizon Telescope results. I. The shadow of the
supermassive black hole in the center of the Milky Waythe Astrophysical
Journal Letters, 930 2 L12 (2022).
- [8]K. Akiyama and al.,First M87 Event Horizon Telescope
Results. IV. Imaging the Central Supermassive Black Hole, Astrophys. J. 875
L4 (2019),arXiv:1906.11241.
- [9]K. Akiyama and al.,First M87 Event Horizon Telescope
Results. V. Imaging the Central Supermassive Black Hole, Astrophys. J. 875
L5 (2019).
- [10]K. Akiyama and al.,First M87 Event Horizon Telescope
Results. VI. Imaging the Central Supermassive Black Hole, Astrophys. J. 875
L6 (2019).
- [11]R. A. Konoplya, A. Zhidenko,Quasinormal modes of
black holes: From astrophysics to string theory, Rev. Mod. Phys. 83 793
(2011),arXiv:1102.4014 [gr-qc].
- [12]Z. Li, C. Bambi,Measuring the Kerr spin parameter of
regular black holes from their shadow, JCAP 01 041 (2014),arXiv:1309.1606 [gr-qc].
- [13]T. W. B. Kibble,Topology of cosmic domains and
strings, J. Phys. A 9, 1387 (1976).
- [14]A. Vilenkin,Cosmic strings and domain walls, Phys.
Rep. 121, 263 (1985).
- [15]A. Belhaj, M. Jemri,On Thermodynamics of Charged
Black Holes via Extended Space-time Derivatives,International Journal of
Modern Physics A, 04 41 (2026),arXiv:2511.18407 [hep-th].
- [16]P. Sedaghatnia, H. Hassanabadi, A. A. Araújo Filho,P. J. Porfirio, and W. S. Chung,Thermodynamical
properties of a deformed Schwarzschild black hole via Dunkl generalization,Int.J.Mod.Phys.A 40 07 2550019 (2025),arXiv:2302.11460.
- [17]N. Askour, A. Belhaj, L. Chakhchi, H. El Moumni, K. Masmar,On M87∗and SgrA∗Observational Constraints of Dunkl Black
Holes,JHEAp 46 100349 (2025),arXiv:2412.09196 [gr-qc].
- [18]S. E. Baddis, A. Belhaj, H. Belmahi, M. Jemri,Constraining Black Hole Shadows in Dunkl Spacetime using CUDA Numerical
Computations,Journal of High Energy Astrophysics 51 100541 (2025),arXiv:2510.16460 [gr-qc].
- [19]A. Elafrou, G. Thomas Collignon,Introduction to CUDA
Performance Optimization,Nvidia.
- [20]Nvidia,CUDA C++ Programming Guide.
- [21]S. E. Baddis, A. Belhaj, and H. Belmahi,CUDA Assisted
Swampland and Black Hole Thermodynamics,arXiv:2508.12378 [hep-th].
- [22]P. Berczik, R. Spurzem, L. Wang, S. Zhong, O. Veles, I.
Zinchenko, S. Huang, M. Tsai, G. Kennedy, S. Li, L. Naso, and C. Li,Up to 700k GPU cores, Kepler, and the Ex ascale future for simulations of
star clusters around black holes,arXiv:1312.1789 [astro-ph.IM].
- [23]A. G. M. Lewis, H. P. Pfeiffer,GPU-Accelerated
Simulations of Isolated Black Holes,Class. Quant. Grav. 35 095017 (2018),arXiv:1804.09101 [gr-qc].
- [24]R. Ginjupalli and G. Khanna,High-Precision Numerical
Simulations of Rotating Black Holes Accelerated by CUDA,arXiv:1006.0663 [physics.comp-ph].
- [25]H. Erbin,Janis- Newman algorithm:
generating rotating and NUT charged black holes, Universe 3 19 (2017),arXiv:1701.00037 [gr-qc].
- [26]A. Kamenshchik, P. Petriakova,Newman–Janis
algorithm’s application to regular black hole models, Phys. Rev. D107, 124020 (2023),arXiv:2305.04697 [gr-qc].
- [27]Z. Cai, Z. Ban, Q.-Q. Liang, H. Feng, Z.-W. Long,Construction of Rotating Sen Black Holes via the Newman-Janis
Algorithm and Applications to Accretion Disks and Shadows,JCAP 09 041
(2025),arXiv:2509.01226 [gr-qc].
- [28]D. Magos, N. Bretòn,Thermodynamics of the
Euler-Heisenberg-AdS black hole, Phys. Rev. D 102, 084011 (2020),arXiv:2009.05904 [gr-qc].
- [29]B. Hamil, B. C. Lütfüoğlu, F. Ahmed, Z. Yousaf,Thermodynamic properties of Quantum-Corrected AdS Black Hole with Phantom
Global Monopoles,Nucl.Phys.B 1014, 116861 (2025),arXiv:2404.16674
[gr-qc].
- [30]A. Chamblin, R. Emparan, C. V. Johnson, and R. C. Myers,Charged AdS Black Holes and Catastrophic Holography, Phys. Rev. D
60, 064018 (1999),arXiv:hep-th/9902170.
- [31]S. W. Wei, Y. C. Zou, Y. X. Liu, R. B. Mann,Curvature
radius and Kerr black hole shadow, JCAP 08 030 (2019),arXiv:1904.07710.
- [32]Y. DÂ´ecanini, A. Folacci, G. Esposito-Far‘ese,Universality of
high-energy absorption cross sections for black holes, Phys. Rev. D 83
044032 (2011),arXiv:1101.0781 [gr-qc].
- [33]S.-W. Wei, Y.-X. Liu,Relationship between high-energy
absorption cross section and strong gravitational lensing for a static and
spherically symmetric black hole, Phys. Rev. D 84 041501 (2011),arXiv:1103.3822 [hep-th].
- [34]V. Perlick,Calculating black hole shadows: Review of
analytical studies,Phys. Rep. 924 1 (2022),arXiv:2105.07101
[gr-qc].
- [35]P. Kocherlakota et al. [Event Horizon Telescope],Constraints on black-hole charges with the 2017 EHT observations of M87*,
Phys. Rev. D 103, no.10 104047 (2021).
- [36]L. Chakhchi, H. El Moumni and K. Masmar,Signatures of
the accelerating black holes with a cosmological constant from the Sgr A*
and M87* shadow prospects, Phys. Dark Univ. 44 101501 (2024).
- [37]D. J. Gogoi and S. Ponglertsakul,Constraints on
quasinormal modes from black hole shadows in regular non-minimal Einstein
Yang Mills gravity, Eur. Phys. J. C 84, no.6 652 (2024).

## 


- 


Major funding support from
