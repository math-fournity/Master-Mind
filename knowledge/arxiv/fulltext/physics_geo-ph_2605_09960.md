# Total Generalized Variation regularization closes the gap between neural-eld and classical methods in seismic travel-time tomography

**arXiv ID**: 2605.09960v1
**Authors**: Isao Kurosawa
**Published**: 2026-05-11
**Categories**: physics.geo-ph, cs.LG, math.NA
**Comments**: 15 pages, 6 figures. Manuscript submitted to Geophysical Journal International
**HTML URL**: https://arxiv.org/html/2605.09960v1

## Abstract

Travel-time tomography forces a trade-off between mesh resolution and stability in which the regularizer choice dominates what can be recovered. We introduce MIMIR, a differentiable framework that represents the 2D velocity field as a Fourier-feature neural network, replacing the grid-based slowness vector with a continuous, infinitely differentiable function. Prior neural-field tomography has staircased smooth fields under total-variation (TV) priors or oscillated near interfaces under $L^2$ Laplacian smoothing. We adopt second-order total generalized variation (TGV$^2$) and parametrize its auxiliary vector field as a second neural network jointly optimized with the velocity field, eliminating the inner Chambolle-Pock primal-dual loop that classically dominates TGV computation. On three synthetic benchmarks (Gaussian, horizontally layered, curved-fault inspired by OpenFWI) using cross-well acquisition, 5% travel-time noise, and five seeds, MIMIR-TGV$^2$ ties a classical FMM-LSMR baseline with auto-tuned hyperparameters on the Gaussian ($p=0.134$, paired $t$-test) and significantly outperforms it on layered ($p<0.0001$, 44% RMSE reduction) and curved-fault ($p=0.0002$, 33% reduction). Replacing TGV$^2$ with TV degrades performance on Gaussian ($p=0.004$) and layered ($p=0.003$); curriculum-annealed TV improves Gaussian RMSE by only 5.4%, confirming that TV's staircase bias is intrinsic to the regularizer rather than a scheduling artifact. The results empirically validate the Bredies-Kunisch-Pock prediction that piecewise-affine priors are better suited to subsurface velocity recovery than piecewise-constant TV priors. We argue that the central design choice in physics-informed neural-field inversion is not the network architecture but the regularizer. The full pipeline reproduces in under one hour on consumer hardware.

## Full Text

Total Generalized Variation regularization closes the gap between neural-field and classical methods in seismic travel-time tomography

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2605.09960v1 [physics.geo-ph] 11 May 2026

## Total Generalized Variation regularization closes the gap between
neural-field and classical methods in seismic travel-time tomographyIsao KurosawaIVXA, Japan. Correspondence: contact form athttps://ivxa.ai(May 11, 2026)

## Abstract

Travel-time tomography is foundational to seismic imaging in geothermal,
carbon-storage and crustal-structure applications, but its discretized
formulation forces a difficult choice between mesh resolution and inversion
stability. We introduce MIMIR, a differentiable framework that represents
the two-dimensional velocity field as a coordinate-based neural network
with Fourier feature embedding, replacing the conventional grid-based
slowness vector with a continuous, infinitely differentiable function.
The regularization choice has been a long-standing weakness of neural-field
tomography: total variation (TV) priors used in prior work staircase
smooth fields, while quadratic Laplacian smoothing oscillates near sharp
interfaces. We adopt second-order total generalized variation (TGV2)
and parametrize its auxiliary vector field as a second neural network
jointly optimized with the velocity field, eliminating the inner
Chambolle–Pock primal–dual loop that classically dominates TGV
computation. We validate the framework on three controlled synthetic
benchmarks (a smooth Gaussian anomaly, a horizontally layered model with
an embedded heterogeneity, and a curved-fault model inspired by the
OpenFWI family) using a cross-well acquisition with5%/5\text{\,}\mathrm{\char 37\relax}\text{/}multiplicative travel-time noise and five independent random seeds per
benchmark. Against a textbook classical baseline (fast marching forward,
curved-ray back-tracing, regularized LSMR with Tikhonov damping and
two-dimensional Laplacian smoothing, hyperparameters auto-tuned per
benchmark), MIMIR-TGV2is statistically indistinguishable from the
classical method on the smooth Gaussian benchmark
(p=0.134p=0.134, paired Student’stt-test) and significantly outperforms it
on the layered (p<0.0001p<0.0001,44%44\,\%root-mean-square-error reduction)
and curved-fault (p=0.0002p=0.0002,33%33\,\%reduction) benchmarks.
Replacing TGV2with TV degrades performance significantly on the
Gaussian (p=0.004p=0.004) and layered (p=0.003p=0.003) benchmarks. Curriculum
annealing of the TV weight produces only a5.4%5.4\,\%improvement on the
Gaussian benchmark and no significant change elsewhere, confirming that
TV’s staircase bias is intrinsic to the regularizer rather than a
scheduling artifact. Our results empirically validate the
Bredies–Kunisch–Pock theoretical prediction that piecewise-affine
priors are better suited to subsurface velocity recovery than the
piecewise-constant priors implied by TV. We argue that the central
design choice in physics-informed neural-field inversion is not the
network architecture but the regularizer, and that practitioners should
select the regularizer based on the expected geological structure
rather than on computational convenience. The full pipeline reproduces
from a single command on consumer hardware in under one hour.

Keywords:Seismic tomography; Inverse theory;
Computational seismology; Wave propagation; Numerical modeling.

## 1Introduction

