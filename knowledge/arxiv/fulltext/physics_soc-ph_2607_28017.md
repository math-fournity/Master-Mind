# Breathing chimera states from purely triadic interactions

**arXiv ID**: 2607.28017v1
**Authors**: Sudo Yi, Gugyoung Kim, Mi Jin Lee, S. -W. Son, B. Kahng
**Published**: 2026-07-30
**Categories**: physics.soc-ph, nlin.AO, nlin.CD
**Comments**: 17 pages, 5 figures, and 1 ancillary video (main text: 10 pages, 3 figures; Supplemental Material: 7 pages, 2 figures). Submitted to Chaos, Solitons & Fractals
**HTML URL**: https://arxiv.org/html/2607.28017v1

## Abstract

Chimera states, characterized by the coexistence of synchronized and desynchronized dynamics in identical oscillators, are typically studied in systems with pairwise interactions. Whether higher-order interactions alone can generate such symmetry-broken collective states remains unclear. Here, we show that chimera states can arise solely from triadic interactions. Furthermore, exploiting the intrinsic $π$-symmetry of the triadic coupling leads to bimodal phase distributions. We construct a bimodal Ott--Antonsen reduction that incorporates an asymmetry parameter via symmetry-breaking initial conditions, thereby achieving an exact low-dimensional description of the macroscopic dynamics. This allows us to derive an analytic condition for the emergence of chimera states and identify a bifurcation to a breathing chimera regime characterized by persistent oscillations. Furthermore, the reduced dynamics can be expressed as a Riccati-type equation, providing a geometric interpretation of the chimera state as a closed periodic orbit in the complex plane. Our results establish purely triadic coupling as a minimal mechanism for chimera formation and provide a tractable framework for studying symmetry-broken collective dynamics in systems dominated by many-body interactions.

## Full Text

Breathing chimera states from purely triadic interactions

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.28017v1 [physics.soc-ph] 30 Jul 2026\fnmark

[1]\creditConceptualization, Investigation, Writing - original draft & editing\fnmark

[1]\creditConceptualization, Investigation, Writing - review & editing\cormark

[1]\creditSupervision, Funding acquisition, Writing - review & editing\cormark

[1]\creditSupervision, Project administration, Funding acquisition, Writing - review & editing\cormark

[1]\creditSupervision, Project administration, Funding acquisition, Writing - review & editing

1]organization=CCSS, KI for Grid Modernization, Korea Institute of Energy Technology,
addressline=21 Kentech-gil,
city=Naju-si,
postcode=58330,
state=Jeollanam-do,
country=Korea

2]organization=Department of Applied Physics, Hanyang University ERICA,
addressline=55 Hanyangdaehak-ro,
city=Ansan-si,
postcode=15588,
state=Gyeonggi-do,
country=Korea

3]organization=Department of Physics, Pusan National University,
addressline=2 Busandaehak-ro 63beon-gil,
city=Geumjeong-gu,
postcode=46241,
state=Busan,
country=Korea\cortext

[1]Corresponding authors\fntext

[1]These authors contributed equally to this work.

## Breathing chimera states from purely triadic interactionsSudo YiGugyoung KimMi Jin Leemijinlee@pusan.ac.krS.-W. Sonsonswoo@hanyang.ac.krB. Kahngbkahng@kentech.ac.kr[[[

## Abstract

Chimera states, characterized by the coexistence of synchronized and desynchronized dynamics in identical oscillators, are typically studied in systems with pairwise interactions. Whether higher-order interactions alone can generate such symmetry-broken collective states remains unclear. Here, we show that chimera states can arise solely from triadic interactions. Furthermore, exploiting the intrinsicπ\pi-symmetry of the triadic coupling leads to bimodal phase distributions. We construct a bimodal Ott–Antonsen reduction that incorporates an asymmetry parameter via symmetry-breaking initial conditions, thereby achieving an exact low-dimensional description of the macroscopic dynamics. This allows us to derive an analytic condition for the emergence of chimera states and identify a bifurcation to a breathing chimera regime characterized by persistent oscillations. Furthermore, the reduced dynamics can be expressed as a Riccati-type equation, providing a geometric interpretation of the chimera state as a closed periodic orbit in the complex plane.
Our results establish purely triadic coupling as a minimal mechanism for chimera formation and provide a tractable framework for studying symmetry-broken collective dynamics in systems dominated by many-body interactions.


