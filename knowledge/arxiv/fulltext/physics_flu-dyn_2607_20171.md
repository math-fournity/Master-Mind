# Hard Guarantees at a Measured Price: Entropy-Stable Learned Finite Volumes for Compressible Flow

**arXiv ID**: 2607.20171v2
**Authors**: Denis Gueyffier
**Published**: 2026-07-22
**Categories**: physics.flu-dyn, cs.LG, math.NA
**Comments**: 16 pages, 7 figures, 3 tables. v2: re-measures the unconstrained wall value against a regenerated certified reference; adds the interaction map of the inference-time correction, the gate width sweep on a second geometry, the same gate applied to the unconstrained arm, a scope statement for the admissibility guarantee, and a verified end-to-end reconstruction of the training pipeline
**HTML URL**: https://arxiv.org/html/2607.20171v2

## Abstract

Learned solvers for compressible flow are usually compared to classical methods at equal mesh resolution rather than at equal computational cost, and they typically offer no guarantee that their solutions remain physically admissible. We present a learned finite volume scheme for the two-dimensional Euler equations on unstructured meshes, admissible by construction and with an entropy-stable interior flux. We evaluate it under protocols fixed before any computation: frozen thresholds, falsification clauses, negative controls, a factor decomposition of the learned components, and an iso-cost comparison against the refined classical baseline. The decomposition produced the central result: the guarantee machinery alone, with both learned heads switched off (the unlearned skeleton), is the strongest scheme at equal mesh on every periodic case. At equal wall-clock cost the picture inverts into a map. Learning pays robustly only on the wall case whose boundary-condition type it never saw (10.8%). Its periodic gains flip sign with the evaluation draw (+10% on one held-out case, -12% on the hardest). The skeleton is the only method whose iso-cost gain never changes sign, at a measured overhead of 1.74x per step. The guaranteed variant completes 36 of 36 rollouts, Mach extrapolation and unseen wall included, with zero negativity events. We fix the guaranteed scheme's one remaining out-of-distribution weakness, Mach extrapolation, at inference time: with scale-invariant network inputs, a specific-entropy floor, and no retraining, the corrected arm overtakes the unconstrained arm on one Mach case, cuts its deficit on the other by a third, passes the skeleton on the unseen wall, and keeps the guarantee. A spatial gate closes the loop: activating the heads only near the walls beats both the skeleton and the corrected arm, and transfers unchanged to a second wall geometry.

## Full Text

Hard Guarantees at a Measured Price: Entropy-Stable Learned Finite Volumes for Compressible Flow

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.20171v2 [physics.flu-dyn] 27 Jul 2026

## Hard Guarantees at a Measured Price:
Entropy-Stable Learned Finite Volumes for Compressible FlowDenis Gueyffier
Direction Scientifique Générale, ONERA
Institut Polytechnique de Paris, Palaiseau, France

## Abstract

Learned solvers for compressible flow are usually compared to classical methods at
equal mesh resolution rather than at equal computational cost, and they typically
offer no guarantee that their solutions remain physically admissible. We present a learned finite volume scheme for the two-dimensional Euler equations on unstructured
meshes, admissible by construction and with an entropy-stable interior flux. We evaluate it under protocols fixed before any computation: frozen thresholds,
falsification clauses, negative controls, a factor decomposition of the learned
components, and an iso-cost comparison against the refined classical baseline. The
decomposition produced the central result: the guarantee machinery alone, with both
learned heads switched off (the unlearned skeleton), is the strongest scheme at
equal mesh on every periodic case. Its relaxed-envelope reconstruction beats the Venkatakrishnan-limited
baseline by 32 to 39% at equal flux and equal step. At equal wall-clock cost the
picture inverts into a map. Learning pays robustly only on the wall case whose
boundary-condition type it never saw (10.8%). Its periodic gains flip sign with
the evaluation draw (+10+10% on one held-out case,−12-12% on the hardest). The skeleton is the only method whose iso-cost gain never changes sign, at a
measured overhead of1.74×1.74\timesper step. The guaranteed variant completes
36 of 36 rollouts, Mach extrapolation and unseen wall included, with zero
negativity events. Earlier hard generations crashed at every seed while remaining
admissible cell by cell: a local entropy-pumping mechanism, removed by face-wise
entropy-stable dissipation. Ablations specified in advance rule out unrolled fine-tuning and a reduced
time step as fixes. We fix the guaranteed scheme’s one remaining
out-of-distribution weakness, Mach extrapolation, at inference time: with
scale-invariant network inputs, a specific-entropy floor, and no retraining, the
corrected arm overtakes the unconstrained arm on one Mach case, cuts its deficit on the other by a third, passes the skeleton on the unseen
wall, and keeps the guarantee. The correction is enabled by the guarantees:
the same inputs, applied to the unconstrained arm, degrade it by 22%. A
spatial gate then closes the loop: activating the learned heads only within
a few cell layers of the walls beats both the skeleton and the full corrected
arm. The gate transfers unchanged to a second wall geometry.

## 1Introduction

Learned discretizations promise coarse-mesh solvers with fine-mesh accuracy. For
compressible flow, two elements are usually missing from this picture. The first is
evaluation at equal computational cost. In the lineage this work extends, accuracy
gains are measured against the classical scheme at equal mesh, with a refined
classical solution as the reference: 20 to 50% forde Romémontet al.(2026), 20
to 60% forde Romémontet al.(2025). Computational cost, where examined, is a
reported trend, not part of the verdict. The practically relevant comparison is against a classical scheme that
is simply given a finer mesh(McGreivy and Hakim,2024). The second is a guarantee. A learned scheme that can produce negative densities, or crash on an unseen
boundary condition, is not a solver an engineer can deploy, whatever its
average-case accuracy. Soft penalties on
entropy or total variation(de Romémontet al.,2025)discourage but do not prevent
such failures, and out of distribution they reliably fail to prevent them.

This paper addresses both at once on the hardest common ground we know: the
two-dimensional compressible Euler equations on unstructured triangular meshes. We
build a learned gradient-reconstruction scheme whose admissibility is guaranteed by
construction: an interval envelope around the Barth–Jespersen limiter(Barth and Jespersen,1989), Zhang–Shu(Zhang and Shu,2010)positivity scaling, and an adaptive positivity time step. Its interior flux is
entropy stable in the sense of Tadmor(Tadmor,1987), with the inequality
proved at first order
and enforced as a permanent executable contract beyond it. Both the guaranteed scheme and its unconstrained sibling are evaluated under
protocols fixed before any computation: frozen thresholds, falsification clauses, negative
controls, and an iso-cost comparison against the refined classical baseline with
references computed on meshes refined twice.

