# Phase transitions and microphases in elastomers. I. Emergence of stable domains

**arXiv ID**: 2607.27516v1
**Authors**: Manu Mannattil, Haim Diamant, David Andelman
**Published**: 2026-07-29
**Categories**: cond-mat.soft, cond-mat.mtrl-sci, cond-mat.stat-mech, nlin.PS, physics.chem-ph
**Comments**: 13 pages, 6 figures
**HTML URL**: https://arxiv.org/html/2607.27516v1

## Abstract

Elasticity often plays a key role in regulating phase separation in physical systems. Recent experiments have shown that elastic effects can be used to control microphase separation in swollen elastomers. Here, microphase separation arises from a mismatch between the characteristic length scales of elastic and thermodynamic interactions. In this first part of a two-part paper, we show that microphase formation in elastomers can be explained using conventional theories of elasticity through a nonlocal thermodynamic-elastic coupling arising from volume conservation. Our theory reproduces the observed dependence of phase transition temperature and domain size on elastomer stiffness in isotropically swollen elastomers. In the companion paper, we investigate the effects of anisotropic swelling and inhomogeneous elastic moduli.

## Full Text

Phase transitions and microphases in elastomers. I. Emergence of stable domains

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.27516v1 [cond-mat.soft] 29 Jul 2026††thanks:Present address: School of Engineering and Applied Sciences, Harvard University, Cambridge, Massachusetts 02138, USA.

## Phase transitions and microphases in elastomers. I. Emergence of stable domainsManu Mannattilmanu.mannattil@posteo.netSchool of Chemistry, and Center for Physics and Chemistry of Living Systems, Tel Aviv University, Tel Aviv 69978, IsraelSchool of Physics and Astronomy, and Center for Physics and Chemistry of Living Systems, Tel Aviv University, Tel Aviv 69978, IsraelHaim Diamanthdiamant@tauex.tau.ac.ilSchool of Chemistry, and Center for Physics and Chemistry of Living Systems, Tel Aviv University, Tel Aviv 69978, IsraelDavid Andelmanandelman@tauex.tau.ac.ilSchool of Physics and Astronomy, and Center for Physics and Chemistry of Living Systems, Tel Aviv University, Tel Aviv 69978, Israel

## Abstract

Elasticity often plays a key role in regulating phase separation in physical systems.
Recent experiments have shown that elastic effects can be used to control microphase separation in swollen elastomers.
Here, microphase separation arises from a mismatch between the characteristic length scales of elastic and thermodynamic interactions.
In this first part of a two-part paper, we show that microphase formation in elastomers
can be explained using conventional theories of elasticity through a nonlocal thermodynamic–elastic coupling arising from volume conservation.
Our theory reproduces the observed dependence of phase transition temperature and domain size on elastomer stiffness in isotropically swollen elastomers.
In the companion paper, we investigate the effects of anisotropic swelling and inhomogeneous elastic moduli.

## IIntroduction

Elasticity and phase separation are ubiquitously interlinked in many condensed matter systems.
Examples include polymer blends and gels, where elastic networks within the material constrain compositional fluctuations[1,2,3,4]; biological cells, where elasticity is known to regulate the formation of biomolecular condensates[5,6,7]; and metallic alloys, where elastic fields mediate long-range interactions between phase-separated domains[8,9].
In these systems, elasticity can modify domain morphologies[10,11], alter phase boundaries[12], and even suppress or promote phase separation[13].
Understanding how elasticity affects phase separation is, therefore, essential for controlling the structure and behavior of a wide variety of physical systems.

A recent experiment[14]demonstrated how the interplay between elasticity and phase separation can be harnessed to create patterned elastomers with complex morphologies.
In these experiments, crosslinked polydimethylsiloxane (PDMS) elastomers are first swollen with a solvent and then cooled to induce phase separation.
Rather than undergoing macroscopic demixing into solvent-rich and polymer-rich phases, the elastomer develops stable microphases with characteristic sizes of a few µm, a phenomenon termedelastic microphase separation(EMPS).
For elastomers of Young’s modulusYY, the characteristic domain size scales asY−1/2Y^{-1/2}, and the phase transition temperature decreases linearly withYY.
Based on these observations, it was proposed that EMPS arises from the distinct length scales over which elastic and thermodynamic interactions operate[14].
EMPS bears some resemblance to earlier observations of phase separation and critical density fluctuations in certain gels when cooled[15,16,17,18].
However, unlike the elastomers studied in Ref.[14], those gels do not exhibit microphase separation and instead undergo spinodal decomposition.

The first theoretical attempt[14]to explain EMPS was based on the Cahn–Larché free energy[13,19]for metallic alloys, but it could not account for microphase formation.
Subsequent work introduced a phenomenological Coulomb-like interaction term, which produced microphase-separated domains in numerical simulations[20].
Alternative approaches based on linear and nonlinear nonlocal elasticity have also been proposed, including a one-dimensional numerical model that captures the experimental scaling trends for deep temperature quenches and high stiffnesses[21,22].
Broader questions concerning solvent–network equilibrium have also been explored, and strain stiffening has been shown to enable phase coexistence between the polymer network and the solvent[23,24].
Even more recently, motivated by EMPS, more general studies on nonlocal pattern formation[25]and on poroelastic coarsening and arrest in gels[26]have also appeared.

In our earlier contribution towards EMPS modeling[27], we developed a three-dimensional (3D) phase-field model and analytically derived the domain-size scaling as observed in experiments.
Our framework is grounded in theoretical approaches to explain density fluctuations and spinodal composition in gels[18,2,28,9]that were subsequently confirmed experimentally.
Furthermore, the transition temperature and phase behavior predicted by our model showed good quantitative agreement with experimental results.

While the models and studies discussed above provide valuable insights into EMPS and, more broadly, into phase separation,
several crucial aspects of EMPS remain insufficiently understood or unexplained.
In our previous work (see also Ref.[21]), we had assumed that the elastomers undergoing EMPS obey nonlocal linear elasticity,
with a nonlocal constitutive relation between the stress and strain[29,30].
Extending such an approach to more general settings, particularly those involving anisotropy, remains challenging and motivates the development
of a framework that captures the same physics.

In this paper, hereafter referred to as Part I, we demonstrate that the restrictive assumption of nonlocal elasticity is not required to account for EMPS.
Instead, all its key features can be explained by introducing a physically intuitive nonlocal coupling between thermodynamics and elasticity that arises from polymer volume conservation.
This places our earlier theory[27]on a firmer foundation while enabling the analysis of anisotropic effects, which the original formulation could not address.
Anisotropic effects are the subject of the companion paper[31], referred to as Part II hereafter.

In Part I, where we consider only isotropically swollen elastomers, we show that our model captures the experimentally observed scaling of domain size and transition temperature with stiffness when standard results from rubber elasticity are incorporated.
We further discuss the possible morphologies that arise during microphase separation and make comments on the phase behavior in the presence of equilibrium fluctuations.
Finally, we show that the scaling behavior observed in EMPS closely parallels that predicted by de Gennes for phase separation in crosslinked polymer blends more than four decades ago[1].

Part I is organized as follows.
SectionIIintroduces the theoretical framework.
General phase behavior for isotropically swollen elastomers is discussed in Sec.III,
while comparisons with experiments are presented in Sec.IV.
SectionVcompares EMPS with phase separation in crosslinked polymer blends,
and Sec.VIsummarizes the main findings.FIG. 1:(a) The volume fraction of a discrete polymer network, represented as a continuum fieldϕ​(𝒙)\phi(\bm{x}),
exhibits a pronounced coarseness at intermolecular length scales.
However, only those variations inϕ\phithat persist beyond a characteristic length scalehhproduce appreciable network deformations.
We describe the deformations using a mesoscopic displacement field𝒖​(𝒙)\bm{u}(\bm{x}).
(b) To capture this separation of scales,ϕ\phiis replaced
with a further coarse-grained versionϕ¯\bar{\phi}in the material-conservation relation,
Eq. (8), that links𝒖\bm{u}andϕ\phi.
This associates𝒖\bm{u}only with variations inϕ\phion length scales larger thanhh.
For isotropically swollen elastomers, we takeh=n​ξh=n\xi, whereξ\xiis the end-to-end distance between adjacent crosslinks in the polymer network andnnis the average number of crosslinks we coarse-grain over.

## IIModel

We consider a charge-neutral elastomer consisting of a crosslinked polymer network isotropically swollen by a solvent.
Because swelling results from coupled thermodynamic and elastic effects and can involve large deformations, swollen elastomers are generally described using nonlinear elasticity[32,33].
Here, we do not model the swelling process itself and we assume that the system has already reached thermodynamic equilibrium.
Furthermore, by studying small fluctuations about an already swollen reference state, we can linearize the underlying nonlinear theory and use linear elasticity.
Within this linear description, at a given temperatureTT, the system is characterized by two continuum fields shown in Fig.1(a): the volume fractionϕ\phiand the displacement field𝒖\bm{u}of the polymer network[34].
Immediately after swelling, the network volume fractionϕ0\phi_{0}is a spatially uniform constant.
Then, upon lowering the temperature, the local volume fractionϕ​(𝒙)\phi(\bm{x})deviates fromϕ0\phi_{0}.

We assume that the polymer–solvent system in the swollen elastomer is close to a critical point(ϕc,Tc)(\phi_{\text{c}},T_{\text{c}}), whereϕc\phi_{\text{c}}is the critical volume fraction andTcT_{\text{c}}the critical temperature.
After defining the order parameterψ​(𝒙)=ϕ​(𝒙)−ϕc\psi(\bm{x})=\phi(\bm{x})-\phi_{\text{c}}, we express the total free energyℱ\mathscr{F}asℱ​[ψ,𝒖]=ℱGL​[ψ]+ℱel​[𝒖],\mathscr{F}[\psi,\bm{u}]=\mathscr{F}_{\text{GL}}[\psi]+\mathscr{F}_{\text{el}}[\bm{u}],(1)

whereℱGL\mathscr{F}_{\text{GL}}is a Ginzburg–Landau free-energy accounting for network-solvent phase separation.
The second term,ℱel​[𝒖]\mathscr{F}_{\text{el}}[\bm{u}], is the elastic energy associated with the network deformation,
to be discussed in more detail momentarily.

The free energyℱGL\mathscr{F}_{\text{GL}}, has the formℱGL​[ψ]=∫d3​x​[f​(ψ)+12​κ​|∇ψ|2+η​(ψ−ψ0)].\mathscr{F}_{\text{GL}}[\psi]=\int\mathrm{d}^{3}x\,\left[f(\psi)+\frac{1}{2}\kappa\left|\bm{\nabla}\psi\right|^{2}+\eta(\psi-\psi_{0})\right].(2)

The coordinate𝒙=(x,y,z)\bm{x}=(x,y,z)in 3D space is an Eulerian coordinate describing the current state of the elastomer.
In addition, the bulk free-energy densityf​(ψ)f(\psi)is written as an expansion about the critical point to quartic order,
retaining only even powers inψ\psi, i.e.,f​(ψ)=12​a​(T−Tc)​ψ2+14​b​ψ4,f(\psi)=\frac{1}{2}a(T-T_{\text{c}})\psi^{2}+\frac{1}{4}b\psi^{4},(3)

