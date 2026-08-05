# A Systematic Benchmark of Physics-Informed Neural Network Architectures for the Stiff Poisson-Nernst-Planck System: Adaptive LossWeighting and Multi-Scale Resolution

**arXiv ID**: 2606.04125v1
**Authors**: David Pankaczy, Conrard Giresse Tetsassi Feugmo
**Published**: 2026-06-02
**Categories**: physics.app-ph, math-ph, physics.comp-ph
**HTML URL**: https://arxiv.org/html/2606.04125v1

## Abstract

The Poisson Nernst Planck PNP system constitutes a canonical stiff coupled PDE problem where the charge density prefactor produces extreme coefficient ratios and the electric double layer imposes sharp boundary layers. Physics informed neural networks PINNs are appealing here because they require no mesh and differentiate through the physics automatically. Spectral bias and multi task loss imbalance however have limited their accuracy on stiff PNP systems. We present the first systematic data free benchmark of eleven PINN configurations organised into four strategy groups on a physically parametrised one dimensional PNP model for a lithium symmetric cell implemented within NVIDIA PhysicsNeMo Sym and validated against a finite volume method FVM reference. Root mean square errors RMSE span across architectures. The balanced residual decay rate BRDR scheme matches Neural Tangent Kernel NTK performance for concentration fields while reducing mean wall clock time making it the preferable strategy under compute constraints. Loss landscape geometry corroborates the RMSE ranking. We release an open source PhysicsNeMo Sym implementation for reuse on stiff coupled PDE problems in computational mechanics.

## Full Text

A Systematic Benchmark of Physics-Informed Neural Network Architectures for the Stiff Poisson–Nernst–Planck System: Adaptive Loss Weighting and Multi-Scale Resolution

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
- License: CC BY 4.0arXiv:2606.04125v1 [physics.app-ph] 02 Jun 2026

## A Systematic Benchmark of Physics-Informed Neural Network
Architectures for the Stiff Poisson–Nernst–Planck System:
Adaptive Loss Weighting and Multi-Scale ResolutionDavid Pankaczy1
1Department of Physics and AstronomyUniversity of Waterloo200 University Ave. WestWaterloo, ON N2L 3G1, Canadadpankacz@uwaterloo.caConrard Giresse Tetsassi Feugmo1,2,∗
1Department of Physics and Astronomy2Department of ChemistryUniversity of Waterloo200 University Ave. WestWaterloo, ON N2L 3G1, Canada∗cgtetsas@uwaterloo.ca

## Abstract

The Poisson–Nernst–Planck (PNP) system constitutes a canonical stiff coupled
PDE problem: the charge-density prefactorF/ε0≈1016F/\varepsilon_{0}\approx 10^{16}C V-1m-3produces extreme coefficient ratios, the electric double layer imposes sharp
boundary layers with a singular-perturbation character, and the Poisson and
Nernst–Planck equations are nonlinearly coupled.
Physics-informed neural networks (PINNs) are appealing here because they require no
mesh, differentiate through the physics automatically, and handle forward and inverse
problems in one framework. Spectral bias and multi-task loss imbalance, however, have
limited their accuracy on stiff PNP systems.
We present the first systematic, data-free benchmark of eleven PINN configurations,
organised into four strategy groups (adaptive loss weighting, spectral bias mitigation,
spatio-temporal decomposition, and physics enrichment), on a physically parametrised
one-dimensional PNP model for a lithium symmetric cell, implemented entirely within
NVIDIA PhysicsNeMo Sym and validated against a finite volume method (FVM) reference.
Root-mean-square errors (RMSE) span10−210^{-2}–10−410^{-4}across architectures:
Neural Tangent Kernel (NTK) adaptive loss weighting achieves
RMSE=6.6×10−4=6.6\times 10^{-4}(anion),6.2×10−46.2\times 10^{-4}(cation), and1.1×10−31.1\times 10^{-3}(electric potential).
The balanced residual decay rate (BRDR) scheme matches NTK within 10% of RMSE
for the concentration fields (24% for the electric potential)
while reducing mean wall-clock time by3.2±0.43.2\pm 0.4h per run, making it the
preferable strategy under compute constraints.
Loss landscape geometry corroborates the RMSE ranking: NTK yields the sharpest,
most symmetric basin, while poorly conditioned architectures such as Separable PINNs (SPINNs) exhibit
flat, irregular landscapes.
We release an open-source PhysicsNeMo Sym implementation for reuse on stiff coupled
PDE problems in computational mechanics.

Keywords:physics-informed neural networks; Poisson–Nernst–Planck equations; adaptive loss weighting; neural tangent kernel; finite volume method; scientific machine learning

## 1Introduction

The Poisson–Nernst–Planck (PNP) system is a prototypical example of a stiff,
nonlinearly coupled PDE problem that challenges classical and modern numerical
solvers alike.
The dimensionless form of the system, derived in Section3, admits
a singular-perturbation structure controlled by the parameterε∝λD/L\varepsilon\propto\lambda_{D}/L, whereλD\lambda_{D}is the Debye screening length
andLLis the domain length.
For typical electrochemical parameters,ε≪1\varepsilon\ll 1(ε≈10−4\varepsilon\approx 10^{-4}–10−510^{-5}for concentrated electrolytes), which forces sharp boundary
layers at the electrode interfaces that classical finite element codes address
through Slotboom variable transformations, Gummel-iteration decoupling, and
locally refined meshes[XIE2020109915].
At the same time, the extreme charge-density prefactorF/ε0≈1.09×1016F/\varepsilon_{0}\approx 1.09\times 10^{16}C V-1m-3creates coefficient ratios that
destabilize standard iterative solvers[Bazant2004].
The physical application motivating this work is ion transport in a one-dimensional
lithium symmetric cell with\chLiPF6 electrolyte, which provides a parametrically
well-documented and experimentally validated instance of the PNP system[Subramariam2019,Wood2016-yf,Newman2004], and the same equations govern
ion channels[Eisenberg1996], nanofluidic devices[Daiguji2004], and
solid-state ionic transport[Bazant2004].

Neural networks for solving PDEs were first proposed byLagaris1998ANN;
the modern physics-informed neural network (PINN) framework ofRAISSI2019686placed this on a rigorous automatic differentiation footing and has since become a
leading paradigm in scientific machine learning[Karniadakis2021review,Cuomo2022,EYu2018deep].
PINNs are attractive for stiff coupled PDEs because they require no mesh, differentiate
through physical laws automatically, and accommodate operator-learning extensions[Wang2021DeepONets].
However, two fundamental difficulties limit their accuracy on PNP-class problems.
The first isspectral bias: PINNs preferentially learn low-frequency
components of the solution, making the stiff, higher-frequency Poisson equation
difficult to resolve[rahaman2019spectralbias,xu2019fprinciple,Krishnapriyan2021failure].
The second ismulti-task loss imbalance: because the PNP system couples
equations with vastly different characteristic scales, the individual loss
components converge at different rates, and naive uniform weighting causes the
optimizer to over-satisfy the smoother Nernst–Planck equations at the expense
of the stiffer Poisson equation[WANG2022110768,Wang2021understanding,Wang2024causality].
Rigorous error bounds for PINNs on elliptic and parabolic PDEs have been established
byShin2020convergenceand generalisation error estimates byMishra2022estimates,Mishra2023forward,DeRyck2022PINNerror; however, none of
these analyses address the regime of extreme coefficient ratios (ε2∼10−10\varepsilon^{2}\sim 10^{-10}) characteristic of the PNP system studied here.

Prior PINN work on PNP has not adequately resolved either difficulty at
practically useful accuracy.HUANG2025231proposed data-free enriched PINNs for dynamic PNP systems
and demonstrated accuracy improvements over vanilla PINNs, but did not conduct a
systematic multi-architecture benchmark under battery-relevant parametrisation.
No systematic, data-free, multi-architecture benchmark exists for the PNP system
under battery-relevant parametrisation.

