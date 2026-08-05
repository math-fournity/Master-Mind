# Emergent Self-Attention from Astrocyte-Gated Associative Memory Dynamics

**arXiv ID**: 2604.25481v1
**Authors**: Arnau Vivet, Alex Arenas
**Published**: 2026-04-28
**Categories**: physics.data-an, cs.LG, nlin.AO, physics.soc-ph
**Comments**: 11 pages, 4 figures
**HTML URL**: https://arxiv.org/html/2604.25481v1

## Abstract

We introduce a Hopfield-type associative memory in which effective connectivity is multiplicatively modulated by astrocytic gains evolving under an entropy-regularized replicator equation. The coupled neuron-astrocyte dynamics admit a Lyapunov function, ensuring global convergence. At fixed points, astrocytic gains implement a softmax-normalized allocation over pattern similarity scores, yielding a mechanistic realization of self-attention as emergent routing on the gain simplex. In regimes of high memory load and interference, the model significantly improves retrieval accuracy relative to classical Hopfield dynamics and recent neuron-astrocyte baselines. These results establish a dynamical systems framework linking glial modulation, competitive resource allocation, and attention-like computation.

## Full Text

Emergent Self-Attention from Astrocyte-Gated Associative Memory Dynamics

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
- License: CC BY 4.0arXiv:2604.25481v1 [physics.data-an] 28 Apr 2026

## Emergent Self-Attention from Astrocyte-Gated Associative Memory DynamicsArnau VivetDepartament d’Enginyeria Informàtica i Matemàtiques, Universitat Rovira i Virgili, 43007 Tarragona, SpainAlex ArenasDepartament d’Enginyeria Informàtica i Matemàtiques, Universitat Rovira i Virgili, 43007 Tarragona, SpainComplexity Science Hub Vienna, Metternichgasse 8, 1030 Vienna, Austria

## Abstract

We introduce a Hopfield-type associative memory in which effective connectivity is multiplicatively modulated by astrocytic gains evolving under an entropy-regularized replicator equation. The coupled neuron–astrocyte dynamics admit a Lyapunov function, ensuring global convergence. At fixed points, astrocytic gains implement a softmax-normalized allocation over pattern similarity scores, yielding a mechanistic realization of self-attention as emergent routing on the gain simplex. In regimes of high memory load and interference, the model significantly improves retrieval accuracy relative to classical Hopfield dynamics and recent neuron–astrocyte baselines. These results establish a dynamical systems framework linking glial modulation, competitive resource allocation, and attention-like computation.

## IIntroduction

Hopfield networks revolutionized our understanding of how collective neuronal dynamics implement
associative memory with biological plausibility[1]. In their original formulation,
neurons evolve under Hebbian connectivity that stores a finite set of patterns as energy minima.
Although this framework provided a foundational bridge between statistical physics and neural
computation, its practical applicability was limited by low storage capacity and the proliferation
of spurious attractors under high pattern load or correlation[2].

Interest resurged with generalized energy-based formulations, dense associative memory and modern
Hopfield networks, that replace the quadratic Hebbian energy with higher-order or exponential
interaction terms, dramatically expanding capacity and retrieval stability[3,4]. A key insight from this line of work is that the fixed-point
readout of modern Hopfield networks is mathematically equivalent to the scaled dot-product attention
mechanism at the core of Transformer architectures[5,6]. This
correspondence has reframed associative memory dynamics as a candidate substrate for attention and
contextual reasoning in both artificial and biological systems.

Neuroscience has concurrently revealed that the brain’s computational resources extend well beyond
neurons. Astrocytes, glial cells long considered purely supportive, actively regulate synaptic
transmission, integrate signals across local microcircuits, and contribute to memory-related
plasticity[7,8,9,10,11,12].
Through Ca2+signaling, neurotransmitter uptake, and connexin-mediated gap-junction coupling,
astrocytes modulate neuronal excitability and impose structured heterogeneity in effective synaptic
strengths[9,11,12].
Astrocytes have also been implicated in controlling circuit-level dynamical regimes, including the modulation of gamma-band synchronization associated with memory processing[13,14,15].
Critically, astrocytes are now
recognized as active participants in memory encoding and consolidation: recent experimental work
demonstrates that astrocyte ensembles selectively encode and stabilize salient experiences, with
individual astrocytes reactivated during memory retrieval undergoing noradrenaline-dependent molecular
tagging that promotes consolidation of specific traces[16,17].
These findings extend the classical engram framework[18]by assigning
astrocytes a mechanistic role in the selection and stabilization of memory representations, motivating
their inclusion in computational models of associative memory.

Building on this foundation, recent theoretical work has proposed that astrocytic modulation could
implement attention-like computation by providing a flexible, content-dependent reweighting of
neuronal ensembles during retrieval[19,20]. In this view, self-attention corresponds to a gain reallocation
across stored patterns driven by their relevance to the current query state. However, a precise
dynamical account of how softmax-normalized gains arise as an emergent, self-organized property of
neuron–astrocyte interaction, rather than being imposed by architectural design, has remained
absent.

Here we close this gap by introducing a Hopfield-type associative memory in which effective
connectivity is multiplicatively modulated by astrocytic gains that evolve on the probability simplex
under an entropy-regularized replicator equation. The coupled neuron–astrocyte system admits a
Lyapunov function, ensuring convergence to stationary points (equilibria) at which gains implement a
Gibbs–Boltzmann (softmax) allocation over pattern similarity scores. The stationary readout is thus
a convex combination of stored patterns with self-attention weights—emerging purely from the
competitive resource dynamics of glial modulation, without any explicit attention mechanism being
prescribed. Under high memory load and pattern interference, this mechanism substantially improves
retrieval accuracy relative to classical Hopfield dynamics and recent neuron–astrocyte baselines,
establishing a dynamical systems framework that links glial gain control, competitive resource
allocation, and the emergence of attention-like computation in neural circuits.

## IIAstrocyte-Gated Associative Memory

To ground the proposed astrocyte-neuron model, we begin by recalling the continuous-time classical Hopfield network, the minimal framework for associative memory. It is a class of recurrent neural network in which we consider a population of rate-based neurons evolving under a fully connected synaptic matrix. One of the key properties of this framework is that it can be derived from a Lyapunov function that guarantees convergence, enabling a precise characterization of memory retrieval as well as interference and capacity limits[1,2]. For these reasons, the Hopfield model provides a natural substrate on which biologically motivated extensions can be constructed.
More precisely, we considerNNrate unitsx​(t)∈ℝNx(t)\in\mathbb{R}^{N}with element-wise activation functionϕ​(x)=tanh⁡(σ​x)∈(−1,1)N\phi(x)=\tanh(\sigma x)\in(-1,1)^{N}and synaptic weightsW∈ℝN×NW\in\mathbb{R}^{N\times N}:τx​x˙i=−xi+∑jWi​j​ϕ​(xj).\tau_{x}\dot{x}^{i}=-x^{i}+\sum_{j}W^{ij}\,\phi(x^{j}).(1)

whereτx\tau_{x}is the neuronal rate time constant. It sets the intrinsic timescale over which the firing-rate statex​(t)x(t)relaxes toward the driveW​ϕ​(x)W\,\phi(x)against the leak term. The synaptic matrixWWis constructed using Hebbian storage ofKKbinary patternsξμ∈{−1,1}N\xi_{\mu}\in\{-1,1\}^{N}located at the vertices of the hypercubeWH=1N​∑μ=1Kξμi​ξμj.W_{H}=\frac{1}{N}\sum_{\mu=1}^{K}\xi_{\mu}^{i}\xi_{\mu}^{j}.(2)

Alternatively in matrix form we haveWH=1N​Ξ​Ξ⊺W_{H}=\frac{1}{N}\Xi\Xi^{\intercal}, whereΞ≡(ξ1,…,ξK)∈{−1,1}N×K\Xi\equiv(\xi_{1},...,\xi_{K})\in\{-1,1\}^{N\times K}is a binary matrix where patterns are stored as columns. Throughout the paper, we use superscripts to label neurons and subscripts to label memory patterns.

## II.1Astrocyte-gated retrieval as pattern-wise gain control

We extend the classical Hopfield rate dynamics by introducingKKastrocytic gain variablesp=(p1,…,pK)p=(p_{1},\dots,p_{K})that modulate the contribution of each stored pattern to the synaptic matrix. The gains are constrained to the probability simplex,pμ≥0(∀μ),∑μ=1Kpμ=1,p_{\mu}\geq 0\quad(\forall\mu),\qquad\sum_{\mu=1}^{K}p_{\mu}=1,(3)

so modulation is non-negative and globally conserved. The resulting neuronal dynamics readτx​x˙i\displaystyle\tau_{x}\dot{x}^{i}=−xi+∑j=1NWi​j​(p)​ϕ​(xj),\displaystyle=-x^{i}+\sum_{j=1}^{N}W^{ij}(p)\,\phi(x^{j}),(4)

with effective synaptic matrixW​(p)≡KN​∑μ=1Kpμ​ξμ​ξμ⊺=KN​Ξ​diag​(p)​Ξ⊺.W(p)\equiv\frac{K}{N}\sum_{\mu=1}^{K}p_{\mu}\,\xi_{\mu}\xi_{\mu}^{\intercal}=\frac{K}{N}\,\Xi\,\mathrm{diag}(p)\,\Xi^{\intercal}.(5)

