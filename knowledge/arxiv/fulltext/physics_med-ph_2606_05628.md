# Transcranial FUS Therapy and Monitoring using Nonlinear Acoustics

**arXiv ID**: 2606.05628v1
**Authors**: Pradosh Pritam Dash
**Published**: 2026-06-04
**Categories**: physics.med-ph, math-ph, physics.app-ph
**Comments**: Ph.D. thesis, Georgia Institute of Technology, 2026. 139 pages. Advisor: Prof. Costas D. Arvanitis. https://hdl.handle.net/1853/81728
**HTML URL**: https://arxiv.org/html/2606.05628v1

## Abstract

Focused ultrasound (FUS) offers a promising, non-invasive method for modulating neural activity and delivering therapies deep within the brain with immense clinical potential. However, progress in developing transcranial ultrasound (TUS) for clinical applications has been hindered by several factors. The complexity of the human skull causes focal aberrations and attenuation, thereby presenting a major obstacle to the precise targeting of ultrasound waves. Although phased arrays can correct for these aberrations, their high cost and continuous reliance on magnetic resonance imaging (MRI) pose significant obstacles for widespread academic research and clinical translation. To address these challenges, this thesis proposes an innovative framework for the design, registration, and clinical application of acoustic holograms. First, we introduce a novel frequency-domain topology optimization method that overcomes the breakdown of traditional phase-only designs in the megahertz regime by accounting for volumetric wave-propagation effects, thereby achieving high-fidelity focusing. Second, we present a non-invasive registration strategy that utilizes the nonlinear parametric array (PA) effect to enable precise lens alignment without requiring any imaging modalities, such as MRI. Finally, we demonstrate the utility of this nonlinear parametric array (PA) effect as a tool for monitoring ventricular dilation as a non-invasive proxy for intracranial pressure changes in hydrocephalus. Collectively, these developments provide a path toward accessible, high-precision transcranial ultrasound systems for research and clinical use. In addition, we demonstrate a novel platform for in vitro focused ultrasound neuromodulation that leverages acoustics to advance therapeutic discovery.

## Full Text

Contents

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2606.05628v1 [physics.med-ph] 04 Jun 2026

math]†‡§¶∥††‡‡

Transcranial FUS Therapy and Monitoring
using Nonlinear Acoustics
A Dissertation
Presented to
The Academic Faculty
By
Pradosh Pritam Dash
In Partial Fulfillment
of the Requirements for the Degree
Doctor of Philosophy in the
School of Mechanical Engineering
Georgia Institute of Technology
May 2026Copyright © Pradosh Pritam Dash 2026

Transcranial FUS Therapy and Monitoring
using Nonlinear Acoustics


Approved by:

Prof. Costas Arvanitis, Advisor

School of Mechanical Engineering &

Dept. of Biomedical Engineering

Georgia Tech & Emory University


Prof. F. Levent Degertekin

School of Mechanical Engineering

Georgia Tech


Prof. Karim Sabra

School of Mechanical Engineering

Georgia Tech


Prof. Levi Wood

School of Mechanical Engineering

Georgia Tech


Prof. Liang Han

School of Biological Sciences

Georgia Tech


Date Approved: March 17, 2026

Acknowledgments


My Ph.D. journey has rarely been a solitary endeavor, and I am deeply grateful and indebted to the many individuals who have been a blessing to me along the way. First and foremost, I would like to express my sincere gratitude to my advisor, Prof. Costas D. Arvanitis, for his invaluable guidance and support throughout my time in the Ultrasound Biophysics and Bioengineering Laboratory. His mentorship and vision have profoundly shaped my approach to research and life. I also express my gratitude to the members of my doctoral committee: Prof. Karim Sabra, Prof. Liang Han, Prof. Levi Wood, and Prof. F. Levent Degertekin. Their insightful feedback and rigorous evaluations shaped this work in ways I did not anticipate.

I owe a special debt of gratitude to Dr. Scott Schoen Jr., whose research I had the privilege to build upon and extend, and whose mentorship has been invaluable. I am also thankful to my colleagues and collaborators for their technical assistance and camaraderie. The countless discussions we shared were instrumental in refining my work, navigating the complexities of this research, and managing the stress of a PhD.

My appreciation also extends to my earlier mentors who laid the foundational stones for my academic journey: Profs. Ricardo Burdisso and Pablo Tarazaga at Virginia Tech, and Prof. Subrata Panda at NIT Rourkela, whose early guidance and belief in my potential set me on this path.

Finally, I want to thank my family and friends for their unwavering support and love. To spell out everything I owe to you will be pure hubris. Your presence has been a constant source of strength, and this milestone would not have been possible without you all.

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

## List of SymbolsSymbolDefinitionSymbolDefinitionA​RARpixel geometric aspect ratio (L2​π/ΛL_{2\pi}/\Lambda)Ps​i​m,Pf​w​dP_{sim},P_{fwd}Simulated high-res vs. forward-sampled fieldsdrd_{r}Vector drag coefficient for dynamic ARFpΔ​fp_{\Delta f}Parametric array difference-frequency pressureEt​r​a​p​p​e​dE_{trapped}Integrated trapped acoustic energy in skullℛ\mathcal{R}Regularization penalty for topology smoothingFr​a​dF^{rad}Time-averaged Acoustic Radiation Force (ARF)SN​LS_{NL}Virtual volumetric nonlinear source densityf1,f2f_{1},f_{2}Biosphere compressibility and density contrastt(n),tm​a​xt^{(n)},t_{max}Computed hologram thickness and upper boundℋ\mathcal{H}HASA forward wave propagation operatoru(n)u^{(n)}Unconstrained thickness optimization parameterΔ​I\Delta ICentral pixel intensity drop (ARF tracking)wkw_{k}Kinetic energy density (elastodynamic shear)kek_{e}Effective stiffness constant of hydrogel matrixwpw_{p}Potential energy density (volumetric compression)L2​πL_{2\pi}Modulation depth for a full2​π2\piphase shiftαT\alpha_{T}Amplitude transmission coefficientℒ(n)\mathcal{L}^{(n)}HASA-ADAM topology optimization lossγ\gammaSpeed of sound mismatch ratiom,ηm,\etaHydrophone linear and nonlinear sensitivitiesθc\theta_{c}Critical angle for elastodynamic shear conversionμ\muSquared refractive index ratio (c02/c2c_{0}^{2}/c^{2})Λ\LambdaHASA spatial variation termorLateral pitchPp​r​i​m​a​r​yP_{primary}Envelope of squared primary pressureϕg​a​s\phi_{gas}Trapped gas volume fraction (pneumocephalus)

SUMMARY


Focused ultrasound (FUS) offers a promising, non-invasive method for modulating neural activity and delivering therapies deep within the brain with immense clinical potential. However, progress in developing transcranial ultrasound (TUS) for clinical applications has been hindered by several factors. The complexity of the human skull causes focal aberrations and attenuation, thereby presenting a major obstacle to the precise targeting of ultrasound waves. Although phased arrays can correct for these aberrations, their high cost and continuous reliance on magnetic resonance imaging (MRI) pose significant obstacles for widespread academic research and clinical translation. To address these challenges, this thesis proposes an innovative framework for the design, registration, and clinical application of acoustic holograms. First, we introduce a novelfrequency-domain topology optimizationmethod that overcomes the breakdown of traditional phase-only designs in the megahertz regime by accounting for volumetric wave-propagation effects, thereby achieving high-fidelity focusing. Second, we present anon-invasive registration strategy that utilizes the nonlinear parametric array (PA) effectto enable precise lens alignment without requiring any imaging modalities, such as MRI. Finally, we demonstrate the utility of this nonlinear parametric array (PA) effect as a tool formonitoring ventricular dilation as a non-invasive proxy for intracranial pressure changes in hydrocephalus. Collectively, these developments provide a path toward accessible, high-precision transcranial ultrasound systems for research and clinical use. In addition, we demonstrate a novel platform forin vitro focused ultrasound neuromodulationthat leverages acoustics to advance therapeutic discovery.

## Chapter 1Introduction and Background

## 1.1  The Evolution of Therapeutic Ultrasound

Ultrasound has evolved from a diagnostic novelty to a nearly ubiquitous tool in the medical ultrasound field[1]in the past five decades. Recent therapeutic advances extended the field into high-intensity regimes, with thermal ablation, cavitation, and shock wave-assisted therapies each entering clinical use[2,3,4].

Adoption in oncology and urology is now broad[5,6,7], yet CNS applications remained largely absent for decades. The obstacle is the complex geometry and heterogeneous microstructure of the human skull, which acts as an acoustic barrier. The skull attenuates energy and induces phase aberrations in the transmitted ultrasound fields, effects that worsen at the higher frequencies needed for precise spatial targeting.

Phased arrays, combined with Computed Tomography (CT) and magnetic resonance (MR) guidance[8,9,10,11,12], have largely resolved this barrier. Phased arrays consist of hundreds of transducer elements, each driven with a pre-calculated phase and amplitude to correct for skull-related aberrations. Per-element control enabled successful pilot studies in thermal ablation[13,14,15,16,17]and contrast agent-enhanced drug delivery[18,19,20].

Phased arrays carry drawbacks that limit access. They are prohibitively expensive, and element count is constrained by the packaging of the driving electronics, restricting the spatial resolution and wavefront complexity they can generate[21,22]. The reduced degrees of freedom narrow the treatable envelope: peripheral brain regions, the skull base, and irregularly shaped lesions are difficult to reach without depositing heat in adjacent healthy tissue or bone. The demand for larger transcranial treatment volumes and the need for conformal, high-resolution fields have outpaced what current phased-array-based solutions can deliver.

## 1.2  Acoustic Holography

Acoustic holography directly addresses the aforementioned limitations of phased arrays. Inspired by optical holography, this method encodes the desired acoustic wavefronts into a physical holographic lens or a metasurface[23].

A 3D-printed holographic lens modulates a single transducer’s output to produce a 2D phase profile that generates targeted focusing[24,25,26]and complex volumetric wave fields with diffraction-limited resolution[23]. The reconstruction degrees of freedom exceed those of commercial phased-array sources by two orders of magnitude, at a fraction of the cost.

## 1.2.1  Historical Context and Fabrication

Acoustic holography was first demonstrated in the 1990s. Recent gains in computational power and additive manufacturing have driven the revival of additive manufacturing in medical ultrasound. 3D printing now produces intricate, patient-specific holograms at low cost[26], which makes the hologram-based approaches more accessible. By calculating the required phase map using time-reversal or similar algorithms, a holographic lens can be tailored to an individual patient’s skull and thereby correct specific aberrations without the need for complex active electronics associated with phased arrays[brown2019].

## 1.2.2  Biomedical Applications

Customizable acoustic fields have extended holography into several areas of noninvasive brain therapy.Blood-Brain Barrier (BBB) Opening:Holographic lenses achieved simultaneous bilateral BBB opening in non-human primates[27]and mouse models[28]using 3D-printed holograms.High-Intensity Focused Ultrasound (HIFU):Holograms shape energy deposition to produce thermal holograms that match tumor geometry or target multiple locations simultaneously[29,30,31].Imaging:Holograms tailor transmit fields to generate Bessel beams with extended depth of field[32]or enable compressive 3D imaging using single sensors[33].

## 1.3  Design Challenges in the High-Frequency Regime

Generating a target acoustic field requires careful specification of the hologram’s phase and amplitude profiles. Available strategies include theIterative Angular Spectrum Approach (IASA)[23]andDirect Searchmethods[34]. Deep learning frameworks[35]and automatic differentiation (Diff-PAT)[36]have since accelerated the design of complex patterns.

High-fidelity holograms for transcranial use remain difficult to produce. Sub-millimeter accuracy for neurological interventions requires operation near1MHz1\text{\,}\mathrm{M}\mathrm{H}\mathrm{z}. Most rapid design methods rely on theThin-Element Approximation (TEA)orThin-Film Approximation (TFA), which treats the lens as a pure phase screen, ignoring its physical thickness. At MHz frequencies and below, lens features become comparable to the wavelength and the lens is acoustically thick (L≫λL\gg\lambda), invalidating the phase-screen model. The result isrefractive walk-off, where energy physically migrates to neighboring pixels within the lens, and volumetric diffraction effects that phase-only methods cannot capture. Full-wave time-domain simulations[25,26,37]model these effects correctly but are too slow for clinical use.

Thesis Contribution (Chapter2):Chap.˜2proposes HASA-ADAM, a frequency-domain lens topology optimization approach. The method accounts for volumetric wave propagation and medium heterogeneity. It scales to clinical dimensions without the computational cost of time-domain solvers.

## 1.4  The Registration Bottleneck

The second major challenge isregistrationof the hologram with the patient’s anatomy. A phase plate is a passive lens designed to accommodate the skull’s geometry in a particular orientation. The heterogeneous speed-of-sound map for which the plate is optimized is tied directly to the skull’s position and orientation relative to the transducer; shift one and the correction fails. Precise skull registration is, therefore, a prerequisite for correct operation. It has been shown that HASA fails to correct for skull aberrations when misregistration exceeds 10 wavelengths for point targets at1MHz1\text{\,}\mathrm{M}\mathrm{H}\mathrm{z}[38]. Accurate registration also governs thalamic targeting[39]and the spatial fidelity of real-time MR thermometry monitoring[40].

MR-guided tFUS (MRgFUS)[41]is the current gold standard: accurate, but expensive and slow. Neuronavigation (NaviFUS)[42]and augmented-reality holography[43]use optical tracking and cost far less, but achieve only millimeter-level accuracy. That falls short of the sub-millimeter precision high-frequency holograms demand. As shown in Table1.1, tFUS neuronavigation sits between these options in precision, cost, and clinical accessibility.Table 1.1:Comparison of FUS Registration ModalitiesModalityEst. CostPrecisionPrimary LimitationsMRgFUS[44,20]∼\sim$2.37M<1.0<1.0mmMonopolizes MRI; high capital cost; rigid frame pinning.Optical (NaviFUS)[45]∼\sim$80k1.5–3.5 mmBlind to real-time acoustic distortion; line-of-sight limits.AR (HoloLens)[43]∼\sim$3.5k4.4–7.2 mmHolographic drift; clinically unacceptable error margins.

Thesis Contribution (Chapter3):The gap between MRgFUS accuracy and optical-tracker cost motivates a third approach.Chap.˜3proposes a registration scheme based on thenonlinear parametric array effect. A misaligned lens amplifies nonlinear wave interactions within the skull, producing a measurable acoustic feedback signal. The method uses that signal to achieve sub-millimeter alignment without MR guidance.

## 1.5  Nonlinear Acoustics and Diagnostic Monitoring

The nonlinear wave interactions exploited for registration have uses beyond skull-to-lens alignment. At therapeutic intensities, linear propagation assumptions break down, leading to harmonic generation[46]and parametric mixing. These nonlinear phenomena are sensitive to the acoustic nonlinearity parameter (β\beta) of the medium. Brain tissue (β≈6.6\beta\approx 6.6) and cerebrospinal fluid (CSF,β≈5.2\beta\approx 5.2) have distinct nonlinear properties[47]. Because of this difference, the cumulative nonlinear signal should reflect changes in the intracranial environment, changes in the relative volumes of tissue and fluid alter the integratedβ\betaalong the propagation path. Hydrocephalus, defined by the accumulation of CSF, currently requires invasive intracranial pressure (ICP) monitoring, which carries risks of infection and hemorrhage[48].

Thesis Contribution (Chapter4):Chap.˜4applies nonlinear acoustic feedback to diagnostics. The central question is whether the parametric array effect can detect changes in ventricular volume. A positive result would allow hydrocephalus progression and shunt function to be tracked non-invasively, removing the need for surgical ICP probes.

## 1.6  Challenges in Ultrasound Neuromodulation

Focused ultrasound also offers a route to noninvasive neuromodulation. Transcranial electric stimulation (tES) and transcranial magnetic stimulation (TMS) are established tools, but both are constrained by the diffuse spread of the fields they produce, which limits spatial selectivity[49,50,51,52]. Focused ultrasound propagates mechanical waves deep into neuronal tissue with precise spatial targeting[53].

The biophysical mechanisms governing ultrasound-neuron interactions remain poorly understood. A major obstacle is a hard physical trade-off: precision and penetration depth pull in opposite directions. Sub-millimeter, cellular-level targeting requires frequencies above 10 MHz, which confines useful penetration to superficial tissue[54].In-vivowork is complicated further by thermal accumulation, bulk fluid streaming, and off-target auditory artifacts, which together make isolating specific mechanotransduction events very difficult[55,56]. Controlledin-vitroplatforms are needed to hold those variables fixed to facilitate therapeutic discovery.

Thesis Contribution (Chapter5):Chap.˜5describes the development and validation of anin-vitrofocused ultrasound neuromodulation platform. The apparatus isolates acoustic radiation force from confounders like thermal effects and fluid streaming, which can lead to false-positive neuronal activation. The chapter also introduces contrast-enhanced mechanostimulation using biocompatible metallic microspheres as local stress concentrators. These enable subcellular mechanical stimulation at clinically relevant low frequencies needed for deep tissue targeting.

## 1.7  Thesis Outline

This thesis addresses the design, registration, and monitoring challenges that may enable practical application of acoustic holography in clinical settings. It also introduces a platform forin-vitrofocused ultrasound neuromodulation. Inchapter2,the HASA-ADAM topology optimization framework accounts for volumetric wave propagation at MHz frequencies, where the thin-element approximation is inadequate due to unaccounted refraction and diffraction within the acoustically thick lens. Inchapter3,a registration scheme built on the nonlinear parametric array effect achieves sub-millimeter lens alignment without any external imaging modality such as MRI. This makes the hologram-based focus ultrasound therapy portable and accessible. InChapter4,nonlinear parametric array (PA) effect is applied to diagnostic monitoring: ventricular volume changes associated with hydrocephalus are monitored non-invasively by measuring the change in the PA signal measured outside the skull cavity. Lastly, inChapter5,anin-vitroneuromodulation platform is developed which implements biocompatible metallic microspheres as stress concentrators to deliver subcellular mechanical stimulation at low frequencies, isolating radiation-force effects from thermal and streaming confounders.

Note: An earlier version of portions of the work (chapter 2-4) presented in this thesis is available as a preprint on arXiv (https://arxiv.org/abs/2508.07103)[57].

## Chapter 2Hologram Topology Design00footnotetext:An earlier version of the work presented in this chapter is available as a preprint on arXiv (https://arxiv.org/abs/2508.07103).[57]

## 2.1  Introduction

Recent advancements in acoustic holography based on holographic lenses offer a promising pathway for designing simpler, more economical, and more flexible ultrasound systems for a range of applications, including contactless manufacturing[58], consumer electronics[59], non-destructive testing[60], imaging[33], and targeted neuro-interventions[25,25,37], among others[23,61,62]. These acoustic holograms, also known as phase plates, encode spatial phase patterns onto passive lenses, effectively transforming a single-element transducer into a device capable of generating complex volumetric pressure fields[jimenez2018adaptive,23]. This works because the effective pixel size sits well below the
acoustic wavelength[23]. Crucially, for large apertures (i.e., several cm2) this is equivalent to dense phased arrays (e.g.,104−10510^{4}-10^{5}elements) that are unrealizable, making possible field distributions that current phased-array technology cannot produce. Moreover, recent implementations that use numerical methods for wave propagation in heterogeneous media, such as the human skull, can account for skull-induced aberrations to produce focal spots[25,63]or pressure fields to concurrently target different brain regions[37,64,31,65,66].

Although this approach can achieve the desired phase distribution, converting the optimized phase pattern into a lens topology by scaling it with the relative wavenumber implies that the hologram is a thin element that alters only the phase, neglecting amplitude changes and wave propagation effects within the lens.

Frequencies (≈\approx1  MHz) or below are needed for deep-tissue penetration. The lens feature size in this range approaches the acoustic wavelength (λ<1.5\lambda<1.5mm), which invalidates the thin-element approximation and introduces significant thickness-dependent amplitude and phase errors. In this acoustically thick regime (L≫λL\gg\lambda), acoustic energy migrates laterally into neighboring pixels.

This causes volumetric crosstalk between the lens pixels, which phase-only models ignore. Lower frequencies penetrate the skull more easily; however, an operation near 1 MHz offers a workable compromise between spatial resolution and penetration depth. This frequency range is actively being explored for high-precision, non-thermal transcranial ultrasound (TUS) applications, such as targeted neuromodulation[67]and blood-brain barrier opening[68]. Spatial precision is essential for these applications, but phase-based lens design methods fail. Off-target hotspots are an additional concern at these frequencies. Although time-domain simulations can accurately model heterogeneities, they often take hours to run[37], which is too slow for iterating over the large apertures required in TUS[69]. Frequency-domain methods are faster. The standard angular spectrum approach (ASA) is fast but ignores wave-speed heterogeneities[23]. Other frequency-domain methods, such as the Modified Mixed Domain Method (MMDM)[70], can handle strong heterogeneities and reflections, but folding them into fast iterative optimizers is non-trivial. Automatic differentiation has been used to accelerate hologram design[36], and gradient-based optimization has been applied to related problems[58,71]. A fast 3D-printed lens design that is simultaneously free of thickness-dependent errors and accounts for heterogeneous-medium aberrations, however, remains unsolved[64].

We introduce a unified framework for high-fidelity acoustic holography. This framework uses the heterogeneous angular spectrum approach (HASA), which is a fast spectral method for wave propagation in complex media[72], and its ability to incorporate in-plane varying speed-of-sound maps and support differentiable optimization based on the ADAM iterative optimizer to design acoustic holograms with complex topologies. Unlike phase-only approaches, HASA-ADAM directly optimizes the lens topology and incorporates wave-propagation effects, as well as amplitude and phase changes within the lens material.

## 2.2  Methods

## 2.2.1  Preparing the Transcranial Medium

We must have a realistic heterogeneous three-dimensional (3D) acoustic property map of the skull to perform patient-specific transcranial focused ultrasound (TUS) hologram optimization. The 3D geometry was acquired via a micro-CT scan of the skull secured in the fixture. This makes DICOM volumes co-registered directly with the transducer coordinate space. The raw 3D imaging data were interpolated onto a voxel resolution of 250m​u\ mum (∼λ/6\sim\lambda/6) as per the 1 MHz sampling requirement. The CT voxel intensities were normalized against the water and air baselines to obtain approximate Hounsfield units (HH). These values were then used to calculate the volumetric porosity fraction of the bone, defined asΨ=1−H/1000\Psi=1-H/1000. A porosity-dependent semi-empirical mixture model[73]was then used to convert these values to 3D acoustic properties. Specifically, the density (ρ\rho) and longitudinal speed of sound (cc) for each voxel were linearly interpolated between the baseline properties of pure water (c=1480c=1480m/s,ρ=1000\rho=1000kg/m3) and the upper limits of the dense cortical bone (cmax=2500c_{\max}=2500m/s,ρmax=2200\rho_{\max}=2200kg/m3), proportional to the solid bone fraction (1−Ψ1-\Psi).

## 2.2.2  Holographic Lens Design

## 2.2.2.1  Heterogeneous Wave Propagation with ASA

The first step in our design process was to model wave propagation through skull heterogeneity. For a time-harmonic pressure field𝒑~​(𝒓)​e−i​ω​t\tilde{\bm{p}}(\bm{r})e^{-i\omega t}, whereω\omegais the angular frequency, the angular spectrumPPis given by its 2D spatial Fourier transformP​(kx,ky,z)=ℱk​[p~​(x,y,z)],P(k_{x},k_{y},z)=\mathcal{F}_{k}[\tilde{p}(x,y,z)],(2.1)

For heterogeneous media where the spatial variation of sound speedc​(𝒓)c(\bm{r})is less compared to the wavelength, the ordinary differential equation for the angular spectrumPPbecomesPz+kz2​P=Λ∗P,P_{z}+k_{z}^{2}P=\Lambda*P,(2.2)

Here,Λ=ℱk​[k02​(1−μ)]\Lambda=\mathcal{F}_{k}[k_{0}^{2}(1-\mu)],k0=ω/c0k_{0}=\omega/c_{0},μ=c02/c2\mu=c_{0}^{2}/c^{2},c0c_{0}is a reference (average) sound speed, and∗*indicates a two-dimensional convolution over the component wavenumberskxk_{x}andkyk_{y}. For our design, the skull and tissue (speed-of-sound and density maps) were obtained from micro-CT scan data of a human skull[12,arvanitis2014transcranial](original resolution 95μ\mum binned to 150μ\mum, which amounts to 10 points per wavelength forf0=1f_{0}=1MHz and considering equilibrium sound speedc0=1480c_{0}=1480m/s in water). HASA is specifically designed to handle these spatially varying properties. This wave propagation model captures the refraction and transmission of waves through the skull. In the current implementation, absorption was not considered in the calculations of the acoustic intensity.

An implicit solution of Eq. 2 may be obtained with a Green’s function technique[74], and numerical approximation allows computation ofPPat arbitraryzzviaPn+1≈Pn​ei​kz​Δ​z+ei​kz​Δ​z2​i​kz​(Pn∗Λ)×Δ​z,P^{n+1}\approx P^{n}e^{ik_{z}\Delta z}+\frac{e^{ik_{z}\Delta z}}{2ik_{z}}(P^{n}*\Lambda)\times\Delta z,(2.3)

wherePn=P​(kx,ky,n​Δ​z)P^{n}=P(k_{x},k_{y},n\Delta z).
Provided that the marching step sizeΔ​z\Delta zis much smaller than the wavelength (λ\lambda), Eq. 3 enables the calculation of the field in the heterogeneous medium and ensures the computational stability. We choseΔ​z=150​μ\Delta z=150\mum. To prevent spatial aliasing and circular convolution errors inherent to the discrete Fourier transform during Angular Spectrum propagation, the computational grids were zero-padded byN/2N/2on all boundaries during the forward pass. Using the above wave propagator, the pressure distribution at the target planePtP_{t}can be efficiently computed from the initial pressure fieldP0P_{0}.

## 2.2.2.2  Optimization Parameters

To address the physics described above, we implemented a topology optimization framework (HASA-ADAM). To adapt the optimization for different frequencies for a fixed aperture (60​mm60\,\text{mm}) and focal depth (45​mm45\,\text{mm}), spatial sampling relative to the wavelength (λ\lambda) was kept constant: the voxel sizes (d​xdxandd​zdz) were maintained atλ/6\lambda/6to prevent numerical aliasing. The maximum lens thickness (tm​a​xt_{max}) determines its ability to induce a full2​π2\piphase shift. Because the phase delay is proportional to the frequency, higher frequencies require thinner lenses to achieve the same phase-wrapping effect.Table 2.1:Summary of Optimization ParametersFrequencyWavelength (λ\lambda)Resolution (d​xdx)Grid Size (NN)Max Thickness0.5 MHz3.00 mm0.500 mm25610.0 mm1.0 MHz1.50 mm0.250 mm2405.0 mm2.0 MHz0.75 mm0.125 mm5122.5 mm

To address the stochastic nature of the ADAM optimizer and ensure exact reproducibility across studies, the hyperparameters and mathematical formulations utilized for both the topology and phase optimization pipelines to ensure convergence stability are detailed in Table2.2.Table 2.2:HASA-ADAM Hyperparameters for Topology OptimizationParameterTopology Optimization ValueLearning Rate (η\eta)0.01Max Iterations (Nm​a​xN_{max})500OptimizerADAMInitialization (T0T_{0})3.6 mmLoss Function MetricL1 Intensity LossVariable Constraintmin⁡(softplus​(u),5​mm)\min(\text{softplus}(u),5\text{ mm})Spatial PaddingN/2N/2on all boundaries

## Approach 1 - Topology Optimization

Topology optimization directly optimizes the lens thickness distribution to achieve a prescribed (known as reference) intensity profile at the target plane. This method employs the HASA algorithm to model skull heterogeneity and acoustic propagation through complex media. The algorithm is initialized with a uniform thickness distribution𝒖(0)\bm{u}^{(0)}and iteratively refined to minimize the loss function. At each iterationnn, the thickness is computed ast(n)=min⁡{softplus​(u(n)),tmax},t^{(n)}=\min\{\text{softplus}(u^{(n)}),t_{\max}\},(2.4)

where the softplus function ensures non-negative thickness values, andtmax=5t_{\max}=5mm (in the case of 1 MHz)imposes an upper bound on the hologram thickness. The complex pressure fieldP(n)P^{(n)}is then calculated using the HASA forward modelℋ​(P0,t(n))\mathcal{H}(P_{0},t^{(n)}), whereP0P_{0}represents the initial pressure distribution of the transducer. The loss function quantifies the mismatch between the computed intensityI(n)=|P(n)|2I^{(n)}=|P^{(n)}|^{2}and the target intensityItI_{t}at each spatial location(x,y)(x,y):ℒ(n)=∑x,y|I(n)​(x,y)−It​(x,y)|+λ​ℛ​(t(n)),\mathcal{L}^{(n)}=\sum_{x,y}|I^{(n)}(x,y)-I_{t}(x,y)|+\lambda\mathcal{R}(t^{(n)}),(2.5)

whereλ​ℛ​(t(n))\lambda\mathcal{R}(t^{(n)})is a regularization term that encourages smooth thickness variations, withλ=0.01\lambda=0.01controlling the strength of regularization. The optimization process utilizes the ADAM optimizer with a learning rate ofη=0.01\eta=0.01to update the thickness parameter as follows:u(n+1)=u(n)−η​∇uℒ(n),u^{(n+1)}=u^{(n)}-\eta\nabla_{u}\mathcal{L}^{(n)},(2.6)

We used automatic differentiation with TensorFlow to calculate the gradients. The optimization iterations continue until the loss either converges below a threshold ofϵ=0.001\epsilon=0.001or the maximum number of iterationsNmaxN_{\max}is reached. We have keptNmaxN_{\max}at 500 for single-point focusing and at about 2000 for complex 2D distributions. The steps for optimizing hologram thickness (500 iterations for single-point focusing) are detailed in Table2.3.

## Approach 2 - Phase Optimization

The phase optimization approach[75,76]iteratively refines the phase distributionϕ\phiat the hologram surface while maintaining a fixed amplitude profile. The algorithm begins with an initial uniform phase distributionϕ(0)\phi^{(0)}and a zero-thickness assumption. At each iteration, the algorithm computes the pressure field usingPt(n)=ℋ​(P0,ϕ(n)),P_{t}^{(n)}=\mathcal{H}(P_{0},\phi^{(n)}),(2.7)

Here,ℋ\mathcal{H}represents the HASA propagation operator. The intensity at the target plane is calculated asIt(n)=|Pt(n)|2I_{t}^{(n)}=|P_{t}^{(n)}|^{2}. The loss function for phase optimization is expressed as follows:ℒ(n)=∑x,y|It(n)−It|+λ​ℛ​(ϕ(n)).\mathcal{L}^{(n)}=\sum_{x,y}|I_{t}^{(n)}-I_{t}|+\lambda\mathcal{R}(\phi^{(n)}).(2.8)

whereItI_{t}is the target intensity distribution, andℛ​(ϕ(n))\mathcal{R}(\phi^{(n)})regularizes the phase profile to encourage smoothness. The phase was then updated using the gradient descent with the ADAM optimizer. Following convergence, the optimized phase profile was converted into a thickness map. Furthermore, the optimization routine considers the impact of hologram thickness on amplitude transmission. This was achieved by converting the refined phase profile at the transducer surface into a thickness map of the adhesive layer. This conversion relies on the relationship between the phase change and thickness variation, represented byΔ​ϕ​(x,y)=(kw−kh)​Δ​h​(x,y),\Delta\phi(x,y)=(k_{w}-k_{h})\Delta h(x,y),(2.9)

Here,kwk_{w}andkhk_{h}denote the wave numbers of the water and hologram material, respectively. The thickness is used to compute the transmission coefficientαT\alpha_{T}and the complex amplitude at the hologram plane, following established expressions[23]. The hologram phase optimization steps are summarized in Table2.3Additionally, Figure2.1describes the process of designing a hologram via phase or topology optimization using a process flow chart.Table 2.3:Table 1: HASA-ADAM algorithm for a) topology optimization, b) phase optimizationa. HASA-ADAM: Topology OptimizationHASA-ADAM: Phase OptimizationInput:​Nmax,ϵ,η,λ,u(0),ItOutput:​t,ℒwhile​n​<Nmax​and​ℒ(n)>​ϵ​dot(n)=min⁡{softplus⁡(u(n)),tmax}P(n)=ℋ​(P0,t(n))I(n)=|P(n)|2ℒ(n)=∑x,y|Ii(n)​(x,y)−It​(x,y)|+λ​R​(t(n))u(n+1)=u(n)−η​∇uℒ(n)n←n+1end return​t(n),ℒ(n)\begin{aligned} &\text{ Input: }N_{\max},\epsilon,\eta,\lambda,u^{(0)},I_{t}\\
&\text{ Output: }t,\mathcal{L}\\
&\text{ while }n<N_{\max}\text{ and }\mathcal{L}^{(n)}>\epsilon\text{ do }\\
&t^{(n)}=\min\left\{\operatorname{softplus}\left(u^{(n)}\right),t_{\max}\right\}\\
&P^{(n)}=\mathcal{H}\left(P_{0},t^{(n)}\right)\\
&I^{(n)}=\left|P^{(n)}\right|^{2}\\
&\mathcal{L}^{(n)}=\sum_{x,y}\left|I_{i}^{(n)}(x,y)-I_{t}(x,y)\right|+\lambda R\left(t^{(n)}\right)\\
&u^{(n+1)}=u^{(n)}-\eta\nabla_{u}\mathcal{L}^{(n)}\\
&n\leftarrow n+1\\
&\text{ end return }t^{(n)},\mathcal{L}^{(n)}\end{aligned}Input:​Nmax,ϵ,η,λ,P0,PtOutput:​ϕ,ℒwhile​n​<Nmax​and​ℒ(n)>​ϵ​doPi(n)←ℋ​(P0,ϕ(n));Ii(n)=|Pi(n)|2ℒ(n)←∑x,y|Ii(n)−It|+λ​ℛ​(ϕ(n));ϕ(n+1)←ϕ(n)−η​∇ϕℒ(n);P0(n+1)←αh​P0(n);n←n+1;endreturn​ϕ(n),ℒ(n)\begin{aligned} &\text{ Input: }N_{\max},\epsilon,\eta,\lambda,P_{0},P_{t}\\
&\text{ Output: }\phi,\mathcal{L}\\
&\text{ while }n<N_{\max}\text{ and }\mathcal{L}^{(n)}>\epsilon\text{ do }\\
&P_{i}^{(n)}\leftarrow\mathcal{H}\left(P_{0},\phi^{(n)}\right);I_{i}^{(n)}=\left|P_{i}^{(n)}\right|^{2}\\
&\mathcal{L}^{(n)}\leftarrow\sum_{x,y}\left|I_{i}^{(n)}-I_{t}\right|+\lambda\mathcal{R}\left(\phi^{(n)}\right);\\
&\phi^{(n+1)}\leftarrow\phi^{(n)}-\eta\nabla_{\phi}\mathcal{L}^{(n)};\\
&P_{0}^{(n+1)}\leftarrow\alpha_{h}P_{0}^{(n)};n\leftarrow n+1;\\
&\text{ end }\\
&\text{ return }\phi^{(n)},\mathcal{L}^{(n)}\end{aligned}Figure 2.1:Process Flow Chart for HASA-ADAM Phase and Topology Optimization. We start the process by extracting the acoustic properties from micro-CT scan data, which are then fed to the HASA-ADAM optimizer for phase or topology optimization. Upon convergence, a phase or topology map is generated. The topology map can be printed as is, whereas the phase map needs to be converted into a thickness map.

