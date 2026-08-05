# Phase-Drift Limits and Adaptive Quadrature Readout in Programmable Photonic Processors

**arXiv ID**: 2608.02249v1
**Authors**: Gökhan Elmas, Igor A. Litvin, Janis Nötzel
**Published**: 2026-08-03
**Categories**: physics.optics, quant-ph
**HTML URL**: https://arxiv.org/html/2608.02249v1

## Abstract

Phase fluctuations between optical inputs limit programmable photonic processors because their output powers depend on coherent interference. We study the phase-drift penalty that arises when sine and cosine quadratures are measured sequentially rather than simultaneously. The analysis is motivated by measurements from an eight-mode programmable photonic processor, including 35 free-running recordings of 300 s acquired at approximately 125 samples per second per channel. These recordings provide an empirical route for estimating the phase-increment variance at a selected reconfiguration interval.   The estimate is defined at the time of the second measurement. For fixed quadrature order, perturbation of the atan2 reconstruction gives $e_{C\to S}=-δ_τ\sin^2φ_0+O(δ_τ^2)$ and $e_{S\to C}=-δ_τ\cos^2φ_0+O(δ_τ^2)$. Writing $Q_τ=\operatorname{Var}(δ_τ)$, uniform phase averaging gives the first-order drift mean-square error $3Q_τ/8$. A phase-predicted ordering rule measures the locally less informative quadrature first and the more informative quadrature second. Its uniform first-order penalty is $(3/8-1/π)Q_τ$, which is 84.9 percent below the fixed-order value.   We also derive an increment-aware estimator from a local state-space model. Marginalizing the unknown phase increment increases the variance of a stale phase observation by $Q_τ$, reducing its Fisher information from $I$ to $I/(1+IQ_τ)$. For ideal balanced Poisson detection, the Fisher information of each quadrature equals its detected signal-photon number. This yields dimensionless architecture boundaries in spatial information and phase-increment variance. Nonlinear Monte Carlo simulations validate the perturbative laws, quantify robustness to prediction error, and compare simultaneous, fixed-order, increment-aware, and adaptive receivers under a common noise model.

## Full Text

Phase-Drift Limits and Adaptive Quadrature Readout in Programmable Photonic Processors

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
- License: CC BY 4.0arXiv:2608.02249v1 [physics.optics] 03 Aug 2026

## Phase-Drift Limits and Adaptive Quadrature Readout
in Programmable Photonic ProcessorsGökhan Elmas, Igor A. Litvin, and Janis Nötzel
Emmy-Noether Group Theoretical Quantum Systems Design,
Technical University of Munich, Munich, Germany

## Abstract

Phase fluctuations between optical inputs limit programmable photonic
processors because their output powers depend on coherent interference. We
study the phase-drift penalty that arises when sine and cosine quadratures are
measured sequentially rather than simultaneously. The analysis is motivated by
phase-drift measurements from an eight-mode programmable photonic processor, in
which two equal-power inputs were mapped to four output powers and 35
free-running recordings of 300 s were acquired at approximately 125 samples
per second per channel. These recordings provide an empirical route for
estimating the phase-increment variance associated with a selected
reconfiguration interval, while the receiver laws remain independent of a
particular drift model.

The estimate is defined at the time of the second measurement. For fixed
quadrature order, a detailed perturbation of the exactatan2\operatorname{atan2}reconstruction giveseC→S\displaystyle e_{C\rightarrow S}=−δτ​sin2⁡ϕ0+O​(δτ2),\displaystyle=-\delta_{\tau}\sin^{2}\phi_{0}+O(\delta_{\tau}^{2}),eS→C\displaystyle e_{S\rightarrow C}=−δτ​cos2⁡ϕ0+O​(δτ2)\displaystyle=-\delta_{\tau}\cos^{2}\phi_{0}+O(\delta_{\tau}^{2})

,
whereδτ\delta_{\tau}is the relative-phase change during reconfiguration.
WritingQτ=Var⁡(δτ)Q_{\tau}=\operatorname{Var}(\delta_{\tau}), uniform phase averaging
gives the first-order drift mean-square error3​Qτ/83Q_{\tau}/8. A
phase-predicted ordering rule measures the locally less informative quadrature
first and the more informative quadrature second. Its uniform first-order
penalty is(3/8−1/π)​Qτ(3/8-1/\pi)Q_{\tau}, which is 84.9% below the fixed-order
value.

We further derive an increment-aware estimator from a local state-space model.
Marginalizing the unknown phase increment increases the variance of a stale
phase observation byQτQ_{\tau}, reducing its Fisher information fromIItoI/(1+I​Qτ)I/(1+IQ_{\tau}). For ideal balanced Poisson detection, the Fisher
information of each quadrature equals its detected signal-photon number. This
provides a physical resource interpretation and leads to dimensionless
architecture boundaries in the plane of spatial information and phase-increment
variance. Exact nonlinear Monte Carlo simulations validate the perturbative
laws, quantify robustness to prediction error, and compare simultaneous,
fixed-order, increment-aware, and adaptive receivers under a common
measurement-noise model.

Keywords:photonic processor, phase instability, phase drift, quadrature readout,
phase estimation, adaptive measurement, feedback stabilization

## 1Introduction

Programmable photonic processors implement linear transformations through
interference in meshes of tunable Mach–Zehnder interferometers (MZIs).
Universal mesh architectures were introduced by Recket al.[1]and later improved through the rectangular arrangement proposed
by Clementset al.[2]. Integrated implementations now
support programmable transformations involving many spatial modes and large
numbers of optical components[14,15,16,4]. Such processors are
used in quantum photonics, optical signal processing, secure communications,
and photonic machine learning[3,17,5,6].

The output powers of a multi-input processor depend on the relative optical
phases. In a fiber-coupled system, mechanical vibration changes the propagation
length and produces microbending, while temperature variation changes both the
physical length and refractive index[7,8]. Airflow from active cooling, acoustic
excitation, chip heating, and thermal crosstalk can therefore move the
interference pattern even when the programmed transfer matrix is held fixed.
Measurements on an eight-mode programmable processor characterized the
free-running relative-phase fluctuations and revealed both broad stochastic
evolution and structured spectral components associated with correlated
disturbances[9]. Subsequent work used on-chip feedback to improve the
repeatability of two-input and multi-input transformations[10,12]. Related integrated-photonic
studies have demonstrated active phase control and high-precision phase locking,
providing further context for stabilized interferometric operation[18,19]. Related work from the group also
addressed robust calibration and energy optimization in reconfigurable
photonic processors and joint-detection architectures with multi-input phase
stabilization[11,13].

A common phase-monitoring task is to infer an unknown relative phase from two
responses proportional tocos⁡ϕ\cos\phiandsin⁡ϕ\sin\phi. In the spatial
configuration demonstrated in Ref.[9], the two quadratures
are produced simultaneously in different output pairs. A temporal receiver can
instead reconfigure a smaller set of outputs and measure the quadratures one
after another. The latter choice may reduce parallel detector requirements or
increase the optical information collected in each setting, but the two
measurements then refer to different phases.

These measured phase fluctuations motivate a receiver-design question that
is not resolved by phase-statistics measurements alone: how much estimation
error is caused by sequential quadrature acquisition, and when can a temporal
receiver outperform a simultaneous receiver? To make this comparison
unambiguous, the phase to be estimated is defined at the completion of the
second measurement. We derive the fixed-order drift error step by step, obtain
an adaptive ordering law, construct an increment-aware estimator, and state the
resource assumptions required for an architecture crossover. We also connect
the abstract Fisher-information quantities to ideal balanced photon counting,
define the information-gain factor of temporal reuse, and obtain a general
architecture phase diagram without imposing a particular dependence ofQτQ_{\tau}on delay. The numerical study then evaluates the exact nonlinear
estimators rather than only their small-drift approximations.

## 2Experimental basis and optical transformation

## 2.1Processor configuration and data acquisition

The experimental basis is the eight-mode rectangular processor and synchronized
four-port data set reported in Ref.[9]. The processor
contains tunable MZIs and external thermo-optic phase shifters. With the phase
convention used there, one unit cell is represented byU​(φ,θ)=12​(1−e−i​θ−i​(1+e−i​θ)−i​(1+e−i​θ)​e−i​φ−(1−e−i​θ)​e−i​φ),U(\varphi,\theta)=\frac{1}{2}\begin{pmatrix}1-e^{-i\theta}&-i(1+e^{-i\theta})\\
-i(1+e^{-i\theta})e^{-i\varphi}&-(1-e^{-i\theta})e^{-i\varphi}\end{pmatrix},(1)

whereθ\thetais the internal MZI phase andφ\varphiis the external
phase shift.

