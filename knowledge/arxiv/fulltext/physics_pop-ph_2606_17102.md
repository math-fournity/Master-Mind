# Quantum Cinema: An Interactive Cinematic Exploration of Quantum Computing Hardware via Generative World Models

**arXiv ID**: 2606.17102v3
**Authors**: Aoyu Zhang, Dongping Liu, Luyao Zhang
**Published**: 2026-06-14
**Categories**: physics.pop-ph, cs.AI, cs.ET, cs.HC, quant-ph
**HTML URL**: https://arxiv.org/html/2606.17102v3

## Abstract

Quantum computing promises transformative advances across science and industry, yet the physical hardware that enables these computations remains invisible to the public: quantum processors operate inside sealed dilution refrigerators at temperatures near absolute zero, making direct observation impossible. This "imagination gap" between quantum computing's growing societal impact and the public's ability to visualize it represents a significant barrier to quantum literacy and workforce development. We present Quantum Cinema, an open-source, browser-based interactive application that closes this gap by transforming invisible quantum hardware into explorable, cinematic experiences using generative world models. Quantum Cinema guides users through a four-act narrative -- from the foundational Nobel Prize-winning science of quantum entanglement, through curated video introductions to three major quantum computing architectures (trapped-ion, neutral-atom, and superconducting systems), into immersive three-dimensional generative worlds that make invisible quantum phenomena observable, and finally to interactive radar-chart comparisons grounded in real quantum device specifications. All three-dimensional environments are generated using WorldLabs' generative world model platform and are scientifically grounded in curated metrics from Amazon Web Services (AWS) Braket quantum hardware. Quantum Cinema requires no installation, no specialized hardware, and no quantum computing background. It is designed to serve two distinct communities: scholars and developers seeking to replicate or extend the platform, and educators, researchers, and science communicators seeking an intuitive tool for explaining quantum hardware to diverse audiences. This paper describes the system architecture, the generative world model pipeline, use cases for both communities, and directions for future work.

## Full Text

Quantum Cinema: An Interactive Cinematic Exploration of Quantum Computing Hardware via Generative World Models.

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2606.17102v3 [physics.pop-ph] 02 Aug 2026

## Quantum Cinema: An Interactive Cinematic Exploration of Quantum Computing Hardware via Generative World Models.Aoyu Zhang†Dongping Liu†‡Luyao Zhang†*†Authors are listed in alphabetical order by first name.*Corresponding author: Luyao Zhang (lz183@duke.edu), Digital Innovation Research Center and Social Science Division, Duke Kunshan University. Address: Duke Avenue No.8, Kunshan, Suzhou, Jiangsu, China, 215316.‡Work done while at Amazon Web Services. Dongping Liu is currently with Tenorshare, Hong Kong, China.

## Abstract

Quantum computing promises transformative advances across science and industry, yet the physical hardware that enables these computations remains invisible to the public: quantum processors operate within inaccessible laboratory infrastructure—ranging from dilution refrigerators to ultra-high-vacuum ion traps and optically controlled neutral-atom chambers—making direct observation difficult.. This “imagination gap” between quantum computing’s growing societal impact and the public’s ability to visualize it represents a significant barrier to quantum literacy and workforce development. We presentQuantum Cinema, an open-source, browser-based interactive application that closes this gap by transforming invisible quantum hardware into explorable, cinematic experiences using generative world models. Quantum Cinema guides users through a four-act narrative—from the 2025 Nobel Prize in Physics as a contemporary
quantum-hardware anchor, with the 2022 Nobel Prize-winning science of entanglement situated within the broader historical timeline, through curated video introductions to three major quantum computing architectures (trapped-ion, neutral-atom, and superconducting systems), into immersive three-dimensional generative worlds that make invisible quantum phenomena observable, and finally to interactive radar-chart comparisons grounded in real quantum device specifications. All three-dimensional environments are generated using World Labs’ generative world model platform and are scientifically grounded in curated metrics from Amazon Web Services (AWS) Braket quantum hardware. Quantum Cinema requires no installation, no specialized hardware, and no quantum computing background. It is designed to serve two distinct communities: scholars and developers seeking to replicate or extend the platform, and educators, researchers, and science communicators seeking an intuitive tool for explaining quantum hardware to diverse audiences. This paper describes the system architecture, the generative world model pipeline, use cases for both communities, and directions for future work.◆\blacklozenge[-1pt]Ion[-2pt]Trap⊳\triangleright1⊳\triangleright2⊳\triangleright3⊳\triangleright4⊳\triangleright5∘\circ[-1pt]Neutral[-2pt]Atom⊳\triangleright1⊳\triangleright2⊳\triangleright3⊳\triangleright4⊳\triangleright5■\blacksquare[-1pt]JJ[-2pt]Chip⊳\triangleright1⊳\triangleright2⊳\triangleright3⊳\triangleright4⊳\triangleright5Figure 1:The three generative world models ofQuantum Cinema, each showing five navigable views.Top:trapped-ion (teal)—ytterbium ions in a Paul trap.Middle:neutral-atom (orange)—rubidium array via optical tweezers.Bottom:superconducting (violet)—Josephson-junction chip in a dilution refrigerator.

## IIntroduction

Quantum computing stands poised to transform science, industry, and society. From drug discovery and materials science to cryptography and financial modeling, the potential applications of quantum computational advantage span nearly every sector of the global economy[6]. Yet there exists a profoundimagination gap: while thesoftwarelayer of quantum computing—quantum circuits, algorithms, and gates—has become increasingly accessible through educational tools and cloud platforms, thehardwareitself remains fundamentally invisible to the vast majority of researchers, students, and the public. quantum processors operate within inaccessible laboratory infrastructure—ranging from dilution refrigerators to ultra-high-vacuum ion traps and optically controlled neutral-atom chambers—making direct observation difficult. The physical reality of quantum computing hardware—the golden coaxial cables, the superconductingquantum bits(qubits) etched onto silicon chips, the layered cryogenic stages descending toward absolute zero—has remained locked behind laboratory walls and abstracted away into circuit diagrams and mathematical notation.

The scientific significance of quantum technologies has
received the highest levels of international recognition.
The 2025 Nobel Prize in Physics, awarded to John Clarke,
Michel H. Devoret, and John M. Martinis for macroscopic
quantum mechanical tunnelling and energy quantisation in
an electric circuit, provides the contemporary hardware
anchor for Quantum Cinema[38]. The experience situates this
milestone within the longer history of quantum
information science, including the 2022 Nobel Prize in
Physics awarded to Alain Aspect, John Clauser, and Anton
Zeilinger for foundational experiments on quantum
entanglement and Bell inequalities[36]. Together, these awards connect
the physical foundations of quantum hardware with the
entanglement principles that motivate quantum
computation and communication.

The intersection of artificial intelligence (AI) and quantum science represents one of the most promising frontiers in modern research. The 2024 Nobel Prize in Physics, awarded to John Hopfield and Geoffrey Hinton for foundational discoveries in neural networks and machine learning[37], underscored the transformative role of AI in scientific discovery. Parallel advances in quantum machine learning (QML) — the use of quantum computers to enhance machine learning algorithms and vice versa — have demonstrated potential advantages in areas ranging from molecular simulation to optimization[6]. However, the inaccessibility of quantum hardware remains a bottleneck: even as AI techniques increasingly support the quantum-computing stack and the representation and characterization of quantum systems[1,13], the physical reality of quantum processors remains hidden from the researchers, educators, and students who most need to understand them. This paper bridges that gap by applying generative world models — a technology at the forefront of AI research[41]— to the specific scientific challenge of quantum hardware visualization.

For researchers outside quantum physics—including the artificial intelligence (AI) and computer science communities that this venue serves—this invisibility creates a significant barrier to engagement. Terms such assuperconducting qubit,Josephson junction,cryogenic stage, andquantum control electronicsremain opaque without a tangible mental model. The physical architecture of a quantum computer, from room-temperature control electronics to the mixing chamber plate at the base of the dilution refrigerator, follows a spatial logic that is difficult to convey through text or two-dimensional diagrams alone. Current visualization approaches fall into two categories, each with significant limitations. Circuit-level simulators such as Quirk[14]and the IBM Quantum Experience[16]provide excellent interactive environments for learning quantum logic gates and circuit construction, but they operate entirely at the abstract level of quantum information—the physical hardware that executes these circuits remains unseen. On the other end of the spectrum, immersive
virtual-reality (VR) approaches—such as the
Bloch-sphere environment studied by Zable et
al.[43]—have demonstrated the
pedagogical potential of spatial immersion, but require
specialized headsets and additional setup. By contrast,
QuantumEyes is a two-dimensional interactive
visualization that maps multi-qubit states to a radial
“dandelion” chart[32], while the
Quantum Flytrap Virtual Lab is a browser-based simulator
for optical quantum circuits[26].
These systems improve access to quantum-state and circuit
abstractions, but do not render physical
quantum-computing hardware as an explorable spatial
environment. Broader reviews likewise identify both the
educational potential of interactive quantum tools and
the accessibility and scalability constraints associated
with headset-based immersive systems[34,35].

We presentQuantum Cinema, the first interactive cinematic platform that leveragesgenerative world modelsto make quantum computing accessible through immersive three-dimensional (3D) narrative environments. Generative world models—AI systems that synthesize interactive, navigable 3D scenes from visual data or semantic descriptions—have emerged as a transformative technology for visual storytelling and education. These models, exemplified by systems capable of generating photorealistic, physically consistent environments from image inputs[42]and from language or image prompts[41], enable a fundamentally new approach to scientific communication: rather than manually constructing 3D assets through traditional computer graphics pipelines, we can generate explorable worlds that are both visually compelling and scientifically informative. The application of generative AI to scientific visualization has been recognized as a frontier with vast untapped potential[5].Quantum Cinemaharnesses this capability to create the first interactive cinematic journey through the landscape of quantum computing—weaving together Nobel Prize-winning science, generative world-model architectures, immersive exploration, and quantitative comparison into a unified four-act narrative.

The experience is structured as afour-act narrative. Act I presents an interactive timeline of Nobel Prize laureates in quantum science, enabling viewers to explore the foundational discoveries that shaped the field. Act II showcases generative video worlds for each major quantum computing architecture—superconducting circuits, trapped ions, and neutral atoms—demonstrating how world models can visualize hardware-specific physics. Act III offers an immersive 3D environment generated fromWorld Labstechnology, allowing viewers to freely explore a navigable quantum world. Act IV provides a quantitative comparison across architectures through interactive radar charts, supporting evidence-based understanding of trade-offs. This narrative architecture organizes fragmented
knowledge into a coherent pedagogical journey designed
to support conceptual understanding alongside visual
appreciation.The four-act structure is described in detail in SectionIII.

This work makes two contributions tailored to the dual
audience of the paper. First, at the methodological
level, we position generative world models as a
scientific-visualization medium between manually
authored artistic 3D content and equation-based physical
simulation. We provide a reproducible pipeline that
connects scientific literature and device documentation,
structured prompt engineering, generative world
synthesis, human curation, and browser-based integration.
The resulting worlds are scientifically informed
explanatory environments, rather than validated physical
simulations.

