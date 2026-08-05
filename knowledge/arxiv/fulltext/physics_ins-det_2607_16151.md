# Radiopurity material assays and radiation exposure projections for superconducting qubit measurements at SNOLAB

**arXiv ID**: 2607.16151v1
**Authors**: Y. Ahmed, B. Binoy, R. Bunker, D. Chauhan, P. Delsing, R. Germond, J. Hall, Z. Hong, A. Iqbal, V. Iyer, A. Klepikova, A. Kubik, S. P. Mantry, A. C. Masuskapoe, C. C. Monk, G. Peng, P. Qin, W. Rau, T. Reynolds, M. Stukel, C. M. Wilson, B. Zatschler, S. Zatschler, A. Zuniga
**Published**: 2026-07-17
**Categories**: physics.ins-det, quant-ph
**Comments**: 44 pages, 11 figures, 15 tables including appendices. To be submitted to the Journal of Instrumentation
**HTML URL**: https://arxiv.org/html/2607.16151v1

## Abstract

Interactions of cosmic rays and other forms of ionizing radiation pose a significant challenge to the reliable operation of state-of-the-art quantum devices and error correction in quantum computing based on superconducting circuits which are typically fabricated on semiconductor substrates. Shielded by 2 km of rock overburden, the Cryogenic Underground TEst facility (CUTE) at SNOLAB provides a unique ultra-low radiation environment to probe the performance of quantum technologies with a particular interest in quantum coherence studies. In this article, we present the findings of an extensive material assaying program in preparation for the first underground operation of superconducting qubits at SNOLAB. The radioactivity levels identified by the material assays enter a thorough Monte Carlo study based on the Geant4 particle physics tracking code. From these simulations, we estimate the rates of energy deposits from radiogenic sources expected for a quantum-device assembly operated in the CUTE facility. We further characterize the spectral components of the projected background and identify the dominant particle interaction types. Finally, we outline how crystal dynamics simulations using the G4CMP solid-state physics extension for Geant4 can inform the community-wide efforts to identify effective strategies to mitigate the effects of high-energy particle impacts.

## Full Text

Radiopurity material assays and radiation exposure projections for superconducting qubit measurements at SNOLAB

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.16151v1 [physics.ins-det] 17 Jul 2026

## Radiopurity material assays and radiation exposure projections for superconducting qubit measurements at SNOLABY. AhmedB. BinoyR. BunkerD. ChauhanP. DelsingR. GermondJ. HallZ. HongA. IqbalV. IyerA. KlepikovaA. KubikS. P. MantryA. C. MasuskapoeC. C. MonkG. PengP. QinW. RauT. ReynoldsM. StukelC. M. WilsonB. ZatschlerS. Zatschler,11footnotetext:Corresponding authors.A. Zuniga

## Abstract

Interactions of cosmic rays and other forms of ionizing radiation pose a significant challenge to the reliable operation of state-of-the-art quantum devices and error correction in quantum computing based on superconducting circuits which are typically fabricated on semiconductor substrates.
Shielded by 2 km of rock overburden, the Cryogenic Underground TEst facility (CUTE) at SNOLAB provides a unique ultra-low radiation environment to probe the performance of quantum technologies with a particular interest in quantum coherence studies.
In this article, we present the findings of an extensive material assaying program in preparation for the first underground operation of superconducting qubits at SNOLAB.
The radioactivity levels identified by the material assays enter a thorough Monte Carlo study based on theGeant4particle physics tracking code.
From these simulations, we estimate the rates of energy deposits from radiogenic sources expected for a quantum-device assembly operated in the CUTE facility.
We further characterize the spectral components of the projected background and identify the dominant particle interaction types.
Finally, we outline how crystal dynamics simulations using the G4CMP solid-state physics extension forGeant4can inform the community-wide efforts to identify effective strategies to mitigate the effects of high-energy particle impacts.

## 1Introduction

In recent decades, the emergence of quantum information science (QIS) has intensified research toward using quantum circuits as quantum bits (qubits)[37,48].
The realization that superconducting qubits can be controlled and read out reliably with microwave pulses[12,30]led to the creation of the field of circuit quantum electrodynamics[13].
Although many platforms are still being pursued to implement quantum information processing, superconducting circuit architectures are one of the leading candidates[14,12,13,30], partly because of their ease of fabrication using well-established semiconductor manufacturing techniques.
One specific realization of a hardware-level implementation of a qubit is the so-calledtransmon qubit[39,60].
Transmon qubits are designed to have reduced sensitivity to charge noise and operate as anharmonic LC222The term “LC” refers to an inductanceLLand capacitanceCC.oscillators with distinct, non-equidistant energy levels.
These systems utilize the quantum dynamics of electromagnetic fields by embedding a nonlinear inductor, in the form of a Josephson junction, into complex systems of planar microwave circuitry made from superconductors[54,14].
By engineering Josephson junctions into various topologies, the nonlinearity of the resulting circuit can be used as the basis of a qubit with individually addressable quantum states[60].
The use of superconductors for the surrounding microwave circuitry also minimizes dissipation.
This circumstance is important because it allows the typically fragile qubit states to survive for long enough that the fundamental interactions to create and process quantum information can be leveraged at microwave frequencies[14,12,13,30].

A key characteristic affecting the computing potential of qubits in real-world applications is the coherence time which indicates, on average, how long a qubit will remain in a prepared quantum state.
Improving the coherence time of superconducting qubits has been a major research focus for the last decade[37,60].
Experimental studies demonstrated that ionizing radiation can cause decoherence in superconducting qubits[71,72,50,20], superconducting resonators[21]and superconducting quantum interference devices (SQUIDs)[22].
Further studies observed sequences of quantum errors correlated in time which occur across multiple qubits and extend over entire device substrates[21,72,15,23].
These correlated quantum error events exhibit signatures consistent with the generation of non-equilibrium quasiparticles induced by ionizing radiation[62,40,24]and have been shown to arise in part from cosmic-ray interactions with the substrate[31,44].
Importantly, a single high-energy interaction can create cascades of excitations that simultaneously affect multiple qubits, producing strongly correlated error bursts.
Such events violate the core assumptions of most quantum error correction schemes, including the surface code[29], which rely on sparse and uncorrelated errors in time and space[63,69,38].
As a result, radiation-induced errors can be exceptionally difficult to detect and correct with existing techniques, motivating ongoing efforts to engineer more resilient qubit designs[64,49].

Identifying the fundamental mechanisms that lead to quantum decoherence in the presence of ionizing radiation requires the ability to test quantum devices while reliably controlling the radiation environment.
To address this need, new experimental facilities were developed in shallow and deep underground laboratories worldwide[47,15,21].
At this interface, the QUTEbits collaboration333The QUTEbits collaboration consists of researchers from the Institute for Quantum Computing (IQC) at the University of Waterloo, the University of Toronto, SNOLAB and Laurentian University in Ontario, Canada, as well as Chalmers University of Technology in Sweden.was formed to investigate the impact of radiation and cosmic rays on quantum technologies.
A key focus of this new collaboration is to study how ionizing radiation affects the coherence of individual qubits and how it causes correlated errors that are problematic for quantum error correction.
The goal of the project is to perform an advanced characterization of superconducting qubits by comparing the results of coherence times measured in surface laboratories to those measured deep underground at SNOLAB[27,65]with identical quantum devices.

SNOLAB is located at the 6800-foot level in Vale’s Creighton Mine near Sudbury, Ontario, and uses the Canadian Shield to protect experiments from the cosmic rays present at the Earth’s surface.
As one of the deepest and cleanest underground science facilities in operation in the world, the rock overburden of 2 km (equivalent to 6000 m of water coverage) achieves a suppression of the cosmic ray induced muon flux by a factor of fifty million compared to the surface[56].
One of the underground facilities available to SNOLAB users is CUTE – the Cryogenic Underground TEst facility – which is a platform for testing and operating cryogenic devices in an environment with low levels of background radiation[19].
CUTE was constructed originally for testing cryogenic detectors for the SuperCDMS SNOLAB dark matter experiment[3,9,36].
CUTE is now a SNOLAB user facility and is available for projects based on proposals assessed for their scientific and technological merits.
The facility consists of a 3.5 m wide tank filled with highly purified water that has a drywell of about 50 cm diameter in its center.
The drywell is lined with a magnetic shield and 11 cm of lead for shielding against environmental radiation.
Located within this shielding is a cryogen-free dilution refrigerator mounted on a vibration-isolating damper system.
Inside the cryostat, directly above the experimental volume (∼\sim20 L) is a 13 cm thick layer of lead encased in 1.5 cm of copper acting as an internal radiation shield.
It covers the direct line of sight above the experimental space and shields from radioactive materials in the brazing of the dilution unit.

The first quantum research project approved to be hosted in SNOLAB’s CUTE facility is the QUTEbits project.
In this report, we present a detailed Monte Carlo study for this project, propagating the results of an extensive material-assay program with theGeant4particle physics tracking code[4,10,11].
The Monte Carlo simulations allow us to estimate the expected rates of energy deposits from ambient radioactive background sources as observed by the proposed quantum-device payload to be operated in CUTE.

This article is organized as follows: in section2we report on the radioactivity measurements, their results, and highlight notable findings.
Section3describes the radiation modeling workflow withGeant4, covering the geometry implementation of the experimental apparatus and our approaches to account for different categories of background sources.
A detailed breakdown of the composition of each background category is provided.
In section4, we present the results of the simulation data analysis with a summary of the background composition.
This section also includes a comparison of the total expected background rate to the rate of ionizing radiation hits caused by the presence of radioactive calibration sources in the vicinity of the quantum-device payload.
In section5, we extend the particle tracking simulations to include crystal dynamics effects by making use of theGeant4Condensed Matter Physics (G4CMP) package[35].
The results obtained from G4CMP, such as the phonon energy collection time, feed back into the processing of theGeant4background and radiation source simulations.
In section6, we close with our conclusions.

## 2Radioactivity measurements

Radioactive isotopes are prevalent in our everyday world and are present to some degree in all materials due to their natural abundance and long half-lives.
Additionally, radioactive contaminants may be introduced at various stages of manufacturing processes.
A common form of contamination arises from the accumulation of radioisotopes on the surfaces of materials through exposure to dust and radon in the air.
Dust can have relatively high concentrations of238U,232Th, and40K[26].
Likewise, the decay products from airborne222Rn can implant into surfaces, leading to an accumulation of the long-lived radioisotope210Pb (and by extension its210Bi and210Po progeny), producing a nearly constant emission ofγ\gammarays,β\betaelectrons, andα\alphaparticles[17].
Radioisotopes can also be introduced as byproducts from cosmic-ray interactions – a process known as cosmogenic activation.
Common examples of radioisotopes produced through cosmogenic activation include tritium,54Mn, and several cobalt species[41].
It should be noted that the activity produced is typically lower than the activity of contaminants introduced by dust or radon[26].

The level of radioactivity in a material can be probed with different techniques.
In order to measure the level of radioactive contamination from a complex decay chain such as the primordial decay chains of238U and232Th, not all of the elements need to be separated out.
Instead, typical trace elements can be used to evaluate whether there are any deviations from secular equilibrium in the decay chain.
Because of the presence of long-lived isotopes and the mobile noble gas radon in the238U decay chain, activities for this chain are often reported separately for the “top” and “bottom” part where the break is at226Ra.
The same convention will be used in this report.

## 2.1Low-background counting techniques

Prior to upgrading the CUTE cryostat at SNOLAB for microwave measurements of superconducting qubits, the collaboration characterized the radioactivity of common components and materials.
SNOLAB provides a world-class low-background measurement laboratory in its underground facility to screen materials for radioactive impurities[42,43].
The counting facility’s primary goal is to identify materials which have low concentrations of naturally occurring40K and the long-lived decay chains of238U and232Th, often well below the parts per trillion (ppt) level.
These radioactivity levels are below what is generally accessible by chemical and analytical techniques, therefore assay methods are often performed through radiation counting using high-purity germanium (HPGe) detectors.
HPGe spectroscopy can reach sensitivities of𝒪​(10)\mathcal{O}(10)to𝒪​(100)\mathcal{O}(100)μ\muBq/kg for isotopes in the primordial decay chains.

The presence of radioactive isotopes in a sample can be identified via their characteristicγ\gammarays.
A comparison with background rates together with Monte Carlo simulations assessing the impact of the sample characteristics allows for a quantification of the contaminants, where upper limits are extracted when no significant excess above background is observed.

For the QUTEbits project, radioactivity measurements were performed with several HPGe detectors, each with varying sensitivity to the relevant isotopes of interest and optimized for different sample sizes.
All of the detectors are situated in the low-background counting laboratory atSNOLAB(approximately 2 km below surface), and protected from environmentalγ\gammarays with roughly 20 cm of lead shielding and 5 cm of copper shielding.
The detectors are constantly flushed with evaporated dry nitrogen at a rate of 2 L/min to suppress radon which is present in the environmental air[68].
Characteristics of the five SNOLAB HPGe detectors (PGT, Canberra, Lively, Gopher, VDA) and their isotope-specific sensitivities are presented in table1.Table 1:Characteristics and sensitivities of the SNOLAB HPGe detectors[68]. The relative efficiencies are reported with respect to a standard NaI(Tl) detector.DetectorPGTCanberraLivelyGopherVDADetector volume [cm3]210300400400400Relative efficiency55%80%107%120%120%Nominal sample size1 L8 mL1 L1 L1 LEnergy range [keV]90–300010–90040–300040–300040–3000238U sensitivity [mBq]0.110.020.050.170.09235U sensitivity [mBq]0.160.010.020.080.06232Th sensitivity [mBq]0.100.020.060.210.0840K sensitivity [mBq]1.420.920.451.011.22137Cs sensitivity [mBq]0.130.020.020.080.0560Co sensitivity [mBq]0.040.030.020.040.0254Mn sensitivity [mBq]0.0430.0330.0210.0440.034210Pb sensitivity [mBq]-0.5531.5316.497.71

Most of the recorded HPGe detector spectra are evaluated for the same set of radioactive isotopes including the top and bottom parts of the238U decay chain, the235U decay chain, the232Th decay chain and single-isotope decays including40K,137Cs and60Co.
For the bottom part of the238U decay chain, only isotopes down to214Bi are included in the evaluation, leaving210Pb to be determined separately.
For some materials, we also looked for typical cosmogenic activation products such as57Co,58Co and54Mn.

## 2.2Material assay results

A selection of the collected radioactivity data of the assayed components is presented in table2.
This selection is limited to the naturally occurring decay chains and40K. It lists the assays of the components which we are going to deploy for the QUTEbits measurements and thus are considered in the subsequent background simulation studies as discussed in section3.
A complete list of all assayed components can be found in appendixA, table10.
All assay results (including results of isotopes not listed in this report) have been made publicly available onradiopurity.org444Search for keyword “QBITS-CUTE” or “QUBITS-CUTE” on the website.[46,67].Table 2:Assay results of components considered in the background simulation studies. Listed are the component names, the corresponding quantity and the mass of a single component, and the determined radioactivity level of the natural decay chains and40K. Some assay results are reported as 90% C.L. upper limits. In order to account for disequilibrium within the238U decay chain, it is split at226Ra into the top (t) and bottom (b) of the decay chain. If no quantity value is given in the second column, the mass value in the third column is the total component mass.ComponentQuantityMass238U235U232Th210Pb40Kin setup[g][mBq/kg][mBq/kg][mBq/kg][mBq/kg][mBq/kg]Si chip20.057t:<<516.8<<22.0<<28.5(29±\pm22)⋅103\cdot 10^{3}<<336.7b:<<12.6PCB in OQTO holder23.9t: 6132±\pm1973106.5±\pm27.92232.0±\pm138.9-1380.1±\pm567.8b: 1499.0±\pm101.2OQTO holder2204.6t: 1099.0±\pm195.428.6±\pm2.638.4±\pm4.7-60.2±\pm25.5b: 20.4±\pm3.3Cu in QUTEbits stack-1688t:<<130.81.2±\pm1.6<<4.9-<<65.1b:<<2.4Microwave switch395.5t: 7554.0±\pm667.9133.5±\pm8.2826.0±\pm32.7(41±\pm15)⋅104\cdot 10^{4}806.2±\pm92.6b: 453.0±\pm19.8Al cavity637.2t:<<85.7<<2.89.5±\pm3.6-<<26.9b:<<3.9CM shield at QUTEbits stack11354t:<<171.4<<14.6134.1±\pm21.4<<3703<<126.6CM shield at internal lead12005b: 3.7±\pm19.8Formable non-magnetic1410.1t: 787.7±\pm1024.0<<14.2<<38.9-233.6±\pm289.6cable assemblyb:<<37.7SMA connectors163.59t: 96.7±\pm41.85.6±\pm1.41.2±\pm3.96922.0±\pm407.591.7±\pm99.8b:<<3.8Brass screws500.87t:<<62.2<<6.6<<11.8<<603.7391.5±\pm525.7b:<<15.0BF-6 glue at Si chip10.012t:<<44.7<<1.626.6±\pm4.5<<13042.9±\pm24.4b:<<1.3CliQ10 IR filter425.3t: 39.6±\pm23.32.4±\pm1.246.4±\pm6.1<<146.4720.3±\pm246.5b: 32.5±\pm6.1

The proximity of a component with respect to the quantum-device substrate (silicon in this case) is related to its impact in terms of additional radiation; closer components may contribute more, whereas components located farther away are likely to be shielded and may contribute less.
In the simulations we denote the “QUTEbits stack” as the assembly of all components inside the cryogenic magnetic (CM) shield which completely encloses the OQTO holder[1]containing the QUTEbits Si chip, up to six 3D Al resonator cavities, and several electronic components (see section3.1for a detailed description).
The components listed in table2are all within this CM shield, except for a second CM shield surrounding the internal lead shield of CUTE and the microwave switches located in between the internal shield and the QUTEbits stack.
The OQTO holder, PCB and the BF-6 glue are the only components which are in direct line of sight with the Si chips.
However, the Al cavities are in direct line of sight to several cables, screws, the CliQ10 IR filters and various Cu parts in the QUTEbits stack.

The expected emission rate of a component can be calculated from the specific activity reported in table2and the component mass.
Figure1displays a summary of the emission rates for the components and isotopes of interest.Figure 1:Emission rate of each component for each measured isotope or decay chain. The emission rate is calculated per piece, not taking into account the actual quantity of components to be used in the QUTEbits setup. A line extending from the marker to the bottom of the plot indicates an upper limit of the corresponding assay result at 90% C.L., while all other values are measurements with symmetric error bars, which appear asymmetric on logarithmic scale.

In addition to the assayed components for the QUTEbits project, figure1also includes a combined representation of the assays of the CUTE cryogenic vessels as well as the CUTE shielding layers, which includes the internal lead shield above the QUTEbits stack, the different layers of thermal shielding within the cryostat, several stainless steel components such as the outer vacuum chamber, the outer radiation lead shield and the ultra pure water in the CUTE water tank.
The CUTE material assay results are available online at[68].

## 2.3Notable assay findings

While a comprehensive simulation study (see section3) provides an estimate of the impact of individual components, the emission rate of each component can already be a helpful indicator for material selection criteria and design choices.
Considering the assembly geometry, the most significant background contributions are from components with a direct line of sight to the Si chips and from components that are part of the Si chip assembly.

Single-crystal Si is a common substrate material for quantum devices.
The screening results from several Si wafers show similar contamination levels compared to each other (see table10). However, most of the results are upper limits and those not quoted as upper limits have large uncertainties and could arguably be considered to be upper limits. Thus, it is expected that the Si samples are actually much cleaner than indicated by the assay results which is consistent with other findings[5].
In any case, because the Al circuit layer is directly deposited onto the Si substrate, the radiopurity of the silicon is a central contribution to the overall background budget.
By considering these assays in our background simulation campaign, we adopt a very conservative approach leading to the background rate being dominated by the Si assay results.

For several of the assayed components, the reported210Pb activities and uncertainties appear unrealistically high.
These measurements are likely imprecise because the HPGe detector sensitivity is poor for210Pb (see table1).
The main emittedγ\gammaray has a relatively low energy (46.5 keV) and is readily absorbed within the sample or the HPGe detector enclosure such that it cannot be detected efficiently.
We also note a potential systematic uncertainty related to the distribution of210Pb in the sample.
The assumption that210Pb is homogeneously distributed in the sample may be incorrect, because210Pb can accumulate on surfaces when a material is exposed to air which contains radon.
We explore this possibility in section3.5.

Several raw aluminum samples used for the deposition of the thin superconducting Al films on top of the Si substrates were screened, and their rates were generally found to be quite low with a few exceptions of rather high levels of238U,232Th and40K (see table10).
However, because of the tiny mass of the films, we can safely neglect their contribution.

Printed circuit boards (PCBs) from multiple vendors were assayed and their respective activities were found to be relatively high.
While this is not surprising as the many steps in the manufacturing process can lead to the introduction of additional radioisotopes that can be held in the materials, this does point to an important avenue for reducing backgrounds as this component would be in direct contact with the Si chip.
Notably, some of the measured PCBs were much more radioactive than others (see table10), indicating which products are suitable for the anticipated low-background assembly to be operated in CUTE.

