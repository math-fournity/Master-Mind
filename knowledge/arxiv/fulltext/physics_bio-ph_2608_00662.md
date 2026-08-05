# No persistent circadian oscillator at genome resolution: pseudo-coherence in gut microbiome dynamics

**arXiv ID**: 2608.00662v1
**Authors**: V. Troude, L. Takayasu, R. Maskawa, W. Suda, D. Sornette, H. Takayasu, M. Takayasu
**Published**: 2026-08-01
**Categories**: physics.bio-ph, nlin.AO, q-bio.GN
**Comments**: 18 pages, 9 figures, 5 tables
**HTML URL**: https://arxiv.org/html/2608.00662v1

## Abstract

Diurnal rhythms in the gut microbiome are commonly read as evidence of host-driven entrainment or of microbial oscillators that synchronise to a common clock. We reanalyse hourly genome-resolved (MAG-level) mouse-gut time series with diagnostics tailored to test that interpretation. At this resolution and for both animals in the dataset, the time-frequency representation carries no persistent ridge; the time-averaged spectrum is enhanced at low frequencies and depleted at intermediate frequencies; the lagged covariance is markedly time-asymmetric, with a global imbalance peak near tens of hours; and an amplitude-adjusted Fourier surrogate test identifies a weak time-averaged construction in the candidate circadian band, never as a fixed time-frequency ridge. The two functional guilds that carry the inferred non-normal amplification are identified independently by the rankings of two inferred dynamical modes (the reaction mode, into which fluctuations are transiently amplified, and the non-normal mode, which injects them), and recover the primary polysaccharide degraders of Bacteroidota and the secondary butyrate and propionate fermenters of Bacillota A without invoking any phase information. The conjunction of these signatures matches a stable but strongly non-normal stochastic regime, that is, pseudo-coherence: geometric amplification reshapes stochastic fluctuations onto a low-dimensional reaction subspace, producing intermittent synchronisation-like episodes, broken time-reversal symmetry, and emergent time-averaged characteristic scales without an underlying oscillator. We propose a falsifiable test via high-resolution clock-gene-knockout cohorts.

## Full Text

No persistent circadian oscillator at genome resolution: pseudo-coherence in gut microbiome dynamics

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
- License: CC BY 4.0arXiv:2608.00662v1 [physics.bio-ph] 01 Aug 2026

## No persistent circadian oscillator at genome resolution:
pseudo-coherence in gut microbiome dynamicsV. TroudeInstitute of Risks Analysis, Prediction and Management,
Southern University of Science and Technology, Shenzhen, ChinaL. TakayasuMeinig School of Biomedical Engineering, Cornell University, Ithaca, NY, USAR. MaskawaGraduate School of Informatics, Nagoya University, Nagoya, JapanW. SudaRIKEN Center for Integrative Medical Sciences, Yokohama, JapanD. SornetteInstitute of Risks Analysis, Prediction and Management,
Southern University of Science and Technology, Shenzhen, ChinaH. TakayasuDepartment of Computer Science, Institute of Science Tokyo, Yokohama, JapanM. TakayasuDepartment of Computer Science, Institute of Science Tokyo, Yokohama, Japan

## Abstract

Diurnal rhythms in the gut microbiome are commonly read as evidence of
host-driven entrainment or of microbial oscillators that synchronise to a
common clock. We reanalyse hourly genome-resolved (MAG-level) mouse-gut
time series with diagnostics tailored to test that interpretation. At this
resolution and for both animals in the dataset, the time-frequency
representation carries no persistent ridge; the time-averaged spectrum is
enhanced at low frequencies and depleted at intermediate frequencies; the
lagged covariance is markedly time-asymmetric, with a global imbalance peak
near tens of hours; and an amplitude-adjusted Fourier surrogate test
identifies a weak time-averaged construction in the candidate circadian
band, never as a fixed time-frequency ridge. The two functional guilds
that carry the inferred non-normal amplification are identified independently by the rankings of two inferred dynamical modes (the reaction mode, into which fluctuations are transiently amplified, and the non-normal mode, which injects them), and
recover the primary polysaccharide degraders of Bacteroidota and the
secondary butyrate and propionate fermenters of Bacillota A without
invoking any phase information. The conjunction of these signatures
matches a stable but strongly non-normal stochastic regime, that is,
pseudo-coherence: geometric amplification reshapes stochastic fluctuations
onto a low-dimensional reaction subspace, producing intermittent
synchronisation-like episodes, broken time-reversal symmetry, and
emergent time-averaged characteristic scales without an underlying
oscillator. We propose a falsifiable test via high-resolution clock-gene-knockout cohorts.

## IIntroduction

Diurnal patterns in microbiome abundance and host-microbe coupling are
extensively documented[1,2,3,4,5].
Synchronisation, clustering, and time-frequency structure of microbial
composition are routinely interpreted with the conceptual toolkit of
coupled phase oscillators[6,7,8].
This toolkit makes a strong physical assumption: the system contains
intrinsic or effectively entrained oscillators, possibly close to a Hopf
bifurcation, that phase-lock under common forcing. Once oscillators are
postulated, observed rhythmicity, anti-synchronised clusters, and
finite-time spectral peaks are read as evidence of phase locking.

We ask a different question. Must the time-frequency structure of a
genome-resolved gut microbiome originate from oscillators, or is it
consistent with a stable, oscillator-free stochastic dynamics in which
geometric properties of the interaction matrix, rather than eigenvalue
criticality, organise the collective behaviour?

The relevant geometric mechanism is non-normal transient amplification.
For a stable linear stochastic system𝐱˙=𝐀𝐱+𝝃\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\bm{\xi}, when the
operator𝐀\mathbf{A}has non-orthogonal eigenvectors, perturbations can be
transiently amplified by factors far larger than predicted by modal
stability theory[9,10,11,12].
In the stochastic case, the amplification funnels fluctuations onto a
low-dimensional reaction subspace, producing intermittent collective
excursions, irreversible probability currents, and finite-window spectral
peaks that drift in time. Ref.[13,14,15]identifies a sharp geometric transition (pseudo-criticality) at which
these features turn on while the system remains spectrally stable and
admits no Hopf bifurcation. Broader physical implications of non-normal architectures
have recently been argued from a non-equilibrium-steady-state standpoint[16], where life itself is interpreted through the non-normal amplification of fluxes, organising asymmetric reaction networks to amplify free-energy throughput and entropy export. The gut microbiome,
embedded in a host that imposes circadian and dietary flux, is a natural
empirical substrate for this picture.

Asymmetric processes also dominate the microbiome at the interaction
level: directed polysaccharide-utilisation cascades among Bacteroides and
related primary degraders[17,18,19,20,21,22];
one-directional cross-feeding of metabolic by-products (acetate, lactate,
formate) into secondary fermenters such asFaecalibacteriumand
Lachnospiraceae[23,24,25,26];
predation byBdellovibrio bacteriovorus[27];
bacteriocin warfare[28]; and bile-acid mediated chemical
inhibition[29]. Time-series inference of generalised
Lotka-Volterra interaction matrices on murine and human gut data returns
non-symmetric off-diagonal coefficients[30,31,32];
statistical-physics models of directed cross-feeding networks generate
multistability and bursty collective dynamics[33,34]. “Reactivity”, the canonical ecological
footprint of non-normal transient growth, has been formalised for decades[35].

A long tradition in stochastic ecology and stochastic neuroscience has
explored noise-driven collective rhythms in linearly stable systems
without intrinsic oscillators. Demographic-noise quasi-cycles in
predator-prey communities[36,37]exploit a complex-eigenvalue pair with negative real part: the linear
Jacobian carries a damped oscillation at finite frequency and white
noise resonantly amplifies this intrinsic mode, producing persistent
spectral peaks. Non-normality enters this picture as a multiplier of
the amplification: Refs.[38,39]widen and shift the resulting quasi-cycle peaks via the numerical
abscissa of the non-normal Jacobian, but the pre-existing complex
eigenvalues are still required. Ref.[40]uses
non-normality to amplify the spatial amplitude of fluctuation-induced
Turing patterns, with a steady-state spatial wavenumber as the
observable. Recent work on directed neural networks[41,42,43,44]extends the framework to mixed-spectrum non-reciprocal architectures
with reactive transients and effective dimensionality reduction.
These works establish that non-normality is a generic amplifier of
fluctuation-driven structure in stable linear stochastic systems.
The framework we use here[13,14]differs in two respects from this tradition: (i) the linearised
operator that produces pseudo-coherent organisation is taken to have
strictly real negative eigenvalues, so there is no pre-existing
complex mode to resonate with, and (ii) the collective observable is
a time-resolved cluster order parameter, not a spatial wavenumber or
a stationary peak. Pseudo-coherence is the regime in which non-normal
amplification by itself reorganises the imaginary pseudospectrum
sufficiently to produce drifting finite-window spectral peaks,
transient phase alignment, and broken time-reversal symmetry, in a setting with a strictly real spectrum, additive noise, and autonomous linear dynamics. The
present empirical analysis tests whether this regime is realised in
genome-resolved gut-microbiome dynamics, using observables (cluster
order parameter, lead-lag imbalance, wavelet coherence between
support and synchronization, co-membership cluster recovery) that
are diagnostic of pseudo-coherence and that do not require the
detection of an intrinsic frequency.

Using the genome-resolved (MAG-level) mouse-gut dataset of
Ref.[45], we test whether the system carries the joint
signatures of pseudo-coherence:
- (i)

intermittent cluster-level phase alignment, governed by the spatial
extent of the inferred reaction mode rather than by eigenvalue
criticality;
- (ii)

broken time-reversal symmetry quantified by a lagged covariance
imbalance, with a global maximum at intermediate lag;
- (iii)

a time-averaged spectrum with low-frequency enhancement and depleted
intermediate frequencies, no persistent time-frequency ridge, and
strong temporal intermittency in the bands carrying the largest power;
- (iv)

independent identification, from the reaction and non-normal mode
rankings, of the two functional guilds that drive and absorb the
amplification.

All four signatures are observed in both animals. They are jointly
consistent with pseudo-coherence and jointly inconsistent with persistent
oscillator-based synchronisation at the MAG scale. Where the surrogate
analysis admits a weak modulation, it is at the time-averaged level only,
with no fixed time-frequency ridge, which is the operational signature
predicted by the theory. We close with a falsifiable prediction for
clock-gene knockout cohorts.

The claim is scale-specific. The host circadian clock is not denied, and
rhythmic modulation at the coarse bacterial-abundance level is not denied.
What is denied is circadiandominanceat the genome-resolved level,
and an alternative null (pseudo-coherence) is offered that fits the data.

## IIGeometric setup

## Minimal non-normal model.

Consider a linear overdamped stochastic dynamics𝐱˙​(t)=𝐀𝐱​(t)+𝝃​(t),𝐀∈ℝN×N,\dot{\mathbf{x}}(t)=\mathbf{A}\mathbf{x}(t)+\bm{\xi}(t),\qquad\mathbf{A}\in\mathbb{R}^{N\times N},(1)

with𝝃\bm{\xi}a zero-mean white noise and all eigenvalues of𝐀\mathbf{A}in the
strict left half-plane. When𝐀\mathbf{A}is normal, relaxation is purely
Ornstein-Uhlenbeck and the spectrum is featureless. For non-normal𝐀\mathbf{A}([𝐀,𝐀⊤]≠0[\mathbf{A},\mathbf{A}^{\top}]\neq 0), eigenvectors are non-orthogonal and finite-time
perturbations may grow transiently even though every eigenvalue is stable[9,10,11].

When non-normality is strong, all leading transient amplification is
confined to a two-dimensional subspace spanned by a pair of maximally
aligned left and right singular directions of𝐀\mathbf{A}. Diagonalisation of
the commutator𝐁=𝐀𝐀⊤−𝐀⊤​𝐀,\mathbf{B}\;=\;\mathbf{A}\mathbf{A}^{\top}-\mathbf{A}^{\top}\mathbf{A},(2)

which is real symmetric and traceless, returns this subspace as its
rank-two eigenstructure. Projection of𝐀\mathbf{A}onto the subspace yields a2×22\times 2matrix𝚪=(−)​α​β​κ​β/κ−α,α>β>0,κ≥1,\bm{\Gamma}\;=\;\pmatrix{-}\alpha&\beta\kappa\\
\beta/\kappa&-\alpha,\qquad\alpha>\beta>0,\;\kappa\geq 1,(3)

