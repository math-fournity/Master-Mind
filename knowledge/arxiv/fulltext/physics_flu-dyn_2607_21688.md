# Explainable quantum-compressed machine learning for complex fluid flows

**arXiv ID**: 2607.21688v1
**Authors**: Xiao Xue, Maida Wang, Mingyang Gao, Minh Chung, Peter V. Coveney
**Published**: 2026-07-23
**Categories**: physics.flu-dyn, cs.LG, quant-ph
**HTML URL**: https://arxiv.org/html/2607.21688v1

## Abstract

Machine-learning surrogates of physical systems face a paradox: explainable models facing the challenge of expressivity to capture complex nonlinear flows, whereas expressive deep surrogates match high-fidelity simulations only through massive parameterisations that turn the learned dynamics into a black box. Here, we introduce quantum-compressed machine learning (QCML), which resolves this tension by compressing the latent propagator of a flow surrogate from $524{,}288$ trainable parameters to no more than $8$. This parameter reduction brings the learned dynamical law to the parameter scale of a physical constitutive relation rather than a black-box neural network, making the surrogate directly interpretable and controllable without sacrificing expressivity. The compression is realised by a structured quantum circuit whose unitary propagator constrains the latent spectrum to the unit circle exactly and by construction, replacing exponential error growth with linear accumulation over autoregressive rollouts. Classical regularisation only approximates this constraint: even a quantum-inspired classical baseline penalised towards unitarity collapses within one Lyapunov time on turbulent channel flow, whereas QCML remains stable over the full rollout. Shared phase and coupling angles parameterising the circuit correspond directly to modal frequencies and inter-mode interactions, giving the learned dynamics a physical interpretation in spectral space. On two patient-specific cardiovascular benchmarks, the structured QCML propagator matches the predictive accuracy of its classical counterpart on surface pressure spectra, pressure drop, and wall shear stress. These results establish QCML as a working component of scientific machine learning and a concrete contribution towards practical quantum advantage in real-world prediction.

## Full Text

Explainable quantum-compressed machine learning for complex fluid flows

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
- License: CC BY 4.0arXiv:2607.21688v1 [physics.flu-dyn] 23 Jul 2026††thanks:†These authors contributed equally as the first author.

## Explainable quantum-compressed machine learning for complex fluid flowsXiao Xue†Centre for Computational Science, University College London, London, UKMaida Wang†Centre for Computational Science, University College London, London, UKMingyang GaoCentre for Computational Science, University College London, London, UKMinh ChungLeibniz Supercomputing Centre of the Bavarian Academy of Sciences and Humanities,
Boltzmannstraße 1, 85748 Garching, GermanyPeter V. Coveneyp.v.coveney@ucl.ac.ukCentre for Computational Science, University College London, London, UKCentre for Advanced Research Computing, University College London, London, UK

## Abstract

Machine-learning surrogates of physical systems face a paradox: explainable models facing the challenge of expressivity to capture complex nonlinear flows, whereas expressive deep surrogates match high-fidelity simulations only through massive parameterisations that turn the learned dynamics into a black box. Here, we introduce quantum-compressed machine learning (QCML), which resolves this tension by compressing the latent propagator of a flow surrogate from524,288524{,}288trainable parameters to no more than88. This parameter reduction brings the learned dynamical law to the parameter scale of a physical constitutive relation rather than a black-box neural network, making the surrogate directly interpretable and controllable without sacrificing expressivity. The compression is realised by a structured quantum circuit whose unitary propagator constrains the latent spectrum to the unit circle exactly and by construction, replacing exponential error growth with linear accumulation over autoregressive rollouts. Classical regularisation only approximates this constraint: even a quantum-inspired classical baseline penalised towards unitarity collapses within one Lyapunov time on turbulent channel flow, whereas QCML remains stable over the full rollout. Shared phase and coupling angles parameterising the circuit correspond directly to modal frequencies and inter-mode interactions, giving the learned dynamics a physical interpretation in spectral space. On two patient-specific cardiovascular benchmarks, the structured QCML propagator matches the predictive accuracy of its classical counterpart on surface pressure spectra, pressure drop, and wall shear stress. These results establish QCML as a working component of scientific machine learning and a concrete contribution towards practical quantum advantage in real-world prediction.

## IMain

Predicting how nonlinear physical systems evolve in time is a central problem of computational science, spanning turbulence in engineering[1], climate dynamics[2,3], astrophysics[4,5], and blood flows in cardiovascular medicine[6,7]. High-performance computing (HPC) now resolves such systems at unprecedented fidelity, yet each simulation routinely consumes tens of thousands of HPC node hours per second of physical time, far exceeding most decision-making timescales[8,9,10,11].
Artificial intelligence for science has matured in response, producing deployable surrogate models for fluid mechanics[12,13], weather[14,15]and biomedical applications[16,17,18]. Representative families include physics-informed neural networks[19], neural operators[20]and broader scientific machine-learning architectures that learn solution maps directly from simulation or observational data[21,22].
Quantum computing offers a complementary route: quantum algorithms provide potential speed-ups for linear quantum dynamics, most prominently the Schrödinger equation, and related ideas have been extended to broader classes of linear partial differential equations (PDEs)[23,24]. Nonlinear physical flows are substantially harder: quantum evolution is linear and unitary, whereas fluid dynamics involves nonlinear transport, dissipation and multiscale closure. Although quantum algorithms for nonlinear PDEs and computational fluid dynamics (CFD) have been proposed, existing demonstrations remain largely limited to low-dimensional model equations or simplified flows[25,26,27,28,29]. Direct quantum CFD therefore remains a longer-term target for fault-tolerant devices. Across these efforts, the central challenge persists: building surrogates of nonlinear physical flows that are not only reliable and fast but also stable over long prediction horizons, parameter-efficient, and transparent in the way they learn the dynamics.

Existing surrogate-modelling families address parts of this challenge, but none address all of it. Reduced-order models built from physical priors expose interpretable spectral structure and admit principled stability arguments. Representative examples include proper-orthogonal-decomposition projections and classical Koopman and dynamic-mode-decomposition approximations[30,31,32,33]. Their nonlinear capacity is, however, bounded by the chosen basis, which limits their ability to resolve the spatially complex, potentially turbulent multiscale flow structures that govern many real applications. Neural operators and deep learning surrogates, including Fourier neural operators[20]and DeepONet[34], recover nonlinear behaviour with comparatively little inductive bias[35,36,6]. Their accuracy, however, relies on millions to billions of trainable parameters whose individual roles remain opaque, eroding the interpretability needed to trust predictions in safety-critical settings. Autoregressive rollouts compound the problem: without an intrinsic stability mechanism, prediction errors accumulate silently across long time horizons[37].

The alternative near-term route is hybrid quantum-classical learning, in which quantum processors act not as standalone PDE solvers but as components inside classical scientific machine-learning pipelines[38,39]. This route introduces its own design challenges. Variational quantum circuits are shallow enough for present devices, but their usefulness depends critically on the ansatz. Generic hardware-efficient ansatz families can suffer from barren plateaus with exponentially small gradients, while problem-agnostic circuits provide few spectral or physical properties[40,41,25].
A problem-matched quantum prior, by contrast, can be genuinely informative: quantum-informed machine learning shows that such a prior can guide classical machine-learning systems toward more physical solutions and improve their efficiency and accuracy[42,24].
In that setting the quantum prior is coupled loosely, shaping training from outside the main learning loop while the latent dynamics of the classical model remains heavily parameterised and effectively a black box, so the end-to-end pipeline is also opaque. What has been missing is an end-to-end quantum-classical loop, compressing the latent dynamics into a small, interpretable set of parameters for real-world physical-flow surrogacy. Across these families, three needs remain unmet at once: stable long-horizon rollout, parameter efficiency and explainable latent dynamics.

Here we introduce quantum-compressed machine learning (QCML), a hybrid quantum-classical framework summarised in Fig.1a. A classical transformer encoder–decoder[43]maps physical states into a compressed quantum latent space, and a structured quantum circuit propagates this latent representation in time. The central design principle is extreme parameter compression: a structured ansatz shares two trainable scalars per layer across all qubits and edges, reducing the latent propagator from ca.525,000525{,}000trainable parameters in the classical baseline to as few as88, a66,00066{,}000-fold reduction that brings the learned dynamical law to the parameter scale of a physical governing equation rather than a black-box neural network[44,45,46,47](Fig.1a, top-right inset). This compression delivers the capabilities that existing surrogates lack. Long-horizon stability follows from the unitarity of the quantum propagator, which pins latent eigenvalues to the unit circle and replaces exponential error growth with linear accumulation over autoregressive rollouts[48,49,50,30,51,32,33](Fig.1a, top-left inset); this constraint holds as an operator identity for every parameter value, whereas classical surrogates can only approximate it through soft spectral penalties whose residual drift compounds over the rollout (See Methods). The same parameter sharing mitigates the barren-plateau pathology of generic variational circuits[40,52,53]and tightens the generalisation bound[54], keeping the model trainable in the small-data regime of physical-flow surrogacy (see Methods).
Explainability follows from the compression itself: with only a few trainable parameters, each corresponding to an identifiable modal frequency or inter-mode coupling strength, the learned propagator becomes directly readable, unlike the opaque weight matrices of classical surrogates.

We evaluate QCML on three nonlinear systems of increasing complexity: turbulent channel flow inflow, stenotic aortic flow, and patient-specific abdominal aortic aneurysm haemodynamics (Fig.1b)[6,7,8]. With only88trainable quantum parameters in the structured variant, QCML matches the predictive accuracy of the classical ML baseline on the diagnostically relevant quantities: velocity spectra for turbulence, pressure drop for the stenotic flow, and wall shear stress for the aneurysm. On a noise-aware classical emulator of the structured circuit, per-cardiac-cycle inference is several orders of magnitude cheaper than the∼3.4​h{\sim}3.4\,\mathrm{h}required per cycle on1,0241{,}024CPU cores under conventional CFD[8]; we report this as the algorithmic cost of the latent propagation, which excludes the state-preparation, measurement-shot and classical–quantum data-transfer overheads of present quantum hardware (Supplementary S3.6). Backend validation on IQM’s 54-qubit Emerald processor yields79.69%79.69\%one-step agreement for turbulent channel flow; the two cardiovascular benchmarks, evaluated on a noise-aware emulator, reach95.54%95.54\%and95.25%95.25\%agreement respectively (Table1). To our knowledge, these results demonstrate the first hybrid quantum-classical surrogate for application-scale nonlinear physical flows, spanning turbulence and patient-specific cardiovascular haemodynamics, and point to integrated quantum-HPC workflows as a practical near-term route to broader deployment.Figure 1:QCML framework for nonlinear physical flows.(a) Hybrid quantum–classical training loop. A transformer encoder maps the input fieldu​(𝐱,t)u(\mathbf{x},t)into a compact latent representation; this latent state is embedded into a quantum Hilbert space, propagated forward by a structured unitaryUqU_{q}, and decoded back into a transformer decoder that returns the next-step fieldu​(𝐱,t+1)u(\mathbf{x},t+1). Left inset: latent-norm behaviour under different spectral radiiρ\rho;ρ=1\rho=1(unitary) keeps the observable bounded over the rollout, whereasρ<1\rho<1andρ>1\rho>1produce vanishing and exploding regimes. Centre: Bloch-sphere sketch of the latent state evolving underUqU_{q}; the equatorial(x,y)(x,y)plane spans the real and imaginary parts of the off-diagonal coherence and the polarzzaxis encodes the populations, soUqU_{q}traces a norm-preserving trajectory on the unit sphere despite being a complex-valued operator. Right inset: structured ansatz design, showing the Hamiltonian operator that generatesUqU_{q}, the sparse coupling graph, and two design properties: as few as88trainable parameters through parameter sharing, and interpretable phase and coupling parameters.
(b) Three benchmark systems of increasing complexity: 3D turbulent channel flow, stenotic aortic flow, and patient-specific abdominal aortic aneurysm haemodynamics.

