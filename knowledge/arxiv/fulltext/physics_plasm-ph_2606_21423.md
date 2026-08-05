# Geometric numerical discretization of a quasineutral hybrid model of drift-kinetic electrons and fully kinetic ions

**arXiv ID**: 2606.21423v1
**Authors**: Nishant Narechania, Guo Meng, Emil Poulsen, Eric Sonnendruecker
**Published**: 2026-06-19
**Categories**: physics.plasm-ph, math-ph
**HTML URL**: https://arxiv.org/html/2606.21423v1

## Abstract

We extend the geometric electromagnetic particle-in-cell (PIC) framework, GEMPICX, to solve the quasineutral hybrid Vlasov-Maxwell equations with drift-kinetic electrons and fully kinetic ions. A structure-preserving finite difference method that employs dual grids is used. The discrete action principle for the hybrid model is derived, using the dual nature of the grids. The dynamical system for this hybrid quasineutral model does not explicitly involve the temporal evolution term for the electric field. A curl-curl equation is therefore used to implicitly obtain the component of the electric field that is parallel to the background magnetic field, at every timestep. The perpendicular component of the electric field is obtained using the quasineutral Ampere's equation without the displacement current, combined with the definition of the current in the drift-kinetic model. The discretized versions of the electric field equations are large, sparse linear systems. A fully explicit time-stepping scheme as well as two implicit-explicit (IMEX) schemes are tested. The numerical model is validated by verifying the various waves obtained from the dispersion relation.

## Full Text

Geometric numerical discretization of a quasineutral hybrid model of drift-kinetic electrons and fully kinetic ions

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
- License: CC ZeroarXiv:2606.21423v1 [physics.plasm-ph] 19 Jun 2026

[orcid=0009-0007-1249-0843]\cortext[cor1]Corresponding author\cormark[1]

[orcid=0000-0002-0969-733X]
[orcid=0000-0003-3826-5226]
[orcid=0000-0002-8340-7230]

1]organization=Numerical Methods in Plasma Physics, Max Planck Institute for Plasma Physics,
addressline=Boltzmannstraße 2,
city=Garching,
citysep=,
postcode=85748,
state=Bavaria,
country=Germany

2]organization=School of Computation, Information and Technology, Technical University of Munich,
addressline=Boltzmannstraße 3,
city=Garching,
citysep=,
postcode=85748,
state=Bavaria,
country=Germany

## Geometric numerical discretization of a quasineutral hybrid model of drift-kinetic electrons and fully kinetic ionsNishant Narechanianishant.narechania@ipp.mpg.deGuo MengEmil PoulsenEric Sonnendrücker[[

## Abstract

We extend the geometric electromagnetic particle-in-cell (PIC) framework,GEMPICX, to solve the quasineutral hybrid Vlasov-Maxwell equations with drift-kinetic electrons and fully kinetic ions. A structure-preserving finite difference method that employs dual grids is used. The discrete action principle for the hybrid model is derived, using the dual nature of the grids. The dynamical system for this hybrid quasineutral model does not explicitly involve the temporal evolution term for the electric field. A curl-curl equation is therefore used to implicitly obtain the component of the electric field that is parallel to the background magnetic field, at every timestep. The perpendicular component of the electric field is obtained using the quasineutral Ampère’s equation without the displacement current, combined with the definition of the current in the drift-kinetic model. The discretized versions of the electric field equations are large, sparse linear systems. A fully explicit time-stepping scheme as well as two implicit-explicit (IMEX) schemes are tested. The numerical model is validated by verifying the various waves obtained from the dispersion relation.

## keywords:structure-preserving methods\sepquasineutral models\sephybrid PIC methods\sepdrift-kinetics

## 1Introduction

Hybrid kinetic models, that are a combination of fully kinetic and reduced models, are fundamental to modern computational plasma physics(lipatov2002hybrid). They present an effective balance between computational efficiency and physical accuracy in applications where kinetic effects are essential but a full kinetic treatment of all species is prohibitively expensive. In many plasma physics applications, the large mass disparity between ions and electrons leads to their dynamics occurring over significantly different spatial and temporal scales(hazeltine2003plasma). A widely adopted hybrid modelling approach therefore is to treat ions kinetically, while approximating electrons using reduced models. Quasineutral hybrid models are especially appealing in the context of computational efficiency. In applications with physical dimensions greatly exceeding the Debye length, the quasineutrality approximation is generally valid. By neglecting the displacement current in the Ampère equation, quasineutral models filter out the small length scales associated with charge separation phenomena, and also eliminate high-frequency electromagnetic wave propagation from the full Vlasov-Maxwell system. They therefore significantly relax the stringent time-step restrictions tied to the full Vlasov-Maxwell system, while still maintaining key kinetic effects. In the reduced drift-kinetic electron model, the electron gyromotion is modelled as a limiting case of gyrokinetic theory in the small Larmor radius limit(burby2019gauge-free). This removes the description of phenomena occurring at electron gyromotion time and length scales. Therefore, in hybrid drift-kinetic quasineutral models, with kinetic ions and drift-kinetic electrons, the time-step restriction is relaxed even further by the use of reduced models for electron motion coupled with quasineutrality.

Hybrid plasma models span a broad class of approaches that combine kinetic and reduced descriptions for different species. On one hand, hybrid Vlasov models treat ions kinetically via a phase-space distribution while modelling electrons as a fluid, providing a noise-free but computationally expensive alternative to particle methods(valentini2007753). On the other hand, the more widely used hybrid particle-in-cell (PIC) models represent ions with particles and electrons as a fluid, as established in earlier works(winske1985hybrid;matthews1994current;lipatov2002hybrid). These ion-kinetic/electron-fluid models remain the standard in many applications and have seen continued development in recent years, including large-scale and application-oriented codes such asAHKASH(chirakkara), as well as improved hybrid PIC formulations(jiao2025;wu2024;joshi2023fluid), often employing simplified closures such as adiabatic electrons, where the electron response is assumed to follow a prescribed equation of state rather than being evolved dynamically.

Beyond fluid closures, there is a growing class of hybrid models with kinetic ions and reduced kinetic descriptions for electrons, such as gyrokinetic or drift-kinetic descriptions, providing a balance between fluid and kinetic descriptions of electrons. Such models, which are also the focus of this work, are rooted in the theoretical framework ofbrizard2007foundations, and are particularly well suited to strongly magnetized plasmas. In addition, hybrid formulations based directly on the electric and magnetic fields, avoiding the use of electromagnetic potentials, have been developed in recent years(chen2009particle;chen2019new). Such models have been explored in a variety of contexts. For example,tyushev2025performed drift-kinetic PIC simulations of magnetic mirror configurations and transport problems.glinskiy2024developed semi-implicit drift-kinetic PIC schemes for plasma confinement and heating processes.seo2021developed a hybrid drift-kinetic PIC model for studying plasma turbulence in a cylindrical tokamak geometry. These developments provide the conceptual and numerical foundation for the present work, which combines kinetic ions with drift-kinetic electrons in a structure-preserving quasineutral PIC framework.

Despite their advantages, the numerical solution of hybrid quasineutral models presents substantial challenges and remains an active field of research(hockney2021computer;birdsall2018plasma). Conventional PIC methods usually suffer from long-term numerical instabilities, violation of conservation laws, and unphysical energy growth. These issues are caused due to the lack of compatibility between discrete field solvers and particle updates, and to the breakdown of geometric properties of the continuous system at the discrete level. Structure-preserving methods that preserve certain geometric structures of the physical system of governing equations, such as conservation laws, gauge symmetry, and the Gauss laws, have emerged as a reliable approach to address these difficulties. For example, various researchers have developed discrete energy-conserving semi-implicit(chen2011energy;chen2015multi)and fully implicit(markidis2011energy;lapenta2017exactly)PIC schemes. A subset of structure-preserving methods are methods that exactly preserve discretized equivalents of invariants by discretizing the action principle or Hamiltonian structure of the governing equations. Recently, significant progress has been made in the development of structure-preserving PIC schemes, including variational integrators(squire2012geometric;marsden2001discrete), finite element exterior calculus (FEEC) approaches(arnold2018finite), and compatible discretizations based on the de Rham complex(bossavit1998computational;hiptmair2002finite;tronci2014hybrid).

Methods based on the de Rham complex ensure an exact preservation of the Gauss laws after discretization. One such method, namely the finite element geometric electromagnetic PIC (GEMPIC) method, was developed based on the Vlasov-Maxwell system’s intrinsic Hamiltonian structure(kraus2017gempic;campos2022variational;kormann2024). This method conserved discretized versions of the Gauss laws, total energy, the Poisson structure and Casimir invariants. This method was then also extended to a discretization based on structure-preserving mimetic finite differences, now known asGEMPICX(kormann2024). Mimetic discretization methods use operators designed to preserve key identities from vector calculus within a discrete framework(bochev2006principles). In this setting, unknown quantities are expressed as values associated with points, as well as integrals over edges, faces, and volumes, forming a discrete analogue of the de Rham complex. More recently,meng2025extended this framework to the drift-kinetic (DK) model and to hybrid models that combine drift-kinetic electrons with fully kinetic ions. Similarly,narechania2026FKQNextended it to the quasineutral Vlasov-Maxwell model with fully kinetic descriptions of both species.

In this work, we extendGEMPICXto solve the quasineutral hybrid drift-kinetic model with drift-kinetic electrons and kinetic ions, using a structure-preserving discretization.
This model eliminates fast light waves, thereby enabling efficient and realistic studies of Alfvén wave and ion cyclotron dynamics; the model formulation and its physical applications are described in a companion paper(meng2026QN-DeFi).
We start with the Lagrangian fromburby2019gauge-freeand propose a discretized Lagrangian based on mimetic finite differences using dual grids. Discretized field equations and equations of motion for particles are obtained from the discretized Lagrangian using the variational principle, ensuring consistency with the de Rham geometric structure of the continuous equations. Particle-field coupling is achieved using spline-based interpolation consistent with this discretization. A key aspect of the proposed formulation is the decomposition of the electric field into components parallel and perpendicular to the background magnetic field. The removal of the displacement current eliminates the standard evolution equation for the electric field, requiring alternative formulations to determine it consistently. The perpendicular component is obtained from a modified quasineutral Ampère equation, while the parallel component is determined from a curl-curl equation derived from Faraday’s law and current evolution. These formulations lead to large, sparse linear systems, whose efficient treatment is essential for practical simulations. We therefore investigate both fully explicit and implicit-explicit (IMEX) time integration schemes, and analyze their stability properties using a cold plasma model. We validate the numerical model by examining the wave spectra of quasineutral plasmas, in a quasi-1D setting under periodic boundary conditions. Additionally, an ion cyclotron wave simulation with periodic boundaries is performed to demonstrate the capability of the numerical method to model a higher order process such as damping.

The organization of this paper is as follows: Section2describes the quasineutral hybrid model with drift-kinetic electrons and fully kinetic ions, including the action principle, governing equations, and the electric field equations. Section3describes the structure-preserving dual-mesh approach used for discretization of fields. Section4describes the coupling between particles and discretized field variables. Section5describes the semi-discrete equivalents of the action principle, governing equations, and electric field equations. Section6derives the time-step criterion for stability of the numerical time-stepping algorithm, using a cold plasma model. Section7details the time-stepping schemes used for solving the semi-discrete system of equations. The dispersion relation and the various eigenmodes generated are discussed in Section8. Section9describes numerical simulations with periodic boundary conditions performed to validate this numerical model. The parallelization strategy is described in Section10. We finally summarize this work, draw conclusions and discuss future directions in Section11.

## 2The quasineutral hybrid model with drift-kinetic electrons and fully kinetic ions

In this section, we describe the Lagrangian for the hybrid drift-kinetic quasineutral model, comprising terms associated with the electron kinetic energy, the ion kinetic energy and the magnetic field energy. We then obtain the governing equations from this action. Finally, the electric field equations are obtained from the governing equations.

## 2.1Action principle

We first describe the Lagrangian and action principle for the electrons in our hybrid model, that are described using the drift-kinetic model. The drift-kinetic model is obtained from the gyrokinetic model described byburby2019gauge-free, by taking the zero Larmor radius limit. Let𝑩e​q\bm{B}_{eq}be the time-invariant, equilibrium background magnetic field acting on the plasma and𝒃e​q=𝑩e​q/|𝑩e​q|\bm{b}_{eq}=\bm{B}_{eq}/|\bm{B}_{eq}|its associated unit vector.𝑬\bm{E}and𝑩\bm{B}denote the perturbed electric and magnetic fields, respectively. Their components perpendicular to𝑩e​q\bm{B}_{eq}are therefore given by the vectors𝑩=⟂(Id−𝒃e​q𝒃e​qT)𝑩\bm{B}\mathbf{{}_{\perp}}=(Id-\bm{b}_{eq}{\bm{b}_{eq}}^{T})\bm{B}and𝑬=⟂(Id−𝒃e​q𝒃e​qT)𝑬\bm{E}\mathbf{{}_{\perp}}=(Id-\bm{b}_{eq}{\bm{b}_{eq}}^{T})\bm{E}, respectively. The associated vector potentials of these magnetic fields are𝑨e​q\bm{A}_{eq}and𝑨\bm{A}, so that𝑩e​q=∇×𝑨e​q\bm{B}_{eq}=\nabla\times\bm{A}_{eq}and𝑩=∇×𝑨\bm{B}=\nabla\times\bm{A}. We also denote the total magnetic field as𝑩t​o​t=𝑩e​q+𝑩\bm{B}_{tot}=\bm{B}_{eq}+\bm{B}. The electrostatic potential is given byϕ\phiand the charge of the particle species byqeq_{e}, which is the electron charge in the present context. The particle kinetic energy for the drift-kinetic electrons is denoted byK=K0+K1+K2K=K_{0}+K_{1}+K_{2}. Here,K0K_{0}is the component independent of𝑬\bm{E}and𝑩\bm{B},K1K_{1}depends linearly on𝑬\bm{E}and𝑩\bm{B}, andK2K_{2}depends quadratically on𝑬\bm{E}and𝑩\bm{B}. These are given by:K0\displaystyle K_{0}=12​me​v∥2+μ​|𝑩e​q|,\displaystyle=\frac{1}{2}m_{e}v_{\parallel}^{2}+\mu|\bm{B}_{eq}|,(1)K1\displaystyle K_{1}=μ​𝒃e​q⋅𝑩,\displaystyle=\mu\bm{b}_{eq}\cdot\bm{B},(2)K2\displaystyle K_{2}=(μ​|𝑩e​q|−me​v∥2)​|𝑩|2⟂2​|𝑩e​q|2−me|𝑬|2⟂2​|𝑩e​q|2−me​v∥​𝑬×𝒃e​q⋅𝑩𝑩e​q2.\displaystyle=\left(\mu|\bm{B}_{eq}|-m_{e}v_{\parallel}^{2}\right)\frac{|\bm{B}\mathbf{{}_{\perp}}|^{2}}{2|\bm{B}_{eq}|^{2}}-\frac{m_{e}|\bm{E}\mathbf{{}_{\perp}}|^{2}}{2|\bm{B}_{eq}|^{2}}-\frac{m_{e}v_{\parallel}\bm{E}\times\bm{b}_{eq}\cdot\bm{B}}{\bm{B}_{eq}^{2}}.(3)

Here,mem_{e}is the particle mass of the electron species,𝒗e,g​c\bm{v}_{e,gc}is the particle guiding center velocity andv∥=𝒗e,g​c⋅𝑩e​qv_{\parallel}=\bm{v}_{e,gc}\cdot\bm{B}_{eq}is its component that is parallel to the equilibrium magnetic field.μ\muis the magnetic moment of the particle. We also introduce the effective magnetic field𝑩∗\bm{B}^{\ast}and its associated vector potential𝑨∗\bm{A}^{\ast}. These are given by:𝑨∗\displaystyle\bm{A}^{\ast}=𝑨+𝑨e​q+meqe​v∥​𝒃e​q,\displaystyle=\bm{A}+\bm{A}_{eq}+\frac{m_{e}}{q_{e}}v_{\parallel}\bm{b}_{eq},(4)𝑩∗\displaystyle\bm{B}^{\ast}=∇×𝑨=𝑩+𝑩e​q+meqe​v∥​∇×𝒃e​q.\displaystyle=\nabla\times\bm{A}=\bm{B}+\bm{B}_{eq}+\frac{m_{e}}{q_{e}}v_{\parallel}\nabla\times\bm{b}_{eq}.(5)

Here, themeqe​v∥​∇×𝒃e​q\frac{m_{e}}{q_{e}}v_{\parallel}\nabla\times\bm{b}_{eq}term is the field-line geometry correction, that arises from the removal of electron gyromotion in this model. Finally, the Lagrangian for the drift-kinetic model has been described bymeng2025. For the quasineutral model considered here, the electric field energy term must be removed and hence the Lagrangian for the drift-kinetic model in this case is given by:Le​(𝑨​(t),ϕ​(t),𝑿e,g​c​(t),𝑿˙e,g​c​(t),V∥​(t),μ;fe,g​c,0)=∫qe​(𝑨∗​(t,𝑿e,g​c​(t),V∥​(t),𝑨​(t,𝑿e,g​c​(t)))⋅𝑿˙e,g​c​(t)−ϕ​(t,𝑿e,g​c​(t)))​fe,g​c,0​B∥∗​0d​𝒙0​d​v∥​0d​μ−∫K0​(𝑿e,g​c​(t),V∥​(t),μ)​fe,g​c,0​B∥∗​0d​𝒙0​d​v∥​0d​μ−∫(K1+K2)​(𝑿e,g​c​(t),V∥​(t),𝑬​(t,𝑿e,g​c​(t)),𝑩​(t,𝑿e,g​c​(t)),μ)​fe,g​c,0​B∥∗​0d​𝒙0​d​v∥​0d​μ.L_{e}(\bm{A}(t),\phi(t),\bm{X}_{e,gc}(t),\dot{\bm{X}}_{e,gc}(t),V_{\parallel}(t),\mu;f_{e,gc,0})\\
=\int q_{e}\left(\bm{A}^{\ast}(t,\bm{X}_{e,gc}(t),V_{\parallel}(t),\bm{A}(t,\bm{X}_{e,gc}(t)))\cdot\dot{\bm{X}}_{e,gc}(t)-\phi(t,\bm{X}_{e,gc}(t))\right)f_{e,gc,0}B^{\ast}_{\parallel}{{}_{0}}\mathop{}\!\mathrm{d}\bm{x}_{0}\mathop{}\!\mathrm{d}v_{\parallel}{{}_{0}}\mathop{}\!\mathrm{d}\mu\\
-\int K_{0}(\bm{X}_{e,gc}(t),V_{\parallel}(t),\mu)f_{e,gc,0}B^{\ast}_{\parallel}{{}_{0}}\mathop{}\!\mathrm{d}\bm{x}_{0}\mathop{}\!\mathrm{d}v_{\parallel}{{}_{0}}\mathop{}\!\mathrm{d}\mu\\
-\int(K_{1}+K_{2})(\bm{X}_{e,gc}(t),V_{\parallel}(t),\bm{E}(t,\bm{X}_{e,gc}(t)),\bm{B}(t,\bm{X}_{e,gc}(t)),\mu)f_{e,gc,0}B^{\ast}_{\parallel}{{}_{0}}\mathop{}\!\mathrm{d}\bm{x}_{0}\mathop{}\!\mathrm{d}v_{\parallel}{{}_{0}}\mathop{}\!\mathrm{d}\mu.(6)

Here,fe,g​cf_{e,gc}is the guiding center phase-space distribution function expressed using the guiding center volume elementB∥∗​qe​d​𝒙​d​v∥​d​μB^{\ast}_{\parallel}q_{e}\mathop{}\!\mathrm{d}\bm{x}dv_{\parallel}\mathop{}\!\mathrm{d}\mu.B∥∗=𝑩∗⋅𝒃e​qB^{\ast}_{\parallel}=\bm{B}^{\ast}\cdot\bm{b}_{eq}is the component of𝑩∗\bm{B}^{\ast}that is parallel to𝑩e​q\bm{B}_{eq}. For the ions, we must use the Lagrangian for the quasineutral fully kinetic model, developed byTronci2015Neutral-Vlasov-. This is given by:Li​(𝑨​(t),ϕ​(t),𝑿i​(t),𝑿i˙​(t),𝑽i​(t);fi,0)=∫((mi​𝑽i​(t)+qi​𝑨​(t,𝑿i​(t)))⋅𝑿i˙​(t)−12​mi​Vi2−qi​ϕ​(t,𝑿i​(t)))​fi,0​d​𝒙0​d​𝒗0,L_{i}(\bm{A}(t),\phi(t),\bm{X}_{i}(t),\dot{\bm{X}_{i}}(t),\bm{V}_{i}(t);f_{i,0})=\\
\int\left((m_{i}\bm{V}_{i}(t)+q_{i}\bm{A}(t,\bm{X}_{i}(t)))\cdot\dot{\bm{X}_{i}}(t)-\frac{1}{2}m_{i}V_{i}^{2}-q_{i}\phi(t,\bm{X}_{i}(t))\right)f_{i,0}\mathop{}\!\mathrm{d}\bm{x}_{0}\mathop{}\!\mathrm{d}\bm{v}_{0},(7)

Here,mim_{i}andqiq_{i}are the ion particle mass and charge, respectively, whilefif_{i}is the phase-space distribution function for the ions. The Lagrangian accounting for the magnetic field energy is given by:Lf​(𝑨​(t))=−∫(12​μ0​|∇×𝑨e​q​(𝒙)+∇×𝑨​(t,𝒙)|2)​d​𝒙.L_{f}(\bm{A}(t))=-\int\left(\frac{1}{2\mu_{0}}\left|\nabla\times\bm{A}_{eq}(\bm{x})+\nabla\times\bm{A}(t,\bm{x})\right|^{2}\right)\mathop{}\!\mathrm{d}\bm{x}.(8)

In the above equations,𝑩e​q=∇×𝑨e​q\bm{B}_{eq}=\nabla\times\bm{A}_{eq}and𝑩=∇×𝑨\bm{B}=\nabla\times\bm{A}. Also, the electric field can be written in terms of the potentials as𝑬=−∂𝑨∂t−∇ϕ\bm{E}=-\frac{\partial\bm{A}}{\partial t}-\nabla\phi. The total Lagrangian for the complete hybrid model is therefore given by:L=Le+Li+Lf.L=L_{e}+L_{i}+L_{f}.(9)

## 2.2Governing equations

We obtain the physical system of governing equations from the above action. Note that these equations can also be obtained from the non-quasineutral hybrid drift-kinetic model presented in the work bymeng2025, by simply taking the formal limitϵ0→0\epsilon_{0}\to 0, whereϵ0\epsilon_{0}is the permittivity of vacuum. Taking variations with respect to𝑿\bm{X}and𝑽\bm{V}yields the Euler-Lagrange equations for the particles,∂∂t​∂L∂𝑿˙=∂L∂𝑿\frac{\partial}{\partial t}\frac{\partial L}{\partial\dot{\bm{X}}}=\frac{\partial L}{\partial\bm{X}}and∂L∂𝑽=𝟎\frac{\partial L}{\partial\bm{V}}=\bf 0. Taking variations with respect to the electron guiding-center positions and velocities,𝑿e,g​c\bm{X}_{e,gc}and𝒗e,g​c\bm{v}_{e,gc}, gives the following equations of motion for the drift-kinetic electrons:d​𝑿e,g​cd​t=𝑽e,g​c\displaystyle\frac{\mathrm{d}\bm{X}_{e,gc}}{\mathrm{d}t}=\bm{V}_{e,gc}=V∥​𝑩∗B∥∗+1B∥∗​(𝑬×𝒃e​q−μqe​∇B∥,tot×𝒃e​q),\displaystyle=V_{\parallel}\frac{\bm{B}^{\ast}}{B_{\parallel}^{\ast}}+\frac{1}{B_{\parallel}^{\ast}}\left(\bm{E}\times\bm{b}_{eq}-\frac{\mu}{q_{e}}\nabla B_{\parallel,tot}\times\bm{b}_{eq}\right),(10)d​V∥d​t\displaystyle\frac{\mathrm{d}V_{\parallel}}{\mathrm{d}t}=qeme​𝑩∗B∥∗⋅(𝑬−μqe​∇B∥,tot)=ae,g​c,\displaystyle=\frac{q_{e}}{m_{e}}\frac{\bm{B}^{\ast}}{B_{\parallel}^{\ast}}\cdot\left(\bm{E}-\frac{\mu}{q_{e}}\nabla B_{\parallel,tot}\right)=a_{e,gc},(11)