Travel-time tomography has been a cornerstone of seismic imaging for half a
century, from the seminal work ofAki and Lee (1976)on three-dimensional
crustal structure beneath seismic arrays through the modern era of regional
and global Earth-structure imaging(Thurber,1983; Zhang and Thurber,2003; Liu and Tromp,2008; Tape et al.,2010). Its appeal is simplicity: the forward map is
the line integral of slowness along ray paths, and a regularized
least-squares update suffices to invert travel-time residuals into velocity
perturbations. The same problem statement underlies microseismic
event-location pipelines, ambient-noise tomography, induced-seismicity
monitoring, and the velocity-model-building stages of full-waveform
inversion(Sun and Williamson,2024). Despite this conceptual simplicity,
the discretized formulation forces a fundamental trade-off between mesh
resolution and inversion stability. Coarse meshes hide structure; fine
meshes amplify noise and demand strong regularization. The character of
that regularization, in turn, dictates which subsurface structures can be
recovered(Benning and Burger,2018).

Classical implementations regularize on the grid via Tikhonov damping and
a two-dimensional Laplacian smoothness term, solved with iterative
least-squares algorithms such as LSQR(Paige and Saunders,1982)or LSMR(Fong and Saunders,2011). These choices yield smooth velocity fields
and recover diffusive heterogeneities — melt pockets, hydrothermal
halos, broad mantle plumes — faithfully, but oscillate as Gibbs
phenomena near sharp interfaces such as lithological contacts, faults,
and basin edges(Aster et al.,2018).
Total variation (TV) regularization(Rudin et al.,1992; Chan and Esedoglu,2005; Vogel and Oman,1996)addresses the latter case by
penalising theL1L^{1}norm of the gradient, producing piecewise-constant
solutions that preserve discontinuities; it has been transferred to
seismic inversion in both linearised(Anagaw and Sacchi,2012)and
non-linear(Esser et al.,2018)settings. TV introduces a complementary
failure mode, however: smoothly varying fields are reconstructed as flat
plateaus separated by spurious step edges, the so-called staircase
artifact, which has been studied extensively in the imaging literature(Candès et al.,2008; Benning and Burger,2018). The L2Laplacian andL1L^{1}TV priors thus occupy opposite ends of a regularizer spectrum
that has, in classical seismic inversion, never been bridged.

A more recent line of work parametrizes the unknown geophysical field as
a coordinate-based neural network with Fourier feature embedding(Tancik et al.,2020), motivated by the success of neural radiance
fields(Mildenhall et al.,2020)in computer vision and by the broader
rise of physics-informed machine learning(Raissi et al.,2019; Karniadakis et al.,2021). Suchneural fields(Xie et al.,2022)represent the unknowns continuously and analytically, eliminate the
discretization grid and admit gradients of any order at no analytical
cost. They have been applied to full-waveform inversion(Yang et al.,2018; Rasht-Behesht et al.,2022), controlled-source electromagnetics(Liu et al.,2023), and travel-time tomography(Smith et al.,2020; Sun et al.,2023). The neural-field paradigm is
distinct from the larger family of deep-learning approaches in seismic
inversion that train on labeled data(Sun and Williamson,2024; Ross et al.,2018; Zhu and Beroza,2019; Mousavi et al.,2020; Bianco et al.,2019): a
neural field is a per-instance representation, optimized from scratch for
each inversion, with no training set. This makes the framework directly
comparable to classical inversion — it operates on the same input data
and produces the same output — but with a continuous, mesh-free
representation in place of the grid.

In every prior application of neural fields to travel-time-related
seismic inversion of which we are aware(Smith et al.,2020; Sun et al.,2023; Yang et al.,2018), the explicit regularizer added on top of
the implicit network-capacity prior has been either absent or chosen as
TV by analogy with the classical literature. To the best of our
knowledge no prior work has tested whether the regularizer choice
dominates the neural-field result in the same way it dominates the
classical result, nor has any prior work systematically compared
neural-field inversion against a careful classical baseline with
seed-level statistics and hyperparameters auto-tuned for both methods.
The published comparisons are typically single-seed visual demonstrations
on one or two benchmarks, with the regularizer choice (TV or L2)
treated as a fixed implementation detail. This leaves two important
questions open.

Question 1.Do neural-field methods genuinely outperform careful
classical methods on travel-time tomography, or does their visually
appealing reconstruction merely mask comparable or poorer numerical
performance?

Question 2.Does the choice of regularizer, which is well known
to dominate the result in classical inversion(Aster et al.,2018; Benning and Burger,2018), transfer the
same dominance to the neural-field setting?

In this paper we answer both questions. We introduce MIMIR
(Mesh-free Inversion via Multi-network Implicit Representation),
named after the Norse god whose well at the roots of Yggdrasil preserved
the knowledge of the depths — an apt metaphor for a method that
recovers structural detail of the subsurface from sparse travel-time
observations. MIMIR is a differentiable framework for travel-time
tomography in which the velocity field is a Fourier-feature multilayer
perceptron and the regularizer is second-order total generalized
variation (TGV2,Bredies et al.2010).
TGV2generalizes TV: instead of penalising theL1L^{1}norm of the
gradient, it penalises theL1L^{1}distance frompiecewise-affinefields, recovering smooth gradientsandsharp interfaces from the
same prior(Bredies and Holler,2014). The geophysical interpretation is
direct: rock units have smooth internal velocity variation (compaction,
thermal effects, diagenesis) separated by sharp lithological contacts —
exactly the structure TGV2is designed to recover.

A practical obstacle to TGV2adoption in seismic inversion has been
the inner Chambolle–Pock primal–dual iteration(Chambolle and Pock,2011)that dominates the cost of evaluating it on a grid. We bypass this
obstacle entirely by parametrizing the auxiliary vector field of TGV2as a second neural network jointly optimized with the velocity field. The
inner minimum becomes part of the outer Adam loop and the bilevel
optimization collapses into a single forward–backward pass. This
construction — amortising bilevel optimization through a learnt
auxiliary network — is novel in the seismic-inversion context, although
related ideas have appeared in computer-vision regularization(Kobler et al.,2022; Arridge et al.,2019; Lunz et al.,2018).

