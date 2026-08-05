# Fate of moiré flat bands for a weakly repulsive Bose-Einstein condensate in one-dimensional $\mathcal{PT}$-symmetric bichromatic optical lattices

**arXiv ID**: 2608.01680v1
**Authors**: Enhong Cheng, Yu Tan, Yanzhen Xu, Li-Jun Lang
**Published**: 2026-08-03
**Categories**: cond-mat.quant-gas, quant-ph
**Comments**: 14 pages, 7 figures
**HTML URL**: https://arxiv.org/html/2608.01680v1

## Abstract

One-dimensional (1D) superlattices provide one simplified platform for exploring moiré physics from a low-dimensional perspective, with the ratio of lattice constants playing a role analogous to the twist angle in two-dimensional bilayers. Here, we propose a 1D $\mathcal{PT}$-symmetric bichromatic optical lattice for a weakly repulsive Bose-Einstein condensate and investigate how the interplay of dissipation and interaction impacts the lowest moiré flat band.   Without interaction, we find that the lowest-band flatness induced by commensurate ratios exhibits a parity-dependent response to the $\mathcal{PT}$-symmetric imaginary potential due to the distinct $\mathcal{PT}$ pairing mechanism for the energy spectrum.   For ratios with even denominators (i.e., even parities), the level attraction and thus the $\mathcal{PT}$-symmetry breaking occur within the lowest two bands, leading to a monotonic broadening of the lowest flat band, whereas odd denominators (i.e., odd parities) yield a nonmonotonic response due to the $\mathcal{PT}$-symmetry breaking within the second and the third lowest bands instead while the lowest band remains purely real.   This parity-dependent phenomenon can be understood by the perturbation theory.   Furthermore, by solving the Gross-Pitaevskii equation, we also find that although the weak repulsive interaction can broaden the moiré bands alone, the combined effects of interaction and imaginary potential also lead to parity-dependent behaviors.   For even parities, band flattening is consistently diminished, whereas for odd parities, the imaginary potential can either enhance or reduce the degree of flattening.   These results pave the way for experimental studies of dissipation and interaction effects on band flatness in moiré systems.

## Full Text

Fate of moiré flat bands for a weakly repulsive Bose-Einstein condensate in one-dimensional 𝒫⁢𝒯-symmetric bichromatic optical lattices

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.01680v1 [cond-mat.quant-gas] 03 Aug 2026††thanks:They contribute equally to this work.††thanks:They contribute equally to this work.

## Fate of moiré flat bands for a weakly repulsive Bose-Einstein condensate in one-dimensional𝒫​𝒯\mathcal{PT}-symmetric bichromatic optical latticesEnhong ChengSchool of Physics, South China Normal University, Guangzhou 510006, ChinaYu TanSchool of Physics, South China Normal University, Guangzhou 510006, ChinaYanzhen XuSchool of Physics, South China Normal University, Guangzhou 510006, ChinaLi-Jun Langljlang@scun.edu.cnSchool of Physics, South China Normal University, Guangzhou 510006, ChinaGuangdong Provincial Key Laboratory of Quantum Engineering and Quantum Materials, South China Normal University, Guangzhou 510006, ChinaGuangdong-Hong Kong Joint Laboratory of Quantum Matter, South China Normal University, Guangzhou 510006, China

## Abstract

One-dimensional (1D) superlattices provide one simplified platform for exploring moiré physics from a low-dimensional perspective, with the ratio of lattice constants playing a role analogous to the twist angle in two-dimensional bilayers. Here, we propose a 1D𝒫​𝒯\mathcal{PT}-symmetric bichromatic optical lattice for a weakly repulsive Bose–Einstein condensate and investigate how the interplay of dissipation and interaction impacts the lowest moiré flat band.
Without interaction, we find that the lowest-band flatness induced by commensurate ratios exhibits a parity-dependent response to the𝒫​𝒯\mathcal{PT}-symmetric imaginary potential due to the distinct𝒫​𝒯\mathcal{PT}pairing mechanism for the energy spectrum.
For ratios with even denominators (i.e., even parities), the level attraction and thus the𝒫​𝒯\mathcal{PT}-symmetry breaking occur within the lowest two bands, leading to a monotonic broadening of the lowest flat band, whereas odd denominators (i.e., odd parities) yield a nonmonotonic response due to the𝒫​𝒯\mathcal{PT}-symmetry breaking within the second and the third lowest bands instead while the lowest band remains purely real.
This parity-dependent phenomenon can be understood by the perturbation theory.
Furthermore, by solving the Gross–Pitaevskii equation, we also find that although the weak repulsive interaction can broaden the moiré bands alone, the combined effects of interaction and imaginary potential also lead to parity-dependent behaviors.
For even parities, band flattening is consistently diminished, whereas for odd parities, the imaginary potential can either enhance or reduce the degree of flattening.
These results pave the way for experimental studies of dissipation and interaction effects on band flatness in moiré systems.

## IIntroduction

Ultracold atoms are an ideal platform for quantum simulation, enabling the realization of complex lattice structures via highly controllable lasers that are difficult to fabricate in solid-state materials[1,2,3]. Recently, a two-dimensional moiré model was implemented in a Bose-Einstein condensate (BEC) with spin-dependent optical lattices[4].
This advance allows a reexamination of many-body effects in moiré physics[5,6,7,8,9]within a clean and highly tunable atomic setting.
To explore the physical essence of such effects in a more tractable setting, theoretical interest has naturally turned to a one-dimensional analog.
The one-dimensional (1D) moiré lattice, a commensurate bichromatic lattice with a large unit cell, has been theoretically shown to host strongly flattened bands and interaction-driven correlated states similar to those in twisted two-dimensional systems[10].
This has inspired studies on the interplay between interactions and (in)commensurability in 1D moiré systems[11,12], and has also prompted its implementation in other platforms, such as photonics[13,14,15,16,17,18].
Meanwhile, theoretical investigations of related phenomena have been conducted in cold-atom systems[19,20,21,22].
Thanks to extensive research on incommensurate bichromatic lattices[23,24,25], the experimental realization of the 1D moiré lattice is now well-established with ultracold atoms.

On the other hand, among the various research directions in non-Hermitian systems[26,27], parity-time-reversal (𝒫​𝒯\mathcal{PT}) symmetry systems constitute a crucial branch of study due to their potential to exhibit entirely real eigenvalue spectra[28,29,30].
Early investigations focused on𝒫​𝒯\mathcal{PT}-symmetric optical waveguides with periodic modulation of complex refractive indices, where novel wave-dynamic phenomena such as Bloch oscillations were observed[31,32].
These works prompted further exploration into more generalized forms of periodic𝒫​𝒯\mathcal{PT}-symmetric lattices.
In the linear regime, properties such as symmetry-breaking phase transitions and associated dynamics in models like the sinusoidal𝒫​𝒯\mathcal{PT}-symmetric optical lattice have been extensively studied[33,34,35,36].
When nonlinearity is present, for example in the context of Kerr nonlinearity in optical waveguides or the Gross–Pitaevskii equation (GPE) describing mean-field BEC, a rich variety of nonlinear localized states and excitations can emerge in such lattices[30].
These include periodic Bloch waves[37]and various types of solitons[38,39,40,41].
Particularly noteworthy is the recent discovery of asymmetric swallowtail structures in nonlinear sinusoidal𝒫​𝒯\mathcal{PT}-symmetric lattices[42], which highlights the significant impact of the interplay between nonlinearity and𝒫​𝒯\mathcal{PT}symmetry on the band structure and dynamical behavior of the system.

Inspired by the correlated states in strongly flat bands of 1D moiré lattices[10]and the pronounced band-structure control in nonlinear𝒫​𝒯\mathcal{PT}-symmetric systems[42], it is natural to explore their combined effects.
A central question is how𝒫​𝒯\mathcal{PT}symmetry influences the flatness of the lowest moiré band, and how weak repulsive interactions interplay with non-Hermiticity to further modulate this flatness.
In this paper, we numerically study the lowest band of a BEC in a 1D𝒫​𝒯\mathcal{PT}-symmetric moiré optical lattice using the GPE.
In the noninteracting regime, the parity-dependent response originates from distinct𝒫​𝒯\mathcal{PT}-pairing structures within each moiré unit cell.
For ratios with even denominators (i.e., even parities), the lowest two bands couple directly through the imaginary potential, leading to monotonic broadening;
while for odd denominators (i.e., odd parities), a self-conjugate center region delays the𝒫​𝒯\mathcal{PT}-symmetry breaking of the lowest band, and its competition with non-Hermitian confinement produces a nonmonotonic response.
This parity-dependent phenomenon can be understood by the perturbation theory.
With weak repulsive interactions, the overall band dispersion increases, yet the combination of interaction and non-Hermiticity selectively enhances or suppresses flattening depending on the parity of ratio denominators. These results advance the understanding of how non-Hermitian effects and weak interactions cooperate or compete in modulating moiré band flatness.

## IIGPE under a𝒫​𝒯\mathcal{PT}-symmetric potential

We consider a BEC with a large particle number in a 3D potential composed of a transverse harmonic trap in the(x,y)(x,y)plane and a longitudinal optical lattice along thezzdirection.
This system can be modeled at the mean-field level by the 3D GPE, and the effective interaction between two atoms is described byg3​D=4​π​ℏ2​as/mg_{\rm 3D}=4\pi\hbar^{2}a_{s}/m, whereasa_{s}is thess-wave scattering length.
Under sufficiently strong harmonic confinement that no transverse excitations are induced by weak interactions, i.e., whenas2/a⟂2≪as​nz≪1a_{s}^{2}/a_{\perp}^{2}\ll a_{s}n_{z}\ll 1, witha⟂a_{\perp}andnzn_{z}being the oscillator length and average 1D density, the BEC can be effectively described by a reduced 1D GPE along the lattice direction[43,44].
Consequently, the 1D macroscopic condensate wave functionΨ≡Ψ​(z,t)\Psi\equiv\Psi(z,t)is governed byi​ℏ​∂∂t​Ψ=[−ℏ22​m​∂2∂z2+VOL​(z)+g​|Ψ|2]​Ψ,i\hbar\frac{\partial}{\partial t}\Psi=\left[-\frac{\hbar^{2}}{2m}\frac{\partial^{2}}{\partial z^{2}}+V_{\rm OL}(z)+g|\Psi|^{2}\right]\Psi,(1)

wheremmis the atomic mass, andg=g3​D/2​π​a⟂2g=g_{\rm 3D}/2\pi a^{2}_{\perp}is the effective 1D interaction strength[43].
The external potentialVOL​(z)V_{\rm OL}(z)is a 1D moiré optical lattice formed by superimposing a primary lattice with wave vectork1k_{1}and a complex secondary lattice with wave vectork2k_{2}. It is given byVOL​(z)=V0​[cos2⁡(k1​z)+cos2⁡(k2​z)+i​γ2​sin⁡(2​k2​z)],V_{\rm OL}(z)=V_{0}\left[\cos^{2}(k_{1}z)+\cos^{2}(k_{2}z)+i\frac{\gamma}{2}\sin(2k_{2}z)\right],(2)

whereV0V_{0}denotes the potential strength.
The real part ofVOL​(z)V_{\rm OL}(z)corresponds to the potential actually loaded onto the atoms, while the purely imaginary sinusoidal term with strengthγ\gammain the secondary lattice represents the spatial gain or loss.
Both lattices are𝒫​𝒯\mathcal{PT}-symmetric due to their even real and odd imaginary parts, making the total potential satisfyVOL​(z)=VOL∗​(−z)V_{\rm OL}(z)=V^{*}_{\rm OL}(-z).
In such non-Hermitian settings, the total particle numberN​(t)N(t)is interpreted as the change in the norm of the wave function with the system lengthLL[45,46].∫L|Ψ​(z,t)|2​𝑑z=N​(t).\displaystyle\int_{L}|\Psi(z,t)|^{2}dz=N(t).(3)

For convenience, we introduce the following dimensionless transformationst→ℏEr​t,z→12​k1​z,V0→2​Er​V0,\displaystyle t\to\dfrac{\hbar}{E_{r}}t,~~~~~z\to\dfrac{1}{2k_{1}}z,~~~~~V_{0}\to 2{E_{r}}V_{0},(4)

where the characteristic energyEr=ℏ2​k12/2​mE_{r}=\hbar^{2}k_{1}^{2}/2mis defined as the primary lattice recoil energy.
Thus, Eq. (1) reduces to the dimensionless formi​∂∂t​Ψ=[−4​∂2∂z2+V​(z)+c​|Ψ|2]​Ψ,\displaystyle i\dfrac{\partial}{\partial t}\Psi=\left[-4\dfrac{\partial^{2}}{\partial z^{2}}+V(z)+c|\Psi|^{2}\right]\Psi,(5)

