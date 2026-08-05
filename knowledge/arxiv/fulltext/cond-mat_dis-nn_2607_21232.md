# Driven criticality links universal computation and optimal representations

**arXiv ID**: 2607.21232v2
**Authors**: Adrián Roig, Miguel A. Muñoz, Guillermo B. Morales
**Published**: 2026-07-23
**Categories**: cond-mat.dis-nn, nlin.CD
**Comments**: Supplementary material is available as Dynamically-optimal-RC_SI.pdf in the arXiv source files
**HTML URL**: https://arxiv.org/html/2607.21232v2

## Abstract

Near-critical dynamics are often linked to enhanced computation, but the underlying mechanism remains unclear. We address this question in reservoir computing, where a fixed recurrent network maps input sequences into high-dimensional states and only a simple readout is trained. We extend fixed-reservoir universality results to discrete-time input-driven reservoirs and connect their key geometric condition, neighborhood separation, to dynamics. To this end, we introduce a finite-resolution neighborhood separability index and an input-conditioned maximal Lyapunov exponent. We find that neighborhood separability, chaotic time-series prediction, and smooth high-dimensional representation geometry are optimized in the same narrow window of marginal driven stability. In this regime, the covariance spectrum approaches the power-law scaling expected for near-optimal smooth representations. Our results link edge-of-instability computation, universality, readout performance, and optimal representation geometry within a common dynamical framework.

## Full Text

Driven criticality links universal computation and optimal representations

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.21232v2 [cond-mat.dis-nn] 27 Jul 2026

## Driven criticality links universal computation and optimal representationsAdrián RoigDepartamento de Electromagnetismo y Física de la Materia and Instituto Carlos I
de Física Teórica y Computacional. Universidad de Granada.E-18071, Granada, SpainMiguel A. Muñoz†Departamento de Electromagnetismo y Física de la Materia and Instituto Carlos I
de Física Teórica y Computacional. Universidad de Granada.E-18071, Granada, SpainGuillermo B. Morales†Departamento de Electromagnetismo y Física de la Materia and Instituto Carlos I
de Física Teórica y Computacional. Universidad de Granada.E-18071, Granada, Spain(July 27, 2026)

## Abstract

Near-critical dynamics are often linked to enhanced computation, but the underlying mechanism remains unclear. We address this question in reservoir computing, where a fixed recurrent network maps input sequences into high-dimensional states and only a simple readout is trained. We extend fixed-reservoir universality results to discrete-time input-driven reservoirs and connect their key geometric condition, neighborhood separation, to dynamics. To this end, we introduce a finite-resolution neighborhood separability index and an input-conditioned maximal Lyapunov exponent. We find that neighborhood separability, chaotic time-series prediction, and smooth high-dimensional representation geometry are optimized in the same narrow window of marginal driven stability. In this regime, the covariance spectrum approaches the power-law scaling expected for near-optimal smooth representations. Our results link edge-of-instability computation, universality, readout performance, and optimal representation geometry within a common dynamical framework.

†These authors contributed equally.

A recurring theme in complex recurrent systems is that operating near the boundary between distinct dynamical regimes or phases can yield an unusual combination of sensitivity, dynamic range across many scales, and flexible yet robust responses; features often linked to enhanced computational capacity[19,34,8,25,3,27,31]. In neuroscience, this idea is captured by the criticality hypothesis: cortical circuits may operate close to a critical regime to support efficient information transmission, memory, and rapid adaptation[1,6,40,13,7,50,2,33].
Empirically, near-critical brain dynamics have been probed through scale-invariant activity, long-range correlations, and correlation-based signatures of proximity to criticality[1,35,26,9,14,28].
A closely related theme appears in machine learning, particularly in the reservoir computing (RC) paradigm[38,39], where a fixed recurrent neural network (the reservoir) maps an input stream into a high-dimensional dynamical internal state, while only a simple readout layer is trained to perform a task (see
Fig.1b)[16,18,15,17,23,24,22,3,5,20,49,29,41,10].
Since pioneering studies of computation at the edge of chaos, such systems have often been reported to perform best near the boundary between strongly stable dynamics and unstable, perturbation-amplifying regimes[5,20,49,29].

A particularly relevant advance has been the formulation of functional optimality in terms of representation geometry[42,32,9,29]. Here, arepresentationis the map from an external input, stimulus, or task parameter to the corresponding network state, viewed as a point or trajectory in a high-dimensional state space (see Fig.1a). Stringeret al.[42]proposed that near-optimal representations should be as high-dimensional as possible while remaining smooth, and showed that for a smooth representation of adℓd_{\ell}-dimensional input manifold the covariance eigenspectrum must decay asλn∼n−μ\lambda_{n}\sim n^{-\mu}, withμ≥μc=1+2/dℓ\mu\geq\mu_{c}=1+2/d_{\ell}, so that the broadest possible smooth representation lies nearμ≃μc\mu\simeq\mu_{c}.

Since scale-free spectra are a hallmark of critical phenomena[4,14,28], this observation raises the question of whether the dynamical regimes that produce high-dimensional optimal representations arise at the boundary between stable and unstable dynamics. While this possibility has been explored computationally by some of us[29], a principled explanation of why such a regime should support both optimal representations and computational power remains lacking.

Here we take a step in this direction by building on recent universality results of Sugiura and collaborators[44,45,46].
Universality denotes the property that a fixed reservoir, by training only a polynomial readout, can approximateanytarget dynamical input–output map to arbitrary accuracy. In Sugiura’set al.framework, universality is guaranteed by a local necessary and sufficient condition known as theneighborhood separation property(NSP): non-overlapping input neighborhoods must remain distinguishable after they are represented in reservoir state space. In contrast to earlier approaches based on strong fading-memory assumptions[11], NSP is a local separability condition on input neighborhoods.

We explore these ideas in a minimal reservoir-computing model driven by chaotic time series, using the input-conditioned maximal Lyapunov exponent (MLE) to track the reservoir’s driven stability as recurrent connectivity is varied. We find that NSP and task performance peak sharply in a narrow marginally stable regime,MLE≃0−\mathrm{MLE}\simeq 0^{-}, which is also where the covariance-spectrum exponent most closely approaches the optimal smoothness bound of Stringeret al.

Thus, our central goal is to connect the reservoir’s dynamical regime to the geometry of its representation. We argue that marginal driven stability is the regime where two geometric requirements can coexist: local neighborhood separation, needed for universal computation, and smooth high-dimensional structure, needed for near-optimal representations. In this view, edge-of-instability performance reflects a dynamical balance between sensitivity and regularity.Figure 1:Representation map and reservoir-computing architecture.(a) External stimuli are encoded as neural activity patterns forming a trajectory or point cloud in high-dimensional state space.
(b) A multivariate input stream,u​(t)u(t), drives a fixed recurrent network throughWinW^{\rm in}, producing reservoir states,x​(t)x(t). Only the readout matrix,WoutW^{\rm out}, is trained to produce the target,y​(t)y(t).