whose eigenvaluesλ±=−α±β\lambda_{\pm}\;=\;-\alpha\pm\beta(4)

remain strictly real and negative for allκ\kappa. The parameterκ\kappameasures eigenvector alignment (κ=1\kappa=1normal,κ≫1\kappa\gg 1strongly
non-normal). The two eigendirections ofΓ\Gammain\eqrefeq:Gamma define the modes: the non-normal mode𝐧^\hat{\mathbf{n}}, which absorbs the stochastic forcing, and the reaction mode𝐫^\hat{\mathbf{r}}into which
perturbations are transiently redirected and amplified. We use the
non-normality indexK=\tfrac​12​(κ−κ−1),K\;=\;\tfrac{1}{2}\bigl(\kappa-\kappa^{-1}\bigr),(5)

and the geometric thresholdKc=1−δ21−1−δ2,δ=|βα|,K_{c}\;=\;\sqrt{\frac{\sqrt{1-\delta^{2}}}{1-\sqrt{1-\delta^{2}}}},\qquad\delta=\biggl|\frac{\beta}{\alpha}\biggr|,(6)

above which the system is reactive: a small perturbation transiently grows before it decays, so that the maximal transient gainG=maxt>0⁡\lVert​eΓ​t​\rVertG=\max_{t>0}\lVert e^{\Gamma t}\rVertexceeds one even though the spectrum stays real and stable[14].

## Pseudo-coherence.

AboveK/Kc=1K/K_{c}=1, the theoretical work[13,14,15]establishes
a sharp geometric transition: the reaction mode acquires extensive support
across system components; stochastic fluctuations concentrate onto this
subspace; the imaginary pseudospectrum reshapes the marginal stochastic
spectrum to amplify slow components and suppress intermediate frequencies;
the lagged covariance becomes asymmetric and a finite imbalance appears;
and finite-window spectra develop drifting peaks that disappear under
stationary, long-time averaging. No eigenvalue crosses the imaginary axis,
no Hopf bifurcation occurs, and no oscillator is required. The empirical
fingerprint of the regime is the conjunction of (i)-(iv) of
Sec.I.

## Per-MAG participation and mode support.

Once the rank-two subspace is identified, the reaction and non-normal
modes are vectors in the original genome-resolved coordinate system. Their
per-MAG magnitudes|ri​(t)|​and​|ni​(t)||r_{i}(t)|\;\;\text{and}\;\;|n_{i}(t)|(7)

give, at every timett, the absolute loading of MAGiion the reaction mode and on the non-normal mode. Because each mode is normalised to unit Euclidean norm (∑iri2=1\sum_{i}r_{i}^{2}=1), these loadings are components of a unit vector, not fractional shares; their time average⟨|ri|⟩t\langle|r_{i}|\rangle_{t}is the mean absolute mode loading reported below. The
commutator𝐁\mathbf{B}has eigenvectors defined up to a common sign, so only|ri||r_{i}|and|ni||n_{i}|are biologically interpretable: the sign of each mode
is a calibration gauge and is not used. The globalsupportof each
mode, that is, how broadly the participation spreads across theNNMAGs,
is summarised bysr​(t)=1N​∑i=1N|ri​(t)|,sn​(t)=1N​∑i=1N|ni​(t)|,s_{r}(t)\;=\;\frac{1}{\sqrt{N}}\sum_{i=1}^{N}|r_{i}(t)|,\qquad s_{n}(t)\;=\;\frac{1}{\sqrt{N}}\sum_{i=1}^{N}|n_{i}(t)|,(8)

withsr,n→1s_{r,n}\to 1for a uniformly distributed mode andsr,n→1/Ns_{r,n}\to 1/\sqrt{N}for a fully localised one. The accompanying
theoretical work[13]shows that assrs_{r}andsns_{n}grow, the amplified subspace becomes extensive, irreversibility and
entropy production rise jointly, and macroscopic phase coherence emerges
as a secondary consequence: support, not eigenvalue proximity to
instability, is the geometric order parameter of pseudo-coherence.

## Cluster-resolved phase coherence.

We follow the non-parametric phase determination of
Ref.[45](briefly recalled in the Methods) to obtain a
phaseθi​(t)\theta_{i}(t)for each MAGii. The cyc7plus assignment of MAGs into
two phase clusters𝒞1\mathcal{C}_{1}and𝒞2\mathcal{C}_{2}[45], obtained by average-linkage hierarchical
clustering on pairwise circular-phase distance, is taken as the input to
two cluster-resolved Kuramoto-like order parametersR𝒞​(t)=|1|𝒞|​∑i∈𝒞ei​θi​(t)|,𝒞∈{𝒞1,𝒞2},R_{\mathcal{C}}(t)\;=\;\left|\frac{1}{|\mathcal{C}|}\sum_{i\in\mathcal{C}}e^{\mathrm{i}\,\theta_{i}(t)}\right|,\qquad\mathcal{C}\in\{\mathcal{C}_{1},\mathcal{C}_{2}\},(9)

which take values in[0,1][0,1]:R𝒞=1R_{\mathcal{C}}=1when all MAGs in cluster𝒞\mathcal{C}share the same instantaneous phase andR𝒞→0R_{\mathcal{C}}\to 0when phases are uniformly scattered around the unit circle. The two
clusters typically realise opposite values ofcos⁡θ\cos\thetaat a given time
and read as anti-synchronised; in the pseudo-coherent framework this
opposition is the geometric sign structure of the reaction mode rather
than evidence of competing oscillator populations[13,14].

## Time-resolved inference.

Over two successive sampling steps the local Jacobian is taken constant
and is estimated from four consecutive observations(𝐱k−3,𝐱k−2,𝐱k−1,𝐱k)(\mathbf{x}_{k-3},\mathbf{x}_{k-2},\mathbf{x}_{k-1},\mathbf{x}_{k})by the least-squares update𝐀^k=𝐘k​𝐗k+,\widehat{\mathbf{A}}_{k}\;=\;\mathbf{Y}_{k}\,\mathbf{X}_{k}^{+},(10)

with𝐘k=(𝐱k,𝐱k−1,𝐱k−2)\mathbf{Y}_{k}=(\mathbf{x}_{k},\mathbf{x}_{k-1},\mathbf{x}_{k-2}),𝐗k=(𝐱k−1,𝐱k−2,𝐱k−3)\mathbf{X}_{k}=(\mathbf{x}_{k-1},\mathbf{x}_{k-2},\mathbf{x}_{k-3}), and𝐗k+\mathbf{X}_{k}^{+}the Moore-Penrose pseudo-inverse. The full Jacobian𝐀^k\widehat{\mathbf{A}}_{k}is
high-dimensional and ill-conditioned, but the non-normal amplification is
rank two and is robustly extracted by diagonalising the commutator𝐁k=[𝐀^k,𝐀^k⊤]\mathbf{B}_{k}=[\widehat{\mathbf{A}}_{k},\widehat{\mathbf{A}}_{k}^{\top}]from
Eq.\eqrefeq:commutator, which is small and well-conditioned even when𝐀^k\widehat{\mathbf{A}}_{k}is itself nearly degenerate. Synthetic calibration
(Methods, Fig.9) shows that the inferredK/KcK/K_{c}never produces false positives, that estimator variance grows with the
trueK/KcK/K_{c}and itself serves as a diagnostic, and that reaction-mode
recovery becomes essentially perfect forK/Kc≳2K/K_{c}\gtrsim 2.

## IIIResults

We apply the pipeline of Sec.IIto the genome-resolved
mouse-gut time series of Ref.[45], hourly samples across
two weeks of two animals (Mouse A and Mouse B). The two animals are
treated in parallel throughout, and every diagnostic is reported for both.

## III.1Cluster order parameters and non-normal diagnostics through time

We follow the non-parametric phase determination (NPPD) of
Ref.[45](recalled in the Methods) to obtain a phaseθi​(t)\theta_{i}(t)for each MAGii. The cyc7plus assignment of MAGs to two
phase clusters𝒞1,𝒞2\mathcal{C}_{1},\mathcal{C}_{2}[45],
obtained by average-linkage hierarchical clustering on circular-phase
distance, gives the two cluster-resolved Kuramoto-like order parameters
of Eq.\eqrefeq:Rcluster, and our local non-normal calibration
returns the time seriesK/Kc​(t)K/K_{c}(t), the log spectral radiuslog⁡ρ​(𝐀^​(t))\log\rho(\widehat{\mathbf{A}}(t)), and the mode supportssr​(t)s_{r}(t),sn​(t)s_{n}(t)of Eq.\eqrefeq:support. All four observables are shown side by side
for both animals in Fig.1.

The system is linearly stable at every time in both animals
(log⁡ρ<0\log\rho<0throughout). The record-meanK/KcK/K_{c}sits clearly above
unity (red dashed lines on the third row of Fig.1): the
inferred local Jacobian is in a strongly non-normal regime on average,
without ever crossing into spectral instability. The cluster
order-parameter excursions in the second row line up with the support
excursions (twin axis, blue and orange) and with theK/KcK/K_{c}excursions
in the third row: macroscopic phase coherence rises when the amplified
subspace becomes more extensive. In Mouse B, the first 75 h of the
record carry a known nutritional perturbation that disrupted phase
synchronisation transiently (grey shaded window); the local non-normal
observables in the lower panels are unaffected and remain informative
through that interval.Figure 1:Cluster order parameters, mode support, and non-normal
diagnostics through time, Mouse A (left) and Mouse B (right).Rows from top to bottom: cluster-mean abundances; cluster-resolved
Kuramoto-like order parameters (black, firebrick) overlaid with the
reaction- and non-normal-mode supportsr​(t)s_{r}(t),sn​(t)s_{n}(t)of
Eq.\eqrefeq:support on the twin axis (blue solid, orange dashed);
time-resolvedK/KcK/K_{c}with the geometric thresholdK/Kc=1K/K_{c}=1as a
thick black line and the record-mean as a red dashed line on top
(annotated value at the right edge); log spectral radius of the
locally inferred Jacobian with the stability thresholdlog⁡ρ=0\log\rho=0as a thick black line and the record-mean as a red
dashed line. The first75​h75\,\mathrm{h}of the Mouse B record carry
a documented nutritional perturbation (grey shaded window).

## Synchronisation tracks reaction-mode support.

The supportssr​(t)s_{r}(t)andsn​(t)s_{n}(t)on the twin axis of the second row of
Fig.1grow in the same time windows in which the cluster
order parameters peak. To make the link quantitative without imposing
an instantaneous-regression assumption we compute the wavelet coherence
betweensr​(t)s_{r}(t)and the cluster-averaged order parameter⟨R𝒞⟩​(t)=\tfrac​12​[R𝒞1​(t)+R𝒞2​(t)]\langle R_{\mathcal{C}}\rangle(t)=\tfrac{1}{2}\bigl[R_{\mathcal{C}_{1}}(t)+R_{\mathcal{C}_{2}}(t)\bigr]on the same Morlet scale grid as the marginal spectrum. In both
animals the mean coherence sits in the range[0.55,0.70][0.55,0.70]across
every resolved frequency band, with a between-mice gap of at most0.060.06(Table1). The link is therefore present at
every timescale we resolve and is of comparable strength in the two
animals studied (Fig.2and
Table1). Linear Granger causality at lag4​h4\;\mathrm{h}is consistent with the directionalitysr→⟨R𝒞⟩s_{r}\to\langle R_{\mathcal{C}}\ranglein both mice (Mouse Ap=0.033p=0.033;
Mouse Bp=0.061p=0.061; reverse direction not significant in either,p=0.156p=0.156andp=0.131p=0.131), and the lagged cross-correlation
(Fig.3) peaks at zero lag in
Mouse A and at+19​h+19\;\mathrm{h}in Mouse B, the reaction-mode support reaches its maximum roughly one day before the cluster synchronization in Mouse B.
Macroscopic coherence is controlled by how broadly the amplified
excursion spreads across genomes, not by how strongly one could in
principle amplify. This is the geometric signature of pseudo-coherence[13], order is driven by
support, not by proximity to a spectral instability that never occurs.Table 1:Wavelet coherence between the reaction-mode supportsr​(t)s_{r}(t)and the cluster-averaged order parameter⟨R𝒞⟩​(t)\langle R_{\mathcal{C}}\rangle(t), in four frequency bands.Mean cross-Morlet coherence on the same scale grid as the marginal
spectrum. The coherence sits in[0.55,0.70][0.55,0.70]in every band of
both animals, with a between-mice gap of at most0.060.06,
demonstrating that the support–coherence link is present at every
resolved timescale and is of comparable strength in the two mice
studied.Mouse44–1212h1212–2424h2424–4848h4848–100100hA0.610.610.670.670.580.580.700.70B0.650.650.660.660.550.550.640.64Figure 2:Wavelet coherence between the reaction-mode supportsr​(t)s_{r}(t)and the cluster-averaged order parameter⟨R𝒞⟩​(t)\langle R_{\mathcal{C}}\rangle(t), per mouse.Mean cross-Morlet
coherenceΓ2​(f,t)\Gamma^{2}(f,t)for Mouse A (left) and Mouse B (right)
on the same period axis with a single shared colorbar.Figure 3:Lagged cross-correlation betweensr​(t)s_{r}(t)and⟨R𝒞⟩​(t)\langle R_{\mathcal{C}}\rangle(t), per mouse.ρ​(τ)\rho(\tau)forτ∈[−48,+48]​h\tau\in[-48,+48]\,\mathrm{h}; Mouse A in
solid black, Mouse B in dashed black; the peak(ρ,τ)(\rho,\tau)is
marked with a red vertical guide and annotated. Hereρ​(τ)\rho(\tau)correlatessr​(t)s_{r}(t)with⟨R𝒞⟩​(t+τ)\langle R_{\mathcal{C}}\rangle(t+\tau), so a positive peak lag means the supportsrs_{r}reaches its maximum before (leads) the cluster synchronization.

