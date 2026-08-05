# Harnessing resonant dipolar interactions in a hybrid atom-molecule quantum system

**arXiv ID**: 2607.15976v1
**Authors**: Daniel K. Ruttley, Tom R. Hepworth, Juan M. García-Garrido, Caleb J. H. Rich, Rosario González-Férez, Alexander Guttridge, Simon L. Cornish
**Published**: 2026-07-17
**Categories**: physics.atom-ph, quant-ph
**Comments**: 20 pages, 10 figures
**HTML URL**: https://arxiv.org/html/2607.15976v1

## Abstract

Hybrid quantum systems offer a route to combining the complementary strengths of distinct quantum platforms while mitigating their limitations. A particularly promising architecture combines neutral atoms and polar molecules: atoms provide fast, controllable interactions through excitation to Rydberg states, while molecules possess long-lived rotational states that are attractive for quantum memories and qudits. Although dipolar interactions between atoms and molecules have been observed in gas-phase and beam experiments, they have not previously been explored in a scalable optical tweezer platform that enables the controlled coherent interactions needed for quantum state transfer and entanglement. Here, we realise this goal, demonstrating coherent dipolar interactions between an individual Rydberg atom and an individual polar molecule. The separation of the particles is controlled using species-specific optical tweezers and their dipolar interactions are made strongly state-dependent by tuning two atom-molecule pair states into resonance. We exploit these interactions to demonstrate atom-mediated state readout of a molecular qubit, observe coherent spin exchange between the particles, and generate entanglement using a blockade-based controlled-NOT operation. Together, these results establish a coherent atom-molecule interface in which long-lived molecular quantum information can be rapidly mapped onto internal states of a Rydberg atom for readout or onward coherent transfer. This platform can be scaled to realise hybrid quantum processors utilising atom-mediated readout and entanglement of molecular qubits and mixed-species quantum simulators of dipolar systems.

## Full Text

Harnessing resonant dipolar interactions in a hybrid atom-molecule quantum system

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- License: CC BY 4.0arXiv:2607.15976v1 [physics.atom-ph] 17 Jul 2026

## Harnessing resonant dipolar interactions in a hybrid atom-molecule quantum systemDaniel K. Ruttleydaniel.k.ruttley@durham.ac.ukDepartment of Physics, Durham University, South Road, Durham, DH1 3LE, United KingdomTom R. HepworthDepartment of Physics, Durham University, South Road, Durham, DH1 3LE, United KingdomJuan M. García-GarridoDepartamento de Física Atómica, Molecular y Nuclear, Universidad de Granada, 18071 Granada, SpainCaleb J. H. RichDepartment of Physics, Durham University, South Road, Durham, DH1 3LE, United KingdomRosario González-FérezDepartamento de Física Atómica, Molecular y Nuclear, Universidad de Granada, 18071 Granada, SpainInstituto Carlos I de Física Teórica y Computacional, Universidad de Granada, 18071 Granada, SpainAlexander GuttridgeDepartment of Physics, Durham University, South Road, Durham, DH1 3LE, United KingdomSimon L. Cornishs.l.cornish@durham.ac.ukDepartment of Physics, Durham University, South Road, Durham, DH1 3LE, United Kingdom

## Abstract

Hybrid quantum systems offer a route to combining the complementary strengths of distinct quantum platforms while mitigating their limitations[1,2].
A particularly promising architecture combines neutral atoms and polar molecules[3,4,5,6,7]: atoms provide fast, controllable interactions through excitation to Rydberg states[8,9,10,11], while molecules possess long-lived rotational states that are attractive for quantum memories and qudits[12].
Although dipolar interactions between atoms and molecules have been observed in gas-phase[13,14]and beam[15,16]experiments, they have not previously been explored in a scalable optical tweezer platform that enables the controlled coherent interactions needed for quantum state transfer and entanglement.
Here, we realise this goal, demonstrating coherent dipolar interactions between an individual Rydberg atom and an individual polar molecule.
The separation of the particles is controlled using species-specific optical tweezers and their dipolar interactions are made strongly state-dependent by tuning two atom–molecule pair states into resonance.
We exploit these interactions to demonstrate atom-mediated state readout of a molecular qubit, observe coherent spin exchange between the particles, and generate entanglement using a blockade-based controlled-NOT operation.
Together, these results establish a coherent atom–molecule interface in which long-lived molecular quantum information can be rapidly mapped onto internal states of a Rydberg atom for readout or onward coherent transfer.
This platform can be scaled to realise hybrid quantum processors utilising atom-mediated readout[17,18,19,15,20,21]and entanglement of molecular qubits[4,5,6,7]and mixed-species quantum simulators of dipolar systems[22,23].

## Introduction

Hybrid quantum systems provide a route to combining the advantages of distinct quantum platforms while mitigating their individual limitations[1,2].
In such architectures, the large variation in energy scales, timescales, and sensitivities of the constituent quantum platforms can give rise to new capabilities. Cross-talk can be strongly suppressed[24,25,26], enabling high fidelity mid-circuit readout[27,25,21], quantum syndrome measurements[28], the engineering of novel Hamiltonians for quantum simulation[29,30], and computation schemes based on global control[31].

A particularly promising hybrid platform combines neutral atoms and polar molecules. Both support long-range dipolar interactions and can be individually controlled using optical tweezer arrays.
Neutral-atom arrays are emerging as a leading platform for quantum science[8,9,10,11]: large arrays of atoms can be prepared[32], and their interactions can be rapidly switched via excitation to Rydberg states, enabling fast entangling operations with high connectivity[33].
However, the Rydberg states are comparatively short-lived, limiting the timescales over which strong interactions can be maintained[34].
In contrast, polar molecules possess a rich structure of long-lived rotational and hyperfine states[12], making them attractive as qudits[35]and quantum memories with coherence times of many seconds[36,37,38,39,40,41].
However, dipolar interactions between molecules are typically much weaker than those between Rydberg atoms, leading to comparatively slow entangling operations[42,43,44,40,45,46,47].

Hybrid atom–molecule systems offer a route to combine these complementary strengths, using molecules for long-lived information storage and atoms for fast quantum control.
Such systems have been proposed for quantum computation[3,5,4,6,7], quantum simulation[22,23], and non-destructive molecular detection[17,18,19,15,20,21].
Beyond quantum information processing, atom–molecule systems provide a platform for studying fundamentally new phenomena, including Rydberg-mediated molecular cooling[48,49,50]and exotic polyatomic bound states[51,52,53].
Realising many of these applications requires strong and controllable interactions between the atom and molecule.
Although atom–molecule dipolar interactions have been observed in several systems[13,15,16,14], they have not yet been explored in a scalable optical tweezer platform that enables the controlled coherent interactions combined with single particle control.
As a result, crucial operations such as coherent exchange of quantum information and entanglement generation between atoms and molecules have remained out of reach.

In this work, we overcome this limitation by engineering resonant dipolar interactions between a single atom–molecule pair confined in separate species-specific optical tweezers.
By tuning atomic and molecular transitions into resonance, we realise MHz-scale interactions at micron-scale separations that are strongly state dependent.
We use these interactions to perform atom-mediated molecular readout, observe coherent spin exchange between the particles, and generate atom-molecule entanglement.
These results establish a new hybrid platform for quantum science.

## Engineering resonant interactions

We engineer resonant dipolar interactions between a single Rb atom and a single RbCs molecule.
The particles are confined in species-specific optical tweezers which enable precise control of the interparticle separationRR(see Methods).
We start with the atom in the electronic ground state|5​s⟩\ket{5\mathrm{s}}and the molecule in the absolute ground state|0⟩\ket{0}, labelled by the rotational quantum numberNN.
Throughout this work, we restrict both particles to stretched states (see Methods).
An applied magnetic field ofB≈200​GB\approx 200\,\mathrm{G}defines the quantisation axis, which is aligned with the interparticle vector (see Fig.1a).

To create long-ranged interactions, we excite the atom to a Rydberg state with a spatially extended electron wavefunction.
Typically, we operate in a regime where the atom–molecule separation is large compared with the spatial extent of this wavefunction.
In this limit, the interactions can be approximated in terms of effective transition dipole moments between internal states (see Methods). Although the particles interact fundamentally through the dipole–dipole interaction, the single-particle eigenstates possess no permanent electric dipole moments.
Off-resonance, the leading interaction arises only at second order in perturbation theory, producing a van der Waals interaction that scales as1/R61/R^{6}[10,11].
At micron-scale separations, the resulting interaction strengths are typically only a few kHz[54], making them difficult to exploit experimentally.

A much stronger interaction emerges when an electric-dipole transition in the atom is resonant with an electric-dipole transition in the molecule[55]. In this Förster-resonant regime, the dipole–dipole interaction appears at first order and scales as1/R31/R^{3}[10,11].
Resonant interactions of this form have previously been engineered in single-species atomic[9,10,11]and molecular[42,43,44,40,12]optical-tweezer platforms.
Additionally, they have been observed in dual-species atomic experiments[24,25,26].
In the atom–molecule context, they have been observed in gas-phase[13,14]and beam[15,16]experiments, but have not yet been brought into the coherent regime.

To engineer these resonant interactions, we match an electric-dipole-allowed transition in the molecule with a corresponding transition in the Rydberg manifold such that the detuningδ≡(Δ​EA+Δ​EM)/h\delta\equiv(\Delta E_{\mathrm{A}}+\Delta E_{\mathrm{M}})/hvanishes.
Here,Δ​EA\Delta E_{\mathrm{A}}andΔ​EM\Delta E_{\mathrm{M}}are the difference in energies between the pairs of atomic and molecular states.
In Fig.1b, we showΔ​EA\Delta E_{\mathrm{A}}for atomic transitions experimentally accessible with two-photon excitation from the state|5​s⟩\ket{5\mathrm{s}}(see Methods).
We coarsely tune the Förster defect by choice of states and tune the states into exact resonance using a magnetic field.
The vertical extent of the data points reflects this tunability over a 100 G range.
Resonance occurs where these atomic transitions intersect the allowed molecular transitions (−Δ​EM-\Delta E_{\mathrm{M}}, dashed lines).Figure 1:Engineering resonant interactions between a molecule and an atom.a, Schematic of the experiment showing a RbCs molecule and a Rb Rydberg atom which are prepared in species-specific optical tweezers.b, Energies of transitions,Δ​EA\Delta E_{\mathrm{A}}, between the Rydberg levels of Rb as a function of the initial principal quantum number,nn. The height of the lines show the energy range accessible by varying a magnetic field over100100\,G. The dashed lines show when the atomic transitions become resonant with molecular transitions labelled as|N⟩→|N′⟩\ket{N}\to\ket{N^{\prime}}. The highlighted point shows the transitions that we use in this work.c, Energy levels used in this work, as described in the text. We tune the pair state|3;83​d⟩\ket{3;83\mathrm{d}}(blue) to be resonant with|4;84​p⟩\ket{4;84\mathrm{p}}(green).d, Microwave spectroscopy near the resonance condition. We show the frequencies|Δ​EA|/h|\Delta E_{\mathrm{A}}|/h(blue) and|Δ​EM|/h|\Delta E_{\mathrm{M}}|/h(black) of the atomic and molecular transitions as a function of magnetic field,BB. Resonance is achieved atBres=205.16​(2)B_{\mathrm{res}}=205.16(2)\,G. The error bars show the1​σ1\sigmaconfidence intervals and, on average, there are 1214 experimental shots per data point.e, Born–Oppenheimer potential-energy curvesU​(R)U(R)of as a function of the interparticle separation,RR, for different pair states atB=BresB=B_{\mathrm{res}}.

Here, we use the resonant pair states|3;83​d⟩\ket{3;83\mathrm{d}}and|4;84​p⟩\ket{4;84\mathrm{p}}, labelled|N;n​l⟩≡|N,MN=N;n​l,j=l+12,mj=j⟩\ket{N;nl}\equiv\ket{N,M_{N}=N;nl,j=l+\frac{1}{2},m_{j}=j}(see Methods for the full state labels).
Figure1c shows the corresponding single-particle energy levels, with the resonant pair states highlighted in blue and green.
The molecule is rotationally excited using microwave pulses[56]and the excited states are long-lived[40,41].
The atom is optically excited from|5​s⟩\ket{5\mathrm{s}}to|83​d⟩\ket{83\mathrm{d}}via a two-photon transition (see Methods).
We choose these pair states to balance the number of microwave pulses required for molecular state preparation against the practical challenges of atomic excitation to high-nnRydberg states[34].

We set the resonance condition using microwave spectroscopy of the single-particle transitions.
Figure1d shows the measured transition frequencies|Δ​EA|/h|\Delta E_{\mathrm{A}}|/h(blue) and|Δ​EM|/h|\Delta E_{\mathrm{M}}|/h(black) as a function of magnetic field.Δ​EA\Delta E_{\mathrm{A}}is strongly field-dependent due to the large Zeeman shift of the Rydberg manifold (see Methods).
In contrast,Δ​EM\Delta E_{\mathrm{M}}is effectively constant, as the stretched molecular states share identical nuclear spins and exhibit a negligible rotational Zeeman shift[57].
As a result, there is a crossing at a resonance fieldBres=205.16​(2)​GB_{\mathrm{res}}=205.16(2)\,\mathrm{G}whereΔ​EM=−Δ​EA≈3.9​GHz×h\Delta E_{\mathrm{M}}=-\Delta E_{\mathrm{A}}\approx 3.9\,\mathrm{GHz}\times h.

Figure1e shows the calculated Born–Oppenheimer potential-energy curvesU​(R)U(R)for different pair states, referenced to their asymptotic pair-state energies at infinite separation.
These energies are calculated using the full charge–dipole Hamiltonian, which tends to the dipole–dipole interaction at long range (see Methods).
The grey lines show the non-resonant cases|0;83​d⟩\ket{0;83\mathrm{d}}and|1;83​d⟩\ket{1;83\mathrm{d}}.
For these pair states, the interaction strength is kHz-scale until the molecule enters the spatial extent of the Rydberg-electron wavefunction, aroundR≈0.5​μ​mR\approx 0.5\,\mu\mathrm{m}[54].

By contrast, in the resonant case (δ→0\delta\to 0) the pair states|3;83​d⟩\ket{3;83\mathrm{d}}and|4;84​p⟩\ket{4;84\mathrm{p}}are strongly mixed at finiteRRand are no longer eigenstates of the system.
This hybridisation leads to MHz-scale interaction energies at micrometre separations (orange lines).
At long range, the coupling between the resonant states is well approximated by a dipolar interaction.
Then, the system can be described by the dipole–dipole Hamiltonian[10]Hdd=(0C3/R3C3/R3h​δ),H_{\mathrm{dd}}=\begin{pmatrix}0&C_{3}/R^{3}\\
C_{3}/R^{3}&h\delta\end{pmatrix},

in the basis{|3;83​d⟩,|4;84​p⟩}\{\ket{3;83\mathrm{d}},\ket{4;84\mathrm{p}}\}, whereC3=−dA​dM/(4​π​ϵ0)C_{3}=-d_{\mathrm{A}}d_{\mathrm{M}}/(4\pi\epsilon_{0})for our geometry (see Methods).
Here,dA=−14.5d_{\mathrm{A}}=-14.5\,kD anddM=0.82d_{\mathrm{M}}=0.82\,D are the transition dipole moments for the atom and molecule, respectively, givingC3/h=1.79​MHz​μ​m3C_{3}/h=1.79\,\mathrm{MHz}\,\mu\mathrm{m}^{3}.
At resonance, the eigenstates of this Hamiltonian are|±⟩=12​(|3;83​d⟩±|4;84​p⟩)\ket{\pm}=\frac{1}{\sqrt{2}}(\ket{3;83\mathrm{d}}\pm\ket{4;84\mathrm{p}})with energiesU​(R)=±C3/R3U(R)=\pm C_{3}/R^{3}.
This dipolar description is accurate forR≳1​μ​mR\gtrsim 1\,\mu\mathrm{m}, but at smaller distances, the full charge–dipole Hamiltonian must be considered to accurately calculateU​(R)U(R)(see Methods).Figure 2:Rydberg blockade caused by resonant atom–molecule interactions.a, Energy levels of the atom–molecule system for the non-resonant (red) and resonant (blue) cases atR≈1​μR\approx 1\,\mum, as described in the text.b, Atomic survival probability as a function of the two-photon detuning of the Rydberg excitation light. Red and blue points show data for molecules prepared in the states|0⟩\ket{0}and|3⟩\ket{3}, respectively, atR=0.9​(1)​μR=0.9(1)\,\mum. Grey points show the spectrum measured in the absence of a molecule. When the molecule is prepared in|3⟩\ket{3}, excitation of the atom is strongly suppressed.c, Atomic survival probability as a function of the duration of the Rydberg-excitation pulse. Colours are as in b.d, Characterisation of the distance dependence of the interactions. The atomic-survival probability is shown as a function of the separationRRof the atom and molecule. Blue (red) points show data for molecules prepared in|3⟩\ket{3}(|0⟩\ket{0}). Solid lines show the predicted behaviour, as described in the text. The dashed line is a fit to the blue data assuming a purely dipolar interaction; the blue shaded region shows the1​σ1\sigmaconfidence interval.
The grey region indicates the atom-only excitation contrast. Inset: atom-survival probability for different molecular rotational states atR=0.9​(1)​μR=0.9(1)\,\mum.
In all panels, the error bars show the1​σ1\sigmaconfidence intervals and, on average, there are 91 experimental shots per data point.

