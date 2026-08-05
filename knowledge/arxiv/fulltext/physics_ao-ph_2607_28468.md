# Memory compression and physical state augmentation favor different AMOC prediction tasks

**arXiv ID**: 2607.28468v1
**Authors**: Mauricio Herrera-Marín
**Published**: 2026-07-30
**Categories**: physics.ao-ph, math.DS, stat.AP
**HTML URL**: https://arxiv.org/html/2607.28468v1

## Abstract

The Atlantic Meridional Overturning Circulation is monitored and emulated through reduced indices, but such projections discard thermohaline structure and may require either explicit physical state or memory of the observed index. We compare these strategies in 30 branch-consistent CMIP6 trajectories from eight model families using leave-one-family-out validation. Salinity, temperature and density information improves direct 20-year forecasts, whereas compact scalar memory is top-ranked at every recursive horizon and yields the lowest case-averaged Brier score. A matched ablation confirms that feedback from memory improves long-horizon prediction. Physical state and recent trends also predict future ocean-state changes beyond the emissions pathway, most robustly at five years. NorESM under SSP5--8.5 identifies a forcing-dependent limit of scalar compression, while MIROC shows negative long-horizon transfer. A resolvent analysis explains why stable memory components do not guarantee stability of the complete learned model. Physical augmentation and memory compression therefore serve different AMOC prediction tasks.

## Full Text

Memory compression and physical state augmentation favor different AMOC prediction tasks

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- License: CC BY 4.0arXiv:2607.28468v1 [physics.ao-ph] 30 Jul 2026

## Memory compression and physical state augmentation favor different AMOC prediction tasksMauricio Herrera-Marín
Faculty of Engineering, Universidad del Desarrollo, Santiago, ChileCorrespondence:mherrera@udd.cl; ORCID 0000-0002-9604-3077

## Abstract

The Atlantic Meridional Overturning Circulation is monitored and emulated through reduced indices, but such projections discard thermohaline structure and may require either explicit physical state or memory of the observed index. We compare these strategies in 30 branch-consistent CMIP6 trajectories from eight model families using leave-one-family-out validation. Salinity, temperature and density information improves direct 20-year forecasts, whereas compact scalar memory is top-ranked at every recursive horizon and yields the lowest case-averaged Brier score. A matched ablation confirms that feedback from memory improves long-horizon prediction. Physical state and recent trends also predict future ocean-state changes beyond the emissions pathway, most robustly at five years. NorESM under SSP5–8.5 identifies a forcing-dependent limit of scalar compression, while MIROC shows negative long-horizon transfer. A resolvent analysis explains why stable memory components do not guarantee stability of the complete learned model. Physical augmentation and memory compression therefore serve different AMOC prediction tasks.

Keywords:Atlantic Meridional Overturning Circulation; climate prediction; Mori–Zwanzig reduction; memory operator; CMIP6; cross-family transfer; first-passage risk.

## Introduction

The Atlantic Meridional Overturning Circulation (AMOC) redistributes heat, freshwater, carbon and nutrients through the Atlantic and links high-latitude water-mass transformation to climate far beyond the ocean basin. A substantial weakening would alter North Atlantic heat uptake, European climate, tropical rainfall, marine productivity and regional sea level. The assessed consensus is that the AMOC will very likely weaken during the twenty-first century under all Shared Socioeconomic Pathways, while the magnitude of weakening and the likelihood of an abrupt transition remain uncertain1. This uncertainty is not a peripheral detail: it limits the interpretation of early-warning indicators, the construction of reduced emulators for climate-risk assessment and the use of multi-model ensembles to estimate forced AMOC change.

The observational problem is intrinsically one of partial observation. Trans-basin arrays directly measure overturning and its heat and freshwater transports, but their records are short relative to multidecadal variability and forced adjustment2;3;4. Longer reconstructions therefore rely on fingerprints such as subpolar sea-surface temperature, salinity, density gradients, air–sea heat fluxes or freshwater transport. These fingerprints have supported evidence for historical weakening and loss of stability5;6;7;8, but their interpretation is contested because internal variability, atmospheric forcing and non-stationary proxy–AMOC relationships can mimic or obscure a circulation signal9;10;11. Recent observations and reconstructions continue to sharpen, rather than remove, this tension.

The model evidence is equally structured. Rare-event simulations and biased freshwater budgets show that noise, mean-state errors and multistability can reorganize transition pathways12;13. At the same time, a 34-model analysis found a weakened but persistent overturning branch even under extreme greenhouse-gas and freshwater forcing14. Across CMIP6, the spread in future weakening is related to the simulated mean state and to the pathways by which deep and upper-ocean waters connect the Atlantic to the Southern Ocean and Indo-Pacific15; observational constraints can therefore shift projected weakening substantially16. Western-boundary observations additionally indicate a meridionally coherent decline that is only partly compensated elsewhere in the basin17. Together, these studies show that AMOC uncertainty is not simply uncertainty in one scalar amplitude. It reflects how different models represent thermohaline structure, overturning pathways, forced drift and memory across timescales.

