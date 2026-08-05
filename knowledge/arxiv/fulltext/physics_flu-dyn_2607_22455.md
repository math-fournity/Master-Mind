# Modeling and Stabilization of Transport-Dominated Flows

**arXiv ID**: 2607.22455v1
**Authors**: Christopher Agesen, Sam Bradford, Abhijnan Dikshit, Anshi Gupta, Bhavana Morankar, Jack Murphy, Nanda N. Raghunathan, Karnav Raval, Lane H. Rogers, Valeria Barra
**Published**: 2026-07-24
**Categories**: physics.flu-dyn, math-ph, math.NA
**Comments**: 2026 Graduate Student Mathematical Modeling Camp Final Report
**HTML URL**: https://arxiv.org/html/2607.22455v1

## Abstract

This report explores and compares numerical stabilization methods for transport-dominated flows arising in atmospheric modeling. The Streamline-Upwind (SU) and Streamline-Upwind Petrov-Galerkin (SUPG) stabilization formulations are implemented in Julia's ClimaCore.jl package and Python's Firedrake package for a test problem with slotted-cylinder initial conditions. These methods are compared for their ability to mitigate spurious oscillations while preserving sharp features against existing hyperdiffusion and quasi-monotone limiter methods, alongside various combinations. For this benchmark, quasi-monotone limiters were most effective at minimizing un-physical extrema, at the expense of diffusing the overall structure. The SUPG method was not found to improve upon the no stabilization case, for this test case in the computed error metrics. However, it performs best at preserving sharp feature and overall structure, among tested stabilized runs. Theoretical properties of SUPG are analyzed, and an asymptotics-based SUPG algorithm is proposed as future work.

## Full Text

Modeling and Stabilization of Transport-Dominated Flows 2026 Graduate Student Mathematical Modeling Camp Final Report

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
- License: CC BY 4.0arXiv:2607.22455v1 [physics.flu-dyn] 24 Jul 2026

## Modeling and Stabilization of Transport-Dominated Flows
2026 Graduate Student Mathematical Modeling Camp
Final ReportChristopher AgesenSam BradfordAbhijnan DikshitNJITWestern UniversityPurdue UniversityAnshi GuptaBhavana MorankarJack MurphyU. of HoustonNC State UniversityU. of ArizonaNanda N. RaghunathanKarnav RavalLane H. RogersU. of PittsburghWestern UniversityU. of TennesseeMentored by Dr. Valeria BarraSan Diego State University

## Abstract

This report explores and compares numerical stabilization methods for transport-dominated flows arising in atmospheric modeling. The Streamline-Upwind (SU) and Streamline-Upwind Petrov-Galerkin (SUPG) stabilization formulations are implemented in Julia’sClimaCore.jlpackage and Python’sFiredrakepackage for a test problem with slotted-cylinder initial conditions. These methods are compared for their ability to mitigate spurious oscillations while preserving sharp features against existing hyperdiffusion and quasi-monotone limiter methods, alongside various combinations. For this benchmark, quasi-monotone limiters were most effective at minimizing un-physical extrema, at the expense of diffusing the overall structure. The SUPG method was not found to improve upon the no stabilization case, for this test case in the computed error metrics. However, it performs best at preserving sharp feature and overall structure, among tested stabilized runs. Theoretical properties of SUPG are analyzed, and an asymptotics-based SUPG algorithm is proposed as future work.

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

## 1Introduction

Accurate numerical simulations of the Earth’s atmosphere are important for studying phenomena such as climate change. Among several classical modeling challenges in atmospheric flows, the transport of a passive tracer via pure advection is especially challenging due to the nature of such problems. A pure advection problem is an example of a partial differential equation (PDE) that, when discretized with a high-order Finite Element Method (FEM) or Spectral Element Method (SEM), leads to spurious numerical oscillations and instabilities.

As such, it is necessary to implement stabilization strategies that can mitigate oscillations and instabilities. Examples of such stabilization strategies include a fourth-order Laplacian operator (referred to ashyperdiffusion)[15], slope or flux-limiters[4], and flux-corrected transport[17]. Such methods, however, are not specific to the Finite or Spectral Element Methods (FEM or SEM), apply isotropic diffusion, symmetric in all directions, and often tend to overly smear out desired sharp gradients. Other methods such as the Streamline-Upwind Petrov Galerkin (SUPG) method[1](and its simplified version, the Streamline-Upwind (SU) method) apply diffusion only along the streamlines of the flow and thus, can better maintain sharp gradients present in the flow.

The main aim of this project is to systematically compare different stabilization strategies using the transport of a passive tracer as a test problem. The model of passive tracer transport (via pure advection) was implemented in theClimaCore.jl[2]and Firedrake[7]packages, which use the Julia and Python programming languages, respectively.

ClimaCore.jl[2]is an open-source library for the dynamical core (dycore) of a proposed advanced Earth System Model (ESM). An ESM is a massive, multiscale, multiphysics model that couples different model components and media (including the atmosphere, ocean, and land masses) to provide an accurate representation of Earth’s climate systems. The proposed ESM has been developed by the Climate Modeling Alliance (CliMA), which is a coalition of scientists, engineers, and applied mathematicians from CalTech, MIT, and the NASA Jet Propulsion Laboratory. The dynamical core (also calleddycore) of this ESM is described in this paper[16].

In theClimaCore.jllibrary, some stabilization strategies are readily available and utilized to counteract the numerical instability of such transport-dominated flows. These include artificial diffusion, limiters, and flux-corrected transport strategies mentioned earlier.

In this project, the subject of primary interest is the FEM/SEM-specific SUPG[1](and simplified SU method) of stabilizing numerical solutions to PDEs. We hypothesize that the SUPG method will exhibit superior performance at preserving the sharp features in transport-dominated flows (which can be of interest in problems with discontinuities or variations of scales), as this method introduces stabilization along the streamlines of the flow only—that is, anisotropically. Accordingly, we study the initial condition characterized by two high-density regions of passive tracers in the shape of slotted cylinders, as described below in Section2. We then proceed to compare the performance of the SU and SUPG methods to alternative methods of stabilizing transport dominated flows, such as a specific class of slope/flux-limiters and hyperdiffusion in Section4. In this paper, we offer an extensive numerical and theoretical analysis of the mathematical basis of SU and SUPG method for reducing spurious oscillations and preserving sharp features in transport dominated flow problems.

In Section5(Theoretical Analysis), we distinguish global conservation of density and tracer mass from pointwise boundedness of the tracer mixing ratio. We show that the conservative semidiscrete SUPG formulation preserves total mass on the closed spherical domain, but that standard linear SUPG does not guarantee nonnegativity, a discrete maximum principle, or total-variation-diminishing behavior. We then discuss residual-based discontinuity capturing and conservative flux limiting as possible modifications for suppressing crosswind oscillations and enforcing physically admissible tracer bounds. Additionally, we propose an improved time-dependent SUPG algorithm based on an asymptotic expansion of the tracer density. This algorithm allows us to solve an implicit SUPG problem by solving a series of explicit SUPG problems instead; greatly reducing computational cost.

## 2Problem Statement

