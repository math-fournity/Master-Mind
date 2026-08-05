# A Research-Informed Module on Quantum Superposition for Rapid Classroom Adoption

**arXiv ID**: 2605.23976v1
**Authors**: Boris Kiefer
**Published**: 2026-05-13
**Categories**: physics.ed-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2605.23976v1

## Abstract

We present an adoption-ready instructional module for introducing quantum superposition in a two-state system. The package combines a five-activity classroom sequence with grading-ready assessment materials organized around six conceptual barriers documented in the physics education research literature: interpreting superposition as physical splitting, confusing coherent superposition with classical mixture, making basis-change errors, misreading finite-sample fluctuations as changes in the underlying state, using inconsistent notation, and, in an optional extension, reasoning about ordered operations. The main claim is that the bottleneck for introductory quantum instruction is rarely the absence of a usable simulator, but rather the absence of a coherent activity sequence, barrier-targeted prompts, and aligned assessment tools that an instructor can deploy without additional development work. We make the instructional rationale explicit through backward mapping from documented barriers to activity prompts and rubric-based evidence. The resulting module is designed for a single 50-minute class meeting and can be implemented with the included notebook or adapted to comparable two-state quantum simulators.

## Full Text

A Research-Informed Module on Quantum Superposition for Rapid Classroom Adoption

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2605.23976v1 [physics.ed-ph] 13 May 2026

## A Research-Informed Module on Quantum Superposition for Rapid Classroom AdoptionBoris KieferDepartment of Physics, New Mexico State University, Las Cruces, NM 88003, USA

## Abstract

We present an adoption-ready instructional module for introducing quantum superposition in a two-state system. The package combines a five-activity classroom sequence with grading-ready assessment materials organized around six conceptual barriers documented in the physics education research literature: interpreting superposition as physical splitting, confusing coherent superposition with classical mixture, making basis-change errors, misreading finite-sample fluctuations as changes in the underlying state, using inconsistent notation, and, in an optional extension, reasoning about ordered operations. The main claim is that the bottleneck for introductory quantum instruction is rarely the absence of a usable simulator, but rather the absence of a coherent activity sequence, barrier-targeted prompts, and aligned assessment tools that an instructor can deploy without additional development work. We make the instructional rationale explicit through backward mapping from documented barriers to activity prompts and rubric-based evidence. The resulting module is designed for a single 50-minute class meeting and can be implemented with the included notebook or adapted to comparable two-state quantum simulators.

## IIntroduction

Superposition is often the point at which students first confront the difference between classical state descriptions and amplitude-based quantum reasoning. Even in two-state systems, students commonly struggle to coordinate basis choice, state representation, and measurement statements[1,2,3,4]. Reported difficulties include treating superposition as physical splitting, confusing coherent superpositions with classical mixtures, making basis-dependent prediction errors, and misreading finite measurement samples as changes in the underlying state[5,6,7,8,9].

A range of quantum learning tools already exists. PhET and QuVis lower access barriers through browser-based interactives and broad topic coverage[10,11], while research-oriented platforms such as QuTiP and Qiskit support flexible modeling in more advanced settings[12,13]. These tools address the technical barrier to simulation effectively. The instructional problem addressed here is different: an instructor preparing a single class meeting still must decide which conceptual barriers to address, write prompts that target those barriers, and construct aligned formative checks. This module does not claim simulator novelty as its primary contribution. It includes a reference simulator, but its main contribution is the activity sequence, concept checks, rubric, and implementation path that existing tools typically leave for the instructor to assemble.

The module is intentionally narrow. Restricting scope to a two-state system with a fixed prepared input state allows the entire package to fit within a single class meeting. The payoff is a feasible implementation path, explicit alignment between documented difficulties and activity prompts, and assessment artifacts suitable for rapid grading. The finite-sampling activity deserves particular emphasis because it addresses a persistent misconception that is systematically underemphasized in short superposition modules: finite-run frequencies fluctuate even when the quantum state and theoretical probabilities remain unchanged[8,14].