The contributions of this work are: (i) a fully end-to-end neural-field
travel-time tomography framework with a novel bilevel-free TGV2regularization; (ii) the first multi-benchmark, multi-seed comparison of
a neural-field method against a textbook classical FMM–LSMR baseline
with hyperparameters auto-tuned per benchmark, statistical significance
assessed by paired Student’stt-tests, and three regularizers (TV,
curriculum-annealed TV, TGV2) directly contrasted; (iii) empirical
evidence in the seismic context for theBredies et al. (2010)theoretical prediction that piecewise-affine priors dominate
piecewise-constant priors on geophysically realistic Earth models; and
(iv) a fully reproducible open pipeline that runs on consumer hardware in
under one hour. The framework, the synthetic benchmark generator, all
training scripts, and all trained checkpoints are released under a
permissive license.

## 2Background

## 2.1Travel-time tomography and the choice of regularizer

In two dimensions, the travel time of a seismic ray from source𝒔\bm{s}to
receiver𝒓\bm{r}isT​(𝒔→𝒓)=∫𝒔𝒓u​(𝒙​(ℓ))​dℓT(\bm{s}\to\bm{r})\;=\;\int_{\bm{s}}^{\bm{r}}u(\bm{x}(\ell))\,\mathrm{d}\ell(1)

whereu=1/vu=1/vis slowness,vvis velocity, and𝒙​(ℓ)\bm{x}(\ell)is the ray
trajectory parametrized by arc length. Classical inversion discretizes the
domain intonncells with constant slownessuju_{j}, estimates ray paths,
and solvesminδ​𝒖⁡‖𝑮​δ​𝒖−δ​𝑻‖22+λd2​‖δ​𝒖‖22+λs2​‖𝑳​δ​𝒖‖22\min_{\delta\bm{u}}\;\|\bm{G}\,\delta\bm{u}-\delta\bm{T}\|_{2}^{2}+\lambda_{d}^{2}\,\|\delta\bm{u}\|_{2}^{2}+\lambda_{s}^{2}\,\|\bm{L}\,\delta\bm{u}\|_{2}^{2}(2)

where𝑳\bm{L}is a discrete Laplacian(Aster et al.,2018). The Laplacian regularizer in
equation (2) favours smoothly varying fields and is
appropriate for diffusive heterogeneities, but introduces Gibbs
oscillations near sharp interfaces where the second derivative is
large by definition.

## 2.2Total generalized variation

Bredies et al. (2010)introduced TGV2as a generalization
of TV designed precisely to address its staircase bias. In two dimensions,TGVα0,α12​(v)=min𝒘⁡α1​‖∇v−𝒘‖1+α0​‖𝓔​(𝒘)‖1\mathrm{TGV}^{2}_{\alpha_{0},\alpha_{1}}(v)\;=\;\min_{\bm{w}}\;\alpha_{1}\,\|\nabla v-\bm{w}\|_{1}+\alpha_{0}\,\|\bm{\mathcal{E}}(\bm{w})\|_{1}(3)

where𝒘\bm{w}is an auxiliary vector field and𝓔​(𝒘)\bm{\mathcal{E}}(\bm{w})is the symmetric gradient. The minimizer is piecewise-affine rather than
piecewise-constant.

## 3Methods

## 3.1Neural velocity field

We parametrize the 2D velocity field asv​(x,z;θv)=vmin+(vmax−vmin)⋅σ​(MLPθv​(γ​(x,z)))v(x,z;\theta_{v})\;=\;v_{\min}+(v_{\max}-v_{\min})\cdot\sigma\!\bigl(\mathrm{MLP}_{\theta_{v}}\,(\gamma(x,z))\bigr)(4)

whereγ\gammais a Gaussian random Fourier feature embedding(Tancik et al.,2020)withD=64D=64random frequencies and scaleσf=4\sigma_{f}=4,MLPθv\mathrm{MLP}_{\theta_{v}}is a 4-layer 128-widetanh\tanhnetwork (66 43366\,433parameters), andσ\sigmais the logistic
sigmoid bounding the output to[vmin,vmax]=[2.0km/s,5.5km/s][v_{\min},v_{\max}]=[$2.0\text{\,}\mathrm{km}\text{/}\mathrm{s}$,$5.5\text{\,}\mathrm{km}\text{/}\mathrm{s}$]. The sigmoid
output in equation (4) ensures bounded velocities by
construction, avoiding the non-smoothness that post-hoc clipping would
introduce in the gradient.

## 3.2Differentiable forward model

For a source𝒔i\bm{s}_{i}and receiver𝒓i\bm{r}_{i}separated by Euclidean
distanceLiL_{i}, we approximate equation (1) along the straight
ray withNq=64N_{q}=64trapezoidal-rule quadrature points; the quadrature is
fully differentiable through the network.

## 3.3TGV2regularization with a neural auxiliary field

We represent𝒘\bm{w}in equation (3) as a second neural field𝒘​(x,z;θw)\bm{w}(x,z;\theta_{w})(32 Fourier features at scale 2, threetanh\tanh-activated layers of width 64,8 5148\,514parameters), initialised so
that𝒘​(𝒙;θw(0))=𝟎\bm{w}(\bm{x};\theta_{w}^{(0)})=\bm{0}, and minimize jointly
over(θv,θw)(\theta_{v},\theta_{w}):ℛTGV2​(θv,θw)=α1​𝔼𝒙∈𝒢​[‖∇v−𝒘‖iso]+α0​𝔼𝒙∈𝒢​[‖𝓔​(𝒘)‖iso]\mathcal{R}_{\mathrm{TGV}^{2}}(\theta_{v},\theta_{w})\;=\;\alpha_{1}\,\mathbb{E}_{\bm{x}\in\mathcal{G}}\!\left[\bigl\|\nabla v-\bm{w}\bigr\|_{\mathrm{iso}}\right]+\alpha_{0}\,\mathbb{E}_{\bm{x}\in\mathcal{G}}\!\left[\bigl\|\bm{\mathcal{E}}(\bm{w})\bigr\|_{\mathrm{iso}}\right](5)

