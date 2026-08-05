# Molecular Dynamics-Derived Coloured Noise Mediates Anderson Localisation and Environment-Assisted Transport of Tryptophan Excitons in Tubulin

**arXiv ID**: 2607.11135v3
**Authors**: Chen Xin
**Published**: 2026-07-13
**Categories**: cond-mat.soft, physics.bio-ph, quant-ph
**Comments**: 15 pages, 5 main + 5 supplementary figures. Code: https://github.com/Varato/tubulin-bath-fluctuation v2: introduction tightened; citation and punctuation fixes; results unchanged. v3: added Fig. 1 fit-residual inset; clarified AIC model selection vs two-step parameter extraction; no scientific changes
**HTML URL**: https://arxiv.org/html/2607.11135v3

## Abstract

The tryptophan residues in tubulin $αβ$-dimers form an ordered aromatic network that has been proposed to support quantum exciton transport even under physiological environmental noise. Existing studies of this system mostly assume white-noise dephasing, but the statistical properties of the protein-solvent bath coupled to tryptophan sites remain uncharacterised under physiological conditions. Here we characterise this fluctuation bath via all-atom molecular dynamics simulations of a solvated tubulin dimer at 310 K, combining high-frequency and long-time trajectories with 10 fs and 10 ps sampling intervals. The resulting autocorrelation of the site-energy fluctuations is tri-exponential, with three well-separated decay modes: sub-100-fs and picosecond fluctuations driven by water dynamics, and a nanosecond mode originating from protein conformational rearrangements. All three modes fall deep within the non-Markovian regime. We further demonstrate that the slow protein mode introduces strong quasi-static disorder, which results in Anderson localisation, while the two fast water modes frequently tune chromophore pairs through resonance, enabling environment-assisted quantum transport (ENAQT). On the full eight-site network, the coloured-noise bath confines excitons predominantly to strongly coupled proximal tryptophan pairs, in marked contrast to the more uniform delocalisation predicted by the standard white-noise Haken-Strobl model. Our workflow generalises to other pigment-protein systems with solvent-exposed chromophores.

## Full Text

Molecular Dynamics-Derived Coloured Noise Mediates Anderson Localisation and Environment-Assisted Transport of Tryptophan Excitons in Tubulin

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.11135v3 [cond-mat.soft] 19 Jul 2026

## Molecular Dynamics-Derived Coloured Noise Mediates Anderson Localisation and Environment-Assisted Transport of Tryptophan Excitons in TubulinChen Xinimxinchen@outlook.com(July 15, 2026)

## Abstract

The tryptophan residues in tubulinα​β\alpha\beta-dimers form an ordered aromatic network that has been proposed to support quantum exciton transport even under physiological environmental noise. Existing studies of this system mostly assume white-noise dephasing, but the statistical properties of the protein–solvent bath coupled to tryptophan sites remain uncharacterised under physiological conditions. Here we characterise this fluctuation bath via all-atom molecular dynamics simulations of a solvated tubulin dimer at 310 K, combining high-frequency and long-time trajectories with 10 fs and 10 ps sampling intervals. The resulting autocorrelation of the site-energy fluctuations is tri-exponential, with three well-separated decay modes: sub-100-fs and picosecond fluctuations driven by water dynamics, and a nanosecond mode originating from protein conformational rearrangements. All three modes fall deep within the non-Markovian regime. We further demonstrate that the slow protein mode introduces strong quasi-static disorder, which results in Anderson localisation, while the two fast water modes frequently tune chromophore pairs through resonance, enabling environment-assisted quantum transport (ENAQT). On the full eight-site network, the coloured-noise bath confines excitons predominantly to strongly coupled proximal tryptophan pairs, in marked contrast to the more uniform delocalisation predicted by the standard white-noise Haken–Strobl model. Our workflow generalises to other pigment–protein systems with solvent-exposed chromophores.

## IIntroduction

The discovery of long-lived (660 fs) quantum coherence in the Fenna–Matthews–Olson (FMO) complex at cryogenic temperature (77 K)[1]ignited broad interest in quantum biology. Long assumed to wash out rapidly in warm and wet biological environments, quantum effects have been repeatedly observed under physiological conditions across photosynthetic systems: FMO coherence was subsequently observed at physiological temperature for at least 300 fs[2]; long-lasting excitation oscillations have been detected in cryptophyte algae light-harvesting proteins[3]; ultrafast energy transfer pathways have been mapped in plant light-harvesting complex II (LHCII) at room temperature[4]; and exciton–vibrational coherence has been observed in cyanobacterial allophycocyanin[5]for 501 fs, where the coherence is closely linked to molecular vibrations. These findings confirm that quantum effects can modulate biological exciton dynamics under native conditions.

Additionally, environment-assisted quantum transport (ENAQT) theory[6]has shown that thermal fluctuations can actively assist transport when their amplitude and correlation time fall in the appropriate regime, refining the early intuition that the protein environment acts purely as a decoherence source. Ref.[7]established that the dependence is non-monotonic, with transfer maximised at an optimal intermediate noise correlation time, and Ref.[8]recently confirmed this prediction experimentally in perovskite nanocrystal superlattices, where exciton diffusion peaks at a sample-dependent turnover temperature. The accuracy of environmental modelling is therefore a critical determinant of reliable theoretical predictions for excitonic systems.

Beyond photosynthetic antennae, the network of tryptophan residues inα​β\alpha\beta-tubulin dimers constitutes another naturally ordered chromophore system for investigating biological excitonic transport. Microtubules, ubiquitous eukaryotic cytoskeletal filaments assembled fromα​β\alpha\beta-tubulin dimers, contain eight tryptophan residues per dimer. With the lowest-energyLa1{}^{1}L_{a}excited state among natural amino acids and a large transition dipole moment, tryptophan serves as a natural exciton carrier with physical mechanisms directly analogous to those in photosynthetic systems. Early debates about quantum effects in microtubules focused on charge polarisation and conformational superposition states, with substantial disagreement over decoherence timescales[9,10]; the tryptophan excitonic degree of freedom, by contrast, provides a physically grounded and experimentally testable framework.

The first quantitative eight-site Hamiltonian for this system was established in Ref.[11], where exciton dynamics was treated under the Haken–Strobl white-noise approximation, a common simplification in the field.
Whether this simplification is justified depends strongly on the system: exact simulations show that neglecting the structured nature of the vibrational environment can bias electronic parameter estimates[12], yet studies on the FMO complex find that Markovian descriptions may still adequately capture energy transfer dynamics due to the masking effect of the phonon background[13].
The degree of non-Markovianity and the applicability of white-noise models therefore cannot be assumed a priori, and all-atom molecular dynamics (MD) has emerged as a powerful tool to characterise native environmental fluctuations inaccessible to static structural analysis[14].

Subsequent theoretical and experimental work has advanced our understanding of tubulin tryptophan excitons. Excitonic models extended to microtubule lattices predict superradiant lowest-energy exciton states and supertransfer[15], and a recent Lindblad-based analysis of multi-spiral microtubule assemblies identified subradiant retention channels and signatures of non-Markovian information backflow[16]. On the experimental side, tryptophan autofluorescence lifetime measurements revealed excitation diffusion lengths far exceeding Förster resonance energy transfer (FRET) predictions, which can be reversibly suppressed by volatile anaesthetics[17]; steady-state fluorescence quantum yield measurements further corroborated collective excitonic behaviour, showing elevated quantum yields in polymerised microtubules compared to isolated dimers[18].

However, existing theoretical studies of tubulin tryptophan excitons share a fundamental limitation: environmental modelling relies entirely on phenomenological assumptions without an atomistic foundation. While recent work has explored non-Markovianity arising from the structural connectivity of the microtubule lattice[16], the intrinsic non-Markovianity driven by the multi-timescale thermal fluctuations of the protein–solvent environment remains uncharacterised. Dephasing rates are artificially tuned, and the complex spectral density spanning four orders of magnitude is entirely ignored. No study to date has characterised the statistical properties and physical origins of tryptophan site-energy fluctuations directly from all-atom dynamics. Furthermore, although experiments suggest that environmental perturbations (e.g., by anaesthetics) alter energy transport via dielectric screening[17], the atomistic mechanism underlying this screening via protein–water electrostatic interactions remains unexplored.

In this work, we address these gaps by constructing a microscopic coloured-noise model for tryptophan site-energy fluctuations in the solvated tubulin dimer, derived entirely from all-atom MD simulations at 310 K with dual time-resolution. Our main findings are as follows. First, site-energy fluctuations follow a tri-exponential autocorrelation function with three well-separated relaxation timescales, all deep in the non-Markovian regime, demonstrating a qualitative failure of the Markovian approximation. Second, the slowest, protein-driven mode imposes strong quasi-static disorder and Anderson localisation, while faster water-driven modes break localisation and enable ENAQT, with native MD parameters falling within the optimal transport window. Third, source decomposition reveals strong protein–water electrostatic anticorrelation that suppresses effective disorder by a factor of∼2\sim\sqrt{2}via dielectric screening, providing a microscopic origin for tubulin’s high optical dielectric constant. Fourth, on the full eight-site network, the coloured-noise bath confines excitons to strongly coupled proximal pairs, in contrast to the uniform delocalisation predicted by the white-noise model, explaining the suppressed fluorescence yield of isolated dimers through disorder-induced localisation. This work moves tubulin exciton modelling beyond phenomenological dephasing toward atomistically derived multi-timescale baths, and the general workflow is applicable to other pigment–protein systems.

The remainder of this paper is organised as follows. SectionIIdetails the computational methods, SectionsIIIandIVpresent the results and their physical implications, and SectionVsummarises our conclusions.

## IIMethods

## II.1Molecular Dynamics Simulation Setup