To make the classroom use explicit, the instructor distributes a single worksheet containing the five activity prompts and the five concept-check items. Students alternate between short written predictions, simulator interaction, and brief explanations. After class, the instructor grades the collected worksheets with a rubric. The Supplementary Material provides the concept checks, pre/post prompts, answer key, deployment variants, and the reference notebook used in the paper. What is new here is not simulation capability, but the integration of barrier selection, activity wording, concept checks, rubric scoring, and a one-class implementation path into a single package ready for immediate use.

## IIDesign logic and barrier-to-design mapping

## II.1Barrier selection

The module is organized around six recurrent learner barriers drawn from the PER literature. Barriers were included if they were documented in the literature and could be addressed within a two-state, fixed-preparation setting without formalism beyond introductory quantum mechanics. For the core in-class sequence (C1–C4, C6), we prioritized barriers supported by multiple independent studies. The ordered-operations extension (C5) is treated separately as an optional enrichment topic that is pedagogically accessible in this setting but not essential to the main 50-minute module. Barriers requiring density matrices, multi-qubit entanglement, or full Hamiltonian time evolution were excluded as outside the scope of a single class meeting, though they are natural extensions of this work.

The six selected barriers are:
- •

C1:superposition interpreted as physical splitting[5,7];
- •

C2:basis-change and measurement-context errors[6,9];
- •

C3:conflation of coherent superposition and classical mixture[7,15];
- •

C4:confusion between Born probabilities and finite-sample frequencies[8,14];
- •

C5:difficulty reasoning about ordered operations[16];
- •

C6:notation-level ambiguity between amplitudes, basis states, and measurement claims[17,18,19].

## II.2Learning goals and backward mapping

These barriers motivate five learning goals. After the module, students should be able to: (LG1) distinguish coherent superposition from classical mixture; (LG2) predict basis-dependent measurement probabilities; (LG3) interpret finite-sample variability without changing the underlying state; (LG4) explain how phase conventions and basis choice affect quantum-state descriptions at an introductory level; and (LG5) communicate reasoning in consistent Dirac notation. Ordered-operation reasoning is treated as an optional extension aligned with LG4.

Documented barriers determine the learning goals, which in turn determine the activity prompts and assessment evidence. Table1makes that alignment explicit. An instructor adapting the module for a different topic can use the same structure: identify barriers from the literature, state the design response as a prompt or activity type, and specify which assessment item provides evidence for each learning goal.

Barrier C6 is treated differently from the others. Rather than being assigned to a single activity, it is reinforced throughout the sequence via reflection prompts embedded in every activity and a dedicated rubric row. This choice reflects the finding that notation errors often persist even when conceptual understanding improves, and that targeted notation feedback at multiple points is more effective than a single isolated exercise[17,19].Table 1:Mapping from documented student difficulties to design responses and assessment evidence. CC and PP labels refer to supplementary concept checks and pre/post prompts.BarrierPER finding(s)Design responseWhere implementedLearning goals and aligned evidence
C1Superposition interpreted as splitting[5,7].Amplitude-explicit labels and repeated Born sampling.Activities 1 and 3; simulator panel.LG1, LG5:CC1,PP1. Distinguish coherent superposition from classical mixture and explain single-shot versus ensemble language.C2Basis-tracking and measurement-context errors[6,9].Explicit basis selector and side-by-side probability updates.Activities 2–4.LG2, LG5:CC2,PP2. Basis-specific projection prediction and notation-consistent justification.C3Mixture versus coherent superposition conflation[7,15].Phase-sensitive comparison tasks in an incompatible basis.Activity 3.LG1, LG4:CC1,PP1. Identify coherence signatures in an incompatible basis; optional extension connects phase reasoning to ordered operations.C4Finite-sample misconceptions[8,14].NtrialN_{\text{trial}}control, histogram, and uncertainty language.Activity 5 and statistics panel.LG3:CC3,PP3. Separate sampling variability from changes in state preparation.C5Ordered-operation reasoning errors[16].Optional analytic extension on operator order.Supplementary challenge material.LG4:CC4,PP4. Introductory non-commutativity reasoning.C6Notation and interpretation disconnect[17,19,2].Consistent notation and reflection prompts throughout.All activities and rubric rows.LG5:CC5,PP5. Coherent symbolic-to-verbal explanation quality.