## Rydberg blockade

First, we demonstrate blockade of the atomic transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}arising from resonant atom–molecule interactions.
We hold the particles at a separation ofR=0.9​(1)​μR=0.9(1)\,\mum and drive the atomic transition using a resonantπ\pipulse with two-photon Rabi frequencyΩRyd/2​π=931​(5)\Omega_{\mathrm{Ryd}}/2\pi=931(5)\,kHz.
The optical tweezers are antitrapping for Rydberg atoms, meaning population of the Rydberg state results in atomic loss. We detect this loss via fluorescence imaging at the end of the experimental sequence (see Methods).
For all measurements presented in this work, we postselect experimental runs in which an atom–molecule pair is successfully prepared and the molecule is detected at the end of the sequence (see Methods).

In the absence of resonant interactions, such as when the molecule is prepared in the state|0⟩\ket{0}, the atom and molecule are effectively decoupled (Fig.2a, red).
By varying the two-photon detuning of the excitation light, we measure an excitation spectrum (Fig.2b, red) that approximately agrees with a reference measurement performed without a molecule (Fig.2b, grey). Crucially, the atom-loss probability when the light is on resonance, which provides a measure of the chance of Rydberg excitation, is consistent between the two cases (0.91(5) for the molecule in state|0⟩\ket{0}and 0.93(2) for the atom-only case).

By contrast, when the molecule is prepared in the state|3⟩\ket{3}, atomic excitation to|83​d⟩\ket{83\mathrm{d}}is strongly suppressed. In this regime, the resonant atom–molecule interaction hybridises the pair states into eigenstates|±⟩\ket{\pm}(Fig.2a, blue). AtR=0.9​(1)​μR=0.9(1)\,\mum, the interaction strength|U​(R)|/h≈2​MHz|U(R)|/h\approx 2\,\mathrm{MHz}exceeds the power-broadened linewidth of the transition and blockades excitation (i.e.|U​(R)|≳ℏ​ΩRyd|U(R)|\gtrsim\hbar\Omega_{\mathrm{Ryd}}). Consistent with this, the blue data in Fig.2b show a clear suppression of atomic excitation.
We do not resolve excitation to the interaction-shifted states|±⟩\ket{\pm}, which we attribute to fluctuations in the interaction strength and coupling to undetected hyperfine states in the molecule (see Methods).

In Fig.2c, we show the effect of varying the duration of the Rydberg-excitation pulse on resonance with the bare-atom transition.
In the absence of blockade (grey: no molecule, red: molecule in the state|0⟩\ket{0}), we observe clear Rabi oscillations. The lower bound of the atom-recovery probability is limited by infidelity in atomic-state preparation and Rydberg excitation (see Methods).
Conversely, when we prepare the molecule in the state|3⟩\ket{3}, the Rabi oscillation is strongly suppressed.
Compared with the non-resonant interactions observed in Ref.[54], the blockade is substantially more robust.
We attribute this to the fact that here moderate fluctuations inδ\deltaandRRdo not compromise the condition that the interaction shift exceeds the transition linewidth (see Methods).

We use the blockade to characterise the distance dependence of the interaction, as shown in Fig.2d. We perform this measurement with a two-photon Rabi frequencyΩRyd/2​π=318​(3)\Omega_{\mathrm{Ryd}}/2\pi=318(3)kHz and record the atomic survival after the Rydberg pulse as a function of interparticle separationRR.
As we varyRR, we compensate for light shifts of the Rydberg transition caused by varying the tweezer overlap (see Methods).
The atom-only excitation contrast is indicated by the grey shaded region.

The blue data in Fig.2d show the atomic recovery when the molecule is prepared in the state|3⟩\ket{3}.
We compare these data to the predicted survival probability (blue line) from a model in which we consider point-like particles with an interaction strength following the state|+⟩\ket{+}shown in Fig.1e (see Methods).
The oscillatory features observed forR≲1.4​μR\lesssim 1.4\,\mum arise from the use of a square excitation pulse: at the minima of these features, thesinc2\operatorname{sinc}^{2}sidelobes in the Fourier spectrum of the pulse overlap with the interaction-shifted transition (see Methods).

To facilitate comparison with other dipolar systems, we fit this data assuming perfect resonance, point-like particles, and a pure dipole–dipole interactionVdd​(R)V_{\mathrm{dd}}(R). From this fit (blue dashed line), we obtainC3/h=1.36​(15)​MHz​μ​m3C_{3}/h=1.36(15)\,\mathrm{MHz}\,\mu\mathrm{m}^{3}, with the corresponding shaded region indicating the1​σ1\sigmaconfidence interval.
We expect that this is slightly weaker than the theoretical estimate presented earlier for point-like particles due to the finite spatial extent of the particle wavefunctions[40].

The red data and corresponding model line show the behaviour when the molecule is prepared in the state|0⟩\ket{0}. In this case, we observe no significant blockade untilR≲0.5​μR\lesssim 0.5\,\mum, where the molecule is within the Rydberg-electron wavefunction.
Furthermore, this blockade is less robust, as small fluctuations inRRare now sufficient to break the blockade condition (see Methods).

The inset of Fig.2d demonstrates the state selectivity of the interaction for the states|N⟩\ket{N}withN∈[0,4]N\in[0,4]atR=0.9​(1)​μR=0.9(1)\,\mum.
Consistent with the resonance condition, we observe significant blockade only when the molecule is in the state|3⟩\ket{3}.

The strong state-selectivity of the blockade at distancesR≈1​μR\approx 1\,\mum enables several applications in the hybrid quantum system[3].
For the remainder of this work, we focus on two such applications.
First, we demonstrate non-destructive readout of the molecular state, in which the state of the molecule is inferred without requiring a change in its internal state.
Second, we show how this interaction can be used to realise coherent spin-exchange and generate, for the first time, entanglement between a neutral atom and a polar molecule.

## Molecular-state readout

We use the strong state dependence of the atom–molecule interaction to realise atom-mediated readout of the molecular state. This is highly advantageous because state-resolved molecular detection is generally destructive, relying either on dissociation of the molecule[56,58]or photon scattering that can alter the internal state[59,60,61]. By mapping specific molecular populations to the resonant state, we selectively blockade the Rydberg excitation of an auxiliary atom. Measuring the atomic state therefore infers the molecular state without direct interrogation, leaving the molecule intact for subsequent quantum operations.Figure 3:Molecular readout with a Rydberg atom.a, Schematic of the experimental sequence used to map the state of a molecule onto an atom. First, we drive a Rabi oscillation on the molecular transition|0⟩→|1⟩\ket{0}\to\ket{1}to prepare it in a superposition. Then, we map the population of one of the component states (here,|1⟩\ket{1}) to the resonant state|3⟩\ket{3}with a series of microwaveπ\pipulses. Next, we attempt to resonantly excite the atom to the Rydberg state. This is blockaded state selectively and any Rydberg atoms are ejected from the tweezer. Finally, the molecule is returned to its original state and we readout both particles.b, Rabi oscillations on the molecular transition|0⟩→|1⟩\ket{0}\to\ket{1}. We show the relative occupations of the two states.c, Atom-survival probability after this detection scheme. The shaded regions indicate the contrast of the Rydberg excitation when we prepare no molecules.d, The correlations between the molecular population and atom recovery and loss. The left panel shows data fromτ=65​μ\tau=65\,\mus (highlighted point), the right panel shows data from the whole Rabi oscillation. The correlations are as expected, with the largest infidelity being recovery of the atom when the molecule is in|0⟩\ket{0}.
In all panels, the error bars show the1​σ1\sigmaconfidence intervals and, on average, there are 51 experimental shots per data point.

Here, we focus on a strong, projective measurement of the molecular state, establishing an essential capability for hybrid quantum systems. By mapping the molecular state to an auxiliary atom, we realise the non-destructive readout required to extract error syndromes for quantum error correction[62,28]and to probe complex many-body observables, including out-of-time-order correlators[63]. In addition to enabling high-fidelity readout, projective measurements of this kind provide the basis for heralded state preparation[1]and measurement-based quantum information protocols[64]in hybrid atom-molecule systems.

We demonstrate this readout technique by tracking a Rabi oscillation on the molecular transition|0⟩→|1⟩\ket{0}\rightarrow\ket{1}. The experimental sequence is shown in Fig.3a.
First, the molecular population is driven using a microwave pulse of variable durationτ\tau.
The resulting state populations are shown in Fig.3b and are extracted by mapping the molecular state onto distinct configurations of the constituent atoms following dissociation of the molecule at the end of the sequence[56](see Methods).

To perform the atom-mediated readout, we map the population of one molecular state onto the state which causes Rydberg blockade.
This readout sequence is shown in the highlighted region of Fig.3a.
We transfer molecular population in the state|1⟩\ket{1}to the state|3⟩\ket{3}using two additional microwave pulses (see Methods).
Then, we apply aπ\pipulse on the bare-atom transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}atR=1.1​(1)​μR=1.1(1)\,\mum.
As in Fig.2, this excitation is blockaded when the molecule occupies|3⟩\ket{3}, but proceeds freely when it remains in|0⟩\ket{0}.
Following this, we transfer population in|3⟩\ket{3}back to|1⟩\ket{1}.
This protocol implements the conditional mapping|0;5​s⟩→|0;83​d⟩\ket{0;5\mathrm{s}}\rightarrow\ket{0;83\mathrm{d}}and|1;5​s⟩→|1;5​s⟩\ket{1;5\mathrm{s}}\rightarrow\ket{1;5\mathrm{s}}.
Ejection of the Rydberg atom maps these outcomes to atomic loss and survival, respectively.

Figure3c shows the resulting atom-survival probability.
The signal closely follows the population of the molecular state|1⟩\ket{1}, demonstrating successful mapping of the molecular state onto the atom.
This is highlighted in Fig.3d which shows the correlations between the measured molecular state and the atomic outcome forτ=65​μ\tau=65\,\mus (left) and allτ\tau(right).
From the fit in Fig.3c, we extract the fidelity of atom-mediated molecular readout asFmeas=12​(F0|0+F1|1)=0.91​(1)F_{\mathrm{meas}}=\frac{1}{2}(F_{0|0}+F_{1|1})=0.91(1), whereFN|NF_{N|N}is the probability of inferring from the atomic measurement that the molecule is in state|N⟩\ket{N}, given that it was prepared in|N⟩\ket{N}. Specifically, we obtainF0|0=0.86​(2)F_{0|0}=0.86(2)andF1|1=0.95​(2)F_{1|1}=0.95(2).
These fidelities are primarily limited by imperfections in atomic control with the dominant error corresponding to atom survival when the molecule occupies|0⟩\ket{0}, as shown in Fig.3d.
This is consistent with the imperfect Rydberg excitation that we observe in the absence of a molecule, indicated by the grey shaded regions in Fig.3c.
These technical imperfections can be mitigated, and the detection fidelities substantially improved, by adopting the high-fidelity optical control routinely demonstrated in modern neutral-atom processors.
Additionally, from the fit in Fig.3b, we determine that the probability of the atomic measurement inducing a molecular bit flip is consistent with zero (see Methods).
The Rydberg-excitation light induces molecular loss with a probability of9​(6)%9(6)\%.
This constitutes an erasure error that is removed via postselection and could be eliminated in future implementations (see Methods).

## Spin exchange and entanglementFigure 4:Dipolar spin-exchange and entanglement of an atom and molecule.a, Experimental sequence (see text) that we use to observe atom–molecule spin exchange.b, Relative populations of the states|4⟩​|83​d⟩\ket{4}\ket{83\mathrm{d}}(purple) and|3⟩​|84​p⟩\ket{3}\ket{84\mathrm{p}}(black) with varying spin-exchange durationτ\tau. The different panels show different interparticle separations. We perform a global fit to extract the parameters given in the text.c, Entanglement of the atom and molecule using state-selective dipolar interactions. Upper: experimental sequence, as described in the text. Lower: Entanglement-mediated phase transfer between particles. We prepare the maximally entangled Bell state|Ψ⟩\ket{\Psi}by performing aCNOTgate on the atom with the excitation light while the molecule is in the state(|2⟩−i​|3⟩)/2(\ket{2}-i\ket{3})/\sqrt{2}. We verify this entanglement by disentangling the particles with an atomicπ\pipulse of varying phaseφ\varphi. When the particles are entangled, this phase is coherently mapped to the molecular state (large panel). In contrast, when the molecule are prepared in the state(|1⟩−i​|2⟩)/2(\ket{1}-i\ket{2})/\sqrt{2}, there are no resonant interactions. Therefore, we do not entangle the particles and the molecule does not acquire the phase of the atomic pulse (small panel).
In both cases, the atom and molecule are prepared atR=1.1​μR=1.1\,\mum.
In all panels, the error bars show the1​σ1\sigmaconfidence intervals and, on average, there are 107 experimental shots per data point.

Next, we engineer coherent dipolar spin exchange between an atom and a molecule.
For this, we implement the sequence shown in Fig.4a.
First, we prepare the system in the pair state|4;83​d⟩\ket{4;83\mathrm{d}}(green) by preparing the molecule in|4⟩\ket{4}and driving aπ\pipulse on the Rydberg transition.
This pair state is non-resonant, so the atomic excitation can proceed freely.
Spin-exchange dynamics are initiated by driving a microwaveπ\pipulse to the pair state|4;84​p⟩\ket{4;84\mathrm{p}}with a Rabi frequencyΩMW\Omega_{\mathrm{MW}}that is much greater than the dipolar interaction with the resonantly coupled|3;83​d⟩\ket{3;83\mathrm{d}}(i.e.ℏ​ΩMW≫|U​(R)|\hbar\Omega_{\mathrm{MW}}\gg|U(R)|).
In terms of the interacting eigenstates, this initialises the system in|4;84​p⟩=12​(|+⟩−|−⟩)\ket{4;84\mathrm{p}}=\frac{1}{\sqrt{2}}(\ket{+}-\ket{-}).
The relative phase of this superposition then evolves with time due to the different eigenenergies of|+⟩\ket{+}and|−⟩\ket{-}.
We map this onto an oscillation in the populations by applying a second atomic microwaveπ\pipulse after timeτ\tauthat also freezes the dynamics prior to readout.

With this protocol,
we ideally prepare the state|ψ​(τ)⟩=cos⁡(τ​Δ​(R)ℏ)​|4;83​d⟩−i​sin⁡(τ​Δ​(R)ℏ)​|3;84​p⟩.\ket{\psi(\tau)}=\cos\left(\frac{\tau\Delta(R)}{\hbar}\right)\ket{4;83\mathrm{d}}-i\sin\left(\frac{\tau\Delta(R)}{\hbar}\right)\ket{3;84\mathrm{p}}.

Here,Δ​(R)\Delta(R)is the energy difference between the states|+⟩\ket{+}and|−⟩\ket{-}. It follows that the maximally entangled state,12​(|4;83​d⟩−i​|3;84​p⟩)\frac{1}{\sqrt{2}}(\ket{4;83\mathrm{d}}-i\ket{3;84\mathrm{p}}), is prepared whenτ=h/(4​Δ​(R))\tau=h/(4\Delta(R)).

