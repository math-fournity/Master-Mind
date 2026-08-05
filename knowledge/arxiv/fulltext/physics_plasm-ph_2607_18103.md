# An Implicit Time-Domain Harmonic Balance Method for Radio-Frequency Capacitively Coupled Plasma Simulations

**arXiv ID**: 2607.18103v2
**Authors**: Yuze Zhu, Yufeng Wei, Yue Zhang, Kun Xu
**Published**: 2026-07-20
**Categories**: physics.plasm-ph, math-ph, physics.flu-dyn
**Comments**: 41 pages, 23 figures, research article
**HTML URL**: https://arxiv.org/html/2607.18103v2

## Abstract

Fast and accurate fluid simulation of radio-frequency capacitively coupled plasmas (RF CCPs) is of great importance for the iterative design and parameter optimization of modern plasma reactors. This study presents the first successful extension of the time-domain harmonic balance (HB) method to a fully coupled drift-diffusion-Poisson system with complete electron-energy transport for RF plasma simulations. To resolve the severe numerical stiffness arising from highly nonlinear energy-dependent kinetics and dense phase-coupling, a highly efficient spatiotemporal operator-splitting strategy is employed. By sequentially executing a spatial implicit relaxation and a cell-local temporal inversion, this strategy entirely avoids the memory-intensive assembly of global Jacobians while preserving robust numerical stability. The proposed method is rigorously validated against a standard parallel-plate argon CCP benchmark. Evaluated across all discrete temporal collocation points, the HB solution demonstrates that retaining eight harmonics perfectly resolves both the quasi-steady bulk plasma and the highly nonlinear transient sheath dynamics, yielding macroscopic relative errors strictly below 0.3% compared to conventional dual-time stepping (DTS) solutions. Beyond its high physical fidelity, the time-domain HB method completely bypasses the prohibitive physical transients required by conventional time-marching methods. Evaluated on a purely sequential single-core execution, the HB method delivers a greater than 10-fold speedup over fully converged DTS baselines and remains over 5 times faster than the coarsest time-marching configurations. These results establish the time-domain HB framework as a physically rigorous, memory-efficient, and highly accelerated paradigm for practical RF plasma simulations.

## Full Text

An Implicit Time-Domain Harmonic Balance Method for Radio-Frequency Capacitively Coupled Plasma Simulations

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.18103v2 [physics.plasm-ph] 23 Jul 2026

## An Implicit Time-Domain Harmonic Balance Method for Radio-Frequency Capacitively Coupled Plasma SimulationsYuze ZHUYufeng WEIYue ZHANGKun XU

## Abstract

Fast and accurate fluid simulation of radio-frequency capacitively coupled plasmas (RF CCPs) is of great importance for the iterative design and parameter optimization of modern plasma reactors. This study presents the first successful extension of the time-domain harmonic balance (HB) method to a fully coupled drift-diffusion-Poisson system with complete electron-energy transport for RF plasma simulations. To resolve the severe numerical stiffness arising from highly nonlinear energy-dependent kinetics and dense phase-coupling, a highly efficient spatiotemporal operator-splitting strategy is employed. By sequentially executing a spatial implicit relaxation and a cell-local temporal inversion, this strategy entirely avoids the memory-intensive assembly of global Jacobians while preserving robust numerical stability. The proposed method is rigorously validated against a standard parallel-plate argon CCP benchmark. Evaluated across all discrete temporal collocation points, the HB solution demonstrates that retaining eight harmonics (NH=8N_{H}=8) perfectly resolves both the quasi-steady bulk plasma and the highly nonlinear transient sheath dynamics, yielding macroscopic relative errors strictly below0.3%0.3\%compared to conventional dual-time stepping (DTS) solutions. Beyond its high physical fidelity, the time-domain HB method completely bypasses the prohibitive physical transients required by conventional time-marching methods. Evaluated on a purely sequential single-core execution, the HB method delivers a greater than 10-fold speedup over fully converged DTS baselines and remains over 5 times faster than the coarsest time-marching configurations. These results establish the time-domain HB framework as a physically rigorous, memory-efficient, and highly accelerated paradigm for practical RF plasma simulations.

## keywords:Harmonic balance , Capacitively coupled plasma , Fluid simulation , Operator splitting , Electron-energy transport , Radio-frequency discharge††journal:Journal of Computational Physics\affiliation

[a]
organization= Department of Mathematics, Hong Kong University of Science and Technology,
city= Clear Water Bay, Kowloon, Hong Kong,
country= China,\affiliation

[b]
organization= Department of Mechanical and Aerospace Engineering, Hong Kong University of Science and Technology,
city= Clear Water Bay, Kowloon, Hong Kong,
country= China,\affiliation

[c]
organization= Shenzhen Research Institute, Hong Kong University of Science and Technology,
city= Shenzhen,
country= China,

## 1Introduction

Radio-frequency capacitively coupled plasmas (RF CCPs) are widely used in plasma-assisted etching, deposition, surface activation, and semiconductor manufacturing[16,5,4,20]. Their practical importance has motivated decades of work on kinetic[2,23], hybrid[13,18], and fluid plasma simulation[19,3]. Among these approaches, fluid models remain attractive for reactor-scale calculations because they reduce the kinetic degrees of freedom to a comparatively small set of moments, thereby providing the computational efficiency required for routine iterative design and optimization. While the plasma dynamics are driven by periodic excitations with fixed frequencies, the numerical integration must simultaneously capture complex multiphysics and chemical processes, such as electron drift and diffusion, dielectric relaxation, sheath formation, volumetric reaction kinetics, and electron-energy transport. Consequently, conventional time-marching calculations remain computationally demanding: the time step is tightly restricted by the smallest relevant physical or numerical scales, and the computation must be advanced over many RF cycles until the initial transient decays[7,22].

The immense computational cost of reaching the periodic steady state has motivated various acceleration strategies[10,1,8]. Fully implicit and semi-implicit drift-diffusion-Poisson solvers can significantly relax the severe restrictions imposed by dielectric-relaxation and explicit transport stability limits. However, taking large time steps yields strongly coupled nonlinear algebraic systems, whose poorly conditioned Jacobians demand carefully designed scaling, linearization, and preconditioning techniques. Alternatively, high-order finite-volume or finite-element spatial discretizations can achieve a target accuracy with significantly fewer spatial degrees of freedom[6]. More recently, reduced-order and machine-learning models have been deployed to accelerate repeated parameter queries; yet, because these data-driven approaches rely on high-fidelity time-domain simulations for training, they inherently inherit the prohibitive upfront cost of generating the database[24]. Another classical approach to bypass the transient phase is the Newton-Raphson cycle-acceleration method, which formulates a root-finding problem for the periodic state by integrating sensitivity equations over a full RF cycle[17]. While this scheme dramatically reduces the number of simulated cycles for species with slow response times, such as metastables, evaluating the full-cycle Jacobian is generally too memory- and CPU-intensive to apply to all degrees of freedom in multidimensional fluid models. Despite these remarkable advancements, completely eliminating the computational waste of time-marching through a long transient phase remains a critical problem to be solved.

The harmonic balance (HB) method directly overcomes this computational barrier by rigorously solving for the periodic state[12,11,27]. By expanding a periodic variable as a truncated Fourier series—or equivalently, sampling it at a finite set of time-domain collocation points—the physical time derivative is exactly mapped to a dense time-spectral operator that couples all temporal phases. This spectral transformation essentially converts the unsteady governing equations into an inherently quasi-steady system of coupled spatial equations, which can then be efficiently driven to convergence using pseudo-time relaxation or Newton-type algorithms. While HB and its time-spectral variants have achieved mature success in structural dynamics[14], turbomachinery aeroelasticity[26], and periodic fluid flows[9], their extension to RF plasma simulation is exceptionally promising. Not only is the discharge driven by a strictly prescribed external frequency, but both experimental diagnostics and baseline numerical responses of RF CCPs naturally exhibit strongly discrete harmonic components, making them an ideal physical system for frequency-domain or time-spectral resolution.

A recent study demonstrated the potential of HB for accelerating low-temperature plasma simulations by applying a high-dimensional HB formulation to a one-dimensional argon discharge[28]. While achieving substantial reductions in CPU time for density-only drift-diffusion-Poisson calculations, that benchmark work also brought to light the characteristic HB challenges of harmonic truncation and aliasing. However, to maintain numerical tractability, the plasma model in that study relied on the local-field approximation (LFA), wherein the electron energy equation is omitted and transport and ionization coefficients are assumed to be determined instantaneously by the local electric field. However, for realistic RF discharges, a physically rigorous description requires the local-mean-energy approximation (LMEA) to couple electron energy dynamics. Numerically, this coupling drastically escalates the stiffness and non-linearity of the system due to the introduction of energy transport, Joule heating, and strongly temperature-dependent reaction rates.

To address these limitations, this work develops a generalized time-domain HB framework for fluid simulations of RF CCPs based on the drift-diffusion approximation. The governing equations comprise species continuity and electron energy equations, tightly coupled with a phase-resolved Poisson equation. By employing a truncated Fourier expansion and evaluating the macroscopic variables at discrete temporal collocation points, the physical time derivatives are strictly transformed into time-spectral source terms. This spectral mapping inherently couples the transient states across all temporal collocation points, converting the original unsteady problem into a quasi-steady system and effectively bypassing the prohibitive computational overhead of conventional time-marching methods.

Solving this pseudo-spectral system, however, presents a significant computational challenge. The primary bottleneck stems from the numerical stiffness introduced by the dense phase-coupling nature of the time spectral operator. An explicit treatment of these source terms inevitably amplifies errors and triggers severe instabilities at large pseudo-time steps. To ensure robust numerical stability, we propose an implicit pseudo-time marching strategy based on a spatiotemporal operator-splitting strategy. In this approach, the spatial transport and volumetric reaction terms are advanced via a local implicit relaxation method independently at each temporal collocation point, while the stiff time spectral source term is treated implicitly through a cell-local dense matrix inversion. Concurrently, a semi-implicit correction is integrated into the phase-wise Poisson solver to overcome the strict dielectric relaxation limit. By restricting all implicit inversion operations strictly to the cell level, this decoupled approach entirely avoids the assembly of a massive global Jacobian matrix. This ensures high memory efficiency while significantly widening the stability margins against strong nonlinearity and stiffness. To rigorously assess the overall performance of the proposed framework, comprehensive benchmark evaluations are conducted against fully converged time-marching solutions.

The remainder of this paper is organized as follows. Section2details the numerical methodology, including the physical governing equations, the time-domain HB formulation, and the proposed implicit pseudo-time relaxation method. Section3presents a rigorous spatiotemporal validation of the HB solver, followed by a systematic assessment of its harmonic convergence and computational acceleration for representative RF CCP configurations. Finally, Section4draws the main conclusions of this work.

## 2Mathematical and Numerical Formulation

## 2.1Governing Equations and Nondimensionalization

The radio-frequency capacitively coupled plasma (RF CCP) is modeled based on a macroscopic continuum fluid framework. Given that the characteristic length scales of the reactor are significantly smaller than the electromagnetic wavelength of the RF drive, inductive effects can be negligible. Consequently, the self-consistent electric field𝐄=−∇ϕ\mathbf{E}=-\nabla\phiis rigorously described by the electrostatic approximation, where the potentialϕ\phiis governed by Poisson’s equation:−∇⋅(ϵ0​∇ϕ)=e​(ni−ne),-\nabla\cdot\left(\epsilon_{0}\nabla\phi\right)=e\left(n_{i}-n_{e}\right),(1)

wherenen_{e}andnin_{i}denote the electron and positive ion number densities,eeis the elementary charge, andϵ0\epsilon_{0}is the vacuum permittivity.