## 2.2.2.3  Fabrication

The final step in the design process was the fabrication of the holograms. For topology optimization (i.e., Approach 1), we 3D-printed the thickness mask without any additional processing. To do this for phase opEq..e., approach 2), we utilize equation (9) to convert the optimized phase map to a thickness map and 3D-print it. In our design, we used a clear white v4 resin from Formlabs (Somerville, MA). Lenses were printed using a Formlabs Form 3B printer. This resin has low attenuation values across the frequency range of interest and a higher speed of sound (with group velocitycg=2591c_{g}=2591m/s and attenuationα0=2.922\alpha_{0}=2.922dBMHz-1.044cm-1), making it suitable for 3D printing acoustic holograms among the materials characterized by Bakaric et al.[77].

## 2.2.3  Hologram Design Validation

## 2.2.3.1  Trans-Skull Simulations

Holograms were tested using 3D linear acoustics simulations in the open-source k-wave toolbox with GPU acceleration[78]. The elastic effects were ignored because the angle of incidence on the skull bone in our study was below the critical angle in most cases. All simulations used a spatial grid size ofΔ​x=Δ​y=250​μ\Delta x=\Delta y=250\,\mum and a CFL number below 0.3. A porosity-dependent semi-empirical relationship converted Hounsfield unitsHHfrom the micro-CT scan to the speed of soundcc, densityρ\rho, and attenuationα\alpha. Spatially varying maps for these properties were used throughout. The maximum speed and density of solid bone were taken ascbone=2500c_{\text{bone}}=2500m/s andρbone=2000\rho_{\text{bone}}=2000kg/m3. Attenuation followed a power lawα=α0⋅fβ\alpha=\alpha_{0}\cdot f^{\beta}withβ=1.2\beta=1.2.

To capture shear mode conversion and propagation at the lens interfaces, we ran full-wave 3D elastic simulations using thepstdElastic3Dsolver in k-Wave[78]. Skull bone was isolated by a density threshold (ρ>1100\rho>1100kg/m3), with a shear wave speed ofcs=1400c_{s}=1400m/s and shear attenuationαs=20\alpha_{s}=20dB/cm assigned to those voxels. A concern was whether the lower MSE in the elastic model reflected higher attenuation, which can artificially reduce the error amplitude. To rule this out, we zeroed the shear attenuation (αs=0\alpha_{s}=0) while keeping the slow shear velocity intact (Table2.4). Sharp fluid-solid boundaries can trigger numerical instability in elastic simulations. We addressed this by smoothing the property matrices and holding the CFL number to 0.1.Table 2.4:Acoustic Parameters for k-Wave Fluid and Elastic SimulationsParameterFluid ModelElastic ModelBackground Density (ρ0\rho_{0})1000​kg/m31000\,\text{kg/m}^{3}1000​kg/m31000\,\text{kg/m}^{3}Density Threshold (ρb​o​n​e\rho_{bone})>1100​kg/m3>1100\,\text{kg/m}^{3}>1100​kg/m3>1100\,\text{kg/m}^{3}Compressional Speed (cpc_{p})Derived from CT scanDerived from CT scanShear Speed (csc_{s})N/A1400​m/s1400\,\text{m/s}Fluid Attenuation (α0\alpha_{0})0.0022​dB/cm/MHzy0.0022\,\text{dB/cm/MHz}^{y}0.0022​dB/cm/MHzy0.0022\,\text{dB/cm/MHz}^{y}Compressional Atten. (αp\alpha_{p})Derived from CT scanDerived from CT scanShear Attenuation (αs\alpha_{s})N/A10−20​dB/cm/MHzy10-20\,\text{dB/cm/MHz}^{y}Courant Number (CFL)0.30.30.10.1

## 2.2.3.2  Trans-Skull Experiments

Ex vivo trans-skull experiments were performed using a degassed deionized water tank. A 60 mm diameter piston transducer (Precision Acoustics, Dorchester, UK) was coupled to a 3D printed hologram lens. The transducer was driven by a function generator (HP Agilent Keysight, 33511B)) amplified by a power amplifier (E&I, Rochester, NY, USA). The transducer and lens assembly were then attached to the parietal region of an overnight degassed (approximately 12h) skull cap (Skulls Unlimited, Oklahoma City, OK, USA). The focal field of the lens was scanned using a calibrated 2 mm needle hydrophone (Precision Acoustics, Dorchester, UK) mounted on a three-axis positioning system (Velmex, Bloomfield, NY, USA) and recorded using a digital oscilloscope (Pico Technologies, St Neots, UK).

## 2.2.4  Forward Modeling of Hydrophone Aperture and Sampling Effects

Blurring and pixelation differences between simulations and measurements were reproduced by a forward model of the physical acquisition chain. The model has two steps, following the physics of the measurement setup:

## Finite Aperture Spatial Averaging & Discrete Subsampling

The first step models the continuous physical interaction between the acoustic field and the sensor face. The simulation fieldPs​i​m​(x,y)P_{sim}(x,y), generated on a high-resolution grid (250​μ​m250\,\mu\text{m}), was convolved with a spatial kernel representing the active area of the needle hydrophone (active element diameterD=2.0D=2.0mm):Pa​v​g​(x,y)=Ps​i​m​(x,y)∗Hd​i​s​k​(D)P_{avg}(x,y)=P_{sim}(x,y)*H_{disk}(D)(2.10)

Performing this on the full-resolution grid captures the spatial averaging over the sensor face.

The second step models the digitisation of the stepper-motor scan. Despite the fine simulation grid, the experimental raster scan had a500​μ500\,\mum step. We therefore downsampledPa​v​g​(x,y)P_{avg}(x,y)to the experimental scan grid:Pf​w​d​(i,j)=Pa​v​g​(xi,yj)forx,y∈Gride​x​pP_{fwd}(i,j)=P_{avg}(x_{i},y_{j})\quad\text{for}\quad x,y\in\text{Grid}_{exp}(2.11)

The result is a synthetic measurement that reproduces both the aperture blur and the step-limited pixelation seen in the data.

## 2.3  Results

## 2.3.1  Hyperparameter Study of the HASA-ADAM Topology Optimization

Stochastic optimizers can be sensitive to hyperparameter choices. We ran an empirical sweep to check convergence across configurations. We swept learning rates acrossη∈{0.001,0.005,0.01,0.05,0.1}\eta\in\{0.001,0.005,0.01,0.05,0.1\}and observed stable, monotonic loss curves in every case (Figure2.2a). High learning rates fell fast but oscillated near convergence; low rates were stable but slow.η=0.01\eta=0.01was the best practical compromise. We also checked the Total Variation (TV) regularizer. TV smoothing is needed for manufacturability, but excessive weight could compromise acoustic accuracy. Sweepingλ∈{0.0,0.01,0.1,1.0,10.0}\lambda\in\{0.0,0.01,0.1,1.0,10.0\}while tracking the raw intensity L1 error over 200 iterations showed no separation between curves (Figure2.2b). This confirmed that TV smooths the lens geometry without degrading the acoustic reconstruction in our optimizer.Figure 2.2:HASA-ADAM Hyperparameter Study.(a)Optimization convergence across varying learning rates.(b)Pure data loss across varying TV regularizer weights. The coincident plateaus confirm that the regularizer shapes the topology without reducing focal fidelity.

## 2.3.2  Canonical Validation of the HASA-ADAM Optimization Framework

As a first test, we validated the optimizer on a canonical inverse problem—single-point focusing in a homogeneous free field—before introducing the skull.
We optimized a 1  MHz Gaussian point focus at 45  mm depth using a 60  mm aperture in pure water (c0=1500c_{0}=1500m/s), as per the steps in the computational graph of Section 2.2.1.2. Asoftplusactivation was used to bound the lens to 5 mm, and an L1 loss drove convergence. Grids were zero-padded to prevent aliasing.
The Rayleigh-Sommerfeld analytical solution for single-point focusing[79]was our benchmark for this exercise. In this idealized environment, the required lens thicknessha​n​a​l​y​t​i​c​a​l​(x,y)h_{analytical}(x,y)maps to a standard Fresnel zone plate:ha​n​a​l​y​t​i​c​a​l​(x,y)=(x2+y2+F2−F1−c0/cl​e​n​s)(modL2​π)h_{analytical}(x,y)=\left(\frac{\sqrt{x^{2}+y^{2}+F^{2}}-F}{1-c_{0}/c_{lens}}\right)\pmod{L_{2\pi}}(2.12)

wherecl​e​n​s=2591c_{lens}=2591m/s, andL2​πL_{2\pi}is the material thickness for a full2​π2\piphase shift. As shown in Figure2.3, both optimizers avoided local minima and produced tightly confined focal spots. Thickness profiles were compared with the analytical Fresnel geometry to assess structural fidelity. Phase optimization achieved a high structural correlation (r=0.892r=0.892), consistent with its planar phase-matching formulation. Topology optimization showed a lower morphological correlation (r=0.70r=0.70), with noticeable deviations from the analytical ideal. This divergence has a straightforward physical explanation. Topology optimization targets intensity at the focal plane rather than a prescribed surface phase, giving the optimizer far more freedom to distribute material. Since phase retrieval from intensity is ill-posed, many different thickness profiles produce nearly the same focal spot. Thesoftplusactivation also smooths the sharp2​π2\piphase-wrap discontinuities required by the analytical lens. The result is a more continuous, printable lens that explores the volumetric wave-propagation space more fully, at the cost of a slight reduction in peak focal intensity. The optimizer still finds valid topographies that satisfy the focal objective, confirming that the HASA gradients are accurate.Figure 2.3:Canonical Validation of HASA-ADAM Optimization.Top row:1D thickness profiles.Second row:2D thickness maps.Bottom rows:Focal intensity in the axial (XZ) and lateral (XY) planes. Correlation drops from 0.892 (Phase Opt) to 0.70 (Topology Opt), but the topology optimizer finds an alternative valid topography that produces a well-confined focal spot.

## 2.3.3  HASA combined with ADAM iterative optimizer can design holographic lens topologies for high fidelity acoustic holography

We introduce a framework that combines the Heterogeneous Angular Spectrum Approach (HASA), a fast spectral method for wave propagation in complex media[72]with the ADAM iterative optimizer to reduce a loss function (absolute difference in intensity between reference or target image and image plane)[36], for accelerated hologram optimization (Fig.2.4a and Table2.3). This approach takes advantage of HASA’s ability to incorporate in-plane varying speed-of-sound maps and support a differentiable optimization of lens thickness profiles (that is, assuming an initial zero phase and constant amplitude at the source; Fig.2.4a and Table2.3). Consequently, the proposed framework allows for direct topology optimization and the design of holographic lens topologies that account for the physical effects of wave propagation within the lens, and consequently, generate holographic lenses that encode complex acoustic holograms in the megahertz frequency range (Fig.2.4b). This approach can also be used for acoustic holography based on the optimized phase (Fig.2.4c).Figure 2.4:(a) Schematic of the hologram design framework, comprising two key steps: 1) the Heterogeneous Angular Spectrum Approach (HASA) for wave propagation and 2) optimization using ADAM. The HASA algorithm for phase or thickness optimization via gradient descent is presented in Table2.3. (b) The HASA-ADAM framework was used to optimize the topology of a lens for a complex 2D hologram. At 2 MHz, this direct thickness optimization results in a high-fidelity target reconstruction. (c) HASA-ADAM phase optimization results for the complex 2D hologram at 2 MHz. Because the lens is acoustically thin at this higher frequency, the thin-element approximation holds; converting an ideal phase mask (top, utilizing a 125μ\mum pitch over a 60 mm aperture) into a physical thickness profile (bottom) produces good holographic results. (d) Complexity analysis of hologram optimization using HASA, showing that HASA optimization (O​(N2​log⁡N)O(N^{2}\log N)) requires more computational time than ASA (O​(N​log⁡N)O(N\log N)).

To test this concept and evaluate its performance, we first aimed to generate a complex holographic pattern at 2 MHz. We compared the performance of our direct topology optimization approach (Fig.2.4b) with conventional acoustic holography methods, which rely on generating an optimized phase pattern and converting it to a physical thickness profile based on the thin-element approximation (Fig.2.4c). For the optimization and lens topology, a fine discretization ofλ/6\lambda/6(125μ\mum at 2 MHz) was used over a 60 mm aperture. As shown in Fig.2.4b and c, at 2 MHz, both direct topology optimization and the phase-to-thickness conversion successfully produce the target holographic pattern with high fidelity. Because the physical thickness required to achieve a full2​π2\piphase shift at 2 MHz is relatively small, the lens remains acoustically thin, and the thin-element approximation holds. However, for many practical biomedical applications, such as transcranial ultrasound, operating at lower frequencies (e.g., 1 MHz or below) is critical to minimize acoustic attenuation and safely penetrate the skull. As the operating frequency drops, the acoustic wavelength increases, necessitating a proportionally thicker lens to achieve the same phase modulation.

The computational complexity (∼O​(N2​log⁡N)\sim O(N^{2}\log N)) of the proposed framework is higher than that of the homogeneous ASA (∼O​(N​log⁡N)\sim O(N\log N)) (Fig.2.4d)[23], the optimized hologram topology converged in approximately 20 min using a discretization ofλ/10\lambda/10at 1 MHz within a domain size ofN=40N=40mm (corresponding to a volume of 40 mm3) on a system equipped with a 24 GB NVIDIA RTX 3090 GPU. Moreover, increasing the linear dimension by 50% (i.e., 6 cm, which was the upper limit in the capacity of the GPU used) resulted in approximately a threefold increase in computational time (close to the 2.4-fold expected from theO​(N2​log⁡N)O(N^{2}\log N)scaling and consistent with typical GPU-memory overhead). This highlights the method’s scalability and efficiency for large aperture (i.e., clinical-scale) designs. A major reduction in optimization time (∼\sim15 min for 500 iterations) can be achieved by downsampling the domain to a discretization ofλ/6\lambda/6at 1 MHz, without any loss in performance. Thus, we adopted aλ/6\lambda/6discretization for the subsequent studies. Together, HASA-ADAM constitutes a major advancement in acoustic holography, providing a unified framework for designing 3D-printed lenses for high-fidelity holography and enabling high-performance systems at a fraction of the cost.

## 2.3.4   Effect of Thin-Element Approximation on Hologram Optimization

Traditional hologram optimizations (such as Rayleigh-Sommerfeld diffraction[79]or homogeneous Angular Spectrum approaches)use the Thin-Element Approximation (TEA), also known as the Thin-Film Approximation (TFA), to get the thickness map for 3D printing. Phase-only optimization may be insufficient for high-fidelity holography once the lens becomes acoustically thick (i.e., at sub-megahertz frequencies). The TEA treats phase shifts as purely longitudinal ( in other words, along the axis of wave propagation) phenomena and ignores lateral energy migration. Below roughly 1  MHz, this assumption does not hold. Reducing the frequency shifts wave propagation from a locally planar regime to a volumetric diffraction regime. To motivate HASA-ADAM, we first examine where the TEA fails. The following subsections cover the theory and results across frequencies, which highlight this failure.

Resolving a lateral featureδ\deltaat depthzzrequires:2​d​x⏟Sampling Limit≤cf⏟λ≲δ⏟Resolution≈c⋅zf⋅D⏟Diffraction Geometry\boxed{\underbrace{2dx}_{\text{Sampling Limit}}\leq\underbrace{\frac{c}{f}}_{\lambda}\lesssim\underbrace{\delta}_{\text{Resolution}}\approx\underbrace{\frac{c\cdot z}{f\cdot D}}_{\text{Diffraction Geometry}}}(2.13)

Spatial resolution scales inversely with frequency: halvingffdoubles the minimum resolvable feature. Applying our geometry (f=1f=1MHz,D=60D=60mm,z=45z=45mm) givesδ≈1.13\delta\approx 1.13mm. The fine lines of the GT logo push directly against this boundary. The system is diffraction-limited.

## 2.3.4.1  Numerical Aperture and Feature Scaling

In acoustic holography, lens performance is characterized by its numerical aperture (NA). For the geometry used here (D=60D=60mm,F=45F=45mm), the maximum steering angle isθm​a​x≈33.7∘\theta_{max}\approx 33.7^{\circ}:NA=sin⁡(θm​a​x)=sin⁡(arctan⁡(D/2​F))≈0.55\text{NA}=\sin(\theta_{max})=\sin(\arctan(D/2F))\approx 0.55(2.14)

To steer a wavefront to angleθ\theta, the phase gradient on the lens surface must bed​ϕ/d​x=k0​sin⁡(θ)d\phi/dx=k_{0}\sin(\theta). The sampling pitchΛ\Lambdamust satisfy Nyquist to avoid grating lobes:Λ≤λ2⋅NA\Lambda\leq\frac{\lambda}{2\cdot\text{NA}}(2.15)

For a fixed NA, holographic feature sizeΛ\Lambdamust therefore scale linearly withλ\lambda.

## 2.3.4.2  Acoustically Thick Regime

The thin-film approximation fails because lens thicknessLLshrinks far less favorably than feature sizeΛ\Lambdaas the frequency increases. Unlike an electronic phased array, a passive lens generates phase delays by propagating through a material with a different sound speedcl​e​n​sc_{lens}. A full2​π2\piwrap requires a modulation depth:L2​π=λ|1−c0/cl​e​n​s|L_{2\pi}=\frac{\lambda}{|1-c_{0}/c_{lens}|}(2.16)

For biocompatible polymers in water, the contrast is moderate (∼0.6\sim 0.6), requiring 3–5 mm at 1 MHz. The total lens thicknessLLis therefore much larger thanλ\lambdaat these frequencies.

## Refractive Walk-off and Grid Distortion

Define thegeometric aspect ratioAR=L2​π/Λ\text{AR}=L_{2\pi}/\Lambda. For high-NA lenses,AR>1\text{AR}>1: the phase-modulating features resemble tall acoustic columns rather than a thin film. In this volumetric regime, the scalar TEA fails because the acoustic energy migrates laterally, commonly known as the refractive walk-off.

As illustrated by the ray-tracing analysis in Figure2.5A, acoustic waves undergo pronounced refraction at the steep sawtooth features. Instead of propagating longitudinally, the energy migrates laterally inside the lens. The macroscopic result is aHologram Grid Distortion(Figure2.5B): the acoustic exit coordinates (solid blue grid) contract radially relative to the ideal design grid (dashed grey). Energy intended for one pixel leaks into neighbors, generating volumetric crosstalk that phase-only optimization does not consider.

## Multi-Frequency Optimization Results

To assess volumetric cross-talk, we compared phase-based TEA optimization with HASA-ADAM topology optimization across operating frequencies (Figure2.5C). Converting a 2D phase map to a 3D thickness map degrades performance, as expected from the walk-off theory. HASA-ADAM topology optimization compensates for this.

At0.5 MHz, the required lens is∼\sim10 mm thick. This maximizes the ray walk-off. The phase-converted lens degrades sharply (SSIM: 0.25). HASA-ADAM pre-compensates these effects, recovering the target fidelity (SSIM: 0.77) to a greater extent.1.0  MHzoffers the best geometry-acoustics tradeoff for the given aperture. The standard phase-to-thickness conversion gave a PSNR of 14.83 dB. HASA-ADAM reached 18.88 dB by capturing volumetric diffraction. Lastly,2.0  MHz, being a higher frequency, should improve resolution. But the dense phase wrapping (which resets every multiple of the wavelength, i.e.,∼\sim0.75  mm) introduces edge diffraction and localized scattering. Even so, topology optimization (PSNR: 17.63 dB) outperformed the TEA conversion using phase-only optimization (PSNR: 14.54 dB).Figure 2.5:Simulations were performed for a high-NA acoustic lens (f=1f=1MHz,D=60D=60mm,F=45F=45mm) using a sound speed ofcl​e​n​s=2500c_{lens}=2500m/s.(A) Mechanism:Ray tracing through the lens cross-section. The Thin-Film Approximation (TFA) assumes that acoustic rays travel in straight lines (dashed gray), accumulating phase locally. In reality, the significant acoustic thickness causes the rays to refract according to Snell’s law (solid red),(B) Consequence:Hologram Grid Distortion. A top-down view comparing the ideal pixel grid assumed by the TFA (dashed gray) with the acoustic exit locations (solid blue). The simulation reveals significant Pixel Migration. Energy intended for a specific spatial coordinate is displaced into neighboring pixels.Video S1 & S2(C) Reconstruction Results:Comparison of holographic reconstructions across three frequencies (F0=0.5,1.0,2.0F_{0}=0.5,1.0,2.0MHz). The columns display the idealized Phase Screen, the Lens model (incorporating walk-off effects), and the topology model, alongside their respective intensity fields. Quantitative metrics (PSNR, SSIM) demonstrate the severe degradation in image quality resulting from refractive walk-off when using conventional phase-to-thickness conversion.

Parametric sweeps also corroborate these trends.Video S1shows a frequency sweep from 5.0 to 0.5  MHz, illustrating how bulkier lens geometries at lower frequencies worsen walk-off.Video S2isolates the effect of focusing strength. This shows that higher NA requires steeper phase gradients that worsen internal refraction.

## 2.3.5  Comparison with the IASA phase optimization confirms degradation of performance with frequency scaling

To further understand this failure, we re-examined the benchmark holograms from Melde et al. (2016)[23]and the GT logo to show the impact of frequency scaling (Figure.2.6). In this study, we used conventional Iterative Angular Spectrum Approach (IASA) phase optimization (similar to Melde et al. (2016)) to indicate where conventional phase optimization fails as we scale down the frequency.Figure 2.6:Impact of Frequency Scaling on Hologram Fidelity.(Blue Box) 2 MHz Regime:Comparison of Dove (Top Row) and GT Logo (Bottom Row) reconstruction.
(a, e) Ideal Phase & Amplitude.
(b, f) Phase only (Iterative Angular Spectrum Approach).
(c, g) Lens. Note that at 2 MHz, the IASA phase map is coherent, but the Lens (c, g) shows distortion due to Refractive Walk-off.(Red Box) 1 MHz Regime:(d, f-right) Scaling the GT Logo design to 1 MHz results in a loss of fidelity. The diffraction limitδ\deltadoubles. This merges the fine details of the image. Thus, the IASA-designed lens fails to form a coherent image.

At 2 MHz (λ≈0.75\lambda\approx 0.75mm), the diffraction limitδ\deltais sufficiently fine for resolving the targets.IASA Performance (b, f):The Phase-Only approximation produces coherent images for both the Dove (top) and GT Logo (bottom).Physical Lens (c, g):However, the physical lens introduces distortion. This is the Volumetric Failure where the lens is acoustically thick, causing a refractive walk-off that IASA cannot predict. When we scale to 1 MHz (Bottom Right) while maintaining the same aperture (D=50D=50mm) and distance (z=20z=20mm), the system hits the diffraction limit.
- •

Resolution Collapse:Halvingffdoubles the minimum feature sizeδ\delta. The fine lines of the GT logo are now smaller than the acoustic point-spread function.
- •

IASA Failure:The standard IASA optimization fails in this condition. It attempts to create features that physics cannot support, resulting in noisy and unrecognizable distributions.

We explicitly compare the performance of the proposed Topology Optimization (TO) against the standard IASA method using the specific geometric constraints of this study (f=1f=1MHz,D=60D=60mm,z=45z=45mm). Figure2.7a shows the pressure field resulting from a physical lens designed using the IASA. As predicted by the scaling analysis, the IASA failed to converge to a valid solution. The combination of the resolution limit (δ≈1.13\delta\approx 1.13mm) and the volumetric thickness (refractive walk-off) results in incoherent scattering.

In contrast, Figure.2.7b shows the result of the HASA-ADAM Topology Optimization. By solving the heterogeneous wave equation through the lens volume, the optimizer accounts for lateral energy transport and diffraction effects. It pre-compensated for the distortion and resulted in a coherent reconstruction of the GT logo.Figure 2.7:Phase-Only Optimization vs. Topology Optimization.A comparison of acoustic pressure fields simulated using k-wave for the GT Logo target atf=1f=1MHz (D=60D=60mm,z=45z=45mm).(a) IASA (Thin Film Approximation):The standard phase-optimization approach fails to produce a recognizable image. The lens thickness introduces phase errors and lateral walk-off that the optimizer ignores, resulting in aberrations.(b) Topology Optimization (This Work):The proposed method, which models the volumetric wave propagation, restores the fidelity of the hologram. (Scale Bar 2 mm)

The study confirms that converting phase maps to thickness is insufficient for high-fidelity acoustic holography (a∼5\sim 5-dB loss in PSNR due to refractive walk-off and volumetric diffraction). Failure here is governed by pixel migration and grid distortion in the thick-lens regime due to the Geometric Aspect Ratio of the lens features. Topology optimization compensates for these effects by accounting for volumetric wave propagation.

## 2.3.6  Experimental Validation and the Impact of Shear Wave Mode Conversion at the Lens Interface

We then experimentally validated the topology optimization framework at 1  MHz. We 3D-printed an optimized lens for the GT Bee logo (at a 45 mm distance from the transducer with a 60 mm aperture), characterized its acoustic field at the focal plane using a hydrophone raster scan, and compared it with k-wave predictions.

Initially, we observed a significant discrepancy between the fluid (compressional-only) simulation and the experiments in terms of edge definition and diffuse background haze. The k-wave fluid simulation (Fig.2.9a) predicts a tight, high-contrast spot, but the measured field (Fig.2.9c) is broader and shows off-axis leakage that the fluid model misses. The fluid model MSE was 0.0230 when compared with the experimental scan.

We investigated elastic mode conversion at the lens-water interface as the likely cause. Although the lens polymer is homogeneous and isotropic, the optimized surface topology creates many locally varying oblique incidence angles. Such geometry introduces pronounced shear-wave interactions that are omitted in scalar fluid models. The Zoeppritz equations govern energy partitioning at fluid-solid boundaries. An incident P-wave at non-normal incidence splits into a transmitted P-wave and a mode-converted shear S-wave. For the photopolymer used here,cs≈1300c_{s}\approx 1300m/s—roughly halfcp≈2590c_{p}\approx 2590m/s. The resulting S-waves degrade holographic fidelity via Phase Aberration and Refractive Steering.
- 1.

Phase Aberration:TheSS-waves due to mode conversion propagate at a reduced velocity. They accumulate phase delays relative to the primary longitudinal wavefront, which propagates at a faster velocity. This causes an uncorrelated phase, which in turn leads to destructive interference and a reduced peak focal intensity.
- 2.

Refractive Steering:The trajectory of the mode-converted shear waves is governed by Snell’s law for elastic media:sin⁡θscs=sin⁡θpcp.\frac{\sin\theta_{s}}{c_{s}}=\frac{\sin\theta_{p}}{c_{p}}.(2.17)

Owing to their lower sound speed (cs<cpc_{s}<c_{p}), shear waves are refracted at steeper angles relative to the surface normal. This differential refraction actively steers the acoustic energy away from the designated target features, spatially dispersing it across the observation plane to form the diffuse background haze observed experimentally.Figure 2.8:Verification of Phase Aberration vs. Shear Damping.Zeroing shear absorption (left) produces virtually the same field as the standard shear model (middle). The absolute difference (right) is negligible (MSE: 0.00, SSIM: 0.99, Correlation: 1.00), confirming that blurring originates from slow-shear-wave phase aberration and refraction, not attenuation.Video S3 & S4.

To confirm that the smearing results from slow-shear-wave aberration rather than simple attenuation, we ran an ablation study in the k-Wave elastic solver. We setαs=0\alpha_{s}=0while keepingcs=1400c_{s}=1400m/s. The resulting field is virtually identical to the fully attenuating case (Figure2.8). Correlation is 1.00, SSIM is 0.99, and the MSE is negligible. This shows that holographic degradation is driven by slow-shear-wave phase aberration and refractive steering at steep lens interfaces — not by energy absorption. Supplementary animations compare the fluid and elastic propagation fields (Video S3& S4). Also, FigureB.1in the appendix provides an elaborate description of the temporal evolution of shear waves relative to compressional waves at the lens interface and the effects of varying attenuation.Figure 2.9:Top row: Normalized intensity distributions of(a)the baseline Fluid Model,(b)the proposed Shear Model, and(c)the experimental ground truth.
Bottom row: Absolute error maps relative to the experimental data for(d)the Fluid Model and(e)the Shear Model. The Shear Model exhibited reduced residual artifacts and a lower Mean Squared Error (MSE: 0.0163) than the Fluid Model (MSE: 0.0230).(f)Quantitative performance metrics showing the Mean Squared Error (left axis) and Correlation Coefficient (right axis). The Shear Model achieves a 29.1% reduction in reconstruction error compared to the baseline.

By incorporating these shear phenomena into a full-wave elastic simulation, the proposed Shear Model (Fig.2.9b) successfully reproduces the distortions and background scattering observed in the experimental measurements.

The corresponding error map for the Shear Model was substantially attenuated (decrease in the MSE to 0.0163)(Fig.2.9e). As per (Fig.2.9f), shear wave propagation accounts for a 29.1% reduction in the reconstruction error and also improves the spatial correlation. These results suggest that the acoustic blurring and haze observed in high-frequency acoustic holography may be driven by elastic mode conversion at the lens’s topographical interfaces.Figure 2.10:Experimental validation of trans-skull hologram focusing and assessment of registration errors on focusing quality. (a) Schematic of phase and topology optimization for single focusing. (b) Single-point focusing phase maps for a transducer with a diameter of 60 mm and anF​#F\#of 0.75, with and without skull corrections (scale bar: 1 cm) and equivalent topology map. (c) Skull speed of sound map obtained from micro-CT scan. (d) Lateral and axial focal profiles with contours obtained from simulations and (e) experiments, both with and without aberration correction for phase and topology optimized lenses (scale bar: 2 mm). (f) Simulation mask for skull rotation (scale bar: 5 mm). (g) Axial and lateral 2D surface maps demonstrating targeting and focusing errors due to a±4​°\pm 4°skull rotation (scale bar: 2 mm). (h) Effect of skull rotation on peak amplitude and FWHM (Top) and focal shift and x, y and z directions (Bottom).

## 2.3.7  HASA-ADAM iterative optimizer for holographic lens topologies for TUS

To demonstrate that HASA-ADAM thickness optimization can be used for transcranial ultrasound (TUS), we optimized topologies for a single focus (1 MHz with an F-number of 0.75) through the human skull (Fig.2.10a-b). The optimization utilized spatially varying speed-of-sound (SoS) and density maps derived from micro-CT data (Fig.2.10c). We compared the thickness-optimized lens (Corrected Topology) with a lens design to generate a single focus in the free field (uncorrected/aberrated) and a lens optimized to account for aberration but designed with a standard phase-to-thickness conversion (Corrected Phase) (Fig.2.10a-c). The generated pressure was compared using both acoustic simulations and ex vivo trans-skull experiments (Fig.2.10d). We observed that the HASA-ADAM-based framework corrected for aberration and reduced the sidelobes in both the axial (x​zxz) and lateral (x​yxy) focal planes. These are indicated by both experimental and simulated data (Fig.2.10d).

The Corrected Topology optimization achieved a lower peak sidelobe level than the Corrected Phase approach. Additionally, the optimized hologram that incorporates aberration correction (Corrected Topology) achieves a 24.5% reduction in lateral 3 dB beam width and collimation of intended and actual focus(Fig.2.10d). Evidently, the focal pressure using the other two lenses was characterized by significant aberration (Fig.2.10d) and high side lobes, demonstrating suboptimal performance for high-frequency TUS.