## IITurbulent channel flow inflow generation

Turbulent channel flow atR​eτ=180Re_{\tau}=180is a canonical chaotic benchmark for extended autoregressive rollouts[55,56,13,57]. We use it to test whether the unitary latent dynamics of QCML translate into stable long-horizon prediction. Rollout time is reported in dimensionless formt∗=t/Tλt^{*}=t/T_{\lambda}, withTλT_{\lambda}the Lyapunov time of the resolved ground-truth field (Supplementary S2.1). Two QCML variants are reported throughout. Both share the same transformer encoder–decoder backbone and act onNq=9N_{q}=9qubits throughLLvariational layers, but differ in the quantum ansatz. The structured variant QCML (S) uses a structured circuit in which each layer applies a shared mode-wise phase rotation on every qubit followed by a shared coupling on every edge of a sparse graph, leaving only2​L2Ltrainable scalars per circuit (Methods, Eq. (5)). The baseline variant QCML uses a generic hardware-efficient circuit, with an independent general single-qubit rotation on every qubit and a fixed entangling ring in each layer, giving3​L​Nq3LN_{q}trainable parameters and no trainable couplings. Comparing the two isolates the effect of imposing Koopman-inspired structure rather than merely reducing the parameter count. The detailed gate-level definitions and per-case counts are given in Supplementary S3.4 and S4.

Figure2a sketches the simulation that generated the training, validation and test data: a streamwise-driven 3D turbulent channel flow with no-slip top and bottom walls and periodic streamwise/spanwise boundaries[58]. Once the flow had reached a statistically stationary turbulent regime, 320 two-dimensional trajectories of wall-normal velocity were recorded on the mid-plane at192×192192\times 192resolution and downsampled to64×6464\times 64; the full data-generation protocol is given in SI S2.1. The 320 realisations were partitioned 80/10/10 into training, validation and test sets. The classical ML baseline[42]was trained on the same split for comparison.

All surrogates were evaluated under an autoregressive window-rollout protocol𝐮^t+1:t+k=fθ​(𝐮t−k+1:t)\hat{\mathbf{u}}_{t+1:t+k}=f_{\theta}(\mathbf{u}_{t-k+1:t}), in which a window ofkkconsecutive snapshots of the predicted field𝐮\mathbf{u}is mapped to the nextkkand the model is then advanced on its own predictions without further reference input (Supplementary S3.5). Starting from a reference initial window, the rollout was carried out to five Lyapunov times (t∗≈5t^{\ast}\approx 5). Figure2b shows instantaneous velocity fields at five instants along this rollout against the ground-truth large-eddy lattice Boltzmann reference, in which a Smagorinsky closure is embedded into the lattice Boltzmann collision step[59,60,61]. Classical ML lost near-wall streaks already byt∗≈1t^{\ast}\approx 1and relaxed toward a nearly featureless mean-like field for the rest of the rollout. Both QCML variants kept the large-scale streaks and boundary-layer coherence visible in the reference out tot∗=5.27t^{\ast}=5.27, with QCML (S) marginally cleaner than QCML at late times. Unitarity fixes the latent norm by construction (Methods, Sec. “Stability against exploding and vanishing gradients”), which sustained coherent fluctuations across the plotted window for both QCML variants but was absent in classical ML.

Spectral and statistical diagnostics over the same turbulent-inflow rollout corroborate this stability; the formal definitions of all metrics reported here and in subsequent figures are collected in SI S6. Figure2c shows that both QCML variants overlap the reference spectrum⟨E​(k)⟩\langle E(k)\rangleover more than a decade of wavenumber space, whereas classical ML overshoots the reference at highkkand accumulates spurious small-scale energy. In Fig.2d, the mean streamwise velocity in wall units lies on the direct numerical simulation (DNS) reference and the log law atR​eτ=180Re_{\tau}=180for every model, indicating that the wall-normal profile is recovered correctly by both QCML variants and the classical baseline. Figure2e then shows that both QCML variants reproduce the bulk-flow density of the reference around the peak atu≈0.027u\approx 0.027in lattice Boltzmann units (LBU; conversion to physical SI units is detailed in SI S1), whereas classical ML sharpens this peak and underpopulates the tails, consistent with the loss of small-scale variability already visible in Fig.2b; the agreement is achieved without any distribution-matching loss in training.Figure 2:QCML on long-rollout turbulent channel flow.Blue, green, purple and red denote the reference data, classical ML, QCML and QCML (S), respectively; in paneld, grey and black dashed curves indicate DNS and the logarithmic law.
(a) Three-dimensional channel setup: no-slip top and bottom walls, periodic streamwise/spanwise boundaries; the highlighted plane is the mid-plane on which the surrogate is learned.
(b) Instantaneous velocity-field snapshots at Lyapunov-normalised timest∗∈{0.00,1.29,2.62,3.95,5.27}t^{\ast}\in\{0.00,\,1.29,\,2.62,\,3.95,\,5.27\}, with rows showing, from top to bottom, the reference, classical ML, QCML and QCML (S).
(c) Time-averaged isotropic energy spectrum⟨E​(k)⟩\langle E(k)\rangleversus wavenumberkk.
(d) Mean streamwise velocity profileu+u^{+}versus wall-normal coordinatey+y^{+}, with DNS and the log law atR​eτ=180Re_{\tau}=180as auxiliary references.
(e) Pixel-wise velocity density on the mid-plane (LBU).
(f) Cumulative turbulent kinetic-energy error relative to the reference (relativeL2L_{2}) versust∗t^{\ast}.

Figure2f tracks how the surrogates evolve through the rollout via the cumulative turbulent-kinetic-energy (TKE) error relative to the reference (definition in Supplementary Information S6.2). Both QCML variants start above unity att∗=0t^{\ast}=0, decrease rapidly within the first Lyapunov time, apart from a brief transient excursion of QCML neart∗≈0.7t^{\ast}\approx 0.7, and settle to a plateau of∼0.6{\sim}0.6for the remainder of the rollout, indicating statistical convergence of the surrogate state toward the reference attractor. Classical ML, by contrast, stays pinned at unity throughout: a flat TKE error at11corresponds to a vanishing predicted TKE, that is, a near-zero coherent-fluctuation field, consistent with the stagnant, mean-like snapshots already visible in Fig.2b. Notably, the classical baseline is itself trained with a soft unitarity penalty‖𝐊⊤​𝐊−𝐈‖F2\|\mathbf{K}^{\top}\mathbf{K}-\mathbf{I}\|_{F}^{2}on its latent propagator[42], so its collapse is not an artefact of an unregularised comparison: a soft penalty is minimised only up to optimisation tolerance and leaves a residual spectral drift that compounds over the rollout, whereas the unitarity ofUqU_{q}holds exactly for every parameter value. The two trajectories therefore separate by mechanism rather than by tuning, and we show in Methods, Sec. “Stability against exploding and vanishing gradients” why QCML is norm-preserving by construction whereas a classical latent operator, even a spectrally regularised one, can collapse under autoregressive rollout.

## IIIStenotic aortic flow

Stenosis of the aorta concentrates the haemodynamic challenge onto a single focal lesion. A40%40\%diameter reduction in the thoracic aorta accelerates the local jet to∼1.8​m​s−1{\sim}1.8\,\mathrm{m\,s^{-1}}, destabilises the distal shear layer and produces a pressure drop across the throat[6,7]. This throat pressure drop is the primary clinical biomarker for haemodynamic severity, so a surrogate must be validated on three quantities at once: the global pressure morphology across the cardiac phase, the multi-scale energy cascade inherited from the disturbed shear layer and the localised pressure drop across the throat.

Figure3a sketches the simulation and surrogate-modelling pipeline[62]. Pulsatile blood flow through a patient-specific thoracic aorta[63]with a localised40%40\%stenotic throat was simulated with the HemeLB lattice Boltzmann solver[11,64,65]at100​μ​m100\,\mu\mathrm{m}resolution, producing twenty independent trajectories of five cardiac cycles each, i.e.100100cardiac cycles of haemodynamic data in total. The three-dimensional surface pressure field on the curved aortic wall was then UV-unwrapped onto a two-dimensional map across the throat region of interest (ROI), and this 2D map is the field that all surrogates predict. The twenty trajectories were partitioned75/10/1575/10/15into independent training, validation and test sets; the full data-generation protocol, including the20​μ​m20\,\mu\mathrm{m}DNS reference used to validate the LES-LBM resolution, is given in Supplementary S2.2. Five representative cardiac instantst^1\hat{t}_{1}–t^5\hat{t}_{5}, spanning systolic acceleration, peak systole, distal shear-layer formation, late systole and diastolic relaxation, are marked along the pulsatile pressure waveform in Fig.3b. All surrogates were evaluated under the same autoregressive window-rollout protocol𝐮^t+1:t+k=fθ​(𝐮t−k+1:t)\hat{\mathbf{u}}_{t+1:t+k}=f_{\theta}(\mathbf{u}_{t-k+1:t})as in Sec.II(Supplementary S3.5), advanced from a reference initial window over∼3.9{\sim}3.9cardiac cycles without further reference input.

