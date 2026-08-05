# Permutationally Invariant Quantum State Tomography for Fermions

**arXiv ID**: 2607.23579v1
**Authors**: Shion Yamashika, Daisuke Yamamoto
**Published**: 2026-07-26
**Categories**: cond-mat.quant-gas, cond-mat.stat-mech, quant-ph
**Comments**: 7+4 pages, 2 figures
**HTML URL**: https://arxiv.org/html/2607.23579v1

## Abstract

Quantum state tomography provides complete information about a quantum state, but its measurement cost generally grows exponentially with system size. In many-particle quantum simulators, this challenge is further compounded by the limited accessibility of local measurements and controls. Here we develop a tomography protocol for permutation-invariant fermionic many-body states with U(1) particle-number symmetry. We show that any such state is completely determined by the distribution of the total particle number and the occupation of a single collective mode within each particle-number sector, both of which are accessible in current ultracold-atom experiments. The number of required observables scales only linearly with the system size. More generally, the protocol reconstructs the permutation-symmetrized component of arbitrary U(1)-symmetric fermionic states, which can still encode nontrivial many-body and state-level structure beyond conventional few-body observables. We demonstrate this protocol in interacting non-Gaussian states of the complex Sachdev-Ye-Kitaev model and in free-fermion chains across a Lifshitz transition. This framework opens a route toward information-theoretic characterization of strongly correlated itinerant quantum matter in experimentally realistic fermionic quantum simulators.

## Full Text

Permutationally Invariant Quantum State Tomography for Fermions

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.23579v1 [cond-mat.quant-gas] 26 Jul 2026

## Permutationally Invariant Quantum State Tomography for FermionsShion YamashikaDepartment of Engineering Science, University of Electro-Communications, Chofu, Tokyo 182-8585, JapanDaisuke YamamotoDepartment of Physics, College of Humanities and Sciences, Nihon University, Sakurajosui, Setagaya, Tokyo 156-8550, JapanRIKEN Center for Quantum Computing (RQC), Wako, Saitama 351-0198, JapanGlobal R&D Center for Business by Quantum-AI Technology (G-QuAT),
National Institute of Advanced Industrial Science and Technology (AIST),
Tsukuba, Ibaraki 305-8568, Japan

## Abstract

Quantum state tomography provides complete information about a quantum state, but its measurement cost generally grows exponentially with system size. In many-particle quantum simulators, this challenge is further compounded by the limited accessibility of local measurements and controls. Here we develop a tomography protocol for permutation-invariant fermionic many-body states with U(1) particle-number symmetry. We show that any such state is completely determined by the distribution of the total particle number and the occupation of a single collective mode within each particle-number sector, both of which are accessible in current ultracold-atom experiments. The number of required observables scales only linearly with the system size. More generally, the protocol reconstructs the permutation-symmetrized component of arbitrary U(1)-symmetric fermionic states, which can still encode nontrivial many-body and state-level structure beyond conventional few-body observables. We demonstrate this protocol in interacting non-Gaussian states of the complex Sachdev-Ye-Kitaev model and in free-fermion chains across a Lifshitz transition. This framework opens a route toward information-theoretic characterization of strongly correlated itinerant quantum matter in experimentally realistic fermionic quantum simulators.

Introduction.—Quantum simulators have transformed the study of quantum many-body physics by realizing controllable interacting systems beyond the reach of classical computation or effective theories. This development has proceeded along two complementary directions. One direction is programmable qubit platforms, such as superconducting processors[9,13,25,57,8]and trapped ions[29,35,5,50,42,17], which offer flexible local control and measurements, making them powerful platforms for controlled many-body dynamics and quantum-information processing. The other is many-particle quantum simulators, especially ultracold atoms in optical lattices[6,7,38,58,20,21,49], which directly realize strongly correlated itinerant quantum matter, a central theme of
condensed-matter physics, under microscopic Hamiltonian control.

Understanding the many-body phenomena produced in these simulators requires characterizing the underlying quantum states and correlations. In principle, quantum state tomography provides a complete characterization[54,36,56], since it reconstructs the density matrix and thereby enables the evaluation of arbitrary observables as well as state-level diagnostics such as entanglement entropy. In practice, however, full tomography rapidly becomes infeasible because its measurement cost grows exponentially with system size[44,11,14,3].

For qubit systems, substantial progress has been made in mitigating this difficulty. Compressed-sensing tomography and related methods exploit additional assumptions on the state, such as low rank or specific spatial structure[22,23,51,31,34,40,41]. Symmetry-adapted protocols provide another route, as exemplified by permutationally invariant quantum tomography (PIQT)[52,43,19], which reconstructs permutation-invariant many-qubit states from only polynomially many collective measurements. More recently, randomized measurements and classical shadows have emerged as a complementary approach, allowing many observables and state diagnostics to be estimated without reconstructing the full density matrix[2,26,15].

The situation is more restrictive for many-particle quantum simulators. While these platforms have enabled the observation of a wide variety of many-body phenomena[6,7,38,58,20,21,49]through measurements of conventional observables such as density profiles, correlation functions, and momentum distributions, access to state-level information remains much more limited. Unlike programmable qubit platforms, they generally do not allow arbitrary local-basis rotations and measurements, preventing the direct implementation of many characterization protocols developed for qubit systems. Recent advances, including measurements of Rényi entanglement entropies in bosonic systems[27,32], demonstrate growing access to quantum-information properties in many-particle systems, yet scalable state characterization remains a major challenge.

In this Letter, we establish a PIQT protocol for itinerant fermionic systems with U(1) particle-number symmetry. Our main result is that the permutation-symmetrized density matrix of any U(1)-symmetric fermionic state is fully reconstructed from only two sets of observables scaling linearly with system size: the total particle-number distribution and the occupation of a single collective mode within each particle-number sector. These quantities are directly accessible through band-mapping measurements[6,7,38,58,20,21,49]in ultracold-atom experiments. When the original state is invariant under permutations, the protocol yields a complete reconstruction of the original density matrix. More generally, for states without permutation symmetry, it reconstructs the corresponding permutation-symmetrized density matrix, which can still retain nontrivial state-level structure and correlations beyond conventional observables. After deriving the reconstruction formula, we discuss its utility as a scalable tomography protocol and then demonstrate its broader applicability in interacting non-Gaussian states of the complex Sachdev-Ye-Kitaev (SYK) model and in free-fermion chains across a Lifshitz transition.

Preliminaries.—We consider a system ofNNfermionic modes. Here, a mode denotes a single-particle mode in a chosen basis; it may correspond to a lattice site, an internal state, or another mode label. We denote the annihilation and creation operators in theii-th mode bycic_{i}andci†c_{i}^{\dagger}, respectively. Throughout this work, we focus on a stateρ\rhowith the U(1) symmetry generated by the total particle number operatorQ=∑i=1Nci†​ciQ=\sum_{i=1}^{N}c_{i}^{\dagger}c_{i}. This assumption is natural for fermionic quantum simulators with cold atoms, where the total particle number is conserved to an excellent approximation and measurements are usually performed in a fixed or resolved particle-number sector[6,7,38,58,20,21,49]. The U(1) symmetry forbids coherences between different particle-number sectors and hence the density matrix can be written asρ=⨁q=0Npq​ρq.\displaystyle\rho=\bigoplus_{q=0}^{N}p_{q}\rho_{q}.(1)

Here,pq=Tr⁡[Pq​ρ]p_{q}=\Tr[P_{q}\rho]is the probability of findingqqparticles,PqP_{q}is the projector onto theqq-particle sector, andρq=Pq​ρ​Pq/pq\rho_{q}=P_{q}\rho P_{q}/p_{q}is the normalized density matrix in that sector.

Such a fermionic state is specified by the expectation values of many-body correlation functions such asci†​cj†​ck​clc_{i}^{\dagger}c_{j}^{\dagger}c_{k}c_{l}, and their higher-order generalizations, whose number grows exponentially with system size. Full reconstruction of the density matrix would therefore require measuring a complete set of high-order fermionic correlations, which is generally unavailable in many-particle platforms such as ultracold atoms.

