# yancc: A GPU-accelerated, differentiable solver for neoclassical transport in tokamaks and stellarators

**arXiv ID**: 2607.20861v1
**Authors**: Rory Conlin, Matt Landreman
**Published**: 2026-07-23
**Categories**: physics.plasm-ph, math.NA
**HTML URL**: https://arxiv.org/html/2607.20861v1

## Abstract

We present yancc, a new GPU-accelerated solver for the drift kinetic equation that computes neoclassical transport fluxes, flows, and currents in tokamaks and stellarators. The drift kinetic equation is challenging to solve numerically due to strong advection-dominance, recirculating flows, internal boundary layers, severe anisotropy, and high dimensionality. The code solves both the full four-dimensional drift kinetic equation (retaining speed-dependent collisions, energy scattering, and full interspecies coupling), and the reduced monoenergetic form. The discretization combines a Maxwell polynomial collocation grid in speed with finite differences in pitch angle and the flux surface coordinates, using a modified upwind stencil designed to improve diagonal dominance for multigrid efficiency. The resulting linear system is solved with a multigrid-preconditioned Krylov method. Built in JAX, yancc is fully differentiable, enabling gradient-based optimization and adjoint sensitivity analysis. Benchmarks against MONKES and SFINCS show agreement within 1\% across a range of collisionalities, geometries, and multi-species configurations. yancc achieves roughly an order of magnitude speedup over SFINCS on a per-scan basis while using an order of magnitude less memory, with runtime remaining nearly flat across the full range of collisionality. The combination of speed, low memory footprint, and differentiability makes yancc well suited for integration into stellarator optimization workflows, uncertainty quantification, and profile prediction.

## Full Text

yancc: A GPU-accelerated, differentiable solver for neoclassical transport in tokamaks and stellarators

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
- License: CC BY 4.0arXiv:2607.20861v1 [physics.plasm-ph] 23 Jul 2026

## yancc: A GPU-accelerated, differentiable solver for neoclassical transport in
tokamaks and stellaratorsRory ConlinInstitute for Research in Electronics and Applied Physics,
University of Maryland, College Park, MD 20742, USAMatt LandremanInstitute for Research in Electronics and Applied Physics,
University of Maryland, College Park, MD 20742, USA

## Abstract

We presentyancc, a new GPU-accelerated solver for the drift kinetic
equation that computes neoclassical transport fluxes, flows, and currents in
tokamaks and stellarators. The drift kinetic equation is challenging to solve
numerically due to strong advection-dominance, recirculating flows, internal
boundary layers, severe anisotropy, and high dimensionality. The code solves
both the full four-dimensional drift kinetic equation (retaining
speed-dependent collisions, energy scattering, and full interspecies
coupling), and the reduced monoenergetic form. The discretization combines a
Maxwell polynomial collocation grid in speed with finite differences in pitch angle
and the flux surface coordinates, using a modified upwind stencil designed to
improve diagonal dominance for multigrid efficiency. The resulting linear
system is solved with a multigrid-preconditioned Krylov method. Built in JAX,yanccis fully differentiable, enabling gradient-based optimization and
adjoint sensitivity analysis. Benchmarks against MONKES and SFINCS show
agreement within 1% across a range of collisionalities, geometries, and
multi-species configurations.yanccachieves roughly an order of magnitude
speedup over SFINCS on a per-scan basis while using an order of magnitude less
memory, with runtime remaining nearly flat across the full range of
collisionality. The combination of speed, low memory footprint, and
differentiability makesyanccwell suited for integration into stellarator
optimization workflows, uncertainty quantification, and profile prediction.

## 1Introduction

Magnetic confinement fusion devices use strong magnetic fields to confine a
high-temperature plasma in toroidal geometry. The magnetic field can be
configured with both toroidal and poloidal components, creating nested flux
surfaces along which charged particles move while radial transport across
surfaces is suppressed. In stellarators, this confining field is generated primarily
through external coils without requiring a toroidal plasma current, providing
inherent steady-state operation and immunity to current-driven disruptions.
However, the three-dimensional magnetic geometry of stellarators makes the
dynamics of confined particles significantly more complex than in axisymmetric
devices such as tokamaks.

Neoclassical transport theory describes the collisional transport of
particles, heat, and momentum in these devices, extending classical transport
to account for the effects of toroidal geometry. The inhomogeneous magnetic
field in a torus causes particle drifts that produce populations of trapped
particles that bounce between magnetic field maxima. These trapped particles,
combined with guiding center drifts of the passing population, yield transport
that exceeds classical predictions and depends sensitively on the
collisionality regime and the structure of the magnetic field. Solving the
drift kinetic equation (DKE) gives the neoclassical particle flux, heat flux,
and parallel flow for each plasma species. From these one computes the radial
electric field via the ambipolarity condition, the bootstrap current, and the
neoclassical conductivity, all essential inputs for transport modeling,
stability analysis, and scenario development.

In stellarators, neoclassical transport differs qualitatively from tokamaks
due to the three-dimensional geometry. The lack of axisymmetry creates
additional ripple-trapped particle populations that can dominate transport at
certain collisionalities. The radial electric field plays a crucial role:
sufficiently strongE×BE\times Brotation suppresses ripple-induced transport,
producing electron-root and ion-root solutions for the ambipolar electric
field with transitions between them as plasma parameters vary. Accurate
computation thus requires a solver that handles the full 3D geometry while
resolving the sharp boundary layers that develop between different classes of
trapped particles at low collisionality.

The numerical solution of the DKE is challenging due to the high resolution
required for the boundary layers, the high-dimensional phase space, strong
advection, anisotropic diffusion, and the need to solve the equation
repeatedly for optimization or parameter scans. To carry out high-resolution solves of
the DKE efficiently, a promising option is a multigrid approach. Multigrid methods
achieve rapid convergence by operating on a hierarchy of discretizations: classical
iterations efficiently damp high-frequency error but stall on low-frequency
components, while multigrid overcomes this by recursively solving coarse-grid
representations where low-frequency fine-grid errors appear high-frequency and
are rapidly damped. Originally developed for elliptic problems[47,9,51],
multigrid has been extended through algebraic multigrid[38,46]and geometric
approaches. Advection-diffusion equations present particular difficulties. At
high Péclet numbers, strong advective coupling renders standard smoothers
ineffective, motivating upwinded discretizations, line smoothers,
operator-dependent transfer operators, or algebraic multigrid approaches[13,37,52,36]. Multigrid has been applied to
the gyrokinetic equation[1,45], Poisson and Ampère solves in PIC
simulations[10], and problems in
magnetohydrodynamics[7,2], though its
application to the DKE for neoclassical transport is relatively novel.

A number of codes have been developed to solve the drift kinetic equation.
DKES[24,48,44]and more recently MONKES[16]use a
spectral Legendre expansion
for the monoenergetic form, eliminating the speed coordinate and thereby
dropping energy scattering and momentum conservation in exchange for
performance. SFINCS[30]solves the full
four-dimensional DKE (dropping only radial coupling) with the full linearized
Fokker-Planck collision operator using a mixture of finite difference and spectral
methods and a sparse direct preconditioner, providing high accuracy across
collisionality regimes at the cost of substantial computational cost. NEO[3,4,6]adopts a
similar approach and is primarily focused on tokamak geometry, though
extensions to 3D fields also exist[5]. FORTEC-3D[43,42]is a radially
global code that uses a Monte Carlo approach to solve the DKE, and can capture
full orbit width effects. PIC codes such as Euterpe[28,29]can also be used to
solve the global drift kinetic equation, though the cost is significantly
higher than 4D codes such as SFINCS, making it impractical for optimization or
large database studies. KNOSOS[49]uses a bounce averaged
approach to
reduce the dimensionality, making it extremely fast, but contains only pitch
angle scattering and is limited to low collisionality regimes, making it
inaccurate when dealing with impurities. NEO-2[26,27]uses field line
following coordinates and the full linearized collision operator, making it
accurate across a wide range of collisionality, but neglects the effects of the𝐄×𝐁\mathbf{E}\times\mathbf{B}drift which moves particles across field lines.

Existing neoclassical solvers make unavoidable compromises between speed and
physics fidelity. The monoenergetic approximation sacrifices interspecies
coupling and energy scattering, limiting accuracy for multi-species plasmas at
high collisionality. Full 4D solvers like SFINCS require substantial memory and
scale poorly to GPU hardware due to sparse matrix factorizations with irregular
memory access. We attempt to fill this gap withyancc(“Yet Another
NeoClassical Code”), providing a fast solver for the full DKE with minimal
physics approximations by exploiting GPU parallelism for high-throughput
parameter scans and optimization. Built on JAX[8],yanccis
automatically differentiable, enabling gradient-based optimization and
uncertainty quantification workflows that require derivatives of transport
coefficients with respect to input parameters.

## 2Drift Kinetic Equation

The drift kinetic equation[19]governs neoclassical
transport in toroidal
confinement devices. It has been derived a number of times in the literature[20,22], so we only focus on the
salient points here. We expand the kinetic
equation for small normalized gyroradiusρ∗=m​vt​h/(|q|​B0​a)\rho_{*}=mv_{th}/(|q|B_{0}a)(heremmis the particle mass,qqthe charge,vt​hv_{th}the thermal speed,B0B_{0}the average field strength, andaasome characteristic macroscopic
length scale, taken here to be the minor radius) and take the guiding center
distribution function for speciesssasfs=f1,s+FM,sf_{s}=f_{1,s}+F_{M,s}(1)

WhereFM,sF_{M,s}is a Maxwellian, and we assume that the first order correctionf1,s/FM,s∼ρs∗f_{1,s}/F_{M,s}\sim\rho_{s}^{*}which is well satisfied in the core of tokamaks
and stellarators. The guiding center distribution function depends on 5
variables, 3 in real space and 2 in velocity space. In real space we
parameterize a toroidal volume by coordinates(ρ,θ,ζ)(\rho,\theta,\zeta)whereρ=ψN\rho=\sqrt{\psi_{N}}is a radial coordinate which labels flux surfaces, equal
to the square root of the normalized toroidal fluxψ\psienclosed by the
surface (not to be confused with the normalized gyroradiusρ∗\rho_{*}), andθ\thetaandζ\zetaare general poloidal and toroidal angles on each surface
(we make no assumptions that field lines are straight in these coordinates,
just that the field is tangent to surfaces of constantρ\rho). In these
coordinates the magnetic field can be written as𝐁=Bθ​∇θ+Bζ​∇ζ+Bρ​∇ρ=Bθ​∂𝐫∂θ+Bζ​∂𝐫∂ζ\mathbf{B}=B_{\theta}\nabla\theta+B_{\zeta}\nabla\zeta+B_{\rho}\nabla\rho=B^{\theta}\tfrac{\partial\mathbf{r}}{\partial\theta}+B^{\zeta}\tfrac{\partial\mathbf{r}}{\partial\zeta}(2)

and the Jacobian determinant of the coordinate system isg=∂𝐫∂ρ⋅∂𝐫∂θ×∂𝐫∂ζ\sqrt{g}=\tfrac{\partial\mathbf{r}}{\partial\rho}\cdot\tfrac{\partial\mathbf{r}}{\partial\theta}\times\tfrac{\partial\mathbf{r}}{\partial\zeta}(3)

