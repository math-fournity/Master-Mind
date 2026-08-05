# Nonlinear Model Reduction of Complex Networks via Spectral Submanifolds

**arXiv ID**: 2607.24121v1
**Authors**: Kaviya Bhaskaran, Shobhit Jain, Mingwu Li
**Published**: 2026-07-27
**Categories**: physics.soc-ph, math.DS, q-bio.QM
**HTML URL**: https://arxiv.org/html/2607.24121v1

## Abstract

Complex networked systems are prevalent in biology, engineering, and the social sciences, yet their high-dimensional, nonlinear dynamics pose major challenges for analysis and prediction. A mathematically rigorous route to simplification is to represent system behavior on a low-dimensional, smooth invariant manifold known as a spectral submanifold (SSM). Here we present a comprehensive SSM reduction framework and its globalized extension (gSSM) for dimensionality reduction in large-scale nonlinear networks. Our approach yields accurate global and node-level predictions across synthetic and real networks, including highly heterogeneous topologies and systems with higher-order interactions. Crucially, SSM is a robust tipping-point predictor: even at low truncation order (e.g., $O(2)$) it reliably identifies the onset of sustained activity, while higher orders and gSSM capture post-onset amplitudes and saturation. Consistently, the reduction collapses the full network dynamics to a one-dimensional system, offering clarity and efficiency. Across all the realizations, SSM/gSSM consistently outperform classical spectral and mean-field methods in modeling critical transitions at both microscopic and macroscopic scales, establishing SSM-based reduction as a robust, interpretable tool for nonlinear networked systems with broad applicability to epidemiology, ecology, and engineered networks.

## Full Text

Nonlinear Model Reduction of Complex Networks via Spectral Submanifolds

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.24121v1 [physics.soc-ph] 27 Jul 2026

## Nonlinear Model Reduction of Complex Networks via Spectral SubmanifoldsKaviya BhaskaranDepartment of Mechanics and Aerospace Engineering, Southern University of Science and Technology, Shenzhen 518055, ChinaShobhit JainDelft Institute of Applied Mathematics, TU Delft, Mekelweg 4, 2628 CD Delft, The NetherlandsMingwu LiDepartment of Mechanics and Aerospace Engineering, Southern University of Science and Technology, Shenzhen 518055, China

## Abstract

Complex networked systems are prevalent in biology, engineering, and the social sciences, yet their high-dimensional, nonlinear dynamics pose major challenges for analysis and prediction. A mathematically rigorous route to simplification is to represent system behavior on a low-dimensional, smooth invariant manifold known as a spectral submanifold (SSM). Here we present a comprehensive SSM reduction framework and its globalized extension (gSSM) for dimensionality reduction in large-scale nonlinear networks. Our approach yields accurate global and node-level predictions across synthetic and real networks, including highly heterogeneous topologies and systems with higher-order interactions. Crucially, SSM is a robust tipping-point predictor: even at low truncation order (e.g.,O​(2)O(2)) it reliably identifies the onset of sustained activity, while higher orders and gSSM capture post-onset amplitudes and saturation. Consistently, the reduction collapses the full network dynamics to a one-dimensional system, offering clarity and efficiency. Across all the realizations, SSM/gSSM consistently outperform classical spectral and mean-field methods in modeling critical transitions at both microscopic and macroscopic scales, establishing SSM-based reduction as a robust, interpretable tool for nonlinear networked systems with broad applicability to epidemiology, ecology, and engineered networks.

Keywords:Spectral submanifolds (SSM), Node level model reduction, Complex networks, Tipping-point prediction

## IIntroduction

Complex networked systems are fundamental to key processes in ecology, epidemiology, power engineering, and neuroscience[28,1,12,33]. Their interactions are high-dimensional and nonlinear, rendering direct analysis and large-scale simulations computationally demanding and often intractable. Dimensionality reduction is, therefore, indispensable for prediction, control, and decision-making while preserving the essential mechanisms that govern system behavior[13,21].

Existing approaches to reduce network dynamics range from mean-field and spectral projections to broader analytical and data-driven methods. Mean-field schemes provide coarse-grained, low-dimensional descriptions of system-level resilience and may capture tipping-point behavior in favorable settings, but they typically lose node-level fidelity[13,19]and do not uniformly predict critical thresholds accurately, especially in heterogeneous networks. Spectral reductions project the dynamics onto dominant eigenmodes and can reveal bifurcations and collective trends; refinements that incorporate sub-dominant modes or modular structure can enhance accuracy in heterogeneous networks[22,26,44]. General analytical frameworks further condense high-dimensional dynamics into a small set of effective variables, including treatments for heterogeneous, discrete-time, and stochastic regimes[40,42,41]. Complementary strategies combine spectral ideas with coarse-graining and adaptivity[39], use entropy-based compression for resilience[46], or employ nature-inspired optimization and data-driven prediction with limited topological information[27,32,31,11]. Recent theory also highlights low-rank structure as a foundation for reduction in complex systems[38].

Despite this progress, many reductions struggle with strongly nonlinear, heterogeneous, or node-resolved behaviors. Mean-field models compress the dynamics over global coordinates, obscuring heterogeneity and potentially misidentifying critical thresholds[13,19]. Spectral projections rely on the sufficiency of a few linear modes. Indeed, when the leading spectral gapΔ=Re⁡λ1−Re⁡λ2\Delta=\operatorname{Re}\lambda_{1}-\operatorname{Re}\lambda_{2}is small, whereλ1\lambda_{1}andλ2\lambda_{2}denote the eigenvalues with the two largest real parts, or when the dominant eigenvector is localized on high-degree hubs rather than distributed across the network, trajectories may depart from a one-mode reduced subspace and node-level errors can increase[22,26,44]. Hybrid, entropy-based, and data-driven methods can fit aggregate behavior but often lack mathematical guarantees and may generalize poorly beyond training regimes[39,46,27,32,31,11]. These limitations motivate a nonlinear, invariant, and globalizable reduction that preserves fidelity across regimes[20,40,42,41].

To address these limitations, we introduce a reduction framework based on spectral submanifolds (SSMs) and their globalized extension (gSSM). Given an equilibrium𝐱∗=𝟎\mathbf{x}^{\ast}=\mathbf{0}of𝐱˙=f​(𝐱)\dot{\mathbf{x}}=f(\mathbf{x})and a spectral subspaceEEof the linearized operatorL=D​f​(𝟎)L=Df(\mathbf{0}), a spectral submanifold (SSM) is the smoothest invariant manifoldW​(E)W(E)tangent toEEat𝐱∗\mathbf{x}^{\ast}. The dynamics on this manifold are governed by a reduced equationη˙=R​(η)\dot{\eta}=R(\eta), while the full network state is reconstructed through the lifting map𝐱=W​(η)\mathbf{x}=W(\eta). In this work, the globalized SSM (gSSM) refers to a Padé-type rational continuation of the local Taylor-series SSM reduction, introduced to extend the validity of the reduced model beyond the convergence region of its polynomial approximation. This approach is rooted in rigorous theoretical foundations and leverages scalable computational techniques for constructing invariant manifolds and their reduced dynamics[15,17]. When local Taylor-series parameterizations of an SSM yield only a limited domain of convergence, we employ Padé-type rational approximations to extend the validity domain of the reduced models significantly[20]. Recent advances in the SSM literature include explicit steady-state analyses and prediction of bifurcation structure in resonant systems[6,30,24,23], as well as data-driven extensions that recover SSMs and their reduced dynamics directly from trajectory data, enabling robust model reduction even for non-linearizable or chaotic systems[8,25]. Our main goal is to develop an equation-driven SSM/gSSM workflow that preserves the nonlinear structure of network dynamics across heterogeneous topologies, while delivering accurate node-level and macroscopic forecasts.Figure 1:Schematic of the SSM reduction pipeline for complex networks. Starting from node dynamics and topology, a spectral analysis selects a master spectral mode (more generally, a master spectral subspace) of the linearized system and constructs a low-dimensional SSM and its autonomous reduced dynamics. The lifting map reconstructs node-level trajectories and global observables, enabling robust prediction of dynamics, tipping points, and degree-class behavior across heterogeneous and higher-order networks.

Our results demonstrate that SSM/gSSM-based reductions substantially enhance predictive accuracy for both node-level trajectories and global observables across synthetic and empirical contact networks. Here, by a global observable we mean any aggregate quantity𝐲​(t)=𝒪​(𝐱​(t))\mathbf{y}(t)=\mathcal{O}(\mathbf{x}(t)), where𝒪:ℝN→ℝq\mathcal{O}:\mathbb{R}^{N}\to\mathbb{R}^{q}maps the full node-state vector to a low-dimensional summary of collective behavior; in the SIS examples below, the principal case is the mean prevalence⟨I⟩​(t)=N−1​∑i=1Nxi​(t)\langle I\rangle(t)=N^{-1}\sum_{i=1}^{N}x_{i}(t). These SSM/gSSM reductions outperform classical spectral and mean-field reductions, especially in heterogeneous settings and near critical thresholds, and remain effective in the presence of higher-order interactions (HOI). A key advantage of our approach is its parsimony: for the SIS cases studied here, the full node-level dynamics are effectively captured by a single scalar reduced coordinate on the dominant spectral submanifold, from which both global and node-wise behaviors can be reconstructed. Notably, SSM provides a robust tipping-point predictor: even at low truncation orders it accurately identifies the onset of sustained activity, while higher orders and gSSM recover post-onset amplitudes and saturation. This framework is interpretable because the reduction yields a single latent coordinate whose evolution captures the dominant collective dynamics, while the corresponding lifting map reconstructs every node’s behavior from this low-dimensional description. In this way, the model offers a transparent connection between individual node interactions and macroscopic network outcomes, supporting reliable forecasting and control of high-dimensional nonlinear systems in epidemiology, ecology, and engineered infrastructures.

The remainder of the paper is organized as follows: we first formulate the network dynamics and governing equations; next, we develop the SSM framework and its globalized variant (gSSM); we then apply the reduction to epidemic networks by the Susceptible–Infected–Susceptible (SIS) model and benchmark it against alternative methods; we extend the study to higher–order SIS dynamics with triadic interactions; and we conclude with key findings and future directions. Additional applications and full diagnostic analyses are provided in the Supplementary Material (SM)[5].

## IINetwork Dynamics and Model Reduction

## II.1Network dynamics formulation

We consider a dynamical system defined on a network with adjacency matrix𝐀\mathbf{A},x˙i=F​(xi)+∑jAi​j​G​(xi,xj),1≤i≤N,\dot{x}_{i}\;=\;F(x_{i})+\sum_{j}A_{ij}\,G(x_{i},x_{j}),\qquad 1\leq i\leq N,(1)

whereFFencodes intrinsic node dynamics,GGdescribes pairwise interactions, andAi​jA_{ij}is the(i,j)(i,j)entry of𝐀\mathbf{A}. Without loss of generality, we shift an equilibrium so thatx1=⋯=xN=0x_{1}=\cdots=x_{N}=0is an attracting fixed point of (1). For compactness, we focus on undirected graphs and assume𝐀\mathbf{A}is symmetric (extensions to directed/weighted graphs are straightforward). This compact form covers a broad class of networked systems (e.g., SIS-type epidemic, ecological, and logistic diffusion models) while keeping notation minimal for the reduction that follows. We next construct a one-dimensional reduced-order model using spectral submanifolds (SSMs) and their globalized rational extension (gSSM). For clarity and reproducibility, we summarize the general SSM/gSSM methodology in Sec.II.2, while the network-specific coefficient derivations and higher-order recursions are provided in AppendixA.

## II.2SSM/gSSM reduction method

In all examples considered in this paper, the system admits multiple equilibria, but the reduction is constructed only about the trivial equilibrium. Let𝐟:ℝN→ℝN\mathbf{f}:\mathbb{R}^{N}\to\mathbb{R}^{N}denote the network vector field and let𝐋=D​𝐟​(0)\mathbf{L}=D\mathbf{f}(0)be its linearization at the selected fixed point. In all these examples, the resulting one-dimensional SSM recovers the heteroclinic orbit connecting to the other fixed point, so the relevant nonlinear evolution is obtained from this single local construction. We compute the eigenpairs(λk,𝐯k)(\lambda_{k},\mathbf{v}_{k})of𝐋\mathbf{L}and select a master spectral subspaceE=span​{𝐯1,…,𝐯m}E=\mathrm{span}\{\mathbf{v}_{1},\dots,\mathbf{v}_{m}\}

associated with the eigenvalue(s) having the largest real part (slowest decay).

In the present study, this choice is appropriate because our objective is to approximate the slow departure from the attracting trivial equilibrium and the subsequent approach along the heteroclinic connection toward the other fixed point. When the leading eigenvalue is real and spectrally separated, this choice gives a one-dimensional master subspace. Other choices of master subspace are meaningful for different dynamical questions. For instance, in a Laplacian-coupled system near a synchronous state, if we restrict that the perturbation from the synchronous state is orthogonal to the null space of the Laplacian, an SSM constructed to the study of approaching the synchronous state would naturally be built over the weakly stable or critical transverse Laplacian modes. Likewise, near-degenerate leading spectra, complex conjugate pairs, or symmetry-breaking modes would require a higher-dimensional master subspace. This clarifies that the master-mode selection is context-dependent and chosen to capture the dominant slow dynamics relevant to the examples studied in this manuscript.

Under standard nonresonance and spectral-quotient conditions, there exists aCrC^{r}spectral submanifold (SSM)𝐖:E→ℝN\mathbf{W}:E\to\mathbb{R}^{N}tangent toEEat the origin that carries autonomous reduced dynamics𝜼˙=𝐑​(𝜼)\dot{\boldsymbol{\eta}}=\mathbf{R}(\boldsymbol{\eta})[15]. The pair(𝐖,𝐑)(\mathbf{W},\mathbf{R})is defined by the invariance equationD​𝐖​(𝜼)​𝐑​(𝜼)=𝐟​(𝐖​(𝜼)).D\mathbf{W}(\boldsymbol{\eta})\,\mathbf{R}(\boldsymbol{\eta})=\mathbf{f}\!\big(\mathbf{W}(\boldsymbol{\eta})\big).(2)

We compute(𝐖,𝐑)(\mathbf{W},\mathbf{R})via the parameterization method[17], using Taylor series expansions𝐖​(𝜼)=∑|𝜶|≥1𝐰𝜶​𝜼𝜶,𝐑​(𝜼)=𝚲​𝜼+∑|𝜶|≥2𝐫𝜶​𝜼𝜶,\mathbf{W}(\boldsymbol{\eta})=\sum_{|\boldsymbol{\alpha}|\geq 1}\mathbf{w}_{\boldsymbol{\alpha}}\,\boldsymbol{\eta}^{\boldsymbol{\alpha}},\qquad\mathbf{R}(\boldsymbol{\eta})=\boldsymbol{\Lambda}\boldsymbol{\eta}+\sum_{|\boldsymbol{\alpha}|\geq 2}\mathbf{r}_{\boldsymbol{\alpha}}\,\boldsymbol{\eta}^{\boldsymbol{\alpha}},(3)

with𝚲=diag​(λ1,…,λm)\boldsymbol{\Lambda}=\mathrm{diag}(\lambda_{1},\dots,\lambda_{m}). Matching coefficients in the invariance equation yields linear homological equations for{𝐰𝜶,𝐫𝜶}\{\mathbf{w}_{\boldsymbol{\alpha}},\mathbf{r}_{\boldsymbol{\alpha}}\}, solved order-by-order to a chosen truncation orderpp(denotedO​(p)O(p)throughout).