Thus,pμp_{\mu}acts as a multiplicative gain on theμ\mu-th Hebbian outer product. The classical Hopfield coupling is recovered for uniform gainspμ=1/Kp_{\mu}=1/K, for whichW​(p)=WHW(p)=W_{H}.

We model astrocytic modulation as an adaptive allocation process governed by a softmax-regularized replicator flow (hereafter “s-replicator”):τp​p˙μ\displaystyle\tau_{p}\dot{p}_{\mu}=pμ​(Fμ−∑ν=1Kpν​Fν),\displaystyle=p_{\mu}\Big(F_{\mu}-\sum_{\nu=1}^{K}p_{\nu}F_{\nu}\Big),(6)

which preserves the simplex constraints. The fitness is defined asFμ≡fμ−T​log⁡pμ,T>0,F_{\mu}\equiv f_{\mu}-T\log p_{\mu},\qquad T>0,(7)

wherefμ≡12​N​(∑j=1Nξμj​ϕ​(xj))2f_{\mu}\equiv\frac{1}{2N}\Big(\sum_{j=1}^{N}\xi_{\mu}^{j}\phi(x^{j})\Big)^{2}(8)

is the squared overlap with patternμ\mu, and the logarithmic term acts as an entropic (temperature-like) regularizer that discourages collapse of the gains onto a single pattern. Throughout, we use the same neuronal nonlinearity as in the classical model,ϕ​(xj)=tanh⁡(σ​xj)\phi(x^{j})=\tanh(\sigma x^{j})withσ>0\sigma>0.

We study retrieval dynamics by initializing the neuronal statex​(0)x(0)as a corrupted version of one of the stored patterns. Unless stated otherwise, the astrocytic gains are initialized uniformly,pμ​(0)=1/Kp_{\mu}(0)=1/Kfor allμ\mu. During the dynamics, Eq. (6) reallocates gain toward patterns with larger instantaneous overlapfμ​(x)f_{\mu}(x), thereby reshaping the effective couplingW​(p)W(p)in Eq. (5). This positive feedback selectively amplifies the synaptic contribution of the most compatible patterns and suppresses competing ones, reducing interference and effectively increasing the basin of attraction of the target memory.

The biophysical motivation for Eqs. (4,6) is the following. We view each stored pattern as an engram-like neuronal ensemble, and interpret the gainpμp_{\mu}as an effective proxy for astrocyte-mediated modulation of the synaptic pathways supporting that ensemble. Specifically,pμp_{\mu}summarizes (at a coarse-grained level) how local astrocytic activity can bias presynaptic release probability and thus rescale the effective strength of the synapses recruited by patternμ\mu. This abstraction is inspired by evidence that synaptic activity can evoke highly localized astrocytic Ca2+signals in perisynaptic microdomains adjacent to individual synapses[21]. In several experimental settings, astrocytic Ca2+elevations have been reported to modulate presynaptic release probability and thereby reshape effective synaptic transmission, consistent with an activity-dependent astrocytic gating of synaptic pathways[22]. At the same time, the extent to which Ca2+-dependent astrocytic signaling modulates excitatory transmission and plasticity under baseline conditions remains debated and depends on preparation and stimulation regime[23]; accordingly, we treatpμp_{\mu}as a phenomenological variable that aggregates multiple microscopic mechanisms rather than as a direct readout of any single molecular process.

Finally, we constrain the astrocytic gains to the simplex,p∈ΔK−1p\in\Delta^{K-1}, i.e.,pμ≥0p_{\mu}\geq 0and∑μ=1Kpμ=1\sum_{\mu=1}^{K}p_{\mu}=1. In the model, this implements a finite modulatory capacity: increasing gain for one pattern necessarily reduces the gain available to others, thereby enforcing competitive allocation across pathways. This is a deliberate modeling device that operationalizes resource limitation and homeostatic competition at the level of pattern gains, rather than a claim that the brain explicitly maintains a globally conserved scalar “budget”[24].

The neuron–astrocyte coupling is driven by a pattern-match functionalfμ​(x)f_{\mu}(x), which quantifies how strongly the current neuronal state expresses patternμ\mu(via its overlap withξμ\xi_{\mu}). We map this match to a fitnessFμF_{\mu}that controls the gain dynamics: patterns with largerFμF_{\mu}are preferentially upweighted by Eq. (6). The additional logarithmic term inFμF_{\mu}acts as an entropic regularizer, penalizing highly concentrated allocations and preventing winner-take-all behavior; consequently, the stationary distribution of gains is softmax-like, with sharpness set by the parameterTT.

## II.2Analytic results

We now summarize three analytic results that organize the theoretical picture and will be used throughout the remainder of the paper. First, we show that the coupled neuron–astrocyte dynamics admit a global Lyapunov function, so trajectories are dissipative and converge to the set of stationary points rather than exhibiting sustained oscillations or chaos. This structural result justifies focusing on equilibria. Second, we characterize these equilibria explicitly via coupled fixed-point equations for(x∗,p∗)(x^{*},p^{*}), which reveal how astrocytic modulation implements a temperature-controlled, softmax-like allocation over patterns at stationarity. Finally, we connect the framework back to the classical Hopfield model by identifying limiting regimes in which the gain distribution becomes uniform and the effective synaptic matrix reduces toWHW_{H}. Together, these three results provide (i) a convergence guarantee, (ii) an interpretable description of the attractors, and (iii) a consistency link to the standard associative-memory baseline.

## II.2.1The system is a global gradient flow

A key property of the classical Hopfield network is the existence of an energy (Lyapunov) function that decreases along the trajectories thus guaranteeing convergence of the dynamics. As shown in the Appendix.1, our system can also be written as a gradient flow whose energy is given byℒ​(x,p)=\displaystyle\mathcal{L}(x,p)=K​T​∑μpμ​log⁡pμπμ−K​T​log⁡Z\displaystyle KT\sum_{\mu}p_{\mu}\log\frac{p_{\mu}}{\pi_{\mu}}-KT\log Z(9)+∑iNxi​ϕ​(xi)−L​(xi),\displaystyle+\sum_{i}^{N}x^{i}\phi(x^{i})-L(x^{i}),

whereπμ=1Z​efμ/T\pi_{\mu}=\frac{1}{Z}e^{f_{\mu}/T}withZ=∑μefμ/TZ=\sum_{\mu}e^{f_{\mu}/T}andL​(xi)=1σ​log⁡cosh⁡(σ​xi)L(x^{i})=\frac{1}{\sigma}\log\cosh(\sigma\,x^{i}). The gradient flow condition implies that this quantity decreases along the trajectoriesdd​t​ℒ​(x,p;t)=−‖∇ℒ​(x,p;t)‖2≤0\frac{d}{dt}\mathcal{L}(x,p;t)=-\|\nabla\mathcal{L}(x,p;t)\|^{2}\leq 0

. The last two terms of Eq.9are similar to the modern Hopfield networks[25,6], while the first term is the potential for the s-replicator equation also encoding for neuron-astrocyte interaction.
Sinceℒ\mathcal{L}is non-increasing and constant only at stationary points, the long-time behavior is fully determined by the coupled equilibria(x∗,p∗)(x^{*},p^{*}), which we analyze next.

## II.2.2Fixed point analysis

The equilibrium(x∗,p∗)(x^{*},p^{*}), satisfies the coupled fixed point conditionx∗=W​(p∗)​ϕ​(x∗)\displaystyle x^{*}=W(p^{*})\,\phi(x^{*})(10)pμ∗=exp⁡(fμ/T)∑νexp⁡(fν/T)=softmaxμ⁡(fμ​(x∗)T).\displaystyle p^{*}_{\mu}=\frac{\exp(f_{\mu}/T)}{\sum_{\nu}\exp(f_{\nu}/T)}=\operatorname{softmax}_{\mu}\!\left(\frac{f_{\mu}(x^{*})}{T}\right).(11)

This can be interpreted as a mixture of (rank 1) experts[26]commonly expressed asx∗=∑μgμ​(x∗)​Eμ​(ϕ​(x∗))x^{*}=\sum_{\mu}g_{\mu}(x^{*})E_{\mu}(\phi(x^{*})), where the self-attention like routinggμ​(x)≡pμg_{\mu}(x)\equiv p_{\mu}emerges naturally from the s-replicator, and the experts are rank-1 matricesEμ​(ϕ​(x))≡ξμ​ξμ⊺​ϕ​(x)E_{\mu}(\phi(x))\equiv\xi_{\mu}\xi_{\mu}^{\intercal}\phi(x). In this interpretation, astrocytic modulation provides the routing mechanism that selects the relevant memory patterns in a context-dependent and dynamical manner. These equilibrium relations make clear that the model reduces to the classical Hopfield network whenever the gain distribution is forced to remain (or becomes) uniform, which we discuss next through two limiting regimes.

## II.2.3Recovering the classical Hopfield model