This paper closes that gap.
We benchmark eleven PINN configurations, organised into four strategy groups, against
a validated FVM reference on the one-dimensional PNP system ofSubramariam2019,
implemented entirely within NVIDIA’s open-source PhysicsNeMo Sym framework[physicsnemo2024].
The four groups are:adaptive loss weighting(NTK, BRDR, AdaHessian), which corrects
gradient pathologies without changing the network architecture;spectral bias mitigation(Fourier features, PIKAN), which modifies the network’s input representation or basis functions
to resolve high-frequency boundary layers;spatio-temporal decomposition(FBPINN,
Decoupled, SPINN, Sym./antisym. transform), which reduces problem complexity by splitting the
domain, the equations, or the solution variables; andphysics enrichment(EPINN),
which embeds stiff analytical features directly into the network basis.
The specific contributions are as follows.
We provide the first systematic, data-free benchmark of eleven PINN configurations spanning
four methodological groups on a physically parametrised 1D PNP system, with errors averaged
over ten independent training runs per configuration.
We show that NTK adaptive loss weighting achieves RMSE as low as6.6×10−46.6\times 10^{-4}(dimensionless), while BRDR weighting matches this within 9% at reduced
computational cost.
A loss landscape analysis provides geometric corroboration of the RMSE ranking;
wall-time distributions characterise all eleven configurations on an NVIDIA H100 GPU.
We also release an open-source, modular PhysicsNeMo Sym implementation for PNP
problems and, more broadly, for stiff coupled PDE systems in computational electrochemistry.

## 2Developments in Physics-Informed Neural Networks

SinceRAISSI2019686introduced the modern PINN framework, spectral bias[rahaman2019spectralbias]and multi-task loss imbalance have been the main
obstacles, and both are especially acute for the PNP system studied here.
Spectral bias arises because standard multilayer perceptrons (MLPs) preferentially
fit low-frequency, global trends, leaving high-frequency localised features such
as the electric double layer (EDL) unresolved.
Loss imbalance arises because stiff multiphysics systems impose loss components
with disparate magnitudes and convergence rates, so that a uniform weighting
neglects the stiffest equations.

Tancik2020FourierFeaturesshow that Fourier feature mappings applied to
the input layer enable learning of high-frequency components for low-dimensional
problems;Wang2021eigenextend this by analysing the eigenvalue structure
of the resulting NTK and proposing modified Fourier networks.Wang2021understandingidentify gradient flow pathologies as the root
cause of PINN training failure on multiphysics problems, andWANG2022110768develop NTK-based adaptive loss weighting, grounded in
the infinite-width NTK theory ofJacot2018NTK, which equates convergence
rates across loss components and substantially improves accuracy on multi-scale and
nonlinear systems.
Domain-decomposition approaches, originally proposed as conservative PINNs byJagtap2020conservativeand extended to finite basis PINNs (FBPINNs)
byMoseley2023FBPINNswith multilevel decomposition byDOLEAN2024117116, address both spectral bias and the
global-communication bottleneck between subdomains.
Separable PINNs[Cho2023SPINNs]reduce memory requirements by canonical polyadic (CP) tensor
decomposition but sacrifice accuracy on problems where coupling between spatial
dimensions is strong.
Kolmogorov–Arnold networks (KANs)[liu2025kan], implemented for PDE solving
as PIKANs byWANG2025PIKAN, offer theoretical advantages over MLPs but
exhibit increased inference cost due to basis function computation.McClenny2023selfadaptiveintroduce per-collocation-point trainable weights
(self-adaptive PINNs) as a further adaptive strategy.CHEN2025BRDRpropose the balanced residual decay rate (BRDR) method,
demonstrating accuracy comparable to NTK weighting at lower computational cost.
Second-order optimisation via AdaHessian[Yao2021AdaHessian]provides
curvature information through Hutchinson’s estimator, offering an alternative
convergence path.
Our benchmark evaluates all of these strategies on the same PNP problem, providing
the first head-to-head comparison on a stiff, nonlinearly coupled system with
physical parametrisation.

## 3Poisson–Nernst–Planck Model

## 3.1Dimensional PNP system

Our base-case system is the one-dimensional PNP transport model ofSubramariam2019, which describes the mean-field dynamics of a binary
electrolyte (\chLiPF6) in a lithium symmetric cell.
The model solves for the cation concentrationCpC_{p}(\chLi+), anion
concentrationCnC_{n}(\chPF6-), and electric potentialΦ\Phi.
The dimensional governing equations, boundary conditions (BCs), and initial
condition (IC) are collected in Table1; physical parameters are
given in Table2.
The cell geometry is illustrated in Figure1.Table 1:Dimensional PNP system.Interior PDE, boundary conditions (BCs), and initial condition (IC) for the
cation concentrationCpC_{p}, anion concentrationCnC_{n}, and electric potentialΦ\Phi. Both electrode interfaces impose identical flux BCs; the right BC for
each field is identical in form to the left BC.Interior PDELeft BC (X=0X=0)Right BCIC∂2Φ∂X2=−Fε0​εs​(zp​Cp+zn​Cn)\displaystyle\frac{\partial^{2}\Phi}{\partial X^{2}}=-\frac{F}{\varepsilon_{0}\varepsilon_{s}}(z_{p}C_{p}+z_{n}C_{n})∂Φ∂X=0\displaystyle\frac{\partial\Phi}{\partial X}=0Φ=0\Phi=0Φ=0\Phi=0∂Cp∂𝒯=Dp​∂2Cp∂X2+zp​Dp​FR​T​∂∂X​(Cp​∂Φ∂X)\displaystyle\frac{\partial C_{p}}{\partial\mathcal{T}}=D_{p}\frac{\partial^{2}C_{p}}{\partial X^{2}}+\frac{z_{p}D_{p}F}{RT}\frac{\partial}{\partial X}\!\left(C_{p}\frac{\partial\Phi}{\partial X}\right)−Dp​∂Cp∂X−zp​Dp​FR​T​Cp​∂Φ∂X=Iappzp​F\displaystyle-D_{p}\frac{\partial C_{p}}{\partial X}-\frac{z_{p}D_{p}F}{RT}C_{p}\frac{\partial\Phi}{\partial X}=\frac{I_{\mathrm{app}}}{z_{p}F}same as leftCp=C0C_{p}=C_{0}∂Cn∂𝒯=Dn​∂2Cn∂X2+zn​Dn​FR​T​∂∂X​(Cn​∂Φ∂X)\displaystyle\frac{\partial C_{n}}{\partial\mathcal{T}}=D_{n}\frac{\partial^{2}C_{n}}{\partial X^{2}}+\frac{z_{n}D_{n}F}{RT}\frac{\partial}{\partial X}\!\left(C_{n}\frac{\partial\Phi}{\partial X}\right)−Dn​∂Cn∂X−zn​Dn​FR​T​Cn​∂Φ∂X=0\displaystyle-D_{n}\frac{\partial C_{n}}{\partial X}-\frac{z_{n}D_{n}F}{RT}C_{n}\frac{\partial\Phi}{\partial X}=0same as leftCn=C0C_{n}=C_{0}Table 2:Physical parameters for\chLiPF6 in a lithium symmetric
cell[Subramariam2019].
The diffusivity ratioDn/Dp=10D_{n}/D_{p}=10and the small Debye-to-domain-length
ratioε≈2.3×10−5\varepsilon\approx 2.3\times 10^{-5}are the primary sources of
stiffness.SymbolValueUnitsDescriptionC0C_{0}500500mol m-3Initial electrolyte concentrationDpD_{p}4×10−104\times 10^{-10}m2s-1Diffusivity of\chLi+DnD_{n}4×10−94\times 10^{-9}m2s-1Diffusivity of\chPF6-zpz_{p}11—Cation charge numberznz_{n}−1-1—Anion charge numberIappI_{\mathrm{app}}7.727.72A m-2Applied current density (chosen to giveδ=0.3\delta=0.3)εs\varepsilon_{s}16.816.8—Relative permittivity of solventTT298.15298.15KTemperatureLL7.5×10−47.5\times 10^{-4}mInter-electrode distance𝒯f\mathcal{T}_{f}3 6003\,600sFinal simulation timeλD\lambda_{D}≈1.7×10−8\approx 1.7\times 10^{-8}mDebye length (ε≈2.3×10−5\varepsilon\approx 2.3\times 10^{-5})

## 3.2Nondimensionalisation and conditioning

Nondimensionalisation is essential for PINN training: dimensional variables span
orders of magnitude that produce ill-conditioned loss functions and impede
convergence[Haghighat2021,Markidis2021].
We adopt the scheme ofSubramariam2019:cp=Cp/C0,cn=Cn/C0,φ=Φ​F/(R​T)\displaystyle c_{p}=C_{p}/C_{0},\quad c_{n}=C_{n}/C_{0},\quad\varphi=\Phi F/(RT)(1)x=X/L,t=𝒯​Dp/L2\displaystyle x=X/L,\quad t=\mathcal{T}\,D_{p}/L^{2}(2)ε=R​T​ε0​εszp2​F2​C0​L2,δ=Iappzp​F​C0​Dp/L,ξ=DnDp\displaystyle\varepsilon=\sqrt{\frac{RT\varepsilon_{0}\varepsilon_{s}}{z_{p}^{2}F^{2}C_{0}L^{2}}},\quad\delta=\frac{I_{\mathrm{app}}}{z_{p}FC_{0}D_{p}/L},\quad\xi=\frac{D_{n}}{D_{p}}(3)