The above data demonstrate the potential of the proposed framework to effectively correct skull-induced aberrations and lead to diffraction-limited performance; however, they also indicate that the focus attained with the experimental system is below the theoretical limits (Fig.2.10e). This discrepancy between the simulation and experiment is most likely due to registration errors or uncertainties in the skull and lens material properties or a combination of both. Past investigations have demonstrated that skull properties need to deviate by more than 20% to lead to significant errors[38], which is unrealistic in many cases.

To investigate this discrepancy, we performed a theoretical sensitivity analysis of the Speed of Sound (SoS) parameters. As shown in Table2.7, a±15%\pm 15\%mismatch in the skull or lens SoS can lead to a±30%\pm 30\%variation in the peak focal pressure and an axial focal shift of up to 2.0 mm. This axial shift is consistent with the broadening observed in the experimental data (Fig.2.10e). Additionally, the mechanical rotation of the skull fixture induces a coupled lateral translation (e.g.,∼10.6\sim 10.6mm for a6∘6^{\circ}rotation). This misregistration likely enlarged the focal spot during the experimental scan.Figure 2.11:

Validating HASA-ADAM repeatability across different skull anatomies. 2D acoustic field maps and the 3D focal beam of the uncorrected beam are compared with our topologically corrected projections across three distinct human skulls (S1, S2, S3). Our results show three uncorrected failure modes due to skull aberration and the recovery after topology-based correction. Patient-specific topologies eliminate spatial targeting errors (Segment 1), recover lost acoustic pressure (Segment 2), and reconstruct defocused beams (Segment 3).Table 2.5:Focal Performance: Aberrated vs. Corrected (Segments S1, S2, S3)MetricSegment 1Segment 2Segment 3Aberr.Corr.Aberr.Corr.Aberr.Corr.Peak Gain7.376.956.218.522.643.52Total Error (mm)4.761.523.822.311.541.50Lateral+0.00-0.25+0.50+0.25-0.25+0.00Elevational-0.25-1.50+0.50+0.50+0.25-0.00Axial-4.75+0.00-3.75-2.75-1.50+1.50Axial FWHM (mm)11.0812.2911.3111.2013.8513.34Lateral FWHM (mm)2.082.141.991.992.342.14Focal Vol. at -3 dB (mm3)9.911.18.68.8875.459.5Note: Aberr. and Corr. stands for Aberrated and Corrected cases, respectively.

A single successful focusing trial is insufficient for clinical validation. Human skulls show large topographical variance. Accounting for patient-specific aberrations is needed to generalize our topology-optimization-based skull correction. We expanded our 3D k-Wave simulations across three distinct human skull segments (S1, S2, and S3).

Without skull corrections, the acoustic beam suffers unpredictable failure modes (Table2.5). Each skull geometry introduces a somewhat different failure mode. Segment 1 causes spatial misalignment of the focus (4.76 mm off-target). Segment 2 drops the transmitted acoustic energy, and segment 3 results in defocusing of the focal volume into a large 875.4 mm3aberrating zone. Our topology optimization restores the focal quality for all the skull segments. For S1, it eliminates the axial shift and reduces the total spatial error by 68%. For S2, it recovers transmission efficiency (a 37% peak gain increase). For S3, the lens focuses the aberrated beam back into a confined focal spot of 59.5 mm3. This reduces off-targeting errors. Thus, our trans-skull holograms account for the skull’s geometry and ensure that acoustic energy goes to the targeted region as intended.(Fig.2.11).

## 2.4  Analysis of Experimental Discrepancies

## 2.4.1  Speed of Sound (SOS) Estimation

The longitudinal speed of sound in the ClearWhite v4 resin was determined using a through-transmission method. A reference signal was first acquired through a water path (baseline), followed by five measurements with the sample (thicknessd=15mmd=$15\text{\,}\mathrm{m}\mathrm{m}$) inserted into the path at different positions between the transducer and hydrophone.

The arrival time was determined using a peak-threshold detection method of the envelope of the signal using the Hilbert transform,E​(t)=|ℋ​(s​(t))|E(t)=|\mathcal{H}(s(t))|. The time shift (Δ​t\Delta t) was calculated as the difference between the sample and baseline arrival times. The speed of sound in the sample (cs​a​m​p​l​ec_{sample}) was estimated using the relative ToF, given the sample thicknessd=\qty​15​m​md=\qty{15}{mm}and the speed of sound in watercw​a​t​e​r≈\qty​1480​m/sc_{water}\approx\qty{1480}{m/s}:cs​a​m​p​l​e=(1cw​a​t​e​r−Δ​td)−1c_{sample}=\left(\frac{1}{c_{water}}-\frac{\Delta t}{d}\right)^{-1}(2.18)Figure 2.12:Speed of Sound estimation using through transmit measurementTable 2.6:Measured Time Shifts and Speed of Sound CalculationMeasurement PairTime Shift (μ\bm{\mu}s)Pair #14.5920Pair #24.6640Pair #34.4240Pair #44.6480Pair #54.4480Average Shift (Δ​t\Delta t)4.56±\pm0.11μ\bm{\mu}sEst. Sound Speed (ce​x​pc_{exp})2689±\pm54 m/s

The average time shift is4.56±\pm0.11μ\bm{\mu}s(mean±\pmstandard deviation). Thus, the longitudinal speed of sound in the sample material is2689±\pm54 m/swhich compares well with the standard literature value for the material (cd​e​s​i​g​n=\qty​2590​m/sc_{design}=\qty{2590}{m/s}). The percentage error is:%Error=|ce​x​p−cd​e​s​i​g​ncd​e​s​i​g​n|×100=|2689−25902590|×100≈3.8%\%\text{ Error}=\left|\frac{c_{exp}-c_{design}}{c_{design}}\right|\times 100=\left|\frac{2689-2590}{2590}\right|\times 100\approx 3.8\%(2.19)

The measured value deviated by approximately3.8%from the reference design value, which is relatively minor and falls near the estimated error bounds.

## 2.4.2  Lens Speed of Sound (SoS) Sensitivities: Longitudinal Shift and Wavefront Aberration

To investigate further discrepancies, we performed a sensitivity analysis on the Speed of Sound (SoS) parameters.

Letcd​e​sc_{des}be the speed of sound assumed in the optimization algorithm, andcr​e​a​lc_{real}be the actual speed of sound of lens material. The phase accumulationϕ\phithrough a thicknesshhis governed by the refractive contrast with the background medium (c0c_{0}):ϕr​e​a​l​(x,y)=ω​h​(x,y)​(1c0−1cr​e​a​l)\phi_{real}(x,y)=\omega h(x,y)\left(\frac{1}{c_{0}}-\frac{1}{c_{real}}\right)(2.20)

The optimization routine calculates the thicknessh​(x,y)=ϕt​a​r​g​e​t​(x,y)ω​(1c0−1cd​e​s)h(x,y)=\frac{\phi_{target}(x,y)}{\omega\left(\frac{1}{c_{0}}-\frac{1}{c_{des}}\right)}to achieve a target phaseϕt​a​r​g​e​t\phi_{target}based oncd​e​sc_{des}.
Substituting this into Eq.2.20, the actual phase realized in the experiment is:ϕr​e​a​l​(x,y)=ϕt​a​r​g​e​t​(x,y)×[1c0−1cr​e​a​l1c0−1cd​e​s]⏟γ\phi_{real}(x,y)=\phi_{target}(x,y)\times\underbrace{\left[\frac{\frac{1}{c_{0}}-\frac{1}{c_{real}}}{\frac{1}{c_{0}}-\frac{1}{c_{des}}}\right]}_{\gamma}(2.21)

γ\gammais a scalar constant representing the mismatch ratio. Whethercd​e​sc_{des}was chosen incorrectly orcr​e​a​lc_{real}shifted due to curing, the result is identical: the output phase map is the target phase map scaled byγ\gamma.
However, because our sub-megahertz acoustic holograms operate in the acoustically thick regime (as established in Section 2.3.2), this paraxial assumption is incomplete. At the microscopic level, a change in the physical SoS alters the refractive index contrast at the lens-water interface. According to Snell’s Law, this alters the internal angles of refraction for acoustic rays incident upon the steep topology of the lens. Consequently, the altered refraction angles simultaneously exacerbate the refractive walk-off effect.

## 2.4.2.1  SoS Mismatch Primarily Causes a Z-Axis Shift for Single Point Focusing

For point targetting however, the requirement for spatial coherence can be tempered. A lens SoS error shifts the hologram along the Z-direction instead of destroying it. In the paraxial approximation (Fresnel domain), a focusing element imparts a quadratic phase profile to the wavefront as follows:ϕt​a​r​g​e​t​(r)≈−k​r22​Fd​e​s\phi_{target}(r)\approx-\frac{kr^{2}}{2F_{des}}(2.22)

wherekkis the wavenumber, andFd​e​sF_{des}is the design focal length.

Owing to the SoS mismatch derived from Eq.2.21, the physical phase profile becomes:ϕr​e​a​l​(r)=γ⋅(−k​r22​Fd​e​s)=−k​r22​(Fd​e​s/γ)\phi_{real}(r)=\gamma\cdot\left(-\frac{kr^{2}}{2F_{des}}\right)=-\frac{kr^{2}}{2(F_{des}/\gamma)}(2.23)

This equation describes a perfect lens with anew focal lengthFn​e​wF_{new}:Fn​e​w=Fd​e​sγF_{new}=\frac{F_{des}}{\gamma}(2.24)

Consequently, the internal phase relationships that create the hologram shapes are preserved because the entire phase map is scaled uniformly. The hologram is coherent and forms atZ=Fn​e​wZ=F_{new}. However, the coherence is not destroyed; instead, the plane of image formation is displaced.

## 2.4.3  Skull Sound-speed (SOS) and Frequency variation

Errors in the the estimation of the of the speed of sound in the skull can lead to uncertainty in aberration correction. Because precise knowledge of skull acoustic properties is challenging to obtain under clinical conditions, it is important to understand how these uncertainties propagate through holographic reconstruction and effect on focusing accuracy. Although our main analysis assumes operation at the design frequency, real transducers have finite bandwidths and may operate at frequencies that deviate from the nominal design value. We also assessed the effect of deviation from the design frequency on focusing performance.

## Speed of Sound (SOS) variation:

A phase-only hologram is designed for a skull speedcdesign=2500c_{\text{design}}=2500m/s and average thicknessdskull=7d_{\text{skull}}=7mm. If the actual speed isc=cdesign​(1±0.15)c=c_{\text{design}}(1\pm 0.15), the one-way travel-time error isΔ​t=(1c0−1c)​dskull≈±0.15​dskullc0=±4.2×10−7​s,\Delta t=\left(\frac{1}{c_{0}}-\frac{1}{c}\right)d_{\text{skull}}\approx\frac{\pm 0.15d_{\text{skull}}}{c_{0}}=\pm 4.2\times 10^{-7}\text{s},(2.25)

At the design frequencyf0=1f_{0}=1MHz this corresponds to a phase slip|Δ​ϕ|=2​π​f0​|Δ​t|≈2.64​rad​(1510),|\Delta\phi|=2\pi f_{0}|\Delta t|\approx 2.64\text{rad}(151^{0}),(2.26)

