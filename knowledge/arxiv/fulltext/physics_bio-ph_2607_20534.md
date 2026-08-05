# Quantum error correction and biological error correction: A structural analogy between qubits and neurons

**arXiv ID**: 2607.20534v1
**Authors**: Ian Whitehouse, Anıl Zenginoğlu, Franz Klein, Mohe Edeen Abu Maizer, Wilson Smith, Skylar Chan, Siri Duddella, Wolfgang Losert
**Published**: 2026-07-10
**Categories**: physics.bio-ph, quant-ph
**Comments**: 13 pages, 3 figures, submitted to Physics Review E
**HTML URL**: https://arxiv.org/html/2607.20534v1

## Abstract

We draw a structural analogy between quantum error correction (QEC) and error handling in neural circuits with respect to their redundant encodings and constraint-based inferences. In QEC, logical information is embedded in a protected codespace within a larger Hilbert space. A set of commuting checks (e.g. stabilizer constraints) is repeatedly evaluated to produce an error syndrome that identifies which constraints were violated without directly revealing the logical state. A decoder then maps the syndrome to a recovery operation that returns the system to the codespace and suppresses logical failure below a threshold.   Neural circuits exhibit error-control strategies that can be viewed through a related biological error correction (BEC) pattern: information is distributed across multiple neurons (redundant encoding), yielding reliable collective activity from error-prone unit operations of individual neurons. The structural analogy with QEC raises the question whether collective activity may be constrained on lower-dimensional manifolds (a biological codespace), allowing recurrent circuit dynamics and mismatch signals to function as syndrome-like indicators of constraint violations, driving fast corrective dynamics and slower adaptive updates.   Our structural analogy also suggests that new insights into brain-inspired algorithms for collective information processing may inform novel QEC approaches. We perform numerical experiments using simplified models of qubit and neuron dynamics to illustrate the analogy.

## Full Text

Quantum error correction and biological error correction: A structural analogy between qubits and neurons

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
- License: CC BY 4.0arXiv:2607.20534v1 [physics.bio-ph] 10 Jul 2026

## Quantum error correction and biological error correction:
A structural analogy between qubits and neuronsIan WhitehouseInstitute for Physical Science and Technology, University of Maryland, College Park, MD 20742, USADepartment of Computer Science, University of Maryland, College Park, MD 20742, USAAnıl ZenginoğluInstitute for Physical Science and Technology, University of Maryland, College Park, MD 20742, USAFranz KleinNational Quantum Laboratory, University of Maryland, College Park, MD 20740, USAMohe Edeen Abu MaizerDepartment of Physics, University of Maryland, College Park, MD 20742, USAWilson SmithDepartment of Computer Science, University of Maryland, College Park, MD 20742, USASkylar ChanUniversity of Maryland School of Medicine, Baltimore, MD 21201, USASiri DuddellaDepartment of Physics, University of Maryland, College Park, MD 20742, USAWolfgang Losertwlosert@umd.eduInstitute for Physical Science and Technology, University of Maryland, College Park, MD 20742, USADepartment of Physics, University of Maryland, College Park, MD 20742, USA

## Abstract

We draw a structural analogy between quantum error correction (QEC) and error handling in neural circuits with respect to their redundant encodings and constraint-based inferences. In QEC, logical information is embedded in a protected codespace within a larger Hilbert space. A set of commuting checks (e.g. stabilizer constraints) is repeatedly evaluated to produce an error syndrome that identifies which constraints were violated without directly revealing the logical state. A decoder then maps the syndrome to a recovery operation that returns the system to the codespace and suppresses logical failure below a threshold.

Neural circuits exhibit error-control strategies that can be viewed through a related biological error correction (BEC) pattern: information is distributed across multiple neurons (redundant encoding), yielding reliable collective activity from error-prone unit operations of individual neurons. The structural analogy with QEC raises the question whether collective activity may be constrained on lower-dimensional manifolds (a biological codespace), allowing recurrent circuit dynamics and mismatch signals to function as syndrome-like indicators of constraint violations, driving fast corrective dynamics and slower adaptive updates.

Our structural analogy also suggests that new insights into brain-inspired algorithms for collective information processing may inform novel QEC approaches. We perform numerical experiments using simplified models of qubit and neuron dynamics to illustrate the analogy.

## IIntroduction

How can we perform reliable computation with unreliable parts? This fundamental question has shaped both the theory of computing and our understanding of neural systems for decades. Von Neumann’s classic lectures on "Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components" formulated this question for noisy logical elements and for neural networks, showing that redundancy and majority voting can ensure reliable computation, provided the component error rate lies below a threshold[46]. This insight shapes both classical and quantum error-correcting codes today.

Over the last three decades, quantum information has provided new perspectives into error correction. Shor’s discovery of a QEC code that protects a logical qubit from arbitrary single physical qubit errors[41]and the later development of the stabilizer formalism and topological codes[31,44], established that reliable quantum computation is possible for noisy physical qubits within a specific error threshold. In these constructions, logical information is encoded nonlocally in a subspace of a larger Hilbert space called thecodespace, and ancillary degrees of freedom help extract error syndromes without collapsing the encoded logical state. QEC thus implements von Neumann’s vision in the quantum domain by using structured redundancy and constrained dynamics to protect fragile information. This separation between protected information (the logical degrees of freedom) and measured information (the syndrome) is the core principle of QEC.

In this paper, we argue that an analogous story can be told in a different physical medium, the brain. Individual neurons and synapses are noisy and unreliable devices; yet behavior, perception, and memory are remarkably robust. Population-coding frameworks and attractor-network models suggest that neural networks in the brain achieve reliability by distributing information over many neurons so that noise averages out[10,14]. An explicit example is provided by entorhinal grid cells. Sreenivasan and Fiete showed that multi-periodic firings implement an analog error-correcting code that supports path integration with high resolution despite substantial neural noise[42]. More recently, Zlokapa et al. used biological error-correcting codes to construct fault-tolerant artificial neural networks, demonstrating a transition from faulty to reliable computation analogous to fault-tolerance thresholds in QEC[51]. These examples demonstrate that error-correcting structure is not unique to engineered digital or quantum devices, but also appears in biological neural systems.Figure 1:An illustration of the structural analogy between QEC and BEC. Each system protects information by moving from noisy physical units to redundant logical representations.
In biology, a percept is represented with noisy neurons that are stabilized through population coding to form local neuronal populations.
In quantum, a state is represented with noisy physical qubits that are stabilized as code block to form a logical qubit.

Crucially, we donotassume or invoke quantum coherence or entanglement in biological tissue. While quantum mechanics has been hypothesized to play a role in neural computation and consciousness[1,30], the hypothesis is controversial and empirical studies have called for further research[16,17,48]. Instead, we treat neurons as noisy classical elements. Entanglement appears only in the QEC examples. The analogy is therefore between mathematical structures and the organization of observable activity. We are mappingstructure and behavior, not physics.

Concretely, we define translations between objects in QEC and BEC (see Fig.1). Logical quantum states map to low-dimensional cognitive variables; physical qubits to individual neurons; stabilizer checks to circuit-level constraints that may include glial modulation; and ancilla qubits to auxiliary interneuron, glial, or collective modes that probe and relay error information. We explore models illustrating these translations. One such model is how neuronal damping can implement syndrome-like error signals and correction in classical networks. Then we relate these models to existing data on grid-cell error correction and astrocytic control of oscillations and discuss how this structural correspondence may guide new algorithm and circuit designs. In doing so, we aim to place von Neumann’s original question about reliable computation from unreliable parts within a modern framework that spans both quantum devices and the brain.

This perspective suggests a possible transfer from neuroscience to QEC. Neural circuits maintain robust representations using local feedback that operates continuously and adapts as noise statistics change. QEC relies on local, repeated syndrome extraction, but many decoders are designed for fixed or slowly calibrated noise models. Biological error-control mechanisms may therefore suggest adaptive decoders that update online in response to correlated or nonstationary noise while preserving logical information.

Our contribution is not the claim that neural circuits implement QEC, but a minimal stochastic-dynamical construction showing how constraint damping in a neural population code can share the generator structure and steady-state violation scaling of a simple QEC recovery model. By defining a common structural vocabulary across engineered QEC and organic BEC, we aim to clarify what concepts and patterns are universal. Furthermore, we hope that this analogy will help develop improved methods for robust quantum decoding and fault-tolerant architectures.

## IIPrimers on error correction: Quantum and Biological

## II.1Introduction to Quantum Computing

In quantum computing, a quantum bit, orqubit, is the fundamental unit of quantum information. Similar to a classical bit, a qubit has two computational basis states, written inDirac notationas|0⟩\ket{0}and|1⟩\ket{1}. The vertical bar and angle bracket are read together as aket. Unlike a classical bit, a qubit need not be in only one of these two basis states; it can also be in a normalized complex linear combination, orsuperposition, of both:|ψ⟩=α​|0⟩+β​|1⟩.\ket{\psi}=\alpha\ket{0}+\beta\ket{1}.(1)