with an interaction strengthc=g/Erc=g/E_{r}. The lattice potential becomesV​(z)=V0​[cos⁡(z)+cos⁡(α​z)+i​γ​sin⁡(α​z)],\displaystyle V(z)=V_{0}\left[\cos\left(z\right)+\cos\left(\alpha z\right)+i\gamma\sin\left(\alpha z\right)\right],~~~(6)

where an overall additive constantV0V_{0}has been omitted.
The parameterα≡k2/k1\alpha\equiv k_{2}/k_{1}is defined as the 1D moiré ratio[10], which gives rise to either aperiodic (incommensurate) or periodic (commensurate) potential functions.
Notable phenomena such as Anderson transitions[47]and mobility edges[48,49]have been studied in 1D incommensurate lattice models.
In this work, we focus on the commensurate case, whereα=1/q∈ℚ\alpha=1/q\in\mathbb{Q}, with denominatorq≥1q\geq 1.
The unit cell sizes of the primary and secondary lattices area1=2​πa_{1}=2\pianda2=2​π/αa_{2}=2\pi/\alpha, respectively. The resulting commensurate potentialV​(z)V(z)exhibits a period ofA=a2=q​a1≥a1A=a_{2}=qa_{1}\geq a_{1}, referred to as the 1D moiré cell[10].

To analyze the properties of the energy bands, we consider solutions of Eq. (5) in the form of a stationary Bloch-type wave functionΨν​k​(z,t)=ei​(k​z−μ​t)​ψν​k​(z),\displaystyle\Psi_{\nu k}(z,t)=e^{i\left(kz-\mu t\right)}\psi_{\nu k}(z),(7)

whereν≥1\nu\geq 1is the band index (bands are ordered by the real part of the energy, withν=1\nu=1labeling the lowest band),μ\muis the chemical potential, and the moiré Bloch wave vectorkkis restricted to the first Brillouin zonek∈[−K/2,K/2)k\in[-K/2,K/2)withK=2​π/AK=2\pi/A.
Here, we only focus on the wave functionψν​k​(z)\psi_{\nu k}(z)with periodAA, while period-multiplied[50]and soliton[51]solutions may also exist.
Substituting Eq. (7) into Eq. (5), we find thatψν​k​(z)\psi_{\nu k}(z)satisfies the time-independent GPE[−4​(∂∂z+i​k)2+V​(z)+c​|ψν​k|2]​ψν​k=μν​k​ψν​k.\displaystyle\small\left[-4\left(\dfrac{\partial}{\partial z}+ik\right)^{2}+V(z)+c|\psi_{\nu k}|^{2}\right]\psi_{\nu k}=\mu_{\nu k}\psi_{\nu k}.~~(8)

Given that the size of the BEC system is far greater than the moiré cellAA(i.e.,L≫AL\gg A), the average particle number per moiré cellNA=A​nzN_{A}=An_{z}can be expressed by the average 1D density.
The wave function can be normalized as∫−A/2A/2𝑑z​|ψν​k​(z)|2=NA,\displaystyle\int_{-A/2}^{A/2}dz|\psi_{\nu k}(z)|^{2}=N_{A},(9)

and the energy functional density is given byε​[ψ]=1A​∫−A/2A/2𝑑z​ψ∗​[−4​(∂∂z+i​k)2+V​(z)+c2​|ψ|2]​ψ.\small\varepsilon[\psi]=\dfrac{1}{A}\int_{-A/2}^{A/2}dz\psi^{*}\left[-4{\left(\dfrac{\partial}{\partial z}+ik\right)^{2}}+V(z)+\frac{c}{2}|\psi|^{2}\right]\psi.(10)

We define the energy bands by the energy per particle,E​[ψ]≡ε​[ψ]/nzE[\psi]\equiv\varepsilon[\psi]/n_{z}, expressed as a function ofkk.
Here, the average particle densitynzn_{z}is independent ofkkand is treated as a system parameter.
Similarly, for each moiré ratio, we fixnzn_{z}such that the dimensionlessnz​cn_{z}ccan be used to describe the interaction strength.

In the non-Hermitian framework of the𝒫​𝒯\mathcal{PT}-symmetric lattice (6), both the chemical potentialμ\muand the energyEEare generally complex.
In the non-interacting limit (c=0c=0), the complex single-particle bands correspond to the Bloch stationary states that satisfy Eq. (7), whereas the nonlinear mean-field bands (c≠0c\neq 0) withμi≠0\mu^{\rm i}\neq 0are not classified as stationary solutions (the superscriptsr\rm randi\rm idenote the real and imaginary parts).
A nonzero imaginary part ofμ\mucauses the amplitudes of the corresponding condensate wave functions to grow or decay exponentially over time, as indicated in Eq. (7).
This leads to a time-dependent violation of the normalization constraint of the nonlinear equation (8), which contradicts the definition of a stationary state.
Such solutions can only be regarded as instantaneous initial states[52].
On the other hand, the solutions with a purely real chemical potential do not exhibit this inconsistency in the definition of stationary states.
However, it does not ensure stability against perturbations[53]or the feasibility of adiabatic band tracking[54].
Therefore, in the remainder of this article, we will focus on the lowest purely real mean-field energy bands and the non-interacting band.Figure 1:Lowest (Eν=1E_{\nu=1}, solid lines) and second (Eν=2E_{\nu=2}, dashed lines) bands of the non-interacting Hermitian system for moiré ratiosα=1/q\alpha=1/qatV0=0.8V_{0}=0.8. The right panel shows the corresponding band gap ratioGqG_{q}defined in Eq. (12).

## IIINon-Hermitian effect on moiré flat bands without interactionFigure 2:(a)-(f) Several lowest energy bands as a function of the non-Hermitian strengthγ\gammafor different moiré ratios(1/q)(1/q)in the absence of interactions.
The black and blue curves represent the real and imaginary parts of the lowest band (Eν=1E_{\nu=1}), respectively; the gray curves represent the real parts of higher bands (Eν>1E_{\nu>1}), while the light-blue lines correspond to the imaginary parts of a few selected higher bands.
(a)-(c) odd paritiesqo={1,3,5}q_{o}=\{1,3,5\}, with the dispersionDqoD_{q_{o}}and gap ratioGqoG_{q_{o}}of the lowest real band plotted againstγ\gammain (g) shown as solid and dashed lines, respectively; (d)-(f) even paritiesqe={2,4,6}q_{e}=\{2,4,6\}, with the correspondingDqeD_{q_{e}}andGqeG_{q_{e}}shown in (h).
The𝒫​𝒯\mathcal{PT}-breaking pointsγp​t\gamma_{pt}of the lowest band are determined numerically, marked by vertical dash-dotted lines in (a) and (d)-(f), while the real‑part crossing pointsγc\gamma_{c}in (b) and (c) are marked by vertical dashed lines.

In this section, we consider the effects of the moiré ratios and non-Hermiticity on the lowest band and its flatness in the absence of interactions.
In the following analysis, we set the potential strengthV0V_{0}of the moiré lattice [Eq. (6)] to0.80.8.
We consider a set of moiré ratiosα={1/2,1/3,1/4,1/5,1/6}\alpha=\{1/2,1/3,1/4,1/5,1/6\}and compare them with the single-lattice case of double depth atα=1\alpha=1.
These ratios correspond to configurations where the period of the secondary lattice is an integer multipleqqof the primary lattice period, yielding a moiré cell size ofA=2​π​qA=2\pi qfor ratio denominatorsq={1,2,3,4,5,6}q=\{1,2,3,4,5,6\}.

To characterize the flatness of the lowest band, we define the band dispersion ratioDq=log10⁡(wq),\displaystyle D_{q}=\log_{10}\left(w_{q}\right),(11)

wherewq≡max⁡(Eν=1)−min⁡(Eν=1)w_{q}\equiv\max(E_{\nu=1})-\min(E_{\nu=1})is the bandwidth of the lowest real band.
To quantify the interplay between dispersion and excitation, we introduce the inverse gap ratioGq=log10⁡(wq/Δq),\displaystyle G_{q}=\log_{10}\left(w_{q}/\Delta_{q}\right),(12)

whereΔq≡min⁡(Eν=2r)−max⁡(Eν=1)\Delta_{q}\equiv\min(E^{\mathrm{r}}_{\nu=2})-\max(E_{\nu=1})denotes the real band gap.
A value ofDq​(Gq)→−∞D_{q}(G_{q})\to-\inftycorresponds to a completely dispersionless lowest band, whereasGq→+∞G_{q}\to+\inftyindicates that the lowest band becomes gapless or its real part becomes degenerate.

The lowest two bands for the Hermitian cases are shown in the main panel of Fig.1as solid and dashed lines, respectively (see AppendixAfor numerical details).
Asqqincreases, the bandwidth ofEν=1E_{\nu=1}decays exponentially, consistent with Ref.[10].
In contrast, the band gap exhibits an overall oscillatory decrease, while decreasing monotonically when the even and odd denominators are considered separately.
Meanwhile, the gap ratioGqG_{q}decreases with increasingqq, as shown in the right subpanel of Fig.1, demonstrating that the expansion of the moiré unit cell suppresses the band dispersion more effectively than it narrows the band gap.

Figure2shows the noninteracting lowest complex energy bands, along withDqD_{q}andGqG_{q}, as functions ofγ\gamma.
The real (imaginary) parts ofEν=1E_{\nu=1}andEν>1E_{\nu>1}are shown in black and gray (blue and light blue), respectively.
For the single-lattice case [q=1q=1, Fig.2(a)], asγ\gammaincreases, the bandwidth ofEν=1E_{\nu=1}widens monotonically, while the band gap narrows.
This trend is reflected inD1D_{1}andG1G_{1}in Fig.2(g) (solid and dashed lines, respectively).𝒫​𝒯\mathcal{PT}symmetry breaks atγp​t=2\gamma_{pt}=2, where the lowest two bands coalesce at exceptional points (vertical dash-dotted line).
This critical point follows from the transformationz→z−i​tanh−1⁡(γ/2)z\to z-i\tanh^{-1}(\gamma/2)applied to Eq. (6)[36].
The even moiré paritiesqe={2,4,6}q_{e}=\{2,4,6\}exhibit similar behavior.
As shown in Figs.2(d)–2(f), the first𝒫​𝒯\mathcal{PT}-symmetry breaking also involves the lowest two bands, with numerically determined thresholdsγp​t\gamma_{pt}.
Asγ\gammaapproachesγp​t\gamma_{pt}, the bandwidth ofEν=1E_{\nu=1}increases while the gap between the lowest two bands decreases; bothDqeD_{q_{e}}andGqeG_{q_{e}}increase monotonically, withGqeG_{q_{e}}diverging at the EP in Fig.2(h).

Odd denominatorsqo={3,5}q_{o}=\{3,5\}exhibit qualitatively different behavior.
In contrast to the even case, the first𝒫​𝒯\mathcal{PT}-breaking transition occurs betweenEν=2E_{\nu=2}andEν=3E_{\nu=3}atγp​t\gamma_{pt}, as illustrated in Figs.2(b) and2(c).
Beyondγp​t\gamma_{pt}, the two levels split into a complex-conjugate pair, whileEν=1E_{\nu=1}remains purely real and shifts upward.
Meanwhile, the common real part ofEν=2,3E_{\nu=2,3}changes only weakly.
Over a broad range ofγ\gammabefore the real-part crossing,Eν=1E_{\nu=1}stays purely real, withDqoD_{q_{o}}andGqoG_{q_{o}}in Fig.2(g) behaving nonmonotonically.
Atγc\gamma_{c}in Figs.2(b) and2(c), the real part ofEν=1E_{\nu=1}crosses the common real part ofEν=2,3E_{\nu=2,3}, as marked by the vertical dashed lines.
This crossing reorders the bands by their real parts; the originally purely real band is no longer the lowest and is relabeled to a higherν\nu, while the complex-conjugate pair is labeledEν=1,2E_{\nu=1,2}in the real-part ordering.

To understand the parity-dependent flattening behaviors induced by this𝒫​𝒯\mathcal{PT}-symmetric imaginary potential, we adopt the perturbation theory regarding smallγ\gamma.
The energy up to the second order inγ\gammayieldsEν=E~ν+γ2​∑μ≠ν|𝒱μ​ν|2Δμ​ν+O​(γ3),\displaystyle E_{\nu}=\tilde{E}_{\nu}+\gamma^{2}\sum_{\mu\neq\nu}\frac{|\mathcal{V}_{\mu\nu}|^{2}}{\Delta_{\mu\nu}}+O(\gamma^{3}),(13)