This section describes the slotted cylinders benchmark problem statement. This benchmark problem is similar to the test case proposed by Nair and Lauritzen[10]. Consider the advection problem on the domainΩ\Omega{∂ρ∂t=−∇⋅ρ​𝐮,∂Q∂t=−∇⋅Q​𝐮\begin{cases}\frac{\partial\rho}{\partial t}=-\nabla\cdot\rho\mathbf{u},\\
\frac{\partial Q}{\partial t}=-\nabla\cdot Q\mathbf{u}\end{cases}(1)

Here,ρ​(λ,θ,t)∈ℜ\rho(\lambda,\theta,t)\in\Reis the fluid density,Q​(λ,θ,t)=q​(λ,θ,t)∗ρ​(λ,θ,t)∈ℜQ(\lambda,\theta,t)=q(\lambda,\theta,t)*\rho(\lambda,\theta,t)\in\Reis the tracer density, and𝐮​[u,v]\mathbf{u}[u,v]is the two-dimensional velocity field. The symbol∇⋅\nabla\cdotdenotes the divergence operator on the surface of a sphere. Moreover,λ,θ,and​t\lambda,\theta,\text{and}\;tdenote latitude, longitude, and time respectively.

For a divergent flow,𝐮​[u,v]\mathbf{u}[u,v]is defined as𝐮​[u​(λ,θ,t),v​(λ,θ,t)]=[u0​sin2⁡(λ)​sin⁡(2​θ)​cos⁡(π​tT)+(360T)​cos⁡(θ)u0​sin⁡(2​λ)​cos⁡(θ)​cos⁡(π​tT)]\mathbf{u}[u(\lambda,\theta,t),v(\lambda,\theta,t)]=\begin{bmatrix}u_{0}\sin^{2}(\lambda)\sin(2\theta)\cos(\frac{\pi t}{T})+(\frac{360}{T})\cos(\theta)\\
u_{0}\sin(2\lambda)\cos(\theta)\cos(\frac{\pi t}{T})\end{bmatrix}

Here,u0=2​π​RTu_{0}=\frac{2\pi R}{T}, with the spherical radius of the EarthR=6.37122×106R=6.37122\times 10^{6}m andT=12⋅24⋅60⋅60T=12\cdot 24\cdot 60\cdot 60s represents a total duration of twelve days in seconds.

Consider the problem characterized by two slotted-cylinders for the tracer concentration as initial condition. Letr0=R/2=3.18561×106r_{0}=R/2=3.18561\times 10^{6}be the radii of the two slotted cylinders, centered at(−π/6,0)(-\pi/6,0)and(π/6,0)(\pi/6,0)respectively. The symbolsr1r_{1}andr2r_{2}denote the radii of the two great circles centered at these respective points. Accordingly, we initialize the tracer densityQ​(λ,θ,0)Q(\lambda,\theta,0)as follows:Q={1,r1≤r0​and​|λ−λ1|​R≥D​(r0/6),1,r2≤r0​and​|λ−λ2|​R≥D​(r0/6),1,r1≤r0​and​|λ−λ1|​R<D​(r0/6)​and​(ϕ−ϕ1)​R<D​(−5​r0/12),1,r2≤r0​and​|λ−λ2|​R​<D​(r0/6)∧(ϕ−ϕ2)​R>​D​(5​r0/12),0.1,otherwise.Q=\begin{cases}1,&r_{1}\leq r_{0}\ \text{ and }\ |\lambda-\lambda_{1}|\,R\geq D(r_{0}/6),\\
1,&r_{2}\leq r_{0}\ \text{ and }\ |\lambda-\lambda_{2}|\,R\geq D(r_{0}/6),\\
1,&r_{1}\leq r_{0}\ \text{ and }\ |\lambda-\lambda_{1}|\,R<D(r_{0}/6)\ \text{ and }\ (\phi-\phi_{1})\,R<D(-5r_{0}/12),\\
1,&r_{2}\leq r_{0}\ \text{ and }\ |\lambda-\lambda_{2}|\,R<D(r_{0}/6)\ \wedge\ (\phi-\phi_{2})\,R>D(5r_{0}/12),\\
0.1,&\text{otherwise.}\end{cases}

whereD​(s)=180π​sD(s)=\tfrac{180}{\pi}s.

## 2.1SUPG Stabilization method

The weak form of the above advection problem may be derived by multiplying the strong-form equations presented in (1) by a test functionv∈H1​(Ω)v\in H^{1}(\Omega)to obtain∫Ω∂ρ∂t​v​𝑑Ω\displaystyle\int_{\Omega}\frac{\partial\rho}{\partial t}vd\Omega=−∫Ω[(∇⋅ρ​𝐮)​v]​𝑑Ω,\displaystyle=-\int_{\Omega}\left[(\nabla\cdot\rho\mathbf{u})v\right]d\Omega,(2)∫Ω∂Q∂t​v​𝑑Ω\displaystyle\int_{\Omega}\frac{\partial Q}{\partial t}\ v\ d\Omega=−∫Ω[(∇⋅Q​𝐮)​v]​𝑑Ω\displaystyle=-\int_{\Omega}\left[(\nabla\cdot Q\mathbf{u})v\right]d\Omega(3)

In order to apply integration by parts to the above form it will be necessary to letvvto be inH01​(Ω)H^{1}_{0}(\Omega). Since the standard Galerkin bilinear form is not coercive in the streamline direction,
spurious oscillations tend to emerge near sharp gradients in convection-dominated problems. But an anisotropic stabilization may be achieved through the Streamline-Upwinding Petrov Galerkin (SUPG) method[1]. The core idea of the Petrov-Galerkin stabilization strategy is to is to replace the test functionvvby an alternate function,v~=v+τ​𝐮⋅∇v\tilde{v}=v+\tau\,\mathbf{u}\cdot\nabla v, which clearly indicates the flow direction. As a part of this approach the test function resides in a different function space than the trial function, unlike the classical Galerkin formulation. Thus, the SUPG weak form of (3) is given as∫Ωv~​(∂Q∂t+∇⋅(Q​𝐮))​dΩ=0.\int_{\Omega}\tilde{v}\left(\frac{\partial Q}{\partial t}+\nabla\cdot(Q\mathbf{u})\right)\mathrm{d}\Omega=0.

Upon expandingv~\tilde{v}we get,∫Ωv​(∂Q∂t+∇⋅(Q​𝐮))​dΩ⏟standard Galerkin+∫Ωτ​(𝐮⋅∇v)​(∂Q∂t+∇⋅(Q​𝐮))​dΩ⏟SUPG correction=0\displaystyle\underbrace{\int_{\Omega}v\left(\frac{\partial Q}{\partial t}+\nabla\cdot(Q\,\mathbf{u})\right)\mathrm{d}\Omega}_{\text{standard Galerkin}}+\underbrace{\int_{\Omega}\tau\,(\mathbf{u}\cdot\nabla v)\left(\frac{\partial Q}{\partial t}+\nabla\cdot(Q\,\mathbf{u})\right)\mathrm{d}\Omega}_{\text{SUPG correction}}=0(4)

## 3Numerical Methods

In this section, we present the discrete weak formulation underlying the ClimaCore.jl and Firedrake implementations.

## 3.1SU and SUPG weak formulation: discrete implementation

The standard Galerkin formulation for the density equation is given as follows. Findρh∈Vh⊂H01​(Ω)\rho_{h}\in V_{h}\subset H^{1}_{0}(\Omega)such that for allvh∈Vhv_{h}\in V_{h}:(∂ρh∂t,vh)−(ρh​𝐮,∇vh)=0,\displaystyle\left(\frac{\partial\rho_{h}}{\partial t},\,v_{h}\right)-\left(\rho_{h}\,\mathbf{u},\,\nabla v_{h}\right)=0,(5)

where(⋅,⋅)(\cdot,\cdot)denotes theL2​(Ω)L^{2}(\Omega)inner product and the
divergence term has been integrated by parts. Note that SUPG correction is not applied to the density. A formulation of conservative SUPG for the tracer equation is formulated in the following lines.Table 1:Description of corrections based on the residual equation used.ModeResidualℛadv​(qh)\mathcal{R}_{\mathrm{adv}}(q_{h}):SU(Streamline Upwind only)𝐮⋅∇qh\mathbf{u}\cdot\nabla q_{h}non-consistent:consistent(full Brooks–Hughes SUPG[1])∂tqh+𝐮⋅∇qh\partial_{t}q_{h}+\mathbf{u}\cdot\nabla q_{h}consistent

Find(ρ​q)h∈Vh(\rho q)_{h}\in V_{h}such that for allvh∈Vhv_{h}\in V_{h}:0\displaystyle 0=(∂Qh∂t,vh)−(Qh​𝐮,∇vh)+∫∂Ωvh​Qh​(𝐮⋅n^)​dσ⏟standard Galerkin\displaystyle=\underbrace{\left(\frac{\partial Q_{h}}{\partial t},\,v_{h}\right)-\left(Q_{h}\,\mathbf{u},\,\nabla v_{h}\right)+\int_{\partial\Omega}v_{h}\,Q_{h}\,(\mathbf{u}\cdot\hat{n})\,\mathrm{d}\sigma}_{\text{standard Galerkin}}(6)+∑K∫ΩKτ​(𝐮⋅∇vh)​ρh​ℛadv​(qh)​dΩ⏟SUPG correction.\displaystyle\phantom{\qquad\qquad}+\underbrace{\sum_{K}\int_{\Omega_{K}}\tau\,(\mathbf{u}\cdot\nabla v_{h})\,\rho_{h}\,\mathcal{R}_{\mathrm{adv}}(q_{h})\,\mathrm{d}\Omega}_{\text{SUPG correction}}.

Depending on the precise choice of the termℛadv​(qh)\mathcal{R}_{\mathrm{adv}}(q_{h}), the correction may be the consistent SUPG correction or the non-consistent SU correction. The various choices ofℛadv​(qh)\mathcal{R}_{\mathrm{adv}}(q_{h})and the corresponding corrections that they describe are charted in Table1.

Petrov-Galerkin interpretation:To reiterate, the SU and SUPG terms may be interpreted as making use of the test function:v~h=vh+τ​𝐮⋅∇vh,\displaystyle\tilde{v}_{h}=v_{h}+\tau\,\mathbf{u}\cdot\nabla v_{h},(7)

so that the trial and test function spaces differ. Consequently, we perturb the test functions so that the compact support of those functions travels along the direction of the streamlines.


## 3.2The Stabilization Parameterτ\tau

The code uses the Tezduyar–Osawa[12]formula for pure
advection (κ=0\kappa=0):τϵ=[(2Δ​t)2+(2​‖𝐮‖h)2]−1/2,\tau^{\epsilon}=\left[\left(\frac{2}{\Delta t}\right)^{2}+\left(\frac{2\|\mathbf{u}\|}{h}\right)^{2}\right]^{-1/2},(8)

wherehhis the averagenodallength scaleh∼he/ph\sim h_{e}/p(element width divided by polynomial degree).
Reasoning behind the stabilization parameter:Recall the optimal stabilisation parameter for the 1D steady
advection-diffusion problem:τ∗\displaystyle\tau^{*}=h2​‖𝐮‖​ξ​(P​e),\displaystyle=\frac{h}{2\|\mathbf{u}\|}\,\xi(Pe),where​ξ​(P​e)\displaystyle\text{where}\ \xi(Pe)=coth⁡(P​e)−1P​e,and​P​e=‖𝐮‖​h2​ε.\displaystyle=\coth(Pe)-\frac{1}{Pe},\ \text{and}\ Pe=\frac{\|\mathbf{u}\|\,h}{2\varepsilon}.

But for an advection dominated problem(P​e≫1Pe\gg 1,ε→0\varepsilon\to 0),coth⁡(P​e)→1,1P​e→0⇒ξ​(P​e)→1,\coth(Pe)\to 1,\qquad\frac{1}{Pe}\to 0\qquad\Rightarrow\qquad\xi(Pe)\to 1,

and hence,τ∗⟶h2​‖𝐮‖.\tau^{*}\;\longrightarrow\;\frac{h}{2\|\mathbf{u}\|}.

The UGN element length scale:UGN stands for Upwind-direction, Global,
Nodal, describing how the element length scalehUGNh_{\mathrm{UGN}}is constructed[12]:
- •

U: the length is measured in theupwind
(streamline) direction𝐮^=𝐮/‖𝐮‖\hat{\mathbf{u}}=\mathbf{u}/\|\mathbf{u}\|,
not isotropically.
- •

G: it is aglobalelement length, usingallnodes of the element by summing over all basis functionsNaN_{a}.
- •

N: it isnodal, computed directly from the
nodal basis functionsNaN_{a}and their gradients∇Na\nabla N_{a}.

The explicit formula from[12]is:hUGN=2​‖𝐮‖​(∑a=1nen|𝐮⋅∇Na|)−1,h_{\mathrm{UGN}}=2\|\mathbf{u}\|\left(\sum_{a=1}^{n_{\mathrm{en}}}\bigl|\mathbf{u}\cdot\nabla N_{a}\bigr|\right)^{-1},

wherenenn_{\mathrm{en}}is the number of nodes per element. Geometrically,hUGNh_{\mathrm{UGN}}is the distance spanned by𝐮\mathbf{u}across the element in the streamline direction.
SUGN stands for Stabilisation parameter,
Upwind, Global, Nodal — it is simply the
prefix S (stabilisation parameter) appended to UGN. The three components are[12]:τSUGN1\displaystyle\tau_{\mathrm{SUGN1}}=hUGN2​‖𝐮‖\displaystyle=\frac{h_{\mathrm{UGN}}}{2\|\mathbf{u}\|}(advective timescale),\displaystyle\text{(advective timescale)},τSUGN2\displaystyle\tau_{\mathrm{SUGN2}}=Δ​t2\displaystyle=\frac{\Delta t}{2}(temporal timescale),\displaystyle\text{(temporal timescale)},τSUGN3\displaystyle\tau_{\mathrm{SUGN3}}=hUGN24​ν\displaystyle=\frac{h_{\mathrm{UGN}}^{2}}{4\nu}(diffusive timescale).\displaystyle\text{(diffusive timescale)}.

They are combined as anℓ2\ell^{2}inverse norm:(τSUPG)UGN=[1τSUGN12+1τSUGN22+1τSUGN32]−1/2,(\tau_{\mathrm{SUPG}})_{\mathrm{UGN}}=\left[\frac{1}{\tau_{\mathrm{SUGN1}}^{2}}+\frac{1}{\tau_{\mathrm{SUGN2}}^{2}}+\frac{1}{\tau_{\mathrm{SUGN3}}^{2}}\right]^{-1/2},

so thatτ\tauis always bounded by the smallest of the three
timescales.
By removing the diffusing term, thus we get the formula defined in (8).

## 3.3Implementation details for the ClimaCore.jl code

The ClimaCore.jl code used in testing was created by augmenting the existing sphere examplelimiters_advection.jlin the public repository[2](located in
ClimaCore.jl/examples/sphere/limiters_advection.jl). The quasi-monotone limiters and hyperdiffusion stabilization techniques were already implemented in the ClimaCore.jl API and exercised in thelimiters_advection.jlexample file. SU and SUPG were novel implementations, developed in this project. After computing the weak form of the solution, the resulting differential equation is solved using the tri-stage, third-order Strong Stability Preserving Runge-Kutta method (SSPRK33) from theOrdinaryDiffEq.jlpackage. At each time step, a weighted direct stiffness summation is applied for continuity enforcement of the continuous-Galerkin (CG) spectral elements. Table2below highlights choices made for key solver and discretization parameters in the code when solving the test case considered in this work.Table 2:Discretization and solver parameters used in the ClimaCore.jl code.ParameterValueNumber of horizontal elements per cube panel20Number of quadrature nodes4Time step size,Δ​t\Delta t345.60 sNumber of time steps3000Hyperdiffusion coefficient6.6×10146.6\times 10^{14}

The example code enables the combination of different stabilization methods. SU and SUPG cannot be applied in the same run, but either can be paired with limiters hyperdiffusion, or both limiters and hyperdiffusion. The implementation of the continuous equations and residual calculation for SUPG is described below.

LetΩ\Omegabe the sphere. The state consists of densityρ\rhoand
tracerqq(e.g. concentration). The strong form of the
system is:∂ρ∂t+∇⋅(ρ​𝐮)\displaystyle\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\,\mathbf{u})=0\displaystyle=0(9)∂(ρ​q)∂t+∇⋅(ρ​q​𝐮)\displaystyle\frac{\partial(\rho q)}{\partial t}+\nabla\cdot(\rho q\,\mathbf{u})=0\displaystyle=0(10)

where𝐮\mathbf{u}is a prescribed, time-dependent velocity field. Because the continuity equation (9) holds, the tracer equation (10) can be rewritten via the product rule:∂(ρ​q)∂t+∇⋅(ρ​q​𝐮)=ρ​(∂q∂t+𝐮⋅∇q)⏟ℛadv​(q)+q​(∂ρ∂t+∇⋅(ρ​𝐮))⏟=0​by (9)=ρ​ℛadv​(q).\frac{\partial(\rho q)}{\partial t}+\nabla\cdot(\rho q\,\mathbf{u})=\rho\underbrace{\left(\frac{\partial q}{\partial t}+\mathbf{u}\cdot\nabla q\right)}_{\mathcal{R}_{\mathrm{adv}}(q)}+q\underbrace{\left(\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\,\mathbf{u})\right)}_{=\,0\text{ by \eqref{eq:density}}}=\rho\,\mathcal{R}_{\mathrm{adv}}(q).

