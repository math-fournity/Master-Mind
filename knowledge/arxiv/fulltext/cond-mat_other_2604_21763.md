# Physics of Computation and Behavior in Plants

**arXiv ID**: 2604.21763v1
**Authors**: Yasmine Meroz
**Published**: 2026-04-23
**Categories**: cond-mat.other, nlin.AO
**Comments**: 5 figures
**HTML URL**: https://arxiv.org/html/2604.21763v1

## Abstract

Plants solve complex problems without centralized control, relying instead on growth-driven dynamics to sense, navigate, and optimize resource acquisition. This review presents a unified physical framework for understanding plant behavior through three complementary principles: distributed physical computation, embodied mechanical intelligence, and functional stochasticity. Tropic responses and circumnutations are interpreted as spatio-temporal dynamical systems in which information is encoded in biochemical and mechanical fields, integrated over space and time, and translated into differential growth. Mechanical interactions couple morphology to environmental constraints, enabling computation through material properties. Stochastic fluctuations, from molecular to organismal scales, act as functional resources that enhance sensing, exploration, and collective organization. Together, these processes position plants as a model system for decentralized computation in active matter, where behavior and structure emerge from the interplay of growth, transport, mechanics, and noise.

## Full Text

Physics of Computation and Behavior in Plants

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
- License: CC BY-NC-ND 4.0arXiv:2604.21763v1 [cond-mat.other] 23 Apr 2026\jvol

AA\jyearYYYY

## Physics of Computation and Behavior in PlantsYasmine Meroz1,2

## Abstract

Plants solve complex problems without centralized control, relying instead on growth-driven dynamics to sense, navigate, and optimize resource acquisition. This review presents a unified physical framework for understanding plant behavior through three complementary principles: distributed physical computation, embodied mechanical intelligence, and functional stochasticity. Tropic responses and circumnutations are interpreted as spatio-temporal dynamical systems in which information is encoded in biochemical and mechanical fields, integrated over space and time, and translated into differential growth. Mechanical interactions couple morphology to environmental constraints, enabling computation through material properties. Stochastic fluctuations, from molecular to organismal scales, act as functional resources that enhance sensing, exploration, and collective organization. Together, these processes position plants as a model system for decentralized computation in active matter, where behavior and structure emerge from the interplay of growth, transport, mechanics, and noise.

## keywords:plants, tropisms, active material, physical computation, embodied intelligence, embodied mechanical intelligence, morphological computation, functional noise, stochasticity

## doi:10.1146/((please add article doi))††journal:Xxxx. Xxx. Xxx. Xxx.

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

## 1INTRODUCTION

Growing plants solve complex navigational problems in a continuously changing environment. Unlike motile organisms, they move by growing. A plant root needs to find water and nutrients in a heterogeneous granular environment, while identifying and overcoming obstacles such as rocks. A climbing plant in a dense jungle needs to search for light while assessing objects in order to twine on them for support. Already in the nineteenth century, Darwin invoked the idea of a root “brain” to account for such complex behaviors, raising the question of how coordination arises in the absence of centralized control. And yet, from a computational perspective, plants are completely decentralized systems, with no brain or neurons, made up of rigid cells glued together and typically considered as communicating primarily through transport of water, nutrients, and hormones.

The absence of a centralized computing system, and the simplicity of the underlying anatomy of plants, offer an exciting opportunity to study the physical concepts which enable plants, considered here as essentially decentralized active materials, to sense, compute, and move, performing complex behavioral processes.
Over evolutionary timescales, plants have developed complementary strategies to overcome the lack of centralized control, centered around complementary concepts that are currently at the forefront of condensed matter physics and active matter, with strong connections to physical computation and robotics:(i) Distributed physical computation, where information is encoded, processed, and integrated through the intrinsic dynamics of a spatially extended material system, rather than through symbolic or centralized control;(ii) Embodied mechanical intelligenceor morphological computation, offloading computational tasks by capitalizing on the system’s morphological and mechanical properties; and(iii) Functional noise, taking advantage of inherent stochasticity as a computational and behavioral resource.
Although elements of these ideas have appeared across plant biology, their integration into a unified physical framework for plant computation and behavior remains in its early stages.
From a physics perspective, these concepts share a common role in enabling computation in decentralized systems, yet are typically developed in distinct contexts. Plants provide a unique setting in which they naturally coexist and interact, offering an opportunity to uncover new couplings and emergent phenomena arising from their interplay.
This review therefore aims not only to synthesize existing results, but also to outline a conceptual foundation for a nascent and inherently interdisciplinary field.

In physical systems, observed dynamics provide a primary window into underlying mechanisms: whether in driven matter, critical phenomena, or transport processes, macroscopic behavior encodes the governing principles. A similar perspective underlies the study of biological systems, where movement serves as the macroscopic readout of internal computation and is widely used to investigate behavioral processes such as decision-making, motor control, and collective dynamics.
In plants, movement is achieved primarily through growth, which spans a wide range of spatial and temporal scales, from rapid mechanically driven motions to slow reorientations mediated by differential growth[40,45]. These growth-driven movements are essential for acquiring key resources, such as light for photosynthesis and water and nutrients in roots. Because growth corresponds to the continuous addition of new material, movement does not simply reposition the organism, but builds its structure over time, shaping morphology, posture, and mechanical stability. As a result, unlike motile systems in which trajectories can be reversed or erased, the geometry of a growing plant encodes the history of its behavior-related movements, making behavior and development inherently inseparable.

To maintain a coherent thread, we frame this review around growth-driven movements of shoots and roots, including internally driven oscillatory movements, termed circumnutations, and growth responses to external directional stimuli such as light and gravity, termed tropisms. A complementary example from leaf morphogenesis is discussed in Box 1. This focus enables us to adopt an experimentally and theoretically tractable input–output framework. For clarity, we emphasize selected representative examples, which are by no means exhaustive. In doing so, we hope to highlight plants as a rich system for exploring decentralized computation in living matter, and to encourage further theoretical and experimental contributions at the interface of condensed matter physics and plant science. Plants are all around us, inviting us to open our eyes to the rich playground of fundamental questions hidden in plain sight.

## 2PLANT TROPISMS: SPATIO-TEMPORAL DYNAMICAL SYSTEMS

Growth-driven movements in plants are broadly classified as eithernasticortropic[59]. Nastic movements are driven by internal cues and are not directly oriented by an external directional stimulus. A canonical example is circumnutation, a quasi-periodic bending motion often associated with exploratory behavior, although more irregular forms are sometimes broadly referred to as nutations[40,147]. Tropisms are the growth-driven responses of a plant to a directional stimulus, for example a shoot redirects its growth toward light (phototropism) or away from gravity (gravitropism)[40,50]. Fig.1a shows snapshots of the gravitropic response of anArabidopsisshoot; the organ is placed horizontally and, over time, reorients its growth away from gravity until it reaches a steady-state configuration.
Shoots and roots display distinct tropic responses: shoots bend toward blue light and away from gravity, whereas roots bend away from light and toward gravity.
Other tropisms include responses to water (hydrotropism), touch (thigmotropism), and chemicals (chemotropism), however their sensory systems remain less well understood[50].
The morphological changes of a growing organ reflect a spatio-temporal problem in which growth, transport, mechanics, and geometry are intrinsically coupled[106,107]. Plants must integrate information over a distributed sensory system and coordinate many growing cells into a coherent response. A growing organ can be viewed as an active slender body whose local growth rate and curvature evolve according to internal fields encoding environmental information.
In what follows we briefly describe the biological building blocks underlying tropic responses and review current theoretical frameworks that treat tropisms as dynamical systems in space and time.{marginnote}

[]\entryNastic movementsInherent, driven by internal cues\entryTropic movementsDirectional responses to environmental cuesFigure 1:Multiscale description of tropic dynamics.(a) Gravitropic response of anArabidopsis thalianahypocotyl placed horizontally att=0t=0, reorienting its growth toward the vertical, shown as snapshots over time. The organ is described by its centerline geometry, parameterized by the local angleθ​(s,t)\theta(s,t).
(b) Directional stimuli are sensed by specialized sensory systems. Gravity is detected by statocytes, gravity-sensing cells located in the root cap. A single statocyte (right) shows the sedimentation of statoliths under gravity[17].
(c) Directional stimuli induce polarization of PIN transporters, biasing auxin transport along the organ and leading to the formation of a gradient across the cross-section. Shown here is the initially homogeneous distribution in anArabidopsis thalianaroot prior to reorientation (top), followed by the emergence of an asymmetric distribution after approximately one hour (bottom), visualized using the auxin-responsive DII-VENUS reporter, whose fluorescence is inversely related to auxin concentration[167]. In roots, higher auxin levels inhibit elongation, so that the resulting growth gradient is opposite to the auxin gradient.
(d) Schematic cross-section. The auxin gradient generates a spatial variation in local growth rateϵ˙\dot{\epsilon}, giving rise to a differential growth vector𝚫\boldsymbol{\Delta}.
(e) Because cells are mechanically coupled, differential growth induces curvature and bending of the organ. The geometry is described using the Frenet–Serret frame, with tangent𝐓^\hat{\mathbf{T}}, normal𝐍^\hat{\mathbf{N}}, and curvature vector𝜿\boldsymbol{\kappa}.
Panel a adapted from Bastien et al. (2013)[9].
Panel b adapted from Bérut et al. (2018)[17], CC BY-NC-ND 4.0.
Panel c adapted from von Wangenheim et al. (2017), eLife[167], licensed under CC BY.

## 2.1Plant tropisms as sensory-growth systems: sensing, processing, actuating

From a historical perspective, our understanding of tropisms is rooted in a sequence of key biological observations made in the late 19th and early 20th centuries[172]. Julius von Sachs[135]established that directional growth responses depend on differential growth rates rather than active bending, grounding tropisms in growth physiology. Charles and Francis Darwin then showed[40]that, in shoot phototropism, stimulus perception occurs near the tip, while the growth response is executed elsewhere, implying signal transmission. This separation was experimentally confirmed by Boysen-Jensen and later by Went[170], who demonstrated that
the signal is transmitted as a diffusible substance, identified as the growth hormone auxin, which controls curvature via asymmetric distribution. These insights culminated in the Cholodny–Went framework[113,171], which linked tropic curvature to lateral auxin gradients.

Building on this historical framework, through the lens of dynamical systems, plant tropisms can be viewed as sensory-growth systems. The complex sequence of biological processes underlying tropic responses can be organized into three main steps: spatially distributed sensory systems detect the direction of external stimuli, leading to redistribution of signaling molecules and growth hormones, which in turn produces differential growth and bending of the organ toward or away from the stimulus. We now describe each of these components.

Sensing.Plant sensory systems are typically not confined to a single organ, but are distributed over extended surfaces composed of many individual sensing units. Like other biological sensors, they must balance sensitivity and robustness in fluctuating and noisy environments.
In phototropism, directional light is detected by blue-light photoreceptors known as phototropins[26,32,70,88].
Redundancy among photoreceptors enhances sensitivity and dynamic range, facilitating accurate detection of environmental fluctuations[46], although the relative roles of different photoreceptors can become more complex under high-light or canopy conditions, where additional pathways such as phytochrome-mediated responses contribute[54,102].
In gravitropism, the direction of gravity is sensed in specialized cells called statocytes, which contain starch-rich organelles known as statoliths, shown in Fig.1b.
The rearrangement of statoliths under gravity (sedimentation) provides a mechanical readout of the gravity vector[30,100,153,48]. Recent work has shown that statoliths behave collectively as an active granular liquid[17], offering a physical explanation for the remarkable sensitivity of plants to small inclination angles.{marginnote}

[]\entryAuxinregulates cell wall loosening\entryPINpolar transporters establishing auxin gradients\entryTurgor pressuredrives cell expansion\entryDifferential growthgrowth gradient driving curvature

Signal processing.Although light and gravity sensing rely on distinct molecular mechanisms, both are transduced into a spatial redistribution of the growth regulator auxin[161], which acts as a morphogen that breaks symmetry at the organ scale (example shown in Fig.1c). This redistribution is largely controlled by PIN efflux carriers, whose subcellular orientation determines the direction of auxin transport across the tissue. Directional stimuli therefore induce lateral PIN relocalization, generating a transverse auxin gradient across the organ.
Signaling dynamics differ between shoots and roots at the microscopic level[58]. The kinetics and spatial organization of auxin redistribution vary substantially between these organs, reflecting differences in transport pathways, tissue architecture, and regulatory mechanisms.

Actuation.Plant movement is achieved through growth, localized near the tip, where newly formed cells undergo irreversible expansion that drives elongation. Cell expansion is driven by turgor pressure, the internal hydrostatic pressure of water within plant cells, which acts against the cell wall and enables growth when the wall yields. Auxin regulates this process by promoting cell wall loosening, thereby biasing expansion across the organ and generating a gradient of differential growth (shown schematically in Fig.1d,e). This leads to curvature analogous to a spatially programmable bilayer, similar to thermal bending in bimetallic strips[159]. In roots, by contrast, auxin inhibits growth, leading to an opposite sign of curvature for comparable auxin asymmetries.

## 2.2Theoretical models describing tropic dynamics

Modern theoretical models of tropisms formalize how stimulus sensing and transport generate differential growth, with curvature emerging as a geometric consequence[62,55,9,107]. Here we focus on macroscopic dynamics, and mechanical feedback is addressed in the next section.