For the one-dimensional reductions used in the SIS examples below, the reduced coordinate𝜼\boldsymbol{\eta}reduces to a scalar coordinateη\eta. In that case, the general expansion above becomes𝐖​(η)=𝐮​η+∑k=2p𝐰k​ηk,R​(η)=λ​η+∑k=2prk​ηk.\mathbf{W}(\eta)=\mathbf{u}\eta+\sum_{k=2}^{p}\mathbf{w}_{k}\eta^{k},\qquad R(\eta)=\lambda\eta+\sum_{k=2}^{p}r_{k}\eta^{k}.

where𝐮\mathbf{u}is the leading right eigenvector,𝐰k∈ℝN\mathbf{w}_{k}\in\mathbb{R}^{N}are lifting-map coefficients, andrk∈ℝr_{k}\in\mathbb{R}are reduced-dynamics coefficients. AppendixAgives the corresponding coefficient-level homological equations for this one-dimensional case.

In all the cases used here, the dominant eigenvalue is real and sufficiently separated from the remainder of the spectrum, so a one-dimensional reduction captures the asymptotic slow dynamics accurately. This does not preclude transient improvements from higher-dimensional reductions. In particular, when the full initial condition is chosen off the reduced manifold, a two-dimensional reduction can provide a more accurate early-time approximation before both reductions approach the same long-time slow dynamics; see Sec. S1 of the SM.

A key advantage of SSM reduction is node-resolved reconstruction. Here, thelifting map𝐖\mathbf{W}is the map from the low-dimensional reduced coordinate back to the original network state space: if the intrinsic coordinateη​(t)\eta(t)evolves according toη˙=R​(η)\dot{\eta}=R(\eta)on the SSM, then the corresponding full state is recovered as𝐱​(t)=𝐖​(η​(t))\mathbf{x}(t)=\mathbf{W}(\eta(t)). In this way, the reduced dynamics are solved in a low-dimensional latent variable, while the lifting map reconstructs every nodal trajectory and hence derived global observables such as the mean prevalence⟨I⟩=N−1​∑ixi\langle I\rangle=N^{-1}\sum_{i}x_{i}. In practice, the computation of higher-order coefficients and the assembly of(𝐖,𝐑)(\mathbf{W},\mathbf{R})are automated usingSSMTool(v2.6)[18].

To enlarge validity beyond the local Taylor radius, we globalize the reduced dynamics using Padé-type rational approximants (gSSM)[20]. Specifically, we replace the truncated Taylor polynomial of the reduced vector field by a rational approximation whose series matches up to a prescribed order. Unless stated otherwise, we use a diagonal-type Padé approximant of type[8/7][8/7]constructed from the order-15 Taylor expansion of the reduced vector field; implementation details are provided in AppendixB. Next, we compare SSM-reduced model performance on recovering mean and node-level dynamics (transient as well as steady-state) in various SIS networks.

## IIIResults

We simulate the SIS dynamicsx˙i=−γ​xi+β​∑j=1NAi​j​(1−xi)​xj,\dot{x}_{i}=-\gamma x_{i}+\beta\sum_{j=1}^{N}A_{ij}(1-x_{i})\,x_{j},(4)

on networks withN=200N=200,γ=1.0\gamma=1.0,β=0.5\beta=0.5, and initialization on the dominant SSM coordinate atη0=0.01\eta_{0}=0.01. Here, the dominant SSM coordinate denotes the scalar intrinsic coordinate on the one-dimensional SSM tangent to the leading eigenvectorv1v_{1}of the linearized system, so that an aligned initial condition in the full state space is taken along the corresponding tangent direction. The valueη0=0.01\eta_{0}=0.01is a small prescribed amplitude chosen to initialize the dynamics near the selected equilibrium within the local regime of validity of the reduction, while keeping the setup consistent across all benchmark networks.
To verify robustness to initial conditions, we also tested aligned, orthogonal, and near-aligned states in the physical coordinates (seeSec. S1 of SM[5]). At the same time, additional off-manifold tests showed that a two-dimensional reduction can yield a more accurate transient prediction than a one-dimensional reduction, particularly at node level and more clearly in less homogeneous networks. For the initialization tests reported inSec. S1of the SM, the trajectories considered there converged after a brief fast transient to the same effective slow evolution, which is why the one-dimensional SSM reduction accurately captures the long-term behavior in those cases. Unless otherwise noted, we use the same network instance for each synthetic topology—Erdős–Rényi (ER), Small-World (SW), and Scale-Free (SF) models representing, respectively, homogeneous, shortcut rich - locally clustered, and heterogeneous connectivity—and the same empirical contact networks (Hospital, Workplace, Rural) across all analyses. Full construction details and network statistics are provided in theSec. S2of SM[5]. Error metrics (trajectory mean squared error, steady-state errorϵiss\epsilon_{i}^{\mathrm{ss}}) and the evaluation workflow are detailed in theSec. S3of SM[5]. To quantify reduced-model accuracy, we use two primary measures. First, for the macroscopic observable⟨I⟩​(t)\langle I\rangle(t), we define the mean-squared errorMSE⟨I⟩(p)=1M​∑m=1M(⟨I⟩^(p)​(tm)−⟨I⟩ref​(tm))2,\mathrm{MSE}_{\langle I\rangle}^{(p)}=\frac{1}{M}\sum_{m=1}^{M}\Big(\widehat{\langle I\rangle}^{(p)}(t_{m})-\langle I\rangle_{\mathrm{ref}}(t_{m})\Big)^{2},

wheretmt_{m}denotes the common comparison grid. Second, at the node level we quantify the steady-state discrepancy byϵis​s,(p)=|x^i(p)​(T)−xiref​(T)|.\epsilon_{i}^{ss,(p)}=\big|\hat{x}_{i}^{(p)}(T)-x_{i}^{\mathrm{ref}}(T)\big|.

These metrics are used throughout to assess macroscopic and node-resolved agreement; additional diagnostics are provided in Sec. S3 of the SM.Figure 2:SIS dynamics and comparison of full and reduced trajectories Erdős–Rényi (ER), Scale-Free (SF), and Small-World (SW) (N=200N{=}200,μ=1.0\mu{=}1.0,β=0.5\beta{=}0.5,η=0.01\eta{=}0.01).
(a,e,i) Representative network realizations.
(b,f,j) Node-level trajectories:O​(2)O(2)(blue) underestimates both transient and steady behavior;O​(10)O(10)(orange) isnearly indistinguishablefrom the full system (black) on ER/SW; SF requiresO​(15)O(15)–O​(20)O(20).
(c,g,k) Mean prevalence⟨I⟩\langle I\rangleshows the same ordering of accuracy.
(d,h,l)Taylor convergence plot:magenta points are zeros of the truncated radial driftaA​(ρ)a_{A}(\rho); the positive-real zero marks the predicted nonzero steady amplitude. The dashed gray circle has radiusRPR_{P}computed from the outer half of the highest-order root moduli serving as an empirical Taylor radius.Figure 3:Modular-bottleneck benchmark using a two-block stochastic block model with weak inter-community coupling.
(a) Network colored by community; the square marks a representative bridge node.
(b) Infection trajectory at the bridge node:O​(2)O(2)underestimates,O​(20)O(20)tracks the full system.
(c) Global mean prevalence⟨I⟩\langle I\rangle: low-order truncation is biased, higher-order matches well.
(d) Community-level prevalence⟨I⟩c\langle I\rangle_{c}:O​(2)O(2)underestimates block means,O​(20)O(20)recovers them closely.
Modular bottlenecks make low-order reductions less accurate, especially for bridge and community observables.

In Fig.2, we compare the full system (black) with SSM reductions at ordersO​(2)O(2)(blue),O​(10)O(10)(orange),O​(15)O(15)(pink), andO​(20)O(20)(gray), reporting accuracy for both a representative node trajectory and the mean prevalence⟨I⟩=N−1​∑ixi\langle I\rangle=N^{-1}\sum_{i}x_{i}.
Here,O​(p)O(p)denotes the truncation order of the SSM Taylor expansion, with anO​(p)O(p)–SSM reduction referring to the model truncated at orderpp. For node-level time series, the ER network shows thatO​(2)O(2)-reduced model underestimates both the transient rise and theasymptotic endemic equilibrium (steady state), whereas theO​(10)O(10)–SSM reduction converges to the full trajectory and higher-order results arenearly indistinguishable(Fig.2b). This low-order bias has a simple interpretation: theO​(2)O(2)model is only a local approximation of the SSM dynamics near the reference equilibrium, so it retains only the leading nonlinear curvature of both the reduced drift and the lifting map. In the SIS system, where the infection termAi​j​(1−xi)​xjA_{ij}(1-x_{i})x_{j}introduces amplitude-dependent saturation, the neglected higher-order terms become important once the trajectory moves away from the immediate neighborhood of the equilibrium. As a result, theO​(2)O(2)truncation tends to predict both a slower transient rise and a reduced nonzero steady amplitude.
For the SF network, at low orders (e.g.,O​(2)O(2)), the SSM-reduced model exhibits the largest underestimation relative to the full dynamics; this decreases substantially atO​(10)O(10)–O​(20)O(20)(Fig.2f). In the SW network,O​(10)O(10)-approximation reproduces the full trajectory with sufficient accuracy and any further increase in order brings negligible change (Fig.2j).

Similar accuracy trends are observed in the mean curves:O​(10)O(10)-approximations are sufficiently accurate for ER and SW networks (Fig.2c and Fig.2k), while similar accuracy is achieved atO​(15)O(15)–O​(20)O(20)in the case of SF network (Fig.2g). ER and SW networks are relatively homogeneous: most nodes have comparable numbers of links (narrow degree distribution), and the leading eigenvector is broadly distributed across nodes, a property known as delocalization. In contrast, in heterogeneous networks such as SF, the leading eigenvector becomes localized on high-degree hubs such that only a few nodes have dominant weights. This localization has a direct dynamical consequence: when activity concentrates on a few hub nodes, the effective nonlinear coupling is enhanced and the local Taylor expansion of the reduced dynamics shows slower convergence. As a result, higher-order terms of the expansion are needed to accurately represent such nonlinear interactions present in the full network. Thus, in ER and SW networks, the reduced coordinate behaves like a population average and low to moderate expansion orders already suffice for recovering the full system dynamics. In SF networks, however, higher-order Taylor expansions (or gSSM) are required for accuracy because localization on hubs effectively amplifies nonlinear effects and shrinks the radius of convergence of the SSM’s Taylor expansions. In our experience, the pattern of errors across node degrees is intuitive: at low truncation order, the reduced model captures the behavior of highly connected nodes more accurately, while discrepancies arise mainly among low-degree (peripheral) nodes. In SF networks, small residual errors can persist around hub nodes even at higher orders, but these remain within acceptable numerical tolerance (seeSec. S3of the SM[5]for detailed diagnostics).

To assess the validity of Taylor-only SSM model predictions, we perform a truncated polynomial root analysis. At each truncation orderp≤20p\leq 20, we consider the single-mode reduced dynamicsρ˙=a​(ρ)\dot{\rho}=a(\rho)and plot the complex zeros of the truncated polynomiala​(ρ)a(\rho)(Fig.2d,h,j ). Here, anon-spurious(bona fide) root means a zero that persists under increasing truncation order and remains well inside the estimated domain of convergence of the Taylor expansion, so that it can be interpreted as a genuine fixed point of the reduced dynamics. By contrast, aspuriousroot is a truncation-induced zero, typically appearing near the boundary of the convergence domain and shifting substantially withpp, and is therefore not regarded as a reliable physical prediction. Asppincreases, the spurious roots ofa​(ρ)a(\rho)cluster around the domain of convergence of the functiona​(ρ)a(\rho)and any roots inside this domain are bona fide fixed points[29]. Across all topologies, a single nontrivial transverse zeroρ1\rho_{1}persists within the estimated convergence domain ofa​(ρ)a(\rho), signaling a robust nonzero endemic level on the reduced coordinate. In ER and SW networks, a positive-real zero persists well within the root cloud asppincreases (Fig.2d,h), consistent with rapid agreement atO​(10)O(10)–O​(15)O(15)in both the transients and the steady state. In the SF network, however, a non-spurious root persists near the boundary of the convergence domain (Fig.2l), explaining the slower error decay and the utility ofO​(15)O(15)–O​(20)O(20)terms. In cases that our domain of convergence of Taylor expansions is not sufficiently large, a Padé approximant (gSSM) still captures the full trajectory and resolves the high-prevalence regime, as demonstrated in Fig.4.

## III.1Targeted modular-bottleneck benchmark

To isolate the effect of modular bottlenecks more directly, we supplement the ER, SW, and SF ensembles with a two-block stochastic block model of matched mean degree and weak inter-community coupling. This provides a controlled modular test in which transport between communities is confined to a relatively small set of bridge links. Construction details are given inSec. S2of the SM.

Figure3shows that the reduction remains accurate in this setting, although low-order truncations are more sensitive in the presence of bottlenecks. At the bridge node in Fig.3(b), theO​(2)O(2)approximation underestimates the full-system response, while theO​(20)O(20)reduction follows the full trajectory closely. The same pattern appears in the global mean prevalence in Fig.3(c): the low-order truncation still captures the epidemic level qualitatively, but with a visible bias that is much smaller at higher order.

The effect of modular structure is most evident in the community-level dynamics in Fig.3(d). TheO​(2)O(2)reduction underestimates the mean prevalence in both communities, which indicates that low-order truncation does not fully resolve the balance between intra-community growth and bridge-mediated transfer. TheO​(20)O(20)reduction, by contrast, reproduces the block-level means closely and remains consistent with the full-system trajectory throughout. These results do not suggest a qualitative failure of the SSM-based reduction on modular networks. They instead identify a topology-sensitive regime in which low-order truncations are less accurate, especially for bridge-node and community-resolved observables, whereas higher-order reductions recover both node-level and aggregate behavior reliably. Additional topology-aware diagnostics for this benchmark are reported inSec. S7of the SM.

## III.2One-parameter sweeps across synthetic and real networks

We now assess how SSM reduction captures a macroscopic observable and the tipping onset with respect to some control parameter. We varyβ/γ\beta/\gammaas our control parameter and record the final mean infection⟨I⟩\langle I\rangleacross three synthetic topologies and three empirical contact networks discussed below. In Fig.4, we compare the full system results (black) with spectral reduction (green, dotted); modified spectral reduction (magenta, dashed)[13,22,26]; and SSM reduction at different orders:O​(2)O(2)(blue),O​(10)O(10)(orange), andO​(15)O(15)(red). Implementation details for the spectral baselines are provided in the Sec. 4 of SM[5].

Synthetic networks.For the ER network (Fig.4b), all curves stay near zero for small values ofβ/γ\beta/\gammaand start increasing in a similar range (β/γ≲0.2\beta/\gamma\lesssim 0.2). Beyond this range, theO​(2)O(2)SSM reduction underestimates the steady state for high values ofβ/γ\beta/\gamma, whereas theO​(10)O(10)–O​(15)O(15)approximations accurately reproduce the full system, consistent with the nearly uniform connectivity of ER and SW networks, where nodes have similar degrees and the normalized dominant eigenvectoruuis delocalized, meaning that itsℓ2\ell^{2}mass is distributed across many nodes rather than concentrated on a small subset. Equivalently, its inverse participation ratioIPR​(u)=∑i=1Nui4\mathrm{IPR}(u)=\sum_{i=1}^{N}u_{i}^{4}(for‖u‖2=1\|u\|_{2}=1) remains comparatively small. For the SW network, the onset and subsequent growth are approximated well by all reductions (Fig.4f); higher-order SSM terms are required when the network is more heterogeneous because degree variation enhances nonlinear coupling among nodes. In SW networks this heterogeneity is moderate, and the leading eigenvector remains broadly spread across nodes, so higher-order SSM approximations reproduce the asymptotic mean infection with high accuracy. In contrast, on the SF network (Fig.4j), the spectral and the modified spectral reductions provide incorrect estimates for the tipping onset and the steady state; SSM-based estimates agree with the initial near-zero regime and correctly capture the tipping onset forβ/γ≲0.15\beta/\gamma\lesssim 0.15. WhileO​(2)O(2)-SSM predicts an incorrect bias in the steady states forβ/γ\beta/\gamma-values beyond the tipping onset, this bias is eliminated upon increasing approximation order. Indeed,O​(10)O(10)–O​(15)O(15)SSM reductions recover the final mean, indicating that higher-order nonlinear corrections are required under hub localization, consistent with the stronger nonlinear coupling described above.Figure 4:One-parameter sweeps of final mean infection⟨I⟩\langle I\rangleversusβ/γ\beta/\gamma. Synthetic networks: ER, SW, SF (e.g., panelsb,f,j); empirical networks: Hospital, Workplace, Rural (e.g., panelsd,h,l). Black: full model; green dotted: spectral; magenta dashed: modified spectral; blue/orange/red: SSMO​(2)O(2)/O​(10)O(10)/O​(15)O(15); purple markers: gSSM where included. Methods for spectral baselines are in the Sec. S4 of the SM[5].

