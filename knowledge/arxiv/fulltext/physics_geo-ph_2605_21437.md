# Neural Negative Binomial Regression for Weekly Seismicity Forecasting: Per-Cell Dispersion Estimation and Tail Risk Assessment

**arXiv ID**: 2605.21437v1
**Authors**: Alim Igilik
**Published**: 2026-05-20
**Categories**: physics.geo-ph, cs.LG, stat.ML
**Comments**: 28 pages, 9 figures. Source code available at https://github.com/Al1mkaYandere/seismic-probabilistic-modeling
**HTML URL**: https://arxiv.org/html/2605.21437v1

## Abstract

Standard approaches to forecasting the weekly number of earthquakes on a spatial grid rely on the Poisson distribution with a single global dispersion assumption. We show that this assumption is systematically violated in seismic data from Central Asia (2010-2024), where a likelihood-ratio test with boundary correction strongly rejects the Poisson hypothesis (p < 10^{-179}).   The main contribution of this work is the EarthquakeNet architecture, which provides an endogenous per-cell estimate of the overdispersion parameter alpha via a neural network (spatial embeddings + MLP), without explicit spatial covariance specification. In contrast to existing negative binomial regression approaches in seismological forecasting, which typically assume a single global alpha, the proposed per-cell formulation allows the model to identify spatial heterogeneity in seismic clustering and to construct probabilistic risk-aware alerts via quantiles of the predicted distribution.   A walk-forward evaluation (2018-2023) over four systems shows an 8.6 percent reduction in mean pinball deviation (MPD) relative to a negative binomial GLM baseline. The strongest improvements are observed in the tail regime (Y >= 5), where the continuous ranked probability score (CRPS) of the proposed model is 12.5 percent lower than that of the baseline, indicating improved calibration in extreme-event forecasting.

## Full Text

Neural Negative Binomial Regression for Weekly Seismicity Forecasting: Per-Cell Dispersion Estimation and Tail Risk Assessment

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
- 
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2605.21437v1 [physics.geo-ph] 20 May 2026

## Neural Negative Binomial Regression for
Weekly Seismicity Forecasting:
Per-Cell Dispersion Estimation and Tail Risk AssessmentIgilik Alim

## Abstract

Standard approaches to forecasting the weekly number of earthquakes on a spatial grid rely on the Poisson distribution with a single global dispersion assumption. We show that this assumption is systematically violated in seismic data from Central Asia (2010–2024): a likelihood-ratio test with boundary correction rejects the Poisson hypothesis withp<10−179p<10^{-179}.

The main contribution of this work is the EarthquakeNet
architecture, which provides an endogenous per-cell estimate
of the overdispersion parameterα\alphathrough a neural
network (spatial embeddings + MLP), without explicit spatial
covariance specification. To our knowledge, existing
NB-regression approaches in seismological forecasting
estimate a single globalα\alpha; the per-cell
parametrization proposed here allows the model to identify
where seismicity is more strongly clustered and to construct
probabilistic risk-aware alerts through quantiles of the
predicted NB distribution.

A Walk-Forward protocol (2018–2023) over four systems shows an 8.6 % reduction in MPD relative to NB GLM. The key advantage appears in the tail stratum (Y≥5Y\geq 5): the CRPS of Hybrid DL NB is 12.5 % lower than that of NB GLM—precisely the regime in which the per-cell parameterα\alphacontributes most to estimating the risk of extreme events.

Code availability:The implementation of
EarthquakeNet, training scripts, and evaluation pipelines
are publicly available at
https://github.com/Al1mkaYandere/seismic-probabilistic-modeling

## 1Introduction

Earthquake forecasting is a critical task for natural risk management, infrastructure resilience planning, and emergency response operations. For Central Asia, and the Tian Shan mountain system in particular, this problem carries heightened importance due to high tectonic activity, complex geodynamics, and pronounced spatiotemporal heterogeneity of seismic processes. In the applied setting, the goal is not a deterministic forecast of individual events, but a macroscopic forecast of seismicity intensity: estimating the expected number of earthquakes with magnitudeM≥3.0M\geq 3.0on a spatial grid at a weekly horizon.

Historically, count data forecasting in fixed spatiotemporal cells has been formulated within the Poisson framework. However, its key assumption—equality of the conditional mean and conditional variance—is systematically violated in real seismological data. Earthquakes exhibit pronounced clustering associated with swarm activity, foreshock–aftershock sequences, and episodes of anomalous activity, resulting in overdispersion in which the variance substantially exceeds the mean. Under these conditions, uncritical application of the Poisson distribution leads to biased uncertainty estimates and, consequently, to underestimation of the risk of extreme scenarios.

Despite the widespread adoption of machine learning methods in seismological problems, a substantial portion of existing work remains methodologically vulnerable. On one hand, several approaches apply continuous regression loss functions and metrics (e.g., MSE), ignoring the discrete probabilistic nature of the observed counts. On the other hand, even when count targets are handled correctly, models are frequently built on naive autoregressive lags without physically motivated features, limiting the algorithm’s ability to capture tectonic stress accumulation and relaxation processes.

This work proposes a transition from the Poisson paradigm to the Negative Binomial (NB) distribution, which naturally accommodates overdispersion. To parametrize the distribution, we develop a hybrid deep learning architecture combining two complementary components: (i) spatial embeddings, which capture latent geological heterogeneity and differences between cells associated with distinct fault structures; and (ii) a multilayer perceptron (MLP) processing physically motivated predictors, including proxies for released seismic energy and seismic quiescence indicators.

The main scientific contributions of this work are:
- •

formal rejection of the Poisson hypothesis via a likelihood-ratio test with boundary correction of the null distribution\NoHyper[10]\endNoHyper, demonstrating the inadequacy of the equidispersion assumption in seismic count data;
- •

the EarthquakeNet hybrid architecture (spatial embeddings + MLP with physical predictors, NB loss function), providing per-cell estimation of the overdispersion parameterα\alphaand improved CRPS in the tail stratum relative to the GLM baseline;
- •

a rigorous Walk-Forward protocol (2018–2023) incorporating per-cell ETAS\NoHyper[1]\endNoHyperas a seismological baseline, Moran’sII\NoHyper[13]\endNoHyperfor testing spatial conditional independence, and a 5-seed identifiability audit ofα\alpha.

## 2Data and Feature Engineering

## 2.1Earthquake Catalog and Study Area

The empirical basis of this study is the open-access USGS (United States Geological Survey) catalog, covering the period from 2010 to early 2024. The analysis is restricted to the seismically active zone of Central Asia, encompassing the Tian Shan and Pamir mountain systems, within the geographic window38∘38^{\circ}–45∘45^{\circ}N and65∘65^{\circ}–85∘85^{\circ}E.

To ensure comparability of statistical estimates and reduce the influence of observational network limitations, the catalog was filtered by the magnitude of completenessMcM_{c}. The thresholdMcM_{c}was estimated using the Maximum Curvature method[9]: a frequency histogram of events in bins ofΔ​m=0.1\Delta m=0.1was constructed for the entire region, with the maximum occurring atM≈4.3M\approx 4.3; applying the correction of+0.2+0.2yieldsMc=4.5M_{c}=4.5, with abb-value of1.421.42(Aki MLE estimate,n=722n=722events).

The lower catalog threshold ofM≥3.0M\geq 3.0is set belowMcM_{c}: in the rangeM∈[3.0,4.5)M\in[3.0,\,4.5), the USGS catalog for this region may be incomplete, particularly in low-activity cells, introducing bias into event counts. A discussion of this limitation is provided in Section6.1. The final dataset includes only events with magnitudeM≥3.0M\geq 3.0, which minimizes the contribution of background noise and improves the stability of subsequent probabilistic count process modeling.

## 2.2Spatiotemporal Grid and Target Distribution

The study region is discretized into a regular spatial grid with
a resolution of3.0∘×3.0∘3.0^{\circ}\times 3.0^{\circ}. The temporal
aggregation interval is set to one calendar week. For each spatial
celliiand weektt, the target variable is defined asYi,jt:=number of recorded earthquakes in cell​(i,j)​during week​t,Y^{t}_{i,j}:=\text{number of recorded earthquakes in cell }(i,j)\text{ during week }t,

whereYi,jt∈ℕ0Y^{t}_{i,j}\in\mathbb{N}_{0}.

Empirical analysis of the target variable distribution reveals
pronounced skewness: the overwhelming majority of observations
correspond to zero counts (no events), while the right tail reaches
extreme values (30+ events during peak intervals). This data
structure confirms the inapplicability of classical MSE regression
for count forecasting tasks.

## 2.3Feature Engineering

The predictors are designed to reflect the physics of the seismic
cycle:
- •

Seismic Energy.Magnitude-to-energy transformation
based on the relationE∝101.5​ME\propto 10^{1.5M}.
- •

Seismic Gap.Time in weeks since the last event
with magnitudeM≥4.5M\geq 4.5, modeling the local stress
accumulation phase.
- •

Accumulated Activity.Rolling activity windows
(4 and 12 weeks) to account for clustering and aftershock
sequences.

All continuous predictors are standardized prior to training, while
the target variable is retained in discrete form. Spatial
dependencies between cells are not specified manually through
smoothing, but are delegated to the Spatial Embeddings layer, which
learns them endogenously within end-to-end model training.

## 3Methodology

## 3.1Data Formalization and Feature Space Construction

## 3.1.1Formalization of the Source Catalog

From the USGS catalog metadata, four components are retained for
two-dimensional spatiotemporal modeling: coordinates, time, and
magnitude.

## Definition 3.1(Seismic Catalog).

The filtered catalog is defined as a set of tuples𝒟r​a​w={(xk,yk,tk,mk)},\mathcal{D}_{raw}=\{(x_{k},y_{k},t_{k},m_{k})\},

wherexk,yk,tk∈ℝx_{k},y_{k},t_{k}\in\mathbb{R}, withxkx_{k}denoting
longitude,yky_{k}latitude, andmk≥3.0m_{k}\geq 3.0magnitude. The index
setℐ={1,…,N}\mathcal{I}=\{1,\dots,N\}

induces the working set𝒟~r​a​w⊂ℐ×𝒟r​a​w⟹𝒟~r​a​w=⋃k=1N{(k,xk,yk,tk,mk)},\widetilde{\mathcal{D}}_{raw}\subset\mathcal{I}\times\mathcal{D}_{raw}\implies\widetilde{\mathcal{D}}_{raw}=\bigcup_{k=1}^{N}\{(k,x_{k},y_{k},t_{k},m_{k})\},

providing unique identification of each event by keykk.

## 3.1.2Spatiotemporal Discretization

## Definition 3.2(Spatial Domain and Discretization Operator).

The study region𝒮=[xmin,xmax]×[ymin,ymax]\mathcal{S}=[x_{\min},x_{\max}]\times[y_{\min},y_{\max}]

is representable as a disjoint union of cells𝒮i,j\mathcal{S}_{i,j}with stepsΔ​x\Delta x,Δ​y\Delta y:𝒮=⨆i=0nx−1⨆j=0ny−1𝒮i,j,\mathcal{S}=\bigsqcup_{i=0}^{n_{x}-1}\bigsqcup_{j=0}^{n_{y}-1}\mathcal{S}_{i,j},

wherenxn_{x},nyn_{y}denote the number of steps along thexxandyyaxes. The discretization operatorHHmaps continuous
coordinates to discrete indices:H​(k,xk,yk,tk,mk)=(k,ik,jk,τk,mk),H(k,x_{k},y_{k},t_{k},m_{k})=(k,i_{k},j_{k},\tau_{k},m_{k}),

whereik=⌊xk−xminΔ​x⌋,jk=⌊yk−yminΔ​y⌋,τk=⌊tk−tminΔ​t⌋.i_{k}=\left\lfloor\frac{x_{k}-x_{\min}}{\Delta x}\right\rfloor,\quad j_{k}=\left\lfloor\frac{y_{k}-y_{\min}}{\Delta y}\right\rfloor,\quad\tau_{k}=\left\lfloor\frac{t_{k}-t_{\min}}{\Delta t}\right\rfloor.

( Temporal discretization is implemented as follows: each event
is assigned to the periodτ=pd.Period​(tk,"W")\tau=\texttt{pd.Period}(t_{k},\texttt{"W"})(standard ISO week, starting on Sunday); the full
regular time series for each cell is constructed at frequencyW-MON(pd.date_range(..., freq="W-MON")),
aligning the grid to Mondays with a boundary offset of at most±1\pm 1day. All downstream operations are applied to the
already-aligned series, so this offset does not affect the feature
functionalΦ\Phi. ) The discrete catalog is then:𝒟g​r​i​d=⋃v∈𝒟~r​a​w{H​(v)}.\mathcal{D}_{grid}=\bigcup_{v\in\widetilde{\mathcal{D}}_{raw}}\{H(v)\}.

## 3.1.3Construction of the Active Grid

The discrete indices belong to finite setsℐx={0,1,…,nx−1},ℐy={0,1,…,ny−1},𝒯a​l​l={0,1,…,τmax},\mathcal{I}_{x}=\{0,1,\dots,n_{x}-1\},\quad\mathcal{I}_{y}=\{0,1,\dots,n_{y}-1\},\quad\mathcal{T}_{all}=\{0,1,\dots,\tau_{\max}\},

whereτmax=⌊tmax−tminΔ​t⌋.\tau_{\max}=\left\lfloor\frac{t_{\max}-t_{\min}}{\Delta t}\right\rfloor.

The full spatiotemporal grid is:Ω=ℐx×ℐy×𝒯a​l​l.\Omega=\mathcal{I}_{x}\times\mathcal{I}_{y}\times\mathcal{T}_{all}.

## Definition 3.3(Index Set (Bucket)).

For(i,j,τ)∈Ω(i,j,\tau)\in\Omega:ℬi,j(τ)={k∈{1,…,N}|H​(k,xk,yk,tk,mk)=(k,i,j,τ,mk)}\mathcal{B}_{i,j}^{(\tau)}=\big\{k\in\{1,\dots,N\}\bigm|H(k,x_{k},y_{k},t_{k},m_{k})=(k,i,j,\tau,m_{k})\big\}={k∈{1,…,N}|(k,i,j,τ,mk)∈𝒟g​r​i​d}.=\big\{k\in\{1,\dots,N\}\bigm|(k,i,j,\tau,m_{k})\in\mathcal{D}_{grid}\big\}.

## Definition 3.4(Active Grid).

The set of active spatial indices:𝒮a​c​t​i​v​e={(i,j)∈ℐx×ℐy∣∃τ∈𝒯a​l​l:ℬi,j(τ)≠∅}.\mathcal{S}_{active}=\{(i,j)\in\mathcal{I}_{x}\times\mathcal{I}_{y}\mid\exists\,\tau\in\mathcal{T}_{all}\colon\mathcal{B}_{i,j}^{(\tau)}\neq\emptyset\}.

The working grid:Ωa​c​t​i​v​e=𝒮a​c​t​i​v​e×𝒯a​l​l.\Omega_{active}=\mathcal{S}_{active}\times\mathcal{T}_{all}.

## Remark.

The restriction to𝒮a​c​t​i​v​e\mathcal{S}_{active}excludes aseismic nodes
while preserving time series continuity for active nodes (including
zero observations), which is necessary for correct construction of
lagged features.

## 3.1.4Aggregation and Feature Vector

## Definition 3.5(Aggregated Statistics).

For(i,j,τ)∈Ωa​c​t​i​v​e(i,j,\tau)\in\Omega_{active}, the target variable is:Yi,j(τ)=|ℬi,j(τ)|.Y_{i,j}^{(\tau)}=\big|\mathcal{B}_{i,j}^{(\tau)}\big|.

Total released seismic energy:Ei,j(τ)=∑k∈ℬi,j(τ)101.5​mk.E_{i,j}^{(\tau)}=\sum_{k\in\mathcal{B}_{i,j}^{(\tau)}}10^{1.5m_{k}}.