In the smallρ∗\rho_{*}limit we drop radial coupling, reducing the problem to 4D
(θ\theta,ζ\zeta, and 2 velocity space coordinates). In velocity space we
choose our coordinates to be normalized speedxs=v/vt​h,sx_{s}=v/v_{th,s}and the pitch
angleα=arccos⁡(−v||/v)\alpha=\arccos(-v_{||}/v). In these coordinates, the drift kinetic
equation becomes:x˙s​∂f1,s∂xs+α˙​∂f1,s∂α+θ˙​∂f1,s∂θ+ζ˙​∂f1,s∂ζ−∑s′Cs​s′ℓ+Ss=−𝐯drift,s⋅∇ρ​(∂FM,s∂ρ)W0,s+qsTs​v||​B​⟨E||​B⟩⟨B2⟩​FM,s\begin{split}\dot{x}_{s}\frac{\partial f_{1,s}}{\partial x_{s}}+\dot{\alpha}\frac{\partial f_{1,s}}{\partial\alpha}+\dot{\theta}\frac{\partial f_{1,s}}{\partial\theta}+\dot{\zeta}\frac{\partial f_{1,s}}{\partial\zeta}-\sum_{s^{\prime}}C^{\ell}_{ss^{\prime}}+S_{s}&=-\mathbf{v}_{\mathrm{drift},s}\cdot\nabla\rho\Bigg(\frac{\partial F_{M,s}}{\partial\rho}\Bigg)_{W_{0,s}}\\
&\quad+\frac{q_{s}}{T_{s}}v_{||}B\frac{\langle E_{||}B\rangle}{\langle B^{2}\rangle}F_{M,s}\end{split}(4)

Here and throughout the angle brackets⟨h⟩\langle h\rangledenote the flux surface
average of a quantityhh. The trajectories are given byθ˙=−vt​h,s​xs​cos⁡α​BθB−BζB2​g​Eρ\dot{\theta}=-\frac{v_{th,s}x_{s}\cos{\alpha}~B^{\theta}}{B}-\frac{B_{\zeta}}{B^{2}\sqrt{g}}E_{\rho}(5)ζ˙=−vt​h,s​xs​cos⁡α​BζB+BθB2​g​Eρ\dot{\zeta}=-\frac{v_{th,s}x_{s}\cos{\alpha}~B^{\zeta}}{B}+\frac{B_{\theta}}{B^{2}\sqrt{g}}E_{\rho}(6)α˙=−vt​h,s​xs​sin⁡α2​B2​(Bθ​∂B∂θ+Bζ​∂B∂ζ)+cos⁡α​sin⁡α​12​B3​g​Eρ​(Bζ​∂B∂θ−Bθ​∂B∂ζ)\dot{\alpha}=-\frac{v_{th,s}x_{s}\sin{\alpha}}{2B^{2}}\Bigg(B^{\theta}\frac{\partial B}{\partial\theta}+B^{\zeta}\frac{\partial B}{\partial\zeta}\Bigg)+\cos{\alpha}\sin{\alpha}\frac{1}{2B^{3}\sqrt{g}}E_{\rho}\Bigg(B_{\zeta}\frac{\partial B}{\partial\theta}-B_{\theta}\frac{\partial B}{\partial\zeta}\Bigg)(7)x˙s=−(1+cos2⁡α)​xs2​B3​g​Eρ​(Bζ​∂B∂θ−Bθ​∂B∂ζ)\dot{x}_{s}=-(1+\cos^{2}\alpha)\frac{x_{s}}{2B^{3}\sqrt{g}}E_{\rho}\Bigg(B_{\zeta}\frac{\partial B}{\partial\theta}-B_{\theta}\frac{\partial B}{\partial\zeta}\Bigg)(8)

Here the radial electric field enters asEρ=−∂Φ0/∂ρE_{\rho}=-\partial\Phi_{0}/\partial\rhowithΦ0\Phi_{0}the leading
order potential that is constant on a flux surface,vt​h,s=2​Ts/msv_{th,s}=\sqrt{2T_{s}/m_{s}}is the thermal speed of speciesss, andBBis the
magnetic field magnitude.SsS_{s}is a source term that will be described below.

The collision operatorCs​s′ℓC^{\ell}_{ss^{\prime}}is the Fokker-Planck-Landau operator
linearized around a Maxwellian:Cs​s′ℓ\displaystyle C^{\ell}_{ss^{\prime}}=Cs​s′​[f1,s,FM,s′]+Cs​s′​[FM,s,f1,s′]\displaystyle=C_{ss^{\prime}}[f_{1,s},F_{M,s^{\prime}}]+C_{ss^{\prime}}[F_{M,s},f_{1,s^{\prime}}](9)=CL,s​s′+CE,s​s′+CF,s​s′\displaystyle=C_{L,ss^{\prime}}+C_{E,ss^{\prime}}+C_{F,ss^{\prime}}(10)

CL+CEC_{L}+C_{E}make up the test particle part of the collision operator, withCLC_{L}the Lorentz pitch angle scattering operator betweenf1,sf_{1,s}andFM,s′F_{M,s^{\prime}}:CL,s​s′=νD,s​s′2​sin⁡α​∂∂α​[sin⁡α​∂f1,s∂α]C_{L,ss^{\prime}}=\frac{\nu_{D,ss^{\prime}}}{2\sin\alpha}\frac{\partial}{\partial\alpha}\Bigg[\sin{\alpha}\frac{\partial f_{1,s}}{\partial\alpha}\Bigg](11)

andCEC_{E}the energy scattering operator betweenf1,sf_{1,s}andFM,s′F_{M,s^{\prime}}:CE,s​s′=ν||,ss′​[v22​∂2f1,s∂v2−v2vt​h,s′2​(1−msms′)​v​∂f1,s∂v]+νD,s​s′​v​∂f1,s∂v+4​π​Γs​s′​msms′​FM,s′​f1,sC_{E,ss^{\prime}}=\nu_{||,ss^{\prime}}\Big[\frac{v^{2}}{2}\frac{\partial^{2}f_{1,s}}{\partial v^{2}}-\frac{v^{2}}{v_{th,s^{\prime}}^{2}}\Big(1-\frac{m_{s}}{m_{s^{\prime}}}\Big)v\frac{\partial f_{1,s}}{\partial v}\Big]+\nu_{D,ss^{\prime}}v\frac{\partial f_{1,s}}{\partial v}+4\pi\Gamma_{ss^{\prime}}\frac{m_{s}}{m_{s}^{\prime}}F_{M,s^{\prime}}f_{1,s}(12)

CFC_{F}is the field-particle scattering operator with Rosenbluth potentialsHs′H_{s^{\prime}}andGs′G_{s^{\prime}}CF,s​s′\displaystyle C_{F,ss^{\prime}}=Γs​s′​FM,s​[2​v2vt​h,s4​∂2Gs′∂v2−2​vvt​h,s2​(1−msms′)​∂Hs′∂v−2vt​h,s2​Hs′+4​π​msms′​f1,s′]\displaystyle=\Gamma_{ss^{\prime}}F_{M,s}\Big[\frac{2v^{2}}{v_{th,s}^{4}}\frac{\partial^{2}G_{s^{\prime}}}{\partial v^{2}}-\frac{2v}{v_{th,s}^{2}}\Big(1-\frac{m_{s}}{m_{s^{\prime}}}\Big)\frac{\partial H_{s^{\prime}}}{\partial v}-\frac{2}{v_{th,s}^{2}}H_{s^{\prime}}+4\pi\frac{m_{s}}{m_{s^{\prime}}}f_{1,s^{\prime}}\Big](13)∇v2Hs′\displaystyle\nabla^{2}_{v}H_{s^{\prime}}=−4​π​f1,s′\displaystyle=-4\pi f_{1,s^{\prime}}(14)∇v2Gs′\displaystyle\nabla^{2}_{v}G_{s^{\prime}}=2​Hs′\displaystyle=2H_{s^{\prime}}(15)

The collision frequencies and related coefficients are given byνD,s​s′\displaystyle\nu_{D,ss^{\prime}}=Γs​s′​ns′v3​[erf​(v/vt​h,s′)−Ψ​(v/vt​h,s′)]\displaystyle=\frac{\Gamma_{ss^{\prime}}n_{s^{\prime}}}{v^{3}}[\mathrm{erf}(v/v_{th,s^{\prime}})-\Psi(v/v_{th,s^{\prime}})](16)ν||,ss′\displaystyle\nu_{||,ss^{\prime}}=2​Γs​s′​ns′v3​Ψ​(v/vt​h,s′)\displaystyle=2\frac{\Gamma_{ss^{\prime}}n_{s^{\prime}}}{v^{3}}\Psi(v/v_{th,s^{\prime}})(17)Γs​s′\displaystyle\Gamma_{ss^{\prime}}=4​π​qs2​qs′2​ln⁡Λs​s′(4​π​ϵ0)2​ms2\displaystyle=\frac{4\pi q_{s}^{2}q_{s^{\prime}}^{2}\ln\Lambda_{ss^{\prime}}}{(4\pi\epsilon_{0})^{2}m_{s}^{2}}(18)Ψ​(x)\displaystyle\Psi(x)=12​x2​[erf​(x)−2​xπ​exp⁡(−x2)]\displaystyle=\frac{1}{2x^{2}}\Big[\mathrm{erf}(x)-\frac{2x}{\sqrt{\pi}}\exp(-x^{2})\Big](19)

whereln⁡Λs​s′\ln\Lambda_{ss^{\prime}}is the Coulomb logarithm.

The right hand side drive term is given byRs\displaystyle R_{s}=−𝐯drift,s⋅∇ρ​(∂FM,s∂ρ)W0,s+qsTs​v||​B​⟨E||​B⟩⟨B2⟩​FM,s\displaystyle=-\mathbf{v}_{\mathrm{drift},s}\cdot\nabla\rho\Bigg(\frac{\partial F_{M,s}}{\partial\rho}\Bigg)_{W_{0,s}}+\frac{q_{s}}{T_{s}}v_{||}B\frac{\langle E_{||}B\rangle}{\langle B^{2}\rangle}F_{M,s}(20)=−(𝐯drift,s⋅∇ρ)​[1ns​∂ns∂ρ+qsTs​∂Φ0∂ρ+(xs2−32)​1Ts​∂Ts∂ρ]​FM,s\displaystyle=-(\mathbf{v}_{\mathrm{drift},s}\cdot\nabla\rho)\Big[\frac{1}{n_{s}}\frac{\partial n_{s}}{\partial\rho}+\frac{q_{s}}{T_{s}}\frac{\partial\Phi_{0}}{\partial\rho}+(x_{s}^{2}-\tfrac{3}{2})\frac{1}{T_{s}}\frac{\partial T_{s}}{\partial\rho}\Big]F_{M,s}+qsTs​v||​B​⟨E||​B⟩⟨B2⟩​FM,s\displaystyle\quad+\frac{q_{s}}{T_{s}}v_{||}B\frac{\langle E_{||}B\rangle}{\langle B^{2}\rangle}F_{M,s}(21)=(ms​v2qs​1+cos2⁡α2​B3​𝐁×∇ρ⋅∇B)​[1ns​∂ns∂ρ+qsTs​∂Φ0∂ρ+(xs2−32)​1Ts​∂Ts∂ρ]​FM,s\displaystyle=\Big(\frac{m_{s}v^{2}}{q_{s}}\frac{1+\cos^{2}\alpha}{2B^{3}}\mathbf{B}\times\nabla\rho\cdot\nabla B\Big)\Big[\frac{1}{n_{s}}\frac{\partial n_{s}}{\partial\rho}+\frac{q_{s}}{T_{s}}\frac{\partial\Phi_{0}}{\partial\rho}+(x_{s}^{2}-\tfrac{3}{2})\frac{1}{T_{s}}\frac{\partial T_{s}}{\partial\rho}\Big]F_{M,s}+qsTs​v||​B​⟨E||​B⟩⟨B2⟩​FM,s\displaystyle\quad+\frac{q_{s}}{T_{s}}v_{||}B\frac{\langle E_{||}B\rangle}{\langle B^{2}\rangle}F_{M,s}(22)

here the radial derivative of the leading order Maxwellian is
taken at constant leading order energy:W0,s=ms​v22+qs​Φ0W_{0,s}=\frac{m_{s}v^{2}}{2}+q_{s}\Phi_{0}(23)

The drive term is commonly split into three linearly independent components:Rs=(A1,s+xs2​A2,s)​(−𝐯m,s⋅∇ρ)​FM,s+A3,s​B​v||​FM,sR_{s}=(A_{1,s}+x_{s}^{2}A_{2,s})(-\mathbf{v}_{m,s}\cdot\nabla\rho)F_{M,s}+A_{3,s}Bv_{||}F_{M,s}(24)

