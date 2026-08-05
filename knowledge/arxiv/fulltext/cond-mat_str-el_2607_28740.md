# Gapped Parent Hamiltonians for the Strongly Deformed Toric Code

**arXiv ID**: 2607.28740v1
**Authors**: Nandagopal Manoj, Zack Weinstein, Jason Alicea
**Published**: 2026-07-30
**Categories**: cond-mat.str-el, cond-mat.stat-mech, quant-ph
**Comments**: 7 + 25 pages, 1 + 2 figures
**HTML URL**: https://arxiv.org/html/2607.28740v1

## Abstract

Local non-unitary deformations of topologically ordered wavefunctions can drive transitions into peculiar states that challenge modern perspectives on gapped quantum matter. The strongly deformed toric code offers a curious case, hosting $m$ anyon condensation alongside perimeter-law scaling of Wilson loops charged under an exact 1-form symmetry---properties that typically do not coexist in gapped ground states. Nevertheless, we rigorously construct local gapped parent Hamiltonians for these strongly deformed toric code states. The Hamiltonians we construct are not strictly finite-range, but contain sums of Wilson loop operators whose coefficients decay exponentially in their diameter. If one adopts standard locality bounds used to define gapped phases---which allow for such exponentially decaying terms---our construction shows that these states realize a trivial gapped phase. Within this locality class, we demonstrate that perimeter-law scaling of Wilson loops does not imply a spontaneously broken 1-form symmetry, and from a dual perspective, that long-range ferromagnetic order and perimeter-law disorder parameter correlations can coexist in a 2D gapped ground state. We evade a recent no-go theorem [Sahay et al., arXiv:2503.01977] by relaxing its assumptions in a manner that we quantify as benign in the thermodynamic limit. More broadly, our results highlight that stronger notions of locality are necessary for prohibiting these counterintuitive properties within a gapped phase.

## Full Text

Gapped Parent Hamiltonians for the Strongly Deformed Toric Code

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
- License: CC BY 4.0arXiv:2607.28740v1 [cond-mat.str-el] 30 Jul 2026

## Gapped Parent Hamiltonians for the Strongly Deformed Toric CodeNandagopal Manojnmanoj@caltech.eduZack WeinsteinJason AliceaDepartment of Physics and Institute for Quantum Information and Matter, California Institute of Technology, Pasadena, CA 91125, USA

## Abstract

Local non-unitary deformations of topologically ordered wavefunctions can drive transitions into peculiar states that challenge modern perspectives on gapped quantum matter.
The strongly deformed toric code offers a curious case, hostingmmanyon condensation alongside perimeter-law scaling of Wilson loops charged under an exact 1-form symmetry—properties that typically do not coexist in gapped ground states. Nevertheless, we rigorously construct local gapped parent Hamiltonians for these strongly deformed toric code states. The Hamiltonians we construct are not strictly finite-range, but contain sums of Wilson loop operators whose coefficients decay exponentially in their diameter. If one adopts standard locality bounds used to define gapped phases—which allow for such exponentially decaying terms—our construction shows that these states realize a trivial gapped phase. Within this locality class, we demonstrate that perimeter-law scaling of Wilson loops does not imply a spontaneously broken 1-form symmetry, and from a dual perspective, that long-range ferromagnetic order and perimeter-law disorder parameter correlations can coexist in a 2D gapped ground state. We evade a recent no-go theorem [Sahay et al., arXiv:2503.01977] by relaxing its assumptions in a manner that we quantify as benign in the thermodynamic limit. More broadly, our results highlight that stronger notions of locality are necessary for prohibiting these counterintuitive properties within a gapped phase.

Ground states of local gapped Hamiltonians have been rigorously proven to exhibit exponentially decaying correlations[23,24]. The nature of the converse relationship—the sufficient conditions for a quantum state to be the gapped ground state of a local Hamiltonian—remains a fundamental open problem outside of one spatial dimension. In one dimension, the identification of matrix product states as the relevant ‘corner of Hilbert space’ enables an analytical classification of gapped phases[21,22,10,11,41]and underlies powerful variational techniques for their numerical study[49,38,46,45,13]. Attaining an analogous understanding in two (and higher) dimensions potentially paves the way for similar applications.

Deformed toric code states [see Eq. (2)] provide an interesting edge case that subtly challenges modern methods of classifying phases. These states arise from deforming toric code ground states by a non-unitary operator that createsmm-anyon pairs, driving a quantum phase transition out of the topological phase beyond a critical deformation strength[9]. In the resulting strongly deformed phase, a peculiar combination of properties emerges: (i) condensedmmanyons; (ii) an exact ‘electric’ 1-form symmetry; and (iii)perimeter-lawscaling of Wilson loops[25]. The final property is especially puzzling, given the first two: such a perimeter law is typically interpreted as a signature of deconfinedeeanyons and a spontaneously broken 1-form symmetry[20,37], both of which appear incompatible with a conventionalmm-condensed gapped phase[8]. Based on this observation, Ref.40proved a rigorous no-go theorem showing—subject to several technical assumptions—that the strongly deformed toric code states areintrinsically gapless; that is, they do not admit a local gapped parent Hamiltonian with a finite ground-state degeneracy.Figure 1:(a) Properties of the deformed toric code state|ψ​(β)⟩\ket{\psi(\beta)}.
Forβ\betabeyond a critical deformation strengthβc\beta_{c},mmanyons condense and destroy the topological order, yet Wilson loops continue to exhibit perimeter-law scaling. The vertical axis on the phase diagram sketches the spectral gap of two parent Hamiltonians for|ψ​(β)⟩\ket{\psi(\beta)}: the Castelnovo-Chamon HamiltonianHCCH_{\rm CC}[Eq. (6)] and our parent HamiltonianH​(β)H(\beta)[Eq. (9)], proved to be gapped and
non-degenerate for sufficiently largeβ\beta.
(b) Toric-code stabilizersAvA_{v}andBpB_{p}, the associated11-form symmetryZℒ~Z_{\tilde{\mathcal{L}}}, and Wilson loop operatorXℒX_{\mathcal{L}}.Table 1:Corollaries of the parent Hamiltonian construction. Gapped ground state is in reference to an exponential-in-diameter-local Hamiltonian [cf. Eq. (15)].1. Perimeter-law Wilson loops in a gapped ground state do not imply11-form SSB.2. Long-range order parameter correlations and perimeter-law disorder correlations can coexist in a 2D gapped ground state.3. Toric code under strong Pauli-ZZdecoherence is separable as a convex sum of trivial gapped ground states.4. 2D classical Ising ferromagnet at low temperature is dual to aℤ2\mathbb{Z}_{2}gauge theory with exponentially decaying interactions at high temperature.

In this Letter, we explicitly construct local parent Hamiltonians for which the strongly deformed toric code states are the unique gapped ground states. We circumvent the no-go theorem of Ref.40by relaxing its assumptions in a physically motivated way—such that the violations to these assumptions vanish exponentially quickly in the thermodynamic limit. Our parent Hamiltonians naturally incorporate the perimeter law by containing sums of Wilson loop operators with coefficients decaying exponentially in their support; although the resulting Hamiltonians are not strictly finite-range, they nevertheless satisfy standard locality bounds commonly used to define and analyze gapped phases of matter[23,24]. More broadly, we demonstrate that within the standard definition of locality, perimeter-law decay of Wilson loops is compatible with a trivial symmetric phase and is therefore not a reliable probe of 1-form spontaneous symmetry breaking (SSB). Our construction yields a number of nontrivial corollaries, highlighted in Table1.

Deformed toric code.Consider anLx×LyL_{x}\times L_{y}square lattice with periodic boundary conditions, where each edgeeehosts a qubit equipped with Pauli operatorsXe,ZeX_{e},Z_{e}. The code space of the toric code is the simultaneous +1 eigenspace of the vertex stabilizersAv=∏e∋vZeA_{v}=\prod_{e\ni v}Z_{e}and the plaquette stabilizersBp=∏e∈pXeB_{p}=\prod_{e\in p}X_{e}[see Fig.1(b)]. In other words, it is the four-dimensional ground-state subspace of the Hamiltonian[28]HTC=∑v(1−Av)+∑p(1−Bp).H_{\text{TC}}=\sum_{v}(1-A_{v})+\sum_{p}(1-B_{p}).(1)

We will initially focus on the logical ‘++’ toric code state|TC⟩=∑ℒXℒ​|0⟩\ket{\text{TC}}=\sum_{\mathcal{L}}X_{\mathcal{L}}\ket{0}, whereXℒ=∏e∈ℒXeX_{\mathcal{L}}=\prod_{e\in\mathcal{L}}X_{e}is a product over a collection of (possibly disconnected or non-contractible) closed loopsℒ\mathcal{L}in the direct lattice, and|0⟩\ket{0}is the simultaneous +1 eigenstate of eachZeZ_{e}. This state satisfiesXℒ​|TC⟩=|TC⟩X_{\mathcal{L}}\ket{\text{TC}}=\ket{\text{TC}}for any loopℒ\mathcal{L}, and is therefore the +1 eigenstate of the two logical-XXoperators.

Given|TC⟩\ket{\text{TC}}, the (unnormalized) deformed toric code state is defined by[9]|ψ​(β)⟩\displaystyle\ket{\psi(\beta)}=eβ2​∑eZe​|TC⟩∝∑ℒe−β​|ℒ|​Xℒ​|0⟩\displaystyle=e^{\frac{\beta}{2}\sum_{e}Z_{e}}\ket{\text{TC}}\propto\sum_{\mathcal{L}}e^{-\beta\absolutevalue{\mathcal{L}}}X_{\mathcal{L}}\ket{0}(2)

with|ℒ|\absolutevalue{\mathcal{L}}the number of edges inℒ\mathcal{L}. This state is symmetric under the 1-form symmetryZℒ~Z_{\tilde{\mathcal{L}}}[Fig.1(b)] for anycontractibleloopℒ~\tilde{\mathcal{L}}in the dual lattice, and thus differs slightly from the deformed state considered in Ref.40; we address the latter as well in later sections.

The norm of|ψ​(β)⟩\ket{\psi(\beta)},⟨ψ​(β)|ψ​(β)⟩∝∑ℒe−2​β​|ℒ|,\displaystyle\innerproduct{\psi(\beta)}{\psi(\beta)}\propto\sum_{\mathcal{L}}e^{-2\beta\absolutevalue{\mathcal{L}}},(3)

is proportional to the partition function of the two-dimensional (2D) classical Ising model, where eachℒ\mathcal{L}represents a configuration of magnetic domain walls[1]. This connection suggests that|ψ​(β)⟩\ket{\psi(\beta)}exhibits a phase transition in the 2D classical Ising⋆universality class at a critical deformation strengthβc=12​ln⁡(1+2)≈0.441\beta_{c}=\frac{1}{2}\ln(1+\sqrt{2})\approx 0.441.
Within the strongly deformed phaseβ>βc\beta>\beta_{c},|ψ​(β)⟩\ket{\psi(\beta)}exhibits long-range order in the string operatorZP~=∏e∈P~ZeZ_{\tilde{P}}=\prod_{e\in{\tilde{P}}}Z_{e}that createsmmanyons at the endpoints of the dual-lattice pathP~{\tilde{P}},
indicating thatmmanyons are condensed[8]. The resulting state is topologically trivial, as indicated by a vanishing topological entanglement entropy[9,34,29].

In typical Hamiltonian deformations ofHTCH_{\text{TC}}that condense themmanyons while preserving the exact 1-form symmetry[48,31], the resulting ground states exhibit area-law scaling of Wilson loop expectation values:⟨Xℒ⟩∼e−α​Area​(ℒ)\expectationvalue{X_{\mathcal{L}}}\sim e^{-\alpha\text{Area}(\mathcal{L})}, for a large contractible loopℒ\mathcal{L}. In contrast, Ref.25emphasized that|ψ​(β)⟩\ket{\psi(\beta)}exhibits perimeter-law scaling⟨Xℒ⟩∼e−μ​|ℒ|\expectationvalue{X_{\mathcal{L}}}\sim e^{-\mu\absolutevalue{\mathcal{L}}}for any finiteβ\beta, even within the strongly deformed phase. These authors interpreted the perimeter-law scaling of Wilson loops in theβ>βc\beta>\beta_{c}phase as indicative of spontaneous 1-form symmetry-breakingwithouttopological order, in apparent violation of the generalized Landau paradigm[37]. Subsequently, Ref.40suggested that the combination of exact 1-form symmetry underZℒ~Z_{\tilde{\mathcal{L}}}, long-range order in⟨ZP~⟩\expectationvalue{Z_{\tilde{P}}}, and perimeter-law scaling in⟨Xℒ⟩\expectationvalue{X_{\mathcal{L}}}cannot arise in the ground state of a gapped Hamiltonian with a finite degeneracy. Here we will offer an alternative perspective on the state|ψ​(β)⟩\ket{\psi(\beta)}by constructing, at large deformation strengthsβ\beta, an exact local parent Hamiltonian for which|ψ​(β)⟩\ket{\psi(\beta)}is the unique gapped ground state.

Parent Hamiltonian constructions.Equation (2) reveals two complementary perspectives on|ψ​(β)⟩\ket{\psi(\beta)}. At smallβ\beta, where the topological order persists,|ψ​(β)⟩\ket{\psi(\beta)}is most naturally viewed as a deformation of theHTCH_{\rm TC}ground state|TC⟩\ket{\rm{TC}}. Conversely, largeβ\betamassacres the topological order and exponentially suppresses large loops in the representation on the right side of Eq. (2). There it is more natural to view|ψ​(β)⟩\ket{\psi(\beta)}as a deformation of the trivial product state|0⟩\ket{0}, which is the unique zero-energy ground state ofH0=∑e(1−Ze).H_{0}=\sum_{e}(1-Z_{e}).(4)

We will show that these two viewpoints lead to distinct parent Hamiltonians—adiabatically connected toHTCH_{\text{TC}}andH0H_{0}, respectively—that are local and gapped in their ‘natural’ regimes.

Let us start with the former viewpoint and define manifestly
Hermitian, positive-semidefinite operatorsQpQ_{p}by the following deformation of theBpB_{p}projectors in Eq. (1):Qp=e−β2​∑e∈pZe​(1−Bp)​e−β2​∑e∈pZe=e−β​∑e∈pZe−Bp.\begin{split}Q_{p}&=e^{-\frac{\beta}{2}\sum_{e\in p}Z_{e}}(1-B_{p})e^{-\frac{\beta}{2}\sum_{e\in p}Z_{e}}\\
&=e^{-\beta\sum_{e\in p}Z_{e}}-B_{p}.\end{split}(5)

Notice that the exponentials in the first line contain only pieces of the non-unitary deformationeβ2​∑eZee^{\frac{\beta}{2}\sum_{e}Z_{e}}from Eq. (2) that do not commute with a particularBpB_{p}. All of the operators(1−Av)(1-A_{v})andQpQ_{p}clearly annihilate|ψ​(β)⟩\ket{\psi(\beta)}, which accordingly admits the finite-range, frustration-free parent HamiltonianHCC​(β)=∑v(1−Av)+∑pQpH_{\rm CC}(\beta)=\sum_{v}(1-A_{v})+\sum_{p}Q_{p}(6)

for anyβ\beta. One can readily show thatHCC​(β)H_{\text{CC}}(\beta)is an exact parent Hamiltonian for any toric code ground state deformed byeβ2​∑eZee^{\frac{\beta}{2}\sum_{e}Z_{e}}.
Equation (6) is precisely the Castelnovo-Chamon Hamiltonian[9]and is indeed gapped forβ<βc\beta<\beta_{c}but, interestingly, gapless forβ>βc\beta>\beta_{c}[40].

Next we apply similar logic at largeβ\beta, where|ψ​(β)⟩\ket{\psi(\beta)}appears ‘close’ to|0⟩\ket{0}. First note that the operator𝒵=∑ℒe−β​|ℒ|​Xℒ∝∑{sv=±1}eK​∑⟨v​v′⟩Xv​v′​sv​sv′\mathcal{Z}=\sum_{\mathcal{L}}e^{-\beta\absolutevalue{\mathcal{L}}}X_{\mathcal{L}}\propto\sum_{\quantity{s_{v}=\pm 1}}e^{K\sum_{\expectationvalue*{vv^{\prime}}}X_{vv^{\prime}}s_{v}s_{v^{\prime}}}(7)

acting on|0⟩\ket{0}in Eq. (2) is positive-definite for allβ>0\beta>0. This observation follows from the right side of Eq. (7), which identifies𝒵\mathcal{Z}with the partition function of a bond-disordered Ising model at inverse temperatureK=artanh⁡(e−β)>0K=\operatorname{artanh}(e^{-\beta})>0. There,svs_{v}’s represent auxiliary classical spins on the verticesvvof the lattice, and the Pauli operatorsXv​v′≡XeX_{vv^{\prime}}\equiv X_{e}on the linkseeconnecting verticesv,v′v,v^{\prime}encode signs of the Ising couplings. Positive-definiteness of𝒵\mathcal{Z}guarantees that the operatorW=log⁡𝒵≡∑ℒJℒ​XℒW=\log\mathcal{Z}\equiv\sum_{\mathcal{L}}J_{\mathcal{L}}X_{\mathcal{L}}(8)

is well-defined and Hermitian. Furthermore,WWcommutes with each vertex stabilizerAvA_{v}and hence can be expanded as a sum over loop operatorsXℒX_{\mathcal{L}}with real-valued coefficientsJℒJ_{\mathcal{L}}, as shown above.

At this point we have expressed|ψ​(β)⟩\ket{\psi(\beta)}as the trivial state|0⟩\ket{0}deformed by a non-unitary operator𝒵=eW\mathcal{Z}=e^{W}, whereWWis a sum of commuting operators—paralleling the middle representation in Eq. (2). Defining operatorsWe=∑ℒ∋eJℒ​XℒW_{e}=\sum_{\mathcal{L}\ni e}J_{\mathcal{L}}X_{\mathcal{L}}that contain only the components ofWWthat anticommute withZeZ_{e}, we analogously obtain our alternate
frustration-free parent Hamiltonian for|ψ​(β)⟩\ket{\psi(\beta)},H​(β)=∑ee−We​(1−Ze)​e−We=∑e(e−2​We−Ze).\begin{split}H(\beta)&=\sum_{e}e^{-W_{e}}\left(1-Z_{e}\right)e^{-W_{e}}\\
&=\sum_{e}\quantity(e^{-2W_{e}}-Z_{e}).\end{split}(9)

Indeed, similar to the Castelnovo-Chamon Hamiltonian (6),H​(β)H(\beta)sums Hermitian, positive-semidefinite terms that individually annihilate|ψ​(β)⟩\ket{\psi(\beta)}.

Contrary to the Castelnovo-Chamon Hamiltonian, locality ofH​(β)H(\beta)is not manifest but can be argued heuristically at largeβ\betaas follows. In the extreme limitβ→∞\beta\to\infty, eachJℒJ_{\mathcal{L}}for non-empty loop configurationsℒ\mathcal{L}vanishes, andH​(β→∞)H(\beta\to\infty)reduces to the trivial local parent Hamiltonian (4). More generally, eachJℒJ_{\mathcal{L}}decays asymptotically in|ℒ|\absolutevalue{\mathcal{L}}ase−β​|ℒ|e^{-\beta\absolutevalue{\mathcal{L}}}, exponentially suppressing large loop contributions toWeW_{e}. Furthermore, as we carefully explain below, the logarithm in Eq. (8) ensures that potentially problematic nonlocal loop configurations consisting of far-separated disconnected loops are effectively absent inWW.
This observation—which one can readily verify to low orders by Taylor expanding the logarithm—closely relates to the linked-cluster theorem from diagrammatic perturbation theory[51], and crucially ensures extensivity of the “free energy”WWfor the disordered Ising model𝒵\mathcal{Z}[26]. Consequently, it is natural to expect that each operatore−2​Wee^{-2W_{e}}is locally supported near the edgeee, and can be organized as a sum of terms that decay exponentially in their diameter abouteein the large-β\betaregime.

Proving locality and spectral gap.We now outline a rigorous proof that, for sufficiently largeβ\beta, our parent HamiltonianH​(β)H(\beta)is local in the sense of Refs.23,24,40and consequently exhibits a finite spectral gap. Technical details are deferred to the Supplemental Material[5]. Our approach uses the Mayer cluster expansion[19]to explicitly write Eq. (8) as a sum of exponentially localized terms, bolstering the intuition developed above. Locality ofH​(β)H(\beta)arises directly from properties of the cluster expansion, and the spectral gap at largeβ\betathen follows from the gap stability results of Refs.6,7.

To this end, we interpret𝒵\mathcal{Z}in Eq. (7) as the (operator-valued) partition function for a hard-corepolymer model. Each loop configurationℒ\mathcal{L}is first decomposed into a collection of connected loopsγ\gamma(‘polymers’), each carrying the operator-valued weightw​(γ)=e−β​|γ|​Xγw(\gamma)=e^{-\beta\absolutevalue{\gamma}}X_{\gamma}. Each pair of polymersγ,γ′\gamma,\gamma^{\prime}is then assigned a hard-core interactionδ​(γ,γ′)=0\delta(\gamma,\gamma^{\prime})=0if they intersect and11otherwise. With this notation, Eq. (7) can be rewritten as𝒵=∑Γ′⊆Γ[∏γ∈Γ′w​(γ)]​[∏{γ,γ′}⊆Γ′δ​(γ,γ′)],\mathcal{Z}=\sum_{\Gamma^{\prime}\subseteq\Gamma}\left[\prod_{\gamma\in\Gamma^{\prime}}w(\gamma)\right]\left[\prod_{\left\{\gamma,\gamma^{\prime}\right\}\subseteq\Gamma^{\prime}}\delta(\gamma,\gamma^{\prime})\right],(10)

whereΓ\Gammadenotes the set of all possible polymersγ\gamma, andΓ′\Gamma^{\prime}sums over all subsets ofΓ\Gamma. The hard-core interactions ensure that the contributing subsetsΓ′\Gamma^{\prime}are in one-to-one correspondence with the loop configurationsℒ\mathcal{L}in Eq. (7).

The Mayer cluster expansion expresses the ‘polymer free energy’WWas a sum overconnected clusters𝒞\mathcal{C}, each defined as a (possibly repeating) finite sequence of polymers(γ1,γ2,…,γn)\left(\gamma_{1},\gamma_{2},\ldots,\gamma_{n}\right)whose union is connected[19].
Eq. (8) accordingly admits the more constrained formW=∑𝒞f​(𝒞)​X𝒞,W={\sum_{\mathcal{C}}f(\mathcal{C})X_{\mathcal{C}}},(11)

whereX𝒞=(γ1,…,γn)≡Xγ1​Xγ2​…​XγnX_{\mathcal{C}=(\gamma_{1},\dots,\gamma_{n})}\equiv X_{\gamma_{1}}X_{\gamma_{2}}\dots X_{\gamma_{n}}, and the coefficientsf​(𝒞)f(\mathcal{C})are defined precisely in the End Matter. We can then identifyWe=∑𝒞∈𝒮ef​(𝒞)​X𝒞W_{e}=\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}, where𝒮e≡{𝒞:support​(X𝒞)∋e}\mathcal{S}_{e}\equiv\left\{\mathcal{C}:\text{support}(X_{\mathcal{C}})\ni e\right\}defines the set of connected clusters for whichX𝒞X_{\mathcal{C}}anticommutes withZeZ_{e}. Our parent Hamiltonian then admits the useful representationH​(β)=H0+V​(β)H(\beta)=H_{0}+V(\beta), whereV​(β)=∑e(exp⁡[−2​∑𝒞∈𝒮ef​(𝒞)​X𝒞]−1).V(\beta)=\sum_{e}\left(\exp\left[-2\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}\right]-1\right).(12)

In the Supplemental Material[5], we derive several properties of the coefficientsf​(𝒞)f(\mathcal{C})relevant for the locality ofH​(β)H(\beta). We first show that the coefficients decay exponentially with the size of the constituent polymers defining𝒞\mathcal{C}—i.e.,|f​(𝒞)|≲∏γ∈𝒞e−β​|γ|\absolutevalue{f(\mathcal{C})}\lesssim\prod_{\gamma\in\mathcal{C}}e^{-\beta\absolutevalue{\gamma}}. This fact alone does not suffice for locality, since eachWeW_{e}sums over combinatorially many connected clusters. To prove thatH​(β)H(\beta)is bounded and local, we further derive the crucial inequality (see also Ref.17for a tighter bound)∑𝒞∈𝒮e|f​(𝒞)|≤const×e−4​β\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})}\leq\mathrm{const}\times e^{-4\beta}(13)

which involves the sum ofallf​(𝒞)f(\mathcal{C})’s contributing to a givenWeW_{e}, and holds forβ>β∗=2+log⁡3\beta>\beta^{*}=2+\log 3. These bounds are proved using graph-theoretic techniques that are standard to the cluster expansion[19,39,32]; the nontrivial step involves bounding the∼n!\sim n!growth in the number of ways the same set ofnnpolymers can form a cluster.
Equation (13), together with the exponential decay off​(𝒞)f(\mathcal{C})in cluster size, ensures thatH​(β)H(\beta)is a sum of exponentially localized operators for sufficiently largeβ\beta, in harmony with the intuition developed earlier.

Finally, sinceH​(β)H(\beta)in Eq. (9) is obtained from a local perturbationV​(β)V(\beta)to the trivial gapped HamiltonianH0H_{0}in Eq. (4), we can leverage the results of Bravyi et al.[6,7]to prove thatH​(β)H(\beta)is also gapped for sufficiently largeβ\beta. Explicitly, we first decomposeV​(β)=∑r≥1∑A∈S​(r)Vr,AV(\beta)=\sum_{r\geq 1}\sum_{A\in S(r)}V_{r,A}into a sum of local terms, whereS​(r)S(r)is the set of allr×rr\times rsquaresAAon the lattice, andVr,AV_{r,A}exhibits trivial support outside ofAA. Next, we prove in the Supplemental Material[5]that the operator norm‖Vr,A‖\norm{V_{r,A}}of each local term can be (conservatively) upper-bounded as‖Vr,A‖≤J​(β)​e−r,J​(β)=e−4​β×(4.11×105),\norm{V_{r,A}}\leq J(\beta)e^{-r},\quad J(\beta)=e^{-4\beta}\times(4.11\times 10^{5}),(14)