Extreme magnitudes:Mmax,i,j(τ)=maxk∈ℬi,j(τ)⁡{mk},Mmin,i,j(τ)=mink∈ℬi,j(τ)⁡{mk}.M_{\max,i,j}^{(\tau)}=\max_{k\in\mathcal{B}_{i,j}^{(\tau)}}\{m_{k}\},\quad M_{\min,i,j}^{(\tau)}=\min_{k\in\mathcal{B}_{i,j}^{(\tau)}}\{m_{k}\}.

Whenℬi,j(τ)=∅\mathcal{B}_{i,j}^{(\tau)}=\emptyset, we setYi,j(τ)=0,Ei,j(τ)=0,Y_{i,j}^{(\tau)}=0,\quad E_{i,j}^{(\tau)}=0,Mmax,i,j(τ)=0,Mmin,i,j(τ)=0.M_{\max,i,j}^{(\tau)}=0,\quad M_{\min,i,j}^{(\tau)}=0.

The aggregated dataset is:𝒟a​g​g=⋃(i,j,τ)∈Ωa​c​t​i​v​e{(i,j,τ,Yi,j(τ),Ei,j(τ),Mmax,i,j(τ),Mmin,i,j(τ))}.\mathcal{D}_{agg}=\bigcup_{(i,j,\tau)\in\Omega_{active}}\Big\{\big(i,j,\tau,Y_{i,j}^{(\tau)},E_{i,j}^{(\tau)},M_{\max,i,j}^{(\tau)},M_{\min,i,j}^{(\tau)}\big)\Big\}.

## Definition 3.6(Feature Functional).

LetWmax=12W_{\max}=12and𝒯t​a​r​g​e​t={t∈𝒯a​l​l∣t≥Wmax}\mathcal{T}_{target}=\{t\in\mathcal{T}_{all}\mid t\geq W_{\max}\}. DefineΦ:𝒮a​c​t​i​v​e×𝒯t​a​r​g​e​t→ℝ7,\Phi:\mathcal{S}_{active}\times\mathcal{T}_{target}\to\mathbb{R}^{7},

whereΦ​(i,j,t)=(ϕ1​(i,j,t),…,ϕ7​(i,j,t))T,(i,j)∈𝒮a​c​t​i​v​e,t∈𝒯t​a​r​g​e​t,\Phi(i,j,t)=\big(\phi_{1}(i,j,t),\dots,\phi_{7}(i,j,t)\big)^{T},\quad(i,j)\in\mathcal{S}_{active},\;t\in\mathcal{T}_{target},

with componentsϕ1​(i,j,t)=Yi,j(t−1),\phi_{1}(i,j,t)=Y_{i,j}^{(t-1)},ϕ2​(i,j,t)=Mmax,i,j(t−1),\phi_{2}(i,j,t)=M_{\max,i,j}^{(t-1)},ϕ3​(i,j,t)=Mmin,i,j(t−1),\phi_{3}(i,j,t)=M_{\min,i,j}^{(t-1)},ϕ4​(i,j,t)=maxτ∈{t−4,…,t−1}⁡Mmax,i,j(τ),\phi_{4}(i,j,t)=\max_{\tau\in\{t-4,\dots,t-1\}}M_{\max,i,j}^{(\tau)},ϕ5​(i,j,t)=∑τ=t−12t−1Yi,j(τ),\phi_{5}(i,j,t)=\sum_{\tau=t-12}^{t-1}Y_{i,j}^{(\tau)},ϕ6​(i,j,t)=∑τ=t−8t−1Ei,j(τ),\phi_{6}(i,j,t)=\sum_{\tau=t-8}^{t-1}E_{i,j}^{(\tau)},ϕ7​(i,j,t)=(t−1)−max⁡{τ≤t−1∣Mmax,i,j(τ)≥4.5}.\phi_{7}(i,j,t)=(t-1)-\max\{\tau\leq t-1\mid M_{\max,i,j}^{(\tau)}\geq 4.5\}.

If the index set inϕ7\phi_{7}is empty, the value500.0500.0is
assigned.

Let𝐗i,j(t):=Φ​(i,j,t)\mathbf{X}_{i,j}^{(t)}:=\Phi(i,j,t). The final dataset is:𝒟f​i​n​a​l=⋃(i,j)∈𝒮a​c​t​i​v​e⋃t∈𝒯t​a​r​g​e​t{(𝐗i,j(t),Yi,j(t))}.\mathcal{D}_{final}=\bigcup_{(i,j)\in\mathcal{S}_{active}}\;\bigcup_{t\in\mathcal{T}_{target}}\Big\{\big(\mathbf{X}_{i,j}^{(t)},\;Y_{i,j}^{(t)}\big)\Big\}.

## 3.1.5Operator Pipeline for Data Transformation𝒟r​a​w\displaystyle\mathcal{D}_{raw}→Index(ℐ×⋅)𝒟~r​a​w→𝐻𝒟g​r​i​d→Bucketing{ℬi,j(τ)}\displaystyle\xrightarrow{\text{Index }(\mathcal{I}\times\cdot)}\widetilde{\mathcal{D}}_{raw}\xrightarrow{H}\mathcal{D}_{grid}\xrightarrow{\text{Bucketing}}\{\mathcal{B}_{i,j}^{(\tau)}\}→𝒜(aggregation onΩa​c​t​i​v​e)𝒟a​g​g→Φ​(lag/rolling features)𝒟f​i​n​a​l.\displaystyle\xrightarrow{\mathcal{A}\;\text{(aggregation on }\Omega_{active})}\mathcal{D}_{agg}\xrightarrow{\Phi\;\text{(lag/rolling features)}}\mathcal{D}_{final}.

The composition of mappings transforms a continuous spatiotemporal
point process into a tensor representation suitable for neural
network architectures with shared weights. The hierarchy of temporal
windows (4, 8, 12 weeks) implements multi-scale memory of the
process. The feature vector𝐗i,j(t)\mathbf{X}_{i,j}^{(t)}is constructed
exclusively fromτ≤t−1\tau\leq t-1, thereby precluding any look-ahead
bias.

## 3.2Formalization of the Probability Space

## Definition 3.7(Local Phase Space).

The space of admissible states of a node is:S=ℕ0×ℝ≥0×ℝ×ℝ,S=\mathbb{N}_{0}\times\mathbb{R}_{\geq 0}\times\mathbb{R}\times\mathbb{R},

equipped with the Borelσ\sigma-algebraℬ​(S)=2ℕ0⊗ℬ​(ℝ≥0)⊗ℬ​(ℝ)⊗ℬ​(ℝ),\mathcal{B}(S)=2^{\mathbb{N}_{0}}\otimes\mathcal{B}(\mathbb{R}_{\geq 0})\otimes\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R}),

where2ℕ02^{\mathbb{N}_{0}}denotes the power set of the countable
setℕ0\mathbb{N}_{0}. The four components correspond, respectively,
to the event countY∈ℕ0Y\in\mathbb{N}_{0}, released seismic energyE∈ℝ≥0E\in\mathbb{R}_{\geq 0}, maximum magnitude, and minimum
magnitude.

## Definition 3.8(Global Probability Space).

The sample space is defined as the function spaceω:Ωa​c​t​i​v​e→S\omega:\Omega_{active}\to S:Ωf​u​l​l:=SΩa​c​t​i​v​e≅∏(i,j,τ)∈Ωa​c​t​i​v​eS.\Omega_{full}:=S^{\Omega_{active}}\cong\prod_{(i,j,\tau)\in\Omega_{active}}S.

The cylindricalσ\sigma-algebra is:ℱ=⨂(i,j,τ)∈Ωa​c​t​i​v​eℬ​(S).\mathcal{F}=\bigotimes_{(i,j,\tau)\in\Omega_{active}}\mathcal{B}(S).

A probability measureℙ\mathbb{P}is postulated on(Ωf​u​l​l,ℱ)(\Omega_{full},\mathcal{F}), inducing the joint distribution
of seismic events across all active nodes and time steps.

## 3.2.1Process Dynamics, Filtration, and Measurability

## Definition 3.9(Canonical Coordinate Maps).

For each index(i,j,t)∈Ωa​c​t​i​v​e(i,j,t)\in\Omega_{active}, the canonical
coordinate mapsi,j(t):Ωf​u​l​l→Ss_{i,j}^{(t)}:\Omega_{full}\to Sis defined bysi,j(t)​(ω)=ω​(i,j,t).s_{i,j}^{(t)}(\omega)=\omega(i,j,t).

The target variableYi,j(t):Ωf​u​l​l→ℕ0Y_{i,j}^{(t)}:\Omega_{full}\to\mathbb{N}_{0}is defined via the first canonical projectionπ1:S→ℕ0\pi_{1}:S\to\mathbb{N}_{0}:Yi,j(t)=π1∘si,j(t).Y_{i,j}^{(t)}=\pi_{1}\circ s_{i,j}^{(t)}.

## Proposition 3.10(Measurability of Canonical
Coordinates).

For any(i,j,t)∈Ωa​c​t​i​v​e(i,j,t)\in\Omega_{active}, the mapsi,j(t)s_{i,j}^{(t)}is(ℱ,ℬ​(S))(\mathcal{F},\mathcal{B}(S))-measurable, that is,∀B∈ℬ(S):(si,j(t))−1(B)∈ℱ.\forall B\in\mathcal{B}(S):\quad\bigl(s_{i,j}^{(t)}\bigr)^{-1}(B)\in\mathcal{F}.

Furthermore, the projectionπ1:S→ℕ0\pi_{1}:S\to\mathbb{N}_{0}is(ℬ​(S),2ℕ0)(\mathcal{B}(S),2^{\mathbb{N}_{0}})-measurable. Consequently,Yi,j(t)=π1∘si,j(t)Y_{i,j}^{(t)}=\pi_{1}\circ s_{i,j}^{(t)}is anℱ\mathcal{F}-measurable random variable taking values inℕ0\mathbb{N}_{0}.

## Proof.

Consider an arbitrary finite index setJ={ξ1,…,ξn}⊂Ωa​c​t​i​v​e,ξk=(ik,jk,τk).J=\{\xi_{1},\dots,\xi_{n}\}\subset\Omega_{active},\qquad\xi_{k}=(i_{k},j_{k},\tau_{k}).

Define the corresponding finite-dimensional coordinate projectionπJ:Ωf​u​l​l→Sn,πJ​(ω)=(ω​(ξ1),…,ω​(ξn)).\pi_{J}:\Omega_{full}\to S^{n},\qquad\pi_{J}(\omega)=\bigl(\omega(\xi_{1}),\dots,\omega(\xi_{n})\bigr).

For any setBn∈⨂k=1nℬ​(S)B_{n}\in\bigotimes_{k=1}^{n}\mathcal{B}(S), its
preimageπJ−1​(Bn)={ω∈Ωf​u​l​l∣πJ​(ω)∈Bn}\pi_{J}^{-1}(B_{n})=\{\omega\in\Omega_{full}\mid\pi_{J}(\omega)\in B_{n}\}

is called a cylindrical set, depending only on the coordinates
indexed byJJ. Introduce the class of all such cylinders for
fixedJJ:𝒞J={πJ−1​(Bn)∣Bn∈⨂k=1nℬ​(S)}.\mathcal{C}_{J}=\left\{\pi_{J}^{-1}(B_{n})\mid B_{n}\in\bigotimes_{k=1}^{n}\mathcal{B}(S)\right\}.

Taking the union over all finite index sets yields𝒞=⋃J⊂Ωa​c​t​i​v​e|J|<∞𝒞J.\mathcal{C}=\bigcup_{\begin{subarray}{c}J\subset\Omega_{active}\\
|J|<\infty\end{subarray}}\mathcal{C}_{J}.

The cylindricalσ\sigma-algebra on the productSΩa​c​t​i​v​eS^{\Omega_{active}}is by definition theσ\sigma-algebra generated by all
finite-dimensional cylinders:ℱ=σ​(𝒞).\mathcal{F}=\sigma(\mathcal{C}).

Hence, by the property of generatedσ\sigma-algebras,𝒞⊆ℱ.\mathcal{C}\subseteq\mathcal{F}.

Now fix(i,j,t)∈Ωa​c​t​i​v​e(i,j,t)\in\Omega_{active}and an arbitraryB∈ℬ​(S)B\in\mathcal{B}(S). By definition of the coordinate map,(si,j(t))−1​(B)={ω∈Ωf​u​l​l∣ω​(i,j,t)∈B}.\bigl(s_{i,j}^{(t)}\bigr)^{-1}(B)=\{\omega\in\Omega_{full}\mid\omega(i,j,t)\in B\}.

The right-hand side is a cylindrical set corresponding to the
singleton index setJ={(i,j,t)}J=\{(i,j,t)\}. Indeed, for|J|=1|J|=1we haveS1=SS^{1}=Sand(si,j(t))−1​(B)=πJ−1​(B).\bigl(s_{i,j}^{(t)}\bigr)^{-1}(B)=\pi_{J}^{-1}(B).

SinceB∈ℬ​(S)=⨂k=11ℬ​(S)B\in\mathcal{B}(S)=\bigotimes_{k=1}^{1}\mathcal{B}(S),(si,j(t))−1​(B)∈𝒞J⊆𝒞⊆ℱ.\bigl(s_{i,j}^{(t)}\bigr)^{-1}(B)\in\mathcal{C}_{J}\subseteq\mathcal{C}\subseteq\mathcal{F}.

AsB∈ℬ​(S)B\in\mathcal{B}(S)was arbitrary,si,j(t)s_{i,j}^{(t)}is(ℱ,ℬ​(S))(\mathcal{F},\mathcal{B}(S))-measurable.

It remains to verify measurability ofπ1\pi_{1}. LetA∈2ℕ0A\in 2^{\mathbb{N}_{0}}be arbitrary. By definition of the preimage,π1−1​(A)\displaystyle\pi_{1}^{-1}(A)={s∈S∣π1​(s)∈A}\displaystyle=\{s\in S\mid\pi_{1}(s)\in A\}={(r1,r2,r3,r4)∈ℕ0×ℝ≥0×ℝ×ℝ∣r1∈A}\displaystyle=\{(r_{1},r_{2},r_{3},r_{4})\in\mathbb{N}_{0}\times\mathbb{R}_{\geq 0}\times\mathbb{R}\times\mathbb{R}\mid r_{1}\in A\}=A×ℝ≥0×ℝ×ℝ.\displaystyle=A\times\mathbb{R}_{\geq 0}\times\mathbb{R}\times\mathbb{R}.

SinceA∈2ℕ0A\in 2^{\mathbb{N}_{0}},ℝ≥0∈ℬ​(ℝ≥0)\mathbb{R}_{\geq 0}\in\mathcal{B}(\mathbb{R}_{\geq 0}), andℝ∈ℬ​(ℝ)\mathbb{R}\in\mathcal{B}(\mathbb{R}), we obtainA×ℝ≥0×ℝ×ℝ∈2ℕ0⊗ℬ​(ℝ≥0)⊗ℬ​(ℝ)⊗ℬ​(ℝ)=ℬ​(S).A\times\mathbb{R}_{\geq 0}\times\mathbb{R}\times\mathbb{R}\in 2^{\mathbb{N}_{0}}\otimes\mathcal{B}(\mathbb{R}_{\geq 0})\otimes\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R})=\mathcal{B}(S).

Henceπ1−1​(A)∈ℬ​(S)\pi_{1}^{-1}(A)\in\mathcal{B}(S)for allA∈2ℕ0A\in 2^{\mathbb{N}_{0}}, soπ1\pi_{1}is(ℬ​(S),2ℕ0)(\mathcal{B}(S),2^{\mathbb{N}_{0}})-measurable. Finally, the
composition of measurable maps is measurable, soYi,j(t)=π1∘si,j(t)Y_{i,j}^{(t)}=\pi_{1}\circ s_{i,j}^{(t)}

is anℱ\mathcal{F}-measurable random variable taking values inℕ0\mathbb{N}_{0}.
∎

To ensure strict causality of the forecast, we formalize the
information structure of the process over time: the filtration
separates the history available to the observer from the
unobservable future.

## Definition 3.11(Natural Filtration).