whereψ~\tilde{\psi}is the unperturbed wave function for Hermitian systems, and𝒱μ​ν≡i​V0A​∫Aψ~μ∗​Vi​ψ~ν​𝑑z=−𝒱ν​μ∗\mathcal{V}_{\mu\nu}\equiv\frac{iV_{0}}{A}\int_{A}\tilde{\psi}_{\mu}^{*}V^{\rm i}\tilde{\psi}_{\nu}dz=-\mathcal{V}_{\nu\mu}^{*}.
Equation (13), valid in the weak-γ\gammaregime away from EPs, shows that the level attraction between bands coupled throughViV^{\rm i}is determined by|𝒱μ​ν|2/|Δμ​ν||\mathcal{V}_{\mu\nu}|^{2}/|\Delta_{\mu\nu}|.
The pair that first reaches the EP is therefore the one with the largest coupling strength relative to the gap.
For the lowest band,∂E1/∂γ>0\partial E_{1}/\partial\gamma>0implies a monotonic upward shift.
For higher bands, the wave function overlap and the level spacing together determine the shift. Generally, the wave functions of the lowest few levels are concentrated near the minima ofVr​(z)V^{\rm r}(z); within each moiré unit cell, these minima satisfyq​sin⁡z=−sin⁡(z/q)q\sin z=-\sin(z/q)and occur in𝒫​𝒯\mathcal{PT}-conjugate pairszn⇔zq−n+1z_{n}\Leftrightarrow z_{q-n+1}, withV​(zn)=V∗​(zq−n+1)V(z_{n})=V^{*}(z_{q-n+1}).
For evenqq, all minima formq/2q/2conjugate pairs.
Takingq=2q=2as an example,ψ~1\tilde{\psi}_{1}andψ~2\tilde{\psi}_{2}are mainly constructed from orbitals localized around the paired minima
atz1/A≈0.3z_{1}/A\approx 0.3andz2/A≈0.7z_{2}/A\approx 0.7, as shown in Fig.3(a1), forming a bonding-antibonding pair analogous to a𝒫​𝒯\mathcal{PT}-symmetric double well[46,55].
The same concentration pattern persists in the non-Hermitian regime as seen in Fig.3(a2).
Sinceψ~1\tilde{\psi}_{1}andψ~2\tilde{\psi}_{2}share the most similar concentration profiles, their energies are close (Δ21<Δ32\Delta_{21}<\Delta_{32}) and|𝒱21|>|𝒱32||\mathcal{V}_{21}|>|\mathcal{V}_{32}|, hence∂E1/∂γ≈−∂E2/∂γ>0\partial E_{1}/\partial\gamma\approx-\partial E_{2}/\partial\gamma>0at weakγ\gamma.
The resulting strong attraction between the lowest two bands triggers𝒫​𝒯\mathcal{PT}-symmetry breaking first at the moiré Brillouin boundary, where the gap is smallest;D2D_{2}therefore increases monotonically withγ\gammain Fig.2(h).
Oddqqhas a different𝒫​𝒯\mathcal{PT}-breaking sequence due to the self-conjugate center minimumVi​(A/2)=0V^{\rm i}(A/2)=0.
Forq=3q=3, as shown in Fig.3(b),ψ~2\widetilde{\psi}_{2}andψ~3\widetilde{\psi}_{3}are concentrated on the same pair of off-center minimaz1/A≈0.2z_{1}/A\approx 0.2andz3/A≈0.8z_{3}/A\approx 0.8, producing a largeViV^{\rm i}-weighted off-diagonal matrix element|𝒱32||\mathcal{V}_{32}|.
By contrast, the center concentration ofψ~1\widetilde{\psi}_{1}suppresses|𝒱21||\mathcal{V}_{21}|, hence∂E2/∂γ≈−∂E3/∂γ>0\partial E_{2}/\partial\gamma\approx-\partial E_{3}/\partial\gamma>0, driving𝒫​𝒯\mathcal{PT}-symmetry breaking betweenEν=2E_{\nu=2}andEν=3E_{\nu=3}.
The same perturbative picture extends to general denominators.
For evenqeq_{e}, the strongest coupling relative to the band gap occurs between the two lowest bands. Therefore,𝒫​𝒯\mathcal{PT}-symmetry breaking first occurs in this band pair, andDqeD_{q_{e}}increases monotonically.
For oddqoq_{o}, the self-conjugate center minimum weakens the coupling of the lowest band and favors𝒫​𝒯\mathcal{PT}-symmetry breaking in the higher off-center band pairs.
The tight-binding analysis in AppendixBshows that the self-conjugate central site couples only indirectly to the imaginary potential for oddqoq_{o}, whereas the lowest doublet couples directly for evenqeq_{e}. This structural difference determines the first𝒫​𝒯\mathcal{PT}-breaking band pair.

On the other hand, for oddqoq_{o}, the nonmonotonic behaviors in Fig.2(g) arise from the competition between level attraction and non-Hermitian confinement.
At weakγ\gamma, attraction from higher bands broadens the lowest band, while𝒫​𝒯\mathcal{PT}-symmetry breaking among these higher bands produces sharpGqoG_{q_{o}}features and subsequently weakens this attraction.
Asγ\gammagrows further, the imaginary part of the potential dominates[56,57]and concentratesψ1\psi_{1}toward the center of each unit cell. This non-Hermitian confinement is evidenced by the decreasing wave-packet widthσ\sigmain Fig.3(c) and the increasingly concentrated wave function forq=5q=5in Fig.3(d), while its behavior at largeγ\gammais analyzed further in AppendixC. It eventually overcomes the level-attraction-induced broadening and causesD5D_{5}to decrease.Figure 3:Wave functionsψν​(z)\psi_{\nu}(z)atk=0k=0for the lowest three bands (upper panels) and the corresponding potential profiles (lower panels) within one moiré unit cell for (a)q=2q=2and (b)q=3q=3.
The real and imaginary parts of the potential are shown by gray solid and blue dashed curves, respectively.
The circles mark minima of the potential real part from Eq. (6), with the±\pmsigns labeling the sign of its imaginary part; the red open circle specifically marks the center minimum, at whichVi​(A/2)=0V^{\rm i}(A/2)=0.
(a1) and (b1) representψ~ν\tilde{\psi}_{\nu}in the Hermitian case, with|𝒱21|/|𝒱32|≈3|\mathcal{V}_{21}|/|\mathcal{V}_{32}|\approx 3and0.630.63, respectively;
the corresponding non-Hermitian counterparts (γ=0.1\gamma=0.1) in (a2) and (b2), where in the latterψ2\psi_{2}andψ3\psi_{3}are near an EP, with|1A​∫Aψ3∗​ψ2​𝑑z|≈0.8\bigl|\frac{1}{A}\int_{A}\psi_{3}^{*}\,\psi_{2}\,dz\bigr|\approx 0.8.
(c) The normalized spatial widthσ/A\sigma/Aofψ1\psi_{1}varies withγ\gamma.
(d) Profiles ofψ1\psi_{1}forq=5q=5atγ=1\gamma=1and44.

## IVAdditional interaction effect on the lowest moiré bandFigure 4:The lowest real mean-field band and its dispersionDqD_{q}as functions of the non-Hermitian strengthγ\gamma, for different interaction strengthsnz​cn_{z}c(color coded).
Results for even parities (q=2,4q=2,4) are shown in (a)-(b), using a blue color scale fornz​c=0.1−0.5n_{z}c=0.1-0.5. (a1)(b1)D2,4D_{2,4}versusγ\gamma, while the typical band structures atγ={0.05,0.15,0.25}\gamma=\{0.05,0.15,0.25\}are displayed in (a2)-(a4) and (b2)-(b4).
Similarly, (c)-(d) present the odd parities (q=3,5q=3,5), withnz​c=0.05−0.2n_{z}c=0.05-0.2indicated by a green scale. TheD3,5D_{3,5}versusγ\gammarelation is in (c1)(d1), and the band structures atγ={0.5,1.5,2.5}\gamma=\{0.5,1.5,2.5\}are in (c2)-(c4) and (d2)-(d4).

This section examines the effects of interaction strengthnz​cn_{z}cand non-Hermiticityγ\gammaon the mean-field band structure and its dispersion within the GPE framework of a𝒫​𝒯\mathcal{PT}moiré lattice. We focus on weak repulsive interactions (nz​c>0n_{z}c>0) to avoid the emergence of mean-field band swallowtails at the boundaries of the Brillouin zone.
For eachqq, we restrictγ\gammabelow the point at which the branch originating from the noninteracting lowest band either undergoes𝒫​𝒯\mathcal{PT}-symmetry breaking for evenqeq_{e}, or loses the lowest-real-part ordering through the crossing atγc\gamma_{c}for oddqoq_{o}.
For single-lattice systems, it is often possible to approximateψ​(z)\psi(z)analytically using a superposition of a few plane waves for generic analysis[58,42].
However, the moiré lattice potential contains significantly more plane-wave components, making such trial wave functions inadequate.
Therefore, we numerically compute directly the self-consistent nonlinear solutions of Eq. (8), setting the plane-wave momentum cutoff to10​q​K10qKto ensure accuracy (see AppendixAfor details).

Figure4presents our numerical results, with the even (qe={2,4}q_{e}=\{2,4\}) and odd (qo={3,5}q_{o}=\{3,5\}) parities discussed separately.
For the even parities, shown in Figs.4(a1)–4(b1), the interaction-dependent dispersionsDqeD_{q_{e}}(blue lines) exhibit a monotonically increasing trend withγ\gamma, consistent with the non-interacting case (gray lines).
As expected, the presence of interactions enhances band dispersion.
Interestingly, under the combined effect of interactions and non-Hermiticity, the band becomes asymmetric (i.e.,Ek≠E−kE_{k}\neq E_{-k}), yielding an asymmetric band structure reminiscent of the single-lattice model discussed in Ref.[42].
To illustrate this clearly, Figs.4(a2)–4(a4) and Figs.4(b2)–4(b4) display the lowest real bands forγ={0.05,0.15,0.25}\gamma=\{0.05,0.15,0.25\}under different interaction strengths.
Both stronger interactions and larger non-Hermiticity enhance band asymmetry, which shifts the band maximum and ground state away fromk=K/2k=K/2andk=0k=0, respectively, and also increase the band dispersion.
Moreover, bands with a larger moiré unit cell (q=4q=4) show greater sensitivity to interactions and non-Hermiticity than those with a smaller cell (q=2q=2).
At the sameγ\gamma, the bandwidth ofq=4q=4[Fig.4(b2)] increases significantly with interaction strength, in contrast to the modest increase forq=2q=2[Fig.4(a2)].
Similarly, for fixednz​cn_{z}c, with increasingγ\gamma, band asymmetry is more pronounced forq=4q=4[Figs.4(b2) and4(b4)] than forq=2q=2[Figs.4(a2) and4(a4)], further reflecting the heightened sensitivity of the larger moiré unit cell to non-Hermitian effects.

For odd paritiesqo={3,5}q_{o}=\{3,5\}, interactions enhance the dispersion while the nonmonotonic dependence ofDqoD_{q_{o}}onγ\gammapersists and develops local dips, most pronounced forq=5q=5at intermediateγ\gamma, as shown in Figs.4(c1) and4(d1).
The origin of this complex behavior can be traced through the interaction strengthnz​cn_{z}cas a control parameter.
Atnz​c=0n_{z}c=0,DqoD_{q_{o}}are governed by the𝒫​𝒯\mathcal{PT}-breaking ofEν=2E_{\nu=2}andEν=3E_{\nu=3}alone, inheriting the band-correlation rules in Sec.III.
For smallnz​c≲0.1n_{z}c\lesssim 0.1, the dispersion curves retain this structure, remaining smooth and undistorted [Figs.4(c2)–4(c4)], where the noninteracting picture remains qualitatively valid.
For largernz​cn_{z}c, the repulsive interaction shifts the nonlinear bands upward and reduces some interband gaps.
The enhanced influence of several higher-band branches amplifies the nonmonotonic behavior inherited from the noninteracting system, producing the pronounced oscillations and dips in Figs.4(c1) and4(d1). The lowest real bands forγ={0.5,1.5,2.5}\gamma=\{0.5,1.5,2.5\}are presented in Figs.4(c2)–4(c4) and4(d2)–4(d4), respectively, where band asymmetry induced by interactions and non-Hermiticity is again observed.
Unlike before, asγ\gammaincreases, the ground state exhibits oscillatory shifts towardKKand−K-Kat the correspondingkkpoints, a behavior generally accompanied by a noticeable enhancement in band dispersion.

## VConclusion and Discussion

In summary, we investigated how non-Hermiticity and interactions modify the flatness of the lowest band in a𝒫​𝒯\mathcal{PT}-symmetric moiré lattice.
In the noninteracting regime, the parity of the denominatorqqin the commensurate ratio determines the first𝒫​𝒯\mathcal{PT}-breaking pair and the resulting response of the lowest-band flatness.
For ratios with even denominators, the lowest two bands break𝒫​𝒯\mathcal{PT}-symmetry first, and their level attraction produces monotonic broadening.
For ratios with odd denominators, the second and third lowest bands undergo𝒫​𝒯\mathcal{PT}symmetry breaking, while the lowest band remains real over a broad range of non-Hermiticity.
The subsequent competition between level attraction and non-Hermitian confinement gives rise to a nonmonotonic response.
This parity-dependent phenomenon can be understood from perturbation theory.
Within the GPE framework, interactions generally enhance the mean-field band dispersion. For even denominators, interactions and non-Hermiticity both weaken the moiré-induced band flattening.
For odd denominators, however, non-Hermiticity can either enhance or suppress the flattening, leading to a richer interplay of cooperation and competition with interactions.