which shows that‖Vr,A‖\norm{V_{r,A}}decays (at least) exponentially in the diameter ofAA. With this precise definition of a local perturbationV​(β)V(\beta), Ref.6proved that the gapΔ​(β)\Delta(\beta)ofH​(β)H(\beta)is lower-bounded asΔ​(β)≥[1−c1​J​(β)]​Δ0\Delta(\beta)\geq[1-c_{1}J(\beta)]\Delta_{0}up to corrections that vanish super-polynomially in system size[2], wherec1c_{1}is a constant andΔ0=2\Delta_{0}=2is the gap ofH0H_{0}. SinceJ​(β)J(\beta)decays exponentially withβ\beta, we have shown that for sufficiently largeβ\beta, our local parent HamiltonianH​(β)H(\beta)admits the unique ground state|ψ​(β)⟩\ket{\psi(\beta)}with a finite spectral gapΔ​(β)\Delta(\beta)[3].

Consistency with the no-go theorem.Let us describe the relationship between our construction and the rigorous no-go theorem from Ref.40. Thus far we have focused on the deformed logical ‘++’ state—Eq. (2)—which we now denote more explicitly by|ψ++​(β)⟩\ket{\psi_{++}(\beta)}. Our parent HamiltonianH​(β)H(\beta)for this state does not violate the no-go theorem, since|ψ++​(β)⟩\ket{\psi_{++}(\beta)}does not satisfy all of its assumptions: namely, the theorem requires an exact 1-form symmetryZℒ~Z_{\tilde{\mathcal{L}}}about both contractibleandnon-contractible loopsℒ~\tilde{\mathcal{L}}in the dual lattice. To meet these assumptions, we should instead consider the logical ‘00’ state|ψ00​(β)⟩∝∑ℒ′e−β​|ℒ|​Xℒ​|0⟩\ket{\psi_{00}(\beta)}\propto\sum_{\mathcal{L}}^{\prime}e^{-\beta\absolutevalue{\mathcal{L}}}X_{\mathcal{L}}\ket{0}, where the prime indicates that the sum is performed over only contractible loopsℒ\mathcal{L}.

Since non-contractible loops in|ψ++​(β)⟩\ket{\psi_{++}(\beta)}are exponentially suppressed in the linear system sizeL≡min⁡(Lx,Ly)L\equiv\min(L_{x},L_{y})throughout the strongly deformed phaseβ>βc\beta>\beta_{c}, the (normalized) fidelity between|ψ00​(β)⟩\ket{\psi_{00}(\beta)}and|ψ++​(β)⟩\ket{\psi_{++}(\beta)}is lower-bounded by1−e−𝒪​(L)1-e^{-\mathcal{O}(L)}at largeβ\beta. Consequently, these two states are indistinguishable from each other in the thermodynamic limit; in particular,H​(β)H(\beta)is an excellentapproximateparent Hamiltonian for|ψ00​(β)⟩\ket{\psi_{00}(\beta)}, with a variational energye−𝒪​(L)e^{-\mathcal{O}(L)}. Since phases of matter are strictly well-defined in the thermodynamic limitL→∞L\to\infty, we should regard|ψ00​(β)⟩\ket{\psi_{00}(\beta)}as belonging to the same phase of matter as|ψ++​(β)⟩\ket{\psi_{++}(\beta)}, namely, a trivial gapped phase. This observation is again consistent with the results of Ref.40, which focuses on the existence ofexactparent Hamiltonians.

Nevertheless, by employing identical cluster expansion techniques as in the previous section, we can indeed construct an exact 1-form symmetric parent HamiltonianH(00)​(β)H^{(00)}(\beta)for which|ψ00​(β)⟩\ket{\psi_{00}(\beta)}is the unique gapped ground state[5]. This Hamiltonian differs from Eq. (12) by terms of total spectral norme−𝒪​(L)e^{-\mathcal{O}(L)}in the large-β\betaregime, and satisfies a locality criterion analogous to Eq. (14) for anyfixedaspect ratioax​y≡Lx/Lya_{xy}\equiv L_{x}/L_{y}. Once more, this result is consistent with the no-go theorem, which forbids the existence of a parent Hamiltonian obeying anaspect-ratio-independentlocality bound. Specifically, Ref.40begins from the standard definition of local HamiltoniansH=∑ℛ⊆ΛhℛH=\sum_{\mathcal{R}\subseteq\Lambda}h_{\mathcal{R}}with exponentially decaying tails[23,24], which are required to satisfy the bound[4]supi∈Λ∑ℛ∋i‖hℛ‖​|ℛ|​eμ​diam⁡(ℛ)≤s\sup_{i\in\Lambda}\sum_{\mathcal{R}\ni i}\norm{h_{\mathcal{R}}}\absolutevalue{\mathcal{R}}e^{\mu\operatorname{diam}(\mathcal{R})}\leq s(15)

for finite constantsμ,s\mu,s, but additionally demands thatμ,s\mu,scan be chosen independently of the aspect ratioax​ya_{xy}. On the other hand, our HamiltonianH(00)​(β)H^{(00)}(\beta)contains terms which createpairsof far-separated non-contractible closed loops. Although the total norm of such terms is exponentially suppressed inLL, the aspect ratio can always be chosen sufficiently small that Eq. (15) is violated for any constantsμ,s\mu,sfixed in advance. Our parent Hamiltonian construction therefore demonstrates that the aspect-ratio-independent locality criterion is not just a technical assumption, but physically necessary for proving enforced gaplessness of|ψ00​(β)⟩\ket{\psi_{00}(\beta)}.

Discussion.We have demonstrated that the strongly deformed toric code state|ψ​(β)⟩\ket{\psi(\beta)}admits a local and gapped parent HamiltonianH​(β)H(\beta)with|ψ​(β)⟩\ket{\psi(\beta)}as the unique ground state. SinceH​(β)H(\beta)is connected to the trivial HamiltonianH0H_{0}by a gap-preserving deformation, this result demonstrates that|ψ​(β)⟩\ket{\psi(\beta)}lies within the trivial phase for sufficiently largeβ\beta.
Although our cluster expansion techniques only prove thatH​(β)H(\beta)is local and gapped at largeβ\beta, it is natural to conjecture that the entireβ>βc\beta>\beta_{c}regime realizes a trivial phase with a corresponding gapped parent Hamiltonian.

An immediate corollary of our result is that, within the space of Hamiltonians exhibiting exponentially decaying interactions [see Eq. (15)], perimeter-law decay of Wilson loops is not a reliable diagnostic of 1-form SSB. In the presence of an exact 1-form symmetry, it is commonly argued[20,37]that a perimeter-law Wilson loop can be “locally dressed” into an additional topological operator that braids nontrivially with the 1-form symmetry, resulting in topological order and ground-state degeneracy on the torus. Our construction demonstrates that this intuition fails in the deformed toric code states. A natural question is whether there might be more robust diagnostics of 1-form SSB at the level of individual states, i.e., without reference to a particular parent Hamiltonian.

The techniques developed in this work also shed light on the mixed-state separability of the stronglydecoheredtoric code. Previously, Refs.12,47demonstrated that the toric code under strong Pauli-ZZdecoherence can be expressed as an incoherent mixture of topologically trivial pure states with condensedmmanyons. These states are structurally similar to the deformed toric code states, and given the results of Ref.40, one might wonder whether they are intrinsically gapless. As described in the End Matter, and elaborated in the Supplemental Material[5], one can construct exact gapped parent Hamiltonians for these states at large decoherence strengths by an identical procedure as for the deformed toric code. This result completes the argument of Refs.12,47into a rigorous proof that the stronglyZZ-decohered toric code is separable, i.e., can be written as a convex sum of short-range entangled pure states.

From a dual perspective, our result also demonstrates that gapped Ising-symmetric wavefunctions can simultaneously exhibit long-range ferromagnetic correlations and perimeter-law disorder parameter correlations. Conventionally, when a gapped Hamiltonian exhibits a spontaneously broken global (0-form) Ising symmetry, its symmetric ground state exhibits long-range order parameter correlations andarea-lawdisorder parameter correlations. Indeed, a no-go theorem[35]rules out the coexistence of long-range order parameter and long-range disorder parameter correlations in 1D, and a recent result[36]demonstrates thatexponential-in-volumelocal perturbations to the 2D ferromagnetic Ising fixed point result in area-law disorder parameters. In contrast, the strongly deformed toric code state|ψ00​(β)⟩\ket{\psi_{00}(\beta)}is dual to a ferromagnetic ground state|φ​(β)⟩\ket{\varphi(\beta)}with perimeter-law disorder parameters, and our gapped parent HamiltonianH(00)​(β)H^{(00)}(\beta)is correspondingly dual to a gapped Ising-symmetric parent HamiltonianHdual​(β)H_{\text{dual}}(\beta)for|φ​(β)⟩\ket{\varphi(\beta)}; see the End Matter for details. Interestingly, althoughHdual​(β)H_{\text{dual}}(\beta)satisfies the exponential-in-diameter locality bound of Eq. (15), itfailsto satisfy the more stringent exponential-in-volume locality criterion. We expect that with a restriction to exponential-in-volume local Hamiltonians, long-range order parameters and area-law disorder parameters cannot coexist in a gapped ground state.

Our results highlight that the specific notion of locality imposed on the space of allowed Hamiltonians is a subtle but physically consequential choice in the classification of gapped quantum phases. It is particularly interesting to consider whether a more restrictive notion of locality can resurrect the correspondence between perimeter-law Wilson loops, 1-form SSB, and topological order. Crucially, the exponential-in-volume locality criterion previously discussed is insufficient for this purpose: in the Supplemental Material[5], we show that our parent HamiltoniansH​(β)H(\beta)andH(00)​(β)H^{(00)}(\beta)satisfy even these locality bounds. Inspired by the dual Ising parent Hamiltonian, perhaps the physically correct notion of locality in 1-form symmetric systems requires the suppression of Wilson loop operatorsXℒX_{\mathcal{L}}not by the volume|ℒ|\absolutevalue{\mathcal{L}}of their support, but by the area of the region they bound. Alternatively, it may be preferable to focus on Hamiltonian-agnostic criteria for gapped phases, such as the (approximate) entanglement bootstrap axioms[42,43,27]. Given that the deformed toric code states satisfy these axioms as well[5], it is interesting to ask whether there might exist a stronger Hamiltonian-agnostic definition of a gapped state which restores the intrinsic gaplessness of these funky states.

Note added:During the completion of this work, we became aware of a forthcoming work by Sahay, Zhang, von Keyserlingk, and Verresen that overlaps in part with the mixed state results of this work. Where our results overlap they agree.

Acknowledgements.We thank Rahul Sahay for inspiring discussions and introducing us to this problem. We also thank Tarun Grover, Ethan Lake, Anton Kapustin, John McGreevy, Spyridon Michalakis, Olexei Motrunich, Zohar Nussinov, Daniel Ranard, Ruben Verresen, Curt von Keyserlingk, and Carolyn Zhang for helpful discussions and comments. This work was primarily supported by the U.S. Department of Energy, Office of Science, National Quantum Information Science Research Centers, Quantum Science Center. We also acknowledge funding provided by the Institute for Quantum Information and Matter, an NSF Physics Frontiers Center (NSF Grant PHY-2317110).

## References
- [1]Note:Since there is no constraint that the loops be homologically trivial, Eq. (3) sums over all periodic and anti-periodic boundary conditions for the 2D Ising model.Cited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [2]Note:Although Refs.6and7assume anL×LL\times Ltorus in their proofs, the proof generalizes to arbitrary aspect ratio with no changes.Cited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [3]Note:We note that the expectation values of Wilson loops oriented in thex​τx\tauory​τy\tauplanes in Euclidean spacetime, defined via imaginary time evolution byH​(β)H(\beta), displayarea-lawscaling. Creating twoeeanyons from the ground state costs energy proportional to their separation, although this is not reflected in thex​yxy-oriented Wilson loops.Cited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [4]Note:The two locality bounds (14) and (15) are equivalent; see the Supplemental Material[5]for a simple proof.Cited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [5]Note:See the Supplemental Material, which contains Refs.[33,30,44,50,14,15,16,18], for further details of the cluster expansion, details of the proof of locality for the parent Hamiltonian (including exponential-in-volume locality), a detailed discussion of the parent Hamiltonian for the deformed toric code in the ‘00’ sector, equivalence of locality bounds (14) and (15), a discussion showing that the strongly deformed toric code satisfies approximate entanglement bootstrap axioms, and a proof that the strongly Pauli-ZZdecohered toric code is short-range entangled.Cited by:§I,§I,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,4.
- [6]S. Bravyi, M. B. Hastings, and S. Michalakis(2010-09)Topological quantum order: Stability under local perturbations.J. Math. Phys.51(9),pp. 093512–093512.External Links:DocumentCited by:§SIII,§SVI,Definition 2,Theorem 2,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,2.
- [7]S. Bravyi and M. B. Hastings(2011-11)A Short Proof of Stability of Topological Order under Local Perturbations.Commun. Math. Phys.307(3),pp. 609–627.External Links:DocumentCited by:§SIII,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,2.
- [8]F.J. Burnell(2018-03)Anyon Condensation and Its Applications.Annu. Rev. Condens. Matter Phys.9(1),pp. 307–327.External Links:ISSN 1947-5462,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [9]C. Castelnovo and C. Chamon(2008-02)Quantum topological phase transition at the microscopic level.Phys. Rev. B77,pp. 054433.External Links:Document,LinkCited by:§SIX,§SIX,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [10]X. Chen, Z. Gu, and X. Wen(2010-10)Local unitary transformation, long-range quantum entanglement, wave function renormalization, and topological order.Phys. Rev. B82,pp. 155138.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [11]X. Chen, Z. Gu, and X. Wen(2011-01)Classification of gapped symmetric phases in one-dimensional spin systems.Phys. Rev. B83,pp. 035107.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [12]Y. Chen and T. Grover(2024-04)Separability Transitions in Topological States Induced by Local Decoherence.Phys. Rev. Lett.132(17),pp. 170602.External Links:ISSN 1079-7114,LinkCited by:§I,§SVIII.1,§SVIII.1,§SVIII.1,§SVIII.1,§SVIII,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [13]J. I. Cirac, D. Pérez-García, N. Schuch, and F. Verstraete(2021-12)Matrix product states and projected entangled pair states: concepts, symmetries, theorems.Rev. Mod. Phys.93,pp. 045003.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [14]W. De Roeck, V. Khemani, Y. Li, N. O’Dea, and T. Rakovszky(2025-08)Low-Density Parity-Check Stabilizer Codes as Gapped Quantum Phases: Stability under Graph-Local Perturbations.PRX Quantum6(3),pp. 030330.External Links:ISSN 2691-3399,LinkCited by:§I,§SVII,5.
- [15]E. Dennis, A. Kitaev, A. Landahl, and J. Preskill(2002-09)Topological quantum memory.J. Math. Phys.43(9),pp. 4452–4505.External Links:ISSN 0022-2488,Link,DocumentCited by:§I,§SVIII.1,§SVIII.1,5.
- [16]R. Fan, Y. Bao, E. Altman, and A. Vishwanath(2024-05)Diagnostics of Mixed-State Topological Order and Breakdown of Quantum Memory.PRX Quantum5(2),pp. 020343.External Links:Link,DocumentCited by:§I,§SVIII.1,5.
- [17]R. Fernández and A. Procacci(2007-08)Cluster Expansion for Abstract Polymer Models. New Bounds from an Old Approach.Commun. Math. Phys.274(1),pp. 123–140.External Links:DocumentCited by:§SIV,§SIV,Lemma 4,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [18]E. Fradkin and J. E. Moore(2006-08)Entanglement entropy of 2d conformal quantum critical points: hearing the shape of a quantum drum.Phys. Rev. Lett.97,pp. 050404.External Links:Document,LinkCited by:§SIX,5.
- [19]S. Friedli and Y. Velenik(2017)Cluster expansion.InStatistical Mechanics of Lattice Systems: A Concrete Mathematical Introduction,pp. 232–261.External Links:LinkCited by:§I,§SII.2,§SII,§SIV,§SV,Theorem 1,Theorem 1,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [20]D. Gaiotto, A. Kapustin, N. Seiberg, and B. Willett(2015-02)Generalized global symmetries.J. High Energy Phys.2015,pp. 172.External Links:DocumentCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [21]F. D. M. Haldane(1983-02)Continuum dynamics of the 1-D Heisenberg antiferromagnet: Identification with the O(3) nonlinear sigma model.Phys. Lett. A93(9),pp. 464–468.External Links:DocumentCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [22]F. D. M. Haldane(1983-04)Nonlinear field theory of large-spin heisenberg antiferromagnets: semiclassically quantized solitons of the one-dimensional easy-axis Néel state.Phys. Rev. Lett.50,pp. 1153–1156.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [23]M. B. Hastings and T. Koma(2006-08)Spectral Gap and Exponential Decay of Correlations.Commun. Math. Phys.265(3),pp. 781–804.External Links:DocumentCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [24]M. B. Hastings(2010)Locality in quantum systems.arXiv:1008.5137.External Links:LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [25]J. Huxford, D. X. Nguyen, and Y. B. Kim(2023)Gaining insights on anyon condensation and 1-form symmetry breaking across a topological phase transition in a deformed toric code model.SciPost Phys.15,pp. 253.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [26]M. Kardar(2007)Statistical physics of fields.Cambridge University Press,Cambridge ; New York.External Links:ISBN 978-0-521-87341-3,LCCN QC793.3.F5 K37 2007,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [27]I. H. Kim, T. Lin, D. Ranard, and B. Shi(2024)Strict area law implies commuting parent Hamiltonian.arXiv:2404.05867.External Links:LinkCited by:§SIX,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [28]A.Yu. Kitaev(2003-01)Fault-tolerant quantum computation by anyons.Ann. Phys.303(1),pp. 2–30.External Links:ISSN 00034916,Link,DocumentCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [29]A. Kitaev and J. Preskill(2006-03)Topological Entanglement Entropy.Phys. Rev. Lett.96(11),pp. 110404.External Links:DocumentCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [30]J. Kleinberg and É. Tardos(2006)Algorithm design.Pearson/Addison-Wesley,Boston.External Links:ISBN 0-321-29535-8Cited by:§SIV,§SIV,5.
- [31]J. B. Kogut(1979-10)An introduction to lattice gauge theory and spin systems.Rev. Mod. Phys.51,pp. 659–713.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [32]R. Kotecký and D. Preiss(1986)Cluster expansion for abstract polymer models.Commun. Math. Phys.103(3),pp. 491–498.External Links:Document,Link,ISSN 1432-0916Cited by:§SII.2,§SIV,§SIV,Lemma 2,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [33]J. B. Kruskal(1956)On the shortest spanning subtree of a graph and the traveling salesman problem.Proc. Am. Math. Soc.7(1),pp. 48–50.External Links:DocumentCited by:§SIV,§SIV,5.
- [34]M. Levin and X. Wen(2006-03)Detecting Topological Order in a Ground State Wave Function.Phys. Rev. Lett.96(11),pp. 110405.External Links:DocumentCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [35]M. Levin(2020-07)Constraints on Order and Disorder Parameters in Quantum Spin Chains.Commun. Math. Phys.378(2),pp. 1081–1106.External Links:ISSN 1432-0916,LinkCited by:§I,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [36]B. T. McDonough, C. Yin, A. Lucas, and C. Zhang(2025-11)Lieb-Robinson Bounds with Exponential-in-Volume Tails.PRX Quantum6(4),pp. 040322.External Links:ISSN 2691-3399,LinkCited by:§I,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [37]J. McGreevy(2023-03)Generalized Symmetries in Condensed Matter.Annu. Rev. Condens. Matter Phys.14,pp. 57–82.External Links:DocumentCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [38]S. Östlund and S. Rommer(1995-11)Thermodynamic limit of density matrix renormalization.Phys. Rev. Lett.75,pp. 3537–3540.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [39]O. Penrose(1967)Convergence of fugacity expansions for classical systems.InStatistical Mechanics: Foundations and Applications,A. Bak (Ed.),pp. 101–109.Cited by:§SII.2,§SIV,§SIV,Lemma 1,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [40]R. Sahay, C. von Keyserlingk, R. Verresen, and C. Zhang(2025)Enforced Gaplessness from States with Exponentially Decaying Correlations.arXiv:2503.01977.External Links:LinkCited by:§I,§SI,§SV.2,§SV,§SV,§SVIII.1,§SVIII.3,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [41]N. Schuch, D. Pérez-García, and I. Cirac(2011-10)Classifying quantum phases using matrix product states and projected entangled pair states.Phys. Rev. B84,pp. 165139.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [42]B. Shi, K. Kato, and I. H. Kim(2020-07)Fusion rules from entanglement.Ann. Phys.418,pp. 168164.External Links:ISSN 0003-4916,LinkCited by:§SIX,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [43]B. Shi and I. H. Kim(2021-03)Entanglement bootstrap approach for gapped domain walls.Phys. Rev. B103(11),pp. 115150.External Links:DocumentCited by:§SIX,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [44]D. Ueltschi(2003)Cluster expansions and correlation functions.arXiv:math-ph/0304003.External Links:LinkCited by:§SIV,5.
- [45]F. Verstraete and J. I. Cirac(2006-03)Matrix product states represent ground states faithfully.Phys. Rev. B73,pp. 094423.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [46]G. Vidal(2003-10)Efficient classical simulation of slightly entangled quantum computations.Phys. Rev. Lett.91,pp. 147902.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [47]T. Wang, M. Song, Z. Y. Meng, and T. Grover(2025-03)Analog of Topological Entanglement Entropy for Mixed States.PRX Quantum6(1),pp. 010358.External Links:ISSN 2691-3399,LinkCited by:§SVIII.1,§SVIII,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [48]F. J. Wegner(1971-10)Duality in Generalized Ising Models and Phase Transitions without Local Order Parameters.J. Math. Phys.12(10),pp. 2259–2272.External Links:ISSN 1089-7658,LinkCited by:§I,Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [49]S. R. White(1992-11)Density matrix formulation for quantum renormalization groups.Phys. Rev. Lett.69,pp. 2863–2866.External Links:Document,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.
- [50]C. Yin and A. Lucas(2025-08)Low-Density Parity-Check Codes as Stable Phases of Quantum Matter.PRX Quantum6(3),pp. 030329.External Links:ISSN 2691-3399,LinkCited by:§I,§SVII,5.
- [51]J. Zinn-Justin(2021)Quantum field theory and critical phenomena.Fifth edition edition,International Series of Monographs on Physics,Oxford University Press,New York, NY.External Links:ISBN 978-0-19-883462-5,LCCN QC174.45 .Z56 2021,LinkCited by:Gapped Parent Hamiltonians for the Strongly Deformed Toric Code.

## IEnd Matter

Exact expression for the parent Hamiltonian.We now provide exact expressions for the coefficientsf​(𝒞)f(\mathcal{C})appearing in Eq. (12), thereby fully specifying the parent HamiltonianH​(β)H(\beta)for the strongly deformed toric code|ψ​(β)⟩=eW​|0⟩\ket{\psi(\beta)}=e^{W}\ket{0}at largeβ\beta. In our derivation we wroteW=log⁡𝒵=∑𝒞f​(𝒞)​X𝒞,W=\log\mathcal{Z}=\sum_{\mathcal{C}}f(\mathcal{C})X_{\mathcal{C}},(16)