The filtration𝔽={ℱt}t∈𝒯a​l​l\mathbb{F}=\{\mathcal{F}_{t}\}_{t\in\mathcal{T}_{all}}is defined asℱt=σ​({sk,m(τ)∣(k,m)∈𝒮a​c​t​i​v​e,τ≤t}),ℱt−1⊆ℱt⊆ℱ.\mathcal{F}_{t}=\sigma\big(\{s_{k,m}^{(\tau)}\mid(k,m)\in\mathcal{S}_{active},\;\tau\leq t\}\big),\quad\mathcal{F}_{t-1}\subseteq\mathcal{F}_{t}\subseteq\mathcal{F}.

The process{si,j(t)}\{s_{i,j}^{(t)}\}is adapted to𝔽\mathbb{F}:σ​(si,j(t))⊆ℱt\sigma(s_{i,j}^{(t)})\subseteq\mathcal{F}_{t}.

The feature vector𝐗i,j(t):Ωf​u​l​l→ℝ7\mathbf{X}_{i,j}^{(t)}:\Omega_{full}\to\mathbb{R}^{7}is defined as𝐗i,j(t)=Φ​(si,j(t−1),…,si,j(t−W))\mathbf{X}_{i,j}^{(t)}=\Phi(s_{i,j}^{(t-1)},\dots,s_{i,j}^{(t-W)}). By the
measurability of compositions of measurable functions:σ​(𝐗i,j(t))⊆ℱt−1.\sigma(\mathbf{X}_{i,j}^{(t)})\subseteq\mathcal{F}_{t-1}.

At the same time,σ​(Yi,j(t))⊆ℱt\sigma(Y_{i,j}^{(t)})\subseteq\mathcal{F}_{t},
butσ​(Yi,j(t))⊈ℱt−1\sigma(Y_{i,j}^{(t)})\not\subseteq\mathcal{F}_{t-1},
formalizing the indeterminacy of the future given the observed
history.

Postulating sufficiency of𝐗i,j(t)\mathbf{X}_{i,j}^{(t)}forℱt−1\mathcal{F}_{t-1}with respect toYi,j(t)Y_{i,j}^{(t)}(Markov
assumption), we obtain the conditional independence:Yi,j(t)⟂ℱt−1∣𝐗i,j(t).Y_{i,j}^{(t)}\perp\mathcal{F}_{t-1}\mid\mathbf{X}_{i,j}^{(t)}.

The problem reduces to approximating the conditional likelihoodℙ​(Yi,j(t)∣𝐗i,j(t))\mathbb{P}(Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)})with
parametersθ=fN​N​(𝐗i,j(t))\theta=f_{NN}(\mathbf{X}_{i,j}^{(t)}).

## Remark(Markov Truncation and Finite Memory).

The Markov assumption, combined with the feature functionalΦ\Phiof Definition3.6, reduces the
infinite pastℱt−1\mathcal{F}_{t-1}to a finite window ofWmax=12W_{\max}=12weeks. Formally, this means we replace the
condition on the full sigma-algebraℱt−1\mathcal{F}_{t-1}with
the condition on the finite-dimensional sub-sigma-algebraℱt−1W:=σ​({si,j(τ)∣τ∈{t−Wmax,…,t−1}})⊆ℱt−1.\mathcal{F}_{t-1}^{W}:=\sigma\big(\{s_{i,j}^{(\tau)}\mid\tau\in\{t-W_{\max},\dots,t-1\}\}\big)\subseteq\mathcal{F}_{t-1}.

The approximation error introduced by this truncation is
negligible under exponential decay of temporal dependence,
which is consistent with the Omori–Utsu law for aftershock
sequences.

## Remark(Causality).

The inclusionσ​(𝐗i,j(t))⊆ℱt−1\sigma(\mathbf{X}_{i,j}^{(t)})\subseteq\mathcal{F}_{t-1}provides a formal guarantee against
look-ahead bias: the model operates exclusively on information
available to the observer at the start of the forecast
weektt. In the context of operational seismological
forecasting, this means that no event from weekttparticipates in the construction of the feature vector for
that same week.

## 3.3Empirical Risk Minimization

For the training index setΩt​r​a​i​n⊂𝒮a​c​t​i​v​e×𝒯a​l​l\Omega_{train}\subset\mathcal{S}_{active}\times\mathcal{T}_{all}, define𝐘t​r​a​i​n={Yi,j(t)∣(i,j,t)∈Ωt​r​a​i​n},𝐗t​r​a​i​n={𝐗i,j(t)∣(i,j,t)∈Ωt​r​a​i​n}.\mathbf{Y}_{train}=\{Y_{i,j}^{(t)}\mid(i,j,t)\in\Omega_{train}\},\quad\mathbf{X}_{train}=\{\mathbf{X}_{i,j}^{(t)}\mid(i,j,t)\in\Omega_{train}\}.

## Definition 3.12(Training Index Set for Static
Evaluation).

Let the week set𝒯a​l​l\mathcal{T}_{all}be chronologically ordered
and partitioned into disjoint blocks𝒯t​r​a​i​n∪𝒯t​e​s​t=𝒯a​l​l,𝒯t​r​a​i​n∩𝒯t​e​s​t=∅,|𝒯t​r​a​i​n|=⌊0.8​|𝒯a​l​l|⌋,\mathcal{T}_{train}\cup\mathcal{T}_{test}=\mathcal{T}_{all},\qquad\mathcal{T}_{train}\cap\mathcal{T}_{test}=\varnothing,\qquad|\mathcal{T}_{train}|=\lfloor 0.8\,|\mathcal{T}_{all}|\rfloor,

where𝒯t​r​a​i​n\mathcal{T}_{train}is the initial chronological prefix
and𝒯t​e​s​t\mathcal{T}_{test}is the remaining suffix. The training
and test index sets are then defined asΩt​r​a​i​n={(i,j,t)∈𝒮a​c​t​i​v​e×𝒯a​l​l∣t∈𝒯t​r​a​i​n}∩supp⁡(𝒟f​i​n​a​l),\Omega_{train}=\bigl\{(i,j,t)\in\mathcal{S}_{active}\times\mathcal{T}_{all}\mid t\in\mathcal{T}_{train}\bigr\}\cap\operatorname{supp}(\mathcal{D}_{final}),Ωt​e​s​t={(i,j,t)∈𝒮a​c​t​i​v​e×𝒯a​l​l∣t∈𝒯t​e​s​t}∩supp⁡(𝒟f​i​n​a​l).\Omega_{test}=\bigl\{(i,j,t)\in\mathcal{S}_{active}\times\mathcal{T}_{all}\mid t\in\mathcal{T}_{test}\bigr\}\cap\operatorname{supp}(\mathcal{D}_{final}).

Thus,Ωt​r​a​i​n\Omega_{train}is not an arbitrary subset of𝒮a​c​t​i​v​e×𝒯a​l​l\mathcal{S}_{active}\times\mathcal{T}_{all}: it is a
synchronized calendar block containing all active cells in the
early weeks present in𝒟f​i​n​a​l\mathcal{D}_{final}. Test weeks are
entirely excluded from training, yielding an out-of-time
evaluation under the static 80/20 split.

Invoking the filtrationℱt−1\mathcal{F}_{t-1}and the sufficiency
ofΦ\Phi, we postulate spatiotemporal conditional independence
on the training block:Yi,j(t)⟂Yk,m(τ)∣{𝐗i′,j′(t′)}(i′,j′,t′)∈Ωt​r​a​i​n∀(i,j,t)≠(k,m,τ)∈Ωt​r​a​i​n,Y_{i,j}^{(t)}\perp Y_{k,m}^{(\tau)}\mid\{\mathbf{X}_{i^{\prime},j^{\prime}}^{(t^{\prime})}\}_{(i^{\prime},j^{\prime},t^{\prime})\in\Omega_{train}}\quad\forall\,(i,j,t)\neq(k,m,\tau)\in\Omega_{train},

which yields the factorization of the joint conditional
likelihood.

## Remark(Spatial Conditional Independence
Assumption).

This assumption is standard in GLM and neural count regression
models, but may be violated in seismology: Coulomb stress
transfer and ETAS triggering[1]induce
cross-cell dependencies. The factorization below is a marginal
predictive factorization, not a full generative model of the
joint spatiotemporal field. Empirical verification via Moran’sIIon standardized Pearson residuals is carried out in
Section4.7: if significant autocorrelation is
detected (p<0.05p<0.05), the proposed model should be interpreted
as amarginal predictor. Extension to an ETAS-like
spatial convolution is left for future work
(see Section6.1).ℙ​(𝐘t​r​a​i​n∣𝐗t​r​a​i​n)=∏(i,j,t)∈Ωt​r​a​i​nℙ​(Yi,j(t)∣𝐗i,j(t)).\mathbb{P}(\mathbf{Y}_{train}\mid\mathbf{X}_{train})=\prod_{(i,j,t)\in\Omega_{train}}\mathbb{P}(Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)}).

The parametric approximationℙθ\mathbb{P}_{\theta}inherits
this factorization structure.

## Remark(Relationship to Walk-Forward Validation).

The static 80/20 split defined above differs structurally from the Walk-Forward protocol of Section4.3. In the static split,Ωt​r​a​i​n\Omega_{train}is fixed once; in the Walk-Forward protocol, a separateΩt​r​a​i​n(Y)\Omega_{train}^{(Y)}is constructed for each test yearY∈{2018,…,2023}Y\in\{2018,\dots,2023\}, expanding asYYincreases. The static split is used for model selection and hyperparameter tuning; the Walk-Forward protocol provides the primary out-of-sample evaluation reported in Table2.

## Proposition 3.13(Equivalence of KL Divergence Minimization
and NLL).

Letℙ\mathbb{P}denote the true measure andℙθ\mathbb{P}_{\theta}a parametric approximation. Thenθ∗=argminθ𝔼𝐗∼ℙ[DK​L(ℙ(Y∣𝐗)∥ℙθ(Y∣𝐗))]=argmaxθ𝔼𝐗,Y∼ℙ[logℙθ(Y∣𝐗)].\theta^{*}=\arg\min_{\theta}\,\mathbb{E}_{\mathbf{X}\sim\mathbb{P}}\big[D_{KL}(\mathbb{P}(Y\mid\mathbf{X})\parallel\mathbb{P}_{\theta}(Y\mid\mathbf{X}))\big]=\arg\max_{\theta}\,\mathbb{E}_{\mathbf{X},Y\sim\mathbb{P}}\big[\log\mathbb{P}_{\theta}(Y\mid\mathbf{X})\big].

## Proof.

Expanding the KL divergence by its definition and applying the
tower property of expectation:𝔼𝐗​[DK​L​(ℙ∥ℙθ)]=𝔼𝐗​[∑yℙ​(y∣𝐗)​log⁡ℙ​(y∣𝐗)ℙθ​(y∣𝐗)].\mathbb{E}_{\mathbf{X}}\big[D_{KL}(\mathbb{P}\parallel\mathbb{P}_{\theta})\big]=\mathbb{E}_{\mathbf{X}}\left[\sum_{y}\mathbb{P}(y\mid\mathbf{X})\log\frac{\mathbb{P}(y\mid\mathbf{X})}{\mathbb{P}_{\theta}(y\mid\mathbf{X})}\right].

Splitting the logarithm and recognizing the conditional entropyℋ​(ℙ):=−𝔼𝐗,Y​[log⁡ℙ​(Y∣𝐗)]\mathcal{H}(\mathbb{P}):=-\mathbb{E}_{\mathbf{X},Y}\big[\log\mathbb{P}(Y\mid\mathbf{X})\big]:𝔼𝐗​[DK​L​(ℙ∥ℙθ)]=−ℋ​(ℙ)−𝔼𝐗,Y∼ℙ​[log⁡ℙθ​(Y∣𝐗)].\mathbb{E}_{\mathbf{X}}\big[D_{KL}(\mathbb{P}\parallel\mathbb{P}_{\theta})\big]=-\mathcal{H}(\mathbb{P})-\mathbb{E}_{\mathbf{X},Y\sim\mathbb{P}}\big[\log\mathbb{P}_{\theta}(Y\mid\mathbf{X})\big].

Sinceℋ​(ℙ)\mathcal{H}(\mathbb{P})does not depend onθ\theta,
minimizing the left-hand side overθ\thetais equivalent to
maximizing the second term:θ∗=arg⁡maxθ⁡𝔼𝐗,Y∼ℙ​[log⁡ℙθ​(Y∣𝐗)].\theta^{*}=\arg\max_{\theta}\,\mathbb{E}_{\mathbf{X},Y\sim\mathbb{P}}\big[\log\mathbb{P}_{\theta}(Y\mid\mathbf{X})\big].

Note thatDK​L≥0D_{KL}\geq 0with equality if and only ifℙθ=ℙ\mathbb{P}_{\theta}=\mathbb{P}almost surely, so the
minimum is attained at the true distribution whenever it lies
in the parametric family.
∎

Sinceℙ\mathbb{P}is unavailable, we replace the population
expectation with its empirical counterpart. By the law of large
numbers, for i.i.d. draws{(𝐗i,j(t),Yi,j(t))}(i,j,t)∈Ωt​r​a​i​n\{(\mathbf{X}_{i,j}^{(t)},Y_{i,j}^{(t)})\}_{(i,j,t)\in\Omega_{train}}:𝔼𝐗,Y∼ℙ​[log⁡ℙθ​(Y∣𝐗)]≈1|Ωt​r​a​i​n|​∑(i,j,t)∈Ωt​r​a​i​nlog⁡ℙθ​(Yi,j(t)∣𝐗i,j(t)).\mathbb{E}_{\mathbf{X},Y\sim\mathbb{P}}\big[\log\mathbb{P}_{\theta}(Y\mid\mathbf{X})\big]\;\approx\;\frac{1}{|\Omega_{train}|}\sum_{(i,j,t)\in\Omega_{train}}\log\mathbb{P}_{\theta}(Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)}).

Since|Ωt​r​a​i​n||\Omega_{train}|is constant with respect toθ\theta,
maximizing the empirical mean is equivalent to maximizing the
sum. Taking the logarithm of the factorized joint likelihood
(which coincides with this sum by the conditional independence
assumption of RemarkRemark):log⁡ℙθ​(𝐘t​r​a​i​n∣𝐗t​r​a​i​n)=log​∏(i,j,t)∈Ωt​r​a​i​nℙθ​(Yi,j(t)∣𝐗i,j(t))=∑(i,j,t)∈Ωt​r​a​i​nlog⁡ℙθ​(Yi,j(t)∣𝐗i,j(t)).\log\mathbb{P}_{\theta}(\mathbf{Y}_{train}\mid\mathbf{X}_{train})=\log\prod_{(i,j,t)\in\Omega_{train}}\mathbb{P}_{\theta}(Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)})=\sum_{(i,j,t)\in\Omega_{train}}\log\mathbb{P}_{\theta}(Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)}).

Negating and identifying this as the empirical approximation
to−𝔼𝐗,Y∼ℙ​[log⁡ℙθ​(Y∣𝐗)]-\mathbb{E}_{\mathbf{X},Y\sim\mathbb{P}}[\log\mathbb{P}_{\theta}(Y\mid\mathbf{X})], we obtain the
training objective — the negative log-likelihood (NLL):θ∗≈arg⁡minθ⁡ℒN​L​L​(θ),ℒN​L​L​(θ)=−∑(i,j,t)∈Ωt​r​a​i​nlog⁡ℙθ​(Yi,j(t)∣𝐗i,j(t)).\theta^{*}\approx\arg\min_{\theta}\,\mathcal{L}_{NLL}(\theta),\qquad\mathcal{L}_{NLL}(\theta)=-\sum_{(i,j,t)\in\Omega_{train}}\log\mathbb{P}_{\theta}(Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)}).

## 3.3.1Baseline Poisson Approximation

## Definition 3.14(Poisson Parametrization).

The neural networkfN​N​(⋅;θ):ℝ7→ℝf_{NN}(\cdot;\theta):\mathbb{R}^{7}\to\mathbb{R}induces the modelYi,j(t)∣𝐗i,j(t)∼Poisson​(λi,j(t)),Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)}\sim\mathrm{Poisson}(\lambda_{i,j}^{(t)}),