We start by considering tropic dynamics in response to a single stimulus. In this case, movement is confined to a single plane, as evident in the evolution of the gravitropic response shown in Fig.1a. Without loss of generality, we focus on gravitropism, where the relevant plane is defined by the direction of gravity and the initial orientation of the organ, and the same reasoning applies to other single-direction stimuli, such as directional light in phototropism. This constraint allows the problem to be formulated in two dimensions[9,10,11], providing a more intuitive and analytically tractable framework before addressing more general three-dimensional dynamics
The organ is described by its centerline geometry, parameterized by the local angleθ​(s,t)\theta(s,t)and curvatureκ​(s,t)=∂θ​(s,t)∂s\kappa(s,t)=\frac{\partial\theta(s,t)}{\partial s}.
Building on Sachs’ sine law[136], we take the input signal to scale assin⁡(θ​(s,t)−θp)\sin(\theta(s,t)-\theta_{\text{p}})[106], whereθp\theta_{\text{p}}is the direction of the stimulus.
The simplest model equates the change in curvature directly to this signal. However, this formulation does not admit a stable steady-state solution. This formulation does not admit a stable steady state, requiring an additional curvature-dependent relaxation term.
The term reflects proprioception, the sensing of curvature, and its associated response, autotropism, the tendency of an organ to grow straight in the absence of external stimuli[9]. The role of proprioception in stabilizing posture in a growing system[9,103]is not trivial, since the target configuration is not predefined but continuously generated by growth. Put together, the tropic dynamics follow:∂∂t​κ​(s,t)=−β​sin⁡(θ​(s,t)−θp)−γ​κ​(s,t),s>L−Lgz\frac{\partial}{\partial t}\kappa(s,t)=-\beta\sin\left(\theta(s,t)-\theta_{\text{p}}\right)-\gamma\kappa(s,t),\qquad s>L-L_{\text{gz}}(1)

The parametersβ\betaandγ\gammaquantify gravitropic and proprioceptive sensitivities, respectively[9]. We note thatβ\betais a constant since gravitropic responses are independent of gravitational acceleration[30].
Growth occurs within a finite apical region of lengthLgzL_{\text{gz}},
where curvature can evolve. In the mature zone, where no growth-driven bending can occur, the dynamics are subject to the constraint∂∂t​κ​(s,t)=0\frac{\partial}{\partial t}\kappa(s,t)=0, so curvature is passively advected by growth but not actively generated.

We now generalize this framework to include explicit growth and three-dimensional dynamics[56,24,125,80]. The organ is modeled as a slender rod with centerline𝐫​(s,t)\mathbf{r}(s,t), and we adopt
We adopt the Frenet-Serret framework[53], where𝐓^\hat{\mathbf{T}}and𝐍^\hat{\mathbf{N}}are the tangent and normal to the centerline, and𝜿\boldsymbol{\kappa}is the local curvature vector (Fig.1e).
Growth enters through a material derivativeDD​t=v​∂∂s+∂∂t\frac{D}{Dt}=v\frac{\partial}{\partial s}+\frac{\partial}{\partial t}, and a differential growth vector𝚫\boldsymbol{\Delta}, representing the transverse gradient of the axial growth rate (Fig.1d), which can be expressed to leading order as𝚫≈−Rε˙0​∇ε˙.\boldsymbol{\Delta}\approx-\frac{R}{\dot{\varepsilon}_{0}}\,\nabla\dot{\varepsilon}.(2)

The tropic dynamics can be expressed in a compact vectorial form:D​𝜿D​t=ε˙0R​𝐓^×𝚫,s>L−Lgz\frac{D\boldsymbol{\kappa}}{Dt}=\frac{\dot{\varepsilon}_{0}}{R}\hat{\mathbf{T}}\times\boldsymbol{\Delta},\qquad s>L-L_{\text{gz}}(3)

whereε˙0\dot{\varepsilon}_{0}is the average axial growth rate in the growth zone, and as before, we omit the explicit dependence on(s,t)(s,t)for clarity.
This relation is kinematic and independent of specific constitutive assumptions, though it can be derived from more complete morphoelastic descriptions[108,107].
The differential growth vector, in turn, encodes the combined contributions of external directional cues, such as light and gravity, which are represented by vectors𝐈=I​𝐈^\mathbf{I}=I\hat{\mathbf{I}}and𝒈=g​𝒈^\boldsymbol{g}=g\hat{\boldsymbol{g}}respectively.
Only components perpendicular to the centerline contribute[11], as reflected by the projected stimuli𝐈⟂\mathbf{I}^{\perp}and𝐠⟂\mathbf{g}^{\perp}.
The net differential growth vector can be written as the sum of stimulus-specific contributions and a curvature-dependent proprioceptive term:𝚫=ν​(I⟂)​𝐈^⟂+β​𝒈^⟂+γ​R​κ​𝐍^\boldsymbol{\Delta}=\nu(I^{\perp})\hat{\mathbf{I}}^{\perp}+\beta\hat{\boldsymbol{g}}^{\perp}+\gamma R\kappa\hat{\mathbf{N}}(4)

where againβ\betais the gravitropic sensitivity, andγ\gammarepresents proprioceptive sensitivity.
The phototropic sensitivity is characterized byν​(I)\nu(I), a general function which encodes phototropic signal transduction sensitivity. This has been found to follow complex dependencies, such as a power law[11,80], or independence on light intensity, depending on factors such as fluence rate, internal structure, and previous exposure to light (etiolation)[69,155,140,112,36].
Together, Eqs.3and4provide the generalized form of Eq.1.

Finally, we note that in this formulation the sensitivities correspond to the growth-normalized versions of the parameters introduced in Eq.1, withβ\betaandγ\gammaeffectively normalized by the characteristic growth rate and organ size, i.e. proportional toβ​R/ε˙\beta R/\dot{\varepsilon}andγ/ε˙\gamma/\dot{\varepsilon}[10]. This normalization allows direct comparison of sensitivities across different species, independently of their size and mean elongation rate.Figure 2:Characteristic length scales and dynamical regimes of tropic responses[9].(a) Steady state shape of the gravitropic response of anArabidopsisshoot. The length of the growth zoneLgzL_{\text{gz}}, over which differential growth can generate curvature, is marked with a yellow line. The convergence lengthLcL_{\text{c}}(Eq.6), the spatial extent over which curvature occurs, is marked in pink. Their ratio defines the dimensionless balance numberB=Lgz/LcB=L_{\text{gz}}/L_{\text{c}}, which defines both shape and dynamics.
(b) Transient dynamics. Snapshots of three representative species during their gravitropic response, illustrating distinct dynamical modes defined by the number of overshoots of the vertical: mode 0 (none), mode 1 (single), and mode 2 (multiple), exemplified by a wheat coleoptile, anArabidopsis thalianahypocotyl, andImpatiens glandulifera, respectively.
(c) Relationship between oscillatory mode and balance number B across multiple species, showing that B organizes both steady-state shape and transient dynamics into distinct regimes.
All panels adapted from Bastien et al. (2013)[9], apart from Impatiens snapshot in b reproduced from Pfeffer (1898–1900)[122](public domain).

These quantities can be measured directly in experiments. In an experimentaltour de force, Bastien et al.[9]examined tropic responses across 12 angiosperm genotypes, from wheat coleoptiles to poplar trees. For wheat, Arabidopsis, and poplar, the measured tip-angle dynamics closely matched the analytical solution of Eq.1. From steady-state shapes, the authors extracted the balance numberBB(Eq.7), which ranged from approximately 0.9 to 9.3, reflecting broad intra- and interspecific variability. To further test the model, they introduced discrete oscillatory modes, defined as the maximal number of simultaneous overshoots observed during a tropic response, reflecting a range of transient dynamics: mode 0 shows no overshoot, mode 1 displays a single C-shaped overshoot, mode 2 exhibits two overshoots resembling an S shape, and so on (see examples in Fig.2b).{marginnote}

[]\entryLgzL_{\text{gz}}extent of growth zone\entryLcL_{\text{c}}extent over which curvature develops\entryTvT_{\text{v}}time until 1st vertical crossover\entryTcT_{\text{c}}convergence time until steady state

Plotting the observed modes for all 12 species against their estimated balance numbersBBrevealed a clear organization of the data according to this single control parameter (Fig.2c). Low values ofBBcorrespond to overdamped dynamics with no oscillations, as in the wheat coleoptile, whereas higher values ofBByield successive oscillatory modes, as in impatiens (Fig.2b). In this way, the experimentally measured balance number effectively maps different species onto distinct dynamical regimes, providing empirical support for the phase-diagram-like structure predicted by Eq.1.

Together, these models provide a quantitative framework for describing tropic responses as dynamical systems, establishing a common mathematical language that links sensing, growth, and shape. Tropisms thus serve as an experimentally tractable input–output system for studying computation and behavior in plants, while this framework renders these processes theoretically tractable and amenable to quantitative analysis. In the following sections, we build on this foundation to interpret plant behavior through complementary physical perspectives, beginning with distributed physical computation, and extending to embodied mechanics and stochastic dynamics

## 2.3Characteristic length and time scales: a dimensionless control parameter for tropic dynamics

Insight into tropic dynamics can be gained through dimensional analysis and steady-state solutions[9,103], revealing intrinsic length and time scales that control both posture and dynamics.
In the small-angle limit (sin⁡θ≈θ\sin\theta\approx\theta), the steady-state solution of Eq.1is exponential:θ​(s)=θ0​e−βγ​s\theta(s)=\theta_{0}e^{-\frac{\beta}{\gamma}s}(5)

While the full nonlinear problem can be solved for arbitrarily large angles[119], this linear approximation captures the essential behavior and yields a simple analytical form.
This defines a characteristic length scale, theconvergence length[9],Lc=γβL_{\text{c}}=\frac{\gamma}{\beta}(6)

which sets the spatial extent of curvature: smallLcL_{\text{c}}corresponds to localized bending, while largeLcL_{\text{c}}yields distributed curvature (Fig.2a).
A second length scale is the growth-zone lengthLgzL_{\text{gz}}, over which curvature can develop. Their ratioB=LgzLc=Lgz​βγB=\frac{L_{\text{gz}}}{L_{\text{c}}}=\frac{L_{\text{gz}}\beta}{\gamma}(7)

defines a dimensionless control parameter, termed thebalance number. ForB<1B<1, bending is insufficient to reach the vertical, whereas forB>1B>1, the organ reaches and may overshoot it (Fig.2).
The same parameter emerges from timescale considerations: the convergence timeTc∼1/γT_{\text{c}}\sim 1/\gammaand reorientation timeTv∼1/(β​Lgz)T_{\text{v}}\sim 1/(\beta L_{\text{gz}})yieldB=Tc/TvB=T_{\text{c}}/T_{\text{v}}. Thus,BBunifies spatial and temporal dynamics:B<1B<1corresponds to relaxation-dominated dynamics that do not reach the vertical, whereasB>1B>1leads to overshooting before convergence.

These quantities can be measured experimentally. Bastien et al.[9]analyzed tropic responses across 12 species and extractedBBvalues ranging from∼0.9\sim 0.9to9.39.3. The dynamics fall into distinct regimes: lowBByields overdamped responses without oscillations, while higherBBproduces successive overshoot modes, organizing species behavior into a phase-diagram-like structure (Fig.2c).
Together, these results establish tropisms as a quantitative input–output system governed by a single control parameter, linking sensing, growth, and shape.

## 3DISTRIBUTED PHYSICAL COMPUTATION IN PLANT TISSUE

Information processing in physical systems need not rely on symbolic manipulation or digital architectures. Instead, physical computation can emerge from the intrinsic dynamics of matter, when internal state variables evolve under local interactions and non-equilibrium driving to implement structured mappings between inputs and outputs[130,51,65,150,149]. In this framework, information is encoded directly in the physical configuration of the system, and computation arises from the evolution of those configurations rather than from externally imposed algorithms. Information processing therefore requires memory, namely the capacity to encode and retrieve signatures of past events within the system’s state.{marginnote}[]\entryPhysical computationcomputation implemented by intrinsic dynamics of a material system, rather than symbolic or centralized control

Driven disordered systems provide a particularly transparent example of how memory and computation can emerge from physical dynamics[109,79]. In amorphous solids and granular media, repeated driving leads to irreversible rearrangements that encode information in the material configuration, shaping subsequent responses to perturbations[78,79]. In such systems, memory is not stored in a dedicated unit, but in the collective organization of metastable states reached through non-equilibrium evolution.
A complementary perspective arises in adaptive networks, where internal parameters evolve locally to produce optimized global responses. Flow, mechanical, and electrical networks can reorganize conductances or couplings under repeated driving, thereby acquiring structured input–output mappings[18,148,5,132,130,150]. In these systems, computation resides in the gradual reshaping of internal state variables through local update rules.
Similar principles appear in biological systems, including neural networks[67], evolving bacterial populations[41], and living transport networks such as vasculature[132,83]. In plants, related mechanisms operate in vascular development, where transport optimization and mechanical feedback shape network architecture[8,77].
Across these examples, three common features emerge:(i) Memory, the encoding of past inputs in internal state variables;(ii) Spatial integration, the combination of local signals into collective responses;(iii) State updating, the evolution of internal variables under driven, dissipative dynamics.
In what follows, we identify these features in plant tropisms, presenting them as a natural realization of distributed physical computation at the tissue level.

## 3.1Memory and integration of sensory information over time in plant tropisms

Temporal integration, the ability to process, compare, and store information over time, is a fundamental requirement for adaptive behavior in living systems. In plants, where sensory information is translated into irreversible growth processes rather than immediate motion, the challenge of temporal computation is especially acute: environmental cues fluctuate across multiple timescales, yet growth decisions must remain coherent and robust[85].

Evidence accumulated over recent decades indicates that plants not only respond to instantaneous stimuli but also retain and process information about past inputs across a wide range of timescales. For example, the phototropic response depends on prior light exposure, with repeated unilateral illumination leading to desensitization or adaptation[69]. The Venus flytrap closes only when two mechanosensory hairs are triggered within a characteristic time window, implementing a clear temporal integration rule[22,166,154]. Repeated bending in poplar stems leads to attenuation of transcriptional responses, reflecting adaptation to recurring mechanical stimuli[93,104]. At longer timescales, plants can retain information about past stress events through changes in internal molecular states, including epigenetic modifications and hormonal or metabolic adjustments[66,39].

Within this broad landscape of memory processes, tropisms provide a uniquely tractable system for quantitative analysis, owing to the well-controlled experimental conditions and the availability of theoretical frameworks linking stimuli to growth-driven motion. Experimental observations of gravitropism and phototropism show that plants integrate time-varying stimuli rather than responding instantaneously. In particular, stimuli that differ in temporal structure but share the same time-integrated signal can lead to the same response[44,164,124,111,76,27,25,47,20,73,61,74,165].