whereaaandbbare positive phenomenological constants.
Bulk energy densities of this form are commonly employed to describe swelling and deswelling of polymer networks[28,35,36].
All thermodynamic contributions from polymer-solvent interactions are implicitly included inf​(ψ)f(\psi).
An advantage of the Landau free energyffis that, forb>0b>0, it has a stable double-well form.
The quartic termψ4\psi^{4}ensures thermodynamic stability and avoids limitations of mean-field free energies that lack an explicit double-well structure[23].

The above free energyℱGL\mathscr{F}_{\text{GL}}, Eq. (2), also contains a squared-gradient contribution involving an interfacial parameterκ>0\kappa>0, which penalizes spatial inhomogeneities inψ\psi.
Finally, the chemical potentialη\etainℱGL\mathscr{F}_{\text{GL}}acts as a Lagrange multiplier and constrains the spatial average ofψ\psito a constant meanψ0=ϕ0−ϕc\psi_{0}=\phi_{0}-\phi_{\text{c}}, thereby conserving the total volume of the system.

As the swollen polymer is assumed to follow conventional linear elasticity, its elastic energy isℱel​[𝒖]=12​∫d3​x​[λ​(tr⁡𝜺)2+2​μ​tr⁡(𝜺2)],\mathscr{F}_{\text{el}}[\bm{u}]=\frac{1}{2}\int\mathrm{d}^{3}x\,\left[\lambda(\operatorname{tr}\bm{\varepsilon})^{2}+2\mu\operatorname{tr}(\bm{\varepsilon}^{2})\right],(4)

where𝜺=12​[∇𝒖+(∇𝒖)𝖳]\bm{\varepsilon}=\frac{1}{2}[\bm{\nabla}\bm{u}+(\bm{\nabla}\bm{u})^{\mathsf{T}}]is the linearized strain, with(∇𝒖)𝖳(\bm{\nabla}\bm{u})^{\mathsf{T}}being the transpose of∇𝒖\bm{\nabla}\bm{u}.
The Lamé moduliλ\lambdaandμ\mudepend on the polymer volume fractionϕ0\phi_{0}of the elastomer in the swollen state.
The dependence is typically weak, and since the elastomer is close to criticality, we takeϕ0≈ϕc\phi_{0}\approx\phi_{\text{c}}in the estimates below.
For an isotropically swollen elastomer composed of Gaussian chains, we have[18]λ=ν​kB​T​(ϕc−ϕc1/3),μ=ν​kB​T​ϕc1/3.\lambda=\nu k_{\text{B}}T\left(\phi_{\text{c}}-\phi_{\text{c}}^{1/3}\right),\quad\mu=\nu k_{\text{B}}T\phi_{\text{c}}^{1/3}.(5)

Above,kBk_{\text{B}}is the Boltzmann constant andν\nudenotes the density of network strands,
namely the number of polymer segments connecting neighboring crosslinks per unit volume.
A strand here refers to the portion of a chain between two successive crosslinks.

Finally, it is also worth noting that linear theories of gels[34,18,37,38]are sometimes formulated entirely in terms of the displacement field𝒖\bm{u}.
In these theories, thermodynamic contributions that are quadratic in the strain are absorbed
into the first Lamé modulusλ\lambdaby adding an osmotic termϕ02​f′′​(0)\phi_{0}^{2}f^{\prime\prime}(0).
By contrast, our framework treats thermodynamic and elastic effects as operating at distinct length scales.
Consequently, we do not use osmotic elastic moduli in our analysis.

## Nonlocal effects via volume conservation

The total free energy in Eq. (1) is written as a sum of thermodynamic
and elastic effects, which depend on the fieldsψ\psiand𝒖\bm{u}, respectively.
Although bothψ\psiand𝒖\bm{u}describe the same underlying discrete polymer network,
they are defined at different length scales and serve distinct physical roles.
Specifically, interface formation and thermodynamic interactions, described byψ\psi,
occur at intermolecular length scales of a few Å,
while the elastic energy is dominated by those deformations𝒖\bm{u}occurring above
a characteristic mesoscopic (µm) scale (see Fig.1).

The fieldsψ\psiand𝒖\bm{u}are not mutually independent.
They are linked by the requirement that the total volume of the polymer network be conserved during phase separation.
Recalling that𝒙\bm{x}is an Eulerian coordinate describing the current configuration of the elastomer,
conservation of polymer volume over an arbitrary subvolume yields∫d3​x​[1−∇⋅𝒖]​ϕ0=∫d3​x​ϕ¯​(𝒙),\int\mathrm{d}^{3}x\,\left[1-\bm{\nabla\cdot}\bm{u}\right]\phi_{0}=\int\mathrm{d}^{3}x\,\bar{\phi}(\bm{x}),(6)

where the Jacobian correction1−∇⋅𝒖1-\bm{\nabla\cdot}\bm{u}accounts for the linear-order change in the local volume measure due to the deformation.
Although the above equality is well known in continuum theories of gels[39,18,9,21,27], in Eq. (6) the second integral is written in terms ofϕ¯​(𝒙)\bar{\phi}(\bm{x})rather thanϕ​(𝒙)\phi(\bm{x}).
The fieldϕ¯​(𝒙)\bar{\phi}(\bm{x})is a coarse-grained polymer volume fraction with its short-wavelength fluctuations suppressed.
This ensures that the displacement field𝒖\bm{u}is coupled only to those variations inϕ\phioccurring on comparable length scales.

There are several possible ways to chooseϕ¯​(𝒙)\bar{\phi}(\bm{x}).
For convenience, we obtain it by filteringϕ​(𝒙)\phi(\bm{x})using an isotropic Gaussian kernelK​(𝒙)=(2​π​h2)−3/2​exp⁡(−12​|𝒙|2/h2)K(\bm{x})=(2\pi h^{2})^{-3/2}\exp(-\frac{1}{2}\left|\bm{x}\right|^{2}/h^{2}), thereby preferentially retaining its long-wavelength components:ϕ¯​(𝒙)=∫d3​x′​K​(𝒙−𝒙′)​ϕ​(𝒙′).\bar{\phi}(\bm{x})=\int\mathrm{d}^{3}{x^{\prime}}\,K(\bm{x}-\bm{x}^{\prime})\,\phi(\bm{x}^{\prime}).(7)

In the above equation, the length scalehhcontrols the extent to whichϕ¯\bar{\phi}is coarse-grained again.
It is related to the polymer network’s mesh size, as will be discussed in more detail in Sec.IV(see also Fig.1).
Our earlier work[27]also used a similar Gaussian kernel to impose a nonlocal stress–strain relation.
However, the physical basis of such a constitutive relation is not transparent and limits its generalizability.
For that reason, here we retain the standard strain-energy relation, Eq. (4).
Nonlocality instead arises naturally from volume conservation, which couples the fields𝒖\bm{u}andψ\psidefined at distinct length scales.

As Eq. (6) holds for arbitrary domains, we can equate its two integrands. Then, upon
further expanding around the critical volume fractionϕ=ϕc\phi=\phi_{\text{c}}, we obtain a nonlocal material conservation relationship of the form∇⋅𝒖=−ϕc−1​ψ¯​(𝒙)+𝒪​(ψ0)+𝒪​(ψ2),\bm{\nabla\cdot}\bm{u}=-\phi_{\text{c}}^{-1}\bar{\psi}(\bm{x})+\mathcal{O}(\psi_{0})+\mathcal{O}(\psi^{2}),\quad(8)

whereψ¯=ϕ¯−ϕc\bar{\psi}=\bar{\phi}-\phi_{\text{c}}.

For the remainder of the analysis, it is convenient to work in Fourier space.
Fourier transforming Eqs. (7) and (8) we obtain (to lowest order)i​𝒒⋅𝒖𝒒=−ϕc−1​ψ𝒒​e−12​h2​q2,i\bm{q}\cdot\bm{u}_{\bm{q}}=-\phi_{\text{c}}^{-1}\psi_{\bm{q}}\,\mathrm{e}^{-\frac{1}{2}h^{2}q^{2}},(9)

where𝒖𝒒=∫d3​x​e−i​𝒒⋅𝒙​𝒖​(𝒙)\bm{u}_{\bm{q}}=\int\mathrm{d}^{3}x\,\mathrm{e}^{-i\bm{q}\cdot\bm{x}}\,\bm{u}(\bm{x})andψ𝒒\psi_{\bm{q}}are the Fourier transforms of𝒖​(𝒙)\bm{u}(\bm{x})andψ​(𝒙)\psi(\bm{x}), respectively, withq=|𝒒|q=\left|\bm{q}\right|.
Likewise, making use of the Parseval–Plancherel theorem, the total elastic energy, Eq. (4), can be written asℱel​[𝒖𝒒]\displaystyle\mathscr{F}_{\text{el}}[\bm{u}_{\bm{q}}]=12∫d3​q(2​π)3[(2μ+λ)(𝒒⋅𝒖𝒒)(𝒒⋅𝒖−𝒒)\displaystyle=\frac{1}{2}\int\frac{\mathrm{d}^{3}q}{(2\pi)^{3}}\Big[(2\mu+\lambda)(\bm{q}\cdot\bm{u}_{\bm{q}})(\bm{q}\cdot\bm{u}_{-\bm{q}})+μq2𝒖𝒒⟂⋅𝒖−𝒒⟂]\displaystyle\quad+\mu q^{2}\bm{u}^{\perp}_{\bm{q}}\cdot\bm{u}^{\perp}_{-\bm{q}}\Big](10)

with𝒖𝒒⟂=𝒖𝒒−q−2​(𝒒⋅𝒖𝒒)​𝒒\bm{u}_{\bm{q}}^{\perp}=\bm{u}_{\bm{q}}-q^{-2}(\bm{q}\cdot\bm{u}_{\bm{q}})\bm{q}being the transverse component of𝒖𝒒\bm{u}_{\bm{q}}.

Throughout our analysis, we assume that material transport during phase separation is diffusion dominated and does not excite elastic shear modes.
Thermodynamic–elastic coupling gives rise only to longitudinal instabilities (those along𝒒\bm{q}),
as thermodynamic contributions to the free energy arise exclusively through the order parameterψ\psi.
Although elastic longitudinal and shear modes can undergo mode conversion at system boundaries,
such effects are negligible when the deformations remain much smaller
than the system size—a standard assumption in the theory of gels[40].
For the elastomers studied in Ref.[14], for example, microphase domains
are only a few µm across, whereas the sample size is of the order of a few cm.
Boundary-induced mode conversion is, therefore, negligible, allowing us to focus on contributions toℱel\mathscr{F}_{\text{el}}from the bulk longitudinal modes alone[9].