We also evaluate SSM performance on three empirical contact networks from theSocioPatternscollaboration, Hospital, Workplace, and Rural, srepresenting healthcare, office, and community interaction settings[34,35,36]. Full dataset descriptions and preprocessing details are provided inSec. S1of the SM[5]. In the Hospital network (Fig.4d), dense connectivity leads toclose agreementamong all reduction methods over the rangeβ/γ∈(0,1)\beta/\gamma\in(0,1), except for very low-order SSM. In the Workplace network (Fig.4h), the spectral reduction underestimates the final mean infection for small values ofβ/γ\beta/\gammaand inaccurately predicts the onset, while the modified spectral variant occasionally overshoots. SSM-based reductions converge closely to the full system for intermediate values ofβ/γ\beta/\gamma, but underestimate the outcome at larger values. The Rural network (Fig.4l) exhibits the greatest variation across methods: spectral reduction misestimates the steady state overβ/γ∈(0,0.5)\beta/\gamma\in(0,0.5), and the modified spectral reduction remains inaccurate across the entire range of the control parameter. SSM reductions accurately capture the initial regime forβ/γ∈(0,0.2)\beta/\gamma\in(0,0.2)but underestimate the steady state at larger values, even at higher orders of approximation. As the Rural network displays localization, this slow convergence aligns with our earlier observations on synthetic networks regarding the limited accuracy of truncated Taylor expansions under localization. We employ the globalized SSM extension (gSSM) where necessary (purple markers), and observe good agreement with the full system across the entire range of the control parameter.Figure 5:Final mean infection⟨I⟩\langle I\rangleversusβ/γ\beta/\gammafor HOI SIS with triadic interactions on ER, SW, and SF networks. Curves: full (black), spectral (green, dotted), SSMO​(2)O(2)(gray), SSMO​(15)O(15)(blue), and gSSM (orange, dashed) where included. Spectral/closure implementation details are provided in the Sec. S5 of SM[5].

## III.3One-parameter sweep for HOI SIS with triadic interactions

Many real systems transmit influence in groups rather than pairs. For such systems, a standard modeling approach is to lift a graphAAto a simplicial complex by closing cliques (e.g., adding a 2-simplex for each triangle) and allowing transmission to depend on group participation. This framework is well established and can induce discontinuous (first-order) transitions and bistability that do not appear in purely pairwise models[16,4,3]. We adopt this construction (triangle closure to obtainTi​j​kT_{ijk}, fixed HOI strengthη\eta) and extend the SIS dynamics as:x˙i=−γ​xi+β​∑jAi​j​(1−xi)​xj+η​∑j<kTi​j​k​(1−xi)​xj​xk,\dot{x}_{i}\;=\;-\gamma x_{i}\;+\;\beta\sum_{j}A_{ij}(1-x_{i})\,x_{j}\;+\;\eta\sum_{j<k}T_{ijk}\,(1-x_{i})\,x_{j}x_{k},(5)

whereAAis the adjacency matrix,Ti​j​kT_{ijk}encodes 2-simplices (triangles), and the parameterη\etais held fixed while varyingβ/γ\beta/\gammaas the control parameter. We use the simplicial-closure construction, where every triangle inAAis lifted to a 2-simplex, following standard practice in higher-order contagion
models[16,4,3]. Additional simplicial-closure construction and parameter details are given inSec. S5of the SM[5].

On the ER network (Fig.5b), the full HOI system and the SSM results agree closely for values ofβ/γ∈(0,0.35)\beta/\gamma\in(0,0.35), capturing both onset and early growth. Beyond this range, low-order SSM underestimates the steady-state, whileO​(15)O(15)remains aligned. The spectral baseline performs reasonably at large values ofβ/γ\beta/\gammabut misses the onset and produces an overly smooth transition. On the SW network (Fig.5d), the SSM results converge to steady-state throughout:O​(2)O(2)slightly overestimates⟨I⟩\langle I\rangleforβ/γ∈(0.15,0.5)\beta/\gamma\in(0.15,0.5), whereasO​(15)O(15)(and gSSM where shown) reproduce both the knee, namely the high-curvature crossover region of the response curve⟨I⟩s​s​(β/γ)\langle I\rangle_{ss}(\beta/\gamma)marking the onset of rapid prevalence growth, and the asymptotic mean. The SF case (Fig.5f) is the most demanding: SSM reductions at all orders (and gSSM reduction) are inclose agreementwith the full model near onsetβ/γ∈(0,0.15)\beta/\gamma\in(0,0.15), butO​(2)O(2)-SSM later drifts to a false steady state; in the intermediate rangeβ/γ∈(0.2,0.6)\beta/\gamma\in(0.2,0.6),O​(15)O(15)-SSM and gSSM reproduce the full system curve, and for largerβ/γ\beta/\gammatheO​(15)O(15)-SSM overshoots the steady-state level, whereas gSSM remains accurate.

These trends reflect two mechanisms: (i) triadic reinforcement makes the response⟨I⟩s​s​(β/γ)\langle I\rangle_{ss}(\beta/\gamma)steeper and more abrupt near the transition region, which can support discontinuities and bistability; and (ii) eigenvector localization around hubs in heterogeneous graphs reduces the effectiveness of aggregate spectral projections, conditions under which higher-order SSM or gSSM reductions are advantageous[16,4,3].

## III.4Generalization beyond SIS models

Beyond SIS dynamics, our equation-driven SSM workflow applies to generalized Lotka–Volterra, gene-regulatory, and logistic–diffusion network models across ER, SW, and SF topologies. In all cases, the SSM-reduced models similarly reproduce node-level time series and macroscopic trends; full trajectories, convergence diagnostics, and comparisons against full-order simulations are provided inSec. S6of SM[5].

## IVConclusion

We developed an equation-driven reduction framework based on spectral submanifolds (SSMs) and their rational extension (gSSM) to simplify nonlinear network dynamics while preserving both node-level and system-level fidelity. Applied to synthetic and empirical contact networks, this approach consistently advanced beyond classical spectral and mean-field surrogates. On Erdős–Rényi and small-world topologies, moderate-orderO​(p)O(p)–SSM reductions (e.g.,O​(10)O(10)–O​(15)O(15)) sufficed to reproduce full trajectories and steady-state levels with high accuracy. In contrast, scale-free networks revealed the limitations of eigenvector-based reductions relative to SSMs:O​(2)O(2)-SSMs already captured the epidemic threshold (tipping point) correctly, while higher-orderO​(p)O(p)–SSM reductions or gSSM recovered the nonlinear rise and high-prevalence steady state that spectral baselines misestimated under hub localization.

A key novelty of our approach is its ability to make node-resolved prediction: the reduced coordinate, together with its lifting map, reconstructs every individual nodal trajectory alongside global observables–a capability absent in traditional spectral approaches. Also, throughout all experiments, the SSM/gSSM consistently yielded a one-dimensional reduced-order model, despite the high-dimensionality of the underlying network dynamics. This highlights both the robustness and interpretability of the proposed framework.

Extending the analysis to higher-order contagion, the triadic SIS model displayed sharper rises in prevalence and, in some regimes, discontinuous shifts in the endemic state. Here as well, SSM-based reductions consistently identified the epidemic onset tipping point, with evenO​(2)O(2)-approximations accurately identifying the tipping point despite structural heterogeneity. Quantitative agreement in the post-onset regime improved systematically with increasing polynomial order, and gSSM restored accuracy when polynomial truncations saturated for high values of the control parameter. These findings underscore SSM as a robust local predictor of tipping points and gSSM as an effective globalization tool, particularly in heterogeneous or higher-order settings. Beyond epidemic processes, the same workflow generalized seamlessly to other complex networks such as the generalized Lotka–Volterra, gene-regulation dynamics, and logistic–diffusion dynamics, where reduced models successfully reproduced both node-level and macroscopic behaviors (see Sec. S6 of the SM[5]for details).

Overall, our results establish SSM/gSSM reduction as a rigorous and broadly applicable method for nonlinear networked systems. By combining node-level reconstructions with reliable tipping-point prediction, it provides a practical bridge between mechanistic models and interpretable reduced dynamics. Immediate extensions include applying the framework to time-delayed network dynamics, where interactions depend on past states[37]. Such systems have been analyzed using invariant-manifold theory for delay differential equations, providing a natural setting to extend SSM-based reductions. Longer-term directions involve incorporating temporal variability through nonautonomous formulations[23,6], integrating uncertainty quantification via data-driven manifold inference[8,25], and scaling the methodology to high-dimensional empirical datasets. These avenues highlight the promise of SSM-based reductions as general tools for forecasting, intervention, and resilience analysis in complex biological, social, and engineered systems.

## Data availability Statement

All codes and datasets required to reproduce the results presented in this study are available atGoogle Drive Repository.
The repository contains MATLAB.mlxdashboards and scripts for all models discussed in the paper, including SIS, GLV, GRN, and logistic–diffusion systems.
Each folder includes labeled files and documentation to facilitate reproducibility of the simulations.

## Author contributions

M.L. and K.B. designed and carried out the research. K.B drafted the manuscript and produced the graphical illustrations. All authors contributed to the software development, and the review and editing of the paper.

## Acknowledgements

M.L. acknowledges financial support from the National Natural Science Foundation of China (Nos. 12302014 and 12572010). The authors also thank the anonymous reviewer for their careful reading and constructive suggestions, which substantially improved the clarity and presentation of the manuscript.

## Competing interests

The authors declare no competing interests.

## Appendix ANetwork-specific coefficient derivations and implementation details

For completeness, we collect in this Appendix the network-specific derivations of the SSM reduced dynamics used in the main text. A concise description of the general SSM/gSSM methodology (invariance equation, parameterization method, and Padé globalization) is given in Sec.II.2. Here we focus on the explicit coefficient-level derivation for the network model in Sec.A.1.

## A.1Derivation of the SSM reduced dynamics for the network model

Consider a networked dynamical system onNNnodes with state variables{xi​(t)}i=1N\{x_{i}(t)\}_{i=1}^{N}, governed byx˙i=F​(xi)+∑j=1NAi​j​G​(xi,xj),i=1,…,N,\dot{x}_{i}\;=\;F(x_{i})\,+\,\sum_{j=1}^{N}A_{ij}\,G(x_{i},x_{j}),\qquad i=1,\dots,N,(6)

where𝐀=[Ai​j]\mathbf{A}=[A_{ij}]is the adjacency matrix for an undirected graph; treatment for directed graphs is analogous.

We assume that the reduction is constructed about a selected equilibrium𝐱∗\mathbf{x}^{\ast}of the full system. After shifting coordinates so that this equilibrium is mapped to the origin, we write the shifted dynamics again in the form of Eq. (6). In the SIS-type setting considered here, this yieldsF​(0)=0F(0)=0andG​(0,0)=0G(0,0)=0, and hence the Taylor expansions below start at first order. In the more general case where the local and coupling terms do not vanish separately at the equilibrium, the same derivation applies after expanding the shifted full vector field about the translated origin.F​(x)\displaystyle F(x)=∑k≥1F(k)​xk,\displaystyle=\sum_{k\geq 1}F^{(k)}x^{k},G​(x,y)\displaystyle G(x,y)=G(1,0)​x+G(0,1)​y\displaystyle=G^{(1,0)}x+G^{(0,1)}y+∑k≥1,ℓ≥1G(k,ℓ)​xk​yℓ.\displaystyle\quad+\sum_{k\geq 1,\;\ell\geq 1}G^{(k,\ell)}x^{k}y^{\ell}.(7)

Collecting terms gives the vector form𝐱˙=𝐀^​𝐱+∑k≥2F(k)​𝐱k+∑k≥1,ℓ≥1G(k,ℓ)​𝐱k∗(𝐀​𝐱ℓ),\dot{\mathbf{x}}\;=\;\hat{\mathbf{A}}\,\mathbf{x}\;+\;\sum_{k\geq 2}F^{(k)}\,\mathbf{x}^{k}\;+\;\sum_{k\geq 1,\;\ell\geq 1}G^{(k,\ell)}\;\mathbf{x}^{k}*\big(\mathbf{A}\,\mathbf{x}^{\ell}\big),(8)

where(𝐱k)i=xik(\mathbf{x}^{k})_{i}=x_{i}^{k},∗*is the Hadamard (element-wise) product, and𝐀^=\displaystyle\hat{\mathbf{A}}\;=F(1)​𝐈+G(1,0)​𝐃+G(0,1)​𝐀,\displaystyle\;F^{(1)}\mathbf{I}\;+\;G^{(1,0)}\mathbf{D}\;+\;G^{(0,1)}\mathbf{A},𝐃=\displaystyle\mathbf{D}=diag​(d1,…,dN),di=∑jAi​j.\displaystyle\;\mathrm{diag}(d_{1},\dots,d_{N}),\;d_{i}=\sum_{j}A_{ij}.

Let(λ,𝐮)(\lambda,\mathbf{u})be the leading eigenpair of𝐀^\hat{\mathbf{A}}, i.e.,λ\lambdais the eigenvalue with the largest real part. For the undirected networks considered in this derivation, we normalize the eigenvector as𝐮⊤​𝐮=1\mathbf{u}^{\top}\mathbf{u}=1and use the graph-style gauge𝐮⊤​𝐰k=0\mathbf{u}^{\top}\mathbf{w}_{k}=0for all higher-order lifting coefficientsk≥2k\geq 2. Under generic nonresonance with the remaining spectrum[15], we obtain the existence and uniqueness of a one-dimensional SSM tangent tospan​{𝐮}\mathrm{span}\{\mathbf{u}\}at the origin.

We parametrize this one-dimensional SSM using the same notation as in the main text. Thus, the scalar intrinsic coordinate is denoted byη∈ℝ\eta\in\mathbb{R}, the lifting map is𝐖​(η)\mathbf{W}(\eta), and the autonomous reduced dynamics are denoted byR​(η)R(\eta). In the present one-dimensional setting, the general SSM representationη˙=R​(η)\dot{\eta}=R(\eta)and𝐱=𝐖​(η)\mathbf{x}=\mathbf{W}(\eta)takes the Taylor form𝐖​(η)\displaystyle\mathbf{W}(\eta)=𝐮​η+∑k≥2𝐰k​ηk,\displaystyle=\mathbf{u}\,\eta+\sum_{k\geq 2}\mathbf{w}_{k}\,\eta^{k},(9)R​(η)\displaystyle R(\eta)=λ​η+∑k≥2rk​ηk.\displaystyle=\lambda\,\eta+\sum_{k\geq 2}r_{k}\,\eta^{k}.

Here,𝐰k∈ℝN\mathbf{w}_{k}\in\mathbb{R}^{N}are the coefficients of the lifting map andrk∈ℝr_{k}\in\mathbb{R}are the coefficients of the scalar reduced dynamics. This notation is the one-dimensional specialization of the expansion used in Sec.II.2.

