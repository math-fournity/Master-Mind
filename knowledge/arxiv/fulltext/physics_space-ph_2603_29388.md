# Closed-Form Solutions to the Fokker-Planck Equation for Orbital Uncertainty Propagation

**arXiv ID**: 2603.29388v1
**Authors**: Jose Antonio Rebollo, Rafael Vazquez, Claudio Bombardelli
**Published**: 2026-03-31
**Categories**: physics.space-ph, math.NA
**Comments**: Extended abstract submitted to 2026 AAS/AIAA Astrodynamics Specialist Conference, Whistler, British Columbia, July 26-30 2026
**HTML URL**: https://arxiv.org/html/2603.29388v1

## Abstract

Non-Gaussian tails dominate collision probability estimates in conjunction assessment, yet capturing them without Monte Carlo sampling is challenging, especially when process noise is included. We present a closed-form, grid-free solution to the Fokker-Planck equation by proving that an exponential-of-quadratic-form ansatz is structurally preserved under advection and diffusion. The probability density function propagates via a compact ODE system, significantly cheaper than Monte Carlo and without spatial discretization. As an application, the method performs orbit uncertainty propagation under stochastic forcing representative of atmospheric drag. Results demonstrate the method faithfully captures non-Gaussian features, asymmetric tails, and stochastic broadening, matching a Monte Carlo benchmark.

## Full Text

Closed-Form Solutions to the Fokker-Planck Equation for Orbital Uncertainty Propagation

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
- License: CC BY-NC-ND 4.0arXiv:2603.29388v1 [physics.space-ph] 31 Mar 2026

## Closed-Form Solutions to the Fokker-Planck Equation for Orbital Uncertainty PropagationJosé Antonio Rebollo111PhD Student, Aerospace Engineering Department, University of Seville, 41092, Seville, Spain.and Rafael Vázquez222Professor, Aerospace Engineering Department, University of Seville, 41092, Seville, Spain.Claudio Bombardelli333Professor, Department of Applied Physics for Aeronautical Engineering, Technical University of Madrid, 28040, Madrid, Spain.

## Abstract

Non-Gaussian tails dominate collision probability estimates in conjunction assessment, yet capturing them without Monte Carlo sampling is challenging, especially when process noise is included. We present a closed-form, grid-free solution to the Fokker-Planck equation by proving that an exponential-of-quadratic-form ansatz is structurally preserved under advection and diffusion. The probability density function propagates via a compact ODE system, significantly cheaper than Monte Carlo and without spatial discretization. As an application, the method performs orbit uncertainty propagation under stochastic forcing representative of atmospheric drag. Results demonstrate the method faithfully captures non-Gaussian features, asymmetric tails, and stochastic broadening, matching a Monte Carlo benchmark.

## 1Introduction

Characterizing how uncertainty evolves under nonlinear orbital dynamics is fundamental to modern space operations. Conjunction assessment, collision avoidance maneuver planning, re-entry prediction, and Space Domain Awareness (SDA) all depend on knowing not just where a spacecraft is likely to be, but how probable it is to be somewhere unexpected[Luo2017]. In these applications, thetailsof the probability distribution are often more consequential than its peak: a conjunction screening decision, for instance, hinges on whether the probability of collision, typically on the order of10−510^{-5}or smaller, exceeds an actionable threshold[Akella2000,Patera2001,Chan2008]. Accurately modeling these low-probability tails requires a faithful representation of the full probability density function (PDF), not merely its first two moments.

Current operational methods overwhelmingly rely on Gaussian assumptions propagated through linearized dynamics, e.g., via covariance propagation with state transition matrices[Maybeck1979]. These approximations systematically misrepresent the tails of the distribution: nonlinear dynamics stretch, curve, and skew an initially Gaussian cloud into distinctly non-Gaussian shapes[Junkins1996], while the Gaussian model continues to assign probability mass symmetrically. The practical consequence is that collision probabilities are either over- or under-estimated, both of which carry real operational cost, unnecessary avoidance maneuvers consuming finite fuel, or missed warnings for genuinely dangerous encounters. Extensions such as the unscented transform[Julier2004]improve moment propagation but remain fundamentally limited to low-order statistics and cannot reconstruct the full PDF shape. A complementary strategy is to reformulate the problem in a coordinate set that renders the dynamics nearly linear, so that the Gaussian assumption remains approximately valid; the Generalized Equinoctial Orbital Elements (GEqOE) have been shown to achieve this for the deterministic propagation case[Hernando2023].

