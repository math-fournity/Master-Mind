# Deterministic loading of molecular arrays by microwave-assisted collisions

**arXiv ID**: 2607.25783v2
**Authors**: Etienne F. Walraven, Kang Feng, Jonas Rodewald, Michael R. Tarbutt, Tijs Karman
**Published**: 2026-07-28
**Categories**: physics.atom-ph, cond-mat.quant-gas, physics.chem-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2607.25783v2

## Abstract

Molecular tweezer arrays offer great prospects for quantum simulation, sensing, and computing, and would benefit from methods that enhance loading efficiency. Whereas light-assisted collisions underpin enhanced loading methods for atomic tweezer arrays, this approach cannot be directly extended to molecular arrays due to collisional loss. We show how this collisional loss can be suppressed by shelving molecules in rotationally or vibrationally excited states, so that a shelved molecule interacts with a newly loaded molecule through a repulsive van der Waals interaction. By introducing microwave assisted collisions, we show how to control the final states and the energy released in a collision between a pair of molecules. Following this controlled collision, one of the two molecules can be ejected, and we explore several strategies for ensuring deterministic ejection. Our schemes rely on currently available techniques for laser-coolable molecules, and we predict achievable filling fractions up to 96%, paving the way for scalable molecular arrays.

## Full Text

Deterministic loading of molecular arrays by microwave-assisted collisions

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
- License: CC BY 4.0arXiv:2607.25783v2 [physics.atom-ph] 31 Jul 2026

## Deterministic loading of molecular arrays by microwave-assisted collisionsEtienne F. WalravenInstitute for Molecules and Materials, Radboud University, 6525 AJ Nijmegen, The NetherlandsKang FengInstitute for Molecules and Materials, Radboud University, 6525 AJ Nijmegen, The NetherlandsJonas RodewaldCentre for Cold Matter, Blackett Laboratory, Imperial College London, London SW7 2AZ, United KingdomMichael R. TarbuttCentre for Cold Matter, Blackett Laboratory, Imperial College London, London SW7 2AZ, United KingdomTijs Karmant.karman@science.ru.nlInstitute for Molecules and Materials, Radboud University, 6525 AJ Nijmegen, The Netherlands

## Abstract

Molecular tweezer arrays offer great prospects for quantum simulation, sensing, and computing, and would benefit from methods that enhance loading efficiency.
Whereas light-assisted collisions underpin enhanced loading methods for atomic tweezer arrays, this approach cannot be directly extended to molecular arrays due to collisional loss.
We show how this collisional loss can be suppressed by shelving molecules in rotationally or vibrationally excited states, so that a shelved molecule interacts with a
newly loaded molecule through a repulsive van der Waals interaction.
By introducing microwave assisted collisions, we show how to control the final states and the energy released in a collision between a pair of molecules. Following this controlled collision, one of the two molecules can be ejected, and we explore several strategies for ensuring deterministic ejection. Our schemes rely on currently available techniques for laser-coolable molecules, and we predict achievable filling fractions up to 96%, paving the way for scalable molecular arrays.

## IIntroduction

Arrays of neutral atoms and molecules using optical tweezer arrays have become a central platform in quantum information, quantum simulation, and quantum metrology[1]. Across these fields, there is an ever-increasing demand for scalable arrays, enabling higher stability optical clocks[2], simulation of more complex collective phenomena[3], and possible quantum advantage in quantum computing[4]. Currently, arrays may contain thousands of atoms[5,6,7,8,9,10], and tens of molecules[11,12,13,14]. For most applications, these arrays need to be free of defects. However, conventional tweezer loading relies on collisional blockade, leading to arrays that are stochastically filled with a probability of about 50% for atoms[15,16]and 30–40% for molecules[11,13,12,14]. Rearrangement of tweezers is therefore necessary, but the unfavorable scaling of rearrangement time with array size reduces the probability of successfully creating a defect-free array, constraining scalability. Deterministic preparation resulting in near-unity filling is therefore highly sought after.

Several methods have so far improved tweezer loading of atoms beyond the conventional 50% filling fraction. Dark-state enhanced loading is an iterative approach based on imaging the loaded atoms, shelving them into long-lived states that are dark to the loading dynamics, and lowering the trap depths of the loaded tweezers to inhibit further loading[17]. This approach has achieved a filling fraction of 84%. Similarly, a recent paper proposes to use repulsive barriers to protect loaded atoms from collisions[18]. Continuous operation schemes, on the other hand, use reservoirs to constantly refill the main atom array[19,5,6,9], achieving the highest filling fractions of up to 99%, yet requiring infrastructure for continuous rearrangement of tweezers. Lastly, light-assisted collisions have been used to eject all but one particle from each tweezer deterministically[20,21,22,23,24,25,26,27,28,29,30]. In such collisions, the detuning of the light provides a controlled energy release that can be tuned such that the probability for a single atom to escape the tweezer is maximized.
Using such schemes, the typical loading efficiency for atoms is around 80%[25],
while the highest reported array-averaged single-site occupancy is 93%[28].Figure 1:Sketch of a microwave-assisted collision with short-range repulsion and subsequent deterministic ejection.Molecules in rotational statesj+j′=1+3j+j^{\prime}=1+3experience repulsive rotational van der Waals interactions, reducing short-range loss. Dressing the molecule inj=3j=3toj=2j=2using microwaves creates resonant dipolar interactions between molecules inj=1j=1and the dressed state. In a microwave-dressed picture, as sketched here, the coupling due to the Rabi frequencyΩ\Omegaenables the inelastic process as shown in blue, releasing energy set by the detuningΔ\Delta. Processes resulting in residual loss from tunneling to the short range or from transitions to other hyperfine states are not illustrated. The post-collision energy release then enables the ejection of a single particle, either using an asymmetry in momenta from the initial temperature, by utilizing the various molecular tensor Stark shifts, or by actively pushing out one of the two molecules.

Polar molecules are a more recent addition to the field, with experiments already showing long coherence times in rotational states[31,32], as well as the implementation of quantum gates based on rotational qubits[12,13,33,32]. For laser-cooled molecules, stochastic loading probabilities have been observed between 30 and 40%[11,13,12,14], while enhanced methods have not been implemented yet. The iterative feedback-based schemes of Refs.[17,18]could also be applied to molecules. In earlier work, we proposed an iterative scheme to deterministically load laser-cooled molecules into tweezers with an efficiency up to 80%, by exploiting a dipolar blockade mechanism and collisional stability derived from a repulsive van der Waals interaction[34]. Here, we propose alternative enhanced loading methods for molecules inspired by the light-assisted collision schemes for atoms.

The core principle of atomic light-assisted collisions relies on non-adiabatic transitions during the collision between two atoms, where one atom is excited to a higher-lying electronic state by blue-detuned cooling light[35]. After excitation and subsequent spontaneous emission, the particles gain kinetic energy that is a fraction of the detuning[22,29]. For atoms at rest, this energy is shared equally between the atoms due to momentum conservation, but a momentum imbalance can arise from a non-zero initial temperature, so there is potential for just one particle to escape[20,22]. If both atoms remain trapped, subsequent elastic collisions can redistribute the momentum, and there can be multiple light-assisted collisions. Consequently, light-assisted collisions can eject all but a single atom, thereby loading tweezers deterministically with single atoms. For ultracold molecules, this concept cannot be applied directly as short-range encounters typically result in universal loss rather than elastic collisions[36,37,38,39,40,41]. This universal loss prevents enhanced loading[34]. While microwave shielding could in principle create repulsive interactions that decrease this loss[42,43,44], it disrupts laser cooling by dressing thej=1j=1rotational state with another rotational state for which the cooling is not rotationally closed.

In this paper, we propose several strategies for the deterministic loading of optical tweezer arrays with laser-cooled molecules. They rely on three main components, as illustrated in Fig.1: shelving into states with repulsive interactions, controlled collisional energy release and deterministic single-molecule ejection.
The collisional loss that prevents direct application of light-assisted collisions is suppressed by exploiting a repulsive van der Waals interaction that arises when the colliding molecules are in different rotational or ro-vibrational states.
The controlled energy release can then be realized by dressing rotational states with microwaves, enabling a new type of collision process that we term microwave-assisted collisions (MWACs), analogous to light-assisted collisions (LACs) for atoms.
We describe how this engineered interaction leads to controlled energy release, whose efficiency we quantify through coupled-channels scattering calculations. Following this controlled collision, a single molecule can be ejected deterministically. We consider several single-molecule ejection methods: thermal ejection, push-beam ejection, trap-lowering ejection, and tensor-Stark ejection.
Based on these ideas, we present experimentally viable loading schemes, which iteratively increase the filling fraction of a molecular tweezer array.
When rotational van der Waals repulsion is utilized, we find that filling fractions of up to 87% can be achieved, limited by residual collisional loss. Using the stronger ro-vibrational van der Waals repulsion eliminates this collisional loss, leading to filling fractions up to 96%, limited by the lifetime of the vibrationally excited state.

## IIConcept

