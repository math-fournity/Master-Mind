# Nuclear Quantum Effects as a Denoising Problem

**arXiv ID**: 2607.19680v1
**Authors**: Weizhou Wang, Jonathan Weare, Aaron R. Dinner
**Published**: 2026-07-22
**Categories**: physics.chem-ph, cond-mat.stat-mech, cs.LG, physics.comp-ph, quant-ph
**Comments**: 9 pages, 3 figures
**HTML URL**: https://arxiv.org/html/2607.19680v1

## Abstract

Nuclear quantum effects are rigorously captured by imaginary-time path integrals, which map the quantum Boltzmann distribution onto a ring polymer of classical replicas. Yet the nuclear masses, the coupling to the environment, and the boundary conditions of the path remain hard-wired in the simulation or the trained model, even though this quantum context enters the path measure only through a quadratic action known in closed form. Here we show that a denoiser trained on classical Boltzmann statistics alone, composed at sampling time with an analytic Gaussian component carrying the entire quantum context, yields the quantum Boltzmann distribution of the nuclei. Such a composition exists and is exact whenever the training noise does not exceed the intrinsic quantum uncertainty of the target ensemble, and it is invariant across all quantum contexts admitted by this bound. We show exact transfer across temperature, isotopic mass, dissipation strength, and the boundary conditions of the path in theory and in numerical experiments, without retraining. The last yields the end-to-end displacement and momentum distributions of a tagged nucleus from open imaginary-time paths. The same invariance extends in principle to the permuted boundary conditions of bosonic exchange, with the identical denoiser. In this view, the noise of generative modeling and the quantum fluctuations of the nuclei are two faces of the same quadratic structure.

## Full Text

Nuclear Quantum Effects as a Denoising Problem

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
- License: CC BY 4.0arXiv:2607.19680v1 [physics.chem-ph] 22 Jul 2026

## Nuclear Quantum Effects as a Denoising ProblemWeizhou WangDepartment of Chemistry, University of Chicago, Chicago, Illinois 60637, USAJames Franck Institute, University of Chicago, Chicago, Illinois 60637, USAJonathan Weareweare@nyu.eduCourant Institute of Mathematical Sciences, New York University, New York, New York 10012, USAAaron R. Dinnerdinner@uchicago.eduDepartment of Chemistry, University of Chicago, Chicago, Illinois 60637, USAJames Franck Institute, University of Chicago, Chicago, Illinois 60637, USA

## Abstract

Nuclear quantum effects are rigorously captured by imaginary-time path integrals, which map the quantum Boltzmann distribution onto a ring polymer of classical replicas. Yet the nuclear masses, the coupling to the environment, and the boundary conditions of the path remain hard-wired in the simulation or the trained model, even though this quantum context enters the path measure only through a quadratic action known in closed form. Here we show that a denoiser trained on classical Boltzmann statistics alone, composed at sampling time with an analytic Gaussian component carrying the entire quantum context, yields the quantum Boltzmann distribution of the nuclei. Such a composition exists and is exact whenever the training noise does not exceed the intrinsic quantum uncertainty of the target ensemble, and it is invariant across all quantum contexts admitted by this bound. We show exact transfer across temperature, isotopic mass, dissipation strength, and the boundary conditions of the path in theory and in numerical experiments, without retraining. The last yields the end-to-end displacement and momentum distributions of a tagged nucleus from open imaginary-time paths. The same invariance extends in principle to the permuted boundary conditions of bosonic exchange, with the identical denoiser. In this view, the noise of generative modeling and the quantum fluctuations of the nuclei are two faces of the same quadratic structure.

## IIntroduction

Zero-point energy and tunneling of light nuclei govern phenomena ranging from the hydrogen-bond network of liquid water to isotope effects and proton transfer in biomolecules. Standard molecular dynamics (MD) treats the nuclei classically, neglecting these effects[22]. The path-integral formulation provides a rigorous framework to map the quantum Boltzmann distribution onto a classical ring polymer ofPPreplicas (beads) of the system connected by harmonic springs[5]. Path-integral molecular dynamics (PIMD)[2,31]and path-integral Monte Carlo (PIMC)[25,11,12]exploit this isomorphism to incorporate nuclear quantum effects (NQEs) rigorously, atPPtimes the cost of the corresponding classical simulation.

This cost has driven two broad strategies. The first retains the ring polymer but lowers the cost of each step or the number of steps needed to converge, through ring-polymer contraction[23], advanced integrators[4,21], or machine-learned force fields (MLFFs)[7,18]. The second discards the ring polymer altogether, replacing it with a single classical system governed by an effective potential[26,35]or driven by a colored-noise thermostat[3], generally at the price of approximations. Recently, GG-PI[34]opened a third, generative route. It recognizes that the distribution of a single bead conditioned on its neighbors is the posterior of a Gaussian denoising problem, in which the noise variance reflects the quantum fluctuations. The denoiser can be trained on classical statistics alone and transfer across temperatures by adjusting the number of beadsPPat a fixed imaginary-time sliceτ=β/P\tau=\beta/P. In these methods, however, the remaining quantum context stays hard-wired. The nuclear masses and the coupling to a dissipative bath are fixed either in the simulation or, in GG-PI, in the very noise the model is trained to remove. Changing any one of them requires a new simulation or a retrained model, even though each enters the path measure only through the quadratic part of the action, which is known in closed form. Existing methods entangle this analytically known structure with the anharmonic classical statistics that must be learned.

Here we show that this structure can be exploited in full, so that nuclear quantum effects are injected entirely at sampling time rather than encoded in the learned model. The discretized imaginary-time action naturally separates into two parts: a quadratic term in the bead coordinates that encapsulates the complete quantum context in closed form, with the harmonic springs of the bare ring polymer as its simplest instance, and a residual potential term that factorizes into purely classical single-bead Boltzmann factors, blind to the quantum context. The entire quantum context enters the path measure as correlated Gaussian noise acting on otherwise independent classical replicas. Therefore, a denoiser trained to remove Gaussian noise from this classical distribution can be composed at sampling time with a matching quadratic component to recover the target path distribution exactly. This composition exists as long as the training noise does not exceed the intrinsic quantum uncertainty prescribed by the target ensemble, establishing a physical bound for the denoiser. Changing any element of the quantum context, including nuclear mass, bath coupling, and even the boundary conditions of the imaginary-time path, thus amounts to recomputing this quadratic component, with the denoiser left untouched. Mathematically, the composition is a real Hubbard–-Stratonovich[29,16]transformation applied not to the confining quadratic action, which admits no real decoupling field, but to its complement within the training noise, with the physical bound above as the positivity condition of that complement (End Matter). The construction thereby offers an alternative to the imaginary-field route for confining quadratic forms, at the price of a bounded noise and a learnable residual.

We demonstrate the exact transferability of DPI across temperature, isotope, bath coupling, and boundary conditions without retraining on three systems of increasing complexity. In a double-well coupled to a Caldeira–Leggett bath[1,24], a single denoiser tracks numerically exact reference values as the temperature and dissipation strength are varied at sampling time. In the Zundel cation and in liquid water, the same construction reproduces proton delocalization and radial distribution functions across different temperatures and isotopic substitutions, in agreement with reference path-integral simulations. In water, opening the imaginary-time path of a tagged nucleus with the same denoiser further yields its end-to-end displacement and momentum distributions, which probe the thermal density matrix beyond the diagonal sampled by closed paths. The quantum context thereby becomes a property set at sampling time rather than one learned by the model: within each system, a single denoiser trained once supplies the classical Boltzmann statistics, while temperature, mass, dissipation, and the boundary conditions of the path enter through an analytic Gaussian component drawn at each sampling step. The same invariance extends beyond distinguishable particles, since bosonic exchange merely permutes the boundary conditions of the paths, entering through the analytic step (End Matter).