More sophisticated approaches exist. Monte Carlo methods can capture the full nonlinear PDF, but require10510^{5}–10610^{6}samples to resolve the10−510^{-5}tail probabilities relevant to conjunction assessment, making them computationally prohibitive for operational timelines[Luo2017]. Gaussian mixture models[Horwood2011,Vittaldev2016]and entropy-based methods[DeMars2013]improve on the single-Gaussian approximation, but require an increasing number of components or basis functions to capture non-Gaussian tails, and the associated computational cost grows accordingly. Grid-based numerical solvers for the Fokker-Planck equation[Risken1996,Kumar2009]suffer from the curse of dimensionality: a 6D orbital state on even a coarse5050-point-per-axis grid requires506≈101050^{6}\approx 10^{10}evaluations per time step. The Probability Transformation Method (PTM), combined with Differential Algebra (DA) and Taylor maps[Berz1999,Park2006,Valli2013,Armellin2010,Wittig2015], elegantly solves the deterministic part of the problem (the Liouville equation) by propagating the flow map as a high-order polynomial expansion. However, all physical systems experience stochastic forcing, atmospheric drag fluctuations, unmodeled gravitational perturbations, solar radiation pressure variability, thrust execution errors, and incorporating this process noise into the PTM framework has remained an open challenge. Previous work has addressed stochastic uncertainty in specific applications using DA-based approaches[Vazquez2017], while Servadio and Zanetti[Servadio2020]developed recursive polynomial methods for nonlinear estimation applied to orbital mechanics. Nevertheless, extending the PTM to the full stochastic setting requires evaluating high-dimensional convolution integrals that reintroduce the very curse of dimensionality that DA was designed to circumvent.

This paper presents Taylor Map Diffusion, a framework that closes this gap. We show that the Fokker-Planck equation, including both deterministic advection and stochastic diffusion, admits solutions of a specific structural form: the exponential of a quadratic function of a nonlinear map. To the authors’ knowledge, this exponential-of-quadratic-form solution structure is new in the literature: while exponential-quadratic forms are well known for linear systems (where they reduce to Gaussians propagated by the Kalman filter), their preservation under the combined action of nonlinear advection and additive diffusion has not previously been established. The key result is a set of coupled ordinary differential equations (ODEs) governing the time evolution of the map and the precision matrix. These ODEs are derived by direct substitution into the FPE, yielding zero residual: the structural form is preserved rigorously under the combined action of advection and diffusion. In practice, the map is represented as a finite-order Taylor expansion, so the accuracy of the computed PDF is controlled by the truncation order, converging to the theoretical solution as the expansion order increases. The method is grid-free, captures the full non-Gaussian shape of the distribution including its tails, and naturally incorporates process noise. We demonstrate the algorithm on a planar Keplerian orbit problem and validate it against Monte Carlo stochastic simulations.

## 2The Taylor Diffusion Framework

## 2.1Ansatz and Main Result

Consider a dynamical system subject to additive white Gaussian noise,d​X=f​(X)​d​t+σ​d​Wt,dX=f(X)\,dt+\sigma\,dW_{t},(1)

whereX∈ℝnX\in\mathbb{R}^{n},ffis the deterministic drift, andΣ0=σ​σ⊤\Sigma_{0}=\sigma\sigma^{\top}is the diffusion tensor. The probability densityp​(x,t)p(x,t)satisfies the Fokker-Planck equation (FPE):∂p∂t=−∇⋅(f​p)+12​Tr​(Σ0​∇2p).\frac{\partial p}{\partial t}=-\nabla\cdot(f\,p)+\frac{1}{2}\mathrm{Tr}\!\left(\Sigma_{0}\,\nabla^{2}p\right).(2)