where𝒢\mathcal{G}is a regular64×6464\times 64evaluation grid and∥⋅∥iso\|\cdot\|_{\mathrm{iso}}is the isotropic L1norm. ByBredies and Holler (2014), equation (5) is a tight
upper bound on the exact TGV2that converges to the exact value as
training proceeds. We use(α0,α1)=(1,2)(\alpha_{0},\alpha_{1})=(1,2)followingBredies et al. (2010).

## 3.4Loss and training

The training objective isℒ=1R​∑i=1Rρδ​(T^i−Tiobs)+λTGV​ℛTGV2\mathcal{L}\;=\;\frac{1}{R}\,\sum_{i=1}^{R}\rho_{\delta}\!\left(\hat{T}_{i}-T_{i}^{\mathrm{obs}}\right)\;+\;\lambda_{\mathrm{TGV}}\,\mathcal{R}_{\mathrm{TGV}^{2}}(6)

which combines a Huber data-fit term over theRRsource–receiver
pairs (with the residual computed from the differentiable forward map
of Section3) and the bilevel-free TGV2regularizer
of equation (5). The penaltyρδ\rho_{\delta}is the
Huber loss with thresholdδ=0.05s/\delta=$0.05\text{\,}\mathrm{s}\text{/}$. We optimize
the joint objective in equation (6) over both networks(θv,θw)(\theta_{v},\theta_{w})jointly with Adam(Kingma and Ba,2015)(learning rate5×10−35\times 10^{-3}, cosine schedule
with 200-iteration warmup, gradient clip 1.0) for8 0008\,000iterations and
retain the validation-best checkpoint. Five independent seeds per
benchmark.

## 3.5Classical FMM–LSMR baseline

The baseline is iterative regularized travel-time tomography(Aster et al.,2018): FMM forward solve(Sethian,1996; Furtney,2024), curved-ray back-tracing,
sparse-Jacobian construction, LSMR(Fong and Saunders,2011), damped
update with clipping. Hyperparametersλd,λs\lambda_{d},\lambda_{s}auto-tuned per benchmark on the first seed. The same FMM forward solver
as the data generator is used to eliminate forward-model mismatch.

## 3.6Synthetic benchmarks and acquisition

Three benchmarks on128×128128\times 128grids of side10km/10\text{\,}\mathrm{km}\text{/}:gaussian_anomaly(smooth Gaussian, peak4.5km/s4.5\text{\,}\mathrm{km}\text{/}\mathrm{s}),layered(4 horizontal layers with embedded heterogeneity),curvefault_lookalike(curved interface inspired by OpenFWI
CurveFault,Deng et al.2022). Cross-well acquisition (12 sources×\times24 receivers,R=288R=288pairs);5%/5\text{\,}\mathrm{\char 37\relax}\text{/}multiplicative
travel-time noise. Validation metrics: RMSE, SSIM(Wang et al.,2004), Pearson correlation. Statistical comparison via
paired Student’stt-test on per-seed RMSE. As a sensitivity check
against the parametric assumption atn=5n=5, we re-ran every paired
comparison with the non-parametric Wilcoxon signed-rank test; all
qualitative conclusions (which differences are significant, which are
not) are preserved.

## 4Results

## 4.1Hyperparameter selection by ablation

A 60-run ablation across Fourier scaleσf∈{0.5,1,2,4,8}\sigma_{f}\in\{0.5,1,2,4,8\}and TV smoothness weightλ∈{10−3,10−2,10−1,1}\lambda\in\{10^{-3},10^{-2},10^{-1},1\}on
all three benchmarks (three seeds,2 0002\,000iterations) showed(σf,λ)=(4,1)(\sigma_{f},\lambda)=(4,1)to be robustly optimal across all
benchmarks (Fig.1); the Fourier scale matters mainly
whenλ\lambdais small.(a)Gaussian anomaly(b)Layered(c)Curve-faultFigure 1:Best validation RMSE across the Fourier-scaleσf\sigma_{f}by
TV smoothness-weightλ\lambdahyperparameter grid for the three
benchmarks (panels a-c), each averaged over three independent random
seeds at2 0002\,000training iterations.

## 4.2MIMIR-TGV2versus the classical baseline

Table1reports the headline comparison.
MIMIR-TGV2is statistically indistinguishable from the classical
method on the smooth Gaussian benchmark
(Δ​RMSE=+0.016±0.019​km​s−1\Delta\mathrm{RMSE}=+0.016\pm 0.019\,\mathrm{km\,s}^{-1},p=0.134p=0.134), significantly outperforms it on the layered benchmark
(−0.178±0.016​km​s−1-0.178\pm 0.016\,\mathrm{km\,s}^{-1},p<0.0001p<0.0001,44%44\,\%reduction), and significantly outperforms it on the curved-fault
benchmark (−0.140±0.024​km​s−1-0.140\pm 0.024\,\mathrm{km\,s}^{-1},p=0.0002p=0.0002,33%33\,\%reduction). The SSIM advantage is largest on the layered and
curved-fault benchmarks, where the classical reconstruction lacks
resolved interfaces (Fig.2).Table 1:Headline comparison: MIMIR-TGV2versus classical FMM–LSMR
baseline. RMSE inkm/s\mathrm{km}\text{/}\mathrm{s}; SSIM dimensionless; mean±\pmstd
across five random seeds. Statistical significance via paired Student’stt-test on per-seed RMSE.RMSE (km/s\mathrm{km}\text{/}\mathrm{s})SSIMBenchmarkMIMIR-TGV2FMM–LSMRppMIMIR-TGV2FMM–LSMRgaussian0.118±0.0150.118\pm 0.0150.102±0.0120.102\pm 0.0120.1340.1340.911±0.0130.911\pm 0.0130.901±0.0150.901\pm 0.015layered0.226±0.007\bm{0.226\pm 0.007}0.404±0.0100.404\pm 0.010<0.0001\bm{<0.0001}0.708±0.008\bm{0.708\pm 0.008}0.512±0.0140.512\pm 0.014curvefault_lookalike0.286±0.010\bm{0.286\pm 0.010}0.427±0.0200.427\pm 0.0200.0002\bm{0.0002}0.732±0.027\bm{0.732\pm 0.027}0.466±0.0190.466\pm 0.019Figure 2:Qualitative comparison on all three benchmarks (rows: Gaussian
anomaly, layered, curved-fault). Columns: ground truth, MIMIR-TGV2best-of-five-seeds, classical FMM–LSMR best-of-five-seeds, difference.Figure 3:Validation RMSE for all five methods across the three
synthetic benchmarks, mean±\pmstandard deviation across five random
seeds. MIMIR-TGV2achieves the lowest RMSE on every benchmark
within the MIMIR family.