## IIIQuantum framework and simulator conventions

The activities assume a fixed prepared input state|+z⟩\ket{+z}analyzed in a user-selected basis. The analysis basis is parameterized by the standardU​3U3/ZYZ Euler decomposition[20]U​(θ,ϕ,λ)=Rz​(ϕ)​Ry​(θ)​Rz​(λ),U(\theta,\phi,\lambda)=R_{z}(\phi)\,R_{y}(\theta)\,R_{z}(\lambda),(1)

whereRk​(φ)=e−i​φ​σk/2R_{k}(\varphi)=e^{-i\varphi\sigma_{k}/2}. The displayed basis states are|0⟩=U†​|+z⟩,|1⟩=U†​|−z⟩,\ket{0}=U^{\dagger}\ket{+z},\qquad\ket{1}=U^{\dagger}\ket{-z},(2)

and the Born-rule probabilities arePtheo​(k)=|⟨k|+z⟩|2,k∈{0,1}.P_{\mathrm{theo}}(k)=|\braket{k|+z}|^{2},\qquad k\in\{0,1\}.(3)

The convention is passive:UUrotates the analyzer frame rather than the state. Instructors using a tool that rotates the state vector, as in a Bloch-sphere display, can apply the same activity prompts with the substitutionU→U†U\to U^{\dagger}in the interface; all probability expressions and student-facing questions are unchanged. The full matrix form ofU​(θ,ϕ,λ)U(\theta,\phi,\lambda)is given in Supplementary Material S2 for reference.

Several reference settings are useful across the activities:U​(0,0,0)U(0,0,0)gives the identity analyzer (aligned with the preparation),U​(π,0,π)U(\pi,0,\pi)gives theσx\sigma_{x}analyzer,U​(π,π/2,π/2)U(\pi,\pi/2,\pi/2)givesσy\sigma_{y}, andU​(0,0,π)U(0,0,\pi)givesσz\sigma_{z}, all up to global phase[20].

A pedagogically useful feature of this parameterization is that different parameter triples(θ,ϕ,λ)(\theta,\phi,\lambda)can produce basis states that differ only by overall phase. The printed ket components may change abruptly when angles wrap, even though all measurable probabilities remain unchanged. This provides a concrete, simulator-verifiable illustration of global-phase invariance that recurs across Activities 2 and 4.

The included Jupyter notebook is the reference implementation used in this paper because its notation and controls match the activity wording (Fig.1). The sequence can also be adapted to comparable two-state quantum simulators, including PhET or QuVis, provided that the interface displays basis states, reports Born-rule probabilities, and allows students to vary analyzer orientation and trial count. Minor wording changes may be needed when a tool uses different controls or a different visualization convention.Figure 1:Simulator interface (included Jupyter notebook) showing analyzer-angle controls, trial count and seed inputs, theoretical and sampled probabilities, and an outcome histogram. Any two-state simulator with equivalent affordances can substitute; see text for portability notes.

## IVActivity sequence

The module is designed for a single class meeting, with optional challenge extensions assigned outside class. The five activities move from aligned-basis measurement through incompatible-basis reasoning to finite-sample statistics. Notation consistency is reinforced throughout via embedded reflection prompts rather than assigned to a single activity.

Each activity uses a predict–observe–explain structure. Students first record a written prediction, then compare it with the simulator output, and finally write a brief explanation reconciling the two. Predictions are completed individually before simulator interaction, and the final written explanations are collected as the main assessment artifacts for that activity. This structure is consistent with evidence that recording written predictions before observation improves conceptual engagement and reduces uncritical acceptance of confirming outcomes[21,11].

## Activity 1: aligned-basis measurement (C1, C2).

With the analyzer set to the identity orientation (θ=0\theta=0), the basis is aligned with the preparation and the simulator reportsPtheo​(0)=1P_{\text{theo}}(0)=1andPtheo​(1)=0P_{\text{theo}}(1)=0. The prompt asks students to explain this outcome in terms of state–basis alignment rather than device behavior, and to predict what would change if the input state were|−z⟩\ket{-z}instead. The purpose is to establish early that deterministic outcomes reflect a relationship between preparation and measurement basis, not a property intrinsic to either alone.