## IIMethod

We consider a system of distinguishable particles in the canonical (N​V​TNVT) ensemble at inverse temperatureβ\beta. In the main text we present the primitive discretization together with an isotropic Gaussian noise model.

Discretizing the imaginary time intoPPslices of widthτ=β/P\tau=\beta/Pmaps the quantum Boltzmann distribution onto a ring polymer ofPPreplicas𝐱=(𝐱1,…,𝐱P)\mathbf{x}=(\mathbf{x}_{1},\dots,\mathbf{x}_{P}),𝐱k∈ℝd​N\mathbf{x}_{k}\in\mathbb{R}^{dN}with𝐱P+1≡𝐱1\mathbf{x}_{P+1}\equiv\mathbf{x}_{1}[5,12]. The discretized action splits into a quadratic and a residual part,{gathered}​π​(𝐱)∝exp⁡[−\tfrac​12​𝐱⊤​K​𝐱]​exp⁡[−U​(𝐱)],U​(𝐱)=τ​∑k=1PV​(𝐱k).\gathered\pi(\mathbf{x})\;\propto\;\exp\!\Big[-\tfrac 12\,\mathbf{x}^{\top}K\,\mathbf{x}\Big]\,\exp\!\big[-U(\mathbf{x})\big],\\
U(\mathbf{x})=\tau\sum_{k=1}^{P}V(\mathbf{x}_{k}).(1)

The positive-semidefinite matrixKKcollects the analytically known quadratic context. Its simplest instance is the bare ring polymer, where\tfrac​12​𝐱⊤​K​𝐱=12​ℏ2​τ​∑k=1P(𝐱k+1−𝐱k)⊤​M​(𝐱k+1−𝐱k)\tfrac 12\mathbf{x}^{\top}K\mathbf{x}=\frac{1}{2\hbar^{2}\tau}\sum_{k=1}^{P}(\mathbf{x}_{k+1}-\mathbf{x}_{k})^{\top}M(\mathbf{x}_{k+1}-\mathbf{x}_{k})is the harmonic spring energy coupling neighboring beads, withMMthe diagonal mass matrix. For a system with additional harmonic terms, or one linearly coupled to a Caldeira–Leggett bath,KKis a more general positive-semidefinite matrix, still known in closed form. The residualUUcollects the remaining single-bead potentialsVV, so thate−U=∏ke−τ​V​(𝐱k)e^{-U}=\prod_{k}e^{-\tau V(\mathbf{x}_{k})}is a product of independent classical Boltzmann factors, all governed by the same potentialVVat inverse temperatureτ\tau.

We introduce an auxiliary path𝐲=(𝐲1,…,𝐲P)\mathbf{y}=(\mathbf{y}_{1},\dots,\mathbf{y}_{P})and construct the joint distribution{gathered}​p​(𝐱,𝐲)=π​(𝐱)​p​(𝐲∣𝐱),p​(𝐲∣𝐱)=𝒩​(𝐲;(I−σ2​K)​𝐱,σ2​(I−σ2​K)).\gathered p(\mathbf{x},\mathbf{y})=\pi(\mathbf{x})\,p(\mathbf{y}\mid\mathbf{x}),\\
p(\mathbf{y}\mid\mathbf{x})=\mathcal{N}\!\big(\mathbf{y};\,(I-\sigma^{2}K)\mathbf{x},\;\sigma^{2}(I-\sigma^{2}K)\big).(2)

For any normalized conditional, integrating out𝐲\mathbf{y}returns the target, so the𝐱\mathbf{x}-marginal of Eq.\eqrefeq:joint is exact by construction. The Gaussian channel in Eq.\eqrefeq:joint is tuned so that the reverse conditionalp​(𝐱∣𝐲)p(\mathbf{x}\mid\mathbf{y})is freed of the quadratic contextKK.

Completing the square in𝐱\mathbf{x}(detailed in End Matter) gives the reverse conditional{aligned}​p​(𝐱∣𝐲)∝exp⁡[−\lVert​𝐱−𝐲​\rVert22​σ2−U​(𝐱)]=∏k=1Pexp⁡[−\lVert​𝐱k−𝐲k​\rVert22​σ2−τ​V​(𝐱k)].\aligned p(\mathbf{x}\mid\mathbf{y})&\;\propto\;\exp\!\Big[-\frac{\lVert\mathbf{x}-\mathbf{y}\rVert^{2}}{2\sigma^{2}}-U(\mathbf{x})\Big]\\
&\;=\;\prod_{k=1}^{P}\exp\!\Big[-\frac{\lVert\mathbf{x}_{k}-\mathbf{y}_{k}\rVert^{2}}{2\sigma^{2}}-\tau V(\mathbf{x}_{k})\Big].(3)

The quadratic contextKKhas cancelled entirely. Eq.\eqrefeq:posterior is exactly the Bayesian posterior of recovering a classical configuration𝐱k∼e−τ​V\mathbf{x}_{k}\sim e^{-\tau V}from an observation𝐲k=𝐱k+σ​𝝃\mathbf{y}_{k}=\mathbf{x}_{k}+\sigma\bm{\xi}corrupted by isotropic Gaussian noise—the denoising posterior underlying score-based and flow-based generative models[28,20]. BecauseUUis a sum of single-bead terms, this posterior factorizes over beads and one denoiser acting on a single replica suffices.

For the Gaussian channel in Eq.\eqrefeq:joint to be a valid distribution, its covarianceσ2​(I−σ2​K)\sigma^{2}(I-\sigma^{2}K)must stay positive definite, which caps the noise variance:σ2<λmax​(K)−1.\sigma^{2}<\lambda_{\max}(K)^{-1}.(4)

For the bare ring polymer, it reduces toσ2<ℏ2​τ/4​m\sigma^{2}<\hbar^{2}\tau/4m, one quarter of the free-particle mean-square imaginary-time displacement between adjacent slices[32]. Equation\eqrefeq:ceiling is the physical bound on the denoiser: the injected noise cannot exceed the quantum uncertainty encoded in the quadratic action, which is set by the stiffest mode.

We sample the joint density in Eq.\eqrefeq:joint by Gibbs sampling[9], which constructs a Markov chain to iteratively draw each variable from its conditional distribution. In our case, the conditional distribution is given by Eq.\eqrefeq:joint and Eq.\eqrefeq:posterior. In each sweep, we alternate between two steps: (i) an analytic Gaussian draw𝐲∼p​(𝐲∣𝐱)\mathbf{y}\sim p(\mathbf{y}\mid\mathbf{x})from Eq.\eqrefeq:joint, which injects the quantum context throughKK; and (ii) a bead-wise denoising draw𝐱∼p​(𝐱∣𝐲)\mathbf{x}\sim p(\mathbf{x}\mid\mathbf{y})from Eq.\eqrefeq:posterior, supplied by the learned denoiser. The quantum context and the classical statistics thus enter through two separate, alternating updates.

This separation makes the construction transferable in a strong sense. For any family of quadratic contexts sharing the residualVV, the sliceτ\tau, and the noise level, the reverse conditional Eq.\eqrefeq:posterior is the same for every member (End Matter). A single denoiser therefore samples an entire family of quantum ensembles, with temperature entering through the bead numberPPat fixedτ\tau, isotopic mass throughMMinKK, dissipation through the bath kernel inKK, and the boundary conditions of the path through the connectivity thatKKencodes.

In practice we realize Eq.\eqrefeq:posterior with a conditional continuous normalizing flow trained by flow matching[20](End Matter). Since only the conditionalp​(𝐱∣𝐲)p(\mathbf{x}\mid\mathbf{y})is needed, training pairs may come from standard MD at inverse temperatureτ\tau, restrained MD, or existing PIMD trajectories, all of which yield the same conditional (End Matter).