Let us consider a standard reservoir-computing setup in which a fixed recurrent network ofNNnodes transforms an input stream into a high-dimensional state, and only a readout is trained[15,16,22](see Fig.1b). The reservoir evolves in discrete time steps according to the input-driven dynamics:xt=ϕ​(ρ​Wr​e​s​xt−1+ε​Wi​n​ut−1),x_{t}=\phi\left(\rho W^{res}x_{t-1}+\varepsilon W^{in}u_{t-1}\right),(1)

wherext∈ℳ⊂ℝNx_{t}\in\mathcal{M}\subset\mathbb{R}^{N}is the reservoir state at timett,ut−1∈𝒰⊂ℝdu_{t-1}\in\mathcal{U}\subset\mathbb{R}^{d}is the input at the previous time step, with𝒰\mathcal{U}bounded andd≪Nd\ll N, andϕ\phiis a smooth component-wise activation function. We useϕ​(y)=tanh⁡(y)\phi(y)=\tanh(y)as a representative bounded sigmoidal nonlinearity (with general assumptions stated in SI, Sec. S1.2). Forϕ=tanh\phi=\tanh, the reservoir state space is the N-dimensional hypercubeℳ=[−1,1]N\mathcal{M}=[-1,1]^{N}.
The recurrent matrix,Wr​e​s∈ℝN×NW^{res}\in\mathbb{R}^{N\times N}, and input matrix,Wi​n∈ℝN×dW^{in}\in\mathbb{R}^{N\times d}, are drawn with i.i.d. Gaussian entries of zero mean and variances1/N1/Nand1/d1/d, respectively; and the two fundamental hyperparameters of the model areρ\rho, which controls the effective recurrent gain; andε\varepsilon, which sets the input strength, so the autonomous limit is recovered forε=0\varepsilon=0.

For any finite input sequenceu0:T−1≡(u0,…,uT−1)u_{0:T-1}\equiv(u_{0},\ldots,u_{T-1}),
Eq. (1) maps the sequence into the final reservoir state,
which we call its representation:xT=𝐟​(u0:T−1).x_{T}=\mathbf{f}(u_{0:T-1}).(2)

The set of all finite sequences with entries in𝒰\mathcal{U}is denoted
by𝕍∗\mathbb{V}^{*}, so𝐟:𝕍∗→ℝN\mathbf{f}:\mathbb{V}^{*}\to\mathbb{R}^{N}.

Our aim is not to identify yet another performance “sweet spot,” but
to determine which dynamical regimes supportuniversality: the
ability of a fixed reservoir, with only the readout trained, to
approximate arbitrary continuous tasks of the input sequence (End
Matter, Sec. B.1). To make this precise, we equip𝕍∗\mathbb{V}^{*}with a fading-memory metric, so that it becomes an input-sequence space in which sequences are close when they differ little in recent inputs, while differences in the remote past are weighted less strongly (End Matter, Sec. A.1).

In this geometry, the neighborhood separation property (NSP) requires
distinct local neighborhoods of sequences to remain separated after
mapping into reservoir state space by𝐟\mathbf{f}. Equivalently, NSP
constrains the local non-degeneracy of the inverse relation𝐟−1\mathbf{f}^{-1}: nearby reservoir states should not ambiguously
correspond to unrelated input sequences (End Matter, Sec. A.2).

Sugiura and collaborators proved that this condition is necessary and sufficient for universal approximation with polynomial readouts in input-driven continuous-time reservoirs[44,45,46]. Here, we have extended these universality results todiscrete-timereservoirs (End Matter, Sec. A.1, and SI Secs. S1.1 and S1.2), showing that the same NSP criterion guarantees universality with polynomial readouts in our setting. Thus, NSP and the Stringeret al.smoothness bound enter a common geometric language: the Stringer bound constrains the regularity of𝐟\mathbf{f}, whereas NSP constrains the local non-degeneracy of𝐟−1\mathbf{f}^{-1}.

To examine how different dynamical regimes affect NSP, we vary the gain parameterρ\rho, which controls the relative strength of recurrence and therefore how input sequences are embedded into reservoir states,xT=𝐟​(u0:T−1)x_{T}=\mathbf{f}(u_{0:T-1}). We first use the isolated reservoir,ε=0\varepsilon=0, to identify the underlying autonomous dynamical regimes, and then interpret the input-driven case,ε>0\varepsilon>0, as a perturbation of these regimes. In the autonomous limit, increasingρ\rhoproduces a classical bifurcation scenario (Fig.2): reservoir units move from a globally attracting fixed point to oscillatory dynamics and chaos, before saturation drives activity toward the boundaries (faces, edges, vertices) of the state-space hypercube. Although the transition values depend on the nonlinearity and reservoir realization, this phenomenology is generic for bounded sigmoidal activation functions.

In the weakly recurrent regime (left of Fig.2,ρ≪1\rho\ll 1), the driven reservoir cannot propagate past information far into the future. Indeed, in the limiting caseρ=0\rho=0, one hasxt=ϕ​(ε​Win​ut−1)x_{t}=\phi(\varepsilon W^{\rm in}u_{t-1})forε≠0\varepsilon\neq 0, so the map𝐟\mathbf{f}collapses all input sequences sharing the same last value into the same representation. Consequently,𝐟\mathbf{f}is not injective: no inverse function𝐟−1\mathbf{f}^{-1}exists on its image that can recover the input sequence uniquely from the representation, precluding NSP.
More generally, a Taylor expansion of Eq. (1)
inρ\rho, truncated at ordernn, shows thatxTx_{T}depends only
on the most recentO​(n)O(n)inputs; to that order, sequences that
coincide on their lastnnentries map to the same state,
only a short effective memory is available and NSP does not hold in practice.Figure 2:Autonomous reservoir dynamics changes with recurrent gain.(a) Unforced dynamics (ε=0\varepsilon=0,N=200N=200) as the recurrent gainρ\rhois increased. The panel shows the statex0x_{0}of a representative reservoir unit versusρ\rho, with the typical structure of a bifurcation diagram. Shaded regions indicate the corresponding driven dynamical regimes classified by the input-conditioned maximal Lyapunov exponent (MLE): contracting dynamics (MLE<0\mathrm{MLE}<0), marginal driven stability (MLE≃0\mathrm{MLE}\simeq 0), and expanding dynamics (MLE>0\mathrm{MLE}>0).
(b–f) Representative reservoir trajectories in state space for increasingρ\rho: weak recurrence collapses the representation near a fixed point (b); near marginal stability, trajectories unfold into a structured geometry (c); beyond stability, stretching and folding lead to mixing (d); and at very largeρ\rho, saturation drives activity onto the faces, edges, and vertices of the state-space hypercube (e,f). Gray lines connect consecutive reservoir states.