The MD simulation was performed with GROMACS 2026.2[19]. The starting structure was taken from the Protein Data Bank as entry 1JFF[20], which contains theα\alphaandβ\betamonomers and three ligands: GTP, Mg2+, and GDP. The dimer carries GTP at the non-exchangeable (N) site on theα\alphamonomer and GDP at the exchangeable (E) site on theβ\betamonomer, with Mg2+coordinating the GTP phosphates. The dimer contains eight tryptophan (Trp) residues, referred to as Trp1–Trp8 throughout this work following the convention of Ref.[11]: Trp1–4 areα\alphaW21,α\alphaW346,α\alphaW388, andα\alphaW407 on chain A, and Trp5–8 areβ\betaW21,β\betaW101,β\betaW344, andβ\betaW397 on chain B. The missing residues in the PDB entry (39 in chain A and 19 in chain B) were repaired with PDBFixer, and protonation states of ionisable residues were predicted with PROPKA at pH 7.0 via PDB2PQR[21]. The protein was described with the AMBER99SB-ILDN[22]force field. GTP and GDP used the polyphosphate parameters from Ref.[23], which extend the AMBER parm94/99 family with atom charges and bonded terms for phosphate groups.111Parameter files obtained from the Bryce Group AMBER Parameter Database:http://personalpages.manchester.ac.uk/staff/Richard.Bryce/amber/cof/The solvated system contained 128,053 atoms in a12.39×7.83×13.3112.39\times 7.83\times 13.31nm3periodic box, with 37,976 TIP3P waters and 0.15 M NaCl. After steepest-descent energy minimisation toFmax<100F_{\max}<100kJ mol-1nm-1, the system was equilibrated in two stages: 100 ps NVT followed by 500 ps NPT, both at 310 K and 1 bar with position restraints on heavy atoms. A 50 ns unrestrained NPT production run was then carried out with a 2 fs timestep, LINCS bond constraints, and PME electrostatics using a 1.0 nm real-space cutoff and 0.12 nm grid spacing. Frames were saved every 10 ps. The first 10 ns showed residual equilibration drift and was excluded from analysis, leaving 4,001 frames from the 10–50 ns window. To resolve sub-picosecond solvent dynamics that the 10 ps cadence cannot capture, an additional 2 ns continuation trajectory was run from thet=50t=50ns endpoint with identical MD configuration but frames saved every 10 fs, yielding 200,001 frames. The two trajectories thus provide complementary time resolutions (Table1): the long trajectory captures nanosecond protein conformational dynamics, while the short trajectory resolves sub-picosecond solvent librations. The three ligands (GTP, Mg2+, and GDP) remained bound at their respective sites throughout the 50 ns trajectory. A movie of the full simulation is available as supplementary material.Figure 1:Dipole geometry of the eight tryptophans (Trp1–Trp8) in the tubulinα​β\alpha\beta-dimer, extracted from the MD frame att=50t=50ns. Each blue arrow starts at the centroid of an indole ring and points along𝝁m\bm{\mu}_{m}(from the benzene ring toward the pyrrole ring, reflecting the direction of the S→0La1{}_{0}\to{}^{1}L_{a}difference dipole). The dipole magnitudes are assumed identical (μ=5\mu=5D) for all Trp residues, but the directions𝒏m​(t)\bm{n}_{m}(t)fluctuate with the trajectory. The Trp1–Trp8 labels follow Ref.[11]: Trp1–4 areα\alphaW21,α\alphaW346,α\alphaW388,α\alphaW407 on chain A, and Trp5–8 areβ\betaW21,β\betaW101,β\betaW344,β\betaW397 on chain B.Table 1:The two MD trajectories used in this work. They share identical MD configurations (2 fs integrator step, deep thermal equilibration) and differ only in output cadenceΔ​t\Delta tfor data efficiency, and they resolve complementary timescales ofδ​ϵm​(t)\delta\epsilon_{m}(t).trajectoryΔ​t\Delta tframesspanNyquistlong10 ps4 00140 ns1.67 cm-1short0.01 ps200 0012 ns1668 cm-1

## II.2Site-energy Fluctuation Modelling

The site-energy fluctuation model is based on the linear Stark effect and the excitation Hamiltonian from Ref.[11].

The site energy of themm-th tryptophan in a tubulin dimer is the energy needed to excite the tryptophan fromS0S_{0}toLa1{}^{1}L_{a}, the lowest fluorescent excited state of tryptophan under physiological conditions. Ref.[11]formulates the site energyϵm\epsilon_{m}by three terms:ϵm=ϵ0+ϵqm+ϵcoul,\epsilon_{m}=\epsilon_{0}+\epsilon_{\mathrm{qm}}+\epsilon_{\mathrm{coul}},(1)

whereϵ0=35000\epsilon_{0}=35000cm-1is a constant baseline transition energy for spectral alignment. The quantum correction termϵqm\epsilon_{\mathrm{qm}}accounts for the intrinsic vertical excitation energy of each isolated Trp residue, obtained from scaled time-dependent density-functional theory (TD-DFT) calculations. The electrostatic contributionϵcoul\epsilon_{\mathrm{coul}}describes the environmentally induced electrochromic shift, evaluated via charge-density coupling (CDC) between the differential excitation charge density of each Trp and the background protein electrostatic field. In Ref.[11], the site energy is treated as static for subsequent exciton dynamics simulations performed via the Haken–Strobl pure-dephasing model.

To capture site-energy fluctuations induced by the thermal environment, we introduce time dependence to the site energies. We assume the quantum correction termϵqm\epsilon_{\mathrm{qm}}is time-invariant, so the temporal variation of the site energy arises predominantly from the electrostatic termϵcoul\epsilon_{\mathrm{coul}}. This approximation is well justified: small-amplitude side-chain rotations induce only minor variations in the intrinsic vertical excitation energy (on the order of tens of cm-1), which are far smaller than the electrostatically induced site-energy fluctuations (102−10310^{2}-10^{3}cm-1) and therefore contribute negligibly.

ϵcoul​(t)\epsilon_{\mathrm{coul}}(t)is evaluated within the linear Stark approximation, which involves only the transition difference dipole moment𝝁m\bm{\mu}_{m}of the indole ring of Trpmmand the local electric field𝑬m​(𝒓m,t)\bm{E}_{m}(\bm{r}_{m},t)at the indole ring center𝒓m\bm{r}_{m}:ϵcoul​(t)\displaystyle\epsilon_{\mathrm{coul}}(t)=−𝝁m⋅𝑬m​(𝒓m,t)\displaystyle=-\bm{\mu}_{m}\cdot\bm{E}_{m}(\bm{r}_{m},t)=−μ​(𝒏m​(t)⋅𝑬m​(𝒓m,t)).\displaystyle=-\mu\Big(\bm{n}_{m}(t)\cdot\bm{E}_{m}(\bm{r}_{m},t)\Big).(2)

Notice that here𝝁m\bm{\mu}_{m}is decomposed further into its magnitudeμ\mu(assumed constant for all Trp residues) and its direction𝒏m​(t)\bm{n}_{m}(t), as the orientational fluctuation dominates over the magnitude variation. The site-energy fluctuation of themm-th Trp is then given byδ​ϵm​(t)\displaystyle\delta\epsilon_{m}(t)=ϵm​(t)−⟨ϵm​(t)⟩T\displaystyle=\epsilon_{m}(t)-\langle\epsilon_{m}(t)\rangle_{T}=−μ​(𝒏m⋅𝑬m−⟨𝒏m⋅𝑬m⟩T),\displaystyle=-\mu\Big(\bm{n}_{m}\cdot\bm{E}_{m}-\langle\bm{n}_{m}\cdot\bm{E}_{m}\rangle_{T}\Big),(3)

where⟨⋅⟩T\langle\cdot\rangle_{T}denotes the time average over the MD trajectory.

The magnitudeμ\mufor tryptophan residues in protein interiors has been reported in the range of 4.82–8 D, and the electron density shifts from the pyrrole ring to the benzene ring upon excitation fromS0S_{0}toLa1{}^{1}L_{a}[24]. We adopt a representative value ofμ=5\mu=5D for all tryptophan residues, and use unit vectors pointing from the benzene to the pyrrole ring to represent the direction of the difference dipole moment. Figure1shows the geometry of the extracted dipole directions in one MD frame.

To compute the site-energy fluctuation, the local electric field𝑬m\bm{E}_{m}at the indole ring center𝒓m\bm{r}_{m}is extracted from the MD trajectory and projected onto the dipole direction𝒏m​(t)\bm{n}_{m}(t). The electric field𝑬m\bm{E}_{m}is computed by direct Coulomb summation over the explicit MD partial charges:𝑬m​(𝒓m,t)=14​π​ε0​∑i=1Kqi​e​𝒓m−𝒓i(bg)|𝒓m−𝒓i(bg)|3,\displaystyle\bm{E}_{m}(\bm{r}_{m},t)=\frac{1}{4\pi\varepsilon_{0}}\sum_{i=1}^{K}q_{i}\,e\,\frac{\bm{r}_{m}-\bm{r}_{i}^{(\mathrm{bg})}}{\lvert\bm{r}_{m}-\bm{r}_{i}^{(\mathrm{bg})}\rvert^{3}},(4)

whereε0\varepsilon_{0}is the vacuum permittivity,eeis the elementary charge,qiq_{i}are the AMBER99SB-ILDN partial charges (in units ofee) at positions𝒓i(bg)\bm{r}_{i}^{(\mathrm{bg})}of the background environment,KKis the total number of background atoms. The summation excludes all atoms belonging to the indole side chain of Trpmm, while including the protein backbone, other tryptophan residues, solvent molecules, nucleotides, and ions. The background charges are partitioned into four disjoint groups: protein, water, nucleotide, and ions. Therefore, Eq.4can be evaluated separately for each source, allowing the fluctuationδ​ϵm​(t)\delta\epsilon_{m}(t)to be decomposed accordingly.

The dielectric treatment requires careful explanation. In the static CDC site-energy calculation of Ref.[11], only protein partial charges enter the Coulomb sum, and the missing solvent screening is compensated by an effective optical dielectric constantεopt=8.41\varepsilon_{\mathrm{opt}}=8.41, the experimentally measured high-frequency dielectric of tubulin. In the MD-based approach, the trajectory explicitly resolves all sources of electrostatic response (solvent, ions, nucleotides, and protein), so the instantaneous fluctuation of𝑬m\bm{E}_{m}is captured intrinsically by the rearranged positions of these explicit partial charges, and no additional continuum dielectric is applied (εr=1\varepsilon_{r}=1, i.e., vacuum permittivity).

The two treatments are physically complementary. We retain the static Hamiltonian from Ref.[11], including mean site energies and inter-Trp couplings computed withεopt=8.41\varepsilon_{\mathrm{opt}}=8.41, as the baseline describing static energetic disorder. The MD-derived fluctuationδ​ϵm​(t)\delta\epsilon_{m}(t)is added on top to account for dynamic disorder induced by thermal motions. Inter-site excitonic couplings are treated as static throughout this work, as their relative fluctuations are substantially smaller than site-energy disorder and thus negligible.

## II.3Exciton Dynamics

Under the single-excitation approximation, the exciton Hamiltonian
is expressed in the site basis{|m⟩}m=18\{\ket{m}\}_{m=1}^{8}asH​(t)\displaystyle H(t)=H0+∑mδ​ϵm​(t)​|m⟩​⟨m|\displaystyle=H_{0}+\sum_{m}\delta\epsilon_{m}(t)\ket{m}\bra{m}=∑m(ϵm+δ​ϵm​(t))​|m⟩​⟨m|+∑m≠nJm​n​|m⟩​⟨n|\displaystyle=\sum_{m}(\epsilon_{m}+\delta\epsilon_{m}(t))\ket{m}\bra{m}+\sum_{m\neq n}J_{mn}\ket{m}\bra{n}(5)