Rather than attempting such a full reconstruction, we target the permutation-symmetrized version of the original density matrix defined as follows. Let𝒮N\mathcal{S}_{N}denote the permutation group ofNNmodes. For a permutationπ∈𝒮N\pi\in\mathcal{S}_{N}, we define the corresponding unitary operatorUπU_{\pi}byUπ​ci​Uπ†=cπ​(i).\displaystyle U_{\pi}c_{i}U_{\pi}^{\dagger}=c_{\pi(i)}.(2)

The permutation-symmetrized density matrix is then defined asΠ​(ρ)=1N!​∑π∈𝒮NUπ​ρ​Uπ†.\displaystyle\Pi(\rho)=\frac{1}{N!}\sum_{\pi\in\mathcal{S}_{N}}U_{\pi}\rho U_{\pi}^{\dagger}.(3)

This operation preserves positivity,Π​(ρ)≥0\Pi(\rho)\geq 0, and traceTr⁡Π​(ρ)=1\Tr\Pi(\rho)=1, and henceΠ​(ρ)\Pi(\rho)is again a density matrix. By construction,Π​(ρ)\Pi(\rho)is invariant under all permutations, i.e.,Uπ​Π​(ρ)​Uπ†=Π​(ρ)U_{\pi}\Pi(\rho)U_{\pi}^{\dagger}=\Pi(\rho)for everyπ∈𝒮N\pi\in\mathcal{S}_{N}.Figure 1:Few-sample construction of a permutation-invariant disorder-averaged state in the complex SYK model.
(a,b) Conditional uniform-mode occupationνq\nu_{q}and particle-number distributionpqp_{q}atβ=10\beta=10, estimated fromNsN_{\rm s}disorder realizations. These two quantities are the only inputs inserted into Eq. (4) to constructΠ​(ρ¯Ns​(β))\Pi(\bar{\rho}_{N_{\rm s}}(\beta)).
(c) Uhlmann fidelity betweenΠ​(ρ¯Ns​(β))\Pi(\bar{\rho}_{N_{\rm s}}(\beta))and a large-sample reference forρ¯​(β)\bar{\rho}(\beta)obtained from10410^{4}disorder realizations.
We setN=8N=8in all panels.

Fermionic PIQT.—The central result of this work is that the permutation-symmetrized density matrix in Eq. (3) can be written asΠ​(ρ)=⨁q=0Npq​(1−νq(N−1q)​Pq,0+νq(N−1q−1)​Pq,1).\displaystyle\Pi(\rho)=\bigoplus_{q=0}^{N}p_{q}\quantity(\frac{1-\nu_{q}}{\binom{N-1}{q}}P_{q,0}+\frac{\nu_{q}}{\binom{N-1}{q-1}}P_{q,1}).(4)

Here,νq=Tr⁡[ρq​n0]\nu_{q}=\Tr[\rho_{q}n_{0}]is the conditional occupation of the uniform mode in theqq-particle sector, wheren0=d0†​d0n_{0}=d_{0}^{\dagger}d_{0}anddk=N−1/2​∑i=1Ne−i​k​i​cid_{k}=N^{-1/2}\sum_{i=1}^{N}e^{-{\rm i}ki}c_{i}.Pq,0=Pq​(1−n0)P_{q,0}=P_{q}(1-n_{0})andPq,1=Pq​n0P_{q,1}=P_{q}n_{0}are the projection operators onto the subspaces of theqq-particle sector in which the uniform mode is empty and occupied, respectively. Terms associated with zero-dimensional subspaces are omitted: onlyP0,0P_{0,0}contributes forq=0q=0, and onlyPN,1P_{N,1}contributes forq=Nq=N. Equation (4) is not restricted to Gaussian states; it holds for any density matrix with U(1) particle-number symmetry, including interacting non-Gaussian states.

Proof of Eq. (4).—Because the permutations conserve the total particle number, permutation symmetrizationΠ​(⋅)\Pi(\cdot)acts independently in eachqq-particle sector of the density matrix (1). Letℋq\mathcal{H}_{q}be theqq-particle Hilbert space and letΠq\Pi_{q}denote permutation symmetrization restricted toℋq\mathcal{H}_{q}. Equation (1) then givesΠ​(ρ)=⨁q=0Npq​Πq​(ρq).\displaystyle\Pi(\rho)=\bigoplus_{q=0}^{N}p_{q}\Pi_{q}(\rho_{q}).(5)

The proof of Eq. (4) thus reduces to determiningΠq​(ρq)\Pi_{q}(\rho_{q})for a fixedqq. The sectorsq=0q=0andq=Nq=Nare one-dimensional and satisfy Eq. (4) immediately, and we therefore restrict the following argument to1≤q≤N−11\leq q\leq N-1.

Permutations conserve not only the total particle number but also the uniform-mode occupationn0n_{0}. This fact allows us to decompose the representation of𝒮N\mathcal{S}_{N}onℋq\mathcal{H}_{q}into the two subspacesVq,n=Pq,n​ℋqV_{q,n}=P_{q,n}\mathcal{H}_{q}withn=0,1n=0,1.
More specifically, if we rewrite the one-particle Hilbert space asℋ1=span​{d0†​|0⟩}⊕W,\displaystyle\mathcal{H}_{1}=\mathrm{span}\{d_{0}^{\dagger}\ket{0}\}\oplus W,(6)

whereW=span​{dk†​|0⟩|k≠0}W=\mathrm{span}\{d_{k}^{\dagger}\ket{0}\,|k\neq 0\}is the subspace orthogonal to the uniform mode, we obtainℋq=Vq,0⊕Vq,1,\displaystyle\mathcal{H}_{q}=V_{q,0}\oplus V_{q,1},(7)

withVq,0=∧qW,Vq,1=span{d0†|0⟩}∧∧q−1W.\displaystyle V_{q,0}=\wedge^{q}W,~V_{q,1}=\mathrm{span}\{d_{0}^{\dagger}\ket{0}\}\wedge\wedge^{q-1}W.(8)

Here,∧q\wedge^{q}denotes theqqth exterior power. Since every permutation acts trivially onspan​{d0†​|0⟩}\mathrm{span}\{d_{0}^{\dagger}\ket{0}\},Vq,nV_{q,n}in Eq. (7) carries the representation∧q−nW\wedge^{q-n}W(n=0,1n=0,1). These two representations are irreducible[18]and mutually inequivalent, as shown in the End Matter.

Applying the decomposition (7) to the density matrixρq\rho_{q}and taking the permutation symmetrization, we obtainΠq​(ρq)=∑n,m=01Xq,n​m,\displaystyle\Pi_{q}(\rho_{q})=\sum_{n,m=0}^{1}X_{q,nm},(9)

whereXq,n​m=Πq​(Pq,n​ρq​Pq,m)X_{q,nm}=\Pi_{q}\quantity(P_{q,n}\rho_{q}P_{q,m}).
By definition,Xq,n​mX_{q,nm}is invariant under every permutation, implying thatUπ,q,n​Xq,n​m=Xq,n​m​Uπ,q,m∀π∈𝒮N,\displaystyle U_{\pi,q,n}X_{q,nm}=X_{q,nm}U_{\pi,q,m}\qquad\forall\pi\in\mathcal{S}_{N},(10)

whereUπ,q,nU_{\pi,q,n}is the restriction ofUπU_{\pi}to the subspaceVq,nV_{q,n}.
Forn≠mn\neq m,Xq,n​mX_{q,nm}in Eq. (10) is an intertwiner between inequivalent irreducible representations∧qW\wedge^{q}Wand∧q−1W\wedge^{q-1}W. Schur’s lemma then givesXq,n​m=0X_{q,nm}=0. Forn=mn=m,Xq,n​nX_{q,nn}commutes with an irreducible representation, and hence Schur’s lemma givesXq,n​n=αq,n​Pq,nX_{q,nn}=\alpha_{q,n}P_{q,n}, whereαq,n\alpha_{q,n}are constants. Equation (9) therefore reduces toΠq​(ρq)=αq,0​Pq,0+αq,1​Pq,1.\displaystyle\Pi_{q}(\rho_{q})=\alpha_{q,0}P_{q,0}+\alpha_{q,1}P_{q,1}.(11)