Hence at thecontinuouslevel the conservative residual of
(10) factors as:R​(ρ​q)=ρ​ℛadv​(q),whereℛadv​(q)=∂q∂t+𝐮⋅∇q.{R(\rho q)=\rho\,\mathcal{R}_{\mathrm{adv}}(q),\qquad\text{where}\qquad\mathcal{R}_{\mathrm{adv}}(q)=\frac{\partial q}{\partial t}+\mathbf{u}\cdot\nabla q.}

At the discrete level, ifρh\rho_{h}does not satisfy (9) exactly (which it generally will not), then the conservative and advective forms decouple.

## 3.4Implementation details for the Firedrake code

The Firedrake library[7]implementation utilized the SU stabilization method for solving the advection problem. Originally, the SUPG stabilization implemented in the Gusto library[13]was utilized. However, further exploration uncovered that stabilization is only implemented in Gusto for planar meshes rather than spherical meshes, which are of interest in this work, since the pure advection problem is modeled on a cubed spherical mesh in this project. As such, the SU stabilization was directly implemented through the Firedrake library using the weak form of the governing equations. The Gusto library example for the slotted cylinders benchmark[13]was adapted to test the Firedrake implementation.

Firedrake allows the user to directly specify the test function space (whereas this is indirectly implemented in ClimaCore.jl and not part of the public-facing API). This allowed an easy specification of the SU correction test function shown in (7). This test function can then be used to specify the linear and bilinear forms of FEM as follows.