where|ψ⟩\ket{\psi}is aquantum state, andα\alphaandβ\betaare the complex amplitudes of|0⟩\ket{0}and|1⟩\ket{1}, respectively. Quantum states follow a strict set of rules which include:
- •

Normalization: A quantum state is normalized when|α|2+|β|2=1|\alpha|^{2}+|\beta|^{2}=1
- •

Complex Amplitude: Amplitudes of a quantum state must belong to the complex space whereα,β∈ℂ\alpha,\beta\in\mathbb{C}
- •

Measurement postulate: When a quantum state is measured, it collapses onto the measurement basis. For simplicity, the measurement basis is selected as|0⟩\ket{0}and|1⟩\ket{1}. A measured qubit has probabilities|α|2|\alpha|^{2}and|β|2|\beta|^{2}of collapsing to|0⟩\ket{0}and|1⟩\ket{1}respectively.

Quantum states can be combined to model a higher dimensional space, represented algebraically with atensor product:|ψ⟩=|ψA⟩⊗|ψB⟩\ket{\psi}=\ket{\psi_{A}}\otimes\ket{\psi_{B}}(2)

States that can be factorized into individual qubit states are calledproduct states. States that cannot be written in this product form areentangled states; for such states, measurement outcomes can exhibit correlations that are not reducible to independent single-qubit states.

One example of an entangled state is presented by theBell state:|Φ+⟩=12​(|00⟩+|11⟩).\ket{\Phi^{+}}=\frac{1}{\sqrt{2}}\left(\ket{00}+\ket{11}\right).(3)

For this state, measurements in the computational basis are perfectly correlated. If the first qubit is measured as|0⟩\ket{0}, the post-measurement state is|00⟩\ket{00}; if it is measured as|1⟩\ket{1}, the post-measurement state is|11⟩\ket{11}.

## II.2Quantum error correction

QEC asks how one can protect an unknown quantum state from noise without directly measuring that state. There are fundamental differences to classical error correction that make QEC subtler and more challenging. A classical bit can be copied, compared to other copies, and majority-voted if one copy is corrupted. An unknown qubit cannot be cloned, and a direct measurement of the qubit generally collapses the superposition. QEC therefore protects information indirectly: it encodes onelogical qubitinto a larger collection of noisyphysical qubitssuch that likely errors can be detected and corrected without revealing the logical state itself[41,31,44].

Consider a basic quantum state|ψ⟩=α​|0⟩+β​|1⟩.\ket{\psi}=\alpha\ket{0}+\beta\ket{1}.(4)

Instead of storing this state in a single physical qubit, we store|ψL⟩=α​|0L⟩+β​|1L⟩,\ket{\psi_{L}}=\alpha\ket{0_{L}}+\beta\ket{1_{L}},(5)

where|0L⟩\ket{0_{L}}and|1L⟩\ket{1_{L}}are logical qubits, orcodewords. The set of allowed encoded states forms thecodespace𝒞(Q)\mathcal{C}^{(Q)}. The central idea is that typical local noise perturbs the physical qubits in a way that can be detected at the level of collective constraints, before it becomes an error on the logical information itself.

A simple example is the three-qubit bit-flip code,|0L⟩=|000⟩,|1L⟩=|111⟩.\ket{0_{L}}=\ket{000},\qquad\ket{1_{L}}=\ket{111}.(6)

Note that this encoding does not copy the unknown state|ψ⟩\ket{\psi}. Instead, it stores the logical information in correlations among physical qubits. The basis codewords|000⟩\ket{000}and|111⟩\ket{111}are product states but a generic encoded superpositionα​|000⟩+β​|111⟩\alpha\ket{000}+\beta\ket{111}is entangled. With this representation, if one physical qubit flips, then the encoded state leaves the set of consistent patterns. One can detect which qubit flipped by measuring the paritiesZ1​Z2Z_{1}Z_{2}andZ2​Z3Z_{2}Z_{3}. These measurements donotask whether the logical state is|0L⟩\ket{0_{L}}or|1L⟩\ket{1_{L}}; instead, they ask whether neighboring qubits agree. Thus they extracterror informationwithout revealing the amplitudesα\alphaandβ\beta. This example illustrates the basic architecture of QEC, although it protects only against bit-flip errors. Full QEC must also protect againstphaseerrors, which have no classical analog. Shor’s original code and the more general stabilizer formalism extend the same logic to arbitrary single-qubit errors[41,31,44].

The stabilizer picture is especially useful for the structural comparison developed later in this paper. In a stabilizer code, one specifies a set of commuting check operatorsSj(Q)S_{j}^{(Q)}whose simultaneous+1+1eigenspace defines the codespace:𝒞(Q)={|ψ⟩:Sj(Q)​|ψ⟩=|ψ⟩​for all​j}.\mathcal{C}^{(Q)}=\left\{\ket{\psi}:S_{j}^{(Q)}\ket{\psi}=\ket{\psi}\text{ for all }j\right\}.(7)

EachSj(Q)S_{j}^{(Q)}is aconstrainton the joint state of several physical qubits. If an error occurs, one or more of these constraints may be violated. Measuring the checks produces a set of binary outcomes𝒔(Q)=(s1(Q),…,sm(Q)),sj(Q)∈{±1},\bm{s}^{(Q)}=(s_{1}^{(Q)},\dots,s_{m}^{(Q)}),\qquad s_{j}^{(Q)}\in\{\pm 1\},(8)

called theerror syndrome. A valuesj(Q)=−1s_{j}^{(Q)}=-1indicates that the corresponding constraint has been violated.

In practice, these checks are not measured directly on the data qubits. Instead, the data qubitsqi(Q)q_{i}^{(Q)}are coupled to auxiliaryancilla qubitsak(Q)a_{k}^{(Q)}prepared in known states. The ancillas interact with the data through a syndrome-extraction circuit and are then measured. In this way, the ancillas act as temporary carriers of syndrome information. The protected logical state remains encoded nonlocally in the data qubits, while the ancillas report which checks were satisfied or violated. This separation betweenprotected informationandmeasured informationis one of the defining ideas of QEC.

A second important point, which is often counterintuitive at first, is that QEC can correct continuous noise using discrete syndrome data. A generic perturbation of a qubit can change amplitudes and phases continuously. However, once one measures the stabilizer checks, the relevant information is represented in a discrete syndrome. In the standard qubit language, arbitrary local errors can be decomposed into bit flips (XX), phase flips (ZZ), and combinations. QEC does not need to reconstruct the full error; it needs just enough information to decide which recovery operation is most likely to restore the logical state.

Thedecoderis the map that makes this decision. Given a syndrome pattern, or more realistically a time history of syndrome patterns from repeated measurements,
the decoder𝒟(Q)\mathcal{D}^{(Q)}outputs arecovery operationℛ(Q)\mathcal{R}^{(Q)}:𝒟(Q):𝒔(Q)↦ℛ(Q).\mathcal{D}^{(Q)}:\bm{s}^{(Q)}\mapsto\mathcal{R}^{(Q)}.(9)

Importantly, the decoder is usually a classical algorithm, even though the information being protected is quantum. A logical error occurs when the physical noise and recovery together enact a nontrivial transformation on the encoded information.

For the structural comparison below, the important point is not any particular code construction, but the organization of the correction process: noisy physical degrees of freedom support protected logical variables, constraints define a codespace, syndrome extraction reports constraint violations without measuring the logical state, and a decoder selects a recovery. In fault-tolerant architectures this cycle is repeated using imperfect hardware, and below a threshold physical error rate, increasing the code size can reduce the logical error rate[31,44]. This combination of redundant encoding, repeated constraint checking, syndrome-based inference, and recovery is the organizational pattern that we compare to error control in neural systems.

## II.3Neurons and Computation

Neurons are the central computational units within the brain. They receive electrical signals through dendrites, which form synapses with the axons of other neurons. When a neuron’s action potential spikes and exceeds the activation potential, it sends electrical signals through its axons, potentially triggering connected neurons to propagate the signal.

Compared to digital computing, neurons compute fundamentally differently. They are fully asynchronous, with each neuron separately reacting to incoming electrical signals. Neurons operate in both the analog and discrete domains, performing calculations with varying voltages but sending information as discrete spiking events.

## II.3.1Neural population coding and biological error correction

Neurons encode information, including sensory stimuli, through a phenomenon known as population coding[21]. A significant amount of prior work has focused on how stimuli are encoded through population coding, which is essential for understanding how neurons represent complex, high-dimensional signals through spiking dynamics[26,37,50]. However, population coding is also essential for error correction.