## Summary.

Order is driven by the spatial extent of the inferred reaction subspace,
in both animals. Support and entropy production are linked in the theory[13,16], and the empiricalsrs_{r},sns_{n}traces here are the dynamical observable behind that link.

## III.2The marginal spectrum carries a weak time-averaged construction without a persistent ridgeFigure 4:Time-frequency structure for Mouse A (left) and Mouse B
(right).Top row: Morlet wavelet scalogram of the MAG-averaged power
on the full record; the vertical dashed line marks the72​h72\,\mathrm{h}cage-transfer cutoff. Bottom row: time-averaged
Morlet spectrum, solid black for the full record and dashed red for
the post-72​h72\,\mathrm{h}window, superposed on the5%5\%–95%95\%envelope of250250amplitude-adjusted Fourier surrogates per MAG[46,47,48,49].
Vertical dotted lines mark the candidate harmonic frequencies1/12,1/24,1/48,1/72​h−11/12,1/24,1/48,1/72\,\mathrm{h}^{-1}; a dotted black guide
shows the1/f41/f^{4}reference slope. The candidate low-frequency band below1/10​h−11/10\,\mathrm{h}^{-1}sits in the left portion of the bottom-row panels.

The time-frequency representation (Fig.4, top row)
carries no persistent ridge at any frequency in either animal. The
time-averaged spectrum (bottom row) shows a weak low-frequency
construction in both mice. To test the significance of this construction,
we generateNsurr=250N_{\mathrm{surr}}=250amplitude-adjusted Fourier (AAFT) surrogates per
MAG[46,47,48,49]: each
surrogate preserves the per-MAG one-point distribution and approximately
the marginal power spectrum but destroys phase coherence across MAGs and
non-stationary temporal structure. The time-averaged spectrum of the
observed dataset is compared, at each frequency, with the 5%-95%
empirical surrogate envelope, with the per-frequency exceedancepp-values controlled across frequency bins by the Benjamini–Hochberg false-discovery-rate procedure atq=0.05q=0.05, both on the full record and on the
post-72 h window after the cage-transfer transient[50,51,52]. The candidate harmonic
locations1/121/12,1/241/24,1/481/48,1/72​h−11/72\;\mathrm{h}^{-1}are marked.

The observed spectrum carries a construction in the low-frequency band
in both mice. The peak location falls in the range between roughly1/241/24and1/16​h−11/16\;\mathrm{h}^{-1}in either animal (resolved in the low-frequency part of the bottom-row panels of Fig.4), and is not pinned to exactly1/24​h−11/24\;\mathrm{h}^{-1}. The MAG-level data are obtained after a long
compression chain from raw reads to relative abundance to phase, and the
band averaging implicit in that pipeline can shift the constructive peak
by a few hours, so we read the peak location as a soft band rather than
a sharp frequency. What the surrogate test does establish in both
animals is that the low-frequency band carries a marginal excess over
the AAFT null. The scalograms in the top row of Fig.4simultaneously show that this excess doesnottake the form of a
persistent ridge in the time-frequency plane. The high-frequency tail
in both animals follows the1/f41/f^{4}guide line shown in the bottom
panels, which is the slope predicted by non-normal spectral reshaping
for a system with a strong reaction-mode amplification[13]: the tail therefore validates the
pseudo-coherent picture independently of the low-frequency band.

## Summary.

A time-averaged characteristic time scale exists, in both animals, but no
persistent ridge does. This dissociation, a global construction without
a stationary ridge, is the operational signature of pseudo-coherence:
finite-window spectral concentrations drift in time, and only the average
across many windows shows the construction.

## III.3Broken time-reversal symmetry with a global imbalance peak at intermediate lagFigure 5:Lead-lag covariance imbalance.I​(τ)=‖𝐂​(τ)−𝐂​(τ)⊤‖F/2I(\tau)=\|\mathbf{C}(\tau)-\mathbf{C}(\tau)^{\top}\|_{F}/\sqrt{2}as a function
of lag, computed on the full state including the residual subspace;
Mouse A in solid black, Mouse B in dashed black.

The data𝐱​(t)\mathbf{x}(t)are centered to zero time-mean before the
covariance is computed, so the empirical estimator is unbiased under
time-reversal. The lagged covariance𝐂​(τ)=⟨𝐱​(t)​𝐱​(t+τ)⊤⟩,\mathbf{C}(\tau)\;=\;\langle\mathbf{x}(t)\,\mathbf{x}(t+\tau)^{\top}\rangle,(11)

with𝐱​(t)=𝐱~​(t)−⟨𝐱~⟩t\mathbf{x}(t)=\widetilde{\mathbf{x}}(t)-\langle\widetilde{\mathbf{x}}\rangle_{t},
would be symmetric under time reversal; its Frobenius antisymmetric
componentI​(τ)=12​‖𝐂​(τ)−𝐂​(τ)⊤‖FI(\tau)\;=\;\frac{1}{\sqrt{2}}\,\bigl\|\mathbf{C}(\tau)-\mathbf{C}(\tau)^{\top}\bigr\|_{F}(12)

measures the deviation. In both Mouse A and Mouse B
(Fig.5),I​(τ)I(\tau)is strictly positive, with a clear
maximum at intermediate lag and a gradual decay at larger lag. A finite
imbalance peak is direct evidence of irreversibility and circulating
probability currents at the community level[53,54,55,13].

## Why the peak sits at tens of hours.

The peak ofI​(τ)I(\tau)does not localise a microscopic interaction time;
it localises a macroscopic memory. The biological inputs that the
microbiome processes are themselves multi-scale: intestinal transit (of
order a day in the mouse colon), the enterohepatic bile-acid axis[29], mucus turnover[56,57], and bacterial replication times
of11-7​h7\;\mathrm{h}depending on phylum[58,59]. The directed cross-feeding chain of
Sec.III.4convolves these scales: a perturbation entering
the primary-degrader guild traverses several biochemical layers before
appearing in the downstream fermenters, so the global imbalance peaks at
the length of the pipeline rather than at any single step. Diet response
in the murine gut sits at11-33days[50,52],
which matches the order of magnitude of the observed peak. The local
imaginary-pseudospectrum geometry of the inferred Jacobian[13]provides the corresponding microscopic
contribution.

## Empirical entropy production rate.

The small-τ\tauexpansion of Eq.\eqrefeq:Itau_closed defines a
directly measurable entropy-production proxyΣlocal​(t)=∂τI​(τ,t)|τ=0\Sigma_{\rm local}(t)=\left.\partial_{\tau}I(\tau,t)\right|_{\tau=0}(Eq.\eqrefeq:Sigma_local). We estimateΣlocal​(t)\Sigma_{\rm local}(t)by a
linear fit toI​(τ,t)I(\tau,t)onτ∈[0,3]​h\tau\in[0,3]\;\mathrm{h}within a7272h centred rolling window. The fit recovers the predicted
small-τ\taulinearity with mean coefficient of determinationR2=0.957R^{2}=0.957(Mouse A) andR2=0.968R^{2}=0.968(Mouse B), so the
linear-coefficient identification of Eq.\eqrefeq:Sigma_local is the
correct empirical reduction of Eq.\eqrefeq:Itau_closed at hourly
sampling. The recoveredΣlocal​(t)\Sigma_{\rm local}(t)is strictly positive at
every measurement window of both animals studied (n=2n=2;100%100\%of172172windows in Mouse A and209209windows in Mouse B) and
quasi-stationary in time, with coefficient of variation0.180.18in
Mouse A and0.120.12in Mouse B. The time-mean⟨Σlocal⟩\langle\Sigma_{\rm local}\rangleagrees across the two animals to0.5%0.5\%(Table2) despite their different feeding
histories and different time-mean⟨K/Kc⟩\langle K/K_{c}\rangle(1.861.86in Mouse A,1.631.63in Mouse B). The
corresponding⟨Σlocal2⟩\langle\Sigma_{\rm local}^{2}\rangleis proportional to
the non-equilibrium entropy production rateΦ\Phiof
Eq.\eqrefeq:Phi_closed through the isotropic-noise identityΣlocal2=(σ4/4​α)​Φ\Sigma_{\rm local}^{2}=(\sigma^{4}/4\alpha)\,\Phi. Both animals
therefore carry a strictly positive, stable, and cross-mouse-consistent
entropy production rate of the rank-two reaction subspace, and the
system is in a non-equilibrium steady state rather than near
equilibrium throughout the record[13].Table 2:Empirical entropy-production proxyΣlocal​(t)\Sigma_{\rm local}(t)summary statistics per mouse, computed
from the linear-fit slope ofI​(τ,t)I(\tau,t)onτ∈[0,3]​h\tau\in[0,3]\;\mathrm{h}in a7272h centred rolling window. The time-mean⟨Σlocal⟩\langle\Sigma_{\rm local}\rangleagrees across the two animals
studied to0.5%0.5\%. The proxy is strictly positive at100%100\%of
measurement windows in both mice (fifth column), establishing a
strict non-equilibrium steady state throughout the record.Mouse⟨Σlocal⟩\langle\Sigma_{\rm local}\rangle⟨Σlocal2⟩\langle\Sigma_{\rm local}^{2}\rangleCVnnwindowsfraction>0>0A0.06350.06350.004170.004170.180.18172172100%100\%B0.06320.06320.004050.004050.120.12209209100%100\%Figure 6:Empirical entropy-production proxyΣlocal​(t)\Sigma_{\rm local}(t)time series, per mouse.Light grey: raw
per-stepΣlocal​(t)=∂τI​(τ,t)|τ=0\Sigma_{\rm local}(t)=\partial_{\tau}I(\tau,t)|_{\tau=0}.
Solid black: centred rolling-mean smoothing atW=24​hW=24\,\mathrm{h}.
Black dotted: time mean.

## Summary.

A finite irreversibility scale appears in both animals at intermediate
lag, as expected from multi-step propagation along a directed
cross-feeding pipeline; the slope of the lead-lag imbalance at the
origin returns a strictly positive, quasi-stationary, and
cross-mouse-consistent measurement of the non-equilibrium entropy
production rate that sustains the pseudo-coherent steady state.

## III.4Phase-agnostic cluster recovery and biological composition

The commutator diagonalisation of Eq.\eqrefeq:commutator fixes the
sign of each axis of the rank-two subspace only up to a common sign per
calibration step. Ref.[13,14]shows that the sign of the per-MAG reaction-mode componentri​(t)r_{i}(t)encodes the cluster identity of
the pseudo-coherent regime: components withri>0r_{i}>0co-evolve as one
cluster, components withri<0r_{i}<0as the anti-synchronised partner. To
use this within a sign-degenerate calibration, we definesi​(t)=sign​(ri​(t))s_{i}(t)=\mathrm{sign}(r_{i}(t))and form the per-step co-membership
matrixCi​j=⟨𝟙​[si​(t)=sj​(t)]⟩t=\tfrac​12​(1+⟨si​(t)​sj​(t)⟩t).C_{ij}\;=\;\bigl\langle\mathds{1}[s_{i}(t)=s_{j}(t)]\bigr\rangle_{t}\;=\;\tfrac{1}{2}\bigl(1+\langle s_{i}(t)\,s_{j}(t)\rangle_{t}\bigr).(13)