Using simulations, we varied the speed of sound of the skull for two focusing configurations with phase-only lenses computed from the time of flight for a focus at 45 mm (F​#​0.75F\#0.75) and 60 mm (F​#​1.0F\#1.0) and observed the effect of peak amplitude and peak location variation. We observed approximately (±30%\pm 30\%) variation in the peak focal pressure, whereas the axial drift ranges were relatively minor (Fig2.13right). This is evident from the fact that SOS error (±15%\pm 15\%) results in a maximum shift in focus (2.0 mm for x45 configuration, Table2.7), which slightly exceeds the wavelength in water at 1 MHz (1.5 mm). For applications that require high-precision targeting, this can still be a significant source of error, and methods to account for it should be considered.Figure 2.13:Peak pressure and peak location versus SOS error (±15%\pm 15\%) for both nominal foci.Table 2.7:Peak Amplitude and Location Statistics for Two ConfigurationsConfigurationMinMaxRangeMeanStd DevPeak Amplitude (Norm.)x450.7371.3520.6151.0160.200x600.7351.2990.5641.0270.197Peak Location (mm)x45-0.2501.7502.0000.5000.685x60-1.2500.5001.750-0.2120.548

## Frequency variation:

To keep our analysis simple, we assume a homogenous medium. A planar aperture is driven with a static phase patternϕc​(r)=−2​π​f0c​(z02+r2−z0),\phi_{c}(r)=-\frac{2\pi f_{0}}{c}\left(\sqrt{z_{0}^{2}+r^{2}}-z_{0}\right),(2.27)

wrapped into the range[0,2​π)[0,2\pi). Applying the same pattern at a new frequency,ffproduces an effective time delayτ′​(r)=ϕc​(r)2​π​f=f0f​z02+r2−z0c,\tau^{\prime}(r)=\frac{\phi_{c}(r)}{2\pi f}=\frac{f_{0}}{f}\frac{\sqrt{z_{0}^{2}+r^{2}}-z_{0}}{c},(2.28)

Therefore, the quadratic phase coefficient becomes(f0/f)(f_{0}/f)times smaller. The new on-axis focusz​(f)z(f)satisfiesz​(f)=f0f​z0,z(f)=\frac{f_{0}}{f}z_{0},(2.29)

Using simulations, we varied the frequency of excitation for two focusing configurations with phase-only lenses computed from the time of flight for a focus at 45 mm (F​#​0.75F\#0.75) and 60 mm (F​#​1.0F\#1.0) and observed the effect on focusing. The wavelength changes scale the beamwidth and depth-of-field inversely withff; a high frequency tightens and attenuates the beam, whereas a low frequency broadens and deepens it, moving the focus away from its intended position (Eqn. S5). The analysis suggests that for±5%\pm 5\%frequency shifts (which is the range of our registration trial withf±Δ​f/2f\pm\Delta f/2the max shift is comparable to 2-3 wavelengths in water at 1 MHz (Fig2.14bottom right and Table2.8).Figure 2.14:Peak pressure and location versus frequency error (±50%\pm 50\%) for both nominal foci.Table 2.8:Peak Amplitude and Location StatisticsConfigurationMinMaxRangeStd DevStd DevPeak Amplitude (Norm.)x450.8501.1730.3231.0030.112x600.8591.2820.4231.0590.147Peak Location (mm)x45-2.7504.5007.2500.5912.432x60-3.2503.2506.5000.0452.159

## 2.4.4  Limitations and Failure Modes of the HASA-ADAM Framework

The HASA-ADAM framework relies on several physical and mathematical approximations. We first isolate its primary failure modes to define the operational bounds of this method: (1) compressional amplitude apodization and shear mode conversion, driven by steep topographical gradients in the free field, and (2) internal reflections and phase discontinuities induced by the highly heterogeneous human skull.

## 2.4.4.1  Free-Field Limitations: Compressional Apodization and Shear Mode Conversion

Projecting complex holograms (e.g., the GT Bee target) or tight focal spots requires steering acoustic energy at large off-axis angles. The principle of superposition requires that every point across the active transducer aperture contributes to the pressure field at the target plane. For an acoustic ray originating at a lateral aperture positionxxand targeting a focal point at depthZZ, the required steering angle relative to the optical axis isθ=arctan⁡(|x|/Z)\theta=\arctan(|x|/Z).

To steer via refraction from the solid lens (cl​e​n​sc_{lens}) into the water medium (cwc_{w}), the lens surface must possess a specific topographical slope. Letα\alphabe the angle of the surface normal relative to the incident longitudinal wave; as per Snell’s law, the required slope (|∇h|=tan⁡α|\nabla h|=\tan\alpha) is governed by:tan⁡α=sin⁡θcos⁡θ−cw/cl​e​n​s\tan\alpha=\frac{\sin\theta}{\cos\theta-c_{w}/c_{lens}}(2.30)

This relationship reveals two failure modes at high numerical apertures. Decreasing the focal depthZZincreases the required steering angle rapidlyθ\theta. This forces the optimizer to generate steep slopes at the lens periphery.

1. Compressional Fluid Limit (Fresnel Apodization):Asθ\thetaincreases, the denominator in Eq.2.30approaches zero. This imposes an absolute refractive limit:θm​a​x=arccos⁡(cw/cl​e​n​s)\theta_{max}=\arccos(c_{w}/c_{lens}). For our 3D-printed lens (cl​e​n​s≈2590c_{lens}\approx 2590m/s) in water (cw≈1500c_{w}\approx 1500m/s),θm​a​x≈54.6∘\theta_{max}\approx 54.6^{\circ}. Our 1D analysis (Fig.2.15a) shows that moving the focal plane toZ=20Z=20mm pushes peripheral rays above this limit. This makes single-interface refraction impossible. Steep incidence angles trigger additional amplitude attenuation via Fresnel reflection. Because the one-way HASA forward propagator forces a reflection coefficient of zero (R=0R=0), it overestimates the forward energy transmission through the aberrating layer(see appendixA.1for derivations). In other words, the portion of the lens at the periphery becomes inactive and does not contribute to the hologram at the focal plane. This reduces the effective numerical aperture, which is also known as apodization, leading to a loss of peak focal pressure.

2.Shear Limit:Another mode of failure is the conversion of compressional waves to shear mode: High oblique incidence due to steeper slopes (α\alpha) triggers substantial energy partitioning. Above the critical angle (θc≈arcsin⁡(cw/cs,l​e​n​s)≈30∘\theta_{c}\approx\arcsin(c_{w}/c_{s,lens})\approx 30^{\circ}), a large fraction of the incident acoustic energy converts into transverse shear waves (S-waves). HASA, as a scalar fluid model (μ=0\mu=0), cannot account for shear-mode conversion. We define a geometricFigure of Merit (FOM)to quantify this limitation. It is defined as the percentage of the transducer aperture that requires a lens slope to exceed the critical shear-conversion threshold. As the target plane is moved toZ=20Z=20mm, this FOM increases at the periphery (Fig.2.15b), mapping the spatial region where the fluid-based optimizer degrades. The result is that at extreme steering, the effective aperture that would constructively interfere is reduced, and unaccounted-for shear-mode energy leads to phase decorrelation.Figure 2.15:Combined free-field failure modes at high numerical apertures.(a) Compressional Limits (1D):Focusing rays to a close focal plane (Z=20Z=20mm) forces peripheral steering angles to approach the refractive limit (θm​a​x=54.6∘\theta_{max}=54.6^{\circ}). The steeper lens slope causes a drop in transmitted power (Fresnel Apodization). The HASA algorithm erroneously models this as 100% transmission.(b) Shear Limits (2D FOM):Geometric incidence analysis shows the percentage of the aperture exceeding the shear critical angle (θc≈30∘\theta_{c}\approx 30^{\circ}) for every point on the target plane. Moving the target plane closer increases the shear risk at the periphery. This reduces the effective aperture.

## 2.4.4.2   Quantification of Free-Field Limits

Let’s focus on the fidelity of holographic reconstruction results from the free-field optimizations. We evaluated them using full-wave simulations (k-wave toolbox[78]) at multiple focal depths (Z=20,45,Z=20,45,and6060mm), spatial resolutions (point spacings from 2.5 to 40.0 mm), and target geometries (isolated 4-point targets and the continuous GT Bee pattern).

The key insight from all the 2D optimization configurations is that near-field focusing (Z=20Z=20mm) forces the optimizer into more challenging steering regimes for our algorithm. This results in structural degradation (i.e., drop in correlation coefficient) and is consistent with refractive limits and Fresnel apodization. Quantitative analysis at this depth showed the highest overall error (MSE>0.34>0.34) and the weakest structural definition (Correlation≈0.534\approx 0.534for the 4-point target). Moving the focal plane deeper to4545mm and6060mm relaxed the required steep steering angles. A deeper focusing plane reduces amplitude apodization and mode-conversion limits and results in a sharp recovery of image fidelity, increasing correlation by approximately0.200.20for both target patterns. We also see a lower free-field MSE of0.1550.155atZ=60Z=60mm (Fig.2.16). The deterioration we observed does not necessarily pose a strict limitation in a clinical setting; we can always steer the transducer so that the focal plane is in the far field, or use smaller-aperture transducers.Figure 2.16:Empirical validation of compressional limits. Both the 4-point and GT Bee targets show improved correlation as the focal plane moves deeper (from2020mm to6060mm). The degradation atZ=20Z=20mm aligns with the failure modes. The peripheral rays exceed the absolute refractive limit. They undergo significant Fresnel amplitude apodization and unmodeled shear-mode conversion.

Another key factor is the portion of the aperture covered by the hologram in the focal plane. This decides whether the resulting pattern is a point target or a 2D image at two extremes.
Evaluating the effect of spacing between four-point targets across these depths revealed a sensitivity profile for effective aperture limits.

At the optimalZ=45Z=45mm focal plane, performance peaked at a20.020.0mm point spacing (achieving an absolute peak system correlation of0.8350.835), but degraded at tighter spacings (<5.0<5.0mm). This is primarily due to acoustic diffraction. At wider spacings (40.040.0mm) due to peripheral amplitude loss from extreme off-axis steering, the performance also dropped.(Fig.2.17). The deeperZ=60Z=60mm plane provided greater tolerance to spatial variation, although it did not achieve the absolute peak resolution of the4545mm plane. The reduced steering angles nonetheless allowed the optimizer to maintain a stable correlation profile (∼0.771\sim 0.771to0.7740.774) across point spacings from5.05.0mm to40.040.0mm. Thus, it effectively avoided near-field failure modes.Figure 2.17:Spacing sensitivity across focal depths. The4545mm focal plane show a distinct performance curve, peaking optimally at a2020mm point spacing (Correlation0.8350.835). The deeper6060mm plane shows high focal-plane tolerance, which has a flat performance profile across a wide range of target distributions. This confirms that the relaxed steering angles keep the rays within the high-transmission regime.

## 2.4.4.3  Transcranial Limitations in HASA-ADAM Optimization

The HASA wave propagator is based on a parabolic (one-way) approximation of the heterogeneous Helmholtz equation. The second-order axial spatial derivative is neglected in the heterogeneous Helmholtz equation:∂2P∂z2≈0\frac{\partial^{2}P}{\partial z^{2}}\approx 0This assumes that backscattering effects can be neglected. But, the large difference in acoustic impedance between the water coupling medium (Zw≈1.5Z_{w}\approx 1.5MRayl) and the dense cortical bone (Zb≈5.5−6.0Z_{b}\approx 5.5-6.0MRayl) means that a reflection coefficient (RR) is large:R=Zb−ZwZb+Zw≈0.57R=\frac{Z_{b}-Z_{w}}{Z_{b}+Z_{w}}\approx 0.57(2.31)

This shows that aboutR2≈32%R^{2}\approx 32\%of the incident acoustic energy is reflected back. The multi-layered structure of the skull traps sound waves, producing complex reverberation within it. The one-way approximation in the HASA model imposesR=0R=0. It overestimates transcranial transmission and fails to account for phase decorrelation caused by internal standing waves. Additionally, the HASA convolution step (Λ∗P\Lambda*P) is derived under the slowly varying envelope approximation (also known as WKB approximation, see appendixA.2for details).[80]. This requires the spatial variation of the medium’s speed of sound to change slowly relative to the acoustic wavelength:1k0​|∇cc|≪1\frac{1}{k_{0}}\left|\frac{\nabla c}{c}\right|\ll 1(2.32)

The speed of sound discontinuously jumps from∼1480\sim 1480m/s to over25002500m/s within a sub-millimeter distance at the water-skull boundary. This spatial step-function violates the continuity assumption, introducing spectral leakage and artificial phase accumulation errors during HASA’s spatial Fourier transforms. The strong heterogeneity of the skull may break the assumption on which the HASA model was built.

The skull’s geometry may also cause shear conversion. Due to local anatomical curvature, approximately 50% of the illuminated skull surface presents an incidence angle exceeding the critical threshold (θc≈30∘\theta_{c}\approx 30^{\circ}) even under perfect registration (Chapter 3). Thus, the projection of high-spatial-frequency patterns through a strongly aberrating skull imposes a hard boundary condition. The fluid-based optimizer used here degrades due to multiple reflections, spectral leakage, phase discontinuities, and shear errors.

Let’s evaluate how focal depth and transcranial propagation interact using the previous example of four-point targets. Under Free-Field conditions, the optimizer resolves focal spots effectively atZ=45Z=45mm. The beam naturally widens at deeper planes. However, introducing the skull boundary degrades correlation across all depths. The skull blurs the focus. It also introduces additional sources of error. The optimal 45 mm depth focal plane case retains a fraction of its original shape (Correlation∼0.50\sim 0.50). At shallower focal planes(20 mm), the effects of near-field blurring and skull-induced phase aberrations reduce the correlations drastically (Fig.2.19). This indicates that the phase distortions generated by the cranial barrier not only degrade resolution but also penalize targets positioned too close to the internal bone interface. These failure modes are worst when projecting complex targets. This leads to a major drop in correlation of the GT Bee pattern (Fig.2.18).Figure 2.18:Transcranial correlation degradation of the high-spatial-frequency GT Bee target pattern. (Top) Simulated acoustic pressure fields demonstrating the target reconstruction in FreeField (FF) versus TransSkull (TS) conditions across varying axial depths (Z=20,45,Z=20,45,and6060mm). The Fluid-based HASA-ADAM optimizer accurately predicts the complex pattern in a homogeneous medium; focal blurring and distortion occur when it passes through the skull. (Bottom) correlation metrics highlighting the significant drop in fidelity. This degradation visualizes the failure of the HASA model’s one-way parabolic and slowly varying envelope approximations when subjected to the heterogeneous skull for complex 2D targets.Figure 2.19:Acoustic field reconstruction and structural fidelity for the 4-points target with a fixed 10.0 mm point spacing. (Top and Middle) Simulated 2D maximum pressure planes (pm​a​xp_{max}) demonstrating target reconstruction in FreeField versus TransSkull conditions at axial depths ofZ=20,45,Z=20,45,and6060mm. (Bottom) Quantitative trends comparing the correlation of the simulated fields against the ideal target. The Free Field condition demonstrates excellent focal fidelity that stabilizes at deeper planes (Correlation>0.77>0.77); the introduction of the skull causes phase distortion and signal attenuation, particularly in the near-field (Z=20Z=20mm).

## 2.5  Discussion

We showed that the HASA-ADAM framework generates acoustically thick lens topologies that account for thickness-dependent effects, including amplitude errors, scattering, and edge diffraction. HASA-ADAM achieves this by implementing the physics of wave propagation within the lens topology. Such consideration is more important at sub-MHz frequencies, where the thin-element approximation (i.e., treating the lens as an ideal flat 2D phase screen) fails. Using HASA-ADAM, we achieve improved performance, including reduced sidelobes during trans-skull focusing (Fig.2.10) compared to optimized phase-only methods. This capability is an improvement in acoustic holography, enabling the generation of holographic fields with fidelity that thin-element-lens-based systems and commercially viable phased arrays can not achieve (Fig.2.4). The framework, as such, can also be extended to use with dense or sparse phased arrays[81]for transcranial applications.

We have used automated differentiation with the ADAM optimizer to reduce the risk of getting stuck in local minima and maintain robust, uniform focal accuracy. But the wave propagator has limitations that define the operational boundaries of our HASA-ADAM formulation. The underlying wave propagator for HASA-ADAM is built on the one-way wave equation. This means it does not account for multiple internal reflections (backscattering) or shear mode conversions within the cranial bone. For relatively simple targets, such as single-point focusing, the acoustic energy is steered at near-normal incidence, thereby minimizing shear-mode conversion at the water-lens interface. In these cases, the performance of HASA is only limited by diffraction. Projecting complex holographic patterns (e.g., the GT logo) through a highly aberrating skull, on the other hand, requires higher spatial frequencies and steeper angular steering gradients. As oblique acoustic rays incident on the skull near or beyond the critical angle (θc≈30∘\theta_{c}\approx 30^{\circ}), a substantial percentage of energy is diverted into unmodeled shear waves. HASA-ADAM relies on a scalar fluid formulation and is blind to these solid-mechanics phenomena. It cannot pre-compensate for them. This represents a failure mode that bounds the fidelity of highly complex holographic projections through thick cortical bone.

In terms of computational speed, HASA-ADAM bridges the gap between computationally intensive methods such as time reversal[71,82]and trained deep learning frameworks[83,84,85]that are opaque and reliant on extensive training datasets. While methods such as MMDM[70]offer high accuracy by including reflections (which HASA currently neglects), HASA’s formulation is highly amenable to automatic differentiation, offering a significant computational advantage for iterative optimization. It provides a favorable balance of speed and accuracy for the forward optimization problem. Although directly optimizing the thickness is more challenging than phase optimization and thus requires approximately twice as long to converge (∼\sim15 min atλ/6\lambda/6discretization for 500 iterations), with improved tuning of the hyperparameter of optimization and initial conditions, the convergence can be further accelerated.
Likewise, hybrid strategies that merge the speed of deep learning methods with HASA’s accuracy and interpretability of wave propagation of HASA with GPU acceleration can further mitigate the computational cost associated with theO​(N2​log⁡N)O(N^{2}\log N)scaling, allowing real-time implementations, which can be desirable in some applications[86,87].

Despite the remarkable performance of the proposed framework for designing holographic lens topologies, we observed discrepancies between the optimization results, k-wave simulations, and hydrophone scans, especially for high-fidelity holograms in the free field (Fig.2.4c and d). As investigated in Section 5, these discrepancies primarily originated fromelastic mode conversion within the lens materialand uncertainties in the material properties of the 3D-printed lens. First, the reported 2590 m/s group velocity[77]may not accurately represent the 3D-printed sample (using Clear White v4 resin) owing to curing-induced density variations and internal stresses. Characterization of the specific sample used and subsequent updating of the simulations largely reconciled these differences. Second, the manufacturing tolerances of±\pm0.05-0.1 mm (∼\sim5% of thickness)[88]may introduce additional timing errors. Another potential source of error is related to variations in the speed of sound (e.g., from the lens to the water), which, for the current HASA implementation, cannot be very high relative to the wavelength[72].

Furthermore, the current HASA implementation does not account for absorption (see Methods), which may affect the optimization accuracy, particularly for highly attenuating media. We acknowledge this as a limitation that may be addressed in future iterations. Finally, understanding the impact of multiple reflections, which are neglected in the currently implemented HASA algorithm, and their role in optimization convergence[89]may enable further improvements in hologram quality. Despite these potential sources of error, the HASA-ADAM framework delivers a balanced approach to scalable, rapid, and accurate hologram design. It also accommodates patient-specific skull variations, enabling transcranial targeting of specific brain regions during treatment planning.

## 2.6  Conclusions

This chapter resolves a major bottleneck in acoustic hologram design. We established a framework for volumetric lens topology optimization that overcomes the limitations of the phase-based thin-film approximation to generate high-fidelity, patient-specific lenses in the sub-megahertz regime. This approach yields four primary contributions:


Failure Thin-Element Approximation in the Thick-Lens Regime:We showed that at frequencies needed for transcranial applications (∼\sim1 MHz or lower), acoustic holograms operate in an acoustically thick regime where phase-to-thickness conversions fail. The resulting refractive walk-off and transverse energy migration degrade holographic fidelity. Our HASA-ADAM topology optimizer pre-compensates for these volumetric diffraction effects during the design.

Shear Mode Conversion:We postulated the mechanisms driving the background acoustic haze observed in our 2D complex holographic experiments.

Full-wave elastic ablation studies indicated that this haze results directly from longitudinal-to-shear mode conversion at the lens’s steep interfaces. It causes phase aberration and refractive steering. Actively modeling this shear wave propagation dropped the experimental reconstruction error by 29.1%.

Validation of Patient-Specific Transcranial Aberration Correction:We showed the robustness and repeatability of the HASA-ADAM framework across highly variable human skull segments (S1, S2, and S3). In every case, the patient-specific topologies improved the dominant acoustic failure modes. The lenses corrected severe spatial misalignments (reducing targeting error by 68% in S1), recovered lost acoustic pressure (driving a 37% increase in peak gain in S2), and forced diffused energy back into tightly confined focal spots.

Operational Optimization Boundaries:We mapped the failure modes of our HASA-ADAM holographic optimization. We conclude that forcing the system to generate high numerical apertures (e.g.,Z=20Z=20mm) triggers Fresnel apodization and mode conversion. Finally, we bounded the framework’s transcranial limitations to unmodelled multiple reflections (R≈0.57R\approx 0.57) and violations of the slowly varying envelope approximation.

## Chapter 3Hologram Registration00footnotetext:An earlier version of the work presented in this chapter is available as a preprint on arXiv (https://arxiv.org/abs/2508.07103).[57]

## 3.1  Introduction

Our ability to reconfigure the potentially disruptive technology of acoustic holography for biomedical applications such as transcranial ultrasound also depends on our ability to accurately register the holographic lens to the patient’s anatomy, orientation, and position relative to the transducer/lens plane[90,64]. For instance, complex hologram designs and pressure field topologies, which require a higher operation frequency (≥0.7\geq 0.7MHz) and skull-compensating lens topologies, are very sensitive to lens-skull misalignment[29]. Hence, high-quality registration (i.e., sub-wavelength accuracy,<<1.5 mm at 1 MHz) is required to preserve the fidelity and targeting accuracy. Unfortunately, current non-MRI-based registration methods (e.g., standard neuronavigation) typically achieve an accuracy of only∼\sim2 mm, which can lead to targeting errors of a few millimeters (i.e., 1–2 wavelengths) and reduced performance[69,91,45,92]. Therefore, robust and accurate registration strategies that can accurately align the lens to the patient’s skull anatomy are critical for designing cost-effective and portable transcranial ultrasound (TUS) systems for high-precision (i.e., subwavelength) neurointerventions.

To address this critical challenge of registration, we hypothesize that nonlinear acoustic effects can be leveraged for noninvasive lens–skull registration.[93]The hypothesis was tested through modelling and experiment. A parametric array (PA) signal, the low-frequency tone produced when two high-frequency beams mix nonlinearly[94,95], serves as the registration metric. We investigations suggest that a misaligned (aberrated) lens augments the finite-amplitude wave propagation effects within a highly nonlinear skull, giving rise to a strong PA signal that can penetrate the skull with minimal losses. Thus, minimizing the PA signal leads to an effective acoustic feedback mechanism for noninvasively aligning the holographic lens with the skull.

In the following sections, we summarize the rationale and theory behind hologram registration using nonlinear PA feedback, followed by simulation and experimental results, as well as a sensitivity analysis. They help us explore the limitations of this method and draw key insights for clinical applications.

## 3.2  Methods

## 3.2.1  Mechanism of Lens Registration

To establish the theoretical basis for our registration strategy, we modeled the interaction of finite-amplitude ultrasound waves within a medium of spatially varying nonlinearity. We utilize the Westervelt equation to model the generation of the difference frequency component, where the finite-amplitude primary waves act as a volumetric driving source.

## The Nonlinear Source Term

Under the quasilinear approximation, the secondary difference frequency fieldpΔ​f​(𝐫,t)p_{\Delta f}(\mathbf{r},t)is driven by a virtual volumetric source density,SN​LS_{NL}:∇2pΔ​f−1c02​∂2pΔ​f∂t2=−β​(𝐫)ρ0​c04​∂2∂t2​⟨pp​r​i​m​a​r​y2⟩⏟SN​L​(𝐫,t)\nabla^{2}p_{\Delta f}-\frac{1}{c_{0}^{2}}\frac{\partial^{2}p_{\Delta f}}{\partial t^{2}}=-\underbrace{\frac{\beta(\mathbf{r})}{\rho_{0}c_{0}^{4}}\frac{\partial^{2}}{\partial t^{2}}\langle p_{primary}^{2}\rangle}_{S_{NL}(\mathbf{r},t)}(3.1)

Where:
- •

β​(𝐫)\beta(\mathbf{r})is the spatially dependent coefficient of nonlinearity.
- •

⟨pp​r​i​m​a​r​y2⟩\langle p_{primary}^{2}\rangleis the envelope of the squared primary pressure field.
- •

SN​LS_{NL}represents the local strength of nonlinear generation.

The amplitude of the parametric signal is proportional to the volume integral of the source term over the interaction domainVV:PΔ​f​(𝐫o​b​s)∝∫Vβ​(𝐫)ρ0​c04​|pp​r​i​m​a​r​y​(𝐫)|2​G​(𝐫,𝐫o​b​s)​𝑑VP_{\Delta f}(\mathbf{r}_{obs})\propto\int_{V}\frac{\beta(\mathbf{r})}{\rho_{0}c_{0}^{4}}\left|p_{primary}(\mathbf{r})\right|^{2}G(\mathbf{r},\mathbf{r}_{obs})\,dV(3.2)

## The Material Contrast Mechanism

To determine the sensitivity of this method, we analyzed the significant contrast in the nonlinearity parameterβ\betabetween the skull bone and the surrounding soft tissue.
- •

Soft Tissue / Water:β≈3.5−4.5\beta\approx 3.5-4.5.
- •

Skull Bone:β≈188\beta\approx 188(derived fromB/A≈374B/A\approx 374).

Becauseβs​k​u​l​l≫βt​i​s​s​u​e\beta_{skull}\gg\beta_{tissue}, the integral in Eq.3.2is primarily dominated by the volume of the skull illuminated by high-intensity ultrasound.

Two limiting cases bound the expected PA emission:
- 1.

Misaligned:In this state, the lens no longer corrects the skull’s aberration profile. Primary-beam energy scatters and reverberates inside the porous bone (highβ\beta). The productβ​(𝐫)⋅|pprimary|2\beta(\mathbf{r})\cdot|p_{\text{primary}}|^{2}is large throughout the bone volume, so the skull radiates a strong PA signal.
- 2.

Aligned:Phase aberration due to the skull are compensated; constructive interference occursbeyondthe skull. Primary energy propagates through the bone quickly and focuses in low-β\betabrain tissue. The overlap integral (Eq.3.2) is minimized under this condition.

## 3.2.2  Practical Implementation: Double-Layer Propagation

## Frequency-Dependent Transmission

For external detection, the PA signal must cross the distal skull layer. The primary beam (f0≈1f_{0}\approx 1MHz) after the focal plane attenuates heavily on this second pass (α∝fb\alpha\propto f^{b}), but the 100 kHz difference frequency crosses the distal skull with negligible loss.
- •

Atf0=1f_{0}=1MHz, attenuation is high (∼15\sim 15dB/cm). The primary beam was effectively filtered out by the exit layer.
- •

AtΔ​f=100\Delta f=100kHz, attenuation is negligible (∼0.15\sim 0.15dB/cm).

Therefore, the PA signal generated at the entry layer propagates through the brain and exits the skull layer with minimal energy loss.

## 3.2.3  Volumetric Analysis of Energy Trapping

To rigorously confirm that the registration signal arose from the acoustic energy trapped within the skull, we performed a 3D volumetric analysis of the primary pressure fields obtained from the k-Wave simulations.

The nonlinear source termSN​LS_{NL}is proportional to the square of the primary pressure inside the bone (SN​L∝βs​k​u​l​l​|pp​r​i​m​a​r​y|2S_{NL}\propto\beta_{skull}|p_{primary}|^{2}). We defined the skull interaction volume via the acoustic impedance map (c>1700c>1700m/s) and calculated theIntegrated Source Potential(Et​r​a​p​p​e​dE_{trapped}) specifically within the bone matrix as follows:Et​r​a​p​p​e​d=∫Vs​k​u​l​l|pp​r​i​m​a​r​y​(𝐫)|2​𝑑VE_{trapped}=\int_{V_{skull}}|p_{primary}(\mathbf{r})|^{2}\,dV(3.3)

## 3.2.4  Calculation of Elastodynamic Energy Partitioning and Parametric Amplification

To assess whether mode conversion played a significant role in the angular sensitivity of the acoustic feedback, we calculated the elastodynamic energy partitioning and parametric amplification within the solid skull matrix.

Geometric Incidence and Critical Angle.The threshold for longitudinal wave transmission at the fluid-bone interface is analytically quantified using Snell’s law for elastic media. Assuming that the speed of sound in the water coupling medium iscw≈1480c_{w}\approx 1480m/s, and the longitudinal speed of sound in the cortical bone iscb≈2800c_{b}\approx 2800m/s, the critical angleθc\theta_{c}isθc=arcsin⁡(cwcb)≈arcsin⁡(0.528)≈31.9∘\theta_{c}=\arcsin\left(\frac{c_{w}}{c_{b}}\right)\approx\arcsin(0.528)\approx 31.9^{\circ}(3.4)

For computational thresholding in the Shear Mode Risk analysis, this value was approximated as30∘30^{\circ}.

Stress Tensor and Energy Densities.In the k-wave elastic solver, the macroscopic scalar pressurePPis derived exclusively from the trace of the stress tensor (normal stresses):P=−12​(σx​x+σy​y)P=-\frac{1}{2}(\sigma_{xx}+\sigma_{yy})(3.5)

To rigorously quantify the elastodynamic partitioning of acoustic energy within a solid skull matrix, the total energy density was separated into kinetic and potential components. TheKinetic Energy Density(wkw_{k}), which captures the total particle motion (including both compressional and shear contributions), is defined via the peak particle velocity vector𝐮=(ux,uy)\mathbf{u}=(u_{x},u_{y}):wk​(𝐫)=12​ρ​(𝐫)​(|ux​(𝐫)|2+|uy​(𝐫)|2)w_{k}(\mathbf{r})=\frac{1}{2}\rho(\mathbf{r})\left(|u_{x}(\mathbf{r})|^{2}+|u_{y}(\mathbf{r})|^{2}\right)(3.6)

whereρ​(𝐫)\rho(\mathbf{r})denotes the local mass density. ThePotential Energy Density(wpw_{p}), representing the energy stored purely in volumetric compression, is approximated using the peak scalar pressurePP:wp​(𝐫)=12​P​(𝐫)2ρ​(𝐫)​cL​(𝐫)2w_{p}(\mathbf{r})=\frac{1}{2}\frac{P(\mathbf{r})^{2}}{\rho(\mathbf{r})c_{L}(\mathbf{r})^{2}}(3.7)

wherecLc_{L}is the speed of longitudinal sound. Because pure shear waves are isochoric, their energy is captured almost exclusively by the kinetic termwkw_{k}. The total trapped energy,Et​o​t​a​lE_{total}, is obtained by volume-integrating these densities over the spatial domain of the skull mask,Ωs​k​u​l​l\Omega_{skull}:Et​o​t​a​l=∑𝐫∈Ωs​k​u​l​l(wk​(𝐫)+wp​(𝐫))​Δ​x​Δ​yE_{total}=\sum_{\mathbf{r}\in\Omega_{skull}}\left(w_{k}(\mathbf{r})+w_{p}(\mathbf{r})\right)\Delta x\Delta y(3.8)

Derivation of thec−3c^{-3}Scaling in Bone.The difference-frequency pressurepd​fp_{df}is derived from the Westervelt equation source termSS[94,96]:∇2pd​f−1c2​∂2pd​f∂t2=−βρ​c4​∂2pp2∂t2⏟S\nabla^{2}p_{df}-\frac{1}{c^{2}}\frac{\partial^{2}p_{df}}{\partial t^{2}}=-\underbrace{\frac{\beta}{\rho c^{4}}\frac{\partial^{2}p_{p}^{2}}{\partial t^{2}}}_{S}(3.9)

The local source strength scales as:S∝β⋅Δ​ω2ρ​c4S\propto\frac{\beta\cdot\Delta\omega^{2}}{\rho c^{4}}(3.10)

In the absorption-limited case (common in cortical bone), the total accumulated pressurePd​fP_{df}is the integral of the source over the effective interaction lengthLe​f​f=1/αL_{eff}=1/\alpha:Pd​f≈∫0∞S​e−α​z​𝑑z=SαP_{df}\approx\int_{0}^{\infty}Se^{-\alpha z}dz=\frac{S}{\alpha}(3.11)

Given that the absorption coefficientα\alphain bone roughly scales with1/c1/cfor a fixed frequency[97], the total efficiencyη\etascales as:η∝1c4⋅c=1c3\eta\propto\frac{1}{c^{4}}\cdot c=\frac{1}{c^{3}}(3.12)

Therefore, hypothetically, for shear waves (cs≈1400c_{s}\approx 1400m/s) vs. longitudinal waves (cl≈2800c_{l}\approx 2800m/s):ηsηl=(clcs)3=23=8\frac{\eta_{s}}{\eta_{l}}=\left(\frac{c_{l}}{c_{s}}\right)^{3}=2^{3}=8(3.13)

This derivation suggests that if fast longitudinal waves are mode-converted into slow shear waves, an approximately 8-fold generation efficiency boost couldpotentiallyoccur. However, we present this strictly as an exploratory hypothesis to help explain possible experimental discrepancies, rather than a definitively validated physical mechanism.

## 3.2.5  Robustness and Artifact Analysis Methodology

Robustness to Hydrophone Placement:To determine whether the registration metric is robust to the positioning of the receiving hydrophone, a requirement for clinical translation, we evaluated its spatial invariance. We simulated a finite aperture receiver (e.g., piston hydrophone or ultrasound transducer) scanned across a region of interest40−10040-100mm axially and±25\pm 25mm laterally behind the skull. To quantify the benefits of using larger detectors, we performed a parameter sweep by varying the receiver aperture from 2 mm to 30 mm.

Pseudo-Sound Quantification:To verify that the measured low-frequency signals originated from true parametric generation within the medium rather than from the nonlinear transfer function of the hydrophone, we quantified the contribution of pseudo-sound. Pseudo-sound arises from the nonlinearity of the hydrophone (e≈m​p+η​p2e\approx mp+\eta p^{2}). We took advantage of near-field measurements taken at the focus, 60 mm from the focus, and 120 mm from the focus to quantify and isolate pseudo-sounds based on how true difference-frequency waves scale differently with range.

Intrinsic Skull Nonlinearity vs. Microbubble Artifacts:To investigate whether the observed Difference Frequency (DF) stemmed from the intrinsic classical cumulative nonlinearity of the bone matrix rather than artifactual resonant bubble nonlinearity from trapped gas, we analyzed the spectral content predicted by two competing models of nonlinearity. Degassed human skull samples were submerged in a water tank. A bichromatic excitation pulse (f1,f2≈1f_{1},f_{2}\approx 1MHz,Δ​f≈100\Delta f\approx 100kHz) was transmitted through the skull, and the resulting acoustic field was measured using a hydrophone along the propagation axis (zz). A system governed by classical modular nonlinearity produces only integer linear combinations of input frequencies, whereas microbubble artifacts are characterized by bifurcation and the emission of subharmonics (f0/2f_{0}/2).

Simulation of Intracranial Trapped Gas:We simulated the effect of trapped gas within the porous structure of the skull on PA generation, to evaluate the robustness of the proposed acoustic lens system against realistic postoperative conditions (e.g., pneumocephalus). We used the k-wave toolbox to solve nonlinear coupled wave equations. A morphological void-filling algorithm assigned the acoustic properties of air to a specified volume fraction (ϕg​a​s\phi_{gas}) of the voids. The source was driven by bi-frequency excitation to generate a difference frequency (Δ​f=100\Delta f=100kHz) at the target depth.

## 3.3  Simulation and Experimental Results

## 3.3.1  Skull-compensating lens misalignment augments nonlinear wave propagation and parametric array signal

We observed in FigureFig.˜2.10that transcranial focusing at 1 MHz is highly sensitive to registration errors. We evaluated whether non-linear wave propagation through the human skull could serve as an active acoustic feedback mechanism to indicate the status of skull-lens alignment. Briefly, the parametric array effect is a nonlinear wave propagation effect[94], where two (primary) high-frequency sound beams of finite amplitude interact to produce (secondary) sum- and difference-frequency beams. The strength of the difference frequency|pΔ​f||p_{\Delta f}|, here termed the parametric array signal (PA signal), which has several unique properties, including high directionality and penetration through the skull, is proportional to the medium’s nonlinearity parameterβ\beta, the square of the primary beam amplitudepf1,2p_{f_{1,2}}, and their propagation length[hamilton1997nonlinear]. Considering the characteristics of the PA signal, we hypothesized that skull-compensating lens misregistration (i.e., suboptimal aberration correction) can affect the amplitude of|pΔ​f||p_{\Delta f}|which once detected and quantified (e.g., using a hydrophone) can provide a real-time feedback mechanism to noninvasively align the holographic lens to the patient’s skull (Fig.3.2a). Registration is performed before sonication by adjusting the lens pose until the PA signal is minimised.Figure 3.1:Process flow chart for trans-skull hologram registration in a clinical setting.We mount a 3D-printed acoustic lens (fabricated via HASA-ADAM) on a 6-DOF stage and align it for transcranial ultrasound (TUS) therapy using an iterative process. At each iteration, we drive the transducer with bi-frequency excitation (Δ​f=f2−f1=100​kHz\Delta f=f_{2}-f_{1}=100\,\text{kHz}) and record the PA signal magnitude|pΔ​f||p_{\Delta f}|. We seek a minimum atθ=0∘\theta=0^{\circ}. If the loop has not converged, we apply positional and angular corrections (Δ​θ,Δ​x,Δ​y,Δ​z\Delta\theta,\,\Delta x,\,\Delta y,\,\Delta z) and repeat. Once converged, we lock the lens position and initiate TUS therapy, achieving a targeting accuracy of<1.5​mm<1.5\,\text{mm}.

In our fixture the pivot axis (𝐏pivot=[443,644,23]\mathbf{P}_{\text{pivot}}=[443,\,644,\,23]) is offset from the transducer centre. A purezz-rotation therefore couples into lateral and axial translation. Tracking a surface voxel (𝐓initial=[1120,620,590]\mathbf{T}_{\text{initial}}=[1120,\,620,\,590]) through±6∘\pm 6^{\circ}of rotation gives a 10.6 mm total displacement (Table3.1; Figure3.3a). Even small angular errors produce large linear misregistration.Table 3.1:Geometric displacement of central voxel relative to pivot over the range±6∘\pm 6^{\circ}.Angle (∘)Δ​X\Delta X(mm)Δ​Y\Delta Y(mm)Δ​Z\Delta Z(mm)Total Euclidean Shift (mm)-6-0.1800+10.63460.000010.6361-5-0.0727+8.86440.00008.8647-4+0.0038+7.09250.00007.0925-3+0.0492+5.31970.00005.3199-2+0.0638+3.54620.00003.5467-1+0.0474+1.77280.00001.773400.00000.00000.00000.0000+1-0.0783-1.77170.00001.7734+2-0.1875-3.54190.00003.5467+3-0.3276-5.30980.00005.3199+4-0.4985-7.07500.00007.0925+5-0.7002-8.83700.00008.8647+6-0.9326-10.59510.000010.6361Figure 3.2:(a) Top: Nonlinear mixing of two high-frequency waves generated by a flat ultrasound (US) transducer attached to a hologram lens. At higher intensities, a low-frequency difference frequency arises from nonlinear steepening. This is known as the parametric array (PA) effect. Bottom: Schematic illustration of the hologram-assisted FUS therapy device integrated with a six-degree-of-freedom (6 DOF) robotic arm. The system utilizes standard acoustic coupling (e.g., a gel or water bolus). The receiver was placed at a fixed position relative to the head. The acoustic feedback from nonlinear parametric array signals is then used for accurate registration. (b) Top: 2D acoustic simulation demonstrating the generation of a 100 kHz parametric field within the skull cavity and its subsequent transmission through the skull cavity. Bottom: Waveforms showing increasing nonlinear distortion as primary waves attenuate due to skull-induced losses, and absolute pressure traces along the axial direction for varying source pressures at the transducer. (c) Top: (Row 1), Simulation of the primary ultrasound field with 3dB (in red) and 6 dB (in black) contour maps in the skull region showing local pressure maxima in the skull for skull rotationθ=0∘\theta=0^{\circ}andθ=2∘\theta=2^{\circ}, (Row 2) with zoomed view of the focal region as ROI with 3dB and 6dB contours (both in black); Bottom: The parametric field with (θ=2∘\theta=2^{\circ}) and without (θ=0∘\theta=0^{\circ}) skull rotation indicating aberration leads to higher PA signal (plot on the right). (d) 2D simulation results illustrate a decrease in parametric pressure corresponding to zero skull rotation (θ=0∘\theta=0^{\circ}) for various transverse skull slices.

Nonlinear k-Wave simulations (Westervelt/PSTD) confirmed that the effect is detectable in a realistic skull geometry[78].

These models were run along with bone and tissue nonlinearity parameters from the literature[98,99]. Using primary frequencies of 0.95 MHz and 1.05 MHz that resulted in 100 kHz difference frequency and pressures ranging from 0.25 to 1 MPa (safe exposure), we found that the parametric signal was immediately evident after the primary beams passed through the skull (Fig.3.2b). Despite the formation of a weak standing wave (≤\leq1.5 kPa), which is expected owing to the difference in frequency used[100], the parametric signal outside the skull was also evident and well within the detection limits of many piezoelectric detectors (Fig.3.2(b), bottom). While the observed temporal profile is atypical of nonlinear propagation (i.e., the peak positive pressure tends to be higher), this is due to the accumulation of nonlinearities over extended propagation distances, combined with the substantially higher attenuation of the primary and secondary MHz-range fields. In a clinical geometry the signal must cross two skull layers. The primary MHz tones are heavily attenuated on the return pass; the 100 kHz PA signal passes through with minimal loss (α∝fb\alpha\propto f^{b}). The skull itself acts as a low-pass filter that isolates the diagnostic tone.

Replacing the intracranial medium with water (βwater=3.5\beta_{\text{water}}=3.5) or brain (βbrain=4.45\beta_{\text{brain}}=4.45) changed the primary field negligibly but suppressed the PA signal when skull nonlinearity was absent. Bone (β≈188\beta\approx 188) overwhelms the volume integral in Eq.3.2; the skull region under the primary beam dominates PA generation.

Building on these observations, we tested the impact of lens misregistration on|pΔ​f||p_{\Delta f}|. We found that in the presence of misregistration, the PA signal increases substantially (Fig.3.2c, plot on the right). Further analysis revealed that the aberrated beams, in addition to distorting the pressure field (i.e., defocusing), also lead to a higher pressure buildup in the highly nonlinear skull. The quantitative integration of the volumetric data revealed an accumulation of acoustic energy in the misaligned state. We established a baseline potential of7.729×1067.729\times 10^{6}Pa2m3in the aligned state (θ=0∘\theta=0^{\circ}). Integration of the squared primary pressure within the skull bone volume revealed a +9.3% surge in trapped acoustic energy during a mere2∘2^{\circ}misalignment, increasing to8.446×1068.446\times 10^{6}Pa2m3(Table3.2, Fig.3.3b). This acts as a volumetric pump, significantly amplifying the nonlinear source term (SN​L∝β​|pp​r​i​m​a​r​y|2S_{NL}\propto\beta|p_{primary}|^{2}) and supporting the physical mechanism of the alignment feedback.Figure 3.3:(a)Visualization of skull fixture displacement. The skull is shown at-6∘(left),0∘(neutral), and+6∘(right). TheRed Linerepresents the fixed pivot axis. TheGreen Markertracks the target voxel at the center of the skull segment facing the transducer. This shows a translation in the X-Y plane due to the pivot offset.Fixture Rotation Animation(b)Analysis of Energy Trapped between the skull layers.Left:3D Mask Overlay verifying spatial coherence between the skull geometry and the pressure field grid.Middle:Isosurfaces of acoustic pressure hotspots trapped within the skull bone, showing a denser distribution of scattering nodes in the misaligned state (θ=2∘\theta=2^{\circ}) compared to the aligned state (θ=0∘\theta=0^{\circ}).Right:integration confirms a+9.3%increase in trapped energy during misalignment.Table 3.2:Quantification of acoustic energy trapped within the high-nonlinearity skull volume.Registration StateIntegrated Source Potential[Pa2m3]Aligned (θ=0∘\theta=0^{\circ})7.729×1067.729\times 10^{6}Misaligned (θ=2∘\theta=2^{\circ})8.446×1068.446\times 10^{6}Relative Increase+9.3%

This effectively extends the nonlinear interaction region, which is critical for the development of finite-amplitude effects[hamilton1997nonlinear]. Finally, we assessed the influence of misregistration on the PA signal by rotating the skull (Fig.3.2d). Interestingly, we found a steep increase in the PA signal for very small angles (i.e., small misregistration errors). We also verified the robustness of this metric to translational misalignments. 3D nonlinear simulations confirm that any error degrading aberration correction increases energy trapping, making the method highly sensitive to both rotational and translational shifts driven by the coupled kinematic moments discussed earlier.

Crucially, these observations persisted for different skull slices (Fig.3.2d), indicating that the PA signal drop is persistent and sensitive to the skull-compensating lens alignment. Together, these findings supported the notion that the low frequency acoustic signal generated by the nonlinear mixing of high frequency beams can be leveraged to attain accurate skull-compensating lens alignment.

## 3.3.2  Sensitivity analysis reveals that parametric array signal is a robust and sensitive surrogate to skull-compensating lens alignment

Motivated by these initial observations of volumetric energy trapping and augmented PA signals, we systematically evaluated the robustness of this metric using comprehensive three-dimensional (3D) nonlinear simulations. First, we investigated the impact of skull nonlinearity(B/A)skull(B/A)_{\text{skull}}on parametric generation. As expected, the primary field (1.05 MHz) remained unaltered across different levels of skull nonlinearity; however, the parametric field (100 kHz) decreased markedly when skull nonlinearity was absent (Fig.3.4a). To further clarify this observation, we varied the skull nonlinearity parameter ((B/A)skull=374,74.8(B/A)_{\text{skull}}=374,74.8, and 37.24; these are equivalent to Goldberg numbers of 3.0, 0.62, and 0.32, respectively) and performed multiple registration iterations by rotating the 3D skull in the transverse plane. Evidently, the parametric pressure drop closely followed skull nonlinearity (Fig.3.4(a), right). Crucially, when skull misalignment is minimized (i.e.,θ=0∘\theta=0^{\circ}), the drop in the PA signal becomes even more pronounced in the more realistic 3D simulations, as compared to 2D, for the same B/A parameters.Figure 3.4:(a) Left: Primary and parametric array pressures under conditions of high and low skull nonlinearity. Right: Effect of varying skull nonlinearity on parametric pressure drop. The observed drop in parametric pressure indicates optimal registration of the hologram lens with the skull. (b) Influence of difference frequency on the parametric pressure. (c) Variation in parametric pressure drop with different depths of focusing (or F#) across varying levels of nonlinearity, difference frequencies, and focusing parameters. (d) Impact of skull rotation about the x, y, and z axes on parametric pressure.

We also explored the effect of varying the difference frequencyΔ​f\Delta f(Fig.3.4b) and observed that the PA signal drop appears to be insensitive toΔ​f\Delta fwhen it ranges from 50 to 100 kHz. Notably, the relationship between the PA signal amplitude and downshift ratio (f/Δ​ff/\Delta f) follows established parametric array theory[94], where larger downshift ratios yield smaller PA signals owing to lower nonlinear interaction efficiency. Conversely, smaller downshift ratios, while potentially producing stronger signals, require transducers with broader bandwidths and are hindered by higher frequency-dependent attenuation through the propagation medium. This complex interplay of contributing factors determines the sensitivity of the PA signal changes to downshift-ratio variations. Next, we assessed the influence of focal depth by reducing the f-number while maintaining a constant aperture, producing a progressively weakly focused beam. Although we did not observe any major differences, lower f-numbers appeared to have higher variation. Finally, the drop in the PA signal during optimal alignment is robust to different axes of rotation, although rotations about the z-axis resulted in more substantial decreases in parametric pressure (Fig.3.4d).

To assess clinical feasibility, we investigated the robustness to receiver placement. Because the parametric source (λΔ​f≈15\lambda_{\Delta f}\approx 15mm) is larger than the skull thickness, it acts as a subwavelength source radiating quasi-omnidirectionally. This ensures the feedback signal is detectable even with ipsilateral receiver placement.

Across all tested parameters the PA signal dropped≥20\geq 20% at optimal alignment, provided the skull nonlinearity was high.

## 3.3.3  Parametric array signal provides a real-time feedback mechanism to noninvasively align skull-compensating holographic lens to human skull

To experimentally validate the theoretical sensitivity of this nonlinear acoustic feedback mechanism, we designed a holographic lens using the HASA-ADAM framework (Fig.2.4) and conducted experiments with a 1 MHz transducer with an active aperture D = 60 mm, coupled with a single focusing lens (F# 0.75). The transducer was excited with a bi-frequency input signal (containing 0.95 MHz and 1.05 MHz) at 0.2 MPa peak-to-peak pressure to produce a 100 kHz nonlinear difference frequency. The excitation consisted of short tone bursts (30 cycles) to avoid standing wave artifacts. This signal was then recorded with a needle hydrophone after 40 dB of low-pass filtering and compared with 3D simulations using the same geometry and skull segment (Fig.3.5). To perform axial scans and characterize the PA signal at different distances from the skull using a hydrophone, we removed part of the skull (Fig.3.5a). The skull cavity was immersed in degassed water to provide a standardized acoustic environment. This choice allowed us to isolate the effect of skull-induced aberration and nonlinearity on the PA signal, as water has low nonlinearity, and helped minimize the risk of pseudosound artifacts due to hydrophone nonlinearity[101].

Axial line scans confirmed that a 0.2 MPa (peak-to-peak) primary field (peak pressure at the focus) produced increasing nonlinear distortion along the axis and beyond the focal position. This was evident in the waterfall plot showing progressive self-demodulation (Fig.3.5d).Figure 3.5:(a) Experimental setup with the skull mounted on a rotating fixture, with the skull cavity filled with degassed water. (b) Sample bi-frequency normalized input signal in both time and frequency domains; and Zoomed-in sections highlighting the absence of nonlinear distortion. (c) Sample measured signals using hydrophone and after 600kHz low pass filtering with 40 dB gain in both time and frequency domains; and Zoomed-in sections highlighting the presence of nonlinear distortion. (d) Stacked waterfall plot indicating progressive nonlinear distortion of the measured signal (forθ=0∘\theta=0^{\circ}). (e) Hydrophone line scans demonstrating Primary and parametric signals. (f) 3D simulation mimicking the experimental setup, illustrating the variation of parametric pressure with skull rotation in the transverse plane. (g) Experimental variation of parametric pressure, showing a decrease corresponding to zero registration error. In (f) and (g), normalization is performed across the different rotational angles (θ\theta) for measurements taken at specific axial positions (e.g.,Z0+20​λZ_{0}+20\lambda).

To minimize pseudo-sound effects that can appear in the measurements when the hydrophone is subject to strong primary pressure fields, the measurement window was extended several wavelengths away from the focus (Fig.3.5d). We established the presence of a measurable PA signal for clinically relevant primary pressures (M.I.= 0.1), we rotated the skull at1∘1^{\circ}increments around the z-axis and measured its amplitude, as in the simulations above (Figs.3.2and3.4). The line scans for the primary frequency revealed broadening of the axial beamwidth for both positive (θ>0∘\theta>0^{\circ}) and negative (θ<0∘\theta<0^{\circ}) registration errors (Fig.3.5e). These measurements, aggregated across z-axis positions, not only closely aligned with the simulation predictions, but also confirmed the pronounced drop in parametric pressure when the skull rotation was zero (Fig.3.5f-g). The normalization in Fig.3.5f-g is performed across the different rotational angles (θ\theta) for measurements taken at specific axial positions (e.g.,Z0+20​λZ_{0}+20\lambda), not by spatial averaging. This procedure is accessible in a clinical setting; the operator monitors the signal at a fixed location while adjusting the lens orientation to find the minimum PA signal.

Taken together, these findings (Figs.3.2–3.5) support our hypothesis that the feedback from parametric acoustic array effect is sensitive to skull-aberrations caused by misregistration. We thus demonstrated its potential to provide real-time feedback to align the skull-compensating holographic lens to the patient’s skull.Figure 3.6:Effect of Skull Nonlinearity on Angular Sensitivity.Top:The magnitude of the relative drop in the normalized difference frequency (Δ​f\Delta f) amplitude increases monotonically with the skull’s nonlinearity parameter (B/AB/A), ranging from a 5.8% drop atB/A=0.0B/A=0.0to a 19.1% drop atB/A=374.0B/A=374.0.Bottom Left:NormalizedΔ​f\Delta famplitude as a function of skull rotation angle for varyingB/AB/Avalues, demonstrating that higher nonlinearity yields a steeper and more pronounced registration dip.Bottom Right:Axial profiles of theΔ​f\Delta famplitude at optimal alignment (θ=0∘\theta=0^{\circ}), illustrating the baseline enhancement of parametric generation with increasingB/AB/A.

## 3.3.4  Mechanisms Governing the Angular Sensitivity of PA Acoustic Feedback

In the preceding sections, the key result that a consistent parametric array signal drop atθ=0∘\theta=0^{\circ}is observed in both simulations and the experiment was shown, which proved our primary hypothesis. We investigate a secondary issue here: experiments showed a steeper angular roll-off than the fluid model predicted. Three candidate explanations are mechanical fixture inaccuracy, an underestimated skullB/AB/A, and unmodelled shear-wave generation. To evaluate the impact of the skull’s nonlinearity on the registration metric, we quantified the normalized drop in the difference frequency (Δ​f\Delta f) across a range ofB/AB/Avalues (Fig.3.6). The analysis reveals a direct, positive correlation: as the assumed nonlinearity of the skull increases, the magnitude of the signal drop at optimal alignment (θ=0∘\theta=0^{\circ}) increases substantially. For instance, while a purely linear skull approximation (B/A=0.0B/A=0.0) yields a relative drop of roughly 5.8% (calculated between±1∘\pm 1^{\circ}misalignment and0∘0^{\circ}alignment), increasingB/AB/Ato upper physiological estimates (B/A=374.0B/A=374.0) yields a pronounced, steep signal reduction of 19.1%. This parametric relationship provides strong evidence that the steep angular drop-off observed in ourex vivoexperiments could be largely attributed to a higher trueB/AB/Avalue of the skull segment than the conservative estimates we used in our simulations. Consequently, underestimating the skull’s nonlinearity is a highly probable, simple explanation for the discrepancy between the PA drop simulation and the experiment. Nevertheless, to examine all possibilities, we also explored mode conversion at the fluid-bone interface.

Geometric incidence and shear mode risk.Continuous parametric sweeps of the rotation angle (±10∘\pm 10^{\circ}) revealed a piecewise linear sensitivity to spatial misalignment (Fig.3.8a). We observed a threshold-like abrupt change in sensitivity at (±4∘\pm 4^{\circ}) angular rotation. The mode-conversion risk is minimized at zero fixture rotation (θ≈0∘\theta\approx 0^{\circ}), which indicates optimal longitudinal transmission. However, at the rotation angle exceeding±4∘\pm 4^{\circ}, the primary beam interacts with the steeper skull curvature that pushes the acoustic aperture above the critical angle(θc≈30∘\theta_{c}\approx 30^{\circ}). We can see these abrupt jumps in the animation for skull fixture rotation (Fig.3.8a). Even small positioning errors can result in a rapid loss of the effective transmitting aperture. This increases the absolute shear risk by nearly 10% at a6∘6^{\circ}misalignment. Such geometric dependence of mode conversion also explains why projecting complex holographic patterns is more difficult than projecting a simple single-focus pattern (as discussed in Chapter 2). Simpler point-focusing tasks typically involve near-normal incidence (i.e., low mode conversion), complex holographic patterns require steep phase gradients and highly oblique incidence angles. This increases their susceptibility to such scattering and mode conversion.

The shear energy trap.While fluid-based models partially explain the baseline signal increase during misalignment, capturing the spatial redistribution of acoustic hotspots from the weakly nonlinear brain tissue back into the highly nonlinear cranial bone (βe​f​f≈40\beta_{eff}\approx 40), they fail to capture the magnitude of the experimental PA signal spike. This is because fluid solvers inherently neglect solid mechanics. By comparing the elastic simulations against fluid solvers (Fig.3.8b), we show that geometrically triggered mode conversion could possibly act as an angle-dependent acoustic energy trap.

In the elastic regime, angular misalignment (θi>30∘\theta_{i}>30^{\circ}) causes the incident longitudinal energy to be mode-converted into transverse shear waves (SS-waves). Shear waves are volume-preserving. This means their kinetic energy does not appear in scalar pressure measurements. They only show up instead as a sharp drop in forward-transmitted compressional energy (Fig.3.8c).

Parametric amplification via velocity mismatch.As derived in Section 3.2.4, the efficiency of nonlinear parametric interaction is theoretically proportional toc−3c^{-3}. Assuming this scaling can be extrapolated from fluids to elastodynamic modes in a solid, the slower velocity of shear waves in bone (cS≈1400c_{S}\approx 1400m/s) compared to longitudinal waves (cL≈2800c_{L}\approx 2800m/s) implies that a unit of shear energy could be approximately eight times more efficient at generating nonlinear byproducts. By potentially converting fast-propagating waves into slow-propagating ones, the misaligned skull could effectively force acoustic energy to linger inside the highly nonlinear diploe layer for twice the duration, acting as a highly efficient volumetric pump.

This shear-amplification explanation needs dedicated future studies for verification. No existing solver, unfortunately, couples 3D elastodynamics with dual-frequency nonlinear parametric mixing. Greater shear attenuation in bone may also reduce the effect before it accumulates. An underestimatedB/AB/Aor fixture error can be a simpler and more plausible explanation. The conclusion remains unaffected. The PA signal drop we observe at accurate registration is replicable in both simulation and experiment.

Spatiotemporal waveform validation.We also empirically probed this hypothesis via waveform analysis ofex vivotransmissions. Any parametric signal generated via shear-mode mixing must arrive at the detector at a distinct time lag due to slower shear wave speeds (roughly 0.5 times the compresional wave speed). As shown in Fig.3.7, the experimental waveform at the optimal normal incidence (θ=0∘\theta=0^{\circ}) is temporally compact and consistent with longitudinal propagation. However, at an oblique incidence of4∘4^{\circ}, the wave packet exhibits temporal elongation. But this is absent in the aligned case. This delayed signature offers a possible mechanism in which a slower-propagating shear mode contributes to nonlinear generation. This lends circumstantial support to the shear hypothesis as a contributing factor. Our primary finding, regardless, is that the robust drop in the PA signal indicating alignment remains validated independently of this effect.Figure 3.7:Spatiotemporal evidence of Shear Mode Conversion(a)At optimal alignment (θ=0∘\theta=0^{\circ}), the received signal envelope is compact in the time domain. This is consistent with Longitudinal propagation (cL≈2900c_{L}\approx 2900m/s), where energy goes through the skull quickly.(b)At4∘4^{\circ}rotation, the wave packet exhibits distincttemporal elongation(a delayed energy tail).Mechanism:This delayed energy possibly corresponds to Shear Modes (cS≈1400c_{S}\approx 1400m/s) generated by mode conversion at the oblique interface. We know that shear waves propagate at approximately half the speed of longitudinal waves; so they could be effectively trapped within the high-nonlinearity diploe layer for a longer duration. This lingering energy density within the skull bone acts as a potential source for nonlinear mixing (SP​A∝P2S_{PA}\propto P^{2}). This is one possible mechanism to explain the steeper drop-off in sensitivity observed in experiments.Figure 3.8:(a) Geometric Incidence and Shear Risk:Top:3D beam-skull mapping and Shear Risk profile (θc=30∘\theta_{c}=30^{\circ}) as a function of misalignment.Bottom:Incidence maps for−6∘,0∘,+6∘-6^{\circ},0^{\circ},+6^{\circ};greenindicates safer transmission for longitudinal or compressioanl waves.Redhighlights the portion on the skull cap prone to shear mode conversion due to angle of incidence exceeding the critical angle for fluid-bone interface(Animation).(b) Full-Wave Propagation:Comparison of Fluid (top) and Elastic (bottom) steady-state pressure fields across0∘,2∘,4∘0^{\circ},2^{\circ},4^{\circ}misalignment, showing energy dampening due to shear scattering.(c) Energy Dynamics and Amplification:Left:Centerline profiles showing fluid model overestimation of internal standing waves.Middle:Stacked area plot of energy transfer from compressional (blue) to kinetic shear modes (red) with increasing rotation.Right:Isolated trend of trapped kinetic shear energyexploring its potential as a driver forparametric amplification. (Animation).

## 3.3.5  Registration metric is robust to hydrophone placement and aperture size

Figure3.9shows the sensitivity map of the registration dip magnitude across a60×6060\times 60mm region behind the skull. The signal was detectable across most of the fields. The difference between the Best and Worst detection points decreases significantly as the aperture increases (Figure3.10). A 20 mm aperture averages sub-wavelength interference to minimize dead spots and ensure detection in a robust manner.

The radiation pattern of the parametric source within the skull is governed by the diffraction limitk​DkD, whereDDdenotes the skull thickness.
Theprimary beam (λ≈1.5\lambda\approx 1.5mm)is highly directional; it requires precise targeting. On the other hand, theparametric signal (λΔ​f≈15\lambda_{\Delta f}\approx 15mm)has a wavelength larger than the skull thickness (L<λΔ​fL<\lambda_{\Delta f},L≈7L\approx 7mm). Thus, the interaction volume acts as a sub-wavelength acoustic source.

A source smaller thanλΔ​f\lambda_{\Delta f}radiates as a monopole. The receiver, therefore, needs no phase alignment with the transmitter; any acoustically coupled position on the head captures the alignment-induced energy dip.Figure 3.9:Spatial Robustness of Nonlinear Acoustic Feedback.(a)Spatial Sensitivity Map showing the magnitude of the registration dip (signal drop at0∘0^{\circ}) across a60×6060\times 60mm region behind the skull. The signal was detectable across most of the fields.(b)Edge-case analysis contrasting the signal trace at the most sensitive spatial pixel (Green) versus a diffraction node (Red).(c)Robustness analysis aggregated over a large number of spatial points (N=52,130N=52,130). While individual point measurements vary (Gray envelope), the spatially averaged response (Blue line), which can also be observed with a larger-aperture receiver, exhibits a global minimum at accurate registration.Figure 3.10:Effect of Sensor Aperture on Signal Stability.(a)Spatial Sensitivity Map showing the magnitude of the registration dip across a60×6060\times 60mm region.(b)Comparing the signal trace at the best versus worst sensor positions. The difference between the Best and Worst detection points decreases as the aperture increases. A 20 mm aperture averages sub-wavelength interference and ensures consistent detection.(c)The larger 20 mm aperture acts as a spatial filter, which lowers uncertainty limits (Gray region) and gives a reliable mean response (Blue line).

## 3.3.6  Near-field measurements suggest parametric generation over pseudo-sound

Figure3.11shows the difference in frequency atΔ​f=100\Delta f=100kHz measured using a needle hydrophone as a function of the primary pressureΔ​f1=1.05\Delta f_{1}=1.05MHz for three separate conditions: at focus, 60 mm from the focus, and 120 mm from the focus. Evidently, as the hydrophone moves away from the focus, the primary pressure decreases (indicated by the rightward shift in the curves); however, the difference in frequency pressure at 60 mm and 120 mm from the focus remains the same and has an almost linear relationship with the primary pressure. Conversely, the difference in frequency pressure at the focus has a quadratic relationship with the focal pressure (i.e., the quadratic term associated with the pseudo-sound is significant).

The primary pressure decreases with increasing distance, following the inverse-square law. Pseudo-sound depends on this primary pressure amplitude and is expected to drop following a similar trend. However, the PA signal we observe remains relatively flat. We can conclude that the measured signal at those distances is not due to hydrophone nonlinearity and may be due to true parametric generation that accumulates over a longer propagation distance.Figure 3.11:Pseudo-sound quantification using near-field measurements. Axial Distance from Focus: z = 0 mm (black circles), z = +60 mm (blue squares), z = +120 mm (red triangles).

## 3.3.7  Spectral analysis supports intrinsic skull nonlinearity over microbubble artifacts

Figure3.12shows the time-domain waveforms (left column) and their corresponding frequency spectra (FFT) (right column) at various depthszz. The spectral data provide evidence regarding the physical origin of nonlinearity:
- 1.

Confirmation of Classical Mixing:As seen in the FFT plots (positions 18 through 71), there are distinct, high-SNR peaks corresponding to the mixing terms predicted by the Westervelt model: The Primary inputs (f1,f2f_{1},f_{2}) around 1 MHz and the targetDifference Frequency (Δ​f\Delta f)at≈100\approx 100kHz.
- 2.

Absence of Bubble Signatures:We examined the spectral region corresponding to the subharmonic frequency (fs​u​b≈500f_{sub}\approx 500kHz). As shown in the FFT plots, the noise floor in the0.2−0.80.2-0.8MHz range remained flat. There isno detectable energyatf0/2f_{0}/2.

If incident pressures typically exceed the threshold for inertial cavitation and period-doubling bifurcations, any trapped gas bodies would be driven into a strong-scattering regime. This is characterized by the emission of subharmonics (f0/2f_{0}/2) and broadband noise. Therefore, the observation of a robust Difference Frequency signal and absence of subharmonic content suggests that microbubbles are not the source of the nonlinearity. Thus, the signal is attributable to the intrinsic cumulative nonlinearity of the bone matrix.

We further analyzed the signal integrity relative to thresholds for bubbly media[102]. It has been demonstrated that gas-saturated layers exhibit softening nonlinearity; incident pressures of only 50 kPa are sufficient to distort the carrier wave into a steep sawtooth, resulting in a large number of high-frequency harmonics. In contrast, in our experiments, we used focal pressures of approximately 0.1 MPa. If trapped gas microbubbles were present in the diploë layer, this pressure would force the system into inertial cavitation. And we would see significant signal degradation, along with the presence of sub-harmonics and ultra-harmonics. Our spectral analysis (Fig.3.12) reveals transmission of the primary frequencies and a clean Difference Frequency (Δ​f\Delta f) peak. The medium’s ability to support 0.1 MPa propagation without degrading into the shock regime provides further evidence that the propagation path is free of resonant bubbles.Figure 3.12:Time-domain waveforms and Frequency Spectra along the propagation axis.The left column shows the raw voltage recorded by the hydrophone at increasing depths (Top to Bottom). The column on the right shows the corresponding FFT results. Dashed lines indicate the Difference Frequency (Δ​f\Delta f, blue), the Primary Frequency (f1f_{1}andf2f_{2}, orange and yellow)

## 3.3.8  Impact of Intracranial Trapped Gas on Parametric Array Generation

The results illustrated in Figure3.13demonstrate a nonlinear threshold response regarding the survival of the parametric array compared to that of the fundamental beam under gas exposure. As shown in the axial pressure profiles (Figure3.13, Right Panel), two distinct regimes were observed. In theWeakening Regime (orange curve) (ϕg​a​s=0.1%\phi_{gas}=0.1\%), the primary beam undergoes scattering but retains a focal structure. The difference frequency was also similarly attenuated, but remained coherent and visible. In theElimination Regime (yellow curve) (ϕg​a​s≥1%\phi_{gas}\geq 1\%), a transition occurs at 1% gas inclusion. The scattered and broadened primary beam still transmits through the skull, but the difference frequency (PA) signal drops to the noise floor immediately after the skull. This suppression of the difference frequency (Δ​f\Delta f) could be due to the disruption of the nonlinear mixing zone inside the skull bone. The amplitude of the parametrically generated wave,PΔ​fP_{\Delta f}, scales with the coefficient of nonlinearity (β\beta) of the medium as follows:PΔ​f∝β⋅Pf​1⋅Pf​2∗P_{\Delta f}\propto\beta\cdot P_{f1}\cdot P_{f2}^{*}(3.14)

The skull volume acts as a local amplifier for the generation of different frequencies. Trapped gas bubbles disrupt this mechanism by randomizing the phases of the primary waves, which destroys the phase coherence required for cumulative generation. Additionally, because difference frequency generation scales with theproductof the primary pressures (Eq.3.14), a linear reduction in primary amplitude due to scattering results in a quadratic reduction in the secondary source strength. Therefore, we conclude that gas inclusions act as passive scatterers. The elimination of the parametric array is caused by the high acoustic impedance mismatch, which scatters the primary energy and disrupts the nonlinear coherence.Figure 3.13:(Top Panel)Longitudinal field maps showing skull geometry (row 1), fundamental frequency amplitude (row 2), and difference frequency amplitude (row 3).(Bottom Left Panel)Skull slice of speed of sound without (Row 1) and with (Row 2) gas inclusions in the microstructure(Bottom Right Panel)Axial pressure profiles extracted through the geometric focus. The top plot shows the fundamental frequency (f1f_{1}), whereas the bottom plot shows the difference in frequency (Δ​f\Delta f). A critical transition occurs atϕg​a​s≥1%\phi_{gas}\geq 1\%, where the difference frequency signal is effectively extinguished.

## 3.4  Discussion

To comply with the targeting requirements in the brain, where mistargeting can pose safety risks, or when accurately targeting specific brain regions or neuronal circuits is essential,[67,103]a millimeter (i.e., subwavelength) targeting accuracy is required. To achieve this level of accuracy, our investigations addressed the long-standing challenge of skull-compensating lens registration by uncovering the close relationship between skull nonlinearity and aberrations caused by misregistration. The PA minimum provides sub-wavelength alignment—below the∼2{\sim}2mm floor of current neuronavigation[69,91,45,92]. The proposed PA feedback method complements neuronavigation by providing the sub-wavelength accuracy required for high-frequency TUS, and our simulations show it is robust to both rotational (Fig. 4) and translational misalignments.Regarding the clinically acceptable margin of error, our experimental data demonstrated that a registration tolerance of±1∘\pm 1^{\circ}was acceptable for the specific skull segment tested—maintaining targeting accuracy and focal pressure within safe therapeutic margins. However, human skulls show high variability in thickness, geometry, porosity, and internal composition. Thus, determining a universal clinical tolerance for registration will require future studies across a large dataset of varying skull geometries. The core mechanism of tracking the PA signal minimum should remain robust (i.e., a drop of more than 10-20% at accurate registration) across these variations.

Beyond its immediate application to skull-compensating lens registration, one natural extension is that PA acoustic feedback, combined with the HASA-ADAM framework, can also be utilized for noninvasive aberration correction of phased arrays, where it can be used as an objective function for noninvasive in vivo phase and amplitude optimization of each element. Together, these conceptual contributions and advancements support the design of simple, economical, and high-performance ultrasound systems for high-precision neurointerventions. Such systems may also support daily/weekly treatments, possibly in outpatient and/or limited resource settings, without compromising performance, thereby supporting the effective translation and broad dissemination (i.e., similar to US imaging) of this technology[68,104]. This may also alleviate the need for repeated use of intraoperative MRI during TUS interventions such as targeted drug delivery or liquid biopsy, which can complicate or even prevent their implementation (e.g., the average time to obtain an MRI appointment can be several months[105]).

Although our experimental and numerical results indicate a substantial drop in the PA signal during good skull-compensating lens alignment, we noticed some discrepancies that can be attributed to several interrelated factors.As discussed, the steeper signal drop in experiments compared to baseline fluid simulations may stem from unmodeled shear wave parametric generation, physical fixture errors, or an underestimation of the skull’s nonlinearity. For instance,the nonlinearity parameterβ\beta, which fundamentally governs PA signal generation, exhibits frequency-dependent behavior that is often oversimplified in simulations[106,107]. Additionally,β\betafor the skull, which is a highly porous structure, has not been characterized in the literature, suggesting that the current values used in theoretical investigations may not be optimal. The experimental uncertainties may also have contributed to this. Most notably, microscopic air bubbles trapped in skull pores may persist[108]despite the extended degassing we performed (see Methods). These microbubbles, which are resonant in the MHz range and exhibit extreme nonlinearity even at very low void fractions, may contribute to skull non-linearity[109,110]. Additionally, the skull bone follows complex frequency-dependent attenuation and has high interindividual variability that is often underestimated in simulations[111,99]. Together, these sources of uncertainty can lead to a higher Goldberg number (i.e., nonlinearities) and PA signal under the experimental conditions. Accurate, frequency-resolved measurements of skullB/AB/Aand shear parameters are now a priority. The principal validation stands: the PA signal drops at optimal alignment in both computation and experiment, confirming its value as a registration metric.

Collectively, the proposed research, by accelerating hologram design and introducing robust registration strategies to support the design of high-fidelity transcranial holography, may support the effective translation and broad dissemination of this technology in the clinic. Although our work is primarily focused on biomedical applications, the implications of high-fidelity acoustic holography are much broader and will invite researchers to explore this new capability across a range of applications[58,59,60,33,25,37,23]. Our research also lays the groundwork for future studies exploring low-frequency nonlinear acoustic feedback for the diagnosis, monitoring, and treatment of brain diseases and highlights the importance of relatively thin and highly nonlinear media to augment finite-amplitude effects.

## 3.5  Conclusions

To conclude, nonlinear wave propagation through the skull provides a feedback signal for registering holographic lenses to the skull bone. The key findings of this chapter are:

PA feedback as a registration metric.The difference-frequency signal generated inside the skull drops to a minimum when the lens is correctly aligned. This dip was observed in both fluid simulations andex vivoexperiment.

Energy-trapping mechanism and shear hypothesis.Misalignment traps primary-beam energy in the high-β\betabone, increasing the PA source term by∼9{\sim}9%. Our secondary hypothesis that mode-converted shear waves amplify the effect via ac−3c^{-3}scaling is consistent with temporal waveform data. It requires rigorous future studies for validation. Under-estimatedB/AB/Aand fixture error are equally plausible explanations.

Intrinsic skull nonlinearity isolated.Near-field pseudo-sound measurements and the absence of subharmonic spectral lines ruled out microbubble cavitation. The registration signal originates from cumulative quadratic nonlinearity of the bone matrix.

Spatial robustness confirmed.The PA interaction volume (λΔ​f≈15\lambda_{\Delta f}\approx 15mm>>skull thickness) acts as a monopole source. A receiver anywhere on the acoustically coupled head surface detects the alignment dip; a 20 mm aperture virtually eliminates dead spots.

## Chapter 4Monitoring Intracranial Pressure in Hydrocephalus00footnotetext:An earlier version of the work presented in this chapter is available as a preprint on arXiv (https://arxiv.org/abs/2508.07103).[57]

## 4.1  Introduction

In this chapter, we explore whether the parametric acoustic (PA) array can be used to non-invasively monitor ventricular expansion as a proxy for changes in intracranial pressure (ICP). We believe this is possible by detecting shifts in the brain’s effective acoustic nonlinearity in response to relative changes in ventricular size. We have simulated transcranial bi-frequency nonlinear ultrasound transmission to assess the diagnostic feasibility of this approach.

Hydrocephalus is a disturbance in cerebrospinal fluid (CSF) dynamics that results in enlarged ventricles and elevated intracranial pressure (ICP). The management of hydrocephalus requires frequent monitoring of ICP, which is a key biomarker for tracking disease progression to help guide treatment by removing excess CSF (e.g., via shunt-based treatments). Invasive ICP monitoring using external ventricular drains (EVDs) or parenchymal microsensors is the gold standard[112]in clinical practice. This approach, though, carries several associated risks such as infection, hemorrhage, and mechanical failure[48,113]. Such invasive monitoring is also episodic. Clinicians often lack continuous insight into intracranial dynamics in the outpatient setting after catheter removal. Non-invasive surrogates such as Transcranial Doppler (TCD) ultrasonography or Optic Nerve Sheath Diameter (ONSD) measurements can be used to mitigate this. But, they often lack a direct physical correlation with ventricular volume or result in significant operator variability[114,115]. Therefore, non-invasive techniques that accurately detect ventricular volume changes and reliably assess shunt function can reduce complications by closing the monitoring gap.

Because clinical investigations show that the removal of excess CSF leads to a decrease in ICP, which in turn results in reduced ventricular space (or increased space occupied by brain tissue)[116], we used the distinct physical contrast between the acoustic nonlinearity parameters of brain parenchyma (B/A≈7.4→β≈4.7B/A\approx 7.4\rightarrow\beta\approx 4.7) and the protein-poor, water-like CSF (B/A≈5.2→β≈3.6B/A\approx 5.2\rightarrow\beta\approx 3.6)[47,117]. As ventricles expand, they displace higher-nonlinearity brain tissue with lower-nonlinearity CSF. We hypothesize that this volumetric substitution suppresses the cumulative generation of difference-frequency ultrasound along the transcranial path.

Linear pulse-echo ultrasound (e.g., at 500 kHz) could be used to track the geometric expansion of the ventricles by measuring the distance to the brain-water interface. But such techniques rely heavily on precise registration to capture specular reflections from the ventricular walls. This makes them highly operator-dependent and prone to signal loss due to skull-induced scattering or misalignment. In contrast, the Parametric Array-based method may serve as a continuous, bulk proxy measurement to track the drop in the effective nonlinearity parameter (β\beta) as CSF replaces brain tissue. Because this volumetric signal is more tolerant to lateral misalignment, it may provide a reliable basis for a simple, operator-independent wearable sensor.

## 4.2  Methods

## 4.2.1  Nonlinear Acoustic Sensing

The origin of acoustic nonlinearity can provide a basis for detecting ventricular expansion. The propagation of finite-amplitude ultrasound in thermoviscous tissue is modeled by the Westervelt equation[96], where the local nonlinearity parameterβ\betaacts as a virtual source density. When the medium is excited by two primary frequencies (ω1\omega_{1}andω2\omega_{2}), the nonlinear interaction generates a low-frequency wave at the difference frequency (ωd=|ω1−ω2|\omega_{d}=|\omega_{1}-\omega_{2}|). The amplitude of this difference frequency,PΔ​fP_{\Delta f}, grows cumulatively over an interaction lengthLLand under quasilinear approximation can be written as :PΔ​f​(L)∝ωd2​∫0Lβ​(z)ρ0​c05​P1​(z)​P2​(z)​e−αd​z​𝑑zP_{\Delta f}(L)\propto\omega_{d}^{2}\int_{0}^{L}\frac{\beta(z)}{\rho_{0}c_{0}^{5}}P_{1}(z)P_{2}(z)e^{-\alpha_{d}z}\,dz(4.1)

This relationship indicates that the received signal acts as a path integral of the nonlinearityβ​(z)\beta(z)weighted by the primary pressure fields. Consequently, if expanding ventricles displace brain tissue with CSF in the focal region, the local value ofβ​(z)\beta(z)drops, thereby reducing the integrated signal. Thus,PΔ​fP_{\Delta f}can serve as a non-invasive volumetric indicator of tissue composition.

## 4.2.2  Computational Modeling of Ventricular Expansion

High-resolution two-dimensional (2D) pseudo-spectral time-domain (PSTD) simulations examined the relationship between ventricular expansion and the PA signal using the k-Wave MATLAB toolbox[118].

We developed a realistic 2D head model derived fromμ\muCT data, using the Evans Index (EI)(the ratio of frontal horn width to maximum skull diameter) to define pathological states[119]. The ventricular mask was dynamically resized to simulate expansion from a baseline cross-sectional area (CSA) of 20 cm2(representing moderate ventriculomegaly) to 40 cm2(representing severe hydrocephalus). Primary frequencies of 0.95 MHz and 1.05 MHz were emitted by a focused transducer to generate a 100 kHz difference frequency.

The pulse length for this bi-frequency excitation sequence can be constrained to avoid auditory neuromodulation or other adverse artifacts caused by long, low-frequency pulses. Our simulated sonications used very short bursts consisting of 30 to 40 cycles of the primary 1 MHz pulse (resulting in a total pulse duration of 30–40μ\mus). Also, these pulses can be delivered at a very low Pulse Repetition Frequency (PRF) of 1-2 Hz as per the desired sensor refresh rate. These pulse parameters are sufficient to generate parametric array signals without crossing thermal and mechanical safety thresholds. Our simulation domain included the entire realistic 2D skull-brain slice to capture the nonlinear propagation effects as the beam passes through the proximal skull layer, the brain parenchyma/ventricles (interaction zone), and the distal skull layer. We eventually detect the external PA signal in transmission mode outside the skull cavity.

## 4.2.3   Lateral Misalignment Robustness

We performed a robustness analysis to evaluate performance under realistic conditions with sensor placement errors. We modeled a fixed hardware setup that incorporates a physical acoustic plano-concave lens to focus the 1 MHz beam at a depth of 60 mm. We introduced lateral positioning errors by shifting the patient anatomy relative to the fixed probe in 1 mm increments over a±5\pm 5mm range. The diagnostic metric was defined as the maximum amplitude of the signal envelope captured by a broad receiver window (Region of Interest, ROI) of 20 mm positioned in the far-field. This broad ROI was selected to determine if spatial integration could maintain diagnostic contrast despite localized geometric beam steering caused by the skull.

## 4.2.4  Frequency Dependence

We also probed the frequency dependence of our sensing modality’s performance.
We characterized the sensitivity across a range of different frequencies (Δ​f\Delta f) from 20 kHz to 200 kHz. The goal of this study was to understand the optimal operating window. We considered the trade-off between nonlinear conversion efficiency (which favors higher frequencies) and the practical limitations of transducer bandwidth.

## 4.3  Results

## 4.3.1  Parametric acoustic (PA) feedback detects ventricular expansion

Our in silico models showed expected propagation behaviors when propagated across the skull-brain layers. The primary 1 MHz field suffered∼\sim20 dB attenuation and scattering at the entry skull interface; the parametric array signal, or the difference-frequency field generated at 100 kHz, indicated better penetration due to favorable inverse-frequency attenuation. Also, the difference frequency is generated cumulatively along the propagation path within the tissue. This allows it to maintain a coherent beam profile that effectively tunnels through the distal skull layer.

Next, we simulated ventricular expansion using a clinically relevant scenario for untreated hydrocephalus[120]. Our results show that as the ventricular size doubles (progressively expanding from 20 cm2to 40 cm2ventricular cross-sectional area), the PA signal measured outside the skull cavity drops by approximately 10% (Fig.4.1d). This drop in amplitude suggests a drop in nonlinear generation efficiency, as expected. As the interaction zone is increasingly occupied by low-nonlinearity CSF, the generated PA signal drops as per Equation4.1. This decrease is also sensitive to the transducer F-number. Tightly focused beams (F​#​1.00F\#1.00) leading to a larger relative drop in parametric pressure.Figure 4.1:Nonlinear acoustic feedback can detect relative changes in ventricular size. (a) Schematic showing hydrocephalus monitoring using the parametric array effect: increasing hydrocephalus leads to a drop in the PA signal. (b) The simulation mask and the nonlinearity parameter map correspond to enlarged hydrocephalus. (c) Primary and parametric field obtained from simulation. (d) Peak parametric signal pressure outside the skull cavity decreases with increasing ventricular size.

## 4.3.2  Robustness analysis shows a consistent diagnostic margin

Lateral probe misalignment (±5\pm 5mm) simulations were used to determine system reliability under typical operational conditions. The results( Fig.4.2) show that the PA signal levels outside the skull cavity for the Normal state (ventricle size 20 cm2) and the Hydrocephalus state (ventricle size 40 cm2) do not intersect.

In linear acoustic models, complex skull scattering can lead to overlapping signal distributions for normal and disease states. Our nonlinear analysis showed that the Normal signal amplitude remains higher than the Hydrocephalus signal across the entire sweep. This points to the robustness of the method. The detector acts as a spatial integrator due to a broad receiver window in the far field. This broad ROI captures the bulk of the forward-propagating energy flux and averages out local geometric steering artifacts caused by skull curvature. The hydrocephalic brain produces less nonlinear signal due to CSF replacement, which leads to lower integrated signal at the difference frequency. This creates a persistent diagnostic margin (Fig.4.2A, shaded region) for reliable differentiation between the two states.Figure 4.2:Robustness Analysis and Diagnostic Margin in Hydrocephalus Monitoring. (A) Normalized parametric signal strength (100 kHz) as a function of lateral probe misalignment (±5\pm 5mm). The trend lines for Normal (blue circles) and Hydrocephalus (orange squares) do not intersect. This creates a distinctDiagnostic Contrast Region(shaded gray). The vertical dashed lines correspond to the misalignment scenarios shown in the lower panels.
(B) 2D acoustic field maps showing the spatial distribution of the difference frequency pressure. The top row displays the Normal case, and the bottom row displays the Hydrocephalus case with lateral shifts of -4 mm and +2 mm (indicated by the cyan receiver box). The Hydrocephalus cases demonstrate a steady reduction in signal intensity due to the volumetric replacement of high-nonlinearity brain tissue with low-nonlinearity CSF.Figure 4.3:Process Flow Chart for ICP Monitoring in a Clinical Setting using PA signalThe protocol has an initialization phase and a continuous monitoring loop. The system is configured with a difference frequency (Δ​f\Delta f) of 100 kHz and a region of interest (ROI) of 20 mm, establishing a baseline PA signal magnitude (|pΔ​f|0|p_{\Delta f}|_{0}) representing baseline ventricular state. The system then uses bi-frequency transmission (30–40 cycles, PRF = 1–2 Hz) to measure the variation in PA signal (|pΔ​f||p_{\Delta f}|) in a loop. If the measured signal drops by more than 10% relative to the baseline, the system detects ventricular expansion and issues a clinical alert.

## 4.3.3  Frequency dependence shows an optimal operational window

The analysis of difference frequencies (Δ​f\Delta f) revealed a trade-off between system performance and diagnostic contrast (Fig.4.4). At low difference frequencies (Δ​f≤50\Delta f\leq 50kHz), the nonlinear conversion efficiency dropped as expected from the theory of parametric acoustic arrays[121]. Additionally, the larger acoustic wavelengths (λ≈30\lambda\approx 30mm) led to diffraction, resulting in a diffuse beam that failed to interact with the ventricular volume, thereby lowering the diagnostic contrast.

On the other hand, generating higher difference frequencies (e.g., 200 kHz) requires a wider separation between the primary frequencies; this separation is limited by the bandwidth of piezoelectric transducers (typically high-Q). A larger separation reduces primary pressure amplitudes. Our simulation identified the 75–125 kHz range as the optimal operational window. In this regime, the parametric conversion efficiency is sufficient to generate a measurable signal. Also, the beam maintains effective collimation to interact with the ventricles. Thus, the diagnostic contrast remains stable at∼\sim10–15%.Figure 4.4:Frequency Robustness Analysis in Hydrocephalus Monitoring. (A) Normalized signal strength across various difference frequencies (Δ​f\Delta f). (B) Relative signal drop (Hydrocephalus/Normal). A stable diagnostic contrast (Ratio<1.0<1.0) appears above 75 kHz. (Bottom Panels) Acoustic field maps show beam collimation. At low frequencies (Δ​f=50\Delta f=50kHz), the beam is diffuse due to diffraction, which reduces spatial sensitivity. At higher frequencies (Δ​f≥100\Delta f\geq 100kHz), the parametric array forms a collimated beam. This maximizes the interaction with the ventricular volume.

## 4.4  Discussion

Monitoring relative changes in the parametric pressure outside the skull cavity can help us gauge ventricular expansion during hydrocephalus progression. It can also be used to detect ventricular shrinkage during successful shunt treatment. The separation between normal and hydrocephalus states (termed as diagnostic contrast) shown during robustness testing (Fig.4.2) indicates that a decrease in nonlinear gain is the dominant mechanism behind the sensitivity; the contrast relies on changes in the medium’s effective nonlinearity parameter (β\beta). Expanding ventricles replace higher-nonlinearity tissue with lower-nonlinearity CSF in the interaction zone. Such displacement results in lower total nonlinear acoustic energy at the difference frequency and in a stable signal offset. Additionally, the non-intersecting nature of these robustness curves for normal and hydrocephalus states enables threshold-based classification. A PA signal below a baseline threshold can indicate pathological ventricular expansion. This does not need complex image reconstruction or expert operator interpretation. The diagnostic margin of the signal across±5\pm 5mm of lateral misalignment implies that precise stereotactic placement is not required. This misalignment tolerance highlights the key advantage of the PA method over conventional 500 kHz linear pulse-echo ultrasound. The latter would rapidly lose the required specular reflection from the ventricular wall under similar probe translation. In other words, for meaningful interpretation, we need to put the probe in the exact configuration that it was during baseline calibration. This makes the linear pulse-echo method quite restrictive.
Using our PA-based approach, on the other hand, a patient or caregiver applying a wearable sensor based on general anatomical landmarks would have a high probability of obtaining a valid diagnosis. This built-in tolerance to user error provides a safety margin against false negatives (missed shunt failures). This matters most when monitoring elevated ICP via the proxy of ventricular expansion) in an outpatient setting. ICU patients with External Ventricular Drains (EVDs) have direct ICP measurement. We target the monitoring gap that opens once the patient leaves the hospital. Our PA-based monitoring approach provides a reliable, non-invasive surrogate for tracking ventricular volume after the EVD has been removed. This addresses a major limitation in long-term management of hydrocephalus.

Our results argue for safer, non-invasive diagnostics to reduce infection and hemorrhage risks[122,123]as compared to gold standard invasive ICP monitoring[112]. By using tissue acoustic properties alone, this modality also offers a favorable safety profile compared to contrast-enhanced ultrasound[124]. Future efforts will require extending our models to complex 3D human skull geometries and validating them experimentally in large-animal models (e.g., non-human primates). Additionally, characterizing the nonlinearity parameter of CSF and the brain in vivo will improve experimental correlation.

Apart from its immediate implications for monitoring ICP post-shunt treatment, this approach could also be used for early detection and disease progression monitoring in resource-limited settings. Alternatively, it could also be integrated into existing ultrasound imaging modalities for diagnosing hydrocephalus (e.g., in infants) to improve their accuracy, as our method does not rely on
operator skill and favorable acoustic windows[48,125,126].

## 4.5  Conclusions

This chapter showed the computational feasibility of using the parametric acoustic array effect to non-invasively monitor variations in ventricular volume (a proxy for ICP changes) associated with hydrocephalus. The acoustic nonlinearity contrast between brain parenchyma and cerebrospinal fluid produces a steady, detectable signal attenuation in transmission mode. PA suppression as a diagnostic contrast for hydrocephalus remains stable across a wide operational frequency band (75–125 kHz) and is tolerant to lateral probe misalignment (±5\pm 5mm). It thus addresses the main reliability barriers in wearable sensor design.

To conclude, our monitoring mechanism supports the development of operator-independent, continuous, portable monitoring tools that rely on tissue acoustic properties. Hopefully, this could reduce the clinical risks and healthcare burdens associated with current invasive hydrocephalus management methods.

## Chapter 5In-vitroHigh-throughput Ultrasound Neuromodulation: Platform Development and Proof-of-Concept

## 5.1  Introduction

Noninvasive neuronal stimulation allows researchers to modulate brain activity without surgical intervention. Traditional modalities like transcranial electric stimulation (tES)[49]and transcranial magnetic stimulation (TMS)[50]are widely used in basic and translational neuroscience, but they suffer from low spatial selectivity because their applied electric and magnetic fields diffuse easily[51,52].

In contrast, Focused Ultrasound (FUS) offers an alternative by facilitating the propagation of mechanical waves deep within the neuronal tissue without compromising spatial targeting precision. These mechanical waves, based on the pulsing regime, can elicit several thermal and non-thermal bioeffects (such as acoustic cavitation, fluid streaming, and radiation pressure)[53]. Consequently, ultrasound as a tool for noninvasive neuromodulation has garnered increasing interest in recent years. Supporting investigations have revealed the role of polymodal US-neuron interaction, including acoustic cavitation[127,128,129], shear stress[130,131], and radiation pressure[132,133], across diverse neuronal populations[132,134,135], as well as across different species (such as worms, rodents, and non-human primates)[133,136,137,138]. However, despite these encouraging findings, the complex nature of US-neuron interactions remains elusive. US exposure settings that may lead to a desired robust activation or suppression of certain neuronal populations are poorly understood[139,140]. Furthermore, the specific genes and molecular pathways responsible for neuromodulation within neurons are not fully characterized. This underscores the need for further controlledin-vitroinvestigations to methodically disentangle the cellular and molecular basis of US-mediated neuromodulation.

A critical challenge in advancing ultrasound neuromodulation is the fundamental trade-off between spatial precision and penetration depth. Mechanical stimuli elicit diverse neuronal responses, ranging from transient to sustained, depending on their magnitude and location[141]. To apply mechanical stimuli at cellular and subcellular levels, patch clamp tips or atomic force microscopy (AFM) cantilevers have been used in the literature at nanometer spatial resolution and piconewton force sensitivity[142,143]. However, therapeutic ultrasound (1-10 MHz) operates on much larger scales (0.15-1.5 mm). While the acoustic radiation force is an established biophysical mechanism for ultrasound neuromodulation[144,145], both the targeting precision and magnitude of mechanically induced stress show a positive dependence on frequency. This creates a challenging scenario: higher spatial targeting (sub-millimeter) necessitates the application of very high frequencies (i.e., exceeding 10 MHz)[54]. However, increasing the frequency restricts the penetration depth, thereby limiting the proposed method to superficial applications.

We address these limitations by developing an in-vitro apparatus[146]that isolates the specific mechanical effects of ultrasound (such as acoustic radiation force (ARF)) from thermal and streaming confounders. We also show that using contrast-enhanced ARF in combination with biospheres can enable targeted, subcellular mechanical stimulation at lower, clinically relevant frequencies. Our efforts in this chapter focus on the preliminary work required to design and validate this in vitro platform. We first outline the design of the apparatus, which is optimized to enhance acoustic radiation force while suppressing thermal effects and fluid shear forces[55,56,144]. We then introduce the theoretical framework for using micron-scale, biocompatible metallic spheres to locally amplify mechanical stress via their high acoustic impedance. Finally, we present preliminary physical and biological experiments utilizing Dorsal Root Ganglion (DRG) neurons and surrogate 4T1 cells to validate the platform’s capabilities.

## 5.2  Methods

## 5.2.1  Experimental Setup Design

To provide a controlled environment to promote the acoustic radiation force while minimizing thermal effects and fluid-streaming-related shear forces, our experimental setup was designed for simultaneous US exposure and high-throughput calcium imaging (Figure5.1a). The setup was based on an inverted fluorescent microscope (Nikon Ti, Japan). US waves were transmitted from above using a custom-made40mm40\text{\,}\mathrm{m}\mathrm{m}diameter 0.5 MHz focused transducer (F# 0.75) in a direction perpendicular to the bottom of the experimental chamber. The transducer was coupled to the experimental chamber using a 3D-printed cone filled with degassed deionized water and an acoustically transparent film at the interface. The outer experimental chamber was a 3D-printed cylindrical well fitted with a glass bottom and filled withC​a2+Ca^{2+}imaging buffer solution, in which the cell culture dish was placed at a2mm2\text{\,}\mathrm{m}\mathrm{m}elevated position. This ensured that the pressure release surface due to the water-air interface at the bottom was away from the area where the cells were cultured (Figure5.1b). Furthermore, to avoid the formation of local minima caused by standing waves, we established a consistent distance of3mm3\text{\,}\mathrm{m}\mathrm{m}between the substrate and the tip of the FUS cone or collimator. This parameter was determined through numerical simulations and was validated experimentally through pulse and echo measurements.

To optimize acoustic transmission and cell viability, our design entailed a comprehensive investigation of different materials for cell culture substrates (such as glass coverslips, mylar, and polymers) and several types of coatings on top (poly-d-lysine plus laminin, matrigel, and collagen). We found that culturing cells directly on a polymer bottom dish (ibidi, Germany) with poly-D-lysine plus laminin pre-coating provided optimal results. The selection of a thick polymer substrate (150μ​m150\text{\,}\mu\mathrm{m}) allowed maximal US transmission and minimal heating owing to acoustic absorption. To avoid fluid streaming (Figure5.1b) due to the presence of free fluid between the substrate and FUS cone, a2%2\text{\,}\%wt/vol agarose layer was added over the cells. This demonstrably reduced the streaming without affecting the acoustic fields.

Finally, to minimize the unpredictable effects of cavitation, a rigorous degassing protocol was established. We degassed all relevant fluids that came in contact with the cells, such as the calcium imaging buffer and agarose solution, using an ultrasonic degasser (Branson CPX2800H) at a temperature below the agarose gelation point ( 50°C). We verified the absence of cavitation activity optically by observing high frame time recordings of sonication (10million10\text{\,}\mathrm{m}\mathrm{i}\mathrm{l}\mathrm{l}\mathrm{i}\mathrm{o}\mathrm{n}frames per second) (Figure5.1d), confirming the efficacy of our degassing protocol.Figure 5.1:High Throughput US Apparatus for in-vitro Neuromodulation a) Schematic showing in-vitro aparatus with poly-modal US interaction with DRG neurons, b) US pulse sequence used in the in-vitro characterization, c) Finite elmement simulation for acoustic characterization (i-ii), Prevention of fluid streaming using agarose layer(iv), and Thermal effects (v) d) Ultrasonic degassing and qualitative estimation of cavitation with high frame rate optical microscopy

## 5.2.2  US-Pulse Parameters

Our ultrasound pulsing sequence for varying acoustic stimuli involves a 3-layered structure(Figure5.1c). Careful design of pulse parameters controls the degree to which thermal and streaming effects are amplified relative to mechanical stimulation. In the top layer, the total sonication duration (SD) was kept at10sec10\text{\,}\mathrm{s}\mathrm{e}\mathrm{c}. This is interleaved with15sec15\text{\,}\mathrm{s}\mathrm{e}\mathrm{c}and25sec25\text{\,}\mathrm{s}\mathrm{e}\mathrm{c}of the idle period for background measurements. Each SD is, in turn, divided into a set of burst durations (BD) lasting100msec100\text{\,}\mathrm{m}\mathrm{s}\mathrm{e}\mathrm{c}with a repetition frequency of1Hz1\text{\,}\mathrm{H}\mathrm{z}or2Hz2\text{\,}\mathrm{H}\mathrm{z}. Each burst can have various pulse distributions (e.g., continuous, modulated, or pulsed). Lastly, each pulse contains a waveform at the carrier frequency of0.5MHz0.5\text{\,}\mathrm{M}\mathrm{H}\mathrm{z}.

## 5.2.3  Theoretical Formulation of Acoustic Radiation Force

To establish the physical basis for applying localized mechanical stress to individual cells using contrast agents, we evaluated the Acoustic Radiation Force (ARF). ARF is a time-averaged net force on an object (e.g. a sphere) placed in an acoustic field due to the interaction between incident and scattered acoustic field from the object.[147]

For objects of arbitrary size,𝑭rad\bm{F}^{\mathrm{rad}}can be calculated by integrating the second-order pressure (also known as radiation pressure) over the surface of the object.[148,149,150]. Based on this definition, a relatively easier and versatile approach[151]to quantify the ARF is to compute the scattered acoustic field owing to the presence of the object and employ a numerical approach to compute the change in momentum flux.[152]. Assuming the fluid medium to be inviscid the second-order radiation pressure can be expressed in terms of first-order linear quantities as[153]:⟨p2⟩=12ρ0c02⟨p1⟩2−12ρ0⟨v1⟩2\left\langle p_{2}\right\rangle=\frac{1}{2\rho_{0}c_{0}{}^{2}}\left\langle p_{1}{}^{2}\right\rangle-\frac{1}{2}\rho_{0}\left\langle v_{1}{}^{2}\right\rangle(5.1)

whereρ0\rho_{0}andc0c_{0}are the equilibrium fluid density and speed of sound, andp1p_{1}andv1v_{1}are the time-harmonic linear acoustic pressure and particle velocities, respectively. Here⟨.⟩\langle.\rangledenotes time averaging. By integrating the normal component ofp2p_{2}over the surface of the particle (S0S_{0}) acoustic radiation pressure can be computed as[150]:𝑭rad=∫S0p2​𝐧​𝑑𝐚−∫S0ρ​⟨(𝐯𝟏​𝐧)⋅𝐯𝟏⟩​𝑑𝐚\bm{F}^{\mathrm{rad}}=\int_{S_{0}}p_{2}\mathbf{n}d\mathbf{a}-\int_{S_{0}}\rho\langle(\mathbf{v_{1}n})\cdot\mathbf{v_{1}}\rangle d\mathbf{a}(5.2)

Here, the second term on the right side is a compensating term that accounts for the convective momentum flux due to the time-dependent movement of the surface enclosing the particles​(t)s(t)which is considered a fixedS0S_{0}in the boundary integration.

For a small spherical object of radiusaain a progressive ultrasound field of wavelengthλ\lambdasuch thata≪λa\ll\lambda, ARF can be expressed as[154]:𝑭rad=4​π3​a3​[Im⁡[f1]​κ02​⟨pin2⟩+Im⁡[f2]​3​ρ04​⟨vin2⟩]​𝒌\bm{F}^{\mathrm{rad}}=\frac{4\pi}{3}a^{3}\left[\operatorname{Im}\left[f_{1}\right]\frac{\kappa_{0}}{2}\left\langle p_{\text{in }}^{2}\right\rangle+\operatorname{Im}\left[f_{2}\right]\frac{3\rho_{0}}{4}\left\langle v_{\text{in }}^{2}\right\rangle\right]\bm{k}(5.3)

Whereκ0\kappa_{0}andρ0\rho_{0}is the isentropic compressibility and density of the background medium,pinp_{\text{in }}andvinv_{\text{in }}are incident first-order pressure and velocity fields.f1f_{1}andf2f_{2}are the compressibilities and density contrast factors, respectively, on which the magnitude of the radiation force depends. This strong dependence on acoustic contrast indicates that introducing a bio-sphere with a significantly higher acoustic impedance than the surrounding tissue can generate highly localized mechanical stress.

## 5.2.4  Formulation of Dynamic Acoustic Radiation Force

To explore the theoretical potential of simulating transient tactile stimuli, we evaluated Dynamic Radiation Force (DRF). Several studies have demonstrated that tactile perception arises primarily from the leading and trailing edges of transient mechanical pulses, highlighting heightened neural sensitivity to the temporal derivative of the applied stimulation[155,156]. This indicates that neural structures might be more sensitive to the gradient of applied stimulation. Thus, exploring the effect of time-varying radiation force or Dynamic Radiation Force (DRF), widely used in vibroacoustography[157], on the activation of bio-sphere-labeled neurons is worth exploring in future iterations. DRF on an areaSSsubjected to an acoustic wave with energy density⟨E⟩\langle E\ranglecan be described as:F=dr​S​⟨E⟩F=d_{r}S\langle E\rangle(5.4)

wheredrd_{r}is the vector drag coefficient in the wave propagation direction. To produce an oscillating radiation force, incident ultrasound (f0=ω0/2​πf_{0}=\omega_{0}/2\pi) is typically amplitude modulated at a desired low frequency (Δ​f=Δ​ω/2​π\Delta f=\Delta\omega/2\pi), typically in the kHz range[158]. Notably, nonlinearities within the medium can induce parametric amplification of the DRF, leading to even finer subwavelength localization of forces within the kilohertz range[159].

## 5.2.5  Quantification of ARF-induced Bio-sphere Displacement

To empirically quantify the displacement of biospheres owing to the ARF without biological confounders, we utilized anin-vitrophantom setup similar to that shown in Figure5.1a. This setup consists of metallic bio-spheres embedded in a layer of an agarose gel matrix (1%1\text{\,}\%wt/vol ). Under the assumption of small linear deformation,Fr​a​d=−ke​xF^{rad}=-k_{e}x(Hooke’s law), wherekek_{e}is the effective stiffness constant of the hydrogel. Consequently, measuring the displacement allows for the estimation of the ARF.

Consider a sphere placed in the focal plane; the scattered fieldu​(r,z)u(r,z)from the object interferes with the undiffracted reference field to generate an interference pattern characterized by a central bright spot and surrounding rings. A change in this interference pattern was observed upon the application of ultrasound, which displaced the sphere downwards, effectively shifting the focal plane of the microscope upwards. Thus, by tracking the central pixel intensity as a function ofzz, we can obtain a set of calibration images that serve as a look-up table. We then compared them within-vitrorecordings of sphere movements due to ultrasound and quantified the ARF-induced displacement with precision.

## 5.2.6  Preparation of Cellular Models

To evaluate the operational capacity of the apparatus, we utilized Dorsal Root Ganglion (DRG) sensory neurons isolated fromPirtGCaMP6f\text{Pirt}^{\text{GCaMP6f}}mice, in which the pan-sensory neuronal Pirt promoter drives the expression of GCaMP6f in more than 95% of sensory neurons. These neurons were selected due to their baseline sensitivity to mechanical stimuli.

Furthermore, to demonstrate the practical feasibility of physically attaching micro-particles to living cells within a 3D matrix, we conducted a proof-of-concept labeling assay. Because robust protocol optimization was required to refine the avidin-biotin attachment chemistry prior to utilizing sensitive primary DRG neurons, we pragmatically employed GFP-expressing 4T1 cells (chosen for their accessibility, robust adherence, and ease of manipulation) as a technical surrogate, and labeled them with avidin-coated iron oxide biospheres (Banglabs, USA). The protocol involved the creation of a 3D cell culture environment: a base layer of agarose gel (1%1\text{\,}\%wt/vol) was prepared, followed by the addition of a collagen (TeloCol 6, Advanced Biomatrix, USA) layer. After growing the 4T1 cells to confluency, they were incubated with anti-GFP biotin, and then the biospheres were added. These biosphere-labeled cells were then plated onto a collagen matrix, with a layer of agarose added on top.

## 5.3  Preliminary Results

## 5.3.1   DRG Activation and Acoustic Parameter Study

We conducted preliminary experiments using the isolated DRG sensory neurons to test the apparatus. We must emphasize that these findings are preliminary and currently lack comprehensive controls. Future trials need to include proper controls such as sham sonications, temperature monitoring, and pharmacological blockers. However, they serve as a proof of concept for the apparatus design.

We identified exploratory US settings (excitation frequency: 0.5 MHz; pressure: 0.67 MPa; pulse duration: 1 msec; pulse repetition frequency: 1 Hz; Number of pulses: 10) where more than 20% of dissociated DRG sensory neurons indicated qualitative activation (Figure5.2a). Upon using a long pulse duration (100 ms) with a pulse repetition frequency of 1 Hz and 10 pulses, we observed activation of 31.7% at 0.67 MPa and 33.49% at 0.8 MPa (Figure5.2b). Interestingly, we observed a delayΔ​t\Delta tof7sec7\text{\,}\mathrm{s}\mathrm{e}\mathrm{c}in the trigger of an action potential at 0.67 MPa, which reduced to3sec3\text{\,}\mathrm{s}\mathrm{e}\mathrm{c}at 0.8 MPa. Long pulse durations are associated with streaming-induced shear stresses and heating, which may play a role in the delayed onset of neuronal activation.Figure 5.2:DRG neurons expressing GCaMP6f stimulated by ultrasound. a) Top: Several cells show increased fluorescence levels. This demonstrates preliminary US-mediated neuronal activation. Bottom: Quantification of the increase in relative fluorescence levels during US application. Bottom: Histogram showing that the US activated a heterogeneous group of neurons, including small-, medium-, and large-diameter neurons. b) Long pulse durations (100 msec) at different pressures (top: 0.67 MPa and bottom:0.80 MPa) lead to delayed onset of DRG neuron activation.Figure 5.3:a) Schematic of the experimental setup indicating micro-spheres being pushed down by Ultrasound ARF leading to blurring of the image once in focus, b) Normalized intensity drop of the central pixel, c) Calibration curve obtained by z-stack images of the same sphere, d) quantification of the ARF induced displacement.