Tkačik et al. provide an overview of population coding-based error correction through redundant information, finding that, as noise and stimulus changed, the optimal coding and amount of redundant information did as well[45]. Boerlin et al. and Bourdoukan et al. argue that the coding communicates the error level to the system, which allows for the system to self-correct by integrating the signals from other neurons above an error threshold[8,9]. Both Berry and Tkačik propose that neural activity patterns can be clustered to represent population codewords[7]. These clusters are error correcting despite the noise associated with individual neurons.

In addition to proposing the idea of population codeword clusters, Berry and Tkačik discuss how the dynamics of the neuronal system affect population coding and error rates, finding that the system resides in a subcritical, glassy state[7]. Calvo et al. support this, also finding that the brain operates in a subcritical system while remaining close to criticality[13]. They argue that this allows for a robust system with a long lifetime. This echoes findings on reservoir computing, where being close to criticality is seen as essential for high performance[40]. Calaim et al. discuss the distance to criticality, using a spiking model to draw a ‘bounding box’ regime where the network is robust[12].

Other work has examined robustness that stems from the connectivity and circuitry of the neuronal network. Arle et al. use a spiking neuron model to simulate the brain, and find that more complex, connected systems, such as the brain, are inherently more stable and robust[4]. Lim and Goldman analyze the microcircuitry of the brain, finding that it generates a negative corrective signal that compensates for errors caused by noisy-firing neurons, allowing them to develop a model of short-term memory that is similarly robust to the brain[27].

## II.3.2Individual neuron complexity and population coding

Neurons are significantly more complex than qubits, a feature that makes them less analogous than this comparison might suggest. Beniaguev et al. show that modeling a single neuron, with its N-methyl-D-aspartate (NMDA) receptors, requires a 5 hidden layer artificial neural network, while a neuron without its NMDA receptors require only 1 hidden layer[6]. Similarly, Aizenbud et al. show that a single neuron is capable of solving complex problems, like XOR, through its dendritic networks[3]. Findings like these have inspired the field of dendritic computing.

In contrast, qubits are closer to classical bits, where they are basic units of data and are not capable of compute by themselves. Therefore, the capability gap between neurons and qubits calls into question the accuracy of this metaphor. Despite their complexity, neurons can be, and are, usefully approximated as simple binary variables in reduced models. For example, the leaky-integrate-and-fire model, employed in Sec.IV.3, captures important features of neuronal firing[43]. Despite this complexity, neurons still rely on population coding to develop complex representations and suppress errors[26,37,50,45].

## IIIStructural dictionary between quantum error correction and neural population codes

In this section we introduce a structural dictionary to translate between QEC and neural population codes, with the goal of preparing a quantitative, mathematical treatment in Sec.IV.
Our aim is to identify which quantum objects map to which biological objects, and specify what aspects of their structure can be exploited.

We use a superscript(Q)(Q)for quantities associated with a quantum code and a superscript(B)(B)for the corresponding biological implementation. For example,𝒞(Q)\mathcal{C}^{(Q)}denotes a QEC code space andℳ(B)\mathcal{M}^{(B)}a neural manifold. The mapping we propose isstructural: we treat neurons as classical stochastic dynamical elements, and we do not assume quantum coherence or entanglement in the brain. The analogy is between roles rather than physical phenomena, with shared roles including redundant encoding, constraint checks, syndrome-like signals, and decoding.

We organize the dictionary into four groups of objects:
- 1.

core structural elements, presented in Sec.III.1,
- 2.

checks, syndromes, and ancillary degrees of freedom, presented in Sec.III.2,
- 3.

decoding and correction dynamics, presented in Sec.III.3, and
- 4.

design, evolution, and thresholds, presented in Sec.III.4.

## III.1Core structural objects

The first group of objects concerns what information is represented, where that information is encoded, how noise acts on the underlying physical degrees of freedom, and how robustness is quantified.

On the QEC side, we take as a reference point a stabilizer code embedded in a larger fault-tolerant architecture[31,44]. The basic ingredients are:
- •

Physical qubitsqi(Q)q_{i}^{(Q)}that are subject to noise.
- •

Logical qubitsQα(Q)Q_{\alpha}^{(Q)}(or logical states) encoded in an error-correcting code.
- •

Acode space𝒞(Q)⊂ℋ⊗n\mathcal{C}^{(Q)}\subset\mathcal{H}^{\otimes n}, defined as the simultaneous+1+1eigenspace of a commuting group of stabilizer operators.
- •

Anoise channel𝒩(Q)\mathcal{N}^{(Q)}acting on the physical degrees of freedom.
- •

Acode distanced(Q)d^{(Q)}that characterizes how many local errors are required to cause a logical error.

On the biological side, we consider a recurrently connected neural population, as in the experimental and theoretical work reviewed in[10,14,38,24,34,25,28]. Here the natural counterparts are:
- •

Physical unitsxi(B)x_{i}^{(B)}, which may be individual neurons, synapses, or small microcircuits, each with noisy, variable response properties.
- •

Low-dimensional variablesXα(B)X_{\alpha}^{(B)}representing quantities encoded by the population code including spatial position, working-memory state, and muscle-control signals.
- •

Aneural manifoldorattractor setℳ(B)⊂ℝN\mathcal{M}^{(B)}\subset\mathbb{R}^{N}(or a suitable state space) consisting of patterns of activity across neurons that implement particular values of the low-dimensional variables. This is downstream from the connectome, which is the physical wiring of the neurons in the brain.
- •

An effectivenoise process𝒩(B)\mathcal{N}^{(B)}with fast neural variability (spiking noise, synaptic failures). This does not include slow, structural changes like neuroplasticity, which plays a role in learning but does not cause the type of errors we are interested in.
- •

A notion ofrobustness scaled(B)d^{(B)}quantifying the size of perturbations in the physical units (e.g. fraction of neurons or synapses perturbed) that can be tolerated before the encoded variableXα(B)X_{\alpha}^{(B)}changes appreciably. Computational experiments studying how perturbations can push the brain to criticality quantify this notion[12,4,13].

Thus the first layer of the dictionary is:{qi,Qα,𝒞,𝒩,d}(Q)⟷{xi,Xα,ℳ,𝒩,d}(B).\bigl\{q_{i},Q_{\alpha},\mathcal{C},\mathcal{N},d\bigr\}^{(Q)}\ \longleftrightarrow\ \bigl\{x_{i},X_{\alpha},\mathcal{M},\mathcal{N},d\bigr\}^{(B)}.(10)

In Sec.IVwe will use this correspondence to define explicit measures of representational robustness and to compareV∞(Q)V_{\infty}^{(Q)}andV∞(B)V_{\infty}^{(B)}on equal footing for concrete models.

## III.2Checks, syndromes, and ancillary degrees of freedom

The second group of objects concerns how errors aredetected. In stabilizer QEC, this is achieved by measuring a set of commuting operatorsSj(Q)S_{j}^{(Q)}(stabilizer generators) on the physical qubits. The outcome of each measurement is a binarysyndrome bitsj(Q)∈{±1}s_{j}^{(Q)}\in\{\pm 1\}indicating whether the corresponding stabilizer constraint is satisfied. In many schemes, these measurements are implemented by coupling the data qubitsqi(Q)q_{i}^{(Q)}to ancillary qubitsak(Q)a_{k}^{(Q)}, which are prepared in a known state, entangled with the data via a syndrome-extraction circuit, and then measured in the computational basis[31,44]. The ancillas thus serve as dedicated carriers of syndrome information.

In neural systems, there is no exact analog of a projective stabilizer measurement, but several layers of circuitry implementconstraintsandmismatch signalsthat play related roles. Recurrent inhibitory and excitatory loops enforce consistency conditions on population activity[10,14,42]. Astrocytes may add an additional, slower layer of monitoring and modulation[38,24,34,25,28], however that is not the focus of this analogy (see Sec.V.1for a discussion of future work along these lines).

We identify the following structural correspondence:
- •

Stabilizer checksSj(Q)S_{j}^{(Q)}may map tocircuit-level constraintsCj(B)C_{j}^{(B)}on joint activity patterns, such as consistency of firing with a learned manifoldℳ(B)\mathcal{M}^{(B)}, maintenance of excitation–inhibition balance, or preservation of particular phase relationships in ongoing oscillations, with possible astrocyte-mediated contributions.
- •

Syndrome bitssj(Q)s_{j}^{(Q)}map tomismatch signalsmj(B)m_{j}^{(B)}, which can be realized by deviations of neural activity fromℳ(B)\mathcal{M}^{(B)}, by prediction errors in circuits that implement internal models signaling that the current pattern of activity is out of learned constraints.
- •

Ancilla qubitsak(Q)a_{k}^{(Q)}map toancillary degrees of freedomak(B)a_{k}^{(B)}that monitor and relay information about the state of the network without directly encoding the low-dimensional variablesXα(B)X_{\alpha}^{(B)}. These could include interneurons, collective oscillatory modes, and possibly astrocytes that are more sensitive to constraint violations than to the exact value of the encoded variable.