The quantityCi​jC_{ij}is invariant
under a global sign flip ofrrat any timettand is therefore unaffected
by the calibration sign gauge. Average-linkage hierarchical clustering
onDi​j=1−Ci​jD_{ij}=1-C_{ij}returns a two-cluster partition of the MAGs that
uses no instantaneous phaseθi\theta_{i}, no NPPD pipeline, and no
Kuramoto-like order parameter. The per-MAG confidenceφi=C¯own​(i)−C¯opp​(i)\varphi_{i}=\bar{C}_{\rm own}(i)-\bar{C}_{\rm opp}(i)(mean
co-membership with own cluster minus mean co-membership with the
opposite cluster) ranks MAGs from the most to the least confidently
classified.Figure 7:Co-membership cluster recovery.Per-MAG signed co-membership confidence±φi=±(C¯own​(i)−C¯opp​(i))\pm\varphi_{i}=\pm(\bar{C}_{\rm own}(i)-\bar{C}_{\rm opp}(i))(positive for MAGs assigned to recovered cluster 1, negative
for cluster 2), plotted against the cyc7plus cluster label of
Ref.[45]for Mouse A (left) and Mouse B (right);
each marker is colour-coded by taxonomic family (shared legend
below). The horizontal dashed line is the decision boundary at
zero.

Empirically (Fig.7), the co-membership partition
defined by Eq.\eqrefeq:comem agrees with the cyc7plus NPPD-based
partition of Ref.[45]for98.3%98.3\%of all118118labelled MAGs in Mouse A and93.4%93.4\%of all181181labelled MAGs in
Mouse B (chance baseline:50%50\%). The two partitions are constructed
by two operationally distinct pipelines whose inputs do not share the
same dynamical observable: cyc7plus uses circular-phase distance on the
NPPD-derivedθi​(t)\theta_{i}(t), while the co-membership statistic uses only
the per-step sign ofri​(t)r_{i}(t)inferred from the commutator of the local
Jacobian, with no phase information and no Kuramoto-like order
parameter. The recovered cluster sizes are(44,74)(44,74)in Mouse A and(108,73)(108,73)in Mouse B; the cyc7plus sizes are(46,72)(46,72)and(120,61)(120,61), respectively. Restricting to the top9090MAGs by
per-MAG confidenceφi\varphi_{i}, the agreement with cyc7plus reaches100%100\%in both animals, so all disagreement is concentrated in the
low-confidence tail.

An amplitude-adjusted Fourier surrogate null on the per-MAG
abundance series (Methods) returns a chance
agreement of60.2%60.2\%in Mouse A and63.5%63.5\%in Mouse B, with the
empirical98.3%/93.4%98.3\%/93.4\%values sitting3838and2424percentage
points above the null maximum, respectively, and empiricalp<5×10−3p<5\times 10^{-3}in both animals. The two pipelines are
therefore complementary: they share the same low-rank organisation of
the data, and the size of the agreement above the surrogate null is
itself empirical evidence that the system carries the rank-two
reaction-mode structure assumed by the pseudo-coherent reading[13]; were the dynamics not concentrated on a
low-dimensional non-normal subspace, the commutator-based reaction
mode would not stably extract a sign series that recovers a partition
built independently from the phase signal.

The agreement is conditional on the per-MAG calibration confidenceφi\varphi_{i}in a way that is sharp and quantitatively interpretable.
The NPPD pipeline retains only the MAGs that pass a phase-significance
filter, so its cluster labels are most reliable for the MAGs with the
strongest cyclic signal; symmetrically, the co-membership confidenceφi\varphi_{i}is large only for MAGs whose participation in the reaction
mode is well above the noise floor. Restricting the comparison to the
topKKMAGs byφi\varphi_{i}is therefore the natural conditioning. In
both animals the top9090MAGs reach100%100\%agreement with the
cyc7plus partition. The few MAGs on which the two partitions disagree
all sit in the low-confidence tail and contribute marginally to the
order parameter and to the spectral signature. The reaction-mode
geometry therefore recovers, through a pipeline that does not use the
phaseθi​(t)\theta_{i}(t), the same two-cluster organisation that the
original phase-based analysis extracts; at the per-MAG-confidence
level the recovery is exact for the high-confidence top decile.Figure 8:Time-resolved per-MAG absolute mode loading, organised by the co-membership cluster recovery.Each row pairs the smoothed loading heatmap of the top-1212MAGs with the time-averaged absolute loading as a horizontal bar coloured by taxonomic family. Top
row: reaction-mode cluster 1 in each mouse; middle row:
reaction-mode cluster 2 in each mouse; bottom row: the top-1212contributors to the non-normal mode in each mouse. Cluster labels
are those returned by hierarchical clustering on the co-membership
matrixCi​jC_{ij}of Eq.\eqrefeq:comem, aligned to cyc7plus by the
global sign flip that maximises agreement; partition sizes are(44,74)(44,74)in Mouse A and(108,73)(108,73)in Mouse B. A single colour
scale (top bar) applies to all six heatmaps.

## Biological composition of the two recovered clusters and of the non-normal mode.

Fig.8shows the per-MAG reaction-mode time series
and the time-averaged participation, separately for the two clusters in
each animal, and adds the non-normal-mode top contributors as a third row. Before naming the loaded taxa we quantify how concentrated the modes are. Withpi​(t)=ri​(t)2p_{i}(t)=r_{i}(t)^{2}the per-MAG energy fraction of the unit-norm mode, the inverse participation ratioNeff​(t)=1/∑ipi​(t)2N_{\mathrm{eff}}(t)=1/\sum_{i}p_{i}(t)^{2}gives the effective number of MAGs carrying the mode; a random unit vector inNNdimensions hasNeff≈N/3N_{\mathrm{eff}}\approx N/3. Averaged over time, the reaction and non-normal modes giveNeff≈22N_{\mathrm{eff}}\approx 22(Mouse A,N=118N=118) and≈29\approx 29(Mouse B,N=181N=181), about half the random baselines (4141and6262), and the2020largest-loading MAGs carry77%77\%(Mouse A) and67%67\%(Mouse B) of the mode energy against59%59\%and46%46\%for a random mode. The modes are therefore moderately concentrated, about twice beyond chance, on a few tens of MAGs spanning the two guilds, rather than dominated by a few species or spread uniformly across the community. The two reaction-mode clusters are well populated in both
animals:(44,74)(44,74)in Mouse A and(108,73)(108,73)in Mouse B; the
cyc7plus labelling of the same MAGs reads as(46,72)(46,72)and(120,61)(120,61), respectively. In each animal, one cluster is dominated by
Bacteroidota lineages: Muribaculaceae and Bacteroidaceae in Mouse A,
Muribaculaceae together with Rikenellaceae-type (Alistipes)
and Sutterellaceae-type (Parasutterella) genera in Mouse B,
all of which belong to the upstream guild of primary polysaccharide
degraders and dietary-fibre fermenters. The other cluster is dominated
by Bacillota A families (Lachnospiraceae, Oscillospiraceae,
Butyricicoccaceae, Ruminococcaceae), the canonical secondary
fermenters of the short-chain fatty-acid cascade[17,21,18,23,24,25,26].
The directional cross-feeding architecture of the colon is therefore
reproduced, in both animals and at the genus level visible in
Fig.8, by a partition constructed from a strictly
phase-agnostic calibration. The non-normal-mode top contributors in
the bottom row of Fig.8are more mixed than the
two reaction-mode clusters: primary-degrader Muribaculaceae lineages
are over-represented in both mice, but Lachnospiraceae secondary
fermenters also contribute substantially. This is consistent with the
reading that the non-normal mode reads the spatial gradient that drives
the amplification, set primarily by the upstream donors but also
loaded on the strongest downstream recipients; the reaction
mode encodes its coherent two-cluster output side.

## Why species memberships are not identical across animals.

The two animals share the families most strongly loaded on the amplification (Bacteroidota primary degraders and Bacillota A secondary fermenters),
but the exact genus-level membership of the top-12 ranking differs
between mice; for example,PrevotellaandPseudobutyricicoccusappear in Mouse A but not Mouse B, whileParasutterellaandAlistipesare prominent in Mouse B and absent from Mouse A.
Three contributions to this variability are worth naming: each animal
hosts an individually unique community at the strain and genus level
(sample-to-sample biological variation in the mouse microbiome is well
documented[45]), the metagenomic assembly and binning
pipeline used to construct the MAGs is itself stochastic and recovers
slightly different binnings in the two mice from independent sequencing
runs, and the rank-two calibration places MAGs into the top of the
ranking on the basis of their participation in the inferred reaction
direction (which itself depends on the local Jacobian of the actual
community, not on which genera are most abundant). The fact that the
family-level identity of the upstream and downstream guilds is
preserved across the two animals while the genus-level identity is not
is therefore the expected pattern: the directional trophic
architecture is a community-wide property; the particular genera that
occupy each position in that architecture are animal-specific.

## Summary.

A calibration that uses only the local Jacobian geometry recovers the
two-cluster organisation of Ref.[45]:98.3%98.3\%of
all118118labelled MAGs in Mouse A and93.4%93.4\%of all181181labelled
MAGs in Mouse B, with the top9090MAGs by per-MAG co-membership
confidence reaching100%100\%agreement in both animals. The two
recovered clusters carry biologically distinct family compositions
(Fig.8): Bacteroidota primary degraders vs
Bacillota A secondary fermenters, the same upstream/downstream trophic
split identified earlier in Sec.III.4.

## IVDiscussion

The four expected fingerprints of pseudo-coherence are present jointly, and consistently across both animals, in the genome-resolved mouse-gut data. These four are: intermittent cluster-level phase alignment that tracks the spatial support of the amplified mode rather than proximity to an instability; a markedly time-asymmetric lagged covariance with a global imbalance peak at intermediate lag; a time-averaged spectrum enhanced at low frequency with drifting, non-stationary peaks rather than a fixed ridge; and reaction- and non-normal-mode rankings that recover the two trophic guilds without phase information. Cluster-level phase alignment is intermittent and tracks the
spatial extent of the inferred non-normal amplification rather than
proximity to a spectral instability that never occurs. The lagged
covariance is markedly time-asymmetric, with a global peak at
intermediate lag whose magnitude reflects the directed multi-step
structure of the gut cross-feeding network. The time-averaged spectrum
shows the predicted shape (low-frequency enhancement, depleted
intermediate frequencies, strong temporal intermittency on the same
bands that carry the largest mean power) and no persistent ridge in the
scalograms. Quantitative AAFT surrogate testing[46,47,48,49]localises a
weak time-averaged construction in the low-frequency band of both mice
without a fixed ridge in time. The inferred reaction and non-normal
modes independently identify the two canonical functional guilds of the
mouse colon and assign them biologically informative donor-recipient
roles.

These findings strain the dominant oscillator-based reading of microbiome
rhythmicity at the MAG scale. A persistent host-entrained ridge would
have to manifest in the scalogram of every individual; it does not. A
near-Hopf interpretation would predict qualitative reorganisation after
moderate perturbations; the antibiotic dataset reported in
Ref.[45]shows shock-and-recovery rather than
bifurcation crossing. A genuine persistent multi-mouse circadian
component, at exactly1/24​h−11/24\;\mathrm{h}^{-1}and stationary in time, is
not what the data show. By contrast, every signature of pseudo-coherence
is present in both mice and at every diagnostic. We emphasise that the surrogate test on the marginal spectrum is a lower-bound consistency check on excess power, not in itself a discriminator between an oscillator and pseudo-coherence: an amplitude-adjusted surrogate inherits each MAG’s marginal spectrum, so a genuine narrow-band oscillator would copy into the surrogate ensemble and erode its own exceedance. The discrimination instead rests on the absence of a persistent scalogram ridge, on the lead–lag imbalance peaking at tens of hours rather than at an oscillator half-period, and on the recovery of two genuine reaction-mode clusters.

This does not deny the host circadian clock, nor does it deny the
existence of rhythmic modulation at the abundance level of bacterial
families. It denies that, at hourly genome resolution, a stable
oscillator is the appropriate null. The appropriate null is a stable,
strongly non-normal stochastic system.