Substituting Eq. (9) into Eq. (6), or equivalently into Eq. (8), gives the invariance equationD​𝐖​(η)​R​(η)=\displaystyle\mathrm{D}\mathbf{W}(\eta)\,R(\eta)\;=𝐀^​𝐖​(η)+∑k≥2F(k)​𝐖​(η)k\displaystyle\;\hat{\mathbf{A}}\,\mathbf{W}(\eta)\;+\;\sum_{k\geq 2}F^{(k)}\,\mathbf{W}(\eta)^{k}+∑k≥1,ℓ≥1G(k,ℓ)​𝐖​(η)k∗(𝐀​𝐖​(η)ℓ),\displaystyle\;+\;\sum_{k\geq 1,\;\ell\geq 1}G^{(k,\ell)}\;\mathbf{W}(\eta)^{k}*\big(\mathbf{A}\,\mathbf{W}(\eta)^{\ell}\big),

which can be solved recursively for increasing powers ofη\etato determine the unknown coefficients{𝐰k}\{\mathbf{w}_{k}\}and{rk}\{r_{k}\}in an automated fashion[18]. We provide the explicit solution up to cubic order below.

## Orderη1\eta^{1}.

This yields𝐀^​𝐮=λ​𝐮\hat{\mathbf{A}}\mathbf{u}=\lambda\mathbf{u}by construction.

## Orderη2\eta^{2}.

Collecting allη2\eta^{2}terms givesr2​𝐮+2​λ​𝐰2=\displaystyle r_{2}\,\mathbf{u}\;+2\lambda\,\mathbf{w}_{2}\;=𝐀^​𝐰2+F(2)​𝐮2\displaystyle\;\hat{\mathbf{A}}\,\mathbf{w}_{2}\;+\;F^{(2)}\,\mathbf{u}^{2}(10)+G(1,1)​𝐮∗(𝐀𝐮).\displaystyle\;+\;G^{(1,1)}\,\mathbf{u}*\big(\mathbf{A}\mathbf{u}\big).

Projecting onto𝐮⊤\mathbf{u}^{\top}fixes the reduced coefficientr2=\displaystyle r_{2}\;=F(2)​𝐮⊤​𝐮2+G(1,1)​𝐮⊤​(𝐮∗(𝐀𝐮)),\displaystyle\;F^{(2)}\,\mathbf{u}^{\top}\mathbf{u}^{2}\;+\;G^{(1,1)}\,\mathbf{u}^{\top}\big(\mathbf{u}*(\mathbf{A}\mathbf{u})\big),(11)

after which the second-order lifting coefficient𝐰2\mathbf{w}_{2}follows from𝐰2=\displaystyle\mathbf{w}_{2}\;=(𝐀^−2λ𝐈)−1[r2𝐮−F(2)𝐮2\displaystyle\;\big(\hat{\mathbf{A}}-2\lambda\,\mathbf{I}\big)^{-1}\left[\,r_{2}\,\mathbf{u}\;-\;F^{(2)}\,\mathbf{u}^{2}\right.(12)−G(1,1)𝐮∗(𝐀𝐮)].\displaystyle\left.\qquad\qquad-\;G^{(1,1)}\,\mathbf{u}*(\mathbf{A}\mathbf{u})\,\right].

## Orderη3\eta^{3}.

Collectingη3\eta^{3}terms yieldsr3​𝐮+3​λ​𝐰3+2​𝐰2​r2=𝐀^​𝐰3+2​F(2)​𝐮∗𝐰2+F(3)​𝐮3+G(1,1)​(𝐮∗(𝐀𝐰2)+𝐰2∗(𝐀𝐮))+G(1,2)​𝐮∗(𝐀𝐮2)+G(2,1)​𝐮2∗(𝐀𝐮).\begin{split}r_{3}\,\mathbf{u}\;+\;3\lambda\,\mathbf{w}_{3}\;+\;2\,\mathbf{w}_{2}\,r_{2}\;=\;&\;\hat{\mathbf{A}}\,\mathbf{w}_{3}\\
&\;+\;2F^{(2)}\,\mathbf{u}*\mathbf{w}_{2}\;+\;F^{(3)}\,\mathbf{u}^{3}\\
&\;+\;G^{(1,1)}\!\Big(\mathbf{u}*(\mathbf{A}\mathbf{w}_{2})+\mathbf{w}_{2}*(\mathbf{A}\mathbf{u})\Big)\\
&\;+\;G^{(1,2)}\,\mathbf{u}*(\mathbf{A}\mathbf{u}^{2})\\
&\;+\;G^{(2,1)}\,\mathbf{u}^{2}*(\mathbf{A}\mathbf{u}).\end{split}(13)

Projecting onto𝐮⊤\mathbf{u}^{\top}givesr3=𝐮⊤[−2𝐰2r2+2F(2)𝐮∗𝐰2+F(3)𝐮3+G(1,1)(𝐮∗(𝐀𝐰2)+𝐰2∗(𝐀𝐮))]+𝐮⊤​[G(1,2)​𝐮∗(𝐀𝐮2)+G(2,1)​𝐮2∗(𝐀𝐮)].\begin{split}r_{3}\;=\;&\;\mathbf{u}^{\top}\!\Big[-2\,\mathbf{w}_{2}\,r_{2}\;+\;2F^{(2)}\,\mathbf{u}*\mathbf{w}_{2}\;+\;F^{(3)}\,\mathbf{u}^{3}\\
&\qquad\qquad\;\;+\;G^{(1,1)}\!\Big(\mathbf{u}*(\mathbf{A}\mathbf{w}_{2})+\mathbf{w}_{2}*(\mathbf{A}\mathbf{u})\Big)\Big]\\
&\;+\;\mathbf{u}^{\top}\!\Big[G^{(1,2)}\,\mathbf{u}*(\mathbf{A}\mathbf{u}^{2})\;+\;G^{(2,1)}\,\mathbf{u}^{2}*(\mathbf{A}\mathbf{u})\Big].\end{split}(14)

and then𝐰3=(𝐀^−3λ𝐈)−1[r3𝐮+2𝐰2r2−2F(2)𝐮∗𝐰2−F(3)​𝐮3−G(1,1)​(𝐮∗(𝐀𝐰2)+𝐰2∗(𝐀𝐮))−G(1,2)𝐮∗(𝐀𝐮2)−G(2,1)𝐮2∗(𝐀𝐮)].\begin{split}\mathbf{w}_{3}\;=\;&\;\big(\hat{\mathbf{A}}-3\lambda\,\mathbf{I}\big)^{-1}\!\Big[r_{3}\,\mathbf{u}+2\,\mathbf{w}_{2}\,r_{2}-2F^{(2)}\,\mathbf{u}*\mathbf{w}_{2}\\
&\qquad\quad-F^{(3)}\,\mathbf{u}^{3}-G^{(1,1)}\!\Big(\mathbf{u}*(\mathbf{A}\mathbf{w}_{2})+\mathbf{w}_{2}*(\mathbf{A}\mathbf{u})\Big)\\
&\qquad\quad-G^{(1,2)}\,\mathbf{u}*(\mathbf{A}\mathbf{u}^{2})-G^{(2,1)}\,\mathbf{u}^{2}*(\mathbf{A}\mathbf{u})\Big].\end{split}(15)

Proceeding inductively, theηk\eta^{k}balance yields a linear homological problem for the unknown lifting coefficient𝐰k\mathbf{w}_{k}and reduced coefficientrkr_{k}. The lower-order coefficients{𝐰j}j<k\{\mathbf{w}_{j}\}_{j<k}and{rj}j<k\{r_{j}\}_{j<k}determine the known forcing terms at orderkk; projection onto the master direction fixesrkr_{k}, and the remaining component determines𝐰k\mathbf{w}_{k}on the complementary subspace.
In practice one truncates (9) at orderpp, obtainingR​(η)\displaystyle R(\eta)=λ​η+r2​η2+⋯+rp​ηp,\displaystyle=\lambda\eta+r_{2}\eta^{2}+\cdots+r_{p}\eta^{p},𝐖​(η)\displaystyle\mathbf{W}(\eta)=𝐮​η+𝐰2​η2+⋯+𝐰p​ηp.\displaystyle=\mathbf{u}\eta+\mathbf{w}_{2}\eta^{2}+\cdots+\mathbf{w}_{p}\eta^{p}.

Quadratic truncation already yields a closed-form prediction forη​(t)\eta(t)and the nontrivial fixed levelη∞=−λ/r2\eta_{\infty}=-\lambda/r_{2}whenλ>0\lambda>0andr2≠0r_{2}\neq 0; higher orders improve quantitative accuracy and extend the local validity.
Throughout this work, we denote byppthe truncation order of the Taylor expansion used in the SSM construction, e.g.,O​(2)O(2),O​(5)O(5),O​(10)O(10),O​(15)O(15), orO​(20)O(20), and refer to each case as the correspondingO​(p)O(p)–SSM reduction.

All coefficient solves above are linear and sparse once𝐀^\hat{\mathbf{A}}and the coefficients of nonlinearities are assembled. We rely on a graph-style parameterization (no re-centering) and compute{𝐰k}\{\mathbf{w}_{k}\}and{rk}\{r_{k}\}up to orderppvia order-by-order homological solves. For automating these computations, we have employed the MATLAB-based packageSSMTool[18]that enables scalable SSM computations in physical coordinates with minimal eigenvectors, and provides diagnostics for spectral gaps and internal resonances.

## Appendix BGlobalization of invariant manifolds via Padé approximation

This Appendix provides implementation-level details for the gSSM construction summarized in Sec.II.2. A classical strategy for analytic continuation of a function near a specific point is its Padé approximant, which replaces a truncated Taylor series by a rational function capable of representing singularities that limit the convergence of pure polynomials. In our setting, the reduced dynamics on an SSM, computed upto any desired order, are extended by constructing a rational approximation of the form[20]F^​(z)=∑|α|≤Naα​zα1+∑|β|≤Mbβ​zβ,b0=1,z∈ℝℓ,\widehat{F}(z)\;=\;\frac{\sum_{|\alpha|\leq N}a_{\alpha}z^{\alpha}}{\,1+\sum_{|\beta|\leq M}b_{\beta}z^{\beta}},\qquad b_{0}=1,\quad z\in\mathbb{R}^{\ell},(16)

where the numerator and the denominator are multivariate polynomials of chosen degreesNNandMM. The coefficients are fixed so that the series ofF^\widehat{F}matches the Taylor expansion of the reduced dynamics up to orderN+MN+M. This construction applies to both univariate and multivariate cases.

Diagonal Padé approximants[M/M][M/M], in which numerator and denominator have the same degree, are particularly effective and are closely related to continued–fraction representations in the univariate case[45,2,9]. For meromorphic functions with unknown pole structure, classical convergence results (e.g., de Montessus–type theorems and modern refinements) ensure that appropriate Padé sequences converge almost everywhere on compact sets, with exceptions corresponding to the zero sets of the denominator[10,2,7]. Analogous constructions and guarantees extend to multivariate and vector settings via rational/vector Padé frameworks[14,2,9]. We adopt this theory in our context and use the data–driven globalization strategy in[20].

We use this procedure to obtain globalized SSMs (gSSMs): the local Taylor coefficients from the invariance equation are preserved near the origin, while the rational form extends the validity of the reduced dynamics far beyond the Taylor radius. Throughout this work, unless noted otherwise, we adopt diagonal Padé approximants of type[8/7][8/7]constructed from the order-15 Taylor expansion of the reduced vector field. This choice has proven effective in balancing accuracy and robustness across all network models studied.

Supplemental Material for “Nonlinear Model Reduction of Complex Networks via Spectral Submanifolds”
Kaviya Bhaskaran, Shobhit Jain, Mingwu Li

## Appendix S1Effect of initialization: aligned, orthogonal, and near-aligned comparisons

In Fig.S1, we examine how different initialization strategies
influence the transient and long-term dynamics on an Erdős–Rényi network.
All simulations use the same model parameters and reduced orderO​(20)O(20)as in the
main text. We prepared three representative initial conditions using the same
notation as in main text.

We therefore refer to the three cases as:
- (i)

Aligned initialization(dominantly on the slow manifold),𝐳0(A)=η0​𝐯1\mathbf{z}_{0}^{(\mathrm{A})}=\eta_{0}\mathbf{v}_{1}, where𝐯1\mathbf{v}_{1}is
the leading right eigenvector of the linearized operator, tangent to the
one-dimensional SSM.
- (ii)

Orthogonal initialization(transverse to the slow manifold),𝐳0(B)=η0​𝐫\mathbf{z}_{0}^{(\mathrm{B})}=\eta_{0}\mathbf{r}, where𝐫⟂𝐯1\mathbf{r}\perp\mathbf{v}_{1}is chosen to be Euclidean-orthogonal to the
manifold tangent direction.
- (iii)

Near-aligned initialization(slightly displaced from the manifold),𝐳0(C)=η0​𝐯1+ε​𝐫\mathbf{z}_{0}^{(\mathrm{C})}=\eta_{0}\mathbf{v}_{1}+\varepsilon\mathbf{r},
representing a state close to the slow manifold but perturbed by a small
orthogonal component withε≪η0\varepsilon\ll\eta_{0}.Figure S1:Effect of initialization on the reduced dynamics.(a) Erdős–Rényi network withN=200N=200nodes and throughout all three simulations, theη0\eta_{0}was initialized as1.51.5.
(b) Representative node trajectoryI84​(t)I_{84}(t)for the full system launched
from the aligned state (solid black), compared with reducedO​(20)O(20)SSM
trajectories initialized on the manifold (solid blue), from an off-manifold
projection (dashed orange), and from a small-shift projection (dash–dotted
magenta). (c) Mean prevalence⟨I⟩​(t)\langle I\rangle(t)under the same color
scheme. The reduced trajectories reproduce the slow dynamics accurately
after the initial contraction, demonstrating the SSM’s robustness to
initialization choices while clarifying that the early fast transient is
inherently absent from the reduced model.

The full system was integrated only from the aligned state𝐳0(A)\mathbf{z}_{0}^{(\mathrm{A})}, while the reduced dynamics on theO​(20)O(20)SSM were launched from the three reduced coordinates corresponding to
cases (i)–(iii) above, i.e., either directly fromq0q_{0}or from the projections
of𝐳0(B)\mathbf{z}_{0}^{(\mathrm{B})}and𝐳0(C)\mathbf{z}_{0}^{(\mathrm{C})}onto the
slow coordinate. The network layout fig.S1(a), representative node-level
trajectoryIi∗​(t)I_{i^{*}}(t)fig.S1(b), and mean prevalence⟨I⟩​(t)\langle I\rangle(t)fig.S1(c) are shown for comparison.

The blue curves, corresponding to the aligned initialization, show that
the full and reduced trajectories overlap from the start, indicating
that the initial state lies entirely on the slow manifold governed by
the dominant SSM coordinateη\eta.
The orange trajectories, corresponding to the orthogonal
initialization, exhibit a clear delay in activation: the state initially
evolves along fast stable directions before relaxing toward the slow
subspace, resulting in a later onset of infection growth.
The magenta curves, representing the near-aligned initialization,
display only a short transient deviation before converging to the same
trajectory as the aligned case, confirming that small displacements from
the manifold have minimal long-term influence.