Fig.4b shows the resulting dynamics for several values ofRR.
We plot the relative populations of the states|4;83​d⟩\ket{4;83\mathrm{d}}and|3;84​p⟩\ket{3;84\mathrm{p}}and ignore other pair states: this corrects for technical errors like imperfect state preparation (see Methods).
Clear oscillations are observed with a rate that depends on the distanceRR, demonstrating coherent spin exchange between the atom and molecule.

We fit the data using a global Monte Carlo model that accounts for shot-to-shot fluctuations in interparticle separation and detuning from resonance. In the model, we sample the separationRRfrom a Gaussian distribution with meanR¯\bar{R}and widthσR\sigma_{R}, and the detuningδ\deltafrom a Gaussian distribution with meanδ¯\bar{\delta}and widthσδ\sigma_{\delta}.
We independently measureR¯\bar{R}(see Methods) and extract parametersσR=0.36​(2)​μ\sigma_{R}=0.36(2)\,\mum,δ¯=0.29​(2)​MHz\bar{\delta}=0.29(2)\,\mathrm{MHz}, andσδ=0.12​(4)​MHz\sigma_{\delta}=0.12(4)\,\mathrm{MHz}.
We attribute the separation fluctuations to the ejection of the Rydberg atom and finite wavefunction spreads of the particles.
The detuning fluctuations are attributed to magnetic-field noise (see Methods).

Whilst the spin-exchange sequence can, in principle, generate maximally entangled states of the atom and molecule, in practice its performance is limited by noise on the interaction strength.
Proposals using quantum optimal control[65]to mitigate these effects have been developed for dipolar systems[66,67,68,69,70,71,72], but they are challenging to implement here because we cannot currently perform single-particle operations on the molecule while the atom occupies a Rydberg state.
This is because the Rydberg atom has a much larger electric dipole moment than the molecule, leading to strong off-resonant driving of the atom when attempting to address the molecule.

A more robust route to entanglement is provided by the blockade mechanism, which requires only that|U​(R)|≳ℏ​ΩRyd|U(R)|\gtrsim\hbar\Omega_{\mathrm{Ryd}}. The trade-off is the entangling operation is slower.
We implement such an approach using the protocol shown in the top panel of Fig.4c.
We first prepare the system in the state12​(|2;5​s⟩−i​|3;5​s⟩)\frac{1}{\sqrt{2}}(\ket{2;5\mathrm{s}}-i\ket{3;5\mathrm{s}})by applying a sequence of microwave pulses to the molecule atR=1.1​(1)​μR=1.1(1)\,\mum.
We then drive an atomicπ\pipulse which is resonant when the molecule occupies|2⟩\ket{2}but blockaded when it occupies|3⟩\ket{3}.
Ideally, this implements a controlled-NOT operation and prepares the Bell state|Ψ⟩=12​(|2;83​d⟩−i​|3;5​s⟩),\ket{\Psi}=\frac{1}{\sqrt{2}}\left(\ket{2;83\mathrm{d}}-i\ket{3;5\mathrm{s}}\right),

which is a maximally entangled state of the atom and molecule.

Full state tomography would require single-particle rotations that overcome the blockade condition (ℏ​ΩRyd≳|U​(R)|\hbar\Omega_{\mathrm{Ryd}}\gtrsim|U(R)|), which are not presently available with our Rydberg-excitation system (see Methods). Instead, we probe the coherence generated during Bell-state preparation through coherent phase transfer between the atom and molecule.

Starting from|Ψ⟩\ket{\Psi}, we apply a second atomicπ\pipulse with controllable phaseϕ\phirelative to the first pulse (we take the phase of the first pulse to be zero).
This maps the state|Ψ⟩\ket{\Psi}to12​(ei​ϕ​|2;5​s⟩−i​|3;5​s⟩)\frac{1}{\sqrt{2}}\left(e^{i\phi}\ket{2;5\mathrm{s}}-i\ket{3;5\mathrm{s}}\right),
transferring the phase of the atomic drive onto the molecular superposition. A molecularπ/2\pi/2pulse then converts this phase into populations that are measured via state-selective molecular readout.
Then varying the phaseϕ\phiwe expect to observe Ramsey-type oscillations in the molecular populations.

The results of this measurement are shown in the central panel of Fig.4c.
We postselect on the recovery of both the atom and molecule, excluding the 22% of experimental runs in which imperfect transfer on the Rydberg transition resulted in atom loss.
The measured fringe contrast is0.57​(1)0.57(1).
Observation of these oscillations demonstrates coherent transfer of phase information between the atom and molecule.
This requires coherence between the two components of the Bell state.
Therefore, the measured contrast provides a measurement of the Bell-state coherence.
From this, we estimate a SPAM-corrected entanglement fidelity of0.77​(3)0.77(3)and an uncorrected fidelity of0.52​(2)0.52(2), most likely limited by imperfections in the atomic and molecular excitations and decoherence during the sequence (see Methods). The grey shaded region indicates the contrast obtained when the same pulse sequence is applied with the Rydberg-excitation light detuned from resonance, and highlights the fidelity of the molecular microwave transfers.

To verify that the observed fringes originate from the state-dependent blockade, we repeat the experiment with the particles initially prepared in the superposition12​(|1;5​s⟩−i​|2;5​s⟩)\frac{1}{\sqrt{2}}(\ket{1;5\mathrm{s}}-i\ket{2;5\mathrm{s}}), for which neither molecular component is resonantly coupled to the atom. In this case the atomic pulse sequence imparts only a global phase,ei​ϕ​12​(|1;5​s⟩−i​|2;5​s⟩)e^{i\phi}\frac{1}{\sqrt{2}}(\ket{1;5\mathrm{s}}-i\ket{2;5\mathrm{s}}),
which cannot affect any observable. As shown in the lower panel of Fig.4c, no phase-dependent oscillations are observed.
The observation of fringes only in the resonant case confirms that the measured coherence originates from the interaction-mediated atom-molecule entangled state.

## Outlook

We have engineered coherent dipolar interactions between a single ultracold atom in a Rydberg state and a single ultracold polar molecule in the electronic and vibrational ground state.
Using these interactions, we observed strong, state-dependent blockade of the atomic Rydberg transition.
Exploiting this effect, we have realised what is, to our knowledge, the first observation of coherent spin-exchange between a neutral atom and a polar molecule, performed readout of the molecular state using an auxiliary atom and generated an entangled atom-molecule pair.

Looking forward, the performance of this hybrid architecture can be rapidly advanced by addressing its primary bottleneck: the atomic operations. State-of-the-art neutral atom processors routinely achieve infidelities approaching0.1%0.1\%[73], two orders of magnitude lower than those reported here. Adopting these established capabilities, including using an atomic qubit in the ground hyperfine manifold, will significantly improve the performance. Crucially, this ground-state encoding will facilitate mid-circuit measurement protocols where the auxiliary atomic qubit can be read out, reset, and reused[74]for repetitive interrogation of the molecular state. In addition, the spectrally distinct transitions enable global single-qubit operations, while addressing tweezers provide independent, local control[56]. Finally, implementing quantum optimal control promises to further enhance the robustness of the atom-molecule blockade.

Ultimately, the capabilities demonstrated here unlock a broad range of applications across quantum science. Foremost, entanglement of atoms and molecules in a scalable optical tweezer platform establishes a clear path towards interfacing neutral-atom processors with molecular systems. This hybrid platform promises to exploit the long coherence times and dense information encoding natively available in molecules[12]. At the single-particle level, our auxiliary-atom-based measurement could be extended to the multiplexed detection of multiple internal states, an essential capability for leveraging molecular qudits in quantum information processing[35]and offering a new tool to probe molecular quantum simulators[75]. Scaling up, resonant dipolar interactions can be exploited to mediate fast molecule-molecule gates via Rydberg atoms[3,5,4], bypassing the traditional limitations of weak molecular dipole moments. This provides a robust route to engineering macroscopic entangled molecular states[7], offering a highly sensitive resource for quantum-enhanced metrology and precision sensing[76,77,40,41].