For the OQTO holder made from copper, the assay results turned out to be low in radioactivity.
The OQTO holder was assayed with its brass screws and SMA connectors in place, which were also measured separately.
The radioactivity of the brass screws was below the detector’s sensitivity and the SMA connectors were relatively clean except for210Pb.
The most radioactive part of the SMA connectors are the SMA pins, which were assayed separately as well (see table10).

Components that would be mounted below the internal lead shield of CUTE, but not in direct line of sight of the Si chips, include up to six 3D Al resonator cavities and two cylindrical CM shields (used for shielding against environmental magnetic fields).
Some of the assayed Amumetal samples showed high levels of238U and210Pb.
For the CM shield material, we requested samples from different vendors, and the sample provided by Ad-Vance Magnetics Inc (referred to as “CP-EXP-1184”) met our radiopurity requirements.

For the formable non-magnetic cable assembly (EZ-FLEX.86-CU from EZ Form cable) inside the QUTEbits stack that connects the qubit holder to the feedthrough plate mounted on the magnetic shield, the measured activities were close to the sensitivity of the HPGe detector.
The readout components above the level of the CUTE internal lead shield include additional microwave cables, filters, and circulators.
Most of the cables that would be above the internal lead shield did not show high levels of radioactivity, nor did the circulators.
Since the internal lead shield absorbs radiation very well, none of the components above the internal shield were considered in the simulation studies discussed in section3.

We considered two potential locations for dedicated IR absorbers: one directly at the inside of the CM shield, and another one inside the OQTO holder on surfaces with direct line of sight to the Si chip.
For both cases, the components of a hypothetical recipe consisting of a Cu sheet, Stycast 1266, glass beads and carbon black (also known as Berkeley Black[57]) were assayed separately.
Considering the constituents’ mass contribution, carbon black would dominate the emission rate, and we decided to replace it with a copper powder in our simulation studies (see assay results in table10).
While this reduced the expected radioactivity of the IR absorber assembly, more work is needed to identify vendors for specific components such as the glass beads with sufficiently low levels of radioactivity.
Consequently, the initial QUTEbits measurements will be performed without such IR absorbers and the total background rates reported in this article do not include their contribution.
We do, however, discuss their potential impact in appendixB.

Finally, it shall be noted that the BF-6 glue provided by Ukrvet Biopharm, Ukraine, turned out to be quite clean and can be recommended for use in low-background environments.

## 2.4Cosmogenic activation products

Secondary cosmic-ray particles such as neutrons, protons and muons can trigger nuclear reactions and in consequence lead to the activation of materials.
As the particle flux is strongly suppressed underground, this effect is negligible for materials stored at locations like SNOLAB.
Due to the rather high energy of these particles, spallation reactions can produce various radionuclides, e.g.60Co,58Co,57Co and54Mn which may contribute noticeably to the overall background budget, as indicated in figure1.
For copper, the most important activation product is60Co because of its high production rate, relatively long half-life and high-energy gamma emission[41].

A complete tracking of the location of materials allows the activity of each radionuclide to be estimated using production rates provided in the literature, such as[41].
However, the emission rates were deemed to be not significant enough compared to the overall radiopurity of the considered materials to justify this effort.
Thus, for this project the assay results of60Co,58Co,57Co and54Mn were used instead, even though the assayed component may have a different exposure history regarding cosmogenic activation than the actual component used in the final QUTEbits setup.

A cosmogenic activation product commonly found in silicon is32Si, aβ\betaemitter with a half-life of 153 years.
It is primarily produced in the atmosphere and can be introduced into silicon in different ways and at different stages of the production process[55], leading to significant sample-to-sample variations in terms of specific activity[18,6,5].
The DAMIC collaboration measured the32Si content of different batches of their silicon CCDs[6,5], with the latest measurement indicating140±30​μ​Bq/kg140\pm 30\,\mathrm{\mu Bq/kg}of32Si in the CCD substrates.
Compared to other sources of radioactivity in the QUTEbits setup, this level of32Si activity is negligible for us.

## 3Radiation exposure modeling withGeant4

TheGeant4toolkit is a Monte Carlo simulation code which models the passage of particles through matter[4,10,11].
Of particular interest for this work is the radioactive decay of various isotopes and the interaction of the emitted particles with the surrounding matter, most importantly the energy deposits in the Si substrates and Al cavities.
A comprehensive description of radioactive decay physics and how these are modeled inGeant4’s radioactive decay module can be found in[32,33].

The general workflow to model the radiation exposure in the Si chips and Al cavities is as follows:
at firstGeant4volumes are designed as geometrical representations of all relevant components and material properties are assigned accordingly.
The assays presented in section2.2are mapped to the corresponding volumes, i.e. each volume is homogeneously contaminated with the radioisotopes it contains according to the assay results.
The decay of these contaminants is modeled byGeant4as a primary event and the emission products are tracked through the geometry where they interact with matter, create secondary particles and are eventually absorbed in a material.
For these simulations, theShieldingphysics lists, including NeutronHP, together with the electromagnetic option 4 (EMZ) were used withGeant4-10.7.4.
In the case of decay chains, all subsequent decays are modeled, if not specified otherwise.
For the top part of the238U decay chain, the decays are stopped at226Ra, while for the bottom part they start with the decay of226Ra, which allows modeling of the disequilibrium indicated in some of the assay results.

Finally, all energy deposits of the particles reaching the Si chips or any of the 3D Al cavities are recorded.
In the analysis procedure described in section3.2, these energy deposits are grouped into physical events according to their timestamps.
Together with the total number of simulated primary decays and the isotope emission rates from the assay results (see also figure1), the event rates inside the Si chips and Al cavities can be calculated.

In addition to the bulk material radioactive contaminants identified from the assay results, we simulated contamination accumulated on a material’s surface due to radon exposure and ionizing radiation from the SNOLAB rock cavern; these are discussed in the following sections.
Note that we neglect any radioactive contribution from dust accumulation in our studies, because SNOLAB is a controlled class 2000 cleanroom environment.
In addition, all components were wiped upon entering the CUTE cleanroom, which achieves class 200 cleanroom conditions on average[19].

## 3.1Geometry overview

The QUTEbits setup is deployed into CUTE at SNOLAB[19].
A visualization of the CUTE shielding and its cryogenic stages is shown in figure2.
OurGeant4geometry model also contains a rough representation of the SNOLAB rock cavern around the CUTE facility.Figure 2:Visualization of the CUTE geometry inGeant4. Left: components from outside to inside include: PE block on top (gray), water tank (blue), stainless steel cans (green, yellow, gray), two layers of lead (lilac, dark purple), mu-metal magnetic shield (dark gray), OVC (pink) and cryogenic stages (50 K – red, 4 K – white, 1 K – light blue, 100 mK – mid blue, MC – blue). The internal lead shield (dark gray) is encased in copper (brown) and a CM shield (mint green). Right: above the QUTEbits stack, there are an additional MC plate (blue) and microwave switches (gray, brown). The QUTEbits stack is enclosed by a CM shield (mint green) and hosts Al cavities (light gray) mounted to the top. The OQTO holder (dark gray) contains the PCB (green) and the Si chip (red), which is partly visible through a transparent lid.

The CUTE shielding consists of a water tank and a polyethylene (PE) block on top of it to moderate and absorb neutrons emitted by the cavern walls.
Stainless steel cans are submerged into the water tank forming a drywell that hosts the inner shielding as well as mechanical and electronics parts.
Two layers of lead with a total thickness of about 11 cm absorb high-energyγ\gammarays from the cavern walls and other external materials.
A mu-metal shield is present between them to protect sensitive electronics from environmental magnetic fields.

The CUTE cryogenic stages have an outer vacuum chamber (OVC) made of stainless steel at the outside, and several cryogenic stages made of copper: 50 K, 4 K, 1 K, 100 mK and 10 mK.
The coldest stage is denoted as the mixing chamber (MC).
Inside the cryostat, there is an internal lead shield above the experimental payload which is thermally anchored to the 1 K stage.
It serves as an absorber forγ\gammarays from electronics located at warmer stages and the cryostat itself.
As lead typically contains several radioactive contaminants, it is encased in radiopure copper.

The QUTEbits sample space at the MC is fully enclosed in a CM shield.
It is designed to hold up to two OQTO sample holders[1]mounted back-to-back on a copper plate (see figure2).
Each OQTO holder hosts one Si chip with a dimension of7×7×0.57\times 7\times 0.5mm3(mass of 57.1 mg) and a 300 nm thick Al circuit layer.
These Si chips are patterned with different quantum circuit designs and are provided by Chalmers University of Technology and the Institute for Quantum Computing (IQC) at the University of Waterloo.
The circuit mask is not relevant for theGeant4radiation transport simulations, but it matters when studying the propagation of charge carriers and lattice vibrations (phonons) with G4CMP (see section5).

The QUTEbits setup can also host up to six Al cavities acting as 3D resonators.
Inside the CM shield, there are several copper parts supporting the Al cavities and OQTO holders, ensuring thermal conductivity to the MC stage.
The internal lead shield above the payload can be surrounded by an additional CM shield to isolate any trapped magnetic flux from the lead block when it transitions to its superconducting state at a critical temperature ofTc=7.2T_{c}=7.2K.

Additionally, there are several small components which do not have a physical geometry in the simulation, because their attenuation of radiation is negligible compared to other volumes.
These include microwave connectors, cables and adapters as well as screws and washers, but also the IR filters at the OQTO holder and glue spots on the Si chip.
To take into account their radioactive contributions, these contaminants are mapped to a representative volume and if applicable limited to a certain region of the volume.

In each QUTEbits run, a different configuration of the internal assembly might be used.
In particular, there could be runs with two OQTO holders and no Al cavities, or with just one OQTO holder and up to six Al cavities.
These modest changes in the setup can be taken into account by switching off components in the overall background budget calculation.
For the following sections, the full setup described above and shown in figure2is assumed.

## 3.2Geant4detector hit processing

This section describes the output format and event processing applied in our simulation pipeline.
OurGeant4application saves energy deposits in the sensitive elements (Si chips, Al cavities) using a particle hit collection in a ROOT TTree format[16].
Along with the particle type that created the hit and the amount of deposited energy, we store additional G4Track information such as the hit time with respect to the time when the primary decay took place (defined as start timet=0≡t0t=0\equiv t_{0}in our framework).
Saving the simulation output per particle hit allows for an offline processing without having to rerun large parts of the particle tracking simulation to extract additional G4Track information of interest.

The hit processing output consists of binned energy histograms for each sensitive detector.
The standard hit processing involves the following steps.
First, we sum all energy deposits that occur in the same geometry element within a time period ofΔ​t=15​μ\Delta t=15\,\mus in eachGeant4event.
This step virtually splits complexGeant4events that may span large time periods, e.g. for decay chains with tens of seconds to years in between consecutive decays, into sensible readout time windows that would be recorded in a real-world device as a single topological event.
The split time windowΔ​t\Delta tis informed by crystal dynamics simulations using G4CMP[35]in response to radiation hits as discussed in section5.1.
By evaluating the particle type that resulted in an energy deposit, the energy spectra observed by the detectors can be split according to the underlying radiation type.
In our case, we distinguish betweenα\alphaparticle hits,β/γ\beta/\gammahits and nuclear recoils induced by neutron interactions or nuclei (see section4.1).

For the calibration source simulations using252Cf discussed in section4.2, there is an additional step in the hit processing which includes some but not all hits arising from the decay chain seeded by252Cf.
By default,Geant4models the full252Cf decay chain which includes several long-lived isotopes such as248Cm (T1/2=3.5⋅105T_{1/2}=3.5\cdot 10^{5}yr) and244Pu (T1/2=8.1⋅107T_{1/2}=8.1\cdot 10^{7}yr).
Only a very small fraction of these long-lived decay products are likely to contribute to the radiation exposure over the course of the experiment.
To ensure fair consideration of subsequent decays while limiting the radiation exposure to the reasonably observable fraction, we reject hits that occur more than 6 years after the primary252Cf decay.
This choice is also intended to mimic the effects of aging.
Over time, the aging of the source alters its emitted spectrum, evolving from an almost pure252Cf spectrum (when the source was manufactured) to a more diverse spectrum with significant contributions from decay products with half-lives longer thanT1/2(252Cf)=2.6T_{1/2}(^{252}\text{Cf})=2.6yr.
The 6-yr cutoff corresponds to the approximate age of the source at the time of the planned QUTEbits measurements.
In practice, this additional hit selection does not have a significant impact on our reported rates.

## 3.3Bulk contamination

Contaminants in the bulk of a material are simulated by uniformly distributing the identified isotopes throughout the volume.
The characteristic decays are then generated byGeant4, the emitted particles are propagated through the geometry and the energy deposits are recorded and analyzed as described in section3.2.

If a component is not represented by a dedicated geometry in the simulation, a representative volume has been identified and contaminated.
For instance, for connectors punching through the CM shield, the corresponding part of the CM shield has been contaminated according to the connectors’ assay measurements, while for the BF-6 glue at the Si chip, a small surface area at each of the four corners of the Si chip was contaminated.
On the other hand, for the formable non-magnetic cables inside the CM shield, a virtual cylindrical volume with smaller dimensions than the CM shield was defined to homogeneously sample corresponding decay positions.

The individual contributions to the overall background rate of each of the 482 combinations of components and corresponding isotopes (see appendixEfor more details) were grouped into component categories.
The resulting event rates for these categories are shown in figure3for the example of one of the two Si chips and in figure4for one of the six Al cavities.
The event rates are very similar for both Si chips and among the six Al cavities, respectively.

The event rate calculations take into account whether an assay result was reported as an upper limit or as a measurement with uncertainties.
The statistical uncertainties from the simulations are generally negligible with the exception of volumes far away from the payload or for isotopes which emit only low-energyγ\gammarays.
If no hits were registered in a simulation, a 90% C.L. upper limit is calculated using the Feldman-Cousins method for Poisson signals[28].
Consequently, the event rate of a component which originally had an assay measurement with an uncertainty as shown in figure1, may appear as an upper limit in figure3or figure4.Figure 3:Simulated event rates in one of the Si chips according to the assay results and corresponding emission rates for various components. The Si chip itself, as well as components in direct line of sight, are the dominating backgrounds. A line extending from a marker to the bottom of the plot indicates a 90% C.L. upper limit.Figure 4:Simulated event rates in one of the Al cavities according to the assay results and corresponding emission rates for various components. The dominant background originates from the Al cavity itself and components which are in direct line of sight. A line extending from a marker to the bottom of the plot indicates a 90% C.L. upper limit.

Figure3indicates that the dominating background contribution for the Si chip originates from the substrate itself as well as the PCB (see appendixBfor a comparison of different PCBs) and the OQTO holder, i.e. the components which are in direct contact with it.
While the BF-6 glue is also in direct contact with the Si chip, due to its radiopurity and tiny mass, its contribution is two orders of magnitude lower.

The event rate in the Si chip induced by the connectors and screws is several orders of magnitude below the contribution of the Si chip itself, mainly because none of the screws or connectors are in direct line of sight, but also because they are relatively low in radioactivity.

We also simulated two potential IR absorbers – one at the CM shield, and one inside the OQTO holder – but do not include them in the total background projections, because their emission rate was deemed to be too high.
Their background estimates are shown in figures3and4and are discussed in appendixBconsidering different recipes.

The event rates in one of the Al cavities, displayed in figure4, show similar results.
The largest contributions are from the Al cavities themselves, as well as components in direct line of sight.
For both, the Si chips and the Al cavities, we observe that even though the CUTE shielding layers have by far the highest emission rate (see figure1) among all components, their contribution to the background event rate in the devices is at least one order of magnitude lower compared to the contributions from the internal device components.
This validates the design of the CUTE shielding, e.g. the high emission rate of the outer lead shield is compensated by its distance to the payload and the presence of the inner shielding layers absorbing most of the emittedγ\gammarays.

As pointed out in section2.3, it is challenging to make a precise assessment of the210Pb contamination in the bulk of a material by using HPGe spectroscopy.
Hence, we report the simulated event rates in table3for one of the Si chips and Al cavities with and without taking into account the reported210Pb bulk assays.
Table3also shows the composition of the total event rate broken down by particle type.
For the Si chips, the total background rate is one order of magnitude higher when taking into account the210Pb bulk assay results, while for the Al cavity the effect is subdominant because the assay of aluminum does not include results for210Pb itself.Table 3:Simulated background rates in one Si chip and one Al cavity from bulk contaminants of all considered components. The rates are reported with and without the contribution of the210Pb assays. In addition, the total rates are broken down by particle type.DetectorSi chipAl cavitywith210Pbwithout210Pbwith210Pbwithout210PbTotal rate [mHz]5.575.51⋅10−15.51\cdot 10^{-1}8.50⋅1018.50\cdot 10^{1}7.78⋅1017.78\cdot 10^{1}α\alpharate [mHz]1.821.28⋅10−11.28\cdot 10^{-1}2.41⋅1012.41\cdot 10^{1}2.38⋅1012.38\cdot 10^{1}β/γ\beta/\gammarate [mHz]3.814.52⋅10−14.52\cdot 10^{-1}5.68⋅1015.68\cdot 10^{1}5.01⋅1015.01\cdot 10^{1}NR rate [mHz]5.222.08⋅10−12.08\cdot 10^{-1}4.32⋅1014.32\cdot 10^{1}4.27⋅1014.27\cdot 10^{1}

The breakdown per particle type indicates that the total background rate is roughly equally shared by the energy deposits ofα\alphaparticles, electromagnetic interactions fromβ\betaelectrons, positrons orγ\gammarays and nuclear recoils (NR) induced by neutrons interacting with a nucleus or as consequence to the radioactive decay of a nucleus.
When excluding210Pb, this ratio is mostly retained.
In all cases, theα\alphaparticle induced rate is found to be the lowest.
However, anα\alphadecay close to the detectors may deposit significantly more energy compared to the other cases (see section4.1).
Note that the sum of the rates broken down per particle type is not necessarily equal to the total rate because one simulation event can produce hits of different particle types.

## 3.4Interstitial air

The cavern rock surrounding SNOLAB contains traces of the naturally occurring long-lived isotope238U.
While the metals of the decay chain usually stay inside the rock, the gaseous and radioactive radon isotope222Rn emanates into the mine air.
As a result, the radon level underground is generally higher than in an above ground laboratory.
SNOLAB has a dedicated ventilation system that provides fresh air to the underground laboratory which reduces the constantly monitored222Rn concentration to about123.1±6.2​Bq/m3123.1\pm 6.2\,\mathrm{Bq/m^{3}}inside the laboratory[43].

This same level of222Rn diffuses into the interstitial air between the CUTE shielding layers. However, the air between the OVC and the inner of the two lead shield layers is flushed with low-radon air (<10​Bq/m3<10\,\mathrm{Bq/m^{3}})[19].
In the simulation, the air inside and outside of the CUTE lead shield has been contaminated with222Rn to determine the contribution to the overall background rate.
Table4reports the resulting rates.Table 4:Simulated background rate from222Rn decays in the interstitial air inside and outside of the low-radioactivity lead shield which surrounds the CUTE cryostat.DetectorSi chipAl cavityTotal rate [mHz]1.39⋅10−31.39\cdot 10^{-3}4.55⋅10−14.55\cdot 10^{-1}Air inside lead shield [mHz]<4.29⋅10−4<4.29\cdot 10^{-4}<1.95⋅10−1<1.95\cdot 10^{-1}Air outside lead shield [mHz]9.57⋅10−49.57\cdot 10^{-4}2.60⋅10−12.60\cdot 10^{-1}

The contribution of the interstitial air to the total background rate is about two orders of magnitude lower than from the bulk contaminants; it does not introduce a significant background rate that needs to be mitigated.
Broken down by particle type, there were no recordedα\alphaparticle hits, no NR hits in the Si chips, and only a few NR hits in the Al cavities.
The latter contribution is three orders of magnitude below theβ/γ\beta/\gammarate and is therefore negligible.

## 3.5Surface contamination

In this section, we perform a dedicated estimate of the210Pb activity due to radon exposure under different scenarios.
As noted before in section3.4, the average222Rn level underground at SNOLAB is123.1±6.2​Bq/m3123.1\pm 6.2\,\mathrm{Bq/m^{3}}[43].
On Earth’s surface, the222Rn level can widely vary depending on location, season, and ventilation.
In the SNOLAB surface building, it has been measured to be5.55±4.44​Bq/m35.55\pm 4.44\,\mathrm{Bq/m^{3}}[66], which we use as the reference value for our estimates.

When222Rn decays in air, its progeny can deposit (or “plate out”) onto exposed material surfaces.
The subsequentα\alphadecays of218Po and214Po impart significant momentum to their nuclear decay products such that they can be implanted into the material.
Further down the decay chain is the long-lived210Pb (half-life of 22.2 yr).
Exposure to radon in air therefore results in the accumulation of210Pb surface contamination through these plate-out and implantation processes.

With a half-life of 3.8 days,222Rn can easily diffuse in air due to Brownian motion and ventilation; the volume distribution is well-approximated as uniform.
Depending on the ventilation rate and the size of the room, a so-called plate-out height555Height of air above a surface from which it is expected that all radon progeny adhere to the surface below.can be determined and used to estimate the210Pb surface contamination rate[53].
For the area at SNOLAB where CUTE is located, the plate-out height for copper was measured to be36.3±0.8​cm36.3\pm 0.8\,\mathrm{cm}[70].
Because the CUTE cleanroom is supplied with low-radon air with<10​Bq/m3<10\,\mathrm{Bq/m^{3}}of222Rn[19], the210Pb accumulation inside the cleanroom can be neglected, and only the222Rn exposure in the underground laboratory and on Earth’s surface is taken into account.

