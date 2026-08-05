# Inferring Non-Normal Amplification Geometry from Multivariate Time Series

**arXiv ID**: 2607.14786v1
**Authors**: V. R. Saiprasad, V. Troude, D. Sornette
**Published**: 2026-07-16
**Categories**: physics.data-an, cs.CG, nlin.CD
**Comments**: 35 pages, 17 figures
**HTML URL**: https://arxiv.org/html/2607.14786v1

## Abstract

Across hydrodynamics, ecology, neuroscience, network dynamics, non-Hermitian physics, and socio-economic systems, asymptotically stable dynamics can exhibit large transient amplifications that are invisible to eigenvalue-based analyses. The mechanism is geometric rather than spectral: perturbations entering along one direction may be expressed transiently along another, allowing asymptotic decay to coexist with strong transient or noise-driven amplification. We introduce non-normal directional response inference, a data-driven method for detecting this geometry from multivariate time series when the governing operator is unknown. A local linear operator is estimated from sliding windows and projected onto the dominant two-dimensional input-response subspace. The reduced dynamics are summarized by the eigenvalue splitting $Δ$, eigenvector non-orthogonality $K$, and the scale-free ratio $R=K/K_c(Δ)$, where $K_c(Δ)$ is the two-dimensional threshold for transient amplification. Controlled benchmarks show that the reduced geometry, particularly $R$, can be recovered from finite data even when the full high-dimensional operator is poorly estimated. Tests across sample size, dimension, training horizon, spectral structure, and non-stationarity confirm that the relevant response geometry requires far fewer observations than full-matrix recovery. Applied in moving windows to electrohysterogram, seizure EEG, freezing-of-gait, and unstable push-up inertial recordings, the method reveals systematic changes around known physiological or behavioral episodes through shifts in $R$, changes in $Δ$, or stronger projection of fluctuations onto the inferred response direction. It thus exposes interpretable changes in local response geometry without framing the problem as supervised event detection.

## Full Text

Inferring Non-Normal Amplification Geometry from Multivariate Time Series

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
- License: CC BY 4.0arXiv:2607.14786v1 [physics.data-an] 16 Jul 2026

## Inferring Non-Normal Amplification Geometry from Multivariate Time SeriesV.R. Saiprasad111These two authors contributed equally to this work.V. Troude222These two authors contributed equally to this work.D. Sornettedsornette@ethz.chInstitute of Risk Analysis, Prediction and Management (Risks-X),
Academy for Advanced Interdisciplinary Sciences,
Southern University of Science and Technology, Shenzhen, China

## Abstract

Across hydrodynamics, ecology, neuroscience, network dynamics, non-Hermitian physics, and socio-economic systems, asymptotically stable dynamics can nevertheless exhibit large transient amplifications that remain invisible to analyses based solely on the eigenvalue spectrum. The mechanism is geometric rather than spectral: perturbations entering along some directions can be transiently expressed along distinct response directions, allowing asymptotic decay to coexist with strong transient or noise-driven amplification.
We introduce non-normal directional response inference, a data-driven method for detecting this geometry from multivariate time series when the governing operator is unknown. The method estimates a local linear operator from sliding windows of the multivariate recording, projects it onto the dominant two-dimensional input-response subspace, and summarizes the reduced dynamics by three diagnostics: the reduced eigenvalue splittingΔ\Delta, the reduced eigenvector non-orthogonalityKK, and the scale-free ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta), whereKc​(Δ)K_{c}(\Delta)is the two-dimensional transient-amplification threshold.
Controlled benchmarks show that this reduced geometry, and in particularRR, can be recovered from finite data even when the entries of the full high-dimensional operator are poorly estimated. Tests across data quantity, dimension, training horizon, spectral structure, and non-stationarity confirm that the relevant response geometry remains identifiable with far fewer samples than full-matrix recovery would require. Applied in moving windows to electrohysterogram, seizure EEG, freezing-of-gait, and unstable push-up inertial recordings, the method reveals systematic changes in the reduced non-normal geometry around known physiological or behavioral episodes. These changes involve shifts inRR, changes inΔ\Delta, or increased projection of the observed fluctuations onto the inferred response direction.
These applications show that the method can expose interpretable changes in local response geometry associated with known events, without treating the problem as one of supervised event detection.

## keywords:non-normal dynamics , data-driven operator inference , dominant two-dimensional transient plane , input-response geometry , transient amplification , multivariate time series††journal:Communications in Nonlinear Science and Numerical Simulation

## 1Introduction

A stable system can still erupt. A linear system whose eigenvalues all predict decay of disturbances can nonetheless amplify
a perturbation by orders of magnitude before that decay
sets in, provided its eigenvectors are sufficiently non-orthogonal. This non-normal transient growth is classical in hydrodynamic stability[1,2,3]and has since been recognized as a generic route to large finite-time responses in ecology[4,5,6], neural circuits[7,8], directed and hierarchical networks[9,10,11,12], non-Hermitian physics[13], and socio-economic influence networks that form bubbles or crashes below any conventional critical threshold[14,15]. The unifying point is that the size of a finite-time event can be set by geometry, not by eigenvalues, and the early-warning signatures usually attributed to proximity to a bifurcation[16,17,18], including the still-debated critical slowing down before epileptic seizures[19,20], can also arise from a stable system with non-normal local dynamics[21,22].

The possible relevance of the non-normal mechanism shifts the empirical problem from estimating distance to an instability to identifying the local response geometry that can amplify perturbations while the system remains asymptotically stable. The difficulty is that this geometry is encoded in the local dynamical operator, which is rarely available in applications and must instead be inferred from multivariate observations. This is the typical situation in physiological and behavioral recordings, such as scalp electroencephalogram (EEG), inertial gait sensors, or multichannel electrohysterogram (EHG) signals[23,24,25]. For such data, eigenvalues estimated from a fitted local model may characterize asymptotic decay, but they do not reveal the input and response directions through which finite-time amplification occurs. Variance-based reductions face the complementary limitation: they may identify energetic modes of variability without recovering the directed coupling geometry that generates them. Existing data-driven modelling tools infer governing equations, interaction matrices, or latent dynamics[26,27,28,29], but they do not directly target the low-dimensional non-normal response geometry itself.
The question we address is therefore precise: from a multivariate time series alone, can one infer the dominant two-dimensional input–response plane of a locally stable system, and measure how close this plane lies to the threshold for transient amplification, even when the full operator is not reliably identifiable entry by entry? We show that the answer is yes. The reduced geometry remains identifiable across data quantity, dimension, training horizon, spectral structure, and non-stationarity.

We therefore develop non-normal directional response inference, a data-driven framework for extracting transient-amplification geometry from multivariate time series. The method estimates local linear dynamics from sliding windows of the data, identifies the dominant two-dimensional plane through which perturbations are received and transiently amplified, and reduces the resulting geometry to interpretable diagnostics.
We compare three ways of identifying this plane: an eigenbasis-SVD baseline (M1), an optimization-based search for directed input–response coupling (M2), and a commutator-based construction targeting non-normality directly (M3). The dynamics restricted to the selected plane are then summarized by the reduced eigenvalue splittingΔ\Delta, the reduced non-normality indexKK, and the scale-free ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta), which locates the inferred geometry below, at, or above the two-dimensional threshold for transient amplification.

The paper proceeds in two stages. First, controlled synthetic benchmarks establish whether the proposed framework can recover the dominant non-normal plane and the normalized reduced non-normality ratioRRfrom finite data. We test robustness across fixed non-normality parameter scans, sample size, system dimension, training horizon, broad spectral structure, and time-varying non-normality. Second, we apply the same moving-window procedure to four empirical settings, ordered by decreasing evidential strength: uterine EHG activity, seizure EEG, freezing-of-gait acceleration, and push-up inertial recordings. The purpose of these applications is not to build universal event detectors, but to ask whether known physiological or behavioral episodes are accompanied by interpretable changes in local response geometry. The central claim is that non-normal amplification geometry can be inferred from time series alone and can explain finite-time responses in locally stable high-dimensional systems.

## 2Motivation: stable systems can still amplify

Classical linear stability analysis describes the long-time fate of small perturbations. If all eigenvalues of a linearized continuous-time system lie in the stable half-plane, then perturbations eventually decay. This statement is correct, but it does not describe the full finite-time response. A stable non-normal system can first amplify selected perturbations before the eventual decay becomes visible.

A minimal example is the two-dimensional system𝒙˙=Aα​𝒙,Aα=(−1α0−2),α>0.\dot{\bm{x}}=A_{\alpha}\bm{x},\qquad A_{\alpha}=\begin{pmatrix}-1&\alpha\\
0&-2\end{pmatrix},\qquad\alpha>0.(1)

The eigenvalues ofAαA_{\alpha}are−1-1and−2-2, independently ofα\alpha. Thus the system is asymptotically stable for every value of the coupling parameterα\alpha. The matrix is diagonalizable because the two eigenvalues are distinct, so the transient amplification discussed below does not rely on a defective matrix or on eigenvalue degeneracy. The matrix is nevertheless non-normal forα≠0\alpha\neq 0, sinceAα​Aα⊤≠Aα⊤​Aα.A_{\alpha}A_{\alpha}^{\top}\neq A_{\alpha}^{\top}A_{\alpha}.(2)

The off-diagonal termα\alphacreates a directional coupling between two stable modes.

For the simple initial condition𝒙​(0)=(01),\bm{x}(0)=\begin{pmatrix}0\\
1\end{pmatrix},(3)

the solution isx1​(t)=α​(e−t−e−2​t)x2​(t)=e−2​t.x_{1}(t)=\alpha\left(e^{-t}-e^{-2t}\right)\qquad x_{2}(t)=e^{-2t}~.(4)

The second component decays monotonically, but during its decay it feeds the first component.
The responsex1​(t)x_{1}(t)first grows asx1​(t)=α​(t−3​t22+𝒪​(t3))x_{1}(t)=\alpha\left(t-{3t^{2}\over 2}+{\cal O}(t^{3})\right)at short times, reaches its maximum att∗=log⁡2,x1​(t∗)=α4,t_{*}=\log 2,\qquad x_{1}(t_{*})=\frac{\alpha}{4},(5)

and then decays to zero. Thus the transient response can be increased by increasing the non-normal couplingα\alpha, without moving either eigenvalue toward instability. The initial condition in (3) is chosen to make the algebra transparent; the same qualitative behavior occurs for a generic starting point, as the phase portrait infig.1illustrates.

This example separates two notions that are often conflated. Spectral stability controls the long-time decay rate. Non-normal geometry controls the finite-time path taken by the perturbation before that decay is observed. In the notation used below, the spectral part of the reduced dynamics is summarized by the reduced eigenvalue splittingΔ\Delta, while the geometric part is summarized by the reduced non-normality indexKK. These are the two fundamental contributors to finite-time amplification considered in this paper. Other observable effects sometimes discussed separately, such as one-step singular-vector gain, near-rank-one channel focusing, or cumulative finite-time response, are consequences of these two ingredients rather than independent amplification mechanisms. Their combination is reported through the normalized reduced non-normality ratioR=K/Kc​(Δ),R=K/K_{c}(\Delta),

whereKc​(Δ)K_{c}(\Delta)is the reduced threshold obtained from the two-dimensional real-eigenvalue calculation. The parameterRRis therefore a reduced diagnostic:R<1R<1means below the reduced threshold,R=1R=1means at the reduced threshold, andR>1R>1means above the reduced threshold.

The relevant directions are not necessarily eigenvectors. One direction acts as an input direction, denoted by𝒏^\widehat{\bm{n}}, while the induced response is expressed along a response direction, denoted by𝒓^\widehat{\bm{r}}. In the example above, perturbations initialized with a component in the second coordinate can generate a transient response in the first coordinate before both components decay.Agives the corresponding discrete-time calculation for a canonical2×22\times 2non-normal matrix. That calculation gives the thresholdKc​(Δ)K_{c}(\Delta)used later to normalize the reduced non-normality indexKK.

The same mechanism also appears under stochastic forcing. Consider𝒙˙=Aα​𝒙+σ​𝝃​(t),\dot{\bm{x}}=A_{\alpha}\bm{x}+\sigma\bm{\xi}(t),(6)

where𝝃​(t)\bm{\xi}(t)denotes temporally uncorrelated forcing andσ\sigmasets the forcing amplitude. Although the deterministic system is stable, repeated perturbations can be projected onto directions that undergo transient amplification. The resulting time series can therefore contain intermittent bursts whose dominant component is aligned with the response direction. A normal system with the same eigenvalues does not have the same finite-time input–response geometry.Figure 1:Finite-time amplification in a stable non-normal system.The non-normal system is𝒙˙=Ann​𝒙\dot{\bm{x}}=A_{\rm nn}\bm{x}, withAnn=(−1100−2)A_{\rm nn}=\begin{pmatrix}-1&10\\
0&-2\end{pmatrix}.
The normal comparison is𝒙˙=Anormal​𝒙\dot{\bm{x}}=A_{\rm normal}\bm{x}, withAnormal=(−100−2)A_{\rm normal}=\begin{pmatrix}-1&0\\
0&-2\end{pmatrix}.
Both matrices have eigenvalues−1-1and−2-2.(a)Phase-space trajectories from the initial condition𝒙​(0)=(0.70,0.92)⊤\bm{x}(0)=(0.70,0.92)^{\top}. The grey streamlines show the vector field of the non-normal system. The solid red curve is the non-normal trajectory and the dotted blue curve is the normal trajectory. The magenta arrows show the slow and fast eigendirections ofAnnA_{\rm nn}. The directions𝒏^\widehat{\bm{n}}and𝒓^\widehat{\bm{r}}indicate the input and response directions used schematically in the reduced description.(b)Deterministic time series of the Euclidean norm‖𝒙​(t)‖2\|\bm{x}(t)\|_{2}for the same two systems and the same initial condition as in panel (a). The red marker denotes the maximum of the non-normal norm.(c)Stochastically forced trajectories generated from𝒙˙=A​𝒙+σ​𝝃​(t)\dot{\bm{x}}=A\bm{x}+\sigma\bm{\xi}(t), withσ=0.55\sigma=0.55, time stepd​t=0.01dt=0.01, and the same noise realization for the normal and non-normal systems. The blue dotted curve is‖𝒙​(t)‖2\|\bm{x}(t)\|_{2}for the normal system, the red curve is‖𝒙​(t)‖2\|\bm{x}(t)\|_{2}for the non-normal system, and the black dashed curve is the projection|𝒓^⊤​𝒙​(t)||\widehat{\bm{r}}^{\top}\bm{x}(t)|, where𝒓^\widehat{\bm{r}}is the direction of the largest non-normal burst in the plotted stochastic trajectory.

Figure1illustrates the same distinction in phase space, deterministic time series, and stochastically forced time series. Panel (a) shows that the non-normal trajectory can move away from the stable fixed point before returning to it, whereas the normal comparison decays directly. Panel (b) shows the corresponding transient increase in‖𝒙​(t)‖2\|\bm{x}(t)\|_{2}for the non-normal system. Panel (c) shows that, under repeated forcing, the largest bursts in the non-normal system are concentrated along a response direction. These observations motivate the inference problem studied in this paper.

In empirical systems, the local operator is unknown, the state dimension can be high, and the amplification mechanism may be concentrated in a low-dimensional subspace. Eigenvalues alone do not identify the directions responsible for transient growth. Variance-based reductions also need not recover the directional coupling that produces amplification. The problem is therefore not only to estimate a stable operator from data, but also to infer the low-dimensional geometry through which stable dynamics can produce large finite-time or noise-driven responses.

The framework developed below follows this logic. From multivariate time series, we estimate a local linear operator, extract a two-dimensional non-normal response plane, and project the fitted dynamics onto that plane. The reduced operator is then used to compute the reduced eigenvalue splittingΔ\Delta, the reduced non-normality indexKK, and the normalized reduced non-normality ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta). This provides a data-driven route from observed fluctuations to the reduced geometry that organizes them.

## 3Data-driven inference of reduced non-normal geometry

## 3.1The inference problem: recovering a reduced non-normal response geometry

The preceding example shows that a stable linear system can exhibit large transient amplification when its eigenvectors are non-orthogonal. We now formulate the corresponding inference problem for data. Stated compactly, the problem is the following.

Input.A multivariate time series{𝒙k}k=1T\{\bm{x}_{k}\}_{k=1}^{T},𝒙k∈ℝN\bm{x}_{k}\in\mathbb{R}^{N}, sampled from a locally stable high-dimensional system whose generating operator is unknown.

Step 1 (fit).Estimate a one-step linear operatorF^\widehat{F}from the data in the current window using ridge regression (11).

Step 2 (reduce).Extract a two-dimensional orthonormal input–response planeQ=[𝒓^,𝒏^]∈ℝN×2Q=[\widehat{\bm{r}},\widehat{\bm{n}}]\in\mathbb{R}^{N\times 2}, with input direction𝒏^\widehat{\bm{n}}and response direction𝒓^\widehat{\bm{r}}, and project the fitted operator onto it,𝚪=Q⊤​𝑭^​Q∈ℝ2×2\bm{\Gamma}=Q^{\top}\widehat{\bm{F}}Q\in\mathbb{R}^{2\times 2}.

Output.Three scalar diagnostics of𝚪\bm{\Gamma}: the reduced eigenvalue splittingΔ\Delta, the reduced eigenvector non-orthogonalityKK, and the normalized reduced non-normality ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta), whereKc​(Δ)K_{c}(\Delta)is the two-dimensional transient-amplification threshold (A). The valuesR<1R<1,R=1R=1,R>1R>1place the inferred geometry below, at, or above that threshold.

The target of inference is this two-dimensional geometry, not entrywise recovery of the fullN×NN\times Noperator. The synthetic benchmarks ofsection5establish that the geometry is recoverable even when the full operator is not.Figure 2:Schematic of the inference workflow.A multivariate time series{𝒙k}\{\bm{x}_{k}\}is used to estimate a local one-step linear operator𝑭^\widehat{\bm{F}}. A two-dimensional orthonormal basisQ=[𝒓^,𝒏^]Q=[\widehat{\bm{r}},\widehat{\bm{n}}]is then extracted using one of the methods introduced insection4. The fitted operator is projected onto this plane to obtain the reduced matrix𝚪=Q⊤​𝑭^​Q\bm{\Gamma}=Q^{\top}\widehat{\bm{F}}Q. The scalar diagnostics computed from𝚪\bm{\Gamma}are the reduced eigenvalue splittingΔ\Delta, the two-dimensional eigenvector-conditioning measureκ2​D\kappa_{2D}, the reduced non-normality indexKK, and the normalized reduced non-normality ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta). HereKc​(Δ)K_{c}(\Delta)denotes the reduced threshold for transient amplification in the two-dimensional real-eigenvalue model.

## 3.2Observation model and local linear fit

Let𝒙​(t)∈ℝN\bm{x}(t)\in\mathbb{R}^{N}denote the observed state of a high-dimensional system. Over a finite observation window, we approximate the local dynamics by a stable linear system with additive stochastic forcing. In continuous time, this local model is written as𝒙˙​(t)=A​𝒙​(t)+2​δ​𝝃​(t),𝝃​(t)∼𝒩​(0,IN),\dot{\bm{x}}(t)=A\bm{x}(t)+\sqrt{2\delta}\,\bm{\xi}(t),\qquad\bm{\xi}(t)\sim\mathcal{N}(0,I_{N}),(7)

whereA∈ℝN×NA\in\mathbb{R}^{N\times N}is a stable local generator,INI_{N}is theN×NN\times Nidentity matrix, andδ>0\delta>0is the forcing intensity. For uniformly sampled data, and for the synthetic benchmarks used below, we use the discrete-time VAR(1) approximation𝒙k+1=F​𝒙k+𝜼k,𝜼k∼𝒩​(0,σ2​IN),ρ​(F)<1,\bm{x}_{k+1}=F\bm{x}_{k}+\bm{\eta}_{k},\qquad\bm{\eta}_{k}\sim\mathcal{N}(0,\sigma^{2}I_{N}),\qquad\rho(F)<1,(8)

whereF∈ℝN×NF\in\mathbb{R}^{N\times N}is the one-step linear map andρ​(F)\rho(F)denotes its spectral radius. When a continuous-time interpretation is appropriate and the sampling intervalΔ​t\Delta tis small, the two descriptions are formally related byF≈eA​Δ​t,A≈Δ​t−1​log⁡(F).F\approx e^{A\Delta t},\qquad A\approx\Delta t^{-1}\log(F).(9)

