# Approximate Invariant Analysis: An Efficient Framework for Nonlinear Beam Dynamics, Part I: Geometric Approaches of the Poincaré Rotation Number

**arXiv ID**: 2605.12267v1
**Authors**: Yongjun Li, Sergei Nagaitsev, Derong Xu, Yue Hao, Chad Mitchell
**Published**: 2026-05-12
**Categories**: physics.acc-ph, nlin.CD
**Comments**: 5 pages, 6 figures, submitted to IPAC26
**HTML URL**: https://arxiv.org/html/2605.12267v1

## Abstract

We present the first part of an efficient framework for nonlinear beam dynamics, termed Approximate Invariant Analysis (AIA). The framework is based on the construction of approximate invariants~[Y.~Li, D.~Xu, and Y.~Hao, Phys.\ Rev.\ Accel.\ Beams \textbf{28}, 074001 (2025)] and on the extraction of the betatron frequency with the geometric foundations of Poincaré rotation number~[S.~Nagaitsev and T.~Zolkin, Phys.\ Rev.\ Accel.\ Beams \textbf{23}, 054001 (2020)]. The method is demonstrated using the National Synchrotron Light Source~II (NSLS-II) storage ring as an illustrative example.

## Full Text

Approximate Invariant Analysis: An Efficient Framework for Nonlinear Beam Dynamics Part I: Geometric Approaches of the Poincaré Rotation Number

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2605.12267v1 [physics.acc-ph] 12 May 2026††thanks:email: yli@bnl.gov

## Approximate Invariant Analysis: An Efficient Framework for Nonlinear Beam Dynamics
Part I: Geometric Approaches of the Poincaré Rotation NumberYongjun LiIDBrookhaven National Laboratory, Upton, New York 11973, USASergei NagaitsevIDBrookhaven National Laboratory, Upton, New York 11973, USADerong XuIDBrookhaven National Laboratory, Upton, New York 11973, USAYue HaoIDMichigan State University, East Lansing, Michigan 48864, USAChad MitchellIDLawrence Berkeley National Laboratory, Berkeley, California 94720, USA

## Abstract

We present the first part of an efficient framework for nonlinear beam dynamics, termed Approximate Invariant Analysis (AIA). The framework is based on the construction of approximate invariants [Y. Li, D. Xu, and Y. Hao, Phys. Rev. Accel. Beams28, 074001 (2025)] and on the extraction of the betatron frequency with the geometric foundations of Poincaré rotation number [S. Nagaitsev and T. Zolkin, Phys. Rev. Accel. Beams23, 054001 (2020)]. The method is demonstrated using the National Synchrotron Light Source II (NSLS-II) storage ring as an illustrative example.

## IIntroduction

In most existing ring-based particle accelerators, the presence of nonlinear magnets renders the machines non-integrable Hamiltonian systems. Consequently, exact analytical solutions for particle motion are generally unattainable because the system lacks a complete set of conserved quantities. A central goal of single-particle beam dynamics is therefore to assess particles’ long-term stability.

Traditional nonlinear beam-dynamics analysis is usually rooted in Hamiltonian perturbation theory. The linearized beam motion is first parameterized using Courant-Snyder theoryCourant and Snyder (1958). Once stable linear motion is established, nonlinear contributions are treated as perturbations. Common tools for studying nonlinear dynamics include, though are not limited to: (1) classical Hamiltonian perturbation theory, which employs canonical transformations to systematically average out fast oscillatory terms, thereby simplifying the Hamiltonian and highlighting the essential slow dynamicsWilson (1995); and (2) Lie-algebraic methods, which decompose nonlinear perturbations into resonance-driving termsDragt (2011). Such perturbation methods can be extended to high order terms by combining with differential algebraBerz (1991)and normal-formChao (2020)techniques.