where the thermodynamic forces are given byA1,s\displaystyle A_{1,s}=1ns​∂ns∂ρ−qs​EρTs−32​1Ts​∂Ts∂ρ,\displaystyle=\frac{1}{n_{s}}\frac{\partial n_{s}}{\partial\rho}-\frac{q_{s}E_{\rho}}{T_{s}}-\frac{3}{2}\frac{1}{T_{s}}\frac{\partial T_{s}}{\partial\rho},(25)A2,s\displaystyle A_{2,s}=1Ts​∂Ts∂ρ,\displaystyle=\frac{1}{T_{s}}\frac{\partial T_{s}}{\partial\rho},(26)A3,s\displaystyle A_{3,s}=qsTs​⟨E∥​B⟩⟨B2⟩.\displaystyle=\frac{q_{s}}{T_{s}}\frac{\langle E_{\parallel}B\rangle}{\langle B^{2}\rangle}.(27)

Given solutions to the drift kinetic equation, one can compute neoclassical
fluxes and flows, the most common of which include the per-species surface
average particle flux:⟨Γs⟩=⟨∫f1,s​𝐯drift⋅∇ρ​d3​𝐯⟩\langle\Gamma_{s}\rangle=\Bigg\langle\int f_{1,s}\mathbf{v}_{\mathrm{drift}}\cdot\nabla\rho~\mathrm{d}^{3}\mathbf{v}\Bigg\rangle(28)

per-species surface average heat flux:⟨Qs⟩=⟨∫ms​v22​f1,s​𝐯drift⋅∇ρ​d3​𝐯⟩\langle Q_{s}\rangle=\Bigg\langle\int\frac{m_{s}v^{2}}{2}f_{1,s}\mathbf{v}_{\mathrm{drift}}\cdot\nabla\rho~\mathrm{d}^{3}\mathbf{v}\Bigg\rangle(29)

per-species surface average parallel flow:⟨V||,s​B⟩=⟨B​∫v||​f1,s​𝐯drift⋅∇ρ​d3​𝐯⟩\langle V_{||,s}B\rangle=\Bigg\langle B\int v_{||}f_{1,s}\mathbf{v}_{\mathrm{drift}}\cdot\nabla\rho~\mathrm{d}^{3}\mathbf{v}\Bigg\rangle(30)

the radial current:⟨Jρ⟩=∑sqs​⟨Γs⟩\langle J_{\rho}\rangle=\sum_{s}q_{s}\langle\Gamma_{s}\rangle(31)

and the parallel current (including both bootstrap and Ohmic components):⟨J||​B⟩=∑sqs​⟨V||,s​B⟩\langle J_{||}B\rangle=\sum_{s}q_{s}\langle V_{||,s}B\rangle(32)

In addition to the full 4D problem described above,yancccan also solve a
reduced set of equations commonly called the “monoenergetic drift kinetic
equation” which is also solved by DKES[24]and MONKES[16]. For the
monoenergetic form we drop all coupling in speed, reducing the problem to 3
dimensions (2 real space coordinates and pitch angle) which also makes it
species independent:α˙​∂fj∂α+θ˙​∂fj∂θ+ζ˙​∂fj∂ζ−ν^​ℒ​fj=sj\dot{\alpha}\frac{\partial f_{j}}{\partial\alpha}+\dot{\theta}\frac{\partial f_{j}}{\partial\theta}+\dot{\zeta}\frac{\partial f_{j}}{\partial\zeta}-\hat{\nu}\mathcal{L}f_{j}=s_{j}(33)

The monoenergetic equation uses a modified set of trajectories to ensure
conservation of the magnetic moment and to remove all direct dependence on
velocity:θ˙=−cos⁡α​BθB−Bζ⟨B2⟩​g​E^ρ\dot{\theta}=-\frac{\cos{\alpha}~B^{\theta}}{B}-\frac{B_{\zeta}}{\langle B^{2}\rangle\sqrt{g}}\hat{E}_{\rho}(34)ζ˙=−cos⁡α​BζB+Bθ⟨B2⟩​g​E^ρ\dot{\zeta}=-\frac{\cos{\alpha}~B^{\zeta}}{B}+\frac{B_{\theta}}{\langle B^{2}\rangle\sqrt{g}}\hat{E}_{\rho}(35)α˙=−sin⁡α2​B2​(Bθ​∂B∂θ+Bζ​∂B∂ζ)\dot{\alpha}=-\frac{\sin{\alpha}}{2B^{2}}\Bigg(B^{\theta}\frac{\partial B}{\partial\theta}+B^{\zeta}\frac{\partial B}{\partial\zeta}\Bigg)(36)

Here the monoenergetic electric field is defined asE^ρ=Eρ/v\hat{E}_{\rho}=E_{\rho}/v.
In the collision operator we keep only the Lorentz pitch angle scattering with
the monoenergetic collisionalityν^=∑s′νD,s​s′/v\hat{\nu}=\sum_{s^{\prime}}\nu_{D,ss^{\prime}}/v. The
right hand side is made up of 3 components corresponding to the three
thermodynamic forces, and the equation is solved once for each right hand side:s1\displaystyle s_{1}=1+cos2⁡α2​B3​𝐁×∇ρ⋅∇B\displaystyle=\frac{1+\cos^{2}\alpha}{2B^{3}}\mathbf{B}\times\nabla\rho\cdot\nabla B(37)s2\displaystyle s_{2}=s1\displaystyle=s_{1}(38)s3\displaystyle s_{3}=−cos⁡α​B\displaystyle=-\cos{\alpha}~B(39)

giving the three monoenergetic solutionsf1,f2,f3f_{1},f_{2},f_{3}. These are then used
to compute the so called monoenergetic transport coefficientsDi​j=⟨∫0πsi​fj​sin⁡α​d​α⟩D_{ij}=\Bigg\langle\int_{0}^{\pi}s_{i}f_{j}\sin{\alpha}~\mathrm{d}\alpha\Bigg\rangle(40)

## 2.1Boundary conditions

Using generalized angle like coordinates in real space allows us to use simple
periodic boundary conditions in(θ,ζ)(\theta,\zeta), as opposed to more
complicated conditions required when using field line following coordinates
such as in KNOSOS[49]. Using the pitch angleα\alphagives symmetric
boundary conditions atα=0\alpha=0andα=π\alpha=\pi, requiringf​(−α)=f​(α)f(-\alpha)=f(\alpha)andf​(π−α)=f​(π+α)f(\pi-\alpha)=f(\pi+\alpha), as opposed to a
regularity type condition that appears when usingξ=−cos⁡α\xi=-\cos\alpha. In
speed, we require thatf→0f\rightarrow 0asx→∞x\rightarrow\inftywhich we will
impose with the choice of basis for the speed coordinate in
Section3.

## 2.2Properties of the drift kinetic equation

Both the forms of the drift kinetic equation have the form of a linear
advection diffusion equation, for which there is a rich history of methods[34]. The prototypical equation for linear advection
diffusion is𝐰⋅∇f−ν​∇2f=S\mathbf{w}\cdot\nabla f-\nu\nabla^{2}f=S(41)

however, several features of the drift kinetic equation make it more
complicated than the prototypical example. In the prototypical equation, the
problem generally becomes easier forν≫1\nu\gg 1as it becomes more Poisson
like, while it becomes singular asν→0\nu\rightarrow 0. In the drift kinetic
equation the diffusive term (the collision operator) acts only in velocity
space, so the diffusion is highly anisotropic – there is zero diffusion in the
real space coordinates. This makes the equation singular in both limits of
collisionality, asν→∞\nu\rightarrow\inftywe lose coupling in real space. In
practice this is only a minor issue, as the normalized collisionalityν∗\nu^{*}is typically in the range(10−4,10−2)(10^{-4},10^{-2})though for impurities it can be
several orders of magnitude larger.

Another important feature of the drift kinetic equation is that all
collisionless characteristics are effectively closed. This is strictly true for
trapped particles, as well as passing particles on rational surfaces. On
irrational surfaces, the trajectories approximately close after a sufficient
number of transits. The periodic boundary conditions in real space combined
with the symmetry/reflecting boundaries in pitch angle means that no
information enters or leaves the domain, which will affect the choice of
smoothing operation in the multigrid scheme, described in
Section4.2.

One can show[30]that the drift kinetic equation
has a null space of
dimension2​ns2n_{s}wherensn_{s}is the number of species consisting off1,s=cs​FM,sf_{1,s}=c_{s}F_{M,s}andf1,s=cs​v2​FM,sf_{1,s}=c_{s}v^{2}F_{M,s}wherecsc_{s}is an
arbitrary constant. The monoenergetic form has a null space of dimension 1,
corresponding tofj=cf_{j}=cfor some constantcc. To remove this null space, we
impose additional gauge constraints. For the full drift kinetic equation, we
require that all of the density and pressure reside in the leading order
Maxwellian for each species:⟨∫f1,s​d3​𝐯⟩\displaystyle\Bigg\langle\int f_{1,s}~\mathrm{d}^{3}\mathbf{v}\Bigg\rangle=0\displaystyle=0(42)⟨∫v2​f1,s​d3​𝐯⟩\displaystyle\Bigg\langle\int v^{2}f_{1,s}~\mathrm{d}^{3}\mathbf{v}\Bigg\rangle=0\displaystyle=0(43)

In addition to this gauge freedom, one can also show that the steady state
drift kinetic equation requires an additional source for it to be solvable whenEρE_{\rho}is nonzero and not at its ambipolar value (ieEρE_{\rho}such thatJρ=0J_{\rho}=0). To account for this we add additional terms that serve as a source
of particles and heat for each species to ensure solvability for arbitraryEρE_{\rho}. For the trajectory models considered here the particle source is not
strictly necessary (the source is always zero at the solution) but it helps by
making the overall system square, and is needed when alternative trajectory
models are considered[30]. The source term for each
species has the form:Ss​(xs)=Ss,p​(xs)​FM,s​(xs)​(xs2−52)+Ss,h​(xs)​FM,s​(xs)​(xs2−32)S_{s}(x_{s})=S_{s,p}(x_{s})F_{M,s}(x_{s})(x_{s}^{2}-\tfrac{5}{2})+S_{s,h}(x_{s})F_{M,s}(x_{s})(x_{s}^{2}-\tfrac{3}{2})(44)

whereSs,pS_{s,p}andSs,hS_{s,h}are the free parameters to be solved for.

For the monoenergetic equation, the only gauge freedom that exists is the
choice of the average offjf_{j}. One could impose an additional constraint
requiring eg, zero average, but it is simplier to just require thatfftake a
fixed value at a given point:fj​(α=π/2,θ=0,ζ=0)=constf_{j}(\alpha=\pi/2,\theta=0,\zeta=0)=\mathrm{const}(45)

The final important feature, which also appears in the prototypical equation, is
the presence of internal boundary layers that develop in the solution with a
characteristic widthν\sqrt{\nu}. These layers correspond to the accumulation
of particles near transitions between trapping regions[23,25], and
necessitates very high resolution, primarily in the real space and pitch angle
coordinates.

## 3Discretization

Because the location of boundary layers doesn’t depend on speedxsx_{s}, we can
often get away with a relatively coarse discretization in the speed coordinate.
Following SFINCS[30], we use a collocation approach
based on weighted Maxwell
polynomials, which are orthogonal on(0,∞)(0,\infty)with respect to the weight
functione−x2e^{-x^{2}}[31]. In practice we usually only need
5–10 points in the speed
coordinate with this discretization.

One could consider using a fully spectral method for the drift kinetic
equation, which has been sucessfully used for the monoenergetic form in DKES
and MONKES, however we found that these did not scale well when applied to the
full 4D problem. Due to the sharp boundary layers that develop at low
collisionality, any method requires a large number of grid points or spectral
collocation points to sufficiently resolve these, so the usual reduction in
resolution possible with spectral methods for smooth solutions isn’t possible.
Additionally, spectral methods tend to give dense matrices (though using
Legendre polynomials for pitch angle results in a block pentadiagonal system,
the block size would bens​nx​nθ​nζn_{s}n_{x}n_{\theta}n_{\zeta}which can be quite large).