We propose the following ansatz for the density:p​(x,t)=𝒩​(t)​μ​(x,t)​exp⁡(−F​(x,t)⊤​Q​(t)​F​(x,t)),p(x,t)=\mathcal{N}(t)\,\mu(x,t)\,\exp\!\Big(-F(x,t)^{\top}Q(t)\,F(x,t)\Big),(3)

whereF:ℝn→ℝnF:\mathbb{R}^{n}\to\mathbb{R}^{n}is a smooth, invertible map withF​(x0​(t),t)=0F(x_{0}(t),t)=0(centered at the distribution’s mode),Q​(t)≻0Q(t)\succ 0is a symmetric positive definite precision matrix,μ​(x,t)\mu(x,t)is a smooth scalar field accounting for the divergence of the dynamics, and𝒩​(t)\mathcal{N}(t)is a normalization constant.

The central result of this work is:

## Theorem 1(Quadratic Form Conservation)

Let the initial density be of the form (3) whereF​(⋅,t0)F(\cdot,t_{0})is a diffeomorphism with isolated zero atx0​(t0)x_{0}(t_{0}),Q​(t0)≻0Q(t_{0})\succ 0, andμ​(x,t0)\mu(x,t_{0})a smooth scalar volume field. Under additive white Gaussian noise with diagonal covarianceΣ0=σ​σ⊤\Sigma_{0}=\sigma\sigma^{\top}, this structural form is preserved over time, provided(F,μ,Q)(F,\mu,Q)satisfy the coupled system:∂F∂t\displaystyle\frac{\partial F}{\partial t}=−JF​f+12​(F​∑iαi+Q−1​∑iDi+Δ−Γ),\displaystyle=-J_{F}\,f+\frac{1}{2}\!\left(F\sum_{i}\alpha_{i}+Q^{-1}\!\sum_{i}D_{i}+\Delta-\Gamma\right),(4)∂μ∂t\displaystyle\frac{\partial\mu}{\partial t}=(∇⋅f)−∇μ⋅f−(∇μ)⊤​Σ0​JF+12​Tr​(Σ0​∇2μ),\displaystyle=(\nabla\cdot f)-\nabla\mu\cdot f-(\nabla\mu)^{\top}\Sigma_{0}\,J_{F}+\frac{1}{2}\mathrm{Tr}\!\left(\Sigma_{0}\,\nabla^{2}\mu\right),(5)d​Qd​t\displaystyle\frac{dQ}{dt}=12​∑iJF−⊤​JΛi⊤​Q​JΛi​JF−1,\displaystyle=\frac{1}{2}\sum_{i}J_{F}^{-\top}\,J_{\Lambda_{i}}^{\top}Q\,J_{\Lambda_{i}}\,J_{F}^{-1},(6)

whereJF=∇xFJ_{F}=\nabla_{x}Fis the Jacobian ofFF;Λi=Σ0,i​∇Fi\Lambda_{i}=\sqrt{\Sigma_{0,i}}\,\nabla F_{i}withJΛi=∇xΛiJ_{\Lambda_{i}}=\nabla_{x}\Lambda_{i};Γ=2​JF​Σ0​JF⊤​Q​F\Gamma=2J_{F}\Sigma_{0}J_{F}^{\top}QF;Δk=∑jΣ0,j​∂2Fk/∂xj2\Delta_{k}=\sum_{j}\Sigma_{0,j}\,\partial^{2}F_{k}/\partial x_{j}^{2}; andDi∈ℝnD_{i}\in\mathbb{R}^{n},αi∈ℝ\alpha_{i}\in\mathbb{R}are smooth coupling fields that regularize the diffusion correction atF=0F=0(see below).