## References
- Wallquistet al.[2009]M. Wallquist, K. Hammerer, P. Rabl, M. Lukin, and P. Zoller, Hybrid quantum devices and quantum engineering,Phys. Scr.2009, 014001 (2009).
- Kurizkiet al.[2015]G. Kurizki, P. Bertet, Y. Kubo, K. Mølmer, D. Petrosyan, P. Rabl, and J. Schmiedmayer, Quantum technologies with hybrid systems,Proc. Natl. Acad. Sci.112, 3866 (2015).
- Kuznetsovaet al.[2011]E. Kuznetsova, S. T. Rittenhouse, H. R. Sadeghpour, and S. F. Yelin, Rydberg atom mediated polar molecule interactions: a tool for molecular-state conditional quantum gates and individual addressability,Phys. Chem. Chem. Phys.13, 17115 (2011).
- Wanget al.[2022]K. Wang, C. P. Williams, L. R. B. Picard, N. Y. Yao, and K.-K. Ni, Enriching the quantum toolbox of ultracold molecules with Rydberg atoms,PRX Quantum3, 030339 (2022).
- Zhang and Tarbutt [2022]C. Zhang and M. R. Tarbutt, Quantum computation in a hybrid array of molecules and Rydberg atoms,PRX Quantum3, 030340 (2022).
- Baiet al.[2026]Y.-H. Bai, Y. Wei, C. Zhang, W. Li, and X.-Q. Shao,Multipartite controlled-NOT gates using molecules and Rydberg atoms(2026),arXiv:2603.29349 [quant-ph].
- Zhanget al.[2026]C. Zhang, S. Murciano, N. Tantivasadakarn, and R. Finkelstein,Quantum logic control and entanglement in hybrid atom-molecule arrays(2026),arXiv:2602.12909 [quant-ph].
- Saffmanet al.[2010]M. Saffman, T. G. Walker, and K. Mølmer, Quantum information with Rydberg atoms,Rev. Mod. Phys.82, 2313 (2010).
- Browaeys and Lahaye [2020]A. Browaeys and T. Lahaye, Many-body physics with individually controlled Rydberg atoms,Nat. Phys.16, 132 (2020).
- Wuet al.[2021]X. Wu, X. Liang, Y. Tian, F. Yang, C. Chen, Y.-C. Liu, M. K. Tey, and L. You, A concise review of Rydberg atom based quantum computation and quantum simulation*,Chin. Phys. B30, 020305 (2021).
- Defenuet al.[2023]N. Defenu, T. Donner, T. Macrì, G. Pagano, S. Ruffo, and A. Trombettoni, Long-range interacting quantum systems,Rev. Mod. Phys.95, 035002 (2023).
- Cornishet al.[2024]S. L. Cornish, M. R. Tarbutt, and K. R. A. Hazzard, Quantum computation and quantum simulation with ultracold molecules,Nat. Phys.20, 730 (2024).
- Petitjeanet al.[1986]L. Petitjean, F. Gounand, and P. R. Fournier, Collisions of rubidium Rydberg-state atoms with ammonia,Phys. Rev. A33, 143 (1986).
- Zhuet al.[2025]L. Zhu, J. Luke, R. Shaham, Y.-X. Liu, and K.-K. Ni, Probing dipolar interactions between Rydberg atoms and ultracold polar molecules,Phys. Rev. Lett.135, 153001 (2025).
- Gawlas and Hogan [2020]K. Gawlas and S. D. Hogan, Rydberg-state-resolved resonant energy transfer in cold electric-field-controlled intrabeam collisions of NH3with Rydberg He atoms,J. Phys. Chem. Lett.11, 83 (2020).
- Zou and Hogan [2022]J. Zou and S. D. Hogan, Probing van der Waals interactions and detecting polar molecules by Förster-resonance energy transfer with Rydberg atoms at temperatures below 100 mK,Phys. Rev. A106, 043111 (2022).
- Kuznetsovaet al.[2016]E. Kuznetsova, S. T. Rittenhouse, H. R. Sadeghpour, and S. F. Yelin, Rydberg-atom-mediated nondestructive readout of collective rotational states in polar-molecule arrays,Phys. Rev. A94, 032325 (2016).
- Zeppenfeld [2017]M. Zeppenfeld, Nondestructive detection of polar molecules via Rydberg atoms,EPL118, 13002 (2017).
- Jarisch and Zeppenfeld [2018]F. Jarisch and M. Zeppenfeld, State resolved investigation of Förster resonant energy transfer in collisions between polar molecules and Rydberg atoms,New J. Phys.20, 113044 (2018).
- Patschet al.[2022]S. Patsch, M. Zeppenfeld, and C. P. Koch, Rydberg atom-enabled spectroscopy of polar molecules via Förster resonance energy transfer,J. Phys. Chem. Lett.13, 10728 (2022).
- Younget al.[2026]J. T. Young, K.-K. Ni, and A. V. Gorshkov,Simultaneous nondestructive measurement of many polar molecules using Rydberg atoms(2026),arXiv:2601.08921 [quant-ph].
- Kuznetsovaet al.[2018]E. Kuznetsova, S. T. Rittenhouse, I. I. Beterov, M. O. Scully, S. F. Yelin, and H. R. Sadeghpour, Effective spin-spin interactions in bilayers of Rydberg atoms and polar molecules,Phys. Rev. A98, 043609 (2018).
- Dobrzyniecki and Tomza [2023]J. Dobrzyniecki and M. Tomza, Quantum simulation of the central spin model with a Rydberg atom and polar molecules in optical tweezers,Phys. Rev. A108, 052618 (2023).
- Zenget al.[2017]Y. Zeng, P. Xu, X. He, Y. Liu, M. Liu, J. Wang, D. J. Papoular, G. V. Shlyapnikov, and M. Zhan, Entangling two individual atoms of different isotopes via Rydberg blockade,Phys. Rev. Lett.119, 160502 (2017).
- Singhet al.[2023]K. Singh, C. E. Bradley, S. Anand, V. Ramesh, R. White, and H. Bernien, Mid-circuit correction of correlated phase errors using an array of spectator qubits,Science380, 1265 (2023).
- Anandet al.[2024]S. Anand, C. E. Bradley, R. White, V. Ramesh, K. Singh, and H. Bernien, A dual-species Rydberg array,Nat. Phys.20, 1744 (2024).
- Wanget al.[2026]Y. Wang, R. Cimmino, K. Wang, S. Lopez, J. Li, J. M. Koh, J. N. Hallén, A. Matthies, N. Y. Yao, and K.-K. Ni,Multi-qubit stabilizer readout on a dual-species Rydberg array(2026),arXiv:2605.10924 [quant-ph].
- Mileset al.[2026]J. Miles, M. T. Lichtman, A. M. Scott, J. Scott, S. A. Norrell, M. J. Bedalov, D. A. Belknap, D. C. Cole, S. Y. Eubanks, M. Gillette, P. Gokhale, J. Goldwin, M. Iliev, R. A. Jones, K. W. Kuper, D. Mason, P. T. Mitchell, J. D. Murphree, N. A. Neff-Mallon, T. W. Noel, A. G. Radnaev, I. V. Vinogradov, and M. Saffman,Qubit syndrome measurements with a high fidelity Rb-Cs Rydberg gate(2026),arXiv:2603.13492 [quant-ph].
- Homeieret al.[2023]L. Homeier, A. Bohrdt, S. Linsel, E. Demler, J. C. Halimeh, and F. Grusdt, Realistic scheme for quantum simulation ofℤ2{{\mathbb{Z}}}_{2}lattice gauge theories with dynamical matter in (2 + 1)D,Commun. Phys.6, 127 (2023).
- Chepiga [2024]N. Chepiga, Tunable quantum criticality in multicomponent Rydberg arrays,Phys. Rev. Lett.132, 076505 (2024).
- Cesa and Pichler [2023]F. Cesa and H. Pichler, Universal quantum computation in globally driven Rydberg atom arrays,Phys. Rev. Lett.131, 170601 (2023).
- Manetschet al.[2025]H. J. Manetsch, G. Nomura, E. Bataille, X. Lv, K. H. Leung, and M. Endres, A tweezer array with 6,100 highly coherent atomic qubits,Nature647, 60 (2025).
- Bluvsteinet al.[2022]D. Bluvstein, H. Levine, G. Semeghini, T. T. Wang, S. Ebadi, M. Kalinowski, A. Keesling, N. Maskara, H. Pichler, M. Greiner, V. Vuletić, and M. D. Lukin, A quantum processor based on coherent transport of entangled atom arrays,Nature604, 451 (2022).
- Adamset al.[2019]C. S. Adams, J. D. Pritchard, and J. P. Shaffer, Rydberg atom quantum technologies,J. Phys. B53, 012002 (2019).
- Sawantet al.[2020]R. Sawant, J. A. Blackmore, P. D. Gregory, J. Mur-Petit, D. Jaksch, J. Aldegunde, J. M. Hutson, M. R. Tarbutt, and S. L. Cornish, Ultracold polar molecules as qudits,New J. Phys.22, 013027 (2020).
- Parket al.[2017]J. W. Park, Z. Z. Yan, H. Loh, S. A. Will, and M. W. Zwierlein, Second-scale nuclear spin coherence time of ultracold23Na40K molecules,Science357, 372 (2017).
- Gregoryet al.[2021]P. D. Gregory, J. A. Blackmore, S. L. Bromley, J. M. Hutson, and S. L. Cornish, Robust storage qubits in ultracold polar molecules,Nat. Phys.17, 1149 (2021).
- Burcheskyet al.[2021]S. Burchesky, L. Anderegg, Y. Bao, S. S. Yu, E. Chae, W. Ketterle, K.-K. Ni, and J. M. Doyle, Rotational coherence times of polar molecules in optical tweezers,Phys. Rev. Lett.127, 123202 (2021).
- Gregoryet al.[2024]P. D. Gregory, L. M. Fernley, A. L. Tao, S. L. Bromley, J. Stepp, Z. Zhang, S. Kotochigova, K. R. A. Hazzard, and S. L. Cornish, Second-scale rotational coherence and dipolar interactions in a gas of ultracold polar molecules,Nat. Phys.20, 415 (2024).
- Ruttleyet al.[2025]D. K. Ruttley, T. R. Hepworth, A. Guttridge, and S. L. Cornish, Long-lived entanglement of molecules in magic-wavelength optical tweezers,Nature637, 827 (2025).
- Hepworthet al.[2025]T. R. Hepworth, D. K. Ruttley, F. von Gierke, P. D. Gregory, A. Guttridge, and S. L. Cornish, Long-lived multilevel coherences and spin-1 dynamics encoded in the rotational states of ultracold molecules,Nat. Commun.16, 7131 (2025).
- Baoet al.[2023]Y. Bao, S. S. Yu, L. Anderegg, E. Chae, W. Ketterle, K.-K. Ni, and J. M. Doyle, Dipolar spin-exchange and entanglement between molecules in an optical tweezer array,Science382, 1138 (2023).
- Hollandet al.[2023a]C. M. Holland, Y. Lu, and L. W. Cheuk, On-demand entanglement of molecules in a reconfigurable optical tweezer array,Science382, 1143 (2023a).
- Picardet al.[2025]L. R. B. Picard, A. J. Park, G. E. Patenotte, S. Gebretsadkan, D. Wellnitz, A. M. Rey, and K.-K. Ni, Entanglement and iSWAP gate between molecular qubits,Nature637, 821 (2025).
- Luet al.[2026]Y. Lu, C. M. Holland, C. L. Welsh, X.-Y. Chen, and L. W. Cheuk,Probing coherent many-body spin dynamics in a molecular tweezer array quantum simulator(2026),arXiv:2603.19090 [cond-mat.quant-gas].
- Hollandet al.[2026]C. M. Holland, C. L. Welsh, Y. Lu, D. Wellnitz, X.-Y. Chen, A. M. Rey, and L. W. Cheuk,Creating and probing spin-squeezed states of molecules(2026),arXiv:2606.02500 [physics.atom-ph].
- Yuet al.[2026]S. S. Yu, A. Periwal, J. You, Z. Liu, Q. Lyu, Y. Cho, L. Anderegg, E. Chae, and J. M. Doyle,High-fidelity entanglement of polar molecules by dynamic geometric control(2026),arXiv:2607.13008 [physics.atom-ph].
- Zhaoet al.[2012]B. Zhao, A. W. Glaetzle, G. Pupillo, and P. Zoller, Atomic Rydberg reservoirs for polar molecules,Phys. Rev. Lett.108, 193007 (2012).
- Huber and Büchler [2012]S. D. Huber and H. P. Büchler, Dipole-interaction-mediated laser cooling of polar molecules to ultracold temperatures,Phys. Rev. Lett.108, 193006 (2012).
- Zhanget al.[2024]C. Zhang, S. T. Rittenhouse, T. V. Tscherbul, H. R. Sadeghpour, and N. R. Hutzler, Sympathetic cooling and slowing of molecules with Rydberg atoms,Phys. Rev. Lett.132, 033001 (2024).
- Rittenhouse and Sadeghpour [2010]S. T. Rittenhouse and H. R. Sadeghpour, Ultracold giant polyatomic Rydberg molecules: Coherent control of molecular orientation,Phys. Rev. Lett.104, 243002 (2010).
- Rittenhouseet al.[2011]S. T. Rittenhouse, M. Mayle, P. Schmelcher, and H. R. Sadeghpour, Ultralong-range polyatomic Rydberg molecules formed by a polar perturber,J. Phys. B44, 184005 (2011).
- González-Férezet al.[2020]R. González-Férez, S. T. Rittenhouse, P. Schmelcher, and H. R. Sadeghpour, A protocol to realize triatomic ultralong range Rydberg molecules in an ultracold KRb gas,J. Phys. B53, 074002 (2020).
- Guttridgeet al.[2023]A. Guttridge, D. K. Ruttley, A. C. Baldock, R. González-Férez, H. R. Sadeghpour, C. S. Adams, and S. L. Cornish, Observation of Rydberg blockade due to the charge-dipole interaction between an atom and a polar molecule,Phys. Rev. Lett.131, 013401 (2023).
- Walker and Saffman [2005]T. G. Walker and M. Saffman, Zeros of Rydberg–Rydberg Föster interactions,J. Phys. B38, S309 (2005).
- Ruttleyet al.[2024]D. K. Ruttley, A. Guttridge, T. R. Hepworth, and S. L. Cornish, Enhanced quantum control of individual ultracold molecules using optical tweezer arrays,PRX Quantum5, 020333 (2024).
- Aldegundeet al.[2008]J. Aldegunde, B. A. Rivington, P. S. Żuchowski, and J. M. Hutson, Hyperfine energy levels of alkali-metal dimers: Ground-state polar molecules in electric and magnetic fields,Phys. Rev. A78, 033434 (2008).
- Picardet al.[2024]L. R. B. Picard, G. E. Patenotte, A. J. Park, S. F. Gebretsadkan, and K.-K. Ni, Site-selective preparation and multistate readout of molecules in optical tweezers,PRX Quantum5, 020344 (2024).
- Anderegget al.[2019]L. Anderegg, L. W. Cheuk, Y. Bao, S. Burchesky, W. Ketterle, K.-K. Ni, and J. M. Doyle, An optical tweezer array of ultracold molecules,Science365, 1156 (2019).
- Hollandet al.[2023b]C. M. Holland, Y. Lu, and L. W. Cheuk, Bichromatic imaging of single molecules in an optical tweezer array,Phys. Rev. Lett.131, 053202 (2023b).
- Vilaset al.[2024]N. B. Vilas, P. Robichaud, C. Hallas, G. K. Li, L. Anderegg, and J. M. Doyle, An optical tweezer array of ultracold polyatomic molecules,Nature628, 282 (2024).
- Bluvsteinet al.[2024]D. Bluvstein, S. J. Evered, A. A. Geim, S. H. Li, H. Zhou, T. Manovitz, S. Ebadi, M. Cain, M. Kalinowski, D. Hangleiter, J. P. Bonilla Ataides, N. Maskara, I. Cong, X. Gao, P. Sales Rodriguez, T. Karolyshyn, G. Semeghini, M. J. Gullans, M. Greiner, V. Vuletić, and M. D. Lukin, Logical quantum processor based on reconfigurable atom arrays,Nature626, 58 (2024).
- Miet al.[2021]X. Mi, P. Roushan, C. Quintana, S. Mandrà, J. Marshall, C. Neill, F. Arute, K. Arya, J. Atalaya, R. Babbush, J. C. Bardin, R. Barends, J. Basso, A. Bengtsson, S. Boixo, A. Bourassa, M. Broughton, B. B. Buckley, D. A. Buell, B. Burkett, N. Bushnell, Z. Chen, B. Chiaro, R. Collins, W. Courtney, S. Demura, A. R. Derk, A. Dunsworth, D. Eppens, C. Erickson, E. Farhi, A. G. Fowler, B. Foxen, C. Gidney, M. Giustina, J. A. Gross, M. P. Harrigan, S. D. Harrington, J. Hilton, A. Ho, S. Hong, T. Huang, W. J. Huggins, L. B. Ioffe, S. V. Isakov, E. Jeffrey, Z. Jiang, C. Jones, D. Kafri, J. Kelly, S. Kim, A. Kitaev, P. V. Klimov, A. N. Korotkov, F. Kostritsa, D. Landhuis, P. Laptev, E. Lucero, O. Martin, J. R. McClean, T. McCourt, M. McEwen, A. Megrant, K. C. Miao,
M. Mohseni, S. Montazeri, W. Mruczkiewicz, J. Mutus, O. Naaman, M. Neeley, M. Newman, M. Y. Niu, T. E. O’Brien, A. Opremcak, E. Ostby, B. Pato, A. Petukhov, N. Redd, N. C. Rubin, D. Sank, K. J. Satzinger, V. Shvarts, D. Strain, M. Szalay, M. D. Trevithick, B. Villalonga, T. White, Z. J. Yao, P. Yeh, A. Zalcman, H. Neven, I. Aleiner, K. Kechedzhi, V. Smelyanskiy, and Y. Chen, Information scrambling in
quantum circuits,Science374, 1479 (2021).
- Wei [2021]T.-C. Wei, Measurement-based quantum computation, inOxford Research Encyclopedia of Physics, edited by B. Foster (Oxford University Press, Oxford, 2021).
- Werschnik and Gross [2007]J. Werschnik and E. K. U. Gross, Quantum optimal control theory,J. Phys. B40, R175 (2007).
- Goerzet al.[2011]M. H. Goerz, T. Calarco, and C. P. Koch, The quantum speed limit of optimal controlled phasegates for trapped neutral atoms,J. Phys. B44, 154011 (2011).
- Mülleret al.[2011]M. M. Müller, D. M. Reich, M. Murphy, H. Yuan, J. Vala, K. B. Whaley, T. Calarco, and C. P. Koch, Optimizing entangling quantum gates for physical systems,Phys. Rev. A84, 042315 (2011).
- Goerzet al.[2014]M. H. Goerz, E. J. Halperin, J. M. Aytac, C. P. Koch, and K. B. Whaley, Robustness of high-fidelity Rydberg gates with single-site addressability,Phys. Rev. A90, 032329 (2014).
- Hugheset al.[2020]M. Hughes, M. D. Frye, R. Sawant, G. Bhole, J. A. Jones, S. L. Cornish, M. R. Tarbutt, J. M. Hutson, D. Jaksch, and J. Mur-Petit, Robust entangling gate for polar molecules using magnetic and microwave fields,Phys. Rev. A101, 062308 (2020).
- Jandura and Pupillo [2022]S. Jandura and G. Pupillo, Time-optimal two- and three-qubit gates for Rydberg atoms,Quantum6, 712 (2022).
- Maet al.[2023]S. Ma, G. Liu, P. Peng, B. Zhang, S. Jandura, J. Claes, A. P. Burgers, G. Pupillo, S. Puri, and J. D. Thompson, High-fidelity gates and mid-circuit erasure conversion in an atomic qubit,Nature622, 279 (2023).
- Bergonzoniet al.[2025]M. Bergonzoni, S. Jandura, and G. Pupillo, iSWAP gate with polar molecules: Robustness criteria for entangling operations,Phys. Rev. A112, 032621 (2025).
- Everedet al.[2026]S. J. Evered, M. Xu, S. H. Li, A. A. Geim, J. P. B. Ataides, M. Kalinowski, D. Bluvstein, N. Maskara, C. Kokail, M. Greiner, V. Vuletić, and M. D. Lukin,High-fidelity entangling gates and nonlocal circuits with neutral atoms(2026),arXiv:2604.25987
[quant-ph].
- Finkelsteinet al.[2024]R. Finkelstein, R. B.-S. Tsai, X. Sun, P. Scholl, S. Direkci, T. Gefen, J. Choi, A. L. Shaw, and M. Endres, Universal quantum operations and ancilla-based read-out for tweezer clocks,Nature634, 321 (2024).
- Baranovet al.[2012]M. Baranov, M. Dalmonte, G. Pupillo, and P. Zoller, Condensed matter theory of dipolar quantum gases,Chem. Rev.112, 5012 (2012).
- DeMilleet al.[2024]D. DeMille, N. R. Hutzler, A. M. Rey, and T. Zelevinsky, Quantum sensing and metrology for fundamental physics with molecules,Nat. Phys.20, 741 (2024).
- Zhanget al.[2023]C. Zhang, P. Yu, A. Jadbabaie, and N. R. Hutzler, Quantum-enhanced metrology for molecular symmetry violation using decoherence-free subspaces,Phys. Rev. Lett.131, 193602 (2023).
- Spenceet al.[2022]S. Spence, R. V. Brooks, D. K. Ruttley, A. Guttridge, and S. L. Cornish, Preparation of87Rb and133Cs in the motional ground state of a single optical tweezer,New J. Phys.24, 103022 (2022).
- Tauschinskyet al.[2013]A. Tauschinsky, R. Newell, H. B. van Linden van den Heuvell, and R. J. C. Spreeuw, Measurement of87Rb Rydberg-state hyperfine splitting in a room-temperature vapor cell,Phys. Rev. A87, 042522 (2013).
- Gregoryet al.[2016]P. D. Gregory, J. Aldegunde, J. M. Hutson, and S. L. Cornish, Controlling the rotational and hyperfine state of ultracoldRb13387​Cs{}^{87}\mathrm{Rb}^{133}\mathrm{Cs}molecules,Phys. Rev. A94, 041403(R) (2016).
- González-Férezet al.[2015]R. González-Férez, H. R. Sadeghpour, and P. Schmelcher, Rotational hybridization, and control of alignment and orientation in triatomic ultralong-range Rydberg molecules,New J. Phys.17, 013021 (2015).
- Wallet al.[2015]M. L. Wall, K. R. A. Hazzard, and A. M. Rey, Quantum magnetism with ultracold molecules, inFrom Atomic to Mesoscale(World Scientific, Singapore, 2015) Chap. 1, pp. 3–37.
- Ravetset al.[2015]S. Ravets, H. Labuhn, D. Barredo, T. Lahaye, and A. Browaeys, Measurement of the angular dependence of the dipole-dipole interaction between two individual Rydberg atoms at a Förster resonance,Phys. Rev. A92, 020701(R) (2015).
- Wadenpfuhl and Adams [2025]K. Wadenpfuhl and C. S. Adams, Unraveling the structures in the van der Waals interactions of alkali-metal Rydberg atoms,Phys. Rev. A111, 062803 (2025).
- García-Garridoet al.[tion]J. M. García-Garrido, T. R. Hepworth, P. Fernández-Mayo, D. K. Ruttley, S. L. Cornish, and R. González-Férez, Resonant interaction between a Rydberg atom and a polar molecule: Theoretical description (in preparation).
- Brookset al.[2021]R. V. Brooks, S. Spence, A. Guttridge, A. Alampounti, A. Rakonjac, L. A. McArd, J. M. Hutson, and S. L. Cornish, Preparation of one87Rb and one133Cs atom in a single optical tweezer,New J. Phys.23, 065002 (2021).
- Ruttleyet al.[2023]D. K. Ruttley, A. Guttridge, S. Spence, R. C. Bird, C. R. Le Sueur, J. M. Hutson, and S. L. Cornish, Formation of ultracold molecules by merging optical tweezers,Phys. Rev. Lett.130, 223401 (2023).
- Barakhshanet al.[2022]P. Barakhshan, A. Marrs, A. Bhosale, B. Arora, R. Eigenmann, and M. S. Safronova,Portal for high-precision atomic data and computation (version 2.0), [Online] (2022).
- Blackmoreet al.[2020]J. A. Blackmore, R. Sawant, P. D. Gregory, S. L. Bromley, J. Aldegunde, J. M. Hutson, and S. L. Cornish, Controlling the ac Stark effect of RbCs with dc electric and magnetic fields,Phys. Rev. A102, 053316 (2020).
- Blackmoreet al.[2023]J. A. Blackmore, P. D. Gregory, J. M. Hutson, and S. L. Cornish, Diatomic-py: A Python module for calculating the rotational and hyperfine structure ofΣ1{}^{1}{\Sigma}molecules,Comput. Phys. Commun.282, 108512 (2023).
- Vexiauet al.[2017]R. Vexiau, D. Borsalino, M. Lepers, A. Orbán, M. Aymar, O. Dulieu, and N. Bouloufa-Maafa, Dynamic dipole polarizabilities of heteronuclear alkali dimers: optical response, trapping and control of ultracold molecules,Int. Rev. Phys. Chem.36, 709 (2017).
- Stefanazziet al.[2022]L. Stefanazzi, K. Treptow, N. Wilcer, C. Stoughton, C. Bradford, S. Uemura, S. Zorzetti, S. Montella, G. Cancelo, S. Sussman, A. Houck, S. Saxena, H. Arnaldi, A. Agrawal, H. Zhang, C. Ding, and D. I. Schuster, The QICK (Quantum Instrumentation Control Kit): Readout and control for qubits and detectors,Rev. Sci. Instrum.93, 044709 (2022).
- Raghuramet al.[2026]A. P. Raghuram, F. M. Blondell, J. M. Mortlock, B. P. Maddox, S. Dasgupta, H. A. J. Middleton-Spencer, K. R. A. Hazzard, H. M. Price, P. D. Gregory, and S. L. Cornish,Probing topological edge states in a molecular synthetic dimension(2026),arXiv:2604.00745 [physics.atom-ph].
- Weberet al.[2017]S. Weber, C. Tresp, H. Menke, A. Urvoy, O. Firstenberg, H. P. Büchler, and S. Hofferberth, Calculation of Rydberg interaction potentials,J. Phys. B50, 133001 (2017).
- Mögerleet al.[2026]J. Mögerle, F. Hummel, A. Keil, T. Legrand, E. J. Braun, H. Menke, J. King, B. Olmos, S. Hofferberth, H. P. Büchler, and S. Weber,Accurate modeling of Rydberg atoms and their interactions: Theory and implementation in PairInteraction(2026),arXiv:2605.14993 [physics.atom-ph].
- Steck [2025]D. A. Steck, Rubidium 87 D line data, available online athttp://steck.us/alkalidata(revision 2.3.4, 2025).
- Johanssonet al.[2012]J. Johansson, P. Nation, and F. Nori, QuTiP: An open-source Python framework for the dynamics of open quantum systems,Comput. Phys. Commun.183, 1760–1772 (2012).
- Johanssonet al.[2013]J. Johansson, P. Nation, and F. Nori, QuTiP 2: A python framework for the dynamics of open quantum systems,Comput. Phys. Commun.184, 1234 (2013).
- Lambertet al.[2026]N. Lambert, E. Giguère, P. Menczel, B. Li, P. Hopf, G. Suárez, M. Gali, J. Lishman, R. Gadhvi, R. Agarwal, A. Galicia, N. Shammah, P. Nation, J. R. Johansson, S. Ahmed, S. Cross,
A. Pitchford, and F. Nori, QuTiP 5: The quantum toolbox in Python,Phys. Rep.1153, 1 (2026).