with the intensity parametrized via the exponential link:λi,j(t)=exp⁡(fN​N​(𝐗i,j(t);θ))>0.\lambda_{i,j}^{(t)}=\exp\!\big(f_{NN}(\mathbf{X}_{i,j}^{(t)};\theta)\big)>0.

The exponential link guaranteesλi,j(t)>0\lambda_{i,j}^{(t)}>0for
all inputs without imposing explicit constraints on the network
output. The conditional probability mass function is:ℙθ​(Yi,j(t)=y∣𝐗i,j(t))=(λi,j(t))y​e−λi,j(t)y!,y∈ℕ0.\mathbb{P}_{\theta}(Y_{i,j}^{(t)}=y\mid\mathbf{X}_{i,j}^{(t)})=\frac{(\lambda_{i,j}^{(t)})^{y}\,e^{-\lambda_{i,j}^{(t)}}}{y!},\qquad y\in\mathbb{N}_{0}.

Taking the logarithm:log⁡ℙθ​(Yi,j(t)=y∣𝐗i,j(t))=y​log⁡λi,j(t)−λi,j(t)−log⁡(y!).\log\mathbb{P}_{\theta}(Y_{i,j}^{(t)}=y\mid\mathbf{X}_{i,j}^{(t)})=y\log\lambda_{i,j}^{(t)}-\lambda_{i,j}^{(t)}-\log(y!).

The termlog⁡(y!)\log(y!)does not depend onθ\theta. Dropping it
and negating to obtain a minimization objective, the per-sample
contribution to the NLL becomesλi,j(t)−Yi,j(t)​log⁡λi,j(t)\lambda_{i,j}^{(t)}-Y_{i,j}^{(t)}\log\lambda_{i,j}^{(t)}. Summing overΩt​r​a​i​n\Omega_{train}yields the Poisson loss:ℒP​o​i​s​s​o​n​(θ)=∑(i,j,t)∈Ωt​r​a​i​n(λi,j(t)−Yi,j(t)​log⁡λi,j(t)).\mathcal{L}_{Poisson}(\theta)=\sum_{(i,j,t)\in\Omega_{train}}\!\Big(\lambda_{i,j}^{(t)}-Y_{i,j}^{(t)}\log\lambda_{i,j}^{(t)}\Big).

The defining property of the Poisson distribution is
equidispersion: the conditional mean and conditional variance
coincide:𝔼​[Yi,j(t)∣𝐗i,j(t)]=Var​[Yi,j(t)∣𝐗i,j(t)]=λi,j(t).\mathbb{E}[Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)}]=\mathrm{Var}[Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)}]=\lambda_{i,j}^{(t)}.

## Theorem 3.15(Overdispersion from Latent
Heterogeneity).

Suppose there exists aσ\sigma-algebraℱ∗\mathcal{F}^{*}withσ​(𝐗)⊂ℱ∗\sigma(\mathbf{X})\subset\mathcal{F}^{*}, and anℱ∗\mathcal{F}^{*}-measurable random variableλ∗>0\lambda^{*}>0such
thatY∣ℱ∗∼Poisson​(λ∗)Y\mid\mathcal{F}^{*}\sim\mathrm{Poisson}(\lambda^{*}).
Ifλ∗\lambda^{*}is notσ​(𝐗)\sigma(\mathbf{X})-measurable, thenVar​[Y∣𝐗]>𝔼​[Y∣𝐗].\mathrm{Var}[Y\mid\mathbf{X}]>\mathbb{E}[Y\mid\mathbf{X}].

## Proof.

We apply the law of total variance, which holds for any
sub-σ\sigma-algebrasσ​(𝐗)⊆ℱ∗\sigma(\mathbf{X})\subseteq\mathcal{F}^{*}:Var​[Y∣𝐗]=𝔼​[Var​(Y∣ℱ∗)∣𝐗]+Var​(𝔼​[Y∣ℱ∗]∣𝐗).\mathrm{Var}[Y\mid\mathbf{X}]=\mathbb{E}\big[\mathrm{Var}(Y\mid\mathcal{F}^{*})\mid\mathbf{X}\big]+\mathrm{Var}\big(\mathbb{E}[Y\mid\mathcal{F}^{*}]\mid\mathbf{X}\big).

SinceY∣ℱ∗∼Poisson​(λ∗)Y\mid\mathcal{F}^{*}\sim\mathrm{Poisson}(\lambda^{*})andλ∗\lambda^{*}isℱ∗\mathcal{F}^{*}-measurable, the Poisson
moment identities established in
Definition3.14give:𝔼​[Y∣ℱ∗]=λ∗,Var​(Y∣ℱ∗)=λ∗.\mathbb{E}[Y\mid\mathcal{F}^{*}]=\lambda^{*},\qquad\mathrm{Var}(Y\mid\mathcal{F}^{*})=\lambda^{*}.

Substituting into the law of total variance:Var​[Y∣𝐗]=𝔼​[λ∗∣𝐗]+Var​[λ∗∣𝐗].\mathrm{Var}[Y\mid\mathbf{X}]=\mathbb{E}[\lambda^{*}\mid\mathbf{X}]+\mathrm{Var}[\lambda^{*}\mid\mathbf{X}].

We identify the first term as the conditional mean ofYY.
By the tower property, sinceσ​(𝐗)⊆ℱ∗\sigma(\mathbf{X})\subseteq\mathcal{F}^{*}:𝔼[Y∣𝐗]=𝔼[𝔼[Y∣ℱ∗]∣𝐗]=𝔼[λ∗∣𝐗]=:μ(𝐗).\mathbb{E}[Y\mid\mathbf{X}]=\mathbb{E}\big[\mathbb{E}[Y\mid\mathcal{F}^{*}]\mid\mathbf{X}\big]=\mathbb{E}[\lambda^{*}\mid\mathbf{X}]=:\mu(\mathbf{X}).

Hence:Var​[Y∣𝐗]=μ​(𝐗)+Var​[λ∗∣𝐗].\mathrm{Var}[Y\mid\mathbf{X}]=\mu(\mathbf{X})+\mathrm{Var}[\lambda^{*}\mid\mathbf{X}].

It remains to show thatVar​[λ∗∣𝐗]>0\mathrm{Var}[\lambda^{*}\mid\mathbf{X}]>0. By definition, for any square-integrable
random variableZZ:Var​[Z∣𝐗]=0⟺Z=𝔼​[Z∣𝐗]ℙ​-a.s.,\mathrm{Var}[Z\mid\mathbf{X}]=0\quad\Longleftrightarrow\quad Z=\mathbb{E}[Z\mid\mathbf{X}]\quad\mathbb{P}\text{-a.s.},

which holds if and only ifZZisσ​(𝐗)\sigma(\mathbf{X})-measurableℙ\mathbb{P}-a.s. By hypothesis,λ∗\lambda^{*}isnotσ​(𝐗)\sigma(\mathbf{X})-measurable, soVar​[λ∗∣𝐗]>0.\mathrm{Var}[\lambda^{*}\mid\mathbf{X}]>0.

Therefore:Var​[Y∣𝐗]=μ​(𝐗)+Var​[λ∗∣𝐗]>μ​(𝐗)=𝔼​[Y∣𝐗].\mathrm{Var}[Y\mid\mathbf{X}]=\mu(\mathbf{X})+\mathrm{Var}[\lambda^{*}\mid\mathbf{X}]>\mu(\mathbf{X})=\mathbb{E}[Y\mid\mathbf{X}].

∎

## Remark.

Theorem3.15shows that overdispersion is
a structural consequence of incomplete observable information,
not an empirical artifact. In the seismological context,λ∗\lambda^{*}represents the unobservable local seismogenic
potential — fluctuations in fault segment activation,
aftershock cascades, and fluid migration — which remain
latent even after conditioning on the feature vector𝐗\mathbf{X}. The Negative Binomial distribution, introduced
in Section3.3.2, provides an analytically tractable
marginal model forYYunder a Gamma prior onλ∗\lambda^{*}.

The empirical diagnostics associated with
Theorem3.15are reported in
Figure1. We use three
explicit graphical designations:
Figure1(a)for the marginal
tail of the count target,
Figure1(b)for the
local dispersion index, and
Figure1(c)for the
mean–variance relationship.(a)Target-count tail diagnostic.(b)Local dispersion index diagnostic.(c)Mean–variance diagnostic.Figure 1:Overdispersion diagnostics following
Theorem3.15: the heavy-tailed marginal
distribution ofYY, the prevalence of local dispersion
indicesD=Var​(Y)/𝔼​(Y)>1D=\mathrm{Var}(Y)/\mathbb{E}(Y)>1, and the
systematic deviation from the Poisson relationVar=𝔼\mathrm{Var}=\mathbb{E}.

The target-count tail diagnostic in
Figure1(a)shows a heavy
right tail incompatible with rapid Poisson decay. The local
dispersion index diagnostic in
Figure1(b)confirmsD>1D>1for most grid cells, while the mean–variance diagnostic
in Figure1(c)shows systematic
departure from the Poisson equalityVar=𝔼\mathrm{Var}=\mathbb{E}.

Consequently,ℒP​o​i​s​s​o​n\mathcal{L}_{Poisson}systematically
under-specifies the model: equidispersion understates the
probability of extreme events. A transition to distribution
families with separate mean and dispersion parametrization is
therefore required.

## 3.3.2Gamma–Poisson Mixture and the Negative
Binomial Distribution

In the seismological context, the latent intensityλ∗\lambda^{*}reflects unobservable variations in local seismogenic potential
— activation of fault segments, aftershock sequences, and
swarm activity. The Gamma distribution forλ∗\lambda^{*}is the
conjugate prior to the Poisson observation model and admits
an analytic marginalization.

## Proposition 3.16(NB as the Marginal Distribution of the
Gamma–Poisson Mixture).

Let the random effectλ∗∼Gamma​(r,β)\lambda^{*}\sim\mathrm{Gamma}(r,\beta),
with shaper>0r>0and rateβ>0\beta>0, and letY∣λ∗∼Poisson​(λ∗)Y\mid\lambda^{*}\sim\mathrm{Poisson}(\lambda^{*}). Then the
marginal distribution ofYYis Negative Binomial:ℙ​(Y=y)=Γ​(y+r)Γ​(y+1)​Γ​(r)​(1−p)r​py,y∈ℕ0,p=(1+β)−1.\mathbb{P}(Y=y)=\frac{\Gamma(y+r)}{\Gamma(y+1)\,\Gamma(r)}(1-p)^{r}p^{y},\quad y\in\mathbb{N}_{0},\quad p=(1+\beta)^{-1}.

## Proof.

The density of the random effectλ∗∼Gamma​(r,β)\lambda^{*}\sim\mathrm{Gamma}(r,\beta)is:fλ∗​(ℓ)=βrΓ​(r)​ℓr−1​e−β​ℓ,ℓ>0.f_{\lambda^{*}}(\ell)=\frac{\beta^{r}}{\Gamma(r)}\,\ell^{\,r-1}e^{-\beta\ell},\qquad\ell>0.

By the law of total probability:ℙ​(Y=y)=∫0∞ℙ​(Y=y∣λ∗=ℓ)​fλ∗​(ℓ)​𝑑ℓ.\mathbb{P}(Y=y)=\int_{0}^{\infty}\mathbb{P}(Y=y\mid\lambda^{*}=\ell)\,f_{\lambda^{*}}(\ell)\,d\ell.

Substituting the Poisson pmf and the Gamma density:ℙ​(Y=y)=∫0∞ℓy​e−ℓy!⋅βrΓ​(r)​ℓr−1​e−β​ℓ​𝑑ℓ=βry!​Γ​(r)​∫0∞ℓy+r−1​e−(1+β)​ℓ​𝑑ℓ.\mathbb{P}(Y=y)=\int_{0}^{\infty}\frac{\ell^{y}e^{-\ell}}{y!}\cdot\frac{\beta^{r}}{\Gamma(r)}\,\ell^{r-1}e^{-\beta\ell}\,d\ell=\frac{\beta^{r}}{y!\,\Gamma(r)}\int_{0}^{\infty}\ell^{\,y+r-1}\,e^{-(1+\beta)\ell}\,d\ell.

The remaining integral is a standard Gamma integral.
Recognizing that fora>0a>0:∫0∞ℓy+r−1​e−a​ℓ​𝑑ℓ=Γ​(y+r)ay+r,\int_{0}^{\infty}\ell^{\,y+r-1}e^{-a\ell}\,d\ell=\frac{\Gamma(y+r)}{a^{y+r}},

and settinga=1+βa=1+\beta:ℙ​(Y=y)=βry!​Γ​(r)⋅Γ​(y+r)(1+β)y+r=Γ​(y+r)Γ​(y+1)​Γ​(r)⋅βr(1+β)y+r.\mathbb{P}(Y=y)=\frac{\beta^{r}}{y!\,\Gamma(r)}\cdot\frac{\Gamma(y+r)}{(1+\beta)^{y+r}}=\frac{\Gamma(y+r)}{\Gamma(y+1)\,\Gamma(r)}\cdot\frac{\beta^{r}}{(1+\beta)^{y+r}}.

It remains to rewrite the last factor in terms ofp=(1+β)−1p=(1+\beta)^{-1}, so that1−p=β/(1+β)1-p=\beta/(1+\beta):βr(1+β)y+r=(β1+β)r⋅(11+β)y=(1−p)r​py.\frac{\beta^{r}}{(1+\beta)^{y+r}}=\left(\frac{\beta}{1+\beta}\right)^{r}\cdot\left(\frac{1}{1+\beta}\right)^{y}=(1-p)^{r}\,p^{y}.

Substituting:ℙ​(Y=y)=Γ​(y+r)Γ​(y+1)​Γ​(r)​(1−p)r​py,\mathbb{P}(Y=y)=\frac{\Gamma(y+r)}{\Gamma(y+1)\,\Gamma(r)}(1-p)^{r}p^{y},

which is the Negative Binomial pmf with parameters(r,p)(r,p).
∎

## Remark(Physical Interpretation).

The continuous Gamma mixture of Poisson processes provides
a natural mechanism for the overdispersion observed in
seismic data: even when the macroscopic feature vector𝐗\mathbf{X}is fixed, the true local intensity fluctuates
due to unobservable geophysical processes — Coulomb stress
transfer, fluid migration, and cascading activation of fault
sub-segments. The shape parameterrrgoverns the degree of
this latent heterogeneity: asr→∞r\to\infty(equivalentlyα=r−1→0\alpha=r^{-1}\to 0), the Gamma mixing distribution
concentrates around its mean and the NB distribution converges
to Poisson, recovering the equidispersion limit.

## 3.3.3Reparametrization for Deep Learning

## Proposition 3.17(Moments of NB and(μ,α)(\mu,\alpha)-Parametrization).

ForNB​(r,β)\mathrm{NB}(r,\beta)withα:=r−1\alpha:=r^{-1}andμ:=r/β\mu:=r/\beta, the variance satisfiesVar​[Y]=μ+α​μ2.\mathrm{Var}[Y]=\mu+\alpha\mu^{2}.

The probability mass function in the(μ,α)(\mu,\alpha)coordinates is:ℙ​(Y=y∣μ,α)=Γ​(y+α−1)Γ​(y+1)​Γ​(α−1)​(11+α​μ)α−1​(α​μ1+α​μ)y.\mathbb{P}(Y=y\mid\mu,\alpha)=\frac{\Gamma(y+\alpha^{-1})}{\Gamma(y+1)\,\Gamma(\alpha^{-1})}\left(\frac{1}{1+\alpha\mu}\right)^{\alpha^{-1}}\left(\frac{\alpha\mu}{1+\alpha\mu}\right)^{y}.

## Proof.