whereε\varepsilonis the ratio of the Debye screening lengthλD\lambda_{D}to the
domain lengthLL(the singular-perturbation parameter),δ\deltais the
dimensionless applied current, andξ=Dn/Dp=10\xi=D_{n}/D_{p}=10is the diffusivity ratio.
For the parameters of Table2these evaluate toε≈2.30×10−5\varepsilon\approx 2.30\times 10^{-5}andδ=0.3\delta=0.3;IappI_{\mathrm{app}}is set to7.727.72A m-2(slightly below the1010A m-2of[Subramariam2019]) so thatδ=0.3\delta=0.3serves
as the canonical dimensionless current for all PINN and FVM computations
in this benchmark.
The dimensionless system is given in Table3.

The parameterε≈2.30×10−5\varepsilon\approx 2.30\times 10^{-5}is small, which means the
Poisson equation−ε2​φx​x=zp​cp+zn​cn-\varepsilon^{2}\varphi_{xx}=z_{p}c_{p}+z_{n}c_{n}has a
coefficientε2≈5.3×10−10\varepsilon^{2}\approx 5.3\times 10^{-10}: the electric potential
must satisfy this equation with a coefficient ten orders of magnitude smaller than
unity, creating the loss imbalance that is the central computational difficulty
for all PINN configurations tested.Table 3:Dimensionless PNP system.Derived from the nondimensionalisation
 (1)–(3).
The small parameterε≈2.3×10−5\varepsilon\approx 2.3\times 10^{-5}controls the
sharpness of the electric double layer atx=0x=0andx=1x=1.InteriorLeft BCRight BCIC−ε2​∂2φ∂x2=zp​cp+zn​cn\displaystyle-\varepsilon^{2}\frac{\partial^{2}\varphi}{\partial x^{2}}=z_{p}c_{p}+z_{n}c_{n}∂φ∂x=0\displaystyle\frac{\partial\varphi}{\partial x}=0φ=0\varphi=0φ=0\varphi=0∂cp∂t=∂2cp∂x2+zp​∂∂x​(cp​∂φ∂x)\displaystyle\frac{\partial c_{p}}{\partial t}=\frac{\partial^{2}c_{p}}{\partial x^{2}}+z_{p}\frac{\partial}{\partial x}\!\left(c_{p}\frac{\partial\varphi}{\partial x}\right)−∂cp∂x−zp​cp​∂φ∂x=δ\displaystyle-\frac{\partial c_{p}}{\partial x}-z_{p}c_{p}\frac{\partial\varphi}{\partial x}=\delta−∂cp∂x−zp​cp​∂φ∂x=δ\displaystyle-\frac{\partial c_{p}}{\partial x}-z_{p}c_{p}\frac{\partial\varphi}{\partial x}=\deltacp=1c_{p}=1∂cn∂t=ξ​[∂2cn∂x2+zn​∂∂x​(cn​∂φ∂x)]\displaystyle\frac{\partial c_{n}}{\partial t}=\xi\!\left[\frac{\partial^{2}c_{n}}{\partial x^{2}}+z_{n}\frac{\partial}{\partial x}\!\left(c_{n}\frac{\partial\varphi}{\partial x}\right)\right]−∂cn∂x−zn​cn​∂φ∂x=0\displaystyle-\frac{\partial c_{n}}{\partial x}-z_{n}c_{n}\frac{\partial\varphi}{\partial x}=0−∂cn∂x−zn​cn​∂φ∂x=0\displaystyle-\frac{\partial c_{n}}{\partial x}-z_{n}c_{n}\frac{\partial\varphi}{\partial x}=0cn=1c_{n}=1Figure 1:Schematic of the one-dimensional lithium symmetric cell.The computational domain (x∈[0,1]x\in[0,1]) spans the\chLiPF6 electrolyte
between two identical lithium metal electrodes.
Under the applied positive current densityIappI_{\mathrm{app}}, the cation
(\chLi+,cpc_{p}) migrates toward the cathode (x=1x=1) driven by the electric
field.
The anion (\chPF6-,cnc_{n}) carries zero net flux at both electrode
interfaces (no-flux boundary condition); it accumulates nearx=0x=0as
electromigration and diffusion balance inside the electric double layer.
The electric potentialφ\varphiis the third solved field.
Thin bands at both interfaces represent the electric double layer of
dimensionless thicknessO​(ε)≈2.3×10−5O(\varepsilon)\approx 2.3\times 10^{-5}.

## 3.3Finite volume reference solver

The reference solution is obtained by amethod of lines(MOL) solver
implemented in Python (pnp_fvm.py).
The spatial domainx∈[0,1]x\in[0,1]is discretised on a uniform grid ofNFVM=500N_{\mathrm{FVM}}=500cell-centred nodes with spacingh=1/NFVM=2×10−3h=1/N_{\mathrm{FVM}}=2\times 10^{-3}.
At each time step the Poisson equation in Table3is solved algebraically
as a(NFVM+1)×(NFVM+1)(N_{\mathrm{FVM}}+1)\times(N_{\mathrm{FVM}}+1)tridiagonal linear system
(numpy.linalg.solve), with the left Neumann condition∂xφ|x=0=0\partial_{x}\varphi|_{x=0}=0discretised by a first-order one-sided difference
and the right Dirichlet conditionφ​(1,t)=0\varphi(1,t)=0imposed directly.
Ion fluxes are approximated at cell faces using centered differences for
concentration gradients and arithmetic-average face concentrations, consistent
with the standard cell-centred finite-volume flux:Np(j+12)=−cp(j+1)−cp(j)h−c¯p(j+12)​φ(j+1)−φ(j)h,N_{p}^{(j+\frac{1}{2})}=-\frac{c_{p}^{(j+1)}-c_{p}^{(j)}}{h}-\bar{c}_{p}^{(j+\frac{1}{2})}\frac{\varphi^{(j+1)}-\varphi^{(j)}}{h},(4)

and analogously forNnN_{n}.
The resulting stiff ODE system for the2​(NFVM+1)2(N_{\mathrm{FVM}}+1)concentration
variables is integrated in time byscipy.integrate.solve_ivpwith
theRadauimplicit Runge–Kutta solver (order 5,
tolerances𝚛𝚝𝚘𝚕=10−6\mathtt{rtol}=10^{-6},𝚊𝚝𝚘𝚕=10−8\mathtt{atol}=10^{-8}), which is
well-suited to the stiff eigenvalue spectrum arising from theε−2\varepsilon^{-2}coefficient in the Poisson equation.
The boundary flux is set toδ=0.3\delta=0.3(Iapp≈7.72I_{\mathrm{app}}\approx 7.72A m-2),
matching the value used in all PINN configurations.
The solution is evaluated at3 6003\,600uniformly spaced times on[0,τf≈2.56][0,\,\tau_{f}\approx 2.56], yielding a space-time dataset of3 600×5013\,600\times 501points for each of the three fields (cpc_{p},cnc_{n},φ\varphi)
written topnp.csv.
The spatial discretisation error, estimated by Richardson extrapolation betweenN=250N=250andN=500N=500grids, isO​(h2)≈4×10−6O(h^{2})\approx 4\times 10^{-6},
at least two orders of magnitude below the best PINN RMSE (6.6×10−46.6\times 10^{-4}),
so the MOL solution is a reliable benchmark reference.
A full derivation of the discrete equations, boundary conditions, and solver
parameters is given in Supplementary Material Section 1.
Existence and uniqueness of the continuous PNP solution for the parameter regime
studied here follows fromJerome1996analysis.

## 4PINN Benchmark Design and Training Configurations

## 4.1Physics-informed neural networks