## keywords:chimera state\sepcoupled oscillators\septriadic interactions\sephigher-order interaction\sepnonlinear dynamics{highlights}

Chimera states can emerge from purely triadic interactions without any pairwise coupling.

The intrinsicπ\pi-symmetry of the triadic coupling induces bimodal phase distributions.

A bimodal Ott–Antonsen ansatz with an asymmetry parameter yields an exact reduction.

Riccati-type reduced dynamics reveals breathing chimeras as closed periodic orbits in the complex plane.

## 1Introduction

The phenomenon of chimera states, where synchronized and desynchronized oscillators coexist within a population of identical oscillators, has become a central topic in the study of complex systems[Kuramoto2002,Abrams2004,Abrams2006,Panaggio2015,Parastesh2021]. As a striking example of spontaneous symmetry breaking, chimera states demonstrate how macroscopic heterogeneity can emerge even in systems that are structurally homogeneous and composed of identical units[Kuramoto2002,Abrams2004].
Beyond numerous theoretical and experimental studies, chimera states have recently been observed in natural systems, most notably in synchronous firefly swarms, highlighting their broader relevance to collective dynamics[Sarfati2022].
This counterintuitive behavior was originally motivated by biological observations such as unihemispheric sleep, observed in certain birds and marine mammals, where one cerebral hemisphere remains synchronized while the other stays desynchronized and awake[Rattenborg2000,Bohm2015]. Such phenomena raise a fundamental question: how is symmetry dynamically broken in networks of otherwise identical components?

From a theoretical perspective, extensive efforts have been devoted to identifying the minimal conditions under which chimera states can emerge. Within the framework of pairwise-coupled oscillator systems, it has been revealed that phase lag and nonlocal coupling can facilitate the coexistence of coherent and incoherent subpopulations[Kuramoto2002,Abrams2004,Abrams2008,Yi2022]. In these settings, analytical approaches based on the Ott–Antonsen (OA) ansatz have played a crucial role by enabling a reduction of the high-dimensional dynamics to a tractable set of low-dimensional equations, thereby allowing systematic analysis of the existence and stability of chimera states[Abrams2008,Ott2008,Laing2009].

Meanwhile, many real-world systems may involve higher-order interactions, in which three or more elements interact simultaneously. Examples range from neural systems, where collective activity depends on interactions among many neurons rather than on pairwise coupling alone, to ecological and social systems governed by group-level dynamics. Recent developments in network science have emphasized that such higher-order interactions can fundamentally alter the collective behavior of dynamical systems, leading to enhanced multistability, abrupt transitions, and novel synchronization patterns[Skardal2019,Skardal2020,Millan2020,Boccaletti2023,Tanaka2011,Kundu2022,Luo2024]. However, since higher-order interactions are often considered together with pairwise coupling, the intrinsic role of higher-order coupling in generating chimera states remains unclear. In particular, whether purely triadic interactions alone, as a minimal form of higher-order interactions, can generate chimera states remains an open question.

In this work, we address this issue by introducing a minimal oscillator model that incorporates purely triadic interactions within a simple two-community structure. By explicitly excluding pairwise coupling, we isolate the intrinsic dynamical effects of higher-order interactions and demonstrate that they are sufficient to induce chimera states.
The resulting triadic dynamics possesses an intrinsicπ\pi-symmetry, leading naturally to bimodal phase distributions that cannot be captured by the standard OA ansatz.

To overcome this difficulty, we develop a modified OA ansatz that incorporates an asymmetry parameter to describe bimodal phase distributions. This formulation yields an exact dimensional reduction of the higher-order oscillator dynamics to a closed low-dimensional system. Building on this exact reduction, we analytically derive the criterion for the emergence of chimera states, identify the corresponding center-type fixed points, and show that the resulting dynamics is a breathing chimera, in which the partially synchronized population undergoes persistent periodic oscillations.

## 2Model and Order Parameter