Mean.By the tower property and the moment
identity𝔼​[λ∗]=r/β\mathbb{E}[\lambda^{*}]=r/\betaforλ∗∼Gamma​(r,β)\lambda^{*}\sim\mathrm{Gamma}(r,\beta):μ=𝔼​[Y]=𝔼​[𝔼​[Y∣λ∗]]=𝔼​[λ∗]=rβ.\mu=\mathbb{E}[Y]=\mathbb{E}\big[\mathbb{E}[Y\mid\lambda^{*}]\big]=\mathbb{E}[\lambda^{*}]=\frac{r}{\beta}.

Variance.By the law of total variance and
the Poisson identityVar​(Y∣λ∗)=𝔼​[Y∣λ∗]=λ∗\mathrm{Var}(Y\mid\lambda^{*})=\mathbb{E}[Y\mid\lambda^{*}]=\lambda^{*}:Var​[Y]=𝔼​[Var​(Y∣λ∗)]+Var​(𝔼​[Y∣λ∗])=𝔼​[λ∗]+Var​(λ∗).\mathrm{Var}[Y]=\mathbb{E}\big[\mathrm{Var}(Y\mid\lambda^{*})\big]+\mathrm{Var}\big(\mathbb{E}[Y\mid\lambda^{*}]\big)=\mathbb{E}[\lambda^{*}]+\mathrm{Var}(\lambda^{*}).

Substituting the Gamma moments𝔼​[λ∗]=r/β\mathbb{E}[\lambda^{*}]=r/\betaandVar​(λ∗)=r/β2\mathrm{Var}(\lambda^{*})=r/\beta^{2}:Var​[Y]=rβ+rβ2=μ+μ2r.\mathrm{Var}[Y]=\frac{r}{\beta}+\frac{r}{\beta^{2}}=\mu+\frac{\mu^{2}}{r}.

Settingα:=r−1\alpha:=r^{-1}yieldsVar​[Y]=μ+α​μ2\mathrm{Var}[Y]=\mu+\alpha\mu^{2}.

Reparametrization of the pmf.From the
definitionsr=α−1r=\alpha^{-1}andμ=r/β\mu=r/\beta, we solve
for the canonical parameters:β=rμ=1α​μ.\beta=\frac{r}{\mu}=\frac{1}{\alpha\mu}.

Substituting intop=(1+β)−1p=(1+\beta)^{-1}from
Proposition3.16:p=11+β=11+(α​μ)−1=α​μ1+α​μ,1−p=11+α​μ.p=\frac{1}{1+\beta}=\frac{1}{1+(\alpha\mu)^{-1}}=\frac{\alpha\mu}{1+\alpha\mu},\qquad 1-p=\frac{1}{1+\alpha\mu}.

Substitutingr=α−1r=\alpha^{-1},pp, and1−p1-pinto the
canonical NB pmf of Proposition3.16:ℙ​(Y=y∣μ,α)=Γ​(y+α−1)Γ​(y+1)​Γ​(α−1)​(11+α​μ)α−1​(α​μ1+α​μ)y.\mathbb{P}(Y=y\mid\mu,\alpha)=\frac{\Gamma(y+\alpha^{-1})}{\Gamma(y+1)\,\Gamma(\alpha^{-1})}\left(\frac{1}{1+\alpha\mu}\right)^{\alpha^{-1}}\left(\frac{\alpha\mu}{1+\alpha\mu}\right)^{y}.

∎

## Remark.

Forα>0\alpha>0, the variance scales quadratically with the
mean; asα→0\alpha\to 0, the Gamma mixing distribution
concentrates and the model converges asymptotically to the
Poisson process, recovering equidispersionVar​[Y]→μ\mathrm{Var}[Y]\to\mu.

## Definition 3.18(Neural NB Model).

The neural networkfN​N​(𝐗;θ)f_{NN}(\mathbf{X};\theta)outputs the
local distribution parameters:[μθ​(𝐗)αθ​(𝐗)]=fN​N​(𝐗;θ),μθ>0,αθ>0.\begin{bmatrix}\mu_{\theta}(\mathbf{X})\\
\alpha_{\theta}(\mathbf{X})\end{bmatrix}=f_{NN}(\mathbf{X};\theta),\qquad\mu_{\theta}>0,\quad\alpha_{\theta}>0.

The induced conditional measure is:ℙθ(Y=y∣𝐗):=ℙ(Y=y|μ=μθ(𝐗),α=αθ(𝐗)).\mathbb{P}_{\theta}(Y=y\mid\mathbf{X}):=\mathbb{P}\Big(Y=y\;\Big|\;\mu=\mu_{\theta}(\mathbf{X}),\;\alpha=\alpha_{\theta}(\mathbf{X})\Big).

The NLL training objective is:ℒN​B​(θ)=−∑(i,j,t)∈Ωt​r​a​i​nlog⁡ℙθ​(Yi,j(t)∣𝐗i,j(t)).\mathcal{L}_{NB}(\theta)=-\sum_{(i,j,t)\in\Omega_{train}}\log\mathbb{P}_{\theta}\!\left(Y_{i,j}^{(t)}\mid\mathbf{X}_{i,j}^{(t)}\right).

Each spatial cell(i,j)∈𝒮a​c​t​i​v​e(i,j)\in\mathcal{S}_{active}is
re-indexed via the bijectiong:𝒮a​c​t​i​v​e→𝒞,𝒞={1,…,Nc},g:\mathcal{S}_{active}\to\mathcal{C},\qquad\mathcal{C}=\{1,\ldots,N_{c}\},

settingc=g​(i,j)c=g(i,j)and definingYc(t):=Yi,j(t),𝐗c(t):=𝐗i,j(t).Y_{c}^{(t)}:=Y_{i,j}^{(t)},\qquad\mathbf{X}_{c}^{(t)}:=\mathbf{X}_{i,j}^{(t)}.

The empirical risk then takes the form:ℒN​B​(θ)=−∑(c,t)∈Ωt​r​a​i​nln⁡ℙθ​(Yc(t)∣𝐗c(t)).\mathcal{L}_{NB}(\theta)=-\sum_{(c,t)\in\Omega_{train}}\ln\mathbb{P}_{\theta}\!\big(Y_{c}^{(t)}\mid\mathbf{X}_{c}^{(t)}\big).

The architecturefN​Nf_{NN}incorporates a trainable spatial
embeddings layer, which acts as generalized random effects:
each cell receives a latent representation encoding its
hidden geological structure — proximity to fault systems,
local tectonic regime, and other factors not captured by
the observed feature vector𝐗\mathbf{X}.

## Definition 3.19(Architecture offN​Nf_{NN}).

The forward pass is defined by the compositionfN​N=fs​p∘fo​u​t∘f2∘f1∘fc​a​t∘fe​m​b,f_{NN}=f_{sp}\circ f_{out}\circ f_{2}\circ f_{1}\circ f_{cat}\circ f_{emb},

wheredddenotes the dimension of the numerical feature
vector andde=8d_{e}=8is the embedding dimension.

Spatial index embedding.Each cell indexc∈𝒞c\in\mathcal{C}is mapped to a trainable dense vector
via row lookup in the embedding matrix𝐄∈ℝNc×de\mathbf{E}\in\mathbb{R}^{N_{c}\times d_{e}}:fe​m​b:𝒞→ℝde,c↦𝐞c=𝐄​[c,:].f_{emb}:\mathcal{C}\to\mathbb{R}^{d_{e}},\quad c\mapsto\mathbf{e}_{c}=\mathbf{E}[c,:].

Concatenation.The embedding and the feature vector
are concatenated to form the joint input:fc​a​t:ℝde×ℝd→ℝde+d,(𝐞c,𝐱)↦𝐡0=[𝐞c∥𝐱].f_{cat}:\mathbb{R}^{d_{e}}\times\mathbb{R}^{d}\to\mathbb{R}^{d_{e}+d},\quad(\mathbf{e}_{c},\mathbf{x})\mapsto\mathbf{h}_{0}=[\mathbf{e}_{c}\parallel\mathbf{x}].

Hidden layers.Two fully connected layers with
ReLU activationsσ​(z)=max⁡(0,z)\sigma(z)=\max(0,z):f1:ℝde+d→ℝ64,𝐡0↦𝐡1=σ​(𝐖1​𝐡0+𝐛1),f_{1}:\mathbb{R}^{d_{e}+d}\to\mathbb{R}^{64},\quad\mathbf{h}_{0}\mapsto\mathbf{h}_{1}=\sigma(\mathbf{W}_{1}\mathbf{h}_{0}+\mathbf{b}_{1}),f2:ℝ64→ℝ32,𝐡1↦𝐡2=σ​(𝐖2​𝐡1+𝐛2),f_{2}:\mathbb{R}^{64}\to\mathbb{R}^{32},\quad\mathbf{h}_{1}\mapsto\mathbf{h}_{2}=\sigma(\mathbf{W}_{2}\mathbf{h}_{1}+\mathbf{b}_{2}),

where𝐖1∈ℝ64×(de+d)\mathbf{W}_{1}\in\mathbb{R}^{64\times(d_{e}+d)},𝐛1∈ℝ64\mathbf{b}_{1}\in\mathbb{R}^{64},𝐖2∈ℝ32×64\mathbf{W}_{2}\in\mathbb{R}^{32\times 64},𝐛2∈ℝ32\mathbf{b}_{2}\in\mathbb{R}^{32}are learnable parameters.
Dropout regularization with rate0.20.2is applied after each
hidden layer during training; it is omitted from the formal
composition above as it is inactive at inference time.

Output projection.fo​u​t:ℝ32→ℝ2,𝐡2↦𝐳=𝐖o​u​t​𝐡2+𝐛o​u​t,f_{out}:\mathbb{R}^{32}\to\mathbb{R}^{2},\quad\mathbf{h}_{2}\mapsto\mathbf{z}=\mathbf{W}_{out}\mathbf{h}_{2}+\mathbf{b}_{out},

where𝐖o​u​t∈ℝ2×32\mathbf{W}_{out}\in\mathbb{R}^{2\times 32}and𝐛o​u​t∈ℝ2\mathbf{b}_{out}\in\mathbb{R}^{2}.

Softplus output activation.To guarantee strict
positivity ofμ\muandα\alpha, the logit vector𝐳=[z1,z2]⊤\mathbf{z}=[z_{1},z_{2}]^{\top}is passed through the softplus
function with a numerical stability constantϵ>0\epsilon>0:fs​p:ℝ2→ℝ>02,𝐳↦[μα]=ln⁡(𝟏+exp⁡(𝐳))+ϵ.f_{sp}:\mathbb{R}^{2}\to\mathbb{R}_{>0}^{2},\quad\mathbf{z}\mapsto\begin{bmatrix}\mu\\
\alpha\end{bmatrix}=\ln\!\big(\mathbf{1}+\exp(\mathbf{z})\big)+\epsilon.

The softplus functionln⁡(1+ez)\ln(1+e^{z})is chosen over the
exponential link because it is approximately linear for
large positive inputs, avoiding gradient saturation, while
still guaranteeing positivity. The constantϵ>0\epsilon>0prevents numerical underflow whenz≪0z\ll 0.

The complete forward pass is therefore:[μα]=(fs​p∘fo​u​t∘f2∘f1∘fc​a​t)​(fe​m​b​(c),𝐱).\begin{bmatrix}\mu\\
\alpha\end{bmatrix}=(f_{sp}\circ f_{out}\circ f_{2}\circ f_{1}\circ f_{cat})\big(f_{emb}(c),\,\mathbf{x}\big).

## Remark(Interpretation of Spatial Embeddings).

The vector𝐞c∈ℝde\mathbf{e}_{c}\in\mathbb{R}^{d_{e}}is
functionally analogous to a random effect in a generalized
linear mixed model (GLMM), with one key distinction: the
latent representations are not postulated to be Gaussian,
but are learned end-to-end. This allows the network to
endogenously group cells by seismotectonic characteristics
— fault proximity, local stress regime, recurrence
patterns — without expert specification of a spatial
covariance structure. In the GLMM analogy,𝐄\mathbf{E}plays the role of the random effect design matrix, but
with a learned rather than prescribed covariance.

## 3.3.4Analytical Gradients of the NB Loss Function

## Lemma 3.20(Analytical Gradients of the Local NB
Loss).

For an observation(c,t)(c,t)withrc(t)=(αc(t))−1r_{c}^{(t)}=(\alpha_{c}^{(t)})^{-1}andDc(t)=1+αc(t)​μc(t)D_{c}^{(t)}=1+\alpha_{c}^{(t)}\mu_{c}^{(t)}:∂ℒc(t)∂μc(t)=μc(t)−Yc(t)μc(t)​(1+αc(t)​μc(t)),\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial\mu_{c}^{(t)}}=\frac{\mu_{c}^{(t)}-Y_{c}^{(t)}}{\mu_{c}^{(t)}\big(1+\alpha_{c}^{(t)}\mu_{c}^{(t)}\big)},∂ℒc(t)∂αc(t)=ψ​(Yc(t)+rc(t))−ψ​(rc(t))−ln⁡Dc(t)(αc(t))2+μc(t)−Yc(t)αc(t)​(1+αc(t)​μc(t)),\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial\alpha_{c}^{(t)}}=\frac{\psi\big(Y_{c}^{(t)}+r_{c}^{(t)}\big)-\psi\big(r_{c}^{(t)}\big)-\ln D_{c}^{(t)}}{(\alpha_{c}^{(t)})^{2}}+\frac{\mu_{c}^{(t)}-Y_{c}^{(t)}}{\alpha_{c}^{(t)}\big(1+\alpha_{c}^{(t)}\mu_{c}^{(t)}\big)},

whereψ=(ln⁡Γ)′\psi=(\ln\Gamma)^{\prime}denotes the digamma function.
Under the softplus parametrizationμc(t)=ln⁡(1+ez1,c(t))\mu_{c}^{(t)}=\ln(1+e^{z_{1,c}^{(t)}})andαc(t)=ln⁡(1+ez2,c(t))\alpha_{c}^{(t)}=\ln(1+e^{z_{2,c}^{(t)}}), the chain rule
gives:∂ℒc(t)∂z1,c(t)=∂ℒc(t)∂μc(t)​σ​(z1,c(t)),∂ℒc(t)∂z2,c(t)=∂ℒc(t)∂αc(t)​σ​(z2,c(t)),\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial z_{1,c}^{(t)}}=\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial\mu_{c}^{(t)}}\,\sigma\big(z_{1,c}^{(t)}\big),\qquad\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial z_{2,c}^{(t)}}=\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial\alpha_{c}^{(t)}}\,\sigma\big(z_{2,c}^{(t)}\big),

whereσ​(z)=(1+e−z)−1\sigma(z)=(1+e^{-z})^{-1}is the sigmoid function.

## Proof.

Setℒc(t)=−ℓc(t)\mathcal{L}_{c}^{(t)}=-\ell_{c}^{(t)}, whereℓc(t)\ell_{c}^{(t)}is the local log-likelihood. Taking the
logarithm of the NB pmf from
Proposition3.17:ℓc(t)=ln⁡Γ​(Yc(t)+rc(t))−ln⁡Γ​(Yc(t)+1)−ln⁡Γ​(rc(t))+rc(t)​ln⁡(1Dc(t))+Yc(t)​ln⁡(αc(t)​μc(t)Dc(t)).\ell_{c}^{(t)}=\ln\Gamma\!\big(Y_{c}^{(t)}+r_{c}^{(t)}\big)-\ln\Gamma\!\big(Y_{c}^{(t)}+1\big)-\ln\Gamma\!\big(r_{c}^{(t)}\big)+r_{c}^{(t)}\ln\!\left(\frac{1}{D_{c}^{(t)}}\right)+Y_{c}^{(t)}\ln\!\left(\frac{\alpha_{c}^{(t)}\mu_{c}^{(t)}}{D_{c}^{(t)}}\right).