## 5.3.2  Physical Validation of ARF-induced Bio-sphere Displacement

An experimental demonstration of the optical tracking technique is shown in5.3.6μ​m6\text{\,}\mu\mathrm{m}biospheres (Banglabs, USA) were embedded in an agarose gel matrix (1%​w​t/v​o​l$1\text{\,}\%$wt/vol). A 500-cycle ultrasound pulse train at 3.3 MHz was applied at varying pressures (0.2, 0.5, and 0.7 MPa). This displaced the spheres out of the microscope focal plane and resulted in a blurred image (Figure5.3a).

We quantified the drop in the central pixel’s intensity by tracking it during sonication at 0.5 million frames per second using high-speed videography with a Shimadzu HPV-X2 camera (Kyoto, Japan). A moving average was applied to the normalized traces to remove the high-frequency measurement noise. The drop in the mid-pixel intensityΔ​I\Delta Iwas then quantified (Figure5.3b). Additionally, a set of z-stack images of the sphere was obtained to provide a mapping between the z-position and central pixel intensity. This calibration trace served as a look-up table to translate the drop in intensityΔ​I\Delta Ito displacementddin microns (Figure5.3c). The sphere moved by8μ​m8\text{\,}\mu\mathrm{m}at an input of 0.7 MPa (Figure5.3d). We suggest that this magnitude of displacement, when localized to a cellular membrane, could generate sufficient local mechanical stress to elicit a functional response.