Consequently, we express the total elastic energy entirely in terms of the order parameterψ\psiusing the material conservation, Eq. (8).
Making use of Eq. (9) and discarding the transverse shear modes, we find that the total elastic energy isℱel​[ψ]=12​∫d3​q(2​π)3​M𝒒​ψ−𝒒​ψ𝒒,\mathscr{F}_{\text{el}}[\psi]=\frac{1}{2}\int\frac{\mathrm{d}^{3}q}{(2\pi)^{3}}M_{\bm{q}}\psi_{-\bm{q}}\psi_{\bm{q}},(11)

where the effectiveq{q}-dependent longitudinal modulus isM𝒒=ν​kB​Tϕc2​(ϕc+ϕc1/3)​e−h2​q2.M_{\bm{q}}=\frac{\nu k_{\text{B}}T}{\phi_{\text{c}}^{2}}\left(\phi_{\text{c}}+\phi_{\text{c}}^{1/3}\right)\mathrm{e}^{-h^{2}q^{2}}.(12)

Note thatM𝒒M_{\bm{q}}has aqq-dependence owing solely to the nonlocal nature of the material conservation relation, Eq. (8).

## IIIGeneral phase behavior

## III.1Linear stability analysis

For linear stability analysis, we setψ=ψ0+δ​ψ\psi=\psi_{0}+\delta\psiin the total free energyℱ=ℱGL+ℱel\mathscr{F}=\mathscr{F}_{\text{GL}}+\mathscr{F}_{\text{el}}, withℱGL\mathscr{F}_{\text{GL}}andℱel\mathscr{F}_{\text{el}}given by Eqs. (2) and (11), respectively.
After omitting the nonquadratic terms in the free energy, which are not relevant for linear stability analysis, the total Gaussian (quadratic)
free energy of the modulationsδ​ψ\delta\psitakes the formℱG​[δ​ψ]=12​∫d3​q(2​π)3​F𝒒​δ​ψ𝒒​δ​ψ−𝒒,\mathscr{F}_{\text{G}}[\delta\psi]=\frac{1}{2}\int\frac{\mathrm{d}^{3}q}{(2\pi)^{3}}\,F_{\bm{q}}\delta\psi_{\bm{q}}\delta\psi_{-\bm{q}},(13)

withF𝒒F_{\bm{q}}being the Fourier transform of the effective binary interaction inδ​ψ\delta\psi, given byF𝒒=a​(T−Tc)+3​b​ψ02+κ​q2+M𝒒,F_{\bm{q}}=a(T-T_{\text{c}})+3b\psi_{0}^{2}+\kappa q^{2}+M_{\bm{q}},(14)

and the longitudinal modulusM𝒒M_{\bm{q}}is given by Eq. (12).
BecauseM𝒒∼e−h2​q2M_{\bm{q}}\sim\mathrm{e}^{-h^{2}q^{2}}, the elastic energy cost
can be reduced by preferentially enhancing modulations at short wavelengths (largeqq).
By contrast, the interfacial contributionκ​q2\kappa q^{2}penalizes rapid spatial variations and, therefore, favors long-wavelength
(smallqq) modulations. The competition between these two opposing tendencies can, in principle,
lead to the stabilization of a spatially modulated phase at an intermediate wavenumber[1,41,42].

During a temperature quench, the onset of this instability occurs at the temperature whereF𝒒F_{\bm{q}}first vanishes.
IfF𝒒≲0F_{\bm{q}}\lesssim 0for someqq, the correspondingqq-modes become energetically favorable and grow,
thereby continuously lowering the free energy until the quartic term inℱGL\mathscr{F}_{\text{GL}}stabilizes their growth.
Additionally, the most unstable wavenumberqmq_{\text{m}}is the wavenumber
at whichF𝒒F_{\bm{q}}has a minimum, since it is this mode that first becomes
unstable during the quench[1,43,44].
This wavenumber sets both the emergent length scale and the form of the resulting modulation.
Consequently, instead of a macroscopic phase separation into solvent-rich and polymer-rich domains,
we expect the emergence of a periodic pattern of alternating solvent-rich and polymer-rich regions.

MinimizingF𝒒F_{\bm{q}}in Eq. (14)
with respect toqq, we see that the most unstable wavenumberqmq_{\text{m}}isqm2=h−2​ln⁡γ0.q_{\text{m}}^{2}=h^{-2}\ln\gamma_{0}.(15)

where the dimensionless parameterγ0\gamma_{0}is defined asγ0=M0​h2κ\gamma_{0}=\frac{M_{0}h^{2}}{\kappa}(16)

andM0=M𝒒→0M_{0}=M_{\bm{q}\to 0}from Eq. (12) is the long-wavelength modulus
of an isotropically swollen elastomer, given byM0=ν​kB​Tϕc2​(ϕc+ϕc1/3).M_{0}=\frac{\nu k_{\text{B}}T}{\phi_{\text{c}}^{2}}\left(\phi_{\text{c}}+\phi_{\text{c}}^{1/3}\right).(17)

Clearly, from Eq. (15), we see that a realqmq_{\text{m}}exists only ifγ0>1\gamma_{0}>1.

The dimensionless parameterγ0\gamma_{0}is analogous to an elastocapillary number and measures the relative importance of elastic and interfacial contributions to the free energy.111Our definition of the elastocapillary numberγ0\gamma_{0}differs from the more conventional
one[45,46], which is defined as the ratio of capillary (interfacial) effects to elastic effects.Whenγ0<1\gamma_{0}<1, interfacial costs dominate, and the system does not undergo microphase separation.
Instead, a bulk linear instability develops below the temperatureTc−a−1​[3​b​ψ02+M0]T_{\text{c}}-a^{-1}[3b\psi_{0}^{2}+M_{0}]and the system undergoes a conventional macrophase separation into polymer-rich and solvent-rich phases.

Whenγ0>1\gamma_{0}>1, elastic costs dominate, favoring the formation of many stable, finite-size domains, resulting in microphase separation.
In this case, settingq=qmq=q_{\text{m}}inF𝒒=0F_{\bm{q}}=0, we find the temperatureTmT_{\text{m}}at which microphase separation occurs to beTm​(ψ0)=Tc−a−1​[3​b​ψ02+M0​γ0−1​(1+ln⁡γ0)].T_{\text{m}}(\psi_{0})=T_{\text{c}}-a^{-1}\left[3b\psi_{0}^{2}+M_{0}\gamma_{0}^{-1}(1+\ln\gamma_{0})\right].(18)

From the above equation, we see that elastic effects—quantified by the longitudinal modulusMM—lowers the microphase separation temperatureTmT_{\text{m}}.
Such a downward shift of the transition temperature due to elasticity is well documented (for example, in metallic alloys[12]).
It shows that elasticity increases the temperature range over which the system remains stable.

The onset of microphase separation can also be gleaned from the static structure factorS​(𝒒)=⟨δ​ψ𝒒​δ​ψ−𝒒⟩S(\bm{q})=\langle\delta\psi_{\bm{q}}\,\delta\psi_{-\bm{q}}\rangle.
At temperatures aboveTmT_{\text{m}}, the scattering intensity arising from equilibrium fluctuationsδ​ψ\delta\psiis proportional toS​(𝒒)S(\bm{q}).
Within the Gaussian approximation,S​(𝒒)S(\bm{q})can be evaluated (up to multiplicative constants) as[9]S​(𝒒)\displaystyle S(\bm{q})=∫𝒟​[δ​ψ𝒒]​𝒟​[δ​ψ−𝒒]​δ​ψ𝒒​δ​ψ−𝒒​e−ℱG/kB​T∫𝒟​[δ​ψ𝒒]​𝒟​[δ​ψ−𝒒]​e−ℱG/kB​T\displaystyle=\frac{\int\mathcal{D}[\delta\psi_{\bm{q}}]\,\mathcal{D}[\delta\psi_{-\bm{q}}]\,\delta\psi_{\bm{q}}\,\delta\psi_{-\bm{q}}\,\mathrm{e}^{-\mathscr{F}_{\text{G}}/k_{\text{B}}T}}{\int\mathcal{D}[\delta\psi_{\bm{q}}]\,\mathcal{D}[\delta\psi_{-\bm{q}}]\,\mathrm{e}^{-\mathscr{F}_{\text{G}}/k_{\text{B}}T}}∼F𝒒−1,\displaystyle\sim F_{\bm{q}}^{-1},(19)

Forγ0>1\gamma_{0}>1, the structure factorS​(𝒒)S(\bm{q})exhibits a peak atq=qmq=q_{\text{m}}, with the peak heightS​(𝒒m)∼(T−Tm)−1S(\bm{q}_{\text{m}})\sim(T-T_{\text{m}})^{-1}.
As the elastomer temperature is reduced towardTmT_{\text{m}}, the scattering intensity develops a continuously growing peak at
a fixed wavenumberqmq_{\text{m}}, signaling the onset of instability and the formation of periodic structures.FIG. 2:Schematics of modulated phases showing (a) lamellae and (b) hexagonal phase, which also shows the unit-vector triad{𝒏j}\{\bm{n}_{j}\}.
At temperatures close to the critical temperature, the modulations are well approximated by sinusodial functions.
In both panels, solvent rich (deficient) regions are shown in red (blue).

## III.2Modulated phases

In the weak-segregation regime (T≲TcT\lesssim T_{\text{c}}), where the modulations are well represented by sinusoidal oscillations, a phase diagram can be obtained analytically using the single-mode approximation[47,43,41].
Upon re-expressing the elastic free energyℱel\mathscr{F}_{\text{el}}, Eq. (11),
in real space, the total free energyℱ=ℱGL+ℱel\mathscr{F}=\mathscr{F}_{\text{GL}}+\mathscr{F}_{\text{el}}for isotropically swollen elastomers becomesℱ=∫d3​x​[f​(ψ)+12​κ​|∇ψ|2+12​M0​(ψ¯)2].\mathscr{F}=\int\mathrm{d}^{3}x\,\left[f(\psi)+\frac{1}{2}\kappa\left|\bm{\nabla}\psi\right|^{2}+\frac{1}{2}M_{0}(\bar{\psi})^{2}\right].(20)

Although our discussion so far has been in 3D, to keep the analysis of phase behavior tractable, we limit it to two-dimensional (2D) modulations.
In 2D, one considers two spatially modulated phases, namely, lamellar, and hexagonally symmetric phases, as well as a spatially uniform phase.
From the free-energy densities of each phase, the phase boundaries follow from a standard common-tangent construction.
To streamline the discussion below, we introduce the following dimensionless parameterΣ=b−1​[a​(T−Tc)+3​b​ψ02+M0​γ0−1​(1+ln⁡γ0)].\Sigma=b^{-1}\left[a(T-T_{\text{c}})+3b\psi_{0}^{2}+M_{0}\gamma_{0}^{-1}(1+\ln\gamma_{0})\right].(21)

## Uniform phase

For the spatially uniform phase withψ​(𝒙)=ψ0\psi(\bm{x})=\psi_{0}, the free-energy density takes the formfU​(ψ0,T)=12​[a​(T−Tc)+M0]​ψ02+14​b​ψ04.f_{\text{U}}(\psi_{0},T)=\frac{1}{2}\left[a(T-T_{\text{c}})+M_{0}\right]\psi_{0}^{2}+\frac{1}{4}b\psi_{0}^{4}.(22)