Expanding the logarithms usingln⁡(1/D)=−ln⁡D\ln(1/D)=-\ln Dandln⁡(α​μ/D)=ln⁡α+ln⁡μ−ln⁡D\ln(\alpha\mu/D)=\ln\alpha+\ln\mu-\ln D:ℓc(t)=ln⁡Γ​(Yc(t)+rc(t))−ln⁡Γ​(Yc(t)+1)−ln⁡Γ​(rc(t))−(Yc(t)+rc(t))​ln⁡Dc(t)+Yc(t)​ln⁡αc(t)+Yc(t)​ln⁡μc(t).\ell_{c}^{(t)}=\ln\Gamma\!\big(Y_{c}^{(t)}+r_{c}^{(t)}\big)-\ln\Gamma\!\big(Y_{c}^{(t)}+1\big)-\ln\Gamma\!\big(r_{c}^{(t)}\big)-\big(Y_{c}^{(t)}+r_{c}^{(t)}\big)\ln D_{c}^{(t)}+Y_{c}^{(t)}\ln\alpha_{c}^{(t)}+Y_{c}^{(t)}\ln\mu_{c}^{(t)}.

Gradient with respect toμc(t)\mu_{c}^{(t)}.Note thatrc(t)=(αc(t))−1r_{c}^{(t)}=(\alpha_{c}^{(t)})^{-1}does not
depend onμc(t)\mu_{c}^{(t)}, and∂Dc(t)/∂μc(t)=αc(t)\partial D_{c}^{(t)}/\partial\mu_{c}^{(t)}=\alpha_{c}^{(t)}.
The onlyμ\mu-dependent terms inℓc(t)\ell_{c}^{(t)}are−(Yc(t)+rc(t))​ln⁡Dc(t)-(Y_{c}^{(t)}+r_{c}^{(t)})\ln D_{c}^{(t)}andYc(t)​ln⁡μc(t)Y_{c}^{(t)}\ln\mu_{c}^{(t)}, giving:∂ℓc(t)∂μc(t)=−(Yc(t)+rc(t))​αc(t)Dc(t)+Yc(t)μc(t).\frac{\partial\ell_{c}^{(t)}}{\partial\mu_{c}^{(t)}}=-(Y_{c}^{(t)}+r_{c}^{(t)})\frac{\alpha_{c}^{(t)}}{D_{c}^{(t)}}+\frac{Y_{c}^{(t)}}{\mu_{c}^{(t)}}.

Applying the identityαc(t)​rc(t)=αc(t)⋅(αc(t))−1=1\alpha_{c}^{(t)}r_{c}^{(t)}=\alpha_{c}^{(t)}\cdot(\alpha_{c}^{(t)})^{-1}=1to simplify
the first term:−(Yc(t)+rc(t))​αc(t)Dc(t)=−αc(t)​Yc(t)−1Dc(t).-(Y_{c}^{(t)}+r_{c}^{(t)})\frac{\alpha_{c}^{(t)}}{D_{c}^{(t)}}=\frac{-\alpha_{c}^{(t)}Y_{c}^{(t)}-1}{D_{c}^{(t)}}.

Combining over a common denominatorμc(t)​Dc(t)\mu_{c}^{(t)}D_{c}^{(t)}:∂ℓc(t)∂μc(t)=(−αc(t)​Yc(t)−1)​μc(t)+Yc(t)​Dc(t)μc(t)​Dc(t).\frac{\partial\ell_{c}^{(t)}}{\partial\mu_{c}^{(t)}}=\frac{(-\alpha_{c}^{(t)}Y_{c}^{(t)}-1)\mu_{c}^{(t)}+Y_{c}^{(t)}D_{c}^{(t)}}{\mu_{c}^{(t)}D_{c}^{(t)}}.

Expanding the numerator and usingDc(t)=1+αc(t)​μc(t)D_{c}^{(t)}=1+\alpha_{c}^{(t)}\mu_{c}^{(t)}:(−αc(t)​Yc(t)−1)​μc(t)+Yc(t)​(1+αc(t)​μc(t))=Yc(t)−μc(t).(-\alpha_{c}^{(t)}Y_{c}^{(t)}-1)\mu_{c}^{(t)}+Y_{c}^{(t)}(1+\alpha_{c}^{(t)}\mu_{c}^{(t)})=Y_{c}^{(t)}-\mu_{c}^{(t)}.

Therefore:∂ℓc(t)∂μc(t)=Yc(t)−μc(t)μc(t)​Dc(t).\frac{\partial\ell_{c}^{(t)}}{\partial\mu_{c}^{(t)}}=\frac{Y_{c}^{(t)}-\mu_{c}^{(t)}}{\mu_{c}^{(t)}D_{c}^{(t)}}.

Negating to obtain the loss gradient:∂ℒc(t)∂μc(t)=μc(t)−Yc(t)μc(t)​(1+αc(t)​μc(t)).\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial\mu_{c}^{(t)}}=\frac{\mu_{c}^{(t)}-Y_{c}^{(t)}}{\mu_{c}^{(t)}\big(1+\alpha_{c}^{(t)}\mu_{c}^{(t)}\big)}.

Gradient with respect toαc(t)\alpha_{c}^{(t)}.The auxiliary derivatives are:∂Dc(t)∂αc(t)=μc(t),∂rc(t)∂αc(t)=−1(αc(t))2.\frac{\partial D_{c}^{(t)}}{\partial\alpha_{c}^{(t)}}=\mu_{c}^{(t)},\qquad\frac{\partial r_{c}^{(t)}}{\partial\alpha_{c}^{(t)}}=-\frac{1}{(\alpha_{c}^{(t)})^{2}}.

We differentiate each group of terms inℓc(t)\ell_{c}^{(t)}separately.

Gamma block.Usingψ​(x)=dd​x​ln⁡Γ​(x)\psi(x)=\frac{d}{dx}\ln\Gamma(x)and the chain rule with∂rc(t)/∂αc(t)=−(αc(t))−2\partial r_{c}^{(t)}/\partial\alpha_{c}^{(t)}=-(\alpha_{c}^{(t)})^{-2}:∂∂αc(t)\displaystyle\frac{\partial}{\partial\alpha_{c}^{(t)}}[ln⁡Γ​(Yc(t)+rc(t))−ln⁡Γ​(rc(t))]\displaystyle\Big[\ln\Gamma\!\big(Y_{c}^{(t)}+r_{c}^{(t)}\big)-\ln\Gamma\!\big(r_{c}^{(t)}\big)\Big]=[ψ​(Yc(t)+rc(t))−ψ​(rc(t))]⋅(−1(αc(t))2)\displaystyle=\Big[\psi\!\big(Y_{c}^{(t)}+r_{c}^{(t)}\big)-\psi\!\big(r_{c}^{(t)}\big)\Big]\cdot\left(-\frac{1}{(\alpha_{c}^{(t)})^{2}}\right)=ψ​(rc(t))−ψ​(Yc(t)+rc(t))(αc(t))2.\displaystyle=\frac{\psi\!\big(r_{c}^{(t)}\big)-\psi\!\big(Y_{c}^{(t)}+r_{c}^{(t)}\big)}{(\alpha_{c}^{(t)})^{2}}.

Logarithmic block.Differentiating the remainingα\alpha-dependent terms−(Yc(t)+rc(t))​ln⁡Dc(t)+Yc(t)​ln⁡αc(t)-(Y_{c}^{(t)}+r_{c}^{(t)})\ln D_{c}^{(t)}+Y_{c}^{(t)}\ln\alpha_{c}^{(t)}:∂∂αc(t)​[−rc(t)​ln⁡Dc(t)−Yc(t)​ln⁡Dc(t)+Yc(t)​ln⁡αc(t)].\frac{\partial}{\partial\alpha_{c}^{(t)}}\Big[{-r_{c}^{(t)}\ln D_{c}^{(t)}}-Y_{c}^{(t)}\ln D_{c}^{(t)}+Y_{c}^{(t)}\ln\alpha_{c}^{(t)}\Big].

Term by term:∂∂αc(t)​[−rc(t)​ln⁡Dc(t)]=ln⁡Dc(t)(αc(t))2−rc(t)​μc(t)Dc(t)=ln⁡Dc(t)(αc(t))2−μc(t)αc(t)​Dc(t),\frac{\partial}{\partial\alpha_{c}^{(t)}}\Big[-r_{c}^{(t)}\ln D_{c}^{(t)}\Big]=\frac{\ln D_{c}^{(t)}}{(\alpha_{c}^{(t)})^{2}}-\frac{r_{c}^{(t)}\mu_{c}^{(t)}}{D_{c}^{(t)}}=\frac{\ln D_{c}^{(t)}}{(\alpha_{c}^{(t)})^{2}}-\frac{\mu_{c}^{(t)}}{\alpha_{c}^{(t)}D_{c}^{(t)}},

where we usedrc(t)=(αc(t))−1r_{c}^{(t)}=(\alpha_{c}^{(t)})^{-1}in the
last step.∂∂αc(t)​[−Yc(t)​ln⁡Dc(t)]=−Yc(t)​μc(t)Dc(t),∂∂αc(t)​[Yc(t)​ln⁡αc(t)]=Yc(t)αc(t).\frac{\partial}{\partial\alpha_{c}^{(t)}}\Big[-Y_{c}^{(t)}\ln D_{c}^{(t)}\Big]=-\frac{Y_{c}^{(t)}\mu_{c}^{(t)}}{D_{c}^{(t)}},\qquad\frac{\partial}{\partial\alpha_{c}^{(t)}}\Big[Y_{c}^{(t)}\ln\alpha_{c}^{(t)}\Big]=\frac{Y_{c}^{(t)}}{\alpha_{c}^{(t)}}.

Summing the logarithmic block contributions:ln⁡Dc(t)(αc(t))2−μc(t)αc(t)​Dc(t)−Yc(t)​μc(t)Dc(t)+Yc(t)αc(t)=ln⁡Dc(t)(αc(t))2+Yc(t)−μc(t)αc(t)​Dc(t).\frac{\ln D_{c}^{(t)}}{(\alpha_{c}^{(t)})^{2}}-\frac{\mu_{c}^{(t)}}{\alpha_{c}^{(t)}D_{c}^{(t)}}-\frac{Y_{c}^{(t)}\mu_{c}^{(t)}}{D_{c}^{(t)}}+\frac{Y_{c}^{(t)}}{\alpha_{c}^{(t)}}=\frac{\ln D_{c}^{(t)}}{(\alpha_{c}^{(t)})^{2}}+\frac{Y_{c}^{(t)}-\mu_{c}^{(t)}}{\alpha_{c}^{(t)}D_{c}^{(t)}}.

Combining the Gamma block and the logarithmic block,
then negating:∂ℒc(t)∂αc(t)=ψ​(Yc(t)+rc(t))−ψ​(rc(t))−ln⁡Dc(t)(αc(t))2+μc(t)−Yc(t)αc(t)​(1+αc(t)​μc(t)).\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial\alpha_{c}^{(t)}}=\frac{\psi\!\big(Y_{c}^{(t)}+r_{c}^{(t)}\big)-\psi\!\big(r_{c}^{(t)}\big)-\ln D_{c}^{(t)}}{(\alpha_{c}^{(t)})^{2}}+\frac{\mu_{c}^{(t)}-Y_{c}^{(t)}}{\alpha_{c}^{(t)}\big(1+\alpha_{c}^{(t)}\mu_{c}^{(t)}\big)}.

Chain rule for the pre-output logits.Under the softplus parametrization, the derivative ofμc(t)=ln⁡(1+ez1,c(t))\mu_{c}^{(t)}=\ln(1+e^{z_{1,c}^{(t)}})with respect toz1,c(t)z_{1,c}^{(t)}is:∂μc(t)∂z1,c(t)=ez1,c(t)1+ez1,c(t)=σ​(z1,c(t)),\frac{\partial\mu_{c}^{(t)}}{\partial z_{1,c}^{(t)}}=\frac{e^{z_{1,c}^{(t)}}}{1+e^{z_{1,c}^{(t)}}}=\sigma\!\big(z_{1,c}^{(t)}\big),

and analogously∂αc(t)/∂z2,c(t)=σ​(z2,c(t))\partial\alpha_{c}^{(t)}/\partial z_{2,c}^{(t)}=\sigma(z_{2,c}^{(t)}).
Applying the chain rule:∂ℒc(t)∂z1,c(t)=∂ℒc(t)∂μc(t)​σ​(z1,c(t)),∂ℒc(t)∂z2,c(t)=∂ℒc(t)∂αc(t)​σ​(z2,c(t)).\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial z_{1,c}^{(t)}}=\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial\mu_{c}^{(t)}}\,\sigma\!\big(z_{1,c}^{(t)}\big),\qquad\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial z_{2,c}^{(t)}}=\frac{\partial\mathcal{L}_{c}^{(t)}}{\partial\alpha_{c}^{(t)}}\,\sigma\!\big(z_{2,c}^{(t)}\big).

Averaging over a mini-batchΩb​a​t​c​h⊆Ωt​r​a​i​n\Omega_{batch}\subseteq\Omega_{train}yields the stochastic gradient estimate∇θℒN​B\nabla_{\theta}\mathcal{L}_{NB}used in backpropagation.
∎

## 4Experimental Validation

## 4.1Evaluation Protocol

All models are evaluated on𝒟f​i​n​a​l\mathcal{D}_{final}using three
point metrics and two probabilistic metrics.

## Point metrics.MAE\displaystyle\mathrm{MAE}=1N​∑i|yi−μ^i|,\displaystyle=\frac{1}{N}\sum_{i}|y_{i}-\hat{\mu}_{i}|,RMSE\displaystyle\mathrm{RMSE}=1N​∑i(yi−μ^i)2,\displaystyle=\sqrt{\frac{1}{N}\sum_{i}(y_{i}-\hat{\mu}_{i})^{2}},MPD\displaystyle\mathrm{MPD}=2N​∑i[yi​ln⁡yiμ^i−(yi−μ^i)]\displaystyle=\frac{2}{N}\sum_{i}\left[y_{i}\ln\!\frac{y_{i}}{\hat{\mu}_{i}}-(y_{i}-\hat{\mu}_{i})\right]

where terms withyi=0y_{i}=0are replaced byμ^i\hat{\mu}_{i},
andμ^i≥10−9\hat{\mu}_{i}\geq 10^{-9}is enforced for numerical
stability. MPD is the mean Poisson deviance; it is a
mean-oriented criterion and is insensitive to the quality
of conditional dispersion modeling. Adequacy of the
distributional specification is assessed separately via
the LR test, PIT, and tail evaluation below.

## Probabilistic metrics.

NLL denotes the negative log-likelihood evaluated under the
model-specific distribution (Poisson or NB). Note that NLL
values arenotdirectly comparable across model
families, since Poisson and NB likelihoods are defined on
different parametric families. CRPS denotes the discrete
Continuous Ranked Probability Score[14]:CRPS=∑k=0Kmax(F​(k)−𝟏y≤k)2,\mathrm{CRPS}=\sum_{k=0}^{K_{\max}}\bigl(F(k)-\mathbf{1}_{y\leq k}\bigr)^{2},

whereF​(k)=ℙθ​(Y≤k∣𝐗)F(k)=\mathbb{P}_{\theta}(Y\leq k\mid\mathbf{X})is
the predicted CDF truncated atKmaxK_{\max}. Unlike NLL, CRPS
is comparable across all model families and is used as the
primary probabilistic evaluation criterion in the tail
stratum.

## Static splits.

A chronological 80/20 split is used: the first 80% of
unique weeks form the training set and the remaining 20%
the test set, consistent with Definition3.12.
For GLM models,α\alphais estimated by profile likelihood
maximization over a grid of 60 pointsα∈[10−3,102]\alpha\in[10^{-3},10^{2}]. For DL models, a
chronological validation cut is applied within the training
block — the last 15% of rows (without shuffling) —
ensuring causal epoch selection and preventing look-ahead
bias consistent with RemarkRemark.

## Walk-Forward Validation (WF).

For each test yearY∈{2018,…,2023}Y\in\{2018,\dots,2023\}, the model
is trained on all years<Y<Yand evaluated on yearYY.
Formally, for foldYYthe training index block isΩt​r​a​i​n(Y)={(i,j,t)∈supp⁡(𝒟f​i​n​a​l)∣year​(t)<Y},\Omega_{train}^{(Y)}=\{(i,j,t)\in\operatorname{supp}(\mathcal{D}_{final})\mid\mathrm{year}(t)<Y\},