Second, at the practical level, we provide an open-source,
zero-install browser application and a reusable
development workflow for educators, science
communicators, quantum-computing practitioners, and
world-model researchers. The platform offers a concrete
test case for future parameter-conditioned,
time-resolved, and scientifically evaluated generative
environments. This paper reports the system design,
implementation, and qualitative demonstration; it does
not yet evaluate learning outcomes through a controlled
user study.

Data and Code Availability: Quantum Cinema is released under the MIT License. The complete source code, documentation, and generative world templates are available on GitHub111https://github.com/QuantBlockchain/quantum-cinema. A permanent archived version (v1.0.0) has been deposited on Zenodo[30]. The repository includes installation instructions, the full AWS deployment configuration, bilingual documentation, teaching guides for all three architectures, and templates for extending the platform to additional quantum hardware modalities. No proprietary datasets are required: all device parameters are sourced from published manufacturer specifications and the AWS Braket service documentation.

The remainder of this paper is organized as follows. SectionIIsurveys related work in quantum visualization, generative world models, and AI-driven scientific communication. SectionIIIdetails the Quantum Cinema architecture and four-act narrative design. SectionVIconcludes with limitations and future directions.

## IIRelated WorkTABLE I:Comparison of Quantum Education and Visualization PlatformsToolVenue∞\inftyCircuit■\blacksquareHardware↺\circlearrowleftInteract.𝐖\mathbf{W}Web★\bigstarGenAI⊳\trianglerightNo InstallQuirk[14]Web’16⚫❍⚫⚫❍⚫IBM Q Exp.[16]IBM’24⚫❍⚫⚫❍⚫QuantumEyes[32]TVCG’23⚫❍⚫❍❍❍VENUS[33]EuroVis’23⚫❍⚫❍❍❍QNotation[28]QCE’24⚫❍⚫⚫❍⚫QWalkVis[18]QCE’23⚫❍⚫⚫❍⚫Virtual Lab[26]SPIE’22⚫❍⚫⚫❍⚫Intuit[19]CHI’25◗❍⚫❍❍❍VR Quantum[43]VRST’20◗❍⚫❍❍❍Black Opal[29]2024⚫❍⚫⚫❍⚫Quantum Cinema2025⚫⚫⚫⚫⚫⚫

Legend.⚫= full support;◗= partial support;❍= not supported.
Categories:∞\inftyCircuit– visualization of quantum circuit diagrams and gate-level operations;■\blacksquareHardware– rendering of physical quantum processor architectures as spatial environments;↺\circlearrowleftInteractive– user manipulation and real-time feedback;𝐖\mathbf{W}Web– browser-based delivery without native application installation;★\bigstarGenAI– use of generative artificial intelligence (world models, neural rendering) for content creation;⊳\trianglerightNo Install– immediate accessibility without setup, registration, or specialized hardware. Quantum Cinema is the first platform to offer all six capabilities simultaneously.

We positionQuantum Cinemaat the intersection of four active research areas: quantum computing visualization, immersive quantum education, generative artificial intelligence (AI) for scientific visualization, and AI for quantum science. In what follows, we review the most relevant prior work in each area and identify the key gaps our system addresses.

## II-AQuantum Computing Visualization Tools

The earliest and most widely adopted tools for quantum computing education operate at thecircuit level, enabling users to construct and simulate quantum circuits through graphical interfaces. Quirk, developed by Gidney at Google, remains the most popular browser-based quantum circuit simulator, offering drag-and-drop construction, real-time state-vector simulation, and support for up to 16 qubits entirely within the browser[14]. Its accessibility and zero-installation model have made it a staple in undergraduate quantum computing courses. Similarly, the IBM Quantum Experience provides a cloud-based platform with a visual circuit composer, allowing users to execute quantum programs on real superconducting quantum processors[16]. While powerful, these platforms present quantum computation primarily through abstract circuit diagrams, leaving the underlying physical hardware opaque to the learner.

Recent research has introduced novel visual encodings to improve circuit interpretability. Ruan et al. proposed QuantumEyes, an interactive visualization system centered on a “dandelion chart” that maps multi-qubit states to radial visual patterns; their design was validated through 12 expert interviews[32]. In subsequent work, the same authors introduced VENUS, a two-dimensional (2D) geometrical representation of quantum states that generalizes the conventional Bloch sphere to multi-qubit systems[33]. Complementary efforts have focused on pedagogical notation: Norrie et al. developed QNotation, a visual notation translator that bridges formal Dirac notation with intuitive graphical representations for novice learners[28]. For domain-specific education, Jordon et al. created QWalkVis, an interactive visualization tool for quantum walks designed to teach stochastic quantum processes[18]. In the optical domain, Quantum Flytrap’s Virtual Lab offers a no-code, drag-and-drop simulator for optical quantum circuits supporting up to three entangled photons[26].

Despite these advances,allexisting circuit-level tools share a common limitation: they visualize quantum computation through abstract symbolic representations rather than rendering the physical hardware itself as an explorable spatial environment.

## II-BImmersive and Interactive Quantum Education

A growing body of work has explored immersive technologies to improve quantum concept comprehension. Zable and Velloso conducted the first controlled study comparing virtual reality (VR) and desktop interfaces for quantum education, using Bloch sphere tutorials to demonstrate that VR can significantly improve spatial understanding of single-qubit states[43]. More recently, Karunathilaka et al. presented Intuit at ACM CHI 2025, an augmented reality (AR) system that explains quantum concepts through everyday analogies projected into the user’s physical environment[19]. Quantum Flytrap’s Virtual Lab also contributes in this space by providing web-based interactive quantum simulation accessible without specialized hardware[26]. Song et al. conducted a systematic review of extended reality (XR) in quantum education, finding that while immersive modalities show promise for conceptual learning, adoption remains limited by hardware cost, setup complexity, and scalability concerns[35].

These findings reveal a critical tension: VR and AR approaches require specialized headsets or equipment that limit accessibility, while fully web-based immersive experiences—which could reach the broadest audience—remain underexplored in quantum education.

## II-CGenerative AI for Scientific Visualization

Generative world models represent a paradigm shift in how complex environments can be synthesized from natural language or structural descriptions. In scientific visualization, this capability enables the automatic generation of explorable three-dimensional (3D) scenes from high-level specifications. Xie et al. introduced PhysGaussian at CVPR 2024, integrating physics simulation with 3D Gaussian splatting to produce dynamic, physically grounded environments; the work has since accumulated over 470 citations[42], underscoring the community’s interest in generative 3D content. Basole and Major proposed a comprehensive framework for integrating generative AI into scientific visualization pipelines, identifying data-to-scene translation as a key challenge[5]. In industry, World Labs’ Marble platform—founded by Fei-Fei Li—demonstrates that generative 3D world models can produce consistent, navigable environments from single images or text prompts[41]. Concurrently, a comprehensive survey by Zhu et al. examined whether video diffusion models such as Sora can function as world simulators, concluding that while limitations remain, these models exhibit emerging capabilities for physical reasoning and environment generation[44].

To our knowledge, generative world models have not yet been applied to quantum hardware visualization, leaving a significant opportunity unexplored.

## II-DAI for Quantum Science

The convergence of AI and quantum science has emerged as a major research direction with applications spanning simulation, optimization, and discovery. Biamonte et al. provided a comprehensive survey of quantum machine learning (QML), establishing the theoretical foundations and identifying near-term opportunities on noisy intermediate-scale quantum (NISQ) devices[6]. On the algorithmic front, variational quantum eigensolvers (VQE) and the quantum approximate optimization algorithm (QAOA) have become flagship approaches for applying quantum computers to real-world problems in chemistry and combinatorial optimization[10]. Complementing these algorithmic advances, Carleo and Troyer demonstrated that neural networks can represent quantum many-body states with remarkable accuracy, introducing the paradigm of neural quantum states for simulating quantum systems that would be intractable for classical methods[9].

While these approaches use AI toadvancequantum science, few works use AI tomake quantum science accessibleto broader audiences. Quantum Cinema occupies this unique position at the intersection of AI-driven visualization and quantum education, applying generative world models to bridge the accessibility gap identified across all three research areas above.

While much of the existing literature uses AI to advance quantum-system design, simulation, characterization, and computation, complementary systems in this broader research program explore public-facing and programming-oriented
interfaces to quantum science. QSignAI combines AI-mediated interaction with quantum-randomness-seeded identity
signatures[21]; Quantum Futures Interactive integrates quantum-risk education, participatory technology prioritization, and infrastructure
tradeoff exploration[23]; and Quantum Circuit Vision evaluates visual AI agents for quantum code generation under explicit cost constraints[22]. Quantum Cinema occupies a distinct position within this landscape by applying generative world models specifically to the physical hardware layer of quantum computing, transforming otherwise inaccessible architectures into browser-based, explorable environments for broad audiences.

TableIsummarizes the capabilities of existing tools across eight key dimensions. No prior system simultaneously supports circuit-level accuracy, hardware environment visualization, full interactivity, web-based delivery, generative AI content creation, AI-for-quantum-science framing, and no-code accessibility. To address these gaps, we presentQuantum Cinema, a unified platform that combines generative world models with quantum circuit simulation to produce interactive cinematic walkthroughs of quantum computing hardware, accessible from any modern web browser without installation or specialized equipment.

## IIISystem Design and Architecture

This section presents the end-to-end architecture ofQuantum Cinema, an interactive web application that combines generative world models with cinematic storytelling to explain quantum computing hardware. We describe the cloud deployment stack (SectionIII-A), the four-act narrative structure that guides users through the experience (SectionIII-B), and the three quantum architectures featured in the system (SectionIII-C). Detailed walkthroughs of each act, including annotated screenshots, are provided in AppendixB.

## III-ASystem Architecture

Quantum Cinemais built as a single-page application (SPA) using Next.js 16 with React 19, authored entirely in TypeScript[40,25]. This stack provides server-side rendering, automatic code splitting, and a component-based architecture that supports both cinematic scroll-driven animations and interactive 3D world embedding within a unified codebase.

The application is deployed on Amazon Web Services (AWS)[2]following a three-tier cloud architecture optimized for global content delivery and automatic scaling. As illustrated in Fig.2, user requests first reach an AWS CloudFront Content Delivery Network (CDN) edge location, which serves cached static assets and forwards dynamic requests to an Application Load Balancer (ALB). The ALB distributes traffic across tasks running in AWS Elastic Container Service (ECS) Fargate, a serverless compute engine that eliminates the need to manage underlying virtual machine infrastructure.UCLAWUserBrowserCloudFrontCDNALBECS FargateNext.js 16 SPAWorld Labsmarble.wlabs.aiStatic Assets:Videos + ImagesHTTPSsecretport 3000iframe3D streamNo Database⋅\cdotNo Live QPU⋅\cdotStatic-FirstMissing secret→\rightarrow403 ForbiddenFigure 2:System Architecture of Quantum Cinema. The static-first design requires no database and places no live quantum processing unit (QPU) in the request path. All content is baked into the container at build time; 3D worlds stream from World Labs via public URL embedding. Requests without the shared CDN secret header are rejected at the edge.