We consider a system of coupled oscillators organized into two distinct groups with a phase lag, as suggested by[Abrams2008]. Here, we introduce purely higher-order interactions instead of pairwise ones, and the resulting dynamics of each oscillatoriiin groupσ\sigmais described by the following equation:d​θiσd​t=ω+∑σ′∑σ′′Kσ​σ′​σ′′Nσ′​Nσ′′​∑j=1Nσ′∑k=1Nσ′′sin⁡(θjσ′+θkσ′′−2​θiσ−α),\frac{d\theta_{i}^{\sigma}}{dt}=\omega+\sum_{\sigma^{\prime}}\sum_{\sigma^{\prime\prime}}\frac{K_{\sigma\sigma^{\prime}\sigma^{\prime\prime}}}{N_{\sigma^{\prime}}N_{\sigma^{\prime\prime}}}\sum_{j=1}^{N_{\sigma^{\prime}}}\sum_{k=1}^{N_{\sigma^{\prime\prime}}}\sin(\theta_{j}^{\sigma^{\prime}}+\theta_{k}^{\sigma^{\prime\prime}}-2\theta_{i}^{\sigma}-\alpha)~,(1)

where the group indicesσ,σ′,σ′′∈{1,2}\sigma,\sigma^{\prime},\sigma^{\prime\prime}\in\{1,2\}. The interaction term represents triadic coupling among oscillators, withσ′\sigma^{\prime}andσ′′\sigma^{\prime\prime}denoting the groups from which the two interacting oscillators are selected. The coefficientsKσ​σ′​σ′′K_{\sigma\sigma^{\prime}\sigma^{\prime\prime}}determine the coupling strength for each combination of these group labels. The strength of interaction decreases as the group of the receiving oscillator differs from the group(s) of the participating oscillator(s) [see Fig.1(a)]. The interaction term is normalized by the number of oscillators in the respective groups, ensuring that the coupling effect does not scale trivially with system size. The presence of the phase lag parameterα\alphaplays a crucial role in modulating the interaction, affecting the emergence and stability of synchronization patterns, including chimera states. Here, we consider that the number of oscillatorsNσ=NN_{\sigma}=Nfor allσ\sigma’s so that the system contains a total of2​N2Noscillators.Figure 1:Schematic view of the coupling strengthKσ​σ′​σ′′K_{\sigma\sigma^{\prime}\sigma^{\prime\prime}}and the initial phase distributions.
(a) Intra-group coupling is assumed to be the strongest, and coupling is weakened by a termμ\mudepending on the number of oscillators in the opposite group.
(b) Initial phase distributionsfσ​(θ,t=0)f_{\sigma}(\theta,t=0)of the two groups. Group 1 is prepared in a symmetry-broken synchronized state withη1≠0.5\eta_{1}\neq 0.5andQ1=1Q_{1}=1, whereas Group 2 is initialized in a symmetric partially synchronized bimodal state withη2=0.5\eta_{2}=0.5andQ2<1Q_{2}<1.

The coupling tensorKσ​σ′​σ′′K_{\sigma\sigma^{\prime}\sigma^{\prime\prime}}is determined by the community composition of the interacting triad. As schematically shown in Fig.1(a), the coupling strength in this system is given byKσ​σ′​σ′′=μ(1−δσ​σ′)+(1−δσ​σ′′),K_{\sigma\sigma^{\prime}\sigma^{\prime\prime}}=\mu^{(1-\delta_{\sigma\sigma^{\prime}})+(1-\delta_{\sigma\sigma^{\prime\prime}})}~,(2)

whereμ\muis defined by the inter-group interaction parameter (μ∈[0,1)\mu\in[0,1)) andδ\deltadenotes the Kronecker delta. This formulation determines the interaction strength based on the group membership of the interacting oscillators. We set the intra-community triadic interaction strength to unity,Kσ​σ​σ=1K_{\sigma\sigma\sigma}=1, and assume that the coupling is weakened by a positive factorμ<1\mu<1whenever an oscillator from the other community participates in the interaction. Accordingly, configurations containing one oscillator from the opposite community have strengthμ\mu, while those containing two oscillators from the opposite community have strengthμ2\mu^{2}. This structure ensures that intra-group interactions remain strong while inter-group interactions are suppressed depending on the value ofμ\mu, which plays a crucial role in the emergence of chimera states.

Order parameter —The phase synchronization is typically quantified by the Kuramoto order parameterRσ​ei​ψσ=1Nσ​∑j=1Nσei​θjσ,R_{\sigma}e^{{\rm i}\psi_{\sigma}}=\frac{1}{N_{\sigma}}\sum_{j=1}^{N_{\sigma}}e^{{\rm i}\theta_{j}^{\sigma}}~,(3)