Casting∂Q/∂t+𝐮⋅∇Q=0\partial Q/\partial t+\mathbf{u}\cdot\nabla Q=0as a method-of-lines problem for the ratek≡∂Q/∂tk\equiv\partial Q/\partial t, each stage solves: findkkwith∫Ωvh​k​𝑑x⏟a​(wh,k)=−∫Ωv~h​(𝐮⋅∇Q)​𝑑x⏟L​(wh),v~h=vh+τ​𝐮⋅∇vh,∀vh∈Vh.\underbrace{\int_{\Omega}v_{h}\,k\,dx}_{a(w_{h},k)}=\underbrace{-\int_{\Omega}\tilde{v}_{h}\,(\mathbf{u}\cdot\nabla Q)\,dx}_{L(w_{h})},\quad\tilde{v}_{h}=v_{h}+\tau\,\mathbf{u}\cdot\nabla v_{h},\quad\forall\,v_{h}\in V_{h}.(11)

Since the SU correction is applied to the advection term only and not the temporal term,a​(ϕ,k)a(\phi,k)is the standard Galerkin mass matrix, independent of𝐮\mathbf{u}andτ\tau. It is therefore assembled and factorised once (constant_jacobian=True) and reused across all stages, unlike the full SUPG, where the mass matrix must be reassembled whenever𝐮\mathbf{u}changes; the trade-off is that the stabilization is only𝒪​(h)\mathcal{O}(h)consistent. The stabilization parameter follows the Tezduyar formula as given in (8). To calculate the stabilization parameter,h=|K|h=\sqrt{|K|}is computed from the local cell area,|K||K|, and stored as aD​G​0DG0field in Firedrake.

Subsequently, theLinearVariationalSolvefunctionality from Firedrake can be used to solve the weak form of the equations. To advance the solution in time, the SSPRK3 scheme[11]is implemented, which solves the weak form of the equations and updates the solution at each time step. In this way, the Firedrake implementation can apply the SU stabilization to an unsteady advection problem.

Withk​(D,t)k(D,t)the rate from (11) at fieldDDand velocity timett, the stepD(n)→D(n+1)D^{(n)}\to D^{(n+1)}isD(1)\displaystyle D^{(1)}=D(n)+Δ​t​k​(D(n),t(n)),\displaystyle=D^{(n)}+\Delta t\,k\left(D^{(n)},\,t^{(n)}\right),D(2)\displaystyle D^{(2)}=34​D(n)+14​D(1)+14​Δ​t​k​(D(1),t(n)+Δ​t),\displaystyle=\tfrac{3}{4}D^{(n)}+\tfrac{1}{4}D^{(1)}+\tfrac{1}{4}\Delta t\,k\left(D^{(1)},\,t^{(n)}+\Delta t\right),(12)D(n+1)\displaystyle D^{(n+1)}=13​D(n)+23​D(2)+23​Δ​t​k​(D(2),t(n)+12​Δ​t),\displaystyle=\tfrac{1}{3}D^{(n)}+\tfrac{2}{3}D^{(2)}+\tfrac{2}{3}\Delta t\,k\left(D^{(2)},\,t^{(n)}+\tfrac{1}{2}\Delta t\right),

with the velocity re-evaluated at the stage abscissaec=[0,1,12]c=[0,\,1,\,\tfrac{1}{2}]. Each stage is one LU solve of the pre-factored mass matrix; being strong-stability-preserving, SSPRK3 adds no oscillations beyond those in the spatially stabilized operator. Table3below details choices for important discretization and solver parameters used in the Firedrake code. The refinement level is an indication of the spatial grid size. A refinement level ofnnindicates that there are2n2^{n}segments along each edge of a panel in the discretization.Table 3:Discretization and solver parameters used in the Firedrake code.ParameterValueRefinement level4Time step size,Δ​t\Delta t345.60 sNumber of time steps3000Polynomial degree of elements3Quadrature degree6

## 4Results and Discussion

We now compare numerical solutions of the passive-tracer advection system (1) under various stabilization (and combinations thereof) methods, using both theClimaCore.jl[2]and Firedrake[7]packages. We compare the simulations both qualitatively through the tracer fields and quantitatively using particular error metrics of interest.

We solve the advection system with the slotted-cylinder test case, with the initial condition as shown in Figure1. Following the examples inClimaCore.jl[2], this is chosen such that the tracer field returns to its initial configuration after one cyclet∈[0,T]t\in[0,T].Figure 1:Initial condition for all simulations showing two slotted cylinders, plotted on a latitude-longitude grid.

As such, we choose two classes of metrics to quantify the error between the initial and final field. In order to evaluate if the tracer field remains physically bounded (no spurious undershoots/overshoots), we computeqover\displaystyle q_{\mathrm{over}}=maxλ,θ⁡qT−maxλ,θ⁡q0Δ​q0,\displaystyle=\frac{\max_{\lambda,\theta}q_{T}-\max_{\lambda,\theta}q_{0}}{\Delta q_{0}},qunder\displaystyle q_{\mathrm{under}}=minλ,θ⁡qT−minλ,θ⁡q0Δ​q0,\displaystyle=\frac{\min_{\lambda,\theta}q_{T}-\min_{\lambda,\theta}q_{0}}{\Delta q_{0}},(13)

whereq0q_{0}andqTq_{T}denote the initial and final tracer fields (respectively) and the initial tracer range is defined asΔ​q0=maxλ,θ⁡q0−minλ,θ⁡q0.\Delta q_{0}=\max_{\lambda,\theta}q_{0}-\min_{\lambda,\theta}q_{0}.(14)

While (13) measure the appearance of local nonphysical extrema, they do not measure the preservation of the overall shape of the tracer field. Thus, we also compute the global errors between the initial and final tracer fieldsℓ1=I​[|qT−q0|]I​[|q0|],ℓ2=(I​[(qT−q0)2]I​[q02])1/2,ℓ∞=maxλ,θ⁡|qT−q0|maxλ,θ⁡|q0|,\displaystyle\ell_{1}=\frac{I\!\left[|q_{T}-q_{0}|\right]}{I\!\left[|q_{0}|\right]},\ \ \ell_{2}=\left(\frac{I\!\left[(q_{T}-q_{0})^{2}\right]}{I\!\left[q_{0}^{2}\right]}\right)^{1/2},\ \ \ell_{\infty}=\frac{\max_{\lambda,\theta}|q_{T}-q_{0}|}{\max_{\lambda,\theta}|q_{0}|},(15)

whereI​[f]=14​π​∫02​π∫−π/2π/2f​(λ,θ)​cos⁡θ​d​θ​d​λ\displaystyle I[f]=\frac{1}{4\pi}\int_{0}^{2\pi}\int_{-\pi/2}^{\pi/2}f(\lambda,\theta)\cos\theta\,\mathrm{d}\theta\,\mathrm{d}\lambda(16)

denotes the spherical area average.

We numerically solve the passive-tracer advection system (1) for the slotted-cylinder test case, using hyperdiffusion, quasi-monotone limiting, SU, SUPG, and selected combinations of these stabilization methods. The error metrics (13) and (15) are computed for each case, and shown in Table4.Table 4:Comparison of simulations with different stabilization choices, including combinations. All results were computed using ClimaCore.jl except for the labeled Firedrake run. Here H, L, SU, and SUPG denote hyperdiffusion, the quasi-monotone limiter, streamline upwind, and streamline-upwind Petrov–Galerkin stabilization, respectively.Stabilizationqoverq_{\mathrm{over}}qunderq_{\mathrm{under}}ℓ1\ell_{1}ℓ2\ell_{2}ℓ∞\ell_{\infty}None9.43×10−39.43\text{\times}{10}^{-3}−1.37×10−02-1.37\text{\times}{10}^{-02}9.60×10−049.60\text{\times}{10}^{-04}4.39×10−034.39\text{\times}{10}^{-03}1.34×10−011.34\text{\times}{10}^{-01}H1.24×10−011.24\text{\times}{10}^{-01}−1.42×10−01-1.42\text{\times}{10}^{-01}1.62×10−011.62\text{\times}{10}^{-01}5.99×10−015.99\text{\times}{10}^{-01}6.826.82L4.69×10−074.69\text{\times}{10}^{-07}−7.32×10−08-7.32\text{\times}{10}^{-08}9.86×10−029.86\text{\times}{10}^{-02}4.48×10−014.48\text{\times}{10}^{-01}6.306.30SU3.99×10−023.99\text{\times}{10}^{-02}−7.36×10−02-7.36\text{\times}{10}^{-02}9.39×10−029.39\text{\times}{10}^{-02}4.36×10−014.36\text{\times}{10}^{-01}4.504.50SU (Firedrake)6.57×10−026.57\text{\times}{10}^{-02}−7.83×10−02-7.83\text{\times}{10}^{-02}7.92×10−027.92\text{\times}{10}^{-02}1.70×10−011.70\text{\times}{10}^{-01}6.17×10−016.17\text{\times}{10}^{-01}SUPG5.96×10−025.96\text{\times}{10}^{-02}−4.61×10−02-4.61\text{\times}{10}^{-02}1.43×10−021.43\text{\times}{10}^{-02}2.75×10−022.75\text{\times}{10}^{-02}6.25×10−016.25\text{\times}{10}^{-01}H + L1.41×10−071.41\text{\times}{10}^{-07}−7.32×10−08-7.32\text{\times}{10}^{-08}1.43×10−011.43\text{\times}{10}^{-01}5.98×10−015.98\text{\times}{10}^{-01}7.017.01L + SU4.69×10−074.69\text{\times}{10}^{-07}−7.32×10−08-7.32\text{\times}{10}^{-08}1.21×10−011.21\text{\times}{10}^{-01}5.14×10−015.14\text{\times}{10}^{-01}5.525.52L + SUPG4.69×10−074.69\text{\times}{10}^{-07}−7.32×10−08-7.32\text{\times}{10}^{-08}9.86×10−029.86\text{\times}{10}^{-02}4.48×10−014.48\text{\times}{10}^{-01}6.306.30H + L + SU1.38×10−071.38\text{\times}{10}^{-07}−7.32×10−08-7.32\text{\times}{10}^{-08}1.63×10−011.63\text{\times}{10}^{-01}6.34×10−016.34\text{\times}{10}^{-01}6.586.58H + L + SUPG1.41×10−071.41\text{\times}{10}^{-07}−7.32×10−08-7.32\text{\times}{10}^{-08}1.43×10−011.43\text{\times}{10}^{-01}5.98×10−015.98\text{\times}{10}^{-01}7.017.01