## Activity 2: global phase and basis labeling (C1, C2).

Settingλ=π\lambda=\piwithθ=0\theta=0changes the sign of the displayed|1⟩\ket{1}component but leaves all probabilities unchanged. Students record both the displayed state vector and the probabilities, then explain in one sentence why the two descriptions are physically equivalent. This gives a compact, simulator-verifiable illustration of global-phase invariance and reinforces the distinction between displayed state vectors and observable outcomes — a common source of notation confusion (C6).

## Activity 3: incompatible basis and coherence (C2, C3).

This is the conceptual core of the module. With the analyzer set to thexxbasis viaU​(π/2,0,0)U(\pi/2,0,0), the simulator reports equal probabilities for the prepared state|+z⟩\ket{+z}in both outcome slots. Students are then given two hypothetical source descriptions and asked to predict whetherxx-basis probabilities would differ between them. Source A produces the coherent superposition|ψA⟩=|+z⟩+|−z⟩2=|+x⟩,\ket{\psi_{A}}=\frac{\ket{+z}+\ket{-z}}{\sqrt{2}}=\ket{+x},(4)

while Source B produces a 50/50 classical mixture of|+z⟩\ket{+z}and|−z⟩\ket{-z}. Both sources yield identicalzz-basis statistics, so thezz-basis simulator readout cannot distinguish them. Students project each description onto|+x⟩\ket{+x}and|−x⟩\ket{-x}and compare. The crucial observation is that Source A is already the eigenstate|+x⟩\ket{+x}and therefore gives a definite outcome in thexxbasis, whereas Source B gives equal probabilities. Class discussion links this result to the coherent-superposition versus mixture distinction and to the need to specify a basis when characterizing a state.

## Activity 4: general basis exploration (C2).

Students vary(θ,ϕ,λ)(\theta,\phi,\lambda)freely and record how the displayed basis states and probabilities change. The prompt directs attention to three observations: (i) probabilities always sum to one regardless of analyzer orientation; (ii) in this module’s fixed-input convention, changingϕ\phiorλ\lambdacan alter the displayed phase labeling of the kets while leaving the reported probabilities unchanged whenθ\thetais fixed — students are asked to write one sentence explaining why the probabilities are unaffected; and (iii) abrupt sign changes in displayed kets at angle wrap-around leave probabilities unchanged, revisiting the global-phase point from Activity 2. The ordered-operations extension is assigned only as a supplementary challenge so that the main sequence remains focused on basis and probability (Supplementary Material S3).

## Activity 5: finite sampling and uncertainty (C4).

Students hold the analyzer fixed and vary only the trial countNtrialN_{\text{trial}}and random seed, observing how the sampled frequencyp^\hat{p}fluctuates around the theoretical probabilityPtheoP_{\text{theo}}. The prompt asks them to estimate the standard error (Supplementary Material S4)S​E​(p^)=p^​(1−p^)/NtrialSE(\hat{p})=\sqrt{\hat{p}(1-\hat{p})/N_{\text{trial}}}(5)

for two values ofNtrialN_{\text{trial}}and to explain explicitly why the spread in outcomes decreases without implying that the quantum state changed. This activity addresses an instructional gap common to short superposition modules: students often apply the Born rule correctly as a formula yet still interpret run-to-run variability as evidence of state collapse or state change[8]. The emphasis on language, asking students to write a sentence that correctly attributes the variability to sampling, not to the state, connects naturally to C6.Figure 2:Measurement structure for Activities 1–4. The fixed prepared state|+z⟩\ket{+z}is analyzed in basis states{|0⟩,|1⟩}={U†​|+z⟩,U†​|−z⟩}\{\ket{0},\ket{1}\}=\{U^{\dagger}\ket{+z},U^{\dagger}\ket{-z}\}, yielding probabilitiesPtheo​(k)=|⟨k|+z⟩|2P_{\text{theo}}(k)=|\braket{k|+z}|^{2}. Panel (a) shows aligned-basis measurement, (b) a phase-only display change, (c) incompatiblexx-basis measurement, and (d) a general analyzer orientation.