Because of this, in all other coordinates we adopt a finite difference
discretization with a defect correction approach where we use a 2nd order
scheme for the preconditioner and a 4th order scheme for the main operator. We
use uniform grids inα,θ,ζ\alpha,\theta,\zeta, with full index grids inθ,ζ\theta,\zetaand half index grid inα\alpha:α\displaystyle\alpha=π​(2​j+1)2​nα\displaystyle=\frac{\pi(2j+1)}{2n_{\alpha}}\quadj∈[0,1,…,nα−1]\displaystyle j\in[0,1,...,n_{\alpha}-1](46)θj\displaystyle\theta_{j}=2​π​jnθ\displaystyle=\frac{2\pi j}{n_{\theta}}\quadj∈[0,1,…,nθ−1]\displaystyle j\in[0,1,...,n_{\theta}-1](47)ζj\displaystyle\zeta_{j}=2​π​jNF​P​nζ\displaystyle=\frac{2\pi j}{N_{FP}~n_{\zeta}}\quadj∈[0,1,…,nζ−1]\displaystyle j\in[0,1,...,n_{\zeta}-1](48)

whereNF​PN_{FP}is the number of field periods of the underlying equilibrium (a
discrete toroidal symmetry common in stellarators). We use standard centered
differences differences for the collision operator, with the Lorentz pitch angle
scattering operator being explicitly split into first and second derivative
parts, with centered differences applied to each:ℒ=1sin⁡α​∂∂α​sin⁡α​∂∂α=∂2∂α2+cos⁡αsin⁡α​∂∂α\mathcal{L}=\frac{1}{\sin\alpha}\frac{\partial}{\partial\alpha}\sin\alpha\frac{\partial}{\partial\alpha}=\frac{\partial^{2}}{\partial\alpha^{2}}+\frac{\cos\alpha}{\sin\alpha}\frac{\partial}{\partial\alpha}(49)

Using the half index grid inα\alphaavoids the singular behavior atα=0\alpha=0andα=π\alpha=\pi. To enforce boundary conditions inα\alphawe
mirrorffaround the endpoints which explicitly enforcesf​(−α)=f​(α)f(-\alpha)=f(\alpha)andf​(π−α)=f​(π+α)f(\pi-\alpha)=f(\pi+\alpha).

For the advective terms we use an upwinded stencil. The “standard” 2nd/4th
order upwind scheme uses stencil points(0,1,2)(0,1,2)and(0,1,2,3,4)(0,1,2,3,4)respectively,
where these integers give the relative grid indices for a forward difference, with0being the point the derivative is being evaluated at, positive numbers are grid
points to the right, negative to the left; indices are reversed about 0 for backward
differences.
In contrast, we use a modified stencil containing the points(0,1,4)(0,1,4)(2nd
order) and(−2,0,1,3,4)(-2,0,1,3,4)(4th order). These wider stencils give a larger
element on the diagonal relative to the off-diagonals, resulting in matrices
with a higher degree of diagonal dominance. We quantify this diagonal dominance with
the ratiodd:d=|ai​i|∑j≠i|ai​j|.d=\frac{|a_{ii}|}{\sum_{j\neq i}|a_{ij}|}.(50)

A matrix withd>1d>1is diagonally dominant in the traditional sense. In
Table1we compare the stencils and coefficients for our
widened 2nd and 4th order schemes vs the standard upwinded stencils, comparing
the degree of diagonal dominance along with the magnitude of the leading order
error constant. We find that these more diagonally dominant stencils
significantly improve the multigrid smoothing (see Section4.2)
with negligible loss in accuracy.SchemeStencilCoefficientsdd|leading error||\text{leading error}|standard 2nd order(0,1,2)(0,1,2)1h​(−32,2,−12)\frac{1}{h}(-\frac{3}{2},2,-\frac{1}{2})0.600.33wide 2nd order(0,1,4)(0,1,4)1h​(−54,43,−112)\frac{1}{h}(-\frac{5}{4},\frac{4}{3},-\frac{1}{12})0.880.67standard 4th order(0,1,2,3,4)(0,1,2,3,4)1h​(−2512,4,−3,43,−14)\frac{1}{h}(-\frac{25}{12},4,-3,\frac{4}{3},-\frac{1}{4})0.240.20wide 4th order(−2,0,1,3,4)(-2,0,1,3,4)1h​(−115,−1312,43,−415,112)\frac{1}{h}(-\frac{1}{15},-\frac{13}{12},\frac{4}{3},-\frac{4}{15},\frac{1}{12})0.620.20Table 1:Comparison of the widened upwind stencils used inyanccagainst the
standard upwind stencils, showing the diagonal dominance ratioddand the
magnitude of the leading order error constant. Our widened stencils have a larger
relative magnitude on the diagonal for similar error.

An important requirement when considering discretizations for a multigrid
scheme is to ensure numerical stability not just at the finest grid level but at
all levels. Using upwinded finite differences achieves this by adding artificial
numerical diffusion to avoid small grid scale oscillations that can happen when
under-resolving sharp features. This increased numerical stability is not
without cost though. Because the additional diffusion is proportional to the
grid spacing, coarser grids effectively have higher diffusion, which can make
them a poor approximation to the true fine grid problem, causing convergence
issues for a multigrid scheme. This is a well known problem when using multigrid
for advection diffusion problems[47]and
techniques to mitigate it will be
discussed in Section4.3.

The integrals required for output moments are computed with spectral accuracy in
all coordinates. Inxxwe use the Gaussian quadrature weights associated with
the Maxwell polynomials, while inθ,ζ\theta,\zetawe use standard trapezoidal
quadrature which is spectrally accurate for periodic integrands. Inα\alphawe
use Fejer type 1 quadrature which is equivalent to Chebyshev quadrature inξ=−cos⁡α\xi=-\cos\alpha.

For the field part of the collision operator, there are a number of possible
ways to discretize the Rosenbluth potentials. One could treat them as additional
unknowns and solve a system of equations forf,G,Hf,G,H, but we adopt a Green’s
function approach to analytically solve the Poisson equations forG,HG,H[33]. The details of this derivation are given in
AppendixA.

## 4Multigrid method and Krylov solver

When discretized, the drift kinetic equation becomes a large, sparse linear
system of the formA​f=sAf=s. The matrixAAis banded inθ\thetaandζ\zeta(due
to the finite difference discretization), and dense inα\alphaandxx(due to
the spectral collocation inxxand the integral terms in the collision operator
forα\alpha). The monoenergetic equation is banded in all three coordinates(α,θ,ζ)(\alpha,\theta,\zeta). Due to the high resolution required to resolve the
trapped passing boundary, the resulting system typically has∼106−107\sim 10^{6}-10^{7}degrees of freedom (∼105\sim 10^{5}is typical for the monoenergetic problem). At
this size for this problem, direct sparse solvers were found to be quite poor,
with scipy’sspsolve[50,14]failing to solve even the monoenergetic
problem in a reasonable time.

A more efficient approach is to use a Krylov method like GMRES combined with a
good preconditioner. Existing codes like SFINCS use a sparse LU factorization of
an approximateAAas a preconditioner, which tends to work well at low to
moderate collisionality, at the cost of a significant amount of memory (often
100s of GB) to perform the sparse factorization. Additionally, by dropping
certain terms from the preconditioner, it becomes far less effective at high
collisionality, requiring many more Krylov iterations. Finally, sparse matrix
factorizations tend to see minimal speedup on GPU, due to the irregular memory
access[41,17,11].

We opt for a different approach, using a multigrid preconditioner combined with
an outer Krylov solver. The main elements of a multigrid scheme are a hierarchy
of grids, a smoothing operation, and a coarse grid correction. The basic idea is
as follows:
- 1.

Starting from some initial guess on a fine grid, apply a smoothing
operation which reduces the high frequency components of the error.
- 2.

Restrict the fine grid problem down to a coarser grid. Because the
smoothing eliminated the high frequency error, the coarse grid problem now
captures the dominant error.
- 3.

Solve the coarse grid problem (possibly approximately) to obtain a
correction.
- 4.

Interpolate this correction back to the fine grid.
- 5.

Repeat.

The key idea is that step 3 can be done recursively, using additional coarser
levels to reduce the problem size until it is small enough to solve directly. In
the ideal case, multigrid methods can achieve a grid independent rate of
convergence, where each pass through the multigrid cycle reduces the error by a
fixed fraction, regardless of resolution, meaning that the number of iterations
required to achieve a given error tolerance is constant as the resolution is
increased (compared to many other methods which require a larger number of
iterations at higher resolution). For advection-diffusion problems obtaining
ideal multigrid convergence is generally difficult, but even in this case it can
be a highly efficient preconditioner.

## 4.1Grid hierarchy

The first ingredient in a multigrid scheme is a hierarchy of different grids and
a method to transfer information between them. The resolution on the finest grid
is chosen to properly represent the physics of the problem with our given
discretization. We then must define how the coarse grids are constructed.
Because even the finest grid generally requires very low resolution inxx(nx∼5n_{x}\sim 5–1010) we find little benefit in coarsening thexxcoordinate, so
we retain the finestxxgrid across all levels. This is a form of
“semi-coarsening” where one only coarsens the grid in certain directions. In
the other coordinates(α,θ,ζ)(\alpha,\theta,\zeta)we coarsen by a factor of 2 in
each direction each time we go down a grid level, for a total reduction in cost
of roughly 8 per grid level. We find that increasing the coarsening factor in
each coordinate to 3 or even 4 only moderately degrades solver performance.
Semi-coarsening in other coordinates was also considered but was found to be
significantly more expensive in time and memory per iteration (due to the
correspondingly larger coarse grids) without a significant decrease in the
number of iterations.

The final choice in grid hierarchy is when to stop coarsening. For simple
problems one can coarsen extremely far, until the coarsest grid contains only a
single node. In our case we find that using a larger coarse grid improves
performance. Typically we coarsen until the coarsest grid has a few thousand
degrees of freedom at which point we directly solve the coarsest grid system
with a dense LU factorization. Going coarser than this is generally inefficient,
as dense linear algebra on GPU is very fast, as well as the increased overhead
of more grid levels. Using an exact solve on a larger grid also reduces the
effects of the additional numerical diffusion on the coarse grid discussed in
Section4.3.

In addition to the grid hierarchy, we must define operations for moving
information between grids. These are generally referred to as restriction
(moving from fine to coarse) and prolongation (from coarse to fine). There are a
number of methods for restriction/prolongation in use in the literature. A
common approach is to use operator dependent methods,[13]where one
considers the direction of flow and diffusive coupling to determine how to move
between grids. We find in our case that prolongating with simple piecewise
linear interpolation is sufficient, with higher order interpolation or operator
dependent methods increasing the per iteration cost and complexity without a
noticeable decrease in the required number of iterations. For restriction we use
the volume weighted transpose of the prolongation operator.

## 4.2Smoothing

The next key ingredient for a multigrid scheme is an efficient smoothing
operation. For linear problems, this typically takes the form of a classical
relaxation method which takes the formfk+1=fk+ωs​K−1​(s−A​fk)f_{k+1}=f_{k}+\omega_{s}K^{-1}(s-Af_{k})(51)

whereKKis some approximation ofAAandωs\omega_{s}is a
damping/under-relaxation parameter. For Poisson type problems the standard
choice isK=diag​(A)K=\mathrm{diag}(A), however for advective or anisotropic diffusion
problems this is generally poor due to strong coupling along characteristics
which is ignored by the diagonal approximation. For advection problems, it is
common to takeKKas the upper or lower triangle ofAA, or a block triangular
approximation where one keeps full coupling in some coordinates and triangular
coupling in others. For problems with open characteristics and Dirichlet
boundary conditions this can be extremely efficient, as the smoothing operation
takes the known boundary value and sweeps it in along characteristics, reducing
the error at all frequencies across the entire domain. As discussed previously
however, the drift kinetic equation has periodic boundary conditions and a wide
variety of closed characteristics. Because of this, instead of a triangular
approximation ofAAwe instead use a block diagonal approximation for
smoothing. This is significantly cheaper to apply (especially on GPU) and
performs just as well in practice.