Kolmogorov-Arnold-Moser (KAM) theoryKolmogorov (1954); Arnold (1963); Moser (1962)proves that long-term stable motion can persist in the presence of nonlinear perturbations, provided they remain sufficiently small. In such regions – referred to as the dynamic aperture in accelerator physics – quasi-periodic trajectories reside on invariant tori, which, although deformed, continue to inhibit chaotic diffusion. ReferenceLiet al.(2025)presents a method for constructing approximations to the invariant tori using Approximate Invariants (AI), enabling a qualitative assessment of particle stability by examining whether the resulting tori remain closed. Moreover, for a given torus, the associated quasi-constant betatron frequency can be extracted using the Poincaré rotation number (PRN) via a geometric approachNagaitsev and Zolkin (2020). Building on these established foundations, this paper introduces an efficient framework for nonlinear beam dynamics analysis – Approximate Invariant Analysis (AIA) – and demonstrates its application using the National Synchrotron Light Source II (NSLS-II) storage ringDierker (2007).

## IIApproximate invariant

Although the concept of closed orbits is well known, we briefly revisit it for the sake of completeness of the overall framework. In accelerator physics, three types of closed orbits are commonly considered. An ideal transverse closed orbit coincides with the design trajectory, passing through the magnetic centers such that𝐗T=[x,px,y,py]=[0,0,0,0]\mathbf{X}^{T}=[x,p_{x},y,p_{y}]=[0,0,0,0]throughout the entire machine. The construction of approximate invariants (AIs) around the ideal reference orbit has been described in Ref.Liet al.(2025). In the presence of magnetic imperfections and alignment errors, the actual closed orbit, denoted by𝐗co\mathbf{X}_{\mathrm{co}}, deviates from the design trajectory. Furthermore, for an off-momentum particle, a momentum-dependent dispersive closed orbit is superimposed on this distorted orbit. Thus, a realistic closed orbit reads as𝐗c​o​(δ,s)≈𝟎+𝐗c​o​(s)+∑i=1,2,⋯𝐃i​(s)​δi,\mathbf{X}_{co}(\delta,s)\approx\mathbf{0}+\mathbf{X}_{co}(s)+\sum_{i=1,2,\cdots}\mathbf{D}_{i}(s)\delta^{i},(1)

here𝐃i​(s)\mathbf{D}_{i}(s)is theit​hi^{th}-order dispersion vector atss,δ=d​PP0\delta=\frac{\mathrm{d}P}{P_{0}}is the relative momentum deviation111Strictly speaking, in the presence of an RF cavity system operating at a fixed frequency, variations in the closed-orbit path length lead to small changes in the beam momentum.. Dispersive orbits can be obtained through iteration with re-normalized magnet bending or focusing strengths withP=(1+δ)​P0P=(1+\delta)P_{0}. If there exist nonlinear magnets, it usually differs from the linear parameterization as shown in the left subplot of Fig.1. High order dispersions can be obtained by a polynomial fitting as shown in the right subplot, or by implementing a differentiable map tracking.Figure 1:Left: one NSLS-II super-cell’sδ=1.5%\delta=1.5\%dispersive orbit (top) and its derivative (bottom). Solid blue lines include the nonlinear contribution from sextupoles and dash-dotted yellow lines represent the linear part𝐃1\mathbf{D}_{1}. Right: different dispersive orbits observed at the longitudinal locations=0s=0. The first order dispersion is near zero, because the NSLS-II lattice is a linear achromat.

Once a closed orbit is established, one-turn maps in the form of truncated power series (TPS)Berz (1991); Yang (2009); Zhang (2024)can be obtained by tracking particles through the entire ring. Using the method described in Ref.Liet al.(2025), two independent and Poisson-commuting AIs are constructed by computing the eigenvectors of the transpose of the one-turn transfer matrix expressed in square form. These AIs describe a family of (approximately) invariant tori in the transverse phase space(x,px,y,py)(x,p_{x},y,p_{y}). In this paper, we only focus on the AI that predominantly characterizes the horizontal motion in the mid-plane,y=py=0y=p_{y}=0, as a representative example. For clarity, this constitutes a one Degree-of-Freedom (1-DoF) system in a two-dimensional phase space.𝒦=∑m​ncm,n​xm​pxn.\mathcal{K}=\sum_{mn}c_{m,n}x^{m}p_{x}^{n}.(2)