Our aim is to control the energy released in a collision between two tweezer-trapped molecules. To do that, the first challenge is to suppress the short-range encounters that produce uncontrolled, lossy collisions. We do this by engineering a repulsive van der Waals interaction that prevents the molecules from reaching short range. Consider a pair of molecules in rotational statesj,j′j,j^{\prime}and label this pair statej+j′j+j^{\prime}. Its energy isEj,j′=B​[j​(j+1)+j′​(j′+1)]E_{j,j^{\prime}}=B[j(j+1)+j^{\prime}(j^{\prime}+1)]. The van der Waals interaction is the second-order dipole-dipole coupling to other pair states. It is necessary to sum over all relevant pair states, but this sum may be dominated by a single term when one pair state,k+k′k+k^{\prime}, is much closer in energy than all the others. In this case the interaction is proportional to|⟨k|​d^​|j⟩|2​|⟨k′|​d^​|j′⟩|2/(R6​Δ​E)|\bra{k}\hat{d}\ket{j}|^{2}\,|\bra{k^{\prime}}\hat{d}\ket{j^{\prime}}|^{2}/(R^{6}\Delta E), whered^\hat{d}is the dipole operator andΔ​E=Ej,j′−Ek,k′\Delta E=E_{j,j^{\prime}}-E_{k,k^{\prime}}is the energy difference between the interacting pair states. WhenΔ​E\Delta Eis small and positive the interaction will be strong and repulsive. When|j′−j|≥2|j^{\prime}-j|\geq 2, the interaction is always repulsive[45]. Takingj+j′=1+3j+j^{\prime}=1+3as an example, the closest pair state is2+22+2, which lies lower in energy by2​B2Bresulting in repulsion at long range that is strong enough to effectively suppress short-range encounters. This repulsive interaction is ubiquitous for polar molecules where the rotational contribution to the van der Waals interaction far outweighs the electronic one. The repulsion can be made even stronger by using different ro-vibrational states. To see this, consider the pair of states(v,j)+(v′,j′)=(0,1)+(1,0)(v,j)+(v^{\prime},j^{\prime})=(0,1)+(1,0). The dipole-dipole interaction couples it to(0,0)+(1,1)(0,0)+(1,1)which is slightly lower in energy due to the small difference in the rotational constants ofv=0v=0andv=1v=1, givingΔ​E=2​(Bv=0−Bv=1)\Delta E=2(B_{v=0}-B_{v=1}). SinceΔ​E≪B\Delta E\ll B, this repulsive ro-vibrational van der Waals interaction[46]is much stronger than the repulsive rotational van der Waals interaction discussed above.

Having suppressed the unwanted short-range collisions, we now introduce a controlled microwave-assisted collision (MWAC) similar to the light-assisted collisions used for atoms. Figure1illustrates the idea for the case where the initial state isj+j′=1+3j+j^{\prime}=1+3, so that there is a repulsive rotational van der Waals interaction. A microwave field red detuned byΔ\Deltafrom thej′=3→2j^{\prime}=3\rightarrow 2transition brings1+21+2close to1+31+3in a dressed-state picture. The pair state1+21+2has a resonant dipole-dipole interaction whose repulsive branch crosses1+31+3at an interparticle distance set byΔ\Delta, and the microwave coupling turns this into an avoided crossing. As the molecules approach and separate, they traverse the crossing twice, and if one traversal is diabatic and the other adiabatic they will be transferred to1+21+2, gaining energyℏ​Δ\hbar\Delta. This energy release can then be used to to eject one of the two particles with high probability.

With these foundations, we can sketch the complete scheme for deterministic loading of a tweezer:
- 1.

Load– Load molecules inj=1j=1by laser cooling.
- 2.

MWAC– Apply a microwave field to induce a collision with a precise, chosen kinetic energy release.
- 3.

Eject– Allow one of the two molecules to escape, or actively drive it out.
- 4.

Shelve– Transfer the molecule to a state that has a repulsive van der Waals interaction withj=1j=1.
- 5.

Iterate– Repeat from step 1.

In the following sections, we describe each of these steps in detail. To give a concrete realization, we explain how the steps work for CaF molecules, since tweezer experiments with this species are already well advanced[11,41,12,13,47,48,49,50]. The same ideas will also work for other laser-cooled molecules. We make extensive use of the hyperfine components of the low-lying rotational states. For CaF, these are shown in Fig.2.Figure 2:CaF hyperfine structurein rotational states (a)j=0j=0, (b)j=1j=1, (c)j=2j=2, and (d)j=3j=3.
Panel (e) shows the hyperfine structure of apairof molecules inj+j′=0+1j+j^{\prime}=0+1. Here, color and line style encode hyperfine states inj=0j=0andj=1j=1, respectively. The hyperfine intervals are shown in MHz.

## IIILoad

Molecules in rotational statej=1j=1are loaded into optical tweezers using standard laser cooling methods[51]. Several gray molasses cooling schemes are available that reach temperatures of a fewμ\muK, both in free space and in optical traps[52,53]. These cooling schemes take about 1 ms to reach the equilibrium temperature. The loading time should be long compared to this so that loaded molecules are likely to be cold, but short enough that the probability of loading more than one molecule into a tweezer is small. Through the choice of density, we set the loading rate to about 20 molecules per second, and choose a loading time of 5 ms, so that the average loading probability is about 0.1 per tweezer in each loading cycle.

CaF, and similar laser-coolable molecules, have four hyperfine components withinj=1j=1, arising from spin-rotation and electron-nuclear spin interactions. They aref=0,1−,1+,2f=0,1^{-},1^{+},2whereffis the total angular momentum quantum number and the two states withf=1f=1are distinguished by the±\pmsuperscript, with1−1^{-}having the lower energy.
This hyperfine structure is illustrated in Fig.2(b).
Laser cooling tends to leave molecules distributed amongst the 12 Zeeman sub-levels of these four hyperfine states, but the subsequent steps work best for molecules in a single quantum state. We suggest using the deep cooling method described in[52], because it reaches temperatures around 5μ\muK, is robust to the tensor Stark shifts produced by the tweezer light, and drives the molecules towards a dark state withinf=2f=2only. If necessary, the cooling step can be followed by a brief optical pumping pulse that prepares molecules in a single state. In particular, the state(f,mf)=(2,2)(f,m_{f})=(2,2)[or(2,−2)(2,-2)] can be prepared with high fidelity[48].

## IVMicrowave-assisted collisions

To help understand microwave-assisted collisions (MWACs), we first review the light-assisted collisions used for atoms. At long range, the interaction between two ground state atoms is an attractive van der Waals interaction. The interaction between a ground state atom and an excited atom is a resonant dipole-dipole interaction with an attractive branch and a repulsive branch.
In a dressed-state picture, for positive, blue detuning, the van der Waals state crosses the repulsive dipole-dipole state at the so-called Condon point.
The coupling of the states by the light turns this into an avoided crossing.
If the approaching particles traverse the crossing diabatically, they will have a short-range encounter. If they traverse the crossing adiabatically they will repel and separate, traversing the crossing again on their way out. If this second crossing is diabatic, the particles will gain kinetic energy equal to the detuning (or some fraction of it, see below). This is a light-assisted collision with a controlled energy release. However, the probability of a short-range encounter is always greater than that of the light-assisted collision[34]. For atoms, this is not an issue, as short-range collisions lead to redistribution of momentum. For molecules, on the other hand, this leads to universal loss, and for such an approach to work, we require the interaction between the two molecules to be repulsive at shorter separation than the Condon point.

Instead of using light to couple electronic states, we use microwaves to couple rotational states, as illustrated in Fig.1and described in Sec.II. This has two major advantages: we can utilize the repulsive van der Waals interactions described in Sec.II, and the rotational states have such long lifetimes that spontaneous emission is negligible. In contrast to atomic light-assisted collisions, where a non-deterministic fraction of the detuning is released as kinetic energy by fast spontaneous emission[29], MWACs yield the precisely detuning as the energy release. It follows that a molecule can be ejected through a single collision as the energy release is well defined. We explore this in Sec.V. In this section, we consider the MWAC process for molecule pairs in the same vibrational state (utilizing rotational van der Waals repulsion) and for molecules in different vibrational states (utilizing ro-vibrational van der Waals repulsion).

## IV.1Calculation methods

We calculate collision rates through coupled-channels scattering calculations using the renormalized Numerov method[54], with a short-range absorbing boundary condition and long-rangeSS-matrix boundary conditions[55]. We treat the molecules as rigid rotors with hyperfine structure, tensor Stark shifts and microwave-dressed states, interacting via electrostatic interactions through the dipole and quadrupole moments, including the electronic van der Waals interaction, as described in more detail in Refs.[45,56,42].
Molecular vibrations are included as described in Ref.[46].
We then define the collisional MWAC efficiencyPMWACP_{\mathrm{MWAC}}using collision rate coefficientskkof the various processes asPMWAC=kMWACkMWAC+kshort+kinel,P_{\mathrm{MWAC}}=\frac{k_{\mathrm{MWAC}}}{k_{\mathrm{MWAC}}+k_{\mathrm{short}}+k_{\mathrm{inel}}}\,,(1)

where ‘short’ and ‘inel’ respectively stand for all short-range and inelastic loss processes, excluding the inelastic rates to desired microwave-dressed channels. The residual loss consists of short-range loss by tunneling through the barrier set by the repulsive van der Waals interaction, as well as inelastic loss to undesired channels, especially nearby hyperfine states.

## IV.2MWAC using purely rotational statesFigure 3:Microwave-assisted collision (MWAC) efficiency. (a) Efficiency as a function of Rabi frequencyΩ\Omegaand detuningΔ\Deltaforj+j′=0+2j+j^{\prime}=0+2withm=m′=0m=m^{\prime}=0. We have assumed a temperature of 5μ\muK and a microwave field on the transitionj=2→1j=2\to 1. These results do not account for hyperfine structure and tensor Stark shifts. (b) Efficiency forΩ=1×2​π\Omega=1\times 2\piMHz, where the blue curve represents the data from (a), as indicated by the blue line. The data points in green are forj+j′=1+3j+j^{\prime}=1+3in hyperfine states(j,f,mf)+(j′,f′,mf′)=(1,2,1)+(3,4,4)(j,f,m_{f})+(j^{\prime},f^{\prime},m_{f}^{\prime})=(1,2,1)+(3,4,4), with a microwave field on(j′,f′,mf′)=(3,4,4)→(2,3,3)(j^{\prime},f^{\prime},m_{f}^{\prime})=(3,4,4)\to(2,3,3)and tensor Stark shifts set by tweezer depths ofℏ​Δ/2\hbar\Delta/2.