## 5.3.3   Observation of ARF on Bio-sphere-labeled 4T1 Cells

We prepared biosphere-labeled GFP 4T1 cells using the previously outlined 3D culture procedure. We verified their viability and confirmed successful physical attachment to the biospheres (Figure5.4a) using fluorescent imaging.

We then applied continuous wave (CW) excitation at 3.3 MHz at three different pressure levels (0.05, 0.075, and 0.1 MPa) to facilitate optical tracking. While short-pulse excitations are ideal for studying purely ARF-induced displacement, they require ultra-high frame rate acquisition to discern sphere motion. The sphere was demonstrably pushed downward by ultrasound. This is evident from the blurred base image corresponding to a sonication pressure of 0.1 MPa (Figure5.4b).

Background subtraction and SVD filtering showed the differential motion of the sphere relative to the surrounding cell membrane. We believe that this observed motion arises from the radiation force exerted on the sphere owing to its contrasting acoustic properties. These results provide an initial proof-of-concept for targeted cellular mechanostimulation using our in-vitro setup.Figure 5.4:a) Schematic showing 3D cell culture where GFP 4T1 cells cultured on collagen are sandwiched between two layers of agarose. Fluorescent microscopy in the bottom confirms cell viability and successful attachment of biospheres. b) Ultrasound sonication trial with 3.3 MHz CW excitation at three different time points showing the base, background subtracted and SVD filtered images to quantify the ARF-induced bead displacement qualitatively.

## 5.4  Discussion

The aim of this chapter was to develop and validate anin-vitroplatform designed to explore the poly-modal mechanisms underlying ultrasonic neuromodulation. By creating an apparatus that allows for simultaneous ultrasound exposure and high-throughput calcium imaging, we established a framework to evaluate specific acoustic parameters while minimizing macroscopic environmental confounders.

Although the biological investigations presented here are still in their early stages, they offer valuable initial observations that confirm the apparatus’s utility. For example, the preliminary data show a different temporal response of DRG neurons to varying pulse durations. Longer pulses (100msec100\text{\,}\mathrm{m}\mathrm{s}\mathrm{e}\mathrm{c}) led to a delayed onset (Δ​t≈3sec−7sec\Delta t\approx$3\text{\,}\mathrm{s}\mathrm{e}\mathrm{c}$-$7\text{\,}\mathrm{s}\mathrm{e}\mathrm{c}$). This suggests the potential involvement of separate transduction pathways and slow-acting mechanisms. This is likely due to residual thermal accumulation or shear stress as opposed to the immediate effect of acoustic radiation force on ion channels. This shows the necessity of our agarose overlay and degassing protocols for isolating mechanotransduction events from bulk fluid dynamics.

Moreover, the introduction and quantification of biosphere labeling represent a promising step toward bridging the gap between applying forces on the cell membrane, similar to precise microindentation using AFM, and non-invasive, low-spatial-resolution therapeutic ultrasound.

The selection of 4T1 cells for the bio-sphere experiments indicates the preliminary nature of this research. Demonstrating the actuation of biospheres on easily manipulated 4T1 cells was a pragmatic step before adapting the protocol to more sensitive primary neuronal populations. Our data suggest that this contrast-enhanced approach can generate localized displacements of up to8μ​m8\text{\,}\mu\mathrm{m}at clinically relevant frequencies. Thus, localized membrane deformation can be achieved without sonicating the entire tissue volume by using the acoustic impedance mismatch of the bio-spheres. Essentially, we devised a way to convert a macroscopic acoustic field into a microscopic, targeted mechanical stimulus.

Significant future work is required to translate these preliminary findings into firm conclusions. Through biological controls, larger sample sizes, and rigorous statistical evaluations, we must confirm mechanosensitive channel gating. The specificity of the ligand-receptor binding used to attach the bio-spheres also requires further optimization to ensure the targeted excitation of specific neuronal subtypes. Lastly, evaluating the theoretical Dynamic Acoustic Radiation Force (DRF) formulations proposed here will be important to determine if oscillating mechanostimuli can better match the time constants of specific neural circuits.

## 5.5  Conclusions

The primary contribution of this work are laying the engineering groundwork for a targetedin-vitroultrasound neuromodulation platform.
- •

Design of an Artifact-MitigatedIn-VitroApparatus:We designed a high-throughput platform pairing focused ultrasound with fluorescence imaging. This configuration ensures accurate acoustic targeting while suppressing bulk fluid streaming.
- •

Quantification of Acoustic Radiation Force:We developed an optical tracking method capable of measuring micro-scale displacements ( 8μ​m\mu m) of targets subjected to localized acoustic radiation forces. This technique provides a reliable calibration metric for future mechano-stimulation research.
- •

Framework for Contrast-Enhanced Mechanostimulation:We introduced a stimulation approach that uses biocompatible metallic microspheres as localized acoustic stress concentrators. We validated the labeling protocols in 4T1 cell lines and confirmed the actuation mechanisms; we then showed that macroscopic acoustic fields can be translated into targeted, subcellular mechanical stimuli at clinically viable frequencies.

In conclusion, although future controlled studies are needed to fully determine the biological mechanisms underlying the efficacy of ultrasound-sonicated neuronal activation, the in vitro platform developed here may serve as an essential foundation for exploring the molecular mechanisms underlying targeted, non-invasive neuromodulation.

## Chapter 6Summary and Conclusions

## 6.1  Thesis Objectives and Context

This thesis bridges the gap between the potential of acoustic holography and its clinical realization in transcranial ultrasound (TUS) therapies. Focused ultrasound has become an effective tool for non-invasive neuro-intervention; however, its widespread adoption faces key challenges, including the prohibitive cost of phased arrays, electronic packaging constraints, and the correction of skull aberrations at high frequencies[10,21].

Acoustic holography, although, offers an accessible alternative by using passive, patient-specific lenses to correct skull-induced distortions[23], it has two bottlenecks toward clinical translation: (1) low-fidelity design approximations that fail at clinical sub-megahertz frequencies, (2) reliance on imaging modalities such as magnetic resonance imaging (MRI) for precise lens–skull registration[41]. We addressed these limitations by modeling the holographic lens as an acoustically thick volume. Furthermore, we modeled the human skull as a nonlinear medium to use the parametric array effect for skull-lens registration. In addition, we addressed the challenge of noninvasive monitoring of the intracranial environment during treatment and designed an artifact-mitigatedin vitroplatform that isolates specific ultrasonic mechanotransduction mechanisms for targeted neuromodulation.

## 6.2  Thesis Contributions

The chapter-wise key contributions of the thesis are listed below in juxtaposition with the current state-of-the-art.

## 6.2.1  Hologram Topology Optimization (HASA-ADAM)

State of the Art:Current rapid design methods for acoustic holograms, such as the Iterative Angular Spectrum Approach (IASA), rely on the Thin-Element Approximation (TEA) to generate the lens post optimization[23]. These models treat the lens as a simple 2D phase screen, ignoring internal wave dynamics. While full-wave time-domain solvers can capture these physics, they remain computationally prohibitive for iterative clinical-scale lens design[37].

Contribution:InChapter2, we showed that TEA breaks down at the sub megahertz frequencies required for transcranial targeting. At frequencies near1MHz1\text{\,}\mathrm{M}\mathrm{H}\mathrm{z}and below, the lens enters an acoustically thick regime (L≫λL\gg\lambda), where the high aspect ratio of lens features inducesrefractive walk-offand diffraction spreading the energy laterally leading to pixel migration and volumetric cross talk.

To overcome this limitation, we introducedHASA-ADAM. HASA-ADAM shifts from phase-screen estimation to true volumetric topology optimization. By optimizing the 3D topology rather than a 2D phase profile, this framework accounts for internal wave propagation, amplitude modulation, and edge diffraction without the computational burden of time-domain solvers due to frequency domain propagation. This approach achieved a PSNR improvement of approximately7dB7\text{\,}\mathrm{d}\mathrm{B}over conventional methods, enabling the rapid generation (<20<20min) of large-aperture lenses (≈60mm\approx$60\text{\,}\mathrm{m}\mathrm{m}$) for transcranial focusing.

## 6.2.2  Nonlinear Acoustic Registration

State of the Art:The effectiveness of hologram lenses to correct for skull-aberration depends on accurate registration with the skull anatomy. Currently, sub-millimeter registration relies on MR-guided TUS (MRgFUS)[44], which monopolizes expensive imaging infrastructure, or optical neuronavigation[42], which suffers from error margins (∼\sim1.5–3.5 mm) insufficient for high-frequency targeting. These limitations make passive transcranial holography inaccessible and inaccurate.

Contribution:Historically, acoustic models have treated the human skull purely as a passive, linear aberrator. InChapter3, we reconceptualized the skull as anactive nonlinear emitter. By exploiting the extreme contrast in the nonlinearity parameter (β\beta) between cortical bone and soft tissue[47], we introduced the Parametric Array (PA) signal as a direct, real-time feedback mechanism for active alignment of the lens with skull geometry.

We showed the mechanisms underlying this sensitivity: angular misregistration triggersVolumetric energy trappingandshear mode conversionthrough which misaligned primary acoustic energy is trapped within the diploë layer and may be converted into slow-moving shear waves. We also showed that parametric generation efficiency scales inversely with the cube of wave velocity (c−3c^{-3}). This trapped energy may act as a volumetric pump, amplifying the difference-frequency (Δ​f\Delta f) signal. Our approach thus provides an alternative hologram-skull registration method by correlating optimal sub-millimeter alignment (θ=0∘\theta=0^{\circ}) with a drop in the PA signal (≥20%\geq 20\%), which circumvents the spatial limitations of optical tracking and the infrastructure burden of MRI.

## 6.2.3  Non-invasive ICP Monitoring in Hydrocephalus

State of the Art:The clinical management of hydrocephalus relies on invasive External Ventricular Drains (EVDs)[112], which carry risks of infection and hemorrhage, whereas Non-invasive surrogates, such as Transcranial Doppler[114,115], are indirect measurements often confounded by systemic hemodynamics and operator variability.

Contribution:Building upon our nonlinear acoustic findings, inChapter4we extended the parametric array effect to introduce a novel diagnostic paradigm based onvolumetric suppression. We established that the volumetric replacement of higher-nonlinearity brain tissue (β≈4.7\beta\approx 4.7) with lower-nonlinearity cerebrospinal fluid (β≈3.6\beta\approx 3.6) in the focal zone causes a reduction in the nonlinear amplifier gain of the intracranial medium.

We showed that clinically relevant ventricular expansion yields a detectable∼\sim10% signal attenuation in transmission mode which is above the detection threshold of a hydrophone. By proving that this diagnostic margin remains stable across a wide operational frequency band (75–125kHz) and is highly tolerant to lateral probe misalignment (±5\pm 5mm), this contribution provides groundwork for wearable, operator-independent intracranial monitoring of ventricle expansion in hydrocephalus.

## 6.2.4  In-Vitro Neuromodulation Platform Development

State of the Art:In-vivoandin-vitroultrasonic neuromodulation studies are frequently confounded by bulk fluid streaming, thermal accumulation, and off-target auditory artifacts[55]. Tools like atomic force microscopy (AFM) provide high-resolution mechanical stimulation but lack therapeutic penetration depth. Thus, to target the subcellular membrane, we need to use frequencies above 10 MHz, which restricts the modality to superficial targets[54].

Contribution:InChapter5, we developed an artifact-mitigatedin-vitrohigh-throughput hardware platform. We isolated the Acoustic Radiation Force (ARF) from thermal and streaming confounders using specific geometric spacing, degassing protocols, and agarose tissue-mimicking overlays.

We also developed a proof-of-concept prototype for contrast-enhanced mechanostimulation. We showed that the acoustic impedance mismatch acts as a local stress concentrator by attaching bio-spheres to cellular membranes. We quantified that this approach converted a macroscopic acoustic field (0.5– 1 Hz) into a targeted subcellular mechanical displacement (∼8µ​m\sim$8\text{\,}\mathrm{\SIUnitSymbolMicro m}$) using optical tracking. Thus, using our approach, localized mechanical stimuli can be achieved without using high-frequency, high-intensity fields.

## 6.3  Significance

The four contributions define a framework forPrecision Passive Acoustics. By treating the holographic lens as a volumetric refractive element and the skull as a nonlinear medium, we converted obstacles into engineering tools.
- 1.

Design:A patient-specific lens is generated using topology optimization (HASA-ADAM) to ensure optimal diffraction-limited focal quality for both complex and point targeting. We did this by overcoming the limitations of the thin-film approximation in phase-based hologram optimization.
- 2.

Register:During the procedure, the lens is aligned using the nonlinear parametric acoustic signature of the skull itself. This eliminates the need for continuous MRI monitoring, making transcranial ultrasound therapy more accessible and portable.
- 3.

Monitor:The parametric array principles can be used diagnostically to track intracranial volumetric expansion of the ventricles. This approach ensures patient safety during hydrocephalus monitoring or treatment without the need for invasive probes.
- 4.