## Lamellar phase

To represent the morphology of the lamellar phase, we assume that the order parameterψ​(𝒙)=ψ0+δ​ψ=ψ0+A​cos⁡(q​x),\psi(\bm{x})=\psi_{0}+\delta\psi=\psi_{0}+A\cos(qx),(23)

representing a unidirectional modulation (chosen arbitrarily along thexx-direction) with amplitudeAAand wavenumberqq.
See Fig.2(a) for an illustration.
Inserting this expression into the total free energy, Eq. (20), and minimizing it with respect to bothqqandAAyields
the free-energy densityfLf_{\text{L}}of the lamellar phase asfL​(ψ0,T)=fU​(ψ0,T)−b6​Σ2,f_{\text{L}}(\psi_{0},T)=f_{\text{U}}(\psi_{0},T)-\frac{b}{6}\Sigma^{2},(24)

with the wavenumberqmq_{\text{m}}and amplitudeAmA_{\text{m}}of the modulation beingqm2=h−2​ln⁡γ0,Am2=−43​Σ.q_{\text{m}}^{2}=h^{-2}\ln\gamma_{0},\quad A_{\text{m}}^{2}=-\frac{4}{3}\Sigma.(25)

Clearly, the aboveqmq_{\text{m}}is the same as the one derived in Eq. (15) using linear stability analysis.
As the modulation amplitudeAmA_{\text{m}}must be real for the lamellar phase to exist, the conditionΣ=0\Sigma=0in Eq. (21)
provides an estimate for the onset temperature of microphase separation, and we recover the expression in Eq. (18).

## Hexagonal phase

For the hexagonal phase, we consider modulations in the(x,y)(x,y)plane of the form[41,48]δ​ψ​(𝒙)=A​∑j=13cos⁡(q​𝒏j⋅𝒙),\delta\psi(\bm{x})=A\sum_{j=1}^{3}\cos\left(q\,\bm{n}_{j}\cdot\bm{x}\right),(26)

with the 2D unit vectors𝒏j\bm{n}_{j}satisfying∑j=13𝒏j=0\sum_{j=1}^{3}\bm{n}_{j}=0.
The hexagonal phase is illustrated in Fig.2(b).
Following the same procedure as for the lamellar phase, the solutionψ0+δ​ψ​(𝒙)\psi_{0}+\delta\psi(\bm{x})is substituted into Eq. (20),
which, after minimization, yields the free-energy density of the hexagonal phase asfH​(ψ0,T)=fU​(ψ0,T)−3​b64​Am,±2​(ψ0​Am,±−2​Σ),f_{\text{H}}(\psi_{0},T)=f_{\text{U}}(\psi_{0},T)-\frac{3b}{64}A_{\text{m},\pm}^{2}\left(\psi_{0}A_{\text{m},\pm}-2\Sigma\right),(27)

withqmq_{\text{m}}as in Eqs. (15) and (25), andAmA_{\text{m}}given byAm,±=45​[ψ0±(ψ02−53​Σ)1/2].A_{\text{m},\pm}=\frac{4}{5}\left[\psi_{0}\pm\left(\psi_{0}^{2}-\frac{5}{3}\Sigma\right)^{1/2}\right].(28)

Modulations with amplitudeAm,+A_{\text{m},+}correspond to the conventional hexagonal phase, whileAm,−A_{\text{m},-}describes the inverted hexagonal phase, with polymer-rich, hexagonally symmetric domains dispersed in a solvent-rich matrix.

Phase coexistence curves are determined using the common-tangent construction, which enforces equality of both the chemical potential and the osmotic pressure between the different phases.
This leads to the coupled system of equations∂fi∂ψ0,i\displaystyle\frac{\partial f_{i}}{\partial\psi_{0,i}}=∂fj∂ψ0,j,\displaystyle=\frac{\partial f_{j}}{\partial\psi_{0,j}},(29)ψ0,i​(∂fi∂ψ0,i)−fi\displaystyle\psi_{0,i}\left(\frac{\partial f_{i}}{\partial\psi_{0,i}}\right)-f_{i}=ψ0,j​(∂fj∂ψ0,j)−fj.\displaystyle=\psi_{0,j}\left(\frac{\partial f_{j}}{\partial\psi_{0,j}}\right)-f_{j}.(30)

The indicesiiandjjlabel any coexisting pair among the uniform, lamellar, hexagonal, and inverted hexagonal phases.
By numerically solving these equations, one obtains the phase diagram as a function of temperatureTTand mean polymer volume fractionϕ0\phi_{0}.FIG. 3:Phase diagram in the polymer volume fraction–temperature plane(ϕ0,T)(\phi_{0},T),
for an isotropically swollen elastomer with elastocapillary number [see Eq. (16)],γ0=4\gamma_{0}=4.
For illustrative purposes, we set the critical parameters to(ϕc,Tc)=(0.2,0)(\phi_{\text{c}},T_{\text{c}})=(0.2,0).
All other free-energy parameters are set to unity.
Elastic effects shift the critical temperature toTc′=Tm​(0)=−(1+ln⁡4)≈−2.386T_{\text{c}}^{\prime}=T_{\text{m}}(0)=-(1+\ln 4)\approx-2.386[Eq. (18)] below which three phases appear: lamellar (L), hexagonal (H), and inverted hexagonal (IH).
Only the uniform (U) phase appears aboveTc′T_{\text{c}}^{\prime}.
The phase coexistence regions separated by binodals (solid curves) are shaded in grey.
The two crosses in the lower right corner indicate the(ϕ0,T)(\phi_{0},T)values used later in Fig. 2 of Part II[31].
The part of the phase diagram withϕ0<0\phi_{0}<0is shown for illustration purposes alone and does not constitute a physical scenario for the problem treated here.

A representative phase diagram constructed from the above free-energy expressions for 2D modulations is shown in Fig.3in the(ϕ0,T)(\phi_{0},T)plane.
Here, we have set the long-wavelength modulus toM0=4M_{0}=4and all other free-energy parameters to unity, yielding an elastocapillary number ofγ0=4\gamma_{0}=4.
In polymer networks, we expecthhto be micron-scale or less, while interfaces form over a few Å, so𝒪​(γ0)∼1–10\mathcal{O}(\gamma_{0})\sim\text{1--10}corresponds to very soft networks with stiffness of a few kPa, comparable to certain hydrogels[49].

In the vicinity of the critical point, three principal phases appear: a uniform phase, a hexagonal or droplet phase consisting of solvent-rich domains embedded in a polymer-rich matrix, and a lamellar phase made up of alternating solvent-rich and polymer-rich bands.
An additional inverted-hexagonal phase is also present, where solvent-poor regions form isolated domains within a solvent-rich background.
In between these phases, four regions of phase coexistence appear.

Except at the critical point—where a second-order phase transition from the uniform to the lamellar phase can occur—all phase transitions displayed in Fig.3are first order.
The topology of the phase diagram closely resembles that of other systems with modulated phases such as ferromagnets[47], block copolymers[50], membranes[43,51], monolayers[41], etc., which is not surprising because their long-wavelength behavior is similar, as we saw from Eq. (31).

## III.3Lifshitz behavior

For smallqqandγ0≳1\gamma_{0}\gtrsim 1, we can expandF𝒒F_{\bm{q}}in Eq. (14) to𝒪​(q4)\mathcal{O}(q^{4}), resulting inF𝒒=a​(T−Tc)+M0+3​b​ψ02+(1−γ0)​κ​q2+12​γ0​κ​h2​q4.F_{\bm{q}}=a(T-T_{\text{c}})+M_{0}+3b\psi_{0}^{2}+(1-\gamma_{0})\kappa q^{2}+\frac{1}{2}\gamma_{0}\kappa h^{2}q^{4}.(31)

The form ofF𝒒F_{\bm{q}}considered here commonly appears in a wide variety of pattern-forming systems.
Examples include those described by Landau–Brazovskii or Swift–Hohenberg-type free energies, such as bilayer membranes[43], block copolymers[50], Langmuir monolayers[43], phase-field crystals[52], etc.
In the presence of fluctuations, these systems can display the so-called Lifshitz behavior[53,54].

To understand the effect of equilibrium fluctuations, we consider the structure factorS​(𝒒)∼F𝒒−1S(\bm{q})\sim F_{\bm{q}}^{-1}, Eq. (19), which is of the formS​(𝒒)=S​(0)​ττ+2​(1−γ0)​q2+γ0​h2​q4,S(\bm{q})=\frac{S(0)\tau}{\tau+2(1-\gamma_{0})q^{2}+\gamma_{0}h^{2}q^{4}},(32)

whereτ\tauis an effective temperature given byτ=2​κ−1​[a​(T−Tc)+3​b​ψ02+M].\tau=2\kappa^{-1}[a(T-T_{\text{c}})+3b\psi_{0}^{2}+M].(33)

The inverse Fourier transform ofS​(𝒒)S(\bm{q})is the real-space correlation function,G​(𝒙)=⟨δ​ψ​(𝒙)​δ​ψ​(0)⟩,G(\bm{x})=\langle\delta\psi(\bm{x})\delta\psi(0)\rangle,(34)

which quantifies the spatial correlation of composition fluctuations.

To streamline the discussions below, we introduce the dimensionless parameterχ=1−γ0γ0​τ​h2.\chi=\frac{1-\gamma_{0}}{\sqrt{\gamma_{0}\tau h^{2}}}.(35)

The correlation function associated with Eq. (32) takes the following form when|χ|<1\left|\chi\right|<1[55,56]:G​(𝒙)=G​(0)​e−|𝒙|/ζ​sinc⁡(2​π​|𝒙|d).G(\bm{x})=G(0)\,\mathrm{e}^{-\left|\bm{x}\right|/\zeta}\operatorname{sinc}\left(\frac{2\pi\left|\bm{x}\right|}{d}\right).(36)

The above correlation function describes damped oscillations with correlation lengthζ\zetaand perioddd, given byζ4=4​γ0​h2τ​(1+χ)2,d4=4​γ0​h2τ​(1−χ)2.\zeta^{4}=\frac{4\gamma_{0}h^{2}}{\tau(1+\chi)^{2}},\quad d^{4}=\frac{4\gamma_{0}h^{2}}{\tau(1-\chi)^{2}}.(37)

