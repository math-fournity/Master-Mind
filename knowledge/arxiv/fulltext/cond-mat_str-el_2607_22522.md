# Exact Neural-Network Representations of the Motzkin States

**arXiv ID**: 2607.22522v1
**Authors**: Runde Zha, Yuntian Gu, Chaohui Fan, Jia-lin Chen, Hai-Jun Liao, Tao Xiang
**Published**: 2026-07-24
**Categories**: cond-mat.str-el, quant-ph
**HTML URL**: https://arxiv.org/html/2607.22522v1

## Abstract

Motzkin spin chains are paradigmatic frustration-free one-dimensional quantum systems whose ground states feature exactly solvable combinatorial structures and exotic, area-law-violating entanglement scaling. Specifically, colorless Motzkin states exhibit critical logarithmic entanglement divergence \(\log N\) with system size \(N\), while their colorful counterparts host supercritical sublinear \(\sqrt{N}\) entanglement growth. Such unconventional entanglement behaviors place these states well beyond the expressive capability of standard matrix product states, which are fundamentally constrained by the entanglement area law. Here, we systematically construct exact, training-free neural-network representations for both colorless and colorful Motzkin states across four mainstream architectures, including recurrent, feedforward, convolutional, and transformer networks. Our core design leverages a causal prefix-sum module, implementable via recurrent updates, feedforward mappings, or masked attention layers, combined with position-selective rectified linear gates that enforce the Motzkin height constraints. For the colorful states, we further introduce a dedicated causal stack module that explicitly encodes the last-in-first-out color-matching rule. Our results demonstrate that neural architectures can accurately capture highly non-trivial entanglement features inaccessible to conventional tensor networks, providing prototypic examples for benchmarking and a constructive design framework for future neural-network quantum state developments targeting strongly entangled quantum systems.

## Full Text

Exact Neural-Network Representations of the Motzkin States

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.22522v1 [cond-mat.str-el] 24 Jul 2026††thanks:These authors contributed equally to this work.††thanks:These authors contributed equally to this work.††thanks:These authors contributed equally to this work.

## Exact Neural-Network Representations of the Motzkin StatesRunde ZhaBeijing National Laboratory for Condensed Matter Physics, Institute of Physics,
Chinese Academy of Sciences, Beijing 100190, ChinaSchool of Physical Sciences, University of Chinese Academy of Sciences, Beijing
100049, ChinaYuntian GuState Key Laboratory of General Artificial Intelligence, School of Intelligence
Science and Technology, Peking UniversityByteDance Seed, ChinaChaohui FanBeijing National Laboratory for Condensed Matter Physics, Institute of Physics,
Chinese Academy of Sciences, Beijing 100190, ChinaSchool of Physical Sciences, University of Chinese Academy of Sciences, Beijing
100049, ChinaByteDance Seed, ChinaJia-lin ChenBeijing National Laboratory for Condensed Matter Physics, Institute of Physics,
Chinese Academy of Sciences, Beijing 100190, ChinaSchool of Physical Sciences, University of Chinese Academy of Sciences, Beijing
100049, ChinaHai-Jun Liaonavyphysics@iphy.ac.cnBeijing National Laboratory for Condensed Matter Physics, Institute of Physics,
Chinese Academy of Sciences, Beijing 100190, ChinaTao Xiangtxiang@iphy.ac.cnBeijing National Laboratory for Condensed Matter Physics, Institute of Physics,
Chinese Academy of Sciences, Beijing 100190, ChinaSchool of Physical Sciences, University of Chinese Academy of Sciences, Beijing
100049, ChinaBeijing Academy of Quantum Information Sciences, Beijing 100193, China

## Abstract

Motzkin spin chains are paradigmatic frustration-free one-dimensional quantum systems whose ground states feature exactly solvable combinatorial structures and exotic, area-law-violating entanglement scaling. Specifically, colorless Motzkin states exhibit critical logarithmic entanglement divergencelog⁡N\log Nwith system sizeNN, while their colorful counterparts host supercritical sublinearN\sqrt{N}entanglement growth. Such unconventional entanglement behaviors place these states well beyond the expressive capability of standard matrix product states, which are fundamentally constrained by the entanglement area law. Here, we systematically construct exact, training-free neural-network representations for both colorless and colorful Motzkin states across four mainstream architectures, including recurrent, feedforward, convolutional, and transformer networks. Our core design leverages a causal prefix-sum module, implementable via recurrent updates, feedforward mappings, or masked attention layers, combined with position-selective rectified linear gates that enforce the Motzkin height constraints. For the colorful states, we further introduce a dedicated causal stack module that explicitly encodes the last-in-first-out color-matching rule. Our results demonstrate that neural architectures can accurately capture highly non-trivial entanglement features inaccessible to conventional tensor networks, providing prototypic examples for benchmarking and a constructive design framework for future neural-network quantum state developments targeting strongly entangled quantum systems.

## IIntroduction

Quantum entanglement is one of the most distinctive features of quantum mechanics, revealing correlations with no classical counterpart. In quantum many-body systems, it measures nonclassical correlations, constrains the complexity of quantum states, and distinguishes quantum phases beyond local order parameters. In one-dimensional gapped systems, ground-state entanglement is typically constrained by an area law[24,15], while critical systems described by conformal field theory show only logarithmic violations[28,51,31,4,5].

Motzkin spin chains provide an exceptional exactly solvable setting beyond this standard picture. The original spin-1 Motzkin chain is frustration-free and critical, with a ground state given by an equal-weight superposition of Motzkin paths, namely constrained random walks or balanced-parenthesis configurations[3]. Its colored generalization gives the first rigorously solvable local spin-chain example with supercritical entanglement, where the half-chain entanglement entropy grows asN\sqrt{N}withNNthe chain length, parametrically faster than logarithmic critical scaling while still arising from local frustration-free interactions[40]. Because this anomalous entanglement arises from simple local constraints and an explicitly known wave function, Motzkin states provide a controlled setting for benchmarking the quantum-state preparation and simulation protocols implemented on quantum computers and quantum simulators, as well as the representational power of tensor-network states, neural-network quantum states (NQS), and other variational wavefunctions.

This benchmark role has motivated recent work along several complementary directions. On the state-preparation side, digital dissipative protocols have been proposed for frustration-free gapless systems, including Motzkin-type spin chains[18]. On the simulation front, Rydberg-atom platforms offer a promising route to realizing Motzkin spin-chain constraints and dynamics in controllable atomic arrays[41]. From a representation perspective, Motzkin states have inspired exact tensor-network constructions, including holographic tensor-network descriptions of the Motzkin spin chain[2]and rainbow tensor networks for colorful Motzkin and Fredkin chains[1]. These developments reinforce the role of Motzkin states as analytically tractable but nontrivial testbeds for comparing how different physical platforms and classical ansatzes capture anomalous entanglement.

In recent years, NQS have emerged as highly expressive variational ansatzes for many-body wave functions[6]. Deep networks can efficiently encode broad classes of entangled states[19], and close connections have been uncovered between neural-network states and tensor-network representations[9,29,23,10,36,17]. The capabilities of NQS have been demonstrated in frustrated spin systems[12,43,17]and, more generally, in strongly correlated fermions. Early work adopted restricted Boltzmann machines to treat Hubbard models[42]. Later architectures include autoregressive and recurrent networks for efficient sampling and sequential wave-function modeling[48,26], alongside determinant- and Pfaffian-based neural-network states that incorporate fermionic antisymmetry and pairing correlations[20,33,8,11,44,38,7]. Recently, autoregressive, transformer and convolutional backflow architectures have achieved high accuracy for doped Hubbard and related models, capturing stripe correlations and enabling large-scale benchmarks[30,22,21]. At the same time, NQS have also been used as impurity solvers for quantum embedding[54]. These developments highlight the strong representational capabilities of NQS and raise a natural question as to whether such frameworks can exactly encode critical and supercritical Motzkin states with entanglement properties that depart from standard area-law scaling.

In this work, we resolve this question by constructing exact neural-network representations of both colorless and colorful Motzkin states. The construction is fully analytic and uses fixed weights, thereby eliminating the need for variational training. For the colorless state, a common height block computes prefix sums and excludes paths that violate nonnegativity or endpoint closure. For the colorful state, this block is supplemented by a stack, or equivalently by an attention pointer to the most recent unmatched up step, to enforce color matching.

The remainder of the paper is organized as follows. SectionIIreviews the colorless and colorful Motzkin states, including their path constraints, parent Hamiltonians, and entanglement structure. SectionIIIpresents the exact NQS construction for the colorless case, based on feed-forward, recurrent, and causal-attention implementations of the height rule. SectionIVextends this construction to colorful Motzkin states by incorporating stack and attention-pointer blocks that perform color matching. SectionVanalyzes how the parameter count scales with system size N for the various neural-network models and compares the resulting representations with tensor-network descriptions. Finally, SectionVIsummarizes our findings and discusses implications and future directions.

## IIMotzkin States(a)crossingxxaxis−1-10112233yy0112233445566778899101011111212xx(b)011223344yy0112233445566778899101011111212xx(c)color mismatch011223344yy0112233445566778899101011111212xx

FIG. 1.Examples of Motzkin-path constraints.(a) A path that violates the height constraint by
crossing below the axis. (b) A legal colorful Motzkin path, where each down step matches the most
recent unmatched up step of the same color. (c) A path with the same height profile as in (b), but
with an illegal color mismatch.

Motzkin spin chains were introduced by Shor and coworkers as frustration-free one-dimensional models whose ground states are controlled by Motzkin paths[3]. Their colored generalization, developed by Movassagh and Shor, provided the first rigorously solvable local spin-chain example with supercritical entanglement[40]. These models connect combinatorial path languages with quantum many-body physics and provide a useful testing ground for Hamiltonian complexity, entanglement structure, and variational representations.