## From host-clock labels to a trophic re-reading of the two clusters.

The two phase clusters𝒞1,𝒞2\mathcal{C}_{1},\mathcal{C}_{2}in
Ref.[45]are extracted from circular-phase distance
on the NPPD-derivedθi​(t)\theta_{i}(t)and identified there with a
host-clock-aligned night vs day partition. The cluster recovery of
Sec.III.4uses an independent route: it builds the
co-membership statistic from the sign of the per-step reaction-mode
component, which by construction is phase-agnostic and
spectrally-agnostic. The fact that the two routes agree on98.3%98.3\%(Mouse A) and93.4%93.4\%(Mouse B) of all labelled MAGs, and on the top9090MAGs of each animal exactly, shows that the same two-cluster
organisation is the natural output of two very different lenses on the
data. The composition of the two clusters
(Fig.8) makes the interpretation concrete: the
cyc7plus cluster𝒞1\mathcal{C}_{1}collects the Bacteroidota primary
polysaccharide degraders (Muribaculaceae and Bacteroidaceae in
Mouse A, together with Rikenellaceae-likeAlistipesand
Sutterellaceae-likeParasutterellain Mouse B), while cluster𝒞2\mathcal{C}_{2}collects the Bacillota A secondary SCFA fermenters
(Lachnospiraceae, Butyricicoccaceae, Oscillospiraceae,
Ruminococcaceae). The two clusters are therefore not naturally a
night/day partition but the upstream and downstream ends of the
cross-feeding cascade.

This re-reading is in fact directly consistent with the host-clock
labels in Ref.[45]: in nocturnal mice the active
feeding phase is the dark phase, dietary fibre arrives at the colon
predominantly during the night, the primary-degrader Bacteroidota
respond first, and the secondary fermenters of the SCFA cascade
respond a multi-hour lag later through cross-feeding. The
cyc7plus night cluster of
Ref.[45]is then exactly the upstream guild that
tracks fibre arrival, and the day cluster is the downstream guild
that tracks the delayed SCFA wave. The apparent
night/day split is a faithful readout of the cross-feeding delay
between primary and secondary fermenters, not evidence of an
autonomous oscillator at the MAG level. The
intermediate-lag peak ofI​(τ)I(\tau)in Fig.5(Sec.III.3) gives an independent estimate of this
delay from the genome-resolved data alone. Under this reading, the
24 h modulation of the host feeding cycle remains the natural
entrainment input, but the two-cluster organisation of the MAG-level
dynamics is a property of the trophic architecture of the community,
not of a community-level circadian oscillator. This is a
non-circadian-driven mechanistic account that is fully compatible
with the cyc7plus phenomenology and with the absence of a persistent
24 h ridge in the scalograms of Fig.4.

## Support, entropy production, and non-equilibrium steady state.

A subtler feature of the data is that the supportssrs_{r}andsns_{n}of
Eq.\eqrefeq:support grow synchronously with the cluster order
parameters, and the band-resolved wavelet coherence betweensrs_{r}and⟨R𝒞⟩\langle R_{\mathcal{C}}\rangle(Table1) plus the
slow-component Pearson correlation identify support, notK/KcK/K_{c}, as
the dominant geometric driver of macroscopic phase coherence. In the pseudo-coherent framework, support has a
thermodynamic meaning: as the reaction subspace becomes more extensive,
circulating probability currents in phase space grow, the lead-lag
imbalance of Fig.5rises, and the entropy production
rate increases. The community is held away from equilibrium by a
continuous influx of free energy from the host (dietary input, bile-acid
recycling) and exports the corresponding entropy through metabolic
products (SCFAs, gases, microbial cell death). The empirical observation
that support and coherence rise together is therefore the dynamical
signature of a microbiome operating in a non-equilibrium steady state[53,54,55],
sustained by directional cross-feeding rather than by oscillator-mediated
phase locking.

## Life as non-normal amplification of fluxes.

This reading aligns the microbiome with a recent general framework in which life is interpreted through the non-normal amplification of fluxes[16]: biological systems evolve asymmetric,
hierarchical reaction networks that amplify the throughput of free energy
without crossing a bifurcation, and the resulting directional
architectures generate transient amplification cycles that maintain the
non-equilibrium steady state. The gut microbiome here provides a direct
empirical realisation of that principle. In the gut, metabolic by-products that leak from one population become resources for others, so resource competition and unidirectional cross-feeding commensalism act together; this combination raises free-energy use, entropy production, and the amplification of metabolic fluxes. The directional cross-feeding chain from Bacteroidota primary degraders to Bacillota A secondary fermenters identified in Sec.III.4is exactly the kind of hierarchical asymmetric architecture the framework predicts will generate large flux amplification, and the inferred reaction and non-normal modes localise the upstream and downstream endpoints of the chain from a dynamical observable alone.

## Active matter and broader physics.

At the same level of generality, active matter itself is a proper subfield of non-normal stochastic dynamics[60,61]: its non-reciprocal, hierarchical interactions render the linearised operator non-normal, so the transient amplification, broken time-reversal symmetry, and entropy production documented here also organise self-propelled active systems, of which the gut microbiome is one chemical realisation. Active matter literature has long observed that directional
inter-particle interactions generate band-pass spectral signatures and
broken time-reversal symmetry without underlying
oscillators[62,63,64];
the present analysis brings the same machinery to genome-resolved
microbial data and demonstrates that the operational signatures are
present and quantifiable.

Non-normal stochastic systems are common in ecological interaction
networks[30,31,32,33,34,35],
in atmospheric and oceanic dynamics[10,65,11], and
in balanced neural networks[42,43,44].
Whenever interactions are intrinsically directional, the operator that
governs the dynamics is generically non-normal, and rhythmic structure in
observables of such systems is not in general evidence of oscillators.
In neural systems, the canonical frequency bands of the rhythm of the
brain[66,67]have been interpreted within the
pseudo-coherent framework as finite-time spectral concentrations driven
by non-normal amplification in balanced networks[13,42]. The same diagnostic battery used
here, namely reaction- and non-normal-mode participation, support-based
coherence regression, lead-lag imbalance, and marginal-spectrum surrogate
testing, is portable to such other high-dimensional rhythmic biological
data.

## Falsifiable prediction for clock-gene-knockout cohorts.

The mechanism makes two contrasting empirical predictions for a
genome-resolved hourly cohort of clock-gene-disrupted mice (intestinal
Bmal1 knockout, Per1/Per2 double knockout, Cry1/Cry2 double knockout, or
environmental jet lag[1,68,3,69,70,71,72,73,74,75,76,77,78,79,80,4]).
The non-normal interpretation predicts a selective dissociation between two classes of observables, rather than a binary opposite to an oscillator picture. Quantities tied to the microbial interaction geometry, namely transient amplification, the reaction- and non-normal-mode structure, the lead-lag asymmetry, and the broad guild identities of the highest-loading MAGs, should remain present, although their numerical values may shift if the knockout changes diet, transit, bile acids, or community composition. By contrast, any narrow host-clock-locked24​h24\;\mathrm{h}component should be reduced or lose phase consistency. The decisive signature is therefore the preservation of finite-time asymmetric response structure together with the weakening of host-clock-locked circadian coherence. This separates three pictures: a host-clock-entrainment picture, in which clock disruption primarily degrades phase locking, cluster synchrony, and any24​h24\;\mathrm{h}ridge, with the interaction-geometry diagnostics changing only as consequences of that loss; a microbial-autonomous-oscillator picture, in which a coherent near-24​h24\;\mathrm{h}ridge persists even without the host clock; and the non-normal pseudo-coherence picture, in which the narrow24​h24\;\mathrm{h}component weakens but the transient amplification, lead-lag asymmetry, and mode-guild structure remain. Existing datasets can test coarse circadian abundance rhythms, but not the hourly, MAG-resolved non-normal diagnostics used here; the discriminating experiment therefore requires hourly, genome-resolved sampling under clock disruption.

## VMethods

## Data.

We use the genome-resolved mouse-gut metagenomic time series of
Ref.[45], sampled hourly across two weeks for two
animals (Mouse A and Mouse B). For each animal we use the relative-
abundance and phase tables together with the cyc7plus cluster assignments
of Ref.[45], joined with the GTDB-Tk taxonomy of each
MAG[81]. The taxonomic family and genus labels
appearing in the figures and text are those assigned by the GTDB-Tk
toolkit on the MAGs provided with Ref.[45], not
hand-curated; uncultured lineages carry placeholder names of the form
“UBA”/“CAG”/“MGBC”.

## Phase extraction (NPPD).

The non-parametric phase determination is taken verbatim from
Ref.[45]. For a discrete time seriesx​(t)x(t)sampled
hourly, a moving-median trend over a24​h24\;\mathrm{h}window is removed,x′​(t)=x​(t)−xmed​(t)x^{\prime}(t)=x(t)-x_{\mathrm{med}}(t). A local referencem​(t)m(t)is taken as
the median ofx′x^{\prime}in the same24​h24\;\mathrm{h}window. Within that
window the signs ofx′x^{\prime}relative tom​(t)m(t)are tabulated into a2×22\times 2contingency table comparing past and future halves, and a
one-tailed Fisher exact test produces app-valuePFisher​(t)P_{\mathrm{Fisher}}(t). The signed local significance scorew​(t)=sign​[a​(t)​d​(t)−b​(t)​c​(t)]​log⁡PFisher​(t)w(t)\;=\;\mathrm{sign}\bigl[a(t)d(t)-b(t)c(t)\bigr]\,\log P_{\mathrm{Fisher}}(t)(14)

captures the direction and statistical strength of local transitions.
Zero-crossings ofw​(t)w(t)and local extrema between them serve as anchor
points; each cycle is divided into four quadrantsϕT∈{0,π/2,π,3​π/2}\phi_{T}\in\{0,\pi/2,\pi,3\pi/2\}, and the instantaneous phaseθ​(t)=ϕT​(t)mod2​π\theta(t)=\phi_{T}(t)\bmod 2\piis obtained by linear interpolation
between anchors followed by wrapping. The procedure is non-parametric,
makes no waveform assumption, and is robust to non-stationarity and
non-sinusoidal shapes.

## Cluster construction.

The cyc7plus partition of MAGs into two clusters (used throughout this
paper and in the original Ref.[45]) is built from the
pairwise circular phase distance between MAGs. After phase unwrapping,
the pairwise mean phase differenceΔ​ϕi​j\Delta\phi_{ij}is computed and
mapped to a distancedi​j=\tfrac​12​(1−cos⁡Δ​ϕi​j)d_{ij}=\tfrac{1}{2}(1-\cos\Delta\phi_{ij}).
Average-linkage hierarchical clustering ondi​jd_{ij}followed by
two-cluster extraction yields the partition reported in
Ref.[45]that we adopt as the input to the Kuramoto-
like order parametersR𝒞​(t)=|1|𝒞|​∑i∈𝒞ei​θi​(t)|.R_{\mathcal{C}}(t)\;=\;\biggl|\frac{1}{|\mathcal{C}|}\sum_{i\in\mathcal{C}}e^{\mathrm{i}\theta_{i}(t)}\biggr|.(15)

## Local non-normal calibration via the commutator.

Over four consecutive observations we estimate𝐀^k\widehat{\mathbf{A}}_{k}from
Eq.\eqrefeq:Ahat. Rather than diagonalising𝐀^k\widehat{\mathbf{A}}_{k}, we
diagonalise the commutator𝐁k\mathbf{B}_{k}of Eq.\eqrefeq:commutator, which
is real symmetric and traceless. When non-normality is significant,𝐁k\mathbf{B}_{k}has rank two with eigenvalues±λmax\pm\lambda_{\mathrm{max}}and
eigenvectors spanning the non-normal subspace. Projecting𝐀^k\widehat{\mathbf{A}}_{k}onto this subspace yields the reduced2×22\times 2matrix𝚪k\bm{\Gamma}_{k}of Eq.\eqrefeq:Gamma, from which the non-normality
indexKKfrom\eqrefeq:K, the thresholdKcK_{c}from\eqrefeq:Kc, the
spectral radiusρ\rho, and the per-MAG reaction- and non-normal-mode
loadings of\eqrefeq:participation are computed. The signs of the
loadings are not used because the eigendecomposition of𝐁k\mathbf{B}_{k}fixes
each axis only up to a common sign flip.Figure 9:Synthetic calibration of the local non-normal
inference.Inferred⟨K/Kc⟩\langle K/K_{c}\rangle(top), estimator standard
deviation (middle), and reaction-mode recovery accuracy (bottom)
versus trueK/KcK/K_{c}.