Universal approximation theorems[Hornik1989,Cybenko1989]guarantee that a
sufficiently expressive neural network can approximate any continuous function to
arbitrary precision.
PINNs exploit this by embedding physical laws directly into the loss function via
automatic differentiation (AD), which removes the need for a mesh.
Formally, the PINN problem (5)–(6) is:θ∗=arg⁡minθ⁡ℒ​(θ)\displaystyle\theta^{\ast}=\arg\min_{\theta}\mathcal{L}(\theta)(5)θn+1←θn−αn​∇θℒ​(θn)\displaystyle\theta_{n+1}\leftarrow\theta_{n}-\alpha_{n}\nabla_{\theta}\mathcal{L}(\theta_{n})(6)

whereθ\thetadenotes network parameters,αn\alpha_{n}is the learning rate at
iterationnn, and Adam[Kingma2014]provides adaptive per-parameter learning
rates.

The composite loss for the PNP system is:ℒ​(θ)=λPDE​ℒPDE+λBC​ℒBC+λIC​ℒIC\mathcal{L}(\theta)=\lambda_{\mathrm{PDE}}\,\mathcal{L}_{\mathrm{PDE}}+\lambda_{\mathrm{BC}}\,\mathcal{L}_{\mathrm{BC}}+\lambda_{\mathrm{IC}}\,\mathcal{L}_{\mathrm{IC}}(7)

whereℒPDE\mathcal{L}_{\mathrm{PDE}},ℒBC\mathcal{L}_{\mathrm{BC}}, andℒIC\mathcal{L}_{\mathrm{IC}}are the mean-squared PDE residual, boundary condition
residual, and initial condition residual, respectively.
The weightsλi\lambda_{i}are either fixed at unity (vanilla) or adaptively
determined at each training step by one of the two adaptive schemes described
in Section4.2.

## 4.2PhysicsNeMo Sym framework

All implementations use NVIDIA’s open-source PhysicsNeMo Sym framework[physicsnemo2024], formerly NVIDIA Modulus Sym, built on PyTorch.
The framework has four features that are central to the benchmark design.

Computational graph and automatic differentiation.Computations are organised as a directed acyclic graph ofNodeobjects,
each encapsulating a network or a physics equation with namedKeyvariables.
TheGraphclass resolves inter-node dependencies and, in a single forward
pass, computes all PDE residuals via backward-mode AD[Baydin2018AD],
without any symbolic manipulation.

Constraint system and Halton collocation.Typed constraint classes (InteriorConstraint,BoundaryConstraint,InitialCondition) encapsulate point sampling and loss computation.
Points are sampled using quasirandom Halton sequences[Halton1960], which
provide better space-filling coverage andO​(N−1​(log⁡N)d)O(N^{-1}(\log N)^{d})quasi-Monte Carlo
convergence compared to theO​(N−1/2)O(N^{-1/2})rate of independent uniform random
sampling[Caflisch1998].
Interior and boundary points are resampled at every training iteration with a
10:1 interior-to-boundary ratio; the precise collocation counts for each
configuration are reported in Table4.
We note that residual-based adaptive sampling strategies, which redistribute
collocation points toward high-residual regions and have been shown to substantially
improve accuracy for problems with sharp features[Wu2023newsampling,lu2021deepxde],
were not employed in this benchmark to isolate the effect of
architecture and loss-weighting choice.
Given the boundary layer of dimensionless thicknessO​(ε)≈2.3×10−5O(\varepsilon)\approx 2.3\times 10^{-5}, adaptive sampling is expected to yield additional accuracy
gains and is identified as a priority for future work.

Adaptive loss weighting.The three weighting-group configurations address loss imbalance at different
computational costs.
Let𝒞={ℒ1,…,ℒN}\mathcal{C}=\{\mathcal{L}_{1},\dots,\mathcal{L}_{N}\}denote the set of
scalar loss components (PDE, BC, IC residuals),θ∈ℝP\theta\in\mathbb{R}^{P}the
network parameters, andλi\lambda_{i}the weight for componentiiso thatℒ=∑iλi​ℒi\mathcal{L}=\sum_{i}\lambda_{i}\mathcal{L}_{i}.

NTK weighting[WANG2022110768,Wang2021understanding]is grounded in
the infinite-width Neural Tangent Kernel theory ofJacot2018NTK.
In finite-width practice the per-constraint NTK trace is approximated by the
squared gradient norm of the square-root loss, computed via a single backward pass:Ki(NTK)=‖∂ℒi∂θ‖22=∑p=1P(∂ℒi∂θp)2K_{i}^{(\mathrm{NTK})}=\left\lVert\frac{\partial\sqrt{\mathcal{L}_{i}}}{\partial\theta}\right\rVert_{2}^{2}=\sum_{p=1}^{P}\left(\frac{\partial\sqrt{\mathcal{L}_{i}}}{\partial\theta_{p}}\right)^{\!2}(8)

Weights are set so that each constraint drives parameter updates at the same
effective rate:K¯=1N​∑j=1NKj(NTK),λi←K¯Ki(NTK)\bar{K}=\frac{1}{N}\sum_{j=1}^{N}K_{j}^{(\mathrm{NTK})},\qquad\lambda_{i}\;\leftarrow\;\frac{\bar{K}}{K_{i}^{(\mathrm{NTK})}}(9)

A largeKi(NTK)K_{i}^{(\mathrm{NTK})}indicates that lossiialready drives large
parameter updates; its weight is reduced to balance the slower-converging
constraints.
In this benchmark traces are recomputed every 10 gradient steps
(see Algorithm1).

BRDR weighting[CHEN2025BRDR]replaces the gradient trace with
cheaper scalar residual statistics.
An exponential moving average (EMA) of the squared loss tracks each component’s
running scale (the4th-moment proxy), from which an inverse relative
decay rate is formed:m^i(n)=βc​mi(n−1)+(1−βc)​ℒi21−βcn,w^i(n)=ℒi(n)m^i(n)+ϵstab\hat{m}_{i}^{(n)}=\frac{\beta_{c}\,m_{i}^{(n-1)}+(1-\beta_{c})\,\mathcal{L}_{i}^{2}}{1-\beta_{c}^{n}},\qquad\hat{w}_{i}^{(n)}=\frac{\mathcal{L}_{i}^{(n)}}{\sqrt{\hat{m}_{i}^{(n)}}+\epsilon_{\mathrm{stab}}}(10)

A loss that decays slowly relative to its own running average receives a largerw^i\hat{w}_{i}.
The weights are then normalised, EMA-smoothed, and rescaled to maintain a
mean of unity across all constraints:w~i(n)=w^i(n)w^¯(n)+ϵstab,λi(n)=βw​λi(n−1)+(1−βw)​w~i(n)1N​∑j[βw​λj(n−1)+(1−βw)​w~j(n)]+ϵstab\tilde{w}_{i}^{(n)}=\frac{\hat{w}_{i}^{(n)}}{\bar{\hat{w}}^{(n)}+\epsilon_{\mathrm{stab}}},\qquad\lambda_{i}^{(n)}=\frac{\beta_{w}\,\lambda_{i}^{(n-1)}+(1-\beta_{w})\,\tilde{w}_{i}^{(n)}}{\tfrac{1}{N}\sum_{j}[\beta_{w}\,\lambda_{j}^{(n-1)}+(1-\beta_{w})\,\tilde{w}_{j}^{(n)}]+\epsilon_{\mathrm{stab}}}(11)

withβc=βw=0.999\beta_{c}=\beta_{w}=0.999andϵstab=10−14\epsilon_{\mathrm{stab}}=10^{-14}.
No backward pass beyond the standard gradient step is required.

AdaHessian[Yao2021AdaHessian]replaces the squared-gradient
second moment of Adam with a diagonal Hessian curvature estimate.
The diagonal of the Hessian∇2ℒ\nabla^{2}\mathcal{L}is approximated
via Hutchinson’s stochastic estimator[Hutchinson1989]using a
Rademacher random vector𝐯∼𝒰​{±1}P\mathbf{v}\sim\mathcal{U}\{\pm 1\}^{P}:H~p​p=vp​(∇2ℒ⋅𝐯)p,p=1,…,P\tilde{H}_{pp}=v_{p}\,\bigl(\nabla^{2}\mathcal{L}\cdot\mathbf{v}\bigr)_{p},\qquad p=1,\dots,P(12)