Equation (2) describes a family ofx−pxx-p_{x}contours arising from the intersection of invariant tori with the mid-plane. The closure of these contours provides a qualitative measure of dynamical stability: closed curves (tori) correspond to stable motion, whereas open curves indicate unbounded or unstable trajectories. The outermost torus approximately delineates the boundary of the dynamic aperture. This qualitative stability criterion is further validated by tracking simulations, as illustrated in Fig.2.Figure 2:Contour plot of the horizontal AI of the NSLS-II ring in the mid-plane (solid red curves), overlaid with simulated Poincaré maps comprising 512 iterations. The simulations are shown as black dots for stable trajectories and blue dots for unbounded motion. Closed contours (tori) correspond to stable motion, whereas open contours indicate unbounded trajectories.

## IIIBetatron tune

AIs not only provide a qualitative criterion for dynamical stability, but also enable the extraction of the Betatron frequency using the geometric method proposed in Appendix B of Ref.Nagaitsev and Zolkin (2020)and its erratumNagaitsev and Zolkin (2026). In accelerator physics, this frequency – defined as the number of oscillation cycles completed in one turn – is referred to as the tune. Its fractional part often plays a critical role in determining proximity to resonant conditions. Here, we briefly outline the procedure for extracting the fractional tune using the concept of the rotation number, as defined by the following equation:ν=∫xx′(∂𝒦∂px)−1​dx/∮(∂𝒦∂px)−1​dx=d​J′d​𝒦/d​Jd​𝒦,\nu=\int_{x}^{x^{\prime}}{(\frac{\partial\mathcal{K}}{\partial p_{x}})^{-1}}\mathrm{d}x\bigg/\oint{(\frac{\partial\mathcal{K}}{\partial p_{x}})^{-1}}\mathrm{d}x=\frac{\mathrm{d}J^{\prime}}{\mathrm{d}\mathcal{K}}\bigg/\frac{\mathrm{d}J}{\mathrm{d}\mathcal{K}},(3)

Here, the action integralLichtenberg and Lieberman (2013)J=12​π​∮𝒦px​dxJ=\frac{1}{2\pi}\oint_{\mathcal{K}}p_{x}\,\mathrm{d}x

is defined as a contour integral over the closed torus𝒦\mathcal{K}, while the partial actionJ′=12​π​∫xx′px​dxJ^{\prime}=\frac{1}{2\pi}\int_{x}^{x^{\prime}}p_{x}\,\mathrm{d}x

represents a sector integral corresponding to a single-turn iteration fromxxtox′x^{\prime}. Both integrals are evaluated along the AI tori defined by Eq. (2), as illustrated in Fig.3.

To evaluate the betatron tune using Eq. (3), we need to determine the constant-level sets of𝒦\mathcal{K}defined by Eq. (2). In general, these level sets do not admit simple parameterization whenm+n≥4m+n\geq 4. Nevertheless, they can be populated numerically with arbitrarily high density using a simple gradient-based minimization algorithm: starting from an initial guess of the formc2,0​x02+c0,2​px,02=𝒦,c_{2,0}x_{0}^{2}+c_{0,2}p_{x,0}^{2}=\mathcal{K},

we compute the deviation from the target value of𝒦\mathcal{K}and iteratively update the phase-space coordinates using local gradient information,∇𝒦=[∑m,nm​cm,n​xm−1​pxn,∑m,nn​cm,n​xm​pxn−1],\nabla\mathcal{K}=\left[\sum_{m,n}m\,c_{m,n}\,x^{m-1}p_{x}^{n},\;\sum_{m,n}n\,c_{m,n}\,x^{m}p_{x}^{n-1}\right],(4)

until convergence is achieved.

Once a sufficiently dense set of points on a torus has been populated, the derivative∂J/∂𝒦\partial J/\partial\mathcal{K}can be evaluated conveniently in a polar coordinate system(r,θ)(r,\theta). Specifically, we calculate the radial derivative of𝒦\mathcal{K}with respect torrat a fixed azimuthal angleθ\theta,𝒦\displaystyle\mathcal{K}=∑m,ncm,n​xm​pxn=∑m,ncm,n​rm+n​cosm⁡θ​sinn⁡θ,\displaystyle=\sum_{m,n}c_{m,n}x^{m}p_{x}^{n}=\sum_{m,n}c_{m,n}r^{m+n}\cos^{m}\theta\sin^{n}\theta,∂𝒦∂r\displaystyle\frac{\partial\mathcal{K}}{\partial r}=∑m,n(m+n)​cm,n​rm+n−1​cosm⁡θ​sinn⁡θ.\displaystyle=\sum_{m,n}(m+n)c_{m,n}\,r^{m+n-1}\cos^{m}\theta\sin^{n}\theta.(5)