Figure3c shows that both QCML variants maintain low relativeL2L_{2}rollout error (Supplementary S6.1) over multi-cycle prediction, on a par with the classical ML baseline. Away from brief phase-transition intervals, the error remains at the few-percent level, and the occasional sharp excursions are temporally localised and rapidly decay within the same cardiac cycle. The QCML and QCML (S) curves exhibit nearly overlapping envelopes throughout the rollout, indicating that the structured ansatz preserves the long-horizon accuracy of QCML without introducing monotonic error accumulation. Figure3d provides a point-wise comparison at five representative cardiac phasest^1\hat{t}_{1}–t^5\hat{t}_{5}. Classical ML and both QCML variants reproduce the systolic, diastolic and late-cycle pressure morphology of the reference, and the absolute-error map of the structured variant,|err|​(S)|\mathrm{err}|(\mathrm{S}), remains much smaller than the local pressure amplitude, with residuals mainly confined to the stenotic jet region.Figure 3:QCML on stenotic aortic haemodynamics.Line colours denote the reference, classical ML baseline, QCML and QCML (S) in blue, green, purple and red, respectively, unless otherwise stated.
(a) Patient-specific stenosis of the aorta geometry; the 3D pressure field is UV-unwrapped onto a 2D map across the throat ROI.
(b) Reference pressure waveform versus normalised cardiac phaset^/T\hat{t}/T, with five diagnostic instantst^1\hat{t}_{1}–t^5\hat{t}_{5}.
(c) RelativeL2L_{2}rollout error versust^/T\hat{t}/Tover a∼3.9{\sim}3.9-cycle horizon, normalised by120​mmHg120\,\mathrm{mmHg}; shaded bands are one s.d. acrossN=3N{=}3held-out trajectories, dotted vertical lines mark integer cycles.
(d) Per-phase pressure fields att^1\hat{t}_{1}–t^5\hat{t}_{5}(columns), with rows showing the reference, classical ML, QCML, QCML (S), and the absolute-error map|err|​(S)|\mathrm{err}|(\mathrm{S})of QCML (S) (mmHg).
(e) Time-averaged radial energy spectrum⟨E​(k)⟩\langle E(k)\rangleversus wavenumberkk.
(f) Pixel-wise pressure density over all valid pixels and rollout frames (mmHg).
(g) Throat-ROI pressure dropΔ​p\Delta ppooled overN=3N{=}3trajectories and∼3.9{\sim}3.9cycles, for the reference, classical ML and both QCML variants; markers denote the mean, thick whiskers±1\pm 1s.d., thin whiskers the full range.
(h) Trainable latent-propagator parameter count for classical ML, QCML and QCML (S).

Spectral and statistical diagnostics over the same rollout corroborate this agreement. Figure3e shows that the time-averaged spectrum⟨E​(k)⟩\langle E(k)\rangleof both QCML variants tracked the reference over more than a decade of wavenumber space, with the two variants indistinguishable across the entirekk-range. Figure3f shows that the pressure density of QCML (S) overlapped the reference within line width across the whole pressure range, including both the dominant peak near90​mmHg90\,\mathrm{mmHg}and the high-pressure shoulder above105​mmHg105\,\mathrm{mmHg}associated with peak systolic loading. QCML tracked the same distribution with only a slight overshoot at the main peak, whereas the classical ML baseline underestimated the peak density by around a fifth, showing that both QCML variants capture the pressure statistics more faithfully than the classical baseline, without any distribution-matching loss during training. Figure3g then evaluates the clinically decisive endpoint, the throat pressure dropΔ​p=p¯upstream−p¯downstream\Delta p=\bar{p}_{\mathrm{upstream}}-\bar{p}_{\mathrm{downstream}}, defined as the cross-sectionally averaged pressure on the upstream side of the throat minus that on the downstream side (Supplementary S6.6). The pooledΔ​p\Delta pdistributions of both QCML variants reproduce the reference mean and interquartile range; QCML (S) sits marginally closer to the reference median and spread than QCML, although the difference is small relative to sampling variability.
The parameter budget then separates the two variants in Fig.3h: the quantum-circuit parameter count drops from216216in QCML to1616in QCML (S), a∼13.5×{\sim}13.5\timescompression of the latent propagator at predictive accuracy that is essentially indistinguishable across Figs.3c–3g. The two variants use different ansätze (Supplementary S3.4): the generic QCML circuit carries3​L​Nq3LN_{q}trainable parameters, a general single-qubit rotation on every qubit plus a fixed entangling ring per layer (L=8L=8layers andNq=9N_{q}=9qubits give216216), whereas the structured QCML (S) keeps only2​L=162L=16scalars, one shared phaseαℓ\alpha_{\ell}and one shared couplingβℓ\beta_{\ell}per layer; the full structured ansatz and its layer-by-layer gate-level definition are given in Supplementary S4. The contrast isolates the contribution of the structured ansatz: imposing physical structure on the quantum latent removes more than an order of magnitude of trainable parameters without measurable cost on either point-wise fields or the haemodynamic biomarker.

## IVAbdominal aortic aneurysm haemodynamics

The abdominal aortic aneurysm (AAA) is the most clinically demanding setting in our evaluation. The flow is strongly pulsatile, the geometry is patient-specific, and the quantities most relevant to rupture-risk assessment, peak systolic pressure and local wall shear stress (WSS), are spatially concentrated and temporally transient[66,8]. A surrogate must therefore be accurate not only on average, but in the precise spatiotemporal regions where haemodynamic risk is highest.

Figure4a sketches the simulation and surrogate-modelling pipeline. Pulsatile blood flow through a single patient-specific AAA geometry[66], with one main aortic inlet, eight side-branch inlets and two outlets, was simulated with the HemeLB lattice Boltzmann solver[11,64]at100​μ​m100\,\mu\mathrm{m}resolution, producing twenty independent trajectories generated by uniformly shifting the inlet-waveform phase across the diastolic low-velocity window. Each trajectory advances for five cardiac cycles, yielding100100cardiac cycles of haemodynamic data in total. The aneurysm area of interest (AoI) was extracted from the full 3D geometry, and the 3D surface pressure and WSS fields on the AoI were UV-unwrapped onto matching 2D maps, which are the fields all surrogates predict. The twenty trajectories were partitioned80/10/1080/10/10into independent training, validation and test sets; the full data-generation protocol, including the branch boundary conditions and the sponge-layer configuration used to damp outflow acoustic reflections[67,68,69], is given in Supplementary S2.3. Four representative cardiac instantst^1\hat{t}_{1}–t^4\hat{t}_{4}, spanning systolic acceleration, peak systole, late systole and diastolic relaxation, are marked along the pulsatile inflow waveform in Fig.4b. QCML, QCML (S) and the classical ML baseline were evaluated under the same autoregressive rollout protocol𝐮^t+1:t+k=fθ​(𝐮t−k+1:t)\hat{\mathbf{u}}_{t+1:t+k}=f_{\theta}(\mathbf{u}_{t-k+1:t})(Supplementary S3.5), with the predicted field𝐮t=(pt,τtw)\mathbf{u}_{t}=(p_{t},\,\tau^{\mathrm{w}}_{t})jointly comprising the AoI pressure and WSS, and advanced from a reference initial window over five cardiac cycles without further reference input.

Figure4c compares the predicted pressure fields att^1\hat{t}_{1}–t^4\hat{t}_{4}against the reference. Both QCML and QCML (S) reproduced the elevated systolic field att^1\hat{t}_{1}and the low diastolic field att^3\hat{t}_{3}–t^4\hat{t}_{4}in magnitude and spatial localisation, and the absolute-error map|err|​(S)|\mathrm{err}|(\mathrm{S})of QCML (S) stayed an order of magnitude below the local field amplitude. Figure4d shows the WSS fields at the same instants: the peak stress concentration on the aneurysm wall att^1\hat{t}_{1}, which dominates rupture-risk evaluation, was recovered by both QCML variants with the correct hotspot location and intensity, with residuals concentrated outside the clinically critical region.

Distribution-level diagnostics over the same rollout corroborate this agreement; the formal definitions of the AAA biomarkers are given in Supplementary Information S6.5 (pixel-wise PDFs) and S6.7 (peak pressure and peak wall shear stress). Figure4e shows that the pressure density aggregated over the AoI traces the bimodal reference distribution for both QCML variants, including the high-pressure tail above160​mmHg160\,\mathrm{mmHg}associated with peak systolic loading; the two prediction curves overlap the reference within line width. Figure4f shows that both QCML variants reproduced the heavy-tailed WSS density of the reference, dominated by a sharp peak near baseline stress with a long tail toward elevated values, again with no distribution-matching loss during training.Figure 4:QCML on patient-specific abdominal aortic aneurysm haemodynamics.Line colours denote the reference, classical ML baseline, QCML and QCML (S) in blue, green, purple and red, respectively; field panels use the indicated pressure, stress and absolute-error colour bars.
(a) Patient-specific abdominal aortic aneurysm geometry; the 3D surface pressure and WSS fields on the area of interest (AoI) are UV-unwrapped onto matching 2D maps.
(b) Reference pressure waveform versus normalised cardiac phaset^/T\hat{t}/T, with four diagnostic instantst^1\hat{t}_{1}–t^4\hat{t}_{4}.
(c) Pressure fields over the AoI att^1\hat{t}_{1}–t^4\hat{t}_{4}(columns), with rows showing the reference, classical ML, QCML, QCML (S), and the absolute-error map|err|​(S)|\mathrm{err}|(\mathrm{S})of QCML (S) (mmHg).
(d) WSS fields at the same instants: same row layout as (c).
(e) Pixel-wise pressure density over the AoI (mmHg).
(f) Pixel-wise WSS-magnitude density over the AoI.
(g) Trainable latent-propagator parameter count for classical ML, QCML and QCML (S); the annotated ratio is the compression of QCML (S) relative to classical ML.
(h) Per-cycle latent-propagation cost for HPC compute, QCML and QCML (S), evaluated on a classical emulator of the quantum circuit.

The combination of parameter efficiency and inference speed is the most striking result. Figure4g shows that the classical baseline carries524,288524{,}288trainable latent parameters, QCML uses108108and QCML (S) only88, a∼65,536×{\sim}65{,}536\timescompression of the latent propagator from classical ML to the structured QCML variant at predictive accuracy that is indistinguishable across Figs.4c–4f. The three models use different latent propagators (Supplementary S3.4): classical ML uses a dense Koopman operator on aD=512D=512latent space, trained with a soft unitarity regulariser (2​D2≈5.24×1052D^{2}\approx 5.24\times 10^{5}entries across the forward and backward operators), the generic QCML circuit carries3​L​Nq3LN_{q}trainable parameters (L=4L=4layers andNq=9N_{q}=9qubits give108108), and the structured QCML (S) keeps only2​L=82L=8scalars, one shared phase and one shared coupling per layer; the full structured ansatz and its gate-level definition are given in Supplementary S4. Figure4h reports the per-cycle latent-propagation cost, evaluated on a classical emulator of the quantum circuit. Relative to the∼3.4​h{\sim}3.4\,\mathrm{h}required per cardiac cycle by the HPC CFD reference on1,0241{,}024CPU cores, both QCML variants reduce this algorithmic cost by several orders of magnitude. This figure quantifies the intrinsic inference complexity of the surrogate and deliberately excludes the state-preparation, measurement-shot and classical–quantum data-transfer overheads that would dominate an end-to-end run on present quantum hardware (Supplementary S3.6); it is therefore not a hardware wall-clock claim. Figure4g, the parameter compression, is a hardware-independent property of the model and carries the primary efficiency message: imposing physical structure on the quantum latent removes more than four orders of magnitude of trainable parameters without measurable cost on either point-wise fields or the haemodynamic distributions.