The MWAC efficiency,PMWAC,P_{\mathrm{MWAC}},is defined above as the branching of collision rates to the desired energy release. This efficiency depends on the detuningΔ\Deltaand Rabi frequencyΩ\Omegaof the microwave field. To build intuition, we first explore this parameter space for CaF molecules in(j,mj)=(0,0)(j,m_{j})=(0,0)and(2,0)(2,0)with a microwave field addressingj=2→1j=2\to 1. This is the simplest case for which MWACs can be engineered, which is also computationally the least expensive, while it preserves the essential features. For simplicity, we neglect hyperfine structure and tensor Stark shifts due to the tweezer in this case, with results converged toL=7L=7partial waves at a temperature of 5μ\muK. Figure3(a) shows the calculated MWAC efficiency as a function ofΔ\DeltaandΩ\Omega. We see that the efficiency can be high for a very wide range ofΩ\OmegaandΔ\Deltavalues, providedΩ\Omegais between0.01​Δ0.01\DeltaandΔ\Delta. The optimum occurs whenΩ∼0.1​Δ\Omega\sim 0.1\Delta. As we discuss in Sec.V, a detuning of about twice the trap depth enables efficient ejection of molecules. Efficient loading typically requires a trap depth of at leastV0/h=5V_{0}/h=5MHz, so a realistic lower bound for the detuning isΔ∼10×2​π\Delta\sim 10\times 2\piMHz, calling forΩ∼1×2​π\Omega\sim 1\times 2\piMHz. The blue line in Fig.3(b) shows the efficiency versusΔ\DeltaatΩ=1×2​π\Omega=1\times 2\piMHz. It reaches 97.5% atΔ=4×2​π\Delta=4\times 2\piMHz, falling to 95% atΔ=10×2​π\Delta=10\times 2\piMHz and dropping below 90% forΔ>20×2​π\Delta>20\times 2\piMHz.

Since laser cooling leaves molecules inj=1j=1, we next consider the case where one molecule is inj=1j=1and the other is shelved inj=3j=3, as sketched in Fig.1. We engineer MWACs by applying microwaves on thej′=3→2j^{\prime}=3\to 2transition. This dressing does not interfere with the laser cooling of the molecules inj=1j=1, which means that the dressing can be applied continuously.

While MWACs can work for any of the hyperfine states(f,mf)(f,m_{f}), it works better for some states than others, so we need to consider the optimum choice. First, we note that the tensor Stark shift causes molecules in different(f,mf)(f,m_{f})to experience different tweezer depths. For the energy release after MWAC to be as well-defined as possible, we prefer to pump into a specific(f,mf)(f,m_{f})state withinj=3j=3. Figure2(d) shows these states. A suitable choice is(j,f,mf)=(3,4,4)(j,f,m_{f})=(3,4,4). We show how to shelve into this state in Sec.VI. The microwave field needed for MWAC is then tuned close to resonance with the transition(j,f,mf)=(3,4,4)→(2,3,3)(j,f,m_{f})=(3,4,4)\to(2,3,3).Figure 4:Microwave-dressed CaF interaction potentials.(a,b) Molecules are in different rotational states with microwave dressing on(j,f)=(3,4)→(2,3)(j,f)=(3,4)\to(2,3). (c) Molecules are in different ro-vibrational states with microwave dressing on(v,j,f)=(0,2,2−)→(0,1,1−)(v,j,f)=(0,2,2^{-})\to(0,1,1^{-}). The blue arrows indicate the MWAC trajectories. The three panels show the scenarios where the post-MWAC states experience (a) dipole-dipole, (b) hyperfine van der Waals and (c) ro-vibrational van der Waals interactions. OnlyL=0L=0and 2 are shown here with (a,b)Mtot=0M_{\mathrm{tot}}=0and (c)Mtot=3M_{\mathrm{tot}}=3.

Figure4shows the adiabatic interaction potentials obtained by diagonalization of the full Hamiltonian, except radial kinetic energy, at every intermolecular distanceRR. In Fig.4(a), we focus on the case(j,f)+(j′,f′)=(1,2)+(3,4)(j,f)+(j^{\prime},f^{\prime})=(1,2)+(3,4).
The microwave dressing is on the transition(j,f)=(3,4)→(2,3)(j,f)=(3,4)\to(2,3).
Because the interaction between(j,f)=(1,2)(j,f)=(1,2)and(2,3)(2,3)is dipolar, scaling asR−3R^{-3}, the Condon points with(1,2)+(3,4)(1,2)+(3,4)are formed at large distances. For the other hyperfine states ofj=1j=1(f=1−,0,1+f=1^{-},0,1^{+}), dipolar selection rules prevent first-order coupling, leading to repulsiveR−6R^{-6}hyperfine van der Waals interactions[56]. This interaction is stronger than the rotational van der Waals, so we still obtain Condon points but at shorter distances than for the dipolar case,
as seen in Fig.4(b) forj=1,f=1−j=1,f=1^{-}.
Consequently, the range of detunings where MWAC is effective is smaller whenf≠2f\neq 2. Nevertheless, for our particular choice of detuning (Δ=10×2​π\Delta=10\times 2\piMHz), we find that the collisional loss and MWAC rates are comparable amongst allfffor the(1,f)+(3,4)(1,f)+(3,4)states so that MWAC can be effective in all cases. This is helpful because, although the deep laser cooling scheme[52]drives molecules into a dark state(j,f,mf)=(1,2,±1)(j,f,m_{f})=(1,2,\pm 1), the molecules also spend time in the other hyperfine states. In summary, we propose to use the following CaF hyperfine states:(j,f,mf)=(1,2,±1)(j,f,m_{f})=(1,2,\pm 1)from deep laser cooling,(3,4,4)(3,4,4)as the shelved state, with microwaves red detuned from(2,3,3)(2,3,3).

Using the methods described above, we calculate collision rate coefficients for one molecule in(j,f,mf)=(1,2,±1)(j,f,m_{f})=(1,2,\pm 1)and the other in in(3,4,4)(3,4,4), with a microwave field close to the(3,4,4)→(2,3,3)(3,4,4)\to(2,3,3)transition, using a basis set up toL=5L=5. Here, we include hyperfine structure and tensor Stark shifts. We take a tweezer depth ofV0=ℏ​Δ/2V_{0}=\hbar\Delta/2, a scalar polarizability ofα0=1.4×10−3\alpha_{0}=1.4\times 10^{-3}Hz/(W/m2) and a tensor polarizability ofα2=−0.8×10−3\alpha_{2}=-0.8\times 10^{-3}Hz/(W/m2), which are the appropriate values for a CaF molecule at 780 nm. The green points in Fig.3(b) show the results atΩ=1×2​π\Omega=1\times 2\piMHz, for three different values ofΔ\Delta. The MWAC efficiency is 95.5% atΔ=5×2​π\Delta=5\times 2\piMHz, and 90.0% atΔ=10×2​π\Delta=10\times 2\piMHz. We also see from Fig.3(b) that the results for this case are not too far from the results obtained for the simplerj+j′=0+2j+j^{\prime}=0+2system where hyperfine structure and tensor Stark shifts were neglected, indicating that the simpler calculation can be a reliable guide.

## IV.3MWAC using ro-vibrational states

Next, we consider the case where the molecules are shelved in a different rotation-vibration state(v,j)=(2,0)(v,j)=(2,0). This has the advantage of almost eliminating the residual collisional loss because the repulsive ro-vibrational van der Waals interaction[46]between a(v,j)=(2,0)(v,j)=(2,0)molecule and a(v,j)=(0,1)(v,j)=(0,1)molecule is far more effective than the rotational van der Waals interaction. The scheme is similar to the one sketched in Fig.1: the new molecule loaded in(v,j)=(0,1)(v,j)=(0,1)is first transferred to(0,2)(0,2)using a short microwave pulse, and then the same microwave field induces a MWAC by dressing between(2,0)+(0,1)(2,0)+(0,1)(ro-vibrational van der Waals) and(2,0)+(0,2)(2,0)+(0,2)(rotational van der Waals). This produces molecules in the pair state(2,0)+(0,1)(2,0)+(0,1)with a tuneable energy release. To illustrate this, we show adiabatic interaction potentials using these ro-vibrational states in Fig.4(c). Since the ro-vibrational van der Waals is stronger than the rotational one, Condon points are formed between the prepared and MWAC channels.
After the MWAC, one of the molecules is ejected, see Sec.V.
Microwave pulses transfer the retained molecule to(2,1)(2,1)or(0,1)(0,1), followed by re-cooling (the same cooling light works for both cases) and shelving in(v,j)=(2,0)(v,j)=(2,0), see Sec.VI. After each iteration, more tweezers will be filled with single molecules in(v,j)=(2,0)(v,j)=(2,0), but never more than one.Figure 5:Loss rates for shelving in ro-vibrational states.
Panels (a) and (b) correspond to shelving in(v,j)=(1,0)(v,j)=(1,0)and(2,0)(2,0), respectively.

Dashed (solid) denotef=0f=0(f=1f=1) of thej=0j=0molecule, whereas the colors encodef=1−,0,1+,2f=1^{-},0,1^{+},2of thej=1j=1molecule, see Fig.2.
Loss rates above10−1410^{-14}cm3/s are highlighted in red, indicating loss is not suppressed sufficiently to completely eliminate background collisional loss.

We quantify collisional loss rate coefficients by coupled-channels calculations as before,
but now including ro-vibrational energy level structure as explained in more detail in Ref.[46].
These calculations include AC tensor Stark shifts and are performed at a temperature of 5μ\muK, although the loss rate coefficients are essentially temperature independent in this regime.
The resulting rates are shown per pair of rotation-vibration-hyperfine states in Fig.5(a) and (b) for shelving inv=1v=1andv=2v=2, respectively.
Loss rates can be suppressed below10−1410^{-14}cm3/s, which almost eliminates collisional loss on all relevant timescales even for high in-tweezer densities exceeding101410^{14}cm-3.
However, such low loss rates only occur for hyperfine states in(v,j)+(v′,j′)=(v,0)+(0,1)(v,j)+(v^{\prime},j^{\prime})=(v,0)+(0,1)that are higher in energy than all hyperfine states in the pair(0,0)+(v,1)(0,0)+(v,1).
For shelving inv=1v=1, this is realized in many but not all hyperfine states, as can be seen in Fig.5(a).
In this case, the(0,0)+(1,1)(0,0)+(1,1)channel is lower by2​αe=1472\alpha_{e}=147MHz which is comparable to the combined hyperfine structure in both molecules[57].
By shelving inv=2v=2, the energy splitting is doubled, and collisional loss is effectively eliminated in every hyperfine state,
as can be seen in Fig.5(b).
Therefore, we propose shelving inv=2v=2despite its shorter radiative lifetime (120 ms) relative to that ofv=1v=1(240 ms).