This creates a specific gap for reduced climate prediction. Most AMOC warning studies choose a scalar fingerprint and ask whether its trend, variance or autocorrelation changes. Most emulators instead enlarge the predictor set with physical covariates. What has not been established is whether discarded ocean structure should be retained asinstantaneous physical stateor represented asmemory of a reduced AMOC observable, and whether the answer changes between two climate tasks: a forecast fitted separately at a fixed lead and a single learned operator propagated recursively. These tasks are often conflated, although they impose different requirements. Fixed-horizon prediction rewards any state information correlated with the target at that lead. Recursive rollout additionally demands a compact representation whose own forecast errors do not amplify under repeated application.

Mori–Zwanzig projection provides a principled framework for this comparison. Eliminating unresolved coordinates yields an instantaneous resolved tendency, a history-dependent feedback and orthogonal dynamics18;19;20. In climate dynamics, this formalism justifies delay and non-Markovian closures rather than adding lags only heuristically21;22;23. Recent reduced-order work likewise shows that memory can improve partially observed dynamics, but it also raises a stability question that is especially relevant for climate emulators: stable hidden memory modes do not necessarily imply that the complete resolved–memory map is contractive24;25.

Here we connect this projection problem to cross-model AMOC prediction. We derive a matrix Schur–resolvent criterion that identifies the restoring balance after hidden variables are eliminated and separates hidden-pole stability from stability of the complete learned operator. We then test scalar memory, vector physical state and finite-lag alternatives on 30 branch-consistent historical–scenario trajectories from eight CMIP6 model families. The outer split leaves out an entire family, so success measures transfer across structural model differences rather than interpolation among members of the same family. We evaluate direct prediction, recursive rollout, probabilistic first-passage risk, matched memory ablations, cross-family physical-state information and local Jacobian geometry. Figure1summarizes the design. Our principal finding is bidirectional: explicit thermohaline information improves fixed-horizon 20-year forecasts, whereas compact scalar memory is the most consistently top-ranked representation for recursive transfer. The forcing-dependent NorESM crossover and the negative MIROC transfer identify where that compression ceases to be sufficient.Figure 1:Cross-family design separates fixed-horizon and recursive AMOC prediction.Branch-consistent CMIP6 trajectories support two complementary tasks. Horizon-specific direct forecasts measure the value of explicit physical state at a fixed lead, whereas recursive rollouts measure transfer of one propagated operator. Schur–resolvent diagnostics distinguish stable hidden memory from local stability of the complete resolved–memory map. All preprocessing and model selection exclude the held-out climate-model family, and no prediction uses future physical forcing.

## Results

## Prediction task changes the preferred AMOC representation

The direct experiment fits an independent map at each lead. At one year, scalar ARX has the lowest pooled RMSE, consistent with a short-lead problem dominated by the recent AMOC state. At 20 years, the ordering reverses: scalar ARX has RMSE 1.595, whereas vector lag, oscillatory vector Mori–Zwanzig (MZ) and real vector MZ reach 1.297, 1.300 and 1.317, respectively. The 0.003 difference between vector lag and oscillatory MZ is negligible relative to family variation. Thus salinity, temperature and density summaries carry long-lead information that is absent from the scalar index, but no unique advantage of a vector MZ closure over an explicit finite-lag state is resolved (Fig.2a).

The recursive experiment asks a different question by propagating one learned operator over all horizons. Scalar MZ is top-ranked in mean error at 1, 5, 10 and 20 years (Fig.2b). At 20 years, mean family–seed MSE is 2.336 for scalar MZ, compared with 2.985 for vector lag, 3.042 for signed-real MZ and 3.355 for signed-oscillatory MZ. The corresponding equal-family RMSE is 1.381 for scalar MZ. The contrast between panels is the central empirical result: physical augmentation improves a lead-specific mapping, but the compact memory representation accumulates less cross-family error when its own outputs become future inputs.Figure 2:Fixed-horizon and recursive prediction favor different reduced states.a, Equal-family RMSE for horizon-specific direct prediction; shading gives 95% family-bootstrap intervals. Physical-state models improve the 20-year forecast, while vector lag and vector MZ are nearly tied.b, Equal-family RMSE for recursive rollout after averaging the three seeds within family; shading gives 95% family-bootstrap intervals. Scalar MZ is top-ranked at every horizon.