whereϵm\epsilon_{m}is the site energy of themm-th tryptophan,Jm​nJ_{mn}is the excitonic coupling between sitesmmandnn,
andδ​ϵm​(t)\delta\epsilon_{m}(t)denotes the MD-derived site-energy fluctuations
described in Sec.II.2.
Bothϵm\epsilon_{m}andJm​nJ_{mn}are taken from Ref.[11].

The dynamics of each realisation are governed by the stochastic Schrödinger equation (SSE):i​ℏ​|ψ˙​(t)⟩=H​(t)​|ψ​(t)⟩.\displaystyle i\hbar|\dot{\psi}(t)\rangle=H(t)|\psi(t)\rangle.(6)

BecauseH​(t)H(t)is stochastic, physical observables are obtained by ensemble-averaging over many independent realisations.
The bath is fully characterised by its autocorrelation function (ACF).
Assuming the process is stationary (verified in AppendixC),
the ACF depends only on the lagτ=t−t′\tau=t-t^{\prime}:Cm​(τ)=⟨δ​ϵm​(t)​δ​ϵm​(t+τ)⟩T.\displaystyle C_{m}(\tau)=\langle\delta\epsilon_{m}(t)\,\delta\epsilon_{m}(t+\tau)\rangle_{T}.(7)

The ACF is well described by a tri-exponential decay with three
well-separated timescalesTkT_{k}(k=1,2,3k{=}1,2,3), as determined in
Sec.III.2.
All three modes lie deep in the non-Markovian regime
(Kubo numberκk=σk​Tk/ℏ≫1\kappa_{k}=\sigma_{k}T_{k}/\hbar\gg 1[25],
a dimensionless measure of bath memory; values reported in
Sec.III.4), requiring a coloured-noise treatment
rather than a Markovian white-noise approximation.

We therefore model the bath as a superposition of three independent
Ornstein–Uhlenbeck (OU) processes, one per timescale:δ​ϵm​(t)\displaystyle\delta\epsilon_{m}(t)=∑k=13xm,k​(t)\displaystyle=\sum_{k=1}^{3}x_{m,k}(t)(8)

wherexm,kx_{m,k}is an OU process with ACF⟨xm,k​(t)​xm,k​(t+τ)⟩T=σm,k2​e−|τ|/Tk\displaystyle\langle x_{m,k}(t)\,x_{m,k}(t+\tau)\rangle_{T}=\sigma_{m,k}^{2}\mathrm{e}^{-|\tau|/T_{k}}(9)

Each process can be sampled exactly using the Gillespie discretisation scheme[26]:xm,k​(t+d​t)=\displaystyle x_{m,k}(t+\mathrm{d}t)=xm,k​(t)​e−d​t/Tk\displaystyle x_{m,k}(t)e^{-\mathrm{d}t/T_{k}}+σm,k​1−e−2​d​t/Tk​ξ​(t),\displaystyle+\sigma_{m,k}\sqrt{1-e^{-2\mathrm{d}t/T_{k}}}\,\xi(t),(10)

whereξ​(t)\xi(t)is a random variable sampled from the standard normal distribution𝒩​(0,1)\mathcal{N}(0,1). Fig.2shows the ACF computed from the summation of the three sampled OU processes and the tri-exponential fit to the MD-derived ACF, confirming that the OU sampler reproduces the fitted statistics. The total fluctuation variance on each site is thenσm2=∑kσm,k2\sigma_{m}^{2}=\sum_{k}\sigma_{m,k}^{2}.Figure 2:ACF of the OU sum (a single 30 ns trajectory, five-realisation average; dots) versus the analytic target∑kfk​e−t/Tk\sum_{k}f_{k}e^{-t/T_{k}}(solid).Lower panel:residual (sampled−-theory). RMS residual=0.028=0.028over 10 fs–7.5 ns, confirming the sampler reproduces the fitted statistics.

The SSE is solved by Monte Carlo (MC) trajectory sampling.
For each ofNMC=500N_{\mathrm{MC}}=500independent bath realisations,
the stochastic Schrödinger equationi​ℏ​|ψ˙⟩=H​(t)​|ψ⟩i\hbar|\dot{\psi}\rangle=H(t)|\psi\rangleis integrated numerically with an adaptive-step ODE solver,
with the OU noise enteringH​(t)H(t)as time-dependent site-diagonal
coefficients sampled atd​t=2\mathrm{d}t=2fs.
The ensemble-averaged density matrixρ¯​(t)=NMC−1​∑i|ψi​(t)⟩​⟨ψi​(t)|\bar{\rho}(t)=N_{\mathrm{MC}}^{-1}\sum_{i}|\psi_{i}(t)\rangle\langle\psi_{i}(t)|yields the physical observables.
The resulting coloured-noise model (CNM) is compared against the
Haken–Strobl model (HSM)[27,28],
aδ\delta-correlated white-noise reference.
Computational parameters and results are given in
Sec.III.4.
Numerical propagation uses QuTiP v5.3.0[29].

## IIIResults

We now characterise the site-energy fluctuationsδ​ϵm​(t)\delta\epsilon_{m}(t)from two MD trajectories of complementary time resolution (Sec.II.1–II.2, Table1), with excitonic couplings and mean site energies from Ref.[11]. Prior dynamical studies on this Hamiltonian have treated the environment within the Haken–Strobl white-noise framework; the MD-derived bath presented below lies instead deep in the non-Markovian regime, and Sec.III.4quantifies the resulting differences in exciton transport.

This section is structured as follows. First, we quantify the overall amplitude and statistical properties of the site-energy fluctuations (Sec.III.1). Next, we dissect the multiple timescales of the underlying bath modes (Sec.III.2), decompose fluctuations by physical origin, and evaluate dielectric screening contributions from each environment component (Sec.III.3). We conclude by presenting exciton dynamics simulations under the coloured-noise bath, first on the strongly-coupled Trp4–Trp7 two-site system and then on the full eight-site network (Sec.III.4).

## III.1Magnitude and statistics of the fluctuationsTable 2:Per-site fluctuation characterisation.σ\sigma: standard deviation of the site-energy fluctuations from the long trajectory, taken as the total amplitude.σshort\sigma_{\mathrm{short}}: standard deviation from the short trajectory, which undersamples the nanosecond slow mode and is therefore systematically smaller (meanσ2/σshort2≈1.2\sigma^{2}/\sigma_{\mathrm{short}}^{2}\approx 1.2).σ/J\sigma/J: ratio ofσ\sigmato the strongest coupling|J47|=59|J_{47}|=59cm-1.fk,Tkf_{k},T_{k}: weights and timescales of the corrected tri-exponential fit to the autocorrelation (Sec.III.2); all times in ps.siteσ\sigma(cm-1)σshort\sigma_{\mathrm{short}}(cm-1)σ/J\sigma/Jf1f_{1}T1T_{1}(ps)f2f_{2}T2T_{2}(ps)f3f_{3}T3T_{3}(ps)Trp184478214.30.560.0360.360.510.071926Trp297275516.50.460.0270.400.640.14776Trp380663613.70.620.0680.141.770.246820Trp499986116.90.570.0410.371.000.058524Trp572172612.20.470.0500.130.410.39957Trp684694714.30.530.0620.318.580.16492Trp767562711.40.520.0340.380.580.09452Trp81453151224.60.360.0470.520.650.121358mean91485615.50.510.0460.331.770.162663

The site-energy fluctuationsδ​ϵm​(t)\delta\epsilon_{m}(t)are zero-mean by construction, approximately Gaussian, and stationary (AppendixC). The standard deviation from the long trajectoryσlong\sigma_{\mathrm{long}}is systematically larger than that from the short trajectoryσshort\sigma_{\mathrm{short}}(Table2), because the 2 ns short trajectory resolves the sub-picosecond bath but undersamples the nanosecond slow mode, whereas the 40 ns long trajectory captures both. Therefore, we takeσlong\sigma_{\mathrm{long}}as the total fluctuation amplitude, denoted asσ\sigmafor simplicity. Also notice that the ratioσ/J\sigma/Jranges from 11 (Trp7) to 25 (Trp8), placing every site deep in thestrong-disorderregime (σ/J≫1\sigma/J\gg 1), for which Anderson localisation of the exciton is expected.

## III.2Three well-separated relaxation timescalesFigure 3:Stitched autocorrelation and power spectrum of the site-energy fluctuations.(a)Self-normalised autocorrelationsCm​(t)C_{m}(t)(dots) with corrected tri-exponential fits (solid lines; two-step refit withT3T_{3}anchored to the long trajectory, Sec.III.2); per-siteR2≥0.972R^{2}\geq 0.972(mean0.9870.987).Inset: residualCm−CmfitC_{m}-C_{m}^{\mathrm{fit}}vs lag, showing the spike at the 10 ps stitch (grey dotted), the known signature of slow-mode undersampling in the short trajectory.(b)Stitched power spectral densities (arbitrary units). The stitch is set atf=1f=1cm-1, below the long trajectory’s Nyquist frequency (1.671.67cm-1, determined by its1010ps sampling). The visible jump at the stitch is due to aliasing: power from frequencies above the Nyquist frequency folds back into the[0,1.67][0,\,1.67]cm-1band, artificially inflating the long-trajectory PSD.

Autocorrelation functions (ACFs) for each tryptophan siteCm​(t)=⟨δ​ϵm​(0)​δ​ϵm​(t)⟩/σm2C_{m}(t)=\langle\delta\epsilon_{m}(0)\delta\epsilon_{m}(t)\rangle/\sigma_{m}^{2}are computed independently on both trajectories andstitchedat lag timet=10t=10ps (the long trajectory’s first lag): the short ACF fort<10t<10ps, the long ACF fort≥10t\geq 10ps. The power spectral densities (PSDs) are stitched analogously atf=1f=1cm-1. Because each ACF is self-normalised, the per-trajectory variance mismatch is absorbed into the normalisation; absolute variance re-enters downstream computations viaσm\sigma_{m}.

The stitched ACFs are decisively described by atri-exponentialdecay,Cm​(t)=∑k=13fk​e−t/Tk,∑k=13fk=1,C_{m}(t)=\sum_{k=1}^{3}f_{k}\,e^{-t/T_{k}},\qquad\textstyle\sum_{k=1}^{3}f_{k}=1,(11)