Given a uniformly sampled trajectory{𝒙k}k=1T\{\bm{x}_{k}\}_{k=1}^{T}, defineX=[𝒙1𝒙2⋯𝒙T−1],Y=[𝒙2𝒙3⋯𝒙T].X=\begin{bmatrix}\bm{x}_{1}&\bm{x}_{2}&\cdots&\bm{x}_{T-1}\end{bmatrix},\qquad Y=\begin{bmatrix}\bm{x}_{2}&\bm{x}_{3}&\cdots&\bm{x}_{T}\end{bmatrix}.(10)

The fitted one-step map is obtained by ridge regression,𝑭^​(λ)=Y​X⊤​(X​X⊤+λ​IN)−1,λ>0.\widehat{\bm{F}}(\lambda)=YX^{\top}\left(XX^{\top}+\lambda I_{N}\right)^{-1},\qquad\lambda>0.(11)

For multiple independent trajectories generated under the same operator, the correspondingXXandYYmatrices are concatenated columnwise before applying
(11). In the synthetic benchmarks,MMdenotes the number
of such independent training trajectories, andTtrainT_{\mathrm{train}}denotes
the number of time samples in each trajectory. Thus,M>1M>1is used only in
controlled simulations where repeated trajectories from the same known operator
can be generated. In empirical recordings, one usually observes a single long
time series rather than repeated independent realizations of the same local
dynamics. We therefore setM=1M=1for each empirical window and estimate a
separate window-dependent operator from the consecutive sample pairs inside
that window. When several comparable events are available, such as multiple
seizures, freezing episodes, contractions, or repeated movement bursts, they are
used to assess repeatability of the diagnostics across events or recordings.
They are not treated as independent trajectories for a single fitted operator
unless an explicit pooling assumption is stated.

The regularization parameterλ\lambdacontrols the finite-sample bias–variance tradeoff. In synthetic benchmarks, it is selected using predictive accuracy and stability of the fitted map. In empirical moving-window analyses, additional mild stabilization or screening is applied when the local regression problem is poorly conditioned. These empirical safeguards are described insection6, because they depend on the dataset and are not part of the mathematical definition of the reduced diagnostics.

## 3.3Target of inference

The goal is not to recover every entry of the full operator with equal accuracy. Instead, the goal is to identify the low-dimensional geometry that organizes the dominant transient response. We therefore seek a two-dimensional orthonormal basisQ=[𝒓^𝒏^]∈ℝN×2,Q⊤​Q=I2.Q=\begin{bmatrix}\widehat{\bm{r}}&\widehat{\bm{n}}\end{bmatrix}\in\mathbb{R}^{N\times 2},\qquad Q^{\top}Q=I_{2}.(12)

Here𝒏^\widehat{\bm{n}}denotes the inferred input direction in which perturbations or fluctuations are most susceptible to transient amplification, while𝒓^\widehat{\bm{r}}denotes the associated response direction. The interpretation is that a component along𝒏^\widehat{\bm{n}}is preferentially mapped by the fitted dynamics into the direction𝒓^\widehat{\bm{r}}.

OnceQQhas been identified, the fitted operator is projected onto this plane:𝚪=Q⊤​𝑭^​Q∈ℝ2×2.\bm{\Gamma}=Q^{\top}\widehat{\bm{F}}Q\in\mathbb{R}^{2\times 2}.(13)

All reduced diagnostics are computed from the same2×22\times 2matrix𝚪\bm{\Gamma}, regardless of how the planeQQwas extracted. This common projection step makes it possible to compare different plane-extraction methods using the same reduced operator.

## 3.4Reduced diagnostics

Letλ1,λ2\lambda_{1},\lambda_{2}denote the eigenvalues of the reduced operator𝚪\bm{\Gamma}. We first define the normalized reduced eigenvalue splittingΔ=|λ1−λ2λ1+λ2|.\Delta=\left|\frac{\lambda_{1}-\lambda_{2}}{\lambda_{1}+\lambda_{2}}\right|.(14)

The quantityΔ\Deltameasures the separation of the two reduced eigenvalues relative to their mean scale. SmallΔ\Deltacorresponds to a nearly degenerate reduced spectrum, whereas larger values indicate more separated reduced eigenvalues.

Let𝒑1,𝒑2\bm{p}_{1},\bm{p}_{2}be normalized right eigenvectors of𝚪\bm{\Gamma}. Their non-orthogonality is measured byκ2​D=1+|⟨𝒑1,𝒑2⟩|1−|⟨𝒑1,𝒑2⟩|.\kappa_{2D}=\sqrt{\frac{1+\left|\left\langle\bm{p}_{1},\bm{p}_{2}\right\rangle\right|}{1-\left|\left\langle\bm{p}_{1},\bm{p}_{2}\right\rangle\right|}}.(15)

For an orthogonal reduced eigenbasis,κ2​D=1\kappa_{2D}=1. As the two reduced eigenvectors become nearly parallel,κ2​D\kappa_{2D}increases.

We then define the reduced non-normality indexK=κ2​D−κ2​D−12.K=\frac{\kappa_{2D}-\kappa_{2D}^{-1}}{2}.(16)

This scalar is zero for an orthogonal reduced eigenbasis and increases with the non-orthogonality of the two reduced eigenvectors. It therefore measures the geometric component of transient amplification inside the inferred two-dimensional plane.

The reduced thresholdKc​(Δ)K_{c}(\Delta)is obtained from the two-dimensional real-eigenvalue calculation summarized inA. In this setting,Kc​(Δ)=[1−Δ21−1−Δ2]1/2,0≤Δ<1.K_{c}(\Delta)=\left[\frac{\sqrt{1-\Delta^{2}}}{1-\sqrt{1-\Delta^{2}}}\right]^{1/2},\qquad 0\leq\Delta<1.(17)

We compare the measured reduced non-normalityKKwith this threshold through the normalized reduced non-normality ratioR=KKc​(Δ).R=\frac{K}{K_{c}(\Delta)}.(18)

The parameterRRshould be interpreted as a reduced diagnostic. ValuesR<1R<1indicate that the reduced geometry lies below the two-dimensional transient-amplification threshold defined by (17). ValuesR=1R=1correspond to that reduced threshold, and valuesR>1R>1indicate that the reduced geometry lies above it. ThusRRcontrols whether the inferred two-dimensional dynamics are below or above the reduced threshold;RRitself is not the phenomenon of criticality. The threshold in (17) is specific to the two-dimensional real-eigenvalue reduction and should not be interpreted as a universal stability boundary for the fullNN-dimensional system.

## Conditioning of the operator versus conditioning of eigenvectors.

We distinguish four related but non-equivalent quantities. First, the matrix condition numberκ​(𝑭^)=σmax​(𝑭^)σmin​(𝑭^)\kappa(\widehat{\bm{F}})=\frac{\sigma_{\max}(\widehat{\bm{F}})}{\sigma_{\min}(\widehat{\bm{F}})}(19)

measures the spread of singular values of the fitted operator. It is sensitive to anisotropic gain and near-singularity, but it is not by itself a measure of eigenvector non-orthogonality. Second, if𝑭^​P=P​Λ,\widehat{\bm{F}}P=P\Lambda,(20)

thenκ​(P)=‖P‖2​‖P−1‖2\kappa(P)=\left\lVert P\right\rVert_{2}\left\lVert P^{-1}\right\rVert_{2}(21)

measures the conditioning of the eigenvector matrixPP. This quantity is tied to the non-orthogonality of the eigenvectors of the full fitted operator𝑭^\widehat{\bm{F}}. Third,κ2​D\kappa_{2D}in (15) measures the non-orthogonality of the eigenvectors of the reduced operator𝚪=Q⊤​𝑭^​Q\bm{\Gamma}=Q^{\top}\widehat{\bm{F}}Q. Fourth,KKin (16) is a scalar reparameterization ofκ2​D\kappa_{2D}used to compare the reduced geometry with the thresholdKc​(Δ)K_{c}(\Delta). Thusκ​(𝑭^)\kappa(\widehat{\bm{F}}),κ​(P)\kappa(P),κ2​D\kappa_{2D}, andKKare different objects and should not be interchanged.

## 3.5Validation metrics in synthetic data

When a known reference operatorFFis available, the inference can be evaluated at three levels. First, full-operator recovery is measured by the relative Frobenius errorrelErr​(𝑭^)=‖𝑭^−F‖F‖F‖F.\mathrm{relErr}(\widehat{\bm{F}})=\frac{\left\lVert\widehat{\bm{F}}-F\right\rVert_{F}}{\left\lVert F\right\rVert_{F}}.(22)

This diagnostic quantifies the accuracy of the high-dimensional regression problem.

Second, plane recovery is measured using the largest principal angle between the inferred planeQQand a reference planeQrefQ_{\mathrm{ref}}. We defineθ​(Q,Qref)=arccos⁡[σmin​(Q⊤​Qref)],\theta(Q,Q_{\mathrm{ref}})=\arccos\left[\sigma_{\min}\left(Q^{\top}Q_{\mathrm{ref}}\right)\right],(23)

whereσmin\sigma_{\min}denotes the smallest singular value. The matrixQ⊤​QrefQ^{\top}Q_{\mathrm{ref}}contains the inner products between the two orthonormal bases. Its singular values are the cosines of the principal angles between the two planes, so (23) reports the largest angular mismatch.

Third, mechanism-level recovery is assessed using the reduced diagnostics and observable correlations. For a scalar observable such as the mean fieldmk=1N​𝟏⊤​𝒙k,m_{k}=\frac{1}{N}\bm{1}^{\top}\bm{x}_{k},(24)

we use a plane-invariant correlation scorecplane=max‖𝒂‖=1⁡|corr​(mk,𝒂⊤​Q⊤​𝒙k)|.c_{\mathrm{plane}}=\max_{\left\lVert\bm{a}\right\rVert=1}\left|\mathrm{corr}\left(m_{k},\,\bm{a}^{\top}Q^{\top}\bm{x}_{k}\right)\right|.(25)

This score asks whether the inferred two-dimensional plane contains a direction whose activity is strongly related to the observable. Because the maximization is over all unit directions inside the plane, the score depends on the plane itself and not on an arbitrary choice of basis within the plane.

These three levels answer different questions. The operator error in (22) measures recovery of the fullN×NN\times Nmap. The principal angle in (23) measures recovery of the reduced response plane. The reduced diagnostics andcplanec_{\mathrm{plane}}measure whether that plane captures an amplification-related component visible in the data. This distinction is important because the reduced response plane can be recovered well even when the full operator is not recovered entry by entry.

## 3.6Use in empirical data

For empirical datasets, the reference operator and reference response plane are unavailable. We therefore do not reportrelErr​(𝑭^)\mathrm{relErr}(\widehat{\bm{F}})or reference principal-angle errors. Instead, the evidence is based on internal consistency and alignment with independently observed events: agreement between independent extraction methods, persistence of the reduced diagnostics across neighboring windows, alignment with event times or activity envelopes, and exclusion of degenerate reduced matrices.

In empirical data,R=K/Kc​(Δ)R=K/K_{c}(\Delta)should be read as a local reduced diagnostic of amplification-prone geometry. A rise inRRdoes not by itself prove causality or establish a universal event detector. Its interpretation depends on whether the rise is reproducible across neighboring windows, whether the optimization-based extraction (M2) and commutator-based extraction (M3) agree, whether the reduced eigenvalue splittingΔ\Deltaremains non-degenerate, and whether the inferred response direction is related to an observed signal. This conservative interpretation is used throughout the empirical demonstrations insection6.

## 4Plane-extraction methods

## 4.1Three methods for extracting the dominant two-dimensional response plane

The reduced diagnostics introduced insection3.4require a two-dimensional planeQ=[𝒓^,𝒏^]Q=[\widehat{\bm{r}},\widehat{\bm{n}}]on which the fitted operator𝑭^\widehat{\bm{F}}is projected. We compare three ways of extracting this plane from the same fitted operator. The first method,eigenbasis-SVD baseline extraction (M1), applies a singular-value decomposition (SVD) to the matrix of right eigenvectors ofF^\widehat{F}and uses the resulting dominant directions to define the reduced plane. The second method,optimization-based directed-coupling extraction (M2), searches directly for an orthonormal pair of directions with large transverse action under𝑭^\widehat{\bm{F}}. The third method,commutator-based plane extraction (M3), identifies a two-dimensional plane from the symmetric commutator of𝑭^\widehat{\bm{F}}.

For compactness, we refer to these methods as M1, M2, and M3 in figures and tables. Their full names areM1\displaystyle\mathrm{M1}:eigenbasis-SVD baseline extraction,\displaystyle:\quad\text{eigenbasis-SVD baseline extraction},M2\displaystyle\mathrm{M2}:optimization-based directed-coupling extraction,\displaystyle:\quad\text{optimization-based directed-coupling extraction},M3\displaystyle\mathrm{M3}:commutator-based plane extraction.\displaystyle:\quad\text{commutator-based plane extraction}.

Each method takes𝑭^\widehat{\bm{F}}as input and returns either an ordered orthonormal pairQ=[𝒓^,𝒏^]∈ℝN×2,Q⊤​Q=I2,Q=[\widehat{\bm{r}},\widehat{\bm{n}}]\in\mathbb{R}^{N\times 2},\qquad Q^{\top}Q=I_{2},

or, in the case of M3, a two-dimensional plane that is subsequently ordered into the pair(𝒓^,𝒏^)(\widehat{\bm{r}},\widehat{\bm{n}})when an input–response interpretation is needed. In all cases, the reported reduced operator is𝚪=Q⊤​𝑭^​Q,\bm{\Gamma}=Q^{\top}\widehat{\bm{F}}Q,

and the diagnosticsΔ\Delta,κ2​D\kappa_{2D},KK, andR=K/Kc​(Δ)R=K/K_{c}(\Delta)are computed from𝚪\bm{\Gamma}as defined insection3.4. Thus the three methods differ only in how the planeQQis extracted; the final projection and diagnostic definitions are the same.

## 4.2Method 1: eigenbasis-SVD baseline extraction (M1)

The eigenbasis-SVD baseline extraction (M1) provides a reference construction based on the eigenspace geometry of the fitted operator. Starting from𝑭^\widehat{\bm{F}}, we compute a numerical eigendecomposition𝑭^​P=P​Λ,\widehat{\bm{F}}P=P\Lambda,(26)

where the columns ofPPare right eigenvectors andΛ\Lambdais the corresponding diagonal matrix of eigenvalues.

The conditioning of the eigenvector matrix is obtained from the singular value decompositionP=U​Σ​V⊤,Σ=diag​(σ1,…,σN),σ1≥⋯≥σN>0.P=U\Sigma V^{\top},\qquad\Sigma=\mathrm{diag}(\sigma_{1},\ldots,\sigma_{N}),\qquad\sigma_{1}\geq\cdots\geq\sigma_{N}>0.(27)

We defineκ​(P)=σ1σN,\kappa(P)=\frac{\sigma_{1}}{\sigma_{N}},(28)

which is equivalent to (21).
This quantity measures the conditioning of the eigenvector matrixPP. Largeκ​(P)\kappa(P)indicates that the eigenvectors of𝑭^\widehat{\bm{F}}are close to being linearly dependent. It is therefore a measure of eigenvector geometry. It is not the matrix condition numberκ​(𝑭^)=σmax​(𝑭^)σmin​(𝑭^),\kappa(\widehat{\bm{F}})=\frac{\sigma_{\max}(\widehat{\bm{F}})}{\sigma_{\min}(\widehat{\bm{F}})},

which measures the singular-value spread of the fitted operator itself.

In M1, the non-normal direction is taken to be the left singular vector ofPPassociated with its smallest singular value:𝒏^=U:,N.\widehat{\bm{n}}=U_{:,N}.(29)

The corresponding response direction is obtained by applying𝑭^\widehat{\bm{F}}to𝒏^\widehat{\bm{n}}and removing the component parallel to𝒏^\widehat{\bm{n}}:𝒓~=(IN−𝒏^​𝒏^⊤)​𝑭^​𝒏^,𝒓^=𝒓~‖𝒓~‖.\widetilde{\bm{r}}=\left(I_{N}-\widehat{\bm{n}}\widehat{\bm{n}}^{\top}\right)\widehat{\bm{F}}\widehat{\bm{n}},\qquad\widehat{\bm{r}}=\frac{\widetilde{\bm{r}}}{\left\lVert\widetilde{\bm{r}}\right\rVert}.(30)

The extracted basis and the reduced operator areQM1=[𝒓^,𝒏^],𝚪M1=QM1⊤​𝑭^​QM1.Q_{\mathrm{M1}}=[\widehat{\bm{r}},\widehat{\bm{n}}],\qquad\bm{\Gamma}_{\mathrm{M1}}=Q_{\mathrm{M1}}^{\top}\widehat{\bm{F}}Q_{\mathrm{M1}}.(31)

M1 is useful because it connects directly to the classical eigenvector picture of non-normality. Its limitation is that it relies on the eigendecomposition of𝑭^\widehat{\bm{F}}. When the fitted operator is noisy, nearly defective, or strongly non-normal, small perturbations in𝑭^\widehat{\bm{F}}can produce large changes in its eigenvectors. For this reason, M1 is used as a baseline rather than as the main estimator of the response plane.

## 4.3Method 2: optimization-based directed-coupling extraction (M2)

The optimization-based directed-coupling extraction (M2) estimates the input and response directions directly from the fitted operator, without using an eigendecomposition. The method searches for an orthonormal pair of directions for which the action of𝑭^\widehat{\bm{F}}maps one direction strongly into the other.

We define(𝒓^,𝒏^)(\widehat{\bm{r}},\widehat{\bm{n}})as a solution of(𝒓^,𝒏^)=arg⁡max‖𝒖‖=1,‖𝒗‖=1⟨𝒖,𝒗⟩=0⁡⟨𝒖,𝑭^​𝒗⟩.(\widehat{\bm{r}},\widehat{\bm{n}})=\arg\max_{\begin{subarray}{c}\left\lVert\bm{u}\right\rVert=1,\ \left\lVert\bm{v}\right\rVert=1\\
\left\langle\bm{u},\bm{v}\right\rangle=0\end{subarray}}\left\langle\bm{u},\widehat{\bm{F}}\bm{v}\right\rangle.(32)

Here𝒏^\widehat{\bm{n}}is the input direction and𝒓^\widehat{\bm{r}}is the response direction. The objective in (32) measures the component of𝑭^​𝒏^\widehat{\bm{F}}\widehat{\bm{n}}transverse to𝒏^\widehat{\bm{n}}and aligned with𝒓^\widehat{\bm{r}}.

A practical solver is alternating maximization with orthogonal projection. Given a current vector𝒗\bm{v}, the maximizing update for𝒖\bm{u}is𝒖←(IN−𝒗​𝒗⊤)​𝑭^​𝒗‖(IN−𝒗​𝒗⊤)​𝑭^​𝒗‖.\bm{u}\leftarrow\frac{(I_{N}-\bm{v}\bm{v}^{\top})\widehat{\bm{F}}\bm{v}}{\left\lVert(I_{N}-\bm{v}\bm{v}^{\top})\widehat{\bm{F}}\bm{v}\right\rVert}.(33)

Given a current vector𝒖\bm{u}, the corresponding update for𝒗\bm{v}is𝒗←(IN−𝒖​𝒖⊤)​𝑭^⊤​𝒖‖(IN−𝒖​𝒖⊤)​𝑭^⊤​𝒖‖.\bm{v}\leftarrow\frac{(I_{N}-\bm{u}\bm{u}^{\top})\widehat{\bm{F}}^{\top}\bm{u}}{\left\lVert(I_{N}-\bm{u}\bm{u}^{\top})\widehat{\bm{F}}^{\top}\bm{u}\right\rVert}.(34)

The updates are iterated until the objective in (32), or equivalently the extracted plane, changes by less than a prescribed numerical tolerance. Multiple initializations are used to reduce sensitivity to local optima.