The210Pb surface contaminationAPbA_{\text{Pb}}can be estimated as follows:APb​(t)=ARn⋅h⋅s⋅(1−e−λPb⋅t)withλPb=ln⁡2T1/2​(Pb210).A_{\text{Pb}}(t)=A_{\text{Rn}}\cdot h\cdot s\cdot\left(1-\mathrm{e}^{-\lambda_{\text{Pb}}\cdot t}\right)\quad\text{with}\quad\lambda_{\text{Pb}}=\frac{\ln 2}{T_{1/2}\left({}^{210}\text{Pb}\right)}.(3.1)

whereARnA_{\text{Rn}}is the radon concentration in air and is assumed to be constant,hhis the plate-out height taken from[70], andssis the exposed surface area of a component.
Table5summarizes the total emission rates from210Pb surface contamination for three radon exposure scenarios, summed over all considered components.
Because of the long half-life of210Pb, the emission rates and corresponding simulated background rates depend approximately linearly on the exposure time.Table 5:Radon exposure scenarios assuming different time spans for materials being stored on Earth’s surface and inside SNOLAB. The total emission rates of210Pb accumulated at the components’ surfaces were calculated for each of the exposure scenarios. These emission rates were used to scale the simulation results of a210Pb surface contamination to obtain an estimate of the expected surface background rates.Radon exposure scenarioshortmediumlongExposure on Earth’s surface [years]123Exposure underground at SNOLAB [days]71421Emission rate from Earth’s surface exposure [mBq]90.4178.2263.2Emission rate from SNOLAB exposure [mBq]39.178.1117.1Total emission rate [mBq]129.5256.3380.3Surface background rate in Si chip [mHz]6.94⋅10−26.94\cdot 10^{-2}1.37⋅10−11.37\cdot 10^{-1}2.04⋅10−12.04\cdot 10^{-1}Surface background rate in Al cavity [mHz]5.171.02⋅1011.02\cdot 10^{1}1.52⋅1011.52\cdot 10^{1}

Compared to the simulated background rates determined from radiocontaminants in the bulk of the materials, the simulated rate from210Pb on component surfaces is about an order of magnitude lower, which is more in line with the other bulk contaminants when neglecting the assay results for210Pb.
In the following, the radon exposure scenario with the medium time span is used.

The contribution from210Pb on a material’s surface is composed of two different categories:210Pb adsorbed on the surface, and210Pb implanted in the surface.
For the corresponding simulations, we apply the Jacobi model[34,53]to determine the ratio of adsorbed vs. implanted210Pb.
In combination withGeant4simulations, we found that this ratio is independent of the material, and about55.8%55.8\%of the210Pb is implanted, while the remaining fraction is adsorbed on the surface (see appendixCfor a discussion of the systematic uncertainties).
For these simulations, as well as for determining the implantation depth profile of210Pb, dedicatedGeant4simulations were run using the Screened Nuclear Recoil Physics List[51].
This physics list has been added to ourGeant4application[58]and validated against results obtained with SRIM[74]for individual ions.
While SRIM is limited to simulating the transport of individual ion species with a fixed momentum direction,Geant4allows simulation of complex decay chains, effectively modeling subsequent implantation of isotopes with randomized nuclear recoil direction.
This eventually leads to an implantation depth profile of210Pb which depends on the material properties.
For our study, we determined210Pb implantation depth profiles for Si, Cu, Al and mu-metal.Table 6:Simulated background rates for210Pb adsorbed on surfaces and implanted in surfaces using the medium exposure scenario presented in table5. The rates were scaled with the determined ratio between adsorbed and implanted210Pb.DetectorSi chipAl cavityContamination modeadsorbedimplantedadsorbedimplantedTotal rate [mHz]6.69⋅10−26.69\cdot 10^{-2}7.05⋅10−27.05\cdot 10^{-2}5.744.50Earth’s surface exposure [mHz]4.65⋅10−24.65\cdot 10^{-2}4.90⋅10−24.90\cdot 10^{-2}3.993.13SNOLAB exposure [mHz]2.04⋅10−22.04\cdot 10^{-2}2.15⋅10−22.15\cdot 10^{-2}1.751.37α\alpharate [mHz]1.05⋅10−21.05\cdot 10^{-2}1.63⋅10−21.63\cdot 10^{-2}0.630.91β/γ\beta/\gammarate [mHz]4.72⋅10−24.72\cdot 10^{-2}5.19⋅10−25.19\cdot 10^{-2}4.183.46NR rate [mHz]2.25⋅10−22.25\cdot 10^{-2}3.31⋅10−23.31\cdot 10^{-2}1.841.92

Table6summarizes the simulated background rates obtained for210Pb adsorbed on the surface and when using the implantation depth profiles for implanted210Pb.
The total simulated210Pb activity is a sum of the contributions due to the radon exposure on Earth’s surface and inside SNOLAB.
The breakdown per particle type may result in a higher sum because an event can be composed of multiple particle interaction types.

The contribution of adsorbed and implanted210Pb is almost equal, while the exposure on Earth’s surface has a larger impact due to the longer exposure time, which compensates the lower radon activity as indicated by the emission rates shown in table5.
The breakdown per particle type shows that the rate ofβ\betaparticles andγ\gammarays is the largest, but the contribution ofα\alphaparticles and NRs is relevant as well.

## 3.6External radiation sources

The muon flux is strongly suppressed 2 km underground at SNOLAB and has been measured to be roughly two muons per square meter per week[7].
Taking into account the tiny size of our Si chip and its vertical orientation which reduces the effective area exposed to vertically incoming particles, the background introduced by muons is completely negligible.

The cavern rock surrounding SNOLAB contains traces of40K and the natural decay chains of238U and232Th, which all emitγ\gammarays.
The natural decay chains also emitα\alphaparticles which can produce neutrons via(α,n)(\alpha,n)reactions in the rock itself.
Additionally, for some isotopes in the decay chains there is a small probability that neutrons are produced by spontaneous fission.
The thermal neutron flux at SNOLAB was measured as4144.9±49.8​(stat.)±105.3​(syst.)​n/m2/day4144.9\pm 49.8(\text{stat.})\pm 105.3(\text{syst.})\,\mathrm{n/m^{2}/day}and the fast neutron flux was estimated to be roughly4000​n/m2/day4000\,\mathrm{n/m^{2}/day}[66].
The cavernγ\gammaray flux has been measured in SNOLAB’s J-drift to be about4.25⋅104​γ/m2/s4.25\cdot 10^{4}\,\mathrm{\gamma/m^{2}/s}[59].

To determine the background rate introduced by cavernγ\gammarays and neutrons in ourGeant4simulation framework, we draw primary particle configurations from the known energy distributions of these particle species and start particle tracks from inside the cavern wall around the CUTE facility.
We simulated3⋅10123\cdot 10^{12}primaryγ\gammarays and10910^{9}primary neutrons.
Because of the CUTE facility’s extensive shielding, no hits were observed in any of the Si chips or Al cavities.
This null result yields a 90% C.L. upper limit on the expected background rate of<8.16⋅10−3​mHz<8.16\cdot 10^{-3}\,\mathrm{mHz}in a single Si chip or Al cavity, which breaks down into<8.14⋅10−3​mHz<8.14\cdot 10^{-3}\,\mathrm{mHz}fromγ\gammarays and<1.81⋅10−5​mHz<1.81\cdot 10^{-5}\,\mathrm{mHz}from neutrons.
Since these background rates are well below the rate from bulk contaminants, they are deemed negligible.

## 4Background projection results

This section summarizes the outcome of our background and calibration source simulation studies.
Table7reports the results of the previously discussed background categories and the composition of the estimated total background rate for one of the Si chips and one of the Al cavities.
The bulk material contaminants inferred from the assay results dominate, while the contribution of the interstitial air in the CUTE shield is negligible.
The assumptions made for the radon exposure leading to an excess of210Pb on the materials’ surfaces indicate that the accumulated210Pb activity may cause a rate on the same order of magnitude as the bulk contaminants for very thin volumes such as the Si chips, and an order of magnitude below the bulk contaminants for larger volumes like the Al cavities.
Because the emitted particles of the210Pb decay chain have rather low energies, their penetration power is poor, thus the210Pb contribution is crucial for thin volumes, but subdominant for thicker volumes.
In all cases, the expected rate introduced byγ\gammarays or neutrons emitted from the cavern rock is much lower than the intrinsic bulk contamination of the materials proving the efficiency of CUTE’s multilayered radiation shield.

Note that we omit the simulated bulk210Pb rates corresponding to the210Pb-specific HPGe assay results.
The relatively low sensitivity of the210Pb-specific assays provides low confidence in the measurements.
Instead, we infer the bulk210Pb contribution from the HPGe assays of the bottom part of the238U decay chain assuming secular equilibrium.
We also include the210Pb surface contamination from radon exposure as discussed in section3.5.Table 7:Summary of simulated background contributions. The total rate is composed of the four considered categories: bulk contaminants according to the assay results with210Pb in secular equilibrium with238U, interstitial air in the CUTE shield,210Pb accumulated on material surfaces due to radon exposure andγ\gammarays and neutrons emitted from the SNOLAB cavern rock.DetectorSi chipAl cavityTotal rate [mHz]6.98⋅10−16.98\cdot 10^{-1}8.85⋅1018.85\cdot 10^{1}Bulk [mHz]5.51⋅10−15.51\cdot 10^{-1}7.78⋅1017.78\cdot 10^{1}Interstitial air [mHz]1.39⋅10−31.39\cdot 10^{-3}4.55⋅10−14.55\cdot 10^{-1}Surface210Pb [mHz]1.37⋅10−11.37\cdot 10^{-1}1.02⋅1011.02\cdot 10^{1}Cavern rock [mHz]<8.16⋅10−3<8.16\cdot 10^{-3}<8.16⋅10−3<8.16\cdot 10^{-3}α\alpharate [mHz]1.55⋅10−11.55\cdot 10^{-1}2.53⋅1012.53\cdot 10^{1}β/γ\beta/\gammarate [mHz]5.52⋅10−15.52\cdot 10^{-1}5.82⋅1015.82\cdot 10^{1}NR rate [mHz]2.64⋅10−12.64\cdot 10^{-1}4.65⋅1014.65\cdot 10^{1}

The breakdown per particle type shows that while the contribution ofβ\betaparticles andγ\gammarays is higher than fromα\alphaparticles or NRs, all particle types are relevant.
The sum of the individual particle rates is larger than the total background rate, which indicates that some events are composed of more than one particle interaction type.

A discussion of the uncertainties of the background rates shown in table7and the fraction of upper limits contributing to the total rate can be found in appendixC.

## 4.1Spectral component analysis

In addition to characterizing the rate of ionizing radiation hits in the simulation, we are also interested in the energy spectrum of the expected background radiation field and its composition.
Figure5illustrates the spectrum observed by one of the Si chips for the simulated decays of the top part of the238U decay chain in the bulk of the Si substrate.Figure 5:Recorded spectrum of the top part of the238U decay chain simulated as bulk contamination in one of the Si chips. The combined spectrum of all particle hits (black) is broken down into different particle interaction types:α\alphaparticles (red),β/γ\beta/\gammaparticles (blue), nuclear recoils (green). The displacement between the full-energyα\alphapeaks in the combined spectrum compared to theα\alphaparticlespectrum is due to the separation of the nuclear recoil contribution.

The spectrum of all particles hits, grouped into topological events as discussed in section3.2, is dominated by the full-energy absorption ofα\alphaparticles emitted by the decays of238U (Qα=4270Q_{\alpha}=4270keV),234U (Qα=4858Q_{\alpha}=4858keV) and230Th (Qα=4770Q_{\alpha}=4770keV) following the decay sequence:U238​⟶𝛼​Th234​⟶β−​Pa234​⟶β−​U234​⟶𝛼​Th230​⟶𝛼​Ra226.{{}^{238}\text{U}}\overset{\alpha}{\longrightarrow}{{}^{234}\text{Th}}\overset{\beta^{-}}{\longrightarrow}{{}^{234}\text{Pa}}\overset{\beta^{-}}{\longrightarrow}{{}^{234}\text{U}}\overset{\alpha}{\longrightarrow}{{}^{230}\text{Th}}\overset{\alpha}{\longrightarrow}{{}^{226}\text{Ra}}.(4.1)

The highest-energy lines in the spectrum correspond to theα\alphadecays transitioning into the ground state of the progeny nuclides.
The line features are caused by the full-energy absorption ofα\alphaparticles carrying the kinetic energyEα=Qα−ENRE_{\alpha}=Q_{\alpha}-E_{\text{NR}}, withQαQ_{\alpha}being the energy released in the nuclear reaction (Q-value) andENRE_{\text{NR}}the kinetic energy transferred to the decay nucleus.
Additional lines at lower energies thanQαQ_{\alpha}are visible for transitions into excited states which involve the emission of discreteγ\gammarays and typically a lower decay probability than the ground state transition.

The endpoint of theβ/γ\beta/\gammacomponent of the spectrum agrees with the Q-value of theβ−\beta^{-}decay of234Pa (Qβ=2194Q_{\beta}=2194keV).
Because of the small size of the Si chip, there is a moderate chance for high-energyβ\betaelectrons to escape the Si substrate without depositing their full kinetic energy, which is why the recorded spectrum does not extend all the way to the Q-value of234Pa with the simulated statistics.
At lower energies, theβ/γ\beta/\gammaspectrum is a superposition of the twoβ−\beta^{-}decays present in the chain from234Pa and234Th (Qβ=274Q_{\beta}=274keV).

The energy range in between theα\alphapeaks and the endpoint of the combinedβ/γ\beta/\gammaspectrum is populated byα\alphaparticle hits that deposit only a fraction ofQαQ_{\alpha}.
Forα\alphadecays that are simulated close to the surface of the Si chip, theα\alphaparticle can escape the volume without depositing its full kinetic energy.
This partial energy deposit occurs for about 2.1% of the simulated events in this particular configuration.

In the energy range from 30 keV to 80 keV, characteristic X-ray andγ\gammalines are visible in theβ/γ\beta/\gammaspectrum.
Similarly, the energy spectrum of nuclear recoils shows distinct lines for the recoiling nuclei from the presentα\alphadecays of238U (ENR=70E_{\text{NR}}=70keV),234U (ENR=81E_{\text{NR}}=81keV) and230Th (ENR=81E_{\text{NR}}=81keV).
These discrete lines are not visible in the total spectrum of all particle hits because there are usually multiple hits of different particle types that get grouped into the same topological event characterized by the sum of all energy deposits withinΔ​t=15​μ\Delta t=15\,\mus (see section3.2).
Because of the separation of particle type interactions, theα\alphapeaks in theα\alphaspectrum appear at the kinetic energy of the emittedα\alphaparticlesEαE_{\alpha}while they appear atQα=Eα+ENRQ_{\alpha}=E_{\alpha}+E_{\text{NR}}in the total spectrum of all particle hits.

Based on the total rate estimates reported in table7, we do not expect significant contributions from external background radiation sources such as the SNOLAB rock cavern or from radon decays in the interstitial air inside the CUTE lead shield.
These contributions will henceforth be neglected.

Figure6depicts the projected total background spectrum in one of the Si chips for all the simulated radioisotopes arising from bulk and surface contaminants.
The total spectrum is broken down into particle type interactions following the single bulk contaminant example presented in figure5.
Each spectrum has been normalized to standardized decay rate units to report the simulated event rate in terms of counts per energy bin, device mass and live time.
The integral over the normalized spectra multiplied by the energy bin width of 20 keV, the device mass of 57 mg and conversion from days to seconds yields the background rates reported in table7.Figure 6:Projected total background spectrum of all simulated radioisotopes from bulk and surface contaminants for one of the Si chips. The total spectrum (black) is composed of all particle hit types whereas the other histograms show the contributions of specific particle type interactions:α\alphaparticles (red),β/γ\beta/\gammaparticles (blue), nuclear recoils (green). The spectral features are described in the text. Each spectrum has been normalized to decay rate units.

The same characteristic features as discussed for the example shown in figure5are present in the total background projection in figure6.
From the highest energies observed in the simulation down to about 1.5 MeV,α\alphadecays dominate the spectrum both in intensity and rate.
The highest-energy deposits are caused by a summation of two subsequentα\alphadecays within the235U decay chain (see also figure7):219Rn with the most probable emission ofEα=6819E_{\alpha}=6819keV and215Po withEα=7386E_{\alpha}=7386keV yield a summed energy ofEα=14205E_{\alpha}=14205keV.
This summation effect is a consequence of the split time windowΔ​t=15​μ\Delta t=15\,\mus applied in our processing of theGeant4events discussed in section3.2.
Because the half-life of215Po is only 1.78 ms, there is a small likelihood for this decay to occur withinΔ​t\Delta twith respect to the previous decay in the chain from219Rn.
The lowerα\alphapeaks in that high-energy region above 10 MeV are summation peaks involving less probable transitions into excited states of the progeny nuclei.
The flat region below the summation peak atEα=14205E_{\alpha}=14205keV and the highest singleα\alphadecay line atEα=8954E_{\alpha}=8954keV from212Po is caused by coincidentα\alphadecays in which one of the particles does not deposit its full energy in the substrate.

Another summation effect is visible in the total background spectrum with the sawtooth-like feature around 9 MeV.
This feature is attributed to the delayed coincidence decay of212Bi (Qβ=2252Q_{\beta}=2252keV) into212Po (Qα=8954Q_{\alpha}=8954keV) as part of the232Th decay chain.
The half-life of212Po is0.3​μ0.3\,\mus and much shorter thanΔ​t=15​μ\Delta t=15\,\mus resulting in a high chance of summing up the energy deposits from the discreteα\alphaparticle energy from the polonium decay and the continuousβ\betaspectrum of the bismuth isotope.
A similar decay sequence is found in the bottom part of the238U decay chain starting with214Bi (Qβ=3269Q_{\beta}=3269keV) which decays into214Po (Qα=7833.54Q_{\alpha}=7833.54keV).
The latter isotope214Po has a half-life of164​μ164\,\mus which is ten times longer thanΔ​t\Delta t, but still results in a summation feature visible in the238U bottom part spectrum in figure7.
However, in the total background spectrum the214Bi-214Po coincidence is subdominant.
The214Bi-214Po coincidence would be more prominent in the total spectrum for a much larger value of the split timeΔ​t\Delta t.

Below the lowest visibleα\alphadecay peak from232Th (Eα=3947E_{\alpha}=3947keV), degraded energy deposits byα\alphaparticles make up about 13% of the totalα\alphaparticle rate.
Theβ/γ\beta/\gammarate is dominated by theβ−\beta^{-}-decay of234Pa withQβ=2194Q_{\beta}=2194keV from the top part of the238U decay chain.
BelowQβQ_{\beta}of234Pa, the integratedβ/γ\beta/\gammarate is about forty times higher than the integrated rate over the same energy range in theα\alphaparticle spectrum.

Another breakdown of the total background spectrum is shown in figure7where the contributions of the individual radioisotopes and their decay chains are highlighted.
The main contributions arise from the bulk contamination with the primordial decay chain elements238U (lower energy range dominated by top part, mid energy range by bottom part),232Th (mid to high energy range) and235U (high energy range).
The spectrum of the bottom part of the238U chain clearly shows the214Bi-214Po summation feature around 8 MeV.
Another significant contribution arises from the210Pb surface contamination.
The remaining radioisotopes contribute roughly equally to the total spectrum at low energies.Figure 7:Isotopic composition of the total background projection for one of the Si chips. The total spectrum (gray filling) is the sum of the individual radioisotope spectra (colored histograms). Each spectrum has been normalized to decay rate units.

## 4.2Comparison to radioactive calibration sources

In addition to characterizing the ambient background radiation level for the QUTEbits project, we use the same simulation framework to study the prospects of using available calibration sources at CUTE to expose the quantum devices to a controlled level of ionizing radiation above the expected background level.
Similar studies using radioactive calibration sources were reported in Ref.[71,40]using a strong60Co source, in Ref.[21]using232Th and Ref.[24]using137Cs.

At CUTE there are calibration sources forγ\gammaray calibration using a133Ba source and neutron exposure using a252Cf source.
Both sources have a nominal activity of37.0±5.637.0\pm 5.6kBq, which has reduced to about 22.5 kBq for133Ba and to about 7.6 kBq for252Cf taking into account the half-lives and reference manufacturing dates of the sources for a projected date of use in April 2026.
More information on the CUTE calibration systems can be found in[19].

The estimate of the calibration source event rates follows analogously to the steps described in section3.
For the sources themselves, a source container assembly is placed at different positions in the geometry resembling CUTE’s calibration systems.
The inner volume of the source container is a sphere of 2 mm diameter which is contaminated with the radioisotope of interest to simulate the decay physics and particle tracking withGeant4.
The simulation output is then processed as described in section3.2with the distinction that we split the252Cf detector hits into electron recoils (ERs) and nuclear recoils (NRs) in order to separately assess the neutron induced event rate.