## Methods

Atomic and molecular states
Throughout this work, we use shorthand notation for the atomic and molecular states of interest. Here, we define the full state labels used for both species.


Atomic states.The Rb atoms are initially prepared in the hyperfine state|5​s⟩≡|5​s1/2,f=2,mf=2⟩\ket{5\mathrm{s}}\equiv\ket{5\mathrm{s}_{1/2},f=2,m_{f}=2}.
Here, the electronic manifold of the valence electron is labelled by the quantum numbers|n​lj⟩\ket{nl_{j}}, wherennis the principal quantum number,llis the orbital angular momentum, andjjis the total angular momentum.
This state is populated by optical pumping at low magnetic field (4.78​G4.78\,\mathrm{G}) (Ref.[78]) after the ground-state molecule has been formed.

We excite the atom to the Rydberg state|83​d⟩≡|83​d5/2,mj=5/2⟩\ket{83\mathrm{d}}\equiv\ket{83\mathrm{d}_{5/2},m_{j}=5/2}by driving twoσ+\sigma^{+}transitions from|5​s⟩\ket{5\mathrm{s}}.
At the high magnetic fields that we use in this work, the Rydberg states are in the diamagnetic regime, with GHz-scale Zeeman shifts (see below).
We do not resolve their hyperfine structure because the relevant energy scale (∼100​kHz×h\sim 100\,\mathrm{kHz}\times h, see Ref.[79]) is smaller than the excitation linewidth.
The Rydberg excitation occurs via a virtual level which is blue-detuned from the intermediate state|6​p⟩≡|6​p3/2,mj=3/2⟩\ket{6\mathrm{p}}\equiv\ket{6\mathrm{p}_{3/2},m_{j}=3/2}(see Ref.[54]and below).

To engineer resonant atom–molecule interactions, we use the atomic transition|83​d⟩→|84​p⟩\ket{83\mathrm{d}}\rightarrow\ket{84\mathrm{p}}, where the state|84​p⟩≡|84​p3/2,mj=3/2⟩\ket{84\mathrm{p}}\equiv\ket{84\mathrm{p}_{3/2},m_{j}=3/2}.


Molecular states.We prepare RbCs molecules in the rovibrational and hyperfine ground state|0⟩≡|N=0,MN=0,mRb=3/2,mCs=7/2⟩\ket{0}\equiv\ket{N=0,M_{N}=0,m_{\mathrm{Rb}}=3/2,m_{\mathrm{Cs}}=7/2}.
Here,NNis the rotational quantum number andMNM_{N}is its projection, whilemam_{a}denotes the nuclear-spin projection of atomaa.

To engineer atom–molecule resonance, we rotationally excite the molecule with resonant microwave fields[56].
Electric-dipole selection rules permit transitions withΔ​N=±1\Delta N=\pm 1andΔ​MN=0,±1\Delta M_{N}=0,\pm 1, while the nuclear-spin projections remain unchanged.
Throughout this work, we drive onlyσ+\sigma^{+}transitions by using 10-kHz-scale Rabi frequencies which are small enough to prevent significant off-resonant excitation to other hyperfine states[56,40].
Therefore, the molecules remain within the stretched-state manifold|N⟩≡|N,MN=N,mRb=3/2,mCs=7/2⟩\ket{N}\equiv\ket{N,M_{N}=N,m_{\mathrm{Rb}}=3/2,m_{\mathrm{Cs}}=7/2}.
The energies of the rotational levels areEN≈Bv​N​(N+1)E_{N}\approx B_{v}N(N+1)withBv/h=490B_{v}/h=490\,MHz[80].
We make use of the excited rotational states|1⟩\ket{1},|2⟩\ket{2},|3⟩\ket{3}, and|4⟩\ket{4}.


Theoretical calculations
The hybrid Rydberg atom–molecule system is described by the Hamiltonian[51,81]H=HA+HM+Hcd.H=H_{\mathrm{A}}+H_{\mathrm{M}}+H_{\mathrm{cd}}.(1)

Here,HAH_{\mathrm{A}}andHMH_{\mathrm{M}}describe the internal structure of the atom and molecule, including their response to external electric and magnetic fields.HcdH_{\mathrm{cd}}accounts for the charge–dipole interaction between the molecular electric dipole moment𝒅M\boldsymbol{d}_{\mathrm{M}}and the electric field produced by the Rb ion core and the valence electron. It has the formHcd=−e4​π​ϵ0​(𝒅M⋅[𝑹|𝑹|3−𝑹−𝒓|𝑹−𝒓|3]),H_{\mathrm{cd}}=-\frac{e}{4\pi\epsilon_{0}}\left(\boldsymbol{d}_{\mathrm{M}}\cdot\left[\frac{\boldsymbol{R}}{|\boldsymbol{R}|^{3}}-\frac{\boldsymbol{R}-\boldsymbol{r}}{|\boldsymbol{R}-\boldsymbol{r}|^{3}}\right]\right),(2)

where𝒓\boldsymbol{r}and𝑹\boldsymbol{R}are measured from the Rb ionic core and denote, respectively, the Rydberg-electron position operator and the molecule position.
Within the Born–Oppenheimer approximation, the atom–molecule separation𝑹\boldsymbol{R}is treated as a fixed parameter, and by solving the time-independent Schrödinger equation associated with Hamiltonian (1) we obtain the Born–Oppenheimer potentials (BOP)U​(R)U(R). For each pair state, we reference each
potential curve to the corresponding uncoupled pair-state energy atR→∞R\rightarrow\infty.

The charge-resolved nature of the interaction Hamiltonian is particularly relevant
when the atomic core–molecule separationRRbecomes comparable to the spatial extent of the Rydberg-electron wavefunction.
In this regime, the full charge–dipole interaction is required to accurately describe this hybrid system as illustrated in Extended Data
Fig.1.
Panel a shows the BOP of the state|+⟩\ket{+}(orange line), as in Fig.1e, together with the BOP predicted by a point-dipole model with dipolar coefficientC3/h=1.79​MHz​μ​m3C_{3}/h=1.79\,\mathrm{MHz}\,\mu\mathrm{m}^{3}(black dashed line). Deviations between the two curves become apparent at short range,R≲1​μ​mR\lesssim 1\,\mu\mathrm{m}, where the point-dipole description breaks down as the molecule probes the extended Rydberg-electron charge distribution.
To characterise this crossover quantitatively, we extract a local effective power-law exponent and coefficient from the calculated BOPs withα​(R)=−d​log⁡|U​(R)|d​log⁡R,Cα​(R)=U​(R)​Rα​(R).\alpha(R)=-\frac{\mathrm{d}\log|U(R)|}{\mathrm{d}\log R},\qquad C_{\alpha}(R)=U(R)R^{\alpha(R)}.(3)

In panel b, we show the behaviour ofα​(R)\alpha(R). It deviates from the ideal point dipole–dipole interaction value of 3 asRRdecreases and the molecule probes the extended Rydberg-electron charge distribution.
The coefficientCα​(R)/hC_{\alpha}(R)/hvaries from1.51​MHz​μ​mα​(R)1.51\,\mathrm{MHz}\,\mu\mathrm{m}^{\alpha(R)}to2.59​MHz​μ​mα​(R)2.59\,\mathrm{MHz}\,\mu\mathrm{m}^{\alpha(R)}over the experimentally-relevant rangeR>0.5​μ​mR>0.5\,\mu\mathrm{m}, and tends to dipole–dipole limit of1.79​MHz​μ​m31.79\,\mathrm{MHz}\,\mu\mathrm{m}^{3}asR→∞R\to\infty.

For comparison to the non-resonant case, in Extended Data Fig.1a, we also plot|U​(R)||U(R)|for the state|0;83​d⟩\ket{0;83\mathrm{d}}(grey line).
Over the range shown here, the interaction between the molecule and atom is much weaker, and, as a consequence, the energy shift of this potential compared to its asymptotic limit is significantly smaller.

For the resonant states at experimental atom–molecule separationsR≳1​μ​mR\gtrsim 1\,\mu\mathrm{m},
the dipole–dipole interaction provides a good
approximation to the charge-dipole one.
WhenRRis larger than the characteristic spatial extent of the Rydberg-electron wavefunction, the instantaneous electric field generated by the Rydberg atom at𝑹\boldsymbol{R}is well approximated by that of a point dipole, and the interaction can be expressed in terms of effective transition dipole moments.
In the dipole–dipole limit, the interaction between the atom and molecule is[82]Vdd​(𝑹)=14​π​ϵ0​R3​[𝒅A⋅𝒅M−3​(𝒅A⋅𝒆R)​(𝒅M⋅𝒆R)],V_{\mathrm{dd}}(\boldsymbol{R})=\frac{1}{4\pi\epsilon_{0}R^{3}}\left[\boldsymbol{d}_{\mathrm{A}}\cdot\boldsymbol{d}_{\mathrm{M}}-3(\boldsymbol{d}_{\mathrm{A}}\cdot{\boldsymbol{e}_{R}})(\boldsymbol{d}_{\mathrm{M}}\cdot{\boldsymbol{e}_{R}})\right],(4)

where𝒅A\boldsymbol{d}_{\mathrm{A}}and𝒅M\boldsymbol{d}_{\mathrm{M}}are the dipole operators of the atom and molecule, and𝒆R≡𝑹/|𝑹|\boldsymbol{e}_{R}\equiv\boldsymbol{R}/|\boldsymbol{R}|is the interparticle unit vector.

In spherical coordinates, with the z-axis aligned along the quantisation axis, this can be written as[83,84]Vdd​(R,θ,φ)=14​π​ϵ0​R3​(ℳ0+ℳ1+ℳ2),V_{\mathrm{dd}}(R,\theta,\varphi)=\frac{1}{4\pi\epsilon_{0}R^{3}}\left(\mathcal{M}_{0}+\mathcal{M}_{1}+\mathcal{M}_{2}\right),(5)

whereθ\thetaandφ\varphiare the polar and azimuthal angles
of𝑹\boldsymbol{R}andℳ0\displaystyle\mathcal{M}_{0}=(1−3​cos2⁡θ)​[dMz​dAz+12​(dM+​dA−+dM−​dA+)],\displaystyle=(1-3\cos^{2}\theta)\,\left[d_{\mathrm{M}}^{z}d_{\mathrm{A}}^{z}+\tfrac{1}{2}(d_{\mathrm{M}}^{+}d_{\mathrm{A}}^{-}+d_{\mathrm{M}}^{-}d_{\mathrm{A}}^{+})\right],(6)ℳ1\displaystyle\mathcal{M}_{1}=−32​sin⁡θ​cos⁡θ​[ei​φ(dMzdA−+dM−dAz)−e−i​φ(dMzdA++dM+dAz)],\displaystyle=-\frac{3}{\sqrt{2}}\sin\theta\cos\theta\begin{aligned} &\Big[e^{i\varphi}(d_{\mathrm{M}}^{z}d_{\mathrm{A}}^{-}+d_{\mathrm{M}}^{-}d_{\mathrm{A}}^{z})\\
&\qquad-e^{-i\varphi}(d_{\mathrm{M}}^{z}d_{\mathrm{A}}^{+}+d_{\mathrm{M}}^{+}d_{\mathrm{A}}^{z})\Big],\end{aligned}(7)ℳ2\displaystyle\mathcal{M}_{2}=−32​sin2⁡θ​[e2​i​φ​dM−​dA−+e−2​i​φ​dM+​dA+],\displaystyle=-\frac{3}{2}\sin^{2}\theta\left[e^{2i\varphi}d_{\mathrm{M}}^{-}d_{\mathrm{A}}^{-}+e^{-2i\varphi}d_{\mathrm{M}}^{+}d_{\mathrm{A}}^{+}\right],(8)

whered±≡∓(dx±i​dy)/2d^{\pm}\equiv\mp(d^{x}\pm id^{y})/\sqrt{2}are the spherical components of the dipole operator, anddxd^{x},dyd^{y}, anddzd^{z}are its Cartesian components.
The operatorsℳ0\mathcal{M}_{0},ℳ1\mathcal{M}_{1}, andℳ2\mathcal{M}_{2}couple states with total angular-momentum projectionsMF+mjM_{F}+m_{j}differing by0,±1\pm 1, and±2\pm 2, respectively.
Here,MF≡MN+mRb+mCsM_{F}\equiv M_{N}+m_{\mathrm{Rb}}+m_{\mathrm{Cs}}is the projection of the total molecular angular momentum.

In this work, the interparticle axis is aligned with the quantisation axis (set by the magnetic field), as shown in Fig.1a, so thatθ=φ=0\theta=\varphi=0.
In this geometry,ℳ1\mathcal{M}_{1}andℳ2\mathcal{M}_{2}vanish, and the interaction conserves the total projectionMF+mjM_{F}+m_{j}.
The stretched states which are used in the experiment are|3;83​d⟩\ket{3;83\mathrm{d}}(withj=mj=5/2j=m_{j}=5/2andMN=3M_{N}=3) and|4;84​p⟩\ket{4;84\mathrm{p}}(withj=mj=3/2j=m_{j}=3/2andMN=4M_{N}=4).
These are coupled through the termdM+​dA−d_{\mathrm{M}}^{+}d_{\mathrm{A}}^{-}inℳ0\mathcal{M}_{0}, and the matrix element of the
dipole–dipole interaction readsVdd​(R)\displaystyle V_{\mathrm{dd}}(R)≡⟨4;84​p|Vdd​(R,0,0)|3;83​d⟩\displaystyle\equiv\braket{4;84\mathrm{p}|V_{\mathrm{dd}}(R,0,0)|3;83\mathrm{d}}=−⟨4|dM+|3⟩​⟨84​p|dA−|83​d⟩4​π​ϵ0​R3,\displaystyle=-\frac{\braket{4|d_{\mathrm{M}}^{+}|3}\braket{84\mathrm{p}|d_{\mathrm{A}}^{-}|83\mathrm{d}}}{4\pi\epsilon_{0}R^{3}},(9)