## Co-membership cluster recovery.

The commutator diagonalisation of𝐁k\mathbf{B}_{k}fixes the axis𝐫^​(t)\hat{\mathbf{r}}(t)of the rank-two reaction subspace only up to a
common sign flip:(𝐫^,𝐧^)(\hat{\mathbf{r}},\hat{\mathbf{n}})and(−𝐫^,−𝐧^)(-\hat{\mathbf{r}},-\hat{\mathbf{n}})are
indistinguishable eigenpairs of the real symmetric𝐁k\mathbf{B}_{k}. Any quantity
built from the time seriesri​(t)r_{i}(t)that is not invariant under
this per-step sign gauge is therefore not a well-defined statistic.
In particular, the naive cluster recoveryci=sign​⟨ri​(t)⟩tc_{i}=\mathrm{sign}\,\langle r_{i}(t)\rangle_{t}requires an a priori
sign-alignment of𝐫^​(t)\hat{\mathbf{r}}(t)across consecutive calibration
windows, and is sensitive to spurious sign flips that the alignment
procedure inevitably introduces in low-confidence stretches.

To bypass the gauge entirely we use the per-step co-membership
matrix of Eq.\eqrefeq:comem. Withsi​(t)=sign​ri​(t)s_{i}(t)=\mathrm{sign}\,r_{i}(t),
the statisticCi​j=⟨𝟙​[si​(t)=sj​(t)]⟩t=\tfrac​12​(1+⟨si​(t)​sj​(t)⟩t)C_{ij}\;=\;\bigl\langle\mathds{1}\bigl[s_{i}(t)=s_{j}(t)\bigr]\bigr\rangle_{t}\;=\;\tfrac{1}{2}\bigl(1+\langle s_{i}(t)\,s_{j}(t)\rangle_{t}\bigr)(16)

is manifestly invariant under a global sign flip of𝐫^\hat{\mathbf{r}}atanytimett, because flipping all signs at the samettdoes
not change the indicator𝟙​[si​(t)=sj​(t)]\mathds{1}[s_{i}(t)=s_{j}(t)]for any pair(i,j)(i,j).Ci​j∈[0,1]C_{ij}\in[0,1]measures the fraction of calibration windows
in which MAGsiiandjjsit on the same side of zero in the reaction
mode, and is well-defined without any sign-alignment pass.

The partition is obtained by average-linkage hierarchical clustering on
the distance matrixDi​j=1−Ci​jD_{ij}=1-C_{ij}, symmetrised and with zero
diagonal, with the dendrogram cut at two clusters. Per-MAG confidence
is the gap between mean own-cluster and mean opposite-cluster
co-membership,φi=1|𝒞​(i)|−1​∑\substack​j∈𝒞​(i)​j≠iCi​j−1|𝒞​(i)c|​∑j∈𝒞​(i)cCi​j,\varphi_{i}\;=\;\frac{1}{|\mathcal{C}(i)|-1}\!\!\!\!\sum_{\substack{j\in\mathcal{C}(i)\\
j\neq i}}\!\!\!C_{ij}\;-\;\frac{1}{|\mathcal{C}(i)^{c}|}\!\!\!\sum_{\,j\in\mathcal{C}(i)^{c}}\!\!\!C_{ij},(17)

where𝒞​(i)\mathcal{C}(i)is the cluster containing MAGiiand𝒞​(i)c\mathcal{C}(i)^{c}its complement.φi→1\varphi_{i}\to 1for a MAG that is
in the same group as all of its own cluster at every time and never in
the same group as the opposite cluster;φi→0\varphi_{i}\to 0for a MAG
whose sign in the reaction mode is uninformative. The top-KKconditional agreement reported in Sec.III.4is the fraction
of cyc7plus labels reproduced when theKKMAGs of largestφi\varphi_{i}are retained.

## Surrogate test for the marginal Morlet spectrum.

For each MAG we generateNsurr=250N_{\mathrm{surr}}=250amplitude-adjusted Fourier
surrogates following Refs.[46,47,48].
Each surrogate preserves the per-MAG one-point distribution and
approximately the marginal power spectrum, but destroys phase coherence
across MAGs and non-stationary temporal structure. For each surrogate we
compute the time-averaged Morlet spectrum on the same scale grid as the
data (100 scales logarithmically spaced over periods of11-100​h100\;\mathrm{h},
cmor1.5-1.0 wavelet) and average across MAGs. Per-frequency exceedance probabilities are corrected for multiple comparisons across frequency bins by the Benjamini–Hochberg procedure at a false-discovery rate of0.050.05; atNsurr=250N_{\mathrm{surr}}=250the resolvablepp-value floor (≈1/251\approx 1/251) is small enough to pass this correction, whereasNsurr=50N_{\mathrm{surr}}=50is not. The full record and the
post-72 h window (after the cage-transfer transient) are analysed
separately.

## Lead-lag imbalance: closed form and small-τ\tauexpansion.

The lagged covariance𝐂​(τ)\mathbf{C}(\tau)of Eq.\eqrefeq:Ctau is estimated
by direct sample average andI​(τ)I(\tau)from Eq.\eqrefeq:Itau by the
Frobenius norm of its antisymmetric part. For the reduced two-dimensional
pseudo-coherent dynamics with noise covariance𝐁=(σ)12​ρ​σ1​σ2​ρ​σ1​σ2​σ22\mathbf{B}=\pmatrix{\sigma}_{1}^{2}&\rho\sigma_{1}\sigma_{2}\\
\rho\sigma_{1}\sigma_{2}&\sigma_{2}^{2},
Ref.[13,14]derives the closed formI​(τ)=σ1​σ22​2​α​|Kσ|​|e−(α−β)​τ−e−(α+β)​τ|,I(\tau)=\frac{\sigma_{1}\sigma_{2}}{2\sqrt{2}\,\alpha}\,|K_{\sigma}|\,\left|e^{-(\alpha-\beta)\tau}-e^{-(\alpha+\beta)\tau}\right|,(18)

whereα\alphaandβ\betaare the diagonal coefficients of the
rotated reduced operator𝚪rot\bm{\Gamma}_{\rm rot}, andKσ=\tfrac​12​(κσ−κσ−1)K_{\sigma}=\tfrac{1}{2}(\kappa_{\sigma}-\kappa_{\sigma}^{-1})withκσ=κ​σ2/σ1\kappa_{\sigma}=\kappa\,\sigma_{2}/\sigma_{1}is the effective
non-normality index modulated by the noise covariance. In the
isotropic-noise case (σ1=σ2\sigma_{1}=\sigma_{2},ρ=0\rho=0),Kσ=KK_{\sigma}=Kand the lead-lag imbalance is controlled purely by
the geometric non-normality of the operator.

Expanding Eq.\eqrefeq:Itau_closed aroundτ=0\tau=0gives, to
leading order inτ\tau,{split}​I​(τ)=Σlocal​τ+𝒪​(τ2),Σlocal≡∂τI​(τ)|τ=0=σ1​σ2​β​|Kσ|2​α.\split I(\tau)\;&=\;\Sigma_{\rm local}\,\tau\;+\;\mathcal{O}(\tau^{2}),\\
\Sigma_{\rm local}\;&\equiv\;\left.\partial_{\tau}I(\tau)\right|_{\tau=0}\;=\;\frac{\sigma_{1}\sigma_{2}\,\beta\,|K_{\sigma}|}{\sqrt{2}\,\alpha}.(19)

The slope ofI​(τ)I(\tau)at the origin is therefore a directed-flow
amplitude that grows linearly with the effective non-normality|Kσ||K_{\sigma}|and serves as a local, hour-scale empirical observable.
We estimateΣlocal​(t)\Sigma_{\rm local}(t)from a parabolic fit toI​(τ,t)I(\tau,t)onτ∈[0,3]​h\tau\in[0,3]\;\mathrm{h}within a72​h72\;\mathrm{h}centred rolling window.

## Entropy production rate.

For the same reduced dynamics, Ref.[13]derives
the closed form for the stationary entropy production rate of the
non-equilibrium steady state,Φ=2​β2α​Kσ21−ρ2,\Phi\;=\;\frac{2\beta^{2}}{\alpha}\,\frac{K_{\sigma}^{2}}{1-\rho^{2}},(20)

which grows quadratically with the effective non-normality and
vanishes in the normal limit. Comparing
Eqs.\eqrefeq:Sigma_local and\eqrefeq:Phi_closed in the
isotropic-noise case yields the identityΣlocal2=\tfrac​14​σ4​Φ/α\Sigma_{\rm local}^{2}=\tfrac{1}{4}\sigma^{4}\,\Phi/\alpha, so that
the empirically accessibleΣlocal​(t)\Sigma_{\rm local}(t)is theτ→0\tau\to 0projection of the same non-equilibrium current that is
captured byΦ\Phi. Increases of the reaction-mode and non-normal-mode
supports therefore couple directly to increases ofΦ\Phithrough the
effective non-normality indexKσK_{\sigma}: an extended reaction
subspace amplifies the noise anisotropy seen by the rank-two
projection, raisingKσK_{\sigma},Σlocal\Sigma_{\rm local}, andΦ\Phitogether. This is the thermodynamic content of pseudo-coherence[13,16].

## Support–coherence link: three
diagnostics with disjoint sensitivities.

The link between the reaction-mode supportsr​(t)s_{r}(t)and the cluster-
averaged order parameter⟨R𝒞⟩​(t)\langle R_{\mathcal{C}}\rangle(t)is
quantified by three standard signal-processing tools,
each probing a different aspect of the dependence.

Wavelet coherence.Cross-Morlet decomposition with the samecmor1.5-1.0wavelet and scale grid as the marginal spectrum
yields a time-frequency coherence mapΓ2​(f,t)∈[0,1]\Gamma^{2}(f,t)\in[0,1]that
measures the squared magnitude of the local cross-spectrum normalised
by the geometric mean of the two local autospectra; the local
autospectra and cross-spectrum are smoothed in time by a Hann window
of width33periods at each scale before normalisation. We report
the band-averaged mean coherence in four logarithmically spaced bands
of periods44–1212,1212–2424,2424–4848, and4848–100​h100\;\mathrm{h}. Edge effects within one period of either
record boundary are excluded by a cone-of-influence mask. This measure
is invariant to constant phase offsets between the two series and is
therefore unaffected by the lead-lag structure that biases the
instantaneous Pearson correlation.

Lagged cross-correlation.We standardisesrs_{r}and⟨R𝒞⟩\langle R_{\mathcal{C}}\rangleto zero mean and unit variance and
compute the cross-correlationρ​(τ)=corr​[sr​(t),⟨R𝒞⟩​(t+τ)]\rho(\tau)=\mathrm{corr}\bigl[s_{r}(t),\langle R_{\mathcal{C}}\rangle(t+\tau)\bigr]forτ∈[−48,+48]​h\tau\in[-48,+48]\;\mathrm{h}at the
hourly resolution of the data, and report the peak amplitude and the
peak lag. A positive peak lag indicates thatsrs_{r}leads⟨R𝒞⟩\langle R_{\mathcal{C}}\rangle.

Linear Granger causality.We fit two vector-autoregressive
models of lagL=4​hL=4\;\mathrm{h}on the centred series: an
unrestricted model where each series is regressed on its own four
past values and on the four past values of the other, and a
restricted model where the cross-series terms are zero. The GrangerFF-test of the restricted-vs-unrestricted residual sum of squares
gives app-value for the null “the second series does not
Granger-cause the first”; we report thepp-values in both
directions at lag4​h4\;\mathrm{h}on the un-smoothed series; the
test is reported as a directional consistency check, not as a
hypothesis test against a0.050.05threshold, because the residual
autocorrelation of the data inflates the variance of theFF-statistic. Implementation usesstatsmodels.tsa.stattools.grangercausalitytests.

## Calibration pipeline at a glance.