Our contributions are four. (1) A factor decomposition of the learned components reveals that the guarantee
machinery alone, with both heads switched off, is the strongest scheme at equal
mesh on every periodic case, in and out of distribution. The driver is the
reconstruction itself: its relaxed envelope with positivity scaling beats the
Venkatakrishnan-limited baseline by 32 to 39% at equal flux and equal time step.
Every learned head degrades this skeleton at equal mesh: the constant-like limiter
position by 10 to 33%, the stencil reweighting by up to a factor 4.6. Run
uncompensated, the reweighting crashes one in-distribution rollout.
(2) The guaranteed scheme completes every rollout of two full campaigns, 36 of 36
including Mach extrapolation and the unseen wall, with zero negativity events. The
earlier hard generations crashed on the wall at every seed despite maintaining
admissibility to the last step; we exhibit the local mechanism and show that
face-wise entropy-stable dissipation closes it. Across four frozen generations
the in-distribution price of the guarantee falls monotonically, reaching parity
(0.999) on one of three cases.
(3) An iso-cost audit under a clean protocol (identical fixed-step integrators,
compilation excluded from every timing) maps where learning actually pays. It pays
robustly on the unseen-boundary wall case (10.8%), with a draw-dependent sign on
periodic cases:+10.3+10.3% on one held-out draw,−12-12% on the hardest. The
unlearned skeleton is the only method that never loses to the cost-matched
classical baseline, at a1.74×1.74\timesper-step overhead. Re-measuring our own
earlier audit under this protocol quantifies a 4-point timing bias in it.
(4) A failure-mode analysis and two ablations that ground the design. A scheme can
be admissible at every cell, with nonincreasing total entropy, and still blow up;
that is the gap the entropy-stable core closes. Neither unrolled fine-tuning nor a
reduced positivity time step repairs the robustness gap, which rules out the
default fixes before any architecture change. The same discipline then repairs the guaranteed scheme’s Mach weakness at
inference time, with no retraining (Section5.6). A boundary gate that
activates the heads only near walls then beats both the skeleton and the
corrected arm out of distribution, across two wall geometries
(Section5.7).

## 2Related work

## Learned discretizations for fluids.

The founding line runs from
data-driven discretizations of PDEs(Bar-Sinaiet al.,2019)through learned advection
schemes(Zhuanget al.,2021)to learning-accelerated CFD with
solver-in-the-loop training(Kochkovet al.,2021). These works established the coarse-mesh promise and unrolled training on
structured grids, without hard admissibility or entropy guarantees;Kochkovet al.(2021)also
popularized cost-aware reporting, which our audit systematizes with thresholds
and controls fixed in advance. Our direct lineage learns finite volume components:
a flux limiter discretization on structured grids(de Romémontet al.,2026)and a
gradient-recovery operator on unstructured triangulations(de Romémontet al.,2025),
both evaluated at equal mesh, the latter constrained by soft entropy and
total-variation penalties. We keep the second paper’s architecture unchanged
and replace its penalties by guarantees that hold by construction, precisely to
isolate
what the guarantee costs.

## Structure-preserving learned schemes.

A recent cluster builds the structure of conservation laws directly into
network architectures. RoeNet embeds Roe solvers(Tonget al.,2024); GoRINNs inform the network with Godunov–Riemann structure(Patsatziset al.,2025); (U)NFV generalizes finite volume updates into neural
architectures with supervised and weak-residual training(Lichtléet al.,2025);
a TVD closure has been shown to work in turbulent combustion(Suhet al.,2025).
A complementary hybrid philosophy keeps the exactly known part of a solution
operator as a classical core and learns only the remainder, shown for equivariant
boundary corrections in Stokes flow(Gueyffier,2026). Our envelope construction applies the same idea to the full scheme for
compressible flow: the classical machinery carries the guarantee, the network
only chooses a position inside it.
Closest to us in spirit is the conservative flux form network family(Chenet al.,2024; Liuet al.,2024), whose latest member learns an entropy-stable
fluxanda convex entropy from trajectory data(Liuet al.,2025). The
resemblance is nominal and the problems are complementary: that line solves an
inverse problem, recovering unknown equations from data, on one-dimensional systems
and uniform grids with two-dimensional scalar extensions. It uses a learned
neural entropy and first-order entropy-stable dissipation, without admissibility
guarantees or cost audits. We solve the forward acceleration problem for a known
system, on unstructured two-dimensional Euler, with the physical entropy, a proved
and contracted inequality, admissibility by construction, and an iso-cost verdict
under frozen thresholds. Neural-operator surrogates for conservation laws (e.g. local-global
operators,Wanget al.,2026) learn full flow maps with striking long-rollout dissipation control, but
without admissibility guarantees or controlled cost audits. To our
knowledge no prior work occupies this cell.

## Entropy-stable and positivity-preserving schemes.

Our guarantee
machinery is deliberately classical: entropy-conservative fluxes and entropy-stable
dissipation(Tadmor,1987,2003; Ismail and Roe,2009; Fjordholmet al.,2012), limiter
envelopes on unstructured meshes(Barth and Jespersen,1989; Venkatakrishnan,1995),
positivity by convex scaling(Zhang and Shu,2010), SSP time integration(Gottlieb and Shu,1998). The contribution is not a new inequality. It is the measured evidence that this
machinery can host a learned reconstruction without giving up its guarantees, at a
price that four method generations drove to parity on one case.

## 3Method

The scheme assembles three layers: a classical second-order finite volume solver,
the learned gradient-correction operator ofde Romémontet al.(2025)kept unchanged,
and the guarantee machinery this paper adds around it.
Figure1and Table1state what is inherited and
what is new; the rest of the section gives each layer in reproducible detail.Figure 1:Concept. Top: the coarse rollout (density fields from the wall case,
Figure2); the orange contract holds for the entire trajectory,
by construction, for any network parameters. Bottom left: inside one step, the
network only reweights the reconstruction stencil (α\alpha, blue, inherited fromde Romémontet al.,2025) and picks a positionλ\lambdainside a provably safe
limiter interval (orange, this work); flux and update are classical modules made
entropy stable and positivity preserving. Right: the unconstrained scheme can leave
the admissible set under distribution shift; ours cannot.Table 1:Starting point versus contribution, component by component.ComponentOriginFV MUSCL solver, SSP-RK2, Rusanov flux, mirror wallsclassicalLearned gradient correction (architecture, features, size)de Romémontet al.(2025)Single-step solver-in-the-loop trainingde Romémontet al.(2025)Soft entropy and TV penaltiesde Romémontet al.(2025),replacedInterval envelope withK​h2Kh^{2}relaxation, learnedλ\lambdathis workExact positivity scaling and adaptive positivity CFLZhang and Shu (2010)+ this workEntropy-stable interior flux with wall closure and contractIsmail and Roe (2009); Tadmor (2003)+ this workFour-generation evaluation under frozen protocolsthis work

## 3.1Base solver

We solve the two-dimensional compressible Euler equations in conservative form,∂t𝐰+∇⋅𝐅​(𝐰)=0\partial_{t}\mathbf{w}+\nabla\!\cdot\!\mathbf{F}(\mathbf{w})=0with𝐰=(ρ,ρ​𝐮,ρ​E)\mathbf{w}=(\rho,\rho\mathbf{u},\rho E), on unstructured triangular meshes with a
cell-centered finite volume scheme,d​𝐰id​t=−1|Ki|​∑f∈∂Ki|f|​𝐅^​(𝐰Lf,𝐰Rf,𝐧f),\frac{d\mathbf{w}_{i}}{dt}=-\frac{1}{|K_{i}|}\sum_{f\in\partial K_{i}}|f|\,\widehat{\mathbf{F}}\!\left(\mathbf{w}_{L}^{f},\mathbf{w}_{R}^{f},\mathbf{n}_{f}\right),(1)

where𝐅^\widehat{\mathbf{F}}is a Rusanov flux in the baseline configuration. The face states𝐰L,Rf\mathbf{w}_{L,R}^{f}are second-order MUSCL reconstructions in primitive variables.
A per-cell gradient is computed by face-weighted least squares over the three
face neighbors; the linear extrapolation from the centroid to the face midpoint
is scaled by a limiter factorϕi∈[0,1]\phi_{i}\in[0,1]per cell and variable. The
limiter is Barth–Jespersen(Barth and Jespersen,1989)or its smooth
Venkatakrishnan variant(Venkatakrishnan,1995)depending on the chain. Time integration uses
the strong stability preserving two-stage Runge–Kutta scheme SSP-RK2(Gottlieb and Shu,1998), a convex combination of forward-Euler steps. Wall
boundaries are treated by mirror ghost states. This baseline, run on a mesh refined until
it matches the learned scheme’s wall-clock cost, is the comparison target throughout
the paper. This followsMcGreivy and Hakim (2024): learned solvers should be measured
against strong classical baselines, not against themselves.