Each container runs the Next.js standalone build on Node.js 20 Alpine Linux with a non-root user for security hardening. The service auto-scales between one and four tasks based on 70 % CPU utilization, with circuit-breaker rollback to maintain availability during deployment updates. All static assets—including pre-rendered videos, Nobel laureate photographs, and architecture diagrams—are baked directly into the container image at build time. Thisstatic-firstdesign eliminates runtime dependencies on object storage, databases, or live quantum cloud services.

The immersive 3D environments stream from World Labs[41]via public Universal Resource Locator (URL) embeddings, allowing generative world content to render directly from the provider’s infrastructure without intermediate processing. TableIIsummarizes the deployment parameters.TABLE II:System Specifications of Quantum CinemaLayerComponentTechnology⟨⟩\langle\rangle[-2pt]FrontendWeb FrameworkNext.js 16 / React 19LanguageTypeScript★\bigstar[-2pt]CloudCDNCloudFrontLoad BalancerALBComputeECS Fargate (1–4 tasks, 70% CPU)□\square[-2pt]RuntimeContainerNode.js 20 Alpine (non-root)3D PlatformWorld Labs (marble.worldlabs.ai)∅\varnothing[-2pt]UniqueDatabaseNone(static-by-design)QPU in PathNone(no live quantum hardware)

Note.The static-first architecture eliminates all runtime dependencies on databases, quantum processing units (QPUs), and external APIs. All content is baked into the container image at build time. Icons denote architectural layers:⟨⟩\langle\rangleFrontend,★\bigstarCloud,□\squareRuntime,∅\varnothingUnique (none by design).

## III-BFour-Act Narrative Design

The user experience follows a four-act narrative that mirrors cinematic storytelling conventions while progressively building technical understanding. Each act occupies a distinct section of the scroll-driven SPA, with smooth transitions and consistent visual theming. Fig.3depicts the overall flow, and TableIIIprovides the structural breakdown. AppendixBpresents a detailed walkthrough of each act, including annotated screenshots and pedagogical rationale.1Nobel Prize⊙\odot2025 Laureate profilesThe Quantum TimelineContextWhy2World Models◆\blacklozengeIon trap∘\circAtom■\blacksquareSuperconductingVideo introductionsConceptsWhat3Explore★\bigstarGenerative 3D worldsWorld Labs immersionNavigate + discoverExperienceHow4Compare⋈\bowtieRadar charts6-metric paradigm-aware comparisonUse-case matchingDecide(a) Historical context→\rightarrow(b) Physical concepts→\rightarrow(c) Immersive exploration→\rightarrow(d) Informed selectionFigure 3:The Four-Act Narrative Flow of Quantum Cinema. Each act is numbered, color-coded, and annotated with its pedagogical role and key content. Arrows are labeled with the cognitive transition they enable.TABLE III:The Four-Act Narrative Structure of Quantum CinemaActNamePurposeComponentKey Content1⊙\odotNobel PrizeEstablish why quantum mattersNobelPrizeStep2025 Nobel Prize in Physics with interactive history timeline of quantum research2◆\blacklozengeWorld ModelsIntroduce architecturesVideoShowcaseStepCurated videos per architecture: ion trap, neutral atom, superconducting3★\bigstarExploreImmersive 3D experienceWorldModelStepGenerative world (World Labs): navigable 3D environment with scientific annotations4⋈\bowtieCompareHardware comparisonComparisonStepRadar charts grouped by paradigm
(6 metrics: coherence, 2-qubit fidelity, readout fidelity,
error rate, connectivity, and qubit count)
+ use-case matching

Note.Each act is color-coded and icon-tagged to match Figure3. The narrative follows a “why→\rightarrowwhat→\rightarrowhow→\rightarrowwhich” cognitive progression: Act I motivates through the 2025 Nobel Prize and historical context, Act II introduces physical concepts through video, Act III enables embodied learning through immersive 3D exploration, and Act IV supports decision-making through quantitative comparison. The Component column names the React component implementing each act in the source code.

Act I—Nobel Prize(SectionB-A) establisheswhyquantum computing matters. Users encounter an interactive horizontal timeline centered on the 2025 Nobel Prize in Physics, with historical context connecting the laureates’ contributions to the broader arc of quantum research. This creates an emotional and historical anchor for the technical content that follows.

Act II—World Models(SectionB-B) introduces the three quantum hardware architectures through curated video content. Users scroll through vertically stacked architecture cards, each containing a short looping video and a concise description of the underlying physical mechanism. At the conclusion of this act, users select one architecture to explore in depth—a choice that parameterizes the remainder of the experience.

Act III—Explore(SectionB-C) constitutes the immersive centerpiece. Upon selecting an architecture, the user enters a generative three-dimensional (3D) world representing that quantum hardware platform. These environments are AI-generated interactive scenes from World Labs[41], not physics-based simulations. However, each world is grounded in real device parameters—cryostat geometry, vacuum chamber dimensions, laser cooling apparatus—to ensure visual fidelity and educational value. Users can orbit, zoom, and pan within the scene while annotated hotspots explain individual hardware components. Representative views of all three 3D worlds are shown in Figure1of the main text.

Act IV—Compare(SectionB-D) provides an interactive
comparison across quantum architectures, grouped by computational
paradigm. Users view animated radar charts across six quantitative
metrics: coherence time, two-qubit gate fidelity, readout fidelity,
error rate, connectivity topology, and qubit count. Gate-based
devices—trapped-ion and superconducting processors—are compared
directly, whereas the neutral-atom analog Hamiltonian-simulation
device is presented separately using platform-native sequence-level
and per-atom equivalents. This grouping avoids placing gate-model
and analog hardware on a single misleading yardstick while
transforming the qualitative impressions gathered during exploration
into technically grounded comparison.

## III-CThree Quantum Computing Architectures

Quantum Cinemafeatures three leading quantum computing architectures, chosen to represent distinct physical qubit implementations with contrasting engineering trade-offs. TableIVpresents the comparative overview, and the generative world models for each are shown in Figure1. The device-level metrics reported below are representative,
dated snapshots curated from Amazon Braket device
documentation and official specifications for IonQ Aria,
Rigetti Ankaa-3, and QuEra Aquila[3,17,31,4].
Architecture-level interpretation is grounded in peer-reviewed
studies of trapped-ion, neutral-atom, and superconducting
platforms[8,7,20].
The frozen values used by the paper and application are
maintained inquantum-cinema/src/lib/data.ts.TABLE IV:Comparison of Quantum Computing Architectures and Computational Models in Quantum CinemaComputational modelGate-Based Quantum ProcessorsAnalog Hamiltonian Simulation (AHS)Physical architecture◆\blacklozengeTrapped-Ion■\blacksquareSuperconducting∘\circNeutral AtomsRepresentative deviceIonQ AriaRigetti Ankaa-3QuEra AquilaExecution mechanismDiscrete quantum gates and circuitsDiscrete quantum gates and circuitsContinuous programmable Hamiltonian evolutionCoherence / evolution time1–10 s20–100μ\mus1–10μ\musa2-Qubit / sequence fidelity99.5%99.0%97–99%bReadout fidelity∼\sim99.7%∼\sim97–99%∼\sim99% per atomError rate∼\sim0.5%∼\sim1%∼\sim1–3%ConnectivityAll-to-allNearest-neighborProgrammable geometryPhysical qubits / atoms2584256Operating temperatureRoom temperature (vacuum)10–15 mKRoom temperature (vacuum)Key visualized phenomenonLinear ion chain with Raman-laser addressingJosephson-junction chip in a dilution refrigeratorProgrammable atom array controlled by optical tweezers

Note.The table distinguishes thephysical architectureof
each platform from itscomputational model. IonQ Aria
and Rigetti Ankaa-3 are gate-based quantum processors that
execute discrete quantum circuits. QuEra Aquila is a
neutral-atom quantum processor implementing analog
Hamiltonian simulation through continuous programmable
quantum evolution. The computational-model labels apply to
the representative devices shown here; neutral-atom technology
as a broader hardware family is not necessarily restricted to
analog Hamiltonian simulation.

Note.Values are representative, dated device snapshots rather than
live calibration measurements. IonQ Aria values are curated
from Amazon Braket and IonQ specifications[3,17]; Rigetti Ankaa-3 values are
curated from Amazon Braket and Rigetti specifications[3,31]; and QuEra Aquila values are
curated from Amazon Braket and QuEra documentation[3,4]. Architecture-level context is
drawn from peer-reviewed studies of trapped-ion,
neutral-atom, and superconducting platforms[8,7,20].

For QuEra Aquila, the reported microsecond value denotes a
platform-native analog-Hamiltonian-simulation evolution or
sequence window rather than a gate-modelT2T_{2}measurement.
Because Aquila does not expose discrete two-qubit gates, its
reported fidelity is a platform-native sequence-level
equivalent and is not directly interchangeable with
two-qubit gate fidelity on gate-based devices.

The frozen device snapshot used throughout the paper and
application is maintained inquantum-cinema/src/lib/data.ts. The frozen device snapshot used by the paper and
application is maintained inquantum-cinema/src/lib/data.ts. It supplies the
raw values reported in Table IV and used by the
architecture-comparison interface. No cell is designated as universally
“best,” because suitability depends on the computational
model, target workload, and dashboard scoring convention.

The visual encodings are used consistently throughout the
paper:◆\blacklozengetrapped-ion,■\blacksquaresuperconducting, and∘\circneutral-atom.

Trapped-Ionquantum computers suspend charged atoms (ions) in electromagnetic fields within an ultra-high vacuum chamber[8]. Lasers tuned to specific wavelengths manipulate individual ions to perform quantum gate operations. Because all ions share a common trapping potential, trapped-ion systems offer native all-to-all connectivity and exhibit long coherence times, often exceeding one second[17].

Neutral Atomsystems use focused laser beams, or optical
tweezers, to arrange atoms in programmable
two-dimensional arrays[7,4].
By exciting atoms to Rydberg states, engineers create
controllable many-body interactions. In QuEra Aquila,
these interactions implement analog Hamiltonian
simulation through continuous programmable evolution,
rather than a sequence of discrete two-qubit gates.

Superconductingquantum processors fabricate electrical circuits containing Josephson junctions and cool them to millikelvin temperatures inside dilution refrigerators[20]. Microwave pulses manipulate the quantum state of each circuit element. Within the three-device snapshot used in Quantum Cinema,
QuEra Aquila has the largest addressable register, with
256 programmable atoms. Rigetti Ankaa-3 represents the
superconducting gate-based architecture, offering fast gate
operations and mature fabrication while requiring
millikelvin cryogenic infrastructure and exhibiting
substantially shorter coherence times than trapped-ion
systems[31,20].