## VNoise-aware emulator and hardware validation

The results in Figs.2–4were obtained with a classical emulator of the structured quantum circuit. To assess backend robustness, the trained QCML (S) models were evaluated either on IQM’s 54-qubit Emerald processor or on a noise-aware emulator configured with the same device-noise profile (See Methods, Sec. “Hardware implementation and training”). Table1reports the backend and the one-step prediction agreement for each benchmark. Executed on Emerald, the turbulent-channel model retained79.69%79.69\%agreement with the reference under device noise. The stenotic-aorta and abdominal-aortic-aneurysm models, evaluated on the noise-aware emulator inside the same inference loop, reached95.54%95.54\%and95.25%95.25\%agreement respectively. Backend noise therefore degrades the one-step prediction but does not destroy it, and the trained models transfer across backends without retraining.Table 1:Backend validation of QCML (S) on the three benchmark flows. Agreement is defined as the complement of the one-step relativeL2L_{2}prediction error,agreement=(1−ℓrel​L2)×100%\mathrm{agreement}=(1-\ell_{\mathrm{rel}\,L_{2}})\times 100\%, whereℓrel​L2=‖y^−y‖2/‖y‖2\ell_{\mathrm{rel}\,L_{2}}=\|\hat{y}-y\|_{2}/\|y\|_{2}compares the predicted next frame with the reference next frame. Losses are summed within each batch and then averaged over the test-loader batches of the held-out trajectories; identity, backward and long-rollout losses are not included. The turbulent-channel case was evaluated on IQM’s 54-qubit Emerald superconducting quantum processor; the stenotic-aorta and abdominal-aortic-aneurysm cases were evaluated on a noise-aware emulator configured with the Emerald device-noise profile.Benchmark (diagnostic)BackendAgreementTurbulent channel flow inflowEmerald QPU79.69%79.69\%Stenotic aortaNoise-aware emulator95.54%95.54\%Abdominal aortic aneurysmNoise-aware emulator95.25%95.25\%

## VIConclusion

We have introduced quantum-compressed machine learning as a hybrid quantum-classical surrogate for nonlinear physical flows. A classical encoder-decoder learns a compact representation of the physical state, and a structured quantum propagator carries that representation forward in time on a small superconducting quantum processor. We evaluated the framework on three benchmarks of increasing complexity: turbulent channel flow under extended autoregressive rollouts, stenotic aortic flow with its associated pressure drop, and patient-specific abdominal aortic aneurysm haemodynamics. Across these benchmarks, QCML does more than reproduce the classical baseline: it maintains coherent turbulent structures over five Lyapunov times after the soft-unitarity-regularised classical model collapses, captures stenotic pressure statistics more faithfully, and preserves pressure and wall-shear-stress fidelity in patient-specific aneurysm haemodynamics, while reducing the latent-propagator parameter count from524,288524{,}288to∼108{\sim}108in QCML and to as few as88in QCML (S). On a classical emulator of the quantum circuit, per-cycle inference takes∼1.69​s{\sim}1.69\,\mathrm{s}for QCML (S), compared with∼3.4​h{\sim}3.4\,\mathrm{h}per cardiac cycle for conventional CFD on1,0241{,}024CPU cores, corresponding to a∼7,300×{\sim}7{,}300\timesreduction in algorithmic inference cost.

Three advantages underlie these results. Long-horizon stability follows from the unitarity of the latent propagator, which pins its spectrum to the unit circle by construction and suppresses the compounding term that dominates autoregressive surrogate error; the turbulent-channel benchmark shows that approximate spectral regularisation does not substitute for this exact constraint. Parameter efficiency follows from the structured circuit, whose mode-wise rotations and sparse inter-mode couplings compress the latent propagator by more than four orders of magnitude without measurable loss of expressive power, as the structured variant matches the unshared QCML on the haemodynamic biomarkers. Explainability follows from the same structure: the trainable parameters map one-to-one onto identifiable mode frequencies and inter-mode interactions, in contrast to the opaque dense matrices of neural latents.

Three directions remain open for scaling the framework towards deployment: tighter integration of quantum processors with HPC clusters over low-latency interconnects, to reduce the classical–quantum data-exchange overhead, which becomes limiting at larger circuit sizes; structured circuits with higher qubit counts and richer connectivity graphs, opening a path from the two-dimensional projections treated here to volumetric, patient-specific flows; and the transition to early fault-tolerant processors, which will lift the noise floor that currently limits hardware fine-tuning depth. For safety-relevant nonlinear systems, where transparent latent dynamics are a deployment prerequisite rather than an afterthought, a surrogate that is at once parameter-efficient, structurally stable and directly explainable offers a credible path towards trustworthy hybrid quantum-classical prediction.

## Methods

## VI.1Hybrid quantum–classical architecture

QCML reformulates the Koopman learning paradigm by realising the latent evolution of dynamical systems within a quantum-mechanical representation. Instead of representing the learned linear dynamics as an explicit classical matrix operator, it implements latent propagation through a structured unitary transformation acting in a quantum Hilbert space, followed by observable-based reconstruction in the latent space.

For a discrete-time dynamical system𝐮t+1=f​(𝐮t),\mathbf{u}_{t+1}=f(\mathbf{u}_{t}),(1)

the Koopman operator𝒦\mathcal{K}acts linearly on observablesg:ℳ→ℂg:\mathcal{M}\rightarrow\mathbb{C}as(𝒦​g)​(𝐮)=g​(f​(𝐮)),(\mathcal{K}g)(\mathbf{u})=g(f(\mathbf{u})),(2)

whereℳ⊂ℝd\mathcal{M}\subset\mathbb{R}^{d}denotes the physical state space. In data-driven Koopman learning, an encoder-decoder pair(ϕ,ψ)(\phi,\psi)constructs a finite-dimensional latent representation in which nonlinear dynamics are approximately linear:𝐳t+1≈UK​𝐳t,𝐮^t=ψ​(𝐳t),\mathbf{z}_{t+1}\approx U_{K}\mathbf{z}_{t},\qquad\hat{\mathbf{u}}_{t}=\psi(\mathbf{z}_{t}),(3)

where𝐳t=ϕ​(𝐮t)∈𝒵\mathbf{z}_{t}=\phi(\mathbf{u}_{t})\in\mathcal{Z}is the latent coordinate andUKU_{K}approximates the Koopman propagator in the latent space𝒵\mathcal{Z}.

In QCML, the latent space𝒵\mathcal{Z}is embedded into a quantum Hilbert spaceℋNq\mathcal{H}_{N_{q}}consisting ofNqN_{q}qubits. Under amplitude encoding, the latent dimension satisfiesk=2Nqk=2^{N_{q}}[70]. The latent state𝐳t\mathbf{z}_{t}is mapped to a quantum state|ψin​(𝐳t)⟩∈ℋNq|\psi_{\mathrm{in}}(\mathbf{z}_{t})\rangle\in\mathcal{H}_{N_{q}}, and its evolution is implemented through a unitary operatorUq​(𝜽)U_{q}(\bm{\theta})acting on the quantum register:|ψout⟩=Uq​(𝜽)​|ψin​(𝐳t)⟩,𝐳t+1=ℛ​(|ψout⟩),|\psi_{\mathrm{out}}\rangle=U_{q}(\bm{\theta})|\psi_{\mathrm{in}}(\mathbf{z}_{t})\rangle,\qquad\mathbf{z}_{t+1}=\mathcal{R}\!\left(|\psi_{\mathrm{out}}\rangle\right),(4)

whereℛ​(⋅)\mathcal{R}(\cdot)denotes the observable-based reconstruction map, implemented through expectation values of a fixed set of measurement observables𝐎^\hat{\mathbf{O}}(see Supplementary Information S4 for the explicit choice).

The headline propagator, QCML (S), is constructed from a structured circuit. Rather than employing a generic hardware-efficient ansatz, we restrict the generators of the evolution to operators corresponding to mode-wise single-qubit rotations and structured inter-mode coupling. Specifically, the structured unitary operator is drawn from the familyUq​(𝜽)=∏ℓ=1L(∏i=1Nqe−i​αℓ,i​Xi)​(∏(i,j)∈Ee−i​βℓ,(i,j)​(Xi​Xj+Yi​Yj)),U_{q}(\bm{\theta})=\prod_{\ell=1}^{L}\left(\prod_{i=1}^{N_{q}}e^{-i\alpha_{\ell,i}X_{i}}\right)\left(\prod_{(i,j)\in E}e^{-i\beta_{\ell,(i,j)}(X_{i}X_{j}+Y_{i}Y_{j})}\right),(5)

whereXiX_{i}generates a mode-wise phase rotation of theii-th latent mode andXi​Xj+Yi​YjX_{i}X_{j}+Y_{i}Y_{j}induces structured coupling between modes adjacent on a sparse graphEE. QCML (S) ties these parameters within each layer, sharing one phaseαℓ\alpha_{\ell}across all qubits and one strengthβℓ\beta_{\ell}across all edges, so the trainable set reduces to𝜽={αℓ,βℓ}ℓ=1L\bm{\theta}=\{\alpha_{\ell},\beta_{\ell}\}_{\ell=1}^{L}with only2​L2Lscalars (Fig.5b). The baseline variant QCML instead uses a generic hardware-efficient circuit, a general single-qubit rotation (three Euler angles) on every qubit followed by a fixed entangling ring in each layer, giving3​L​Nq3LN_{q}trainable parameters and no trainable couplings; comparing the two isolates the contribution of the imposed structure.

The unitarity of the quantum propagator is guaranteed by construction,Uq​(𝜽)†​Uq​(𝜽)=IU_{q}(\bm{\theta})^{\dagger}U_{q}(\bm{\theta})=I, which preserves the norm of the encoded quantum state:⟨ψout|ψout⟩=⟨ψin​(𝐳t)|ψin​(𝐳t)⟩.\langle\psi_{\mathrm{out}}|\psi_{\mathrm{out}}\rangle=\langle\psi_{\mathrm{in}}(\mathbf{z}_{t})|\psi_{\mathrm{in}}(\mathbf{z}_{t})\rangle.(6)