In this view, interneurons, collective oscillatory modes, and possibly astrocytes are not quantum ancillas, but they can play an ancillaryrole: they may carry syndrome-like information about whether local neural activity and environmental conditions are compatible with the current code manifoldℳ(B)\mathcal{M}^{(B)}.

## III.3Decoding and correction dynamics

The third group of objects concerns how detected errors arecorrected. On the quantum side, adecoderis an algorithm (or, more generally, a map) that takes a syndrome pattern(sj(Q))(s_{j}^{(Q)})as input and outputs a recovery operationℛ(Q)\mathcal{R}^{(Q)}acting on the data qubits. In stabilizer codes,ℛ(Q)\mathcal{R}^{(Q)}is typically chosen from the Pauli group, and the decoder is designed to minimize the probability of a logical error given a noise model[44]. In fault-tolerant architectures, such decoders are applied repeatedly in time to keep the logical state within the code space𝒞(Q)\mathcal{C}^{(Q)}.

In neural population codes, much of the “decoding” and “correction” is implemented by the intrinsic dynamics of the network. Prominent examples are attractor models of memory: starting from a noisy pattern of activity, interactions drive the system toward a family of stable states (an attractor manifold), thus correcting microscopic noise and preserving the encoded variable[10,14,42].

We identify the following structural correspondence:
- •

Adecoder map𝒟(Q):(sj(Q))↦ℛ(Q)\mathcal{D}^{(Q)}:(s_{j}^{(Q)})\mapsto\mathcal{R}^{(Q)}on the QEC side with an effectiveerror-control map𝒟(B):(mj(B))↦Δ​θ(B)\mathcal{D}^{(B)}:(m_{j}^{(B)})\mapsto\Delta\theta^{(B)}on the biological side, whereΔ​θ(B)\Delta\theta^{(B)}denotes changes in neuronal and astrocytic parameters (e.g. synaptic weights, intrinsic excitability).
- •

Therecovery operationℛ(Q)\mathcal{R}^{(Q)}corresponds with a combination of fastrelaxation dynamicstoward an attractor manifoldℳ(B)\mathcal{M}^{(B)}(correcting noise).

Glia-inspired rhythmic-sharing algorithms provide an artificial example of continuous syndrome-like monitoring: oscillatory modulation of network couplings introduces ancillary degrees of freedom, and deviations of synchrony or phase-locking structure from a learned baseline act as mismatch signals. The phase dynamics can then reconfigure effective information pathways when input statistics change[49]. This is a classical, continuous analog of constraint monitoring coupled to adaptive recovery. In Sec.IVwe will formalize𝒟(B)\mathcal{D}^{(B)}andℛ(B)\mathcal{R}^{(B)}in tractable models and quantify their error-correcting properties.

## III.4Design, evolution, and thresholds

Finally, we consider how codes and circuits aredesigned, and what notions ofthresholdapply. In the QEC setting, codes are engineered to optimize distance and locality, subject to hardware and architectural constraints[44]. Threshold theorems then guarantee that if the physical error rate is below a critical valuepth(Q)p_{\mathrm{th}}^{(Q)}, and if sufficient resources are allocated, accurate logical computation is possible.

Biological systems, by contrast, are shaped by evolution, development, and learning, and not engineered with an explicit code in mind. However, as we argue in this work, numerous works show they have code-like structure: redundantly encoded variables, clustered population activity, and error-correcting dynamics that can be analyzed in the language of codes and decoders. Like QEC settings, neural circuits are constrained by their “hardware" and optimized for distance and locality[5]. Recent work has shown that biologically inspired error-correcting codes can be used to construct fault-tolerant artificial neural networks, with a transition between reliable and unreliable computation as the rate of neuron failure is varied, similar to QEC thresholds[51].Table 1:A structural dictionary between the core objects of quantum error correction (QEC) and neural population codes. Superscripts(Q)(Q)and(B)(B)denote quantum and biological quantities, respectively.QEC elementBiological counterpartInformal rolePhysical qubitsqi(Q)q_{i}^{(Q)}Physical unitsxi(B)x_{i}^{(B)}(neurons, synapses, microcircuits)Noisy elements that directly experience the noise process.Logical qubitsQα(Q)Q_{\alpha}^{(Q)}Low-dimensional variablesXα(B)X_{\alpha}^{(B)}(cognitive variables)Information to be protected and made behaviorally robust.Code space𝒞(Q)\mathcal{C}^{(Q)}Neural manifold / attractor setℳ(B)\mathcal{M}^{(B)}Set of valid global states implementing particular values ofXα(B)X_{\alpha}^{(B)}.Noise channel𝒩(Q)\mathcal{N}^{(Q)}Neural noise and drift process𝒩(B)\mathcal{N}^{(B)}Perturbations due to spiking variability, synaptic failures,
neuromodulation, and slow nonstationarities.Code distanced(Q)d^{(Q)}Robustness scaled(B)d^{(B)}Tolerable size of perturbation in physical units before the encoded
variable changes appreciably.

## IVQuantitative framework for biological and quantum error correction

We now construct a quantitative model for the structural dictionary of Table1. Our goal is to describe both QEC and biological error correction asredundant encoding plus constraint-based inference. On the quantum side, noisy physical qubitsqi(Q)q_{i}^{(Q)}support protected logical variablesQα(Q)Q_{\alpha}^{(Q)}inside a code spaceC(Q)C^{(Q)}. On the biological side, noisy physical unitsxi(B)x_{i}^{(B)}(neurons, synapses, or small microcircuits) support protected low-dimensional variablesXα(B)X_{\alpha}^{(B)}inside a neural manifold or attractor setM(B)M^{(B)}. The analogy is structural, organized around distributed redundancy, constraint checks, syndrome-like variables, and recovery dynamics.

These ideas appear in many other areas of physics. We name a few familiar examples. In thermodynamics, a given macrostate corresponds to many microstates, and is therefore protected against “noise” that changes microstates of individual particles (atoms). In general relativity, the Einstein equations can be formulated as a system of hyperbolic evolution equations that preserve constraints. Constraint damping or projection methods bring the evolutionary dynamics back to the constraint manifold.

## IV.1Quantum

For a stabilizer code, the protected quantum states lie in a code manifold that we write asC(Q)={|ψ⟩∈ℋ⊗n:Sj(Q)|ψ⟩=|ψ⟩,j=1,…,m},C^{(Q)}=\left\{|\psi\rangle\in\mathcal{H}^{\otimes n}:S_{j}^{(Q)}|\psi\rangle=|\psi\rangle,\;\;j=1,\dots,m\right\},(11)

where the commuting operatorsSj(Q)S_{j}^{(Q)}are the stabilizer checks.
Under a noisy channelN(Q)N^{(Q)}, syndrome extraction leads to a binary
syndrome vectors(Q)​(t)=(s1(Q)​(t),…,sm(Q)​(t)),sj(Q)​(t)∈{±1},s^{(Q)}(t)=\left(s_{1}^{(Q)}(t),\dots,s_{m}^{(Q)}(t)\right),\qquad s_{j}^{(Q)}(t)\in\{\pm 1\},(12)

and a decoderD(Q)D^{(Q)}maps the syndrome history to a recovery
operationRt(Q)R_{t}^{(Q)},Rt(Q)=D(Q)(s(Q)(0:t)).R_{t}^{(Q)}=D^{(Q)}\!\left(s^{(Q)}(0{:}t)\right).(13)

A full correction cycle can therefore be written schematically asρt+1=Rt(Q)∘Nt(Q)​(ρt).\rho_{t+1}=R_{t}^{(Q)}\circ N_{t}^{(Q)}(\rho_{t}).(14)

The logical error rate decreases with code distanced(Q)d^{(Q)}whenever the physical noise is below threshold:pL(Q)​(d(Q),p)≈AQ​(ppth(Q))(d(Q)+1)/2,p<pth(Q).p_{L}^{(Q)}(d^{(Q)},p)\approx A_{Q}\left(\frac{p}{p_{\mathrm{th}}^{(Q)}}\right)^{(d^{(Q)}+1)/2},\qquad p<p_{\mathrm{th}}^{(Q)}.(15)

## IV.2Numerical implementation of a QEC experiment

To make the structural dictionary quantitative, we perform a numerical experiment where both the quantum and biological systems are treated as noisy dynamics on a larger state space together with a correction mechanism that steers trajectories to a protected manifold. On the quantum side this protected set is the codespaceC(Q)C^{(Q)}; on the biological side it is the neural code manifoldM(B)M^{(B)}. The same class of observables is then compared across the two systems: an encoded-information observable and a manifold-violation observable.

As a minimal QEC model we use the three-qubit repetition code (6), which protects against bit-flip errors[41,19,44]. The logical codewords are|0L⟩=|000⟩,|1L⟩=|111⟩,|0_{L}\rangle=|000\rangle,\qquad|1_{L}\rangle=|111\rangle,(16)