## IIIResults

We validate the framework on three systems of increasing complexity. Within each system a single denoiser is used for all test conditions, at a fixed noise model whose per-component levels satisfy the ceiling Eq.\eqrefeq:ceiling throughout. The quantum context enters only through the analytic Gaussian step. In the Caldeira–Leggett double well the denoiser is numerically exact, giving a clean test of transfer across temperature and bath coupling. The Zundel cation uses a learned denoiser to test transfer across temperature and isotopic mass. In liquid water, we validate transfer across isotopic mass and use the same denoiser to sample open imaginary-time paths, testing transfer across the boundary conditions of the path.

## III.1Dissipative double well

We first validate our framework in the dissipative double well, a particle in a symmetric quartic double wellV​(x)=(x2−1)2V(x)=(x^{2}-1)^{2}linearly coupled to an Ohmic bath of harmonic oscillators. This is a canonical benchmark for open quantum systems and the dissipation-driven quantum-to-classical crossover[1,24]. Integrating out the bath couples the beads nonlocally while keeping the quadratic form:{aligned}​\tfrac​12​𝐱⊤​K​𝐱=m2​ℏ2​τ​∑k(xk+1−xk)2+α​∑k<l(π/P)24​sin2⁡[π​(k−l)/P]​(xk−xl)2.\aligned\tfrac 12\,\mathbf{x}^{\top}K\,\mathbf{x}&=\frac{m}{2\hbar^{2}\tau}\sum_{k}(x_{k+1}-x_{k})^{2}\\
&\quad+\alpha\sum_{k<l}\frac{(\pi/P)^{2}}{4\sin^{2}[\pi(k-l)/P]}\,(x_{k}-x_{l})^{2}.(5)

The first term is the ring-polymer springs and the second is the long-ranged imaginary-time kernel of the Ohmic bath[24], whose strengthα\alphasets the dissipation. Crucially,K=Kspr+α​KbathK=K_{\mathrm{spr}}+\alpha\,K_{\mathrm{bath}}is linear inα\alpha.α=0\alpha=0is the isolated well, and increasingα\alphastrengthens the bath coupling and suppresses quantum delocalization between the wells. Because the system is one-dimensional, the single-bead posterior Eq.\eqrefeq:posterior is available by direct numerical quadrature, so the denoiser here is numerically exact. A single noise levelσ\sigma, below the ceiling Eq.\eqrefeq:ceiling across test parameters, is used throughout. Changingα\alphaor the temperature then alters only the analytic Gaussian step.Figure 1:Bath and temperature transfer in the Caldeira–Leggett double well.
(a) Centroid distribution for bath couplingsα=0,1,2\alpha=0,1,2. Increasingα\alphadrives the distribution from unimodal (the particle delocalized over both wells) to bimodal (localized in the wells).
(b) Radius of gyrationRgR_{g}versus inverse temperatureβ\betaat fixedτ\taufor the same couplings.RgR_{g}increases as the temperature decreases and decreases with coupling.
Solid: our method with a single denoiser; dashed: PIMC reference.

Figure1shows that a single denoiser reproduces the PIMC reference across all three couplings and across temperature at fixedτ\tau.

## III.2Zundel cation

The Zundel cationH5​O2+\mathrm{H_{5}O_{2}^{+}}describes a shared proton between two water molecules. It is a benchmark for nuclear quantum effects in hydrogen bonding and proton transfer[15,30]. Here the denoiser is a learned model trained on existing PIMD trajectories at300​K300~\mathrm{K}withP=32P=32, then applied across isotopes (H, D, T) and temperatures.

We examine two isotope effects. Fig.2(a) reports the distribution of the radius of gyrationRgR_{g}of the shared nucleus for the three isotopes. Fig.2(b) reports its site preference. On replacing one H by D or T, the heavier isotope may occupy one of the four peripheralO−H\mathrm{O\!-\!H}sites or the central shared site, and we compute its probability of being peripheral. Because mass enters only throughKK, this probability follows from an alchemical path in mass. We sample the corresponding sequence ofKKmatrices with the same denoiser and obtain the free energy between the shared and peripheral sites by MBAR[27].Figure 2:Isotope effects in the Zundel cation.
(a) Radius of gyrationRgR_{g}of the shared nucleus for H, D, and T at300​K300~\mathrm{K}withP=32P=32.
(b) Probability that a substituted isotope occupies a peripheral site rather than the central shared site (highlighted in yellow in the illustration), versus temperature at fixedτ\tau. Heavier isotopes prefer the peripheral sites more strongly, and the preference weakens with temperature. The dotted line marks the isotope-free value4/54/5.
Solid: our method with a single denoiser. Dashed: PIMD reference.

The shared-nucleusRgR_{g}decreases from H to D to T (Fig.2(a)), so heavier isotopes are less delocalized. Heavier isotopes also favor the peripheral sites over the shared site, and this preference grows with mass and weakens with temperature (Fig.2(b)). Across isotopes and temperatures the single denoiser matches the PIMD reference.

## III.3Liquid water

Finally, we apply the framework to liquid water,216216molecules in a periodic box at300​K300~\mathrm{K}withP=32P=32, described by the q-TIP4P/F force field[10]. Here the denoiser is trained from restrained MD. For each classical configuration𝐲\mathbf{y}, a short MD run restrained toward𝐲\mathbf{y}draws a sample𝐱\mathbf{x}from the posterior Eq.\eqrefeq:posterior, giving training pairs without any path-integral simulation. We use the single denoiser to examine isotope effects on the radial distribution functions (RDFs) of the O–O, O–H, and H–H pairs, on the intramolecular H–O–H angle, and, by opening the imaginary-time path of a tagged nucleus, on its end-to-end displacement and momentum distributions[17].Figure 3:Isotope effects and open-path observables in liquid water.
(a-c) Radial distribution functions of the O–O, O–H, and H–H pairs for H2O, D2O, and T2O at300​K300~\mathrm{K}withP=32P=32.
(d) Intramolecular H–O–H angle distribution for the same isotopes.
(e) Normalized radial end-to-end distributionP​(Δ)P(\Delta)of the opened imaginary-time path of a tagged nucleus for the same three liquids.
(f) Radial momentum distributionI​(p)I(p)of the tagged nucleus.
Solid: our method with a single denoiser. Dashed: PIMD reference, open-path PIMD in (e) and (f). Dotted: classical MD in (a-d).

Nuclear quantum effects broaden the distributions relative to classical MD, which is over-structured throughout (Fig.3). The effect is strongest on the light hydrogens and weakens with isotope mass. The O–H covalent peak sharpens from H2O to T2O (Fig.3(b), inset), the first H–H peak grows (Fig.3(c), inset), and the H–O–H angle distribution narrows (Fig.3(d)), while the O–O RDF is nearly isotope-independent (Fig.3(a)). Across all isotopes the single denoiser matches the PIMD reference.

The open-path observables probe the quantum delocalization directly. The radial end-to-end distribution narrows from H2O to T2O (Fig.3(e)), and the corresponding radial momentum distribution broadens and shifts to higher momentum (Fig.3(f)). The same denoiser, recomposed with the open-chain quadratic context, follows the open-path PIMD reference for all three isotopes.

## IVDiscussion

DPI partitions the path measure into an analytically known component and a learned component. The learned component is a single denoiser for the classical Boltzmann statistics, while temperature, isotopic mass, bath coupling, and the boundary conditions of the path enter through the analytic Gaussian step alone. Every demonstrated transfer is therefore the recomposition of a fixed denoiser with a different quadratic formKKunder the ceiling Eq.\eqrefeq:ceiling. The underlying structure is the graph invariance of the reverse conditional (End Matter). Once the residual and the noise model are fixed, every admissible quadratic context shares the same denoising posterior. The open-chain observables are the direct demonstration, the same denoiser yielding the end-to-end displacement and the momentum distribution once the edge closing the path of a tagged nucleus is deleted. A systematic wall-clock comparison is left to future work. Here we focus on the exactness and transferability of the construction.