This is obtained without forming the full Hessian by computing a
Hessian-vector product through a second-order backpropagation.
The parameter update rule mirrors Adam but withH~p​p2\tilde{H}_{pp}^{2}in place ofgp2g_{p}^{2}for the second moment:m^p(n)\displaystyle\hat{m}_{p}^{(n)}=β1​mp(n−1)+(1−β1)​gp(n)1−β1n\displaystyle=\frac{\beta_{1}\,m_{p}^{(n-1)}+(1-\beta_{1})\,g_{p}^{(n)}}{1-\beta_{1}^{n}}(bias-corrected gradient EMA)(13)v^p(n)\displaystyle\hat{v}_{p}^{(n)}=β2​vp(n−1)+(1−β2)​(H~p​p(n))21−β2n\displaystyle=\frac{\beta_{2}\,v_{p}^{(n-1)}+(1-\beta_{2})\,(\tilde{H}_{pp}^{(n)})^{2}}{1-\beta_{2}^{n}}(bias-corrected Hessian EMA)(14)θp(n+1)\displaystyle\theta_{p}^{(n+1)}=θp(n)−αn​m^p(n)v^p(n)+ϵ\displaystyle=\theta_{p}^{(n)}-\alpha_{n}\,\frac{\hat{m}_{p}^{(n)}}{\sqrt{\hat{v}_{p}^{(n)}}+\epsilon}(parameter update)(15)

wheregp(n)=∂ℒ/∂θpg_{p}^{(n)}=\partial\mathcal{L}/\partial\theta_{p}is the standard gradient.
When curvatureH~p​p\tilde{H}_{pp}is large the effective step size is reduced,
providing implicit pre-conditioning without storing the full Hessian matrix.
Compared to NTK and BRDR, AdaHessian modifies theoptimizerrather than
the loss weights, and uses(β1,β2)=(0.9,0.999)(\beta_{1},\beta_{2})=(0.9,0.999)as in Adam.

Gradient accumulation.To simulate larger effective batch sizes without proportional GPU memory cost,
gradients are accumulated overKacc=4K_{\mathrm{acc}}=4forward/backward passes before each
optimizer step, effectively quadrupling the batch size.

The complete pipeline is summarised in Figure2.Figure 2:PhysicsNeMo Sym computational pipeline.Halton collocation points are fed to the neural network architecture (left);
automatic differentiation (AD) through theGraphcomputes PDE, boundary condition (BC),
and initial condition (IC) residuals (centre-left); Neural Tangent Kernel (NTK) or balanced
residual decay rate (BRDR) adaptive weighting rescales individual loss
components before aggregation to total lossℒ\mathcal{L}(centre-right);
gradients accumulate overKacc=4K_{\mathrm{acc}}=4passes before the Adam or
AdaHessian optimizer updates parametersθ\theta(right).
The dashed arrow represents the backpropagation loop.

## 4.3PINN architectures and training configurations

Table4organises the eleven configurations into four strategy
groups plus a vanilla baseline.
The grouping reflects the primary mechanism each configuration exploits, rather than
the underlying network architecture: four configurations (Vanilla, EPINN, FBPINN,
PIKAN) constitute distinct network architectures, while the remaining seven are
modifications of the base MLP through optimizer choice (AdaHessian), loss weighting
(NTK, BRDR), input-layer encoding (Fourier features), or variable/equation
reformulation (Decoupled, SPINN, Sym./antisym. transform).
A vanilla fully connected PINN (6 layers, 512 neurons per layer, tanh activation)
serves as the baseline.
All configurations except AdaHessian use the Adam optimizer[Kingma2014]with initial learning rateα0=3×10−4\alpha_{0}=3\times 10^{-4}and exponential decay;
weights are initialised by Kaiming uniform/normal[He2015].
Each model is trained for 100 000 epochs with gradient accumulation frequencyKacc=4K_{\mathrm{acc}}=4; results are averaged over ten independent runs per configuration.
PINN-FVM validation RMSE is computed every 1 000 epochs.
The self-adaptive per-collocation-point weighting ofMcClenny2023selfadaptivewas not included among the eleven configurations due to incompatibility with the
PhysicsNeMo Sym constraint API; this constitutes a limitation and a direction for
future work.Table 4:Summary of eleven PINN configurations organised into four strategy groups.Configurations sharing the same group exploit the same primary mechanism.
Four entries constitute distinct network architectures (Vanilla, EPINN, FBPINN, PIKAN);
the remaining seven modify the base MLP through optimizer, loss weighting, input encoding,
or variable reformulation.NintN_{\mathrm{int}}: interior collocation points per step;NbndN_{\mathrm{bnd}}: boundary/initial condition (IC) points per step.
All configurations share the base architecture (6 layers, 512 neurons, tanh) except where noted.GroupConfigurationPrimary strength (key reference)NintN_{\mathrm{int}}NbndN_{\mathrm{bnd}}BaselineVanilla PINNReference MLP; uniform loss weights[RAISSI2019686]160001600Adaptive WeightingNTK weightingFixes loss imbalance via NTK-based rescaling[WANG2022110768]160001600BRDR weightingFixes loss imbalance via balanced residual decay rate[CHEN2025BRDR]160001600AdaHessianCurvature-aware optimizer; Hessian diagonal via Hutchinson[Yao2021AdaHessian]; halved collocation budget to offset the memory overhead of the Hessian-vector product8000800Spectral Bias MitigationFourier featuresHigh-frequency input mapping lifts spectral bias[Tancik2020FourierFeatures]160001600PIKANKAN basis functions resolve multi-scale features[WANG2025PIKAN]160001600Spatio-Temporal DecompositionFBPINN (multilevel)Domain decomposition; localised subdomain networks[DOLEAN2024117116]160001600Decoupled PINNGummel-style equation splitting; reduces nonlinear coupling160001600SPINNSeparable CP tensor decomposition; memory-efficient[Cho2023SPINNs]160001600Sym./antisym. transf.Bazant variable decomposition reduces effective nonlinearity[Bazant2004]160001600EnrichmentEnriched PINN (EPINN)Physics-aware basis enrichment models stiff EDL features[HUANG2025231]160001600

## 4.3.1Spectral bias mitigation: Fourier features and PIKAN

Fourier feature mapping[Tancik2020FourierFeatures]replaces the
raw input𝐱=(x,t)\mathbf{x}=(x,t)with a random sinusoidal embedding before the
first MLP layer:γ​(𝐱)=[cos⁡(2​π​𝐁𝐱),sin⁡(2​π​𝐁𝐱)]⊤,𝐁∈ℝm×2,Bj​k∼𝒩​(0,σ2)\gamma(\mathbf{x})=\bigl[\cos(2\pi\mathbf{B}\mathbf{x}),\;\sin(2\pi\mathbf{B}\mathbf{x})\bigr]^{\top},\qquad\mathbf{B}\in\mathbb{R}^{m\times 2},\quad B_{jk}\sim\mathcal{N}(0,\sigma^{2})(16)

By projecting inputs into a high-frequency feature space, the MLP backbone can
represent the sharp EDL gradients that are suppressed by standard spectral bias[rahaman2019spectralbias,Wang2021eigen].
The implementation uses the PhysicsNeMofourierarchitecture (6 layers,
512 neurons, sigmoid linear unit (SiLU) activation).

PIKAN[WANG2025PIKAN]replaces the weight×\timesactivation
structure of each MLP layer with learnable univariate spline maps.
Each KAN layer computes:xj(l+1)=∑iφi​j(l)​(xi(l)),φi​j​(x)=wb​tanh⁡(x)+∑k=0G+pci​j​k​Bkp​(x)x_{j}^{(l+1)}=\sum_{i}\varphi_{ij}^{(l)}(x_{i}^{(l)}),\qquad\varphi_{ij}(x)=w_{b}\,\tanh(x)+\sum_{k=0}^{G+p}c_{ijk}\,B_{k}^{p}(x)(17)

whereBkpB_{k}^{p}are B-spline basis functions of orderp=3p=3on a fixed uniform
grid ofG=32G=32points over the normalised domain[−1,1]2[-1,1]^{2},wbw_{b}is a
learnable base-activation weight, andci​j​kc_{ijk}are learnable spline
coefficients.
The per-unit expressive power of the spline basis allows a shallower,
narrower network (2 hidden layers, width 16) relative to the MLP baseline.

## 4.3.2Spatio-temporal decomposition: FBPINN, SPINN, Decoupled, and
symmetric/antisymmetric transformation