which we write asVdd​(R)=C3/R3≡−dA​dM/(4​π​ϵ0​R3)V_{\mathrm{dd}}(R)=C_{3}/R^{3}\equiv-d_{\mathrm{A}}d_{\mathrm{M}}/(4\pi\epsilon_{0}R^{3})in the main text (likewise for⟨3;83​d|Vdd​(R,0,0)|4;84​p⟩\braket{3;83\mathrm{d}|V_{\mathrm{dd}}(R,0,0)|4;84\mathrm{p}}).

If the interparticle axis were not exactly aligned with the quantisation axis,
the matrix elements ofℳ1\mathcal{M}_{1}andℳ2\mathcal{M}_{2}would no longer vanish
andMF+mjM_{F}+m_{j}would not be conserved.
In this regime, pair states involving different molecular hyperfine states could couple to our chosen pair states[85].
These pair states are numerous and closely spaced in energy, with detunings on the kHz scale, and their admixture of|83​d⟩\ket{83\mathrm{d}}character makes them optically accessible with our laser system.

We do not measure population in these states experimentally as we readout only the populations of the stretched molecular states, and so transfer to the non-stretched states appears as a lack of molecule recovery which is removed in our postselection routine (see below).
We attribute the absence of resolvable interaction-shifted features to coupling to these states, which can be caused by technical imperfections in alignment of the interparticle axis (θ≠0\theta\neq 0), shot-to-shot fluctuations in the relative geometry, and the finite wavefunction spread of the particles.
We note, however, that these couplings do not constitute a fundamental limitation for blockade-based gates, since these rely only on the presence of an interaction shift exceeding the excitation linewidth (|U​(R)|≳ℏ​ΩRyd|U(R)|\gtrsim\hbar\Omega_{\mathrm{Ryd}}), rather than isolation of individual hyperfine channels.
Extended Data Fig. 1:Comparison between charge–dipole and dipole–dipole interactions.a, Magnitudes|U​(R)||U(R)|of the interaction-induced energy shifts for the states|+⟩\ket{+}(orange) and|0;83​d⟩\ket{0;83\mathrm{d}}(grey), calculated using the full charge–dipole Hamiltonian.b, Local power-law exponentα​(R)\alpha(R)for the state|+⟩\ket{+}, extracted pointwise from the curve ina.
In both panels, the black dashed line shows the behaviour expected from the point-dipole model withC3/h=1.79​MHz​μ​m3C_{3}/h=1.79\,\mathrm{MHz}\,\mu\mathrm{m}^{3}. At short distances, the dipole–dipole approximation breaks down due to the finite spatial extent of the Rydberg electron, requiring the full charge–dipole description.

Experimental apparatus
Our experimental apparatus has been described in previous publications[56].
The platform enables the preparation, control, and detection of single atoms and molecules trapped in an ultrahigh-vacuum (UHV) environment with species-specific optical tweezers.

The experiments presented here begin with two Rb atoms and one Cs atom, each trapped in species-specific optical tweezers[86].
The optical tweezers are formed by a high numerical-aperture objective lens mounted below a UHV glass cell.
The atoms are cooled to the motional ground state via Raman sideband cooling[78]and rearranged using tweezer transport to form a co-trapped Rb–Cs atom pair and a single Rb atom.
The atom pair is then magnetoassociated into a weakly bound molecule[87], which is subsequently transferred to the rovibrational ground state|0⟩\ket{0}using a two-photon STIRAP sequence[54].
After molecular preparation, we reconfigure the optical tweezers to set a controlled interparticle separationRRbetween the RbCs molecule and the Rb atom.
The Rb atom is then excited to the Rydberg manifold using a two-photon excitation scheme (see Ref.[54]and below).
At the end of each experimental sequence, we dissociate the molecule and map its internal states onto distinct atomic configurations[56].
Final detection is performed via fluorescence imaging of the tweezer occupations.

Below, we provide further details of techniques and experimental upgrades which are critical for the measurements presented in this work.


Control of the interparticle distanceRR.To precisely control the distance between the particles, we use species-specific optical tweezers.
The molecule is primarily trapped by a tweezer using light at a wavelength of 1066 nm (the “molecule tweezer”) and the atom is primarily trapped by a tweezer using light at a wavelength of 817 nm (the “atom tweezer”)[54]. The positions of the tweezers are controlled by optical elements in their beam path prior to the objective lens which forms the traps and images the atoms.
Specifically, the position of the molecule tweezer is set using a spatial light modulator and remains fixed throughout experimental sequences.
The position of the atom tweezer (and the other 817-nm tweezers used in experiments) is controlled by an acousto-optic deflector (AOD).
By changing the frequencies of the radio-frequency (RF) tones applied to the AOD, we can dynamically and precisely translate the 817-nm tweezers.
We calibrate the relationship between RF frequency and tweezer position using fluorescence images of individual Rb atoms recorded at different AOD frequencies, and have independently verified this calibration by measuring the interaction shift between two Rydberg atoms, as described in Ref.[54].

We calibrate the relative position of the atom tweezer and the molecule tweezer by measuring the differential ac Stark shiftΔ​E\Delta Eof the atomic transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}induced by the molecule tweezer.
An example measurement is shown in Extended Data Fig.2.
A Rb atom is initially prepared in the atom tweezer, which has an intensity of63​kW/cm263\,\mathrm{kW/cm^{2}}.
The atom tweezer is then translated towards the molecule tweezer (intensity18​kW/cm218\,\mathrm{kW/cm^{2}}), held at a separationRtR_{\mathrm{t}}, and the atomic transition frequency is measured.
When the tweezers are overlapped (Rt=0R_{\mathrm{t}}=0), the transition frequency is maximised because the atom experiences the largest differential ac Stark shift from the molecule tweezer.
This method is sensitive to the radial overlap of the tweezers but relatively insensitive to overlap along the propagation direction because the tweezers have micron-scale Rayleigh ranges.
Along this axis, we optimise the overlap by maximising the contrast of the atom–molecule spin-exchange signal.
With our postselection scheme, this contrast is maximised when the interparticle vector is aligned with the quantisation axis, because couplings to other molecular hyperfine states (which are not detected) are minimised[85].Extended Data Fig. 2:Calibration of the relative tweezer positions.We show the measured frequency of the atomic transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}as a function of the separationRtR_{\mathrm{t}}between the centres of the atom and molecule tweezers. The molecule tweezer induces a differential ac Stark shift of the transition, with a magnitude that depends on the local intensity experienced by the atom. The transition frequency is maximised when the tweezers are spatially overlapped (Rt=0R_{\mathrm{t}}=0).
The solid line is a Gaussian fit used to determine the relative radial alignment of the tweezers.
The error bars show the1​σ1\sigmaconfidence intervals and, on average, there are 432 experimental shots per data point.

As in Ref.[54], we determine the interparticle separationRRby modelling the three-dimensional trapping potential experienced by each particle. For the atom, we use the polarisabilitiesα1066Rb=687×4​π​ε0​a03\alpha^{\mathrm{Rb}}_{1066}=687\times 4\pi\varepsilon_{0}a_{0}^{3}[88]andα817Rb=4307×4​π​ε0​a03\alpha^{\mathrm{Rb}}_{817}=4307\times 4\pi\varepsilon_{0}a_{0}^{3}[88]. For the molecule, the polarisability of the stretched state|N⟩\ket{N}isαλRbCs​(N)=aλ(0)−N2​N+3​aλ(2),\alpha^{\mathrm{RbCs}}_{\lambda}(N)=a^{(0)}_{\lambda}-\frac{N}{2N+3}a^{(2)}_{\lambda},(10)

whereaλ(0)a^{(0)}_{\lambda}andaλ(2)a^{(2)}_{\lambda}are the isotropic and anisotropic polarisabilities at wavelengthλ\lambda.
For the molecule tweezer, we takea1066(0)=2.0×103×4​π​ε0​a03a^{(0)}_{1066}=2.0\times 10^{3}\times 4\pi\varepsilon_{0}a_{0}^{3}[56]anda1066(2)=1980×4​π​ε0​a03a^{(2)}_{1066}=1980\times 4\pi\varepsilon_{0}a_{0}^{3}[56]. For the atom tweezer,a817(0)=4.0×102×4​π​ε0​a03a^{(0)}_{817}=4.0\times 10^{2}\times 4\pi\varepsilon_{0}a_{0}^{3}[54]anda817(2)=−2814×4​π​ε0​a03a^{(2)}_{817}=-2814\times 4\pi\varepsilon_{0}a_{0}^{3}[56].
At large separations, the interparticle separationRRis approximately equal to the separationRtR_{\mathrm{t}}between the tweezer centres.
However, at smallRtR_{\mathrm{t}}, the particles experience attractive forces from both tweezers.
This means that they move closer together, such thatR<RtR<R_{\mathrm{t}}[54].


Molecule detection.Direct fluorescence imaging of RbCs molecules is not possible because there are no closed optical cycling transitions suitable for repeated photon scattering.
Instead, we detect molecules by dissociating them into their constituent atoms and subsequently imaging the resulting atoms.

The dissociation process is state-selective and only molecules in the rotational ground state|0⟩\ket{0}are dissociated. This enables state-resolved molecular detection.
To measure the population in a rotational state|N⟩\ket{N}, we first transfer molecules in|N⟩\ket{N}to|0⟩\ket{0}and then apply the dissociation sequence.
For example, to distinguish populations in|2⟩\ket{2}and|3⟩\ket{3}, molecules in|2⟩\ket{2}are first transferred to|0⟩\ket{0}, dissociated, and the resulting atoms moved to a designated storage location within the tweezer array.
Molecules in|3⟩\ket{3}are then transferred to|0⟩\ket{0}and detected in an analogous manner.
The resulting atoms from each detection step are rearranged into distinct locations within the tweezer array.
In this way, the rotational state of the molecule is mapped onto the final positions of the dissociated atoms, allowing the populations of multiple molecular states to be determined from a single fluorescence image.
A detailed description of the detection protocol is given in Ref.[56].

In this work, we use this technique to determine both the presence of a molecule and its rotational state.
First, we identify experimental shots in which a molecule was not formed (≈50%\approx 50\%) by storing the Rb atom from the atom pair in a dedicated “detection tweezer”[54].
Subsequently, the Cs atom is removed using resonant light, ensuring that the molecule tweezer is empty.
This procedure provides a reference data set corresponding to experimental runs in which no molecule was present, such as the grey data shown in Fig.2.
For experimental shots in which a molecule is successfully formed, this detection step does not affect the molecule.
We then apply postselection to discard runs in which no atoms are recovered following the molecular readout sequence.
Such events correspond primarily to molecule loss during the experimental sequence.
These loss processes are approximately independent of the molecular rotational state[56,40]and therefore do not significantly affect the relative state populations that are the focus of this work.


Rydberg excitation.We excite the atoms to the Rydberg state|83​d⟩\ket{83\mathrm{d}}using the inverted two-photon scheme described in Ref.[54]. As illustrated in Fig.1c, we drive theσ+\sigma^{+}transition from the state|5​s⟩\ket{\mathrm{5s}}to a virtual level detuned by approximately1.61.6\,GHz from|6​p⟩\ket{6\mathrm{p}}using light at a wavelength of 420 nm. The 420-nm beam propagates perpendicular to the quantisation axis and is linearly polarised orthogonal to it. We couple this virtual level to|83​d⟩\ket{83\mathrm{d}}using light at a wavelength of 1012 nm from a beam that propagates approximately parallel to the quantisation axis and is approximately circularly polarised (see below). The beam waists are52​(6)​μ52(6)\,\mum and35​(2)​μ35(2)\,\mum for the 420-nm and 1012-nm beams, respectively.

This two-photon excitation scheme allows us to access Rydberg states with orbital angular momentuml=0l=0(s\mathrm{s}) andl=2l=2(d\mathrm{d}). When identifying resonances, we therefore consider electric-dipole-allowed transitions originating from these states. The corresponding transition energies are shown in Fig.1b, withs→p\mathrm{s}\rightarrow\mathrm{p}transitions shown in red,d→p\mathrm{d}\rightarrow\mathrm{p}transitions in blue, andd→f\mathrm{d}\rightarrow\mathrm{f}transitions in purple. Although electric-dipole selection rules place no restriction onΔ​n\Delta n, only a narrow range ofΔ​n\Delta nvalues yields atomic transition frequencies comparable to the molecular transition frequencies relevant here.

Our polarisation configuration could in principle also address Rydberg states withmj=1/2m_{j}=1/2. However, the transitions to these states are significantly detuned from the transition|5​s⟩→|83​d⟩\ket{\mathrm{5s}}\rightarrow\ket{83\mathrm{d}}at the magnetic fields used in this work (see below) and are therefore not appreciably driven.

To drive the Rydberg transition, we first switch on the 1012-nm light and then apply a pulse of 420-nm light using an acousto-optic modulator (AOM).
The 1012-nm light is switched off after the pulse, such that the duration of the 420-nm pulse defines the duration with which we drive the Rydberg transition.


Molecule loss caused by Rydberg-excitation light.We find that the 1012-nm light can strongly reduce the probability of recovering a molecule when its intensity is too high. We attribute this effect to light-induced avoided crossings between hyperfine states within the molecular rotational manifolds. The applied light produces differential ac Stark shifts between hyperfine states and, when its polarisation is not purely linear along the quantisation axis, can couple states with different values ofMF≡MN+mRb+mCsM_{F}\equiv M_{N}+m_{\mathrm{Rb}}+m_{\mathrm{Cs}}[89].Extended Data Fig. 3:Molecular loss induced by the 1012-nm Rydberg-excitation light.a, Calculated energy shiftsΔ​Eaniso\Delta E_{\mathrm{aniso}}due to the anisotropic part of the molecular polarisability in theN=3N=3rotational manifold as a function of the 1012-nm intensity. Colours indicate the overlap with the state|3⟩\ket{3}at zero intensity. A dense network of avoided crossings emerges near8​kW/cm28\,\mathrm{kW/cm^{2}}.b, Measured relative probability of recovering a molecule prepared in|3⟩\ket{3}as a function of the 1012-nm intensity. The reduction in recovery probability coincides with the onset of the avoided crossings shown ina, consistent with population transfer into hyperfine states that are not detected by the imaging sequence.
The solid line is a fit to the error function; the shaded region shows the1​σ1\sigmaconfidence interval of the fit.
The dashed line corresponds to the 1012-nm power that we typically use.
The error bars show the1​σ1\sigmaconfidence intervals and, on average, there are 138 experimental shots per data point.

To model this effect, we use the Python packagediatomic-py[90], extended to include optical fields with arbitrary polarisation. The polarisation of the 1012-nm beam is measured before the vacuum chamber using a polarimeter (Thorlabs PAX1000IR1/M). The beam propagates at an angle of7∘7^{\circ}to the quantisation axis and is approximately left-handed circularly polarised, with azimuthal angle28∘28^{\circ}and ellipticity−39∘-39^{\circ}. Extended Data Fig.3a shows the calculated energy shiftsΔ​Eaniso\Delta E_{\mathrm{aniso}}of the hyperfine states in theN=3N=3manifold due to the anisotropic part of the molecular polarisability as a function of the 1012-nm intensity.
The isotropic shift common to all states has been removed. The calculations assumea1012(2)=3.3×103×4​π​ε0​a03a^{(2)}_{1012}=3.3\times 10^{3}\times 4\pi\varepsilon_{0}a_{0}^{3}[91],and a trapping intensity of3.5​kW/cm23.5\,\mathrm{kW}/\mathrm{cm}^{2}from the molecular tweezer. The colour scale indicates the overlap of each eigenstate with the state|3⟩\ket{3}in the absence of the 1012-nm light. A dense network of avoided crossings appears when the 1012-nm intensity reaches approximately8​kW/cm28\,\mathrm{kW}/\mathrm{cm}^{2}. At this intensity, the light shift of the state|3⟩\ket{3}caused by the anisotropic polarisability is approximately−200​kHz-200\,\mathrm{kHz}.
The behaviour of the corresponding states in theN=4N=4manifold is similar, resulting in only a small differential shift of the frequency of the transition|3⟩→|4⟩\ket{3}\to\ket{4}.