Although we only demonstrate the mean-field bands at weak interaction strengths, the strongly interacting regime featuring nonlinear swallowtail structures can also be numerically solved. By iterating over a large number of random trial solutions, we obtained the swallowtail bands of the𝒫​𝒯\mathcal{PT}-symmetric moiré lattice withq=2q=2, for the Hermitian [Fig.5(a)] and non-Hermitian [Fig.5(b)] cases, respectively.
Specifically, non-Hermiticity appears to disrupt the swallowtail structure by removing one of the connecting points of the looped spectrum, in contrast to the single-lattice model[42].
Given this peculiar multivalued band structure, it would be valuable to further investigate the corresponding dynamics, such as adiabatic or non-adiabatic Landau–Zener tunneling under a nonlinear sweep[59].
Moreover, for other moiré ratios, how non-Hermiticity and interactions affect the existence of swallowtail structures is also an open and meaningful question to explore.

On the other hand, the experimental realization of a BEC in such complex a potential (2) may become feasible in the future.
A real bichromatic optical lattice can be generated by superimposing two standing-wave laser potentials with different periods[23], and the effective 1D interaction strength can be tuned via Feshbach resonance by adjusting thess-wave scattering length[60,61].
Moreover, imaginary periodic potentials implemented in coherently preparednn-level atomic vapors have been reported[62,63,64].
Although there is no direct evidence that such configurations can support a stable BEC, controlled atomic gain[65]and loss[66,67,68,69]among hyperfine levels have been progressively achieved.
Along with the rapid advances of the ultracold atomic experimental techniques, the realization of𝒫​𝒯\mathcal{PT}-symmetric lattices with periodic gain and loss can be expected experimentally.Figure 5:Several lowest mean-field bands at interaction strengthnz​c=2n_{z}c=2forq=2q=2in (a) Hermitian and (b) non-Hermitian withγ=0.25\gamma=0.25. The lowest (black dots) and second (blue dots) bands are purely real, while the third band (orange dots) is complex and only shows the real part. The linear bands are shown in gray for comparison.

## Acknowledgements.We thank Kangwu Zheng and Congjun Zou for valuable discussions.
This work was supported by the National Key Research and Development Program of China (Grant No. 2022YFA1405304), the Guangdong Basic and Applied Basic Research Foundation (Grant No. 2024A1515010188), and the Startup Fund of South China Normal University.

## Appendix ANumerical methods for mean-field energy bands

To obtain the energy per particleE​[ψ]E[\psi], the nonlinear equation (8) must first be solved. We define the operatorH​[ψ]=[−4​(∂∂z+i​k)2+V​(z)+c​|ψν​k|2],\displaystyle H[\psi]=\left[-4\left(\dfrac{\partial}{\partial z}+ik\right)^{2}+V(z)+c|\psi_{\nu k}|^{2}\right],(14)

which satisfiesH​[ψ]​ψν​k=μ​ψν​kH[\psi]\psi_{\nu k}=\mu\psi_{\nu k}.
Because of the periodicity ofψν​k\psi_{\nu k}, we expand it in a plane wave basis:ψν​k​(z)=nz​∑l=−ddaν,k;l​ei​l​K​z,\displaystyle\psi_{\nu k}(z)=\sqrt{n_{z}}\sum_{l=-d}^{d}a_{\nu,k;l}e^{ilKz},(15)

where the integerddis the cut-off constant.
Substituting Eq. (15) into Eq. (9) yields the normalization condition for the coefficients:∑l=−dd|aν,k;l|2=1.\displaystyle\sum_{l=-d}^{d}|a_{\nu,k;l}|^{2}=1.(16)

In this plane-wave basis,H​[ψ]H[\psi]forα=p/q\alpha=p/qtakes a matrix form. Its elements are given by:Hk;n,m\displaystyle H_{k;n,m}=\displaystyle=4​(n​K+k)2​δn,m+V02​(δn,m+p+δn,m−p)\displaystyle 4{\left(nK+k\right)^{2}}\delta_{n,m}+\frac{V_{0}}{2}\left(\delta_{n,m+p}+\delta_{n,m-p}\right)\qquad+V02​(1+γ)​δn,m+q+V02​(1−γ)​δn,m−q\displaystyle+~\frac{V_{0}}{2}(1+\gamma)\delta_{n,m+q}+\frac{V_{0}}{2}(1-\gamma)\delta_{n,m-q}\qquad+nz​c​∑l′,laν,k;l′∗​aν,k;l​δl′+n,l+m.\displaystyle+~n_{z}c\sum_{l^{\prime},l}a_{\nu,k;l^{\prime}}^{*}a_{\nu,k;l}\delta_{l^{\prime}+n,l+m}.

Consequently, the time-independent GPE (8) becomes a complex nonlinear system of equations∑m=−ddHk;n,m​aν,k;m=μν,k​aν,k;n,\displaystyle\sum_{m=-d}^{d}H_{k;n,m}a_{\nu,k;m}=\mu_{\nu,k}a_{\nu,k;n},(18)

and the energy-per-particle functional for the interacting cases can be derivedE​[a]=μ−nz​c2​∑n=−2​d2​d|∑m=−ddam​an−m|2.E[a]=\mu-\dfrac{n_{z}c}{2}\sum_{n=-2d}^{2d}\left|\sum_{m=-d}^{d}a_{m}a_{n-m}\right|^{2}.(19)

In the non-interacting limit (c=0c=0), Eq. (18) reduces to a non-Hermitian eigenvalue problem, which can be solved straightforwardly.
However, for the interacting case (c≠0c\neq 0), we use the numerical iteration method to solve the complex nonlinear system of equations (18) under the normalization constraint (16).
We decompose the(2​d+1)(2d+1)equations (18) into their real and imaginary parts since the coefficientsaaand the chemical potentialμ\muare generally complex.
This yields a doubled system of equations over the real numbers[Hr−μr−Hi+μiHi−μiHr−μr]​[a¯ra¯i]=0\displaystyle\begin{bmatrix}H^{\rm r}-\mu^{\rm r}&-H^{\rm i}+\mu^{\rm i}\\
H^{\rm i}-\mu^{\rm i}&H^{\rm r}-\mu^{\rm r}\end{bmatrix}\begin{bmatrix}\underline{a}^{\rm r}\\
\underline{a}^{\rm i}\end{bmatrix}=0(20)

wherea¯\underline{a}is the vector of plane-wave coefficients.
We choose a specific gauge to ensureaν,k;di=0a_{\nu,k;d}^{\rm i}=0.
This reduces the number of free variables to4​d+34d+3, which matches the total number of equations from the system (20) plus the normalization condition (16).

We solve for the set{a¯,μ}\{\underline{a},\mu\}using the𝑓𝑠𝑜𝑙𝑣𝑒\mathit{fsolve}function in MATLAB©.
The initial guess for the solution vector(a¯r,a¯i,μr,μi)T\left(\underline{a}^{\rm r},\underline{a}^{\rm i},\mu^{\rm r},\mu^{\rm i}\right)^{\rm T}is constructed as follows: for the lowest band [Fig.4], we used the result from the linear case(c=0)(c=0)as the trial solution to first iterate for the ground state (assumed atk=0k=0).
After successful iteration, this solution was then used as the trial solution fork+Δ​kk+\Delta k, and the process was repeated until reachingk=Kk=K. Subsequently, we iterated backwards fromk=Kk=Ktok=0k=0. If the results from the forward and backward iterations coincide completely neark=K/2k=K/2, we conclude that no nonlinear swallowtail structure has emerged.
For higher bands [Fig.5], we use random initial conditions.
The guess for the coefficient vector{a¯}\{\underline{a}\}is normalized on the(4​d+2)(4d+2)-dimensional hypersphere to satisfy the normalization condition (16). The initial guesses forμr\mu^{\rm r}andμi\mu^{\rm i}are set to the linear result multiplied by a random number between0and1010.
The moiré lattice introduces additional plane-wave couplings, necessitating an expansion in a large number of plane waves. The cut-off was set tod=10​qd=10qto ensure convergence, defined by the following criteria: the plane-wave coefficients for the lowest band at the Brillouin zone boundary satisfy|a1,K/2;±d|<10−13|a_{1,K/2;\pm d}|<10^{-13}, and the energy difference satisfies|Ek=0−Ek=±K|<10−8|E_{k=0}-E_{k=\pm K}|<10^{-8}.
Figure 6:(a),(b) Tight-binding Hamiltonian parameters as functions ofVp/VsV_{p}/V_{s}at fixedVs=0.8V_{s}=0.8, computed from the overlap integrals of the maximally localized Wannier functions via Eqs. (26) and (27).
(c)-(f) Non-Hermitian band structures forq={2,3,4,5}q=\{2,3,4,5\}atVp=Vs=0.8V_{p}=V_{s}=0.8.
Tight-binding bands (black lines) are compared with the full continuum calculation performed using plane-wave-basis diagonalization (gray lines).
Panels (c),(d) correspond to Class I (ϕp=0\phi_{p}=0,ϕs=0\phi_{s}=0);
panels (e),(f) correspond to Class III (ϕp=π\phi_{p}=\pi,ϕs=0\phi_{s}=0) as defined in Eq. (43).

## Appendix BTight-binding approximation for the
continuum model

In this section, we discuss the non-interacting bands using a tight‑binding approach.
We rewrite the lattice potential in Eq. (6) asV~​(z)=Vp​cos⁡(z)+Vs​[cos⁡(α​z)+i​γ​sin⁡(α​z)],\displaystyle\tilde{V}(z)=V_{p}\cos\left(z\right)+V_{s}\left[\cos\left(\alpha z\right)+i\gamma\sin\left(\alpha z\right)\right],(21)

and restrict ourselves to the caseVp≥Vs>0V_{p}\geq V_{s}>0.
Although the main text focuses onV~​(z)\tilde{V}(z)withVp=VsV_{p}=V_{s}, the key physical conclusions for weakγ\gammacan be captured by Eq. (21).
In our setup, the period of the primary lattice is always smaller than that of the secondary lattice.
Consequently, the lowest band of the primary lattice undergoes significant folding once the secondary lattice is introduced.
This folding occursqqtimes, giving rise toqqmoiré subbands in the lowest energy region, located in momentum space atkν=±ν/2​qk_{\nu}=\pm\nu/2q(ν=1,2,…,q\nu=1,2,\dots,q).
Within the moiré Brillouin zone, gaps open between these subbands:
the gaps associated with oddν\nuare located atk=±1/2​qk=\pm 1/2q, whereas those associated with evenν\nuappear atk=0k=0.
Because the gaps among theseqqlowest moiré subbands are much smaller than the gap above the lowest band of the primary lattice and can be estimated by perturbation theory, a tight-binding model based on the lowest band of the primary lattice provides an effective means of analyzing the moiré band structure.

To construct the tight‑binding model, we identify the minima of the primary lattice (which nearly coincide with the moiré lattice minima[70,71]) as the Wannier centersRsR_{s}.
The associated maximally localized Wannier functions centered atRsR_{s}are denoted byW​(z−Rs)W(z-R_{s})and can be chosen to be real and to have even parity[72].
Within one moiré unit cell, there areqqsuch centers, i.e.,Rs=(2​s−1)​π,s=1,…,q.\displaystyle R_{s}=(2s-1)\pi,\qquad s=1,\dots,q.(22)

Let(n,s)(n,s)label thess‑th site within thenn‑th moiré unit cell, andcn,s(†)c_{n,s}^{(\dagger)}be the corresponding annihilation (creation) operator.
The noninteracting real‑space Hamiltonian with nearest-neighbour hopping takes the formH=∑n,sε~s​cn,s†​cn,s+∑n,s(t~s​cn,s+1†​cn,s+h.c.),H=\sum_{n,s}\tilde{\varepsilon}_{s}\,c_{n,s}^{\dagger}c_{n,s}+\sum_{n,s}\bigl(\tilde{t}_{s}\,c_{n,s+1}^{\dagger}c_{n,s}+\text{h.c.}\bigr),(23)

where the onsite energies and nearest-neighbor hopping amplitudes are defined asε~s\displaystyle\tilde{\varepsilon}_{s}≡∫−∞+∞W​(z−Rs)​[−4​∂2∂z2+V~​(z)]​W​(z−Rs)​𝑑z,\displaystyle\equiv\int_{-\infty}^{+\infty}W(z-R_{s})\left[-4\frac{\partial^{2}}{\partial z^{2}}+\tilde{V}(z)\right]W(z-R_{s})\,dz,(24)t~s\displaystyle\tilde{t}_{s}≡∫−∞+∞W​(z−Rs+1)​[−4​∂2∂z2+V~​(z)]​W​(z−Rs)​𝑑z.\displaystyle\equiv\int_{-\infty}^{+\infty}W(z-R_{s+1})\left[-4\frac{\partial^{2}}{\partial z^{2}}+\tilde{V}(z)\right]W(z-R_{s})\,dz.