## 3.2Learned gradient reconstruction

Followingde Romémontet al.(2025), the learned component does not replace the
solver: it reweights the gradient stencil. For each cell the network outputs one
coefficient per face neighbor,α∈ℝ3\alpha\in\mathbb{R}^{3}, and the least-squares
weights becomewk​(1+αk)w_{k}(1+\alpha_{k}), so thatα=0\alpha=0recovers the classical
gradient exactly. The inputs are invariant by construction: the branch takes the
twelve differences of primitive variables to the three neighbors (translation
invariance), the trunk takes three angular descriptors of the stencil geometry
(rotation invariance). Boundary cells are forced toα=0\alpha=0. The
architecture is the geometric operator head ofde Romémontet al.(2025): branch12→28→2812\to 28\to 28and trunk3→283\to 28with GELU activations, an elementwise
product, and a linear head, for 1347 parameters in total (their reference network
has 1332). The output is bounded,α=12​tanh⁡(⋅)\alpha=\tfrac{1}{2}\tanh(\cdot), and
vanishes at initialization, so training starts from the classical scheme. The hard
arm uses the same network with one extra head output, a scalarλ∈(0,1)\lambda\in(0,1)per cell obtained by a sigmoid, whose role is defined in
Section3.3. The unconstrained arm ignores that output, so the
two arms have strictly equal capacity. All learned arms are trained
solver-in-the-loop through the differentiable implementation described in
Section3.5.

## 3.3Admissibility by construction

The unconstrained learned scheme can and does leave the admissible set𝒢={𝐰:ρ>0,p​(𝐰)>0}\mathcal{G}=\{\mathbf{w}:\rho>0,\ p(\mathbf{w})>0\}under distribution shift; we
quantify this in Section5. The hard arm removes this failure mode by
construction rather than by penalty, in three nested steps.

## Interval lemma.

For a scalar reconstruction on cellKiK_{i}with limited
slope factorϕ∈[0,ϕBJ]\phi\in[0,\phi_{\mathrm{BJ}}], whereϕBJ\phi_{\mathrm{BJ}}is the Barth–Jespersen factor, every reconstructed face
value lies between the local minimum and maximum of the neighboring cell averages.
The admissible set of slope factors is therefore the interval[0,ϕBJ][0,\phi_{\mathrm{BJ}}]: any learned output mapped into this interval yields a
reconstruction that cannot create new extrema. The learned limiter thus parameterizes
a positioninsidea provably safe envelope, the unstructured analogue of a
Sweby region, instead of an unconstrained correction.

## Relaxed envelope and learned position.

A strict Barth–Jespersen
envelope clips the scheme to first order at smooth extrema. We therefore relax the interval bounds by a fixed termK​hi2Kh_{i}^{2},
withhi=2​Aih_{i}=\sqrt{2A_{i}}the local cell size andK=0.5K=0.5in the
canonical configuration. The relaxation vanishes ash→0h\to 0, preserving the envelope in the limit while restoring second-order
accuracy away from discontinuities. Inside the relaxed envelope, the factor boundϕBJ\phi_{\mathrm{BJ}}is computed with a smooth log-sum-exp softmin over the
face constraints. The softmin is a strict lower bound of the hard minimum at every
temperature, so the bound is conservative for all parameter values. The learned limiter is
then simplyϕ=λ​ϕBJ\phi=\lambda\,\phi_{\mathrm{BJ}}with the network’s
sigmoid outputλ∈(0,1)\lambda\in(0,1). The network chooses a position strictly inside
a provably safe interval, and cannot leave it at initialization or after any
gradient step.

## Positivity and time step.

Reconstruction admissibility does not by itself
guarantee positivity of the updated averages. We combine two mechanisms. The Zhang–Shu scaling limiter(Zhang and Shu,2010)pulls reconstructed states toward the cell average until density and pressure are
positive. An adaptive positivity CFL then sets the time step to the largestΔ​t\Delta t,
capped atCFL=0.3\mathrm{CFL}=0.3, for which the updated averages of the current state remain
in𝒢\mathcal{G}under a first-order bound. Both
SSP-RK2 stages inherit admissibility by convexity. The adaptive step is decisive for the hard arm in long rollouts. At a fixed step
the same scheme fails in the pre-shock regime; the adaptive variant completes every
rollout in our campaigns (Section5). The measured convergence
order of the full hard scheme is 2.33.

## Scope of the guarantee.

The three steps above are properties of the
chain as specified, interior flux and step bound included, and we probed that
scope rather than assuming it. Replacing the entropy-stable flux by a Rusanov
flux and changing nothing else produces one inadmissible cell after about two
thousand steps of the unseen wall case. Bisecting on the step size along both
trajectories locates the failure precisely. The bound admits at least four times
its own step everywhere on the chain we ship. On the substituted chain it keeps
that margin until ten steps before the event, then falls to about one half. The single failing cell carries a wall face, sits in a stagnant
near-vacuum pocket, and has its limiter clamped to zero, so neither the learned
heads nor the relaxed envelope is active there. We therefore read this as a
property of the flux and the boundary treatment near vacuum, not of the learned
construction, and we state the guarantee for the chain we ship.

## 3.4Entropy-stable core

Admissibility bounds the state but not the entropy production mechanism that our wall
diagnostics identify as the actual failure driver (Section5.8). We
therefore replace the interior flux of the learned scheme by an entropy-stable pair
in the sense of Tadmor(Tadmor,1987,2003). The pair is the
entropy-conservative Ismail–Roe flux(Ismail and Roe,2009), built from logarithmic
means of the𝐳\mathbf{z}-vector variables, plus Rusanov-type dissipation applied to the
jump of the conservative state,𝐅^ES=𝐅^EC−12smax⟦𝐰⟧,\widehat{\mathbf{F}}^{\mathrm{ES}}=\widehat{\mathbf{F}}^{\mathrm{EC}}-\tfrac{1}{2}\,s_{\max}\,\llbracket\mathbf{w}\rrbracket,(2)

withsmaxs_{\max}the maximal wave speed at the face. Since the mapping𝐯↦𝐰\mathbf{v}\mapsto\mathbf{w}is the gradient of a convex potential,⟦𝐯⟧⋅⟦𝐰⟧≥0\llbracket\mathbf{v}\rrbracket\cdot\llbracket\mathbf{w}\rrbracket\geq 0, so the dissipation term is
entropy-dissipative and the pair satisfies a discrete cell entropy inequality for the
physical entropyη=−ρ​s/(γ−1)\eta=-\rho s/(\gamma-1). At wall faces the mirror
state makes the entropy flux vanish by symmetry of the𝐳\mathbf{z}-vector, which
extends the inequality to solid boundaries.

Two honest scope notes. First, the inequality above is a first-order statement: the
limited MUSCL reconstruction with the learned limiter is not covered by the proof. We
therefore pair the theorem with a permanent executable contract: on every build, a
200-step rollout on both a periodic and a wall case must produce a nonincreasing
total entropy to tolerance10−1010^{-10}. The campaigns below report the measured
entropy traces. Second, the entropy-stable core costs 7.7% per step over the Rusanov
baseline, and the measured convergence order of the core on a smooth vortex is 2.36;
both numbers enter the iso-cost audit of Section5.2.

## 3.5Training