Mathematically, our construction is a real Hubbard–Stratonovich (HS) transformation applied to the complement of the quantum coupling,σ−2​I−K\sigma^{-2}I-K, rather than to the confining coupling itself (End Matter). Our construction and the HS transformation share the same localizing step. Conditioned on the auxiliary variable, the coupled system factorizes into subsystems, each linked only to its own component of the auxiliary. They differ in which coupling is transferred and in what becomes of the localized subsystems. In many-body applications the interaction is the intractable element. The transformation moves it into the field, the localized particles become conditionally Gaussian and are integrated out, and the difficulty reappears in the non-Gaussian marginal of the field. In the path measure the roles are reversed. The Gaussian part is precisely the quantum content and is known in closed form, while the intractable residual is classical and local in imaginary time. The channel accordingly transfers the known coupling. Each bead is then linked to its own auxiliary component through a conditional that is classical and non-Gaussian, the object the denoiser represents, and nothing is integrated out. The marginal of the auxiliary path is never required.

The same construction admits a second understanding at each sweep. The denoiser removes the full training noise every time it is invoked, while the channel injects only part of it, withholding a share corresponding to the quantum coupling (End Matter, Eq.\eqrefeq:em_budget). The quantum context thus emerges from the “over-denoising” of the denoiser, and this leads to the ceiling in Eq.\eqrefeq:ceiling. This bound places GG-PI[34]outside the framework. GG-PI learns the conditional distribution of one bead given its two neighbors along the chain, which for the free ring polymer is Gaussian with varianceℏ2​τ/2​m\hbar^{2}\tau/2m, as the two adjacent springs contribute precision2​m/ℏ2​τ2m/\hbar^{2}\tau. This is twice the ceilingℏ2​τ/4​m\hbar^{2}\tau/4m. The noise that GG-PI removes is thus the quantum fluctuation itself and exceeds every admissible training noise for the context it targets. No channel of the form Eq.\eqrefeq:joint exists at that level, no share can be withheld, and the quantum context cannot be separated from the learned conditional.

Our construction rests on elementary Gaussian identities, yet it becomes practical only once the denoising posterior Eq.\eqrefeq:posterior admits an amortized model. Score-based and flow-based generative models have recently made such models accurate and inexpensive to evaluate[28,20]. Since the Gaussian step is analytic, the accuracy of the sampled ensemble is determined entirely by the learned conditional. The framework thereby both demands high-fidelity generative models and provides a natural benchmark for their design, and a Metropolis correction can in principle remove the residual bias (End Matter). More broadly, DPI and our earlier work[34,33]follow one recipe, in which a model trained on easily sampled statistics is amortized and then extended to a much harder target by an augmented Gibbs sampler that supplies the analytically known structure at sampling time. The same learned model is reused across contexts, a philosophy that is portable to problems well beyond nuclear quantum effects.

As in any Markov chain method, mixing sets the remaining cost. Each sweep displaces the configuration on the scale of the training noise, which the ceiling ties to the stiffest mode, so the chain advances by local moves and collective rearrangements decorrelate slowly. Replica exchange across a ladder of admissibleKKmatrices at fixed bead number, all sampled with the same denoiser, provides a natural remedy. Because every member of the family shares the residual, the swap acceptance involves only the analytic quadratic forms, the residual canceling identically (End Matter).

The latent-graph corollary (End Matter) indicates the natural next step. Bosonic exchange becomes an analytic update over the permutation graphs that runs alongside the unchanged denoiser[13], while fermionic signs remain outside the present framework[19]. Beyond the path integral, the complement construction offers a general route for decoupling confining quadratic forms. The conventional imaginary-field transformation achieves this at the price of oscillatory weights, whereas the complement admits a real auxiliary variable at the price of the ceiling and of a residual that must be learnable.

## Acknowledgments

This work was supported by National Institutes of Health award R35 GM136381 and completed with computational resources administered by the University of Chicago Research Computing Center, including Beagle-3, a shared GPU cluster for biomolecular sciences supported by the NIH under the High-End Instrumentation (HEI) grant program award 1S10OD028655-0. JW’s effort was supported by National Science Foundation award 2425899.