The proof proceeds by direct substitution of the ansatz (3) into the FPE (2). Computing both sides independently, the time derivative via the chain rule onμ​e−Φ\mu e^{-\Phi}withΦ=F⊤​Q​F\Phi=F^{\top}QF, and the right-hand side via the advection and diffusion operators, one verifies that all terms cancel identically when(F,μ,Q)(F,\mu,Q)satisfy the above system. The coupling fieldsDiD_{i}andαi\alpha_{i}arise from a key algebraic identity: any perturbation of a quadratic formF⊤​Q​FF^{\top}QFby a small symmetric correction can be absorbed into a smooth deformation of the underlying map and metric, providedDiD_{i}andαi\alpha_{i}are chosen to remove the apparent singularity atF=0F=0. Specifically:Di=JF−⊤​JΛi⊤​Q​Λi​(x0),αi=Λi⊤​Q​Λi−F⊤​JF−⊤​JΛi⊤​Q​JΛi​JF−1​F−Di⊤​F−CiF⊤​Q​F,D_{i}=J_{F}^{-\top}J_{\Lambda_{i}}^{\top}Q\,\Lambda_{i}(x_{0}),\qquad\alpha_{i}=\frac{\Lambda_{i}^{\top}Q\Lambda_{i}-F^{\top}J_{F}^{-\top}J_{\Lambda_{i}}^{\top}QJ_{\Lambda_{i}}J_{F}^{-1}F-D_{i}^{\top}F-C_{i}}{F^{\top}QF},(7)

whereCi=Λi​(x0)⊤​Q​Λi​(x0)C_{i}=\Lambda_{i}(x_{0})^{\top}Q\Lambda_{i}(x_{0})is a scalar constant ensuringlimx→x0αi=0\lim_{x\to x_{0}}\alpha_{i}=0.

Remark (theoretical vs. numerical).Theorem1establishes that the structural form (3) is closed under the FPE dynamics: no approximation is introduced in the evolution equations (4)–(6). In a numerical implementation,FFis represented as a finite-order Taylor expansion (e.g., up to quadratic terms). This truncation is the sole source of approximation: its effect diminishes as expansion order increases, and for linear dynamics the first-order representation is exact, recovering the result described in the following remark.

Remark (classical covariance propagation).The linear case provides the clearest illustration of the framework’s structure and its generalization. For linear dynamicsf​(x)=A​xf(x)=Ax, the Fokker-Planck equation admits an exact Gaussian solution, where the PDF is fully characterized at all times by its meanx0​(t)x_{0}(t)and covarianceP​(t)P(t), satisfying the finite ODE systemx˙0=A​x0,P˙=A​P+P​A⊤+Σ0.\dot{x}_{0}=A\,x_{0},\qquad\dot{P}=AP+PA^{\top}+\Sigma_{0}.(8)

No approximation is needed in this case; instead, a finite set of scalars, thenncomponents of the mean and then​(n+1)/2n(n+1)/2independent elements of the covariance fully encode the PDF at all times. In the present framework, this corresponds to takingF​(x,t)=Φ​(t)​(x−x0​(t))F(x,t)=\Phi(t)\bigl(x-x_{0}(t)\bigr), whereΦ​(t)\Phi(t)is the State Transition Matrix (STM) satisfyingΦ˙=A​Φ\dot{\Phi}=A\Phi,Φ​(t0)=I\Phi(t_{0})=I. With this choiceJF=ΦJ_{F}=\Phiand all higher-order terms vanish, so the system (4)–(6) reduces exactly to (8). Taylor Map Diffusion generalizes this structure directly to nonlinear dynamics: the nominal trajectoryx0x_{0}and STMΦ\Phiare generalized to a full nonlinear Taylor mapFF, capturing non-Gaussian deformations through its higher-order coefficients, and the precision matrixQQplays the role of the inverse covariance, governing the spread of the distribution. The result is an ODE system of the same type, finite-dimensional and integrable by any standard solver, that characterizes a non-Gaussian density in the way that mean and covariance characterize a Gaussian one.

## 2.2Physical Interpretation

Equation (4) governs the evolution of theshapeof the distribution. Its first term (−JF​f-J_{F}f) is pure advection: the contours of the PDF are transported along the deterministic flow, exactly as in the classical Liouville equation. The remaining terms represent the diffusion correction: process noise smoothly deforms the mapFF, stretching the distribution in directions dictated by the local geometry of the flow and the structure of the noise.