Our model recovers the classical associative memory in two dynamical regimes. For the first case we take the gain timescale to be infiniteτp→∞\tau_{p}\to\inftysuch that the astrocytic influence remains constant for all timep˙μ=0\dot{p}_{\mu}=0(see Appendix.4). Since the modulation is initialized uniformlypμ=1/Kp_{\mu}=1/K, we recover the classical Hopfield mechanismτx​x˙=−x+W​(1/K)​ϕ​(x).\tau_{x}\dot{x}=-x+W(1/K)\phi(x).(12)

This should be interpreted as the astrocytic processes being frozen, in which case there may not be a modulatory influence on the neuron dynamics. The second limit in which we recover the classical model is when we takeT→∞T\to\infty, in which case the entropic term dominates and the only stable gain distribution is again uniformpμ=1/Kp_{\mu}=1/K(Appendix.4).

## II.3Simulation results

Our focus is on how two control knobs shape retrieval: (i) the relative timescales of neuronal relaxation and astrocytic routing, quantified byτx\tau_{x}andτp\tau_{p}, and (ii) the selectivity parameterTT, which sets the strength of entropic regularization in the gain dynamics. Because our dynamics are Lyapunov (Sec.II.2), convergence is guaranteed in principle; numerically, however, we observe a competition between intrinsic convergence time and the finite simulation horizontft_{f}. We therefore report both end-point observables and empirical convergence times to disentangle genuine failure from slow convergence.
We emphasize that these simulations are intended as proof-of-principle demonstrations of dynamical regimes controlled by(τx,τp,T)(\tau_{x},\tau_{p},T).

## II.3.1Dynamical analysis

In this first analysis, the goal is to understand the long term behavior of the system. To that end, we define two observables, one representative of the neuron component and the other for the astrocytic gains. Our focus is on how two control knobs shape retrieval: (i) the relative timescales of neuronal relaxation and astrocytic routing, quantified byτx\tau_{x}andτp\tau_{p}, and (ii) the selectivity parameterTT, which sets the strength of entropic regularization in the gain dynamics. Because our dynamics are Lyapunov (Sec.II.2), convergence is guaranteed in principle; numerically, however, we observe a competition between intrinsic convergence time and the finite simulation horizontft_{f}. We therefore report both end-point observables and empirical convergence times to disentangle genuine failure from slow convergence.
We simulate a network ofN=30N=30neurons storingK=100K=100binary (overlapping) patterns{ξμ}\{\xi_{\mu}\}via Eq.5. To probe retrieval, we corrupt a reference memoryξ0→ξ0η\xi_{0}\to\xi_{0}^{\eta}by flippingnnrandomly chosen entries, defining the noise levelη:=n/N=0.2\eta:=n/N=0.2(six flipped bits). We initialize the neuronal state with the corrupted memory,x​(ti)=ξ0ηx(t_{i})=\xi_{0}^{\eta}(see Appendix.5).

We quantify neuronal retrieval attft_{f}using asoftHamming error,Error=ϵ​(tf):=12​∑i=1N|ξ0i−ϕ​(xi​(tf))|,\text{Error}=\epsilon(t_{f}):=\frac{1}{2}\sum_{i=1}^{N}\left|\xi_{0}^{i}-\phi(x^{i}(t_{f}))\right|,(13)

which reduces to the standard Hamming distance whenϕ​(xi)∈{−1,1}\phi(x^{i})\in\{-1,1\}and satisfiesϵsoft∈[0,N]\epsilon_{\mathrm{soft}}\in[0,N].

To quantify how concentrated the gain vectorp​(tf)p(t_{f})is over memories, we compute its Shannon entropyH​[p]H[p]and the associated perplexityP:=exp⁡(H​[p])=exp⁡(−∑μ=1Kpμ​log⁡pμ).P:=\exp(H[p])=\exp(-\sum_{\mu=1}^{K}p_{\mu}\log p_{\mu}).(14)

Perplexity satisfiesP∈[1,K]P\in[1,K], withP=1P=1indicating near winner-take-all routing andP≈KP\approx Kindicating near-uniform allocation.
Unless stated otherwise, we setτx=1\tau_{x}=1,τp=1\tau_{p}=1, andT=0.01T=0.01, and vary one parameter at a time.

Varying astrocyte timescaleτp\tau_{p}(keepingτx=1\tau_{x}=1)

Mechanistically,τp\tau_{p}controls how rapidly the routing weightspμ​(t)p_{\mu}(t)track the instantaneous overlapsfμ​(x​(t))f_{\mu}(x(t)); smallτp\tau_{p}yields fast reweighting ofW​(p)W(p)toward the correct pattern, whereas largeτp\tau_{p}delays this reshaping, i.e.τp\tau_{p}parameter controls the gainp​(t)p(t)response time Fig.2. If we let astrocytic modulation be very fastτp→0\tau_{p}\to 0, the gains quickly concentrate on the most compatible memories, so the retrieval is fast and we get both low error and low perplexity. Asτp\tau_{p}increases, we see the gain adaptation become slower and the system needs more time to route the right memory. With a fixed simulation time, it looks like performance gets worse beyondτp∼10\tau_{p}\sim 10, but this behavior is explained simply because the simulation is stopped before convergence. In the extremeτp→∞\tau_{p}\to\inftycase, since the modulation essentially becomes frozen, the classical Hopfield regime is recovered, which performs poorly in this high memory storage regime (see also Appendix.4).Figure 1:End-of-run retrieval errorϵ​(tf)\epsilon(t_{f})and gain perplexityP​(tf)P(t_{f})as functions of the astrocytic timescaleτp\tau_{p}(withτx=1\tau_{x}=1), together with the corresponding convergence times. Solid lines show medians across trials; shaded bands denote percentile ranges(5,95)(5,95),(10,90)(10,90),(20,80)(20,80), and(25,75)(25,75).

Varying astrocyte timescaleτx\tau_{x}(keepingτp=1\tau_{p}=1)

τx\tau_{x}controls how fast neuronsx​(t)x(t)relax Fig.1. Settingτx→0\tau_{x}\to 0the neuron relaxation is essentially instantaneous, this makes the neuron configuration ”commit” to an attractor too early, before the modulatory signal has time to reshape the landscape. Then the gain modifies the effective connectivity around the wrong attractor leading to high confidence (low perplexity) on the wrong memory. On the other hand, as we increaseτx\tau_{x}, we see a decrease in the error as well as an increase in perplexity. High perplexity here means multiple patterns share similar overlap, so routing stays diffuse. This seemingly paradoxical region happens because as the neuron dynamics become slower, they do not have enough time to break the symmetry between patterns with similar fitness (see Appendix.3). In fact, if we increase the time limit, symmetry breaks and we get high pattern selectivity again. If we keep increasing toτx→∞\tau_{x}\to\infty, the convergence time increases super-linearly and we see the error stay exactly atϵ​(tf)=6\epsilon(t_{f})=6(in our simulations this happens atτx∼102\tau_{x}\sim 10^{2}, simply because the simulation time is bounded) (see Appendix.4).Figure 2:Final-time retrieval errorϵ​(tf)\epsilon(t_{f})and gain perplexityP​(tf)P(t_{f})as functions of the neuronal timescaleτx\tau_{x}(withτp=1\tau_{p}=1), together with the corresponding convergence times. Solid lines show medians across trials; shaded bands denote percentile ranges(5,95)(5,95),(10,90)(10,90),(20,80)(20,80), and(25,75)(25,75).

Varying temperatureTT(keepingτp=τx=1\tau_{p}=\tau_{x}=1):

ThusTTtunes a selectivity–robustness tradeoff: lowTTyields sharp routing (smallPP) and effective interference suppression, whereas highTTenforces near-uniform gains and recovers Hopfield-like behavior, i.e. temperature controls astrocyte selectivity Fig.3. WhenT→0T\to 0, both error and perplexity are low since the regularization effect is weak and becomes highly selective. WhenT→∞T\to\inftythe error increases because the entropy dominates, meaning thatppstays close to uniform and once again we recover the Hopfield regime (see Appendix.4).Figure 3:Final-time retrieval errorϵ​(tf)\epsilon(t_{f})and gain perplexityP​(tf)P(t_{f})as functions of temperatureTT(withτx=τp=1\tau_{x}=\tau_{p}=1), together with the corresponding convergence times. Solid lines show medians across trials; shaded bands denote percentile ranges(5,95)(5,95),(10,90)(10,90),(20,80)(20,80), and(25,75)(25,75).

## II.3.2Comparative retrieval performanceFigure 4:Retrieval benchmark across models. Each heat map reports the mean Hamming retrieval errorϵ​(tf)\epsilon(t_{f})(lighter indicates lower error) as a function of memory loadKK(x-axis) and corruption levelnn(y-axis; number of flipped bits in the query pattern). Each entry is averaged over 50 independent random pattern realizations.

We benchmark retrieval performance against (i) the classical Hopfield network and (ii) the neuron–astrocyte associative-memory model of Kozachkovet al.[20]; see Fig.4. To enable a dense scan over memory load and corruption, we setN=20N=20and vary the number of stored random binary patterns fromK=2K=2toK=200K=200. For each(K,n)(K,n)condition, we generate an independent pattern matrixΞ\Xi, corrupt the target patternξ0\xi_{0}by flippingnnrandomly chosen entries (equivalently, corruption fractionη=n/N\eta=n/N), and initialize the network asx​(ti)=ξ0(n)x(t_{i})=\xi_{0}^{(n)}(simulation protocol and model-specific parameters are reported in Appendix.5). All models are evaluated under the same initialization and the same finite simulation horizontft_{f}.