where𝒵\mathcal{Z}is the polymer-model partition function in Eq. (10). The weights and hard-core interaction parameters in𝒵\mathcal{Z}respectively readw​(γ)=e−β​|γ|​Xγ,δ​(γ,γ′)={0γ,γ′​intersect1otherwise,w(\gamma)=e^{-\beta\absolutevalue{\gamma}}X_{\gamma},\,\,\,\delta(\gamma,\gamma^{\prime})=\begin{cases}0&\gamma,\gamma^{\prime}\text{ intersect}\\
1&\text{otherwise}\end{cases},(17)

whereXγ=∏e∈γXeX_{\gamma}=\prod_{e\in\gamma}X_{e}, and two polymersγ,γ′\gamma,\gamma^{\prime}intersect if there exists edgese∈γe\in\gammaande′∈γ′e^{\prime}\in\gamma^{\prime}such thate,e′e,e^{\prime}share a vertex on the square lattice. (For example, this convention counts a ‘figure 8’ as a single polymer, rather than two intersecting polymers.)

The Mayer cluster expansion[19]rewrites the polymer free energyWWas a sum over connected clusters𝒞\mathcal{C}, allowing us to extractf​(𝒞)f(\mathcal{C})through the right side of Eq. (16). Specifically,
the cluster expansion provides the decompositionlog⁡𝒵=∑n=1∞∑γ1,…,γn∈Γφ​(γ1,…,γn)​∏i=1nw​(γi).\log\mathcal{Z}=\sum_{n=1}^{\infty}\sum_{\gamma_{1},\dots,\gamma_{n}\in\Gamma}\varphi(\gamma_{1},\dots,\gamma_{n})\prod_{i=1}^{n}w(\gamma_{i}).(18)

HereΓ\Gammadenotes the set of all possible polymersγ\gamma, whileφ\varphiareUrsell functions, defined asφ​(γ)=1\varphi(\gamma)=1andφ​(γ1,…,γn)=1n!​∑G∈𝒢nc∏(i,j)∈E​(G)[δ​(γi,γj)−1]\varphi(\gamma_{1},\dots,\gamma_{n})=\frac{1}{n!}\sum_{G\in\mathcal{G}_{n}^{c}}\prod_{(i,j)\in{E(G)}}\left[\delta(\gamma_{i},\gamma_{j})-1\right](19)

forn>1n>1. The sum is performed over allconnectedgraphsGGonnnvertices{1,…,n}\{1,\ldots,n\}, with𝒢nc\mathcal{G}^{c}_{n}the set of all such connected graphs, andE​(G)E(G)the edge set ofGG. Note that if the polymersγ1,…,γn\gamma_{1},\dots,\gamma_{n}have any mutually non-intersecting bipartition, then for any connected graphG∈𝒢ncG\in\mathcal{G}^{c}_{n}, there will always be an edge(i,j)∈E​(G)(i,j)\in E(G)such thatδ​(γi,γj)−1=0\delta(\gamma_{i},\gamma_{j})-1=0, ensuring thatφ​(γ1,…,γn)=0\varphi(\gamma_{1},\dots,\gamma_{n})=0. Therefore, we can restrict the sum over polymers in Eq. (18) toconnectedsets of polymers—i.e., connected clusters—that we compactly label by𝒞=(γ1,…,γn)\mathcal{C}=(\gamma_{1},\ldots,\gamma_{n}), wherenncan range from11to∞\infty.
We can then writelog⁡𝒵=∑𝒞φ​(𝒞)​∏i=1length​(𝒞)w​(γi),\log\mathcal{Z}=\sum_{\mathcal{C}}\varphi(\mathcal{C})\prod_{i=1}^{\text{length}(\mathcal{C})}w(\gamma_{i}),(20)

and read off, with the aid of Eq. (16), the coefficientsf​(𝒞)=φ​(𝒞)​∏i=1length​(𝒞)e−β​|γi|f(\mathcal{C})=\varphi(\mathcal{C})\prod_{i=1}^{\text{length}(\mathcal{C})}e^{-\beta\absolutevalue{\gamma_{i}}}(21)

that define our parent HamiltonianH​(β)H(\beta)[see Eq. (12)].

Dual Ising Wavefunction.From a dual description, our construction demonstrates that long-range ferromagnetic order and perimeter-law disorder parameter correlations can coexist in a gapped ground state. Explicitly, the no-go state|ψ00​(β)⟩\ket{\psi_{00}(\beta)}is related by Wegner duality to the Ising wavefunction|φ​(β)⟩=exp⁡{β2​∑⟨p​q⟩Zp​Zq}​|+⟩,\ket{\varphi(\beta)}=\exp\quantity{\frac{\beta}{2}\sum_{\expectationvalue{pq}}Z_{p}Z_{q}}\ket{+},(22)

whereZp,XpZ_{p},X_{p}are a new set of Pauli operators defined on the dual lattice (i.e., at the centers of plaquettesp,qp,qof the original lattice), and|+⟩\ket{+}is the simultaneous+1+1eigenstate of eachXpX_{p}. This state is symmetric under theℤ2\mathbb{Z}_{2}symmetry∏pXp\prod_{p}X_{p}, and exhibits long-range ferromagnetic correlations⟨Zp​Zp′⟩∼𝒪​(1)\expectationvalue{Z_{p}Z_{p^{\prime}}}\sim\mathcal{O}(1)forβ>βc\beta>\beta_{c}; i.e., theℤ2\mathbb{Z}_{2}symmetry is spontaneously broken at largeβ\beta.

Conventional quantum ferromagnets, such as the 2D transverse-field Ising model, exhibitarea-lawscaling of the disorder parameter,⟨∏p∈ℛXp⟩∼e−α​|ℛ|\expectationvalue*{\prod_{p\in\mathcal{R}}X_{p}}\sim e^{-\alpha\absolutevalue{\mathcal{R}}}for a large 2D regionℛ\mathcal{R}. This scaling is especially natural from a “mean-field” perspective, where the ferromagnetic ground state is approximated as a symmetry-broken product state. In contrast,|φ​(β)⟩\ket{\varphi(\beta)}exhibitsperimeter-lawcorrelations of the disorder parameter,⟨∏p∈ℛXp⟩∼e−μ​|∂ℛ|\expectationvalue*{\prod_{p\in\mathcal{R}}X_{p}}\sim e^{-\mu\absolutevalue{\partial\mathcal{R}}}. Indeed, the latter operators are directly related to the Wilson loopsXℒX_{\mathcal{L}}of the deformed toric code via Wegner duality[48].

In 1D gapped ground states, a rigorous theorem[35]forbids the coexistence of long-range order parameter correlations and perimeter-law (i.e., long-ranged) disorder parameter correlations, and a natural question is whether a similar result can hold in two dimensions. Our parent HamiltonianH(00)​(β)H^{(00)}(\beta)for|ψ00​(β)⟩\ket{\psi_{00}(\beta)}is dual to aℤ2\mathbb{Z}_{2}-symmetric gapped parent HamiltonianHdual​(β)H_{\text{dual}}(\beta)with an exact two-fold degeneracy at largeβ\beta. This Hamiltonian demonstrates via counterexample that a result analogous to Ref.35cannot hold in 2D under the standard definition of local Hamiltonians, which allows for interactions decaying exponentially in theirdiameter[see Eq. (15)].

Recently, Ref.36proved that weakℤ2\mathbb{Z}_{2}-symmetric perturbations of the 2D ferromagnetic fixed point yield ferromagnetic ground states exhibiting area-law disorder parameters,⟨∏p∈ℛXp⟩∼e−α​|ℛ|\expectationvalue*{\prod_{p\in\mathcal{R}}X_{p}}\sim e^{-\alpha\absolutevalue{\mathcal{R}}}, so long as these perturbations exhibit interactions which decay exponentially with theirvolume. This result is consistent with our parent HamiltonianHdual​(β)H_{\text{dual}}(\beta), which violates this exponential-in-volume locality constraint. Indeed,Hdual​(β)H_{\text{dual}}(\beta)contains interaction terms of the form∏p∈ℛXp\prod_{p\in\mathcal{R}}X_{p}which are only suppressed in theirperimeter|∂ℛ|\absolutevalue{\partial\mathcal{R}}, rather than their volume|ℛ|\absolutevalue{\mathcal{R}}. It is natural to conjecture that long-range ferromagnetic order and perimeter-law disorder parameters cannot coexist in 2D gapped ground states of exponential-in-volume local Hamiltonians.

The Strongly Decohered Toric Code is Separable.Letρp=[∏eℰe]​(|TC⟩⟨TC|)\rho_{p}=[\prod_{e}\mathcal{E}_{e}](\outerproduct{\text{TC}}{\text{TC}})be the mixed state obtained by applying a phase-flip channelℰe​(ρ)=(1−p)​ρ+p​Ze​ρ​Ze\mathcal{E}_{e}(\rho)=(1-p)\rho+pZ_{e}\rho Z_{e}of strengthppto each qubit of a toric code state|TC⟩\ket{\text{TC}}. Such a mixed state is well-known to undergo a mixed-statedecodabilityphase transition[15,16]at a critical thresholdpc≈0.109p_{c}\approx 0.109, such that the initial state|TC⟩\ket{\text{TC}}can no longer be reliably recovered fromρp\rho_{p}forp>pcp>p_{c}. Reference12argued that this transition coincides with aseparabilityphase transition, whereuponρp\rho_{p}can be expressed as a convex sum of short-range entangled states forp>pcp>p_{c}. Specifically, letting the initial state|TC⟩\ket{\text{TC}}be the ‘++’ logical state, Ref.12demonstrated thatρp\rho_{p}admits a decomposition into a mixture of the states|ψℒ​(K)⟩=Xℒ​∑{xe=±1}𝒵KIsing​({xe})​|{xe}⟩x,\ket{\psi_{\mathcal{L}}(K)}=X_{\mathcal{L}}\sum_{\quantity{x_{e}=\pm 1}}\sqrt{\mathcal{Z}^{\text{Ising}}_{K}(\quantity{x_{e}})}\ket{\quantity{x_{e}}}_{x},(23)

whereK=−12​log⁡[p/(1−p)]K=-\frac{1}{2}\log[p/(1-p)],|{xe}⟩x\ket{\quantity{x_{e}}}_{x}are the Pauli-XXbasis states, and𝒵KIsing​({xe})=∑{sv}eK​∑⟨v​v′⟩xv​v′​sv​sv′\mathcal{Z}^{\text{Ising}}_{K}(\quantity{x_{e}})=\sum_{\quantity{s_{v}}}e^{K\sum_{\expectationvalue{vv^{\prime}}}x_{vv^{\prime}}s_{v}s_{v^{\prime}}}is the partition function of a bond-disordered Ising model with disorder realization{xe}\quantity{x_{e}}.

Similar to the deformed toric code state (2), the states|ψℒ​(K)⟩\ket{\psi_{\mathcal{L}}(K)}are 1-form symmetric under contractible loop operatorsZℒ~Z_{\tilde{\mathcal{L}}}, exhibit condensedmmanyons forp>pcp>p_{c}, but maintain perimeter-law Wilson loops for allp<12p<\frac{1}{2}. Therefore, although each|ψℒ​(K)⟩\ket{\psi_{\mathcal{L}}(K)}is topologically trivial forp>pcp>p_{c}, the results of Ref.40call into question whether these states are indeed short-range entangled. Using identical cluster expansion techniques to those described in the main text, we answer this question in the affirmative for sufficiently largep<12p<\frac{1}{2}[5].

Explicitly, recalling the expression for the operator𝒵\mathcal{Z}in the right-hand side of Eq. (7), we see that|ψℒ​(K)⟩\ket{\psi_{\mathcal{L}}(K)}can be rewritten as|ψℒ​(K)⟩∝Xℒ​𝒵​|0⟩=Xℒ​eW/2​|0⟩,\ket{\psi_{\mathcal{L}}(K)}\propto X_{\mathcal{L}}\sqrt{\mathcal{Z}}\ket{0}=X_{\mathcal{L}}e^{W/2}\ket{0},(24)

where we have used the simple identity𝒵​|{xe}⟩x=𝒵KIsing​({xe})​|{xe}⟩x\mathcal{Z}\ket{\quantity{x_{e}}}_{x}=\mathcal{Z}^{\text{Ising}}_{K}(\quantity{x_{e}})\ket{\quantity{x_{e}}}_{x}[see Eq. (7)]. Using an identical approach as for the deformed toric code state|ψ​(β)⟩\ket{\psi(\beta)}, one can construct a local parent HamiltonianHℒ​(K)H_{\mathcal{L}}(K)for which|ψℒ​(K)⟩\ket{\psi_{\mathcal{L}}(K)}is the unique gapped ground state at sufficiently largepp. Applying the results of Ref.[50,14],|ψℒ​(K)⟩\ket{\psi_{\mathcal{L}}(K)}can be prepared via finite-time unitary evolution with a local generator, and is therefore short-range entangled.

In the Supplemental Material[5], we note that there is a minor subtlety when the ‘++’ initial state is replaced by a general toric code state|TC⟩\ket{\text{TC}}. For certain choices of|TC⟩\ket{\text{TC}}, the pure-state decomposition ofρp\rho_{p}is not completely trivial: instead, it contains an exponentially small (in trace norm) sector of gapless states. Such mixed statesρp\rho_{p}are thereforeapproximatelyseparable at largepp; in particular, they are indistinguishable from a corresponding separable state in the thermodynamic limit.

Classical High-Low Temperature Duality.Our rewriting of the deformed toric code state|ψ​(β)⟩=eW​|0⟩\ket{\psi(\beta)}=e^{W}\ket{0}as a deformation of the trivial paramagnet leads to a novel high/low temperature duality between the 2D classical Ising model and a 2D gauge theory with exponentially decaying interactions. This duality is valid at largeβ\beta, where the Ising model lies in a ferromagnetic phase and the dual gauge theory lies within a confined phase.

Recall first from Eq. (3) that the norm of|ψ​(β)⟩\ket{\psi(\beta)}can be expressed as the partition function of a 2D Ising model, where the loop configurationsℒ\mathcal{L}are understood as magnetic domain walls. On the other hand, by Eq. (11), the same norm can be written as⟨ψ​(β)|​|ψ​(β)⟩=⟨0|​e2​W​|0⟩=⟨0|​e2​∑𝒞f​(𝒞)​X𝒞​|0⟩.\bra{\psi(\beta)}\ket{\psi(\beta)}=\bra{0}e^{2W}\ket{0}=\bra{0}e^{2\sum_{\mathcal{C}}f(\mathcal{C})X_{\mathcal{C}}}\ket{0}.(25)

By expanding|0⟩∝∑{xe}|{xe}⟩x\ket{0}\propto\sum_{\quantity{x_{e}}}\ket{\quantity{x_{e}}}_{x}in the Pauli-XXbasis, we find that the 2D Ising partition function is proportional to the following dual partition function with Ising spinsxe=±1x_{e}=\pm 1on the edges of the square lattice:⟨ψ​(β)|​|ψ​(β)⟩∝∑{xe=±1}e2​∑𝒞f​(𝒞)​x𝒞,x𝒞=∏γ∈𝒞∏e∈γxe.\bra{\psi(\beta)}\ket{\psi(\beta)}\propto\sum_{\quantity{x_{e}=\pm 1}}e^{2\sum_{\mathcal{C}}f(\mathcal{C})x_{\mathcal{C}}},\quad x_{\mathcal{C}}=\prod_{\gamma\in\mathcal{C}}\prod_{e\in\gamma}x_{e}.(26)

This classical partition function is invariant under the localℤ2\mathbb{Z}_{2}symmetry transformationxv​v′↦sv​xv​v′​sv′x_{vv^{\prime}}\mapsto s_{v}x_{vv^{\prime}}s_{v^{\prime}}, where we’ve writtenxv​v′≡xex_{vv^{\prime}}\equiv x_{e}fore=⟨v​v′⟩e=\expectationvalue{vv^{\prime}}, and{sv=±1}\quantity{s_{v}=\pm 1}. Consequently, the above partition function describes a pureℤ2\mathbb{Z}_{2}gauge theory. It is unclear whether this dual model can be extended to (or past) the critical point, since the cluster expansion generally fails to converge at sufficiently smallβ\beta.\do@columngrid

oneΔ††footnotetext:

nmanoj@caltech.edu


Supplemental Material For:
Gapped Parent Hamiltonians for the Strongly Deformed Toric Code

Nandagopal Manoj,*Zack Weinstein, and Jason Alicea

Department of Physics and Institute for Quantum Information and
Matter, California Institute of Technology, Pasadena, California 91125, USA

(Dated: )

This supplemental material describes the technical statements in the Letter in more detail and, wherever applicable, provides rigorous proofs and bounds.

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

## SISetup and Notation

We work on anLx×LyL_{x}\times L_{y}square latticeΛ\Lambdawith periodic boundary conditions, where we assumeLx≥LyL_{x}\geq L_{y}without loss of generality. The qubits live on the edges, labeled byee. We write Pauli operators acting on these qubits asXe,ZeX_{e},Z_{e}. We useℒ\mathcal{L}to denote closed (not necessarily connected) loop configurations in the direct lattice—that is,ℒ\mathcal{L}is a subset of edgeseesuch that each vertexv∈Λv\in\Lambdais incident to an even number of edges inℒ\mathcal{L}. For eachℒ\mathcal{L}, we define the operatorXℒ≡∏e∈ℒXe,X_{\mathcal{L}}\equiv\prod_{e\in{\mathcal{L}}}X_{e},(S1)

and denote by|ℒ|\absolutevalue{\mathcal{L}}the number of edges inℒ{\mathcal{L}}.

The deformed toric code states are defined as|ψ​(β)⟩∝eβ2​∑eZe​|TC⟩,\ket{\psi(\beta)}\propto e^{\frac{\beta}{2}\sum_{e}Z_{e}}\ket{\text{TC}},(S2)

where|TC⟩\ket{\text{TC}}is a simultaneous +1 eigenstate of the stabilizersAv≡∏e∋vZeA_{v}\equiv\prod_{e\ni v}Z_{e}andBp≡∏e∈pBpB_{p}\equiv\prod_{e\in p}B_{p}. In the main text, we primarily focused on the state obtained by deforming the ‘++’ logical state|TC++⟩\ket{\text{TC}_{++}}, given explicitly by|ψ++​(β)⟩∝eβ2​∑eZe​|TC++⟩∝∑ℒe−β​|ℒ|​Xℒ​|0⟩,\ket{\psi_{++}(\beta)}\propto e^{\frac{\beta}{2}\sum_{e}Z_{e}}\ket{\text{TC}_{++}}\propto\sum_{\mathcal{L}}e^{-\beta\absolutevalue{\mathcal{L}}}X_{\mathcal{L}}\ket{0},(S3)

where|0⟩\ket{0}is the simultaneous+1+1eigenstate of eachZeZ_{e}. In other words,|ψ++​(β)⟩\ket{\psi_{++}(\beta)}contains a superposition of all closed loops ofZe=−1Z_{e}=-1in the direct lattice, including both contractible and non-contractible loops.

Similarly, the “no-go state” is obtained by deforming the ‘00’ logical state, and is given by|ψ00​(β)⟩∝eβ2​∑eZe​|TC00⟩∝∑ℒ=∂ℛe−β​|ℒ|​Xℒ​|0⟩.\ket{\psi_{00}(\beta)}\propto e^{\frac{\beta}{2}\sum_{e}Z_{e}}\ket{\text{TC}_{00}}\propto\sum_{{\mathcal{L}}=\partial\mathcal{R}}e^{-\beta\absolutevalue{\mathcal{L}}}X_{\mathcal{L}}\ket{0}.(S4)

This state contains only contractible loops in the superposition, and consequently satisfies the assumptions of Theorem 1 in Ref.40. We shall initially focus on the simpler state|ψ++​(β)⟩\ket{\psi_{++}(\beta)}, which we denote by|ψ​(β)⟩\ket{\psi(\beta)}to lighten the notation; we return to the no-go state|ψ00​(β)⟩\ket{\psi_{00}(\beta)}in Sec.SV.

Finally, we define the gapped parent Hamiltonian for the trivial product state|0⟩\ket{0}byH0=∑e(1−Ze),H_{0}=\sum_{e}(1-Z_{e}),(S5)

which hosts a unique ground state with the spectral gapΔ0=2\Delta_{0}=2.

## SIIPolymer models and Mayer Cluster Expansion

In order to construct parent a Hamiltonian for the state|ψ​(β)⟩\ket{\psi(\beta)}at largeβ\beta, it is insightful to view it as non-unitary deformation of the trivial state|0⟩\ket{0}. From Eqs. (S3) we have|ψ​(β)⟩=𝒵^​(β)​|0⟩\ket{\psi(\beta)}=\hat{\mathcal{Z}}(\beta)\ket{0}, where the operator𝒵^​(β)\hat{\mathcal{Z}}(\beta)is defined by𝒵^​(β)≡∑ℒe−β​|ℒ|​Xℒ.\hat{\mathcal{Z}}(\beta)\equiv\sum_{\mathcal{L}}e^{-\beta\absolutevalue{\mathcal{L}}}X_{\mathcal{L}}.(S6)

As described in the main text [see Eq. (7)], this operator can be expressed as the high-temperature expansion of a bond-disordered Ising model with coupling constantK=artanh⁡(e−β)K=\operatorname{artanh}(e^{-\beta}), and is therefore a positive-definite operator. Its logarithm,W^​(β)≡log⁡𝒵^​(β),\hat{W}(\beta)\equiv\log\hat{\mathcal{Z}}(\beta),(S7)

is therefore a well-defined Hermitian operator.

The locality of the parent HamiltonianH​(β)H(\beta)we will construct depends sensitively on the locality properties ofW^​(β)\hat{W}(\beta). Heuristically, sinceW^\hat{W}is the free energy of a bond-disordered Ising model, we expect it to be an extensive sum of terms which are exponentially localized at largeβ\beta. We will formally demonstrate this property using theMayer cluster expansion, described extensively in Ref.19. Here we review the basics of this series expansion.

## SII.1Polymer model definition

Apolymer, labeled byγ\gamma, is a collection of edges that form aconnectedclosed loop. Note that polymers can be self-intersecting, like a figure of eight. We defineΓ\Gammato be the set of all polymers on theLx×LyL_{x}\times L_{y}square lattice. Apolymer modelis defined by associating a complex weightw:Γ→ℂw:\Gamma\to\mathbb{C}to each polymer and a real symmetric interactionδ:Γ×Γ→[−1,1]\delta:\Gamma\times\Gamma\to[-1,1]to each pair of polymers. Given(Γ,w,δ)(\Gamma,w,\delta), the polymer partition function is defined as𝒵=∑Γ′⊆Γ[∏γ∈Γ′w​(γ)]​[∏{γ,γ′}⊆Γ′δ​(γ,γ′)].\mathcal{Z}=\sum_{\Gamma^{\prime}\subseteq\Gamma}\quantity[\prod_{\gamma\in\Gamma^{\prime}}w(\gamma)]\quantity[\prod_{\left\{\gamma,\gamma^{\prime}\right\}\subseteq\Gamma^{\prime}}\delta(\gamma,\gamma^{\prime})].(S8)

Throughout this work, we will largely focus on the weight functionw​(γ)=e−β​|γ|w(\gamma)=e^{-\beta|\gamma|}. To describe the operator-valued partition function (S6), we will later promotew​(γ)w(\gamma)to the operator-valued weight functionw^​(γ)≡e−β​|γ|​Xγ,\hat{w}(\gamma)\equiv e^{-\beta\absolutevalue{\gamma}}X_{\gamma},(S9)

whereXγ≡∏e∈γXeX_{\gamma}\equiv\prod_{e\in\gamma}X_{e}. These operators mutually commute, so we can regard the operator-valued partition function𝒵^​(β)\hat{\mathcal{Z}}(\beta)obtained from these weights as an ordinary polymer partition function within each simultaneous Pauli-XXeigenstate.

Finally, it will be sufficient to work with a hard-core interaction whereδ​(γ,γ′)∈{0,1}\delta(\gamma,\gamma^{\prime})\in\left\{0,1\right\}, defined presently111A slightly more intricate definition will be necessary to describe the no-go state; see Sec.SV.as follows:δ​(γ,γ′)={0,γ,γ′​intersect1,otherwise.\delta(\gamma,\gamma^{\prime})=\begin{cases}0,&\gamma,\gamma^{\prime}\text{ intersect}\\
1,&\text{otherwise}\end{cases}.(S10)

Two polymersγ,γ′\gamma,\gamma^{\prime}are defined as intersecting if there exists edgese∈γe\in\gammaande′∈γ′e^{\prime}\in\gamma^{\prime}such thate,e′e,e^{\prime}share a common vertex in the lattice. Note that by this definition, two diagonally adjacent polymers which touch at a single corner are considered intersecting. Loop configurations such as ‘figure-eights’ are therefore considered as a single polymer.

We say that two intersecting polymersγ,γ′\gamma,\gamma^{\prime}areincompatible, as if the subsetΓ′\Gamma^{\prime}in the partition sum contains two such polymers, the summand will be zero and will not contribute. We also say thatγ,γ′\gamma,\gamma^{\prime}arecompatible, ornon-interacting, ifδ​(γ,γ′)=1\delta(\gamma,\gamma^{\prime})=1.

## SII.2Cluster Expansion and Ursell Functions

Acluster𝒞\mathcal{C}is a finite non-empty sequence of polymers(γ1,γ2,…,γn)(\gamma_{1},\gamma_{2},\dots,\gamma_{n}), with repetitions allowed. A cluster is calleddisconnectedif there exists a partition of the integers{1,…,n}=I1⊔I2\{1,\ldots,n\}=I_{1}\sqcup I_{2}such that, for alli∈I1i\in I_{1}andj∈I2j\in I_{2},γi\gamma_{i}is compatible withγj\gamma_{j}(i.e.,δ​(γi,γj)=1\delta(\gamma_{i},\gamma_{j})=1); in other words, a disconnected cluster can be divided into two sub-clusters𝒞1\mathcal{C}_{1}and𝒞2\mathcal{C}_{2}such that eachγi∈𝒞1\gamma_{i}\in\mathcal{C}_{1}is compatible with eachγj∈𝒞2\gamma_{j}\in\mathcal{C}_{2}. Finally, a cluster isconnectedif it is not disconnected.

The Mayer cluster expansion[19,32,39]provides an explicit series expansion for the polymer free energyW=log⁡𝒵W=\log\mathcal{Z}as a sum over connected clusters:

## Theorem 1(Mayer Cluster Expansion[19]).

=

Given the polymer model(Γ,w,δ)(\Gamma,w,\delta)and the corresponding polymer partition function𝒵\mathcal{Z}[see Eq. (S8)], the polymer free energyW≡log⁡𝒵W\equiv\log\mathcal{Z}can be expressed as the following infinite series over clusters𝒞\mathcal{C}:W≡log⁡𝒵=∑𝒞f​(𝒞),f​(𝒞)≡φ​(γ1,…,γn)​∏i=1nw​(γi).W\equiv\log\mathcal{Z}=\sum_{\mathcal{C}}f(\mathcal{C}),\quad f(\mathcal{C})\equiv\varphi(\gamma_{1},\ldots,\gamma_{n})\prod_{i=1}^{n}w(\gamma_{i}).(S11)

Hereφ​(γ1,…,γn)\varphi(\gamma_{1},\ldots,\gamma_{n})is theUrsell function, defined for each cluster𝒞=(γ1,…,γn)\mathcal{C}=(\gamma_{1},\ldots,\gamma_{n})asφ​(γ1,…,γn)≡1n!​∑G∈𝒢nc∏(i,j)∈E​(G)ζ​(γi,γj),\varphi(\gamma_{1},\dots,\gamma_{n})\equiv\frac{1}{n!}\sum_{G\in\mathcal{G}^{c}_{n}}\prod_{(i,j)\in E(G)}\zeta(\gamma_{i},\gamma_{j}),(S12)

where𝒢nc\mathcal{G}^{c}_{n}is the set of all connected graphsGGwith vertex setV​(G)={1,…,n}V(G)=\{1,\ldots,n\},E​(G)E(G)is the edge set ofGG, andζ​(γ,γ′)≡δ​(γ,γ′)−1\zeta(\gamma,\gamma^{\prime})\equiv\delta(\gamma,\gamma^{\prime})-1, so thatζ​(γ,γ′)\zeta(\gamma,\gamma^{\prime})vanishes if the polymers are compatible. Forn=1n=1we defineφ​(γ1)=1\varphi(\gamma_{1})=1. Note that the Ursell functions vanish on disconnected clusters, and so we can restrict the sum in Eq. (S11) to connected clusters𝒞\mathcal{C}. For a derivation of Eq. (S11) and details on its convergence, we refer the reader to Ref.19.

We can apply the cluster expansion to Eq. (S6), using the weights (S9) and interactions (S10). As the weightsw^​(γ)\hat{w}(\gamma)are composed only ofXeX_{e}operators, we can ignore the operator nature of the weights by working in theXeX_{e}eigenbasis. Then, we haveW^​(β)≡log⁡𝒵^​(β)=∑n≥1∑γ1,…,γn∈Γφ​(γ1,…,γn)​∏i=1ne−β​|γi|​Xγi≡∑𝒞f​(𝒞)​X𝒞,\hat{W}(\beta)\equiv\log\hat{\mathcal{Z}}(\beta)=\sum_{n\geq 1}\sum_{\gamma_{1},\dots,\gamma_{n}\in\Gamma}\varphi(\gamma_{1},\dots,\gamma_{n})\prod_{i=1}^{n}e^{-\beta\absolutevalue{\gamma_{i}}}X_{\gamma_{i}}\equiv\sum_{\mathcal{C}}f(\mathcal{C})X_{\mathcal{C}},(S13)

whereX𝒞≡∏i=1nXγiX_{\mathcal{C}}\equiv\prod_{i=1}^{n}X_{\gamma_{i}}for any cluster𝒞=(γ1,…,γn)\mathcal{C}=(\gamma_{1},\ldots,\gamma_{n}). A crucial bound satisfied by these coefficientsf​(𝒞)f(\mathcal{C})is Eq. (13) in the main text (Lemma5). Since the proof of this bound is rather technical, we postpone its proof to AppendixSIV.

## SIIIProof of Locality and Spectral Gap

In this Appendix, we provide explicit technical details to prove that our parent HamiltonianH​(β)H(\beta)is local and exhibits a nonzero spectral gap at large values ofβ\beta. Our essential strategy is to use properties of the cluster expansion—specifically, the bound in Eq. (13) of the main text—to show thatH​(β)H(\beta)satisfies the locality properties demanded by the assumptions of Refs.6,7. The gap stability results of these works then immediately imply thatH​(β)H(\beta)is gapped at sufficiently largeβ\beta.

Let us first recall the derivation of our parent HamiltonianH​(β)H(\beta). We begin by using the cluster expansion to express the deformed toric code state|ψ​(β)⟩\ket{\psi(\beta)}as an exponential deformation of the trivial state|0⟩\ket{0}:|ψ​(β)⟩=𝒵^​(β)​|0⟩=eW^​(β)​|0⟩=exp⁡{∑𝒞f​(𝒞)​X𝒞}​|0⟩,\ket{\psi(\beta)}=\hat{\mathcal{Z}}(\beta)\ket{0}=e^{\hat{W}(\beta)}\ket{0}=\exp\quantity{\sum_{\mathcal{C}}f(\mathcal{C})X_{\mathcal{C}}}\ket{0},(S14)

c.f. Eqs. (S6) and (S13). As described in the main text, this form naturally motivates the construction of a frustration-free parent Hamiltonian as follows: we first define the manifestly positive-semidefinite Hermitian operatorsPe​(β)P_{e}(\beta)viaPe​(β)≡e−∑𝒞∈𝒮ef​(𝒞)​X𝒞​(1−Ze)​e−∑𝒞∈𝒮ef​(𝒞)​X𝒞=e−2​∑𝒞∈𝒮ef​(𝒞)​X𝒞−Ze,\begin{split}P_{e}(\beta)&\equiv e^{-\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}}(1-Z_{e})e^{-\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}}\\
&=e^{-2\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}}-Z_{e},\end{split}(S15)