Using the above results, we can summarize the general phase behavior of elastomers in the(γ0,τ)(\gamma_{0},\tau)plane as follows (also illustrated in Fig.4).FIG. 4:Phase diagram in the(γ0,τ)(\gamma_{0},\tau)plane forh=1h=1,
whereτ\tauis the effective temperature defined in Eq. (33),
andγ0\gamma_{0}is the elastocapillary number, Eq. (16).
Second-order phase transition boundaries are shown as dashed red curves and correspond toτ=(1−γ0)2/γ0\tau=(1-\gamma_{0})^{2}/\gamma_{0}forγ0>1\gamma_{0}>1, and toτ=0\tau=0forγ0<1\gamma_{0}<1.
The solid blue curve, given byτ=−(2+6)​(1−γ0)2/γ0\tau=-(2+\sqrt{6})(1-\gamma_{0})^{2}/\gamma_{0}, marks a first-order triple line separating the lamellar phase from the two-phase coexistence region.
The solid black curve defined byτ=(1−γ0)2/γ0\tau=(1-\gamma_{0})^{2}/\gamma_{0}forγ0<1\gamma_{0}<1is the disorder line, which distinguishes the structured-disorderd regime withqm≠0q_{\text{m}}\neq 0fluctuations from the conventional disordered phase.
The vertical black line atγ0=1\gamma_{0}=1is the Lifshitz line, terminating at the Lifshitz point (black dot).
Both the disorder and Lifshitz lines represent regime crossovers rather than thermodynamic phase transitions.Table 1:Parameter definitions and their values.ParameterDescriptionValueaaQuadratic coefficient of the Landau free energyf​(ψ)f(\psi)[Eq. (3)]0.025​kPa​K−10.025{\kern 2.333pt}\text{kPa}{\kern 2.333pt}\text{K}^{-1}(25​J​m−3​K−125{\kern 2.333pt}\text{J}{\kern 2.333pt}\text{m}^{-3}{\kern 2.333pt}\text{K}^{-1})bbQuartic coefficient off​(ψ)f(\psi)2​kPa​K−12{\kern 2.333pt}\text{kPa}{\kern 2.333pt}\text{K}^{-1}(2×103​J​m−32\times 10^{3}\text{J}{\kern 2.333pt}\text{m}^{-3})TcT_{\text{c}}Critical temperature off​(ψ)f(\psi)70​C∘70{\kern 2.333pt}{{}^{\circ}}\text{C}(343​K343{\kern 2.333pt}\text{K})ϕc\phi_{\text{c}}Critical volume fraction off​(ψ)f(\psi)0.2nnMean number of crosslinks coarse-grained over [Eq. (43)]35C∞C_{\infty}Flory characteristic ratio of PDMS[57]6.8ϱ\varrhoMass density of dry PDMS[58]970​kg​m−3970{\kern 2.333pt}\text{kg}{\kern 2.333pt}\text{m}^{-3}ℓ\ellLength of the PDMS monomer [–Si​(CH3)2​O\text{Si}(\text{CH}_{3})_{2}\text{O}–][59]3.28​Å3.28{\kern 2.333pt}\text{\r{A}}m0m_{0}Molecular mass of PDMS monomer1.23×10−25​kg1.23\times 10^{-25}{\kern 2.333pt}\text{kg}(74.2​g​mol−174.2{\kern 2.333pt}\text{g}{\kern 2.333pt}\text{mol}^{-1})kB​Tk_{\text{B}}TThermal energy atT=300​KT=300{\kern 2.333pt}\text{K}4.14×10−21​J4.14\times 10^{-21}{\kern 2.333pt}\text{J}BBC∞​ϱ​ℓ2​kB​T/m0C_{\infty}\varrho\ell^{2}k_{\text{B}}T/m_{0}[Eq. (41)]0.024​kPa​µm20.024{\kern 2.333pt}\text{kPa}{\kern 2.333pt}\text{\textmu m}^{2}(2.4×10−11​J​m−12.4\times 10^{-11}{\kern 2.333pt}\text{J}{\kern 2.333pt}\text{m}^{-1})κ\kappaInterfacial parameter (∼kB​T/ℓ\sim k_{\text{B}}T/\ell[43])0.013​kPa​µm20.013{\kern 2.333pt}\text{kPa}{\kern 2.333pt}\text{\textmu m}^{2}(1.3×10−11​J​m−11.3\times 10^{-11}{\kern 2.333pt}\text{J}{\kern 2.333pt}\text{m}^{-1})

i) When the effective temperatureτ<0\tau<0andγ0<1\gamma_{0}<1, the system undergoes macrophase demixing and exists in a low-temperature coexistence phase.

ii) For|χ|<1\left|\chi\right|<1, bothζ\zetaandddremain finite.
The system is then in a structure-disordered phase, characterized by fluctuating mesoscopic structures embedded within an otherwise disordered medium[56].
The oscillatory decay ofG​(𝒙)G(\bm{x})reflects this behavior.

iii) Whenγ0<1\gamma_{0}<1, we have0<χ<10<\chi<1, and the structure factor exhibits a maximum
only atqm=0q_{\text{m}}=0, despite the oscillatory form of the correlation function.
Asχ\chiapproaches unity, the characteristic perioddddiverges.
The conditionχ=1\chi=1defines the disorder line[56].
Whenχ>1\chi>1, oscillations disappear andG​(𝒙)G(\bm{x})decays monotonically, corresponding to a fully disordered phase.
In the limitχ≫1\chi\gg 1, the positiveq2q^{2}contribution dominates the denominator of Eq. (32).
The resulting structure factor reduces to an Ornstein–Zernike form with purely exponential decay.

iv) The conditionχ=0\chi=0(equivalently,γ0=1\gamma_{0}=1) marks the Lifshitz line[53], which terminates at the Lifshitz point(γ0,τ)=(1,0)(\gamma_{0},\tau)=(1,0).
Forγ0>1\gamma_{0}>1and−1<χ<0-1<\chi<0, the structure factor develops a peak atqm2=h−2​(1−γ0−1)q_{\text{m}}^{2}=h^{-2}(1-\gamma_{0}^{-1}),
signaling the presence of fluctuating microstructures.
Asχ→−1\chi\to-1, the correlation length diverges, indicating the emergence of long-range order.
Finally, whenχ<−1\chi<-1stable microphases appear.

Because Eq. (31) belongs to the Swift–Hohenberg class of free energies,
critical fluctuations (beyond the mean-field treatment presented here)
are expected to modify the phase behavior near the order–disorder phase transition[60].
In particular, the second-order critical point is replaced by a line of fluctuation-induced first-order phase transitions,
an effect known to be important in block copolymers[61,62].
While the mean-field phase diagrams we have presented in Figs.3and4should describe
the phase behavior away from the critical point, fluctuations may result in direct phase transitions between
disordered and ordered phases, including the gyroid phase in 3D systems[63].

## IVComparison with experiments

The results reported in Ref.[14]are primarily for isotropically swollen elastomers with uniform stiffnesses,
and we only consider such systems in the present work (Part I).

## IV.1Rubber elasticity

The microphase domain size and the phase transition temperature in Ref.[14]are reported in terms of the Young’s modulusYYof the (dry) PDMS elastomer before swelling.
The Young’s modulus of the dry elastomer is related to the strand densityν\nuvia[64]Y=3​ν​kB​T.Y=3\nu k_{\text{B}}T.(38)

In elastomers and gels, a common measure of the network length scale is the end-to-end distance
of the strands between crosslinks[65,66].
If the strands are modeled as freely jointed chains with a Flory characteristic ratioC∞C_{\infty},
the root-mean-square end-to-end distanceξ\xiin the unswollen state follows from
the standard relation[57,64,67]ξ2=C∞​N​ℓ2.\xi^{2}=C_{\infty}N\ell^{2}.(39)

In this expression,NNdenotes the degree of polymerization, corresponding to
the number of monomers along a strand, whileℓ\ellis the length
of a single PDMS monomer [–Si​(CH3)2​O\text{Si}(\text{CH}_{3})_{2}\text{O}–].
For PDMS and other polymers with siloxane backbones, one can takeℓ\ellto be equal
to twice the Si–O bond length of1.64​Å1.64{\kern 2.333pt}\text{\r{A}}[59].

In polymer networks with strands of mean molecular massmsm_{\text{s}}and monomers of massm0m_{0}, the mean degree of polymerization of the strand between crosslinks isN=ms/m0N=m_{\text{s}}/m_{0}[67].
The strand massmsm_{\text{s}}can be determined fromYYin Eq. (38) by noting that the mean strand densityν=ϱ/ms\nu=\varrho/m_{\text{s}}, whereϱ\varrhois the mean mass density of the dry elastomer.
This yields an estimate forNNin terms of the Young’s modulusYYasN=msm0=3​ϱ​kB​TY​m0.N=\frac{m_{\text{s}}}{m_{0}}=\frac{3\varrho k_{\text{B}}T}{Ym_{0}}.(40)

For the PDMS elastomers considered in Ref.[14], we find thatNNvaries from aroundN=102N=10^{2}(forY=800​kPaY=800{\kern 2.333pt}\text{kPa}) to nearlyN=104N=10^{4}(forY=10​kPaY=10{\kern 2.333pt}\text{kPa}).
Using Eq. (40) in Eq. (39), the characteristic distanceξ\xibetween crosslinks in an elastomer takes the form[68,65]ξ≈(3​BY)1/2​withB=C∞​ϱ​ℓ2​kB​Tm0.\xi\approx\left(\frac{3B}{Y}\right)^{1/2}\kern 5.0pt\text{with}\quad B=\frac{C_{\infty}\varrho\ell^{2}k_{\text{B}}T}{m_{0}}.(41)

The material-specific parameterBBcarries dimensions of energy per unit length, and for PDMS, we estimateB≈0.024​kPa​µm2B\approx 0.024{\kern 2.333pt}\text{kPa}{\kern 2.333pt}\text{\textmu m}^{2}using the values of the relevant physical parameters compiled in Table1.
The mesh size predicted by Eq. (41) varies fromξ≈5​nm\xi\approx 5{\kern 2.333pt}\text{nm}atY=800​kPaY=800{\kern 2.333pt}\text{kPa}toξ≈50​nm\xi\approx 50{\kern 2.333pt}\text{nm}atY=10​kPaY=10{\kern 2.333pt}\text{kPa}.

Here, it is prudent to note that alternative estimates of the mesh sizeξ\ximay exhibit scaling behavior that differs from Eq. (41).
For example, if the network volume element is assumed to scale with the mesh size asξ3\xi^{3}, the strand density can be estimated asν∼ξ−3\nu\sim\xi^{-3}.
Puttingν∼ξ−3\nu\sim\xi^{-3}inY=3​ν​kB​TY=3\nu k_{\text{B}}Tleads to the scaling relationξ∼(3​kB​T/Y)1/3\xi\sim(3k_{\text{B}}T/Y)^{1/3}[1,69,70],
which is sometimes referred to as the rheological mesh size[71].
However, this estimate is only valid for weakly crosslinked networks, where it is reasonable to assume
that each volume element of the network contains a single strand.
By contrast, the estimate in Eq. (41) is consistent with the central assumption of rubber elasticity—namely
that it originates from changes in the configurational entropy of strands following Gaussian statistics
with a mean-square end-to-end distance given by Eq. (39).FIG. 5:(a) Scattering intensity peakqmq_{\text{m}}as a function of the Young’s modulusYY(log-log plot).
Experimental results from Ref.[14]are shown with circles.
The dashed line is the theoretical prediction from Eq. (45),qm∼Y1/2q_{\text{m}}\sim Y^{1/2}.
(b) Microphase separation temperatureTmT_{\text{m}}as function ofYYfor elastomers with different initial swelling temperaturesTsT_{\text{s}}, which determine the value of the polymer volume fractionϕ0\phi_{0}at equilibrium.
Experimental values are shown as circles, and theoretical estimates from Eq. (46) are shown as crosses.
The dashed guidelines illustrate the linearity ofTmT_{\text{m}}withYY.
(c)TmT_{\text{m}}as a function ofϕ0\phi_{0}for differentYYusing Eq. (46) (dashed curves) and experimental results (circles).
All physical parameters used in obtaining the theoretical results have been compiled in Table1.