Taking into account the parity of the integrands, these expressions can be reduced toε~s\displaystyle\tilde{\varepsilon}_{s}=ε0+Cε​[cos⁡(Rsq)+i​γ​sin⁡(Rsq)],\displaystyle=\varepsilon_{0}+C_{\varepsilon}\Bigl[\cos\Bigl(\frac{R_{s}}{q}\Bigr)+i\gamma\sin\Bigl(\frac{R_{s}}{q}\Bigr)\Bigr],(25)t~s\displaystyle\tilde{t}_{s}=t0+Ct​[cos⁡(Rs+πq)+i​γ​sin⁡(Rs+πq)],\displaystyle=t_{0}+C_{t}\Bigl[\cos\Bigl(\frac{R_{s}+\pi}{q}\Bigr)+i\gamma\sin\Bigl(\frac{R_{s}+\pi}{q}\Bigr)\Bigr],

whereε0,t0∈ℝ\varepsilon_{0},t_{0}\in\mathbb{R}are the onsite energy and nearest-neighbor hopping amplitude of the primary lattice, respectively, and are given explicitly byε0\displaystyle\varepsilon_{0}=∫−∞+∞W​(z−Rs)​[−4​∂2∂z2+Vp​cos⁡z]​W​(z−Rs)​𝑑z,\displaystyle=\int_{-\infty}^{+\infty}W(z-R_{s})\left[-4\frac{\partial^{2}}{\partial z^{2}}+V_{p}\cos z\right]W(z-R_{s})dz,(26)t0\displaystyle t_{0}=∫−∞+∞W​(z−Rs+1)​[−4​∂2∂z2+Vp​cos⁡z]​W​(z−Rs)​𝑑z.\displaystyle=\int_{-\infty}^{+\infty}W(z-R_{s+1})\left[-4\frac{\partial^{2}}{\partial z^{2}}+V_{p}\cos z\right]W(z-R_{s})dz.

The constantsCε\displaystyle C_{\varepsilon}≡Vs​∫−∞+∞W2​(u)​cos⁡(u/q)​𝑑u,\displaystyle\equiv V_{s}\int_{-\infty}^{+\infty}W^{2}(u)\cos(u/q)du,(27)Ct\displaystyle C_{t}≡Vs​∫−∞+∞W​(v+π)​W​(v−π)​cos⁡(v/q)​𝑑v\displaystyle\equiv V_{s}\int_{-\infty}^{+\infty}W(v+\pi)W(v-\pi)\cos(v/q)dv

are real numbers withCε/Vs>0C_{\varepsilon}/V_{s}>0andCt/Vs>0C_{t}/V_{s}>0, whose precise values do not affect the symmetry content of Eq. (25).
Throughout this work, we restrict our discussion toCt<|t0|,t0<0,\displaystyle C_{t}<|t_{0}|,~~~t_{0}<0,(28)

which ensures that the primary lattice tight-binding description underpinning Eq. (23) remains valid.
The numerically computed tight-binding parameters across a range of primary and secondary lattice depths are shown in Figs.6(a) and6(b).

One readily verifies the following relationsε~s=ε~q−s+1∗,t~s=t~q−s∗,\displaystyle\tilde{\varepsilon}_{s}=\tilde{\varepsilon}_{q-s+1}^{*},\qquad\tilde{t}_{s}=\tilde{t}^{*}_{q-s},(29)

which reveal a𝒫​𝒯\mathcal{PT}-type pairing between sublatticessandq−s+1q-s+1; in particular, for oddqqone hasε~(q+1)/2i=0\tilde{\varepsilon}^{\rm i}_{(q+1)/2}=0.
Moreover, denotingφs≡arg⁡[t~s]\varphi_{s}\equiv\arg[\tilde{t}_{s}], the pairing relation in Eq. (29) implies pairwise cancellation; hence,∑s=1qφs≡0\sum_{s=1}^{q}\varphi_{s}\equiv 0(modπ\pi).
Applying the Peierls transformationcn,s→ei​θs​cn,sc_{n,s}\to e^{i\theta_{s}}c_{n,s}withθs+1−θs=φs\theta_{s+1}-\theta_{s}=\varphi_{s}(modπ\pi) renders every hopping real[73,26].
After the transformation,ts=tq−st_{s}=t_{q-s}, while the onsite terms are unaffected:εs=ε~s\varepsilon_{s}=\tilde{\varepsilon}_{s}.

Applying a Fourier transform to Eq. (23), the Bloch Hamiltonian inkkspace readsH​(k)=[ε1t10⋯0tq​e−i​θkt1ε2t2⋯00⋮⋮⋮⋱⋮⋮000⋯ε2∗t1tq​ei​θk00⋯t1ε1∗]q×q,\displaystyle H(k)=\begin{bmatrix}\varepsilon_{1}&t_{1}&0&\cdots&0&t_{q}e^{-i\theta_{k}}\\
t_{1}&\varepsilon_{2}&t_{2}&\cdots&0&0\\
\vdots&\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&0&\cdots&\varepsilon_{2}^{*}&t_{1}\\
t_{q}e^{i\theta_{k}}&0&0&\cdots&t_{1}&\varepsilon_{1}^{*}\end{bmatrix}_{q\times q},(30)

whereθk=2​π​q​k\theta_{k}=2\pi qk.
DiagonalizingH​(k)H(k)at eachγ\gammayields the moiré tight-binding band structureℰq\mathcal{E}_{q}, from whichDqD_{q}andGqG_{q}are extracted.

## B.1The even case ofq=2q=2

Forq=2q=2the tight-binding chain reduces to the non-Hermitian Su-Schrieffer-Heeger model[74,26], whose eigenvalues can be obtained analytically:E±​(k)=ε0±2​(t02+Ct2)+2​(t02−Ct2)​cos⁡θk−γ2​Cε2.E_{\pm}(k)=\varepsilon_{0}\pm\sqrt{2(t_{0}^{2}+C_{t}^{2})+2\left(t_{0}^{2}-C_{t}^{2}\right)\cos\theta_{k}-\gamma^{2}C_{\varepsilon}^{2}}.(31)

Figure6(c) compares the tight-binding bands (black) with the continuum bands (gray) atγ=0.5\gamma=0.5.

Under the condition in Eq. (28), the𝒫​𝒯\mathcal{PT}-symmetry breaking threshold isγp​t​(k)=2​(t02+Ct2)+2​(t02−Ct2)​cos⁡θkCε.\gamma_{pt}(k)=\dfrac{\sqrt{2(t_{0}^{2}+C_{t}^{2})+2\left(t_{0}^{2}-C_{t}^{2}\right)\cos\theta_{k}}}{C_{\varepsilon}}.(32)

The earliest𝒫​𝒯\mathcal{PT}-symmetry breaking occurs at the moiré Brillouin-zone boundary,k=±1/4k=\pm 1/4, whereγp​t​(±1/4)=2​Ct/Cε\gamma_{pt}(\pm 1/4)=2C_{t}/C_{\varepsilon}. Numerical integration with the maximally localized Wannier functions yieldsγp​t​(1/4)≈0.48\gamma_{pt}(1/4)\approx 0.48forVp=Vs=0.8V_{p}=V_{s}=0.8, slightly above the continuum-model value0.460.46shown in Fig.2(d).

## B.2The odd case ofq=3q=3

Forq=3q=3, the model is usually referred to as the𝒫​𝒯\mathcal{PT}-trimer model[75,76,77,78,79], where𝒫​𝒯\mathcal{PT}symmetry pairs sublattices|s=1⟩↔|3⟩|s=1\rangle\leftrightarrow|3\rangle, while|2⟩|2\rangleis self-conjugate.
Using the pairing unitary matrixU=12​[10−1101020],\displaystyle U=\frac{1}{\sqrt{2}}\begin{bmatrix}1&0&-1\\
1&0&1\\
0&\sqrt{2}&0\end{bmatrix},\quad(33)

which satisfies(|−⟩,|+⟩,|2⟩)T=U​(|1⟩,|2⟩,|3⟩)T(|-\rangle,|+\rangle,|2\rangle)^{\rm T}=U(|1\rangle,|2\rangle,|3\rangle)^{\rm T}with|±⟩≡(|1⟩±|3⟩)/2|\pm\rangle\equiv(|1\rangle\pm|3\rangle)/\sqrt{2}, the transformed Hamiltonianℋ​(k)=U​H​(k)​UT\mathcal{H}(k)=UH(k)U^{\rm T}readsℋ​(k)=[ε1r−t3​cos⁡θki​(ε1i−t3​sin⁡θk)0i​(ε1i+t3​sin⁡θk)ε1r+t3​cos⁡θk2​t102​t1ε2],\displaystyle\mathcal{H}(k)=\begin{bmatrix}\varepsilon_{1}^{\rm r}-t_{3}\cos\theta_{k}&i(\varepsilon_{1}^{\rm i}-t_{3}\sin\theta_{k})&0\\
i(\varepsilon_{1}^{\rm i}+t_{3}\sin\theta_{k})&\varepsilon_{1}^{\rm r}+t_{3}\cos\theta_{k}&\sqrt{2}t_{1}\\
0&\sqrt{2}t_{1}&\varepsilon_{2}\end{bmatrix},\qquad~~(34)

whereε1=ε0+Cε​(1+i​3​γ)/2\varepsilon_{1}=\varepsilon_{0}+C_{\varepsilon}(1+i\sqrt{3}\gamma)/2andε2=ε0−Cε\varepsilon_{2}=\varepsilon_{0}-C_{\varepsilon}.

We first consider the Hermitian limitγ=0\gamma=0.
At the moiré zone centerk=0k=0, the matrix becomes block diagonal:|−⟩|-\rangledecouples completely, with eigenvalueE|−⟩=ε1r−t3E_{|-\rangle}=\varepsilon_{1}^{\mathrm{r}}-t_{3}, while|+⟩|+\rangleand|2⟩|2\rangleform a coupled2×22\times 2subsystem whose eigenvalues we denote byE±=(ε1r+ε2+t3±D)/2E_{\pm}=(\varepsilon_{1}^{\rm r}+\varepsilon_{2}+t_{3}\pm D)/2whereD≡(3​Cε/2+t3)2+8​t12>0D\equiv\sqrt{(3C_{\varepsilon}/2+t_{3})^{2}+8t_{1}^{2}}>0.

Under the condition in Eq. (28), one hast3<0t_{3}<0in the weak-γ\gammatight-binding regime.
Together withCε≫CtC_{\varepsilon}\gg C_{t}(the onsite term induced by the
secondary lattice dominates over the hopping modulation [Figs.6(a),(b)]), a direct calculation yieldsE|−⟩>E+>E−,Δ21>Δ32.\displaystyle E_{|-\rangle}>E_{+}>E_{-},\qquad\Delta_{21}>\Delta_{32}.(35)

whereΔ21≡E+−E−\Delta_{21}\equiv E_{+}-E_{-}andΔ32≡E|−⟩−E+\Delta_{32}\equiv E_{|-\rangle}-E_{+}follow the band-index convention of Sec.III.
The two upper bands (the decoupled|−⟩|-\rangleand the anti-bonding combination of|+⟩|+\rangleand|2⟩|2\rangle) are split by the smaller gapΔ32\Delta_{32}, while the lowest band, dominated by the self-conjugate center sublattice|2⟩|2\rangle, is separated from them by the larger gapΔ21\Delta_{21}.
This inverted gap hierarchy is the key structural feature that governs the𝒫​𝒯\mathcal{PT}-breaking sequence.

Whenγ≠0\gamma\neq 0, the imaginary onsite contrast generates the couplingε1i=γ​Cε​3/2\varepsilon_{1}^{\rm i}=\gamma C_{\varepsilon}\sqrt{3}/2between|+⟩|+\rangleand|−⟩|-\rangle.
To analyze theγ\gammadependence of the lowest level, we takek=0k=0and consider the characteristic equationdet[ℋ−E​I]=0\det[\mathcal{H}-EI]=0.
A direct expansion yields(E−ε2)​[(E−ε1r)2−t32+(ε1i)2]=2​t12​(E−ε1r+t3).(E-\varepsilon_{2})\bigl[(E-\varepsilon_{1}^{\rm r})^{2}-t_{3}^{2}+(\varepsilon_{1}^{\rm i})^{2}\bigr]=2t_{1}^{2}\,(E-\varepsilon_{1}^{\rm r}+t_{3}).(36)