where𝒮e\mathcal{S}_{e}denotes the set of connected clusters𝒞\mathcal{C}for whichX𝒞X_{\mathcal{C}}anticommutes withZeZ_{e}. EachPe​(β)P_{e}(\beta)clearly annihilates|ψ​(β)⟩\ket{\psi(\beta)}, and therefore the HamiltonianH​(β)≡∑ePe​(β)=∑e(e−2​∑𝒞∈𝒮ef​(𝒞)​X𝒞−Ze)H(\beta)\equiv\sum_{e}P_{e}(\beta)=\sum_{e}\quantity(e^{-2\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}}-Z_{e})(S16)

admits|ψ​(β)⟩\ket{\psi(\beta)}as a frustration-free ground state. In the same way that the Castelnovo-Chamon HamiltonianHCC​(β)H_{\text{CC}}(\beta)[see Eq. (6) of the main text] can be viewed as a deformation of the fixed-point toric code HamiltonianHTCH_{\text{TC}}, our parent HamiltonianH​(β)H(\beta)can be viewed as a deformation of the trivial HamiltonianH0=∑e(1−Ze)H_{0}=\sum_{e}(1-Z_{e}).

To prove a spectral gap, it will suffice to demonstrate thatH​(β)H(\beta)is exponentially localized at sufficiently largeβ\beta. More precisely, our goal is to writeH​(β)H(\beta)in the formH​(β)=H0+V,H(\beta)=H_{0}+V,(S17)

whereH0=∑e(1−Ze)H_{0}=\sum_{e}(1-Z_{e})is the trivial Hamiltonian, whileVVis a perturbation of the formV=∑r≥1∑A∈S​(r)Vr,A,V=\sum_{r\geq 1}\sum_{A\in S(r)}V_{r,A},(S18)

whereS​(r)S(r)is the set of allr×rr\times rsquares of lattice sites222For simplicity, we group the edgese=(v,v+x^)e=(v,v+\hat{x})ande=(v,v+y^)e=(v,v+\hat{y})together on the vertexvv, so that each vertex is regarded as hosting two qubits., andVr,AV_{r,A}is an operator supported on ther×rr\times rsquareAAwith a spectral norm bounded as‖Vr,A‖≤J​e−μ​r∀A∈S​(r)\norm{V_{r,A}}\leq Je^{-\mu r}\quad\forall A\in S(r)(S19)

for constantsJ,μ>0J,\mu>0to be determined. Note that this locality criterion is equivalent to that of Eq. (15) of the main text (see AppendixSVI). As we shall see, we will be able to chooseμ=1\mu=1andJ=J​(β)∝e−4​βJ=J(\beta)\propto e^{-4\beta}, so thatJ​(β)J(\beta)becomes exponentially small at largeβ\beta. The following theorem then guarantees that|ψ​(β)⟩\ket{\psi(\beta)}is the unique gapped ground state ofH​(β)H(\beta)with a nonvanishing spectral gap:

## Theorem 2(Stability of Gap[6]).

There exist constantsJ0,c1>0J_{0},c_{1}>0depending only onμ\muand the spatial dimensionDD, such that for allJ≤J0J\leq J_{0}, the spectrum ofH0+VH_{0}+Vis contained (up to an overall energy shift) in the union of intervals∪k≥0Ik\cup_{k\geq 0}I_{k}, wherekkruns over the spectrum ofH0H_{0}andIkI_{k}is the closed intervalIk=[k​(1−c1​J)−δ,k​(1+c1​J)+δ]I_{k}=\left[k(1-c_{1}J)-\delta,k(1+c_{1}J)+\delta\right](S20)

for someδ\deltabounded byJJtimes a quantity decaying faster than any power of the system sizeLL.

We can ignoreδ\deltaas we are ultimately interested in the thermodynamic limit. This theorem tells us that the spectral gap ofH​(β)H(\beta)is lower-bounded by2−2​c1​J2-2c_{1}J, which is positive for sufficiently smallJJ.

## SIII.1Proving thatH​(β)H(\beta)is local

We now set out to prove thatH​(β)H(\beta)is local at sufficiently largeβ\beta, in the sense of Eqs. (S17), (S18), and (S19). Theorem2will then immediately imply the existence of a spectral gap at sufficiently large values ofβ\beta. The results of this section will crucially rely on the bound in Eq. (13) of the main text, which we repeat here for convenience: forβ>β∗=2+log⁡3\beta>\beta^{*}=2+\log 3, we have the inequality∑𝒞∈𝒮e|f​(𝒞)|≤Cclus​e−4​β,\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})}\leq C_{\mathrm{clus}}e^{-4\beta},(S21)

whereCclus≈5.115×103C_{\mathrm{clus}}\approx 5.115\times 10^{3}is a constant. Since the proof of this bound is rather technical, we defer it to AppendixSIV.

We begin by Taylor expanding the exponential in Eq. (S16) [justified by the bound in Eq. (S21)] to writeH​(β)=H0+∑e∑n≥1(−2)nn!​[∑𝒞∈𝒮ef​(𝒞)​X𝒞]n=H0+∑e∑n≥1(−2)nn!​∑𝒞1​…​𝒞n∈𝒮e∏j=1n[f​(𝒞j)​X𝒞j].\begin{split}H(\beta)&=H_{0}+\sum_{e}\sum_{n\geq 1}\frac{(-2)^{n}}{n!}\quantity[\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}]^{n}\\
&=H_{0}+\sum_{e}\sum_{n\geq 1}\frac{(-2)^{n}}{n!}\sum_{\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}}\prod_{j=1}^{n}\quantity[f(\mathcal{C}_{j})X_{\mathcal{C}_{j}}].\end{split}(S22)

Our goal is to express the second term above in the form of Eq. (S18). For each vertexvvand odd values ofrr, letAv​(r)∈S​(r)A_{v}(r)\in S(r)denote the set of vertices contained within ther×rr\times rsquare centered onvv. We then define the operatorVr,vV_{r,v}supported onAv​(r)A_{v}(r)viaVr,v≡∑e=(v,v+x^),(v,v+y^)∑n≥1(−2)nn!​∑𝒞1​…​𝒞n∈𝒮emaxj⁡‖𝒞j‖=r+1∏j=1n[f​(𝒞j)​X𝒞j],V_{r,v}\equiv\sum_{e=(v,v+\hat{x}),(v,v+\hat{y})}\sum_{n\geq 1}\frac{(-2)^{n}}{n!}\sum_{\begin{subarray}{c}\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}\\
\max_{j}\norm{\mathcal{C}_{j}}=r+1\end{subarray}}\prod_{j=1}^{n}[f(\mathcal{C}_{j})X_{\mathcal{C}_{j}}],(S23)

where‖𝒞‖≡∑γ∈𝒞|γ|\norm{\mathcal{C}}\equiv\sum_{\gamma\in\mathcal{C}}\absolutevalue{\gamma}denotes the total length of all polymers (including repetitions) contained in the cluster𝒞\mathcal{C}. In the above, we have restricted the sum over clusters𝒞1​…​𝒞n\mathcal{C}_{1}\ldots\mathcal{C}_{n}such that the maximum value of any‖𝒞j‖\norm{\mathcal{C}_{j}}is preciselyr+1r+1. It is straightforward to show333Indeed, the “worst-case scenario” arises when a cluster𝒞j\mathcal{C}_{j}consists of a single closed-loop polymer of width 1 and length⌊r/2⌋\lfloor r/2\rfloor, whose perimeter is preciselyr+1r+1.that with this restriction,Vr,vV_{r,v}is supported on ther×rr\times rsquareAv​(r)A_{v}(r). We then have the decomposition444Forr≥Ly=min⁡(Lx,Ly)r\geq L_{y}=\min(L_{x},L_{y}), one may worry that many different squaresAv​(r)∈S​(r)A_{v}(r)\in S(r)(namely, shifts ofvvin theyydirection) actually describe the same set of lattice points. This is not an issue, since the bound we will prove demonstrates that the spectral norms of resulting operatorsVr,vV_{r,v}are exponentially suppressed inr≥Lyr\geq L_{y}. By Weyl’s inequality, such terms cannot shift the eigenvalues ofH​(β)H(\beta)by more than ane−𝒪​(Ly)e^{-\mathcal{O}(L_{y})}amount, and we can therefore neglect them in proving the stability of the gap for sufficiently large system sizes.H​(β)=H0+∑v∑r≥3,oddVr,v,H(\beta)=H_{0}+\sum_{v}\sum_{r\geq 3,\text{odd}}V_{r,v},(S24)

which matches the desired form in Eq. (S18).

Next, we want to bound the spectral norm of eachVr,vV_{r,v}as in Eq. (S19). Since each∏jX𝒞j\prod_{j}X_{\mathcal{C}_{j}}has a spectral norm of 1, the triangle inequality immediately gives‖Vr,v‖\displaystyle\norm{V_{r,v}}≤∑e=(v,v+x^),(v,v+y^)∑n≥12nn!​∑𝒞1​…​𝒞n∈𝒮emaxj⁡‖𝒞j‖=(r+1)∏j=1n|f​(𝒞j)|\displaystyle\leq\sum_{e=\left(v,v+\hat{x}\right),\left(v,v+\hat{y}\right)}\sum_{n\geq 1}\frac{2^{n}}{n!}\sum_{\begin{subarray}{c}\mathcal{C}_{1}\dots\mathcal{C}_{n}\in\mathcal{S}_{e}\\
\max_{j}\norm{\mathcal{C}_{j}}=(r+1)\end{subarray}}\prod_{j=1}^{n}{\absolutevalue{f(\mathcal{C}_{j})}}(S25a)≤∑e=(v,v+x^),(v,v+y^)∑n≥12nn!​∑k=1n∑𝒞1​…​𝒞n∈𝒮e‖𝒞k‖=(r+1)∏j=1n|f​(𝒞j)|\displaystyle\leq\sum_{e=\left(v,v+\hat{x}\right),\left(v,v+\hat{y}\right)}\sum_{n\geq 1}\frac{2^{n}}{n!}\,\sum_{k=1}^{n}\,\sum_{\begin{subarray}{c}\mathcal{C}_{1}\dots\mathcal{C}_{n}\in\mathcal{S}_{e}\\
\norm{\mathcal{C}_{k}}=(r+1)\end{subarray}}\prod_{j=1}^{n}{\absolutevalue{f(\mathcal{C}_{j})}}(S25b)=∑e=(v,v+x^),(v,v+y^)∑n≥12n(n−1)!​(∑𝒞∈𝒮e‖𝒞‖=r+1|f​(𝒞)|)​(∑𝒞∈𝒮e|f​(𝒞)|)n−1.\displaystyle=\sum_{e=\left(v,v+\hat{x}\right),\left(v,v+\hat{y}\right)}\sum_{n\geq 1}\frac{2^{n}}{(n-1)!}\left(\sum_{\begin{subarray}{c}\mathcal{C}\in\mathcal{S}_{e}\\
\norm{\mathcal{C}}=r+1\end{subarray}}\absolutevalue{f(\mathcal{C})}\right)\left(\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})}\right)^{n-1}.(S25c)

To obtain Eq. (S25b), we replace the maximization over𝒞j\mathcal{C}_{j}with a sum over all possible𝒞k\mathcal{C}_{k}for which‖𝒞k‖=r+1\norm{\mathcal{C}_{k}}=r+1; Eq. (S25c) then follows immediately by noting that the summand for eachkkis identical.

The latter sum over clusters is immediately bounded using Eq. (S21). To bound the former sum over clusters, we note from Eq. (21) that|f​(𝒞)|=e−β​‖𝒞‖/2​|fβ/2​(𝒞)|\absolutevalue{f(\mathcal{C})}=e^{-\beta\norm{\mathcal{C}}/2}\absolutevalue{f_{\beta/2}(\mathcal{C})}, wherefβ/2​(𝒞)f_{\beta/2}(\mathcal{C})is the same functionf​(𝒞)f(\mathcal{C})evaluated at the deformation strengthβ/2\beta/2instead ofβ\beta. If we assume for simplicity thatβ≥2​β∗\beta\geq 2\beta^{*}, we can once again use Eq. (S21) to bound the former sum over clusters as follows:‖Vr,v‖\displaystyle\norm{V_{r,v}}≤∑e=(v,v+x^),(v,v+y^)∑n≥12n(n−1)!​(e−β​(r+1)/2​∑C∈𝒮e‖𝒞‖=r+1|fβ/2​(𝒞)|)​(∑C∈𝒮e|f​(𝒞)|)n−1\displaystyle\leq\sum_{e=(v,v+\hat{x}),(v,v+\hat{y})}\sum_{n\geq 1}\frac{2^{n}}{(n-1)!}\quantity(e^{-\beta(r+1)/2}\sum_{\begin{subarray}{c}C\in\mathcal{S}_{e}\\
\norm{\mathcal{C}}=r+1\end{subarray}}\absolutevalue{f_{\beta/2}(\mathcal{C})})\quantity(\sum_{C\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})})^{n-1}(S26a)≤2​e−β​(r+1)/2​(Cclus​e−2​β)​∑n≥12n(n−1)!​(Cclus​e−4​β)n−1\displaystyle\leq 2e^{-\beta(r+1)/2}\quantity(C_{\mathrm{clus}}e^{-2\beta})\sum_{n\geq 1}\frac{2^{n}}{(n-1)!}\quantity(C_{\mathrm{clus}}e^{-4\beta})^{n-1}(S26b)=4​e−β​r/2​Cclus​e−5​β/2​exp⁡[2​Cclus​e−4​β]\displaystyle=4e^{-\beta r/2}C_{\mathrm{clus}}e^{-5\beta/2}\exp[2C_{\mathrm{clus}}e^{-4\beta}](S26c)=(4​Cclus​e−4​β​exp⁡[2​Cclus​e−4​β])​e−β​(r−3)/2\displaystyle=\quantity(4C_{\mathrm{clus}}e^{-4\beta}\exp\quantity[2C_{\mathrm{clus}}e^{-4\beta}])e^{-\beta(r-3)/2}(S26d)≤(4​Cclus​e−4​β​exp⁡[2​Cclus​e−8​β∗])​e−(r−3),\displaystyle\leq\quantity(4C_{\mathrm{clus}}e^{-4\beta}\exp\quantity[2C_{\mathrm{clus}}e^{-8\beta^{*}}])e^{-(r-3)},(S26e)

where we’ve usedβ/2≥β∗≥1\beta/2\geq\beta^{*}\geq 1inside therr-dependent exponential, recalling thatr≥3r\geq 3. Altogether, we have proven the bound‖Vr,v‖≤J~​e−4​β​e−r,J~=4​Cclus​exp⁡[3+2​Cclus​e−8​β∗]≈4.11×105.\norm{V_{r,v}}\leq\tilde{J}e^{-4\beta}e^{-r},\quad\tilde{J}=4C_{\mathrm{clus}}\exp\quantity[3+2C_{\mathrm{clus}}e^{-8\beta^{*}}]\approx 4.11\times 10^{5}.(S27)

We have therefore proven that our parent HamiltonianH​(β)=H0+VH(\beta)=H_{0}+Vsatisfies the locality bound in Eq. (S18), withμ=1\mu=1. SinceJ​(β)≡J~​e−4​βJ(\beta)\equiv\tilde{J}e^{-4\beta}can be made arbitrarily small at largeβ\beta(eg. forβ=5,J​(β)≈10−3\beta=5,J(\beta)\approx 10^{-3}), it follows from Theorem2thatH​(β)H(\beta)is gapped and nondegenerate for sufficiently largeβ\beta. Moreover, sinceH​(β)H(\beta)is continuously connected to the trivial HamiltonianH0H_{0}by a gap-preserving deformation, we also find that|ψ​(β)⟩\ket{\psi(\beta)}lies in the trivial phase at largeβ\beta.

## SIVProof of Cluster Expansion Bound

Having proven the locality of our parent HamiltonianH​(β)H(\beta)utilizing the bound in Eq. (13) of the main text, we now return and demonstrate this bound. We will prove this result in several steps, using techniques which are standard to the cluster expansion[19,32,39,33,30,17].

## Lemma 1(Tree-graph identity for the Ursell function[39]).

For anyn≥1n\geq 1and polymersγ1,…,γn\gamma_{1},\dots,\gamma_{n}(repetitions allowed), the Ursell functions (S12) can be expressed as a sum over tree graphs as follows:φ​(γ1,…,γn)=1n!​∑T∈𝒯n(∏(i,j)∈E​(T)ζ​(γi,γj))​(∏(i,j)∈ℰextra​(T)δ​(γi,γj)),\varphi(\gamma_{1},\dots,\gamma_{n})=\frac{1}{n!}\sum_{T\in\mathcal{T}_{n}}\left(\prod_{(i,j)\in E(T)}\zeta(\gamma_{i},\gamma_{j})\right)\left(\prod_{(i,j)\in\mathcal{E}_{\text{extra}}(T)}\delta(\gamma_{i},\gamma_{j})\right),(S28)

where𝒯n\mathcal{T}_{n}is the set of spanning trees overnnlabeled vertices, andℰextra\mathcal{E}_{\mathrm{extra}}is defined below.

## Proof.

This result was first derived in Ref.39to show convergence of the cluster expansion. For completeness, we include a proof here.

First, we describe Kruskal’s algorithm[33,30], which constructs a unique spanning treeT∈𝒯nT\in\mathcal{T}_{n}given anyG∈𝒢ncG\in\mathcal{G}_{n}^{c}. We start by defining an ordering over all possible edges inGG(we will call this setEnE_{n}). We choose the ordering(1,2),(1,3),…,(1,n),(2,3),(2,4),…,(2,n),(3,4),…,(n−1,n).(1,2),\ (1,3),\ \dots,(1,n),\ (2,3),\ (2,4),\ \dots,\ (2,n),\ (3,4),\ \dots,\ (n-1,n).(S29)

Kruskal’s algorithm then defines a mapK:𝒢nc→𝒯nK:\mathcal{G}_{n}^{c}\to\mathcal{T}_{n}which goes through each link inG∈𝒢ncG\in\mathcal{G}_{n}^{c}in the above order, and adds the link to the resulting tree if it does not create a cycle, skipping the link otherwise. WhileKKassigns a uniqueT∈𝒯nT\in\mathcal{T}_{n}to eachG∈𝒢ncG\in\mathcal{G}^{c}_{n}, note thatKKis not injective; several different connected graphsGGare mapped to each treeTT.

Using Kruskal’s algorithm, we can reorder the sum asφ​(γ1,…,γn)\displaystyle\varphi(\gamma_{1},\dots,\gamma_{n})=1n!​∑T∈𝒯n∑G∈𝒢nc:K​(G)=T∏(i,j)∈E​(G)ζ​(γi,γj)\displaystyle=\frac{1}{n!}\sum_{T\in\mathcal{T}_{n}}\sum_{G\in\mathcal{G}_{n}^{c}:K(G)=T}\prod_{(i,j)\in E(G)}\zeta(\gamma_{i},\gamma_{j})(S30a)=1n!​∑T∈𝒯n(∏(i,j)∈E​(T)ζ​(γi,γj))​∑G∈𝒢nc:K​(G)=T∏(i,j)∈E​(G)∖E​(T)ζ​(γi,γj).\displaystyle=\frac{1}{n!}\sum_{T\in\mathcal{T}_{n}}\left(\prod_{(i,j)\in E(T)}\zeta(\gamma_{i},\gamma_{j})\right)\sum_{G\in\mathcal{G}_{n}^{c}:K(G)=T}\prod_{(i,j)\in E(G)\setminus E(T)}\zeta(\gamma_{i},\gamma_{j}).(S30b)

Next, consider the setE​(G)∖E​(T)E(G)\setminus E(T). By the construction of Kruskal’s algorithm, an edge is present inGGbut excluded fromTTif and only if its addition would create a cycle with the edges already selected. Consequently, there exists a set of edgesℰextra​(T)⊆En\mathcal{E}_{\text{extra}}(T)\subseteq E_{n}that would be skipped over in Kruskal’s algorithm for any input that resulted inTT. Therefore, instead of summing over all graphs such thatK​(G)=TK(G)=T, we can equivalently sum over all subsets ofℰextra​(T)\mathcal{E}_{\text{extra}}(T):∑G∈𝒢nc:K​(G)=T∏(i,j)∈E​(G)∖E​(T)ζ​(γi,γj)\displaystyle\sum_{G\in\mathcal{G}_{n}^{c}:K(G)=T}\prod_{(i,j)\in E(G)\setminus E(T)}\zeta(\gamma_{i},\gamma_{j})=∑ℰ⊆ℰextra​(T)∏(i,j)∈ℰζ​(γi,γj)\displaystyle=\sum_{\mathcal{E}\subseteq\mathcal{E}_{\text{extra}}(T)}\prod_{(i,j)\in\mathcal{E}}\zeta(\gamma_{i},\gamma_{j})(S31a)=∏(i,j)∈ℰextra​(T)[1+ζ​(γi,γj)]\displaystyle=\prod_{(i,j)\in\mathcal{E}_{\text{extra}}(T)}[1+\zeta(\gamma_{i},\gamma_{j})](S31b)=∏(i,j)∈ℰextra​(T)δ​(γi,γj),\displaystyle=\prod_{(i,j)\in\mathcal{E}_{\text{extra}(T)}}\delta(\gamma_{i},\gamma_{j}),(S31c)

from which Eq. (S28) follows.
∎

A useful feature of this rewriting is that every spanning treeT∈𝒯nT\in\mathcal{T}_{n}has preciselyn−1n-1edges; consequently, every term in Eq. (S28) contributes with the same sign [unlike the original expression in Eq. (S12)]. We therefore have the immediate corollary:|φ​(γ1,…,γn)|=1n!​∑T∈𝒯n(∏(i,j)∈E​(T)|ζ​(γi,γj)|)​(∏(i,j)∈ℰextra​(T)δ​(γi,γj)).\absolutevalue{\varphi(\gamma_{1},\ldots,\gamma_{n})}=\frac{1}{n!}\sum_{T\in\mathcal{T}_{n}}\quantity(\prod_{(i,j)\in E(T)}\absolutevalue{\zeta(\gamma_{i},\gamma_{j})})\quantity(\prod_{(i,j)\in\mathcal{E}_{\text{extra}}(T)}\delta(\gamma_{i},\gamma_{j})).(S32)

## Lemma 2(Kotecky-Preiss inequality[32]).

Whenβ≥β∗=2+log⁡3\beta\geq\beta^{\ast}=2+\log 3, the weightw​(γ)=e−β​|γ|w(\gamma)=e^{-\beta\absolutevalue{\gamma}}satisfies∑γ′≁γw​(γ′)​e|γ′|≤|γ|,\sum_{\gamma^{\prime}\nsim\gamma}w(\gamma^{\prime})e^{|\gamma^{\prime}|}\leq\absolutevalue{\gamma},(S33)

whereγ′≁γ\gamma^{\prime}\nsim\gammaindicates the sum is performed over all polymersγ′\gamma^{\prime}which are incompatible with the fixed polymerγ\gamma(i.e., such thatδ​(γ,γ′)=0\delta(\gamma,\gamma^{\prime})=0).

## Proof.

The number of polymers on the square lattice of lengthsscontaining a given vertexvvis upper bounded by3s3^{s}.
Therefore, the number of incompatibleγ′\gamma^{\prime}of fixed length|γ′|=s\absolutevalue{\gamma^{\prime}}=sis upper-bounded by|γ|​3s\absolutevalue{\gamma}3^{s}, sinceγ′\gamma^{\prime}has no more than|γ|\absolutevalue{\gamma}options where it can intersectγ\gamma. Then,∑γ′≁γw​(γ′)​e|γ′|\displaystyle\sum_{\gamma^{\prime}\nsim\gamma}w(\gamma^{\prime})e^{|\gamma^{\prime}|}≤∑s≥4,even|γ|​3s​e−β​s​es\displaystyle\leq\sum_{s\geq 4,\mathrm{even}}\absolutevalue{\gamma}3^{s}e^{-\beta s}e^{s}(S34a)=(3​e1−β)41−(3​e1−β)2​|γ|\displaystyle=\frac{(3e^{1-\beta})^{4}}{1-(3e^{1-\beta})^{2}}\absolutevalue{\gamma}(S34b)≤e−41−e−2​e−4​(β−β∗)​|γ|\displaystyle\leq\frac{e^{-4}}{1-e^{-2}}e^{-4(\beta-\beta^{\ast})}\absolutevalue{\gamma}(S34c)≤|γ|\displaystyle\leq\absolutevalue{\gamma}(S34d)