whereRσR_{\sigma}captures the coherence of oscillator phases in a groupσ\sigma. In the present triadic interaction model, however, the intrinsicπ\pi-symmetry of the phase dynamics in Eq. (1) leads to the formation of bimodal phase distributions, in which two clusters separated byπ\picoexist withRσ≈0R_{\sigma}\approx 0, even when the system exhibits a high coherence of phase synchronization. Therefore, in the present system withπ\pi-symmetry, it is more appropriate to employ the Daido order parameter[Daido1996]defined asQσ​ei​χσ=1Nσ​∑j=1Nσei2​θjσ,Q_{\sigma}e^{{\rm i}\chi_{\sigma}}=\frac{1}{N_{\sigma}}\sum_{j=1}^{N_{\sigma}}e^{{\rm i}2\theta_{j}^{\sigma}}~,(4)

which remains sensitive to bimodal phase coherence.

In the following, we define a chimera state as a configuration in which one community exhibits a fully phase-locked bimodal distribution (Q1=1Q_{1}=1), while the other remains only partially synchronized (Q2<1Q_{2}<1). This distinction allows us to characterize the coexistence of coherent and incoherent dynamics within the higher-order interaction framework.

## 3Modified OA Ansatz

The intrinsicπ\pi-symmetry of the triadic interaction naturally generates stable bimodal phase distributions, which cannot be described by the standard OA ansatz assuming unimodal coherence[Ott2008]. To incorporate this bimodal structure, we decompose the phase density into two anti-phase subpopulations,fσ=ησ​fσ,a+(1−ησ)​fσ,b,f_{\sigma}=\eta_{\sigma}f_{\sigma,a}+(1-\eta_{\sigma})f_{\sigma,b}~,(5)

where the adjustable valueησ\eta_{\sigma}is the asymmetry parameter of the distribution [Fig.1(b)] and the two terms in Eq. (5) satisfy theπ\pi-shift symmetryfσ,b​(θ)=fσ,a​(θ−π)f_{\sigma,b}(\theta)=f_{\sigma,a}(\theta-\pi).
Applying the OA ansatz separately to each subpopulation allows us to rewrite the phase density by decomposing odd and even terms asfσ=12​π(1+[∑n=1∞aσ2​nei2​n​θ+(2ησ−1)∑n=1∞aσ2​n−1ei​(2​n−1)​θ]+c.c.),f_{\sigma}=\frac{1}{2\pi}\left(1+\left[\sum_{n=1}^{\infty}{a_{\sigma}^{2n}e^{{\rm i}2n\theta}}+(2\eta_{\sigma}-1)\sum_{n=1}^{\infty}{a_{\sigma}^{2n-1}e^{{\rm i}(2n-1)\theta}}\right]+\mathrm{c.c}.\right),(6)

and yields a reduced bimodal manifold parameterized by the asymmetry parameterησ\eta_{\sigma}(see Supplemental Material Sec. S1.B for details). Under this construction, the macroscopic dynamics remains reducible to a low-dimensional manifold described by a complex amplitudeaσ≡rσ​e−i​ψσa_{\sigma}\equiv r_{\sigma}e^{-{\rm i}\psi_{\sigma}},
whererσ∈[0,1]r_{\sigma}\in[0,1]is the real-valued modulus of the complex amplitude and represents the degree of synchronization within each peak of the bimodal distribution.

A direct consequence of this bimodal OA formulation is that the Kuramoto and Daido order parameters becomeRσ=|2​ησ−1|​rσ,Qσ=rσ2.R_{\sigma}=\left|2\eta_{\sigma}-1\right|r_{\sigma}~,\qquad Q_{\sigma}=r_{\sigma}^{2}~.(7)

See Supplemental Material Sec. S1.B for the derivation of Eq. (7) from the modified bimodal OA ansatz.
These expressions reveal that the first-order coherenceRσR_{\sigma}is controlled explicitly by the asymmetry parameterησ\eta_{\sigma}, whereas the second-order coherenceQσQ_{\sigma}depends only on the modulus of the complex amplitudeaσa_{\sigma}, i.e.,rσr_{\sigma}. In particular, the symmetric bimodal stateησ=0.5\eta_{\sigma}=0.5givesRσ=0R_{\sigma}=0, even when the second-order coherence is maintained (Qσ>0Q_{\sigma}>0).