To resolve the fundamental discharge kinetics, the transport model tracks the spatiotemporal evolution of electrons, positive ions, and neutral metastable atoms (denoted by the subscript∗*). Under the highly collisional regime typical of such discharges, the macroscopic species fluxes are adequately captured by the drift-diffusion approximation. The corresponding continuity equations are formulated as:∂ne∂t+∇⋅𝚪e=Se,\frac{\partial n_{e}}{\partial t}+\nabla\cdot\bm{\Gamma}_{e}=S_{e},(2)∂ni∂t+∇⋅𝚪i=Si,\frac{\partial n_{i}}{\partial t}+\nabla\cdot\bm{\Gamma}_{i}=S_{i},(3)∂n∗∂t+∇⋅𝚪∗=S∗.\frac{\partial n_{*}}{\partial t}+\nabla\cdot\bm{\Gamma}_{*}=S_{*}.(4)

The transport fluxes𝚪\bm{\Gamma}incorporate both electromigration driven by the macroscopic electric field and concentration-gradient-driven diffusion. Because the metastable species are electrically neutral, their transport reduces to pure diffusion. The respective fluxes are explicitly given by:𝚪e=−μe​ne​𝐄−De​∇ne,\bm{\Gamma}_{e}=-\mu_{e}n_{e}\mathbf{E}-D_{e}\nabla n_{e},(5)𝚪i=μi​ni​𝐄−Di​∇ni,\bm{\Gamma}_{i}=\mu_{i}n_{i}\mathbf{E}-D_{i}\nabla n_{i},(6)𝚪∗=−D∗​∇n∗,\bm{\Gamma}_{*}=-D_{*}\nabla n_{*},(7)

whereμ\muandDDrepresent the mobilities and diffusion coefficients of the respective species.

The volumetric source terms (SeS_{e},SiS_{i}, andS∗S_{*}) represent the net production and depletion rates dictated by gas-phase chemical kinetics. For the charged species, the primary generation mechanisms include direct electron-impact ionization from the background ground state, stepwise ionization of metastables, and metastable pooling. Assuming singly charged ions, the electron and ion sources are strictly equivalent (Se=SiS_{e}=S_{i}) and can be expanded as:Se=kion​Ng​ne+ksi​n∗​ne+kmp​n∗2,S_{e}=k_{\rm ion}N_{g}n_{e}+k_{\rm si}n_{*}n_{e}+k_{\rm mp}n_{*}^{2},(8)

whereNgN_{g}is the number density of background neutral gas, andkionk_{\rm ion},ksik_{\rm si}, andkmpk_{\rm mp}are the rate coefficients for direct ionization, stepwise ionization, and metastable pooling, respectively.

To accurately capture the non-local and non-equilibrium electron dynamics, the electron energy densityεe=32​ne​kB​Te\varepsilon_{e}=\frac{3}{2}n_{e}k_{B}T_{e}(withTeT_{e}denoting the electron temperature inK\mathrm{K}) is governed by a conservative transport equation:∂εe∂t+∇⋅𝚪ε=𝐉e⋅𝐄−∑jΔ​ℰj​Sj.\frac{\partial\varepsilon_{e}}{\partial t}+\nabla\cdot\bm{\Gamma}_{\varepsilon}=\mathbf{J}_{e}\cdot\mathbf{E}-\sum_{j}\Delta\mathcal{E}_{j}S_{j}.(9)

Within the drift-diffusion framework, the electron energy flux𝚪ε\bm{\Gamma}_{\varepsilon}is modeled assuming standard electron-enthalpy closure:𝚪ε=−53​μe​εe​𝐄−53​De​∇εe.\bm{\Gamma}_{\varepsilon}=-\frac{5}{3}\mu_{e}\varepsilon_{e}\mathbf{E}-\frac{5}{3}D_{e}\nabla\varepsilon_{e}.(10)

On the right-hand side of Eq. (9), the term𝐉e⋅𝐄\mathbf{J}_{e}\cdot\mathbf{E}accounts for the local Joule heating, where𝐉e=−e​𝚪e\mathbf{J}_{e}=-e\bm{\Gamma}_{e}is the electron current density. The summation term encompasses the aggregate inelastic collisional energy losses. For eachjj-th collision channel,SjS_{j}represents its volumetric reaction rate, andΔ​ℰj\Delta\mathcal{E}_{j}dictates the specific threshold energy loss.

Because the rate coefficients for electron-impact reactions are acutely sensitive to the electron energy, they are typically parameterized as functions of the local mean electron energy. In the present macroscopic formulation, this mean energy is defined directly from the transported state variables as:ε¯e=εene=32​kB​Te.\bar{\varepsilon}_{e}=\frac{\varepsilon_{e}}{n_{e}}=\frac{3}{2}k_{B}T_{e}.(11)

To alleviate the severe numerical stiffness caused by the vast multi-scale disparities in physical quantities, the governing system is rigorously nondimensionalized. DefiningLrefL_{\rm ref},nrefn_{\rm ref},Te,refT_{e,\rm ref}, andΦref\Phi_{\rm ref}as the chosen reference length, number density, electron temperature, and electrostatic potential, respectively, the reference electron thermal speed and characteristic timescale are derived as:vref=(8​kB​Te,refπ​me)1/2,v_{\rm ref}=\left(\frac{8k_{B}T_{e,\rm ref}}{\pi m_{e}}\right)^{1/2},(12)tref=Lrefvref,t_{\rm ref}=\frac{L_{\rm ref}}{v_{\rm ref}},(13)

wherekBk_{B}is the Boltzmann constant andmem_{e}is the electron mass. The reference electron energy density is correspondingly scaled by:εref=32​nref​kB​Te,ref.\varepsilon_{\rm ref}=\frac{3}{2}n_{\rm ref}k_{B}T_{e,\rm ref}.(14)

All subsequent secondary variables—including transport coefficients, reaction rate coefficients, and vacuum permittivity—are scaled consistently against these primary reference values. This systematic scaling ensures that the dimensionless governing equations maintain the exact mathematical structure of their dimensional counterparts; thus, the dimensionless forms are omitted here for brevity.

## 2.2Time-Domain Harmonic Balance Formulation

The RF-periodic solution is assumed to reach a quasi-steady state with the fundamental periodT=2​πω.T=\frac{2\pi}{\omega}.(15)

For a scalar periodic variableQ​(𝐱,t)Q(\mathbf{x},t), the representation based on a truncated Fourier series withNHN_{H}harmonics isQ​(𝐱,t)≈∑k=−NHNHQ^k​(𝐱)​ei​k​ω​t,Q(\mathbf{x},t)\approx\sum_{k=-N_{H}}^{N_{H}}\widehat{Q}_{k}(\mathbf{x})e^{ik\omega t},(16)

whereQ^k\widehat{Q}_{k}represents the complex Fourier coefficients satisfying the conjugate symmetryQ^−k=Q^k∗\widehat{Q}_{-k}=\widehat{Q}_{k}^{*}. The number of temporal collocation points is chosen to satisfy the Nyquist criterion:NT=2​NH+1,N_{T}=2N_{H}+1,(17)

with the temporal collocation points uniformly distributed over one fundamental period:tm=m​TNT,m=0,1,…,NT−1.t_{m}=\frac{mT}{N_{T}},\qquad m=0,1,\ldots,N_{T}-1.(18)

By assembling the flow variables at these collocation points into time-domain vectors, e.g.,𝐐=[𝐐|t0,…,𝐐|t2​NH]T\mathbf{Q}=[\mathbf{Q}|_{t_{0}},\dots,\mathbf{Q}|_{t_{2N_{\text{H}}}}]^{T}, the discrete Fourier transform (DFT) provides a direct mapping between the solution values at the discrete sub-time levels and their corresponding frequency-domain Fourier coefficients:𝐐^=𝐃​𝐐.\widehat{\mathbf{Q}}=\mathbf{D}\,\mathbf{Q}.(19)

The discrete Fourier transform (DFT) matrix𝐃\mathbf{D}and its inverse𝐃−1\mathbf{D}^{-1}govern this transformation. Specifically, the inverse DFT matrix𝐃−1\mathbf{D}^{-1}is explicitly defined using the complex exponential basis functions evaluated at the collocation points as follows:𝐃−1=[1ei​ω​t0ei​2​ω​t0…e−i​ω​t01ei​ω​t1ei​2​ω​t1…e−i​ω​t1⋮⋮⋮⋱⋮1ei​ω​tNT−1ei​2​ω​tNT−1…e−i​ω​tNT−1].\mathbf{D}^{-1}=\begin{bmatrix}1&e^{i\omega t_{0}}&e^{i2\omega t_{0}}&\dots&e^{-i\omega t_{0}}\\
1&e^{i\omega t_{1}}&e^{i2\omega t_{1}}&\dots&e^{-i\omega t_{1}}\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&e^{i\omega t_{N_{T}-1}}&e^{i2\omega t_{N_{T}-1}}&\dots&e^{-i\omega t_{N_{T}-1}}\end{bmatrix}.(20)

Consequently, the differentiation in physical time can be exactly represented at the discrete temporal collocation points by a matrix multiplication:∂𝐐∂t=𝐃−1​𝐊​𝐐^=𝐃−1​𝐊𝐃​𝐐=𝐄𝐐,\frac{\partial\mathbf{Q}}{\partial t}=\mathbf{D}^{-1}\mathbf{K}\widehat{\mathbf{Q}}=\mathbf{D}^{-1}\mathbf{K}\mathbf{D}\,\mathbf{Q}=\mathbf{E}\mathbf{Q},(21)

where matrix𝐊\mathbf{K}is defined as𝐊=i​ω​diag⁡(0,1,…,NH,−NH,…,−1).\mathbf{K}=i\omega\operatorname{diag}(0,1,\ldots,N_{H},-N_{H},\ldots,-1).(22)

