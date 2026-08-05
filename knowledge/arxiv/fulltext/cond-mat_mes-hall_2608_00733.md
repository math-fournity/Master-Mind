# How NOT to build control-target gates in semiconductor quantum dots and beyond

**arXiv ID**: 2608.00733v1
**Authors**: Roman Korol, John Nichol, Ignacio Franco
**Published**: 2026-08-01
**Categories**: cond-mat.mes-hall, quant-ph
**HTML URL**: https://arxiv.org/html/2608.00733v1

## Abstract

Universal quantum computation requires single-qubit control together with at least one entangling two-qubit gate. CNOT and CROT gates are two famous examples of such gates, wherein the state of one qubit (control) dictates the transformation applied to the other (target). By using a simple derivation motivated by symmetry, we show that current device architectures of semiconductor-based quantum dot devices prevent efficient implementation of a CNOT and other asymmetric control-target gates via Heisenberg exchange, Coulomb repulsion, or other interaction that is invariant under spin exchange. Guided by this general principle, we propose a heterogeneous blueprint of double quantum dot devices that enables efficient implementation of the CNOT by breaking the spin exchange symmetry. Crucially, our numerical simulations predict that this novel device blueprint can enable a single-pulse fault-tolerant 100-ns CNOT gate in isotopically purified silicon.

## Full Text

How NOT to build control-target gates in semiconductor quantum dots and beyond

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.00733v1 [cond-mat.mes-hall] 01 Aug 2026

## How NOT to build control-target gates in semiconductor quantum dots and beyondRoman Korolroman.korol@sherbrooke.caDepartment of Chemistry, University of Rochester, Rochester, New York 14627, United StatesDépartement de Chimie, Université de Sherbrooke, Sherbrooke, Québec J1K 2R1, CanadaJohn Nicholjohn.nichol@rochester.eduDepartment of Physics and Astronomy, University of Rochester, Rochester, New York 14627, United StatesIgnacio Francoignacio.franco@rochester.eduDepartment of Chemistry, University of Rochester, Rochester, NY, USADepartment of Physics and Astronomy, University of Rochester, Rochester, NY, USAThe Institute of Optics, University of Rochester, Rochester, NY, USA

## Abstract

Universal quantum computation requires single-qubit control together with at least one entangling two-qubit gate. CNOT and CROT gates are two famous examples of such gates, wherein the state of one qubit (control) dictates the transformation applied to the other (target). By using a simple derivation motivated by symmetry, we show that current device architectures of semiconductor-based quantum dot devices prevent efficient implementation of a CNOT and other asymmetric control-target gates via Heisenberg exchange, Coulomb repulsion, or other interaction that is invariant under spin exchange. Guided by this general principle, we propose a heterogeneous blueprint of double quantum dot devices that enables efficient implementation of the CNOT by breaking the spin exchange symmetry. Crucially, our numerical simulations predict that this novel device blueprint can enable a single-pulse fault-tolerant100100ns CNOT gate in isotopically purified silicon.††preprint:APS/123-QED

## IIntroduction

Universal quantum computation hinges on the ability to execute a set of single- and two-qubit quantum gates with high fidelity across a scalable qubit architecture[1]. Single qubit gate fidelities exceeding the fault tolerance mark have been demonstrated across various leading quantum computing platforms: semiconductor spin qubits surpassing four nines (>99.99%>99.99\%)[2], superconducting circuits above six nines[3], and trapped ions approaching nine nines[4]. In contrast, for two-qubit gates the gate fidelity lags behind with recently reported fidelity of99.99%99.99\%for ion qubits – record-high across all platforms[5]– at the cost of relatively slow operation times (∼200\sim 200μ\mus). Semiconductor spins[6]and superconducting circuits[7,8,9]provide faster but less precise control with the highest two-qubit gate fidelity reported at the level of three nines. Why are the two-qubit gates more prone to error, and, more importantly, how can we mitigate that?

Many two-qubit gates require not one but a series of operations, sometimes including more than one two-qubit interaction[10,11,12,13]. This requirement increases the total gate time and accumulates errors, contributing to the lower gate fidelity for two-qubit gates compared to the gates achieved in a single shot[14]. Thus, designing simpler two-qubit operation sequences is of great interest. Specifically, we show that additional operations are unavoidable in devices that use a single qubit blueprint if the interaction between qubits is symmetric, while the target gate is not. Both Coulomb repulsion and Heisenberg exchange between identical particles are symmetric with respect to particle exchange. The Heisenberg exchange interaction is used to couple semiconductor quantum dot qubits[15]and Coulomb repulsion is at the core of capacitive coupling in quantum dots[16], superconducting circuits[17], and ion qubits[18]. Because scalability of the device is typically achieved by repeating a single-qubit building block, a homogeneous array of identically constructed qubits is generated, and the symmetry of both Coulomb and Heisenberg interactions is preserved.
This, as we show here, makes it impossible todirectlyimplement any asymmetric gate, such as controlled-not (CNOT) or controlled-rotation (CROT). To enable the implementation of these asymmetric gates, the exchange symmetry is broken by other means, for instance, via spin-orbit interaction in hole-spin qubits[19]or by selectively driving one of the two QD qubits[12]. As a last resort, exchange symmetry is broken by sandwiching the symmetric interaction with additional qubit operations[10,11], leading to longer gate times and larger errors.

Here we articulate the mismatch in symmetry between a symmetric two-qubit interaction and an asymmetric target gate as a core reason why additional interactions are needed. Based on this analysis, we suggest a novel and general approach to overcome it via a heterogeneous device architecture. Specifically, we show that when devices are constructed in a homogeneous fashion by repeating one qubit blueprint throughout, the symmetry of the underlying interqubit interaction is necessarily preserved. In contrast, by defining neighboring qubits in non-identical ways, the effective interqubit interaction in the computational subspace can be asymmetric, facilitating the implementation of asymmetric gates. Although this principle is general, for concreteness, we illustrate it in semiconductor quantum dots. This platform is chosen because of the wide variety of distinct qubit mappings that have been realized on virtually identical hardware. Specifically, we show that by adopting a hybrid qubit encoding that alternates betweenS​T0ST_{0}andS​T−ST_{-}qubits, a CNOT gate can be realized directly using only the symmetric Heisenberg exchange. Numerical simulations assessing the effects of the main sources of decoherence in these devices – static noise and leakage out of computational subspace – yield gate fidelities of over 99% for experimentally accessible parameter regimes, advancing the platform into the fault-tolerant regime based on the commonly quoted∼1%\sim 1\%surface-code threshold[20].

The paper is outlined as follows. We begin with Sec.II, presenting the general proof of the symmetry preservation in homogeneously mapped devices as well as its implications. Sec.IIIprovides general background of the semiconductor quantum dot setup, and can be skipped by specialists.
The CNOT gate is constructed in Secs.V.1-V.2and its performance is tested in Secs.V.3-V.5. Before concluding, we discuss the implications of our finding for quantum dots and beyond in Sec.VI.

## IISymmetry Constraints in Qubit Design

Is it possible to realize an asymmetric two-qubit gate with a single symmetric interaction? In this section, we show that this task is impossible for a device that is built out of homogeneous blocks. However, it can be achieved by utilizing a heterogeneous qubit encoding.

## II.1Homogeneous Architecture Preserves Interaction Symmetry

Firstly, we demonstrate that a two-qubit interaction that is symmetric with respect to qubit exchange cannot by itself implement an asymmetric gate (such as CNOT) if the two qubits are encoded identically.

For this, let the total Hilbert spaceℋ\mathcal{H}be the tensor product of two identical subsystems, A and B, each containing a qubit:ℋ=ℋA⊗ℋB.\mathcal{H}=\mathcal{H}_{\text{A}}\otimes\mathcal{H}_{\text{B}}.

We define the exchange operatorSABS_{\text{AB}}that swaps the quantum states of the two subsystems. Since a basis ofℋ\mathcal{H}can be constructed from all product states, the linear operatorSABS_{\text{AB}}can be defined by its action on a general product state:SAB​(|ψA⟩⊗|ϕB⟩)=(−1)η​|ϕA⟩⊗|ψB⟩S_{\text{AB}}(\ket{\psi_{\text{A}}}\otimes\ket{\phi_{\text{B}}})=(-1)^{\eta}\ket{\phi_{\text{A}}}\otimes\ket{\psi_{\text{B}}}(1)

whereη\etais the number of fermions in each subsystem, which accounts for the exchange statistics of identical particles.

The nature of the interaction between subsystems A and B is such that the interaction HamiltonianHintH_{\text{int}}between two subsystems is symmetric with respect to this exchange, meaning it commutes with the exchange operator:[Hint,SAB]=0.[H_{\text{int}},S_{\text{AB}}]=0.

The qubits are defined on both subsystems A and B in the same way, meaning that the projection operator that defines the qubit subspace is identical, i.e.,PA=PB=PP_{\text{A}}=P_{\text{B}}=Pand the total projector is𝒫=P⊗P,\mathcal{P}=P\otimes P,

where the first (second) operator acts on the Hilbert space of A (B).
The effective Hamiltonian within the projected computational subspace is then given byHint′=𝒫​Hint​𝒫.H^{\prime}_{\text{int}}=\mathcal{P}H_{\text{int}}\mathcal{P}.(2)

We now show that effective Hamiltonian (2) acting on the computational subspace must retain the exchange symmetry of the full Hamiltonian, provided the two qubits are formed by an analogous projection of identical subsystems.

The key step is to recognize that the projection operator𝒫\mathcal{P}is symmetric with respect to the subsystem exchange operator. This is a direct consequence of using the same projectorPPfor both subsystemsAAandBB.
A similarity transformation withSABS_{\text{AB}}swaps the operators in the tensor product. Because both operators are the same, the projector is invariant:SAB​𝒫​SAB−1=SAB​(P⊗P)​SAB−1=P⊗P=𝒫,S_{\text{AB}}\mathcal{P}S_{\text{AB}}^{-1}=S_{\text{AB}}(P\otimes P)S_{\text{AB}}^{-1}=P\otimes P=\mathcal{P},

which means that the swap and the projection operators commute:[𝒫,SAB]=0.[\mathcal{P},S_{\text{AB}}]=0.(3)

The projected HamiltonianHint′H^{\prime}_{\text{int}}also commutes with the swap operator:[Hint′,SAB]=(𝒫​Hint​𝒫)​SAB−SAB​(𝒫​Hint​𝒫)=0,[H^{\prime}_{\text{int}},S_{\text{AB}}]=(\mathcal{P}H_{\text{int}}\mathcal{P})S_{\text{AB}}-S_{\text{AB}}(\mathcal{P}H_{\text{int}}\mathcal{P})=0,(4)

sinceSABS_{\text{AB}}commutes with both𝒫\mathcal{P}andHintH_{\text{int}}.
Equation4signifies thatHint′H^{\prime}_{\text{int}}(the effective interaction within the computational subspace) must remain symmetric.Thus, a symmetric interaction between identical subsystems cannot by itself implement any asymmetric operation in the (projected) qubit subspace.

## II.2Breaking of Symmetry via Heterogeneity

This symmetry need not be preserved if the two qubits are not constructed by identical projectors, as is the case in the heterogeneous architecture proposed in this paper. If projectors are non-identical, i.e.,PA≠PBP_{\text{A}}\neq P_{\text{B}}, the total projection operator𝒫=PA⊗PB\mathcal{P}=P_{\text{A}}\otimes P_{\text{B}}is no longer guaranteed to be symmetric:SAB​𝒫​SAB−1=SAB​(PA⊗PB)​SAB−1=PB⊗PA≠𝒫S_{\text{AB}}\mathcal{P}S_{\text{AB}}^{-1}=S_{\text{AB}}(P_{\text{A}}\otimes P_{\text{B}})S_{\text{AB}}^{-1}=P_{\text{B}}\otimes P_{\text{A}}\neq\mathcal{P}