We quantify retrieval at timetft_{f}by binarizing the final state and computing the Hamming error with respect to the target:ϵ​(tf)=12​∑i=1N|ξ0i−sign​(xi​(tf))|,\epsilon(t_{f})=\frac{1}{2}\sum_{i=1}^{N}\left|\xi_{0}^{i}-\mathrm{sign}\!\big(x^{i}(t_{f})\big)\right|,(15)

so thatϵ∈[0,N]\epsilon\in[0,N]andϵ=0\epsilon=0indicates perfect retrieval. For statistical stability, we repeat each condition 50 times with independently sampledΞ\Xiand report the mean error.

Across the tested(K,n)(K,n)grid, our model yields lower mean retrieval error than both baselines, with the largest gains appearing at high memory loads where interference is strongest (Fig.4).

## IIIDiscussion

We introduced an astrocyte-gated extension of a Hopfield-type associative memory in which astrocytic processes allocate a finite modulatory capacity across stored patterns. By dynamically reweighting pattern-specific contributions to the effective connectivity, this additional degree of freedom reduces interference during retrieval and enlarges the regime in which accurate recall is achieved at high memory load.

We interpret each stored pattern as a memory-specific (engram-like) neuronal ensemble and the gain variablepμp_{\mu}as a coarse-grained proxy for the effective strength of astrocyte-mediated modulation of the synaptic pathway supporting patternμ\mu. This abstraction is motivated by the tripartite-synapse framework, in which astrocytes integrate local activity and can modulate synaptic efficacy through Ca2+-dependent signaling and related pathways[7,8,9,10,11,12]. Importantly, we do not interpretpμp_{\mu}as a direct readout of any single molecular mechanism; rather, it summarizes pathway-level modulation at the scale relevant for associative retrieval.

A central modeling assumption is the simplex constraint∑μpμ=1\sum_{\mu}p_{\mu}=1, which enforces competitive allocation: increasing gain for one pathway necessarily reduces gain available to others. This operationalizes finite modulatory capacity (e.g., limited signaling/metabolic resources distributed across microdomains) and homeostatic competition at the level of pattern gains, without implying that the brain literally implements a globally conserved scalar “budget.”

Mechanistically, the gain dynamics implement state-dependent competition. When the current neuronal state is more compatible with patternμ\mu, the corresponding matchfμ​(x)f_{\mu}(x)increases the fitnessFμF_{\mu}and thereby upweightspμp_{\mu}, which amplifies theμ\mu-th contribution toW​(p)W(p)while suppressing competitors. The logarithmic term inFμF_{\mu}acts as an entropic regularizer: it penalizes highly concentrated allocations and discourages winner-take-all routing. In this view, the temperature parameterTTcontrols selectivity: lowTTyields sharp, concentrated routing, whereas highTTenforces broader, near-uniform modulation and recovers Hopfield-like behavior. The joint neuron–astrocyte system remains Lyapunov-consistent (it admits a global Lyapunov function), ensuring convergence of the coupled dynamics.

Modern Hopfield networks and related dense-memory models achieve softmax-like retrieval through neuronal energy descent shaped by higher-order or exponential storage functions[3,4,6,19,20]. Our model produces a similar normalized reweighting, but via a different mechanism: normalization arises from competitive dynamics on the gain simplex (replicator-type routing) rather than being hard-wired into the neuronal energy landscape. In regimes where gains adapt rapidly, the stationary allocation approachespμ∗∝exp⁡(fμT),p^{*}_{\mu}\propto\exp\!\left(\frac{f_{\mu}}{T}\right),

so retrieval can be viewed as operating with a dynamically reweighted subset of memories. Compared to the classical Hopfield model, where high load is associated with numerous spurious mixture states, our routing variable tends to concentrate weight on a small set of candidates under ambiguity, consistent with the low-perplexity regimes observed in simulations.

In addition, the degree to which attention-like structure is explicit in our framework depends on the choice of pattern score. While the main model uses a squared-overlap scorefμ​(x)∝⟨ξμ,ϕ​(x)⟩2f_{\mu}(x)\propto\langle\xi_{\mu},\phi(x)\rangle^{2}(hence invariant under⟨ξμ,ϕ​(x)⟩↦−⟨ξμ,ϕ​(x)⟩\langle\xi_{\mu},\phi(x)\rangle\mapsto-\langle\xi_{\mu},\phi(x)\rangle), one may alternatively define a linear-overlap scorefμ​(x)=⟨ξμ,ϕ​(x)⟩f_{\mu}(x)=\langle\xi_{\mu},\phi(x)\rangle. In this variant, the neuronal drive becomes a linear combination of stored patterns weighted by the gain vector, i.e. the update takes the formx˙=−x+Ξ​p\dot{x}=-x+\Xi p(up to timescale factors), and in the fast-gain limit the stationary allocation becomesp∗∝exp⁡(Ξ⊺​ϕ​(x)/T)p^{*}\propto\exp(\Xi^{\intercal}\phi(x)/T), yielding the standard attention readoutx←Ξ​softmax​(Ξ⊺​ϕ​(x)/T)x\leftarrow\Xi\,\mathrm{softmax}(\Xi^{\intercal}\phi(x)/T)[5,6]. We do not analyze this variant further here; we include it to emphasize that competitive routing on the gain simplex can mechanistically reproduce attention-like computation under closely related definitions of pattern compatibility.

Numerically, this modulatory degree of freedom improves retrieval accuracy across increasing memory loadKKand increasing corruption levelnn(equivalentlyη=n/N\eta=n/N), outperforming both the classical Hopfield model[1]and the neuron–astrocyte associative-memory baseline[20]in the tested regimes (Fig.4). Intuitively, adaptive gain allocation reshapes the effective connectivity (and hence the attractor structure) during recall by amplifying task-relevant patterns and suppressing competitors, in line with recent evidence that time-dependent modulation can improve robustness of Hopfield-type retrieval[27].

The model also suggests qualitative dependencies that could guide future theoretical and computational work. In particular, changes in astrocytic kinetics or background modulatory tone would be expected to alter the sharpness of pattern selection (captured here byTT), while retrieval speed and stability should depend on the ratioτp/τx\tau_{p}/\tau_{x}setting the competition between routing and neuronal relaxation. More generally, the framework highlights a route by which transient changes in astrocyte-mediated signaling could bias recall without invoking synaptic plasticity. A limitation of the present formulation is thatpμp_{\mu}aggregates multiple biophysical processes and timescales into a single effective variable; identifying which cellular mechanisms and dynamical regimes can realize competitive allocation of this type remains an important direction for future work, and connects naturally to multi-timescale theories of memory stabilization[28].

An important direction is to convert the proposed competitive routing mechanism into a scalable ML architecture, whereppacts as a parameterized, context-dependent gating distribution over memory components andTTcontrols gating entropy. This suggests lightweight mixture-of-experts memories with explicit competition and separable routing and state-update timescales (set byτp/τx\tau_{p}/\tau_{x}). Developing stable, differentiable implementations and benchmarking them on noisy retrieval and continual-learning tasks are natural next steps.

## Acknowledgements.We thank Prof. Luiz Pessoa and Prof. Sergio Gómez for discussions on astrocyte kinetics and associative memory. This work has been supported by spanish Ministerio de Ministerio de Ciencia, Innovación y Universidades PID2024-158120NB-C21. AA also acknowledges the ICREA Academia program of Generalitat de Catalunya.

## Appendix

For the reader’s convenience, we collect here the few definitions that are repeatedly used in the derivations below, so the proofs can be followed without having to refer back to the main text. In particular, the effective synaptic matrix isW​(p)=KN​Ξ​diag​(p)​Ξ⊺=KN​∑μ=1Kpμ​ξμ​ξμ⊺W(p)=\frac{K}{N}\,\Xi\,\mathrm{diag}(p)\,\Xi^{\intercal}=\frac{K}{N}\sum_{\mu=1}^{K}p_{\mu}\,\xi_{\mu}\xi_{\mu}^{\intercal}.
For the gain dynamics,p∈ΔK−1p\in\Delta^{K-1}implies𝟏⊤​p˙=0\mathbf{1}^{\top}\dot{p}=0(tangent-space constraint), and the projector acts onTp​ΔK−1T_{p}\Delta^{K-1}. In the gradient-flow formulation we use the Shahshahani (Fisher information) metric onΔK−1\Delta^{K-1},G​(p)=diag​(1/p)G(p)=\mathrm{diag}(1/p), and the diagonal metric on neuronal pre-activations,Hx=diag​(ϕ′​(x))H_{x}=\mathrm{diag}(\phi^{\prime}(x))withϕ′​(x)=σ​sech2​(σ​x)\phi^{\prime}(x)=\sigma\,\mathrm{sech}^{2}(\sigma x)forϕ​(x)=tanh⁡(σ​x)\phi(x)=\tanh(\sigma x).

## .1Gradient-flow structure and Lyapunov function