## IVGenerative World Model Pipeline

This section describes the pipeline for creating the 3D immersive environments that form the experiential core of Quantum Cinema. We detail the five-step world creation methodology, discuss the scientific accuracy of generative visualizations, and explain how developers can extend the platform with new quantum architectures.

## IV-AWorld Creation Methodology

Each 3D world in Quantum Cinema is created through a five-step pipeline that transforms scientific specifications into navigable, photorealistic environments. The pipeline bridges quantum hardware documentation and generative 3D scene synthesis, enabling rapid prototyping of educational environments without manual 3D modeling.⊙\odotConceptLiterature review1⟨⟩\langle\ranglePromptStructured text2★\bigstarGenerateWorld Labs AI3✓\checkmarkRefineHuman curation4⊳\trianglerightIntegrateReact embed5extractsubmitrenderapproveiteratePublic URL→\rightarrowiframeFigure 4:The five-stage generative world model pipeline in Quantum Cinema. Each architecture’s immersive 3D environment progresses from scientific literature review (Step 1) through structured prompt engineering (Step 2), AI synthesis via World Labs[41](Step 3), human curation with iterative refinement (Step 4), and frontend integration (Step 5). The feedback loop between Steps 3 and 4 ensures scientific accuracy before publication.

Step 1 – Scientific Concept Extraction.For each quantum architecture, we identify key physical phenomena and structural details from peer-reviewed literature and Amazon Web Services (AWS) Braket device specifications[3]. For example, the trapped-ion world is grounded in the physical description of alinear chain of ytterbium ionsconfined in aPaul trap(an oscillating electromagnetic field configuration that confines charged particles) and addressed byRaman laser beams(lasers tuned to induce stimulated Raman transitions between atomic energy levels, enabling qubit operations). Similarly, the superconducting world captures the visual character of dilution refrigerators housing quantum processors built fromJosephson junctions(superconducting devices consisting of two superconducting electrodes separated by a thin insulating barrier, serving as the fundamental qubit element).

Step 2 – Prompt Engineering.We craft detailed text prompts that balance scientific accuracy with visual storytelling. Each prompt incorporates three elements: (1) the physical layout of the hardware (e.g., chandelier structure of a superconducting processor, hexagonal lattice of neutral atoms), (2) salient visual features that distinguish the architecture (e.g., gold-plated coaxial lines, vacuum chamber windows), and (3) reference device photographs from published hardware teardowns and manufacturer documentation to ensure structural fidelity. The prompt for the trapped-ion world, for instance, specifies “a linear chain of ytterbium ions suspended in a vacuum chamber, illuminated by intersecting Raman laser beams, with gold-plated electrodes of a Paul trap visible along the axis.”

Step 3 – Generative World Synthesis.The engineered prompts are submitted to the World Labs Marble platform[41], a generative 3D world creation system that produces persistent, navigable environments from text and image inputs. The resulting environments are fully explorable via keyboard and mouse, with spatial audio and dynamic lighting, creating an embodied sense of presence within quantum hardware facilities.

Step 4 – Curated Refinement.Generated worlds are iteratively refined using the World Labs Chisel editor, an interactive curation tool that allows authors to adjust camera angles, lighting conditions, material properties, and spatial composition. This step ensures that the environments accurately reflect hardware topology – for example, verifying that the superconducting world conveys the vertical “chandelier” hierarchy of control electronics above the cryostat, or that the neutral-atom world correctly depicts the two-dimensional array of traps created byoptical tweezers(focused laser beams that trap and manipulate individual atoms) and the spatial patterns induced by theRydberg blockade(a phenomenon where excitation of one atom to a Rydberg state shifts the energy levels of nearby atoms, preventing simultaneous excitation within a critical radius).

Step 5 – Integration.The refined world is exported as a public URL via the World Labs viewer and embedded directly into the React frontend component. The viewer handles all rendering, navigation, and event propagation, requiring only a single iframe or WebView integration point. This architecture decouples world creation from application development, allowing pedagogical content to be authored independently of the 3D pipeline.

## IV-BScientific Accuracy of Generative Worlds

It is essential to emphasize that the 3D worlds in Quantum Cinema aregenerative visualizations– AI-generated scenes informed by quantum-hardware
documentation and curated device parameters, not exact physical simulations. They make otherwise invisible quantum phenomena (decoherence, laser cooling, energy loss during gate operations) observable as visual narrative, but should not be interpreted as precise physical models. Their intended pedagogical value lies in supporting more
concrete explanatory models of hardware structure and
operating principles, rather than in providing
computational fidelity to quantum-mechanical equations.

To maintain a meaningful connection to real hardware, we
curate six device metrics from Amazon Braket documentation
and official manufacturer specifications[3,17,31,4]:
coherence or platform-native evolution time, two-qubit or
sequence-level fidelity, readout fidelity, error rate,
connectivity topology, and physical qubit or atom count.

For gate-based devices, these quantities correspond to
standard calibration metrics. For QuEra Aquila, an analog
Hamiltonian-simulation device, the temporal and fidelity
axes use explicitly labelled platform-native equivalents
rather than a gate-modelT2T_{2}measurement or a discrete
two-qubit-gate fidelity. These metrics anchor the
architecture comparison in quantitative device
characteristics while avoiding a misleading direct
equivalence between gate-based and analog platforms.

The frozen raw values used by the paper and application
are maintained inquantum-cinema/src/lib/data.ts.TABLE V:Generative World Model Concepts by ArchitectureArchitectureScientific ConceptKey Visual Elements in Generated World◆\blacklozengeTrapped-Ion(IonQ)Linear chain of Yb+ions confined in a Paul trap, addressed by intersecting Raman laser beams for quantum gate operationsGlowing blue-white ytterbium ions in perfect equilibrium; gold-violet Raman beams entering from multiple angles; faint golden standing-wave field representing shared vibrational mode; dark cylindrical vacuum chamber∘\circNeutral Atoms(QuEra)Programmable two-dimensional array of Rb atoms held by optical tweezers, with Rydberg interactions enabling programmable many-body
dynamics and analog Hamiltonian simulationRed optical tweezer beams crisscrossing to form atom grid; soft blue glow of individual rubidium atoms; Rydberg excitation halo around targeted atoms; reconfigurable geometric patterns (triangular, square)■\blacksquareSuperconducting(Rigetti)Josephson junction circuits cooled to∼\sim15 mK in a dilution refrigerator, controlled by microwave pulsesGolden microwave waveguides routing control signals; superconducting processor chip with circuit traces; frost and ice crystals on copper cooling stages; tall cylindrical dilution refrigerator vessel

Note.Each row describes the scientific concept grounding the generative prompt and the resulting visual elements in the AI-generated 3D world. Colors are consistent with TableIVand Figure1. All three environments are synthesized via World Labs’ generative world-model pipeline from combinations of scientific illustrations and reference device photographs (AppendixC).

TableVpresents representative prompts and the corresponding visual outputs for each quantum architecture, illustrating how physical specifications are translated into generative scene descriptions.

## IV-CExtensibility for New Architectures

Adding a new architecture follows a modular workflow designed to separate pedagogical content from application logic. First, the developer reviews the scientific literature for the target hardware platform and extracts key physical phenomena, structural parameters, and visual features that distinguish the architecture. Second, these specifications are translated into structured text prompts for the World Labs Marble generative world model platform, following the prompt engineering methodology described in SectionIV-A. Third, the generated world is iteratively refined through manual curation to ensure scientific accuracy and pedagogical clarity. Fourth, the developer authors a teaching guide specifying learning objectives, key concepts, discussion questions, and cross-references to existing architectures. Finally, the new world and its teaching content are registered in the application configuration, and the platform is redeployed through its continuous delivery pipeline. This separation of concerns—content, world assets, and application logic—ensures that domain experts can contribute new quantum hardware visualizations without modifying core application code, a design decision that supports community-driven expansion to emerging architectures such as photonic and topological qubit systems.

This modular structure ensures that domain experts can contribute new worlds without modifying core application code. The separation of pedagogical content (Markdown files), 3D world assets (World Labs URLs), and application logic (React components) follows established software engineering principles and lowers the barrier to community contributions. As new modalities such as photonic quantum computing and topological qubits mature[3], they can be incorporated into the platform through this same standardized workflow.

## VUse Cases and Demonstration

This section presents four use cases illustrating howQuantum Cinemaserves its dual target communities: educators, researchers, and science communicators seeking an intuitive tool for explaining quantum hardware, and developers seeking to replicate or extend the platform.

## V-AUse Case 1: Teaching Quantum Entanglement

Consider an undergraduate physics instructor preparing a lesson on quantum entanglement for a classroom of students with no prior exposure to quantum computing hardware. The instructor directs students toQuantum Cinema, where each student progresses through the four-act narrative at their own pace.

InAct 1—Nobel Prize, students first encounter the
2025 Nobel Prize in Physics as the contemporary hardware
anchor for the experience[38]. The interactive timeline then
connects this milestone to the 2022 Nobel Prize in
Physics awarded to Alain Aspect, John Clauser, and Anton
Zeilinger for foundational experiments on quantum
entanglement and Bell inequalities[36]. This sequence links the physical
hardware of contemporary quantum processors to the
entanglement principles introduced in the subsequent
acts.

InAct 2—World Models, the student selects thetrapped-ionarchitecture card. A short looping video introduces the core physical concept: individual charged atoms suspended in an electromagnetic trap and manipulated by laser beams. The student learns that trapped-ion systems are one of the leading platforms for realizing entangled quantum states in a controlled, repeatable manner[17].

Act 3—Exploredelivers the immersive centerpiece. The student enters a generative three-dimensional world depicting a linear chain of trapped ytterbium ions suspended in an ultra-high vacuum chamber. Gold-violetRaman laser beamsenter from multiple directions, and a faint golden standing-wave structure represents thecollective phonon mode—the shared vibrational motion of the entire chain that serves as the quantum bus coupling distant qubits. Two highlighted ions at opposite ends of the chain are phase-locked to this shared field. An annotation delivers the key teaching moment: these ions are entangled not through any physical wire, but through their shared coupling to the collective motion of the ion chain. This makes abstract textbook descriptions of entanglement concrete and observable. Teaching guides with discussion questions and conceptual checkpoints accompany the scene[28].

InAct 4—Compare, the student observes that trapped-ion systems offerall-to-all connectivity—any qubit interacts directly with any other—in contrast to the limited nearest-neighbor connectivity of superconducting architectures or the geometry-constrained connectivity of neutral-atom systems. This observation reinforces why trapped-ion platforms have been central to entanglement research: their native connectivity mirrors the non-local correlations that entanglement produces.

## V-BUse Case 2: Architecture Comparison for Quantum Researchers