and the stabilizer checks areS1(Q)=Z1​Z2,S2(Q)=Z2​Z3.S_{1}^{(Q)}=Z_{1}Z_{2},\qquad S_{2}^{(Q)}=Z_{2}Z_{3}.(17)

For a generic encoded state|ψL⟩=α​|0L⟩+β​|1L⟩,|α|2+|β|2=1,|\psi_{L}\rangle=\alpha|0_{L}\rangle+\beta|1_{L}\rangle,\qquad|\alpha|^{2}+|\beta|^{2}=1,(18)

we evolve the density operatorρ\rhounder independent bit-flip noise and compare discrete and continuous recovery. In the numerical implementation we choose a generic superposition with non-vanishing amplitudes to demonstrate decay of multi-qubit errors.

The discrete-time bit-flip channel is𝒩p(Q)​(ρ)=∑e∈{0,1}3p|e|​(1−p)3−|e|​X​(e)​ρ​X​(e)†,\mathcal{N}_{p}^{(Q)}(\rho)=\sum_{e\in\{0,1\}^{3}}p^{|e|}(1-p)^{3-|e|}X(e)\,\rho\,X(e)^{\dagger},(19)

whereX​(e)=X1e1​X2e2​X3e3,|e|=e1+e2+e3.X(e)=X_{1}^{e_{1}}X_{2}^{e_{2}}X_{3}^{e_{3}},\qquad|e|=e_{1}+e_{2}+e_{3}.(20)

Syndrome sectors are resolved by the projectorsPs1,s2=14​(I⊗3+s1​S1(Q))​(I⊗3+s2​S2(Q)),P_{s_{1},s_{2}}=\frac{1}{4}\left(I^{\otimes 3}+s_{1}S_{1}^{(Q)}\right)\left(I^{\otimes 3}+s_{2}S_{2}^{(Q)}\right),(21)

withs1,s2∈{±1}s_{1},s_{2}\in\{\pm 1\}, and correction operatorsR++=I,R−+=X1,R−−=X2,R+−=X3.R_{++}=I,\quad R_{-+}=X_{1},\quad R_{--}=X_{2},\quad R_{+-}=X_{3}.(22)

The corresponding syndrome-sector recovery map isℛ(Q)​(ρ)=∑s1,s2Rs1,s2​Ps1,s2​ρ​Ps1,s2​Rs1,s2†.\mathcal{R}^{(Q)}(\rho)=\sum_{s_{1},s_{2}}R_{s_{1},s_{2}}\,P_{s_{1},s_{2}}\,\rho\,P_{s_{1},s_{2}}\,R_{s_{1},s_{2}}^{\dagger}.(23)

A discrete correction cycle is thenρn+1=ℛ(Q)∘𝒩p(Q)​(ρn).\rho_{n+1}=\mathcal{R}^{(Q)}\!\circ\mathcal{N}_{p}^{(Q)}(\rho_{n}).(24)

To compare projections and damping, we evolve the system in continuous time according tod​ρd​t=γ​∑i=13(Xi​ρ​Xi−ρ)+κ​(ℛ(Q)​(ρ)−ρ),\frac{d\rho}{dt}=\gamma\sum_{i=1}^{3}\left(X_{i}\rho X_{i}-\rho\right)+\kappa\left(\mathcal{R}^{(Q)}(\rho)-\rho\right),(25)

whereγ\gammais the physical bit-flip rate andκ\kappais the recovery rate. The first term continuously injects syndrome violations, while the second term continuously steers the state back to the codespace. Numerically, the discrete model is iterated by direct application of the channel and recovery map, while the continuous generator is integrated with a fourth-order Runge–Kutta scheme[2,39,23,20].Figure 2:Numerical simulation of the three-qubit repetition code comparing discrete and continuous recovery. Left: logical fidelityFL(Q)​(t)F_{L}^{(Q)}(t)given in (26).
Right: stabilizer violationV(Q)​(t)V^{(Q)}(t)given in (28). The blue solid curve shows discrete-time bit-flip noise without recovery; the orange solid curve shows discrete syndrome recovery after each cycle; the green dashed curve shows continuous-time bit-flip noise without recovery; and the red dashed curve shows continuous-time recovery at finite rateκ\kappa. Exact syndrome recovery returns the state to the codespace after each cycle, soV(Q)=0V^{(Q)}=0identically, while the logical fidelity still decays due to uncorrectable multi-qubit errors. Continuous-time recovery suppresses stabilizer violation but leaves a nonzero steady-state residual under persistent noise, demonstrating the difference between projection recovery and damping recovery.

The quantum observables recorded in the simulation areFL(Q)​(t)\displaystyle F_{L}^{(Q)}(t)=⟨ψL|ρ​(t)|ψL⟩,\displaystyle=\langle\psi_{L}|\rho(t)|\psi_{L}\rangle,(26)PC(Q)​(t)\displaystyle P_{C}^{(Q)}(t)=Tr​(P++​ρ​(t)),\displaystyle=\mathrm{Tr}\!\left(P_{++}\rho(t)\right),(27)V(Q)​(t)\displaystyle V^{(Q)}(t)=∑j=121−Tr​(Sj(Q)​ρ​(t))2,\displaystyle=\sum_{j=1}^{2}\frac{1-\mathrm{Tr}\!\left(S_{j}^{(Q)}\rho(t)\right)}{2},(28)

whereFL(Q)F_{L}^{(Q)}is the logical fidelity,PC(Q)P_{C}^{(Q)}the codespace population, andV(Q)V^{(Q)}a stabilizer violation. For the continuous model, starting from the codespace, we findV∞(Q)=4​γκ+4​γ,V_{\infty}^{(Q)}=\frac{4\gamma}{\kappa+4\gamma},(29)

showing that continuous recovery suppresses, but does not eliminate, off-manifold error under persistent noise. By contrast, the ideal discrete recovery map of Eq. (23) returns the state exactly to the codespace after each correction cycle, although logical fidelity can still decay due to uncorrectable multi-qubit errors.

For the data shown in Fig.2, we choose a generic logical superposition with nonvanishing amplitudes and evolve it for6060effective correction cycles. In the discrete model, each physical qubit undergoes an independent bit flip with probabilityp=0.02p=0.02per cycle. In the continuous model, we useγ=1\gamma=1,κ=12\kappa=12, andΔ​t=0.02\Delta t=0.02, and plot the continuous trajectories against the effective cycle indext/Δ​tt/\Delta tfor direct comparison with the discrete-time evolution.

The left panel in Fig.2displays the logical fidelity (26), while the right panel displays the stabilizer violation (28). The discrete and continuous noise curves lie nearly on top of each other, showing that the continuous-time generator reproduces the same qualitative degradation of the encoded state as repeated discrete bit-flip noise. Under exact discrete syndrome recovery,V(Q)​(t)=0V^{(Q)}(t)=0throughout, because each correction cycle returns the state to the codespace exactly. Nevertheless, the logical fidelity still decays slowly, demonstrating uncorrectable multi-qubit bit flips that act nontrivially within the logical subspace. By contrast, continuous recovery at finite rateκ\kappasubstantially suppresses the growth of stabilizer violation and improves the logical fidelity relative to noise-only evolution, but it does not restore the state exactly to the codespace under persistent noise. Instead, the stabilizer-violation observable approaches the nonzero asymptotic value given in Eq. (29). This explicitly distinguishes recovery due to projection from recovery due to damping: projection enforces exact return to the code manifold after each cycle, whereas damping results in a stationary balance between noise injection and restorative flow.

## IV.3BEC equivalent of the QEC numerical experimentFigure 3:The biological counterpart to Fig.2: a numerical simulation of a three-neuron population code. Left: codespace populationPC(B)​(t)P_{C}^{(B)}(t).
Right: constraint violation Eq. (37). The blue curve shows noise without recovery; the orange curve shows recovery without noise; and the green curve shows both together. Without recovery,V(B)V^{(B)}grows towards its maximum as noise drives units from the two codewords. Recovery alone holds the system exactly on the codespace. With both, continuous recovery suppresses constraint violation but leaves a nonzero steady-state residual. Unlike Fig.2, the biological model is integrated in continuous time only.

A structurally similar reduced model can be constructed for a biological setting. We start from a bistable stochastic neuron model motivated by the Ornstein–Uhlenbeck description of the subthreshold membrane potential of a LIF neuron, provided by Burkitt[11],τ​d​vd​t=−[v−V0]+μ+σ​2​τ​ξi​(t)\tau\frac{dv}{dt}=-\left[v-V_{0}\right]+\mu+\sigma\sqrt{2\tau}\xi_{i}(t)(30)