The specific forms of the coefficientsαq,n\alpha_{q,n}can be derived from the conditionsTr⁡[Πq​(ρq)]=1\Tr[\Pi_{q}(\rho_{q})]=1andTr⁡[Πq​(ρq)​n0]=νq\Tr[\Pi_{q}(\rho_{q})n_{0}]=\nu_{q}asαq,0=1−νq(N−1q),αq,1=νq(N−1q−1).\displaystyle\alpha_{q,0}=\frac{1-\nu_{q}}{\matrixquantity(N-1\\
q)},\qquad\alpha_{q,1}=\frac{\nu_{q}}{\matrixquantity(N-1\\
q-1)}.(12)

Multiplying by the sector probabilitypqp_{q}and summing overqqgives Eq. (4).

Applications.—Equation (4) has two immediate uses. First, if the original state is permutationally invariant, it gives a scalable tomography protocol: Forρ=Π​(ρ)\rho=\Pi(\rho), the density matrix can be reconstructed from the input data{pq,νq}q=0N\{p_{q},\nu_{q}\}_{q=0}^{N}, whose number grows only linearly withNN.
Second, Eq. (4) gives expectation values of permutation-invariant observables even when the original state is not permutation invariant: Wheneverρ\rhorespects the U(1) particle-number symmetry,Π​(ρ)\Pi(\rho)can always be reconstructed from Eq. (4). For any observableOOsatisfyingΠ​(O)=O\Pi(O)=O, one then obtainsTr⁡[ρ​O]=Tr⁡[ρ​Π​(O)]=Tr⁡[Π​(ρ)​O]\Tr[\rho O]=\Tr[\rho\Pi(O)]=\Tr[\Pi(\rho)O].

We now illustrate the broader utility of Eq. (4) in two physically distinct settings.

Example 1: Complex SYK model.—We first consider the complex SYK model[48,24]HJ=∑i<j,k<lJi​j,k​l​ci†​cj†​ck​cl,\displaystyle H_{J}=\sum_{i<j,k<l}J_{ij,kl}c_{i}^{\dagger}c_{j}^{\dagger}c_{k}c_{l},(13)

where the couplingsJi​j,k​lJ_{ij,kl}are complex Gaussian variables with zero mean and varianceN−3N^{-3}and satisfyJi​j,k​l=−Jj​i,k​l=−Ji​j,l​k=Jk​l,i​j∗J_{ij,kl}=-J_{ji,kl}=-J_{ij,lk}=J_{kl,ij}^{*}.
Cold-atom realizations of this model and closely related variants have been proposed[12,55,10].
We aim to reconstruct the disorder-averaged Gibbs stateρ¯​(β)=𝔼J​[ρJ​(β)],\displaystyle\bar{\rho}(\beta)=\mathbb{E}_{J}[\rho_{J}(\beta)],(14)

whereρJ​(β)=e−β​HJ/Tr⁡(e−β​HJ)\rho_{J}(\beta)=e^{-\beta H_{J}}/\Tr(e^{-\beta H_{J}})is the Gibbs state for a realizationJJat the inverse temperatureβ\beta.
Since the coupling distribution is invariant under permutations of the mode labels,ρ¯​(β)\bar{\rho}(\beta)is permutation invariant:Π​(ρ¯​(β))=ρ¯​(β)\Pi(\bar{\rho}(\beta))=\bar{\rho}(\beta).
The difficulty in constructingρ¯​(β)\bar{\rho}(\beta)is that it requires averaging over infinitely many disorder realizations, which is impractical in both numerical calculations and experiments.

Figure1shows that Eq. (4) allows us to circumvent this difficulty. Here, we estimateνq\nu_{q}andpqp_{q}fromNsN_{\rm s}realizations, as shown in Figs.1(a) and1(b). We then insert them into Eq. (4) to constructΠ​(ρ¯Ns​(β))\Pi(\bar{\rho}_{N_{\rm s}}(\beta)), whereρ¯Ns​(β)=Ns−1​∑a=1NsρJa​(β)\bar{\rho}_{N_{\rm s}}(\beta)=N_{\rm s}^{-1}\sum_{a=1}^{N_{\rm s}}\rho_{J_{a}}(\beta)is the finite-sample averaged state. Figure1(c) plots the Uhlmann fidelityF​(ρ,σ)=Tr⁡ρ​σ​ρF(\rho,\sigma)=\Tr\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}[53,30]betweenΠ​(ρ¯Ns​(β))\Pi(\bar{\rho}_{N_{\rm s}}(\beta))andρ¯​(β)\bar{\rho}(\beta)as a function ofβ\beta. The fidelity remains close to unity even with only a few tens of realizations, showing that the finite-sample construction approximates wellρ¯​(β)\bar{\rho}(\beta).

The effectiveness of this construction comes from the additional averaging introduced by permutation symmetrization, which givesΠ​(ρ¯Ns​(β))=1Ns​N!​∑a=1Ns∑π∈𝒮NUπ​ρJa​(β)​Uπ†.\displaystyle\Pi(\bar{\rho}_{N_{\rm s}}(\beta))=\frac{1}{N_{\rm s}N!}\sum_{a=1}^{N_{\rm s}}\sum_{\pi\in\mathcal{S}_{N}}U_{\pi}\rho_{J_{a}}(\beta)U_{\pi}^{\dagger}.(15)

Each stateUπ​ρJa​(β)​Uπ†U_{\pi}\rho_{J_{a}}(\beta)U_{\pi}^{\dagger}in the above equation is the Gibbs state obtained by applying the same permutation to the coupling labels. Equation (15) therefore shows that the reconstructed state incorporates the entire permutation orbit of every sampled realization without explicitly sampling additional disorder realizations, effectively increasing the number of samples fromNsN_{\rm s}toNs​N!N_{\rm s}N!. In addition, the reconstructed state respects the permutation symmetry ofρ¯​(β)\bar{\rho}(\beta), thereby removing the permutation-noninvariant component of the finite-sample error. These facts explain the high fidelity obtained from only a few realizations.

Example 2: Lifshitz transition.—We next consider a Lifshitz transition in a one-dimensional free-fermion ground state corresponding to the Fermi sea|Ψ⟩=∏k:εk<0dk†​|0⟩.\displaystyle\ket{\Psi}=\prod_{k:\varepsilon_{k}<0}d_{k}^{\dagger}\ket{0}.(16)

Hereεk\varepsilon_{k}is the single-particle dispersion. A Lifshitz transition occurs when varyingεk\varepsilon_{k}changes the topology of the occupied momentum region[39,4].
It is known that, for an intervalAAofNAN_{A}sites, the ground-state entanglement entropyS​(ρA)=−TrA⁡ρA​log⁡ρAS(\rho_{A})=-\Tr_{A}\rho_{A}\log\rho_{A}of the reduced stateρA=TrA¯⁡|Ψ⟩⟨Ψ|\rho_{A}=\Tr_{\bar{A}}\outerproduct{\Psi}{\Psi}exhibits a nonanalyticity at a Lifshitz transition[47,45]. We ask whether this signature survives permutation symmetrization.

SinceρA\rho_{A}has U(1) symmetry,ΠA​(ρA)\Pi_{A}(\rho_{A})can be obtained by Eq. (4), whereΠA\Pi_{A}stands for the permutation symmetrization with respect to the sites inside subsystemAA. As derived in the Supplemental Material (SM)[1], its von Neumann entropy can be calculated asS​(ΠA​(ρA))=NA​h​(ϱ)−12​ln⁡NA+O​(ln⁡ln⁡NA),\displaystyle S(\Pi_{A}(\rho_{A}))=N_{A}h(\varrho)-\frac{1}{2}\ln N_{A}+O(\ln\ln N_{A}),(17)