Figure6shows the MWAC efficiency for shelving inv=2v=2,
defined as the fraction of collisions with the desired energy release equal to the detuning.
Panel (a) shows the MWAC efficiency for various choices of hyperfine states. The fidelity exceeds 90% for all choices and is 99% or higher in several cases.
These states can be prepared by optical pumping followed by microwave transfer.
Unlike the purely rotational case considered previously, the MWAC efficiency of this ro-vibrational shelving scheme is so high that the fidelity of tweezer loading is no longer limited by collisions but instead by the lifetime of the vibrationally excited state.

Figure6(b) shows the dependence of the MWAC efficiency on the detuning.
When compared to the case of purely rotational shelving, Fig.3(b),
it is apparent that the MWAC efficiency remains much closer to 100% for much deeper tweezers.
In the purely rotational case, this is attributed to the barrier height in thej+j′=1+2j+j^{\prime}=1+2channel,
which is limited by dipole-dipole coupling toj+j′=2+3j+j^{\prime}=2+3.
The detuning must be smaller than this maximum barrier height to form an effective Condon point, see Fig.4.
In the ro-vibrational case, the barrier height is similarly limited by coupling of the(v,j)+(v′,j′)=(1,0)+(0,1)(v,j)+(v^{\prime},j^{\prime})=(1,0)+(0,1)channel to(1,1)+(0,2)(1,1)+(0,2),
but the resulting repulsive barrier is much higher.
In fact, in this case the maximum detuning is no longer limited by the barrier height,
but rather by dressing with another hyperfine state that occurs in this particular case when the detuning exceeds 120 MHz.
The ability to perform efficient MWACs at much larger detunings suggests that this scheme could be effective for much deeper tweezers and higher temperature than the examples used in this paper (5 MHz depth and 5μ\muK temperature),
but we do not explore this further.Figure 6:MWAC efficiency for ro-vibrational shelving(a) computed for detuningΔ=10×2​π\Delta=10\times 2\piMHz and Rabi frequencyΩ=1×2​π\Omega=1\times 2\piMHz for various hyperfine states,
and (b) computed as a function of the detuning for a single pair of hyperfine states(v,j,f)+(v′,j′,f′)=(2,0,1)+(0,2,2−)(v,j,f)+(v^{\prime},j^{\prime},f^{\prime})=(2,0,1)+(0,2,2^{-}).
In all cases, the tweezer depth is half the detuning.

## VEjection

The MWAC releases kinetic energy, just like for light-assisted collisions in atomic enhanced loading. In the atomic case, it has been shown that the momentum asymmetry from the pre-collision temperature can lead to loss of a single atom after multiple collisions[20,22]. For molecules, we would like to eject one of the two molecules after a single collision. In this section, we explore several strategies to achieve this and determine their efficiencies. The strategies apply to the final states produced by both the rotational and ro-vibrational schemes; where we need to be specific we will focus on the rotational scheme.

## V.1Thermal ejection and the role of tensor Stark shifts

By choosing a collisional energy release that does not exceed twice the trap depth, we create a situation where one molecule could escape, while the other remains trapped.
The efficiency of single-molecule ejection from a trap depends on the trap depth and in-tweezer temperature prior to the collision. We consider molecules initially trapped in internal statesiiin tweezers of depthVi=V0​(1+gi)V_{i}=V_{0}(1+g_{i})with trapping frequencyωi=ω0​(1+gi)\omega_{i}=\omega_{0}\sqrt{(1+g_{i})}, whereV0V_{0}andω0\omega_{0}are the tweezer depth and frequency due to the isotropic part of the polarizability, andgig_{i}is the state-dependent modification due to the tensor Stark shift. After a MWAC, the molecules end up in final statesfif_{i}, releasing an amount of energy that is state-dependent throughℏ​Δ=ℏ​Δ0+V0​(gf1+gf2−gi1−gi2)\hbar\Delta=\hbar\Delta_{0}+V_{0}(g_{f_{1}}+g_{f_{2}}-g_{i_{1}}-g_{i_{2}}), withΔ0\Delta_{0}the detuning without tensor Stark shifts.Figure 7:Distribution of post-MWAC statesof the variousmf,mf′m_{f},m_{f}^{\prime}product pairs of(j,f,mf)=(1,2,mf)(j,f,m_{f})=(1,2,m_{f})and(2,3,mf′)(2,3,m_{f}^{\prime})after a MWAC between(1,2,1)(1,2,1)and(3,4,4)(3,4,4). These are obtained atΔ=10×2​π\Delta=10\times 2\piMHz,V0/h=5V_{0}/h=5MHz, andE/kB=5E/k_{B}=5μ\muK from the initialss-wave channelL=0L=0. The pairs are arranged from the largest positive to the largest negative tensor Stark shifts. For thermal ejection, we assume a uniform distribution as presented by the dashed line.

The MWAC products from a collision between our proposed hyperfine states(j,f,mf)=(1,2,1)(j,f,m_{f})=(1,2,1)and(3,4,4)(3,4,4)end up in the(1,2,mf)+(2,3,mf′)(1,2,m_{f})+(2,3,m_{f}^{\prime})manifold. Which finalmf,mf′m_{f},m_{f}^{\prime}states dominate depends on the dynamics of the MWAC. In Fig.7, we show the distribution of thesemf,mf′m_{f},m_{f}^{\prime}forΔ=10×2​π\Delta=10\times 2\piMHz,V0/h=5V_{0}/h=5MHz, andE/kB=5E/k_{B}=5μ\muK from the initialss-wave channel. The final states experience slightly varying tweezer depths, and to capture the efficiency of ejection, we need to account for this product distribution by averaging over the various final states. In the following, we approximate the final state distribution as a uniform distribution, since there are no particularly dominant post-MWAC states.

We investigated the efficiency of deterministic ejection using a simple Monte Carlo (MC) simulation, which randomly samples pre-collision momenta𝒑\bm{p}and center-of-mass positions𝑹\bm{R}for both molecules, as well as the direction of the momenta imparted by the collision. SinceT≪Vi/kBT\ll V_{i}/k_{B}, we approximate the tweezer to be harmonic withωx=ωy=50×2​π\omega_{x}=\omega_{y}=50\times 2\pikHz andωz=5×2​π\omega_{z}=5\times 2\pikHz, drawing the positions and momenta from their corresponding thermal Gaussian distributions. We then update the relative momentum vector to point in a uniformly distributed random direction, effectively assuming an isotropic collision cross section, with a magnitude corresponding to energy conservationpf2=pi2+2​μ​ℏ​Δ​(𝑹)p_{f}^{2}=p_{i}^{2}+2\mu\hbar\Delta(\bm{R}). Here, the energy released is position-dependent through the local trapping potential asℏ​Δ​(𝑹)=ℏ​Δ0+(V0−12​m​[ωx2​X2+ωy2​Y2+ωz2​Z2])​(gf1+gf2−gi1−gi2)\hbar\Delta(\bm{R})=\hbar\Delta_{0}+(V_{0}-\frac{1}{2}m[\omega_{x}^{2}X^{2}+\omega_{y}^{2}Y^{2}+\omega_{z}^{2}Z^{2}])(g_{f_{1}}+g_{f_{2}}-g_{i_{1}}-g_{i_{2}}). This yields final kinetic energies of the two molecules, and if either exceeds the local trapping potential, we classify that molecule as ejected. This ejected molecule does not return for secondary collisions.
This is in contrast to atomic enhanced loading, where due to spontaneous emission the energy release is typically a fraction of the detuning and not sharply-defined.
Therefore, the energy release is not necessarily sufficient to fully eject a single atom.
In that case, secondary light-assisted collisions take place that eventually eject an atom.

Figure8shows the ejection efficiency given our proposed(j,f,mf)=(1,2,1)(j,f,m_{f})=(1,2,1)and(3,4,4)(3,4,4)hyperfine states at a detuning of10×2​π10\times 2\piMHz, forT=0,5T=0,5and 50μ\muK.
The range of efficiencies for the individual finalmf,mf′m_{f},m_{f}^{\prime}states is indicated by the shaded regions around the uniform average shown by the solid curves, where for each final state we took10510^{5}MC samples. For each state, we obtaingig_{i}as a function ofV0V_{0}by calculating their AC Stark shift. For example, atV0/h=10V_{0}/h=10MHz, we findg(1,2,1)=−0.079g_{(1,2,1)}=-0.079andg(3,4,4)=0.19g_{(3,4,4)}=0.19.
The dotted curves represent the simplified scenario where we neglect the tensor Stark shifts, i.e.,gi=0g_{i}=0, such that all states experience the same tweezer depth.
In the low-temperature limit,T=0T=0, energy and momentum conservation require the post-collision momenta to be in opposite directions and with equal magnitude2​μ​ℏ​Δ\sqrt{2\mu\hbar\Delta}.
Thus, when the tweezer depths are the same for all states, it is impossible to eject only one of the two particles, and the single particle ejection efficiency is zero.
When we include the tensor Stark shifts of the various molecular states, the trap depths become unequal, which can aid in ejection.
While the kinetic energy is still shared equally, one of the molecules sees a shallower trap and is ejected.
This results in single-particle ejection efficiencies that reach 100% within a window of trap depths.
The width of this window is set by the state dependence of the trap depth.
This still holds after averaging over all final states in our case, as shown by the blue curve in Fig.8(a).

When the thermal energy is large compared to the difference in trap depths arising from the tensor shifts, it is nota prioriclear how much of the deterministic ejection survives.
One expects that the difference in trap depth less effectively aids ejection,
but on the other hand the unequal initial momenta can now also lead to single-molecule ejection.
From our MC simulations, we find the window of tweezer depths for which a single molecule is loaded broadens, while the peak performance declines.
The optimal tweezer depth shifts from aroundℏ​Δ0/2\hbar\Delta_{0}/2at low temperature, to deeper traps needed to hold on to the molecules with higher thermal energies.
In this regime, deterministic loading of single molecules is driven by the difference in pre-collision momenta, rather than by the difference in state-dependent trap depth.
In Fig.8(b), we highlight the different probabilities of loading zero, one, or two molecules forT=5T=5μ\muK.Figure 8:Thermal deterministic ejection efficiencyof molecules from an optical tweezer after a successful MWAC withΔ=10×2​π\Delta=10\times 2\piMHz. (a) Probability of ejection of a single molecule atT=0,5T=0,5and 50μ\muK, given initial states before the collision of(j,f,mf)=(1,2,1)(j,f,m_{f})=(1,2,1)and(3,4,4)(3,4,4). Solid curves represent a uniform average over all resultingmf,mf′m_{f},m_{f}^{\prime}states of(1,2,mf)+(2,3,mf′)(1,2,m_{f})+(2,3,m_{f}^{\prime}), with shaded areas between the minima and maxima across allmf,mf′m_{f},m_{f}^{\prime}states due to the state-specific tensor Stark shifts. The dotted curves neglect these Stark shifts. (b) Probabilities atT=5T=5μ\muK of retaining zero, one, or two molecules.