Thus, the commutator[𝒫,SAB][\mathcal{P},S_{\text{AB}}]does not necessarily vanish and the central step in the above proof fails. The effective HamiltonianHint′=𝒫​Hint​𝒫H^{\prime}_{\text{int}}=\mathcal{P}H_{\text{int}}\mathcal{P}canbecome asymmetric and facilitate asymmetric operations. In fact, we show in Sec.Vthat this insight can be used to implement a single-pulse fault-tolerant CNOT gate using only the natural symmetric Heisenberg exchange interaction between qubits.

To understand this in the context of QDs, below we connect the physical Fermi-Hubbard Hamiltonian provided by this quantum hardware and the effective spin Hamiltonian used in quantum information considerations.

## IIIBackground: The Case for Quantum Dots

Electron spins in semiconductor quantum dots constitute one of the leading quantum computing platforms. They offer a strong potential for scalability and long coherence times[21,22,23]and benefit from their compatibility with advanced semiconductor manufacturing techniques[24].

This platform enables many different qubit encodings. Here we focus on the variants of singlet-triplet double quantum dot (DQD) qubits[25,26], where the qubit is encoded using two neighboring quantum dots.
Of course, the spin of a single electron localized on one quantum dot is intrinsically a two-level system and can naturally define a (Loss-DiVincenzo) qubit[27]. However, controlling such a qubit can be experimentally demanding, requiring precise control of magnetic fields on the nanoscale to address individual spins[27]. In contrast, the mapping of a qubit onto electrons localized in two different dots allows for manipulation using electrical control, simplifying the experimental setup, and broadening the accessible operations – at the cost of halving the number of qubits obtained from a quantum dot array[15]. Other possible encodings include exchange-only qubits that use three or four[28,29]dots per qubit.

## III.1From Fermi-Hubbard Model to Spin Dynamics

Electron spins tightly confined in gate-defined quantum dots can be modeled with the Fermi-Hubbard model, with each dot corresponding to a site that can host up to two fermions with opposite spin (due to Pauli exclusion). The Hamiltonian written in second quantization is[15]H^FH=∑i=1N[ϵi​n^i+Ui​n^i​(n^i−1)]+∑σ=↑,↓⟨i,j⟩[ti​j​c^i​σ†​c^j​σ+H.c.].\hat{H}_{\text{FH}}=\sum_{i=1}^{N}\left[\epsilon_{i}\hat{n}_{i}+U_{i}\hat{n}_{i}(\hat{n}_{i}-1)\right]+\sum_{\begin{subarray}{c}\sigma=\uparrow,\downarrow\\
\braket{i,\,j}\end{subarray}}[t_{ij}\hat{c}_{i\sigma}^{\dagger}\hat{c}_{j\sigma}+\text{H.c.}].(5)

Here, indexiiruns over the dots,ϵi\epsilon_{i}is the voltage-controlled chemical potential,c^i​σ†\hat{c}_{i\sigma}^{\dagger}(c^i​σ\hat{c}_{i\sigma}) is the creation (annihilation) operator for the fermion [electron or hole] with spinσ=↑or↓\sigma=\uparrow\text{ or }\downarrowdefined along the spin quantization (zz) axis. The quantityn^i=∑σ=↑,↓c^i​σ†​c^i​σ\hat{n}_{i}=\sum_{\sigma=\uparrow,\downarrow}\hat{c}_{i\sigma}^{\dagger}\hat{c}_{i\sigma}is the fermionic number operator,ti​jt_{ij}is the spin-conserving tunnel coupling between nearest neighbor dots,UUis the intradot (onsite) Coulomb repulsion, andH.c.stands for Hermitian conjugate. This treatment includes the more general case of odd number of electrons per dot[30]via renormalization of Hamiltonian parameters.
Here, we have omitted spin-flipping tunnel couplings, which is valid when spin-orbit coupling is weak (e.g., for electrons in Si-based quantum dots). Holes in Si or electrons in heavier materials such asGe{}\mathrm{Ge}andGaAs{}\mathrm{GaAs}can have significant spin-flip tunnel couplings, which need to be added to the second summation. Third, we have neglected any magnetic field contributions to the Hamiltonian at this stage. These will be added later.

Experiments typically operate at the half-filled regime where the number of electronsNNand dots coincide.
A single DQD qubit (N=2N=2) yields 6 electronic states:{|↑,↑⟩,|↑,↓⟩,|↓,↑⟩,|↓,↓⟩,|↑↓,0⟩,|0,↑↓⟩}\{\ket{\uparrow,\uparrow},\ket{\uparrow,\downarrow},\ket{\downarrow,\uparrow},\ket{\downarrow,\downarrow},\ket{\uparrow\downarrow,0},\ket{0,\uparrow\downarrow}\}and 70 states forN=4N=4, growing combinatorially fast with(2​NN)\binom{2N}{N}states forNNdots.

The Fermi-Hubbard Hamiltonian (5) can be mapped to the spin Hamiltonian used for quantum information[15]H​(t)=14​∑⟨i,j⟩Ji​j​(t)​𝝈i⋅𝝈j+12​∑igi​μB​𝐁i⋅𝝈i.H(t)=\frac{1}{4}\sum_{\langle i,j\rangle}J_{ij}(t)\boldsymbol{\sigma}_{i}\cdot\boldsymbol{\sigma}_{j}+\frac{1}{2}\sum_{i}g_{i}\mu_{B}\mathbf{B}_{i}\cdot\boldsymbol{\sigma}_{i}.(6)

The Heisenberg exchange (first term) defines interactions between spinsiiandjjand the Zeeman splitting (second term) outlines how individual spins are affected by magnetic fields. Here,gig_{i}is the g-factor of the electronii, andμB\mu_{B}is the Bohr magneton.
The derivation of Eq. (6) from the Fermi-Hubbard model informs us about the physical nature of the effective exchange interaction between spins[31]:Ji​j=2​ti​j2Ui−ϵi+ϵj+2​ti​j2Uj−ϵj+ϵi.J_{ij}=\frac{2t_{ij}^{2}}{U_{i}-\epsilon_{i}+\epsilon_{j}}+\frac{2t_{ij}^{2}}{U_{j}-\epsilon_{j}+\epsilon_{i}}.(7)

This simplifies toJi​j=4​ti​j2/UJ_{ij}=4t_{ij}^{2}/Uwhen the biases and onsite Coulomb repulsions for the two dots are equal. Note thatJi​j>0J_{ij}>0, because exchange lowers the energy of the singlet relative to the triplet. Local magnetic fields𝐁i\mathbf{B}_{i}or intrinsic variability ingig_{i}enable individual addressing of qubits with magnetic fields. The latter is provided by the differences in Landé𝒢\mathcal{G}-tensors due to spin-orbit coupling and material inhomogeneity.

To arrive at Eq. (6) from (5), one first assumes small bias conditionsϵi≪U\epsilon_{i}\ll U. That is, keeping the chemical potential differences between dots much smaller than the onsite repulsion, such that each dot’s occupation is unity up to small perturbative corrections. This clearly delineates the single occupation subspace of size2N2^{N}containing all and only states with 1 fermion per site.
The effective single occupation Hamiltonian [Eq.6] is obtained by block diagonalization via Schrieffer-Wolff perturbation theory[31]or, equivalently, by diagonalizing the sector formed by all singlets with a subsequent projection[19]. The resulting Hamiltonian describes the dynamics of spins decoupled from any dynamics of charges and has the form of a homogeneous Heisenberg interaction between spins.

## III.2Qubit Encodings

The single occupation subspace of the double quantum dot (DQD),N=2N=2, hosts2N=42^{N}=4spin states, a singletSSand a tripletT−T_{-},T0T_{0}andT+T_{+}.
In the presence of a strong magnetic field in thezz-direction, the degeneracy of the triplet can be removed via Zeeman splitting. The singletSSand the unpolarized tripletT0T_{0}are in turn split by tunnel coupling between the two dots in the DQD.

Traditionally, the singlet and the unpolarized triplet states are chosen as the qubit states,|0⟩\ket{0}and|1⟩\ket{1}, defining a computational subspace in the Hilbert space and forming theS​T0ST_{0}qubit.

Alternative singlet-triplet resonant (↑↓\uparrow\downarrow) qubits can be defined by spin of the individual electrons, i.e.,{|↑↓⟩​and​|↓↑⟩}\{\ket{\uparrow\downarrow}\text{ and }\ket{\downarrow\uparrow}\}, rather than the total spin states. Either encoding makes the qubit states resistant to global magnetic field fluctuations, since the spacing between the singlet and unpolarized triplet do not depend on the global magnetic field strength. This is the well-known decoherence-free subspace (DFS)[32,33]. More recently, the use of the lower-energy triplet state (T−T_{-}orT+T_{+}depending on the sign ofgg) was proposed to construct[26]and experimentally realize[34,35]a useful qubit, which we refer to asS​T−ST_{-}below. In all cases, the remaining levels define a leakage subspace in Hilbert space that needs to be isolated from the qubit.

## III.3Two-qubit Gates

While DQD devices feature electrically controlled single-qubit operations with gate fidelities of 99.6% in isotopically purified silicon (Si)[36], achieving high fidelity two-qubit gates remains a significant challenge.
This type of gate is realized between qubits hosted in two neighboring DQDs that are interacting via either capacitive (Coulomb) or Heisenberg exchange coupling. The Heisenberg exchange coupling Eq.(7) is controlled by manipulating the tunnel couplingti​jt_{ij}between consecutive quantum dots. The capacitive coupling is activated by controlling the charge distribution of the singlet state by manipulating theϵi\epsilon_{i}through bias voltages. Motivated by a plethora of theoretical proposals[37,38,25,39], the first exchange-based 2-qubit entangling operation was recently reported[35]. The implementation featured a variant of theSWAP\sqrt{\text{SWAP}}, achieving Bell state fidelities of 73-90%. By contrast, no experimental demonstration of the CNOT gate has been reported so far in these devices, even though there is widespread interest in the quantum information community.

We argue that the disparity in progress in state-of-the-art experimental implementations ofSWAP\sqrt{\text{SWAP}}vs. CNOT entangling gates arise because of the symmetry of the physical setup and the underlying interqubit interaction.
Both the capacitive coupling and Heisenberg exchange arise due to electron-electron interactions, which are invariant with respect to particle permutations. As discussed in Sec.II, when interacting qubits are constructed using the same blueprint, this interaction symmetry leads to an invariance in the effective interaction Hamiltonian with respect to qubit exchange. In turn, this symmetry aids the implementation of two-qubit gates that act on both qubits symmetrically,
such as the variants of SWAP[35], as well as XX, ZZ, and CPHASE gates[37,38,25,39]– all requiring a simple series of pulses.
By contrast, asymmetric gates, such as CNOT or CROT, are more difficult to achieve with capacitive coupling or with Heisenberg exchange. They
require multiple two-qubit interactions intertwined with single-qubit gates to inject the asymmetry between the control and target qubits[33], see, e.g., Refs.10,11,12,13.
As we demonstrate below, high fidelity entangling CNOT gates can be generated by adopting an asymmetric device blueprint.