Modulate:The engineeredin-vitroplatform provides a standardized apparatus to isolate and study the mechanotransduction pathways required for future targeted non-invasive neuromodulation therapies.

## 6.4  Limitations

Biological Validation of Mechanostimulation.The neuromodulation platform (Chapter5) represents exploratory proof-of-concept work. Although the actuation of the biospheres was validated, the preliminary biological observations lacked the exhaustive controls, such as sham sonications, precise continuous temperature monitoring, and pharmacological blockers required to confirm mechanosensitive channel gating.

Material Characterization.The fidelity of topology optimization is highly sensitive to the exact material properties of the 3D-printed lens. Sub-wavelength discrepancies in the speed of sound owing to manufacturing and curing variations can lead to axial focal shifts, thereby requiring post-print calibration.

Elastic Modeling Cost.The HASA propagator currently used for iterative lens design relies on a fluid model. Although our registration investigations highlighted the critical role of shear modes in the skull and lens, incorporating full elastic wave propagation into a topology optimization loop remains computationally expensive for rapid clinical optimization and prototyping.

Skull Variability and Trapped Gas.Nonlinear sensing strategies rely on the cumulative generation of parametric waves. Clinical scenarios involving trapped postoperative gas (pneumocephalus) or large variations in bone porosity induce severe acoustic impedance mismatches (Zskull/Zair≈7500Z_{\text{skull}}/Z_{\text{air}}\approx 7500) that scatter primary energy and destroy phase coherence, which can extinguish the diagnostic feedback loop. This though represents a small population of patients.

## 6.5  Future Directions

Sonogenetics and Targeted Mechanopharmacology.Future studies should apply biological controls to validate targeted neuromodulation, building on the in vitro biosphere platform. Researchers could functionalize these spheres to target specific ion channels, enabling precise, low-frequency ultrasonic modulation of neural circuits.

Elastic Topology Optimization.Future iterations of HASA-ADAM should integrate computationally efficient elastic wave approximations. This could pioneer shear-mode holography, in which passive lenses are deliberately crafted to exploit mode conversion to minimize off-target skull heating or enhance transcranial energy transfer.

Autonomous Closed-Loop Alignment.Future work could realize autonomous, closed-loop lens registration in outpatient clinical environments by coupling the real-time nonlinear feedback signal with six-degree-of-freedom robotic positioning systems and eliminating operator dependency.

In-VivoValidation of Diagnostic Sensing.

The hydrocephalus monitoring work has so far been validated only computationally. Translation to a large animal model — non-human primates being the most relevant anatomically — is the necessary next step. Physiological confounders that are absent from phantoms, including pulsatile cerebral blood flow, respiratory motion, and the variable acoustic attenuation of scalp and subcutaneous fat, will all need to be characterized before the approach can be taken into a clinical trial.

## 6.6  Conclusion

This thesis shows that the key obstacles to holography-assisted high-precision transcranial ultrasound therapy, specifically aberration correction and MRI-free registration, can be solved. The solution lies in modeling wave propagation in acoustically thick diffractive elements and exploiting the intrinsic nonlinear acoustic signatures of cranial tissues. We have developed a novel framework for acoustic hologram design and registration, and also demonstrated its use for monitoring ventricular expansion in hydrocephalus. These contributions make transcranial neuro-therapeutic and diagnostic tools more accessible to everyone, providing the engineering foundation needed to translate them into routine clinical practice.

## Appendix AHASA Wave Propagation Assumptions

## A.1  The Parabolic (One-Way) Wave Equation

The core of our HASA-ADAM hologram optimization is the Heterogeneous Angular Spectrum Approach (HASA), which uses a frequency-domain forward-marching scheme to model wave propagation through an aberrating skull layer. It relies on the parabolic (also known as one-way) approximation of the wave equation. In this section, we will derive the paraxial wave equation without backward-propagating reflections.

Wave propagation in a heterogeneous, non-absorbing medium is governed by the Helmholtz equation. For a time-harmonic acoustic pressure fieldP​(𝐫)P(\mathbf{r})operating at an angular frequencyω\omega, the governing equation is[80]∇2P​(𝐫)+k2​(𝐫)​P​(𝐫)=0\nabla^{2}P(\mathbf{r})+k^{2}(\mathbf{r})P(\mathbf{r})=0(A.1)

wherek​(𝐫)=ω/c​(𝐫)k(\mathbf{r})=\omega/c(\mathbf{r})is the spatially varying wavenumber andc​(𝐫)c(\mathbf{r})represents the local speed of sound.

To isolate the forward-propagating behavior, the total pressure field is factored into a slowly varying complex envelopeU​(𝐫)U(\mathbf{r})[74]that modulates a fast-oscillating carrier wave traveling along the primary propagation axiszz:P​(x,y,z)=U​(x,y,z)​ei​k0​zP(x,y,z)=U(x,y,z)e^{ik_{0}z}(A.2)

Here,k0=ω/c0k_{0}=\omega/c_{0}serves as a constant reference background wavenumber. Substituting this assumed solution into the Helmholtz equation requires evaluating the spatial derivatives with respect to the axial coordinatezz. Applying the product rule yields the first and second derivatives:∂P∂z=(∂U∂z+i​k0​U)​ei​k0​z\frac{\partial P}{\partial z}=\left(\frac{\partial U}{\partial z}+ik_{0}U\right)e^{ik_{0}z}(A.3)∂2P∂z2=(∂2U∂z2+2​i​k0​∂U∂z−k02​U)​ei​k0​z\frac{\partial^{2}P}{\partial z^{2}}=\left(\frac{\partial^{2}U}{\partial z^{2}}+2ik_{0}\frac{\partial U}{\partial z}-k_{0}^{2}U\right)e^{ik_{0}z}(A.4)

Inserting these expansions back into EquationA.1and dividing out the common exponential phase termei​k0​ze^{ik_{0}z}results in the exact envelope equation:∇⟂2U+∂2U∂z2+2​i​k0​∂U∂z+(k2​(𝐫)−k02)​U=0\nabla_{\perp}^{2}U+\frac{\partial^{2}U}{\partial z^{2}}+2ik_{0}\frac{\partial U}{\partial z}+\left(k^{2}(\mathbf{r})-k_{0}^{2}\right)U=0(A.5)

where the transverse Laplacian operator is defined as∇⟂2=∂2∂x2+∂2∂y2\nabla_{\perp}^{2}=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}.

The parabolic approximation imposes a restriction: the envelopeUUmust evolve slowly along the propagation axis relative to the acoustic wavelength making the second-order axial variation is vanishingly small compared to the first-order spatial variation:|∂2U∂z2|≪|2​k0​∂U∂z|\left|\frac{\partial^{2}U}{\partial z^{2}}\right|\ll\left|2k_{0}\frac{\partial U}{\partial z}\right|(A.6)

Applying this condition and neglecting the second-order axial derivative (∂2U∂z2≈0\frac{\partial^{2}U}{\partial z^{2}}\approx 0), EquationA.5simplifies into the paraxial wave equation:2​i​k0​∂U∂z=−∇⟂2U−(k2​(𝐫)−k02)​U2ik_{0}\frac{\partial U}{\partial z}=-\nabla_{\perp}^{2}U-\left(k^{2}(\mathbf{r})-k_{0}^{2}\right)U(A.7)

This approximation carries a real world implication. A second-order spatial differential equation supports two independent solutions. They represent forward- and backward-traveling waves. Dropping the∂2U∂z2\frac{\partial^{2}U}{\partial z^{2}}term reduces the system to a first-order differential equation inzzfor forward only propagation.

Thus, our formulation assumes 100% forward energy transmission across all interfaces. When this model encounters high-contrast boundaries (such as the water-to-skull interface, where the reflection coefficient is large (R≈0.57R\approx 0.57)), the algorithm enforcesR=0R=0. This overestimates transcranial transmission.

The optimizer as a result is blind to the phase decorrelation caused by internal standing waves and backscattering within the diploë layer of the skull.

## A.2  WKB (Slowly Varying Envelope) Approximation

Spectral convolution methods for heterogeneous media rely on the Wentzel–Kramers–Brillouin (WKB) approximation[74]to get analytical solutions for wave propagation through media with spatially varying (gradually varying compared to wavelength) properties. We derive the continuity constraint using the WKB approximation to show why sharp acoustic boundaries can cause spectral leakage in our HASA model.

Consider the simplified one-dimensional Helmholtz equation for a wave propagating through a heterogeneous medium:d2​Pd​z2+k2​(z)​P=0\frac{d^{2}P}{dz^{2}}+k^{2}(z)P=0(A.8)

wherek​(z)k(z)is the spatially dependent wavenumber. The WKB method gives us a solution where the amplitudeA​(z)A(z)and the accumulated phaseϕ​(z)\phi(z)are decoupled:P​(z)=A​(z)​ei​ϕ​(z)P(z)=A(z)e^{i\phi(z)}(A.9)

Let’s substitute this decoupled expression forP​(z)P(z)into EquationA.8:d2d​z2​(A​(z)​ei​ϕ​(z))+k2​(z)​A​(z)​ei​ϕ​(z)=0\frac{d^{2}}{dz^{2}}\left(A(z)e^{i\phi(z)}\right)+k^{2}(z)A(z)e^{i\phi(z)}=0(A.10)

Now let’s expand the second derivative through the product rule, get both real and imaginary terms:(d2​Ad​z2−A​(d​ϕd​z)2+i​(2​d​Ad​z​d​ϕd​z+A​d2​ϕd​z2))​ei​ϕ​(z)+k2​(z)​A​ei​ϕ​(z)=0\left(\frac{d^{2}A}{dz^{2}}-A\left(\frac{d\phi}{dz}\right)^{2}+i\left(2\frac{dA}{dz}\frac{d\phi}{dz}+A\frac{d^{2}\phi}{dz^{2}}\right)\right)e^{i\phi(z)}+k^{2}(z)Ae^{i\phi(z)}=0(A.11)

Isolating the real components provides the governing relationship for the phase accumulation:d2​Ad​z2−A​(d​ϕd​z)2+k2​(z)​A=0\frac{d^{2}A}{dz^{2}}-A\left(\frac{d\phi}{dz}\right)^{2}+k^{2}(z)A=0(A.12)

Dividing by the amplitudeA​(z)A(z)gives us a expression for the square of the local phase gradient:(d​ϕd​z)2=k2​(z)+1A​d2​Ad​z2\left(\frac{d\phi}{dz}\right)^{2}=k^{2}(z)+\frac{1}{A}\frac{d^{2}A}{dz^{2}}(A.13)

The WKB approximation requires the amplitude profile to vary so gradually that the wave amplitudeA​(z)A(z)remains decoupled from rapid phase fluctuations. Thus, its second spatial derivative is negligible compared to the square of the local wavenumber:|1A​d2​Ad​z2|≪k2​(z)\left|\frac{1}{A}\frac{d^{2}A}{dz^{2}}\right|\ll k^{2}(z)(A.14)

Under this condition, EquationA.13allows the phase gradient to be approximated by the local wavenumber (d​ϕd​z≈±k​(z)\frac{d\phi}{dz}\approx\pm k(z)). However, this truncation requires the medium’s properties to remain stable over a single acoustic wavelength. In other words, the fractional change in the local wavenumber must be small over one wavelength:|1k2​(z)​d​kd​z|≪1\left|\frac{1}{k^{2}(z)}\frac{dk}{dz}\right|\ll 1(A.15)

Now let’s relate this wavenumber constraint to material properties. We substitute the definition of the wavenumberk​(z)=ω/c​(z)k(z)=\omega/c(z)q and apply the chain rule:d​kd​z=dd​z​(ωc​(z))=−ωc2​(z)​d​cd​z\frac{dk}{dz}=\frac{d}{dz}\left(\frac{\omega}{c(z)}\right)=-\frac{\omega}{c^{2}(z)}\frac{dc}{dz}(A.16)

Substituting this derivative back into the continuity constraint (EquationA.15) and expanding this into three dimensions and normalizing against the reference background wavenumberk0=ω/c0k_{0}=\omega/c_{0}, the requirement becomes:|c2ω2​(−ωc2​∇c)|=1ω​|∇c|=cω​|∇cc|≈1k0​|∇cc|≪1\left|\frac{c^{2}}{\omega^{2}}\left(-\frac{\omega}{c^{2}}\nabla c\right)\right|=\frac{1}{\omega}|\nabla c|=\frac{c}{\omega}\left|\frac{\nabla c}{c}\right|\approx\frac{1}{k_{0}}\left|\frac{\nabla c}{c}\right|\ll 1(A.17)

EquationA.17defines the limit of the slowly varying envelope approximation, which requires the local speed of sound to vary continuously. At the water-skull interface, however, the speed of sound jumps abruptly from∼1480\sim 1480m/s to over25002500m/s across a fraction of the acoustic wavelength. This results in a step-function discontinuity that violates the≪1\ll 1inequality and breaks the decoupled phase assumption. Propagating waves thus produce artificial phase accumulation and spectral leakage in the Fourier transforms.

## Appendix BShear Wave Propagation

## B.1  Shear Mode Conversion at the Lens Interface

We analyzed the normal and shear stress temporal evolution using at the lens interface k-Wave elastic solvers assuming a shear attenuation of 10 dB/MHz within the lens. The numerical solver models the propagation of elastic waves within an isotropic solid medium by integrating the coupled first-order velocity-stress equations:ρ​∂vi∂t=∂σi​j∂xj\rho\frac{\partial v_{i}}{\partial t}=\frac{\partial\sigma_{ij}}{\partial x_{j}}and∂σi​j∂t=λ​δi​j​∂vk∂xk+μ​(∂vi∂xj+∂vj∂xi)\frac{\partial\sigma_{ij}}{\partial t}=\lambda\delta_{ij}\frac{\partial v_{k}}{\partial x_{k}}+\mu\left(\frac{\partial v_{i}}{\partial x_{j}}+\frac{\partial v_{j}}{\partial x_{i}}\right)whereviv_{i}is the particle velocity vector,σi​j\sigma_{ij}is the stress tensor,ρ\rhois the mass density,δi​j\delta_{ij}is the Kronecker delta,λ\lambdaandμ\muare the Lamé parameters of the lens material. Here, the Einstein summation convention is used for repeated indices.

First, we looked at the shear and compressional wave propagation effects at different time points. The compressional (longitudinal) wave speedcpc_{p}and shear (transverse) wave speedcsc_{s}are governed by the following elastic material properties:cp=λ+2​μρ,cs=μρc_{p}=\sqrt{\frac{\lambda+2\mu}{\rho}},\quad c_{s}=\sqrt{\frac{\mu}{\rho}}. Because bothλ\lambdaandμ\muare positive for solid media,cp>csc_{p}>c_{s}. As expected the normal stress propagated rapidly through the lens (FigureB.1b), the shear wave was noticeably delayed owing to its relatively lower speed (cs≈1300c_{s}\approx 1300m/s), as shown in FigureB.1c. Moreover, the effect of shear was only accentuated at the steep lens-water interface. Shear waves vanished beyond the lens interface as water cannot support shear propagation.

In a lossy medium, the decay of the propagating shear stressσshear​(x)\sigma_{\text{shear}}(x)can be described by:σshear​(x)=σ0​e−αshear​x\sigma_{\text{shear}}(x)=\sigma_{0}e^{-\alpha_{\text{shear}}x}whereσ0\sigma_{0}is the initial amplitude,xxis the propagation distance, andαshear\alpha_{\text{shear}}is the attenuation coefficient. Without attenuation (αshear=0\alpha_{\text{shear}}=0dB/MHz), the shear stress was more prominent, which reduced in amplitude as we increased the attenuation to 10 and 15 dB/MHz. It is to be noted that these attenuation values are much higher than that for compressional waves for a resin-based 3D-printed lens (approx. 3 dB/MHz[77]) and are only used here as worst-case scenarios.Figure B.1:Simulation of elastic wave propagation through lens topology.(a)Acoustic lens topology and the simulation domain. (Left) A 2D heat map shows the Lens Mask Profile (XY plane) with thickness ranging from 0 to 5 mm. (Middle) A 2D visualization of the computational domain in the XZ plane. (Right) A 3D view illustrating the simulation domain.(b)Temporal evolution of Normal Stress within the XZ plane. A sequence of five time snapshots (t=0.28t=0.28µs,t=0.96t=0.96µs,t=1.92t=1.92µs,t=3.85t=3.85µs, andt=5.78t=5.78µs) shows the progression of normal stress waves.(c)Temporal evolution of Shear Stress in the XZ plane for the same five time points as in (b). Shear waves are generated at the solid-fluid interface within the domain. Black arrows indicate the origin points at the lens interface.(d)A parametric study showing Shear Stress distribution in the XZ plane at a fixed time,t=3.85t=3.85µs, for three different attenuation coefficients (αshear\alpha_{\text{shear}}): 0 dB/MHz, 10 dB/MHz, and 15 dB/MHz. The higher the shear attenuation, the larger the reduction in the amplitude of shear stress .

## Appendix CExperimental Equipment

## C.1  Acoustic Hologram ExperimentFigure C.1:An arbitrary waveform generator (AWG) generates a signal, amplified to drive a transducer with an acoustic hologram. Ultrasound waves propagate through a skull in a water tank. A hydrophone on a 3D positioning system measures the transmitted acoustic pressure field. The signal is conditioned by a preamplifier (Preamp) and digitized by an oscilloscope (Scope). A computer controls data acquisition and synchronizes (SYNC) the AWG and oscilloscope.

## C.2  Acoustic Holography RegistrationFigure C.2:We affixed the transducer, hologram, and skull assembly to a rotational axis (Rotation,Θ\Theta) to cause misregistration. A 3D positioning system moves the hydrophone along the z-axis. We apply an additional 40 dB analog low-pass gain between the preamplifier (Preamp) and the oscilloscope (Scope).

## Appendix DLiterature Review

## D.1  Acoustic Holography

In TableLABEL:tab:lit_reviewbelow, we provide a summary of various design methodologies, operational parameters, and specific insights and limitations found in recent research related to acoustic holography.Table D.1:Study of Acoustic Holography LiteratureCitationMethodology & ParametersApplicationKey Findings & LimitationsMelde et al. (2016)[23]Passive Lens (IASA Optimization)
2.0 MHz
50​μ50\,\mum (SLA printing)
Aperture 50mm;Z=20Z=20mmPushing PDMS particles, 2D free-fieldReconstructed diffraction-limited beams. Limit: Assumes thin-element approximation.Brown et al. (2017)[160]Kinoforms (Binary Search)
1.9, 2.5, 3.1 MHz
Target planesMulti-frequency field generationEncoded different patterns on different frequencies. Limit: Crosstalk, lack of full-wave modeling.Brown et al. (2019)[brown2019]Composite Lens (Phase & Amp)
2.7 MHz
Far-fieldIndependent Phase/Amp modulationLimit: Loss of amplitude due to multiple plates; narrowband.Brown et al. (2020)[161]Stackable Holograms
3.0 MHz
Far-fieldReconfigurable combined fieldsHolograms can be translated relative to each other to shift target patterns.Fushimi et al. (2021)[36]Diff-PAT (Automatic Diff.)
40 kHz
PAT array /150​μ150\,\mum pixels
Near-field / 3D VolumetricComplex image reconstructionAchieved much higher PSNR than IASA (by∼\sim8 dB). Limit: Hyperparameter tuning needed.Li et al. (2021)[34]Direct Search vs IASA
Near-fieldGeneral HolographyDirect search balanced target and whole-region metrics better than IASA.Lee et al. (2022)[85]Deep Learning Framework
2.0 MHz
Near-fieldHigh-res image generationExtremely fast generation times. Limit: Generalizability to novel constraints.Maimbourg et al. (2018)[90]Adaptive Lens (FDTD)
0.914 MHz
Curved (D=67, R=59)
Trans-skullSingle focus (TUS)Restored focus throughex-vivoskull. Limit: Susceptible to physical registration errors.Jiménez-Gambín et al. (2019)[37]Time-Reversal / Phase Conj.
1 MHz
Flat (D=50)
Trans-skullSingle, double, volumetricProduced complex fields compensating for aberration. Limit: Computationally heavy.Acquaticci et al. (2019)[162]Axicon Lenses (k-Wave)
0.445 MHz
Flat (D=28)
Trans-skull (5mm)Deep focal depthImproved spatial resolution. Limit: Phase aberration not fully accounted for.Ferri et al. (2019)[26]Enhanced FDTD (Shear/Absorp)
0.760 MHz
Curved (D=67, R=59)
Trans-skullSingle (BBB levels, 100 kPa)Proved inclusion of shear waves improves focus quality. Limit: Simulation only.Hu et al. (2022)[163]Binary Metasurfaces (BAM)
0.45–0.55 MHz
Flat (D=120)
Trans-skullDynamic multi-pointCorrected aberrations and dynamically steered focus by changing frequency.Stanziola et al. (2023)[89]Physics-Based Deep Learning
Hologram property map
Water / SkullHigh-fidelity beam shapingDifferentiable model improved field fidelity over thin-element methods.Jiménez-Gambín et al. (2022)[164]Acoustic Holograms
1.68 MHz
Flat/Curved
Bilateral mouse skullBBB Opening in miceEnabled simultaneous multi-target bilateral BBB openingin vivo.He et al. (2022)[31]Phase-only Hologram
Mouse skullSmall animal tFUSMulti-target neuromodulation without phased arrays.Marzo & Drinkwater (2018)[165]Holographic Acoustic Tweezers
0.040 MHz
two opposing16×1616\times 16PAT elements
Mid-air levitationParticle manipulationDemonstrated independent 3D manipulation of multiple particles using HATs.Jiménez et al. (2021)[166]Self-Demodulation
Far-fieldAcoustic Vortex BeamsExplored subwavelength acoustic vortex beams using self-demodulation.Sallam et al. (2024)[71]Gradient Descent Opt.
Trans-skullNonlinear HolographyGradient descent optimization of acoustic holograms for transcranial FUS.Kruizinga et al. (2017)[33]Compressive Holography
Single Sensor
3D Imaging3D Ultrasound ImagingUtilized a single sensor and compressive sensing for 3D ultrasound imaging.Zhong et al. (2024)[167]Physics-Based Deep Learning
PAT Array
Micro-nanoRobotic ManipulationReal-time calculation of Phase-Only Holograms (POH) for dexterous manipulation.Wang et al. (2025)[168]Semi-Supervised Neural Net
Holographic fieldReal-Time ReconstructionKnowledge-driven method for real-time acoustic holographic field reconstruction.Khan & Kim (2025)[169]IASA Simulation Study
0.75–4.0 MHz
Fresnel zoneFidelity AnalysisHigher frequencies improve resolution but introduce edge ringing and high attenuation above 4 MHz.Baresch & Garbin (2020)[170]Holographic Trapping
Complex environmentsPayload releaseAcoustic trapping of microbubbles in complex environments.Ma et al. (2020)[171]Holographic Patterning
5.0 MHz
Biocompatible hydrogelCell patterningAcoustic holographic cell patterning in a biocompatible hydrogel.Pinton et al. (2011)[99]Full-Wave Nonlinear Sim.
TranscranialHigh-intensity brain therapyEffects of nonlinear ultrasound propagation on high-intensity brain therapy.Kook et al. (2023)[65]Skull-Compensated TUS
Trans-skullNeuromodulationMultifocal skull-compensated system for targeted neuromodulation applications.Estrada et al. (2021)[estrada2021]Spherical Array System
Multi-element Array
Rodent skullTUS and OptoacousticsHigh-precision transcranial ultrasound stimulation and optoacoustic imaging in rodents.