whereϱ=∑kΘ​(−εk)/N\varrho=\sum_{k}\Theta(-\varepsilon_{k})/Nandh​(ϱ)=−ϱ​ln⁡ϱ−(1−ϱ)​ln⁡(1−ϱ)h(\varrho)=-\varrho\ln\varrho-(1-\varrho)\ln(1-\varrho). At a Lifshitz transition point, a Fermi pocket appears or disappears, causing the fractionϱ\varrhoof occupied modes to change nonanalytically. The functionh​(ϱ)h(\varrho)inherits this nonanalyticity. Equation (17) therefore predicts a nonanalyticity inS​(ΠA​(ρA))S(\Pi_{A}(\rho_{A}))at the transition point.Figure 2:(a) The energy dispersion relation of the Hamiltonian (18) withJ2/J1=1.5J_{2}/J_{1}=1.5. The empty and occupied modes are plotted by dotted and solid lines, respectively.
(b) von Neumann entropy of the permutation-symmetrized reduced density matrix for the ground state of the Hamiltonian (18). The symbols and solid lines are the exact numerical results and the asymptotic prediction in Eq. (17), respectively. We useNA=27N_{A}=2^{7}andN=214N=2^{14}.

We now illustrate this prediction with the nearest- and next-nearest-neighbor hopping modelH=−12∑i[J1ci†ci+1+J2ci†ci+2+H.c.]−μ∑ici†ci,\displaystyle H=-\frac{1}{2}\sum_{i}[J_{1}c_{i}^{\dagger}c_{i+1}+J_{2}c_{i}^{\dagger}c_{i+2}+\mathrm{H.c.}]-\mu\sum_{i}c_{i}^{\dagger}c_{i},(18)

where the single-particle dispersion relation is given byεk=−J1​cos⁡k−J2​cos⁡2​k−μ.\displaystyle\varepsilon_{k}=-J_{1}\cos k-J_{2}\cos 2k-\mu.(19)

ForJ2>J1/4J_{2}>J_{1}/4, the local minimum atk=πk=\picrosses the Fermi level atμc=J1−J2\mu_{\rm c}=J_{1}-J_{2}, creating a Fermi pocket forμ>μc\mu>\mu_{\rm c}[see Fig.2(a)]. As shown in Fig.2(b),S​(ΠA​(ρA))S(\Pi_{A}(\rho_{A}))indeed exhibits the predicted nonanalyticity at the transition point.

Experimental Implementation.—As mentioned before, the fermionic PIQT protocol based on Eq. (4) requires only two types of data in each experimental shot: the total particle number and the occupation of the uniform mode. For fermions in an optical lattice, the latter corresponds to the zero-momentum mode. Repeated band-mapping measurements therefore give both quantities simultaneously[6,7,38,58,20,21,49]: the histogram of the measured total particle number givespqp_{q}, while the conditional average of the zero-momentum occupation among shots with total particle numberqqgivesνq\nu_{q}. Once these quantities are obtained for allqq, the permutation-symmetrized density matrix is reconstructed directly from Eq. (4).
Thus, the fermionic PIQT protocol does not require local basis rotations, site-by-site control, or measurements of a complete set of high-order fermionic correlations. It relies only on number- and momentum-resolved data, making it well matched to ultracold-atom fermionic simulators.

Conclusions.—We have shown that the permutation-symmetrized density matrix of a U(1)-symmetric fermionic many-body state is generally determined by particle-number statistics and one uniform-mode occupation in each particle-number sector. This gives a fermionic version of PIQT protocol in which the quantities to be measured scale linearly with system size and are accessible in ultracold-atom experiments. The formula applies beyond Gaussian states, as illustrated by the disorder-averaged Gibbs state of the complex SYK model, and it can also extract transition signatures from states that are not permutation invariant, as shown for spatial subsystems of free-fermion chains across Lifshitz transitions. These results establish fermionic PIQT as an efficient route to information-theoretic characterization of many-body fermionic states without full density-matrix reconstruction.

Looking ahead, it will be important to extend the present framework beyond U(1)-symmetric fermionic states and to bosonic systems. Such extensions would broaden the range of quantum simulators to which PIQT can be applied. Another important direction is to clarify what kinds of quantum information are retained in the permutation-symmetrized density matrix. Understanding how this reconstructed state reflects strong correlations, topology, and other organizing principles of quantum matter would help turn the present protocol into a powerful diagnostic for many-particle quantum simulators.

Acknowledgments—We thank T. Fukuhara and H. Katsura for fruitful discussions.
This work was supported by JSPS KAKENHI Grant Numbers JP25K23355 (SY), JP26K17050 (SY), JP23K25830 (DY), JP24K06890 (DY), and JP26K00664 (DY), and JST PRESTO Grant Number JPMJPR245D (DY). SY acknowledges support from the University of Electro-Communications.