A different route to NSP failure occurs asρ\rhoincreases into expanding, mixing regimes: nearby inputs may separate rapidly, but bounded dynamics stretch and fold their images, so nearby reservoir states can originate from unrelated input sequences and local inverse discriminability is lost. Saturation provides a limiting form of this bounded-state-space distortion. In the large-ρ\rholimit (Fig.2, right), the autonomous dynamics is driven toward the boundaries of the state spaceℳ\mathcal{M}, namely the hypercube (SI Secs. S1.3 and S1.4). In saturated directions, small input perturbations are filtered by the local Jacobian, i.e., to orderε\varepsilon,ϕ​(ρ​Wres​x+ε​Win​u)≃ϕ​(ρ​Wres​x)+ε​Jϕ​(ρ​Wres​x)​Win​u,\phi(\rho W^{\rm res}x+\varepsilon W^{\rm in}u)\simeq\phi(\rho W^{\rm res}x)+\varepsilon J_{\phi}(\rho W^{\rm res}x)W^{\rm in}u,(3)

so that, forϕ=tanh\phi=\tanh, the diagonal entries ofJϕJ_{\phi}are1−tanh2⁡[(ρ​Wres​x)]1-\tanh^{2}[(\rho W^{\rm res}x)]and vanish in saturated units. Thus, the directions that dominate the state become locally insensitive to the input, violating the local non-degeneracy required by NSP.

Together, weak recurrence and mixing-induced folding, which culminates in saturation, obstruct NSP in complementary ways. Increasingρ\rhotoward marginal stability makes higher-order recurrent effects dynamically relevant and extends memory; beyond this window, however, uncontrolled folding destroys the smooth geometry of the input representation (SI Secs. S1.3 and S1.4). Marginal driven stability is therefore the natural candidate regime in which memory, local separation, and a smooth, optimal input-representation geometry can coexist.

To examine this semi-analytical picture computationally, we use a representative reservoir realization with fixed architecture (WresW^{\rm res},WinW^{\rm in},ϕ=tanh\phi=\tanh), small input gainε\varepsilon, and varyingρ\rho, as a numerical instance of the generic mechanism described above. Inputs are normalized time series,ut∈𝒰⊂ℝ3u_{t}\in\mathcal{U}\subset\mathbb{R}^{3}, generated from the Lorenz attractor[21,43](Fig.1b). Starting from an arbitrary pointu0∈ℝ3u_{0}\in\mathbb{R}^{3}on the attractor, we construct length-TTsequences:u0:T−1=(u0,g​(u0),…,gT−1​(u0)),u_{0:T-1}=\bigl(u_{0},\,g(u_{0}),\,\ldots,\,g^{T-1}(u_{0})\bigr),(4)

whereg:ℝ3→ℝ3g:\mathbb{R}^{3}\to\mathbb{R}^{3}denotes a discrete-time flow map of the Lorenz dynamics. The terminal statexT=𝐟​(u0:T−1)x_{T}=\mathbf{f}(u_{0:T-1})should retain task-relevant information to be used by the readout.

The remaining question is which dynamical regime makes the induced representation𝐟\mathbf{f}both locally separable and useful for readout-based approximation. To connect the underlying dynamical regime with NSP, we introduce two measures. First, we characterize the stability of the driven reservoir dynamics through an input-conditioned maximal Lyapunov exponent (MLE), which measures the rate of amplification of infinitesimal state perturbations along trajectories driven by a given input sequence (SI Sec. S2.2)[12,48,37,36].
Second, we introduce the neighborhood separability index (NSI), a new finite-resolution diagnostic that quantifies how closely a sampled reservoir representation realizes the neighborhood separation required by NSP (SI Sec. S2.1).
For each pair of nearby but disjoint input neighborhoods in the fading-memory metric, we map the corresponding inputs through the reservoir and compare the separation between the resulting state clouds with their internal spread. Specifically, ifXAX_{A}andXBX_{B}are the two image clouds, with empirical centroidsm​(XA),m​(XB)m(X_{A}),m(X_{B})and radiir​(XA),r​(XB)r(X_{A}),r(X_{B}), NSI is based on the local margin:ΔA​B=‖m​(XA)−m​(XB)‖2−[r​(XA)+r​(XB)],\Delta_{AB}=\|m(X_{A})-m(X_{B})\|_{2}-\bigl[r(X_{A})+r(X_{B})\bigr],(5)

where∥⋅∥2\|\cdot\|_{2}denotes the Euclidean norm in reservoir state space. Positive margins certify finite-resolution neighborhood separation, whereas negative margins indicate overlap of the corresponding envelope of image clouds. NSI is obtained by averaging the positive part of this margin over sampled neighborhood pairs.
Thus, NSI is a geometric diagnostic: a computable, finite-resolution
counterpart of NSP for readout-based interpolation (SI Sec. S2.1 and
Figs. S3–S5).Figure 3:Neighborhood separability and performance peak near
marginal driven stability.(a) Neighborhood separability index (NSI) versus input-conditioned
maximal Lyapunov exponent (MLE), obtained by varyingρ\rhoforN=2000N=2000(SI Secs. S2.1 and S2.2). Error bars indicate variability
across sampled neighborhood pairs. Shaded regions indicate the regimes
identified in Fig.2: strongly contractive R1, marginally
stable R2, and unstable/saturation-dominated R3. NSI is maximal nearMLE≃0−\mathrm{MLE}\simeq 0^{-}.
(b) Supremum-norm error (SEN) for benchmark tasks (End Matter,
Sec. B.2, and SI Sec. S2.3), withN=2000N=2000andε=0.01\varepsilon=0.01.
SEN is minimized in the same R2 window.Figure 4:Marginal driven stability meets optimal representation geometry and predictive power.(a) Input-conditioned maximal Lyapunov exponent (MLE) as a function of spectral radiusρ\rhoand input scaleε\varepsilon.
(b) PCA projections of reservoir activity for four representative parameter choices, together with the corresponding covariance spectra.
(c, d) Furthest-predicted point (FPP) and Root-mean-square error (RMSE), showing optimal prediction near marginal driven stability,MLE≃0−\mathrm{MLE}\simeq 0^{-}.
(e, f) Input-conditioned MLE and spectral exponentμ\muas a function ofρ\rho, showingμ≈1+2/dℓ\mu\approx 1+2/d_{\ell}near the point of marginal driven stability,MLE≃0−\mathrm{MLE}\simeq 0^{-}.