The recursive ranking is consistent but not a claim of universal statistical superiority. Scalar MZ is better than vector lag in six of eight families at 20 years, yet the exact two-sided family test givesp=0.3125p=0.3125. None of the seven secondary scalar-MZ architecture comparisons survives Holm correction at 0.05; the minimum adjusted value is 0.0547. We therefore describe scalar MZ as the strongest default and the most consistently top-ranked recursive representation in this benchmark, not as uniformly superior to every vector alternative.

## Forcing and model family expose structured limits of scalar compression

The family-level pattern reveals why a single average ranking is incomplete (Fig.3a). Scalar MZ has lower 20-year MSE than vector lag in ACCESS, CanESM5, FGOALS, INM, MIROC and MPI, is nearly tied in CESM2, and is worse in NorESM. The NorESM difference is organized by both lead and forcing pathway. Under SSP1–2.6 and SSP2–4.5, scalar MZ is better at 1–5 years but vector lag crosses over by 10 years. Under SSP5–8.5, vector lag is better from the first horizon and retains a 20-year MSE advantage of 4.70 (Fig.3b).

This crossover is not adequately described as generic out-of-distribution failure. NorESM origin states are well separated from the training-family state distribution, but other strongly separated families do not show the same ranking. Moreover, the NorESM conditional transition residual falls below the training-family reference at 20 years, when the vector-lag advantage is largest. The evidence instead points to a forcing-dependent limit of compression: recent multivariate physical history contains target-relevant structure that the scalar AMOC trajectory does not always retain.Figure 3:Recursive transfer is heterogeneous across climate-model families.a, Log MSE ratio at 20 years for each alternative relative to scalar MZ; positive values favor scalar MZ.b, NorESM differenceMSEscalar​MZ−MSEvector​lag\mathrm{MSE}_{\mathrm{scalar\,MZ}}-\mathrm{MSE}_{\mathrm{vector\,lag}}. Positive values indicate a vector-lag advantage. The crossover occurs by 10 years in SSP1–2.6 and SSP2–4.5 and is present at every horizon in SSP5–8.5.

## Matched ablation identifies memory feedback rather than hidden capacity

The confirmatory mechanistic comparison isolates the return path from hidden memory to the resolved AMOC increment. Signed-oscillatory MZ and its no-feedback ablation retain the same hidden coordinates and Schur-stable poles, but the ablation removes hidden-to-resolved feedback. At 20 years, the feedback model has lower MSE in seven of eight families, with mean paired difference−2.280-2.280and exact two-sidedp=0.03125p=0.03125. The result supports memory feedback as a predictive mechanism rather than hidden capacity alone. It does not establish a privileged oscillatory kernel: signed-real and signed-oscillatory variants are not resolved from each other, and vector lag remains statistically tied with the oscillatory model.

## Probability accuracy and event discrimination favor different models

Residual-resampled rollouts generate cumulative first-passage probabilities for a model-relative sustained AMOC weakening event. After averaging the three seeds for each unique forecast case, scalar MZ has the lowest Brier score at 5, 10 and 20 years. At 20 years its Brier score is 0.1441, ROC-AUC 0.8148 and average precision 0.6989. Mean forecast probability is 0.332 against prevalence 0.248, indicating moderate overprediction; the calibration slope is 0.906 and the intercept is−0.599-0.599.

The lowest Brier score does not imply the strongest event ranking. Vector lag and multivariate MZ models have higher macro-averaged discrimination at 20 years. Figure4a therefore separates probability accuracy from discrimination: scalar MZ produces the best average probabilities, whereas vector representations preserve stronger ranking information in some summaries. Reliability curves (Fig.4b) show close agreement at low risk and increasing long-horizon overprediction at intermediate probabilities. Scalar MZ has lower family-level Brier than four matched alternatives in all eight families, but none of nine secondary Brier comparisons survives Holm correction (minimum adjustedp=0.0703p=0.0703). The first-passage results are consequently used to compare representations, not to forecast an imminent real-world AMOC collapse.Figure 4:Probability accuracy and discrimination separate under long-horizon rollout.a, Brier score versus ROC-AUC at 20 years after averaging seeds by forecast case. Lower Brier is better; scalar MZ is most accurate, whereas vector models retain stronger discrimination.b, Scalar-MZ reliability at 5, 10 and 20 years. The dashed line denotes perfect reliability.

## Physical state retains dynamical information beyond the emissions pathway

The four-dimensional origin state—subpolar salinity, subpolar and subtropical temperature, and their density contrast—contains strong model-family fingerprints. Across 22 available family–scenario combinations, mean domain-classifier AUC is 0.938 and held-out states frequently lie beyond the training-family support. Yet marginal state separation does not predict relative 20-year performance, and neither static Mahalanobis distance nor maximum mean discrepancy explains the NorESM crossover (Supplementary Note 8).