All eigenvalues ofUq​(𝜽)U_{q}(\bm{\theta})therefore lie on the unit circle,λj=ei​ωj\lambda_{j}=e^{i\omega_{j}}for real phasesωj\omega_{j}, so the quantum latent state undergoes a norm-preserving evolution in Hilbert space. The centre inset of Fig.1a illustrates this behaviour through a single-qubit Bloch-sphere schematic, whose equatorial(x,y)(x,y)plane encodes the real and imaginary parts of the off-diagonal coherence. This unitary backbone replaces the exponential rollout error of generic linear latent propagators with a strictly linear-in-nnbound, suppressing in principle the unstable amplification and decay regimes that destabilise autoregressive surrogates over long horizons.

## VI.2Stability of the quantum latent propagator in autoregressive rollout

The deployed surrogate produces predictions by composing encoder, latent propagator and decoder, and is then advanced autoregressively on its own outputs, so the same latent propagatorUUis appliednntimes across annn-step rollout. For any observableggin the encoder’sNN-dimensional subspace𝒱N⊂ℋ\mathcal{V}_{N}\subset\mathcal{H}, the gap between the true Koopman evolution𝒦n​g\mathcal{K}^{n}gand the surrogate compositionUn​gU^{n}gobeys the Koopman–Galerkin telescoping bound (Supplementary Information S5.2)‖𝒦n​g−Un​g‖ℋ≤εN​∑j=0n−1ρ​(U)j,\bigl\|\mathcal{K}^{n}g-U^{n}g\bigr\|_{\mathcal{H}}\;\leq\;\varepsilon_{N}\sum_{j=0}^{n-1}\rho(U)^{\,j},(7)

whereεN\varepsilon_{N}is the per-step encoder–decoder invariance defect[32,33]andρ​(U)\rho(U)is the spectral radius of the latent propagator. The full encoder–latent–decoder error therefore decomposes into a per-stepadditiveencoder–decoder reconstruction termεN\varepsilon_{N}and amultiplicativelatent compoundingρ​(U)n\rho(U)^{n}; long-horizon stability is controlled by the latter, becauseεN\varepsilon_{N}is fixed per step whileρ​(U)n\rho(U)^{n}accumulates geometrically withnn. The autoregressive question therefore reduces to a single question: how fast does‖Un‖2\|U^{n}\|_{2}grow withnn?

This compounding of a single operatorUUovernnrollout steps is structurally analogous to the mechanism behind exploding and vanishing gradients in autoregressive sequence models[51,71]: the forward latent state and the gradient back-propagated from the lossℒ\mathcal{L}both pass through powers of the same operator,𝐳n=Un​𝐳0,∂ℒ∂𝐳0=(U†)n​∂ℒ∂𝐳n.\mathbf{z}_{n}=U^{n}\mathbf{z}_{0},\qquad\frac{\partial\mathcal{L}}{\partial\mathbf{z}_{0}}=\bigl(U^{\dagger}\bigr)^{n}\frac{\partial\mathcal{L}}{\partial\mathbf{z}_{n}}.(8)

The analogy is structural only: our model is not a recurrent network, since the latent state is a Koopman observable obtained by the encoder rather than a learned hidden vector, and training does not back-propagate through a learned recurrent dynamics. What carries over is the mathematical issue of repeatedUU-composition. For a general, possibly non-normalUU, the growth of‖Un‖2\|U^{n}\|_{2}cannot be read off any single singular value at finitenn, and intermediate steps may exhibit transient amplification even whenUUis ultimately contractive. The asymptotic rate is nevertheless pinned by a classical theorem of Gelfand[72], which identifies it with the spectral radius,ρ​(U)=limn→∞‖Un‖21/n,\rho(U)\;=\;\lim_{n\to\infty}\|U^{n}\|_{2}^{1/n},(9)