Figure3a shows NSI as a function of the input-conditioned MLE asρ\rhois varied, revealing three regimes. At smallρ\rho, region R1 is strongly contractive, withMLE<0\mathrm{MLE}<0: input sequences are rapidly forgotten, nearby input neighborhoods overlap in reservoir state space, and NSI is negligible.
At intermediateρ\rho, region R2 approaches marginal driven stability,MLE≃0−\mathrm{MLE}\simeq 0^{-}, where robustly positive NSI indicates
finite-resolution separation and locally coherent geometry inℳ\mathcal{M}.
At largerρ\rho, region R3 is unstable and/or saturation-dominated, and NSI collapses again because input geometry is degraded by suppressed sensitivity or uncontrolled stretching and folding. The same R2 window minimizes the test supremum-norm error (SEN; Fig.3b and End Matter, Sec. B.2) for all benchmark tasks, showing that neighborhood separability and readout performance are optimized together near marginal driven stability. Although NSP guarantees universality for polynomial readouts, Fig.3further indicates that near this optimum a simple linear readout already suffices for the tasks considered here.

The coincidence of separability and optimal performance in Fig.3suggests that the marginally stable regime should also be distinguished by the geometry of its internal representations. To quantify the linear degrees of freedom available to the readout (SI Secs. S1.5 and S1.7), we analyze the covariance matrix of reservoir states sampled along driven trajectories:C=𝔼u∈𝕍∗​[x​(u)​x​(u)⊤],x​(u)=𝐟​(u)∈ℝN,C=\mathbb{E}_{u\in\mathbb{V}^{*}}\left[x(u)x(u)^{\top}\right],\qquad x(u)=\mathbf{f}(u)\in\mathbb{R}^{N},(6)

together with its rank-ordered eigenvaluesλ1≥⋯≥λN\lambda_{1}\geq\cdots\geq\lambda_{N}.
Over an intermediate range of parameters, the spectrum follows a power law,λn∼n−μ\lambda_{n}\sim n^{-\mu}, with the fitted exponentμ\muvarying across the(ρ,ε)(\rho,\varepsilon)plane, as shown in Fig.4a. Smallerμ\mucorresponds to slower spectral decay and therefore to a broader representation, with more active linear modes available to the readout.

Fig.4b shows reservoir trajectories projected onto the leading principal components for four representative regimes. For smallρ\rho, the representation closely mimics the Lorenz attractor and deterministically tracks the input, but task performance remains low in this low-dimensional representation regime. Asρ\rhoincreases at fixedε\varepsilon, the trajectories spread across more principal directions, reaching their largest effective dimensionality near the stability boundary. Comparing the fitted spectral exponent with the Stringeret al. smoothness bound,μc=1+2/dℓ\mu_{c}=1+2/d_{\ell}, shows that this regime approaches the highest-dimensional representation compatible with the bound. For the Lorenz attractor, the intrinsic dimension givesμc≃1.95\mu_{c}\simeq 1.95, in agreement with the exponent measured where NSI is positive, as shown in Fig.4f.

Thus, the optimal regime is not merely high-dimensional; it also respects the smoothness constraint set by the dimensionality of the input space. We have therefore connected two geometric requirements: the Stringeret al.bound constrains the forward regularity of𝐟\mathbf{f}, whereas NSP constrains the local non-degeneracy of the inverse relation𝐟−1\mathbf{f}^{-1}(see thecovering-learning protocol, SI Sec. S1.6). Near marginal stability, both requirements are approximately satisfied: the reservoir-state manifold remains smooth enough to approachμc\mu_{c}while preserving finite-resolution neighborhood separation.

In more unstable or saturation-dominated regimes, forward smoothness and/or local inverse discriminability deteriorate, the usable linear degrees of freedom become less reliable, and predictive performance worsens (Fig.4c,d; see End Matter, Sec. B.2 for the furthest-predicted point, FPP, and root-mean-square error, RMSE). Taken together, Figs.3and4show that the best-performing regime combines input-dependent separation with a broad, high-dimensional but regular linear encoding, explaining why a simple linear readout suffices in our benchmarks.

In conclusion, we identify a dynamical mechanism underlying edge-of-instability optimality in input-driven reservoirs. Marginal driven stability balances memory, sensitivity, and regularity: input sequences are neither erased by strong contraction nor degraded by uncontrolled amplification, folding, or saturation. This balance allows the reservoir representation to approach the smooth high-dimensional geometry predicted by the Stringeret al.bound while retaining the finite-resolution neighborhood separation required for universal computation.

Our results bring together three complementary perspectives. First, by extending Refs.[44,45,46]to discrete time, we show that NSP remains a necessary and sufficient condition for universality with polynomial readouts. Second, NSI and the input-conditioned MLE provide an operational bridge from this theory to finite reservoirs: asρ\rhois varied, finite-resolution neighborhood separability becomes robust and task performance is optimized near marginal driven stability,MLE≃0−\mathrm{MLE}\simeq 0^{-}. Third, this marginally stable regime also yields broad covariance spectra approaching the Stringeret al.bound,μ≃1+2/dℓ\mu\simeq 1+2/d_{\ell}, thereby linking computational performance to smooth high-dimensional representation geometry. In this way, our results connect edge-of-instability computation, universality theory, and the geometry of near-optimal representations within a common dynamical framework.

Several open avenues remain for future work, including extending these results to continuous-time reservoirs and identifying self-organization mechanisms that tune reservoirs toward marginal driven stability for broad classes of inputs and tasks. Such mechanisms could make neighborhood separability, predictive performance, and smooth high-dimensional representations robust without external fine tuning, providing design principles for optimized physical reservoirs across different substrates[47].

Acknowledgments:We acknowledge the Spanish Ministry
and Agencia Estatal de Investigación (AEI), MICIN/AEI/10.13039/501100011033, for financial support, Project PID2023-149174NB-I00 funded also by ERDF/EU.
We acknowledge inspiring discussions with V. Buendía and R. Calvo.