We therefore tested a more climate-relevant question: after conditioning on SSP, does present thermohaline structure contain transferable information about future ocean-state adjustment? For each horizon, a nested leave-one-family-out ridge model predictsΔ​Xh=Xt+h−Xt\Delta X_{h}=X_{t+h}-X_{t}from the origin state, retrospective 5- and 10-year trends and SSP indicators. The baseline is the training-family mean transition within the same SSP. Conditional skill is𝒮h=1−MSEconditionalMSESSP​mean.\mathcal{S}_{h}=1-\frac{\mathrm{MSE}_{\mathrm{conditional}}}{\mathrm{MSE}_{\mathrm{SSP\ mean}}}.(1)

Mean equal-family skill is 0.088 at one year and 0.157 at five years, with 95% family-bootstrap intervals[0.020,0.152][0.020,0.152]and[0.096,0.215][0.096,0.215]. Five-year skill is positive in all eight families and remains significant in an exact two-sided family test after Holm correction across horizons (pHolm=0.03125p_{\mathrm{Holm}}=0.03125). At 10 and 20 years, seven of eight families remain positive, but the intervals include zero because MIROC exhibits strong negative transfer (Fig.5a).

The long-horizon signal is strongest under SSP5–8.5. For NorESM, conditional physical skill reaches 0.332, 0.293 and 0.449 at 5, 10 and 20 years, respectively, while vector lag outperforms scalar MZ throughout that pathway (Fig.5b). Across the seven families represented in all three SSPs, the 20-year contrast between SSP5–8.5 and the mean of SSP1–2.6/SSP2–4.5 is positive in six families, but does not survive adjustment across horizons. We therefore interpret stronger long-horizon physical information under intense forcing as structured exploratory evidence. The general result is firmer: the physical state is not redundant with the emissions pathway, although its value for choosing an AMOC architecture is family dependent.Figure 5:Thermohaline state carries information beyond the SSP pathway.a, Conditional skill for predicting future physical-state changes relative to an SSP-only transition-mean baseline. Each cell averages the available scenarios within a family; FGOALS contributes SSP5–8.5 only.b, NorESM conditional skill by SSP and the SSP5–8.5 scalar-MZ minus vector-lag MSE difference. High physical skill and vector-lag advantage coexist under strong forcing, but the association is not systematic across families.

## A resolvent criterion separates projected restoring feedback from full-map stability

To connect the empirical rankings to reduced climate dynamics, consider a sampled lifted state with resolved coordinateqn∈ℝdq_{n}\in\mathbb{R}^{d}and hidden memoryzn∈ℝmz_{n}\in\mathbb{R}^{m}. Around a frozen state,(qn+1zn+1)=J​(qnzn),J=(ABCD),rad⁡(D)<1.\begin{pmatrix}q_{n+1}\\
z_{n+1}\end{pmatrix}=J\begin{pmatrix}q_{n}\\
z_{n}\end{pmatrix},\qquad J=\begin{pmatrix}A&B\\
C&D\end{pmatrix},\qquad\operatorname{rad}(D)<1.(2)

Eliminating the hidden state generates the matrix lag kernelKk=B​Dk−1​CK_{k}=BD^{k-1}C.

## Theorem 1(Schur–resolvent criterion).

For everyζ∉spec⁡(D)\zeta\notin\operatorname{spec}(D), defineΦ​(ζ)=ζ​Id−A−B​(ζ​Im−D)−1​C.\Phi(\zeta)=\zeta I_{d}-A-B(\zeta I_{m}-D)^{-1}C.(3)

Thendet(ζ​Id+m−J)=det(ζ​Im−D)​detΦ​(ζ).\det(\zeta I_{d+m}-J)=\det(\zeta I_{m}-D)\det\Phi(\zeta).(4)

Writing𝒩j=B​(I−D)−(j+1)​C\mathcal{N}_{j}=B(I-D)^{-(j+1)}C, a stationary unit multiplier occurs if and only ifdet(Id−A−𝒩0)=0.\det(I_{d}-A-\mathcal{N}_{0})=0.(5)

Equation (5) is the exact restoring balance seen by the projected AMOC state. The instantaneous resolved blockAAis renormalized by the integrated memory feedback𝒩0\mathcal{N}_{0}; neither term is interpretable in isolation. For a simple slow direction, the same resolvent reconstructs the multiplier asρslow=1+δγ+ℓ⊤​(𝒩2+H​G​Q​H)​rγ3​δ2+O​(δ3),\rho_{\mathrm{slow}}=1+\frac{\delta}{\gamma}+\frac{\ell^{\top}(\mathcal{N}_{2}+HGQH)r}{\gamma^{3}}\delta^{2}+O(\delta^{3}),(6)

whereH=Id+𝒩1H=I_{d}+\mathcal{N}_{1},Q=I−r​ℓ⊤Q=I-r\ell^{\top}andGGis the reduced inverse on the complement of the slow mode. TheH​G​Q​HHGQHterm records coupling between the slow AMOC-like direction and the remaining resolved physical modes. Full proofs, the continuous-time limit, general unit-circle crossings, and stable signed and oscillatory realizations are given in Supplementary Notes 1–6.