This framework enables an exact dimensional reduction of the microscopic dynamics into a small set of macroscopic variables. Here, the asymmetry parameterησ\eta_{\sigma}determines the initial imbalance between the two anti-phase subpopulations and remains conserved throughout the dynamics, since the two subpopulations evolve independently within the reduced manifold. Consequently,ησ\eta_{\sigma}controls the initial degree of symmetry breaking and thereby influences the emergence of chimera states.

Initial conditions —It is well known that, since higher-order interaction systems exhibit strong multistability, the resulting macroscopic dynamics depends sensitively on the initial condition[Skardal2019,Zhang2024]. To induce chimera states, we confine asymmetric initial phase distributions inspired by unihemispheric sleep[Rattenborg2000], as illustrated in Fig.1(b): one community (σ=1\sigma=1) is initialized in a symmetry-broken coherent state withη1≠0.5\eta_{1}\neq 0.5andQ1=1Q_{1}=1, while the other (σ=2\sigma=2) remains symmetric withη2=0.5\eta_{2}=0.5and partial synchronization0<Q2<10<Q_{2}<1. This asymmetry acts as a dynamical trigger that drives the coexistence of synchronized and partially synchronized collective states.
The specific initial conditions used in the numerical simulations are given in Supplemental Material Sec. S1.C.

Reduced dynamics —By substituting the modified OA ansatz into the continuity equation for the phase densityffand collecting the resulting Fourier harmonics, we reduce the infinite-dimensional dynamics to a closed set of equations for the macroscopic variables (see Supplemental Material Sec. S1.D for details). Usingaσ=rσ​e−i​ψσa_{\sigma}=r_{\sigma}e^{-{\rm i}\psi_{\sigma}}in Eq. (6), the system is fully described by the amplituderσr_{\sigma}and the phaseψσ\psi_{\sigma}of each community. Focusing on the interaction between the two communities, it is convenient to introduce the phase differenceϕ≡ψ1−ψ2\phi\equiv\psi_{1}-\psi_{2}. Under the asymmetric initialization described above, withr1=1r_{1}=1,η1≠0.5\eta_{1}\neq 0.5, andη2=0.5\eta_{2}=0.5, the dynamics simplifies to a two-dimensional system governing the evolution ofr≡r2r\equiv r_{2}andϕ\phi(with the shorthandη≡η1\eta\equiv\eta_{1}):r˙\displaystyle\dot{r}=12​r​(1−r4)​μ2​(2​η−1)2​cos⁡(2​ϕ+α),\displaystyle=\frac{1}{2r}(1-r^{4})\,\mu^{2}(2\eta-1)^{2}\cos(2\phi+\alpha)~,(8)ϕ˙\displaystyle\dot{\phi}=−12​r2​(1+r4)​μ2​(2​η−1)2​sin⁡(2​ϕ+α)+(2​η−1)2​sin⁡α.\displaystyle=-\frac{1}{2r^{2}}(1+r^{4})\,\mu^{2}(2\eta-1)^{2}\sin(2\phi+\alpha)+(2\eta-1)^{2}\sin\alpha~.(9)

For given initial conditions and parametersμ\mu,η\eta, andα\alpha, it provides a minimal description of the interplay between coherence (rr) and phase difference (ϕ\phi), allowing direct analysis of steady states, stability, and oscillatory behavior.