## References
- [1]Note:See Supplemental Material for details of numerical and analytical calculations, which includes Refs.[28,33,16,37,46].Cited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [2]S. Aaronson(2018)Shadow tomography of quantum states.InProceedings of the 50th Annual ACM SIGACT Symposium on Theory of Computing,STOC 2018,New York, NY, USA,pp. 325–338.External Links:ISBN 9781450355599,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [3]J. Amiet and S. Weigert(1999-01)Reconstructing a pure state of a spinsthrough three Stern-Gerlach measurements.Journal of Physics A: Mathematical and General32(15),pp. 2777–2784.External Links:ISSN 1361-6447,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [4]Ya.M. Blanter, M.I. Kaganov, A.V. Pantsulaya, and A.A. Varlamov(1994-09)The theory of electronic topological transitions.Physics Reports245(4),pp. 159.External Links:ISSN 0370-1573,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [5]R. Blatt and C. F. Roos(2012-04)Quantum simulations with trapped ions.Nature Physics8(4),pp. 277–284.External Links:ISSN 1745-2481,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [6]I. Bloch(2005-10)Ultracold quantum gases in optical lattices.Nature Physics1(1),pp. 23–30.External Links:ISSN 1745-2481,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions.
- [7]I. Bloch(2008-06)Quantum coherence and entanglement with ultracold atoms in optical lattices.Nature453(7198),pp. 1016–1022.External Links:ISSN 1476-4687,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions.
- [8]S. Bravyi, O. Dial, J. M. Gambetta, D. Gil, and Z. Nazario(2022-10)The future of quantum computing with superconducting qubits.Journal of Applied Physics132(16).External Links:ISSN 1089-7550,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [9]J. Clarke and F. K. Wilhelm(2008-06)Superconducting quantum bits.Nature453(7198),pp. 1031–1042.External Links:ISSN 1476-4687,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [10]C. Creffield, F. Sols, M. Schirò, and N. Goldman(2026-07)Sachdev-Ye-Kitaev Physics from the Hubbard Model: A Floquet-Engineering Approach.Phys. Rev. Lett.137,pp. 046302.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [11]G. M. D Ariano, L. Maccone, and M. Paini(2003-01)Spin tomography.Journal of Optics B: Quantum and Semiclassical Optics5(1),pp. 77–84.External Links:ISSN 1464-4266,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [12]I. Danshita, M. Hanada, and M. Tezuka(2017-07)Creating and probing the Sachdev-Ye-Kitaev model with ultracold gases: Towards experimental studies of quantum gravity.Progress of Theoretical and Experimental Physics2017(8).External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [13]L. DiCarlo, J. M. Chow, J. M. Gambetta, L. S. Bishop, B. R. Johnson, D. I. Schuster, J. Majer, A. Blais, L. Frunzio, S. M. Girvin, and R. J. Schoelkopf(2009-06)Demonstration of two-qubit algorithms with a superconducting quantum processor.Nature460(7252),pp. 240–244.External Links:ISSN 1476-4687,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [14]V.V. Dodonov and V.I. Man’ko(1997-06)Positive distribution description for spin states.Physics Letters A229(6),pp. 335–339.External Links:ISSN 0375-9601,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [15]A. Elben, S. T. Flammia, H. Huang, R. Kueng, J. Preskill, B. Vermersch, and P. Zoller(2022-12)The randomized measurement toolbox.Nature Reviews Physics5(1),pp. 9–24.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [16]M. E. Fisher and R. E. Hartwig(1969)Toeplitz Determinants: Some Applications, Theorems, and Conjectures.InAdvances in Chemical Physics,pp. 333.External Links:ISBN 9780470143605,Document,LinkCited by:§I,1.
- [17]M. Foss-Feig, G. Pagano, A. C. Potter, and N. Y. Yao(2025-03)Progress in Trapped-Ion Quantum Simulation.Annual Review of Condensed Matter Physics16(1),pp. 145–172.External Links:ISSN 1947-5462,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [18]W. Fulton and J. Harris(2004)Representation Theory.Springer New York.External Links:ISBN 9781461209799,ISSN 2197-5612,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [19]T. Gao, F. Yan, and S. J. van Enk(2014-05)Permutationally Invariant Part of a Density Matrix and Nonseparability ofNN-Qubit States.Phys. Rev. Lett.112,pp. 180501.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [20]N. Goldman, J. C. Budich, and P. Zoller(2016-06)Topological quantum matter with ultracold gases in optical lattices.Nature Physics12(7),pp. 639–645.External Links:ISSN 1745-2481,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions.
- [21]C. Gross and I. Bloch(2017-09)Quantum simulations with ultracold atoms in optical lattices.Science357(6355),pp. 995–1001.External Links:ISSN 1095-9203,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions.
- [22]D. Gross, Y. Liu, S. T. Flammia, S. Becker, and J. Eisert(2010-10)Quantum State Tomography via Compressed Sensing.Phys. Rev. Lett.105,pp. 150401.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [23]D. Gross(2011)Recovering Low-Rank Matrices From Few Coefficients in Any Basis.IEEE Transactions on Information Theory57(3),pp. 1548–1566.External Links:DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [24]Y. Gu, A. Kitaev, S. Sachdev, and G. Tarnopolsky(2020-02)Notes on the complex Sachdev-Ye-Kitaev model.Journal of High Energy Physics2020(2).External Links:ISSN 1029-8479,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [25]H. Huang, D. Wu, D. Fan, and X. Zhu(2020-07)Superconducting quantum computing: a review.Science China Information Sciences63(8).External Links:ISSN 1869-1919,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [26]H. Huang, R. Kueng, and J. Preskill(2020-06)Predicting many properties of a quantum system from very few measurements.Nature Physics16(10),pp. 1050–1057.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [27]R. Islam, R. Ma, P. M. Preiss, M. E. Tai, A. Lukin, M. Rispoli, and M. Greiner(2015-12)Measuring entanglement entropy in a quantum many-body system.Nature528(7580),pp. 77–83.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [28]D. A. Ivanov, A. G. Abanov, and V. V. Cheianov(2013-02)Counting free fermions on a line: a Fisher-Hartwig asymptotic expansion for the Toeplitz determinant in the double-scaling limit.Journal of Physics A: Mathematical and Theoretical46(8),pp. 085003.External Links:ISSN 1751-8121,Link,DocumentCited by:§I,1.
- [29]M. Johanning, A. F. Varón, and C. Wunderlich(2009-07)Quantum simulations with cold trapped ions.Journal of Physics B: Atomic, Molecular and Optical Physics42(15),pp. 154009.External Links:ISSN 1361-6455,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [30]R. Jozsa(1994-12)Fidelity for Mixed Quantum States.Journal of Modern Optics41(12),pp. 2315.External Links:ISSN 1362-3044,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [31]A. Kalev, R. L. Kosut, and I. H. Deutsch(2015-12)Quantum tomography protocols with positivity are compressed sensing protocols.npj Quantum Information1(1).External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [32]A. M. Kaufman, M. E. Tai, A. Lukin, M. Rispoli, R. Schittko, P. M. Preiss, and M. Greiner(2016-08)Quantum thermalization through entanglement in an isolated many-body system.Science353(6301),pp. 794–800.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [33]I. Klich(2002)Full Counting Statistics: An elementary derivation of Levitov’s formula.External Links:cond-mat/0209642Cited by:§I,1.
- [34]M. Krishnan Vijayan, A. Paler, J. Gavriel, C. R. Myers, P. P. Rohde, and S. J. Devitt(2024-02)Compilation of algorithm-specific graph states for quantum circuits.Quantum Science and Technology9(2),pp. 025005.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [35]B. P. Lanyon, C. Hempel, D. Nigg, M. Müller, R. Gerritsma, F. Zähringer, P. Schindler, J. T. Barreiro, M. Rambach, G. Kirchmair, M. Hennrich, P. Zoller, R. Blatt, and C. F. Roos(2011-10)Universal Digital Quantum Simulation with Trapped Ions.Science334(6052),pp. 57–61.External Links:ISSN 1095-9203,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [36]U. Leonhardt(1995-05)Quantum-State Tomography and Discrete Wigner Function.Phys. Rev. Lett.74,pp. 4101–4105.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [37]L. S. Levitov and G. B. Lesovik(1993)Charge distribution in quantum shot noise.JETP Letters58,pp. 230.External Links:LinkCited by:§I,1.
- [38]M. Lewenstein, A. Sanpera, and V. Ahufinger(2012-03)Ultracold Atoms in Optical Lattices: Simulating quantum many-body systems.Oxford University Press.External Links:ISBN 9780199573127,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions.
- [39]I. Lifshitz(1960)Anomalies of electron characteristics of a metal in the high pressure region.Sov. Phys. JETP11(5),pp. 1130.Cited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [40]Y. Liu(2011)Universal low-rank matrix recovery from Pauli measurements.InAdvances in Neural Information Processing Systems,J. Shawe-Taylor, R. Zemel, P. Bartlett, F. Pereira, and K. Weinberger (Eds.),Vol.24,pp..External Links:LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [41]G. Marmorini, T. Fukuhara, and D. Yamamoto(2026-03)Measuring Entanglement Without Local Addressing in Quantum Many-Body Simulators via Spiral Quantum State Tomography.PRX Quantum7,pp. 010355.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [42]C. Monroe and J. Kim(2013-03)Scaling the Ion Trap Quantum Processor.Science339(6124),pp. 1164–1169.External Links:ISSN 1095-9203,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [43]T. Moroder, P. Hyllus, G. Tóth, C. Schwemmer, A. Niggebaum, S. Gaile, O. Gühne, and H. Weinfurter(2012-10)Permutationally invariant state reconstruction.New Journal of Physics14(10),pp. 105001.External Links:ISSN 1367-2630,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [44]M. Paris and J. Řeháček(2004)Quantum State Estimation.Springer Berlin Heidelberg.External Links:ISBN 9783540444817,ISSN 1616-6361,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [45]I. Peschel and V. Eisler(2009-12)Reduced density matrices and entanglement entropy in free lattice models.Journal of Physics A: Mathematical and Theoretical42(50),pp. 504003.External Links:ISSN 1751-8121,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [46]I. Peschel(2003-03)Calculation of reduced density matrices from correlation functions.Journal of Physics A: Mathematical and General36(14),pp. L205.External Links:ISSN 1361-6447,Link,DocumentCited by:§II,1.
- [47]M. Rodney, H. F. Song, S. Lee, K. Le Hur, and E. S. Sørensen(2013-03)Scaling of entanglement entropy across Lifshitz transitions.Physical Review B87(11),pp. 115132.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [48]S. Sachdev(2015-11)Bekenstein-Hawking Entropy and Strange Metals.Phys. Rev. X5,pp. 041025.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [49]F. Schäfer, T. Fukuhara, S. Sugawa, Y. Takasu, and Y. Takahashi(2020-07)Tools for quantum simulation with ultracold atoms in optical lattices.Nature Reviews Physics2(8),pp. 411–425.External Links:ISSN 2522-5820,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions.
- [50]C. Schneider, D. Porras, and T. Schaetz(2012-01)Experimental quantum simulations of many-body physics with trapped ions.Reports on Progress in Physics75(2),pp. 024401.External Links:ISSN 1361-6633,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [51]C. Schwemmer, G. Tóth, A. Niggebaum, T. Moroder, D. Gross, O. Gühne, and H. Weinfurter(2014-07)Experimental Comparison of Efficient Tomography Schemes for a Six-Qubit State.Phys. Rev. Lett.113,pp. 040503.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [52]G. Tóth, W. Wieczorek, D. Gross, R. Krischek, C. Schwemmer, and H. Weinfurter(2010-12)Permutationally Invariant Quantum Tomography.Phys. Rev. Lett.105,pp. 250403.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [53]A. Uhlmann(2010-01)Transition Probability (Fidelity) and Its Relatives.Foundations of Physics41(3),pp. 288.External Links:ISSN 1572-9516,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [54]K. Vogel and H. Risken(1989-09)Determination of quasiprobability distributions in terms of probability distributions for the rotated quadrature phase.Phys. Rev. A40,pp. 2847(R)–2849(R).External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [55]C. Wei and T. A. Sedrakyan(2021-01)Optical lattice platform for the Sachdev-Ye-Kitaev model.Phys. Rev. A103,pp. 013323.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [56]A. G. White, D. F. V. James, P. H. Eberhard, and P. G. Kwiat(1999-10)Nonmaximally Entangled States: Production, Characterization, and Utilization.Phys. Rev. Lett.83,pp. 3103–3107.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [57]Y. Wu, W. Bao, S. Cao, F. Chen, M. Chen, X. Chen, T. Chung, H. Deng, Y. Du, D. Fan, M. Gong, C. Guo, C. Guo, S. Guo, L. Han, L. Hong, H. Huang, Y. Huo, L. Li, N. Li, S. Li, Y. Li, F. Liang, C. Lin, J. Lin, H. Qian, D. Qiao, H. Rong, H. Su, L. Sun, L. Wang, S. Wang, D. Wu, Y. Xu, K. Yan, W. Yang, Y. Yang, Y. Ye, J. Yin, C. Ying, J. Yu, C. Zha, C. Zhang, H. Zhang, K. Zhang, Y. Zhang, H. Zhao, Y. Zhao, L. Zhou, Q. Zhu, C. Lu, C. Peng, X. Zhu, and J. Pan(2021-10)Strong Quantum Computational Advantage Using a Superconducting Quantum Processor.Phys. Rev. Lett.127,pp. 180501.External Links:Document,LinkCited by:Permutationally Invariant Quantum State Tomography for Fermions.
- [58]E. Zohar, J. I. Cirac, and B. Reznik(2015-12)Quantum simulations of lattice gauge theories using ultracold atoms in optical lattices.Reports on Progress in Physics79(1),pp. 014401.External Links:ISSN 1361-6633,Link,DocumentCited by:Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions,Permutationally Invariant Quantum State Tomography for Fermions.