These observations suggest that plant responses encode a memory of past inputs. The minimal tropism model (Eq.1) is linear and instantaneous, and therefore cannot account for temporal integration. To incorporate memory, concepts fromlinear response theoryandcontrol theorycan be adopted[96,129,29,38]. In this framework, the responsey​(t)y(t)is expressed as a weighted integral over the history of stimuli,y​(t)=∫−∞tμ​(t−τ)​x​(τ)​𝑑τ,y(t)=\int^{t}_{-\infty}\mu(t-\tau)x(\tau)\,d\tau,(8)

whereμ​(t)\mu(t)is the memory kernel. This formalism provides an effective description of temporal processing, even when the underlying dynamics are complex or unknown, and has been applied to diverse biological systems, including chemotaxis and light-driven growth responses[143,42,127,87].

Applying this framework to tropisms, the dependence of curvature dynamics on past stimuli can be interpreted as a form of memory. Recalling Eq.1, the input signalsin⁡(θ​(s,t)−θp)\sin\left(\theta(s,t)-\theta_{\text{p}}\right)represents the direct physical stimulus. This input can be replaced by a transduced signal obtained by convolution with a memory kernelμ​(t)\mu(t), representing internal signal processing, yielding∂∂t​κ​(s,t)=−β​∫−∞tsin⁡(θ​(s,τ)−θp​(τ))​μ​(t−τ)​𝑑τ−γ​κ​(s,t).\frac{\partial}{\partial t}\kappa(s,t)=-\beta\int_{-\infty}^{t}\sin\left(\theta(s,\tau)-\theta_{\text{p}}(\tau)\right)\mu(t-\tau)d\tau-\gamma\kappa(s,t).(9)

Experimental work supports this description. In wheat coleoptiles, the inferred response kernel exhibits a biphasic structure, with a positive and negative peak (Fig.3a)[129]. This structure implies that the system can compute both weighted sums and differences of stimuli depending on their temporal separation: closely spaced inputs add, intermediate delays produce subtraction, and long delays suppress earlier inputs.

Overall, this form of memory reveals computational features not previously identified in tropic responses[96,129]. The extracted response function is well described by a second-order ordinary differential equation (Fig.3a), corresponding to a nearly critically damped forced oscillator or an RLC circuit. While a direct mapping to underlying biological mechanisms remains to be established,
this analogy suggests a useful interpretive framework that may help identify biological processes with functional roles, linking macroscopic behavior to microscopic processes. More generally, approaches from signal processing and control theory offer powerful tools for understanding feedback and information processing in biological systems[38,15,4].Figure 3:Physical mechanisms underlying distributed computation in plant tropisms.(a) Memory kernel extracted from gravitropic responses of wheat coleoptiles[129](blue line), exhibiting a biphasic structure with a positive peak followed by a negative peak. The kernel is well described by a second-order linear ODE (dashed line), consistent with a band-pass filter and analogous to a forced damped oscillator or an RLC circuit.
(b) Spatial integration in nonlinear distributed systems[80]. Cross-section of a sunflower seedling (Helianthus annuus), illustrating its distributed photosensory system. Photoreceptors are arranged along the circumference (schematically marked in grey), and directional light is sensed locally. Two perpendicular light sources𝐈1\mathbf{I}_{1}and𝐈2\mathbf{I}_{2}are shown schematically. Each signal is transduced locally through a nonlinear functionν​(I)\nu(I), and the plant responds to the sum of transduced signals rather than to the physical sum of incident light. As a consequence, nonlinear encoding leads to systematic deviations between the physical and internally represented stimulus direction[80].
(c) Microscopic encoding of spatial and temporal information. Directional stimuli induce the redistribution of signaling molecules, such as the growth hormone auxin, generating gradients that encode both stimulus direction and magnitude. Stochastic transport provides a natural mechanism for temporal integration and memory. As a schematic example, two consecutive stimuli (I1I_{1}, grey, followed byI2I_{2}, yellow) induce transport processes that initially produce distinct molecular distributions. Over time, stochastic spreading causes these distributions to broaden and overlap, leading to a combined (confounded) response to multiple stimuli. Circles represent individual molecules undergoing stochastic motion.
Panel a adapted from Rivière et al. (2023)[129](CC BY 4.0)”, panels b and c, image of cross-section of sunflower seedling provided by Roni Kempinski, originals.

## 3.2Spatial integration through distributed nonlinear sensing

Another central feature of physical computation in matter is the emergence of global responses from the spatial integration of local signals. In such systems, local inputs are combined through distributed interactions, so that global function arises from geometry, coupling, and nonlinear encoding.
This problem appears broadly in decentralized sensory systems, where spatially resolved cues must be converted into a single behavioral output without centralized processing, for example in chemotactic cells, growing neurons, and other systems that integrate signals across extended surfaces.
In plant tissues, composed of many interacting cells, spatial integration emerges naturally from the extended geometry of the organ together with transport- and growth-mediated coupling between cells. As an example, mechanosensing illustrates this type of distributed integration, where spatially distributed strain sensing and tissue-scale interactions shape the effective growth response[101,90].

Phototropism provides a particularly transparent realization of this principle in the presence of multiple directional cues. Models represent stimuli as effective vectors acting on the organ centerline (Eq.4), suggesting that plants respond to the physical vector sum of incident light𝐈tot=∑𝐈i\mathbf{I}_{\text{tot}}=\sum{\mathbf{I}_{\text{i}}}. However, photoreceptors such as phototropins are distributed along the epidermis (Fig.3b), so that light is sensed and transduced locally along the shoot circumference before being integrated across the organ. Thus, the question is not simply how plants respond to light, but how a spatially distributed sensory surface encodes and combines multiple directional inputs into a single growth response. Within the general 3D framework (Eqs.3and4), the phototropic contribution to differential growth can be written as a sum of locally transduced perpendicular components[80]:𝚫ph=∑iν​(|𝐈i⟂|)​𝐈^i⟂,\boldsymbol{\Delta}_{\text{ph}}=\sum_{i}\nu(|\mathbf{I}^{\perp}_{i}|)\hat{\mathbf{I}}^{\perp}_{i},(10)

implying that the plant responds to the vectorial sum of transduced signals rather than to the physical sum of incident light. In this sense, the organ constructs an internal representation of the stimulus field prior to generating growth.

Experimental evidence supports this distributed integration rule. Under bilateral illumination, the growth direction does not follow a simple linear dependence on intensity difference, but reflects nonlinear summation at the level of local encoding. Opposing stimuli cancel at the level of transduced signals, while a weaker orthogonal cue can dominate the response by breaking this symmetry. This already shows that plants do not simply maximize physical light intensity, but respond to the vectorially integrated representation of locally encoded signals.
A key ingredient in this behavior is nonlinear signal transduction. Across biological systems, sensory inputs are typically transformed nonlinearly, often following logarithmic or power-law relations[21,146,116,151]. In phototropism, the transduction function is well described by a compressive power law,ν​(I)=ν0​Iα\nu(I)=\nu_{0}I^{\alpha}withα<1\alpha<1[11,80].
As a consequence, the integrated response does not correspond to the transduction of the total physical illumination, so that, in general,∑iν​(|𝐈i⟂|)​𝐈^i⟂≠ν​(|𝐈tot|)​𝐈^tot\sum_{i}\nu(|\mathbf{I}^{\perp}_{i}|)\hat{\mathbf{I}}^{\perp}_{i}\neq\nu(|\mathbf{I}_{\text{tot}}|)\hat{\mathbf{I}}_{\text{tot}}, and nonlinear distributed sensing produces systematic distortions between the physical and perceived directions of illumination, akin to an optical illusion (illustrated in Fig.3b).
As a result, when exposed to multiple light sources, plants are generally expected to grow not in the direction of physically maximal illumination, but in the direction of maximalperceivedillumination.
This mismatch is a structural consequence of surface-based sensing and nonlinear local encoding, rather than of any particular biochemical implementation. In this sense, plants provide a particularly transparent example of a multicellular system in which sensing and integration are fully decentralized. More broadly, the same geometric principle may operate in other systems that integrate spatially resolved cues across extended surfaces, including chemotactic cells, growing neurons, and engineered embodied sensing platforms.

## 3.3Microscopic encoding of spatial and temporal information

The previous subsections described temporal and spatial integration at the organ scale, using effective input–output descriptions such as memory kernels and vectorial integration rules. A natural question is how these computational primitives are implemented microscopically, that is, which internal degrees of freedom encode spatial information and how temporal integration arises.

In plant tropisms, spatial information is encoded in the same internal fields that underlie differential growth.
Directional stimuli are transduced into gradients of multiple signaling molecules, including auxin, PIN transporters, and associated regulatory factors. For clarity, we focus here on auxin as a representative signaling field, treating it as an information carrier encoding directional environmental cues.
As discussed above, directional stimuli generate asymmetric auxin distributions across the organ, which define the differential growth vector𝚫\boldsymbol{\Delta}, corresponding to a spatial gradient of growth rate (Eq.2), thereby providing a direct physical realization of the vectorial representation of environmental cues at the tissue scale.
More generally, if the local growth rate depends on multiple signaling and physical fields,ε˙=ε˙​(μ1,…,μN)\dot{\varepsilon}=\dot{\varepsilon}(\mu_{1},\ldots,\mu_{N}), the resulting differential growth can be decomposed into a sum of contributions,𝚫=∑i𝚫i\boldsymbol{\Delta}=\sum_{i}\boldsymbol{\Delta}_{i}, each reflecting the spatial variation of an individual cue[80].
This decomposition provides a physical basis for vectorial summation: different stimuli are first encoded locally as growth biases, and their combined effect emerges through their superposition at the level of the growth field.
In this sense, the observed vectorial integration of stimuli arises naturally from the underlying growth dynamics.
The resulting gradients are not imposed globally, but instead emerge from the collective effect of local sensing and directed transport across many cells, mediated by the polarity of PIN transporters.

Temporal integration may, in turn, arise from the dynamics of the same internal field that encodes spatial information. While spatial integration is captured by the instantaneous structure of the differential growth vector𝚫\boldsymbol{\Delta}, its time dependence reflects the processes that generate and maintain the underlying gradients. Auxin redistribution involves a hierarchy of transport and signaling steps, including statolith dynamics, PIN relocalization, and intercellular fluxes, each operating on distinct timescales[29,17,110,100,128].
Because these processes operate on multiple timescales, the response cannot be instantaneous and instead reflects a weighted history of past inputs. This motivates interpreting𝚫​(t)\boldsymbol{\Delta}(t)as an effective temporal filter, consistent with the response-kernel formulation introduced above.
Importantly, these processes are inherently stochastic: molecular transport and signaling occur through discrete, noisy events. As a consequence, initially localized signals may spread, overlap, and persist over time, providing a plausible mechanism for integrating information across temporal windows, as illustrated in Fig.3c.

In this framework, spatial and temporal integration arise from the evolution of a single internal field. The auxin distribution encodes both the spatial structure and recent history of environmental cues, and its dynamics, driven by active transport and dissipative growth, shape subsequent responses. Thus, auxin transport provides a concrete microscopic realization of distributed physical computation in plant tropisms, in which encoding, integration, and state updating emerge from the dynamics of a transported signaling field.
Unlike many physical systems discussed earlier, where memory is encoded in configurations or local interactions, here information is carried by a transported signaling field that evolves across space and time. This suggests a distinct paradigm of physical computation based on transport and field dynamics, which may open new directions for understanding decentralized information processing in living and engineered systems.

## 4EMBODIED MECHANICAL INTELLIGENCE IN PLANT ORGANS

The preceding section focused on how plant tissues process information through distributed biochemical dynamics, such as transport-mediated field integration and state-dependent growth. A complementary perspective, increasingly explored in soft condensed matter and active matter physics, is that physical structure and mechanics can themselves participate directly in computation. In this view, a material body is not merely a passive substrate executing internally determined commands, but a dynamical system whose geometry, elasticity, and environmental coupling shape its effective response to external stimuli. The system’s behavior is partly encoded in its constitutive laws and boundary conditions, so that aspects of both computation and control are implemented through physical interactions.{marginnote}

[]\entryEmbodied mechanical intelligenceFunctional behavior emerging from morphology and material response without centralized control

This idea appears across a range of physical and biological systems. Passive-dynamic walkers (Fig.4a) demonstrate that stable locomotion can arise purely from passive dynamics, maintaining a walking gait without motors or active control[95,33]. In fluid–structure interactions, compliant bodies can extract propulsion or directional bias directly from environmental flows, as in the passive upstream swimming of a dead fish in a vortex wake[86,14](Fig.4b). In active and soft matter, geometry and elasticity can encode functional responses under global loading, as in mechanical metamaterials and topological systems[35,75,16]. More broadly, robophysics has shown how behavior emerges from the coupling between body compliance and the environment[3,169].
Across these examples, function arises from constraint-driven dynamics rather than centralized control. In condensed matter terms, such systems can be viewed as active solids with feedback between deformation and internal fields[92,91], where embodied mechanical intelligence corresponds to the ability of a structured material to transform external forces into organized responses through its intrinsic mechanics.

Plant organs naturally operate in this regime. They are growing, deformable active solids whose geometry and material properties coevolve with environmental interactions. Growth modifies shape and stress distributions, while stress feeds back on growth orientation and magnitude, forming a closed dynamical loop. In this sense, plant behavior emerges from the coupled evolution of growth, mechanics, and geometry, without centralized control. The following sections examine how this principle manifests in specific plant systems and connects to broader ideas of morphological computation in biological and engineered systems[115,123,2,34].

## 4.1Growth–mechanics coupling in plant–environment interactions

Plants are continuously subject to mechanical forces arising from their environment and from growth itself. External forces include gravity, wind, soil resistance, and obstacles. Unlike motile organisms, plants cannot reposition their bodies through locomotion. Instead, they adapt their growth patterns and material properties to accommodate and exploit these mechanical constraints.
Internal forces arise from turgor pressure, the hydrostatic pressure generated by water within plant cells, and from differential growth, which generates internal stresses as neighboring cells expand at different rates within a mechanically coupled tissue. From a physical perspective, plant tissues can therefore be viewed as active elastic solids, in which growth and mechanics are intrinsically coupled.
In what follows, we focus on root growth in mechanically heterogeneous substrates as a particularly clear and experimentally accessible realization of these principles.