## IVSymmetry Constraints in Double Quantum Dot Qubits

We now proceed to apply the principles developed in Secs.II-IIIto design more efficient asymmetric quantum gates in the platform of our choice: gate-defined double quantum dot qubits. In Sec.IV.1we establish the notation and specify the three qubit encodings using DQDs. Then, in Secs.IV.2andIV.3we present all six possible two-qubit interactions based on pairing these encodings.

## IV.1Single Qubit Hamiltonians

In the{S,T0}\{S,T_{0}\}basis, theS​T0ST_{0}qubit is described via Hamiltonian[15]:HS​T0=[−J12Δ​ζ12(z)Δ​ζ12(z)0],H_{ST_{0}}=\begin{bmatrix}-J_{12}&\Delta\zeta_{12}^{(z)}\\
\Delta\zeta_{12}^{(z)}&0\end{bmatrix},(8)

where we set the energy ofT0T_{0}as 0 throughout. Here we have adopted the view that the main component of the magnetic field is along thezz-direction and defines the quantization axis. Throughout we use numbers1,2,3,41,2,3,4etc. to label the dots.
Theσz\sigma_{z}control of this qubit is achieved by varying the exchange couplingJ12J_{12}through the chemical potential of the dotsϵi\epsilon_{i}. TheΔ​ζ12(z)\Delta\zeta_{12}^{(z)}generatingσx\sigma_{x}control is opened by magnetic field gradients created through local micromagnets and/or by inhomogeneities in the spin-orbit coupling encountered in the material in the presence of a homogeneous magnetic field. To be general, we describe these magnetic field terms via𝜻i=μB2​𝒢i​𝐁i\boldsymbol{\zeta}_{i}=\frac{\mu_{B}}{2}\mathcal{G}_{i}\mathbf{B}_{i}. This is a cartesian vector containing the Zeeman energy components for siteiialongxx,yyandzzdirections, and Landé g-tensor𝒢i\mathcal{G}_{i}generalizing thegig_{i}of Eq. (6) to magnetically inhomogeneous materials. The differenceΔ​𝜻i​j=μB2​(𝒢j​𝐁j−𝒢i​𝐁i)\Delta\boldsymbol{\zeta}_{ij}=\frac{\mu_{B}}{2}\left(\mathcal{G}_{j}\mathbf{B}_{j}-\mathcal{G}_{i}\mathbf{B}_{i}\right)is between the dotsiiandjj.

For the resonant qubit, the Hamiltonian written in the{|↑,↓⟩,|↓,↑⟩}\{\ket{\uparrow,\downarrow},\ket{\downarrow,\uparrow}\}basis isHres=[Δ​ζ12(z)−J12/2J12/2J12/2−Δ​ζ12(z)−J12/2].H_{\text{res}}=\begin{bmatrix}\Delta\zeta_{12}^{(z)}-J_{12}/2&J_{12}/2\\
J_{12}/2&-\Delta\zeta_{12}^{(z)}-J_{12}/2\end{bmatrix}.(9)

Here, the control parameters are the same as in theS​T0ST_{0}qubit but with their roles switched.

For theS​T−ST_{-}qubit, we analogously getHS​T−=[−J12(Δ​ζ12(x)+i​Δ​ζ12(y))/2(Δ​ζ12(x)−i​Δ​ζ12(y))/2−ζ12(z)]H_{ST_{-}}=\begin{bmatrix}-J_{12}&\left(\Delta\zeta_{12}^{(x)}+i\Delta\zeta_{12}^{(y)}\right)/\sqrt{2}\\
\left(\Delta\zeta_{12}^{(x)}-i\Delta\zeta_{12}^{(y)}\right)/\sqrt{2}&-\zeta_{12}^{(z)}\end{bmatrix}(10)

in the{S,T−}\{S,T_{-}\}basis. The term𝜻i​j=μB2​(𝒢i​𝐁i+𝒢j​𝐁j)\boldsymbol{\zeta}_{ij}=\frac{\mu_{B}}{2}\left(\mathcal{G}_{i}\mathbf{B}_{i}+\mathcal{G}_{j}\mathbf{B}_{j}\right)refers to the sum over the two dotsiiandjj. In this case, the magnetic field alongzzalso providesσz\sigma_{z}control as it shifts theT−T_{-}state, whileσx\sigma_{x}control is achieved via the magnetic field components perpendicular tozz.

As summarized in Table1, single qubit control in DQD qubits can be achieved by balancing the relative strength of the effective exchangeJ12J_{12}and the particular cartesian component of the generalized magnetic field gradientΔ​𝜻\Delta\boldsymbol{\zeta}between dots. Undesirable leakage outside of the computational space is caused by stray transverse magnetic field components (ζ1(x,y),ζ2(x,y)\zeta_{1}^{(x,y)},\,\zeta_{2}^{(x,y)}) in all three cases. In addition, leakage of the resonant (↑↓\uparrow\downarrow) andS​T−ST_{-}qubits can be caused by the longitudinal field gradientΔ​ζ12(z)\Delta\zeta_{12}^{(z)}.Qubit Typeσz\sigma_{z}controlσx\sigma_{x}controlleakageS​T0ST_{0}J12J_{12}Δ​ζ12(z)\Delta\zeta_{12}^{(z)}ζ1(x,y),ζ2(x,y)\zeta_{1}^{(x,y)},\,\zeta_{2}^{(x,y)}↑↓\uparrow\downarrowΔ​ζ12(z)\Delta\zeta_{12}^{(z)}J12J_{12}ζ1(x,y),ζ2(x,y),Δ​ζ12(z)\zeta_{1}^{(x,y)},\,\zeta_{2}^{(x,y)},\,\Delta\zeta_{12}^{(z)}S​T−ST_{-}J12,ζ12(z)J_{12},\,\zeta_{12}^{(z)}Δ​ζ12(x,y)\Delta\zeta_{12}^{(x,y)}ζ1(x,y),ζ2(x,y),Δ​ζ12(z)\zeta_{1}^{(x,y)},\,\zeta_{2}^{(x,y)},\,\Delta\zeta_{12}^{(z)}Table 1:Single-qubit control handles for different qubit encodings.ExchangeJ12J_{12}and the gradient of the Zeeman energy splitting vector𝜻12\boldsymbol{\zeta}_{12}determine the matrix elements of the effective Hamiltonian.

## IV.2Interaction Hamiltonians between Identical Qubits

To scale the quantum hardware from a single qubit to many qubits, the standard procedure is to employ identically constructed qubits. In our context, each qubit will be constructed using a DQD in any of the three encodings discussed above. Table2summarizes the three types of qubit coupling for each encoding in this homogeneous approach.

Coupling twoS​T0ST_{0}qubits via exchange leads to a transverse-field Ising (−14​J23​σ12x⊗σ34x-\frac{1}{4}J_{23}\sigma_{12}^{x}\otimes\sigma_{34}^{x}) interaction between them, which can be modulated by adjusting the exchange between neighboring dots that belong to different qubits[10].
Note that we continue to use numbers to refer to dots. Thus, the first qubit is formed by dots labeled byi=1,2i=1,2and the second qubit is formed by dots labeled byi=3,4i=3,4. For the resonant qubits, the interqubit interaction is longitudinal-field Ising (−14​J23​σ12z⊗σ34z-\frac{1}{4}J_{23}\sigma_{12}^{z}\otimes\sigma_{34}^{z})[10,38], which is easy to see by changing the computational basis on both qubits. Finally, twoS​T−ST_{-}qubits are coupled via−18​J23​[σ12x⊗σ34x+σ12y⊗σ34y+12​(1−σ12z)⊗(1−σ34z)]-\frac{1}{8}J_{23}\left[\sigma^{x}_{12}\otimes\sigma^{x}_{34}+\sigma^{y}_{12}\otimes\sigma^{y}_{34}+\frac{1}{2}(1-\sigma^{z}_{12})\otimes(1-\sigma^{z}_{34})\right][35].

When scaling, an important consideration is that of the influence of leakage states. InS​T0ST_{0}and resonant encodings, the leakage states become degenerate with the computational space. Such degeneracies can be broken by introducing local magnetic fields, which is experimentally challenging. By contrast, theS​T−ST_{-}encoding isolates the computational space energetically, making this encoding preferable for multi-qubit devices, e.g. Refs.35,19.CoupledQubitsCouplingDegeneracies withleakage statesS​T0+S​T0ST_{0}+ST_{0}−14​J23​σ12x⊗σ34x-\frac{1}{4}J_{23}\sigma^{x}_{12}\otimes\sigma^{x}_{34}|T0,T0⟩⇌\ket{T_{0},T_{0}}\rightleftharpoons|T−,T+⟩,|T+,T−⟩\ket{T_{-},T_{+}},\ket{T_{+},T_{-}}↑⁣↓⁣+⁣↑⁣↓\uparrow\downarrow+\uparrow\downarrow−14​J23​σ12z⊗σ34z-\frac{1}{4}J_{23}\sigma^{z}_{12}\otimes\sigma^{z}_{34}|↑↓,↑↓⟩​, etc.⇌\ket{\uparrow\downarrow,\uparrow\downarrow}\text{, etc.}\rightleftharpoons|↑↑,↓↓⟩,|↓↓,↑↑⟩\ket{\uparrow\uparrow,\downarrow\downarrow},\ket{\downarrow\downarrow,\uparrow\uparrow}S​T−+S​T−ST_{-}+ST_{-}−18J23[σ12x⊗σ34x+σ12y⊗σ34y+12(1−σ12z)⊗(1−σ34z)]\begin{aligned} -\frac{1}{8}J_{23}\big[&\sigma^{x}_{12}\otimes\sigma^{x}_{34}+\sigma^{y}_{12}\otimes\sigma^{y}_{34}\\
&+\frac{1}{2}(1-\sigma^{z}_{12})\otimes(1-\sigma^{z}_{34})\big]\end{aligned}NoneTable 2:Coupling qubits with the same encoding leads tosymmetricinteractions.Qubit A (B) is formed by dots 1 and 2 (3 and 4). InS​T0ST_{0}and resonant qubits an interqubit magnetic field gradientΔ​ζ23(z)\Delta\zeta^{(z)}_{23}is needed to prevent leakage due to degeneracies between computational (e.g.|T0,T0⟩\ket{T_{0},T_{0}}) and leakage states (e.g.|T−,T+⟩\ket{T_{-},T_{+}}.)

Overall, we emphasize that the interaction between identically constructed qubits is symmetric with respect to qubit exchange.
In contrast, the CNOT gate–the basic building block of many quantum algorithms–is manifestly non-symmetric. As a result, additional interactions are needed to break the exchange symmetry resulting in more complex schemes to construct asymmetric gates[10,11].

## IV.3Our Proposal: The Case for Non-identical Qubit Encodings

Previous work has attempted to utilize the individual strengths of distinct qubit platforms in heterogeneous qubit encodings, while also recognizing the challenges[40]. For instance, Ref.41demonstrates the coupling interface that is useful for a CPHASE gate by pairing a Loss-DiVincenzo and a singlet-triplet qubit in which the faster qubit initialization and readout for singlet-triplet qubits is exploited. Here we go beyond these initial arguments, by investigating the emerging properties of heterogeneous qubit arrays that arise from broken symmetries. That is, by investigating how non-identical qubit encodings are different from the sum of their parts.