where the first sum converges as long asβ>β∗−1=1+log⁡3\beta>\beta^{\ast}-1=1+\log 3. The parameterβ∗\beta^{*}is chosen for convenience, so that the numerical prefactor is smaller than unity.
∎

## Lemma 3(Rooted tree recursion).

Define, for any polymerγ\gamma, the absolute rooted cluster weightg​(γ)=∑n≥1n​∑γ2,…,γn|φ​(γ,γ2,…,γn)|​∏i=1nw​(γi),γ1≡γ.g(\gamma)=\sum_{n\geq 1}n\sum_{\gamma_{2},\dots,\gamma_{n}}\absolutevalue{\varphi(\gamma,\gamma_{2},\dots,\gamma_{n})}\prod_{i=1}^{n}w(\gamma_{i}),\qquad\gamma_{1}\equiv\gamma.(S35)

Theng​(γ)g(\gamma)satisfies the recursive inequalityg​(γ)≤w​(γ)​e∑γ′≁γg​(γ′).g(\gamma)\leq w(\gamma)e^{\sum_{\gamma^{\prime}\nsim\gamma}g(\gamma^{\prime})}.(S36)

## Proof.

We refer the reader to[32,17,44]for detailed discussions (including regarding convergence), leaving only the essential derivation here. Using Eq. (S32), we haveg​(γ1)=∑n≥11(n−1)!​∑γ2,…,γn∑T∈𝒯n(∏(i,j)∈E​(T)|ζ​(γi,γj)|)​(∏(i,j)∈ℰextra​(T)δ​(γi,γj))​∏i=1nw​(γi).g(\gamma_{1})=\sum_{n\geq 1}\frac{1}{(n-1)!}\sum_{\gamma_{2},\dots,\gamma_{n}}\sum_{T\in\mathcal{T}_{n}}\left(\prod_{(i,j)\in E(T)}\absolutevalue{\zeta(\gamma_{i},\gamma_{j})}\right)\left(\prod_{(i,j)\in\mathcal{E}_{\text{extra}}(T)}\delta(\gamma_{i},\gamma_{j})\right)\prod_{i=1}^{n}w(\gamma_{i}).(S37)

To derive Eq. (S36), we regard each spanning treeT∈𝒯nT\in\mathcal{T}_{n}as arootedtree, with vertex 1 as the root. If vertex 1 is connected tokkother verticesc1,…,ckc_{1},\ldots,c_{k}by edges inE​(T)E(T), then removing vertex 1 splits the rooted tree intokkdisjoint rooted subtreesT1,…,TkT_{1},\ldots,T_{k}withTrT_{r}rooted atcrc_{r}. LettingVrV_{r}denote the vertex set ofTrT_{r}, we note thatV1,…,VkV_{1},\ldots,V_{k}forms a partition of{2,…,n}\{2,\ldots,n\}.

We now simplifyg​(γ1)g(\gamma_{1})as follows. First, we can write the product over edges(i,j)∈E​(T)(i,j)\in E(T)as∏(i,j)∈E​(T)|ζ​(γi,γj)|=∏r=1k[|ζ​(γ1,γcr)|​∏(i,j)∈E​(Tr)|ζ​(γi,γj)|].\prod_{(i,j)\in E(T)}\absolutevalue{\zeta(\gamma_{i},\gamma_{j})}=\prod_{r=1}^{k}\quantity[\absolutevalue{\zeta(\gamma_{1},\gamma_{c_{r}})}\prod_{(i,j)\in E(T_{r})}\absolutevalue{\zeta(\gamma_{i},\gamma_{j})}].(S38)

Similarly, the product over weights trivially factorizes:∏i=1nw​(γi)=w​(γ1)​∏r=1k∏i∈Vrw​(γi).\prod_{i=1}^{n}w(\gamma_{i})=w(\gamma_{1})\prod_{r=1}^{k}\prod_{i\in V_{r}}w(\gamma_{i}).(S39)

To handle the product overℰextra​(T)\mathcal{E}_{\text{extra}}(T), we will use the inequality∏(i,j)∈ℰextra​(T)δ​(γi,γj)≤∏r=1k∏(i,j)∈ℰextra​(Tr)δ​(γi,γj).\prod_{(i,j)\in\mathcal{E}_{\text{extra}}(T)}\delta(\gamma_{i},\gamma_{j})\leq\prod_{r=1}^{k}\prod_{(i,j)\in\mathcal{E}_{\text{extra}}(T_{r})}\delta(\gamma_{i},\gamma_{j}).(S40)

This inequality follows from noting thatℰextra​(Tr)⊆ℰextra​(T)\mathcal{E}_{\text{extra}}(T_{r})\subseteq\mathcal{E}_{\text{extra}}(T)for each subtreeTrT_{r}, so the former product contains extra delta functions which can cause the left-hand side to vanish. Finally, we organize the sum over treesT∈𝒯nT\in\mathcal{T}_{n}as a sum over all possible subtreesT1​…​TkT_{1}\ldots T_{k}: for some functionF​(T)F(T)which only depends on the graph structure ofTT(i.e.,F​(T)=F​(T′)F(T)=F(T^{\prime})for isomorphic treesT,T′T,T^{\prime}), we have∑T∈𝒯nF​(T)=∑k≥01k!​∑n1+…+nk=n−1(n−1)!n1!​…​nk!​n1​…​nk​∑T1∈𝒯n1…​∑Tk∈𝒯nkF​(T=(T1​…​Tk)),\sum_{T\in\mathcal{T}_{n}}F(T)=\sum_{k\geq 0}\frac{1}{k!}\sum_{n_{1}+\ldots+n_{k}=n-1}\frac{(n-1)!}{n_{1}!\ldots n_{k}!}n_{1}\ldots n_{k}\sum_{T_{1}\in\mathcal{T}_{n_{1}}}\ldots\sum_{T_{k}\in\mathcal{T}_{n_{k}}}F(T=(T_{1}\ldots T_{k})),(S41)

wherekksums over the number of possible subtrees, andn1​…​nkn_{1}\ldots n_{k}sums over the number of vertices in each subtree. The multinomial coefficient(n−1)!/n1!​…​nk!(n-1)!/n_{1}!\ldots n_{k}!counts the number of ways of sorting vertices{2,…,n}\{2,\ldots,n\}into thekksubtrees, and the factor1/k!1/k!accounts for the fact that the ordering of thekksubtrees is immaterial. The productn1​…​nkn_{1}\ldots n_{k}accounts for thenrn_{r}choices of root vertex in each subtree. Finally, the notationT=(T1​…​Tk)T=(T_{1}\ldots T_{k})indicates that the rooted treeT∈𝒯nT\in\mathcal{T}_{n}is constructed by joining the roots of the subtreesTrT_{r}as children to a new root.

Putting all of these facts together, we arrive at the inequalityg​(γ1)≤w​(γ1)​∑k≥01k!​∏r=1k[∑nr≥11(nr−1)!​∑γ1′​…​γnr′∑Tr∈𝒯nr|ζ​(γ1,γ1′)|​(∏(i,j)∈E​(Tr)|ζ​(γi′,γj′)|)​(∏(i,j)∈ℰextra​(Tr)δ​(γi′,γj′))​∏i=1nrw​(γi′)]=w​(γ1)​∑k≥01k!​∏r=1k[∑γ1′|ζ​(γ1,γ1′)|​g​(γ1′)]=w​(γ1)​exp⁡{∑γ1′|ζ​(γ1,γ1′)|​g​(γ1′)}.\begin{split}g(\gamma_{1})&\leq w(\gamma_{1})\sum_{k\geq 0}\frac{1}{k!}\prod_{r=1}^{k}\quantity[\sum_{n_{r}\geq 1}\frac{1}{(n_{r}-1)!}\sum_{\gamma_{1}^{\prime}\ldots\gamma_{n_{r}}^{\prime}}\sum_{T_{r}\in\mathcal{T}_{n_{r}}}\absolutevalue{\zeta(\gamma_{1},\gamma_{1}^{\prime})}\quantity(\prod_{(i,j)\in E(T_{r})}\absolutevalue{\zeta(\gamma_{i}^{\prime},\gamma_{j}^{\prime})})\quantity(\prod_{(i,j)\in\mathcal{E}_{\text{extra}}(T_{r})}\delta(\gamma_{i}^{\prime},\gamma_{j}^{\prime}))\prod_{i=1}^{n_{r}}w(\gamma_{i}^{\prime})]\\
&=w(\gamma_{1})\sum_{k\geq 0}\frac{1}{k!}\prod_{r=1}^{k}\quantity[\sum_{\gamma_{1}^{\prime}}\absolutevalue{\zeta(\gamma_{1},\gamma_{1}^{\prime})}g(\gamma_{1}^{\prime})]\\
&=w(\gamma_{1})\exp\quantity{\sum_{\gamma_{1}^{\prime}}\absolutevalue{\zeta(\gamma_{1},\gamma_{1}^{\prime})}g(\gamma_{1}^{\prime})}.\end{split}(S42)

Finally noting that|ζ​(γ1,γ1′)|\absolutevalue{\zeta(\gamma_{1},\gamma_{1}^{\prime})}is unity whenγ1≁γ1′\gamma_{1}\nsim\gamma_{1}^{\prime}and zero otherwise, we arrive at Eq. (S36).

∎

## Lemma 4(Absolute rooted cluster bound[17]).

The absolute rooted cluster weight is bounded above asg​(γ)≤w​(γ)​e|γ|.g(\gamma)\leq w(\gamma)e^{|\gamma|}.(S43)

## Proof.

We begin by defining, for any functionh:Γ→ℝh:\Gamma\to\mathbb{R}on the polymers, a new function𝒥​[h]:Γ→ℝ\mathcal{J}[h]:\Gamma\to\mathbb{R}as follows:𝒥​[h]​(γ)≡w​(γ)​e∑γ′≁γh​(γ).\mathcal{J}[h](\gamma)\equiv w(\gamma)e^{\sum_{\gamma^{\prime}\nsim\gamma}h(\gamma)}.(S44)

We also define a partial ordering on the space of such functions: for any two real-valued functionsh,h′h,h^{\prime}on the polymers, we writeh≤h′h\leq h^{\prime}ifh​(γ)≤h′​(γ)h(\gamma)\leq h^{\prime}(\gamma)for allγ∈Γ\gamma\in\Gamma.

Note that the functional map𝒥\mathcal{J}has the following two properties:
- 1.

𝒥\mathcal{J}ismonotone: ifh≤h′h\leq h^{\prime}, then𝒥​[h]≤𝒥​[h′]\mathcal{J}[h]\leq\mathcal{J}[h^{\prime}].
- 2.

the functionb​(γ)≡w​(γ)​e|γ|b(\gamma)\equiv w(\gamma)e^{|\gamma|}is anupper-barrier: for anyh≤bh\leq b, we have𝒥​[h]​(γ)≤𝒥​[b]​(γ)=w​(γ)​exp⁡{∑γ′≁γw​(γ)​e|γ|}≤w​(γ)​e|γ|=b​(γ),\mathcal{J}[h](\gamma)\leq\mathcal{J}[b](\gamma)=w(\gamma)\exp\quantity{\sum_{\gamma^{\prime}\nsim\gamma}w(\gamma)e^{|\gamma|}}\leq w(\gamma)e^{|\gamma|}=b(\gamma),(S45)

where we have used the result of Lemma2. In other words, wheneverh≤bh\leq b, we also have𝒥​[h]≤b\mathcal{J}[h]\leq b.

To prove Eq. (S43), let us recursively define the sequence of functionshn:Γ→ℝh_{n}:\Gamma\to\mathbb{R}byh0​(γ)≡0h_{0}(\gamma)\equiv 0andhd≡𝒥​[hd−1]h_{d}\equiv\mathcal{J}[h_{d-1}]ford≥1d\geq 1; from the above two properties of𝒥\mathcal{J}, we immediately haveh0≤h1≤h2≤…≤bh_{0}\leq h_{1}\leq h_{2}\leq\ldots\leq b. We also define the functionsgd​(γ1)≡∑n≥11(n−1)!​∑γ2,…,γn∑T∈𝒯n,depth​(T)≤d(∏(i,j)∈E​(T)|ζ​(γi,γj)|)​(∏(i,j)∈ℰextra​(T)δ​(γi,γj))​∏i=1nw​(γi),g_{d}(\gamma_{1})\equiv\sum_{n\geq 1}\frac{1}{(n-1)!}\sum_{\gamma_{2},\dots,\gamma_{n}}\sum_{\begin{subarray}{c}T\in\mathcal{T}_{n},\\
\text{depth}(T)\leq d\end{subarray}}\left(\prod_{(i,j)\in E(T)}\absolutevalue{\zeta(\gamma_{i},\gamma_{j})}\right)\left(\prod_{(i,j)\in\mathcal{E}_{\text{extra}}(T)}\delta(\gamma_{i},\gamma_{j})\right)\prod_{i=1}^{n}w(\gamma_{i}),(S46)

which are identical to the absolute rooted cluster weightg​(γ)g(\gamma)[see Eq. (S37)], save for the restriction to treesTTof depth less than or equal todd. So long as Eq. (S37) converges, we havelimd→∞gd​(γ)=g​(γ)\lim_{d\to\infty}g_{d}(\gamma)=g(\gamma).

We now make the following observations:
- 1.

Ford=1d=1, we haveh1​(γ)=g1​(γ)=w​(γ)h_{1}(\gamma)=g_{1}(\gamma)=w(\gamma).
- 2.

Ford=2d=2, we haveh2​(γ)=w​(γ)​e∑γ′≁γw​(γ′)h_{2}(\gamma)=w(\gamma)e^{\sum_{\gamma^{\prime}\nsim\gamma}w(\gamma^{\prime})}. On the other hand, by dropping theℰextra\mathcal{E}_{\text{extra}}product in the definition ofg2g_{2}, we obtain the inequalityg2​(γ1)≤∑n≥11(n−1)!​∑γ2,…,γn≁γ1∏j=1nw​(γj)=w​(γ1)​e∑γ′≁γ1w​(γ′)=h2​(γ1),g_{2}(\gamma_{1})\leq\sum_{n\geq 1}\frac{1}{(n-1)!}\sum_{\gamma_{2},\ldots,\gamma_{n}\nsim\gamma_{1}}\prod_{j=1}^{n}w(\gamma_{j})=w(\gamma_{1})e^{\sum_{\gamma^{\prime}\nsim\gamma_{1}}w(\gamma^{\prime})}=h_{2}(\gamma_{1}),(S47)

i.e.,g2≤h2g_{2}\leq h_{2}.
- 3.

More generally, supposegn−1≤hn−1g_{n-1}\leq h_{n-1}. Then, by following an identical strategy to the proof of Lemma3, we obtain the inequalitygd​(γ)≤w​(γ)​e∑γ′≁γgd−1​(γ′)≤w​(γ)​e∑γ′≁γhd−1​(γ′)=hd​(γ),g_{d}(\gamma)\leq w(\gamma)e^{\sum_{\gamma^{\prime}\nsim\gamma}g_{d-1}(\gamma^{\prime})}\leq w(\gamma)e^{\sum_{\gamma^{\prime}\nsim\gamma}h_{d-1}(\gamma^{\prime})}=h_{d}(\gamma),(S48)

where the first inequality follows from noting that the subtrees(T1,…,Tk)(T_{1},\ldots,T_{k})of a depth-ddtreeTTeach have depthd−1d-1. By induction, we therefore learn thatgd≤hdg_{d}\leq h_{d}for alldd. In the limitd→∞d\to\infty, we obtain the resultg​(γ)≤limd→∞hd​(γ)≤b​(γ)=w​(γ)​e|γ|,g(\gamma)\leq\lim_{d\to\infty}h_{d}(\gamma)\leq b(\gamma)=w(\gamma)e^{|\gamma|},(S49)

as desired.

∎

## Lemma 5.

Leteebe an arbitrary edge on the latticeΛ\Lambda. Whenβ≥β∗=2+log⁡3\beta\geq\beta^{\ast}=2+\log 3, there existsCclus>0C_{\mathrm{clus}}>0such that∑𝒞∈𝒮e|f​(𝒞)|≤Cclus​e−4​β,\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})}\leq C_{\mathrm{clus}}e^{-4\beta},(S50)

whereCclusC_{\text{clus}}is a constant defined below.

## Proof.

Using Lemma4,∑𝒞∈𝒮e|f​(𝒞)|\displaystyle\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})}≤∑n≥1∑γ1,…,γn∃γk∋e|φ​(γ1,…,γn)|​∏j=1nw​(γj)\displaystyle\leq\sum_{n\geq 1}\sum_{\begin{subarray}{c}\gamma_{1},\dots,\gamma_{n}\\
\exists\gamma_{k}\ni e\end{subarray}}\absolutevalue{\varphi(\gamma_{1},\dots,\gamma_{n})}\prod_{j=1}^{n}w(\gamma_{j})(S51a)≤∑n≥1n​∑γ1∋e∑γ2,…,γn|φ​(γ1,…,γn)|​∏j=1nw​(γj)\displaystyle\leq\sum_{n\geq 1}n\sum_{\gamma_{1}\ni e}\sum_{\gamma_{2},\dots,\gamma_{n}}\absolutevalue{\varphi(\gamma_{1},\dots,\gamma_{n})}\prod_{j=1}^{n}w(\gamma_{j})(S51b)=∑γ1∋eg​(γ1)\displaystyle=\sum_{\gamma_{1}\ni e}g(\gamma_{1})(S51c)≤∑γ∋ew​(γ)​e|γ|\displaystyle\leq\sum_{\gamma\ni e}w(\gamma)e^{|\gamma|}(S51d)≤∑s≥4,even3s​e−β​s​es\displaystyle\leq\sum_{s\geq 4,\mathrm{even}}3^{s}e^{-\beta s}e^{s}(S51e)=(3​e1−β)41−(3​e1−β)2\displaystyle=\frac{(3e^{1-\beta})^{4}}{1-(3e^{1-\beta})^{2}}(S51f)=Cclus​e−4​β\displaystyle=C_{\mathrm{clus}}e^{-4\beta}(S51g)

where we’ve noted that the number of polymers of lengthsscontaining the edgeeeis upper-bounded by3s3^{s}. In the last line we identify the constantCclus≡(3​e)4/(1−e−2)≈5.115×103C_{\mathrm{clus}}\equiv{(3e)^{4}}/(1-e^{-2})\approx 5.115\times 10^{3}.
∎

## SVThe 00 sector: deriving the parent Hamiltonian with aspect-ratio dependent locality bounds

Having proven that the deformed toric code state|ψ​(β)⟩≡|ψ++​(β)⟩\ket{\psi(\beta)}\equiv\ket{\psi_{++}(\beta)}admits a gapped parent Hamiltonian, we now return to the “no-go” state|ψ00​(β)⟩\ket{\psi_{00}(\beta)}; see Eq. (S4). As noted in the main text, the slightly simpler state|ψ++​(β)⟩\ket{\psi_{++}(\beta)}does not strictly satisfy the assumptions of Ref.40’s Theorem 1, which requires an exact 1-form symmetry about both contractible and non-contractible cycles of the torus. In contrast,|ψ00​(β)⟩\ket{\psi_{00}(\beta)}does exhibit an exact 1-form symmetry about all cycles, and therefore satisfies Ref.40’s assumptions.

We begin by comparing the no-go state|ψ00​(β)⟩\ket{\psi_{00}(\beta)}to the state|ψ++​(β)⟩\ket{\psi_{++}(\beta)}we have studied thus far. From Eqs. (S3) and (S4), it is clear that these two states only differ by the inclusion of non-contractible loops in the latter state|ψ++​(β)⟩\ket{\psi_{++}(\beta)}. Deep in the strongly deformed phase, large loops are rare, and the relative amplitude of these non-contractible loops is suppressed exponentially in linear system sizeLL. Indeed, a simple Peierls argument[19]allows for the overlap between the two states to be lower-bounded for largeβ\betaas|⟨ψ00​(β)|ψ++​(β)⟩|2⟨ψ00​(β)|ψ00​(β)⟩​⟨ψ++​(β)|ψ++​(β)⟩\displaystyle\frac{\absolutevalue{\innerproduct{\psi_{00}(\beta)}{\psi_{++}(\beta)}}^{2}}{\innerproduct{\psi_{00}(\beta)}{\psi_{00}(\beta)}\innerproduct{\psi_{++}(\beta)}{\psi_{++}(\beta)}}=𝒵e-e𝒵e-e+𝒵e-o+𝒵o-e+𝒵o-o≥1−e−𝒪​(L),\displaystyle=\frac{\mathcal{Z}_{\text{e-e}}}{\mathcal{Z}_{\text{e-e}}+\mathcal{Z}_{\text{e-o}}+\mathcal{Z}_{\text{o-e}}+\mathcal{Z}_{\text{o-o}}}\geq 1-e^{-\mathcal{O}(L)},(S52)

where𝒵e-e\mathcal{Z}_{\text{e-e}}is the partition function of the Ising ferromagnet at inverse temperatureβ\betawith periodic (even) boundary conditions (BC),𝒵e-o\mathcal{Z}_{\text{e-o}}has periodic (even) BC alongxxand anti-periodic (odd) BC alongyy, and so on. We bound the middle expression by noting that every contribution to the odd sectors contains a system-spanning polymer, and consequently the odd-sector partition functions are all exponentially suppressed relative to𝒵e-e\mathcal{Z}_{\text{e-e}}at largeβ\beta.

As a direct consquence, the states|ψ00​(β)⟩\ket{\psi_{00}(\beta)}and|ψ++​(β)⟩\ket{\psi_{++}(\beta)}are essentially indistinguishable from each other in the thermodynamic limit: the difference in expectation values of any observable is upper-bounded bye−𝒪​(L)e^{-\mathcal{O}(L)}. In particular, the original state|ψ++​(β)⟩\ket{\psi_{++}(\beta)}is 1-form symmetric about non-contractible loops up to exponentially small corrections, and our parent HamiltonianH​(β)H(\beta)is an excellentapproximateparent Hamiltonian for the no-go state|ψ00​(β)⟩\ket{\psi_{00}(\beta)}.

Nevertheless, it is interesting to construct anexactparent Hamiltonian for|ψ00​(β)⟩\ket{\psi_{00}(\beta)}to see how our approach relates to the rigorous result of Ref.40. Towards this end, we write|ψ00​(β)⟩\ket{\psi_{00}(\beta)}in terms of a deformation operator𝒵^00​(β)\hat{\mathcal{Z}}_{00}(\beta)analogously to Eq. (S14):|ψ00​(β)⟩∝𝒵^00​(β)​|0⟩,𝒵^00​(β)=∑ℒ=∂ℛe−β​|ℒ|​Xℒ,\ket{\psi_{00}(\beta)}\propto\hat{\mathcal{Z}}_{00}(\beta)\ket{0},\qquad\hat{\mathcal{Z}}_{00}(\beta)=\sum_{\mathcal{L}=\partial\mathcal{R}}e^{-\beta\absolutevalue{\mathcal{L}}}X_{\mathcal{L}},(S53)

where the sum is restricted to contractible closed loopsℒ\mathcal{L}, which can always be represented as the boundary of a collection of plaquettesℛ\mathcal{R}. As in the previous case,𝒵^00​(β)\hat{\mathcal{Z}}_{00}(\beta)is a positive-definite operator555To see that𝒵^00​(β)\hat{\mathcal{Z}}_{00}(\beta)is positive-definite, we take a similar strategy as for𝒵^​(β)\hat{\mathcal{Z}}(\beta)in Eq. (7). Specifically, we can express𝒵^00​(β)\hat{\mathcal{Z}}_{00}(\beta)as the high-temperature expansion of a bond-disordered Ising model summed over periodic and antiperiodic boundary conditions:𝒵^00​(β)∝∑{sv=±1}∑ηx,ηy=±1exp⁡{K​∑e=⟨v​v′⟩Ue(ηx,ηy)​Xe​sv​sv′},\hat{\mathcal{Z}}_{00}(\beta)\propto\sum_{\quantity{s_{v}=\pm 1}}\sum_{\eta_{x},\eta_{y}=\pm 1}\exp\quantity{K\sum_{e=\expectationvalue{vv^{\prime}}}U_{e}^{(\eta_{x},\eta_{y})}X_{e}s_{v}s_{v^{\prime}}},(S54)whereUe(ηx,ηy)U_{e}^{(\eta_{x},\eta_{y})}equals+1+1everywhere besides along two non-contractible loopsℒ~x,ℒ~y\tilde{\mathcal{L}}_{x},\tilde{\mathcal{L}}_{y}in the dual lattice; alongℒ~x\tilde{\mathcal{L}}_{x}(ℒ~y\tilde{\mathcal{L}}_{y}),UeU_{e}instead equalsηx\eta_{x}(ηy\eta_{y}). The sum overηx,ηy\eta_{x},\eta_{y}effectively imposes a sum over periodic and antiperiodic boundary conditions, which eliminates non-contractible cycles from the high-temperature expansion., and its logarithm is therefore well-defined. Our goal is to use the Mayer cluster expansion to explicitly take the logarithm of𝒵^00​(β)\hat{\mathcal{Z}}_{00}(\beta), thereby deriving a parent Hamiltonian by the same strategy as in AppendixSIII. Explicitly, we will show similar to the ‘++’ case that the logarithm admits an expansion of the formW^00​(β)≡log⁡𝒵^00​(β)=∑𝒞f​(𝒞)​X𝒞,f​(𝒞)≡φ​(γ1,…,γn)​∏i=1nw​(γi),\hat{W}_{00}(\beta)\equiv\log\hat{\mathcal{Z}}_{00}(\beta)=\sum_{\mathcal{C}}f(\mathcal{C})X_{\mathcal{C}},\quad f(\mathcal{C})\equiv\varphi(\gamma_{1},\ldots,\gamma_{n})\prod_{i=1}^{n}w(\gamma_{i}),(S55)

in perfect analogy to Eq. (S13). The only difference is that the collection of allowed polymersγ∈Γ\gamma\in\Gammaand the form of their interactionsδ​(γ,γ′)\delta(\gamma,\gamma^{\prime})needs to be slightly modified relative to the ‘++’ case, so as to disallow non-contractible loop configurations. Once this modification is made, we obtain a parent Hamiltonian for|ψ00​(β)⟩\ket{\psi_{00}(\beta)}of an identical form to that of|ψ++​(β)⟩\ket{\psi_{++}(\beta)}[see Eq. (S16)]:H00​(β)≡∑e(e−2​∑e∈𝒮ef​(𝒞)​X𝒞−Ze).H_{00}(\beta)\equiv\sum_{e}\quantity(e^{-2\sum_{e\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}}-Z_{e}).(S56)