A quantum-computing researcher evaluating hardware
platforms can access Act IV directly, bypassing the
narrative Acts I–III. The comparison dashboard shown in
Fig.5groups devices by
computational paradigm. The gate-based view directly
compares IonQ Aria and Rigetti Ankaa-3, whereas QuEra
Aquila is presented in a separate analog
Hamiltonian-simulation view using platform-native
sequence-level and per-atom quantities.

The dashboard reports six metrics: coherence or evolution
time, two-qubit or sequence-level fidelity, readout
fidelity, error rate, connectivity, and physical qubit or
atom count. Users may switch between paradigm views and
toggle the displayed devices. The interface deliberately
avoids producing a single universal ranking because
hardware suitability depends on computational model and
target workload.

The current deployment instead provides illustrative
workload matches. IonQ Aria is associated with
small-molecule simulation, where long coherence and high
fidelity are important; Rigetti Ankaa-3 is associated with
iterative optimization applications such as power-grid
planning, where fast gate operations are valuable; and
QuEra Aquila is associated with materials and
carbon-capture modelling that can exploit native analog
Hamiltonian simulation. These examples are explanatory
workload mappings rather than claims of benchmarked
application superiority.

This capability transforms architecture comparison from a
fragmented documentation exercise into an interactive,
visually grounded exploration of hardware trade-offs.(a) Gate-Based Quantum ProcessorsDirect comparison: IonQ Aria vs. Rigetti Ankaa-3◆\blacklozengeIonQ Aria■\blacksquareRigetti Ankaa-320406080100Coherence /[-1pt]
EvolutionEntangling /[-1pt]
Sequence Fid.Readout[-1pt]
FidelityError Rate†ConnectivityScale[-1pt]
(Qubits / Atoms)(b) Analog Hamiltonian SimulationQuEra Aquila; platform-native AHS equivalents∘\circQuEra Aquila20406080100Coherence /[-1pt]
EvolutionEntangling /[-1pt]
Sequence Fid.Readout[-1pt]
FidelityError Rate†ConnectivityScale[-1pt]
(Qubits / Atoms)Scores are displayed on a 0–100 scale and oriented so that
higher is better.†Only the error-rate axis is inverted; QuEra uses
platform-native evolution- and sequence-level equivalents.Figure 5:Paradigm-aware comparison of the three
representative quantum devices across six 0–100 dashboard display scores. The gate-based panel
directly compares IonQ Aria and Rigetti Ankaa-3, while QuEra
Aquila is shown separately because analog Hamiltonian simulation
does not expose all gate-model calibration quantities. Scores
reproduce the current deployed comparison dashboard on a
0–100 scale; only the error-rate axis is inverted so that higher
values are preferable. QuEra’s temporal and fidelity axes use
explicitly labelled platform-native evolution-window and
sequence-level equivalents. Raw device values are curated from
Amazon Braket and official manufacturer specifications[3,17,31,4].

## V-CUse Case 3: Science Communication and Public Engagement

A science journalist preparing an article on the competitive landscape of quantum computing needs to understand the differences between hardware architectures but lacks a physics background. Existing technical documentation assumes familiarity with concepts such as cryogenic cooling, electromagnetic confinement, and laser addressing—barriers that prevent accurate reporting.Quantum Cinemaaddresses this gap through its four-act narrative structure, which requires no quantum computing background and progressively builds understanding through visual metaphors.

Thefreezing temperaturerequired for superconducting qubits—approximately 15 millikelvin, colder than outer space—is rendered as shimmering ice crystals descending through the cryogenic stages of the dilution refrigerator. Thelaser beamsthat control trapped-ion qubits appear as golden threads of light, making visible the invisible electromagnetic fields that perform quantum gate operations. Theoptical tweezersthat arrange neutral atoms are depicted as delicate pink beams sculpting a programmable lattice, conveying the programmable reconfigurability of this architecture.

These visual metaphors are intended to provide
accessible explanatory representations that journalists
can translate into prose for general readerships. The
experience is shareable through a single URL and can be
embedded into web articles as an iframe, avoiding the
installation and headset requirements associated with
many virtual-reality approaches. Prior immersive and
augmented-reality research motivates the use of spatial
interaction for quantum communication[43,19]; however, the
present paper does not measure engagement, retention, or
learning gains. Controlled evaluation of these outcomes
is therefore identified as future work.

## V-DD. Use Case 4: Extending the Platform

For developers and systems researchers who wish to replicate Quantum Cinema or adapt its pipeline to other domains of scientific infrastructure, the platform provides a complete, documented path from source code to deployed application. The replication workflow is designed to require minimal configuration: the application runs locally with a single command after dependency installation, and all static assets are bundled at build time, eliminating external service dependencies during development.

The extension workflow for adding new quantum architectures follows the modular pipeline described in SectionIV-A. Developers begin by conducting a scientific literature review for the target hardware, extract key physical phenomena and structural features, engineer structured text prompts for the generative world model platform, curate the resulting environment for accuracy, author pedagogical content, and register the new world in the application configuration. This separation of pedagogical content, three-dimensional world assets, and application logic ensures that domain experts can contribute without modifying core code.

The deployment pipeline provisions the CloudFront content delivery network, Application Load Balancer, and Elastic Container Service Fargate cluster through infrastructure-as-code configuration. The static-first architecture ensures predictable scaling behavior and low operational overhead, making the platform suitable for classroom deployment, public outreach events, and integration into institutional learning management systems.

## VIConclusion, Limitations, and Future Work

Quantum Cinema represents the first interactive system to leverage generative world models—neural networks that learn to simulate virtual environments—for the visualization of quantum computing hardware, directly addressing the “imagination gap” between quantum computing’s transformative potential and public understanding. By rendering the invisible subatomic machinery of quantum processors as explorable cinematic worlds, we bridge a critical communication barrier that has long impeded the broader adoption and comprehension of quantum technologies.

The platform’s four-act cinematic structure—spanning from a Nobel Prize historical narrative through curated video introductions for conceptual grounding, into freeform 3D exploration, and culminating in side-by-side hardware comparison—makes quantum hardware accessible to non-expert audiences while preserving the scientific depth required by researchers. Each featured architecture is accompanied by a dated, curated device snapshot drawn from Amazon Braket and official manufacturer documentation. These values support the quantitative architecture comparison but do not constitute live calibration measurements or physical validation of the generated scenes.The complete system is open-source, runs entirely in the browser without installation, and is freely accessible to a global audience regardless of technical background or computational resources.

We acknowledge several limitations of the current system and outline corresponding future directions across three areas.

## Fidelity and Coverage

The generative worlds are explanatory visualizations
informed by device documentation and curated parameters,
not physical simulations. They are designed to support
more concrete understanding of hardware structure and
operating principles; users seeking computational
fidelity should consult dedicated quantum-simulation
frameworks. Device parameters further represent static snapshots rather than real-time data, and the platform is currently limited to three architectures (superconducting, trapped-ion, and neutral atom), with photonic and topological qubit systems under active development. The reliance on a commercial generative platform (World Labs) also introduces a dependency, which we mitigate by documenting our complete prompt engineering methodology so that worlds can be regenerated using alternative platforms as the ecosystem evolves. Future work will pursue live integration with AWS Braket to dynamically update hardware parameters, incorporate additional architectures including photonic and topological qubits, and maintain platform-agnostic documentation for reproducibility.

## Interactivity and Pedagogy

The immediate research
priority is a controlled user study with students,
educators, and science communicators to evaluate changes
in quantum-hardware understanding, conceptual retention,
usability, and engagement. Such an evaluation is
necessary before making causal claims about educational
effectiveness. The platform also does not currently support interactive
quantum-circuit execution within the 3D environments,
limiting users to observational rather than experimental
exploration. Subsequent engineering work will embed
circuit simulators within the immersive worlds so that
users can observe how program-level operations relate to
hardware-level representations. Integration with
established frameworks and curricula, including Qiskit,
Cirq, and PennyLane, will further support adoption in
existing educational settings.

## Accessibility and Community.

Future releases will
extend global accessibility through multi-language
support and collaborative multiplayer exploration modes
that enable group learning and shared scientific
discovery.

Broader Impact.Quantum Cinema is intended to contribute to United
Nations Sustainable Development Goal 4 through
browser-based access to quantum-science education, and
to the inclusive-infrastructure and access objectives of
SDGs 9 and 10 through its open-source, zero-install, and
no-headset design[39]. The platform can be
reused by educators and science communicators without
requiring local quantum hardware. These connections
describe intended accessibility contributions; the
present study does not report measured learning gains,
low-bandwidth performance, or the comparative energy
efficiency of quantum and classical computing.

In closing, Quantum Cinema establishes a new paradigm at
the intersection of generative artificial intelligence
(AI) and quantum education.

## Acknowledgment

The authors thank the participants and organizers of the tutorials at The Web
Conference 2026[24]and IEEE ICBC 2026[15], whereQuantum Cinemawas presented as an interactive demonstration and
subsequently refined based on participant feedback. The authors also acknowledge
the open-source communities supporting Next.js, React, and Amazon Web Services,
and World Labs for the generative world-model platform used in this work.

