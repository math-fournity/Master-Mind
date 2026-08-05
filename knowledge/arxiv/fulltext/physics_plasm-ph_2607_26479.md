# Kinetic Optimization of Magnetic Mirror Confinement: Beyond Classical Loss-Cone Theory

**arXiv ID**: 2607.26479v1
**Authors**: Lukas Einkemmer, Martin Guerra, Qin Li, Leonardo Zepeda-Núñez
**Published**: 2026-07-29
**Categories**: physics.plasm-ph, math.OC
**Comments**: 24 pages, 15 figures
**HTML URL**: https://arxiv.org/html/2607.26479v1

## Abstract

Magnetic mirrors are among the conceptually simplest plasma confinement configurations and remain promising candidates for thermonuclear fusion. Their design requires shaping an externally applied magnetic field to confine plasma within an open-ended cylindrical device. In contrast to toroidally closed devices such as tokamaks and stellarators, confinement in magnetic mirrors depends intrinsically on kinetic mechanisms, particularly velocity-space trapping and particle loss through the open ends.   We formulate magnetic mirror design as a PDE-constrained optimization problem governed by a reduced multispecies drift-kinetic-Poisson model. The resulting optimization reveals two physical effects not captured by the classical loss-cone argument. First, the self-consistent electric field generated through Poisson coupling acts as a secondary confinement barrier and substantially alters particle retention in the nonlinear regime. Second, the optimized magnetic-field configuration depends qualitatively on the underlying kinetic model: an electron-only model favors an unconventional centrally peaked field, whereas the fully coupled electron-ion model recovers the classical boundary-peaked mirror configuration. These results demonstrate that optimal magnetic mirror design cannot be determined solely from loss-cone considerations, but must account for the self-consistent nonlinear kinetic dynamics of the plasma.

## Full Text

Kinetic Optimization of Magnetic Mirror Confinement: Beyond Classical Loss-Cone Theory

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
- License: CC BY 4.0arXiv:2607.26479v1 [physics.plasm-ph] 29 Jul 2026

## Kinetic Optimization of Magnetic Mirror Confinement: Beyond Classical Loss-Cone TheoryLukas EinkemmerDepartment of Mathematics, Universität Innsbruck, Innsbruck, AustriaMartin GuerraDepartment of Mathematics, University of Wisconsin-Madison, Madison, WI, USAQin Li22footnotemark:2Leonardo Zepeda-NúñezGoogle Research, Mountain View, CA, USA

## Abstract

Magnetic mirrors are among the conceptually simplest plasma confinement configurations and remain promising candidates for thermonuclear fusion. Their design requires shaping an externally applied magnetic field to confine plasma within an open-ended cylindrical device. In contrast to toroidally closed devices such as tokamaks and stellarators, confinement in magnetic mirrors depends intrinsically on kinetic mechanisms, particularly velocity-space trapping and particle loss through the open ends.

We formulate magnetic mirror design as a PDE-constrained optimization problem governed by a reduced multispecies drift-kinetic–Poisson model. The resulting optimization reveals two physical effects not captured by the classical loss-cone argument. First, the self-consistent electric field generated through Poisson coupling acts as a secondary confinement barrier and substantially alters particle retention in the nonlinear regime. Second, the optimized magnetic-field configuration depends qualitatively on the underlying kinetic model: an electron-only model favors an unconventional centrally peaked field, whereas the fully coupled electron–ion model recovers the classical boundary-peaked mirror configuration. These results demonstrate that optimal magnetic mirror design cannot be determined solely from loss-cone considerations, but must account for the self-consistent nonlinear kinetic dynamics of the plasma.

## 1Introduction

The confinement of high-temperature plasmas is a fundamental challenge in the development of controlled thermonuclear fusion[8]. The goal is to design a device capable of confining hot plasma particles at sufficiently high density and for sufficiently long times to sustain nuclear fusion reactions. While much of the research effort has focused on the design and control of tokamaks and stellarators, alternative designs have also shown significant promise. Among them are magnetic mirror devices[28], which have recently attracted renewed attention and are undergoing active development[29].

In contrast with relying on toroidal closure for confinement (as is done in tokamaks and stellarators), a magnetic mirror typically consists of a cylindrical device with a magnetic field strength that increases towards the ends. Such stronger fields exert a force on particles so the particles that travel towards the ends eventually reverse directions. It effectively generates two mirrors at the ends that bounce particles back and forth in the cylindrical chamber, thus confining particles.

Although conceptually simple, pure magnetic mirror devices are inherently lossy. Plasma particles with insufficient velocity perpendicular to the magnetic field can escape through the ends of the device. A central objective in magnetic mirror design is therefore to engineer magnetic field configurations that minimize particle leakage, thus maximizing long-time confinement. Mathematically, this objective naturally leads to an inverse design problem in which one seeks an optimal magnetic field configuration𝐁\mathbf{B}maximizing plasma confinement:arg​max𝐁⁡𝒥​(𝐁),\operatorname*{arg\,max}_{\mathbf{B}}\mathcal{J}(\mathbf{B}),(1.1)

where𝒥\mathcal{J}measures the amount of plasma retained inside the confinement region over a prescribed time horizon. The classic concept of the “loss cone” states that particles that have an unfavorable ratio of the velocity parallel versus the velocity perpendicular to the magnetic field can escape, forming a depleted cone in phase space[24]. Such theories are primarily based on single-particle trajectory arguments and largely neglect self-consistent collective effects generated by the plasma itself. In reality, however, the plasma system is intrinsically nonlinear: the collective charge distribution generates a self-consistent electric field, which in turn significantly modifies particle confinement and escape dynamics. Understanding the role of this self-consistent electrostatic effect in magnetic mirror optimization is the primary objective of this work.

The collective dynamics is described by Vlasov-type kinetic equations. While the most fundamental formulation is a multi-species3​D​3​V3\text{D}3\text{V}Vlasov system, the presence of a strong background magnetic field permits a substantial reduction of complexity. Averaging over the fast circular motion of the particles perpendicular to the magnetic field (the gyromotion) results in a drift-kinetic equation that only depends on the velocity parallel to the magnetic field and the magnitude of the velocity perpendicular to it. The latter is expressed in terms of the magnetic momentμ\mu, and is an adiabatic invariant. It only enters the drift-kinetic equations as a (continuous) parameter. If we further assume a homogeneous plasma in the direction perpendicular to the magnetic field, we obtain a1​D​1​V1\text{D}1\text{V}kinetic model parameterized by continuousμ\mu-slices[7,32,22,21,30]. This reduced formulation preserves the essential kinetic features while significantly lowering the computational cost. Coupling this reduced model with the confinement objective (1.1) yields a PDE-constrained optimization framework for magnetic mirror design, which we will investigate in this work.

Our findings reveal several nonclassical confinement phenomena. First, confinement performance cannot be accurately predicted solely through classical mirror-ratio heuristics: magnetic field configurations with similar mirror ratios may exhibit substantially different confinement behavior once self-consistent electrostatic effects are incorporated. In particular, the induced electric potential forms an additional confinement barrier that significantly alters particle escape dynamics (especially for electrons). Second, through running PDE-constrained optimization using reverse-mode automatic differentiation, we discover that the optimal magnetic topology depends strongly on the plasma composition. In the single-species regime, optimized configuration turns out to favor nonclassical centrally-peaked structures that have a double-well form. This deviates substantially from traditional design of single-well mirror profiles. In the multi-species setting, the disparate electron-ion mass ratio introduces strongly separated confinement timescales, leading to a two-stage leakage process and the recovery of the classical one-well design.

The remainder of the paper is organized as follows. In Section2, we derive the reduced kinetic formulation and present the PDE-constrained optimization framework. In Section3, we investigate the emergence of nonlinear self-consistent confinement effects and we demonstrate the limitations of classical loss-cone predictions through extensive numerical experiments. Section4presents optimized magnetic confinement configurations for both single-species and multi-species plasmas.

## 1.1Related Work

The mathematical formulation and numerical simulation of magnetic mirror plasmas intersect several active areas of research, including reduced kinetic modeling, structure-preserving numerical methods for Vlasov equations, and PDE-constrained optimization through differentiable simulation.

The foundational physics of magnetic mirrors and the associated loss-cone mechanism have long been studied theoretically[28,27,6]. Given that the charged particles undergo rapid gyromotion around magnetic field lines, direct simulation of the full multi-species3​D​3​V3\text{D}3\text{V}Vlasov system is computationally demanding. Modern multiscale plasma modeling therefore heavily exploits asymptotic reductions based on strong background magnetic fields. In particular, by averaging over the fast cyclotron motion and exploiting the adiabatic invariance of the magnetic moment, one obtains drift-kinetic and gyrokinetic descriptions that substantially reduce computational complexity while preserving the essential confinement dynamics[7,6].
This formulation follows a similar philosophy by adopting a continuousμ\mu-parameterized reduced kinetic description that isolates the slow confinement dynamics while averaging over fast gyromotion.

The reduced multi-species Vlasov–Poisson system nevertheless remains numerically challenging due to the strong disparity between electron and ion time scales. Standard explicit Eulerian discretizations are severely restricted by the Courant–Friedrichs–Lewy (CFL) condition associated with the fastest characteristic speeds[19]. Consequently, Semi-Lagrangian (SL) methods have become a central tool in kinetic plasma simulations[30,11,10,15,16]. By transporting the distribution function along characteristic trajectories, SL schemes substantially relax the CFL constraint while retaining favorable conservation properties and positivity when combined with suitable interpolation procedures.