## References
- [1]J. M. Beggs and D. Plenz(2003)Neuronal Avalanches in Neocortical Circuits.J.Neurosci.23(35),pp. 11167–11177.Cited by:Driven criticality links universal computation and optimal representations.
- [2]J. M. Beggs(2022)The cortex and the critical point: understanding the power of emergence.MIT Press.Cited by:Driven criticality links universal computation and optimal representations.
- [3]N. Bertschinger and T. Natschläger(2004-07)Real-Time Computation at the Edge of Chaos in Recurrent Neural Networks.Neural Computation16(7),pp. 1413–1436.External Links:ISSN 0899-7667,Link,DocumentCited by:Driven criticality links universal computation and optimal representations.
- [4]J. J. Binney, N. J. Dowrick, A. J. Fisher, and M. E. J. Newman(1992)The theory of critical phenomena: an introduction to the renormalization group.Oxford Science Publications,Clarendon Press,Oxford.Cited by:Driven criticality links universal computation and optimal representations.
- [5]J. Boedecker, O. Obst, J. T. Lizier, N. M. Mayer, and M. Asada(2011)Information Processing in Echo State Networks at the Edge of Chaos.Theory in Biosciences131(3).External Links:DocumentCited by:Driven criticality links universal computation and optimal representations.
- [6]D. R. Chialvo(2010)Emergent complex neural dynamics.Nature physics6(10),pp. 744–750.Cited by:Driven criticality links universal computation and optimal representations.
- [7]L. Cocchi, L. L. Gollo, A. Zalesky, and M. Breakspear(2017)Criticality in the brain: a synthesis of neurobiology, models and cognition.Progress in Neurobiology.Cited by:Driven criticality links universal computation and optimal representations.
- [8]J. P. Crutchfield and K. Young(1988)Computation at the onset of chaos.InThe Santa Fe Institute, Westview,pp. 223–269.Cited by:Driven criticality links universal computation and optimal representations.
- [9]D. Dahmen, S. Grün, M. Diesmann, and M. Helias(2019-06)Second type of criticality in the brain uncovers rich multiple-neuron dynamics.Proceedings of the National Academy of Sciences116(26),pp. 13051–13060.External Links:ISSN 0027-8424, 1091-6490,Link,DocumentCited by:Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [10]J. Dambre, D. Verstraeten, B. Schrauwen, and J. Van Campenhout(2012)Information processing capacity of dynamical systems.Scientific Reports2,pp. 514.External Links:DocumentCited by:Driven criticality links universal computation and optimal representations.
- [11]L. Grigoryeva and J. Ortega(2018)Echo state networks are universal.Neural Networks108,pp. 495–508.External Links:ISSN 0893-6080,Document,LinkCited by:Driven criticality links universal computation and optimal representations.
- [12]J. D. Hart(2024)Attractor reconstruction with reservoir computers: the effect of the reservoir’s conditional lyapunov exponents on faithful attractor reconstruction.Chaos34(4),pp. 043123.External Links:DocumentCited by:Driven criticality links universal computation and optimal representations.
- [13]K. B. Hengen and W. L. Shew(2025)Is criticality a unified setpoint of brain function?.Neuron113(16),pp. 2582–2598.Cited by:Driven criticality links universal computation and optimal representations.
- [14]Y. Hu and H. Sompolinsky(2022)The spectrum of covariance matrices of randomly connected recurrent neuronal networks with linear dynamics.PLoS computational biology18(7),pp. e1010327.Cited by:Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [15]H. Jaeger and H. Haas(2004-04)Harnessing Nonlinearity: Predicting Chaotic Systems and Saving Energy in Wireless Communication.Science304(5667),pp. 78–80.External Links:ISSN 0036-8075, 1095-9203,Link,DocumentCited by:Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [16]H. Jaeger(2001-01)The” echo state” approach to analysing and training recurrent neural networks-with an erratum note’.Bonn, Germany: German National Research Center for Information Technology GMD Technical Report148.Cited by:Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [17]H. Jaeger(2007)Echo state network.scholarpedia2(9),pp. 2330.Cited by:Driven criticality links universal computation and optimal representations.
- [18]H. Jaeger(2002-03)Short term memory in echo state networks.GMD ReportTechnical Report152,GMD — German National Research Center for Information Technology,Sankt Augustin, Germany.Note:Technical ReportExternal Links:LinkCited by:Driven criticality links universal computation and optimal representations.
- [19]C. G. Langton(1990-06)Computation at the edge of chaos: phase transitions and emergent computation.Physica D: Nonlinear Phenomena42(1),pp. 12–37.External Links:ISSN 0167-2789,Link,DocumentCited by:Driven criticality links universal computation and optimal representations.
- [20]R. Legenstein and W. Maass(2007-04)Edge of chaos and prediction of computational performance for neural circuit models.Neural Networks20(3),pp. 323–334.External Links:ISSN 0893-6080,Link,DocumentCited by:Driven criticality links universal computation and optimal representations.
- [21]E. N. Lorenz(1963-03)Deterministic Nonperiodic Flow.Journal of the Atmospheric Sciences20(2),pp. 130–141.External Links:ISSN 0022-4928, 1520-0469,Link,DocumentCited by:Driven criticality links universal computation and optimal representations.
- [22]M. Lukoševičius(2012)A Practical Guide to Applying Echo State Networks.InNeural Networks: Tricks of the Trade: Second Edition,G. Montavon, G. B. Orr, and K. Müller (Eds.),Lecture Notes in Computer Science,pp. 659–686.External Links:ISBN 978-3-642-35289-8,Link,DocumentCited by:Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [23]W. Maass, T. Natschläger, and H. Markram(2002)Real-Time Computing without Stable States: a New Framework for Neural Computation Based on Perturbations.Neural Computation14(11).External Links:DocumentCited by:Driven criticality links universal computation and optimal representations.
- [24]W. Maass(2011)Liquid state machines: motivation, theory, and applications.Computability in context: computation and logic in the real world,pp. 275–296.Cited by:Driven criticality links universal computation and optimal representations.
- [25]M. Melanie(1993)Dynamics, computation, and the” edge of chaos”; A reexamination.Complexity: Metaphors, Models, and Reality.Cited by:Driven criticality links universal computation and optimal representations.
- [26]L. Meshulam, J. L. Gauthier, C. D. Brody, D. W. Tank, and W. Bialek(2019)Coarse graining, fixed points, and scaling in a large population of neurons.Physical review letters123(17),pp. 178103.Cited by:Driven criticality links universal computation and optimal representations.
- [27]T. Mora and W. Bialek(2011)Are biological systems poised at criticality?.J. Stat. Phys.144(2),pp. 268–302.Cited by:Driven criticality links universal computation and optimal representations.
- [28]G. B. Morales, S. Di Santo, and M. A. Muñoz(2023)Quasiuniversal scaling in mouse-brain neuronal activity stems from edge-of-instability critical dynamics.Proceedings of the National Academy of Sciences120(9),pp. e2208998120.Cited by:Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [29]G. B. Morales and M. A. Muñoz(2021)Optimal input representation in neural systems at the edge of chaos.Biology10(8),pp. 702.Cited by:Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [30]G. B. Morales, C. R. Mirasso, and M. C. Soriano(2021-05)Unveiling the role of plasticity rules in reservoir computing.Neurocomputing.External Links:ISSN 0925-2312,Link,DocumentCited by:2.2.§.
- [31]M. A. Muñoz(2018-07)Colloquium: Criticality and Dynamical Scaling in Living Systems.Rev. Mod. Phys.90(3),pp. 031001.Cited by:Driven criticality links universal computation and optimal representations.
- [32]J. Nassar, P. A. Sokol, S. Chung, K. D. Harris, and I. M. Park(2020-12)On 1/n neural representation and robustness.arXiv:2012.04729 [cs].Note:arXiv: 2012.04729External Links:LinkCited by:Driven criticality links universal computation and optimal representations.
- [33]J. O’Byrne and K. Jerbi(2022)How critical is brain criticality?.Trends in Neurosciences45(11),pp. 820–837.Cited by:Driven criticality links universal computation and optimal representations.
- [34]N. H. Packard(1988)Adaptation toward the edge of chaos.Dynamic Patterns in Complex Systems,pp. 293–301.Cited by:Driven criticality links universal computation and optimal representations.
- [35]J. M. Palva and S. Palva(2014)The correlation of the neuronal long-range temporal correlations, avalanche dynamics with the behavioral scaling laws and interindividual variability.Criticality in Neural Systems,pp. 105–126.Cited by:Driven criticality links universal computation and optimal representations.
- [36]L. M. Pecora and T. L. Carroll(1991)Driving systems with chaotic signals.Physical Review A44(4),pp. 2374–2383.External Links:DocumentCited by:Driven criticality links universal computation and optimal representations.
- [37]K. Pyragas(1997)Conditional lyapunov exponents from time series.Physical Review E56(5),pp. 5183–5188.External Links:DocumentCited by:Driven criticality links universal computation and optimal representations.
- [38]B. Schrauwen, D. Verstraeten, and J. Van Campenhout(2007)An overview of reservoir computing: theory, applications and implementations.InProceedings of the European Symposium on Artificial Neural Networks (ESANN),Bruges, Belgium.Cited by:Driven criticality links universal computation and optimal representations.
- [39]L. F. Seoane(2019)Evolutionary aspects of reservoir computing.Philosophical Transactions of the Royal Society B: Biological Sciences374(1774).Cited by:Driven criticality links universal computation and optimal representations.
- [40]W. L. Shew and D. Plenz(2013)The functional benefits of criticality in the cortex.The Neuroscientist19(1),pp. 88–100.Cited by:Driven criticality links universal computation and optimal representations.
- [41]P. Singh, L. Sankaranarayanan, and B. Raman(2025)Contraction, criticality, and capacity: a dynamical-systems perspective on echo-state networks.arXiv preprint arXiv:2507.18467.External Links:Document,2507.18467Cited by:Driven criticality links universal computation and optimal representations.
- [42]C. Stringer, M. Pachitariu, N. Steinmetz, M. Carandini, and K. D. Harris(2019-07)High-dimensional geometry of population responses in visual cortex.Nature571(7765),pp. 361–365.External Links:ISSN 1476-4687,Link,DocumentCited by:Driven criticality links universal computation and optimal representations.
- [43]S. H. Strogatz(2000)Nonlinear Dynamics and Chaos : with Applications to Physics, Biology, Chemistry, and Engineering.Westview Press.External Links:ISBN 978-0-7382-0453-6Cited by:Driven criticality links universal computation and optimal representations.
- [44]S. Sugiura, R. Ariizumi, T. Asai,et al.(2024)Existence of reservoir with finite-dimensional output for universal reservoir computing.Scientific Reports14,pp. 8448.External Links:Document,LinkCited by:1.1.§,Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [45]S. Sugiura, R. Ariizumi, T. Asai, and S. Azuma(2024)Nonessentiality of reservoir’s fading memory for universality of reservoir computing.IEEE Transactions on Neural Networks and Learning Systems35(11),pp. 16801–16815.External Links:DocumentCited by:1.1.§,Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [46]S. Sugiura, R. Ariizumi, T. Asai, and S. Azuma(2025)Necessary and sufficient reservoir condition for universal reservoir computing.Mathematics13(21),pp. 3440.Cited by:1.1.§,Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations,Driven criticality links universal computation and optimal representations.
- [47]G. Tanaka, T. Yamane, J. B. Héroux, R. Nakane, N. Kanazawa, S. Takeda, H. Numata, D. Nakano, and A. Hirose(2019)Recent advances in physical reservoir computing: a review.Neural Networks115,pp. 100–123.Cited by:Driven criticality links universal computation and optimal representations.
- [48]A. Uchida, K. Yoshimura, P. Davis, S. Yoshimori, and R. Roy(2008)Local conditional lyapunov exponent characterization of consistency of dynamical response of the driven lorenz system.Physical Review E78(3),pp. 036203.External Links:DocumentCited by:Driven criticality links universal computation and optimal representations.
- [49]X. R. Wang, J. T. Lizier, and M. Prokopenko(2011)Fisher information at the edge of chaos in random boolean networks.Artificial Life17(4),pp. 315–329.External Links:DocumentCited by:Driven criticality links universal computation and optimal representations.
- [50]J. Wilting and V. Priesemann(2019-10)25 years of criticality in neuroscience — established results, open controversies, novel concepts.Current Opinion in Neurobiology58,pp. 105–111.External Links:ISSN 0959-4388,Link,DocumentCited by:Driven criticality links universal computation and optimal representations.