Finally, we will use similar techniques as in AppendicesSIII.1andSIVto obtain a bound on the cluster weightsf​(𝒞)f(\mathcal{C}), which will in turn allow us to demonstrate the locality ofH00​(β)H_{00}(\beta)for anyfixedaspect ratioax​y≡Lx/Lya_{xy}\equiv L_{x}/L_{y}.

## SV.1Cluster Expansion

To employ the cluster expansion for𝒵^00​(β)\hat{\mathcal{Z}}_{00}(\beta), our first goal is to express it as a polymer model. We immediately see that we cannot use the same set of polymersΓ\Gammaas for the+⁣+++case, which allow for homologically nontrivial polymers in the partition function. Instead, we define the set of polymersΓ\Gammato contain:
- 1.

The set of connected, closed (possibly self-intersecting) loops with trivial homology, and
- 2.

Pairsof connected, closed (possibly self-intersecting) loops withnon-trivialhomology, such that they are disconnected from each other.

For brevity, we will call these “type-1” and “type-2” polymers respectively. The disconnected condition in the second case implies that both loops must be in the same homology class (i.e., they are either both contractible or both non-contractible), and therefore are together the boundary of some regionℛ\mathcal{R}(note that if they were connected, then the two loops are regarded as a single type-1 polymer). The associated weights are defined the same way as before,w^​(γ)=e−β​|γ|​Xγ,Xγ≡∏e∈γXe,\hat{w}(\gamma)=e^{-\beta\absolutevalue{\gamma}}X_{\gamma},\qquad X_{\gamma}\equiv\prod_{e\in\gamma}X_{e},(S57)

but the interaction is modified. We defineδ​(γ,γ′)={0,γ,γ′​intersect,0,γ​and​γ′​are type-2, and are disconnected andunlinked,1,otherwise.\delta(\gamma,\gamma^{\prime})=\begin{cases}0,&\gamma,\gamma^{\prime}\text{ intersect,}\\
0,&\gamma\text{ and }\gamma^{\prime}\text{ are type-2, and are disconnected and \emph{unlinked}},\\
1,&\text{otherwise.}\end{cases}(S58)

We say two disconnected type-2 polymersγ,γ′\gamma,\gamma^{\prime}arelinkedif, for anyℛ,ℛ′\mathcal{R},\mathcal{R}^{\prime}such thatγ=∂ℛ\gamma=\partial\mathcal{R}andγ′=∂ℛ′\gamma^{\prime}=\partial\mathcal{R}^{\prime}, thenℛ\mathcal{R}andℛ′\mathcal{R^{\prime}}have overlapping plaquettes. They areunlinkedotherwise.

To justify this choice of polymers and interactions, we must show that writing out the polymer partition function (S8) produces the correct deformation operator𝒵^00​(β)=∑ℒ=∂ℛe−β​ℒ​Xℒ=∑Γ′⊆Γ[∏γ∈Γ′w^​(γ)]​[∏{γ,γ′}⊆Γ′δ​(γ,γ′)].\hat{\mathcal{Z}}_{00}(\beta)=\sum_{\mathcal{L}=\partial\mathcal{R}}e^{-\beta\mathcal{L}}X_{\mathcal{L}}=\sum_{\Gamma^{\prime}\subseteq\Gamma}\quantity[\prod_{\gamma\in\Gamma^{\prime}}\hat{w}(\gamma)]\quantity[\prod_{\left\{\gamma,\gamma^{\prime}\right\}\subseteq\Gamma^{\prime}}\delta(\gamma,\gamma^{\prime})].(S59)

It is clear from the preceding discussion that the right-hand side produces only contractible loop configurations. Therefore, we only need to ensure that for anyℒ\mathcal{L}on the left-hand side, the right-hand side produces the same term with the correct coefficient (i.e., without overcounting). To this end, we make the following observations:Figure S1:A loop configuration with three type-2 polymers, in maroon, blue, and green respectively. These type-2 polymers are each pairwise compatible, since they satisfy the linking criterion [see Eq. (S58)] withδ​(γ,γ′)=1\delta(\gamma,\gamma^{\prime})=1.
- 1.

Given a loop configurationℒ\mathcal{L}, there is a unique decomposition into connected loops such that all connected loops are mutually disconnected.
- 2.

For a givenℒ\mathcal{L}, if there are no non-contractible connected loops in this decomposition, thenℒ\mathcal{L}is reproduced exactly by a subsetΓ′⊂Γ\Gamma^{\prime}\subset\Gammaon the right-hand side containing only type-1 polymers, where each polymer corresponds to a connected loop inℒ\mathcal{L}.
- 3.

If the decomposition ofℒ\mathcal{L}contains two non-contractible connected loops wrapping the same cycle of the torus (a single non-contractible loop is disallowed),ℒ\mathcal{L}is reproduced by a subsetΓ′\Gamma^{\prime}containing a single type-two polymer.
- 4.

The nontrivial case is whenℒ\mathcal{L}is decomposed into four or more non-contractible connected loops, each wrapping the same cycle of the torus (Fig.S1). Naively, ifℒ\mathcal{L}contains2​n2nsuch loops, there are(2​n−1)!!(2n-1)!!ways to pair these loops into type-2 polymers. The middle condition in the interaction (S58) ensures that only one of these pairings gives a nonzero contribution to𝒵^00\hat{\mathcal{Z}}_{00}. Specifically, a subsetΓ′\Gamma^{\prime}containing multiple type-2 polymers contributes to𝒵^00\hat{\mathcal{Z}}_{00}only if all type-2 polymers inΓ′\Gamma^{\prime}arepairwise linked. The only way to achieve this pairwise linking is to pair the loopsantipodally; that is, if the non-contractible connected loops are labeled1,…,2​n1,\ldots,2nin order, only the pairing{{1,n+1},{2,n+2},…,{n,2​n}}\quantity{\quantity{1,n+1},\quantity{2,n+2},\ldots,\quantity{n,2n}}(S60)

into type-2 polymers leads to a nonvanishing contribution to𝒵^00​(β)\hat{\mathcal{Z}}_{00}(\beta)(see Fig.S1).

In this way, we see that the preceding definition of polymers together with the interaction (S58) avoids overcounting in the polymer partition function on the right-hand side of Eq. (S59), reproducing𝒵^00​(β)\hat{\mathcal{Z}}_{00}(\beta)exactly.

We briefly note that the polymer model for the no-go state differs from that of the+⁣+++state only by the properties of non-contractible loops; the weights and interactions for type-1 polymers are identical in both partition functions. In the large-β\betaregime, we therefore expect that the differences between the two polymer models will be largely inconsequential in the thermodynamic limit, consistent with the observations of the preceding section and with our final conclusions. However, for purposes of constructing an exact parent Hamiltonian for any finite system size, we will exactly keep track of these exponentially small contributions from non-contractible loops.

## SV.2Modified Cluster Expansion Bound

Since the definition of our polymer model has changed slightly, the technical details required to prove the cluster expansion bound in Eq. (13) of the main text are slightly modified. The most important qualitative modification is that, whereas Eq. (13) held at sufficiently largeβ\betafor any system size, the same bound holds in the present setting only for sufficiently largeLx,LyL_{x},L_{y}, and at afixedaspect ratioax​y≡Lx/Lya_{xy}\equiv L_{x}/L_{y}. While the aspect ratio can be chosen arbitrarily, it is crucial that it is held fixed asLx,LyL_{x},L_{y}are taken large; as we will see, our parent Hamiltonian construction can fail if we take (for example)LxL_{x}to scale ase𝒪​(Ly)e^{\mathcal{O}(L_{y})}, consistent with Theorem 1 of Ref.40.

For notational simplicity, we will assume throughoutLx≥LyL_{x}\geq L_{y}without loss of generality.

## Lemma 6(Kotecky-Preiss inequality for the polymer model𝒵^00\hat{\mathcal{Z}}_{00}).

Whenβ≥β∗=2+log⁡3\beta\geq\beta^{\ast}=2+\log 3, and for sufficiently large system sizesLx,LyL_{x},L_{y}with any fixed aspect ratioax​ya_{xy}, the weightw​(γ)=e−β​|γ|w(\gamma)=e^{-\beta\absolutevalue{\gamma}}satisfies∑γ′≁γw​(γ′)​e|γ′|≤|γ|\sum_{\gamma^{\prime}\nsim\gamma}w(\gamma^{\prime})e^{|\gamma^{\prime}|}\leq|\gamma|(S61)

whereγ′≁γ\gamma^{\prime}\nsim\gammameans the two polymers are incompatible (δ​(γ,γ′)=0\delta(\gamma,\gamma^{\prime})=0) according to the interaction (S58).

Note that the statement of the bound is identical to that of Lemma2; the only difference lies in the collection of allowed type-2 polymers and their interactions.

## Proof.

Our strategy is to divide the incompatible polymersγ′≁γ\gamma^{\prime}\nsim\gammainto type-1 and type-2 polymers, respectively:∑γ′≁γw​(γ′)​e|γ′|=∑γ′≁γγ′​type-1w​(γ′)​e|γ′|+∑γ′≁γγ′​type-2w​(γ′)​e|γ′|=∑γ′≁γγ′​type-1w​(γ′)​e|γ′|+∑γ′​type-2w​(γ′)​e|γ′|,\begin{split}\sum_{\gamma^{\prime}\nsim\gamma}w(\gamma^{\prime})e^{|\gamma^{\prime}|}&=\sum_{\begin{subarray}{c}\gamma^{\prime}\nsim\gamma\\
\gamma^{\prime}\text{ type-1}\end{subarray}}w(\gamma^{\prime})e^{|\gamma^{\prime}|}+\sum_{\begin{subarray}{c}\gamma^{\prime}\nsim\gamma\\
\gamma^{\prime}\text{ type-2}\end{subarray}}w(\gamma^{\prime})e^{|\gamma^{\prime}|}\\
&=\sum_{\begin{subarray}{c}\gamma^{\prime}\nsim\gamma\\
\gamma^{\prime}\text{ type-1}\end{subarray}}w(\gamma^{\prime})e^{|\gamma^{\prime}|}+\sum_{\gamma^{\prime}\text{ type-2}}w(\gamma^{\prime})e^{|\gamma^{\prime}|},\end{split}(S62)

where in the second line, we have extended the second sum to run over all type-2 polymers (including those compatible withγ\gamma). The sum over incompatible type-1 polymers is bounded by an identical method to that of Lemma2: the number of such polymersγ′\gamma^{\prime}of fixed length|γ′|=s|\gamma^{\prime}|=sis upper-bounded by|γ|​3s|\gamma|3^{s}.

To bound the sum over type-2 polymersγ′\gamma^{\prime}, lets1s_{1}ands2s_{2}denote the respective lengths of the two connected components ofγ′\gamma^{\prime}. Each ofs1s_{1}ands2s_{2}can be no smaller thanLyL_{y}, since these connected components must form non-contractible loops. For a fixed pair of lengths(s1,s2)(s_{1},s_{2}), The total number of type-2 polymers is upper-bounded by(Lx+Ly)2​3s1+s2(L_{x}+L_{y})^{2}3^{s_{1}+s_{2}}; the two factors of(Lx+Ly)(L_{x}+L_{y})come from observing that each of the two non-contractible loops must cross either thexx-axis or theyy-axis, and there areLxL_{x}(LyL_{y}) locations at which the loop can cross thexx-axis (yy-axis). We therefore obtain the bound∑γ′​type-2w​(γ′)​e|γ′|\displaystyle\sum_{\gamma^{\prime}\text{ type-2}}w(\gamma^{\prime})e^{|\gamma^{\prime}|}≤(Lx+Ly)2​∑s1,s2≥Ly3s1+s2​e−β​(s1+s2)​es1+s2\displaystyle\leq(L_{x}+L_{y})^{2}\sum_{s_{1},s_{2}\geq L_{y}}3^{s_{1}+s_{2}}e^{-\beta(s_{1}+s_{2})}e^{s_{1}+s_{2}}(S63a)≤4​Lx2​((3​e1−β)Ly1−3​e1−β)2\displaystyle\leq 4L_{x}^{2}\quantity(\frac{(3e^{1-\beta})^{L_{y}}}{1-3e^{1-\beta}})^{2}(S63b)≤4(1−e−1)2​(Lx​e−Ly)2​e−2​(β−β∗)​Ly,\displaystyle\leq\frac{4}{(1-e^{-1})^{2}}(L_{x}e^{-L_{y}})^{2}e^{-2(\beta-\beta^{*})L_{y}},(S63c)

valid wheneverβ>β∗−1\beta>\beta^{*}-1. Combined with the bound on type-1 polymers obtained in the proof of Lemma2, we obtain the result∑γ′≁γw​(γ′)​e|γ′|\displaystyle\sum_{\gamma^{\prime}\nsim\gamma}w(\gamma^{\prime})e^{|\gamma^{\prime}|}≤e−41−e−2​e−4​(β−β∗)​|γ|+4(1−e−1)2​(Lx​e−Ly)2​e−2​(β−β∗)​Ly\displaystyle\leq\frac{e^{-4}}{1-e^{-2}}e^{-4(\beta-\beta^{*})}|\gamma|+\frac{4}{(1-e^{-1})^{2}}(L_{x}e^{-L_{y}})^{2}e^{-2(\beta-\beta^{*})L_{y}}(S64a)≤|γ|,\displaystyle\leq|\gamma|,(S64b)

where the last inequality holds for sufficiently largeLyL_{y}, withLx=ax​y​LyL_{x}=a_{xy}L_{y}.
∎

Using the result of Lemma6, the analogs of Lemmas3and4are obtained by identical proofs. The analog of Lemma5is obtained similar to Lemma6, and results in a bound over cluster weightsf​(𝒞)f(\mathcal{C}):

## Lemma 7.

Leteebe an arbitrary edge on the latticeΛ\Lambda. Whenβ≥β∗=2+log⁡3\beta\geq\beta^{\ast}=2+\log 3, and for sufficiently large system sizesLx,LyL_{x},L_{y}with any fixed aspect ratioax​ya_{xy}, there existsCclus>0C_{\mathrm{clus}}>0such that∑𝒞∈𝒮e|f​(𝒞)|≤Cclus​(1+ε)​e−4​β,\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})}\leq C_{\mathrm{clus}}(1+\varepsilon)e^{-4\beta},(S65)

whereε\varepsiloncan be chosen arbitrarily small.

## Proof.

By an identical strategy as in Lemma5, we have∑𝒞∈𝒮e|f​(𝒞)|\displaystyle\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})}≤∑n≥1∑γ1,…,γn∃γk∋e|φ​(γ1,…,γn)|​∏iw​(γi)\displaystyle\leq\sum_{n\geq 1}\sum_{\begin{subarray}{c}\gamma_{1},\dots,\gamma_{n}\\
\exists\gamma_{k}\ni e\end{subarray}}\absolutevalue{\varphi(\gamma_{1},\dots,\gamma_{n})}\prod_{i}w(\gamma_{i})(S66a)≤∑n≥1n​∑γ1∋e∑γ2,…,γn|φ​(γ1,…,γn)|​∏iw​(γi)\displaystyle\leq\sum_{n\geq 1}n\sum_{\gamma_{1}\ni e}\sum_{\gamma_{2},\dots,\gamma_{n}}\absolutevalue{\varphi(\gamma_{1},\dots,\gamma_{n})}\prod_{i}w(\gamma_{i})(S66b)=∑γ1∋eg​(γ1)\displaystyle=\sum_{\gamma_{1}\ni e}g(\gamma_{1})(S66c)≤∑γ∋ew​(γ)​e|γ|\displaystyle\leq\sum_{\gamma\ni e}w(\gamma)e^{|\gamma|}(S66d)≤(∑s≥4,even3s​e−β​s​es+∑γ​type-2w​(γ)​e|γ|)\displaystyle\leq\left(\sum_{s\geq 4,\mathrm{even}}3^{s}e^{-\beta s}e^{s}+\sum_{\gamma\text{ type-2}}w(\gamma)e^{|\gamma|}\right)(S66e)≤(3​e1−β)41−(3​e1−β)2+4(1−e−1)2​(Lx​e−Ly)2​e−2​(β−β∗)​Ly\displaystyle\leq\frac{(3e^{1-\beta})^{4}}{1-(3e^{1-\beta})^{2}}+\frac{4}{(1-e^{-1})^{2}}(L_{x}e^{-L_{y}})^{2}e^{-2(\beta-\beta^{*})L_{y}}(S66f)≤Cclus​(1+ε)​e−4​β,\displaystyle\leq C_{\mathrm{clus}}(1+\varepsilon)e^{-4\beta},(S66g)

where we have once again broken the sum over polymers into type-1 and type-2 polymers, using the bound in Eq. (S63), and we have identifiedCclus=[(3​e)4/(1−e−2)]≈5.115×103C_{\mathrm{clus}}=[(3e)^{4}/(1-e^{-2})]\approx 5.115\times 10^{3}. The arbitrarily small parameterε\varepsilonin the last expression is used to bound the second term in the previous line; for any fixedε>0\varepsilon>0,LyL_{y}andLx=ax​y​LyL_{x}=a_{xy}L_{y}can be taken sufficiently large that the inequality is satisfied.

∎

## SV.3Proving thatH00​(β)H_{00}(\beta)is local and gapped

Finally, we use the result of Lemma7to prove that the parent HamiltonianH00​(β)H_{00}(\beta)is local in the sense of Eqs. (S17), (S18), and (S19) at sufficiently largeβ\beta, from which Theorem 2 implies thatH00​(β)H_{00}(\beta)exhibits a nonzero spectral gap. Our approach mirrors that of the ‘++’ case in AppendixSIII: once again, we Taylor expand the exponential in Eq. (S56) (justified by Lemma7) to writeH00​(β)=H0+∑e∑n≥1(−2)nn!​∑𝒞1​…​𝒞n∈𝒮e∏j=1n[f​(𝒞j)​X𝒞j].H_{00}(\beta)=H_{0}+\sum_{e}\sum_{n\geq 1}\frac{(-2)^{n}}{n!}\sum_{\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}}\prod_{j=1}^{n}\quantity[f(\mathcal{C}_{j})X_{\mathcal{C}_{j}}].(S67)

To divide the sum into local terms, it is convenient to distinguish between clusters𝒞\mathcal{C}containing entirely type-1 polymers and clusters which contain some type-2 polymers. We call a cluster𝒞=(γ1,…,γn)\mathcal{C}=(\gamma_{1},\ldots,\gamma_{n})type-1 if all of its constituent polymers are all type-1; otherwise, we call𝒞\mathcal{C}type-2. We then group terms in Eq. (S67) based on whether they contain type-2 clusters or not. Specifically, we first defineVr,v≡∑e=(v,v+x^),(v,v+y^)∑n≥1(−2)nn!​∑𝒞1​…​𝒞n∈𝒮e𝒞j​type 1​∀jmaxj⁡‖𝒞j‖=r+1∏j=1n[f​(𝒞j)​X𝒞j],V_{r,v}\equiv\sum_{e=(v,v+\hat{x}),(v,v+\hat{y})}\sum_{n\geq 1}\frac{(-2)^{n}}{n!}\sum_{\begin{subarray}{c}\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}\\
\mathcal{C}_{j}\text{ type 1 }\forall j\\
\max_{j}\norm{\mathcal{C}_{j}}=r+1\end{subarray}}\prod_{j=1}^{n}[f(\mathcal{C}_{j})X_{\mathcal{C}_{j}}],(S68)

for all verticesvvand all oddr≥3r\geq 3, in perfect analogy to Eq. (S23), save for the restriction to exclusively type-1 clusters. Recall that the restriction to clusters with maximum lengthmaxj⁡‖𝒞j‖=r+1\max_{j}\norm{\mathcal{C}_{j}}=r+1implies thatVr,vV_{r,v}is contained within ther×rr\times rsquareAv​(r)∈S​(r)A_{v}(r)\in S(r)centered on vertexvv. To capture terms with type-2 clusters, we also define the (highly nonlocal) operatorsVv′≡∑e=(v,v+x^),(v,v+y^)∑n≥1(−2)nn!​∑𝒞1​…​𝒞n∈𝒮e∃type-2​𝒞j∏j=1n[f​(𝒞j)​X𝒞j].V_{v}^{\prime}\equiv\sum_{e=(v,v+\hat{x}),(v,v+\hat{y})}\sum_{n\geq 1}\frac{(-2)^{n}}{n!}\sum_{\begin{subarray}{c}\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}\\
\exists\text{ type-2 }\mathcal{C}_{j}\end{subarray}}\prod_{j=1}^{n}[f(\mathcal{C}_{j})X_{\mathcal{C}_{j}}].(S69)

Combining these two terms, we obtain a partition ofH00​(β)H_{00}(\beta)into terms as follows:H00​(β)=∑v∑r≥3,oddVr,v+∑vVv′.H_{00}(\beta)=\sum_{v}\sum_{r\geq 3,\text{ odd}}V_{r,v}+\sum_{v}V^{\prime}_{v}.(S70)

By an identical calculation to that of Eqs. (S25) and (S26), we immediately obtain the same bound on the spectral norm ofVr,vV_{r,v}in the present setting:‖Vr,v‖≤J​(β)​e−r,J​(β)≡(1+ε)​J~​e−4​β,\norm{V_{r,v}}\leq J(\beta)e^{-r},\quad J(\beta)\equiv(1+\varepsilon)\tilde{J}e^{-4\beta},(S71)

whereJ~\tilde{J}is given explicitly in Eq. (S27), and the parameterε\varepsiloncan be chosen to be arbitrarily small (see Lemma7). Therefore, by Theorem2, themodifiedHamiltonianH~00​(β)≡∑v∑r≥3,oddVr,v\widetilde{H}_{00}(\beta)\equiv\sum_{v}\sum_{r\geq 3,\text{ odd}}V_{r,v}(S72)

is gapped and nondegenerate at sufficiently largeβ\betaand sufficiently large system sizes. On the other hand, we will now show that the remainder term∑vVv′\sum_{v}V^{\prime}_{v}exhibits an exponentially small spectral norm, and therefore the exact parent HamiltonianH00​(β)H_{00}(\beta)is also gapped and nondegnerate in this regime. Explicitly, by a calculation similar to Eq. (S25), we have‖Vv′‖\displaystyle\norm{V_{v}^{\prime}}≤∑e=(v,v+x^),(v,v+y^)∑n≥12nn!​∑𝒞1​…​𝒞n∈𝒮e∃type-2​𝒞j∏j=1n|f​(𝒞j)|\displaystyle\leq\sum_{e=(v,v+\hat{x}),(v,v+\hat{y})}\sum_{n\geq 1}\frac{2^{n}}{n!}\sum_{\begin{subarray}{c}\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}\\
\exists\text{ type-2 }\mathcal{C}_{j}\end{subarray}}\prod_{j=1}^{n}\absolutevalue{f(\mathcal{C}_{j})}(S73a)≤∑e=(v,v+x^),(v,v+y^)∑n≥12n(n−1)!​(∑𝒞∈𝒮e𝒞​type-2|f​(𝒞)|)​(∑𝒞∈𝒮e|f​(𝒞)|)n−1\displaystyle\leq\sum_{e=(v,v+\hat{x}),(v,v+\hat{y})}\sum_{n\geq 1}\frac{2^{n}}{(n-1)!}\quantity(\sum_{\begin{subarray}{c}\mathcal{C}\in\mathcal{S}_{e}\\
\mathcal{C}\text{ type-2}\end{subarray}}\absolutevalue{f(\mathcal{C})})\quantity(\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})})^{n-1}(S73b)

Analogously to Eq. (S26), we bound the last sum over clusters using the result of Lemma7, and we bound the sum over type-2 clusters by noting thatf​(𝒞)≤e−β​Ly​fβ/2​(𝒞)f(\mathcal{C})\leq e^{-\beta L_{y}}f_{\beta/2}(\mathcal{C}), since each type-2 cluster𝒞\mathcal{C}has cluster length‖𝒞‖≥2​Ly\norm{\mathcal{C}}\geq 2L_{y}. Following the same steps as in Eq. (S26), we obtain the bound‖Vv′‖≤Cglobal​e−β​Ly,Cglobal≡4​Cclus​e−2​β∗​exp⁡[2​Cclus​e−4​β∗].\norm{V^{\prime}_{v}}\leq C_{\text{global}}e^{-\beta L_{y}},\quad C_{\text{global}}\equiv 4C_{\mathrm{clus}}e^{-2\beta^{*}}\exp\quantity[2C_{\mathrm{clus}}e^{-4\beta^{*}}].(S74)

Correspondingly,‖∑vVv′‖≤Lx​Ly​Cglobal​e−β​Ly\norm{\sum_{v}V_{v}^{\prime}}\leq L_{x}L_{y}C_{\text{global}}e^{-\beta L_{y}}is exponentially small for sufficiently largeLx,LyL_{x},L_{y}, so long as the aspect ratioax​ya_{xy}is held fixed. By Weyl’s inequality, the spectral gap ofH00​(β)H_{00}(\beta)cannot differ from that ofH~00​(β)\widetilde{H}_{00}(\beta)by more than twice the spectral norm of∑vVv′\sum_{v}V_{v}^{\prime}, and thereforeH00​(β)H_{00}(\beta)also exhibits a nonzero spectral gap in the thermodynamic limit for sufficiently largeβ\beta.

## SVIEquivalent Definitions of locality

In this Appendix, we show that the exponential-in-diameter notion of locality [as defined in Eq. (15) of the main text] and the notion of locality used to prove the stability of gap theorem in Ref.6[Eq. (S19)] are equivalent. For completeness, we recap the definitions here. Note that theexponential-in-volumedefinition of locality [Eq. (S80)] is a strictly stronger criterion than the definitions discussed in this section.

## Definition 1(Exponential-in-diameter locality).

A HamiltonianH=∑ℛ⊆ΛhℛH=\sum_{\mathcal{R}\subseteq\Lambda}h_{\mathcal{R}}, where each local termhℛh_{\mathcal{R}}is supported on subregionℛ\mathcal{R}, is consideredexponential-in-diameter localif there exists finite constantsμ,s>0\mu,s>0such thatsupv∈Λ∑ℛ∋v‖hℛ‖​|ℛ|​eμ​diam⁡(ℛ)≤s.\sup_{v\in\Lambda}\sum_{\mathcal{R}\ni v}\norm{h_{\mathcal{R}}}\absolutevalue{\mathcal{R}}e^{\mu\operatorname{diam}(\mathcal{R})}\leq s.(S75)