In parallel, plasma confinement optimization has increasingly benefited from advances in PDE-constrained optimization, scientific machine learning, and differentiable programming[12,14,18,13,2,9,4,3,26]. Traditional approaches to magnetic topology optimization, including the design of quasi-isodynamic stellarators and mirror configurations, often rely on surrogate models or gradient-free heuristics due to the large dimensionality and complexity of the design space[34,1]. More recently, differentiable simulation frameworks have enabled gradient-based optimization directly through discretized plasma solvers by applying reverse-mode automatic differentiation to the numerical pipeline[20,23,5,31,25]. Such approaches permit the computation of discrete gradients of macroscopic quantities, including confinement metrics and energy functionals, with respect to control parameters and boundary conditions.

While reduced kinetic modeling, structure-preserving Vlasov solvers, and differentiable PDE optimization have each been extensively investigated independently, our goal here is to study the effect of kinetic nonlinearities on the optimal magnetic field configuration. In particular, the role of the self-consistent electric field in reshaping confinement behavior and how it modifies loss cone dynamics is investigated. Our code enables a complete end-to-end differentiable optimization of magnetic mirrors within a three-dimensional drift-kinetic model.

## 2Mathematical Formulation

In this section, we derive a reduced kinetic formulation for magnetic mirror confinement based on the adiabatic invariance of the magnetic moment. Starting from the full particle dynamics under a strong magnetic field, we perform a guiding-center reduction that leads to a1​D​1​V1\text{D}1\text{V}Vlasov–Poisson system parameterized by the magnetic momentμ\mu. We then formulate the corresponding PDE-constrained optimization problem for magnetic mirror design.

## 2.1Guiding-center reduction and magnetic moment

We begin with the dynamics of a single charged particle under an external magnetic field𝐁\mathbf{B}. Writing𝐁=B0​𝐛,\mathbf{B}=B_{0}\mathbf{b},

whereB0=|𝐁|B_{0}=|\mathbf{B}|denotes the magnetic field strength and𝐛\mathbf{b}is the associated unit direction vector. The particle velocity can then be decomposed into parallel and perpendicular components:𝐯=v∥​𝐛+𝐯⟂,v∥=𝐯⋅𝐛,|𝐯⟂|=v⟂.\mathbf{v}=v_{\parallel}\mathbf{b}+\mathbf{v}_{\perp},\qquad v_{\parallel}=\mathbf{v}\cdot\mathbf{b},\qquad|\mathbf{v}_{\perp}|=v_{\perp}.

The corresponding magnetic moment is defined byμ=v⟂22​B0.\mu=\frac{v_{\perp}^{2}}{2B_{0}}.

Ignoring the electric field for the moment, the particle trajectory satisfies the Lorentz force law. Choose units such that the mass and magnitude of the charge of the particles is unity and that the particles are positively charged:𝐱˙=𝐯,𝐯˙=𝐯×𝐁.\dot{\mathbf{x}}=\mathbf{v},\qquad\dot{\mathbf{v}}=\mathbf{v}\times\mathbf{B}.

Since the Lorentz force is orthogonal to the velocity, the kinetic energy is conserved:dd​t​|𝐯|22=𝐯⋅𝐯˙=𝐯⋅(𝐯×𝐁)=0.\frac{\mathrm{d}}{\mathrm{d}t}\frac{|\mathbf{v}|^{2}}{2}=\mathbf{v}\cdot\dot{\mathbf{v}}=\mathbf{v}\cdot(\mathbf{v}\times\mathbf{B})=0.

When the magnetic field is spatially uniform, for example𝐁=B​z^\mathbf{B}=B\hat{z}, the perpendicular velocity undergoes circular motion with cyclotron frequencyΩc=B\Omega_{c}=B, while the parallel component remains constant. The resulting trajectory is a helix along the magnetic field lines. In this regime, the magnetic momentμ\muis exactly conserved.

For slowly varying magnetic fields, the magnetic moment remains approximately conserved. Denoting byLB:=B|∇B|L_{B}:=\frac{B}{|\nabla B|}, the characteristic magnetic variation length scale and byρ=v⟂B\rho=\frac{v_{\perp}}{B}the Larmor radius, we define the small parameterε=ρLB.\varepsilon=\frac{\rho}{L_{B}}.

In the strongly magnetized regimeε≪1\varepsilon\ll 1, standard guiding-center theory yields the adiabatic estimated​μd​(Ωc​t)=𝒪​(ε)​μ\frac{\mathrm{d}\mu}{\mathrm{d}(\Omega_{c}t)}=\mathcal{O}(\varepsilon)\mu. Thus, over the fast gyromotion timescale, the magnetic moment varies only weakly and may be treated as an adiabatic invariant.

Averaging over the fast gyromotion therefore yields an effective reduced dynamics along the magnetic field direction. The resulting model evolves only in the longitudinal spatial coordinate and parallel velocity, while the magnetic momentμ\muacts as a parameter labeling distinct kinetic slices.

## 2.2Drift-kinetic system

Under the guiding-center approximation, the multi-species Vlasov equation reduces to the following1​D​1​V1\text{D}1\text{V}system parameterized byμ\mu[22,32]. This system is typically termed drift-kinetic model.∂tfs+v​∂zfs+(qsms​E​(t,z)−μ​∂z|𝐁​(z)|)​∂vfs=0,\partial_{t}f_{s}+v\partial_{z}f_{s}+\left(\frac{q_{s}}{m_{s}}E(t,z)-\mu\partial_{z}|\mathbf{B}(z)|\right)\partial_{v}f_{s}=0,(2.1)

wherefs​(t,z,v,μ)f_{s}(t,z,v,\mu)denotes the distribution function for speciess∈{e,i}s\in\{e,i\};z∈ℝz\in\mathbb{R}is the longitudinal spatial coordinate;v∈ℝv\in\mathbb{R}is the parallel velocity;μ∈ℝ+\mu\in\mathbb{R}_{+}is the magnetic moment parameter; andqsq_{s}andmsm_{s}denote the charge and mass of speciesss, respectively.

The effective acceleration contains two distinct contributions: the self-consistent electric fieldE​(t,z)E(t,z); and the magnetic mirror force−μ​∂z|𝐁​(z)|-\mu\partial_{z}|\mathbf{B}(z)|. Within the reduced formulation, the magnetic momentμ\muremains fixed along characteristics and therefore acts as a parameter rather than a dynamical variable.

The electric field is generated self-consistently through a one-dimensional Poisson equation. After normalizing the charges so thatqi=1,qe=−1,q_{i}=1,\qquad q_{e}=-1,