The lowest level is close toε2\varepsilon_{2}.
We defineE−=ε2+δ​EE_{-}=\varepsilon_{2}+\delta Eand|δ​E|≪Δε|\delta E|\ll\Delta_{\varepsilon}, whereΔε≡ε1r−ε2\Delta_{\varepsilon}\equiv\varepsilon_{1}^{\rm r}-\varepsilon_{2}.
In the tight-binding regime, Eq. (36) yields, to leading order int12t_{1}^{2},δ​E≈−2​t12​(Δε−t3)Δε2−t32+(ε1i)2.\displaystyle\delta E\approx-\dfrac{2t_{1}^{2}(\Delta_{\varepsilon}-t_{3})}{\Delta_{\varepsilon}^{2}-t_{3}^{2}+(\varepsilon_{1}^{\rm i})^{2}}.(37)

The numerator contains aγ\gamma-dependent term that scales asγ2​Ct2\gamma^{2}C_{t}^{2}, while the denominator contains(ε1i)2∝γ2​Cε2(\varepsilon_{1}^{\rm i})^{2}\propto\gamma^{2}C_{\varepsilon}^{2}.
SinceCε2≫Ct2C_{\varepsilon}^{2}\gg C_{t}^{2}[Figs.6(a),(b)], the denominator grows much faster withγ\gammathan the numerator does;
consequently|δ​E||\delta E|decreases and the real part ofE−E_{-}shifts upward, consistent with the continuum model behavior shown in Fig.2(b).
This suppression of the level repulsion signals a non-Hermitian-induced level attraction in the weak-γ\gammaregion.

For the two upper levels, the|±⟩|\pm\ranglesector determinant in Eq. (34) controls the𝒫​𝒯\mathcal{PT}-symmetry breaking.
The two eigenvaluesE|−⟩E_{|-\rangle}andE+E_{+}satisfy(E−ε1r)2≈t32−(ε1i)2(E-\varepsilon_{1}^{\rm r})^{2}\approx t_{3}^{2}-(\varepsilon_{1}^{\rm i})^{2}(neglecting the couplingt1t_{1}), and coalesce whenε1i=|t3|\varepsilon_{1}^{\rm i}=|t_{3}|, i.e.,γp​t≈2​|t3|/(Cε​3)\gamma_{pt}\approx 2|t_{3}|/(C_{\varepsilon}\sqrt{3}).

## B.3The general case

The𝒫​𝒯\mathcal{PT}pairing|s⟩↔|q−s+1⟩|s\rangle\leftrightarrow|q-s+1\rangleencoded in Eq. (25) has fundamentally different consequences for odd and evenqq. For oddq=2​m+1q=2m+1, the sublattices in each moiré unit cell formmm𝒫​𝒯\mathcal{PT}-conjugate pairs together with one additional self-conjugate center sublatticesc=(q+1)/2=m+1s_{c}=(q+1)/2=m+1atRsc=q​πR_{s_{c}}=q\pi.
From Eq. (25), its onsite energy satisfiesεsc=ε0−Cε\varepsilon_{s_{c}}=\varepsilon_{0}-C_{\varepsilon}andεsci=0\varepsilon_{s_{c}}^{\rm i}=0, and is therefore purely real.
For evenqq, no self-conjugate center sublattice exists, and every sublattice belongs to a𝒫​𝒯\mathcal{PT}-conjugate pair.

To determine the coupling of the center sublattice for oddqq, we introduce the pairing basis|s,±⟩≡(|s⟩±|q−s+1⟩)/2|s,\pm\rangle\equiv(|s\rangle\pm|q-s+1\rangle)/\sqrt{2}, withs=1,…,ms=1,\ldots,m.
In the original site basis, the center state|sc⟩=|m+1⟩|s_{c}\rangle=|m+1\ranglecouples only to its nearest neighbors|m⟩|m\rangleand|m+2⟩|m+2\rangle.
These two states form the last conjugate pair|m,±⟩=(|m⟩±|m+2⟩)/2|m,\pm\rangle=(|m\rangle\pm|m+2\rangle)/\sqrt{2}.
Because the two corresponding hoppings are equal under the𝒫​𝒯\mathcal{PT}pairing, their antisymmetric contributions cancel, and the center state couples only to|m,+⟩|m,+\rangle. Equivalently,⟨m,+|H|​sc⟩=2​tm\langle m,+|H|s_{c}\rangle=\sqrt{2}t_{m}, whereas⟨m,−|H|​sc⟩=0\langle m,-|H|s_{c}\rangle=0.

In the paired basis(|1,−⟩,|1,+⟩,…,|m,−⟩,|m,+⟩,|sc⟩)T\left(|1,-\rangle,|1,+\rangle,\ldots,|m,-\rangle,|m,+\rangle,|s_{c}\rangle\right)^{\rm T}, the odd-qqBloch Hamiltonian takes the block-tridiagonal formℋ​(k)=[𝐇1​(k)𝐓12𝟎⋯𝟎𝐓12T𝐇2⋱⋮𝟎⋱⋱⋱𝟎⋮⋱𝐇m𝐕m,c𝟎⋯𝟎𝐕m,cTεsc].\displaystyle\mathcal{H}(k)=\begin{bmatrix}\mathbf{H}_{1}(k)&\mathbf{T}_{12}&\mathbf{0}&\cdots&\mathbf{0}\\
\mathbf{T}_{12}^{\rm T}&\mathbf{H}_{2}&\ddots&&\vdots\\
\mathbf{0}&\ddots&\ddots&\ddots&\mathbf{0}\\
\vdots&&\ddots&\mathbf{H}_{m}&\mathbf{V}_{m,c}\\
\mathbf{0}&\cdots&\mathbf{0}&\mathbf{V}_{m,c}^{\rm T}&\varepsilon_{s_{c}}\end{bmatrix}.(38)

Here, each boldface diagonal block𝐇s\mathbf{H}_{s}is a2×22\times 2𝒫​𝒯\mathcal{PT}-symmetric matrix associated with one conjugate sublattice pair. The onlykk-dependent block is𝐇1​(k)\mathbf{H}_{1}(k), which originates from the intercell hoppingtqt_{q}connecting the two sites of the outermost conjugate pair:𝐇1​(k)=[ε1r−tq​cos⁡θki​(ε1i−tq​sin⁡θk)i​(ε1i+tq​sin⁡θk)ε1r+tq​cos⁡θk].\displaystyle\mathbf{H}_{1}(k)=\begin{bmatrix}\varepsilon_{1}^{\rm r}-t_{q}\cos\theta_{k}&i(\varepsilon_{1}^{\rm i}-t_{q}\sin\theta_{k})\\
i(\varepsilon_{1}^{\rm i}+t_{q}\sin\theta_{k})&\varepsilon_{1}^{\rm r}+t_{q}\cos\theta_{k}\end{bmatrix}.(39)

The remaining diagonal blocks arekk-independent and take the form𝐇s=[εsri​εsii​εsiεsr],s=2,…,m.\displaystyle\mathbf{H}_{s}=\begin{bmatrix}\varepsilon_{s}^{\rm r}&i\varepsilon_{s}^{\rm i}\\
i\varepsilon_{s}^{\rm i}&\varepsilon_{s}^{\rm r}\end{bmatrix},\qquad s=2,\ldots,m.(40)

The inter-pair couplings and the coupling to the center site are𝐓s,s+1=ts​𝐈2\mathbf{T}_{s,s+1}=t_{s}\mathbf{I}_{2}fors=1,…,m−1s=1,\ldots,m-1and𝐕m,c=2​tm​(0,1)T\mathbf{V}_{m,c}=\sqrt{2}t_{m}(0,1)^{\rm T}, respectively.

The form of𝐕m,c\mathbf{V}_{m,c}explicitly shows that the additional self-conjugate state|sc⟩|s_{c}\ranglecouples directly only to the symmetric state|m,+⟩|m,+\rangle. Its coupling to the antisymmetric state|m,−⟩|m,-\rangleis indirect and occurs through the imaginary matrix elementi​εmii\varepsilon_{m}^{\rm i}in𝐇m\mathbf{H}_{m}[Eq. (40)].
Sinceεsci=0\varepsilon_{s_{c}}^{\rm i}=0and the lowest eigenstate is dominated by the self-conjugate center site in the lattice considered here, its first-order energy correction from the imaginary potential vanishes.
Its leading correction at weakγ\gammais therefore second order and real. Consequently, the lowest band remains real over a broader range of non-Hermiticity, while the directly coupled second and third bands reach𝒫​𝒯\mathcal{PT}-breaking exceptional points first.

For evenqq, the additional self-conjugate center site and the scalar blockεsc\varepsilon_{s_{c}}are absent. The paired basis then consists entirely of|s,±⟩|s,\pm\rangledoublets, and the Hamiltonian contains only coupled2×22\times 2𝒫​𝒯\mathcal{PT}-symmetric blocks. The lowest doublet therefore couples directly through the imaginary onsite terms and breaks𝒫​𝒯\mathcal{PT}symmetry first. Thus, the presence or absence of the additional self-conjugate center site determines the first symmetry-breaking band pair and provides the structural origin of the parity-dependent response of the lowest-band flatness.

## B.4Nontrivial relative phase in a moiré lattice

In experimental realisations of bichromatic optical lattices, the primary and secondary lattices generally possess independent relative phases with respect to the laboratory frame.
The real part of the potential is accordingly generalized toV~r​(z)=Vp​cos⁡(z+ϕp)+Vs​cos⁡(α​z+ϕs),\tilde{V}^{\rm r}(z)=V_{p}\cos\left(z+\phi_{p}\right)+V_{s}\cos\left(\alpha z+\phi_{s}\right),(41)

withVp,Vs>0V_{p},V_{s}>0. The imaginary part, on the other hand, carries no phase degree of freedom; its form is determined by the effective non‑Hermitian control in experiments[66,67,68,69,65]V~i​(z)=γ​VI​sin⁡(α​z),VI≡Vs.\displaystyle\tilde{V}^{\rm i}(z)=\gamma V_{I}\sin\left(\alpha z\right),~~V_{I}\equiv V_{s}.(42)

Imposing𝒫​𝒯\mathcal{PT}symmetry,V~∗​(−z)=V~​(z)\tilde{V}^{*}(-z)=\tilde{V}(z), constrainsϕp=np​π\phi_{p}=n_{p}\piandϕs=ns​π\phi_{s}=n_{s}\piwithnp,ns∈ℤn_{p},n_{s}\in\mathbb{Z}.
Modulo2​π2\pi, this yields four distinct𝒫​𝒯\mathcal{PT}-symmetric configurations,(ϕp,ϕs)∈{(0,0),(0,π),(π,0),(π,π)}.(\phi_{p},\phi_{s})\in\left\{(0,0),~(0,\pi),~(\pi,0),~(\pi,\pi)\right\}.(43)

These four classes are inequivalent under spatial translations of the coordinate, and they correspond to the four distinct combinations of red‑ and blue‑detuned primary and secondary lattices:
- •

I(0,0)(0,0):   both blue‑detuned;
- •

II(0,π)(0,\pi):  primary blue, secondary red‑detuned;
- •

III(π,0)(\pi,0): primary red, secondary blue‑detuned;
- •

IV(π,π)(\pi,\pi): both red‑detuned.

We now use the tight-binding model to examine how the relative phases modify the low-energy𝒫​𝒯\mathcal{PT}-breaking sequence in all four classes.