## References
- [1]A. O. Caldeira and A. J. Leggett(1983)Quantum tunnelling in a dissipative system.Ann. Phys.149(2),pp. 374–456.External Links:DocumentCited by:§I,§III.1.
- [2]D. M. Ceperley(1995)Path integrals in the theory of condensed helium.Rev. Mod. Phys.67(2),pp. 279–355.Cited by:§I.
- [3]M. Ceriotti, G. Bussi, and M. Parrinello(2009)Nuclear quantum effects in solids using a colored-noise thermostat.Phys. Rev. Lett.103(3),pp. 030603.Cited by:§I.
- [4]M. Ceriotti, M. Parrinello, T. E. Markland, and D. E. Manolopoulos(2010)Efficient stochastic thermostatting of path integral molecular dynamics.J. Chem. Phys.133(12),pp. 124104.Cited by:§I.
- [5]D. Chandler and P. G. Wolynes(1981)Exploiting the isomorphism between quantum theory and classical statistical mechanics of polyatomic fluids.J. Chem. Phys.74(7),pp. 4078–4095.Cited by:§I,§II.
- [6]R. T. Chen, Y. Rubanova, J. Bettencourt, and D. K. Duvenaud(2018)Neural ordinary differential equations.Adv. Neural Inf. Process. Syst.31.Cited by:§C.1.
- [7]C. Fan, M. Li, S. Yuan, Z. Xie, D. Chen, Y. I. Yang, and Y. Q. Gao(2025)Performing path integral molecular dynamics using an artificial intelligence-enhanced molecular simulation framework.J. Chem. Theory Comput.21(15),pp. 7279–7289.Cited by:§I.
- [8]G. H. Fredrickson, V. Ganesan, and F. Drolet(2002)Field-theoretic computer simulation methods for polymers and complex fluids.Macromolecules35(1),pp. 16–39.Cited by:Appendix B.
- [9]A. E. Gelfand(2000)Gibbs sampling.J. Am. Stat. Assoc.95(452),pp. 1300–1304.Cited by:§II.
- [10]S. Habershon, T. E. Markland, and D. E. Manolopoulos(2009)Competing quantum effects in the dynamics of a flexible water model.J. Chem. Phys.131(2),pp. 024501.Cited by:§III.3.
- [11]W. K. Hastings(1970)Monte carlo sampling methods using markov chains and their applications.Biometrika57(1),pp. 97–109.Cited by:§I.
- [12]M. F. Herman, E. J. Bruskin, and B. J. Berne(1982)On path integral Monte Carlo simulations.J. Chem. Phys.76(10),pp. 5150–5155.Cited by:§I,§II.
- [13]B. Hirshberg, V. Rizzi, and M. Parrinello(2019)Path integral molecular dynamics for bosons.Proc. Natl. Acad. Sci. U.S.A.116(43),pp. 21445–21449.Cited by:§IV.
- [14]R. A. Horn and C. R. Johnson(2012)Matrix analysis.Cambridge university press.Cited by:Appendix C.
- [15]X. Huang, B. J. Braams, and J. M. Bowman(2005)Ab initiopotential energy and dipole moment surfaces for H5O2+.J. Chem. Phys.122(4).Cited by:§III.2.
- [16]J. Hubbard(1959)Calculation of partition functions.Physical Review Letters3(2),pp. 77.Cited by:§I.
- [17]V. Kapil, A. Cuzzocrea, and M. Ceriotti(2018)Anisotropy of the proton momentum distribution in water.The Journal of Physical Chemistry B122(22),pp. 6048–6054.Cited by:Appendix C,§III.3.
- [18]C. Li and G. A. Voth(2022)Using machine learning to greatly accelerate path integral ab initio molecular dynamics.J. Chem. Theory Comput.18(2),pp. 599–604.Cited by:§I.
- [19]Z. Li and H. Yao(2019)Sign-problem-free fermionic quantum monte carlo: developments and applications.Annual Review of Condensed Matter Physics10(1),pp. 337–356.Cited by:§IV.
- [20]Y. Lipman, R. T. Q. Chen, H. Ben-Hamu, M. Nickel, and M. Le(2023)Flow matching for generative modeling.InInt. Conf. Learn. Represent.,Cited by:§C.1,§II,§II,§IV.
- [21]J. Liu, D. Li, and X. Liu(2016)A simple and accurate algorithm for path integral molecular dynamics with the Langevin thermostat.J. Chem. Phys.145(2),pp. 024103.Cited by:§I.
- [22]T. E. Markland and M. Ceriotti(2018)Nuclear quantum effects enter the mainstream.Nat. Rev. Chem.2(3),pp. 0109.Cited by:§I.
- [23]T. E. Markland and D. E. Manolopoulos(2008)An efficient ring polymer contraction scheme for imaginary time path integral simulations.J. Chem. Phys.129(2),pp. 024105.Cited by:§I.
- [24]T. Matsuo, Y. Natsume, and T. Kato(2008)Quantum-classical transition and decoherence in dissipative double-well potential systems: Monte Carlo algorithm.Phys. Rev. B77,pp. 184304.External Links:DocumentCited by:§I,§III.1,§III.1.
- [25]N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller(1953)Equation of state calculations by fast computing machines.J. Chem. Phys.21(6),pp. 1087–1092.Cited by:§I.
- [26]F. Musil, I. Zaporozhets, F. Noé, C. Clementi, and V. Kapil(2022)Quantum dynamics using path integral coarse-graining.J. Chem. Phys.157(18),pp. 181102.Cited by:§I.
- [27]M. R. Shirts and J. D. Chodera(2008)Statistically optimal analysis of samples from multiple equilibrium states.The Journal of chemical physics129(12).Cited by:§III.2.
- [28]Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole(2021)Score-based generative modeling through stochastic differential equations.InInt. Conf. Learn. Represent.,Cited by:§II,§IV.
- [29]R. L. Stratonovich(1957)A method for the. computation of quantum distribution functions.InDoklady Akademii Nauk,Vol.115,pp. 1097–1100.Cited by:§I.
- [30]K. Suzuki, M. Tachikawa, and M. Shiga(2013)Temperature dependence on the structure of Zundel cation and its isotopomers.J. Chem. Phys.138(18).Cited by:§III.2.
- [31]M. E. Tuckerman, B. J. Berne, G. J. Martyna, and M. L. Klein(1993)Efficient molecular dynamics and hybrid Monte Carlo algorithms for path integrals.J. Chem. Phys.99(4),pp. 2796–2808.Cited by:§I.
- [32]M. E. Tuckerman(2023)Statistical mechanics: theory and molecular simulation.Oxford university press.Cited by:§II.
- [33]W. Wang, J. Weare, and A. R. Dinner(2026)Composing diffusion priors with explicit physical context via generative gibbs sampling.arXiv preprint arXiv:2605.10642.Cited by:§IV.
- [34]W. Wang, X. Zhang, J. Weare, and A. R. Dinner(2026)Quantum statistics from classical simulations via generative gibbs sampling.arXiv preprint arXiv:2601.20228.Cited by:§I,§IV,§IV.
- [35]I. Zaporozhets, F. Musil, V. Kapil, and C. Clementi(2024)Accurate nuclear quantum statistics on machine-learned classical effective potentials.J. Chem. Phys.161(13),pp. 134102.Cited by:§I.

## Appendix ADerivation of the reverse conditional

LetA≡I−σ2​KA\equiv I-\sigma^{2}K, so that the channel in Eq.\eqrefeq:joint readsp​(𝐲∣𝐱)=𝒩​(𝐲;A​𝐱,σ2​A)p(\mathbf{y}\mid\mathbf{x})=\mathcal{N}(\mathbf{y};\,A\mathbf{x},\,\sigma^{2}A). Under the ceiling Eq.\eqrefeq:ceiling,AAis symmetric positive definite, soA−1A^{-1}exists. Sincep​(𝐱∣𝐲)∝π​(𝐱)​p​(𝐲∣𝐱)p(\mathbf{x}\mid\mathbf{y})\propto\pi(\mathbf{x})\,p(\mathbf{y}\mid\mathbf{x})at fixed𝐲\mathbf{y}, we track only the𝐱\mathbf{x}-dependence, andc​(𝐲)c(\mathbf{y})collects𝐱\mathbf{x}-independent terms and may change between lines. Using the symmetry ofAA, we expand the exponent of the Gaussian
channel as(𝐲−A​𝐱)⊤​A−1​(𝐲−A​𝐱)=𝐱⊤​A​𝐱−2​𝐲⊤​𝐱+𝐲⊤​A−1​𝐲.(\mathbf{y}-A\mathbf{x})^{\top}A^{-1}(\mathbf{y}-A\mathbf{x})=\mathbf{x}^{\top}\!A\,\mathbf{x}-2\,\mathbf{y}^{\top}\mathbf{x}+\mathbf{y}^{\top}\!A^{-1}\mathbf{y}.(6)

Substituting this expansion into the logarithm ofp​(𝐱∣𝐲)p(\mathbf{x}\mid\mathbf{y})gives{aligned}​log⁡p​(𝐱∣𝐲)=−𝐱⊤​A​𝐱−2​𝐲⊤​𝐱2​σ2−𝐱⊤​K​𝐱2−U​(𝐱)+c​(𝐲)=−\lVert​𝐱​\rVert2−2​𝐲⊤​𝐱2​σ2−U​(𝐱)+c​(𝐲)=−\lVert​𝐱−𝐲​\rVert22​σ2−U​(𝐱)+c​(𝐲),\aligned\log p(\mathbf{x}\mid\mathbf{y})&=-\frac{\mathbf{x}^{\top}\!A\mathbf{x}-2\,\mathbf{y}^{\top}\mathbf{x}}{2\sigma^{2}}-\frac{\mathbf{x}^{\top}K\mathbf{x}}{2}-U(\mathbf{x})+c(\mathbf{y})\\
&=-\frac{\lVert\mathbf{x}\rVert^{2}-2\,\mathbf{y}^{\top}\mathbf{x}}{2\sigma^{2}}-U(\mathbf{x})+c(\mathbf{y})\\
&=-\frac{\lVert\mathbf{x}-\mathbf{y}\rVert^{2}}{2\sigma^{2}}-U(\mathbf{x})+c(\mathbf{y}),(7)

usingA+σ2​K=IA+\sigma^{2}K=Iin the second line.

## Appendix BComplement Hubbard–Stratonovich transformation

For a symmetric positive-definite matrixBB, the Hubbard–Stratonovich (HS) identity readse12​𝐱⊤​B​𝐱=𝔼𝐳∼𝒩​(0,B)​[e𝐱⊤​𝐳],e^{\frac{1}{2}\mathbf{x}^{\top}B\,\mathbf{x}}=\mathbb{E}_{\mathbf{z}\sim\mathcal{N}(0,B)}\!\big[e^{\mathbf{x}^{\top}\mathbf{z}}\big],(8)