Extended Data Fig.3b shows the relative probability of recovering a molecule initially prepared in|3⟩\ket{3}after the 1012-nm beam is pulsed for532​μ532\,\mus at varying intensities.
The plotted intensities are inferred from the beam power measured outside the vacuum chamber assuming perfect transmission and alignment; the actual intensity at the molecules may therefore be somewhat lower.
We observe a sharp reduction in the recovery probability once the intensity reaches the approximate region where the avoided crossings occur.
We attribute this behaviour to population transfer into other hyperfine states as the crossings are traversed. Because these states are not detected by our state-sensitive imaging sequence, the transfer appears experimentally as a loss of molecules.

Experimentally, these avoided crossings and the associated loss features constrain the maximum usable intensity of the 1012-nm light during Rydberg excitation while maintaining molecular survival.
Typically, we use100​mW100\,\mathrm{mW}of 1012-nm power, corresponding to an intensity of approximately8​kW/cm28\,\mathrm{kW/cm^{2}}under ideal alignment (Fig.3b, dashed line).
The onset of loss can be shifted to higher intensities by increasing the depth of the molecular tweezer, which increases the tweezer-induced anisotropic light shifts and thereby separates the relevant hyperfine states further.
To estimate the probability of molecule loss induced by the 1012-nm light, we fit the data in Fig.3b with the error function (solid line).
The shaded region indicates the1​σ1\sigmaconfidence interval of the fit.
From this, we extract a loss probability of9​(6)%9(6)\%at our typical operating intensity.
This corresponds to an erasure error on the molecular qubit that is removed by postselecting on the recovery of the molecule at the end of the experimental sequence.

In future, these effects may be mitigated either by employing 1012-nm light linearly polarised along the quantisation axis, which would require selecting alternative Rydberg states, or by delivering the 1012-nm beam through the objective lens so that it addresses only the atoms.


Control of optical and microwave pulses.The optical and microwave pulses used for atomic and molecular excitation are generated using a direct-digital-synthesis platform (AMD RFSoC 4x2, controlled via theQICKfirmware[92])[93].
This system provides precise control over pulse duration, amplitude, frequency, and phase.

One output drives an external dipole antenna via an RF amplifier (Minicircuits ZVA-183-S+) to generate the microwave fields used for molecular excitation[56], while the second output controls the AOM that switches the 420-nm light used for atomic Rydberg excitation[54].
This enables a well-defined relative phase between the atomic and molecular control channels, which is essential for the phase mapping presented in Fig.4c which we use to characterise the atom–molecule entanglement.


Rydberg spectroscopy
Ground-to-Rydberg Zeeman spectroscopy.Extended Data Fig.4shows the energies of Rydberg states near|83​d⟩\ket{83\mathrm{d}}as a function of magnetic field. The lines show state energies calculated using the Python packagePairInteraction[94,95]. We include states withl≤6l\leq 6and neglect hyperfine structure. Energies are referenced to the state|83​d⟩\ket{83\mathrm{d}}at zero magnetic field and are calculated assuming zero electric field.Extended Data Fig. 4:Effect of a magnetic field on Rydberg states withl<6l<6around the state|83​d⟩\ket{83\mathrm{d}}.Lines show the calculated state energies and we highlight the states used in this work.
Data points show measured energies which are referenced to the blue empty point, which is set to lie on the calculated curve.
The error bars corresponding to the1​σ1\sigmaconfidence intervals are smaller than the markers and, on average, there are 971 experimental shots per data point.

The interaction of the atom with an external magnetic field𝑩\boldsymbol{B}is described by[94,95]HB=−𝝁⋅𝑩+18​me​|𝒅×𝑩|2,H_{B}=-\boldsymbol{\mu}\cdot\boldsymbol{B}+\frac{1}{8m_{\mathrm{e}}}|\boldsymbol{d}\times\boldsymbol{B}|^{2},(11)

where𝝁\boldsymbol{\mu}is the magnetic dipole operator,𝒅\boldsymbol{d}is the electric dipole operator, andmem_{\mathrm{e}}is the electron mass.
The first term gives rise to the linear Zeeman shift, while the second describes the diamagnetic interaction.

For the Rydberg states used in this work (n≈83n\approx 83), diamagnetic effects become significant at magnetic fields above approximately1010\,G and therefore strongly influence the Rydberg spectrum over the magnetic-field range relevant to our experiments. It is thus essential to include this contribution when calculatingΔ​EA\Delta E_{\mathrm{A}}in order to identify and tune resonances.
It gives rise to a wide variation in the tuning ofΔ​EA\Delta E_{\mathrm{A}}that is possible for transitions with different initialnn.
This can be seen in Fig.1b, where we show howΔ​EA\Delta E_{\mathrm{A}}varies in the field range150150\,G to250250\,G.
The diamagnetic interaction can mix states with the same value ofmjm_{j}within a givenn​lnlmanifold. This further motivates our use of stretched states, which possess a unique value ofmjm_{j}for eachnnandll. As a result, their state composition remains unchanged over the magnetic-field range that we use.

The data points in Extended Data Fig.4show measured energies of Rydberg states accessible with our two-photon excitation scheme.
Error bars are smaller than the symbol size; typical statistical uncertainties are approximately100​kHz×h100\,\mathrm{kHz}\times h, obtained from fits to spectroscopic features such as those shown in Fig.2b.
When comparing measurements taken at different magnetic fields, we correct for the linear Zeeman shift of the atomic ground state[96].
Additional systematic uncertainties arise from differential light shifts induced by the excitation lasers and from stray electric fields, but we estimate these to be on the order of approximately1​MHz×h1\,\mathrm{MHz}\times hwhich is much smaller than the energy range shown here.

To facilitate comparison with theory, all measured energies are referenced to the empty point in Extended Data Fig.4, which is constrained to lie on the corresponding calculated curve. We determine energy differences rather than absolute transition frequencies because the quoted accuracy of our wavemeter (Bristol Instruments 671A-NIR) is±0.2\pm 0.2parts per million, corresponding to a systematic uncertainty of approximately200​MHz200\,\mathrm{MHz}on the two-photon transition frequency.


Ground-to-Rydberg dc Stark spectroscopy.Our apparatus incorporates an array of electrodes[56]that provides control of the electric field both parallel to the magnetic field defining the quantisation axis and along one perpendicular direction. These electrodes are used to compensate stray electric fields in the corresponding directions.Extended Data Fig. 5:dc Stark spectroscopy of the transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}.Measured Stark shiftsΔ​E\Delta Eas a function of applied electrode voltage for electric fields parallel (a) and perpendicular (b) to the quantisation axis. Solid lines show calculations usingPairInteraction[94,95]. Insets show the corresponding electrode configurations. Fits to the spectra are used to calibrate the applied fields and determine the residual stray fields. Dashed lines indicate the voltages used to compensate the stray electric fields.
The error bars corresponding to the1​σ1\sigmaconfidence intervals are smaller than the markers and, on average, there are 951 experimental shots per data point.

To determine the stray electric fields, we perform dc Stark spectroscopy of the transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}. We generate an electric fieldℰ\mathcal{E}by applying a potential differenceVVacross the electrode array, with the electrode voltages set to±V/2\pm V/2. The measured spectra are shown in Extended Data Fig.5for electric fields parallel (a) and perpendicular (b) to the quantisation axis. The insets show the corresponding electrode configurations.
The solid lines show calculations performed usingPairInteraction[94,95]atB=181.7B=181.7\,G, the magnetic field used for these measurements. By fitting the measured transition frequencies to these calculations, we obtain calibration factors ofℰ∥/V∥=1.065​(2)​(mV/cm)/mV\mathcal{E}_{\parallel}/V_{\parallel}=1.065(2)\,(\mathrm{mV}/\mathrm{cm})/\mathrm{mV}andℰ⟂/V⟂=0.957​(4)​(mV/cm)/mV\mathcal{E}_{\perp}/V_{\perp}=0.957(4)\,(\mathrm{mV}/\mathrm{cm})/\mathrm{mV}. From the fitted offsets, we infer stray fields ofℰ∥=−5.4​(1)​mV/cm\mathcal{E}_{\parallel}=-5.4(1)\,\mathrm{mV}/\mathrm{cm}andℰ⟂=−58.9​(8)​mV/cm\mathcal{E}_{\perp}=-58.9(8)\,\mathrm{mV}/\mathrm{cm}when no voltages are applied to the electrodes.
For all measurements presented in the main text, we compensate these stray fields by applying the corresponding offset voltages.

We do not have independent control over the second electric-field component perpendicular to the quantisation axis. From microwave spectroscopy of the transition|83​d⟩→|84​p⟩\ket{83\mathrm{d}}\rightarrow\ket{84\mathrm{p}}, we estimate the magnitude of this residual field to be approximately12​mV/cm12\,\mathrm{mV}/\mathrm{cm}(see below).


Rydberg-to-Rydberg spectroscopy.We perform spectroscopy of the transition|83​d⟩→|84​p⟩\ket{83\mathrm{d}}\rightarrow\ket{84\mathrm{p}}to determine the atomic transition energyΔ​EA\Delta E_{\mathrm{A}}and thereby identify the atom–molecule resonance condition.

The spectroscopy sequence is based on a resonant2​π2\pipulse on the transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}.
In the absence of additional driving, this pulse returns the atom to the trapped state|5​s⟩\ket{5\mathrm{s}}.
During the middle of the pulse, however, we apply a short microwaveπ\pipulse near resonance with the transition|83​d⟩→|84​p⟩\ket{83\mathrm{d}}\rightarrow\ket{84\mathrm{p}}using the antenna normally employed for molecular control.
If the microwave pulse transfers population to|84​p⟩\ket{84\mathrm{p}}, the atom is no longer returned to|5​s⟩\ket{5\mathrm{s}}and is subsequently lost from the tweezer.
We therefore detect the Rydberg-to-Rydberg transition through atomic loss.

This sequence allows us to perform the Rydberg-to-Rydberg spectroscopy in the presence of the excitation light.
This ensures that any light shifts caused by the excitation beams are included in the measured transition frequency and therefore correspond directly to the conditions under which interaction-induced blockade is observed.Extended Data Fig. 6:Spectroscopy of the transition|83​d⟩→|84​p⟩\ket{83\mathrm{d}}\rightarrow\ket{84\mathrm{p}}.a, Pulse sequence used to probe the|83​d⟩→|84​p⟩\ket{83\mathrm{d}}\rightarrow\ket{84\mathrm{p}}transition, as described in the text. The panel also shows a simulation of the state evolution under resonant driving of both transitions, performed usingQuTiP[97,98,99].b, Measured transition frequencies as a function of magnetic field compared with calculations fromPairInteraction[94,95](black line). The calculated resonance lies approximately1.7​MHz1.7\,\mathrm{MHz}below the observed transition. The red shaded region indicates the contribution from the light shift of|83​d⟩\ket{83\mathrm{d}}induced by the 1012-nm excitation beam. The remaining shift (blue) is attributed to a residual electric field of approximately12​mV/cm12\,\mathrm{mV}/\mathrm{cm}along the direction which we cannot control. The black point and dashed line show the energy of the molecular transition|3⟩→|4⟩\ket{3}\to\ket{4}.
The error bars show the1​σ1\sigmaconfidence intervals and, on average, there are 1214 experimental shots per data point.

For the measurements shown in Fig.1d, we drive the microwave transition|83​d⟩→|84​p⟩\ket{83\mathrm{d}}\rightarrow\ket{84\mathrm{p}}with a Rabi frequency of approximately1​MHz1\,\mathrm{MHz}, while the transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}is driven with a Rabi frequency of0.95​(6)​MHz0.95(6)\,\mathrm{MHz}.
In Extended Data Fig.6a, we show this pulse sequence together with a simulation of the state populations under resonant driving of both transitions, calculated with the Python packageQuTiP[97,98,99]. The simulation shows near-complete transfer from|5​s⟩\ket{5\mathrm{s}}to|84​p⟩\ket{84\mathrm{p}}when both drives are on resonance.

In Extended Data Fig.6b, we reproduce the data shown in Fig.1d and compare them with calculations fromPairInteraction[94,95].
The theoretical calculations assume zero electric field and are shown by the black line.
The calculated transition frequencies are approximately 1.7 MHz below the observed frequencies.
Of this offset,0.33​(2)0.33(2)\,MHz (red shaded region) comes from the shift of the state|83​d⟩\ket{83\mathrm{d}}from the 1012-nm light, which we have independently measured.
We attribute the remaining difference (blue shaded region) to a stray electric field in the direction that we cannot control with our electrode configuration; from calculations withPairInteraction[94,95]we estimate this field is approximately12​mV/cm12\,\mathrm{mV}/\mathrm{cm}.

For comparison, the black square in Fig.1d (and Extended Data Fig.6b) shows the energy of the transition|3⟩→|4⟩\ket{3}\to\ket{4}measured under the conditions used to engineer resonance (i.e. with the Rydberg-excitation light on), but with no atom present.
We determine this transition frequency using microwave spectroscopy of the molecule, as in Ref.[56].
The differential Zeeman shift of the transition is negligible: usingdiatomic-py[90], we calculate the magnetic moments of the molecular states|3⟩\ket{3}and|4⟩\ket{4}to be5.335​μN5.335\mu_{\mathrm{N}}and5.329​μN5.329\mu_{\mathrm{N}}, respectively.
The resulting differential magnetic moment of the transition is approximately6×10−3​μN=5​Hz/G×h6\times 10^{-3}\mu_{\mathrm{N}}=5\,\mathrm{Hz/G}\times h, meaning that the transition frequency is effectively constant over the range of magnetic fields explored here (dashed line).


TheRRdependence of blockade
We model the dependence of the Rydberg blockade onRR, as shown in Fig.2d, using a minimal three-level model.
For the resonant case, we use the basis{|3;5​s⟩,|3;83​d⟩,|4;84​p⟩}\{\ket{3;5\mathrm{s}},\ket{3;83\mathrm{d}},\ket{4;84\mathrm{p}}\}and assume that the resonance condition is exactly satisfied, such thatEA=−EME_{\mathrm{A}}=-E_{\mathrm{M}}. Under the rotating-wave approximation, the Hamiltonian describing the system isH=(012​ℏ​ΩRyd012​ℏ​ΩRyd0V​(R)0V​(R)0),H=\begin{pmatrix}0&\frac{1}{2}\hbar\Omega_{\mathrm{Ryd}}&0\\
\frac{1}{2}\hbar\Omega_{\mathrm{Ryd}}&0&V(R)\\
0&V(R)&0\end{pmatrix},(12)

whereΩRyd/2​π=318​(3)​kHz\Omega_{\mathrm{Ryd}}/2\pi=318(3)\,\mathrm{kHz}is the Rabi frequency with which we resonantly drive the atomic transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}andV​(R)V(R)is the coupling between the pair states|3;83​d⟩\ket{3;83\mathrm{d}}and|4;84​p⟩\ket{4;84\mathrm{p}}.
In the dipole-dipole regime,V​(R)=Vdd​(R)=C3/R3V(R)=V_{\mathrm{dd}}(R)=C_{3}/R^{3}(as in the main text). However, this Hamiltonian remains valid in the charge-dipole regime because the relevant pair states remain strongly hybridised[85].
In the absence of the Rydberg-excitation light, the energies of the hybridised pair states|±⟩\ket{\pm}areU​(R)=±V​(R)U(R)=\pm V(R), as described in the main text and shown by the orange lines in Fig.1e.