## References
- [1]T. L. Szabo,Diagnostic Ultrasound Imaging: Inside Out, Second Edition, 2 edition edition (Academic Press, Amsterdam ; Boston) (2013).
- [2]D. L. Miller, N. B. Smith, M. R. Bailey, G. J. Czarnota, K. Hynynen, and I. R. S. Makin, “Overview of Therapeutic Ultrasound Applications and Safety Considerations”, Journal of Ultrasound in Medicine31, 623–634 (2012).
- [3]C. Chaussy, E. Schmiedt, D. Jocham, J. Schüller, H. Brandl, and B. Liedl, “Extracorporeal shock-wave lithotripsy (ESWL) for treatment of urolithiasis”, Urology23, 59–66 (1984).
- [4]A. Skolarikos, G. Alivizatos, and J. de la Rosette, “Extracorporeal Shock Wave Lithotripsy 25 Years Later: Complications and Their Prevention”, European Urology50, 981–990 (2006).
- [5]V. S. Bachu, J. Kedda, I. Suk, J. J. Green, and B. Tyler, “High-intensity focused ultrasound: A review of mechanisms and clinical applications”, Annals of Biomedical Engineering49, 1975–1991 (2021).
- [6]C. Chaussy, S. Thüroff, X. Rebillard, and A. Gelet, “Technology insight: high-intensity focused ultrasound for urologic cancers”, Nature Clinical Practice Urology2, 191–198 (2005).
- [7]Z. Izadifar, Z. Izadifar, D. Chapman, and P. Babyn, “An introduction to high intensity focused ultrasound: systematic review on principles, devices, and clinical applications”, Journal of Clinical Medicine9, 460 (2020).
- [8]H. E. Cline, J. F. Schenck, K. Hynynen, R. D. Watkins, S. P. Souza, and F. A. Jolesz, “Mr-guided focused ultrasound surgery”, Journal of computer assisted tomography16, 956–965 (1992).
- [9]M. Tanter, J.-L. Thomas, and M. Fink, “Focusing and steering through absorbing and aberrating layers: Application to ultrasonic propagation through the skull”, The Journal of the Acoustical Society of America103, 2403–2410 (1998).
- [10]K. Hynynen and F. A. Jolesz, “Demonstration of potential noninvasive ultrasound brain therapy through an intact skull”, Ultrasound in medicine & biology24, 275–283 (1998).
- [11]M. Pernot, J.-F. Aubry, M. Tanter, J.-L. Thomas, and M. Fink, “High power transcranial beam steering for ultrasonic brain therapy”, Physics in Medicine & Biology48, 2577 (2003).
- [12]J.-F. Aubry, M. Tanter, M. Pernot, J.-L. Thomas, and M. Fink, “Experimental demonstration of noninvasive transskull adaptive focusing based on prior computed tomography scans”, The Journal of the Acoustical Society of America113, 84–93 (2003).
- [13]N. McDannold, G. T. Clement, P. Black, F. Jolesz, and K. Hynynen, “Transcranial Magnetic Resonance Imaging–Guided Focused Ultrasound Surgery of Brain Tumors: Initial Findings in 3 Patients”, Neurosurgery66, 323–332 (2010).
- [14]D. Jeanmonod, B. Werner, A. Morel, L. Michels, E. Zadicario, G. Schiff, and E. Martin, “Transcranial magnetic resonance imaging-guided focused ultrasound: noninvasive central lateral thalamotomy for chronic neuropathic pain”, Neurosurgical Focus32, 1–11 (2012).
- [15]W. J. Elias, D. Huss, T. Voss, J. Loomba, M. Khaled, E. Zadicario, R. C. Frysinger, S. A. Sperling, S. Wylie, S. J. Monteith, J. Druzgal, B. B. Shah, M. Harrison, and M. Wintermark, “A pilot study of focused ultrasound thalamotomy for essential tremor”, The New England Journal of Medicine369, 640–648 (2013).
- [16]H. H. Jung, S. J. Kim, D. Roh, J. G. Chang, W. S. Chang, E. J. Kweon, C.-H. Kim, and J. W. Chang, “Bilateral thermal capsulotomy with MR-guided focused ultrasound for patients with treatment-refractory obsessive-compulsive disorder: a proof-of-concept study”, Molecular Psychiatry20, 1205–1211 (2015).
- [17]A. Fasano, M. Llinas, R. P. Munoz, E. Hlasny, W. Kucharczyk, and A. M. Lozano, “MRI-guided focused ultrasound thalamotomy in non-ET tremor syndromes”, Neurology89, 771–775 (2017).
- [18]A. Carpentier, M. Canney, A. Vignot, V. Reina, K. Beccaria, C. Horodyckid, C. Karachi, D. Leclercq, C. Lafon, J.-Y. Chapelon, L. Capelle, P. Cornu, M. Sanson, K. Hoang-Xuan, J.-Y. Delattre, and A. Idbaih, “Clinical trial of blood-brain barrier disruption by pulsed ultrasound”, Science Translational Medicine8, 343re2–343re2 (2016).
- [19]A. Abrahao, Y. Meng, M. Llinas, Y. Huang, C. Hamani, T. Mainprize, I. Aubert, C. Heyn, S. E. Black, K. Hynynen, N. Lipsman, and L. Zinman, “First-in-human trial of blood–brain barrier opening in amyotrophic lateral sclerosis using MR-guided focused ultrasound”, Nature Communications10, 1–9 (2019).
- [20]N. Lipsmanet al., “Blood-brain barrier opening in alzheimer’s disease using mr-guided focused ultrasound”, Nature Communications (2018).
- [21]F. A. Jolesz,Intraoperative imaging and image-guided therapy(Springer Science & Business Media) (2014).
- [22]Y. Hertzberg, A. Volovick, Y. Zur, Y. Medan, S. Vitek, and G. Navon, “Ultrasound focusing using magnetic resonance acoustic radiation force imaging: application to ultrasound transcranial therapy”, Medical physics37, 2934–2942 (2010).
- [23]K. Melde, A. G. Mark, T. Qiu, and P. Fischer, “Holograms for acoustics”, Nature537, 518–522 (2016).
- [24]C. Shen, J. Xu, N. X. Fang, and Y. Jing, “Anisotropic complementary acoustic metamaterial for canceling out aberrating layers”, Physical Review X4, 041033 (2014).
- [25]G. Maimbourg, A. Houdouin, T. Deffieux, M. Tanter, and J.-F. Aubry, “3d-printed adaptive acoustic lens as a disruptive technology for transcranial ultrasound therapy using single-element transducers”, Physics in Medicine & Biology63, 025026 (2018).
- [26]M. Ferri, J. M. Bravo, J. Redondo, and J. V. Sánchez-Pérez, “Enhanced numerical method for the design of 3-d-printed holographic acoustic lenses for aberration correction of single-element transcranial focused ultrasound”, Ultrasound in medicine & biology45, 867–884 (2019).
- [27]S. Jiménez-Gambín, S. Bae, R. Ji, F. Tsitsos, and E. E. Konofagou, “Feasibility of hologram-assisted bilateral blood-brain barrier opening in non-human primates”, IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control71, 164–173 (2024).
- [28]S. Jiménez-Gambínet al., “Acoustic holograms for bilateral blood-brain barrier opening in a mouse model”, IEEE Transactions on Biomedical Engineering69, 1359–1368 (2021).
- [29]D. Andrés, N. Jiménez, J. M. Benlloch, and F. Camarena, “Numerical study of acoustic holograms for deep-brain targeting through the temporal bone window”, Ultrasound in Medicine & Biology48, 872–886 (2022).
- [30]B. Glicksteinet al., “Rationally designed acoustic holograms for uniform nanodroplet-mediated tissue ablation”, IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control71(2024).
- [31]J. He, J. Wu, Y. Zhu, Y. Chen, M. Yuan, L. Zeng, and X. Ji, “Multitarget transcranial ultrasound therapy in small animals based on phase-only acoustic holographic lens”, IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control69, 662–671 (2021).
- [32]S. Jiménez-Gambín, N. Jimenez, J. M. Benlloch, and F. Camarena, “Generating bessel beams with broad depth-of-field by using phase-only acoustic holograms”, Scientific reports9, 20104 (2019).
- [33]P. Kruizinga, P. van der Meulen, A. Fedjajevs, F. Mastik, G. Springeling, N. de Jong, J. G. Bosch, and G. Leus, “Compressive 3d ultrasound imaging using a single sensor”, Science advances3, e1701423 (2017).
- [34]J. Li, Z. Lv, Z. Hou, and Y. Pei, “Comparison of balanced direct search and iterative angular spectrum approaches for designing acoustic holography structure”, Applied Acoustics175, 107848 (2021), URLhttp://dx.doi.org/10.1016/j.apacoust.2020.107848.
- [35]M. H. Lee, H. M. Lew, S. Youn, T. Kim, and J. Y. Hwang, “Deep learning-based framework for fast and accurate acoustic hologram generation”, IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control69, 3353–3366 (2022).
- [36]T. Fushimi, K. Yamamoto, and Y. Ochiai, “Acoustic hologram optimisation using automatic differentiation”, Scientific reports11, 12678 (2021).
- [37]S. Jiménez-Gambín, N. Jiménez, J. M. Benlloch, and F. Camarena, “Holograms to focus arbitrary ultrasonic fields through the skull”, Physical Review Applied12, 014016 (2019).
- [38]S. Schoen, P. Dash, and C. D. Arvanitis, “Experimental demonstration of trans-skull volumetric passive acoustic mapping with the heterogeneous angular spectrum approach”, IEEE transactions on ultrasonics, ferroelectrics, and frequency control69, 534–542 (2021).
- [39]M. A. O’Reilly, R. M. Jones, G. Birman, and K. Hynynen, “Registration of human skull computed tomography data to an ultrasound treatment space using a sparse high frequency ultrasound hemispherical array”, Medical Physics43, 5063–5071 (2016).
- [40]B. D. de Senneville, C. Mougenot, B. Quesson, I. Dragonu, N. Grenier, and C. T. Moonen, “Mr thermometry for monitoring tumor ablation”, European radiology17, 2401–2410 (2007).
- [41]A. Kyriakou, E. Neufeld, B. Werner, M. M. Paulides, G. Szekely, and N. Kuster, “A review of numerical and experimental compensation techniques for skull-induced phase aberrations in transcranial focused ultrasound”, International journal of hyperthermia30, 36–46 (2014).
- [42]K.-T. Chen, Y.-J. Lin, W.-Y. Chai, C.-J. Lin, P.-Y. Chen, C.-Y. Huang, J. S. Kuo, H.-L. Liu, and K.-C. Wei, “Neuronavigation-guided focused ultrasound (navifus) for transcranial blood-brain barrier opening in recurrent glioblastoma patients: Clinical trial protocol”, Annals of Translational Medicine8(2020).
- [43]J. A. van Doormaalet al., “Clinical accuracy of holographic navigation using a head-mounted display”, Operative Neurosurgery (2019).
- [44]W. J. Eliaset al., “A randomized trial of focused ultrasound thalamotomy for essential tremor”, New England Journal of Medicine (2016).
- [45]K. C. Weiet al., “Neuronavigation-guided focused ultrasound-induced blood-brain barrier opening”, American Journal of Neuroradiology (2013).
- [46]A. Sallam and S. Shahab, “Nonlinear acoustic holography with adaptive sampling”, IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control70, 1516–1526 (2023).
- [47]F. A. Duck,Physical properties of tissue: A comprehensive reference book(Academic press) (2013).
- [48]Y. Jiang, W. Huang, X.-J. Wu, X.-L. Shi, R.-R. Hu, W. Chen, T.-F. Zhang, X.-L. Xu, C.-G. Huang, and L.-J. Hou, “Invention of a non-invasive intracranial pressure (icp) monitoring system–an enlightenment from a hydrocephalus study”, British Journal of Neurosurgery36, 693–698 (2022).
- [49]M. A. Nitsche, L. G. Cohen, E. M. Wassermann, A. Priori, N. Lang, A. Antal, W. Paulus, F. Hummel, P. S. Boggio, F. Fregni,et al., “Transcranial direct current stimulation: state of the art 2008”, Brain stimulation1, 206–223 (2008).
- [50]V. Walsh and A. Cowey, “Transcranial magnetic stimulation and cognitive neuroscience”, Nature Reviews Neuroscience1, 73–80 (2000).
- [51]P. Faria, M. Hallett, and P. C. Miranda, “A finite element analysis of the effect of electrode area and inter-electrode distance on the spatial distribution of the current density in tdcs”, Journal of neural engineering8, 066017 (2011).
- [52]Z.-D. Deng, S. H. Lisanby, and A. V. Peterchev, “Electric field depth–focality tradeoff in transcranial magnetic stimulation: simulation comparison of 50 coil designs”, Brain stimulation6, 1–13 (2013).
- [53]G. T. Haar, “Ultrasound bioeffects and safety”, Proceedings of the Institution of Mechanical Engineers, Part H: Journal of Engineering in Medicine224, 363–373 (2010).
- [54]S. Cadoni, C. Demené, I. Alcala, M. Provansal, D. Nguyen, D. Nelidova, G. Labernède, J. Lubetzki, R. Goulet, E. Burban,et al., “Ectopic expression of a mechanosensitive channel confers spatiotemporal resolution to ultrasound stimulations of neurons for visual restoration”, Nature Nanotechnology18, 667–676 (2023).
- [55]T. Sato, M. Shapiro, and D. Tsao, “Ultrasonic Neuromodulation Causes Widespread Cortical Activation via an Indirect Auditory Mechanism”, (2018).
- [56]H. Guo, M. Hamilton, S. Offutt, C. Gloeckner, T. Li, Y. Kim, W. Legon, J. Alford, and H. Lim, “Ultrasound Produces Extensive Brain Activation via a Cochlear Pathway”, Neuron98, 1020–1030 (2018).
- [57]P. P. Dash and C. D. Arvanitis, “Acoustic Holography in the Megahertz Frequency Range with Optimal Lens Topologies and Nonlinear Acoustic Feedback”, (2025), URLhttps://arxiv.org/abs/2508.07103.
- [58]K. Melde, H. Kremer, M. Shi, S. Seneca, C. Frey, I. Platzman, C. Degel, D. Schmitt, B. Schölkopf, and P. Fischer, “Compact holographic sound fields enable rapid one-step assembly of matter in 3D”, Science Advances9, eadf6182 (2023).
- [59]R. Hirayama, D. M. Plasencia, N. Masuda, and S. Subramanian, “A volumetric display for visual, tactile and audio presentation using acoustic trapping”, Nature575, 320–323 (2019).
- [60]Y. Xie, C. Shen, W. Wang, J. Li, D. Suo, B.-I. Popa, Y. Jing, and S. A. Cummer, “Acoustic holographic rendering with two-dimensional metamaterial-based passive phased array”, Scientific Reports6, 35437 (2016).
- [61]Z. Hu, Y. Yang, L. Yang, Y. Gong, C. Chukwu, D. Ye, Y. Yue, J. Yuan, A. V. Kravitz, and H. Chen, “Airy-beam holographic sonogenetics for advancing neuromodulation precision and flexibility”, Proceedings of the National Academy of Sciences121, e2402200121 (2024).
- [62]D. Andrés, I. Rivens, P. Mouratidis, N. Jiménez, F. Camarena, and G. ter Haar, “Holographic focused ultrasound hyperthermia system for uniform simultaneous thermal exposure of multiple tumor spheroids”, Cancers15, 2540 (2023).
- [63]M. Daniel, D. Attali, T. Tiennot, M. Tanter, and J.-F. Aubry, “Multifrequency transcranial ultrasound holography with acoustic lenses”, Physical Review Applied21, 014011 (2024).
- [64]S. Jiménez-Gambín, S. Bae, R. Ji, F. Tsitsos, and E. E. Konofagou, “Feasibility of hologram-assisted bilateral blood–brain barrier opening in non-human primates”, IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control71, 1172–1185 (2024).
- [65]G. Kook, Y. Jo, C. Oh, X. Liang, J. Kim, S.-M. Lee, S. Kim, J.-W. Choi, and H. J. Lee, “Multifocal skull-compensated transcranial focused ultrasound system for neuromodulation applications based on acoustic holography”, Microsystems & Nanoengineering9, 45 (2023).
- [66]X. Yao, X. Piao, S. Hong, C. Ji, M. Wang, Y. Wei, Z. Xu, J.-J. Pan, Y. Pei, and B. Cheng, “Acoustic hologram-enabled simultaneous multi-target blood-brain barrier opening (AH-SiMBO)”, Communications Engineering4, 99 (2025).
- [67]Y. Meng, K. Hynynen, and N. Lipsman, “Applications of focused ultrasound in the brain: from thermoablation to drug delivery”, Nature Reviews Neurology17, 7–22 (2021).
- [68]S. Schoen, M. S. Kilinc, H. Lee, Y. Guo, F. L. Degertekin, G. F. Woodworth, and C. Arvanitis, “Towards controlled drug delivery in brain tumors with microbubble-enhanced focused ultrasound”, Advanced Drug Delivery Reviews180, 114043 (2022).
- [69]S. W. Choi, M. Komaiha, D. Choi, N. Lu, T. I. Gerhardson, A. Fox, N. Chaudhary, S. Camelo-Piragua, T. L. Hall, A. S. Pandey, Z. Xu, and J. R. Sukovich, “Neuronavigation-guided transcranial histotripsy (NaviTH) system”, Ultrasound in Medicine & Biology50, 1155–1166 (2024).
- [70]J. Gu and Y. Jing, “A modified mixed domain method for modeling acoustic wave propagation in strongly heterogeneous media”, The Journal of the Acoustical Society of America147, 4055–4068 (2020).
- [71]A. Sallam, C. Cengiz, M. Pewekar, E. Hoffmann, W. Legon, E. Vlaisavljevich, and S. Shahab, “Gradient descent optimization of acoustic holograms for transcranial focused ultrasound”, Journal of Applied Physics136, 144901 (2024).
- [72]S. Schoen and C. D. Arvanitis, “Heterogeneous angular spectrum method for trans-skull imaging and focusing”, IEEE Transactions on Medical Imaging39, 1605–1614 (2019).
- [73]S. Pichardo, V. W. Sin, and K. Hynynen, “Multi-frequency characterization of the speed of sound and attenuation coefficient for longitudinal transmission of freshly excised human skulls”, Physics in Medicine and Biology56, 219–250 (2011).
- [74]P. M. Morse and H. Feshbach,Methods of Theoretical Physics, Part I(McGraw-Hill Book Company, New York) (1946).
- [75]P. P. Dash and C. Arvanitis, “Heterogenous angular spectrum approach based holograms for trans-skull focused ultrasound therapy”, The Journal of the Acoustical Society of America153, A103–A103 (2023), URLhttp://dx.doi.org/10.1121/10.0018312.
- [76]C. Arvanitis and P. P. Dash, “Trans-skull focused ultrasound using acoustic hologram and heterogenous angular spectrum approach, and hologram registration”, (2025), uS Patent 12,502,558.
- [77]M. Bakaric, P. Miloro, A. Javaherian, B. T. Cox, B. E. Treeby, and M. D. Brown, “Measurement of the ultrasound attenuation and dispersion in 3d-printed photopolymer materials from 1 to 3.5 mhz”, The Journal of the Acoustical Society of America150, 2798–2805 (2021).
- [78]B. E. Treeby and B. T. Cox, “k-wave: MATLAB toolbox for the simulation and reconstruction of photoacoustic wave fields”, Journal of Biomedical Optics15, 021314 (2010).
- [79]D. T. Blackstock,Fundamentals of Physical Acoustics(John Wiley & Sons) (2000).
- [80]S. Schoen and C. D. Arvanitis, “Heterogeneous angular spectrum method for trans-skull imaging and focusing”, IEEE transactions on medical imaging39, 1605–1614 (2019).
- [81]M. S. Kilinc, H. Lee, Y. R. Ferry, B. Ingram, B. Skowronski, P. P. Dash, R. P. Zangabad, C. Arvanitis, and F. L. Degertekin, “A Piezo-Cmut Hybrid Hemispherical Transmit Array for Passive Acoustic Mapping of Microbubble Activity”, in2025 IEEE International Ultrasonics Symposium (IUS), 1–5 (IEEE) (2025), URLhttp://dx.doi.org/10.1109/IUS62464.2025.11201469.
- [82]C. Angla, B. Larrat, J.-L. Gennisson, and S. Chatillon, “Transcranial ultrasound simulations: A review”, Medical Physics50, 1051–1072 (2023).
- [83]M. Bu, W. Gu, B. Li, Q. Zhu, X. Jiang, D. Ta, and X. Liu, “A deep learning-based method of acoustic holographic lens generation for transcranial focused ultrasound”, AIP Advances14, 125026 (2024).
- [84]B. Li, M. Lu, C. Liu, X. Liu, and D. Ta, “Acoustic hologram reconstruction with unsupervised neural network”, Frontiers in Materials9(2022).
- [85]M. H. Lee, H. M. Lew, S. Youn, T. Kim, and J. Y. Hwang, “Deep learning-based framework for fast and accurate acoustic hologram generation”, IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control69, 3353–3366 (2022).
- [86]L. Jiang, G. Lu, Y. Zeng, Y. Sun, H. Kang, J. Burford, C. Gong, M. S. Humayun, Y. Chen, and Q. Zhou, “Flexible ultrasound-induced retinal stimulating piezo-arrays for biomimetic visual prostheses”, Nature Communications13, 3853 (2022).
- [87]O. Naor, Y. Hertzberg, E. Zemel, E. Kimmel, and S. Shoham, “Towards multifocal ultrasonic neural stimulation II: design considerations for an acoustic retinal prosthesis”, Journal of Neural Engineering9, 026006 (2012).
- [88]V. Lagerburg, A. Vrancken, S. Bergsma, J. Dekker, W. Diemer, J. Waldner-Troost, and M. Koenrades, “Dimensional accuracy and resolution assessment of the formlabs form 3B 3D printer for medical applications”, Annals of 3D Printed Medicine19, 100204 (2025).
- [89]A. Stanziola, B. T. Cox, B. E. Treeby, and M. D. Brown, “Physics-based acoustic holograms”, arXiv preprint arXiv:2305.03625 (2023), URLhttps://arxiv.org/abs/2305.03625.
- [90]G. Maimbourg, A. Houdouin, T. Deffieux, M. Tanter, and J.-F. Aubry, “3D-printed adaptive acoustic lens as a disruptive technology for transcranial ultrasound therapy using single-element transducers”, Physics in Medicine & Biology63, 025026 (2018).
- [91]K.-T. Chen, W.-Y. Chai, Y.-J. Lin, C.-J. Lin, P.-Y. Chen, H.-C. Tsai, C.-Y. Huang, J. S. Kuo, H.-L. Liu, and K.-C. Wei, “Neuronavigation-guided focused ultrasound for transcranial blood-brain barrier opening and immunostimulation in brain tumors”, Science Advances7, eabd0772 (2021).
- [92]A. N. Pouliopoulos, S.-Y. Wu, M. T. Burgess, M. E. Karakatsani, H. A. S. Kamimura, and E. E. Konofagou, “A clinical system for non-invasive blood–brain barrier opening using a neuronavigation-guided single-element focused ultrasound transducer”, Ultrasound in Medicine & Biology46, 73–89 (2020).
- [93]P. P. Dash and C. Arvanitis, “Leveraging the parametric array effect for transcranial focused ultrasound interventions”, The Journal of the Acoustical Society of America157, A307–A307 (2025), URLhttp://dx.doi.org/10.1121/10.0038401.
- [94]P. J. Westervelt, “Parametric acoustic array”, The Journal of the acoustical society of America35, 535–537 (1963).
- [95]P. P. Dash and C. Arvanitis, “Non-linearities under highly focused high-intensity ultrasound fields”, The Journal of the Acoustical Society of America150, A125–A125 (2021), URLhttp://dx.doi.org/10.1121/10.0007852.
- [96]M. F. Hamilton and D. T. Blackstock,Nonlinear Acoustics(Acoustical Society of America) (2008).
- [97]G. T. Clement, P. J. White, and K. Hynynen, “Enhanced ultrasound transmission through the human skull using shear mode conversion”, The Journal of the Acoustical Society of America115, 1356–1364 (2004).
- [98]G. Renaud, S. Calle, J. P. Remenieras, and M. Defontaine, “Exploration of trabecular bone nonlinear elasticity using time-of-flight modulation”, IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control55, 1497–1507 (2008).
- [99]G. Pinton, J.-F. Aubry, M. Fink, and M. Tanter, “Effects of nonlinear ultrasound propagation on high intensity brain therapy”, Medical Physics38, 1207–1216 (2011).
- [100]C. Baron, J.-F. Aubry, M. Tanter, S. Meairs, and M. Fink, “Simulation of intracranial acoustic fields in clinical trials of sonothrombolysis”, Ultrasound in Medicine & Biology35, 1148–1158 (2009).
- [101]J. Song, D. Jung, J. S. Kim, and J. Lee, “Experimental evaluation of pseudo-sound in a parametric array”, Journal of the Acoustical Society of America150, 3787–3796 (2021).
- [102]S. Karpov, A. Prosperetti, and L. Ostrovsky, “Nonlinear wave interactions in bubble layers”, The Journal of the Acoustical Society of America113, 1304–1316 (2003), URLhttp://dx.doi.org/10.1121/1.1539519.
- [103]R. Airan, “Neuromodulation with nanoparticles”, Science357, 465 (2017).
- [104]J. Rincon-Torroella, H. Khela, A. Bettegowda, and C. Bettegowda, “Biomarkers and focused ultrasound: the future of liquid biopsy for brain tumor patients”, Journal of Neuro-Oncology156, 33–48 (2022).
- [105]B. Hofmann, I. Ø. Brandsaeter, and E. Kjelle, “Variations in wait times for imaging services: a register-based study of self-reported wait times for specific examinations in Norway”, BMC Health Services Research23, 1287 (2023).
- [106]A. Panfilova, R. J. G. van Sloun, H. Wijkstra, O. A. Sapozhnikov, and M. Mischi, “A review on B/A measurement methods with a clinical perspective”, Journal of the Acoustical Society of America149, 2200–2237 (2021).
- [107]D. Zhang, X. Gong, and X. Chen, “Experimental imaging of the acoustic nonlinearity parameter B/A for biological tissues via a parametric array”, Ultrasound in Medicine & Biology27, 1359–1365 (2001).
- [108]M.-X. Tang, J. Loughran, E. Stride, D. Zhang, and R. J. Eckersley, “Effect of bubble shell nonlinearity on ultrasound nonlinear propagation through microbubble populations”, Journal of the Acoustical Society of America129, EL76–82 (2011).
- [109]M. Cavaro, C. Payan, J. Moysan, and F. Baqué, “Microbubble cloud characterization by nonlinear frequency mixing”, Journal of the Acoustical Society of America129, EL179–183 (2011).
- [110]M. Overvelde, V. Garbin, J. Sijl, B. Dollet, N. de Jong, D. Lohse, and M. Versluis, “Nonlinear shell behavior of phospholipid-coated microbubbles”, Ultrasound in Medicine & Biology36, 2080–2092 (2010).
- [111]G. Pinton, J.-F. Aubry, E. Bossy, M. Muller, M. Pernot, and M. Tanter, “Attenuation, scattering, and absorption of ultrasound in the skull bone”, Medical Physics39, 299–307 (2012).
- [112]X. Zhang, J. E. Medow, B. J. Iskandar, F. Wang, M. Shokoueinejad, J. Koueik, and J. G. Webster, “Invasive and noninvasive means of measuring intracranial pressure: a review”, Physiological measurement38, R143–R182 (2017).
- [113]J. B. Fischer, A. Ghouse, S. Tagliabue, F. Maruccia, A. Rey-Perez, M. Báguena, P. Cano, R. Zucca, U. M. Weigel, J. Sahuquillo, M. A. Poca, and T. Durduran, “Non-invasive estimation of intracranial pressure by diffuse optics: A proof-of-concept study”, Journal of Neurotrauma37, 2569–2579 (2020).
- [114]J. Qiu, T.-J. Zou, D.-M. Wang, H.-R. Luo, H.-T. Yu, L. Lei, and W.-H. Yin, “Noninvasive intracranial pressure prediction using a multimodal ultrasound-based hemispheric modeling strategy: A prospective dual-center study”, Neurocritical Care43, 911–926 (2025).
- [115]X. Jiang, H. Guo, W. Xiao, L. Wang, D. Wu, J. Liu, Q. Zhao, and Y. Shao, “Advancements in non-invasive intracranial pressure monitoring via optic nerve sheath diameter measurement”, Medical Science Monitor: International Medical Journal of Experimental and Clinical Research31, e947237 (2025).
- [116]M. Czosnyka and J. D. Pickard, “Monitoring and interpretation of intracranial pressure”, Journal of Neurology, Neurosurgery & Psychiatry75, 813–821 (2004).
- [117]M. Blomqvist, H. Zetterberg, K. Blennow, and J.-E. Månsson, “Sulfatide in health and disease. the evaluation of sulfatide in cerebrospinal fluid as a possible biomarker for neurodegeneration”, Molecular and Cellular Neuroscience116, 103670 (2021).
- [118]B. E. Treeby and B. T. Cox, “k-wave: Matlab toolbox for the simulation and reconstruction of photoacoustic wave fields”, (2010).
- [119]D. Jaraj, K. Rabiei, T. Marlow, C. Jensen, I. Skoog, and C. Wikkelsø, “Estimated ventricle size using evans index: reference values from a population-based sample”, European journal of neurology24, 468–474 (2017).
- [120]Z. Bendella, V. Purrer, R. Haase, S. Zülow, C. Kindler, V. Borger, M. Banat, F. Dorn, U. Wüllner, A. Radbruch, and F. C. Schmeel, “Brain and ventricle volume alterations in idiopathic normal pressure hydrocephalus determined by artificial intelligence-based MRI volumetry”, Diagnostics14, 1422 (2024).
- [121]P. J. Westervelt, “Parametric acoustic array”, Journal of the Acoustical Society of America35, 535–537 (1963).
- [122]F. Geraldini, A. D. Cassai, and M. Munari, “Transcranial ultrasound as a useful tool in early detection and follow-up of hydrocephalus in acute subarachnoid hemorrhage”, Journal of Neurosurgical Anesthesiology34, e75 (2022).
- [123]A. Caricato, S. Pitoni, L. Montini, M. G. Bocci, P. Annetta, and M. Antonelli, “Echography in brain imaging in intensive care unit: State of the art”, World Journal of Radiology6, 636–642 (2014).
- [124]B. Zhang, Z. Huang, H. Song, H. S. Kim, and J. Park, “Wearable intracranial pressure monitoring sensor for infants”, Biosensors11, 213 (2021).
- [125]S. I. Moskowitz, W. J. Davros, M. E. Kelly, D. Fiorella, P. A. Rasmussen, and T. J. Masaryk, “Cumulative radiation dose during hospitalization for aneurysmal subarachnoid hemorrhage”, American Journal of Neuroradiology31, 1377–1382 (2010).
- [126]V. Filippou and C. Tsoumpas, “Recent advances on the development of phantoms using 3D printing for imaging with CT, MRI, PET, SPECT, and ultrasound”, Medical Physics45, e740–e760 (2018).
- [127]B. Krasovitski, V. Frenkel, S. Shoham, and E. Kimmel, “Intramembrane cavitation as a unifying mechanism for ultrasound-induced bioeffects”, Proc. Natl. Acad. Sci108, 3258–3263 (2011).
- [128]R. King, J. Brown, W. Newsome, and K. Pauly, “Effective Parameters for Ultrasound-Induced In Vivo Neurostimulation”, Ultrasound Med. Biol39, 312–331 (2013).
- [129]M. Plaksin, S. Shoham, and E. Kimmel, “Intramembrane cavitation as a predictive bio-piezoelectric mechanism for ultrasonic brain stimulation”, Physical review X4, 011004 (2014).
- [130]M. Prieto, K. Firouzi, B. Khuri-Yakub, and M. Maduke, “Activation of Piezo1 but Not NaV1.2 Channels by Ultrasound at 43 MHz”, Ultrasound Med. Biol44, 1217–1232 (2018).
- [131]D. Liao, M.-Y. Hsiao, G. Xiang, and P. Zhong, “Optimal pulse length of insonification for Piezo1 activation and intracellular calcium response”, Sci. Rep11, 709 (2021).
- [132]B. Hoffman, Y. Baba, S. Lee, C.-K. Tong, E. Konofagou, and E. Lumpkin, “Focused ultrasound excites action potentials in mammalian peripheral neurons in part through the mechanically gated ion channel PIEZO2”, Proc. Natl. Acad. Sci119, e2115821119(2022).
- [133]J. Kubanek, P. Shukla, A. Das, S. A. Baccus, and M. B. Goodman, “Ultrasound Elicits Behavioral Responses through Mechanical Effects on Neurons and Ion Channels in a Simple Nervous System”, Journal of Neuroscience38, 3081–3091 (2018).
- [134]S. Yoo, D. Mittelstein, R. Hurt, J. Lacroix, and M. Shapiro, “Focused ultrasound excites cortical neurons via mechanosensitive calcium accumulation and ion channel amplification”, Nat. Commun13, 493 (2022).
- [135]V. Cotero, Y. Fan, T. Tsaava, A. Kressel, I. Hancu, P. Fitzgerald, K. Wallace, S. Kaanumalle, J. Graf, W. Rigby, T.-J. Kao, J. Roberts, C. Bhushan, S. Joel, T. Coleman, S. Zanos, K. Tracey, J. Ashe, S. Chavan, and C. Puleo, “Noninvasive sub-organ ultrasound stimulation for targeted neuromodulation”, Nat. Commun10, 952 (2019).
- [136]D. Folloni, L. Verhagen, R. Mars, E. Fouragnan, C. Constans, J.-F. Aubry, M. Rushworth, and J. Sallet, “Manipulation of Subcortical and Deep Cortical Activity in the Primate Brain Using Transcranial Focused Ultrasound Stimulation”, Neuron101, 1109–1116 (2019).
- [137]Y. Tufail, A. Matyushov, N. Baldwin, M. L. Tauchmann, J. Georges, A. Yoshihiro, S. I. H. Tillery, and W. J. Tyler, “Transcranial Pulsed Ultrasound Stimulates Intact Brain Circuits”, Neuron66, 681–694 (2010).
- [138]J. Kubanek, J. Brown, P. Ye, K. Pauly, T. Moore, and W. Newsome, “Remote, brain region–specific control of choice behavior with ultrasonic waves”, Sci. Adv6, eaaz4193(2020).
- [139]J. Blackmore, S. Shrivastava, J. Sallet, C. Butler, and R. Cleveland, “Ultrasound Neuromodulation: A Review of Results, Mechanisms and Safety”, Ultrasound Med. Biol45, 1509–1536 (2019).
- [140]G. Darmani, T. O. Bergmann, K. Butts Pauly, C. F. Caskey, L. de Lecea, A. Fomenko, E. Fouragnan, W. Legon, K. R. Murphy, T. Nandi, M. A. Phipps, G. Pinton, H. Ramezanpour, J. Sallet, S. N. Yaakub, S. S. Yoo, and R. Chen, “Non-invasive transcranial ultrasound stimulation for neuromodulation”, Clinical Neurophysiology135, 51–73 (2022).
- [141]B. M. Gaub, K. C. Kasuba, E. Mace, T. Strittmatter, P. R. Laskowski, S. A. Geissler, A. Hierlemann, M. Fussenegger, B. Roska, and D. J. Müller, “Neurons differentiate magnitude and location of mechanical stimuli”, Proceedings of the National Academy of Sciences117, 848–856 (2020).
- [142]D. Alsteens, H. E. Gaub, R. Newton, M. Pfreundschuh, C. Gerber, and D. J. Müller, “Atomic force microscopy-based characterization and design of biointerfaces”, Nature Reviews Materials2, 1–16 (2017).
- [143]M. Krieg, G. Fläschner, D. Alsteens, B. M. Gaub, W. H. Roos, G. J. Wuite, H. E. Gaub, C. Gerber, Y. F. Dufrêne, and D. J. Müller, “Atomic force microscopy-based mechanobiology”, Nature Reviews Physics1, 41–57 (2019).
- [144]C. Rabut, S. Yoo, R. C. Hurt, Z. Jin, H. Li, H. Guo, B. Ling, and M. G. Shapiro, “Ultrasound technologies for imaging and modulating neural activity”, Neuron108, 93–110 (2020).
- [145]M. Mohammadjavadi, R. T. Ash, N. Li, P. Gaur, J. Kubanek, Y. Saenz, G. H. Glover, G. R. Popelka, A. M. Norcia, and K. B. Pauly, “Transcranial ultrasound neuromodulation of the thalamic visual pathway in a large animal model and the dose-response relationship with mr-arfi”, Scientific Reports12, 19588 (2022).
- [146]C. Arvanitis, P. P. Dash, and C. Kim, “Ultrasound mediated control of neurons and immune cells”, The Journal of the Acoustical Society of America153, A31–A31 (2023), URLhttp://dx.doi.org/10.1121/10.0018046.
- [147]A. P. Sarvazyan, O. V. Rudenko, and W. L. Nyborg, “Biomedical applications of radiation force of ultrasound: historical roots and physical basis”, Ultrasound in medicine & biology36, 1379–1394 (2010).
- [148]O. A. Sapozhnikov and M. R. Bailey, “Radiation force of an arbitrary acoustic beam on an elastic sphere in a fluid”, The Journal of the Acoustical Society of America133, 661–676 (2013).
- [149]L. P. Gor’kov, “On the forces acting on a small particle in an acoustical field in an ideal fluid”, inSelected Papers of Lev P. Gor’kov, 315–317 (2014).
- [150]K. Yosioka and Y. Kawasima, “Acoustic radiation pressure on a compressible sphere”, Acta Acustica united with Acustica5, 167–173 (1955).
- [151]P. Glynne-Jones, P. P. Mishra, R. J. Boltryk, and M. Hill, “Efficient finite element modeling of radiation forces on elastic particles of arbitrary size and geometry”, The Journal of the Acoustical Society of America133, 1885–1893 (2013).
- [152]O. A. Sapozhnikov, L. A. Trusov, A. I. Gromov, N. R. Owen, M. R. Bailey, and L. A. Crum, “Radiation force imparted on a kidney stone by a doppler-mode diagnostic pulse”, The Journal of the Acoustical Society of America120, 3109–3109 (2006).
- [153]H. Bruus,Theoretical microfluidics, volume 18 (Oxford university press) (2007).
- [154]M. Settnes and H. Bruus, “Forces acting on a small particle in an acoustical field in a viscous fluid”, Physical Review E85, 016327 (2012).
- [155]L. R. Gavrilov, “Use of focused ultrasound for stimulation of nerve structures”, Ultrasonics22, 132–138 (1984).
- [156]L. Gavrilov and E. Tsirulnikov, “Focused ultrasound as a tool to input sensory information to humans”, Acoustical Physics58, 1–21 (2012).
- [157]M. Fatemi and J. F. Greenleaf, “Probing the dynamics of tissue at low frequencies with the radiation force of ultrasound”, Physics in Medicine & Biology45, 1449 (2000).
- [158]M. Fatemi and J. F. Greenleaf, “Vibro-acoustography: An imaging modality based on ultrasound-stimulated acoustic emission”, Proceedings of the National Academy of Sciences96, 6603–6608 (1999).
- [159]G. T. Silva, S. Chen, and L. P. Viana, “Parametric amplification of the dynamic radiation force of acoustic waves in fluids”, Physical review letters96, 234301 (2006).
- [160]M. D. Brown, B. T. Cox, and B. E. Treeby, “Design of multi-frequency acoustic kinoforms”, Applied Physics Letters111, 244101 (2017).
- [161]M. D. Brown, B. T. Cox, and B. E. Treeby, “Stackable acoustic holograms”, Applied Physics Letters116, 261901 (2020).
- [162]F. Acquaticciet al., “Ultrasound axicon: Systematic approach to optimize focusing resolution through human skull bone”, Materials12, 3433 (2019).
- [163]Z. Hu, Y. Yang, L. Xu, Y. Hao, and H. Chen, “Binary acoustic metasurfaces for dynamic focusing of transcranial ultrasound”, Frontiers in Neuroscience16, 984953 (2022).
- [164]S. Jiménez-Gambínet al., “Acoustic holograms for bilateral blood-brain barrier opening in a mouse model”, IEEE Transactions on Biomedical Engineering69, 1359–1368 (2021).
- [165]A. Marzo and B. W. Drinkwater, “Holographic acoustic tweezers”, Proceedings of the National Academy of Sciences116, 84–89 (2019), URLhttp://dx.doi.org/10.1073/pnas.1813047115.
- [166]N. Jiménez, J. Ealo, R. D. Muelas-Hurtado, A. Duclos, and V. Romero-García, “Subwavelength Acoustic Vortex Beams Using Self-Demodulation”, Physical Review Applied15(2021), URLhttp://dx.doi.org/10.1103/PhysRevApplied.15.054027.
- [167]C. Zhonget al., “Real-time acoustic holography with physics-based deep learning for robotic manipulation”, IEEE Transactions on Automation Science and Engineering21, 2951–2962 (2023).
- [168]S. Wang, F. You, X. Wang, and H. Xiao, “A knowledge-driven method for real-time acoustic holographic field reconstruction using physical modeling and semi-supervised neural networks”, Knowledge-Based Systems311, 113044 (2025), URLhttp://dx.doi.org/10.1016/j.knosys.2025.113044.
- [169]H. Khan and J. Kim, “Reconstruction Fidelity of Acoustic Holograms Across 0.75–4.0 MHz Excitation Frequencies: A Simulation Study”, Applied Sciences15, 10991 (2025), URLhttp://dx.doi.org/10.3390/app152010991.
- [170]D. Baresch and V. Garbin, “Acoustic trapping of microbubbles in complex environments”, Proceedings of the National Academy of Sciences117, 15490–15496 (2020).
- [171]Z. Maet al., “Acoustic holographic cell patterning in a biocompatible hydrogel”, Advanced Materials32, 1904181 (2020).
- [172]P. P. Dash, “Operational modal analysis of rolling tire: A tire cavity accelerometer mediated approach”, Ph.D. thesis, Virginia Tech (2020).

## Vita

Pradosh P. Dash earned his Bachelor of Technology in Mechanical Engineering from the National Institute of Technology in Rourkela, India, in 2015 and started his career in Noise, Vibration, and Harshness (NVH) engineering for powertrain systems in the R&D division at Bajaj Auto Ltd. Pradosh then attended Virginia Tech to pursue his interest in vibrations and acoustics. He received a Master of Science in 2020 for his research on operational modal analysis[172]to predict structure-borne noise.

In 2020, he began his Ph.D. at the Georgia Institute of Technology, working with Prof. Costas D. Arvanitis in the Ultrasound Biophysics and Bioengineering Laboratory. His doctoral research focused on holography-based transcranial focused ultrasound therapy and monitoring using nonlinear acoustics. While he was a graduate student, he also completed a Research Scientist Internship at Meta Reality Labs, where he worked on ultrasound-based sensors for robotics applications. Pradosh has actively engaged with the academic community at Georgia Tech during his PhD, serving as president of the IEEE UFFC Society’s Georgia Tech Chapter and as the national representative for the Acoustical Society of America. Post graduation, he looks forward to continuing his work on connecting wave physics and acoustics.

pradosh-dash.github.iolinkedin.com/in/ppdash

## 


- 


Major funding support from