a Gaussian mixture of linear tilts whose covariance enters the exponent with a positive sign. However, the quadratic action of the path integral is confining,e−12​𝐱⊤​K​𝐱e^{-\frac{1}{2}\mathbf{x}^{\top}K\mathbf{x}}withK⪰0K\succeq 0, and decoupling it through Eq.\eqrefeq:em_hs requires an imaginary couplingi​𝐱⊤​𝐳i\,\mathbf{x}^{\top}\mathbf{z}. This produces oscillatory weights and underlies the sign problem of auxiliary-field methods[8].

The channel Eq.\eqrefeq:joint circumvents this obstruction by transforming the complement of the coupling within the training noise. Writing{aligned}​e−12​𝐱⊤​K​𝐱=e−\lVert​𝐱​\rVert22​σ2​e+12​𝐱⊤​B​𝐱,B=σ−2​I−K,\aligned e^{-\frac{1}{2}\mathbf{x}^{\top}K\mathbf{x}}&=e^{-\frac{\lVert\mathbf{x}\rVert^{2}}{2\sigma^{2}}}\,e^{+\frac{1}{2}\mathbf{x}^{\top}B\,\mathbf{x}},\\
B&=\sigma^{-2}I-K,(9)

the complementBBis positive definite exactly under the ceiling Eq.\eqrefeq:ceiling. Applying Eq.\eqrefeq:em_hs toBBleads to the joint distributionp​(𝐱,𝐳)∝exp⁡[−\lVert​𝐱​\rVert22​σ2+𝐱⊤​𝐳−U​(𝐱)−\tfrac​12​𝐳⊤​B−1​𝐳],p(\mathbf{x},\mathbf{z})\propto\exp\!\Big[-\frac{\lVert\mathbf{x}\rVert^{2}}{2\sigma^{2}}+\mathbf{x}^{\top}\mathbf{z}-U(\mathbf{x})-\tfrac 12\,\mathbf{z}^{\top}B^{-1}\mathbf{z}\Big],(10)

whose𝐳\mathbf{z}-marginal recoversπ​(𝐱)\pi(\mathbf{x})by Eq.\eqrefeq:em_hs. In the rescaled variable𝐲=σ2​𝐳\mathbf{y}=\sigma^{2}\mathbf{z}the joint becomesp​(𝐱,𝐲)∝exp⁡[−\lVert​𝐱​\rVert2−2​𝐱⊤​𝐲2​σ2−U​(𝐱)−\tfrac​12​𝐲⊤​Σ−1​𝐲],p(\mathbf{x},\mathbf{y})\propto\exp\!\Big[-\frac{\lVert\mathbf{x}\rVert^{2}-2\,\mathbf{x}^{\top}\mathbf{y}}{2\sigma^{2}}-U(\mathbf{x})-\tfrac 12\,\mathbf{y}^{\top}\Sigma^{-1}\mathbf{y}\Big],(11)

withΣ=σ4​B=σ2​(I−σ2​K)\Sigma=\sigma^{4}B=\sigma^{2}(I-\sigma^{2}K). Completing the square in𝐲\mathbf{y}at fixed𝐱\mathbf{x}, and in𝐱\mathbf{x}at fixed𝐲\mathbf{y}, shows that the two conditionals of Eq.\eqrefeq:em_yjoint are exactly the channel Eq.\eqrefeq:joint and the posterior Eq.\eqrefeq:posterior. The construction of the main text is therefore a real HS transformation applied to the complement of the quantum coupling.

This construction has an operational reading. In the absence of quadratic context,K=0K=0, the channel injects the full training noise,𝐲∼𝒩​(𝐱,σ2​I)\mathbf{y}\sim\mathcal{N}(\mathbf{x},\sigma^{2}I), so each sweep corrupts the configuration with exactly the noise the denoiser was trained to remove, and the loop leaves the classical product distributione−Ue^{-U}invariant. A nonzero quantum context contracts the channel mean byI−σ2​KI-\sigma^{2}Kand withholds the matching share of the training noiseσ2​(I−σ2​K)⏟injected+σ4​K⏟withheld=σ2​I⏟training noise.\underbrace{\sigma^{2}\big(I-\sigma^{2}K\big)}_{\text{injected}}\;+\;\underbrace{\sigma^{4}K}_{\text{withheld}}\;=\;\underbrace{\sigma^{2}I}_{\text{training noise}}.(12)

The denoiser removes the full training noise in every sweep, while the channel injects only the remainder. This deficit, which encodes the chosen quantum coupling, turns the stationary distribution from the classical producte−Ue^{-U}into the path measureπ\pi. Because the injected covariance cannot be negative, the withheld share can never exceed the training noise; this constraint is the ceiling Eq.\eqrefeq:ceiling.

## Appendix CGraph-invariant denoising decomposition

The main-text construction is one instance of a decomposition defined on a family of graphs. LetG=(V,E)G=(V,E)be a graph whose vertices carry the configurations𝐱=(𝐱1,…,𝐱B)\mathbf{x}=(\mathbf{x}_{1},\dots,\mathbf{x}_{B}). Each vertex𝐱b\mathbf{x}_{b}is the unit on which the denoiser acts, and the edges encode analytically known quadratic couplings. The target distribution associated withGGisπG​(𝐱)∝exp⁡[−\tfrac​12​𝐱⊤​KG​𝐱]​exp⁡[−U​(𝐱)],\pi_{G}(\mathbf{x})\propto\exp\!\Big[-\tfrac 12\,\mathbf{x}^{\top}K_{G}\,\mathbf{x}\Big]\exp[-U(\mathbf{x})],(13)

whereKG=KG⊤⪰0K_{G}=K_{G}^{\top}\succeq 0is the quadratic context that collects the edge couplings and any on-site terms,\tfrac​12​𝐱⊤​KG​𝐱=∑(b,b′)∈E\tfrac​12​kb​b′​\lVert​𝐱b−𝐱b′​\rVert2+\tfrac​12​𝐱⊤​K(2)​𝐱,\tfrac 12\,\mathbf{x}^{\top}K_{G}\,\mathbf{x}=\sum_{(b,b^{\prime})\in E}\tfrac 12\,k_{bb^{\prime}}\lVert\mathbf{x}_{b}-\mathbf{x}_{b^{\prime}}\rVert^{2}+\tfrac 12\,\mathbf{x}^{\top}K^{(2)}\mathbf{x},(14)

withkb​b′k_{bb^{\prime}}the stiffness of edge(b,b′)(b,b^{\prime})andK(2)K^{(2)}any remaining analytically known contribution, such as a harmonic restraint or a nonlocal bath kernel. Throughout,GGdenotes the complete graph-structured quadratic context, comprising the connectivity, the edge weights, the on-site terms, and the number of vertices. A linear term in the action would require a corresponding shift of the channel mean, and we omit it for simplicity.

Fix a residualUUand a noise matrixR=diag​(R1,…,RB)R=\mathrm{diag}(R_{1},\dots,R_{B}), which is block-diagonal with one blockRb≻0R_{b}\succ 0per vertex, both shared by every member of a family𝒢\mathcal{G}of such contexts. For eachGGthe auxiliary configuration𝐲=(𝐲1,…,𝐲B)\mathbf{y}=(\mathbf{y}_{1},\dots,\mathbf{y}_{B})is drawn from the channelp​(𝐲∣𝐱,G)=𝒩​(𝐲;(I−R​KG)​𝐱,R−R​KG​R),p(\mathbf{y}\mid\mathbf{x},G)=\mathcal{N}\!\big(\mathbf{y};\,(I-RK_{G})\mathbf{x},\;R-RK_{G}R\big),(15)