so the long-horizon rollout norm falls into a sharp trichotomy,‖Un​𝐳0‖2​∼n→∞​ρ​(U)n​‖𝐳0‖2,ρ​(U)={1+δ>1,exploding state and gradient,1,norm-preserving,1−δ<1,vanishing state and gradient.\|U^{n}\mathbf{z}_{0}\|_{2}\;\underset{n\to\infty}{\sim}\;\rho(U)^{\,n}\,\|\mathbf{z}_{0}\|_{2},\qquad\rho(U)\;=\;\begin{cases}1+\delta>1,&\text{exploding state and gradient},\\[2.0pt]
1,&\text{norm-preserving},\\[2.0pt]
1-\delta<1,&\text{vanishing state and gradient}.\end{cases}(10)

The asymptotic equivalence is up to polynomial factors arising from any non-trivial Jordan structure ofUU; equality on the middle row requiresUUto be normal, which is automatic for the unitaryUqU_{q}used below. For any measure-preserving dynamical system, the Koopman operator is anL2L^{2}isometry withρ​(𝒦)=1\rho(\mathcal{K})=1. A surrogate withρ<1\rho<1then injects spurious dissipation into the encoder–latent–decoder loop, and one withρ>1\rho>1injects spurious amplification. The physically faithful target is therefore not merely a contractiveUU, but one whose spectrum sits on the unit circle.

## Classical latent propagators.

A classical dense propagatorUKU_{K}is typically fitted by least squares on single-step prediction, which controls only the one-step residual and imposes no global constraint on the eigenvalue distribution ofUKU_{K}. Spectral discipline can be encouraged by augmenting the training loss with a soft unitarity penalty‖UK⊤​UK−I‖F2\|U_{K}^{\top}U_{K}-I\|_{F}^{2}, and the classical ML baseline used throughout this work carries exactly such a regulariser on its latent propagator[42]. A penalty of this form is, however, a regularisation target rather than a constraint: it competes with the data-fit terms and is minimised only up to the optimisation tolerance, so at convergence it is small but generically non-zero and the trained propagator retains a residual spectral driftδ>0\delta>0, leavingρ​(UK)\rho(U_{K})detached from the unit circle. A residual of onlyδ=10−2\delta=10^{-2}already compounds to(1+δ)n≈eδ​n≈148(1+\delta)^{n}\approx e^{\delta n}\approx 148overn=500n=500autoregressive inference steps. Both exploding and vanishing rollout regimes therefore remain generic failure modes of classical autoregressive surrogates, with or without soft spectral regularisation. Specialising Eq. (7) toρ=1+δ>1\rho=1+\delta>1and assumingUKU_{K}is normal so that‖UK‖2=ρ\|U_{K}\|_{2}=\rho, the geometric sum is dominated by its highest power and the bound becomes‖𝒦n​g−UKn​g‖ℋ≤εN​ρn−1ρ−1∼εNδ​eδ​n(ρ=1+δ>1),\bigl\|\mathcal{K}^{n}g-U_{K}^{n}g\bigr\|_{\mathcal{H}}\;\leq\;\varepsilon_{N}\,\frac{\rho^{\,n}-1}{\rho-1}\;\sim\;\frac{\varepsilon_{N}}{\delta}\,e^{\delta n}\qquad(\rho=1+\delta>1),(11)

whereεN\varepsilon_{N}is the encoder-decoder invariance defect. (For non-normalUKU_{K}, a numerical-range constant must be added; the bound is otherwise unchanged.)

## Quantum latent propagator.

Lyapunov’s theory of stability[48,49]provides the canonical criterion for bounded trajectories of a discrete-time system𝐳t+1=Φ​(𝐳t)\mathbf{z}_{t+1}=\Phi(\mathbf{z}_{t}). It suffices to exhibit a continuous energyV:ℂk→ℝ≥0V:\mathbb{C}^{k}\to\mathbb{R}_{\geq 0}withV​(𝟎)=0V(\mathbf{0})=0andV​(𝐳)>0V(\mathbf{z})>0for𝐳≠𝟎\mathbf{z}\neq\mathbf{0}that does not increase along the flow,V​(Φ​(𝐳))≤V​(𝐳)V(\Phi(\mathbf{z}))\leq V(\mathbf{z}). When this inequality saturates asV​(Φ​(𝐳))=V​(𝐳)V(\Phi(\mathbf{z}))=V(\mathbf{z}), the system is marginally stable with conserved latent energy, and every eigenvalue of the one-step map lies on the unit circle. For the quantum latent propagator, this criterion is met by the simplest choice, the Euclidean latent energyV​(𝐳)=‖𝐳‖22V(\mathbf{z})=\|\mathbf{z}\|_{2}^{2}, where𝐳\mathbf{z}is identified with the amplitude vector of|ψin​(𝐳)⟩|\psi_{\mathrm{in}}(\mathbf{z})\rangleunder amplitude encoding. BecauseUq​(𝜽)U_{q}(\bm{\theta})is a product of exponentials of Hermitian generators (Eq. (14) below) and is therefore unitary, a one-line computation givesV​(Uq​(𝜽)​𝐳)=𝐳†​Uq†​Uq​𝐳=‖𝐳‖22=V​(𝐳)for every​𝜽​and every​𝐳,V\!\bigl(U_{q}(\bm{\theta})\,\mathbf{z}\bigr)\;=\;\mathbf{z}^{\dagger}U_{q}^{\dagger}U_{q}\,\mathbf{z}\;=\;\|\mathbf{z}\|_{2}^{2}\;=\;V(\mathbf{z})\qquad\text{for every }\bm{\theta}\text{ and every }\mathbf{z},(12)

soVVis a strict Lyapunov function with conserved energy for the latent rollout. Because Eq. (12) holds pointwise in parameter space,ρ​(Uq​(𝜽))=1\rho(U_{q}(\bm{\theta}))=1is not a target to be optimised towards but an identity imposed by the model class itself, holding at random initialisation, at every stochastic-gradient-descent (SGD) update, and at inference.

This Lyapunov–spectrum correspondence closes the chain of Eqs. (8)–(10). Conserved energy underUqU_{q}pins every eigenvalue ofUqU_{q}to the unit circle. Settingρ​(Uq)=1\rho(U_{q})=1collapses the trichotomy of Eq. (10) onto its norm-preserving branch, ruling out both exploding and vanishing rollout regimes. Taking the limitρ→1\rho\to 1in Eq. (11) vialimρ→1(ρn−1)/(ρ−1)=n\lim_{\rho\to 1}(\rho^{\,n}-1)/(\rho-1)=nthen replaces the exponential classical bound with a strictly linear one,‖𝒦n​g−Uqn​(𝜽)​g‖ℋ≤n​εNfor all​n≥1,\bigl\|\mathcal{K}^{n}g-U_{q}^{n}(\bm{\theta})\,g\bigr\|_{\mathcal{H}}\;\leq\;n\,\varepsilon_{N}\qquad\text{for all }n\geq 1,(13)

whose slope is the encoder-decoder invariance defectεN\varepsilon_{N}alone. A self-contained proof of Eqs. (12)–(13) is given in Supplementary Information S5.2, together with the lemma that propagates the per-step defectεN\varepsilon_{N}into thenn-step bound and the corresponding corollary for classical dense propagators.

The layered circuit of Eq. (5) admits a Hamiltonian representation as a product ofLLlayer-wise unitaries,Uq​(𝜽)=∏ℓ=1Le−i​Hℓ​(𝜽)​Δ​t/L,U_{q}(\bm{\theta})=\prod_{\ell=1}^{L}e^{-iH_{\ell}(\bm{\theta})\,\Delta t/L},(14)

in which each Hermitian generatorHℓ​(𝜽)=Hℓ​(𝜽)†H_{\ell}(\bm{\theta})=H_{\ell}(\bm{\theta})^{\dagger}governs the latent-space dynamics within a single layer,Hℓ​(𝜽)=∑i=1Nqαℓ,i​Xi+∑(i,j)∈Eβℓ,(i,j)​(Xi​Xj+Yi​Yj),H_{\ell}(\bm{\theta})=\sum_{i=1}^{N_{q}}\alpha_{\ell,i}\,X_{i}+\sum_{(i,j)\in E}\beta_{\ell,(i,j)}(X_{i}X_{j}+Y_{i}Y_{j}),(15)

combining latent-mode phase evolution with sparse inter-mode energy transfer, with QCML (S) tyingαℓ,i=αℓ\alpha_{\ell,i}=\alpha_{\ell}andβℓ,(i,j)=βℓ\beta_{\ell,(i,j)}=\beta_{\ell}within each layer. The eigenvalues of eachHℓ​(𝜽)H_{\ell}(\bm{\theta})define characteristic frequenciesωj(ℓ)\omega_{j}^{(\ell)}throughλj(ℓ)=e−i​ωj(ℓ)​Δ​t/L\lambda_{j}^{(\ell)}=e^{-i\omega_{j}^{(\ell)}\Delta t/L}, yielding a layer-resolved spectral decomposition of the learned dynamics in Hilbert space. This structure aligns with the Koopman spectral viewpoint, in which nonlinear dynamics are approximated as a superposition of mode frequencies and structured mode interactions. Each layer-wise factor in Eq. (14) is unitary, and so is their productUq​(𝜽)U_{q}(\bm{\theta}); the Lyapunov argument of Eq. (12) therefore applies layer by layer and globally.

The structured quantum latent propagator of Eq. (14)–(15) delivers a decisive advantage over a classical dense Koopman propagator on the same latent. It is structurally immune to the exploding and vanishing rollout regimes that plague classical latent dynamics. Unitarity pinsρ​(Uq)=1\rho(U_{q})=1pointwise in𝜽\bm{\theta}, replacing the exponential classical-latent error of Eq. (11) with the strictly linear-in-nnKoopman–Galerkin bound of Eq. (13). In parallel, amplitude encoding stores thekk-dimensional latent inNq=log2⁡kN_{q}=\log_{2}kqubits, so the dense matrix–vector multiplication(UK​𝐳t)i=∑j=1k(UK)i​j​(𝐳t)j,(U_{K}\mathbf{z}_{t})_{i}=\sum_{j=1}^{k}(U_{K})_{ij}(\mathbf{z}_{t})_{j},(16)

of cost𝒪​(k2)\mathcal{O}(k^{2})per step[20]is replaced by the structured circuit of Eq. (5) at a tighter gate complexityCostQCML=𝒪​(L​Nq)=𝒪​(L​log⁡k),\mathrm{Cost}_{\mathrm{QCML}}=\mathcal{O}(L\,N_{q})=\mathcal{O}(L\log k),(17)

linear inlog⁡k\log krather than polynomial inkk.

The structured generator family and its Koopman spectral interpretation are detailed in Supplementary Information S4. The Lyapunov stability of the latent rollout and the associated linear error bound are derived in Supplementary Information S5.2, and the parametric-sensitivity and locality analyses follow in Supplementary Information S5.3–S5.5.

## VI.3Hardware implementation and training

The encoder, decoder and quantum-circuit parameters of Eqs. (3)–(4) are optimised jointly in a single end-to-end hybrid loop against a field-space reconstruction loss. Training is first carried out on a noise-aware classical emulator of the structured circuit to validate convergence. Backend validation is then performed either on the same noise-aware emulator or on IQM’s superconducting quantum processor Emerald, a 54-qubit device for quantum latent propagator (Fig.5).

Classical neural-network components are implemented in PyTorch and executed on the BEAST GPU cluster at the Leibniz Supercomputing Centre, while the quantum circuit is invoked through Qiskit interfaces to Emerald. The low gate count and shallow depth of the structured ansatz of Eq. (5) keep the hybrid execution within the coherence-limited regime of the device. The classical–quantum exchange between BEAST and IQM Emerald is carried over a dedicated network channel between the supercomputing centre and IQM, which keeps the round-trip overhead modest at the circuit sizes used here. Co-locating the QPU with the HPC system would reduce this overhead further.Figure 5:Structured quantum circuit and its hardware realisation.a.Native connectivity graph of the IQM 54-qubit Emerald processor; colours mark the four qubit groups, unavailable couplers are greyed out, and the blue outline highlights the qubit subset used in one execution of a single task. Each task was run as four parallel executions to reduce resource consumption.b.Native gate-level realisation of the structured quantum latent propagatorUq​(𝜽)U_{q}(\bm{\theta})of Eq. (5) after transpilation to the IQM Emerald native gate set: the latent state𝐳t\mathbf{z}_{t}is amplitude-encoded into the qubit register, transformed byLLrepeated structured layersUℓU_{\ell}, and read out into𝐳t+1\mathbf{z}_{t+1}. Each layer uses the nativeRX​(αℓ)\mathrm{RX}(\alpha_{\ell})single-qubit gate for the mode-wise rotation and the nativeXY​(βℓ)\mathrm{XY}(\beta_{\ell})two-qubit gate for the XY coupling on adjacent qubits along the interaction graphEE. In QCML (S), a singleαℓ\alpha_{\ell}and a singleβℓ\beta_{\ell}are shared across allRX\mathrm{RX}andXY\mathrm{XY}gates of layerℓ\ell, leaving2​L2Ltrainable scalars per circuit.

## VI.3.1Structured quantum latent propagator

The choice of variational quantum ansatz is central to the trainability of the quantum latent propagator. One of the main obstacles in variational quantum circuits is not back-propagation in the ordinary neural-network sense, but the emergence of barren plateaus in the cost landscape. As the number of qubits, the circuit depth or the expressibility of the ansatz increases, gradients of expectation-value objectives can concentrate around zero and their variance can decay exponentially[40,41]. A key mechanism is concentration of measure: when an ansatz becomes sufficiently expressive to approximate Haar-random unitaries, or to form an approximate unitary 2-design, local parameter perturbations are averaged over the Hilbert space and have exponentially small influence on measured observables.

The design goal is therefore not simply to reduce the number of possible unitary maps. It is to avoid an unstructured search over the full unitary group while preserving the dynamical transformations needed by the problem. QCML (S) uses a structured ansatz for this purpose. The circuit restricts the latent propagator to the submanifold generated by mode-wise single-qubit rotations and sparse inter-mode couplings, which are the two operator classes required to represent latent frequencies and their leading interactions. This structure reduces exposure to one common route into barren plateaus, while keeping the search space aligned with the spectral dynamics that determine prediction accuracy.

The quantum latent propagator is implemented through the structured parameterised quantum circuit of Eq. (5). Rather than an unstructured hardware-efficient ansatz of arbitrary rotations and entanglers, the framework restricts the generators to the mode-wise single-qubit rotations and sparse inter-mode couplings of Eq. (5), with the interaction graphEEfollowing the native connectivity of the quantum processor (Fig.5a).

## VI.3.2Two-stage hybrid training

Training variational quantum models directly on hardware is limited by latency and execution cost. To address this challenge, the framework adopts a two-stage hybrid training strategy that combines noise-aware simulation with hardware deployment.

Phase 1: noise-aware simulation training.In the first phase, the hybrid model is trained on the BEAST GPU cluster using a noise-aware quantum simulator integrated into the PyTorch training loop. We use Qiskit Aer configured with the Emerald noise profile derived from calibration data of the physical processor. This lets the classical encoder–decoder networks and the quantum circuit parameters𝜽\bm{\theta}converge under realistic noise conditions, while substantially reducing the cost of quantum hardware calls.

Phase 2: hardware fine-tuning and inference.After convergence in simulation, the quantum backend is switched to the physical IQM Emerald processor through the IQM-Qiskit-provider. The structured ansatz uses onlyNq=9N_{q}=9qubits, so multiple independent copies of the same circuit are placed in parallel on the5454-qubit chip, yielding up to44concurrent circuit executions per hardware call (due to the maintenance on several qubits); this parallelism is used in both the fine-tuning epochs that adapt𝜽\bm{\theta}to hardware-specific noise and the final inference runs used for prediction and validation, which are executed directly on the quantum hardware.

All circuits are compiled and transpiled using Qiskit’s transpile function targeting the Emerald backend. This process maps logical qubits to physical qubits, decomposes composite operations into native gates, optimises circuit depth, and inserts SWAP operations when required by the hardware connectivity. The native single-qubit gate of IQM Emerald is the parameterisedRX\mathrm{RX}pulse, which directly implements the mode-wise rotatione−i​αℓ,i​Xie^{-i\alpha_{\ell,i}X_{i}}of Eq. (5), so the structured ansatz maps onto the native gate set without a basis change (Fig.5b). Each hardware execution uses 4096 measurement shots, and expectation values are estimated by statistical averaging.

## VI.3.3Error mitigation

Computation on NISQ devices is affected by multiple noise sources that can degrade measurement fidelity. We therefore apply measurement-error mitigation during the hardware fine-tuning and inference phase. The procedure calibrates the measurement confusion matrix of the relevant qubits and applies correction techniques such as matrix inversion or constrained least-squares reconstruction, implemented in libraries including mthree[73]. The output is a mitigated quasi-probability distribution used to estimate expectation values.

Depending on the dominant error channels observed on the device, additional mitigation strategies such as zero-noise extrapolation[74]or randomised compiling[75]can be added. In practice, the structured quantum circuits used in the framework are relatively shallow and carry few parameters, which further improves robustness to hardware noise compared with deeper generic variational circuits.

## References
- Duraisamy, Iaccarino, and Xiao [2019]K. Duraisamy, G. Iaccarino, and H. Xiao, “Turbulence
modeling in the age of data,” Annual review of fluid mechanics51, 357–377 (2019).
- Biet al.[2023]K. Bi, L. Xie, H. Zhang, X. Chen, X. Gu, and Q. Tian, “Accurate medium-range global weather forecasting with 3d neural networks,” Nature619, 533–538 (2023).
- Lamet al.[2023]R. Lam, A. Sanchez-Gonzalez, M. Willson, P. Wirnsberger, M. Fortunato, F. Alet,
S. Ravuri, T. Ewalds, Z. Eaton-Rosen, W. Hu,et al., “Learning skillful medium-range global weather
forecasting,” Science382, 1416–1421
(2023).
- Cho, Lazarian, and Vishniac [2002]J. Cho, A. Lazarian, and E. T. Vishniac, “Simulations of
magnetohydrodynamic turbulence in a strongly magnetized medium,” The Astrophysical
Journal564, 291
(2002).
- Gopakumaret al.[2024]V. Gopakumar, S. Pamela,
L. Zanisi, Z. Li, A. Gray, D. Brennand, N. Bhatia, G. Stathopoulos, M. Kusner, M. P. Deisenroth,et al., “Plasma surrogate modelling using fourier neural
operators,” Nuclear Fusion64, 056025 (2024).
- Feigeret al.[2020]B. Feiger, J. Gounley,
D. Adler, J. A. Leopold, E. W. Draeger, R. Chaudhury, J. Ryan, G. Pathangey, K. Winarta, D. Frakes,et al., “Accelerating massively parallel hemodynamic models of
coarctation of the aorta using neural networks,” Scientific Reports10, 9508 (2020).
- Xueet al.[2025]X. Xue, T. M. Athawale,
J. W. McCullough,
S. C. Lo, I. Zacharoudiou, B. Joo, A. Georgiadou, and P. V. Coveney, “An uncertainty visualization framework for large-scale
cardiovascular flow simulations: A case study on aortic stenosis,” arXiv preprint
arXiv:2508.15420 (2025).
- Tanadeet al.[2022]C. Tanade, S. J. Chen,
J. A. Leopold, and A. Randles, “Analysis identifying minimal governing
parameters for clinically accurate in silico fractional flow reserve,” Frontiers in
Medical Technology4, 1034801 (2022).
- Leuprechtet al.[2003]A. Leuprecht, S. Kozerke,
P. Boesiger, and K. Perktold, “Blood flow in the human ascending aorta:
a combined MRI and CFD study,” Journal of engineering mathematics47, 387–404 (2003).
- Groenet al.[2013]D. Groen, J. Hetherington,
H. B. Carver, R. W. Nash, M. O. Bernabeu, and P. V. Coveney, “Analysing and modelling the performance of the
HemeLB lattice-Boltzmann simulation environment,” Journal of Computational
Science4, 412–422
(2013).
- Mazzeo and Coveney [2008]M. D. Mazzeo and P. V. Coveney, “HemeLB: A high
performance parallel lattice-Boltzmann code for large scale fluid flow in
complex geometries,” Computer Physics Communications178, 894–914 (2008).
- Brunton, Noack, and Koumoutsakos [2020]S. L. Brunton, B. R. Noack, and P. Koumoutsakos, “Machine learning for fluid
mechanics,” Annual review of fluid mechanics52, 477–508 (2020).
- Xueet al.[2026]X. Xue, T. Yang, M. Gao, L. Pan, M. Wang, K. Zhu, S. Wang, J. Li, M. F. ten Eikelder, and P. V. Coveney, “Uni-flow: a unified autoregressive-diffusion
model for complex multiscale flows,” arXiv preprint arXiv:2602.15592 (2026).
- Priceet al.[2025]I. Price, A. Sanchez-Gonzalez, F. Alet, T. R. Andersson,
A. El-Kadi, D. Masters, T. Ewalds, J. Stott, S. Mohamed, P. Battaglia,et al., “Probabilistic weather forecasting with machine
learning,” Nature637, 84–90
(2025).
- Pathaket al.[2026]J. Pathak, Y. Cohen,
P. Garg, P. Harrington, N. Brenowitz, D. Durran, M. Mardani, A. Vahdat, S. Xu, K. Kashinath,et al., “Kilometer-scale convection-allowing model emulation using generative
diffusion modeling,” Science Advances12, eadv0423 (2026).
- Passaroet al.[2025]S. Passaro, G. Corso,
J. Wohlwend, M. Reveiz, S. Thaler, V. R. Somnath, N. Getz, T. Portnoi, J. Roy,
H. Stark,et al., “Boltz-2: Towards accurate
and efficient binding affinity prediction,” BioRxiv (2025).
- Bhatiet al.[2026]A. P. Bhati, S. Wan, H. H. Loeffler, M. Klähn, M. Bieniek, K. Liu, S. Ahmad, L. Halabelian,
J. Dong, X. Zhang,et al., “An integrated workflow comprising AI,
physics and experiment: Discovery of nanomolar-potent inhibitors,” (2026).
- Wanet al.[2026]S. Wan, X. Zhang, X. Xue, and P. V. Coveney, “On the reliability of AI methods in drug
discovery: Evaluation of Boltz-2 for structure and binding affinity
prediction,” arXiv preprint arXiv:2603.05532 (2026).
- Karniadakiset al.[2021]G. E. Karniadakis, I. G. Kevrekidis, L. Lu,
P. Perdikaris, S. Wang, and L. Yang, “Physics-informed machine learning,” Nature Reviews Physics3, 422–440 (2021).
- Liet al.[2020]Z. Li, N. Kovachki,
K. Azizzadenesheli,
B. Liu, K. Bhattacharya, A. Stuart, and A. Anandkumar, “Fourier neural operator for parametric partial
differential equations,” arXiv preprint arXiv:2010.08895 (2020).
- Oommenet al.[2025]V. Oommen, A. Bora,
Z. Zhang, and G. E. Karniadakis, “Integrating neural operators with
diffusion models improves spectral representation in turbulence modelling,”Proceedings of the Royal Society A: Mathematical,
Physical and Engineering Sciences481, 20240819 (2025),https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.2024.0819.
- Raissi, Perdikaris, and Karniadakis [2019]M. Raissi, P. Perdikaris, and G. E. Karniadakis, “Physics-informed neural
networks: A deep learning framework for solving forward and inverse problems
involving nonlinear partial differential equations,” Journal of Computational
physics378, 686–707
(2019).
- Preskill [2018]J. Preskill, “Quantum
computing in the NISQ era and beyond,” Quantum2, 79 (2018).
- Huanget al.[2025]H.-Y. Huang, S. Choi,
J. R. McClean, and J. Preskill, “The vast world of quantum advantage,” arXiv preprint
arXiv:2508.05720 (2025).
- Lubaschet al.[2020]M. Lubasch, J. Joo,
P. Moinier, M. Kiffner, and D. Jaksch, “Variational quantum algorithms for nonlinear problems,” Physical Review
A101, 010301 (2020).
- Sanavio and Succi [2024]C. Sanavio and S. Succi, “Lattice
Boltzmann–Carleman quantum algorithm and circuit for fluid flows at
moderate Reynolds number,” AVS Quantum Science6(2024).
- Sanavio, Mauri, and Succi [2025]C. Sanavio, E. Mauri, and S. Succi, “Explicit quantum circuit for simulating
the advection-diffusion-reaction dynamics,” IEEE Transactions on Quantum Engineering 
(2025).
- Kocherlaet al.[2024]S. Kocherla, Z. Song,
F. E. Chrit, B. Gard, E. F. Dumitrescu, A. Alexeev, and S. H. Bryngelson, “Fully quantum algorithm for mesoscale fluid
simulations with application to partial differential equations,” AVS Quantum
Science6(2024).
- Wawrzyniaket al.[2024]D. Wawrzyniak, J. Winter,
S. Schmidt, T. Indinger, U. Schramm, C. Janßen, and N. A. Adams, “Unitary quantum algorithm for the lattice-Boltzmann method,” arXiv preprint
arXiv:2405.13391 (2024).
- Mezić [2021]I. Mezić, “Koopman
operator, geometry, and learning of dynamical systems,” Not. Am. Math. Soc68, 1087–1105 (2021).
- Bruntonet al.[2022]S. L. Brunton, M. Budišić, E. Kaiser, and J. N. Kutz, “Modern Koopman
theory for dynamical systems,”SIAM Review64, 229–340 (2022).
- Williams, Kevrekidis, and Rowley [2015]M. O. Williams, I. G. Kevrekidis, and C. W. Rowley, “A data-driven
approximation of the Koopman operator: Extended dynamic mode
decomposition,” Journal of Nonlinear Science25, 1307–1346 (2015).
- Korda and Mezić [2018]M. Korda and I. Mezić, “On
convergence of extended dynamic mode decomposition to the Koopman
operator,” Journal of Nonlinear Science28, 687–710 (2018).
- Luet al.[2021]L. Lu, P. Jin, G. Pang, Z. Zhang, and G. E. Karniadakis, “Learning nonlinear operators via DeepONet
based on the universal approximation theorem of operators,” Nature machine intelligence3, 218–229 (2021).
- Kovachkiet al.[2023]N. Kovachki, Z. Li,
B. Liu, K. Azizzadenesheli, K. Bhattacharya, A. Stuart, and A. Anandkumar, “Neural operator: Learning maps between function
spaces with applications to PDEs,” Journal of Machine Learning Research24, 1–97 (2023).
- Liet al.[2021]Z. Li, M. Liu-Schiaffini,
N. Kovachki, B. Liu, K. Azizzadenesheli, K. Bhattacharya, A. Stuart, and A. Anandkumar, “Learning dissipative dynamics in chaotic
systems,” arXiv
preprint arXiv:2106.06898 (2021).
- McCabeet al.[2023]M. McCabe, P. Harrington,
S. Subramanian, and J. Brown, “Towards stability of autoregressive
neural operators,” arXiv preprint arXiv:2306.10619 (2023).
- Dunjko, Taylor, and Briegel [2016]V. Dunjko, J. M. Taylor, and H. J. Briegel, “Quantum-enhanced machine
learning,” Physical review letters117, 130501 (2016).
- Ghazi Vakiliet al.[2025]M. Ghazi Vakili, C. Gorgulla, J. Snider,
A. Nigam, D. Bezrukov, D. Varoli, A. Aliper, D. Polykovsky, K. M. Padmanabha Das, H. Cox Iii,et al., “Quantum-computing-enhanced algorithm unveils potential
KRAS inhibitors,” Nature biotechnology43, 1954–1959 (2025).
- McCleanet al.[2018]J. R. McClean, S. Boixo,
V. N. Smelyanskiy,
R. Babbush, and H. Neven, “Barren plateaus in quantum neural network
training landscapes,”Nature Communications9, 4812 (2018).
- Cerezoet al.[2022]M. Cerezo, G. Verdon,
H.-Y. Huang, L. Cincio, and P. J. Coles, “Challenges and opportunities in quantum machine
learning,” Nature Computational Science2, 567–576 (2022).
- Wanget al.[2026]M. Wang, X. Xue, M. Gao, and P. V. Coveney, “Quantum-informed machine learning for predicting
spatiotemporal chaos with practical quantum advantage,” Science Advances12, eaec5049 (2026).
- Zamiret al.[2022]S. W. Zamir, A. Arora,
S. Khan, M. Hayat, F. S. Khan, and M.-H. Yang, “Restormer: Efficient transformer for high-resolution image
restoration,” inProceedings
of the IEEE/CVF conference on computer vision and pattern recognition(2022) pp. 5728–5739.
- Cerezoet al.[2021a]M. Cerezo, A. Arrasmith,
R. Babbush, S. C. Benjamin, S. Endo, K. Fujii, J. R. McClean, K. Mitarai, X. Yuan,
L. Cincio, and P. J. Coles, “Variational quantum algorithms,”Nature Reviews Physics3, 625–644 (2021a).
- Mitaraiet al.[2018]K. Mitarai, M. Negoro,
M. Kitagawa, and K. Fujii, “Quantum circuit learning,” Physical Review A98, 032309 (2018).
- Goto, Tran, and Nakajima [2021]T. Goto, Q. H. Tran, and K. Nakajima, “Universal approximation
property of quantum machine learning models in quantum-enhanced feature
spaces,” Physical Review Letters127, 090506 (2021).
- Wang, Jiang, and Coveney [2025]M. Wang, J. Jiang, and P. V. Coveney, “Parameter-efficient quantum
anomaly detection method on a superconducting quantum processor,” Physical Review
Research7, 043094
(2025).
- Lyapunov [1992]A. M. Lyapunov, “The general
problem of the stability of motion,” International Journal of Control55, 531–773 (1992), english translation by A. T. Fuller of the 1892 Russian
doctoral dissertation, Kharkov Mathematical Society.
- Khalil [2002]H. K. Khalil,Nonlinear Systems, 3rd ed. (Prentice Hall, Upper Saddle River, NJ, 2002).
- Koopman [1931]B. O. Koopman, “Hamiltonian
systems and transformation in Hilbert space,” Proceedings of the National Academy of
Sciences17, 315–318
(1931).
- Bengio, Simard, and Frasconi [1994]Y. Bengio, P. Simard, and P. Frasconi, “Learning long-term
dependencies with gradient descent is difficult,” IEEE transactions on neural networks5, 157–166 (1994).
- Cerezoet al.[2021b]M. Cerezo, A. Sone,
T. Volkoff, L. Cincio, and P. J. Coles, “Cost function dependent barren plateaus in shallow
parametrized quantum circuits,”Nature Communications12, 1791 (2021b).
- Laroccaet al.[2025]M. Larocca, S. Thanasilp,
S. Wang, K. Sharma, J. Biamonte, P. J. Coles, L. Cincio, J. R. McClean,
Z. Holmes, and M. Cerezo, “A review of barren plateaus in variational
quantum computing,”Nature Reviews Physics 
(2025), 10.1038/s42254-025-00813-9, volume / pages to be confirmed at nature.com.
- Caroet al.[2022]M. C. Caro, H.-Y. Huang,
M. Cerezo, K. Sharma, A. Sornborger, L. Cincio, and P. J. Coles, “Generalization in quantum machine learning from few
training data,” Nature communications13, 4919 (2022).
- Fukamiet al.[2019]K. Fukami, Y. Nabae,
K. Kawai, and K. Fukagata, “Synthetic turbulent inflow generator using
machine learning,” Physical Review Fluids4, 064603 (2019).
- Fukami, Fukagata, and Taira [2019]K. Fukami, K. Fukagata, and K. Taira, “Super-resolution reconstruction of
turbulent flows with machine learning,” Journal of Fluid Mechanics870, 106–120 (2019).
- Xue, Yao, and Davidson [2022]X. Xue, H.-D. Yao, and L. Davidson, “Synthetic turbulence generator for
lattice Boltzmann method at the interface between RANS and LES,” Physics of
Fluids34, 055118
(2022).
- Lattet al.[2008]J. Latt, B. Chopard,
O. Malaspinas, M. Deville, and A. Michler, “Straight velocity boundaries in the lattice Boltzmann
method,” Physical Review E77, 056703 (2008).
- Smagorinsky [1963]J. Smagorinsky, “General
circulation experiments with the primitive equations: I. the basic
experiment,” Monthly weather review91, 99–164 (1963).
- Houet al.[1994]S. Hou, J. Sterling,
S. Chen, and G. Doolen, “A lattice Boltzmann subgrid model for high
Reynolds number flows,” arXiv preprint comp-gas/9401004 (1994).
- Koda and Lien [2015]Y. Koda and F.-S. Lien, “The lattice
Boltzmann method implemented on the GPU to simulate the turbulent flow
over a square cylinder confined in a channel,” Flow, Turbulence and Combustion94, 495–512 (2015).
- Xueet al.[2024]X. Xue, J. W. McCullough,
S. C. Lo, I. Zacharoudiou, B. Joó, and P. V. Coveney, “The lattice Boltzmann based large eddy
simulations for the stenosis of the aorta,” inInternational Conference on Computational Science(Springer Nature Switzerland, 2024) pp. 408–420.
- Wilson, Ortiz, and Johnson [2013]N. M. Wilson, A. K. Ortiz, and A. B. Johnson, “The Vascular Model
Repository: A Public Resource of Medical Imaging Data and Blood Flow
Simulation Results,”Journal of Medical Devices7(2013), 10.1115/1.4025983.
- Zacharoudiou, McCullough, and Coveney [2023]I. Zacharoudiou, J. McCullough, and P. Coveney, “Development
and performance of a HemeLB GPU code for human-scale blood flow
simulation,” Computer Physics Communications282, 108548 (2023).
- Succi [2001]S. Succi,The lattice Boltzmann
equation: for fluid dynamics and beyond(Oxford
University Press, 2001).
- Loet al.[2024]S. C. Lo, J. W. McCullough,
X. Xue, and P. V. Coveney, “Uncertainty quantification of the impact
of peripheral arterial disease on abdominal aortic aneurysms in blood flow
simulations,” Journal of the Royal Society Interface21, 20230656 (2024).
- Guo, Kleiser, and Adams [1994]Y. Guo, L. Kleiser, and N. Adams, “A comparison study of an improved
temporal DNS and spatial DNS of compressible boundary layer
transition,” inFluid
Dynamics Conference(1994) p. 2371.
- Adams [2000]N. A. Adams, “Direct simulation
of the turbulent boundary layer along a compression ramp at m= 3 and
reθ\theta= 1685,” Journal of Fluid Mechanics420, 47–83 (2000).
- Loet al.[2025]S. C. Lo, A. Zingaro,
J. W. McCullough,
X. Xue, P. Gonzalez-Martin, B. Joo, M. Vázquez, and P. V. Coveney, “A multi-component, multi-physics computational model for solving
coupled cardiac electromechanics and vascular haemodynamics,” Computer Methods in Applied
Mechanics and Engineering446, 118185 (2025).
- Gonzalez-Condeet al.[2024]J. Gonzalez-Conde, T. W. Watts, P. Rodriguez-Grasa, and M. Sanz, “Efficient quantum
amplitude encoding of polynomial functions,” Quantum8, 1297 (2024).
- Pascanu, Mikolov, and Bengio [2013]R. Pascanu, T. Mikolov, and Y. Bengio, “On the difficulty of
training recurrent neural networks,” inInternational Conference on Machine Learning (ICML)(2013) pp. 1310–1318.
- Gelfand [1941]I. M. Gelfand, “Normierte
ringe,” Recueil
Mathématique [Matematicheskiĭ Sbornik] N.S.9(51), 3–24 (1941).
- Nationet al.[2021]P. D. Nation, H. Kang,
N. Sundaresan, and J. M. Gambetta, “Scalable mitigation of
measurement errors on quantum computers,” PRX Quantum2, 040326 (2021).
- Heet al.[2020]A. He, B. Nachman,
W. A. de Jong, and C. W. Bauer, “Zero-noise extrapolation for
quantum-gate error mitigation with identity insertions,” Physical Review A102, 012426 (2020).
- Wallman and Emerson [2016]J. J. Wallman and J. Emerson, “Noise tailoring
for scalable quantum computation via randomized compiling,” Physical Review A94, 052325 (2016).

## Acknowledgements

P.V.C. and X.X. acknowledge funding support from the European Commission CompBioMed Centre of Excellence (Grant No. 675451 and 823712). Support from the UK Engineering and Physical Sciences Research Council under the following projects “UK Consortium on Mesoscale Engineering Sciences (UKCOMES)” (Grant No.EP/R029598/1) and “Software Environment for Actionable and VVUQ-evaluated Exascale Applications (SEAVEA)” (Grant No. EP/W007711/1) is gratefully acknowledged. P.V.C. and X.X. acknowledge the 2024-2025 DOE INCITE award for computational resources on supercomputers at the Oak Ridge Leadership Computing Facility under the “COMPBIO3” project. P.V.C. and X.X. acknowledge the use of resources provided by the Isambard-AI National AI Research Resource (AIRR). Isambard-AI is operated by the University of Bristol and is funded by the UK Government’s Department for Science, Innovation and Technology (DSIT) via UK Research and Innovation; and the Science and Technology Facilities Council [ST/AIRR/I-A-I/1023]. We are grateful to IQM Quantum Computers for providing access to the Emerald superconducting quantum device. We thank Leibniz Supercomputing Centre (LRZ) for access to the BEAST GPU cluster.

## Author contributions

X.X. and M.W. conceptualised the approach. X.X. designed and ran the numerical simulations and generated the training and validation datasets. X.X. and M.W. developed the hybrid quantum–classical machine-learning framework and implemented the structured quantum latent propagator, including runs on the emulator and on the superconducting quantum device. M.G. performed the post-processing of the simulation data. M.C. contributed to the project discussions and planned access to BEAST at LRZ. P.V.C. supervised the project and provided access to the required infrastructure. All authors contributed to writing the manuscript.

## Competing interests

The authors declare no competing interests.

## 


- 


Major funding support from