Table3summarizes three pairings of distinctly encoded qubits. These were obtained via Schrieffer-Wolff perturbation theory[31]for the system of four dots analogously to the results from the literature presented in Sec.IV.2.
As opposed to those in Table2, all of them result in a distinct asymmetric interqubit interaction.
The most straightforward way to break the qubit-exchange symmetry
is to rotate the basis of one of the qubits relative to the uniform resonant orS​T0ST_{0}mapping. This 1-qubit basis change results in anS​T0+↑↓ST_{0}+\uparrow\downarrowpair withX​ZXZinteraction that can facilitate the implementation of the asymmetric CNOT gate. However, this mapping may present experimental challenges, asS​T0ST_{0}vs. resonant qubits require different control pulses. TheS​T0ST_{0}is manipulated using baseband voltage pulses applied to the gates, while the resonant qubit by excitation using external microwave sources.

By contrast, by pairing theS​T0ST_{0}andS​T−ST_{-}qubits an asymmetricX​ZXZinteraction between qubits is achieved
without introducing the necessity for the microwave radiation, simplifying the experimental set-up as both singlet-triplet qubits are controlled by electrostatic gates. In fact, as we detail below, theS​T−ST_{-}andS​T0ST_{0}pairing of qubits leads to an experimentally realistic platform for the realization of a fast single-pulse fault-tolerant CNOT gate.

Lastly, the pairing ofS​T−ST_{-}with the resonant qubit yields an interaction that affects the phases of the two qubits differently, suggesting that it could potentially be useful for controlled rotation (CROT) gates[19]. Moreover, in this case the computational basis states are no longer degenerate with any of the leakage states, which could potentially alleviate leakage relative to the resonant qubit devices. Nevertheless, this type of mixed encoding has the same experimental challenges as theS​T0+↑↓ST_{0}+\uparrow\downarrow, and does not merit further consideration at this stage.CoupledcouplingdegeneraciesQubitswith leakage statesS​T−+S​T0ST_{-}+ST_{0}−18​J23​(1−σ12z)⊗σ34x-\frac{1}{8}J_{23}(1-\sigma^{z}_{12})\otimes\sigma^{x}_{34}|T−,T0⟩⇌|T0,T−⟩,etc.\ket{T_{-},T_{0}}\rightleftharpoons\ket{T_{0},T_{-}},\text{etc.}S​T0+↑↓ST_{0}+\uparrow\downarrow−14​J23​σ12x⊗σ34z-\frac{1}{4}J_{23}\sigma^{x}_{12}\otimes\sigma^{z}_{34}|T0,↑↓⟩⇌|T−,↑↑⟩,|T+,↓↓⟩\ket{T_{0},\uparrow\downarrow}\rightleftharpoons\ket{T_{-},\uparrow\uparrow},\ket{T_{+},\downarrow\downarrow}S​T−+↑↓ST_{-}+\uparrow\downarrow−18​J23​(1−σ12z)⊗σ34z-\frac{1}{8}J_{23}(1-\sigma^{z}_{12})\otimes\sigma^{z}_{34}NoneTable 3:Coupling qubits with different encodings leads toasymmetricinteractions.Pairing of eitherS​T−ST_{-}or a resonant qubit with anS​T0ST_{0}qubit leads to anX​ZXZinteraction, that facilitates the realization of CNOT. While degeneracies are introduced as in Table2, leakage suppression strategy is unchanged. Pairing anS​T−ST_{-}and a resonant qubit gives an asymmetric phase shift.

## VSingle-pulse CNOT Gate via theS​T−+S​T0ST_{-}+ST_{0}Pairing

As established in Sec.IV.3(Table3), pairing anS​T−ST_{-}with anS​T0ST_{0}qubit yields an asymmetricX​ZXZ-type interqubit coupling,−18​J23​(1−σ12z)⊗σ34x-\frac{1}{8}J_{23}(1-\sigma^{z}_{12})\otimes\sigma^{x}_{34}, while retaining the experimental simplicity of electrostatic control. We now exploit this asymmetry to construct a direct, single-pulse CNOT gate and benchmark its performance under realistic experimental conditions.

In Sec.V.1we derive the effective two-qubit Hamiltonian and in Sec.V.2we derive the timing conditions needed to realize the CNOT gate and demonstrate its ideal action on Bell states. Finally, we test the gate against two dominant sources of infidelity in gate-defined quantum dots: leakage out of the computational subspace (Sec.V.3) and quasi-static electric and magnetic noise (Sec.V.5).

## V.1Effective Hamiltonian and Gate Construction

The upper-triangular portion of the two-qubit Hamiltonian for anS​T−+S​T0ST_{-}+ST_{0}device, written in the basis{|S,S⟩,|S,T0⟩,|T−,S⟩,|T−,T0⟩}\{\ket{S,S},\ket{S,T_{0}},\ket{T_{-},S},\ket{T_{-},T_{0}}\}, readsHS​T−+S​T0=H12S​T−+H34S​T0−18​J23​(1−σ12z)⊗σ34x=[ζ12(z)−J12−J34Δ​ζ34(z)(Δ​ζ12(x)+i​Δ​ζ12(y))/20∗ζ12(z)−J120(Δ​ζ12(x)+i​Δ​ζ12(y))/2∗∗−J34Δ​ζ34(z)−J23/4∗∗∗0].H^{ST_{-}+ST_{0}}=H_{12}^{ST_{-}}+H_{34}^{ST_{0}}-\frac{1}{8}J_{23}(1-\sigma^{z}_{12})\otimes\sigma^{x}_{34}=\begin{bmatrix}\zeta^{(z)}_{12}-J_{12}-J_{34}&\Delta\zeta^{(z)}_{34}&\left(\Delta\zeta^{(x)}_{12}+i\Delta\zeta^{(y)}_{12}\right)/\sqrt{2}&0\\
*&\zeta^{(z)}_{12}-J_{12}&0&\left(\Delta\zeta^{(x)}_{12}+i\Delta\zeta^{(y)}_{12}\right)/\sqrt{2}\\
*&*&-J_{34}&\Delta\zeta^{(z)}_{34}-J_{23}/4\\
*&*&*&0\end{bmatrix}.(11)

To derive Eq. (11) we have followed the Schrieffer-Wolff transformation[31]for defining low-energy subspace Hamiltonian, which naturally leads to the Hamiltonians of the individual qubits defined in (8) and (10) and their interaction.
In this qubit-pair, individual qubit control is provided by the intraqubit exchangesJ12J_{12}andJ34J_{34}, magnetic field in thezz-direction and the effective magnetic-field gradientsΔ​𝜻i​j\Delta\boldsymbol{\zeta}_{ij}.
The distinguishing feature of Eq. (11) relative to the cases of symmetrically interacting qubits (Table2) is that the interqubit exchangeJ23J_{23}appears only once in the upper-triangular block, as an off-diagonal element coupling|T−,S⟩\ket{T_{-},S}and|T−,T0⟩\ket{T_{-},T_{0}}but not|S,S⟩\ket{S,S}and|S,T0⟩\ket{S,T_{0}}. This singular appearance is a direct consequence of the asymmetricX​ZXZcoupling and — as we show next — is what enables a direct single-pulse implementation of CNOT.

For the duration of the gate, the intraqubit magnetic-field gradients are turned off,Δ​𝜻=𝟎\Delta\boldsymbol{\zeta}=\mathbf{0}.
For convenience we will now set the zero of energy to the state|T−,T0⟩\ket{T_{-},T_{0}}, reducing the Hamiltonian (11) toH2q=[TA+TB0000TA0000TBTAB00TAB0],H_{\text{2q}}=\begin{bmatrix}T_{\text{A}}+T_{\text{B}}&0&0&0\\
0&T_{\text{A}}&0&0\\
0&0&T_{\text{B}}&T_{\text{AB}}\\
0&0&T_{\text{AB}}&0\end{bmatrix},(12)

whereTA=ζ12(z)−J12T_{\text{A}}=\zeta_{12}^{(z)}-J_{12}is the level splitting of theS​T−ST_{-}qubit (qubit A),TB=−J34T_{\text{B}}=-J_{34}is the level splitting of theS​T0ST_{0}qubit (qubit B), andTAB=−J23/4T_{\text{AB}}=-J_{23}/4is the interqubit coupling.

It is now convenient to transition from physical to logical qubit labels. The singlet (triplet) state is assigned the label|0⟩\ket{0}(|1⟩\ket{1}) such that, for example,|T−,T0⟩=|1A,1B⟩\ket{T_{-},T_{0}}=\ket{1_{\text{A}},1_{\text{B}}}. The basis ordering in Eq. (11) is identical to the one in (12) but is now labeled as|0A,0B⟩\ket{0_{\text{A}},0_{\text{B}}},|0A,1B⟩\ket{0_{\text{A}},1_{\text{B}}},|1A,0B⟩\ket{1_{\text{A}},0_{\text{B}}},|1A,1B⟩\ket{1_{\text{A}},1_{\text{B}}}.

The structure ofH2qH_{\text{2q}}exposes the conditional logic required for CNOT. When A is in|0A⟩\ket{0_{\text{A}}}, qubit B sees only the diagonal elements and does not rotate; when A is in|1A⟩\ket{1_{\text{A}}}, the off-diagonalTABT_{\text{AB}}couples|0B⟩\ket{0_{\text{B}}}and|1B⟩\ket{1_{\text{B}}}and drives a bit flip. This is precisely the action of a control–target gate:
the CNOT gate flips the target qubit if and only if the control qubit is in|1⟩\ket{1}. That is,CNOT=ei​π4​(I1−Z1)​(I2−X2)=[1000010000010010].\text{CNOT}=e^{i\frac{\pi}{4}(I_{1}-Z_{1})(I_{2}-X_{2})}=\begin{bmatrix}1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0\end{bmatrix}.(13)

## V.2Ideal Gate Operation

We first consider the limiting case in which|TB||T_{\text{B}}|is small relative to|TAB||T_{\text{AB}}|(i.e.TB→0T_{\text{B}}\rightarrow 0), where the fidelity of the CNOT gate is maximized; the effect of a residual finiteTBT_{\text{B}}is examined in Sec.V.4. In this limit, comparing the reduced Hamiltonian (12) with the target gate (13) shows that CNOT can be generated by a single pulse ofHCNOT=[TA0000TA00000TAB00TAB0],H_{\text{CNOT}}=\begin{bmatrix}T_{\text{A}}&0&0&0\\
0&T_{\text{A}}&0&0\\
0&0&0&T_{\text{AB}}\\
0&0&T_{\text{AB}}&0\end{bmatrix},(14)

in which qubit B idles unless driven by qubit A. By inspection, the propagatorU​(t)=e−i​HCNOT​tU(t)=e^{-iH_{\text{CNOT}}t}isU​(t)=[e−i​TA​t0000e−i​TA​t0000cos⁡(TAB​t)−i​sin⁡(TAB​t)00−i​sin⁡(TAB​t)cos⁡(TAB​t)].U(t)=\begin{bmatrix}e^{-iT_{\text{A}}t}&0&0&0\\
0&e^{-iT_{\text{A}}t}&0&0\\
0&0&\cos(T_{\text{AB}}t)&-i\sin(T_{\text{AB}}t)\\
0&0&-i\sin(T_{\text{AB}}t)&\cos(T_{\text{AB}}t)\end{bmatrix}.(15)

When the control is in|0⟩A\ket{0}_{\text{A}}the target merely accumulates the phasee−i​TA​te^{-iT_{\text{A}}t}; when the control is in|1⟩A\ket{1}_{\text{A}}the target rotates aboutx^\hat{x}at rateTABT_{\text{AB}}.

To recover the CNOT of Eq. (13) up to an irrelevant global phase, we require the following two conditions for the gate timeτ\tau:
- 1.