The CM shield surrounding the QUTEbits payload was designed in a way that allows rotation of the payload in steps of30∘30^{\circ}with respect to a fixed reference as illustrated in figure8for the133Ba source position.
In order to optimize the133Ba event rate in the Si chips, simulations were performed with varying rotation anglesαrot\alpha_{\text{rot}}while the source was aligned with the center of the Si chips in the same horizontal plane.
The resulting rates versus rotation angle are shown in figure9.
The uncertainty on the estimated event rates is dominated by the systematic uncertainty of the source activity which is reported as 15% of the nominal activity by the manufacturer.Figure 8:Geant4visualization of different rotations of the QUTEbits payload with respect to the133Ba source position (lower right). From left to right the rotations are referred to asαrot=90∘\alpha_{\text{rot}}=90^{\circ},180∘180^{\circ}and330∘330^{\circ}. The visualization only displays some of the geometry elements for better visibility.Figure 9:Simulated133Ba rates in both Si chips for different payload rotations. The highest event rates are achieved forαrot=90∘\alpha_{\text{rot}}=90^{\circ}andαrot=180∘\alpha_{\text{rot}}=180^{\circ}. The error bars take into account a source position uncertainty ofΔ​αrot=±5∘\Delta\alpha_{\text{rot}}=\pm 5^{\circ}and the combined statistical and systematical uncertainty on the rate extracted from theGeant4simulations and their normalization.

The highest event rates are obtained forαrot=90∘\alpha_{\text{rot}}=90^{\circ}(Si chip 2) andαrot=180∘\alpha_{\text{rot}}=180^{\circ}(Si chip 1), which is when the Si chips provide the largest effective solid angle coverage.
Likewise, rotation anglesαrot≥300∘\alpha_{\text{rot}}\geq 300^{\circ}expose the smallest effective cross-section resulting in the lowest133Ba event rate.
The difference in rate between the two Si chips is caused by the additional amount of material from the OQTO holders and their mounting in between the source and the Si chip facing away from the source.
The presence of the material between the Si chips and their small size also result in a very low coincident hit rate of about 0.03% of the recorded single detector hits for the highest133Ba rate positions.

In comparison to the expected133Ba rates, the simulated252Cf rates are much lower for the most favorable payload rotation.
Because the252Cf source is being deployed inside the water tank of CUTE, which is further out from the133Ba source position within the outer lead shield, there is a higher position uncertainty associated with its deployment.
A comparison of the expected calibration source event rates is presented in table8.

While the combined252Cf event rate, composed of roughly the same amount of NRs and ERs, turns out to be comparable to the total background projection (see table7), the133Ba event rates are expected to exceed the background level in all deployment scenarios.
For the highest133Ba rate deployment (αrot=90∘,180∘\alpha_{\text{rot}}=90^{\circ},180^{\circ}), the expected excess over background is about fifty times the projected background rate.
For the lowest rate deployment (αrot=300∘,330∘\alpha_{\text{rot}}=300^{\circ},330^{\circ}), the excess is expected to be about a factor of seven.Table 8:Comparison of simulated calibration source event rates for133Ba and252Cf in Si chip 1 for different payload rotations. The statistical uncertainties reflect the statistics of the hits achieved in theGeant4simulation. The systematic uncertainties are dominated by the uncertainty of the source activities. The results for the second Si chip are statistically equivalent.Source configurationEvent rate in Si chip [mHz]133Ba withαrot=90∘\alpha_{\text{rot}}=90^{\circ}13.8±0.2​(stat.)±2.5​(syst.)13.8\pm 0.2(\text{stat.})\pm 2.5(\text{syst.})133Ba withαrot=180∘\alpha_{\text{rot}}=180^{\circ}38.8±0.3​(stat.)±5.8​(syst.)38.8\pm 0.3(\text{stat.})\pm 5.8(\text{syst.})133Ba withαrot=330∘\alpha_{\text{rot}}=330^{\circ}5.0±0.1​(stat.)±0.7​(syst.)5.0\pm 0.1(\text{stat.})\pm 0.7(\text{syst.})252Cf ERs withαrot=90∘\alpha_{\text{rot}}=90^{\circ}0.5±0.1​(stat.)±0.2​(syst.)0.5\pm 0.1(\text{stat.})\pm 0.2(\text{syst.})252Cf NRs withαrot=90∘\alpha_{\text{rot}}=90^{\circ}0.4±0.1​(stat.)±0.2​(syst.)0.4\pm 0.1(\text{stat.})\pm 0.2(\text{syst.})252Cf combined0.9±0.1​(stat.)±0.3​(syst.)0.9\pm 0.1(\text{stat.})\pm 0.3(\text{syst.})

## 5Crystal dynamics simulations with G4CMP

TheGeant4Condensed Matter Physics (G4CMP) package[35]is a publicly available addition to theGeant4toolkit[4,10,11].
It provides the relevant solid-state physics to simulate the response of crystalline substrates to interactions of high-energy particles at cryogenic temperatures (T≪1T\ll 1K).

If sufficiently energetic particles interact in a semiconductor, they produce lattice vibrations (phonons) and electron-hole pairs (e-h+pairs).
Because of energy conservation, we can assume that the energy expended to generate the charge carriers is eventually deposited into the phonon energy system, in particular when the charge carriers recombine either in the bulk of the semiconductor or thin-film metal electrodes attached on the surface.
Following this assumption, the total phonon energy collected by the sensitive metal films, in our case superconducting Al, is a direct measure of the original particle’s energy deposit when interacting with the Si substrate.

G4CMP models the e-h+pair production from particle impacts in a variety of substrate materials including Si, the subsequent charge carrier transport, their recombination and induced production of acoustic phonons666G4CMP does not model optical phonons explicitly, because in cryogenic devices held at milikelvin temperatures, optical phonons immediately downconvert to lower-energy (acoustic) phonon modes[35]., as well as the resulting phonon dynamics.
Additionally, G4CMP comprises a set of generalized physics processes related to the production of Bogoliubov quasiparticles which result from the breaking of Cooper pairs in superconducting films (see Ref.[35]for more details).

In this section, we apply G4CMP to study the phonon and charge carrier dynamics in one of our QUTEbits chip designs with two main objectives.
The first is to inform the event processing of theGeant4-based background simulations by estimating the typical phonon energy collection time (see section5.1).
The second goal of this study is to make a connection between the composition of the total background spectrum and the potential of different particle types to cause individual qubit errors or a cluster of correlated errors across multiple qubits (see section5.2).

Both of these objectives can be targeted with a simplified approach that does not require an elaborate implementation of the complex quantum circuit layout as dedicatedGeant4geometry elements.
Instead, we split the one-sided chip layout provided by Chalmers University in the form of a GDS file into two layers: one representing the center lines of the quantum circuit layout covering about 8.2% of the surface and one representing the ground plane (see figure10).
Furthermore, we attach the two layers to the opposite faces of the Si chip in the simulation, with the top layer resembling the layout of the quantum circuitry and the bottom layer being a solid Al plane covering the entire substrate surface of7×77\times 7mm2.
With this approach, the total Al coverage of the chip is slightly increased compared to the original single-side layout.
However, because of the Monte Carlo nature of the particle tracking simulations, defining the Al mask in this way does not make a statistically significant difference for studying phenomena such as the localized phonon absorption probability and temporal characteristics of the phonon dynamics.

The planar circuit layout extracted from the GDS file gets converted into a 3D object through voxelization.
The voxel size is informed by the thickness of the Al film of 300 nm and the dimensions of the circuitry elements such as the transmission lines, 2D resonators and the width of the stripes forming the transmon crosses.
Different voxel sizes were explored and we found that cuboids of10×\times10×\times0.3μ\mum3provide a sufficient level of granularity to achieve the targeted fidelity of the geometry description for this study.
The advantage of this simplified approach over a more sophisticated geometry is its flexibility to allow reading in a variety of designs with the same framework and minimal coding work.
An apparent drawback, on the other hand, is the limited fidelity which may not satisfy the needs for more advanced characterization studies such as presented in Ref.[73,24].
We hope that our approach may spark new developments in the context of G4CMP and the QIS community with a shared long-term vision of exploring effective strategies for mitigating phonon-mediated quasiparticle poisoning in quantum systems.

The configuration of the material properties and interfaces for this study as well as viable downsample options available in G4CMP are described in appendixD.
All simulations discussed in the following were performed with GCPMP version V09-09-02 andGeant4-10.7.4.

Similar to the previously discussed radioactive source simulations, we record particle hits caused by the specific G4CMP particle types – acoustic phonons of different polarizations, drift charges representing e-h+pairs – incident on the sensitive Al planes.
For the top surface and side walls, the bare Si substrate acts as a diffuse mirror for phonons.
Charge carrier tracks that reach a surface are terminated and we do not model any other form of charge trapping.
When charge carriers are created, we allow for Fano fluctuations of the number of created e-h+pairs.
For a complete overview of the capabilities of G4CMP and configuration options see Ref.[35].
While the background studies discussed in section3do not take into account an energy threshold when calculating the projected background rates, in practice the Si bandgap ofεg=1.17\varepsilon_{g}=1.17eV (see table14in appendixD) acts as a lower bound for ionization to appear.
In the context of radioactive backgrounds,εg\varepsilon_{g}is a good approximation for a “no threshold” scenario.
For the anticipated G4CMP simulations, there is an additional energy threshold of2​ΔAl2\Delta_{\text{Al}}to be considered which is the minimum phonon energy required to break a Cooper pair in the superconducting Al film.
In our case, we only track phonons that carryEph≥2​ΔAlE_{\text{ph}}\geq 2\Delta_{\text{Al}}withΔAl=0.174\Delta_{\text{Al}}=0.174\,meV being our adopted value of the superconducting energy gap of bulk Al at 0 K (see table14).
It should be noted that for thin Al films, there is typically an increase ofΔAl\Delta_{\text{Al}}compared to bulk Al[25].
However, our film thickness of 300 nm is still in the regime that can be described by bulk Al properties (see also appendixD).

A summary of the performed G4CMP simulations is given in table9with details described in the following sections.
We investigated phonon-only simulations, starting with individual phonons as primary particles of varying energy, electron and nuclear recoils with varying number of charge carrier pairs, and finally high-energyβ\betaelectrons andα\alphaparticles up to multiple MeV of kinetic energy.
Considering all investigated energy scales, the crystal response to particle impacts was probed over nine orders of magnitude from𝒪​(1​meV)\mathcal{O}(1\,\text{meV})to𝒪​(1​MeV)\mathcal{O}(1\,\text{MeV}).Figure 10:Visualization of a G4CMP simulation with a phonon-only point source emitting single phonons ofEph=4E_{\text{ph}}=4\,meV at the center of a chip design with four transmon qubits (Q1 – Q4). Left: phonon hits collected by the Al layout on top of the Si chip resembling the quantum circuitry with a zoom-in on the central transmission line. Right: bottom view of the spatial hit distribution recorded by the planar backside of the chip. Both figures show the imprints of the characteristic phonon caustics pattern for (100) Si with a45∘45^{\circ}lattice rotation (see e.g.[35]for more details). Each hit coordinate has been weighted with the energy deposited by the phonon. In contrast, the response to a homogeneously distributed phonon contamination in the bulk would be completely uniform.

An example of a phonon-only simulation withEph=4E_{\text{ph}}=4meV is shown in figure10.
All particle types of interest were simulated with two different source configurations: 1) a point source at the center of the Si chip, and 2) a Si bulk contamination source.
The point source option was mainly used to optimize the G4CMP runtime (see appendixD) and perform general consistency checks such as observing the expected phonon caustics pattern for (100) Si as shown in figure10.
The phonon caustics would not be visible for higher phonon energies because the pattern gets washed out due to the stronger impact of phonon scattering and phonon downconversion processes such as the anharmonic decay of a high-energy phonon into two lower energy phonons in the crystal bulk.

With the bulk contamination source, points are sampled homogeneously in the Si substrate to start primary particles of the specified kinetic energy.
This approach is representative for the majority of the simulated background events, in particular the radioactive contaminants intrinsic to the Si chip undergoingβ\betaandα\alphadecays.

## 5.1Phonon energy collection time

The phonon energy collection time informs theGeant4particle hit processing discussed in section3.2.
In this work, we define it as the time it takes to collect all of the athermal phonons created in a particle interaction that are able to break Cooper pairs in the superconducting Al films.
In order to study the effect of different kinds of particle interactions and energy scales, we perform separate G4CMP simulations with a phonon-only bulk source, ER and NR-like energy deposits as well as full particle tracking simulations forβ\betaelectrons andα\alphaparticles.
Energy deposits by incident particles such asγ\gammarays or high-energyβ\betaelectrons will create a population of charge carriers without depositing energy via lattice vibrations (orprompt phonons).
These types of interactions are referred to as electron recoils (ERs).

The initial energetic charge carrier pairs ionize subsequent e-h+pairs in an energy cascade for which the total number of e-h+pairs pairs created isNeh=Er/εeh​(Er)N_{\text{eh}}=E_{r}/\varepsilon_{\text{eh}}(E_{r}), whereErE_{r}is the recoil energy deposited andεeh\varepsilon_{\text{eh}}is the average energy required to create one e-h+pair.
In G4CMP we assumeεeh=3.81\varepsilon_{\text{eh}}=3.81eV in Si to be constant but allow for Fano fluctuations of the number of charge carrier pairs.
Electrons drifting through the crystal can produce secondary phonons via intervalley scattering.
Both charge carrier species can also emit secondary phonons when they recombine at interface boundaries.
When recombination occurs, half of the Si bandgap energy (εg=1.17\varepsilon_{g}=1.17eV) is emitted via phonons at the Debye frequency ofωD=15\omega_{D}=15THz in Si (see table14).
All of these secondary phonons propagate diffusively and quickly transition to ballistic transport as the phonons downconvert in energy (see Ref.[35]for more details).

If an incident high-energy particle interacts primarily with the nucleus of an atom, such as neutrons causing nuclear recoils (NRs), the energy is split between e-h+pairs and prompt phonons.
The energy sharing between charge carriers and prompt phonons is determined by the so-called ionization yieldYY.
The ionization yield is a function of the recoil energy and can be expressed as the ratio of the ionization energy over the recoil energy.
It is generally assumed to be unity for ER-like interactions and smaller than unity for NR-like interactions following a widely accepted model developed by Lindhardet al.[45,61].
By default, we let G4CMP calculate the ionization yield according to the Lindhard theory based on the particle type and target material.
For our low-energy NR-like simulations, we fix it toY=0.1Y=0.1taking into consideration a recent measurement of the ionization yield in Si at recoil energies as low as 100 eV[8].
Forα\alphaparticles, the nature of the energy deposit depends on their kinetic energy and the mass of the target nuclei.
For lowα\alphaparticle energies of𝒪\mathcal{O}(1 keV) in Si, the interactions are NR-like with about 80% of the energy transferred into prompt phonons (Y=0.2Y=0.2).
At about 100 keV, the deposited energy is shared roughly equally between e-h+pairs and prompt phonons.
For typicalα\alphadecay energies in the range of 4 – 10 MeV, the interactions are ER-like with the ionization yield approaching close to unity (see table9).

For our G4CMP-based simulations, we evaluate the hit-time distribution of phonons that are absorbed by the Al sensor planes causing a G4CMP particle hit to find the mean and maximum phonon collection times,τ¯\overline{\tau}andτmax\tau_{\text{max}}, reported in table9.
The maximum collection time accounts for 99.9% of the total collected phonon energy per event.Table 9:Overview of G4CMP simulations for different particle interaction types and energy ranges. The Lindhard ionization yield,YY, is fixed to the reported values for the respective energy ranges except forα\alphaparticles for which G4CMP calculates a value for each energy. The uncertainties on the mean (τ¯\overline{\tau}) and maximum (τmax\tau_{\text{max}}) of the phonon energy collection time represent the standard deviation of the simulations performed for different energies of the primary particles.Primary particleEnergy rangeLindhardYYτ¯\overline{\tau}[μ\mus]τmax\tau_{\text{max}}[μ\mus]Phonon2 meV – 2 eV-1.2±0.21.2\pm 0.214.7±1.114.7\pm 1.1ER2 eV – 192 eV1.01.2±0.11.2\pm 0.115.9±1.615.9\pm 1.6NR2 eV – 192 eV0.11.3±0.11.3\pm 0.116.1±0.816.1\pm 0.8β\betaelectron1 keV – 3000 keV1.01.2±0.11.2\pm 0.116.7±2.616.7\pm 2.6α\alphaparticle1 keV – 8000 keV0.2 – 1.01.3±0.11.3\pm 0.116.0±2.416.0\pm 2.4

We find that the results forτ¯\overline{\tau}andτmax\tau_{\text{max}}are consistent across all particle interaction types and investigated energy ranges.
The first three cases (phonon-only, ER and NR) allow us to separate the contributions from the phonon and charge carrier propagation.
Using the same evaluation approach to determine the charge collection time reveals that the overall energy collection is dominated by the phonon propagation with the charge collection being about a factor of three faster.
On a similar note, the full particle tracking simulations withβ\betaelectrons andα\alphaparticles reveal that the primary particle energy is transferred into e-h+pairs via ionization and prompt phonons on timescales on the order of𝒪\mathcal{O}(10 ps), which is orders of magnitude faster than the typical phonon propagation.

The energy ranges for the different particle type interactions were chosen deliberately to cover the typical energies encountered in different background scenarios (see section4.1) with some overlap between the categories.
For theβ/α\beta/\alphasimulations, the energy deposits were downsampled to an appropriate energy scale that was inferred from the spatial phonon hit distribution analysis presented in the next section (see also appendixD).

Finally, it should be noted that the determined collection times strongly depend on the simulated chip geometry, its aspect ratio and assigned surface properties as well as the substrate material and its lattice orientation.
Moreover, we do not model any quasiparticle dynamics in the Al film beyond the version of Kaplan’s model of phonon-quasiparticle behavior implemented in G4CMP[35].
Because of that, the collection times do not include a contribution from quasiparticle diffusion in the superconducting films.
Future versions of G4CMP will include modeling of energy delocalization via quasiparticle diffusion, quasiparticle recombination and concomitant phonon emission777An extension adding the ability to track quasiparticles in superconducting films was implemented in G4CMP V10..

For the processing of theGeant4hits discussed in section3.2, we decided to use a split time ofΔ​t=15​μ\Delta t=15\,\mus informed by the determined values ofτmax\tau_{\text{max}}for the phonon-only simulations.
A simple interpretation of the determined phonon energy collection time can be made by relating the timescale to the lateral chip dimension and thickness using the speed of sound in Si ofvs=9.0​μv_{s}=9.0\,\mum/ns (see table14) to express the determined values ofτ¯\overline{\tau}andτmax\tau_{\text{max}}in terms of lateral (from side-to-side) or face-to-face phonon reflections.
The mean value ofτ¯=1.2​μ\overline{\tau}=1.2\,\mus (τmax=14.7​μ\tau_{\text{max}}=14.7\,\mus) corresponds to 21.6 (264) face-to-face or 1.5 (18.9) lateral reflections prior to absorption.

## 5.2Qubit hit multiplicity

The same set of G4CMP simulations evaluated in the previous section with a focus on the temporal crystal dynamics can be used to infer spatial characteristics such as the probability to disturb one or multiple qubits on the same substrate.
To first order, we assume that any phonon hit withEph≥2​ΔAlE_{\text{ph}}\geq 2\Delta_{\text{Al}}depositing energy in the qubit islands represented by the transmon crosses indicated in figure10would result in a loss of qubit coherence.
If the same occurs for multiple qubits on the same substrate simultaneously, it would be indicative of the rate of correlated qubit errors.

In this section, we present the results of the spatial hit evaluation of the simulations summarized in table9focusing on the qubit hit multiplicity.
We define the multiplicity asM∈[0,1,2,3,4]M\in[0,1,2,3,4]withM=1M=1meaning that one of the four transmon qubits recorded at least one phonon hit andM=4M=4that all qubits were hit in the same simulation event.
A simulation event is characterized by the maximum phonon collection time reported in table9.
To that extent, we analyze the phonon hit coordinates for all simulations and extract the qubit multiplicity per event.
Figure11illustrates the qubit hit multiplicities for the idealized G4CMP simulations with a bulk contamination source to create phonon-only, ER and NR events of increasing total energy deposits.(a)Phonon-only simulation.(b)Electron-recoil (ER) simulation.(c)Nuclear-recoil (NR) simulation.Figure 11:Simulated qubit hit multiplicities for different particle interaction types (11(a)–11(c)) modeled as uniform bulk contaminant sources. The color coding and values are indicative for the probability of a specific multiplicity to be observed by the 4-qubit chip design presented in figure10. For the phonon-only simulations with energy deposits higher than the Debye energy ofωD=62\omega_{D}=62\,meV in Si, multiple primary phonons are generated per event. The ER simulations were performed with an ionization yield ofY=1Y=1while the NR simulations were done withY=0.1Y=0.1.

The phonon-only simulations starting with a single phonon show a low likelihood to reachM>1M>1, whereas theM=1M=1probability increases roughly linearly with the phonon energy.
This linearity is a consequence of the increase in number of secondary phonons from the rapid anharmonic downconversion of the initial phonon which directly depends on the deposited recoil energy.
Above the Debye energy in Si (ωD=62\omega_{D}=62meV), multiple phonons are created initially which increases the chance for higher multiplicities to occur.