Then, on the torus, the data points are ordered according to the azimuthal angleθ∈[−π,π]\theta\in[-\pi,\pi]. Between two neighboring points, the contribution to the action integralJJis approximated byJi≈12​π​ri2​(θi+1−θi)2=12​π​ri2​Δ​θi2.J_{i}\approx\frac{1}{2\pi}\frac{r_{i}^{2}(\theta_{i+1}-\theta_{i})}{2}=\frac{1}{2\pi}\frac{r_{i}^{2}\Delta\theta_{i}}{2}.(6)

Its derivative with respect to𝒦\mathcal{K}isd​Jid​𝒦=ri​Δ​θi2​π​d​rid​𝒦=ri​Δ​θi2​π​(d​𝒦d​ri)−1,\frac{\mathrm{d}J_{i}}{\mathrm{d}\mathcal{K}}=\frac{r_{i}\Delta\theta_{i}}{2\pi}\frac{\mathrm{d}r_{i}}{\mathrm{d}\mathcal{K}}=\frac{r_{i}\Delta\theta_{i}}{2\pi}\left(\frac{\mathrm{d}\mathcal{K}}{\mathrm{d}r_{i}}\right)^{-1},(7)

when the gradient of𝒦\mathcal{K}is predominantly radial,d​𝒦d​r≈∂𝒦∂r\frac{\mathrm{d}\mathcal{K}}{\mathrm{d}r}\approx\frac{\partial\mathcal{K}}{\partial r}, which has already been evaluated in Eq. (5). The denominator of Eq. (3) becomesd​Jd​𝒦=∑id​Jid​𝒦.\frac{\mathrm{d}J}{\mathrm{d}\mathcal{K}}=\sum_{i}\frac{\mathrm{d}J_{i}}{\mathrm{d}\mathcal{K}}.(8)

To calculate the numerator of Eq. (3), we choose a point(x​(r,θ),px​(r,θ))(x(r,\theta),\,p_{x}(r,\theta))on the torus and apply a one-turn iteration to obtain its image(x′​(r′,θ′),px′​(r′,θ′))(x^{\prime}(r^{\prime},\theta^{\prime}),\,p_{x}^{\prime}(r^{\prime},\theta^{\prime})). The derivative of the partial action isd​J′d​𝒦=∑θ′≤θi≤θd​Jid​𝒦.\frac{\mathrm{d}J^{\prime}}{\mathrm{d}\mathcal{K}}=\sum_{\theta^{\prime}\leq\theta_{i}\leq\theta}\frac{\mathrm{d}J_{i}}{\mathrm{d}\mathcal{K}}.

Because one-turn iterations advance clockwise, we always haveθ′<θ\theta^{\prime}<\theta, as annotated with the blue shaded area in Fig.3. However, whenθ′\theta^{\prime}crosses the−π-\piboundary, the integration region becomes the union of two adjacent sectors,[θ,−π][\theta,-\pi]and[π,θ′][\pi,\theta^{\prime}], corresponding to the yellow shaded area.Figure 3:The derivatives of the partial actionJ′J^{\prime}with respect to the AI𝒦\mathcal{K}under one-turn iteration are obtained by estimating the corresponding shadowed areas in phase space. Note that the one-turn map induces a clockwise rotation.

Since nonlinear Betatron oscillations are quasi-periodic, the instantaneous turn-to-turn rotation angle varies depending on the integration interval[θ,θ′][\theta,\theta^{\prime}]. A quasi-constant tune is obtained by averaging over many successive iterations,ν=limN→∞1N​∑i=1Nνi.\nu=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{i=1}^{N}\nu_{i}.(9)