rather than a bi-exponential one. We select between the two with the Akaike information criterion[30]AIC=n​ln⁡(RSS/n)+2​k\mathrm{AIC}=n\ln(\mathrm{RSS}/n)+2k(nn: number of data points; RSS: residual sum of squares;kk: number of free parameters), whose2​k2kterm penalises free parameters so that a model cannot win merely by overfitting. On the stitched ACF the tri-exponential lowers the AIC byΔ​AIC=−331\Delta\mathrm{AIC}=-331relative to the bi-exponential, giving decisive evidence, since|Δ​AIC|>10|\Delta\mathrm{AIC}|>10is conventionally regarded as strong support for the lower-AIC model. This comparison fixes only the model structure (three components rather than two); the parameter values themselves are extracted below with explicit treatment of the 10 ps stitch artefact, which would otherwise bias the slow timescale.

The stitched ACF is not smooth at the 10 ps crossover: the short trajectory underestimates the nanosecond-mode variance (σlong2/σshort2≈1.2\sigma^{2}_{\mathrm{long}}/\sigma^{2}_{\mathrm{short}}\approx 1.2, Table2), so its self-normalised ACF sits below the long-trajectory ACF at the stitch. Directly fitting a tri-exponential across this discontinuity yields a high globalR2=0.988R^{2}=0.988but systematically underestimatesT3T_{3}, because the optimiser bends the slow decay faster to absorb the upward jump at 10 ps; the resultingT3≈1.1T_{3}\approx 1.1ns is less than half the unbiased value of2.662.66ns. The fit residual is localised at the stitch, where it reaches0.040.04–0.070.07per site (2–4×\timesthe typical residual of∼0.02{\sim}0.02elsewhere; Fig.3(a), inset). We therefore adopt a two-step procedure: (i) readT3T_{3}from the long trajectory alone, which resolves the nanosecond mode, and (ii) refit the two fast components on the stitched ACF withT3T_{3}anchored to this value. The globalR2R^{2}remains0.9870.987(Δ​R2=−0.001\Delta R^{2}=-0.001), confirming that the correction removes theT3T_{3}bias without degrading the overall fit. The residual at 10 ps is thus the known signature of slow-mode undersampling in the short trajectory, not a failure of the tri-exponential model itself. Fig.3(a) shows the corrected tri-exponential fits for all eight Trps, and Table2reports the fitted parameters.

The physics picture underlying the three timescalesT1T_{1},T2T_{2},T3T_{3}is well understood from the literature (e.g. Ref.[31]).
- •

T1∼46T_{1}\sim 46fs (f1=0.51f_{1}=0.51): sub-100-fs librational motions of water molecules strongly coupled to the protein surface.
- •

T2∼1.77T_{2}\sim 1.77ps (f2=0.33f_{2}=0.33): water reorientation and hydrogen-bond reformation.
- •

T3∼2.66T_{3}\sim 2.66ns (f3=0.16f_{3}=0.16): nanosecond protein conformational dynamics and tumbling; slow and site-dependent, reflecting heterogeneous local environments.

Heref1f_{1},f2f_{2},f3f_{3}indicate each mode’s fractional contribution to the total fluctuation varianceσm2\sigma_{m}^{2}. We see that the two fast modes dominate the variance (84%), while the slow mode contributes only 16%.
These timescales will be further validated by the source decomposition analysis below.

## III.3Source decomposition and dielectric screening

To decompose the site-energy fluctuation by environmental source, we first verify that the difference dipole𝝁m\bm{\mu}_{m}is effectively static on the exciton timescale.
Its autocorrelationC𝝁​(τ)=⟨𝝁m​(t)⋅𝝁m​(t+τ)⟩tC_{\bm{\mu}}(\tau)=\langle\bm{\mu}_{m}(t)\cdot\bm{\mu}_{m}(t+\tau)\rangle_{t}remains0.9840.984after a 2 ps lag on the short trajectory (site-averaged; per-site ranges0.980.98–0.990.99).
Consistently, freezing𝝁m\bm{\mu}_{m}to its time-average𝝁¯m\bar{\bm{\mu}}_{m}and recomputingδ​ϵm\delta\epsilon_{m}leaves the site-averaged standard deviation unchanged (σfixed/σ=1.00\sigma_{\mathrm{fixed}}/\sigma=1.00, specifically0.9980.998on the long trajectory and1.0031.003on the short). The fluctuation is therefore carried by the field𝑬m​(t)\bm{E}_{m}(t)alone, and we hold𝝁m=𝝁¯m\bm{\mu}_{m}=\bar{\bm{\mu}}_{m}fixed in the following analysis.

With𝝁m\bm{\mu}_{m}fixed,δ​ϵm​(t)=−𝝁¯m⋅𝑬m​(t)\delta\epsilon_{m}(t)=-\bar{\bm{\mu}}_{m}\cdot\bm{E}_{m}(t)is linear in the field. The Coulomb field decomposes exactly by source group,𝑬m=∑g𝑬g,m\bm{E}_{m}=\sum_{g}\bm{E}_{g,m}(g∈{g\in\{protein, water, nucleotide, ions}\}), so the site energy inherits the same decomposition,δ​ϵm=∑gδ​ϵg,m\delta\epsilon_{m}=\sum_{g}\delta\epsilon_{g,m}. Fig.4(a) shows the decomposedσm\sigma_{m}, and Fig.4(b) shows the decomposed PSDs. Two findings stand out:Figure 4:Source decomposition and dielectric screening.(a)Per-source standard deviationσg,m\sigma_{g,m}(bars) with the measured totalσm\sigma_{m}(black marker) and the uncorrelated expectation∑gσg,m2\sqrt{\sum_{g}\sigma_{g,m}^{2}}(open circles); the gap between the two markers is the cross-source cancellation.(b)Source-resolved PSD, averaged over the eight sites, with the measured total (black) and the direct source sum (grey dashed). Water dominates every frequency band, protein is second, and nucleotide is negligible. The direct sum overestimates the total by a factor of two due to cross-source cancellation.

## Water dominates every frequency band.

Water is the largest fluctuation source across all bands, contributing 52–65% of the spectral power in each (54% in the slow band). Protein is consistently second (27–39%), while nucleotide is negligible everywhere (<1.3%<1.3\%). Ions contribute∼\sim18% only in the slow band and vanish at sub-ps frequencies.

## Dielectric screening.

The component spectra sum totwicethe measured total (∫∑gSg​d​f/∫Stot​𝑑f=2.0\int\sum_{g}S_{g}\,df\,/\,\int S_{\mathrm{tot}}\,df=2.0). Equivalently, the screening ratioRscreen=1−σm2/∑gσg,m2R_{\mathrm{screen}}=1-\sigma_{m}^{2}/\sum_{g}\sigma_{g,m}^{2}averages0.660.66, meaning cross-source terms cancel two-thirds of the naive variance sum. The dominant cancellation is protein–water, whose fluctuations are anti-correlated (Pearsonr=−0.39r=-0.39) because polarised water partially cancels the protein field at the indole rings. Any noise model that treats sources as independent therefore overestimatesσ\sigmaby∼2\sim\sqrt{2}.

Fitting the tri-exponential to each source’s own ACF independently confirms the timescale assignment of Sec.III.2. Water recovers the two fast modes (T1≈54T_{1}\approx 54fs,T2≈1.1T_{2}\approx 1.1ps), while protein recovers the nanosecond mode (T3≈2.5T_{3}\approx 2.5ns). The fast modes are thus water-driven and the slowest mode protein-driven; the temporal and source decompositions independently converge on the same physical picture.

## III.4Exciton dynamics under coloured noise

We now apply the CNM and HSM of Sec.II.3to the tryptophan network, using the Hamiltonian from Ref.[11]reproduced in Table3.Table 3:Exciton Hamiltonian (cm-1) of the eight Trp sites in the tubulin dimer, copied from Ref.[11]. Diagonal entries are site-energy offsets relative to a base of3588835888cm-1; off-diagonal entries are excitonic couplingsJm​nJ_{mn}.12345678Trp1110−13-130−2-2−1-155−1-1Trp20388388−41-41441111−4-411Trp3−13-13−41-4134234222011−6-611Trp404422207207−4-466−59-59−1-1Trp5−2-2110−4-457572121221111Trp6−1-1111166212110210255−51-51Trp755−4-4−6-6−59-59225524824833Trp8−1-11111−1-11111−51-51330

First, we focus on an isolated pair Trp4–Trp7, which has the strongest coupling|J|=59|J|=59cm-1and a site-energy offsetΔ​ϵ=41\Delta\epsilon=41cm-1. Each site carries its three-component OU bath (Table2). For each ofNMC=500N_{\mathrm{MC}}=500realisations the HamiltonianH​(t)=[ϵ4+δ​ϵ4​(t)JJϵ7+δ​ϵ7​(t)]H(t)=\begin{bmatrix}\epsilon_{4}+\delta\epsilon_{4}(t)&J\\[4.0pt]
J&\epsilon_{7}+\delta\epsilon_{7}(t)\end{bmatrix}(12)

is propagated unitarily with time stepΔ​t=2\Delta t=2fs for an observation timeTobs=4T_{\mathrm{obs}}=4ps in total. The observables are then ensemble-averaged. This computation is exact for classical Gaussian noise. The two sites are treated as independent, justified by the negligible spatial correlations (AppendixA). Since the triple OU processes give us plenty of room to tweak, a noise-ablation simulation is conducted, as shown in Fig.5.

As can be seen from Fig.5(a), with only the slow componentT3T_{3}(σ3=227​cm−1\sigma_{3}=227~\mathrm{cm}^{-1}on Trp4,205​cm−1205~\mathrm{cm}^{-1}on Trp7), the exciton remains partially localised on Trp4 (P4≈0.83P_{4}\approx 0.83at 4 ps).
SinceT3T_{3}far exceeds the observation window, the system is under strong static disorder, resulting in Anderson localisation[32]. However, after adding the much fasterT1T_{1}and/orT2T_{2}modes, the localisation is broken and the population on Trp7 rises to∼0.50\sim 0.50at 4 ps. This is a clear demonstration of ENAQT[33,34,35], where moderate dynamic noise counteracts Anderson localisation to enhance transport. The phenomenon has recently been directly observed in experiments on perovskite nanocrystal superlattices, where exciton transport is maximised at intermediate dephasing strength[8]. In our system, the fast noise drives the detuning across resonance repeatedly, opening transfer windows for the exciton to hop from Trp4 to Trp7. In addition, the individual MC realisations (Fig.5(b), grey) show coherent oscillations which are averaged out by the ensemble averaging. This is a signature of inhomogeneous dephasing.