τ×TAB=π2+π​kAB\tau\times T_{\text{AB}}=\frac{\pi}{2}+\pi k_{\text{AB}},
- 2.

τ×TA=π​(2​kA−kAB)+π2\tau\times T_{\text{A}}=\pi(2k_{\text{A}}-k_{\text{AB}})+\frac{\pi}{2},

withkA,kAB∈ℤk_{\text{A}},\,k_{\text{AB}}\in\mathbb{Z}(integers). Condition 1 makes the conditional rotation an odd multiple ofπ/2\pi/2, ensuring a full bit flip on the target withcos⁡(TAB​t)=0\cos(T_{\text{AB}}t)=0; condition 2 returns the control qubit to itself with the matching global phase±i\pm i.Figure 1:Ideal CNOT gate operation in a heterogeneous qubit encoding.Four Bell states (|Φ±⟩=12​(|0A​0B⟩±|1A​1B⟩)\ket{\Phi^{\pm}}=\frac{1}{\sqrt{2}}(\ket{0_{\text{A}}0_{\text{B}}}\pm\ket{1_{\text{A}}1_{\text{B}}}),|Ψ±⟩=12​(|0A​1B⟩±|1A​0B⟩)\ket{\Psi^{\pm}}=\frac{1}{\sqrt{2}}(\ket{0_{\text{A}}1_{\text{B}}}\pm\ket{1_{\text{A}}0_{\text{B}}})) are evolved under the Hamiltonian (14) over100100ns. Each panel shows the population of each computational basis state{|0A​0B⟩,|0A​1B⟩,|1A​0B⟩,|1A​1B⟩}\{\ket{0_{\text{A}}0_{\text{B}}},\ket{0_{\text{A}}1_{\text{B}}},\ket{1_{\text{A}}0_{\text{B}}},\ket{1_{\text{A}}1_{\text{B}}}\}. The populations of the computational states with leading0are unaffected and the populations of the states with leading11are interchanged.

Figure1demonstrates the action of Hamiltonian (14) on the four Bell states. Since the evolution is unitary, we work with pure states and plot the projection onto each computational basis state. The interqubit coupling is set toJ23=2​π×107J_{\text{23}}=2\pi\times 10^{7}rad/s (corresponding to experimentally measured frequency of1010MHz)[42,43], and the timing conditions above are imposed withkAB=kA=−1k_{\text{AB}}=k_{\text{A}}=-1(the shortest gate time). This fixesTAB=TA=−5​π×106T_{\text{AB}}=T_{\text{A}}=-5\pi\times 10^{6}rad/s and the gate time atτ=100\tau=100ns. Each Bell state transforms as expected under a perfect CNOT.

This figure was generated for a square pulse, without taking into account the finite ramp-up and ramp-down ofTABT_{\text{AB}}. However, we have verified that both sinusoidal and linear ramping yield a perfect CNOT with timing conditions determined by the time-averaged value ofTABT_{\text{AB}}.

Demonstrating the ideal limit, however, is only the first step. To assess whether this proposal is viable for realistic gate-defined quantum dot devices, we must account for three sources of gate infidelity: (i) leakage outside the computational subspace, (ii) nonzero exchange coupling in qubit B (J34=−TB≠0J_{34}=-T_{\text{B}}\neq 0), and (iii) decoherence due to imperfect isolation from the environment. We address these below.

## V.3Effect of Leakage

For a two-qubit gate, the computational space consists of 4 out of the 16 single occupation manifold levels, with 12 being leakage states. We verify that CNOT operation does not cause considerable leakage outside of the computational space in Figure2. To do so, we propagate the dynamics under the full 16-level Hamiltonian as determined by Eq. (6).
Echoing the ideal example (Sec.V.2), we keep the level splitting of theS​T−ST_{-}qubitTA=ζ12(z)−J12=−5​π×106T_{\text{A}}=\zeta^{(z)}_{12}-J_{12}=-5\pi\times 10^{6}rad/s andTB=−J34=0T_{\text{B}}=-J_{34}=0, and the interqubit coupling constant atTAB=−J23/4=−5​π×106T_{\text{AB}}=-J_{23}/4=-5\pi\times 10^{6}rad/s.
The magnetic fields are oriented along thezz-axis withζ1(z)=ζ2(z)=2​π×109\zeta^{(z)}_{1}=\zeta^{(z)}_{2}=2\pi\times 10^{9}rad/s (11GHz) andζ3(z)=ζ4(z)=1.7​π×109\zeta^{(z)}_{3}=\zeta^{(z)}_{4}=1.7\pi\times 10^{9}rad/s (850850MHz), which are representative of the usual experimental conditions[44,35,36].
The non-zero magnetic field in thezz-direction is required to break the triplet degeneracy and suppress the leakage into theT+T_{+}states. It is also necessary to establish a non-zero magnetic field gradient in thezzdirection between the dots to suppress the leakage into|T0,T−⟩\ket{T_{0},T_{-}}.

Each panel of Fig.2shows the system initialized in one of the four computational basis states and evolved over a period of100100ns under the influence of the CNOT gate pulse. Because the populations of leakage states are orders of magnitude smaller than that of the computational states, we utilize a secondaryyy-axis to show the sum of populations in all the leakage states in gray. When the control qubit is in the state|0⟩\ket{0}, the two-qubit state remains unchanged, apart from the leakage of less than4×10−44\times 10^{-4}. When the control qubit is in the state|1⟩\ket{1}, leakage of up to4×10−34\times 10^{-3}accompanies the bit flip of the second qubit. In this case, the slightly higher leakage is due to transitions to|T0​T−⟩\ket{T_{0}T_{-}}and|S​T−⟩\ket{ST_{-}}, i.e. the leakage states that have the same structure as the computational basis states but opposite qubit ordering.

We thus conclude that the magnetic field gradientΔ​ζ23(z)\Delta\zeta^{(z)}_{23}of realistic magnitude (150150MHz) efficiently suppresses the leakage during this novel implementation of the CNOT gate.Figure 2:CNOT in the presence of leakage states.Time evolution over the gate duration of100100ns of the four-spin system. Note that the population outside of the computational space is plotted in gray on a secondaryyy-axis which is zoomed in by a factor of 1000 (panels a,b) and a factor of 100 (panels c,d).

## V.4Influence ofTB≠0T_{\text{B}}\neq 0

We now assess the influence ofTB≠0T_{\text{B}}\neq 0on the CNOT gate. For this, we increase the|TB||T_{\text{B}}|magnitude while keeping the gate timeτ\tauand other gate parameters intact. Figure3shows the percent of|10⟩↔|11⟩\ket{10}\leftrightarrow\ket{11}interconversion with increasing|TB/TAB||T_{\text{B}}/T_{\text{AB}}|. The simulations are performed with the same parameters as in Fig.2, exceptTBT_{\text{B}}is allowed to vary. The leftmost point corresponds toTB=0T_{\text{B}}=0, featuring the state interconversion of 99.6% shown in Fig.2.
The conversion probability decays as∼|TB/TAB|2\sim|T_{\text{B}}/T_{\text{AB}}|^{2}, with the linear term being negligible in the range considered. For this reason, increasing|TB||T_{\text{B}}|to as much as 10% of|TAB||T_{\text{AB}}|leaves the effectiveness of the gate essentially intact, with a reduction of the state interconversion of no more than 0.2%.

When|TB|≠0|T_{\text{B}}|\neq 0it breaks the degeneracy between|0A,0B⟩\ket{0_{\text{A}},0_{\text{B}}}and|0A,1B⟩\ket{0_{\text{A}},1_{\text{B}}}, and that between|1A,0B⟩\ket{1_{\text{A}},0_{\text{B}}}and|1A,1B⟩\ket{1_{\text{A}},1_{\text{B}}}. This leads to a shift of the transition frequency that transitions the originally designed gate (forTB=0T_{\text{B}}=0) off-resonance, and to mixing of the computational states.
The detrimental influence ofTB≠0T_{\text{B}}\neq 0on gate operation can be further minimized by correcting for the frequency shift, changing the gate timing, and accounting for the coherent gate errors that result from the computational state mixing. Thus, the results shown here overestimate the influence ofTBT_{\text{B}}on gate operation, and should be seen as an upper limit.

Overall, these results show that small|TB/TAB|<0.1|T_{\text{B}}/T_{\text{AB}}|<0.1are tolerated while maintaining high gate fidelity. This requirement of small|TB/TAB||T_{\text{B}}/T_{\text{AB}}|can be achieved by controlling the gate voltages, in a manner akin to what was already accomplished in Ref.35for nonzero magnetic field gradients that are made negligibly small relative to the intraqubit exchange coupling.Figure 3:Effect of non-zeroTBT_{\text{B}}.Percent interconversion between the|10⟩\ket{10}and|11⟩\ket{11}upon applying the CNOT gate as a function ofTBT_{\text{B}}relative toTABT_{\text{AB}}. Note the quadratic decay of the percent conversion, enabling essentially full interconversion for small values ofTBT_{\text{B}}.

## V.5Effect of Quasi-Static Noise

We next address the effect of the environmentally-induced decoherence on the performance of the CNOT gate. In semiconductor quantum dots, it is the low-frequency components of electrical and hyperfine noise that dominate. Because this source of quantum noise is essentially frozen during the dynamics, a quasi-static treatment is appropriate[15]. In this approach, the noise is treated as a source of inhomogeneity and sampled from a Gaussian distribution to define parameters for an individual quantum realization, which are then averaged to yield the density matrix influenced by quasi-static noise.

For these simulations, we keep the average interqubit couplingTAB=−J23/4=−5​π×106T_{\text{AB}}=-J_{23}/4=-5\pi\times 10^{6}rad/s but apply a sinusoidal ramp-on profile[38]that starts and ends withTAB=0T_{\text{AB}}=0over the100100ns duration of the pulse as in Fig.2. Noise is introduced in both thezz-component of the magnetic field and the exchange couplings: isotropic Gaussian magnetic-field fluctuations with mean0and standard deviation0.44​π×1060.44\pi\times 10^{6}rad/s per Cartesian component — corresponding to a single-spin inhomogeneous dephasing timeT2∗≈3.6​μT_{2}^{*}\approx 3.6\,\mus — and Gaussian fractional exchange noise with standard deviation(2​π​Q)−1(2\pi Q)^{-1}, with an exchange-oscillation quality factorQ=40Q=40, which is accessible in nuclear-spin free systems like28Si{}\hphantom{{}^{\mathrm{28}}_{\mathrm{}}}{\vphantom{\mathrm{X}}}^{\mathchoice{\hbox to0.0pt{\hss$\displaystyle\vphantom{\smash[t]{\mathrm{2}}}\mathrm{28}$}}{\hbox to0.0pt{\hss$\textstyle\vphantom{\smash[t]{\mathrm{2}}}\mathrm{28}$}}{\hbox to0.0pt{\hss$\scriptstyle\vphantom{\smash[t]{\mathrm{2}}}\mathrm{28}$}}{\hbox to0.0pt{\hss$\scriptscriptstyle\vphantom{\smash[t]{\mathrm{2}}}\mathrm{28}$}}}\kern 0.0pt\mathrm{Si}[45,46,47,48].
Leakage is also taken into account because the simulation spans both the computational and leakage states. We further consider the cases ofTB=0T_{\text{B}}=0andTB≠0T_{\text{B}}\neq 0.