After convergence, we impose a consistent response-direction convention. Once𝒏^\widehat{\bm{n}}has been identified, we set𝒓~=(IN−𝒏^​𝒏^⊤)​𝑭^​𝒏^,𝒓^=𝒓~‖𝒓~‖.\widetilde{\bm{r}}=(I_{N}-\widehat{\bm{n}}\widehat{\bm{n}}^{\top})\widehat{\bm{F}}\widehat{\bm{n}},\qquad\widehat{\bm{r}}=\frac{\widetilde{\bm{r}}}{\left\lVert\widetilde{\bm{r}}\right\rVert}.(35)

The basis and reduced operator are thenQM2=[𝒓^,𝒏^],𝚪M2=QM2⊤​𝑭^​QM2.Q_{\mathrm{M2}}=[\widehat{\bm{r}},\widehat{\bm{n}}],\qquad\bm{\Gamma}_{\mathrm{M2}}=Q_{\mathrm{M2}}^{\top}\widehat{\bm{F}}Q_{\mathrm{M2}}.(36)

M2 targets the directed amplification geometry directly. It does not require the eigenvectors of𝑭^\widehat{\bm{F}}, and therefore avoids one source of numerical instability present in M1. It also returns an ordered pair(𝒓^,𝒏^)(\widehat{\bm{r}},\widehat{\bm{n}}), which is useful in empirical data because the response direction can be compared with observable activity, event-aligned signals, or collective coordinates.

## 4.4Method 3: commutator-based plane extraction (M3)

The commutator-based plane extraction (M3) identifies a two-dimensional non-normal plane from the symmetric commutator of the fitted operator. We defineB=𝑭^​𝑭^⊤−𝑭^⊤​𝑭^.B=\widehat{\bm{F}}\widehat{\bm{F}}^{\top}-\widehat{\bm{F}}^{\top}\widehat{\bm{F}}.(37)

For a normal operator,𝑭^​𝑭^⊤=𝑭^⊤​𝑭^\widehat{\bm{F}}\widehat{\bm{F}}^{\top}=\widehat{\bm{F}}^{\top}\widehat{\bm{F}}, soB=0B=0. Thus,BBmeasures the departure of𝑭^\widehat{\bm{F}}from normality in the sense of non-commutation with its transpose. SinceBBis symmetric, its leading eigenspaces can be computed through a symmetric eigenproblem.

Let𝒘+\bm{w}_{+}denote the eigenvector associated with the largest positive eigenvalue ofBB, and let𝒘−\bm{w}_{-}denote the eigenvector associated with the most negative eigenvalue ofBB. The commutator plane isQcomm=[𝒘+,𝒘−].Q_{\mathrm{comm}}=[\bm{w}_{+},\bm{w}_{-}].(38)

If necessary, the two columns are orthonormalized numerically before projection. Projecting the fitted operator onto this plane gives𝚪comm=Qcomm⊤​𝑭^​Qcomm.\bm{\Gamma}_{\mathrm{comm}}=Q_{\mathrm{comm}}^{\top}\widehat{\bm{F}}Q_{\mathrm{comm}}.(39)

Unlike M2, the commutator construction returns a plane rather than a uniquely ordered input–response pair. When only scalar reduced diagnostics are needed, they can be computed from𝚪comm\bm{\Gamma}_{\mathrm{comm}}. When an ordered pair is needed, for example to compare the response direction with an observable signal, we solve the two-dimensional version of the directed-coupling problem inside the commutator plane.

Concretely, let(𝒓c,𝒏c)∈ℝ2×ℝ2(\bm{r}_{c},\bm{n}_{c})\in\mathbb{R}^{2}\times\mathbb{R}^{2}solve(𝒓c,𝒏c)=arg⁡max‖𝒖‖=1,‖𝒗‖=1⟨𝒖,𝒗⟩=0⁡⟨𝒖,𝚪comm​𝒗⟩.(\bm{r}_{c},\bm{n}_{c})=\arg\max_{\begin{subarray}{c}\left\lVert\bm{u}\right\rVert=1,\ \left\lVert\bm{v}\right\rVert=1\\
\left\langle\bm{u},\bm{v}\right\rangle=0\end{subarray}}\left\langle\bm{u},\bm{\Gamma}_{\mathrm{comm}}\bm{v}\right\rangle.(40)

The corresponding directions in the original state space are𝒓^=Qcomm​𝒓c,𝒏^=Qcomm​𝒏c,QM3=[𝒓^,𝒏^].\widehat{\bm{r}}=Q_{\mathrm{comm}}\bm{r}_{c},\qquad\widehat{\bm{n}}=Q_{\mathrm{comm}}\bm{n}_{c},\qquad Q_{\mathrm{M3}}=[\widehat{\bm{r}},\widehat{\bm{n}}].(41)

For consistency with M1 and M2, the reduced operator used for the reported M3 diagnostics is𝚪M3=QM3⊤​𝑭^​QM3.\bm{\Gamma}_{\mathrm{M3}}=Q_{\mathrm{M3}}^{\top}\widehat{\bm{F}}Q_{\mathrm{M3}}.(42)

This is the same commutator-plane projection expressed in the internally ordered basis.

The extremal eigenvalues ofBBprovide an additional marker of non-normal structure. In the synthetic benchmarks, we report the leading positive and negative commutator eigenvalues separately from the reduced diagnostics. These eigenvalues ofBBshould not be confused with the ridge parameterλ\lambdaused to estimate𝑭^\widehat{\bm{F}}, with the eigenvalues of the fitted operator𝑭^\widehat{\bm{F}}, or with the eigenvalues of the reduced matrix𝚪\bm{\Gamma}.

M3 is useful because the plane-extraction step is based on a symmetric matrix, even though the fitted operator𝑭^\widehat{\bm{F}}is generally non-normal. Its limitation is that, when the fitted dynamics are only weakly non-normal, the commutator signal can be small and the dominant plane can be less identifiable. In the moderately and strongly non-normal regimes considered below, M3 provides an independent check on the plane obtained by M2.

## 5Synthetic validation

## 5.1Synthetic benchmark protocol and validation ladder

We first test the reduced non-normality diagnostics on controlled synthetic data. In this setting, the full operator is known, so the reference response plane, the reduced operator, and the ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta)can be computed directly. The construction also allows the strength of the non-normal geometry to be varied while keeping the eigenvalue spectrum, forcing amplitude, and orientation template fixed. This separates changes caused by the reduced non-normal geometry from changes caused by the stochastic forcing or by unrelated changes in the spectrum. The central parameter reported in this section is the normalized reduced non-normality ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta)of (18), whereKKis the reduced non-normality index andKc​(Δ)K_{c}(\Delta)the threshold set by the reduced eigenvalue splittingΔ\Deltathrough (17). The scalarκ\kappaused below is only an internal construction parameter used to generate a family of increasingly anisotropic operators. It should not be confused withκ​(𝑭^)\kappa(\widehat{\bm{F}}), with the eigenvector-basis condition numberκ​(P)\kappa(P), or with the reduced eigenvector-conditioning measureκ2​D\kappa_{2D}. We therefore present the synthetic transition in terms ofRR, rather than in terms of the internal parameterκ\kappa. We organise these tests as a ladder, each rung establishing one property of the inferred diagnostic:
- (i)

the transition controlled byRRexists in the reference reduction (section5.2);
- (ii)

the plane andRRare recoverable onceFFis unknown and must be estimated from finite data (section5.3);
- (iii)

recovery scales favourably with the amount of data and the ambient dimension, well below theN2N^{2}samples needed to identify the full operator (section5.4);
- (iv)

the diagnostic can be tracked through time in a causal rolling window (section5.5); and
- (v)

it stays identifiable when the operator carries a broad singular-value spectrum rather than a single small mode (section5.6).

The empirical demonstrations insection6then apply exactly the moving-window construction validated by the last two rungs.

## 5.2VAR(1) benchmark

Synthetic trajectories are generated from the stable discrete-time VAR(1) model𝒙k+1=F​(κ)​𝒙k+𝜼k,𝜼k∼𝒩​(0,σ2​IN),ρ​(F​(κ))<1.\bm{x}_{k+1}=F(\kappa)\bm{x}_{k}+\bm{\eta}_{k},\qquad\bm{\eta}_{k}\sim\mathcal{N}(0,\sigma^{2}I_{N}),\qquad\rho(F(\kappa))<1.(43)

HereF​(κ)∈ℝN×NF(\kappa)\in\mathbb{R}^{N\times N}is a stable one-step linear map andκ\kappais the internal anisotropy parameter. We constructF​(κ)=U​Σ​(κ)​V⊤​Λ​V​Σ​(κ)−1​U⊤,F(\kappa)=U\,\Sigma(\kappa)\,V^{\top}\Lambda V\,\Sigma(\kappa)^{-1}U^{\top},(44)

whereUUandVVare fixed orthogonal matrices,Λ\Lambdais a fixed diagonal matrix of stable eigenvalues, andΣ​(κ)\Sigma(\kappa)is a diagonal anisotropy matrix. Within the parameter scan,UU,VV,Λ\Lambda, and the baseline singular-value scales are fixed. Onlyκ\kappais varied. The spectral radius is fixed atρ=0.95\rho=0.95, and the remaining eigenvalues are sampled inside the stable disk. Thus the observed changes across the parameter scan are driven by the changing non-normal geometry, not by movement of the spectrum toward instability. For each trajectory, we examine three scalar projections. The first is the empirical mean fieldmk=1N​𝟏⊤​𝒙km_{k}=\tfrac{1}{N}\bm{1}^{\top}\bm{x}_{k}of (24). The second is the input coordinate𝒏^⊤​𝒙k\widehat{\bm{n}}^{\top}\bm{x}_{k}, and the third is the response coordinate𝒓^⊤​𝒙k\widehat{\bm{r}}^{\top}\bm{x}_{k}. In this benchmark, the directions(𝒓^,𝒏^)(\widehat{\bm{r}},\widehat{\bm{n}})are extracted from the known operatorF​(κ)F(\kappa). This isolates the effect of the reduced non-normal geometry from the additional uncertainty introduced by estimating the operator from finite data.Figure 3:Synthetic VAR(1) trajectories across values of the ratioRR.Trajectories are generated from𝒙k+1=F​(κ)​𝒙k+𝜼k\bm{x}_{k+1}=F(\kappa)\bm{x}_{k}+\bm{\eta}_{k}, withN=200N=200, spectral radiusρ​(F)=0.95\rho(F)=0.95,𝜼k∼𝒩​(0,σ2​IN)\bm{\eta}_{k}\sim\mathcal{N}(0,\sigma^{2}I_{N}),σ=0.05\sigma=0.05, andT=600T=600time steps. The same noise realization is used for the four representative cases. The operatorF​(κ)F(\kappa)is constructed according to (44)
with fixed orthogonal matricesU,VU,V, a fixed stable diagonal spectrumΛ\Lambda, and a varied diagonal anisotropy matrixΣ​(κ)\Sigma(\kappa). The plots correspond toR=0.1R=0.1,R=1R=1,R=9.8R=9.8, andR=30R=30, whereR=K/Kc​(Δ)R=K/K_{c}(\Delta)andKcK_{c}is given by expression (17). The left column shows the two casesR=0.1R=0.1andR=1R=1, and the right column shows the two casesR=9.8R=9.8andR=30R=30above the reduced thresholdR=1R=1.(a)Mean fieldmk=N−1​𝟏⊤​𝒙km_{k}=N^{-1}\bm{1}^{\top}\bm{x}_{k}.(b)Input coordinate𝒏^⊤​𝒙k\widehat{\bm{n}}^{\top}\bm{x}_{k}.(c)Response coordinate𝒓^⊤​𝒙k\widehat{\bm{r}}^{\top}\bm{x}_{k}. The directions𝒏^\widehat{\bm{n}}and𝒓^\widehat{\bm{r}}are extracted from the known operatorF​(κ)F(\kappa)for each value ofκ\kappa.

Figure3shows representative trajectories for different values ofRRdefined in (18). ForR=0.1R=0.1andR=1R=1, the mean field and the two reduced coordinates remain small under the chosen forcing amplitude. ForR=9.8R=9.8andR=30R=30, the response coordinate𝒓^⊤​𝒙k\widehat{\bm{r}}^{\top}\bm{x}_{k}develops much larger excursions than the input coordinate𝒏^⊤​𝒙k\widehat{\bm{n}}^{\top}\bm{x}_{k}. Thus, as the reduced geometry crosses the transient-amplification threshold, fluctuations entering along the input direction are increasingly expressed along a nearly transverse response direction before eventually decaying.Figure 4:Mean-field correlation with the response coordinate across the non-normal transition.The horizontal axis is the normalized reduced non-normality ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta), computed from the known reduced operatorQ⊤​F​(κ)​QQ^{\top}F(\kappa)Q. The vertical axis is the absolute correlation|corr​(mk,𝒓^⊤​𝒙k)||\mathrm{corr}(m_{k},\widehat{\bm{r}}^{\top}\bm{x}_{k})|between the mean fieldmk=N−1​𝟏⊤​𝒙km_{k}=N^{-1}\bm{1}^{\top}\bm{x}_{k}and the response coordinate𝒓^⊤​𝒙k\widehat{\bm{r}}^{\top}\bm{x}_{k}. The parameter scan uses the same synthetic VAR(1) construction as infig.3, withN=200N=200,ρ​(F)=0.95\rho(F)=0.95,σ=0.05\sigma=0.05, andT=1000T=1000time steps per realization. The internal anisotropy parameterκ\kappais sampled at 116 values, with denser sampling below and aroundR=1R=1. For each value ofκ\kappa, the plotted line is the median over 16 independent noise realizations and the shaded band is the interquartile interval. The vertical dashed line marksR=1R=1.

Figure4summarizes the same transition over the parameter scan. The alignment|corr​(mk,𝒓^⊤​𝒙k)|\left|\mathrm{corr}\!\left(m_{k},\,\widehat{\bm{r}}^{\top}\bm{x}_{k}\right)\right|(45)

is small forR<1R<1and increases asRRgrows above11. This shows that the response direction becomes progressively more visible in the observed mean field as the non-normal geometry strengthens. The relevant control variable isR=K/Kc​(Δ)R=K/K_{c}(\Delta), which expresses the strength of the reduced non-normal geometry directly, rather than the internal anisotropy parameterκ\kappaused only to generate the synthetic operators. Figures3and4first validate the controlled synthetic construction. BecauseF​(κ)F(\kappa)and the reference response plane are known, these plots do not yet test finite-data operator inference. They instead show that the constructed family realizes the intended transition: increasingRRturns a weakly expressed response coordinate into a strongly amplified one. The next subsection removes access to the true operator and asks whether the reduced geometry can still be recovered from observed trajectories alone.

## 5.3Recovery from estimated operators

We next test the full inference problem. In this setting, the operatorFFis treated as unknown and must be estimated from observed trajectories. For each value of the internal anisotropy parameterκ\kappa, training trajectories are generated from (43), a fitted operator𝑭^\widehat{\bm{F}}is obtained by ridge regression using (11), and the three plane-extraction methods introduced insection4are applied to𝑭^\widehat{\bm{F}}. The reference plane is obtained by applying optimization-based directed-coupling extraction (M2) directly to the known operatorFF. To compare with the empirical setting, we show both theM=25M=25ensemble benchmark and theM=1M=1single-trajectory case.

The reference ratio is denoted byRtrue=KtrueKc​(Δtrue),R_{\mathrm{true}}=\frac{K_{\mathrm{true}}}{K_{c}(\Delta_{\mathrm{true}})},(46)

whereKtrueK_{\mathrm{true}}andΔtrue\Delta_{\mathrm{true}}are computed from the reference reduced operator𝚪true=Qtrue⊤​F​Qtrue.\bm{\Gamma}_{\mathrm{true}}=Q_{\mathrm{true}}^{\top}FQ_{\mathrm{true}}.

For an estimated operator𝑭^\widehat{\bm{F}}and an extracted planeQQ, the corresponding inferred value is denoted byR^\widehat{R}. The inferred plane is compared with the reference planeQtrueQ_{\mathrm{true}}using the largest principal angleθ​(Q,Qtrue)\theta(Q,Q_{\mathrm{true}})of (23), withQref=QtrueQ_{\mathrm{ref}}=Q_{\mathrm{true}}, and the observable content of the recovered plane is measured using the plane-invariant alignment scorecplanec_{\mathrm{plane}}defined in (25).Figure 5:Inferred reduced non-normality ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta)and response plane from estimated operators, for plane-extraction methods M1, M2, and M3.Synthetic trajectories are generated from the VAR(1) model𝒙k+1=F​(κ)​𝒙k+𝜼k\bm{x}_{k+1}=F(\kappa)\bm{x}_{k}+\bm{\eta}_{k}, withN=100N=100,ρ​(F)=0.95\rho(F)=0.95,𝜼k∼𝒩​(0,σ2​IN)\bm{\eta}_{k}\sim\mathcal{N}(0,\sigma^{2}I_{N}), andσ=0.05\sigma=0.05. For each value ofκ\kappa, the fitted operator𝑭^\widehat{\bm{F}}is estimated by
concatenatingM=25M=25independent synthetic training trajectories, each of
lengthTtrain=300T_{\mathrm{train}}=300, generated from the same operatorF​(κ)F(\kappa). Filled markers connected by lines show thisM=25M=25ensemble estimate. Open markers show the correspondingM=1M=1single-trajectory estimates, using the same method symbols. TheM=1M=1case matches the empirical moving-window setting, where each local operator is fitted from one observed trajectory segment.
The ridge parameterλ\lambdais chosen by validation: for each candidate value in a logarithmic grid from10−810^{-8}to10210^{2},F^\widehat{F}is fitted on 80% of the available training pairs and evaluated on the remaining 20%; the value minimizing the validation one-step prediction error is retained. The test trajectory used forcplanec_{\mathrm{plane}}(25) has lengthTtest=1200T_{\mathrm{test}}=1200. The horizontal axis in all panels is the reference ratioRtrue=Ktrue/Kc​(Δtrue)R_{\mathrm{true}}=K_{\mathrm{true}}/K_{c}(\Delta_{\mathrm{true}}), computed from the known operatorFF. The vertical dotted line marksRtrue=1R_{\mathrm{true}}=1.(a)Inferred ratioR^\widehat{R}for eigenbasis-SVD baseline extraction (M1), optimization-based directed-coupling extraction (M2), and commutator-based plane extraction (M3). The black diagonal curve is the reference value computed fromFF.(b)Signed deviationR^−Rtrue\widehat{R}-R_{\mathrm{true}}. The inset shows the same quantity for M1 on a larger vertical scale. Values outside the main vertical display range are indicated at the boundary; the full numerical deviations are retained in the data.(c)Plane recovery errorθ​(Q,Qtrue)\theta(Q,Q_{\mathrm{true}})(23), measured as the largest principal angle in degrees between the inferred plane and the reference plane.(d)Plane-invariant observable alignmentcplanec_{\mathrm{plane}}(25), computed between the empirical mean field and the best direction inside the inferred plane.

Figure5compares the three plane-extraction methods after the operator has been estimated from finite data. Infig.5a, the estimatedR^\widehat{R}obtained from optimization-based directed-coupling extraction (M2) and commutator-based plane extraction (M3) remain close to the true value over most of the parameter scan. The openM=1M=1markers are noisier, as expected from a single finite trajectory, but they retain the same qualitative behavior of M2 and M3 near and above the reduced threshold. The eigenbasis-SVD baseline extraction (M1) underestimatesR^\widehat{R}across a broad intermediate range. This shows that the main difficulty is not only estimating𝑭^\widehat{\bm{F}}, but also extracting a stable response plane from the estimated operator.

The deviationR^−Rtrue\widehat{R}-R_{\mathrm{true}}infig.5b gives a more sensitive comparison of the scalar diagnostic. M2 and M3 exhibit small deviations relative to the range ofRtrueR_{\mathrm{true}}, whereas M1 has larger negative deviations, shown in the inset. These negative biases indicate that M1 should not be used as the primary estimator of the response plane, but only as a transparent baseline against which the directed M2 and M3 constructions can be compared.

The plane recovery errorθ​(Q^,Qtrue)\theta({\hat{Q}},Q_{\mathrm{true}})defined by expression (23)
is shown infig.5c. ForRtrue≪1R_{\mathrm{true}}\ll 1, the response plane is weakly expressed and is difficult to identify from finite trajectories. AsRtrueR_{\mathrm{true}}approaches and exceeds the thresholdR=1R=1, the principal-angle error for M2 and M3 decreases rapidly. M1 remains poorly aligned over much of the parameter range and improves only at the largest values ofRtrueR_{\mathrm{true}}. Thus the reduced response plane becomes identifiable from finite data when the non-normal geometry is sufficiently expressed.