To further investigate the ENAQT effect, we first apply theT3T_{3}mode noise to Trp4 and Trp7 to place the two-site system in the strong static-disorder regime, then scan over the correlation timeTOUT_{\mathrm{OU}}or amplitudeσOU\sigma_{\mathrm{OU}}of an additional OU process (fixing one and varying the other). ENAQT is considered effective whenP7P_{7}exceeds 0.3 at 4 ps. Fig.5(c) shows that, at fixed amplitudeσOU=300​cm−1\sigma_{\mathrm{OU}}=300~\mathrm{cm}^{-1}, correlation times below∼7\sim 7ps enable ENAQT, with maximum transfer nearTOU≲1T_{\mathrm{OU}}\lesssim 1ps. Both theT1T_{1}andT2T_{2}modes characterised in Sec.III.2fall within this regime. Fig.5(d) shows the complementary scan over amplitude at fixedTOU=50T_{\mathrm{OU}}=50fs. The ENAQT regime spansσOU≈36\sigma_{\mathrm{OU}}\approx 36–9700​cm−19700~\mathrm{cm}^{-1}, with a broad peak nearσOU∼200\sigma_{\mathrm{OU}}\sim 200–1000​cm−11000~\mathrm{cm}^{-1}. Weaker noise (σOU≲36\sigma_{\mathrm{OU}}\lesssim 36cm-1) cannot overcome theT3T_{3}static disorder (σ3∼200\sigma_{3}\sim 200cm-1per site) to bring the detuning across resonance, while excessively stronger noise (σOU≫J\sigma_{\mathrm{OU}}\gg J) creates large quasi-static detunings (Kubo numberκ=σ​T/ℏ≈90\kappa=\sigma T/\hbar\approx 90at the upper boundary;κ≫1\kappa\gg 1marks the non-Markovian regime where the bath acts quasi-statically and the white-noise approximation fails), so the system rarely visits resonance.Figure 5:Inhomogeneous dephasing and ENAQT on the Trp4–Trp7 two-site system (J=−59​cm−1J=-59~\mathrm{cm}^{-1}).
The excitation is initialised on Trp4 in all panels. Each site carries its own bath of three additive Ornstein–Uhlenbeck processes fitted to the per-site MD fluctuations (Table2).
Dynamics are computed by MC sampling of the stochastic Schrödinger equation withNMC=500N_{\mathrm{MC}}=500realisations.(a) Noise ablation:populationP7​(t)P_{7}(t)on Trp7 under various noise configurations. The noiseless case (grey dotted) gives coherent Rabi oscillations. The slowest modeT3T_{3}alone partially localises the excitation (P7​(4​ps)=0.17P_{7}(4~\mathrm{ps})=0.17, green). Adding the fast modeT1T_{1}breaks the localisation and enables transport (T1T_{1}alone:P7=0.50P_{7}=0.50;T1+T3T_{1}{+}T_{3}:P7=0.50P_{7}=0.50; full model:P7=0.50P_{7}=0.50, black), demonstrating ENAQT. For solver validation, the HSM solution atγ=50​cm−1\gamma=50~\mathrm{cm}^{-1}(blue dashed) is compared with a white-noise MC trajectory (σOU=163​cm−1\sigma_{\mathrm{OU}}=163~\mathrm{cm}^{-1},TOU=5T_{\mathrm{OU}}=5fs, tuned so that2​σ2​T=γ2\sigma^{2}T=\gamma; blue solid).(b) Individual trajectories:five MC realisations under the full bath (grey) together with theNMC=500N_{\mathrm{MC}}=500ensemble average (black). Individual trajectories oscillate coherently, whereas the ensemble average dephases smoothly. This is the signature of inhomogeneous dephasing, where coherence is lost by phase dispersion across realisations rather than by within-trajectory dissipation.(c) ENAQT scan over correlation time:P7​(4​ps)P_{7}(4~\mathrm{ps})vs.TOUT_{\mathrm{OU}}, withT3T_{3}always present at full MD strength and an additional OU process of fixed amplitudeσOU=300​cm−1\sigma_{\mathrm{OU}}=300~\mathrm{cm}^{-1}scanned over its correlation time. Defining the ENAQT regime asP7>0.3P_{7}>0.3(dotted line), transport is assisted for allTOU≲7T_{\mathrm{OU}}\lesssim 7ps and is optimal nearℏ/J≈90\hbar/J\approx 90fs. The MDT1T_{1}mode (∼\sim35–41 fs, red markers) sits in the optimal regime;T2T_{2}(∼\sim0.4–1.0 ps at most sites, blue) lies well within.(d) ENAQT scan over noise amplitude:as in (c) but withTOU=50T_{\mathrm{OU}}=50fs fixed andσOU\sigma_{\mathrm{OU}}scanned. The ENAQT window (P7>0.3P_{7}>0.3) spansσOU≈36\sigma_{\mathrm{OU}}\approx 36–9700​cm−19700~\mathrm{cm}^{-1}, with a broad peak nearσOU∼200\sigma_{\mathrm{OU}}\sim 200–1000​cm−11000~\mathrm{cm}^{-1}(P7≈0.51P_{7}\approx 0.51). Weaker noise cannot overcome theT3T_{3}static disorder (σ3∼200\sigma_{3}\sim 200cm-1) to reach resonance; excessively strong noise (σOU≫J\sigma_{\mathrm{OU}}\gg J, Kubo numberκ≫1\kappa\gg 1) creates large quasi-static detunings that keep the system far from resonance.

An OU process reaches the Haken–Strobl white-noise limit when its correlation time tends to zero with the productσ2​T\sigma^{2}Theld fixed, so the same Monte Carlo code, run in this limit, must reproduce the analytic HSM solution. We exploit this to validate the solver: a single symmetric OU process per site withT=5T=5fs andσ≈163\sigma\approx 163cm-1, tuned so that2​σ2​T=γ=502\sigma^{2}T=\gamma=50cm-1(1/γ=1061/\gamma=106fs; the factor of 2 accounts for both sites dephasing the coherence symmetrically), is propagated as a white-noise MC and overlaid in Fig.5(a) alongside the analytic HSM transient for comparison. The MC reproduces the HSM transient (P7​(4​ps)=0.47±0.01P_{7}(4~\mathrm{ps})=0.47\pm 0.01versus the HSM value of0.500.50), confirming the solver. The matching pair(σ,T)=(163​cm−1,5​fs)(\sigma,T)=(163~\mathrm{cm}^{-1},5~\mathrm{fs})is not a physical bath but simply the OU representation of the phenomenological rateγ=50\gamma=50cm-1. For comparison, the CNM’s fast mode alone (σ1≈650\sigma_{1}\approx 650cm-1,T1≈46T_{1}\approx 46fs) would correspond to a Markovian dephasing rate∼102​γ\sim\!10^{2}\gammaif it were white noise, yet the coloured bath produces comparable transfer because its spectral power is distributed away from the system frequency by the large Kubo numberκ1≈6\kappa_{1}\approx 6.

Although the two-site system clearly illustrates the ENAQT mechanism, it cannot distinguish the coloured-noise model from white-noise dephasing. The endpoint carries no discriminating information, because any two-level system with pure dephasing approaches an equal-population limit of1/21/2at long times regardless of the underlying mechanism or transient shape. We therefore turn to the full eight-site network, which provides a more discriminating test: its steady-state population distribution directly reveals the difference between delocalising white-noise dephasing and confinement by quasi-static disorder.

Fig.6shows the population dynamics under the HSM (dashed) and the CNM (solid) for initial excitation on each of the eight Trp sites. In every panel the CNM retains more population on the starting site and its strongest-coupled partner than the HSM. Starting from Trp4, for instance, the CNM givesP4​(3​ps)=0.46P_{4}(3~\mathrm{ps})=0.46,P7​(3​ps)=0.44P_{7}(3~\mathrm{ps})=0.44, and onlyPleak=0.10P_{\mathrm{leak}}=0.10escapes the pair. The HSM, by contrast, spreads population across the full network (Pleak=0.50P_{\mathrm{leak}}=0.50), approaching the long-time uniform limit of1/81/8per site.

This qualitative difference is expected because the MD-derived bath violates the assumptions of the HSM on every count: (i) the bath is slow, with even the fastest correlation timeT1≈46T_{1}\approx 46fs comparable to the coherent timescaleℏ/Jmax≈90\hbar/J_{\max}\approx 90fs (andT2T_{2},T3T_{3}exceeding it by 1–4 orders of magnitude); and (ii) the coupling is strong, withσ/J≈11\sigma/J\approx 11–2525at every site. Crucially, all three modes are deep in the non-Markovian regime (κ1∼6\kappa_{1}\sim 6,κ2∼102\kappa_{2}\sim 10^{2},κ3∼105\kappa_{3}\sim 10^{5}, all≫1\gg 1). The HSM dephasing rateγ=50\gamma=50cm-1is therefore not anab initioprediction of the bath but a phenomenological fit, and exciton transport on the tryptophan network proceeds via ENAQT under a bath that lies outside the HSM’s validity.Figure 6:Exciton dynamics on the full eight-site Trp network[11], for initial excitation on each of the eight sites (3 ps evolution,NMC=500N_{\mathrm{MC}}=500). In every panel, solid lines show the CNM and dashed lines the HSM atγ=50\gamma=50cm-1; colours distinguish the eight Trp sites. The CNM consistently retains more population on the starting site and its strongest-coupled partner (e.g. Trp4↔\leftrightarrowTrp7), whereas the HSM spreads population across the full network.

Collectively, this section establishes a multi-scale picture of tryptophan site-energy disorder in a tubulin dimer system, drawn from all-atom molecular dynamics at 310 K in explicit solvent. The site-energy fluctuations follow a tri-exponential autocorrelation spanning solvent librational (T1≈46T_{1}\approx 46fs), water reorientation (T2≈1.77T_{2}\approx 1.77ps), and protein conformational (T3≈2.66T_{3}\approx 2.66ns) timescales, with water dominating the spectral power and substantial protein–water dielectric screening (Rscreen≈0.66R_{\mathrm{screen}}\approx 0.66). The observed ENAQT emerges from the competition between these bath components: the quasi-staticT3T_{3}disorder localises excitons through inhomogeneous dephasing and Anderson localisation, while the fasterT1T_{1}andT2T_{2}modes dynamically modulate the site detuning and repeatedly drive the system through resonance, opening transient transfer windows. Transport peaks at an intermediate fast-noise strength that matches the MD-derivedT1T_{1}andT2T_{2}timescales, and falls off when the noise is too weak to overcome the static localisation or so strong that it reintroduces quasi-static detunings. With all three components deep in the non-Markovian regime (κk≫1\kappa_{k}\gg 1), the full eight-site network confirms the picture: the CNM confines excitons to strongly coupled site pairs, whereas the Markovian HSM delocalises them across the entire network.

## IVDiscussion

## The bath is non-Markovian.