Motzkin states are the ground states of Motzkin spin chains, with support defined by Motzkin
paths[3]. For a length-NNspin-1 chain, the local basis{|↑⟩,|0⟩,|↓⟩}\{\ket{\uparrow},\ket{0},\ket{\downarrow}\}is identified with an up, flat, or down step with an incrementxi={+1,up​step=u,0,flat​step=0,−1,down​step=d.x_{i}=\begin{cases}+1,&\mathrm{up\,step}=u,\\
0,&\mathrm{flat\,step}=0,\\
-1,&\mathrm{down\,step}=d.\end{cases}(1)

A basis configurationX=(x1,…,xN)X=(x_{1},\ldots,x_{N})defines prefix heightsSt=∑i=1txi,S0=0.S_{t}=\sum_{i=1}^{t}x_{i},\qquad S_{0}=0.(2)

The Motzkin constraint isSt≥0(t=1,…,N−1),SN=0,S_{t}\geq 0\quad(t=1,\ldots,N-1),\qquad S_{N}=0,(3)

namely the path never crosses below the axis and returns to zero at the endpoint.

The colorless
Motzkin state is the equal-weight superposition of all configurations satisfying
Eq. (3),|ℳN⟩=1|C0,0​(N)|​∑s∈C0,0​(N)|s⟩,\ket{\mathcal{M}_{N}}=\frac{1}{\sqrt{|C_{0,0}(N)|}}\sum_{s\in C_{0,0}(N)}\ket{s},(4)

whereC0,0​(N)C_{0,0}(N)denotes the set of valid length-NNMotzkin paths.

The colorful Motzkin state is obtained by assigning one ofsscolors, e.g., thekkth color, to every up and down step,|uk⟩\ket{u^{k}}and|dk⟩\ket{d^{k}}, while flat steps remain colorless. In addition to the height rule
in Eq. (3), every down step must match the color of the most recent unmatched
up step. Equivalently, the path obeys a last-in-first-out color-matching rule, as in balanced
colored parentheses; see Fig.IIfor representative examples.

The normalized colorful Motzkin state is therefore|ℳN,s⟩=1MN,s​∑w∈Motzkin⁡(N,s)|w⟩,\ket{\mathcal{M}_{N,s}}=\frac{1}{\sqrt{M_{N,s}}}\sum_{w\in\operatorname{Motzkin}(N,s)}\ket{w},(5)

whereMotzkin⁡(N,s)\operatorname{Motzkin}(N,s)is the set of color-matched Motzkin paths andMN,s=|Motzkin⁡(N,s)|M_{N,s}=|\operatorname{Motzkin}(N,s)|is the number of all allowed paths.

## II.1Parent Hamiltonians

The Motzkin states arise as exact ground states of local frustration-free parent Hamiltonians. In the colorless case, the Hamiltonian is built from local equivalence moves[3]00↔u​d,0​u↔u​0,0​d↔d​0.00\leftrightarrow ud,\qquad 0u\leftrightarrow u0,\qquad 0d\leftrightarrow d0.(6)

These moves make all paths in the same equivalence class have equal amplitude. The frustration-free Hamiltonian isH=Πb+∑j=1N−1Πj,j+1,H=\Pi_{\rm b}+\sum_{j=1}^{N-1}\Pi_{j,j+1},(7)

whereΠi,j\displaystyle\Pi_{i,j}=\displaystyle=(|ϕ⟩​⟨ϕ|+|ψu⟩​⟨ψu|+|ψd⟩​⟨ψd|)i,j,\displaystyle\left(|\phi\rangle\langle\phi|+|\psi_{u}\rangle\langle\psi_{u}|+|\psi_{d}\rangle\langle\psi_{d}|\right)_{i,j},(8)

withΠb\Pi_{\rm b}the boundary termΠb\displaystyle\Pi_{\rm b}=\displaystyle=|↓⟩⟨↓|1+|↑⟩⟨↑|N.\displaystyle|\downarrow\rangle\langle\downarrow|_{1}+|\uparrow\rangle\langle\uparrow|_{N}.(9)

and|ϕ⟩\displaystyle\ket{\phi}=\displaystyle=12​(|↑↓⟩−|00⟩),\displaystyle\frac{1}{\sqrt{2}}(\ket{\uparrow\downarrow}-\ket{00}),(10)|ψu⟩\displaystyle\ket{\psi_{u}}=\displaystyle=12​(|↑0⟩−|0↑⟩),\displaystyle\frac{1}{\sqrt{2}}(\ket{\uparrow 0}-\ket{0\uparrow}),(11)|ψd⟩\displaystyle\ket{\psi_{d}}=\displaystyle=12​(|↓0⟩−|0↓⟩).\displaystyle\frac{1}{\sqrt{2}}(\ket{\downarrow 0}-\ket{0\downarrow}).(12)

The bulk projectors enforce equal amplitudes within each equivalence class, while the boundary terms remove all classes exceptC0,0​(N)C_{0,0}(N). Eq. (4) is therefore the unique zero-energy ground state.

Fors≥2s\geq 2, each site carries|0⟩\ket{0},|uk⟩\ket{u^{k}}, or|dk⟩\ket{d^{k}}, withk=1,…,sk=1,\ldots,s. The parent Hamiltonian[40]adds local terms that enforce color matching:H=Πb+∑j=1N−1Πj,j+1+∑j=1N−1Πj,j+1c,H=\Pi_{\rm b}+\sum_{j=1}^{N-1}\Pi_{j,j+1}+\sum_{j=1}^{N-1}\Pi_{j,j+1}^{\rm c},(13)

whereΠb\displaystyle\Pi_{\rm b}=\displaystyle=∑k=1s(|dk⟩​⟨dk|1+|uk⟩​⟨uk|N),\displaystyle\sum_{k=1}^{s}\left(|d_{k}\rangle\langle d_{k}|_{1}+|u_{k}\rangle\langle u_{k}|_{N}\right),(14)Πi,j\displaystyle\Pi_{i,j}=\displaystyle=∑k=1s(|Dk⟩​⟨Dk|+|Uk⟩​⟨Uk|+|ϕk⟩​⟨ϕk|)i,j,\displaystyle\sum_{k=1}^{s}\left(|D_{k}\rangle\langle D_{k}|+|U_{k}\rangle\langle U_{k}|+|\phi_{k}\rangle\langle\phi_{k}|\right)_{i,j},(15)Πi,jc\displaystyle\Pi_{i,j}^{\rm c}=\displaystyle=∑k≠l|uk​dl⟩​⟨uk​dl|i,j,\displaystyle\sum_{k\neq l}|u_{k}d_{l}\rangle\langle u_{k}d_{l}|_{i,j},(16)

with|Dk⟩\displaystyle\ket{D_{k}}=\displaystyle=12​(|dk​0⟩−|0​dk⟩),\displaystyle\frac{1}{\sqrt{2}}(\ket{d_{k}0}-\ket{0d_{k}}),(17)|Uk⟩\displaystyle\ket{U_{k}}=\displaystyle=12​(|uk​0⟩−|0​uk⟩),\displaystyle\frac{1}{\sqrt{2}}(\ket{u_{k}0}-\ket{0u_{k}}),(18)|ϕk⟩\displaystyle\ket{\phi_{k}}=\displaystyle=12​(|uk​dk⟩−|00⟩).\displaystyle\frac{1}{\sqrt{2}}(\ket{u_{k}d_{k}}-\ket{00}).(19)

The cross projectors remove locally mismatched adjacent pairs. Together with the equivalence
moves in Eq. (6), these local terms select
Eq. (5) as the unique zero-energy ground state. The cases=1s=1reduces to
the colorless Hamiltonian becauseΠc\Pi^{\rm c}vanishes.

## II.2Entanglement entropy

The unusual entanglement of Motzkin states follows from a Schmidt decomposition organized by the
height at the bipartition. For a half-chain cut, the left half can end at heighthh, while the
right half must start from the same height and return to zero. In the colorless case, the Schmidt
sectors are labeled only byhh, and their weights are fixed by the number of partial Motzkin
paths with boundary heighthh. This gives the logarithmic violation of the area law[3],Ss=1​(N2)=12​ln⁡N+𝒪​(1).S_{s=1}\left(\frac{N}{2}\right)=\frac{1}{2}\ln N+\mathcal{O}(1).(20)

The colored case is much more strongly entangled. If the height at the cut ishh, thehhunmatched up steps crossing the cut can carryshs^{h}independent color strings. Since typical
heights scale ash∼Nh\sim\sqrt{N}, this color degeneracy produces a supercriticalN\sqrt{N}contribution to the entropy[40]. In natural logarithms,
the half-chain entropy behaves asymptotically asSs≥2​(N2)=2​ln⁡(s)​κ​Nπ+12​ln⁡(π​κ​N)+𝒪​(1),S_{s\geq 2}\left(\frac{N}{2}\right)=2\ln(s)\sqrt{\frac{\kappa N}{\pi}}+\frac{1}{2}\ln(\pi\kappa N)+\mathcal{O}(1),(21)

whereκ=s/(2​s+1)\kappa=\sqrt{s}/(2\sqrt{s}+1).

Thus the colorless Motzkin chain is critical with logarithmic entanglement, whereas the colorful chain gives a rigorously solvable local spin chain with supercritical entanglement. It shows that locality and frustration-free alone do not guarantee weak entanglement.

The neural network constructions below do not compute these entropies directly; instead, they reproduce the exact support and uniform amplitudes from which the Schmidt decompositions and entanglement scalings follow.

## IIINeural Representation of the Colorless Motzkin State

For the colorless Motzkin state, exact neural representation amounts to enforcing the path
constraints in Eq. (3) while assigning the same amplitude to every legal
configuration. This can be done in two steps: first compute each prefix heightStS_{t}, and then
convert the nonnegativity and return-to-zero conditions into multiplicative gates. Based on this
principle, we construct four exact neural-network realizations for the colorless Motzkin state,
including recurrent neural network (RNN)[16,27,26], feedforward neural
network (FNN)[45,46,13], convolutional neural network
(CNN)[34,32,25,37], and transformer[49,14,52].

Throughout the constructions below, the activation function is defined byσ​(x)≡ReLU​(x)=max⁡(x,0).\sigma(x)\equiv\mathrm{ReLU}(x)=\max(x,0).(22)

The network output must be divided byMN,s\sqrt{M_{N,s}}to ensure proper normalization of the wavefunction. To illustrate the architecture, we present graphical representations for a chain of lengthN=4N=4. However, the formalism applies generally to arbitraryNN.

## III.1Recurrent Neural Network (RNN)

The RNN architecture provides the most natural framework for realizing the Motzkin state in both the colorless and colored cases (the latter being discussed in Sec.IV.1). Each neuron receives as input the local signal at the current site together with the hidden state from the preceding neuron, initialized by a parameter for the first neuron. This sequential dependence precludes parallel computation. However, it endows the RNN an intrinsic capacity for prefix summation and the associated constraint verification, both of which are essential for constructing the Motzkin state.

A recurrent network is illustrated schematically asx1x_{1}x2x_{2}x3x_{3}x4x_{4}h1h_{1}h2h_{2}h3h_{3}h4h_{4}Φ1\Phi_{1}Φ2\Phi_{2}Φ3\Phi_{3}Φ0\Phi_{0}Φ4=(Ψ​(X)S4)\Phi_{4}=\begin{pmatrix}\Psi(X)\\
S_{4}\end{pmatrix}

with input configurationX=(x1,x2,…,xN)X=(x_{1},x_{2},...,x_{N}).
It storesΦi=(ψi,Si)T\Phi_{i}=(\psi_{i},S_{i})^{T}, whereΦi\Phi_{i}is the legality judgment of the input configuration until siteiiandSiS_{i}is the prefix sum. And the initialization parameter for neuronh1h_{1}isΦ0=(1,0)T\Phi_{0}=(1,0)^{T}. The operation in each neuron isSi\displaystyle S_{i}=\displaystyle=Si−1+xi,\displaystyle S_{i-1}+x_{i},(23)ψi\displaystyle\psi_{i}=\displaystyle=ψi−1⋅σ​[1−hi​(Si)],\displaystyle\psi_{i-1}\cdot\sigma\left[1-h_{i}(S_{i})\right],(24)hi​(Si)\displaystyle h_{i}(S_{i})=\displaystyle=σ​(−Si)+δi,N⋅σ​(Si).\displaystyle\sigma(-S_{i})+\delta_{i,N}\cdot\sigma(S_{i}).(25)

Thusψi=1\psi_{i}=1iff all constraints up to siteiihave been satisfied, and the network outputΨ​(X)=ψN\Psi(X)=\psi_{N}is the exact support indicator.

## III.2Feedforward Neural Network (FNN)

The colorless Motzkin state can also be realized by generating the prefix sum through a linear transformation with a lower-triangular matrixWW, and outputting the legality constraintΨi\Psi_{i}at each site via a designed activation function. The resulting wavefunctionΨ​(X)\Psi(X)is a product of the local amplitudesψi\psi_{i}, which naturally yields a Motzkin state with equal-amplitude superposition over all legal configurations.

The FNN representation of the colorless Motzkin state is schematically depicted asx1x_{1}x2x_{2}x3x_{3}x4x_{4}S1S_{1}S2S_{2}S3S_{3}S4S_{4}ψ1\psi_{1}ψ2\psi_{2}ψ3\psi_{3}ψ4\psi_{4}WWActivationΨ​(X)=∏iψi\Psi(X)=\displaystyle\prod_{i}\psi_{i}

Starting from the input configurationX=(x1,x2,…,xN)X=(x_{1},x_{2},\ldots,x_{N}), this network uses a lower-triangular matrixWi​j={1,j≤i,0,j>i,W_{ij}=\begin{cases}1,&j\leq i,\\
0,&j>i,\end{cases}(26)

to map the configuration to a sequence of prefix sumsSi=∑jWi​j​xj=∑j=1ixj.S_{i}=\sum_{j}W_{ij}x_{j}=\sum_{j=1}^{i}{x_{j}}.(27)

While the linear transformation layerWWis fully connected, only solid lines corresponding to nonzero entriesWi​jW_{ij}are plotted for this particular construction.

EachSiS_{i}is subsequently fed into an activation functionψi=σ​[1−σ​(−Si)−δi,N⋅σ​(Si)].\psi_{i}=\sigma\left[1-\sigma(-S_{i})-\delta_{i,N}\cdot\sigma(S_{i})\right].(28)

Since allSiS_{i}take integer values, the outputs satisfyψi=1\psi_{i}=1iffSi≥0S_{i}\geq 0for alli<Ni<Notherwise 0, andψN=1\psi_{N}=1iffSN=0S_{N}=0otherwise 0.

The final wavefunction is a product of allψi\psi_{i}Ψ​(X)=∏i=1Nψi​(X)\Psi(X)=\prod_{i=1}^{N}\psi_{i}(X)(29)

which constitutes an exact neural network representation of the colorless Motzkin state.

## III.3Convolutional Neural Network (CNN)

In the FNN construction, a linear transformationWWis introduced to compute the prefix sums. The same objective can be achieved with a CNN. In the convolutional realization,WWis replaced by a convolutional layer that introducesN−1N-1ancilla nodes and generates the prefix sums sequentially. For example,S1S_{1}is produced asAncillaInput X000x1x_{1}x2x_{2}x3x_{3}x4x_{4}S1S_{1}S2S_{2}S3S_{3}S4S_{4}1111Kernel

Similarly,S3S_{3}is obtained fromAncillaInput X000x1x_{1}x2x_{2}x3x_{3}x4x_{4}S1S_{1}S2S_{2}S3S_{3}S4S_{4}1111Kernel

and the remaining prefix sums follow in the same manner. Here, theN−1N-1ancilla are initialized to 0 and placed ahead of the input arrayXX, so that the full input configurationxix_{i}comprises2​N−12N-1nodes, withxi=0x_{i}=0fori≤0i\leq 0and the physical input otherwise. A uniform convolution kernelKerneli=1,(1≤i≤N){\rm Kernel}_{i}=1,\qquad(1\leq i\leq N)(30)

is then applied, where the kernel window acting onxix_{i}covers theNNnodes{xj;j=i−N+1,…,i}\{x_{j};\,j=i-N+1,\dots,i\}counting backwards fromxix_{i}. This convolution yieldsSi=∑j=1NKernelj⋅xi+j−N=∑j=1ixj.S_{i}=\sum_{j=1}^{N}{{\rm Kernel}_{j}\cdot x_{i+j-N}}=\sum_{j=1}^{i}x_{j}\,.(31)

which reproduces precisely the triangular map of Eq. (26). Finally, the gates of Eq. (28), together with the production rule of Eq. (29) complete the CNN representation of the Motzkin state.

## III.4Transformer

The transformer, which is the most prevalent neural network architecture to date, owes its success to its all-to-all connectivity, which captures correlations at all scales. The Motzkin state can also be represented by a single-layer transformer, as depicted inx1x_{1}x2x_{2}x3x_{3}x4x_{4}EmbeddingActivationResidualz10z_{1}^{0}z20z_{2}^{0}z30z_{3}^{0}z40z_{4}^{0}z11z_{1}^{1}z21z_{2}^{1}z31z_{3}^{1}z41z_{4}^{1}ATTNh1h_{1}h2h_{2}h3h_{3}h4h_{4}ψ1\psi_{1}ψ2\psi_{2}ψ3\psi_{3}ψ4\psi_{4}Ψ​(X)=∏iψi\Psi(X)=\displaystyle\prod_{i}{\psi_{i}}

Although it seems that the transformer construction is more complicated in the figure, the attention block works similarly toWWmatrix in FNN and the convolution kernel and outputs a prefix average for every site. The advantage of the transformer is that it can be most easily generalized to other models we may further investigate, e.g., some perturbed situation of the Motzkin model.

This transformer architecture consists of an attention block mappingz0z^{0}toz1z^{1}, followed by an activation block mappingz1z^{1}toψ\psi. Below, we describe each block in detail.

## III.4.1Attention block

In this transformer construction, each site is first embedded aszi0=(xi,ei,0)T∈ℝN+2,z_{i}^{0}=(x_{i},e_{i},0)^{T}\in\mathbb{R}^{N+2},(32)

whereeie_{i}is theiith standard basis vector in position space, i.e.(ei)j=δi,j,(e_{i})_{j}=\delta_{i,j},(33)

and the last component is left empty to receive the attention output.

The attention block uses the projection matricesWQ,WK,WVW_{Q},W_{K},W_{V}to map the inputz0z^{0}into queries, keys, and values, respectively. The queries and keys are combined into Logit scores, which a softmax converts into attention weightsα​(t,i)\alpha(t,i). These weights then multiply the values, and the resulting output, added to the residual (herez0z^{0}itself), yields thez1z^{1}layer. Graphically, this block isz10z_{1}^{0}z20z_{2}^{0}z30z_{3}^{0}z40z_{4}^{0}ATTNWQ​zt0=et​WQposW_{Q}z_{t}^{0}=e_{t}W_{Q}^{\mathrm{pos}}WK​zi0=ei​WKposW_{K}z_{i}^{0}=e_{i}W_{K}^{\mathrm{pos}}WV​zj0=xjW_{V}z_{j}^{0}=x_{j}Logit​(t,i)\mathrm{Logit}(t,i)α​(t,i)\alpha(t,i)At=SttA_{t}=\displaystyle\frac{S_{t}}{t}z11z_{1}^{1}z21z_{2}^{1}z31z_{3}^{1}z41z_{4}^{1}Residual

To implement a causally masked attention layer, we take the positional key matrix to be the identity,WKpos=INW_{K}^{\rm pos}=I_{N}, and the positional query matrix to beWQpos​(t,i)={0,i≤t,−∞,i>t,W_{Q}^{\rm pos}(t,i)=\begin{cases}0,&i\leq t,\\
-\infty,&i>t,\end{cases}(34)

or, equivalently, a finite penalty−C-Cin the limitC→∞C\to\infty. Setting the first and the last rows and columns ofWQ/KW_{Q/K}to zero so thatWQ/KW_{Q/K}acts only on the position subspace and decouples the physical variable and the empty slot from the attention scores, givingWQ​zt0⋅WK​zi0=et​WQpos⋅ei​WKposW_{Q}z_{t}^{0}\cdot W_{K}z_{i}^{0}=e_{t}W_{Q}^{\mathrm{pos}}\cdot e_{i}W_{K}^{\mathrm{pos}}(35)

The logit score between sitettand siteiiis thenLogit​(t,i)=WQ​zt0⋅WK​zi0={0,i≤t,−∞,i>t.\displaystyle\mathrm{Logit}(t,i)=W_{Q}z_{t}^{0}\cdot W_{K}z_{i}^{0}=\begin{cases}0,&i\leq t,\\
-\infty,&i>t.\end{cases}(36)

The softmax therefore yields exact causal weightsαt,i=exp⁡(Logit​(t,i))∑jexp⁡(Logit​(t,j))={1/t,i≤t,0,i>t,\alpha_{t,i}=\frac{\exp(\mathrm{Logit}(t,i))}{\sum_{j}{\exp(\mathrm{Logit}(t,j)})}=\begin{cases}1/t,&i\leq t,\\
0,&i>t,\end{cases}(37)

and choosing the value matrixWVW_{V}to extract the physical variable, i.e.(WV)i​j\displaystyle(W_{V})_{ij}=\displaystyle={1i=N+2,j=1,0otherwise,\displaystyle\begin{cases}1&i=N+2,\,j=1,\\
0&\mathrm{otherwise},\end{cases}(38)WV​zi0\displaystyle W_{V}z_{i}^{0}=\displaystyle=(0,0,…,0,xi)T,\displaystyle(0,0,\dots,0,x_{i})^{T},(39)

the attention output at sitettbecomes the prefix averageAt=∑i=1Nαt,i​xi=1t​∑i=1txi=Stt.A_{t}=\sum_{i=1}^{N}\alpha_{t,i}x_{i}=\frac{1}{t}\sum_{i=1}^{t}x_{i}=\frac{S_{t}}{t}.(40)

After the residual connection, the intermediate vector readszt1=(xt,et,St/t)T.z_{t}^{1}=(x_{t},e_{t},S_{t}/t)^{T}.(41)

i.e., the firstN+1N+1components inzt1z_{t}^{1}are inherited unchanged fromzt0z_{t}^{0}, while the last componentSt/tS_{t}/tis supplied by the attention block and equals the prefix average at sitett. In numerical implementations, one may replace−∞-\inftyby a large negative constant−C-C. The exact limit is recovered by the standard hard causal mask or by theC→∞C\to\inftylimit.

## III.4.2Activation

Starting fromzt1=(xt,et,S¯t)Tz_{t}^{1}=(x_{t},e_{t},\bar{S}_{t})^{T}, obtained from the attention block with a residual connection, we define the hidden unit at sitettasht​(zt1)\displaystyle h_{t}(z_{t}^{1})=\displaystyle=σ​(−t​S¯t)+σ​(1−N+t)​σ​(t​S¯t)\displaystyle\sigma\left(-t\bar{S}_{t}\right)+\sigma(1-N+t)\sigma\left(t\bar{S}_{t}\right)(42)=\displaystyle=σ​(−St)+δt,N​σ​(St).\displaystyle\sigma\left(-S_{t}\right)+\delta_{t,N}\sigma\left(S_{t}\right).

The corresponding site gate isψt=σ​[1−ht​(zt1)],\psi_{t}=\sigma\left[1-h_{t}(z_{t}^{1})\right],(43)

which can be written explicitly asψt={σ​[1−σ​(−St)],t<N,σ​[1−σ​(−SN)−σ​(SN)],t=N.\psi_{t}=\begin{cases}\sigma\left[1-\sigma(-S_{t})\right],&t<N,\\
\sigma\left[1-\sigma(-S_{N})-\sigma(S_{N})\right],&t=N.\end{cases}(44)

SinceStS_{t}is integer-valued,ψt=1\psi_{t}=1iff the corresponding Motzkin height constraint is satisfied, whereasψt=0\psi_{t}=0otherwise. Thus, the product of all site gates enforces the Motzkin constraints and yields the Motzkin-state amplitude.

## IVNeural Representation of the Colorful Motzkin States

Colorless neural network constructions demonstrate that height constraints can be exactly enforced via neural gates. In contrast, the legality of colorful Motzkin states depends not only on path height, but also on the sequential order of color opening and closing operations. Characterizing valid configurations thus requires tracking the stack of unmatched colors and enforcing the corresponding last-in-first-out matching rule. In this section, we construct neural networks that implement this stack-based memory mechanism while maintaining uniform amplitudes across all valid colorful Motzkin paths.

Fors≥2s\geq 2, each incrementxix_{i}is specified by a height incrementΔi\Delta_{i}and a color labelcic_{i}:xix_{i}cic_{i}Δi\Delta_{i}

The height incrementΔi\Delta_{i}

is defined independently of the color label viaΔi={+1,xi=uk,0,xi=0,−1,xi=dk,\Delta_{i}=\begin{cases}+1,&x_{i}=u^{k},\\
0,&x_{i}=0,\\
-1,&x_{i}=d^{k},\end{cases}(45)

while the color label is set toci=kc_{i}=kfor bothuku^{k}anddkd^{k}.

Valid colored equivalence moves are given by the pairwise local transformations[40,39]0​dk↔dk​0,0​uk↔uk​0,00↔uk​dk.0d^{k}\leftrightarrow d^{k}0,\qquad 0u^{k}\leftrightarrow u^{k}0,\qquad 00\leftrightarrow u^{k}d^{k}.(46)

Beyond the height constraint, colorful Motzkin paths obey a strict last-in-first-out color-matching condition. Any downward stepdkd^{k}must exclusively close the most recent unmatched upward stepuku^{k}. A valid height profile is therefore a necessary but not sufficient condition for path legality. For instance, the state|u1​d2⟩\ket{u^{1}d^{2}}exhibits a valid height sequence(1,0)(1,0)yet corresponds to an illegal colorful path due to mismatched color ordering.

To systematically track color matching information, we adopt a stack structure as the minimal causal memory unit and decompose the stack vectorqiq_{i}asqi=⨁h=1qih,qih∈0,±1,…±s,q_{i}=\bigoplus_{h=1}q_{i}^{h},\qquad q_{i}^{h}\in{0,\pm 1,\ldots\pm s},(47)

where each componentqi(h)q_{i}^{(h)}encodes the color of the unmatched upward step residing at heighthh. We further introduceχi\chi_{i}as a local color validity flag, such thatχi=1\chi_{i}=1if the current color configuration satisfies the last-in-first-out matching rule, andχi=0\chi_{i}=0otherwise.

LetSi−1S_{i-1}denote the stack height prior to processing siteii. The update rules for the stack vectorqiq_{i}and color flagχi\chi_{i}fall into three distinct cases:Push(xi=uk)(x_{i}=u^{k})

SetqiSi−1+1=ciq_{i}^{S_{i-1}+1}=c_{i}, inherit all remaining entries ofqi−1q_{i-1}to form the full stack vectorqiq_{i}, and assign the local color flagχi=1\chi_{i}=1:Flat(xi=0)(x_{i}=0)

Preserve the stack state by settingqi=qi−1q_{i}=q_{i-1}andχi=1\chi_{i}=1:Pop(xi=dk)(x_{i}=d^{k})

IfSi−1=0S_{i-1}=0or the color stored at the current stack topqi−1Si−1≠ciq_{i-1}^{S_{i-1}}\neq c_{i}, leave the stack state unchanged and setχi=0\chi_{i}=0. Otherwise, copy the full stackqi−1q_{i-1}toqiq_{i}, erase the stack-top entry at heightSi−1S_{i-1}, and setχi=1\chi_{i}=1:

Corresponding to these three cases, the stack vectorqiq_{i}is updated according to the equationqi={qi−1⊕ci,if​Δi=1,qi−1/qi−1Si−1,if​ci=qi−1Si−1,Δi=−1,qi−1,otherwise,q_{i}=\begin{cases}q_{i-1}\oplus c_{i},&{\rm if}\,\,\Delta_{i}=1,\\
q_{i-1}/q^{S_{i-1}}_{i-1},&{\rm if}\,c_{i}=q_{i-1}^{S_{i-1}},\,\Delta_{i}=-1,\\
q_{i-1},&{\rm otherwise},\end{cases}(48)

whereqi−1/qi−1Si−1q_{i-1}/q^{S_{i-1}}_{i-1}denotes the removal of the top elementqi−1Si−1q^{S_{i-1}}_{i-1}from the stack vectorqi−1q_{i-1}.
The color validity flag follows the update equationχi={0if​Δi=−1,ci≠qi−1Si−1,,1,otherwise.\chi_{i}=\begin{cases}0&{\rm if}\,\,\Delta_{i}=-1,\,\,c_{i}\not=q_{i-1}^{S_{i-1}},,\\
1,&{\rm otherwise}.\end{cases}(49)

The ReLU color gatevi=σ​(χi)v_{i}=\sigma(\chi_{i})(50)

is one iff the color operation at siteiiis stack-consistent.

## IV.1Stack-augmented RNN

Similar to the colorless case discussed in Sec.III.1, RNN gives a direct method to construct a representation of a colorful Motzkin state. However, because of the extra color rule, the previous RNN structure can not satisfy our requirement. Therefore, we use a stack-augmented RNN structure, which contains a height RNN and a color RNN, to recurrently determine the height and color wavefunctions, respectively.

Analogous to the colorless formulation presented in Sec.III.1, RNN provides a natural framework for constructing neural-network representations of colorful Motzkin states. However, the additional color-matching constraints invalidate the standard RNN architecture designed for colorless paths, which only enforces height consistency. To resolve this limitation, we adopt a stack-augmented dual-branch RNN structure, consisting of a height RNN and a color RNN. The two branches perform recurrent updates independently to characterize the height wavefunction and color configuration wavefunction, respectively.

For the height branch, we inherit the variablesΦi\Phi_{i}andhih_{i}defined in the colorless RNN framework (Sec.III.1). Replacing the inputxix_{i}in Eqs. (23–25) with the height incrementΔi\Delta_{i}yields the feed-forward update pipeline for the height subnetworkΔ1\Delta_{1}Δ2\Delta_{2}Δ3\Delta_{3}Δ4\Delta_{4}h1h_{1}h2h_{2}h3h_{3}h4h_{4}Φ1\Phi_{1}Φ2\Phi_{2}Φ3\Phi_{3}Φ0\Phi_{0}Φ4=(ψ4S4)\Phi_{4}=\begin{pmatrix}\psi_{4}\\
S_{4}\end{pmatrix}

The final outputΦN=(ψN,SN)T\Phi_{N}=(\psi_{N},S_{N})^{T}(illustrated here forN=4N=4) encodes the height validity indicatorψN\psi_{N}, which quantifies whether the path satisfies the global height constraint.

Complementing the height branch, we design a structurally consistent RNN subnetwork to model color dynamicsx1x_{1}x2x_{2}x3x_{3}x4x_{4}h~1\tilde{h}_{1}h~2\tilde{h}_{2}h~3\tilde{h}_{3}h~4\tilde{h}_{4}R1R_{1}R2R_{2}R3R_{3}R0R_{0}R4=(χ~4q4)R_{4}=\begin{pmatrix}\tilde{\chi}_{4}\\
q_{4}\end{pmatrix}

This color RNN evolves the composite color state vectorRi=(χ~iqi),R_{i}=\begin{pmatrix}\tilde{\chi}_{i}\\
q_{i}\end{pmatrix},(51)

whereqiq_{i}is the color stack vector,χi\chi_{i}denotes the local color validity flag andχ~i\tilde{\chi}_{i}denotes the prefix color validity flag. The initial state is set toR0=(1,∅)TR_{0}=(1,\emptyset)^{T}. Each hidden neuronh~i\tilde{h}_{i}takes (Ri−1,Δi,ciR_{i-1},\Delta_{i},c_{i}) as input, it recursively updates the stack vectorqiq_{i}following Eq. (48) with the local color validity flagχi\chi_{i}following Eq. (49), and global validity flagχ~i\tilde{\chi}_{i}is generated byχ~i=χ~i−1​χi.\tilde{\chi}_{i}=\tilde{\chi}_{i-1}\chi_{i}\,.(52)

The update ofχ~t\tilde{\chi}_{t}, which is equivalent to the product over all local color-validity flags, ensures that a color mismatch at any intermediate site permanently sets the wave-function amplitude to zero. Together with the height indicatorψN\psi_{N}, the resulting wave function,Ψ​(X)=ψN​χ~N,\Psi(X)=\psi_{N}\tilde{\chi}_{N},(53)

satisfiesΨ​(X)=1\Psi(X)=1iffXXis a valid colorful Motzkin path, and vanishes otherwise.

## IV.2Feedforward Neural Network

The last-in-first-out stack rule can be viewed as a causal pointer. For a down step at siteii, its matching up step is the most recent preceding up step satisfying the height consistency conditionSi−1=Si+1S_{i-1}=S_{i}+1, where the post-up height of the matched up step equals the pre-pop height of the target down step. Such paired up-down motion lies on the same horizontal level. This observation suggests that we can slightly modify the colorless FNN architecture to obtain an FNN representation for the colorful case.

The proposed colorful FNN retains the hierarchical layer design of the original colorless framework. Specifically, one dedicated layer is employed to compute prefix sums identically to the colorless state, followed byN−1N-1successive layers that encode the nearest preceding up-step information for each input site. A full schematic visualization of this network is presented below:EmbeddingW1W^{1}W2W^{2}+ActivationW3W^{3}+ActivationW4W^{4}+ActivationActivationx1x_{1}x2x_{2}x3x_{3}x4x_{4}z10z_{1}^{0}z20z_{2}^{0}z30z_{3}^{0}z40z_{4}^{0}z11z_{1}^{1}z21z_{2}^{1}z31z_{3}^{1}z41z_{4}^{1}z12z_{1}^{2}z22z_{2}^{2}z32z_{3}^{2}z42z_{4}^{2}z13z_{1}^{3}z23z_{2}^{3}z33z_{3}^{3}z43z_{4}^{3}z14z_{1}^{4}z24z_{2}^{4}z34z_{3}^{4}z44z_{4}^{4}ψ1\psi_{1}ψ2\psi_{2}ψ3\psi_{3}ψ4\psi_{4}Ψ​(X)=∏iψi\Psi(X)=\displaystyle\prod_{i}\psi_{i}Residual

We first embed each input configuration into a 4-dimensional feature vectorzik=(Δi,ci,Si,nik)T,z_{i}^{k}=(\Delta_{i},c_{i},S_{i},n_{i}^{k})^{T},(54)

initialized aszi0=(Δi,ci,0,σ​(xi))T.z_{i}^{0}=(\Delta_{i},c_{i},0,\sigma(x_{i}))^{T}.(55)

Here,nikn_{i}^{k}denotes the color attribute of the nearest preceding up step for theii-th site, captured up to thekk-th layer, while the indexkkenumerates the hierarchical layers of the FNN.

As in the colorless FNN, the prefix sum of height increments is determined by the linear transformationSi=∑jWi​j1​Δj,S_{i}=\sum_{j}W_{ij}^{1}\Delta_{j},(56)

whereW1=WW^{1}=Wis the lower triangular matrix, defined in Eq. (26). Together with the residual connection, this yields
havezi1=(Δi,ci,Si,σ​(xi))T.z_{i}^{1}=(\Delta_{i},c_{i},S_{i},\sigma(x_{i}))^{T}.(57)

For the subsequent2≤k≤N2\leq k\leq Nlayers (withN=4N=4here), we implement a layer-specific linear transformation:(pi,di,bi)=∑jWi​jk​(cj,Sj,Δj),\left(p_{i},d_{i},b_{i}\right)=\sum_{j}W_{ij}^{k}\left(c_{j},S_{j},\Delta_{j}\right),(58)

where the auxiliary variablespip_{i},did_{i}, andbib_{i}are intermediate features encoding color information, prefix sum values, and height increments, respectively. The layer-specific weight matrix obeys the binary ruleWi​jk=δj,i−k+1W_{ij}^{k}=\delta_{j,i-k+1}(59)

This weight design enables thekkth layer to extract(pi,di,bi)(p_{i},d_{i},b_{i})from thekkth preceding site(i−k+1)(i-k+1).

The layer-wise activation function is defined asd​nik=pi​δnik−1,0​δdi,Si+1​δbi,1.dn_{i}^{k}=p_{i}\delta_{n_{i}^{k-1},0}\delta_{d_{i},S_{i}+1}\delta_{b_{i},1}.(60)

The updated​nik=pidn_{i}^{k}=p_{i}is activated iff the(i+1−k)(i+1-k)-th site is an up step horizontally aligned with theiith site, and no valid color is stored innik−1n_{i}^{k-1}in prior layers. Under this condition, the updated featurenik−1+d​nikn_{i}^{k-1}+dn_{i}^{k}stores the valid color information of the matched up step.

Note that the Kronecker delta functions in the activation can be fully implemented via rectified linear unit (ReLU) activations, through the identitiesδx,y\displaystyle\delta_{x,y}=\displaystyle=σ​(1−|x−y|)\displaystyle\sigma(1-|x-y|)(61)|x|\displaystyle|x|=\displaystyle=σ​(x)+σ​(−x)\displaystyle\sigma(x)+\sigma(-x)(62)

After applying residual connections, the updated feature vector readszik=(Δi,ci,Si,nik−1+d​nik)T.z_{i}^{k}=(\Delta_{i},c_{i},S_{i},n_{i}^{k-1}+dn_{i}^{k})^{T}.(63)

After propagating through all layers, the final output feature vector converges toziN=(Δi,ci,Si,ni)T,z_{i}^{N}=(\Delta_{i},c_{i},S_{i},n_{i})^{T},(64)

wherenin_{i}uniquely encodes the color information of the nearest valid preceding up step. The site-wise wavefunctionψi​(X)\psi_{i}(X)is then computed via a composite activation function:ψi​(X)\displaystyle\psi_{i}(X)=\displaystyle=yi​(ziN)​vi​(ziN)\displaystyle y_{i}(z_{i}^{N})\,v_{i}(z_{i}^{N})(65)yi​(ziN)\displaystyle y_{i}(z_{i}^{N})=\displaystyle=σ​(1−σ​(−Si)−σ​(i−N+1)​σ​(Si))\displaystyle\sigma(1-\sigma(-S_{i})-\sigma(i-N+1)\sigma(S_{i}))(66)vi​(ziN)\displaystyle v_{i}(z_{i}^{N})=\displaystyle=(1−δΔi,−1)+δni,ci​δΔi,−1\displaystyle(1-\delta_{\Delta_{i},-1})+\delta_{n_{i},c_{i}}\delta_{\Delta_{i},-1}(67)

Here,yiy_{i}enforces the height validity, whileviv_{i}imposes the color consistency constraint for each configuration.
Finally, we get the wavefunctionΨ​(X)=∏iψi\Psi(X)=\prod_{i}\psi_{i}up to a normalization constant.

One potential concern is that the color validity termviv_{i}does not explicitly constrain the stack to be empty afterNNmoves. This omission, however, does not affect the validity of the construction. A non-empty stack will result in a non-zero final height, which is strictly penalized by the height validity product∏iyi\prod_{i}y_{i}. In such cases, the overall wavefunction amplitude vanishes.

We note that an analogous modification applies to the colorful CNN construction, starting from its colorless counterpart. The first layer employs the same convolution kernel as in the colorless case, while for all subsequent layers2≤k≤N2\leq k\leq N, we employ one-hot convolution kernels defined by(Kernelk)j=δj,N−k+1,(\mathrm{Kernel}_{k})_{j}=\delta_{j,N-k+1},(68)

which reproduce the exact feature extraction operations of the corresponding FNN layers described above. Given the structural consistency and functional equivalence between the modified FNN and CNN for colorful cases, we do not present a separate section devoted to the CNN construction.

## IV.3Transformer

Beyond the ansatz built on FNN, CNN, and stack-augmented RNN, we propose an alternative construction leveraging causally masked self-attention. The design adopts a three-layer multi-head transformer equipped with hard softmax attention and pointwise multi-layer perception (MLP) modules:Embedding3-layerATTN+MLPx1x_{1}x2x_{2}x3x_{3}x4x_{4}Layer 1Layer 2Layer 3Ψ​(X)\Psi(X)

The internal layer structure is illustrated below:z1iz_{1}^{i}z2iz_{2}^{i}z3iz_{3}^{i}z4iz_{4}^{i}ATTNA1iA_{1}^{i}A2iA_{2}^{i}A3iA_{3}^{i}A4iA_{4}^{i}MLPResidual

At initialization, we embed each input configurationxtx_{t}into a 9-dimensional feature vectorzt0=(xt,t,Δt,0,0,0,0,0,1)T.z_{t}^{0}=(x_{t},t,\Delta_{t},0,0,0,0,0,1)^{T}.(69)

We now detail the function of each layer in sequence.

Layer 1: prefix sums and height constraints.We set the projection weightsWQ1=WK1=0,WV1=e1​e3T,W_{Q}^{1}=W_{K}^{1}=0,\quad W_{V}^{1}=e_{1}e_{3}^{T},(70)

wheree1e_{1}ande3e_{3}are the first and third one-hot basis in the embedded vector space, respectively. This yields,WV1​zt0=(Δt,0,0,0,0,0,0,0,0)T\displaystyle W_{V}^{1}z_{t}^{0}=(\Delta_{t},0,0,0,0,0,0,0,0)^{T}(71)

and a lower triangular causal mask matrixMt​i\displaystyle M_{ti}=\displaystyle={0t≥i−∞t<i.\displaystyle\begin{cases}0&t\geq i\\
-\infty&t<i\end{cases}.(72)

The resulting attention logit readsLogit1​(t,i)\displaystyle\mathrm{Logit}^{1}(t,i)=\displaystyle=Mt​i+(WQ1​zt0)T​(WK1​zi0)=Mt​i.\displaystyle M_{ti}+(W_{Q}^{1}z_{t}^{0})^{T}(W_{K}^{1}z_{i}^{0})=M_{ti}\,.(73)

Following the weighting construction introduced in Eq. (37), we obtain the attention weightsα​(t,i)\displaystyle\alpha(t,i)=\displaystyle={1/t,t≥i,0,t<i.\displaystyle\begin{cases}\displaystyle 1/t,&t\geq i,\\
0,&t<i.\end{cases}(74)

Applying the averaging procedure of Eq. (40), we obtainAt1=St/tA_{t}^{1}=S_{t}/t. The subsequent MLP computesSt\displaystyle S_{t}=\displaystyle=t⋅At1=St,\displaystyle t\cdot A_{t}^{1}=S_{t},(75)St−1\displaystyle S_{t-1}=\displaystyle=St−Δt,\displaystyle S_{t}-\Delta_{t},(76)Bt\displaystyle B_{t}=\displaystyle=σ​(−St).\displaystyle\sigma(-S_{t}).(77)

Incorporating the residual connection yieldszt1=(xt,t,Δt,St,St−1,(St−1)2,Bt,0,1)T.z_{t}^{1}=\big(x_{t},t,\Delta_{t},S_{t},S_{t-1},(S_{t-1})^{2},B_{t},0,1\big)^{T}.(78)

Layer 2: color matching.The projection operators act asWQ2​zt1\displaystyle W_{Q}^{2}z_{t}^{1}=\displaystyle=(St1)\displaystyle\begin{pmatrix}S_{t}\\
1\end{pmatrix}(79)WK2​zt1\displaystyle W_{K}^{2}z_{t}^{1}=\displaystyle=(2​N​ω​St−1−N​ω​(St−1)2+ω⋅t)\displaystyle\begin{pmatrix}2N\omega S_{t-1}\\
-N\omega(S_{t-1})^{2}+\omega\cdot t\end{pmatrix}(80)WV2​zt1\displaystyle W_{V}^{2}z_{t}^{1}=\displaystyle=xt.\displaystyle x_{t}\,.(81)

Here we introduce a parameterω\omegasatisfyingω≫1\omega\gg 1, whereN​ωN\omegaandω\omegaact as filters for height and horizontal distance, respectively. This hierarchy of scales is selected to ensure the distance filter does not interfere with the height filter. Both filters decay rapidly as a function of the site separation. The corresponding attention logit becomesLogit2​(t,i)\displaystyle\mathrm{Logit}^{2}(t,i)(82)=\displaystyle=Mt,i+(WQ2​zt1)T​(WK2​zi1)\displaystyle M_{t,i}+(W_{Q}^{2}z_{t}^{1})^{T}(W_{K}^{2}z_{i}^{1})=\displaystyle=Mt,i−β​(St−Si−1)2+β​(St)2+ω⋅i.\displaystyle M_{t,i}-\beta(S_{t}-S_{i-1})^{2}+\beta(S_{t})^{2}+\omega\cdot i\,.

For fixedtt, the termβ​(St)2\beta(S_{t})^{2}shifts the logits uniformly across allii, and therefore cancels out upon softmax normalization.

The output of this attention block satisfiesAt2=xj\displaystyle A_{t}^{2}=x_{j}(83)

for every down step attt, wherejjis the most recent preceding up step sharing the same height as sitett. We note that when no such prior up step exists, attention weights become nearly uniform andAt2A_{t}^{2}may return an arbitrary color. This, however, does not affect the wavefunction since such configurations necessarily violate the height constraint and correspond to invalid paths. The MLP then evaluatesΓt=δ​(xt<0)⋅δ​(xt+At2≠0),\Gamma_{t}=\delta(x_{t}<0)\cdot\delta(x_{t}+A_{t}^{2}\neq 0),(84)

which flags a violation of the color-matching rule. With the residual connection, we obtainzt2=(xt,t,Δt,St,St−1,(St−1)2,Bt,Γt,1)T.z_{t}^{2}=\big(x_{t},t,\Delta_{t},S_{t},S_{t-1},(S_{t-1})^{2},B_{t},\Gamma_{t},1\big)^{T}.(85)

Layer 3: global aggregation and readout.We setWQ3=WK3=0,WV3​zt2=(Bt,Γt)T.W_{Q}^{3}=W_{K}^{3}=0,\quad W_{V}^{3}z_{t}^{2}=(B_{t},\Gamma_{t})^{T}.(86)

The attention output takes the formAt3=1t​∑i=1t(BiΓi)=(At3​[1]At3​[2]).\displaystyle A_{t}^{3}=\frac{1}{t}\sum_{i=1}^{t}\begin{pmatrix}{B_{i}}\\
{\Gamma_{i}}\end{pmatrix}=\begin{pmatrix}A_{t}^{3}[1]\\
A_{t}^{3}[2]\end{pmatrix}\,.(87)

Consequently,AN3A_{N}^{3}aggregates all the constraint violation statistics along the full path. The final MLP relies solely onAN3A_{N}^{3}to produce the wavefunctionyN\displaystyle y_{N}=\displaystyle=σ​(1−|SN|−N⋅AN3​[1])\displaystyle\sigma(1-|S_{N}|-N\cdot A_{N}^{3}[1])(88)vN\displaystyle v_{N}=\displaystyle=σ​(1−N⋅AN3​[2])\displaystyle\sigma(1-N\cdot A_{N}^{3}[2])(89)Ψ​(X)\displaystyle\Psi(X)=\displaystyle=σ​(yN+vN−1)=yN​vN.\displaystyle\sigma(y_{N}+v_{N}-1)=y_{N}v_{N}\,.(90)

HereyNy_{N}andvNv_{N}encode the height and color criteria, respectively. The resulting wavefunctionΨ​(X)=1\Psi(X)=1iffyN=vN=1y_{N}=v_{N}=1and 0 otherwise.

The transformer construction has a more complex architecture than the other approaches, which may seem excessive for representing Motzkin states alone. However, it offers the potential to be extended into a variational NQS for studying quantum systems related to the Motzkin model that are not exactly soluble.

## VDiscussion

## V.1Parameter complexity of neural-network representations

We have presented exact neural-network representations for both critical and supercritical Motzkin states. The colorless formulation confines the wavefunction support to prefix-sum constraints, supplemented by nonnegativity and endpoint conditions. The colorful construction further imposes a last-in-first-out color-matching rule. In all cases, the network weights are fixed analytically by the Motzkin legality rules. The different representations, however, involve distinct parameter counts, whose scaling with the system sizeNNis summarized and compared in Table1, along with their tensor-network counterparts.

The RNN construction uses few parameters, of order𝒪​(1)\mathcal{O}(1)for the colorless height rule and𝒪​(N)\mathcal{O}(N)for an explicit color stack. Its sequential update, however, is not naturally parallel, and the colorful stack operations are not differentiable. The RNN is therefore best viewed as an algorithmic template rather than a practical training ansatz.

The FNN construction encodes prefix sums through dense triangular maps. It requires anN×NN\times Nweight matrix for the colorless state andNNsuch matrices for the colorful pointer construction, giving𝒪​(N2)\mathcal{O}(N^{2})and𝒪​(N3)\mathcal{O}(N^{3})scaling, respectively. Because the colorful pointer is equivalent to the stack rule but uses only differentiable operations, the FNN and the subsequent architectures are computationally trainable.

The CNN construction replaces the denseN×NN\times Nweight matrices by convolution kernels of lengthNN. Prefix sums are then generated by convolution rather than by a full linear transform, which reduces the parameter count to𝒪​(N)\mathcal{O}(N)for the colorless state and𝒪​(N2)\mathcal{O}(N^{2})for the colorful one.

The colorful transformer employs three9×99\times 9projection matrices,WQW_{Q},WKW_{K}, andWVW_{V}, which act on the embedded vectors in each layer. Since the mask is fixed rather than variational in the general transformer construction, the total number of variational parameters scales as𝒪​(1)\mathcal{O}(1).

The colorless transformer construction presented in Sec.III.4has a simple and intuitive structure, but is not optimal in terms of parameter scaling. Because the embedded vectors have dimensionN+2N+2, each of the three projection matricesWQW_{Q},WKW_{K}, andWVW_{V}has dimensions(N+2)×(N+2)(N+2)\times(N+2). Consequently, the number of parameters scales as𝒪​(N2)\mathcal{O}(N^{2}). This scaling can nevertheless be reduced to𝒪​(1)\mathcal{O}(1)by implementing the colorless transformer within the colorful architecture presented in Sec.IV.3and settings=1s=1.Table 1:Parameter scaling versus chain lengthNNfor various representations of colorless and colorful Motzkin states. Results for the tensor-network-state (TNS) representation are shown for comparison.RepresentationColorlessColorfulRNN𝒪​(1)\mathcal{O}(1)𝒪​(N)\mathcal{O}(N)FNN𝒪​(N2)\mathcal{O}(N^{2})𝒪​(N3)\mathcal{O}(N^{3})CNN𝒪​(N)\mathcal{O}(N)𝒪​(N2)\mathcal{O}(N^{2})Transformer𝒪​(1)\mathcal{O}(1)𝒪​(1)\mathcal{O}(1)TNS𝒪​(N​log2⁡N)\mathcal{O}(N\log_{2}N)[2]𝒪​((2​s+2)4​N2)\mathcal{O}((2s+2)^{4}N^{2})[1]

All colorful constructions can represent the colorless state without structural modification. The colorless Motzkin state is thes=1s=1specialization of the colorful problem. Once the height rule is enforced, the color-matching constraint becomes vacuous. Consequently, the colorful architectures remain exact fors=1s=1if the color branch is retained but never activated, or equivalently if the color labels are fixed to a single value. The price is that one carries the full colorful parameter budget even though a dedicated colorless network would suffice. The scalings in the colorful column of Table1therefore also upper-bound the cost of representing the colorless state.

Across these architectures, the parameter counts above refer to fixed analytic weights rather than to a trained variational ansatz. All of these weights are determined by(N,s)(N,s)and by the exact masks that encode Motzkin legality. They are not variationally optimized.

## V.2Comparison with tensor-network representation

Exact tensor-network representations of Motzkin states have been constructed from elementary building-block tensors[1,2]. For the colorless Motzkin state, an exact hierarchical construction[2]uses𝒪​(N​log2⁡N)\mathcal{O}(N\log_{2}N)blocks of shape3×3×3×33\times 3\times 3\times 3, so the native tensor-network parameter count scales as𝒪​(N​log2⁡N)\mathcal{O}(N\log_{2}N). For the colorful model[1], one needs𝒪​(N2)\mathcal{O}(N^{2})building blocks of shape(2​s+2)×(2​s+2)×(2​s+2)×(2​s+2)(2s+2)\times(2s+2)\times(2s+2)\times(2s+2), giving a parameter count𝒪​(s4​N2)\mathcal{O}(s^{4}N^{2}). Relative to these native TNS costs, the comparison is architecture dependent. For the colorless state, the TNS scaling𝒪​(N​log2⁡N)\mathcal{O}(N\log_{2}N)is higher than RNN and CNN, but lower than the FNN and transformer budgets. For the colorful state, several neural-network constructions remain𝒪​(N)\mathcal{O}(N)or𝒪​(N2)\mathcal{O}(N^{2}), matching or improving upon the TNS scaling. Beyond raw parameter counting, the neural constructions offer a more direct route to generalizations such as perturbed Motzkin models.

The two frameworks are complementary rather than competing. Tensor networks encode Motzkin states through virtual spaces associated with height and color sectors, making the Schmidt structure across a cut explicit. This viewpoint underlies exact rainbow and holographic constructions[1,2]. The neural constructions instead treat the same states as recognition problems. A causal network reads the spin configuration, updates a small set of program variables, and returns a legality indicator. Tensor networks emphasize on the entanglement structure, while neural networks expose the computational structure of the support.

This distinction matters for variational many-body physics. Neural-network ansätze are often optimized as black-box function approximators, whereas exact constructions identify which architectural motifs encode which physical constraints. For Motzkin states, prefix aggregation is the natural primitive for the height rule, and a stack or attention pointer is the natural primitive for nested colors. Analogous motifs appear in other constrained states, for example, Dyck and Fredkin paths require parenthesis matching, gauge-theory wave functions require local Gauss-law constraints, stabilizer states require parity checks, and string-net or loop-gas states require global connectivity information. Therefore, the present work suggests a general route to exact or near-exact neural-network states for a wider class of quantum states.

The same perspective clarifies why anomalous entanglement need not preclude a compact neural representation. The colorful Motzkin state hasΘ​(N)\Theta(\sqrt{N})half-chain entanglement entropy because many color strings can cross a cut, yet the legality of a complete configuration is still decided by a polynomial-size causal computation. In this sense, neural- and tensor-networks diagnose different kinds of complexity. Tensor networks are sensitive to bipartite entanglement, whereas causal neural networks can exploit algorithmic structure in the computational basis. This complementarity is potentially useful for area-deformed Motzkin models[53,35], Fredkin chains[47], and Rydberg implementations of constrained spin-1 dynamics[41], where MPS bond dimensions can become large while the physically allowed configurations remain highly structured.

More broadly, Motzkin states show that exact neural-network representations can be obtained by design rather than by training. The fixed weights derived here provide benchmarks for studying optimization, sampling, and generalization in neural quantum states. This offers templates for exact neural-network representations of other quantum states whose amplitudes are governed by interpretable combinatorial rules.

## VISummary

We have constructed exact neural-network representations of both colorless and colorful Motzkin states. The constructions are fully analytic, and all weights are fixed by the system size and the Motzkin legality rules. For the colorless state, a causal prefix-sum block, realized as a recurrent update, a dense triangular map, a one-sided convolution, or a masked attention layer, computes the path heights, while position-selective ReLU gates enforce nonnegativity at every prefix and return to zero at the endpoint. For the colorful state, this height block is augmented by a last-in-first-out color block, implemented either as an explicit stack or as an attention pointer to the matching up step, which enforces the nested color-matching rule.

Despite the anomalous entanglement of the target states, logarithmic for the colorless state andO​(N)O(\sqrt{N})for the colorful state, the resulting parameter counts remain polynomial. Depending on the architecture, they scale from𝒪​(1)\mathcal{O}(1)to𝒪​(N2)\mathcal{O}(N^{2})in the colorless case and from𝒪​(N)\mathcal{O}(N)to𝒪​(N3)\mathcal{O}(N^{3})in the colorful case, and are competitive with the exact tensor-network representations.

These results show that NQS can exactly represent combinatorially constrained wavefunctions beyond the entanglement area-law. More importantly, these constructions reveal a general design principle: when the support and phase structure of a many-body state can be computed by a finite causal algorithm, the algorithm may, under suitable architectural assumptions, be compiled into a faithful neural-network representation of the state. The fixed-weight architectures constructed herein provide analytically controlled benchmarks for optimization, sampling, and generalization. Furthermore, they serve as prototypes for investigating related constrained systems, including area-deformed Motzkin models[53,35], Fredkin spin chains[47], and Rydberg simulator realizations of Motzkin-type dynamics[41].

## Acknowledgements.This work was supported by the National Key Research and Development Project of China (Grants No. 2024YFA1408604, No. 2021ZD0301800, and No. 2022YFA1403900), the National Natural Science Foundation of China (Grants No. 12488201, No. 12322403, and No. 12347107), and the Strategic Priority Research Program of Chinese Academy of Sciences (Grant No. XDB0500202).

## Code Availability

The source code used to verify the neural-network constructions at small system sizes is publicly available[50].

## References
- [1]R. N. Alexander, A. Ahmadain, Z. Zhang, and I. Klich(2019)Exact rainbow tensor networks for the colorful Motzkin and Fredkin spin chains.Phys. Rev. B100,pp. 214430.External Links:DocumentCited by:§I,§V.2,§V.2,Table 1.
- [2]R. N. Alexander, G. Evenbly, and I. Klich(2021)Exact holographic tensor networks for the Motzkin spin chain.Quantum5,pp. 546.External Links:DocumentCited by:§I,§V.2,§V.2,Table 1.
- [3]S. Bravyi, L. Caha, R. Movassagh, D. Nagaj, and P. W. Shor(2012)Criticality without frustration for quantum spin-1 chains.Phys. Rev. Lett.109,pp. 207202.External Links:DocumentCited by:§I,§II.1,§II.2,§II,§II.
- [4]P. Calabrese and J. Cardy(2004)Entanglement entropy and quantum field theory.J. Stat. Mech.2004,pp. P06002.External Links:DocumentCited by:§I.
- [5]P. Calabrese and J. Cardy(2009)Entanglement entropy and conformal field theory.J. Phys. A42,pp. 504005.External Links:DocumentCited by:§I.
- [6]G. Carleo and M. Troyer(2017)Solving the quantum many-body problem with artificial neural networks.Science355,pp. 602.External Links:DocumentCited by:§I.
- [7]A. Chen, C. Roth, Z. Wan, A. Sengupta, and A. Georges(2025)Scalable and accurate simulations of the hubbard model with neural quantum states.Note:Presented at the Machine Learning and the Physical Sciences (ML4PS) Workshop,
NeurIPS 2025External Links:LinkCited by:§I.
- [8]A. Chen, Z. Wan, A. Sengupta, A. Georges, and C. Roth(2025)Neural network-augmented Pfaffian wave-functions for scalable simulations of interacting fermions.External Links:2507.10705Cited by:§I.
- [9]J. Chen, S. Cheng, H. Xie, L. Wang, and T. Xiang(2018)Equivalence of restricted Boltzmann machines and tensor network states.Phys. Rev. B97,pp. 085104.External Links:DocumentCited by:§I.
- [10]S. Cheng, L. Wang, T. Xiang, and P. Zhang(2019)Tree tensor networks for generative modeling.Phys. Rev. B99,pp. 155131.External Links:DocumentCited by:§I.
- [11]K. Choo, A. Mezzacapo, and G. Carleo(2020)Fermionic neural-network states for ab-initio electronic structure.Nat. Commun.11,pp. 2368.External Links:DocumentCited by:§I.
- [12]K. Choo, T. Neupert, and G. Carleo(2019)Two-dimensional frustratedJ1−J2J_{1}-J_{2}model studied with neural network quantum states.Phys. Rev. B100,pp. 125124.External Links:DocumentCited by:§I.
- [13]G. Cybenko(1989)Approximation by superpositions of a sigmoidal function.Math. Control Signals Syst.2,pp. 303–314.External Links:DocumentCited by:§III.
- [14]J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova(2019)BERT: Pre-training of deep bidirectional transformers for language understanding.Proc. NAACL-HLT,pp. 4171–4186.External Links:DocumentCited by:§III.
- [15]J. Eisert, M. Cramer, and M. B. Plenio(2010)Colloquium: Area laws for the entanglement entropy.Rev. Mod. Phys.82,pp. 277.External Links:DocumentCited by:§I.
- [16]J. L. Elman(1990)Finding structure in time.Cognitive Science14(2),pp. 179–211.External Links:DocumentCited by:§III.
- [17]C. Fan, B. Zhan, Y. Gu, T. Liu, Y. Wu, M. Qin, D. Lv, and T. Xiang(2026)Disentangling tensor network states with deep neural network.External Links:2603.14425Cited by:§I.
- [18]J. Feldmeier, Y. Liu, M. D. Lukin, and S. Choi(2026)Digital dissipative state preparation for frustration-free gapless quantum systems.External Links:2603.10119Cited by:§I.
- [19]X. Gao and L.-M. Duan(2017)Efficient representation of quantum many-body states with deep neural networks.Nat. Commun.8,pp. 662.External Links:DocumentCited by:§I.
- [20]C. Gauvin-Ndiaye, J. Tindall, J. R. Moreno, and A. Georges(2024)Mott transition and volume law entanglement with neural quantum states.External Links:2311.05749Cited by:§I.
- [21]Y. Gu, Z. Han, W. Li, Z. Xiao, T. Xiang, M. Qin, L. Wang, and D. Lv(2026)Pareto frontier of neural quantum states: Scalable, affordable, and accurate convolutional backflow for strongly correlated lattice fermions.External Links:2604.25775Cited by:§I.
- [22]Y. Gu, W. Li, H. Lin, B. Zhan, R. Li, Y. Huang, D. He, Y. Wu, T. Xiang, M. Qin, L. Wang, and D. Lv(2026)Solving the Hubbard model with neural quantum states.Nat. Commun.,pp..External Links:DocumentCited by:§I.
- [23]Z.-Y. Han, J. Wang, H. Fan, L. Wang, and P. Zhang(2018)Unsupervised generative modeling using matrix product states.Phys. Rev. X8,pp. 031012.External Links:DocumentCited by:§I.
- [24]M. B. Hastings(2007-08)An area law for one-dimensional quantum systems.J. Stat. Mech.2007(08),pp. P08024.External Links:Document,LinkCited by:§I.
- [25]K. He, X. Zhang, S. Ren, and J. Sun(2016)Deep residual learning for image recognition.Proc. IEEE Conf. Comput. Vis. Pattern Recognit.,pp. 770–778.External Links:DocumentCited by:§III.
- [26]M. Hibat-Allah, M. Ganahl, L. E. Hayward, R. G. Melko, and J. Carrasquilla(2020)Recurrent neural network wave functions.Phys. Rev. Res.2,pp. 023358.External Links:DocumentCited by:§I,§III.
- [27]S. Hochreiter and J. Schmidhuber(1997)Long short-term memory.Neural Comput.9(8),pp. 1735–1780.External Links:DocumentCited by:§III.
- [28]C. Holzhey, F. Larsen, and F. Wilczek(1994)Geometric and renormalized entropy in conformal field theory.Nucl. Phys. B424,pp. 443–467.External Links:DocumentCited by:§I.
- [29]Y. Huang and J. E. Moore(2021)Neural network representation of tensor network and chiral states.Phys. Rev. Lett.127,pp. 170601.External Links:DocumentCited by:§I.
- [30]E. Ibarra-García-Padilla, H. Lange, R. G. Melko, R. T. Scalettar, J. Carrasquilla, A. Bohrdt, and E. Khatami(2025)Autoregressive neural quantum states of Fermi Hubbard models.Phys. Rev. Res.7,pp. 013122.External Links:DocumentCited by:§I.
- [31]V. E. Korepin(2004)Universality of entropy scaling in one dimensional gapless models.Phys. Rev. Lett.92,pp. 096402.External Links:DocumentCited by:§I.
- [32]A. Krizhevsky, I. Sutskever, and G. E. Hinton(2012)ImageNet classification with deep convolutional neural networks.Advances in Neural Information Processing Systems 25,pp. 1097–1105.External Links:DocumentCited by:§III.
- [33]H. Lange, A. Böhler, C. Roth, and A. Bohrdt(2025)Simulating the two-dimensionalt−Jt-{J}model at finite doping with neural quantum states.Phys. Rev. Lett.135,pp. 136504.External Links:DocumentCited by:§I.
- [34]Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner(1998)Gradient-based learning applied to document recognition.Proc. IEEE86(11),pp. 2278–2324.External Links:DocumentCited by:§III.
- [35]L. Levine and R. Movassagh(2017)The gap of the area-weighted Motzkin spin chain is exponentially small.J. Phys. A50,pp. 255302.External Links:DocumentCited by:§V.2,§VI.
- [36]S. Li, F. Pan, P. Zhou, and P. Zhang(2021)Boltzmann machines as two-dimensional tensor networks.Phys. Rev. B104,pp. 075154.External Links:DocumentCited by:§I.
- [37]X. Liang, W.-Y. Liu, P.-Z. Lin, G.-C. Guo, Y.-S. Zhang, and L. He(2018)Solving frustrated quantum many-particle models with convolutional neural networks.Phys. Rev. B98,pp. 104426.External Links:DocumentCited by:§III.
- [38]Z.-C. Liu and B. K. Clark(2024)Unifying view of fermionic neural network quantum states: From neural network backflow to hidden fermion determinant states.Phys. Rev. B110,pp. 115124.External Links:DocumentCited by:§I.
- [39]V. Menon, A. Gu, and R. Movassagh(2024)Symmetries, correlation functions, and entanglement of general quantum Motzkin spin-chains.External Links:2408.16070Cited by:§IV.
- [40]R. Movassagh and P. W. Shor(2016)Supercritical entanglement in local systems: counterexample to the area law for quantum matter.Proc. Natl. Acad. Sci.113,pp. 13278.External Links:DocumentCited by:§I,§II.1,§II.2,§II,§IV.
- [41]K. Mukherjee, H. Barghathi, A. Del Maestro, and R. Mukherjee(2026)Quantum simulation of Motzkin spin chain with Rydberg atoms.External Links:2603.23422Cited by:§I,§V.2,§VI.
- [42]Y. Nomura, A. S. Darmawan, Y. Yamaji, and M. Imada(2017)Restricted Boltzmann machine learning for solving strongly correlated quantum systems.Phys. Rev. B96,pp. 205152.External Links:DocumentCited by:§I.
- [43]Y. Nomura and M. Imada(2021)Dirac-type nodal spin liquid revealed by refined quantum many-body solver using neural-network wave function, correlation ratio, and level spectroscopy.Phys. Rev. X11,pp. 031034.External Links:DocumentCited by:§I.
- [44]J. Robledo Moreno, G. Carleo, A. Georges, and J. Stokes(2022)Fermionic wave functions from neural-network constrained hidden states.Proc. Natl. Acad. Sci.119,pp. e2122059119.External Links:DocumentCited by:§I.
- [45]F. Rosenblatt(1958)The perceptron: A probabilistic model for information storage and organization in the brain.Psychological Review65(6),pp. 386–408.External Links:DocumentCited by:§III.
- [46]D. E. Rumelhart, G. E. Hinton, and R. J. Williams(1986)Learning representations by back-propagating errors.Nature323,pp. 533–536.External Links:DocumentCited by:§III.
- [47]O. Salberger and V. E. Korepin(2017)Entangled spin chain.Rev. Math. Phys.29,pp..External Links:DocumentCited by:§V.2,§VI.
- [48]O. Sharir, Y. Levine, N. Wies, G. Carleo, and A. Shashua(2020)Deep autoregressive models for the efficient variational simulation of many-body quantum systems.Phys. Rev. Lett.124,pp. 020503.External Links:DocumentCited by:§I.
- [49]A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin(2017)Attention is all you need.Advances in Neural Information Processing Systems 30,pp. 5998–6008.External Links:1706.03762Cited by:§III.
- [50](2026)Verification code for exact neural-network representations of the motzkin states.Note:https://github.com/ArtistET/Neuralnetwork_representation_motzkinCited by:Code Availability.
- [51]G. Vidal, J. I. Latorre, E. Rico, and A. Kitaev(2003)Entanglement in quantum critical phenomena.Phys. Rev. Lett.90,pp. 227902.External Links:DocumentCited by:§I.
- [52]Y.-H. Zhang and M. Di Ventra(2023)Transformer quantum state: A multipurpose model for quantum many-body problems.Phys. Rev. B107,pp. 075147.External Links:DocumentCited by:§III.
- [53]Z. Zhang, A. Ahmadain, and I. Klich(2017)Novel quantum phase transition from bounded to extensive entanglement.Proc. Natl. Acad. Sci.114(20),pp. 5142–5146.External Links:DocumentCited by:§V.2,§VI.
- [54]Z. Zhouyin, T.-H. Lee, A. Chen, N. Lanatà, and H. Guo(2026)Neural-quantum-states impurity solver for quantum embedding problems.Phys. Rev. B113,pp. 155123.External Links:DocumentCited by:§I.

## 


- 


Major funding support from