whereξi​(t)\xi_{i}(t)is zero-mean, unit-variance white noise. We couple three such reduced units and let the mean drive become dependent through the population transfer functionϕ\phi, which is a monotone, saturating gain function of the membrane state, sharing the sigmoidal shape of the Siegert transfer function[11]but treated as a static nonlinearity rather than as a rate evaluated on input statistics,τ​d​vid​t\displaystyle\tau\frac{dv_{i}}{dt}=−[vi−V0]+μ+σ​2​τ​ξi​(t)\displaystyle=-\left[v_{i}-V_{0}\right]+\mu+\sigma\sqrt{2\tau}\xi_{i}(t)(31)+wself​ϕ​(vi)+wcouple​∑j≠iϕ​(vj),\displaystyle+w_{\text{self}}\phi(v_{i})+w_{\text{couple}}\sum_{j\neq i}\phi(v_{j}),i\displaystyle i=1,2,3\displaystyle=1,2,3

Under the assumptions below, three features of Eq. (31) permit a reduction to discrete dynamics. First, when the self-coupling exceeds a critical value,wself>wcw_{\text{self}}>w_{c}, the deterministic single-neuron drift of an isolated unit,f​(vi)=−[vi−V0]+μ+wself​ϕ​(vi)f(v_{i})=-\left[v_{i}-V_{0}\right]+\mu+w_{\text{self}}\phi(v_{i})(32)

has three roots: two stable fixed pointsv−∗v_{-}^{\ast},v+∗v_{+}^{\ast}, separated by a barriervb∗v_{b}^{\ast}. The membrane potential of each neuron, therefore, resides, over long timescales, in one of two basins, and we label this choice by a binary variablebi∈{0,1}b_{i}\in\{0,1\}. The effective potentialU​(v)=−∫vf​(v′)​𝑑v′U(v)=-\!\int^{v}f(v^{\prime})\,\,dv^{\prime}implied by Eq. (32) is the double well that governs transitions.

Second, noise drives transitions across the barriervb∗v_{b}^{\ast}at the Kramers rate,γ\displaystyle\gamma=12​π​τ​|U′′​(v−∗)​U′′​(vb∗)|​exp⁡(−Δ​UD)\displaystyle=\frac{1}{2\pi\tau}\sqrt{\left|U^{\prime\prime}\left(v_{-}^{\ast}\right)\;U^{\prime\prime}\left(v_{b}^{\ast}\right)\right|}\;\exp\!\left(-\frac{\Delta U}{D}\right)(33)D\displaystyle D=σ2\displaystyle=\sigma^{2}

withΔ​U=U​(vb∗)−U​(v−∗)\Delta U=U\left(v_{b}^{\ast}\right)-U\left(v_{-}^{\ast}\right).γ\gammais the symbolic rate defined by Eq. (33), and it is dependent on the biophysical parameters in the Ornstein–Uhlenbeck function. These parameters are not required for the structural result, Eq. (35).

Finally, the reduction to a discrete configuration is valid in the metastable regime, where relaxation within a basin is fast compared to inter-basin transitions,τrelax≪γ−1,κ−1\tau_{\text{relax}}\ll\gamma^{-1},\,\kappa^{-1}. Then, the continuous states of the neurons collapse into discrete configurations(b1,b2,b3)∈{0,1}3(b_{1},b_{2},b_{3})\in\{0,1\}^{3}, and the dynamics are a Markov jump process between these eight states.

Because the noise termsξi​(t)\xi_{i}(t)in Eq. (31) are independent, noise-driven, single-unit flips occur independently. The noise-driven part of the generator, therefore, factorizes into a sum of independent single-unit flip operators,γ​∑i(πi−𝕀)\gamma\sum_{i}(\pi_{i}-\mathbb{I}).

Flips are corrected by inter-unit coupling. When neuroniiis in the minority and the majority units are static, the termwcouple​∑j≠iϕ​(vj)w_{\text{couple}}\sum_{j\neq i}\phi(v_{j})in Eq. (31) adds a constant tilt to its potential,Uc=U​(v)−(wcouple​∑j≠iϕ​(vj∗))​vU_{c}=U(v)-\left(w_{\text{couple}}\sum_{j\neq i}\phi(v^{\ast}_{j})\right)v(34)

lowering the barrier towards the majority basin and raising it towards the minority one. We treat the majority neurons as static when evaluating the minority neuron’s escape. The resulting biased escape rate back to consensus definesκ\kappa, the Kramers rate of the tilted potential in Eq. (34), in parallel withγ\gammain Eq. (33). In this reduced model,wcouplew_{\text{couple}}performs the role played by the recovery channel in Eq. (25): it is a directed relaxation towards the code subspace. Collecting the independent flip generator and the majority-pull generator givesd​pd​t=γ​∑i=13(πi−𝕀)​p+κ​(Rc,b(B)−𝕀)​p\frac{dp}{dt}=\gamma\sum_{i=1}^{3}\left(\pi_{i}-\mathbb{I}\right)p+\kappa\left(R_{c,b}^{(B)}-\mathbb{I}\right)p(35)

whereRc,b(B)R^{(B)}_{c,b}is a majority-vote recovery generator. Eq. (35) is the classical counterpart of Eq.25:πi\pi_{i}replacesXi​ρ​XiX_{i}\rho X_{i}, andR(B)R^{(B)}replaces the recovery channel(ℛ(Q)​(ρ)−ρ)\left(\mathcal{R}^{(Q)}(\rho)-\rho\right), withγ\gammaandκ\kappanow classical rates rather than the physical bit-flip and recovery rates. The plots in Fig.3show how these equations’ results parallel their quantum counterparts in Fig.2. To generate these plots, we define the codespace population, or the classical probability mass that sits on a valid codeword:PC(B)​(t)=Pr​[b​(t)=000]+Pr​[b​(t)=111]P_{C}^{(B)}(t)=\text{Pr}[b(t)=000]+\text{Pr}[b(t)=111](36)

and the probability that constraints are violated:V(B)=Pr​(b1≠b2)+Pr​(b2≠b3)V^{(B)}=\text{Pr}(b_{1}\neq b_{2})+\text{Pr}(b_{2}\neq b_{3})(37)

Eq. (36) is different from Eq. (26) due to the classical nature of neurons, which have no quantum amplitude or coherence. Eq. (37) can be evaluated at the stationary distribution to getV∞(B)V_{\infty}^{(B)}, similar to Eq. (29). The stationary distribution assigns equal weightaato the two codewords and equal weightbbto each of the six non-codeword configurations. The stationarity condition for the consensus state000000balances its noise-driven outflow3​γ​a3\gamma aagainst the combined noise and recovery inflow3​(γ+κ)​b3(\gamma+\kappa)bfrom the weight-one states, givingγ​a=(γ+κ)​b\gamma a=(\gamma+\kappa)b. With the normalization2​a+6​b=12a+6b=1, this fixesb=γ/[2​(κ+4​γ)]b=\gamma/[2(\kappa+4\gamma)]. Each adjacent check is violated by exactly four configurations, each carrying probabilitybb, soV∞(B)\displaystyle V_{\infty}^{(B)}=Pr⁡[b1≠b2]+Pr⁡[b2≠b3]=8​b\displaystyle=\Pr[b_{1}\neq b_{2}]+\Pr[b_{2}\neq b_{3}]=8b(38)=4​γκ+4​γ\displaystyle=\frac{4\gamma}{\kappa+4\gamma}

matching the quantum steady-state violationV∞(Q)V_{\infty}^{(Q)}of Eq. (29) for this reduced model. The two generators therefore share the same off-manifold residual under persistent noise, governed by the single ratioγ/κ\gamma/\kappa.

## VConclusions

This work argues that quantum error correction and biological error correction in neuronal circuits share a common organizational pattern: redundant encoding of protected information with constraint-based inference that detects and suppresses errors. To make this analogy precise, we constructed a structural dictionary whose core objects are summarized in Table1: physical qubits, logical qubits, the codespaceC(Q)C^{(Q)}, noise, and code distanced(Q)d^{(Q)}map onto noisy physical unitsxi(B)x^{(B)}_{i}, low-dimensional cognitive variablesXα(B)X^{(B)}_{\alpha}, a neural manifoldℳ(B)\mathcal{M}^{(B)}, neural noise, and a robustness scaled(B)d^{(B)}. The extended mapping of checks, syndromes, ancillary degrees of freedom, decoding, and recovery is developed in Secs.III.2–III.3. The correspondence is structural rather than physical: neurons are treated throughout as noisy classical elements, and no quantum coherence or entanglement is invoked in biological tissue.