## V.2Active ejection

Instead of relying on the thermal energy and differential Stark shifts, we can take a more active approach. One option is to choose a detuning greater than twice the trap depth, so that both molecules can escape, and then rely on the laser cooling to re-capture the molecule that is inj=1j=1. The simulations we present below show that the cooling is too slow for this approach to work. A second option is to set the detuning smaller than twice the trap depth so that neither molecule escapes, drive out one of the molecules using a ‘push beam’, and cool the other one.
A third option is to again set the detuning smaller than twice the trap depth, re-cool thej=1j=1molecule, then briefly lower the trap depth so that the other molecule can escape.

## V.2.1Push-beam ejection in the purely rotational scheme

Consider the case where the detuning is less than twice the trap depth so that both molecules remain trapped, albeit at a higher energy. After a rotational MWAC, we havej+j′=1+2j+j^{\prime}=1+2and the collisional loss rate coefficient will be high due to resonant dipolar interactions. However, the energy release in a MWAC dramatically reduces the density of the two molecules in the tweezer, reducing the rate for the dipolar collisions.
The collision timescale is given by1τ=k​∭n1​(𝒒)​n2​(𝒒)​d𝒒.\frac{1}{\tau}=k\iiint n_{1}(\bm{q})n_{2}(\bm{q})\mathrm{d}\bm{q}\,.(2)

wherekkis the loss rate coefficient,nin_{i}is the density distribution of speciesii, and the integral is the density overlap.
The densityn​(𝒒)n(\bm{q})of the barely trapped molecule with massmmat constant energyEEin a trapV​(𝒒)V(\bm{q})is given by the microcanonical ensemble asn​(𝒒)\displaystyle n(\bm{q})=1N​∭δ​[E−p22​m−V​(𝒒)]​d𝒑\displaystyle=\frac{1}{N}\iiint\delta\left[E-\frac{p^{2}}{2m}-V\left(\bm{q}\right)\right]\mathrm{d}\bm{p}=4​π​mN​2​m​[E−V​(𝒒)],\displaystyle=\frac{4\pi m}{N}\sqrt{2m\left[E-V\left(\bm{q}\right)\right]}\,,(3)

withNNa normalization constant determined by setting the integral ofn​(𝒒)n(\bm{q})over all space equal to the total number of molecules.

Once the molecule inj=1j=1is cooled to the center of the trap, which takes about 1 ms, the density overlap corresponds well to the peak density of the molecule inj=2j=2. For a harmonic trap, this peak density evaluates tonharm​(𝟎)=(2​m3/2​ωx​ωy​ωz/π2)​E−3/2n_{\mathrm{harm}}(\bm{0})=(\sqrt{2}m^{3/2}\omega_{x}\omega_{y}\omega_{z}/\pi^{2})E^{-3/2}. Before cooling, with both molecules at an energyEE, the density overlap is a factor15​π/32≈1.4715\pi/32\approx 1.47smaller than the peak density. For a Gaussian trap, the density is slightly lower, and we evaluate the normalization constant by numerical integration. We assume here a trap with frequenciesωx=ωy=50×2​π\omega_{x}=\omega_{y}=50\times 2\pikHz andωz=5×2​π\omega_{z}=5\times 2\pikHz with depthV0/h=10V_{0}/h=10MHz, where we chooseΔ=10×2​π\Delta=10\times 2\piMHz, such that molecules are excited toE/h=5E/h=5MHz. Withj=1j=1at energies betweenE/h=5E/h=5MHz andE/kB=5E/k_{B}=5μ\muK during cooling, the overlap density ranges from3.8×10103.8\times 10^{10}to5.7×10105.7\times 10^{10}cm-3. Using coupled-channels calculations, we find the dipolar collision rate between molecules inj=1j=1and 2 at a collision energy of 5 MHz to bek∼1.0×10−9k\sim 1.0\times 10^{-9}cm3/s. For the highest density overlap, this gives a collisional timescale ofτ∼17\tau\sim 17ms, which is long compared to other relevant timescales.
Alternatively, optical pumping ofj=2→4j=2\rightarrow 4can completely eliminate this loss from dipolar collisions.

While thej=1j=1molecule is being cooled, thej=2j=2molecule can be ejected by using a resonant laser that pushes it out of the trap. The push is a constant force that tilts the trap potential, making it shallower in the push direction. We use Monte Carlo simulations to model these processes. The initial velocities and positions of the two trapped molecules are drawn at random assuming a thermal distribution at temperatureTT. In the centre-of-mass frame, a collision at timet=0t=0imparts equal and opposite momenta with a random orientation, adding an energy ofℏ​Δ/2\hbar\Delta/2to each molecule. We then simulate the trajectories of the two molecules in the tweezer trap. In addition to the restoring force of the trap, there is a damping force for thej=1j=1molecule due to the laser cooling. We take the velocity-dependent force for the ‘single frequency’ deep laser cooling method given in Ref.[52]. Thej=2j=2molecule is pushed by a resonant laser beam that drives an optical cycling transition (B2​Σ+​(j=1)←X2​Σ+​(j=0,2)B^{2}\Sigma^{+}(j=1)\leftarrow X^{2}\Sigma^{+}(j=0,2)), applying a constant force along the axis of the tweezer. For both molecules, the momentum recoil due to photon absorption and spontaneous emission is included in the model. Forj=1j=1, we take a mean scattering rate of2×1052\times 10^{5}photons/s, resulting in an equilibrium temperature ofT=5T=5μ\muK. Forj=2j=2, the scattering rate is a parameter that we can vary. We simulate10410^{4}molecule pairs. We divide the space into volume elementsd​V\mathrm{d}Vand count the number of particles in each element to determine the density distributionsn1,2n_{1,2}of the two molecules as a function of time, Then we calculate the density overlap∑n1​n2​d​V\sum n_{1}n_{2}\mathrm{d}V. Multiplying this bykkgives the collision rate as a function of time.Figure 9:Ejecting a molecule with a resonant push beam.Overlap density of aj=1j=1andj=2j=2molecule as a function of time, determined from Monte Carlo simulations. A MWAC occurs att=0t=0, thej=1j=1molecule is re-cooled, and thej=2j=2molecule is pushed out in the axial direction of the tweezer. The legend gives the scattering rate due to the push beam. The tweezer has a depth of 5 MHz, a wavelength of 780 nm and a waist of 800 nm. The collision energy (detuning) is 0.5 times the trap depth.

Figure9shows how the overlap density evolves for four different values of the push force, determined by the scattering rate of the push beam. The overlap density first drops rapidly due to the energy released by the collision, then oscillates due to the radial oscillations in the tweezer, and continues to drop due to the push. When the push is strong (red line) it overwhelms the confining force of the trap and the particle is rapidly ejected. The overlap density drops below10910^{9}cm-3within 30μ\mus in this case. When the push is weak (blue line) the reduction in trap depth due to the tilt may not be sufficient to eject the molecule. Instead, it makes large amplitude oscillations in the trap so there is still a large reduction in density. We see that a scattering rate exceeding10610^{6}s-1is more than sufficient to eject the molecule rapidly. This is 10 times smaller than the maximum possible scattering rate on this transition, confirming the feasibility of this ejection method. Integrating the collision rate over time gives the probability of a dipolar collision. For the results shown in Fig.9, this probability is 6.0% for the weakest push and 2.4% for the strongest push.

## V.2.2Push-beam ejection in the ro-vibrational scheme

In the ro-vibrational scheme, shelved molecules are in(v,j)=(2,0)(v,j)=(2,0),
while after the MWAC a pair of molecules is in(2,0)+(0,1)(2,0)+(0,1). Instead of re-cooling thej=1j=1molecule, we eject it using a push beam resonant with the optical cycling transitionB2​Σ+​(j=0)←X2​Σ+​(j=1)B^{2}\Sigma^{+}(j=0)\leftarrow X^{2}\Sigma^{+}(j=1). Note that the pair(v,j)+(v′,j′)=(2,0)+(0,1)(v,j)+(v^{\prime},j^{\prime})=(2,0)+(0,1)does not experience fast loss by dipolar collisions. Instead, due to the ro-vibrational van der Waals repulsion, the loss is negligible, making the ejection fully deterministic in this scheme.

## V.2.3Trap-lowering ejection in the ro-vibrational scheme

Consider the case where the detuning is less than twice the trap depth so that after a MWAC both molecules remain trapped.
In either scheme, one of the molecules is inj=1j=1and can be re-cooled on a 1 ms timescale.
After this, the tweezer trap depth can be temporarily lowered,
resulting in the ejection of the second molecule.
In tweezers that contain only a shelved or only a newly loaded molecule,
no MWAC occurred and the single molecule is already cold, and is not ejected.
Trap-lowering ejection is not recommended for the purely rotational scheme,
where dipolar collisions lead to loss before ejection on the timescale needed for re-cooling of thej=1j=1molecule.
For the ro-vibrational scheme, however, collisional loss is essentially eliminated,
enabling almost deterministic ejection.

## V.3Enhancing tensor Stark shifts

Another ejection strategy exploits the different tensor Stark shifts of the rotational states. At low temperatures, we found that a window in tweezer depths exists where deterministic ejection can be 100%, as was shown in Fig.8(a). This window grows with increasing differential Stark shifts. We envision such conditions could be achieved with ‘anti-magic’ tweezers. In contrast to magic conditions where the anisotropic polarizability vanishes[58,31,32], the wavelength could also be chosen to deliberately increase the difference in polarizability. This asymmetry in tweezer depths could then enable more efficient and deterministic ejection of one of the particles. This requires the difference in tweezer depth to be large compared tokB​Tk_{B}T. To give some examples for CaF,α2≈0.75​α0\alpha_{2}\approx 0.75\alpha_{0}at 650 nm, andα0\alpha_{0}crosses zero near 546 nm whileα2\alpha_{2}remains large.