All fitted MZ realizations have Schur-stable hidden blocks, and all nonlinear rollouts remain finite. The complete local Jacobian is nevertheless not uniformly contractive. Scalar MZ is locally Schur stable at 64.0% of evaluated states, compared with 3.5% and 4.4% for signed-real and signed-oscillatory MZ. Its 95th-percentile full spectral radius is also smaller (1.115 versus 1.466 and 1.561), and lower expansion co-occurs with lower 20-year error (Fig.6). Stable hidden memory therefore licenses the realization but does not establish stability of the complete learned climate emulator. Our claim is bounded predictive rollout with audited local geometry, not global asymptotic stability or evidence that the real AMOC is near a mathematical bifurcation.Figure 6:Stable memory components do not guarantee a contractive AMOC emulator.a, Fraction of evaluated states with complete-Jacobian spectral radius below one.b, 95th-percentile full local spectral radius versus equal-family 20-year RMSE. The dashed line marks unit spectral radius. Hidden memory blocks are stable for all MZ fits, but complete maps are only intermittently contractive.

## Discussion

The central climate result is that physical state augmentation and memory compression answer different prediction questions. Thermohaline structure improves direct 20-year forecasts because salinity, temperature and density gradients contain information about the future forced state that is absent from a single AMOC index. Recursive rollout imposes a second requirement: the representation must remain stable and transferable when forecast states are repeatedly reused. Under that requirement, scalar memory is the most consistently top-ranked default across model families and horizons. The two findings are complementary rather than contradictory.

This distinction matters for the interpretation of AMOC fingerprints. A reduced SST or salinity index is not expected to be a sufficient physical state; its apparent persistence can arise from unresolved ocean adjustment, remote forcing and coupled feedbacks. The present results show that part of this discarded information can be recovered through memory of the index, but not in every forcing regime. Consequently, early-warning and attribution studies should distinguish three propositions that are often merged: a fingerprint may correlate with AMOC strength, its history may improve prediction, and it may contain enough state information for recursive extrapolation. Our experiment supports the second proposition broadly, the third only conditionally, and does not use either as a direct estimate of real-world tipping time.

The results also inform climate emulators and multi-model constraints. A lead-specific emulator intended to estimate AMOC weakening at 2100 can benefit from explicit thermohaline predictors, consistent with the growing use of salinity, temperature and overturning-pathway information to constrain CMIP6 projections. A generative emulator used for first-passage probabilities, scenario exploration or sequential data assimilation should additionally control recursive error and full-map expansion. In such applications, selecting the state only by one-step or fixed-horizon skill can favor a representation that is less robust when propagated. Task-specific validation should therefore be treated as part of the climate question, not as a technical afterthought.

NorESM SSP5–8.5 and MIROC make the implications concrete. NorESM shows that strong forced drift can preserve long-horizon physical information and favor explicit vector lags even when scalar memory remains competitive elsewhere. MIROC shows the opposite failure mode: adding physical state can transfer negatively across families at long horizons. These exceptions argue against a universal AMOC fingerprint or a universal reduced state. They instead motivate adaptive emulators that use compact scalar memory as a cross-family baseline and activate multivariate physical history when trajectory diagnostics indicate forcing-dependent residual information.

The Schur–resolvent result provides the dynamical interpretation. Projecting a high-dimensional circulation does not remove unresolved feedback; it moves that feedback into a memory kernel. The relevant local threshold is therefore a Schur complement involving both resolved drift and integrated memory. Stable hidden poles are useful because they prevent an internally divergent memory realization, but they do not imply that the complete emulator is contractive. This matters for early-warning language: a learned spectral radius, autocorrelation increase or slow multiplier is a property of a chosen projection and fitted map. It should not be equated automatically with the stability margin of the full ocean circulation.

The statistical evidence is deliberately tiered. The matched feedback ablation is confirmatory and supports hidden-to-resolved memory feedback. Five-year conditional physical skill is also robust after correction across horizons. By contrast, scalar MZ versus vector lag is a descriptive ranking supported by consistency across recursive horizons and Brier scores, not by a significant pairwise test with eight families. This distinction limits the headline to what the design can establish: scalar memory is the strongest default in the evaluated cross-family rollout benchmark, while physical augmentation remains indispensable for fixed-lead prediction and identifiable forced regimes.

Several boundaries remain. Eight model families provide strict structural validation but limited family-level power, and shared components reduce their effective independence. FGOALS contributes SSP5–8.5 only, so balanced-family sensitivity is necessary for scenario averages. Surface salinity, temperature and density summaries do not exhaust freshwater transports, deep-ocean heat content, wind-driven pathways or Southern Ocean controls. The first-passage threshold is model relative and is not an estimate of collapse probability in the observed climate. Current observationally constrained projections and reconstructions remain in tension11;16;17; this study addresses how reduced representations transfer across climate models rather than adjudicating those observational claims.