the electrostatic potentialϕ\phisatisfies{−∂z​zϕ+∂zϕ​∂z|𝐁​(z)||𝐁​(z)|=2​π​|𝐁​(z)|​∬(fi−fe)​dv​dμ,ϕ​(t,−Lz)=ϕ​(t,Lz)=0.\left\{\begin{aligned} -\partial_{zz}\phi+\partial_{z}\phi\frac{\partial_{z}|\mathbf{B}(z)|}{|\mathbf{B}(z)|}&=2\pi|\mathbf{B}(z)|\iint\left(f_{i}-f_{e}\right)\,\mathrm{d}v\,\mathrm{d}\mu,\\
\phi(t,-L_{z})=\phi(t,L_{z})&=0.\end{aligned}\right.(2.2)

The electric field is then recovered throughE​(t,z)=−∂zϕ​(t,z),E(t,z)=-\partial_{z}\phi(t,z),

and the corresponding electric energy asℰ​(t)=12​∫E​(t,z)2​dz.\mathcal{E}(t)=\frac{1}{2}\int E(t,z)^{2}\,\mathrm{d}z.

We define the following two density quantities that will play an important role throughout the paper: the three-dimensional density, which is given byρs​(t,z)=2​π​|𝐁​(z)|​∬fs​(t,z,v,μ)​dv​dμ,\rho_{s}(t,z)=2\pi|\mathbf{B}(z)|\iint f_{s}(t,z,v,\mu)\,\mathrm{d}v\,\mathrm{d}\mu,(2.3)

and the effective longitudinal density, which is given byρs1​D​(t,z)=∬fs​(t,z,v,μ)​dv​dμ.\rho_{s}^{1D}(t,z)=\iint f_{s}(t,z,v,\mu)\,\mathrm{d}v\,\mathrm{d}\mu.(2.4)

The important distinction between these two definitions arises because increasing the magnetic field strength pushes the field lines closer together. Since particles mostly follow these magnetic field lines, increasing the field strength also increases the particle density, as can be seen from the|𝐁​(z)||\mathbf{B}(z)|term in (2.3). However, if we integrate out the two spatial dimensions perpendicular to the magnetic field, the corresponding line density in equation (2.4) does not have this dependence on the magnetic field. Since our model only depends on one spatial variable and takes this compression effect into account, it is more natural to consider the one-dimensional line density, which is also the density corresponding to the mass/charge conservation in our drift-kinetic equation.

## 2.3PDE-constrained optimization problem

The goal of magnetic mirror design is to identify magnetic field configurations that maximize particle confinement over a prescribed time horizon. To this end, we parameterize the magnetic field profile through a neural network representation|𝐁​(z)|=𝒩​(z;θ),|\mathbf{B}(z)|=\mathcal{N}(z;\theta),

whereθ\thetadenotes the trainable parameters. The optimization problem is then formulated asmaxθ⁡𝒥​(θ)=maxθ​∑s∈{e,i}∫−LzLzρs1​D​(T,z;θ)​dz,\max_{\theta}\mathcal{J}(\theta)=\max_{\theta}\sum_{s\in\{e,i\}}\int_{-L_{z}}^{L_{z}}\rho_{s}^{1D}(T,z;\theta)\,\mathrm{d}z,(2.5)

subject to the reduced drift-kinetic system (2.1)–(2.2).

Here,ρs1​D​(T,z;θ)\rho_{s}^{1D}(T,z;\theta)denotes the longitudinal particle density (2.4), associated with the magnetic field generated by the parameter vectorθ\theta. The objective functional therefore measures the total amount of plasma retained within the computational domain at the final simulation timeTTwithin the domain of size2​Lz2L_{z}.

Throughout this work, gradients of the objective functional with respect to the neural network parameters are computed through reverse-mode automatic differentiation applied directly to the discretized numerical solver, yielding an end-to-end differentiable optimization framework.

## 3Nonlinear effects and limitations of loss-cone theory

Classical magnetic mirror confinement theory is primarily derived from single-particle dynamics under prescribed magnetic fields. Within this framework, confinement behavior is a function of the mirror ratio (the ratio between the largest and smallest magnetic field) and the associated loss-cone criterion, which predicts the fraction of particles expected to remain trapped inside the device.

However, as we demonstrate in Section3.1, the self-consistent electrostatic field generated through the Vlasov–Poisson coupling can qualitatively alter the confinement dynamics. In particular, particles with small magnetic moment, which are only weakly influenced by the magnetic mirror force, may nevertheless remain confined due to the emergence of an electrostatic trapping mechanism. Consequently, confinement can no longer be characterized solely through single-particle mirror dynamics.

The objective of this section is to examine the limitations of the classical loss-cone predictions in the nonlinear self-consistent regime. We first investigate the confinement mechanism generated by the self-consistent electric field through forward simulations in Section3.1. Then, in Section3.2, we review the classical loss-cone prediction derived from linear transport dynamics and finally compare these theoretical predictions against fully coupled numerical simulations in Section3.3to demonstrate the breakdown of the loss cone argument.

## 3.1Forward simulations and electrostatic confinement

The self-consistent electrostatic field generated through the Poisson coupling can fundamentally alter the confinement behavior of the reduced Vlasov system. In particular, we observe the emergence of confinement mechanisms that cannot be explained solely through classical magnetic mirror arguments based on single-particle trajectories and mirror ratios. To illustrate this effect, we first numerically investigate a simplified electron-only regime and subsequently consider the fully coupled multi-species system. The numerical methods used for these simulations are summarized in Section4.1.

In both simulations, we initialize the distribution functions using spatially localized Maxwellian-type profiles:fs​(0,z,v,μ)=[D​exp⁡(−(z−zc)22​σz2)]​[ms3/2​|𝐁​(z)|2​π​exp⁡(−ms​(v2+2​|𝐁​(z)|​μ)2)],f_{s}(0,z,v,\mu)=\left[D\exp\left(-\frac{(z-z_{c})^{2}}{2\sigma_{z}^{2}}\right)\right]\left[\frac{m_{s}^{3/2}|\mathbf{B}(z)|}{\sqrt{2\pi}}\exp\left(-\frac{m_{s}(v^{2}+2|\mathbf{B}(z)|\mu)}{2}\right)\right],(3.1)

whereσz2\sigma_{z}^{2}controls the spatial variance,zcz_{c}denotes the center of the plasma distribution, andDDis a normalization constant chosen so that the total initial particle density equals one. Integrating with respect tovvandμ\muyieldsρe1​D​(0,z)=ρi1​D​(0,z)=D​exp⁡(−(z−zc)22​σz2),\rho_{e}^{1D}(0,z)=\rho_{i}^{1D}(0,z)=D\exp\left(-\frac{(z-z_{c})^{2}}{2\sigma_{z}^{2}}\right)\,,

so that the initial longitudinal density profile is Gaussian. The initial densities for ions and electrons are chosen identical to ensure charge neutrality att=0t=0. The corresponding initial phase-space distributions are displayed in Figure1(b). The numerical parameters are set according to Table1in Section4.1.(a)Single-well magnetic profile(b)Initial phase-space distributions for electrons (top) and ions (bottom) generated from (3.1) at three differentμ\mu-slices.Figure 1:Initial setup for|𝐁​(z)||\mathbf{B}(z)|(left) andfs​(0,z,v,μ)f_{s}(0,z,v,\mu)(right).

We first consider a simplified electron-only regime where the ion distribution is treated as an stationary neutralizing background sofif_{i}does not evolve. This approximation is valid on timescales that are short enough such that the heavy ions do not have enough time to respond to the fast electrons. Therefore, this approximation isolates the fast electron dynamics and allows us to study the confinement mechanism generated by the self-consistent electric field. In the simulations we setme=1m_{e}=1and adopt a prototypical magnetic mirror geometry consisting of a single magnetic well, see Figure1(a).

To examine the role of the self-consistent electric field, we compare simulations with and without the electric field. Figure2displays the phase-space distribution at final timeT=25T=25for several representativeμ\mu-slices. When the self-generated electric field is turned off, the dynamics are effectively linear and particles evolve independently under the magnetic mirror force. In this case, particles with small magnetic moment experience only weak magnetic confinement, since the mirror force−μ​∂z|𝐁|-\mu\partial_{z}|\mathbf{B}|vanishes asμ→0\mu\to 0. Consequently, classical single-particle mirror theory predicts that particles with sufficiently small magnetic moment should rapidly escape the confinement region, while particles with larger magnetic moment remain localized. This can be seen the top row of Figure2.

In contrast, once the self-consistent electric field is added to the model, the confinement behavior changes significantly. Particles with vanishing magnetic moment (μ≈0\mu\approx 0), which experience negligible magnetic mirror force, nevertheless remain confined. Since magnetic confinement alone cannot explain this phenomenon, the observed trapping mechanism must originate from the nonlinear electrostatic field generated self-consistently through the Poisson equation. The electric field therefore acts as an additional confinement barrier beyond the classical magnetic mirror mechanism, see the bottom row of Figure2.Figure 2:Electron densityfe​(T=25)f_{e}(T=25)for simulating (2.1) with a stationary ion background without the presence ofEE(top) and with the presence ofEE(bottom). Clearly, the electric field provides another layer of confinement.

In Figure3we plot the evolution of electric energy in time, different time slices of electric field profile, and the mirror force for multiple choices ofμ\mu. While the electric field has different profiles at different time, the rough structure remains the same: with a basin on the left side of the origin and a hill on the right. This structure induces a force that acts in the same direction as the mirror force (i.e. increases confinement). In the right most panel of the plot, we add the black dotted line as the electric field at timet=5t=5, and it is roughly negative ofμ​∂z|𝐁​(z)|\mu\partial_{z}|\mathbf{B}(z)|forμ∼1\mu\sim 1. This means, particles with magnetic momentumμ∼1\mu\sim 1, at timet=5t=5sense roughly the same amount of force from magnetic and electric field.Figure 3:Physical quantities computed from the simulation of the electron drift-kinetic equation with a stationary ion background. From left to right: electric energyℰ​(t)\mathcal{E}(t), electric fieldsE​(t,z)E(t,z)for different timesttand, mirror forceμ​∂z|𝐁​(z)|\mu\partial_{z}|\mathbf{B}(z)|for the single-species regime.

Intuitively, the electric field provides an extra layer of confinement: fast electrons escape the computational (or physical) domain, and since the ions are stationary, a net positive charge builds up in the middle of the domain. This results in an electric field that prevents further leakage. For largerμ\mu, the electric force is negligible compared to the mirror force. However, for particles in the loss cone (smallμ\mu), the electric field is the main mechanism that prevents the escape of such particles.

We now turn to the multi-species system. To reduce computational cost while preserving the scale separation between electrons and ions, we adopt the reduced mass ratiome=1,mi=25.m_{e}=1,\qquad m_{i}=25.

Although this ratio is substantially smaller than the physical proton-electron mass ratio (mi/me≈1836m_{i}/m_{e}\approx 1836), it is sufficient to capture the distinct macroscopic timescales of the two species. We point out that reducing the mass ratio in such a manner in order to reduce computational cost is common in the literature (see, e.g.,[33]).

Due to the large mass ratio, ions take longer time to escape and saturate, as such the simulation is performed with a larger time horizon (T=80T=80). The resulting phase-space distributions at the final timeT=80T=80are shown in Figure4. The distribution of ions remains roughly unchanged with self-generated electric field turned off or on. The change is more visible for electrons, whose distribution is better confined when the self-generated electric field turned on. Such confinement is more clearly visible for smaller values ofμ\mu. Nevertheless, the confinement effect is significantly weaker in comparison to the single-species case (see Figure2). Similar to the single-species case, we also plot the electric energy as a function of time, the electric field’s evolution in time and the magnetic field for different slices ofμ\mu. Compared to Figure3, we observe that the strength of electric field in this scenario is weaker, and is only comparable to the magnetic force generated for particles with magnetic momentumμ=0.22\mu=0.22, see Figure5.Figure 4:Final particle densityfs​(T=80)f_{s}(T=80)(s∈{e,i}s\in\{e,i\}) of (2.1) without the presence ofEE(top22rows) and with the presence ofEE(bottom22rows).Figure 5:Physical quantities computed from the simulation of the coupled electron-ion drift-kinetic equations. From left to right: electric energyℰ​(t)\mathcal{E}(t), electric fieldsE​(t,z)E(t,z)for different timesttand, mirror forceμ​∂z|𝐁​(z)|\mu\partial_{z}|\mathbf{B}(z)|for the full-species regime.

## 3.2Classical loss-cone prediction

Classical magnetic mirror theory predicts particle confinement through single-particle dynamics under a prescribed magnetic field. In this framework, particles with sufficiently large parallel velocity are unable to reverse direction before reaching the boundary and therefore escape the confinement region. The corresponding set of escaping trajectories forms the so-calledloss conein velocity space.

When the self-consistent electric field is suppressed, namelyE≡0E\equiv 0, the reduced Vlasov equation (2.1) becomes a linear transport equation in which particles evolve independently under the magnetic mirror force. Consequently, the confinement properties can be deduced directly from single-particle dynamics by exploiting the conservation of the magnetic moment and kinetic energy.

LetRm:=BmaxBminR_{m}:=\frac{B_{\max}}{B_{\min}}

denote the mirror ratio, whereBmaxB_{\max}andBminB_{\min}represent the maximum and minimum magnetic field strengths, respectively. Since the magnetic momentμ=v⟂22​B\mu=\frac{v_{\perp}^{2}}{2B}is conserved along particle trajectories, we obtainμ=v⟂,max2Bmax=v⟂,min2Bmin,⇒v⟂,max2=Rm​v⟂,min2.\mu=\frac{v_{\perp,\max}^{2}}{B_{\max}}=\frac{v_{\perp,\min}^{2}}{B_{\min}}\,,\quad\Rightarrow\quad v_{\perp,\max}^{2}=R_{m}v_{\perp,\min}^{2}\,.(3.2)

Meanwhile, the conservation of kinetic energy givesv∥,max2+v⟂,max2=v∥,min2+v⟂,min2v_{\parallel,\max}^{2}+v_{\perp,\max}^{2}=v_{\parallel,\min}^{2}+v_{\perp,\min}^{2}. Substituting the magnetic moment relation into (3.2) yields:v∥,max2=v∥,min2−(Rm−1)​v⟂,min2.v_{\parallel,\max}^{2}=v_{\parallel,\min}^{2}-(R_{m}-1)v_{\perp,\min}^{2}\,.

A particle is reflected before reaching the boundary if its parallel velocity vanishes at some point along the trajectory, namelyv∥,max2=0v_{\parallel,\max}^{2}=0. Introducing the pitch angleθ\thetathroughsin⁡(θ)=v⟂|𝐯|\sin(\theta)=\frac{v_{\perp}}{|\mathbf{v}|}, the reflection criterion becomessin2⁡(θ)≥1Rm.\sin^{2}(\theta)\geq\frac{1}{R_{m}}.

Namely, particles escape when their pitch angles:θ<θc,whereθc=arcsin⁡(1Rm),\theta<\theta_{c}\,,\quad\text{where}\quad\theta_{c}=\arcsin\left(\frac{1}{\sqrt{R_{m}}}\right)\,,

whereθc\theta_{c}is termed the critical pitch angle. The corresponding region in velocity space is referred to as theloss cone. Intuitively, particles with sufficiently small pitch angle possess a dominant velocity component parallel to the magnetic field and therefore escape before magnetic reflection can occur.

When the initial velocity distribution is Maxwellian, one may explicitly compute the fraction of particles predicted to remain trapped. Integrating over the complement of the loss cone yieldsFtrapped=14​π​∫θcπ−θc∫02​πsin⁡(θ)​dϕ​dθ=cos⁡(θc)=Rm−1Rm.F_{\mathrm{trapped}}=\frac{1}{4\pi}\int_{\theta_{c}}^{\pi-\theta_{c}}\int_{0}^{2\pi}\sin(\theta)\,\mathrm{d}\phi\,\mathrm{d}\theta=\cos(\theta_{c})=\sqrt{\frac{R_{m}-1}{R_{m}}}.(3.3)

Observe that:
- •

ifRm=1R_{m}=1(no magnetic mirror), thenFtrapped=0,F_{\mathrm{trapped}}=0,

meaning all particles escape;
- •

ifRm→∞R_{m}\to\infty(perfect mirror), thenFtrapped→1,F_{\mathrm{trapped}}\to 1,

meaning all particles remain confined.

For the magnetic profile used in the simulations of Section3.1, the mirror ratio is set to beRm=10R_{m}=10, thus using the arguments above one predictsFtrapped=Rm−1Rm≈0.95.F_{\mathrm{trapped}}=\sqrt{\frac{R_{m}-1}{R_{m}}}\approx 0.95.

In addition to predicting the fraction of trapped particles, the classical single-particle picture also provides estimates for the characteristic escape times of different species. Since parallel transport is dominated by the streaming term in (2.1), particles with larger parallel velocity escape more rapidly from the computational domain. Using the same numerical setup as in Section3.1, we have[−Lz,Lz]=[−2​π,2​π][-L_{z},L_{z}]=[-2\pi,2\pi], and the characteristic transit time scales astesc∼Lz|v|t_{\mathrm{esc}}\sim\frac{L_{z}}{|v|}.
- •

For electrons with maximal parallel velocity|ve|=4|v_{e}|=4, the earliest escape occurs at approximatelytesc(e)=2​π4=π2≈1.57t_{\mathrm{esc}}^{(e)}=\frac{2\pi}{4}=\frac{\pi}{2}\approx 1.57.
- •

For ions, the larger mass reduces the characteristic thermal velocity by a factormime=5\sqrt{\frac{m_{i}}{m_{e}}}=5, yielding substantially larger escape times. We set|vi|=4/mi/me|v_{i}|=4/\sqrt{m_{i}/m_{e}}and the fastest ions do not reach the boundary until approximatelytesc(i)=5​π2≈7.85t_{\mathrm{esc}}^{(i)}=\frac{5\pi}{2}\approx 7.85.

Since ions are much heavier and thus slower, they escape at a much larger time horizon, and the mass ratio dictates the pronounced difference of escape dynamics between electrons and ions.

Observe that the classical loss-cone prediction depends solely on the magnetic geometry through the mirror ratioRmR_{m}. In particular, the derivation neglects modifications of the effective particle dynamics induced by self-consistent electrostatic fields and collective plasma interactions.

## 3.3Breakdown of the loss cone argument

The loss-cone criterion reviewed in the previous subsection predicts confinement is solely determined by the mirror ratioRmR_{m}and therefore attributes trapping entirely to magnetic reflection. However, the simulations of Section3.1suggest the existence of an additional confinement mechanism generated by the self-consistent electrostatic field and that its effect depends on many factors, including whether the ions can be regarded as stationary, and the mass ratio between ions and electrons. In general, particles with small magnetic moment, which experience only weak magnetic mirror forces, are more affected by the self-consistent electric field. We now investigate quantitatively how this nonlinear effect modifies the predictions of classical loss-cone theory.

For the electron-only system, Figure6reports the retained particle massMe​(t)=∫−LzLzρe1​D​(t,z)​dz.M_{e}(t)=\int_{-L_{z}}^{L_{z}}\rho_{e}^{1D}(t,z)\mathrm{d}z.

When the electric field is suppressed, the dynamics reduce to the linear transport regime discussed in Section3.2. In this case, the retained mass converges to approximately94%94\%, in agreement with the classical loss-cone prediction (3.3) for a mirror ratioRm=10R_{m}=10. The earliest particle loss is predicted at approximatelyt≈1.57t\approx 1.57, and this agrees well with the simulation also, see red dash line in Figure6.

Once the self-consistent electric field is restored, the confinement behavior changes significantly. The retained particle mass now saturates above97%97\%, indicating that particles predicted to escape under purely magnetic confinement remain trapped in the nonlinear regime. This observation is consistent with the phase-space distributions shown in Figure2, where particles withμ≈0\mu\approx 0remain localized despite experiencing negligible magnetic mirror force. The additional confinement therefore originates from the electrostatic potential generated self-consistently through the Poisson equation, and it serves as a second layer of confinement. This is a pure nonlinear and collective mechanism.Figure 6:Retained electron mass as a function of time for simulations with and without the self-consistent electric field when ions are stationary. The nonlinear electrostatic coupling increases the amount of confined plasma.

We next consider the fully coupled electron-ion system. The corresponding density evolution is reported in Figure7. Once again, the initial escape time is expected to be7.857.85for ions and is plotted as the red dashed line, and this agrees with the simulation well. But we also observe four distinct phases.
- •

Initial Electron Escape (roughlyt<7.85t<7.85):Highly mobile electrons rapidly exit. This phase is when the heavier ions, due to inertia, remain confined and the dynamics of electron is very similar to that of the single-species situation, see comparison with Figure6.
- •

Ambipolar Confinement (roughly7.85<t<157.85<t<15):Electron depletion generates a net positive charge. The resulting electric field accelerates ion expulsion while keeping electrons confined.
- •

Field Reversal and Secondary Escape (15<t<5015<t<50):Continuous ion loss alters the self-consistent field, triggering a secondary wave of electron expulsion. At aboutt=50t=50, ion loss is stronger than electron loss, generating a net negative charge, and resulting in a crossover of confining effect with electric field turned on and off.
- •

Equilibrium (t>50t>50):The system relaxes into a quasi-steady state with minimal subsequent mass loss. Net negative charge confines ions, and combined effect of electric and magnetic field confines electrons.

This four phase dynamics cannot be drawn from classical loss-cone argument, and the disparity between having self-generated electric field switched on and off is clearly visible comparing the orange and blue lines. Overall, the fraction of both electrons and ions that are confined is significantly larger with the electric field switched on.Figure 7:Retained particle mass for the fully coupled electron-ion system. Left: electron mass evolution. Right: ion mass evolution. The coupled system exhibits both electrostatic confinement and a pronounced separation between electron and ion escape times.

Taken together, these results demonstrate that confinement cannot be characterized solely through the mirror ratio. While the classical loss-cone argument captures important aspects of magnetic reflection, the self-consistent electrostatic field introduces additional confinement mechanisms that substantially modify both the amount of retained plasma and the temporal evolution of particle escape. Consequently, confinement performance depends on the full nonlinear dynamics.

## 4Numerical Experiments

So far, we have numerically confirmed that the classical loss-cone theory fails to capture the nonlinear additional confinement mechanisms induced by the electrostatic field. Therefore, the confinement should be also a function of the geometry of external field and not only the mirror ratioRmR_{m}.

In this section, we explore how the geometry affects the confinement. Thus, we investigate the PDE-constrained optimization problem introduced in Section2aiming at finding optimal confinement configurations. This section first summarizes the computational setup and optimization framework, followed by numerical studies of the resulting optimal magnetic mirror configurations. To facilitate verification and further development of this approach, we have made the complete source code, simulation parameters, and optimization configurations publicly available111Please seehttps://github.com/maguerrap/vp-mirror_modelfor the collection of all code and numerical results related to this paper..

The simulation parameters used throughout this section are summarized in Table1.Parameter / DomainValues and SetupMass and chargesme=1m_{e}=1,qe=−1q_{e}=-1,mi=25m_{i}=25,qi=1q_{i}=1Magnetic mirrorBmin=1B_{\min}=1,Bmax=10⟹Rm=10B_{\max}=10\implies R_{m}=10Temporal domaint∈[0,T]t\in[0,T], (T=25T=25single-species,T=80T=80multi-species)Spatial domainz∈[−Lz,Lz]z\in[-L_{z},L_{z}]withLz=2​πL_{z}=2\piVelocity domainve∈[−v0,v0]v_{e}\in[-v_{0},v_{0}](v0=4v_{0}=4), andvi∈[−v0/mi,v0/mi]v_{i}\in[-v_{0}/\sqrt{m_{i}},v_{0}/\sqrt{m_{i}}]Magnetic momentμ∈[0,μ0]\mu\in[0,\mu_{0}], bounded by tolerancee−μ0​Bmax=10−12e^{-\mu_{0}B_{\max}}=10^{-12}Table 1:Parameters and domain setup for the numerical simulations.

## 4.1Computational setup

The reduced drift-kinetic system is discretized on a uniform phase-space grid in(z,v,μ)(z,v,\mu)and advanced in time using Strang operator splitting[17]. The resulting transport equations are solved using a conservative semi-Lagrangian method. Since the numerical discretization is not the focus of this work, implementation details are given in AppendixA.

The principal computational challenge lies in the optimization of the magnetic field geometry. Following the formulation of Section2, we seek magnetic field profiles that maximize the confinement objective (2.5). To this end, the magnetic field is parameterized through a neural network representation|𝐁​(z)|=𝒩​(z;θ),|\mathbf{B}(z)|=\mathcal{N}(z;\theta),

whereθ\thetadenotes the trainable network parameters. A schematic of the complete neural-network architecture is provided in AppendixB; see Figure14.

Several structural constraints are imposed on the admissible magnetic field profiles. First, the magnetic field is required to remain symmetric with respect to the center of the device. This symmetry is enforced by using the squared distance(z−zc)2(z-z_{c})^{2}as the network input. Second, all admissible fields are constrained to share the same mirror ratioRm=BmaxBmin=10.R_{m}=\frac{B_{\max}}{B_{\min}}=10.

To enforce this constraint, the raw network output is evaluated on the spatial grid, normalized, and scaled to the interval1≤|𝐁​(z)|≤101\leq|\mathbf{B}(z)|\leq 10.

This normalization plays an important role in the interpretation of the optimization results. Since all candidate magnetic fields possess the same mirror ratio, any improvement in confinement cannot be attributed to a stronger magnetic mirrors. Instead, performance gains must arise from the detailed spatial configuration of the magnetic field and its interaction with the drift-kinetic model.

The optimization problem is solved using gradient-based methods. Within each iteration, we differentiate directly through the full numerical pipeline using reverse-mode automatic differentiation.

Consequently, the optimization procedure can efficiently exploit gradient information from the underlying kinetic dynamics, enabling end-to-end PDE-constrained optimization of magnetic mirror geometries. The overall optimization procedure is summarized in Algorithm1.Algorithm 1Differentiable Optimization of the Magnetic Mirror Profile1:Initial distributionfs​(0,z,v,μ)f_{s}(0,z,v,\mu)fors∈{e,i}s\in\{e,i\}, initial network weightsθ0\theta_{0}, learning rateα\alpha, total iterationsNitersN_{\text{iters}}, simulation end timeTT, time stepΔ​t\Delta t, grid{zi,vj,μk}i,j,k=0N−1\{z_{i},v_{j},\mu_{k}\}_{i,j,k=0}^{N-1}.2:Optimized network weightsθ∗\theta^{*}3:θ←θ0\theta\leftarrow\theta_{0}4:foriteration=1,2,…,Niters=1,2,\dots,N_{\text{iters}}do5:Evaluate MLP to obtain spatial magnetic field|𝐁​(z;θ)||\mathbf{B}(z;\theta)|6:Initialize statesfs←fs​(0,z,v,μ)f_{s}\leftarrow f_{s}(0,z,v,\mu)fors∈{e,i}s\in\{e,i\}according to (3.1)7:fe​(T),fi​(T)←PDE_Solver​({{zi,vj(s),μk}i,j,k=0N−1,fs}s∈{e,i},Δ​t,⌊TΔ​t⌋,|𝐁​(z;θ)|)f_{e}(T),f_{i}(T)\leftarrow\texttt{PDE\_Solver}\left(\{\{z_{i},v_{j}^{(s)},\mu_{k}\}_{i,j,k=0}^{N-1},f_{s}\}_{s\in\{e,i\}},\Delta t,\left\lfloor\frac{T}{\Delta t}\right\rfloor,|\mathbf{B}(z;\theta)|\right)⊳\trianglerightSee Algorithm28:Compute final densityρs1​D​(T,z;θ)=∬fs​(T,z,v,μ)​dv​dμ\rho_{s}^{1D}(T,z;\theta)=\iint f_{s}(T,z,v,\mu)\,\mathrm{d}v\,\mathrm{d}\mufors∈{e,i}s\in\{e,i\}9:Evaluate objective𝒥​(θ)\mathcal{J}(\theta)10:Compute gradients∇θ𝒥​(θ)\nabla_{\theta}\mathcal{J}(\theta)via reverse-mode automatic differentiation11:θ←Adam​(θ,∇θ𝒥​(θ),α)\theta\leftarrow\texttt{Adam}(\theta,\nabla_{\theta}\mathcal{J}(\theta),\alpha)⊳\trianglerightUpdate network parameters12:endfor13:returnθ\theta

## 4.2Numerical results

We present our numerical results for both electron-only system and the ion-electron coupled system, summarized in the following subsections respectively. For each case, we present our found optimal magnetic field, and provide physical justification.

## 4.2.1Electron-only regime

We first investigate the electron-only regime, where ions are treated as a stationary neutralizing background. This setting isolates the interaction between magnetic confinement and the nonlinear electrostatic trapping mechanism identified in Section3.1.

Figure8summarizes the optimization results. Surprisingly, we observe that the optimized field differs qualitatively from the classical magnetic mirror configuration. Rather than forming a single magnetic well with peaks located near the boundaries, the optimizer consistently finds a field profile with a pronounced maximum at the center of the device and two symmetric secondary wells roughly between the middle and the boundaries.

To confirm this is not a consequence of a particular initialization, in AppendixCwe test and report the robustness of the optimization procedure where we repeat the optimization process using100100independent random initializations of the neural network parameters and report the resulting mean magnetic field profile together with a95%95\%confidence interval. The resulting confidence bands remain narrow throughout the domain and consistently exhibit a pronounced magnetic peak at the center.Figure 8:Optimization for the electron drift-kinetic equation with stationary ions. Top-left: initial and optimized magnetic field profiles. Top-right: retained particles mass (optimalθ∗\theta^{\ast}vs. initial guessθ0\theta_{0}) as a function of time. Bottom-left: Electric fields for optimal configuration at four time slices. Bottom-right: Different time-slices forρ1​D\rho^{1D}.

Though counter-intuitive, the observed better performance of the double-well field can be explained as follows. There are two layers of this explanation. Firstly, we notice there is a strong magnetic field in the center of the domain. Since the source term in the Poisson equation (2.2) scales with|𝐁​(z)||\mathbf{B}(z)|, such strong magnetic field also induces a strong electric field in the center of the domain. This is particularly visible if we compare bottom-left of Figure8with middle of Figure3, the electric field generated by a single-well field. Physically, since the magnetic field is stronger in the domain center, it pushes the magnetic field lines to be closer, and the cross section of the plasma perpendicular to the magnetic field lines shrinks. This drives up the electric field with the same net charge and accelerates particles with stronger force.

Secondly, we also notice the two wells are located symmetrically with respect to the origin. They are also important, and they are in charge of providing confinement to the majority of particles that initially escape from the domain center. These wells create the net positive charge required for the buildup of the electric field. See distribution of particles in Figure10. Particles with largerμ\muare pushed and confined in the regions of the two wells.Figure 9:Initial phase-space distributions generated from the optimized double well magnetic fields for the drift-kinetic electron simulation with stationary ions.Figure 10:Electron phase-space distributions at final timeT=25T=25when ions are stationary equipped with the optimized double well magnetic field. The distributions are shown for fourμ\mu-slices.

## 4.2.2Multi-species confinement optimization

We now consider the fully coupled electron-ion system. Unlike the electron-only regime, the optimization objective must simultaneously account for the confinement of both species and therefore incorporates the complete nonlinear multiscale dynamics.

The resulting optimal configurations are shown in Figure11. The most striking observation is that the preferred magnetic topology changes completely once ion dynamics are introduced. In contrast to the centrally-peaked fields obtained previously, the optimizer now consistently recovers a geometry that closely resembles the classical magnetic mirror configuration: strong magnetic peaks near the boundaries and a broad magnetic well in the center.Figure 11:Optimization results in the fully coupled electron-ion system. Top-left: initial and optimized magnetic field profiles. Top-right: retained particles mass (optimalθ⋆\theta_{\star}vs. initial guessθ0\theta_{0}) as a function of time. Bottom-left: Electric fields for optimal configuration. Bottom-right: Different time-slices forρe,i1​D\rho_{e,i}^{1D}.

As in the single-species case, optimization trajectories originating from different initializations converge to nearly identical magnetic profiles. The robustness is even more pronounced than in the electron-only regime, suggesting the existence of a strongly preferred confinement topology in the electron-ion case.

We perform the same uncertainty quantification study for the electron-ion system. As shown in AppendixC, the variance among optimized profiles is even smaller than in the electron-only regime. The optimizer consistently converges toward a boundary-peaked magnetic mirror configuration, indicating an even stronger preference for this topology once ion dynamics are incorporated.

The physical mechanism underlying this different optimization profile transition differs substantially from the electron-only case. Once ion dynamics are included, confinement is no longer dominated by the low-μ\muelectron population alone. Instead, long-time retention of both species becomes the determining factor. Under these conditions, the optimizer naturally favors a broad central confinement region bounded by strong magnetic mirrors, thereby recovering a configuration reminiscent of traditional mirror devices.

Figures12and13further illustrate this behavior. The optimized field concentrates both species near the center of the device while maintaining strong reflection barriers at the boundaries. As a consequence, only particles with magnetic moments extremely close to zero escape during the simulation horizon.(a)fs=fef_{s}=f_{e}(b)fs=fif_{s}=f_{i}Figure 12:Initial phase-space distributions for the optimized multi-species configuration.(a)fs=fef_{s}=f_{e}(b)fs=fif_{s}=f_{i}Figure 13:Phase-space distributions atT=80T=80for the optimized multi-species configuration.

Taken together, these results reveal two distinct confinement strategies discovered through optimization.
- •

In the electron-only regime, the optimizer exploits nonlinear electrostatic trapping and therefore favors centrally-peaked magnetic fields that preserve the dominant low-μ\mupopulation.
- •

In the fully coupled system, long-time confinement of both species becomes paramount, leading the optimizer to recover a configuration closely resembling the classical magnetic mirror.

The transition between these two optimal topologies highlights the fundamentally different confinement mechanisms operating in the two regimes.

## Acknowledgment

MG and QL acknowledge the support by ONR Award AWD-100997 and NSF grant DMS-2308440. QL further acknowledges Vilas Associate Award. The work was initiated when MG, QL and LE were visiting Simons Laufer Mathematical Sciences Institute in Berkeley, California, during the Fall 2025 semester to participate in the semester program on “Kinetic Theory: Novel Statistical, Stochastic and Analytical Methods”. This research was funded in part by the Austrian Science Fund (FWF)https://doi.org/10.55776/PAT2937525.

## References
- [1]C. G. Albert, S. V. Kasilov, and W. Kernbichler(2020)Accelerated methods for direct computation of fusion alpha particle losses within, stellarator optimization.Journal of Plasma Physics86(2),pp. 815860201.Cited by:§1.1.
- [2]G. Albi, G. Dimarco, F. Ferrarese, and L. Pareschi(2025)Instantaneous control strategies for magnetically confined fusion plasma.Journal of Computational Physics527,pp. 113804.External Links:ISSN 0021-9991,Document,LinkCited by:§1.1.
- [3]G. Albi, G. Dimarco, F. Ferrarese, and L. Pareschi(2025)Robust feedback control of collisional plasma dynamics in presence of uncertainties.Journal of Computational Physics,pp. 114512.Cited by:§1.1.
- [4]J. Bartsch and A. Borzi(2024)On the stabilization of a kinetic model by feedback-like control fields in a monte carlo framework.Kinetic and Related Models17(6),pp. 892–913.External Links:ISSN 1937-5093,DocumentCited by:§1.1.
- [5]J. Bartsch, P. Knopf, S. Scheurer, and J. Weber(2024)Controlling a vlasov–poisson plasma by a particle-in-cell method based on a monte carlo framework.SIAM Journal on Control and Optimization62(4),pp. 1977–2011.External Links:Document,Link,https://doi.org/10.1137/23M1563852Cited by:§1.1.
- [6]A. J. Brizard and T. S. Hahm(2007)Foundations of nonlinear gyrokinetic theory.Review of Modern Physics79,pp. 421–468.External Links:Document,LinkCited by:§1.1.
- [7]J. R. Cary and A. J. Brizard(2009)Hamiltonian theory of guiding-center motion.Review of Modern Physics81,pp. 693–738.External Links:Document,LinkCited by:§1.1,§1.
- [8]F. F. Chen(1984)Introduction to plasma physics and controlled fusion.Springer,New York, NY.External Links:Document,ISBN 9783319223087Cited by:§1.
- [9]N. Crouseilles, L. Einkemmer, Q. Li, U. Shumlak, and Y. Yue(2025)Control of kinetic plasma instabilities by laser fields.arXiv:2509.23080, to appear in Physics of Plasmas.Cited by:§1.1.
- [10]N. Crouseilles, H. Liu, and Y. Yue(2026)Semi-lagrangian sav method for vlasov-maxwell equations.Journal of Computational Physics549,pp. 114606.External Links:ISSN 0021-9991,Document,LinkCited by:§1.1.
- [11]N. Crouseilles, M. Mehrenberger, and E. Sonnendrücker(2010)Conservative semi-lagrangian schemes for vlasov equations.Journal of Computational Physics229(6),pp. 1927–1953.External Links:ISSN 0021-9991,Document,LinkCited by:§1.1.
- [12]J. Degrave, F. Felici, J. Buchli, M. Neunert, B. Tracey, F. Carpanese, T. Ewalds, R. Hafner, A. Abdolmaleki, D. de las Casas, C. Donner, L. Fritz, C. Galperti, A. Huber, J. Keeling, M. Tsimpoukelli, J. Kay, A. Merle, J. Moret, S. Noury, F. Pesamosca, D. Pfau, O. Sauter, C. Sommariva, S. Coda, B. Duval, A. Fasoli, P. Kohli, K. Kavukcuoglu, D. Hassabis, and M. Riedmiller(2022)Magnetic control of tokamak plasmas through deep reinforcement learning.Nature602,pp. 414–419.External Links:DocumentCited by:§1.1.
- [13]L. Einkemmer, Q. Li, C. Mouhot, and Y. Yue(2025)Control of instability in a Vlasov-Poisson system through an external electric field.Journal of Computational Physics530,pp. 113904.External Links:ISSN 0021-9991,Document,LinkCited by:§1.1.
- [14]L. Einkemmer, Q. Li, L. Wang, and Y. Yunan(2024)Suppressing instability in a Vlasov–Poisson system by an external electric field through constrained optimization.Journal of Computational Physics498,pp. 112662.External Links:ISSN 0021-9991,Document,LinkCited by:§1.1.
- [15]L. Einkemmer and A. Moriggl(2024)A semi-Lagrangian discontinuous Galerkin method for drift-kinetic simulations on GPUs.SIAM Journal on Scientific Computing46(2),pp. B33–B55.Cited by:§1.1.
- [16]L. Einkemmer and A. Moriggl(2025)Kinetic scrape off layer simulations with semi-Lagrangian discontinuous Galerkin schemes.Computer Physics Communications,pp. 109775.Cited by:§1.1.
- [17]L. Einkemmer and A. Ostermann(2014)Convergence analysis of a discontinuous galerkin/strang splitting approximation for the vlasov–poisson equations.SIAM Journal on Numerical Analysis52(2),pp. 757–778.External Links:DocumentCited by:§4.1.
- [18]L. Einkemmer(2024)Stabilization of beam heated plasmas by beam modulation.Physics of Plasmas31(12).Cited by:§1.1.
- [19]F. Filbet, E. Sonnendrücker, and P. Bertrand(2001)Conservative numerical schemes for the vlasov equation.Journal of Computational Physics172(1),pp. 166–187.External Links:ISSN 0021-9991,Document,LinkCited by:§1.1.
- [20]M. Guerra, Q. Li, Y. Yue, and L. Zepeda-Núñez(2026)What metric to optimize for suppressing instability in a vlasov-poisson system?.Journal of Computational Physics564,pp. 115169.External Links:ISSN 0021-9991,Document,LinkCited by:§1.1.
- [21]R. D. Hazeltine and J. D. Meiss(2003)Plasma confinement.Courier Corporation.External Links:ISBN 9780486432427Cited by:§1.
- [22]P. Jiménez, L. Chacón, and M. Merino(2024)An implicit, conservative electrostatic particle-in-cell algorithm for paraxial magnetic nozzles.Journal of Computational Physics502,pp. 112826.External Links:ISSN 0021-9991,Document,LinkCited by:§1,§2.2.
- [23]A. S. Joglekar, A. G. R. Thomas, A. L. Milder, K. G. Miller, J. P. Palastro, and D. H. Froula(2026)Differentiable programming for plasma physics: from diagnostics to discovery and design.External Links:2603.11231,LinkCited by:§1.1.
- [24]E.J. Kolmes, I.E. Ochs, and N.J. Fisch(2024)Loss-cone stabilization in rotating mirrors: thresholds and thermodynamics.Journal of Plasma Physics90(2).External Links:DocumentCited by:§1.
- [25]Q. Li, L. Wang, and Y. Yang(2023)Monte carlo gradient in optimization constrained by radiative transport equation.SIAM Journal on Numerical Analysis61(6),pp. 2744–2774.External Links:Document,Link,https://doi.org/10.1137/22M1524515Cited by:§1.1.
- [26]J. Lu, L. Wang, and J. Calder(2025)Dynamical feedback control with operator learning for the vlasov-poisson system.arXiv preprint arXiv:2509.23063.Cited by:§1.1.
- [27]V.P. Pastukhov(1974)Collisional losses of electrons from an adiabatic trap in a plasma with a positive potential.Nuclear Fusion14(1),pp. 3–6.External Links:DocumentCited by:§1.1.
- [28]R.F. Post(1987)The magnetic mirror approach to fusion.Nuclear Fusion27(10),pp. 1579.External Links:Document,LinkCited by:§1.1,§1.
- [29]Realta fusion.Note:https://realtafusion.com/Accessed: 2026-05-21Cited by:§1.
- [30]E. Sonnendrücker, J. Roche, P. Bertrand, and A. Ghizzo(1999)The semi-Lagrangian method for the numerical resolution of the vlasov equation.Journal of Computational Physics149(2),pp. 201–220.External Links:Document,LinkCited by:§1.1,§1.
- [31]Z. Tang, E. Lovbak, J. Koellermeier, and G. SamaeyNumerical analysis of fluid estimation for source terms in neutral particle simulations.Contributions to Plasma Physicsn/a(n/a),pp. e70129.External Links:Document,Link,https://onlinelibrary.wiley.com/doi/pdf/10.1002/ctpp.70129Cited by:§1.1.
- [32]M. Tyushev, A. Smolyakov, A. Sabo, R. Groenewald, A. Necas, and P. Yushmanov(2025)Drift-kinetic PIC simulations of plasma flow and energy transport in the magnetic mirror configuration.Physics of Plasmas32(3).Cited by:§1,§2.2.
- [33]G. Vogman and J. Hammer(2024)Complete quasilinear model for the acceleration-driven lower hybrid drift instability and a computational assessment of its validity.Physical Review E110(2),pp. 025201.Cited by:§3.1.
- [34]X. Wei, H. Huang, H. Chen, H. Zhu, Z. Bai, S. Williams, and Z. Lin(2026)Low-dimensional geometry learning for turbulence prediction in optimized stellarators.External Links:2603.17366,LinkCited by:§1.1.

## Appendix ANumerical Scheme

In this section, we explain in detail the numerical scheme employed to solve (2.1). We recall that our phase-space is(z,v(s),μ)(z,v^{(s)},\mu)for speciess∈{e,i}s\in\{e,i\}which gets discretized into an isotropic grid{zi,vj(s),μk}i,j,k=0N\{z_{i},v_{j}^{(s)},\mu_{k}\}_{i,j,k=0}^{N}with uniform widthsΔ​z\Delta z,Δ​v(s)\Delta v^{(s)}andΔ​μ\Delta\mu. Also, the cell boundaries are denoted byzi±1/2z_{i\pm 1/2}and the time domain is discretized as{tn}n=0Nt\{t^{n}\}_{n=0}^{N_{t}}.

## A.1Finite Volume Scheme

Let𝖿sn​(zi,vj(s),μk)≈fs​(tn,z,v(s),μ)\mathsf{f}_{s}^{n}(z_{i},v_{j}^{(s)},\mu_{k})\approx f_{s}(t^{n},z,v^{(s)},\mu)be our numerical approximation now represents the cell-averaged distribution function. A single full time step proceeds in four distinct stages.

First, we perform a half-step spatial advection for both species. We define the discrete spatial primitive function (cumulative mass) evaluated at the cell edges as:𝖥s,z​(zi+1/2,vj(s),μk)=∑m=0i𝖿sn​(zm,vj(s),μk)​Δ​z,\mathsf{F}_{s,z}(z_{i+1/2},v_{j}^{(s)},\mu_{k})=\sum_{m=0}^{i}\mathsf{f}_{s}^{n}(z_{m},v_{j}^{(s)},\mu_{k})\Delta z\,,

where𝖥s,z​(z−1/2)=0\mathsf{F}_{s,z}(z_{-1/2})=0. We trace the cell boundaries backward along the characteristics:zi±1/2∗=zi±1/2−vj(s)​Δ​t/2.z_{i\pm 1/2}^{\ast}=z_{i\pm 1/2}-v_{j}^{(s)}\Delta t/2\,.

The intermediate distribution is then updated by interpolating the primitive function at the advected edges and computing the flux difference:𝖿s∗​(zi,vj(s),μk)=1Δ​z​[𝒫​(𝖥s,z)​(zi+1/2∗)−𝒫​(𝖥s,z)​(zi−1/2∗)],\mathsf{f}_{s}^{\ast}(z_{i},v_{j}^{(s)},\mu_{k})=\frac{1}{\Delta z}\left[\mathcal{P}(\mathsf{F}_{s,z})(z_{i+1/2}^{\ast})-\mathcal{P}(\mathsf{F}_{s,z})(z_{i-1/2}^{\ast})\right]\,,

where𝒫\mathcal{P}represents a shape-preserving Piecewise Cubic Hermite Interpolating Polynomial (PCHIP) interpolation to maintain strict monotonicity. To naturally enforce zero-inflow and open outflow boundaries,𝒫​(𝖥s,z)\mathcal{P}(\mathsf{F}_{s,z})is strictly clamped to the interval[0,𝖥s,z​(zN−1/2)][0,\mathsf{F}_{s,z}(z_{N-1/2})].

Next, we compute the macroscopic 1D densitiesρe1​D\rho_{e}^{1D}andρi1​D\rho_{i}^{1D}using the intermediate distributions𝖿e∗\mathsf{f}_{e}^{\ast}and𝖿i∗\mathsf{f}_{i}^{\ast}. We use these to solve the Poisson system (2.2) for the electrostatic potentialϕ\phi. We employ a 4th-order finite difference scheme with homogeneous Dirichlet boundary conditions (which we detail in SectionA.2below). Using these approximations, we evaluate the electric field at the current time step:𝖤in+12≈−∂zϕ​(tn+12,zi)\mathsf{E}_{i}^{n+\frac{1}{2}}\approx-\partial_{z}\phi(t^{n+\frac{1}{2}},z_{i}). We then perform a full-step velocity advection for each species using the same conservative framework. The local characteristic acceleration is computed as𝖺i,k,sn+12=qsms​𝖤in+12−μk​∂z|𝐁​(zi)|\mathsf{a}_{i,k,s}^{n+\frac{1}{2}}=\frac{q_{s}}{m_{s}}\mathsf{E}_{i}^{n+\frac{1}{2}}-\mu_{k}\partial_{z}|\mathbf{B}(z_{i})|. We trace the velocity boundaries backward:vj±1/2(s)⁣∗=vj±1/2(s)−𝖺i,k,sn+12​Δ​t.v_{j\pm 1/2}^{(s)\ast}=v_{j\pm 1/2}^{(s)}-\mathsf{a}_{i,k,s}^{n+\frac{1}{2}}\Delta t\,.

Defining the velocity primitive function𝖥s,v\mathsf{F}_{s,v}generated from𝖿s∗\mathsf{f}_{s}^{\ast}as,𝖥s,v​(zi,vj+12(s),μk)=∑m=0j𝖿s∗​(zi,vm(s),μk)​Δ​v(s)\mathsf{F}_{s,v}(z_{i},v_{j+\frac{1}{2}}^{(s)},\mu_{k})=\sum_{m=0}^{j}\mathsf{f}_{s}^{\ast}(z_{i},v_{m}^{(s)},\mu_{k})\Delta v^{(s)}

then, the full-step velocity advection is computed as:𝖿s∗∗​(zi,vj(s),μk)=1Δ​v(s)​[𝒫​(𝖥s,v)​(vj+1/2(s)⁣∗)−𝒫​(𝖥s,v)​(vj−1/2(s)⁣∗)].\mathsf{f}_{s}^{\ast\ast}(z_{i},v_{j}^{(s)},\mu_{k})=\frac{1}{\Delta v^{(s)}}\left[\mathcal{P}(\mathsf{F}_{s,v})(v_{j+1/2}^{(s)\ast})-\mathcal{P}(\mathsf{F}_{s,v})(v_{j-1/2}^{(s)\ast})\right]\,.

Finally, we compute the remaining half-step spatial advection on𝖿s∗∗\mathsf{f}_{s}^{\ast\ast}exactly as before to complete the time step,𝖥s,z​(zi+12,vj(s),μk)=∑m=0i𝖿s∗∗​(zm,vj(s),μk)​Δ​z,\mathsf{F}_{s,z}(z_{i+\frac{1}{2}},v_{j}^{(s)},\mu_{k})=\sum_{m=0}^{i}\mathsf{f}_{s}^{\ast\ast}(z_{m},v_{j}^{(s)},\mu_{k})\Delta z\,,

and obtain𝖿sn+1\mathsf{f}_{s}^{n+1},𝖿sn+1​(zi,vj(s),μk)=1Δ​z​[𝒫​(𝖥s,z)​(zi+1/2∗)−𝒫​(𝖥s,z)​(zi−1/2∗)].\mathsf{f}_{s}^{n+1}(z_{i},v_{j}^{(s)},\mu_{k})=\frac{1}{\Delta z}\left[\mathcal{P}(\mathsf{F}_{s,z})(z_{i+1/2}^{\ast})-\mathcal{P}(\mathsf{F}_{s,z})(z_{i-1/2}^{\ast})\right]\,.

We summarize the generalized numerical integration scheme in Algorithm2.Algorithm 2Multi-Species Conservative Semi-LagrangianPDE_Solver1:Input:Centers and edges of grid{zi,vj(s),μk}i,j,k=0N−1\{z_{i},v_{j}^{(s)},\mu_{k}\}_{i,j,k=0}^{N-1}fors∈{e,i}s\in\{e,i\}, initial distributions𝖿s0\mathsf{f}_{s}^{0}, time stepΔ​t\Delta t, final stepsNtN_{t}, magnetic field|𝐁​(z)||\mathbf{B}(z)|.2:Output:Final distributions𝖿sNt​(z,v,μ)\mathsf{f}_{s}^{N_{t}}(z,v,\mu)3:t←0t\leftarrow 04:forn=0,…,Nt−1n=0,...,N_{t}-1do5:fors∈{e,i}s\in\{e,i\}do6:Compute cumulative mass𝖥s,z\mathsf{F}_{s,z}from𝖿sn\mathsf{f}_{s}^{n}⊳\trianglerightHalf-stepzzadvection7:zi±1/2∗←zi±1/2−vj(s)​Δ​t/2z_{i\pm 1/2}^{\ast}\leftarrow z_{i\pm 1/2}-v_{j}^{(s)}\Delta t/28:𝖿s∗​(zi,vj,μk)←1Δ​z​[𝒫​(𝖥s,z)​(zi+1/2∗)−𝒫​(𝖥s,z)​(zi−1/2∗)]∀i,j,k\mathsf{f}_{s}^{\ast}(z_{i},v_{j},\mu_{k})\leftarrow\frac{1}{\Delta z}[\mathcal{P}(\mathsf{F}_{s,z})(z_{i+1/2}^{\ast})-\mathcal{P}(\mathsf{F}_{s,z})(z_{i-1/2}^{\ast})]\quad\forall i,j,k9:endfor10:Compute net charge density from𝖿e∗\mathsf{f}_{e}^{\ast}and𝖿i∗\mathsf{f}_{i}^{\ast}11:Solve (2.2) via finite differences to obtain𝖤in+12≈E​(t+Δ​t/2,zi)∀i\mathsf{E}_{i}^{n+\frac{1}{2}}\approx E(t+\Delta t/2,z_{i})\quad\forall i⊳\trianglerightSelf-consistent field12:fors∈{e,i}s\in\{e,i\}do13:Compute cumulative mass𝖥s,v\mathsf{F}_{s,v}from𝖿s∗\mathsf{f}_{s}^{\ast}⊳\trianglerightFull-stepvvadvection14:𝖺i,k,sn+12←qsms​𝖤in+12−μk​∂z|𝐁​(zi)|\mathsf{a}_{i,k,s}^{n+\frac{1}{2}}\leftarrow\frac{q_{s}}{m_{s}}\mathsf{E}_{i}^{n+\frac{1}{2}}-\mu_{k}\partial_{z}|\mathbf{B}(z_{i})|15:vj±1/2(s)⁣∗←vj±1/2(s)−𝖺i,k,sn+12​Δ​tv_{j\pm 1/2}^{(s)\ast}\leftarrow v_{j\pm 1/2}^{(s)}-\mathsf{a}_{i,k,s}^{n+\frac{1}{2}}\Delta t16:𝖿s∗∗​(zi,vj(s),μk)←1Δ​v​[𝒫​(𝖥s,v)​(vj+1/2(s)⁣∗)−𝒫​(𝖥s,v)​(vj−1/2(s)⁣∗)]∀i,j,k\mathsf{f}_{s}^{\ast\ast}(z_{i},v_{j}^{(s)},\mu_{k})\leftarrow\frac{1}{\Delta v}[\mathcal{P}(\mathsf{F}_{s,v})(v_{j+1/2}^{(s)\ast})-\mathcal{P}(\mathsf{F}_{s,v})(v_{j-1/2}^{(s)\ast})]\quad\forall i,j,k17:Compute cumulative massFs,zF_{s,z}from𝖿s∗∗\mathsf{f}_{s}^{\ast\ast}⊳\trianglerightHalf-stepzzadvection18:zi±1/2∗←zi±1/2−vj(s)​Δ​t/2z_{i\pm 1/2}^{\ast}\leftarrow z_{i\pm 1/2}-v_{j}^{(s)}\Delta t/219:𝖿sn+1​(zi,vj(s),μk)←1Δ​z​[𝒫​(𝖥s,z)​(zi+1/2∗)−𝒫​(𝖥s,z)​(zi−1/2∗)]∀i,j,k\mathsf{f}_{s}^{n+1}(z_{i},v_{j}^{(s)},\mu_{k})\leftarrow\frac{1}{\Delta z}[\mathcal{P}(\mathsf{F}_{s,z})(z_{i+1/2}^{\ast})-\mathcal{P}(\mathsf{F}_{s,z})(z_{i-1/2}^{\ast})]\quad\forall i,j,k20:endfor21:t←t+Δ​tt\leftarrow t+\Delta t22:endfor23:return𝖿eNt,𝖿iNt\mathsf{f}_{e}^{N_{t}},\mathsf{f}_{i}^{N_{t}}

## A.2Finite difference Scheme

To solve the Poisson system (2.2) forϕ\phiand compute the electric fieldE=−∂zϕE=-\partial_{z}\phiwe implement a 4th-order finite difference scheme with homogeneous Dirichlet boundary conditions (i.e.,ϕ0=ϕN−1=0\phi_{0}=\phi_{N-1}=0). For the interior points, the second derivative is approximated as:∂z​zϕ​(t,zi)≈−ϕi−2+16​ϕi−1−30​ϕi+16​ϕi+1−ϕi+212​Δ​z2,for​i=2,3,…,N−3.\partial_{zz}\phi(t,z_{i})\approx\frac{-\phi_{i-2}+16\phi_{i-1}-30\phi_{i}+16\phi_{i+1}-\phi_{i+2}}{12\Delta z^{2}},\quad\text{for }i=2,3,\dots,N-3\,.

For the near-boundary points (i=1i=1andi=N−2i=N-2), we use the corresponding one-sided 4th-order schemes:∂z​zϕ​(t,z1)\displaystyle\partial_{zz}\phi(t,z_{1})≈11​ϕ0−20​ϕ1+6​ϕ2+4​ϕ3−ϕ412​Δ​z2,\displaystyle\approx\frac{11\phi_{0}-20\phi_{1}+6\phi_{2}+4\phi_{3}-\phi_{4}}{12\Delta z^{2}}\,,∂z​zϕ​(t,zN−2)\displaystyle\partial_{zz}\phi(t,z_{N-2})≈−ϕN−5+4​ϕN−4+6​ϕN−3−20​ϕN−2+11​ϕN−112​Δ​z2.\displaystyle\approx\frac{-\phi_{N-5}+4\phi_{N-4}+6\phi_{N-3}-20\phi_{N-2}+11\phi_{N-1}}{12\Delta z^{2}}\,.

Similarly, we construct the 4th-order central difference scheme for the first derivative:∂zϕ​(t,zi)≈ϕi−2−8​ϕi−1+8​ϕi+1−ϕi+212​Δ​zfor​i=2,3,…,N−3,\partial_{z}\phi(t,z_{i})\approx\frac{\phi_{i-2}-8\phi_{i-1}+8\phi_{i+1}-\phi_{i+2}}{12\Delta z}\quad\text{for }i=2,3,\dots,N-3\,,

with the near-boundary approximations:∂zϕ​(t,z1)\displaystyle\partial_{z}\phi(t,z_{1})≈−3​ϕ0−10​ϕ1+18​ϕ2−6​ϕ3+ϕ412​Δ​z,\displaystyle\approx\frac{-3\phi_{0}-10\phi_{1}+18\phi_{2}-6\phi_{3}+\phi_{4}}{12\Delta z}\,,∂zϕ​(t,zN−2)\displaystyle\partial_{z}\phi(t,z_{N-2})≈−ϕN−5+6​ϕN−4−18​ϕN−3+10​ϕN−2+3​ϕN−112​Δ​z.\displaystyle\approx\frac{-\phi_{N-5}+6\phi_{N-4}-18\phi_{N-3}+10\phi_{N-2}+3\phi_{N-1}}{12\Delta z}\,.

## Appendix BArchitecture of the MLP

We summarize the architecture of the MLP used to parametrize the magnetic field|𝐁||\mathbf{B}|in Figure14.Figure 14:Architecture of the MLP used to define|𝐁​(z;θ)||\mathbf{B}(z;\theta)|.

## Appendix CRobustness of the optimization routine

We run Algorithm1for100100different initializations and plot the mean of the different optimal magnetic profiles and a95%95\%confidence interval for both, the single-species and multi-species regimes.Figure 15:Mean of optimal magnetic profiles|𝐁​(z;θ∗)||\mathbf{B}(z;\theta^{\ast})|for different initializationsθ0\theta_{0}and shaded area representing a95%95\%confidence interval. From left to right: single-species and multi-species.

## 


- 


Major funding support from