## VImplementation and assessment

## V.1Timing and deployment modes

A full 50-minute implementation proceeds as follows: a 5-minute prediction-first warmup using the pre/post prompt PP1 (supplemental material S5); 10 minutes of instructor-led work on Activities 1 and 2; 12 minutes of paired work on Activity 3 including the pencil-and-paper prediction and class debrief; 10 minutes for Activity 4; 8 minutes for Activity 5; and a 5-minute exit prompt drawn from CC3 or CC5 (Supplementary Material S5). Optional challenge items may be assigned as homework.

Two compressed modes are supported for time-constrained settings. In apartialmode, Activities 1–3 are completed in class and Activity 5 plus one concept-check item are assigned as homework; this preserves the coherence/mixture distinction as the in-class centerpiece. In aflippedmode, Activities 1 and 2 are completed before class using the pre-reading and simulator, so that class time focuses on Activity 3 and the statistics discussion in Activity 5.

## V.2Assessment design

Assessment is built at two levels: brief in-class concept checks (CC1–CC5) and matched pre/post prompts (PP1–PP5). All items are designed for paper collection and straightforward rubric-based grading without requiring a learning management system or automated scoring. Table2summarizes the rubric, and the full item text and answer keys appear in the Supplementary Material S5.

The rubric is designed for single-grader use in a typical course context. The binary LG5 criterion and the anchored partial-credit descriptions for LG1–LG3 are intended to minimize scorer discretion: each performance level is defined by the presence or absence of a specific identifiable element rather than by holistic impression. LG4 is optional and its rubric row applies only when the ordered-operations extension is assigned.Table 2:Grading rubric for the module (10 points total).CriterionPerformance levelsLG1 (0–2 pts)Superposition versus mixture: cites coherence/phase in an incompatible basis (2); partial basis reasoning (1); incorrect (0).LG2 (0–3 pts)Probability prediction: correct projection setup and numerics (3); minor error or one probability correct (2); setup only (1); incorrect (0).LG3 (0–2 pts)Sampling interpretation: correctly separates estimator variability from state change (2); partly correct (1); incorrect (0).LG4 (0–2 pts)Optional operation-order reasoning: correct matrix products plus physical interpretation (2); partial argument (1); incorrect (0).LG5 (0–1 pt)Notation consistency: consistent basis-aware notation throughout (1); inconsistent or incorrect (0).

Representative prompts illustrate the alignment between items and barriers. For LG1, students explain why a coherent superposition and a classical mixture can produce identical statistics in one basis but differ in another. For LG2, students computeP​(+x)P(+x)andP​(−x)P(-x)for a state expressed in thezzbasis, showing the projection steps. For LG3, students interpret the effect of increasingNtrialN_{\text{trial}}on the standard error without claiming that the state evolved or collapsed differently. These tasks keep the emphasis on basis-aware reasoning rather than algebra for its own sake. LG4 is included only as an optional extension and is not required for the core 50-minute implementation.

## VIScope and contribution

The module deliberately excludes density matrices, continuous-variable systems, multi-qubit entanglement, sequential projective measurement with explicit state update, and Hamiltonian time evolution. Each exclusion follows the same criterion used for barrier selection: the topic cannot be addressed within a two-state, fixed-preparation setting without introducing formalism that exceeds a single class meeting. These are natural next modules rather than weaknesses of this one.

Within that scope, the paper contributes a classroom-ready example of barrier-targeted instructional design. The activity sequence, prompts, and rubric are tied to specific conceptual barriers documented in the PER literature rather than assembled as generic add-ons to a simulator. We treat the integrated design of activities, assessment, and implementation materials as a contribution independent of learning-gain measurement. The included assessment artifacts are ready for immediate classroom use and designed to support future validation work across institutional settings.

## VIIConclusion