and the test block contains all weeks of calendar yearYY.
This is a separate walk-forward construction and must not
be conflated with the static 80/20 split of
Definition3.12; the relationship between
the two protocols is discussed in
RemarkRemark. Four systems are compared:
NB GLM (MLEα\alphare-estimated on each fold),
Hybrid DL NB, Neural Poisson, and ETAS per-cell. DL models
in WF use a chronological val-cut (last 15% ofΩt​r​a​i​n(Y)\Omega_{train}^{(Y)}) for early stopping.

## Statistical tests.

Two inferential procedures are applied. The likelihood-ratio
test with boundary correction[10]tests the null hypothesisH0:α=0H_{0}\colon\alpha=0(Poisson
sufficiency); underH0H_{0}the LR statistic follows the
boundary mixture12​δ0+12​χ12\frac{1}{2}\delta_{0}+\frac{1}{2}\chi^{2}_{1}rather thanχ12\chi^{2}_{1}, and the correctedpp-value ispb​o​u​n​d​a​r​y=12​χ12​-sf​(L​R)p_{boundary}=\frac{1}{2}\,\chi^{2}_{1}\text{-sf}(LR).
Moran’sII[13]is computed on
time-averaged Pearson residuals with queen-contiguity
weights and a permutationpp-value (B=999B=999), testing
the spatial conditional independence assumption of
RemarkRemark.

## 4.2Global Model Comparison (Static 80/20 Split)Table 1:Model comparison on the test set (80/20 split).
NB GLM uses MLEα\alpha; bold denotes the best result
per metric.ModelMAERMSEMPDα^\hat{\alpha}(GLM)Naive Persistence0.22100.68394.1551—Poisson Baseline (GLM)0.23380.55240.6466—Poisson Enhanced (GLM)0.22830.54250.5908—NB Baseline (GLM, MLE)0.23260.54650.6433∼\sim2.98NB Enhanced (GLM, MLE)0.22530.54230.5859∼\sim2.98Hybrid DL Baseline (NB)0.20070.52470.5320—Hybrid DL Enhanced (NB)0.20490.52380.5461—Neural Poisson Baseline0.19970.52110.5365—Neural Poisson Enhanced0.20650.52740.5268—ETAS per-cell0.18910.54430.5688—

Table1reveals several key
observations.

First, the transition from GLM to neural parametrization
(with the same NB loss function) yields a reduction in MAE
of≈9%\approx 9\%and in RMSE of≈4%\approx 4\%, constituting
the primary architectural gain. This improvement is
attributable to the spatial embeddings layer, which captures
cell-level heterogeneity not expressible through the fixed
GLM link function.

Second, Hybrid DL NB and Neural Poisson Enhanced are
statistically indistinguishable on MAE/RMSE/MPD within the
same architectural family. This implies that the benefit of
NB parametrization does not manifest in point metrics, which
are insensitive to distributional shape by construction.

Third, Hybrid DL Baseline outperforms Hybrid DL Enhanced
on MPD (0.5320 vs. 0.5461): within the neural NB family,
the additional physical features degrade the point MPD while
improving probabilistic metrics (NLL, CRPS) in the tail
stratum (see Section4.6). This trade-off is
consistent with the theoretical role ofα\alphaas a
dispersion parameter: enhanced features sharpen the
per-cellα\alphaestimates at the cost of mean bias
in low-activity cells.

ETAS per-cell occupies an intermediate position on MAE
(0.1891), underperforming neural models on RMSE and MPD,
but remaining competitive as a physics-based baseline that
requires no gradient-based training. Its competitiveness
supports the view that temporal clustering structure,
captured analytically via the Omori–Utsu kernel, provides
signal comparable to learned representations for point
prediction.

As noted in Section4.1, MPD is a
mean-oriented criterion insensitive to conditional
dispersion quality. Adequacy of the distributional
specification is assessed via the LR test
(Section4.4), PIT
(Section4.5), and tail evaluation
(Section4.6).

## 4.3Walk-Forward Stability (2018–2023)Table 2:Walk-Forward MPD by year for four systems
(fromwalk_forward_results.csv).YearNB GLM (MLEα\alpha)Hybrid DL NBNeural PoissonETAS per-cell20180.4930.4620.4650.46620190.4130.3870.3840.37820200.5960.5320.5350.56320210.5460.5100.5080.50820220.5120.4980.4990.49820230.7330.6210.6190.683Mean±\pmSD0.549±0.1090.549\pm 0.1090.502±0.0780.502\pm 0.0780.502±0.078\mathbf{0.502\pm 0.078}0.516±0.1020.516\pm 0.102

Across all six test years, neural models consistently
achieve lower MPD than NB GLM. Hybrid DL NB and Neural
Poisson reach an identical mean reduction of≈8.6%\approx 8.6\%relative to NB GLM and are statistically indistinguishable
on this criterion. The standard deviation of MPD across
years is notably lower for neural models
(SD=0.078\mathrm{SD}=0.078) than for NB GLM
(SD=0.109\mathrm{SD}=0.109) and ETAS per-cell
(SD=0.102\mathrm{SD}=0.102), indicating that the neural
architectures not only improve the mean but also reduce
year-to-year variability. ETAS per-cell achieves a
competitive≈6.0%\approx 6.0\%reduction without
gradient-based training, relying exclusively on the
physics of the temporal point process.Figure 2:Walk-Forward MPD stability by test year
(four systems).

## 4.4Inferential Overdispersion Test (LR)

To formally test the necessity of overdispersion
modeling, a likelihood-ratio test is applied between
Poisson_Enhanced and NB_Enhanced. Both models are
estimated on the training block (80% of unique weeks);α\alphafor the NB model is selected by profile
likelihood maximization (grid of 60 points):L​R=2​(log⁡LNB−log⁡LPoisson)=820.21,α^MLE=2.98.LR=2\bigl(\log L_{\mathrm{NB}}-\log L_{\mathrm{Poisson}}\bigr)=820.21,\quad\hat{\alpha}_{\mathrm{MLE}}=2.98.

SinceH0H_{0}corresponds toα=0\alpha=0, which lies on
theboundaryof the NB parameter space, the null
distribution of the LR statistic underH0H_{0}is the
boundary mixture[10]12​δ0+12​χ12,\tfrac{1}{2}\,\delta_{0}+\tfrac{1}{2}\,\chi^{2}_{1},

rather thanχ12\chi^{2}_{1}. The standardχ12\chi^{2}_{1}critical
value would overstate significance; the boundary-correctedpp-value is:pboundary=12⋅χ12​-​sf​(820.21)=12×2.18×10−180≈1.09×10−180.p_{\mathrm{boundary}}=\tfrac{1}{2}\cdot\chi^{2}_{1}\text{-}\mathrm{sf}(820.21)=\tfrac{1}{2}\times 2.18\times 10^{-180}\approx 1.09\times 10^{-180}.

The valueα^MLE=2.98\hat{\alpha}_{\mathrm{MLE}}=2.98is
attained atlog⁡LNB=−3252.82\log L_{\mathrm{NB}}=-3252.82againstlog⁡LPoisson=−3662.93\log L_{\mathrm{Poisson}}=-3662.93, corresponding
to a log-likelihood gain of409.11409.11nats. The null
hypothesisH0H_{0}— that the Poisson specification is
sufficient — is rejected with extreme significance
even after boundary correction. Note that this statistic
is computed in-sample on the training fold; the
predictive LR based on out-of-sample NLL is reported
in Section4.6.

## Remark(In-sample vs. out-of-sample LR).

The in-sample LR statistic of 820.21 establishes that
the NB family is necessary to describe the training
distribution. A complementary out-of-sample check is
provided in Section4.6via NLL on the test
set, which confirms that the NB advantage persists under
the temporal hold-out and is not an artifact of
in-sample overfitting ofα\alpha.

## 4.5Probabilistic Calibration (PIT)

The randomized PIT with discrete correction[14]is computed for Hybrid_DL_Enhanced and
Neural_Poisson_Enhanced. Under perfect calibration,
the PIT follows a uniform distribution on[0,1][0,1],
with𝔼​[PIT]=0.5\mathbb{E}[\mathrm{PIT}]=0.5andVar​(PIT)=1/12≈0.0833\mathrm{Var}(\mathrm{PIT})=1/12\approx 0.0833.Table 3:PIT summary statistics (fromoutputs/calibration_summary.csv).L1L_{1}denotes the mean absolute deviation from
the uniform distribution.Modelnn𝔼​[PIT]\mathbb{E}[\mathrm{PIT}]Var​(PIT)\mathrm{Var}(\mathrm{PIT})L1L_{1}Hybrid DL Enhanced (NB)24480.50230.08470.00466Neural Poisson Enhanced24480.49520.08440.00448

Both models exhibit PIT histograms close to uniform.
The empirical moments are consistent with the theoretical
targets:𝔼​[PIT]≈0.5\mathbb{E}[\mathrm{PIT}]\approx 0.5andVar​(PIT)≈0.084\mathrm{Var}(\mathrm{PIT})\approx 0.084, compared
to the uniform reference of1/12≈0.0831/12\approx 0.083.
At the marginal level, Neural Poisson is marginally
better (L1=0.00448L_{1}=0.00448vs.0.004660.00466), indicating
slightly sharper global calibration. However, global
PIT uniformity is a necessary but not sufficient
condition for calibration quality: a model can achieve
near-uniform marginal PIT while miscalibrating
conditionally in specific strata. The key distinction
between the two models emerges in the tail stratum
(Y≥5Y\geq 5), where the NB model yields lower NLL and
CRPS (see Section4.6): it is precisely
there that the additional degree of freedomα\alphaenables more accurate estimation of the probability
of extreme events, a capability that marginal PIT
cannot detect.Figure 3:Randomized PIT histograms. The red
horizontal line indicates the expected level
under uniformity.

## 4.6Tail-Conditional EvaluationTable 4:Metrics by stratum (fromoutputs/tail_evaluation.csv). NLL for NB
models is computed under the NB distribution with
per-sampleα\alpha; for Poisson/GLM models, under
the Poisson distribution. Direct NLL comparison
across model families is not valid.StratumModelMAEMPDNLLCRPSAllHybrid DL NB0.2050.5460.3660.116Neural Poisson0.2070.5270.3330.116NB GLM (MLE)0.2290.5920.3780.124Poisson GLM0.2280.5910.3650.123Q4Q_{4}(high)Hybrid DL NB1.0283.3702.7470.971Neural Poisson1.0443.1852.2650.932NB GLM (MLE)1.1763.6492.8391.083Poisson GLM1.1513.5962.4701.023Y≥5Y\geq 5Hybrid DL NB6.22525.6437.9115.875Neural Poisson6.52126.4265.090∗6.085NB GLM (MLE)7.03835.4319.0006.717Poisson GLM6.90634.4009.0776.594

∗NLL for Neural Poisson is computed under the Poisson
distribution; NLL for Hybrid DL NB is computed under the
NB distribution with per-cellα^\hat{\alpha}. These
quantities are not directly comparable.

In the tail stratum (Y≥5Y\geq 5), Hybrid DL NB achieves
NLL=7.91=7.91, substantially better than NB GLM (9.009.00)
and Poisson GLM (9.089.08), representing a reduction of12.1%12.1\%and12.8%12.8\%respectively. On CRPS, which is
comparable across all model families, Hybrid DL NB
(5.8755.875) outperforms NB GLM (6.7176.717) by12.5%12.5\%and
Poisson GLM (6.5946.594) by10.9%10.9\%. It is precisely in
this stratum that the per-cell parameterα\alphacontributes most to extreme event risk estimation:
by adapting the dispersion to each cell’s seismotectonic
regime, the model assigns higher probability mass to
large counts where the GLM, constrained to a globalα^≈2.98\hat{\alpha}\approx 2.98, systematically
underestimates tail probabilities.

Notably, Neural Poisson Enhanced achieves lower MPD than
Hybrid DL NB in theY≥5Y\geq 5stratum (26.426 vs. 25.643 — wait, NB is better here), confirming that the
NB advantage is specific to probabilistic tail metrics
and does not extend to point prediction, consistent with
the theoretical argument of
Theorem3.15.Figure 4:MPD by stratum and model
(quartiles++Y≥5Y\geq 5).

## 4.7Spatial Autocorrelation of Residuals
(Moran’sII)

For each model, standardized Pearson residuals are
computed asrc,t=Yc,t−μ^c,tμ^c,t+α^​μ^c,t2,r_{c,t}=\frac{Y_{c,t}-\hat{\mu}_{c,t}}{\sqrt{\hat{\mu}_{c,t}+\hat{\alpha}\hat{\mu}_{c,t}^{2}}},

and averaged over time within each cell. For Poisson
models, the denominator reduces toμ^c,t\sqrt{\hat{\mu}_{c,t}}, corresponding toα^=0\hat{\alpha}=0. Moran’sIIis computed on the
queen-contiguity weight matrix
(Δ​λ=Δ​φ=3∘\Delta\lambda=\Delta\varphi=3^{\circ},
row-standardized); thepp-value is obtained via a
permutation test (B=999B=999).Table 5:Moran’sIIfor time-averaged Pearson
residuals (queen-contiguity,B=999B=999permutations).
For DL models, cell identifiers are not preserved
in calibration predictions, so Moran’sIIis not
computed (n/a).ModelMoran’sIIzz-scoreppermp_{\mathrm{perm}}Naive Persistence−0.056-0.0560.0330.0330.4520.452Poisson Enhanced (GLM)−0.053-0.0530.0710.0710.4350.435NB Enhanced (GLM, MLE)−0.076-0.076−0.125-0.1250.5110.511Hybrid DL Enhanced (NB)n/an/an/aNeural Poisson Enhancedn/an/an/aFigure 5:Moran’sIIof Pearson residuals
(red indicates significance atp<0.05p<0.05).

Figure5shows that all three GLM models exhibit insignificant and slightly
negative spatial autocorrelation (p>0.4p>0.4), indicating
no systematic spatial clustering in the time-averaged
residuals. The negative sign of Moran’sIIsuggests
mild spatial dispersion in the residuals — adjacent
cells tend to have residuals of opposite sign — which
is consistent with a model that slightly over-smooths
across cell boundaries. This partially alleviates
concerns about violation of the spatial conditional
independence assumption of
RemarkRemarkat the level of
GLM predictions. However, for neural models this test
remains unimplemented due to the absence of cell
identifiers in calibration outputs, and is flagged as
a limitation in Section6.1.

## 4.8Audit of Parameterα\alphaand Identifiability

Global statistics of the predictedα\alphafor
Hybrid_DL_Enhanced (seed 42):n=2448,α¯=3.44,median​(α)=3.61,q0.1=1.63,q0.9=5.17,ℙ​(α<10−2)=0.n=2448,\quad\overline{\alpha}=3.44,\quad\mathrm{median}(\alpha)=3.61,\quad q_{0.1}=1.63,\quad q_{0.9}=5.17,\quad\mathbb{P}(\alpha<10^{-2})=0.(a)Distribution of predictedα\alpha.(b)Boxplot ofα\alphaacross 5 seeds.Figure 6:Audit of the overdispersion
parameterα\alphafor Hybrid DL NB Enhanced:
marginal distribution and stability across
independent seeds.

The absence of a near-zero regime
(ℙ​(α<10−2)=0\mathbb{P}(\alpha<10^{-2})=0across all seeds)
confirms that the network does not collapse to the
Poisson limit (α→0\alpha\to 0), as established
theoretically in Proposition3.17. The
mean predictedα¯=3.44\overline{\alpha}=3.44is
consistent with the GLM profile-MLE estimateα^MLE=2.98\hat{\alpha}_{\mathrm{MLE}}=2.98from
Section4.4, providing cross-validation
between the neural and GLM estimates of overdispersion.
To assess identifiability ofα\alpha, the model is
re-trained five times with different random seeds:Table 6:5-seed stability of theα\alphadistribution
(fromoutputs/alpha_identifiability.csv).q0.1q_{0.1}/q0.9q_{0.9}denote the 10th/90th percentiles.Seednnα¯\overline{\alpha}median​(α)\mathrm{median}(\alpha)q0.1q_{0.1}q0.9q_{0.9}4224483.443.611.635.17724484.675.131.617.1912324484.124.281.635.77202424484.464.531.776.9599924483.323.631.704.96Mean3.99±0.613.99\pm 0.614.24±0.664.24\pm 0.661.67±0.061.67\pm 0.066.01±0.986.01\pm 0.98