## References
- [1]Y. Alexeev, M. H. Farag, T. L. Patti,et al.(2025)Artificial intelligence for quantum computing.Nature Communications16,pp. 10829.External Links:Document,LinkCited by:§I.
- [2]Amazon Web Services(2024)AWS Cloud Infrastructure.Note:Cloud computing platformAccessed: 2024-12-01External Links:LinkCited by:TABLE VIII,TABLE VIII,§III-A.
- [3]Amazon Web Services(2026)Amazon braket supported regions and devices.Note:https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.htmlAccessed 1 August 2026Cited by:TABLE VIII,§B-D,§III-C,TABLE IV,§IV-A,§IV-B,§IV-C,Figure 5.
- [4]Amazon Web Services(2026)QuEra Aquila on amazon braket.Note:https://aws.amazon.com/braket/quantum-computers/quera/Accessed 1 August 2026Cited by:§B-D,§III-C,§III-C,TABLE IV,§IV-B,Figure 5.
- [5]R. C. Basole and T. Major(2024)Generative AI for visualization: opportunities and challenges.IEEE Comput. Graph. Appl.44(2),pp. 55–64.External Links:DocumentCited by:§I,§II-C.
- [6]J. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost, N. Wiebe, and S. Lloyd(2017)Quantum machine learning.Nature549,pp. 195–202.External Links:DocumentCited by:TABLE VI,§I,§I,§II-D.
- [7]D. Bluvstein, S. J. Evered, A. A. Geim, S. H. Li, H. Zhou, T. Manovitz, S. Ebadi, M. Cain, M. Kalinowski, D. Hangleiter, J. P. B. Ataides, N. Maskara, I. Cong, X. Gao, P. S. Rodriguez, T. Karolyshyn, G. Semeghini, M. J. Gullans, M. Greiner, V. Vuletić, and M. D. Lukin(2024)Logical quantum processor based on reconfigurable atom arrays.Nature626,pp. 58–65.External Links:DocumentCited by:TABLE VI,TABLE VI,TABLE VI,TABLE VI,§III-C,§III-C,TABLE IV.
- [8]C. D. Bruzewicz, J. Chiaverini, R. McConnell, and J. M. Sage(2019)Trapped-ion quantum computing: progress and challenges.Applied Physics Reviews6(2),pp. 021314.External Links:DocumentCited by:TABLE VI,TABLE VI,TABLE VI,TABLE VI,§C-A,§C-B,§III-C,§III-C,TABLE IV.
- [9]G. Carleo and M. Troyer(2017)Solving the quantum many-body problem with artificial neural networks.Science355(6325),pp. 602–606.External Links:DocumentCited by:§II-D.
- [10]M. Cerezo, A. Arrasmith, R. Babbush, S. Benjamin, S. Endo, K. Fujii, J. McClean, K. Mitarai, X. Yuan, L. Cincio, and P. Coles(2021)Variational quantum algorithms.Nature Reviews Physics3,pp. 625–644.External Links:DocumentCited by:TABLE VI,TABLE VI,TABLE IX,TABLE IX,§II-D.
- [11]C. Dede(2009)Immersive interfaces for engagement and learning.Science323(5910),pp. 66–69.External Links:DocumentCited by:§B-A,§B-C.
- [12]J. Ding, Y. Zhang, Y. Shang,et al.(2025)Understanding world or predicting future? a comprehensive survey of world models.ACM Computing Surveys58(3),pp. 1–37.External Links:Document,LinkCited by:TABLE VII,TABLE VII.
- [13]Y. Du, Y. Zhu, Y. Zhang,et al.(2026)Artificial intelligence for representing and characterizing quantum systems.Nature Reviews Physics.Note:Published online 29 July 2026External Links:Document,LinkCited by:§I.
- [14]C. Gidney(2016)Quirk: a drag-and-drop quantum circuit simulator.Note:Web toolAccessed: 2024-12-01External Links:LinkCited by:§I,§II-A,TABLE I.
- [15]S. Guo, H. Huang, D. Liu, A. Zhang, and L. Zhang(2026)Blockchain infrastructure for intelligent cyber–physical–social systems:post-quantum security, interoperability, and trustworthy data economies in the era of embodied ai.External Links:2606.06895,LinkCited by:Acknowledgment.
- [16]IBM(2024)IBM Quantum: quantum computing platform.Note:Online platformAccessed: 2024-12-01External Links:LinkCited by:§I,§II-A,TABLE I.
- [17]IonQ(2026)IonQ Aria: quantum-system specifications.Note:https://www.ionq.com/quantum-systems/ariaAccessed 1 August 2026Cited by:§B-D,§III-C,§III-C,TABLE IV,§IV-B,Figure 5,§V-A.
- [18]A. Jordon, A. Hawkins-Seagram, S. Norrie, J. Ossorio, and U. Stege(2023)QWalkVis: quantum walks visualization application.InProc. IEEE Int. Conf. Quantum Comput. Eng. (QCE),pp. 87–93.External Links:DocumentCited by:§II-A,TABLE I.
- [19]M. Karunathilaka, S. Ruan, Y. Mao, and Y. Wang(2025)Intuit: explain quantum computing concepts via AR-based analogy.InExtended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA),Note:Late-Breaking WorkExternal Links:DocumentCited by:§II-B,TABLE I,§V-C.
- [20]P. Krantz, M. Kjaergaard, F. Yan, T. P. Orlando, S. Gustavsson, and W. D. Oliver(2019)A quantum engineer’s guide to superconducting qubits.Applied Physics Reviews6(2),pp. 021318.External Links:DocumentCited by:TABLE VI,TABLE VI,TABLE VI,TABLE VI,TABLE VI,§C-C,§III-C,§III-C,TABLE IV.
- [21]D. Liu, A. Zhang, and L. Zhang(2026)QSignAI: quantum-randomness-seeded identity signatures at the intersection of ai for science and science for ai.External Links:2605.27729,LinkCited by:§II-D.
- [22]D. Liu, A. Zhang, and L. Zhang(2026)Quantum Circuit Vision: cost-aware evaluation of visual AI agents for quantum code generation.Note:arXiv preprint arXiv:2607.10057External Links:LinkCited by:§II-D.
- [23]D. Liu, A. Zhang, and L. Zhang(2026)Quantum Futures Interactive: a live demonstration of post-quantum blockchain security, infrastructure tradeoffs, and sustainable distributed trust.External Links:2605.15991,LinkCited by:§II-D.
- [24]D. Liu, A. Zhang, and L. Zhang(2026)Quantum-safe, efficient, and ai-enhanced blockchains for the web: a cooperative tutorial on quantum computing, blockchain applications, and data standards.InCompanion Proceedings of the ACM Web Conference 2026,WWW Companion ’26,New York, NY, USA,pp. 35––38.External Links:ISBN 9798400723087,Link,DocumentCited by:Acknowledgment.
- [25]Meta Platforms(2024)React 19: A JavaScript library for building user interfaces.Note:UI libraryAccessed: 2024-12-01External Links:LinkCited by:TABLE VIII,§III-A.
- [26]P. Migdał, K. Jankiewicz, P. Grabarz, C. Decaroli, and P. Cochin(2022)Visualizing quantum mechanics in an interactive simulation — Virtual Lab by Quantum Flytrap.Optical Engineering61(8),pp. 081808.External Links:DocumentCited by:§I,§II-A,§II-B,TABLE I.
- [27]M. A. Nielsen and I. L. Chuang(2010)Quantum computation and quantum information.10th Anniversary edition,Cambridge University Press.External Links:ISBN 978-1107002173Cited by:TABLE VI,TABLE VI,TABLE VI,TABLE VI,TABLE VI,TABLE VI,TABLE IX,TABLE IX.
- [28]S. Norrie, A. Estey, H. A. Müller, and U. Stege(2024)QNotation: a visual browser-based notation translator for learning quantum computing.InProc. IEEE Int. Conf. Quantum Comput. Eng. (QCE),pp. 25–33.External Links:DocumentCited by:§II-A,TABLE I,§V-A.
- [29]Q-CTRL(2024)Black opal: quantum learning platform.Note:https://q-ctrl.com/black-opalAccessed: 2025-01-15Cited by:TABLE I.
- [30]QuantBlockchain and Quantum Cinema Team(2026-06)Quantum cinema.Note:Zenodo archiveExternal Links:DocumentCited by:§I.
- [31]Rigetti Computing(2024-12)Rigetti computing launches 84-qubit Ankaa-3 system and reports two-qubit gate-fidelity milestones.Note:https://www.rigetti.com/news/rigetti-computing-launches-84-qubit-ankaa-3-system-achieves-99-5-median-two-qubit-gate-fidelity-milestoneReports 99.0% median iSWAP fidelity and
99.5% median fSim fidelity; accessed
1 August 2026Cited by:§B-D,§III-C,§III-C,TABLE IV,§IV-B,Figure 5.
- [32]S. Ruan, Q. Guan, P. Griffin, Y. Mao, and Y. Wang(2024)QuantumEyes: towards better interpretability of quantum circuits.IEEE Trans. Vis. Comput. Graph.30(9),pp. 6321–6333.External Links:DocumentCited by:§I,§II-A,TABLE I.
- [33]S. Ruan, R. Yuan, Q. Guan, Y. Lin, Y. Mao, W. Jiang, Z. Wang, W. Xu, and Y. Wang(2023)VENUS: a geometrical representation for quantum state visualization.Comput. Graph. Forum42(3),pp. 247–258.External Links:DocumentCited by:§II-A,TABLE I.
- [34]Z. C. Seskir, P. Migdał, C. Weidner, A. Anupam, N. Case, N. Davis,et al.(2022)Quantum games and interactive tools for quantum technologies outreach and education.Opt. Eng.61(8),pp. 081809.External Links:DocumentCited by:§I.
- [35]G. Song, X. Wang, and R. Ghannam(2024)Immersive quantum: a systematic literature review of XR in quantum technology education.Comput. Educ.: X Reality5,pp. 100087.External Links:DocumentCited by:§I,§II-B.
- [36]The Royal Swedish Academy of Sciences(2022)The Nobel Prize in physics 2022.Note:Nobel MediaAwarded to Alain Aspect, John F. Clauser, and Anton Zeilinger “for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science.”External Links:LinkCited by:TABLE VI,TABLE IX,§I,§V-A.
- [37]The Royal Swedish Academy of Sciences(2024)The Nobel Prize in physics 2024.Note:Nobel MediaAwarded to John J. Hopfield and Geoffrey E. Hinton “for foundational discoveries and inventions that enable machine learning with artificial neural networks.”External Links:LinkCited by:TABLE IX,§I.
- [38]The Royal Swedish Academy of Sciences(2025)The Nobel prize in physics 2025(Website)Nobel Media.Note:Awarded to John Clarke, Michel H. Devoret, and John M. Martinis “for the discovery of macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit”External Links:LinkCited by:TABLE IX,§I,§V-A.
- [39]United Nations(2015)Transforming our world: the 2030 agenda for sustainable development.Technical reportTechnical ReportA/RES/70/1,United Nations General Assembly.Note:Accessed 2 August 2026External Links:LinkCited by:§VI.
- [40]Vercel(2025)Next.js 16: the React framework(Website)External Links:LinkCited by:TABLE VIII,TABLE VIII,TABLE VIII,§III-A.
- [41]World Labs Team(2024)Marble: generative 3d world platform.Note:World Labs Technical BlogAccessed: 2024-12-01External Links:LinkCited by:TABLE VII,§I,§I,§II-C,§III-A,§III-B,Figure 4,§IV-A.
- [42]T. Xie, Z. Zong, Y. Qiu, X. Li, Y. Feng, Y. Yang, and C. Jiang(2024)PhysGaussian: physics-integrated 3d gaussians for generative dynamics.InProc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR),pp. 4389–4398.Cited by:TABLE VII,§I,§II-C.
- [43]A. Zable, L. C. L. Hollenberg, E. Velloso, and J. Goncalves(2020-11)Investigating immersive virtual reality as an educational tool for quantum computing.InProc. ACM Symp. Virtual Reality Software and Technology (VRST),pp. Article 6, 11 pages.External Links:DocumentCited by:§I,§II-B,TABLE I,§V-C.
- [44]Z. Zhu, X. Wang, W. Liu,et al.(2024)Is Sora a world simulator? a comprehensive survey on general world models and beyond.arXiv preprint arXiv:2405.03520.Cited by:§II-C.

## Appendix AGlossary

Quantum Cinema brings together concepts from four distinct knowledge domains: quantum computing hardware, generative artificial intelligence, web application infrastructure, and foundational quantum science. To serve the interdisciplinary readership of this paper—spanning computer scientists, quantum physicists, educators, and science communicators—we provide below a comprehensive glossary organized by domain. Each table is visually distinguished by a unique color and icon to facilitate quick navigation.