whereB∥,tot=𝑩∗⋅𝒃e​qB_{\parallel,tot}=\bm{B}^{\ast}\cdot\bm{b}_{eq}and𝑽e,g​c\bm{V}_{e,gc}andae,g​ca_{e,gc}are the guiding center velocity and acceleration, respectively. Equations (10) and (11) are the characteristic equations of the drift-kinetic Vlasov equation for the electron guiding centers, given by:∂fe,g​c∂t+𝑽e,g​c⋅∇xfe,g​c+ae,g​c​∂fe,g​c∂v∥=0.\frac{\partial f_{e,gc}}{\partial t}+\bm{V}_{e,gc}\cdot\nabla_{x}f_{e,gc}+a_{e,gc}\frac{\partial f_{e,gc}}{\partial v_{\parallel}}=0.(12)

Similarly, taking variations with respect to the ion particle positions and velocities,𝑿i\bm{X}_{i}and𝑽i\bm{V}_{i}, gives the following equations of motion for the ions:d​𝑿id​t\displaystyle\frac{\mathrm{d}\bm{X}_{i}}{\mathrm{d}t}=𝑽i,\displaystyle=\bm{V}_{i},(13)d​𝑽id​t\displaystyle\frac{\mathrm{d}\bm{V}_{i}}{\mathrm{d}t}=qimi​(𝑬+𝑽i×𝑩t​o​t)=ai,\displaystyle=\frac{q_{i}}{m_{i}}\left(\bm{E}+\bm{V}_{i}\times\bm{B}_{tot}\right)=a_{i},(14)

whereaia_{i}is the ion acceleration. The solutions of equations (13) and (14) are the characteristic equations of the fully kinetic Vlasov equation for the ions, given by:∂fi∂t+𝑽i⋅∇xfi+ai⋅∂fi∂𝒗i=0.\frac{\partial f_{i}}{\partial t}+\bm{V}_{i}\cdot\nabla_{x}f_{i}+a_{i}\cdot\frac{\partial f_{i}}{\partial\bm{v}_{i}}=0.(15)

Here,fe,g​cf_{e,gc}andfif_{i}are the velocity-space distribution functions for the electron guiding centers and ions, respectively. The variations in𝑨\bm{A}yield the quasineutral Ampère equation:∇×𝑩t​o​t=μ0​𝑱=μ0​(𝑱i+𝑱e,g​c),\nabla\times\bm{B}_{tot}=\mu_{0}\bm{J}=\mu_{0}(\bm{J}_{i}+\bm{J}_{e,gc}),(16)

where𝑱\bm{J}is the total current density, and𝑱e,g​c\bm{J}_{e,gc}and𝑱i\bm{J}_{i}are the electron and ion current densities, respectively, given by:𝑱e,g​c\displaystyle\bm{J}_{e,gc}=qe​∫fe,g​c​𝒗e,g​c​B∥∗​d​v∥​d​μ,\displaystyle=q_{e}\int f_{e,gc}\bm{v}_{e,gc}B^{\ast}_{\parallel}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu,(17)𝑱i\displaystyle\bm{J}_{i}=qi​∫fi​𝒗​d​𝒗.\displaystyle=q_{i}\int f_{i}\bm{v}\mathop{}\!\mathrm{d}\bm{v}.(18)

The variations inϕ\phiyield the quasineutrality condition:ρ=ρi+ρe,g​c=0,\rho=\rho_{i}+\rho_{e,gc}=0,(19)

whereρ\rhois the total charge density, andρe,g​c\rho_{e,gc}andρi\rho_{i}are the electron and ion charge densities, respectively, given by:ρe,g​c\displaystyle\rho_{e,gc}=qe​∫fe,g​c​B∥∗​d​v∥​d​μ,\displaystyle=q_{e}\int f_{e,gc}B^{\ast}_{\parallel}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu,(20)ρi\displaystyle\rho_{i}=qi​∫fi​d​𝒗.\displaystyle=q_{i}\int f_{i}\mathop{}\!\mathrm{d}\bm{v}.(21)

Equation (19) above
also implies the quasineutral continuity equation∇⋅(𝑱i+𝑱e,g​c)=0\nabla\cdot(\bm{J}_{i}+\bm{J}_{e,gc})=0which can also be obtained by taking the dot product of equation (16). Moreover, the Faraday’s equation follows directly from the definition of the fields from the potentials and is given by:∂𝑩∂t+∇×𝑬=𝟎,\frac{\partial\bm{B}}{\partial t}+\nabla\times\bm{E}={\bf 0},(22)

since the temporal derivative of𝑩e​q\bm{B}_{eq}is zero. Similarly, the Gauss law for magnetism follows from the definition of the magnetic field and is given by:∇⋅𝑩=0.\nabla\cdot\bm{B}=0.(23)

Taking variations of the Lagrangian typically also generates extra polarization and magnetization terms. However, in the present work, these terms have been assumed to be negligible and are therefore not accounted for. For a more complete derivation and detailed treatment of these terms, the reader is referred to the work bymeng2025. In the present work, we also assume𝑩e​q\bm{B}_{eq}to be uniform. Therefore, in this case,∇×𝑩e​q\nabla\times\bm{B}_{eq}in equation (16) and∇⋅𝑩e​q\nabla\cdot\bm{B}_{eq}in equation (23) both simplify to zero.

## 2.3The electric field equations

Without the displacement current and electron polarization current terms in the Ampère’s equation, the electric field cannot be evolved using its time derivative. Other equations are therefore required to obtain the electric field at any time instant. We first write the electric field as a sum of its components perpendicular and parallel to𝑩e​q\bm{B}_{eq}i.e.𝑬=𝑬⟂+𝑬∥\bm{E}=\bm{E}_{\perp}+\bm{E}_{\parallel}. Also𝑬∥\bm{E}_{\parallel}can be written as𝑬∥=E∥​𝒃e​q\bm{E}_{\parallel}=E_{\parallel}\bm{b}_{eq}, whereE∥E_{\parallel}is the scalar value of𝑬∥\bm{E}_{\parallel}.

## 2.3.1Equation for𝑬⟂\bm{E}\mathbf{{}_{\perp}}

The𝑬⟂\bm{E}\mathbf{{}_{\perp}}equation can be directly obtained from the Ampère equation, i.e. equation (16). Using the𝒗e,g​c\bm{v}_{e,gc}definition from equation (10), and the fact that𝑬×𝒃e​q=𝑬×⟂𝒃e​q\bm{E}\times\bm{b}_{eq}=\bm{E}\mathbf{{}_{\perp}}\times\bm{b}_{eq}, the drift-kinetic electron current density defined in equation (17) can be rewritten as:𝑱e,g​c=qe∫v∥𝑩∗fe,g​cdv∥dμ+∫(qe𝑬−⟂μ∇B∥,tot)×𝒃e​qfe,g​cdv∥dμ.\bm{J}_{e,gc}=q_{e}\int v_{\parallel}{\bm{B}^{\ast}}f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu+\int\left(q_{e}\bm{E}\mathbf{{}_{\perp}}-\mu\nabla B_{\parallel,tot}\right)\times\bm{b}_{eq}f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu.(24)

We now take the cross product of𝒃e​q\bm{b}_{eq}with equation (24). Using the relations𝒃e​q×(𝑬×⟂𝒃e​q)=𝑬⟂\bm{b}_{eq}\times(\bm{E}\mathbf{{}_{\perp}}\times\bm{b}_{eq})=\bm{E}\mathbf{{}_{\perp}}and𝒃e​q×(∇B∥,tot×𝒃e​q)=∇⟂B∥,tot\bm{b}_{eq}\times(\nabla B_{\parallel,tot}\times\bm{b}_{eq})=\nabla_{\perp}B_{\parallel,tot}, we get:∫qe​𝑬​fe,g​c⟂​d​v∥​d​μ=𝒃e​q×𝑱e,g​c−qe​∫(v∥​𝒃e​q×𝑩∗−μqe​∇⟂B∥,tot)​fe,g​c​d​v∥​d​μ.\int q_{e}\bm{E}\mathbf{{}_{\perp}}f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu=\bm{b}_{eq}\times\bm{J}_{e,gc}-q_{e}\int\left(v_{\parallel}{\bm{b}_{eq}\times\bm{B}^{\ast}}-\frac{\mu}{q_{e}}\nabla_{\perp}B_{\parallel,tot}\right)f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu.(25)

Finally, using equation (16) to substitute for𝑱e,g​c\bm{J}_{e,gc}, we get the final equation to solve for𝑬⟂\bm{E}\mathbf{{}_{\perp}}:μ0​∫qe​𝑬​fe,g​c⟂​d​v∥​d​μ=𝒃e​q×(∇×𝑩−μ0​𝑱i)−μ0​qe​∫(v∥​𝒃e​q×𝑩∗−μqe​∇⟂B∥,tot)​fe,g​c​d​v∥​d​μ.\mu_{0}\int q_{e}\bm{E}\mathbf{{}_{\perp}}f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu=\bm{b}_{eq}\times(\nabla\times\bm{B}-\mu_{0}\bm{J}_{i})-\mu_{0}q_{e}\int\left(v_{\parallel}{\bm{b}_{eq}\times\bm{B}^{\ast}}-\frac{\mu}{q_{e}}\nabla_{\perp}B_{\parallel,tot}\right)f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu.(26)

Obtaining𝑬⟂\bm{E}\mathbf{{}_{\perp}}by solving equation (26) ensures the satisfaction of Ampère’s law given in equation (16) and hence the divergence-free nature of the current density.

## 2.3.2Equation forE∥E\mathbf{{}_{\parallel}}

Taking the curl of the Faraday’s equation, i.e. (22) and the time derivative of the Ampère equation, i.e. equation (16), and combining the two equations, we obtain:∇×∇×𝑬=−μ0​(∂𝑱i∂t+∂𝑱e,g​c∂t).\nabla\times\nabla\times\bm{E}=-\mu_{0}\left(\frac{\partial\bm{J}_{i}}{\partial t}+\frac{\partial\bm{J}_{e,gc}}{\partial t}\right).(27)

Taking the dot product of equation (27) with𝒃e​q\bm{b}_{eq}, we get:𝒃e​q⋅(∇×∇×𝑬)=∇∥(∇⟂⋅𝑬⟂)−∇⟂2E∥=−μ0​𝒃e​q⋅(∂𝑱i∂t+∂𝑱e,g​c∂t).\bm{b}_{eq}\cdot(\nabla\times\nabla\times\bm{E})=\nabla_{\parallel}(\nabla_{\perp}\cdot\bm{E}_{\perp})-\nabla_{\perp}^{2}E_{\parallel}=-\mu_{0}\bm{b}_{eq}\cdot\left(\frac{\partial\bm{J}_{i}}{\partial t}+\frac{\partial\bm{J}_{e,gc}}{\partial t}\right).(28)

Multiplying the ion Vlasov equation (15) withqi​𝒗iq_{i}\bm{v}_{i}and integrating over the velocity space gives:∂𝑱i∂t=qimi​(ρi​𝑬+𝑱i×𝑩−∇⋅𝕊i),\frac{\partial\bm{J}_{i}}{\partial t}=\frac{q_{i}}{m_{i}}(\rho_{i}\bm{E}+\bm{J}_{i}\times\bm{B}-\nabla\cdot\mathbb{S}_{i}),(29)

whereρi\rho_{i}and𝑱i\bm{J}_{i}are the ion charge and ion current densities defined in equations (21) and (18), respectively. The term𝕊i\mathbb{S}_{i}is the contribution of the ion species to the stress tensor, given by:𝕊i=mi​∫fi​𝒗i⊗𝒗i​𝑑𝒗.\mathbb{S}_{i}=m_{i}\int f_{i}\bm{v}_{i}\otimes\bm{v}_{i}d\bm{v}.(30)

The term𝒃e​q⋅∂𝑱e,g​c∂t\bm{b}_{eq}\cdot\frac{\partial\bm{J}_{e,gc}}{\partial t}becomes∂Je,gc∥∂t\frac{\partial J_{e,gc\parallel}}{\partial t}, whereJe,gc∥J_{e,gc\parallel}is given by:Je,gc∥=qe​∫v∥​fe,g​c​B∥∗​d​v∥​d​μ.J_{e,gc\parallel}=q_{e}\int v_{\parallel}f_{e,gc}B^{\ast}_{\parallel}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu.\\(31)

To obtain∂Je,gc∥∂t\frac{\partial J_{e,gc\parallel}}{\partial t}, we multiply the drift-kinetic electron Vlasov equation (12) withqe​v∥q_{e}v_{\parallel}and integrate over the velocity space to get:∂Je,gc∥∂t+∇⋅(𝒑∗+(η​𝑬−Q​∇B∥,tot)×𝒃e​q)−𝜶∗⋅𝑬+𝝁∗⋅∇B∥,tot=0,\frac{\partial J_{e,gc\parallel}}{\partial t}+\nabla\cdot\left(\bm{p}^{\ast}+(\eta\bm{E}-Q\nabla B_{\parallel,tot})\times\bm{b}_{eq}\right)-\bm{\alpha}^{\ast}\cdot\bm{E}+\bm{\mu}^{\ast}\cdot\nabla B_{\parallel,tot}=0,(32)

where we define:𝒑∗​(𝒙)\displaystyle\bm{p}^{\ast}(\bm{x})=qe​∫v∥2​fe,g​c​𝑩∗​d​v∥​d​μ,\displaystyle=q_{e}\int v_{\parallel}^{2}f_{e,gc}\bm{B}^{\ast}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu,(33)η​(𝒙)\displaystyle\eta(\bm{x})=qe​∫v∥​fe,g​c​d​v∥​d​μ,\displaystyle=q_{e}\int v_{\parallel}f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu,(34)Q​(𝒙)\displaystyle Q(\bm{x})=∫v∥​μ​fe,g​c​d​v∥​d​μ,\displaystyle=\int v_{\parallel}\mu f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu,(35)𝜶∗​(𝒙)\displaystyle\bm{\alpha}^{\ast}(\bm{x})=qe2me​∫fe,g​c​𝑩∗​d​v∥​d​μ,\displaystyle=\frac{q_{e}^{2}}{m_{e}}\int f_{e,gc}\bm{B}^{\ast}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu,(36)𝝁∗​(𝒙)\displaystyle\bm{\mu}^{\ast}(\bm{x})=qeme​∫μ​fe,g​c​𝑩∗​d​v∥​d​μ.\displaystyle=\frac{q_{e}}{m_{e}}\int\mu f_{e,gc}\bm{B}^{\ast}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu.(37)

In equation (36), the term𝜶∗⋅𝑬\bm{\alpha}^{\ast}\cdot\bm{E}reduces to(𝜶∗⋅𝑬⟂+𝜶∗⋅𝒃e​q​E∥)(\bm{\alpha}^{\ast}\cdot\bm{E}_{\perp}+\bm{\alpha}^{\ast}\cdot\bm{b}_{eq}E_{\parallel}). The term𝜶∗⋅𝒃e​q\bm{\alpha}^{\ast}\cdot\bm{b}_{eq}becomes:𝜶∗⋅𝒃e​q=qe2me​∫fe,g​c​B∥∗​d​v∥​d​μ=qeme​ρe,g​c.\bm{\alpha}^{\ast}\cdot\bm{b}_{eq}=\frac{q_{e}^{2}}{m_{e}}\int f_{e,gc}B^{\ast}_{\parallel}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu=\frac{q_{e}}{m_{e}}\rho_{e,gc}.(38)

Therefore, substituting (29), (32) and (38) in (28), the equation forE∥E_{\parallel}becomes:−∇⟂2E∥+μ0​(qi2mi​ni+qe2me​ne,g​c)​E∥=μ0​𝒃e​q⋅(qimi​(−𝑱i×𝑩+∇⋅𝕊i))+μ0​(∇⋅(𝒑∗+(η​𝑬⟂−Q​∇B∥,tot)×𝒃e​q)−𝜶∗⋅𝑬⟂+𝝁∗⋅∇B∥,tot)−∇∥(∇⟂⋅𝑬⟂).-\nabla_{\perp}^{2}E_{\parallel}+\mu_{0}\left(\frac{q_{i}^{2}}{m_{i}}n_{i}+\frac{q_{e}^{2}}{m_{e}}n_{e,gc}\right)E_{\parallel}=\mu_{0}\bm{b}_{eq}\cdot\left(\frac{q_{i}}{m_{i}}(-\bm{J}_{i}\times\bm{B}+\nabla\cdot\mathbb{S}_{i})\right)+\\
\mu_{0}\left(\nabla\cdot\left(\bm{p}^{\ast}+(\eta\bm{E}_{\perp}-Q\nabla B_{\parallel,tot})\times\bm{b}_{eq}\right)-\bm{\alpha}^{\ast}\cdot\bm{E}_{\perp}+\bm{\mu}^{\ast}\cdot\nabla B_{\parallel,tot}\right)-\nabla_{\parallel}(\nabla_{\perp}\cdot\bm{E}_{\perp}).(39)

Here,ni=qi​ρin_{i}=q_{i}\rho_{i}andne,g​c=qe​ρe,g​cn_{e,gc}=q_{e}\rho_{e,gc}are the ion and electron number densities, respectively. Knowing𝑬⟂\bm{E}_{\perp}from equation (26), we can solve forE∥E_{\parallel}using equation (39). The left hand side of equation (39) gives a symmetric, positive definite matrix after discretization, making it a determinate and non-singular system with a unique solution. The magnetic moment,μ\mu, is assumed to be zero in the work presented here. This simplifiesQ​(𝒙)Q(\bm{x})and𝝁∗​(𝒙)\bm{\mu}^{\ast}(\bm{x})in equation (39) and the∇B∥,tot\nabla B_{\parallel,tot}terms in equations (10), (11) and (26) to zero. Going forward, this term and its discretized equivalent will not be shown in any of the equations in the upcoming sections.

## 3Structure-preserving spatial discretization of fields

We use a dual grid approach for the spatial discretization of our model, wherein the dual or adjoint grid vertices are the barycenters of the primal grid cells. The numerical values for the field variables are located on spaces based on points, edges, faces and volumes of hexahedral (3D) or quadrilateral (2D) cells. This discretization, based on mimetic finite differences, has already been used inGEMPICXfor discretizing the fully kinetic(kormann2024), drift-kinetic(meng2025)and fully kinetic quasineutral(narechania2026FKQN)Vlasov-Maxwell models. The nodal, edge, face and volume spaces on the primal grids are denoted by𝒞0\mathcal{C}_{0},𝒞1\mathcal{C}_{1},𝒞2\mathcal{C}_{2}and𝒞3\mathcal{C}_{3}, respectively. Similarly, those on the dual grids are denoted by𝒞~0\tilde{\mathcal{C}}_{0},𝒞~1\tilde{\mathcal{C}}_{1},𝒞~2\tilde{\mathcal{C}}_{2}and𝒞~3\tilde{\mathcal{C}}_{3}, respectively. A duality exists between the primal and duality spaces. The nodes, edges, faces and cell volumes on the primal grid are each uniquely associated with the cell volumes, faces, edges and nodes on the dual grid, respectively. On the primal grid, the electric field𝑬\bm{E}and the vector potential𝑨\bm{A}are defined as edge-integrals and the magnetic field𝑩\bm{B}is defined as face-integrals. On the dual grid, the magnetic field intensity𝑯\bm{H}is defined as edge-integrals, the current density𝑱\bm{J}and electric field intensity𝑫\bm{D}are defined as face-integrals, and the charge densityρ\rhois defined as volume-integrals. Such an approach allows for exact preservation of certain discretized quantities. For example, the discrete divergence of𝑱\bm{J}becomes a cell-integral on the dual grid, which is the same space where the charge densityρ\rhois defined. These spaces are shown in Figure1for the primal grid.Figure 1:Spaces for defining discrete variables on a primal Cartesian grid.

## 3.1Reduction operators

The reduction operators, also called restriction operators, relate a continuous field to its discretized counterparts defined on nodes, edges, faces and volumes. On the primal grid:
- •