FBPINN[DOLEAN2024117116]partitions the(x,t)∈[0,1]×[0,2.56](x,t)\in[0,1]\times[0,2.56]domain into anℓ=3n_{\ell}=3-level hierarchy; levelllcontains2l−12^{l-1}overlapping
subdomains (1+2+4=71+2+4=7total).
Each subdomainjjat levelllcontributes through a small subnetworkul​ju_{lj}weighted by a sigmoid window:u^​(𝐱)\displaystyle\hat{u}(\mathbf{x})=1nℓ​∑l=1nℓ∑jwl​j​(𝐱)​ul​j​(𝐱~l​j)∑jwl​j​(𝐱),\displaystyle=\frac{1}{n_{\ell}}\sum_{l=1}^{n_{\ell}}\frac{\sum_{j}w_{lj}(\mathbf{x})\,u_{lj}(\tilde{\mathbf{x}}_{lj})}{\sum_{j}w_{lj}(\mathbf{x})},(18)wl​j​(𝐱)\displaystyle w_{lj}(\mathbf{x})=σ​(𝐱−(𝐜l​j−𝐫l​j)s)⋅σ​((𝐜l​j+𝐫l​j)−𝐱s)\displaystyle=\sigma\!\left(\frac{\mathbf{x}-(\mathbf{c}_{lj}-\mathbf{r}_{lj})}{s}\right)\cdot\sigma\!\left(\frac{(\mathbf{c}_{lj}+\mathbf{r}_{lj})-\mathbf{x}}{s}\right)(19)

where𝐱~l​j=(𝐱−𝐜l​j)/𝐫l​j\tilde{\mathbf{x}}_{lj}=(\mathbf{x}-\mathbf{c}_{lj})/\mathbf{r}_{lj}is the subdomain-normalised input,𝐜l​j\mathbf{c}_{lj}and𝐫l​j\mathbf{r}_{lj}are
the subdomain centre and half-width,ssis the sigmoid sharpness, and the
overlap ratio is 2.7.
Subnetworks use SiLU activation, 4 layers, and 32 neurons per layer.

SPINN[Cho2023SPINNs]decomposes the solution via a CP tensor
expansion of rankR=30R=30:u^​(x,t)=∑r=1Rfr​(x)​gr​(t)\hat{u}(x,t)=\sum_{r=1}^{R}f_{r}(x)\,g_{r}(t)(20)

wherefrf_{r}andgrg_{r}are scalar-valued MLP subnetworks (6 layers, 256 neurons,
SiLU) applied to each coordinate independently.
PDE derivatives require only 1D derivative computations throughfrf_{r}andgrg_{r},
reducing memory at the cost of accuracy when spatial and temporal modes are strongly coupled, as is the case in the EDL regime.

TheDecoupled PINNfollows a Gummel-style sequential update: at each
training stepφ\varphiis optimised with fixed(cp,cn)(c_{p},c_{n}), then(cp,cn)(c_{p},c_{n})are updated with the resultingφ\varphi.
This reduces the effective nonlinearity of each sub-problem but introduces a
splitting error that grows in the strongly coupled EDL.

For thesymmetric/antisymmetric transformation[Bazant2004],
the Bazant-inspired variable changeρ=12​(cp−cn),\displaystyle\rho=\tfrac{1}{2}(c_{p}-c_{n}),(21)c=12​(cp+cn)\displaystyle c=\tfrac{1}{2}(c_{p}+c_{n})(22)

decouples the two concentration equations at leading order, reducing the
effective nonlinearity presented to the network.
The complete derivation and the transformed PNP system are provided in the
supplementary material.

## 4.3.3Physics enrichment: EPINN

The Enriched PINN (EPINN)[HUANG2025231]applies two modifications to the
baseline MLP.
First, the activation function is changed from tanh to exponential linear unit (ELU) to improve gradient
flow near the sharp EDL transition.
Second, the loss is aggregated via homoscedastic uncertainty weighting, which
introduces a trainable log-variance parameterσi\sigma_{i}for each constraint[Kendall2018multi]:ℒtotal=∑i[ℒi2​σi2+log⁡σi]\mathcal{L}_{\mathrm{total}}=\sum_{i}\left[\frac{\mathcal{L}_{i}}{2\sigma_{i}^{2}}+\log\sigma_{i}\right](23)

Theσi\sigma_{i}are co-optimized by Adam alongside the network weights.
Thelog⁡σi\log\sigma_{i}regularisation term prevents all weights from collapsing to
zero, providing principled loss balancing without requiring gradient traces
(NTK) or residual statistics (BRDR).

Algorithm1describes the complete training workflow.Algorithm 1PINN training loop for the 1D PNP system (PhysicsNeMo Sym)1:PNP parameters (ε\varepsilon,δ\delta,ξ\xi,zpz_{p},znz_{n}), architecture𝒜\mathcal{A}, weighting scheme𝒲\mathcal{W}, max epochsNep=100 000N_{\mathrm{ep}}=100\,000, gradient accumulation frequencyKacc=4K_{\mathrm{acc}}=42:Trained parametersθ∗\theta^{*}, RMSE history vs. FVM reference3:Initializeθ\thetawith Kaiming uniform/normal initialization4:Setα0=3×10−4\alpha_{0}=3\times 10^{-4}, exponential learning-rate decay (decay rate0.920.92, steps40004000)5:forepochn=1n=1toNepN_{\mathrm{ep}}do6:foraccumulation stepk=1k=1toKaccK_{\mathrm{acc}}do7:SampleNintN_{\mathrm{int}}interior points(xi,ti)(x_{i},t_{i})via Halton sequence (see Table4)8:SampleNbndN_{\mathrm{bnd}}points per boundary/IC constraint (see Table4)9:Forward pass:(c^p,c^n,φ^)=NNθ​(x,t)(\hat{c}_{p},\hat{c}_{n},\hat{\varphi})=\mathrm{NN}_{\theta}(x,t)10:Compute PDE/BC/IC residuals via automatic differentiation11:if𝒲\mathcal{W}= NTK andnmod10=0n\bmod 10=0then12:Compute NTK traces{tr​(Ki)}\{\mathrm{tr}(K_{i})\}for each constraint13:Setλi←λ¯/tr​(Ki)\lambda_{i}\leftarrow\bar{\lambda}\,/\,\mathrm{tr}(K_{i}), whereλ¯=1N​∑jtr​(Kj)\bar{\lambda}=\tfrac{1}{N}\sum_{j}\mathrm{tr}(K_{j})14:elseif𝒲\mathcal{W}= BRDRthen15:Updateλi\lambda_{i}via balanced residual decay rate rule[CHEN2025BRDR]16:else17:λi←1\lambda_{i}\leftarrow 1(uniform weights)18:endif19:Computeℒ=λPDE​ℒPDE+λBC​ℒBC+λIC​ℒIC\mathcal{L}=\lambda_{\mathrm{PDE}}\mathcal{L}_{\mathrm{PDE}}+\lambda_{\mathrm{BC}}\mathcal{L}_{\mathrm{BC}}+\lambda_{\mathrm{IC}}\mathcal{L}_{\mathrm{IC}}20:Accumulate:𝐠+=∇θℒ/Kacc\mathbf{g}\mathrel{+}=\nabla_{\theta}\mathcal{L}/K_{\mathrm{acc}}21:endfor22:Clip gradient norm:𝐠←𝐠⋅min⁡(1,0.5/‖𝐠‖)\mathbf{g}\leftarrow\mathbf{g}\cdot\min(1,\,0.5/\|\mathbf{g}\|)23:Update:θ←θ−αn​𝐠\theta\leftarrow\theta-\alpha_{n}\,\mathbf{g}(Adam,β1=0.9\beta_{1}=0.9,β2=0.999\beta_{2}=0.999; or AdaHessian)24:ifnmod1000=0n\bmod 1000=0then25:Compute RMSE against FVM reference; log to file26:endif27:endfor28:returnθ∗←θ\theta^{*}\leftarrow\theta

## 5Results and Discussion

All eleven configurations converged within the 100 000-epoch budget.
Dimensionless RMSE values span10−210^{-2}–10−410^{-4}relative to the FVM reference.
The complete error statistics, comprising mean RMSE and mean absolute error (MAE) averaged
over ten independent runs per architecture, together with their standard deviations, are given in
Table5.
Representative space-time solution surfaces and training loss curves for the
best-performing NTK configuration are shown in Figures3and4.

## 5.1Adaptive loss weighting: NTK vs. BRDR

This subsection evaluates whether correcting loss imbalance via gradient-trace
or residual-rate statistics is the dominant factor in PINN accuracy on the
stiff PNP system, and quantifies the associated computational cost difference.

Both NTK and BRDR adaptive weighting substantially outperformed the vanilla PINN
baseline (Table5). The gain is consistent with loss imbalance,
driven byε2≈5.3×10−10\varepsilon^{2}\approx 5.3\times 10^{-10}, being the primary training
bottleneck rather than architecture choice.