Here we show that the coupled dynamics in Eqs. (4,6) admit a Lyapunov function and can be written as a (projected) gradient flow. We divide the discussion into the astrocyte domain and the neuron domain, where we derive their respective potentials.
Note that the coupled dynamics occur inx,p∈ℝN×ΔK−1x,p\in\mathbb{R}^{N}\times\Delta^{K-1}and the metric (needed for the gradient flow result) is given by a block-diagonal (direct-sum) metricGx,p=Hx⊕Gp.G_{x,p}=H_{x}\oplus G_{p}.

This metric is composed of the astrocyte and neuron domain metrics. The former is given by the Fisher information metric (equivalently the Shahshahani metric), whose components aregμ​μ′​(p)=δμ​μ′pμ,g_{\mu\mu^{\prime}}(p)=\frac{\delta_{\mu\mu^{\prime}}}{p_{\mu}},

so in matrix formG​(p)=diag​(1/p)G(p)=\mathrm{diag}(1/p). The latter is given byHx=diag​(ϕ′​(x)),H_{x}=\mathrm{diag}(\phi^{\prime}(x)),

where in our caseϕ′​(x)=σ​s​e​c​h2​(σ​x)\phi^{\prime}(x)=\sigma sech^{2}(\sigma x).

## .1.1Astrocyte domain

For the astrocyte domain, we first show how the simplex constraints are imposed via the orthogonal projection and then we define the s-replicator potential. With this, we obtain the ODE for theppvariable and we discuss its fixed points.

Following[29], given that we have a differential 0-form (or scalar potential)Φ:ℝK→ℝ\Phi:\mathbb{R}^{K}\to\mathbb{R}and a metricG​(p)G(p), we will define an ODE by computing the gradient of the scalar potential, and then projecting it onto the tangent space of the simplexp˙∈Tp​ΔK−1\dot{p}\in T_{p}\Delta^{K-1}(i.e.𝟏⊺​p˙=∑μKp˙μ=0\mathbf{1}^{\intercal}\dot{p}=\sum_{\mu}^{K}\dot{p}_{\mu}=0).
In more detail, to compute the gradient, we get the 1-form which lives in the cotangent spaced​Φ∈Tp∗​ℝKd\Phi\in T_{p}^{*}\mathbb{R}^{K}, since the gradient lives in the tangent space, using the sharp map musical isomorphism#G:Tp∗​ℝK→Tp​ℝK\#_{G}:T^{*}_{p}\mathbb{R}^{K}\to T_{p}\mathbb{R}^{K}, the gradient becomesz=G−1​(p)​d​Φ​(p)z=G^{-1}(p)d\Phi(p)wherez∈Tp​ℝKz\in T_{p}\mathbb{R}^{K}.
To compute the projection onto the tangent space of the simplexTp​ΔK−1T_{p}\Delta^{K-1}(since we want the evolution law of the ODE to remain on the simplex), we use the orthogonal projector mapΠG:Tp​ℝK→Tp​ΔK−1\Pi_{G}:T_{p}\mathbb{R}^{K}\to T_{p}\Delta^{K-1}, which takeszzto the closest vector inTp​ΔK−1T_{p}\Delta^{K-1}. That is, given a vectorzz, we solve forΠG​(z)=arg⁡minp˙∈Tp​ΔK−1​‖p˙−z‖G2\Pi_{G}(z)={\arg\min}_{\dot{p}\in T_{p}\Delta^{K-1}}||\dot{p}-z||_{G}^{2}, which returns the vector inTp​ΔK−1T_{p}\Delta^{K-1}satisfying the minimum distance condition. Written in variational formℒ​(p˙,λ)=12​‖p˙−z‖G2+λ​𝟏⊺​p˙,\mathcal{L}(\dot{p},\lambda)=\frac{1}{2}||\dot{p}-z||^{2}_{G}+\lambda\mathbf{1}^{\intercal}\dot{p},

its minimum corresponds to the projected vector. Thus, solving for the minimum condition∇p˙ℒ=0=G​(p˙−z)+λ​𝟏=0\nabla_{\dot{p}}\mathcal{L}=0=G(\dot{p}-z)+\lambda\mathbf{1}=0, we get that:p˙=z+λ​G−1​𝟏.\dot{p}=z+\lambda G^{-1}\mathbf{1}.(16)

The condition of a tangent vector to the simplex is𝟏⊺​p˙=0\mathbf{1}^{\intercal}\dot{p}=0, we obtainλ=𝟏⊺​z𝟏⊺​G−1​𝟏.\lambda=\frac{\mathbf{1}^{\intercal}z}{\mathbf{1}^{\intercal}G^{-1}\mathbf{1}}.(17)

where𝟏⊺​G−1​𝟏=∑ipi=1\mathbf{1}^{\intercal}G^{-1}\mathbf{1}=\sum_{i}p_{i}=1. Pluggingλ\lambdainto Eq. (16) and usingz=G−1​d​Φz=G^{-1}d\Phi:p˙=[𝕀−G−1​𝟏𝟏⊺]​G−1​d​Φ,\dot{p}=[\mathbb{I}-G^{-1}\mathbf{1}\mathbf{1}^{\intercal}]G^{-1}d\Phi,

and developing the expression, the ODE becomesp˙=(diag​(p)−p​p⊺)​d​Φ.\dot{p}=(\text{diag}(p)-pp^{\intercal})d\Phi.(18)

Now that we have our gradient flow ODE, we choose our0-form to beΦ(p)=TDK​L(p||π)\Phi(p)=TD_{KL}(p||\pi)withπ=1Z​e1T​f\pi=\frac{1}{Z}e^{\frac{1}{T}f}, such thatΦ​(p)=−⟨p,F⟩+T​log⁡Z,\Phi(p)=-\langle p,F\rangle+T\log Z,

whereF=f−T​log⁡pF=f-T\log pand the differential is given byd​Φ=T​log⁡p+T​𝟏−fd\Phi=T\log p+T\mathbf{1}-f(where neitherlog⁡Z\log Znorffdepend onpp). Substituting into Eq.18, we can write the gradient flow asp˙=−(diag​(p)−p​p⊺)​(T​log⁡p−f),\dot{p}=-(\text{diag}(p)-pp^{\intercal})(T\log p-f),(19)

whereT​𝟏T\mathbf{1}is proportional to𝟏\mathbf{1}and(diag​(p)−p​p⊺)​𝟏=0(\text{diag}(p)-pp^{\intercal})\mathbf{1}=0. We refer to this equation as thes-replicator(for ”soft” replicator) as the entropic termT​log⁡pT\log pprevents winner-take-all dynamics forT>0T>0.

The fixed points of Eq.19satisfy0=(diag​(p)−p​p⊺)​F,0=(\text{diag}(p)-pp^{\intercal})F,

WhereF=f−T​log⁡pF=f-T\log p. One (degenerate) way to satisfy this condition is to make(diag​(p)−p​p⊺)=0(\text{diag}(p)-pp^{\intercal})=0where we get two conditionspμ=pμ2p_{\mu}=p_{\mu}^{2}andpμ​pν=0p_{\mu}p_{\nu}=0. It can only be satisfied whenppis a one-hot vector, thus, the solution lies on the boundary (vertices) of the simplex. Solutions inside the simplex (wherepμ>0​∀μp_{\mu}>0\,\,\forall\mu) satisfydiag​(p)​F=p​p⊺​F.\text{diag}(p)F=pp^{\intercal}F.

Expressing it element-wise, sincepμ>0p_{\mu}>0, dividing bypμp_{\mu}0=Fμ−∑νKpν​Fν∀μ,0=F_{\mu}-\sum_{\nu}^{K}p_{\nu}F_{\nu}\quad\forall\mu,

using thatFμ=fμ−T​log⁡pμF_{\mu}=f_{\mu}-T\log p_{\mu}and solving forpμp_{\mu}log⁡pμ=1T​[fμ−∑νKpν​Fν]⇒pμ=e1T​[fμ−∑νKpν​Fν].\log p_{\mu}=\frac{1}{T}\left[f_{\mu}-\sum_{\nu}^{K}p_{\nu}F_{\nu}\right]\Rightarrow p_{\mu}=e^{\frac{1}{T}\left[f_{\mu}-\sum_{\nu}^{K}p_{\nu}F_{\nu}\right]}.(20)

Imposing∑μKpμ=1\sum_{\mu}^{K}p_{\mu}=1gives1=e−1T​∑νKpν​Fν​∑μKe1T​fμ,1=e^{-\frac{1}{T}\sum_{\nu}^{K}p_{\nu}F_{\nu}}\sum_{\mu}^{K}e^{\frac{1}{T}f_{\mu}},

where taking logarithms, we can identify∑νpν​Fν=T​log​∑μe1T​fμ{\sum_{\nu}p_{\nu}F_{\nu}}=T\log\sum_{\mu}e^{\frac{1}{T}f_{\mu}}and we can recognize the partition functionZ=∑μe1T​fμZ=\sum_{\mu}e^{\frac{1}{T}f_{\mu}}. Finally we can rewrite Eq.20aspμ=1Z​e1T​fμ,p_{\mu}=\frac{1}{Z}e^{\frac{1}{T}f_{\mu}},(21)

where in vector formp∗=softmax​(1T​f∗)p^{*}=\text{softmax}\left(\frac{1}{T}f^{*}\right).

## .1.2Neuron domain