We construct a single-band tight-binding model using the maximally localized Wannier functions of the primary lattice.
The Wannier centers are determined by the minima of the primary potential:Rs={(2​s−1)​π,(I,II),2​(s−1)​π,(III,IV),s=1,…,q.R_{s}=\begin{cases}(2s-1)\pi,&({\rm I,II}),\\
2(s-1)\pi,&({\rm III,IV}),\end{cases}\qquad s=1,\ldots,q.(44)

The shape and parity of the Wannier functions are independent ofϕp\phi_{p}andϕs\phi_{s}because the primary-lattice depth|Vp||V_{p}|is unchanged.

The tight-binding parameters for the four configurations are obtained from the overlap integrals defined in Eqs. (24)–(26).
The primary-lattice phaseϕp\phi_{p}determines the positions and𝒫​𝒯\mathcal{PT}pairing of the Wannier centers through Eq. (44), whereas the secondary-lattice phaseϕs\phi_{s}changes the ordering of their real onsite energies.
The imaginary potential itself remains unchanged because it is generated independently of the detuning configuration.

The𝒫​𝒯\mathcal{PT}-pairing relations are determined byϕp\phi_{p}:ϕp=0​(I,II):\displaystyle\phi_{p}=0~({\rm I,II}):ε~s=ε~q−s+1∗,t~s=t~q−s∗;\displaystyle\widetilde{\varepsilon}_{s}=\widetilde{\varepsilon}_{q-s+1}^{*},\quad\widetilde{t}_{s}=\widetilde{t}_{q-s}^{*};(45)ϕp=π​(III,IV):\displaystyle\phi_{p}=\pi~({\rm III,IV}):ε~s=ε~q−s+2∗,t~s=t~q−s+1∗.\displaystyle\widetilde{\varepsilon}_{s}=\widetilde{\varepsilon}_{q-s+2}^{*},\quad\widetilde{t}_{s}=\widetilde{t}_{q-s+1}^{*}.

The corresponding self-conjugate sites areϕp=0​(I,II):\displaystyle\phi_{p}=0\;(\mathrm{I,II}):ε~(q+1)/2∈ℝ,(odd​q),\displaystyle\tilde{\varepsilon}_{(q+1)/2}\in\mathbb{R},~~~(\mathrm{odd}\;q),(46)ϕp=π​(III,IV):\displaystyle\phi_{p}=\pi\;(\mathrm{III,IV}):{ε~1∈ℝ,(all​q),ε~q/2+1∈ℝ,(even​q).\displaystyle

However, the existence of a self-conjugate site alone does not determine the low-energy𝒫​𝒯\mathcal{PT}-breaking sequence.
Such a site delays the breaking of the lowest band only when it belongs to the lowest-energy sector.
The breaking pattern is therefore jointly controlled by the𝒫​𝒯\mathcal{PT}-pairing geometry and the ordering of the real onsite energies.

In Class I, the self-conjugate center site belongs to the lowest-energy sector for oddqq, whereas no self-conjugate site exists for evenqq.
Consequently, the second and third bands undergo𝒫​𝒯\mathcal{PT}-symmetry breaking first for oddqq, while the lowest two bands break first for evenqq, as discussed in the main text.

In Class II, the phase shiftϕs=π\phi_{s}=\pireverses the ordering of the real onsite energies without changing the imaginary potential.
For oddqq, although a geometrically self-conjugate site still exists, it no longer corresponds to a lowest-energy minimum.
For evenqq, no self-conjugate site exists.
Therefore, for both odd and evenqq, the lowest states are mainly formed from𝒫​𝒯\mathcal{PT}-conjugate sites, and the lowest two bands undergo𝒫​𝒯\mathcal{PT}-symmetry breaking first.

Class III provides the clearest contrast with Class I.
The shiftϕp=π\phi_{p}=\pimoves the primary-lattice Wannier centers by half a primary-lattice period relative to the unchanged imaginary potential.
In this case, a lowest-energy self-conjugate site occurs for evenqqbut not for oddqq, thereby reversing the parity assignment of Class I.
Figures6(e) and6(f) show representative tight-binding and continuum spectra forq=4q=4andq=5q=5, respectively.
Forq=4q=4[Fig.6(e)],𝒫​𝒯\mathcal{PT}-symmetry breaking first occurs betweenE2E_{2}andE3E_{3}, while the lowest band remains real.
Forq=5q=5[Fig.6(f)], the lowest two bands form the first𝒫​𝒯\mathcal{PT}-breaking pair.

In Class IV, the secondary-lattice phase places at least one self-conjugate site in the lowest-energy sector for both odd and evenqq.
The lowest band is therefore protected from the first𝒫​𝒯\mathcal{PT}-breaking transition for both parities, and the first transition instead involves higher bands.

The four configurations thus exhibit distinct low-energy breaking patterns.
Class I shows the parity dependence discussed in the main text, while Class III reverses the roles of odd and evenqq.
Classes II and IV remove the odd–even distinction: the lowest two bands break first for both parities in Class II, whereas the lowest band remains real at the first𝒫​𝒯\mathcal{PT}-symmetry breaking for both parities in Class IV.
Based on the connection established in Sec.IIIbetween the first𝒫​𝒯\mathcal{PT}-symmetry breaking pair and the lowest-band dispersion, we expect the associated monotonic and nonmonotonic responses to follow the same classification.
For conciseness, only the representative Class III spectra are shown in Fig.6; the results for Classes II and IV are summarized above.Figure 7:Over the fitting interval,DqD_{q}is approximately linear inγ\sqrt{\gamma}forq=5q=5andq=7q=7in the continuum model atV0=0.8V_{0}=0.8.
The red lines are linear fitsDq≃c1​γ+c2D_{q}\simeq c_{1}\sqrt{\gamma}+c_{2}over the range2≤γ≤92\leq\gamma\leq 9, where we track the real branch continuously connected to the Hermitian lowest band.
This branch remains sufficiently separated from the other bands in the complex-energy plane.
The lower‑left table lists the fitted parameters and the correspondingR2R^{2}values for eachqq.

## Appendix CThe effective hopping in the large-γ\gammaregime

The tight-binding analysis in AppendixBrelies on the lowest band of the primary lattice, for which only the lowest Wannier orbital of that lattice is retained; the secondary lattice enters solely through the matrix elementsCεC_{\varepsilon}andCtC_{t}.
At largeγ\gamma, this truncation becomes inadequate because the strength of the imaginary potentiali​γ​sin⁡(z/q)i\gamma\sin(z/q)becomes comparable to the primary lattice band gap, thereby mixing higher Wannier orbitals into the lowest band states and suppressing propagation beyond what fixed hopping integrals can capture.
A clear manifestation of this breakdown is the monotonic decrease ofD5D_{5}with increasingγ\gammain Fig.2(g), which signals the progressive failure of Eq. (23).

This section explains the flattening of the lowest band with increasingγ\gammafor oddqq.
We construct a tight-binding model using Wannier functions obtained from the eigenstates of the full non-Hermitian HamiltonianH~=−4​∂z2+V~​(z)\tilde{H}=-4\partial_{z}^{2}+\tilde{V}(z).
The width of the lowest bandwq≈4​|teff|w_{q}\approx 4|t_{\rm eff}|is set by the effective hopping between equivalent Wannier centers in neighboring cells[80,26].
The hopping integral isteff​(γ)≡∫−∞∞[WL​(z−Rc)]∗​H~​WR​(z+Rc)​𝑑z.t_{\rm eff}(\gamma)\equiv\int_{-\infty}^{\infty}[W_{L}(z-R_{c})]^{*}\tilde{H}W_{R}(z+R_{c})dz.(47)

Here,WLW_{L}andWRW_{R}denote the left and right Wannier functions constructed from the eigenstates ofH~†\tilde{H}^{\dagger}andH~\tilde{H}, respectively.

At largeγ\gamma, the imaginary part of the potential dominates in the tail region away from the zeros ofsin⁡(z/q)\sin(z/q), so thatV~​(z)≈i​γ​Vs​sin⁡(z/q)\tilde{V}(z)\approx i\gamma V_{s}\sin(z/q).
Although this approximation is not locally valid near the zeros atz=n​π​qz=n\pi q, including those corresponding to the Wannier centers and the midpoint between neighbouring centers, these narrow matching regions contribute only subleading corrections to the large-γ\gammaaction.
Substituting the left and right ansatzesWL​(z)∝e−SL​(z),WR​(z)∝e−SR​(z),\displaystyle W_{L}(z)\propto e^{-S_{L}(z)},\qquad W_{R}(z)\propto e^{-S_{R}(z)},(48)

into the corresponding eigenvalue equations gives−4​[(SL′)2−SL′′]−i​γ​Vs​sin⁡(z/q)\displaystyle-4[(S_{L}^{\prime})^{2}-S_{L}^{\prime\prime}]-i\gamma V_{s}\sin(z/q)=E∗,\displaystyle=E^{*},(49)−4​[(SR′)2−SR′′]+i​γ​Vs​sin⁡(z/q)\displaystyle-4[(S_{R}^{\prime})^{2}-S_{R}^{\prime\prime}]+i\gamma V_{s}\sin(z/q)=E.\displaystyle=E.(50)

In the tail region away from the zeros ofsin⁡(z/q)\sin(z/q), the logarithmic derivatives vary slowly, such that|SL,R′′|≪|SL,R′|2|S_{L,R}^{\prime\prime}|\ll|S_{L,R}^{\prime}|^{2}, and the second-derivative terms can therefore be neglected.
Choosing the branch of the square root that ensuresRe​[SL,R′]≥0{\rm Re}[S_{L,R}^{\prime}]\geq 0(outward decay), we obtainSL,R′​(z)≈(1∓i​σ)​γ​Vs8​|sin⁡zq|,\displaystyle S_{L,R}^{\prime}(z)\approx(1\mp i\sigma)\sqrt{\frac{\gamma V_{s}}{8}\left|\sin\frac{z}{q}\right|},(51)

whereσ=sgn​[sin⁡(z/q)]\sigma={\rm sgn}\left[\sin(z/q)\right].
Integrating outward from the corresponding Wannier centers shows that the left and right Wannier tails generally have different complex phases,SL≠SRS_{L}\neq S_{R}.
However, their leading real decay laws are the same. Forβ=L,R\beta=L,R, we haveSβr​(z)≈γ​Vs8​|∫Rβz|sin⁡z′q|​𝑑z′|+o​(γ),\displaystyle S_{\beta}^{\rm r}(z)\approx\sqrt{\frac{\gamma V_{s}}{8}}\left|\int_{R_{\beta}}^{z}\sqrt{\left|\sin\frac{z^{\prime}}{q}\right|}\,dz^{\prime}\right|+o(\sqrt{\gamma}),(52)

withRβ=±RcR_{\beta}=\pm R_{c}.
The action accumulated in the narrow matching regions nearz=n​π​qz=n\pi qcontributes only to subleading terms.
The real partSβr​(z)S_{\beta}^{\rm r}(z)controls the decay of the corresponding Wannier function amplitude,|Wβ​(z)|≈Nβ​e−Sβr​(z),|W_{\beta}(z)|\approx N_{\beta}e^{-S_{\beta}^{\rm r}(z)},(53)

whereNβN_{\beta}is the normalization constant.

Returning to the definition (47), the leading exponential dependence of the hopping is determined by the overlap of the two Wannier tails in the region between the neighbouring centers±π​q\pm\pi q. Choosingz=0z=0as a convenient matching point, the overlap amplitude scales as|[WL​(−Rc)]∗​WR​(Rc)|∼exp⁡(−κ​γ).\displaystyle\left|[W_{L}(-R_{c})]^{*}W_{R}(R_{c})\right|\sim\exp(-\kappa\sqrt{\gamma}).(54)

Using Eq. (52), the leading large-γ\gammaexponent isκ​γ\kappa\sqrt{\gamma}, whereκ=q​Vs8​∫02​π|sin⁡u|​𝑑u,\displaystyle\kappa=q\sqrt{\frac{V_{s}}{8}}\int_{0}^{2\pi}\sqrt{|\sin u|}du,(55)

and the effective hopping exhibits the following behaviorteff​(γ)∼C​(γ)​exp⁡(−κ​γ).\displaystyle t_{\rm eff}(\gamma)\sim C({\gamma})\exp(-\kappa\sqrt{\gamma}).(56)

The remaining operator contribution, the local matching coefficients, and the normalization of the left and right Wannier functions can be absorbed into a subexponential prefactorC​(γ)C(\gamma), andln⁡C​(γ)=o​(γ)\ln C(\gamma)=o(\sqrt{\gamma}).

To leading order in the large-γ\gammaregime, the logarithmic bandwidth can be approximated over a finite fitting interval by the linear formDq≃c1​γ+c2,c1=−κ/ln⁡10<0.\displaystyle D_{q}\simeq c_{1}\sqrt{\gamma}+c_{2},~~~~c_{1}=-{\kappa}/{\ln 10}<0.~~(57)

Here,c2c_{2}is an effective intercept that accounts for the subleading contribution of the prefactorC​(γ)C(\gamma)and the local matching regions over the finite fitting interval.

Thisγ\sqrt{\gamma}dependence is supported by direct numerical diagonalization of the continuum model: over2≤γ≤92\leq\gamma\leq 9, the data forDqD_{q}in Fig.7are well fitted byc1​γ+c2c_{1}\sqrt{\gamma}+c_{2}.
The leadingγ\sqrt{\gamma}scaling ofDqD_{q}follows from the stretched-exponential decay of the Wannier function tails at largeγ\gamma; the analytic expression forκ\kappaqualitatively captures the asymptotic slopec1c_{1}.

## References
- Lewensteinet al.[2007]M. Lewenstein, A. Sanpera,
V. Ahufinger, B. Damski, A. Sen(De), and U. Sen,Adv. Phys.56, 243 (2007).
- Blochet al.[2008]I. Bloch, J. Dalibard, and W. Zwerger,Rev. Mod. Phys.80, 885 (2008).
- Zhanget al.[2018]D.-W. Zhang, Y.-Q. Zhu,
Y. X. Zhao, H. Yan, and S.-L. Zhu,Adv. Phys.67, 253 (2018).
- Menget al.[2023]Z. Meng, L. Wang, W. Han, F. Liu, K. Wen, C. Gao, P. Wang, C. Chin, and J. Zhang,Nature615, 231 (2023).
- Caoet al.[2018a]Y. Cao, V. Fatemi,
S. Fang, K. Watanabe, T. Taniguchi, E. Kaxiras, and P. Jarillo-Herrero,Nature556, 43 (2018a).
- Caoet al.[2018b]Y. Cao, V. Fatemi,
A. Demir, S. Fang, S. L. Tomarken, J. Y. Luo, J. D. Sanchez-Yamagishi, K. Watanabe, T. Taniguchi, and E. Kaxiras,Nature556, 80 (2018b).
- Luet al.[2019]X. Lu, P. Stepanov,
W. Yang, M. Xie, M. A. Aamir, I. Das, C. Urgell, K. Watanabe,
T. Taniguchi, G. Zhang, A. Bachtold, A. H. MacDonald, and D. K. Efetov,Nature574, 653 (2019).
- Yankowitzet al.[2019]M. Yankowitz, S. Chen,
H. Polshyn, Y. Zhang, K. Watanabe, T. Taniguchi, D. Graf, A. F. Young, and C. R. Dean,Science363, 1059 (2019).
- Jinet al.[2021]C. Jin, Z. Tao, T. Li, Y. Xu, Y. Tang, J. Zhu, S. Liu, K. Watanabe, T. Taniguchi, J. C. Hone, L. Fu, J. Shan, and K. F. Mak,Nat. Mater.20, 940 (2021).
- Vu and Das Sarma [2021]D. Vu and S. Das Sarma, Phys. Rev. Lett.126, 036803 (2021).
- Gonçalveset al.[2024]M. Gonçalves, B. Amorim,
F. Riche, E. V. Castro, and P. Ribeiro,Nat. Phys.20, 1933 (2024).
- Zhanget al.[2025]G.-Q. Zhang, L.-Z. Tang,
L. F. Quezada, S.-H. Dong, and D.-W. Zhang, Commun. Phys.8,10.1038/s42005-025-02197-9(2025).
- Nguyenet al.[2022]D. X. Nguyen, X. Letartre,
E. Drouard, P. Viktorovitch, H. C. Nguyen, and H. S. Nguyen,Phys. Rev. Res.4, L032031 (2022).
- Talukdaret al.[2022]T. H. Talukdar, A. L. Hardison, and J. D. Ryckman,ACS Photonics9, 1286 (2022).
- Yuet al.[2023]D. Yu, G. Li, L. Wang, D. Leykam, L. Yuan, and X. Chen,Phys. Rev. Lett.130, 143801 (2023).
- Xiaet al.[2024]X. Xia, Q. Liu, B. Zou, P. Hong, and Y. Liang,Opt. Lett.49, 2553 (2024).
- Trushinet al.[2025]S. M. Trushin, T. Ito,
Y. Ishii, S. Iwamoto, and Y. Ota,Opt. Lett.50, 2405 (2025).
- Liet al.[2025]G. Li, Y. He, L. Wang, Y. Yang, D. Yu, Y. Zheng, L. Yuan, and X. Chen,Phys. Rev. Lett.134, 083803 (2025).
- Nath and Roy [2014]A. Nath and U. Roy,Laser Phys. Lett.11, 115501 (2014).
- Nathet al.[2022]A. Nath, J. Bera, M. R. Pathak, and U. Roy, EUR PHYS J D76,10.1140/epjd/s10053-022-00571-8(2022).
- Raghavet al.[2022]S. Raghav, B. Halder,
P. Basu, and U. Roy,Phys. Rev. A106, 063304 (2022).
- Zhouet al.[2025]L. Zhou, Z.-C. Li,
K. Zhang, Z. Lan, A. Celi, and W. Zhang,Phys. Rev. A112, 043718 (2025).
- Roatiet al.[2008]G. Roati, C. D’Errico,
L. Fallani, M. Fattori, C. Fort, M. Zaccanti, G. Modugno, M. Modugno, and M. Inguscio,Nature453, 895 (2008).
- Schreiberet al.[2015]M. Schreiber, S. S. Hodgman, P. Bordia,
H. P. Lüschen, M. H. Fischer, R. Vosk, E. Altman, U. Schneider, and I. Bloch,Science349, 842 (2015).
- Kohlertet al.[2019]T. Kohlert, S. Scherg,
X. Li, H. P. Lüschen, S. Das Sarma, I. Bloch, and M. Aidelsburger,Phys. Rev. Lett.122, 170403 (2019).
- Ashidaet al.[2020]Y. Ashida, Z. Gong, and M. Ueda,Adv. Phys.69, 249 (2020).
- Bergholtzet al.[2021]E. J. Bergholtz, J. C. Budich, and F. K. Kunst,Rev. Mod. Phys.93, 015005 (2021).
- Bender and Boettcher [1998]C. M. Bender and S. Boettcher,Phys. Rev. Lett.80, 5243 (1998).
- Bender [2007]C. M. Bender,Rep. Prog. Phys.70, 947 (2007).
- Konotopet al.[2016]V. V. Konotop, J. Yang, and D. A. Zezyulin,Rev. Mod. Phys.88, 035002 (2016).
- Musslimaniet al.[2008]Z. H. Musslimani, K. G. Makris, R. El-Ganainy, and D. N. Christodoulides,Phys. Rev. Lett.100, 030402 (2008).
- Longhi [2009]S. Longhi,Phys. Rev. Lett.103, 123601 (2009).
- Makriset al.[2010]K. G. Makris, R. El-Ganainy,
D. N. Christodoulides, and Z. H. Musslimani,Phys. Rev. A81, 063807 (2010).
- Midyaet al.[2010]B. Midya, B. Roy, and R. Roychoudhury,Phys. Lett. A374, 2605 (2010).
- Graefe and Jones [2011]E.-M. Graefe and H. F. Jones,Phys. Rev. A84, 013818 (2011).
- Jones [2014]H. F. Jones,Int. J. Theor. Phys.54, 3986 (2014).
- Abdullaevet al.[2010]F. K. Abdullaev, V. V. Konotop, M. Salerno, and A. V. Yulin,Phys. Rev. E82, 056606 (2010).
- Zhouet al.[2010]K. Zhou, Z. Guo, J. Wang, and S. Liu,Opt. Lett.35, 2928 (2010).
- Zhuet al.[2011]X. Zhu, H. Wang, L.-X. Zheng, H. Li, and Y.-J. He,Opt. Lett.36, 2680 (2011).
- Nixonet al.[2012a]S. Nixon, Y. Zhu, and J. Yang,Opt. Lett.37, 4874 (2012a).
- Nixonet al.[2012b]S. Nixon, L. Ge, and J. Yang,Phys. Rev. A85, 023822 (2012b).
- Zhanget al.[2021]Y. Zhang, Z. Chen,
B. Wu, T. Busch, and V. V. Konotop,Phys. Rev. Lett.127, 034101 (2021).
- Salasnichet al.[2002]L. Salasnich, A. Parola, and L. Reatto,Phys. Rev. A65, 043614 (2002).
- Liebet al.[2003]E. H. Lieb, R. Seiringer, and J. Yngvason,Phys. Rev. Lett.91, 150401 (2003).
- Pethick and Smith [2008]C. J. Pethick and H. Smith,Bose–Einstein
condensation in dilute gases(Cambridge university
press, 2008).
- Haaget al.[2014]D. Haag, D. Dast, A. Löhle, H. Cartarius, J. Main, and G. Wunner,Phys. Rev. A89, 023601 (2014).
- Lyeet al.[2007]J. E. Lye, L. Fallani,
C. Fort, V. Guarrera, M. Modugno, D. S. Wiersma, and M. Inguscio,Phys. Rev. A75, 061603 (2007).
- Biddle and Das Sarma [2010]J. Biddle and S. Das Sarma,Phys. Rev. Lett.104, 070601 (2010).
- Zezyulin and Alfimov [2024]D. A. Zezyulin and G. L. Alfimov,Phys. Rev. A110, 063304 (2024).
- Machholmet al.[2004]M. Machholm, A. Nicolin,
C. J. Pethick, and H. Smith,Phys. Rev. A69, 043604 (2004).
- Zhang and Wu [2009]Y. Zhang and B. Wu,Phys. Rev. Lett.102, 093905 (2009).
- Gutöhrleinet al.[2015]R. Gutöhrlein, J. Schnabel, I. Iskandarov, H. Cartarius, J. Main, and G. Wunner,J. Phys. A: Math. Theor.48, 335302 (2015).
- Jianget al.[2023]H. Jiang, E. Cheng,
Z. Zhou, and L.-J. Lang,Chin. Phys. B32, 084203 (2023).
- Wanget al.[2022]W.-Y. Wang, B. Sun, and J. Liu,Phys. Rev. A106, 063708 (2022).
- Dizdarevicet al.[2015]D. Dizdarevic, D. Dast,
D. Haag, J. Main, H. Cartarius, and G. Wunner,Phys. Rev. A91, 033636 (2015).
- Pelinovskyet al.[2013]D. E. Pelinovsky, P. G. Kevrekidis, and D. J. Frantzeskakis,Europhysics Letters101, 11002 (2013).
- Linet al.[2025]H. Lin, J. Pi, Y. Qi, W. Qin, F. Nori, and G.-L. Long,(2025),arXiv:2404.16774 [quant-ph].
- Wu and Niu [2003]B. Wu and Q. Niu,New J. Phys.5, 104 (2003).
- Vitanov and Suominen [1999]N. V. Vitanov and K.-A. Suominen,Phys. Rev. A59, 4580 (1999).
- Tiesingaet al.[1993]E. Tiesinga, B. J. Verhaar, and H. T. C. Stoof,Phys. Rev. A47, 4114 (1993).
- Inouyeet al.[1998]S. Inouye, M. R. Andrews,
J. Stenger, H.-J. Miesner, D. M. Stamper-Kurn, and W. Ketterle,Nature392, 151
(1998).
- Shenget al.[2013]J. Sheng, M.-A. Miri,
D. N. Christodoulides, and M. Xiao,Phys. Rev. A88, 041803 (2013).
- Wuet al.[2014]J.-H. Wu, M. Artoni, and G. C. La Rocca,Phys. Rev. Lett.113, 123004 (2014).
- Zhanget al.[2016]Z. Zhang, Y. Zhang,
J. Sheng, L. Yang, M.-A. Miri, D. N. Christodoulides, B. He, Y. Zhang, and M. Xiao,Phys. Rev. Lett.117, 123601 (2016).
- Tsunoet al.[2025]T. Tsuno, S. Taie,
Y. Takasu, K. Yamashita, T. Ozawa, and Y. Takahashi, Nature Communications17,10.1038/s41467-025-67106-8(2025).
- Liet al.[2019]J. Li, A. K. Harter,
J. Liu, L. de Melo, Y. N. Joglekar, and L. Luo, Nat.
Commun.10,10.1038/s41467-019-08596-1(2019).
- Takasuet al.[2020]Y. Takasu, T. Yagami,
Y. Ashida, R. Hamazaki, Y. Kuno, and Y. Takahashi,Prog. Theor. Exp.2020, 12A110 (2020).
- Renet al.[2022]Z. Ren, D. Liu, E. Zhao, C. He, K. K. Pak, J. Li, and G.-B. Jo,Nat. Phys.18, 385 (2022).
- Wanget al.[2024]C. Wang, N. Li, J. Xie, C. Ding, Z. Ji, L. Xiao, S. Jia, B. Yan, Y. Hu, and Y. Zhao,Phys. Rev. Lett.132, 253401 (2024).
- Gottlob and Schneider [2023]E. Gottlob and U. Schneider,Phys. Rev. B107, 144202 (2023).
- Johnstoneet al.[2025]D. Johnstone, S. Mishra,
Z. Zhu, and L. Sanchez-Palencia,Phys. Rev. A111, 043305 (2025).
- Marzariet al.[2012]N. Marzari, A. A. Mostofi, J. R. Yates,
I. Souza, and D. Vanderbilt,Rev. Mod. Phys.84, 1419 (2012).
- Peierls [1933]R. Peierls,Zeitschrift für Physik80, 763 (1933).
- Langet al.[2018]L.-J. Lang, Y. Wang, H. Wang, and Y. D. Chong,Phys. Rev. B98, 094307 (2018).
- Hanget al.[2013]C. Hang, G. Huang, and V. V. Konotop,Phys. Rev. Lett.110, 083604 (2013).
- Jin [2017]L. Jin,Phys. Rev. A96, 032103 (2017).
- Garmon and Noba [2021]S. Garmon and K. Noba,Phys. Rev. A104, 062215 (2021).
- Anastasiadiset al.[2022]A. Anastasiadis, G. Styliaris, R. Chaunsali, G. Theocharis, and F. K. Diakonos,Phys. Rev. B106, 085109 (2022).
- Yinet al.[2024]K. Yin, K. Tang, L. Tan, S. I. D. Bakhat, T. Dong, H. Zhu, and Y. Yang,(2024),arXiv:2411.00591 [physics.app-ph].
- Gonget al.[2018]Z. Gong, Y. Ashida,
K. Kawabata, K. Takasan, S. Higashikawa, and M. Ueda,Phys. Rev. X8, 031079 (2018).

## 


- 


Major funding support from