TableVI(◆\blacklozengeteal) defines thephysical vocabularyof quantum computing: the three hardware architectures featured in Quantum Cinema (trapped-ion, neutral-atom, and superconducting), their constituent components (Josephson junctions, optical tweezers, Paul traps), and the fundamental quantum mechanical phenomena (entanglement, superposition, decoherence) that make quantum computation possible. These definitions directly inform the generative world models of Act III, ensuring that every 3D environment is grounded in empirically validated hardware descriptions.

TableVII(★\bigstarpurple) covers thegenerative AI technologiesthat enable Quantum Cinema’s immersive visualizations: the world model pipeline that transforms scientific specifications into explorable 3D environments, the Gaussian splatting technique used for real-time neural rendering, and the World Labs platform that powers the scene synthesis. These terms bridge the hardware definitions of TableVIwith the navigable 3D experiences presented to the user.

TableVIII(■\blacksquarenavy) documents theweb engineering stack: the serverless cloud architecture (AWS ECS Fargate, CloudFront CDN), the front-end framework (Next.js, React, TypeScript), and the single-page application model that together enable Quantum Cinema’s zero-installation, globally accessible delivery. Understanding this infrastructure is essential for researchers and developers seeking to replicate or extend the platform.

TableIX(⊙\odotamber) situates the system within its broader scientific
context through the Nobel Prizes, foundational quantum
concepts, and representative quantum algorithms. The
algorithm entries provide general background and are not
used to rank hardware in the current Act IV dashboard.TABLE VI:Glossary of Technical Terms: Quantum Computing Hardware◆\blacklozengeQuantum Computing HardwareTermDefinitionIon TrapA quantum computing platform that confines charged atomic ions in electromagnetic fields within an ultra-high vacuum chamber, using precisely tuned laser pulses to perform quantum gate operations on individual ions with high fidelity [[8]].Neutral AtomAn atom with no net electrical charge that is confined and manipulated using focused laser beams called optical tweezers, forming the basis of a quantum computing platform that offers programmable two-dimensional geometries and flexible connectivity patterns [[7]].Superconducting QubitA quantum bit implemented using superconducting electrical circuits, typically containing one or more Josephson junctions, that are cooled to millikelvin temperatures to preserve quantum coherence and enable gate operations [[20]].Josephson JunctionA superconducting device consisting of two superconducting electrodes separated by a thin insulating barrier, serving as the fundamental nonlinear circuit element that enables superconducting qubit operation through the Josephson effect [[20]].Paul TrapAn ion trap design that uses oscillating radio-frequency electromagnetic fields to confine charged particles in three-dimensional space without the need for physical walls or containers, named after Wolfgang Paul who shared the 1989 Nobel Prize in Physics for its invention [[8]].Optical TweezerA tightly focused laser beam that creates a trapping potential capable of holding and manipulating microscopic particles, used extensively in neutral-atom quantum computing to arrange individual atoms in programmable two-dimensional arrays [[7]].Rydberg BlockadeA quantum phenomenon in which the excitation of one atom to a highly excited Rydberg state shifts the energy levels of nearby atoms within a critical radius, preventing their simultaneous excitation and thereby enabling controlled entangling operations [[7]].Raman LaserA laser tuned to stimulate Raman transitions between atomic energy levels, a technique widely used in trapped-ion quantum computing to implement both single-qubit rotations and multi-qubit entangling gate operations [[8]].Quantum Bit (Qubit)The fundamental unit of quantum information that can exist in a superposition of basis states, enabling quantum parallelism and computational advantages over classical binary computation for certain problem classes [[27]].Coherence TimeThe characteristic duration during which a quantum system maintains its superposition state before environmental interactions cause decoherence, representing a fundamental limit on the length of quantum computations that can be performed reliably [[6]].DecoherenceThe irreversible loss of quantum mechanical properties, including superposition and entanglement, that occurs when a quantum system interacts with its surrounding environment; decoherence represents the primary obstacle to scaling quantum computers [[27]].EntanglementA quantum mechanical phenomenon in which two or more particles become correlated such that the quantum state of each particle cannot be described independently of the others, regardless of the spatial separation between them; the 2022 Nobel Prize in Physics was awarded for experimental demonstrations of this phenomenon [[36]].FidelityA quantitative measure of the accuracy with which a quantum gate operation or quantum state preparation is performed, defined mathematically as the overlap between the intended and actual quantum states, expressed as a value between zero and unity [[10]].Error RateThe probability that a quantum gate operation produces an incorrect output, typically quantified through randomized benchmarking protocols and reported as an aggregate figure of merit for comparing quantum device performance [[10]].GateA quantum logic operation that manipulates one or more qubits through unitary transformations, analogous to classical logic gates but operating on quantum amplitudes rather than binary values [[27]].Bloch SphereA geometric representation of a single qubit’s quantum state as a point on the surface of a unit sphere, providing an intuitive visualization of superposition, quantum phase, and the effects of single-qubit rotations [[27]].SuperpositionA fundamental quantum mechanical principle stating that a quantum system can exist in multiple states simultaneously until a measurement is performed, which collapses the system into a single definite state [[27]].Millikelvin (mK)A unit of temperature equal to one thousandth of a kelvin, representing the operating temperature regime for superconducting qubits where thermal noise is suppressed below the energy scale of the quantum computational states [[20]].Dilution RefrigeratorA specialized cryogenic cooling system that uses a mixture of helium-3 and helium-4 isotopes to reach temperatures in the millikelvin range—approximately fifteen thousandths of a degree above absolute zero—which is required for operating superconducting quantum processors [[20]].

Note.These eighteen terms constitute the physical vocabulary of quantum computing as presented in Quantum Cinema. Each definition grounds the corresponding generative world model—the immersive 3D environments of Act III—in empirically validated hardware descriptions drawn from peer-reviewed reviews of trapped-ion [[8]], neutral-atom [[7]], and superconducting [[20]] architectures. Readers seeking a comprehensive introduction to quantum computation may consult Nielsen and Chuang [[27]].TABLE VII:Glossary of Technical Terms: Generative AI and Scientific Visualization★\bigstarGenerative AI and Scientific VisualizationTermDefinitionGenerative World ModelAn artificial intelligence system that learns to synthesize realistic, interactive virtual environments by predicting the spatial structure, physical dynamics, and visual appearance of scenes from high-level descriptions or partial observations [[12]].Gaussian SplattingA neural rendering technique that represents three-dimensional scenes as collections of three-dimensional Gaussian primitives, enabling real-time photorealistic novel-view synthesis from sparse input photographs or text descriptions [[42]].World LabsA company founded by Fei-Fei Li that develops generative artificial intelligence systems for creating persistent, explorable three-dimensional virtual environments from text descriptions and images, providing the platform that powers Quantum Cinema’s immersive scenes [[41]].

Note.These three terms describe the AI substrate of Quantum Cinema. The generative world model pipeline (SectionIV) translates the hardware concepts of TableVIinto navigable 3D environments, bridging the “imagination gap” between abstract quantum physics and public understanding. For a comprehensive survey of world models, see Ding et al. [[12]].TABLE VIII:Glossary of Technical Terms: Web Application Infrastructure■\blacksquareWeb Application InfrastructureTermDefinitionAmazon Web Services (AWS) BraketA fully managed quantum computing service provided by Amazon Web Services that offers access to quantum hardware from multiple vendors, including trapped-ion, neutral-atom, and superconducting quantum processors, along with classical simulation tools and quantum algorithm development environments [[3]].Content Delivery Network (CDN)A geographically distributed system of proxy servers that caches and delivers web content to end users from the nearest edge location, thereby reducing latency, improving load times, and enhancing global availability [[2]].Elastic Container Service (ECS) FargateA serverless compute engine provided by Amazon Web Services for running containerized applications without requiring the user to provision or manage underlying server infrastructure, enabling automatic scaling and fault-tolerant deployment [[2]].Next.jsAn open-source React framework that provides server-side rendering, automatic code splitting, and hybrid static site generation, designed for building production-grade web applications with optimized performance [[40]].ReactAn open-source JavaScript library for building user interfaces through a component-based architecture that enables declarative, efficient, and flexible front-end development, maintained by Meta Platforms [[25]].Single-Page Application (SPA)A web application architecture that dynamically updates content through JavaScript without loading entire new pages from the server, providing a fluid, responsive user experience similar to native desktop applications [[40]].TypeScriptA typed superset of JavaScript developed by Microsoft that adds static type checking and advanced language features, improving developer productivity and code reliability for large-scale web applications [[40]].

Note.These seven terms describe the software engineering stack that enables Quantum Cinema’s zero-installation, globally accessible delivery model (SectionIII). The static-first, serverless architecture was chosen specifically to eliminate barriers to adoption—no quantum hardware access, no software installation, and no user account are required.TABLE IX:Glossary of Technical Terms: Foundational Science and Algorithms⊙\odotFoundational Science and AlgorithmsTermDefinitionNobel Prize in Physics 2022Awarded to Alain Aspect, John Clauser, and Anton Zeilinger for experiments with entangled photons that established the violation of Bell inequalities and pioneered the field of quantum information science [[36]].Nobel Prize in Physics 2024Awarded to John Hopfield and Geoffrey Hinton for foundational discoveries and inventions that enable machine learning with artificial neural networks, underscoring the transformative role of artificial intelligence in scientific discovery [[37]].Nobel Prize in Physics 2025Recognized advances at the intersection of quantum science and quantum computing, cementing the field’s position at the forefront of modern physics and highlighting the growing societal importance of quantum technologies [[38]].Quantum ComputingA paradigm of computation that exploits quantum mechanical phenomena—superposition, entanglement, and quantum interference—to process information in ways that can provide exponential speedups over classical computers for specific tasks [[27]].Shor’s AlgorithmA quantum algorithm for integer factorization that runs in polynomial time, offering an exponential speedup over the best known classical algorithms and demonstrating the transformative potential of quantum computing for cryptography [[27]].Quantum Approximate Optimization Algorithm (QAOA)A variational quantum algorithm designed for combinatorial optimization problems, which prepares approximate ground states of problem Hamiltonians by alternating between application of a phase separator and a mixer operator [[10]].Variational Quantum Eigensolver (VQE)A hybrid quantum-classical algorithm that uses a quantum computer to prepare trial states and a classical optimizer to adjust parameters, finding approximate ground state energies of molecular Hamiltonians [[10]].

Note.These entries provide foundational scientific and
algorithmic context for Quantum Cinema. The current
Act IV dashboard uses paradigm-aware,
application-oriented workload examples rather than
algorithm-specific claims of hardware superiority.

## Appendix BThe Four Acts of Quantum Cinema

This appendix provides a detailed walkthrough of each act in Quantum Cinema’s narrative, with annotated screenshots for Acts I, II, and IV. Act III (the immersive 3D world exploration) is illustrated in Figure1of the main text.

## B-AAct I: Nobel Prize – Establishing Historical Context