## VIShelving

Following ejection, each tweezer contains a single molecule, but this can be in one of several states.
In all cases, we wish to bring the molecule back into the cooling cycle, cool it, and finally shelve it.

## VI.1Shelving in the purely rotational scheme

Depending on the ejection scheme and on whether molecules were loaded in the current and previous cycle,
the remaining molecule can be in one of a number of states.
For example, thermal ejection in the purely rotational scheme retains a molecule in eitherj=1j=1orj=2j=2, or a previously shelvedj=3j=3molecule.
These can all be brought to the same state by first transferring collided(j,f)=(2,3)(j,f)=(2,3)molecules to(j,f)=(3,3)(j,f)=(3,3)using a microwave pulse that does not affect molecules shelved in(3,4)(3,4).
Subsequentlyj=3j=3molecules can be “de-shelved” by driving all hyperfine components ofB2​Σ+​(j=2)←X2​Σ+​(j=3)B^{2}\Sigma^{+}(j=2)\leftarrow X^{2}\Sigma^{+}(j=3).

The final step is to shelve these molecules irreversibly into(j,f,mf)=(3,4,4)(j,f,m_{f})=(3,4,4). This can be done by simultaneously driving all hyperfine components ofB2​Σ+​(j=2)←X2​Σ+​(j=1)B^{2}\Sigma^{+}(j=2)\leftarrow X^{2}\Sigma^{+}(j=1)and ofB2​Σ+​(j=2)←X2​Σ+​(j=3)B^{2}\Sigma^{+}(j=2)\leftarrow X^{2}\Sigma^{+}(j=3). The latter transition should be driven with bothπ\piandσ+\sigma^{+}components leaving(3,4,4)(3,4,4)as the only dark state in the system.

## VI.2Shelving in the ro-vibrational scheme

In the ro-vibrational scheme, molecules could be in(v,j)=(0,1)(v,j)=(0,1),(0,2)(0,2), or(2,0).(2,0).These can all be brought to the same state by microwave couplingj=1→2j=1\rightarrow 2inv=0v=0andj=0→1j=0\rightarrow 1inv=2v=2,
while applying laser cooling with thev=1v=1re-pump turned off, producing(v,j)=(1,1)(v,j)=(1,1).

After re-cooling these molecules, we wish to shelve them into(v,j)=(2,0)(v,j)=(2,0). The hyperfine state is less important because the loss suppression and the MWAC efficiency are high for all hyperfine states (see Fig.5(b) and Fig.6(a)). There are several ways to reach this state. One way is to turn off one hyperfine component of thev=2v=2repump light used in the laser cooling so that the molecule is pumped into that hyperfine component of(2,1)(2,1), and then apply a microwave pulse to transfer to(2,0)(2,0). Another way is to first use standard optical pumping within(0,1)(0,1), then transfer to(0,0)(0,0)with a microwave pulse, and finally apply a Ramanπ\pi-pulse to transfer to(2,0)(2,0), e.g., viaA2​Π1/2​(v=1)A^{2}\Pi_{1/2}(v=1).

## VIIIteration

The sequence of steps is iterated in order to accumulate single molecules in the tweezers.
The filling fraction of tweezers afternncycles,φn\varphi_{n}, depends on the filling fraction in the previous cycle.
During a new cycle,kkmolecules are loaded into a tweezer with Poissonian probabilitypk=λk​e−λ/k!p_{k}=\lambda^{k}e^{-\lambda}/k!,
whereλ\lambdais the loading rate multiplied by the duration of a cycle.
The overall filling fraction can then be defined recursively asφn=\displaystyle\varphi_{n}=\;φn−1​[p0+(∑even​k≥2pk)+P​(∑odd​kpk)]\displaystyle\varphi_{n-1}\Bigg[p_{0}+\Big(\sum_{\mathrm{even}\ k\geq 2}p_{k}\Big)+P\Big(\sum_{\mathrm{odd}\ k}p_{k}\Big)\Bigg]+(1−φn−1)​[∑odd​kpk].\displaystyle+(1-\varphi_{n-1})\Big[\sum_{\mathrm{odd}\ k}p_{k}\Big]\,.(4)

The last term, proportional to(1−φn−1)(1-\varphi_{n-1}), describes loading of empty tweezers in the collisional blockade regime.
The remaining terms, all proportional toφn−1\varphi_{n-1}, describe the probability that a loaded tweezer remains loaded.
We distinguish three cases.
If no new molecules are loaded, the shelved molecule remains.
If an even number of molecules is loaded, parity projection removes them rapidly in pairs before the MWAC is initiated at the end of the cycle, and so again the shelved molecule remains.
If an odd number of molecules is loaded, parity projection removes all but one molecule before the MWAC is initiated.
The remaining pair of one shelved and one newly loaded molecule is then converted to a single molecule with efficiencyPP.

In the above, the total single-molecule removal efficiencyP=PMWAC​Peject​Pbg​PspontP=P_{\mathrm{MWAC}}P_{\mathrm{eject}}P_{\mathrm{bg}}P_{\mathrm{spont}}is the product of four probabilities.PMWACP_{\mathrm{MWAC}}is the MWAC efficiency discussed in Sec.IV, andPejectP_{\mathrm{eject}}is the ejection efficiency discussed in Sec.V.
The probability that the co-trapped pair of shelved and newly loaded molecules survive the cycle, averaged over the new molecule’s arrival time, is given byPbg=τbgtcycle​[1−exp⁡(−tcycle/τbg)]P_{\mathrm{bg}}=\frac{\tau_{\mathrm{bg}}}{t_{\mathrm{cycle}}}[1-\exp(-t_{\mathrm{cycle}}/\tau_{\mathrm{bg}})]whereτbg\tau_{\mathrm{bg}}is the timescale for background collisions between co-trapped shelved and newly loaded molecules.
All relevant collision rate coefficients are summarized in Table1.
For the purely rotational scheme, given the background loss rate, a density of2.4×10132.4\times 10^{13}cm3, and a 5 ms cycle time, we findτbg=2\tau_{\mathrm{bg}}=2ms andPbg=37%P_{\mathrm{bg}}=37\%.
For the ro-vibrational scheme, collisions are so far suppressed thatτbg\tau_{\mathrm{bg}}exceeds seconds and effectivelyPbg=1P_{\mathrm{bg}}=1.
Finally,PspontP_{\mathrm{spont}}is the probability a shelved molecule remains in the shelved state for the duration of a cycle due to finite lifetime of the shelving state.
In the purely rotational scheme,Pspont=1P_{\mathrm{spont}}=1,
whereas in the ro-vibrational schemePspont=exp⁡(−tcycle/τ)≈96%P_{\mathrm{spont}}=\exp(-t_{\mathrm{cycle}}/\tau)\approx 96\%, given the 120 ms lifetime of thev=2v=2excited state.
If only one of these steps fails, tweezers loaded with an odd number of molecules will be empty,
either because the final MWAC and ejection step failed to convert the co-trapped pair to a single molecule,
or because background collisions or decay of the shelved state led to parity projection before the MWAC step is even initiated.
When no molecules were loaded, or an even number, none of these failures affect the loading fidelity
because, regardless of whether the shelved molecule is collisionally lost or decays,
a single molecule remains after parity projection, and the subsequent MWAC and ejection steps have no effect.Table 1:Collisional rate coefficients.
During loading by laser cooling, multiple hyperfine states inj=1j=1are explored, and the background loss rates relevant in the presence of a shelved molecule are given.
When the microwaves are turned on, MWACs occur at the rate shown.
In the ro-vibrational shelving scheme, MWACs are induced after state transfer of the newly loaded molecule, so the loading and MWAC stages pertain to different pairs of internal states for the pair of molecules.
All results are shown forT=5T=5μ\muK, where MWAC rates are calculated forΔ=10×2​π\Delta=10\times 2\piMHz andΩ=1×2​π\Omega=1\times 2\piMHz.
Rate coefficients are given to one digit since themfm_{f}andmf′m_{f}^{\prime}dependence affects the rates typically at the level of one to few tens of percents.Purely rotational schemeBackgroundMWAC rate(j,f)+(j′,f′)(j,f)+(j^{\prime},f^{\prime})loss rate (cm3/s)(cm3/s)Loading and MWAC(1,2)+(3,4)(1,2)+(3,4)1×10−111\times 10^{-11}2×10−102\times 10^{-10}(1,1+)+(3,4)(1,1^{+})+(3,4)2×10−112\times 10^{-11}2×10−102\times 10^{-10}(1,0)+(3,4)(1,0)+(3,4)1×10−111\times 10^{-11}1×10−101\times 10^{-10}(1,1−)+(3,4)(1,1^{-})+(3,4)1×10−111\times 10^{-11}1×10−101\times 10^{-10}Ro-vibrational scheme(v,j,f)+(v′,j′,f′)(v,j,f)+(v^{\prime},j^{\prime},f^{\prime})Loading(0,1,2)+(2,0,1)(0,1,2)+(2,0,1)1×10−171\times 10^{-17}-(0,1,1+)+(2,0,1)(0,1,1^{+})+(2,0,1)2×10−172\times 10^{-17}-(0,1,0)+(2,0,1)(0,1,0)+(2,0,1)5×10−175\times 10^{-17}-(0,1,1−)+(2,0,1)(0,1,1^{-})+(2,0,1)1×10−171\times 10^{-17}-MWAC(0,2,2−)+(2,0,1)(0,2,2^{-})+(2,0,1)-7×10−117\times 10^{-11}

The filling fraction afternncycles can be written in closed form asφn=1−[12​P+(1−12​P)​exp⁡(−2​λ)]n2−P.\displaystyle\varphi_{n}=\frac{1-\left[\frac{1}{2}P+\left(1-\frac{1}{2}P\right)\exp(-2\lambda)\right]^{n}}{2-P}\,.(5)