We have presented a classroom-ready superposition module for a two-state system built around documented student difficulties rather than around simulator features alone. Its main contribution is the coordinated packaging of activities, prompts, and assessment materials into a form that an instructor can adopt quickly for a single class meeting. The backward-mapping table makes the design logic explicit and portable, Activity 3 provides the conceptual centerpiece, and the finite-sampling activity addresses a difficulty that is often underrepresented in short introductory treatments of superposition.

## Acknowledgements.BK gratefully acknowledge support through the U.S. National Science Foundation under award numbers OST-2410813 and OST-2531569.

## Data and code availability

The simulator notebook, teaching materials, documentation, and example activities are available in the public GitHub repository athttps://github.com/boriskiefer/sim_quantum_superposition.

## author declarations

Conflict of Interest

The author has no conflict to disclose.

## References
- [1]K. Krijtenburg-Lewerissa, H. J. Pol, and A. Brinkman.Insights into teaching quantum mechanics in secondary and lower
undergraduate education.Phys. Rev. Phys. Educ. Res., 13(1):010109, 2017.
- [2]C. Singh and E. Marshman.Review of student difficulties in upper-level quantum mechanics.Phys. Rev. Phys. Educ. Res., 11(2):020117, 2015.
- [3]E. Marshman and C. Singh.Framework for understanding the patterns of student difficulties in
quantum mechanics.Phys. Rev. Phys. Educ. Res., 11(2):020119, 2015.
- [4]T. Bouchee, L. de Putter-Smits, M. Thurlings, and B. Pepin.Towards a better understanding of conceptual difficulties in
introductory quantum physics courses.Stud. Sci. Educ., 58(2):183–202, 2022.
- [5]E. Marshman and C. Singh.Investigating and improving student understanding of quantum
mechanics in the context of single photon interference.Phys. Rev. Phys. Educ. Res., 13(1):010117, 2017.
- [6]G. Zhu and C. Singh.Improving students? understanding of quantum measurement. I.
investigation of difficulties.Phys. Rev. Phys. Educ. Res., 8(1), 2012.
- [7]G. Passante, P. J. Emigh, and P. S. Shaffer.Student ability to distinguish between superposition states and mixed
states in quantum mechanics.Phys. Rev. Phys. Educ. Res., 11(2):020135, 2015.
- [8]E. Marshman and C. Singh.Investigating and improving student understanding of the probability
distributions for measuring physical observables in quantum mechanics.Eur. J. Phys., 38(2):025705, 2017.
- [9]P. Hu, Y. Li, and C. Singh.Challenges in addressing student difficulties with quantum
measurement of two-state quantum systems using a multiple-choice question
sequence in online and in-person classes.Phys. Rev. Phys. Educ. Res., 19(2):020130, 2023.
- [10]K. Perkins, W. Adams, M. Dubson, N. Finkelstein, S. Reid, C. Wieman, and
R. LeMaster.PhET: Interactive simulations for teaching and learning physics.The Physics Teacher, 44(1):18–23, 2006.
- [11]A. Kohnle, C. Baily, A. Campbell, N. Korolkova, and M. J. Paetkau.Enhancing student learning of two-level quantum systems with
interactive simulations.Am. J. Phys., 83(6):560–566, 2015.
- [12]J. R. Johansson, P. D. Nation, and F. Nori.QuTiP: An open-source python framework for the dynamics of open
quantum systems.Comput. Phys. Commun., 183(8):1760–1772, 2012.
- [13]A. Javadi-Abhari, M. Treinish, K. Krsulich, C. J. Wood, J. Lishman, J. Gacon,
S. Martiel, P. D. Nation, L. S. Bishop, A. W. Cross, B. R. Johnson, and J. M.
Gambetta.Quantum computing with qiskit.arXiv preprint arXiv:2405.08810, 2024.
- [14]V. Borish and H. J. Lewandowski.Student reasoning about quantum mechanics while working with physical
experiments.Phys. Rev. Phys. Educ. Res., 20(2):020135, 2024.
- [15]E. Marshman, A. Maries, and C. Singh.Using multiple representations to improve student understanding of
quantum states.Phys. Rev. Phys. Educ. Res., 20(2):020152, 2024.
- [16]P. J. Emigh, G. Passante, and P. S. Shaffer.Student understanding of time dependence in quantum mechanics.Phys. Rev. Phys. Educ. Res., 11(2):020112, 2015.
- [17]C. Baily and N. D. Finkelstein.Teaching and understanding of quantum interpretations in modern
physics courses.Phys. Rev. Phys. Educ. Res., 6(1), 2010.
- [18]C. Baily and N. D. Finkelstein.Teaching quantum interpretations: Revisiting the goals and practices
of introductory quantum physics courses.Phys. Rev. Phys. Educ. Res., 11(2):020124, 2015.
- [19]A. Merzel, E. Y. Weissman, N. Katz, and I. Galili.Mathematical structures in quantum physics education for high school
students: Unveiling the power of dirac notation for conceptual and
problem-solving proficiency.Phys. Rev. Phys. Educ. Res., 20(2):020134, 2024.
- [20]M. A. Nielsen and I. L. Chuang.Quantum Computation and Quantum Information: 10th Anniversary
Edition.Cambridge University Press, 2011.
- [21]C. H. Crouch and E. Mazur.Peer instruction: Ten years of experience and results.Am. J. Phys., 69(9):970–977, 2001.