## IV.2Scaling behavior and phase diagram

From Eq. (17) we see that apart from the critical volume fractionϕc\phi_{\text{c}}andkB​Tk_{\text{B}}T,
the long-wavelength longitudinal modulusM0M_{0}of isotropically swollen elastomers only involves the strand densityν\nu.
One can thus use Eq. (38) to eliminateν\nuand writeM0M_{0}in terms of the dry Young’s modulusYYasM0=13​(ϕc−1+ϕc−5/3)​Y.M_{0}=\frac{1}{3}\left(\phi_{\text{c}}^{-1}+\phi_{\text{c}}^{-5/3}\right)Y.(42)

The typical intermolecular spacing (roughly equal to the monomer sizeℓ\ell) is only a few Å, much smaller than the mesh sizeξ\xi.
As we have remarked previously, thermodynamic interactions between the polymer and the solvent occur at intermolecular length scales, whereas the polymer network can be considered as a continuous elastic medium only at length scales considerably larger thanξ\xi, though proportional to it.
Based on this, for isotropically swollen elastomers, we take the coarse-graining length scale appearing in Eq. (7) to beh=n​ξ​ϕc−1/3≈n​(3​BY)1/2​ϕc−1/3.h=n\,\xi\,\phi_{\text{c}}^{-1/3}\approx n\left(\frac{3B}{Y}\right)^{1/2}\phi_{\text{c}}^{-1/3}.(43)

Here, the dimensionless factorn=h/ξn=h/\xican be interpreted as the average number of crosslinks included along each spatial direction during coarse-graining (see Fig.1).
Its precise value depends on the kernel employed in Eq. (7) and can be determined only by comparing theoretical predictions with experimental data.
In general, broader, long-range kernels lead to smaller values ofnn.
Finally, the additional factor ofϕc−1/3\phi_{\text{c}}^{-1/3}in Eq. (43) reflects the change in the mesh size due to isotropic swelling.

Using Eqs. (42) and (43), we find the elastocapillary numberγ0\gamma_{0}of an isotropically swollen elastomer to beγ0=M0​h2κ=B​n2​κ−1​(ϕc−7/3+ϕc−5/3).\gamma_{0}=\frac{M_{0}h^{2}}{\kappa}=Bn^{2}\kappa^{-1}\left(\phi_{\text{c}}^{-7/3}+\phi_{\text{c}}^{-5/3}\right).(44)

AsM0∼YM_{0}\sim Yandh2∼ξ2∼Y−1h^{2}\sim\xi^{2}\sim Y^{-1}, it is important to note that the elastocapillary numberγ0\gamma_{0}is independent of the Young’s modulusYY.
From the parameter values compiled in Table1, we see thatγ0≫1\gamma_{0}\gg 1, even whenn=1n=1.

The wavenumberqmq_{\text{m}}at which the scattering intensity peaks is obtained from Eq. (15) asqm2=h−2​ln⁡γ0=Y​(ϕc2/33​B​n2)​ln⁡γ0.q_{\text{m}}^{2}=h^{-2}\ln\gamma_{0}=Y\left(\frac{\phi_{\text{c}}^{2/3}}{3Bn^{2}}\right)\ln\gamma_{0}.(45)

In Fig.5(a), we compare the prediction of Eq. (45) with the experimental results of Ref.[14]and find good agreement between the two.
The scalingqm2∼Yq_{\text{m}}^{2}\sim Yin Eq. (45) is very different from the naive estimate
one might expect based on dimensional grounds alone, e.g.,qm2=(Y/kB​T)2/3q_{\text{m}}^{2}=(Y/k_{\text{B}}T)^{2/3}.
For the experimental ranges ofY≈10​–​800​kPaY\approx 10\text{--}800{\kern 2.333pt}\text{kPa}, the naive estimate gives a domain size of2​π​qm−1≈10​–​60​nm2\pi q_{\text{m}}^{-1}\approx 10\text{--}60{\kern 2.333pt}\text{nm}, which is two orders of magnitude smaller than the experimental observations of micron-sized domains.

One can also estimate the microphase separation temperature from Eq. (18) asTm​(ψ0)\displaystyle T_{\text{m}}(\psi_{0})=Tc−3​b​a−1​ψ02\displaystyle=T_{\text{c}}-3ba^{-1}\psi_{0}^{2}−Y​a−1​(ϕc2+ϕc2/31+ϕc2/3)​(1+ln⁡γ0).\displaystyle\quad-{Y}a^{-1}\left(\frac{\phi_{\text{c}}^{2}+\phi_{\text{c}}^{2/3}}{1+\phi_{\text{c}}^{2/3}}\right)\left(1+\ln\gamma_{0}\right).(46)

A comparison of the phase transition temperaturesTmT_{\text{m}}, predicted from the above equation, with the experimentally
measured ones, is showcased in Figs.5(b) and5(c) using all available data from Ref.[14].
We again observe good agreement, withTmT_{\text{m}}decreasing linearly withYY, as predicted.

As we discussed in Sec.III, we can construct a phase diagram in the weak-segregation limit using the single-mode approximation.
Such a phase diagram for an elastomer of stiffnessY=800​kPaY=800{\kern 2.333pt}\text{kPa}is presented in Fig.6.
The phase diagram is in good agreement with experimental observations and correctly predicts the onset of microphase separation.
The first-order phase transition lines separating the various phases terminate at a critical point,Tc′=Tm​(ϕc)T_{\text{c}}^{\prime}=T_{\text{m}}(\phi_{\text{c}}),
where a second-order transition between the uniform and lamellar phases is found.
The associated coexistence regions are extremely narrow and have therefore been omitted.
Their small widths may help explain the reported absence of hysteresis in EMPS[14].

Experiments indicate that droplets (hexagonal phase) appear in soft elastomers withY≲40​kPaY\lesssim 40{\kern 2.333pt}\text{kPa},
whereas stiffer elastomers exhibit only channel-like structures, somewhat analogous to a lamellar phase.
Nevertheless, due to the generic topology of the theoretical phase diagram, we expect the emergence of
the hexagonal phase for off-critical temperature quenches, regardless of stiffness.
This discrepancy suggests that additional mechanisms, such as shear deformations or nonlinear effects, which have been neglected in our study,
likely govern the formation of channel-like structures in stiffer samples.

We note that, for isotropically swollen elastomers, the scalingqm2∼Yq_{\text{m}}^{2}\sim Ydoes not depend on the specific kernel used in Eq. (7).
For a general isotropic and normalized kernelK​(𝒙)K(\bm{x}), the effective longitudinal modulus,
Eq. (12), can be written asM𝒒=M0​K𝒒M_{\bm{q}}=M_{0}K_{\bm{q}}.
SinceK​(𝒙)K(\bm{x})is normalized, its Fourier transformK𝒒K_{\bm{q}}is dimensionless.
Furthermore, becausehhis the only length scale entering the kernel,K𝒒K_{\bm{q}}can depend only on the dimensionless quantityh​qhq.
Isotropy then requiresK𝒒K_{\bm{q}}to be an even function of𝒒\bm{q}, which impliesM𝒒=M0​K𝒒​(h2​q2)M_{\bm{q}}=M_{0}K_{\bm{q}}(h^{2}q^{2}).
Hence, the wavenumberqmq_{\text{m}}at which the scattering intensityS​(𝒒)∼(κ​q2+M𝒒)−1S(\bm{q})\sim(\kappa q^{2}+M_{\bm{q}})^{-1}peaks is the solution of1+γ0​K𝒒′​(h2​qm2)=0.1+\gamma_{0}K_{\bm{q}}^{\prime}(h^{2}q_{\text{m}}^{2})=0.(47)

As beforeM0∼YM_{0}\sim Yandh2∼Y−1h^{2}\sim Y^{-1}making the elastocapillary numberγ0=M0​h2/κ\gamma_{0}=M_{0}h^{2}/\kappaindependent of the Young’s modulusYY.
Hence, anyqmq_{\text{m}}obtained as a solution to the above equation must scale asqm2∼h−2∼Yq_{\text{m}}^{2}\sim h^{-2}\sim Y.
A similar argument applies to the linear dependence of the phase transition temperatureTmT_{\text{m}}onYYas in Eq. (46).FIG. 6:Phase diagram in the polymer volume fraction-temperature(ϕ0,T)(\phi_{0},T)plane for an isotropically swollen elastomer with a dry Young’s modulusY=800​kPaY=800\,{\kern 2.333pt}{\text{kPa}}.
Open circles indicate experimental data taken from Ref.[14]for an elastomer with the same stiffness.
Other material parameters are listed in Table1.
The binodals (phase boundaries) are shown as solid curves.
The phase coexistence regions are extremely narrow and have not been included.
The dashed curve corresponds to the microphase separation temperatureTm​(ϕ0)T_{\text{m}}(\phi_{0})obtained from linear stability analysis,
Eq. (46) [also presented in Fig.5(c)].
The binodals converge at a shifted critical pointTc′=Tm​(ϕc)T_{\text{c}}^{\prime}=T_{\text{m}}(\phi_{\text{c}}).

## VEMPS and de Gennes’ model of crosslinked blends

An early model examining the effect of elasticity on phase separation was suggested by de Gennes for crosslinked AB polymer blends[1].
While an uncrosslinked blend undergoes macroscopic demixing below its critical temperature,
the presence of crosslinks introduces elastic effects that can stabilize microphases with a finite characteristic length scale.
De Gennes’ work on blends is in the same spirit as EMPS, and despite being extensively cited in recent years, a direct comparison to EMPS appears to be lacking in the literature.
We therefore briefly summarize the theory for blends before highlighting its similarities and differences with our approach for EMPS.

Let𝒙A\bm{x}_{\text{A}}and𝒙B\bm{x}_{\text{B}}denote the coordinates of points belonging to polymers A and B, respectively.
A “polarization” field𝑷\bm{P}may then be defined as the displacement between their local centers of mass:𝑷=⟨𝒙A⟩−⟨𝒙B⟩\bm{P}=\langle\bm{x}_{\text{A}}\rangle-\langle\bm{x}_{\text{B}}\rangle, where⟨⋅⟩\langle\cdot\rangledenotes the average over a small spatial region.
In the uniform phase,𝑷=0\bm{P}=0.
The scalar order parameterρ\rho, which describes local compositional fluctuations during phase separation, is identified with the effective
“charge” density associated with𝑷\bm{P}. Extending the electrostatic analogy leads to Gauss’ law∇⋅𝑷=−ρ.\bm{\nabla\cdot}\bm{P}=-\rho.(48)