We initialise the system in the state|3;5​s⟩\ket{3;5\mathrm{s}}and allow it to evolve for a durationτ=π/ΩRyd\tau=\pi/\Omega_{\mathrm{Ryd}}, corresponding to aπ\pipulse on the bare atomic transition. The state after this pulse ise−i​H​τ/ℏ​|3;5​s⟩e^{-iH\tau/\hbar}\ket{3;5\mathrm{s}}.
Experimentally, Rydberg atoms are ejected from the optical tweezer before detection, such that the measured atom-survival probability is proportional to the population remaining in the state|3;5​s⟩\ket{3;5\mathrm{s}}.
Ideally, the population in|3;5​s⟩\ket{3;5\mathrm{s}}after the pulse is|⟨3;5​s|e−i​H​τ/ℏ|3;5​s⟩|2=[1+κ2​cos⁡(π2​κ​1+κ2)]2(1+κ2)2,\left|\braket{3;5\mathrm{s}|e^{-iH\tau/\hbar}|3;5\mathrm{s}}\right|^{2}=\frac{\left[1+\kappa^{2}\cos\!\left(\frac{\pi}{2\kappa}\sqrt{1+\kappa^{2}}\right)\right]^{2}}{(1+\kappa^{2})^{2}},(13)

whereκ≡ℏ​ΩRyd/[2​V​(R)]\kappa\equiv\hbar\Omega_{\mathrm{Ryd}}/[2V(R)].
We use Eq. (13) both to generate the predicted survival probability from the theoretically calculated interaction strengthV​(R)V(R)(Fig.2d, solid blue line) and to extract an effective dipolar coefficientC3/h=1.36​(15)​MHz​μ​m3C_{3}/h=1.36(15)\,\mathrm{MHz}\,\mu\mathrm{m}^{3}by fitting the experimental data under the assumptionV​(R)=Vdd​(R)=C3/R3V(R)=V_{\mathrm{dd}}(R)=C_{3}/R^{3}(Fig.2d, dashed blue line).
The only other free parameters are scaling parameters that account for the experimental contrast.

For the experimental parameters used here, Eq. (13) predicts oscillations in the atom-survival probability forR≲1.4​μ​mR\lesssim 1.4\,\mu\mathrm{m}.
These arise from the square excitation pulse, whose finite duration produces asinc2\mathrm{sinc}^{2}spectral envelope. At sufficiently smallRR, the resulting Fourier sidelobes can become resonant with the interaction-shifted transition, leading to the oscillatory features.
Such effects could be suppressed in future experiments using shaped excitation pulses.

For the non-resonant case, we use the basis{|0;5​s⟩,|0;83​d⟩}\{\ket{0;5\mathrm{s}},\ket{0;83\mathrm{d}}\}and the Hamiltonian describing the system isH′=(012​ℏ​ΩRyd12​ℏ​ΩRydU​(R)).H^{\prime}=\begin{pmatrix}0&\frac{1}{2}\hbar\Omega_{\mathrm{Ryd}}\\
\frac{1}{2}\hbar\Omega_{\mathrm{Ryd}}&U(R)\end{pmatrix}.(14)

Here, we includeU​(R)U(R)directly in the Hamiltonian as an energy shift of the pair state|0;83​d⟩\ket{0;83\mathrm{d}}. Unlike the resonant case, the off-resonant interactions do not lead to strong coupling with a single nearby pair state, and their effect is therefore well described by the energy shift given by the BOP shown in Fig.1e (grey line).
After the Rydberg-excitation pulse, we expect the population of the state|0;83​d⟩\ket{0;83\mathrm{d}}to be|⟨0;5​s|e−i​H′​τ/ℏ|0;5​s⟩|2=1+ξ2​cos2⁡(π2​ξ​1+ξ2)1+ξ2\left|\braket{0;5\mathrm{s}|e^{-iH^{\prime}\tau/\hbar}|0;5\mathrm{s}}\right|^{2}=\frac{1+\xi^{2}\cos^{2}\!\left(\frac{\pi}{2\xi}\sqrt{1+\xi^{2}}\right)}{1+\xi^{2}}(15)

whereξ≡ℏ​ΩRyd/U​(R)\xi\equiv\hbar\Omega_{\mathrm{Ryd}}/U(R).
We use Eq. (15) to plot the solid red line in Fig.2d, using the experimental contrast that we fit to the blue data.


Fidelities in the hybrid system
Atom-mediated readout of the molecule.To determine fidelities associated with the atom-mediated readout of the molecule, we fit the data shown in Fig.3. The fidelity of successfully determining the state of the molecule by measuring the atom isFmeas=12​(F0|0+F1|1)=0.91​(1)F_{\mathrm{meas}}=\frac{1}{2}(F_{0|0}+F_{1|1})=0.91(1). Here,FN|NF_{N|N}is the probability of inferring from the atomic measurement that the molecule is in state|N⟩\ket{N}, given that it was prepared in|N⟩\ket{N}. The values ofF0|0=0.86​(2)F_{0|0}=0.86(2)andF1|1=0.95​(2)F_{1|1}=0.95(2)are obtained from a least-squares fit to the data in Fig.3c. As discussed in the main text, these fidelities are limited by the fidelity of atomic control in our experiment.

To quantify the probability of a measurement-induced bit flip in the molecule, we fit the data in Fig.3b.
The contrast of this measurement corresponds to the probability that the molecular populations are unchanged by the atomic readout protocol.
A least-squares fit to the data yields cosine oscillations with a peak-to-peak contrast of1.014​(9)1.014(9)(Fig.3b, solid lines).
The fitted contrast from this unconstrained fit is slightly larger than the physical maximum of unity due to statistical fluctuations.
It corresponds to a lower bound on the probability of avoiding a measurement-induced bit flip of0.9960.996at the 95% confidence level.

The analysis above considers only bit-flip errors, since all fidelities are conditioned on successful recovery of the molecule at the end of the sequence.
As throughout this work, experimental runs in which the molecule is lost (that is, erasure errors) are discarded through postselection.
As discussed above, these losses arise primarily from coupling to other hyperfine states of the molecule caused by the 1012-nm light when its intensity is too high.


Atom-molecule entanglement.We quantify the fidelity of atom–molecule entanglement using the data shown in Fig.4d.
As described in the main text, the particles are entangled using aπ\pipulse on the Rydberg-excitation transition.
The coherence of the entangled state is then measured by applying a secondπ\pipulse with variable phase and mapping this phase onto the molecular populations using a Ramsey-style measurement.
The phase of the atomic Rydberg drive is transferred to the molecule when coherence exists between the two components of the Bell state|Ψ⟩\ket{\Psi}.
Therefore, the observed fringe contrast directly measures the entanglement coherence, giving𝒞=0.57​(1)\mathcal{C}=0.57(1).
The width of the region between the grey bands corresponds to the fidelity of molecular-state preparation which is0.87​(4)0.87(4).
Correcting for the imperfect molecular-state preparation gives a coherence of𝒞=0.66​(3)\mathcal{C}=0.66(3)for the entangled state.

As in experiments where entanglement is generated between identical molecules[43,42,44,40], we calculate the Bell-state fidelityF=12​(P↑↓+P↓↑+𝒞)F=\frac{1}{2}(P_{\uparrow\downarrow}+P_{\downarrow\uparrow}+\mathcal{C}). Here,P↑↓P_{\uparrow\downarrow}andP↓↑P_{\downarrow\uparrow}are the populations of the Bell-state components|3;5​s⟩\ket{3;5\mathrm{s}}and|2;83​d⟩\ket{2;83\mathrm{d}}.
From the data in Fig.3d, we estimateP↑↓+P↓↑=0.88​(4)P_{\uparrow\downarrow}+P_{\downarrow\uparrow}=0.88(4)when correcting for the state preparation of the molecule.
Combining this with the measured coherence𝒞\mathcal{C}gives an entanglement fidelity ofF=0.77​(3)F=0.77(3)when correcting for the imperfect state preparation of the molecule (this fidelity isF=0.67​(3)F=0.67(3)when not performing this correction).

The measured coherences and fidelities are primarily limited by imperfect driving of the atomic transition|5​s⟩→|83​d⟩\ket{5\mathrm{s}}\rightarrow\ket{83\mathrm{d}}.
In particular, the measured coherence is a lower bound on the true coherence because the same imperfect Rydberg drive is used both to create and to analyse the entangled state.
We emphasise that the values above are conditioned on successful recovery of the atom at the end of the experimental sequence, corresponding to postselection that excludes the22%22\%of runs in which the atom is lost.
Without this postselection, the corresponding entanglement fidelity is0.60​(2)0.60(2)when correcting for the molecular-state preparation, or0.52​(2)0.52(2)when not performing this correction.


Modelling the spin-exchange dynamics
We model the spin-exchange oscillations shown in Fig.4b using a two-state model.
In these experiments, we initially prepare the system in the pair state|4;83​d⟩\ket{4;83\mathrm{d}}by first exciting the molecule to|4⟩\ket{4}and subsequently exciting the atom to|83​d⟩\ket{83\mathrm{d}}. The pair state|4;83​d⟩\ket{4;83\mathrm{d}}is non-resonant, so the atomic excitation is not blockaded (see Fig.2d, inset) and the state does not evolve under any spin-exchange dynamics.

Spin-exchange dynamics are initiated by transferring the atom to|84​p⟩\ket{84\mathrm{p}}via a microwaveπ\pipulse on the transition|83​d⟩→|84​p⟩\ket{83\mathrm{d}}\to\ket{84\mathrm{p}}with Rabi frequencyΩMW/2​π=8.49​(9)\Omega_{\mathrm{MW}}/2\pi=8.49(9)\,MHz which is much greater than the coupling between the interacting pair states. This prepares the system in the state|4;84​p⟩\ket{4;84\mathrm{p}}, which is coherently coupled to|3;83​d⟩\ket{3;83\mathrm{d}}via the spin-exchange interaction. The dynamics in this subspace are described by the HamiltonianHse=(0V​(R)V​(R)h​δ),H_{\mathrm{se}}=\begin{pmatrix}0&V(R)\\
V(R)&h\delta\end{pmatrix},(16)

written in the basis{|3;83​d⟩,|4;84​p⟩}\{\ket{3;83\mathrm{d}},\ket{4;84\mathrm{p}}\}.
As above,V​(R)V(R)is the coupling between the states|3;83​d⟩\ket{3;83\mathrm{d}}and|4;84​p⟩\ket{4;84\mathrm{p}}.
During the interaction window, dynamics are restricted to this two-state manifold, while other pair states remain uncoupled.

To read out the spin-exchange dynamics, a secondπ\pipulse on the transition|83​d⟩↔|84​p⟩\ket{83\mathrm{d}}\leftrightarrow\ket{84\mathrm{p}}maps population in|3;83​d⟩\ket{3;83\mathrm{d}}to|3;84​p⟩\ket{3;84\mathrm{p}}, while population remaining in|4;84​p⟩\ket{4;84\mathrm{p}}is mapped back to|4;83​d⟩\ket{4;83\mathrm{d}}. A subsequentπ\pipulse on the transition|83​d⟩→|5​s⟩\ket{83\mathrm{d}}\to\ket{5\mathrm{s}}transfers population in|4;83​d⟩\ket{4;83\mathrm{d}}to the atomic ground state, resulting in atom recovery, whereas population in|3;84​p⟩\ket{3;84\mathrm{p}}remains in a Rydberg state and is detected as atom loss.
Finally, we detect remaining atoms and readout the molecular state as described above.

With this protocol, after microwave transfers, the population in|3;84​p⟩\ket{3;84\mathrm{p}}(Fig.4b, black points) isP3;84​p​(τ;R,δ)=V​(R)2V~​(R,δ)2​sin2⁡(2​π​τ​V~​(R,δ)h),P_{3;84\mathrm{p}}(\tau;R,\delta)=\frac{V(R)^{2}}{\widetilde{V}}(R,\delta)^{2}\sin^{2}\!\left(2\pi\tau\frac{\widetilde{V}(R,\delta)}{h}\right),(17)

where we have defined the generalised spin-exchange couplingV~​(R,δ)=V​(R)2+(h​δ/2)2.\widetilde{V}(R,\delta)=\sqrt{V(R)^{2}+(h\delta/2)^{2}}\,.(18)

The remaining population remains in|4;83​d⟩\ket{4;83\mathrm{d}}(Fig.4b, purple points).

Imperfect state preparation results in approximately38%38\%of experimental shots populating the two undesired subspaces: atom recovery when the molecule is in|3⟩\ket{3}, and atom loss when the molecule is in|4⟩\ket{4}. These events can be identified using the molecular state readout (see above) and are removed via postselection because they do not contribute to the spin-exchange dynamics of interest.
The first class of events (approximately3%3\%) arises from imperfect excitation of the molecule to|4⟩\ket{4}such that the molecule remains in|3⟩\ket{3}. Then, the atomic excitation is blockaded and the atom stays in the ground state throughout the sequence.
The second class (approximately35%35\%) corresponds to infidelity in the Rydberg excitation and could be substantially improved in the future.
Nevertheless, in both cases, no spin-exchange dynamics occur and the populations in these states are independent of the interaction timeτ\tau.

To model our experimental data, we perform a Monte Carlo simulation that accounts for shot-to-shot fluctuations in both the interparticle separationRRand the detuningδ\delta. For each realisation,RRis sampled from a Gaussian distribution with meanR¯\bar{R}and standard deviationσR\sigma_{R}, andδ\deltais sampled from a Gaussian distribution with meanδ¯\bar{\delta}and standard deviationσδ\sigma_{\delta}.
We take the interaction strength to beV​(R)=Vdd​(R)=C3/R3V(R)=V_{\mathrm{dd}}(R)=C_{3}/R^{3}, withC3/h=1.36​(15)​MHz​μ​m3C_{3}/h=1.36(15)\,\mathrm{MHz}\,\mu\mathrm{m}^{3}obtained from the fit to the blockade measurements shown in Fig.2d (see above).
For each Monte Carlo realisation, we evaluate the spin-exchange dynamics over an interaction timeτ\tauusing the model described above.
The experimentally observable probabilities are obtained by averaging overN=104N=10^{4}iterations and areP¯3;84​p​(τ)\displaystyle\overline{P}_{3;84\mathrm{p}}(\tau)=1N​∑i=1NP3;84​p​(τ;Ri,δi),\displaystyle=\frac{1}{N}\sum_{i=1}^{N}P_{3;84\mathrm{p}}(\tau;R_{i},\delta_{i}),(19)P¯4;83​d​(τ)\displaystyle\overline{P}_{4;83\mathrm{d}}(\tau)=1−P¯3;84​p​(τ).\displaystyle=1-\overline{P}_{3;84\mathrm{p}}(\tau).(20)

The mean separationR¯\bar{R}is independently determined from ac Stark shift measurements described above. The remaining free parametersσR\sigma_{R},σδ\sigma_{\delta}, andδ¯\bar{\delta}are extracted via least-squares fitting to the measured populations.
We attribute the fitted detuning fluctuations primarily to magnetic-field noise, while the fluctuations inRRarise from the finite wavefunction spread of the particles and the ejection of Rydberg atoms from the optical tweezers.


Data availability
The data that support the findings of this study are available
at [link to be inserted].


Acknowledgments
We thank K. Wadenpfuhl, C. S. Adams, and J. D. Pritchard for helpful discussions on experimental matters, M. Bergonzoni and G. Pupillo for discussions on molecular gates mediated by atoms, and H. R. Sadeghpour and A. M. Rey for theoretical discussions.
We acknowledge support from the UK Engineering and Physical Sciences Research Council (EPSRC) Grants EP/P01058X/1, EP/W00299X/1, EP/W016141/1, EP/Y01510X/1 and UKRI2226 funded through the Programme Grant Scheme, UK Research and Innovation (UKRI) Frontier Research Grant EP/X023354/1, the Royal Society, and Durham University.
R.G.F. and J.M.G.G. gratefully acknowledge financial support by the Spanish project PID2023-147039NB-I00.
J.M.G.G. acknowledges financial
support from the grant PRE2021-099603 funded by MICIU/
AEI/10.13039/501100011033 and by “ESF+”.


Author contributions
DKR, TRH, and CJHR performed the experiments. JMGC, RGF, and TRH performed the theoretical calculations. DKR, AG, and SLC conceptualised the experiments. All authors contributed to the analysis of the results. AG and SLC acquired funding for the experimental apparatus. DKR wrote the initial draft of the manuscript and all authors reviewed and edited it. RGF supervised the theoretical work. SLC supervised the overall project.


Competing interests
The authors declare no competing interests.


Correspondence and requests for materialsshould be addressed to Daniel K. Ruttley and Simon L. Cornish.

## 


- 


Major funding support from