The classical Lockhart model[89]describes growth as a stress-dependent yielding process in which cell walls expand irreversibly when the effective driving pressure exceeds a threshold. In the presence of external mechanical constraints, this can be written asε˙=ϕ​(P−PY−σ),\dot{\varepsilon}=\phi\,(P-P_{Y}-\sigma),(11)

wherePPis the turgor pressure,PYP_{Y}is the yield threshold for cell wall extension,σ\sigmarepresents external mechanical resistance, andϕ\phiis the cell wall extensibility. Growth occurs only when the effective pressure satisfiesP−PY>σP-P_{Y}>\sigma, directly linking growth to mechanical stress.
This formulation highlights the central mechanical constraint faced by growing organs: environmental resistance can locally suppress elongation by reducing the effective driving force. As a growing root encounters an obstacle, it continues to exert compressive force through growth until this threshold is reached, at which point axial growth is inhibited. Rather than stopping, the accumulated stress can trigger a buckling instability, allowing the root to reorient and grow around the obstacle (Fig.4c)[19]. In this way, root behavior emerges from the interplay between growth, elasticity, and external constraints.

A particularly clear manifestation of this interplay arises in environments with multiple obstacles. Experiments in structured substrates reveal that root trajectories are not arbitrary, but fall into a small number of dynamical states, including vertical, oblique, and switching trajectories (Fig.4d)[175]. These states emerge from a competition between obstacle-induced deflection and gravitropic reorientation: contact with an obstacle redirects the growing tip, while gravitropism tends to restore vertical growth. The resulting trajectory reflects a balance between these effects, and depends on both the geometry of the obstacle and the intrinsic curvature response of the root. In this sense, path selection can be understood as a mechanically mediated process constrained by the ability of the root to bend and reorient under load.

In more heterogeneous, natural substrates, these mechanisms are further shaped by additional physical effects, as revealed by direct imaging of root–soil interactions[131]. Root geometry, particularly the shape of the tip and cap, influences both frictional contact and susceptibility to mechanical instabilities such as buckling[133]. In disordered or granular media, roots often exhibit helical or oscillatory trajectories, which can redistribute contact forces and reduce trapping[94,144,157,99]. These behaviors can be interpreted as mechanical strategies that facilitate navigation by exploiting growth–mechanics coupling to minimize resistance.
Even in the absence of such strategies, growth itself provides a mechanical advantage: unlike push-driven motion, growth localizes deformation near the tip while the mature region remains largely stationary, reducing distributed friction and mechanical work[82].

Taken together, these examples show that root penetration is governed by the interplay between growth, mechanics, and environmental constraints, rather than by sensing alone. However, this picture remains largely descriptive. A quantitative understanding requires extending tropism models to incorporate elasticity and mechanical contact, allowing growth-driven dynamics to be formulated within a unified physical framework.Figure 4:Embodied mechanical intelligence in biological and physical systems.(a) Passive dynamic walker[33]: a robot without motors or centralized control that achieves stable locomotion through body geometry and gravity-driven dynamics.
(b) Passive propulsion in a vortex wake: snapshots of a dead fish “swimmming” upstream by extracting energy from the surrounding flow[14](top to bottom).
(c) Root growth against a mechanical barrier. A growing root exerts increasing force until a critical threshold is reached, triggering buckling and reorientation[19].
(d) Root growth trajectories in structured obstacle arrays. Roots exhibit distinct dynamical states according to obstacle size, including vertical, oblique, and switching trajectories, emerging from the interplay between obstacle-induced deflection and gravitropic reorientation[175].
(e) Simulation framework coupling growth and mechanics based on separation of timescales. Slow growth-driven changes update the intrinsic configuration, followed by rapid mechanical relaxation to the actual configuration[126].
(f) Simulations show that the interplay of passive mechanics and gravitropism is sufficient to reproduce complex waving patterns observed in real roots on inclined substrates[126,158].
(g) Active mechanical sensing: two snapshots of a climbing shoot using circumnutations to probe its environment, generating mechanical loading upon contact with a support. (h) Analogy to rodent whisking, where contact forces, driven by perioding whisking movements, are used to probe mechanical properties of the environment[68].
Panel a reproduced with permission from Collins et al. (2001); copyright © 2001 Sage Publications. Panel b adapted with permission from Beal et al., Passive propulsion in vortex wakes, J. Fluid Mech. 549:385–402 (2006)[14]. Panel c adapted from Bizet et al.[19]. Panel d adapted with permission from Yao et al., J. Exp. Bot. 76:546 (2025); copyright © 2025 Oxford University Press[175].
Panel e and f adapted from Porat et al. (2023)[126].
Waving root in panel f adapted from Thompson et al.[158].
Panel g adapted from Ohad & Meroz (2025), J. Exp. Bot.[117], CC BY-NC 4.0. Panel h reproduced from Huet et al. (2022), PLoS Comput. Biol.,[68]licensed under CC BY 4.0.

## 4.2A theoretical framework coupling growth and elasticity

The previous subsection showed that root–environment interactions emerge from the interplay between growth and mechanics. To formalize this, we introduce a continuum description that couples active growth to passive elasticity within a single mechanical framework, making explicit how growth-induced strains interact with environmental constraints to shape organ morphology.

The central assumption is a separation of timescales between slow growth and fast mechanical relaxation (schematically illustrated in Fig.4e)[56,24,53,31,1,145,126]. On the timescale of tropic responses, elastic stresses equilibrate rapidly, allowing a quasi-static description in which growth sets intrinsic strains while elasticity enforces mechanical equilibrium.

We model the organ as a growing elastic rod within the Cosserat framework[49]. Growth acts by gradually updating the intrinsic length and curvature of the rod, confined to the apical growth zone near the tip. We therefore distinguish between the intrinsic curvature𝜿0\boldsymbol{\kappa}^{0}, set by differential growth, and the realized curvature𝜿\boldsymbol{\kappa}after elastic relaxation. This evolution can be viewed as an alternating process in which growth first updates the intrinsic curvature𝜿0\boldsymbol{\kappa}^{0}, followed by rapid mechanical relaxation that determines the realized configuration𝜿\boldsymbol{\kappa}(Fig.4e). Incorporating gravitropic feedback and proprioception yieldsD​𝜿0D​t=ε˙gR​𝐓^×(β​𝒈^⟂+γ​R​κ​𝐍^),\frac{D\boldsymbol{\kappa}^{0}}{Dt}=\frac{\dot{\varepsilon}_{g}}{R}\hat{\mathbf{T}}\times\left(\beta\hat{\boldsymbol{g}}^{\perp}+\gamma R\kappa\hat{\mathbf{N}}\right),(12)

so that growth defines the intrinsic geometry while elasticity and environmental forces determine the observed shape.

As a case study, this coupled growth-elastic system reproduces the well-known waving and coiling patterns ofArabidopsisroots grown on inclined substrates[126,176]. In this minimal description, the only active ingredient is gravitropic driving within the apical growth zone; no explicit thigmotropic sensing or imposed oscillatory curvature is required. For small substrate tilt, the root grows approximately straight. Beyond a critical angle, a periodic waving pattern emerges, corresponding to an instability in which bending energy accumulated during growth is periodically released through lateral deflection. At larger tilt angles, a second transition produces coiling, governed by the competition between active reorientation toward gravity and passive reorientation imposed by contact with the plane. The resulting morphological diagram resembles a sequence of bifurcations in which control parameters such as tilt angle and growth rate select among distinct steady or periodic solutions.
In this sense, waving and coiling can be understood as mechanically mediated pattern formation in a growing elastic rod. The phenomenon is reminiscent, in a purely mechanical context, of the coiling and meandering instabilities observed when elastic rods are deposited onto rigid substrates[72], although in roots the driving arises from growth rather than external feeding speed. More generally, this framework shows how growth sets intrinsic curvature while elasticity and environmental interactions select among possible morphologies, providing a quantitative basis for embodied mechanical intelligence. This same framework can be extended to situations in which mechanical interaction is not only a constraint but also a source of information, enabling plants to actively probe and assess the mechanical properties of potential supports.

## 4.3Active mechanical sensing in climbing plants

A particularly compelling extension of embodied mechanical intelligence arises in climbing plants, where mechanical interaction is not only a constraint but also a source of information. While the mechanics of twining and tendril attachment following contact are well understood[52,71,134,81], the stage preceding stable attachment, how a plant evaluates a candidate support, has only recently begun to be addressed.
Climbing shoots use circumnutations to probe their environment, generating mechanical loading upon contact with a support (Fig.4g)[118]. These forces follow reproducible, approximately sinusoidal trajectories, indicating that the plant imposes a controlled mechanical loading through its own motion. Within the mechanical framework introduced above, this interaction can be interpreted as a torque balance between the intrinsic bending moment of the stem and the external resistance of the support, analogous to a cantilever subjected to a rotating load. In this picture, force amplitude is primarily set by stem stiffness and geometry, while the characteristic timescale is determined by the circumnutation period.
Twining is initiated only when two mechanical conditions are satisfied: the stem must reach a critical bending moment threshold, indicating sufficient support stability, and the contact geometry must allow a minimal overshoot required for grasp. These requirements imply that support selection depends jointly on environmental resistance and the plant’s own capacity to deform into a viable wrapping configuration.
Furthermore, the sensing process is intrinsically dynamical, and manipulating the effective circumnutation rate shows that faster rotations accelerate twining initiation, whereas slower rotations delay or suppress attachment despite prolonged contact[118]. This demonstrates that touch alone is insufficient: the relevant information is generated through self-driven motion, which controls both the magnitude and timescale of mechanical loading.
This mechanism parallels active mechanical sensing in animals. Just as whisking rodents infer object properties from contact forces (Fig.4h)[28,68], climbing plants use circumnutation to probe the mechanical stability of supports. In both cases, perception emerges from the coupling between self-generated motion and environmental response.

More generally, these results show that circumnutation functions not only as a search behavior but as a mechanism for active mechanical sensing. The tapered geometry and stiffness gradient of the stem define a distributed mechanical sensor, in which morphology and elasticity encode the conditions for twining. Climbing plants exploit the geometry and elasticity of their own bodies to evaluate support stability and grasping feasibility before attachment, providing a clear example of embodied mechanical intelligence in which sensing emerges directly from the physical properties of a growing system, without the need for centralized control.{textbox}

[h]

## 5Box 1: The growing leaf as an active elastic sheet

While this review focuses on growth-driven movements of shoots and roots, similar physical principles operate in expanding leaves. The growing leaf provides a complementary example of an active elastic sheet in which distributed growth, mechanical coupling, and fluctuations interact to produce coherent organ-scale form. In this sense, leaf morphogenesis illustrates the same three ingredients discussed throughout this review: distributed physical computation, embodied mechanics, and functional stochasticity.
At the level of distributed computation, leaf growth emerges from spatially heterogeneous and temporally fluctuating growth fields. Direct measurements of in-plane growth tensors reveal strong variability in both growth rate and direction, including transient shrinkage events and broad, non-Gaussian statistics[6]. These heterogeneous signals are integrated across the tissue, resulting in smooth, coherent expansion at the organ scale. The macroscopic leaf shape can thus be viewed as a coarse-grained outcome of distributed, fluctuating growth processes.
Embodied mechanics plays a central role in constraining and shaping these dynamics. Leaves behave as viscoelastic solids at short timescales, while growth continuously modifies their intrinsic geometry and effective material properties at longer timescales[138]. Mechanical heterogeneity is particularly important: veins, which are significantly stiffer than the surrounding lamina, act as load-bearing elements that guide stress distribution. Under external loading, veins reorient along principal stress directions and surrounding tissue deforms anisotropically, revealing strongly non-affine growth[8]. Models incorporating viscoelastic rods with threshold growth laws reproduce these behaviors, showing that mechanical feedback between tissue components is sufficient to remodel network geometry. Similar principles arise in passive systems such as drying leaves, where stiffness contrasts between midvein and lamina select distinct morphologies[57]. In all cases, mechanical constraints act as a filtering mechanism that translates local growth variability into robust global form.
Finally, stochasticity itself plays an active and functional role. Growth fluctuations generate local variations in stress and strain, which are sensed and integrated through mechanical feedback, contributing to the regulation of tissue organization. Environmental perturbations such as changes in light or wind induce large strain-rate fluctuations[139], reflecting underlying hydraulic dynamics that redistribute stress during growth. At the intracellular scale, chloroplasts exhibit fluctuation-driven organization: under low light, they form dense, glass-like configurations that maximize light absorption while remaining near a fluidization threshold for rapid reorganization[141], reminiscent of active matter near a glass transition.
Taken together, the growing leaf provides a complementary realization of the same physical principles discussed in this review. Distributed growth fields perform implicit computation, mechanical coupling shapes and stabilizes the resulting form, and stochastic fluctuations provide both variability and control. Although distinct from growth-driven bending in shoots and roots, leaf morphogenesis demonstrates how decentralized plant tissues exploit these physical mechanisms across scales to generate robust, adaptive structures.

## 6STOCHASTICITY AS A FUNCTIONAL RESOURCE

Noise is often treated as a perturbation around deterministic dynamics. Yet in many decentralized physical systems, stochasticity is not merely tolerated but functionally essential. In interacting particle systems and active matter, fluctuations can seed collective motion and trigger symmetry breaking; for example, in minimal models such as the Vicsek model, the balance between local interactions and noise controls the emergence of collective order[163]. In disordered and glassy systems, stochasticity enables exploration of complex energy landscapes and gives rise to memory and history-dependent behavior[23,97,79]. Across these examples, while too little noise confines the system to suboptimal states and too much destroys coherence, intermediate levels of noise enable exploration of configuration space and transitions between states.

In biological systems, noise is likewise increasingly understood as functional. At the cellular scale, stochastic gene expression generates phenotypic variability that enhances survival under fluctuating conditions[43]. At larger scales, variability in behavior, including movement, can facilitate search, navigation, and active sensing in uncertain environments[168,120,173]. Rather than undermining coordination, noise interacts with nonlinear coupling to produce robust distributed function.