(a)(b)Figure 4:Theχ\chi-matrix characterizing the proposed CNOT pulseapplied to a pair of double quantum dots with (a)TB=0T_{\text{B}}=0featuring99.6%99.6\%gate fidelity and (b)TB=0.1​TABT_{\text{B}}=0.1T_{\text{AB}}with99.2%99.2\%gate fidelity. The parameters in Eq.6are:TA=−5​π×106T_{\text{A}}=-5\pi\times 10^{6}rad/s,ζ12(z)=1.3​π×109\zeta^{(z)}_{12}=1.3\pi\times 10^{9}rad/s andζ34(z)=π×109\zeta^{(z)}_{34}=\pi\times 10^{9}rad/s (650650and500500MHz),TABav=−5​π×106T^{\text{av}}_{\text{AB}}=-5\pi\times 10^{6}rad/s. Noise magnitudes are set byQ=40Q=40for the exchange noise on each nearest-neighbor dot pair (1–2, 2–3, 3–4) andΔ​Bi(z)=0.44​π×106\Delta B_{i}^{(z)}=0.44\pi\times 10^{6}rad/s for the magnetic noise. Note that the 0.4% decrease in fidelity for panel (b) is mostly due to the coherent error.

To characterize the two-qubit CNOT operation, Figure4reconstructs the process matrix (orχ\chi-matrix) for the proposed CNOT gate for (a)TB=0T_{\text{B}}=0and (b)TB=0.1​TABT_{\text{B}}=0.1T_{\text{AB}}.
Each element of the matrix is given by how the corresponding two-qubit tensor-product Pauli basis element (e.g.Y​Z=YA⊗ZBYZ=Y_{\text{A}}\otimes Z_{\text{B}}whereII,XX,YYandZZare the usual Pauli matrices) transforms under the action of this operation. The ideal CNOT gate has 16 non-zero elements, all equal to±1/4\pm 1/4. Specifically, only the Pauli componentsI​III,I​ZIZ,X​IXI, andX​ZXZcontribute, reflecting the decompositionUCNOT=(I​I+I​Z+X​I−X​Z)/2U_{\text{CNOT}}=(II+IZ+XI-XZ)/2. Nonzero elements outside this ideal pattern quantify imperfections in the implemented gate that may arise due to noise, and that reduce gate fidelity.

The gate quality is characterized via process fidelity that is defined asℱ=Tr⁡[χideal†​χreal].\mathcal{F}=\operatorname{Tr}\left[\chi^{\dagger}_{\text{ideal}}\chi_{\text{real}}\right].(16)

The calculated fidelities are99.6%99.6\%forTB=0T_{\text{B}}=0and99.2%99.2\%forTB=0.1​TABT_{\text{B}}=0.1T_{\text{AB}}. The decrease in fidelity of0.4%0.4\%forTB≠0T_{\text{B}}\neq 0is minor, keeping the gate within the fault-tolerant threshold of 99% for two-qubit gates and is largely attributed to the incomplete rotation. The coherent error caused byTB≠0T_{\text{B}}\neq 0can be further reduced as discussed in Sec.V.4. Thus, the proposed hybridS​T−+S​T0ST_{-}+ST_{0}platform operates the CNOT gate in the fault-tolerant regime under realistic, experimentally accessible conditions, confirming the heterogeneous-architecture strategy introduced in Sec.IV.3as a practical route to asymmetric two-qubit gates.

## V.6Effect of the Magnetic Field StrengthFigure 5:Fidelity of the CNOT for different magnetic fieldson qubitAA,ζ12(z)\zeta^{(z)}_{\text{12}}and qubitBB,ζ34(z)\zeta^{(z)}_{\text{34}}. The operation is robust to the particular magnetic field strength as long as the magnetic field and the gradient are both non-zero.

As discussed in Secs.IV.2andV.3, magnetic field gradients between qubitAAandBBare needed to suppress the leakage out of the computational states during this novel implementation of the CNOT gate. The gradient is necessary to break the degeneracy between the computational triplet states and the leakage state with the triplet ordering interchanged (e.g.T−​T0T_{-}T_{0}andT0​T−T_{0}T_{-}).

Figure5shows the fidelity of the CNOT gate as a function of magnetic field strengths on the two individual qubits (dots 1 and 2 encode theS​T−ST_{-}qubit; 3 and 4 theS​T0ST_{0}). For simplicity, we focus onTB=0T_{\text{B}}=0, withTB≠0T_{\text{B}}\neq 0results being very similar. Lighter colors signify higher fidelities with fidelities above 99% shown in green, those between 90% and 99% in blue, and those below 90% in gray. In the absence of magnetic field gradients (diagonal), gate fidelities are poor.
By contrast, gate fidelity in the high 90’s is achieved for various magnetic field strengths so long as there is a sufficiently strong magnetic field gradient between the qubits (off-diagonals). Note that the magnetic field gradient suppresses the leakage more effectively for a particular direction of magnetic field gradient, i.e. when theS​T−ST_{-}qubit is subject to stronger magnetic field, as reflected by the asymmetry of the plot. This is because the stronger magnetic field does not meaningfully affect theS​T0ST_{0}qubit; in contrast, on theS​T−ST_{-}qubit, stronger field better suppresses the leakage to theT+T_{+}state. This magnetic field gradient directionality cannot make a difference in the case of homogeneous mapping as the qubits are identical. Crucially, the CNOT gate fidelity is robust for a range of magnetic field strengths off-diagonal in the lower triangular portion of the plot.

## VIDiscussion

## VI.1Implementation in Double Quantum Dots

The importance of having a “simple” CNOT is hard to overestimate as it is heavily featured in many quantum algorithms, and is needed to form the textbook example of the universal gate set[1]. Successful qubit platforms often feature a “simple” CNOT. For example, the cross-resonance gate often implemented in superconducting qubits[49]requires only one two-qubit interaction and one additional localπ/2\pi/2rotation of each qubit to realize a CNOT gate.

Our proposal for the realization of a “simple” high-fidelity CNOT gate in double quantum dots by designing an alternatingS​T−ST_{-}-S​T0ST_{0}heterogeneousA​BABqubit architecture can be implemented straightforwardly in existing DQD devices, as the nature of each qubit can be tuned through gate voltages. In fact, we have shown in Sec.V.5that the gate can be operated above the fault-tolerance threshold of 99% under realistic experimental conditions.

Previously, there had been other proposals to employ hybrid architectures[40,41]that argued that the hybrid approach allowed them to utilize the respective strengths of the two qubit platforms. More specifically, the authors combine a singlet-triplet qubit with a Loss-DiVincenzo single-spin qubit. They take advantage of the significantly faster qubit initialization and readout of singlet-triplet qubits provided by the Pauli spin blockade (as opposed to the slow spin-selective tunneling to a lead used in the Loss-DiVincenzo qubit), and the exceptionally long coherence times of single-spin qubits (as opposed to the much shorter coherence times of singlet-triplet qubits). By contrast to these earlier studies, we do not focus on initialization or readout advantages of the specific qubit platform, but rather on the asymmetry that the heterogeneous encoding generates. Further, instead of using a different number of dots to construct theAAandBBqubit, our proposal uses the same number of dots forAAandBBmaking arbitrarily encoded arrays accessible on any singlet-triplet qubit device, including those that exist today.

## VI.2Scaling Up

As shown, CNOT or other asymmetric gates are best implemented in heterogeneousA​BABqubit architectures.
Scaling up the two-qubit proposal presented here to multi-qubit devices is a natural direction for future research. To facilitate implementation of the CNOT gates between any two nearest neighbors, the multi-qubit device should continue the alternatingA​BABpattern. Although this goal can bring additional experimental challenges (such as gate cross-talk), these are the usual hurdles when the number of qubits on a semiconductor quantum dot device is increased.

Although the proposed CNOT gate is, in principle, enough to achieve universal quantum computation when complemented with single-qubit gates, in practice certain computations will introduce significant gate overheads. For instance, here, we have directly addressed implementation of a CNOT gate between any two nearest-neighbor dots. However, if an operation on distant qubits is desired, it can be achieved either by qubit shuttling or by a consecutive application of the SWAP gates to bring them together and then return them back. This introduces overhead since each SWAP requires 3 CNOT operations. Therefore, while it is not strictly necessary for universal computation, direct implementation of other two-qubit gates like SWAP could significantly reduce the gate overhead.

In contrast to CNOT, symmetric gates like SWAP benefit from the existing homogeneous qubit architecture. In practice, the flexibility of the QD setup enables one to choose a qubit mapping that minimizes the number of elementary steps needed to implement a particular calculation, and this choice can be made immediately before the run, optimizing the qubit encoding for a particular quantum algorithm.

## VI.3Asymmetry as a Resource

The central challenge in realizing high-fidelity entangling gates lies in the fundamental mismatch between the symmetric physical interactions of identical particles (e.g., Heisenberg exchange) and the asymmetric logical requirements of the CNOT gate. Traditionally, quantum information architectures resolve this mismatch at the “software” level via composite, multi-pulse sequences that artificially break the symmetry. Although functional, this approach inevitably increases logical gate depth, prolongs gate times, and exposes the system to further decoherence.

In an attempt to go beyond the limitations of the Heisenberg exchange interaction, various strategies have been proposed at the hardware level as well. One attempt[50]is to couple qubits indirectly via a mediator quantum state that interacts with both of them.
In Ref.51, a superconducting qubit was considered as a mediator between twoS​T0ST_{0}qubits and was shown to yield a longitudinal field Ising interaction between them, which is still symmetric and identical to the coupling between the resonant qubits. The Loss group also proposed mediating interactions between Majorana qubits using quantum-dot spin qubits, which enables a CNOT gate on Majorana qubits without interqubit braiding[52].
The other strategy to generate asymmetry utilizes spin-orbit coupling. Unlike electrons, holes in silicon are affected by strong spin-orbit interactions that create strong exchange anisotropy, which breaks the symmetry and facilitates the realization of asymmetric gates, such as the controlled rotation (CROT) gate[19]. We leave this promising direction for future research.

By contrast, our proposal demonstrates that this symmetry breaking can instead be offloaded directly into the physical hardware and interfaced with standard qubit designs in DQDs. By alternatingS​T0ST_{0}andS​T−ST_{-}encodings, the hardware naturally yields an asymmetricX​ZXZeffective Hamiltonian. This physical asymmetry translates directly into a reduced quantum operation overhead, fulfilling the fundamental quantum information requirement for a fast, single-pulse control-target gate. Framing device engineering through this lens of exchange symmetry provides a clear theoretical framework for identifying and solving hardware bottlenecks at the physical level before they become algorithmic liabilities.