This work fundamentally revisits the theoretical treatment of tryptophan exciton dynamics in tubulin, which has relied on the Haken–Strobl white-noise approximation, e.g.,[11,16]. Our dual-time-resolution MD of the solvated tubulin dimer at 310 K delivers a microscopically derived coloured-noise bath, demonstrating that every relaxation mode resides deep in the non-Markovian regime (Kubo numberκk≫1\kappa_{k}\gg 1), where white-noise and perturbative approximations fail qualitatively[7]. On the full network, the HSM tends to overestimate delocalisation, spreading population broadly, while the coloured bath confines 90% of the excitation within spatially proximal pairs.

## The noise can be a friend.

The MD-derived noise model exhibits a tri-exponential autocorrelation, revealing three physically distinct modes: (i) sub-100-fs water librations, (ii) picosecond water reorientation and hydrogen-bond rearrangements, and (iii) nanosecond protein conformational motions. At 310 K, the slowest mode imposes strong static disorder on the tryptophan network, resulting in Anderson localisation[32], while the two fast modes dynamically drive chromophore pairs through resonance, enabling ENAQT[33,34,35]and facilitating exciton hopping between proximal tryptophan pairs. This illustrates that environmental fluctuations are not inherently detrimental to exciton transport but can, under appropriate conditions of amplitude and timescale, actively facilitate energy transfer. The competition between static disorder and ENAQT observed here is consistent with prior theoretical and experimental results. For example, Ref.[7]showed that an optimal noise correlation time maximises exciton transport efficiency in FMO systems. Ref.[8]showed experimentally that the mean squared displacement of excitons in perovskite nanocrystal superlattices is non-monotonous in temperature, peaking at a sample-dependent turnover temperature where static disorder and dephasing are balanced. These results collectively indicate that coherence, static disorder, and thermal fluctuations interact intricately to govern exciton transport, opening new possibilities for controlling exciton dynamics in biological and synthetic systems.

## Dielectric screening.

Dielectric screening acquires a clear microscopic interpretation within our all-atom framework. By decomposing the electric field at each tryptophan into contributions from protein, water, nucleotide, and ions, we reveal strong anticorrelation between the protein and water components (Pearsonr=−0.39r=-0.39), which cancels two-thirds of the naive variance sum (Rscreen≈0.66R_{\mathrm{screen}}\approx 0.66) and reduces the total disorder amplitude by a factor of∼2\sim\sqrt{2}relative to independent-source estimates. Any noise model that treats these sources as independent therefore overestimates the effective disorder. Crucially, this dynamic anticorrelation arises from the same protein–water polarisation response that gives tubulin its unusually high optical dielectric constantεopt=8.41\varepsilon_{\mathrm{opt}}=8.41[36], a value adopted in prior tubulin exciton calculations[11]through the local-field framework[37]. Our atomistic decomposition thus reveals that the static local-field enhancement of inter-chromophore couplings and the dynamic suppression of site-energy fluctuations are two manifestations of the same polarisation mechanism, unifying the equilibrium and fluctuational descriptions of the dielectric environment.

## Exciton localisation and fluorescence.

In the noise-free Hamiltonian (Table3) of the tryptophan network in tubulin, the intrinsic site-energy spread (388 cm-1) already limits the maximum participation ratio of the eight tryptophan sites to 2.07, and a disorder-strength scan shows that the MD-derived quasi-static component (σ3≈200\sigma_{3}\approx 200cm-1) further reduces it to∼\sim1.4 (see AppendixF). Such strong localisation precludes collective radiative enhancement in the isolated dimer. This is consistent with the measurements of Ref.[18], who reported fluorescence quantum yields of 12.4% for free tryptophan, 10.6% for the tubulin dimer, and 17.6% for assembled microtubules, and attributed the depressed dimer yield to non-radiative protein-environment channels. Our analysis identifies disorder-induced localisation as a complementary, independent mechanism. Upon microtubule assembly, collective inter-dimer coupling broadens the exciton band and may overcome this quasi-static disorder, plausibly explaining the elevated microtubule yield.

## Limitations and outlook.

Several simplifications frame the scope of this work. First, the fluctuation autocorrelation is obtained by stitching a short high-resolution trajectory with a long low-resolution one; the discontinuity at the stitch introduces some fitting uncertainty in the tri-exponential parameters. Second, the excitonic couplingsJm​nJ_{mn}, taken from Ref.[11], are based on the point-dipole approximation with a uniform empirical optical dielectric constant. Third, the difference dipole magnitude is fixed atμ=5\mu=5D, whereas the indoleLa1{}^{1}L_{a}value ranges from 4.82 to 8 D[24]. Nevertheless, this choice does not undermine our core physical conclusions: becauseδ​ϵm∝μ\delta\epsilon_{m}\propto\mu, the disorder amplitudesσm\sigma_{m}and Kubo numbersκk\kappa_{k}all scale linearly withμ\mu, so the dimensionless ratios governing the physics rescale by the single factorμ/(5​D)\mu/(5~\mathrm{D}). Even at the lower bound (μ=4.82\mu=4.82D), every site remains deep in the strong-disorder regime (σ/J≥11≫1\sigma/J\geq 11\gg 1, Table2), and increasingμ\muonly strengthens the Anderson localisation. Looking forward, the full pipeline generalises to other pigment–protein systems, including photosynthetic light-harvesting complexes (LHC) and FMO complexes, and future refinements such as polarisable force fields, extension to the microtubule lattice, and dynamic coupling fluctuations will further improve the atomistic accuracy of the model.

## VConclusions

This work establishes a microscopic coloured-noise model for tryptophan excitons in tubulin by deriving all bath statistics directly from dual-time-resolution all-atom molecular dynamics at 310 K. Our atomistic simulation resolves site-energy fluctuations across four orders of magnitude in time, from sub-100-fs solvent libration to nanosecond protein conformational dynamics, and decomposes them into three well-separated relaxation modes that all reside deep in the non-Markovian regime (κk≫1\kappa_{k}\gg 1). This replaces the phenomenological dephasing rate of the Haken–Strobl white-noise model with a microscopic, multi-timescale bath derived entirely from protein and solvent dynamics.

The central physical message is that environmental noise is not inherently detrimental to exciton transport but can actively facilitate it. The slowest mode (T3T_{3}) imposes strong quasi-static disorder and Anderson localisation, while the two fast modes (T1T_{1},T2T_{2}) repeatedly drive chromophore pairs through resonance, enabling ENAQT. On the full eight-site network, this competition confines excitons within strongly coupled tryptophan pairs, in marked contrast to the uniform delocalisation predicted by the Haken–Strobl model. Protein–water dielectric screening further suppresses the effective disorder by a factor of∼2\sim\sqrt{2}, providing a microscopic origin for the optical dielectric constant adopted in prior static calculations.

These findings move chromophore-disorder modelling beyond phenomenological dephasing toward fully atomistic, multi-timescale environmental baths. The workflow generalises to any pigment–protein complex with water-interfaced chromophores, offering a route to quantify non-Markovian disorder in biological excitonic systems.

## Acknowledgements.All research design, molecular dynamics simulations, data analysis, and manuscript preparation were completed independently by the author. This work builds on the theoretical training obtained during the author’s M.Sc. studies in Physics at the National University of Singapore. CUDA-accelerated GROMACS simulations were performed on rented GPU computational resources from AI Galaxy (https://ai-galaxy.cn). The GLM 5.1 large language model was used to accelerate the preparation of GROMACS input parameter configurations and preliminary data analysis scripts; all generated outputs were manually inspected, verified, and revised by the author to guarantee physical consistency and numerical accuracy. All analysis codes are publicly available on GitHub athttps://github.com/Varato/tubulin-bath-fluctuation; the raw molecular dynamics trajectories (∼\sim100 GB) are available from the author upon reasonable request. The author expresses sincere gratitude to family members for their persistent support and encouragement throughout this study.