Above a total energy deposit of 2 eV, we enter the regime in which real particle interactions would produce e-h+pairs.
We simulate this case separately for ER-like (Y=1Y=1) and NR-like interactions (Y=0.1Y=0.1) with very similar results in terms of qubit multiplicities.
The same level of agreement is apparent for the highest simulated phonon-only energy deposit and the lowest ER and NR energies, respectively.
The observed agreement between the simulations is a strong supportive argument for our original assumption that the total phonon energy collected by the sensor planes is representative of the original particle’s energy deposit.
This statement even holds when considering differences in the ionization yield because the energy deposited into the crystal gets efficiently transferred into the phonon system eventually.
Moreover, we conclude that the rapid downconversion of high-energy phonons quickly erases the origin of the energy deposit leading to very similar temporal, spatial and energy distributions of the phonons incident on the sensor planes.

Another conclusion that can be drawn from the charge-carrier simulations is that above an energy scale of𝒪\mathcal{O}(100 eV), almost all events result in the maximum qubit multiplicity ofM=4≡M​4M=4\equiv M4.
Above this threshold, the energy deposit is large enough that the resulting secondary particles spread out over the entire volume of the simulated Si chip size regardless of the position of the primary energy deposit.
From this observation, we conclude that any point-like energy deposit above∼200\sim 200eV would potentially lead to catastrophic qubit errors regardless of the spatial separation of the qubit islands on the7×77\times 7mm2chip design.
Already at lower energy deposits of𝒪\mathcal{O}(10 eV), the likelihood of observing multiplicitiesM>1M>1dominates withM≥2M\geq 2events showing up in more than 90% of the energy deposits above 8 eV in our simulations.

As a final step, we evaluate our high-energyβ\betaelectron andα\alphaparticle simulations to determine representative average multiplicity fractionsM¯β\overline{M}_{\beta}andM¯α\overline{M}_{\alpha}, respectively.
Based on the results obtained with the ER and NR simulations, the energy deposits of theβ\betaelectrons andα\alphaparticles were downsampled to an equivalent energy deposit ofEr=200E_{r}=200\,eV (see appendixD).
We find that the multiplicity fractions determined for the energy ranges listed in table9are largely independent of the energy scale and higher energy simulations do not provide additional information.
However, we observe a small systematic difference betweenβ\betaelectrons andα\alphaparticles such thatM¯α​(M​4)≈100%\overline{M}_{\alpha}(M4)\approx 100\%while we findM¯β​(M​4)=(96.3±0.4)%\overline{M}_{\beta}(M4)=(96.3\pm 0.4)\%andM¯β​(M​3)=(3.8±0.3)%\overline{M}_{\beta}(M3)=(3.8\pm 0.3)\%forβ\betaelectrons.
For the latter values, we take the standard deviation of the average over the simulated energies as a measure of the uncertainty.
We attribute the difference to the softer phonon spectrum created by ER-like interactions and the larger initial volume over which e-h+pairs get produced, while the initialβ\betaelectron deposits its kinetic energy via ionization.
Another contribution could potentially be arising from the fact that we make use of a G4CMP hit-merging algorithm that groups together energy deposits that are closer together than a specified step size (see also appendixD).

Our findings demonstrate how Monte Carlo tools like G4CMP can be applied for simplified crystal dynamics studies to address questions relevant to the phenomenon of phonon-mediated quasiparticle poisoning in superconducting qubit devices.

## 6Conclusions

We have performed an extensive material screening campaign which informed design choices for the QUTEbits project.
The assay results serve as an input for sophisticated background projections based on radiation transport simulations withGeant4and crystal dynamics studies with G4CMP.
Because of their associated high uncertainties, we replaced the210Pb bulk material assays with the outcome of dedicated studies of the210Pb excess accumulated on material surfaces due to radon exposure, which turned out to be on the same order of magnitude as the contribution of bulk radioactivity to the overall background rate.

Our simulation studies predict a total background rate of less than 1 mHz per Si chip in CUTE and that we can control the radiation environment by switching from the low background rate of the ambient components to a fifty times higher rate by inserting a133Baγ\gammaray calibration source.
This feature will be of particular interest when measuring the coherence times of superconducting qubits in CUTE.
In fact, the same type of measurements will be repeated above ground at the University of Waterloo to provide an additional comparison between the impact of the radiation level on Earth’s surface and the ultra-low background environment at SNOLAB.

By performing dedicated G4CMP simulations, we determined the phonon energy collection time of our chip design to inform theGeant4particle hit processing.
The phonon collection time depends on the substrate dimensions, the material and its physical properties.
Because of that, simplified G4CMP studies could serve as a guide to identify quantum circuit layouts which might be better suited to suppress correlated errors, e.g. by mechanically isolating the qubit islands from the bulk of the substrate, placing and optimizing suitable phonon absorbers and exploring gap-engineered backside coatings to prevent phonon reflections and increase absorption.

Finally, we investigated how multiple qubits on the same substrate respond to different kinds of particle interaction types.
We interpret the occurrence of events with increasing qubit hit multiplicity as a measure of the projected rate of correlated errors between transmon qubits on the same chip.
It turned out that the probability to observe the maximal qubit multiplicity is fairly independent from the type of particle interaction.
Moreover, we found that energy deposits of𝒪\mathcal{O}(10 eV) have a high chance to cause correlated qubit errors even with mm-spaced qubit islands.
Above an energy threshold of𝒪\mathcal{O}(100 eV), we expect the entire
substrate volume to be affected by phonon hits regardless of the origin of the radiation hit impact.

By combining these findings and assuming linear scaling laws, we can make rough projections for quantum computing with fault-tolerant qubits when operated deep underground with a radiation shield comparable to CUTE.
For a benchmark quantum computer processor888Informed by the approximate dimensions of Google’s Willow quantum chip[2].based on a Si chip of 20×\times20×\times0.5 mm3(assuming the same substrate thickness as in our study), we can project a combined background rate of𝒪\mathcal{O}(10 mHz).
If we further assume that this is the rate of catastrophic errors which could not be mitigated by means of quantum error correction, it would limit the continuous algorithm execution time to𝒪\mathcal{O}(100 s).

We can compare this scenario to a typical surface laboratory environment with an unshielded dilution refrigerator at sea level (see e.g. table 6 in Ref.[47]).
The present background rates are dominated by cosmic-ray induced muons and ambientγ\gammarays from radioactive contaminants in the environment.
For the projected Si chip size of 20×\times20×\times0.5 mm3(0.47 g), the simulated interaction rates reported in Ref.[47]would correspond to 90–140 mHz from muon interactions and about 200 mHz from ambientγ\gammarays.
These background levels would limit the undisturbed quantum algorithm execution to a few seconds compared to the previously reported𝒪\mathcal{O}(100 s) for an operation in a well-shielded deep underground facility.

In the near future, the QUTEbits project will perform an advanced characterization of superconducting qubits deep underground at SNOLAB, focusing on measurements of coherence times, for which the performed assay and simulation studies provide an important foundation.

## Acknowledgments

The authors gratefully acknowledge SNOLAB and its staff for providing access to the CUTE facility and continued logistical and technical support of the QUTEbits project.
Moreover, the authors thank SNOLAB for performing extensive material screening measurements throughout the course of the project.
The authors would also like to thank the SuperCDMS collaboration for jointly collaborating on theirGeant4simulation framework.

This research was sponsored by the U.S. Army Research Office (ARO) and the
Laboratory for Physical Sciences (LPS).
It was accomplished under Award Number: W911NF-23-1-0338.
The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the Army Research Office or the U.S. Government.
The U.S. Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein.

This research was enabled in part by support provided by Compute Ontario (computeontario.ca) and the Digital Research Alliance of Canada (alliancecan.ca).