While we have demonstrated this principle in a DQD device, the underlying principle — that a symmetric physical interaction acquires an asymmetric form when projected onto heterogeneously encoded logical subspaces — is general. Therefore, other qubit platforms that feature identical physical constituents, symmetric two-body coupling, and the possibility of inequivalent qubit encodings within a single device can benefit from this. Trapped ions offer a particularly close analog. The Mølmer–Sørensen interaction[53]generates an effective spin–spin coupling that is symmetric under exchange of the ions, while theomgarchitecture[54](employing optical-frequency, metastable-state and ground-state qubits) allows ground-state, metastable, and optical qubit encodings to coexist in a single ion species. Alternatively, a qubit may be encoded in the decoherence-free subspace{|01⟩,|10⟩}\{\ket{01},\ket{10}\}of an ion pair[55,32]— a direct analog of theS​T0ST_{0}encoding in DQDs — while a second is carried by a bare ion. In either case, the heterogeneous encoding could provide asymmetry for the interqubit interaction (see Sec.II.2). Neutral-atom arrays provide a similar setting: the van der Waals interaction between Rydberg-excited atoms is manifestly symmetric between identical atoms[56,57], yet if one atom encodes its qubit in hyperfine or nuclear-spin ground states while its neighbor employs a ground–Rydberg or optical-clock encoding — as realized in the171Yb{}\hphantom{{}^{\mathrm{171}}_{\mathrm{}}}{\vphantom{\mathrm{X}}}^{\mathchoice{\hbox to0.0pt{\hss$\displaystyle\vphantom{\smash[t]{\mathrm{2}}}\mathrm{171}$}}{\hbox to0.0pt{\hss$\textstyle\vphantom{\smash[t]{\mathrm{2}}}\mathrm{171}$}}{\hbox to0.0pt{\hss$\scriptstyle\vphantom{\smash[t]{\mathrm{2}}}\mathrm{171}$}}{\hbox to0.0pt{\hss$\scriptscriptstyle\vphantom{\smash[t]{\mathrm{2}}}\mathrm{171}$}}}\kern 0.0pt\mathrm{Yb}omgarchitecture[58,59]— the projected interaction acts as a phase-type (Z) operator on one logical qubit and a population-dependent projector on the other, yielding precisely the encoding-induced asymmetry discussed here.

It is instructive to contrast this principle with superconducting circuits, where asymmetric effective interactions are well established but arise from a fundamentally different origin. In the cross-resonance gate[49], a symmetric capacitive coupling between two fixed-frequency transmons yields an effectiveZ​XZXinteraction when one qubit is driven at the frequency of the other; the asymmetry, however, is inherited from parameter inhomogeneity — the deliberate detuning of two physically distinct circuits, which singles out control and target roles — rather than from the structure of the qubit encoding. The same holds for hybrid transmon–fluxonium gates[60], where the two circuits differ in their Hamiltonians from the outset and no symmetry exists to be broken. The closest superconducting analogue is therefore not found among circuit-QED two-qubit gates but in bosonic codes, where nominally identical cavities coupled by a symmetric beam-splitter or cross-Kerr interaction can host different logical encodings — for example, a cat code in one mode[61]and a Gottesman–Kitaev–Preskill code[62]in the other — such that the projected logical interaction is again rendered asymmetric by the encoding alone. We therefore expect heterogeneous encoding to offer a hardware-efficient route to asymmetric effective interactions in any platform whose native couplings are symmetric, provided it features multiple inequivalent qubit encodings.

## VIIConclusions

We have identified a symmetry mismatch at the heart of two-qubit gate design: the interactions naturally available between identical particles—Heisenberg exchange and Coulomb repulsion—are invariant
under qubit exchange, while control–target gates such as CNOT are not. Whenever the qubits are encoded
identically (homogeneously), this symmetry must survive the projection onto the computational subspace. Homogeneous qubit encodings therefore cannot implement asymmetric control–target gates directly: the asymmetry must be supplied, for instance, by additional single- or two-qubit operations, at the cost of longer gate times and accumulated errors.

By contrast, encoding neighboring qubits heterogeneously breaks the exchange symmetry at the hardware level, so that the same symmetric physical interaction projects onto an asymmetric effective interaction in the logical subspace. We have exploited this principle in semiconductor double quantum dots,
where multiple qubit encodings coexist on identical hardware and can be selected by gate voltages alone. Pairing anS​T−ST_{-}with anS​T0ST_{0}qubit converts the symmetric Heisenberg exchange into an asymmetricX​ZXZcoupling, enabling a single-pulse, all-electrical CNOT gate with a duration of100100ns. Our simulations account for the leakage out of the computational subspace, residual target-qubit splitting, and quasi-static charge noise as well as hyperfine noise and predict process fidelities above99%99\%for parameters representative of isotopically purified silicon. This is achieved without microwave driving, strong spin–orbit interaction, or modifications to existing device layouts. The proposal is thus
directly testable on current singlet-triplet devices.

More broadly, our results establish qubit encoding as a design resource in its own right: heterogeneous encoding converts a fixed, symmetric physical interaction into an asymmetric logical one, moving symmetry breaking from the pulse sequence into the hardware. Our finding has potential implications to any platform that combines identical physical constituents, symmetric two-body couplings, and inequivalent qubit encodings.

## Acknowledgements.This material is based upon work supported by the National Science Foundation under grant No. PHY-2310657. RK acknowledges helpful discussions with Anna Spak.