These perspectives motivate a similar reexamination in plants. As decentralized organisms lacking centralized control, plants rely on spatially distributed interactions and evolving internal state variables to integrate information. In such systems, stochasticity may not simply reflect biochemical imprecision but can shape dynamics across scales, from microscopic processes within cells, to the movements of individual organs, and ultimately to collective self-organization and emergent structure. The following sections examine these roles across these hierarchical levels.

## 6.1Stochasticity of microscopic processes in tropisms

At the cellular scale, growth-driven movements of shoots and roots emerge from inherently stochastic processes. Auxin transport, transporter relocalization, wall remodeling, and turgor fluctuations all involve discrete molecular events occurring in finite numbers. The macroscopic continuum models describing tropic dynamics can be understood as coarse-grained representations of this hierarchy of noisy microscopic processes. In this context, fluctuations are not merely background variability, but can shape the effective dynamics of curvature evolution and signal integration.
Viewed through this lens, stochasticity plays a role across all components of tropic behavior, from sensing to signal processing and actuation. We illustrate this through three representative examples.

In sensing, statolith sedimentation in gravity-sensing cells exhibits intrinsic fluctuations. Measurements show that statoliths behave collectively as an active granular medium rather than rigid inertial masses (Fig.5a)[17], suggesting that their fluctuating positions may contribute to gravity sensing.
At the level of signal processing, the experimentally extracted memory kernel reflects a coarse-grained combination of multiple stochastic processes, including statolith motion, PIN relocalization, and auxin redistribution[96,29], as discussed in Sec.3.3. This type of coarse-grained memory is reminiscent of glassy systems, where broadly distributed stochastic timescales give rise to history-dependent behavior.
In actuation, fluctuations contribute to growth regulation through proprioception[105]. At the cellular scale, heterogeneous growth generates stochastic variations in strain and stress across the tissue. These fluctuations create local mechanical contrasts that are sensed through stress-dependent feedback, such as microtubule alignment, and used to regulate growth. Although damped at the organ scale, they provide the signals that enable this control.Figure 5:Functional role of fluctuations.(a) Statolith dynamics in gravity-sensing cells[17]: snapshots of statoliths in a tilted statocyte at successive times, showing their behavior as an active granular medium. Intrinsic fluctuations facilitate rapid rearrangement, enhancing sensitivity to small inclination angles.
(b) Oscillations and active sensing in tropisms[12]: small-amplitude nutations during gravitropic responses regulate curvature dynamics. The oscillation timescale matches that of the biphasic memory kernel, suggesting that oscillations enable temporal comparison of signals across successive phases, enhancing sensitivity through an active sensing mechanism.
(c) Circumnutations in root navigation[156]: wild-type roots exhibiting circumnutations successfully penetrate heterogeneous substrates, whereas mutants lacking circumnutation fail to grow into the soil.
Below, robophysical analogs reproduce this behavior, demonstrating that oscillatory tip motion enhances navigation by preventing trapping.
(d) Self-organization of sunflower stands[121]: in sparse conditions, plants grow vertically, whereas in dense rows, mutual shading induces a zig-zag pattern through shade-avoidance responses. (f) Top-view trajectories of plant crowns reveal stochastic motion consistent with a random-walk process exhibiting a broad distribution of step sizes[114]. Circumnutations provide intrinsic fluctuations that balance exploration of configurations with sensitivity to interactions, enabling optimal spatial organization.
(e) Collective dynamics in motile systems: interacting agents (e.g., school of fish) reorient based on neighbors, as captured by minimal models such as the Vicsek model[162,37]. Depending on the ratio of noise to interactions, distinct dynamical phases emerge, including disordered swarms, milling, and polarized collective movement.
(f) Collective dynamics in growth-driven systems: examples of intertwined climbing plants (braiding) illustrate an emergent structure arising from interactions during growth. A schematic of a growth-based interaction model highlights how similar control parameters may give rise to distinct structural regimes, analogous to phases of motile system.
Panel a adapted from Bérut et al. (2018)[17], CC BY-NC-ND 4.0.
Panel b is adapted from Bastien et al. (2018)[12], public domain (CC0).
Panels c d adapted from Taylor et al. (2021), PNAS[156].
Panel e, image of fish school © LuffyKun / iStock, phases of collective dynamics adapted from Tunstrom et al. (2013)[160], licensed under CC BY.
Panel g adapted from Pereira et al. (2017), PNAS[121], Panel h adapted from Nguyen et al. (2024), PRX[114], licensed under CC BY 4.0.

## 6.2Noisy circumnutations facilitate exploration and sensing

At the macroscopic level, stochasticity manifests in the dynamics of whole organs. In motile systems, variability in motion is known to facilitate search, navigation, and active sensing, although this role remains less explored in plants. A prominent example of intrinsic, growth-driven motion in plants is circumnutation, which ranges from highly periodic movements in climbing species, where it aids in locating and assessing supports[40,84,118], to more irregular, lower-amplitude motions in non-climbing shoots, often termed nutations, whose ecological function remains less clear[98,152,7,84]. From the perspective adopted here, these movements can be viewed as macroscopic fluctuations emerging from stochastic growth processes, providing persistent perturbations to organ-level dynamics. Only recently have circumnutations begun to be recognized as playing functional roles in organismal behavior, and here we focus on two major, complementary functions: enhancing sensitivity to environmental signals and facilitating exploration in uncertain environments.

Circumnutation-driven fluctuations can contribute to sensing and postural control. In wheat coleoptiles subjected to a gravitropic perturbation (tilting the organ horizontally), oscillatory pulses of elongation and curvature, (nutations) propagate from the apex toward the base (Fig.5b)[142,12]. During the response, these oscillations become more pronounced and structured, and the resulting reorientation is faster and more tightly regulated than predicted by minimal tropic models, suggesting that they facilitate postural control.
Their role is further supported by their timescale: the oscillation period is comparable to that of the memory kernel extracted from gravitropic responses[129,29]. This suggests that oscillatory growth dynamics and temporal integration may act together, with circumnutation modulating the input and the memory kernel enabling comparison across successive phases, analogous to active sensing in other biological systems[143].
Circumnutations facilitate exploration in heterogeneous environments (Fig.5c)[156]. Wild-type roots exhibiting circumnutations are able to locate accessible paths and grow through the soil, whereas mutants lacking this motion fail to penetrate such substrates. Robophysical experiments reproduce this effect, showing that oscillatory motion introduces lateral forces that reduce trapping. Circumnutation thus acts as a mechanically mediated exploration strategy, enabling the root to sample nearby configurations rather than follow a single deterministic path.
Together, these examples illustrate how circumnutations constitute structured fluctuations that enhance both sensing and exploration at the organ scale, enabling plants to navigate complex environments and refine their responses to weak or noisy signals.

## 6.3Collective dynamics and emergent structures in interacting plants

Building on the role of stochastic fluctuations at the level of single organs, we now consider how these dynamics extend to interactions between multiple growing plants, giving rise to collective behavior and emergent structures.
Noise plays a critical role in interacting physical systems. In motile systems, such as schools of fish or flocks of birds, variability in individual motion can determine whether the group remains disordered or organizes into coherent collective movement. This behavior is captured by models of active matter, such as the Vicsek model[162,37], in which the balance between alignment interactions and noise controls transitions between disordered, clustered, and collectively moving states (Fig.5d). More broadly, fluctuations enable exploration of configuration space, facilitate transitions between states, and seed symmetry breaking in pattern-forming systems[64,63,163]. At intermediate amplitudes, noise enhances adaptability by allowing the system to explore multiple configurations, whereas too little noise traps it in suboptimal states and too much disrupts coherent dynamics.
Collective dynamics of growing plants share these principles but differ in a key aspect: growth is irreversible. Unlike motile systems, where trajectories can be reversed or rearranged, plant organs occupy space permanently as they grow. As a result, space and time become coupled, and past dynamics are encoded in the resulting three-dimensional structure. Different dynamical regimes are thus translated into distinct morphological outcomes. This is particularly evident in functional root structures and the complex architectures of climbing plants, such as trellises and braided configurations (Fig.5e). Similar principles arise in other growth-driven systems, such as fungal networks, neurons, and soft robotic structures[60,137,174].

A concrete realization of these ideas is found in the self-organized growth patterns of dense sunflower populations. Pereira et al.[121]showed that neighboring plants spontaneously adopt alternating stem inclinations, forming a zig-zag pattern driven by shade-avoidance interactions (Fig.5f). Each plant grows away from the far-red light reflected by its neighbors, effectively generating repulsive interactions that propagate along the row.
Subsequent work[114]identified circumnutations as the intrinsic source of noise in this system (Fig.5g), playing a key role in symmetry breaking and in the exploration of possible configurations. Circumnutation dynamics follow a bounded random walk with a broad distribution of velocities spanning several orders of magnitude, a hallmark of efficient exploration in biological systems. An experimentally informed Langevin-type model of interacting growing disks captures these dynamics and shows that this broad distribution corresponds to a sharp transition in the force–noise balance, facilitating exploration and leading to optimized, low-shading configurations.

Despite these advances, a general theoretical framework linking stochastic growth dynamics to emergent three-dimensional structures remains incomplete. A first step[13]extends tropic models to interacting organs, revealing a rich set of steady states and oscillatory regimes driven by deterministic coupling. Extending such approaches to include three-dimensional growth, mechanical interactions, and fluctuations is essential for capturing the full dynamics of collective growth and structure formation in plant systems.

## 7CONCLUSION

Since Darwin first invoked the metaphor of a root “brain” to account for the complex behaviors he observed, plants have challenged our understanding of how intelligence and coordination can arise without centralized control. Plants solve complex navigational and adaptive problems through a paradigm that redefines our traditional notions of agency and intelligence. The central message of this review is that these behavioral capacities are not managed by a central controller, but instead emerge from the material properties of plants and the physics of growth, suggesting that computation in living systems need not be localized in specialized organs or implemented through symbolic operations.

Through the lens of physics, plants provide a unique playground, bringing together distinct concepts, such as distributed computation, embodied mechanics, and functional stochasticity, all within a single system. Moreover, this decentralized, material form of computation is taken to its physical limit in plants: since growth simultaneously encodes information and generates motion, the processing and the response are inseparable components of the same material evolution. Consequently, development and behavior are functionally unified. This “computation-through-growth” paradigm offers a distinct alternative not only to neuromorphic models, but to current frameworks of decentralized systems; here, the material substrate is not a static processor, but an evolving structure that irreversibly reconfigures itself in response to information. This perspective raises a number of fundamental questions in condensed matter physics that remain open. At the same time, it offers a complementary perspective on a long-standing question in plant science: how coordinated, organism-level behavior emerges from distributed sensing and signaling. While this problem has largely been approached through the identification of molecular pathways and hormonal cross-talk, a physical framework may help reveal the organizing principles that link these microscopic processes to macroscopic behavior.

Looking forward, the principles of plant behavior offer a rich blueprint for decentralized technologies. Intelligent matter and adaptive materials, in which sensing and response are embedded within the material itself, remain an emerging area of research that stands to benefit from these insights. Building on this, such materials are becoming integral components of soft robotic systems, where control is distributed across the body and further shaped by embodied mechanical principles. These ideas are beginning to shape a new generation of self-organizing robotic systems, as well as plant-inspired growth-driven robots, capable of navigating and adapting to complex environments through their morphology and material dynamics. Advances in self-growing robotics may also point toward a vision of autonomous, emergent functional architectures without a predefined global design.

In this sense, some of the most compelling questions in condensed matter physics may lie not in exotic systems, but in familiar ones viewed differently, sometimes as close as the plants we pass by every day. So go out and smell the proverbial roses!{summary}

[SUMMARY POINTS]
- 1.

Plant behavior is inherently decentralized: sensing, computation, and movement emerge from the interplay between local growth rules and global mechanical constraints, allowing organisms to solve complex problems without a central controller.
- 2.

Distributed physical computation enables spatially extended tissues to encode and integrate environmental signals through transport and geometry.
- 3.

Embodied mechanical intelligence allows plants to offload aspects of control onto morphology and material properties, transforming environmental interactions into functional responses.
- 4.

Stochasticity acts as a functional resource across scales; rather than being noise to suppress, these fluctuations enhance sensitivity, enable exploration, and drive collective organization.
- 5.

In growing systems, computation and movement are inseparable: growth simultaneously processes information and generates movement.{issues}

[FUTURE ISSUES]
- 1.

How does molecular signaling translate into organism-level action? Establishing the multiscale transfer functions that map microscopic processes to tissue-scale strain and growth remains a significant challenge for a predictive physics of plant behavior.
- 2.

How is information about past stimuli stored and encoded in the evolving material properties of the plant? Identifying these physical substrates of memory is essential for understanding computation in non-neural matter.
- 3.

Can we learn about the physical basis of learning in decentralized systems from plants? While plants exhibit sophisticated adaptive behaviors, the mechanisms by which they modify their responses based on past experience remain largely unexplored.
- 4.

How do the concepts of physical computation, embodied mechanics, and functional noise, often studied as distinct fields, interact within a single system? Investigating the trade-offs and synergies between mechanical constraints that shape signal transport and stochastic fluctuations that drive exploration is necessary for a unified theory of decentralized behavior.
- 5.

Can plants serve as a physical laboratory for studying autonomous, evolving matter? In particular, can we leverage systems in which sensing, computation, and movement are integrated within a single material to develop a broader physics of decentralized, adaptive systems?

## DISCLOSURE STATEMENT

The authors are not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review.

## ACKNOWLEDGMENTS

We are grateful to the many people who have shaped our understanding and appreciation of computation and behavior in plants over years of interactions, several of whom also provided feedback on a draft of this article. A partial list must include Renaud Bastien, Bruno Moulia, Dan Goldman, L. Mahadevan, Alain Goriely, Andrea Liu, Eilon Shani, Yoav Lahini, Orit Peleg, Nahi Stern, Jean-François Louf, Yoël Forterre, Ben Maoz, and of course all of the students who have been part an integral part of the research done in the lab. We also thank Barak Hadad who helped desig beautiful figures.
Y.M. acknowledges support from the Israel Science Foundation Research Grant (ISF) no. 2307/22, and ERC grant GROWsmart 101165101.