The dash–dotted SSM trajectories in each color family start directly on
the manifold and thus do not capture the early fast contraction phase,
but they accurately reproduce the slow evolution once the transient
subsides.
After this short alignment period, all reduced and full trajectories
coincide on the same slow-manifold path.
These results demonstrate that the one-dimensional SSM reliably captures
the long-term network dynamics while clarifying that the fast-mode
relaxation observed in the full system governs only the brief early-time
approach to𝒲SSM\mathcal{W}_{\mathrm{SSM}}.Figure S2:(a) Erdős–Rényi network withN=200N=200nodes. The full initial condition is prescribed directly in physical coordinates and displaced from the reduced manifold by a perturbation along a third mode, while the reduced initial coordinates are obtained by projection onto them=1m=1andm=2m=2modal subspaces. (b) Representative node-level trajectoryIi​(t)I_{i}(t)for the full system (solid black), compared with them=1m=1reduced trajectory (dashed blue) and them=2m=2reduced trajectory (dash–dotted orange). The two-dimensional reduction yields a more accurate early-time approximation than the one-dimensional reduction, although the improvement is modest in the ER case. (c) Mean prevalence⟨I⟩​(t)\langle I\rangle(t)under the same color scheme. At the macroscopic level, the difference between them=1m=1andm=2m=2reductions is largely suppressed by averaging. In all cases, both reduced trajectories approach the same long-time slow dynamics and recover the same steady behavior as the full system.Figure S3:(a) Two-block SBM withN=200N=200nodes. As in Fig.S2, the full initial condition is prescribed directly in physical coordinates and displaced from the reduced manifold by a perturbation along a third mode, while the reduced initial coordinates are obtained by projection onto them=1m=1andm=2m=2modal subspaces. (b) Representative node-level trajectoryIi​(t)I_{i}(t)for the full system (solid black), compared with them=1m=1reduced trajectory (dashed blue) and them=2m=2reduced trajectory (dash–dotted orange). In this more modular and less homogeneous setting, the transient benefit of them=2m=2reduction is more pronounced than in the ER case. (c) Mean prevalence⟨I⟩​(t)\langle I\rangle(t)under the same color scheme. The difference between them=1m=1andm=2m=2reductions is smaller than at node level but remains consistent with the stronger transient role of the second mode in the modular network. At longer times, both reduced trajectories converge to the same slow dynamics and recover the same steady behavior as the full system.

## S1.1Off-manifold initialization and transient benefit ofm=2m=2

In this subsection, we examine whether increasing the reduced dimension fromm=1m=1tom=2m=2improves transient prediction when the full initial condition is chosen off the reduced manifold. This directly addresses the question of whether higher-dimensional reductions provide a measurable benefit beyond the asymptotic one-dimensional slow dynamics emphasized in the main text.

For this test, we considered both an Erdős–Rényi (ER) network and a two-block stochastic block model (SBM). In each case, we first constructed a two-dimensional base state from the leading two modal directions and then displaced the full initial condition off the reduced manifold by adding a perturbation along a third mode. Thus, the full-state initial condition was prescribed directly in physical coordinates and was not restricted to lie on either the one- or two-dimensional reduced manifold. The reduced initial coordinates were then obtained by projection of this same full-state initial condition onto the corresponding one-dimensional and two-dimensional modal subspaces. Consequently, the comparison tests how well them=1m=1andm=2m=2reductions reproduce the transient evolution from the same off-manifold physical state.

Figures S2 and S3 summarize the resulting comparisons. Figure S2 reports the ER case, while Fig. S3 reports the two-block SBM case. In each figure, panel (a) shows the network topology, panel (b) shows a representative node-level trajectory, and panel (c) shows the mean prevalence. The representative node was chosen so that the contribution of the second mode is appreciable, making the transient difference between them=1m=1andm=2m=2reductions visible at node level.

The main observation is that them=2m=2reduction yields a more accurate early-time approximation than them=1m=1reduction. In the ER network (Fig. S2), this improvement is relatively modest and is clearest in the node-level trajectory: them=2m=2curve stays closer to the full system during the initial transient, whereas in the mean prevalence the difference between the two reductions is largely suppressed by averaging. In the SBM network (Fig. S3), the transient benefit ofm=2m=2is more pronounced. Here the modular structure makes the second mode more dynamically relevant, so them=2m=2reduction provides a visibly better approximation thanm=1m=1during the approach to the slow manifold.

At the same time, these tests confirm that the long-time behavior remains effectively one-dimensional for the cases considered here. Althoughm=2m=2improves the transient approximation, both them=1m=1andm=2m=2reductions eventually merge with the same slow dynamics and recover the same steady behavior as the full system. Thus, the role ofm=2m=2in these examples is not to change the asymptotic prediction, but to improve short-time accuracy under off-manifold initialization. This explains why the one-dimensional reductions remain sufficient for the main manuscript figures, while the additionalm=2m=2results are most naturally presented as a supplementary transient test. In summary, these additional results show that higher-dimensional reductions can be beneficial when the full system is initialized away from the reduced manifold, and that this effect is most clearly visible at node level and in less homogeneous networks.

## Appendix S2Network construction, preprocessing, and numerical setup

## S2.1Synthetic topologies.

All experiments use undirected, unweighted, simple graphs onN=200N=200nodes with no self-loops. We consider three canonical ensembles:(i) Erdős–Rényi (ER):each unordered pair is present independently with probabilityp=2​KN−1p=\tfrac{2K}{N-1}, yielding expected degree≈2​K\approx 2K; we useK=4K=4(so𝔼​[deg]≈8\mathbb{E}[\mathrm{deg}]\approx 8).(ii) Scale-free (SF):a target degree sequence is sampled from a truncated power law with exponentγ=3\gamma=3; a configuration-model pairing of stubs produces a simple graph, followed by a minimal connectivity fix (if multiple components occur, we connect each to the largest component by a single edge).(iii) Small-world (SW):a ring lattice with2​Kneigh2K_{\text{neigh}}nearest neighbors (we useKneigh=4K_{\text{neigh}}=4for mean degree88) is rewired with probabilityprew=0.10p_{\text{rew}}=0.10per existing edge (Watts–Strogatz–like).
For the targeted modular-bottleneck benchmark introduced in the revised manuscript, we additionally consider a two-block stochastic block model (SBM) with equal community sizesN/2N/2and matched expected mean degree. Writingpout=ρ​pinp_{\mathrm{out}}=\rho\,p_{\mathrm{in}}withρ<1\rho<1for the inter- to intra-community connection ratio, we choosepinp_{\mathrm{in}}so that(N/2−1)​pin+(N/2)​pout≈8(N/2-1)p_{\mathrm{in}}+(N/2)p_{\mathrm{out}}\approx 8, and then fixρ\rhoto obtain weak inter-community coupling and hence a clearly bottlenecked modular structure.
Adjacency matricesAAare symmetric{0,1}\{0,1\}-valued.

## S2.2Empirical networks (SocioPatterns).

We use three real contact networks from the SocioPatterns collaboration: (i) a hospital ward in Lyon, France (Dec. 6–10, 2010), recording face-to-face proximity among patients and health-care workers; (ii) an office building in France (Jun. 24–Jul. 3, 2013), capturing workplace contacts; and (iii) a rural village in Malawi, providing observational contact data at the household/community scale.
For each dataset, we symmetrize and binarize the temporal edges over the observation window and analyze the largest connected component.
The hospital data span 46 health-care workers and 29 patients over∼\sim72 hours, as documented in the released metadata.
Dataset details and access: Hospital ward, Workplace, and Rural Malawi (SocioPatterns). Temporal SocioPatterns edge lists are first aggregated into static weighted adjacency matrices by summing contact durations (or counts). These matrices are then symmetrized, binarized, and restricted to the largest connected component before performing theβ\beta–sweeps.111SocioPatterns datasets: Hospital ward (Lyon, 2010)[34];
Workplace (France, 2013)[35];
Rural Malawi village[36].
Hospital participant counts from the CRAN mirror of the SocioPatterns documentation[43].Table S1:Global numerical settings used in all simulations.ItemDescriptionValue / noteTime horizonSimulation timetft_{f}, samplestf∈[20,100]t_{f}\in[20,100];nsteps=103n_{\text{steps}}=10^{3}–1.5×1031.5\times 10^{3}SSM ordersTaylor truncationsO​(2),O​(5),O​(10),O​(15),O​(20)O(2),\,O(5),\,O(10),\,O(15),\,O(20)InitializationAlong dominant eigenvectorη0∈[0.01,0.05]\eta_{0}\in[0.01,0.05]IntegratorSolverMATLABode45, default tolerancesNetworksRealizationsFixed per topology, reused in all tests

## S2.3Global numerical settings

All models share the same numerical setup for time-integration and reduction.
These global settings are listed in TableS1.
For consistent comparisons, the same network realizations were used across all experiments.

## Appendix S3Error metrics for SIS time series (full vs. SSM)

## Setup and notation.

Let{tm}m=1M⊂[0,T]\{t_{m}\}_{m=1}^{M}\subset[0,T]be the common time grid used for comparisons.
The trajectory of nodeiiin the full system is denotedxiref​(tm)x_{i}^{\mathrm{ref}}(t_{m}), while the reduced dynamics trajectory on anO​(p)O(p)–SSM reduction isx^i(p)​(tm)\hat{x}_{i}^{(p)}(t_{m}), obtained by interpolation over the same grid.
The mean prevalence is⟨I⟩​(t)=1N​∑i=1Nxi​(t),\langle I\rangle(t)=\frac{1}{N}\sum_{i=1}^{N}x_{i}(t),

with reduced counterpart⟨I⟩^(p)​(t)\widehat{\langle I\rangle}^{(p)}(t).
The degree of nodeiiiski=∑jAi​jk_{i}=\sum_{j}A_{ij}. To evaluate the accuracy of theO​(p)O(p)–SSM reductions, we employ five complementary metrics:

1.Macroscopic mean-squared error (MSE): Mean error vs. order.This measures the mean-squared difference between the reduced and full-system prevalence curves,MSE⟨I⟩(p)=1M​∑m=1M(⟨I⟩^(p)​(tm)−⟨I⟩ref​(tm))2.\mathrm{MSE}_{\langle I\rangle}^{(p)}=\frac{1}{M}\sum_{m=1}^{M}\Big(\widehat{\langle I\rangle}^{(p)}(t_{m})-\langle I\rangle^{\mathrm{ref}}(t_{m})\Big)^{2}.

MSE⟨I⟩(p)\mathrm{MSE}_{\langle I\rangle}^{(p)}quantifies how well the reduced dynamics captures the global infection level; decreasing values with increasingppindicate systematic convergence.

2.Degree–error relation.For any nodeii, we compute the absolute steady-state error,ϵiss,(p)=|x^i(p)​(T)−xiref​(T)|,\epsilon_{i}^{\mathrm{ss},(p)}=\bigl|\hat{x}_{i}^{(p)}(T)-x_{i}^{\mathrm{ref}}(T)\bigr|,

and plot it against the node degreekik_{i}. This shows whether errors are concentrated in low-degree nodes (often harder to approximate) or spread more uniformly across the network.

3.Nodewise steady-state distribution.The values forϵiss,(p)\epsilon_{i}^{\mathrm{ss},(p)}above are summarized across all nodes as boxplots for each orderpp. This provides a compact view of how the distribution of steady-state errors tightens with increasing SSM order.

4.Time-to-steady-state (TSS).We define the relaxation time as the point when the trajectories remain within a fixed toleranceτ\tauof their final steady state. For the full and reduced systems,TSSfull=min⁡{t:1N​∑i=1N|xiref​(t)−xi,∞ref|≤τ},\mathrm{TSS}_{\mathrm{full}}=\min\Bigl\{t:\tfrac{1}{N}\sum_{i=1}^{N}|x_{i}^{\mathrm{ref}}(t)-x_{i,\infty}^{\mathrm{ref}}|\leq\tau\Bigr\},TSSred(p)=min⁡{t:1N​∑i=1N|x^i(p)​(t)−x^i,∞(p)|≤τ}.\mathrm{TSS}_{\mathrm{red}}^{(p)}=\min\Bigl\{t:\tfrac{1}{N}\sum_{i=1}^{N}|\hat{x}_{i}^{(p)}(t)-\hat{x}_{i,\infty}^{(p)}|\leq\tau\Bigr\}.

Comparing these times indicates how well theO​(p)O(p)–SSM reduction reproduces the transient convergence rate of the full system.

5.Global MAE and spatial correlation.The global mean absolute error (MAE) is defined asMAE(p)=1M​N​∑m=1M∑i=1N|x^i(p)​(tm)−xiref​(tm)|,\mathrm{MAE}^{(p)}=\frac{1}{MN}\sum_{m=1}^{M}\sum_{i=1}^{N}\big|\hat{x}_{i}^{(p)}(t_{m})-x_{i}^{\mathrm{ref}}(t_{m})\big|,

while the spatial correlation compares steady-state values node-by-node asCorrsp(p)=corr​(𝐱^(p)​(T),𝐱ref​(T)).\mathrm{Corr}^{(p)}_{\mathrm{sp}}=\mathrm{corr}\!\bigl(\hat{\mathbf{x}}^{(p)}(T),\,\mathbf{x}^{\mathrm{ref}}(T)\bigr).

Together, these capture both the overall trajectory accuracy and whether the final spatial pattern across nodes is faithfully reproduced.

These metrics collectively evaluate our reduced models over multiple scales: the global prevalence curve (MSE), node-level steady states (degree–error and distributions), transient relaxation (TSS), and overall fidelity across time and space (MAE and correlation). All metrics are computed on the same network instances, with reduced trajectories reconstructed viaW(p)W^{(p)}to node-level coordinates and then resampled onto the full-system time grid for consistency.Figure S4:ER error diagnostics.(a) Network layout.
(b) Degree distribution.
(c) Mean-prevalence MSE vs.O​(p)O(p)–SSM order.
(d) Steady-state node errorϵiss\epsilon_{i}^{\mathrm{ss}}vs. degreekik_{i}, shown as scatter points in dark blue (O​(2)O(2)), orange (O​(10)O(10)), blue (O​(15)O(15)), and pink (O​(20)O(20)).
(e) Boxcharts ofϵiss\epsilon_{i}^{\mathrm{ss}}grouped by order.
(f) Time-to-steady-state:TSSred\mathrm{TSS}_{\mathrm{red}}vs.TSSfull\mathrm{TSS}_{\mathrm{full}}, using the same color scheme as panel (d).
(g) Global MAE (blue bars, left axis) and steady-state spatial correlation (orange line, right axis) vs. order.
(h) Time–order error surfaceE(p)​(t)E^{(p)}(t)with colormap representing residual error values.Figure S5:SF error diagnostics.(a) Network layout.
(b) Degree distribution.
(c) Mean-prevalence MSE vs.O​(p)O(p)–SSM order.
(d) Steady-state node errorϵiss\epsilon_{i}^{\mathrm{ss}}vs. degreekik_{i}, shown as scatter points in dark blue (O​(2)O(2)), orange (O​(10)O(10)), blue (O​(15)O(15)), and pink (O​(20)O(20)).
(e) Boxcharts ofϵiss\epsilon_{i}^{\mathrm{ss}}grouped by order.
(f) Time-to-steady-state:TSSred\mathrm{TSS}_{\mathrm{red}}vs.TSSfull\mathrm{TSS}_{\mathrm{full}}, using the same color scheme as panel (d).
(g) Global MAE (blue bars, left axis) and steady-state spatial correlation (orange line, right axis) vs. order.
(h) Time–order error surfaceE(p)​(t)E^{(p)}(t)with colormap representing residual error values.Figure S6:SW error diagnostics.(a) Network layout.
(b) Degree distribution.
(c) Mean-prevalence MSE vs.O​(p)O(p)–SSM order.
(d) Steady-state node errorϵiss\epsilon_{i}^{\mathrm{ss}}vs. degreekik_{i}, shown as scatter points in dark blue (O​(2)O(2)), orange (O​(10)O(10)), blue (O​(15)O(15)), and pink (O​(20)O(20)).
(e) Boxcharts ofϵiss\epsilon_{i}^{\mathrm{ss}}grouped by order.
(f) Time-to-steady-state:TSSred\mathrm{TSS}_{\mathrm{red}}vs.TSSfull\mathrm{TSS}_{\mathrm{full}}, using the same color scheme as panel (d).
(g) Global MAE (blue bars, left axis) and steady-state spatial correlation (orange line, right axis) vs. order.
(h) Time–order error surfaceE(p)​(t)E^{(p)}(t)with colormap representing residual error values.