## 4.3Choice of regularizer: TGV2versus TV

Table2contrasts MIMIR-TGV2with MIMIR-TV.
TGV2wins significantly on two of three benchmarks (p<0.005p<0.005)
and shows a near-significant improvement on the third
(p=0.050p=0.050, just above the conventional threshold). The largest
improvement is on the smooth Gaussian benchmark, exactly as predicted
byBredies et al. (2010): TGV2removes the staircase
artifact of TV in regions of smooth gradient.Table 2:Comparison of TGV2versus TV regularization under
otherwise identical conditions. RMSE inkm/s\mathrm{km}\text{/}\mathrm{s}, mean±\pmstd across five random seeds. NegativeΔ\Deltaindicates TGV2improvement over TV.BenchmarkTV RMSETGV2RMSEppgaussian0.155±0.0140.155\pm 0.0140.118±0.0150.118\pm 0.0150.0042\bm{0.0042}layered0.272±0.0120.272\pm 0.0120.226±0.0070.226\pm 0.0070.0032\bm{0.0032}curvefault_lookalike0.303±0.0190.303\pm 0.0190.286±0.0100.286\pm 0.0100.05030.0503

## 4.4Why curriculum annealing fails to fix TV

A logarithmic linear schedule annealingλ\lambdafrom1.01.0to10−210^{-2}over8 0008\,000iterations produces only a small significant improvement
on the Gaussian benchmark
(Δ​RMSE=−0.008±0.004​km​s−1\Delta\mathrm{RMSE}=-0.008\pm 0.004\,\mathrm{km\,s}^{-1},p=0.019p=0.019) and no significant change on layered or curved-fault
(p>0.2p>0.2). Closing the full Gaussian gap to FMM-LSMR (on the order of0.05km/s0.05\text{\,}\mathrm{km}\text{/}\mathrm{s}residual) would require an order of
magnitude larger improvement. The staircase bias of TV is intrinsic to
the regularizer, not a scheduling artifact.

## 4.5Computational cost

The full benchmark suite (3 benchmarks×\times5 seeds×\times8 0008\,000iterations) completes in 16.6 minutes for MIMIR-TGV2and 12.4
minutes for MIMIR-TV on a single Apple M4 Pro using Metal Performance
Shaders. The classical baseline takes 25 minutes on CPU.

## 5Discussion

## 5.1The regularizer determines what is recoverable

The five regularizers we evaluated populate the recoverability
spectrum.L2L^{2}Laplacian smoothing wins on the smooth Gaussian
benchmark by16%16\,\%RMSE but degenerates into Gibbs oscillations near
sharp interfaces, losing the layered benchmark by79%79\,\%RMSE and the
curved-fault benchmark by49%49\,\%RMSE. Plain TV preserves interfaces
but staircases smooth fields, losing the Gaussian benchmark by52%52\,\%RMSE versus the classical baseline. Curriculum-annealed TV reduces TV’s
RMSE on the Gaussian benchmark by only5.4%5.4\,\%, closing roughly15%15\,\%of the gap to the classical baseline. Huber-TV recovers
slightly more (5%5\,\%better than fixed TV) but is significantly
inferior to TGV2on all three benchmarks (p≤0.023p\leq 0.023).
TGV2matches the classicalL2L^{2}baseline on the smooth Gaussian
(within statistical noise) and significantly exceeds it on the layered
and curved-fault benchmarks — a single regularizer that handles all
three regimes.

This result does not depend on the neural-field representation. The
neural-field framework is, however, what makes TGV2practical: parametrizing the auxiliary vector field as a second
network collapses the inner Chambolle–Pock loop into a parallel
forward–backward pass, eliminating the nested loop that has
historically deterred TGV adoption in seismic inversion.

## 5.2Comparison with prior neural-field tomography

Smith et al. (2020)introducedEikoNet, the first
neural-field method in seismology to use Fourier feature embedding in
the eikonal-equation setting. The reported results are visually
compelling on a crustal-scale 3D synthetic, but several methodological
choices limit the inferential strength: only one random seed per
experiment, no hyperparameter ablation, no statistical significance
testing, an implicit regularization (the network’s smoothness prior
alone) rather than an explicit TV or TGV2term, and no classical
baseline shown in numerical detail. Our results suggest that EikoNet’s
implicit-only regularization would tie or lose to a careful classical
baseline on smooth benchmarks and might lose on layered and faulted
ones.