Here we provide a derivation of the classical Hopfield dynamics starting from the energy. We see that the metricHx=diag​(ϕ′​(x))H_{x}=\text{diag}(\phi^{\prime}(x))emerges as a natural choice. The Hopfield model energy[1]is a scalar functionE:ℝN→ℝE:\mathbb{R}^{N}\to\mathbb{R}expressed asE​(x)=−12​∑i​jNϕ​(xi)​Wi​j​ϕ​(xj)+∑iN[xi​ϕ​(xi)−L​(xi)],E(x)=-\frac{1}{2}\sum_{ij}^{N}\phi(x^{i})W^{ij}\phi(x^{j})+\sum_{i}^{N}[x^{i}\phi(x^{i})-L(x^{i})],(22)

whereL​(xi)=∫xiϕ​(u)​𝑑uL(x^{i})=\int^{x^{i}}\phi(u)duandϕ​(x)=tanh⁡(k​x)\phi(x)=\tanh(k\,x), thusL​(xi)=1k​log⁡cosh⁡(σ​xi)L(x^{i})=\frac{1}{k}\log\cosh(\sigma\,x^{i}). It can be shown that this potential induces a global gradient flow similarly to[30]. To show this, we compute the differential of the energyd​E=∑i∂E∂xi​d​xidE=\sum_{i}\frac{\partial E}{\partial x^{i}}dx^{i}lying ind​E∈Tx∗​ℝNdE\in T_{x}^{*}\mathbb{R}^{N}and convert it to a gradient flow using the sharp map just like before using the metricHx=diag​(ϕ′)H_{x}=\text{diag}(\phi^{\prime}). Differentiating the first termE1E_{1}, we get∂xkE1\displaystyle\partial_{x^{k}}E_{1}=−∑i​j[∂xkϕ​(xi)​Wi​j​ϕ​(xj)+ϕ​(xi)​Wi​j​∂xkϕ​(xj)]\displaystyle=-\sum_{ij}[\partial^{x^{k}}\phi(x^{i})W^{ij}\phi(x^{j})+\phi(x^{i})W^{ij}\partial_{x^{k}}\phi(x^{j})](23)=−∑iϕ​(xi)​Wk​i​ϕ′​(xk),\displaystyle=-\sum_{i}\phi(x^{i})W^{ki}\phi^{\prime}(x^{k}),

where we have assumed thatW=W⊺W=W^{\intercal}. For the second termE2E_{2}, we get:∂xkE2=xk​ϕ′​(xk).\partial_{x^{k}}E_{2}=x^{k}\phi^{\prime}(x^{k}).(24)

Combining both terms,∂xkE=[xk−∑iWi​k​ϕ​(xi)]​ϕ′​(xk),\partial_{x^{k}}E=\left[x^{k}-\sum_{i}W^{ik}\phi(x^{i})\right]\,\phi^{\prime}(x^{k}),

or in vector formd​E=diag​(ϕ′)​[x−W​ϕ].dE=\text{diag}(\phi^{\prime})[x-W\phi].

Taking the sharp map#H:Tx∗​ℝN→Tx​ℝN\#_{H}:T^{*}_{x}\mathbb{R}^{N}\to T_{x}\mathbb{R}^{N}, we getx˙=−H−1​d​E\dot{x}=-H^{-1}dE, where the metric necessarily becomesHx=diag​(ϕ′​(x)).H_{x}=\text{diag}(\phi^{\prime}(x)).

Note that1/ϕ′​(x)>01/\phi^{\prime}(x)>0since in our caseϕ′=s​e​c​h2\phi^{\prime}=sech^{2}. BecauseHxH_{x}is diagonal, it also satisfieshx​(u,u)=0h_{x}(u,u)=0ifu=0u=0andhx​(u,v)=hx​(v,u)h_{x}(u,v)=h_{x}(v,u)for allxx. This is exactly the same as[30]up to the change of variablez=ϕ​(x)z=\phi(x), wherezzis their dynamical variable, this way,z˙=ϕ′​(ϕ−1​(z))​[ϕ−1​(z)−W​z]\dot{z}=\phi^{\prime}(\phi^{-1}(z))[\phi^{-1}(z)-Wz]is exactlyϕ′​x˙=ϕ′​[x−W​ϕ]\phi^{\prime}\dot{x}=\phi^{\prime}[x-W\phi].

## .1.3Joint potential

Finally, we can combine the parts to define the joint potential functionℒ:ℝN×ΔK→ℝ\mathcal{L}:\mathbb{R}^{N}\times\Delta^{K}\rightarrow\mathbb{R}for the whole system from which we can derive the dynamics as a gradient flow. We define it asℒ(x,p)=−KTlogZ+KTDK​L(p||π)+[⟨x,ϕ⟩−L(x)],\mathcal{L}(x,p)=-KT\log Z+KTD_{KL}(p||\pi)+[\langle x,\phi\rangle-L(x)],

which combines the two potentials we have described so far. From Eq..1.1, we know thatTDK​L(p||π)=−⟨p,F⟩+TlogZTD_{KL}(p||\pi)=-\langle p,F\rangle+T\log Zand we can express it likeℒ​(x,p)=−K​⟨p,f⟩+K​T​⟨p,log⁡p⟩+[⟨x,ϕ⟩−L​(x)],\mathcal{L}(x,p)=-K\langle p,f\rangle+KT\langle p,\log p\rangle+[\langle x,\phi\rangle-L(x)],

wherefμ=12​N​(∑iξμi​ϕi)2f_{\mu}=\frac{1}{2N}\left(\sum_{i}\xi^{i}_{\mu}\phi^{i}\right)^{2}. In this form, the interaction term⟨p,f⟩=12​N​∑μpμ​⟨ξμ,ϕ⟩2\langle p,f\rangle=\frac{1}{2N}\sum_{\mu}p_{\mu}\langle\xi_{\mu},\phi\rangle^{2}is in direct analogy to12​ϕ​W​ϕ=12​N​∑μ⟨ξμ,ϕ⟩2\frac{1}{2}\phi W\phi=\frac{1}{2N}\sum_{\mu}\langle\xi_{\mu},\phi\rangle^{2}of Eq.22, where now each term comes multiplied by the modulationpμp_{\mu}. The second term is the astrocytic regularization and the last one is the neuron activation term.
From this potential we can derive the dynamics of our system by taking the differential living ind​ℒ​(x,p)∈Tx,p∗​(ℝN×ΔK−1)d\mathcal{L}(x,p)\in T^{*}_{x,p}(\mathbb{R}^{N}\times\Delta^{K-1})such that:d​ℒ​(x,p)=∑iN∂ℒ∂xi​d​xi+∑μK∂ℒ∂pμ​d​pμ.d\mathcal{L}(x,p)=\sum_{i}^{N}\frac{\partial\mathcal{L}}{\partial x^{i}}dx^{i}+\sum_{\mu}^{K}\frac{\partial\mathcal{L}}{\partial p_{\mu}}dp_{\mu}.(25)

For the∂pℒ​(x,p)\partial_{p}\mathcal{L}(x,p)term, it is exactly the same as in Eq.19. For the first derivative, we have the interaction and activation terms. The activation term is exactly the same as in Eq.24, and for the interaction term we haveK​∂xk⟨p,f⟩=KN​∑μK∑iNpμ​ξμi​ξμk​ϕ​(xi)​ϕ′​(xk),K\partial_{x^{k}}\langle p,f\rangle=\frac{K}{N}\sum_{\mu}^{K}\sum_{i}^{N}p_{\mu}\xi_{\mu}^{i}\xi_{\mu}^{k}\phi(x^{i})\phi^{\prime}(x^{k}),

where in vector formKN​∑μξμk​pμ​⟨ξμ,ϕ​(x)⟩​ϕ′​(xk)=diag​(ϕ′)​W​(p)​ϕ​(x)\frac{K}{N}\sum_{\mu}\xi_{\mu}^{k}p_{\mu}\langle\xi_{\mu},\phi(x)\rangle\phi^{\prime}(x^{k})=\text{diag}(\phi^{\prime})W(p)\phi(x), where we define the weight matrix as:W​(p)=KN​Ξ⊺​diag​(p)​ΞW(p)=\frac{K}{N}\Xi^{\intercal}\text{diag}(p)\Xi

Putting everything together, the two terms of Eq.25become:∂xℒ​(x,p)=diag​(ϕ′)​[x−W​(p)​ϕ]\displaystyle\partial_{x}\mathcal{L}(x,p)=\text{diag}(\phi^{\prime})[x-W(p)\phi](26)∂pℒ​(x,p)=K​(T​log⁡p+T​𝟏−f).\displaystyle\partial_{p}\mathcal{L}(x,p)=K(T\log p+T\mathbf{1}-f).(27)