In addition to the dictionary, we show that this correspondence can be made quantitative in a minimal model. A three-neuron, recurrently coupled population with leaky integrate-and-fire dynamics and an Ornstein–Uhlenbeck subthreshold potential reduces, in the metastable regime to a classical master equation over binary configurations, Eq. (35). This generator has the same structure as the continuous-time recovery generator of the three-qubit repetition code, Eq. (25): independent bit-flip noise appears as independent single-unit flips at rateγ\gamma, and the recovery channel is replaced by a majority-pull term at rateκ\kappagenerated by the recurrent couplingwcouplew_{\text{couple}}. The resulting dynamics, Fig.3, mirror the dynamics of the quantum counterpart, Fig.2. In particular, both systems display the same distinction between projection and damping recovery: exact correction returns the state to the codespace, whereas continuous-time recovery suppresses constraint violation, leaving a nonzero steady-state residual.

Casting both systems in this shared language suggests transfer in both directions. From biology to QEC, neural error control is local, continuous in time, and adaptive, properties that remain challenging for engineered decoders. From QEC to neuroscience, the notions of codespace, syndrome, decoder, and distance supply a quantitative vocabulary in which the representational robustness of a neural code can be defined and ultimately measured.

One caveat, however, is that the correspondence is an analogy of roles, not an identification of mechanisms: neurons are computationally far richer than qubits, and the reduction to a binary code relies on the metastable regime and on treating single-unit noise as independent. We keep the ratesγ\gammaandκ\kappasymbolic, establishing the structural correspondence without committing to parameter identification. The quantitative model captures only the neuronal layer while we acknowledge that astrocytes may contribute to neuronal computation and biological error control.

## V.1Future Work – Astrocytes and Derived Algorithms

In this work, we argued that astrocytes may contribute to biological error control and prevention, however, we do not use them to inform our analogy outside of their potential role as analogs of ancillary degrees of freedom. Astrocytes are the most numerous cell within the brain and may bind to between270,000270,000and 2 million synapses[18,35]. They process information from the neurons, integrating the neurons’ activations non-linearly, suggesting they may play an active computational role[36]. Therefore, astrocytes may play an important, but still incompletely understood role in the neuron’s population coding scheme. One mechanism they may act through is by reshaping and adapting the neuronal network for specific contexts, as suggested by Murphy-Royal et al.[29].

In some ways, astrocytes may contribute to the brain’s error protection. Since the brain is a subcritical system that operates close to criticality, astrocytes may help regulate the system’s state by modulating transmission and plasticity[13,32]. Astrocytes are large and highly connected, enabling them to regulate far-away synapses, and suggesting how a network of the cells could contribute to brain stability[15]. Finally, astrocytes have been linked to neuronal network self-repair, which suggests they may help detect faults and address them autonomously[47].

Astrocyte-inspired algorithms suggest a useful analogy to syndrome extraction: continuous syndrome-like monitoring. In rhythmic sharing, the oscillator phases are not themselves syndromes. Rather, deviations of synchrony or phase-locking structure from a learned baseline provide mismatch signals indicating that the current input stream is no longer compatible with the learned dynamical regime. The resulting reconfiguration is therefore closer to adaptive constraint monitoring than to projective stabilizer readout. For example, the Rhythmic Sharing algorithm modulates effective synaptic coupling via slow oscillations driven by astrocytic rhythms[22]. Such rhythms can provide otherwise static recurrent networks with adaptive performance and sensitivity to distributional shift[49].

Another algorithm based on astrocytes, calledδ→\vec{\delta}-Multiplexed Gradient Descent, uses an astrocyte-inspired module to change an artificial neural network’s weights, leading to a biologically-plausible alternative to backpropagation[33]. This suggests how astrocyte-like variables could help establish population codes for complex neuronal problem-solving. In quantum, logical information is encoded into highly entangled subspaces of many physical qubits; ancillary qubits are used to measure stabilizer generators (parity checks); algorithms map syndrome patterns to correction operations[31,44]. In biology, classical population codes are implemented by neurons, with astrocytes potentially supplying additional degrees of freedom that monitor, average, and modulate neural activity. We plan to carry out future work to understand how astrocytes fit within the analogy we have discussed here.

## Acknowledgements

This study was funded in part by the Air Force Office of Scientific Research Biophysics Program [GrantsFA9550-22-1-0405andFA9550-25-1-0002]. The funder played no role in study design, data collection, analysis and interpretation of data, or the writing of this manuscript.