## References
- [1]202Q-lab Chalmers University(2026)OQTO sample holder.Note:https://github.com/202Q-lab/OQTOAccessed on March 24, 2026Cited by:§2.2,§3.1.
- [2]R. Acharya, D. A. Abanin, L. Aghababaie-Beni, I. Aleiner, T. I. Andersen, M. Ansmann, F. Arute, K. Arya, A. Asfaw, N. Astrakhantsev, J. Atalaya, R. Babbush, D. Bacon, B. Ballard, J. C. Bardin, J. Bausch, A. Bengtsson, A. Bilmes, S. Blackwell, S. Boixo, G. Bortoli, A. Bourassa, J. Bovaird, L. Brill, M. Broughton, D. A. Browne, B. Buchea, B. B. Buckley, D. A. Buell, T. Burger, B. Burkett, N. Bushnell, A. Cabrera, J. Campero, H. Chang, Y. Chen, Z. Chen, B. Chiaro, D. Chik, C. Chou, J. Claes, A. Y. Cleland, J. Cogan, R. Collins, P. Conner, W. Courtney, A. L. Crook, B. Curtin, S. Das, A. Davies, L. De Lorenzo, D. M. Debroy, S. Demura, M. Devoret, A. Di Paolo, P. Donohoe, I. Drozdov, A. Dunsworth, C. Earle, T. Edlich, A. Eickbusch, A. M. Elbag, M. Elzouka, C. Erickson, L. Faoro, E. Farhi, V. S. Ferreira, L. F. Burgos, E. Forati, A. G. Fowler, B. Foxen, S. Ganjam, G. Garcia, R. Gasca, É. Genois, W. Giang, C. Gidney, D. Gilboa, R. Gosula, A. G. Dau, D. Graumann, A. Greene, J. A. Gross, S. Habegger, J. Hall, M. C. Hamilton, M. Hansen, M. P. Harrigan, S. D. Harrington, F. J. H. Heras, S. Heslin, P. Heu, O. Higgott, G. Hill, J. Hilton, G. Holland, S. Hong, H. Huang, A. Huff, W. J. Huggins, L. B. Ioffe, S. V. Isakov, J. Iveland, E. Jeffrey, Z. Jiang, C. Jones, S. Jordan, C. Joshi, P. Juhas, D. Kafri, H. Kang, A. H. Karamlou, K. Kechedzhi, J. Kelly, T. Khaire, T. Khattar, M. Khezri, S. Kim, P. V. Klimov, A. R. Klots, B. Kobrin, P. Kohli, A. N. Korotkov, F. Kostritsa, R. Kothari, B. Kozlovskii, J. M. Kreikebaum, V. D. Kurilovich, N. Lacroix, D. Landhuis, T. Lange-Dei, B. W. Langley, P. Laptev, K. Lau, L. Le Guevel, J. Ledford, J. Lee, K. Lee, Y. D. Lensky, S. Leon, B. J. Lester, W. Y. Li, Y. Li, A. T. Lill, W. Liu, W. P. Livingston, A. Locharla, E. Lucero, D. Lundahl, A. Lunt, S. Madhuk, F. D. Malone, A. Maloney, S. Mandrà, J. Manyika, L. S. Martin, O. Martin, S. Martin, C. Maxfield, J. R. McClean, M. McEwen, S. Meeks, A. Megrant, X. Mi, K. C. Miao, A. Mieszala, R. Molavi, S. Molina, S. Montazeri, A. Morvan, R. Movassagh, W. Mruczkiewicz, O. Naaman, M. Neeley, C. Neill, A. Nersisyan, H. Neven, M. Newman, J. H. Ng, A. Nguyen, M. Nguyen, C. Ni, M. Y. Niu, T. E. O’Brien, W. D. Oliver, A. Opremcak, K. Ottosson, A. Petukhov, A. Pizzuto, J. Platt, R. Potter, O. Pritchard, L. P. Pryadko, C. Quintana, G. Ramachandran, M. J. Reagor, J. Redding, D. M. Rhodes, G. Roberts, E. Rosenberg, E. Rosenfeld, P. Roushan, N. C. Rubin, N. Saei, D. Sank, K. Sankaragomathi, K. J. Satzinger, H. F. Schurkus, C. Schuster, A. W. Senior, M. J. Shearn, A. Shorter, N. Shutty, V. Shvarts, S. Singh, V. Sivak, J. Skruzny, S. Small, V. Smelyanskiy, W. C. Smith, R. D. Somma, S. Springer, G. Sterling, D. Strain, J. Suchard, A. Szasz, A. Sztein, D. Thor, A. Torres, M. M. Torunbalci, A. Vaishnav, J. Vargas, S. Vdovichev, G. Vidal, B. Villalonga, C. V. Heidweiller, S. Waltman, S. X. Wang, B. Ware, K. Weber, T. Weidel, T. White, K. Wong, B. W. K. Woo, C. Xing, Z. J. Yao, P. Yeh, B. Ying, J. Yoo, N. Yosri, G. Young, A. Zalcman, Y. Zhang, N. Zhu, and N. Zobrist(2024-12)Quantum error correction below the surface code threshold.Nature638(8052),pp. 920–926.External Links:ISSN 1476-4687,Link,DocumentCited by:footnote 8.
- [3]R. Agnese, A. J. Anderson, T. Aramaki, I. Arnquist, W. Baker, D. Barker, R. Basu Thakur, D. A. Bauer, A. Borgland, M. A. Bowles, P. L. Brink, R. Bunker, B. Cabrera, D. O. Caldwell, R. Calkins, C. Cartaro, D. G. Cerdeño, H. Chagani, Y. Chen, J. Cooley, B. Cornell, P. Cushman, M. Daal, P. C. F. Di Stefano, T. Doughty, L. Esteban, S. Fallows, E. Figueroa-Feliciano, M. Fritts, G. Gerbier, M. Ghaith, G. L. Godfrey, S. R. Golwala, J. Hall, H. R. Harris, T. Hofer, D. Holmgren, Z. Hong, E. Hoppe, L. Hsu, M. E. Huber, V. Iyer, D. Jardin, A. Jastram, M. H. Kelsey, A. Kennedy, A. Kubik, N. A. Kurinsky, A. Leder, B. Loer, E. Lopez Asamar, P. Lukens, R. Mahapatra, V. Mandic, N. Mast, N. Mirabolfathi, R. A. Moffatt, J. D. Morales Mendoza, J. L. Orrell, S. M. Oser, K. Page, W. A. Page, R. Partridge, M. Pepin, A. Phipps, S. Poudel, M. Pyle, H. Qiu, W. Rau, P. Redl, A. Reisetter, A. Roberts, A. E. Robinson, H. E. Rogers, T. Saab, B. Sadoulet, J. Sander, K. Schneck, R. W. Schnee, B. Serfass, D. Speller, M. Stein, J. Street, H. A. Tanaka, D. Toback, R. Underwood, A. N. Villano, B. von Krosigk, B. Welliver, J. S. Wilson, D. H. Wright, S. Yellin, J. J. Yen, B. A. Young, X. Zhang, and X. Zhao(2017-04)Projected sensitivity of the SuperCDMS SNOLAB experiment.Phys. Rev. D95,pp. 082002.External Links:Document,LinkCited by:§1.
- [4]S. Agostinelli, J. Allison, K. Amako, J. Apostolakis, H. Araujo, P. Arce, M. Asai, D. Axen, S. Banerjee, G. Barrand, F. Behner, L. Bellagamba, J. Boudreau, L. Broglia, A. Brunengo, H. Burkhardt, S. Chauvie, J. Chuma, R. Chytracek, G. Cooperman, G. Cosmo, P. Degtyarenko, A. Dell’Acqua, G. Depaola, D. Dietrich, R. Enami, A. Feliciello, C. Ferguson, H. Fesefeldt, G. Folger, F. Foppiano, A. Forti, S. Garelli, S. Giani, R. Giannitrapani, D. Gibin, J.J. Gómez Cadenas, I. González, G. Gracia Abril, G. Greeniaus, W. Greiner, V. Grichine, A. Grossheim, S. Guatelli, P. Gumplinger, R. Hamatsu, K. Hashimoto, H. Hasui, A. Heikkinen, A. Howard, V. Ivanchenko, A. Johnson, F.W. Jones, J. Kallenbach, N. Kanaya, M. Kawabata, Y. Kawabata, M. Kawaguti, S. Kelner, P. Kent, A. Kimura, T. Kodama, R. Kokoulin, M. Kossov, H. Kurashige, E. Lamanna, T. Lampén, V. Lara, V. Lefebure, F. Lei, M. Liendl, W. Lockman, F. Longo, S. Magni, M. Maire, E. Medernach, K. Minamimoto, P. Mora de Freitas, Y. Morita, K. Murakami, M. Nagamatu, R. Nartallo, P. Nieminen, T. Nishimura, K. Ohtsubo, M. Okamura, S. O’Neale, Y. Oohata, K. Paech, J. Perl, A. Pfeiffer, M.G. Pia, F. Ranjard, A. Rybin, S. Sadilov, E. Di Salvo, G. Santin, T. Sasaki, N. Savvas, Y. Sawada, S. Scherer, S. Sei, V. Sirotenko, D. Smith, N. Starkov, H. Stoecker, J. Sulkimo, M. Takahata, S. Tanaka, E. Tcherniaev, E. Safai Tehrani, M. Tropeano, P. Truscott, H. Uno, L. Urban, P. Urban, M. Verderi, A. Walkden, W. Wander, H. Weber, J.P. Wellisch, T. Wenaus, D.C. Williams, D. Wright, T. Yamada, H. Yoshida, and D. Zschiesche(2003)Geant4 – a simulation toolkit.Nucl. Instrum. Methods Phys. Res. A506(3),pp. 250–303.External Links:ISSN 0168-9002,Document,LinkCited by:§1,§3,§5.
- [5]A. Aguilar-Arevalo, D. Amidei, D. Baxter, G. Cancelo, B.A. Cervantes Vergara, A.E. Chavarria, E. Darragh-Ford, J.C. D’Olivo, J. Estrada, F. Favela-Perez, R. Gaïor, Y. Guardincerri, T.W. Hossbach, B. Kilminster, I. Lawson, S.J. Lee, A. Letessier-Selvon, A. Matalon, P. Mitra, A. Piers, P. Privitera, K. Ramanathan, J. Da Rocha, Y. Sarkis, M. Settimo, R. Smida, R. Thomas, J. Tiffenberg, M. Traina, R. Vilar, and A.L. Virto(2021-06)Measurement of the bulk radioactive contamination of detector-grade silicon with DAMIC at SNOLAB.J. Instrum.16(06),pp. P06019.External Links:Document,LinkCited by:§2.3,§2.4.
- [6]A. Aguilar-Arevalo, D. Amidei, X. Bertou, D. Bole, M. Butner, G. Cancelo, A. C. Vázquez, A.E. Chavarria, J.R.T. d. M. Neto, S. Dixon, J.C. D’Olivo, J. Estrada, G. F. Moroni, K.P. H. Torres, F. Izraelevitch, A. Kavner, B. Kilminster, I. Lawson, J. Liao, M. López, J. Molina, G. Moreno-Granados, J. Pena, P. Privitera, Y. Sarkis, V. Scarpine, T. Schwarz, M. S. Haro, J. Tiffenberg, D. T. Machado, F. Trillaud, X. You, and J. Zhou(2015-08)Measurement of radioactive contamination in the high-resistivity silicon CCDs of the DAMIC experiment.J. Instrum.10(08),pp. P08014.External Links:Document,LinkCited by:§2.4.
- [7]B. Aharmim, S. N. Ahmed, T. C. Andersen, A. E. Anthony, N. Barros, E. W. Beier, A. Bellerive, B. Beltran, M. Bergevin, S. D. Biller, K. Boudjemline, M. G. Boulay, T. H. Burritt, B. Cai, Y. D. Chan, M. Chen, M. C. Chon, B. T. Cleveland, G. A. Cox-Mobrand, C. A. Currat, X. Dai, F. Dalnoki-Veress, H. Deng, J. Detwiler, P. J. Doe, R. S. Dosanjh, G. Doucas, P.-L. Drouin, F. A. Duncan, M. Dunford, S. R. Elliott, H. C. Evans, G. T. Ewan, J. Farine, H. Fergani, F. Fleurot, R. J. Ford, J. A. Formaggio, N. Gagnon, J. T. M. Goon, K. Graham, D. R. Grant, E. Guillian, S. Habib, R. L. Hahn, A. L. Hallin, E. D. Hallman, C. K. Hargrove, P. J. Harvey, R. Hazama, K. M. Heeger, W. J. Heintzelman, J. Heise, R. L. Helmer, R. J. Hemingway, R. Henning, A. Hime, C. Howard, M. A. Howe, M. Huang, B. Jamieson, N. A. Jelley, J. R. Klein, M. Kos, A. Krüger, C. Kraus, C. B. Krauss, T. Kutter, C. C. M. Kyba, R. Lange, J. Law, I. T. Lawson, K. T. Lesko, J. R. Leslie, I. Levine, J. C. Loach, S. Luoma, R. MacLellan, S. Majerus, H. B. Mak, J. Maneira, A. D. Marino, R. Martin, N. McCauley, A. B. McDonald, S. McGee, C. Mifflin, M. L. Miller, B. Monreal, J. Monroe, A. J. Noble, N. S. Oblath, C. E. Okada, H. M. O’Keeffe, Y. Opachich, G. D. O. Gann, S. M. Oser, R. A. Ott, S. J. M. Peeters, A. W. P. Poon, G. Prior, K. Rielage, B. C. Robertson, R. G. H. Robertson, E. Rollin, M. H. Schwendener, J. A. Secrest, S. R. Seibert, O. Simard, J. J. Simpson, D. Sinclair, P. Skensved, M. W. E. Smith, T. J. Sonley, T. D. Steiger, L. C. Stonehill, N. Tagg, G. Tešić, N. Tolich, T. Tsui, R. G. V. de Water, B. A. VanDevender, C. J. Virtue, D. Waller, C. E. Waltham, H. W. C. Tseung, D. L. Wark, P. Watson, J. Wendland, N. West, J. F. Wilkerson, J. R. Wilson, J. M. Wouters, A. Wright, M. Yeh, F. Zhang, and K. Zuber(2009-07)Measurement of the cosmic ray and neutrino-induced muon flux at the Sudbury neutrino observatory.Phys. Rev. D80,pp. 012001.External Links:Document,LinkCited by:§3.6.
- [8]M. F. Albakry, I. Alkhatib, D. Alonso, D. W. P. Amaral, T. Aralis, T. Aramaki, I. J. Arnquist, I. Ataee Langroudy, E. Azadbakht, S. Banik, C. Bathurst, R. Bhattacharyya, P. L. Brink, R. Bunker, B. Cabrera, R. Calkins, R. A. Cameron, C. Cartaro, D. G. Cerdeño, Y.-Y. Chang, M. Chaudhuri, R. Chen, N. Chott, J. Cooley, H. Coombes, J. Corbett, P. Cushman, S. Das, F. De Brienne, M. Rios, S. Dharani, M. L. di Vacri, M. D. Diamond, M. Elwan, E. Fascione, E. Figueroa-Feliciano, C. W. Fink, K. Fouts, M. Fritts, G. Gerbier, R. Germond, M. Ghaith, S. R. Golwala, J. Hall, S. A. S. Harms, N. Hassan, B. A. Hines, Z. Hong, E. W. Hoppe, L. Hsu, M. E. Huber, V. Iyer, V. K. S. Kashyap, M. H. Kelsey, A. Kubik, N. A. Kurinsky, M. Lee, M. Litke, J. Liu, Y. Liu, B. Loer, E. Lopez Asamar, P. Lukens, D. B. MacFarlane, R. Mahapatra, N. Mast, A. J. Mayer, H. Meyer zu Theenhausen, É. Michaud, E. Michielin, N. Mirabolfathi, B. Mohanty, B. Nebolsky, J. Nelson, H. Neog, V. Novati, J. L. Orrell, M. D. Osborne, S. M. Oser, W. A. Page, L. Pandey, S. Pandey, R. Partridge, D. S. Pedreros, L. Perna, R. Podviianiuk, F. Ponce, S. Poudel, A. Pradeep, M. Pyle, W. Rau, E. Reid, R. Ren, T. Reynolds, E. Tanner, A. Roberts, A. E. Robinson, T. Saab, D. Sadek, B. Sadoulet, S. P. Sahoo, I. Saikia, J. Sander, A. Sattari, B. Schmidt, R. W. Schnee, S. Scorza, B. Serfass, S. S. Poudel, D. J. Sincavage, P. Sinervo, Z. Speaks, J. Street, H. Sun, G. D. Terry, F. K. Thasrawala, D. Toback, R. Underwood, S. Verma, A. N. Villano, B. von Krosigk, S. L. Watkins, O. Wen, Z. Williams, M. J. Wilson, J. Winchell, K. Wykoff, S. Yellin, B. A. Young, T. C. Yu, B. Zatschler, S. Zatschler, A. Zaytsev, A. Zeolla, E. Zhang, L. Zheng, Y. Zheng, A. Zuniga, P. An, P. S. Barbeau, S. C. Hedges, L. Li, and J. Runge(2023-08)First Measurement of the Nuclear-Recoil Ionization Yield in Silicon at 100 eV.Phys. Rev. Lett.131,pp. 091801.External Links:Document,LinkCited by:§5.1.
- [9]M. F. Albakry, I. Alkhatib, D. Alonso-González, J. Anczarski, T. Aralis, T. Aramaki, A. A. Esfahani, I. A. Langroudy, R. Bhattacharyya, A. J. Biffl, P. L. Brink, M. Buchanan, R. Bunker, B. Cabrera, R. Calkins, R. A. Cameron, P. Camus, C. Cartaro, D. G. Cerdeño, Y. -Y. Chang, M. Chaudhuri, J. -H. Chen, R. Chen, J. Cooley, J. Corbett, P. Cushman, R. Cyna, S. Das, K. Dering, S. Dharani, M. L. di Vacri, M. D. Diamond, M. Elwan, S. Fallows, E. Figueroa-Feliciano, S. L. Franzen, G. Gerbier, R. Germond, A. Gevorgian, M. Ghaith, G. Godden, S. R. Golwala, G. Gonzalez, J. Hall, C. A. S. Harms, C. Hays, B. A. Hines, Z. Hong, L. Hsu, M. E. Huber, V. Iyer, M. Jha, V. K. S. Kashyap, M. H. Kelsey, K. T. Kennard, Z. Kromer, A. Kubik, N. A. Kurinsky, J. Leyva, J. Liu, Y. Liu, E. L. Asamar, P. Lukens, R. L. Noé, R. Mahapatra, J. S. Mammo, A. Mayer, P. C. McNamara, É. Michaud, E. Michielin, K. Mickelson, N. Mirabolfathi, M. Mirzakhani, B. Mohanty, D. Mondal, D. Monteiro, S. Nagorny, J. Nelson, H. Neog, H. Nguyen, J. L. Orrell, M. D. Osborne, S. M. Oser, P. Pakarha, L. Pandey, S. Pandey, R. Partridge, P. K. Patel, D. S. Pedreros, W. Peng, M. A. Penner, W. L. Perry, R. Podviianiuk, M. Potts, S. S. Poudel, A. Pradeep, M. Pyle, W. Rau, A. Rehberg, T. Reynolds, M. Rios, A. Roberts, A. E. Robinson, L. R. D. Rio, J. L. Ryan, T. Saab, D. Sadek, B. Sadoulet, S. Salehi, J. Sander, A. Sattari, R. W. Schnee, S. Scorza, B. Serfass, R. S. Shenoy, A. Simchony, P. Sinervo, Z. J. Smith, R. Soni, K. Stifter, M. Stukel, H. Sun, E. Tanner, N. Tenpas, D. Toback, R. Underwood, A. N. Villano, J. Viol, O. Wen, Z. Williams, M. J. Wilson, J. Winchell, J. Xiong, S. Yellin, B. A. Young, B. Zatschler, S. Zatschler, A. Zaytsev, E. Zhang, J. Zheng, L. Zheng, A. Zuniga, and M. J. Zurowski(2026-06)Calibration and Performance of Germanium High Voltage Detectors for SuperCDMS SNOLAB.arXiv pre-print.External Links:2606.26391,LinkCited by:§1.
- [10]J. Allison, K. Amako, J. Apostolakis, H. Araujo, P. Arce Dubois, M. Asai, G. Barrand, R. Capra, S. Chauvie, R. Chytracek, G.A.P. Cirrone, G. Cooperman, G. Cosmo, G. Cuttone, G.G. Daquino, M. Donszelmann, M. Dressel, G. Folger, F. Foppiano, J. Generowicz, V. Grichine, S. Guatelli, P. Gumplinger, A. Heikkinen, I. Hrivnacova, A. Howard, S. Incerti, V. Ivanchenko, T. Johnson, F. Jones, T. Koi, R. Kokoulin, M. Kossov, H. Kurashige, V. Lara, S. Larsson, F. Lei, O. Link, F. Longo, M. Maire, A. Mantero, B. Mascialino, I. McLaren, P. Mendez Lorenzo, K. Minamimoto, K. Murakami, P. Nieminen, L. Pandola, S. Parlati, L. Peralta, J. Perl, A. Pfeiffer, M.G. Pia, A. Ribon, P. Rodrigues, G. Russo, S. Sadilov, G. Santin, T. Sasaki, D. Smith, N. Starkov, S. Tanaka, E. Tcherniaev, B. Tome, A. Trindade, P. Truscott, L. Urban, M. Verderi, A. Walkden, J.P. Wellisch, D.C. Williams, D. Wright, and H. Yoshida(2006)Geant4 developments and applications.IEEE Trans. Nucl. Sci.53(1),pp. 270–278.External Links:DocumentCited by:§1,§3,§5.
- [11]J. Allison, K. Amako, J. Apostolakis, P. Arce, M. Asai, T. Aso, E. Bagli, A. Bagulya, S. Banerjee, G. Barrand, B.R. Beck, A.G. Bogdanov, D. Brandt, J.M.C. Brown, H. Burkhardt, Ph. Canal, D. Cano-Ott, S. Chauvie, K. Cho, G.A.P. Cirrone, G. Cooperman, M.A. Cortés-Giraldo, G. Cosmo, G. Cuttone, G. Depaola, L. Desorgher, X. Dong, A. Dotti, V.D. Elvira, G. Folger, Z. Francis, A. Galoyan, L. Garnier, M. Gayer, K.L. Genser, V.M. Grichine, S. Guatelli, P. Guèye, P. Gumplinger, A.S. Howard, I. Hřivnáčová, S. Hwang, S. Incerti, A. Ivanchenko, V.N. Ivanchenko, F.W. Jones, S.Y. Jun, P. Kaitaniemi, N. Karakatsanis, M. Karamitros, M. Kelsey, A. Kimura, T. Koi, H. Kurashige, A. Lechner, S.B. Lee, F. Longo, M. Maire, D. Mancusi, A. Mantero, E. Mendoza, B. Morgan, K. Murakami, T. Nikitina, L. Pandola, P. Paprocki, J. Perl, I. Petrović, M.G. Pia, W. Pokorski, J.M. Quesada, M. Raine, M.A. Reis, A. Ribon, A. Ristić Fira, F. Romano, G. Russo, G. Santin, T. Sasaki, D. Sawkey, J.I. Shin, I.I. Strakovsky, A. Taborda, S. Tanaka, B. Tomé, T. Toshito, H.N. Tran, P.R. Truscott, L. Urban, V. Uzhinsky, J.M. Verbeke, M. Verderi, B.L. Wendt, H. Wenzel, D.H. Wright, D.M. Wright, T. Yamashita, J. Yarba, and H. Yoshida(2016)Recent developments in Geant4.Nucl. Instrum. Methods Phys. Res. A835,pp. 186–225.External Links:ISSN 0168-9002,Document,LinkCited by:§1,§3,§5.
- [12]A. Blais, J. Gambetta, A. Wallraff, D. I. Schuster, S. M. Girvin, M. H. Devoret, and R. J. Schoelkopf(2007-03)Quantum-information processing with circuit quantum electrodynamics.Phys. Rev. A75,pp. 032329.External Links:Document,LinkCited by:§1.
- [13]A. Blais, A. L. Grimsmo, S. M. Girvin, and A. Wallraff(2021-05)Circuit quantum electrodynamics.Rev. Mod. Phys.93,pp. 025005.External Links:Document,LinkCited by:§1.
- [14]A. Blais, R. Huang, A. Wallraff, S. M. Girvin, and R. J. Schoelkopf(2004-06)Cavity quantum electrodynamics for superconducting electrical circuits: an architecture for quantum computation.Phys. Rev. A69,pp. 062320.External Links:Document,LinkCited by:§1.
- [15]G. Bratrud, S. Lewis, K. Anyang, A. C. Cesaní, T. Dyson, H. Magoon, D. Sabhari, G. Spahn, G. Wagner, R. Gualtieri, N. A. Kurinsky, R. Linehan, R. McDermott, S. Sussman, D. J. Temples, S. Uemura, C. Bathurst, G. Cancelo, R. Chen, A. Chou, I. Hernandez, M. Hollister, L. Hsu, C. James, K. Kennard, R. Khatiwada, P. Lukens, V. Novati, N. Raha, S. Ray, R. Ren, A. Rodriguez, B. Schmidt, K. Stifter, J. Yu, D. Baxter, E. Figueroa-Feliciano, and D. Bowring(2025)Measurement of correlated charge noise in superconducting qubits at an underground facility.Nat. Commun.16.External Links:DocumentCited by:§1,§1.
- [16]R. Brun and F. Rademakers(1997)ROOT: An object oriented data analysis framework.Nucl. Instrum. Methods Phys. Res. A389,pp. 81–86.External Links:DocumentCited by:§3.2.
- [17]R. Bunker, T. Aramaki, I.J. Arnquist, R. Calkins, J. Cooley, E.W. Hoppe, J.L. Orrell, and K.S. Thommasson(2020)Evaluation and mitigation of trace 210Pb contamination on copper surfaces.Nucl. Instrum. Methods Phys. Res. A967,pp. 163870.External Links:ISSN 0168-9002,Document,LinkCited by:§2.
- [18]D. O. Caldwell, B. Magnusson, M. S. Witherell, A. Da Silva, B. Sadoulet, C. Cork, F. S. Goulding, D. A. Landis, N. W. Madden, R. H. Pehl, A. R. Smith, G. Gerbier, E. Lesquoy, J. Rich, M. Spiro, C. Tao, D. Yvon, and S. Zylberajch(1990-09)Searching for the cosmion by scattering in Si detectors.Phys. Rev. Lett.65,pp. 1305–1308.External Links:Document,LinkCited by:§2.4.
- [19]P. Camus, J. Corbett, S. Crawford, K. Dering, E. Fascione, G. Gerbier, R. Germond, M. Ghaith, J. Hall, Z. Hong, A. Kubik, A. Mayer, S. Nagorny, P. Pakarha, W. Rau, S. Scorza, and R. Underwood(2023)CUTE: A Cryogenic Underground TEst facility at SNOLAB.Front. Phys.11.External Links:Document,2310.07930,ISSN 2296424XCited by:§1,§3.1,§3.4,§3.5,§3,§4.2.
- [20]L. Cardani, I. Colantoni, A. Cruciani, F. De Dominicis, G. D’Imperio, M. Laubenstein, A. Mariani, L. Pagnanini, S. Pirro, C. Tomei, N. Casali, F. Ferroni, D. Frolov, L. Gironi, A. Grassellino, M. Junker, C. Kopas, E. Lachman, C. R.H. McRae, J. Mutus, M. Nastasi, D. P. Pappas, R. Pilipenko, M. Sisti, V. Pettinacci, A. Romanenko, D. Van Zanten, M. Vignati, J. D. Withrow, and N. Z. Zhelev(2023)Disentangling the sources of ionizing radiation in superconducting qubits.Eur. Phys. J. C83(1).External Links:Document,2211.13597,ISSN 14346052Cited by:§1.
- [21]L. Cardani, F. Valenti, N. Casali, G. Catelani, T. Charpentier, M. Clemenza, I. Colantoni, A. Cruciani, G. D’Imperio, L. Gironi, L. Grünhaupt, D. Gusenkova, F. Henriques, M. Lagoin, M. Martinez, G. Pettinari, C. Rusconi, O. Sander, C. Tomei, A. V. Ustinov, M. Weber, W. Wernsdorfer, M. Vignati, S. Pirro, and I. M. Pop(2021)Reducing the impact of radioactivity on quantum circuits in a deep-underground facility.Nat. Commun.12(1).External Links:Document,2005.02286,ISSN 20411723Cited by:§1,§1,§4.2.
- [22]G. Casagranda, E. Auden, C. Cazzaniga, M. Kastriotou, C. Frost, M. Vallero, F. Vella, and P. Rech(2025-08)SQUID G.A.M.E.: Gamma, Atmospheric, and Mono-Energetic Neutron Effects on Quantum Devices.arXiv pre-print.External Links:2508.06362Cited by:§1.
- [23]G. Casagranda, M. Vallero, F. Vella, and P. Rech(2025)Understanding the Contributions of Terrestrial Radiation Sources to Error Rates in Quantum Devices.IEEE Trans. Nucl. Sci.72(4),pp. 1324–1334.External Links:DocumentCited by:§1.
- [24]E. Celi, R. Linehan, P. M. Harrington, M. Li, H. D. Pinckney, K. Serniak, W. D. Oliver, J. A. Formaggio, E. Figueroa-Feliciano, and D. Baxter(2026)Measuring quasiparticle dynamics for particle impact reconstruction in a superconducting qubit chip.arXiv pre-print.External Links:2604.13176Cited by:§1,§4.2,§5.
- [25]N. A. Court, A. J. Ferguson, and R. G. Clark(2007-11)Energy gap measurement of nanostructured aluminium thin films for single Cooper-pair devices.Supercond. Sci. Technol.21(1),pp. 015013.External Links:Document,LinkCited by:§5.
- [26]M.L. di Vacri, I.J. Arnquist, S. Scorza, E.W. Hoppe, and J. Hall(2021)Direct method for the quantitative analysis of surface contamination on ultra-low background materials from exposure to dust.Nucl. Instrum. Methods Phys. Res. A994,pp. 165051.External Links:ISSN 0168-9002,Document,LinkCited by:§2.
- [27]F. Duncan, A.J. Noble, and D. Sinclair(2010)The Construction and Anticipated Science of SNOLAB.Annu. Rev. Nucl. Part. Sci.60(Volume 60, 2010),pp. 163–180.External Links:Document,Link,ISSN 1545-4134Cited by:§1.
- [28]G. J. Feldman and R. D. Cousins(1998-04)Unified approach to the classical statistical analysis of small signals.Phys. Rev. D57,pp. 3873–3889.External Links:Document,LinkCited by:§3.3.
- [29]A. G. Fowler, M. Mariantoni, J. M. Martinis, and A. N. Cleland(2012-09)Surface codes: Towards practical large-scale quantum computation.Phys. Rev. A86,pp. 032324.External Links:Document,LinkCited by:§1.
- [30]X. Gu, A. F. Kockum, A. Miranowicz, Y. Liu, and F. Nori(2017)Microwave photonics with superconducting quantum circuits.Phys. Rep.718-719,pp. 1–102.Note:Microwave photonics with superconducting quantum circuitsExternal Links:ISSN 0370-1573,Document,LinkCited by:§1.
- [31]P. M. Harrington, M. Li, M. Hays, W. Van De Pontseele, D. Mayer, H. D. Pinckney, F. Contipelli, M. Gingras, B. M. Niedzielski, H. Stickler, J. L. Yoder, M. E. Schwartz, J. A. Grover, K. Serniak, W. D. Oliver, and J. A. Formaggio(2025)Synchronous detection of cosmic rays and correlated errors in superconducting qubit arrays.Nat. Commun.16(1).External Links:Document,2402.03208,ISSN 20411723Cited by:§1.
- [32]S. Hauf, M. Kuster, M. Batic, Z. W. Bell, D. H. H. Hoffmann, P. M. Lang, S. Neff, M. G. Pia, G. Weidenspointner, and A. Zoglauer(2013-08)Radioactive Decays in Geant4.IEEE Trans. Nucl. Sci.60(4),pp. 2966–2983.External Links:Document,ISSN 0018-9499,LinkCited by:§3.
- [33]S. Hauf, M. Kuster, M. Batic, Z. W. Bell, D. H. H. Hoffmann, P. M. Lang, S. Neff, M. G. Pia, G. Weidenspointner, and A. Zoglauer(2013-08)Validation of Geant4-Based Radioactive Decay Simulation.IEEE Trans. Nucl. Sci.60(4),pp. 2984–2997.External Links:Document,ISSN 0018-9499,LinkCited by:§3.
- [34]W. Jacobi(1972)Activity and potential alpha-energy of 222 radon-and 220 radon-daughters in different air atmospheres.Health Phys.22 5,pp. 441–50.External Links:Document,LinkCited by:§3.5.
- [35]M.H. Kelsey, R. Agnese, Y.F. Alam, I. A. Langroudy, E. Azadbakht, D. Brandt, R. Bunker, B. Cabrera, Y.-Y. Chang, H. Coombes, R.M. Cormier, M.D. Diamond, E.R. Edwards, E. Figueroa-Feliciano, J. Gao, P.M. Harrington, Z. Hong, M. Hui, N.A. Kurinsky, R.E. Lawrence, B. Loer, M.G. Masten, E. Michaud, E. Michielin, J. Miller, V. Novati, N.S. Oblath, J.L. Orrell, W.L. Perry, P. Redl, T. Reynolds, T. Saab, B. Sadoulet, K. Serniak, J. Singh, Z. Speaks, C. Stanford, J.R. Stevens, J. Strube, D. Toback, J.N. Ullom, B.A. VanDevender, M.R. Vissers, M.J. Wilson, J.S. Wilson, B. Zatschler, and S. Zatschler(2023)G4CMP: Condensed matter physics simulation using the Geant4 toolkit.Nucl. Instrum. Methods Phys. Res. A1055,pp. 168473.External Links:ISSN 0168-9002,Document,LinkCited by:Table 14,Table 14,Table 14,Table 14,Table 14,Table 14,Table 14,Table 14,Table 14,Table 14,Appendix D,Appendix D,Appendix D,§1,§3.2,Figure 10,Figure 10,§5.1,§5.1,§5,§5,§5,footnote 6.
- [36]K. Kennard, A. Pradeep, M. Buchanan, H. Fu, A. Simchony, Q. Wang, E. Michielin, T. Aralis, E. Cudmore, P. Cushman, M. Diamond, E. Figueroa-Feliciano, C. Fink, S. Harms, B. A. Hines, Z. Hong, M. E. Huber, A. Kubik, N. Kurinsky, R. Mahapatra, V. Novati, L. Pandey, P. K. Patel, W. Peng, M. Platt, R. Pressman-Cyna, W. Rau, R. Ren, T. Reynolds, J. Ryan, T. Saab, D. Sadek, B. Schmidt, Z. Smith, S. Stevens, K. Stifter, M. Stukel, J. Viol, Y. Wang, M. J. Wilson, B. A. Young, S. Zatschler, H. Zenger, and A. Zuñiga-Reyes(2026)Performance of a SuperCDMS HVeV detector with Sub-eV energy resolution and single charge-sensitivity.Nucl. Instrum. Methods Phys. Res. A1091,pp. 171753.External Links:ISSN 0168-9002,Document,LinkCited by:§1.
- [37]M. Kjaergaard, M. E. Schwartz, J. Braumüller, P. Krantz, J. I.-J. Wang, S. Gustavsson, and W. D. Oliver(2020)Superconducting Qubits: Current State of Play.Annu. Rev. Condens. Matter Phys.11(Volume 11, 2020),pp. 369–395.External Links:Document,Link,ISSN 1947-5462Cited by:§1,§1.
- [38]R. Klesse and S. Frank(2005-11)Quantum Error Correction in Spatially Correlated Quantum Noise.Phys. Rev. Lett.95,pp. 230503.External Links:Document,LinkCited by:§1.
- [39]J. Koch, T. M. Yu, J. Gambetta, A. A. Houck, D. I. Schuster, J. Majer, A. Blais, M. H. Devoret, S. M. Girvin, and R. J. Schoelkopf(2007-10)Charge-insensitive qubit design derived from the Cooper pair box.Phys. Rev. A76,pp. 042319.External Links:Document,LinkCited by:§1.
- [40]C. P. Larson, E. Yelton, K. Dodge, K. Okubo, J. Batarekh, V. Iaia, N. A. Kurinsky, and B. L. T. Plourde(2025-03)Quasiparticle poisoning of superconducting qubits with active gamma irradiation.PRX Quantum.External Links:Document,2503.07354,ISSN 2691-3399,LinkCited by:§1,§4.2.
- [41]M. Laubenstein and G. Heusser(2009)Cosmogenic radionuclides in metals as indicator for sea level exposure history.Appl. Radiat. Isot.67(5),pp. 750–754.Note:5th International Conference on Radionuclide Metrology - Low-Level Radioactivity Measurement Techniques ICRM-LLRMT’08External Links:ISSN 0969-8043,Document,LinkCited by:§2.4,§2.4,§2.
- [42]I. Lawson(2020-01)Low Background Measurement Capabilities at SNOLAB.J. Phys.: Conf. Ser.1342(1),pp. 012086.External Links:Document,LinkCited by:§2.1.
- [43]I. Lawson(2023-12)Low Background Measurement Program at SNOLAB.InProceedings of XVIII International Conference on Topics in Astroparticle and Underground Physics — PoS(TAUP2023),External Links:Document,LinkCited by:§2.1,§3.4,§3.5.
- [44]X. Li, J. Wang, Y. Jiang, G. Xue, X. Cai, J. Zhou, M. Gong, Z. Liu, S. Zheng, D. Ma, M. Chen, W. Sun, S. Yang, F. Yan, Y. Jin, S. P. Zhao, X. Ding, and H. Yu(2025)Cosmic-ray-induced correlated errors in superconducting qubit array.Nat. Commun.16.External Links:DocumentCited by:§1.
- [45]J. Lindhard, V. Nielsen, M. Scharff, and P. V. Thomsen(1963-01)Integral equations governing radiation effects.Kgl. Danske Videnskab., Selskab. Mat. Fys. Medd.Vol: 33: No. 10.External Links:LinkCited by:§5.1.
- [46]J.C. Loach, J. Cooley, G.A. Cox, Z. Li, K.D. Nguyen, and A.W.P. Poon(2016-12)A database for storing the results of material radiopurity measurements.Nucl. Instrum. Methods Phys. Res. A839,pp. 6–11.External Links:Document,ISSN 01689002,LinkCited by:§2.2.
- [47]B. Loer, P. M. Harrington, B. Archambault, E. Fuller, B. Pierson, I. J. Arnquist, K. Harouaka, T. D. Schlieder, D. K. Kim, A. J. Melville, B. M. Niedzielski, J. Yoder, K. Serniak, W. D. Oliver, J. L. Orrell, R. Bunker, B. A. VanDevender, and M. Warner(2024)Abatement of ionizing radiation for superconducting quantum devices.J. Instrum.19(9).External Links:Document,2403.01032,ISSN 17480221Cited by:§1,§6.
- [48]S. Majidy, C. Wilson, and R. Laflamme(2024)Building Quantum Computers: A Practical Introduction.Cambridge University Press.Cited by:§1.
- [49]J. M. Martinis(2021)Saving superconducting quantum processors from decay and correlated errors generated by gamma and cosmic rays.Npj Quantum Inf.7,pp. 90.External Links:2012.06137,DocumentCited by:§1.
- [50]M. McEwen, L. Faoro, K. Arya, A. Dunsworth, T. Huang, S. Kim, B. Burkett, A. Fowler, F. Arute, J. C. Bardin, A. Bengtsson, A. Bilmes, B. B. Buckley, N. Bushnell, Z. Chen, R. Collins, S. Demura, A. R. Derk, C. Erickson, M. Giustina, S. D. Harrington, S. Hong, E. Jeffrey, J. Kelly, P. V. Klimov, F. Kostritsa, P. Laptev, A. Locharla, X. Mi, K. C. Miao, S. Montazeri, J. Mutus, O. Naaman, M. Neeley, C. Neill, A. Opremcak, C. Quintana, N. Redd, P. Roushan, D. Sank, K. J. Satzinger, V. Shvarts, T. White, Z. J. Yao, P. Yeh, J. Yoo, Y. Chen, V. Smelyanskiy, J. M. Martinis, H. Neven, A. Megrant, L. Ioffe, and R. Barends(2022-01)Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits.Nat. Phys.18(1),pp. 107–111.External Links:Document,2104.05219Cited by:§1.
- [51]M. H. Mendenhall and R. A. Weller(2005)An algorithm for computing screened Coulomb scattering in Geant4.Nucl. Instrum. Methods Phys. Res. B227(3),pp. 420–430.External Links:ISSN 0168-583X,Document,LinkCited by:§3.5.
- [52]M. V. Moghaddam, C. W. S. Chang, I. Nsanzineza, A. M. Vadiraj, and C. M. Wilson(2019-11)Carbon nanotube-based lossy transmission line filter for superconducting qubit measurements.Appl. Phys. Lett.115(21),pp. 213504.External Links:ISSN 0003-6951,Document,LinkCited by:Appendix A.
- [53]A. Nero(2008)Indoor radon and its decay products: concentrations, causes, and control strategies.Lawrence Berkeley National Laboratory.External Links:LinkCited by:§3.5,§3.5.
- [54]W. D. Oliver and P. B. Welander(2013)Materials in superconducting quantum bits.MRS Bull.38,pp. 816–825.External Links:DocumentCited by:§1.
- [55]J. L. Orrell, I. J. Arnquist, M. Bliss, R. Bunker, and Z. S. Finch(2018)Naturally occurring 32Si and low-background silicon dark matter detectors.Astropart. Phys.99,pp. 9–20.External Links:ISSN 0927-6505,Document,LinkCited by:§2.4.
- [56]V. Pěč, V. A. Kudryavtsev, H. M. Araújo, and T. J. Sumner(2024)Muon-induced background in a next-generation dark matter experiment based on liquid xenon.Eur. Phys. J. C84(5).External Links:Document,ISSN 14346052Cited by:§1.
- [57]M. J. Persky(1999-05)Review of black surfaces for space-borne infrared systems.Rev. Sci. Instrum.70(5),pp. 2193–2217.External Links:ISSN 0034-6748,Document,LinkCited by:§2.3.
- [58]P. Redl(2014)Accurate Simulations of Pb Recoils in SuperCDMS.J. Low Temp. Phys.176,pp. 937–942.External Links:ISSN 0168-583X,DocumentCited by:§3.5.
- [59]A. E. Robinson(2015)Dark matter limits from a 2l c3f8 filled bubble chamber.Ph.D. Thesis,University of Chicago.Cited by:§3.6.
- [60]T. E. Roth, R. Ma, and W. C. Chew(2023)The transmon qubit for electromagnetics engineers: an introduction.IEEE Antennas Propag. Mag.65(2),pp. 8–20.External Links:DocumentCited by:§1,§1.
- [61]Y. Sarkis, A. Aguilar-Arevalo, and J. C. D’Olivo(2020-05)Study of the ionization efficiency for nuclear recoils in pure crystals.Phys. Rev. D101,pp. 102001.External Links:Document,LinkCited by:§5.1.
- [62]K. Serniak, M. Hays, G. de Lange, S. Diamond, S. Shankar, L. D. Burkhart, L. Frunzio, M. Houzet, and M. H. Devoret(2018-10)Hot Nonequilibrium Quasiparticles in Transmon Qubits.Phys. Rev. Lett.121(15),pp. 157701.External Links:Document,ISSN 0031-9007,LinkCited by:§1.
- [63]P. W. Shor(1995-10)Scheme for reducing decoherence in quantum computer memory.Phys. Rev. A52,pp. R2493–R2496.External Links:Document,LinkCited by:§1.
- [64]I. Siddiqi(2021)Engineering high-coherence superconducting qubits.Nat. Rev. Mater.6(10),pp. 875–891.External Links:Document,ISSN 20588437Cited by:§1.
- [65]N. J. T. Smith(2012-09)The SNOLAB deep underground facility.Eur. Phys. J. Plus127(9),pp. 108.External Links:Document,ISSN 2190-5444,LinkCited by:§1.
- [66]SNOLAB(2016)SNOLAB technical reference manual.Note:Revision 0Cited by:§3.5,§3.6.
- [67]SNOLAB(2026)Radiopurity.org.Note:https://www.radiopurity.orgAccessed on March 18, 2026Cited by:Appendix A,Appendix B,§2.2.
- [68]SNOLAB(2026)SNOLAB Low Background Counting Facility.Note:https://www.snolab.ca/users/services/gamma-assay/index.htmlAccessed on March 18, 2026Cited by:§2.1,§2.2,Table 1,Table 1.
- [69]A. M. Steane(1996-07)Error Correcting Codes in Quantum Theory.Phys. Rev. Lett.77,pp. 793–797.External Links:Document,LinkCited by:§1.
- [70]M. Stein, D. Bauer, R. Bunker, R. Calkins, J. Cooley, B. Loer, and S. Scorza(2018)Radon daughter plate-out measurements at SNOLAB for polyethylene and copper.Nucl. Instrum. Methods Phys. Res. A880,pp. 92–97.External Links:ISSN 0168-9002,Document,LinkCited by:§3.5,§3.5.
- [71]A. P. Vepsäläinen, A. H. Karamlou, J. L. Orrell, A. S. Dogra, B. Loer, F. Vasconcelos, D. K. Kim, A. J. Melville, B. M. Niedzielski, J. L. Yoder, S. Gustavsson, J. A. Formaggio, B. A. VanDevender, and W. D. Oliver(2020)Impact of ionizing radiation on superconducting qubit coherence.Nature584(7822),pp. 551–556.External Links:Document,2001.09190,ISSN 14764687Cited by:§1,§4.2.
- [72]C. D. Wilen, S. Abdullah, N. A. Kurinsky, C. Stanford, L. Cardani, G. D’Imperio, C. Tomei, L. Faoro, L. B. Ioffe, C. H. Liu, A. Opremcak, B. G. Christensen, J. L. DuBois, and R. McDermott(2021)Correlated charge noise and relaxation errors in superconducting qubits.Nature594(7863),pp. 369–373.External Links:Document,2012.06029,ISSN 14764687Cited by:§1.
- [73]E. Yelton, C. P. Larson, V. Iaia, K. Dodge, G. La Magna, P. G. Baity, I. V. Pechenezhskiy, R. McDermott, N. A. Kurinsky, G. Catelani, and B. L.T. Plourde(2024)Modeling phonon-mediated quasiparticle poisoning in superconducting qubit arrays.Phys. Rev. B110(2).External Links:Document,2402.15471,ISSN 24699969Cited by:Table 14,Table 14,Table 14,Appendix D,Appendix D,§5.
- [74]J. F. Ziegler, M.D. Ziegler, and J.P. Biersack(2010)SRIM – the stopping and range of ions in matter (2010).Nucl. Instrum. Methods Phys. Res. B268(11),pp. 1818–1823.Note:19th International Conference on Ion Beam AnalysisExternal Links:ISSN 0168-583X,Document,LinkCited by:§3.5.