Finally,fig.5d shows the plane-invariant correlation scorecplanec_{\mathrm{plane}}defined by
expression (25) as a function ofRR. In the strongly non-normal regime, the planes extracted by M2 and M3 contain directions whose activity is aligned with the empirical mean field. This is important for empirical applications, where the reference plane is not known and agreement between independent extraction methods becomes an internal consistency check.

## 5.4Dependence of reduced non-normal geometry recovery on numberMMof samples, state dimensionNN, and training horizonTT

We next examine how recovery scales with the amount of data and with the ambient dimension.
To separate the relevant effects, we vary three quantities one at a time:
the numberMMof independent synthetic trajectories generated from the same operator, the state dimensionNN,
and the training horizonTtrainT_{\mathrm{train}}. For each
setting, trajectories are generated from the controlled VAR(1) family,𝑭^\widehat{\bm{F}}is estimated by ridge regression, and the three plane-extraction methods are
applied to the fitted operator. The scan overMMincludesM=1M=1, and the dimension and training-horizon scans includeM=1M=1insets for the intermediate regimeRtrue≈1R_{\mathrm{true}}\approx 1, to make the comparison with empirical single-segment fits explicit.

The reference plane is denoted byQtrueQ_{\mathrm{true}}. Plane recovery is measured by the largest principal angleθ​(Q,Qtrue)\theta(Q,Q_{\mathrm{true}})(23).
Full-operator recovery is summarized byrelErr​(𝑭^)\mathrm{relErr}(\widehat{\bm{F}})(22).
The accuracy of the estimated ratio is measured byℰR=|log10⁡(R^Rtrue)|.\mathcal{E}_{R}=\left|\log_{10}\left(\frac{\widehat{R}}{R_{\mathrm{true}}}\right)\right|.(47)

A valueℰR=log10⁡2\mathcal{E}_{R}=\log_{10}2corresponds to a factor-of-two error in the inferred ratio.Figure 6:Dependence of reduced non-normal geometry recovery on numberMMof samples, state dimensionNNand training horizonTT.Synthetic trajectories are generated from the VAR(1) model𝒙k+1=F​(κ)​𝒙k+𝜼k\bm{x}_{k+1}=F(\kappa)\bm{x}_{k}+\bm{\eta}_{k}, withρ​(F)=0.95\rho(F)=0.95,𝜼k∼𝒩​(0,σ2​IN)\bm{\eta}_{k}\sim\mathcal{N}(0,\sigma^{2}I_{N}), andσ=0.05\sigma=0.05. For each scaling variable, the internal anisotropy parameterκ\kappais chosen to obtain three reference regimes:Rtrue≈0.2R_{\mathrm{true}}\approx 0.2,Rtrue≈1R_{\mathrm{true}}\approx 1, andRtrue≈10R_{\mathrm{true}}\approx 10, whereRtrue=Ktrue/Kc​(Δtrue)R_{\mathrm{true}}=K_{\mathrm{true}}/K_{c}(\Delta_{\mathrm{true}}). The left column shows the plane errorθ​(Q,Qtrue)\theta(Q,Q_{\mathrm{true}})in degrees. The right column shows the reduced-ratio errorℰR=|log10⁡(R^/Rtrue)|\mathcal{E}_{R}=\left|\log_{10}(\widehat{R}/R_{\mathrm{true}})\right|. Solid curves denote optimization-based directed-coupling extraction (M2), and dashed curves denote commutator-based plane extraction (M3). The eigenbasis-SVD baseline extraction (M1) is out-of-range and not shown.
In the left-column panels, the grey curve with scale corresponding to the right vertical axis shows the relative full-operator errorrelErr​(𝑭^)\mathrm{relErr}(\widehat{\bm{F}})(22) for the intermediate regimeRtrue≈1R_{\mathrm{true}}\approx 1, providing a reference against which the reduced plane-recovery errors on the main axis can be compared.
In the right-column panels,
the horizontal dashed line marksℰR=log10⁡2\mathcal{E}_{R}=\log_{10}2, corresponding to a factor-of-two error.(a,b)Parameter scan over the number of trajectoriesM∈{1,2,5,10,15,25,50,100}M\in\{1,2,5,10,15,25,50,100\}, withN=100N=100andTtrain=200T_{\mathrm{train}}=200.(c,d)Parameter scan over the state dimensionN∈{50,100,150,200,250,300,350,400}N\in\{50,100,150,200,250,300,350,400\}, withM=25M=25andTtrain=200T_{\mathrm{train}}=200. Insets show the correspondingM=1M=1single-trajectory results forRtrue≈1R_{\mathrm{true}}\approx 1, using M2 and M3.(e,f)Parameter scan over the training horizonTtrain∈{3,4,10,25,50,100,200,400,800}T_{\mathrm{train}}\in\{3,4,10,25,50,100,200,400,800\}, withM=25M=25andN=100N=100. Insets show the correspondingM=1M=1single-trajectory results forRtrue≈1R_{\mathrm{true}}\approx 1, using M2 and M3.

Figure6a,b show the effect of increasing the numberMMof independent trajectories. For fixedN=100N=100andTtrain=200T_{\mathrm{train}}=200, adding independent trajectories improves both operator estimation and reduced-geometry recovery. The leftmost pointM=1M=1gives the single-trajectory setting used later in the empirical moving-window analyses. The relative operator error decreases withMM, while the plane errors of M2 and M3 decline and their reduced-ratio estimates eventually fall within the factor-of-two reference band. By contrast, the eigenbasis-SVD baseline extraction (M1) remains systematically less accurate; its errors fall outside the plotted range and are therefore omitted.

The dimension scan infig.6c,d tests whether the reduced geometry remains identifiable as the ambient regression problem grows. WithM=25M=25andTtrain=200T_{\mathrm{train}}=200fixed, increasingNNmakes the fullN×NN\times Noperator increasingly difficult to estimate entry by entry. Yet M2 and M3 preserve small plane errors and small reduced-ratio errors over the tested dimensions. TheM=1M=1insets show the same scan for the intermediate regimeRtrue≈1R_{\mathrm{true}}\approx 1; as expected, the single-trajectory errors are larger, but the M2 and M3 comparison remains visible. This shows that the dominant two-dimensional response geometry can remain identifiable even when full-matrix recovery becomes increasingly demanding.

The scan over training-horizons infig.6e,f probes the regime of small data size. WithM=25M=25andN=100N=100fixed, very short training horizons give larger errors because the regression has limited temporal information. AsTtrainT_{\mathrm{train}}increases, both the plane error and the reduced-ratio error decrease for M2 and M3. TheM=1M=1insets provide the corresponding single-trajectory comparison forRtrue≈1R_{\mathrm{true}}\approx 1. The M1 method leads to much larger errors, as expected from the sensitivity of eigenvector-based extraction to perturbations of the fitted operator.

Together, the three parameter scans show that the relevant object for the proposed reduction is not the full matrix𝑭^\widehat{\bm{F}}entry by entry, but the two-dimensional response plane and the ratio computed on that plane. The optimization-based and commutator-based methods recover these quantities across changes inMM,NN, andTtrainT_{\mathrm{train}}, whereas the eigenbasis-SVD baseline is more fragile.

This data efficiency is worth emphasizing. Entrywise identification of a generalN×NN\times Nlinear operator requires on the order ofN2N^{2}independent observations, since the operator hasN2N^{2}free parameters. The scan over scaling shows that the reduced response plane and the ratioRRare recovered well before this regime is reached: in the dimension scan, accurate recovery of both the response plane andRRis obtained with a fixed data budget ofM=25M=25trajectories of lengthTtrain=200T_{\mathrm{train}}=200, even asNNincreases to several hundred. The total number of observed time steps is therefore far belowN2N^{2}, amounting to only a few percent of the number of entries in the full operator. The target of inference is not the full operator but a two-dimensional geometry, and this lower-dimensional target can be estimated from substantially fewer samples than full operator identification would demand.

## 5.5Recovering the time-varying non-normal geometry ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta)with moving windows

The preceding benchmarks used stationary operators. We now test whether the reduced diagnosticRR, defined in (18), can be tracked when the local dynamics changes over time. This experiment matches the moving-window setting used later for empirical recordings: for each selected window end time, a local operator is estimated from the data contained in that finite window.

We generate trajectories from a VAR(1) model (43)𝒙t+1=Ft​𝒙t+𝜼t,Ft=F​(κt),𝜼t∼𝒩​(0,σ2​IN),\bm{x}_{t+1}=F_{t}\bm{x}_{t}+\bm{\eta}_{t},\qquad F_{t}=F(\kappa_{t}),\qquad\bm{\eta}_{t}\sim\mathcal{N}(0,\sigma^{2}I_{N}),(48)

where the internal anisotropy parameterκt\kappa_{t}increases logarithmically from11to200200over the simulation intervalt=1,…,600t=1,\ldots,600, as shown infig.7. As before,κt\kappa_{t}is used only to construct the time-dependent operatorFtF_{t}. The reported diagnostic is the reduced ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta)defined in (18), computed from the reduced operator.

At each window end timetendt_{\mathrm{end}}, advanced in steps of1010, a local operator is estimated from the moving window[tend−W,tend)[t_{\mathrm{end}}-W,\ t_{\mathrm{end}}), with window lengthW=80W=80. The fitted local operator is denoted by𝑭^W​(tend)\widehat{\bm{F}}_{W}(t_{\mathrm{end}}). We useM=1M=1in this test, matching the single-trajectory setting of the empirical moving-window analyses insection6.

For each window, we compare𝑭^W​(tend)\widehat{\bm{F}}_{W}(t_{\mathrm{end}})with the window average of the true time-dependent operator over the same interval,F¯W​(tend)=1W​∑t=tend−Wtend−1Ft.\bar{F}_{W}(t_{\mathrm{end}})=\frac{1}{W}\sum_{t=t_{\mathrm{end}}-W}^{t_{\mathrm{end}}-1}F_{t}.(49)

Applying optimization-based directed-coupling extraction (M2) toF¯W​(tend)\bar{F}_{W}(t_{\mathrm{end}})gives the window-matched reference valueRref,W​(tend).R_{\mathrm{ref},W}(t_{\mathrm{end}}).

Applying M2 and commutator-based plane extraction (M3) to𝑭^W​(tend)\widehat{\bm{F}}_{W}(t_{\mathrm{end}})gives the inferred valuesR^​(tend)\widehat{R}(t_{\mathrm{end}}). The signed tracking error isR^​(tend)−Rref,W​(tend).\widehat{R}(t_{\mathrm{end}})-R_{\mathrm{ref},W}(t_{\mathrm{end}}).

This comparison is window-matched: the inferred diagnostic is evaluated against the true operator averaged over the same interval used for estimation. With the right-endpoint labelling, no sample later thantendt_{\mathrm{end}}is used to estimate𝑭^W​(tend)\widehat{\bm{F}}_{W}(t_{\mathrm{end}}).Figure 7:Time-varying synthetic test with moving windows. Trajectories are generated from the time-varying VAR(1) model (48), withFt=F​(κt)F_{t}=F(\kappa_{t}),N=100N=100,M=1M=1,T=600T=600time steps,ρ​(Ft)=0.95\rho(F_{t})=0.95,𝜼t∼𝒩​(0,σ2​IN)\bm{\eta}_{t}\sim\mathcal{N}(0,\sigma^{2}I_{N}), andσ=0.05\sigma=0.05. The parameterκt\kappa_{t}increases logarithmically from11to200200. Local operators are estimated using moving windows of lengthW=80W=80with step size1010. Ridge regularization is selected fromλ∈{10−6,…,101}\lambda\in\{10^{-6},\ldots,10^{1}\}using an 80–20 train–validation split as in the previous synthetic tests.(a)Instantaneousκ​(t)\kappa(t)and its moving-window mean.(b)Window-matched reference ratioRref,WR_{\mathrm{ref},W}, obtained by applying M2 to the window-averaged true operatorF¯W​(tend)\bar{F}_{W}(t_{\mathrm{end}})in (49). The ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta)is defined in (18).(c)Inferred ratioR^\widehat{R}from the fitted local operator𝑭^W​(tend)\widehat{\bm{F}}_{W}(t_{\mathrm{end}}), compared withRref,WR_{\mathrm{ref},W}. Orange circles correspond to M2 and green triangles to M3.(d)Signed tracking errorR^−Rref,W\widehat{R}-R_{\mathrm{ref},W}for M2 and M3. In panels (b,c), the horizontal dashed line marksR=1R=1.

Figure7shows the moving-window estimate of the reduced ratioRRas the local operator changes over time. Panel (a) displays the imposed change in the internal construction parameterκt\kappa_{t}and its corresponding moving-window mean. Panel (b) shows the window-matched referenceRref,WR_{\mathrm{ref},W}, which crossesR=1R=1at approximatelytend≈260t_{\mathrm{end}}\approx 260and then continues to increase. Panel (c) compares this reference with the values inferred from fitted operators. The M2 and M3 curves remain close to the reference over most of the record. Panel (d) shows that the signed error is small through the middle of the parameter scan and grows near the final windows, where the imposed change is largest on the scale of the moving window.

This test clarifies how the moving-window diagnostic should be interpreted in non-stationary data. The quantity reported attendt_{\mathrm{end}}is not an instantaneous property of a single sample. It is a local diagnostic computed from the data in the moving window[tend−W,tend)[t_{\mathrm{end}}-W,t_{\mathrm{end}}). The comparison withRref,WR_{\mathrm{ref},W}shows that this estimate follows the corresponding window-averaged reduced geometry. This supports the use of the same moving-window construction in the empirical analyses below.

## 5.6Robustness to broad singular-value spectra

The preceding synthetic benchmarks use controlled operator families in which the dominant response plane is known. We now ask whether the proposed two-dimensional reduction remains reliable when the surrounding high-dimensional operator has a broad singular-value spectrum. This test is important because, in empirical systems, the dominant non-normal response geometry need not appear as an isolated low-dimensional component against an otherwise featureless background. We therefore embed a prescribed two-dimensional non-normal block inside a stable high-dimensional background whose singular values span a broad hierarchy.

The full operator is defined asF=O​(BR00Dβ)​O⊤,F=O\begin{pmatrix}B_{R}&0\\
0&D_{\beta}\end{pmatrix}O^{\top},(50)

whereO∈ℝN×NO\in\mathbb{R}^{N\times N}is a random orthogonal matrix,BR∈ℝ2×2B_{R}\in\mathbb{R}^{2\times 2}is a stable non-normal block with prescribed reference ratioR⋆R_{\star}, andDβD_{\beta}is a stable diagonal background. The background is given byDβ=diag​(c,1−β,c,2−β,…,c,(N−2)−β),D_{\beta}=\mathrm{diag}\left(c,1^{-\beta},c,2^{-\beta},\ldots,c,(N-2)^{-\beta}\right),(51)

withc=0.74c=0.74, so that the background remains stable and below the leading scale of the embedded block. The exponentβ\betacontrols the breadth of the background singular-value spectrum and is varied from0.250.25to2.252.25. The embedded response plane is known by construction and is given byQ⋆=O:,1:2Q_{\star}=O_{:,1:2}.
We generate noisy trajectories fromFF, estimateF^\widehat{F}by ridge regression, and apply optimization-based directed-coupling extraction M2 and commutator-based plane extraction M3 to the fitted operator. The goal is to determine whether the dominant two-dimensional non-normal geometry can still be recovered when it is embedded in a high-dimensional operator with substantial singular-value structure.Figure 8:Inferred response plane and ratioR=K/Kc​(Δ)R=K/K_{c}(\Delta)for operators with broad singular-value spectra.The full operator isF=O​diag​(BR,Dβ)​O⊤F=O\,\mathrm{diag}(B_{R},D_{\beta})\,O^{\top}(50), whereOOis random orthogonal,BRB_{R}is a stable two-dimensional non-normal block with prescribed reference ratioR⋆R_{\star}, andDβ=diag​(c​j−β)D_{\beta}=\mathrm{diag}(cj^{-\beta})is a stable diagonal background withc=0.74c=0.74and exponentβ∈{0.25,0.75,1.25,1.75,2.25}\beta\in\{0.25,0.75,1.25,1.75,2.25\}. The benchmark usesN=80N=80,M=18M=18independent training trajectories,Ttrain=220T_{\mathrm{train}}=220samples per trajectory, additive Gaussian noise withσ=0.035\sigma=0.035, ridge parameterλ=10−4\lambda=10^{-4}, fixed embedded eigenvalue splittingΔ=0.35\Delta=0.35, reference ratiosR⋆∈{1,3,10,30}R_{\star}\in\{1,3,10,30\}and 8 random realizations.(a)Normalized singular-value spectraσj​(F)/σ1​(F)\sigma_{j}(F)/\sigma_{1}(F)for the five values ofβ\beta, shown forR⋆=3R_{\star}=3.(b)Principal-angle errorθ​(Q^,Q⋆)\theta(\widehat{Q},Q_{\star})(23,23), whereQ⋆=O:,1:2Q_{\star}=O_{:,1:2}, between the inferred plane and the embedded response plane, plotted as mean±\pmstandard error over allR⋆R_{\star}values and random realizations for eachβ\beta.(c)ErrorℰR=|log10⁡(R^/R⋆)|\mathcal{E}_{R}=\left|\log_{10}(\widehat{R}/R_{\star})\right|, plotted as mean±\pmstandard error over allR⋆R_{\star}values and random realizations for eachβ\beta.(d)Inferred ratioR^\widehat{R}versus reference ratioR⋆R_{\star}for allβ\beta,R⋆R_{\star}, random realizations, and both extraction methods. The dashed line indicatesR^=R⋆\widehat{R}=R_{\star}. In panels (b–d), circles refer to optimization-based directed-coupling extraction (M2), and triangles refer to commutator-based plane extraction (M3).

Figure8tests whether the proposed reduction can identify a prescribed non-normal response geometry when it is embedded in a high-dimensional operator with a nontrivial singular-value hierarchy. Panel (a) shows the range of background singular-value structures used in the test. For largeβ\beta, the singular values span more than five orders of magnitude, so the leading two-dimensional structure is relatively well separated. For smallβ\beta, in particularβ=0.25\beta=0.25, the spectrum spans less than two decades, leaving many background directions of comparable scale and making recovery of the embedded response plane a more stringent test. The remaining panels then ask whether this additional singular structure interferes with recovery of the embedded response planeQ⋆=O:,1:2Q_{\star}=O_{:,1:2}and of its prescribed reduced ratioR⋆R_{\star}.

Panels (b) and (c) show that both optimization-based directed-coupling extraction (M2) and commutator-based plane extraction (M3) obtain small principal-angle errors and small reduced-ratio errors across the tested values ofβ\beta. Thus, recovery is not restricted to an artificially simple operator whose singular spectrum contains only one dominant low-dimensional component. Panel (d) pools all values ofβ\beta, all reference ratiosR⋆∈1,3,10,30R_{\star}\in{1,3,10,30}, all random realizations, and both extraction methods. The inferred ratios remain close to the identity lineR^=R⋆\widehat{R}=R_{\star}, showing that the scalar diagnostic is preserved not only near threshold but also in strongly non-normal regimes.

This benchmark clarifies what the two-dimensional projection is meant to do. It is not a rank-two approximation to the full operator and does not require the remainingN−2N-2directions to be dynamically negligible. Rather, it seeks the two-dimensional subspace in which the input–response geometry responsible for transient amplification is concentrated. The results show that this geometry remains identifiable even when the full operator contains many additional singular directions.

## 6Empirical applications of non-normal response inference

## 6.1From synthetic validation to empirical moving-window diagnostics

The synthetic benchmarks in Section 5 show that the reduced response plane and the reduced ratioRRdefined in (18) can be recovered from time series. There, a reference operator and response plane were available, but only for scoring; the inference itself never used them.