First, we turn our attention to the solutions computed using the SU stabilization method, as this was the case computed by both the ClimaCore.jl and Firedrake implementations. The solutions at the initial, intermediate (t=T/2t=T/2) and final (t=Tt=T) times are shown in Figure2. Observe that the solutions computed using different implementations qualitatively match with one another over the time domain, with visibly comparable smearing of the sharp tracer features by the final time. This is also reflected in the error results shown in Table4, where all of the metrics match up to the order of magnitude, except forℓ∞\ell_{\infty}. This comparison provides a useful consistency check, as the main behavior of the SU method matches between two independent implementations. However, the discrepancy inℓ∞\ell_{\infty}indicates that they are not numerically identical, and more work is required to find the source of this difference.(a)ClimaCore.jl,t=0t=0.(b)Firedrake,t=0t=0.(c)ClimaCore.jl,t=T/2t=T/2.(d)Firedrake,t=T/2t=T/2.(e)ClimaCore.jl,t=Tt=T.(f)Firedrake,t=Tt=T.Figure 2:Comparison of the streamline-upwind (SU) solutions computed
with ClimaCore.jl and Firedrake. The top row confirms the common initial
tracer configuration att=0t=0; the middle and bottom rows show the
tracer fields att=T/2t=T/2andt=Tt=T, respectively.

In Figure3we show the tracer field at the final time point computed usingClimaCore.jlfor four stabilization methods, including the case without stabilization111For completeness, the tracer fields at botht=T/2t=T/2andt=Tt=Tfor all ten ClimaCore.jl stabilization configurations are shown in AppendixA.. Observe that the solution without stabilization is able to retain the sharp features of the slotted cylinders quite well and the solution with SUPG is not visually different than that with no stabilization. As expected, we see more blurring/smearing around the sharp features of the cylinders in the case of the quasi-monotone limiter and even more in the hyperdiffusion case.(a)No stabilization.(b)SUPG.(c)Quasi-monotone limiter.(d)Hyperdiffusion.Figure 3:Tracer fields at final time pointt=Tt=Tfor four stabilization methods implemented inClimaCore.jl.

Now turning our attention to Table4, we can better assess the methods’ performance in preventing unphysical extrema while retaining the overall tracer field. Observe that compared to the no stabilization case, the quasi-monotone limiter drastically reduces final-time overshoot and undershoot, withqunderq_{\mathrm{under}}andqoverq_{\mathrm{over}}reducing down to10−7​–​10−810^{-7}–10^{-8}. However, this is done at the expense of significantly larger global errors. Hyperdiffusion performs poorly across all of the computed metrics compared to the no stabilization case. Among the ClimaCore.jl stabilized solutions, the SUPG method performs best at preserving the tracer structure (as is evident by the smallestℓ1\ell_{1},ℓ2\ell_{2}, andℓ∞\ell_{\infty}errors), however it does not improve on the unstabilized baseline. Finally, in the cases where the limiter is included in a combined method, the extrema errors remain in the same10−710^{-7}–10−810^{-8}range, showing that the behavior is analogous to that when the limiter method used alone.

Overall, these results illustrate the tradeoff between preserving global structure and suppressing local overshoots and undershoots. The quasi-monotone limiter is most effective at preventing spurious oscillation, but does so at the expense of global errors. The SUPG method is better than the limiters at preserving the global structure, but has largerqunderq_{\text{under}}andqoverq_{\text{over}}errors. No single stabilization method of those tested is best across all metrics – and most notably, the SUPG method does not improve on the no stabilization baseline for any of the metrics.

It should be noted that the metrics chosen here for the definition of the errors, namely equations (13) and (15), only account for the difference between the final time solutions and the initial conditions. They do not track the temporal evolution over time. For a test case such as the one analyzed in this work, where the flow distorts the initial tracer configuration and then reverts it back to match its initial condition, tracking the history of the errors at every time step would give more information on the performance of the different stabilization methods in the transient stages. Finally, higher-order polynomial degree tests should be considered as they would highlight the benefits of the stabilization methods compared to the no stabilization results.

## 5Theoretical Analysis

## 5.1Conservation, boundedness, and variation control

The exact transport system possesses two different kinds of structure. The
conservative variablesρ\rhoandQ=ρ​qQ=\rho qsatisfy global conservation laws,
whereas the mixing ratioqqsatisfies a pointwise transport equation. Indeed,
expanding the tracer-density equation gives0\displaystyle 0=∂(ρ​q)∂t+∇⋅(ρ​q​𝐮)\displaystyle=\frac{\partial(\rho q)}{\partial t}+\nabla\cdot(\rho q\mathbf{u})(17)=ρ​(∂q∂t+𝐮⋅∇q)+q​(∂ρ∂t+∇⋅(ρ​𝐮)).\displaystyle=\rho\left(\frac{\partial q}{\partial t}+\mathbf{u}\cdot\nabla q\right)+q\left(\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{u})\right).(18)

Consequently, whereverρ>0\rho>0, the density equation implies∂q∂t+𝐮⋅∇q=0.\frac{\partial q}{\partial t}+\mathbf{u}\cdot\nabla q=0.(19)

Thusqqis constant along characteristics of the exact velocity field. In
particular, the continuous solution satisfiesminΩ⁡q​(⋅,0)≤q​(𝐱,t)≤maxΩ⁡q​(⋅,0)for all​t\min_{\Omega}q(\cdot,0)\leq q(\mathbf{x},t)\leq\max_{\Omega}q(\cdot,0)\qquad\text{for all }t(20)

for which the characteristic flow remains well defined. For the present
slotted-cylinder problem, the physically relevant interval is therefore0.1≤q≤10.1\leq q\leq 1.

## Semidiscrete conservation

The conservative SUPG formulation in (6) preserves total
tracer mass independently of whether it preserves the pointwise bounds in
(20). To see this, choose the constant test functionwh=1w_{h}=1. This choice is admissible because the computational domain is the
closed sphere and the finite element space contains constants. Since∇1=0\nabla 1=0, both the advective weak term and the SUPG correction vanish.
There is also no boundary-flux contribution on a closed surface. Hence,(∂Qh∂t,1)=0,\left(\frac{\partial Q_{h}}{\partial t},1\right)=0,(21)

which givesdd​t​∫ΩQh​dΩ=0.\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega}Q_{h}\,\mathrm{d}\Omega=0.(22)

The same argument applied to the density equation yieldsdd​t​∫Ωρh​dΩ=0.\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega}\rho_{h}\,\mathrm{d}\Omega=0.(23)

These identities hold at the semidiscrete level, up to quadrature and linear
solver tolerances. A Runge–Kutta method also preserves these linear
invariants provided that the residual at every stage has zero integral.

The factorρh\rho_{h}in the tracer SUPG correction is nevertheless important.
It makes the stabilization act on the advective residual of the mixing ratio
while the prognostic variableQh=ρh​qhQ_{h}=\rho_{h}q_{h}remains conservative. This
mass-weighted construction supports consistency between the density and
tracer equations, including preservation of a spatially constant mixing
ratio. It doesnot, by itself, implyqh≥0q_{h}\geq 0or prevent the creation
of new extrema.

## Why standard SUPG is not bound preserving or TVD

The SUPG term adds residual-based dissipation primarily in the streamline
direction[1]. This improves stability for
advection-dominated problems, but the resulting high-order finite element
operator is not generally monotone and does not satisfy a discrete maximum
principle. In particular, the consistent mass matrix and the off-diagonal
entries of the transport operator need not have the sign structure required
for a positivity-preserving update[5]. This distinction
is visible in Table4: the SUPG solution
conserves the transported quantity but still produces nonzero overshoot and
undershoot metrics, whereas the quasi-monotone limiter reduces both metrics
to nearly machine precision.