Finally, to get the gradient flow, the metric of the whole space is the direct sumM​(x,p)=H​(x)⊕G​(p)M(x,p)=H(x)\oplus G(p)and the orthogonal projection acts only on the astrocyte subspace, thusΠ=𝕀⊕ΠG=𝕀⊕(𝕀−G−1​𝟏⊺​𝟏​G−1)\Pi=\mathbb{I}\oplus\Pi_{G}=\mathbb{I}\oplus(\mathbb{I}-G^{-1}\mathbf{1}^{\intercal}\mathbf{1}G^{-1}). The natural gradient descent ofℒ​(x,p)\mathcal{L}(x,p)can finally be expressed as(τx​x˙τp​p˙)=−(𝕀00ΠG)​(H−100G−1)​(∂xℒ​(x,z)∂pℒ​(x,p)).\begin{pmatrix}\tau_{x}\dot{x}\\
\tau_{p}\dot{p}\end{pmatrix}=-\begin{pmatrix}\mathbb{I}&0\\
0&\,\Pi_{G}\end{pmatrix}\begin{pmatrix}H^{-1}&0\\
0&\,G^{-1}\end{pmatrix}\begin{pmatrix}\partial_{x}\mathcal{L}(x,z)\\
\partial_{p}\mathcal{L}(x,p)\end{pmatrix}.

Thus, the dynamics are as intendedτx​x˙=−x+W​(p)​ϕ​(x)\displaystyle\tau_{x}\dot{x}=-x+W(p)\phi(x)(28)τp​p˙=(diag​(p)−p​p⊺)​(f−T​log⁡p),\displaystyle\tau_{p}\dot{p}=(\text{diag}(p)-pp^{\intercal})(f-T\log p),(29)

where we renormalize the time constantτp/K→τp\tau_{p}/K\rightarrow\tau_{p}. This completes the proof that the system is a gradient flow by construction.

## .2Dynamical analysis of the system:

Now that we have defined the evolution of the system, we can explore both its symmetries as well as its long-term behavior in different parameter regimes to better understand its dynamics.

## .3Symmetry remarks

## .3.1ℤ2\mathbb{Z}_{2}invariance of the squared-overlap score

In the main model the pattern score is a squared overlap,fμ​(x)∝⟨ξμ,ϕ​(x)⟩2f_{\mu}(x)\propto\langle\xi_{\mu},\phi(x)\rangle^{2}.
Consequently, the gain dynamics are invariant under the sign flip⟨ξμ,ϕ​(x)⟩↦−⟨ξμ,ϕ​(x)⟩\langle\xi_{\mu},\phi(x)\rangle\mapsto-\langle\xi_{\mu},\phi(x)\rangle.
Equivalently, definingmμ​(x)≡⟨ξμ,ϕ​(x)⟩m_{\mu}(x)\equiv\langle\xi_{\mu},\phi(x)\rangle, the gain update depends only onmμ2m_{\mu}^{2}and cannot distinguishmμm_{\mu}from−mμ-m_{\mu}. More generally, if two patterns satisfyfμ​(x)=fρ​(x)f_{\mu}(x)=f_{\rho}(x)at a given state, the gain update has no instantaneous preference between them.

## .3.2Symmetry breaking by neuronal dynamics

Even with the squared-overlap score, degeneracies such asfμ​(x)=fρ​(x)f_{\mu}(x)=f_{\rho}(x)are typically lifted by the neuronal evolution. To see this, consider the early-time dynamics with uniform gainsp=𝟏/Kp=\mathbf{1}/K, for whichτx​x˙i=−xi+1N​∑μ=1Kξμi​mμ,mμ≡∑j=1Nξμj​ϕ​(xj).\tau_{x}\dot{x}^{i}=-x^{i}+\frac{1}{N}\sum_{\mu=1}^{K}\xi_{\mu}^{i}\,m_{\mu},\qquad m_{\mu}\equiv\sum_{j=1}^{N}\xi_{\mu}^{j}\,\phi(x^{j}).

Differentiatingmμm_{\mu}givesm˙μ=∑iξμi​ϕ′​(xi)​x˙i\dot{m}_{\mu}=\sum_{i}\xi_{\mu}^{i}\,\phi^{\prime}(x^{i})\dot{x}^{i}, henceτx​m˙μ=−∑i=1Nξμi​ϕ′​(xi)​xi+1N​∑ν=1Kmν​∑i=1Nξμi​ϕ′​(xi)​ξνi.\tau_{x}\dot{m}_{\mu}=-\sum_{i=1}^{N}\xi_{\mu}^{i}\,\phi^{\prime}(x^{i})x^{i}+\frac{1}{N}\sum_{\nu=1}^{K}m_{\nu}\sum_{i=1}^{N}\xi_{\mu}^{i}\,\phi^{\prime}(x^{i})\xi_{\nu}^{i}.

Taking the difference between two overlaps yieldsτx​Δ​m˙=−∑i=1NΔ​ξi​ϕ′​(xi)​xi+1N​∑ν=1Kmν​∑i=1NΔ​ξi​ϕ′​(xi)​ξνi,\tau_{x}\Delta\dot{m}=-\sum_{i=1}^{N}\Delta\xi^{i}\,\phi^{\prime}(x^{i})x^{i}+\frac{1}{N}\sum_{\nu=1}^{K}m_{\nu}\sum_{i=1}^{N}\Delta\xi^{i}\,\phi^{\prime}(x^{i})\xi_{\nu}^{i},(30)

whereΔ​m˙=m˙μ−m˙ρ\Delta\dot{m}=\dot{m}_{\mu}-\dot{m}_{\rho}andΔ​ξi=ξμi−ξρi\Delta\xi^{i}=\xi_{\mu}^{i}-\xi_{\rho}^{i}. Except for nongeneric trajectories where the right-hand side vanishes identically,Δ​m˙≠0\Delta\dot{m}\neq 0and the degeneracy is broken over time. Sincef˙μ=(mμ/N)​m˙μ\dot{f}_{\mu}=(m_{\mu}/N)\dot{m}_{\mu}, this induces a gain reweighting in the astrocytic dynamics. In practice, this mechanism implies that equal-fitness ties are generically transient and are resolved asx​(t)x(t)evolves away from the initialization.

## .4Fixed points of the system

Given the system dynamics of Eq.28fixed point conditions:x∗=W​(p∗)​ϕ​(x∗)\displaystyle x^{*}=W(p^{*})\phi(x^{*})(31)p∗=softmax⁡(f​(x∗)T),\displaystyle p^{*}=\operatorname{softmax}\!\left(\frac{f(x^{*})}{T}\right),(32)

where the second equation comes from Eq.21. Plugging the second equation into the first, it can be rewritten as a single equation on thexxdomain. In this general regime, there are no analytic solutions, but we can see how the system behaves in different regimes: either hold the temperature fixed and take asymptotic limits of the time constants, or instead fix the time constants and examine the temperature limits.

Caseτp→0\tau_{p}\to 0:In this case we instantly getpμ∗=softmax​(12​N​T​⟨ξμ,ϕ​(x)⟩2)p^{*}_{\mu}=\text{softmax}\left(\frac{1}{2NT}\langle\xi_{\mu},\phi(x)\rangle^{2}\right), so the evolution is written like:τx​d​xd​t=−x+W​(p)​ϕ​(x)\tau_{x}\frac{dx}{dt}=-x+W(p)\,\phi(x)

This corresponds to a biased Hopfield network in which every memory is weighted bypμ∗p^{*}_{\mu}likeW=∑μpμ∗​ξμ​ξμ⊺W=\sum_{\mu}p^{*}_{\mu}\xi_{\mu}\xi_{\mu}^{\intercal}. Sincepμ∗p^{*}_{\mu}is highly heterogeneous when|⟨ξμ,ϕ⟩||\langle\xi_{\mu},\phi\rangle|is high, we are biasing the Hopfield evolution matrix towards those patterns which are more likely to contain the pattern we are searching for.

Caseτp→∞\tau_{p}\to\infty:If we takeτp→∞\tau_{p}\to\infty, the astrocytic modulation is frozenp˙=0\dot{p}=0, that is,p​(t)=p¯p(t)=\bar{p}is constant. Since the astrocytic influence is initialized by the uniform vectorp=𝟏/Kp=\mathbf{1}/K, we recover the classical Hopfield dynamicsτx​x˙=−x+W​(p¯)​ϕ​(x),\tau_{x}\dot{x}=-x+W(\bar{p})\,\phi(x),(33)

where withdiag​(p¯)=diag​(1/K)\text{diag}(\bar{p})=\text{diag}(1/K)and thusτx​x˙=−α​x+W​ϕ​(x)\tau_{x}\dot{x}=-\alpha x+W\,\phi(x).

Caseτx→0\tau_{x}\to 0:In this case, the neurons evolve instantaneously to their fixed pointx∗=W​(p)​ϕ​(x∗)x^{*}=W(p)\phi(x^{*}). This way, we haveτp​p˙=(diag​(p)−p​p⊺)​(f−T​log⁡p),\tau_{p}\dot{p}=(\text{diag}(p)-pp^{\intercal})(f-T\log p),

wherefμ=12​N​T​⟨ξμ,ϕ​(x∗)⟩2f_{\mu}=\frac{1}{2NT}\langle\xi_{\mu},\phi(x^{*})\rangle^{2}is a transcendental function that depends also onpp. Since the initial condition for the modulation equation is the uniformp=𝟏/Kp=\mathbf{1}/K, the neurons initial configuration is already at a fixed point of the classical Hopfield dynamicx∗=W​(1/K)​ϕ​(x∗)x^{*}=W(1/K)\phi(x^{*}). For a sufficiently large number of patterns, the initial fixed point will likely be a spurious minima. This means, in the very first instants of time, sincex​(t0)=x∗x(t_{0})=x^{*}, the fitnessf​(x∗)f(x^{*})of astrocytic modulation, will select those patterns that are the most similar to theϕ​(x∗)\phi(x^{*})configuration, which can be arbitrarily far fromx0x_{0}and thus even becoming detrimental for retrieval.