All arms are trained on the same data with the same optimizer, budget, and
architecture; only the constraint mechanism differs. The reference configuration is
single-step supervised training: fine-grid solutions are projected onto the coarse
mesh, and the network minimizes the discrepancy of a single coarse step against the
projected fine trajectory. An unrolled curriculum (2, then 5, then 10 steps) was chosen in advance as the
mechanism most likely to close the robustness gap of the hard arm.
Section5.8reports its failure to do so. Training details, budgets, and
seeds are given in Section4and AppendixC.

## 4Experimental protocol

## 4.1Discipline

Every experimental campaign in this paper was specified in a frozen protocol sheet
before any computation: arms, cases, seeds, evaluation horizon, decision thresholds,
and, where applicable, an explicit falsification clause. Results are reported against
those thresholds as literal verdicts (supported, indeterminate, failed), including
the negative ones, and every amendment made after first contact with the data is
dated, justified, and kept in the record next to the original. Two such amendments
occurred in this work; both are reported in full (Section5.2and
AppendixB).

## 4.2Arms, cases, and thresholds

Three arms share one architecture, dataset, optimizer, and budget: the classical
baselineB0(Section3.1), the unconstrained learned schemeN(neutral), and the hard arm with admissibility by construction
(Section3.3). The hard arm exists in four successive
generations, each produced by one intervention specified in advance:H(single-step
training),Hu(unrolled curriculum fine-tuning),H′(entropy-stable core
of Section3.4plus wall exposure), andH′′(enlarged data pool
at reduced learning rate). The trajectory of the in-distribution accuracy ratio
across these generations is a primary outcome of the paper, not a tuning byproduct:
each generation was frozen, evaluated, and journaled before the next was specified.

Evaluation uses six cases, each integrated to the same physical horizonT=3000​Δ​tcT=3000\,\Delta t_{c}with paired fine references. Three are in-distribution shock
cases (periodic, initial velocity scale matching training, seeds unseen in
training); two are Mach out-of-distribution cases (periodic, velocity scale 2.5
times training); one is a wall-bounded case whose boundary condition type was never
seen by the single-step arms during training. Figure2shows this
last case: reflections of a random multi-shock state build the fine interaction
structure the coarse mesh must capture.Figure 2:The wall case (unseen boundary-condition type, velocity scale 8,
held-out seed): density at the final horizonTT, square-root color scale. Left
to right: initial state; twice-refined projected reference; guaranteed learned
scheme (coarse mesh); classical baseline (same mesh).
The equal-mesh comparison shown here is illustrative; the cost-matched comparison
is Section5.2.

Each arm is trained with three seeds, and every number we
report is a median over seeds with per-seed values in the appendix. The frozen
thresholds are: S1, zero negativity events over all 18 rollouts of an arm; S2, zero
crashes over the same 18; S3, in-distribution error at most1.05×1.05\timesthe neutral
arm’s, per-case median; S4, an out-of-distribution error count against the neutral
arm; S5, integrity of the classical and entropy-stable baselines on every case. The
falsification clause of the final generation stated in advance that if no
in-distribution ratio improved by more than 0.02, the data-regime hypothesis would be
declared falsified and the paper written on the unimproved frontier point.

## 4.3Iso-cost audit

Accuracy at equal mesh and accuracy at equal wall-clock cost are different
comparisons, and the second is the practically relevant one(McGreivy and Hakim,2024; Kochkovet al.,2021). Our audit, frozen as its own protocol sheet,
measures both on two cases (one in-distribution shock, one wall case with the
unseen boundary condition) at three budgets (one third, two thirds, and the full
horizon). Two follow-up sheets, frozen after first contact with the data and
reported as such, extended it: a factor decomposition of the learned heads, and a
re-measurement of every audit cell under one clean timing protocol. The protocol
fixes identical fixed-step integrators for all families, excludes one warm-up
step from every timing, and crosses two held-out periodic draws with two
independently jittered meshes. The reference
solution for each case is computed on a mesh refined twice by exact 1-to-4
subdivision of the evaluation fine mesh, with composed parent maps. All errors
are thenℓ1\ell_{1}distances between cell averages projected onto one common
coarse mesh. The classical family is anchored by the baseline on the coarse and on the fine
mesh, with log-log interpolation in between. The learned scheme’s gain at iso-cost
is the relative error reduction against that interpolant, taken at the learned
scheme’s own measured cost. Costs are measured with
identical integrators (fixed time step for both families), after JIT warm-up,
medians over repetitions; the protocol’s controls are a bit-identical
deterministic duplicate of the baseline rollout and a smooth-vortex negative control
on which no learned gain is expected. The control fired during the first execution and invalidated our initial cost
measurement. The amendment, its verification, and the corrected pipeline are in
AppendixB, a worked example of what the controls are
for.

## 4.4Reproducibility

A versioned results register is the single source of every number in this paper.
A set of executable contracts, including the entropy inequality check of
Section3.4and golden outputs pinning all flux paths, must pass
before any result is archived. Training resumes from atomic checkpoints with seed-derived permutations;
interrupted and resumed runs are identical. AppendixClists seeds, budgets, and hardware.

## 5Results

## 5.1The unlearned skeleton dominates at equal mesh

A factor decomposition, specified in its own frozen sheet, evaluated the hard
scheme with each learned head switched off. Settingα:=0\alpha:=0recovers the
classical least-squares gradient;λ:=1\lambda:=1sets the limiter at the ceiling
of the relaxed envelope; together they leave the guarantee machinery with no
learned parameter at all. At equal mesh, against a twice-refined reference, this unlearned
skeleton is the strongest scheme on every periodic case, in and out of
distribution. It halves the error of the trained hard scheme in distribution and
beats the trained unconstrained arm by 24 to 53%. On the wall case it survives
all 5503 adaptive steps and beats the trained hard scheme by 24%, where the first
hard generation crashed at every seed. Only the unconstrained arm remains ahead
there, by 12%. Cross comparisons attribute the gain to the reconstruction itself: at
equal entropy-stable flux and equal fixed step, the relaxed-envelope limiter with
exact positivity scaling reduces error by 32 to 39% relative to the
Venkatakrishnan-limited baseline. The relaxation itself is not the driver:
sweepingKKover[0,2][0,2], strict Barth–Jespersen atK=0K=0included,
moves every periodic error by less than 0.4% and the wall error by 0.15%, with
zero negativity events. The gain is the BJ-family envelope with exact positivity
scaling; theK​h2Kh^{2}term is kept for asymptotic consistency, not
tuned. Switching the adaptive step on or off changes every
number by less than 0.05%. Each learned head degrades the skeleton:
the limiter positionλ\lambda, which training left as a near-constant0.910.91insensitive to Mach shift, costs 10 to 33%; the stencil reweightingα\alphacosts up to a factor 4.6 and crashes one in-distribution rollout when
uncompensated. The learned pair behaves as an anti-diffusive perturbation and its
own near-constant damping, whose sum is worse than the structure alone.

## 5.2Iso-cost audit: where learning pays