End Matter

Here we verify the claim that the two nonzero irreducible representations carried byVq,0V_{q,0}andVq,1V_{q,1}are inequivalent for1≤q≤N−11\leq q\leq N-1. As established in Eq. (7), these representations are∧qW\wedge^{q}Wand∧q−1W\wedge^{q-1}W, respectively. ForN≠2​qN\neq 2q, they are trivially inequivalent because their dimensionsdim∧q−nW=(N−1q−n),(n=0,1)\displaystyle\dim\wedge^{q-n}W=\matrixquantity(N-1\\
q-n),\quad(n=0,1)(20)

are different.

It remains to check the half-filled caseN=2​qN=2q, wheredim∧qW=dim∧q−1W\dim\wedge^{q}W=\dim\wedge^{q-1}W.
To this end, let us consider the transpositionτ∈𝒮N\tau\in\mathcal{S}_{N}such thatτ​(1)=2\tau(1)=2,τ​(2)=1\tau(2)=1, andτ​(i)=i\tau(i)=ifori=3,4,…,Ni=3,4,\ldots,N.
In the standard representationWW, this transposition has eigenvalue+1+1with multiplicityN−2N-2and eigenvalue−1-1with multiplicity11.
Therefore, on∧rW\wedge^{r}W, the character ofτ\taureadsTr∧rW⁡(τ)=(N−2r)−(N−2r−1).\displaystyle\Tr_{\wedge^{r}W}(\tau)=\binom{N-2}{r}-\binom{N-2}{r-1}.(21)

Indeed, the first term counts basis vectors of∧rW\wedge^{r}Wthat do not contain the−1-1eigenvector ofτ\tau, while the second term counts those that contain it.
If two representations are equivalent, their characters must agree for every group element.
AtN=2​qN=2q, however,Tr∧qW⁡(τ)=(2​q−2q)−(2​q−2q−1),\displaystyle\Tr_{\wedge^{q}W}(\tau)=\binom{2q-2}{q}-\binom{2q-2}{q-1},(22)Tr∧q−1W⁡(τ)=(2​q−2q−1)−(2​q−2q−2),\displaystyle\Tr_{\wedge^{q-1}W}(\tau)=\binom{2q-2}{q-1}-\binom{2q-2}{q-2},(23)

and these two numbers are different.
Thus∧qW\wedge^{q}Wand∧q−1W\wedge^{q-1}Ware inequivalent even whenN=2​qN=2q.

Supplemental Material

## 
- 
- 
- 

## IVon Neumann entropy of the permutation-symmetrized reduced density matrix for a Fermi sea

Here, we give the derivation of Eq. (17) in the main text.
We consider a one-dimensional free-fermion ground state|Ψ⟩=∏k:εk<0dk†​|Ω⟩.\displaystyle\ket{\Psi}=\prod_{k:\varepsilon_{k}<0}d_{k}^{\dagger}\ket{\Omega}.(sm-1)

We divide the whole system into subsystemAAconsisting ofNAN_{A}consecutive sites and the rest. The reduced density matrix for subsystemAAisρA=TrA¯⁡|Ψ⟩⟨Ψ|.\displaystyle\rho_{A}=\Tr_{\bar{A}}\outerproduct{\Psi}{\Psi}.(sm-2)

It has U(1) symmetry with respect to the subsystem particle-number operatorQA=∑i∈Aci†​ci.\displaystyle Q_{A}=\sum_{i\in A}c_{i}^{\dagger}c_{i}.(sm-3)

We denote bypqp_{q}the probability of findingqqparticles inAA,pq=Tr⁡(Pq​ρA),\displaystyle p_{q}=\Tr(P_{q}\rho_{A}),(sm-4)

wherePqP_{q}is the projector onto theqq-particle sector of the subsystem.

According to Eq. (4), the permutation-symmetrized reduced density matrix can be written asΠA​(ρA)=⨁q=0NApq​[1−νqDq,0​Pq,0+νqDq,1​Pq,1],\displaystyle\Pi_{A}(\rho_{A})=\bigoplus_{q=0}^{N_{A}}p_{q}\left[\frac{1-\nu_{q}}{D_{q,0}}P_{q,0}+\frac{\nu_{q}}{D_{q,1}}P_{q,1}\right],(sm-5)

whereDq,0=(NA−1q),Dq,1=(NA−1q−1).\displaystyle D_{q,0}=\binom{N_{A}-1}{q},\qquad D_{q,1}=\binom{N_{A}-1}{q-1}.(sm-6)