Such a calculation formally requires successive iterations of the one-turn map, which can be computationally expensive. However, when the fractional tune is Diophantine irrational, the corresponding multi-turn trajectory becomes dense on the torus. In this case, the tune can be accurately evaluated by averaging a sufficiently large number of instantaneous PRNs, computed from initial conditions uniformly distributed along the AI tori. This tune calculation approach can be boosted by an efficient, embarrassingly parallel computation of PRNs as illustrated in Fig.4.Figure 4:Variation of the instantaneous PRNs as a function of the initial azimuthal launch angleθ\thetaat two different amplitudes 3 and 30mm\mathrm{m}\mathrm{m}. The periodicity of the betatron oscillation degrades with increasing amplitude.

## IVAmplitude-depended detuning

In nonlinear oscillators, amplitude-dependent detuning (ADD) can drive the tune to approach resonances, despite the linear tune being well separated from the resonance. In this section, we extract tunes directly on gradually increasing amplitude AI tori with the method described. Note that, unlike conventional approaches, in which detuning coefficients are typically estimated order-by-order, the proposed framework enables direct evaluation of the overall detuning associated with each torus. Figure5presents the AIA-based estimates of the on- and off-momentum (δ=±1.5%\delta=\pm 1.5\%) dynamic apertures (left column) and the corresponding ADDs (right column) in the mid-plane of the NSLS-II ring. These estimates show reasonable agreement with results obtained from symplectic tracking simulationsYoshida (1990).Figure 5:AI tori around different dispersive closed orbits (left column) and their ADDs (right column). The solid blue lines are calculated with AIA, while the yellow dots are obtained with tracking simulation.

As mentioned previously, even when the motion is confined to a single torus, instantaneous PRNs vary with azimuthal angles as illustrated in Fig.4. When PRNs are averaged over successiveNN-turn intervals, the differences between these averages quantify the sensitivity of the tune to initial conditions, commonly referred to as tune diffusionLaskar (2003); Papaphilippou (2014). However, this procedure requires repeated iterations of the one-turn map and is therefore not computationally more efficient than the Numerical Analysis of Fundamental Frequencies (NAFF) method. In contrast, we observe that PRNs evaluated from non-successive iterations with randomly chosen initial conditions exhibit pronounced variation as particle motion approaches the boundary of the dynamic aperture, as highlighted in the bottom panel of Fig.6. These variations provide a clear signature of the breakdown of quasi-periodicity and, consequently, the loss of long-term stability. Similar behavior has previously been exploited as a fast chaos indicatorSzezech Jret al.(2013), and it may offer a promising tool for nonlinear lattice optimization.Figure 6:Variation of instantaneous PRNs at different amplitudes. The top subplot shows the average amplitude-dependent detuning, with PRN variations indicated by error bars. The bottom subplot highlights the sharp increase in PRN variations near the dynamic aperture boundary.

## VConclusion

We have demonstrated an efficient nonlinear beam-dynamics framework based on approximate invariant reconstruction and betatron frequency extraction, using the NSLS-II storage ring as a representative example. Within this framework, the analysis does not rely on conventional Hamiltonian perturbation theory, Lie-algebraic methods, or normal-form techniques, nor does it require Courant-Snyder linear parameterization. Instead, key dynamical quantities – such as the dynamic aperture and amplitude-dependent detuning – can be evaluated directly and efficiently, with results that are validated by symplectic tracking simulations. In this paper, this analysis approach is applied to a 1-DoF system, specifically the horizontal motion in the mid-plane. Nevertheless, it is readily extensible to N-DoF systems, for example by adopting the formulation described in Ref.Mitchellet al.(2021). An alternative method for extracting betatron tunes in N-DoF systems, based on time-of-flight analysis for approximate invariant flowsXuet al.(2025), will be presented in a forthcoming companion paper (Part II).

## Data availability

The data that support the findings of this study are available upon reasonable request and subject to standard U.S. national laboratory data-sharing policies.

## Acknowledgements.We would like to thank, Y-K. Kan, T. Shaftan and V. Smaluk (BNL) for the discussion and support. This research is supported by the U.S. Department of Energy (DOE) under Contract No. DE-SC0012704, and the DOE Basic Energy Sciences (BES) Field Work Proposal (FWP) 2025-BNL-PS040, the DOE’s Early Career Program, and the DOE High Energy Physics (HEP) award DE-SC0019403.