This limitation is consistent with the classical order barrier identified by
Godunov: within the usual linear one-step setting, a method that is monotone
for linear advection cannot be more than first-order accurate[3]. The theorem does not apply verbatim to every
multidimensional finite element formulation, but it identifies the basic
reason that a consistent residual-based stabilization such as SUPG (which is linear when applied to a linear PDE, and nonlinear otherwise) cannot
simultaneously provide sharp resolution and unconditional monotonicity. A
nonlinear limiting or nonlinear diffusion mechanism is required.

For a one-dimensional grid, the discrete total variation is commonly defined
byTV​(qn)=∑j|qj+1n−qjn|,\mathrm{TV}(q^{n})=\sum_{j}|q_{j+1}^{n}-q_{j}^{n}|,(24)

and a method is TVD ifTV​(qn+1)≤TV​(qn)\mathrm{TV}(q^{n+1})\leq\mathrm{TV}(q^{n})[8]. Strict TVD
should be interpreted cautiously for the present spherical deformational-flow
benchmark. Even the exact multidimensional transport map can stretch
interfaces and increase∫Ω|∇q|​dΩ\int_{\Omega}|\nabla q|\,\mathrm{d}\Omegaduring the
cycle. The more appropriate requirements here are preservation of the
physical interval[0.1,1][0.1,1], absence of numerically generated extrema, and
control of excess variation relative to the exact transported field. Since
the flow returns the tracer to its initial configuration att=Tt=T, the ratioTV​(qh​(T))/TV​(qh​(0))\mathrm{TV}(q_{h}(T))/\mathrm{TV}(q_{h}(0))can still be used as an end-of-cycle
diagnostic, but a per-step TVD inequality is not expected from the exact
multidimensional dynamics.

## Modifications needed for sharper and bound-preserving transport

A first extension is a residual-dependent discontinuity-capturing or
crosswind-diffusion term. One representative form is𝒮DC​(qh,wh)=∑K∫KνDC,K​(𝐏⟂​∇qh)⋅(𝐏⟂​∇wh)​dΩ,\mathcal{S}_{\mathrm{DC}}(q_{h},w_{h})=\sum_{K}\int_{K}\nu_{\mathrm{DC},K}\left(\mathbf{P}_{\perp}\nabla q_{h}\right)\cdot\left(\mathbf{P}_{\perp}\nabla w_{h}\right)\,\mathrm{d}\Omega,(25)

where𝐏⟂=𝐈−𝐮^⊗𝐮^,𝐮^=𝐮‖𝐮‖,\mathbf{P}_{\perp}=\mathbf{I}-\widehat{\mathbf{u}}\otimes\widehat{\mathbf{u}},\qquad\widehat{\mathbf{u}}=\frac{\mathbf{u}}{\|\mathbf{u}\|},(26)

andνDC,K≥0\nu_{\mathrm{DC},K}\geq 0is activated by a local residual or gradient
sensor. At points where‖𝐮‖\|\mathbf{u}\|is zero or sufficiently small, the
projector must be regularized, for example by replacing‖𝐮‖\|\mathbf{u}\|withmax⁡(‖𝐮‖,εu)\max(\|\mathbf{u}\|,\varepsilon_{u})for a small
positive toleranceεu\varepsilon_{u}. The original “beyond SUPG” construction adds precisely this type of discontinuity-capturing mechanism to control strong internal and boundary
layers[14]. Such a term damps crosswind oscillations that
streamline diffusion alone cannot see and can substantially reduce ringing
near the slots. However, a generic shock-capturing term is not automatically
TVD or maximum-principle preserving; its coefficient and nonlinear sensor
must be designed with those properties in mind.

A stronger route is conservative algebraic flux correction or convex
limiting. In algebraic form, write the high-order semidiscrete method as𝐌C​𝐪˙+𝐊H​𝐪=0,\mathbf{M}_{C}\dot{\mathbf{q}}+\mathbf{K}_{H}\mathbf{q}=0,(27)

where𝐌C\mathbf{M}_{C}is the consistent mass matrix and𝐊H\mathbf{K}_{H}contains the Galerkin and SUPG contributions. A
bound-preserving low-order method is first constructed using a lumped mass
matrix𝐌L\mathbf{M}_{L}and sufficient graph viscosity:𝐌L​𝐪˙+𝐊L​𝐪=0.\mathbf{M}_{L}\dot{\mathbf{q}}+\mathbf{K}_{L}\mathbf{q}=0.(28)

The low-order update is chosen to satisfy a local maximum principle under an
appropriate CFL restriction. The difference between the high- and low-order
operators is then decomposed into pairwise antidiffusive fluxesfi​j=−fj​if_{ij}=-f_{ji}. Replacing each flux byαi​j​fi​j\alpha_{ij}f_{ij}, with0≤αi​j≤10\leq\alpha_{ij}\leq 1, restores as much high-order
accuracy as the local bounds permit while retaining conservation. This is
the finite element flux-correction framework developed in[9]; related invariant-domain and maximum-principle
preserving continuous finite element constructions are given in[6].

For the coupled density–tracer system, the conservative variableQhQ_{h}should
continue to be updated in mass form, but the admissible bounds should be
imposed onqh=Qh/ρhq_{h}=Q_{h}/\rho_{h}. The density and tracer fluxes must therefore be
limited consistently. Pointwise clipping ofqhq_{h}after a time step would
restore nonnegativity but generally destroy tracer-mass conservation, whereas
pairwise conservative flux limiting can enforce the bounds and preserve
(22). When an SSP Runge–Kutta method is used,
the limiter must be applied at every forward-Euler stage so that the fully
discrete update remains a convex combination of bound-preserving stages[11].

These additions have clear benefits: they prevent physically impossible
negative tracer concentrations, suppress spurious ringing, and make the
extrema metrics in (13) controlled properties of the
algorithm rather than empirical outcomes. The tradeoffs are additional
nonlinearity, a CFL restriction for explicit bound preservation, and some
extra diffusion near discontinuities. A useful practical hierarchy is
therefore SUPG for streamline stability, residual-based discontinuity
capturing for unresolved crosswind gradients, and conservative flux limiting
only where the physical bounds would otherwise be violated.

## 5.2Asymptotic Approach to Time-Dependent SUPG

In Section3, we explored the efficacy of the time-independent SUPG implementation using the stabilizing termτe​∫Ω(u⋅∇v)​(∇⋅(Q​u)+∂Q∂t)\tau^{e}\int_{\Omega}(u\cdot\nabla v)\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)

Where the term∂Q∂t\frac{\partial Q}{\partial t}is computed from theprevioustime step as a proxy for the∂Q∂t\frac{\partial Q}{\partial t}field at the current time step. While this allows us to set up an explicit method rather than an implicit method, it suffers from inaccuracy for large time steps. Rather than pursuing a computationally costly implicit SUPG method, we take an asymptotic expansion based approach to improve our proxy for∂Q∂t\frac{\partial Q}{\partial t}at the current time step.

Consider the SUPG stabilizing term (assuming no source, i.e.s=0s=0)τe​∫Ω(u⋅∇v)​(∇⋅(Q​u)+∂Q∂t)\tau^{e}\int_{\Omega}(u\cdot\nabla v)\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)=τe​∫Ω∇v⋅[u​(∇⋅(Q​u)+∂Q∂t)]=\tau^{e}\int_{\Omega}\nabla v\cdot\left[u\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)\right]

And since∇⋅(A​B)=(∇A)⋅B+A​(∇⋅B)\nabla\cdot(AB)=(\nabla A)\cdot B+A(\nabla\cdot B), this can be written as=τe​∫Ω∇⋅{v​[u​(∇⋅(Q​u)+∂Q∂t)]}−τe​∫Ωv​{∇⋅[u​(∇⋅(Q​u)+∂Q∂t)]}=\tau^{e}\int_{\Omega}\nabla\cdot\left\{v\left[u\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)\right]\right\}-\tau^{e}\int_{\Omega}v\left\{\nabla\cdot\left[u\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)\right]\right\}

By the divergence theorem,τe​∫Ω∇⋅{v​[u​(∇⋅(Q​u)+∂Q∂t)]}=τe​∮∂Ωv​[u​(∇⋅(Q​u)+∂Q∂t)]⋅𝐧^=0,\tau^{e}\int_{\Omega}\nabla\cdot\left\{v\left[u\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)\right]\right\}=\tau^{e}\oint_{\partial\Omega}v\left[u\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)\right]\cdot\hat{\mathbf{n}}=0,

sincevvvanishes on∂Ω\partial\Omega. Thus, the SUPG stabilizing term is−τe​∫Ωv​{∇⋅[u​(∇⋅(Q​u)+∂Q∂t)]}-\tau^{e}\int_{\Omega}v\left\{\nabla\cdot\left[u\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)\right]\right\}