Although Eq. (21) is mathematically derived using a complex Fourier basis, the resulting operator𝐄\mathbf{E}analytically maps real discrete-time vectors to real temporal derivatives. For an odd number of collocation pointsNTN_{T}, this operator can be written explicitly as a real, dense, skew-symmetric matrix:(𝐄)m​ℓ={ω2​(−1)m−ℓ​csc⁡[π​(m−ℓ)NT],m≠ℓ,0,m=ℓ.(\mathbf{E})_{m\ell}=\begin{cases}\displaystyle\frac{\omega}{2}(-1)^{m-\ell}\csc\left[\frac{\pi(m-\ell)}{N_{T}}\right],&m\neq\ell,\\
0,&m=\ell.\end{cases}(23)

The strict skew-symmetry of𝐄\mathbf{E}intrinsically reflects the non-dissipative character of the time spectral operator within the retained harmonic subspace. Any harmonic truncation errors and nonlinear aliasing effects are systematically controlled by increasingNHN_{H}, which will be assessed in the numerical results.

By applying the time spectral operator defined in Eq. (21) to the continuous governing equations, the continuous time derivatives are replaced by discrete couplings across all phases. Let𝐧e∗\mathbf{n}_{e}^{*},𝐧i∗\mathbf{n}_{i}^{*},𝐧∗∗\mathbf{n}_{*}^{*}, and𝜺e∗\bm{\varepsilon}_{e}^{*}denote the HB phase vectors of the transported variables at a fixed spatial location. For a specific temporal collocation pointtmt_{m}, the HB form of the plasma fluid system is written as:∑ℓ=0NT−1(𝐄)m​ℓ​ne,ℓ+∇⋅𝚪e,m\displaystyle\sum_{\ell=0}^{N_{T}-1}(\mathbf{E})_{m\ell}n_{e,\ell}+\nabla\cdot\bm{\Gamma}_{e,m}=Se,m,\displaystyle=S_{e,m},(24a)∑ℓ=0NT−1(𝐄)m​ℓ​ni,ℓ+∇⋅𝚪i,m\displaystyle\sum_{\ell=0}^{N_{T}-1}(\mathbf{E})_{m\ell}n_{i,\ell}+\nabla\cdot\bm{\Gamma}_{i,m}=Si,m,\displaystyle=S_{i,m},(24b)∑ℓ=0NT−1(𝐄)m​ℓ​n∗,ℓ+∇⋅𝚪∗,m\displaystyle\sum_{\ell=0}^{N_{T}-1}(\mathbf{E})_{m\ell}n_{*,\ell}+\nabla\cdot\bm{\Gamma}_{*,m}=S∗,m,\displaystyle=S_{*,m},(24c)∑ℓ=0NT−1(𝐄)m​ℓ​εe,ℓ+∇⋅𝚪ε,m\displaystyle\sum_{\ell=0}^{N_{T}-1}(\mathbf{E})_{m\ell}\varepsilon_{e,\ell}+\nabla\cdot\bm{\Gamma}_{\varepsilon,m}=PJ,m−∑jΔ​ℰj​Sj,m.\displaystyle=P_{J,m}-\sum_{j}\Delta\mathcal{E}_{j}S_{j,m}.(24d)

Crucially, all strongly nonlinear transport coefficients, volumetric reaction rates (e.g.,Se,mS_{e,m},S∗,mS_{*,m}), Joule heating terms (PJ,mP_{J,m}), and boundary fluxes are evaluated directly at the temporal collocation pointtmt_{m}. This decoupling is the central advantage of the time-domain HB implementation. By evaluating the highly non-linear plasma kinetics and physical constraints strictly locally in each temporal collocation point, the method completely avoids frequency-domain convolutions, while the periodic time evolution remains globally and rigorously governed by the dense time spectral operator𝐄\mathbf{E}.

Furthermore, because Poisson’s equation contains no explicit physical time derivative, it effectively acts as an elliptic constraint evaluated independently at each temporal collocation point:∇⋅(ϵ0​∇ϕm)=−e​(ni,m−ne,m),m=0,1,…,NT−1.\nabla\cdot(\epsilon_{0}\nabla\phi_{m})=-e(n_{i,m}-n_{e,m}),\qquad m=0,1,\ldots,N_{T}-1.(25)

The corresponding time-varying boundary conditions are evaluated at these temporal collocation points, ensuring that the electrostatic constraints are perfectly synchronized with the HB temporal collocation.

## 2.3Finite-Volume Spatial Discretization

To numerically resolve the RF-periodic discharge dynamics, the governing equations in the HB form must be discretized spatially. The computational domain is discretized by non-overlapping cell-centered control volumes. Integrating the governing system over a control volumeΩi\Omega_{i}with volumeViV_{i}yields the discrete nonlinear HB residual for celliiat a specific temporal collocation pointtmt_{m}(denoted by the indexmm):𝐆i,m=−∑f∈∂ΩiAf​𝐅f,m+Vi​𝐒i,m−Vi​∑ℓ=0NT−1𝐄m​ℓ​𝐐i,ℓ=𝟎,\mathbf{G}_{i,m}=-\sum_{f\in\partial\Omega_{i}}A_{f}\mathbf{F}_{f,m}+V_{i}\mathbf{S}_{i,m}-V_{i}\sum_{\ell=0}^{N_{T}-1}\mathbf{E}_{m\ell}\mathbf{Q}_{i,\ell}=\mathbf{0},(26)

whereAfA_{f}represents the face area, and𝐄m​ℓ\mathbf{E}_{m\ell}denotes the components of the denseNT×NTN_{T}\times N_{T}time spectral operator𝐄\mathbf{E}.

At a given collocation pointmm, the conservative variable vector𝐐i,m\mathbf{Q}_{i,m}and the corresponding volumetric source vector𝐒i,m\mathbf{S}_{i,m}for celliiare compactly grouped as:𝐐i,m=[ne,i,mni,i,mn∗,i,mεe,i,m]T,\mathbf{Q}_{i,m}=\begin{bmatrix}n_{e,i,m}&n_{i,i,m}&n_{*,i,m}&\varepsilon_{e,i,m}\end{bmatrix}^{T},(27)𝐒i,m=[Se,i,mSi,i,mS∗,i,mPJ,i,m−∑jΔ​ℰj​Sj,i,m]T.\mathbf{S}_{i,m}=\begin{bmatrix}S_{e,i,m}&S_{i,i,m}&S_{*,i,m}&P_{J,i,m}-\sum_{j}\Delta\mathcal{E}_{j}S_{j,i,m}\end{bmatrix}^{T}.(28)

in which the volumetric electrostatic work is evaluated in a face-consistent discrete form:PJ,i,m​Vi≈−ϕi,m​∑f∈∂ΩiAf​Je,f,m,P_{J,i,m}V_{i}\approx-\phi_{i,m}\sum_{f\in\partial\Omega_{i}}A_{f}J_{e,f,m},(29)

whereJe,f,m=−e​(𝚪e,f,m⋅𝐧f)J_{e,f,m}=-e(\bm{\Gamma}_{e,f,m}\cdot\mathbf{n}_{f})is the local electron-current contribution passing through faceff.

As shown in Eq.26, the total residual𝐆i,m\mathbf{G}_{i,m}is inherently composed of a purely physical residual and a time spectral source term. The physical spatial-chemical residual, denoted as𝐑i,mphys\mathbf{R}_{i,m}^{\text{phys}}, is defined as:𝐑i,mphys=−∑f∈∂ΩiAf​𝐅f,m+Vi​𝐒i,m,\mathbf{R}_{i,m}^{\text{phys}}=-\sum_{f\in\partial\Omega_{i}}A_{f}\mathbf{F}_{f,m}+V_{i}\mathbf{S}_{i,m},(30)

which encapsulates the flux and reactive source evaluations at the temporal collocation pointtmt_{m}. Conversely, the remaining termVi​∑ℓ𝐄m​ℓ​𝐐i,ℓV_{i}\sum_{\ell}\mathbf{E}_{m\ell}\mathbf{Q}_{i,\ell}represents the time spectral source term introduced by the time-domain HB. It mathematically couples the local state at the current temporal collocation point to the states at all other temporal collocation points, thereby driving the transient evolution toward a dynamic steady state.

A fundamental advantage of this time-domain HB framework is that the physical residual𝐑i,mphys\mathbf{R}_{i,m}^{\text{phys}}is evaluated entirely independently at each temporal collocation point. Because the spatial non-linear fluxes𝐅f,m\mathbf{F}_{f,m}and chemical sources are temporally dependent, the formulation strictly follows the identical reconstruction and evaluation procedures used in time-marching solvers. By using only the macroscopic variables attmt_{m}, the method completely avoids the complex frequency convolutions typically encountered in frequency-domain methods.

At convergence, the algebraic residual system𝐆i,m=𝟎\mathbf{G}_{i,m}=\mathbf{0}is strictly satisfied for every spatial cell across all temporal collocation points, yielding the spectrally accurate RF-periodic steady state.

## 2.4Implicit Spatio-Temporal Decoupling and Block Relaxation

To efficiently drive the discrete residual system to convergence, an implicit pseudo-time integration method is introduced by defining a pseudo-time parameterτ\tau. Letssdenote the pseudo-time iteration index, and then define the increment asΔ​𝐐=𝐐s+1−𝐐s.\Delta\mathbf{Q}=\mathbf{Q}^{s+1}-\mathbf{Q}^{s}.(31)

If a standard implicit backward Euler linearization were applied directly to Eq. (26), the corrections of allNTN_{T}collocation points within a cell would be monolithically coupled by the time spectral operator𝐄\mathbf{E}. To mathematically represent this monolithic system at cellii, we temporarily concatenate the conservative variables, physical spatial-chemical residual and total residuals across all temporal collocation points into augmented vectors:𝐐i=[𝐐i,0…𝐐i,NT−1]T,\mathbf{Q}_{i}=\begin{bmatrix}\mathbf{Q}_{i,0}&\dots&\mathbf{Q}_{i,N_{T}-1}\end{bmatrix}^{T},(32)𝐑iphys=[𝐑i,0phys…𝐑i,NT−1phys]T.\mathbf{R}_{i}^{\text{phys}}=\begin{bmatrix}\mathbf{R}_{i,0}^{\text{phys}}&\dots&\mathbf{R}_{i,N_{T}-1}^{\text{phys}}\end{bmatrix}^{T}.(33)𝐆i=[𝐆i,0…𝐆i,NT−1]T.\mathbf{G}_{i}=\begin{bmatrix}\mathbf{G}_{i,0}&\dots&\mathbf{G}_{i,N_{T}-1}\end{bmatrix}^{T}.(34)

The unfactored implicit linear system for celliithen reads:[ViΔ​τ​𝐈+Vi​(𝐄⊗𝐈q)−∂𝐑iphys∂𝐐i]​Δ​𝐐i−∑j∈𝒩​(i)∂𝐑iphys∂𝐐j​Δ​𝐐j=𝐆i​(𝐐s,ϕs),\left[\frac{V_{i}}{\Delta\tau}\mathbf{I}+V_{i}(\mathbf{E}\otimes\mathbf{I}_{q})-\frac{\partial\mathbf{R}_{i}^{\text{phys}}}{\partial\mathbf{Q}_{i}}\right]\Delta\mathbf{Q}_{i}-\sum_{j\in\mathcal{N}(i)}\frac{\partial\mathbf{R}_{i}^{\text{phys}}}{\partial\mathbf{Q}_{j}}\Delta\mathbf{Q}_{j}=\mathbf{G}_{i}(\mathbf{Q}^{s},\phi^{s}),(35)

where𝒩​(i)\mathcal{N}(i)is the set of neighboring spatial cells,𝐈q\mathbf{I}_{q}is theNq×NqN_{q}\times N_{q}identity matrix corresponding to theNqN_{q}conservative variables and⊗\otimesdenotes the Kronecker product.

To avoid the steep computational expense associated with inverting the fully coupled local augmented block, a spatio-temporal approximate factorization (AF) is introduced. By defining the local spatial-chemical Jacobian at a specific temporal collocation pointmmas𝐀i​i,m=−1Vi​∂𝐑i,mphys∂𝐐i,m,\mathbf{A}_{ii,m}=-\frac{1}{V_{i}}\frac{\partial\mathbf{R}_{i,m}^{\text{phys}}}{\partial\mathbf{Q}_{i,m}},(36)

which inherently encapsulates both the exact spatial flux derivatives and the stiff chemical source Jacobians and utilizing the multi-time block form𝐀i​i=diag⁡(𝐀i​i,0,…,𝐀i​i,NT−1),\mathbf{A}_{ii}=\operatorname{diag}(\mathbf{A}_{ii,0},\dots,\mathbf{A}_{ii,N_{T}-1}),(37)

the local implicit coefficient matrix can be algebraically expanded as:𝐈+Δ​τ​(𝐄⊗𝐈q)+Δ​τ​𝐀i​i=(𝐈+Δ​τ​(𝐄⊗𝐈q))​(𝐈+Δ​τ​𝐀i​i)−(Δ​τ)2​(𝐄⊗𝐈q)​𝐀i​i.\mathbf{I}+\Delta\tau(\mathbf{E}\otimes\mathbf{I}_{q})+\Delta\tau\mathbf{A}_{ii}=\big(\mathbf{I}+\Delta\tau(\mathbf{E}\otimes\mathbf{I}_{q})\big)\big(\mathbf{I}+\Delta\tau\mathbf{A}_{ii}\big)-(\Delta\tau)^{2}(\mathbf{E}\otimes\mathbf{I}_{q})\mathbf{A}_{ii}.(38)

Because the last term on the right-hand side of the above equation is of second order in pseudo-time, it introduces minimal factorization error during the iterative relaxation. More importantly, since it operates directly on the state incrementΔ​𝐐i\Delta\mathbf{Q}_{i}, this term strictly vanishes as the system converges toward the exact RF-periodic steady state. Therefore, it can be safely neglected without compromising the final converged solution, successfully decoupling the local implicit coefficient matrix into a product of distinct temporal and spatial structures:𝐈+Δ​τ​(𝐄⊗𝐈q)+Δ​τ​𝐀i​i≈(𝐈+Δ​τ​(𝐄⊗𝐈q))​(𝐈+Δ​τ​𝐀i​i).\mathbf{I}+\Delta\tau(\mathbf{E}\otimes\mathbf{I}_{q})+\Delta\tau\mathbf{A}_{ii}\approx\big(\mathbf{I}+\Delta\tau(\mathbf{E}\otimes\mathbf{I}_{q})\big)\big(\mathbf{I}+\Delta\tau\mathbf{A}_{ii}\big).(39)

Through this approximate factorization, the monolithic system can be decomposed into two sequential and decoupled relaxation stages executed at each pseudo-time step, as schematically illustrated in Fig.1.Figure 1:Schematic illustration of the spatio-temporal decoupling strategy in the time-domain harmonic balance solver.

## Stage 1: Spatial Block-Implicit Relaxation

The first stage evaluates the spatial operator to solve the spatial and chemical coupling, yielding an intermediate state correctionΔ​𝐐∗\Delta\mathbf{Q}^{*}:(𝐈+Δ​τ​𝐀i​i)​Δ​𝐐i∗−Δ​τVi​∑j∈𝒩​(i)∂𝐑iphys∂𝐐j​Δ​𝐐j∗=Δ​τVi​𝐆is.\big(\mathbf{I}+\Delta\tau\mathbf{A}_{ii}\big)\Delta\mathbf{Q}_{i}^{*}-\frac{\Delta\tau}{V_{i}}\sum_{j\in\mathcal{N}(i)}\frac{\partial\mathbf{R}_{i}^{\text{phys}}}{\partial\mathbf{Q}_{j}}\Delta\mathbf{Q}_{j}^{*}=\frac{\Delta\tau}{V_{i}}\mathbf{G}_{i}^{s}.(40)

Crucially, because the spatial-chemical Jacobian𝐀i​i\mathbf{A}_{ii}involves no temporal cross-coupling, all temporal collocation points are completely decoupled in this stage. This allows the local spatial system to be solved independently for each temporal collocation pointmmvia a relaxation sweep. For celliiat a specific collocation pointmm, the local update equations during the forward and backward spatial sweeps are reduced to:Di,m​Δ​𝐐i,m∗∗=Δ​τVi​𝐆i,ms−Δ​τVi​∑j<iLi​j,m​Δ​𝐐j,m∗∗,D_{i,m}\Delta\mathbf{Q}_{i,m}^{**}=\frac{\Delta\tau}{V_{i}}\mathbf{G}_{i,m}^{s}-\frac{\Delta\tau}{V_{i}}\sum_{j<i}L_{ij,m}\Delta\mathbf{Q}_{j,m}^{**},(41)Di,m​Δ​𝐐i,m∗=Di,m​Δ​𝐐i,m∗∗−Δ​τVi​∑j>iUi​j,m​Δ​𝐐j,m∗,D_{i,m}\Delta\mathbf{Q}_{i,m}^{*}=D_{i,m}\Delta\mathbf{Q}_{i,m}^{**}-\frac{\Delta\tau}{V_{i}}\sum_{j>i}U_{ij,m}\Delta\mathbf{Q}_{j,m}^{*},(42)

whereLLandUUare the exact spatial lower and upper neighbor Jacobian matrices.

To avoid the high computational and storage costs of assembling exact spatial flux Jacobians while maintaining strong diagonal dominance, the exact local operator𝐀i​i,m\mathbf{A}_{ii,m}is robustly approximated. The resulting local diagonal preconditioning blockDi,mD_{i,m}is constructed as a compactNq×NqN_{q}\times N_{q}matrix:Di,m=𝐈q+Δ​τ​diag⁡(λe,i,m,λi,i,m,λ∗,i,m,λε,i,m)−Δ​τ​𝐉chem,i,m+𝐃damp,i,m.D_{i,m}=\mathbf{I}_{q}+\Delta\tau\operatorname{diag}(\lambda_{e,i,m},\lambda_{i,i,m},\lambda_{*,i,m},\lambda_{\varepsilon,i,m})-\Delta\tau\mathbf{J}_{{\rm chem},i,m}+\mathbf{D}_{{\rm damp},i,m}.(43)

The transport spectral radiiλs,i,m\lambda_{s,i,m}are conservatively evaluated over all boundary facesf∈∂Ωif\in\partial\Omega_{i}based on local drift-diffusion velocities:λs,i,m\displaystyle\lambda_{s,i,m}≈∑f∈∂ΩiAfVi​(12​μs​|𝐄f,m|+cD​Dq|Δ​𝐫f|),(q=e,i,∗),\displaystyle\approx\sum_{f\in\partial\Omega_{i}}\frac{A_{f}}{V_{i}}\left(\frac{1}{2}\mu_{s}|\mathbf{E}_{f,m}|+c_{D}\frac{D_{q}}{|\Delta\mathbf{r}_{f}|}\right),\quad(q=e,i,*),(44a)λε,i,m\displaystyle\lambda_{\varepsilon,i,m}≈∑f∈∂ΩiAfVi​(56​μe​|𝐄f,m|+53​cD​De|Δ​𝐫f|),\displaystyle\approx\sum_{f\in\partial\Omega_{i}}\frac{A_{f}}{V_{i}}\left(\frac{5}{6}\mu_{e}|\mathbf{E}_{f,m}|+\frac{5}{3}c_{D}\frac{D_{e}}{|\Delta\mathbf{r}_{f}|}\right),(44b)

wherecDc_{D}is a numerical diffusion scaling constant, and|Δ​𝐫f||\Delta\mathbf{r}_{f}|is the characteristic distance between neighboring cell centers. Concurrently, to eliminate severe numerical noise and oscillatory derivatives during the relaxation sweeps, the highly sensitive reaction rate coefficients (e.g.,kion,kexck_{\rm ion},k_{\rm exc}) are kept frozen as local constants during the analytical differentiation of the source vector. For the specific multi-moment plasma system, the symbolic structure of this frozen-rate chemistry Jacobian block is formulated as:𝐉chem,i,m=∂𝐒i,m∂𝐐i,m|frozen​k=[∂Se∂ne∂Se∂ni∂Se∂n∗∂Se∂εe∂Si∂ne∂Si∂ni∂Si∂n∗∂Si∂εe∂S∗∂ne∂S∗∂ni∂S∗∂n∗∂S∗∂εe∂Sε∂ne∂Sε∂ni∂Sε∂n∗∂Sε∂εe]i,m,frozen​k,\mathbf{J}_{{\rm chem},i,m}=\left.\frac{\partial\mathbf{S}_{i,m}}{\partial\mathbf{Q}_{i,m}}\right|_{\text{frozen }k}=\begin{bmatrix}\frac{\partial S_{e}}{\partial n_{e}}&\frac{\partial S_{e}}{\partial n_{i}}&\frac{\partial S_{e}}{\partial n_{*}}&\frac{\partial S_{e}}{\partial\varepsilon_{e}}\\
\frac{\partial S_{i}}{\partial n_{e}}&\frac{\partial S_{i}}{\partial n_{i}}&\frac{\partial S_{i}}{\partial n_{*}}&\frac{\partial S_{i}}{\partial\varepsilon_{e}}\\
\frac{\partial S_{*}}{\partial n_{e}}&\frac{\partial S_{*}}{\partial n_{i}}&\frac{\partial S_{*}}{\partial n_{*}}&\frac{\partial S_{*}}{\partial\varepsilon_{e}}\\
\frac{\partial S_{\varepsilon}}{\partial n_{e}}&\frac{\partial S_{\varepsilon}}{\partial n_{i}}&\frac{\partial S_{\varepsilon}}{\partial n_{*}}&\frac{\partial S_{\varepsilon}}{\partial\varepsilon_{e}}\end{bmatrix}_{i,m,\text{frozen }k},(45)

where the partial derivatives of the source vector with respect to conservative variables are analytically evaluated. Under this frozen-rate assumption, representative non-zero Jacobian entries for the electron volumetric source and energy sink terms elegantly simplify to:∂Se,i,m∂ne,i,m\displaystyle\frac{\partial S_{e,i,m}}{\partial n_{e,i,m}}≈kion​Ng+ksi​n∗,i,m,\displaystyle\approx k_{\rm ion}N_{g}+k_{\rm si}n_{*,i,m},(46a)∂Sε,i,m∂ne,i,m\displaystyle\frac{\partial S_{\varepsilon,i,m}}{\partial n_{e,i,m}}≈−∑jΔ​ℰj​(∂Sj,i,m∂ne,i,m|frozen​k).\displaystyle\approx-\sum_{j}\Delta\mathcal{E}_{j}\left(\left.\frac{\partial S_{j,i,m}}{\partial n_{e,i,m}}\right|_{\text{frozen }k}\right).(46b)

The remaining non-zero elements in𝐉chem,i,m\mathbf{J}_{{\rm chem},i,m}are derived in an identical analytical manner. To enforce diagonal dominance and guarantee numerical stability under extreme chemical transients, a diagonal damping matrix𝐃damp,i,m\mathbf{D}_{{\rm damp},i,m}is explicitly added, whose entries are proportional to the absolute row sums of𝐉chem,i,m\mathbf{J}_{{\rm chem},i,m}.

## Stage 2: Variable-Decoupled Temporal Relaxation

Once the spatial intermediate correctionΔ​𝐐i∗\Delta\mathbf{Q}_{i}^{*}is obtained, the second stage accounts for the dense temporal coupling by solving the remaining temporal factor within each independent control volume:(𝐈+Δ​τ​(𝐄⊗𝐈q))​Δ​𝐐i=Δ​𝐐i∗.\big(\mathbf{I}+\Delta\tau(\mathbf{E}\otimes\mathbf{I}_{q})\big)\Delta\mathbf{Q}_{i}=\Delta\mathbf{Q}_{i}^{*}.(47)

A pivotal computational attribute of this step is that the time spectral operator𝐄\mathbf{E}acts exclusively across the temporal collocation points and introduces no cross-coupling between different fluid variables. Consequently, this multi-variable temporal block system can be segregated intoNqN_{q}independent scalar systems. For each distinct fluid variableq∈{ne,ni,n∗,εe}q\in\{n_{e},n_{i},n_{*},\varepsilon_{e}\}, the time spectral coupling is resolved by a localized dense matrix inversion:(𝐈NT+Δ​τ​𝐄)​Δ​𝐐i,q=Δ​𝐐i,q∗,\left(\mathbf{I}_{N_{T}}+\Delta\tau\mathbf{E}\right)\Delta\mathbf{Q}_{i,q}=\Delta\mathbf{Q}_{i,q}^{*},(48)

where𝐈NT\mathbf{I}_{N_{T}}is theNT×NTN_{T}\times N_{T}identity matrix. This variable-by-variable segregation drops the local temporal inversion cost from a monolithic𝒪​((Nq​NT)3)\mathcal{O}((N_{q}N_{T})^{3})down toNq×𝒪​(NT3)N_{q}\times\mathcal{O}(N_{T}^{3}). Finally, the local physical state is advanced using a dynamic relaxation limiter to guarantee strictly positive species densities and energies:𝐐is+1=𝐐is+α​Δ​𝐐i,\mathbf{Q}_{i}^{s+1}=\mathbf{Q}_{i}^{s}+\alpha\Delta\mathbf{Q}_{i},(49)

whereα∈(0,1]\alpha\in(0,1]is a specified damping factor to prevent non-physical solutions.

## 2.5Temporally Decoupled Semi-Implicit Poisson Update

Solving Poisson’s equation decoupled from the charged-particle transport often imposes a severe dielectric-relaxation pseudo-time step limit, leading to weak electrostatic coupling and numerical instability. To alleviate this issue and ensure robust convergence within the time-domain HB framework, we employ a semi-implicit correction, following the approaches established in[13,15,25]. This method anticipates the fast electron number density response to potential variations over the pseudo-time stepΔ​τi\Delta\tau_{i}.

To construct this semi-implicit operator, the implicit treatment is exclusively applied to the electron drift term during the prediction step. Concurrently, the electron diffusion is evaluated explicitly, and the chemical reaction source terms are neglected. Letssdenote the pseudo-time iteration step. By evaluating the mobility and electron density at the known iteration stepss, the implicit drift flux at a specific temporal collocation pointmmis approximated as𝚪e,ms+1≈−μe​ne,ms​𝐄ms+1=μe​ne,ms​∇ϕms+1.\bm{\Gamma}_{e,m}^{s+1}\approx-\mu_{e}n_{e,m}^{s}\mathbf{E}_{m}^{s+1}=\mu_{e}n_{e,m}^{s}\nabla\phi_{m}^{s+1}.(50)

Substituting this predicted flux into the electron continuity equation and subsequently into Poisson’s equation yields the augmented semi-implicit continuous operator:−∇⋅(ϵ0​∇ϕms+1)−∇⋅(e​μe​ne,ms​Δ​τi​∇ϕms+1)=e​(ni,ms−ne,ms)+𝒟e,ms,-\nabla\cdot\left(\epsilon_{0}\nabla\phi_{m}^{s+1}\right)-\nabla\cdot\left(e\mu_{e}n_{e,m}^{s}\Delta\tau_{i}\nabla\phi_{m}^{s+1}\right)=e(n_{i,m}^{s}-n_{e,m}^{s})+\mathcal{D}_{e,m}^{s},(51)

where𝒟e,ms=−e​Δ​τi​∇⋅(De​∇ne,ms)\mathcal{D}_{e,m}^{s}=-e\Delta\tau_{i}\nabla\cdot\left(D_{e}\nabla n_{e,m}^{s}\right)represents the explicit electron diffusion contribution.

A unique property of the electrostatic Poisson’s equation in the HB formulation is the inherent absence of a physical time derivative. Consequently, the time spectral operator𝐄\mathbf{E}does not couple the electric potential across different temporal collocation points. The Poisson system is naturally block-diagonal, allowing the elliptic equation to be solved completely independently at each temporal collocation pointmm.

Integrating Eq. (51) over a control volumeΩi\Omega_{i}yields the discrete, decoupled finite-volume update for celliiat a specific temporal collocation pointmm:∑f∈∂Ωi\displaystyle\sum_{f\in\partial\Omega_{i}}ϵeff,f,m​Af|Δ​𝐫f|​(ϕi,ms+1−ϕn​b,ms+1)\displaystyle\epsilon_{{\rm eff},f,m}\frac{A_{f}}{|\Delta\mathbf{r}_{f}|}\left(\phi_{i,m}^{s+1}-\phi_{nb,m}^{s+1}\right)=e​(ni,i,ms−ne,i,ms)​Vi−e​Δ​τi​De​∑f∈∂ΩiAf​(∇ne)f,ms⋅𝐧f,\displaystyle=e(n_{i,i,m}^{s}-n_{e,i,m}^{s})V_{i}-e\Delta\tau_{i}D_{e}\sum_{f\in\partial\Omega_{i}}A_{f}(\nabla n_{e})_{f,m}^{s}\cdot\mathbf{n}_{f},(52)

where subscriptn​bnbdenotes the adjacent neighbor cell (or boundary face) sharing faceff, and|Δ​𝐫f||\Delta\mathbf{r}_{f}|is the characteristic distance. To maintain accuracy on distorted elements, the face-normal potential gradients in Eq. (52) are further corrected by incorporating non-orthogonal cross-diffusion terms.

Through this formulation, the original Laplacian operator is mathematically augmented by an effective face permittivity:ϵeff,f,m=ϵ0+e​μe​ne,f,ms​Δ​τi.\epsilon_{{\rm eff},f,m}=\epsilon_{0}+e\mu_{e}n_{e,f,m}^{s}\Delta\tau_{i}.(53)

In the algorithmic workflow, the electric potential is not advanced simultaneously with the fluid variables. Instead, this decoupled Poisson system is solved immediately after the macroscopic variables are updated via the spatial and temporal relaxation processes (Stages 1 and 2). Once the new potentialϕms+1\phi_{m}^{s+1}is obtained independently across all temporal collocation points, the local electric field is strictly recomputed before evaluating the transport fluxes for the next pseudo-time step.

## 2.6Boundary Conditions

To complete the physical model and close the semi-discrete finite-volume system, physically consistent boundary conditions must be specified at the solid electrodes. In the present formulation, the electrostatic potential is imposed via Dirichlet boundary conditions, while the transport equations for charged particles and electron energy are closed through wall-flux boundary conditions. All boundary states are evaluated independently at each temporal collocation pointmm.

For the present RF capacitively coupled discharge, the powered electrode is driven by a prescribed sinusoidal voltage. At a specific temporal collocation pointtmt_{m}, the boundary potential is given by:ϕp,m=VRF​sin⁡(2​π​fRF​tm+φ0),\phi_{{\rm p},m}=V_{\rm RF}\sin\left(2\pi f_{\rm RF}t_{m}+\varphi_{0}\right),(54)

whereVRFV_{\rm RF}is the peak voltage amplitude,fRFf_{\rm RF}is the driving frequency, andφ0\varphi_{0}is the phase shift. The grounded electrode is fixed at a constant reference potentialϕg,m=0.\phi_{{\rm g},m}=0.(55)

Driven predominantly by the strong sheath electric field, ions are accelerated toward the wall. The theoretical drift-driven ion flux at the boundary is given by:𝚪i,m⋅𝐧w=μi​ni,m​𝐄m⋅𝐧w,\bm{\Gamma}_{i,m}\cdot\mathbf{n}_{w}=\mu_{i}n_{i,m}\mathbf{E}_{m}\cdot\mathbf{n}_{w},(56)

where𝐧w\mathbf{n}_{w}is the outward unit normal vector pointing from the plasma domain to the wall. In the actual numerical implementation, to prevent unphysical inward ion drift during highly transient iterative steps, a pure upwind condition is enforced by limiting this flux to non-negative values, i.e.,𝚪i,m⋅𝐧w=max⁡(𝚪i,m⋅𝐧w,0).\bm{\Gamma}_{i,m}\cdot\mathbf{n}_{w}=\max(\bm{\Gamma}_{i,m}\cdot\mathbf{n}_{w},0).(57)

For the electron and electron energy fluxes, the physical treatment at the wall depends heavily on the thermal assumptions. In this work, two distinct sets of flux boundary conditions are implemented within the time-spectral framework to accommodate different benchmarking requirements:

## 1. Prescribed Wall Temperature

The first set assumes an energy-independent electron flux, typically associated with a prescribed constant electron temperature at the wall[17]. The macroscopic electron loss is modeled using a constant surface recombination velocity:𝚪e,m⋅𝐧w=ks​ne,m−γ​(𝚪i,m⋅𝐧w),\bm{\Gamma}_{e,m}\cdot\mathbf{n}_{w}=k_{s}n_{e,m}-\gamma(\bm{\Gamma}_{i,m}\cdot\mathbf{n}_{w}),(58)

whereksk_{s}is the effective electron surface recombination coefficient (assuming a unity sticking coefficient) andγ\gammais the secondary electron emission (SEE) coefficient. Because the flux does not depend on the local energy, the electron energy equation must be closed by explicitly specifying a Dirichlet boundary condition based on the prescribed wall temperatureTe,wT_{e,w}:εe,w,m=32​ne,m​kB​Te,w.\varepsilon_{e,w,m}=\frac{3}{2}n_{e,m}k_{B}T_{e,w}.(59)

## 2. Zero-Gradient Temperature Extrapolation

The second set introduces electron energy dependence derived from kinetic theory, assuming the electron temperature at the boundary is extrapolated from the adjacent interior cell (i.e., a zero-gradient condition forTeT_{e})[21]. The macroscopic electron loss rate is governed by the thermal flux of a half-Maxwellian distribution:𝚪e,m⋅𝐧w=14​ne,m​(8​kB​Te,mπ​me)1/2−γ​(𝚪i,m⋅𝐧w),\bm{\Gamma}_{e,m}\cdot\mathbf{n}_{w}=\frac{1}{4}n_{e,m}\left(\frac{8k_{B}T_{e,m}}{\pi m_{e}}\right)^{1/2}-\gamma(\bm{\Gamma}_{i,m}\cdot\mathbf{n}_{w}),(60)

whereTe,mT_{e,m}is the locally extrapolated electron temperature, andmem_{e}is the electron mass. Consistent with this particle flux, the transported electrons carry their respective mean thermal energies to the wall. The corresponding electron energy boundary flux is robustly evaluated as:𝚪ε,m⋅𝐧w=53​ε¯e,m​[14​ne,m​(8​kB​Te,mπ​me)1/2−γ​(𝚪i,m⋅𝐧w)].\bm{\Gamma}_{\varepsilon,m}\cdot\mathbf{n}_{w}=\frac{5}{3}\bar{\varepsilon}_{e,m}\left[\frac{1}{4}n_{e,m}\left(\frac{8k_{B}T_{e,m}}{\pi m_{e}}\right)^{1/2}-\gamma(\bm{\Gamma}_{i,m}\cdot\mathbf{n}_{w})\right].(61)

## 3Numerical Setups and Results

To comprehensively evaluate the solution accuracy and computational efficiency of the proposed time-domain HB method, a representative RF-CCP benchmark is investigated. The computed macroscopic fluid solutions are systematically compared against both a well-established reference solution and the time-marching results performed within the same unified finite-volume framework.

## 3.1Physical Model and Numerical Configuration

The proposed time-domain HB method is evaluated using a standard one-dimensional, parallel-plate RF CCP benchmark. A schematic diagram of the discharge configuration is illustrated in Fig.2. The plasma reactor is bounded by a powered RF electrode on the left and a grounded electrode on the right, filled with neutral argon gas. As depicted, the discharge gap is macroscopically characterized by a central quasi-neutral bulk plasma region enclosed by two oscillating space-charge sheaths adjacent to the electrodes. Because the transverse dimensions of the electrodes are assumed to be infinitely large compared to the gap distance, radial edge effects can be safely neglected. Consequently, the plasma distribution can be treated as one-dimensional along the axial direction.Figure 2:Schematic diagram of the one-dimensional RF CCP discharge configuration.

The geometric parameters and macroscopic operating conditions are summarized in Table1.Table 1:Geometric parameters and operating conditions for the argon CCP benchmark.ParameterSymbolUnitValueInterelectrode distanceLLm\mathrm{m}0.02540.0254Background gas pressureppTorr\mathrm{Torr}11Gas temperatureTgT_{g}K\mathrm{K}300300Neutral gas densityNgN_{g}m−3\mathrm{m^{-3}}3.22×10223.22\times 10^{22}RF frequencyffMHz\mathrm{MHz}13.5613.56RF voltage amplitudeV0V_{0}V\mathrm{V}100100

The one-dimensional computational domain is discretized using a nonuniform symmetric mesh comprisingNp=91N_{p}=91nodes, yielding 90 cells. To adequately resolve the steep spatial gradients within the sheath regions, the node coordinatesxix_{i}are densely clustered near both electrodes. Following the reference benchmark[17], the grid distribution is mathematically defined as:xi=Lx2​[i−1(Np−1)/2]2,i=1,…,Np−12+1,xNp−i+1=Lx−xi,i=1,…,Np−12+1.\begin{gathered}x_{i}=\frac{L_{x}}{2}\left[\frac{i-1}{(N_{p}-1)/2}\right]^{2},\qquad i=1,\ldots,\frac{N_{p}-1}{2}+1,\\
x_{N_{p}-i+1}=L_{x}-x_{i},\qquad i=1,\ldots,\frac{N_{p}-1}{2}+1.\end{gathered}(62)

At the physical boundaries, a sinusoidal driving voltage is applied to the left powered electrode. For each discrete temporal collocation pointmm, the boundary potential is explicitly given by:ϕp,m=V0​sin⁡(2​π​f​tm),\phi_{{\rm p},m}=V_{0}\sin(2\pi ft_{m}),(63)

and the right grounded electrode remains fixed atϕg,m=0\phi_{\mathrm{g},m}=0. For the charged particle transport, the wall electron temperature is explicitly prescribed to evaluate the surface fluxes. The drift-diffusion transport of electrons and ions is governed by their respective mobilities and diffusivities, which are assumed to be inversely proportional to the neutral gas number densityNgN_{g}. The relevant transport coefficients, surface boundary parameters, and reaction thresholds are listed in Table2.Table 2:Transport coefficients, surface boundary parameters, and reaction threshold energies.ParameterSymbolUnitValueElectron diffusivity productNg​DeN_{g}D_{e}m−1​s−1\mathrm{m^{-1}\,s^{-1}}3.86×10243.86\times 10^{24}Electron mobility productNg​μeN_{g}\mu_{e}V−1​m−1​s−1\mathrm{V^{-1}\,m^{-1}\,s^{-1}}9.66×10239.66\times 10^{23}Ion diffusivity productNg​DiN_{g}D_{i}m−1​s−1\mathrm{m^{-1}\,s^{-1}}2.07×10202.07\times 10^{20}Ion mobility productNg​μiN_{g}\mu_{i}V−1​m−1​s−1\mathrm{V^{-1}\,m^{-1}\,s^{-1}}4.65×10214.65\times 10^{21}Wall electron temperatureTe,wT_{e,w}eV\mathrm{eV}0.5Secondary emission coefficientγ\gamma−-0.01Surface recombination velocityksk_{s}m/s\mathrm{m/s}1.19×1051.19\times 10^{5}Ionization threshold energyΔ​εion\Delta\varepsilon_{\mathrm{ion}}eV\mathrm{eV}15.715.7Excitation threshold energyΔ​εexc\Delta\varepsilon_{\mathrm{exc}}eV\mathrm{eV}11.5611.56

Within the HB framework, the reaction rates are evaluated discretely and independently at each temporal collocation pointmm. Therefore, the reaction rates are expressed as:Rion,m\displaystyle R_{\mathrm{ion},m}=Ng​ne,m​kion​(ε¯e,m),\displaystyle=N_{g}n_{e,m}k_{\mathrm{ion}}(\bar{\varepsilon}_{e,m}),(64)Rexc,m\displaystyle R_{\mathrm{exc},m}=Ng​ne,m​kexc​(ε¯e,m).\displaystyle=N_{g}n_{e,m}k_{\mathrm{exc}}(\bar{\varepsilon}_{e,m}).(65)

In these expressions, the local mean electron energy density at temporal collocation pointmmis explicitly defined as:ε¯e,m=εe,mne,m​e.\bar{\varepsilon}_{e,m}=\frac{\varepsilon_{e,m}}{n_{e,m}e}.(66)

Utilizing this local mean energy, the corresponding rate coefficientskionk_{\mathrm{ion}}andkexck_{\mathrm{exc}}are logarithmically interpolated from the exact tabular data established in the reference benchmark[17].

In the present study, two primary electron-impact reactions are considered. Consequently, direct ionization acts as the sole particle source:Se,m=Si,m=Rion,m,S_{e,m}=S_{i,m}=R_{\mathrm{ion},m},(67)

while both reactions contribute to the inelastic electron energy loss. The total energy sink at each temporal collocation point is formulated as:Sε,m=−Δ​εion​Rion,m−Δ​εexc​Rexc,m,S_{\varepsilon,m}=-\Delta\varepsilon_{\mathrm{ion}}R_{\mathrm{ion},m}-\Delta\varepsilon_{\mathrm{exc}}R_{\mathrm{exc},m},(68)

where the threshold energiesΔ​εion\Delta\varepsilon_{\mathrm{ion}}andΔ​εexc\Delta\varepsilon_{\mathrm{exc}}have been explicitly listed in Table2.

## 3.2Establishment of the Time-Marching Reference Solution

Before the dual-time stepping solution is employed as the reference for assessing the HB results, the convergence of the pseudo-time iterations must first be examined. Although the physical time step in the dual-time formulation is not restricted by the stability condition of equation system, an insufficiently converged inner solution introduces an additional iterative error into the physical-time update. The influence of the pseudo-CFL number and the required number of inner iterations is therefore evaluated at a representative physical time stepΔ​t=T/100\Delta t=T/100. To assess the convergence of the inner iterations, the normalized backward differentiation formula (BDF) residual, denoted asρs\rho_{s}, is monitored. This metric represents theL2L_{2}-norm of the complete residual vector—encompassing the electron number continuity, ion number continuity, and electron energy equations at thess-th pseudo-time iteration—normalized by its initial value at the start of the physical time step.

Figure3shows that the convergence rate is strongly dependent on the pseudo-CFL number when a relatively small value is used.Figure 3:Convergence of the normalized full BDF residual at a representative physical time step for different pseudo-CFL numbers. The physical time step isΔ​t=T/100\Delta t=T/100.

When the pseudo-CFL number is set to 100, the residual decreases slowly and fails to reach an asymptotic level even after 500 inner iterations. By raising this value to 500 and 1000, the initial reduction of the residual is substantially accelerated. Further increasing the pseudo-CFL number to the range of 5000–20000 yields a rapid drop of roughly 1.5 orders of magnitude within the first few iterations. After this initial sharp decrease, the solution enters a slower relaxation stage.

For pseudo-CFL numbers of 5000 and above, the convergence histories become virtually identical once the initial transient passes. In these cases, the residual settles at a plateau aroundlog10⁡(ρs)≃−2.7\log_{10}(\rho_{s})\simeq-2.7. The solver typically reaches this plateau within 250 to 300 inner iterations, and continuing the process up to 500 iterations yields no improvement. Although the robust implicit formulation allows for a significantly higher stability limit, this consistent asymptotic behavior clearly demonstrates that pushing the pseudo-CFL number beyond 10000 offers no meaningful advantage for the current configuration. Guided by these findings, a pseudo-CFL number of 10000 and a maximum limit of 300 inner iterations per physical time step are selected. These parameters are adopted for the subsequent time-step verification and for the construction of the time-marching reference solution.

With the pseudo-time parameters established, a physical-time-step refinement study is conducted to quantify the temporal discretization error. This step is essential to construct a sufficiently resolved time-marching baseline for evaluating the proposed time-domain HB method. Using the fixed pseudo-time configuration determined above, the temporal resolution is systematically refined by increasing the number of physical time steps per RF cycle asT/Δ​t=50,100,200,and​400T/\Delta t=50,\ 100,\ 200,\ \text{and}\ 400. Because the inner convergence is strictly controlled, the discrepancies among these test cases stem almost entirely from the physical-time integration, which is governed by the second-order backward differentiation formula.

Table3presents the spatially averaged electron number density, ion number density, and electron energy density sampled at the beginning of the converged RF cycle. To quantitatively assess the temporal discretization error, the calculation with the finest resolution (T/Δ​t=400T/\Delta t=400) is adopted as the reference. The relative differences for each macroscopic quantity are evaluated as:Erel​(q)=|⟨q⟩Δ​t−⟨q⟩T/400||⟨q⟩T/400|×100%.E_{\mathrm{rel}}(q)=\frac{\left|\langle q\rangle_{\Delta t}-\langle q\rangle_{T/400}\right|}{\left|\langle q\rangle_{T/400}\right|}\times 100\%.(69)Table 3:Physical-time-step refinement based on the spatially
averaged plasma quantities att/T=0t/T=0of the converged RF period.
Relative differences are calculated using theT/Δ​t=400T/\Delta t=400solution as the reference.T/Δ​tT/\Delta t⟨ne⟩\langle n_{e}\rangleEneE_{n_{e}}⟨ni⟩\langle n_{i}\rangleEniE_{n_{i}}⟨εe⟩\langle\varepsilon_{e}\rangleEεeE_{\varepsilon_{e}}(1015​m−3)(10^{15}\,\mathrm{m}^{-3})(%)(\%)(1015​m−3)(10^{15}\,\mathrm{m}^{-3})(%)(\%)(10−3​J⋅m−3)(10^{-3}\,\mathrm{J\cdot m}^{-3})(%)(\%)503.191456040.47983.318384980.46342.949779790.46241003.179873460.11513.306735290.11072.939572940.11482003.176966520.02363.303825910.02262.936895360.02364003.17621689–3.30307807–2.93620186–

All three spatially averaged quantities converge monotonically as the physical time step is refined. Relative to theT/Δ​t=400T/\Delta t=400benchmark, the differences obtained with the coarsest resolution (T/Δ​t=50T/\Delta t=50) are approximately0.460.46–0.48%0.48\%. These deviations rapidly decrease to approximately0.11%0.11\%forT/Δ​t=100T/\Delta t=100and to less than0.024%0.024\%forT/Δ​t=200T/\Delta t=200. This uniform reduction in error across all three variables confirms that refining the time step smoothly and evenly improves the overall physical accuracy. To rigorously verify whether this consistent error reduction aligns with the theoretical expectations of the applied numerical approach, the observed temporal convergence order,pp, is evaluated using three successively refined solutions:p=log2⁡[|⟨q⟩N−⟨q⟩2​N||⟨q⟩2​N−⟨q⟩4​N|],p=\log_{2}\left[\frac{\left|\langle q\rangle_{N}-\langle q\rangle_{2N}\right|}{\left|\langle q\rangle_{2N}-\langle q\rangle_{4N}\right|}\right],(70)

whereN=T/Δ​tN=T/\Delta trepresents the temporal resolution per RF cycle. Evaluated with the coarser triplet (N=50N=50, 100, and 200), the observed orders fornen_{e},nin_{i}, andεe\varepsilon_{e}are calculated as1.9941.994,2.0022.002, and1.9311.931, respectively. When utilizing the finer triplet (N=100N=100, 200, and 400), these estimates become1.9551.955,1.9601.960, and1.9491.949. All computed values exhibit excellent agreement with the theoretical second-order accuracy of the used temporal discretization.

To offer a visual assessment of the time-step refinement, Fig.4compares the spatial distributions of the electron number density sampled at the beginning of the converged RF cycle.Figure 4:Electron number density distributions at the beginning
of the converged RF period for different physical-time-step
resolutions.

All four solutions yield nearly identical sheath-edge locations near the electrodes. As highlighted by the inset, the remaining temporal discretization error is confined primarily to the bulk-density plateau. The coarsest resolution (T/Δ​t=50T/\Delta t=50) slightly overpredicts the bulk density, whereas the profiles forT/Δ​t=100T/\Delta t=100, 200, and 400 progressively converge. Notably, theT/Δ​t=200T/\Delta t=200and 400 curves are almost indistinguishable across the entire discharge gap, perfectly aligning with the negligible relative difference (under0.024%0.024\%) reported in Table3. Moreover, relaxing the resolution from 400 to 200 steps per cycle cuts the dominant time-marching cost roughly in half, assuming the same number of inner iterations.

Accordingly, the configuration utilizingT/Δ​t=200T/\Delta t=200, a pseudo-CFL number of 10000, andninner=300n_{\mathrm{inner}}=300is selected as the reference DTS baseline. This setup will be used to evaluate both the accuracy and the computational efficiency of the proposed time-domain HB method.

## 3.3A Priori Spectral Analysis and Harmonic Truncation

Before performing the HB calculations, ana priorispectral analysis is conducted to determine the optimal number of harmonics required to accurately resolve the RF CCP dynamics. This preliminary analysis relies on the high-fidelity transient signals extracted directly from the reference DTS baseline established in the preceding section.

To capture the spatiotemporal evolution of the discharge, three representative spatial locations are monitored: the near-left electrode (NLE), the bulk region (BR), and the near-right electrode (NRE). The temporal variations of the electron number density and the electric potential over consecutive RF cycles are illustrated in Fig.6and Fig.6, respectively.Figure 5:Time-domain signals of electron number density at different monitoring points.Figure 6:Time-domain signals of electric potential at different monitoring points.

The time-domain signals reveal that thenen_{e}waveforms at both the NLE and NRE exhibit distinct periodic oscillations. Because these profiles deviate significantly from pure sinusoids, they naturally encompass higher-order harmonic components. Although they experience a phase shift in the time domain, their frequency-domain amplitude spectra remain identical. In contrast, the electron density in the BR stays nearly constant; its signal is dominated almost entirely by the time-averaged component, leaving the harmonic amplitudes virtually at zero. Similarly, because the NRE is strictly grounded (ϕ=0\phi=0), its electric potential inherently carries zero harmonic content. Consequently, the subsequent Fast Fourier Transform (FFT) analysis focuses selectively on the NLE fornen_{e}, and on both the NLE and BR forϕ\phi.

The resulting spectral amplitude distributions, normalized by their respective time-averaged values, are presented in Figs.7–9. The electric potential is composed primarily of low-order harmonics. Specifically, the NLE potential is almost exclusively dominated by the fundamental frequency (NH=1N_{H}=1). The BR potential, however, is influenced by the nonlinear response of the bulk plasma, necessitating the inclusion of both the first and second harmonics (NH=2N_{H}=2). Conversely, driven by the intense dynamics of sheath depletion and expansion, the electron number density at the NLE exhibits a much broader spectral distribution. The FFT spectrum ofnen_{e}demonstrates that the normalized amplitudes decay progressively across the first five harmonics, diminishing to negligible levels from the sixth harmonic onward.Figure 7:Normalized FFT spectrum of potential at NLE.Figure 8:Normalized FFT spectrum of potential at BR.Figure 9:Normalized FFT spectrum of electron number density at NLE.Figure 10:Truncated reconstruction of potential using dominant harmonics.Figure 11:Truncated reconstruction of NLE electron number density usingNH=5N_{H}=5.

To quantitatively verify this frequency truncation, inverse FFT reconstructions are performed using the selected dominant harmonics (Figs.11and11). As expected, truncating atNH=1N_{H}=1for the NLE potential andNH=2N_{H}=2for the BR potential demonstrates excellent agreement with the original time-accurate curves. For the electron number density at the NLE, a reconstruction utilizing the first five harmonics (NH=5N_{H}=5) successfully captures the overall shape and magnitude of the original signal. However, due to the steep temporal gradients within the sheath, localized spurious oscillations remain visible near the density minima. Increasing the number of harmonics toNH=6N_{H}=6effectively suppresses these spurious oscillations, yielding a smooth and faithful reconstruction. Guided by thisa priorispectral analysis, the subsequent implicit time-domain HB computations are systematically evaluated across four harmonic truncation levels:NH=6,8,10N_{H}=6,8,10, and1212.

## 3.4Harmonic Convergence and Accuracy Assessment

To evaluate the numerical performance of the proposed method, the implicit HB computations are performed across four selected harmonic truncation levels (NH=6,8,10N_{H}=6,8,10, and1212). Preliminary computations revealed that employing lower harmonic counts, such asNH=4N_{H}=4or55, inevitably leads to numerical divergence. This instability is primarily triggered by unresolved nonlinear aliasing and spurious numerical oscillations within the highly depleted sheath regions, which quickly destabilize the tightly coupled governing equation system. Therefore,NH=6N_{H}=6establishes the minimum threshold for a stable numerical integration. In the time-domain HB formulation, these selected harmonic counts correspond to resolving the plasma dynamics atNT=2​NH+1N_{T}=2N_{H}+1discrete temporal collocation points (i.e.,NT=13,17,21N_{T}=13,17,21, and2525, respectively) per RF cycle.

Benefiting from the robust implicit relaxation approach, the pseudo-time marching circumvents strict stability restrictions, permitting the use of an aggressive pseudo-CFL number of1000010000(consistent with the previously established baseline). Figure12illustrates the convergence histories of the spatially averaged electron number density at the beginning of the RF cycle as a function of the physical wall-clock time.Figure 12:Convergence histories of the spatially averaged electron number density at the beginning of the RF cycle for different harmonic truncation levels.

As depicted, the macroscopic plasma state rapidly converges to a stable periodic solution. Regardless of the harmonic count, all cases reach an identical converged value of approximately3.179×1015​m−33.179\times 10^{15}~\mathrm{m^{-3}}. This rigorous consistency corroborates the preceding spectral analysis, confirming that retaining only the primary harmonics is sufficient to yield an accurate spatially averaged solution.

To further assess the solution accuracy, the reconstructed profiles of the electric potential, electron number density, electron energy density, and electron temperature sampled at the beginning of the RF cycle are compared in Fig.13.(a)Electric potential (ϕ\phi)(b)Electron density (nen_{e})(c)Electron energy density (εe\varepsilon_{e})(d)Electron temperature (TeT_{e})Figure 13:Spatial distributions of macroscopic plasma properties at the beginning of the RF cycle, reconstructed usingNH=6,8,10N_{H}=6,8,10, and1212.

As shown in Figs.13(a)–13(c), the spatial profiles of the electric potential, electron number density, and electron energy density exhibit excellent agreement across all tested harmonic counts. This consistent behavior demonstrates that the primary transport mechanisms and the overall discharge structure are well captured, even with the lowest selected harmonic count (NH=6N_{H}=6).

However, a minor deviation is visible in the electron temperature profile forNH=6N_{H}=6within the near-wall sheath regions (Fig.13(d)). BecauseTeT_{e}is a derived property computed from the ratio of energy density to particle number density, its calculation is inherently sensitive to minor numerical perturbations in these highly depleted zones. Although the underlying conservative variables (nen_{e}andεe\varepsilon_{e}) remain robust and largely unaffected, a slightly higher harmonic count is preferred to guarantee smooth and artifact-free derived properties.

This requirement for higher accuracy must be carefully weighed against the increased computational cost. Since increasing the harmonic count enlarges the coupled HB system, the computational cost grows accordingly. To provide a fair timing assessment, these tests were executed on a single core of an Intel Core Ultra 9 285H processor. TheNH=6N_{H}=6case achieves full convergence in approximately600600s, whereas the highest-resolution case (NH=12N_{H}=12) doubles this duration to roughly12001200s. To eliminate the minor temperature deviations without incurring the severe computational penalty of higher-order truncations,NH=8N_{H}=8is selected. This configuration strikes an optimal balance between accuracy and efficiency, serving as the verified baseline for the subsequent spatiotemporal analyses.

## 3.5Spatiotemporal Validation of the Time-Domain Harmonic Balance Method

To rigorously validate the proposed time-domain HB method, the spatiotemporal evolutions of the charged particle densities are compared against both the conventional DTS solutions and the widely recognized benchmark data of Lymberopoulos and Economou[17]. To ensure a strict and fair comparison, the DTS results utilized here are generated using the rigorously verified baseline configuration established in the preceding section (T/Δ​t=200T/\Delta t=200andninner=300n_{\mathrm{inner}}=300). Figure14illustrates the spatial distributions of the electron and ion number densities sampled at four equidistant phases of the RF cycle:t/T=0,0.25,0.50t/T=0,0.25,0.50, and0.750.75.(a)Electron density (nen_{e})(b)Ion density (nin_{i})Figure 14:Comparison of spatial distributions of (a) electron number density and (b) ion number density at different phases of the RF cycle among the 1993 reference data, the DTS method, and the proposed time-domain HB method (NH=8N_{H}=8).

As shown in Fig.14, the time-domain HB method captures the dynamic expansion and contraction of the sheath regions with high fidelity, demonstrating excellent agreement with both the time-domain DTS solutions and the benchmark data. In the bulk plasma region, the peak particle number densities computed by the DTS baseline and the proposed HB method exhibit perfect mutual consistency. Both approaches align closely with the 1993 reference, yielding a minor relative deviation of within2%2\%.

This successful validation against the reference data[17]confirms the physical configuration and the overall macroscopic discharge structure. Any minor remaining discrepancies can be reasonably attributed to external factors, such as differences in the spatial discretization schemes, the interpolation of tabulated reaction rates, and temporal integration details absent from the original study. Crucially, these external sources of discrepancy must be clearly distinguished from the internal consistency of the proposed methods; both the HB and DTS solvers employ an identical computational mesh, finite-volume method, chemistry model, and boundary conditions.

However, demonstrating agreement at four isolated phases is insufficient to confirm whether the complete periodic response is accurately reproduced. To address this, the spatiotemporal evolutions computed by the time-domain HB and DTS methods are compared comprehensively throughout the entire RF cycle in Fig.15. The filled contours represent the fully converged DTS baseline (utilizingT/Δ​t=200T/\Delta t=200), while the overlaid white isolines denote the HB solution reconstructed usingNH=8N_{H}=8. To ensure a direct and rigorous evaluation, identical contour levels are applied to both solutions.(a)Electron number density,nen_{e}.(b)Electron energy density,εe\varepsilon_{e}.(c)Electron temperature,TeT_{e}.(d)Electric potential,ϕ\phi.Figure 15:Spatiotemporal comparison between the DTS reference
solution and the HB solution over one RF period. Filled contours
represent the DTS solution withT/Δ​t=200T/\Delta t=200, while the white
isolines represent the reconstructed HB solution withNH=8N_{H}=8.
The spatial and temporal coordinates are normalized asξ=x/L\xi=x/Landt/Tt/T, respectively.

The spatiotemporal evolution of the electron number density (Fig.15(a)) reveals a relatively stationary, high-density bulk plasma bounded by periodically modulated sheaths. The dynamic displacement of the sheath edges is clearly reflected in the pronounced curvature of the near-electrode contours. Across the entire RF cycle, the HB isolines perfectly track the underlying DTS reference, even within zones of steep spatiotemporal gradients, confirming that the truncated harmonic set resolves both the quasi-steady bulk and the highly nonlinear transient sheath dynamics.

Broadly correlated withnen_{e}, the electron energy density (Fig.15(b)) nonetheless exhibits a more pronounced temporal asymmetry. This distinction arises from the complex interplay among field-driven heating, energy transport, and collisional losses. The proposed solver faithfully reproduces the high-energy bulk and the periodic contour deformations near the electrodes, demonstrating that the HB formulation’s high fidelity naturally extends to the full electron-energy balance.

By contrast, the electron temperature (Fig.15(c)) displays distinct characteristics stemming directly from its nature as a derived ratio (Te∝εe/neT_{e}\propto\varepsilon_{e}/n_{e}). While the bulk plasma maintains a narrow temperature band, localized heating maxima alternately emerge near the electrodes during intense sheath excitation. The HB method accurately captures the location, phase, and extent of these heating zones. However, as anticipated, the localized deviations between the two solutions are slightly magnified in the strongly depleted sheaths, where minute numerical differences in the conservative variables are amplified by the division operation. Consequently, the near-wallTeT_{e}profiles inherently warrant a more cautious interpretation than the directly integrated fields.

Finally, the electric potential (Fig.15(d)) is strongly modulated by the applied RF voltage, featuring smooth bulk variations but dynamically emerging steep gradients as the voltage drop alternately redistributes between the sheaths. The excellent alignment between the overlaid isolines and the reference contours confirms that the proposed formulation accurately captures the phase and amplitude of this electrostatic response. Accurately resolvingϕ\phiis of paramount importance; as it governs the drift fluxes and heating terms, the potential acts as the primary driver coupling the macroscopic plasma state across all discrete temporal collocation points.

To complement the visual comparisons with a rigorous quantitative assessment, the volume-weighted spatiotemporal relativeL2L_{2}error is defined as:E2​(q)=[∑m=0Ns−1∑i=1NcVi​(qi,mHB−qi,mDTS)2∑m=0Ns−1∑i=1NcVi​(qi,mDTS)2]1/2,E_{2}(q)=\left[\frac{\displaystyle\sum_{m=0}^{N_{s}-1}\sum_{i=1}^{N_{c}}V_{i}\left(q_{i,m}^{\mathrm{HB}}-q_{i,m}^{\mathrm{DTS}}\right)^{2}}{\displaystyle\sum_{m=0}^{N_{s}-1}\sum_{i=1}^{N_{c}}V_{i}\left(q_{i,m}^{\mathrm{DTS}}\right)^{2}}\right]^{1/2},(71)

whereNs=200N_{s}=200represents the number of distinct temporal phase samples per RF cycle. The normalized mean absolute error (EMAE_{\mathrm{MA}}) is defined analogously as:EMA​(q)=∑m=0Ns−1∑i=1NcVi​|qi,mHB−qi,mDTS|∑m=0Ns−1∑i=1NcVi​|qi,mDTS|.E_{\mathrm{MA}}(q)=\frac{\displaystyle\sum_{m=0}^{N_{s}-1}\sum_{i=1}^{N_{c}}V_{i}\left|q_{i,m}^{\mathrm{HB}}-q_{i,m}^{\mathrm{DTS}}\right|}{\displaystyle\sum_{m=0}^{N_{s}-1}\sum_{i=1}^{N_{c}}V_{i}\left|q_{i,m}^{\mathrm{DTS}}\right|}.(72)

Additionally, the maximum pointwise relative error across the entire spatiotemporal domain is evaluated and denoted asE∞​(q)E_{\infty}(q).Table 4:Quantitative spatiotemporal error metrics of the HB solution (NH=8N_{H}=8) evaluated against the fully converged DTS baseline (T/Δ​t=200T/\Delta t=200).VariableE2E_{2}(%)EMAE_{\mathrm{MA}}(%)E∞E_{\infty}(%)nen_{e}0.2580.2220.392εe\varepsilon_{e}0.2360.2080.371TeT_{e}1.1800.3346.385ϕ\phi0.1670.1750.227

As summarized in Table4, the relativeL2L_{2}and mean absolute errors for the directly integrated variables (nen_{e},εe\varepsilon_{e}, andϕ\phi) are remarkably small, all remaining strictly below0.3%0.3\%. While the maximum pointwise error (E∞E_{\infty}) for the electron temperature reaches approximately6.4%6.4\%, this extreme deviation is strictly confined to the near-wall cells. As previously discussed, this localized peak error is simply a mathematical consequence of dividing two extremely small quantities (εe\varepsilon_{e}andnen_{e}) to calculateTeT_{e}. It does not mean the underlying electron-energy calculation itself is inaccurate. Taken together, the isolated phase-resolved profiles, the complete spatiotemporal distributions, and these comprehensive error metrics conclusively demonstrate that retainingNH=8N_{H}=8harmonics is perfectly sufficient to accurately reproduce the rigorous periodic DTS solution for the present RF discharge.

## 3.6Computational Efficiency Analyses

Unlike conventional physical-time integration, the HB formulation inherently bypasses physical time-step errors, introducing instead harmonic-truncation and nonlinear-aliasing errors. As evidenced by the preceding spatiotemporal validation, these spectral errors remain negligible forNH=8N_{H}=8. Crucially, this high spectral accuracy is achieved while entirely circumventing the exhaustive physical transients required to reach a time-asymptotic periodic state.

Beyond physical fidelity, another advantage of the proposed time-domain HB method lies in its exceptional computational efficiency. Figure16compares the convergence histories of the spatially averaged electron density against the physical wall-clock time for both the DTS and HB methods.Figure 16:Convergence histories of the spatially averaged electron density: a wall-clock time comparison between the time-domain DTS method and the proposed HB method.

The traditional DTS approach dictates resolving the macroscopic evolution over hundreds to thousands of RF cycles before periodic steady-state conditions are met. As depicted, the computational expense of the DTS method scales almost linearly with the temporal resolution: achieving full convergence requires approximately 4344 s, 8643 s, and 17793 s forT/Δ​t=100T/\Delta t=100, 200, and 400, respectively. In stark contrast, the time-domain HB method directly targets the coupled steady-state solution across all temporal collocation points via pseudo-time relaxation.

Executed on a single core of the aforementioned processor, theNH=8N_{H}=8HB configuration reaches deep convergence in merely842.5842.5s. When evaluated against the rigorously verified DTS baseline (T/Δ​t=200T/\Delta t=200), the HB approach delivers an impressive order-of-magnitude acceleration with a10.2610.26-fold speedup. Even when compared to the coarsest DTS setup (T/Δ​t=100T/\Delta t=100), the HB method remains5.165.16times faster. Such a dramatic reduction in computational overhead is achieved on a purely sequential architecture without compromising physical accuracy. This unequivocally highlights the superior algorithmic efficiency and practical utility of the proposed HB framework for RF CCP simulations.

## 4Conclusion

In this study, a time-domain harmonic balance (HB) framework was developed to accelerate the fluid simulation of RF CCPs. This work represents the first successful extension of the time-domain HB method to a fully coupled drift-diffusion-Poisson system incorporating the complete electron-energy balance. To overcome the severe numerical stiffness introduced by this complex energy coupling and the dense time-spectral operator, a robust implicit pseudo-time relaxation method was proposed based on a spatiotemporal operator-splitting strategy. By strictly confining the dense temporal matrix inversion to the local cell level and incorporating a temporally decoupled semi-implicit Poisson update, the solver effectively decoupled the highly nonlinear governing system. This approach avoided the assembly of massive global Jacobian matrices while ensuring strong numerical stability against both chemical stiffness and the strict dielectric relaxation limit.

The proposed framework was rigorously validated against a standard one-dimensional argon CCP benchmark. Spectral analysis and convergence tests demonstrated that retaining eight harmonics (NH=8N_{H}=8) is perfectly sufficient to resolve the periodic RF discharge. Evaluated across all discrete temporal collocation points, the HB solution exhibited excellent agreement with the conventional DTS reference, successfully capturing the quasi-steady bulk plasma and the highly nonlinear transient sheath dynamics. The high fidelity of the proposed formulation naturally extended from the charged-particle continuity equations to the full electron-energy balance, with macroscopic relative errors remaining strictly below0.3%0.3\%.

Beyond physical accuracy, the time-domain HB method demonstrated exceptional computational efficiency. By directly solving for the coupled steady-state variables and completely bypassing the exhaustive physical transients, the proposed solver achieved a greater than 10-fold acceleration compared to the fully converged DTS baseline, and remained over 5 times faster even when compared to the coarsest time-marching setup. Crucially, this dramatic reduction in computational overhead was realized using a purely sequential single-core execution. In summary, this work confirms that the time-domain HB framework provides a high-fidelity, memory-efficient, and computationally superior alternative to conventional time-marching methods, showing tremendous potential for the routine parameter optimization and iterative design of RF plasma reactors.

## Acknowledgments

The current research is supported by National Science Foundation of China (92371107) and Hong Kong research grant council (16208324).

## References
- [1]R. R. Arslanbekov and V. I. Kolobov(2021)Implicit and coupled fluid plasma solver with adaptive cartesian mesh and its applications to non-equilibrium gas discharges.Plasma Sources Science and Technology30(4),pp. 045013.Cited by:§1.
- [2]C. K. Birdsall(1991)Particle-in-cell charged-particle simulations, plus monte carlo collisions with neutral atoms, pic-mcc.IEEE Transactions on plasma science19(2),pp. 65–85.Cited by:§1.
- [3]J. Boeuf(1987)Numerical model of rf glow discharges.Physical review A36(6),pp. 2782.Cited by:§1.
- [4]P. Chabert and N. Braithwaite(2011)Physics of radio-frequency plasmas.Cambridge University Press.Cited by:§1.
- [5]F. F. Chen and J. P. Chang(2003)Lecture notes on principles of plasma processing.Springer Science & Business Media.Cited by:§1.
- [6]M. Davoudabadi, J. S. Shrimpton, and F. Mashayek(2009)On accuracy and performance of high-order finite volume methods in local mean energy model of non-thermal plasmas.Journal of Computational Physics228(7),pp. 2468–2479.Cited by:§1.
- [7]V. A. Godyak and N. Sternberg(1990)Dynamic model of the electrode sheaths in symmetrically driven rf discharges.Physical Review A42(4),pp. 2299.Cited by:§1.
- [8]A. D. Gomez, N. Deak, and F. Bisetti(2023)Jacobian-free newton–krylov method for the simulation of non-thermal plasma discharges with high-order time integration and physics-based preconditioning.Journal of Computational Physics480,pp. 112007.Cited by:§1.
- [9]A. Gopinath and A. Jameson(2005)Time spectral method for periodic unsteady computations over two-and three-dimensional bodies.In43rd AIAA aerospace sciences meeting and exhibit,pp. 1220.Cited by:§1.
- [10]G. J. M. Hagelaar(2000)Modeling of microdischarges for display technology.Cited by:§1.
- [11]K. C. Hall, K. Ekici, J. P. Thomas, and E. H. Dowell(2013)Harmonic balance methods applied to computational fluid dynamics problems.International Journal of Computational Fluid Dynamics27(2),pp. 52–67.Cited by:§1.
- [12]K. C. Hall, J. P. Thomas, and W. S. Clark(2002)Computation of unsteady nonlinear flows in cascades using a harmonic balance technique.AIAA journal40(5),pp. 879–886.Cited by:§1.
- [13]M. J. Kushner(2009)Hybrid modelling of low temperature plasmas for fundamental investigations and equipment design.Journal of Physics D: Applied Physics42(19),pp. 194013.Cited by:§1,§2.5.
- [14]A. LaBryer and P. Attar(2009)Modeling the nonlinear structural dynamics of a plunging membrane airfoil using a high dimensional harmonic balance approach.In50th AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference 17th AIAA/ASME/AHS Adaptive Structures Conference 11th AIAA No,pp. 2474.Cited by:§1.
- [15]J. Li, M. Zhao, Y. Zhang, F. Gao, and Y. Wang(2025)Fast simulation strategy for capacitively-coupled plasmas based on fluid model.Computer Physics Communications307,pp. 109392.Cited by:§2.5.
- [16]M. A. Lieberman and A. J. Lichtenberg(1994)Principles of plasma discharges and materials processing.MRS Bulletin30(12),pp. 899–901.Cited by:§1.
- [17]D. P. Lymberopoulos and D. J. Economou(1993)Fluid simulations of glow discharges: effect of metastable atoms in argon.Journal of applied physics73(8),pp. 3668–3679.Cited by:§1,§2.6,§3.1,§3.1,§3.5,§3.5.
- [18]A. P. Matthews(1994)Current advance method and cyclic leapfrog for 2d multispecies hybrid plasma simulations.Journal of Computational Physics112(1),pp. 102–116.Cited by:§1.
- [19]G. Misium, A. Lichtenberg, and M. Lieberman(1989)Macroscopic modeling of radio-frequency plasma discharges.Journal of Vacuum Science & Technology A: Vacuum, Surfaces, and Films7(3),pp. 1007–1013.Cited by:§1.
- [20]G. S. Oehrlein and S. Hamaguchi(2018)Foundations of low-temperature plasma enhanced materials synthesis and etching.Plasma Sources Science and Technology27(2),pp. 023001.Cited by:§1.
- [21]Y. Sakiyama and D. B. Graves(2006)Corona-glow transition in the atmospheric pressure rf-excited plasma needle.Journal of Physics D: Applied Physics39(16),pp. 3644–3652.Cited by:§2.6.
- [22]S. Sharma(2013)Investigation of ion and electron kinetic phenomena in capacitively coupled radio-frequency plasma sheaths: a simulation study.Ph.D. Thesis.Cited by:§1.
- [23]M. Surendra and D. B. Graves(1991)Particle simulations of radio-frequency glow discharges.IEEE transactions on plasma science19(2),pp. 144–157.Cited by:§1.
- [24]J. Trieschmann, L. Vialetto, and T. Gergs(2023)Machine learning for advancing low-temperature plasma modeling and simulation.Journal of Micro/Nanopatterning, Materials, and Metrology22(4),pp. 041504–041504.Cited by:§1.
- [25]P. L. Ventzek, T. J. Sommerer, R. J. Hoekstra, and M. J. Kushner(1993)Two-dimensional hybrid model of inductively coupled plasma sources for etching.Applied physics letters63(5),pp. 605–607.Cited by:§2.5.
- [26]H. Wu, M. Yang, D. Wang, and X. Huang(2024)Efficient forced response minimization using a full-viscosity discrete adjoint harmonic balance method.AIAA Journal62(10),pp. 3644–3661.Cited by:§1.
- [27]Z. Yan, H. Dai, Q. Wang, and S. N. Atluri(2023)Harmonic balancemethods: a review and recent developments.Cited by:§1.
- [28]D. B. Zulevic, S. Gautam, S. Sriraman, and A. Venkattraman(2026)Accelerating low-temperature plasma simulations using the harmonic balance method.Journal of Computational Physics,pp. 115027.Cited by:§1.

## 


- 


Major funding support from