The next step is to couple representation selection to observations and process diagnostics. Direct arrays, boundary-density estimates, freshwater transports and emerging subsurface fingerprints could be used to determine when a scalar history is sufficient and when additional physical coordinates are required. Stability-constrained training of the complete Jacobian, rather than only the hidden block, offers a complementary route. The broader implication is that uncertainty in AMOC prediction is partly uncertainty about representation: what appears as a loss of predictability in one reduced index may be recoverable as memory, while what appears as memory failure may signal missing thermohaline state.

## Methods

## Continuous and sampled hidden-variable elimination

For a continuous linearization with resolved stateq∈ℝdq\in\mathbb{R}^{d}and hidden states∈ℝms\in\mathbb{R}^{m},dd​t​(qs)=(AcBcCcDc)​(qs),\frac{\mathrm{d}}{\mathrm{d}t}\begin{pmatrix}q\\
s\end{pmatrix}=\begin{pmatrix}A_{c}&B_{c}\\
C_{c}&D_{c}\end{pmatrix}\begin{pmatrix}q\\
s\end{pmatrix},(7)

a HurwitzDcD_{c}gives the exact Volterra equationq˙​(t)=Ac​q​(t)+∫0tBc​eDc​(t−τ)​Cc​q​(τ)​dτ+Bc​eDc​t​s​(0).\dot{q}(t)=A_{c}q(t)+\int_{0}^{t}B_{c}e^{D_{c}(t-\tau)}C_{c}q(\tau)\,\mathrm{d}\tau+B_{c}e^{D_{c}t}s(0).(8)

The integrated feedback is𝒳0=−Bc​Dc−1​Cc\mathcal{X}_{0}=-B_{c}D_{c}^{-1}C_{c}. In sampled time, eliminatingznz_{n}from Eq. (2) givesKk=B​Dk−1​CK_{k}=BD^{k-1}C. Resolvent moments𝒩j=B​(I−D)−(j+1)​C\mathcal{N}_{j}=B(I-D)^{-(j+1)}Cyield Eqs. (5) and (6). Proofs, the continuous–discrete limit and the general unit-circle crossing formula are supplied in the Supplementary Information.

## CMIP6 cohort and climate variables

The study uses the Coupled Model Intercomparison Project Phase 6 archive26. The audited cohort contains 30 branch-consistent historical–scenario trajectories from eight model families: ACCESS, CESM2, CanESM5, FGOALS, INM, MIROC, MPI and NorESM. Ten trajectories follow SSP1–2.6, ten SSP2–4.5 and ten SSP5–8.5. Historical and scenario segments are stitched only when source, member, grid and variable identity agree. The physical source variables are sea-surface salinity (sos), sea-surface temperature (tos) and grid-cell area (areacello). Annual summaries include subpolar salinity, subpolar and subtropical temperature, density proxies and the subpolar–subtropical density contrast. The resolved target is an annual AMOC-strength index. The database passed duplicate-key, annual-coverage and historical-to-scenario transition audits.

All standardization, learned feature transformations and hyperparameter selection are fitted within the outer training families. The held-out family is excluded from preprocessing and selection. Models receive only physical values available at the forecast origin and retrospective information. No model receives future physical forcing. This design tests transfer across climate-model structure rather than interpolation among trajectories from the same family.

## Direct horizon-specific prediction

A separate predictor is fitted at each horizonh∈{1,5,10,20}h\in\{1,5,10,20\}years. Models are scalar ARX, vector lag, signed-real vector MZ and damped-oscillatory vector MZ. Hyperparameters are selected using training families only. Performance is reported as RMSE, with family-bootstrap intervals based on the eight held-out families. This protocol tests representation value at a fixed lead and is not interpreted as a recursive dynamical simulation.

## Recursive rollout and matched ablations

The recursive operator propagates resolved and hidden states asqn+1\displaystyle q_{n+1}=8​tanh⁡(qn+Δ​qθ​(qn,zn,un)8),\displaystyle=8\tanh\!\left(\frac{q_{n}+\Delta q_{\theta}(q_{n},z_{n},u_{n})}{8}\right),(9)zn+1\displaystyle z_{n+1}=C​qn+D​zn.\displaystyle=Cq_{n}+Dz_{n}.(10)

The saturation lies outside the observed standardized range and prevents non-finite trajectories; it is part of the propagated map rather than a post-hoc clip. The ten architectures are scalar MZ, vector lag, signed-real MZ, signed-oscillatory MZ, positive-real MZ, shifted-memory placebo, random-reservoir memory, no-feedback memory, capacity-matched joint Markov and capacity-matched scalar ARX. The final design contains eight held-out families, ten architectures and three random seeds, for 240 jobs. All 240 completed, with no failed or missing jobs.