The total elastic energy is taken to be the electrostatic self-energy associated with the bound charges.
It takes the formℱel=12​C​∫d3​x​|𝑷|2,\mathscr{F}_{\text{el}}=\frac{1}{2}C\int\mathrm{d}^{3}x\,\left|\bm{P}\right|^{2},(49)

where the parameterCCis the strength of self-interaction.
Using Eq. (48), we can writeℱel\mathscr{F}_{\text{el}}entirely in terms ofρ\rhoif only contributions from the longitudinal modes (i.e., those along𝒒\bm{q}) are considered.
Then, after including the usual Ginzburg–Landau terms [see Eq. (2)], the total Gaussian (quadratic)
free energy in Fourier space becomes[1]ℱG=12​∫d3​q(2​π)3​[a​(T−Tc)+κ​q2+Cq2]​ρ𝒒​ρ−𝒒.\mathscr{F}_{\text{G}}=\frac{1}{2}\int\frac{\mathrm{d}^{3}q}{(2\pi)^{3}}\left[a(T-T_{\text{c}})+\kappa q^{2}+\frac{C}{q^{2}}\right]\rho_{\bm{q}}\rho_{-\bm{q}}.(50)

Similar free energies have also been proposed to explain microphase separation in diblock copolymers[72].
At sufficiently low temperature, such free energies result in the emergence of microphases owing to competition between the interfacial and elastic terms,κ​q2\kappa q^{2}andC​q−2Cq^{-2}.
The scattering peakqmq_{\text{m}}in the static structure factor associated with this microphase separation isqm4=C/κq_{\text{m}}^{4}=C/\kappa.

De Gennes’ phenomenological model is intended to describe the competition between interfacial effects whose strength
is controlled byκ\kappaand elastic effects, which become relevant only at length scales close toξ\xi, the end-to-end distance between crosslinks.
Sinceκ\kappaandξ\xiprovide the only relevant energy and length scale, dimensional analysis naturally leads to the choiceC=κ/ξ4C=\kappa/\xi^{4}.
Asξ∼N1/2\xi\sim N^{1/2}[Eq. (39)] we see that the scattering peakqmq_{\text{m}}scales with the numberNNof monomers between the crosslinks asqm=(C/κ)1/4∼ξ−1∼N−1/2.q_{\text{m}}=\left(C/\kappa\right)^{1/4}\sim\xi^{-1}\sim N^{-1/2}.(51)

Similarly, one can show that the phase transition temperatureTmT_{\text{m}}decreases linearly withN−1N^{-1}.

Given that the underlying motivation of our approach is similar to that of de Gennes’, we can compare the two as follows:

i) The Gauss law in Eq. (48) is analogous to the volume-conservation constraint in Eq. (8).
Here,𝑷\bm{P}plays a role similar to the displacement field𝒖\bm{u}, whereasρ\rhocorresponds to the uncoarse-grained order parameterψ\psi.
The key distinction lies in the coarse-graining procedure: in our approach, the order parameter is coarse-grained again,
whereas in Eq. (48) it is𝑷\bm{P}that is coarse-grained (once, by construction).

ii) Our model employs the conventional elastic energy density, Eq. (4),
which is quadratic in the strain and, therefore, depends on gradients of the displacement field𝒖\bm{u}.
In contrast, Eq. (49) assumes an elastic energy that is quadratic in the displacement field (𝑷\bm{P}) itself.
The domain-size selection in Eq. (51) is entirely a consequence of this particular choice of elastic energy.

iii) Both our model and Eq. (50) assume that the domain-size selection is governed solely by the longitudinal modes’ contribution to the elastic energy.

iv) In both theories, the key length scale isξ\xi, the end-to-end distance between crosslinks.
It is this choice that gives rise to the experimentally observed scaling behavior in both theories.
In Eq. (50),ξ\xiis only used to set the strengthCCof the elastic self-interaction, whereas in our case,
it governs the length scale of nonlocal coarse-graining and is related to the elastic modulus [via Eq. (41)].

v) From Eq. (40), we see that the dry Young’s modulus follows the scalingY∼N−1Y\sim N^{-1}with the number of monomersNN.
Therefore, from Eqs. (45) and (46) of our model, we see that the EMPS phase transition temperatureTmT_{\text{m}}decreases linearly withN−1N^{-1}with the scattering peakqm∼N−1/2q_{\text{m}}\sim N^{-1/2}, similar to blends.

vi) Even though the structure factor associated with Eq. (50) vanishes as𝒒→0\bm{q}\to 0,
experiments on crosslinked blends[73]have found a nonzeroS​(𝒒=0)S(\bm{q}\,{=}\,0), motivating alternative theoretical descriptions[74].
In comparison, Eqs. (14) and (19) from our model for EMPS predict a nonzeroS​(𝒒=0)S(\bm{q}\,{=}\,0).
This suggests that it can be extended to study blends as well.

## VIConcluding remarks

We have presented a theoretical framework to explain elastic microphase separation (EMPS). Namely, the formation of microphases
of finite size in solvent-swollen elastomers[14].
EMPS arises from a mismatch between the length scales governing elasticity and thermodynamics in elastomeric polymer networks.
Unlike previous approaches[21,22], including our own[27],
which relied on nonstandard theories of elasticity[30], the current framework employs a nonlocal coupling between thermodynamics and makes use of conventional elasticity.
This approach provides an intuitive physical basis for EMPS, while remaining generalizable and compatible
with established theories of phase separation and density fluctuations in gels[18,9,37].

The predictions of the present framework can be directly compared with existing experimental results on EMPS[14].
In particular, the theory captures the dependence of both the characteristic domain size and the phase transition temperature on elastomer stiffness.
For isotropically swollen elastomers, the predicted scaling relations are in good quantitative agreement with the experimentally reported trends[14].
This agreement shows that network elasticity plays a central role in controlling the morphology and phase behavior of elastomers.

Our theory predicts that EMPS in isotropically swollen elastomers is a first-order phase transition,
consistent with known results for other systems exhibiting
microphase separation, such as block copolymers[50].
The experimentally observed hysteresis-free and reversible nature of EMPS can be explained
by the vanishingly small phase-coexistence regions [see Fig.6].
Finally, as we have demonstrated, EMPS exhibits a scaling behavior similar to that observed
in crosslinked polymer blends[73]and predicted earlier by de Gennes[1].
The phase behavior of crosslinked polymer blends and gels can be drastically altered by anisotropic effects[9].
Extending the present framework to account for anisotropy in elastomers is therefore a natural next step and will be the focus of Part II[31].

Elastomers exhibit a wide range of complex behaviors.
Other natural extensions to the questions we have considered in this paper include the phase-separation kinetics, extensions to ternary and multicomponent systems, volume phase transitions, etc.[9].
Our framework may also be applied to similar systems where elastic and thermodynamic effects are often governed by distinct length scales, such as certain porous materials[75,76,77]and colloidal suspensions[78].

## Acknowledgements

M.M. thanks L. Mahadevan and Mehrana Nejad for fruitful discussions.
H.D. acknowledges support from the Israel Science Foundation (ISF Grant No. 1611/24).
D.A. acknowledges support from the Israel Science Foundation (ISF Grant No. 226/24).