When using a block diagonal approximation, the choice of coordinate ordering
determines which matrix elements are on the block diagonal and are thus retained
in the smoothing operation. To avoid having to make an explicit choice, we
consider a family of block diagonal smoothers, which each maintain full coupling
along one coordinate[37,15]. IfAAis our original matrix, andPjP_{j}is a
permutation matrix that reorders the coordinates to put coordinatej∈(x,α,θ,ζ)j\in(x,\alpha,\theta,\zeta)on the block diagonal, then we takeKj=Pj−1​block​_​diag​(Pj​A​Pj−1)​PjK_{j}=P^{-1}_{j}\mathrm{block\_diag}(P_{j}AP_{j}^{-1})P_{j}, giving 4 smoothers (3
for the monoenergetic problem) which each preferentially smooth the errors in a
different direction. One full smoother pass consists of applying these 4
smoothers in sequence to a given estimate of the solution.

This choice of block diagonal smoothing matrices is aided by our choice of
finite difference stencil (Table1), which makes the matrices
more diagonally dominant compared to standard upwinded methods. This larger
element on the diagonal means a block diagonal approximation captures more of
the behavior ofAA, resulting in a more efficient smoother. We can measure the
efficiency of the smoother by considering the operator that multiplies the error
at each smoothing step:fk+1−fe​x​a​c​t≡ek+1=(I−ωs​K−1​A)​ekf_{k+1}-f_{exact}\equiv e_{k+1}=(I-\omega_{s}K^{-1}A)e_{k}(52)

We can then considerr=‖L​(I−ωs​K−1​A)‖‖L‖r=\frac{||L(I-\omega_{s}K^{-1}A)||}{||L||}(53)

whereLLis some approximate high pass filter, which following[18]we take
to be the discrete Laplacian on our phase space. This ratiorrgives a measure
of how much the smoother is reducing the high frequency errors (lower is
better). In Figure1we compare this ratio for the block
diagonal smoothers in each coordinate for our upwinded stencil vs the “QUICK”
method (Quadratic Upstream Interpolation for Convective Kinematics, from[32]) on the monoenergetic problem. In both cases we first
optimize the
damping parameterωs\omega_{s}to achieve the lowestrrpossible for each
collisionality considered across a range of different geometries and electric
fields. We see that our method allows a larger damping parameter and gives much
lower smoothing factor, indicating that more of the high frequency error is
eliminated per application, especially at low collisionality forθ\theta,ζ\zetaand across all collisionalities forα\alpha. For the full drift kinetic
equation, which spans several orders of magnitude in collisionality, we find that a
fixed damping parameter ofωs=0.6\omega_{s}=0.6works best.Figure 1:Smoothing factorrrfor the block diagonal smoothers in each
coordinate, comparing the widened upwind stencil used inyanccagainst the
QUICK scheme on the monoenergetic problem, as a function of collisionality. Using
a wider stencil with a larger diagonal significantly improves the smoothing property.

Because we use a finite difference discretization, the block diagonal itself is
banded for permutations that coupleθ\thetaandζ\zeta, and approximately
banded for permutations that coupleα\alpha(for the smoothing operation we
drop the off band terms corresponding to the integrals in the field part of the
collision operator). This significantly reduces the memory required to store the
smoothers, and due to the larger elements on the diagonal we find that an
unpivoted banded LU factorization is stable, which avoids fill in and irregular
memory access.

## 4.3Coarse grid problem

The standard coarse grid correction takes the form offk+1,f​i​n​e=fk,f​i​n​e+ωc​P​Ac​o​a​r​s​e−1​R​(sf​i​n​e−Af​i​n​e​fk,f​i​n​e)f_{k+1,fine}=f_{k,fine}+\omega_{c}PA^{-1}_{coarse}R(s_{fine}-A_{fine}f_{k,fine})(54)

WhereRRis the restriction operator from fine grid to coarse grid,PPis the
prolongation operator from coarse grid to fine grid, and as in the smoothing we
allow for a damping parameterωc\omega_{c}.

An important consideration in a multigrid scheme is the choice of how to
discretize the coarse grid problem. The two primary methods are direct
discretization, and Galerkin projection. In the direct method, we simply
re-discretize the original problem on the coarser grid, using the same
underlying finite difference method. This has the advantage of being cheap to
implement and apply. Galerkin projection takesAc​o​a​r​s​e=R​Af​i​n​e​PA_{coarse}=RA_{fine}P(55)

This is commonly used in algebraic multigrid schemes and is often recommended
when dealing with advective problems, however it can require more memory and be
difficult to implement in a matrix free manner. The additional memory is due to
the Galerkin projection changing the sparsity structure, meaning that in many
casesAc​o​a​r​s​eA_{coarse}can have more nonzero elements thanAf​i​n​eA_{fine}, especially
when combined with semi-coarsening. This also makes coarse grid operations
proportionally more expensive. Additionally, in our case we wish to avoid ever
materializing even a sparse representation ofAf​i​n​eA_{fine}to keep memory usage
low. This is easy when doing direct re-discretization, as applyingAf​i​n​eA_{fine}andAc​o​a​r​s​eA_{coarse}consist of convolutions, small tensor contractions and
elementwise operations, withAc​o​a​r​s​eA_{coarse}being orders of magnitude smaller and
thus cheaper. With a Galerkin projection however, applyingAc​o​a​r​s​eA_{coarse}in a
matrix free manner requires interpolating the coarse grid residual back to the
fine grid, applyingAf​i​n​eA_{fine}, then restricting. This means that the cost of
the coarse grid operations is as expensive as the fine grid, which
significantly increases the cost of the multigrid cycle. For these reasons we
opt for direct rediscretization which we find works sufficiently well in
practice.

## 4.4Cycle type

The final element of the multgrid scheme to consider is the cycle type,
governed by the “cycle index”. A cycle index of 1 corresponds to a “V”
cycle, where we visit each coarser grid once per cycle. Cycle index 2
corresponds to a “W” cycle, where we visit each coarser grid twice, etc. These
are shown diagrammatically in Figure2. We find that for the
drift kinetic equation cycle index 1 is the most robust. As discussed above, the
coarse grid correction can be unreliable due to additional numerical diffusion,
so higher order cycles that apply this less accurate coarse grid correction more
often tend to slow the solver down. For the monoenergetic equation however, we
find that this is less of an issue and using cycle index 3 tends to be most
efficient.Figure 2:Schematic of multigrid cycle types (V-, W-, and higher cycle indices)
across the grid hierarchy.

## 4.5Krylov solver

For many problems a well tuned multigrid method works efficiently as a
standalone solver, however this is often not the case for advection diffusion
equations. This can be seen in Figure3, where we plot the
spectrum of the discretized drift kinetic equationAA, as well asI−M​AI-MAwhereMMis the multigrid preconditioner. This matrix is what multiplies the error at
each step of a pure multigrid cycle. If all of its eigenvalues are within the
unit circle then pure multigrid would converge. We see that in practice, the
multigrid preconditioner clusters the vast majority of the eigenvalues near
zero, which means they are very efficiently damped. However there are several
eigenvalues near the unit circle which are only weakly damped which would slow
convergence, and there can also be outliers that would cause divergence in a
pure multigrid scheme. To handle this, we use multigrid as a preconditioner for
a Krylov solver. We use a right preconditioned GCROT[12,21]with inner GMRES[39,40]. The largest memory requirement is
typically storing the Krylov
subspace, so we limit the inner GMRES to 150 iterations before restarting. This
is more than enough for the majority of cases tested, and the outer GCROT loop
efficiently handles restarting by preserving the most important elements of the
Krylov subspace between restarts rather than starting from scratch as in
standard restarted GMRES.Figure 3:Spectrum of the discretized drift kinetic operatorAAand of the
preconditioned error operatorI−M​AI-MA, whereMMis the multigrid
preconditioner.

## 5Benchmarks

## 5.1W7-X monoenergetic DKE

As a first example we solve the monoenergetic drift kinetic equation for the
KJM configuration of W7-X over a range of collisionality and electric field. The
results are shown in Figure4, comparingyanccvs MONKES[16]. Both codes are converged to within 1% across the
full range of
collisionality. The resolutions for each code are given in Table2.ρ\rho0.450.45ν^=νD/v\hat{\nu}=\nu_{D}/v∈[1×10−4,3×101]\in[1\times 10^{-4},3\times 10^{1}]Er^=Er/v\hat{E_{r}}=E_{r}/v[0,10−3][0,10^{-3}]MONKES resolution(nl,nθ,nζ)(n_{l},n_{\theta},n_{\zeta})(180,39,99)(180,39,99)yanccresolution(nα,nθ,nζ)(n_{\alpha},n_{\theta},n_{\zeta})(201,31,81)(201,31,81)Table 2:Parameters and resolutions for the W7-X monoenergetic benchmark.Figure 4:Monoenergetic transport coefficientsDi​jD_{ij}for the W7X-KJM
configuration, comparingyanccagainst MONKES over a range of collisionality
and electric field.

For a performance comparison, we re-implement the MONKES algorithm in JAX and
compare time and memory required to solve the monoenergetic equation. Both codes
run on the same hardware (Nvidia A100 GPU) to isolate algorithmic differences.
For this problem,yanccrequired 4GB of memory, while MONKES required only
1.4 GB. This is likely due to the use of a Legendre discretization in MONKES,
and the fact that the monoenergetic coefficients depend only on the first 2
Legendre modes, so very little storage is required. The tradeoff is that MONKES
must invert a large number of dense matrices of size(nθ​nζ)×(nθ​nζ)(n_{\theta}n_{\zeta})\times(n_{\theta}n_{\zeta}), which costsO​(nθ3​nζ3)O(n_{\theta}^{3}n_{\zeta}^{3}), whileyanccrequires only operations that scale
linearly with resolution. A timing comparison is shown in
Figure5, showingyanccis2×2\times–4×4\timesfaster for
this problem over most of the collisionality range, though slowing down to
roughly equal at the lowest collisionality. On problems with simpler geometry
that require less resolution in the two flux surface angles, the MONKES
algorithm will likely be faster. As for the discretization and resolution
required, in this case they are broadly similar despite MONKES using a spectral
discretization in all 3 coordinates. This is likely because the solutions are
not sufficiently smooth for spectral convergence to show an advantage. If higher
accuracy is desired then a fully spectral approach would be more efficient
asymptotically, but at this level of accuracy common in optimization and
analysis there is little difference.Figure 5:Timing comparison betweenyanccand a JAX re-implementation of the
MONKES algorithm for the monoenergetic problem, as a function of
collisionality.

## 5.2Single-species density scan

For the full drift kinetic equation, we compareyanccto SFINCS[30], here
for a single species scan in density / collisionality using an NCSX like
equilibrium. The parameters are summarized in Table3, and a
comparison of the output fluxes (heat flux⟨Q⟩\langle Q\rangle, particle flux⟨Γ⟩\langle\Gamma\rangle, and parallel flow⟨V||​B⟩\langle V_{||}B\rangle) is shown
in Figure6, where again both codes are converged to within
1%.ρ\rho0.50.5Er=Eρ/aE_{r}=E_{\rho}/a−1​kV/m-1~\mathrm{kV/m}TT800​eV800~\mathrm{eV}nn∈[1.5×1019,1.5×1022]​m−3\in[1.5\times 10^{19},1.5\times 10^{22}]~\mathrm{m}^{-3}a/LTa/L_{T}0.810.81a/Lna/L_{n}0.860.86ν∗=R​νDvt​h​ι\nu^{*}=\frac{R\nu_{D}}{v_{th}\iota}5.2×10−3−4.1×1005.2\times 10^{-3}-4.1\times 10^{0}SpeciesHydrogenSFINCS resolution(nx,nξ,nθ,nζ)(n_{x},n_{\xi},n_{\theta},n_{\zeta})(7,141,25,81)(7,141,25,81)yanccresolution(nx,nα,nθ,nζ)(n_{x},n_{\alpha},n_{\theta},n_{\zeta})(7,121,43,65)(7,121,43,65)Table 3:Parameters and resolutions for the single-species NCSX density scan.Figure 6:Output fluxes (heat flux, particle flux, and parallel flow) for the
single-species NCSX density scan, comparingyanccand SFINCS.