which reduces to Eq.\eqrefeq:joint forR=σ2​IR=\sigma^{2}I. The channel is a valid distribution whenR−R​KG​R≻0R-RK_{G}R\succ 0, equivalentlyλmax​(R1/2​KG​R1/2)<1,\lambda_{\max}\!\big(R^{1/2}K_{G}R^{1/2}\big)<1,(16)

which recoversσ2<λmax​(KG)−1\sigma^{2}<\lambda_{\max}(K_{G})^{-1}in the isotropic case. Since the channel is normalized, integrating out𝐲\mathbf{y}returnsπG\pi_{G}for everyGG, so the augmentation is exact by construction.

Proposition (graph-invariant reverse conditional).Let the residualUUbe independent of the graphGG, let the noise matrixRRbe common to every member of𝒢\mathcal{G}, and let the ceiling Eq.\eqrefeq:em_ceiling hold for everyG∈𝒢G\in\mathcal{G}. Then for everyG∈𝒢G\in\mathcal{G}, the conditional distribution of𝐱\mathbf{x}given𝐲\mathbf{y}under the jointπG​(𝐱)​p​(𝐲∣𝐱,G)\pi_{G}(\mathbf{x})\,p(\mathbf{y}\mid\mathbf{x},G)isp​(𝐱∣𝐲)∝exp⁡[−\tfrac​12​(𝐱−𝐲)⊤​R−1​(𝐱−𝐲)−U​(𝐱)],p(\mathbf{x}\mid\mathbf{y})\propto\exp\!\Big[-\tfrac 12(\mathbf{x}-\mathbf{y})^{\top}R^{-1}(\mathbf{x}-\mathbf{y})-U(\mathbf{x})\Big],(17)

independent ofGG. A single denoiser trained for Eq.\eqrefeq:em_posterior therefore serves the entire family, whose members differ only through their analytic channels Eq.\eqrefeq:em_channel. The proof repeats the completion of the square in Eqs.\eqrefeq:em_expand and\eqrefeq:em_square withA=I−R​KGA=I-RK_{G}; the channel mean and covariance share the factorAA, soKGK_{G}cancels.

WhenUUseparates over the vertices,U​(𝐱)=∑bUb​(𝐱b)U(\mathbf{x})=\sum_{b}U_{b}(\mathbf{x}_{b}), the block-diagonal structure ofRRfactorizes the posterior,{gathered}​p​(𝐱∣𝐲)=∏b=1Bpb​(𝐱b∣𝐲b),pb∝exp⁡[−\tfrac​12​(𝐱b−𝐲b)⊤​Rb−1​(𝐱b−𝐲b)−Ub​(𝐱b)].\gathered p(\mathbf{x}\mid\mathbf{y})=\prod_{b=1}^{B}p_{b}(\mathbf{x}_{b}\mid\mathbf{y}_{b}),\\
p_{b}\propto\exp\!\Big[-\tfrac 12(\mathbf{x}_{b}-\mathbf{y}_{b})^{\top}R_{b}^{-1}(\mathbf{x}_{b}-\mathbf{y}_{b})-U_{b}(\mathbf{x}_{b})\Big].(18)

Eachpbp_{b}is the denoising posterior of a single vertex drawn frome−Ube^{-U_{b}}and corrupted with covarianceRbR_{b}. Members of𝒢\mathcal{G}may also differ in size. A change of temperature at fixedτ\tauchanges the number of vertices, and the invariant object is then the single-vertex conditionalpbp_{b}, reused across vertex counts.

Training pairs may be generated from any convenient member of the family. At one extreme,KG=0K_{G}=0reduces sampling to standard MD followed by Gaussian corruption; at the other, the analytic channel converts existing PIMD/PIMC paths at the sameτ\tauinto vertex pairs. Alternatively, restrained MD samplespb​(𝐱b∣𝐲b)p_{b}(\mathbf{x}_{b}\mid\mathbf{y}_{b})directly. Although the marginal of𝐲b\mathbf{y}_{b}does not change the target conditional, its coverage affects denoiser accuracy in practice.

The uniform ceiling is often inherited automatically. Deleting an edge(b,b′)(b,b^{\prime})subtracts the positive-semidefinite harmonic term\tfrac​12​kb​b′​\lVert​𝐱b−𝐱b′​\rVert2\tfrac 12\,k_{bb^{\prime}}\lVert\mathbf{x}_{b}-\mathbf{x}_{b^{\prime}}\rVert^{2}from Eq.\eqrefeq:em_KG, which lowers the context matrix in the Loewner partial order,KG′⪯KGK_{G^{\prime}}\preceq K_{G}. Because congruence preserves this order and the largest eigenvalue is monotonic on it[14], it follows thatλmax​(R1/2​KG′​R1/2)≤λmax​(R1/2​KG​R1/2)\lambda_{\max}\!\big(R^{1/2}K_{G^{\prime}}R^{1/2}\big)\leq\lambda_{\max}\!\big(R^{1/2}K_{G}R^{1/2}\big). In physical terms, removing a spring can only soften the system; in mathematical terms, every subgraph of an admissible graph remains strictly admissible at the same noise level.

Corollary (latent graph).Let the graph itself be a random variable with nonnegative weightsp​(G)p(G)and unnormalized joint densityp​(𝐱,G)∝p​(G)​exp⁡[−\tfrac​12​𝐱⊤​KG​𝐱−U​(𝐱)],p(\mathbf{x},G)\propto p(G)\,\exp\!\Big[-\tfrac 12\,\mathbf{x}^{\top}K_{G}\,\mathbf{x}-U(\mathbf{x})\Big],(19)

normalized over𝐱\mathbf{x}andGGtogether. Let Eq.\eqrefeq:em_ceiling hold for everyGGin the support ofp​(G)p(G). Augmenting each graph with its channelp​(𝐱,𝐲,G)=p​(𝐱,G)​p​(𝐲∣𝐱,G),p(\mathbf{x},\mathbf{y},G)=p(\mathbf{x},G)\,p(\mathbf{y}\mid\mathbf{x},G),(20)

and completing the square as above separates𝐱\mathbf{x}fromGG,{aligned}p(𝐱,𝐲,G)∝f(𝐱,𝐲)h(𝐲,G),f(𝐱,𝐲)=exp[−\tfrac12(𝐱−𝐲)⊤R−1(𝐱−𝐲)−U(𝐱)],h(𝐲,G)=p(G)det(I−KGR)−1/2⋅e−12​𝐲⊤​(I−KG​R)−1​KG​𝐲.\aligned p(\mathbf{x},\mathbf{y},G)&\propto f(\mathbf{x},\mathbf{y})\,h(\mathbf{y},G),\\
f(\mathbf{x},\mathbf{y})&=\exp\!\Big[-\tfrac 12(\mathbf{x}-\mathbf{y})^{\top}R^{-1}(\mathbf{x}-\mathbf{y})-U(\mathbf{x})\Big],\\
h(\mathbf{y},G)&=p(G)\,{\det}(I-K_{G}R)^{-1/2}\\
&\quad\cdot\,e^{-\frac{1}{2}\,\mathbf{y}^{\top}(I-K_{G}R)^{-1}K_{G}\,\mathbf{y}}.(21)

Hence𝐱⟂G∣𝐲\mathbf{x}\perp G\mid\mathbf{y}, andp​(𝐱,G∣𝐲)=p​(𝐱∣𝐲)​p​(G∣𝐲)p(\mathbf{x},G\mid\mathbf{y})=p(\mathbf{x}\mid\mathbf{y})\,p(G\mid\mathbf{y})withp​(G∣𝐲)∝h​(𝐲,G)p(G\mid\mathbf{y})\propto h(\mathbf{y},G). Given the auxiliary configuration𝐲\mathbf{y}, the configuration update through the graph-blind denoiser and the graph update throughp​(G∣𝐲)p(G\mid\mathbf{y})therefore proceed independently and in parallel. The auxiliary configuration screens the physical coordinates from the quadratic context entirely.