Fixed points —The reduced system admits steady-state solutions determined byr˙=0\dot{r}=0andϕ˙=0\dot{\phi}=0. Fixed points arise either atr=1r=1(fully synchronized state) or whencos⁡(2​ϕ+α)=0\cos(2\phi+\alpha)=0fromr˙=0\dot{r}=0. The latter corresponds to partially synchronized states, which we identify as chimera states as shown in Fig.2. Together withϕ˙=0\dot{\phi}=0, the condition for the synchronized regime in the second groupσ=2\sigma=2is given byμ≥sin⁡α\mu\geq\sqrt{\sin\alpha}(for full synchronization) andμ<sin⁡α\mu<\sqrt{\sin\alpha}(for partial synchronization),
which defines a critical threshold for the emergence of chimera states when equality holds: above this threshold the system converges to full synchronization resulting inQ1=1Q_{1}=1andQ2=1Q_{2}=1, whereas below it chimera states (Q1=1Q_{1}=1andQ2<1Q_{2}<1equivalent tor<1r<1) become accessible, as portrayed in Figs.2(a) and2(b). Stability analysis further shows that these chimera states (r≠1r\neq 1) correspond to center-type fixed points with zero trace and positive determinant of a Jacobian matrix for Eqs. (8) and (9) (see Supplemental Material Sec. S2 for details). This implies the emergence of a family of neutrally stable closed orbits surrounding each center-type fixed point in phase space, corresponding to abreathing chimera state[Abrams2008], while the fully synchronized state (r=1r=1) behaves as either a stable sink or an unstable source depending on parameters. The simulation results forQ2Q_{2}in the regimeμ<sin⁡α\mu<\sqrt{\sin\alpha}coincide with the theoretical prediction obtained using the theoretical value ofrrfrom Eqs. (7), (8), and (9) in Fig.2(c), showing the corresponding closed-orbit behavior.Figure 2:Phase diagrams in the(α,μ)(\alpha,\mu)space and temporal dynamics ofQ2Q_{2}. (a) Instantaneous value ofQ2Q_{2}att=20000t=20000in the thermodynamic limit
(Nσ→∞N_{\sigma}\rightarrow\infty). (b) Corresponding result from numerical simulations withN1=N2=10000N_{1}=N_{2}=10000. Color represents the instantaneous value ofQ2Q_{2}after the transient, which varies in time due to the breathing dynamics. The theoretical boundary (red solid line), given byμ=sin⁡α\mu=\sqrt{\sin\alpha}, is in agreement with the boundary of the breathing chimera state region obtained from numerical simulations. See Supplementary Video S1 for the temporal evolution of the phase diagrams in panels (a,b). (c) Time evolution ofQ2Q_{2}for(α,μ)=(π/4,0.5)(\alpha,\mu)=(\pi/4,0.5). The numerical simulation result (thick black line) agrees well with the theoretically predicted thermodynamic-limit result (thin red line).
(d) Zoomed-in view of the shaded time interval in panel (c), showing one oscillation period.
The theoretical amplitude and period,Δ​Q2≃0.266\Delta Q_{2}\simeq 0.266andT≃475.0T\simeq 475.0, agree with the corresponding values measured from the simulation,Δ​Q2≃0.266\Delta Q_{2}\simeq 0.266andT≃474.9T\simeq 474.9.
The absolute differences between theory and simulation are approximately5.1×10−45.1\times 10^{-4}forΔ​Q2\Delta Q_{2}and6.4×10−26.4\times 10^{-2}forTT.
The finite-size scaling of the residual discrepancy between the numerical simulation and the OA prediction is presented in Supplemental Material Sec. S5.

## 4Dynamics in Complex Plane and Geometric Interpretation

The breathing chimera appears as persistent oscillations in the reduced variables. To interpret this motion geometrically, we combine the reduced variables into a single complex order parameterZ=r2​ei​ΦZ=r^{2}e^{{\rm i}\Phi}withΦ=2​ϕ+α\Phi=2\phi+\alpha. The dynamics then reduces to the Riccati-type equation[Marvel2009]Z˙=A​(1−Z2)+2​i​B​Z,\dot{Z}=A\left(1-Z^{2}\right)+2{\rm i}BZ~,(10)

whereA=μ2​(1−2​η)2A=\mu^{2}(1-2\eta)^{2}andB=sin⁡α​(1−2​η)2B=\sin\alpha\,(1-2\eta)^{2}.

This compact form reveals that the breathing chimera is governed by an exactly tractable low-dimensional structure. The Riccati equation admits an invariant, confining the dynamics to a closed periodic orbit in the complex plane. WritingZ=X+i​YZ=X+{\rm i}Y, the invariant takes the formX2+(Y−A2​C0)2=A2−4​C0​(B−C0)4​C02,X^{2}+\left(Y-\frac{A}{2C_{0}}\right)^{2}=\frac{A^{2}-4C_{0}(B-C_{0})}{4C_{0}^{2}}~,(11)