Act I grounds the user in the historical and scientific significance of quantum mechanics through an interactive timeline of Nobel Prize laureates (Figure6). The screen presents three Nobel Prizes in Physics: the 2022 award to Aspect, Clauser, and Zeilinger for experimental entanglement; the 2024 award to Hopfield and Hinton for foundational machine learning; and the 2025 award recognizing quantum computing advances. Each laureate entry includes a portrait, citation text, and a one-sentence explanation of their contribution’s relevance to quantum technology. Users scroll through the timeline at their own pace, building the “why”—the motivational foundation that answers why quantum computing matters.Figure 6:Act I: Nobel Prize timeline. Users interact with laureate profiles to understand the historical significance of quantum entanglement, neural networks, and quantum computing advances.

Pedagogical rationale.Research in science communication emphasizes that historical narrative increases engagement and retention when introducing complex technical topics[11]. By beginning with Nobel Prize laureates rather than abstract physics, Quantum Cinema leverages the authority and familiarity of these awards to build trust and curiosity in non-expert users.

## B-BAct II: World Models – Introducing Architectures

Act II transitions from historical context to technical content through curated video introductions for each of the three quantum architectures (Figure7). The screen presents a horizontal selector: trapped-ion (teal), neutral-atom (orange), and superconducting (violet). Selecting an architecture plays a short video that visually introduces its key physical features—linear ion chains, optical tweezer arrays, or Josephson junction circuits—without requiring prior quantum physics knowledge. Users may watch all three videos in any order before proceeding.Figure 7:Act II: World Models video showcase. Users select an architecture to watch its introductory video, building conceptual understanding before entering the immersive 3D environment.

Pedagogical rationale.The video-first sequence introduces key terminology and
visual motifs before immersive exploration, providing
conceptual orientation for the subsequent
three-dimensional experience.

## B-CAct III: Explore – Immersive 3D World Exploration

Act III is the centerpiece of Quantum Cinema. After selecting an architecture in Act II, the user enters a full-screen, navigable 3D world generated by World Labs’ Gaussian splatting pipeline. Figure1of the main text shows fifteen representative views across all three architectures.

Trapped-Ion World (teal).Users explore a linear chain of ytterbium ions confined in a Paul trap. Gold-violet Raman laser beams enter from multiple directions. A faint golden standing-wave field represents the shared vibrational mode. Two highlighted ions demonstrate entanglement through the shared medium—they are phase-locked not through a physical wire but through collective motion of the ion chain.

Neutral-Atom World (orange).Users navigate a two-dimensional array of rubidium atoms held by red optical tweezers. A Rydberg excitation glow surrounds targeted atoms. The programmable geometry—atoms arranged in triangular, square, or arbitrary patterns—is visible and manipulable.

Superconducting World (violet).Users explore a superconducting processor chip mounted at the base of a dilution refrigerator. Golden microwave waveguides route control signals. Frost and ice crystals on copper stages visualize the cryogenic environment. Circuit traces show the Josephson junction patterns.

Pedagogical rationale.Immersive three-dimensional environments can support
spatial understanding of quantum concepts in ways that
static diagrams cannot[11]. The generative world model approach makes invisible quantum phenomena—decoherence, laser cooling, energy loss—observable as visual narrative, directly addressing the “imagination gap” described in SectionI.

## B-DAct IV: Compare—Paradigm-Aware Architecture Comparison

Act IV provides the final integrative stage of the Quantum
Cinema experience: an interactive architecture-comparison
dashboard organized by computational paradigm
(Fig.8). The gate-based view directly compares
IonQ Aria and Rigetti Ankaa-3, whereas the analog view
presents QuEra Aquila separately as an Analog Hamiltonian
Simulation (AHS) device. This separation avoids treating
gate-model calibration quantities and analog platform-native
quantities as directly interchangeable.

The dashboard reports six metrics: coherence or evolution
time, two-qubit or sequence-level fidelity, readout fidelity,
error rate, connectivity, and physical qubit or atom count.
The corresponding radar and bar-chart values are displayed
on a 0–100 scale, with only the error-rate axis inverted so
that a higher value is preferable. For QuEra Aquila, the
temporal and fidelity axes use explicitly labelled
platform-native evolution-window, sequence-level, and
per-atom equivalents rather than a gate-modelT2T_{2}measurement or discrete two-qubit-gate fidelity. The same
six-axis comparison framework is summarized in
Fig.5.

Rather than producing a single universal ranking, the
dashboard presents illustrative workload matches. In the
current deployment, IonQ Aria is associated with
small-molecule and drug-discovery applications, where long
coherence and high fidelity are valuable; Rigetti Ankaa-3 is
associated with iterative optimization applications such as
power-grid planning, where fast gate operations are useful;
and QuEra Aquila is associated with materials and
carbon-capture modelling that can exploit native analog
Hamiltonian simulation. These mappings are explanatory
examples and should not be interpreted as claims of
benchmarked application superiority.Figure 8:Act IV: paradigm-aware architecture-comparison
dashboard. The gate-based tab directly compares IonQ Aria
and Rigetti Ankaa-3, while the analog tab presents QuEra
Aquila separately as an Analog Hamiltonian Simulation
device. The dashboard reports six 0–100 display
scores—coherence or evolution time, two-qubit or
sequence-level fidelity, readout fidelity, error rate,
connectivity, and physical qubit or atom count—together
with illustrative workload-matching recommendations. Only
the error-rate axis is inverted; QuEra’s temporal and
fidelity axes use platform-native AHS equivalents.

Pedagogical rationale.The comparison stage requires users to integrate the
historical, physical, and architectural concepts introduced
in the preceding acts and apply them to a structured
technology-selection problem. Grouping devices by
computational paradigm helps non-expert users recognize
hardware trade-offs without implying that all metrics have
identical physical meanings across gate-based and analog
systems. The underlying raw values use the same dated device
snapshot reported in TableIVand maintained in the repository’s canonicaldata.tsfile, with values curated from Amazon Braket
and official manufacturer documentation[3,17,31,4].
The dashboard scores support visual explanation and
comparative reasoning; they do not constitute a universal
hardware ranking or an independently benchmarked measure
of application performance.

## Appendix CGenerative World Model Details

This appendix details the generative world model creation process for each of the three quantum computing architectures in Quantum Cinema. For each architecture, we present: (i) the scientific concepts and reference device photographs that inform the prompt, (ii) the AI-generated immersive world output, and (iii) five representative navigable views (Figure1of the main text). The generation pipeline follows the five-step process described in SectionIVand illustrated in Figure4.

## C-ATrapped-Ion World Model

Scientific basis.Trapped-ion quantum computers confine charged atoms (ions) in electromagnetic fields within an ultra-high vacuum chamber[8]. Individual ions are addressed by precisely tuned laser beams to perform quantum gate operations. The key visualized phenomena include: the linear ion chain suspended in the trap, intersecting Raman laser beams, and the shared vibrational mode that mediates entanglement between ions.

Input.The generative prompt combines a scientific concept illustration of ionization (the process of creating charged ions from neutral atoms), a reference photograph of an IonQ trapped-ion device, and an original reference image of the ion trap apparatus (Figure9). These inputs establish the structural fidelity and physical accuracy of the generated scene.(a)Concept: ionization process(b)Device: IonQ trapped-ion system(c)Original: ion trap apparatusFigure 9:Input materials for the trapped-ion generative world model. (a) Scientific concept illustration of ionization. (b) Reference photograph of the IonQ trapped-ion device. (c) Original reference image of the ion trap apparatus.

Output.World Labs’ generative world-model pipeline synthesizes a persistent, navigable 3D environment from these inputs (Figure10). The resulting world features a linear chain of ytterbium ions suspended in a Paul trap, with gold-violet Raman laser beams entering from multiple directions. A faint golden standing-wave field represents the shared vibrational mode. Two highlighted ions demonstrate entanglement through the shared medium.Figure 10:AI-generated trapped-ion world model output. The scene shows a linear chain of ions in a Paul trap with intersecting Raman laser beams, synthesized from the inputs in Figure9.

Navigable views.Five representative viewpoints from the immersive 3D environment are shown in the top row of Figure1.

## C-BNeutral-Atom World Model

Scientific basis.Neutral-atom quantum computers use focused laser beams (optical tweezers) to arrange individual neutral atoms in programmable two-dimensional arrays[8]. By exciting atoms to highly excited Rydberg states, engineers exploit the Rydberg blockade effect—in which nearby atoms cannot simultaneously be excited—Rydberg interactions enabling programmable many-body
dynamics and analog Hamiltonian simulation. Key visualized phenomena include: the optical tweezer array, the Rydberg excitation glow, and the programmable atom geometry.

Input.The prompt combines a scientific concept illustration of atomic structure with multiple reference photographs of QuEra’s neutral-atom device, including the AWS Braket deployment and the HPCWire-featured system (Figure11).(a)Concept: atomic structure(b)Device: QuEra on AWS Braket(c)Device: QuEra HPCWire featureFigure 11:Input materials for the neutral-atom generative world model. (a) Scientific concept illustration of atomic arrangements. (b) Reference photograph of the QuEra neutral-atom device on AWS Braket. (c) QuEra device as featured in HPCWire.

Output.The generated world (Figure12) presents a two-dimensional array of rubidium atoms held by red optical tweezers. A Rydberg excitation glow surrounds targeted atoms, and the programmable geometry—atoms arranged in various patterns—is visible and explorable.Figure 12:AI-generated neutral-atom world model output. The scene shows a programmable rubidium atom array with optical tweezers, synthesized from the inputs in Figure11.

Navigable views.Five representative viewpoints are shown in the middle row of Figure1.

## C-CSuperconducting World Model

Scientific basis.Superconducting quantum processors fabricate electrical circuits containing Josephson junctions—nanoscale superconducting weak links—and cool them to millikelvin temperatures inside dilution refrigerators[20]. Microwave pulses transmitted through on-chip control lines manipulate the quantum state of each circuit element. Key visualized phenomena include: the Josephson junction circuits, the dilution refrigerator cryostat, the golden microwave waveguides, and the frost/ice crystals that form at cryogenic temperatures.

Input.The prompt combines a scientific concept illustration of the Josephson effect with a reference photograph of Rigetti’s superconducting processor (Figure13).(a)Concept: Josephson effect(b)Device: Rigetti superconducting processorFigure 13:Input materials for the superconducting generative world model. (a) Scientific concept illustration of the Josephson effect. (b) Reference photograph of the Rigetti superconducting processor.

Output.The generated world (Figure14) shows a superconducting quantum processor chip mounted at the base of a dilution refrigerator. Golden microwave waveguides route control signals to individual qubits, and frost crystals on copper cooling stages visualize the cryogenic environment.Figure 14:AI-generated superconducting world model output. The scene shows a Josephson-junction chip in a dilution refrigerator with microwave waveguides and cryogenic infrastructure, synthesized from the inputs in Figure13.

Navigable views.Five representative viewpoints are shown in the bottom row of Figure1.

## 


- 


Major funding support from