## End Matter

## .1Appendix A: Fading-memory sequence space

## .1.1A.1. Adapting neighborhood-separation universality to the discrete-time framework

We consider finite input sequences with entries in a compact set𝒰⊂ℝd\mathcal{U}\subset\mathbb{R}^{d}. For eachT≥1T\geq 1, let𝕍T∗={(v−T+1,…,v0):v−k∈𝒰},\mathbb{V}^{*}_{T}=\{(v_{-T+1},\ldots,v_{0}):v_{-k}\in\mathcal{U}\},(7)

and define the set of finite sequences as𝕍∗=⋃T≥1𝕍T∗\mathbb{V}^{*}=\bigcup_{T\geq 1}\mathbb{V}^{*}_{T}.
The use of negative indices is only notational: it identifiesv0v_{0}as the most recent input andv−kv_{-k}as an inputkksteps in the past.

To formulate neighborhood separation,𝕍∗\mathbb{V}^{*}is embedded into a compact
metric space. Let𝕍=𝒰ℤ−\mathbb{V}=\mathcal{U}^{\mathbb{Z}_{-}}be the space
of left-infinite input sequences. In the Supplemental Material we construct an
extended fading-memory metricd~\widetilde{d}on𝕍~=𝕍∪𝕍∗\widetilde{\mathbb{V}}=\mathbb{V}\cup\mathbb{V}^{*}using a decreasing weight sequence
for past coordinates together with a length penalty for finite sequences (SI, Sec. S1.1). This
metric has two key properties:(𝕍~,d~)​is compact,𝕍∗​is dense in​𝕍~.(\widetilde{\mathbb{V}},\widetilde{d})\ \text{is compact},\ \ \mathbb{V}^{*}\ \text{is dense in}\ \widetilde{\mathbb{V}}.(8)