## Supplementary Material

## S1. Deployment modes summary

Three deployment modes are supported. In thefull50-minute mode, instructors use all five activities in sequence as described in the main text. In thecompressedmode, Activities 1–3 are completed in class and Activity 5 plus one concept-check item are assigned as homework, preserving the coherence/mixture distinction as the in-class centerpiece. In theflippedmode, Activities 1 and 2 are completed before class so that all class time can focus on Activity 3 and the statistics discussion in Activity 5. In all modes, the ordered-operations extension is assigned as an optional challenge outside class.

## S2.2×22\times 2unitary parameterization

For reference, the full matrix form of theU​3U3/ZYZ parameterization used in the simulator isU​(θ,ϕ,λ)=(cos⁡θ2−ei​λ​sin⁡θ2ei​ϕ​sin⁡θ2ei​(ϕ+λ)​cos⁡θ2),θ∈[0,π],ϕ,λ∈[0,2​π).U(\theta,\phi,\lambda)=\begin{pmatrix}\cos\dfrac{\theta}{2}&-e^{i\lambda}\sin\dfrac{\theta}{2}\\[6.0pt]
e^{i\phi}\sin\dfrac{\theta}{2}&e^{i(\phi+\lambda)}\cos\dfrac{\theta}{2}\end{pmatrix},\qquad\theta\in[0,\pi],\ \phi,\lambda\in[0,2\pi).

This is the standard Euler factorization of Nielsen and Chuang[20].

## S3. Optional extension: ordered operations

For instructors who want a short extension on non-commutativity, comparingH​σxH\sigma_{x}andσx​H\sigma_{x}Hprovides an accessible entry point:H​σx=12​(11−11),σx​H=12​(1−111).H\sigma_{x}=\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\
-1&1\end{pmatrix},\qquad\sigma_{x}H=\frac{1}{\sqrt{2}}\begin{pmatrix}1&-1\\
1&1\end{pmatrix}.

Applied to|+z⟩\ket{+z}, the two orderings produce orthogonal states. Since orthogonal states cannot differ by a global phase, the order is physically meaningful. This is sufficient to motivate the concept of non-commutativity without requiring the commutator formalism.

## S4. Standard error for binary outcomes

LetXi∈{0,1}X_{i}\in\{0,1\}denote theiith trial withℙ​(Xi=1)=p\mathbb{P}(X_{i}=1)=p, and letp^=N−1​∑iXi\hat{p}=N^{-1}\sum_{i}X_{i}. Independence andXi2=XiX_{i}^{2}=X_{i}giveVar​(p^)=p​(1−p)N,S​E​(p^)=p​(1−p)N.\mathrm{Var}(\hat{p})=\frac{p(1-p)}{N},\qquad SE(\hat{p})=\sqrt{\frac{p(1-p)}{N}}.

This is the uncertainty estimate used in Activity 5 and CC3/PP3.

## S5. Concept checks and pre/post prompts