## Erdős–Rényi (ER): error diagnostics.

In the ER case, the network structure shown in Fig.S4a is visually homogeneous, and the degree histogram in panel (b) confirms this by displaying a narrow, unimodal distribution centered near the mean degree. This structural regularity is reflected in the accuracy of theO​(p)O(p)–SSM reductions. The macroscopic error in the mean prevalence (panel c) decreases almost monotonically with increasingpp, dropping by nearly two orders of magnitude betweenO​(2)O(2)andO​(20)O(20). ByO​(10)O(10), theO​(p)O(p)–SSM reduction already reproduces the full mean dynamics with negligible deviation, indicating that only moderate order is needed for accurate system-level predictions.

At the node level, steady-state errors are strongly anti-correlated with degree (panel d): low-degree nodes carry the bulk of the residual at low order, whereas high-degree nodes are approximated more faithfully from the start. This scatter decays rapidly with increasingpp, and byO​(15)O(15)–O​(20)O(20)the errors are nearly uniform across nodes. The same trend appears in the distribution of final errors across all nodes (panel e): medians fall, interquartile ranges narrow, and outliers disappear with increasing order, demonstrating progressively tighter fidelity.

Dynamical relaxation is also well captured at moderate orders. The time-to-steady-state comparison in panel (f) shows that the lowest-order model (O​(2)O(2)–SSM) relaxes slightly faster than the full system, while higher orders fall directly on the diagonal, confirming that the reduced and full models converge on the same timescale. At the global level (panel g), the mean absolute error decreases steadily with order, while the steady-state spatial correlation approaches unity, showing that both overall levels and cross-node patterns are faithfully reproduced. Finally, the error surface in panel (h) reveals where discrepancies persist: they are concentrated in early transients at low order and vanish almost entirely at higher orders. Together, these diagnostics demonstrate that the structural homogeneity of ER networks and the delocalization of their dominant spectral modes allow theO​(p)O(p)–SSM reduction to rapidly converge. Moderate orders such asO​(10)O(10)are sufficient to recover both macroscopic observables and detailed node-level behavior with high accuracy.

## Scale–Free (SF): error diagnostics.

In the SF case, the network layout in Fig.S5a clearly reveals hub nodes, and the heavy-tailed degree distribution in panel (b) confirms strong structural heterogeneity. This variability directly affects model reduction. The macroscopic error in the mean prevalence (panel c) decreases withO​(p)O(p)–SSM order, dropping by roughly an order of magnitude byO​(10)O(10), but then levels off, reflecting slower convergence compared to the ER network due to the influence of hubs and peripheral nodes.

At the node level, steady-state error versus degree (panel d) shows a strong anti-correlation: low-degree peripheral nodes carry the largest residuals at low order, while the scatter progressively decays towards zero at higher orders. Small residuals can persist even for hubs, but they remain bounded and diminish with order. The overall distribution of steady-state errors (panel e) narrows as the order increases, with reduced medians and spread, though the distribution remains broader than in the ER case, consistent with the heavy-tailed topology.

Dynamical convergence is also topology-dependent. The time-to-steady-state analysis (panel f) shows that the lowest-orderO​(2)O(2)–SSM relaxes too quickly relative to the full system, while higher orders (O​(10)O(10)–O​(20)O(20)) align more closely with the diagonal, correcting the relaxation time bias. At the global scale (panel g), the mean absolute error steadily decreases with order, and the spatial correlation between full and reduced steady states rises to≈0.98\approx 0.98–1.001.00by mid-to-high orders, confirming that both global levels and cross-node structures are recovered. The error surface in panel (h) localizes most discrepancies to early transients at low order, with little error persisting once the order is increased.

Overall, the strong heterogeneity of SF networks slows the rate of Taylor-order convergence and makes low-degree nodes the most challenging to approximate. Nonetheless, by moderate-to-high orders, theO​(p)O(p)–SSM reductions accurately reproduce both macroscopic trends and node-level patterns, offering robust fidelity even in heavy-tailed topologies.

## Small–World (SW): error diagnostics.

In the SW network, the layout in Fig.S6a highlights clustered connectivity with a few shortcuts, while the narrow degree distribution in panel (b) indicates only mild heterogeneity. This structure favors efficient reduction. The macroscopic error in the mean prevalence (panel c) decreases rapidly with order: from about10−310^{-3}atO​(2)O(2)to below10−610^{-6}byO​(15)O(15)–O​(20)O(20), withO​(10)O(10)–SSM reductions already nearly indistinguishable from the full system. At the node level, steady-state error versus degree (panel d) is small across all nodes and loses its weak degree dependence as the order increases; correspondingly, the overall distribution of errors (panel e) becomes tighter, with lower medians and reduced spread.

Dynamically, the time-to-steady-state analysis (panel f) shows thatO​(2)O(2)–SSM relaxes slightly too quickly, while higher orders (O​(15)O(15)–O​(20)O(20)) fall close to the diagonal, reflecting accurate reproduction of relaxation times. Global error metrics reinforce this picture: the mean absolute error falls steadily with order, and the spatial correlation between reduced and full steady states (panel g) approaches unity by mid order, confirming that both overall levels and cross-node structure are well preserved. The error surface in panel (h) localizes residual discrepancies to early transients at low order, which vanish as the order increases. Together, these diagnostics illustrate that the moderate heterogeneity and delocalized modes of SW networks make them particularly well suited forO​(p)O(p)–SSM reduction: accurate node-level and system-level dynamics are already achieved at moderate orders, with little to gain beyondO​(10)O(10).

## Appendix S4Spectral and modified spectral baselines

This section summarizes the two eigenmode-based baselines used in theβ/γ\beta/\gammasweeps: a classicalspectralreduction and amodified
spectralvariant. Both project the SIS dynamics onto a one-dimensional
macroscopic variable aligned with an eigenvector of the adjacency matrixAAand
produce an explicit prediction for the final mean infection⟨I⟩\langle I\rangleas a function ofβ/γ\beta/\gamma. The implementations below corresponds to the spectral reductions in the literature[13,22,26].

## Spectral.[13]

Letλ1\lambda_{1}andu(1)u^{(1)}denote the dominant eigenvalue and the
corresponding right eigenvector ofAA(largest real part). Define the
degree vectork=(k1,…,kN)⊤k=(k_{1},\dots,k_{N})^{\top}withki=∑jAi​jk_{i}=\sum_{j}A_{ij}and the
normalized weightsa=u(1)𝟏⊤​u(1),b=a⊙a𝟏⊤​(a⊙a),a\;=\;\frac{u^{(1)}}{\mathbf{1}^{\top}u^{(1)}},\qquad b\;=\;\frac{a\odot a}{\mathbf{1}^{\top}(a\odot a)}\,,

where⊙\odotdenotes elementwise multiplication and𝟏\mathbf{1}is the
all-ones vector. A degree-weighted factorβ^s=k⊤​bk⊤​a\widehat{\beta}_{s}\;=\;\frac{k^{\top}b}{k^{\top}a}

rescales the macroscopic projection. The resulting
spectral prediction for the final mean infection is⟨I⟩^spec​(β/γ)=max⁡{0,1−1(β/γ)​λ1​β^s}.\widehat{\langle I\rangle}_{\mathrm{spec}}(\beta/\gamma)\;=\;\max\!\left\{\,0,\;1-\frac{1}{(\beta/\gamma)\,\lambda_{1}\,\widehat{\beta}_{s}}\right\}.(S1)

The linear onset is then(β/γ)c=1/λ1(\beta/\gamma)_{c}=1/\lambda_{1};β^s\widehat{\beta}_{s}affects the saturation level but not the threshold.

## Modified spectral.[22,26].

In heterogeneous graphs, the leading eigenvector may be localized around hubs.
To mitigate this, we scan eigenpairs{(λi,u(i))}\{(\lambda_{i},u^{(i)})\}and choose the
indexi⋆i^{\star}that minimizes a degree–eigenvector mismatch score,i⋆=arg⁡mini​∑n=1N(kn−λi)2​(un(i))2,i^{\star}\;=\;\arg\min_{i}\sum_{n=1}^{N}\bigl(k_{n}-\lambda_{i}\bigr)^{2}\,\bigl(u^{(i)}_{n}\bigr)^{2},

which favors less localized modes. Using the selected
eigenvalueλi⋆\lambda_{i^{\star}}, the modified spectral prediction is⟨I⟩^mod​(β/γ)=max⁡{0,1−1(β/γ)​λi⋆}.\widehat{\langle I\rangle}_{\mathrm{mod}}(\beta/\gamma)\;=\;\max\!\left\{\,0,\;1-\frac{1}{(\beta/\gamma)\,\lambda_{i^{\star}}}\right\}.(S2)

Here(β/γ)c=1/λi⋆(\beta/\gamma)_{c}=1/\lambda_{i^{\star}}, and the saturation level follows
directly from the same expression.

For eachβ\beta, we evaluate (S1) and
(S2) and compare them to the full SIS simulations and
SSM/gSSM reductions. On near-homogeneous topologies (e.g., ER, SW), the
dominant eigenvector is delocalized and both baselines track the sweep well.
On heavy-tailed graphs (e.g., SF), eigenvector localization shifts the effective
coupling toward hubs, causing threshold and plateau biases; the anti-localization
choice in the modified spectral baseline partly alleviates this, but SSM/gSSM
consistently provide more accurate node- and system-level predictions in our tests.

## Appendix S5Higher–order (triadic) SIS: mathematical implementation and parameters