Equation (6) governs the evolution of theconcentrationof the distribution. The precision matrixQQdecreases over time (the distribution broadens) at a rate determined by the Hessian of the map, that is, by the local curvature of the nonlinear flow. This is a fundamentally different mechanism from simple covariance growth: the rate at which uncertainty spreads depends on the nonlinear structure of the dynamics throughJF−1J_{F}^{-1}andMiM_{i}.

For conservative dynamics (∇⋅f=0\nabla\cdot f=0), which includes Keplerian motion,μ\muremains identically constant (one can verify directly from (5) thatμ=1\mu=1with∇μ=0\nabla\mu=0and∇2μ=0\nabla^{2}\mu=0satisfies the equation when∇⋅f=0\nabla\cdot f=0). The evolution equation forμ\mutherefore drops out entirely, and the system reduces to the two-equation conservative form:∂F∂t\displaystyle\frac{\partial F}{\partial t}=−JF​f+12​(F​∑iαi+Q−1​∑iDi+Δ−Γ),\displaystyle=-J_{F}\,f+\frac{1}{2}\!\left(F\sum_{i}\alpha_{i}+Q^{-1}\!\sum_{i}D_{i}+\Delta-\Gamma\right),(9)d​Qd​t\displaystyle\frac{dQ}{dt}=12​∑iJF−⊤​JΛi⊤​Q​JΛi​JF−1.\displaystyle=\frac{1}{2}\sum_{i}J_{F}^{-\top}\,J_{\Lambda_{i}}^{\top}Q\,J_{\Lambda_{i}}\,J_{F}^{-1}.(10)

This is the system integrated in the Keplerian orbit application of Section3.

## 2.3Structural Preservation and Tail Modeling

The preservation of the structural form (3) under the full FPE dynamics has a direct practical consequence: the tails of the distribution are determined by the same finite set of parameters(F,Q)(F,Q)that describe the bulk. Once the augmented ODE system is integrated, the densityp​(x,t)p(x,t)can be evaluated at any point in state space, including at5​σ5\sigmaor10​σ10\sigmadeviations from the mode, at negligible additional cost. The non-Gaussian shape of the tails is encoded in the nonlinear mapFF, while their rate of decay is governed by the evolved precision matrixQQ: both are propagated self-consistently by the coupled dynamics.

This stands in contrast to moment-based methods (which truncate at order 2 or 4 and cannot reconstruct tail behavior), Gaussian mixture models (which require an increasing number of components to capture non-Gaussian tails), and Monte Carlo methods (which need exponentially more samples to resolve lower tail probabilities). For conjunction assessment, where the decision-relevant quantity is a collision probability on the order of10−510^{-5}, having a closed-form expression forp​(x,t)p(x,t)that is structurally consistent from the mode to the tails represents a significant operational advantage.

## 3Application: Keplerian Orbit

## 3.1Problem Setup

We apply the Taylor Diffusion algorithm to a spacecraft in an eccentric two-body orbit. The orbit is assumed to be planar, so the full state isX=[x,y,vx,vy]⊤∈ℝ4X=[x,\,y,\,v_{x},\,v_{y}]^{\top}\in\mathbb{R}^{4}. The equations of motion are expressed in non-dimensional units (gravitational parameterμg=1\mu_{g}=1, reference length and time chosen accordingly), giving the dynamics:f​(X)=(vxvy−x/r3−y/r3),r=x2+y2.f(X)=\begin{pmatrix}v_{x}\\
v_{y}\\
-x/r^{3}\\
-y/r^{3}\end{pmatrix},\qquad r=\sqrt{x^{2}+y^{2}}.(11)