Table2and Figure3report the iso-cost audit of
Section4.3: every candidate is compared, at its own measured
wall-clock cost, to the log-log interpolation between the classical scheme on the
coarse mesh and the same scheme on the twice-refined mesh. Learning
pays robustly on exactly one case: the wall whose boundary-condition type it never
saw, where the unconstrained arm reduces error by 10.8% (median over seeds). On
periodic cases its gain flips sign with the evaluation draw:+10.3+10.3% on one
held-out draw and−12.2-12.2% on the hardest. This 22-point case effect is stable
across two independently jittered meshes; the mesh effect stays below 2 points. The
unlearned skeleton is the only method whose iso-cost
gain never changes sign (+0.7+0.7to+8.8+8.8%), at a measured per-step overhead of1.74×1.74\timesover the classical scheme. Re-measuring our first audit under this
protocol quantifies a 4-point bias in its original timing, which had included
compilation in the classical scheme’s first point. Deterministic duplicates were
bit-identical in every cell, and the smooth-vortex negative control of the first
audit remains valid (all methods at the representation floor, learned per-step
overhead1.77×1.77\times). The verdict does not depend on the anchor’s flux either:
re-anchoring the classical interpolation on the entropy-stable classical scheme
(same ES core, Venkatakrishnan limiter) moves the anchor error by at most 2.2%
at the anchoring points, consistent with its 4% per-step overhead, and no
iso-cost verdict changes sign. The first execution of that audit was invalidated by
its own control and repaired under a dated amendment
(AppendixB).Table 2:Iso-cost audit (median over 3 seeds for the learned arm; relativeℓ1\ell_{1}error reduction against the log-log cost-interpolated classical baseline;
positive means more accurate at equal wall-clock cost). Learning pays robustly only
on the unseen-boundary wall; the unlearned skeleton never loses.Case (nominal budgetTT)Learned, unconstrainedUnlearned skeletonWall, unseen BC+10.8%\mathbf{+10.8\%}+5.2%+5.2\%Periodic, held-out draw+10.3%+10.3\%+5.9%+5.9\%Periodic, hardest draw−12.2%-12.2\%+0.7%+0.7\%Mach extrapolation−51.7%-51.7\%+8.8%+8.8\%Figure 3:Cost-error map at the nominal budget under the clean timing protocol.
Gray: classical baseline on the coarse and twice-refined meshes with log-log
interpolation. Blue: learned unconstrained arm at its own measured cost (median of
three seeds). Orange: unlearned skeleton. Below the gray line means better at equal
cost: learning wins on the wall and on one held-out periodic draw, loses on the
hardest draw; the skeleton never loses. Errors areℓ1\ell_{1}distances to anh/4h/4reference on the common coarse mesh.

## 5.3The guarantee holds

Across the two campaigns of the final hard generations (H′andH′′),
all 36 rollouts completed with zero negativity events and zero crashes, walls and
Mach extrapolation included. The same architecture without constraints (N)
survives everywhere but offers no guarantee. The first hard generation (H)
crashed on the wall case at all three seeds despite maintaining admissibility to
the last step. The entropy-stable control baseline completed 6 of 6 rollouts with measured
nonincreasing total mathematical entropy (contract tolerance10−1010^{-10}). It
matches the classical baseline’s wall error to 0.3%. The guarantee is therefore not
decorative: it is realized by the code, contractually re-verified at every build, and
compatible with training (the fine-tuned hard arms reach a periodic training loss
below the neutral arm’s).Table 3:Literal verdicts against frozen thresholds, by campaign (three seeds each).
S1: zero negativity over 18 rollouts. S2: zero crashes over 18. S3: in-distribution
error within1.05×1.05\timesthe neutral arm (count of cases passing, of 3). S4:
out-of-distribution error count against neutral (of 3).GenerationS1S2S3S4H(single-step)passfail (wall 3/3)0/30/3Hu(unrolled)passfail (wall 3/3)0/30/3H′(entropy-stable)passpass1/30/3H′′(enlarged data)passpass1/30/3

## 5.4The price of the guarantee shrinks to parity

Table3records every frozen threshold and its verdict by
campaign; Figure4shows the primary outcome. The in-distribution accuracy ratio of the hard arm against the neutral arm,
per-case median over seeds, decreases monotonically across the four
generations: from 1.689 to 1.624, 1.559, and 1.517 on the hardest case; from 1.338
to 1.308, 1.179, and 1.168 on the second; and from 1.131 to 1.116, 1.037, and0.999on the third. On that third case the fully guaranteed scheme now
matches the unconstrained one. The final generation’s
falsification clause did not fire: two of the three ratios improved by more than the
0.02 margin stated in advance (0.042 and 0.038). The data-regime hypothesis
stands, and the remaining gap on the harder cases is not established as a
structural floor.
The wall case tells the same story against the classical baseline: the hard arm went
from crashing (generations one and two) to beating the classical baseline at
equal mesh on two seeds of three (error reductions of 4.1% and 8.5%, the third seed
at−16.2%-16.2\%and improving).Figure 4:The price of hard guarantees between the two learned arms across four
successive method generations: in-distribution error ratio (hard over neutral,
per-case median of 3 seeds). The third case reaches parity (0.999). At equal mesh
both learned arms are beaten on periodic cases by the unlearned skeleton of
Section5.1.

## 5.5Out-of-distribution map

The picture out of distribution is asymmetric and we report it as such. On the wall
case (boundary-condition shift), the hard arm is now the strongest option available
with a guarantee, and competitive without one. On Mach extrapolation (velocity scale 2.5 times training), the hard arm improves
across generations (median errors 8873 to 8513 and 12496 to 11593 on the two cases)
but remains well behind the neutral arm (6551 and 6961). The learned limiter policy
far outside its training distribution was the open weakness of the guaranteed
scheme; wall exposure during fine-tuning did not transfer to Mach shift. The neutral arm itself beats the classical baseline on the wall case by
36% at equal mesh while losing on Mach cases, so no arm dominates the map; the
guarantee, however, is the only property that holds everywhere.

## 5.6Repairing the Mach weakness at inference timeFigure 5:Mechanism and repair of the instability induced by scale-invariant inputs, on the
in-distribution case. Left: minimum pressure along the rollout. The
adimensionalized inputs alone drive a monotone collapse to blow-up at step 596;
the uncorrected hard scheme is stable; the entropy floor removes the collapse.
Right: the margin trade-off. Lighter floors are more accurate,
and margins at or below 0.15 beat the uncorrected scheme (dashed).

An inference-time correction removes most of this weakness, and the mechanism is
instructive. Adimensionalizing the network inputs by the local state (density and
pressure ratios, velocity over the local sound speed) makes the reweighting
scale-invariant: a Mach-shifted state is no longer out of distribution for the
network. On the hard arm this recovers the Mach cases (median error 6057 on the
first, 29% below the uncorrected scheme, three seeds) but
destabilizes the nominal regime. The scale-invariant inputs steepen the
reconstruction wherever relative contrasts are large; the scalar positivity
limiter bounds density and pressure pointwise but does not stop a slow monotone
drift of the minimum pressure toward zero. The reactivity that recovers the shocks
drives the in-distribution blow-up. The remedy is a specific-entropy floor inside
the envelope: the reconstructed face entropys=ln⁡p−γ​ln⁡ρs=\ln p-\gamma\ln\rhomust stay above the minimum ofssover the cell and its face neighbors, minus a
fixed margin of0.050.05. That margin is the lightest tested that removes the blow-up
(Figure5), and it is not arbitrary: on a smooth start 8% of face values dip benignly
below the stencil minimum (median deficit 0.007, 95th percentile 0.040); the
margin sits just above this benign band, and heavier floors only lose accuracy (Figure5,
right). This discrete form of the minimum entropy principle, implemented as a second
convex scaling toward the cell average, caps exactly the drift the positivity
limiter misses.
With the floor no seed crashes, and the corrected arm beats the uncorrected scheme on all three periodic cases (medians−11.7%-11.7\%in
distribution,−28.9%-28.9\%and−14.1%-14.1\%on the Mach cases) with zero negativity
events. On the wall case, with the margin transferred unchanged from the
periodic calibration, every seed completes with zero negativity and the corrected
arm beats the uncorrected scheme by 29% (median 19910, seeds 19126 to 21552, versus 28030, seeds 26745 to 33952),
edging past the unlearned
skeleton (21205); the unconstrained arm keeps a 5.5% lead (18818). On the first
Mach case the corrected guaranteed arm now leads the unconstrained arm (6057
versus 6551); on the second it still trails (9957 versus 6961), by a third less
than before. The floor is a tightening inside the entropy-stable envelope, so the
guarantee is preserved a fortiori, at no retraining cost. The unlearned skeleton
of Section5.1stays ahead of the corrected arm by roughly a
factor of two on every periodic case; on the unseen wall the corrected arm edges
past it, the first learned arm in this study to do so. The correction repairs
the guaranteed scheme’s weakest regimes without displacing the baseline where it
is strongest.