NTK weighting achieved the lowest RMSE across all three fields:(6.6±0.4)×10−4(6.6\pm 0.4)\times 10^{-4}forcnc_{n},(6.2±0.3)×10−4(6.2\pm 0.3)\times 10^{-4}forcpc_{p},
and(1.1±0.1)×10−3(1.1\pm 0.1)\times 10^{-3}forφ\varphi(mean±\pmone standard deviation
across ten runs).
These values are 9%, 3%, and 19% below the corresponding BRDR RMSEs forcnc_{n},cpc_{p}, andφ\varphi, respectively.
However, BRDR achieved lower MAEs for both concentration fields, indicating that
NTK suppresses large localised outliers more effectively (particularly near the
electrode interfaces), whereas BRDR produces a more spatially uniform error
distribution.

The NTK superiority in RMSE came at a mean additional cost of3.2±0.43.2\pm 0.4h wall-clock time per run (NVIDIA H100), because NTK requires
computing the trace of the NTK matrix for each constraint at every step, whereas
BRDR uses only scalar residual statistics.
When accuracy is the priority, NTK is the method of choice; when compute is
constrained, BRDR delivers near-identical accuracy at lower cost.

## 5.2Frequency-scale resolution and spectral bias

This subsection examines how effectively each architecture mitigates spectral
bias in the high-frequency Poisson equation, and whether spectral bias reduction
translates to lower total RMSE within the fixed training budget.

The point-wise electric potential error fields for all architectures are shown in
Figure 1 of the Supplementary Material.
The vanilla, BRDR-weighted, and NTK-weighted configurations exhibitφ\varphierrors roughly one order of magnitude larger than their concentration errors,
with errors concentrated nearx=0x=0andx=1x=1, which is the signature of spectral bias
in the Poisson equation, whoseε2\varepsilon^{2}prefactor makes it the
highest-frequency component of the system.

In contrast, the AdaHessian, decoupled, enriched, Fourier-featurized, PIKAN, and
SPINN architectures resolve both frequency scales to a similar order of magnitude,
with errors distributed more uniformly across the domain.
These architectures are therefore more effective at mitigating spectral bias,
consistent with theory[rahaman2019spectralbias,xu2019fprinciple].
However, none of these architectures achieved the lowest total RMSE within the
fixed 100 000-epoch budget, suggesting a convergence-speed trade-off: spectral
bias mitigation allows resolution of high-frequency features, but at the cost of
slower convergence to the low-frequency background that adaptive-weighting
configurations learn first.
Training to a precision target rather than a fixed epoch count would better reveal
the ceiling accuracy of spectral-bias-aware architectures.

## 5.3Symmetric/antisymmetric variable transformation

This subsection quantifies the accuracy benefit of the Bazant variable
transformation independently of any loss-weighting strategy, isolating the
effect of algebraic reformulation on the effective problem nonlinearity.

The decomposition into symmetric (cc) and antisymmetric (ρ\rho) concentration
variables (21)–(22) yielded consistent, modest RMSE
improvements over the vanilla PINN: 4% forcnc_{n}, 5% forcpc_{p}, and 1% forφ\varphi.
The relatively small gains indicate that, while the transformation reduces
effective nonlinearity, the dominant accuracy bottleneck remains the loss imbalance
rather than the algebraic form of the field variables.
Combining this transformation with NTK or BRDR weighting is a natural direction
for further accuracy gains.

## 5.4Wall-clock time and computational efficiency

This subsection characterises the computational cost of each configuration to
assess the accuracy–efficiency trade-off and identify bottlenecks for future
optimisation.

Wall-time distributions are shown in Figure5.
The observed minimum wall time of13.1±0.313.1\pm 0.3h per run reflects the overhead
of generating FVM-comparison validation snapshots every 1 000 epochs; production
deployments with less frequent checkpointing would be substantially faster.

SPINN was the fastest architecture owing to its separable forward-mode AD
formulation[Cho2023SPINNs], yet it produced the highest RMSE
(∼\sim10−210^{-2}), demonstrating that speed alone cannot substitute for
adequate loss conditioning in stiff PNP problems.
The multilevel FBPINN was the slowest, a consequence of its loop-based subdomain
iteration; vectorising the subdomain sweeps is expected to recover competitive
training speeds.

## 5.5Loss landscape geometry

This subsection tests whether loss basin sharpness provides a geometry-based
predictor of RMSE rank that does not require FVM comparison.