## References
- [1]B. Adams and F. Petruccione(2020)Quantum effects in the brain: a review.AVS Quantum Science2(2).Cited by:§I.
- [2]C. Ahn, A. C. Doherty, and A. J. Landahl(2002)Continuous quantum error correction via quantum feedback control.Physical Review A65(4),pp. 042301.External Links:DocumentCited by:§IV.2.
- [3]I. Aizenbud, D. Beniaguev, N. Pnueli, I. Segev, and M. London(2026)What can a neuron compute.bioRxiv.External Links:Document,LinkCited by:§II.3.2.
- [4]J. E. Arle, L. Mei, and K. W. Carlson(2020-08)Robustness in neural circuits.InBrain and Human Body Modeling 2020,pp. 213–229.External Links:Document,ISBN 9783030456238,LinkCited by:§II.3.1,5th item.
- [5]V. J. Barranca(2026-12)Distance-dependent connectivity in the brain facilitates high dynamical and structural complexity.Cogn. Neurodyn.20(1),pp. 23(en).Cited by:§III.4.
- [6]D. Beniaguev, I. Segev, and M. London(2021)Single cortical neurons as deep artificial neural networks.Neuron109(17),pp. 2727–2739.e3.External Links:ISSN 0896-6273,Document,LinkCited by:§II.3.2.
- [7]M. J. Berry and G. Tkačik(2020)Clustering of neural activity: a design principle for population codes.Frontiers in Computational NeuroscienceVolume 14 - 2020.External Links:Document,ISSN 1662-5188,LinkCited by:§II.3.1,§II.3.1.
- [8]M. Boerlin, C. K. Machens, and S. Denève(2013-11)Predictive coding of dynamical variables in balanced spiking networks.PLoS Computational Biology9(11),pp. e1003258.External Links:Document,ISSN 1553-7358,LinkCited by:§II.3.1.
- [9]R. Bourdoukan, D. Barrett, S. Deneve, and C. K. Machens(2012)Learning optimal spike-based representations.InAdvances in Neural Information Processing Systems,F. Pereira, C.J. Burges, L. Bottou, and K.Q. Weinberger (Eds.),Vol.25,pp..External Links:LinkCited by:§II.3.1.
- [10]Y. Burak and I. R. Fiete(2009)Accurate path integration in continuous attractor network models of grid cells.PLoS Computational Biology5(2),pp. e1000291.External Links:DocumentCited by:§I,§III.1,§III.2,§III.3.
- [11]A. N. Burkitt(2006-08)A review of the integrate-and-fire neuron model: II. inhomogeneous synaptic input and network properties.Biol. Cybern.95(2),pp. 97–112(en).Cited by:§IV.3,§IV.3.
- [12]N. Calaim, F. A. Dehmelt, P. J. Gonçalves, and C. K. Machens(2022-05)The geometry of robustness in spiking neural networks.eLife11,pp. e73276.External Links:Document,ISSN 2050-084X,LinkCited by:§II.3.1,5th item.
- [13]R. Calvo, C. Martorell, A. Roig, and M. A. Muñoz(2026-02)Robust scaling in human brain dynamics despite correlated inputs and limited sampling distortions.Phys. Rev. Lett.136,pp. 068402.External Links:Document,LinkCited by:§II.3.1,5th item,§V.1.
- [14]R. Chaudhuri and I. R. Fiete(2016)Computational principles of memory.Nature Neuroscience19,pp. 394–403.External Links:DocumentCited by:§I,§III.1,§III.2,§III.3.
- [15]A. Covelo and A. Araque(2016)Lateral regulation of synaptic transmission by astrocytes.Neuroscience323,pp. 62–66.Note:Dynamic and metabolic astrocyte-neuron interactions in healthy and diseased brainExternal Links:Document,ISSN 0306-4522,LinkCited by:§V.1.
- [16]T. J. Craddock(2025)Quantum mechanisms in the brain: from conjectures and theories to experimental evidence.InQuantum Effects and Measurement Techniques in Biology and Biophotonics II,Vol.13340,pp. 1334003.Cited by:§I.
- [17]M. Derakhshani, L. Diósi, M. Laubenstein, K. Piscicchia, and C. Curceanu(2022)At the crossroad of the search for spontaneous radiation and the orch or consciousness theory.Physics of Life Reviews42,pp. 8–14.Cited by:§I.
- [18]M. R. Freeman and D. H. Rowitch(2013)Evolving concepts of gliogenesis: a look way back and ahead to the next 25 years.Neuron80(3),pp. 613–623.Cited by:§V.1.
- [19]D. Gottesman(1997)Stabilizer codes and quantum error correction.Ph.D. Thesis,California Institute of Technology.Note:arXiv:quant-ph/9705052External Links:DocumentCited by:§IV.2.
- [20]E. Hairer and G. Wanner(1991)Solving ordinary differential equations ii.Springer Berlin Heidelberg.External Links:ISBN 9783662099476,ISSN 0179-3632,Link,DocumentCited by:§IV.2.
- [21]K. O. Johnson(2000)Neural coding.Neuron26(3),pp. 563–566.External Links:Document,ISSN 0896-6273,LinkCited by:§II.3.1.
- [22]H. Kang and W. Losert(2026-03)Rhythmic sharing: a bioinspired paradigm for zero-shot adaptive learning in neural networks.Phys. Rev. Res.8,pp. 013267.External Links:Document,LinkCited by:§V.1.
- [23]J. Kerckhoff, H. I. Nurdin, D. S. Pavlichin, and H. Mabuchi(2010)Designing quantum memories with embedded control: photonic circuits for autonomous quantum error correction.Physical Review Letters105(4),pp. 040502.External Links:DocumentCited by:§IV.2.
- [24]P. Kofuji and A. Araque(2021)Astrocytes and behavior.Annual Review of Neuroscience44,pp. 49–67.External Links:DocumentCited by:§III.1,§III.2.
- [25]H. Leeet al.(2014)Astrocytes contribute to gamma oscillations and recognition memory.Proceedings of the National Academy of Sciences of the USA111(32),pp. E3343–E3352.External Links:DocumentCited by:§III.1,§III.2.
- [26]Y. Li, X. Zhu, Y. Qi, and Y. Wang(2024-07)Revealing unexpected complex encoding but simple decoding mechanisms in motor cortex via separating behaviorally relevant neural signals.eLife Sciences Publications, Ltd.External Links:Document,LinkCited by:§II.3.1,§II.3.2.
- [27]S. Lim and M. S. Goldman(2013-08)Balanced cortical microcircuitry for maintaining information in working memory.Nature Neuroscience16(9),pp. 1306–1314.External Links:Document,ISSN 1546-1726,LinkCited by:§II.3.1.
- [28]C. Murphy-Royal, S. Ching, and T. Papouin(2022)Contextual guidance: an integrated theory for astrocytes function in brain circuits and behavior.arXiv preprint.External Links:2211.09906Cited by:§III.1,§III.2.
- [29]C. Murphy-Royal, S. Ching, and T. Papouin(2023-10)A conceptual framework for astrocyte function.Nature Neuroscience26(11),pp. 1848–1856(en).External Links:Document,LinkCited by:§V.1.
- [30]H. Neven, A. Zalcman, P. Read, K. S. Kosik, T. van der Molen, D. Bouwmeester, E. Bodnia, L. Turin, and C. Koch(2024)Testing the conjecture that quantum processes create conscious experience.Entropy26(6),pp. 460.Cited by:§I.
- [31]M. A. Nielsen and I. L. Chuang(2010)Quantum computation and quantum information.10th Anniversary Edition edition,Cambridge University Press,Cambridge.Cited by:§I,§II.2,§II.2,§II.2,§III.1,§III.2,§V.1.
- [32]J. A. Noriega-Prieto and A. Araque(2021-04)Sensing and regulating synaptic activity by astrocytes at tripartite synapse.Neurochemical Research46(10),pp. 2580–2585(en).External Links:Document,LinkCited by:§V.1.
- [33]R. O’Loughlin, B. Oripov, N. Skuda, N. Chongsiriwatana, I. Whitehouse, W. Losert, B. Hayes, A. McCaughan, and S. Buckley(2026)δ→\vec{\delta}Multiplexed gradient descent: perturbative learning with astrocytes.In2026 Neuro Inspired Computational Elements (NICE),Vol.,pp. 1–9.External Links:DocumentCited by:§V.1.
- [34]K. M. O’Neillet al.(2023)Decoding natural astrocyte rhythms: dynamic actin waves result from environmental sensing by primary rodent astrocytes.Advanced Biology7(6),pp. 2200269.External Links:DocumentCited by:§III.1,§III.2.
- [35]N. A. Oberheim, T. Takano, X. Han, W. He, J. H. C. Lin, F. Wang, Q. Xu, J. D. Wyatt, W. Pilcher, J. G. Ojemann, B. R. Ransom, S. A. Goldman, and M. Nedergaard(2009-03)Uniquely hominid features of adult human astrocytes.The Journal of Neuroscience29(10),pp. 3276–3287.External Links:Document,ISSN 1529-2401,LinkCited by:§V.1.
- [36]G. Perea, M. Navarrete, and A. Araque(2009)Tripartite synapses: astrocytes process and control synaptic information.Trends in Neurosciences32(8),pp. 421–431.External Links:Document,ISSN 0166-2236,LinkCited by:§V.1.
- [37]H. Safaai, A. Y. Wang, S. Kira, S. Blanco Malerba, S. Panzeri, and C. D. Harvey(2025-10)Specialized structure of neural population codes in parietal cortex outputs.Nature Neuroscience28(12),pp. 2550–2560.External Links:Document,ISSN 1546-1726,LinkCited by:§II.3.1,§II.3.2.
- [38]M. Santello, N. Toni, and A. Volterra(2019)Astrocyte function from information processing to cognition and cognitive impairment.Nature Neuroscience22(2),pp. 154–166.External Links:DocumentCited by:§III.1,§III.2.
- [39]M. Sarovar and G. J. Milburn(2005)Continuous quantum error correction by cooling.Physical Review A72(1),pp. 012306.External Links:DocumentCited by:§IV.2.
- [40]L. F. Seoane(2019-04)Evolutionary aspects of reservoir computing.Philosophical Transactions of the Royal Society B: Biological Sciences374(1774),pp. 20180377.External Links:Document,ISSN 0962-8436,LinkCited by:§II.3.1.
- [41]P. W. Shor(1995)Scheme for reducing decoherence in quantum computer memory.Physical Review A52(4),pp. R2493–R2496.External Links:DocumentCited by:§I,§II.2,§II.2,§IV.2.
- [42]S. Sreenivasan and I. R. Fiete(2011)Grid cells generate an analog error-correcting code for singularly precise neural computation.Nature Neuroscience14(10),pp. 1330–1337.External Links:DocumentCited by:§I,§III.2,§III.3.
- [43]C. Teeter, R. Iyer, V. Menon, N. Gouwens, D. Feng, J. Berg, A. Szafer, N. Cain, H. Zeng, M. Hawrylycz, C. Koch, and S. Mihalas(2018-02)Generalized leaky integrate-and-fire models classify multiple neuron types.Nature Communications9(1).External Links:ISSN 2041-1723,Link,DocumentCited by:§II.3.2.
- [44]B. M. Terhal(2015)Quantum error correction for quantum memories.Reviews of Modern Physics87(2),pp. 307–346.External Links:DocumentCited by:§I,§II.2,§II.2,§II.2,§III.1,§III.2,§III.3,§III.4,§IV.2,§V.1.
- [45]G. Tkačik, J. S. Prentice, V. Balasubramanian, and E. Schneidman(2010)Optimal population coding by noisy spiking neurons.Proceedings of the National Academy of Sciences107(32),pp. 14419–14424.External Links:Document,LinkCited by:§II.3.1,§II.3.2.
- [46]J. von Neumann(1956)Probabilistic logics and the synthesis of reliable organisms from unreliable components.InAutomata Studies,C. E. Shannon and J. McCarthy (Eds.),Annals of Mathematics Studies, Vol.34,pp. 43–98.Cited by:§I.
- [47]J. Wade(2012)Self-repair in a bidirectionally coupled astrocyte-neuron (an) system based on retrograde signaling.Frontiers in Computational Neuroscience6.External Links:Document,LinkCited by:§V.1.
- [48]H. Wahbeh, D. Radin, C. Cannard, and A. Delorme(2022)What if consciousness is not an emergent property of the brain? observational and empirical challenges to materialistic models.Frontiers in Psychology13,pp. 955594.Cited by:§I.
- [49]I. Whitehouse, H. Kang, and W. Losert(2026-06)Emergent detection of concept drift within the glia-inspired ‘rhythmic sharing’ algorithm.npj Unconventional Computing3(1).External Links:ISSN 3004-8672,Link,DocumentCited by:§III.3,§V.1.
- [50]W. Xie, J. H. Wittig, J. I. Chapeton, M. El-Kalliny, S. N. Jackson, S. K. Inati, and K. A. Zaghloul(2024-10)Neuronal sequences in population bursts encode information in human cortex.Nature635(8040),pp. 935–942.External Links:Document,ISSN 1476-4687,LinkCited by:§II.3.1,§II.3.2.
- [51]A. Zlokapa, A. K. Tan, J. M. Martyn, I. R. Fiete, M. Tegmark, and I. L. Chuang(2024)Fault-tolerant neural networks from biological error correction codes.Physical Review E110(5),pp. 054303.External Links:DocumentCited by:§I,§III.4.

## 


- 


Major funding support from