Caseτx→∞\tau_{x}\to\infty:Here we havex˙=0\dot{x}=0, meaning thatx​(t)x(t)is constant it cannot evolve, so we stay forever in the initial condition even if the astrocyte dynamics converge to a fixed point in theppdomain.

CaseT→∞T\to\infty:Keeping now the time scales constant, in this regime, the regularization effect on the s-replicator is so strong that the system stays in thep=𝟏/Kp=\mathbf{1}/Ksolution. Taking the astrocyte component, we can rearrange for the temperature to obtainτpT​d​pμd​t=1T​pμ​(fμ−∑νpν​fν)−pμ​(log⁡pμ−∑νpν​log⁡pν).\frac{\tau_{p}}{T}\frac{dp_{\mu}}{dt}=\frac{1}{T}p_{\mu}(f_{\mu}-\sum_{\nu}p_{\nu}f_{\nu})-p_{\mu}(\log p_{\mu}-\sum_{\nu}p_{\nu}\log p_{\nu}).

TakingT→∞T\to\infty, we see thatlog⁡pμ=⟨log⁡p⟩\log p_{\mu}=\langle\log p\ranglewhere we are forced into a maximum entropy distribution. This way we recover the classical Hopfield model.

CaseT→0T\to 0:Similarly, rearranging for temperature, if we takeT→0T\to 0, the dynamics becomeτp​d​pμd​t=pμ​(fμ−∑νpν​fν),\tau_{p}\frac{dp_{\mu}}{dt}=p_{\mu}(f_{\mu}-\sum_{\nu}p_{\nu}f_{\nu}),

in which case there is no regularization. The fixed points of the system are given byx∗=1α​Ξ​diag​(p∗)​Ξ⊺​ϕ​(x∗)\displaystyle x^{*}=\frac{1}{\alpha}\Xi\text{diag}(p^{*})\Xi^{\intercal}\phi(x^{*})(34)p∗=𝟏M​(x∗)|M​(x∗)|,\displaystyle p^{*}=\frac{\mathbf{1}_{M(x^{*})}}{|M(x^{*})|},(35)

whereM​(x)M(x)is the set ofpμp_{\mu}elements that satisfyM​(x∗)=arg⁡maxμ⁡fμ​(x∗)M(x^{*})=\arg\max_{\mu}f_{\mu}(x^{*})and𝟏M​(x∗)∈{0,1}K\mathbf{1}_{M(x^{*})}\in\{0,1\}^{K}. Note thatM​(x∗)M(x^{*})will generally have a single element unless in the contrived case discussed before in Eq.(30).

## .5Simulations details

To integrate Eq. (6), we use an explicit Euler method. Trajectories are computed for10/d​t10/dttime steps, withd​t=0.001dt=0.001, using smaller steps for small parameter value regimes (i.e. ifα\alphais the parameter thend​t=α⋅0.05dt=\alpha\cdot 0.05ifα≤0.01\alpha\leq 0.01). For statistically significant results, we run5050simulations with different random pattern matricesΞ\Xifor every different parameter configuration. The observables are computed using the values of the last configuration valuesx​(tf),p​(tf)x(t_{f}),p(t_{f}). To plot the percentile bands, we have smoothed out noise using a 1d Gaussian filter for better visualization. The code to reproduce the simulations is available at[31].

## References
- Hopfield [1982]J. J. Hopfield,Proceedings of the National Academy of
Sciences79, 2554
(1982).
- Amit [1989]D. J. Amit,Modeling Brain Function:
The World of Attractor Neural Networks(Cambridge
University Press, 1989).
- Krotov and Hopfield [2016]D. Krotov and J. J. Hopfield, inAdvances in
Neural Information Processing Systems, Vol. 29 (2016) pp. 1172–1180.
- Krotov and Hopfield [2021]D. Krotov and J. Hopfield, inInternational
Conference on Learning Representations(2021) arXiv:2008.06996.
- Vaswaniet al.[2017]A. Vaswani, N. Shazeer,et al., inAdvances in Neural Information Processing Systems(2017).
- Ramsaueret al.[2021]H. Ramsauer, B. Schäfl,
J. Lehner, P. Seidl, M. Widrich, T. Adler, L. Gruber, M. Holzleitner, M. Pavlović, G. K. Sandve, V. Greiff, D. Kreil,
M. Kopp, G. Klambauer, J. Brandstetter, and S. Hochreiter,Hopfield networks is
all you need(2021),arXiv:2008.02217 [cs.NE].
- Araqueet al.[1999]A. Araque, R. P. Sanzgiri, V. Parpura, and P. G. Haydon,Canadian Journal of Physiology and Pharmacology77, 699 (1999).
- Pereaet al.[2009]G. Perea, M. Navarrete, and A. Araque,Trends in Neurosciences32, 421 (2009).
- Letellieret al.[2016]M. Letellier, Y. K. Park,
T. E. Chater, P. H. Chipman, S. G. Gautam, T. Oshima-Takago, and Y. Goda,Proceedings of the National Academy of Sciences of the USA113, E2685 (2016).
- De Pittàet al.[2016]M. De Pittà, N. Brunel, and A. Volterra,Neuroscience323, 43 (2016).
- Giaumeet al.[2010]C. Giaume, A. Koulakoff,
L. Roux, D. Holcman, and N. Rouach, Nature Reviews Neuroscience11, 87 (2010).
- Verkhratsky and Nedergaard [2018]A. Verkhratsky and M. Nedergaard,Physiological Reviews98, 239 (2018).
- Purushotham and Buskila [2023]S. S. Purushotham and Y. Buskila,Frontiers in Network Physiology3, 1205544 (2023).
- Makovkinet al.[2022]S. Makovkin, E. Kozinov,
M. Ivanchenko, and S. Gordleeva,Scientific Reports12, 6970 (2022).
- Thompsonet al.[2021]L. Thompson, J. Khuc,
M. S. Saccani, N. Zokaei, and M. Cappelletti,Experimental Brain Research239, 2711 (2021).
- Dewaet al.[2025]K.-I. Dewa, K. Kaseda,
A. Kuwahara, H. Kubotera, A. Yamasaki, N. Awata, A. Komori, M. A. Holtz, A. Kasai, H. Skibbe,
N. Takata, T. Yokoyama, M. Tsuda, G. Numata, S. Nakamura, E. Takimoto, M. Sakamoto, M. Ito, T. Masuda, and J. Nagai, Nature10.1038/s41586-025-09619-2(2025), online ahead of
print.
- Zbaranska and Josselyn [2025]S. Zbaranska and S. A. Josselyn,Cell Research35, 241 (2025).
- Josselyn and Tonegawa [2020]S. A. Josselyn and S. Tonegawa,Science367, eaaw4325 (2020).
- Kozachkovet al.[2023]L. Kozachkov, K. V. Kastanenka, and D. Krotov,Proceedings of the National Academy of
Sciences120, e2219150120 (2023).
- Kozachkovet al.[2025]L. Kozachkov, J.-J. Slotine, and D. Krotov,Proceedings of the National Academy of
Sciences122, e2417788122 (2025).
- Di Castroet al.[2011]M. A. Di Castro, J. Chuquet,
N. Liaudet, K. Bhaukaurally, M. Santello, D. Bouvier, P. Tiret, and A. Volterra, Nature Neuroscience14, 1276 (2011).
- Perea and Araque [2007]G. Perea and A. Araque, Science317, 1083 (2007).
- Agulhonet al.[2010]C. Agulhon, T. A. Fiacco, and K. D. McCarthy, Science327, 1250
(2010).
- Shigetomiet al.[2016]E. Shigetomi, S. Patel, and B. S. Khakh, Trends in Cell
Biology26, 300
(2016).
- Krotov and Hopfield [2020]D. Krotov and J. Hopfield, arXiv preprint arXiv:2008.06996 (2020).
- Jacobset al.[1991]R. A. Jacobs, M. I. Jordan,
S. J. Nowlan, and G. E. Hinton, Neural
computation3, 79
(1991).
- Bettetiet al.[2025]S. Betteti, G. Baggio,
F. Bullo, and S. Zampieri,Science Advances11, eadu6991 (2025).
- Benna and Fusi [2016]M. K. Benna and S. Fusi,Nature Neuroscience19, 1697 (2016).
- Mertikopoulos and Sandholm [2018]P. Mertikopoulos and W. H. Sandholm, Journal of Economic Theory177, 315 (2018).
- Halderet al.[2020]A. Halder, K. F. Caluya,
B. Travacca, and S. J. Moura,IEEE Transactions on Neural Networks and Learning Systems31, 4869 (2020).
- Vivet and Arenas [2026]A. Vivet and A. Arenas,Astrocyte-gated associative memory: code repository, GitHub repository (2026), accessed 10 Feb 2026.
https://github.com/arnauvivett/Astrocyte-gated-associative-memory-.

## 


- 


Major funding support from