HerePq,0P_{q,0}andPq,1P_{q,1}project onto the subspaces withqqparticles and with the uniform orbital empty or occupied, respectively. The numberνq=Tr⁡(ρA,q​nA,0)\displaystyle\nu_{q}=\Tr(\rho_{A,q}n_{A,0})(sm-7)

is the occupation of the uniform orbital conditioned on theqq-particle sector, withnA,0=dA,0†​dA,0,dA,0=1NA​∑i∈Aci.\displaystyle n_{A,0}=d_{A,0}^{\dagger}d_{A,0},\qquad d_{A,0}=\frac{1}{\sqrt{N_{A}}}\sum_{i\in A}c_{i}.(sm-8)

The eigenvalues ofΠA​(ρA)\Pi_{A}(\rho_{A})are thereforeλq,0=pq​(1−νq)Dq,0,λq,1=pq​νqDq,1,\displaystyle\lambda_{q,0}=\frac{p_{q}(1-\nu_{q})}{D_{q,0}},\qquad\lambda_{q,1}=\frac{p_{q}\nu_{q}}{D_{q,1}},(sm-9)

with degeneraciesDq,0D_{q,0}andDq,1D_{q,1}, respectively. Hence, the von Neumann entropy ofΠA​(ρA)\Pi_{A}(\rho_{A})can be written asS​(ΠA​(ρA))=−∑q=0NApq​ln⁡pq+∑q=0NApq​[(1−νq)​ln⁡Dq,0+νq​ln⁡Dq,1]+∑q=0NApq​h​(νq),\displaystyle S(\Pi_{A}(\rho_{A}))=-\sum_{q=0}^{N_{A}}p_{q}\ln p_{q}+\sum_{q=0}^{N_{A}}p_{q}\left[(1-\nu_{q})\ln D_{q,0}+\nu_{q}\ln D_{q,1}\right]+\sum_{q=0}^{N_{A}}p_{q}h(\nu_{q}),(sm-10)

whereh​(ν)=−ν​ln⁡ν−(1−ν)​ln⁡(1−ν).\displaystyle h(\nu)=-\nu\ln\nu-(1-\nu)\ln(1-\nu).(sm-11)

The last term in Eq. (sm-10) is bounded byln⁡2\ln 2, and therefore contributes onlyO​(1)O(1)to the entropy.

UsingDq,0=(1−qNA)​(NAq),Dq,1=qNA​(NAq),\displaystyle D_{q,0}=\left(1-\frac{q}{N_{A}}\right)\binom{N_{A}}{q},\qquad D_{q,1}=\frac{q}{N_{A}}\binom{N_{A}}{q},(sm-12)

we can rewrite the second term in Eq. (sm-10) as∑qpq​ln⁡(NAq)+∑qpq​[(1−νq)​ln⁡(1−qNA)+νq​ln⁡(qNA)].\displaystyle\sum_{q}p_{q}\ln\binom{N_{A}}{q}+\sum_{q}p_{q}\left[(1-\nu_{q})\ln\left(1-\frac{q}{N_{A}}\right)+\nu_{q}\ln\left(\frac{q}{N_{A}}\right)\right].(sm-13)

The second sum is at mostO​(1)O(1). Therefore, up toO​(1)O(1)terms, we obtainS​(ΠA​(ρA))=−∑qpq​ln⁡pq+∑qpq​ln⁡(NAq)+O​(1).\displaystyle S(\Pi_{A}(\rho_{A}))=-\sum_{q}p_{q}\ln p_{q}+\sum_{q}p_{q}\ln\binom{N_{A}}{q}+O(1).(sm-14)

We now evaluate the two terms in Eq. (sm-14). The particle-number distributionpqp_{q}is obtained from the full counting statistics ofQAQ_{A}[37]:pq=∫−ππd​θ2​π​e−i​q​θ​χA​(θ),χA​(θ)=Tr⁡[ρA​ei​θ​QA].\displaystyle p_{q}=\int_{-\pi}^{\pi}\frac{d\theta}{2\pi}e^{-iq\theta}\chi_{A}(\theta),\qquad\chi_{A}(\theta)=\Tr\left[\rho_{A}e^{i\theta Q_{A}}\right].(sm-15)

For a Gaussian fermionic state, the full-counting statistics can be written as[33]χA​(θ)=det⁡[1−C+ei​θ​C],\displaystyle\chi_{A}(\theta)=\det\left[1-C+e^{i\theta}C\right],(sm-16)

whereCi​j=Tr⁡(ρA​ci†​cj),i,j∈A,\displaystyle C_{ij}=\Tr(\rho_{A}c_{i}^{\dagger}c_{j}),\qquad i,j\in A,(sm-17)

is the correlation matrix of the subsystem.

For a translation-invariant Fermi sea, the two-point correlation matrix readsCi​j=∫−ππd​k2​π​ei​k​(j−i)​Θ​[−εk].\displaystyle C_{ij}=\int_{-\pi}^{\pi}\frac{dk}{2\pi}e^{ik(j-i)}\Theta[-\varepsilon_{k}].(sm-18)

Thus, the determinant in Eq. (sm-16) is a Toeplitz determinant with symbolfθ​(k)=1+(ei​θ−1)​Θ​[−εk].\displaystyle f_{\theta}(k)=1+(e^{i\theta}-1)\Theta[-\varepsilon_{k}].(sm-19)

The symbol becomes nonanalytic at the Fermi points, at whichεk=0\varepsilon_{k}=0. IfNFN_{F}denotes the number of Fermi points, the Fisher-Hartwig theorem gives[16,28], for fixedθ∈(−π,π)\theta\in(-\pi,\pi),ln⁡χA​(θ)=i​θ​NA​ϱ−NF​θ24​π2​ln⁡NA+O​(1),\displaystyle\ln\chi_{A}(\theta)=i\theta N_{A}\varrho-\frac{N_{F}\theta^{2}}{4\pi^{2}}\ln N_{A}+O(1),(sm-20)

whereϱ=∫−ππd​k2​π​Θ​[−εk]\displaystyle\varrho=\int_{-\pi}^{\pi}\frac{dk}{2\pi}\Theta[-\varepsilon_{k}](sm-21)

is the filling of the Fermi sea.

Equation (sm-20) shows thatpqp_{q}is asymptotically Gaussian:pq=12​π​VA​exp⁡[−(q−NA​ϱ)22​VA]+o​(1),VA=NF2​π2​ln⁡NA+O​(1).\displaystyle p_{q}=\frac{1}{\sqrt{2\pi V_{A}}}\exp\left[-\frac{(q-N_{A}\varrho)^{2}}{2V_{A}}\right]+o(1),\qquad V_{A}=\frac{N_{F}}{2\pi^{2}}\ln N_{A}+O(1).(sm-22)

The entropy of this Gaussian distribution is−∑qpq​ln⁡pq=12​ln⁡(2​π​e​VA)+O​(1)=12​ln⁡ln⁡NA+O​(1).\displaystyle-\sum_{q}p_{q}\ln p_{q}=\frac{1}{2}\ln(2\pi eV_{A})+O(1)=\frac{1}{2}\ln\ln N_{A}+O(1).(sm-23)

Next, we evaluate the binomial term in Eq. (sm-14). Sincepqp_{q}is concentrated aroundq=NA​ϱq=N_{A}\varrhowith varianceVA=O​(ln⁡NA)V_{A}=O(\ln N_{A}), we use Stirling’s formula atq/NA=ϱ+O​(ln⁡NA/NA)q/N_{A}=\varrho+O(\sqrt{\ln N_{A}}/N_{A}):ln⁡(NAq)=NA​h​(qNA)−12​ln⁡[2​π​NA​qNA​(1−qNA)]+O​(NA−1).\displaystyle\ln\binom{N_{A}}{q}=N_{A}h\left(\frac{q}{N_{A}}\right)-\frac{1}{2}\ln\left[2\pi N_{A}\frac{q}{N_{A}}\left(1-\frac{q}{N_{A}}\right)\right]+O(N_{A}^{-1}).(sm-24)