The prespecified mechanistic comparison is signed-oscillatory MZ versus its no-feedback ablation at 20 years. The broader scalar-MZ architecture comparisons are secondary. Seeds are averaged within family before family-level inference.

## First-passage probability audit

The event is the first occurrence of at least three consecutive annual AMOC values below 70% of the model-specific historical mean, conditional on no previous event. Residual-resampled stochastic rollouts yield cumulative event probabilities. Probabilities from the three seeds are averaged for each unique trajectory–origin–horizon case before scoring, leaving 306 cases per model and horizon. Metrics are Brier score, log loss, ROC-AUC, average precision, calibration intercept, calibration slope and the reliability–resolution–uncertainty decomposition27;28.

## Cross-family state shift and conditional physical dynamics

Static shift is evaluated in the four-dimensional origin state(sosS​P​G,tosS​P​G,tosS​T​G,Δ​ρS​P​G−S​T​G)(\mathrm{sos}_{SPG},\mathrm{tos}_{SPG},\mathrm{tos}_{STG},\Delta\rho_{SPG-STG})using Ledoit–Wolf Mahalanobis distance, training-support exceedance, nearest-neighbor distance, radial-basis maximum mean discrepancy and a held-family domain classifier. Because annual origins within a trajectory are dependent, these statistics are treated primarily as descriptive diagnostics.

For the conditional transition analysis, the target at horizonhhisΔ​Xh=Xt+h−Xt\Delta X_{h}=X_{t+h}-X_{t}. Predictors areXtX_{t}, five- and ten-year retrospective trends and SSP indicators. A multi-output ridge model is trained on seven families and evaluated on the eighth. The ridge penalty is selected by an inner leave-one-family-out loop. The baseline is the training-family meanΔ​Xh\Delta X_{h}within SSP. Residual normalization uses scenario-specific inner out-of-family predictions rather than in-sample errors. Family-cluster bootstrap intervals use 5,000 replicates.

## Local stability diagnostics

Automatic differentiation of the complete propagated map gives local Jacobian blocksA,B,C,DA,B,C,D. Hidden stability israd⁡(D)<1\operatorname{rad}(D)<1. Full local stability israd⁡(J)<1\operatorname{rad}(J)<1forJJin Eq. (2). We report the stable fraction, 95th percentile and maximum over evaluated states. Hidden-pole stability is checked separately because it does not imply full-map contraction.

## Statistics and reproducibility

Climate-model family is the inferential unit (n=8n=8). Exact two-sided sign-flip tests enumerate all282^{8}family sign configurations and require no normality assumption. The prespecified feedback contrast is evaluated separately atα=0.05\alpha=0.05. Secondary architecture families are corrected by Holm’s sequential procedure29. Family-bootstrap intervals resample families with replacement and preserve all cases within the selected family. For conditional transition skill, two-sided exact tests across the four horizons are Holm-adjusted; only the five-year effect remains below 0.05. Cross-family shift–performance associations are exploratory and none survives correction across the tested association family. Exact sample sizes, comparison families and unadjusted and adjustedppvalues are reported in the Supplementary Information and source tables.

## Code availability

The analysis code, frozen protocol, environment records, processed source data supporting all figures and tables, derived results, and reproducibility audits are available athttps://github.com/mauricio-herrera/amoc-mz-physical-v4. The version-specific public package is archived on Zenodo athttps://doi.org/10.5281/zenodo.21606982. Raw CMIP6 files are not redistributed; their provenance, model and member identifiers, processing contracts, validation audits, and reconstruction procedures are documented in the archived release.

## Data availability

CMIP6 source fields are available through the Earth System Grid Federation under the terms of the contributing modelling centres and are not redistributed in this repository. The public package provides the model, member, grid, experiment and variable identifiers, extraction and validation procedures, and compact derived data underlying every figure and table. The version-specific archival record is available on Zenodo athttps://doi.org/10.5281/zenodo.21606982.

## Acknowledgements

The author acknowledges institutional support from Universidad del Desarrollo. This work received no specific financial support from any public, commercial, or not-for-profit funding agency.

## Author contributions

M.H.-M. conceived the study, developed the mathematical framework and software, curated and audited the data, performed the analysis, interpreted the results and wrote the manuscript.

## Competing interests

The author declares no financial or non-financial competing interests.