## Definition 2(Bravyi-Hastings-Michalakis (BHM) locality[6]).

We write the Hamiltonian asH=∑r≥1∑A∈S​(r)Vr,AH=\sum_{r\geq 1}\sum_{A\in S(r)}V_{r,A}, whereS​(r)S(r)is the set of allr×rr\times rsquares on the lattice, andVr,AV_{r,A}has support on ther×rr\times rsquareAA. Such a Hamiltonian isBHM-localif there exists constantsJ,μ′>0J,\mu^{\prime}>0such thatsupA∈S​(r)‖Vr,A‖≤J​e−μ′​r.\sup_{A\in S(r)}\norm{V_{r,A}}\leq Je^{-\mu^{\prime}r}.(S76)

We will callJJthe strength of the Hamiltonian andμ′\mu^{\prime}the decay exponent.

## SVI.1Definition 1⟹\impliesDefinition 2

Given an exponential-in-diameter local HamiltonianH=∑ℛ⊆ΛhℛH=\sum_{\mathcal{R}\subseteq\Lambda}h_{\mathcal{R}}, let us define the local termsVr,v≡∑ℛ∋vdiam⁡(ℛ)=r1|ℛ|​hℛ.V_{r,v}\equiv\sum_{\begin{subarray}{c}\mathcal{R}\ni v\\
\operatorname{diam}(\mathcal{R})=r\end{subarray}}\frac{1}{\absolutevalue{\mathcal{R}}}h_{\mathcal{R}}.(S77)

Note that eachhℛh_{\mathcal{R}}contributes to|ℛ|\absolutevalue{\mathcal{R}}distinct termsVr,vV_{r,v}, and thereforeH=∑v∈Λ∑r≥1Vr,vH=\sum_{v\in\Lambda}\sum_{r\geq 1}V_{r,v}. Moreover,Vr,vV_{r,v}is supported on the(2​r−1)×(2​r−1)(2r-1)\times(2r-1)square centerd atvv. Finally, its norm is upper-bounded as‖Vr,v‖\displaystyle\norm{V_{r,v}}≤∑ℛ∋vdiam⁡(ℛ)=r1|ℛ|​‖hℛ‖\displaystyle\leq\sum_{\begin{subarray}{c}\mathcal{R}\ni v\\
\operatorname{diam}(\mathcal{R})=r\end{subarray}}\frac{1}{|\mathcal{R}|}\norm{h_{\mathcal{R}}}(S78a)=e−μ​r​∑ℛ∋vdiam⁡(ℛ)=r|ℛ||ℛ|2​‖hℛ‖​eμ​diam⁡(ℛ)\displaystyle=e^{-\mu r}\sum_{\begin{subarray}{c}\mathcal{R}\ni v\\
\operatorname{diam}(\mathcal{R})=r\end{subarray}}\frac{|\mathcal{R}|}{|\mathcal{R}|^{2}}\norm{h_{\mathcal{R}}}e^{\mu\operatorname{diam}(\mathcal{R})}(S78b)≤s​e−μ​r\displaystyle\leq se^{-\mu r}(S78c)=s​e−μ/2​e−μ2​(2​r−1).\displaystyle=se^{-\mu/2}e^{-\frac{\mu}{2}(2r-1)}.(S78d)

We therefore find that exponential-in-diameter locality implies BHM locality, with strengthJ=s​e−μ/2J=se^{-\mu/2}and decay exponentμ′=μ/2\mu^{\prime}=\mu/2.

## SVI.2Definition 2⟹\impliesDefinition 1

Given a BHM-local HamiltonianH=∑r≥1∑A∈S​(r)Vr,AH=\sum_{r\geq 1}\sum_{A\in S(r)}V_{r,A}, we simply identifyhℛ=Vr,Ah_{\mathcal{R}}=V_{r,A}withℛ=A\mathcal{R}=A. Then, lettingμ\mube an unspecified constant for now, we have∑ℛ∋v‖hℛ‖​|ℛ|​eμ​diam⁡(ℛ)\displaystyle\sum_{\mathcal{R}\ni v}\norm{h_{\mathcal{R}}}\absolutevalue{\mathcal{R}}e^{\mu\operatorname{diam}(\mathcal{R})}=∑r≥1∑A∈S​(r)A∋v‖Vr,A‖​|A|​eμ​diam⁡(A)\displaystyle=\sum_{r\geq 1}\sum_{\begin{subarray}{c}A\in S(r)\\
A\ni v\end{subarray}}\norm{V_{r,A}}\absolutevalue{A}e^{\mu\operatorname{diam}(A)}(S79a)=∑r≥1∑A∈S​(r)A∋v‖Vr,A‖​r2​eμ​2​r\displaystyle=\sum_{r\geq 1}\sum_{\begin{subarray}{c}A\in S(r)\\
A\ni v\end{subarray}}\norm{V_{r,A}}r^{2}e^{\mu\sqrt{2}r}(S79b)≤∑r≥1r2​J​e−μ′​r​r2​eμ​2​r,\displaystyle\leq\sum_{r\geq 1}r^{2}Je^{-\mu^{\prime}r}r^{2}e^{\mu\sqrt{2}r},(S79c)

where in the final line, we’ve noted that there arer2r^{2}squaresA∈S​(r)A\in S(r)containing a given vertexvv. The final sum converges as long asμ<μ′/2\mu<\mu^{\prime}/\sqrt{2}. We therefore find that BHM locality implies exponential-in-diameter locality, for some decay constantμ<μ′/2\mu<\mu^{\prime}/\sqrt{2}and strengths∝Js\propto Jgiven explicitly by the above sum.

## SVIIExponential-in-volume locality bounds

In this Appendix, we show that our parent HamiltonianH​(β)H(\beta)not only satisfies the exponential-in-diameter and BHM locality conditions described in AppendixSVI, but also satisfies a strongerexponential-in-volumelocality condition:

## Definition 3(Exponential-in-volume locality).

A HamiltonianH=∑ℛ⊆ΛhℛH=\sum_{\mathcal{R}\subseteq\Lambda}h_{\mathcal{R}}, where each local termhℛh_{\mathcal{R}}is supported on theconnectedsubregionℛ\mathcal{R}, is consideredexponential-in-volumelocal if there exists finite constantsμ,s>0\mu,s>0such thatsupv∑ℛ∋v‖hℛ‖​|ℛ|​eμ​|ℛ|≤s.\sup_{v}\sum_{\mathcal{R}\ni v}\norm{h_{\mathcal{R}}}|\mathcal{R}|e^{\mu|\mathcal{R}|}\leq s.(S80)

Note that this condition effectively requires‖hℛ‖\norm{h_{\mathcal{R}}}to decay exponentially with thevolume|ℛ||\mathcal{R}|of the subregionℛ\mathcal{R}. This is a stronger condition than the exponential-in-diameter decay required of the preceding section.

From the explicit form of our parent HamiltonianH​(β)H(\beta)[see Eq. (S16)], it is quite natural thatH​(β)H(\beta)satisfies such a bound: indeed, the nontrivial component ofH​(β)H(\beta)consists of a sum of loop operators exponentially suppressed in their lengthℒ\mathcal{L}, which is generally proportional to both the loop’s diameter and the volume of its support. Furthermore, using the results of Ref.50,14, the existence of a gapped exponential-in-volume local parent HamiltonianH​(β)H(\beta)for|ψ​(β)⟩\ket{\psi(\beta)}implies that|ψ​(β)⟩\ket{\psi(\beta)}can be prepared (up to an error exponentially small in the system size) by finite-time unitary evolution using an exponential-in-volume local quasiadiabatic generator.

To prove thatH​(β)=H0+VH(\beta)=H_{0}+Vsatisfies exponential-in-volume locality, it is sufficient to focus on the nontrivial componentVV, which we once again expand in Taylor series:V≡∑e(e−2​∑𝒞∈𝒮ef​(𝒞)​X𝒞−1)=∑e∑n≥1(−2)nn!​∑𝒞1​…​𝒞n∈𝒮e∏j=1n[f​(𝒞j)​X𝒞j].V\equiv\sum_{e}\quantity(e^{-2\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}}-1)=\sum_{e}\sum_{n\geq 1}\frac{(-2)^{n}}{n!}\sum_{\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}}\prod_{j=1}^{n}[f(\mathcal{C}_{j})X_{\mathcal{C}_{j}}].(S81)

Our first goal is to groupVVinto local terms. Towards this end, we associate a connected regionℛ​(𝒞1,…,𝒞n)\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})to each collection of connected clusters(𝒞1,…,𝒞n)(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})with𝒞j≡(γ1(j),…,γmj(j))\mathcal{C}_{j}\equiv(\gamma^{(j)}_{1},\ldots,\gamma^{(j)}_{m_{j}})as follows:ℛ​(𝒞1,…,𝒞n)≡⋃j(γ1(j)∪…∪γmj(j)).\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})\equiv\bigcup_{j}\quantity(\gamma^{(j)}_{1}\cup\ldots\cup\gamma^{(j)}_{m_{j}}).(S82)

Such regionsℛ\mathcal{R}appearing inVVare guaranteed to be connected, since all of the clusters𝒞j\mathcal{C}_{j}comprising a given region are required to contain the same edgeee. Note that the same region will generally appear several times withinVV; by treating them as separate in computing the sum (S80), we are strictly overestimating the left-hand side, since we are ignoring potential sign cancellations. We therefore have the inequalitysupe∑ℛ∋e‖Vℛ‖​|ℛ|​eμ​|ℛ|≤supe∑e′∑n≥1∑𝒞1​…​𝒞n∈𝒮e′ℛ​(𝒞1,…,𝒞n)∋e2nn!​|f​(𝒞1)|​…​|f​(𝒞n)|​|ℛ​(𝒞1,…,𝒞n)|​eμ​|ℛ​(𝒞1,…,𝒞n)|\begin{split}\sup_{e}\sum_{\mathcal{R}\ni e}\norm{V_{\mathcal{R}}}|\mathcal{R}|e^{\mu|\mathcal{R}|}&\leq\sup_{e}\sum_{e^{\prime}}\sum_{n\geq 1}\sum_{\begin{subarray}{c}\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e^{\prime}}\\
\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})\ni e\end{subarray}}\frac{2^{n}}{n!}\absolutevalue{f(\mathcal{C}_{1})}\ldots\absolutevalue{f(\mathcal{C}_{n})}\absolutevalue{\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})}e^{\mu\absolutevalue{\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})}}\end{split}(S83)

Due to translation invariance, the supremum overeecan be discarded. In fact, we can simplify the sum byaveragingover alleeas follows:∑e′∑n≥1∑𝒞1​…​𝒞n∈𝒮e′ℛ​(𝒞1,…,𝒞n)∋e(⋯)\displaystyle\sum_{e^{\prime}}\sum_{n\geq 1}\sum_{\begin{subarray}{c}\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e^{\prime}}\\
\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})\ni e\end{subarray}}\quantity(\cdots)=1Ne​∑e,e′∑n≥1∑𝒞1​…​𝒞n∈𝒮e′ℛ​(𝒞1,…,𝒞n)∋e(⋯)\displaystyle=\frac{1}{N_{e}}\sum_{e,e^{\prime}}\sum_{n\geq 1}\sum_{\begin{subarray}{c}\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e^{\prime}}\\
\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})\ni e\end{subarray}}(\cdots)(S84a)=1Ne​∑e′∑n≥1∑𝒞1​…​𝒞n∈𝒮e′|ℛ​(𝒞1,…,𝒞n)|​(⋯)\displaystyle=\frac{1}{N_{e}}\sum_{e^{\prime}}\sum_{n\geq 1}\sum_{\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e^{\prime}}}\absolutevalue{\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})}(\cdots)(S84b)=∑n≥1∑𝒞1​…​𝒞n∈𝒮e|ℛ​(𝒞1,…,𝒞n)|​(⋯),\displaystyle=\sum_{n\geq 1}\sum_{\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}}\absolutevalue{\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})}(\cdots),(S84c)

where in the second line we’ve performed the sum overeeby noting that there are precisely|ℛ​(𝒞1,…,𝒞n)|\absolutevalue{\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})}nonvanishing terms in the sum, each with the same value; and in the third line we’ve noted that every term in the sum overe′e^{\prime}yields the same value, allowing us to replace the sum overe′e^{\prime}with a fixed edgeee. We therefore have the inequality∑ℛ∋e‖Vℛ‖​|ℛ|​eμ​|ℛ|\displaystyle\sum_{\mathcal{R}\ni e}\norm{V_{\mathcal{R}}}|\mathcal{R}|e^{\mu|\mathcal{R}|}≤∑n≥1∑𝒞1​…​𝒞n∈𝒮e2nn!​|f​(𝒞1)|​…​|f​(𝒞n)|​|ℛ​(𝒞1,…,𝒞n)|2​eμ​|ℛ​(𝒞1,…,𝒞n)|\displaystyle\leq\sum_{n\geq 1}\sum_{\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}}\frac{2^{n}}{n!}\absolutevalue{f(\mathcal{C}_{1})}\ldots\absolutevalue{f(\mathcal{C}_{n})}\absolutevalue{\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})}^{2}e^{\mu\absolutevalue{\mathcal{R}(\mathcal{C}_{1},\ldots,\mathcal{C}_{n})}}(S85a)≤∑n≥1∑𝒞1​…​𝒞n∈𝒮e2nn!​|f​(𝒞1)|​…​|f​(𝒞n)|​[‖𝒞1‖+…+‖𝒞n‖]2​eμ​[‖𝒞1‖+…+‖𝒞n‖]\displaystyle\leq\sum_{n\geq 1}\sum_{\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}}\frac{2^{n}}{n!}\absolutevalue{f(\mathcal{C}_{1})}\ldots\absolutevalue{f(\mathcal{C}_{n})}\Big[\norm{\mathcal{C}_{1}}+\ldots+\norm{\mathcal{C}_{n}}\Big]^{2}e^{\mu\big[\norm{\mathcal{C}_{1}}+\ldots+\norm{\mathcal{C}_{n}}\big]}(S85b)≤∑n≥1∑𝒞1​…​𝒞n∈𝒮e2nn!​|f​(𝒞1)|​…​|f​(𝒞n)|​e[‖𝒞1‖+…+‖𝒞n‖]​eμ​[‖𝒞1‖+…+‖𝒞n‖]\displaystyle\leq\sum_{n\geq 1}\sum_{\mathcal{C}_{1}\ldots\mathcal{C}_{n}\in\mathcal{S}_{e}}\frac{2^{n}}{n!}\absolutevalue{f(\mathcal{C}_{1})}\ldots\absolutevalue{f(\mathcal{C}_{n})}e^{\big[\norm{\mathcal{C}_{1}}+\ldots+\norm{\mathcal{C}_{n}}\big]}e^{\mu\big[\norm{\mathcal{C}_{1}}+\ldots+\norm{\mathcal{C}_{n}}\big]}(S85c)=exp⁡{2​∑𝒞∈𝒮e|f​(𝒞)|​e(μ+1)​‖𝒞‖}−1,\displaystyle=\exp\quantity{2\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f(\mathcal{C})}e^{(\mu+1)\norm{\mathcal{C}}}}-1,(S85d)

recalling that‖𝒞‖=∑γ∈𝒞|γ|\norm{\mathcal{C}}=\sum_{\gamma\in\mathcal{C}}\absolutevalue{\gamma}is the total length of all polymers in the cluster𝒞\mathcal{C}. In the third line we have used the inequalityx2≤exx^{2}\leq e^{x}for allx>0x>0, applied tox=‖𝒞1‖+…+‖𝒞n‖x=\norm{\mathcal{C}_{1}}+\ldots+\norm{\mathcal{C}_{n}}.

As in the proofs of Sec.SIII.1, we bound the sum over clusters by writingf​(𝒞)=e−β​‖𝒞‖/2​fβ/2​(𝒞)f(\mathcal{C})=e^{-\beta\norm{\mathcal{C}}/2}f_{\beta/2}(\mathcal{C}), wherefβ/2​(𝒞)f_{\beta/2}(\mathcal{C})is the same function evaluated at deformation strengthβ/2\beta/2. As long asβ>2​(μ+1)\beta>2(\mu+1), we then have∑ℛ∋e‖Vℛ‖​|ℛ|​eμ​|ℛ|≤exp⁡{2​∑𝒞∈𝒮e|fβ/2​(𝒞)|​e(μ+1−β/2)​‖𝒞‖}−1≤exp⁡{2​∑𝒞∈𝒮e|fβ/2​(𝒞)|}−1≤exp⁡{2​Cclus​e−2​β}−1,\begin{split}\sum_{\mathcal{R}\ni e}\norm{V_{\mathcal{R}}}|\mathcal{R}|e^{\mu|\mathcal{R}|}&\leq\exp\quantity{2\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f_{\beta/2}(\mathcal{C})}e^{(\mu+1-\beta/2)\norm{\mathcal{C}}}}-1\\
&\leq\exp\quantity{2\sum_{\mathcal{C}\in\mathcal{S}_{e}}\absolutevalue{f_{\beta/2}(\mathcal{C})}}-1\\
&\leq\exp\quantity{2C_{\mathrm{clus}}e^{-2\beta}}-1,\end{split}(S86)

where in the final line, we have used the bound in Eq. (13) of the main text (proven in Lemma5), valid forβ>2​β∗=2​(2+log⁡3)\beta>2\beta^{*}=2(2+\log 3). Note that the final expression can be made arbitrarily small at largeβ\beta.

Altogether, we find that foranychoice of the constantsμ,s\mu,s, the perturbationVVsatisfies the exponential-in-volume locality criterion in Eq. (S80) at sufficiently large values ofβ\beta. A similar locality bound can be immediately obtained for the full parent HamiltonianH​(β)=H0+VH(\beta)=H_{0}+Vby addingeμe^{\mu}to the value ofss, to account for the contribution from the strictly local term inH0H_{0}.

## SVIIIThe Strongly Pauli-ZZDecohered Toric Code is Short-Range Entangled

In this section, we outline a rigorous proof that the 2D toric code under sufficiently large Pauli-ZZdecoherence strength is separable as a convex sum of trivial pure states. To do so, we exploit the decomposition of the decohered toric code into pure states given in Refs.12,47, and utilize our construction to construct gapped parent Hamiltonians for these states.

## SVIII.1Review: Separability Transition of the Decohered Toric Code

For completeness, we first review the main result of Ref.12, which constructs a particular pure-state decomposition for the toric code subjected to a single species of Pauli errors. Readers who are already familiar with the result of Ref.12can skip to the next section.

We consider the toric code subjected to incoherent Pauli-ZZdecoherence, such that the local error channel on edgeeeis given byℰe​(ρ)=(1−p)​ρ+p​Ze​ρ​Ze.\mathcal{E}_{e}(\rho)=(1-p)\rho+pZ_{e}\rho Z_{e}.(S87)

Applying the same channel independently to all edges, we haveρp≡ℰ​(|TC⟩⟨TC|)=∑E(1−p)Ne−|E|​p|E|​ZE​|TC⟩⟨TC|​ZE=(1−p)Ne​∑E(p1−p)|E|​ZE​|TC⟩⟨TC|​ZE,\begin{split}\rho_{p}\equiv\mathcal{E}(\outerproduct{\text{TC}}{\text{TC}})&=\sum_{E}(1-p)^{N_{e}-\absolutevalue{E}}p^{\absolutevalue{E}}Z_{E}\outerproduct{\text{TC}}{\text{TC}}Z_{E}\\
&=(1-p)^{N_{e}}\sum_{E}\left(\frac{p}{1-p}\right)^{\absolutevalue{E}}Z_{E}\outerproduct{\text{TC}}{\text{TC}}Z_{E},\end{split}(S88)

whereℰ≡∏eℰe\mathcal{E}\equiv\prod_{e}\mathcal{E}_{e}, andEEis the ‘error configuration’, i.e., the collection of edges which were acted on nontrivially by the error, so thatZE≡∏e∈EZeZ_{E}\equiv\prod_{e\in E}Z_{e}is the corresponding error.

To simplify the decohered state, first note thatZE​|TC⟩=ZE′​|TC⟩Z_{E}\ket{\text{TC}}=Z_{E^{\prime}}\ket{\text{TC}}wheneverZEZ_{E}andZE′Z_{E^{\prime}}differ by vertex stabilizersAv=∏e∋vZeA_{v}=\prod_{e\ni v}Z_{e}. We can therefore sort errors into equivalence classes, denoted[E][E]with representativeEE, and reorganize the sum over errors as a sum over equivalence classes:ρp∝∑[E][∑E′∼E(p1−p)|E′|]​ZE​|TC⟩⟨TC|​ZE=∑[E]𝒵p​(E)​ZE​|TC⟩⟨TC|​ZE,\begin{split}\rho_{p}&\propto\sum_{[E]}\quantity[\sum_{E^{\prime}\sim E}\quantity(\frac{p}{1-p})^{|E^{\prime}|}]Z_{E}\outerproduct{\text{TC}}{\text{TC}}Z_{E}\\
&=\sum_{[E]}\mathcal{Z}_{p}(E)\,Z_{E}\outerproduct{\text{TC}}{\text{TC}}Z_{E},\end{split}(S89)

whereE′∼EE^{\prime}\sim Emeans thatZEZ_{E}andZE′Z_{E^{\prime}}differ by products ofAvA_{v}stabilizers, and the relative probabilities𝒵p​(E)\mathcal{Z}_{p}(E)of each equivalence class are proportional to the partition functions of a bond-disordered Ising model[15]:𝒵p​(E)≡∑E′∼E(p1−p)|E′|∝𝒵KIsing​({xe})≡∑{sv=±1}exp⁡{K​∑e=⟨v​v′⟩xe​sv​sv′},\begin{split}\mathcal{Z}_{p}(E)&\equiv\sum_{E^{\prime}\sim E}\quantity(\frac{p}{1-p})^{|E^{\prime}|}\\
&\propto\mathcal{Z}^{\text{Ising}}_{K}(\quantity{x_{e}})\equiv\sum_{\quantity{s_{v}=\pm 1}}\exp\quantity{K\sum_{e=\expectationvalue{vv^{\prime}}}x_{e}s_{v}s_{v^{\prime}}},\end{split}(S90)

withK=−12​log⁡[p/(1−p)]K=-\frac{1}{2}\log[p/(1-p)], andxe=−1x_{e}=-1(xe=+1x_{e}=+1) whenevere∈Ee\in E(e∉Ee\not\in E). Note thatZp​(E)Z_{p}(E)is independent of the choice of representativeEE; in the language of the Ising model, the partition function depends only on the locations of frustrated plaquettes and the homology of the disorder lines connecting them through the dual lattice. It can be shown from the above representation ofρp\rho_{p}that there is a sharp phase transition atp=pc≈0.109p=p_{c}\approx 0.109in the behavior of an optimal decoder which attempts to recover|TC⟩\ket{\text{TC}}fromρp\rho_{p}, whose critical phenomena is described by the random-bond Ising model on the Nishimori line[15,16].

In Ref.12, the authors argued that the phase transition in optimal decoding coincides with aseparabilitytransition: forp>pcp>p_{c}, it becomes possible to expressρp\rho_{p}as a convex sum of short-range entangled (SRE) states. To demonstrate this result, let us first consider the initial state|TC⟩=|TC++⟩\ket{\text{TC}}=\ket{\text{TC}_{++}}. In this case,ZE​|TC++⟩Z_{E}\ket{\text{TC}_{++}}is orthogonal toZE′​|TC++⟩Z_{E^{\prime}}\ket{\text{TC}_{++}}wheneverE≁E′E\nsim E^{\prime}. This allows us to trivially take the square root ofρp\rho_{p}:ρp∝∑[E]𝒵p​(E)​ZE​|TC++⟩⟨TC++|​ZE.\sqrt{\rho_{p}}\propto\sum_{[E]}\sqrt{\mathcal{Z}_{p}(E)}\,Z_{E}\outerproduct{\text{TC}_{++}}{\text{TC}_{++}}Z_{E}.(S91)

Following Ref.12, we writeρp=ρp​ρp\rho_{p}=\sqrt{\rho_{p}}\sqrt{\rho_{p}}and insert a resolution of identity in the Pauli-ZZbasis:ρp∝∑{ze=±1}ρp​|{ze}⟩⟨{ze}|​ρp=∑ℒXℒ​(ρp​|0⟩⟨0|​ρp)​Xℒ,\begin{split}\rho_{p}&\propto\sum_{\quantity{z_{e}=\pm 1}}\sqrt{\rho_{p}}\outerproduct{\quantity{z_{e}}}{\quantity{z_{e}}}\sqrt{\rho_{p}}\\
&=\sum_{\mathcal{L}}X_{\mathcal{L}}\quantity(\sqrt{\rho_{p}}\outerproduct{0}{0}\sqrt{\rho_{p}})X_{\mathcal{L}},\end{split}(S92)

Where we’ve noted that the only Pauli-ZZbasis states having nonzero overlap withρp\rho_{p}are those satisfyingAv=+1A_{v}=+1(i.e., closed loop states), and therefore can be written asXℒ​|0⟩X_{\mathcal{L}}\ket{0}for some loop operatorXℒX_{\mathcal{L}}; additionally, note thatXℒX_{\mathcal{L}}commutes withρp\rho_{p}andρp\sqrt{\rho_{p}}. We can further simplify the pure state in the parenthesis as follows:ρp​|0⟩\displaystyle\sqrt{\rho_{p}}\ket{0}=∑[E]𝒵p​(E)​ZE​|TC++⟩⟨TC++|​ZE​|0⟩\displaystyle=\sum_{[E]}\sqrt{\mathcal{Z}_{p}(E)}\,Z_{E}\outerproduct{\text{TC}_{++}}{\text{TC}_{++}}Z_{E}\ket{0}(S93a)∝∑[E]𝒵p​(E)​ZE​(∏v(1+Av)​∏p(1+Bp)​∏μ=1,2(1+X¯μ))​ZE​|0⟩\displaystyle\propto\sum_{[E]}\sqrt{\mathcal{Z}_{p}(E)}\,Z_{E}\quantity(\prod_{v}(1+A_{v})\prod_{p}(1+B_{p})\prod_{\mu=1,2}(1+\overline{X}_{\mu}))Z_{E}\ket{0}(S93b)=∑[E]𝒵p​(E)​ZE​(∏p(1+Bp)​∏μ=1,2(1+X¯μ))​ZE​|0⟩\displaystyle=\sum_{[E]}\sqrt{\mathcal{Z}_{p}(E)}\,Z_{E}\quantity(\prod_{p}(1+B_{p})\prod_{\mu=1,2}(1+\overline{X}_{\mu}))Z_{E}\ket{0}(S93c)∝∑[E]𝒵p​(E)​ZE​(∏p(1+Bp)​∏μ=1,2(1+X¯μ))​ZE​∑E′ZE′​|+⟩,\displaystyle\propto\sum_{[E]}\sqrt{\mathcal{Z}_{p}(E)}\,Z_{E}\quantity(\prod_{p}(1+B_{p})\prod_{\mu=1,2}(1+\overline{X}_{\mu}))Z_{E}\sum_{E^{\prime}}Z_{E^{\prime}}\ket{+},(S93d)