Averaging it with the weightpqp_{q}, we obtain∑qpq​ln⁡(NAq)=NA​h​(ϱ)−12​ln⁡NA+O​(1).\displaystyle\sum_{q}p_{q}\ln\binom{N_{A}}{q}=N_{A}h(\varrho)-\frac{1}{2}\ln N_{A}+O(1).(sm-25)

The correction from expandingh​(q/NA)h(q/N_{A})aroundq/NA=ϱq/N_{A}=\varrhoisO​(VA/NA)O(V_{A}/N_{A}), and is therefore included in theO​(1)O(1)term.

Combining Eqs. (sm-23) and (sm-25), we obtain Eq. (17) asS​(ΠA​(ρA))=NA​h​(ϱ)−12​ln⁡NA+12​ln⁡ln⁡NA+O​(1).\displaystyle S(\Pi_{A}(\rho_{A}))=N_{A}h(\varrho)-\frac{1}{2}\ln N_{A}+\frac{1}{2}\ln\ln N_{A}+O(1).(sm-26)

## IIPermutation-symmetrized density matrix of Gaussian states

Here, we describe the method used to numerically calculate the von Neumann entropy in Eq. (sm-10) from the two-point correlation matrix given by Eq. (sm-17).

To calculate Eq. (sm-10), we need{pq,νq}q=0NA\{p_{q},\nu_{q}\}_{q=0}^{N_{A}}. To this end, we first diagonalize this matrix asCi​j=∑α=1NAuα​i​λα​uα​j∗,\displaystyle C_{ij}=\sum_{\alpha=1}^{N_{A}}u_{\alpha i}\lambda_{\alpha}u_{\alpha j}^{*},(sm-27)

where0≤λα≤10\leq\lambda_{\alpha}\leq 1. We define fermionic normal modesfα=∑i∈Auα​i​ci.\displaystyle f_{\alpha}=\sum_{i\in A}u_{\alpha i}c_{i}.(sm-28)

In this basis, the reduced density matrix can be written as[46]ρA=∑𝐧p𝐧​|𝐧⟩⟨𝐧|p𝐧=∏α=1NAλαnα​(1−λα)1−nα,\displaystyle\rho_{A}=\sum_{\mathbf{n}}p_{\mathbf{n}}\outerproduct{\mathbf{n}}{\mathbf{n}}\qquad p_{\mathbf{n}}=\prod_{\alpha=1}^{N_{A}}\lambda_{\alpha}^{n_{\alpha}}(1-\lambda_{\alpha})^{1-n_{\alpha}},(sm-29)

where𝐧=(n1,…,nNA)\mathbf{n}=(n_{1},\ldots,n_{N_{A}}),nα∈{0,1}n_{\alpha}\in\{0,1\}, and|𝐧⟩=∏α=1NA(fα†)nα​|Ω⟩.\displaystyle\ket{\mathbf{n}}=\prod_{\alpha=1}^{N_{A}}(f_{\alpha}^{\dagger})^{n_{\alpha}}\ket{\Omega}.(sm-30)

The probabilitypqp_{q}of findingqqparticles inAAispq=∑𝐧:|𝐧|=qp𝐧.\displaystyle p_{q}=\sum_{\mathbf{n}:|\mathbf{n}|=q}p_{\mathbf{n}}.(sm-31)

We can compute these probabilities from the generating polynomialF​(z)=∏α=1NA[(1−λα)+λα​z]=∑q=0NApq​zq.\displaystyle F(z)=\prod_{\alpha=1}^{N_{A}}\left[(1-\lambda_{\alpha})+\lambda_{\alpha}z\right]=\sum_{q=0}^{N_{A}}p_{q}z^{q}.(sm-32)

Equivalently, we use the recurrencepq(r)=(1−λr)​pq(r−1)+λr​pq−1(r−1),\displaystyle p_{q}^{(r)}=(1-\lambda_{r})p_{q}^{(r-1)}+\lambda_{r}p_{q-1}^{(r-1)},(sm-33)

Here,pq(r)p_{q}^{(r)}is the probability of findingqqparticles among the firstrreigenmodes. We obtain the probabilitypq=pq(NA)p_{q}=p_{q}^{(N_{A})}by numerically solving the recursion relation (sm-33) with initial conditionp0(0)=1p_{0}^{(0)}=1andpq(0)=0p_{q}^{(0)}=0forq≠0q\neq 0.

Next, we compute the conditional occupation of the uniform orbitalνq=Tr⁡(ρA,q​nA,0),ρA,q=Pq​ρA​Pqpq,nA,0=dA,0†​dA,0,dA,0=1NA​∑i∈Aci.\displaystyle\nu_{q}=\Tr(\rho_{A,q}n_{A,0}),\qquad\rho_{A,q}=\frac{P_{q}\rho_{A}P_{q}}{p_{q}},\qquad n_{A,0}=d_{A,0}^{\dagger}d_{A,0},\qquad d_{A,0}=\frac{1}{\sqrt{N_{A}}}\sum_{i\in A}c_{i}.(sm-34)

In thefαf_{\alpha}basis, the uniform orbital can be written asdA,0=∑α=1NAsα​fα,sα=1NA​∑i∈Auα​i∗.\displaystyle d_{A,0}=\sum_{\alpha=1}^{N_{A}}s_{\alpha}f_{\alpha},\qquad s_{\alpha}=\frac{1}{\sqrt{N_{A}}}\sum_{i\in A}u_{\alpha i}^{*}.(sm-35)

SinceρA,q\rho_{A,q}is diagonal in the occupation basis of thefαf_{\alpha}modes, we obtainTr⁡[ρA,q​fα†​fβ]=δα,β​Pr⁡(nα=1|QA=q),\displaystyle\Tr[\rho_{A,q}f_{\alpha}^{\dagger}f_{\beta}]=\delta_{\alpha,\beta}\Pr(n_{\alpha}=1|Q_{A}=q),(sm-36)

wherePr⁡(nα=1∣QA=q)\Pr(n_{\alpha}=1\mid Q_{A}=q)is the probability that theα\alpha-th eigenmode is occupied, conditioned on findingqqparticles in subsystemAA.
Using Eq. (sm-36),νq\nu_{q}can be written asνq=∑α=1NA|sα|2​Pr⁡(nα=1|QA=q).\displaystyle\nu_{q}=\sum_{\alpha=1}^{N_{A}}|s_{\alpha}|^{2}\Pr(n_{\alpha}=1\,|\,Q_{A}=q).(sm-37)

The conditional probabilities in Eq. (sm-37) are computed as follows. For eachα\alpha, we defineF(α)​(z)=∏β≠α[(1−λβ)+λβ​z]=∑m=0NA−1pm(α)​zm.\displaystyle F^{(\alpha)}(z)=\prod_{\beta\neq\alpha}\left[(1-\lambda_{\beta})+\lambda_{\beta}z\right]=\sum_{m=0}^{N_{A}-1}p_{m}^{(\alpha)}z^{m}.(sm-38)

Then the joint probability ofnα=1n_{\alpha}=1andQA=qQ_{A}=qisPr⁡(nα=1,QA=q)=λα​pq−1(α).\displaystyle\Pr(n_{\alpha}=1,Q_{A}=q)=\lambda_{\alpha}p_{q-1}^{(\alpha)}.(sm-39)

Therefore,νq=1pq​∑α=1NA|sα|2​λα​pq−1(α),\displaystyle\nu_{q}=\frac{1}{p_{q}}\sum_{\alpha=1}^{N_{A}}|s_{\alpha}|^{2}\lambda_{\alpha}p_{q-1}^{(\alpha)},(sm-40)

wherep−1(α)=0p_{-1}^{(\alpha)}=0. In the numerical calculation, the coefficientspm(α)p_{m}^{(\alpha)}are obtained from the same recurrence as Eq. (sm-33), with the modeα\alphaomitted.

## 


- 


Major funding support from