Figure10(a) shows the filling fraction given by Eq. (5) as a function of time, for some relevant values ofPP. The filling fraction increases in time towards the equilibrium value of of1/(2−P)1/(2-P). In the case wherePPis close to unity, this equilibrium is close toPP.
For the purely rotational scheme,1/(2−P)=60%1/(2-P)=60\%, limited primarily by background collisional loss,
and to a lesser extent by the efficiency of the MWAC and thermal ejection steps.
For the ro-vibrational scheme,1/(2−P)=96%1/(2-P)=96\%, limited by the finite lifetime of thev=2v=2vibrationally excited state.
For a loading rate of 20 molecules per second, this is reached in about 200 ms.
Given that loading of new molecules can operate in the collisional blockade regime, while(v,j)=(2,0)(v,j)=(2,0)collisional loss is negligible,
one could operate at a higher loading rate[15,16],
to reach the same performance even sooner.

Because the performance of the rotational scheme is limited by collisional loss, the scheme can be improved by applying the microwave dressing continuously to induce MWACs as soon as a second molecule is loaded. The ejection of aj=2j=2molecule using a push beam can also be applied continuously. Neither MWAC nor the ejection interfere with the laser cooling. This method eliminates the background collisional loss of co-trapped pairs so thatPbg=1P_{\mathrm{bg}}=1.
A potential drawback is that the MWAC may occur before the newly loaded molecule is cooled completely to the target temperature of5​μ5~\muK.
This would reduce the efficiency of thermal ejection, but not the efficiency of pushingj=2j=2molecules out with a resonant laser since this method does not rely on a sharply defined energy release.Figure 10:Loading efficiency of our proposed schemes. Filling fraction over time given a cycle duration of 5 ms, applying microwave pulses (a) at the end of each loading cycle, or (b) continuously. In all cases, we useΔ=10×2​π\Delta=10\times 2\piMHz,Ω=1×2​π\Omega=1\times 2\piMHz,V0/h=5V_{0}/h=5MHz andT=5T=5μ\muK. The dashed lines represent the steady-state efficiency in the limit of many cycles. Results in (b) are only shown using purely rotational states for a loading rate of 20 molecules/s, which improves the efficiency over sequential MWACs. (c) Dependence of the final steady-state filling fraction on the loading rate, when applying microwaves continuously. The dotted line indicates the loading rate that is illustrated in (b).

For this continuous MWAC method, the recurrence relation is modified toφn=\displaystyle\varphi_{n}=\;φn−1​[p0+(1−P)​(∑k≥2​evenpk)+P​(∑k​oddpk)]\displaystyle\varphi_{n-1}\Bigg[p_{0}+(1-P)\Big(\sum_{k\geq 2\ \mathrm{even}}p_{k}\Big)+P\Big(\sum_{k\ \mathrm{odd}}p_{k}\Big)\Bigg]+(1−φn−1)​[∑k​oddpk],\displaystyle+(1-\varphi_{n-1})\Big[\sum_{k\ \mathrm{odd}}p_{k}\Big]\,,(6)