A timing comparison is shown in Figure7across the full range
of collisionality. For this case SFINCS was run on 128 CPU cores, whileyanccwas run on a single Nvidia A100 GPU, both on the Perlmutter cluster at NERSC and
both using 64 bit floats. We see a speedup of roughly 5x across the full range,
up to nearly 2 orders of magnitude at higher collisionality where SFINCS slows
down significantly. This is likely because the default preconditioner in SFINCS
drops coupling in the speed coordinate, effectively ignoring energy scattering
which becomes important at high collisionality. On the other handyanccremains relatively flat, showing only modest slowdown at low or high
collisionality. The times foryanccdo not include the cost of just in time
compilation in JAX which must be paid once for a given resolution, after which
the JIT compiled code is re-used across the scan. This is most representative of
real world use where the DKE is solved repeatedly for parameter scans or
optimization tasks.

Due to the different hardware this is not a strictly fair comparison, but to get
a rough estimate we can compare peak theoretical flops. Assuming we could run
SFINCS on GPU with the same overall efficiency as on CPU (unlikely due to the
poor scaling of sparse matrix factorizations on GPU), we would expect a speedup
of roughly 3 going from 128 CPU to 1x A100. We can then see that the speedup
fromyanccis due to both being able to run on GPU as well as purely
algorithmic improvements that are independent of hardware. In addition to the
speed improvement,yanccalso shows a clear win on memory usage. For these
runs, SFINCS needed more than 50 GB, whileyanccneeded only 6 GB, which is
especially important for GPU based codes since GPU memory is often a bottleneck.Figure 7:Timing comparison betweenyancc(1x A100 GPU) and SFINCS (128 CPU
cores) for the single-species NCSX density scan, across collisionality.

## 5.3Two-speciesEρE_{\rho}scan

To confirm the correctness for the 2 species case with full interspecies
collisions and the ambipolarity condition we consider the same NCSX like
equilibrium but perform a scan in radial electric field for 2 species, electrons
and hydrogen. The parameters are given in Table4and the
results shown in Figure8. As before both codes are converged to
within 1% for the particle and heat fluxes and parallel flows (particle flux
and heat flux agree to <1%, the parallel flow is often the hardest to
converge). Composite quantities such as the radial and parallel currents are
also shown. The parallel current shows slightly larger disagreement (∼5%\sim 5\%), which is to be expected as it is the difference of parallel flows.

As with the comparison to MONKES, we see thatyanccrequires broadly
similar resolution to SFINCS, though in some cases SFINCS can use slightly
coarser resolution in the flux surface coordinates. This is likely due to the
centered differences that SFINCS uses, which avoids the extra numerical
diffusion caused by upwinding. The cost of this can be stability, and we find
that in some casesyancccan get away with coarser resolution.ρ\rho0.50.5Er=Eρ/aE_{r}=E_{\rho}/a∈[−8,8]​kV/m\in[-8,8]~\mathrm{kV/m}TH=TeT_{H}=T_{e}800​eV800~\mathrm{eV}nH=nen_{H}=n_{e}1.5×1020​m−31.5\times 10^{20}~\mathrm{m}^{-3}a/LT,H=a/LT,ea/L_{T,H}=a/L_{T,e}0.810.81a/Ln,H=a/Ln,ea/L_{n,H}=a/L_{n,e}0.860.86νH∗=R​νD,Hvt​h,H​ι\nu^{*}_{H}=\frac{R\nu_{D,H}}{v_{th,H}\iota}5.0×10−25.0\times 10^{-2}νe∗=R​νD,evt​h,e​ι\nu^{*}_{e}=\frac{R\nu_{D,e}}{v_{th,e}\iota}1.3×10−11.3\times 10^{-1}SpeciesHydrogen, ElectronsSFINCS resolution(nx,nξ,nθ,nζ)(n_{x},n_{\xi},n_{\theta},n_{\zeta})(7,61,15,31)(7,61,15,31)yanccresolution(nx,nα,nθ,nζ)(n_{x},n_{\alpha},n_{\theta},n_{\zeta})(7,61,25,37)(7,61,25,37)Table 4:Parameters and resolutions for the two-species NCSX radial electric
field scan.Figure 8:Two-species (hydrogen and electron) radial electric field scan for the
NCSX like equilibrium, comparingyanccand SFINCS.

## 6Conclusion

We have presentedyancc, a new solver for the drift kinetic equation designed
for GPU acceleration and automatic differentiability. The code solves both the
monoenergetic and full four-dimensional forms of the equation, using a mixed
pseudo-spectral/finite difference discretization with a multigrid preconditioned
Krylov solver. The numerical benchmarks demonstrate agreement with MONKES and
SFINCS to within 1% across a wide range of collisionalities, electric fields,
and magnetic geometries, for both single-species and multi-species plasmas, and
for both stellarator and tokamak configurations.

In terms of performance,yanccachieves roughly an order of magnitude speedup
over SFINCS on a per-scan basis while using an order of magnitude less memory,
with the gap widening at high collisionality where the SFINCS preconditioner
degrades. The runtime remains nearly flat across a wide range of collisionality,
unlike existing solvers whose iteration counts grow significantly at extremes of
collisionality. This robustness makesyanccpractical for production scans
covering the full parameter space of a given device.

The speed and differentiability ofyanccopen up several applications beyond
standalone neoclassical calculations. In stellarator optimization, neoclassical
transport coefficients must be evaluated many times as the magnetic geometry is
varied, and gradients of these coefficients with respect to geometry parameters
enable efficient gradient-based optimization over the full configuration space.
The low memory footprint and GPU acceleration support the high throughput needed
for uncertainty quantification through Monte Carlo sampling over input parameter
distributions. For integrated modeling and profile prediction,yanccis fast
enough to compute neoclassical coefficients on-the-fly within a transport
solver, replacing the precomputed fit functions or interpolated databases that
are commonly used today. The differentiability also enables adjoint-based
sensitivity analysis, where the derivative of a quantity of interest with
respect to all input parameters can be computed in a single solve.

Several directions for future development are planned. Self-consistent
computation of the ambipolar radial electric field will be added as a built-in
capability, extending beyond the current approach whereErE_{r}is specified as an
input. Adaptive mesh refinement in pitch angle and real space is being explored
to efficiently resolve the trapped-passing boundary layers, which can span
several orders of magnitude in width depending on collisionality, without
requiring uniformly fine grids across the full angular domain. Incorporating
corrections for strong radial electric fields and flows near quasisymmetry,
building on the work of[35], will extend the validity of
the code to regimes
where the conventionalρ∗\rho_{*}ordering assumptions begin to break down.
Together, these developments will makeyancca versatile tool for
neoclassical transport calculations across the full range of fusion-relevant
regimes, from conceptual design through discharge analysis.

## 6.1Data Availability

The source code and data supporting this work is available athttps://github.com/f0uriest/yancc

## 7Acknowledgements

This work was supported by Greg Hammett’s DOE Distinguished Scientist Fellow
award, and by a grant from the Simons Foundation (560651, ML). This research
used resources of the National Energy Research Scientific Computing Center
(NERSC), a Department of Energy User Facility using NERSC award FES-m4505 for
2025-2026. The authors thank Javier Escoto for help with the MONKES benchmark and
for many fruitful discussions about solving the drift kinetic equation, as well
as Greg Hammett for many discussions about subtleties of numerical methods.

## Appendix ARosenbluth potential implementation

The Rosenbluth potentials satisfy Poisson type equations:∇v2Hs=−4​π​f1,s\nabla^{2}_{v}H_{s}=-4\pi f_{1,s}(56)∇v2Gs=2​Hs\nabla^{2}_{v}G_{s}=2H_{s}(57)

We can expand these in Legendre polynomials inξ=−cos⁡α\xi=-\cos\alpha:Hs​(α,xs)=∑lPl​(−cos⁡α)​Hs,l​(xs)H_{s}(\alpha,x_{s})=\sum_{l}P_{l}(-\cos\alpha)H_{s,l}(x_{s})(58)Gs​(α,xs)=∑lPl​(−cos⁡α)​Gs,l​(xs)G_{s}(\alpha,x_{s})=\sum_{l}P_{l}(-\cos\alpha)G_{s,l}(x_{s})(59)

And similarly forf1,sf_{1,s}:f1,s​(α,xs)=∑lPl​(−cos⁡α)​f1,s,l​(xs)f_{1,s}(\alpha,x_{s})=\sum_{l}P_{l}(-\cos\alpha)f_{1,s,l}(x_{s})(60)

The Legendre harmonics of the potentials are then given by the Greens function:Hs,l​(xs)=4​π​vt​h,s22​l+1​[1xsl+1​I2,l​(xs)+xsl​I1,l​(xs)]H_{s,l}(x_{s})=\frac{4\pi v_{th,s}^{2}}{2l+1}\Bigg[\frac{1}{x_{s}^{l+1}}I_{2,l}(x_{s})+x_{s}^{l}I_{1,l}(x_{s})\Bigg](61)Gs,l​(xs)=−4​π​vt​h,s44​l2−1​[xsl​I3,l​(xs)−2​l−12​l+3​xsl+2​I1,l​(xs)−2​l−12​l+3​1xsl+1​I4,l​(xs)+1xsl−1​I2,l​(xs)]G_{s,l}(x_{s})=-\frac{4\pi v_{th,s}^{4}}{4l^{2}-1}\Bigg[{x_{s}^{l}}I_{3,l}(x_{s})-\frac{2l-1}{2l+3}x_{s}^{l+2}I_{1,l}(x_{s})-\frac{2l-1}{2l+3}\frac{1}{x_{s}^{l+1}}I_{4,l}(x_{s})+\frac{1}{x_{s}^{l-1}}I_{2,l}(x_{s})\Bigg](62)

withI1,l​(xs)\displaystyle I_{1,l}(x_{s})=∫xs∞z−l+1​f1,s,l​(z)​dz\displaystyle=\int_{x_{s}}^{\infty}z^{-l+1}f_{1,s,l}(z)\mathrm{d}z(63)I2,l​(xs)\displaystyle I_{2,l}(x_{s})=∫0xszl+2​f1,s,l​(z)​dz\displaystyle=\int_{0}^{x_{s}}z^{l+2}f_{1,s,l}(z)\mathrm{d}z(64)I3,l​(xs)\displaystyle I_{3,l}(x_{s})=∫xs∞z−l+3​f1,s,l​(z)​dz\displaystyle=\int_{x_{s}}^{\infty}z^{-l+3}f_{1,s,l}(z)\mathrm{d}z(65)I4,l​(xs)\displaystyle I_{4,l}(x_{s})=∫0xszl+4​f1,s,l​(z)​dz\displaystyle=\int_{0}^{x_{s}}z^{l+4}f_{1,s,l}(z)\mathrm{d}z(66)

We can then expressf1,s,lf_{1,s,l}using weighted Maxwell polynomialsLk​(xs)L_{k}(x_{s}):f1,s,l​(xs)=∑kf1,s,l,k​Lk​(xs)​exp⁡(−xs2)f_{1,s,l}(x_{s})=\sum_{k}f_{1,s,l,k}L_{k}(x_{s})\exp(-x_{s}^{2})(67)

and defineI1,l,k​(xs)\displaystyle I_{1,l,k}(x_{s})=∫xs∞z−l+1​Lk​(z)​exp⁡(−z2)​dz\displaystyle=\int_{x_{s}}^{\infty}z^{-l+1}L_{k}(z)\exp(-z^{2})\mathrm{d}z(68)I2,l,k​(xs)\displaystyle I_{2,l,k}(x_{s})=∫0xszl+2​Lk​(z)​exp⁡(−z2)​dz\displaystyle=\int_{0}^{x_{s}}z^{l+2}L_{k}(z)\exp(-z^{2})\mathrm{d}z(69)I3,l,k​(xs)\displaystyle I_{3,l,k}(x_{s})=∫xs∞z−l+3​Lk​(z)​exp⁡(−z2)​dz\displaystyle=\int_{x_{s}}^{\infty}z^{-l+3}L_{k}(z)\exp(-z^{2})\mathrm{d}z(70)I4,l,k​(xs)\displaystyle I_{4,l,k}(x_{s})=∫0xszl+4​Lk​(z)​exp⁡(−z2)​dz\displaystyle=\int_{0}^{x_{s}}z^{l+4}L_{k}(z)\exp(-z^{2})\mathrm{d}z(71)