Loss landscapes are computed by evaluating the training loss over a two-dimensional
grid of parameter perturbations along orthogonal random directions in weight space[li2018visualizing].
As shown in Figure6, most architectures converged to sharp,
well-defined basins.
The NTK-weighted PINN produced the sharpest and most symmetric basin, consistent
with its lowest RMSE.
The SPINN landscape was notably flat and irregular, consistent with its highest
RMSE and suggesting that its training trajectory settled in a broad, poorly
conditioned minimum.
We quantify basin sharpness by the ratio of the maximum to minimum loss value over
a fixedL∞L_{\infty}ball of radius10−210^{-2}in the perturbation directions; NTK
achieves the lowest sharpness ratio of 1.8, while SPINN achieves 47.3, providing
a geometric predictor of generalisation quality that correlates monotonically with
the RMSE ranking in Table5.Table 5:PINN-FVM dimensionless solution errors.Root-mean-square error (RMSE) and mean absolute error (MAE) averaged over ten
independent training runs per configuration.
Parenthetical values after RMSE entries are one standard deviation across the
ten runs; MAE values are means only.
Bold indicates the best result per metric per field.
All values are dimensionless.ConfigurationRMSE (std)MAEVanilla PINNcnc_{n}9.355×10−49.355\times 10^{-4}(0.8×10−4)(0.8\times 10^{-4})5.019×10−45.019\times 10^{-4}cpc_{p}8.511×10−48.511\times 10^{-4}(0.7×10−4)(0.7\times 10^{-4})4.496×10−44.496\times 10^{-4}φ\varphi1.585×10−31.585\times 10^{-3}(1.2×10−4)(1.2\times 10^{-4})7.064×10−47.064\times 10^{-4}AdaHessiancnc_{n}3.576×10−33.576\times 10^{-3}(0.5×10−3)(0.5\times 10^{-3})2.567×10−32.567\times 10^{-3}cpc_{p}3.454×10−33.454\times 10^{-3}(0.5×10−3)(0.5\times 10^{-3})2.413×10−32.413\times 10^{-3}φ\varphi6.729×10−36.729\times 10^{-3}(1.1×10−3)(1.1\times 10^{-3})4.291×10−34.291\times 10^{-3}BRDR weightingcnc_{n}7.270×10−47.270\times 10^{-4}(0.6×10−4)(0.6\times 10^{-4})3.526×𝟏𝟎−𝟒\mathbf{3.526\times 10^{-4}}cpc_{p}6.395×10−46.395\times 10^{-4}(0.5×10−4)(0.5\times 10^{-4})3.198×𝟏𝟎−𝟒\mathbf{3.198\times 10^{-4}}φ\varphi1.323×10−31.323\times 10^{-3}(1.0×10−4)(1.0\times 10^{-4})4.484×10−44.484\times 10^{-4}Decoupled PINNcnc_{n}5.651×10−35.651\times 10^{-3}(0.9×10−3)(0.9\times 10^{-3})4.138×10−34.138\times 10^{-3}cpc_{p}5.642×10−35.642\times 10^{-3}(0.8×10−3)(0.8\times 10^{-3})4.122×10−34.122\times 10^{-3}φ\varphi6.643×10−36.643\times 10^{-3}(1.3×10−3)(1.3\times 10^{-3})5.000×10−35.000\times 10^{-3}Enriched PINNcnc_{n}1.174×10−31.174\times 10^{-3}(0.9×10−4)(0.9\times 10^{-4})6.930×10−46.930\times 10^{-4}cpc_{p}1.129×10−31.129\times 10^{-3}(0.8×10−4)(0.8\times 10^{-4})6.639×10−46.639\times 10^{-4}φ\varphi1.717×10−31.717\times 10^{-3}(1.5×10−4)(1.5\times 10^{-4})7.369×10−47.369\times 10^{-4}FBPINN (multilevel)cnc_{n}4.642×10−34.642\times 10^{-3}(0.7×10−3)(0.7\times 10^{-3})2.899×10−32.899\times 10^{-3}cpc_{p}3.600×10−33.600\times 10^{-3}(0.6×10−3)(0.6\times 10^{-3})2.230×10−32.230\times 10^{-3}φ\varphi1.302×10−21.302\times 10^{-2}(2.1×10−3)(2.1\times 10^{-3})7.450×10−37.450\times 10^{-3}Fourier featurescnc_{n}4.758×10−34.758\times 10^{-3}(0.9×10−3)(0.9\times 10^{-3})4.605×10−34.605\times 10^{-3}cpc_{p}4.563×10−34.563\times 10^{-3}(0.8×10−3)(0.8\times 10^{-3})4.399×10−34.399\times 10^{-3}φ\varphi4.461×10−34.461\times 10^{-3}(0.7×10−3)(0.7\times 10^{-3})4.060×10−34.060\times 10^{-3}PIKANcnc_{n}1.419×10−31.419\times 10^{-3}(1.1×10−4)(1.1\times 10^{-4})7.010×10−47.010\times 10^{-4}cpc_{p}1.307×10−31.307\times 10^{-3}(1.0×10−4)(1.0\times 10^{-4})6.258×10−46.258\times 10^{-4}φ\varphi3.395×10−33.395\times 10^{-3}(0.5×10−3)(0.5\times 10^{-3})1.541×10−31.541\times 10^{-3}NTK weightingcnc_{n}6.613×𝟏𝟎−𝟒\mathbf{6.613\times 10^{-4}}(0.4×10−4)(0.4\times 10^{-4})3.739×10−43.739\times 10^{-4}cpc_{p}6.214×𝟏𝟎−𝟒\mathbf{6.214\times 10^{-4}}(0.3×10−4)(0.3\times 10^{-4})3.225×10−43.225\times 10^{-4}φ\varphi1.068×𝟏𝟎−𝟑\mathbf{1.068\times 10^{-3}}(0.1×10−3)(0.1\times 10^{-3})4.180×𝟏𝟎−𝟒\mathbf{4.180\times 10^{-4}}SPINNcnc_{n}2.448×10−22.448\times 10^{-2}(0.4×10−2)(0.4\times 10^{-2})2.406×10−22.406\times 10^{-2}cpc_{p}2.452×10−22.452\times 10^{-2}(0.4×10−2)(0.4\times 10^{-2})2.410×10−22.410\times 10^{-2}φ\varphi8.893×10−38.893\times 10^{-3}(1.5×10−3)(1.5\times 10^{-3})3.755×10−33.755\times 10^{-3}Sym./antisym. transformcnc_{n}8.992×10−48.992\times 10^{-4}(0.7×10−4)(0.7\times 10^{-4})4.636×10−44.636\times 10^{-4}cpc_{p}8.098×10−48.098\times 10^{-4}(0.6×10−4)(0.6\times 10^{-4})4.216×10−44.216\times 10^{-4}φ\varphi1.568×10−31.568\times 10^{-3}(1.1×10−4)(1.1\times 10^{-4})6.229×10−46.229\times 10^{-4}Figure 3:NTK-weighted PINN validation against the FVM reference.Space-time surface plots showing (left) the FVM reference solution, (centre)
the PINN-predicted solution, and (right) the point-wise absolute difference
for the dimensionless anion concentrationcnc_{n}(top), cation concentrationcpc_{p}(middle), and electric potentialφ\varphi(bottom).
Peak errors are localised near the electrode interfaces (x=0,1x=0,1) where the
electric double layer imposes the sharpest gradients.Figure 4:NTK-weighted PINN training loss.Total loss (left) and individual loss components (right), averaged over ten
independent runs.
Individual loss components (PDE: partial differential equation, BC: boundary condition, IC: initial condition) converge at comparable rates
throughout training, consistent with the balanced weighting reported in
Section4.2.Figure 5:Wall-clock time distributions.Box plots of wall time for the NTK configuration over ten runs (left) and
across all architectures (right).
The red line marks the median; box edges denote the first and third quartiles;
whiskers extend to1.5×1.5\timesthe interquartile range (IQR).
All runs performed on one NVIDIA H100 GPU.Figure 6:Loss landscape geometry for all PINN configurations.Two-dimensional landscapes are computed by perturbing trained parameters
along orthogonal random directions in weight space[li2018visualizing].
A sharper, more symmetric basin (NTK, BRDR, vanilla) indicates a
well-conditioned minimum with superior generalisation.
The SPINN landscape is flat and irregular (sharpness ratio 47.3), consistent
with its highest observed RMSE (Table5).
The NTK configuration achieves the sharpest basin (sharpness ratio 1.8).

## 5.6Collocation density sensitivity

This subsection examines whether the NTK benchmark errors atNint=16,000N_{\mathrm{int}}=16{,}000are sensitive to the interior collocation budget,
and whether the reported RMSE values are collocation-converged.

Three additional single-seed NTK runs were performed atNint∈{2,000,6,000,10,000}N_{\mathrm{int}}\in\{2{,}000,\,6{,}000,\,10{,}000\}, maintaining the 10:1
interior-to-boundary ratio used throughout the benchmark.
Figure7shows the aggregated training loss for all
three runs.Figure 7:NTK training loss for three collocation densities.Aggregated training loss (log10scale) over 100 000 epochs for the
NTK-weighted configuration at interior collocation countsNint∈{2,000,6,000,10,000}N_{\mathrm{int}}\in\{2{,}000,\,6{,}000,\,10{,}000\}(10:1
interior-to-boundary ratio throughout).
All three runs converge to a comparable final training loss of
approximately10−310^{-3}; point-wise RMSE against the FVM reference
decreases monotonically with increasingNintN_{\mathrm{int}}.

All three runs converge to a final training loss of approximately10−310^{-3}within the 100 000-epoch budget, and the loss curves are qualitatively
similar across the threeNintN_{\mathrm{int}}values.
Inspection of the validator surfaces suggests that point-wise RMSE against the
FVM reference decreases monotonically asNintN_{\mathrm{int}}increases from
2 000 to 10 000, consistent with the expectation that denser collocation
better resolves the stiff electric double layer near the electrode interfaces.

## 6Conclusions

This benchmark establishes that adaptive loss weighting is the dominant factor
governing PINN accuracy on the stiff PNP system, outweighing architecture choice,
input-space encoding, and variable reformulation.
NTK weighting achieves dimensionless RMSE as low as(6.6±0.4)×10−4(6.6\pm 0.4)\times 10^{-4}(anion),(6.2±0.3)×10−4(6.2\pm 0.3)\times 10^{-4}(cation), and(1.1±0.1)×10−3(1.1\pm 0.1)\times 10^{-3}(electric potential), establishing the strongest data-free accuracy reported for
a 1D PNP system under battery-relevant parametrisation[HUANG2025231].
The cheaper BRDR scheme matches NTK within 10% of RMSE for the concentration
fields (24% forφ\varphi) by computing only scalar
residual statistics rather than full NTK matrix traces, reducing mean wall time by3.2±0.43.2\pm 0.4h per run on an NVIDIA H100; NTK is the right choice when accuracy
is the priority, BRDR when compute is constrained.
Spectral-bias-aware architectures (Fourier features, FBPINN, PIKAN) produce more
spatially uniform error distributions but do not achieve the lowest total RMSE
within the fixed 100 000-epoch budget, indicating a convergence-speed trade-off
that a precision-target or curriculum training protocol could resolve.
Loss basin sharpness correlates monotonically with the RMSE ranking across all
eleven configurations, providing an efficient geometry-based diagnostic that does
not require FVM comparison.
These findings generalise beyond the specific electrochemical application: the
stiffness structure (small singular-perturbation parameter, inter-equation loss
imbalance) is shared by semiconductor drift-diffusion, reactive porous-media
transport, and coupled thermo-mechanical problems, and the same adaptive-weighting
remedies are expected to transfer.

## Acknowledgements

C.G.T.F. acknowledges the support of the Natural Sciences and Engineering Research Council of Canada (NSERC) [RGPIN-2024-03989]. This research was enabled in part by support provided by SHARCNET and the Digital Research Alliance of Canada.

## Declaration of Competing Interests

The authors declare that they have no known competing financial interests or personal
relationships that could have appeared to influence the work reported in this paper.

## Data availability

The full PhysicsNeMo Sym PINN implementation, including all configuration files
and post-processing scripts, is publicly available athttps://github.com/Feugmo-Group/physicsnemo-sym-pnp.

## References

## 


- 


Major funding support from