where the main modification is in the term that describes loading of an even number of molecules into a previously loaded tweezer, withP=PMWAC​PejectP=P_{\mathrm{MWAC}}P_{\mathrm{eject}}.
Previously, this led to successful loading by parity projection before the MWAC was initiated,
but in this modified scheme the MWAC is initiated as soon as the first new molecule is loaded,
and hence parity projection results in an empty tweezer unless the initial MWAC was unsuccessful, with probability1−P1-P.
The filling fraction afternncycles can be written in closed form asφn=12(1−e−2​λ){1−[((1−P)e−2​λ+Pe−λ]n}1−(1−P)​e−2​λ−P​e−λ.\varphi_{n}=\frac{\frac{1}{2}(1-e^{-2\lambda})\left\{1-\left[(\left(1-P\right)e^{-2\lambda}+Pe^{-\lambda}\right]^{n}\right\}}{1-(1-P)e^{-2\lambda}-Pe^{-\lambda}}\,.(7)

In the case of perfect removal of single molecules,P=1P=1, Eq. (7) reduces toφn=12​(1+e−λ)​(1−e−n​λ)\varphi_{n}=\frac{1}{2}(1+e^{-\lambda})(1-e^{-n\lambda})with limitφ∞=12​(1+e−λ)\varphi_{\infty}=\frac{1}{2}(1+e^{-\lambda}),
limited by the finite loading rate. WhenP<1P<1, the largest fraction that can be obtained in the limit of slow loading is1/(2−P)1/(2-P), as before. Figure10(b) shows the filling fraction versus time as given by Eq. (7). We see that the steady state filling fraction is higher for this continuous scheme.
Figure10(c) shows the steady-state filling fraction versus the loading rate. Lower loading rates yield higher steady-state filling fractions, while requiring more cycles to reach that limit. Loading at 20 molecules/s yields a final fraction of 82% in the case of thermal ejection and 87% for active ejection. The limiting factors are the efficiencies of the MWACs and the ejection method.

## VIIIConclusionsFigure 11:Summary of recommended scheme using purely rotational states.Boxes show the steps with indicative timescales, with the 5 main steps highlighted in bold. For ejection, we push thej=2j=2molecule out. The table shows the state(s)(j,f,m)(j,f,m)of the molecule(s) at the end of each step, for three cases: a tweezer contains a shelved molecule and no new molecule is loaded; a tweezer does not contain a shelved molecule and a new molecule is loaded; or a tweezer contains a shelved molecule and a new molecule is loaded. Apart from shelving, all steps can be applied continuously.Figure 12:Summary of recommended scheme using ro-vibrational states.Boxes show the steps with indicative timescales, with the 5 main steps of the sequence highlighted in bold. For ejection, we push thej=1j=1molecule out. The table shows the state(s)(v,j)(v,j)of the molecule(s) at the end of each step, for three cases: a tweezer contains a shelved molecule and no new molecule is loaded; a tweezer does not contain a shelved molecule and a new molecule is loaded; or a tweezer contains a shelved molecule and a new molecule is loaded.

We have proposed schemes for near-deterministic loading of molecular tweezer arrays using microwave-assisted collisions and efficient ejection.
Microwave-assisted collisions between molecules enable controlled energy release, while keeping short-range collisional loss to a minimum using repulsive van der Waals interactions.
Two schemes are identified, one using the rotational van der Waals interaction[45], the other using a ro-vibrational van der Waals interaction[46].
For the subsequent deterministic single-molecule ejection, we have put forward several strategies: thermal ejection, push-beam ejection, trap-lowering ejection, and tensor Stark ejection.
Thermal ejection utilizes the controlled energy release in a similar way to atomic enhanced loading, but unlike the atomic case is not affected by spontaneous emission since the scheme involves only long-lived rotational states. The initial temperature provides asymmetry in the pre-collision momenta needed to eject a single molecule efficiently.
In push-beam ejection, the microwave-assisted collision produces molecules with energies below the trap depth so that both are retained. One of the two is then rapidly ejected using a resonant push beam.
The performance can be limited by collisions that occur between the MWAC and push pulse.
In the rotational scheme this is mitigated by the MWAC energy release which reduces the in-tweezer density,
whereas in the ro-vibrational scheme, the dipolar collisions are eliminated completely.
In trap-lowering ejection, both molecules are retained after the MWAC,
after which one of the molecules is re-cooled and the other ejected by temporarily reducing the tweezer trap depth.
Finally, in tensor Stark ejection, asymmetry in the state-dependent trapping potential is used to deterministically eject single molecules.

Figure11summarizes our recommended scheme using purely rotational states, where ejection is achieved by pushing out thej=2j=2molecule. The figure gives indicative timescales for these steps and shows the states of the molecules at the end of each step for the three cases where, after the loading step, the tweezer contains one molecule inj=3j=3(shelved from previous iteration), one molecule inj=1j=1(loaded in current iteration), or a molecule inj=3j=3and a molecule inj=1j=1. Apart from the shelving, all steps can be applied continuously, which is more efficient than a sequential scheme, yielding a filling fraction of 87%. Figure12shows our recommended scheme using ro-vibrational states. Here, we choose to push out thej=1j=1molecule and do the steps sequentially. The scheme has more rotational state transfer steps than the pure rotational scheme, but these can be done using microwaveπ\pi-pulses or rapid adiabatic passage which have very high fidelities[48]. All the steps are short compared to the loading time, so the scheme reaches near-determistic loading without increasing the loading time. The filling fraction of this scheme can be as high as 96%.

The predicted performance of our scheme is comparable to state-of-the-art enhanced loading of atoms,
which relies on light-assisted collisions that cannot be extended directly to molecules.
The required experimental tools – laser cooling, optical pumping, microwave dressing and rotational state transfer – are all demonstrated. This approach offers a practical route toward near-deterministic loading of molecular tweezers arrays and improved scalability for quantum simulation, sensing, and computing with ultracold molecules.

## Acknowledgements.This work was supported by NWO VIDI (grant ID 10.61686/AKJWK33335).
J.R and M.R.T acknowledge support by EPSRC through grants EP/W00299X/1 and UKRI2226.

## References
- Kaufman and Ni [2021]A. M. Kaufman and K.-K. Ni,Nature Phys.17, 1324 (2021).
- Ludlowet al.[2015]A. D. Ludlow, M. M. Boyd,
J. Ye, E. Peik, and P. O. Schmidt,Rev. Mod. Phys.87, 637 (2015).
- Ebadiet al.[2021]S. Ebadi, T. T. Wang,
H. Levine, A. Keesling, G. Semeghini, A. Omran, D. Bluvstein, R. Samajdar, H. Pichler, W. W. Ho,et al.,Nature595, 227 (2021).
- Daleyet al.[2022]A. J. Daley, I. Bloch,
C. Kokail, S. Flannigan, N. Pearson, M. Troyer, and P. Zoller,Nature607, 667 (2022).
- Gygeret al.[2024]F. Gyger, M. Ammenwerth,
R. Tao, H. Timme, S. Snigirev, I. Bloch, and J. Zeiher,Phys. Rev. Res.6, 033104 (2024).
- Norciaet al.[2024]M. Norcia, H. Kim,
W. Cairncross, M. Stone, A. Ryou, M. Jaffe, M. Brown, K. Barnes, P. Battaglino, T. Bohdanowicz,et al.,PRX Quantum5, 030316 (2024).
- Pichardet al.[2024]G. Pichard, D. Lim,
É. Bloch, J. Vaneecloo, L. Bourachot, G.-J. Both, G. Mériaux, S. Dutartre, R. Hostein, J. Paris,et al.,Phys. Rev. Appl.22, 024073 (2024).
- Linet al.[2025]R. Lin, H.-S. Zhong,
Y. Li, Z.-R. Zhao, L.-T. Zheng, T.-R. Hu, H.-M. Wu, Z. Wu, W.-J. Ma, Y. Gao,et al.,Phys. Rev. Lett.135, 060602 (2025).
- Chiuet al.[2025]N.-C. Chiu, E. C. Trapp,
J. Guo, M. H. Abobeih, L. M. Stewart, S. Hollerith, P. L. Stroganov, M. Kalinowski, A. A. Geim, S. J. Evered,et al.,Nature , 1 (2025).
- Manetschet al.[2025]H. J. Manetsch, G. Nomura,
E. Bataille, X. Lv, K. H. Leung, and M. Endres,Nature , 1 (2025).
- Anderegget al.[2019]L. Anderegg, L. W. Cheuk,
Y. Bao, S. Burchesky, W. Ketterle, K.-K. Ni, and J. M. Doyle,Science365, 1156 (2019).
- Hollandet al.[2023]C. M. Holland, Y. Lu, and L. W. Cheuk,Science382, 1143 (2023).
- Baoet al.[2023]Y. Bao, S. S. Yu,
L. Anderegg, E. Chae, W. Ketterle, K.-K. Ni, and J. M. Doyle,Science382, 1138 (2023).
- Vilaset al.[2024]N. B. Vilas, P. Robichaud,
C. Hallas, G. K. Li, L. Anderegg, and J. M. Doyle,Nature628, 282 (2024).
- Schlosseret al.[2001]N. Schlosser, G. Reymond,
I. Protsenko, and P. Grangier,Nature411, 1024
(2001).
- Schlosseret al.[2002]N. Schlosser, G. Reymond, and P. Grangier,Phys. Rev. Lett.89, 023005 (2002).
- Shawet al.[2023]A. L. Shaw, P. Scholl,
R. Finklestein, I. S. Madjarov, B. Grinkemeyer, and M. Endres,Phys. Rev. Lett.130, 193402 (2023).
- Baldocket al.[2026]A. C. Baldock, A. J. Matthies, L. Caldwell, and H. J. Williams,Near-deterministic loading of optical tweezer arrays via repulsive barricade
potentials(2026),arXiv:2604.22406 [physics.atom-ph].
- Pauseet al.[2023]L. Pause, T. Preuschoff,
D. Schäffner, M. Schlosser, and G. Birkl,Phys. Rev. Res.5, L032009 (2023).
- Grünzweiget al.[2010]T. Grünzweig, A. Hilliard, M. McGovern, and M. Andersen,Nature Phys.6, 951 (2010).
- Fuhrmaneket al.[2012]A. Fuhrmanek, R. Bourgain,
Y. R. Sortais, and A. Browaeys,Phys. Rev. A85, 062708 (2012).
- Sompetet al.[2013]P. Sompet, A. V. Carpentier, Y. H. Fung, M. McGovern, and M. F. Andersen,Phys. Rev. A88, 051401 (2013).
- Fung and Andersen [2015]Y. Fung and M. Andersen,New J. Phys.17, 073011 (2015).
- Lesteret al.[2015]B. J. Lester, N. Luick,
A. M. Kaufman, C. M. Reynolds, and C. A. Regal,Phys. Rev. Lett.115, 073003 (2015).
- Brownet al.[2019]M. Brown, T. Thiele,
C. Kiehl, T.-W. Hsu, and C. Regal,Phys. Rev. X9, 011057 (2019).
- Aliyuet al.[2021]M. M. Aliyu, L. Zhao,
X. Q. Quek, K. C. Yellapragada, and H. Loh,Phys. Rev. Res.3, 043059 (2021).
- Ang’Ong’Aet al.[2022]J. Ang’Ong’A, C. Huang,
J. P. Covey, and B. Gadway,Phys. Rev. Res.4, 013240 (2022).
- Jenkinset al.[2022]A. Jenkins, J. W. Lis,
A. Senoo, W. F. McGrew, and A. M. Kaufman,Phys. Rev. X12, 021027 (2022).
- Pampelet al.[2025]S. K. Pampel, M. Marinelli,
M. O. Brown, J. P. D’Incao, and C. A. Regal,Phys. Rev. Lett.134, 013202 (2025).
- Muzi Falconiet al.[2025]A. Muzi Falconi, R. Panza,
S. Sbernardori, R. Forti, R. Klemt, O. Abdel Karim, M. Marinelli, and F. Scazza,Phys. Rev. Lett.135, 203402 (2025).
- Gregoryet al.[2024]P. D. Gregory, L. M. Fernley, A. L. Tao,
S. L. Bromley, J. Stepp, Z. Zhang, S. Kotochigova, K. R. Hazzard, and S. L. Cornish,Nat. Phys.20, 415 (2024).
- Ruttleyet al.[2025]D. K. Ruttley, T. R. Hepworth, A. Guttridge, and S. L. Cornish,Nature637, 827 (2025).
- Picardet al.[2025]L. R. Picard, A. J. Park,
G. E. Patenotte, S. Gebretsadkan, D. Wellnitz, A. M. Rey, and K.-K. Ni,Nature637, 821 (2025).
- Walravenet al.[2024]E. F. Walraven, M. R. Tarbutt, and T. Karman,Phys. Rev. Lett.132, 183401 (2024).
- Baliet al.[1994]S. Bali, D. Hoffmann, and T. Walker,Europhys. Lett.27, 273 (1994).
- Takekoshiet al.[2014]T. Takekoshi, L. Reichsöllner, A. Schindewolf, J. M. Hutson, C. R. Le
Sueur, O. Dulieu,
F. Ferlaino, R. Grimm, and H. C. Nägerl,Phys. Rev. Lett.113, 205301 (2014).
- Vogeset al.[2020]K. K. Voges, P. Gersema,
M. M. zum Alten Borgloh,
T. A. Schulze, T. Hartmann, A. Zenesini, and S. Ospelkaus,Phys. Rev. Lett.125, 083401 (2020).
- Guoet al.[2018]M. Guo, X. Ye, J. He, M. L. González-Martínez,
R. Vexiau, G. Quéméner, and D. Wang,Phys. Rev. X8, 041044 (2018).
- Yeet al.[2018]X. Ye, M. Guo, M. L. González-Martínez, G. Quéméner, and D. Wang,Sci. Adv.4, eaaq0083 (2018).
- Gregoryet al.[2019]P. D. Gregory, M. D. Frye,
J. A. Blackmore, E. M. Bridge, R. Sawant, J. M. Hutson, and S. L. Cornish,Nat. Commun.10, 3104 (2019).
- Cheuket al.[2020]L. W. Cheuk, L. Anderegg,
Y. Bao, S. Burchesky, S. Y. Scarlett, W. Ketterle, K.-K. Ni, and J. M. Doyle,Phys. Rev. Lett.125, 043401 (2020).
- Karman and Hutson [2018]T. Karman and J. M. Hutson,Phys. Rev. Lett.121, 163401 (2018).
- Lassablière and Quéméner [2018]L. Lassablière and G. Quéméner,Phys. Rev. Lett.121, 163402 (2018).
- Anderegget al.[2021]L. Anderegg, S. Burchesky,
Y. Bao, S. S. Yu, T. Karman, E. Chae, K.-K. Ni, W. Ketterle, and J. M. Doyle,Science373, 779 (2021).
- Walraven and Karman [2024]E. F. Walraven and T. Karman,Phys. Rev. A109, 043310 (2024).
- Fenget al.[2026]K. Feng, H. Yang, H. J. Jóźwiak, and T. Karman,Ro-vibrational van der
waals interaction between ultracold polar molecules(2026),arXiv:2607.25774
[cond-mat.quant-gas].
- Luet al.[2024]Y. Lu, S. J. Li, C. M. Holland, and L. W. Cheuk,Nat. Phys.20, 389 (2024).
- Hollandet al.[2025]C. M. Holland, Y. Lu,
S. J. Li, C. L. Welsh, and L. W. Cheuk,Phys. Rev. X15, 031018 (2025).
- Luet al.[2026]Y. Lu, C. M. Holland,
C. L. Welsh, X.-Y. Chen, and L. W. Cheuk,Probing coherent
many-body spin dynamics in a molecular tweezer array quantum simulator(2026),arXiv:2603.19090 [cond-mat.quant-gas].
- Hollandet al.[2026]C. M. Holland, C. L. Welsh,
Y. Lu, D. Wellnitz, X.-Y. Chen, A. M. Rey, and L. W. Cheuk,Creating and probing
spin-squeezed states of molecules(2026),arXiv:2606.02500 [physics.atom-ph].
- Fitch and Tarbutt [2021]N. J. Fitch and M. R. Tarbutt, inAdv. At. Mol. Opt. Phys., Vol. 70 (Elsevier, 2021) pp. 157–262.
- Caldwellet al.[2019]L. Caldwell, J. Devlin,
H. Williams, N. Fitch, E. Hinds, B. Sauer, and M. Tarbutt,Phys. Rev. Lett.123, 033202 (2019).
- Burauet al.[2024]J. J. Burau, K. Mehling,
M. D. Frye, M. Chen, P. Aggarwal, J. M. Hutson, and J. Ye,Phys. Rev. A110, L041306 (2024).
- Johnson [1978]B. R. Johnson,J. Chem. Phys.69, 4678 (1978).
- Janssenet al.[2013]L. M. Janssen, A. van der
Avoird, and G. C. Groenenboom,Phys. Rev. Lett.110, 063201 (2013).
- Walraven and Karman [2025]E. F. Walraven and T. Karman,Phys. Rev. A112, 032810 (2025).
- Andersonet al.[1994]M. A. Anderson, M. D. Allen, and L. M. Ziurys,Astrophys. J.424, 503 (1994).
- Guanet al.[2021]Q. Guan, S. L. Cornish, and S. Kotochigova,Phys. Rev. A103, 043311 (2021).

## 


- 


Major funding support from