## References
- 1IPCC. Ocean, cryosphere and sea level change. InClimate Change 2021: The Physical Science Basis(eds Masson-Delmotte, V. et al.) 1211–1362 (Cambridge Univ. Press, 2021).
- 2Buckley, M. W. & Marshall, J. Observations, inferences, and mechanisms of Atlantic Meridional Overturning Circulation variability: a review.Rev. Geophys.54, 5–63 (2016).
- 3Frajka-Williams, E. et al. Atlantic Meridional Overturning Circulation: observed transport and variability.Front. Mar. Sci.6, 260 (2019).
- 4Weijer, W. et al. Stability of the Atlantic Meridional Overturning Circulation: a review and synthesis.J. Geophys. Res. Oceans124, 5336–5375 (2019).
- 5Rahmstorf, S. et al. Exceptional twentieth-century slowdown in Atlantic Ocean overturning circulation.Nat. Clim. Change5, 475–480 (2015).
- 6Boers, N. Observation-based early-warning signals for a collapse of the Atlantic Meridional Overturning Circulation.Nat. Clim. Change11, 680–688 (2021).
- 7Ditlevsen, P. & Ditlevsen, S. Warning of a forthcoming collapse of the Atlantic meridional overturning circulation.Nat. Commun.14, 4254 (2023).
- 8van Westen, R. M., Kliphuis, M. & Dijkstra, H. A. Physics-based early warning signal shows that AMOC is on tipping course.Sci. Adv.10, eadk1189 (2024).
- 9Ben-Yami, M., Morr, J., Bathiany, S. & Boers, N. Uncertainties too large to predict tipping times of major Earth system components from historical data.Sci. Adv.10, eadl4841 (2024).
- 10Latif, M. et al. Natural variability has dominated Atlantic Meridional Overturning Circulation since 1900.Nat. Clim. Change12, 455–460 (2022).
- 11Terhaar, J., Vogt, L. & Foukal, N. P. Atlantic overturning inferred from air–sea heat fluxes indicates no decline since the 1960s.Nat. Commun.16, 222 (2025).
- 12Cini, M. et al. Simulating AMOC tipping driven by internal climate variability with a rare event algorithm.npj Clim. Atmos. Sci.7, 31 (2024).
- 13Boot, A. A. & Dijkstra, H. A. Physics of AMOC multistable regime shifts due to freshwater biases in an EMIC.Earth Syst. Dyn.16, 1221–1235 (2025).
- 14Baker, J. A. et al. Continued Atlantic overturning circulation even under climate extremes.Nature638, 987–994 (2025).
- 15Baker, J. A. et al. Overturning pathways control AMOC weakening in CMIP6 models.Geophys. Res. Lett.50, e2023GL103381 (2023).
- 16Portmann, V., Swingedouw, D., Khattab, O. & Chavent, M. Observational constraints project a∼\sim50% AMOC weakening by the end of this century.Sci. Adv.12, eadx4298 (2026).
- 17Xing, Q. et al. Meridionally consistent decline in the observed western boundary contribution to the Atlantic Meridional Overturning Circulation.Sci. Adv.12, eadz7738 (2026).
- 18Mori, H. Transport, collective motion, and Brownian motion.Prog. Theor. Phys.33, 423–455 (1965).
- 19Zwanzig, R. Nonlinear generalized Langevin equations.J. Stat. Phys.9, 215–220 (1973).
- 20Chorin, A. J. & Hald, O. H.Stochastic Tools in Mathematics and Science, 3rd edn (Springer, 2013).
- 21Falkena, S. K. J., Quinn, C., Sieber, J., Frank, J. & Dijkstra, H. A. Derivation of delay equation climate models using the Mori–Zwanzig formalism.Proc. R. Soc. A475, 20190075 (2019).
- 22Kondrashov, D., Chekroun, M. D. & Ghil, M. Data-driven non-Markovian closure models.Physica D297, 33–55 (2015).
- 23Lin, K. K. & Lu, F. Data-driven model reduction, Wiener projections, and the Koopman–Mori–Zwanzig formalism.J. Comput. Phys.424, 109864 (2021).
- 24Gupta, P., Schmid, P. J., Sipp, D., Sayadi, T. & Rigas, G. Mori–Zwanzig latent-space Koopman closure for nonlinear autoencoders.Proc. R. Soc. A481, 20240259 (2025).
- 25Buitrago Ruiz, R., Marwah, T., Gu, A. & Risteski, A. On the benefits of memory for modeling time-dependent PDEs. InInternational Conference on Learning Representations(2025).
- 26Eyring, V. et al. Overview of the Coupled Model Intercomparison Project Phase 6 experimental design and organization.Geosci. Model Dev.9, 1937–1958 (2016).
- 27Brier, G. W. Verification of forecasts expressed in terms of probability.Mon. Weather Rev.78, 1–3 (1950).
- 28Murphy, A. H. A new vector partition of the probability score.J. Appl. Meteorol.12, 595–600 (1973).
- 29Holm, S. A simple sequentially rejective multiple test procedure.Scand. J. Stat.6, 65–70 (1979).

## 


- 


Major funding support from