so thatI1,l​(xs)\displaystyle I_{1,l}(x_{s})=∑kf1,s,l,k​I1,l,k​(xs)\displaystyle=\sum_{k}f_{1,s,l,k}I_{1,l,k}(x_{s})(72)I2,l​(xs)\displaystyle I_{2,l}(x_{s})=∑kf1,s,l,k​I2,l,k​(xs)\displaystyle=\sum_{k}f_{1,s,l,k}I_{2,l,k}(x_{s})(73)I3,l​(xs)\displaystyle I_{3,l}(x_{s})=∑kf1,s,l,k​I3,l,k​(xs)\displaystyle=\sum_{k}f_{1,s,l,k}I_{3,l,k}(x_{s})(74)I4,l​(xs)\displaystyle I_{4,l}(x_{s})=∑kf1,s,l,k​I4,l,k​(xs)\displaystyle=\sum_{k}f_{1,s,l,k}I_{4,l,k}(x_{s})(75)

We can then defineHs,l,k​(xs)=4​π2​l+1​[1xsl+1​I2,l,k​(xs)+xsl​I1,l,k​(xs)]H_{s,l,k}(x_{s})=\frac{4\pi}{2l+1}\Bigg[\frac{1}{x_{s}^{l+1}}I_{2,l,k}(x_{s})+x_{s}^{l}I_{1,l,k}(x_{s})\Bigg](76)Gs,l,k​(xs)=−4​π4​l2−1​[xsl​I3,l,k​(xs)−2​l−12​l+3​xsl+2​I1,l,k​(xs)−2​l−12​l+3​1xsl+1​I4,l,k​(xs)+1xsl−1​I2,l,k​(xs)]G_{s,l,k}(x_{s})=-\frac{4\pi}{4l^{2}-1}\Bigg[{x_{s}^{l}}I_{3,l,k}(x_{s})-\frac{2l-1}{2l+3}x_{s}^{l+2}I_{1,l,k}(x_{s})-\frac{2l-1}{2l+3}\frac{1}{x_{s}^{l+1}}I_{4,l,k}(x_{s})+\frac{1}{x_{s}^{l-1}}I_{2,l,k}(x_{s})\Bigg](77)

The integralsI1,l,kI_{1,l,k}etc can be cheaply computed as incomplete gamma
functions after a change of variables. TakingI1,l,kI_{1,l,k}as an example, we
first expressLkL_{k}in the standard monic polynomial form:Lk​(x)=∑k′kpk′​xk′L_{k}(x)=\sum_{k^{\prime}}^{k}p_{k^{\prime}}x^{k^{\prime}}(78)

thenI1,l,kI_{1,l,k}becomesI1,l,k​(xs)=∑k′kpk′​∫xs∞zk′−l+1​exp⁡(−z2)​dzI_{1,l,k}(x_{s})=\sum_{k^{\prime}}^{k}p_{k^{\prime}}\int_{x_{s}}^{\infty}z^{k^{\prime}-l+1}\exp(-z^{2})\mathrm{d}z(79)

Changing variables toy=z2y=z^{2}we obtainI1,l,k​(xs)\displaystyle I_{1,l,k}(x_{s})=12​∑k′kpk′​∫xs2∞y(k′−l)/2​exp⁡(−y)​dy\displaystyle=\frac{1}{2}\sum_{k^{\prime}}^{k}p_{k^{\prime}}\int_{x^{2}_{s}}^{\infty}y^{(k^{\prime}-l)/2}\exp(-y)\mathrm{d}y(80)=12​∑k′kpk′​Γ​(k′/2−l/2+1,xs2)\displaystyle=\frac{1}{2}\sum_{k^{\prime}}^{k}p_{k^{\prime}}\Gamma(k^{\prime}/2-l/2+1,x_{s}^{2})(81)

whereΓ​(s,x)\Gamma(s,x)is the upper incomplete gamma function. The other integrals
can be transformed similarly, withI2I_{2}andI4I_{4}giving lower incomplete gamma
functionsγ​(s,x)\gamma(s,x). To avoid numerical cancellation due to the large
magnitudes involved, we compute the gamma functions in logarithmic form and
evaluate the integral using a weighted log-sum-exp operation.

The distribution functionfsf_{s}is stored on a grid in(x,α)(x,\alpha)asfs,x,αf_{s,x,\alpha}, and the greens functionsHs,l,kH_{s,l,k}andGs,l,kG_{s,l,k}are
stored on the same speed grid, for each cross species interaction asHs,s′,x′,l,kH_{s,s^{\prime},x^{\prime},l,k}andGs,s′,x′,l,kG_{s,s^{\prime},x^{\prime},l,k}(wherex′=xs​vt​h,s/vt​h,s′x^{\prime}=x_{s}v_{th,s}/v_{th,s^{\prime}},
the potential for speciesssevaluated on the speed grid for speciess′s^{\prime}). The
Rosenbluth potentials can then be evaluated as simple tensor contractions:Hs,s′,x′,α′=∑l,k,x,αTl,α′−1​Hs,s′,x′,l,k​Vk,x​Tl,α​fs,x,αH_{s,s^{\prime},x^{\prime},\alpha^{\prime}}=\sum_{l,k,x,\alpha}T^{-1}_{l,\alpha^{\prime}}H_{s,s^{\prime},x^{\prime},l,k}V_{k,x}T_{l,\alpha}f_{s,x,\alpha}(82)Gs,s′,x′,α′=∑l,k,x,αTl,α′−1​Gs,s′,x′,l,k​Vk,x​Tl,α​fs,x,αG_{s,s^{\prime},x^{\prime},\alpha^{\prime}}=\sum_{l,k,x,\alpha}T^{-1}_{l,\alpha^{\prime}}G_{s,s^{\prime},x^{\prime},l,k}V_{k,x}T_{l,\alpha}f_{s,x,\alpha}(83)

whereTl,αT_{l,\alpha}is the change of basis matrix transforming between pitch
angleα\alphaand Legendre indexllandVk,xV_{k,x}is the change of basis
matrix between speedxxand Maxwell polynomial indexkk. Derivatives of the
potentials with respect to speed required for the collision operator are
obtained analytically and precomputed/applied in a similar fashion. The cost of
these tensor operations is quite low, as the resolution inxxis fairly coarse
(nx∼5n_{x}\sim 5–1010), and generally only a small number of Legendre modes are
required to represent the potentials (generallylm​a​x∼4l_{max}\sim 4–66).