Then the tracer dynamics are described by∫Ωv​(∂Q∂t)=−∫Ωv​(∇⋅(Q​u))−τe​∫Ωv​{∇⋅[u​(∇⋅(Q​u)+∂Q∂t)]}.\int_{\Omega}v\left(\frac{\partial Q}{\partial t}\right)=-\int_{\Omega}v(\nabla\cdot(Qu))-\tau^{e}\int_{\Omega}v\left\{\nabla\cdot\left[u\left(\nabla\cdot(Qu)+\frac{\partial Q}{\partial t}\right)\right]\right\}.

We now perform a nondimensionalization of this problem. TakeQ=cQ¯,u=Uu¯,t=Tt¯,∇⋅=1L∇¯⋅Q=c\bar{Q},\quad u=U\bar{u},\quad t=T\bar{t},\quad\nabla\cdot=\frac{1}{L}\bar{\nabla}\cdot

so we havecT​∫Ωv​(∂Q¯∂t¯)=\displaystyle\frac{c}{T}\int_{\Omega}v\left(\frac{\partial\bar{Q}}{\partial\bar{t}}\right)=−c​UL∫Ωv(∇¯⋅(Q¯u¯))−τec​U2L2∫Ωv{∇¯⋅[u¯(∇¯⋅(Q¯u¯)]}\displaystyle-\frac{cU}{L}\int_{\Omega}v(\bar{\nabla}\cdot(\bar{Q}\bar{u}))-\tau^{e}\frac{cU^{2}}{L^{2}}\int_{\Omega}v\{\bar{\nabla}\cdot[\bar{u}(\bar{\nabla}\cdot(\bar{Q}\bar{u})]\}−τe​c​UL​T​∫Ωv​{∇¯⋅[u¯​(∂Q¯∂t¯)]}.\displaystyle-\tau^{e}\frac{cU}{LT}\int_{\Omega}v\left\{\bar{\nabla}\cdot\left[\bar{u}\left(\frac{\partial\bar{Q}}{\partial\bar{t}}\right)\right]\right\}.

By the substitutionT=L/UT=L/U, we get∫Ωv​(∂Q¯∂t¯)=\displaystyle\int_{\Omega}v\left(\frac{\partial\bar{Q}}{\partial\bar{t}}\right)=−∫Ωv(∇¯⋅(Q¯u¯))−τeUL∫Ωv{∇¯⋅[u¯(∇¯⋅(Q¯u¯)]}\displaystyle-\int_{\Omega}v(\bar{\nabla}\cdot(\bar{Q}\bar{u}))-\tau^{e}\frac{U}{L}\int_{\Omega}v\{\bar{\nabla}\cdot[\bar{u}(\bar{\nabla}\cdot(\bar{Q}\bar{u})]\}−τe​UL​∫Ωv​{∇¯⋅[u¯​(∂Q¯∂t¯)]}\displaystyle-\tau^{e}\frac{U}{L}\int_{\Omega}v\left\{\bar{\nabla}\cdot\left[\bar{u}\left(\frac{\partial\bar{Q}}{\partial\bar{t}}\right)\right]\right\}

In our atmospheric simulation of the Earth,U≈102​[k​m/h​r]U\approx 10^{2}[km/hr],L≈6⋅103​[k​m]L\approx 6\cdot 10^{3}[km]. We haveτe≈2.5⋅10−1​[h​r]\tau^{e}\approx 2.5\cdot 10^{-1}[hr]. Thus,τe​UL≈4⋅10−3≪1.\tau^{e}\frac{U}{L}\approx 4\cdot 10^{-3}\ll 1.

Lettingε:=τe​UL\varepsilon:=\tau^{e}\frac{U}{L}, we have∫Ωv​(∂Q¯∂t¯)\displaystyle\int_{\Omega}v\left(\frac{\partial\bar{Q}}{\partial\bar{t}}\right)=−∫Ωv​(∇¯⋅(Q¯​u¯))\displaystyle=-\int_{\Omega}v(\bar{\nabla}\cdot(\bar{Q}\bar{u}))(29)−ε​∫Ωv​(∇¯⋅{u¯​[∇¯⋅(Q¯​u¯)]})−ε​∫Ωv​{∇¯⋅[u¯​(∂Q¯∂t¯)]}\displaystyle\phantom{=\,}-\varepsilon\int_{\Omega}v(\bar{\nabla}\cdot\{\bar{u}[\bar{\nabla}\cdot(\bar{Q}\bar{u})]\})-\varepsilon\int_{\Omega}v\left\{\bar{\nabla}\cdot\left[\bar{u}\left(\frac{\partial\bar{Q}}{\partial\bar{t}}\right)\right]\right\}

From this point on, we will neglect the overbar notation (e.g.Q¯\bar{Q}) in the non-dimensionalization for simplicity. Consider the asymptotic expansionQ=Q0+ε​Q1+…Q=Q_{0}+\varepsilon Q_{1}+...

Substituting into (1919) and expanding up to𝒪​(1)\mathcal{O}(1), we get the leading term relation∫Ωv​(∂Q0∂t)=−∫Ωv​(∇⋅(Q0​u))\displaystyle\int_{\Omega}v\left(\frac{\partial Q_{0}}{\partial t}\right)=-\int_{\Omega}v(\nabla\cdot(Q_{0}u))(30)

Expanding up to𝒪​(ε)\mathcal{O}(\varepsilon), we have∫Ωv​(∂Q1∂t)\displaystyle\int_{\Omega}v\left(\frac{\partial Q_{1}}{\partial t}\right)=−∫Ωv​(∇⋅(Q1​u))−∫Ωv​{∇⋅[u​(∇⋅(Q0​u))]}\displaystyle=-\int_{\Omega}v(\nabla\cdot(Q_{1}u))-\int_{\Omega}v\{\nabla\cdot[u(\nabla\cdot(Q_{0}u))]\}(31)−∫Ωv​{∇⋅[u​(∂Q0∂t)]}.\displaystyle\phantom{=\,}-\int_{\Omega}v\left\{\nabla\cdot\left[u\left(\frac{\partial Q_{0}}{\partial t}\right)\right]\right\}.

If we consider the time discretization∂Qin∂t≈Qin−Qin−1Δ​t,\displaystyle\frac{\partial Q_{i}^{n}}{\partial t}\approx\frac{Q_{i}^{n}-Q_{i}^{n-1}}{\Delta t},(32)

we can construct an algorithm based on solving consecutive pairs(Q0n+1,Q1n+1)(Q_{0}^{n+1},Q_{1}^{n+1})from(Q0n,Q1n)(Q_{0}^{n},Q_{1}^{n}). First, we initialize the start system based on the initial concentrationQQ. We can set(Q00,Q10)=(Q,0)(Q_{0}^{0},Q_{1}^{0})=(Q,0)

Then, given some pair(Q0n,Q1n)(Q_{0}^{n},Q_{1}^{n})at thent​hn^{th}time step, we follow the diagram in Figure4and the algorithm outlined below.Q0nQ_{0}^{n}Q1nQ_{1}^{n}Q0n+1Q_{0}^{n+1}∂Qin+1∂t\dfrac{\partial Q_{i}^{n+1}}{\partial t}Q1n+1Q_{1}^{n+1}122333\boxed{3}Figure 4:Diagrammatic representation of the solution algorithm for the asymptotic approach of the pure advection problem with SU stabilization.
- 1.

Use the RK4 algorithm to computeQ0n+1Q_{0}^{n+1}fromQ0nQ_{0}^{n}within the standard Galerkin method in (30)
- 2.

Numerically compute∂Q0n+1∂t\frac{\partial Q_{0}^{n+1}}{\partial t}fromQ0nQ_{0}^{n}andQ0n+1Q_{0}^{n+1}in (32).
- 3.

Use the SU method to computeQ1n+1Q_{1}^{n+1}fromQ1nQ_{1}^{n},Q0n+1Q_{0}^{n+1}, and∂Q0n+1∂t\frac{\partial Q_{0}^{n+1}}{\partial t}in (31).
- 4.

Setn=n+1n=n+1, compute the tracer concentrationQn=Q0n+ε​Q1nQ^{n}=Q_{0}^{n}+\varepsilon Q_{1}^{n}, and repeat from step 1.

While this algorithm involves solving two discrete Galerkin-type problems at each time step (standard Galerkin forQ0n+1Q_{0}^{n+1}, SU forQ1n+1Q_{1}^{n+1}), it allows us to include a non-delayed time-dependent term in the strong-form residual in the stabilizing term.

It should be noted that our asymptotic expansionQ=Q0+ε​Q1Q=Q_{0}+\varepsilon Q_{1}is arbitrary, and could contain more terms. The algorithm detailed in this section is but a member of a class of algorithms; the algorithm where the number of expansion terms inn=2n=2. For example, with the addition of a third termQ2Q_{2}scaled byε2\varepsilon^{2}, we could detail an algorithm which requires solving three discrete Galerkin-type problems at each time step. Computation scales linearly with the number of expansion terms, asnnterms requiresnnGalerkin-type problems to be solved at each time step. The choice for the number of expansion terms used should be based on comparisons with implicit SUPG methods, as well as computational constraints.

## 6Conclusions and Future Work

In this work, we have implemented the Streamline Upwind (SU) and Streamline Upwind Petrov-Galerkin (SUPG) stabilization methods for finite element methods (FEM) using theClimaCore.jllibrary[2]. An implementation for SU is also developed in Firedrake[7]to compare and contrast it with the implementation in ClimaCore.jl. Other stabilization methods, such as hyperdiffusion and flux-limiters, are also implemented in ClimaCore.jl and we conduct a cross-comparison of these four stabilization methods.

The comparison between the stabilization methods was performed using the slotted-cylinders deformation flow benchmark problem. For this problem, we found that the solution obtained without numerical stabilization is able to resolve the sharp features of the cylinders quite well and gave the smallest global errors. Stabilization using quasi-monotone limiters greatly improved at reducing spurious extrema at the expense of global accuracy, leading to smearing over the course of the simulation. The hyperdiffusion method performed relatively poorly across all metrics. When methods were combined, the flux-limiter method was shown to largely determine the extrema behavior, with hyperdiffusion, SU, and SUPG having minimal additive impact. In a comparison of implementation, both Python’s Firedrake and Julia’s ClimaCore.jl produced errors at the same order of magnitude, with the notable exception of theℓ∞\ell_{\infty}-error, where they differ by a single order of magnitude. The SUPG method was not found to improve upon the no stabilization baseline, for the metrics tested in this work. However, among the stabilized runs, the SUPG method resulted in the lowest global errors.

Following these results, multiple directions for this research may be pursued. For instance, additional test cases with a variety of tracer configurations and fluid regimes would provide a more comprehensive comparison of the stabilization methods. Moreover, additional error tracking measuring the error over time (rather than only at the final time) would give a more complete view. Finally, our implementations of the the SU and SUPG methods would benefit from different sets of parameter studies.

The theoretical analysis also clarifies that conservation and bound preservation are distinct properties. The conservative semidiscrete SUPG formulation preserves total density and tracer mass on the closed spherical domain, but standard linear SUPG is not generally maximum-principle preserving or total variation diminishing. The overshoots and undershoots observed numerically are therefore consistent with the structure of the method. A future bound-preserving implementation could combine SUPG with residual-based crosswind discontinuity capturing and a conservative flux or convex limiter applied consistently to the density and tracer fluxes.

An asymptotics based SUPG algorithm based on the SU and delayed SUPG methods was developed, but remains to be implemented. For potential future research, this algorithm could be implemented and compared with implicit SUPG methods, and the impact of the number of asymptotic expansion terms on accuracy could be studied.

## 7Acknowledgments

We would like to gratefully acknowledge the support of SIAM and the University of Delaware for providing the resources to conduct this work. Additionally, a special thank you to Dr. Valeria Barra for her excellent mentorship and support.

## 8AI Use Disclosure

The code development for the Firedrake implementation was aided by Claude Opus 4.8.

## References
- [1]A. N. Brooks and T. J.R. Hughes(1982)Streamline upwind/petrov-galerkin formulations for convection dominated flows with particular emphasis on the incompressible navier-stokes equations.Computer Methods in Applied Mechanics and Engineering.External Links:DocumentCited by:§1,§1,§2.1,Table 1,§5.1.
- [2]ClimaCore.jlExternal Links:LinkCited by:§1,§1,§3.3,§4,§4,§6.
- [3]S. K. Godunov(1959)A difference method for numerical calculation of discontinuous solutions of the equations of hydrodynamics.Matematicheskii Sbornik47(3),pp. 271–306.Note:In Russian; English translation published as U.S. Joint Publications Research Service report JPRS 7226 (1969)Cited by:§5.1.
- [4]O. Guba, M. Taylor, and A. St-Cyr(2010)Optimization-based limiters for the spectral element method.Journal of Computational Physics.External Links:DocumentCited by:§1.
- [5]J. Guermond, B. Popov, and Y. Yang(2017)The effect of the consistent mass matrix on the maximum-principle for scalar conservation equations.Journal of Scientific Computing70(3),pp. 1358–1366.External Links:DocumentCited by:§5.1.
- [6]J. Guermond and B. Popov(2017)Invariant domains and second-order continuous finite element approximation for scalar conservation equations.SIAM Journal on Numerical Analysis55(6),pp. 3120–3146.External Links:DocumentCited by:§5.1.
- [7]D. A. Ham, P. H. J. Kelly, L. Mitchell, C. J. Cotter, R. C. Kirby, K. Sagiyama, N. Bouziani, S. Vorderwuelbecke, T. J. Gregory, J. Betteridge, D. R. Shapero, R. W. Nixon-Hill, C. J. Ward, P. E. Farrell, P. D. Brubeck, I. Marsden, T. H. Gibson, M. Homolya, T. Sun, A. T. T. McRae, F. Luporini, A. Gregory, M. Lange, S. W. Funke, F. Rathgeber, G. Bercea, and G. R. Markall(2023-05)Firedrake user manual.First edition edition,Imperial College London and University of Oxford and Baylor University and University of Washington.External Links:DocumentCited by:§1,§3.4,§4,§6.
- [8]A. Harten(1983)High resolution schemes for hyperbolic conservation laws.Journal of Computational Physics49(3),pp. 357–393.External Links:DocumentCited by:§5.1.
- [9]D. Kuzmin and S. Turek(2002)Flux correction tools for finite elements.Journal of Computational Physics175(2),pp. 525–558.External Links:DocumentCited by:§5.1.
- [10]R. D. Nair and P. H. Lauritzen(2010)A class of deformational flow test cases for linear transport problems on the sphere.Journal of Computational Physics.External Links:DocumentCited by:§2.
- [11]C. Shu and S. OsherEfficient implementation of essentially non-oscillatory shock-capturing schemes.Journal of computational physics.Cited by:§3.4,§5.1.
- [12]T. Tezduyar and S. Sathe(2003)Stabilization parameters in supg and pspg formulations.Journal of Computational and Applied Mathematics.Cited by:§3.2,§3.2,§3.2,§3.2.
- [13]The Gusto Development Team(2026)Gusto: a library for dynamical cores using compatible finite element discretisations.GitHub.Note:https://github.com/firedrakeproject/gustoCited by:§3.4.
- [14]M. M. Thomas J.R. Hughes and A. Mizukami(1986)A new finite element formulation for computational fluid dynamics: ii. beyond supg.Computer Methods in Applied Mechanics and Engineering.External Links:DocumentCited by:§5.1.
- [15]P. A. Ullrich, D. R. Reynolds, J. E. Guerra, and M. A. Taylor(2018-12)Impact and importance of hyperdiffusion on the spectral element method: a linear dispersion analysis.Journal of Computational Physics375,pp. 427–446.External Links:Document,ISSN 10902716Cited by:§1.
- [16]D. Yatunin, S. Byrne, C. Kawczynski, S. Kandala, G. Bozzola, A. Sridhar, Z. Shen, A. Jaruga, J. Sloan, J. He, D. Z. Huang, V. Barra, R. Chew, A. Boral, Y. Chen, O. Knoth, P. Ullrich, C. Mbengue, and T. Schneider(2026)The climate modeling alliance atmosphere dynamical core: concepts, numerics, and scaling.Journal of Advances in Modeling Earth Systems18(3),pp. e2025MS005014.External Links:Document,LinkCited by:§1.
- [17]S. T. Zalesak(1979)Fully multidimensional flux-corrected transport algorithms for fluids.Journal of Computational Physics31(3),pp. 335–362.External Links:ISSN 0021-9991,Document,LinkCited by:§1.

## Appendix ATracer Fields for All Stabilization Configurations(a)No stabilization.(b)Hyperdiffusion.(c)Quasi-monotone limiter.(d)SU.(e)SUPG.(f)Hyperdiffusion + limiter.(g)Limiter + SU.(h)Limiter + SUPG.(i)Hyperdiffusion + limiter + SU.(j)Hyperdiffusion + limiter + SUPG.Figure 5:Tracer fields at the intermediate timet=T/2t=T/2for all
stabilization choices implemented in ClimaCore.jl.(a)No stabilization.(b)Hyperdiffusion.(c)Quasi-monotone limiter.(d)SU.(e)SUPG.(f)Hyperdiffusion + limiter.(g)Limiter + SU.(h)Limiter + SUPG.(i)Hyperdiffusion + limiter + SU.(j)Hyperdiffusion + limiter + SUPG.Figure 6:Tracer fields at the final timet=Tt=Tfor all stabilization
choices implemented in ClimaCore.jl.

## 


- 


Major funding support from