In particular, ifv=(…,v−2,v−1,v0)∈𝕍v=(\ldots,v_{-2},v_{-1},v_{0})\in\mathbb{V}, its finite
truncationsv[T]=(v−T+1,…,v0)∈𝕍∗v^{[T]}=(v_{-T+1},\ldots,v_{0})\in\mathbb{V}^{*}converge tovvin(𝕍~,d~)(\widetilde{\mathbb{V}},\widetilde{d})asT→∞T\to\infty.

This compactification is used to define neighborhoods of finite sequences and to
state NSP in the same compact-metric framework as in Refs.[46,44,45]. Importantly,
the reservoir representation𝐟:𝕍∗→ℝN\mathbf{f}:\mathbb{V}^{*}\to\mathbb{R}^{N}must be bounded and is not assumed
to be continuous on𝕍~\widetilde{\mathbb{V}}. The role of NSP is to avoid imposing a strong global
fading-memory condition on the reservoir map, replacing it by a local separation
requirement: distinct neighborhoods in the compactified input space must
have separated images under𝐟\mathbf{f}(SI, Sec. S1.2, S1.2.1).

## .1.2A.2. Neighborhood separability property

In the compactified space(𝕍~,d~)(\widetilde{\mathbb{V}},\widetilde{d}), the
reservoir map is defined only on the dense subset of finite sequences,𝐟:𝕍∗→ℝN.\mathbf{f}:\mathbb{V}^{*}\to\mathbb{R}^{N}.(9)

Accordingly, neighborhoods are taken in the compactified space and then
restricted to finite sequences.

We say that𝐟\mathbf{f}satisfies the
neighborhood separation property (NSP) on𝕍∗\mathbb{V}^{*}if, for every pair of
distinct finite sequencesu,v∈𝕍~u,v\in\widetilde{\mathbb{V}}, there existsδ>0\delta>0such that:𝐟​(Nδ​(u))¯∩𝐟​(Nδ​(v))¯=\varnothing,\overline{\mathbf{f}(N_{\delta}(u))}\cap\overline{\mathbf{f}(N_{\delta}(v))}=\varnothing,(10)

whereNδ​(x)=Bδ​(x)∩𝕍∗,Bδ​(x)={y∈𝕍~:d~​(x,y)<δ}.N_{\delta}(x)=B_{\delta}(x)\cap\mathbb{V}^{*},\quad B_{\delta}(x)=\{y\in\widetilde{\mathbb{V}}:\widetilde{d}(x,y)<\delta\}.(11)

Equivalently, distinct compactified input sequences possess neighborhoods whose finite-sequence traces are mapped by the reservoir into disjoint subsets of state space.

## .2Appendix B: Universality, readout learning, and task performance

## .2.1B.1. Universality for uniform approximations

Lethtarget:𝕍∗→ℝdh_{\mathrm{target}}:\mathbb{V}^{*}\to\mathbb{R}^{d}denote the target task. We assume thathtargeth_{\mathrm{target}}is the restriction to the finite-sequence space𝕍∗\mathbb{V}^{*}of a continuous function defined on the compactified input space𝕍~\widetilde{\mathbb{V}}. Givenε>0\varepsilon>0, we say that the reservoir map𝐟:𝕍∗→ℝN\mathbf{f}:\mathbb{V}^{*}\to\mathbb{R}^{N}is universal for uniform approximation if there exists a polynomial readoutp:ℝN→ℝdp:\mathbb{R}^{N}\to\mathbb{R}^{d}such that:supu∈𝕍∗‖htarget​(u)−(p∘𝐟)​(u)‖<ϵ.\sup_{u\in\mathbb{V}^{*}}\left\|h_{\mathrm{target}}(u)-(p\circ\mathbf{f})(u)\right\|<\epsilon.(12)

For scalar tasks this reduces componentwise to the corresponding scalar inequality.
We refer to the associated uniform error as the supremum-norm error (SEN).

## .2.2B.2. Benchmark tasks

Theorem-level universality is formulated for polynomial readouts, whereas the numerical benchmarks in the paper use linear readouts for computational economy.
The three tasks analyzed in Fig.3are one-step prediction, past reconstruction, and a fading-memory average.
For an input sequenceu=(u−T+1,…,u0)u=(u_{-T+1},\ldots,u_{0}), withggdenoting the discrete-time Lorenz flow map, the corresponding target maps arehtarget(1)​(u−T+1,…,u0)=g​(u0),\displaystyle h^{(1)}_{\rm target}(u_{-T+1},\ldots,u_{0})=g(u_{0}),(13)hk,target(2)​(u−T+1,…,u0)=u−k,0≤k≤T−1,\displaystyle h^{(2)}_{k,\rm target}(u_{-T+1},\ldots,u_{0})=u_{-k},\ 0\leq k\leq T-1,(14)

wheneverk<Tk<Tand equal to a fixed value ifk≥Tk\geq T(SI, Sec. S2.3),
andhtarget(3)​(u0,…,uT−1)=1T​∑n=0T−1βT−1−n​un,h^{(3)}_{\rm target}(u_{0},\ldots,u_{T-1})=\frac{1}{T}\sum_{n=0}^{T-1}\beta^{T-1-n}u_{n},(15)