Two equal-power fields were injected into ports 4 and 8. In the implemented
path, MZI[2]/TPS[6] split the field from input 4, while MZI[4]/TPS[8] split the
field from input 8. The two branches were recombined in the unit cells
MZI[43]/TPS[47] and MZI[46]/TPS[50], with the combining MZIs operated as
50:50 couplers. TPS[42] supplied the additionalπ/2\pi/2shift that converts
one interference pair from cosine to sine dependence. The corresponding optical routing is shown in
Fig.1. The measured phase records motivate the increment
model introduced in Sec.3.1and provide an empirical
route for estimating the phase-increment variance at a selected delay.Figure 1:Eight-mode programmable photonic processor and quadrature-extraction
configuration used for simultaneous sine–cosine phase extraction[9].

## 2.2From input fields to sine and cosine powers

Let the input fields beE4​(t)=E0​ei​ϕ4​(t),E8​(t)=E0​ei​ϕ8​(t),E_{4}(t)=E_{0}e^{i\phi_{4}(t)},\qquad E_{8}(t)=E_{0}e^{i\phi_{8}(t)},(2)

with equal input powerP0=|E0|2P_{0}=|E_{0}|^{2}, and define the relative phaseΔ​ϕ​(t)=ϕ4​(t)−ϕ8​(t).\Delta\phi(t)=\phi_{4}(t)-\phi_{8}(t).(3)

For the programmed transformation, the four
relevant output amplitudes can be written asE1,2​(t)\displaystyle E_{1,2}(t)=±i2​E4​(t)+12​E8​(t),\displaystyle=\pm\frac{i}{2}E_{4}(t)+\frac{1}{2}E_{8}(t),(4a)E7,8​(t)\displaystyle E_{7,8}(t)=−i2​E4​(t)∓i2​E8​(t).\displaystyle=-\frac{i}{2}E_{4}(t)\mp\frac{i}{2}E_{8}(t).(4b)

The power calculation is worth writing explicitly because it shows why four
ports are sufficient. For the first pair,P1,2\displaystyle P_{1,2}=|±i2​E4+12​E8|2\displaystyle=\left|\pm\frac{i}{2}E_{4}+\frac{1}{2}E_{8}\right|^{2}(5)=14​(|E4|2+|E8|2±2​Im⁡[E4​E8∗])\displaystyle=\frac{1}{4}\left(|E_{4}|^{2}+|E_{8}|^{2}\pm 2\operatorname{Im}[E_{4}E_{8}^{*}]\right)(6)=P02​[1±sin⁡Δ​ϕ].\displaystyle=\frac{P_{0}}{2}\left[1\pm\sin\Delta\phi\right].(7)

Similarly,P7,8\displaystyle P_{7,8}=|−i2​E4∓i2​E8|2\displaystyle=\left|-\frac{i}{2}E_{4}\mp\frac{i}{2}E_{8}\right|^{2}(8)=14​(|E4|2+|E8|2±2​Re⁡[E4​E8∗])\displaystyle=\frac{1}{4}\left(|E_{4}|^{2}+|E_{8}|^{2}\pm 2\operatorname{Re}[E_{4}E_{8}^{*}]\right)(9)=P02​[1±cos⁡Δ​ϕ].\displaystyle=\frac{P_{0}}{2}\left[1\pm\cos\Delta\phi\right].(10)

The signs in Eqs. (7) and
(10) depend only on the port labeling; the two
members of each pair are complementary.

Balanced differences remove the common power scale:S=P1−P2P1+P2=sin⁡Δ​ϕ,C=P7−P8P7+P8=cos⁡Δ​ϕ.S=\frac{P_{1}-P_{2}}{P_{1}+P_{2}}=\sin\Delta\phi,\qquad C=\frac{P_{7}-P_{8}}{P_{7}+P_{8}}=\cos\Delta\phi.(11)

The relative phase on the principal interval is thereforeΔ​ϕ^=atan2⁡(S,C).\widehat{\Delta\phi}=\operatorname{atan2}(S,C).(12)

Ref.[9]described the same full-plane reconstruction through
complementary inverse-sine and inverse-cosine branches followed by unwrapping.
Equation (12) is the compact two-quadrature form of that
procedure. For a time series, unwrapping is applied after the circular estimate
to recover excursions beyond a single2​π2\piinterval.

For the receiver analysis, additive quadrature noise is modeled asC~=cos⁡ϕ+nC,S~=sin⁡ϕ+nS,\widetilde{C}=\cos\phi+n_{C},\qquad\widetilde{S}=\sin\phi+n_{S},(13)

where the noise variables are zero mean. Gaussian noise is used in the Monte
Carlo study, but the drift-only perturbation below does not require a Gaussian
measurement model.

## 3Relative-phase increment model

For monochromatic light in a path of lengthL​(t)L(t)and refractive indexn​(t)n(t), the propagation-dependent phase isϕ​(t)=2​πλ​n​(t)​L​(t).\phi(t)=\frac{2\pi}{\lambda}n(t)L(t).(14)

A first-order physical perturbation givesd​ϕ=2​πλ​[n​d​L+L​d​n].d\phi=\frac{2\pi}{\lambda}\left[n\,dL+L\,dn\right].(15)

Thus, fiber displacement and microbending contribute throughd​LdL, while
thermo-optic and strain-induced index changes contribute throughd​ndn.
Airflow, mechanical vibration, chip heating, and thermal crosstalk can therefore
produce a random relative-phase change during a receiver reconfiguration
interval.

The processor measures a relative phase. LetΔ​ϕ​(t)=ϕa​(t)−ϕb​(t),\Delta\phi(t)=\phi_{a}(t)-\phi_{b}(t),(16)

and define the phase increment over the reconfiguration intervalτ\tauasδτ=Δ​ϕ​(t+τ)−Δ​ϕ​(t).\delta_{\tau}=\Delta\phi(t+\tau)-\Delta\phi(t).(17)

After removal of any deterministic offset over the considered interval, the
increment is modeled locally as zero mean:𝔼​[δτ]=0,Qτ=Var⁡(δτ).\mathbb{E}[\delta_{\tau}]=0,\qquad Q_{\tau}=\operatorname{Var}(\delta_{\tau}).(18)

All drift penalties derived below are written directly in terms ofQτQ_{\tau}. For the Gaussian state-space and Monte Carlo calculations, the
increment at a selected delay is represented asδτ∼𝒩​(0,Qτ).\delta_{\tau}\sim\mathcal{N}(0,Q_{\tau}).(19)

This local transition model is sufficient for the receiver analysis and does
not require a separate fit of a diffusion coefficient.

The relation between the two optical paths and the relative-phase increment is
also useful. Ifδτ,a=ϕa​(t+τ)−ϕa​(t),δτ,b=ϕb​(t+τ)−ϕb​(t),\delta_{\tau,a}=\phi_{a}(t+\tau)-\phi_{a}(t),\qquad\delta_{\tau,b}=\phi_{b}(t+\tau)-\phi_{b}(t),(20)

thenδτ=δτ,a−δτ,b,\delta_{\tau}=\delta_{\tau,a}-\delta_{\tau,b},(21)

and thereforeQτ\displaystyle Q_{\tau}=Var⁡(δτ,a)+Var⁡(δτ,b)\displaystyle=\operatorname{Var}(\delta_{\tau,a})+\operatorname{Var}(\delta_{\tau,b})−2​Cov⁡(δτ,a,δτ,b).\displaystyle\quad-2\operatorname{Cov}(\delta_{\tau,a},\delta_{\tau,b}).(22)

Common environmental motion can reduce the relative-phase uncertainty through
the covariance term, whereas independent perturbations add. Throughout the
paper,QτQ_{\tau}denotes the variance of the recovered relative-phase
increment, not that of one individual optical path.

Letϕ0=Δ​ϕ​(t),ϕ1=Δ​ϕ​(t+τ)=ϕ0+δτ.\phi_{0}=\Delta\phi(t),\qquad\phi_{1}=\Delta\phi(t+\tau)=\phi_{0}+\delta_{\tau}.(23)

Because both quadrature samples become available only after the second
acquisition, the estimation target isϕ1\phi_{1}.

## 3.1Measured phase-increment variance

The synchronized four-port data set reported in
Ref.[9]consists ofR=35R=35free-running recordings of
300 s duration, acquired at approximately 125 samples per second per channel.
For recordingrr, letϕ^(r)​[n]=unwrap⁡[atan2⁡(S(r)​[n],C(r)​[n])]\widehat{\phi}^{(r)}[n]=\operatorname{unwrap}\!\left[\operatorname{atan2}\!\left(S^{(r)}[n],C^{(r)}[n]\right)\right](24)

denote the reconstructed relative phase. For a sample separationmm, the
physical delay isτm=m​Δ​t\tau_{m}=m\Delta t, and the measured increments areδm(r)​[n]=ϕ^(r)​[n+m]−ϕ^(r)​[n].\delta_{m}^{(r)}[n]=\widehat{\phi}^{(r)}[n+m]-\widehat{\phi}^{(r)}[n].(25)