The initial condition isX0=[1,0,0,0.8]⊤X_{0}=[1,\,0,\,0,\,0.8]^{\top}(apoapsis, sub-circular velocity, yielding an eccentric orbit with semi-major axisa≈0.74a\approx 0.74and periodT≈3.96T\approx 3.96). The initial PDF is an isotropic Gaussian withσinit=10−4\sigma_{\text{init}}=10^{-4}in all components. Additive process noise acts on velocity only:Σ0=diag​(0,0,σw2,σw2)\Sigma_{0}=\mathrm{diag}(0,\,0,\,\sigma_{w}^{2},\,\sigma_{w}^{2})withσw=10−4\sigma_{w}=10^{-4}. The propagation time istf=12​π≈37.7t_{f}=12\pi\approx 37.7, corresponding to approximately 9.5 complete orbits, a demanding test case in which the spacecraft traverses the strongly nonlinear periapsis region repeatedly, amplifying non-Gaussian distortions with each pass.

## 3.2Implementation

The mapFFis represented through its Taylor coefficients up to second order: the nominal trajectoryx0​(t)x_{0}(t), the JacobianJ​(t)∈ℝ4×4J(t)\in\mathbb{R}^{4\times 4}, and the Hessian tensorH​(t)∈ℝ4×4×4H(t)\in\mathbb{R}^{4\times 4\times 4}. This quadratic truncation captures the leading nonlinear distortion of the PDF; higher-order representations would extend the spatial range of accuracy at the cost of a larger augmented state. Together withQ​(t)∈ℝ4×4Q(t)\in\mathbb{R}^{4\times 4}, these form the augmented state{x0,J,H,Q}\{x_{0},J,H,Q\}, of total dimensionn+n2+n3+n​(n+1)/2=94n+n^{2}+n^{3}+n(n+1)/2=94scalar variables forn=4n=4.

The implementation leverages the key structural property that all quantities needed to advance the augmented state can be extracted from the map derivative functionF˙​(δ​x)\dot{F}(\delta x)evaluatedonly atδ​x=0\delta x=0. In particular, letV0=F˙​(0)V_{0}=\dot{F}(0),J˙=∂δ​xF˙|0\dot{J}=\partial_{\delta x}\dot{F}\big|_{0}, andH˙=∂δ​x2F˙|0\dot{H}=\partial^{2}_{\delta x}\dot{F}\big|_{0}; these three objects fully determine how the Taylor coefficients evolve. The nominal trajectoryx0x_{0}is advanced by the conditionF​(x0,t)=0F(x_{0},t)=0, which requiresx˙0=−J−1​V0\dot{x}_{0}=-J^{-1}V_{0}. SinceF˙\dot{F}depends onδ​x\delta xonly through the dynamicsf​(x0+δ​x)f(x_{0}+\delta x)and the polynomial map itself, all derivatives are computed automatically via forward-mode automatic differentiation444We utilize JAX[jax2018github]for all automatic differentiation and hardware acceleration., eliminating the need to derive the (prohibitively complex) 4D analytical expressions by hand.