The empirical pipeline that produces every per-step observable used
in this work is the same composition of four operations at each
time-steptt: (1) assemble the44-sample windowXt=[𝐱​(t−3),𝐱​(t−2),𝐱​(t−1),𝐱​(t)]⊤X_{t}=[\mathbf{x}(t-3),\mathbf{x}(t-2),\mathbf{x}(t-1),\mathbf{x}(t)]^{\top}; (2) fit the local JacobianA^t\widehat{A}_{t}fromXtX_{t}by Eq.\eqrefeq:Ahat; (3) extract the
rank-two reaction direction𝐫^t\hat{\mathbf{r}}_{t}and non-normal direction𝐧^t\hat{\mathbf{n}}_{t}via the eigenvectors of the commutatorB^t=A^t​A^t⊤−A^t⊤​A^t\widehat{B}_{t}=\widehat{A}_{t}\widehat{A}_{t}^{\top}-\widehat{A}_{t}^{\top}\widehat{A}_{t}(Eq.\eqrefeq:commutator); (4) project per-MAG
components, deriveK/Kc​(t)K/K_{c}(t),sr​(t)s_{r}(t),sn​(t)s_{n}(t), and the per-step
reaction-mode signsi​(t)=sign​(ri​(t))s_{i}(t)=\mathrm{sign}(r_{i}(t))that feeds the
co-membership matrix of Eq.\eqrefeq:comem. The same pipeline
feeds both the spectral and lead-lag analyses (through the time
series ofK/KcK/K_{c}and the support) and the cluster recovery (through
the per-step signs).

## Surrogate-null distribution for the co-membership cluster
agreement.

To distinguish the agreement between the cyc7plus and the
co-membership partitions from the rank-two coincidence that any two
sign-based pipelines might extract from a near-rank-two abundance
matrix, we generateB=200B=200amplitude-adjusted Fourier surrogates
of each MAG abundance series. The surrogate procedure preserves the
per-MAG marginal power spectrum and one-point amplitude distribution
by construction while destroying the inter-MAG phase coherence
through an independent phase randomisation per MAG. On each surrogate
ensemble we run the full co-membership pipeline (rank-two commutator
decomposition, per-step sign extraction,Ci​jC_{ij}matrix
construction, average-linkage hierarchical clustering) and compare
the resulting two-cluster partition to the fixed cyc7plus reference.
We report the empirical distribution of the agreement statistic across
theBBsurrogates, and thepp-value of the data against the quantile
of that distribution.

## References
- Thaisset al.[2014]C. Thaiss, D. Zeevi,
M. Levy, G. Zilberman-Schapira, J. Suez, A. Tengeler, L. Abramson, M. Katz, T. Korem, N. Zmora,
Y. Kuperman, I. Biton, S. Gilad, A. Harmelin, H. Shapiro, Z. Halpern, E. Segal, and E. Elinav,Cell159, 514
(2014).
- Zarrinparet al.[2014]A. Zarrinpar, A. Chaix,
S. Yooseph, and S. Panda,Cell Metabolism20, 1006 (2014).
- Lianget al.[2015]X. Liang, F. D. Bushman, and G. A. FitzGerald,Proc. Natl. Acad. Sci. USA112, 10479 (2015).
- Leoneet al.[2015]V. Leone, S. Gibbons,
K. Martinez, A. Hutchison, E. Huang, C. Cham, J. Pierre, A. Heneghan,
A. Nadimpalli, N. Hubert, E. Zale, Y. Wang, Y. Huang, B. Theriault,
A. Dinner, M. Musch, K. Kudsk, B. Prendergast, J. Gilbert, and E. Chang,Cell Host Microbe17, 681 (2015).
- Asher and Sassone-Corsi [2015]G. Asher and P. Sassone-Corsi,Cell161, 84 (2015).
- Kuramoto [1975]Y. Kuramoto, International Symposium on Mathematical Problems in Theoretical Physics , 420 (1975).
- Acebrónet al.[2005]J. A. Acebrón, L. L. Bonilla, C. J. P. Vicente, F. Ritort, and R. Spigler, Reviews of Modern
Physics77, 137
(2005).
- Pikovskyet al.[2001]A. Pikovsky, M. Rosenblum, and J. Kurths,Synchronization: A
Universal Concept in Nonlinear Sciences(Cambridge
University Press, 2001).
- Trefethen and Embree [2005]L. N. Trefethen and M. Embree,Spectra and
Pseudospectra(Princeton University Press, 2005).
- Farrell and Ioannou [1996]B. F. Farrell and P. J. Ioannou,Journal of the Atmospheric Sciences53, 2025 (1996).
- Trefethenet al.[1993]L. N. Trefethen, A. E. Trefethen, S. C. Reddy, and T. A. Driscoll, Science261, 578
(1993).
- Muoloet al.[2019a]R. Muolo, M. Asllani,
D. Fanelli, P. K. Maini, and T. Carletti,Journal of Theoretical Biology480, 81 (2019a).
- Troude and Sornette [2026]V. Troude and D. Sornette,arXiv preprint arXiv:2603.07206 (2026),arXiv:2603.07206.
- Troude and Sornette [2025]V. Troude and D. Sornette,Phys. Rev. Res.7, L042048 (2025).
- Troudeet al.[2025]V. Troude, S. C. Lera,
K. Wu, and D. Sornette,Illusions of
criticality: Crises without tipping points(2025),arXiv:2412.01833 [nlin.CD].
- Sornette and Troude [2025]D. Sornette and V. Troude,Life
as a non-normal chemical accelerator(2025),arXiv:2512.18438 [cond-mat.stat-mech].
- Koropatkinet al.[2012]N. M. Koropatkin, E. A. Cameron, and E. C. Martens,Nat. Rev. Microbiol.10, 323 (2012).
- Rakoff-Nahoumet al.[2014]S. Rakoff-Nahoum, M. Coyne, and L. Comstock,Curr. Biol.24, 40 (2014).
- Rakoff-Nahoumet al.[2016]S. Rakoff-Nahoum, K. R. Foster, and L. E. Comstock,Nature533, 255 (2016).
- Mahowaldet al.[2009]M. A. Mahowald, F. E. Rey,
H. Seedorf, P. J. Turnbaugh, R. S. Fulton, A. Wollam, N. Shah, C. Wang, V. Magrini,
R. K. Wilson, B. L. Cantarel, P. M. Coutinho, B. Henrissat, L. W. Crock, A. Russell, N. C. Verberkmoes, R. L. Hettich, and J. I. Gordon,Proc. Natl. Acad. Sci. USA106, 5859 (2009).
- Flintet al.[2012]H. J. Flint, K. P. Scott,
S. H. Duncan, P. Louis, and E. Forano,Gut Microbes3, 289 (2012).
- Sonnenburg and Sonnenburg [2014]E. Sonnenburg and J. Sonnenburg,Cell Metab.20, 779 (2014).
- Belengueret al.[2006]A. Belenguer, S. H. Duncan, A. G. Calder,
G. Holtrop, P. Louis, G. E. Lobley, and H. J. Flint,Appl. Environ. Microbiol.72, 3593 (2006).
- Falonyet al.[2006]G. Falony, A. Vlachou,
K. Verbrugghe, and L. D. Vuyst,Appl. Environ. Microbiol.72, 7835 (2006).
- Louis and Flint [2016]P. Louis and H. J. Flint,Environ. Microbiol.19, 29 (2016).
- den Bestenet al.[2013]G. den
Besten, K. van Eunen,
A. K. Groen, K. Venema, D.-J. Reijngoud, and B. M. Bakker,J. Lipid Res.54, 2325 (2013).
- Iebbaet al.[2013]V. Iebba, F. Santangelo,
V. Totino, M. Nicoletti, A. Gagliardi, R. V. D. Biase, S. Cucchiara, L. Nencioni, M. P. Conte, and S. Schippa,PLoS ONE8, e61608 (2013).
- Riley and Wertz [2002]M. A. Riley and J. E. Wertz,Annu. Rev. Microbiol.56, 117 (2002).
- Wahlströmet al.[2016]A. Wahlström, S. Sayin,
H.-U. Marschall, and F. Bäckhed,Cell Metab.24, 41 (2016).
- Steinet al.[2013]R. R. Stein, V. Bucci,
N. C. Toussaint, C. G. Buffie, G. Rätsch, E. G. Pamer, C. Sander, and J. B. Xavier,PLoS Comput. Biol.9, e1003388 (2013).
- Bucci and Xavier [2014]V. Bucci and J. B. Xavier,J. Mol. Biol.426, 3907 (2014).
- Coyteet al.[2015]K. Z. Coyte, J. Schluter, and K. R. Foster,Science350, 663 (2015).
- Goyal and Maslov [2018]A. Goyal and S. Maslov, Phys. Rev. Lett.120,10.1103/physrevlett.120.158102(2018).
- Goyalet al.[2018]A. Goyal, V. Dubinkina, and S. Maslov,ISME J.12, 2823 (2018).
- Neubert and Caswell [1997]M. G. Neubert and H. Caswell,Ecology78, 653 (1997).
- Nisbet and Gurney [1976]R. M. Nisbet and W. S. C. Gurney,Nature263, 319 (1976).
- McKane and Newman [2005]A. J. McKane and T. J. Newman,Physical Review Letters94, 218102 (2005).
- Nicolettiet al.[2018]S. Nicoletti, N. Zagli,
D. Fanelli, R. Livi, T. Carletti, and G. Innocenti,Physical Review E98, 032214 (2018).
- Muoloet al.[2019b]R. Muolo, M. Asllani,
D. Fanelli, P. K. Maini, and T. Carletti,Journal of Theoretical Biology480, 81 (2019b).
- Biancalaniet al.[2017]T. Biancalani, F. Jafarpour, and N. Goldenfeld,Physical Review Letters118, 018101 (2017).
- Poggialiniet al.[2025]A. Poggialini, S. D. Santo, P. Villegas,
A. Gabrielli, and M. A. M. noz, arXiv preprint arXiv:2507.1912710.48550/arXiv.2507.19127(2025).
- Hennequinet al.[2014]G. Hennequin, T. P. Vogels, and W. Gerstner, Neuron82, 1394
(2014).
- Murphy and Miller [2009]B. K. Murphy and K. D. Miller, Neuron61, 635
(2009).
- Ganguliet al.[2008]S. Ganguli, D. Huh, and H. Sompolinsky, Proceedings of the
National Academy of Sciences105, 18970 (2008).
- Kurokawaet al.[2026]R. Kurokawa, R. Maskawa,
M. Arakawa, H. Masuoka, H. Takayasu, Y. Yoshikawa, T. Raihan, C. Shindo, K. Kaida, M. Takagi, M. Tanokura, L. Takayasu, M. Takayasu, and W. Suda, bioRxiv10.64898/2026.03.26.714232(2026), preprint, under review at Microbiome (2026).
- Theileret al.[1992]J. Theiler, S. Eubank,
A. Longtin, B. Galdrikian, and J. D. Farmer,Physica D58, 77 (1992).
- Schreiber and Schmitz [1996]T. Schreiber and A. Schmitz,Phys. Rev. Lett.77, 635 (1996).
- Schreiber and Schmitz [2000]T. Schreiber and A. Schmitz,Physica D142, 346 (2000).
- Lancasteret al.[2018]G. Lancaster, D. Iatsenko,
A. Pidde, V. Ticcinelli, and A. Stefanovska,Phys. Rep.748, 1 (2018).
- Carmodyet al.[2015]R. Carmody, G. Gerber,
J. Luevano, D. Gatti, L. Somes, K. Svenson, and P. Turnbaugh,Cell Host Microbe17, 72 (2015).
- Friswellet al.[2010]M. K. Friswell, H. Gika,
I. J. Stratford, G. Theodoridis, B. Telfer, I. D. Wilson, and A. J. McBain,PLoS ONE5, e8584 (2010).
- Davidet al.[2013]L. A. David, C. F. Maurice,
R. N. Carmody, D. B. Gootenberg, J. E. Button, B. E. Wolfe, A. V. Ling, A. S. Devlin, Y. Varma, M. A. Fischbach, S. B. Biddinger, R. J. Dutton, and P. J. Turnbaugh,Nature505, 559 (2013).
- Seifert [2012]U. Seifert, Reports on Progress in Physics75, 126001 (2012).
- Gnesottoet al.[2018]F. S. Gnesotto, F. Mura,
J. Gladrow, and C. P. Broedersz, Reports on Progress in Physics81, 066601 (2018).
- Fyodorovet al.[2025]Y. V. Fyodorov, E. Gudowska-Nowak, M. A. Nowak, and W. Tarnowski,Phys. Rev. Lett.134, 087102 (2025).
- Johanssonet al.[2008]M. E. V. Johansson, M. Phillipson, J. Petersson, A. Velcich,
L. Holm, and G. C. Hansson,Proc. Natl. Acad. Sci. USA105, 15064 (2008).
- Johansson and Hansson [2013]M. E. Johansson and G. C. Hansson,Dig. Dis.31, 305 (2013).
- Koremet al.[2015]T. Korem, D. Zeevi,
J. Suez, A. Weinberger, T. Avnit-Sagi, M. Pompan-Lotan, E. Matot, G. Jona, A. Harmelin, N. Cohen,
A. Sirota-Madi, C. A. Thaiss, M. Pevsner-Fischer, R. Sorek, R. J. Xavier, E. Elinav, and E. Segal,Science349, 1101 (2015).
- Brownet al.[2016]C. T. Brown, M. R. Olm,
B. C. Thomas, and J. F. Banfield,Nat. Biotechnol.34, 1256 (2016).
- Marchettiet al.[2013]M. C. Marchetti, J. F. Joanny, S. Ramaswamy,
T. B. Liverpool, J. Prost, M. Rao, and R. A. Simha,Reviews of Modern Physics85, 1143 (2013).
- Ramaswamy [2010]S. Ramaswamy,Annual Review of Condensed Matter Physics1, 323 (2010).
- Toner and Tu [1995]J. Toner and Y. Tu,Physical Review Letters75, 4326 (1995).
- Cates and Tailleur [2015]M. E. Cates and J. Tailleur,Annual Review of Condensed Matter Physics6, 219 (2015).
- Fodoret al.[2016]É. Fodor, C. Nardini,
M. E. Cates, J. Tailleur, P. Visco, and F. van Wijland,Physical Review Letters117, 038103 (2016).
- Farrell and Ioannou [2003]B. F. Farrell and P. J. Ioannou,Journal of the Atmospheric Sciences60, 2101 (2003).
- Buzsáki and Draguhn [2004]G. Buzsáki and A. Draguhn,Science304, 1926 (2004).
- Buzsáki and Moser [2013]G. Buzsáki and E. I. Moser,Nat. Neurosci.16, 130 (2013).
- Mukherjiet al.[2013]A. Mukherji, A. Kobiita,
T. Ye, and P. Chambon,Cell153, 812
(2013).
- Heddeset al.[2022]M. Heddes, B. Altaha,
Y. Niu, S. Reitmeier, K. Kleigrewe, D. Haller, and S. Kiessling, Nat. Commun.13,10.1038/s41467-022-33609-x(2022).
- Kuanget al.[2019]Z. Kuang, Y. Wang,
Y. Li, C. Ye, K. A. Ruhn, C. L. Behrendt, E. N. Olson, and L. V. Hooper,Science365, 1428 (2019).
- Reitmeieret al.[2020]S. Reitmeier, S. Kiessling, T. Clavel,
M. List, E. L. Almeida, T. S. Ghosh, K. Neuhaus, H. Grallert, J. Linseisen, T. Skurk, B. Brandl, T. A. Breuninger, M. Troll, W. Rathmann, B. Linkohr, H. Hauner, M. Laudes, A. Franke, C. I. L. Roy, J. T. Bell, T. Spector,
J. Baumbach, P. W. O’Toole, A. Peters, and D. Haller,Cell Host Microbe28, 258 (2020).
- Tuganbaevet al.[2020]T. Tuganbaev, U. Mor,
S. Bashiardes, T. Liwinski, S. P. Nobs, A. Leshem, M. Dori-Bachash, C. A. Thaiss, E. Y. Pinker, K. Ratiner, L. Adlung,
S. Federici, C. Kleimeyer, C. Moresi, T. Yamada, Y. Cohen, X. Zhang, H. Massalha, E. Massasa, Y. Kuperman, P. A. Koni, A. Harmelin, N. Gao,
S. Itzkovitz, K. Honda, H. Shapiro, and E. Elinav,Cell182, 1441 (2020).
- Voigtet al.[2014]R. M. Voigt, C. B. Forsyth,
S. J. Green, E. Mutlu, P. Engen, M. H. Vitaterna, F. W. Turek, and A. Keshavarzian,PLoS ONE9, e97500 (2014).
- Deaveret al.[2018]J. A. Deaver, S. Y. Eum, and M. Toborek, Front. Microbiol.9,10.3389/fmicb.2018.00737(2018).
- Altahaet al.[2022]B. Altaha, M. Heddes,
V. Pilorz, Y. Niu, E. Gorbunova, M. Gigl, K. Kleigrewe, H. Oster, D. Haller, and S. Kiessling,Mol. Metab.66, 101628 (2022).
- Thaisset al.[2016]C. A. Thaiss, M. Levy,
T. Korem, L. Dohnalová, H. Shapiro, D. A. Jaitin, E. David, D. R. Winter, M. Gury-BenAri, E. Tatirovsky, T. Tuganbaev, S. Federici,
N. Zmora, D. Zeevi, M. Dori-Bachash, M. Pevsner-Fischer, E. Kartvelishvily, A. Brandis, A. Harmelin, O. Shibolet, Z. Halpern, K. Honda, I. Amit, E. Segal, and E. Elinav,Cell167, 1495 (2016).
- Pauloseet al.[2016]J. K. Paulose, J. M. Wright,
A. G. Patel, and V. M. Cassone,PLoS ONE11, e0146643 (2016).
- Bishehsariet al.[2020]F. Bishehsari, R. M. Voigt, and A. Keshavarzian,Nat. Rev. Endocrinol.16, 731 (2020).
- Teichmanet al.[2020]E. M. Teichman, K. J. O’Riordan, C. G. Gahan, T. G. Dinan, and J. F. Cryan,Cell Metab.31, 448 (2020).
- Voigtet al.[2016]R. Voigt, C. Forsyth,
S. Green, P. Engen, and A. Keshavarzian,Int. Rev. Neurobiol. , 193 (2016).
- Chaumeilet al.[2019]P.-A. Chaumeil, A. J. Mussig, P. Hugenholtz, and D. H. Parks,Bioinformatics36, 1925 (2019).