The correction is not a generic ingredient. Applied to the unconstrained arm
on the same wall case, the scale-invariant inputs alone degrade its error by
15 to 22% across the three seeds (median ratio 1.22), with no crash and no
negativity event. This completes an interaction map for the inputs. They hurt
the unconstrained arm, they destabilize the guaranteed arm without the floor
(Figure5, left), and they repair it with the floor. The
guarantees are not a price paid on top of the correction; they are what makes
it usable.

## 5.7A boundary-gated scheme: learning only where it paysFigure 6:The boundary gate. Left: wall error against the gate widthdd(one seed; thed=0d=0andd=∞d=\inftyends are certified against the
skeleton and the full corrected arm). One layer is too thin and slightly
hurts; the best width tested isd=4d=4. Right: transfer to the obstacle
geometry withd=4d=4taken unchanged from the first geometry; dots are the
three seeds, the bar is their median.

The map of Section5.5and the decomposition of
Section5.1pull in opposite directions: the learned heads
degrade the skeleton on periodic cases, yet learning pays on the unseen wall.
A spatial gate resolves the tension at inference time. The heads stay active
only withinddcell layers of the walls; elsewhere the reweighting is off and
the limiter position sits at the envelope bound, which is the skeleton
exactly. The gate is a masked evaluation of the corrected arm of
Section5.6, with no retraining, and the gated points remain
inside the admissible interval, so every guarantee is untouched. Both ends of
the mask are certified: the empty mask reproduces the skeleton wall error to
five digits, and the full mask reproduces the corrected arm to ten.

Withd=4d=4, which activates the heads on 21% of the cells, the gated
scheme reaches a median wall error of 19454 over three seeds. That is 8.3% below the skeleton and below the full corrected arm on every
seed. The wall gain of learning is concentrated near the boundary; the
volumetric action of the heads was a net cost, consistent with the periodic
decomposition. One
layer is too thin (d=1d=1slightly degrades the skeleton); the sweep in
Figure6is one seed, so its fine structure betweend=4d=4andd=8d=8is not resolved, andddwas not tuned further.

The construction transfers. On a second wall geometry, a box with a square obstacle (2464 cells), the
regime is milder and absolute errors are not comparable across geometries. The gate withd=4d=4taken unchanged still beats the skeleton, by 5.3%, and
the full corrected arm on all three seeds. Sweepingddon that second geometry
reproduces the qualitative shape of the first. One layer again degrades the
skeleton and every width from two layers up beats it. The interior minimum is a
broad basin rather than a point, withd=4d=4andd=8d=8within 0.6% of each
other. What transfers is therefore the basin, not a tuned width, which is
why carryingd=4d=4across geometries costs nothing. Across the
twelve gated rollouts and both geometries there is no crash and no negativity
event. The gate turns the out-of-distribution map into a scheme: it learns only where
learning pays, and it beats both of its parents there.

The device is not generic. Applying the same gate to the unconstrained arm yields a strictly monotone
curve. On the same wall case, with the full mask certified to reproduce that arm
exactly, the errors are 27360, 25393, 21927, 19662 and 18818 ford=0,2,4,8d=0,2,4,8and∞\infty. There is no interior optimum, and the best
gated width is 4.5% worse than leaving the arm alone. The two curves differ in kind rather than in degree, and we do not offer a
tested explanation for the difference. The natural candidate is that a gate pays
where the fallback outside the band is strong. It fits these two arms. The guarantee
machinery provides such a fallback, while the unconstrained arm’s own fallback,
the plain classical chain, is 45% worse than its learned form. A
dedicated sweep that degrades the fallback continuously, by mixing the
entropy-stable flux with a Rusanov flux, did not reproduce the trend the
candidate predicts. We therefore record it as an open question rather than a
mechanism.

## 5.8Failure-mode analysis and ablations

Three controlled comparisons ground the design of Section3. First, the unrolled curriculum (Hu), designated in advance as the most likely fix
for the hard arm’s wall crash, changed neither the crash (3 of 3 seeds, same
failure) nor materially the ratios. The neutral arm’s unrolled variant stayed
within the±3%\pm 3\%equivalence band of its single-step version. The single-step training hypothesis for the robustness gap was thereby weakened
before
any architecture change. Second, a frozen diagnostic grid on the failing generation separated the candidate
mechanisms. Halving the envelope relaxation changed the failure mode without fixing
accuracy; quartering it prevented the crash but left wall errors catastrophic;
halving the positivity CFL did not prevent failure. The time-step hypothesis was
eliminated, and envelope pumping under an out-of-distribution limiter policy was
isolated as the driver. Third, the autopsy of the failing rollouts (Figure7) shows
admissibility maintained to the last step while kinetic energy grows by 39% in the final quarter and minimum
pressure collapses by four orders of magnitude. A scheme can be admissible at every
cell and still blow up; that is precisely the gap the entropy-stable core closes.Figure 7:Mechanism of the wall failure of the pre-ES hard generations. Minimum
pressure collapses by four orders of magnitude and kinetic energy grows while the
scheme remains admissible at every cellandits total mathematical entropy
remains nonincreasing: the failure is local entropy pumping, which face-wise
entropy-stable dissipation removes by construction.

## 6Discussion and limitations

## What the decomposition changes.

The most consequential result of this
paper is one we did not set out to find. Our own guarantee machinery, run with no
learned parameter, is the strongest baseline at equal mesh and the only method
that never loses at equal cost. This reframes the earlier generations rather than
erasing them: the trajectory of Section5.4measures the price of
constraints between two learned arms, and both sit above the unlearned skeleton on
periodic cases. Under the clean protocol, learning buys exactly one robust gain, the
unseen-boundary wall case: 10.8% at iso-cost for the unconstrained arm, and a
12% equal-mesh lead over the skeleton. The honest target for
any future learned component, including our planned larger-data campaign, is
therefore to beat the skeleton, not the Venkatakrishnan baseline; we adopt this as
the standing baseline of the program.

## What we did not measure.

We compared hard guarantees against an unconstrained scheme and a classical
baseline, not against a trained soft-penalty arm. The penalty route is represented
here by its published equal-mesh results(de Romémontet al.,2025); a head-to-head comparison of penalties against construction under our protocol
remains to be run. The Mach extrapolation gap of the guaranteed scheme, real in the generation
tables, is explained by the decomposition: it is not structural but an artifact of
the learned heads outside their regime. The skeleton at the envelope ceiling
outperforms every arm there. Section5.6repairs that regime at
inference time, scale-invariant inputs plus a specific-entropy floor, with the skeleton still ahead of the corrected arm on periodic cases. On the
unseen wall the corrected arm edges past it, and the boundary gate of
Section5.7goes further by beating both. The repair is specific to the
guaranteed arm: the same inputs degrade the unconstrained one, so the envelope
is what makes the correction usable. The gate points the same way. It creates
an interior optimum on the guaranteed arm and none on the unconstrained one,
so both inference-time devices we tested pay inside the envelope and nowhere
else. Why the periodic iso-cost gain of learning flips sign between two held-out draws
of the same distribution is recorded as an open question. The harder draw is where
it loses. The next campaign, training-set diversity at scale, is re-targeted
accordingly: its success criterion is to beat the unlearned skeleton.