In this work, higher–order effects are implemented viasimplicial (triangle) closureof the pairwise contact network. Starting from the adjacency matrix𝐀=[Ai​j]\mathbf{A}=[A_{ij}], we identify all triangles (3-cliques){i,j,k}\{i,j,k\}in the underlying graph and encode them by the third-order indicator tensorTi​j​kT_{ijk}:Ti​j​k={1,if​{i,j,k}​forms a triangle in​𝐀,0,otherwise,Ti​j​k=Ti​k​j=Tj​i​k=⋯T_{ijk}=\begin{cases}1,&\text{if }\{i,j,k\}\ \text{forms a triangle in }\mathbf{A},\\
0,&\text{otherwise},\end{cases}\qquad T_{ijk}=T_{ikj}=T_{jik}=\cdots

(i.e.,Ti​j​kT_{ijk}is symmetric in its indices). The higher–order SIS dynamics used throughout the manuscript arex˙i=−γ​xi+β​∑j=1NAi​j​(1−xi)​xj+η​∑j<kTi​j​k​(1−xi)​xj​xk,i=1,…,N,\dot{x}_{i}\;=\;-\gamma\,x_{i}\;+\;\beta\sum_{j=1}^{N}A_{ij}\,(1-x_{i})\,x_{j}\;+\;\eta\sum_{j<k}T_{ijk}\,(1-x_{i})\,x_{j}x_{k},\qquad i=1,\dots,N,(S3)

whereγ\gammais the recovery rate,β\betais the pairwise transmission rate, andη\etacontrols the strength of triadic reinforcement. The restrictionj<kj<kavoids double counting of unordered pairs within each triangle.

This simplicial-closure construction is a standard modeling choice for higher–order contagion and can generate discontinuous transitions and bistability that are absent in purely pairwise SIS dynamics[16,4,3]. Unless stated otherwise, all higher–order SIS simulations in the main text use Eq. (S3) withTi​j​kT_{ijk}obtained from triangle closure of the corresponding𝐀\mathbf{A}. We hold the higher–order strengthη\etafixed while varyingβ/γ\beta/\gammaas the control parameter (consistent with the manuscript). The remaining parameter choices are summarized in TableS2.Table S2:Parameters for the HOI SIS (triadic) model.SymbolMeaningValue / ruleβ\betaPairwise transmission rateSweep inβ/γ\beta/\gammaγ\gammaRecovery rate1.01.0η\etaTriadic infection strength1.01.0AAAdjacency matrixFixed per topologyTi​j​kT_{ijk}Triangle tensorClique closure ofAAhih_{i}Triad load of nodeii#​{(j,k):Ti​j​k=1}\#\{(j,k):T_{ijk}=1\}NNNumber of nodes200200

## Appendix S6Other examples

## S6.1Generalized Lotka–Volterra (GLV)

We model a facilitative GLV system on a graph with adjacency matrixAA:N˙i=r​Ni+m​∑j=1NAi​j​Nj+α​Ni​∑j=1NAi​j​Nj−c​Ni2,1≤i≤N,\begin{split}\dot{N}_{i}=\;&r\,N_{i}\;+\;m\sum_{j=1}^{N}A_{ij}\,N_{j}\\
&\;+\;\alpha\,N_{i}\sum_{j=1}^{N}A_{ij}\,N_{j}\;-\;c\,N_{i}^{2},\qquad 1\leq i\leq N,\end{split}(S4)

whererris the intrinsic growth rate,mmis a linear dispersal or immigration term from neighbors,α\alphais the strength of pairwise facilitation (mutualistic gain), andc>0c>0represents intraspecific self-regulation (density dependence).Figure S7:Generalized Lotka–Volterra dynamics on an Erdős–Rényi network.(a) Network layout withN=200N=200nodes.
(b) Representative node abundanceN84​(t)N_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions withp∈{2,10,15,20}p\in\{2,10,15,20\}(colors as shown).
(c) Mean abundance⟨N⟩​(t)=N−1​∑iNi\langle N\rangle(t)=N^{-1}\sum_{i}N_{i}with the same color scheme.
(d) Root diagnostic from the scalar amplitude functiona​(ρ)a(\rho): brighter shades denote higherpp, with the highest-order roots highlighted in magenta.
(e) Mean-squared error (MSE) of⟨N⟩​(t)\langle N\rangle(t)versuspp, showing near-geometric decay.
(f) Degree versus steady-state errorϵiss\epsilon_{i}^{\mathrm{ss}}, with scatter points colored bypp.
Moderatepp(e.g.,O​(10)O(10)) reproduces both node-level and macroscopic dynamics with high fidelity, whileO​(2)O(2)systematically underestimates the equilibrium.Figure S8:Generalized Lotka–Volterra dynamics on a Scale-Free network.(a) Network layout withN=200N=200nodes.
(b) Representative node abundanceN84​(t)N_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions withp∈{2,10,15,20}p\in\{2,10,15,20\}.
(c) Mean abundance⟨N⟩​(t)=N−1​∑iNi\langle N\rangle(t)=N^{-1}\sum_{i}N_{i}.
(d) Root diagnostic froma​(ρ)a(\rho): brighter shades denote higherpp, with the highest-order roots highlighted in magenta.
(e) MSE of⟨N⟩​(t)\langle N\rangle(t)versuspp, showing slower decay than in ER/SW.
(f) Degree versusϵiss\epsilon_{i}^{\mathrm{ss}}colored bypp.
Higher orders (O​(15)O(15)–O​(20)O(20)) are required to fully recover both node- and system-level dynamics due to hub localization and a smaller Taylor radius.Figure S9:Generalized Lotka–Volterra dynamics on a Small-World network.(a) Network layout withN=200N=200nodes.
(b) Representative node abundanceN84​(t)N_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions withp∈{2,10,15,20}p\in\{2,10,15,20\}.
(c) Mean abundance⟨N⟩​(t)=N−1​∑iNi\langle N\rangle(t)=N^{-1}\sum_{i}N_{i}.
(d) Root diagnostic froma​(ρ)a(\rho): brighter shades denote higherpp, with the highest-order roots highlighted in magenta.
(e) MSE of⟨N⟩​(t)\langle N\rangle(t)versuspp, showing rapid decay byO​(10)O(10).
(f) Degree versusϵiss\epsilon_{i}^{\mathrm{ss}}colored bypp.
ByO​(10)O(10), both node-level and macroscopic trajectories are nearly indistinguishable from the full dynamics, with uniformly small errors across degrees.Figure S10:Gene–regulatory dynamics on an Erdős–Rényi network.(a) Network layout withN=200N=200nodes.
(b) Representative node activationx84​(t)x_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions (p∈{2,5,10,15,20}p\in\{2,5,10,15,20\}; colors as shown).
(c) Mean activation⟨x⟩​(t)=N−1​∑ixi​(t)\langle x\rangle(t)=N^{-1}\sum_{i}x_{i}(t).
(d) Root diagnostic froma​(ρ)a(\rho): brighter shades denote higherpp, with the highest order roots highlighted in magenta.
(e) MSE of⟨x⟩​(t)\langle x\rangle(t)versuspp, showing near-geometric decay.
(f) Degree versusϵiss\epsilon_{i}^{\mathrm{ss}}colored bypp.
Moderateppreproduces node-level and macroscopic dynamics with high fidelity;O​(2)O(2)underestimates the equilibrium.Figure S11:Gene–regulatory dynamics on a Small-World network.(a) Network layout withN=200N=200nodes.
(b) Representative node activationx84​(t)x_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions (p∈{2,10,15,20}p\in\{2,10,15,20\}).
(c) Mean activation⟨x⟩​(t)=N−1​∑ixi​(t)\langle x\rangle(t)=N^{-1}\sum_{i}x_{i}(t).
(d) Root diagnostic froma​(ρ)a(\rho): brighter shades denote higherpp, with the highest order roots highlighted in magenta.
(e) MSE of⟨x⟩​(t)\langle x\rangle(t)versuspp, showing near-geometric decay.
(f) Degree versusϵiss\epsilon_{i}^{\mathrm{ss}}colored bypp.
ByO​(10)O(10), both node- and system-level dynamics are reproduced with negligible deviation.Figure S12:Gene–regulatory dynamics on a Scale-Free network.(a) Network layout withN=200N=200nodes.
(b) Representative node activationx84​(t)x_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions (p∈{2,10,15,20}p\in\{2,10,15,20\}).
(c) Mean activation⟨x⟩​(t)=N−1​∑i​xi​(t)\langle x\rangle(t)=N^{-1}\sum i\,x_{i}(t).
(d) Root diagnostic froma​(ρ)a(\rho): brighter shades denote higherpp, with the highest order roots highlighted in magenta.
(e) MSE of⟨x⟩​(t)\langle x\rangle(t)versuspp.
(f) Degree versusϵiss\epsilon_{i}^{\mathrm{ss}}colored bypp.
Higherpp(1515–2020) yields nearly indistinguishable trajectories from the full system despite strong heterogeneity.Figure S13:Logistic growth with diffusive coupling on an Erdős–Rényi network.(a) Network layout withN=200N=200nodes.
(b) Representative node activationx84​(t)x_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions (p∈{2,5,10,15,20}p\in\{2,5,10,15,20\}; colors as shown).
(c) Mean activation⟨x⟩​(t)=N−1​∑ixi​(t)\langle x\rangle(t)=N^{-1}\sum_{i}x_{i}(t).
(d) Root diagnostic froma​(ρ)a(\rho): brighter shades denote higherpp, with the highest-order roots highlighted in magenta.
(e) MSE of⟨x⟩​(t)\langle x\rangle(t)remains negligible at∼10−8\sim 10^{-8}across allpp.
(f) Degree versusϵiss\epsilon_{i}^{\mathrm{ss}}colored bypp.
Across all considered orders, theO​(p)O(p)–SSM reductions reproduce the full-system trajectories with negligible deviation at both node and system scales.Figure S14:Logistic growth with diffusive coupling on a Small-World network.(a) Network layout withN=200N=200nodes.
(b) Representative node activationx84​(t)x_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions (p∈{2,5,10,15,20}p\in\{2,5,10,15,20\}).
(c) Mean activation⟨x⟩​(t)=N−1​∑ixi​(t)\langle x\rangle(t)=N^{-1}\sum_{i}x_{i}(t).
(d) Root diagnostic froma​(ρ)a(\rho): brighter shades denote higherpp, with the highest-order roots highlighted in magenta.
(e) MSE of⟨x⟩​(t)\langle x\rangle(t)versuspp, flat at∼10−8\sim 10^{-8}.
(f) Degree versusϵiss\epsilon_{i}^{\mathrm{ss}}colored bypp.
AllO​(p)O(p)–SSM reductions track the full system without discernible error.Figure S15:Logistic growth with diffusive coupling on a Scale-Free network.(a) Network layout withN=200N=200nodes.
(b) Representative node activationx84​(t)x_{84}(t)for the full system (black) andO​(p)O(p)–SSM reductions (p∈{2,5,10,15,20}p\in\{2,5,10,15,20\}).
(c) Mean activation⟨x⟩​(t)=N−1​∑ixi​(t)\langle x\rangle(t)=N^{-1}\sum_{i}x_{i}(t).
(d) Root diagnostic froma​(ρ)a(\rho): brighter shades denote higherpp, with the highest-order roots highlighted in magenta.
(e) MSE of⟨x⟩​(t)\langle x\rangle(t)versuspp, flat at∼10−8\sim 10^{-8}.
(f) Degree versusϵiss\epsilon_{i}^{\mathrm{ss}}colored bypp.
Diffusion suppresses localization; evenO​(2)O(2)yields trajectories that are nearly indistinguishable from the full system at both node and system levels.

Unless noted otherwise, we follow a common protocol across topologies:N=200N=200nodes,O​(p)O(p)–SSM reductions withp∈{2,10,15,20}p\in\{2,10,15,20\}, initialization of the reduced coordinate atq0=0.01q_{0}=0.01along the dominant eigenvector, and a final simulation horizontf=60t_{f}=60. We compare full trajectories withO​(p)O(p)–SSM reductions at both the node level and the mean abundance⟨N⟩=N−1​∑iNi\langle N\rangle=N^{-1}\sum_{i}N_{i}. The parameters used are summarized in TableS3.Table S3:GLV parameters used across experiments.SymbolMeaningValue usedrrintrinsic growth rate0.200.20mmlinear coupling (dispersal)0.050.05α\alphapairwise facilitation strength0.050.05ccself–limitation (saturation)1.001.00AAadjacencyfixed per topologyNNnumber of nodes200200

## Results across topologies.

In the Erdős–Rényi network (Fig.S7a–f), the representative node trajectory in panel (b) and the mean abundance in panel (c) reveal thatO​(2)O(2)captures the qualitative rise and saturation but settles below the true equilibrium. AtO​(10)O(10), the reduced dynamics are nearly indistinguishable from the full system, andO​(15)O(15)–O​(20)O(20)bring no visible change. The root diagnostic in panel (d) supports this rapid convergence: the highest-order zeros lie well inside a wide annulus, consistent with the near–geometric decay of the mean error in panel (e). The steady-state error in panel (f) concentrates among low-degree nodes at low order but collapses toward zero asppincreases.

The scale-free network (Fig.S8a–f) presents a more stringent test. Panels (b,c) show visible bias atO​(2)O(2)andO​(10)O(10), whileO​(15)O(15)–O​(20)O(20)recover the correct levels. The roots in panel (d) cluster nearer the outer boundary, indicating a reduced analyticity margin for Taylor expansions and explaining slower convergence. Correspondingly, panel (e) shows more gradual MSE decay, though still improving by several orders of magnitude byO​(20)O(20). Degree–error scatter in panel (f) confirms that low-degree nodes are hardest at low order, whereas hubs align well by mid order.

For the Small-World network (Fig.S9a–f), convergence is fast:O​(10)O(10)suffices to match both node-level and mean trajectories; higher orders add only marginal refinements. The roots in panel (d) show a stable positive-real zero well within a broad annulus, aligning with the sharp MSE drop fromO​(2)O(2)toO​(10)O(10)in panel (e). ByO​(15)O(15), degree–error scatter in panel (f) is uniformly small across all degrees.

Overall, ER and SW networks are accurately represented with moderatepp, while SF networks benefit from higherppto resolve localized dynamics. Root maps anticipate these convergence patterns, and degree–error plots highlight where residual inaccuracies may persist.

## S6.2Gene–regulatory (activation–repression) dynamics

## Equation.

We consider a simple gene–regulatory network model capturing activation and repression effects between connected nodes. Each node represents a gene whose activation levelxi​(t)x_{i}(t)evolves according to the balance of decay, activation, and inhibition processes described byx˙i=−μ​xi+γ​∑j=1NAi​j​xj−b​xi2−krep​∑j=1NAi​j​xi​xj,i=1,…,N.\begin{split}\dot{x}_{i}=\;&-\mu\,x_{i}\;+\;\gamma\sum_{j=1}^{N}A_{ij}x_{j}\;-\;b\,x_{i}^{2}\\
&\;-\;k_{\mathrm{rep}}\sum_{j=1}^{N}A_{ij}x_{i}x_{j},\qquad i=1,\dots,N.\end{split}(S5)

The parameters and their values used in the simulations are summarized in TableS4.Table S4:GRN activation–repression parameters.SymbolMeaningValue usedμ\muDegradation / decay0.200.20γ\gammaLinear activation gain0.0600.060bbLocal self–saturation0.800.80krepk_{\mathrm{rep}}Pairwise repression strength0.0400.040AAAdjacencyFixed per topologyNNNumber of nodes200200

## Results across topologies.

For the Erdős–Rényi (ER) network in Fig.S10, the representative node trajectory in panel (b) and the mean activation in panel (c) illustrate thatO​(2)O(2)captures the qualitative trend but settles at a slightly lower steady level than the full system. ByO​(10)O(10), the reduced dynamics are effectively indistinguishable from the reference trajectory, andO​(15)O(15)–O​(20)O(20)bring no visible change, confirming rapid convergence. The roots map in panel (d) shows a clear and persistent positive–real zero of the amplitude function located comfortably inside a broad annulus of complex roots, aligning with the near–geometric decay of the mean–prevalence MSE in panel (e). The degree–error plot in panel (f) confirms that residuals at low order are largely confined to low–degree nodes; byO​(10)O(10), errors are small and uniformly distributed.

The Small–World (SW) case in Fig.S11shows a similar pattern but with even faster convergence. Panels (b,c) demonstrate thatO​(10)O(10)suffices to replicate both node–level and mean trajectories, with higher orders adding only negligible refinements. The root map in panel (d) shows a wide analyticity margin surrounding the persistent positive–real zero, consistent with the sharp drop inMSE​(⟨x⟩)\mathrm{MSE}(\langle x\rangle)betweenO​(2)O(2)andO​(10)O(10)in panel (e). The degree–error scatter in panel (f) is tightly banded byO​(10)O(10), indicating nearly uniform accuracy across degrees.

The Scale–Free (SF) topology in Fig.S12presents a sharper challenge. Panels (b,c) show that atO​(2)O(2)the reduced trajectories significantly underestimate both node–level and mean steady states. Increasing toO​(10)O(10)reduces this bias, and byO​(15)O(15)–O​(20)O(20)theO​(p)O(p)–SSM curves are nearly indistinguishable from the full dynamics, though convergence is visibly slower than in ER or SW. The root map in panel (d) explains this behavior: dominant zeros of the amplitude function cluster closer to the outer boundary, indicating a smaller effective Taylor radius and slower MSE decay in panel (e). The degree–error scatter in panel (f) shows residuals concentrated among low–degree nodes at low order; asppincreases, nodewise errors diminish substantially across the degree spectrum.

Taken together, ER and SW networks are accurately captured by mid–orderO​(p)O(p)–SSM (p≈10p\approx 10), while SF networks benefit from higherpp(1515–2020) to resolve localized dynamics. In all cases, the persistent positive–real zero of the amplitude function serves as a compact reliability check for the Taylor–only reduction.

## S6.3Logistic growth with diffusive coupling

We study logistic growth with diffusion on a graph with adjacency matrixAAand LaplacianL=diag​(deg)−AL=\mathrm{diag}(\deg)-A, wheredeg\degdenotes the node-degree vector whoseiith entry iski=∑jAi​jk_{i}=\sum_{j}A_{ij}. The governing dynamics arex˙i=r​xi​(1−xiK)+D​∑j=1NLi​j​xj,1≤i≤N,\dot{x}_{i}\;=\;r\,x_{i}\!\left(1-\frac{x_{i}}{K}\right)\;+\;D\sum_{j=1}^{N}L_{ij}\,x_{j},\qquad 1\leq i\leq N,(S6)

wherexi​(t)∈[0,K]x_{i}(t)\in[0,K]is the state at nodeii. We construct reduced models on a single-mode SSM at ordersO​(2)O(2),O​(5)O(5),O​(10)O(10),O​(15)O(15), andO​(20)O(20), and perform time integration initialized on the SSM.Table S5:Logistic–diffusion parameters.SymbolMeaningValue usedrrLogistic growth rate1.01.0KKCarrying capacity1.01.0DDDiffusion coefficient0.050.05AAAdjacencyFixed per topologyNNNumber of nodes200200

## Results across topologies.

For the Erdős–Rényi case (Fig.S13a–f), the representative node trajectory in panel (b) and the mean abundance in panel (c) are visually indistinguishable between the full system and allO​(p)O(p)–SSM reductions, even atO​(2)O(2). The root diagnostic in panel (d) shows a large domain of analyticity with a stable positive-real zero persisting well within the domain. Consistent with this observation, the MSE of the macroscopic observable (panel e) remains negligible at∼10−8\sim 10^{-8}for all orders. Degree-resolved errors (panel f) are similarly negligible, confirming uniform accuracy across all nodes.

The Small-World case (Fig.S14a–f) exhibits the same behavior. Node-level trajectories (panel b) and the mean dynamics (panel c) are nearly identical for the full and reduced systems. The roots in panel (d) again form a wide, regular annulus; the macroscopic error curve (panel e) stays at the numerical floor; and steady-state errors (panel f) vanish across degrees.

For the heterogeneous Scale-Free network (Fig.S15a–f), diffusion suppresses localization effects. Panels (b,c) show that full and reduced trajectories remain nearly indistinguishable across allpp. The root map in panel (d) indicates a comfortable analytic buffer; the mean error in panel (e) remains flat at the numerical floor; and degree-wise errors (panel f) are near machine precision.

Together, these results show that diffusion homogenizes the dynamics across the network, collapsing them onto a single smooth mode. Consequently, even the lowest-orderO​(2)O(2)–SSM suffices to reproduce both transient and steady-state dynamics with full fidelity, regardless of topology.
For the logistic–diffusion model, we verified analytically that all higher–order SSM coefficients vanish (ck=0c_{k}=0fork≥3k\geq 3), yielding an exact quadratic reduced dynamicsq˙=r​q−(r/K)​(∑iui3)​q2\dot{q}=rq-(r/K)\,(\sum_{i}u_{i}^{3})q^{2}.
Consequently, theO​(2)O(2)–SSM reduction reproduces the full system exactly, consistent with the numerical results reported above.Figure S16:Full topology-aware diagnostics for the modular stochastic-block-model benchmark.(a) Two-block modular SBM realization, with nodes colored by community; the marked circle denotes a representative bridge node and the marked square denotes a representative core node.
(b) Representative core-node trajectoryI85​(t)I_{85}(t)for the full system andO​(p)O(p)–SSM reductions withp∈{2,10,15,20}p\in\{2,10,15,20\}.
(c) Representative bridge-node trajectoryI9​(t)I_{9}(t)under the same comparison.
(d) Global mean prevalence⟨I⟩​(t)\langle I\rangle(t).
(e) Community-resolved mean prevalence⟨I⟩c​(t)\langle I\rangle_{c}(t)in the two blocks.
(f) Mean-squared error of the global mean and the average block mean versus SSM order.
(g) Steady-state nodewise errorϵiss\epsilon_{i}^{\mathrm{ss}}versus degree.
(h) Steady-state nodewise errorϵiss\epsilon_{i}^{\mathrm{ss}}versus bridge scorekiout/kik_{i}^{\mathrm{out}}/k_{i}.
The benchmark shows that modular bottlenecks do not induce a qualitative breakdown of the reduction, but they do make low-order truncations more sensitive, especially in bridge-mediated and community-resolved observables; increasing the order fromO​(2)O(2)toO​(20)O(20)strongly suppresses these errors.

## Appendix S7Modular stochastic-block-model benchmark

To examine modular structure in a controlled setting, we supplement the ER, SW, and SF ensembles with a two-block stochastic block model (SBM) with matched mean degree and weak inter-community coupling. The purpose of this benchmark is to isolate modular bottlenecks, which are not directly prescribed by the ER, SW, and SF constructions. The network is built under the same conventions as in Sec. S2.1: undirected, unweighted, simple graphs onN=200N=200nodes, with equal-size communities and no self-loops. We match the expected mean degree to the main synthetic benchmarks and choose the ratio of inter-community to intra-community connection probabilities so as to obtain a clearly bottlenecked modular structure. Unless noted otherwise, the SIS dynamics, initialization protocol, time integration, andO​(p)O(p)–SSM truncation orders are the same as in the main-text SIS experiments, and the error metrics follow Sec. S3.

FigureS16shows the full set of diagnostics for this modular benchmark and complements the condensed figure in the main text. Panel (a) displays a representative two-block realization with dense intra-community connectivity and a relatively sparse set of inter-community links. Inter-community transport is therefore constrained to a small set of bridge nodes, making this a more direct test of modular bottlenecks than the SW ensemble.

Panels (b) and (c) show the node-level dynamics. The reduction remains accurate in this setting, but the effect of truncation order is more visible than in the better-connected cases. For the representative core node in panel (b), theO​(2)O(2)reduction underestimates the endemic level, while the higher-order reductions, particularlyO​(15)O(15)andO​(20)O(20), track the full trajectory closely. Panel (c) shows the same pattern for a representative bridge node in a form that is more directly tied to the modular structure: theO​(2)O(2)approximation again underestimates the response, whereas theO​(20)O(20)reduction nearly overlaps with the full-system trajectory. The modular bottleneck therefore does not lead to a qualitative breakdown at the node level, but it does make low-order truncations more sensitive.

This dependence on order also appears in the aggregate observables. In panel (d), the global mean prevalence is captured qualitatively even at low order, but theO​(2)O(2)reduction remains visibly biased. Increasing the order reduces this bias substantially, and theO​(20)O(20)reduction reproduces the full mean prevalence closely. Panel (e) makes the modular effect more explicit through the community-resolved mean dynamics. There, theO​(2)O(2)reduction underestimates the mean prevalence in both communities, which indicates that low-order truncation does not fully represent the balance between intra-community growth and bridge-mediated transfer. TheO​(20)O(20)reduction, by contrast, reproduces the block-level means closely throughout the trajectory.

Panel (f) quantifies the improvement with order. The MSE of the global mean and the average block mean both drop sharply as the truncation order increases fromO​(2)O(2)toO​(10)O(10), followed by a smaller but still clear improvement fromO​(10)O(10)toO​(20)O(20). The modular benchmark therefore does not indicate a breakdown of the SSM framework. It instead identifies a topology-sensitive regime in which higher-order truncation noticeably improves both macroscopic and community-level accuracy.

Panels (g) and (h) show where the remaining steady-state errors are concentrated. In panel (g), theO​(2)O(2)errors are spread broadly across the network, with especially visible deviations among low- and intermediate-degree nodes, whereas theO​(20)O(20)errors are much smaller across nearly the full degree range. Panel (h) reports the same comparison against the bridge scorekiout/kik_{i}^{\mathrm{out}}/k_{i}, which measures the fraction of edges leaving a node’s own community. TheO​(2)O(2)reduction shows appreciable errors across a wide range of bridge scores, while theO​(20)O(20)reduction suppresses these discrepancies substantially. These diagnostics indicate that modular bottlenecks chiefly expose the limitations of low-order truncations, especially near community interfaces, whereas higher-order reductions recover both node-level and aggregate behavior reliably.

This benchmark complements the ER, SW, and SF examples by isolating a structural effect that is only implicit in those ensembles, namely the role of modular bottlenecks in shaping reduction accuracy. The conclusion is not that modularity causes a qualitative failure of the SSM-based reduction. Rather, modularity increases the sensitivity of bridge-node and community-resolved observables to truncation order, which makes topology-aware diagnostics particularly useful in this setting.

## References
- [1]R. M. Anderson and R. M. May(1991)Infectious diseases of humans: dynamics and control.Oxford Science Publications,Oxford University Press,Oxford.External Links:ISBN 9780198540403Cited by:§I.
- [2]G. A. Baker and P. Graves-Morris(1996)Padé approximants.2nd edition,Cambridge University Press,Cambridge, UK.Cited by:Appendix B.
- [3]F. Battiston, E. Amico, A. Barrat, G. Bianconi, G. F. de Arruda, B. Franceschiello, I. Iacopini, S. Kéfi, V. Latora, Y. Moreno, M. M. Murray, T. P. Peixoto, F. Vaccarino, and G. Petri(2021)The physics of higher-order interactions in complex systems.Nature Physics17(10),pp. 1093–1098.External Links:Document,LinkCited by:Appendix S5,§III.3,§III.3,§III.3.
- [4]F. Battiston, G. Cencetti, I. Iacopini, V. Latora, M. Lucas, A. Patania, J. Young, and G. Petri(2020)Networks beyond pairwise interactions: structure and dynamics.Physics Reports874,pp. 1–92.External Links:Document,LinkCited by:Appendix S5,§III.3,§III.3,§III.3.
- [5]K. Bhaskaran, S. Jain, and M. Li(2025)Supplemental material for “nonlinear spectral model reduction of networked systems”.Note:Contains extended derivations, implementation details, and additional figures.Cited by:§I,Figure 4,Figure 5,§III.2,§III.2,§III.3,§III.4,§III,§III,§IV.
- [6]T. Breunung and G. Haller(2018)Explicit backbone curves from spectral submanifolds of forced-damped nonlinear mechanical systems.Proceedings of the Royal Society A474(2213),pp. 20180083.External Links:DocumentCited by:§I,§IV.
- [7]C. Brezinski(1991)Padé-type approximation and general orthogonal polynomials.Birkhäuser,Basel.Cited by:Appendix B.
- [8]M. Cenedese, J. Axås, B. Bäuerlein, K. Avila, and G. Haller(2022)Data-driven modeling and prediction of non-linearizable dynamics via spectral submanifolds.Nature Communications13,pp. 872.External Links:DocumentCited by:§I,§IV.
- [9]A. Cuyt, V. Petersen, B. Verdonk, H. Waadeland, and W. B. Jones(2008)Handbook of continued fractions for special functions.Springer,New York.Cited by:Appendix B.
- [10]R. de Montessus de Ballore(1902)Sur les fractions continues algébriques.Bulletin de la Société Mathématique de France30,pp. 28–36.Cited by:Appendix B.
- [11]Y. Ding, Z. Huang, M. Magdon-Ismail, and J. Gao(2024)Predicting time series of networked dynamical systems without knowing topology.arXiv preprint arXiv:2412.18734.Cited by:§I,§I.
- [12]I. Dobson, B. A. Carreras, V. E. Lynch, and D. E. Newman(2007)Complex systems analysis of series of blackouts: cascading failure, critical points, and self-organization.Chaos17(2),pp. 026103.External Links:DocumentCited by:§I.
- [13]J. Gao, B. Barzel, and A. Barabási(2016)Universal resilience patterns in complex networks.Nature530(7590),pp. 307–312.External Links:DocumentCited by:Appendix S4,Appendix S4,§I,§I,§I,§III.2.
- [14]P. R. Graves-Morris(1979)Vector and matrix padé approximations.Clarendon Press,Oxford.Cited by:Appendix B.
- [15]G. Haller and S. Ponsioen(2016)Nonlinear normal modes and spectral submanifolds: existence, uniqueness and use in model reduction.Nonlinear Dynamics86(3),pp. 1493–1534.External Links:DocumentCited by:§A.1,§I,§II.2.
- [16]I. Iacopini, G. Petri, A. Barrat, and V. Latora(2019)Simplicial models of social contagion.Nature Communications10(1),pp. 2485.External Links:Document,LinkCited by:Appendix S5,§III.3,§III.3,§III.3.
- [17]S. Jain and G. Haller(2022)How to compute invariant manifolds and their reduced dynamics in high-dimensional finite element models.Nonlinear Dynamics107(2),pp. 1417–1450.External Links:DocumentCited by:§I,§II.2.
- [18]S. Jain, M. Li, T. Thurnher, and G. Haller(2024)SSMTool 2.6: computation of invariant manifolds in high-dimensional mechanics problems (v2.6).Note:ZenodoSoftwareExternal Links:Document,LinkCited by:§A.1,§A.1,§II.2.
- [19]J. Jiang, Z. Huang, T. P. Seager, A. Hastings, and Y. Lai(2018)Predicting tipping points in mutualistic networks through dimension reduction.Proceedings of the National Academy of Sciences115(4),pp. E639–E647.External Links:DocumentCited by:§I,§I.
- [20]B. Kaszás and G. Haller(2025)Globalizing manifold-based reduced models for equations and data.Nature Communications16(1),pp. 61252.External Links:DocumentCited by:Appendix B,Appendix B,§I,§I,§II.2.
- [21]P. Landi, H. O. Minoarivelo, Å. Brännström, C. Hui, and U. Dieckmann(2018)Complexity and stability of ecological networks: a review of the theory.Population Ecology60,pp. 319–345.External Links:DocumentCited by:§I.
- [22]E. Laurence, N. Doyon, L. J. Dubé, and P. Desrosiers(2019)Spectral dimension reduction of complex dynamical networks.Physical Review X9(1),pp. 011042.External Links:DocumentCited by:Appendix S4,Appendix S4,§I,§I,§III.2.
- [23]M. Li and G. Haller(2022)Nonlinear analysis of forced mechanical systems with internal resonance using spectral submanifolds, part ii: bifurcation and quasi-periodic response.Nonlinear Dynamics110,pp. 1045–1080.External Links:DocumentCited by:§I,§IV.
- [24]M. Li, S. Jain, and G. Haller(2022)Nonlinear analysis of forced mechanical systems with internal resonance using spectral submanifolds, part i: periodic response and forced response curve.Nonlinear Dynamics110,pp. 1005–1043.External Links:DocumentCited by:§I.
- [25]A. Liu, J. Axås, and G. Haller(2024)Data-driven modeling and forecasting of chaotic dynamics on inertial manifolds constructed as spectral submanifolds.Chaos34(3),pp. 033140.External Links:DocumentCited by:§I,§IV.
- [26]N. Masuda and P. Kundu(2022)Dimension reduction of dynamical systems on networks with leading and nonleading eigenvectors of adjacency matrices.Physical Review Research4(2),pp. 023257.External Links:DocumentCited by:Appendix S4,Appendix S4,§I,§I,§III.2.
- [27]F. G. Mohammadi, M. H. Amini, and H. R. Arabnia(2020)Applications of nature-inspired algorithms for dimension reduction: enabling efficient data analytics.InOptimization, learning, and control for interdependent complex networks,pp. 67–84.Cited by:§I,§I.
- [28]M. Pascual and J. A. Dunne (Eds.)(2006)Ecological networks: linking structure to dynamics in food webs.Santa Fe Institute Studies on the Sciences of Complexity,Oxford University Press,Oxford.External Links:ISBN 9780195188165Cited by:§I.
- [29]S. Ponsioen, T. Pedergnana, and G. Haller(2019)Analytic prediction of isolated forced response curves from spectral submanifolds.Nonlinear Dynamics98(4),pp. 2755–2773.External Links:DocumentCited by:§III.
- [30]S. Ponsioen, L. Renson, G. W. H. van der Veen, and G. Haller(2020)Model reduction to spectral submanifolds and forced response curve computation.Journal of Sound and Vibration488,pp. 115640.External Links:DocumentCited by:§I.
- [31]B. Prasse, K. Devriendt, and P. V. Mieghem(2021)Clustering for epidemics on networks: a geometric approach.Chaos31(6),pp. 063115.External Links:DocumentCited by:§I,§I.
- [32]B. Prasse and P. V. Mieghem(2022)Predicting network dynamics without requiring the knowledge of the interaction graph.Proceedings of the National Academy of Sciences119(43),pp. e2205517119.External Links:DocumentCited by:§I,§I.
- [33]D. E. Rumelhart, G. E. Hinton, and R. J. Williams(1986)Learning representations by back-propagating errors.Nature323(6088),pp. 533–536.External Links:DocumentCited by:§I.
- [34]SocioPatterns Collaboration(2010)Hospital ward contact network, lyon, 2010.Note:https://www.sociopatterns.org/datasets/hospital-ward-dynamic-contact-network/Accessed 2025Cited by:§III.2,footnote 1.
- [35]SocioPatterns Collaboration(2013)Office building contact network, france, 2013.Note:https://www.sociopatterns.org/datasets/contacts-in-a-workplace/Accessed 2025Cited by:§III.2,footnote 1.
- [36]SocioPatterns Collaboration(2014)Rural malawi contact network.Note:https://www.sociopatterns.org/datasets/rural-malawi/Accessed 2025Cited by:§III.2,footnote 1.
- [37]B. Szaksz, G. Orosz, and G. Stepan(2025)Spectral submanifolds in time delay systems.Nonlinear Dynamics113(12),pp. 14265–14286.Cited by:§IV.
- [38]V. Thibeault, A. Allard, and P. Desrosiers(2024)The low-rank hypothesis of complex systems.Nature Physics20(2),pp. 294–302.External Links:DocumentCited by:§I.
- [39]V. Thibeault, G. St-Onge, L. J. Dubé, and P. Desrosiers(2020)Threefold way to the dimension reduction of dynamics on networks: an application to synchronization.Physical Review Research2(4),pp. 043215.External Links:DocumentCited by:§I,§I.
- [40]C. Tu, P. D’Odorico, and S. Suweis(2021)Dimensionality reduction of complex dynamical systems.iScience24(1),pp. 101912.External Links:DocumentCited by:§I,§I.
- [41]C. Tu, J. Luo, Y. Fan, and X. Pan(2023)Dimensionality reduction in stochastic complex dynamical networks.Chaos, Solitons & Fractals175,pp. 114034.Cited by:§I,§I.
- [42]C. Tu, Y. Wu, J. Luo, Y. Jiang, and X. Pan(2023)Dimensionality reduction in discrete-time dynamical systems.Communications in Nonlinear Science and Numerical Simulation123,pp. 107268.Cited by:§I,§I.
- [43]P. Vanhems, A. Barrat, C. Cattuto, J. Pinton, N. Khanafer, C. Regis, B. Kim, B. Comte, and N. Voirin(2013)Estimating potential infection transmission routes in hospital wards using wearable proximity sensors.Vol.8.External Links:Document,LinkCited by:footnote 1.
- [44]M. Vegué, V. Thibeault, P. Desrosiers, and A. Allard(2023)Dimension reduction of dynamics on modular and heterogeneous directed networks.PNAS Nexus2(5),pp. pgad150.External Links:DocumentCited by:§I,§I.
- [45]H. S. Wall(1948)Analytic theory of continued fractions.D. Van Nostrand,New York.Cited by:Appendix B.
- [46]C. Wu, D. Duan, and R. Xiao(2023)A novel dimension reduction method with information entropy to evaluate network resilience.Physica A: Statistical Mechanics and its Applications620,pp. 128727.External Links:DocumentCited by:§I,§I.

## 


- 


Major funding support from