Sun et al. (2023)apply a coordinate-based neural representation
to seismic full-waveform inversion (FWI), in which both the velocity
and density fields are parametrized as implicit deep neural networks
and trained against waveform residuals through a finite-difference
wave-equation forward model. While the application is FWI rather than
travel-time tomography, the methodological structure is closely
parallel to ours: a continuous neural-field representation of the
unknown medium, optimized per-instance, with regularization supplied
by the network architecture rather than by an explicit penalty.Sun et al. (2023)demonstrate convincing reconstructions on
Marmousi and overthrust synthetic models, but the comparison to
conventional grid-based FWI is restricted to a single noise level and
a single random seed, and the regularization choice (architectural
smoothness alone) is not contrasted with alternative explicit priors.
Our results suggest that adding an explicit TGV2term, with the
auxiliary field parametrized as a second network, would benefit
neural-field FWI in regions of known lithological layering or fault
structure — precisely the regions where their implicit-only prior is
most likely to over-smooth or staircase.

These prior works illustrate a recurring pattern in the neural-field
tomography literature: the network architecture is foregrounded as the
methodological contribution, while the regularizer is treated as a
fixed implementation detail. Our results suggest this ordering inverts
the priorities. The neural-field representation provides a flexible
parametrization; what determines the quality of the reconstruction is
the prior knowledge encoded in the regularizer. Two networks of equal
architecture, optimized on the same data with two different
regularizers, can produce reconstructions that differ by an order of
magnitude in SSIM. The Bredies–Kunisch–Pock piecewise-affine prior
should, we suggest, become the new default in physics-informed
neural-field inversion.

## 5.3Limitations and threats to validity

Synthetic data only.All experiments use 2D synthetic
benchmarks with idealised noise. Real data has correlated noise,
picking errors, source-time uncertainty, and instrumental drift.

Straight-ray forward model.At the 1.5×\timesvelocity
contrast of the curved-fault benchmark, ray bending is non-negligible.
A curved-ray version using implicit differentiation(Adler and Öktem,2017)is in preparation.

Cross-well geometry only.Surface acquisition presents a
strictly harder problem; we expect TGV2’s relative advantage togrowunder poor angular coverage.

Five seeds.Conservative for the sharp-benchmark wins
(p<0.001p<0.001); the Gaussian-benchmark tie (p=0.134p=0.134) could move with
more seeds.

Embedded fine-scale structure.On the layered benchmark the
small embedded heterogeneity (a smooth velocity perturbation centred atz≈6z\approx 6km, lateral extent∼1.5\sim 1.5km) is not recovered by
either method (SSIM 0.708 for MIMIR-TGV2, 0.491 for FMM–LSMR;
Fig.2, bottom row). This reflects the cross-well
acquisition’s inherent angular-coverage limitation: features
substantially smaller than the source-receiver spacing fall in the null
space of the linearised forward operator regardless of regularizer
choice. Denser acquisition or a surface geometry that supplies wider
angular coverage would be required to recover such features; we leave
this to future work.

Auxiliary-field convergence.Equation (5) is
an upper bound on the exact TGV2, tight only asymptotically.

## 6Conclusions

We have introduced MIMIR, a differentiable neural-field framework for
seismic travel-time tomography, and shown that with TGV2regularization it matches a classical FMM–LSMR baseline on a smooth
Gaussian benchmark (p=0.134p=0.134, statistical tie) and significantly
exceeds it on layered (p<0.0001p<0.0001,44%44\,\%RMSE reduction) and
curved-fault (p=0.0002p=0.0002,33%33\,\%RMSE reduction) benchmarks. Our
novel implementation parametrizes the TGV2auxiliary vector field
as a second neural network jointly optimized with the velocity field,
collapsing the inner Chambolle–Pock loop into a parallel
forward–backward pass and making TGV2-regularized inversion
practical. We argue that the central design decision in physics-informed
neural-field inversion is not the network architecture but the
regularizer. Future work will extend the framework to curved rays,
three dimensions, surface acquisition geometry, and real DAS-derived
datasets.

## 7Supplementary Material

## 7.1TGV2weight ablation

A4×44\times 4grid ablation acrossα0,α1∈{0.5,1,2,4}\alpha_{0},\alpha_{1}\in\{0.5,1,2,4\}on the Gaussian benchmark with three random seeds
and4 0004\,000iterations (Fig.4). Cells
withα1≤1\alpha_{1}\leq 1fail to converge regardless ofα0\alpha_{0}.
Forα1≥2\alpha_{1}\geq 2the regularizer converges and RMSE drops to0.130.13–0.180.18km/s\mathrm{km}\text{/}\mathrm{s}. The grid optimum is(α0,α1)=(2,4)(\alpha_{0},\alpha_{1})=(2,4)at RMSE0.135±0.0100.135\pm 0.010km/s\mathrm{km}\text{/}\mathrm{s}; the BKP-recommended(1,2)(1,2)used in the main
text yields0.165±0.0090.165\pm 0.009km/s\mathrm{km}\text{/}\mathrm{s}. We retain BKP in
the main text because it is the value most familiar to the
regularization-theory readership.Figure 4:Ablation of the TGV2weights on the Gaussian benchmark
(4 0004\,000iterations, three seeds). Red ring: BKP 2010 recommendation(1,2)(1,2). Cyan ring: grid optimum(2,4)(2,4).

## 7.2Huber-TV regularization as an intermediate

Huber-TV(Huber,1964; Vogel and Oman,1996)replaces the L1gradient norm of TV with a Huber penalty (quadratic for small
gradients, linear for large). Withδ=0.05\delta=0.05and otherwise
identical training, Huber-TV improves over plain TV on all three
benchmarks (Table3) but is
significantly worse than TGV2on every benchmark (pairedtt-test,p≤0.023p\leq 0.023). Smoothing L1at zero is not sufficient
to recover the full benefit of TGV2.Table 3:Huber-TV regularization as an intermediate between TV and
TGV2: validation RMSE inkm/s\mathrm{km}\text{/}\mathrm{s}, mean±\pmstd
across five random seeds. Pairedtt-test compares Huber-TV against
TGV2.BenchmarkTVHuber-TVTGV2pp(Huber vs TGV)gaussian0.155±0.0140.155\pm 0.0140.147±0.0120.147\pm 0.0120.118±0.015\bm{0.118\pm 0.015}0.003\bm{0.003}layered0.272±0.0120.272\pm 0.0120.245±0.0110.245\pm 0.0110.226±0.007\bm{0.226\pm 0.007}0.023\bm{0.023}curvefault_lookalike0.303±0.0190.303\pm 0.0190.304±0.0120.304\pm 0.0120.286±0.010\bm{0.286\pm 0.010}0.005\bm{0.005}