## References
- de Gennes [1979]P.-G. de Gennes, Effect of cross-links
on a mixture of polymers,J. Phys. Lett.40, 69 (1979).
- Panyukov and Rabin [1996]S. Panyukov and Y. Rabin, Statistical physics of
polymer gels,Phys. Rep.269, 1 (1996).
- Peleget al.[2007]O. Peleg, M. Kröger,
I. Hecht, and Y. Rabin, Filamentous networks in phase-separating two-dimensional
gels,EPL77, 58007 (2007).
- Tateno and Tanaka [2021]M. Tateno and H. Tanaka, Power-law coarsening in
network-forming phase separation governed by mechanical relaxation,Nat. Commun.12, 912 (2021).
- Hymanet al.[2014]A. A. Hyman, C. A. Weber, and F. Jülicher, Liquid-liquid phase separation in
biology,Annu. Rev. Cell Dev. Biol.30, 39 (2014).
- Tanaka [2022]H. Tanaka, Viscoelastic phase
separation in biological cells,Commun. Phys.5, 167 (2022).
- Zwickeret al.[2025]D. Zwicker, O. W. Paulin, and C. ter
Burg, Physics of droplet regulation
in biological cells,Rep. Prog. Phys.88, 116601 (2025).
- Onuki [1989a]A. Onuki, Long-range interactions
through elastic fields in phase-separating solids,J. Phys. Soc. Jpn.58, 3069 (1989a).
- Onuki [2002]A. Onuki,Phase Transition
Dynamics(Cambridge University Press, Cambridge, 2002).
- Loudetet al.[2000]J.-C. Loudet, P. Barois, and P. Poulin, Colloidal ordering from phase
separation in a liquid-crystalline continuous phase,Nature407, 611
(2000).
- Nishimori and Onuki [1990]H. Nishimori and A. Onuki, Pattern formation in
phase-separating alloys with cubic symmetry,Phys. Rev. B42, 980 (1990).
- Cahn [1961]J. W. Cahn, On spinodal decomposition,Acta Metall.9, 795 (1961).
- Fratzlet al.[1999]P. Fratzl, O. Penrose, and J. L. Lebowitz, Modeling of phase separation in alloys
with coherent elastic misfit,J. Stat. Phys.95, 1429 (1999).
- Fernández-Ricoet al.[2024]C. Fernández-Rico, S. Schreiber, H. Oudich,
C. Lorenz, A. Sicher, T. Sai, V. Bauernfeind, S. Heyden, P. Carrara, L. D. Lorenzis, R. W. Style, and E. R. Dufresne, Elastic
microphase separation produces robust bicontinuous materials,Nat. Mater.23, 124 (2024).
- Tanakaet al.[1977]T. Tanaka, S. Ishiwata, and C. Ishimoto, Critical behavior of density
fluctuations in gels,Phys. Rev. Lett.38, 771 (1977).
- Tanaka [1978]T. Tanaka, Dynamics of critical
concentration fluctuations in gels,Phys. Rev. A17, 763 (1978).
- Li and Tanaka [1989]Y. Li and T. Tanaka, Study of the universality class of the
gel network system,J. Chem. Phys.90, 5161 (1989).
- Onuki [1993]A. Onuki, Theory of phase transition in polymer gels, inResponsive Gels: Volume Transitions I, edited by K. Dušek (Springer, Berlin, 1993) pp. 63–121.
- Onuki [1989b]A. Onuki, Ginzburg–Landau approach
to elastic effects in the phase separation of solids,J. Phys. Soc. Jpn.58, 3065 (1989b).
- Oudichet al.[2026]H. Oudich, P. Carrara, and L. De Lorenzis, Phase-field modeling of elastic
microphase separation,J. Mech. Phys. Solids206, 106380 (2026).
- Qianget al.[2024]Y. Qiang, C. Luo, and D. Zwicker, Nonlocal elasticity yields equilibrium patterns in
phase separating systems,Phys. Rev. X14, 021009 (2024).
- Paulinet al.[2026]O. W. Paulin, Y. Qiang, and D. Zwicker, Dynamics of phase separation in non-local elastic
networks,Soft Matter22, 1098 (2026).
- Fernández-Ricoet al.[2026]C. Fernández-Rico, R. W. Style, S. Heyden,
S. Wang, P. D. Olmsted, and E. R. Dufresne, Thermodynamics of microphase separation in a swollen,
strain-stiffening polymer network,Soft Matter22, 330 (2026).
- Wang and Olmsted [2025]S. Wang and P. D. Olmsted, The roles of elasticity and
dimension in liquid-gel phase separation (2025),arXiv:2510.05415
[cond-mat.soft].
- Theweset al.[2026]F. C. Thewes, Y. Qiang,
O. W. Paulin, and D. Zwicker, Phase separation with nonlocal interactions,Phys. Rev. Res.8, L022023 (2026).
- Safran [2026]S. A. Safran, Scaling of poroelastic
coarsening and elastic arrest in crosslinked gels (2026),arXiv:2602.09166
[cond-mat.soft].
- Mannattilet al.[2025]M. Mannattil, H. Diamant, and D. Andelman, Theory of microphase separation in
elastomers,Phys. Rev. Lett.135, 108101 (2025).
- Onuki and Puri [1999]A. Onuki and S. Puri, Spinodal decomposition in gels,Phys. Rev. E59, R1331 (1999).
- Eringenet al.[1977]A. Eringen, C. Speziale, and B. Kim, Crack-tip problem in non-local elasticity,J. Mech. Phys. Solids25, 339 (1977).
- Eringen [1987]A. C. Eringen, Theory of nonlocal
elasticity and some applications, Res. Mech.21, 313 (1987).
- [31]M. Mannattil, D. Andelman, and H. Diamant,
Phase transitions and microphases in elastomers. II. Anisotropy-driven
morphologies, in preparation.
- Flory [1953]P. J. Flory,Principles of Polymer
Chemistry(Cornell University Press, Ithaca, NY, 1953).
- Treloar [1975]L. R. G. Treloar,The
Physics of Rubber Elasticity(Oxford University
Press, New York, NY, 1975).
- Doi [2009]M. Doi, Gel dynamics,J. Phys. Soc. Jpn.78, 052001 (2009).
- Yamaueet al.[2000]T. Yamaue, T. Taniguchi, and M. Doi, Shrinking dynamics and patterns of gels,AIP Conf. Proc.519, 584 (2000).
- Yamaueet al.[2004]T. Yamaue, T. Taniguchi, and M. Doi, The simulation of the swelling and deswelling
dynamics of gels,Mol. Phys.102, 167 (2004).
- Dimitriyevet al.[2019]M. S. Dimitriyev, Y.-W. Chang, P. M. Goldbart, and A. Fernández-Nieves, Swelling
thermodynamics and phase transitions of polymer gels,Nano Futures3, 042001 (2019).
- Jia and Muthukumar [2021]D. Jia and M. Muthukumar, Theory of charged
gels: Swelling, elasticity, and dynamics,Gels7, 49
(2021).
- Onuki [1988]A. Onuki, Phase transition in
deformed gels,J. Phys. Soc. Jpn.57, 699 (1988).
- Onuki [1992]A. Onuki, Scattering from deformed
swollen gels with heterogeneities,J. Phys. II France2, 45 (1992).
- Andelmanet al.[1987]D. Andelman, F. Broçhard, and J.-F. Joanny, Phase transitions in
Langmuir monolayers of polar molecules,J. Chem. Phys.86, 3673
(1987).
- de Souzaet al.[2026]J. P. de Souza, A. Vodinh-Ho, and H. A. Stone, Charge stabilization and
dynamics in polyelectrolyte phase separation,Soft Matter (2026).
- Leibler and Andelman [1987]S. Leibler and D. Andelman, Ordered and curved
meso-structures in membranes and amphiphilic films,J. Phys. France48, 2013 (1987).
- Seul and Andelman [1995]M. Seul and D. Andelman, Domain shapes and
patterns: The phenomenology of modulated phases,Science267, 476 (1995).
- Roncerayet al.[2022]P. Ronceray, S. Mao,
A. Košmrlj, and M. P. Haataja, Liquid demixing in elastic networks:
Cavitation, permeation, or size selection?,EPL137, 67001 (2022).
- Liuet al.[2019]Q. Liu, T. Ouchi, L. Jin, R. Hayward, and Z. Suo, Elastocapillary crease,Phys. Rev. Lett.122, 098003 (2019).
- Garel and Doniach [1982]T. Garel and S. Doniach, Phase transitions with
spontaneous modulation-the dipolar Ising ferromagnet,Phys. Rev. B26, 325 (1982).
- Elder and Grant [2004]K. R. Elder and M. Grant, Modeling elastic and plastic
deformations in nonequilibrium processing using phase field crystals,Phys. Rev. E70, 051605 (2004).
- Luoet al.[2022]T. Luo, B. Tan, L. Zhu, Y. Wang, and J. Liao, A review on the design of hydrogels with different stiffness and
their effects on tissue repair,Front. Bioeng. Biotechnol.10, 817391 (2022).
- Fredrickson and Helfand [1987]G. H. Fredrickson and E. Helfand, Fluctuation effects in
the theory of microphase separation in block copolymers,J. Chem. Phys.87, 697
(1987).
- Yu and Košmrlj [2025]Q. Yu and A. Košmrlj, Pattern formation of
lipid domains in bilayer membranes,Soft Matter21, 4288 (2025).
- Elderet al.[2002]K. R. Elder, M. Katakowski,
M. Haataja, and M. Grant, Modeling elasticity in crystal growth,Phys. Rev. Lett.88, 245701 (2002).
- Hornreichet al.[1975]R. M. Hornreich, M. Luban, and S. Shtrikman, Critical behavior at the onset ofk→\vec{k}-space instability on theλ\lambdaline,Phys. Rev. Lett.35, 1678 (1975).
- Chaikin and Lubensky [1995]P. M. Chaikin and T. C. Lubensky,Principles of
Condensed Matter Physics(Cambridge University
Press, New York, NY, 1995).
- Teubner and Strey [1987]M. Teubner and R. Strey, Origin of the scattering
peak in microemulsions,J. Chem. Phys.87, 3195 (1987).
- Komura [2007]S. Komura, Mesoscale structures in
microemulsions,J. Phys.: Condens. Matter19, 463101 (2007).
- Rubinstein and Colby [2003]M. Rubinstein and R. H. Colby,Polymer Physics(Oxford University Press, Oxford, 2003).
- Kuo [1999]A. C. M. Kuo, Poly (dimethylsiloxane), inPolymer Data Handbook, edited by J. E. Mark (Oxford
University Press, New York, NY, 1999) pp. 411–435.
- Mark [2004]J. E. Mark, Some interesting things
about polysiloxanes,Acc. Chem. Res.37, 946 (2004).
- Brazovskii [1975]S. A. Brazovskii, Phase transition of an
isotropic system to a nonuniform state, Sov. Phys. JETP41, 85 (1975).
- Kogaet al.[1999]T. Koga, T. Koga, K. Kimishima, and T. Hashimoto, Long-range density fluctuations in a symmetric diblock
copolymer,Phys. Rev. E60, R3501 (1999).
- Komura and Shimokawa [2008]S. Komura and N. Shimokawa, Dynamical Brazovskii
effect,Soft Mater.6, 85 (2008).
- Hamley and Podneks [1997]I. W. Hamley and V. E. Podneks, On the
Landau–Brazovskii theory for block copolymer melts,Macromolecules30, 3701 (1997).
- Tanaka [2011]F. Tanaka,Polymer Physics:
Applications to Molecular Association and Thermoreversible Gelation(Cambridge University Press, New
York, NY, 2011).
- Parrishet al.[2017]E. Parrish, M. A. Caporizzo, and R. J. Composto, Network confinement and
heterogeneity slows nanoparticle diffusion in polymer gels,J. Chem. Phys.146, 203318 (2017).
- Richbourg and Peppas [2020]N. R. Richbourg and N. A. Peppas, The swollen polymer
network hypothesis: Quantitative models of hydrogel swelling, stiffness, and
solute transport,Prog. Polym. Sci.105, 101243 (2020).
- Lodge and Hiemenz [2020]T. P. Lodge and P. C. Hiemenz,Polymer Chemistry, 3rd ed. (CRC Press, Boca Raton, FL, 2020).
- Yooet al.[2006]S. H. Yoo, C. Cohen, and C.-Y. Hui, Mechanical and swelling properties of PDMS
interpenetrating polymer networks,Polymer47, 6226 (2006).
- Haggertyet al.[1988]L. Haggerty, J. H. Sugarman, and R. K. Prud’homme, Diffusion of polymers
through polyacrylamide gels,Polym.29, 1058 (1988).
- Tsujiet al.[2018]Y. Tsuji, X. Li, and M. Shibayama, Evaluation of mesh size in model polymer networks
consisting of tetra-arm and linear poly(ethylene glycol)s,Gels4, 50
(2018).
- Wisniewskaet al.[2018]M. A. Wisniewska, J. G. Seland, and W. Wang, Determining the scaling of gel mesh
size with changing crosslinker concentration using dynamic swelling,
rheometry, and PGSE NMR spectroscopy,J. Appl. Polym. Sci.135, 46695 (2018).
- Ohta and Kawasaki [1986]T. Ohta and K. Kawasaki, Equilibrium morphology
of block copolymer melts,Macromolecules19, 2621 (1986).
- Briber and Bauer [1988]R. M. Briber and B. J. Bauer, Effect of crosslinks on the
phase separation behavior of a miscible polymer blend,Macromolecules21, 3296 (1988).
- Readet al.[1995]D. J. Read, M. G. Brereton, and T. C. McLeish, Theory of the order-disorder phase
transition in cross-linked polymer blends,J. Phys. II France5, 1679 (1995).
- Coussy [2004]O. Coussy,Poromechanics(John Wiley & Sons, New York,
NY, 2004).
- Derret al.[2020]N. J. Derr, D. C. Fronk,
C. A. Weber, A. Mahadevan, C. H. Rycroft, and L. Mahadevan, Flow-driven branching in a frangible porous medium,Phys. Rev. Lett.125, 158002 (2020).
- Paulinet al.[2022]O. W. Paulin, L. C. Morrow,
M. G. Hennessy, and C. W. MacMinn, Fluid–fluid phase separation in a
soft porous medium,J. Mech. Phys. Solids164, 104892 (2022).
- Tanakaet al.[2005]H. Tanaka, Y. Nishikawa, and T. Koyama, Network-forming phase separation of
colloidal suspensions,J. Phys.: Condens. Matter17, L143 (2005).

## 


- 


Major funding support from