whereC0C_{0}is the conserved value of the invariant determined by the initial condition of the complex variableZZfor given system parametersAAandBB(see Supplemental Material Sec. S3.B for details). This representation exposes the invariant structure underlying the breathing motion and allows the reduced trajectory to be interpreted as a circular orbit in the complex plane. Figure3illustrates how the reduced dynamics converges to the fully synchronized state or evolves along neutrally stable closed orbits depending onα\alpha.Figure 3:Phase portraits in the complex plane, shown in polar coordinates, forμ=0.5\mu=0.5.
The trajectories (red curves), initialized atQ2​(0)=0.6Q_{2}(0)=0.6, either approach the fully synchronized state (Q2=1Q_{2}=1) or evolve along neutrally stable closed orbits depending onα\alpha.
(a) Forα=0.2\alpha=0.2, the trajectory approaches the fully synchronized state (Q2=1Q_{2}=1).
(b,c) Forα=0.3\alpha=0.3andα=0.7\alpha=0.7, the trajectories evolve along neutrally stable closed orbits, corresponding to breathing chimera states.

The oscillatory dynamics of the breathing chimera can be characterized by its period and amplitude. From the linear stability analysis around the center-type fixed point, the oscillation frequency is determined by the eigenvalues of the Jacobian, yielding the periodT/π=(1−2​η)−2​(sin2⁡α−μ4)−1/2T/{\pi}={(1-2\eta)^{-2}{(\sin^{2}\alpha-\mu^{4})^{-1/2}}}[Fig.2(d)]. This expression shows that the period depends only on the system parameters and diverges asμ→sin⁡α\mu\to\sqrt{\sin\alpha}, indicating critical slowing down near the bifurcation point.
In contrast, the oscillation amplitude depends on the initial condition through the invariant of motion. For example, for symmetric initial states, the amplitude scales asΔ​Q∼μ2/sin⁡α\Delta Q\sim{\mu^{2}}/{\sin\alpha}[Fig.2(d)],
demonstrating that the extent of desynchronization is controlled by both coupling strength and phase lag. See Supplemental Material Sec. S4 for detailed derivations.

## 5Discussion and Conclusions

In this work, we demonstrated that chimera states can emerge in a minimal oscillator system governed solely by triadic interactions, without any pairwise coupling. A central feature of the dynamics is the intrinsicπ\pi-symmetry generated by the triadic coupling, which naturally produces bimodal phase distributions. To capture this structure, we developed a modified Ott–Antonsen ansatz incorporating an asymmetry parameter that characterizes the imbalance between two anti-phase subpopulations, enabling an exact dimensional reduction of the microscopic dynamics into a low-dimensional macroscopic system.

The exact reduction further allows us to derive the conditions for the emergence of chimera states and identified the bifurcation threshold separating synchronized and oscillatory regimes. Reformulating the reduced dynamics in terms of a complex order parameter further revealed that the breathing chimera corresponds to persistent periodic orbits with a simple geometric structure in the complex plane. The role of triadic coupling is thus not simply to replace pairwise coupling, but to impose an intrinsicπ\pi-symmetry that supports bimodal collective states: within this bimodal structure, an initial imbalance between the two anti-phase subpopulations allows one community to remain fully synchronized, while the other exhibits partial synchronization with persistent oscillations.

These results establish an analytically tractable mechanism for chimera formation driven by purely higher-order interactions, suggesting more broadly that many-body coupling can support symmetry-broken collective dynamics distinct from those generated by conventional pairwise interactions, with potential implications for biological and neural systems where higher-order interactions may play an intrinsic role[Parastesh2021,Boccaletti2023].
The present analysis focuses on identical oscillators with all-to-all purely triadic interactions and prescribed asymmetric initial conditions; these assumptions make the model analytically tractable but leave open how the mechanism is affected by frequency heterogeneity, noise, sparse hypergraph topology, and mixed pairwise–triadic coupling. Addressing these extensions would clarify the robustness of breathing chimera states driven by purely higher-order interactions in more realistic networked systems.

## 6Acknowledgments

This work was supported by the National Research Foundation (NRF) of Korea through Grant Numbers. RS-2023-00279802 (S.Y, B.K.), RS-2024-00341317 (M.J.L.), and RS-2026-25488703 (S.-W.S.). This work was also partly supported by Korea Research Institute for defense Technology planning and advancement (KRIT) - Grant funded by Defense Acquisition Program Administration (DAPA), South Korea (KRIT-CT-23-026, Integrated Underwater Surveillance Research Center for Adapting Future Technologies, 2023–2029). We thank APCTP, Pohang, Korea, for their hospitality during the Topical Research Program [APCTP-2025-T04], from which this work greatly benefited.\printcredits

## References

## 


- 


Major funding support from