We now apply the same construction to empirical recordings, where the local operator and reference plane are genuinely unavailable. These examples are therefore demonstrations, not ground-truth tests. We read them through one standard, stated here and used throughout the section, so that the individual subsections need only report their results. An increase inRRmeans the fitted local reduction has moved toward or past the two-dimensional thresholdR=1R=1of (18). We treat such a change as event-associated only when four conditions hold together: M2 and M3 agree in time, the diagnostics are coherent across neighboring windows rather than isolated spikes, the change aligns with an independently defined event or activity reference, andΔ\Deltastays away from the degenerate limit. These are the checks each subsection applies. None of the examples is a detector, andR=1R=1is not a clinical or behavioral decision boundary.

We consider four settings: electrohysterogram (EHG) recordings of uterine electrical activity, epileptic seizure EEG, freezing-of-gait acceleration, and wearable inertial data from rhythmic push-ups. They differ in sensor modality, sampling rate, preprocessing, and event definition, so window lengths, filtering, regularization, and alignment rules are set per dataset. The procedure is otherwise common: estimate a local operator from a moving window, extract a two-dimensional response plane, and computeRR(18), the supportS​(𝒓^)S(\widehat{\bm{r}})(61) andΔ\Delta(14). We present the settings in order of decreasing evidential strength, from the multi-level uterine analysis to the single-record push-up example, and summarize them intable1.Table 1:Overview of the four empirical applications of non-normal response inference.For each dataset, we list the multivariate state, the moving-window length and step, the independently defined event or activity reference, the change observed in the reduced diagnosticsRRandΔ\Delta, and the level of evidence. The quantitiesRRandΔ\Deltaare defined in (18) and (14). The settings are ordered by decreasing strength of evidence.DatasetState (channels)Window / stepEvent or activity referenceObserved changeEvidence levelUterine EHG (parturition)multichannel EHG array60​s60\,\mathrm{s}/5​s5\,\mathrm{s}elevated EHG activity envelopeRRrises with activity; broadly supported reaction directionstrongest: representative, peak-aligned, and 45-subject analysesSeizure EEGscalp EEG (CHB-MIT)40​s40\,\mathrm{s}/2​s2\,\mathrm{s}annotated seizure onsetonset-aligned change inRRandΔ\Deltarepresentative and patient-pooled cohortFreezing of gait3 ankle acceleration axes3​s3\,\mathrm{s}/0.5​s0.5\,\mathrm{s}annotated freezing onsetRRrises at the onset intervalrepresentative and dataset-level onset vs baselinePush-up motion3 acceleration axeshigh- vs low-accelerationacceleration-amplitude envelopehigh-accelerationRRlarger than low but belowR=1R=1; reaction coordinate aligned with high-acceleration intervalsdirectional only; subthreshold

## 6.2Moving-window inference in empirical data

For each dataset, we construct a multivariate state𝒙​(t)=[x1​(t),x2​(t),…,xN​(t)]⊤,\bm{x}(t)=\big[x_{1}(t),x_{2}(t),\ldots,x_{N}(t)\big]^{\top},(52)

whose components are channels, sensors, or embedded coordinates, depending on the application. Each recording is first preprocessed for its modality: the filtering, downsampling, demeaning, standardization, and event alignment given in the corresponding subsection.

The data are then analyzed in moving windows. Thejj-th window holds the samples𝒲j={tj,tj+1,…,tj+W−1},\mathcal{W}_{j}=\{t_{j},t_{j}+1,\ldots,t_{j}+W-1\},(53)

whereWWis the window length in samples after preprocessing, and consecutive windows are separated by a dataset-specific step. Each window is labelled by its right endpoint,tend,j=tj+W.t_{\mathrm{end},j}=t_{j}+W.(54)

The diagnostic displayed attend,jt_{\mathrm{end},j}is computed from the samples in𝒲j\mathcal{W}_{j}, that is from the interval[tend,j−W,tend,j)[t_{\mathrm{end},j}-W,\,t_{\mathrm{end},j}); it is not a property of the single sampletend,jt_{\mathrm{end},j}. This is the endpoint convention of the time-varying synthetic test insection5.5. Each window supplies one consecutive trajectory segment, so the empirical setting corresponds toM=1M=1in the notations used for the synthetic tests.

In each window, we fit a local one-step model𝒙k+1≈𝑭^j​𝒙k,k=tj,…,tj+W−2,\bm{x}_{k+1}\approx\widehat{\bm{F}}_{j}\bm{x}_{k},\qquad k=t_{j},\ldots,t_{j}+W-2,(55)

by ridge-regularized regression. When a continuous-time generator is estimated by finite differences, the same reduction is applied to that generator; we write𝑭^j\widehat{\bm{F}}_{j}for the fitted local operator in either case.

Short windows can give poorly conditioned regressions or nearly degenerate reduced matrices, and either can inflateRRfor numerical rather than physical reasons. We therefore apply mild stabilization and screening. The stabilized operator is𝑭^j,reg=(1−α)​𝑭^j+α​μj​IN,μj=tr​(𝑭^j)N,\widehat{\bm{F}}_{j,\mathrm{reg}}=(1-\alpha)\widehat{\bm{F}}_{j}+\alpha\mu_{j}I_{N},\qquad\mu_{j}=\frac{\mathrm{tr}(\widehat{\bm{F}}_{j})}{N},(56)

withα\alphaa dataset-specific shrinkage level. A window is excluded when the regression is too poorly conditioned, when the fitted operator is numerically unstable beyond what regularization repairs, or when the reduced2×22\times 2matrix is too degenerate for a meaningfulΔ\Deltain (14) andKc​(Δ)K_{c}(\Delta)in (17). Excluded windows are missing values, not extreme values ofRR.

For each accepted window, optimization-based directed-coupling extraction (M2), described insection4.3, and commutator-based plane extraction (M3), described insection4.4, giveQjm=[𝒓^jm,𝒏^jm],m∈{M2,M3}.Q_{j}^{m}=[\widehat{\bm{r}}_{j}^{m},\widehat{\bm{n}}_{j}^{m}],\qquad m\in\{\mathrm{M2},\mathrm{M3}\}.(57)

For M3, the internal ordering step ofsection4.4assigns the response and input directions. The reduced operator is𝚪jm=(Qjm)⊤​𝑭^j,reg​Qjm,m∈{M2,M3},\bm{\Gamma}_{j}^{m}=(Q_{j}^{m})^{\top}\widehat{\bm{F}}_{j,\mathrm{reg}}Q_{j}^{m},\qquad m\in\{\mathrm{M2},\mathrm{M3}\},(58)

and from it we compute𝒟jm={Δjm,κ2​D,jm,Kjm,Rjm},m∈{M2,M3},\mathcal{D}_{j}^{m}=\{\Delta_{j}^{m},\kappa_{2D,j}^{m},K_{j}^{m},R_{j}^{m}\},\qquad m\in\{\mathrm{M2},\mathrm{M3}\},(59)

using the definitions (14)–(18) with𝚪\bm{\Gamma}replaced by𝚪jm\bm{\Gamma}_{j}^{m}. The levelRjm=1R_{j}^{m}=1is the reference threshold from the reduced calculation, not a clinical or behavioral boundary.

When an observable signal is available, we compare it with the reaction coordinateyr,jm​(t)=(𝒓^jm)⊤​𝒙​(t),t∈𝒲j,m∈{M2,M3}.y_{r,j}^{m}(t)=(\widehat{\bm{r}}_{j}^{m})^{\top}\bm{x}(t),\qquad t\in\mathcal{W}_{j},\qquad m\in\{\mathrm{M2},\mathrm{M3}\}.(60)

The observable is dataset-specific: an EHG activity envelope, EEG mean-field activity, acceleration magnitude, or an acceleration-amplitude envelope. We also report the reaction support, which separates a response direction spread across many channels from one concentrated on a few. For a normalized reaction direction𝒓^jm\widehat{\bm{r}}_{j}^{m}, the reaction support readsS​(𝒓^jm)=‖𝒓^jm‖1N​‖𝒓^jm‖2,0<S​(𝒓^jm)≤1.S(\widehat{\bm{r}}_{j}^{m})=\frac{\|\widehat{\bm{r}}_{j}^{m}\|_{1}}{\sqrt{N}\|\widehat{\bm{r}}_{j}^{m}\|_{2}},\qquad 0<S(\widehat{\bm{r}}_{j}^{m})\leq 1.(61)

Values near one mean the response direction is distributed across many components; smaller values mean it is localized.

The following subsections apply this construction to the four datasets. In the EHG, seizure, and freezing-of-gait analyses, we ask whether an independently defined event coincides with changes inRR,S​(𝒓^)S(\widehat{\bm{r}}), andΔ\Delta. The push-up example asks a different question: whether the high-acceleration samples carry a largerRRthan the low-acceleration samples, even whileRRstays below11.

## 6.3Parturition and uterine electrical activity

Uterine contractions are coordinated physiological events in which electrical activation spreads across the abdominal electrode array. Multichannel electrohysterogram (EHG) is therefore a natural first test of the method: the activation is spatially distributed, so a coherent reduced response plane, if one exists, should be visible across channels. We ask whether periods of elevated EHG-derived activity coincide with changes in the reduced ratioRRdefined in (18), the reaction supportS​(𝒓^)S(\widehat{\bm{r}})defined in (61), and the reduced eigenvalue splittingΔ\Deltadefined in (14).

The analysis used all available EHG channels. The raw signals were cropped to remove the initial contaminated segment and end effects, converted frommV\mathrm{mV}toμ​V\mu\mathrm{V}, bandpass filtered in the uterine band0.08​–​2.0​Hz0.08\text{--}2.0\,\mathrm{Hz}, and downsampled to10​Hz10\,\mathrm{Hz}. Local generators were estimated on60​s60\,\mathrm{s}moving windows advanced in5​s5\,\mathrm{s}steps by ridge-regularized least squares. Each diagnostic is plotted at the window end time (54). The fitted generator𝑭^j\widehat{\bm{F}}_{j}was stabilized by the trace-preserving shrinkage in (56) at levelα=0.1\alpha=0.1, because freely moving subjects can produce short nonstationary bursts that destabilize the local fit. The reduced plane was extracted independently by optimization-based directed-coupling extraction (M2) and commutator-based plane extraction (M3). For each accepted window, we computed the reduced quantities in (59) and the support in (61). Windows rejected by the screening rules insection6.2were treated as missing values.

For an activity reference, we used the EHG signal itself. Letxi​(t)x_{i}(t)denote the filtered EHG on channelii, and letzi​(t)=xi​(t)+i​ℋ​[xi]​(t)z_{i}(t)=x_{i}(t)+\mathrm{i}\,\mathcal{H}[x_{i}](t)(62)

be its analytic signal, whereℋ\mathcal{H}is the Hilbert transform. The EHG-derived activity envelope issEHG​(t)=1N​∑i=1N|zi​(t)|.s_{\mathrm{EHG}}(t)=\frac{1}{N}\sum_{i=1}^{N}|z_{i}(t)|.(63)

This is an electrical envelope; it is not a measurement of mechanical contraction force.

We also asked whether the reaction coordinate accounts for the coherent EHG mean field. The reaction coordinateyr,jm​(t)y_{r,j}^{m}(t)is defined in (60), and the mean field ism​(t)=1N​∑i=1Nxi​(t).m(t)=\frac{1}{N}\sum_{i=1}^{N}x_{i}(t).(64)

For each accepted window and each methodm∈{M2,M3}m\in\{\mathrm{M2},\mathrm{M3}\}, we measuredR𝒓^→m,j2=corr2​(yr,jm​(t),m​(t)),t∈𝒲j,R^{2}_{\widehat{\bm{r}}\to m,j}=\mathrm{corr}^{2}\left(y_{r,j}^{m}(t),m(t)\right),\qquad t\in\mathcal{W}_{j},(65)

the fraction of the mean-field fluctuations reconstructed by the scalar reaction coordinate. The superscript2in (65) indicates thatR𝒓^→m,j2R^{2}_{\widehat{\bm{r}}\to m,j}a coefficient of determination; it is not the reduced ratioRRof (18). We also computed the alignment between the reaction direction and the uniform mode,A𝒓^,jm=|⟨𝒓^jm,𝟏N⟩|,m∈{M2,M3}.A_{\widehat{\bm{r}},j}^{m}=\left|\left\langle\widehat{\bm{r}}_{j}^{m},\frac{\bm{1}}{\sqrt{N}}\right\rangle\right|,\qquad m\in\{\mathrm{M2},\mathrm{M3}\}.(66)

A largeR𝒓^→m,j2R^{2}_{\widehat{\bm{r}}\to m,j}means the reaction coordinate reconstructs the coherent mean-field fluctuation; a largeA𝒓^,jmA_{\widehat{\bm{r}},j}^{m}means the reaction direction𝒓^jm\widehat{\bm{r}}_{j}^{m}is itself close to the uniform mode.Figure 9:Moving-window EHG diagnostics in one representative recording.One multichannel EHG recording analyzed with60​s60\,\mathrm{s}moving windows advanced in5​s5\,\mathrm{s}steps. Diagnostics are plotted at the window end time (54). The signals were bandpass filtered between0.080.08and2.0​Hz2.0\,\mathrm{Hz}, converted toμ​V\mu\mathrm{V}, and downsampled to10​Hz10\,\mathrm{Hz}. Local generators were estimated by ridge-regularized least squares and stabilized by the shrinkage in (56) withα=0.1\alpha=0.1. Orange curves denote optimization-based directed-coupling extraction (M2), and green curves denote commutator-based plane extraction (M3). Thin transparent curves show unsmoothed values, thick curves show smoothed versions.(a)EHG-derived activity envelopesEHG​(t)s_{\mathrm{EHG}}(t)defined in (63). The grey curve is the raw envelope, the black curve a120​s120\,\mathrm{s}moving average, and inverted triangles mark detected activity peaks.(b)Reduced ratioRRdefined in (18). The dashed horizontal line marksR=1R=1.(c)Reaction supportS​(𝒓^)S(\widehat{\bm{r}})defined in (61).(d)Reaction–mean-field coefficient of determinationR𝒓^→m,j2R^{2}_{\widehat{\bm{r}}\to m,j}defined in (65).(e)Reduced eigenvalue splittingΔ\Deltadefined in (14).

Figure9shows the diagnostics for one representative recording. The activity envelope (63) infig.9a is the reference. The reduced ratioRRinfig.9b rises repeatedly during broad episodes of elevated activity, and the M2 and M3 curves share the same temporal structure. The supportS​(𝒓^)S(\widehat{\bm{r}})infig.9c stays near one over most windows, so the reaction direction is spread across the electrode array rather than concentrated on a few channels. The reaction–mean-fieldR𝒓^→m,j2R^{2}_{\widehat{\bm{r}}\to m,j}infig.9d is also near one for most of the recording: the reaction coordinate captures the coherent mean-field component. The splittingΔ\Deltainfig.9e stays finite and smooth, so the rises inRRare not numerical singularities of the reduced matrix.Figure 10:EHG diagnostics aligned to detected activity peaks in the representative recording.The activity peaks detected infig.9are aligned at time zero, using 23 peaks and a[−100,100]​s[-100,100]\,\mathrm{s}window around each. Orange curves denote optimization-based directed-coupling extraction (M2), and green curves denote commutator-based plane extraction (M3). Shaded bands show the across-peak variability.(a)Peak-aligned activity envelopesEHG​(t)s_{\mathrm{EHG}}(t)defined in (63).(b)Peak-aligned reduced ratioRRdefined in (18). The dashed horizontal line marksR=1R=1.(c)Peak-aligned reduced eigenvalue splittingΔ\Deltadefined in (14).
The vertical dotted line marks the activity peak.

The peak-aligned analysis infig.10tests whether one isolated episode drives the recording or whether the pattern repeats. With the detected peaks aligned, the envelope has a clear maximum at the alignment time,RRis elevated over the same interval for both M2 and M3, andΔ\Deltavaries smoothly across the peak. The pattern therefore recurs across the detected peaks within the recording rather than reflecting a single episode.

To test whether the association holds across the dataset, we repeated the analysis on123123recordings from4545subjects. Because the envelope amplitude is recording-dependent, we compared high-activity and baseline windows within each recording. For recordingjj, letsj​(tend)s_{j}(t_{\mathrm{end}})be the smoothed envelope on the endpoint grid, and defineℋj\displaystyle\mathcal{H}_{j}={tend:sj​(tend)≥Q0.80​[sj]},\displaystyle=\{t_{\mathrm{end}}:s_{j}(t_{\mathrm{end}})\geq Q_{0.80}[s_{j}]\},ℬj\displaystyle\mathcal{B}_{j}={tend:sj​(tend)≤Q0.50​[sj]},\displaystyle=\{t_{\mathrm{end}}:s_{j}(t_{\mathrm{end}})\leq Q_{0.50}[s_{j}]\},(67)

whereQp​[sj]Q_{p}[s_{j}]is thepp-quantile within recordingjj. Thusℋj\mathcal{H}_{j}holds the top20%20\%high-activity windows andℬj\mathcal{B}_{j}the bottom50%50\%. For any diagnosticYjm​(tend)Y_{j}^{m}(t_{\mathrm{end}}), the high-minus-baseline difference isdjm​(Y)\displaystyle d_{j}^{m}(Y)=mediantend∈ℋj​Yjm​(tend)\displaystyle=\mathrm{median}_{t_{\mathrm{end}}\in\mathcal{H}_{j}}Y_{j}^{m}(t_{\mathrm{end}})(68)−mediantend∈ℬj​Yjm​(tend),m∈{M2,M3}.\displaystyle\quad-\mathrm{median}_{t_{\mathrm{end}}\in\mathcal{B}_{j}}Y_{j}^{m}(t_{\mathrm{end}}),\qquad m\in\{\mathrm{M2},\mathrm{M3}\}.

ForY=RY=R, withRRdefined in (18), we also compute the per-recording Spearman correlationρjm=ρS​(sj​(tend),Rjm​(tend)),m∈{M2,M3}.\rho_{j}^{m}=\rho_{\mathrm{S}}\left(s_{j}(t_{\mathrm{end}}),R_{j}^{m}(t_{\mathrm{end}})\right),\qquad m\in\{\mathrm{M2},\mathrm{M3}\}~.(69)

Cliff’s delta,δ=ℙ​(Rℋ​j>R​ℬ​j)−ℙ​(R​ℋ​j<R​ℬ​j)\delta=\mathbb{P}(R_{\mathcal{H}j}>R{\mathcal{B}j})-\mathbb{P}(R{\mathcal{H}j}<R{\mathcal{B}j}), was used as a non-parametric effect size to compareRjm​(t​end)R_{j}^{m}(t{\mathrm{end}})betweenℋj\mathcal{H}_{j}andℬj\mathcal{B}_{j}. For each subject, recording-level quantities were summarized by their median, so that each subject contributed a single value.Figure 11:Subject-level summary of EHG diagnostics during high-activity and baseline windows.The analysis includes123123recordings from4545subjects. High-activity windows are the top20%20\%of the smoothed activity envelope within each recording, baseline windows the bottom50%50\%, as defined in (67). Recording-level quantities are summarized within each subject by their median. Blue denotes optimization-based directed-coupling extraction (M2), orange denotes commutator-based plane extraction (M3).(a)Distribution oflog2⁡(Rhigh/Rbase)\log_{2}(R_{\mathrm{high}}/R_{\mathrm{base}}), whereRhighR_{\mathrm{high}}andRbaseR_{\mathrm{base}}are median values ofRR(18) in high-activity and baseline windows.(b)Paired subject-level values ofRbaseR_{\mathrm{base}}andRhighR_{\mathrm{high}}.(c)Spearman correlationρjm\rho_{j}^{m}between the activity envelope andRR, defined in (69).(d)Cliff’s delta comparingRRbetween high-activity and baseline windows.(e)Method agreement between M2 and M3 forlog2⁡(Rhigh/Rbase)\log_{2}(R_{\mathrm{high}}/R_{\mathrm{base}}). The dashed diagonal marks equality.(f)Subject-levelΔ\Deltadefined in (14) in high-activity windows.(g)Reaction supportS​(𝒓^)S(\widehat{\bm{r}})defined in (61) in high-activity windows.(h)Reaction–mean-field coefficient of determinationR𝒓^→m,j2R^{2}_{\widehat{\bm{r}}\to m,j}defined in (65) in high-activity windows.(i)AlignmentA𝒓^,jmA_{\widehat{\bm{r}},j}^{m}between the reaction direction and the uniform mode, defined in (66), in high-activity windows.