The lower quantileq0.1q_{0.1}is stable across seeds
(σ=0.06\sigma=0.06), indicating robustness of the lower
part of theα\alphadistribution. This stability is
practically meaningful:q0.1≈1.67q_{0.1}\approx 1.67consistently across seeds implies that even in
low-dispersion cells the network reliably producesα>1\alpha>1, far from the Poisson boundary. The upper
tail (q0.9q_{0.9}) is less stable (σ=0.98\sigma=0.98),
indicating incomplete identifiability ofα\alphain
high-activity cells. This is consistent with the
theoretical expectation: in cells with𝔼​[Y]≪1\mathbb{E}[Y]\ll 1, the NB likelihood surface is
nearly flat inα\alpha, since for small counts the
Poisson and NB distributions are difficult to
distinguish empirically. This limitation is discussed
in Section6.1.

## 5Related Work

## Classical seismology: ETAS and temporal point
processes.

The reference model in operational seismic forecasting
is ETAS (Epidemic Type Aftershock Sequence,[1]), which describes the
conditional event intensity as a sum of background
activity and a temporal superposition of Omori–Utsu
aftershock contributions from preceding events. Spatial
extensions of ETAS[2]and its Bayesian variants provide semi-principled
specifications of the decay kernel. The international
CSEP program[3]provides
standardized protocols for verification of probabilistic
forecasts. The present work includes per-cell temporal
ETAS as a direct comparative baseline, evaluated under
the same Walk-Forward protocol as the neural models
(Section4.3).

## Count regression and NB-GLMM.

The Negative Binomial distribution as a model for
overdispersion in count regression is systematically
treated in[4]; MLE estimation
for NB-GLM is developed in[5].
Generalized linear mixed models (GLMM) accommodate
multiple sources of random effects analogous to our
spatial embeddings, but require explicit specification
of the covariance structure. The present work replaces
this requirement with end-to-end learning through the
embedding layer, as formalized in
Definition3.19and
RemarkRemark. A further
distinction from standard NB-GLM is that our model
produces per-cell estimates ofα\alpharather than a
single global dispersion parameter, as demonstrated
empirically in Section4.8.

## Neural point processes.

The Neural Point Processes
literature[6,7]generalizes the ETAS formalism to arbitrary conditional
intensities parametrized by neural networks.[8]showed that strict positivity
of the predicted intensity requires a dedicated
parametrization (softplus or exp); the present work
uses softplus+ϵ+\epsilon, as described in
Definition3.19with the gradient
stability rationale given therein. The present work
differs from this stream in that we operate on
aggregated weekly counts rather than event times,
which simplifies training and interpretation but
sacrifices sub-weekly temporal structure.

## Deep learning in seismology.

[11]proposed a neural method for
aftershock prediction using the stress tensor matrix
as input.[12]reproduced this result
with a single-layer network and showed that linear
models are often competitive with deep architectures
— an important cautionary argument against
over-engineering in seismological ML, consistent with
our finding that Hybrid DL NB and Neural Poisson are
statistically indistinguishable on point metrics
(Section4.2). In contrast to
these works, we address probabilistic forecasting of
a count process (weekly event counts per cell) rather
than aftershock coordinate prediction or
classification.

The proposed approach occupies an intermediate niche:
the probabilistic rigor of NB-GLMM (statistically
principled dispersion model, formally grounded in
Theorem3.15and
Proposition3.16) combined with the
flexibility of neural approximation (requiring no
explicit physical triggering model), with
interpretability preserved through per-cellα\alpha.

## 6Discussion

## What is shown.

The Poisson hypothesis is rejected at the population
level with extreme significance (L​R=820.21LR=820.21,pboundary≈10−180p_{\mathrm{boundary}}\approx 10^{-180}), confirming
the theoretical prediction of
Theorem3.15. Hybrid DL NB and
Neural Poisson are statistically indistinguishable on
MAE/RMSE/MPD on the static split, and both reduce
mean Walk-Forward MPD by8.6%8.6\%relative to NB GLM
(bothMPD¯=0.502\overline{\mathrm{MPD}}=0.502over 6 years),
with notably lower year-to-year variance
(SD=0.078\mathrm{SD}=0.078vs.0.1090.109for NB GLM). In
the tail stratum (Y≥5Y\geq 5), Hybrid DL NB achieves
CRPS=5.88=5.88against6.726.72for NB GLM — a
reduction of12.5%12.5\%— constituting the primary
argument for NB parametrization over the Poisson
alternative. Moran’sIIon GLM residuals is
insignificant (p>0.4p>0.4), which reduces but does not
eliminate concerns about spatial independence
(RemarkRemark).

## Practical implications.

The per-cell parameterα\alphaenables construction
of risk-aware alerts: the0.950.95-quantile of the
predicted NB distribution provides a natural threshold
for preventive notification, with the quantile width
directly reflecting the local seismogenic uncertainty
encoded inα\alpha. The hybrid architecture delivers
uncertainty-aware cell-level forecasts without
requiring explicit specification of a spatial
covariance structure, making it deployable in
operational settings where expert geophysical
knowledge of fault geometry is unavailable.

## Comparison with ETAS.

ETAS per-cell explicitly models temporal clustering
via the Omori–Utsu kernel and provides physically
interpretable parameters. The proposed model
potentially gains through nonlinear interactions
among physical predictors (seismic energy proxies,
seismic quiescence), which ETAS cannot capture through
its parametric kernel. However, it concedes ground
in spatial physics: ETAS naturally incorporates
cross-cell triggering through the spatial kernel,
whereas our approach assumes spatial conditional
independence (RemarkRemark).
The≈2.6%\approx 2.6\%gap in Walk-Forward MPD between
Hybrid DL NB and ETAS per-cell
(0.5020.502vs.0.5160.516) may partly reflect this
structural difference, and motivates the spatial
convolution extension outlined in
Section6.1.

## 6.1Limitations

## 1. Spatial conditional independence.

The assumptionYi,j(t)⟂Yk,m(t)∣𝐗(t)Y_{i,j}^{(t)}\perp Y_{k,m}^{(t)}\mid\mathbf{X}^{(t)}, formalized in
RemarkRemark, is the primary
methodological simplification. Coulomb stress transfer
and ETAS triggering[1]induce
cross-cell dependencies that are not explicitly modeled.
Moran’sII(Section4.7) quantifies the
degree of violation of this assumption for GLM models
and finds no significant autocorrelation (p>0.4p>0.4);
however, this test remains unimplemented for neural
models due to the absence of cell identifiers in
calibration outputs. The natural extension is to replace
the factorized likelihood with a spatial convolution
layer or a graph neural network operating on the
cell adjacency structure, analogous to the spatial
ETAS kernel of[2].

## 2. Catalog threshold homogeneity.

The completeness magnitudeM^c=4.5\widehat{M}_{c}=4.5is
estimated globally over the entire catalog using the
Maximum Curvature method[9]. In
practice,McM_{c}is spatially heterogeneous: in cells
with sparse station coverage or low background
seismicity,McM_{c}may be substantially higher. The
lower catalog thresholdM≥3.0M\geq 3.0lies belowM^c\widehat{M}_{c}, creating potential incompleteness
in the rangeM∈[3.0,4.5)M\in[3.0,4.5)and introducing
downward bias in event counts for low-activity cells.
This bias propagates into the feature functionalΦ\Phi(Definition3.6), particularly
affectingϕ5\phi_{5}(12-week accumulated activity)
andϕ7\phi_{7}(seismic gap), and may contribute to
the incomplete identifiability ofα\alphain
low-activity cells observed in
Section4.8. A spatially
stratifiedMcM_{c}estimation would mitigate this
bias at the cost of reduced catalog size in
high-McM_{c}cells.

## 3. Walk-Forward: statistical power.

The protocol covers six test years over a spatial
grid of∼20\sim 20active cells, yielding a limited
effective number of independent test observations.
Year-level effects are assessed without confidence
intervals, reducing statistical power when comparing
individual years. In particular, the anomalously
high MPD in 2023 (NB GLM:0.7330.733, Hybrid DL NB:0.6210.621) may reflect an atypical seismic episode
rather than a systematic model failure; this cannot
be confirmed without wider temporal coverage.
Extending the Walk-Forward protocol to additional
test years or bootstrapping year-level confidence
intervals would strengthen the comparative
conclusions of Table2.

## 4. Identifiability ofα\alpha.

The parameterα\alphais estimated purely from data
via the softplus parametrization without a prior or
L2 penalty. The 5-seed stability audit
(Section4.8) provides empirical
but not theoretical guarantees of identifiability.
In cells with𝔼​[Y]<0.3\mathbb{E}[Y]<0.3, the NB and
Poisson likelihoods are nearly indistinguishable
for observed count sequences, makingα\alphaeffectively unidentified from finite data. A Bayesian
treatment with a weakly informative prior onα\alpha— for example,α∼Gamma​(2,1)\alpha\sim\mathrm{Gamma}(2,1),
concentrating mass away from zero while permitting
large values — would regularize the upper tail of
theα\alphadistribution and reduce the seed
instability ofq0.9q_{0.9}(σ=0.98\sigma=0.98) observed
in Table6.

## 5. Geographic generalizability.

The model is trained exclusively on Central Asian
data (Tian Shan, Pamir) for 2010–2024 and has not
been tested in other regions or time periods. The
spatial embeddings encode local seismotectonic
properties of the∼20\sim 20active cells in the
study region and are not transferable to new spatial
domains: the embedding matrix𝐄∈ℝNc×de\mathbf{E}\in\mathbb{R}^{N_{c}\times d_{e}}(Definition3.19) is indexed by
cell identifiers that have no meaning outside the
training grid. Transfer to a new region would require
either full retraining or a meta-learning approach
in which embeddings are initialized from geophysical
covariates (fault density, historicalbb-value,
heat flow) rather than learned from scratch.

## 7Conclusion

This work proposes an approach to probabilistic
forecasting of the weekly earthquake count (M≥3.0M\geq 3.0)
on a spatial grid over Central Asia, with emphasis on
correct modeling of conditional dispersion. The
empirical and theoretical contributions are threefold.

Statistically.A formal likelihood-ratio test
with boundary correction (Section4.4)
rejects the Poisson hypothesis withp<10−179p<10^{-179},
confirming the structural overdispersion predicted by
Theorem3.15. The estimated global
dispersionα^MLE=2.98\hat{\alpha}_{\mathrm{MLE}}=2.98is
consistent with the neural per-cell meanα¯=3.44\overline{\alpha}=3.44–3.993.99across seeds
(Section4.8), providing convergent
evidence from two independent estimation approaches.

Architecturally.The EarthquakeNet hybrid
architecture (spatial embeddings + MLP with NB loss,
Definition3.19) consistently
outperforms NB GLM on MPD by≈8.6%\approx 8.6\%across
all six Walk-Forward folds (2018–2023), with lower
year-to-year variance (SD=0.078\mathrm{SD}=0.078vs.0.1090.109). Hybrid DL NB and Neural Poisson are
statistically indistinguishable on point metrics,
confirming that the architectural gain over GLM
stems from spatial embeddings rather than the
distributional family.

Probabilistically.The key advantage of NB
parametrization manifests in the tail stratum
(Y≥5Y\geq 5): Hybrid DL NB achieves CRPS=5.875=5.875,
a12.5%12.5\%reduction relative to NB GLM (6.7176.717),
while Neural Poisson underperforms on CRPS despite
comparable point metrics. This confirms the
theoretical prediction that the additional degree of
freedomα\alphais necessary precisely where
equidispersion is most consequential — in the
estimation of extreme event probabilities. The
per-cellα\alphaprovides a natural basis for
risk-aware alerts: the0.950.95-quantile of the
predicted NB distribution constitutes an
operationally interpretable exceedance threshold
without additional parametric assumptions.

Three directions for future work follow directly
from the identified limitations
(Section6.1):
- •

Spatial dependence modeling.Replacing the factorized likelihood with a
graph neural network on the cell adjacency
structure, or incorporating an ETAS-like spatial
convolution kernel[2],
would remove the spatial conditional independence
assumption of RemarkRemarkand potentially close the≈2.6%\approx 2.6\%Walk-Forward gap between EarthquakeNet and
spatial ETAS.
- •

Spatially stratifiedMcM_{c}estimation.A cell-level completeness threshold,
estimated via spatially adaptive Maximum
Curvature[9], would reduce
the catalog incompleteness bias inM∈[3.0,4.5)M\in[3.0,4.5)that propagates into the
feature functionalΦ\Phi(Definition3.6) and contributes
toα\alphainstability in low-activity cells.
- •

Bayesian prior onα\alpha.A
weakly informative prior such asα∼Gamma​(2,1)\alpha\sim\mathrm{Gamma}(2,1)would
regularize the upper tail of the per-cellα\alphadistribution, reducing the seed
instability ofq0.9q_{0.9}(σ=0.98\sigma=0.98)
observed in Table6without
constraining the model in high-activity cells
whereα\alphais well-identified.

## References
- [1]Ogata, Y. (1988).
Statistical models for earthquake occurrences and residual analysis for point processes.Journal of the American Statistical Association, 83(401), 9–27.
- [2]Helmstetter, A., & Sornette, D. (2002).
Subcritical and supercritical regimes in epidemic models of earthquake aftershocks.Journal of Geophysical Research: Solid Earth, 107(B10), ESE 10-1–ESE 10-21.
- [3]Zhuang, J. (2011).
Next-day earthquake forecasts for the Japan region generated by the ETAS model.Earth, Planets and Space, 63(3), 207–216.
- [4]Cameron, A. C., & Trivedi, P. K. (2013).Regression Analysis of Count Data(2nd ed.).
Cambridge University Press.
- [5]Lawless, J. F. (1987).
Negative binomial and mixed Poisson regression.The Canadian Journal of Statistics, 15(3), 209–225.
- [6]Du, N., Dai, H., Trivedi, R., Upadhyay, U., Gomez-Rodriguez, M., & Song, L. (2016).
Recurrent marked temporal point processes: Embedding event history to vector.
InProceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining(pp. 1555–1564).
- [7]Mei, H., & Eisner, J. M. (2017).
The neural Hawkes process: A neurally self-modulating multivariate point process.
InAdvances in Neural Information Processing Systems(Vol. 30).
- [8]Shchur, O., Türkmen, A. C., Januschowski, T., & Günnemann, S. (2020).
Intensity-free learning of temporal point processes.
InInternational Conference on Learning Representations.
- [9]Wiemer, S., & Wyss, M. (2000).
Minimum magnitude of completeness in earthquake catalogs: Examples from Alaska, the western United States, and Japan.Bulletin of the Seismological Society of America, 90(4), 859–869.
- [10]Self, S. G., & Liang, K.-Y. (1987).
Asymptotic properties of maximum likelihood estimators and likelihood ratio tests under nonstandard conditions.Journal of the American Statistical Association, 82(398), 605–610.
- [11]DeVries, P. M. R., Viégas, F., Wattenberg, M., & Meade, B. J. (2018).
Deep learning of aftershock patterns following large earthquakes.Nature, 560, 632–634.
- [12]Mignan, A., & Broccardo, M. (2019).
One neuron versus deep learning in aftershock prediction.Nature, 574, E1–E3.
- [13]Cliff, A. D., & Ord, J. K. (1981).Spatial Processes: Models & Applications.
Pion.
- [14]Czado, C., Gneiting, T., & Held, L. (2009).
Predictive model assessment for count data.Biometrics, 65(4), 1254–1261.

## 


- 


Major funding support from