Consistently with Eq. (18), a deterministic
mean increment is removed separately from each recording:δ~m(r)​[n]\displaystyle\widetilde{\delta}_{m}^{(r)}[n]=δm(r)​[n]−δ¯m(r),\displaystyle=\delta_{m}^{(r)}[n]-\overline{\delta}_{m}^{(r)},(26)δ¯m(r)\displaystyle\overline{\delta}_{m}^{(r)}=1Nr−m​∑n=0Nr−m−1δm(r)​[n].\displaystyle=\frac{1}{N_{r}-m}\sum_{n=0}^{N_{r}-m-1}\delta_{m}^{(r)}[n].

A pooled observed increment variance is thenQ^τmobs=∑r=1R∑n=0Nr−m−1[δ~m(r)​[n]]2∑r=1R(Nr−m−1).\widehat{Q}_{\tau_{m}}^{\mathrm{obs}}=\frac{\displaystyle\sum_{r=1}^{R}\sum_{n=0}^{N_{r}-m-1}\left[\widetilde{\delta}_{m}^{(r)}[n]\right]^{2}}{\displaystyle\sum_{r=1}^{R}(N_{r}-m-1)}.(27)

If the reconstructed phase contains additive estimation noiseϵ(r)​[n]\epsilon^{(r)}[n], the observed variance also containsQτmmeas=Var⁡[ϵ(r)​[n+m]−ϵ(r)​[n]].Q_{\tau_{m}}^{\mathrm{meas}}=\operatorname{Var}\!\left[\epsilon^{(r)}[n+m]-\epsilon^{(r)}[n]\right].(28)

Under independence of the physical increment and the phase-reconstruction
noise,Q^τmobs≃Qτm+Qτmmeas.\widehat{Q}_{\tau_{m}}^{\mathrm{obs}}\simeq Q_{\tau_{m}}+Q_{\tau_{m}}^{\mathrm{meas}}.(29)

Thus, a calibrated measurement-noise contribution should be subtracted when it
is appreciable; without such a correction,Q^τmobs\widehat{Q}_{\tau_{m}}^{\mathrm{obs}}is a conservative empirical proxy forQτmQ_{\tau_{m}}. This construction connects the measured processor records to
the receiver theory without assuming Brownian diffusion, an
Ornstein–Uhlenbeck process, or any other prescribed delay-scaling law.

## 4Spatial and temporal readout

A spatial receiver produces both quadratures at the end time:Csp=cos⁡ϕ1,Ssp=sin⁡ϕ1,C_{\mathrm{sp}}=\cos\phi_{1},\qquad S_{\mathrm{sp}}=\sin\phi_{1},(30)

and ideally returnsϕ^sp=atan2⁡(Ssp,Csp)=ϕ1(mod​2​π).\widehat{\phi}_{\mathrm{sp}}=\operatorname{atan2}(S_{\mathrm{sp}},C_{\mathrm{sp}})=\phi_{1}\quad(\mathrm{mod}\ 2\pi).(31)

A temporal receiver measures one quadrature atttand the other att+τt+\tau. For the orderC→SC\rightarrow S,C0=cos⁡ϕ0,S1=sin⁡ϕ1,C_{0}=\cos\phi_{0},\qquad S_{1}=\sin\phi_{1},(32)

so thatϕ^C→S=atan2⁡(sin⁡ϕ1,cos⁡ϕ0).\widehat{\phi}_{C\rightarrow S}=\operatorname{atan2}(\sin\phi_{1},\cos\phi_{0}).(33)

For the reverse order,S0=sin⁡ϕ0,C1=cos⁡ϕ1,S_{0}=\sin\phi_{0},\qquad C_{1}=\cos\phi_{1},(34)

andϕ^S→C=atan2⁡(sin⁡ϕ0,cos⁡ϕ1).\widehat{\phi}_{S\rightarrow C}=\operatorname{atan2}(\sin\phi_{0},\cos\phi_{1}).(35)

Because both samples become available only after the second acquisition, the
estimation target isϕ1\phi_{1}. Numerical errors are evaluated circularly:e=Arg⁡[ei​(ϕ^−ϕ1)]∈[−π,π).e=\operatorname{Arg}\!\left[e^{i(\widehat{\phi}-\phi_{1})}\right]\in[-\pi,\pi).(36)

This prevents an artificial error of approximately2​π2\piwhen an estimate
and target lie on opposite sides of the principal branch cut.(a) Spatial readoutInput phaseϕ1\phi_{1}ParallelreceiverCsp=cos⁡ϕ1C_{\rm sp}=\cos\phi_{1}Ssp=sin⁡ϕ1S_{\rm sp}=\sin\phi_{1}Both quadratures describe the same instantaneous phase.(b) Temporal readoutInput phaseϕ0\phi_{0}Setting 1C0=cos⁡ϕ0C_{0}=\cos\phi_{0}Reconfigurationdelayτ\tauInput phaseϕ1=ϕ0+δτ\phi_{1}=\phi_{0}+\delta_{\tau}Setting 2S1=sin⁡ϕ1S_{1}=\sin\phi_{1}The estimate becomes available at the second time, so the target isϕ1\phi_{1}.Figure 2:Spatial and temporal quadrature acquisition. The temporal example
shows the orderC→SC\rightarrow S.

## 5Detailed fixed-order drift calculation

The local differential ofθ=atan2⁡(y,x)\theta=\operatorname{atan2}(y,x)isd​θ=x​d​y−y​d​xx2+y2.d\theta=\frac{x\,dy-y\,dx}{x^{2}+y^{2}}.(37)

This identity provides a direct derivation of the sequential-measurement error.

## 5.1OrderC→SC\rightarrow S

In theC→SC\rightarrow Sordering, the cosine quadrature is measured at the
initial timet0t_{0}, whereas the sine quadrature is measured at the later timet1=t0+τt_{1}=t_{0}+\tau. During this interval, the phase changes fromϕ0\phi_{0}toϕ1=ϕ0+δτ.\phi_{1}=\phi_{0}+\delta_{\tau}.(38)

Consequently, the two measured quadratures do not correspond to the same
instantaneous phase. The phase estimator instead receives the pairx=cos⁡ϕ0,y=sin⁡(ϕ0+δτ),x=\cos\phi_{0},\qquad y=\sin(\phi_{0}+\delta_{\tau}),(39)

and returnsϕ^C→S=atan2⁡(sin⁡(ϕ0+δτ),cos⁡ϕ0).\widehat{\phi}_{C\rightarrow S}=\operatorname{atan2}\left(\sin(\phi_{0}+\delta_{\tau}),\cos\phi_{0}\right).(40)

To obtain the small-drift behavior, expand the delayed sine measurement aboutδτ=0\delta_{\tau}=0:y\displaystyle y=sin⁡(ϕ0+δτ)\displaystyle=\sin(\phi_{0}+\delta_{\tau})(41)=sin⁡ϕ0+δτ​cos⁡ϕ0−δτ22​sin⁡ϕ0+O​(δτ3).\displaystyle=\sin\phi_{0}+\delta_{\tau}\cos\phi_{0}-\frac{\delta_{\tau}^{2}}{2}\sin\phi_{0}+O(\delta_{\tau}^{3}).(42)

The cosine measurement is taken before the drift and therefore remains fixed:x=cos⁡ϕ0.x=\cos\phi_{0}.(43)

Thus, to first order,d​x=0,d​y=cos⁡ϕ0​δτ.dx=0,\qquad dy=\cos\phi_{0}\,\delta_{\tau}.(44)

Atδτ=0\delta_{\tau}=0, the measurement point is(x,y)=(cos⁡ϕ0,sin⁡ϕ0),(x,y)=(\cos\phi_{0},\sin\phi_{0}),(45)

for whichx2+y2=cos2⁡ϕ0+sin2⁡ϕ0=1.x^{2}+y^{2}=\cos^{2}\phi_{0}+\sin^{2}\phi_{0}=1.(46)

Using the differential of the two-argument arctangent,d​ϕ^=x​d​y−y​d​xx2+y2,d\widehat{\phi}=\frac{x\,dy-y\,dx}{x^{2}+y^{2}},(47)

givesd​ϕ^C→S\displaystyle d\widehat{\phi}_{C\rightarrow S}=cos⁡ϕ0​(cos⁡ϕ0​δτ)−sin⁡ϕ0​(0)1\displaystyle=\frac{\cos\phi_{0}\left(\cos\phi_{0}\,\delta_{\tau}\right)-\sin\phi_{0}(0)}{1}(48)=cos2⁡ϕ0​δτ.\displaystyle=\cos^{2}\phi_{0}\,\delta_{\tau}.(49)

Therefore, provided that the drift is sufficiently small that noatan2\operatorname{atan2}branch crossing occurs,ϕ^C→S=ϕ0+δτ​cos2⁡ϕ0+O​(δτ2).\widehat{\phi}_{C\rightarrow S}=\phi_{0}+\delta_{\tau}\cos^{2}\phi_{0}+O(\delta_{\tau}^{2}).(50)