## References
- Courant and Snyder (1958)Ernest D Courant and Hartland S Snyder, “Theory of the alternating-gradient synchrotron,” Annals of physics3, 1–48 (1958).
- Wilson (1995)E Wilson, “Nonlinear
resonances,” inCAS CERN
Accelerator School. 5. Advanced accelerator physics course. Proceedings. Vol.
1(Rhodes, Greece, 1995).
- Dragt (2011)Alex J. Dragt,Lie Methods for Nonlinear
Dynamics with Applications to Accelerator Physics(University of Maryland, 2011).
- Berz (1991)Martin Berz, “Differential
algebraic description of beam dynamics,” Particle Accelerators24, 109–124 (1991).
- Chao (2020)Alexander Wu Chao,Lectures on
accelerator physics(World Scientific, 2020).
- Kolmogorov (1954)A. N. Kolmogorov, “On the
conservation of conditionally periodic motions under small perturbations of
the hamiltonian,” Dokl. Akad. Nauk SSSR98, 527–530 (1954).
- Arnold (1963)V. I. Arnold, “Proof of a
theorem by A. N. Kolmogorov on the preservation of conditionally periodic
motions,”Russian Mathematical Surveys18, 9–36 (1963).
- Moser (1962)J. Moser, “On invariant
curves of area-preserving mappings of an annulus,” Nachr. Akad. Wiss. Göttingen
Math.-Phys. Kl. II , 1–20 (1962).
- Liet al.(2025)Yongjun Li, Derong Xu, and Yue Hao, “Construction of approximate invariants
for nonintegrable hamiltonian systems,” Physical Review Accelerators and Beams28, 074001 (2025).
- Nagaitsev and Zolkin (2020)Sergei Nagaitsev and Timofey Zolkin, “Betatron
frequency and the poincaré rotation number,”Phys. Rev. Accel. Beams23, 054001 (2020).
- Dierker (2007)Steve Dierker, “NSLS-II
preliminary design report,”Brookhaven National Laboratory (2007).
- Note (1)Strictly speaking, in the presence of an RF cavity system
operating at a fixed frequency, variations in the closed-orbit path length
lead to small changes in the beam momentum.
- Yang (2009)Lingyun Yang, “Array based
truncated power series package,” Proc. ICAP’09 , 371–373
(2009).
- Zhang (2024)He Zhang, “cppTPSA/pyTPSA:
a C++/Python package for truncated power series algebra,” Journal of Open Source Software9, 4818 (2024).
- Nagaitsev and Zolkin (2026)Sergei Nagaitsev and Timofey Zolkin, “Erratum:
Betatron frequency and the poincaré rotation number [Phys. Rev. Accel.
Beams 23, 054001 (2020)],”Phys. Rev. Accel. Beams29, 029901 (2026).
- Lichtenberg and Lieberman (2013)Allan J. Lichtenberg and Michael A. Lieberman,Regular and chaotic dynamics, Vol. 38 (Springer Science & Business Media, 2013).
- Yoshida (1990)Haruo Yoshida, “Construction of
higher order symplectic integrators,” Physics letters A150, 262–268 (1990).
- Laskar (2003)Jacques Laskar, “Frequency map
analysis and particle accelerators,” inProceedings of the 2003 Particle Accelerator Conference, Vol. 1 (IEEE, 2003) pp. 378–382.
- Papaphilippou (2014)Yannis Papaphilippou, “Detecting
chaos in particle accelerators through the frequency map analysis method,” Chaos: An
Interdisciplinary Journal of Nonlinear Science24(2014).
- Szezech Jret al.(2013)JD Szezech Jr, AB Schelin,
IL Caldas, SR Lopes, PJ Morrison, and RL Viana, “Finite-time rotation number: A fast indicator for chaotic
dynamical structures,” Physics Letters A377, 452–456 (2013).
- Mitchellet al.(2021)Chad E. Mitchell, Robert D. Ryne, Kilean Hwang,
Sergei Nagaitsev, and Timofey Zolkin, “Extracting dynamical
frequencies from invariants of motion in finite-dimensional nonlinear
integrable systems,”Phys. Rev. E103, 062216 (2021).
- Xuet al.(2025)Derong Xu, Yongjun Li,
Yue Hao, and Sergei Nagaitsev, “Frequency extraction from invariant
flows,” arXiv
preprint arXiv:2512.16060 (2025).

## 


- 


Major funding support from