ℛ0\mathcal{R}_{0}associates a scalar field to its values at primal grid nodes:ℛ0​(ψ)i,j,k=ψ​(xi,yj,zk)=ψψi,j,k.\displaystyle\mathcal{R}_{0}(\psi)_{i,j,k}=\psi(x_{i},y_{j},z_{k})={\text{\vtop{\halign{#\cr\hfil y\hfil\cr\hfil\raise 0.43057pt\hbox{y}\hfil\cr}}}}_{i,j,k}.(42)

Here,ψψ∈𝒞0\text{\vtop{\halign{#\cr\hfil y\hfil\cr\hfil\raise 0.43057pt\hbox{y}\hfil\cr}}}\in\mathcal{C}_{0}.
- •

ℛ1\mathcal{R}_{1}associates a vector field to its integrals on primal grid edges. For thex−x-edge, we have:ℛ1x​(Ex)i,j,k=∫xixi+1Ex​(x,yj,zk)​d​x=𝗘i+1/2,j,k=𝗘i,j,kx.\displaystyle\mathcal{R}_{1}^{x}(E_{x})_{i,j,k}=\int_{x_{i}}^{x_{i+1}}E_{x}(x,y_{j},z_{k})\mathop{}\!\mathrm{d}x={{\bm{\mathsf{E}}}}_{i+1/2,j,k}={{\bm{\mathsf{E}}}}^{x}_{i,j,k}.(43)

Similarly,ℛ1y​(Ey)i,j,k\mathcal{R}_{1}^{y}(E_{y})_{i,j,k}andℛ1z​(Ez)i,j,k\mathcal{R}_{1}^{z}(E_{z})_{i,j,k}can be defined. The complete operator becomes:
ℛ1​(𝑬)=(ℛ1x​(Ex),ℛ1y​(Ey),ℛ1z​(Ez))=(𝗘x,𝗘y,𝗘z)=𝗘∈𝒞1\mathcal{R}_{1}(\bm{E})=(\mathcal{R}_{1}^{x}(E_{x}),\mathcal{R}_{1}^{y}(E_{y}),\mathcal{R}_{1}^{z}(E_{z}))=({{\bm{\mathsf{E}}}}^{x},{{\bm{\mathsf{E}}}}^{y},{{\bm{\mathsf{E}}}}^{z})={\bm{\mathsf{E}}}\in\mathcal{C}_{1}.
- •

ℛ2\mathcal{R}_{2}associates a vector field to its integrals on primal grid faces. For thex−x-edge, we have:ℛ2x​(Bx)i,j,k=∫zkzk+1∫yjyj+1Bx​(xi,y,z)​d​y​d​z=𝗕i,j+1/2,k+1/2=𝗕i,j,kx.\displaystyle\mathcal{R}_{2}^{x}(B_{x})_{i,j,k}=\int_{z_{k}}^{z_{k+1}}\int_{y_{j}}^{y_{j+1}}B_{x}(x_{i},y,z)\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}z={{\bm{\mathsf{B}}}}_{i,j+1/2,k+1/2}={{\bm{\mathsf{B}}}}^{x}_{i,j,k}.(44)

Similarly,ℛ2y​(By)i,j,k\mathcal{R}_{2}^{y}(B_{y})_{i,j,k}andℛ2z​(Bz)i,j,k\mathcal{R}_{2}^{z}(B_{z})_{i,j,k}can be defined. The complete operator becomes:
ℛ2​(𝑩)=(ℛ2x​(Bx),ℛ2y​(By),ℛ2z​(Bz))=(𝗕x,𝗕y,𝗕z)=𝗕∈𝒞2\mathcal{R}_{2}(\bm{B})=(\mathcal{R}_{2}^{x}(B_{x}),\mathcal{R}_{2}^{y}(B_{y}),\mathcal{R}_{2}^{z}(B_{z}))=({{\bm{\mathsf{B}}}}^{x},{{\bm{\mathsf{B}}}}^{y},{{\bm{\mathsf{B}}}}^{z})={\bm{\mathsf{B}}}\in\mathcal{C}_{2}.
- •

ℛ3\mathcal{R}_{3}associates a scalar field to its volume integrals over primal grid cells:ℛ3​(ρ)i,j,k=∫zkzk+1∫yjyj+1∫xixi+1ρ​(x,y,z)​d​x​d​y​d​z=ϱi,j,k.\displaystyle\mathcal{R}_{3}(\rho)_{i,j,k}=\int_{z_{k}}^{z_{k+1}}\int_{y_{j}}^{y_{j+1}}\int_{x_{i}}^{x_{i+1}}\rho(x,y,z)\mathop{}\!\mathrm{d}x\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}z={\bm{\varrho}}_{i,j,k}.(45)

Here,ϱ∈𝒞3\bm{\varrho}\in\mathcal{C}_{3}.

Similarly, reduction/restriction operators are also defined on the dual grid as follows:
- •

ℛ~0\tilde{\mathcal{R}}_{0}associates a scalar field to its values at dual grid nodes:ℛ~0​(ϕ)i,j,k=ϕ​(xi+1/2,yj+1/2,zk+1/2)=ψφ~i+1/2,j+1/2,k+1/2.\displaystyle\tilde{\mathcal{R}}_{0}(\phi)_{i,j,k}=\phi(x_{i+1/2},y_{j+1/2},z_{k+1/2})=\tilde{\text{\vtop{\halign{#\cr\hfil y\hfil\cr\hfil\raise 0.43057pt\hbox{f}\hfil\cr}}}}_{i+1/2,j+1/2,k+1/2}.(48)

Here,ψφ~∈𝒞~0\tilde{\text{\vtop{\halign{#\cr\hfil y\hfil\cr\hfil\raise 0.43057pt\hbox{f}\hfil\cr}}}}\in\tilde{\mathcal{C}}_{0}.
- •

ℛ~1\tilde{\mathcal{R}}_{1}associates a vector field to its integrals on dual grid edges. For thex−x-edge, we have:ℛ~1x​(Hx)i,j,k=∫xi−1/2xi+1/2Hx​(x,yj+1/2,zk+1/2)​d​x=𝗛~i,j+1/2,k+1/2=𝗛~i,j,kx.\displaystyle\tilde{\mathcal{R}}_{1}^{x}(H_{x})_{i,j,k}=\int_{x_{i-1/2}}^{x_{i+1/2}}H_{x}(x,y_{j+1/2},z_{k+1/2})\mathop{}\!\mathrm{d}x=\tilde{{\bm{\mathsf{H}}}}_{i,j+1/2,k+1/2}=\tilde{{\bm{\mathsf{H}}}}^{x}_{i,j,k}.(49)

Similarly,ℛ~1y​(Hy)i,j,k\tilde{\mathcal{R}}_{1}^{y}(H_{y})_{i,j,k}andℛ~1z​(Hz)i,j,k\tilde{\mathcal{R}}_{1}^{z}(H_{z})_{i,j,k}can be defined. The complete operator becomes:
ℛ~1​(𝑯)=(ℛ~1x​(Hx),ℛ~1y​(Hy),ℛ~1z​(Hz))=(𝗛~x,𝗛~y,𝗛~z)=𝗛~∈𝒞~1\tilde{\mathcal{R}}_{1}(\bm{H})=(\tilde{\mathcal{R}}_{1}^{x}(H_{x}),\tilde{\mathcal{R}}_{1}^{y}(H_{y}),\tilde{\mathcal{R}}_{1}^{z}(H_{z}))=(\tilde{{\bm{\mathsf{H}}}}^{x},\tilde{{\bm{\mathsf{H}}}}^{y},\tilde{{\bm{\mathsf{H}}}}^{z})=\tilde{{\bm{\mathsf{H}}}}\in\tilde{\mathcal{C}}_{1}.
- •

ℛ~2\tilde{\mathcal{R}}_{2}relates a vector field to its integrals on dual grid faces. For thex−x-edge, we have:ℛ~2x​(Dx)i,j,k=∫zk−1/2zk+1/2∫yj−1/2yj+1/2Dx​(xi+1/2,y,z)​d​y​d​z=𝗗~i+1/2,j,k=𝗗~i,j,kx.\displaystyle\tilde{\mathcal{R}}_{2}^{x}(D_{x})_{i,j,k}=\int_{z_{k-1/2}}^{z_{k+1/2}}\int_{y_{j-1/2}}^{y_{j+1/2}}D_{x}(x_{i+1/2},y,z)\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}z=\tilde{{\bm{\mathsf{D}}}}_{i+1/2,j,k}=\tilde{{\bm{\mathsf{D}}}}^{x}_{i,j,k}.(50)

Similarlyℛ~2y​(Dy)i,j,k\tilde{\mathcal{R}}_{2}^{y}(D_{y})_{i,j,k}andℛ~2z​(Dz)i,j,k\tilde{\mathcal{R}}_{2}^{z}(D_{z})_{i,j,k}can be defined. The complete operator becomes:
ℛ~2​(𝑫)=(ℛ~2x​(Dx),ℛ~2y​(Dy),ℛ~2z​(Dz))=(𝗗~x,𝗗~y,𝗗~z)=𝗗~∈𝒞~2\tilde{\mathcal{R}}_{2}(\bm{D})=(\tilde{\mathcal{R}}_{2}^{x}(D_{x}),\tilde{\mathcal{R}}_{2}^{y}(D_{y}),\tilde{\mathcal{R}}_{2}^{z}(D_{z}))=(\tilde{{\bm{\mathsf{D}}}}^{x},\tilde{{\bm{\mathsf{D}}}}^{y},\tilde{{\bm{\mathsf{D}}}}^{z})=\tilde{{\bm{\mathsf{D}}}}\in\tilde{\mathcal{C}}_{2}.
- •

ℛ~3\tilde{\mathcal{R}}_{3}relates a scalar field to its volume integrals over dual grid cells:ℛ~3​(ρ)i,j,k=∫zk−1/2zk+1/2∫yj−1/2yj+1/2∫xi−1/2xi+1/2ρ​(x,y,z)​d​x​d​y​d​z=ϱ~i,j,k.\displaystyle\tilde{\mathcal{R}}_{3}(\rho)_{i,j,k}=\int_{z_{k-1/2}}^{z_{k+1/2}}\int_{y_{j-1/2}}^{y_{j+1/2}}\int_{x_{i-1/2}}^{x_{i+1/2}}\rho(x,y,z)\mathop{}\!\mathrm{d}x\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}z=\tilde{\bm{\varrho}}_{i,j,k}.(51)

Here,ϱ~∈𝒞~3\tilde{\bm{\varrho}}\in\tilde{\mathcal{C}}_{3}.

## 3.2Hodge operators

Field variables can be projected from primal grid spaces to their dual counterparts or vice versa using Hodge operators. Hodge operators of an arbitrary order of accuracy can be obtained using the method prescribed bykormann2024. In the current work, only second-order Hodge projections have been used and this simply constitutes the use of scaling factors to relate variables between primal and dual spaces. Consider arbitrary variables𝑲\bm{K},𝑳\bm{L},𝑴\bm{M}and𝑵\bm{N}, defined on primal nodes, edges, faces and cell volumes, respectively. Their corresponding dual mappings, defined on dual cell volumes, faces, edges and nodes are denoted as𝑲~\tilde{\bm{K}},𝑳~\tilde{\bm{L}},𝑴~\tilde{\bm{M}}and𝑵~\tilde{\bm{N}}, respectively. These would be given by:𝗞~=Δ​x​Δ​y​Δ​z​𝗞,\displaystyle\tilde{{\bm{\mathsf{K}}}}=\Delta x\,\Delta y\,\Delta z{\bm{\mathsf{K}}},𝗟~x=Δ​y​Δ​zΔ​x​𝗟x,𝗟~y=Δ​x​Δ​zΔ​y​𝗟y,𝗟~z=Δ​x​Δ​yΔ​z​𝗟z,\displaystyle\tilde{{\bm{\mathsf{L}}}}^{x}=\frac{\Delta y\,\Delta z}{\Delta x}{\bm{\mathsf{L}}}^{x},\quad\tilde{{\bm{\mathsf{L}}}}^{y}=\frac{\Delta x\,\Delta z}{\Delta y}{\bm{\mathsf{L}}}^{y},\quad\tilde{{\bm{\mathsf{L}}}}^{z}=\frac{\Delta x\,\Delta y}{\Delta z}{\bm{\mathsf{L}}}^{z},𝗠~x=Δ​xΔ​y​Δ​z​𝗠x,𝗠~y=Δ​yΔ​x​Δ​z​𝗠y,𝗠~z=Δ​zΔ​x​Δ​y​𝗠z,\displaystyle\tilde{{\bm{\mathsf{M}}}}^{x}=\frac{\Delta x}{\Delta y\,\Delta z}{\bm{\mathsf{M}}}^{x},\quad\tilde{{\bm{\mathsf{M}}}}^{y}=\frac{\Delta y}{\Delta x\,\Delta z}{\bm{\mathsf{M}}}^{y},\quad\tilde{{\bm{\mathsf{M}}}}^{z}=\frac{\Delta z}{\Delta x\,\Delta y}{\bm{\mathsf{M}}}^{z},𝗡~=1Δ​x​Δ​y​Δ​z​𝗡.\displaystyle\tilde{{\bm{\mathsf{N}}}}=\frac{1}{\Delta x\,\Delta y\,\Delta z}{\bm{\mathsf{N}}}.(52)

We can therefore define Hodge operatorsℍ0\mathbb{H}_{0},ℍ1\mathbb{H}_{1},ℍ2\mathbb{H}_{2}, andℍ3\mathbb{H}_{3}, and their corresponding inversesℍ~3\tilde{\mathbb{H}}_{3},ℍ~2\tilde{\mathbb{H}}_{2},ℍ~1\tilde{\mathbb{H}}_{1}, andℍ~0\tilde{\mathbb{H}}_{0}, respectively:𝗞~=ℍ0​𝗞,𝗞=ℍ~3​𝗞~,\displaystyle\tilde{{\bm{\mathsf{K}}}}=\mathbb{H}_{0}{\bm{\mathsf{K}}},\;\hskip 14.22636pt{\bm{\mathsf{K}}}=\tilde{\mathbb{H}}_{3}\tilde{{\bm{\mathsf{K}}}},𝗟~=ℍ1​𝗟,𝗟=ℍ~2​𝗟~,\displaystyle\tilde{{\bm{\mathsf{L}}}}=\mathbb{H}_{1}{\bm{\mathsf{L}}},\;\hskip 14.22636pt{\bm{\mathsf{L}}}=\tilde{\mathbb{H}}_{2}\tilde{{\bm{\mathsf{L}}}},𝗠~=ℍ2​𝗠,𝗠=ℍ~1​𝗠~,\displaystyle\tilde{{\bm{\mathsf{M}}}}=\mathbb{H}_{2}{\bm{\mathsf{M}}},\;\hskip 14.22636pt{\bm{\mathsf{M}}}=\tilde{\mathbb{H}}_{1}\tilde{{\bm{\mathsf{M}}}},𝗡~=ℍ3​𝗡,𝗡=ℍ~0​𝗡~.\displaystyle\tilde{{\bm{\mathsf{N}}}}=\mathbb{H}_{3}{\bm{\mathsf{N}}},\;\hskip 14.22636pt{\bm{\mathsf{N}}}=\tilde{\mathbb{H}}_{0}\tilde{{\bm{\mathsf{N}}}}.(53)

Accordingly, the electric and magnetic fields can be related to their intensities as follows:𝗗~=ℍ1​𝗘,𝗘=ℍ~2​𝗗~,\displaystyle\tilde{{\bm{\mathsf{D}}}}=\mathbb{H}_{1}{\bm{\mathsf{E}}},\;\hskip 14.22636pt{\bm{\mathsf{E}}}=\tilde{\mathbb{H}}_{2}\tilde{{\bm{\mathsf{D}}}},𝗛~=ℍ2​𝗕,𝗕=ℍ~1​𝗛~.\displaystyle\tilde{{\bm{\mathsf{H}}}}=\mathbb{H}_{2}{\bm{\mathsf{B}}},\;\hskip 14.22636pt{\bm{\mathsf{B}}}=\tilde{\mathbb{H}}_{1}\tilde{{\bm{\mathsf{H}}}}.(54)

These various Hodge operators are simply the appropriate scaling factors multiplied by the identity matrix. This corresponds to the classical Yee scheme. While we use only the second-order scheme here, the reader is referred to the work bykormann2024for details of higher-order Hodge operators and their implementation.

## 3.3Discrete scalar products

Discrete approximations ofL2L^{2}inner products of scalar or vector fields can be calculated using discrete scalar products between primal field variables and their dual grid Hodge projections. For the variables𝑲\bm{K},𝑳\bm{L},𝑴\bm{M}and𝑵\bm{N}defined above, these discrete scalar products are as follows:𝗞⋅𝗞~=∑i,j,k𝗞i,j,k​𝗞~i,j,k,{\bm{\mathsf{K}}}\cdot\tilde{{\bm{\mathsf{K}}}}=\sum_{i,j,k}{\bm{\mathsf{K}}}_{i,j,k}\tilde{{\bm{\mathsf{K}}}}_{i,j,k},(55)𝗟⋅𝗟~=𝗟x⋅𝗟~x+𝗟y⋅𝗟~y+𝗟z⋅𝗟~z\displaystyle{\bm{\mathsf{L}}}\cdot\tilde{{\bm{\mathsf{L}}}}={\bm{\mathsf{L}}}^{x}\cdot\tilde{{\bm{\mathsf{L}}}}^{x}+{\bm{\mathsf{L}}}^{y}\cdot\tilde{{\bm{\mathsf{L}}}}^{y}+{\bm{\mathsf{L}}}^{z}\cdot\tilde{{\bm{\mathsf{L}}}}^{z}=∑i,j,k(𝗟i+1/2,j,k​𝗟~i+1/2,j,k+𝗟i,j+1/2,k​𝗟~i,j+1/2,k+𝗟i,j,k+1/2​𝗟~i,j,k+1/2),\displaystyle=\sum_{i,j,k}\big({\bm{\mathsf{L}}}_{i+1/2,j,k}\tilde{{\bm{\mathsf{L}}}}_{i+1/2,j,k}+{\bm{\mathsf{L}}}_{i,j+1/2,k}\tilde{{\bm{\mathsf{L}}}}_{i,j+1/2,k}+{\bm{\mathsf{L}}}_{i,j,k+1/2}\tilde{{\bm{\mathsf{L}}}}_{i,j,k+1/2}\big),(56)𝗠⋅𝗠~=𝗠x⋅𝗠~x+𝗠y⋅𝗠~y+𝗠z⋅𝗠~z\displaystyle{\bm{\mathsf{M}}}\cdot\tilde{{\bm{\mathsf{M}}}}={\bm{\mathsf{M}}}^{x}\cdot\tilde{{\bm{\mathsf{M}}}}^{x}+{\bm{\mathsf{M}}}^{y}\cdot\tilde{{\bm{\mathsf{M}}}}^{y}+{\bm{\mathsf{M}}}^{z}\cdot\tilde{{\bm{\mathsf{M}}}}^{z}=∑i,j,k(𝗠i,j+1/2,k+1/2​𝗠~i,j+1/2,k+1/2+𝗠i+1/2,j,k+1/2​𝗠~i+1/2,j,k+1/2+𝗠i+1/2,j+1/2,k​𝗠~i+1/2,j+1/2,k),\displaystyle=\sum_{i,j,k}\big({\bm{\mathsf{M}}}_{i,j+1/2,k+1/2}\tilde{{\bm{\mathsf{M}}}}_{i,j+1/2,k+1/2}+{\bm{\mathsf{M}}}_{i+1/2,j,k+1/2}\tilde{{\bm{\mathsf{M}}}}_{i+1/2,j,k+1/2}+{\bm{\mathsf{M}}}_{i+1/2,j+1/2,k}\tilde{{\bm{\mathsf{M}}}}_{i+1/2,j+1/2,k}\big),(57)𝗡⋅𝗡~=∑i,j,k𝗡i+1/2,j+1/2,k+1/2​𝗡~i+1/2,j+1/2,k+1/2.{\bm{\mathsf{N}}}\cdot\tilde{{\bm{\mathsf{N}}}}=\sum_{i,j,k}{\bm{\mathsf{N}}}_{i+1/2,j+1/2,k+1/2}\tilde{{\bm{\mathsf{N}}}}_{i+1/2,j+1/2,k+1/2}.(58)

## 3.4Discrete gradient, curl and divergence

In order to define the discrete gradient, curl and divergence operators, we first define a one-dimensional discrete derivative or difference operator:𝕕M1=(−110…00−110⋮⋱⋱0−1110…0−1)∈ℝM1×M1.\mathbb{d}_{M_{1}}=\begin{pmatrix}-1&1&0&\ldots&0\\
0&-1&1&0&\\
\vdots&&\ddots&\ddots&\\
0&&&-1&1\\
1&0&\ldots&0&-1\end{pmatrix}\in\mathbb{R}^{M_{1}\times M_{1}}.

We can represent a𝕕\mathbb{d}matrix and an identity matrix of sizeNNas𝕕N\mathbb{d}_{N}and𝕀N\mathbb{I}_{N}, respectively. Consider a grid withN1N_{1},N2N_{2},N3N_{3}points in thex−x-,y−y-andz−z-directions, respectively, such thatN=N1×N2×N3N=N_{1}\times N_{2}\times N_{3}. For such a grid, the discrete gradient, curl, and divergence operators on the primal grid can be denoted by𝔾\mathbb{G},ℂ\mathbb{C}and𝔻\mathbb{D}. These are built using Kronecker products of the𝕕\mathbb{d}and𝕀\mathbb{I}matrices of appropriate sizes as follows:𝔾=(𝕕N1⊗𝕀N2⊗𝕀N3𝕀N1⊗𝕕N2⊗𝕀N3𝕀N1⊗𝕀N2⊗𝕕N3),\mathbb{G}=\begin{pmatrix}\mathbb{d}_{N_{1}}\otimes\mathbb{I}_{N_{2}}\otimes\mathbb{I}_{N_{3}}\\
\mathbb{I}_{N_{1}}\otimes\mathbb{d}_{N_{2}}\otimes\mathbb{I}_{N_{3}}\\
\mathbb{I}_{N_{1}}\otimes\mathbb{I}_{N_{2}}\otimes\mathbb{d}_{N_{3}}\end{pmatrix},(59)ℂ=(𝕆N−𝕀N1⊗𝕀N2⊗𝕕N3𝕀N1⊗𝕕N2⊗𝕀N3𝕀N1⊗𝕀N2⊗𝕕N3𝕆N−𝕕N1⊗𝕀N2⊗𝕀N3−𝕀N1⊗𝕕N2⊗𝕀N3𝕕N1⊗𝕀N2⊗𝕀N3𝕆N),\mathbb{C}=\begin{pmatrix}\mathbb{O}_{N}&-\mathbb{I}_{N_{1}}\otimes\mathbb{I}_{N_{2}}\otimes\mathbb{d}_{N_{3}}&\mathbb{I}_{N_{1}}\otimes\mathbb{d}_{N_{2}}\otimes\mathbb{I}_{N_{3}}\\
\mathbb{I}_{N_{1}}\otimes\mathbb{I}_{N_{2}}\otimes\mathbb{d}_{N_{3}}&\mathbb{O}_{N}&-\mathbb{d}_{N_{1}}\otimes\mathbb{I}_{N_{2}}\otimes\mathbb{I}_{N_{3}}\\
-\mathbb{I}_{N_{1}}\otimes\mathbb{d}_{N_{2}}\otimes\mathbb{I}_{N_{3}}&\mathbb{d}_{N_{1}}\otimes\mathbb{I}_{N_{2}}\otimes\mathbb{I}_{N_{3}}&\mathbb{O}_{N}\\
\end{pmatrix},(60)𝔻=(𝕕N1⊗𝕀N2⊗𝕀N3𝕀N1⊗𝕕N2⊗𝕀N3𝕀N1⊗𝕀N2⊗𝕕N3).\mathbb{D}=\begin{pmatrix}\mathbb{d}_{N_{1}}\otimes\mathbb{I}_{N_{2}}\otimes\mathbb{I}_{N_{3}}&\mathbb{I}_{N_{1}}\otimes\mathbb{d}_{N_{2}}\otimes\mathbb{I}_{N_{3}}&\mathbb{I}_{N_{1}}\otimes\mathbb{I}_{N_{2}}\otimes\mathbb{d}_{N_{3}}\\
\end{pmatrix}.(61)

The adjoint operators of these operators on the dual grid are given by:𝔾~=−𝔻T,\displaystyle\tilde{\mathbb{G}}=-\mathbb{D}^{T},(62)ℂ~=ℂT,\displaystyle\tilde{\mathbb{C}}=\mathbb{C}^{T},(63)𝔻~=−𝔾T.\displaystyle\tilde{\mathbb{D}}=-\mathbb{G}^{T}.(64)

Due to our degrees of freedom being defined on discrete spaces associated with the de Rham complex, the discrete gradient, curl and divergence operators and their dual operators are always exact.

## 4Particle-in-Cell (PIC) discretization

Let us now consider the particle discretization of the Vlasov equation, where we write:fs​(t,𝒙,𝒗)=∑p=1Nswp​δ​(𝒙−𝒙p​(t))​δ​(𝒗−𝒗p​(t)),f_{s}(t,\bm{x},\bm{v})=\sum_{p=1}^{N_{s}}w_{p}\delta(\bm{x}-\bm{x}_{p}(t))\delta(\bm{v}-\bm{v}_{p}(t)),(65)

wherewpw_{p}is the particle weight,NsN_{s}is the number of particles of species ‘ss’ andδ\deltais the Dirac delta function. This function is clearly not continuous and smooth. However, in order to use particle information to calculate fields such asρ\rho,𝑱\bm{J}and𝕊\mathbb{S}in their discretized forms, we would require a smoothing kernel, typically a spline. Such a spline would effectively spread out the influence of the particle’s mass and charge over a volume centered at the particle location, rather than keep it concentrated at a single point. Hence, for a generic splineSS, the smoothed particle charge densityρs\rho_{s}and particle current density𝑱s\bm{J}_{s}, where the species ‘ss’ can be either ions or electrons, would be given by:ρs​(t,𝒙)\displaystyle\rho_{s}(t,\bm{x})=∑p=1Nsqs​ws,p​S​(𝒙−𝒙p​(t)),\displaystyle=\sum_{p=1}^{N_{s}}q_{s}w_{s,p}S(\bm{x}-\bm{x}_{p}(t)),(66)𝑱s​(t,𝒙)\displaystyle\bm{J}_{s}(t,\bm{x})=∑p=1Nsqs​𝒗s,p​ws,p​S​(𝒙−𝒙p​(t)).\displaystyle=\sum_{p=1}^{N_{s}}q_{s}\bm{v}_{s,p}w_{s,p}S(\bm{x}-\bm{x}_{p}(t)).(67)

These splines would also be used to calculate electric and magnetic fields at particle locations using the discretized forms of the fields. The particles then obey equations (10) and (11), or equations (13) and (14), depending on the species. The splines used in this work are based on the well-known cardinal B-splines. Fundamental cardinal B-splines of an arbitrary degreeddcentered atx=0x=0can be defined recursively using the convolution:S(d)​(x)=S(0)∗S(d−1)​(x)=∫−1/21/2S(d−1)​(x−x′)​𝑑x′,S^{(d)}(x)=S^{(0)}*S^{(d-1)}(x)=\int_{-1/2}^{1/2}S^{(d-1)}(x-x^{\prime})\,dx^{\prime},(68)

withS(0)​(x)={1if−12≤x≤120otherwise.S^{(0)}(x)=\begin{cases}1&\text{if }-\frac{1}{2}\leq x\leq\frac{1}{2}\\
0&\text{otherwise}\end{cases}.(69)

Cardinal B-splines have the property:∫−∞∞S(d)​(x)​𝑑x=1.\int_{-\infty}^{\infty}S^{(d)}(x)\,dx=1.(70)

The coupling of particles and fields involves two kinds of B-splines: node splines and cell splines. These splines are built using the cardinal B-spline described above.

These splines are essential to evaluation of𝑬\bm{E},𝑩\bm{B}fields at particle positions and evaluation of particle-integrated field variables like charge densityρ\rhoand current density𝑱\bm{J}, as defined in their respective spaces. Consider the mesh size in thex−x-direction to be denoted ashh. Node splines are centered on grid nodes, and are defined as:Sin​(xp)=Sd​((xp−xi)/h).S_{i}^{n}(x_{p})=S^{d}((x_{p}-x_{i})/h).(71)

This spline is supported on the interval[xi−(d+1)​h/2,xi+(d+1)​h/2][x_{i}-(d+1)h/2,x_{i}+(d+1)h/2], and its values are independent of the grid size.
Cell splines are centered on cell midpoints, and are defined as:Sic​(xp)=1h​Sd−1​(xp−xi+1/2h).S_{i}^{c}(x_{p})=\frac{1}{h}S^{d-1}\left(\frac{x_{p}-x_{i+1/2}}{h}\right).(72)

This spline is supported on the interval[xi+1/2−d​h/2,xi+1/2+d​h/2][x_{i+1/2}-dh/2,x_{i+1/2}+dh/2], and its cell-integrals are independent of the grid size. Node and cell splines for they−y-andz−z-directions can be similarly defined given the respective mesh sizes in those directions.

The particle charge densitiesρs\rho_{s}are defined as cell volume integrals on the dual grid i.e.ϱ~s=ℛ~3​(ρs)∈𝒞~3\tilde{\bm{\varrho}}_{s}=\tilde{\mathcal{R}}_{3}(\rho_{s})\in\tilde{\mathcal{C}}_{3}. These are calculated as:ϱ~s​(t)i,j,k=ℛ~3​(ρs​(t))i,j,k=∑p=1Nsqs​ws,p​Sin​(xs,p​(t))​Sjn​(ys,p​(t))​Skn​(zs,p​(t)).\tilde{\bm{\varrho}}_{s}(t)_{i,j,k}=\tilde{\mathcal{R}}_{3}(\rho_{s}(t))_{i,j,k}=\sum_{p=1}^{N_{s}}q_{s}w_{s,p}S_{i}^{n}(x_{s,p}(t))S_{j}^{n}(y_{s,p}(t))S_{k}^{n}(z_{s,p}(t)).(73)

The particle current densities𝑱s\bm{J}_{s}are defined as face integrals on the dual grid i.e.𝗝~s=ℛ~2​(𝑱s)∈𝒞~2\tilde{{\bm{\mathsf{J}}}}_{s}=\tilde{\mathcal{R}}_{2}(\bm{J}_{s})\in\tilde{\mathcal{C}}_{2}. Thex−x-component, for instance, is calculated as:𝗝~sx​(t)i+1/2,j,k=ℛ~2​(Jsx​(t))i+1/2,j,k=∑p=1Nsqs​ws,p​vs,p,x​Sic​(xs,p​(t))​Sjn​(ys,p​(t))​Skn​(zs,p​(t)),\tilde{{\bm{\mathsf{J}}}}_{s}^{x}(t)_{i+1/2,j,k}=\tilde{\mathcal{R}}_{2}(J_{s}^{x}(t))_{i+1/2,j,k}=\sum_{p=1}^{N_{s}}q_{s}w_{s,p}v_{s,p,x}S_{i}^{c}(x_{s,p}(t))S_{j}^{n}(y_{s,p}(t))S_{k}^{n}(z_{s,p}(t)),(74)

wherevs,p,xv_{s,p,x}is thex−x-component of the velocity of the kinetic ions or the drift-kinetic electrons. Similarly, they−y-andz−z-components, i.e.𝗝~sy\tilde{{\bm{\mathsf{J}}}}_{s}^{y}and𝗝~sz\tilde{{\bm{\mathsf{J}}}}_{s}^{z}are calculated using the appropriate combinations of the cell and node splines. For the drift-kinetic electrons, the𝗝~e,g​c\tilde{{\bm{\mathsf{J}}}}_{e,gc}would also require calculation of electric and magnetic fields at the particle positions, which is described below. The terms𝑱i×𝑩\bm{J}_{i}\times\bm{B},p∗p^{\ast},η​𝑬\eta\bm{E},𝜶∗⋅𝑬\bm{\alpha}^{\ast}\cdot\bm{E}and𝕊i\mathbb{S}_{i}are all similarly defined as face integrals on the dual grid. Gradients of these terms, wherever required, are simply obtained by replacing the appropriateSnS^{n}orScS^{c}splines in these integrals with their respective spatial derivatives.

The smoothed electric and magnetic fields,𝑬S=(ExS,EyS,EzS)\bm{E}^{S}=(E_{x}^{S},E_{y}^{S},E_{z}^{S})and𝑩S=(BxS,ByS,BzS)\bm{B}^{S}=(B_{x}^{S},B_{y}^{S},B_{z}^{S}), used to update particle velocities, are also calculated at particle positions using node and cell splines. These fields are estimated as spline-weighted linear combinations of the edge-integrated or face-integrated values of these fields. For example, thex−x-components of these fields at particle position, for species ‘ss’, are calculated as:ExS​(𝒙s,p)\displaystyle E_{x}^{S}(\bm{x}_{s,p})=∑i,j,k𝗘i+1/2,j,k​Sic​(xs,p)​Sjn​(ys,p)​Skn​(zs,p),\displaystyle=\sum_{i,j,k}{{\bm{\mathsf{E}}}}_{i+1/2,j,k}S_{i}^{c}(x_{s,p})S_{j}^{n}(y_{s,p})S_{k}^{n}(z_{s,p}),(75)BxS​(𝒙s,p)\displaystyle B_{x}^{S}(\bm{x}_{s,p})=∑i,j,k𝗕i,j+1/2,k+1/2​Sin​(xs,p)​Sjc​(ys,p)​Skc​(zs,p).\displaystyle=\sum_{i,j,k}{{\bm{\mathsf{B}}}}_{i,j+1/2,k+1/2}S_{i}^{n}(x_{s,p})S_{j}^{c}(y_{s,p})S_{k}^{c}(z_{s,p}).(76)

Similarly, they−y-andz−z-components are calculated using the appropriate combinations of node and cell splines.

## 5Semi-discretized governing equations

We now propose a semi-discrete action principle and take its variations to obtain the semi-discrete governing equations. The discretization is only in space, while all quantities are still varying continuously with time. The semi-discrete electric field equations are also derived.

## 5.1Semi-discrete action principle

We use𝑿i\bm{X}_{i}and𝑽i\bm{V}_{i}to respectively denote positions and velocities of particles representing the fully kinetic ions. Similarly, for the drift-kinetic electrons, we use𝑿e,g​c\bm{X}_{e,gc}and𝑽e,g​c\bm{V}_{e,gc}for the guiding centers.
We follow the steps from the works bykormann2024andmeng2025to derive the discrete action principle for the hybrid quasineutral model. The semi-discrete Lagrangians for the drift-kinetic electrons, fully kinetic ions, and the fields are given by:ℒh,e=∑p=1Ne[we,p(meV∥,p𝒃e​q(𝑿e,p)+qe(𝗔e​q+𝗔))⋅ℛ~2(𝑿˙e,pSp(𝑿−𝑿e,p))−qeψφ⋅ℛ~3(Sp(𝑿−𝑿e,p))−me2V∥,p2],\mathcal{L}_{h,e}=\sum_{p=1}^{{N}_{e}}\left[w_{e,p}(m_{e}V_{\parallel,p}\bm{b}_{eq}(\bm{X}_{e,p})+q_{e}({\bm{\mathsf{A}}}_{eq}+{\bm{\mathsf{A}}}))\cdot\tilde{\mathcal{R}}_{2}\left(\dot{\bm{X}}_{e,p}S_{p}(\bm{X}-\bm{X}_{e,p})\right)\right.\\
\left.-q_{e}{\bm{\mathsf{\text{\vtop{\halign{#\cr\hfil y\hfil\cr\hfil\raise 0.43057pt\hbox{f}\hfil\cr}}}}}}\cdot\tilde{\mathcal{R}}_{3}(S_{p}(\bm{X}-\bm{X}_{e,p}))-\frac{m_{e}}{2}V_{\parallel,p}^{2}\right],(77)ℒh,i=∑p=1Ni[wi,p​(mi​𝑽i,p+qi​(𝗔e​q+𝗔))⋅ℛ~2​(𝑿˙i,p​S​(𝑿−𝑿i,p))−12​mi​Vi,p2−qi​ψφ⋅ℛ~3​(S​(𝑿−𝑿i,p))],\displaystyle\mathcal{L}_{h,i}=\sum_{p=1}^{N_{i}}\left[w_{i,p}(m_{i}\bm{V}_{i,p}+q_{i}({\bm{\mathsf{A}}}_{eq}+{\bm{\mathsf{A}}}))\cdot\tilde{\mathcal{R}}_{2}\left(\dot{\bm{X}}_{i,p}S(\bm{X}-\bm{X}_{i,p})\right)-\frac{1}{2}m_{i}V_{i,p}^{2}-q_{i}{\bm{\mathsf{\text{\vtop{\halign{#\cr\hfil y\hfil\cr\hfil\raise 0.43057pt\hbox{f}\hfil\cr}}}}}}\cdot\tilde{\mathcal{R}}_{3}(S(\bm{X}-\bm{X}_{i,p}))\right],(80)ℒh,f=−12​μ0​(ℂ​𝗔)⋅(ℍ1​ℂ​𝗔).\displaystyle\mathcal{L}_{h,f}=-\frac{1}{2\mu_{0}}(\mathbb{C}{\bm{\mathsf{A}}})\cdot(\mathbb{H}_{1}\mathbb{C}{\bm{\mathsf{A}}}).(81)

In the above equations,NiN_{i}andNeN_{e}are the number of ion and electron particles, respectively. The total Lagrangian is thereforeℒh=ℒh,e+ℒh,i+ℒh,f\mathcal{L}_{h}=\mathcal{L}_{h,e}+\mathcal{L}_{h,i}+\mathcal{L}_{h,f}. We first take the variations with respect to𝑿e,g​c,p\bm{X}_{e,gc,p}andV∥,pV_{\parallel,p}to obtain the discretized Euler-Lagrange equations for the drift-kinetic electrons. After rearranging them, we get the following equations of motion for the drift-kinetic electrons:d​𝑿e,g​c,pd​t\displaystyle\frac{\mathrm{d}\bm{X}_{e,gc,p}}{\mathrm{d}t}=V∥,p​𝑩∗​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p)+𝑬⟂S​(𝑿e,g​c,p)×𝒃e​qB∥∗​(𝑿e,g​c,p)=𝑽e,g​c,p,\displaystyle={V}_{\parallel,p}\frac{\bm{B}^{\ast}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}+\frac{\bm{E}_{\perp}^{S}(\bm{X}_{e,gc,p})\times\bm{b}_{eq}}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}=\bm{V}_{e,gc,p},(82)d​V∥,pd​t\displaystyle\frac{\mathrm{d}{V}_{\parallel,p}}{\mathrm{d}t}=𝑩∗​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p)⋅(qeme​𝑬S​(𝑿e,g​c,p))=qeme​E∥S​(𝑿e,g​c,p).\displaystyle=\frac{\bm{B}^{\ast}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\cdot\left(\frac{q_{e}}{m_{e}}\bm{E}^{S}(\bm{X}_{e,gc,p})\right)=\frac{q_{e}}{m_{e}}E_{\parallel}^{S}(\bm{X}_{e,gc,p}).(83)

The discretized Euler-Lagrange equations for the ion particles, obtained by taking the variations with respect to𝑿i,p\bm{X}_{i,p}and𝑽i,p\bm{V}_{i,p}are given by:d​𝑿i,pd​t\displaystyle\frac{\mathrm{d}\bm{X}_{i,p}}{\mathrm{d}t}=𝑽i,p,\displaystyle=\bm{V}_{i,p},(84)d​𝑽i,pd​t\displaystyle\frac{\mathrm{d}\bm{V}_{i,p}}{\mathrm{d}t}=qimi​(𝑬S​(t,𝑿i,p)+𝑽i,p×𝑩S​(t,𝑿i,p)).\displaystyle=\frac{q_{i}}{m_{i}}\left(\bm{E}^{S}(t,\bm{X}_{i,p})+\bm{V}_{i,p}\times\bm{B}^{S}(t,\bm{X}_{i,p})\right).(85)

In our discrete setting, the electromagnetic fields and the potentials, all defined on the primal grid, are related by:𝗘=−d​𝗔d​t−𝔾​ψφ,𝗕=ℂ​𝗔.{\bm{\mathsf{E}}}=-\frac{\mathop{}\!\mathrm{d}{\bm{\mathsf{A}}}}{\mathop{}\!\mathrm{d}t}-\mathbb{G}{\bm{\mathsf{\text{\vtop{\halign{#\cr\hfil y\hfil\cr\hfil\raise 0.43057pt\hbox{f}\hfil\cr}}}}}},~~~~{\bm{\mathsf{B}}}=\mathbb{C}{\bm{\mathsf{A}}}.(86)

This immediately yields the discrete Faraday equation:d​𝗕d​t+ℂ​𝗘=0.\frac{\mathrm{d}{\bm{\mathsf{B}}}}{\mathrm{d}t}+\mathbb{C}{\bm{\mathsf{E}}}=0.(87)

Similarly, the definition of the magnetic field, coupled with the discretization of the magnetic field on primal grid faces, allows us to write the discretized Gauss law of magnetism:𝔻​𝗕=0.\mathbb{D}{\bm{\mathsf{B}}}=0.(88)

Taking the variations ofℒh\mathcal{L}_{h}with respect to𝗔{\bm{\mathsf{A}}}, we find Ampère’s law:ℂ⊤​ℍ2​𝗕=ℂ⊤​ℍ2​ℂ​𝗔=μ0​(𝗝~i+𝗝~e,g​c),\mathbb{C}^{\top}\mathbb{H}_{2}{\bm{\mathsf{B}}}=\mathbb{C}^{\top}\mathbb{H}_{2}\mathbb{C}{\bm{\mathsf{A}}}=\mu_{0}(\tilde{{\bm{\mathsf{J}}}}_{i}+\tilde{{\bm{\mathsf{J}}}}_{e,gc}),(89)

where the discretized current densities are given by:𝗝~i​(t)\displaystyle\tilde{{\bm{\mathsf{J}}}}_{i}(t)=∑p=1Niwi,p​qi​ℛ~2​(𝑽i,p​(t)​S​(𝑿−𝑿i,p​(t))),\displaystyle=\sum_{p=1}^{N_{i}}w_{i,p}q_{i}\tilde{\mathcal{R}}_{2}\left(\bm{V}_{i,p}(t)S(\bm{X}-\bm{X}_{i,p}(t))\right),(90)𝗝~e,g​c​(t)\displaystyle\tilde{{\bm{\mathsf{J}}}}_{e,gc}(t)=∑p=1Newe,p​qe​ℛ~2​(𝑽e,g​c,p​(t)​S​(𝑿−𝑿e,g​c,p​(t))).\displaystyle=\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{2}\left(\bm{V}_{e,gc,p}(t)S(\bm{X}-\bm{X}_{e,gc,p}(t))\right).(91)

Taking the variations with respect toψφleads to the discretized quasineutrality condition:ϱ~i​(t)+ϱ~e,g​c​(t)=0,\tilde{\bm{\varrho}}_{i}(t)+\tilde{\bm{\varrho}}_{e,gc}(t)=0,(92)

where the discretized charge densities are given by:ϱ~i​(t)\displaystyle\tilde{\bm{\varrho}}_{i}(t)=∑p=1Niwi,pqiℛ~3(S(𝑿−𝑿i,p(t)),\displaystyle=\sum_{p=1}^{N_{i}}w_{i,p}q_{i}\tilde{\mathcal{R}}_{3}\left(S(\bm{X}-\bm{X}_{i,p}(t)\right),(93)ϱ~e,g​c​(t)\displaystyle\tilde{\bm{\varrho}}_{e,gc}(t)=∑p=1Newe,pqeℛ~3(S(𝑿−𝑿e,g​c,p(t)),\displaystyle=\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{3}\left(S(\bm{X}-\bm{X}_{e,gc,p}(t)\right),(94)

Equation (89) has a solution only if the discrete divergence of the current density is 0 i.e.𝔻~​(𝗝~i​(t)+𝗝~e,g​c​(t))=0,\tilde{\mathbb{D}}(\tilde{{\bm{\mathsf{J}}}}_{i}(t)+\tilde{{\bm{\mathsf{J}}}}_{e,gc}(t))=0,(95)

as implied by equation (92).
Just like the continuous counterpart, this condition can be obtained by taking the discrete divergence of equation (89).
While equation (19) is valid at the continuous level for the hybrid quasineutral model, its discrete counterpart equation (92) is not satisfied up to machine precision as per our numerical scheme. On account of the number of particles used being finite, the numerical values of the discrete charge density are polluted by statistical sampling noise, and are therefore not exactly 0 in quasineutral simulations. In typical PIC simulations, this noise and the resultant charge density error decreases as𝒪​(1/Np)\mathcal{O}(1/\sqrt{N_{p}})(birdsall2018plasma). While equation (92) is not enforced, we use the discretized Ampère’s equation (89), which implies equation (95), to obtain𝗘⟂{\bm{\mathsf{E}}}_{\perp}, as explained below in Section5.2.1.

## 5.2Semi-discrete electric field equations

## 5.2.1Equation for𝗘⟂{\bm{\mathsf{E}}}_{\perp}

Substituting (82) into (91) gives us the discretized version of equation (24), given by:𝗝~e,g​c​(t)=∑p=1Newe,p​qe​ℛ~2​((V∥,p​𝑩∗​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p)+𝑬⟂S​(𝑿e,g​c,p)×𝒃e​qB∥∗​(𝑿e,g​c,p))​S​(𝑿−𝑿e,g​c,p​(t))).\tilde{{\bm{\mathsf{J}}}}_{e,gc}(t)=\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{2}\left(\left({V}_{\parallel,p}\frac{\bm{B}^{\ast}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}+\frac{\bm{E}_{\perp}^{S}(\bm{X}_{e,gc,p})\times\bm{b}_{eq}}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\right)S(\bm{X}-\bm{X}_{e,gc,p}(t))\right).(96)

Substituting the above equation in equation (89) gives us an asymmetric linear system that is computationally difficult to solve. An alternative approach would be to solve a discretized approximation of (26) given by:μ0​∑p=1Newe,p​qe​ℛ~2​(1B∥∗​(𝑿e,g​c,p)​(𝑬⟂S​(𝑿e,g​c,p))​S​(𝑿−𝑿e,g​c,p​(t)))=ℬe​q×[ℂ⊤​ℍ2​𝗕−μ0​𝗝~i−μ0​∑p=1Newe,p​qe​ℛ~2​(V∥,p​𝑩∗​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p)​S​(𝑿−𝑿e,g​c,p​(t)))].\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{2}\left(\frac{1}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\left(\bm{E}_{\perp}^{S}(\bm{X}_{e,gc,p})\right)S(\bm{X}-\bm{X}_{e,gc,p}(t))\right)\\
=\mathcal{B}_{eq}\times\left[\mathbb{C}^{\top}\mathbb{H}_{2}{\bm{\mathsf{B}}}-\mu_{0}\tilde{{\bm{\mathsf{J}}}}_{i}-\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{2}\left(V_{\parallel,p}\frac{\bm{B}^{\ast}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}S(\bm{X}-\bm{X}_{e,gc,p}(t))\right)\right].(97)

Here,ℬe​q×\mathcal{B}_{eq}\timesis an operator that is needed because the terms inside the large square brackets on the right hand side are not on the same discretized spaces as the term on the left hand side. This happens due to the design of the mimetic finite difference discretization used here. This operator performs a face-to-face projection accounting for the scaling between different dual face spaces and the appropriate signs according to the rules of the cross product operation. Equation (97) is a large, sparse linear system that can be solved to obtain𝗘{\bm{\mathsf{E}}}. The left-hand side of equation (97) is a large, sparse particle ‘mass’ matrix that can be approximated as:∑p=1Newe,p​qe​ℛ~2​(1B∥∗​(𝑿e,g​c,p)​(𝑬⟂S​(𝑿e,g​c,p))​S​(𝑿−𝑿e,g​c,p​(t)))≈ρ¯e,g​cB∥∗¯​𝗘⟂,\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{2}\left(\frac{1}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\left(\bm{E}_{\perp}^{S}(\bm{X}_{e,gc,p})\right)S(\bm{X}-\bm{X}_{e,gc,p}(t))\right)\approx\frac{\bar{\rho}_{e,gc}}{\bar{B_{\parallel}^{\ast}}}{\bm{\mathsf{E}}}_{\perp},(98)

whereρ¯e,g​c\bar{\rho}_{e,gc}andB∥∗¯\bar{B_{\parallel}^{\ast}}can be found with appropriate interpolations. Such an approximation provides us𝗘{\bm{\mathsf{E}}}in straightforward manner, circumventing the computational cost of looping over each particle and the need to solve a linear system.

## 5.2.2Equation forE∥E_{\parallel}

Taking the time derivative of (89) and substitutingd​𝗕d​t\frac{\mathrm{d}{\bm{\mathsf{B}}}}{\mathrm{d}t}(87), we get:ℂ⊤​ℍ2​ℂ​𝗘=−μ0​(d​𝗝~id​t+d​𝗝~e,g​cd​t).\mathbb{C}^{\top}\mathbb{H}_{2}\mathbb{C}{\bm{\mathsf{E}}}=-\mu_{0}\left(\frac{\mathrm{d}\tilde{{\bm{\mathsf{J}}}}_{i}}{\mathrm{d}t}+\frac{\mathrm{d}\tilde{{\bm{\mathsf{J}}}}_{e,gc}}{\mathrm{d}t}\right).(99)

Once we have𝗘⟂{\bm{\mathsf{E}}}_{\perp}from the solution of (97), we only need to solve the∥−\parallel-component of equation (99) to obtainE∥E_{\parallel}. The curl-curl operator above can also be written as:(ℂ⊤​ℍ2​ℂ)=ℍ1​𝔾​ℍ~3​𝔻~​ℍ1−𝕃,(\mathbb{C}^{\top}\mathbb{H}_{2}\mathbb{C})=\mathbb{H}_{1}\mathbb{G}\tilde{\mathbb{H}}_{3}\tilde{\mathbb{D}}\mathbb{H}_{1}-\mathbb{L},(100)

where𝕃\mathbb{L}is the Laplacian operator. The∥−\parallel-component ofℂ⊤​ℍ2​ℂ​𝗘\mathbb{C}^{\top}\mathbb{H}_{2}\mathbb{C}{\bm{\mathsf{E}}}is given by:(ℂ⊤​ℍ2​ℂ​𝗘)∥=ℍ1​𝔾∥​ℍ~3​𝔻~⟂​ℍ1​𝗘⟂−𝕃⟂​𝗘∥.(\mathbb{C}^{\top}\mathbb{H}_{2}\mathbb{C}{\bm{\mathsf{E}}})_{\parallel}=\mathbb{H}_{1}\mathbb{G}_{\parallel}\tilde{\mathbb{H}}_{3}\tilde{\mathbb{D}}_{\perp}\mathbb{H}_{1}{\bm{\mathsf{E}}}_{\perp}-\mathbb{L}_{\perp}{\bm{\mathsf{E}}}_{\parallel}.(101)

This relation helps break down(ℂ⊤​ℍ2​ℂ​𝗘)∥(\mathbb{C}^{\top}\mathbb{H}_{2}\mathbb{C}{\bm{\mathsf{E}}})_{\parallel}into the individual contributions of𝗘∥{\bm{\mathsf{E}}}_{\parallel}and𝗘⟂{\bm{\mathsf{E}}}_{\perp}. Taking the time derivative of (90) and using the equations (84) and (85), we get:d​𝗝~id​t=∑p=1Niqi​wi,p​ℛ~2​(d​𝑽i,pd​t​S​(𝑿−𝑿i,p​(t))−𝑽i,p​d​𝑿i,pd​t⋅∇S​(𝑿−𝑿i,p​(t)))\displaystyle\frac{\mathrm{d}\tilde{{\bm{\mathsf{J}}}}_{i}}{\mathrm{d}t}=\sum_{p=1}^{N_{i}}q_{i}w_{i,p}\tilde{\mathcal{R}}_{2}\left(\frac{\mathrm{d}\bm{V}_{i,p}}{\mathrm{d}t}S(\bm{X}-\bm{X}_{i,p}(t))-\bm{V}_{i,p}\frac{\mathrm{d}\bm{X}_{i,p}}{\mathrm{d}t}\cdot\nabla S(\bm{X}-\bm{X}_{i,p}(t))\right)=∑p=1Niwi,p​ℛ~2​(qi2mi​(𝑬S​(t,𝑿i,p)+𝑽i,p×𝑩S​(t,𝑿i,p))​S​(𝑿−𝑿i,p​(t))−qi​𝑽i,p​𝑽i,p⋅∇S​(𝑿−𝑿i,p​(t))).\displaystyle=\sum_{p=1}^{N_{i}}w_{i,p}\tilde{\mathcal{R}}_{2}\left(\frac{q_{i}^{2}}{m_{i}}(\bm{E}^{S}(t,\bm{X}_{i,p})+\bm{V}_{i,p}\times\bm{B}^{S}(t,\bm{X}_{i,p}))S(\bm{X}-\bm{X}_{i,p}(t))-q_{i}\bm{V}_{i,p}\bm{V}_{i,p}\cdot\nabla S(\bm{X}-\bm{X}_{i,p}(t))\right).(102)

To obtain the∥−\parallel-component ofd​𝗝~e,g​cd​t\frac{\mathrm{d}\tilde{{\bm{\mathsf{J}}}}_{e,gc}}{\mathrm{d}t}, we take the time derivative of (91) and use the relations in equations (82) and (83). We get:d​J~e,gc∥d​t=∑p=1Neqe​we,p​ℛ~2​(d​V∥,pd​t​S​(𝑿−𝑿e,g​c,p)−V∥,p​d​𝑿e,g​c,pd​t⋅∇S​(𝑿−𝑿e,g​c,p))\displaystyle\frac{\mathrm{d}\tilde{J}_{e,gc\parallel}}{\mathrm{d}t}=\sum_{p=1}^{N_{e}}q_{e}w_{e,p}\tilde{\mathcal{R}}_{2}\left(\frac{\mathrm{d}{V}_{\parallel,p}}{\mathrm{d}t}S(\bm{X}-\bm{X}_{e,gc,p})-{V}_{\parallel,p}\frac{\mathrm{d}\bm{X}_{e,gc,p}}{\mathrm{d}t}\cdot\nabla S(\bm{X}-\bm{X}_{e,gc,p})\right)=∑p=1Newe,p​ℛ~2​(qe2me​E∥S​(𝑿e,g​c,p)​S​(𝑿−𝑿e,g​c,p))\displaystyle=\sum_{p=1}^{N_{e}}w_{e,p}\tilde{\mathcal{R}}_{2}\left(\frac{q_{e}^{2}}{m_{e}}E_{\parallel}^{S}(\bm{X}_{e,gc,p})S(\bm{X}-\bm{X}_{e,gc,p})\right)−∑p=1Newe,p​ℛ~2​(qe​V∥,p​(V∥,p​𝑩∗​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p)+𝑬⟂S​(𝑿e,g​c,p)×𝒃e​qB∥∗​(𝑿e,g​c,p))⋅∇S​(𝑿−𝑿e,g​c,p)).\displaystyle-\sum_{p=1}^{N_{e}}w_{e,p}\tilde{\mathcal{R}}_{2}\left(q_{e}{V}_{\parallel,p}\left({V}_{\parallel,p}\frac{\bm{B}^{\ast}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}+\frac{\bm{E}_{\perp}^{S}(\bm{X}_{e,gc,p})\times\bm{b}_{eq}}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\right)\cdot\nabla S(\bm{X}-\bm{X}_{e,gc,p})\right).(103)

Using equations (101) (102) and (103), the∥−\parallel-component of equation (99) becomes:−𝕃⟂​𝗘∥+μ0​∑p=1Niwi,p​ℛ~2​(qi2mi​𝑬∥S​(t,𝑿i,p)​S​(𝑿−𝑿i,p))+μ0​∑p=1Newe,p​ℛ~2​(qe2me​𝑬∥S​(𝑿e,g​c,p)​S​(𝑿−𝑿e,g​c,p))\displaystyle-\mathbb{L}_{\perp}{\bm{\mathsf{E}}}_{\parallel}+\mu_{0}\sum_{p=1}^{N_{i}}w_{i,p}\tilde{\mathcal{R}}_{2}\left(\frac{q_{i}^{2}}{m_{i}}\bm{E}_{\parallel}^{S}(t,\bm{X}_{i,p})S(\bm{X}-\bm{X}_{i,p})\right)+\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}\tilde{\mathcal{R}}_{2}\left(\frac{q_{e}^{2}}{m_{e}}\bm{E}_{\parallel}^{S}(\bm{X}_{e,gc,p})S(\bm{X}-\bm{X}_{e,gc,p})\right)=μ0​∑p=1Niwi,p​ℛ~2​(−𝑽i,p×𝑩S​(t,𝑿i,p)​S​(𝑿−𝑿i,p)+qi​𝑽i,p​𝑽i,p⋅∇S​(𝑿−𝑿i,p))∥\displaystyle=\mu_{0}\sum_{p=1}^{N_{i}}w_{i,p}\tilde{\mathcal{R}}_{2}\left(-\bm{V}_{i,p}\times\bm{B}^{S}(t,\bm{X}_{i,p})S(\bm{X}-\bm{X}_{i,p})+q_{i}\bm{V}_{i,p}\bm{V}_{i,p}\cdot\nabla S(\bm{X}-\bm{X}_{i,p})\right)_{\parallel}+μ0​∑p=1Newe,p​ℛ~2​(qe​V∥,p2​𝑩∗​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p)⋅∇S​(𝑿−𝑿e,g​c,p))\displaystyle+\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}\tilde{\mathcal{R}}_{2}\left(q_{e}{V}_{\parallel,p}^{2}\frac{\bm{B}^{\ast}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\cdot\nabla S(\bm{X}-\bm{X}_{e,gc,p})\right)+μ0​∑p=1Newe,p​ℛ~2​(qe​V∥,p​(𝑬⟂S​(𝑿e,g​c,p)×𝒃e​qB∥∗​(𝑿e,g​c,p))⋅∇S​(𝑿−𝑿e,g​c,p))\displaystyle+\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}\tilde{\mathcal{R}}_{2}\left(q_{e}{V}_{\parallel,p}\left(\frac{\bm{E}_{\perp}^{S}(\bm{X}_{e,gc,p})\times\bm{b}_{eq}}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\right)\cdot\nabla S(\bm{X}-\bm{X}_{e,gc,p})\right)−μ0​∑p=1Newe,p​ℛ~2​(𝑩∗​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p)⋅(qe2me​𝑬⟂S​(𝑿e,g​c,p))​S​(𝑿−𝑿e,g​c,p))−ℍ1​𝔾∥​ℍ~3​𝔻~⟂​ℍ1​𝗘⟂.\displaystyle-\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}\tilde{\mathcal{R}}_{2}\left(\frac{\bm{B}^{\ast}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\cdot\left(\frac{q_{e}^{2}}{m_{e}}\bm{E}_{\perp}^{S}(\bm{X}_{e,gc,p})\right)S(\bm{X}-\bm{X}_{e,gc,p})\right)-\mathbb{H}_{1}\mathbb{G}_{\parallel}\tilde{\mathbb{H}}_{3}\tilde{\mathbb{D}}_{\perp}\mathbb{H}_{1}{\bm{\mathsf{E}}}_{\perp}.(104)

Equation (104) is a large, sparse linear system that is solved to obtain𝗘∥{\bm{\mathsf{E}}}_{\parallel}. This is the discretized version of equation (39). Similar to the equation for𝗘⟂{\bm{\mathsf{E}}}_{\perp}, the second and third terms of equation (104) are also particle ‘mass’ matrices that can be approximated as:∑p=1Niwi,p​ℛ~2​(qi2mi​𝑬∥S​(t,𝑿i,p)​S​(𝑿−𝑿i,p))\displaystyle\sum_{p=1}^{N_{i}}w_{i,p}\tilde{\mathcal{R}}_{2}\left(\frac{q_{i}^{2}}{m_{i}}\bm{E}_{\parallel}^{S}(t,\bm{X}_{i,p})S(\bm{X}-\bm{X}_{i,p})\right)≈qi​ρ¯imi​B∥∗¯​𝗘∥,\displaystyle\approx\frac{q_{i}\bar{\rho}_{i}}{m_{i}\bar{B_{\parallel}^{\ast}}}{\bm{\mathsf{E}}}_{\parallel},(105)∑p=1Newe,p​ℛ~2​(qe2me​𝑬∥S​(𝑿e,g​c,p)​S​(𝑿−𝑿e,g​c,p))\displaystyle\sum_{p=1}^{N_{e}}w_{e,p}\tilde{\mathcal{R}}_{2}\left(\frac{q_{e}^{2}}{m_{e}}\bm{E}_{\parallel}^{S}(\bm{X}_{e,gc,p})S(\bm{X}-\bm{X}_{e,gc,p})\right)≈qe​ρ¯e,g​cme​B∥∗¯​𝗘∥,\displaystyle\approx\frac{q_{e}\bar{\rho}_{e,gc}}{m_{e}\bar{B_{\parallel}^{\ast}}}{\bm{\mathsf{E}}}_{\parallel},(106)

reducing the computational cost of building the particle-based matrix.

## 6Cold plasma stability analysis of hybrid quasineutral model

In this section, we obtain a time-step criterion for stability of the numerical time-stepping algorithm. A linear stability analysis is performed using the simplified 1D cold plasma model. We first obtain a maximum time-step for the fully explicit RK scheme, and then for the implicit-explicit (IMEX) schemes.

## 6.1Linearization of the 1D model

We consider linear perturbations to the equilibrium state in the cold plasma limit of the hybrid quasineutral model considered here. We assume the equilibrium magnetic field to be in thez−z-direction i.e.𝒃e​q=z^\bm{b}_{eq}=\hat{z}. We also assume all gradients in thexxandyydirections to be zero. The linear perturbations applied are of the form:𝑬1=𝑬^​ei​(k​z−ω​t).\bm{E}_{1}=\hat{\bm{E}}e^{i(kz-\omega t)}.(107)

Linearizing (29) in this manner gives the following equations for the individual components of∂𝑱i,1∂t\frac{\partial\bm{J}_{i,1}}{\partial t}:∂Ji,x,1∂t\displaystyle\frac{\partial J_{i,x,1}}{\partial t}=ϵ0​ωp,i2​Ex,1+Ωc,i​Ji,y,1,\displaystyle=\epsilon_{0}\omega_{p,i}^{2}E_{x,1}+\Omega_{c,i}J_{i,y,1},(108)∂Ji,y,1∂t\displaystyle\frac{\partial J_{i,y,1}}{\partial t}=ϵ0​ωp,i2​Ey,1−Ωc,i​Ji,x,1,\displaystyle=\epsilon_{0}\omega_{p,i}^{2}E_{y,1}-\Omega_{c,i}J_{i,x,1},(109)∂Ji,z,1∂t\displaystyle\frac{\partial J_{i,z,1}}{\partial t}=ϵ0​ωp,i2​Ez,1.\displaystyle=\epsilon_{0}\omega_{p,i}^{2}E_{z,1}.(110)

Linearizing equation (24) using equation (10) similarly gives us:Je,x,1\displaystyle J_{e,x,1}=ϵ0​ωp,e2Ωc,e​Ey,1\displaystyle=\epsilon_{0}\frac{\omega_{p,e}^{2}}{\Omega_{c,e}}E_{y,1}(111)Je,y,1\displaystyle J_{e,y,1}=−ϵ0​ωp,e2Ωc,e​Ex,1\displaystyle=-\epsilon_{0}\frac{\omega_{p,e}^{2}}{\Omega_{c,e}}E_{x,1}(112)∂Je,z,1∂t\displaystyle\frac{\partial J_{e,z,1}}{\partial t}=ϵ0​ωp,e2​Ez,1.\displaystyle=\epsilon_{0}\omega_{p,e}^{2}E_{z,1}.(113)

In the above equations, the termsωp,i\omega_{p,i}andωp,e\omega_{p,e}are the ion and electron plasma frequency, respectively. The termsΩc,i\Omega_{c,i}andΩc,e\Omega_{c,e}are the ion and electron cyclotron frequency, respectively. These frequencies are given by:ωp,i=Zi2​ni​e2ϵ0​mi,ωp,e=ne​e2ϵ0​me,\omega_{p,i}=\sqrt{\frac{Z_{i}^{2}n_{i}e^{2}}{\epsilon_{0}m_{i}}},~~~~\omega_{p,e}=\sqrt{\frac{n_{e}e^{2}}{\epsilon_{0}m_{e}}},(114)

andΩc,i=e​Zi​Be​qmi,Ωc,e=−e​Be​qme,\Omega_{c,i}=\frac{eZ_{i}B_{eq}}{m_{i}},~~~~\Omega_{c,e}=-\frac{eB_{eq}}{m_{e}},(115)

whereZiZ_{i}is the ion atomic number,eeis the electronic charge, andBe​qB_{eq}is the magnetic field magnitude. Note that the electron cyclotron frequency,Ωc,e\Omega_{c,e}, is taken to be negative. The termsnin_{i}andnen_{e}are the ion and electron particle number density, respectively. Similarly,mim_{i}andmem_{e}denote the respective particle masses.

We next consider the linearization of the 1D Maxwell equations. Accordingly, equations (16) and (22) become:c2​∂By,1∂z=−1ϵ0​(Ji,x,1+Je,x,1),\displaystyle c^{2}\frac{\partial B_{y,1}}{\partial z}=-\frac{1}{\epsilon_{0}}(J_{i,x,1}+J_{e,x,1}),(116)c2​∂Bx,1∂z=1ϵ0​(Ji,y,1+Je,y,1),\displaystyle c^{2}\frac{\partial B_{x,1}}{\partial z}=\frac{1}{\epsilon_{0}}(J_{i,y,1}+J_{e,y,1}),(117)(Ji,z,1+Je,z,1)=0,\displaystyle(J_{i,z,1}+J_{e,z,1})=0,(118)∂Bx,1∂t=∂Ey,1∂z,\displaystyle\frac{\partial B_{x,1}}{\partial t}=\frac{\partial E_{y,1}}{\partial z},(119)∂By,1∂t=−∂Ex,1∂z,\displaystyle\frac{\partial B_{y,1}}{\partial t}=-\frac{\partial E_{x,1}}{\partial z},(120)∂Bz,1∂t=0.\displaystyle\frac{\partial B_{z,1}}{\partial t}=0.(121)

From equation (121), we see thatBz,1B_{z,1}is constant. From equations (110), (113) and (118), we see thatEz,1=0E_{z,1}=0, andJi,z,1J_{i,z,1}andJe,z,1J_{e,z,1}are constants. From equations (111) and (112) we see that the electron current componentsJe,x,1J_{e,x,1}andJe,y,1J_{e,y,1}can be directly written as constant multiples ofEy,1E_{y,1}andEx,1E_{x,1}and can therefore be eliminated from the rest of the system. The unknowns that finally remain are thereforeEx,1E_{x,1},Ey,1E_{y,1},Bx,1B_{x,1},By,1B_{y,1},Ji,x,1J_{i,x,1}andJi,y,1J_{i,y,1}. The six coupled equations that govern their evolution are equations (108), (109), (116), (117), (119) and (120). For the space discretization of these six unknowns, we use a staggered centered scheme for thez−z-derivatives, wherein the electric field components are centered at the vertices of the grid, while the current densities and magnetic field components are located at the cell centers of the grid. This is also consistent with the structure-preserving discretization of our numerical model. Consider a 1D periodic grid withNNcells and vertices. Note that the last vertex on the right is not used as it corresponds to the first on the left due to periodicity. We then stack the six variablesEx,1E_{x,1},Ey,1E_{y,1},Bx,1B_{x,1},By,1B_{y,1},Ji,x,1J_{i,x,1}andJi,y,1J_{i,y,1}from all cells into a vectorUUof length 6NN.
This yields a semi-discrete system of the form:d​Ud​t=A​U,\frac{\mathrm{d}U}{\mathrm{d}t}=AU,(122)

whereAAis a6​N×6​N6N\times 6Nskew-symmetric real matrix due to the centered space discretization. This implies that all its eigenvaluesλ=−i​ω\lambda=-i\omegaare purely imaginary. We solve the semi-discrete system with a Runge-Kutta (RK) method. It is well known, that first and second order RK methods are not stable for imaginary eigenvalues, whereas RK3 is stable for imaginary eigenvalues provided|λ|≤3|\lambda|\leq\sqrt{3}and RK4 provided|λ|≤2​2|\lambda|\leq 2\sqrt{2}.

Rather than computing the eigenvalues of the6​N×6​N6N\times 6NmatrixAA, we can derive the corresponding numerical dispersion relation by performing a discrete Fourier transform in space. Let us denoteΔ​z=L/N\Delta z=L/Nas the grid spacing, andkkas the wavenumber, wherek=2​π​jN​Δ​zk=\frac{2\pi j}{N\Delta z},j=0,1,…,N−1j=0,1,\ldots,N-1. This corresponds to the discrete Fourier modes of the periodic grid. The discrete Fourier transform of the centered finite difference operator for thez−z-derivative is given by:∂∂z→i​k​sinc​(k​Δ​z2),\frac{\partial}{\partial z}\rightarrow\mathop{}\!\mathrm{i}k\mathop{}\!\mathrm{sinc}\left(\frac{k\Delta z}{2}\right),(123)

wheresinc​(x)=sin⁡(x)x\mathop{}\!\mathrm{sinc}(x)=\frac{\sin(x)}{x}and the second derivative operator by:∂2∂z2→−k2​sinc2​(k​Δ​z2).\frac{\partial^{2}}{\partial z^{2}}\rightarrow-k^{2}\mathop{}\!\mathrm{sinc}^{2}\left(\frac{k\Delta z}{2}\right).(124)

We observe that this is identical to the continuous withkkreplaced byk​sinc​(k​Δ​z2)k\mathop{}\!\mathrm{sinc}\left(\frac{k\Delta z}{2}\right), which is the modified wavenumber due to the space discretization. The maximum
modified wavenumber iskeff,max=2Δ​zk_{\text{eff,max}}=\frac{2}{\Delta z}at the Nyquist pointk=πΔ​zk=\frac{\pi}{\Delta z}.

## 6.2Numerical dispersion relation

In order to compute the numerical dispersion relation for this system, we replace∂/∂t\partial/\partial twith−i​ω-i\omega. Initially, we replace∂/∂z\partial/\partial zwithi​kikfor simplicity. Later, when we obtain the final equation, we can replacekkwithk​sinc​(k​Δ​z/2)k\mathop{}\!\mathrm{sinc}(k\Delta z/2)to account for the space discretization and obtain the time-stepping criterion. We first use equations (111) and (112) to writeJe,x,1J_{e,x,1}andJe,y,1J_{e,y,1}in terms ofEx,1E_{x,1}andEy,1E_{y,1}in equations (116) and (117). Then using the newly obtained expressions forEx,1E_{x,1}andEy,1E_{y,1}from (116) and (117) in equations (119) and (120), we get:d​B^x,kd​t\displaystyle\frac{\mathrm{d}\hat{B}_{x,k}}{\mathrm{d}t}=Ωc,eωp,e2​(c2​k2​B^y,k−i​kϵ0​J^i,x,k),\displaystyle=\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\left(c^{2}k^{2}\hat{B}_{y,k}-\frac{ik}{\epsilon_{0}}\hat{J}_{i,x,k}\right),(125)d​B^y,kd​t\displaystyle\frac{\mathrm{d}\hat{B}_{y,k}}{\mathrm{d}t}=−Ωc,eωp,e2​(c2​k2​B^x,k+i​kϵ0​J^i,y,k).\displaystyle=-\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\left(c^{2}k^{2}\hat{B}_{x,k}+\frac{ik}{\epsilon_{0}}\hat{J}_{i,y,k}\right).(126)

Next, we use equations (111) and (112) to writeEx,1E_{x,1}andEy,1E_{y,1}in terms ofJe,x,1J_{e,x,1}andJe,y,1J_{e,y,1}in equations (108) and (109). Observing thatΩc,e/ωp,e2=−Ωc,i/ωp,i2{\Omega_{c,e}}/{\omega_{p,e}^{2}}=-{\Omega_{c,i}}/{\omega_{p,i}^{2}}for singly charged ions, we can directly substitute equations (116) and (117) into equations (108) and (109) to obtain:1ϵ0​d​J^i,x,kd​t\displaystyle\frac{1}{\epsilon_{0}}\frac{\mathrm{d}\hat{J}_{i,x,k}}{\mathrm{d}t}=−i​k​Ωc,eωp,e2​ωp,i2​c2​B^x,k,\displaystyle=-ik\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\omega_{p,i}^{2}c^{2}\hat{B}_{x,k},(127)1ϵ0​d​J^i,y,kd​t\displaystyle\frac{1}{\epsilon_{0}}\frac{\mathrm{d}\hat{J}_{i,y,k}}{\mathrm{d}t}=−i​k​Ωc,eωp,e2​ωp,i2​c2​B^y,k.\displaystyle=-ik\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\omega_{p,i}^{2}c^{2}\hat{B}_{y,k}.(128)

Now, replacing∂/∂t\partial/\partial twith−i​ω-i\omega, equations (125)–(128) become:−i​ω​B^x,k\displaystyle-i\omega\hat{B}_{x,k}=Ωc,eωp,e2​(c2​k2​B^y,k−i​kϵ0​J^i,x,k),\displaystyle=\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\left(c^{2}k^{2}\hat{B}_{y,k}-\frac{ik}{\epsilon_{0}}\hat{J}_{i,x,k}\right),(129)−i​ω​B^y,k\displaystyle-i\omega\hat{B}_{y,k}=−Ωc,eωp,e2​(c2​k2​B^x,k+i​kϵ0​J^i,y,k),\displaystyle=-\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\left(c^{2}k^{2}\hat{B}_{x,k}+\frac{ik}{\epsilon_{0}}\hat{J}_{i,y,k}\right),(130)−i​ωϵ0​J^i,x,k\displaystyle-\frac{i\omega}{\epsilon_{0}}\hat{J}_{i,x,k}=−i​k​Ωc,eωp,e2​ωp,i2​c2​B^x,k,\displaystyle=-ik\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\omega_{p,i}^{2}c^{2}\hat{B}_{x,k},(131)−i​ωϵ0​J^i,y,k\displaystyle-\frac{i\omega}{\epsilon_{0}}\hat{J}_{i,y,k}=−i​k​Ωc,eωp,e2​ωp,i2​c2​B^y,k.\displaystyle=-ik\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\omega_{p,i}^{2}c^{2}\hat{B}_{y,k}.(132)

After algebraically manipulating equations (129), (130), (131) and (132), we obtain the following dispersion relation:ω−Ωc,e2ωp,e4​ωp,i2​c2​k2ω=±Ωc,eωp,e2​c2​k2.\omega-\frac{\Omega_{c,e}^{2}}{\omega_{p,e}^{4}\omega_{p,i}^{2}}\frac{c^{2}k^{2}}{\omega}=\pm\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}c^{2}k^{2}.(133)

This is a quadratic equation inω\omega, whose two solutions are given by:ω1\displaystyle\omega_{1}=|Ωc,e|​c​k2​ωp,e2​(c​k+c2​k2+4​ωp,i2),\displaystyle=\frac{|\Omega_{c,e}|ck}{2\omega_{p,e}^{2}}\left(ck+\sqrt{c^{2}k^{2}+4\omega_{p,i}^{2}}\right),(134)ω2\displaystyle\omega_{2}=|Ωc,e|​c​k2​ωp,e2​(−c​k+c2​k2+4​ωp,i2).\displaystyle=\frac{|\Omega_{c,e}|ck}{2\omega_{p,e}^{2}}\left(-ck+\sqrt{c^{2}k^{2}+4\omega_{p,i}^{2}}\right).(135)

We observe that fork→0k\to 0, the solutions become:ω1\displaystyle\omega_{1}≈|Ωc,e|​ωp,iωp,e2​c​k=VA,i​k,\displaystyle\approx\frac{|\Omega_{c,e}|\omega_{p,i}}{\omega_{p,e}^{2}}ck=V_{A,i}k,(136)ω2\displaystyle\omega_{2}≈|Ωc,e|​ωp,iωp,e2​c​k=VA,i​k,\displaystyle\approx\frac{|\Omega_{c,e}|\omega_{p,i}}{\omega_{p,e}^{2}}ck=V_{A,i}k,(137)

whereVA,iV_{A,i}is the ion Alfvén speed. We see that ask→0k\rightarrow 0, both modes have the same leading-order frequency and the same group velocity. On the other hand, fork→∞k\to\infty:ω1\displaystyle\omega_{1}≈|Ωc,e|ωp,e2​c2​k2,\displaystyle\approx\frac{|\Omega_{c,e}|}{\omega_{p,e}^{2}}c^{2}k^{2},(138)ω2\displaystyle\omega_{2}→|Ωc,e|​ωp,i2ωp,e2=Ωc,i.\displaystyle\to\frac{|\Omega_{c,e}|\omega_{p,i}^{2}}{\omega_{p,e}^{2}}{=\Omega_{c,i}}.(139)

Now, replacingkkbyk​sinc​(k​Δ​z2)k\mathop{}\!\mathrm{sinc}\left(\frac{k\Delta z}{2}\right)to account for the space discretization, we observe thatω1\omega_{1}is unbounded whenk→∞k\to\infty, whereasω2\omega_{2}remains bounded. This implies that the eigenvaluesλ1=−i​ω1\lambda_{1}=-\mathop{}\!\mathrm{i}\omega_{1}will be the largest for the smallestΔ​z\Delta zor the largest value ofkki.e.keff,maxk_{\text{eff,max}}, and will determine the stability condition of the time integrator. Using RK4, we thus need:|λ1​Δ​t|=|ω1|​Δ​t≤2​2,|\lambda_{1}\Delta t|=|\omega_{1}|\Delta t\leq 2\sqrt{2},(140)

and using the expression ofω1\omega_{1}for largekk, we obtain
the following stability condition:Δ​t≤22​ωp,e2c2​|Ωc,e|​Δ​z2.\Delta t\leq\frac{\sqrt{2}}{2}\frac{\omega_{p,e}^{2}}{c^{2}|\Omega_{c,e}|}\Delta z^{2}.(141)

This shows that the time-step scales asΔ​z2\Delta z^{2}for the hybrid drift-kinetic quasineutral model when using only explicit time-stepping schemes.

## 6.3A splitting scheme to lower the stability restriction

The above stability condition can be very restrictive for smallΔ​z\Delta z. To alleviate this restriction, we can use a splitting scheme where we treat the stiff part of the system involving the highest frequencies implicitly, and the rest explicitly. The stiff part corresponds to the terms involving the second derivatives inzzin equations (125)–(128).

The split system reads:d​B^x,kd​t\displaystyle\frac{\mathrm{d}\hat{B}_{x,k}}{\mathrm{d}t}=−i​kϵ0​Ωc,eωp,e2​J^i,x,k,\displaystyle=-\frac{ik}{\epsilon_{0}}\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\hat{J}_{i,x,k},(142)d​B^y,kd​t\displaystyle\frac{\mathrm{d}\hat{B}_{y,k}}{\mathrm{d}t}=−i​kϵ0​Ωc,eωp,e2​J^i,y,k,\displaystyle=-\frac{ik}{\epsilon_{0}}\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\hat{J}_{i,y,k},(143)1ϵ0​d​J^i,x,kd​t\displaystyle\frac{1}{\epsilon_{0}}\frac{\mathrm{d}\hat{J}_{i,x,k}}{\mathrm{d}t}=−i​k​Ωc,eωp,e2​ωp,i2​c2​B^x,k,\displaystyle=-ik\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\omega_{p,i}^{2}c^{2}\hat{B}_{x,k},(144)1ϵ0​d​J^i,y,kd​t\displaystyle\frac{1}{\epsilon_{0}}\frac{\mathrm{d}\hat{J}_{i,y,k}}{\mathrm{d}t}=−i​k​Ωc,eωp,e2​ωp,i2​c2​B^y,k.\displaystyle=-ik\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}\omega_{p,i}^{2}c^{2}\hat{B}_{y,k}.(145)

for the non-stiff part, and for the stiff part:d​B^x,kd​t\displaystyle\frac{\mathrm{d}\hat{B}_{x,k}}{\mathrm{d}t}=Ωc,eωp,e2​c2​k2​B^y,k,\displaystyle=\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}c^{2}k^{2}\hat{B}_{y,k},(146)d​B^y,kd​t\displaystyle\frac{\mathrm{d}\hat{B}_{y,k}}{\mathrm{d}t}=−Ωc,eωp,e2​c2​k2​B^x,k,\displaystyle=-\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}c^{2}k^{2}\hat{B}_{x,k},(147)1ϵ0​d​J^i,x,kd​t\displaystyle\frac{1}{\epsilon_{0}}\frac{\mathrm{d}\hat{J}_{i,x,k}}{\mathrm{d}t}=0,\displaystyle=0,(148)1ϵ0​d​J^i,y,kd​t\displaystyle\frac{1}{\epsilon_{0}}\frac{\mathrm{d}\hat{J}_{i,y,k}}{\mathrm{d}t}=0.\displaystyle=0.(149)

The dispersion relation of the implicit part can be derived similarly as before, yielding the following eigenvalues:λ=±i​Ωc,eωp,e2​c2​k2.\lambda=\pm\mathop{}\!\mathrm{i}\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}c^{2}k^{2}.(150)

These eigenvalues are purely imaginary, and thus can be treated stably with an implicit time integrator without time-step restriction. The Crank-Nicolson (CN) method can be used here to maintain the energy conservation of the semi-discrete system. The explicit part has the following dispersion relation:ω2=Ωc,e2ωp,e4​ωp​i2​c2​k2,\omega^{2}=\frac{\Omega_{c,e}^{2}}{\omega_{p,e}^{4}}\omega_{pi}^{2}c^{2}k^{2},(151)

yielding the eigenvaluesλ=±i​Ωc,eωp,e2​ωp,i​c​k.\lambda=\pm i\frac{\Omega_{c,e}}{\omega_{p,e}^{2}}{\omega_{p,i}}ck.(152)

Here again in the discrete casekkis replaced byk​sinc​(k​Δ​z2)k\mathop{}\!\mathrm{sinc}\left(\frac{k\Delta z}{2}\right)and thus the time-step restriction for the explicit part, with a 4th order RK method, is now:Δ​t≤2c​ωp,e2|Ωc,e|​ωp,i​Δ​z,\Delta t\leq\frac{\sqrt{2}}{c}\frac{\omega_{p,e}^{2}}{|\Omega_{c,e}|\omega_{p,i}}\Delta z,(153)

which scales asΔ​z\Delta zinstead ofΔ​z2\Delta z^{2}as before, thus significantly alleviating the time-step restriction for smallΔ​z\Delta z. Using this idea, we develop two implicit-explicit (IMEX) time-stepping schemes, wherein the explicit terms are advanced in time using a 4th order low-storage Runge-Kutta (LSRK) scheme, whereas the stiff, implicit terms are advanced using the CN method. The first IMEX scheme, performs a half-step CN advance of the implicit terms, followed by a full-step RK advance of the explicit terms, and finally another half-step CN advance of the implicit terms. This scheme is labelled ‘CN-RK-CN’ for convenience. In the second IMEX scheme, labelled ‘RK-CN-RK’, this order is flipped, applying first a half-step RK advance of explicit terms, followed by a full-step CN advance of implicit terms, and then again a half-step RK advance of explicit terms. We note that the critical time-step for stability for the ‘CN-RK-CN’ scheme is half of that for the ‘RK-CN-RK’ scheme, since the latter uses half of the total time-step for each of its RK updates, while the former uses the full time-step in a single RK update. For comparison purposes, we also implement a fully explicit time-stepping using only RK updates, in our framework. These schemes are described in detail in the next section.

## 7Time-stepping schemes

Initially, the perturbed magnetic field is taken to be zero, i.e.𝑩t​o​t=𝑩e​q\bm{B}_{tot}=\bm{B}_{eq}. The particle positions (𝑿i,p\bm{X}_{i,p},𝑿e,g​c,p\bm{X}_{e,gc,p}) and velocities (𝒗i,p\bm{v}_{i,p},𝒗e,g​c,p\bm{v}_{e,gc,p}) are available. The initial𝗘⟂{\bm{\mathsf{E}}}_{\perp}is calculated from equation (97) and𝗘∥{\bm{\mathsf{E}}}_{\parallel}is calculated from equation (104). The initial charge and current densities can then be obtained from equations (93), (94), (90) and (91). This completes the initialization process.

After setting up initial conditions, the temporal updates can be performed using the fully explicit LSRK scheme or the implicit-explicit schemes described below. The LSRK scheme is a basic component of each of the time-stepping methods considered here and therefore must be described first. Thes−s-stage LSRK scheme used for solving ODEs of the form:u′=F​(u​(t)),u​(0)=u0,u^{\prime}=F(u(t)),\quad u(0)=u_{0},(154)

can be described as follows:S1:=un\displaystyle\quad S_{1}=u^{n}(155)for​i=1:s​do\displaystyle\quad\text{for }i=1:s\ \text{do}S2:=Ai​S2+Δ​t​F​(S1)\displaystyle\quad\quad S_{2}=A_{i}S_{2}+\Delta tF(S_{1})S1:=S1+Bi​S2\displaystyle\quad\quad S_{1}=S_{1}+B_{i}S_{2}endun+1=S1.\displaystyle\quad u^{n+1}=S_{1}.

The coefficientsA1(=0),A2,…,AsA_{1}(=0),A_{2},\dots,A_{s}andB1,…,BsB_{1},\dots,B_{s}can be found in the works bywilliamson1980lsrkandmeng2025.

## 7.1Fully explicit scheme

For the fully explicit scheme, each full time-step update comprises the sequential stages described in equation (155). Within each stage of the LSRK algorithm, the following updates are performed:
- 1.

𝗘⟂{\bm{\mathsf{E}}}_{\perp}is calculated using equation (97).
- 2.

𝗘∥{\bm{\mathsf{E}}}_{\parallel}is calculated using equation (104).
- 3.

Particle velocities are updated using equations (83) and (85).
- 4.

Particle positions are updated using equations (82) and (84).
- 5.

𝗕{\bm{\mathsf{B}}}is updated using equation (87).

## 7.2Implicit-explicit (IMEX) schemes

The equation (22) can be written as:∂𝑩∂t+∇×(𝑬⟂+𝑬∥)=∂𝑩∂t+∇×(𝑬⟂,1+𝑬⟂,2+𝑬∥)=𝟎,\frac{\partial\bm{B}}{\partial t}+\nabla\times(\bm{E}_{\perp}+\bm{E}_{\parallel})=\frac{\partial\bm{B}}{\partial t}+\nabla\times(\bm{E}_{\perp,1}+\bm{E}_{\perp,2}+\bm{E}_{\parallel})={\bf 0},(156)

where𝑬⟂\bm{E}_{\perp}has been written as𝑬⟂=𝑬⟂,1+𝑬⟂,2\bm{E}_{\perp}=\bm{E}_{\perp,1}+\bm{E}_{\perp,2}. Here𝑬⟂,1\bm{E}_{\perp,1}and𝑬⟂,2\bm{E}_{\perp,2}are the solutions of the equations:μ0​∫qe​𝑬⟂,1​fe,g​c​d​v∥​d​μ=−μ0​𝒃e​q×𝑱i−μ0​qe​∫(v∥​𝒃e​q×𝑩∗−μqe​∇⟂B∥,tot)​fe,g​c​d​v∥​d​μ.\mu_{0}\int q_{e}\bm{E}_{\perp,1}f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu=-\mu_{0}\bm{b}_{eq}\times\bm{J}_{i}-\mu_{0}q_{e}\int\left(v_{\parallel}{\bm{b}_{eq}\times\bm{B}^{\ast}}-\frac{\mu}{q_{e}}\nabla_{\perp}B_{\parallel,tot}\right)f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu.(157)μ0​∫qe​𝑬⟂,2​fe,g​c​d​v∥​d​μ=𝒃e​q×∇×𝑩.\mu_{0}\int q_{e}\bm{E}_{\perp,2}f_{e,gc}\mathop{}\!\mathrm{d}v_{\parallel}\mathop{}\!\mathrm{d}\mu=\bm{b}_{eq}\times\nabla\times\bm{B}.(158)

Equations (157) and (158) add up to give equation (26). Note that we assumeμ=0\mu=0in equation (157), and that it is shown here only for consistency with (26). For the temporal update of𝗕{\bm{\mathsf{B}}}in the numerical algorithm, the∇×𝑬⟂,2\nabla\times\bm{E}_{\perp,2}term is a stiff term that imposes a stringent constraint on the time-step used. To overcome this constraint, we use an implicit-explicit (IMEX) scheme, where the equation∂𝑩∂t+∇×(𝑬⟂,1+𝑬∥)=𝟎,\frac{\partial\bm{B}}{\partial t}+\nabla\times(\bm{E}_{\perp,1}+\bm{E}_{\parallel})={\bf 0},(159)

is treated explicitly using the LSRK scheme, and the equation∂𝑩∂t+∇×𝑬⟂,2=𝟎,\frac{\partial\bm{B}}{\partial t}+\nabla\times\bm{E}_{\perp,2}={\bf 0},(160)

is treated implicitly using a Crank-Nicolson scheme.
Therefore, the explicit𝑩−\bm{B}-update is performed as:d​𝗕d​t+ℂ​(𝗘⟂,1+𝗘∥)=0,\frac{\mathrm{d}{\bm{\mathsf{B}}}}{\mathrm{d}t}+\mathbb{C}({\bm{\mathsf{E}}}_{\perp,1}+{\bm{\mathsf{E}}}_{\parallel})=0,(161)

where𝗘⟂,1{\bm{\mathsf{E}}}_{\perp,1}is the discretized version of𝑬⟂,1\bm{E}_{\perp,1}. This is obtained by solving equation (97), without accounting for theℂ⊤​ℍ2​𝗕\mathbb{C}^{\top}\mathbb{H}_{2}{\bm{\mathsf{B}}}term on the right hand side, i.e.μ0​∑p=1Newe,p​qe​ℛ~2​(𝑬⟂,1S​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p)​S​(𝑿−𝑿e,g​c,p​(t)))=ℬe​q×[−μ0​𝗝~i−μ0​∑p=1Newe,p​qe​ℛ~2​(V∥,p​𝑩∗​(𝑿e,g​c,p)B∥∗​(𝑿e,g​c,p))​S​(𝑿−𝑿e,g​c,p​(t))].\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{2}\left(\frac{\bm{E}_{\perp,1}^{S}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}S(\bm{X}-\bm{X}_{e,gc,p}(t))\right)\\
=\mathcal{B}_{eq}\times\left[-\mu_{0}\tilde{{\bm{\mathsf{J}}}}_{i}-\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{2}\left(V_{\parallel,p}\frac{\bm{B}^{\ast}(\bm{X}_{e,gc,p})}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\right)S(\bm{X}-\bm{X}_{e,gc,p}(t))\right].(162)

The implicit𝑩−\bm{B}-update is performed using the semi-discrete equation:d​𝗕d​t+ℂ​𝗘⟂,2=0,\frac{\mathrm{d}{\bm{\mathsf{B}}}}{\mathrm{d}t}+\mathbb{C}{\bm{\mathsf{E}}}_{\perp,2}=0,(163)

where𝗘⟂,2{\bm{\mathsf{E}}}_{\perp,2}is the discretized version of𝑬⟂,2\bm{E}_{\perp,2}given by:μ0​∑p=1Newe,p​qe​ℛ~2​(1B∥∗​(𝑿e,g​c,p)​(𝑬⟂,2S​(𝑿e,g​c,p))​S​(𝑿−𝑿e,g​c,p​(t)))=ℬe​q×[ℂ⊤​ℍ2​𝗕].\mu_{0}\sum_{p=1}^{N_{e}}w_{e,p}q_{e}\tilde{\mathcal{R}}_{2}\left(\frac{1}{B_{\parallel}^{\ast}(\bm{X}_{e,gc,p})}\left(\bm{E}_{\perp,2}^{S}(\bm{X}_{e,gc,p})\right)S(\bm{X}-\bm{X}_{e,gc,p}(t))\right)=\mathcal{B}_{eq}\times\left[\mathbb{C}^{\top}\mathbb{H}_{2}{\bm{\mathsf{B}}}\right].(164)

Using the approximation from equation (98), equation (163) becomes:d​𝗕d​t+ℂ​(B∥∗¯ρ¯e,g​c​ℬe​q×[ℂ⊤​ℍ2​𝗕])=0.\frac{\mathrm{d}{\bm{\mathsf{B}}}}{\mathrm{d}t}+\mathbb{C}\left(\frac{\bar{B_{\parallel}^{\ast}}}{\bar{\rho}_{e,gc}}\mathcal{B}_{eq}\times[\mathbb{C}^{\top}\mathbb{H}_{2}{\bm{\mathsf{B}}}]\right)=0.(165)

Discretizing this equation in time using the Crank-Nicolson method, it becomes:𝗕n+1−𝗕nΔ​t+ℂ​(B∥∗¯ρ¯e,g​c​ℬe​q×[ℂ⊤​ℍ2​(𝗕n+1+𝗕n2)])=0,\frac{{\bm{\mathsf{B}}}^{n+1}-{\bm{\mathsf{B}}}^{n}}{\Delta t}+\mathbb{C}\left(\frac{\bar{B_{\parallel}^{\ast}}}{\bar{\rho}_{e,gc}}\mathcal{B}_{eq}\times\left[\mathbb{C}^{\top}\mathbb{H}_{2}\left(\frac{{\bm{\mathsf{B}}}^{n+1}+{\bm{\mathsf{B}}}^{n}}{2}\right)\right]\right)=0,(166)

whereΔ​t\Delta tis the discrete time-step. This is a large, sparse linear system that can be solved to obtain𝗕n+1{\bm{\mathsf{B}}}^{n+1}given𝗕n{\bm{\mathsf{B}}}^{n}. The resultant IMEX time-stepping schemes that are a combination of the LSRK and Crank-Nicolson updates are as follows:

## 7.2.1IMEX1 (CN-RK-CN)
- 1.

𝗕{\bm{\mathsf{B}}}is updated by a half time-stepΔ​t/2\Delta t/2using equation (166).
- 2.

One full time-step LSRK update:
- (a)

𝗘⟂{\bm{\mathsf{E}}}_{\perp}is calculated using equation (97).𝗘⟂,1{\bm{\mathsf{E}}}_{\perp,1}is calculated using equation (162).
- (b)

𝗘∥{\bm{\mathsf{E}}}_{\parallel}is calculated using equation (104).
- (c)

Particle velocities are updated using equations (83) and (85).
- (d)

Particle positions are updated using equations (82) and (84).
- (e)

𝗕{\bm{\mathsf{B}}}is updated using equation (161).
- 3.

𝗕{\bm{\mathsf{B}}}is updated by a half time-stepΔ​t/2\Delta t/2using equation (166).

## 7.2.2IMEX2 (RK-CN-RK)
- 1.

One half time-step LSRK update:
- (a)

𝗘⟂{\bm{\mathsf{E}}}_{\perp}is calculated using equation (97).𝗘⟂,1{\bm{\mathsf{E}}}_{\perp,1}is calculated using equation (162).
- (b)

𝗘∥{\bm{\mathsf{E}}}_{\parallel}is calculated using equation (104).
- (c)

Particle velocities are updated using equations (83) and (85).
- (d)

Particle positions are updated using equations (82) and (84).
- (e)

𝗕{\bm{\mathsf{B}}}is updated using equation (161).
- 2.

𝗕{\bm{\mathsf{B}}}is updated by a full time-stepΔ​t\Delta tusing equation (166).
- 3.

One half time-step LSRK update:
- (a)

𝗘⟂{\bm{\mathsf{E}}}_{\perp}is calculated using equation (97).𝗘⟂,1{\bm{\mathsf{E}}}_{\perp,1}is calculated using equation (162).
- (b)

𝗘∥{\bm{\mathsf{E}}}_{\parallel}is calculated using equation (104).
- (c)

Particle velocities are updated using equations (83) and (85).
- (d)

Particle positions are updated using equations (82) and (84).
- (e)

𝗕{\bm{\mathsf{B}}}is updated using equation (161).

## 8Dispersion relation

It is possible to perform a linear perturbation analysis of the quasineutral hybrid drift-kinetic Vlasov-Maxwell system to obtain a dispersion relation describing the various eigenmodes generated by the system. The dispersion relation can be obtained from the non-quasineutral, hybrid drift-kinetic Vlasov-Maxwell system(meng2025)by simply taking the quasineutral limit i.e.ϵ0→0\epsilon_{0}\to 0. We now describe the dispersion relation for the system of governing equations considered here. An equilibrium state is assumed where𝑬=𝑬0\bm{E}=\bm{E}_{0},𝑩=𝑩e​q\bm{B}=\bm{B}_{eq},fe=fe,0f_{e}=f_{e,0}andfi=fi,0f_{i}=f_{i,0}. Perturbations from equilibrium quantities are denoted by the subscript ‘1’. To obtain the dispersion relation for linear stability analysis, plane-wave perturbations of the form:𝑬1=𝑬^​ei​(𝒌⋅𝒙−ω​t),\bm{E}_{1}=\hat{\bm{E}}e^{i(\bm{k}\cdot\bm{x}-\omega t)},(167)

can be assumed, where𝒌\bm{k}is the wavenumber andω\omegais the angular frequency for the plane-wave perturbation. Applying such perturbations to equations (17), (18), (12), (15), (16) and (22), we get:𝑱^e,g​c=(qe​n0​E^y/B0−qe​n0​E^x/B0J^e,gc∥),\displaystyle\hat{\bm{J}}_{e,gc}=\begin{pmatrix}{q_{e}n_{0}\hat{E}_{y}}/{B_{0}}\\
-{q_{e}n_{0}\hat{E}_{x}}/{B_{0}}\\
\hat{J}_{e,gc\parallel}\end{pmatrix},(168)𝑱i^=qi​∫fi^​𝒗​𝑑𝒗,\displaystyle\hat{\bm{J}_{i}}=q_{i}\int\hat{f_{i}}\bm{v}d\bm{v},(169)−i​ω​fe^+i​k∥​v∥​fe^+qimi​(E^z​∂fe^∂v∥)=0,\displaystyle-i\omega\hat{f_{e}}+ik_{\parallel}v_{\parallel}\hat{f_{e}}+\frac{q_{i}}{m_{i}}\left(\hat{E}_{z}\frac{\partial\hat{f_{e}}}{\partial v_{\parallel}}\right)=0,(170)−i​ω​fi^+i​𝒗i⋅𝒌​fi^+qimi​[(𝒗i×𝑩t​o​t)⋅∂fi^∂𝒗i+(𝑬^+𝒗i×𝑩^)⋅∂fi,0∂𝒗i]=0,\displaystyle-i\omega\hat{f_{i}}+i{\bm{v}_{i}}\cdot\bm{k}\hat{f_{i}}+\frac{q_{i}}{m_{i}}\left[{(\bm{v}_{i}\times\bm{B}_{tot})}\cdot\frac{\partial\hat{f_{i}}}{\partial\bm{v}_{i}}+{(\hat{\bm{E}}+\bm{v}_{i}\times\hat{\bm{B}})}\cdot\frac{\partial f_{i,0}}{\partial\bm{v}_{i}}\right]=0,(171)i​𝒌×𝑩^=μ0​(𝑱^i+𝑱^e,g​c),\displaystyle i\bm{k}\times\hat{\bm{B}}=\mu_{0}(\hat{\bm{J}}_{i}+\hat{\bm{J}}_{e,gc}),(172)ω​𝑩^=𝒌×𝑬^.\displaystyle\omega\hat{\bm{B}}=\bm{k}\times\hat{\bm{E}}.(173)

Eliminating𝑩^\hat{\bm{B}},fe^\hat{f_{e}},fi^\hat{f_{i}},𝑱^e,g​c\hat{\bm{J}}_{e,gc}and𝑱^i\hat{\bm{J}}_{i}from these equations, we obtain the equation:𝒌×𝒌×𝑬^+(ω/c)2​ϵ¯¯⋅𝑬^=0,\bm{k}\times\bm{k}\times\hat{\bm{E}}+(\omega/c)^{2}\underline{\underline{\bm{\epsilon}}}\cdot\hat{\bm{E}}=0,(174)

whereϵ¯¯\underline{\underline{\epsilon}}is the dielectric tensor of the plasma, that can be written as:ϵ¯¯=[ϵx​xϵx​yϵx​zϵy​xϵy​yϵy​zϵz​xϵz​yϵz​z].\underline{\underline{\bm{\epsilon}}}=\begin{bmatrix}\epsilon_{xx}&\epsilon_{xy}&\epsilon_{xz}\\
\epsilon_{yx}&\epsilon_{yy}&\epsilon_{yz}\\
\epsilon_{zx}&\epsilon_{zy}&\epsilon_{zz}\end{bmatrix}.(175)

The plasma dielectric tensor is a matrix that characterizes how a magnetized plasma responds to an applied electric field. It governs the dispersion relation and encapsulates the properties of linear wave propagation in a uniform magnetized plasma. For the hybrid model considered here, the dielectric tensor can be written as a sum of the contributions of the individual species i.e.ϵ¯¯=ϵe¯¯+ϵi¯¯\underline{\underline{\epsilon}}=\underline{\underline{\epsilon_{e}}}+\underline{\underline{\epsilon_{i}}}. Denoting the magnitude of𝒌\bm{k}askk, we can define the refractive indexn=k​c/ωn=kc/\omegaand the wavevector𝜿=𝒌/k\bm{\kappa}=\bm{k}/k, equation (174) becomes:n2​𝜿×𝜿×𝑬^+ϵ¯¯⋅𝑬^=0.n^{2}\bm{\kappa}\times\bm{\kappa}\times\hat{\bm{E}}+\underline{\underline{\bm{\epsilon}}}\cdot\hat{\bm{E}}=0.(176)

Taking the determinant of this linear system gives us the hot plasma dispersion relation:det|n2​(κi​κj−δi​j)+ϵi​j|=0.\det|n^{2}(\kappa_{i}\kappa_{j}-\delta_{ij})+\epsilon_{ij}|=0.(177)

Given the equivalence of all directions perpendicular to the static background magnetic field, we writeϵ¯¯\underline{\underline{\bm{\epsilon}}}in terms ofk⟂k_{\perp}andk∥k_{\parallel}, which are the components of𝒌\bm{k}perpendicular and parallel to the magnetic field, respectively. We assumeθ\thetato be the angle between𝒌\bm{k}and the static background magnetic field. Without loss of generality, we definekx=k⟂k_{x}=k_{\perp},ky=0k_{y}=0andkz=k∥k_{z}=k_{\parallel}, and therefore get:kx=k⟂=k​sin⁡(θ)⟹κx=sin⁡(θ),\displaystyle k_{x}=k_{\perp}=k\sin(\theta)\Longrightarrow\kappa_{x}=\sin(\theta),(178)kz=k∥=k​cos⁡(θ)⟹κz=cos⁡(θ).\displaystyle k_{z}=k_{\parallel}=k\cos(\theta)\Longrightarrow\kappa_{z}=\cos(\theta).(179)

The background magnetic field is therefore along thez−z-direction. The hot plasma dispersion relation, thus becomes:det[ϵx​x−n2​cos2⁡(θ)ϵx​yϵx​z+n2​cos⁡(θ)​sin⁡(θ)ϵy​xϵy​y−n2ϵy​zϵz​x+n2​cos⁡(θ)​sin⁡(θ)ϵz​yϵz​z−n2​sin2⁡(θ)]=0.\det\begin{bmatrix}\epsilon_{xx}-n^{2}\cos^{2}(\theta)&\epsilon_{xy}&\epsilon_{xz}+n^{2}\cos(\theta)\sin(\theta)\\
\epsilon_{yx}&\epsilon_{yy}-n^{2}&\epsilon_{yz}\\
\epsilon_{zx}+n^{2}\cos(\theta)\sin(\theta)&\epsilon_{zy}&\epsilon_{zz}-n^{2}\sin^{2}(\theta)\end{bmatrix}=0.(180)

A detailed derivation of the dispersion relation for the drift-kinetic species, accounting for the nonlinear polarization and magnetization terms, can be found in the work byZonta2021Dispersion. A simplified model without these terms is provided in the work bymeng2025. We also definen⟂=n​sin⁡(θ)n_{\perp}=n\sin(\theta)andn∥=n​cos⁡(θ)n_{\parallel}=n\cos(\theta). In the model considered here, theϵe,x​y\epsilon_{e,xy},ϵe,y​x\epsilon_{e,yx}andϵe,z​z\epsilon_{e,zz}terms of the drift-kinetic electron dielectric tensorϵ𝒆¯¯\underline{\underline{\bm{\epsilon_{e}}}}are given by:ϵe,x​y=−ϵe,y​x=i​qe​neϵ0​Be​q​ω=i​c2​ωc,eVA,e2​ω,\displaystyle\epsilon_{e,xy}=-\epsilon_{e,yx}=i\frac{q_{e}n_{e}}{\epsilon_{0}B_{eq}\omega}=i\frac{c^{2}\omega_{c,e}}{V_{A,e}^{2}\omega},(181)ϵe,z​z=ωp,e2k∥2​vt​h,e2​[1+ζe​Z​(ζe)],\displaystyle\epsilon_{e,zz}=\frac{\omega_{p,e}^{2}}{k_{\parallel}^{2}v_{th,e}^{2}}\left[1+\zeta_{e}Z(\zeta_{e})\right],(182)

whereζe=ω(2)k∥vt​h,e\zeta_{e}=\frac{\omega}{\sqrt{(}2)k_{\parallel}v_{th,e}}. The termsωp,e\omega_{p,e}andΩc,e\Omega_{c,e}are the electron plasma frequency and electron cyclotron frequency already provided in equations (114) and (115), respectively. Also,vt​h,ev_{th,e}is the electron thermal velocity given by:vt​h,e=2​Teme,v_{th,e}=\sqrt{\frac{2T_{e}}{m_{e}}},(183)

whereTeT_{e}is the electron temperature. The termVA,eV_{A,e}is the electron Alfvén speed given by:VA,e=Be​qμ0​me​ne.V_{A,e}=\frac{B_{eq}}{\sqrt{\mu_{0}m_{e}n_{e}}}.(184)

The remainingϵe\epsilon_{e}terms become zero i.e.ϵe,x​x=ϵe,x​z=ϵe,z​x=ϵe,y​y=ϵe,y​z=ϵe,z​y=0\epsilon_{e,xx}=\epsilon_{e,xz}=\epsilon_{e,zx}=\epsilon_{e,yy}=\epsilon_{e,yz}=\epsilon_{e,zy}=0. The individual terms of the fully kinetic ion dielectric tensorϵ𝒊¯¯\underline{\underline{\bm{\epsilon_{i}}}}are given bybrambilla1998kinetic:ϵi,x​x\displaystyle\epsilon_{i,xx}=−ωp,i2ω2​∑n=−∞n=+∞n2λi​In​(λi)​e−λi​(−x0,i​Z​(xn,i)),\displaystyle=-\frac{\omega_{p,i}^{2}}{\omega^{2}}\sum_{n=-\infty}^{n=+\infty}\frac{n^{2}}{\lambda_{i}}I_{n}(\lambda_{i})e^{-\lambda_{i}}(-x_{0,i}Z(x_{n,i})),(185)ϵi,x​y=−ϵi,y​x\displaystyle\epsilon_{i,xy}=-\epsilon_{i,yx}=−i​ωp,i2ω2​∑n=−∞n=+∞n​[In′​(λi)−In​(λi)]​e−λi​(−x0,i​Z​(xn,i)),\displaystyle=-i\frac{\omega_{p,i}^{2}}{\omega^{2}}\sum_{n=-\infty}^{n=+\infty}n[I^{\prime}_{n}(\lambda_{i})-I_{n}(\lambda_{i})]e^{-\lambda_{i}}(-x_{0,i}Z(x_{n,i})),(186)ϵi,x​z=ϵi,z​x\displaystyle\epsilon_{i,xz}=\epsilon_{i,zx}=−12​n⟂​n∥​ωp,i2ω​Ωc,i​vt​h,i2c2​∑n=−∞n=+∞nλi​In​(λi)​e−λi​(x0,i2​Z′​(xn,i)),\displaystyle=-\frac{1}{2}n_{\perp}n_{\parallel}\frac{\omega_{p,i}^{2}}{\omega\Omega_{c,i}}\frac{v_{th,i}^{2}}{c^{2}}\sum_{n=-\infty}^{n=+\infty}\frac{n}{\lambda_{i}}I_{n}(\lambda_{i})e^{-\lambda_{i}}(x_{0,i}^{2}Z^{\prime}(x_{n,i})),(187)ϵi,y​y\displaystyle\epsilon_{i,yy}=−ωp,i2ω2​∑n=−∞n=+∞[n2λi​In​(λi)−2​λi​[In′​(λi)−In​(λi)]]​e−λi​(−x0,i​Z​(xn,i)),\displaystyle=-\frac{\omega_{p,i}^{2}}{\omega^{2}}\sum_{n=-\infty}^{n=+\infty}\left[\frac{n^{2}}{\lambda_{i}}I_{n}(\lambda_{i})-2\lambda_{i}[I^{\prime}_{n}(\lambda_{i})-I_{n}(\lambda_{i})]\right]e^{-\lambda_{i}}(-x_{0,i}Z(x_{n,i})),(188)ϵi,y​z=−ϵi,z​y\displaystyle\epsilon_{i,yz}=-\epsilon_{i,zy}=i2​n⟂​n∥​ωp,i2ω​Ωc,i​vt​h,i2c2​∑n=−∞n=+∞[In′​(λi)−In​(λi)]​e−λi​(x0,i2​Z′​(xn,i)),\displaystyle=\frac{i}{2}n_{\perp}n_{\parallel}\frac{\omega_{p,i}^{2}}{\omega\Omega_{c,i}}\frac{v_{th,i}^{2}}{c^{2}}\sum_{n=-\infty}^{n=+\infty}[I^{\prime}_{n}(\lambda_{i})-I_{n}(\lambda_{i})]e^{-\lambda_{i}}(x_{0,i}^{2}Z^{\prime}(x_{n,i})),(189)ϵi,z​z\displaystyle\epsilon_{i,zz}=−ωp,i2ω2​∑n=−∞n=+∞In​(λi)​e−λi​(x0,i​xn,i​Z′​(xn,i)).\displaystyle=-\frac{\omega_{p,i}^{2}}{\omega^{2}}\sum_{n=-\infty}^{n=+\infty}I_{n}(\lambda_{i})e^{-\lambda_{i}}(x_{0,i}x_{n,i}Z^{\prime}(x_{n,i})).(190)

In the above expressions,λi\lambda_{i}andxn,ix_{n,i}are dimensionless quantities given by:λi=k⟂2​vt​h,i22​Ωc,i2,\lambda_{i}=\frac{k_{\perp}^{2}v_{th,i}^{2}}{2\Omega_{c,i}^{2}},(191)

andxn,i=ω−n​Ωc,ik∥​vt​h,i.x_{n,i}=\frac{\omega-n\Omega_{c,i}}{k_{\parallel}v_{th,i}}.(192)

The termsωp,i\omega_{p,i}andΩc,i\Omega_{c,i}are the ion plasma frequency and ion cyclotron frequency given in equations (114) and (115), respectively, whilevt​h,iv_{th,i}is the thermal velocity given by:vt​h,i=2​Timi,v_{th,i}=\sqrt{\frac{2T_{i}}{m_{i}}},(193)

whereTiT_{i}is the ion temperature. Also,ZZis the plasma dispersion function andInI_{n}denotes the modified Bessel function of ordernn.

## 8.1Cold Plasma Approximation

To obtain a simplified dispersion relation for the case of a cold plasma, we assume the limitTs→0T_{s}\rightarrow 0. This also impliesλs→0\lambda_{s}\rightarrow 0and|xn,s|→∞|x_{n,s}|\rightarrow\infty, causing the componentsϵx​z\epsilon_{xz},ϵz​x\epsilon_{zx},ϵy​z\epsilon_{yz}andϵz​y\epsilon_{zy}of the dielectric tensor to vanish, i.e.limTs→0ϵx​z=limTs→0ϵz​x=limTs→0ϵy​z=limTs→0ϵz​y=0.\lim_{T_{s}\rightarrow 0}\epsilon_{xz}=\lim_{T_{s}\rightarrow 0}\epsilon_{zx}=\lim_{T_{s}\rightarrow 0}\epsilon_{yz}=\lim_{T_{s}\rightarrow 0}\epsilon_{zy}=0.(194)

The remaining terms simplify as:limTs→0ϵx​x=limTs→0ϵy​y\displaystyle\lim_{T_{s}\rightarrow 0}\epsilon_{xx}=\lim_{T_{s}\rightarrow 0}\epsilon_{yy}=S=12​(R+L)=−ωp​i2ω2−Ωc​i2,\displaystyle=S=\frac{1}{2}(R+L)=-\frac{\omega_{pi}^{2}}{\omega^{2}-\Omega_{ci}^{2}},(195)limTs→0ϵx​y=−limTs→0ϵy​x\displaystyle\lim_{T_{s}\rightarrow 0}\epsilon_{xy}=-\lim_{T_{s}\rightarrow 0}\epsilon_{yx}=−i​D=12​i​(R−L)=−i​(ωp​e2ω​|Ωc​e|+Ωc​i​ωp​i2ω​(ω2−Ωc​i2)),\displaystyle=-iD=\frac{1}{2i}(R-L)=-i\left(\frac{\omega_{pe}^{2}}{\omega|\Omega_{ce}|}+\frac{\Omega_{ci}\omega_{pi}^{2}}{\omega(\omega^{2}-\Omega_{ci}^{2})}\right),(196)limTs→0ϵz​z\displaystyle\lim_{T_{s}\rightarrow 0}\epsilon_{zz}=P=−ωp​i2+ωp​e2ω2.\displaystyle=P=-\frac{\omega_{pi}^{2}+\omega_{pe}^{2}}{\omega^{2}}.(197)

Here the termsRRandLLare given by:R=ωp​e2ω​|Ωc​e|−ωp​i2ω​(ω+Ωc​i),\displaystyle R=\frac{\omega_{pe}^{2}}{\omega|\Omega_{ce}|}-\frac{\omega_{pi}^{2}}{\omega(\omega+\Omega_{ci})},(198)L=−ωp​e2ω​|Ωc​e|−ωp​i2ω​(ω−Ωc​i).\displaystyle L=-\frac{\omega_{pe}^{2}}{\omega|\Omega_{ce}|}-\frac{\omega_{pi}^{2}}{\omega(\omega-\Omega_{ci})}.(199)

Therefore, for a cold plasma, equation (180) simplifies to:det[S−n2​cos2⁡(θ)−i​Dn2​cos⁡(θ)​sin⁡(θ)i​DS−n20n2​cos⁡(θ)​sin⁡(θ)0P−n2​sin2⁡(θ)]=0.\det\begin{bmatrix}S-n^{2}\cos^{2}(\theta)&-iD&n^{2}\cos(\theta)\sin(\theta)\\
iD&S-n^{2}&0\\
n^{2}\cos(\theta)\sin(\theta)&0&P-n^{2}\sin^{2}(\theta)\end{bmatrix}=0.(200)

This is the cold plasma dispersion relation.

## 8.2Waves∥\parallelto𝑩0\bm{B}_{0}

The dispersion relation for waves propagating in a direction parallel to the background magnetic field can be obtained by substitutingθ=0\theta=0in equation (200). We thus get the equation:det[S−n2−i​D0i​DS−n2000P]=0.\det\begin{bmatrix}S-n^{2}&-iD&0\\
iD&S-n^{2}&0\\
0&0&P\end{bmatrix}=0.(201)

For the quasineutral case, there is no solution to the equationP=0P=0. The remaining factor simplifies to the equations:n2=S+D=R,\displaystyle n^{2}=S+D=R,(202)n2=S−D=L.\displaystyle n^{2}=S-D=L.(203)

For the right-handed polarized wave, the dispersion relation becomes:c2​k2ω2=R=S+D=ωp​e2ω​|Ωc​e|−ωp​i2ω​(ω+Ωc​i).\frac{c^{2}k^{2}}{\omega^{2}}=R=S+D=\frac{\omega_{pe}^{2}}{\omega|\Omega_{ce}|}-\frac{\omega_{pi}^{2}}{\omega(\omega+\Omega_{ci})}.(204)

Retaining the positive eigenfrequency, the upper right-hand branch becomes:ωR=|Ωc​e|​c​k2​ωp​e2​(c​k+c2​k2+4​ωp​i2).\omega_{R}=\frac{|\Omega_{ce}|ck}{2\omega_{pe}^{2}}\left(ck+\sqrt{c^{2}k^{2}+4\omega_{pi}^{2}}\right).(205)

This is a right-handed, transverse, circularly polarized wave, called the compressional Alfvén wave at lower frequencies and the Whistler wave at higher frequencies (CAW-WHW). This branch has the eigenvector(Ex,i​Ex,0)(E_{x},iE_{x},0). Similarly, for the left-handed polarized wave, the dispersion relation becomes:c2​k2ω2=L=S−D=−ωp​e2ω​|Ωc​e|−ωp​i2ω​(ω−Ωc​i).\frac{c^{2}k^{2}}{\omega^{2}}=L=S-D=-\frac{\omega_{pe}^{2}}{\omega|\Omega_{ce}|}-\frac{\omega_{pi}^{2}}{\omega(\omega-\Omega_{ci})}.(206)

Retaining the positive eigenfrequency, the lower left-hand branch becomes:ωL=|Ωc​e|​c​k2​ωp​e2​(−c​k+c2​k2+4​ωp​i2).\omega_{L}=\frac{|\Omega_{ce}|ck}{2\omega_{pe}^{2}}\left(-ck+\sqrt{c^{2}k^{2}+4\omega_{pi}^{2}}\right).(207)

This is a left-handed, transverse, circularly polarized wave and the corresponding eigenvector is(Ex,−i​Ex,0)(E_{x},-iE_{x},0). This is called the ion cyclotron wave (ICW).

The above waves have been obtained from the cold plasma dispersion relation. However, there are other modes that do not exist in the cold plasma limit. Describing these waves requires the more generic hot plasma dispersion relation given in equation (180). Substitutingk⟂=0k_{\perp}=0in the plasma dielectric tensor, the termsϵx​z\epsilon_{xz},ϵy​z\epsilon_{yz},ϵz​x\epsilon_{zx}andϵz​y\epsilon_{zy}simplify to 0, while the other terms are given by:ϵx​x=ϵy​y\displaystyle\epsilon_{xx}=\epsilon_{yy}=12​ωp,i2ω​k∥​vt​h,i​[Z​(ω−Ωc,ik∥​vt​h,i)+Z​(ω+Ωc,ik∥​vt​h,i)],\displaystyle=\frac{1}{2}\frac{\omega_{p,i}^{2}}{\omega k_{\parallel}v_{th,i}}\left[Z\left(\frac{\omega-\Omega_{c,i}}{k_{\parallel}v_{th,i}}\right)+Z\left(\frac{\omega+\Omega_{c,i}}{k_{\parallel}v_{th,i}}\right)\right],(208)ϵx​y=−ϵy​x\displaystyle\epsilon_{xy}=-\epsilon_{yx}=i2​ωp,i2ω​k∥​vt​h,i​[Z​(ω−Ωc,ik∥​vt​h,i)−Z​(ω+Ωc,ik∥​vt​h,i)]+i​c2​Ωc,eVA,e2​ω,\displaystyle=\frac{i}{2}\frac{\omega_{p,i}^{2}}{\omega k_{\parallel}v_{th,i}}\left[Z\left(\frac{\omega-\Omega_{c,i}}{k_{\parallel}v_{th,i}}\right)-Z\left(\frac{\omega+\Omega_{c,i}}{k_{\parallel}v_{th,i}}\right)\right]+i\frac{c^{2}\Omega_{c,e}}{V_{A,e}^{2}\omega},(209)ϵz​z\displaystyle\epsilon_{zz}=−ωp,i2(k∥​vt​h,i)2​Z′​(ωk∥​vt​h,i)+ωp​e2k∥2​vt​h,e2​[1+ζe​Z​(ζe)].\displaystyle=-\frac{\omega_{p,i}^{2}}{(k_{\parallel}v_{th,i})^{2}}Z^{\prime}\left(\frac{\omega}{k_{\parallel}v_{th,i}}\right)+\frac{\omega_{pe}^{2}}{k_{\parallel}^{2}v_{th,e}^{2}}\left[1+\zeta_{e}Z(\zeta_{e})\right].(210)

The dispersion relation becomes:((ϵx​x−n2)​(ϵy​y−n2)−ϵx​y​ϵy​x)​ϵz​z=0.((\epsilon_{xx}-n^{2})(\epsilon_{yy}-n^{2})-\epsilon_{xy}\epsilon_{yx})\epsilon_{zz}=0.(211)

Besides the warm plasma generalizations of the waves described above, the other solutions of this equation are the heavily damped, higher-order modes of Alfvén-cyclotron waves that have been studied by various researchers such asaraneda2012interactions,astudillo1996highandMatsuda_1986. These modes, with theExE_{x}andEyE_{y}components, manifest as straight lines emanating from (kk,ω\omega) = (0,Ωc,i\Omega_{c,i}), forming a cone-shaped structure on thek−ωk-\omegaplot. The mode obtained fromϵz​z=0\epsilon_{zz}=0, with eigenvector(0,0,Ez)(0,0,E_{z})also forms a similar cone-shaped structure emanating from (kk,ω\omega) = (0, 0). These higher-order modes are a thermal effect wherein the cone-angle decreases with temperature, reducing to zero in the cold plasma limit.

## 8.3Waves⟂\perpto𝑩0\bm{B}_{0}

The dispersion relation for waves propagating in a direction perpendicular to the background magnetic field can be obtained by substitutingθ=π/2\theta=\pi/2in equation (200). We thus get the equation:det[S−i​D0i​DS−n2000P−n2]=0.\det\begin{bmatrix}S&-iD&0\\
iD&S-n^{2}&0\\
0&0&P-n^{2}\end{bmatrix}=0.(212)

Again, for the quasineutral case, there is no solution forP−n2=0P-n^{2}=0. The remaining factor simplifies to:n2=R​LS.n^{2}=\frac{RL}{S}.(213)

Substituting the expressions forRR,LLandSS, and using the relationΩc,e/ωp,e2=−Ωc,i/ωp,i2{\Omega_{c,e}}/{\omega_{p,e}^{2}}=-{\Omega_{c,i}}/{\omega_{p,i}^{2}}for singly charged ions, the above equation becomes:n2=±ωp,e4ωp,i2​|Ωc,e|2.n^{2}=\pm\frac{\omega_{p,e}^{4}}{\omega_{p,i}^{2}|\Omega_{c,e}|^{2}}.(214)

Using the definitions of the plasma and cyclotron frequencies, as provided in equations (114) and (115), and discarding the negative root, the eigenfrequency obtained isωR=VA,i​k\omega_{R}=V_{A,i}k, whereVA,iV_{A,i}is the ion Alfvén speed given by:VA,i=Be​qμ0​mi​ni.V_{A,i}=\frac{B_{eq}}{\sqrt{\mu_{0}m_{i}n_{i}}}.(215)

This corresponds to the Alfvén wave dispersion relation. The eigenvector for this wave is(Ex,−i​Ex,0)(E_{x},-iE_{x},0).

We now use the hot plasma dispersion relation to look at waves that do not exist in the cold plasma limit. Substitutingk∥=0k_{\parallel}=0in the plasma dielectric tensor, the termsϵx​z\epsilon_{xz},ϵy​z\epsilon_{yz},ϵz​x\epsilon_{zx}andϵz​y\epsilon_{zy}simplify to 0, while the other terms, including the contributions of both species, are given by:ϵx​x\displaystyle\epsilon_{xx}=−ωp,i2ω​e−λiλi​∑n=−∞n=+∞n2​In​(λi)ω−n​Ωc,i,\displaystyle=-\frac{\omega_{p,i}^{2}}{\omega}\frac{e^{-\lambda_{i}}}{\lambda_{i}}\sum_{n=-\infty}^{n=+\infty}\frac{n^{2}I_{n}(\lambda_{i})}{\omega-n\Omega_{c,i}},(216)ϵx​y=−ϵy​x\displaystyle\epsilon_{xy}=-\epsilon_{yx}=−i​ωp,i2ω​e−λi​∑n=−∞n=+∞n​[In′​(λi)−In​(λi)]ω−n​Ωc,i+i​c2​ωc​eVA,e2​ω,\displaystyle=-i\frac{\omega_{p,i}^{2}}{\omega}e^{-\lambda_{i}}\sum_{n=-\infty}^{n=+\infty}\frac{n[I^{\prime}_{n}(\lambda_{i})-I_{n}(\lambda_{i})]}{\omega-n\Omega_{c,i}}+i\frac{c^{2}\omega_{ce}}{V_{A,e}^{2}\omega},(217)ϵy​y\displaystyle\epsilon_{yy}=−ωp,i2ω​e−λiλi​∑n=−∞n=+∞n2​In​(λi)+2​λi2​In​(λi)−2​λi2​In′​(λi)ω−n​Ωc,i,\displaystyle=-\frac{\omega_{p,i}^{2}}{\omega}\frac{e^{-\lambda_{i}}}{\lambda_{i}}\sum_{n=-\infty}^{n=+\infty}\frac{n^{2}I_{n}(\lambda_{i})+2\lambda_{i}^{2}I_{n}(\lambda_{i})-2\lambda_{i}^{2}I^{\prime}_{n}(\lambda_{i})}{\omega-n\Omega_{c,i}},(218)ϵz​z\displaystyle\epsilon_{zz}=−ωp,i2ω​e−λi​∑n=−∞n=+∞In​(λi)ω−n​Ωc,i−ωp​e2ω2.\displaystyle=-\frac{\omega_{p,i}^{2}}{\omega}e^{-\lambda_{i}}\sum_{n=-\infty}^{n=+\infty}\frac{I_{n}(\lambda_{i})}{\omega-n\Omega_{c,i}}-\frac{\omega_{pe}^{2}}{\omega^{2}}.(219)

The dispersion relation becomes:(ϵx​x​(ϵy​y−n2)−ϵx​y​ϵy​x)​(ϵz​z−n2)=0.(\epsilon_{xx}(\epsilon_{yy}-n^{2})-\epsilon_{xy}\epsilon_{yx})(\epsilon_{zz}-n^{2})=0.(220)

We first consider the equation(ϵz​z−n2)=0(\epsilon_{zz}-n^{2})=0, with eigenvector(0,0,Ez)(0,0,E_{z}). From equation (219), we see that the refractive indexn=n⟂n=n_{\perp}becomes infinite at all harmonics of the ion cyclotron frequencies i.e.ω=m​Ωc,i\omega=m\Omega_{c,i}, for a positive integermm. Besides these cyclotron harmonic resonances, there are no wave solutions to this equation. The other factor, i.e.(ϵx​x​(ϵy​y−n2)−ϵx​y​ϵy​x)=0(\epsilon_{xx}(\epsilon_{yy}-n^{2})-\epsilon_{xy}\epsilon_{yx})=0, also gives rise to these resonances on account of the(ω−n​Ωc,i)(\omega-n\Omega_{c,i})terms in the denominators seen on the RHS of equations (216)–(218). The other solutions to this equation are the Bernstein waves(bernstein)with the associated eigenvector(Ex,Ey,0)(E_{x},E_{y},0). We note that thex−x-direction is the direction of wave propagation, and therefore theExE_{x}Bernstein waves are longitudinal in nature, while theEyE_{y}Bernstein waves are transverse.

## 9Numerical tests

Tests are now conducted to validate the numerical algorithm. We consider a quasineutral plasma that is initially uniform with each species being described by a Gaussian distribution. The particles are generated using quasi-random Sobol sampling. A reduced mass ratio ofmi/me=4m_{i}/m_{e}=4is used for all simulations considered here. Unless otherwise specified, a total of 500 particles per cell are used everywhere. The initial magnetic field is constant and uniform, and is aligned with one of the cardinal directions of the Cartesian grid. These simulations are allowed to run for a long time and the Fast-Fourier Transform (FFT) of the resultant electric field time-series data is obtained. The numerical waves obtained from these simulations are manifested on thek−ωk-\omegaplot of the FFT spectrum. These are plotted alongside their analytical counterparts obtained from the dispersion relation described earlier in Section8. We use a quasi-1D computational domain with domain size[0,10]×[0,1]×[0,1][0,10]\times[0,1]\times[0,1]and a computational grid comprising256×8×8256\times 8\times 8cells. The higher 256-cell resolution is taken in the direction along which the wave spectrum is studied. All boundaries are assumed to be periodic. A normalized background magnetic field of magnitudeBe​q=1B_{eq}=1is used in all simulations.

## 9.1Waves propagating∥\parallelto𝑩0\bm{B}_{0}(a)(b)(c)(d)(e)(f)Figure 2:Wave spectra of (a)ExE_{x}, (c)EyE_{y}and (e)Ez​(E∥)E_{z}(E_{\parallel})for the ‘RK-CN-RK’ scheme, and of (b)ExE_{x}, (d)EyE_{y}and (f)Ez​(E∥)E_{z}(E_{\parallel})for the fully explicit scheme, forvt​h,e=0.05​cv_{th,e}=0.05candvt​h,i=0.025​cv_{th,i}=0.025c, for𝒌∥𝑩e​q\bm{k}\parallel\bm{B}_{eq}.ExE_{x}andEyE_{y}waves are transverse andEz​(E∥)E_{z}(E_{\parallel})waves are longitudinal. In (a), (b), (c) and (d), the dotted line shows the ion cyclotron wave (ICW) while the dash-dot line shows the compressional Alfvén-whistler wave (CAW-WHW) branch.(a)(b)(c)Figure 3:Zoomed out plots of theExE_{x}wave spectra forvt​h,e=0.05​cv_{th,e}=0.05candvt​h,i=0.025​cv_{th,i}=0.025c, for𝒌∥𝑩e​q\bm{k}\parallel\bm{B}_{eq}, obtained using the (a) ‘RK-CN-RK’, (b) ‘CN-RK-CN’ and (c) fully explicit schemes. The dotted line shows the ion cyclotron wave (ICW) while the dash-dot line shows the compressional Alfvén-whistler wave (CAW-WHW) branch.

We first consider propagation of waves in the direction parallel to that of the equilibrium background magnetic field. The thermal velocity of the electrons is taken to bevt​h,e=0.05​cv_{th,e}=0.05c. In order to satisfy the requirement of thermal equilibrium, the ion thermal velocity is taken to bevt​h,i=0.025​cv_{th,i}=0.025c. This is calculated based on equating the temperatures of both species, and accounting for the reduced particle mass ratio. With the purpose of studying the spectrum of waves parallel to the direction of the background magnetic field, the 256-cell resolution is along this direction. The left hand side subfigures in Figure2show the wave spectra obtained for this case using the ‘RK-CN-RK’ scheme, while the right hand side subfigures show those obtained using the fully explicit scheme. The results obtained using the ‘CN-RK-CN’ are not shown for brevity. The critical time-step for numerical stability isΔ​tc​r​i​t≈0.85\Delta t_{crit}\approx 0.85for the ‘RK-CN-RK’ scheme andΔ​tc​r​i​t≈0.026\Delta t_{crit}\approx 0.026for the fully explicit scheme. The time-steps used in these simulations areΔ​t=0.75\Delta t=0.75for the ‘RK-CN-RK’ scheme andΔ​t=0.02\Delta t=0.02for the fully explicit scheme. This results in computational savings of∼95%\sim 95\%when using the IMEX schemes as opposed to the fully explicit. The ion cyclotron wave (ICW) is clearly observed here in theExE_{x}andEyE_{y}spectra, with the analytical result from equation (207) and the ion cyclotron frequencyΩc,i\Omega_{c,i}superimposed on it. The compressional Alfvén-Whistler wave (CAW-WHW) branch is also observed in theExE_{x}andEyE_{y}spectra, with the analytical result from equation (205) superimposed on it. The conical structure of the damped higher-order Alfvén-cyclotron modes described in Section8.2is also clearly visible in the wave spectra of all three field components. To observe the behaviour of the time-stepping schemes at higher frequencies, zoomed out views ofExE_{x}spectra obtained using all the three schemes are shown in Figure3. On account of the small time-step used, the fully explicit method shows a strong fit with the analytical CAW-WHW branch at high frequencies as seen in Figure3(c). On the other hand, the IMEX schemes show a poor match with analytical results at higher frequencies. Although both IMEX schemes are formally second-order accurate and time-symmetric Strang splittings, they are not equivalent in their spectral properties. Particularly, the wave-frequency spectrum obtained from the ‘CN-RK-CN’ simulation as shown in Figure3(b)displays a nonphysical folding (spurious dispersion relation). This distortion arises when the non-stiff terms are evolved explicitly over a full time-step and the stiff terms are evolved implicitly over two half time-steps, introducing substantial numerical phase errors at high wavenumbers. In dispersive systems where the stiff linear operator dominates the phase evolution, advancing this operator implicitly over the full time-step is essential for preserving the correct dispersion relation.

## 9.2Waves propagating⟂\perpto𝑩0\bm{B}_{0}

We now study waves propagating in a direction perpendicular to the background magnetic field. The 256-cell resolution is now along a direction perpendicular to the background magnetic field, namely thex−x-direction, as this is the direction of wave propagation studied. We first consider a cold plasma with electron thermal velocityvt​h,e=0.01​cv_{th,e}=0.01cand ion thermal velocityvt​h,i=0.005​cv_{th,i}=0.005c. The wave spectra obtained forExE_{x}andEyE_{y}are shown in Figure4. This result shown was obtained using the ‘CN-RK-CN’ scheme, with a time-step ofΔ​t=0.1\Delta t=0.1. While the critical time-step as dictated by the stability criterion isΔ​tc​r​i​t≈0.42\Delta t_{crit}\approx 0.42, the lower time-step was used to obtain a better match between the numerical and analytical dispersion relations at lower frequencies. The compressional Alfvén wave is clearly observed, and shows excellent agreement at lowerkkandω\omegavalues with the theoretical prediction obtained from the cold-plasma dispersion relation. At higherkkandω\omega, the numerical result shows significant deviation from the theoretical prediction, on account of the larger time-step used, as permitted by the IMEX schemes. These higher frequencies can be resolved better by using smaller time-steps, at the expense of computational efficiency, or with the use of higher-order Hodge operators. We also observe ion cyclotron resonances in these spectra, although the temperature is very low. This is because our numerical model is not a cold-plasma model, and can detect these resonances as long at the temperature is not exactly zero.(a)(b)Figure 4:Wave spectra of (a)ExE_{x}, (c)EyE_{y}forvt​h,e=0.05​cv_{th,e}=0.05candvt​h,i=0.025​cv_{th,i}=0.025c, for an electron-ion plasma, for𝒌⟂𝑩e​q\bm{k}\perp\bm{B}_{eq}.ExE_{x}waves are longitudinal andEyE_{y}waves are transverse. The dashed line represents the ion compressional Alfvén wave, with the Alfvén speed given in equation (215).

We then move on to a hot plasma case withvt​h,e=0.5​cv_{th,e}=0.5candvt​h,i=0.25​cv_{th,i}=0.25c. The electric field spectra for this case are shown in the left column of Figure5for the results obtained using the ‘RK-CN-RK’ time-stepping scheme, and in the right column for the results from the fully-explicit scheme. The results obtained from the ‘CN-RK-CK’ scheme are almost indistinguishable from the ‘RK-CN-RK’ results, and are therefore not shown here. The waves observed in theExE_{x}andEyE_{y}spectra are the Bernstein waves described above in Section8.3. These waves show an excellent agreement with the dotted lines representing the analyticalk−ωk-\omegacurves obtained from equating the first factor of equation (220) to zero. TheEzE_{z}spectra clearly show the ion cyclotron harmonic resonances. The theoretical values of the harmonic resonances are marked with dashed lines in Figures5(e)and5(f). These harmonic resonances are also observed in theExE_{x}andEyE_{y}spectra, but their analytical dashed lines are not shown there for better clarity and to avoid clutter. The numerical time-steps used for each of these schemes areΔ​t=0.1\Delta t=0.1for ‘RK-CN-RK’,Δ​t=0.05\Delta t=0.05for ‘CN-RK-CN’, andΔ​t=0.01\Delta t=0.01for the fully-explicit scheme. The critical time-steps as predicted by the cold plasma stability analysis areΔ​t≈0.85\Delta t\approx 0.85,Δ​t≈0.42\Delta t\approx 0.42andΔ​t≈0.026\Delta t\approx 0.026for the ‘RK-CN-RK’, ‘CN-RK-CN’ and fully explicit schemes, respectively. However, for plasmas with significantly high temperatures as considered in this case, the critical time-step is much smaller and difficult to calculate analytically. The time-steps used here were obtained using trial and error. The total computational time is almost the same for the ‘CN-RK-CN’ and ‘RK-CN-RK’ simulations. This is because although the ‘RK-CN-RK’ simulation uses a total number of time-steps that is half of that used by the ‘CN-RK-CN’ simulation, the ‘RK-CN-RK’ scheme has twice the number of LSRK sequences. Besides, although the ‘CN-RK-CN’ scheme uses four times the total number of Crank-Nicolson steps, as compared to the ‘RK-CN-RK’ scheme, the computational cost of these Crank-Nicolson substeps is very small as compared to the RK substeps. The fully-explicit scheme is prohibitively expensive, on account of its much smaller time-step. This results in relative computational savings of∼80%\sim 80\%, when using either of the IMEX schemes.(a)(b)(c)(d)(e)(f)Figure 5:Wave spectra of (a)ExE_{x}, (c)EyE_{y}and (e)Ez​(E∥)E_{z}(E_{\parallel})for the ‘RK-CN-RK’ scheme, and of (b)ExE_{x}, (d)EyE_{y}and (f)Ez​(E∥)E_{z}(E_{\parallel})for the fully explicit scheme, forvt​h,e=0.5​cv_{th,e}=0.5candvt​h,i=0.25​cv_{th,i}=0.25c, for𝒌⟂𝑩e​q\bm{k}\perp\bm{B}_{eq}.ExE_{x}waves are longitudinal andEyE_{y}andEz​(E∥)E_{z}(E_{\parallel})waves are transverse. The dotted lines in (a), (b), (c) and (d) show the Bernstein waves while the dashed lines in (e) and (f) show the ion cyclotron harmonic resonances.

## 9.3Damping of Ion Cyclotron Waves

The last test we consider is the damping of an ion cyclotron wave in a warm plasma. A single sinusoidal perturbation with a specific wavenumber is initialized in a warm, uniform, equilibrium quasineutral plasma. We consider an ion cyclotron wave with the wavenumberk∥=1.2k_{\parallel}=1.2, traveling in the direction parallel to𝑩e​q\bm{B}_{eq}. The 256-cell resolution is therefore along this direction. The warm plasma has an electron thermal velocity ofvt​h,e=0.1​cv_{th,e}=0.1cand ion thermal velocity ofvt​h,i=0.05​cv_{th,i}=0.05c. From the linear perturbation analysis shown in Section6, the following relations between the perpendicular perturbations of the ion current and magnetic field can be derived:J^i,x,k\displaystyle\hat{J}_{i,x,k}=±i​J^i,y,k,\displaystyle=\pm i\hat{J}_{i,y,k},(221)B^x,k\displaystyle\hat{B}_{x,k}=−ωk∥​Ωc,i​J^i,x,k,\displaystyle=-\frac{\omega}{k_{\parallel}\Omega_{c,i}}\hat{J}_{i,x,k},(222)B^y,k\displaystyle\hat{B}_{y,k}=−ωk∥​Ωc,i​J^i,y,k.\displaystyle=-\frac{\omega}{k_{\parallel}\Omega_{c,i}}\hat{J}_{i,y,k}.(223)

The ‘+’ sign in equation (221) corresponds to the ICW branch with the eigenvector(Ex,−i​Ex,0)(E_{x},-iE_{x},0), while the ‘–’ sign corresponds to the CAW-WHW branch with the eigenvector(Ex,i​Ex,0)(E_{x},iE_{x},0). The dispersion properties of a linear perturbation are obtained by solving the warm plasma dispersion((ϵx​x−n2)​(ϵy​y−n2)−ϵx​y​ϵy​x)=0((\epsilon_{xx}-n^{2})(\epsilon_{yy}-n^{2})-\epsilon_{xy}\epsilon_{yx})=0for the waves propagating parallel to the background magnetic field, whereϵx​x\epsilon_{xx},ϵy​y\epsilon_{yy},ϵx​y\epsilon_{xy}andϵy​x\epsilon_{yx}are given in equations (208) and (209). Substituting the wavenumberk∥=1.2k_{\parallel}=1.2, we obtain the solutionω≈1.657\omega\approx 1.657corresponding to the CAW-WHW branch, andω≈0.181−0.0534​i\omega\approx 0.181-0.0534icorresponding to the ICW branch. Here, the real part is the angular speed and the imaginary part is the damping rate. The high frequency CAW-WHW wave has a zero imaginary component and therefore no damping. Therefore, to observe damping, we initialize the low-frequency ICW wave. The ions are initialized with the velocity perturbation given by:vx=0.01​cos⁡(k∥​z),\displaystyle v_{x}=0.01\cos(k_{\parallel}z),(224)vy=0.01​sin⁡(k∥​z),\displaystyle v_{y}=0.01\sin(k_{\parallel}z),(225)

corresponding to the ‘+’ sign in equation (221). Note that the perturbation relations in equations (221)–(223) are obtained from a cold plasma stability analysis, and we must therefore use the cold plasma frequency to initialize the magnetic field perturbations. Using the cold plasma ICW branch solution from (207), for the wavenumberk∥=1.2k_{\parallel}=1.2, we obtainω≈0.217\omega\approx 0.217. Using this value, the perpendicular magnetic field perturbations are initialized as:Bx=−0.007241​cos⁡(k∥​z),\displaystyle B_{x}=-0.007241\cos(k_{\parallel}z),(226)By=−0.007241​sin⁡(k∥​z),\displaystyle B_{y}=-0.007241\sin(k_{\parallel}z),(227)

according to the relations in equations (222) and (223). The resultant damped ion cyclotron wave manifests as sinusoidal perturbations in the electric fields in the perpendicularx−x-andy−y-directions. The numerically obtained time-evolution of theEx+i​EyE_{x}+iE_{y}perturbation amplitude obtained forω​(k∥=1.2)\omega(k_{\parallel}=1.2)is plotted alongside the analytical results in Figure6. After an initial transient phase, the sinusoidal perturbations match well with the analytical hot plasma ICW frequency and damping rate.Figure 6:Damping of(Ex+i​Ey)(E_{x}+iE_{y})perturbations fork∥=1.2k_{\parallel}=1.2in a warm plasma withvt​h,e=0.1​cv_{th,e}=0.1candvt​h,i=0.05​cv_{th,i}=0.05c. The blue graph shows the result obtained from the numerical simulation, while the dashed orange graph shows the expected analytical result. The dashed green line shows the analytical damping rate.

## 10Parallelization and Performance

The simulations presented here are performed using theGEMPICXsoftware framework(gempicx), built upon theAMReXarchitecture(zhang2021amrex).AMReXcontains functionality for massively parallel, block-structured adaptive mesh refinement (AMR) multiphysics applications, including functionality for particle simulations. Parallelism is achieved primarily through distributed-memory execution using MPI, with additional support for shared-memory threading and accelerator-based backends. The work presented here, however, uses only MPI.AMReXpartitions the computational domain into a set of logically rectangular subdomains (grid patches), which are assigned to MPI ranks using a load-balancing strategy aiming to equalize computational work among processes. Each rank is responsible for advancing the solution on its assigned patches, while communication between patches is handled through optimized routines within the framework. Information describing the grid layout is available on all ranks, allowing communication patterns, such as ghost-cell exchanges, to be constructed once and reused efficiently throughout the simulation. Particles are managed using distributed data structures that associate them with the grid patches in which they reside. During time integration, particles may cross patch or process boundaries. When this occurs, they are reassigned to the appropriate destination patch and MPI rank according to their updated positions. This redistribution typically involves communication only between neighboring processes, which helps to keep communication overhead low. Because the method follows a particle-in-cell formulation, frequent coupling between particles and mesh-based fields is required. In practice, this is handled primarily through communication of mesh data. Before interpolating field quantities to particle positions, ghost regions of the mesh are populated using halo exchanges so that each process has access to the necessary field values locally. Following particle-to-mesh deposition, contributions from overlapping regions are combined to ensure consistency and conservation across subdomain boundaries.

All the large, sparse linear systems in our numerical scheme, i.e. equations (97), (104), (162) and (161) are solved in parallel using theHYPRElibrary(falgout2002;falgout2006design;hypre).AMReXalso provides wrappers to link to theHYPRElibrary which has functionalities for building and solving these linear systems. In terms of computational cost, particle-related operations dominate the overall runtime, as is generally the case in PIC simulations. These include both particle pushing and the deposition of particle quantities onto the mesh. These particle-based quantities defined on the mesh include charge density, current density, and all the particle-based terms on the right hand side of equation (104) used to calculate𝗘∥{\bm{\mathsf{E}}}_{\parallel}. For a simulation with 3000 particles per species per cell, the computational costs of the most dominant computations as percentages of the overall cost are as follows:
- 1.

Calculating the right hand side particle contributions in equation (104)≈41%\approx 41\%.
- 2.

Pushing particles using electromagnetic fields≈26%\approx 26\%.
- 3.

Calculating current density≈18%\approx 18\%.
- 4.

Calculating charge density≈6%\approx 6\%.
- 5.

Redistributing particles≈6%\approx 6\%.
- 6.

Solving linear systems in≈0.4%\approx 0.4\%.

As we reduce the number of particles per cell, the dominance of the particle loop computations reduces. for instance, reducing the particle count to 300 per species per cell, the percentage costs become:
- 1.

Calculating the right hand side particle contributions in equation (104)≈38%\approx 38\%.
- 2.

Pushing particles using electromagnetic fields≈23%\approx 23\%.
- 3.

Calculating current density≈17%\approx 17\%.
- 4.

Calculating charge density≈5.5%\approx 5.5\%.
- 5.

Redistributing particles≈5%\approx 5\%.
- 6.

Solving linear systems in≈4%\approx 4\%.

## 11Discussion and conclusions

In this work, we have extended the structure-preservingGEMPICXframework(gempicx)to solve the quasineutral hybrid Vlasov-Maxwell system with drift-kinetic electrons and fully kinetic ions. The resulting numerical method combines the advantages of hybrid modelling with the robustness of structure-preserving discretizations. By deriving the model from a discrete action principle and employing a dual grid mimetic discretization, the resulting scheme inherits key geometric properties of the continuous system, such as the compatibility of Faraday and Ampère equations with the de Rham complex, the solenoidality constraint for the magnetic field, and the quasineutrality constraint on the current density divergence. The formulation avoids explicit time evolution of the discretized electric field. The electric field perpendicular components are instead calculated using the quasineutral Ampère equation, by extracting the𝗘⟂−{\bm{\mathsf{E}}}_{\perp}-dependent component of the drift-kinetic electron current. The parallel component𝗘∥{\bm{\mathsf{E}}}_{\parallel}is obtained using a curl-curl equation, leading to a well-posed linear system at each time-step. As observed in the dispersion relations and numerical results, this hybrid quasineutral model contains an unphysical, high-frequency wave branch that is numerically stiff, severely restricting the time-step for numerical stability. This restriction was relaxed with the help of implicit-explicit (IMEX) schemes, wherein the stiff term was advanced using an unconditionally stable implicit update, while the rest was advanced explicitly with a much weaker time-step restriction. This approach led to significant computational savings when using the IMEX schemes, as compared to the fully explicit scheme. Our scheme was successfully tested by comparing numerical results with the various waves predicted by dispersion relations, and by simulating the damping of an ion cyclotron wave.

Despite these advancements, our scheme still has several limitations, creating possibilities for improvement in the future. Our model is derived from the gyrokinetic model fromburby2019gauge-free, by taking the zero Larmor radius limit for the electrons, and also neglecting polarization and magnetization effects. Finite Larmor radius, polarization, and magnetization effects become essential in regimes where electron-scale dynamics become significant. Adding such effects to our model is an interesting avenue for further studies. For the cold plasma case in Section9.2, our numerical results show observable deviations from the analytical results at high wavenumbers, as seen in Figure4. These deviations are expected to be mitigated with the use of higher-order Hodge operators that have been found to better capture short-wavelength modes(kormann2024). Implementing such operators would involve significant changes to the matrices in equations (104) and (161), and is left for follow-up efforts. The current work is limited to a Cartesian mesh using slab geometry and periodic boundary conditions. Modelling practical applications involving fusion, space or astrophysical plasmas would provide important benchmarks for our scheme. This would require enhancing the scheme to handle non-periodic boundary conditions(monk2003finite), and possibly curvilinear meshes(kreeft2011mimetic;MEIERBACHTOL2017796;perse2021). Additionally, energy-conserving or symplectic time integrators could be explored to further improve long-time stability, compared to standard Runge-Kutta approaches(kraus2017gempic;squire2012geometric;marsden2001discrete). In PIC methods, statistical noise arising from the finite number of particles per cell introduces numerical errors, which can be particularly problematic when simulating second-order effects such as the ion cyclotron damping process considered in Section9.3. Control variate (δ\deltaf) methods(SONNENDRUCKER2015402;bottino2015monte)offer an effective approach to reducing such noise by evolving only the deviation from a known background distribution, thereby improving accuracy without requiring a prohibitive increase in particle number and computational cost.

## Acknowledgments

Computing resources needed for this work were provided by the Max Planck Computing and Data Facility (MPCDF). The EUROfusion project TSVV-G is acknowledged. This work has been carried out within the framework of the EUROfusion Consortium, funded by the European Union via the Euratom Research and Training Programme (Grant Agreement No 101052200 - EUROfusion). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the European Commission can be held responsible for them.

## References

## 


- 


Major funding support from