for some1>β>01>\beta>0. For each sampled sequenceuu, letxu=𝐟​(u)∈ℝNx_{u}=\mathbf{f}(u)\in\mathbb{R}^{N}denote the final reservoir state and lethu=htarget​(u)∈ℝdh_{u}=h_{\rm target}(u)\in\mathbb{R}^{d}denote the corresponding target.
We fit a linear readoutπ:ℝN→ℝd\pi:\mathbb{R}^{N}\to\mathbb{R}^{d},π​(x)=A​x\pi(x)=Ax, by ridge regression on the training set𝕍train∗⊂𝕍∗\mathbb{V}^{*}_{\rm train}\subset\mathbb{V}^{*}:A∗=arg​minA∈ℝd×N⁡{∑u∈𝕍train∗‖A​xu−hu‖2+λ​‖A‖F2},A^{*}=\operatorname*{arg\,min}_{A\in\mathbb{R}^{d\times N}}\left\{\sum_{u\in\mathbb{V}^{*}_{\rm train}}\|Ax_{u}-h_{u}\|^{2}+\lambda\|A\|_{F}^{2}\right\},(16)

for a small ridge regression coefficientλ>0\lambda>0, and∥⋅∥F\|\cdot\|_{F}is the Frobenius norm.
Performance is then evaluated on a disjoint test set𝕍test∗⊂𝕍∗\mathbb{V}^{*}_{\rm test}\subset\mathbb{V}^{*}using the SEN,SEN=supu∈𝕍test∗‖A∗​𝐟​(u)−htarget​(u)‖.\mathrm{SEN}=\sup_{u\in\mathbb{V}^{*}_{\rm test}}\left\|A^{*}\mathbf{f}(u)-h_{\rm target}(u)\right\|.(17)

Thus, the benchmarks test whether the reservoir representation is sufficiently rich and regular for low-complexity readouts to approximate the target maps from finite data.

To complementarily quantify the goodness of predictions in time-series forecasting tasks for Fig.4, we used the Furthest Predicted Point (FPP)[30], and the standard Root-mean square error (RMSE): For the multi-step forecasting task, letu0:T−1=(u0,…,uT−1)∈𝕍T∗u_{0:T-1}=(u_{0},\ldots,u_{T-1})\in\mathbb{V}^{*}_{T}(18)

be an input sequence from the test set, and letxT=𝐟​(u0:T−1)x_{T}=\mathbf{f}(u_{0:T-1})be the corresponding reservoir state. Starting fromxTx_{T}, we generate an autonomous prediction by closing the loop through the trained readoutπ:ℝN→ℝd\pi:\mathbb{R}^{N}\to\mathbb{R}^{d}:u^T=π​(xT),\widehat{u}_{T}=\pi(x_{T}),(19)

and, fork≥0k\geq 0,x^T=xT,\displaystyle\widehat{x}_{T}=x_{T},(20)x^T+k+1=ϕ​(ρ​Wres​x^T+k+ε​Win​u^T+k),\displaystyle\widehat{x}_{T+k+1}=\phi\!\left(\rho W^{\mathrm{res}}\widehat{x}_{T+k}+\varepsilon W^{\mathrm{in}}\widehat{u}_{T+k}\right),(21)u^T+k+1=π​(x^T+k+1).\displaystyle\widehat{u}_{T+k+1}=\pi(\widehat{x}_{T+k+1}).(22)

The true continuation is denoted byuT+k=gk+1​(uT−1),u_{T+k}=g^{k+1}(u_{T-1}),

whereggis the discrete-time Lorenz flow map. Given a toleranceηFPP>0\eta_{\mathrm{FPP}}>0, the Furthest Predicted Point is defined as
the largest prediction time-step for which the forecast remains within
that tolerance:FPP=max⁡{K>0:‖u^T+k−uT+k‖2≤ηFPP,∀k≤K}.\mathrm{FPP}=\max\left\{K>0:\|\widehat{u}_{T+k}-u_{T+k}\|_{2}\leq\eta_{\mathrm{FPP}},\forall k\leq K\right\}.

Thus, FPP measures the length of the time interval over which the
closed-loop reservoir prediction remains accurate. As a complementary error measure, we compute the root-mean-square error (RMSE) over a maximum lengthKmaxK_{\max}:RMSE=(1Kmax+1​∑k=0Kmax‖u^T+k−uT+k‖22)1/2.\mathrm{RMSE}=\left(\frac{1}{K_{\max}+1}\sum_{k=0}^{K_{\max}}\|\widehat{u}_{T+k}-u_{T+k}\|_{2}^{2}\right)^{1/2}.

Both FPP and RMSE are then averaged over the test sequences.

## .2.3B.3. Driven regimes and practical neighborhood separation

We summarize why the three non-marginal driven regimes—strong contraction,
strong instability/mixing, and saturation—are unfavorable for the
finite-resolution form of neighborhood separation needed for stable
interpolation. The point is not that each regime necessarily violates NSP as
an exact topological property, but rather that each one obstructs its practical,
computationally useful realization.

## (i) Strongly contractive driven regime (MLE≪0\mathrm{MLE}\ll 0).

In a strongly contractive regime, the influence of remote input coordinates is
rapidly attenuated. Sequences that differ mainly far from the readout time can
therefore be mapped to nearly indistinguishable reservoir states. The
representation behaves as an effective finite-memory encoder: it retains only a
short recent window and suppresses distinctions carried by the distant past.
The limiting caseρ=0\rho=0makes this collapse explicit, since the state
depends only on the last input coordinate. For small recurrence, the same
effect appears perturbatively, because low-order terms inρ\rhotransmit
information only from a finite recent window.

## (ii) Strongly unstable or mixing driven regime.

The opposite regime is not characterized by insufficient separation, but by
uncontrolled separation. Strong instability can amplify small input differences,
but nearby input neighborhoods may then be stretched, folded, or mixed into
highly distorted subsets of reservoir space. As a result, nearby sequences need
not remain coherent in state space, and close reservoir states may originate
from unrelated input sequences. This destroys the local geometry required for
reliable low-complexity interpolation.

## (iii) Saturation regime.

For large effective gain, many state components approach the boundary of the
activation range. Input perturbations are then filtered by the derivative of the
activation function, which forϕ=tanh\phi=\tanhbecomes exponentially small in
saturated directions. Thus, the components that dominate the state vector are
also the least responsive to changes in the input. Persistent saturation
therefore produces a form of geometric collapse: distinct sequences may induce
only small state variations because input sensitivity is suppressed by the
bounded nonlinearity.

## (iv) Marginal driven stability.

Near marginal driven stability, input perturbations are neither rapidly erased
nor explosively amplified. The representation varies over input neighborhoods
in a controlled but non-degenerate way: sequences remain distinguishable without
producing unstable geometry. This is the regime in which finite-resolution
proxies of NSP are expected to be both observable and useful. The response clouds
are sufficiently spread out to support interpolation, while retaining enough
local coherence for linear or low-degree polynomial readouts to generalize.

## 


- 


Major funding support from