## References
- Engelet al.[2007]G. S. Engel, T. R. Calhoun,
E. L. Read, T.-K. Ahn, T. Mančal, Y.-C. Cheng, R. E. Blankenship, and G. R. Fleming,Nature446, 782 (2007).
- Panitchayangkoonet al.[2010]G. Panitchayangkoon, D. Hayes, K. A. Fransted,
J. R. Caram, E. Harel, J. Wen, R. E. Blankenship, and G. S. Engel,Proceedings of the National Academy of Sciences107, 12766 (2010).
- Colliniet al.[2010]E. Collini, C. Y. Wong,
K. E. Wilk, P. M. G. Curmi, P. Brumer, and G. D. Scholes,Nature463, 644 (2010).
- Wellset al.[2014]K. L. Wells, P. H. Lambrev,
Z. Zhang, G. Garab, and H.-S. Tan,Physical Chemistry Chemical Physics16, 11640 (2014), _eprint:
https://pubs.rsc.org/cp/article-pdf/16/23/11640/3521124/c4cp00876f.pdf.
- Zhuet al.[2024]R. Zhu, W. Li, Z. Zhen, J. Zou, G. Liao, J. Wang, Z. Wang, H. Chen, S. Qin, and Y. Weng,Nature Communications15, 3171 (2024).
- Mohseniet al.[2008]M. Mohseni, P. Rebentrost,
S. Lloyd, and A. Aspuru-Guzik,The Journal of Chemical Physics129, 174106 (2008).
- Chen and Silbey [2011]X. Chen and R. J. Silbey,The Journal of Physical Chemistry B115, 5499 (2011).
- Blachet al.[2025]D. D. Blach, V. A. Lumsargis-Roth, C. Chuang, D. E. Clark,
S. Deng, O. F. Williams, C. W. Li, J. Cao, and L. Huang,Nature Communications16, 1270 (2025).
- Tegmark [2000]M. Tegmark,Physical Review E61, 4194 (2000).
- Haganet al.[2002]S. Hagan, S. R. Hameroff, and J. A. Tuszyński,Physical Review E65, 061901 (2002).
- Craddocket al.[2014]T. J. A. Craddock, D. Friesen, J. Mane,
S. Hameroff, and J. A. Tuszynski,Journal of The Royal Society Interface11, 20140677 (2014).
- Caycedo-Soleret al.[2022]F. Caycedo-Soler, A. Mattioni, J. Lim,
T. Renger, S. F. Huelga, and M. B. Plenio,Nature Communications13, 2912 (2022).
- Mujica-Martinezet al.[2013]C. A. Mujica-Martinez, P. Nalbach, and M. Thorwart,Physical Review E88, 062719 (2013).
- Liguoriet al.[2015]N. Liguori, X. Periole,
S. J. Marrink, and R. Croce,Scientific Reports5, 15661 (2015).
- Celardoet al.[2019]G. L. Celardo, M. Angeli,
T. J. A. Craddock, and P. Kurian,New Journal of Physics21, 023005 (2019).
- Gassabet al.[2026]L. Gassab, O. Pusuluk, and T. J. A. Craddock,Entropy28, 204 (2026).
- Kalraet al.[2023]A. P. Kalra, A. Benny,
S. M. Travis, E. A. Zizzi, A. Morales-Sanchez, D. G. Oblinsky, T. J. A. Craddock, S. R. Hameroff, M. B. MacIver, J. A. Tuszyński, S. Petry, R. Penrose, and G. D. Scholes,ACS Central Science9, 352 (2023).
- Babcocket al.[2024]N. S. Babcock, G. Montes-Cabrera, K. E. Oberhofer, M. Chergui,
G. L. Celardo, and P. Kurian,The Journal of Physical Chemistry B128, 4035 (2024).
- Abrahamet al.[2026]M. J. Abraham, B. Hess, and E. Lindahl,GROMACS 2026(2026), zenodo.
- Loweet al.[2001]J. Lowe, H. Li, K. Downing, and E. Nogales,Refined structure of
alpha-beta tubulin from zinc-induced sheets stabilized with taxol: 1jff(2001), institution: Worldwide Protein
Data Bank.
- Jurruset al.[2018]E. Jurrus, D. Engel,
K. Star, K. Monson, J. Brandi, L. E. Felberg, D. H. Brookes, L. Wilson, J. Chen,
K. Liles, M. Chun, P. Li, D. W. Gohara, T. Dolinsky, R. Konecny, D. R. Koes, J. E. Nielsen, T. Head-Gordon, W. Geng,
R. Krasny, G.-W. Wei, M. J. Holst, J. A. McCammon, and N. A. Baker,Protein Science27, 112
(2018).
- Lindorff‐Larsenet al.[2010]K. Lindorff‐Larsen, S. Piana, K. Palmo,
P. Maragakis, J. L. Klepeis, R. O. Dror, and D. E. Shaw,Proteins: Structure, Function, and Bioinformatics78, 1950 (2010).
- Meagheret al.[2003]K. L. Meagher, L. T. Redman, and H. A. Carlson,Journal of Computational Chemistry24, 1016 (2003).
- Vivian and Callis [2001]J. T. Vivian and P. R. Callis,Biophysical Journal80, 2093 (2001).
- Kubo [1963]R. Kubo,Journal of Mathematical Physics4, 174 (1963).
- Gillespie [1996]D. T. Gillespie,Physical Review E54, 2084 (1996).
- Rips [1993]I. Rips,Physical Review E47, 67 (1993).
- Chen and Silbey [2010]X. Chen and R. J. Silbey,The Journal of Chemical Physics132, 204503 (2010).
- Lambertet al.[2026]N. Lambert, E. Gigu‘ere,
P. Menczel, B. Li, P. Hopf, G. Su’arez, M. Gali, J. Lishman, R. Gadhvi,
R. Agarwal, A. Galicia, N. Shammah, P. Nation, J. R. Johansson, S. Ahmed, S. Cross,
A. Pitchford, and F. Nori,Physics Reports1153, 1 (2026).
- Akaike [1974]H. Akaike,IEEE Transactions on Automatic Control19, 716 (1974).
- Laageet al.[2017]D. Laage, T. Elsaesser, and J. T. Hynes,Structural Dynamics4, 044018 (2017).
- Anderson [1958]P. W. Anderson,Physical Review109, 1492 (1958).
- Maieret al.[2019]C. Maier, T. Brydges,
P. Jurcevic, N. Trautmann, C. Hempel, B. P. Lanyon, P. Hauke, R. Blatt, and C. F. Roos,Phys. Rev. Lett.122, 050501 (2019).
- Moixet al.[2013]J. M. Moix, M. Khasin, and J. Cao,New Journal of Physics15, 085010 (2013).
- Rebentrostet al.[2009]P. Rebentrost, M. Mohseni,
I. Kassal, S. Lloyd, and A. Aspuru-Guzik,New Journal of Physics11, 033003 (2009).
- Mershinet al.[2004]A. Mershin, A. Kolomenski,
H. Schuessler, and D. Nanopoulos,Biosystems77, 73 (2004).
- Juzeliūnas and Andrews [1994]G. Juzeliūnas and D. L. Andrews,Physical Review B49, 8751 (1994).

Appendix

## Appendix ASpatial correlations of site-energy fluctuationsFigure A1:8×88\times 8Pearson correlation matrix of the site-energy fluctuations (long trajectory). Mean off-diagonal|r|=0.019|r|=0.019. Black lines mark the chain boundary (Trp1–4:α\alpha-tubulin; Trp5–8:β\beta-tubulin).

FigureA1shows the8×88\times 8Pearson correlation matrix of the site-energy fluctuations over the long trajectory. All off-diagonal entries are small (mean|r|=0.019|r|=0.019); the sites are statistically independent, justifying the diagonal covariance used in the exciton-dynamics treatment of Sec.III.4.

## Appendix BFluctuation tracesFigure A2:Two-nanosecond windows ofδ​ϵm​(t)\delta\epsilon_{m}(t)for each Trp. The short trajectory (colour, 10 fs cadence) is overlaid with the last 2 ns of the long trajectory (black, 10 ps cadence), both demeaned. The coarse long trace resolves the nanosecond envelope; the short trace resolves the sub-picosecond jitter invisible at 10 ps sampling.

FigureA2shows representative windows of the rawδ​ϵm​(t)\delta\epsilon_{m}(t)that underlie the statistics of Sec.III.1. The traces are visually consistent with stationary fluctuation about a fixed mean; the amplitude contrast between sites mirrors theσm\sigma_{m}spread of Table2.

## Appendix CDistribution and stationarity of the site-energy fluctuations

## Zero mean.

The quantity analysed throughout this work is the fluctuation about the time-averaged site energy,δ​ϵm​(t)=−𝝁m⋅𝑬m​(t)−⟨−𝝁m⋅𝑬m⟩T\delta\epsilon_{m}(t)=-\bm{\mu}_{m}\!\cdot\!\bm{E}_{m}(t)-\langle-\bm{\mu}_{m}\!\cdot\!\bm{E}_{m}\rangle_{T}.
The raw Stark shift carries a large, site-dependent static mean (the average electrostatic site energy, of order10210^{2}–10310^{3}cm-1); subtracting it makes the fluctuation exactly zero-mean,⟨δ​ϵm⟩T=0\langle\delta\epsilon_{m}\rangle_{T}=0, by construction. Its standard deviation therefore coincides with its root-mean-square, and we reportσm=std​(δ​ϵm)\sigma_{m}=\mathrm{std}(\delta\epsilon_{m})throughout.

## Gaussianity.

TableA1reports the skewnessγ\gammaand excess kurtosisκ\kappaofδ​ϵm\delta\epsilon_{m}on both trajectories. Both are small on each (|γ|≤0.30|\gamma|\leq 0.30long,≤0.32\leq 0.32short;|κ|≤1.1|\kappa|\leq 1.1long,≤0.7\leq 0.7short), so the marginal distribution is close to Gaussian. This justifies treating the autocorrelation as a complete second-order descriptor of the bath and, later, synthesising the bath by Gaussian Monte-Carlo sampling.Table A1:Skewnessγ\gammaand excess kurtosisκ\kappaof the zero-mean fluctuationδ​ϵm\delta\epsilon_{m}(a Gaussian hasγ=κ=0\gamma=\kappa=0), for both trajectories.skewnessγ\gammaexcess kurtosisκ\kappasitelongshortlongshortTrp1−0.15-0.15−0.05-0.05+0.24+0.24+0.06+0.06Trp2−0.30-0.30+0.32+0.32+0.78+0.78+0.48+0.48Trp3−0.29-0.29−0.32-0.32+0.54+0.54+0.68+0.68Trp4−0.13-0.13−0.26-0.26−0.04-0.04+0.12+0.12Trp5−0.03-0.03−0.10-0.10+0.29+0.29−0.13-0.13Trp6−0.02-0.02+0.03+0.03−0.07-0.07−0.11-0.11Trp7−0.08-0.08+0.11+0.11+1.07+1.07+0.62+0.62Trp8−0.11-0.11−0.20-0.20+0.05+0.05−0.07-0.07

## Stationarity.

Treating the autocorrelation as a function of lag only,Cm​(τ)C_{m}(\tau), and pooling the long trajectory into a single ensemble require that the analysis window (10–50 ns) sample a stationary distribution. We verify this by split-half comparison: the 40 ns window is divided into two 20 ns segments (10–30 ns and 30–50 ns) and the per-segment standard deviationσm\sigma_{m}compared site by site. The two halves agree to within 15% for all eight Trps, with no systematic drift; the largest off-diagonal spatial correlation is likewise stable (0.090 and 0.076 in the two halves versus 0.056 over the full window, the half-window values slightly larger as expected from smaller-sample fluctuations). The first 10 ns of the 50 ns production run, which showed residual equilibration drift, was excluded from all analyses (Sec.II.1). The site-energy fluctuations are stationary over the analysis window.

## Appendix DStructural descriptorsTable A2:Structural descriptors of the eight Trp sites. SASA: time-averaged whole-residue solvent-accessible surface area (Lee–Richards).θloc\theta_{\mathrm{loc}}: Procrustes-corrected local angular deviation of the difference dipole — the orientational analogue of RMSF, computed after removing the per-frame global rotationR​(t)R(t)(Wahba’s problem on the 8-vector dipole set) and averagingθm​(t)=arccos⁡(𝒏^mloc​(t)⋅⟨𝒏^mloc⟩)\theta_{m}(t)=\arccos(\hat{\bm{n}}_{m}^{\mathrm{loc}}(t)\cdot\langle\hat{\bm{n}}_{m}^{\mathrm{loc}}\rangle).dnucld_{\mathrm{nucl}}: distance to the nearest GTP/GDP. Hydration: mean count of water molecules within 3.5 Å of the indole ring.siteSASA (nm2)θloc\theta_{\mathrm{loc}}(deg)nearest nucl. (Å)hydrationTrp10.19412.914.2 (GTP)1.71Trp20.70315.029.2 (GTP)2.19Trp30.04612.714.5 (GTP)0.13Trp40.4888.312.2 (GTP)2.36Trp50.0298.613.8 (GDP)0.48Trp60.06610.010.1 (GDP)0.83Trp70.15710.019.7 (GTP)1.52Trp81.00331.99.9 (GDP)3.87