The desired reference is the phase at the end of the measurement interval,ϕ1=ϕ0+δτ\phi_{1}=\phi_{0}+\delta_{\tau}, rather than the initial phaseϕ0\phi_{0}.
The end-time estimation error is thereforeeC→S\displaystyle e_{C\rightarrow S}=ϕ^C→S−ϕ1\displaystyle=\widehat{\phi}_{C\rightarrow S}-\phi_{1}(51)=(ϕ0+δτ​cos2⁡ϕ0)−(ϕ0+δτ)+O​(δτ2)\displaystyle=\left(\phi_{0}+\delta_{\tau}\cos^{2}\phi_{0}\right)-\left(\phi_{0}+\delta_{\tau}\right)+O(\delta_{\tau}^{2})(52)=δτ​(cos2⁡ϕ0−1)+O​(δτ2)\displaystyle=\delta_{\tau}\left(\cos^{2}\phi_{0}-1\right)+O(\delta_{\tau}^{2})(53)=−δτ​sin2⁡ϕ0+O​(δτ2).\displaystyle=-\delta_{\tau}\sin^{2}\phi_{0}+O(\delta_{\tau}^{2}).(54)

This result has a direct interpretation. Nearϕ0=0\phi_{0}=0orπ\pi, the delayed sine measurement is highly sensitive to
the phase drift, and the reconstructed phase follows the end-time phase to
first order. In contrast, nearϕ0=π/2\phi_{0}=\pi/2or3​π/23\pi/2, the sine quadrature is locally insensitive to
the drift, and the estimate remains closer to the initial phase. The resulting
end-time error is therefore weighted bysin2⁡ϕ0\sin^{2}\phi_{0}.

Retaining the quadratic terms in both the delayed quadrature and the nonlinearatan2\operatorname{atan2}estimator givesϕ^C→S=\displaystyle\widehat{\phi}_{C\rightarrow S}=ϕ0+δτ​cos2⁡ϕ0\displaystyle\ \phi_{0}+\delta_{\tau}\cos^{2}\phi_{0}(55)−δτ2​[12​sin⁡(2​ϕ0)+18​sin⁡(4​ϕ0)]+O​(δτ3).\displaystyle-\delta_{\tau}^{2}\left[\frac{1}{2}\sin(2\phi_{0})+\frac{1}{8}\sin(4\phi_{0})\right]+O(\delta_{\tau}^{3}).(56)

This second-order correction describes the first departure from the linear
small-drift approximation and is therefore useful for interpreting deviations
of the simulations from the small-QQprediction.

## 5.2OrderS→CS\rightarrow C

In the reverseS→CS\rightarrow Cordering, the sine quadrature is measured at
the initial timet0t_{0}, while the cosine quadrature is measured after the
phase has changed toϕ0+δτ\phi_{0}+\delta_{\tau}. The estimator therefore receivesx=cos⁡(ϕ0+δτ),y=sin⁡ϕ0,x=\cos(\phi_{0}+\delta_{\tau}),\qquad y=\sin\phi_{0},(57)

and returnsϕ^S→C=atan2⁡(sin⁡ϕ0,cos⁡(ϕ0+δτ)).\widehat{\phi}_{S\rightarrow C}=\operatorname{atan2}\left(\sin\phi_{0},\cos(\phi_{0}+\delta_{\tau})\right).(58)

Expanding the delayed cosine measurement givesx\displaystyle x=cos⁡(ϕ0+δτ)\displaystyle=\cos(\phi_{0}+\delta_{\tau})(59)=cos⁡ϕ0−δτ​sin⁡ϕ0−δτ22​cos⁡ϕ0+O​(δτ3),\displaystyle=\cos\phi_{0}-\delta_{\tau}\sin\phi_{0}-\frac{\delta_{\tau}^{2}}{2}\cos\phi_{0}+O(\delta_{\tau}^{3}),(60)

whereas the earlier sine measurement remains fixed:y=sin⁡ϕ0.y=\sin\phi_{0}.(61)

Hence, to first order,d​x=−sin⁡ϕ0​δτ,d​y=0.dx=-\sin\phi_{0}\,\delta_{\tau},\qquad dy=0.(62)

Substitution into the differential ofatan2\operatorname{atan2}yieldsd​ϕ^S→C\displaystyle d\widehat{\phi}_{S\rightarrow C}=cos⁡ϕ0​(0)−sin⁡ϕ0​(−sin⁡ϕ0​δτ)1\displaystyle=\frac{\cos\phi_{0}(0)-\sin\phi_{0}\left(-\sin\phi_{0}\,\delta_{\tau}\right)}{1}(63)=sin2⁡ϕ0​δτ.\displaystyle=\sin^{2}\phi_{0}\,\delta_{\tau}.(64)

The corresponding first-order estimate is thereforeϕ^S→C=ϕ0+δτ​sin2⁡ϕ0+O​(δτ2).\widehat{\phi}_{S\rightarrow C}=\phi_{0}+\delta_{\tau}\sin^{2}\phi_{0}+O(\delta_{\tau}^{2}).(65)

Subtracting the desired end-time phase giveseS→C\displaystyle e_{S\rightarrow C}=ϕ^S→C−ϕ1\displaystyle=\widehat{\phi}_{S\rightarrow C}-\phi_{1}(66)=δτ​(sin2⁡ϕ0−1)+O​(δτ2)\displaystyle=\delta_{\tau}\left(\sin^{2}\phi_{0}-1\right)+O(\delta_{\tau}^{2})(67)=−δτ​cos2⁡ϕ0+O​(δτ2).\displaystyle=-\delta_{\tau}\cos^{2}\phi_{0}+O(\delta_{\tau}^{2}).(68)

The behavior is complementary to that of theC→SC\rightarrow Sordering.
Nearϕ0=π/2\phi_{0}=\pi/2or3​π/23\pi/2, the delayed cosine quadrature is highly
sensitive to phase drift, so the estimate follows the end-time phase to first
order. Nearϕ0=0\phi_{0}=0orπ\pi, the delayed cosine quadrature is locally
insensitive to the drift, producing the larger end-time error represented by
the factorcos2⁡ϕ0\cos^{2}\phi_{0}.

Including the second-order terms givesϕ^S→C=\displaystyle\widehat{\phi}_{S\rightarrow C}=ϕ0+δτ​sin2⁡ϕ0\displaystyle\ \phi_{0}+\delta_{\tau}\sin^{2}\phi_{0}(69)+δτ2​[12​sin⁡(2​ϕ0)−18​sin⁡(4​ϕ0)]+O​(δτ3).\displaystyle+\delta_{\tau}^{2}\left[\frac{1}{2}\sin(2\phi_{0})-\frac{1}{8}\sin(4\phi_{0})\right]+O(\delta_{\tau}^{3}).(70)

As in theC→SC\rightarrow Scase, this quadratic term quantifies the leading
nonlinear correction when the phase drift is no longer negligibly small.

## 5.3Mean-square drift penalty

Because𝔼​[δτ]=0\mathbb{E}[\delta_{\tau}]=0, both first-order errors have zero mean.
Using𝔼​[δτ2]=Qτ\mathbb{E}[\delta_{\tau}^{2}]=Q_{\tau},DC→S\displaystyle D_{C\rightarrow S}=𝔼​[eC→S2]=Qτ​𝔼​[sin4⁡ϕ0]+O​(Qτ2),\displaystyle=\mathbb{E}[e_{C\rightarrow S}^{2}]=Q_{\tau}\,\mathbb{E}[\sin^{4}\phi_{0}]+O(Q_{\tau}^{2}),(71a)DS→C\displaystyle D_{S\rightarrow C}=𝔼​[eS→C2]=Qτ​𝔼​[cos4⁡ϕ0]+O​(Qτ2).\displaystyle=\mathbb{E}[e_{S\rightarrow C}^{2}]=Q_{\tau}\,\mathbb{E}[\cos^{4}\phi_{0}]+O(Q_{\tau}^{2}).(71b)

For a uniform phase on[0,2​π)[0,2\pi),𝔼​[sin4⁡ϕ0]\displaystyle\mathbb{E}[\sin^{4}\phi_{0}]=12​π​∫02​πsin4⁡ϕ​d​ϕ\displaystyle=\frac{1}{2\pi}\int_{0}^{2\pi}\sin^{4}\phi\,d\phi(72)=12​π​∫02​π3−4​cos⁡2​ϕ+cos⁡4​ϕ8​𝑑ϕ\displaystyle=\frac{1}{2\pi}\int_{0}^{2\pi}\frac{3-4\cos 2\phi+\cos 4\phi}{8}\,d\phi(73)=38.\displaystyle=\frac{3}{8}.(74)

The cosine integral is identical. HenceDfixed=3​Qτ8+O​(Qτ2),D_{\mathrm{fixed}}=\frac{3Q_{\tau}}{8}+O(Q_{\tau}^{2}),(75)