## References
- Nielsen and Chuang [2011]M. A. Nielsen and I. L. Chuang,Quantum Computation and
Quantum Information(Cambridge University Press, 2011).
- Lawrieet al.[2023]W. I. L. Lawrie, M. Rimbach-Russ, F. van
Riggelen, N. W. Hendrickx, S. L. de Snoo, A. Sammak,
G. Scappucci, J. Helsen, and M. Veldhorst, Simultaneous single-qubit driving of semiconductor spin qubits at
the fault-tolerant threshold,Nat. Commun.14, 3617 (2023).
- Liet al.[2023]Z. Li, P. Liu, P. Zhao, Z. Mi, H. Xu, X. Liang, T. Su, W. Sun, G. Xue, J.-N. Zhang, W. Liu, Y. Jin, and H. Yu, Error per single-qubit gate below 10-4
in a superconducting qubit,npj Quantum Inf.9, 111 (2023).
- Smith [2025]M. C. Smith, Single-qubit gates with
errors at the 10-7level, Phys. Rev. Lett.134,10.1103/42w2-6ccy(2025).
- Hugheset al.[2025]A. C. Hughes, R. Srinivas,
C. M. Löschnauer,
H. M. Knaack, R. Matt, C. J. Ballance, M. Malinowski, T. P. Harty, and R. T. Sutherland,Trapped-ion
two-qubit gates with>>99.99% fidelity without ground-state cooling(2025),arXiv:2510.17286 [quant-ph].
- Noiriet al.[2022]A. Noiri, K. Takeda,
T. Nakajima, T. Kobayashi, A. Sammak, G. Scappucci, and S. Tarucha, Fast
universal quantum gate above the fault-tolerance threshold in silicon,Nature601, 338 (2022).
- Ding [2023]L. Ding, High-fidelity,
frequency-flexible two-qubit fluxonium gates with a transmon coupler, Phys. Rev. X13,10.1103/PhysRevX.13.031035(2023).
- Li [2024]R. Li, Realization of high-fidelity
CZ gate based on a double-transmon coupler, Phys. Rev. X14,10.1103/PhysRevX.14.041050(2024).
- Marxeret al.[2025]F. Marxer, J. Mrożek,
J. Andersson, L. Abdurakhimov, J. Adam, V. Bergholm, R. Beriwal, C. F. Chan, S. Dahl, S. R. Das,
F. Deppe, O. Fedorets, Z. Gao, A. G. Frieiro, D. Gusenkova, A. Guthrie, T. Hiltunen, H. Hsu, E. Hyyppä, J. Ikonen,
S. Inel, S. W. Jolin, A. Karis, S.-G. Kim, W. Kindel, A. Komlev, M. Koistinen, R. Kokkoniemi, S. Kumar, H.-S. Ku, J. Lamprich, S. Laine,
A. Landra, L.-H. Lee, N. Lethif, P. Liebermann, W. Liu, K. Mitra, T. Mylläri,
C. Ockeloen-Korppi,
T. Orell, A. Plyshch, J. Räbinä, A. Rebello, M. Renger, O. Reentilä, J. Ritvas, S. Saarinen, O. Salmenkivi, M. Sarsby, M. Savytskyi, V. Selinmaa, M. Steggles, E. Takala, I. Takmakov, B. Tarasinski, J. Tuorila, A. Välimaa, J. Verjauw, J. Wesdorp, N. Wurz, W. Qiu, L. Zhu, J. Hassel, J. Heinsoo, A. Geresdi, and A. Vepsäläinen,Above 99.9%
fidelity single-qubit gates, two-qubit gates, and readout in a single
superconducting quantum device(2025),arXiv:2508.16437 [quant-ph].
- Liet al.[2012]R. Li, X. Hu, and J. Q. You, Controllable exchange coupling between two
singlet-triplet qubits, Phys.
Rev. B86,10.1103/PhysRevB.86.205306(2012).
- Klinovajaet al.[2012]J. Klinovaja, D. Stepanenko, B. I. Halperin, and D. Loss, Exchange-based CNOT
gates for singlet-triplet qubits with spin-orbit interaction, Phys. Rev. B86,10.1103/PhysRevB.86.085423(2012).
- Zajacet al.[2018]D. M. Zajac, A. J. Sigillito, M. Russ,
F. Borjans, J. M. Taylor, G. Burkard, and J. R. Petta, Resonantly driven CNOT gate for electron spins,Science359, 439 (2018).
- Veldhorstet al.[2015]M. Veldhorst, C. H. Yang,
J. C. C. Hwang, W. Huang, J. P. Dehollain, J. T. Muhonen, S. Simmons, A. Laucht, F. E. Hudson, K. M. Itoh, A. Morello, and A. S. Dzurak, A two-qubit logic gate in
silicon,Nature526, 410 (2015).
- Schuch and Siewert [2003]N. Schuch and J. Siewert, Natural two-qubit gate
for quantum computation using the XY interaction,Phys. Rev. A67, 32301 (2003).
- Burkardet al.[2023]G. Burkard, T. D. Ladd,
A. Pan, J. M. Nichol, and J. R. Petta, Semiconductor spin qubits,Rev. Mod. Phys.95, 25003 (2023).
- Tayloret al.[2005]J. M. Taylor, H.-A. Engel,
W. Dür, A. Yacoby, C. M. Marcus, P. Zoller, and M. D. Lukin, Fault-tolerant architecture for quantum computation using
electrically controlled semiconductor spins,Nat. Phys.1, 177
(2005).
- Rasmussenet al.[2021]S. E. Rasmussen, K. S. Christensen, S. P. Pedersen, L. B. Kristensen, T. Bækkegaard, N. J. S. Loft, and N. T. Zinner,The superconducting circuit companion – an introduction with worked
examples, https://arxiv.org/abs/2103.01225v3
(2021).
- Sørensen [2000]A. Sørensen, Entanglement and
quantum computation with ions in thermal motion, Phys. Rev. A62,10.1103/PhysRevA.62.022311(2000).
- Geyeret al.[2024]S. Geyer, B. Hetényi,
S. Bosco, L. C. Camenzind, R. S. Eggli, A. Fuhrer, D. Loss, R. J. Warburton, D. M. Zumbühl, and A. V. Kuhlmann, Anisotropic
exchange interaction of two hole-spin qubits,Nat. Phys.20, 1152 (2024).
- Wanget al.[2011]D. S. Wang, A. G. Fowler, and L. C. L. Hollenberg, Surface code quantum
computing with error rates over 1%,Phys. Rev. A83, 020302 (2011).
- Veldhorstet al.[2017]M. Veldhorst, H. G. J. Eenink, C. H. Yang, and A. S. Dzurak, Silicon CMOS architecture for a
spin-based quantum computer,Nat. Commun.8, 1766 (2017).
- Vandersypenet al.[2017]L. M. K. Vandersypen, H. Bluhm, J. S. Clarke, A. S. Dzurak, R. Ishihara, A. Morello,
D. J. Reilly, L. R. Schreiber, and M. Veldhorst, Interfacing spin qubits in quantum dots and donors—hot,
dense, and coherent,npj Quantum Inf.3, 34 (2017).
- Chatterjeeet al.[2021]A. Chatterjee, P. Stevenson, S. De Franceschi, A. Morello, N. P. de
Leon, and F. Kuemmeth, Semiconductor qubits in
practice,Nat. Rev. Phys.3, 157 (2021).
- Steinackeret al.[2025]P. Steinacker, N. Dumoulin Stuyck, W. H. Lim, T. Tanttu,
M. Feng, S. Serrano, A. Nickl, M. Candido, J. D. Cifuentes, E. Vahapoglu, S. K. Bartee, F. E. Hudson,
K. W. Chan, S. Kubicek, J. Jussot, Y. Canvel, S. Beyne, Y. Shimura, R. Loo, C. Godfrin, B. Raes,
S. Baudot, D. Wan, A. Laucht, C. H. Yang, A. Saraiva, C. C. Escott, K. De Greve, and A. S. Dzurak, Industry-compatible
silicon spin-qubit unit cells exceeding 99% fidelity,Nature646, 81 (2025).
- Shulmanet al.[2012]M. D. Shulman, O. E. Dial,
S. P. Harvey, H. Bluhm, V. Umansky, and A. Yacoby, Demonstration of entanglement of electrostatically coupled
singlet-triplet qubits,Science336, 202 (2012).
- Wonget al.[2015]C. H. Wong, M. A. Eriksson,
S. N. Coppersmith, and M. Friesen, High-fidelity singlet-triplet S-T - qubits in
inhomogeneous magnetic fields,Phys. Rev. B92, 45403 (2015).
- Loss and DiVincenzo [1998]D. Loss and D. P. DiVincenzo, Quantum computation
with quantum dots,Phys. Rev. A57, 120 (1998).
- Laird [2010]E. A. Laird, Coherent spin manipulation
in an exchange-only qubit, Phys. Rev. B82,10.1103/PhysRevB.82.075403(2010).
- Russet al.[2018]M. Russ, J. R. Petta, and G. Burkard, Quadrupolar exchange-only spin
qubit, Phys. Rev. Lett.121,10.1103/PhysRevLett.121.177701(2018).
- Barneset al.[2011]E. Barnes, J. P. Kestner,
N. T. T. Nguyen, and S. Das Sarma, Screening of charged impurities with multielectron
singlet-triplet spin qubits in quantum dots,Phys. Rev. B84, 235309 (2011).
- Burkardet al.[1999]G. Burkard, D. Loss, and D. P. DiVincenzo, Coupled quantum dots as quantum
gates,Phys. Rev. B59, 2070 (1999).
- Lidaret al.[1998]D. A. Lidar, I. L. Chuang, and K. B. Whaley, Decoherence-free subspaces for quantum
computation,Phys. Rev. Lett.81, 2594 (1998).
- Levy [2002]J. Levy, Universal quantum
computation with spin-$1/2$ pairs and heisenberg exchange,Phys. Rev. Lett.89, 147902 (2002).
- Jirovecet al.[2021]D. Jirovec, A. Hofmann,
A. Ballabio, P. M. Mutter, G. Tavani, M. Botifoll, A. Crippa, J. Kukucka, O. Sagi, F. Martins, J. Saez-Mollejo, I. Prieto, M. Borovkov,
J. Arbiol, D. Chrastina, G. Isella, and G. Katsaros, A singlet-triplet hole spin qubit in planar Ge,Nat. Mater.20, 1106 (2021).
- Zhanget al.[2025]X. Zhang, E. Morozova,
M. Rimbach-Russ,
D. Jirovec, T.-K. Hsiao, P. C. Fariña, C.-A. Wang, S. D. Oosterhout, A. Sammak, G. Scappucci, M. Veldhorst, and L. M. K. Vandersypen, Universal control of four singlet–triplet qubits,Nat. Nanotechnol.20, 209 (2025).
- Takeda [2020]K. Takeda, Resonantly driven
singlet-triplet spin qubit in silicon, Phys. Rev. Lett.124,10.1103/PhysRevLett.124.117701(2020).
- Nielsenet al.[2012]E. Nielsen, R. P. Muller, and M. S. Carroll, Configuration interaction
calculations of the controlled phase gate in double quantum dot qubits,Phys. Rev. B85, 35319 (2012).
- Wardrop and Doherty [2014]M. P. Wardrop and A. C. Doherty, Exchange-based two-qubit
gate for singlet-triplet qubits, Phys. Rev. B90,10.1103/PhysRevB.90.045418(2014).
- Chanet al.[2021]G. X. Chan, J. P. Kestner, and X. Wang, Charge noise suppression in capacitively coupled
singlet-triplet spin qubits under magnetic field, Phys. Rev. B103,10.1103/PhysRevB.103.L161409(2021).
- Mehl [2015]S. Mehl, Simple operation sequences
to couple and interchange quantum information between spin qubits of
different kinds, Phys. Rev. B92,10.1103/PhysRevB.92.115448(2015).
- Noiriet al.[2018]A. Noiri, T. Nakajima,
J. Yoneda, M. R. Delbecq, P. Stano, T. Otsuka, K. Takeda, S. Amaha, G. Allison, K. Kawasaki, Y. Kojima, A. Ludwig, A. D. Wieck, D. Loss, and S. Tarucha, A fast quantum interface
between different spin qubit encodings,Nat. Commun.9, 5066 (2018).
- Reedet al.[2016]M. D. Reed, B. M. Maune,
R. W. Andrews, M. G. Borselli, K. Eng, M. P. Jura, A. A. Kiselev, T. D. Ladd, S. T. Merkel, I. Milosavljevic, E. J. Pritchett, M. T. Rakher, R. S. Ross,
A. E. Schmitz, A. Smith, J. A. Wright, M. F. Gyure, and A. T. Hunter, Reduced Sensitivity to Charge Noise in
Semiconductor Spin Qubits via Symmetric Operation,Phys. Rev. Lett.116, 110402 (2016).
- Connorset al.[2022]E. J. Connors, J. Nelson,
L. F. Edge, and J. M. Nichol, Charge-noise spectroscopy of Si/SiGe
quantum dots via dynamically-decoupled exchange oscillations,Nat. Commun.13, 940 (2022).
- Wuet al.[2014]X. Wu, D. R. Ward,
J. R. Prance, D. Kim, J. K. Gamble, R. T. Mohr, Z. Shi, D. E. Savage, M. G. Lagally, M. Friesen, S. N. Coppersmith, and M. A. Eriksson, Two-axis control of a
singlet-triplet qubit with an integrated micromagnet,Proc. Natl. Acad. Sci.111, 11938 (2014).
- Dialet al.[2013]O. E. Dial, M. D. Shulman,
S. P. Harvey, H. Bluhm, V. Umansky, and A. Yacoby, Charge noise spectroscopy using coherent exchange oscillations in a
singlet-triplet qubit,Phys. Rev. Lett.110, 146804 (2013).
- Nicholet al.[2017]J. M. Nichol, L. A. Orona,
S. P. Harvey, S. Fallahi, G. C. Gardner, M. J. Manfra, and A. Yacoby, High-fidelity entangling gate for double-quantum-dot spin qubits,npj Quantum Inf.3, 3 (2017).
- Yonedaet al.[2018]J. Yoneda, K. Takeda,
T. Otsuka, T. Nakajima, M. R. Delbecq, G. Allison, T. Honda, T. Kodera, S. Oda, Y. Hoshi, N. Usami,
K. M. Itoh, and S. Tarucha, A quantum-dot spin qubit with coherence limited by
charge noise and fidelity higher than 99.9%,Nat. Nanotechnol.13, 102 (2018).
- Mauneet al.[2012]B. M. Maune, M. G. Borselli,
B. Huang, T. D. Ladd, P. W. Deelman, K. S. Holabird, A. A. Kiselev, I. Alvarado-Rodriguez, R. S. Ross, A. E. Schmitz, M. Sokolich, C. A. Watson, M. F. Gyure, and A. T. Hunter, Coherent singlet-triplet oscillations in a silicon-based
double quantum dot,Nature481, 344 (2012).
- Rigetti and Devoret [2010]C. Rigetti and M. Devoret, Fully microwave-tunable
universal gates in superconducting qubits with linear couplings and fixed
transition frequencies,Phys. Rev. B81, 134507 (2010).
- Mehlet al.[2014]S. Mehl, H. Bluhm, and D. P. DiVincenzo, Two-qubit couplings of singlet-triplet
qubits mediated by one quantum state,Phys. Rev. B90, 45404 (2014).
- Spethmannet al.[2024]M. Spethmann, S. Bosco,
A. Hofmann, J. Klinovaja, and D. Loss, High-fidelity two-qubit gates of hybrid
superconducting-semiconducting singlet-triplet qubits,Phys. Rev. B109, 85303 (2024).
- Hoffmanet al.[2016]S. Hoffman, C. Schrade,
J. Klinovaja, and D. Loss, Universal quantum computation with hybrid
spin-majorana qubits,Phys. Rev. B94, 45316 (2016).
- Mølmer and Sørensen [1999]K. Mølmer and A. Sørensen, Multiparticle
entanglement of hot trapped ions,Phys. Rev. Lett.82, 1835 (1999).
- Allcocket al.[2021]D. T. C. Allcock, W. C. Campbell, J. Chiaverini, I. L. Chuang, E. R. Hudson,
I. D. Moore, A. Ransford, C. Roman, J. M. Sage, and D. J. Wineland, Omg blueprint for trapped ion quantum computing with metastable states,Appl. Phys. Lett.119, 214002 (2021).
- Kielpinskiet al.[2001]D. Kielpinski, V. Meyer,
M. A. Rowe, C. A. Sackett, W. M. Itano, C. Monroe, and D. J. Wineland, A decoherence-free quantum memory using trapped ions,Science291, 1013 (2001).
- Jakschet al.[2000]D. Jaksch, J. I. Cirac,
P. Zoller, S. L. Rolston, R. Côté, and M. D. Lukin, Fast quantum gates for neutral atoms,Phys. Rev. Lett.85, 2208 (2000).
- Saffmanet al.[2010]M. Saffman, T. G. Walker, and K. Mølmer, Quantum information
with rydberg atoms,Rev. Mod. Phys.82, 2313 (2010).
- Chenet al.[2022]N. Chen, L. Li, W. Huie, M. Zhao, I. Vetter, C. H. Greene, and J. P. Covey, Analyzing the
Rydberg-based optical-metastable-ground architecture for
$^{171}\mathrm{Yb}$ nuclear spins,Phys. Rev. A105, 052438 (2022).
- Liset al.[2023]J. W. Lis, A. Senoo, W. F. McGrew, F. Rönchen, A. Jenkins, and A. M. Kaufman, Midcircuit operations using the omg architecture in
neutral atom arrays,Phys. Rev. X13, 041035 (2023).
- Cianiet al.[2022]A. Ciani, B. M. Varbanov,
N. Jolly, C. K. Andersen, and B. M. Terhal, Microwave-activated gates between a fluxonium and a
transmon qubit,Phys. Rev. Research4, 043127 (2022).
- Mirrahimiet al.[2014]M. Mirrahimi, Z. Leghtas,
V. V. Albert, S. Touzard, R. J. Schoelkopf, L. Jiang, and M. H. Devoret, Dynamically protected cat-qubits: A new paradigm for
universal quantum computation,New J. Phys.16, 045014 (2014).
- Gottesmanet al.[2001]D. Gottesman, A. Kitaev, and J. Preskill, Encoding a qubit in an oscillator,Phys. Rev. A64, 012310 (2001).

## 


- 


Major funding support from