TableA2contextualises the site heterogeneity, and Fig.A3relates these structural descriptors to the fitted bath parameters. The amplitude structure is more regular than the timescales. The water-reorientation amplitudeσ2\sigma_{2}tracks SASA closely (Pearsonr=0.93r=0.93): more exposed indoles sense a larger fluctuating aqueous field, as expected. The libration amplitudeσ1\sigma_{1}follows the same trend more weakly (r=0.82r=0.82). The protein-conformational amplitudeσ3\sigma_{3}is instead non-monotonic (V-shaped): both deeply buried residues (Trp5, Trp3, Trp6) and the most exposed one (Trp8) carry large slow-mode variance, while semi-exposed sites (Trp7, Trp4) are minimal. Buried residues directly sense slow packing fluctuations of the surrounding protein; exposed residues sense slow loop and surface rearrangements; the intermediate-SASA sites sit in locally rigid pockets that suppress the nanosecond mode. Trp8 is the outlier on every axis: highestσ\sigma, largest SASA, highest mobility, closest to a nucleotide, most hydrated.

The relaxation timescalesTkT_{k}show no comparably clean structural trend (|r|<0.44|r|<0.44for allTkT_{k}–SASA pairs) and span wide ranges, especiallyT3T_{3}(0.45–8.5 ns, a factor of∼20{\sim}20). The site-by-site variation and its physical interpretation, including the poor separation ofT2T_{2}andT3T_{3}at Trp6 and the poorly constrainedT3T_{3}at Trp4, are discussed in Sec.E.

## Whyσshort\sigma_{\mathrm{short}}can exceedσ\sigma.

For most sites the long-trajectory standard deviation exceeds the short-trajectory one (σ>σshort\sigma>\sigma_{\mathrm{short}}, Table2), because the 2 ns short trajectory undersamples the nanosecond slow mode. The sign of the difference is governed by whetherT3T_{3}is resolved within the 2 ns window. The two most buried sites are exceptions: Trp5 (SASA=0.029=0.029nm2,T3=0.96T_{3}=0.96ns) and Trp6 (SASA=0.066=0.066nm2,T3=0.49T_{3}=0.49ns) have slow modes that relax well inside the 2 ns short trajectory (2​ns/T3≈22~\mathrm{ns}/T_{3}\approx 2and44, respectively), so there is no missing slow-mode variance to biasσshort\sigma_{\mathrm{short}}downward. The two estimates agree for Trp5 (σshort/σ=1.01\sigma_{\mathrm{short}}/\sigma=1.01) and the short slightly exceeds the long for Trp6 (σshort/σ=1.12\sigma_{\mathrm{short}}/\sigma=1.12), reflecting sampling variability of a slow mode sampled only a few times within the window. Trp8 (T3=1.36T_{3}=1.36ns,σshort/σ=1.04\sigma_{\mathrm{short}}/\sigma=1.04) follows the same logic. In contrast, sites withT3≫2T_{3}\gg 2ns, such as Trp3 (T3=6.8T_{3}=6.8ns,σshort/σ=0.79\sigma_{\mathrm{short}}/\sigma=0.79) and Trp4 (T3=8.5T_{3}=8.5ns,σshort/σ=0.86\sigma_{\mathrm{short}}/\sigma=0.86), show the expectedσ>σshort\sigma>\sigma_{\mathrm{short}}because the short trajectory captures only a fraction of a slow-mode period.

## Appendix ESite-to-site variation of relaxation timescalesFigure A3:Bath parameters vs. whole-residue SASA for each Trp site, coloured by the local dipole angular deviationθloc\theta_{\mathrm{loc}}(TableA2).(top)Relaxation timescalesTkT_{k}:T1T_{1}(solvent libration, 27–68 fs),T2T_{2}(water reorientation, 0.4–8.6 ps),T3T_{3}(protein conformational, 0.5–8.5 ns), showing no clean structural trend (|r|<0.44|r|<0.44).(bottom)Per-component amplitudesσk=σm​fk\sigma_{k}=\sigma_{m}\sqrt{f_{k}}:σ2\sigma_{2}correlates strongly with SASA (r=0.93r=0.93),σ1\sigma_{1}more weakly (r=0.82r=0.82), whileσ3\sigma_{3}is non-monotonic (V-shaped), with both deeply buried and highly exposed sites carrying large slow-mode variance.

FigureA3visualises the wide site-to-site variation in the three fitted timescales. The colour encodesθloc\theta_{\mathrm{loc}}, the local angular mobility of the Trp difference dipole. For each MD frame, the global protein rotationR​(t)R(t)is removed by solving Wahba’s problem (optimal rotation mapping the 8-vector dipole set to its time-averaged reference, via SVD). The corrected dipole directions𝒏^mloc​(t)\hat{\bm{n}}_{m}^{\mathrm{loc}}(t)are then compared to their own time average, giving the mean angular tiltθm=⟨arccos⁡(𝒏^mloc​(t)⋅⟨𝒏^mloc⟩)⟩\theta_{m}=\langle\arccos(\hat{\bm{n}}_{m}^{\mathrm{loc}}(t)\cdot\langle\hat{\bm{n}}_{m}^{\mathrm{loc}}\rangle)\rangle. This is the orientational analogue of the root-mean-square fluctuation: it measures how many degrees the dipole typically deviates from its mean orientation, independent of whole-protein tumbling. Lowθloc\theta_{\mathrm{loc}}(blue) indicates a rigidly held dipole; highθloc\theta_{\mathrm{loc}}(red) indicates conformational flexibility.

The variation inTkT_{k}is real and reflects the distinct local environment of each Trp, but individual values carry varying degrees of uncertainty.

## T3T_{3}(protein conformational).

The largest variation spans an order of magnitude, from 0.45 ns (Trp7) to 8.52 ns (Trp4). Deeply buried residues in rigid regions can sense very slow conformational modes: Trp3 (SASA=0.046=0.046nm2,T3=6.8T_{3}=6.8ns,f3=0.24f_{3}=0.24) is the clearest example. However, burial alone does not determineT3T_{3}: Trp5, the most buried site (SASA=0.029=0.029nm2), hasT3=0.96T_{3}=0.96ns. Sites near theα\alpha–β\betainterface (Trp4, Trp7) show contrasting behaviour: Trp4 hasT3=8.52T_{3}=8.52ns but onlyf3=0.05f_{3}=0.05, meaning the slow component contributes just 5% of the total variance. Because the 40 ns trajectory spans onlyTtraj/T3≈4.7T_{\mathrm{traj}}/T_{3}\approx 4.7slow-mode periods, this value is poorly constrained; the trueT3T_{3}could lie anywhere in the 5–15 ns range. Trp3 (T3=6.8T_{3}=6.8ns,Ttraj/T3≈5.9T_{\mathrm{traj}}/T_{3}\approx 5.9) is similarly marginal. All other sites haveTtraj/T3>20T_{\mathrm{traj}}/T_{3}>20and are well constrained.

## T2T_{2}(water reorientation).

Most sites cluster between 0.4 and 1.0 ps, consistent with hydrogen-bond reformation dynamics. Trp6 (T2=8.58T_{2}=8.58ps) is a pronounced outlier. ItsT3/T2T_{3}/T_{2}ratio is only 57, compared to>700>700for every other site, indicating that theT2T_{2}andT3T_{3}components are poorly separated in the tri-exponential fit. Trp6 is buried (SASA=0.066=0.066nm2) and close to GDP (10.1 Å); the anomalousT2T_{2}likely reflects an intermediate timescale from nucleotide-associated ordered water or phosphate-group fluctuations that the fit cannot cleanly assign to either theT2T_{2}orT3T_{3}component.

## T1T_{1}(solvent libration).

The range is modest (27–68 fs, a factor of∼2.5{\sim}2.5). The short trajectory’s 10 fs cadence resolvesT1T_{1}at 3–7 frames, so absolute values carry∼30%{\sim}30\%uncertainty for the fastest sites (Trp1, 2, 7). Nevertheless, the ordering is physically meaningful: buried sites (Trp3, Trp6) tend to have slowerT1T_{1}, possibly reflecting non-water contributions to the fast mode from backbone fluctuations.

## Implications for the exciton dynamics.

Despite these uncertainties, the conclusions of Sec.III.4are robust because they depend only on theorder of magnitudeofTkT_{k}, not on precise values. All sites satisfyσ/|J|≫1\sigma/|J|\gg 1(strong disorder), all Kubo numbersκk≫1\kappa_{k}\gg 1(non-Markovian), and even the shortestT3T_{3}(0.45 ns) exceedsℏ/J≈90\hbar/J\approx 90fs by three orders of magnitude. The site-to-site heterogeneity is itself a physical feature: no single bath parameter set can describe all eight Trps, reinforcing the need for per-site noise modelling.

## Appendix FEigenstate localisation of the 8-site HamiltonianFigure A4:Eigenstate localisation in the 8-site Trp Hamiltonian, quantified by the participation ratioPRk=1/∑i|ci(k)|4\mathrm{PR}_{k}=1/\sum_{i}|c_{i}^{(k)}|^{4}.(a)PR of each eigenstate of the clean Hamiltonian. No eigenstate exceeds PR=2.07=2.07(Trp4–Trp7 pair), because the 388 cm-1spread of site energies overwhelms the couplings (|J|max=59|J|_{\max}=59cm-1).(b)Maximum PR across all eigenstates vs. added Gaussian disorderσ\sigma(500 realisations per point). The slight initial rise at smallσ\sigma(≲25\lesssim 25cm-1) is a disorder-assisted resonance effect: small random shifts can occasionally reduce the intrinsic detuning between coupled pairs (e.g.Δ​ϵ47=41\Delta\epsilon_{47}=41cm-1). At largerσ\sigma, disorder dominates and localisation sets in. The vertical dashed line marks the MD-derivedT3T_{3}noise level (σ3≈200\sigma_{3}\approx 200cm-1); at this point the max PR drops to 1.40.

Diagonalising the clean Hamiltonian (Table3) reveals that the eight-site network fragments into three weakly connected pairs (Trp4–Trp7, Trp6–Trp8, Trp2–Trp3) and two nearly isolated sites (Trp1, Trp5). The participation ratioPRk=1/∑i|ci(k)|4\mathrm{PR}_{k}=1/\sum_{i}|c_{i}^{(k)}|^{4}measures the effective number of sites spanned by eigenstatekk: it equals 1 for a state fully localised on a single site andNNfor a state uniformly delocalised across allNNsites. As shown in Fig.A4(a), no eigenstate exceeds PR=2.07=2.07, far below the fully delocalised limit of 8. The root cause is the large spread of diagonal site energies (388 cm-1), which exceeds the strongest coupling by a factor of 6.6.

Adding Gaussian static disorderσ\sigmato the diagonal further localises the eigenstates [Fig.A4(b)]. At the MD-derivedT3T_{3}level (σ3≈200\sigma_{3}\approx 200cm-1), the maximum PR drops to 1.40, indicating near-complete single-site confinement under the realistic bath. These results are referenced in the superradiance discussion of Sec.IV.

## 


- 


Major funding support from