and the leading drift-only rms error isRMSEfixed≃3​Qτ8.\operatorname{RMSE}_{\mathrm{fixed}}\simeq\sqrt{\frac{3Q_{\tau}}{8}}.(76)

## 6Phase-predicted adaptive ordering

Equations (54) and (68) show that the
coefficient multiplying the unknown drift depends on phase. If a predictorϕp\phi_{\mathrm{p}}forϕ0\phi_{0}is available from the preceding tracking
cycle, the first-order rule is{C→S,sin2⁡ϕp≤cos2⁡ϕp,S→C,sin2⁡ϕp>cos2⁡ϕp.\begin{cases}C\rightarrow S,&\sin^{2}\phi_{\mathrm{p}}\leq\cos^{2}\phi_{\mathrm{p}},\\
S\rightarrow C,&\sin^{2}\phi_{\mathrm{p}}>\cos^{2}\phi_{\mathrm{p}}.\end{cases}(77)

With perfect prediction, the squared drift coefficient ismin⁡(sin4⁡ϕ0,cos4⁡ϕ0)\min(\sin^{4}\phi_{0},\cos^{4}\phi_{0}). Symmetry divides the full phase interval
into eight equivalent sectors, or equivalently four copies of[0,π/4][0,\pi/4]. Thus𝔼​[min⁡(sin4⁡ϕ,cos4⁡ϕ)]\displaystyle\mathbb{E}[\min(\sin^{4}\phi,\cos^{4}\phi)]=4π​∫0π/4sin4⁡ϕ​d​ϕ\displaystyle=\frac{4}{\pi}\int_{0}^{\pi/4}\sin^{4}\phi\,d\phi(78)=4π​[3​ϕ8−sin⁡2​ϕ4+sin⁡4​ϕ32]0π/4\displaystyle=\frac{4}{\pi}\left[\frac{3\phi}{8}-\frac{\sin 2\phi}{4}+\frac{\sin 4\phi}{32}\right]_{0}^{\pi/4}(79)=4π​(3​π32−14)\displaystyle=\frac{4}{\pi}\left(\frac{3\pi}{32}-\frac{1}{4}\right)(80)=38−1π.\displaystyle=\frac{3}{8}-\frac{1}{\pi}.(81)

ThereforeDadaptive=(38−1π)​Qτ+O​(Qτ2).D_{\mathrm{adaptive}}=\left(\frac{3}{8}-\frac{1}{\pi}\right)Q_{\tau}+O(Q_{\tau}^{2}).(82)

Numerically, the coefficient is 0.05669 rather than 0.375. The relative MSE
reduction is1−3/8−1/π3/8=0.8488,1-\frac{3/8-1/\pi}{3/8}=0.8488,(83)

or 84.9%. The corresponding rms reduction is 61.1%.Figure 3:Phase-dependent drift coefficients for the two fixed
quadrature orders and the adaptive minimum. The vertical dashed
lines indicate the ordering boundaries. The uniform-phase mean
coefficient decreases from0.3750.375to0.05670.0567, corresponding to
an84.9%84.9\%reduction in drift-induced mean-square error.

## 6.1Fisher-information interpretation

Assume independent Gaussian quadrature noise with phase-independent
variancesvCv_{C}andvSv_{S}. For a measurementY∼𝒩​(μ​(ϕ),v)Y\sim\mathcal{N}(\mu(\phi),v), the Fisher information is defined asI​(ϕ)=𝔼​[(∂∂ϕ​ln⁡p​(Y∣ϕ))2]=[μ′​(ϕ)]2v.I(\phi)=\mathbb{E}\!\left[\left(\frac{\partial}{\partial\phi}\ln p(Y\mid\phi)\right)^{2}\right]=\frac{[\mu^{\prime}(\phi)]^{2}}{v}.(84)

Applying Eq. (84) to the cosine and sine
quadratures givesIC​(ϕ)=sin2⁡ϕvC,IS​(ϕ)=cos2⁡ϕvS.I_{C}(\phi)=\frac{\sin^{2}\phi}{v_{C}},\qquad I_{S}(\phi)=\frac{\cos^{2}\phi}{v_{S}}.(85)

For equal variances, Eq. (77) therefore measures the
less informative quadrature first and preserves the more informative
quadrature for the end time. With unequal noise variances, the generalized
ordering rule is obtained by comparing the full information valuesIC​(ϕp)I_{C}(\phi_{p})andIS​(ϕp)I_{S}(\phi_{p}), rather than onlysin2⁡ϕp\sin^{2}\phi_{p}andcos2⁡ϕp\cos^{2}\phi_{p}.

## 7Increment-aware end-time estimation

## 7.1Local phase observations from nonlinear quadratures

The local Gaussian estimator begins by converting a quadrature sample into a
phase observation around a predictorϕ¯\bar{\phi}. Linearizing the cosine
measurement givesC~\displaystyle\widetilde{C}≃cos⁡ϕ¯−sin⁡ϕ¯​(ϕ−ϕ¯)+nC,\displaystyle\simeq\cos\bar{\phi}-\sin\bar{\phi}(\phi-\bar{\phi})+n_{C},(86)

so thatzC=ϕ¯−C~−cos⁡ϕ¯sin⁡ϕ¯≃ϕ+ϵC,z_{C}=\bar{\phi}-\frac{\widetilde{C}-\cos\bar{\phi}}{\sin\bar{\phi}}\simeq\phi+\epsilon_{C},(87)

withVar⁡(ϵC)=vCsin2⁡ϕ¯=IC−1.\operatorname{Var}(\epsilon_{C})=\frac{v_{C}}{\sin^{2}\bar{\phi}}=I_{C}^{-1}.(88)

Similarly,zS=ϕ¯+S~−sin⁡ϕ¯cos⁡ϕ¯≃ϕ+ϵS,Var⁡(ϵS)=IS−1.z_{S}=\bar{\phi}+\frac{\widetilde{S}-\sin\bar{\phi}}{\cos\bar{\phi}}\simeq\phi+\epsilon_{S},\qquad\operatorname{Var}(\epsilon_{S})=I_{S}^{-1}.(89)

These equations make explicit where the local phase observations and Fisher
informations enter the estimator.

## 7.2Marginalization of the phase increment

Consider the orderC→SC\rightarrow S. The stale and fresh local observations
arezC=ϕ0+ϵC,zS=ϕ1+ϵS,z_{C}=\phi_{0}+\epsilon_{C},\qquad z_{S}=\phi_{1}+\epsilon_{S},(90)

withϕ1=ϕ0+w,w∼𝒩​(0,Qτ).\phi_{1}=\phi_{0}+w,\qquad w\sim\mathcal{N}(0,Q_{\tau}).(91)

Rewriting the stale observation in terms of the desired end-time state giveszC=ϕ1+(ϵC−w).z_{C}=\phi_{1}+(\epsilon_{C}-w).(92)

The two independent terms in parentheses have variancesIC−1I_{C}^{-1}andQτQ_{\tau}. ThereforezC∣ϕ1∼𝒩​(ϕ1,IC−1+Qτ).z_{C}\mid\phi_{1}\sim\mathcal{N}\left(\phi_{1},I_{C}^{-1}+Q_{\tau}\right).(93)

The information carried by the stale observation aboutϕ1\phi_{1}isIC,eff=1IC−1+Qτ=IC1+IC​Qτ.I_{C,\mathrm{eff}}=\frac{1}{I_{C}^{-1}+Q_{\tau}}=\frac{I_{C}}{1+I_{C}Q_{\tau}}.(94)

The effective information is bounded above by1/Qτ1/Q_{\tau}: even an
arbitrarily accurate measurement ofϕ0\phi_{0}cannot predictϕ1\phi_{1}more
accurately than the unknown process increment permits.

Combining the independent fresh and stale likelihoods givesϕ^1,C→S=IS​zS+IC,eff​zCIS+IC,eff,\widehat{\phi}_{1,C\rightarrow S}=\frac{I_{S}z_{S}+I_{C,\mathrm{eff}}z_{C}}{I_{S}+I_{C,\mathrm{eff}}},(95)

withMSEC→S,IA=1IS+IC/(1+IC​Qτ).\operatorname{MSE}_{C\rightarrow S,\mathrm{IA}}=\frac{1}{I_{S}+I_{C}/(1+I_{C}Q_{\tau})}.(96)

For the reverse order,MSES→C,IA=1IC+IS/(1+IS​Qτ).\operatorname{MSE}_{S\rightarrow C,\mathrm{IA}}=\frac{1}{I_{C}+I_{S}/(1+I_{S}Q_{\tau})}.(97)

The information lost when a measurement becomes stale isΔ​I​(I,Qτ)=I−I1+I​Qτ=I2​Qτ1+I​Qτ.\Delta I(I,Q_{\tau})=I-\frac{I}{1+IQ_{\tau}}=\frac{I^{2}Q_{\tau}}{1+IQ_{\tau}}.(98)

Because∂Δ​I/∂I>0\partial\Delta I/\partial I>0, delaying a highly informative
quadrature is more costly than delaying a weak one. The increment-aware
calculation therefore gives the same ordering principle as
Section6.

For equal information,IC=IS=II_{C}=I_{S}=I,MSEIA=1+I​QτI​(2+I​Qτ).\operatorname{MSE}_{\mathrm{IA}}=\frac{1+IQ_{\tau}}{I(2+IQ_{\tau})}.(99)

Its limits areMSEIA→{1/(2​I),Qτ→0,1/I,Qτ→∞.\operatorname{MSE}_{\mathrm{IA}}\rightarrow\begin{cases}1/(2I),&Q_{\tau}\rightarrow 0,\\
1/I,&Q_{\tau}\rightarrow\infty.\end{cases}(100)

For comparison, a static equal-weight estimatorϕ^=(zC+zS)/2\widehat{\phi}=(z_{C}+z_{S})/2hasMSEstatic=12​I+Qτ4,\operatorname{MSE}_{\mathrm{static}}=\frac{1}{2I}+\frac{Q_{\tau}}{4},(101)

which continues to trust the stale measurement even when the uncertainty of
the intervening phase change is dominant.

For equal raw quadrature-noise variances, directatan2\operatorname{atan2}already implements the ordinary static Fisher weights
to first order. The new factor in Eq. (94) is not a
replacement for that geometric weighting; it is the additional loss of
information caused by temporal phase evolution.

## 7.3Circular nonlinear implementation

The local equations fail near a quadrature extremum and do not represent phase
wrapping. The numerical study therefore also uses a circular posterior. ForC→SC\rightarrow S,c0=cos⁡ϕ0+nC,s1=sin⁡ϕ1+nS.c_{0}=\cos\phi_{0}+n_{C},\qquad s_{1}=\sin\phi_{1}+n_{S}.(102)

With a uniform circular prior and wrapped-Gaussian transition densityWQτW_{Q_{\tau}},p​(ϕ1∣c0,s1)∝p​(s1∣ϕ1)​∫−ππWQτ​(ϕ1−ϕ0)​p​(c0∣ϕ0)​𝑑ϕ0.p(\phi_{1}\mid c_{0},s_{1})\propto p(s_{1}\mid\phi_{1})\int_{-\pi}^{\pi}W_{Q_{\tau}}(\phi_{1}-\phi_{0})p(c_{0}\mid\phi_{0})\,d\phi_{0}.(103)

The computation used in the simulations consists of four steps. First, the
phase interval is sampled on an equally spaced grid. Second, the stale
likelihoodp​(c0∣ϕ0)p(c_{0}\mid\phi_{0})is propagated to the end time by circular
convolution withWQτW_{Q_{\tau}}. Third, the propagated density is multiplied
by the fresh likelihoodp​(s1∣ϕ1)p(s_{1}\mid\phi_{1})and normalized. Finally, the
estimate is the circular posterior meanϕ^1=arg⁡[∫−ππei​ϕ1​p​(ϕ1∣c0,s1)​𝑑ϕ1].\widehat{\phi}_{1}=\arg\!\left[\int_{-\pi}^{\pi}e^{i\phi_{1}}p(\phi_{1}\mid c_{0},s_{1})\,d\phi_{1}\right].(104)

On a Fourier grid, propagation is implemented efficiently by multiplying
harmonickkbyexp⁡(−k2​Qτ/2)\exp(-k^{2}Q_{\tau}/2). The small-error limit of this
circular procedure is Eq. (95).

## 8Photon resources and architecture criterion

A spatial–temporal comparison is meaningful only after the optical and
detection resources are specified. We first connect the abstract Fisher
information used in Section7to an ideal
shot-noise-limited measurement and then derive receiver-selection boundaries in
terms of the phase-increment varianceQτQ_{\tau}. No particular functional
dependence ofQτQ_{\tau}on the reconfiguration delay is required.

## 8.1Ideal balanced photon-counting benchmark

Consider a cosine-quadrature measurement implemented by two complementary
photon-counting outputs. LetΛC\Lambda_{C}be the signal photon number incident
on this quadrature measurement before detection loss, and letη\etadenote
the total detection efficiency. The two mean detected counts areλC,+​(ϕ)\displaystyle\lambda_{C,+}(\phi)=η​ΛC2​(1+cos⁡ϕ),\displaystyle=\frac{\eta\Lambda_{C}}{2}\left(1+\cos\phi\right),(105a)λC,−​(ϕ)\displaystyle\lambda_{C,-}(\phi)=η​ΛC2​(1−cos⁡ϕ).\displaystyle=\frac{\eta\Lambda_{C}}{2}\left(1-\cos\phi\right).(105b)

The measured counts are modeled as independent Poisson random variables,nC,+∼Poisson⁡(λC,+),nC,−∼Poisson⁡(λC,−).n_{C,+}\sim\operatorname{Poisson}(\lambda_{C,+}),\qquad n_{C,-}\sim\operatorname{Poisson}(\lambda_{C,-}).(106)

For independent Poisson observations, the Fisher information ofϕ\phiisIC​(ϕ)=∑k∈{+,−}1λC,k​(ϕ)​[∂λC,k​(ϕ)∂ϕ]2.I_{C}(\phi)=\sum_{k\in\{+,-\}}\frac{1}{\lambda_{C,k}(\phi)}\left[\frac{\partial\lambda_{C,k}(\phi)}{\partial\phi}\right]^{2}.(107)

Using∂λC,±∂ϕ=∓η​ΛC2​sin⁡ϕ,\frac{\partial\lambda_{C,\pm}}{\partial\phi}=\mp\frac{\eta\Lambda_{C}}{2}\sin\phi,(108)

we obtainIC​(ϕ)\displaystyle I_{C}(\phi)=η​ΛC2​sin2⁡ϕ​[11+cos⁡ϕ+11−cos⁡ϕ]\displaystyle=\frac{\eta\Lambda_{C}}{2}\sin^{2}\phi\left[\frac{1}{1+\cos\phi}+\frac{1}{1-\cos\phi}\right](109)=η​ΛC2​sin2⁡ϕ​2sin2⁡ϕ\displaystyle=\frac{\eta\Lambda_{C}}{2}\sin^{2}\phi\frac{2}{\sin^{2}\phi}(110)=η​ΛC.\displaystyle=\eta\Lambda_{C}.(111)

The expression at an exactly dark output is understood by continuity. The same
calculation for complementary sine outputs,λS,+​(ϕ)\displaystyle\lambda_{S,+}(\phi)=η​ΛS2​(1+sin⁡ϕ),\displaystyle=\frac{\eta\Lambda_{S}}{2}\left(1+\sin\phi\right),(112a)λS,−​(ϕ)\displaystyle\lambda_{S,-}(\phi)=η​ΛS2​(1−sin⁡ϕ),\displaystyle=\frac{\eta\Lambda_{S}}{2}\left(1-\sin\phi\right),(112b)

givesIS​(ϕ)=η​ΛS.I_{S}(\phi)=\eta\Lambda_{S}.(113)

Thus, in the ideal balanced Poisson model, the phase information of each
quadrature is independent of phase and equals the detected signal-photon
number allocated to that quadrature.

This result is used as a resource benchmark rather than as a detector model for
the processor recordings in Section2, which were
obtained from analog power measurements. For an actual receiver,ICI_{C}andISI_{S}should be calculated from its measured likelihood or inferred from its
calibrated noise statistics.

## 8.2Information-gain factor

LetIsp=IC(sp)+IS(sp)I_{\mathrm{sp}}=I_{C}^{(\mathrm{sp})}+I_{S}^{(\mathrm{sp})}(114)

denote the total Fisher information available to the simultaneous spatial
receiver during one complete phase-estimation cycle. The corresponding raw
information available to the temporal receiver isIt=IC(t)+IS(t).I_{\mathrm{t}}=I_{C}^{(\mathrm{t})}+I_{S}^{(\mathrm{t})}.(115)

We define the information-gain factorg=ItIsp.g=\frac{I_{\mathrm{t}}}{I_{\mathrm{sp}}}.(116)

The caseg=1g=1corresponds to equal total information per estimate. Under
that convention, temporal readout has no static information advantage and only
introduces temporal inconsistency. A valueg>1g>1must be justified by the
actual architecture, for example through reuse of detector channels, a longer
integration assigned to each sequential setting, or concentration of optical
power that would otherwise be divided among parallel outputs.

The high-information phase variance of anatan2\operatorname{atan2}estimate
follows from Eq. (37). Around the unit circle,d​ϕ=C​d​S−S​d​C,d\phi=C\,dS-S\,dC,(117)

and for independent quadrature noises,Var⁡(d​ϕ)=C2​vS+S2​vC.\operatorname{Var}(d\phi)=C^{2}v_{S}+S^{2}v_{C}.(118)

If the two quadratures have equal variancevv, the phase variance isvv,
independent of phase. Equivalently, an efficient receiver with total
informationIIhas the local benchmarkMSE≃1/I\operatorname{MSE}\simeq 1/I.

## 8.3Fixed and adaptive direct readout

Using the total-information convention above, the simultaneous spatial
benchmark isMSEsp≃1Isp.\operatorname{MSE}_{\mathrm{sp}}\simeq\frac{1}{I_{\mathrm{sp}}}.(119)

For fixed-order temporal readout, the corresponding leading expression isMSEt,fixed≃1g​Isp+3​Qτ8.\operatorname{MSE}_{\mathrm{t,fixed}}\simeq\frac{1}{gI_{\mathrm{sp}}}+\frac{3Q_{\tau}}{8}.(120)

Temporal readout is preferable whenIsp​Qτ<83​(1−1g),g>1.I_{\mathrm{sp}}Q_{\tau}<\frac{8}{3}\left(1-\frac{1}{g}\right),\qquad g>1.(121)

The productIsp​QτI_{\mathrm{sp}}Q_{\tau}is dimensionless and expresses the
competition between measurement information and the phase uncertainty acquired
between settings.

For ideal phase-predicted ordering,MSEt,adaptive≃1g​Isp+(38−1π)​Qτ,\operatorname{MSE}_{\mathrm{t,adaptive}}\simeq\frac{1}{gI_{\mathrm{sp}}}+\left(\frac{3}{8}-\frac{1}{\pi}\right)Q_{\tau},(122)

so the corresponding boundary isIsp​Qτ<1−1/g3/8−1/π.I_{\mathrm{sp}}Q_{\tau}<\frac{1-1/g}{3/8-1/\pi}.(123)

Because the adaptive drift coefficient is smaller, it tolerates a larger
phase-increment variance for the same static information gain.

## 8.4Symmetric local increment-aware boundary

The following boundary is an idealized local benchmark: it assumes that the
two local phase observations have equal, phase-independent information. For a
symmetric temporal receiver, let each raw quadrature carry informationJ=g​Isp2.J=\frac{gI_{\mathrm{sp}}}{2}.(124)

At the end time, the fresh quadrature retains informationJJ, while the stale
quadrature contributesJ/(1+J​Qτ)J/(1+JQ_{\tau}). ThereforeMSEt,IA=1J+J/(1+J​Qτ).\operatorname{MSE}_{\mathrm{t,IA}}=\frac{1}{J+J/(1+JQ_{\tau})}.(125)

For1<g<21<g<2, comparison with Eq. (119) yieldsIsp​Qτ<4​(g−1)g​(2−g).I_{\mathrm{sp}}Q_{\tau}<\frac{4(g-1)}{g(2-g)}.(126)

Forg=2g=2, the fresh quadrature alone carries the full spatial information,
and the stale quadrature provides an additional positive contribution for every
finiteQτQ_{\tau}. Forg>2g>2, the fresh temporal quadrature alone exceeds the
spatial information in this idealized resource convention. Such cases imply a
larger total measurement resource and must therefore be interpreted together
with the physical photon, time, and detector constraints.

The fully asymmetric local condition remainsIS(t)+IC(t)1+IC(t)​Qτ>IC(sp)+IS(sp)I_{S}^{(\mathrm{t})}+\frac{I_{C}^{(\mathrm{t})}}{1+I_{C}^{(\mathrm{t})}Q_{\tau}}>I_{C}^{(\mathrm{sp})}+I_{S}^{(\mathrm{sp})}(127)

forC→SC\rightarrow S, with the quadratures exchanged for the reverse order.

Figure4presents the three dimensionless
boundaries for the same information gaing=1.6g=1.6used in the numerical
receiver comparison. For this value,Isp​Qτ=1.00,3.75,6.61I_{\mathrm{sp}}Q_{\tau}=1.00,\quad 3.75,\quad 6.61(128)

for fixed, increment-aware, and ideal adaptive readout, respectively. Temporal
operation is favored below the relevant boundary and spatial operation above
it.Figure 4:Architecture-selection boundaries for information gaing=1.6g=1.6.
The horizontal and vertical variables are the simultaneous spatial Fisher
information and the phase-increment variance at the selected reconfiguration
interval. Temporal readout is favored below the boundary associated with its
estimator; spatial readout is favored above it. The increment-aware curve is
the symmetric local benchmark of Eq. (126). The
plot usesQτQ_{\tau}directly and does not require a prescribed delay-scaling
law.

## 8.5Model scope and detector nonidealities

The ideal photon-counting result in Eqs. (111)
and (113) neglects dark counts, background light,
afterpulsing, detector dead time, saturation, unequal channel efficiencies,
and technical intensity noise. These effects can make the Fisher information
phase dependent and can change the resource gaingg. They should be included
through the actual count likelihood or an experimentally calibrated noise
model. For analog power detection, the information should likewise be obtained
from the measured transfer slopes and covariance of the output powers.

The increment-aware expressions are local and presume that the phase posterior
is concentrated around a predictor. When the posterior spans several phase
branches or when a quadrature is operated near a locally singular linearization,
the circular estimator of Section7is required. The
quantityQτQ_{\tau}should be evaluated for the intended switching interval;
the architecture rules depend only on that increment uncertainty and do not
require extrapolation to other delays.

## 9Monte Carlo validation and design study

For compactness in this section,QQdenotes the phase-increment varianceQτQ_{\tau}associated with the selected reconfiguration interval. The first
numerical study sampledϕ0\phi_{0}uniformly on[−π,π)[-\pi,\pi), drewδτ∼𝒩​(0,Q)\delta_{\tau}\sim\mathcal{N}(0,Q), formed the exact mixed-time quadratures,
and evaluated Eqs. (33) and (35). The error in
each trial was wrapped according to Eq. (36), and the MSE
was the average of its square. Each value ofQQused5×1055\times 10^{5}trials.

Figure5confirms the fixed-order first-order
expression3​Q/83Q/8in the small-increment regime. The adaptive result approaches(3/8−1/π)​Q(3/8-1/\pi)QasQ→0Q\rightarrow 0. At largerQQ, the second-order terms
in Eqs. (56) and (70),
order-boundary changes, and circular branch effects produce the visible
departure from the first-order approximation.Figure 5:Exact end-time MSE for fixed and phase-adaptive quadrature ordering.
Markers are Monte Carlo results and lines are the first-order expressions.

A practical controller selects the order usingϕp=ϕ0+η\phi_{\mathrm{p}}=\phi_{0}+\eta, withη∼𝒩​(0,σp2)\eta\sim\mathcal{N}(0,\sigma_{p}^{2}). The second study usedQ=10−4Q=10^{-4}so
that higher-order drift effects were negligible, and estimated the normalized
coefficientD/QD/Qfrom7×1057\times 10^{5}trials per value ofσp\sigma_{p}.
Atσp=0.1\sigma_{p}=0.1rad, the coefficient is approximately 0.0631,
corresponding to an 83.2% reduction relative to the fixed-order value 0.375.
As the prediction becomes uninformative, the order is effectively random and
the coefficient returns to the fixed-order limit.Figure 6:Effect of prior phase uncertainty on adaptive ordering. The vertical
quantity is the drift-induced MSE divided byQQ.

The final study compares complete noisy receiver architectures. It usesvsp=10−2,g=1.6,vt=6.25×10−3.v_{\mathrm{sp}}=10^{-2},\qquad g=1.6,\qquad v_{\mathrm{t}}=6.25\times 10^{-3}.(129)

The adaptive receiver usesσp=0.1\sigma_{p}=0.1rad. Direct estimators use3×1053\times 10^{5}trials per point. The circular increment-aware estimator uses a
512-point phase grid and1.2×1041.2\times 10^{4}trials per point.

For equal quadrature-noise variances, the information values areIsp=1/vsp=100I_{\mathrm{sp}}=1/v_{\mathrm{sp}}=100andg=vsp/vt=1.6g=v_{\mathrm{sp}}/v_{\mathrm{t}}=1.6. Equation (121)
therefore givesQ⋆,fixed=83​Isp​(1−1g)=0.0100.Q_{\star,\mathrm{fixed}}=\frac{8}{3I_{\mathrm{sp}}}\left(1-\frac{1}{g}\right)=0.0100.(130)

The exact simulation gives the same fixed-order crossover. The circular
increment-aware estimator extends the crossing to approximately 0.0127, while
adaptive ordering extends it to approximately 0.0470 for the chosen prediction
error and measurement model. The increment-aware value should not be compared
directly with the local symmetric predictionQ⋆,IA=3.75/Isp=0.0375Q_{\star,\mathrm{IA}}=3.75/I_{\mathrm{sp}}=0.0375from
Eq. (126). That boundary assigns the constant
informationJ=g​Isp/2J=gI_{\mathrm{sp}}/2to each local phase observation, whereas
the circular simulation starts from noisy sine and cosine samples whose local
information varies with phase and vanishes at a quadrature extremum. The exact
nonlinear, phase-averaged comparison is therefore more conservative.Figure 7:Resource-normalized receiver comparison forvsp=0.01v_{\mathrm{sp}}=0.01,vt=0.00625v_{\mathrm{t}}=0.00625, andσp=0.1\sigma_{p}=0.1rad.

## 10Conclusion

We developed a detailed theory of spatial and sequential quadrature readout for
programmable photonic processors, motivated by the optical transformation and
measured phase statistics of an eight-mode processor. The four-port
configuration converts the relative phase of inputs 4 and 8 into complementary
sine and cosine power pairs, allowing the full phase to be reconstructed from
balanced differences.

When the desired estimate is the phase at the completion of the second
measurement, fixed-order temporalatan2\operatorname{atan2}reconstruction has
the first-order errors−δτ​sin2⁡ϕ0-\delta_{\tau}\sin^{2}\phi_{0}and−δτ​cos2⁡ϕ0-\delta_{\tau}\cos^{2}\phi_{0}. WritingQτ=Var⁡(δτ)Q_{\tau}=\operatorname{Var}(\delta_{\tau}), uniform phase averaging gives the
drift MSE3​Qτ/83Q_{\tau}/8. The detailed second-order expansions explain why exact
nonlinear simulations depart from the first-order result when the phase
increment becomes large.

A phase-predicted ordering rule measures the less informative quadrature first
and the more informative one second. Its uniform first-order MSE is(3/8−1/π)​Qτ(3/8-1/\pi)Q_{\tau}, an 84.9% reduction. An increment-aware state-space
derivation reaches the same ordering principle and shows that the information
of a stale measurement is reduced fromIItoI/(1+I​Qτ)I/(1+IQ_{\tau}). This
correction prevents an estimator from continuing to trust an old phase sample
after the uncertainty of the intervening phase change has become dominant.

The resulting crossover conditions separate the possible optical-information
advantage of temporal operation from the phase change accumulated during
reconfiguration. In an ideal balanced Poisson benchmark, each quadrature
contributes Fisher information equal to its detected signal-photon number. The
information-gain factorggthen produces explicit dimensionless boundaries
in the productIsp​QτI_{\mathrm{sp}}Q_{\tau}for fixed-order, symmetric local
increment-aware, and adaptive readout. Exact Monte Carlo simulations validate
the analytical laws, quantify robustness to prediction error, and show the
additional limitations introduced by nonlinear quadrature observations.
Previously acquired synchronized four-port records provide an empirical route
for estimatingQτQ_{\tau}at a selected delay. A physical implementation with
actual sequential reconfiguration would additionally include switching
transients, settling behavior, setting-dependent detection noise, and possible
power changes between the two measurements.

## Acknowledgments

This work was supported by the Federal Ministry of Research, Technology and
Space of Germany through the Q-TREX project under Grant 16KISR026 and the
QD-CamNetz project under Grant 16KISQ077, and by the Bavarian state government
through the Munich Quantum Valley under the Hightech Agenda Bayern Plus.

## Disclosures

The authors declare no conflicts of interest.

## Data availability

No new experimental data were acquired for this study. The processor
recordings analyzed here, together with the simulation code and numerical data
supporting the figures, are available from the authors upon reasonable request.

## References
- [1]M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani,
“Experimental realization of any discrete unitary operator,”Physical Review Letters73, 58–61 (1994),
doi: 10.1103/PhysRevLett.73.58.
- [2]W. R. Clements, P. C. Humphreys, B. J. Metcalf,
W. S. Kolthammer, and I. A. Walmsley,
“Optimal design for universal multiport interferometers,”Optica3, 1460–1465 (2016),
doi: 10.1364/OPTICA.3.001460.
- [3]N. C. Harris, D. Bunandar, M. Pant, G. R. Steinbrecher,
J. Mower, M. Prabhu, T. Baehr-Jones, M. Hochberg, and D. Englund,
“Large-scale quantum photonic circuits in silicon,”Nanophotonics5, 456–468 (2016),
doi: 10.1515/nanoph-2015-0146.
- [4]J. M. Arrazola, V. Bergholm, K. Brádlér,et al.,
“Quantum circuits with many photons on a programmable nanophotonic chip,”Nature591, 54–60 (2021),
doi: 10.1038/s41586-021-03202-1.
- [5]Q. Cheng, J. Kwon, M. Glick, M. Bahadori,
L. P. Carloni, and K. Bergman,
“Silicon photonics codesign for deep learning,”Proceedings of the IEEE108, 1261–1282 (2020),
doi: 10.1109/JPROC.2020.2968184.
- [6]W. Bogaerts, D. Pérez, J. Capmany,et al.,
“Programmable photonic circuits,”Nature586, 207–216 (2020),
doi: 10.1038/s41586-020-2764-0.
- [7]M. Kuschnerov, K. Piyawanno, M. S. Alfiad,
B. Spinnler, A. Napoli, and B. Lankl,
“Impact of mechanical vibrations on laser stability and carrier phase
estimation in coherent receivers,”IEEE Photonics Technology Letters22, 1114–1116 (2010),
doi: 10.1109/LPT.2010.2050472.
- [8]M. Seimetz,High-Order Modulation for Optical Fiber Transmission.
Berlin, Germany: Springer, 2009.
- [9]G. Elmas, I. A. Litvin, P. Kohl, and J. Nötzel,
“Modeling and analysis of phase instability in a photonic processor,”Applied Optics64, 3995–4003 (2025),
doi: 10.1364/AO.560370.
- [10]I. A. Litvin, G. Elmas, P. Kohl, and J. Nötzel,
“Stable signal processing with a photonic processor,”Journal of Lightwave Technology43, 9981–9990 (2025),
doi: 10.1109/JLT.2025.3606027.
- [11]I. A. Litvin, G. Elmas, K. H. El-Safty, S. Chaudhary, and J. Nötzel,
“Robust calibration and energy optimization in reconfigurable photonic
processors,”Optics Express33, 35011–35027 (2025),
doi: 10.1364/OE.566817.
- [12]I. A. Litvin, G. Elmas, P. Kohl, and J. Nötzel,
“Multi-input signal phase stabilization in photonic processors with on-chip
feedback control,”Optics Express34, 11244–11258 (2026),
doi: 10.1364/OE.579969.
- [13]I. A. Litvin, G. Elmas, and J. Nötzel,
“Joint detection on reconfigurable photonic processors with multi-input phase
stabilization,”IEEE Photonics Journal18(3), 1–9 (2026),
doi: 10.1109/JPHOT.2026.3683204.
- [14]N. C. Harris, J. Carolan, D. Bunandar, M. Prabhu,
M. Hochberg, T. Baehr-Jones, M. L. Fanto,
A. M. Smith, C. C. Tison, P. M. Alsing, and D. Englund,
“Linear programmable nanophotonic processors,”Optica5, 1623–1631 (2018),
doi: 10.1364/OPTICA.5.001623.
- [15]C. Taballione, T. A. W. Wolterink, J. M. Renema,
M. S. de Goede, B. J. Metcalf, P. P. Rohde,
H. S. M. T. Yung, M. A. de Dood, E. J. Klein,
D. J. Broeke, and K.-J. Boller,
“8×\times8 reconfigurable quantum photonic processor based on silicon
nitride waveguides,”Optics Express27, 26842–26857 (2019),
doi: 10.1364/OE.27.026842.
- [16]X. Qiang, X. Zhou, J. Wang, C. M. Wilkes, T. Loke,
S. O’Gara, L. Kling, G. D. Marshall, R. Santagati,
T. C. Ralph, J. B. Wang, J. L. O’Brien,
M. G. Thompson, and J. C. F. Matthews,
“Large-scale silicon quantum photonics implementing arbitrary two-qubit
processing,”Nature Photonics12, 534–539 (2018),
doi: 10.1038/s41566-018-0236-y.
- [17]J. W. Silverstone, D. Bonneau, J. L. O’Brien, and M. G. Thompson,
“Silicon quantum photonics,”IEEE Journal of Selected Topics in Quantum Electronics22,
390–402 (2016),
doi: 10.1109/JSTQE.2016.2573218.
- [18]B. J. Smith, D. Kundys, N. Thomas-Peter, P. G. R. Smith, and
I. A. Walmsley,
“Phase-controlled integrated photonic quantum circuits,”Optics Express17, 13516–13525 (2009),
doi: 10.1364/OE.17.013516.
- [19]V. Svarc, M. Nováková, M. Dudka, and M. Ježek,
“Sub-0.1 degree phase locking of a single-photon interferometer,”Optics Express31, 12562–12571 (2023),
doi: 10.1364/OE.487414.

## 


- 


Major funding support from