Since Keplerian dynamics are conservative (∇⋅f=0\nabla\cdot f=0), the volume parameterμ=1\mu=1is constant and does not require integration. The complete procedure is summarized in Algorithm1.Algorithm 1Taylor Diffusion: augmented ODE integration1:Initial stateX0X_{0}, initial covarianceP0P_{0}, process noiseΣ0\Sigma_{0}, final timetft_{f}, stepsNN2:Augmented state(x0,f,Jf,Hf,Qf)(x_{0,f},\,J_{f},\,H_{f},\,Q_{f})encoding the PDF attft_{f}3:Initialize:x0←X0x_{0}\leftarrow X_{0},J←InJ\leftarrow I_{n},H←0H\leftarrow 0,Q←12​P0−1Q\leftarrow\tfrac{1}{2}P_{0}^{-1}4:fork=0,…,N−1k=0,\ldots,N-1do⊳\trianglerightRK4 time integration,Δ​t=tf/N\Delta t=t_{f}/N5:ComputeQ˙\dot{Q}:Q˙←12​∑iΣ0,i​J−⊤​Hα​i​β⊤​Q​Hα​i​β​J−1\displaystyle\dot{Q}\leftarrow\tfrac{1}{2}\sum_{i}\Sigma_{0,i}\,J^{-\top}H_{\alpha i\beta}^{\top}Q\,H_{\alpha i\beta}\,J^{-1}6:DefineF˙​(δ​x)\dot{F}(\delta x)per Eq. (9), usingF​(δ​x)=J​δ​x+12​H​(δ​x,δ​x)F(\delta x)=J\delta x+\tfrac{1}{2}H(\delta x,\delta x)7:Evaluate atδ​x=0\delta x=0(via automatic differentiation):V0\displaystyle V_{0}←F˙​(0),J˙←∂δ​xF˙|0+H⋅x˙0,H˙←∂δ​x2F˙|0\displaystyle\leftarrow\dot{F}(0),\quad\dot{J}\leftarrow\partial_{\delta x}\dot{F}\big|_{0}+H\cdot\dot{x}_{0},\quad\dot{H}\leftarrow\partial^{2}_{\delta x}\dot{F}\big|_{0}8:Zero tracking(enforceF​(x0)=0F(x_{0})=0):x˙0←−J−1​V0\dot{x}_{0}\leftarrow-J^{-1}V_{0}9:Propagation:(x0,J,H,Q)←RK4​-​step​(x˙0,J˙,H˙,Q˙,Δ​t)(x_{0},\,J,\,H,\,Q)\leftarrow\mathrm{RK4\text{-}step}(\dot{x}_{0},\,\dot{J},\,\dot{H},\,\dot{Q},\,\Delta t)10:endfor11:return(x0,f,Jf,Hf,Qf)(x_{0,f},\,J_{f},\,H_{f},\,Q_{f})

## 3.3Validation and Results

We validate the Taylor Diffusion PDF against a Monte Carlo ensemble of 400000 stochastic trajectories, each propagated via RK4 with Euler-Maruyama noise injection at 2000 time steps. The analytical PDF, encoded by(Jf,Hf,Qf)(J_{f},H_{f},Q_{f})at timetft_{f}, is sampled by drawing from𝒩​(0,(2​Qf)−1)\mathcal{N}(0,\,(2Q_{f})^{-1})in the map’s domain and applying the quadratic forward map.

A key point of comparison is computational cost. The Taylor Diffusion solver integrates an augmented ODE system of dimensionn+n2+n3+n​(n+1)/2n+n^{2}+n^{3}+n(n+1)/2(nominal trajectory, Jacobian, Hessian, and precision matrix), forn=4n=4, this amounts to 94 scalar ODEs555While the 4D state requires integrating 94 scalar ODEs, extending this framework to a full 6D orbital state yields an augmented system of 279 ODEs. This computational load remains trivially fast for modern numerical integrators, preserving the method’s stark operational advantage over Monte Carlo sampling.. This single integration, taking less than a second666The computing times have been measured on a11th Gen Intel(R) Core(TM) i7-1165G7CPU., produces the complete analytical description of the PDF at the final time. In contrast, the Monte Carlo validation required 400000 independent stochastic trajectory integrations, a computation that takes more than a minute, and still subject to sampling noise.

The results show close agreement between the Taylor Diffusion and Monte Carlo distributions across both position(x,y)(x,y)and velocity(vx,vy)(v_{x},v_{y})subspaces, even after 9.5 orbits of propagation. Fig.1compares the 2D marginal densities: the method correctly captures the non-Gaussian features induced by the1/r21/r^{2}gravitational nonlinearity, notably the strongly curved, banana-shaped distributions and asymmetric tails, while simultaneously reproducing the broadening due to cumulative stochastic forcing through the evolved precision matrixQfQ_{f}. Fig.2shows the 1D marginal distributions along each state component, demonstrating close correspondence in peak location, width, and asymmetry. The skewed tails visible inδ​x\delta xandδ​vy\delta v_{y}are characteristic of the nonlinear stretching at periapsis and are faithfully reproduced by the second-order Taylor map.Figure 1:Two-dimensional marginal PDFs attf=12​πt_{f}=12\pi(≈\approx9.5 orbits) for the eccentric Keplerian orbit. Left column: Monte Carlo SDE reference (400000 samples). Right column: Taylor Diffusion (second-order map with evolvedQQ). Top row: position subspace(δ​x,δ​y)(\delta x,\delta y). Bottom row: velocity subspace(δ​vx,δ​vy)(\delta v_{x},\delta v_{y}).Figure 2:One-dimensional marginal PDFs for each state component. Blue histograms: Monte Carlo SDE. Red curves: Taylor Diffusion. The close agreement across all four components, including the asymmetric tails inδ​x\delta xandδ​vy\delta v_{y}, confirms that the method captures the non-Gaussian structure induced by the nonlinear dynamics and stochastic forcing.