CC1 (LG1).Two sources produce identical 50/50 outcomes in thezzbasis. Source A is the coherent state|ψ⟩=(|+z⟩+|−z⟩)/2\ket{\psi}=(\ket{+z}+\ket{-z})/\sqrt{2}. Source B is a 50/50 classical mixture of|+z⟩\ket{+z}and|−z⟩\ket{-z}. Are A and B physically equivalent? Justify your answer using an incompatible basis.

CC2 (LG2).Given|ψ⟩=cos⁡(θ2)​|+z⟩+ei​ϕ​sin⁡(θ2)​|−z⟩,\ket{\psi}=\cos\!\left(\frac{\theta}{2}\right)\ket{+z}+e^{i\phi}\sin\!\left(\frac{\theta}{2}\right)\ket{-z},

predictP​(+x)P(+x)andP​(−x)P(-x)and evaluate numerically for(θ,ϕ)=(π/3,π)(\theta,\phi)=(\pi/3,\pi).

CC3 (LG3).One simulator run reportsp^=0.62\hat{p}=0.62fromN=100N=100trials and another uses the same state and analyzer withN=1000N=1000. Compare the expected sampling uncertainty usingS​E​(p^)=p^​(1−p^)/NSE(\hat{p})=\sqrt{\hat{p}(1-\hat{p})/N}. Does changingNNchange the quantum state?

CC4 (LG4).ComputeH​σxH\sigma_{x}andσx​H\sigma_{x}H, apply both to|+z⟩\ket{+z}, and explain why orthogonality of the resulting states rules out global-phase equivalence.

CC5 (LG5).A student writes: “Since|ψ⟩=a​|+x⟩+b​|−x⟩\ket{\psi}=a\ket{+x}+b\ket{-x}, thereforeP​(+z)=|a|2P(+z)=|a|^{2}.” Identify the error and give a correct basis-aware method.

PP1 (LG1).Explain in 2–4 sentences why a coherent superposition and a classical mixture can agree in one basis but disagree in another.

PP2 (LG2).For an instructor-selected state, compute measurement probabilities in a specified basis and show the projection steps.

PP3 (LG3).Two runs use the same analyzer setting but differentNtrialN_{\text{trial}}. Explain why the observed frequencies differ and how the uncertainty scales withNtrialN_{\text{trial}}.

PP4 (LG4).Under what conditions do two ordered products of unitaries produce physically distinct analyzers? Illustrate with one example.

PP5 (LG5).Diagnose and correct a short notation inconsistency involving bras, kets, and probability extraction.

## S6. Answer key

CC1 / PP1.Full credit requires stating that a coherent superposition and a classical mixture can agree in one basis yet differ in an incompatible basis because the superposition retains phase coherence and the mixture does not.

CC2 / PP2.Using|±x⟩=2−1/2​(|+z⟩±|−z⟩)\ket{\pm x}=2^{-1/2}(\ket{+z}\pm\ket{-z}),P​(+x)=12​(1+sin⁡θ​cos⁡ϕ),P​(−x)=12​(1−sin⁡θ​cos⁡ϕ).P(+x)=\tfrac{1}{2}(1+\sin\theta\cos\phi),\qquad P(-x)=\tfrac{1}{2}(1-\sin\theta\cos\phi).

For(θ,ϕ)=(π/3,π)(\theta,\phi)=(\pi/3,\pi):P​(+x)≈0.067P(+x)\approx 0.067,P​(−x)≈0.933P(-x)\approx 0.933.

CC3 / PP3.Full credit requires recognizing that increasingNNreduces the standard error by the expected1/N1/\sqrt{N}scaling and does not change the prepared state or the theoretical probability.

CC4 / PP4.Full credit requires correct matrix products, correct identification of orthogonal resulting states, and the statement that orthogonal states cannot differ only by a global phase.

CC5 / PP5.Full credit requires identifying the basis mismatch (|ψ⟩\ket{\psi}is expressed in thexxbasis but the probability is claimed for azz-basis outcome) and either projecting directly with|⟨+z|ψ⟩|2|\braket{+z|\psi}|^{2}or first rewriting the state in thezzbasis.

## 


- 


Major funding support from