where in the second line,X¯μ≡Xℒμ\overline{X}_{\mu}\equiv X_{\mathcal{L}_{\mu}}are a basis of two logical-XXoperators, given by Wilson loop operators about two representative non-contractible loopsℒμ\mathcal{L}_{\mu}of the torus. In the final line,|+⟩\ket{+}is the simultaneous +1 eigenstate of eachXeX_{e}, and the projectorZE​(⋯)​ZEZ_{E}\quantity(\cdots)Z_{E}annihilates the state to the right unlessEEandE′E^{\prime}are homologous. Finally using that𝒵p​(E)\mathcal{Z}_{p}(E)is independent of the chosen representative, we obtain the simple expressionρp​|0⟩∝∑E𝒵p​(E)​ZE​|+⟩∝∑{xe=±1}𝒵K​({xe})​|{xe}⟩x,\begin{split}\sqrt{\rho_{p}}\ket{0}&\propto\sum_{E}\sqrt{\mathcal{Z}_{p}(E)}\,Z_{E}\ket{+}\\
&\propto\sum_{\quantity{x_{e}=\pm 1}}\sqrt{\mathcal{Z}_{K}(\quantity{x_{e}})}\ket{\quantity{x_{e}}}_{x},\end{split}(S94)

where|{xe}⟩x\ket{\quantity{x_{e}}}_{x}are the simultaneous Pauli-XXeigenstates. In summary, we find thatρp\rho_{p}can be written as a convex sum of pure states as follows:ρp∝∑ℒXℒ​|ϕ​(p)⟩⟨ϕ​(p)|​Xℒ,|ϕ​(p)⟩≡ρp​|0⟩∝∑{xe=±1}𝒵K​({xe})​|{xe}⟩x.\rho_{p}\propto\sum_{\mathcal{L}}X_{\mathcal{L}}\outerproduct{\phi(p)}{\phi(p)}X_{\mathcal{L}},\quad\ket{\phi(p)}\equiv\sqrt{\rho_{p}}\ket{0}\propto\sum_{\quantity{x_{e}=\pm 1}}\sqrt{\mathcal{Z}_{K}(\quantity{x_{e}})}\ket{\quantity{x_{e}}}_{x}.(S95)

The authors of Ref.12argued that the state|ϕ​(p)⟩\ket{\phi(p)}(and thereby each stateXℒ​|ϕ​(p)⟩X_{\mathcal{L}}\ket{\phi(p)}, which differs from|ϕ​(p)⟩\ket{\phi(p)}by the finite-depth unitaryXℒX_{\mathcal{L}}) is short-range entangled from the following properties:
- 1.

One-form symmetry: forcontractibleloopsℒ~\tilde{\mathcal{L}}in the dual lattice,Zℒ~​|ϕ​(p)⟩=|ϕ​(p)⟩Z_{\tilde{\mathcal{L}}}\ket{\phi(p)}=\ket{\phi(p)}. This follows by noting thatZℒ~Z_{\tilde{\mathcal{L}}}commutes withρp\sqrt{\rho_{p}}, so thatZℒ~​ρp​|0⟩=ρp​|0⟩Z_{\tilde{\mathcal{L}}}\sqrt{\rho_{p}}\ket{0}=\sqrt{\rho_{p}}\ket{0}. Alternatively,Zℒ~Z_{\tilde{\mathcal{L}}}ads a contractible closed loop to the disorder realization{xe}\quantity{x_{e}}, leaving the partition functions𝒵K​({xe})\mathcal{Z}_{K}(\quantity{x_{e}})invariant.
- 2.

Condensedmmanyons: if we instead consider an open stringP~\tilde{P}through the dual lattice, we find⟨ϕ​(p)|​ZP~​|ϕ​(p)⟩⟨ϕ​(p)|​|ϕ​(p)⟩=∑E(1−p)Ne−|E|​p|E|​Zp​(E⊕P~)Zp​(E).\frac{\bra{\phi(p)}Z_{\tilde{P}}\ket{\phi(p)}}{\bra{\phi(p)}\ket{\phi(p)}}=\sum_{E}(1-p)^{N_{e}-|E|}p^{|E|}\sqrt{\frac{Z_{p}(E\oplus\tilde{P})}{Z_{p}(E)}}.(S96)

This quantity is a two-point disorder parameter correlator in the Nishimori random-bond Ising model; it decays exponentially forp<pcp<p_{c}and is long-range ordered forp>pcp>p_{c}. We therefore find that|ϕ​(p)⟩\ket{\phi(p)}exhibits condensedmmanyons forp>pcp>p_{c}.

Subsequently, Ref.47demonstrated numerically that|ϕ​(p)⟩\ket{\phi(p)}exhibits zero topological entanglement entropy. It follows from these observations that|ϕ​(p)⟩\ket{\phi(p)}realizes a topologically trivial confined phase.

However, it is also interesting to note that|ϕ​(p)⟩\ket{\phi(p)}exhibitsperimeter-lawWilson loop correlation functions; indeed, sinceXℒX_{\mathcal{L}}commutes withρp\sqrt{\rho_{p}}, we have⟨ϕ​(p)|​Xℒ​|ϕ​(p)⟩⟨ϕ​(p)|​|ϕ​(p)⟩=⟨0|​Xℒ​ρp​|0⟩⟨0|​ρp​|0⟩=∑E(1−p)Ne−|E|​p|E|​⟨0|​Xℒ​ZE​|TC⟩​⟨TC|​|0⟩⟨0|​|TC⟩​⟨TC|​|0⟩=(1−2​p)|ℒ|.\frac{\bra{\phi(p)}X_{\mathcal{L}}\ket{\phi(p)}}{\bra{\phi(p)}\ket{\phi(p)}}=\frac{\bra{0}X_{\mathcal{L}}\rho_{p}\ket{0}}{\bra{0}\rho_{p}\ket{0}}=\sum_{E}(1-p)^{N_{e}-|E|}p^{|E|}\frac{\bra{0}X_{\mathcal{L}}Z_{E}\ket{\text{TC}}\bra{\text{TC}}\ket{0}}{\bra{0}\ket{\text{TC}}\bra{\text{TC}}\ket{0}}=(1-2p)^{|\mathcal{L}|}.(S97)

In other words, the state|ϕ​(p)⟩\ket{\phi(p)}is qualitatively similar to the deformed toric code state studied in the main text. Given the results of Ref.40, one may naturally wonder whether these states are indeed short-range entangled (SRE) or not. In the following section, we will demonstrate explicitly that|ϕ​(p)⟩\ket{\phi(p)}is SRE at sufficiently largeppby constructing a local gapped parent Hamiltonian for which|ϕ​(p)⟩\ket{\phi(p)}is the unique ground state.

## SVIII.2Constructing a Parent Hamiltonian for|ϕ​(p)⟩\ket{\phi(p)}

To construct a parent Hamiltonian for|ϕ​(p)⟩\ket{\phi(p)}, we note from Eq. (S95) that it can be expressed in terms of the deformation operator𝒵^​(β)\hat{\mathcal{Z}}(\beta)defined for the deformed toric code [see Eq. (S6), as well as Eq. (7) of the main text]:|ϕ​(p)⟩∝∑{xe=±1}𝒵^​(β)​|{xe}⟩x∝𝒵^​(β)​|0⟩=exp⁡(12​W^​(β))​|0⟩=exp⁡{12​∑𝒞f​(𝒞)​X𝒞}​|0⟩,\ket{\phi(p)}\propto\sum_{\quantity{x_{e}=\pm 1}}\sqrt{\hat{\mathcal{Z}}(\beta)}\ket{\quantity{x_{e}}}_{x}\propto\sqrt{\hat{\mathcal{Z}}(\beta)}\ket{0}=\exp{\frac{1}{2}\hat{W}(\beta)}\ket{0}=\exp\quantity{\frac{1}{2}\sum_{\mathcal{C}}f(\mathcal{C})X_{\mathcal{C}}}\ket{0},(S98)

whereβ≡−log⁡tanh⁡K=2​artanh⁡[p/(1−p)]\beta\equiv-\log\tanh K=2\operatorname{artanh}[p/(1-p)]. We see that|ϕ​(p)⟩\ket{\phi(p)}is nearly identical to the deformed toric code state|ψ​(β)⟩\ket{\psi(\beta)}, except that the deformation operator ise12​W^e^{\frac{1}{2}\hat{W}}instead ofeW^e^{\hat{W}}. By an identical construction as for|ψ​(β)⟩\ket{\psi(\beta)}, we obtain the following parent Hamiltonian for|ϕ​(p)⟩\ket{\phi(p)}:Hdec​(p)=∑e(e−∑𝒞∈𝒮ef​(𝒞)​X𝒞−Ze),H_{\text{dec}}(p)=\sum_{e}\quantity(e^{-\sum_{\mathcal{C}\in\mathcal{S}_{e}}f(\mathcal{C})X_{\mathcal{C}}}-Z_{e}),(S99)

which differs from the parent HamiltonianH​(β)H(\beta)only by a factor of two inside the exponential term.

Although we will not explicitly prove thatHdec​(p)H_{\text{dec}}(p)is gapped for sufficiently largepp, it is clear that an essentially identical proof to the one of AppendicesSIIIandSIVwill lead to an analogous result: namely,Hdec​(p)H_{\text{dec}}(p)can be shown to be local in the sense of Eqs. (S17), (S18), and (S19), and therefore Theorem2proves thatHdec​(p)H_{\text{dec}}(p)is gapped and exhibits the unique ground state|ϕ​(p)⟩\ket{\phi(p)}for sufficiently largepp.

## SVIII.3More General Decohered Toric Code States

Thus far, we have studied the ++ state|TC++⟩\ket{\text{TC}_{++}}under strong Pauli-ZZdecoherence. It is interesting to consider more general initial toric code states, which can be written in the form|TCΞ⟩=∑ℓΞℓ​Z¯ℓ​|TC++⟩,\ket{\text{TC}_{\Xi}}=\sum_{\ell}\Xi_{\ell}\overline{Z}_{\ell}\ket{\text{TC}_{++}},(S100)

whereZ¯ℓ≡Zℒℓ\overline{Z}_{\ell}\equiv Z_{\mathcal{L}_{\ell}}are a collection of four logical-ZZoperators (for example:Z¯0=1\overline{Z}_{0}=1,Z¯1=Zℒx~\overline{Z}_{1}=Z_{\tilde{\mathcal{L}_{x}}}for a non-contractiblexx-loopℒ~x\tilde{\mathcal{L}}_{x}, etc), andΞℓ\Xi_{\ell}are four complex numbers. Since eachZ¯ℓ\overline{Z}_{\ell}commutes with the Pauli-ZZdecoherence channel, we can immediately write down the corresponding decohered state:ρp≡∑ℓ​ℓ′Ξℓ​Ξℓ′∗​Z¯ℓ​ℰ​(|TC++⟩⟨TC++|)​Z¯ℓ′∝∑ℓ​ℓ′Ξℓ​Ξℓ′∗​Z¯ℓ​(∑ℒXℒ​|ϕ​(p)⟩⟨ϕ​(p)|​Xℒ)​Z¯ℓ′=∑ℒ|Ξℒ​(p)⟩⟨Ξℒ​(p)|,\begin{split}\rho_{p}\equiv\sum_{\ell\ell^{\prime}}\Xi_{\ell}\Xi_{\ell^{\prime}}^{*}\,\overline{Z}_{\ell}\,\mathcal{E}(\outerproduct{\text{TC}_{++}}{\text{TC}_{++}})\overline{Z}_{\ell^{\prime}}&\propto\sum_{\ell\ell^{\prime}}\Xi_{\ell}\Xi_{\ell^{\prime}}^{*}\,\overline{Z}_{\ell}\,\quantity(\sum_{\mathcal{L}}X_{\mathcal{L}}\outerproduct{\phi(p)}{\phi(p)}X_{\mathcal{L}})\overline{Z}_{\ell^{\prime}}\\
&=\sum_{\mathcal{L}}\outerproduct{\Xi_{\mathcal{L}}(p)}{\Xi_{\mathcal{L}}(p)},\end{split}(S101)

where|Ξℒ​(p)⟩≡∑ℓΞℓ​Z¯ℓ​Xℒ​|ϕ​(p)⟩.\ket{\Xi_{\mathcal{L}}(p)}\equiv\sum_{\ell}\Xi_{\ell}\overline{Z}_{\ell}X_{\mathcal{L}}\ket{\phi(p)}.(S102)

For sufficiently largeppand generic complex coefficientsΞℓ\Xi_{\ell}, each state|Ξℒ​(p)⟩\ket{\Xi_{\mathcal{L}}(p)}is once again SRE up to exponentially small corrections. To see this, recall that|ϕ​(p)⟩=e12​W^​|0⟩\ket{\phi(p)}=e^{\frac{1}{2}\hat{W}}\ket{0}is a sum overZe=−1Z_{e}=-1loop configurations such that large loops are suppressed exponentially in their system size. Consequently,|ϕ​(p)⟩\ket{\phi(p)}is approximately 1-form symmetric under non-contractible loops—that is, for each nontrivial logical operatorZ¯ℓ\overline{Z}_{\ell},Z¯ℓ​|ϕ​(p)⟩=|ϕ​(p)⟩+e−𝒪​(L),\overline{Z}_{\ell}\ket{\phi(p)}=\ket{\phi(p)}+e^{-\mathcal{O}(L)},(S103)

where the correction term is a vector of exponentially small norm (relative to that of|ϕ​(p)⟩\ket{\phi(p)}). Therefore, for genericΞℓ\Xi_{\ell}, we have|Ξℒ​(p)⟩∝Xℒ​|ϕ​(p)⟩+e−𝒪​(L).\ket{\Xi_{\mathcal{L}}(p)}\propto X_{\mathcal{L}}\ket{\phi(p)}+e^{-\mathcal{O}(L)}.(S104)

As a result,|Ξℒ​(p)⟩\ket{\Xi_{\mathcal{L}}(p)}is a SRE state, we find that once again that Eq. (S101) constitutes an exact decomposition into SRE states for genericΞℓ\Xi_{\ell}.

On the other hand, for certain special choices of the wavefunction amplitudesΣℓ\Sigma_{\ell}, it is possible to obtain long-range entangled (LRE) states|Ξℒ​(p)⟩\ket{\Xi_{\mathcal{L}}(p)}. For example, consider the state with(Ξ0,Ξ1,Ξ2,Ξ3)=(1,−1,0,0)(\Xi_{0},\Xi_{1},\Xi_{2},\Xi_{3})=(1,-1,0,0)andℒ=∅\mathcal{L}=\emptyset, given explicitly by|(1,−1,0,0)∅​(p)⟩≡(1−Z¯ℒx)​|ϕ​(p)⟩.\ket{(1,-1,0,0)_{\emptyset}(p)}\equiv(1-\overline{Z}_{\mathcal{L}_{x}})\ket{\phi(p)}.(S105)

This state is a sum over all loop configurations with a non-contractibleZe=−1Z_{e}=-1loop about theyycycle of the torus; it can be regarded as a “loop-wave” state, in the terminology of Ref.40. Such states are expected to be LRE, and so Eq. (S101) does not constitute an exact decomposition into SRE states. Nevertheless, since non-contractible loops comprise ane−𝒪​(L)e^{-\mathcal{O}(L)}component of|ϕ​(p)⟩\ket{\phi(p)}, the norm of states such as Eq. (S105) ise−𝒪​(L)e^{-\mathcal{O}(L)}. In terms of normalized SRE states|ψiSRE⟩\ket{\psi_{i}^{\text{SRE}}}and normalized LRE states|ψjLRE⟩\ket{\psi^{\text{LRE}}_{j}}, the full density matrixρp\rho_{p}therefore has the general structureρp=∑ici​|ψiSRE⟩⟨ψiSRE|+∑jdj​|ψiLRE⟩⟨ψiLRE|,∑jdj=e−𝒪​(L).\rho_{p}=\sum_{i}c_{i}\outerproduct{\psi_{i}^{\text{SRE}}}{\psi_{i}^{\text{SRE}}}+\sum_{j}d_{j}\outerproduct{\psi_{i}^{\text{LRE}}}{\psi_{i}^{\text{LRE}}},\quad\sum_{j}d_{j}=e^{-\mathcal{O}(L)}.(S106)

In other words, althoughρp\rho_{p}is not exactly decomposed into a convex sum of SRE states (at least in this particular decomposition), the total probability of all LRE states to in this decomposition ofρp\rho_{p}is exponentially small; consequently, in the thermodynamic limit,ρp\rho_{p}cannot be distinguished from a genuine SRE state by any observable. In this specific sense, we can once again regardρp\rho_{p}as an SRE mixed state.

## SIXVerifying entanglement bootstrap axioms for the strongly deformed toric code

In this Appendix, we provide an informal physicists’ argument showing that the strongly deformed toric code satisfies the A0 and A1 axioms of entanglement bootstrap[42,43,27]approximately, such that the axioms become exact as we scale up the partition size.

We quickly recap the axioms through Fig.S2. In this section, we show that bothΔ​(B,C)\Delta(B,C)of A0 andΔ​(B,C,D)\Delta(B,C,D)of A1 scale as∼rC​exp⁡(−2​β​ℓ)\sim r_{C}\exp(-2\beta\ell), whereℓ\ellis the width of the annulus andrCr_{C}is the radius of the inner circle. To show this, we use the result of Ref.9(see[18]for a field-theoretic version) which states that, for any regionAA, we can write the Von Neumann entanglement entropy of the reduced density matrixρA=TrA¯⁡[|ψ​(β)⟩⟨ψ​(β)|]/⟨ψ​(β)|ψ​(β)⟩\rho_{A}=\Tr_{\overline{A}}\left[\outerproduct{\psi(\beta)}{\psi(\beta)}\right]/\innerproduct{\psi(\beta)}{\psi(\beta)}asSA=−∑ℒe−β​|ℒ|𝒵​log⁡(𝒵ℒ∂A𝒵),𝒵≡∑ℒe−β​|ℒ|,𝒵ℒ∂A≡∑ℒ′:ℒ′=ℒ​on​∂Ae−β​|ℒ′|.S_{A}=-\sum_{\mathcal{L}}\frac{e^{-\beta\absolutevalue{\mathcal{L}}}}{\mathcal{Z}}\log\left(\frac{\mathcal{Z}^{\partial A}_{\mathcal{L}}}{\mathcal{Z}}\right),\qquad\mathcal{Z}\equiv\sum_{\mathcal{L}}e^{-\beta\absolutevalue{\mathcal{L}}},\qquad\mathcal{Z}^{\partial A}_{\mathcal{L}}\equiv\sum_{\begin{subarray}{c}\mathcal{L}^{\prime}:\\
\mathcal{L}^{\prime}=\mathcal{L}\text{ on }\partial A\end{subarray}}e^{-\beta\absolutevalue{\mathcal{L}^{\prime}}}.(S107)

The quantity𝒵ℒ∂A\mathcal{Z}^{\partial A}_{\mathcal{L}}can be regarded as the partition function of an Ising model with its configuration on∂A\partial Aconstrained to agree with that ofℒ\mathcal{L}. This relation maps the von Neumann entanglement entropy of the deformed toric code on a subsystemAAto the entropy of the subsystem spin configuration a classical Ising model666Technically the Ising⋆model, i.e., an Ising model summed over both periodic and antiperiodic boundary conditions, so that domain walls may exhibit non-contractible loops.at inverse temperatureβ\beta, where the latter subsystem lives on the boundary∂A\partial A. We refer the reader to[9]for a derivation of the above result using the replica trick.Figure S2:The two axioms of the entanglement bootstrap. CallingAAthe region outside the annulus in either case, both axioms reduce to having vanishing conditional mutual informationI(A:C|B)=0I(A:C|B)=0. Away from fixed point gapped states, these axioms will only be approximately satisfied, i.e.I(A:C|B)∼exp⁡(−ℓ/ξ)I(A:C|B)\sim\exp(-\ell/\xi), whereℓ\ellis the width of the annulus andξ\xiis a partition-independent length scale called the Markov length. In the (infrared) limit where the annulus is scaled up such thatℓ≫ξ\ell\gg\xi, the axioms become exact.

Usingp​(ℒ)=e−β​|ℒ|/𝒵p(\mathcal{L})=e^{-\beta\absolutevalue{\mathcal{L}}}/\mathcal{Z}as a probability measure over the space of closed loops, we can writeΔ​(B,C)\displaystyle\Delta(B,C)=SB​C+SC−SB\displaystyle=S_{BC}+S_{C}-S_{B}(S108a)=−𝔼ℒ​[log⁡(𝒵ℒ∂(B​C)​𝒵ℒ∂C𝒵ℒ∂B​𝒵)]\displaystyle=-\mathbb{E}_{\mathcal{L}}\left[\log\left(\frac{\mathcal{Z}^{\partial(BC)}_{\mathcal{L}}\mathcal{Z}^{\partial C}_{\mathcal{L}}}{\mathcal{Z}^{\partial B}_{\mathcal{L}}\mathcal{Z}}\right)\right](S108b)

We analyze the argument of the log within a large-β\beta(low-temperature in the Ising language) expansion. The highest weight configuration when we take the expectation value𝔼ℒ\mathbb{E}_{\mathcal{L}}over the probability measurep​(ℒ)p(\mathcal{L})is the empty loop configurationℒ={}\mathcal{L}=\{\}. Correspondingly, the constrained partition functions𝒵ℒ∂ℛ\mathcal{Z}^{\partial\mathcal{R}}_{\mathcal{L}}sum over configurations with no loops cutting across the boundary∂ℛ\partial\mathcal{R}. In this sector, we see that all small loop configurations occur an equal number of times in the two ‘product’ partition functions𝒵ℒ∂(B​C)​𝒵ℒ∂C{\mathcal{Z}^{\partial(BC)}_{\mathcal{L}}\mathcal{Z}^{\partial C}_{\mathcal{L}}}and𝒵ℒ∂B​𝒵{\mathcal{Z}^{\partial B}_{\mathcal{L}}\mathcal{Z}}. The lowest order loop ‘diagram’ that distinguishes the two is a thin connected loop that cuts across both boundaries of regionBB, as such a diagram cannot occur in𝒵ℒ∂(B​C),𝒵ℒ∂C{\mathcal{Z}^{\partial(BC)}_{\mathcal{L}},\mathcal{Z}^{\partial C}_{\mathcal{L}}}, or𝒵ℒ∂B{\mathcal{Z}^{\partial B}_{\mathcal{L}}}but can appear in𝒵{\mathcal{Z}}. Within a large-β\beta(low temperature) expansion, such diagrams contribute as∼rC​e−2​β​ℓ\sim r_{C}e^{-2\beta\ell}tolog⁡(𝒵ℒ∂(B​C)​𝒵ℒ∂C/𝒵ℒ∂B​𝒵)\log\left({\mathcal{Z}^{\partial(BC)}_{\mathcal{L}}\mathcal{Z}^{\partial C}_{\mathcal{L}}}/{\mathcal{Z}^{\partial B}_{\mathcal{L}}\mathcal{Z}}\right), whereℓ\ellis the width of the annulusBBandrCr_{C}is the radius of the inner diskCC.

For loop configurationsℒ\mathcal{L}consisting of sparse small connected loops, we anticipate that a similar conclusion holds, thatlog⁡(𝒵ℒ∂(B​C)​𝒵ℒ∂C/𝒵ℒ∂B​𝒵)∼rC​e−2​β​ℓ\log\left({\mathcal{Z}^{\partial(BC)}_{\mathcal{L}}\mathcal{Z}^{\partial C}_{\mathcal{L}}}/{\mathcal{Z}^{\partial B}_{\mathcal{L}}\mathcal{Z}}\right)\sim r_{C}e^{-2\beta\ell}. Since the low temperature expansion for𝔼ℒ\mathbb{E}_{\mathcal{L}}is dominated by such loop configurations, we argue that for sufficiently largeβ\beta, we the deformed toric code satisfies the A0 axiom approximately, given byΔ​(B,C)∼rC​e−ℓ/ξ,\Delta(B,C)\sim r_{C}e^{-\ell/\xi},(S109)

whereξ≈1/2​β\xi\approx 1/2\betamay be renormalized from the value predicted by this low-temperature expansion by entropic effects that we ignore. Notably, as we uniformly scale up the partitionB​CBC,Δ​(B,C)\Delta(B,C)vanishes exponentially quickly in linear partition size.

For the axiom A1, a very similar argument holds. Using the replica trick, we can writeΔ​(B,C,D)\displaystyle\Delta(B,C,D)=SB​C+SC​D−SB−SD\displaystyle=S_{BC}+S_{CD}-S_{B}-S_{D}(S110a)=−𝔼ℒ​[log⁡(𝒵ℒ∂(B​C)​𝒵ℒ∂(C​D)𝒵ℒ∂B​𝒵ℒ∂D)].\displaystyle=-\mathbb{E}_{\mathcal{L}}\left[\log\left(\frac{\mathcal{Z}^{\partial(BC)}_{\mathcal{L}}\mathcal{Z}^{\partial(CD)}_{\mathcal{L}}}{\mathcal{Z}^{\partial B}_{\mathcal{L}}\mathcal{Z}^{\partial D}_{\mathcal{L}}}\right)\right].(S110b)

One can argue that a very similar diagram (a thin connected loop) that cuts across both the inner and outer boundaries ofBB(DD) is the smallest “distinguishing diagram” that appears in no partition function in (S110b) except𝒵ℒ∂D\mathcal{Z}^{\partial D}_{\mathcal{L}}(𝒵ℒ∂B\mathcal{Z}^{\partial B}_{\mathcal{L}}) for typical loop configurationsℒ\mathcal{L}. Therefore, we expect that, once againΔ​(B,C,D)∼rC​e−ℓ/ξ,ξ≈1/2​β.\Delta(B,C,D)\sim r_{C}e^{-\ell/\xi},\qquad\xi\approx 1/2\beta.(S111)

As we increase the partition size compared toξ\xi,A​1A1becomes approximately satisfied.

## 


- 


Major funding support from