Figure11summarizes the association across subjects. Panels (a) and (b) show largerRRin high-activity than in baseline windows for both M2 and M3. Panel (c) shows a positive within-recording rank correlation between the activity envelope andRR, and panel (d) the corresponding Cliff’s delta. Panel (e) shows that thelog2⁡(Rhigh/Rbase)\log_{2}(R_{\mathrm{high}}/R_{\mathrm{base}})values from M2 and M3 agree across subjects.
Panels (f)–(i) address whether the association is geometrically interpretable.Δ\Deltastays away from the degenerate limit for most subjects, so the reduced matrix is well defined. The supportS​(𝒓^)S(\widehat{\bm{r}})stays high, so the reaction direction remains spread across the array.R𝒓^→m,j2R^{2}_{\widehat{\bm{r}}\to m,j}andA𝒓^,jmA_{\widehat{\bm{r}},j}^{m}are large in high-activity windows, so the reaction coordinate is closely tied to the coherent mean field there.

The evidence is consistent across three levels of analysis: in the representative recording, around aligned activity peaks, and after aggregation at the subject level. In all cases, elevated EHG-derived activity is associated with largerRR, stronger reaction support, and pronounced mean-field alignment. This should be interpreted as an association within the EHG-derived electrical dynamics, not as a direct measurement of mechanical contraction force or as evidence for a causal model of parturition.

## 6.4Epileptic seizure EEG

During a seizure, scalp EEG becomes strongly organized in time and across electrodes. This makes it a test of whether an annotated clinical event coincides with changes in the reduced diagnosticsRR(18),S​(𝒓^)S(\widehat{\bm{r}})(61), andΔ\Delta(14). The seizure onset is annotated independently of the diagnostics, so it serves as an external reference rather than a target the method is tuned to hit.

We use seizure recordings from the CHB-MIT dataset, sampled at256​Hz256\,\mathrm{Hz}. The CHB-MIT Scalp EEG Database is a public PhysioNet dataset of long-term scalp EEG recordings from pediatric subjects with intractable epilepsy, collected at Children’s Hospital Boston. It contains multi-hour to multi-day recordings with expert annotations of seizure onset and offset, and is widely used as a benchmark for automated epileptic seizure detection and prediction.
We retained the EEG channels, removed dummy and non-EEG channels, normalized channel names, bandpass filtered between0.50.5and40​Hz40\,\mathrm{Hz}, applied a60​Hz60\,\mathrm{Hz}notch filter, and downsampled to32​Hz32\,\mathrm{Hz}. Each seizure was aligned to its annotated onset,τ=t−tonset,\tau=t-t_{\mathrm{onset}},(70)

soτ=0\tau=0is onset. The plotted time is the window endpoint relative to onset,τend,j=tend,j−tonset,\tau_{\mathrm{end},j}=t_{\mathrm{end},j}-t_{\mathrm{onset}},(71)

withtend,jt_{\mathrm{end},j}defined in (54). A diagnostic shown atτend,j\tau_{\mathrm{end},j}is thus computed from the corresponding moving window, not from a single EEG sample.

Local operators were estimated on40​s40\,\mathrm{s}moving windows advanced in2​s2\,\mathrm{s}steps by ridge-regularized least squares with mild isotropic shrinkage at levelα=0.05\alpha=0.05. In each accepted window, optimization-based directed-coupling extraction (M2) and commutator-based plane extraction (M3) gave the reduced quantities (59) and the support (61). Windows rejected by the screening rules insection6.2were treated as missing values.

As an activity reference, we use the mean fieldmEEG​(t)=1N​∑i=1Nxi​(t),m_{\mathrm{EEG}}(t)=\frac{1}{N}\sum_{i=1}^{N}x_{i}(t),(72)

and, for the cohort summary, its smoothed absolute amplitude on the onset-aligned grid. This is a reference only; it is not part of the definition of the reduced diagnostics.

We begin with one representative seizure and then pool across the cohort. Onset-aligned curves are summarized within each patient before pooling, so that patients with many recorded seizures do not dominate the cohort median.Figure 12:Moving-window EEG diagnostics in one representative seizure recording.The recording is CHB-MIT filechb01_03.edf. The EEG was bandpass filtered between0.50.5and40​Hz40\,\mathrm{Hz}, notch filtered at60​Hz60\,\mathrm{Hz}, downsampled to32​Hz32\,\mathrm{Hz}, and analyzed with40​s40\,\mathrm{s}moving windows advanced in2​s2\,\mathrm{s}steps. Diagnostics are plotted at the onset-relative window endpointτend\tau_{\mathrm{end}}defined in (71). The shaded interval marks the annotated seizure. Orange curves denote optimization-based directed-coupling extraction (M2), and green curves denote commutator-based plane extraction (M3). Thin transparent curves show unsmoothed values, thick curves show smoothed values.(a)EEG mean fieldmEEG​(t)m_{\mathrm{EEG}}(t)defined in (72).(b)Reduced ratioRRdefined in (18). The dashed horizontal line marksR=1R=1.(c)Reaction supportS​(𝒓^)S(\widehat{\bm{r}})defined in (61).(d)Reduced eigenvalue splittingΔ\Deltadefined in (14).

Figure12shows the diagnostics for one representative seizure. The mean field (72) infig.12a increases during the annotated interval. The reduced ratioRRinfig.12b rises sharply over the same interval for both M2 and M3. The supportS​(𝒓^)S(\widehat{\bm{r}})infig.12c changes during the seizure but does not fall to a single-channel response. The splittingΔ\Deltainfig.12d also changes around the interval. This representative seizure therefore illustrates a clear within-recording change in the reduced geometry during the annotated ictal interval. However, because it concerns only one seizure, it should be interpreted as an illustrative example rather than as evidence for a cohort-level effect.Figure 13:Seizure-aligned EEG diagnostics pooled across patients.The cohort analysis uses the successfully analyzed seizure recordings from the CHB-MIT dataset. Recordings were preprocessed as infig.12and analyzed with40​s40\,\mathrm{s}moving windows advanced in2​s2\,\mathrm{s}steps. Each seizure was aligned to its annotated onset using (70), and diagnostics are plotted at the onset-relative window endpointτend\tau_{\mathrm{end}}defined in (71). Curves were summarized within each patient before pooling. Solid curves show patient-level medians; dotted curves show the patient-level interquartile width on the right vertical axis where shown. The shaded interval marks the median annotated seizure duration. Orange curves denote optimization-based directed-coupling extraction (M2), and green curves denote commutator-based plane extraction (M3).(a)Onset-aligned EEG activity, quantified by the smoothed absolute mean field defined in (72).(b)Reduced ratioRRdefined in (18). The dashed horizontal line marksR=1R=1.(c)Reaction supportS​(𝒓^)S(\widehat{\bm{r}})defined in (61).(d)Reduced eigenvalue splittingΔ\Deltadefined in (14). The dashed horizontal line marksΔ=1\Delta=1.

Figure13pools the analysis across patients. The activity infig.13a rises after onset and stays elevated through the shaded interval marking the annotated seizures. The reduced ratioRRinfig.13b sits near the threshold before onset and increases modestly around the seizure. The increase is smaller than in the representative seizure, as expected after pooling across heterogeneous recordings. M2 and M3 track together in time, so the cohort pattern is not specific to one extraction method.

The support and splitting panels act as controls. The supportS​(𝒓^)S(\widehat{\bm{r}})infig.13c stays roughly constant, so the response direction is not reduced to a single channel at the cohort level. The splittingΔ\Deltainfig.13d falls during the seizure. SinceR=K/Kc​(Δ)R=K/K_{c}(\Delta)couplesKKtoKc​(Δ)K_{c}(\Delta), this panel is part of the reading: the cohort change inRRis interpreted together with the change inΔ\Delta, not as an isolated scalar.

The representative and pooled analyses together show that the annotated seizure interval coincides with changes inRRandΔ\Delta: a sharp rise inRRin the representative seizure, a more moderate one after pooling. The change is not uniform across seizures, andRRdoes not always cross11.

## 6.5Freezing of gait

Freezing of gait is an episodic motor disturbance in Parkinsonian gait in which forward progression is briefly interrupted despite the intention to walk. In inertial recordings, it usually appears as a transition from regular stride-like acceleration to a low-amplitude or irregular state. We ask whether that transition is accompanied by changes inRR(18),S​(𝒓^)S(\widehat{\bm{r}})(61), andΔ\Delta(14).

We analyzed recordings from the Daphnet Freezing of Gait dataset, a public benchmark dataset of wearable accelerometer signals collected from Parkinson’s disease patients during walking tasks designed to elicit freezing-of-gait episodes. In our analysis, we focused on ankle accelerometry, using the annotated freezing intervals to characterize changes in the recorded motor activity.

For the representative event, the state was formed from the three ankle acceleration channels,𝒙​(t)=[ax​(t),ay​(t),az​(t)]⊤,\bm{x}(t)=\big[a_{x}(t),a_{y}(t),a_{z}(t)\big]^{\top},(73)

and the displayed behavioral signal is the acceleration magnitude‖𝒂​(t)‖=ax​(t)2+ay​(t)2+az​(t)2.\|\bm{a}(t)\|=\sqrt{a_{x}(t)^{2}+a_{y}(t)^{2}+a_{z}(t)^{2}}.(74)

Local operators were estimated on3​s3\,\mathrm{s}moving windows advanced in0.5​s0.5\,\mathrm{s}steps using ridge-regularized regression. Each diagnostic is plotted at the window end timetendt_{\mathrm{end}}defined in (54). Optimization-based directed-coupling extraction (M2) and commutator-based plane extraction (M3) were applied to each accepted window to compute the reduced quantities (59) and the reaction support (61). Windows rejected by the screening rules insection6.2were treated as missing values.

The representative event isS01R01, ankle event 03. We separate the annotated freezing episode into two parts. The onset interval is its first4​s4\,\mathrm{s}, where the gait pattern is entering the freezing state; the sustained interval is the remainder, where the ankle acceleration is strongly suppressed. The separation matters becauseRRneed not be largest when the limb is nearly motionless. The relevant question is whetherRRchanges at the entry into freezing.Figure 14:Moving-window diagnostics in one representative freezing-of-gait (FOG) event.The figure shows Daphnet recordingS01R01, ankle event 03. The state is formed from the three ankle acceleration channels in (73). Diagnostics are plotted at the window end timetendt_{\mathrm{end}}defined in (54). Orange curves denote optimization-based directed-coupling extraction (M2), and green curves denote commutator-based plane extraction (M3). Thin transparent curves show unsmoothed moving-window values, and thick curves show smoothed values. The yellow shaded interval marks the onset interval, the first4​s4\,\mathrm{s}of the annotated freezing episode; the gray shaded interval marks the sustained interval, the remaining annotated freezing episode.(a)Ankle acceleration magnitude‖𝒂​(t)‖\|\bm{a}(t)\|defined in (74).(b)Reduced ratioRRdefined in (18). The dashed horizontal line marksR=1R=1.(c)Reaction supportS​(𝒓^)S(\widehat{\bm{r}})defined in (61).(d)Reduced eigenvalue splittingΔ\Deltadefined in (14).

Figure14shows the behavioral signal and the moving-window diagnostics for the representative event. Before the freezing episode, the ankle acceleration (74) contains repeated stride-like bursts; during the sustained interval it is strongly suppressed. The reduced ratioRRinfig.14b rises across the onset interval and then falls during the low-motion sustained interval. The supportS​(𝒓^)S(\widehat{\bm{r}})andΔ\Deltaalso change at the onset. The largest change inRRtherefore occurs at the entry into freezing, not during the most motionless part of the episode.

A second rise inRRcan follow the freezing episode, when stride-like acceleration resumes. We read this differently from the onset rise: it likely reflects gait re-initiation rather than entry into freezing. The dataset-level comparison below therefore uses the onset interval and matched baseline windows taken outside the freezing episode.Figure 15:Onset and baseline distributions of reduced diagnostics.The figure summarizes freezing-of-gait events from the Daphnet recordings. For each event, the onset value is computed from the onset interval and the baseline value from matched windows outside the annotated freezing episode. Orange denotes onset windows and blue denotes baseline windows. White dashed horizontal lines mark the median and quartiles of each distribution. The first two plots show
the reduced ratioRRdefined in (18) obtained with the optimization-based directed-coupling extraction (M2) and commutator-based plane extraction (M3). The last two plots show the corresponding reduced eigenvalue splittingΔ\Deltadefined in (14) for M2 and M3.

Figure15summarizes the same comparison across the analyzed events. The onset distributions ofRRsit above baseline for both M2 and M3, and theΔ\Deltadistributions show a smaller upward shift. This agrees with the representative event:RRis larger in the onset interval than in matched baseline windows. The rise inRRat onset is the reported effect;RRis not expected to stay high through the low-motion part of the episode.

## 6.6Rhythmic push-up motion