## References
- [1]D. Agostinelli, A. Lucantonio, G. Noselli, and A. DeSimone(2020)Nutations in growing plant shoots: the role of elastic deformations due to gravity loading.Journal of the Mechanics and Physics of Solids136,pp. 103702.Cited by:§4.2.
- [2]J. Aguilar, T. Zhang, F. Qian, M. Kingsbury, B. McInroe, N. Mazouchova, C. Li, R. Maladen, C. Gong, M. Travers, R. L. Hatton, H. Choset, P. B. Umbanhowar, and D. I. Goldman(2016)A review on locomotion robophysics: the study of movement at the intersection of robotics, soft matter and dynamical systems.Reports on Progress in Physics79(11),pp. 110001.Cited by:§4.
- [3]J. Aguilar, T. Zhang, F. Qian, M. Kingsbury, B. McInroe, N. Mazouchova, C. Li, R. Maladen, C. Gong, M. Travers,et al.(2016)A review on locomotion robophysics: the study of movement at the intersection of robotics, soft matter and dynamical systems.Reports on Progress in Physics79(11),pp. 110001.Cited by:§4.
- [4]T. Ahamed, A. C. Costa, and G. J. Stephens(2021)Capturing the continuous complexity of behaviour in caenorhabditis elegans.Nature Physics17(2),pp. 275–283.Cited by:§3.1.
- [5]V. R. Anisetti, B. Scellier, and J. M. Schwarz(2023)Learning by non-interfering feedback chemical signaling in physical networks.Physical Review Research5(2),pp. 023024.Cited by:§3.
- [6]S. Armon, M. Moshe, and E. Sharon(2021)The multiscale nature of leaf growth fields.Communications physics4(1),pp. 122.Cited by:§5.
- [7]L. Baillaud(1962)Mouvements autonomes des tiges, vrilles et autres organes à l’exception des organes volubiles et des feuilles.Physiology of Movements/Physiologie der Bewegungen: Part 2: Movements due to the Effects of Temperature, Gravity, Chemical Factors and Internal Factors/Teil2: Bewegungen durch Einflüsse der Temperatur, Schwerkraft, Chemischer Faktoren und aus Inneren Ursachen,pp. 562–634.Cited by:§6.2.
- [8]Y. Bar-Sinai, J. Julien, E. Sharon, S. Armon, N. Nakayama, M. Adda-Bedia, and A. Boudaoud(2016)Mechanical stress induces remodeling of vascular networks in growing leaves.PLoS computational biology12(4),pp. e1004819.Cited by:§3,§5.
- [9]R. Bastien, T. Bohr, B. Moulia, and S. Douady(2013-01)Unifying model of shoot gravitropism reveals proprioception as a central feature of posture control in plants.Proceedings of the National Academy of Sciences of the United States of America110,pp. 755–760.Cited by:Figure 1,Figure 2,Figure 2,Figure 2,§2.2,§2.2,§2.2,§2.2,§2.3,§2.3,§2.3.
- [10]R. Bastien, S. Douady, and B. Moulia(2014)A unifying modeling of plant shoot gravitropism with an explicit account of the effects of growth.Frontiers in plant science5,pp. 136.Cited by:§2.2,§2.2.
- [11]R. Bastien, S. Douady, and B. Moulia(2015)A unified model of shoot tropism in plants: photo-, gravi-and propio-ception.PLoS computational biology11(2),pp. e1004037.Cited by:§2.2,§2.2,§2.2,§3.2.
- [12]R. Bastien, O. Guayasamin, S. Douady, and B. Moulia(2018-03)Coupled ultradian growth and curvature oscillations during gravitropic movement in disturbed wheat coleoptiles.PLOS ONE13(3),pp. e0194893(en).Note:Publisher: Public Library of ScienceExternal Links:ISSN 1932-6203,Link,DocumentCited by:Figure 5,§6.2.
- [13]R. Bastien, A. Porat, and Y. Meroz(2019)Towards a framework for collective behavior in growth-driven systems, based on plant-inspired allotropic pairwise interactions.Bioinspiration & Biomimetics14(5),pp. 055004.Cited by:§6.3.
- [14]D. N. Beal, F. S. Hover, M. S. Triantafyllou, J. C. Liao, and G. V. Lauder(2006)Passive propulsion in vortex wakes.Journal of fluid mechanics549,pp. 385–402.Cited by:Figure 4,§4.
- [15]G. J. Berman(2018)Measuring behavior across scales.BMC biology16(1),pp. 23.Cited by:§3.1.
- [16]K. Bertoldi, V. Vitelli, J. Christensen, and M. Van Hecke(2017)Flexible mechanical metamaterials.Nature Reviews Materials2(11),pp. 1–11.Cited by:§4.
- [17]A. Bérut, H. Chauvet, V. Legué, B. Moulia, O. Pouliquen, and Y. Forterre(2018)Gravisensors in plant cells behave like an active granular liquid.PNAS115,pp. 5123–5128.Cited by:Figure 1,§2.1,§3.3,Figure 5,§6.1.
- [18]K. Bhattacharyya, D. Zwicker, and K. Alim(2022)Memory formation in adaptive networks.Physical Review Letters129(2),pp. 028101.Cited by:§3.
- [19]F. Bizet, A. G. Bengough, I. Hummel, M. Bogeat-Triboulot, and L. X. Dupuy(2016)3D deformation field in growing plant roots reveals both mechanical and biological responses to axial mechanical forces.Journal of Experimental Botany67(19),pp. 5605–5614.Cited by:Figure 4,§4.1.
- [20]A.H. Blaauw(1909)Die perzeption des lichtes.Recueil Trav. Bot. Neerland.5,pp. 209–372.Cited by:§3.1.
- [21]S. M. Block(1992)Biophysical principles of sensory transduction.Sensory transduction1,pp. 91–117.Cited by:§3.2.
- [22]J. Böhm, S. Scherzer, E. Krol, I. Kreuzer, K. Von Meyer, C. Lorey, T. D. Mueller, L. Shabala, I. Monte, R. Solano,et al.(2016)The venus flytrap dionaea muscipula counts prey-induced action potentials to induce sodium uptake.Current Biology26(3),pp. 286–295.Cited by:§3.1.
- [23]J. Bouchaud(1992)Weak ergodicity breaking and aging in disordered systems.Journal de Physique I2(9),pp. 1705–1713.Cited by:§6.
- [24]A. Bressan, M. Palladino, and W. Shen(2017)Growth models for tree stems and vines.Journal of Differential Equations263(4),pp. 2280–2316.Cited by:§2.2,§4.2.
- [25]W. R. Briggs(1960-11)Light Dosage and Phototropic Responses of Corn and Oat Coleoptiles..PLANT PHYSIOLOGY35(6),pp. 951–962.Cited by:§3.1.
- [26]W.R. Briggs and J.M. Christie(2002)Phototropin 1 and phototropin 2: Two versatile plant blue-light receptors.Trends Plant Sci.7,pp. 204–209.Cited by:§2.1.
- [27]R. Bunsen and H.E. Roscoe(1957)Photochemical researches.Phil. Trans. Roy. Soc. London147,pp. 355–380.Cited by:§3.1.
- [28]N. E. Bush, S. A. Solla, and M. J. Hartmann(2016)Whisking mechanics and active sensing.Current Opinion in Neurobiology40,pp. 178–188.External Links:ISSN 0959-4388,DocumentCited by:§4.3.
- [29]H. Chauvet, B. Moulia, V. Legué, Y. Forterre, and O. Pouliquen(2019)Revealing the hierarchy of processes and time-scales that control the tropic response of shoots to gravi-stimulations.Journal of Experimental Botany70(6),pp. 1955–1967.Cited by:§3.1,§3.3,§6.1,§6.2.
- [30]H. Chauvet, O. Pouliquen, Y. Forterre, V. Legué, and B. Moulia(2016)Inclination not force is sensed by plants during shoot gravitropism.Scientific reports6(1),pp. 1–8.Cited by:§2.1,§2.2.
- [31]R. Chelakkot and L. Mahadevan(2017-03)On the growth and form of shoots.Journal of The Royal Society Interface14(128),pp. 20170001.Cited by:§4.2.
- [32]J. M. Christie(2007)Phototropin blue light receptors.Annual Review of Plant Biology58,pp. 21–45.External Links:DocumentCited by:§2.1.
- [33]S. Collins, A. Ruina, R. Tedrake, and M. Wisse(2005)Efficient bipedal robots based on passive-dynamic walkers.Science307(5712),pp. 1082–1085.Cited by:Figure 4,§4.
- [34]C. Coulais, C. Kettenis, and M. van Hecke(2018)A characteristic length scale causes anomalous size effects and boundary programmability in mechanical metamaterials.Nature Physics14(1),pp. 40–44.Cited by:§4.
- [35]C. Coulais, A. Sabbadini, F. Vink, and M. van Hecke(2018)Multi-step self-guided pathways for shape-changing metamaterials.Nature561(7724),pp. 512–515.Cited by:§4.
- [36]C. Coutand, B. Adam, S. Ploquin, and B. Moulia(2019)A method for the quantification of phototropic and gravitropic sensitivities of plants combining an original experimental device with model-assisted phenotyping: exploratory test of the method on three hardwood tree species.PLoS One14(1),pp. e0209973.Cited by:§2.2.
- [37]I.D. Couzin, J. Krause, R. James, G.D. Ruxton, and N.R. Franks(2002)Collective memory and spatial sorting in animal groups..Journal of Theoretical Biology218,pp. 1–11.Cited by:Figure 5,§6.3.
- [38]N. J. Cowan, M. M. Ankarali, J. P. Dyhr, M. S. Madhav, E. Roth, S. Sefati, S. Sponberg, S. A. Stamper, E. S. Fortune, and T. L. Daniel(2014)Feedback control as a framework for understanding tradeoffs in biology.American Zoologist54(2),pp. 223–237.Cited by:§3.1,§3.1.
- [39]P. A. Crisp, D. Ganguly, S. R. Eichten, J. O. Borevitz, and B. J. Pogson(2016)Reconsidering plant memory: intersections between stress recovery, rna turnover, and epigenetics.Science Advances2(2),pp. e1501340.External Links:DocumentCited by:§3.1.
- [40]C. Darwin(1880)The Power of Movement in Plants..London: John Murray Publishers.Cited by:§1,§2.1,§2,§6.2.
- [41]S. G. Das, J. Krug, and M. Mungan(2022)Driven disordered systems approach to biological evolution in changing environments.Physical Review X12(3),pp. 031040.Cited by:§3.
- [42]P. G. de Gennes(2004)Chemotaxis: the role of internal delays..Eur Biophys J.33(8),pp. 691–3.Cited by:§3.1.
- [43]M. B. Elowitz, A. J. Levine, E. D. Siggia, and P. S. Swain(2002)Stochastic gene expression in a single cell.Science297(5584),pp. 1183–1186.Cited by:§6.
- [44]H. Fitting(1905)Untersuchungen über den geotropischen Reizvorgang. Teil I. Die geotropische Empfindlichkeit der Pflanzen. Teil II. Weitere Erfolge mit der intermittierenden Reizung...Jahrbücher für Wissenschaftliche Botanik41,pp. 221–330, 331–398.Cited by:§3.1.
- [45]Y. Forterre(2013)Slow, fast and furious: understanding the physics of plant movements.Journal of experimental botany64(15),pp. 4745–4760.Cited by:§1.
- [46]K. A. Franklin and G. C. Whitelam(2004)Light signals, phytochromes and cross‐talk with other environmental cues.Journal of Experimental Botany55(395),pp. 271–276.External Links:ISSN 0022-0957,DocumentCited by:§2.1.
- [47]P. Fröschel(1908)Unterzuchungen über die heliotropische präzentationszeit. i sitzber mathnaturwiss.Kl Kais Akad Wiss107,pp. 235–256.Cited by:§3.1.
- [48]M. Furutani and M. T. Morita(2021)LAZY1-like-mediated gravity signaling pathway in root gravitropic set-point angle control.Plant Physiology187(3),pp. 1087–1095.Cited by:§2.1.
- [49]M. Gazzola, L. Dudte, A. McCormick, and L. Mahadevan(2018)Forward and inverse problems in the mechanics of soft filaments.Royal Society Open Science5(6).Cited by:§4.2.
- [50]S. Gilroy(2008)Plant tropisms.Current Biology18(7),pp. R275–R277.Cited by:§2.
- [51]C. P. Goodrich, A. J. Liu, and S. R. Nagel(2015)The principle of independent bond-level response: tuning by pruning to exploit disorder for global behavior.Physical review letters114(22),pp. 225501.Cited by:§3.
- [52]A. Goriely and S. Neukirch(2006-11)Mechanics of climbing and attachment in twining plants.Physical Review Letters97(18).External Links:ISSN 1079-7114,Link,DocumentCited by:§4.3.
- [53]A. Goriely(2017)The Mathematics and Mechanics of Biological Growth.Springer.Cited by:§2.2,§4.2.
- [54]A. Goyal, E. Karayekov, V. C. Galvão, H. Ren, J. J. Casal, and C. Fankhauser(2016)Shade promotes phototropism through phytochrome b-controlled auxin production.Current Biology26(24),pp. 3280–3287.Cited by:§2.1.
- [55]V. A. Grieneisen, J. Xu, A. F. Marée, P. Hogeweg, and B. Scheres(2007)Auxin transport is sufficient to generate a maximum and gradient guiding root growth.Nature449(7165),pp. 1008–1013.Cited by:§2.2.
- [56]T. Guillon, Y. Dumont, and T. Fourcaud(2012)A new mathematical framework for modelling the biomechanics of growing trees with rod theory.Mathematical and Computer Modelling55(9-10),pp. 2061–2077.Cited by:§2.2,§4.2.
- [57]K. Guo, Y. Zhang, M. Paradiso, Y. Long, K. J. Hsia, and M. Liu(2025)Midveins regulate the shape formation of drying leaves.Journal of the Mechanics and Physics of Solids,pp. 106391.Cited by:§5.
- [58]H. Han, M. Adamowski, L. Qi, S. S. Alotaibi, and J. Friml(2021)PIN-mediated polar auxin transport regulations in plant tropic responses.New Phytologist232(2),pp. 510–522.Cited by:§2.1.
- [59]S. L. Harmer and C. J. Brooks(2018)Growth-mediated plant movements: hidden in plain sight.Current opinion in plant biology41,pp. 89–94.Cited by:§2.
- [60]E. W. Hawkes, L. H. Blumenschein, J. D. Greer, and A. M. Okamura(2017)A soft robot that navigates its environment through growth.Science Robotics2(8).External Links:DocumentCited by:§6.3.
- [61]D. G. Heathcote, A. H. Brown, and D. K. Chapman(1995-01)The phototropic response of Triticum aestivum coleoptiles under conditions of low gravity.Plant, Cell and Environment18(1),pp. 53–60.Cited by:§3.1.
- [62]M. G. Heisler and H. Jönsson(2006)Modeling auxin transport and plant development: heisler and jönsson.Journal of Plant Growth Regulation25(4),pp. 302–312.Cited by:§2.2.
- [63]D. Helbing and T. Płatkowski(2002)Drift- or fluctuation-induced ordering and self-organization in driven many-particle systems.EPL60,pp. 227.Cited by:§6.3.
- [64]D. Helbing and T. Vicsek(1999)Optimal self-organization.New J. Phys.1,pp. 13.Cited by:§6.3.
- [65]D. Hexner, A. J. Liu, and S. R. Nagel(2018)Role of local response in manipulating the elastic properties of disordered solids by bond removal.Soft matter14(2),pp. 312–318.Cited by:§3.
- [66]M. Hilker and T. Schmülling(2019)Stress priming, memory, and signaling in plants.Plant, Cell & Environment42(3),pp. 753–761.External Links:DocumentCited by:§3.1.
- [67]J. J. Hopfield(1982)Neural networks and physical systems with emergent collective computational abilities..Proceedings of the national academy of sciences79(8),pp. 2554–2558.Cited by:§3.
- [68]L. A. Huet, H. M. Emnett, and M. J. Z. Hartmann(2022-09)Demonstration of three-dimensional contact point determination and contour reconstruction during active whisking behavior of an awake rat.PLOS Computational Biology18(9),pp. e1007763.External Links:Document,LinkCited by:Figure 4,§4.3.
- [69]M. Iino(2001)Phototropism: mechanisms and ecological implications.Plant, Cell & Environment24(1),pp. 31–48.External Links:DocumentCited by:§2.2,§3.1.
- [70]S. Inoue, T. Kinoshita, A. Takemiya, M. Doi, and K. Shimazaki(2008)Blue light induced autophosphorylation of phototropin is a primary step in phototropism.Proceedings of the National National Academy of Sciences USA105(1),pp. 562–567.External Links:DocumentCited by:§2.1.
- [71]S. Isnard and W. K. Silk(2009-07)Moving with climbing plants from charles darwin’s time into the 21st century.American Journal of Botany96(7),pp. 1205–1221.External Links:ISSN 1537-2197,Link,DocumentCited by:§4.3.
- [72]M. K. Jawed, F. Da, J. Joo, E. Grinspun, and P. M. Reis(2014)Coiling of elastic rods on rigid substrates.Proceedings of the National Academy of Sciences111(41),pp. 14663–14668.Cited by:§4.2.
- [73]A. Johnsson, A. H. Brown, D. K. Chapman, D. Heathcote, and C. Karlsson(1995-01)Gravitropic responses of the Avena coleoptile in space and on clinostats. II. Is reciprocity valid?.Physiologia Plantarum95(1),pp. 34–38.Cited by:§3.1.
- [74]A. Johnsson, C. Karlsson, T. Iversen, and D. K. Chapman(1996-02)Random root movements in weightlessness.Physiologia Plantarum96(2),pp. 169–178.Cited by:§3.1.
- [75]C. L. Kane and T. C. Lubensky(2014)Topological boundary modes in isostatic lattices.Nature Physics10(1),pp. 39–45.Cited by:§4.
- [76]H. Kataoka(1979-06)Phototropic Responses of Vaucheria geminata to Intermittent Blue Light Stimuli..PLANT PHYSIOLOGY63(6),pp. 1107–1110.Cited by:§3.1.
- [77]E. Katifori, G. J. Szöllősi, and M. O. Magnasco(2010)Damage and fluctuations induce loops in optimal transport networks.Physical review letters104(4),pp. 048704.Cited by:§3.
- [78]N. C. Keim and S. R. Nagel(2011)Generic transient memory formation in disordered systems with noise.Physical review letters107(1),pp. 010603.Cited by:§3.
- [79]N. C. Keim, J. D. Paulsen, Z. Zeravcic, S. Sastry, and S. R. Nagel(2019)Memory formation in matter.Reviews of Modern Physics91(3),pp. 035002.Cited by:§3,§6.
- [80]A. Kempinski, A. Porat, M. Riviére, and Y. Meroz(2026)Nonlinear distributed sensing of light patterns underlies perceptual distortions in plants.BioRxiv.Cited by:§2.2,§2.2,Figure 3,§3.2,§3.2,§3.3.
- [81]F. Klimm, T. Speck, and M. Thielen(2023-08)Force generation in the coiling tendrils of passiflora caerulea.Advanced Science10(28).External Links:ISSN 2198-3844,Link,DocumentCited by:§4.3.
- [82]Y. Koren, A. Perilli, O. Tchaicheeyan, A. Lesman, and Y. Meroz(2024)Analysis of root-environment interactions reveals mechanical advantages of growth-driven penetration of roots.Plant, Cell & Environment47(12),pp. 5076–5088.Cited by:§4.1.
- [83]M. Kramar and K. Alim(2021)Encoding memory in tube diameter hierarchy of living flow network.Proceedings of the National Academy of Sciences118(10),pp. e2007815118.Cited by:§3.
- [84]K. C. Larson(2000)Circumnutation behavior of an exotic honeysuckle vine and its native congener: influence on clonal mobility.American Journal of Botany87(4),pp. 533–538.Cited by:§6.2.
- [85]N. Leblanc-Fournier, L. Martin, C. Lenne, and M. Decourteix(2014)To respond or not to respond, the recurring question in plant mechanosensitivity.Frontiers in Plant Science5,pp. 401.Cited by:§3.1.
- [86]J. C. Liao, D. N. Beal, G. V. Lauder, and M. S. Triantafyllou(2003)Fish exploiting vortices decrease muscle activity.Science302(5650),pp. 1566–1569.Cited by:§4.
- [87]E. D. Lipson(1975-10)White noise analysis of phycomyces light growth response system. i. normal intensity range..Biophysical Journal15(10),pp. 989.Cited by:§3.1.
- [88]E. Liscum, S. K. Askinosie, D. L. Leuchtman, J. Morrow, K. T. Willenburg, and D. R. Coats(2014)Phototropism: growing towards an understanding of plant movement.Plant Cell26(1),pp. 38–55.External Links:DocumentCited by:§2.1.
- [89]J. A. Lockhart(1965)An analysis of irreversible plant cell elongation.Journal of theoretical biology8(2),pp. 264–275.Cited by:§4.1.
- [90]J. Louf, G. Guéna, E. Badel, and Y. Forterre(2017)Universal poroelastic mechanism for hydraulic signals in biomimetic and natural branches.Proceedings of the National Academy of Sciences114(42),pp. 11034–11039.Cited by:§3.2.
- [91]A. Maitra and S. Ramaswamy(2019)Oriented active solids.Physical review letters123(23),pp. 238001.Cited by:§4.
- [92]M. C. Marchetti, J. Joanny, S. Ramaswamy, T. B. Liverpool, J. Prost, M. Rao, and R. A. Simha(2013)Hydrodynamics of soft active matter.Reviews of modern physics85(3),pp. 1143–1189.Cited by:§4.
- [93]L. Martin, N. Leblanc-Fournier, J. Julien, B. Moulia, and C. Coutand(2010)Acclimation kinetics of physiological and molecular responses of plants to multiple mechanical loadings.Journal of Experimental Botany61(9),pp. 2403–2412.Cited by:§3.1.
- [94]A. D. Martins, F. O’callaghan, A. G. Bengough, K. W. Loades, M. Pasqual, E. Kolb, and L. X. Dupuy(2020)The helical motions of roots are linked to avoidance of particle forces in soil.The New Phytologist225(6),pp. 2356–2367.Cited by:§4.1.
- [95]T. McGeeret al.(1990)Passive dynamic walking.Int. J. Robotics Res.9(2),pp. 62–82.Cited by:§4.
- [96]Y. Meroz, R. Bastien, and L. Mahadevan(2019)Spatio-temporal integration in plant tropisms.Journal of the Royal Society Interface16(154),pp. 20190038.Cited by:§3.1,§3.1,§6.1.
- [97]R. Metzler and J. Klafter(2000)The random walk’s guide to anomalous diffusion: a fractional dynamics approach.Physics reports339(1),pp. 1–77.Cited by:§6.
- [98]F. Migliaccio, P. Tassone, and A. Fortunati(2013)Circumnutation as an autonomous root movement in plants.American Journal of Botany100(1),pp. 4–13.External Links:Document,Link,https://bsapubs.onlinelibrary.wiley.com/doi/pdf/10.3732/ajb.1200314Cited by:§6.2.
- [99]A. K. Mishra, F. Tramacere, R. Guarino, N. M. Pugno, and B. Mazzolai(2018)A study on plant root apex morphology as a model for soft robots moving in soil.PLoS One13(6),pp. e0197411.Cited by:§4.1.
- [100]M. T. Morita(2010)Directional gravity sensing in gravitropism.Annual Review of Plant Biology61,pp. 705–720.External Links:DocumentCited by:§2.1,§3.3.
- [101]B. Moulia, C. Der Loughian, R. Bastien, O. Martin, M. Rodríguez, D. Gourcilleau, A. Barbacci, E. Badel, G. Franchel, C. Lenne, P. Roeckel-Drevet, J. M. Allain, J. M. Frachisse, E. de Langre, C. Coutand, N. Fournier-Leblanc, and J. L. Julien(2011-06)Integrative Mechanobiology of Growth and Architectural Development in Changing Mechanical Environments.InMechanical Integration of Plant Cells and Plants,P. Wojtaszek (Ed.),pp. 269–302.Cited by:§3.2.
- [102]B. Moulia, E. Badel, R. Bastien, L. Duchemin, and C. Eloy(2022)The shaping of plant axes and crowns through tropisms and elasticity: an example of morphogenetic plasticity beyond the shoot apical meristem.New Phytologist233(6),pp. 2354–2379.Cited by:§2.1.
- [103]B. Moulia, R. Bastien, H. Chauvet-Thiry, and N. Leblanc-Fournier(2019)Posture control in land plants: growth, position sensing, proprioception, balance, and elasticity.Journal of Experimental Botany70(14),pp. 3467–3494.Cited by:§2.2,§2.3.
- [104]B. Moulia, C. Coutand, and J. Julien(2015)Mechanosensitive control of plant growth: bearing the load, sensing, transducing, and responding.Frontiers in plant science6,pp. 52.Cited by:§3.1.
- [105]B. Moulia, S. Douady, and O. Hamant(2021)Fluctuations shape plants through proprioception.Science372(6540),pp. eabc6868.Cited by:§6.1.
- [106]B. Moulia and M. Fournier(2009)The power and control of gravitropic movements in plants: a biomechanical and systems biology view.Journal of experimental botany60(2),pp. 461–486.Cited by:§2.2,§2.
- [107]D. E. Moulton, H. Oliveri, and A. Goriely(2020)Multiscale integration of environmental stimuli in plant tropism produces complex behaviors.Proceedings of the National Academy of Sciences117(51),pp. 32226–32237.Cited by:§2.2,§2.2,§2.
- [108]D. E. Moulton, T. Lessinnes, and A. Goriely(2020)Morphoelastic rods III: differential growth and curvature generation in elastic filaments.Journal of the Mechanics and Physics of Solids142,pp. 104022.External Links:ISSN 0022-5096,Document,LinkCited by:§2.2.
- [109]S. R. Nagel, S. Sastry, Z. Zeravcic, and M. Muthukumar(2023)Memory formation.The Journal of Chemical Physics158(21).Cited by:§3.
- [110]M. Nakamura, T. Nishimura, and M. T. Morita(2019)Gravity sensing and signal conversion in plant gravitropism.Journal of experimental botany70(14),pp. 3495–3506.Cited by:§3.3.
- [111]A. Nathansohn and E. Pringseheim(1908)Uber die summation intermittierren der lichtreize..Jahrb Wiss Bot45,pp. 137–190.Cited by:§3.1.
- [112]G. M. Nawkar, M. Legris, A. Goyal, E. Schmid-Siegert, J. Fleury, A. Mucciolo, D. D. Bellis, M. Trevisan, A. Schueler, and C. Fankhauser(2023)Air channels create a directional light signal to regulate hypocotyl phototropism.Science382(6673),pp. 935–940.External Links:Document,Link,https://www.science.org/doi/pdf/10.1126/science.adh9384Cited by:§2.2.
- [113]C. NG(1927)Wuchshormone und tropismen bei den pflanzen.Biol Zentralbl47,pp. 604–626.Cited by:§2.1.
- [114]C. Nguyen, I. Dromi, A. Kempinski, G. E. Gall, O. Peleg, and Y. Meroz(2024)Noisy circumnutations facilitate self-organized shade avoidance in sunflowers.Physical Review X14(3),pp. 031027.Cited by:Figure 5,§6.3.
- [115]K. Nishikawa, A. A. Biewener, P. Aerts, A. N. Ahn, H. J. Chiel, M. A. Daley, T. L. Daniel, R. J. Full, M. E. Hale, T. L. Hedrick,et al.(2007)Neuromechanics: an integrative approach for understanding motor control.Integrative and comparative biology47(1),pp. 16–54.Cited by:§4.
- [116]K. H. Norwich and W. Wong(1997)Unification of psychophysical phenomena: the complete form of fechner’s law.Perception & Psychophysics59(6),pp. 929–940.Cited by:§3.2.
- [117]A. Ohad and Y. Meroz(2025)Camera-based bi-axial measurement of weak forces generated by freely moving plant organs.Journal of Experimental Botany,pp. eraf476.Cited by:Figure 4.
- [118]A. Ohad, A. Porat, and Y. Meroz(2026)Embodied mechanical sensing drives support selection in twining plants.Cited by:§4.3,§6.2.
- [119]H. Oliveri, D. E. Moulton, H. A. Harrington, and A. Goriely(2024)Active shape control by plants in dynamic environments.Physical Review E110(1),pp. 014405.Cited by:§2.3.
- [120]O. Peleg and L. Mahadevan(2016)Optimal switching between geocentric and egocentric strategies in navigation.Royal Society Open Science3(7),pp. 160128.External Links:DocumentCited by:§6.
- [121]M. L. Pereira, V. O. Sadras, W. Batista, J. J. Casal, and A. J. Hall(2017)Light-mediated self-organization of sunflower stands increases oil yield in the field.Proceedings of the National Academy of Sciences114(30),pp. 7975–7980.Cited by:Figure 5,§6.3.
- [122]W. Pfeffer(1940)Kinematographische studien an impatiens, vicia, tulipa, mimosa und desmodium von w. pfeffer (1898-1900).Note:Reichsanstalt für Film und Bild in Wissenschaft und Unterricht (RWU)https://doi.org/10.3203/IWF/B-450External Links:Document,LinkCited by:Figure 2.
- [123]R. Pfeifer, M. Lungarella, and F. Iida(2007)Self-organization, embodiment, and biologically inspired robotics.science318(5853),pp. 1088–1093.Cited by:§4.
- [124]B. G. Pickard(1973)Geotropic response patterns of the Avena coleoptile. II. Induction at low temperature.Canadian Journal of Botany51,pp. 1023–1027.Cited by:§3.1.
- [125]A. Porat, F. Tedone, M. Palladino, P. Marcati, and Y. Meroz(2020)A general 3d model for growth dynamics of sensory-growth systems: from plants to robotics.Frontiers in Robotics and AI7,pp. 89.Cited by:§2.2.
- [126]A. Porat, A. Tekinalp, Y. Bhosale, M. Gazzola, and Y. Meroz(2024)On the mechanical origins of waving, coiling and skewing in arabidopsis thaliana roots.Proceedings of the National Academy of Sciences121(11),pp. e2312761121.Cited by:Figure 4,§4.2,§4.2.
- [127]H. V. Prentice-Mott, Y. Meroz, A. Carlson, M. A. Levine, M. W. Davidson, D. Irimia, G. T. Charras, L. Mahadevan, and J. V. Shah(2016)Directional memory arises from long-lived cytoskeletal asymmetries in polarized chemotactic cells.Proceedings of the National Academy of Sciences of the United States of America113(5),pp. 1267–1272.Cited by:§3.1.
- [128]H. Rakusová, M. Abbas, H. Han, S. Song, H. S. Robert, and J. Friml(2016)Termination of shoot gravitropic responses by auxin feedback on pin3 polarity.Current Biology26(22),pp. 3026–3032.Cited by:§3.3.
- [129]M. Rivière and Y. Meroz(2023)Plants sum and subtract stimuli over different timescales.Proceedings of the National Academy of Sciences120(42),pp. e2306655120.External Links:DocumentCited by:Figure 3,§3.1,§3.1,§3.1,§6.2.
- [130]J. W. Rocks, N. Pashine, I. Bischofberger, C. P. Goodrich, A. J. Liu, and S. R. Nagel(2017)Designing allostery-inspired response in mechanical networks.Proceedings of the National Academy of Sciences114(10),pp. 2520–2525.Cited by:§3.
- [131]E. D. Rogers, D. Monaenkova, M. Mijar, A. Nori, D. I. Goldman, and P. N. Benfey(2016)X-ray computed tomography reveals the response of root system architecture to soil texture.Plant Physiology171(3),pp. 2028–2040.Cited by:§4.1.
- [132]H. Ronellenfitsch and E. Katifori(2019)Phenotypes of vascular flow networks.Physical review letters123(24),pp. 248101.Cited by:§3.
- [133]J. Roué, H. Chauvet, N. Brunel-Michac, F. Bizet, B. Moulia, E. Badel, and V. Legué(2019-11)Root cap size and shape influence responses to the physical strength of the growth medium in Arabidopsis thaliana primary roots.Journal of Experimental Botany71(1),pp. 126–137.External Links:ISSN 0022-0957,Document,Link,https://academic.oup.com/jxb/article-pdf/71/1/126/31550099/erz418.pdfCited by:§4.1.
- [134]N. P. Rowe and T. Speck(2014-10)Stem biomechanics, strength of attachment, and developmental plasticity of vines and lianas.Wiley.External Links:ISBN 9781118392409,Link,DocumentCited by:§4.3.
- [135]J. Sachs(1874)Lehrbuch der botanik.Engelmann.Cited by:§2.1.
- [136]J. Sachs(1882)Über orthotrope und plagiotrope pflanzentheile.Arb. Bot. Inst. Wurzburg2,pp. 226–284.Cited by:§2.2.
- [137]A. Sadeghi, A. Mondini, and B. Mazzolai(2017-09)Toward Self-Growing Soft Robots Inspired by Plant Roots and Based on Additive Manufacturing Technologies.Soft Robotics4(3),pp. 211–223.Cited by:§6.3.
- [138]M. Sahaf and E. Sharon(2016)The rheology of a growing leaf: stress-induced changes in the mechanical properties of leaves.Journal of experimental botany67(18),pp. 5509–5515.Cited by:§5.
- [139]M. Sahaf and E. Sharon(2020)Giant fluctuations in strain rate as part of normal leaf growth..The European Physical Journal Plus135(10),pp. 836.Cited by:§5.
- [140]T. Sakai, T. Kagawa, M. Kasahara, T. E. Swartz, J. M. Christie, W. R. Briggs, M. Wada, and K. Okada(2001)Arabidopsis nph1 and npl1: blue light receptors that mediate both phototropism and chloroplast relocation.Proceedings of the National Academy of Sciences98(12),pp. 6969–6974.Cited by:§2.2.
- [141]N. Schramma, C. Perugachi Israëls, and M. Jalaal(2023)Chloroplasts in plant cells show active glassy behavior under low-light conditions.Proceedings of the National Academy of Sciences120(3),pp. e2216497120.Cited by:§5.
- [142]J. Schuster and W. Engelmann(1997)Circumnutations of arabidopsis thaliana seedlings.Biological Rhythm Research28(4),pp. 422–440.External Links:DocumentCited by:§6.2.
- [143]J. E. Segall, S. M. Block, and H. C. Berg(1986)Temporal comparisons in bacterial chemotaxis..Proceedings of the National Academy of Sciences83(23),pp. 8987–8991.Cited by:§3.1,§6.2.
- [144]J. L. Silverberg, R. D. Noar, M. S. Packer, M. J. Harrison, C. L. Henley, I. Cohen, and S. J. Gerbode(2012-10)3D imaging and mechanical modeling of helical buckling in Medicago truncatula plant roots.Proceedings of the National Academy of Sciences of the United States of America109,pp. 16794–16799.Cited by:§4.1.
- [145]A. A. Sipos and P. L. Várkonyi(2022)A unified morphoelastic rod model with application to growth-induced coiling, waving, and skewing of plant roots.Journal of the Mechanics and Physics of Solids160,pp. 104789.Cited by:§4.2.
- [146]C. U. M. Smith(2008)Biology of sensory systems.John Wiley & Sons.Cited by:§3.2.
- [147]D. R. Smyth(2016)Helical growth in plant organs: mechanisms and significance.Development143(18),pp. 3272–3282.Cited by:§2.
- [148]M. Stern, D. Hexner, J. W. Rocks, and A. J. Liu(2021)Supervised learning in physical networks: from machine learning to learning machines.Physical Review X11(2),pp. 021045.Cited by:§3.
- [149]M. Stern and A. Murugan(2023)Learning without neurons in physical systems.Annual Review of Condensed Matter Physics14(1),pp. 417–441.Cited by:§3.
- [150]M. Stern, M. B. Pinson, and A. Murugan(2020)Continual learning of multiple memories in mechanical networks.Physical Review X10(3),pp. 031044.Cited by:§3.
- [151]S. S. Stevens(1957)On the psychophysical law..Psychological review64(3),pp. 153.Cited by:§3.2.
- [152]M. Stolarz(2009)Circumnutation as a visible plant action and reaction.Plant Signaling & Behavior4(5),pp. 380–387.External Links:DocumentCited by:§6.2.
- [153]A. K. Strohm, K. L. Baldwin, and P. H. Masson(2012)Gravity sensing and signaling in plants.Journal of Experimental Botany63(11),pp. 3747–3755.External Links:DocumentCited by:§2.1.
- [154]H. Suda, H. Mano, M. Toyota, K. Fukushima, T. Mimura, I. Tsutsui, R. Hedrich, Y. Tamada, and M. Hasebe(2020)Calcium dynamics during trap closure visualized in transgenic venus flytrap.Nature Plants6(10),pp. 1219–1224.Cited by:§3.1.
- [155]S. Sullivan, E. Kharshiing, J. Laird, T. Sakai, and J. M. Christie(2019)Deetiolation enhances phototropism by modulating non-phototropic hypocotyl3 phosphorylation status.Plant Physiology180(2),pp. 1119–1131.Cited by:§2.2.
- [156]I. Taylor, K. Lehner, E. McCaskey, N. Nirmal, Y. Ozkan-Aydin, M. Murray-Cooper, R. Jain, E. W. Hawkes, P. C. Ronald, D. I. Goldman,et al.(2021)Mechanism and function of root circumnutation.Proceedings of the National Academy of Sciences118(8),pp. e2018940118.Cited by:Figure 5,§6.2.
- [157]F. Tedone, E. Del Dottore, M. Palladino, B. Mazzolai, and P. Marcati(2020)Optimal control of plant root tip dynamics in soil.Bioinspiration & Biomimetics15(5),pp. 056006.Cited by:§4.1.
- [158]M. V. Thompson and N. M. Holbrook(2004)Root-gel interactions and the root waving behavior of arabidopsis.Plant Physiology135(3),pp. 1822–1837.Cited by:Figure 4.
- [159]S. Timoshenko(1925)Analysis of bi-metal thermostats.Journal of the Optical Society of America11(3),pp. 233–255.Cited by:§2.1.
- [160]K. Tunstrøm, Y. Katz, C. C. Ioannou, C. Huepe, M. J. Lutz, and I. D. Couzin(2013)Collective states, multistability and transitional behavior in schooling fish.PLoS computational biology9(2),pp. e1002915.Cited by:Figure 5.
- [161]S. Vanneste and J. Friml(2009)Auxin: a trigger for change in plant development.Cell136(6),pp. 1005–1016.External Links:DocumentCited by:§2.1.
- [162]T. Vicsek, A. Czirók, E. Ben-Jacob, I. Cohen, and O. Shochet(1995-08)Novel Type of Phase Transition in a System of Self-Driven Particles.Physical Review Letters75(6),pp. 1226–1229.Cited by:Figure 5,§6.3.
- [163]T. Vicsek, A. Czirók, I. J. Farkas, and D. Helbing(1999)Application of statistical mechanics to collective motion in biology.Physica A: Statistical Mechanics and its Applications274(1-2),pp. 182–189.Cited by:§6.3,§6.
- [164]D. Volkmann and M. Tewinkel(1996-10)Gravisensitivity of cress roots: investigations of threshold values under specific conditions of sensor physiology in microgravity.Plant, Cell and Environment19(10),pp. 1195–1202.Cited by:§3.1.
- [165]D. Volkmann and M. Tewinkel(1998)Gravisensitivity of cress roots.Advances in Space Research21(8).Cited by:§3.1.
- [166]A. G. Volkov, H. Carrell, T. Adesina, V. S. Markin, and E. Jovanov(2008)Plant electrical memory.Plant signaling & behavior3(7),pp. 490–492.Cited by:§3.1.
- [167]D. von Wangenheim, R. Hauschild, M. Fendrych, V. Barone, E. Benková, and J. Friml(2017-06)Live tracking of moving samples in confocal microscopy for vertically grown roots.eLife6,pp. e26792.External Links:Document,Link,ISSN 2050-084XCited by:Figure 1.
- [168]N. Wadhwa and H. C. Berg(2022)Bacterial motility: machinery and mechanisms.Nat Rev Microbiol20,pp. 161–173.Cited by:§6.
- [169]T. Wang, C. Pierce, V. Kojouharov, B. Chong, K. Diaz, H. Lu, and D. I. Goldman(2023)Mechanical intelligence simplifies control in terrestrial limbless locomotion.Science Robotics8(85),pp. eadi2243.Cited by:§4.
- [170]F. Went(1926)On growth-accelerating substances in the coleoptile of avena sativa.InProc Kon Akad Wetensch Amsterdam,Vol.30,pp. 10–19.Cited by:§2.1.
- [171]F. W. Went, K. V. Thimann,et al.(1937)Phytohormones.Macmillan New York.Cited by:§2.1.
- [172]C. W. Whippo and R. P. Hangarter(2006)Phototropism: bending towards enlightenment.The Plant Cell18(5),pp. 1110–1119.Cited by:§2.1.
- [173]R. C. Wilson, E. Bonawitz, V. D. Costa, and R. B. Ebitz(2021)Balancing exploration and exploitation with information and randomization.Current Opinion in Behavioral Sciences38,pp. 49–56.Note:Computational cognitive neuroscienceExternal Links:ISSN 2352-1546,Document,LinkCited by:§6.
- [174]M. Wooten and I. Walker(2015)A novel vine-like robot for in-orbit inspection..Proceedings 45th International Conference on Environmental Systems,pp. 1–11.Cited by:§6.3.
- [175]J. Yao, J. Barés, L. X. Dupuy, and E. Kolb(2025)Physical obstacles in the substrate cause maize root growth trajectories to switch from vertical to oblique.Journal of Experimental Botany76(2),pp. 546–561.Cited by:Figure 4,§4.1.
- [176]Z. Zhang, D. van Ophem, R. Chelakkot, N. Lazarovitch, and I. Regev(2022)A mechano-sensing mechanism for waving in plant roots.Scientific Reports12(1),pp. 9635.Cited by:§4.2.

## 


- 


Major funding support from