## Appendix ADetailed assay results

This section provides the full radioactivity screening results of all assayed components and materials.
Table10includes the excerpt presented in table2of this article but contains more isotopes.
The complete assay results including all isotopes probed were published onradiopurity.org[67].
In several cases, the products of different vendors were screened to select components which are low in radioactivity.
For several of the listed components and raw materials such as aluminum or copper, samples were assayed which are not necessarily of the exact same batch as was used for producing certain parts, but they were usually provided by the same vendor.

Previously used999Used PCBs may have residual solder contamination and wire bond footprints from prior assembly.and also new PCBs of different vendors have been assayed.
In particular, CERcuits from Belgium provided several batches of the individual components used to manufacture PCBs Al2O3and AlN, which were separately assayed to better identify which specific components contribute most significantly to the radioactivity of PCBs.Table 10:Results of the assay and screening measurements showing the contamination levels of different radioisotopes and decay chains in the various components. For238U, the top and bottom parts of the chains are reported separately. Entries with a dash (“-”) mean that the detector used for the assay measurement had no sensitivity to the particular radioisotope of interest, or it was not reported. In contrary to the selection presented in table2, here the actual mass of the assayed sample and if applicable the number of units are provided.ComponentMass238U235U232Th210Pb137Cs60Co40K[g][mBq/kg][mBq/kg][mBq/kg][mBq/kg][mBq/kg][mBq/kg][mBq/kg]Sample holdersUWaterloo homemadesample holder126.1t: 59.2±\pm24.21.3±\pm0.56.9±\pm1.6<<42384<<0.5<<1.131.0±\pm13.7b:1.2±\pm1.3OQTO sample holder220.0t: 1099.0±\pm195.428.6±\pm2.638.4±\pm4.7-<<3.0<<0.860.2±\pm25.5b: 20.4±\pm3.3Printed-circuit boardsGold-plated PCBs(Aspocom/Provexa)8.164t: 8911±\pm197779.7±\pm23.92032.0±\pm117.6-<<72.5<<23.71840.5±\pm493.9(2 units)b: 1579.0±\pm88.9Used PCBs RO3010(Rogers Corporation)10.0t: 419.3±\pm94.715.2±\pm2.7220.5±\pm18.01610.1±\pm717.7<<39.79.7±\pm15.13593.4±\pm686.7(5 units)b: 270.4±\pm18.2New PCBs RO3010(Rogers Corporation)10.7t: 459.1±\pm83.611.7±\pm2.5208.7±\pm16.6<<984.9<<40.5<<25.21802.2±\pm517.1(5 units)b: 241.6±\pm16.4Tin-plated PCB(PCBWay)4.806t: 9544.0±\pm688.6304.2±\pm16.56481.0±\pm250.13163.1±\pm1665.0<<70.6<<69.17503.0±\pm1695.0(13 units)b: 5386.0±\pm191.3PCB, EPIG Plating(Elco BV, Hofstetter PCB)7.835t: 6132±\pm1973106.5±\pm27.92232.0±\pm138.9-<<38.0<<26.01380.1±\pm567.8(2 units)b: 1499.0±\pm101.2PCB TMM10(Rogers Corporation)55.6t: 6816.0±\pm2988.0871.7±\pm53.54813.0±\pm202.6-4.0±\pm59.435.5±\pm38.415604.0±\pm1228.0b: 30350.0±\pm659.3PCB RO4350B(Rogers Corporation)165.7t: 27190.0±\pm2974.4913.6±\pm41.718930.0±\pm499.2-17.1±\pm40.027.2±\pm24.415175.0±\pm949.8b: 16050.0±\pm348.4EPIG-plated 7-layer PCB(Aspocomp)20.56t: 3944.0±\pm432.7117.3±\pm15.82275.0±\pm95.4<<589.3<<12.6<<11.21390.4±\pm263.6(5 units)b: 2392.0±\pm85.1AlOx{}_{\text{x}}tin-plated PCB(CERcuits)0.584t: 8104±\pm1197189.5±\pm41.46149.0±\pm407.2<<4672<<679.1<<469.214077±\pm7897(2 units)b: 3337.0±\pm276.7Components used to manufacture PCBs Al2{}_{\text{2}}O3{}_{\text{3}}and AlN by CERcuitsPCB Al2O3- 11.506t: 6719.0±\pm604.5215.9±\pm21.25079.0±\pm256.11439±\pm1707<<323.4<<153.22902±\pm2820(5 units)b: 3144.0±\pm161.8PCB Al2O3- 2134.3t: 15460.0±\pm732.8299.9±\pm8.5810.8±\pm26.7<<1688<<2.5<<4.3835.2±\pm76.0b: 1530.0±\pm36.2PCB AlN - Ceramic strips38.46t: 3233.0±\pm642.450.4±\pm8.3137.2±\pm19.8-<<11.5<<5.0<<166.5b: 18.6±\pm10.1PCB AlN - Ceramic plates10.645t: 3718±\pm104571.2±\pm16.236.6±\pm31.8-<<30.4<<7.3<<266.7b:<<35.0PCB AlN - copperbacked circuit board plates45.2t: 6641±\pm489129.6±\pm8.52296±\pm75<<9088<<12.3<<5.9253.3±\pm97.6b: 1439.0±\pm45.2Silicon wafersSi wafer 4"9.564t: 267.1±\pm305.78.0±\pm4.7<<21.590958±\pm75010<<10.4<<5.985.4±\pm111.4b:<<4.4Si wafer 2" Type 0112.726t: 308.2±\pm405.47.7±\pm10.2<<45.8<<21840<<34.4<<8.0<<290.2b:<<11.9Si wafer 2" Type 0102.677t:<<516.8<<22.0<<28.529123±\pm2215012.9±\pm15.9<<18.4<<336.7b:<<12.6Si wafer 2" Type 122.7t:<<601.7<<10.1<<20.5<<15580<<26.5<<4.3166.4±\pm298.6b:<<7.10UWaterloo Si wafer 4"(University Wafer)9.515t: 125.9±\pm309.79.8±\pm4.5<<25.9<<88870<<8.9<<6.7<<121.7b:<<3.3Microwave cablesNbTi cable assembly6.2t: 17470.0±\pm11043.0352.2±\pm13.3509.4±\pm33.811055±\pm4231<<58.4<<9.3137.8±\pm146.4b: 56.6±\pm13.8Formable non-magnetic cableassembly (EZ Form Cable)20.2t: 787.7±\pm1024.0<<14.2<<38.9-<<21.0<<2.8233.6±\pm289.6b:<<37.7CuNi cable assembly7.2t: 322.2±\pm187.65.9±\pm3.7<<21.557731±\pm179007.8±\pm5.1<<2.5<<75.9b:<<2.6Nb cable assembly9.0t:<<1721.0<<34.6290.7±\pm49.1<<26610<<23.8<<22.7357.6±\pm244.1b: 1200.0±\pm73.8Stainless steelcable assembly39.9t: 163.5±\pm217.8<<7.4103.2±\pm13.8<<1896<<12.82.0±\pm2.8112.3±\pm67.7b:<<10.9continued on next pageComponentMass238U235U232Th210Pb137Cs60Co40K[g][mBq/kg][mBq/kg][mBq/kg][mBq/kg][mBq/kg][mBq/kg][mBq/kg]Microwave componentsIR Filter (CNTs)[52]68.8t: 193.3±\pm37.45.4±\pm0.69.6±\pm2.0753.2±\pm876.4<<0.9<<3.657.8±\pm34.6(3 units)b: 3.5±\pm1.6IR filter (Bluefors)12.9568t: 1459.0±\pm216.528.9±\pm3.420.6±\pm9.177515±\pm5479<<40.7<<21.0505.5±\pm297.6b:<<8.7IR Filter (CliQ10)25.3t: 39.6±\pm23.32.4±\pm1.246.4±\pm6.1<<146.4<<15.74.7±\pm9.7720.3±\pm246.5b: 32.5±\pm6.1Amumetal circulator withcryoperm shield (Raditek)377.9t: 135.0±\pm115.510.1±\pm1.922.4±\pm3.2-<<1.82.5±\pm1.045.5±\pm18.6b: 41.1±\pm3.3Microwave switchR591763600 (Radiall)95.5t: 7554.0±\pm667.9133.5±\pm8.2826.0±\pm32.7410550±\pm150300<<7.32.2±\pm3.2806.2±\pm92.6b: 453.0±\pm19.8Low Pass Filter SLP-1.9+(Mini-Circuits)35.5t:<<200.3<<8.8231.4±\pm17.5<<334.6<<7.111.7±\pm4.4366.4±\pm87.8b: 52.5±\pm13.8Connectors and screwsM2 brass screws(Skruvcenter)5.092t:<<62.2<<6.6<<11.8<<603.7<<79.627.7±\pm28.1391.5±\pm525.7(16 units)b:<<15.0Brass washers(Spaenaur)1.97t:<<166.1<<6.9<<40.1<<994.4<<204.9<<39.94025.6±\pm1520.0b:<<65.8Brass nuts(Spaenaur)2.29t:<<168.320.4±\pm7.622.5±\pm30.6<<834.7<<184.4<<52.91539.1±\pm1351.0b: 27.1±\pm32.7SMA connectors(Quantum Microwave)23.237t: 96.7±\pm41.85.6±\pm1.41.2±\pm3.96922.0±\pm407.50.6±\pm11.42.0±\pm5.391.7±\pm99.8(10 units)b:<<3.8SMA pins(Quantum Microwave)0.048t: 34510.0±\pm10310.0895.2±\pm254.61688.0±\pm1006.0<<55050.0<<8141.0<<1505.052452.0±\pm43130.0b: 488.4±\pm953.0SMA PTFE(Quantum Microwave)0.068t:<<4004.050.8±\pm117.6<<933.74902.9±\pm32940.0<<5595.0<<902.226711.0±\pm25970.0b:<<476.4SMA cap(Amphenol RF)12.67t:<<33.2<<3.28.9±\pm5.62224.3±\pm203.7<<33.8<<36.4<<398.4(5 units)b: 12.0±\pm6.2Magnetic shieldsAmumetal shield (Bluefors)49.6t: 852.6±\pm133.512.5±\pm1.99.9±\pm4.427642±\pm16580<<2.4<<1.945.0±\pm34.6b:<<1.2Al shield593.3t: 6446.0±\pm288.8116.2±\pm2.9125.8±\pm4.67346.1±\pm840.5<<1.60.2±\pm0.312.2±\pm6.5b: 6.2±\pm1.2Amumetal plate15.6t: 527.5±\pm544.6<<15.1<<36.9-<<13.7<<4.41017.9±\pm305.1b:<<20.0Magnetic shield plate CP-EXP-1184(Ad-Vance Magnetics Inc)89.9t:<<171.4<<14.6134.1±\pm21.4<<3703<<13.47.1±\pm5.4<<126.6b: 3.7±\pm19.8AluminumUsed aluminum (99.999%)(Kurt J Lesker)139.063t:<<85.7<<2.89.5±\pm3.6-<<1.7<<0.7<<26.9b:<<3.9Used aluminum (99.999%)(Kurt J Lesker)24.851t:<<403.5<<4.883.0±\pm12.1-<<5.4<<3.497.5±\pm86.5b:<<3.6Al pellets (99.999%)(Kurt-J Lesker)4.246t:<<133.0<<6.716.2±\pm13.4<<967.1<<90.3<<12.6<<754.9b:<<13.6Al slugs (99.999%)(Alfa Aesar, Puratronic)1.97t:<<131.9<<7.8<<18.9<<1762<<209.0<<38.11780.1±\pm962.0b:<<17.3Aluminum alloy semi-disc(Bluefors)33.207t: 7385±\pm1143166.1±\pm15.8339.4±\pm33.4-<<29.5<<3.8<<193.2b: 16.2±\pm14.4Aluminum alloy discs18.036t: 465.7±\pm335.2<<11.0273.1±\pm21.0-<<11.1<<2.0<<106.9(4 units)b:<<9.6Other raw materialsCopper sample (Bluefors)94.08t:<<130.81.2±\pm1.6<<4.9-<<5.9<<0.8<<65.1b:<<2.4Ti pellets (99.999%)(Kurt-J Lesker)2.66t:<<154.45.0±\pm4.3<<23.1<<2802<<129.8<<72.5<<1538b: 22.0±\pm20.1BF-6 glue(Ukrvet Biopharm)94.0t:<<44.7<<1.626.6±\pm4.5<<130<<3.7<<0.842.9±\pm24.4b:<<1.3Copper powder (99%)(thermo scientific)24.5t:<<385.6<<9.9<<50.5<<171812.3±\pm8.8<<9.7195.2±\pm88.8b:<<16.2Glass beads(thermo scientific)28.9t: 14190±\pm1195409.7±\pm36.45785±\pm233.4<<934.6<<80.3<<59.6101610±\pm5762b: 8855±\pm270.7Carbon black (99.9+%)(thermo scientific)1.45t:<<4130<<891199±\pm259<<13270<<128.1<<98.24492.1±\pm1484.0b:<<71.6NbTi superconducting wire(SUPERCON)1.8t:<<20213.1±\pm15.8<<115.8<<518<<225<<188.52310.4±\pm2834.0b:<<106.2Unfluxed desolder braid(Chemtronics)8.745t:<<50.53.0±\pm2.1<<17.8<<160.9<<48.7<<23.81211.4±\pm426.5b:<<13.5RuO2 thermometer10.3t: 222.7±\pm75.07.9±\pm3.2203.0±\pm18.31188.9±\pm291.1<<42.1<<26.01150.7±\pm532.8b: 168.6±\pm17.9OFHC copper(McMaster-Carr)8.49t:<<84.32.8±\pm2.3<<14.5<<214.4<<58.8<<11.6831.5±\pm466.2b:<<16.9Conductive Copper Tape(McMaster-Carr)9.52t:<<49.1<<2.50.13±\pm0.51<<191.7<<48.6<<12.0868.5±\pm331.2b:<<5.1