## Scope of the guarantees.

The entropy inequality is proved at first
order; at second order with the learned limiter it is enforced by a permanent
executable contract and measured on every reported rollout, which is an engineering
guarantee, not a theorem. Admissibility, by contrast, holds by construction at
every order used here. The adaptive positivity time step is part of the guaranteed configuration. The
unconstrained scheme does not need it to survive our cases, shown separately, so
the comparison does not hide a stability subsidy.

## Scale.

Everything here is CPU-scale: two-dimensional Euler, meshes of a few thousand
cells, wall-clock costs in seconds. The iso-cost verdict is a verdict about this regime. Its persistence at larger
scale, where the learned step’s arithmetic intensity favors accelerators, is plausible but unproven; the audit design transfers as is. Sharper
entropy-stable dissipations (kinetic-energy-preserving fluxes,Chandrashekar,2013; Roe-type spectral scaling) fit the same contract
framework and could shift the iso-cost map; we did not measure them. In three dimensions the envelope, positivity scaling, and entropy-stable pairs
carry over; viscous terms need a positivity mechanism for internal energy under
diffusion, new machinery.

## 7Reproducibility statement

The archive accompanying the paper regenerates the datasets from seeds, retrains
all arms, re-runs all evaluations, and rebuilds every figure and table from the raw
evaluation files. The two dated amendments made after first contact with data are
recorded in AppendixB.

We exercised that claim rather than asserting it. After the training artifacts
were lost to an infrastructure failure, the pipeline was rebuilt from the frozen
seeds alone. The regenerated dataset matched the recorded volume, retraining one
seed of the corrected arm reproduced the recorded final loss, and the rebuilt
weights reproduced the reported wall error of Section5.6to
nine significant digits. On the obstacle geometry, whose reference was rebuilt in
the same way, the skeleton and the corrected arm reproduced their reported values
to five significant digits and to the same step count. Reproducibility here is a
property of the repository, not an intention.

## Acknowledgments and disclosure.

Drafting, editing, and figure
scripting were assisted by an AI system (Claude, Anthropic) operating under the
author’s direction. Every number originates from the versioned results register of
Section7and was verified against the raw evaluation files. The
author reviewed and approves all content.

## References
- Y. Bar-Sinai, S. Hoyer, J. Hickey, and M. P. Brenner (2019)Learning data-driven discretizations for partial differential equations.Proceedings of the National Academy of Sciences116(31),pp. 15344–15349.Cited by:§2.
- T. J. Barth and D. C. Jespersen (1989)The design and application of upwind schemes on unstructured meshes.In27th AIAA Aerospace Sciences Meeting,Cited by:§1,§2,§3.1.
- P. Chandrashekar (2013)Kinetic energy preserving and entropy stable finite volume schemes for compressible Euler and Navier–Stokes equations.Communications in Computational Physics14(5),pp. 1252–1286.Cited by:§6.
- Z. Chen, A. Gelb, and Y. Lee (2024)Learning the dynamics for unknown hyperbolic conservation laws using deep neural networks.SIAM Journal on Scientific Computing46(2),pp. A825–A850.Cited by:§2.
- G. de Romémont, F. Renac, F. Chinesta, J. Nunez, and D. Gueyffier (2025)Data-driven adaptive gradient recovery for unstructured finite volume computations.arXiv preprint arXiv:2507.16571.Cited by:Appendix C,§1,§2,Figure 1,§3.2,Table 1,Table 1,Table 1,§3,§6.
- G. de Romémont, F. Renac, J. Nunez, D. Gueyffier, and F. Chinesta (2026)A data-driven learned discretization approach in finite volume schemes for hyperbolic conservation laws and varying boundary conditions.Computers & Fluids307,pp. 106978.Note:Also arXiv:2412.07541External Links:DocumentCited by:§1,§2.
- U. S. Fjordholm, S. Mishra, and E. Tadmor (2012)Arbitrarily high-order accurate entropy stable essentially nonoscillatory schemes for systems of conservation laws.SIAM Journal on Numerical Analysis50(2),pp. 544–573.Cited by:§2.
- S. Gottlieb and C. Shu (1998)Total variation diminishing Runge-Kutta schemes.Mathematics of Computation67(221),pp. 73–85.Cited by:§2,§3.1.
- D. Gueyffier (2026)Solver exactness, learned flexibility: equivariant boundary-correction operators for Stokes flow.arXiv preprint arXiv:2606.25075.Cited by:§2.
- F. Ismail and P. L. Roe (2009)Affordable, entropy-consistent Euler flux functions II: entropy production at shocks.Journal of Computational Physics228(15),pp. 5410–5436.Cited by:Appendix A,§2,§3.4,Table 1.
- D. Kochkov, J. A. Smith, A. Alieva, Q. Wang, M. P. Brenner, and S. Hoyer (2021)Machine learning–accelerated computational fluid dynamics.Proceedings of the National Academy of Sciences118(21),pp. e2101784118.Cited by:§2,§4.3.
- N. Lichtlé, A. Canesse, Z. Fu, H. N. Z. Matin, M. L. Delle Monache, and A. M. Bayen (2025)(U)NFV: supervised and unsupervised neural finite volume methods for solving hyperbolic PDEs.arXiv preprint arXiv:2505.23702.Cited by:§2.
- L. Liu, T. Li, A. Gelb, and Y. Lee (2024)Entropy stable conservative flux form neural networks.arXiv preprint arXiv:2411.01746.Cited by:§2.
- L. Liu, L. Zhang, and A. Gelb (2025)Neural entropy-stable conservative flux form neural networks for learning hyperbolic conservation laws.arXiv preprint arXiv:2507.01795.Cited by:§2.
- N. McGreivy and A. Hakim (2024)Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations.Nature Machine Intelligence6(10),pp. 1256–1269.Cited by:§1,§3.1,§4.3.
- D. G. Patsatzis, M. di Bernardo, L. Russo, and C. Siettos (2025)GoRINNs: Godunov-Riemann informed neural networks for learning hyperbolic conservation laws.Journal of Computational Physics534,pp. 114002.Cited by:§2.
- S. W. Suh, J. F. MacArt, L. N. Olson, and J. B. Freund (2025)A TVD neural network closure and application to turbulent combustion.Journal of Computational Physics523,pp. 113638.Cited by:§2.
- E. Tadmor (1987)The numerical viscosity of entropy stable schemes for systems of conservation laws. I.Mathematics of Computation49,pp. 91–103.Cited by:§1,§2,§3.4.
- E. Tadmor (2003)Entropy stability theory for difference approximations of nonlinear conservation laws and related time-dependent problems.Acta Numerica12,pp. 451–512.Cited by:§2,§3.4,Table 1.
- Y. Tong, S. Xiong, X. He, S. Yang, Z. Wang, R. Tao, R. Liu, and B. Zhu (2024)RoeNet: predicting discontinuity of hyperbolic systems from continuous data.International Journal for Numerical Methods in Engineering125(6),pp. e7406.Cited by:§2.
- V. Venkatakrishnan (1995)Convergence to steady state solutions of the Euler equations on unstructured grids with limiters.Journal of Computational Physics118(1),pp. 120–130.Cited by:§2,§3.1.
- H. Wang, C. Shu, and Q. Tang (2026)LGNO: a local-global neural operator for hyperbolic conservation laws.Note:arXiv:2606.18221Cited by:§2.
- X. Zhang and C. Shu (2010)On positivity-preserving high order discontinuous Galerkin schemes for compressible Euler equations on rectangular meshes.Journal of Computational Physics229(23),pp. 8918–8934.Cited by:Appendix A,§1,§2,§3.3,Table 1.
- J. Zhuang, D. Kochkov, Y. Bar-Sinai, M. P. Brenner, and S. Hoyer (2021)Learned discretizations for passive scalar advection in a two-dimensional turbulent flow.Physical Review Fluids6,pp. 064605.Cited by:§2.