## Appendix ASupplementary Material
No persistent circadian oscillator at genome resolution:
pseudo-coherence in gut microbiome dynamics

This Supplementary Material provides the full per-MAG mode-loading tables, the genus-level aggregation, the multiple-comparison-corrected surrogate results, and the mode-concentration statistics referenced in the main text. All loadings are mean absolute components of the unit-norm reaction (r^\hat{r}) and non-normal (n^\hat{n}) modes over the calibration windows of Mouse A (118 cyc7plus-labelled MAGs, 241 windows of lengthL=3L=3). Signs of the modes are calibration gauges and are not reported.

## A.1Top reaction-mode loadings (Mouse A)Table S1:Top-25 MAGs by mean absolute reaction-mode loading⟨|ri|⟩t\langle|r_{i}|\rangle_{t}(which genomes absorb the amplified excursion). Cluster labels are the cyc7plus assignment of Maskawa et al.Rank⟨|ri|⟩t\langle|r_{i}|\rangle_{t}ClusterGenusFamily10.1082MGBC157735Pumilibacteraceae20.1042SporofaciensLachnospiraceae30.1022PseudobutyricicoccusButyricicoccaceae40.0992SporofaciensLachnospiraceae50.0992UBA7109Lachnospiraceae60.0961FimisomaAnaerovoracaceae70.0952AvidehalobacterUBA575580.0932SporofaciensLachnospiraceae90.0921BacteroidesBacteroidaceae100.0901CAG-485Muribaculaceae110.0892CaccovicinusLachnospiraceae120.0891DuncaniellaMuribaculaceae130.0882MGBC131033Lachnospiraceae140.0871PrevotellaBacteroidaceae150.0871CAG-485Muribaculaceae160.0862UBA1405Ruminococcaceae170.0852Eubacterium_FLachnospiraceae180.0852UBA3402Lachnospiraceae190.0821BacteroidesBacteroidaceae200.0822UBA3402Lachnospiraceae210.0812DysosmobacterOscillospiraceae220.0792CAG-317Lachnospiraceae230.0792CoproplasmaBorkfalkiaceae240.0781EmergenciaAnaerovoracaceae250.0782CAG-95Lachnospiraceae

## A.2Top non-normal-mode loadings (Mouse A)Table S2:Top-25 MAGs by mean absolute non-normal-mode loading⟨|ni|⟩t\langle|n_{i}|\rangle_{t}(which genomes drive the amplified excursion).Rank⟨|ni|⟩t\langle|n_{i}|\rangle_{t}ClusterGenusFamily10.1221PrevotellaBacteroidaceae20.1202PseudobutyricicoccusButyricicoccaceae30.1181CAG-485Muribaculaceae40.1121FimisomaAnaerovoracaceae50.1112MGBC157735Pumilibacteraceae60.1082UBA1405Ruminococcaceae70.1071CAG-485Muribaculaceae80.1032UBA7109Lachnospiraceae90.1001DuncaniellaMuribaculaceae100.0942SporofaciensLachnospiraceae110.0941CAG-485Muribaculaceae120.0942SporofaciensLachnospiraceae130.0922CoproplasmaBorkfalkiaceae140.0922AvidehalobacterUBA5755150.0911AlistipesRikenellaceae160.0911BacteroidesBacteroidaceae170.0912CoproplasmaBorkfalkiaceae180.0872MGBC131033Lachnospiraceae190.0861BacteroidesBacteroidaceae200.0862UBA3402Lachnospiraceae210.0831CAG-873Muribaculaceae220.0832SporofaciensLachnospiraceae230.0821EmergenciaAnaerovoracaceae240.0821CAG-485Muribaculaceae250.0812PseudobutyricicoccusButyricicoccaceae

## A.3Genus-level aggregationTable S3:Top-15 genera by aggregated squared reaction-mode loading∑i|ri|2\sum_{i}|r_{i}|^{2}over their MAGs.RankGenus# MAGs∑i|ri|2\sum_{i}|r_{i}|^{2}Family1Sporofaciens50.0326Lachnospiraceae2CAG-48550.0283Muribaculaceae3COE160.0243Lachnospiraceae4UBA340240.0238Lachnospiraceae5Bacteroides40.0219Bacteroidaceae6Dysosmobacter50.0210Oscillospiraceae7Choladocola70.0208Lachnospiraceae8Pseudobutyricicoccus30.0198Butyricicoccaceae9CAG-87360.0189Muribaculaceae10Muribaculum60.0158Muribaculaceae11Coproplasma30.0150Borkfalkiaceae12UBA328260.0148Lachnospiraceae13Ligilactobacillus60.0137Lactobacillaceae14Duncaniella30.0136Muribaculaceae15CAG-9530.0128Lachnospiraceae

## A.4Mode concentration vs a random-unit-vector nullTable S4:Concentration of the unit-norm modes, time-averaged: cumulative energy (pi=ri2p_{i}=r_{i}^{2}) in the top-5/10/20 MAGs, and inverse participation ratioNeff=1/∑ipi2N_{\rm eff}=1/\sum_{i}p_{i}^{2}. A random unit vector inNNdimensions hasNeff≈N/3N_{\rm eff}\approx N/3. The empirical modes are about twice as concentrated as this null, on a few tens of MAGs across the two guilds.Mouse / modetop-5top-10top-20NeffN_{\rm eff}A (N=118N=118) random null24.3%39.0%59.1%40.7A reaction mode39.9%57.9%77.2%21.9A non-normal mode41.1%59.0%78.0%20.3B (N=181N=181) random null17.9%29.5%46.4%61.7B reaction mode33.8%48.9%66.7%29.0B non-normal mode33.3%48.2%66.0%28.9

## A.5Surrogate spectral test (Benjamini–Hochberg corrected)Table S5:Frequency bins exceeding the amplitude-adjusted Fourier surrogate null (Nsurr=250N_{\rm surr}=250) after Benjamini–Hochberg correction at FDR0.050.05, on the full record. Mouse A: no significant bin in either window. Mouse B (full record): significant in two bands; none survives after removing the first7272h.Mouse / windowsignificant bandperiodempiricalppBHppA, full & post-72hnone———B, full record0.0350.035–0.046​h−10.046\,\mathrm{h}^{-1}∼\sim22–28 h0.0040.033B, full record0.0100.010–0.013​h−10.013\,\mathrm{h}^{-1}∼\sim79–95 h0.0040.033B, post-72hnone———

## 


- 


Major funding support from