## Appendix BBackground contribution of potential components

In this section, we compare some components which were not included in the background projections discussed in section3.3.

We have assayed several PCBs to select which one is best suited for our purpose.
The PCB with EPIG Plating (Elco BV, Hofstetter PCB) which was provided by Chalmers University was chosen relatively early because its contributing background rate of 0.163 mHz in the Si chip was significantly lower compared to others, e.g. the PCB TMM10 (Rogers Corporation) with 0.945 mHz or PCB RO4350B (Rogers Corporation) with 1.199 mHz.
Because the PCB turned out to dominate the background rate together with the Si chip itself and the OQTO holder, the University of Waterloo explored other PCB options.
A more recent assay of an EPIG-plated 7-layer PCB (Aspocomp) shows promising results of 0.159 mHz (without210Pb) which is comparable to the original PCB choice and will be considered for future QUTEbits runs.

In order to mitigate ambient IR, we considered two potential IR absorbers: one as a layer inside the CM shield which is in line of sight with the Al cavities, and another one at the OQTO holder surfaces in direct line of sight with the Si chip.
Table11summarizes the background rates from relevant IR absorber components.
We do not list Stycast 1266 because its background contribution is negligible compared to the other components.
Carbon black and the glass beads dominate.
The former could be replaced by copper powder, which decreases the induced background rate by more than a factor of ten.
The plots shown in figure3and4include the potential contribution of the IR absorbers consisting of a copper sheet, glass beads and copper powder.
We are currently exploring glass beads from various vendors to find a version that suits our low-radioactivity requirements.
Future assay results will be published onradiopurity.org[67]as a service to the community.Table 11:Simulated background rates in one Si chip for potential IR absorber components and locations. The results do not take into account the210Pb bulk assays.IR absorber at CM shieldIR absorber inside OQTO holderRecipe componentbackground rate [mHz]background rate [mHz]Copper sheet1.44⋅10−41.44\cdot 10^{-4}2.70⋅10−22.70\cdot 10^{-2}Glass beads7.49⋅10−37.49\cdot 10^{-3}9.34⋅10−19.34\cdot 10^{-1}Carbon black8.48⋅10−38.48\cdot 10^{-3}7.94⋅10−17.94\cdot 10^{-1}Copper powder4.07⋅10−44.07\cdot 10^{-4}5.19⋅10−25.19\cdot 10^{-2}

## Appendix CUncertainties in background simulations

Table12and table13summarize how the simulated background rates are composed of measurements and limits, because some assay results are reported as a contamination measurement with an uncertainty, while others were only upper limits because the radioactivity was below the detector’s sensitivity.
These differences have been propagated to the determined event rates in the following way.
For the case that a simulation results in no detector hit, a 90% C.L. upper limit is calculated, i.e. some assay results with uncertainties are accounted for as limits if the simulation statistics did not produce a statistically significant result.
This only occurred for components which are very far away from the Si chips, e.g. the outermost lead shield and components outside of it, such as the water tank of CUTE, and the volume attributed to the interstitial air in the shield.
All other simulations have small statistical uncertainties, which are usually well below the systematic uncertainties of the assay results or other known uncertainties such as the radon concentration.

In general, the bulk background rates are roughly equally composed of components reported as measurements or limits, respectively.
The same is true for the interstitial air, which takes into account the radon concentration measured inside SNOLAB and the purged air in the CUTE lead shield.
The surface contamination contains only a tiny portion of upper limits for the Si chips which arise solely from simulations with no detector hits for the presently simulated statistics.Table 12:Uncertainties and composition of simulated background rates for a Si chip.Background categoryTotal rate [mHz]Value±\pmuncertainties [mHz]Limit [mHz]Bulk5.51⋅10−15.51\cdot 10^{-1}(3.39±0.02​(stat.)±0.48​(syst.))⋅10−1(3.39\pm 0.02(\text{stat.})\pm 0.48(\text{syst.}))\cdot 10^{-1}<2.12⋅10−1<2.12\cdot 10^{-1}Interstitial air1.39⋅10−31.39\cdot 10^{-3}(9.57±5.53​(stat.)±0.48​(syst.))⋅10−4(9.57\pm 5.53(\text{stat.})\pm 0.48(\text{syst.}))\cdot 10^{-4}<4.29⋅10−4<4.29\cdot 10^{-4}Surface210Pb1.37⋅10−11.37\cdot 10^{-1}(1.37±0.002​(stat.)±0.76​(syst.))⋅10−1(1.37\pm 0.002(\text{stat.})\pm 0.76(\text{syst.}))\cdot 10^{-1}<1.90⋅10−6<1.90\cdot 10^{-6}Table 13:Uncertainties and composition of simulated background rates for an Al cavity.Background categoryTotal rate [mHz]Value±\pmuncertainties [mHz]Limit [mHz]Bulk7.78⋅1017.78\cdot 10^{1}(1.24±0.004​(stat.)±0.23​(syst.))⋅101(1.24\pm 0.004(\text{stat.})\pm 0.23(\text{syst.}))\cdot 10^{1}<6.54⋅101<6.54\cdot 10^{1}Interstitial air4.55⋅10−14.55\cdot 10^{-1}(2.60±0.09​(stat.)±0.13​(syst.))⋅10−1(2.60\pm 0.09(\text{stat.})\pm 0.13(\text{syst.}))\cdot 10^{-1}<1.95⋅10−1<1.95\cdot 10^{-1}Surface210Pb1.02⋅1011.02\cdot 10^{1}(1.02±0.001​(stat.)±0.57​(syst.))⋅101(1.02\pm 0.001(\text{stat.})\pm 0.57(\text{syst.}))\cdot 10^{1}-

The split time used to separate and combine hits into events (see section3.2) does affect the spectral shape in certain cases, which has been described in section4.1.
For the present analysis, we apply a split time ofΔ​t=15​μ​s\Delta t=15\,\mathrm{\mu s}, which has been informed by simulations performed with G4CMP (see section5.1).
In order to cross check how the split time affects the estimated background rate, the analysis was run with a split time ofΔ​t=1​ms\Delta t=1\,\mathrm{ms}.
The largest impact was observed for the bottom part of the238U decay chain (e.g. when contaminating the Si substrate and calculating the rate in the Si chip), which decreased the238U rate by 10%.
The same level of rate decrease was found for the238U contamination in the Al cavities.
For235U, the observed decrease is only about 2-3%, while for232Th the effect is less than 0.1%.
In combination, a larger split time leads to a relative decrease of the total background rate in the Si chip by 0.2% and in the Al cavity by 0.6%.

For the surface210Pb simulations, the systematic uncertainty is composed of the radon concentration measured on Earth’s surface and inside SNOLAB.
The former has a large uncertainty, which is propagated into the estimated210Pb emission rates from the materials’ surfaces.
Summing up all components, the210Pb emission rate is178.1±142.5​mBq178.1\pm 142.5\,\mathrm{mBq}due to radon exposure on Earth’s surface and78.2±3.9​mBq78.2\pm 3.9\,\mathrm{mBq}from underground exposure, leading to a total emission rate of256.3±142.6​mBq256.3\pm 142.6\,\mathrm{mBq}for the medium exposure scenario (see table5).
The uncertainties were added in quadrature as they are assumed to be uncorrelated.

As mentioned in section3.5, the Jacobi model was used to determine the ratio of adsorbed vs. implanted210Pb on surfaces and it has been found that 55.8% of the210Pb nuclei are implanted.
In order to calculate this ratio, an assumption of the initial fraction of218Po vs.214Po adhered on surfaces needs to be made.
The volume of the room, its ventilation and recirculation rate, and whether radon is filtered out determine the plate-out height.
Together with the half-lives of the222Rn progeny, the fraction of218Po vs.214Po adhered on surfaces was determined to be about 80% vs. 20%.
When adjusting these parameters into extreme ranges, one may end up with a fraction of 100% or 50% for218Po.
These three scenarios introduce an absolute systematic uncertainty of 2.6% on the ratio of adsorbed vs. implanted210Pb, which is an order of magnitude below the systematic uncertainties of the radon concentration, and thus has been neglected.

The simulations to determine the ratio of adsorbed vs. implanted210Pb were run for different materials – including Al, Cu, mu-metal and Si – to confirm that the ratio is independent of the material properties.
The final ratio of 55.8% implanted210Pb was calculated as an average of these simulations with a standard deviation of 0.9%.
The statistical uncertainties in these simulations are well below 0.1%.

## Appendix DG4CMP configuration and runtime optimization

The configuration of G4CMP for our showcase study using a Si chip with attached superconducting Al films, in particular the configuration of the surface properties of the interface between Si and Al, follows the procedure described in the appendix of Ref.[73].
For a general overview of the capabilities of G4CMP and its physics models see Ref.[35].

An excerpt of the most relevant G4CMP configuration parameters for our study is shown in table14.
The majority of the material properties are inherited from the default values shipped with the library.
Moreover, for the thickness of our Al mask ofdAl=300d_{\text{Al}}=300nm, the phonon absorption by Al can be modeled with an energy independent probabilitypabsp_{\text{abs}}:pabs=ptrans​(1−pesc)≈ptrans​with​pesc→0.p_{\text{abs}}=p_{\text{trans}}(1-p_{\text{esc}})\approx p_{\text{trans}}\text{ with }p_{\text{esc}}\rightarrow 0.(D.1)

Equation (D.1) includes a transmission termptransp_{\text{trans}}for the Si-to-Al boundary taken from[73]and an escape probabilitypescp_{\text{esc}}for phonons that traverse the Al film thickness and return to the substrate without breaking a Cooper pair.
The latter can be expressed as[73]:pesc=exp⁡(−4​dAlλ​(Eph)).p_{\text{esc}}=\exp\left(-\frac{4d_{\text{Al}}}{\lambda(E_{\text{ph}})}\right).(D.2)

For superconducting Al, the phonon mean free pathλ​(Eph)\lambda(E_{\text{ph}})can be expressed as the ratio of the isotropic speed of sound in Al, denoted asvsv_{s}, and the Cooper-pair-breaking rateΓphb\Gamma^{b}_{\text{ph}}:λ​(Eph)=vs/Γphb\lambda(E_{\text{ph}})=v_{s}/\Gamma^{b}_{\text{ph}}(D.3)

withΓphb=1τ0ph​{1+0.29​[(EphΔAl)−2]}.\Gamma^{b}_{\text{ph}}=\frac{1}{\tau_{0}^{\text{ph}}}\left\{1+0.29\left[\left(\frac{E_{\text{ph}}}{\Delta_{\text{Al}}}\right)-2\right]\right\}.(D.4)

Table14demonstrates the outcome of eq. (D.1) – (D.4) assuming a phonon energy ofEph=4E_{\text{ph}}=4\,meVwhich is representative for our case study.
For a thinner Al film, e.g.dAl=30d_{\text{Al}}=30nm, the phonon escape probability would result inpesc=38.6%p_{\text{esc}}=38.6\%for the same inputs in comparison.Table 14:Excerpt of relevant G4CMP simulation parameters. The majority of the material parameters for Al and Si are taken from Ref.[35]and[73]. The calculated quantities were evaluated for a phonon energy ofEph=4E_{\text{ph}}=4\,meV.ParameterSymbolValueReferenceAl mask thicknessdAld_{\text{Al}}0.3μ\muminputPhonon energyEphE_{\text{ph}}4.0 meVinputPhonon absorption probability in Alpabsp_{\text{abs}}0.795calculatedPhonon escape probability in Alpescp_{\text{esc}}≈\approx0calculatedPhonon transmission probability for Si-Alptransp_{\text{trans}}0.795[73]Pair-breaking rate in AlΓphb\Gamma^{b}_{\text{ph}}29.33 1/nscalculatedPhonon mean free path in Alλ​(Eph)\lambda(E_{\text{ph}})0.11μ\mumcalculatedIsotropic speed of sound in Alvsv_{s}3.26μ\mum/ns[35](Al)Phonon lifetime in Alτ0ph\tau_{0}^{\text{ph}}0.242 ns[35](Al)Al superconducting bandgapΔAl\Delta_{\text{Al}}0.174 meV[35](Al)Si bandgapεg\varepsilon_{g}1.17 eV[35](Si)Average energy to create e-h+pair in Siεeh\varepsilon_{\text{eh}}3.81 eV[35](Si)Si Fano factorFF0.15[35](Si)Debye frequency / energy in SiωD\omega_{D}15 THz / 62 meV[35](Si)Longitudinal speed of sound in Sivsv_{s}9000 m/s[35](Si)

In addition to the basic configuration of the material properties and phonon interfaces, we optimized the runtime of our G4CMP-based simulations by making use of several available energy downsampling features (see Ref.[35]for a detailed description).
The first measure is to terminate all phonon tracks that are not able to break Cooper pairs in Al because they do not carry a sufficient energy ofEph≥2​ΔAlE_{\text{ph}}\geq 2\Delta_{\text{Al}}withΔAl\Delta_{\text{Al}}being the superconducting gap of Al (see table14).
This greatly reduces the number of low-energy phonons to be tracked in the simulation per event.

For the simulation of the high-energy particle hits byβ\betaelectrons, which can spread out over the entire Si chip volume for sufficiently energetic electrons, we make use of combining hits that are closer together in space than 2 mm.
This measure reduces the overall tracking time significantly for high-energy electrons in particular because eachGeant4particle hit would otherwise be processed separately in G4CMP.
Additionally, each energy deposit is downsampled to an equivalent energy deposit of 200 eV (see section5.2) to reduce the number of charge carrier pairs and primary phonons per event to a representative ensemble with appropriate track weights (see[35]for details).
For an ER-like energy deposit of 200 eV in Si an average of 52.5 e-h+pairs will be created.
For an NR-like energy deposit of the same energy butY=0.1Y=0.1, on average 5 e-h+pairs and about 2800 prompt phonons will be created.
Hits grouped together by the hit-merging algorithm are downsampled together according to the set energy partition value.
Finally, we restrict the maximum number of phonons created by lattice scattering (referred to as “Luke” phonons) and the maximum number of phonon reflections after which tracks get terminated.
A summary is presented in table15.Table 15:Summary of G4CMP downsampling parameters. The options are roughly presented in order of effectiveness with respect to the runtime improvement per event. The last two restrictions barely had an impact on any of the simulated cases discussed in section5when combined with the previous downsampling methods.DescriptionG4CMP commandDo not track phonons withEph<2​ΔAlE_{\text{ph}}<2\Delta_{\text{Al}}/g4cmp/minEPhonons 348e-6 eVDo not record below-minimum energy tracks/g4cmp/recordMinETracks falseCombine hits below step length of 2 mm/g4cmp/combiningStepLength 2 mmDownsample energy deposits to 200 eV/g4cmp/samplingEnergy 200 eVSet maximum of Luke phonons per event to10510^{5}/g4cmp/maxLukePhonons 100000Set maximum phonon reflections to10410^{4}/g4cmp/phononBounces 10000

## Appendix EComputing resources

TheGeant4background simulations consumed in total 32.8 CPU years.
The simulations are composed of 482 combinations of components with their corresponding isotopes in the bulk, two special configurations for the interstitial air, and 20 components with210Pb adsorbed and implanted on surfaces.
The cavernγ\gammaray simulations have been broken down into their contributions from232Th,238U and40K.
The cavern neutrons have been simulated separately.
In total,3.63⋅10123.63\cdot 10^{12}primary decays were generated for the background simulations, which comprises6.1⋅10116.1\cdot 10^{11}events for the bulk,2.1⋅10102.1\cdot 10^{10}events for the surface and3.0⋅10123.0\cdot 10^{12}for the cavern simulations.

The calibration source simulations consumed about 4.9 CPU years for the133Ba source studies and 0.5 CPU years for252Cf.
For each of the twelve possible payload rotations,101010^{10}primary133Ba decays were simulated.
The252Cf induced ER and NR rates were investigated at two different positions, with10910^{9}primary decays each.

The G4CMP simulations were optimized for runtime as discussed in appendixDbefore running the final production batch with high statistics (up to10710^{7}events per configuration) in a multithreaded fashion.
The optimization consumed about 1.1 CPU years and the final production batch comprising simulations of a bulk contaminant source and a point source at the center of the Si chip consumed about 0.4 CPU years.
The multithreaded simulations achieved on average a CPU efficiency of 80% with eight worker threads.

In total, the simulations performed for this work consumed about 39.7 CPU years on the Fir cluster of the Digital Research Alliance of Canada.

## 


- 


Major funding support from