## 4Conclusions and Outlook

We have presented Taylor Map Diffusion, a framework that provides closed-form, grid-free solutions to the Fokker-Planck equation for nonlinear dynamical systems with additive Gaussian noise. The theoretical foundation is rigorous: the exponential-of-quadratic-form ansatz satisfies the FPE with zero residual under the derived coupled ODEs, with no approximation introduced at the continuous level. In practice, the mapFFis represented as a finite-order Taylor expansion, making the truncation order the single, transparent control parameter governing the accuracy of the computed density. Even at second order, the method captures the dominant nonlinear distortions of the PDF, including its non-Gaussian tails, while simultaneously and self-consistently accounting for the broadening effect of process noise through the evolved precision matrixQQ.

Applied to an eccentric Keplerian orbit propagated over 9.5 complete revolutions with continuous stochastic velocity perturbations, the method produces PDFs in close agreement with a 400000-sample Monte Carlo validation, while requiring only the integration of 94 coupled ODEs, with a single trajectory’s worth of computation. This disparity in computational cost grows with the number of Monte Carlo samples needed: resolving a10−510^{-5}tail probability to statistical significance typically requires10610^{6}-10710^{7}samples, whereas the Taylor Diffusion solution provides the density analytically at any point in state space, including arbitrarily deep into the tails.

The framework opens several directions for future work. A natural extension is to perturbed orbits with non-conservative forces (atmospheric drag, solar radiation pressure), which require evolving the volume parameterμ\muand would demonstrate the method’s full generality beyond the conservative case. Higher-order Taylor map expansions would extend accuracy to longer propagation horizons and stronger nonlinearities. Conjunction assessment is a direct target application: the closed-form density enables direct evaluation of collision probabilities in the distribution tails without resorting to sampling.

The present work considers a planar orbit; extension to the full three-dimensional case (six-dimensional state) is straightforward in principle, increasing the augmented ODE system from 94 to 279 scalar equations, still trivially fast for modern integrators. A more significant generalization concerns the choice of state representation. Cartesian coordinates, used here, are natural for the FPE but introduce strong nonlinearities over long arcs. A reformulation in terms of orbital elements, particularly non-singular sets such as the Generalized Equinoctial Orbital Elements (GEqOE)[Hernando2023], would reduce the effective nonlinearity of the flow map and thereby improve the accuracy of low-order Taylor expansions over many revolutions, while also simplifying the treatment of near-circular and near-equatorial orbits. The extension of the GEqOE framework to include continuous process noise, currently an open problem, is a natural target for the Taylor Diffusion mechanism developed here.

A further direction of considerable practical interest is nonlinear orbit determination. Many conventional filtering approaches are constrained by Gaussian approximations (e.g., extended and unscented Kalman filters). This formulation degrades significantly when measurement arcs are sparse and propagation times are long, which is exactly the regime where non-Gaussian effects become most pronounced. Taylor Map Diffusion provides a closed-form, non-Gaussian prior that can be updated analytically upon each measurement, offering a principled route to sequential orbit determination that remains tractable even with large temporal gaps between observations. The combination of mathematical rigor, systematic improvability through expansion order, and computational efficiency makes Taylor Map Diffusion a promising tool for next-generation Space Domain Awareness.

## Acknowledgments

This work was supported by the Air Force Office of Scientific Research (AFOSR) under Grant No. FA8655-25-1-7012.

## References

## 


- 


Major funding support from