## Appendix AStatements and proof sketches

We state the classical results in the form our code implements, with the
executable contract that checks each one.

## Lemma 1(Interval envelope).

Letw¯i\underline{w}_{i}andw¯i\overline{w}_{i}be the minimum and maximum of the cell average
of𝐰\mathbf{w}over cellKiK_{i}and its face neighbors, and letϕBJ,i\phi_{\mathrm{BJ},i}be the Barth–Jespersen factor. For anyϕi∈[0,ϕBJ,i]\phi_{i}\in[0,\phi_{\mathrm{BJ},i}], every face value reconstructed from
the cell average with slope scaled byϕi\phi_{i}lies in[w¯i,w¯i][\underline{w}_{i},\overline{w}_{i}].

Sketch.The reconstruction is affine inϕi\phi_{i}, equal to the cell
average atϕi=0\phi_{i}=0and inside the interval atϕi=ϕBJ,i\phi_{i}=\phi_{\mathrm{BJ},i}by definition of the factor; the interval is
convex. The learned output enters only as a sigmoid factorλi∈(0,1)\lambda_{i}\in(0,1)multiplyingϕBJ,i\phi_{\mathrm{BJ},i}, computed with a log-sum-exp softmin
that bounds the hard minimum from below at every temperature.
The property therefore holds for all network parameters, not only at convergence. The relaxed envelope addsK​h2Kh^{2}times a smoothness indicator to the interval bounds; the addition
vanishes under refinement. Contract: golden-path tests pin the clamp, and campaign
evaluations count negativity events (zero across all reported rollouts).

## Proposition 1(Positivity of the update).

With reconstructed states scaled toward the cell average by the Zhang–Shu limiter
until density and pressure are positive, and a time step below the positivity bound
computed from the current state with a first-order flux estimate, the forward-Euler
update of every cell average remains in𝒢\mathcal{G}; both SSP-RK2 stages, being convex
combinations of such updates, inherit the property.

Sketch.Standard argument ofZhang and Shu (2010)adapted to face-based
unstructured quadrature; the adaptive step, capped atCFL=0.3\mathrm{CFL}=0.3, enforces the
bound at run time rather than assuming it. Contract: the evaluation code asserts
positivity of every stored state.

## Proposition 2(First-order entropy inequality, wall included).

The flux pair of Eq. (2), an Ismail–Roe entropy-conservative flux
plus Rusanov dissipation on the conservative jump, satisfies a discrete cell entropy
inequality for the physical entropy pair; at a wall face, the mirror state makes the
numerical entropy flux vanish, so the inequality extends to solid boundaries.

Sketch.Entropy conservation of the Ismail–Roe flux is by construction of
the logarithmic means(Ismail and Roe,2009); the dissipation term contributes−12smax⟦𝐯⟧⊤⟦𝐰⟧≤0-\tfrac{1}{2}s_{\max}\llbracket\mathbf{v}\rrbracket^{\!\top}\llbracket\mathbf{w}\rrbracket\leq 0because𝐰​(𝐯)\mathbf{w}(\mathbf{v})is the gradient of a convex potential; the wall statement follows
from the antisymmetry of the normal velocity and the symmetry of the remaining𝐳\mathbf{z}-components under mirroring. The statement covers the first-order flux; the
limited second-order reconstruction is outside the proof and covered by the
permanent contract of Section3.4and the measured traces of
Figure7.

## Appendix BAmendments to the iso-cost measurement

We report the one instance where the controls invalidated our own measurement,
and the two dated amendments that followed.

The first execution produced negative iso-cost verdicts on both cases and a
smooth-vortex control far outside its band. The discriminating test found the
cause. The evaluation loop of the learned arm
called its adaptive time-step routine outside the compiled graph, forcing one
device-to-host synchronization per step. A fixed-step rerun of the same weights on
the same case produced the same error to the last digit at 2.3 times less
wall-clock cost. The cost measurement, not the scheme, was wrong. A dated amendment, frozen before any re-verdict, switched the timing to
identical fixed-step integrators, keeping the adaptive step in production. At fixed step the unconstrained scheme survived the wall at all seeds, so the
audit does not subsidize its stability.

The rerun then exposed a second, independent flaw, this time in the control
itself. Its baseline anchors mixed unnormalized error sums across two unrelated meshes;
its sub-second costs sat in the dispatch-noise regime. The repaired control refines the mesh by exact 1-to-4 subdivision, projects
through parent maps, and runs past the noise floor. On the repaired control every method sits at the representation floor and no net
learned gain appears: the pass condition. The honest per-step overhead of the learned scheme,1.77×1.77\times, is
measured there. All
three measurement generations remain in the shipped raw files.

## Appendix CExperimental details

## Network.

The learned operator is the four-output geometric head ofde Romémontet al.(2025)with hidden width 28, totaling 1347 parameters; inputs are rotation- and translation-invariant
stencil descriptors and neighbor state differences. The softmin-LSE limiter relaxation appears only in training, for
differentiability (temperature 50); reported rollouts use the exact minimum. The same initialization scheme
and parameter count are used in every learned arm.

## Meshes and data.

Coarse and fine evaluation meshes have 2592 and 10368
triangles (jittered structured triangulations, factor-two pairs); the iso-cost references
add an exact 1-to-4 subdivision (41472 triangles).
Training data are 8 periodic fine-mesh trajectories projected to the coarse mesh
(generator seeds1000⋅s1000\cdot s). The final generation extends the pool to 10 periodic plus 3 wall trajectories
(wall seeds 8000 to 8002). The obstacle geometry of Section5.7removes a grid-aligned central square from the wall box (2464 cells, 32 wall
faces added by the hole); its reference follows the same twice-refined
protocol with generator seed 7300. Evaluation seeds are 7000 to 7002 (in-distribution), 7100 and 7101
(Mach), and 7200 (wall), all unseen in training.

## Training.

Single-step arms: 12 epochs of full passes over the dataset in
batches of 64 with the Lion optimizer at learning rate6×10−56\times 10^{-5}; identical
budgets for the neutral and hard arms. Entropy-stable fine-tuning (H′): 6
epochs of 250 batches of 64, Lion at6×10−56\times 10^{-5}, warm-started from the hard
single-step weights, alternating periodic and wall data 4:1. Final generation
(H′′): 6 further epochs at2×10−52\times 10^{-5}on the enlarged pools with a
frozen innocuousness guard on the periodic loss. Training seeds are 1, 2, and 3;
per-epoch data permutations are derived deterministically from the seed and epoch
index, so interrupted and resumed runs are identical.

## Hardware and timing.

All computations ran on a single-vCPU container (Intel Xeon, 2.80 GHz) in
double precision with JIT-compiled JAX. Wall-clock costs (Section5.2) are medians on this machine,
compilation excluded. The entropy-stable core converges at second order on the isentropic vortex
(successive-refinement slopes 2.35 and 2.29, Venkatakrishnan limiter,ω=(5​h)3\omega=(5h)^{3}); its per-step overhead over the Rusanov baseline is 7.7%,
and the full learned step costs 77% over the classical step, the1.77×1.77\timesentering the audit. No GPU was used anywhere in this paper.

## 


- 


Major funding support from