The last empirical example uses wearable inertial data recorded with an Apple Watch during rhythmic push-ups performed on two small unstable, deformable elastic fitballs, with closed fists placed parallel to the body, one on each fitball. This exercise belongs to the Logic Workout approach, which exploits controlled instability and the “reactive falling effect” for rehabilitation and performance enhancement[30,31](https://logicworkoutapp.com). It differs from the three preceding datasets in that no event is externally annotated. The movement is a voluntary continuous up–down cycle on deformable supports that induce intermittent corrective adjustments; we ask whether the reduced diagnostics identify a directed input–response geometry associated with these adjustments. With no external event to align to, we separate the recording into higher- and lower-amplitude samples using its own fluctuation envelope.

The state is the three-axis user-acceleration𝒙​(t)\bm{x}(t)as in (73). In the Apple Core Motion convention, gravity is already removed and acceleration is reported in units ofgg(about9.8​m​s−29.8\,\mathrm{m\,s^{-2}}); we subtracted the residual per-channel mean. The acceleration magnitude is defined as in (74).

From the envelope of the magnitude of𝒙​(t)\bm{x}(t), we define thehigh-accelerationclass as
corresponding to the upper15%15\%of samples and the remainder corresponds to thelow-accelerationclass. For each classq∈{low,high}q\in\{\mathrm{low},\mathrm{high}\}we fit a separate local one-step operator,𝒙​(t+Δ​t)≈𝑭^q​𝒙​(t),q∈{low,high},\bm{x}(t+\Delta t)\approx\widehat{\bm{F}}_{q}\,\bm{x}(t),\qquad q\in\{\mathrm{low},\mathrm{high}\},(75)

by ridge regression, with relative ridge level3×10−33\times 10^{-3}and isotropic shrinkageα=0.04\alpha=0.04. Applying M2 and M3 to𝑭^q\widehat{\bm{F}}_{q}gives one reduced ratioRqmR_{q}^{m}per class and method, from (14)–(18). Fitting the two classes separately keeps them from being averaged into a single map.

To test whether the response direction trackswhenthe high-acceleration samples occur, and not merely their size, we form the reaction coordinateyrm​(t)=|(𝒓^m)⊤​𝒙​(t)|,m∈{M2,M3},y_{r}^{m}(t)=\left|(\widehat{\bm{r}}^{m})^{\top}\bm{x}(t)\right|,\qquad m\in\{\mathrm{M2},\mathrm{M3}\},(76)

and quantify their temporal association by estimating the correlation between the
reaction-coordinate envelope and the high-acceleration envelopeehigh​(t)e_{\mathrm{high}}(t),chighm=corr​(ehigh​(t),yrm​(t)),m∈{M2,M3}.c_{\mathrm{high}}^{m}=\mathrm{corr}\!\left(e_{\mathrm{high}}(t),y_{r}^{m}(t)\right),\qquad m\in\{\mathrm{M2},\mathrm{M3}\}.(77)

This correlation is compared with a null obtained by circularly shiftingyrm​(t)y_{r}^{m}(t)relative toehigh​(t)e_{\mathrm{high}}(t), which preserves its amplitude distribution and autocorrelation and destroys only its timing. WithB=1000B=1000shifts and a minimum shift of3​s3\,\mathrm{s}, letμnullm=1B​∑b=1Bcnull,bm,σnullm=[1B−1​∑b=1B(cnull,bm−μnullm)2]1/2.\mu_{\mathrm{null}}^{m}=\frac{1}{B}\sum_{b=1}^{B}c_{\mathrm{null},b}^{m},\qquad\sigma_{\mathrm{null}}^{m}=\left[\frac{1}{B-1}\sum_{b=1}^{B}\left(c_{\mathrm{null},b}^{m}-\mu_{\mathrm{null}}^{m}\right)^{2}\right]^{1/2}.(78)

The standardized score and one-sided Monte Carlopp-value arezm=chighm−μnullmσnullm,z^{m}=\frac{c_{\mathrm{high}}^{m}-\mu_{\mathrm{null}}^{m}}{\sigma_{\mathrm{null}}^{m}},(79)pm=1+#​{b:cnull,bm≥chighm}1+B,p^{m}=\frac{1+\#\{b:c_{\mathrm{null},b}^{m}\geq c_{\mathrm{high}}^{m}\}}{1+B},(80)

so that withB=1000B=1000the smallest attainable value is1/1001=9.99×10−41/1001=9.99\times 10^{-4}.

Figure16a shows a representative axis of the acceleration,ay​(t)a_{y}(t), together with the slow cyclic component isolated below it; this component is small next to the broadband fluctuations.Figure16b overlays the acceleration-amplitude envelope with the M3 reaction coordinate (76). The reaction coordinate is preferentially elevated during the shaded high-acceleration intervals, showing that its temporal modulation is aligned with the timing of these intervals. The reduced ratio is also larger for the high-acceleration class than for the low-acceleration class for both extraction methods (Figure16c). Specifically, the bootstrap median isRlowM2≈0.14R^{\mathrm{M2}}_{\mathrm{low}}\approx 0.14andRhighM2≈0.23R^{\mathrm{M2}}_{\mathrm{high}}\approx 0.23, whileRlowM3≈0.04R^{\mathrm{M3}}_{\mathrm{low}}\approx 0.04andRhighM3≈0.22R^{\mathrm{M3}}_{\mathrm{high}}\approx 0.22; all values remain belowR=1R=1. The timing test (Figure16d) giveschighM2≈0.44c_{\mathrm{high}}^{\mathrm{M2}}\approx 0.44andchighM3≈0.40c_{\mathrm{high}}^{\mathrm{M3}}\approx 0.40, corresponding tozM2≈8.3z^{\mathrm{M2}}\approx 8.3andzM3≈6.6z^{\mathrm{M3}}\approx 6.6; in both casesp=9.99×10−4p=9.99\times 10^{-4}, the floor set by the shifts, since the observed correlation exceeds every shifted sample. The reaction coordinate is therefore temporally aligned with the high-acceleration intervals, rather than merely reflecting their larger amplitudes.

The high-acceleration class contains more of the large periodic push-up excursion than the low-acceleration class, so one may ask whether the elevatedRRreflects the geometry of that dominant rhythm rather than the corrective adjustments. To settle this, we remove the cycle and repeat the analysis. Because its fundamental frequency drifts across the recording, asFigure16a shows, a fixed-frequency subtraction would leave phase-dependent artifacts; we therefore fit a phase-adaptive harmonic model to each channelii,xi​(t)=∑k=1K[ai​k​(t)​cos⁡(k​ϕ​(t))+bi​k​(t)​sin⁡(k​ϕ​(t))]+ϵi​(t),x_{i}(t)=\sum_{k=1}^{K}\left[a_{ik}(t)\cos(k\phi(t))+b_{ik}(t)\sin(k\phi(t))\right]+\epsilon_{i}(t),(81)

whereϕ​(t)\phi(t)is the instantaneous push-up phase, estimated from the first principal component of the acceleration after filtering in the0.20.2–1.2​Hz1.2\,\mathrm{Hz}band. The slowly varying amplitudesai​k​(t),bi​k​(t)a_{ik}(t),b_{ik}(t)are fit by local weighted least squares over a6​s6\,\mathrm{s}window, withK=3K=3harmonics. The non-cycle residualϵ​(t)\epsilon(t)is band-limited to𝒙br​(t)=ℬ1−15​Hz​[ϵ​(t)],\bm{x}_{\mathrm{br}}(t)=\mathcal{B}_{1-15\,\mathrm{Hz}}\left[\epsilon(t)\right],(82)

withℬ1−15​Hz\mathcal{B}_{1-15\,\mathrm{Hz}}a bandpass filter, and the procedure of (75)–(80) is repeated with𝒙br​(t)\bm{x}_{\mathrm{br}}(t)in place of𝒙​(t)\bm{x}(t). The high-/low-acceleration difference is unchanged: the bootstrap median isRlowM2≈0.12R^{\mathrm{M2}}_{\mathrm{low}}\approx 0.12andRhighM2≈0.24R^{\mathrm{M2}}_{\mathrm{high}}\approx 0.24, andRlowM3≈0.04R^{\mathrm{M3}}_{\mathrm{low}}\approx 0.04andRhighM3≈0.24R^{\mathrm{M3}}_{\mathrm{high}}\approx 0.24, all high-acceleration values below11, with the reaction coordinate again aligned to the high-acceleration intervals (chighM2≈0.44c_{\mathrm{high}}^{\mathrm{M2}}\approx 0.44,chighM3≈0.40c_{\mathrm{high}}^{\mathrm{M3}}\approx 0.40); it also survives widening the residual band to11–25​Hz25\,\mathrm{Hz}, clipped below the Nyquist frequency. Since removing the cycle leaves the difference essentially unchanged, the excessRRin the high-acceleration class is carried by the non-cycle component, not by the push-up rhythm. This is also why the cycle is kept in the EHG, seizure, and freezing-of-gait analyses: there the cyclic activity is itself the annotated event and is analyzed directly, whereas here the voluntary cycle is a confound for the corrective-adjustment question.

The result does not hinge on the15%15\%cutoff. Varying it from the top30%30\%down to the top9%9\%keepsRhigh>RlowR_{\mathrm{high}}>R_{\mathrm{low}}for both methods, and the separation widens monotonically as the cutoff becomes more selective (for M2,RhighR_{\mathrm{high}}grows from≈0.17\approx 0.17to≈0.28\approx 0.28), with every value below11. The effect also appears in a moving-window analysis of the kind used for the other datasets: with short windows (≈1​s\approx 1\,\mathrm{s}, matched to the correction timescale) the localRRcorrelates positively with the acceleration envelope (Spearmanρ≈0.1\rho\approx 0.1–0.20.2) and is larger in high- than in low-acceleration windows, whereas the association washes out for windows≳2​s\gtrsim 2\,\mathrm{s}that span a full push-up cycle. This places the effect at the sub-second timescale of the reactive corrections and explains why the sample-conditioned partition, rather than the longer moving windows appropriate to the temporally extended events of the other datasets, is the natural construction here.

The point of this unstable push-up example is not thatRRcrosses the transient-amplification threshold; it does not. It is that the high-acceleration class carries a substantially largerRRthan the low-acceleration class, reproducibly across the two independent extractions M2 and M3 and across the raw and cycle-removed analyses. These high-acceleration samples are therefore not merely larger-amplitude fluctuations: they are organized along a directed input–response geometry. In the Logic Workout setting, this geometry is naturally read as the footprint of reactive stabilization, in which the participant continually counters the instability of the deformable supports. Both in the raw recording and after cycle removal, the high-acceleration samples show increased reduced non-normality with a reaction coordinate locked to their timing, suggesting that the participant generates intermittent directed correction dynamics while controlling the instability of the deformable supports, characterized by their tendency to roll and to react like a spring, consistent with the reactive falling effect[30,31]. The evidence is mechanistic and suggestive, not yet proof of clinical or performance benefit.

The fact thatRRstays below unity here is consistent with the comparatively weak amplitude contrast of the recording. Unlike the uterine, seizure, and freezing-of-gait cases, whose signals show abrupt excursions several times larger than their background, the push-up acceleration stays within a relatively narrow range, roughly0.20.2–0.8​g0.8\,g, and reads as a continuously modulated noisy signal rather than a sharply amplified transient. AlthoughRRis inferred from the geometry of the fitted local operator rather than directly from signal amplitude, such limited contrast provides weaker evidence for a pronounced directional transfer from an input direction to a distinct response direction. The method therefore identifies some organization of the high-acceleration samples, but not an input–response geometry strong enough to cross the reduced thresholdR=1R=1.

Diagnosing this subthreshold geometry is nonetheless informative, because non-normality can leave visible effects before the threshold is crossed: fluctuations become preferentially channelled along particular response directions, high-acceleration intervals align more strongly with the inferred reaction coordinate than low-acceleration intervals, and directional sensitivity can increase without producing large macroscopic excursions. The unstable push-up case is thus a useful instance of significant but sub-transient non-normal organization.

Together, the four empirical examples then span a range of behaviours, from the clearly above-threshold episodes of the uterine, seizure, and freezing-of-gait recordings to this subthreshold regime.Figure 16:Diagnostics for rhythmic unstable push-up motion using the LW protocol (https://logicworkoutapp.com).The analyzed signal is a three-axis Apple Watch user acceleration; the channels were demeaned. The reduced diagnostics are fitted to the acceleration𝒙​(t)\bm{x}(t)(73); high-acceleration samples are the upper15%15\%of the acceleration envelope and low-acceleration samples the remainder. Panels (a,b) show one representative axis,ay​(t)a_{y}(t), for legibility, while all three channels are used in the fit. Ridge regularization used relative ridge level3×10−33\times 10^{-3}and isotropic shrinkageα=0.04\alpha=0.04.(a)Accelerationay​(t)a_{y}(t)(grey) and the small slow cyclic component (dark) isolated by the phase-adaptive harmonic model of the main text, which is removed only in the robustness check described in the text.(b)Acceleration-amplitude envelopeehigh​(t)e_{\mathrm{high}}(t)with high-acceleration samples shaded, and the M3 reaction coordinateyrM3​(t)y_{r}^{\mathrm{M3}}(t)(76) overlaid on the right axis; these are the two slow traces whose correlation is tested in panel (d). The analyzed signal itself is the time series in panel (a).(c)Reduced ratioRqmR_{q}^{m}for low- and high-acceleration samples, from (75) and (14)–(18). Bars show the bootstrap median and error bars the central50%50\%interval. Color encodes class (grey low-acceleration, black high-acceleration); horizontal position encodes the method (M2 left, M3 right).(d)Vertical lines mark the observed correlationchighmc_{\mathrm{high}}^{m}between the high-acceleration envelope andyrm​(t)y_{r}^{m}(t); histograms show the corresponding circular-shift null distributions (10001000shifts, minimum shift3​s3\,\mathrm{s}).

## 7Discussion

This work has developed a data-driven reduction framework for identifying non-normal response geometry from multivariate time series. The central object is not the full fitted operator alone, but the two-dimensional response planeQ=[𝒓^,𝒏^]Q=[\widehat{\bm{r}},\widehat{\bm{n}}]defined in (12), where𝒏^\widehat{\bm{n}}is the input direction and𝒓^\widehat{\bm{r}}is the response direction. The fitted dynamics are projected onto this plane through the reduced operator𝚪\bm{\Gamma}in (13), and the reduced diagnosticsΔ\Delta,κ2​D\kappa_{2D},KK, andRRare computed from𝚪\bm{\Gamma}using (14)–(18). The levelR=1R=1is a reference threshold from the two-dimensional reduced calculation, not a universal clinical, behavioral, or full-system stability boundary.

The synthetic benchmarks provide the main validation. In the controlled VAR(1) family, the spectral template and orientation are fixed while the non-normal geometry is varied. As the reduced geometry becomes more non-normal, the response coordinate is increasingly expressed in the observable trajectories. This is organized byRR: below threshold the response stays weak, above it the reduced dynamics can produce large transient or noise-driven amplification. The mean-field correlation with the response coordinate increases withRR, so the inferred response direction is not only a geometric feature of the fitted operator but also appears in the observed trajectories.

The comparison of plane-extraction methods shows why the choice of reduction matters. Eigenbasis-SVD baseline extraction (M1) is a transparent reference but is fragile when the eigenvectors of the fitted operator are unstable. Optimization-based directed-coupling extraction (M2) and commutator-based plane extraction (M3) are more robust: they recover bothRRand the response plane in the stationary benchmark, and their agreement is informative because the two methods rest on different geometric principles. M2 maximizes directed transverse coupling; M3 uses the symmetric commutator (37) to identify a plane associated with non-normal imbalance. Agreement between them therefore indicates that the inferred plane is a property of the fitted dynamics, not an artifact of one extraction rule.

The scaling and robustness experiments clarify the target of the method. Entrywise recovery of anN×NN\times Noperator becomes harder as the dimension grows or the data shrink. Yet M2 and M3 recover the dominant response plane and the correspondingRRacross a broad range of dimensions, trajectory counts, and training horizons. TheM=1M=1synthetic results matter most for the empirical comparison, where each local fit comes from one observed segment. The broad singular-value benchmark shows further that the method does not assume the full operator is rank two or has only two important singular directions: the two-dimensional plane is a diagnostic projection of the dominant response geometry, not a low-rank approximation of the full operator.

The time-varying experiment extends this to non-stationary data. Moving-window inference tracks the window-matched referenceRref,WR_{\mathrm{ref},W}computed from the mean true operator over the same window. This matters for empirical recordings, where a single stationary operator is rarely justified. The diagnostic reported attendt_{\mathrm{end}}is a property of the data in the window[tend−W,tend)[t_{\mathrm{end}}-W,t_{\mathrm{end}}), not of one sample. This is the convention used throughout the empiricalsection6.

The empirical demonstrations show how the reduced diagnostics behave in heterogeneous recordings, read under the single standard set insection6.1. In EHG recordings, elevated activity coincides with largerRR, high reaction support, and strong alignment between the reaction coordinate and the coherent mean field, supported at three levels: one representative recording, activity-peak alignment within it, and a subject-level summary. In seizure EEG, the annotated onset interval coincides with changes inRRandΔ\Delta, sharp in the representative seizure and more moderate after patient-level pooling. In freezing of gait,RRrises at the onset interval and is larger there than in matched baseline windows. In unstable push-ups,RRstays below11, but high-acceleration samples carry a largerRRthan low-acceleration samples and the reaction coordinate tracks the high-acceleration intervals.

The strength of the evidence differs across these examples, and the diagnosticsRR,S​(𝒓^)S(\widehat{\bm{r}}),Δ\Delta, and the reaction-coordinate alignment measure related but distinct aspects of the reduced geometry. The EHG analysis gives the strongest, multi-level support. The seizure and freezing analyses show changes that are clear in representative recordings and more moderate in pooled summaries. The push-up example shows a directed response confined to the high-acceleration samples without crossingR=1R=1.

Several limitations remain. First, the framework depends on the quality of the local fit: short windows, low signal-to-noise ratio, ill-conditioned regression, or within-window non-stationarity can destabilize the reduced diagnostics. Ridge regularization, trace-preserving shrinkage, and screening of degenerate windows reduce this but do not remove the need for dataset-specific preprocessing and sensitivity checks. Second, the thresholdKc​(Δ)K_{c}(\Delta)for the existence of transient non-normal amplifications is derived for a two-dimensional real-eigenvalue reduction; it normalizesKKbut is not a universal stability boundary. Third, empirical recordings provide no reference plane, so interpretation rests on the agreement of M2 and M3, temporal coherence, event alignment, support, and non-degenerate spectra. Fourth, the framework is local and linear: it can locate a directed response inside finite windows, but it does not by itself establish the nonlinear mechanism that generates an event.

Future work can extend the framework in three directions.
Methodologically, one important direction is to derive analogous reduced diagnostics for complex-eigenvalue regimes and
for continuous-time generators with more general spectral structures.
Statistically, the framework should be complemented by uncertainty estimates for the inferred response planeQQ,
the reduced ratioRR, the reaction supportS​(r^)S(\hat{r}), and the eigenvalue splittingΔ\Delta,
for example through resampling, perturbation analysis, or state-space bootstrap methods.
Empirically, the next step is to test whether the diagnostic changes observed here persist across larger cohorts,
alternative preprocessing pipelines, and independent datasets. Together, these developments would move the approach beyond illustrative demonstrations toward
a systematic inferential framework for non-normal response geometry in clinical, physiological, and behavioral time series.

## 8Conclusion

Stable high-dimensional systems can produce large finite-time responses when their local dynamics are non-normal. Eigenvalues then set the asymptotic decay, but they do not identify the directions through which transient or noise-driven amplification occurs. This work addresses that gap with a data-driven reduction that estimates a local operator from multivariate time series, extracts a two-dimensional response plane, and computes reduced diagnostics of non-normal geometry.

The central reduced object is the projected operator𝚪\bm{\Gamma}in (13), obtained from the response planeQ=[𝒓^,𝒏^]Q=[\widehat{\bm{r}},\widehat{\bm{n}}]in (12). From it, we compute the reduced eigenvalue splittingΔ\Delta, the reduced eigenvector non-orthogonalityκ2​D\kappa_{2D}, the reduced non-normality indexKK, and the normalized ratioRRusing (14)–(18). The ratioRRgives a common scale for comparing reduced geometry across synthetic and empirical examples; it is not a stability boundary for the full system.

The synthetic benchmarks show that the reduction recovers the dominant response plane andRRfrom finite time series. M2 and M3 recover the reduced geometry more reliably than the eigenbasis-SVD baseline (M1), especially when the fitted operator is noisy or its eigenvectors unstable. The scaling experiments show that the response plane can be recovered even when entrywise recovery of the full operator is imperfect, and the broad singular-value benchmark shows that the two-dimensional plane is a diagnostic projection of the dominant response geometry, not a low-rank approximation of the full dynamics.

The empirical demonstrations show how the same diagnostics organize heterogeneous recordings. Elevated uterine EHG activity coincides with largerRR, high reaction support, and strong mean-field alignment; the annotated seizure interval coincides with changes inRRandΔ\Delta; freezing of gait shows a rise inRRat onset relative to baseline; and unstable push-up high-acceleration samples stay belowR=1R=1while carrying a largerRRthan low-acceleration samples, with the reaction coordinate tracking the high-acceleration intervals.

These are demonstrations of a diagnostic framework, not universal event detectors, and they do not replace mechanistic modeling of seizures, uterine contractions, freezing of gait, or rhythmic movement. The framework instead offers a way to identify, quantify, and visualize the low-dimensional directions through which stable local dynamics amplify fluctuations: a practical bridge from multivariate time series to interpretable non-normal response geometry.

## Appendix ATwo-dimensional transient growth in a stable non-normal system

This note gives a self-contained calculation showing how a stable two-dimensional non-normal system can exhibit finite-time amplification. The purpose is not to introduce a new estimator, but to explain the mechanism behind the reduced diagnostics used in the main text. The calculation distinguishes three different notions: spectral stability, one-step singular-value amplification, and delayed transient growth from a specified input direction.

## A.1Canonical discrete-time non-normal matrix

Consider the discrete-time linear system𝒙t+1=F​𝒙t,𝒙t∈ℝ2,\bm{x}_{t+1}=F\bm{x}_{t},\qquad\bm{x}_{t}\in\mathbb{R}^{2},(83)

withF=(aq​(a−b)0b),|a|<1,|b|<1,q≥0.F=\begin{pmatrix}a&q(a-b)\\
0&b\end{pmatrix},\qquad|a|<1,\quad|b|<1,\quad q\geq 0.(84)

The parameterqqcontrols the strength of the non-normal coupling. The off-diagonal entry is written asq​(a−b)q(a-b)because this form gives a simple expression for the powers ofFF.

The eigenvalues ofFFareλ1=a,λ2=b.\lambda_{1}=a,\qquad\lambda_{2}=b.(85)

Thus the system is asymptotically stable whenever|a|<1|a|<1and|b|<1|b|<1. The matrix is non-normal unlessq=0q=0ora=ba=b. Hence the eigenvalues determine the long-time decay, while the non-normal coupling controls the possible finite-time response.

## A.2One-step singular-value amplification

The largest possible one-step amplification is the largest singular value ofFF,σmax​(F)=λmax​(F⊤​F).\sigma_{\max}(F)=\sqrt{\lambda_{\max}\left(F^{\top}F\right)}.(86)

For the matrix in (84),F⊤​F=(a2a​q​(a−b)a​q​(a−b)b2+q2​(a−b)2).F^{\top}F=\begin{pmatrix}a^{2}&aq(a-b)\\
aq(a-b)&b^{2}+q^{2}(a-b)^{2}\end{pmatrix}.(87)

Thereforeσmax2​(F)=τ+τ2−4​a2​b22,τ=a2+b2+q2​(a−b)2.\sigma_{\max}^{2}(F)=\frac{\tau+\sqrt{\tau^{2}-4a^{2}b^{2}}}{2},\qquad\tau=a^{2}+b^{2}+q^{2}(a-b)^{2}.(88)

One-step growth occurs if and only ifσmax​(F)>1.\sigma_{\max}(F)>1.(89)

Solvingσmax​(F)=1\sigma_{\max}(F)=1givesqc,1=(1−a2)​(1−b2)|a−b|.q_{c,1}=\frac{\sqrt{(1-a^{2})(1-b^{2})}}{|a-b|}.(90)

Thus a stable matrix can amplify some initial condition after one step ifq>qc,1.q>q_{c,1}.(91)

The initial condition that maximizes one-step amplification is the dominant right singular vector ofFF, not an eigenvector. This is the first reason why transient amplification cannot be inferred from eigenvalues alone.

## A.3Exact powers and delayed transient growth

The powers of the canonical matrix areFt=(atq​(at−bt)0bt),t=0,1,2,….F^{t}=\begin{pmatrix}a^{t}&q(a^{t}-b^{t})\\
0&b^{t}\end{pmatrix},\qquad t=0,1,2,\ldots.(92)

Starting from the input coordinateen=(01),e_{n}=\begin{pmatrix}0\\
1\end{pmatrix},(93)

we obtainFt​en=(q​(at−bt)bt).F^{t}e_{n}=\begin{pmatrix}q(a^{t}-b^{t})\\
b^{t}\end{pmatrix}.(94)

The second component decays asbtb^{t}, but during this decay it feeds the first component through the non-normal couplingq​(at−bt)q(a^{t}-b^{t}). The response norm is‖Ft​en‖2=q2​(at−bt)2+b2​t.\|F^{t}e_{n}\|_{2}=\sqrt{q^{2}(a^{t}-b^{t})^{2}+b^{2t}}.(95)

For largeqq, the first component dominates during the transient phase, and‖Ft​en‖2≃q​|at−bt|.\|F^{t}e_{n}\|_{2}\simeq q\,|a^{t}-b^{t}|.(96)

This is the simplest expression of the mechanism: a stable input coordinate can be redirected into a response coordinate before both components decay asymptotically.

## A.4Peak time for the transient response

Assume for clarity that0<b<a<1.0<b<a<1.(97)

The large-qqtransient envelope is proportional tog​(t)=at−bt.g(t)=a^{t}-b^{t}.(98)

Treatingttas continuous, the maximum satisfiesdd​t​g​(t)=at​log⁡a−bt​log⁡b=0.\frac{d}{dt}g(t)=a^{t}\log a-b^{t}\log b=0.(99)

Therefore(ab)t∗=log⁡blog⁡a,\left(\frac{a}{b}\right)^{t_{\ast}}=\frac{\log b}{\log a},(100)

andt∗=log⁡(log⁡b/log⁡a)log⁡(a/b).t_{\ast}=\frac{\log\!\left(\log b/\log a\right)}{\log(a/b)}.(101)

Bothlog⁡a\log aandlog⁡b\log bare negative, so the ratiolog⁡b/log⁡a\log b/\log ais positive. Ifaaandbbare close, the two stable decay rates compete over a longer time and the peak is delayed. Ifbbis much smaller thanaa, the peak occurs earlier.

The corresponding continuous-time peak height of the large-qqenvelope isg∗=at∗−bt∗.g_{\ast}=a^{t_{\ast}}-b^{t_{\ast}}.(102)

Using (100),bt∗=at∗​log⁡alog⁡b,b^{t_{\ast}}=a^{t_{\ast}}\frac{\log a}{\log b},(103)

so thatg∗=at∗​(1−log⁡alog⁡b).g_{\ast}=a^{t_{\ast}}\left(1-\frac{\log a}{\log b}\right).(104)

For the exact discrete-time system, the maximum is obtained by checking the nearest integers tot∗t_{\ast},tpeak∈{⌊t∗⌋,⌈t∗⌉},t_{\mathrm{peak}}\in\left\{\lfloor t_{\ast}\rfloor,\,\lceil t_{\ast}\rceil\right\},(105)

and choosing the integer that maximizes‖Ft​en‖2\|F^{t}e_{n}\|_{2}.

## A.5Exact delayed-peak threshold for the canonical matrix

One-step amplification and delayed transient amplification are related but not identical. The one-step thresholdqc,1q_{c,1}in (90) asks whether some optimally chosen initial condition grows after one iterate. A different question is whether the specified input coordinateene_{n}produces a delayed response larger than its initial size.

For the exact response in (94), peak amplification fromene_{n}occurs if there exists an integert≥1t\geq 1such thatq2​(at−bt)2+b2​t>1.q^{2}(a^{t}-b^{t})^{2}+b^{2t}>1.(106)

Equivalently, the exact discrete delayed-peak threshold isqc,peakdisc=mint≥1⁡1−b2​t|at−bt|.q_{c,\mathrm{peak}}^{\mathrm{disc}}=\min_{t\geq 1}\frac{\sqrt{1-b^{2t}}}{|a^{t}-b^{t}|}.(107)

In the strongly non-normal regime, thebtb^{t}term in (95) is subdominant near the peak, and a useful approximation isqc,peak≃1maxt≥0⁡|at−bt|=1g∗.q_{c,\mathrm{peak}}\simeq\frac{1}{\max_{t\geq 0}|a^{t}-b^{t}|}=\frac{1}{g_{\ast}}.(108)

This threshold depends on the specified eigenvalue pair(a,b)(a,b). It is therefore a per-matrix threshold, not the scale-normalized threshold used for comparing different inferred reduced planes.

## A.6Illustration of delayed transient amplification

The calculation above is a finite-dimensional version of the classical nonmodal transient-growth mechanism: eigenvalues determine asymptotic decay, while singular vectors and finite-time propagators determine the largest finite-time response[1,2]. In stochastic systems, the same geometry can amplify noise-driven fluctuations even when the underlying dynamics remain linearly stable[32]. The canonical matrix in (84) makes this distinction explicit.Figure A.1:Finite-time amplification in a stable two-dimensional non-normal system.The matrix isF=(aq​(a−b)0b)F=\left(\begin{smallmatrix}a&q(a-b)\\
0&b\end{smallmatrix}\right),
witha=0.97a=0.97,b=0.75b=0.75, and0<b<a<10<b<a<1. The eigenvalues areλ1=a\lambda_{1}=aandλ2=b\lambda_{2}=b, so both lie inside the unit disk. The input coordinate isen=(0,1)⊤e_{n}=(0,1)^{\top}.(a)Response norm‖Ft​en‖2\|F^{t}e_{n}\|_{2}forq=0.50​qc,peakq=0.50\,q_{c,\mathrm{peak}},q=0.90​qc,peakq=0.90\,q_{c,\mathrm{peak}}, andq=1.45​qc,peakq=1.45\,q_{c,\mathrm{peak}}. For these parameters,qc,peak≃1.46q_{c,\mathrm{peak}}\simeq 1.46, and the displayed super-threshold response peaks neartpeak=9t_{\mathrm{peak}}=9.(b)Amplification factors as functions of the non-normal couplingqq. The blue curve shows the delayed peak responseGpeak​(q)=maxt⁡‖Ft​en‖2G_{\mathrm{peak}}(q)=\max_{t}\|F^{t}e_{n}\|_{2}. The orange curve shows the one-step optimal amplificationσmax​(F)\sigma_{\max}(F). The blue vertical dotted line marksqc,peak≃1.46q_{c,\mathrm{peak}}\simeq 1.46, and the orange vertical dotted line marks the one-step thresholdqc,1≃0.73q_{c,1}\simeq 0.73. The grey horizontal dashed line marks amplification factor11.

FigureA.1a shows the delayed response from the input coordinateene_{n}. Forq<qc,peakq<q_{c,\mathrm{peak}}, the response does not exceed its initial norm. Forq>qc,peakq>q_{c,\mathrm{peak}}, the response grows to a finite-time peak and then decays. This panel illustrates the delayed transfer from the input coordinate into the response coordinate, even though both eigenvalues lie inside the unit disk.

FigureA.1b compares two amplification thresholds for the same stable matrix family. The blue curve is the delayed peak responseGpeak​(q)=maxt≥0⁡‖Ft​en‖2,G_{\mathrm{peak}}(q)=\max_{t\geq 0}\|F^{t}e_{n}\|_{2},(109)

where the initial direction is fixed to beene_{n}. The orange curve is the one-step optimal gainσmax​(F)=max‖𝒙0‖2=1⁡‖F​𝒙0‖2.\sigma_{\max}(F)=\max_{\|\bm{x}_{0}\|_{2}=1}\|F\bm{x}_{0}\|_{2}.(110)

The two thresholds differ because they answer different questions. The one-step thresholdqc,1q_{c,1}asks whether some optimally chosen initial condition grows after one iterate. The delayed-peak thresholdqc,peakq_{c,\mathrm{peak}}asks whether the specified input coordinateene_{n}produces a response above its initial norm at a later time.

This distinction also clarifies the empirical interpretation in the main text. A reaction coordinate can align with observed bursts even whenR<1R<1. By contrast,R>1R>1indicates that the inferred reduced plane lies above the scale-normalized reduced threshold used in the two-dimensional diagnostic.

## Appendix BBasis-invariant form of the reduced threshold

Aused the canonical matrixF=(aq​(a−b)0b),|a|<1,|b|<1,F=\begin{pmatrix}a&q(a-b)\\
0&b\end{pmatrix},\qquad|a|<1,\quad|b|<1,(111)

to show how a stable two-dimensional system can produce finite-time amplification. Here we connect the coordinate-dependent parameterqqto the basis-invariant reduced quantities used in the main text.

The eigenvalues ofFF(111) areλ1=a,λ2=b.\lambda_{1}=a,\qquad\lambda_{2}=b.(112)

The reduced eigenvalue splitting isΔ=|λ1−λ2λ1+λ2|=|a−ba+b|.\Delta=\left|\frac{\lambda_{1}-\lambda_{2}}{\lambda_{1}+\lambda_{2}}\right|=\left|\frac{a-b}{a+b}\right|.(113)

ThusΔ\Deltameasures the relative separation of the two reduced eigenvalues.

Fora≠ba\neq b, the right eigenvectors may be chosen asv1=(10),v2=(−q1).v_{1}=\begin{pmatrix}1\\
0\end{pmatrix},\qquad v_{2}=\begin{pmatrix}-q\\
1\end{pmatrix}.(114)

After normalization,p1=(10),p2=11+q2​(−q1).p_{1}=\begin{pmatrix}1\\
0\end{pmatrix},\qquad p_{2}=\frac{1}{\sqrt{1+q^{2}}}\begin{pmatrix}-q\\
1\end{pmatrix}.(115)

Their absolute inner product is|⟨p1,p2⟩|=q1+q2.|\langle p_{1},p_{2}\rangle|=\frac{q}{\sqrt{1+q^{2}}}.(116)

Substitution into the reduced eigenvector-conditioning diagnostic givesκ2​D\displaystyle\kappa_{2D}=1+|⟨p1,p2⟩|1−|⟨p1,p2⟩|\displaystyle=\sqrt{\frac{1+|\langle p_{1},p_{2}\rangle|}{1-|\langle p_{1},p_{2}\rangle|}}=1+q/1+q21−q/1+q2=1+q2+q.\displaystyle=\sqrt{\frac{1+q/\sqrt{1+q^{2}}}{1-q/\sqrt{1+q^{2}}}}=\sqrt{1+q^{2}}+q.(117)

Thereforeκ2​D−1=1+q2−q,\kappa_{2D}^{-1}=\sqrt{1+q^{2}}-q,(118)

and the reduced non-normality index becomesK=κ2​D−κ2​D−12=q.K=\frac{\kappa_{2D}-\kappa_{2D}^{-1}}{2}=q.(119)

Thus, in the canonical triangular model, the coordinate couplingqqis exactly equal to the basis-invariant reduced non-normality indexKK.

The exact delayed-peak threshold in (107) depends on the absolute eigenvalue pair(a,b)(a,b). This dependence is appropriate when the full two-dimensional matrix is specified. The main text, however, compares reduced planes across windows, datasets, and fitted operators. For this purpose, we use a scale-normalized threshold that depends only on the reduced eigenvalue splittingΔ\Delta:Kc2​(Δ)=1−Δ21−1−Δ2,0≤Δ<1.K_{c}^{2}(\Delta)=\frac{\sqrt{1-\Delta^{2}}}{1-\sqrt{1-\Delta^{2}}},\qquad 0\leq\Delta<1.(120)

Equivalently,Kc​(Δ)=[1−Δ21−1−Δ2]1/2.K_{c}(\Delta)=\left[\frac{\sqrt{1-\Delta^{2}}}{1-\sqrt{1-\Delta^{2}}}\right]^{1/2}.(121)

This threshold is not the same object asqc,peakdiscq_{c,\mathrm{peak}}^{\mathrm{disc}}. The latter is an exact delayed-peak threshold for a specified matrix and a specified input direction. In contrast,Kc​(Δ)K_{c}(\Delta)is a scale-normalized reduced threshold expressed in the basis-invariant diagnosticsΔ\DeltaandKK.

The limiting behavior ofKc​(Δ)K_{c}(\Delta)is consistent with the role of spectral splitting. AsΔ→0\Delta\to 0, the two reduced eigenvalues become nearly equal andKc​(Δ)→∞.K_{c}(\Delta)\to\infty.(122)

In this limit, a larger amplitude of reduced eigenvector non-orthogonality is required to obtain the same scale-normalized amplification level. AsΔ→1\Delta\to 1,Kc​(Δ)→0.K_{c}(\Delta)\to 0.(123)

In this limit, the two reduced eigenvalues are strongly separated and less non-orthogonality is needed to reach the reduced threshold.

The normalized reduced non-normality ratio used in the main text isR=KKc​(Δ).R=\frac{K}{K_{c}(\Delta)}.(124)

For the canonical triangular model, sinceK=qK=q, this can be written asR=qKc​(Δ).R=\frac{q}{K_{c}(\Delta)}.(125)

ValuesR<1R<1indicate that the inferred reduced geometry lies below the scale-normalized reduced threshold, while valuesR>1R>1indicate that it lies above that threshold. This statement concerns the inferred two-dimensional reduced geometry. It does not imply asymptotic instability of the full system.

The distinction betweenqc,peakdiscq_{c,\mathrm{peak}}^{\mathrm{disc}}andKc​(Δ)K_{c}(\Delta)is essential. The exact thresholdqc,peakdiscq_{c,\mathrm{peak}}^{\mathrm{disc}}is tied to a specified eigenvalue pair and a specified initial direction. The reduced thresholdKc​(Δ)K_{c}(\Delta)is used to compare inferred planes throughΔ\Delta,κ2​D\kappa_{2D}, andKK. Consequently,R=K/Kc​(Δ)R=K/K_{c}(\Delta)should be interpreted as a reduced diagnostic of the inferred plane, not as a universal full-system stability boundary.

## CRediT authorship contribution statement

V.R. Saiprasad:Software, Investigation, Formal analysis, Validation, Writing – original draft, Writing – review & editing.V. Troude:Conceptualization, Methodology, Writing – original draft, Writing – review & editing.D. Sornette:Conceptualization, Supervision, Funding acquisition, Writing – review & editing. V.R. Saiprasad and V. Troude contributed equally to this work.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Funding

D.S. was partially supported by the National Natural Science Foundation of China (Grant No. T2350710802 and No. U2039202), the Shenzhen Science and Technology Innovation Commission (Grants No. GJHZ20210705141805017 and No. K23405006), and the Center for Computational Science and Engineering at the Southern University of Science and Technology.

## Data and code availability

The non-normal directional response inference method is released as an open-source, reusable calibration package, provided together with the code that reproduces the analyses and synthetic benchmarks of this paper and a per-dataset reproducibility guide in a single public repository[33], which also contains the push-up inertial recording analysed here. The three public datasets are available from their original sources: the multichannel electrohysterogram recordings and the CHB-MIT Scalp EEG Database through PhysioNet[23,25], and the Daphnet Freezing-of-Gait dataset[24].

## References
- [1]L. N. Trefethen, A. E. Trefethen, S. C. Reddy, T. A. Driscoll, Hydrodynamic
stability without eigenvalues, Science 261 (5121) (1993) 578–584.doi:10.1126/science.261.5121.578.
- [2]L. N. Trefethen, M. Embree, Spectra and Pseudospectra: The Behavior of
Nonnormal Matrices and Operators, Princeton University Press, Princeton, NJ,
2005.
- [3]P. J. Schmid, Nonmodal stability theory, Annual Review of Fluid Mechanics 39
(2007) 129–162.doi:10.1146/annurev.fluid.38.050304.092139.
- [4]M. G. Neubert, H. Caswell, Alternatives to resilience for measuring the
responses of ecological systems to perturbations, Ecology 78 (3) (1997)
653–665.doi:10.1890/0012-9658(1997)078[0653:ATRFMT]2.0.CO;2.
- [5]M. G. Neubert, H. Caswell, J. D. Murray, Transient dynamics and pattern
formation: reactivity is necessary for turing instabilities, Mathematical
Biosciences 175 (1) (2002) 1–11.doi:10.1016/S0025-5564(01)00087-6.
- [6]S. Tang, S. Allesina, Reactivity and stability of large ecosystems, Frontiers
in Ecology and Evolution 2 (2014) 21.doi:10.3389/fevo.2014.00021.
- [7]B. K. Murphy, K. D. Miller, Balanced amplification: A new mechanism of
selective amplification of neural activity patterns, Neuron 61 (4) (2009)
635–648.doi:10.1016/j.neuron.2009.02.005.
- [8]G. Hennequin, T. P. Vogels, W. Gerstner, Non-normal amplification in random
balanced neuronal networks, Physical Review E 86 (1) (2012) 011909.doi:10.1103/PhysRevE.86.011909.
- [9]M. Asllani, R. Lambiotte, T. Carletti, Structure and dynamical behavior of
non-normal networks, Science Advances 4 (12) (2018) eaau9403.doi:10.1126/sciadv.aau9403.
- [10]M. Asllani, T. Carletti, Topological resilience in non-normal networked
systems, Physical Review E 97 (4) (2018) 042302.doi:10.1103/PhysRevE.97.042302.
- [11]S. Nicoletti, D. Fanelli, A. J. McKane, M. Asllani, T. Biancalani, T. Carletti,
Non-normal amplification of stochastic quasicycles, Physical Review E 98 (3)
(2018) 032214.doi:10.1103/PhysRevE.98.032214.
- [12]R. Muolo, T. Carletti, J. P. Gleeson, M. Asllani, Synchronization dynamics in
non-normal networks: the trade-off for optimality, Entropy 23 (1) (2021) 36.doi:10.3390/e23010036.
- [13]N. Hatano, D. R. Nelson, Localization transitions in non-hermitian quantum
mechanics, Physical Review Letters 77 (3) (1996) 570–573.doi:10.1103/PhysRevLett.77.570.
- [14]D. Sornette, Why Stock Markets Crash: Critical Events in Complex Financial
Systems, Princeton University Press, Princeton, NJ, 2003.
- [15]D. Sornette, S. C. Lera, J. Lin, K. Wu, Non-normal interactions create
socio-economic bubbles, Communications Physics 6 (2023) 261.doi:10.1038/s42005-023-01379-7.
- [16]M. Scheffer, J. Bascompte, W. A. Brock, V. Brovkin, S. R. Carpenter, V. Dakos,
H. Held, E. H. van Nes, M. Rietkerk, G. Sugihara, Early-warning signals for
critical transitions, Nature 461 (2009) 53–59.doi:10.1038/nature08227.
- [17]M. Scheffer, S. R. Carpenter, T. M. Lenton, J. Bascompte, W. Brock, V. Dakos,
J. van de Koppel, I. A. van de Leemput, S. A. Levin, E. H. van Nes,
M. Pascual, J. Vandermeer, Anticipating critical transitions, Science
338 (6105) (2012) 344–348.doi:10.1126/science.1225244.
- [18]T. M. Lenton, H. Held, E. Kriegler, J. W. Hall, W. Lucht, S. Rahmstorf, H. J.
Schellnhuber, Tipping elements in the earth’s climate system, Proceedings of
the National Academy of Sciences 105 (6) (2008) 1786–1793.doi:10.1073/pnas.0705414105.
- [19]M. I. Maturana, C. Meisel, K. Dell, P. J. Karoly, W. D’Souza, D. B. Grayden,
A. N. Burkitt, P. Jiruska, J. Kudlacek, J. Hlinka, M. J. Cook, L. Kuhlmann,
D. R. Freestone, Critical slowing down as a biomarker for seizure
susceptibility, Nature Communications 11 (2020) 2172.doi:10.1038/s41467-020-15908-3.
- [20]T. Wilkat, T. Rings, K. Lehnertz, No evidence for critical slowing down prior
to human epileptic seizures, Chaos 29 (9) (2019) 091104.doi:10.1063/1.5122759.
- [21]V. Troude, S. C. Lera, K. Wu, D. Sornette, Pseudo-bifurcations in stochastic
non-normal systems and the limits of early-warning signals, Communications
Physics (2026).
- [22]V. Troude, D. Sornette, Unifying framework for amplification mechanisms:
Spectral criticality, resonance, and nonnormality, Physical Review Research
7 (4) (2025) L042048.
- [23]A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov,
R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, H. E. Stanley, Physiobank,
physiotoolkit, and physionet: components of a new research resource for
complex physiologic signals, Circulation 101 (23) (2000) e215–e220.doi:10.1161/01.CIR.101.23.e215.
- [24]B. R. Bloem, J. M. Hausdorff, J. E. Visser, N. Giladi, Falls and freezing of
gait in parkinson’s disease: a review of two interconnected, episodic
phenomena, Movement Disorders 19 (8) (2004) 871–884.doi:10.1002/mds.20115.
- [25]A. Alexandersson, T. Steingrimsdottir, J. Terrien, C. Marque, B. Karlsson, The
icelandic 16-electrode electrohysterogram database, Scientific Data 2 (2015)
150017.doi:10.1038/sdata.2015.17.
- [26]S. L. Brunton, J. L. Proctor, J. N. Kutz, Discovering governing equations from
data by sparse identification of nonlinear dynamical systems, Proceedings of
the National Academy of Sciences 113 (15) (2016) 3932–3937.doi:10.1073/pnas.1517384113.
- [27]S. H. Rudy, S. L. Brunton, J. L. Proctor, J. N. Kutz, Data-driven discovery of
partial differential equations, Science Advances 3 (4) (2017) e1602614.doi:10.1126/sciadv.1602614.
- [28]K. Course, P. B. Nair, State estimation of a physical system with unknown
governing equations, Nature 622 (2023) 261–267.doi:10.1038/s41586-023-06574-8.
- [29]T.-T. Gao, B. Barzel, Learning interpretable dynamics of stochastic complex
systems from experimental data, Nature Communications 15 (2024) 6029.doi:10.1038/s41467-024-50378-x.
- [30]P.-E. Sornette, D. Sornette,Harnessing
the “reactive falling effect” for rehabilitation and performance boosting(2025).arXiv:2506.13959.
URLhttps://arxiv.org/abs/2506.13959
- [31]P.-E. Sornette, D. Sornette,Nature
doesn’t optimize for comfort: How instability makes you resilient, Schweizer
Monat (1122) (2026) 11–13.
URLhttps://schweizermonat.ch/nature-doesnt-optimize-for-comfort-how-instability-makes-you-resilient/
- [32]B. F. Farrell, P. J. Ioannou, Variance maintained by stochastic forcing of
non-normal dynamical systems associated with linearly stable shear flows,
Physical Review Letters 72 (8) (1994) 1188–1191.doi:10.1103/PhysRevLett.72.1188.
- [33]V. R. Saiprasad, V. Troude, D. Sornette,NNDR — non-normal
directional response inference: reusable calibration package with analysis
and synthetic-benchmark reproduction code and per-dataset reproducibility
guide, Software (2026).doi:10.5281/zenodo.21386107.
URLhttps://github.com/Saiprasad-V-R/nndr-toolkit

## 


- 


Major funding support from