## References
- [1]M. F. Adams and Y. Nishimura(2007-02)Parallel Algebraic Multigrid Methods in Gyrokinetic Turbulence Simulations.Communications in Computational Physics2(5),pp. 881–899.External Links:ISSN 1991-7120, 1815-2406,DocumentCited by:§1.
- [2]M. F. Adams, R. Samtaney, and A. Brandt(2010-09)Toward textbook multigrid efficiency for fully implicit resistive magnetohydrodynamics.Journal of Computational Physics229(18),pp. 6208–6219(en).External Links:ISSN 00219991,DocumentCited by:§1.
- [3]E. A. Belli and J. Candy(2009-07)An Eulerian method for the solution of the multi-species drift-kinetic equation.Plasma Physics and Controlled Fusion51(7),pp. 075018(en).External Links:ISSN 0741-3335, 1361-6587,DocumentCited by:§1.
- [4]E. A. Belli and J. Candy(2012-01)Full linearized Fokker–Planck collisions in neoclassical transport simulations.Plasma Physics and Controlled Fusion54(1),pp. 015015(en).External Links:ISSN 0741-3335, 1361-6587,DocumentCited by:§1.
- [5]E. A. Belli and J. Candy(2015-05)Neoclassical transport in toroidal plasmas with nonaxisymmetric flux surfaces.Plasma Physics and Controlled Fusion57(5),pp. 054012(en).External Links:ISSN 0741-3335, 1361-6587,DocumentCited by:§1.
- [6]E. A. Belli and J. Candy(2008)Kinetic calculation of neoclassical transport including self-consistent electron and impurity dynamics.Plasma Physics and Controlled Fusion50(9).External Links:ISSN 07413335,DocumentCited by:§1.
- [7]B. J. Braams(1986)Magnetohydrodynamic equilibrium calculations using multigrid.InMultigrid Methods II,W. Hackbusch and U. Trottenberg (Eds.),Vol.1228,pp. 38–51(en).Note:Series Title: Lecture Notes in MathematicsExternal Links:ISBN 978-3-540-17198-0 978-3-540-47372-5,DocumentCited by:§1.
- [8]JAX: composable machine learning for high-performance computingCited by:§1.
- [9]J. H. Bramble(1993)Multigrid methods.1 edition,Chapman and Hall/CRC(en).External Links:ISBN 978-0-203-74633-2,DocumentCited by:§1.
- [10]G. Chen and L. Chacón(2015-12)A multi-dimensional, energy- and charge-conserving, nonlinearly implicit, electromagnetic Vlasov–Darwin particle-in-cell algorithm.Computer Physics Communications197,pp. 73–87(en).External Links:ISSN 00104655,DocumentCited by:§1.
- [11]L. Claus, P. Ghysels, W. H. Boukaram, and X. S. Li(2025-01)A graphics processing unit accelerated sparse direct solver and preconditioner with block low rank compression.The International Journal of High Performance Computing
Applications39(1),pp. 18–31(en).External Links:ISSN 1094-3420, 1741-2846,DocumentCited by:§4.
- [12]E. De Sturler(1999)Truncation strategies for optimal krylov subspace methods.SIAM Journal on Numerical Analysis36(3),pp. 864–889.External Links:DocumentCited by:§4.5.
- [13]P.M. De Zeeuw(1990-12)Matrix-dependent prolongations and restrictions in a blackbox multigrid solver.Journal of Computational and Applied Mathematics33(1),pp. 1–27(en).External Links:ISSN 03770427,DocumentCited by:§1,§4.1.
- [14]J. W. Demmel, S. C. Eisenstat, J. R. Gilbert, X. S. Li, and J. W. H. Liu(1999-01)A Supernodal Approach to Sparse Partial Pivoting.SIAM Journal on Matrix Analysis and Applications20(3),pp. 720–755(en).External Links:ISSN 0895-4798, 1095-7162,DocumentCited by:§4.
- [15]H. C. Elman, D. J. Silvester, and A. J. Wathen(2014)Finite elements and fast iterative solvers: with applications in incompressible fluid dynamics.2nd ed edition,Numerical mathematics and scientific computation,Oxford university press,Oxford(en).External Links:ISBN 978-0-19-967879-2Cited by:§4.2.
- [16]F.J. Escoto, J.L. Velasco, I. Calvo, M. Landreman, and F.I. Parra(2024-07)MONKES: a fast neoclassical code for the evaluation of monoenergetic transport coefficients in stellarator plasmas.Nuclear Fusion64(7),pp. 076030.External Links:ISSN 0029-5515, 1741-4326,DocumentCited by:§1,§2,§5.1.
- [17]T. Gale, M. Zaharia, C. Young, and E. Elsen(2020-11)Sparse GPU Kernels for Deep Learning.InSC20: International Conference for High Performance
Computing, Networking, Storage and Analysis,Atlanta, GA, USA,pp. 1–14.External Links:ISBN 978-1-7281-9998-6,DocumentCited by:§4.
- [18]W. Hackbusch(1985)Multi-Grid Methods and Applications.Springer Series in Computational Mathematics, Vol.4,Springer Berlin Heidelberg,Berlin, Heidelberg.External Links:DocumentCited by:§4.2.
- [19]R. D. Hazeltine(1973-01)Recursive derivation of drift-kinetic equation.Plasma Physics15(1),pp. 77–80(en).External Links:ISSN 0032-1028,DocumentCited by:§2.
- [20]P. Helander and D. J. Sigmar(2005)Collisional transport in magnetized plasmas.Digitally printed 1st pbk. version edition,Cambridge University Press,Cambridge(eng).Note:OCLC: 61303062External Links:ISBN 978-0-521-02098-5Cited by:§2.
- [21]J. E. Hicken and D. W. Zingg(2010-01)A Simplified and Flexible Variant of GCROT for Solving Nonsymmetric Linear Systems.SIAM Journal on Scientific Computing32(3),pp. 1672–1694(en).External Links:ISSN 1064-8275, 1095-7197,DocumentCited by:§4.5.
- [22]F. L. Hinton and R. D. Hazeltine(1976-04)Theory of plasma transport in toroidal confinement systems.Reviews of Modern Physics48(2),pp. 239–308(en).External Links:ISSN 0034-6861,DocumentCited by:§2.
- [23]F. L. Hinton and M. N. Rosenbluth(1973-06)Transport properties of a toroidal plasma at low-to-intermediate collision frequencies.The Physics of Fluids16(6),pp. 836–854(en).External Links:ISSN 0031-9171,DocumentCited by:§2.2.
- [24]S. P. Hirshman, K. C. Shaing, W. I. van Rij, C. O. Beasley, and E. C. Crume(1986)Plasma transport coefficients for nonsymmetric toroidal confinement systems.Physics of Fluids29(9),pp. 2951–2959.External Links:ISSN 0031-9171,DocumentCited by:§1,§2.
- [25]D. D.-M. Ho and R. M. Kulsrud(1987-02)Neoclassical transport in stellarators.The Physics of Fluids30(2),pp. 442–461(en).External Links:ISSN 0031-9171,DocumentCited by:§2.2.
- [26]W. Kernbichler, S. V. Kasilov, G. Kapper, A. F. Martitsch, V. V. Nemov, C. Albert, and M. F. Heyn(2016-11)Solution of drift kinetic equation in stellarators and tokamaks with broken symmetry using the code NEO-2.Plasma Physics and Controlled Fusion58(10),pp. 104001(en).External Links:ISSN 0741-3335, 1361-6587,DocumentCited by:§1.
- [27]W. Kernbichler, S. V. Kasilov, G. O. Leitold, V. V. Nemov, and K. Allmaier(2008)Recent Progress in NEO-2 - A Code for Neoclassical Transport Computations Based on Field Line Tracing.Plasma and Fusion Research3(0),pp. S1061–S1061(en).External Links:ISSN 1880-6821,DocumentCited by:§1.
- [28]R. Kleiber, M. Borchardt, R. Hatzky, A. Könies, H. Leyh, A. Mishchenko, J. Riemann, C. Slaby, J.M. García-Regaña, E. Sánchez, and M. Cole(2024-02)EUTERPE: A global gyrokinetic code for stellarator geometry.Computer Physics Communications295,pp. 109013(en).External Links:ISSN 00104655,DocumentCited by:§1.
- [29]M. D. Kuczyńskiet al.(2024-04)Self-consistent, global, neoclassical radial-electric-field calculations of electron-ion-root transitions in the W7-X stellarator.Nuclear Fusion64(4),pp. 046023.External Links:DocumentCited by:§1.
- [30]M. Landreman, H. M. Smith, A. Mollén, and P. Helander(2014-04)Comparison of particle trajectories and collision operators for collisional transport in nonaxisymmetric plasmas.Physics of Plasmas21(4),pp. 042503(en).External Links:ISSN 1070-664X, 1089-7674,DocumentCited by:§1,§2.2,§2.2,§3,§5.2.
- [31]M. Landreman and D. R. Ernst(2013-06)New velocity-space discretization for continuum kinetic calculations and Fokker–Planck collisions.Journal of Computational Physics243,pp. 130–150(en).External Links:ISSN 00219991,DocumentCited by:§3.
- [32]B.P. Leonard(1979-06)A stable and accurate convective modelling procedure based on quadratic upstream interpolation.Computer Methods in Applied Mechanics and Engineering19(1),pp. 59–98(en).External Links:ISSN 00457825,DocumentCited by:§4.2.
- [33]A. Mollen, M. Landreman, H. M. Smith, S. Braun, and P. Helander(2015-11)Impurities in a non-axisymmetric plasma: transport and effect on bootstrap current.Physics of Plasmas22(11),pp. 112508(en).Note:arXiv:1504.04810 [physics]External Links:ISSN 1070-664X, 1089-7674,DocumentCited by:§3.
- [34]K. W. Morton(1996)Numerical Solution of Convection-Diffusion Problems.1 edition,CRC Press.External Links:DocumentCited by:§2.2.
- [35]R. D. C. Nies(2025)Turbulence and flows in toroidal fusion plasmas.Ph.D. Thesis,Princeton University, (en).Cited by:§6.
- [36]Y. Notay(2012-01)Aggregation-Based Algebraic Multigrid for Convection-Diffusion Equations.SIAM Journal on Scientific Computing34(4),pp. A2288–A2316(en).External Links:ISSN 1064-8275, 1095-7197,DocumentCited by:§1.
- [37]C.W. Oosterlee, F.J. Gaspar, T. Washio, and R. Wienands(1998-01)Multigrid Line Smoothers for Higher Order Upwind Discretizations of Convection-Dominated Problems.Journal of Computational Physics139(2),pp. 274–307(en).External Links:ISSN 00219991,DocumentCited by:§1,§4.2.
- [38]J. W. Ruge and K. Stüben(1987-01)Algebraic Multigrid.InMultigrid Methods,S. F. McCormick (Ed.),pp. 73–130(en).External Links:ISBN 978-1-61197-188-0 978-1-61197-105-7,DocumentCited by:§1.
- [39]Y. Saad and M. H. Schultz(1986-07)GMRES: A Generalized Minimal Residual Algorithm for Solving Nonsymmetric Linear Systems.SIAM Journal on Scientific and Statistical Computing7(3),pp. 856–869(en).External Links:ISSN 0196-5204, 2168-3417,DocumentCited by:§4.5.
- [40]Y. Saad(1993-03)A Flexible Inner-Outer Preconditioned GMRES Algorithm.SIAM Journal on Scientific Computing14(2),pp. 461–469(en).External Links:ISSN 1064-8275, 1095-7197,DocumentCited by:§4.5.
- [41]P. Sao, R. Vuduc, and X. S. Li(2014)A Distributed CPU-GPU Sparse Direct Solver.InEuro-Par 2014 Parallel Processing,F. Silva, I. Dutra, and V. Santos Costa (Eds.),Vol.8632,pp. 487–498(en).Note:Series Title: Lecture Notes in Computer ScienceExternal Links:ISBN 978-3-319-09872-2 978-3-319-09873-9,DocumentCited by:§4.
- [42]S. Satake, R. Kanno, and H. Sugama(2008)Development of a Non-Local Neoclassical Transport Code for Helical Configurations.Plasma and Fusion Research3,pp. S1062–S1062(en).External Links:ISSN 1880-6821,DocumentCited by:§1.
- [43]S. Satake, M. Okamoto, N. Nakajima, H. Sugama, and M. Yokoyama(2006)Non-Local Simulation of the Formation of Neoclassical Ambipolar Electric Field in Non-Axisymmetric Configurations.Plasma and Fusion Research1,pp. 002–002(en).External Links:ISSN 1880-6821,DocumentCited by:§1.
- [44]K. C. Shaing, E. C. Crume, J. S. Tolliver, S. P. Hirshman, and W. I. van Rij(1989-01)Bootstrap current and parallel viscosity in the low collisionality regime in toroidal plasmas.Physics of Fluids B: Plasma Physics1(1),pp. 148–152(en).External Links:ISSN 0899-8221,DocumentCited by:§1.
- [45]A. Stegmeir, C. Lalescu, M. Lin, J. Trilaksono, N. Varini, and T. Dannert(2026-06)A high-performance elliptic solver for plasma boundary turbulence codes.InProceedings of the Platform for Advanced Scientific
Computing Conference,Bern Switzerland,pp. 1–13(en).External Links:ISBN 979-8-4007-2734-4,DocumentCited by:§1.
- [46]K. Stüben(2001-03)A review of algebraic multigrid.Journal of Computational and Applied Mathematics128(1-2),pp. 281–309(en).External Links:ISSN 03770427,DocumentCited by:§1.
- [47]U. Trottenberg, C. W. Oosterlee, A. Schüller, A. Brandt, P. Oswald, and K. Stüben(2007)Multigrid.Transferred to digital print edition,Elsevier Academic Press,Amsterdam Heidelberg(en).External Links:ISBN 978-0-12-701070-0Cited by:§1,§3.
- [48]W. I. van Rij and S. P. Hirshman(1989-03)Variational bounds for transport coefficients in three‐dimensional toroidal plasmas.Physics of Fluids B: Plasma Physics1(3),pp. 563–569(en).External Links:ISSN 0899-8221,DocumentCited by:§1.
- [49]J.L. Velasco, I. Calvo, F.I. Parra, and J.M. García-Regaña(2020-10)KNOSOS: A fast orbit-averaging neoclassical code for stellarator geometry.Journal of Computational Physics418,pp. 109512(en).External Links:ISSN 00219991,DocumentCited by:§1,§2.1.
- [50]P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D. Cournapeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J. van der Walt, M. Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R.J. Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey, İ. Polat, Y. Feng, E. W. Moore, J. VanderPlas, D. Laxalde, J. Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C. R. Harris, A. M. Archibald, A. H. Ribeiro, F. Pedregosa, P. van Mulbregt, A. Vijaykumar, A. P. Bardelli, A. Rothberg, A. Hilboll, A. Kloeckner, A. Scopatz, A. Lee, A. Rokem, C. N. Woods, C. Fulton, C. Masson, C. Häggström, C. Fitzgerald, D. A. Nicholson, D. R. Hagen, D. V. Pasechnik, E. Olivetti, E. Martin, E. Wieser, F. Silva, F. Lenders, F. Wilhelm, G. Young, G. A. Price, G. L. Ingold, G. E. Allen, G. R. Lee, H. Audren, I. Probst, J. P. Dietrich, J. Silterra, J. T. Webber, J. Slavič, J. Nothman, J. Buchner, J. Kulick, J. L. Schönberger, J. V. de Miranda Cardoso, J. Reimer, J. Harrington, J. L. C. Rodríguez, J. Nunez-Iglesias, J. Kuczynski, K. Tritz, M. Thoma, M. Newville, M. Kümmerer, M. Bolingbroke, M. Tartre, M. Pak, N. J. Smith, N. Nowaczyk, N. Shebanov, O. Pavlyk, P. A. Brodtkorb, P. Lee, R. T. McGibbon, R. Feldbauer, S. Lewis, S. Tygier, S. Sievert, S. Vigna, S. Peterson, S. More, T. Pudlik, T. Oshima, T. J. Pingel, T. P. Robitaille, T. Spura, T. R. Jones, T. Cera, T. Leslie, T. Zito, T. Krauss, U. Upadhyay, Y. O. Halchenko, and Y. Vázquez-Baeza(2020)SciPy 1.0: fundamental algorithms for scientific computing in Python.Nature Methods17(3),pp. 261–272.Note:arXiv: 1907.10121External Links:ISSN 15487105,DocumentCited by:§4.
- [51]P. Wesseling(1995)An introduction to multigrid methods.Pure and applied mathematics,Wiley,Chichester(en).External Links:ISBN 978-0-471-93083-9Cited by:§1.
- [52]C. Wu and H. C. Elman(2006-01)Analysis and Comparison of Geometric and Algebraic Multigrid for Convection‐Diffusion Equations.SIAM Journal on Scientific Computing28(6),pp. 2208–2228(en).External Links:ISSN 1064-8275, 1095-7197,DocumentCited by:§1.

## 


- 


Major funding support from