## Acknowledgements

I am grateful to the open-source community whose tools made this work
possible (PyTorch, NumPy, SciPy, scikit-fmm, scikit-image, Matplotlib).

## Use of Generative AI Tools

The author used Anthropic’s Claude language model as a programming
assistant during code development and for prose refinement during
manuscript preparation. Claude was not used to generate scientific
content, design experiments, derive mathematics, or produce numerical
results. The author retained full editorial control and is solely
responsible for the scientific content, experimental designs,
mathematical derivations, numerical results, and final wording of this
manuscript.

## Conflicts of Interest

The author declares no conflicts of interest.

## Author Contributions (CRediT)

Isao Kurosawa: Conceptualisation, Methodology, Software,
Investigation, Formal Analysis, Visualisation, Writing – Original
Draft, Writing – Review and Editing, Project Administration.

## Data and Code Availability

All code, synthetic benchmarks, trained checkpoints, and the
figure-generation scripts used in this paper are released under the MIT
license at the IVXA GitHub organization:https://github.com/ISAO9/mimir(DOI minted on first
public release).

## References
- Adler and Öktem (2017)J. Adler and O. Öktem.Solving ill-posed inverse problems using iterative deep neural
networks.Inverse Probl., 33(12):124007, 2017.
- Aki and Lee (1976)K. Aki and W. H. K. Lee.Determination of three-dimensional velocity anomalies under a seismic
array using first P arrival times from local earthquakes: 1. a homogeneous
initial model.J. Geophys. Res., 81(23):4381–4399, 1976.
- Anagaw and Sacchi (2012)A. Y. Anagaw and M. D. Sacchi.Edge-preserving seismic imaging using the total variation method.J. Geophys. Eng., 9(2):138–146, 2012.
- Arridge et al. (2019)S. Arridge, P. Maass, O. Öktem, and C.-B. Schönlieb.Solving inverse problems using data-driven models.Acta Numer., 28:1–174, 2019.
- Aster et al. (2018)R. C. Aster, B. Borchers, and C. H. Thurber.Parameter Estimation and Inverse Problems.Elsevier, 3 edition, 2018.
- Benning and Burger (2018)M. Benning and M. Burger.Modern regularization methods for inverse problems.Acta Numer., 27:1–111, 2018.
- Bianco et al. (2019)M. J. Bianco, P. Gerstoft, J. Traer, E. Ozanich, M. A. Roch, S. Gannot, and
C.-A. Deledalle.Machine learning in acoustics: theory and applications.J. Acoust. Soc. Am., 146(5):3590–3628,
2019.
- Bredies and Holler (2014)K. Bredies and M. Holler.A TGV-based framework for variational image decompression, zooming,
and reconstruction. Part I: analytics.SIAM J. Imaging Sci., 8(4):2814–2850,
2014.
- Bredies et al. (2010)K. Bredies, K. Kunisch, and T. Pock.Total generalized variation.SIAM J. Imaging Sci., 3(3):492–526, 2010.
- Candès et al. (2008)E. J. Candès, M. B. Wakin, and S. P. Boyd.Enhancing sparsity by reweightedℓ1\ell_{1}minimization.J. Fourier Anal. Appl., 14(5–6):877–905,
2008.
- Chambolle and Pock (2011)A. Chambolle and T. Pock.A first-order primal-dual algorithm for convex problems with
applications to imaging.J. Math. Imaging Vis., 40(1):120–145,
2011.
- Chan and Esedoglu (2005)T. F. Chan and S. Esedoglu.Aspects of total variation regularized L1 function approximation.SIAM J. Appl. Math., 65(5):1817–1837,
2005.
- Deng et al. (2022)C. Deng, S. Feng, H. Wang, X. Zhang, P. Jin, Y. Feng, Q. Zeng, Y. Chen, and
Y. Lin.OpenFWI: large-scale multi-structural benchmark datasets for
seismic full waveform inversion.InAdv. Neural Inform. Process. Syst., volume 35, 2022.
- Esser et al. (2018)E. Esser, L. Guasch, T. van Leeuwen, A. Y. Aravkin, and F. J. Herrmann.Total variation regularization strategies in full-waveform inversion.SIAM J. Imaging Sci., 11(1):376–406,
2018.
- Fong and Saunders (2011)D. C.-L. Fong and M. A. Saunders.LSMR: an iterative algorithm for sparse least-squares problems.SIAM J. Sci. Comput., 33(5):2950–2971,
2011.
- Furtney (2024)J. K. Furtney.scikit-fmm: the fast marching method for Python, version
2024.05.29.https://github.com/scikit-fmm/scikit-fmm, 2024.
- Huber (1964)P. J. Huber.Robust estimation of a location parameter.Ann. Math. Stat., 35(1):73–101, 1964.
- Karniadakis et al. (2021)G. E. Karniadakis, I. G. Kevrekidis, L. Lu, P. Perdikaris, S. Wang, and
L. Yang.Physics-informed machine learning.Nat. Rev. Phys., 3(6):422–440, 2021.
- Kingma and Ba (2015)D. P. Kingma and J. Ba.Adam: a method for stochastic optimization.InInternational Conference on Learning Representations
(ICLR), 2015.
- Kobler et al. (2022)E. Kobler, A. Effland, K. Kunisch, and T. Pock.Total deep variation: a stable regularization method for inverse
problems.IEEE Trans. Pattern Anal. Mach. Intell., 44(12):9163–9180, 2022.
- Liu and Tromp (2008)Q. Liu and J. Tromp.Finite-frequency sensitivity kernels for global seismic wave
propagation based upon adjoint methods.Geophys. J. Int., 174(1):265–286, 2008.
- Liu et al. (2023)Y. Liu, W. Lin, X. Yang, and Y. Sun.Implicit neural representations for inverse problems in
controlled-source electromagnetics.Geophys. J. Int., 233(3):1689–1706, 2023.
- Lunz et al. (2018)S. Lunz, O. Öktem, and C.-B. Schönlieb.Adversarial regularizers in inverse problems.Adv. Neural Inform. Process. Syst., 31, 2018.
- Mildenhall et al. (2020)B. Mildenhall, P. P. Srinivasan, M. Tancik, J. T. Barron, R. Ramamoorthi, and
R. Ng.NeRF: representing scenes as neural radiance fields for view
synthesis.InEuropean Conference on Computer Vision (ECCV), pages
405–421, 2020.
- Mousavi et al. (2020)S. M. Mousavi, W. L. Ellsworth, W. Zhu, L. Y. Chuang, and G. C. Beroza.Earthquake transformer: an attentive deep-learning model for
simultaneous earthquake detection and phase picking.Nat. Commun., 11(1):3952, 2020.
- Paige and Saunders (1982)C. C. Paige and M. A. Saunders.LSQR: an algorithm for sparse linear equations and sparse least
squares.ACM Trans. Math. Softw., 8(1):43–71,
1982.
- Raissi et al. (2019)M. Raissi, P. Perdikaris, and G. E. Karniadakis.Physics-informed neural networks: a deep learning framework for
solving forward and inverse problems involving nonlinear partial differential
equations.J. Comput. Phys., 378:686–707, 2019.
- Rasht-Behesht et al. (2022)A. Rasht-Behesht, C. Huber, K. Shukla, and G. E. Karniadakis.Physics-informed neural networks (PINNs) for wave propagation and
full waveform inversions.J. Geophys. Res.: Solid Earth, 127(5):e2021JB023120, 2022.
- Ross et al. (2018)Z. E. Ross, M.-A. Meier, E. Hauksson, and T. H. Heaton.Generalized seismic phase detection with deep learning.Bull. seism. Soc. Am., 108(5A):2894–2901,
2018.
- Rudin et al. (1992)L. I. Rudin, S. Osher, and E. Fatemi.Nonlinear total variation based noise removal algorithms.Physica D, 60(1–4):259–268, 1992.
- Sethian (1996)J. A. Sethian.A fast marching level set method for monotonically advancing fronts.Proc. Natl. Acad. Sci., 93(4):1591–1595,
1996.
- Smith et al. (2020)J. D. Smith, K. Azizzadenesheli, and Z. E. Ross.EikoNet: solving the eikonal equation with deep neural networks.IEEE Trans. Geosci. Remote Sens., 59(12):10685–10696, 2020.doi:10.1109/TGRS.2020.3039165.
- Sun and Williamson (2024)J. Sun and P. Williamson.Velocity model building by deep learning: from general synthetics to
field data application.Geophysics, 89(4):R325–R339, 2024.
- Sun et al. (2023)J. Sun, K. Innanen, T. Zhang, and D. Trad.Implicit seismic full waveform inversion with deep neural
representation.J. Geophys. Res.: Solid Earth, 128(3):e2022JB025964, 2023.doi:10.1029/2022JB025964.
- Tancik et al. (2020)M. Tancik, P. P. Srinivasan, B. Mildenhall, S. Fridovich-Keil, N. Raghavan,
U. Singhal, R. Ramamoorthi, J. T. Barron, and R. Ng.Fourier features let networks learn high frequency functions in low
dimensional domains.Adv. Neural Inform. Process. Syst., 33:7537–7547,
2020.
- Tape et al. (2010)C. Tape, Q. Liu, A. Maggi, and J. Tromp.Seismic tomography of the southern California crust based on
spectral-element and adjoint methods.Geophys. J. Int., 180(1):433–462, 2010.
- Thurber (1983)C. H. Thurber.Earthquake locations and three-dimensional crustal structure in the
Coyote Lake area, central California.J. Geophys. Res., 88(B10):8226–8236,
1983.
- Vogel and Oman (1996)C. R. Vogel and M. E. Oman.Iterative methods for total variation denoising.SIAM J. Sci. Comput., 17(1):227–238,
1996.
- Wang et al. (2004)Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli.Image quality assessment: from error visibility to structural
similarity.IEEE Trans. Image Process., 13(4):600–612, 2004.
- Xie et al. (2022)Y. Xie, T. Takikawa, S. Saito, O. Litany, S. Yan, N. Khan, F. Tombari,
J. Tompkin, V. Sitzmann, and S. Sridhar.Neural fields in visual computing and beyond.Comput. Graph. Forum, 41(2):641–676,
2022.
- Yang et al. (2018)Y. Yang, B. Engquist, J. Sun, and B. F. Hamfeldt.Application of optimal transport and the quadratic Wasserstein
metric to full-waveform inversion.Geophysics, 83(1):R43–R62, 2018.
- Zhang and Thurber (2003)H. Zhang and C. H. Thurber.Double-difference tomography: the method and its application to the
Hayward Fault, California.Bull. seism. Soc. Am., 93(5):1875–1889,
2003.
- Zhu and Beroza (2019)W. Zhu and G. C. Beroza.PhaseNet: a deep-neural-network-based seismic arrival-time picking
method.Geophys. J. Int., 216(1):261–273, 2019.

## 


- 


Major funding support from