In the path integral of the main text, each vertex carries one replica𝐱b≡𝐱k∈ℝd​N\mathbf{x}_{b}\equiv\mathbf{x}_{k}\in\mathbb{R}^{dN}withUb=τ​V​(𝐱k)U_{b}=\tau V(\mathbf{x}_{k}), andGGis the imaginary-time graph of the ring polymer, with a Gaussian bath entering as additional nonlocal edges. Within each transfer family, the noise matrixRbR_{b}is fixed once and shared by all contexts; only the quadratic contextKGK_{G}changes. Opening the imaginary-time path of a tagged atom deletes the edge that closes its cycle. We adopt the factorization of Ref.[17], in which every bead retains the residual weightτ​V\tau V, soUUis common to the open and the closed graph, the proposition applies, and the ceiling is inherited by the monotonicity above.

Bosonic exchange assigns uniform weightsp​(G)p(G)to the permutation graphs that reconnect the imaginary-time endpoints, and the corollary reduces its sampling to the analytic updatep​(G∣𝐲)∝h​(𝐲,G)p(G\mid\mathbf{y})\propto h(\mathbf{y},G)of Eq.\eqrefeq:em_fh
alongside the unchanged denoiser. In principle, the same denoiser combined with this permutation update therefore samples bosonic systems. Fermionic weights carry signs, outside the present hypotheses, and are left to future work.

## C.1Conditional normalizing flow

We realize each single-vertex posteriorpb​(𝐱b∣𝐲b)p_{b}(\mathbf{x}_{b}\mid\mathbf{y}_{b})of Eq.\eqrefeq:em_factor with a conditional continuous normalizing flow (CNF) trained by flow matching[20,6]. Conditioned on𝐲b\mathbf{y}_{b}, the model transports a Gaussian base sample𝐱0∼𝒩​(𝐲b,Rb)\mathbf{x}^{0}\sim\mathcal{N}(\mathbf{y}_{b},R_{b})to a target sample𝐱1∼pb​(𝐱b∣𝐲b)\mathbf{x}^{1}\sim p_{b}(\mathbf{x}_{b}\mid\mathbf{y}_{b})alongs∈[0,1]s\in[0,1]through the ODEd​𝐱sd​s=vθ​(𝐱s,𝐲b,s),𝐱s=0=𝐱0.\frac{d\mathbf{x}^{s}}{ds}=v_{\theta}(\mathbf{x}^{s},\mathbf{y}_{b},s),\qquad\mathbf{x}^{s=0}=\mathbf{x}^{0}.(22)

The conditional is equivariant under simultaneous rigid transformations of the sample and conditioning configuration. We construct the velocity field from relative coordinates so that, forQ∈O​(3)Q\in O(3)and𝐭∈ℝ3\mathbf{t}\in\mathbb{R}^{3},vθ​(Q​𝐱+𝐭,Q​𝐲b+𝐭,s)=Q​vθ​(𝐱,𝐲b,s).v_{\theta}(Q\mathbf{x}+\mathbf{t},Q\mathbf{y}_{b}+\mathbf{t},s)=Q\,v_{\theta}(\mathbf{x},\mathbf{y}_{b},s).(23)

Because the Gaussian base is centered at𝐲b\mathbf{y}_{b}, translating𝐲b\mathbf{y}_{b}translates the initial condition and the entire ODE trajectory by the same𝐭\mathbf{t}.
A lightweight network suffices, as the base is already centered at𝐲b\mathbf{y}_{b}and localized byRbR_{b}. The velocity is trained by the conditional flow-matching loss{aligned}​ℒ​(θ)=𝔼s,(𝐱0,𝐱1)​\lVert​vθ​((1−s)​𝐱0+s​𝐱1,𝐲b,s)−(𝐱1−𝐱0)​\rVert2,\aligned\mathcal{L}(\theta)&=\mathbb{E}_{s,\,(\mathbf{x}^{0},\mathbf{x}^{1})}\big\lVert v_{\theta}\big((1-s)\mathbf{x}^{0}+s\mathbf{x}^{1},\,\mathbf{y}_{b},\,s\big)\\
&\qquad-(\mathbf{x}^{1}-\mathbf{x}^{0})\big\rVert^{2},(24)

withs∼𝒰​[0,1]s\sim\mathcal{U}[0,1].

## C.2Flow likelihood and Metropolis-Hastings correction

The conditional flow has an exact likelihood. Integrating the instantaneous change of variables along the ODE giveslog⁡qθ​(𝐱b∣𝐲b)=log⁡𝒩​(𝐱0;𝐲b,Rb)−∫01∇⋅vθ​(𝐱s,𝐲b,s)​𝑑s,\log q_{\theta}(\mathbf{x}_{b}\mid\mathbf{y}_{b})=\log\mathcal{N}(\mathbf{x}^{0};\,\mathbf{y}_{b},R_{b})-\int_{0}^{1}\nabla\!\cdot v_{\theta}(\mathbf{x}^{s},\mathbf{y}_{b},s)\,ds,(25)

where𝐱0\mathbf{x}^{0}is obtained by integrating the ODE backward from𝐱b\mathbf{x}_{b}. An independence Metropolis–Hastings step then removes the residual bias of the learned conditional. A proposal𝐱b′∼qθ(⋅∣𝐲b)\mathbf{x}_{b}^{\prime}\sim q_{\theta}(\cdot\mid\mathbf{y}_{b})is accepted with probabilityα=min⁡{1,p~b​(𝐱b′∣𝐲b)​qθ​(𝐱b∣𝐲b)p~b​(𝐱b∣𝐲b)​qθ​(𝐱b′∣𝐲b)},\alpha=\min\!\left\{1,\;\frac{\tilde{p}_{b}(\mathbf{x}_{b}^{\prime}\mid\mathbf{y}_{b})\,q_{\theta}(\mathbf{x}_{b}\mid\mathbf{y}_{b})}{\tilde{p}_{b}(\mathbf{x}_{b}\mid\mathbf{y}_{b})\,q_{\theta}(\mathbf{x}_{b}^{\prime}\mid\mathbf{y}_{b})}\right\},(26)

withp~b\tilde{p}_{b}the unnormalized posterior. This can remove the error in the learned conditional at the price of extra potential evaluations per proposal. The reported results do not employ the correction.

## C.3Replica exchange

By thegraph-invariant proposition, many ensembles can share the same denoiser with differentKK. Suppose two ensemblesπi\pi_{i}andπj\pi_{j}have the same residualUUbut different quadratic contextsKiK_{i}andKjK_{j}. Exchanging their configurations is accepted with probabilitymin⁡(1,eΔi​j)\min(1,e^{\Delta_{ij}}), whereΔi​j=\tfrac​12​(𝐱i⊤​Ki​𝐱i+𝐱j⊤​Kj​𝐱j−𝐱i⊤​Kj​𝐱i−𝐱j⊤​Ki​𝐱j),\Delta_{ij}=\tfrac 12\big(\mathbf{x}_{i}^{\top}K_{i}\mathbf{x}_{i}+\mathbf{x}_{j}^{\top}K_{j}\mathbf{x}_{j}-\mathbf{x}_{i}^{\top}K_{j}\mathbf{x}_{i}-\mathbf{x}_{j}^{\top}K_{i}\mathbf{x}_{j}\big),(27)

in whichUUhas cancelled identically. The acceptance involves only the analytic quadratic forms. This provides a way to exchange across mass ladders to accelerate the mixing. Exchange across temperature changes the bead number and is not of this form.

## 


- 


Major funding support from
