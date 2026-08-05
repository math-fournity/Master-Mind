# LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems

**arXiv ID**: 2608.01582v1
**Authors**: Shida Liu, Abhishek Gupta, Sumit Sinha, L. Mahadevan
**Published**: 2026-08-03
**Categories**: cond-mat.stat-mech, cond-mat.dis-nn, cs.LG, math-ph
**Comments**: 25 Pages, 7 figures. Accepted to the International Conference on Machine Learning (ICML 2026)
**HTML URL**: https://arxiv.org/html/2608.01582v1

## Abstract

Symmetry is central to modern machine learning and physics: invariances and equivariances improve sample efficiency, robustness, and out-of-distribution generalization, while symmetry principles guide scientific modeling. Yet for stochastic dynamical systems the relevant continuous symmetries are rarely known, and symmetry discovery for SDEs has remained essentially unexplored. We introduce \textit{LieStoNet}, an end-to-end, \emph{template-free} framework for discovering Lie-point symmetries of SDEs directly from spatiotemporal trajectories, without prespecifying symmetry groups, templates, or canonical coordinates. Building on the seminal SDE Lie-symmetry theory of Gaeta and Quintero (1999), which formalizes Lie-point SDE symmetries and their relation to Fokker-Planck symmetries, LieStoNet learns neural surrogates for drift and diffusion from increments, then learns projectable generators by enforcing the SDE determining equations, separately regularizing for closure under Lie brackets, adherence to the Lie algebra axioms (bilinearity, antisymmetry, Jacobi), and a non-redundant independent basis. The surrogate also defines an associated Fokker-Planck equation, enabling optional discovery of its Lie-point symmetries in parallel. Across multiple canonical SDEs with known analytic symmetries, LieStoNet recovers generators consistent with the ground-truth symmetry algebra, providing interpretable symmetry discovery for noisy dynamics. Code is available at \href{https://github.com/sumit-sinha-seas/LieStoNet_Final.git}{this link}.

## Full Text

LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2608.01582v1 [cond-mat.stat-mech] 03 Aug 2026

## LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical SystemsShida LiuAbhishek GuptaSumit SinhaL. Mahadevan

## Abstract

Symmetry is central to modern machine learning and physics: invariances and equivariances improve sample efficiency, robustness, and out-of-distribution generalization, while symmetry principles guide scientific modeling. Yet for stochastic dynamical systems the relevant continuous symmetries are rarely known, and symmetry discovery for SDEs has remained essentially unexplored. We introduceLieStoNet, an end-to-end,template-freeframework for discovering Lie-point symmetries of SDEs directly from spatiotemporal trajectories, without prespecifying symmetry groups, templates, or canonical coordinates. Building on the seminal SDE Lie-symmetry theory of Gaeta and Quintero (1999), which formalizes Lie-point SDE symmetries and their relation to Fokker-Planck symmetries, LieStoNet learns neural surrogates for drift and diffusion from increments, then learns projectable generators by enforcing the SDE determining equations, separately regularizing for closure under Lie brackets, adherence to the Lie algebra axioms (bilinearity, antisymmetry, Jacobi), and a non-redundant independent basis. The surrogate also defines an associated Fokker-Planck equation, enabling optional discovery of its Lie-point symmetries in parallel. Across multiple canonical SDEs with known analytic symmetries, LieStoNet recovers generators consistent with the ground-truth symmetry algebra, providing interpretable symmetry discovery for noisy dynamics. Code is available atthis link.Machine Learning, ICML

## 1Introduction

Symmetry is a foundational idea in science: it captures the notion that certain transformations of a system leave its behavior unchanged. In physics, symmetry principles have repeatedly guided the construction of successful theories and helped explain why diverse phenomena can be described by the same underlying laws(Gross,1995; Gross and Wilczek,1973). In machine learning, symmetry plays a similarly structural role. When a task is known to be insensitive to specific transformations (e.g., rotations, translations, permutations), incorporating the corresponding invariance or equivariance into models can substantially improve sample efficiency, robustness, and out-of-distribution generalization. This has motivated a broad line of work on symmetry-respecting architectures and learning pipelines, including group-equivariant convolutional networks(Cohen and Welling,2016; Cohenet al.,2019), rotation/translation-equivariant attention and geometric deep learning methods(Fuchset al.,2020; Thomaset al.,2018; Satorraset al.,2021; Kondoret al.,2018), and equivariant generative models for scientific simulation(Kanwaret al.,2020; Boydaet al.,2021). More broadly, symmetry is a key ingredient in physics-guided learning for dynamical systems(Wang and Yu,2021), and can complement approaches that learn conserved quantities or structured dynamics to enhance interpretability and generalization(Greydanuset al.,2019; Aletet al.,2021).

Despite these advances, the most impactful symmetries are oftenunknownin the settings where we would most like to exploit them. Real-world data may come from partially observed systems, complex coordinate representations, or measurements that mix latent variables, so the relevant transformations are not obvious. This motivatessymmetry discovery: learning the symmetry structure directly from data, rather than prescribing it by hand. Recent work has advanced symmetry discovery for deterministic dynamical systems, ranging from methods that infer invariances from learned representations/predictors to approaches that explicitly learn continuous transformations or generators, with downstream use in scientific modeling such as governing-equation and variable discovery(Bentonet al.,2020; Liu and Tegmark,2022; Yanget al.,2024a; Forestanoet al.,2023; Koet al.,2024; Shawet al.,2024; Yanget al.,2024b; Mohapatraet al.,2025). Collectively, these results position symmetry discovery as a practical route to interpretable, data-efficient learning in deterministic settings.

In this paper we move to the stochastic regime. Many systems of interest are inherently stochastic - due to unresolved degrees of freedom, environmental variability, or deliberate modeling of uncertainty - and stochastic differential equations (SDEs) provide a standard, flexible language for such dynamics. SDEs arise broadly across machine learning and the sciences, from diffusion-based generative modeling and Langevin-type sampling to canonical stochastic models in quantitative finance, molecular/biophysical dynamics, neuroscience, and climate/geophysical systems. Yet, while symmetry discovery for deterministic equations has rapidly evolved,symmetry discovery for SDEs remains essentially unexplored: to the best of our knowledge, there is no existing symmetry-discovery pipeline for SDEs at all. We close this gap withLieStoNet, an end-to-end framework that learns continuous SDE symmetries directly from trajectory data without prespecifying the symmetry group. In particular, “symmetry” may mean preserving sample-path behavior, preserving the evolution of probability distributions, or preserving derived deterministic descriptions of the system. A central derived description is the Fokker–Planck equation, which governs how the state’s probability density evolves over time. Because it is deterministic, the Fokker–Planck viewpoint is attractive for analysis and validation, but it does not automatically settle what it means to be a symmetry of the underlying stochastic dynamics. A principled approach must therefore ground the learning objective in the correct stochastic definition while still leveraging the Fokker–Planck perspective when useful.

Lie-point symmetry theory for SDEs.Our approach is grounded in the Lie-point (continuous) symmetry theory for SDEs of Gaeta and Rodríguez Quintero(Gaeta and Quintero,1999). This theory formalizes when a smooth, continuously-parameterized transformation maps an SDE to an equivalent SDE while respecting its stochastic structure, and it clarifies how SDE symmetries relate to (yet need not coincide with) symmetries of the associated Fokker–Planck equation. While it provides the correct conceptual target, it is not itself a data-driven discovery method. Our goal is to translate these principles into LieStoNet, a modern ML pipeline that discovers such symmetries directly from trajectory data.

## Contributions.

We summarize our main contributions as follows:
- •

SDE symmetry discovery.We introduce LieStoNet, to the best of our knowledge the first end-to-end ML framework for discovering continuous (Lie-point) symmetries of stochastic dynamical systems, addressing a gap in the symmetry-discovery literature that has largely focused on deterministic equations.
- •

Template-free discovery pipeline.LieStoNet does not prespecify a symmetry group, canonical coordinates, symbolic library, or generator template. Instead, it learns symmetry structure directly from spatiotemporal data while enforcing the stochastic symmetry conditions ofGaeta and Quintero (1999). The method is not assumption-free: it operates within the class of projectable Lie-point SDE symmetries, while broader stochastic symmetry classes, including random Lie-point symmetries, have also been studied(Gaeta and Spadaro,2017). The neural parameterization and optimization procedure also introduce inductive biases. We therefore use “template-free” to mean free of prespecified symmetry templates within this projectable SDE symmetry class.
- •

Connecting SDE and Fokker–Planck viewpoints.By learning a neural surrogate of the underlying SDE, our framework also induces a surrogate Fokker–Planck description for probability density evolution. We show symmetry discovery is possible in this associated deterministic view as well; nevertheless, since the Fokker–Planck equation does not capture all subtleties of stochastic symmetry, we emphasize discovery and validation at the SDE level.

## Related works.

Our work is most closely connected to recent machine-learning approaches that aim to discover symmetries from observations, particularly in deterministic settings. This includes methods that infer symmetries through invariance patterns in learned representations or predictors(Bentonet al.,2020; Liu and Tegmark,2022; Yanget al.,2024a), adversarial and generative formulations(Yanget al.,2023), explicit generator-style learning of continuous symmetries(Forestanoet al.,2023; Koet al.,2024; Shawet al.,2024), and data-driven Lie-point symmetry detection for deterministic continuous dynamical systems(Gabelet al.,2024). Related deterministic work has also used known Lie-point symmetries for data augmentation and equivariance in neural PDE solvers(Brandstetteret al.,2022). Other recent approaches go beyond restricted transformation classes(Shawet al.,2024; Huet al.,2025; Shawet al.,2025). There is also growing interest in discovering discrete symmetry groups(Calvo-Barléset al.,2024,2025)and in identifying local or approximate symmetries in high-dimensional systems(Bhatet al.,2025). Finally, symmetry has been used as a structural prior for downstream scientific modeling tasks, including governing-equation and variable discovery as well as scientific representation learning(Yanget al.,2024b; Mohapatraet al.,2025; Wanget al.,2020).PaperGenerator typeLie algebra?IIC?Dynamics typeKo et al.(Koet al.,2024)VF■\blacksquareM□\square□\square□\squareSTO□\squareDET■\blacksquareForestano et al.(Forestanoet al.,2023)VF□\squareM■\blacksquare■\blacksquare□\squareSTO□\squareDET■\blacksquareLieGAN(Yanget al.,2023)VF□\squareM■\blacksquare■\blacksquare□\squareSTO□\squareDET■\blacksquareAugerino(Bentonet al.,2020)VF□\squareM■\blacksquare□\square□\squareSTO□\squareDET■\blacksquareLaLiGAN(Yanget al.,2024a)VF□\squareM■\blacksquare■\blacksquare□\squareSTO□\squareDET■\blacksquareShaw et al.(Shawet al.,2024)VF■\blacksquareM□\square□\square□\squareSTO□\squareDET■\blacksquareLieNLSD(Huet al.,2025)VF■\blacksquareM□\square□\square■\blacksquareSTO□\squareDET■\blacksquareLieStoNet (Ours)VF■\blacksquareM□\square■\blacksquare■\blacksquareSTO■\blacksquareDET□\squareTable 1:Comparison with related symmetry discovery works.■\blacksquaredenotes yes and□\squaredenotes no.
“VF” = vector-field generator; “M” = matrix/linear parameterization.
“STO” = stochastic; “DET” = deterministic.
Columns indicate whether methods explicitly use Lie-algebra structure and an infinitesimal invariance condition (IIC). VF parameterizations can represent nonlinear, state-dependent symmetry transformations, whereas M parameterizations are typically limited to linear/affine actions.
Lie-algebra regularization enforces coherent composition/closure among generators, stabilizes training, and promotes recovery of a complete basis spanning the symmetry space rather than a bag of unrelated invariances.
IIC constraints provide a principled local criterion that can be enforced densely and differentiably, yielding more reliable and data-efficient symmetry learning than finite, sample-based checks alone.

## 2Mathematical Preliminaries

In this section, we briefly review the mathematical preliminaries; see AppendixAfor details.

## 2.1Stochastic Differential Equations and Lie Algebraic Symmetries

We use the Itô convention to model stochastic dynamics. An Itô stochastic differential equation describes the evolution of a state𝐱t\mathbf{x}_{t}through two components: a drift termff, which captures the deterministic tendency of the dynamics, and a diffusion termσ\sigma, which captures random fluctuations driven by a Wiener process. In this work, symmetries of such systems are understood as transformations of time and state variables that preserve the stochastic model. Because SDE sample paths are random, this preservation is interpreted distributionally: a symmetry maps the process to another process with equivalent induced stochastic dynamics in the transformed coordinates. To describe continuous families of such transformations, we work infinitesimally. A smooth one-parameter transformation has an infinitesimal generator, written schematically as a vector fieldX=(τ,ξ)X=(\tau,\xi), whose components describe the first-order changes in time and state. The full finite transformation can be recovered by integrating this vector field, and Itô’s formula determines how the drift and diffusion coefficients transform under the resulting change of variables.

The infinitesimal symmetry generators naturally form a Lie algebra. A Lie algebra is a vector space equipped with a bilinear bracket operation that records how infinitesimal transformations fail to commute; the bracket is antisymmetric and satisfies the Jacobi identity. For vector-field generators, this bracket is the usual commutator[X,Y]=X​Y−Y​X[X,Y]=XY-YX, which measures the difference between applying two infinitesimal transformations in opposite orders. The set of SDE symmetry generators is closed under linear combinations and under this bracket, so learning several generators amounts to learning a symmetry subspace together with its composition structure. For example, the span of the translation generator∂x\partial_{x}and the scaling generatorx​∂xx\partial_{x}is closed because their bracket is again a generator in the same span, namely[x​∂x,∂x]=−∂x[x\partial_{x},\partial_{x}]=-\partial_{x}. In what follows, our symmetry generators are represented as vector fields, and the Lie bracket provides the natural notion of closure under composition; the resulting Lie algebra is the main object we aim to discover and evaluate.

## 2.2Determining Equations for Projectable Generators

For clarity we present the one-dimensional setting (higher dimensions similar), however the theory and our implementations extend to high-dimensional examples as well. Aprojectable generatoris a Lie-point symmetry generator whose time component depends only on time, not on the state. We therefore restrict symmetry generators to the formX=τ​(t)​∂t+ξ​(t,x)​∂x.X\;=\;\tau(t)\,\partial_{t}\;+\;\xi(t,x)\,\partial_{x}.(1)

This excludes state-dependent time reparameterizations while retaining the continuous symmetries considered in this work.

In deterministic ODE/PDE symmetry theory, a standard route to validatingXXis theinfinitesimal invariance condition(IIC): invariance under the generator’s flow implies local differential constraints on(τ,ξ)(\tau,\xi)(Olver,1993). In the SDE
setting, the analogous IIC must account for both drift and diffusion and the stochastic
structure, yielding theSDE determining equationsbelow.d​Xt=f​(t,Xt)​d​t+σ​(t,Xt)​d​Wt.\mathrm{d}X_{t}=f(t,X_{t})\,\mathrm{d}t+\sigma(t,X_{t})\,\mathrm{d}W_{t}.(2)

## Theorem 2.1(SDE determining equations for projectable Lie-point symmetries(Gaeta and Quintero,1999)).

Consider the Itô SDE (2) and a projectable generatorXXas in (1).
ThenXXgenerates a (Lie-point) symmetry of (2) if and only if(τ,ξ)(\tau,\xi)satisfy,
for all(t,x)(t,x),ξt+f​ξx−ξ​fx−∂t(f​τ)+12​σ2​ξx​x=0,\xi_{t}+f\xi_{x}-\xi f_{x}-\partial_{t}(f\tau)+\tfrac{1}{2}\sigma^{2}\xi_{xx}=0,σ​ξx−ξ​σx−τ​σt−12​σ​τt=0.\sigma\xi_{x}-\xi\sigma_{x}-\tau\sigma_{t}-\tfrac{1}{2}\sigma\tau_{t}=0.

Here subscripts denote partial derivatives (e.g.,ξt=∂tξ\xi_{t}=\partial_{t}\xi,ξx​x=∂x​xξ\xi_{xx}=\partial_{xx}\xi),
and∂t(f​τ)=ft​τ+f​τt\partial_{t}(f\tau)=f_{t}\tau+f\tau_{t}.

We compute using these determining equations, the full symmetry Lie-algebras for four different SDEs in appendicesJ,K,L,M.

## 2.3Fokker–Planck Symmetries

## Associated FP equation.

The SDE (2) induces a deterministic evolution equation for the one-point densityu​(t,x)u(t,x)ofxtx_{t}, namely the (forward) Fokker–Planck equationut=−∂x(f​(t,x)​u)+12​∂x​x(σ2​(t,x)​u).u_{t}=-\partial_{x}\!\big(f(t,x)\,u\big)+\tfrac{1}{2}\partial_{xx}\big(\sigma^{2}(t,x)u\big).(3)

Because (3) is deterministic and linear inuu, it admits a well-developed Lie-point symmetry theory.

## FP symmetry generators.

A general Lie-point generator acting on(t,x,u)(t,x,u)has the formY=τ​(t,x,u)​∂t+ξ​(t,x,u)​∂x+ϕ​(t,x,u)​∂u.Y=\tau(t,x,u)\partial_{t}+\xi(t,x,u)\partial_{x}+\phi(t,x,u)\partial_{u}.(4)

One can prove that the linearity of FP implies that, theuu-component of the generator must be affine inuu:ϕ​(t,x,u)=α​(t,x)+β​(t,x)​u\phi(t,x,u)=\alpha(t,x)+\beta(t,x)\,u(theα\alpha-part corresponds to linear superposition) (see(Gaeta and Quintero,1999)). The FP analogue of the IIC yields a system of determining equations for(τ,ξ,α,β)(\tau,\xi,\alpha,\beta).

## Theorem 2.2(FP determining equations for projectable Lie-point symmetries(Gaeta and Quintero,1999)).

Consider the (one-dimensional) Fokker–Planck equation associated with the Itô SDE (2),
written in the linear formut+A​(t,x)​ux​x+B​(t,x)​ux+C​(t,x)​u=0,u_{t}+A(t,x)u_{xx}+B(t,x)u_{x}+C(t,x)u=0,(5)

where, for (3),A​(t,x)=−12​σ2​(t,x),B​(t,x)=f​(t,x)−∂x(σ2​(t,x)),A(t,x)=-\tfrac{1}{2}\sigma^{2}(t,x),\ B(t,x)=f(t,x)-\partial_{x}\big(\sigma^{2}(t,x)\big),C​(t,x)=∂xf​(t,x)−12​∂x​x(σ2​(t,x)).C(t,x)=\partial_{x}f(t,x)-\tfrac{1}{2}\partial_{xx}\big(\sigma^{2}(t,x)\big).

LetYYbe aprojectableLie-point generator acting on(t,x,u)(t,x,u)withuu-component affine inuu:Y=τ​(t)​∂t+ξ​(t,x)​∂x+(α​(t,x)+β​(t,x)​u)​∂u.Y=\tau(t)\partial_{t}+\xi(t,x)\partial_{x}+\big(\alpha(t,x)+\beta(t,x)u\big)\partial_{u}.(6)

ThenYYis a Lie-point symmetry of (5) if and only if:
- 1.

α​(t,x)\alpha(t,x)is any (fixed) solution of (5) (the linear superposition symmetry); and
- 2.

(τ,ξ,β)(\tau,\xi,\beta)satisfy the determining equations∂t(τ​A)+ξ​∂xA−2​A​∂xξ=0,\partial_{t}\big(\tau A\big)+\xi\partial_{x}A-2A\partial_{x}\xi=0,∂t(τ​B)−∂tξ+B​∂xξ−ξ​∂xB+2​A​∂xβ−A​∂x​xξ=0,\partial_{t}\big(\tau B\big)-\partial_{t}\xi+B\,\partial_{x}\xi-\xi\partial_{x}B+2A\partial_{x}\beta-A\partial_{xx}\xi=0,∂t(τ​C)+∂tβ+A​∂x​xβ+B​∂xβ+ξ​∂xC=0.\partial_{t}\big(\tau C\big)+\partial_{t}\beta+A\partial_{xx}\beta+B\partial_{x}\beta+\xi\partial_{x}C=0.

This theorem supplies an infinite family of symmetries:α​(t,x)​∂u\alpha(t,x)\partial_{u}for any solutionα\alphaof the FP-equation. These are considered as trivial symmetries and are often quotiented-out when defining the Lie algebra𝔤F​P\mathfrak{g}_{FP}of Fokker-Planck symmetries. We present more details in the AppendixD. The analytic symmetry algebra generators for the FP equation associated with the Brownian motiond​xt=σ0​d​Wtdx_{t}=\sigma_{0}dW_{t}are presented in appendixN.

## SDE symmetries as a nested subalgebra of FP symmetries.

Additionally, SDE symmetries can be extended to FP symmetries which induces an injection of Lie algebras𝔤I​t​o↪𝔤F​P\mathfrak{g}_{Ito}\hookrightarrow\mathfrak{g}_{FP}thus allowing us to think of SDE symmetries as a Lie-subalgebra of FP-symmetries. We provide more details along with a proof in AppendixE.

## 3Symmetry Discovery PipelineFigure 1:Pipeline for LieStoNet

On top of the above mathematical preliminaries, we presentLieStoNet, an end-to-end pipeline for discovering a basis of infinitesimal
generators that spans the Lie algebra of Lie-point symmetries of anunknownItô SDE.
We assume access only to discrete samples of trajectories (spatiotemporal data). In our
experiments, these samples are produced by simulating analytic SDEs, after which we discard
the governing equations and treat the data as observational data.Fokker–Planck (FP) symmetries are deterministic, so we only showcase FP-route symmetry discovery in Example 1 as a brief companion result, and otherwise keep the focus onstochastic(SDE-level) symmetry discovery to avoid expanding the scope.Ex.Analytic Equations1d​xt=1​d​Wtdx_{t}=1\ dW_{t}2d​xt=xt​d​t+1​d​Wtdx_{t}=x_{t}\ dt+1\ dW_{t}3d​xt=yt​d​t,d​yt=−1⋅yt​d​t+2​d​Wdx_{t}=y_{t}\ dt,\ dy_{t}=-1\cdot y_{t}\ dt+\sqrt{2}dW4d​xt=(1/x)​d​t+d​W1,d​yt=d​t+d​W2dx_{t}=(1/x)dt+dW_{1},dy_{t}=dt+dW_{2}Table 2:Analytic equations for each example. The analytic ground-truth generators are derived in the appendices.

## 3.1Stage 1: Neural SDE Surrogate from Increments

## Data and surrogate.

We observe trajectories{x(k)​(tn)}k=1K\{x^{(k)}(t_{n})\}_{k=1}^{K}on a gridt0<t1<⋯<tNt_{0}<t_{1}<\cdots<t_{N}withΔ​t=tn+1−tn\Delta t=t_{n+1}-t_{n}, and define incrementsΔ​xn(k):=x(k)​(tn+1)−x(k)​(tn).\Delta x_{n}^{(k)}:=x^{(k)}(t_{n+1})-x^{(k)}(t_{n}).

We fit a differentiable surrogate SDEdxt=fθ​(t,xt)​dt+σθ​(t,xt)​dWt,\differential x_{t}\;=\;f_{\theta}(t,x_{t})\,\differential t\;+\;\sigma_{\theta}(t,x_{t})\,\differential W_{t},(7)

wherefθf_{\theta}andσθ>0\sigma_{\theta}>0are parameterized by neural networks (details in the
appendixP.0.1). The role of this surrogate is to provide smooth coefficient functions so that all
derivatives required by the symmetry constraints in Theorem2.1and AppendixCcan be computed via autodiff.

## Increment likelihood (local MLE).

Euler–Maruyama motivates the conditional approximationΔ​x∣(tn,xn)≈𝒩​(fθ​(tn,xn)​Δ​t,σθ2​(tn,xn)​Δ​t),\Delta x\mid(t_{n},x_{n})\approx\mathcal{N}\!\bigl(f_{\theta}(t_{n},x_{n})\Delta t,\;\sigma_{\theta}^{2}(t_{n},x_{n})\Delta t\bigr),

leading to the per-sample negative log-likelihood (up to an additive constant)ℓθ=(Δ​x−fθ​Δ​t)22​σθ2​Δ​t+12​log(σθ2​Δ​t).\ell_{\theta}=\frac{\bigl(\Delta x-f_{\theta}\,\Delta t\bigr)^{2}}{2\,\sigma_{\theta}^{2}\,\Delta t}+\frac{1}{2}\log\bigl(\sigma_{\theta}^{2}\,\Delta t\bigr.).(8)

We minimizeLSDE​(θ)=𝔼​[ℓθ]+λreg​‖θ‖2L_{\mathrm{SDE}}(\theta)=\mathbb{E}[\ell_{\theta}]+\lambda_{\mathrm{reg}}\|\theta\|^{2}and then freezeθ\theta. In the remainder we writef:=fθf:=f_{\theta}andσ:=σθ\sigma:=\sigma_{\theta}.

## 3.2Stage 2: Generator Parameterization

## Projectable generators.

We learnmmprojectable Lie-point generators of the form in Eq. (9)Xi=τi​(t)​∂t+ξi​(t,x)​∂x,i=1,…,m,X_{i}\;=\;\tau_{i}(t)\,\partial_{t}\;+\;\xi_{i}(t,x)\,\partial_{x},\qquad i=1,\dots,m,(9)

whereτi\tau_{i}andξi\xi_{i}are represented by multi-head MLPs producing(τ1,…,τm)(\tau_{1},\ldots,\tau_{m})and(ξ1,…,ξm)(\xi_{1},\ldots,\xi_{m}). This enforces∂xτi≡0\partial_{x}\tau_{i}\equiv 0by
construction while allowing nonlinear, state-dependent symmetries throughξi​(t,x)\xi_{i}(t,x).

## Training points.

After fitting and freezing the Stage-1 surrogate(fθ,σθ)(f_{\theta},\sigma_{\theta}), we generate a point cloudΩ\Omegafor Stage-2 by simulating trajectories from the learned surrogate SDE and collecting the resulting space-time states(tn,xn)(t_{n},x_{n}). All losses below are then computed as Monte Carlo averages over samples fromΩ\Omega(and, when needed, over adjacent trajectory-time pairs).

## 3.3Learning Objectives

LieStoNet trains{Xi}i=1m\{X_{i}\}_{i=1}^{m}using two families of losses. We first defineSDE-validity lossesthat enforce Lie-point symmetry constraints for the surrogate SDE,
then defineLie-algebra structure lossesthat regularize the learned generators to form
a finite-dimensional Lie algebra under the Lie bracket. See AppendixCfor detailed mathematical formulations.Algorithm of LieStoNetInput:Trajectories / spatiotemporal samplesDD; generator-count schedulem=1,2,…m=1,2,...Output:Symmetry Lie-algebra dimensionmm, generators{Xk}k=1K\{X_{k}\}_{k=1}^{K}, diagnosticsSurrogate LearningTrain a differentiable surrogatesfθf_{\theta},σθ\sigma_{\theta}onDD.Generator Learning (fixedmm)ParameterizeXiX_{i}fori=1,…,mi=1,...,m. Optimize the composite objective:∑i=17wi​Li\sum_{i=1}^{7}w_{i}L_{i}.Dimension SelectionIncreasemmand repeat generator learning; choosem^\hat{m}at the first minimum of the closure lossL1​(m)L_{1}(m)within the dimension bound.ReportFor the discovered dimensionm=m^m=\hat{m}, compute span alignment with principal angles against analytic ground-truth generators (when available), evaluate/plot after-push residuals, and release{Xi}\{X_{i}\}.Table 3:Overview of LieStoNet. The method learns vector-field generators by enforcing infinitesimal invariance
and Lie-algebra closure constraints using learned drift and diffusion neural surrogates.(a)Ex1(b)Ex2(c)Ex3(d)Ex4Figure 2:Post-training Lie bracket closure lossL1L_{1}vs. number of generatorsmmacross four experiments.Colors denote independent runs with identical settings (different random seeds), showing the minimum is consistently attained at the ground-truth m rather than a one-off.

## Lie-algebra structural losses
- •

L1L_{1}(Lie-bracket closure + constancy, fixed).Encourages[Xi,Xj][X_{i},X_{j}]to lie inspan​{Xk}\mathrm{span}\{X_{k}\}(via projection) and the resulting structure coefficientsci​jkc_{ij}^{k}to be approximately constant over(t,x)(t,x).
- •

L2L_{2}(Jacobi identity).Penalizes Jacobi violations so nested commutators compose consistently, i.e., the learned bracket behaves as a Lie bracket.
- •

L3L_{3}(Skew-symmetry).Enforces antisymmetry of the bracket: swapping generator order flips the commutator sign.
- •

L4L_{4}(Bilinearity).Enforces linearity of the bracket in each argument so it distributes correctly over linear combinations.
- •

L5L_{5}(Functional independence).Penalizes near-linear dependence of the learned fields over the domain to avoid redundant generators and ensure a trulymm-dimensional span.

## SDE-validity losses
- •

L6L_{6}(SDE determining-equation loss).Enforces the Itô symmetry determining conditions (Theorem2.1), making each learned generator compatible with the SDE drift and diffusion and thus a valid infinitesimal SDE symmetry.
- •

L7L_{7}(Prolonged pushforward residual; SDE-only,τ/ξ\tau/\xi).Adds a finite-ε\varepsiloncheck by flowing(t,x)(t,x)along the generator and comparing the pushed-forward surrogate coefficients to the surrogate coefficients evaluated at the pushed point, providing nonlocal validation beyond the infinitesimal conditions.

## FP losses

(When learning FP symmetries, we replace the SDE-validity losses with FP-specific losses while keeping the same algebraic losses.)
- •

L8L_{8}(Fokker–Planck determining-equation loss).Enforces Lie-point determining conditions for the induced Fokker–Planck PDE using generatorsXi=τi​(t)​∂t+ξi​(t,x)​∂x+βi​(t,x)​u​∂uX_{i}=\tau_{i}(t)\partial_{t}+\xi_{i}(t,x)\partial_{x}+\beta_{i}(t,x)\,u\,\partial_{u},
by minimizing the batch-averaged magnitude of the three FP determining-equation (2.2) residuals so each generator is a valid infinitesimal FP symmetry.
- •

L9L_{9}(Fokker–Planck after-flow / pushforward-on-uuloss).Adds a finite-ε\varepsiloncheck by flowing(t,x,u)(t,x,u)along the prolonged generator (includingu˙=βi​(t,x)​u\dot{u}=\beta_{i}(t,x)u) and penalizing disagreement between the flowed valueuεu_{\varepsilon}and the FP surrogate evaluated at the flowed pointu^​(tε,xε)\hat{u}(t_{\varepsilon},x_{\varepsilon}), i.e., approximately mapping FP solutions to FP solutions.

## Total objective.

Let𝒘=(w1,…,w7)\bm{w}=(w_{1},\dots,w_{7})denote nonnegative weights. We train generator
parametersψ\psiby minimizingLgen​(ψ)=∑j=17wj​Lj+wwd​‖ψ‖2L_{\mathrm{gen}}(\psi)\;=\;\sum_{j=1}^{7}w_{j}\,L_{j}\;+\;w_{\mathrm{wd}}\|\psi\|^{2}(10)

wherewwdw_{\mathrm{wd}}represents the weight on weight decay of the generator parameters. Note that for the FP symmetry case,L6,L7L_{6},L_{7}are replaced byL8,L9L_{8},L_{9}. See AppendixPfor training details.

## 3.4Determining the Lie algebra Dimensionmm

In practice, we follow the above symmetry generator training while sweeping through different candidates for the number of learned generators (m=1,2,…m=1,2,\dots) and record the post-training Lie bracket closure loss (L1L_{1}). The value ofmmwhich minimizesL1L_{1}is selected as the recovered dimension of the symmetry Lie algebra.

This sweep is finite in the SDE settings considered here because the admissible symmetry search space is a priori bounded: scalar Itô SDEs admit Lie algebras of dimension at most33, whilenn-dimensional systems with full-rank diffusion have maximal dimensionn+2n+2(Kozlov,2010b,2011,a). In contrast, deterministic differential equations may have arbitrarily large or infinite-dimensional symmetry algebras, with much larger finite bounds when they exist, e.g.,n2+4​n+3n^{2}+4n+3for certain second-order ODE systems(González-López,1988). Thus the Itô structure, diffusion determining equations, and noise irregularity make LieStoNet’s dimension sweep a finite search over a theoretically justified range: one sweeps admissiblemmand selects the minimizer of the post-training closure lossL1L_{1}. For genuinely high-dimensional systems, LieStoNet can also be applied after deriving a reduced effective SDE, e.g., via projection or Mori–Zwanzig-type coarse-graining.

## 4Experiments: Evaluation Protocol(a)Ex1(b)Ex2(c)Ex3(d)Ex4Figure 3:Distribution of combination-wise maximum principal angles.Number of learned generators (mm) vs. principal angles. The blue boxes denote the interquartile range; the orange horizontal lines inside the box denote the median; the green up triangles and the blue down triangles denote the maximum and minimum of maximum principal angles, respectively; the orange dots denote the mean.

Element-wise comparison of learned symmetries is ill-posed because infinitely many bases can span the same Lie algebra; the basis-invariant object is therefore thespanof the generators.

## 4.1Span Alignment via Principal Angles (basis-invariant)

Concretely, we evaluate each set of generators over a shared(t,x)(t,x)region and view them as vectors in a common feature space; this yields a learned subspace and a ground-truth subspace. We then quantify how well these subspaces align usingprincipal angles, which measure the smallest angular discrepancies between two subspaces: angles near0∘0^{\circ}indicate that the learned generators span (up to basis change) the same symmetry directions as the analytic ones, while larger angles indicate missing or spurious directions. This metric is (i) basis-invariant, (ii) global over the evaluation region, and (iii) useful for diagnosing dimension mismatch (extra generators typically introduce directions that increase the worst-case misalignment) (see AppendixB).

## 4.2Results

As shown in Figure2, the post-training closure objectiveL1L_{1}consistently attains its minimum at the analytic Lie-algebra dimension, so LieStoNet recovers the symmetry dimension without receiving it as input. We then compare learned and analytic generator spans using principal angles. Form≤3m\leq 3, we compare the learnedmm-dimensional span with each analyticmm-generator subspace; form>3m>3, we compare each learned 3-generator subspace with the full analytic 3-dimensional span. Figure3reports the resulting maximum-angle distributions. SinceL1L_{1}selects the correct dimension, the principal angles at that dimension mainly reflect surrogate and optimization accuracy. The smallest maximum angles occur at the selected dimension, indicating recovery of the symmetry-algebra span rather than spurious low-residual generators. Tables4and5report the selected-dimension SDE and Fokker–Planck angles.Ex.Ang 1Ang 2Ang 316.261∘6.261^{\circ}2.487∘2.487^{\circ}2.313∘2.313^{\circ}219.370∘19.370^{\circ}11.051∘11.051^{\circ}0.571∘0.571^{\circ}37.643∘7.643^{\circ}1.329∘1.329^{\circ}0.276∘0.276^{\circ}414.292∘14.292^{\circ}6.241∘6.241^{\circ}2.505∘2.505^{\circ}Table 4:Principal angles of SDE symmetry for all examples at the ground-truth dimension.Ang 1Ang 2Ang 3Ang 4Ang 5Ang 68.417∘8.417^{\circ}7.424∘7.424^{\circ}1.829∘1.829^{\circ}1.091∘1.091^{\circ}0.752∘0.752^{\circ}0.303∘0.303^{\circ}Table 5:Principal angles of Fokker-Planck equation symmetry for example 1 at the ground-truth dimension.

In AppendixF, we additionally verify that the learned SDE generators embed into the learned Fokker–Planck generator span when both are projected to the common(τ,ξ)(\tau,\xi)-space.

## Higher-dimensional symmetry algebra.

We test recovery of larger algebras on the ten-dimensional Brownian SDEd​Xti=d​Wti,i=1,…,10,\mathrm{d}X_{t}^{i}=\mathrm{d}W_{t}^{i},\qquad i=1,\ldots,10,

a high-dimensional analogue of Example 1 with a 12-dimensional projectable symmetry algebra. Its generators mirror AppendixJ, with translations∂i\partial_{i}and scaling2​t​∂t+∑ixi​∂i2t\partial_{t}+\sum_{i}x_{i}\partial_{i}. LieStoNet recovers a 12-dimensional algebra with principal angles0.73∘,0.79∘,0.82∘,0.93∘,0.98∘,1.14∘,1.17∘,1.38∘0.73^{\circ},0.79^{\circ},0.82^{\circ},0.93^{\circ},0.98^{\circ},1.14^{\circ},1.17^{\circ},1.38^{\circ},1.63∘1.63^{\circ},2.08∘,10.21∘,16.55∘2.08^{\circ},10.21^{\circ},16.55^{\circ}, supporting extension beyond the low-dimensional 3-generator benchmarks.

## Surrogate sensitivity and computational overhead.

Because LieStoNet computes symmetry losses through a learned SDE surrogate, we also evaluate sensitivity to surrogate perturbations; recovery degrades smoothly under controlled structured and random perturbations. We additionally report per-loss runtime measurements and polynomial scaling estimates for the algebraic and SDE-validity losses. These analyses are provided in AppendicesHandI.

## Ablation of generator losses.

We further test whether the algebraic and SDE-validity losses are all practically useful by ablatingL1,…,L7L_{1},\ldots,L_{7}one at a time. Removing any single loss worsens the maximum principal angle between the learned and analytic symmetry-algebra spans; the largest degradations occur when removing the closure lossL1L_{1}or the SDE determining-equation lossL6L_{6}. Removing the finite-step after-push lossL7L_{7}also substantially worsens recovery, suggesting that finite-flow consistency provides useful stabilization beyond local infinitesimal invariance. The full ablation results, weight-sensitivity sweep, and qualitative generator plots are reported in AppendicesO,Q, andG.

## 5Additional Experiment Results

## 5.1After-Push Residual (finite-ϵ\epsilonsymmetry check).

The defining property of an SDE symmetry is that the induced transformation maps the SDEd​Xt=f​(t,Xt)​d​t+σ​(t,Xt)​d​Wt\mathrm{d}X_{t}=f(t,X_{t})\mathrm{d}t+\sigma(t,X_{t})\mathrm{d}W_{t}to thesameSDE form (equivalently, it preserves the drift–diffusion coefficients under the change of variables). To test this definition beyond the infinitesimal regime, we perform a finite-ϵ\epsilon“after-push” check for each learned generatorXi=τi​∂t+ξi​∂xX_{i}=\tau_{i}\partial_{t}+\xi_{i}\partial_{x}(or its 2D analogue). We first sample 500 trajectories from the analytic SDE, then push every space–time point(t,𝐱)(t,\mathbf{x})along the generator flowΦϵ=exp⁡(ϵ​Xi)\Phi_{\epsilon}=\exp(\epsilon X_{i})to obtain(t~,𝐱~)(\tilde{t},\tilde{\mathbf{x}}). IfXiX_{i}is a true symmetry direction, then the pushed trajectory should still be governed by the same coefficients, so the drift and diffusion inferred from the pushed data should match the analytic drift and diffusion evaluated at(t~,𝐱~)(\tilde{t},\tilde{\mathbf{x}}). Operationally, we therefore fit a neural SDE surrogate on the pushed trajectories and measure the residual between its learned(f^,σ^)(\hat{f},\hat{\sigma})and the analytic(f,σ)(f,\sigma)on a fixed evaluation box, reported separately for drift (Dft.) and diffusion (Dfu.) in Table6. The residuals remain small across all examples and generators forϵ∈{1,3,5}\epsilon\in\{1,3,5\}, providing empirical evidence that the learned generators induce finite transformations that approximately map the SDE to itself, consistent with the definition of an SDE symmetry.Ex.Gen 1Gen 2Gen 3Dft.Dfu.Dft.Dfu.Dft.Dfu.19.69.64.64.68.08.05.65.62.32.35.15.121.91.92.72.71.11.16.06.05.75.74.44.437.67.61.41.41.31.39.79.72.72.70.20.241.91.96.26.26.416.411.01.02.52.59.29.2Ex.Gen 1Gen 2Gen 3Dft.Dfu.Dft.Dfu.Dft.Dfu.18.28.28.98.99.79.76.46.48.88.88.58.529.19.10.60.67.37.38.88.81.01.08.48.437.57.58.18.19.69.60.90.96.36.36.26.240.80.88.08.07.97.98.78.79.59.58.48.4Ex.Gen 1Gen 2Gen 3Dft.Dfu.Dft.Dfu.Dft.Dfu.10.20.22.92.91.41.40.70.72.12.10.40.423.03.00.10.10.60.62.52.51.81.82.82.831.11.12.32.32.72.70.30.30.90.91.61.642.42.40.80.81.91.93.03.00.00.02.62.6Table 6:After-push residuals forϵ=1,3,5\epsilon=1,3,5from top to bottom; units are10−410^{-4}forϵ=1\epsilon=1andϵ=3\epsilon=3, and10−310^{-3}forϵ=5\epsilon=5.

## 5.2Real-World Stochastic Data: High-Frequency BTC/USDT

To test whether LieStoNet transfers beyond synthetic SDEs with known analytic symmetries, we apply the same pipeline without architectural or algorithmic modifications to high-frequency BTC/USDT trade data from Binance. The dataset contains approximately1.81.8million ticks over 24 hours, aggregated to500500ms resolution, filtered, and split into 575 overlapping sub-trajectories. Since no ground-truth symmetry algebra is available for this empirical system, we use the same closure-based dimension-selection criterion and finite-flow validation diagnostics used in the synthetic experiments.

Sweepingm=1,2,3m=1,2,3, the first nontrivial minimum of the post-training closure loss occurs atm⋆=2m^{\star}=2, with a pronounced increase fromm=2m=2tom=3m=3. This suggests a stable two-dimensional learned symmetry algebra. We then validate the two learned generators using two complementary tests. First, the after-push residual measures whether trajectories pushed along the learned generator flow remain consistent with the learned SDE drift and diffusion. Second, the distributional invariance test evaluates whether the standardized Euler–Maruyama residual distribution is preserved after pushing trajectories. Both tests indicate that the learned transformations preserve the empirical stochastic dynamics substantially better than random-push controls, as shown in Tables7and8.ϵ\epsilonGenerator 1Generator 2Dft.Dfu.Dft.Dfu.11.4×10−31.4\times 10^{-3}2.3×10−72.3\times 10^{-7}1.0×10−21.0\times 10^{-2}2.6×10−42.6\times 10^{-4}37.9×10−27.9\times 10^{-2}9.9×10−29.9\times 10^{-2}5.0×10−25.0\times 10^{-2}1.7×10−11.7\times 10^{-1}51.3×10−11.3\times 10^{-1}2.7×10−12.7\times 10^{-1}5.0×10−25.0\times 10^{-2}2.8×10−12.8\times 10^{-1}Table 7:After-push residuals on BTC/USDT data.Drift and diffusion residuals are reported after pushing trajectories along each learned generator for step lengthϵ\epsilon. Smaller values indicate better finite-flow preservation of the learned stochastic dynamics.ϵ\epsilonGen. 1Gen. 2Random control0.050.0080.0279.70.100.0270.111191.60.200.0910.827232.00.300.3244.65166.00.506.4117.6112.0Table 8:Distributional invariance on BTC/USDT data.We reportΔ​NLL=NLLpushed−NLLorig\Delta\mathrm{NLL}=\mathrm{NLL}_{\mathrm{pushed}}-\mathrm{NLL}_{\mathrm{orig}}. The learned-generator pushes preserve the residual distribution far better than random-push controls over the tested step sizes.

## 6Conclusion

We introducedLieStoNet, an end-to-end pipeline for discovering projectable Lie-point symmetries of SDEs from trajectory data. LieStoNet learns a neural SDE surrogate and then learns symmetry generators by enforcing SDE determining equations, Lie-algebraic structure, independence, and finite-flow validation losses. Across analytic SDE benchmarks, it recovers the correct symmetry dimension and strong span-level alignment with the ground-truth algebra. Ablations, after-push checks, BTC/USDT experiments, surrogate-sensitivity tests, runtime measurements, and a higher-dimensional SDE further support the proposed objectives.

## Limitations and outlook.

LieStoNet depends on the fidelity and coverage of the learned drift/diffusion surrogate, though perturbation experiments suggest smooth degradation under controlled surrogate errors. The method also restricts attention to projectable Lie-point generators. Scaling to complex high-dimensional empirical systems will require more efficient parameterizations, better surrogate calibration, and validation under partial observation and measurement noise. Future work includes extending beyond projectable symmetries and using discovered symmetries to build symmetry-constrained stochastic surrogates.

## Impact Statement

This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.

## References
- F. Alet, D. Doblar, A. Zhou, J. Tenenbaum, K. Kawaguchi, and C. Finn (2021)Noether networks: meta-learning useful conserved quantities.Advances in Neural Information Processing Systems34,pp. 16384–16397.Cited by:§1.
- G. Benton, M. Finzi, P. Izmailov, and A. G. Wilson (2020)Learning invariances in neural networks from training data.Advances in neural information processing systems33,pp. 17605–17616.Cited by:§1,Table 1,§1.
- M. Bhat, J. Park, J. Yang, N. Dehmamy, R. Walters, and R. Yu (2025)AtlasD: automatic local symmetry discovery.InProceedings of the 42nd International Conference on Machine Learning,Proceedings of Machine Learning Research, Vol.267,pp. 4153–4171.Cited by:§1.
- D. Boyda, G. Kanwar, S. Racanière, D. J. Rezende, M. S. Albergo, K. Cranmer, D. C. Hackett, and P. E. Shanahan (2021)Sampling using su (n) gauge equivariant flows.Physical Review D103(7),pp. 074504.Cited by:§1.
- J. Brandstetter, M. Welling, and D. E. Worrall (2022)Lie point symmetry data augmentation for neural pde solvers.InProceedings of the 39th International Conference on Machine Learning (ICML),Proceedings of Machine Learning Research, Vol.162,pp. 2241–2256.Cited by:§1.
- P. Calvo-Barlés, S. G. Rodrigo, E. Sánchez-Burillo, and L. Martín-Moreno (2024)Finding discrete symmetry groups via machine learning.Physical Review E110(4),pp. 045304.Cited by:§1.
- P. Calvo-Barlés, S. G. Rodrigo, and L. Martín-Moreno (2025)Machine learning for detection of equivariant finite symmetry groups in dynamical systems.Machine Learning: Science and Technology6(2),pp. 025058.External Links:DocumentCited by:§1.
- T. S. Cohen, M. Geiger, and M. Weiler (2019)A general theory of equivariant cnns on homogeneous spaces.Advances in neural information processing systems32.Cited by:§1.
- T. Cohen and M. Welling (2016)Group equivariant convolutional networks.InInternational conference on machine learning,pp. 2990–2999.Cited by:§1.
- R. T. Forestano, K. T. Matchev, K. Matcheva, A. Roman, E. B. Unlu, and S. Verner (2023)Deep learning symmetries and their lie groups, algebras, and subalgebras from first principles.Machine Learning: Science and Technology4(2),pp. 025027.Cited by:§1,Table 1,§1.
- F. Fuchs, D. Worrall, V. Fischer, and M. Welling (2020)Se (3)-transformers: 3d roto-translation equivariant attention networks.Advances in neural information processing systems33,pp. 1970–1981.Cited by:§1.
- A. Gabel, R. Quax, and E. Gavves (2024)Data-driven lie point symmetry detection for continuous dynamical systems.Machine Learning: Science and Technology5(1),pp. 015037.External Links:DocumentCited by:§1.
- G. Gaeta and N. R. Quintero (1999)Lie-point symmetries and stochastic differential equations.Journal of Physics A: Mathematical and General32(48),pp. 8485–8505.Cited by:§E.1,§E.1,§E.1,Appendix E,Appendix E,Appendix E,Appendix E,2nd item,§1,§2.3,Theorem 2.1,Theorem 2.2.
- G. Gaeta and F. Spadaro (2017)Random lie-point symmetries of stochastic differential equations.Journal of Mathematical Physics58(5),pp. 053503.External Links:DocumentCited by:2nd item.
- A. González-López (1988)Symmetries of linear systems of second-order ordinary differential equations.Journal of Mathematical Physics29(5),pp. 1097–1105.External Links:DocumentCited by:§3.4.
- S. Greydanus, M. Dzamba, and J. Yosinski (2019)Hamiltonian neural networks.Advances in neural information processing systems32.Cited by:§1.
- D. J. Gross and F. Wilczek (1973)Asymptotically free gauge theories. i.Physical Review D8(10),pp. 3633.Cited by:§1.
- D. J. Gross (1995)Symmetry in physics: wigner’s legacy.Physics Today48(12),pp. 46–50.Cited by:§1.
- L. Hu, Y. Li, and Z. Lin (2025)Explicit discovery of nonlinear symmetries from dynamic data.InProceedings of the 42nd International Conference on Machine Learning,Proceedings of Machine Learning Research, Vol.267,pp. 24509–24534.Cited by:§1,Table 1.
- G. Kanwar, M. S. Albergo, D. Boyda, K. Cranmer, D. C. Hackett, S. Racaniere, D. J. Rezende, and P. E. Shanahan (2020)Equivariant flow-based sampling for lattice gauge theory.Physical Review Letters125(12),pp. 121601.Cited by:§1.
- G. Ko, H. Kim, and J. Lee (2024)Learning infinitesimal generators of continuous symmetries from data.Advances in Neural Information Processing Systems37,pp. 85973–86003.Cited by:§1,Table 1,§1.
- R. Kondor, Z. Lin, and S. Trivedi (2018)Clebsch–gordan nets: a fully fourier space spherical convolutional neural network.Advances in Neural Information Processing Systems31.Cited by:§1.
- R. Kozlov (2010a)Symmetries of systems of stochastic differential equations with diffusion matrices of full rank.Journal of Physics A: Mathematical and Theoretical43(24),pp. 245201.External Links:DocumentCited by:§3.4.
- R. Kozlov (2010b)The group classification of a scalar stochastic differential equation.Journal of Physics A: Mathematical and Theoretical43(5),pp. 055202.External Links:DocumentCited by:§3.4.
- R. Kozlov (2011)On maximal lie point symmetry groups admitted by scalar stochastic differential equations.Journal of Physics A: Mathematical and Theoretical44(20),pp. 205202.External Links:DocumentCited by:§3.4.
- Z. Liu and M. Tegmark (2022)Machine learning hidden symmetries.Physical Review Letters128(18),pp. 180201.Cited by:§1,§1.
- J. Mohapatra, N. Dehmamy, C. Both, S. Das, and T. Jaakkola (2025)Symmetry-driven discovery of dynamical variables in molecular simulations.InProceedings of the 42nd International Conference on Machine Learning,Proceedings of Machine Learning Research, Vol.267,pp. 44594–44614.Cited by:§1,§1.
- P. J. Olver (1993)Applications of lie groups to differential equations.Vol.107,Springer Science & Business Media.Cited by:§2.2.
- V. G. Satorras, E. Hoogeboom, and M. Welling (2021)E (n) equivariant graph neural networks.InInternational conference on machine learning,pp. 9323–9332.Cited by:§1.
- B. Shaw, S. Kunapuli, A. Magner, and K. R. Moon (2025)Lie group symmetry discovery and enforcement using vector fields.arXiv preprint arXiv:2505.08219.Cited by:§1.
- B. Shaw, A. Magner, and K. Moon (2024)Symmetry discovery beyond affine transformations.Advances in Neural Information Processing Systems37,pp. 112889–112918.Cited by:§1,Table 1,§1.
- N. Thomas, T. Smidt, S. Kearnes, L. Yang, L. Li, K. Kohlhoff, and P. Riley (2018)Tensor field networks: rotation-and translation-equivariant neural networks for 3d point clouds.arXiv preprint arXiv:1802.08219.Cited by:§1.
- R. Wang, R. Walters, and R. Yu (2020)Incorporating symmetry into deep dynamics models for improved generalization.arXiv preprint arXiv:2002.03061.Cited by:§1.
- R. Wang and R. Yu (2021)Physics-guided deep learning for dynamical systems: a survey.arXiv preprint arXiv:2107.01272.Cited by:§1.
- J. Yang, N. Dehmamy, R. Walters, and R. Yu (2024a)Latent space symmetry discovery.InProceedings of the 41st International Conference on Machine Learning,Proceedings of Machine Learning Research, Vol.235,pp. 56047–56070.Cited by:§1,Table 1,§1.
- J. Yang, W. Rao, N. Dehmamy, R. Walters, and R. Yu (2024b)Symmetry-informed governing equation discovery.Advances in Neural Information Processing Systems37,pp. 65297–65327.Cited by:§1,§1.
- J. Yang, R. Walters, N. Dehmamy, and R. Yu (2023)Generative adversarial symmetry discovery.InProceedings of the 40th International Conference on Machine Learning,Proceedings of Machine Learning Research, Vol.202,pp. 39488–39508.Cited by:§1,Table 1.

## Appendix AMathematical Preliminaries

## A.1Stochastic Differential Equations

We use the Itô convention for SDEs. Annn-dimensional Itô SDE is written asd​𝐱t=𝐟​(t,𝐱t)​d​t+𝝈​(t,𝐱t)​d​𝐖t,\mathrm{d}\mathbf{x}_{t}=\mathbf{f}(t,\mathbf{x}_{t})\,\mathrm{d}t+\bm{\sigma}(t,\mathbf{x}_{t})\,\mathrm{d}\mathbf{W}_{t},(11)

where𝐱t∈ℝn\mathbf{x}_{t}\in\mathbb{R}^{n},𝐟:ℝ×ℝn→ℝn\mathbf{f}:\mathbb{R}\times\mathbb{R}^{n}\to\mathbb{R}^{n}is thedrift,𝝈:ℝ×ℝn→ℝn×n\bm{\sigma}:\mathbb{R}\times\mathbb{R}^{n}\to\mathbb{R}^{n\times n}is thediffusion, and𝐖t\mathbf{W}_{t}is annn-dimensional standard Wiener process capturing the random
fluctuations.

## A.2Lie algebras: Definitions and Motivation

ALie algebrais a vector space equipped with a product that capturescomposition of infinitesimal transformations. Formally, it is a real vector space𝔤\mathfrak{g}whose elementsX,Y,Z∈𝔤X,Y,Z\in\mathfrak{g}admit a bilinear operation[⋅,⋅]:𝔤×𝔤→𝔤[\cdot,\cdot]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}(theLie bracket) satisfyingantisymmetry[X,Y]=−[Y,X][X,Y]=-[Y,X]and theJacobi identity[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0along with bilinearity in each argument.

## A.3Infinitesimal SDE Symmetry Generators as Lie Algebras

Asymmetryof a dynamical system - deterministic or stochastic - is a transformation of variables that preserves the model’s behavior. Symmetries compose: applying one symmetry after another yields another symmetry, and for smooth, continuous families this structure forms (at least locally) aLie group. Many common symmetries are parameterized continuously (e.g., time shifts or state scalings), and for such families it is most convenient to work infinitesimally: what an arbitrarily small transformation does. The set of all infinitesimal symmetry directions forms aLie algebra.

Concretely, consider a smooth one-parameter change of variables(t,x)↦(t′,x′)=Φε​(t,x)(t,x)\mapsto(t^{\prime},x^{\prime})=\Phi_{\varepsilon}(t,x)withΦ0\Phi_{0}equal to the identity andε\varepsilonbeing the pseudo-time component (how far is the trajectory being pushed along the generator). Its infinitesimal generator is the vector fieldX=τ​(t,x)​∂t+ξ​(t,x)​∂x,X\;=\;\tau(t,x)\,\partial_{t}\;+\;\xi(t,x)\,\partial_{x},(12)

(shorthanded as(τ,ξ)(\tau,\xi)) which acts to first order ast↦t+ε​τ​(t,x)t\mapsto t+\varepsilon\,\tau(t,x)andx↦x+ε​ξ​(t,x)x\mapsto x+\varepsilon\,\xi(t,x). Conversely, given a vector fieldτ,ξ\tau,\xi, one can recoverΦϵ=exp⁡(ϵ​X)\Phi_{\epsilon}=\exp(\epsilon X)by integrating:dd​ε​(t​(ε),x​(ε))=(τ​(t​(ε),x​(ε)),ξ​(t​(ε),x​(ε)))\frac{d}{d\varepsilon}(t(\varepsilon),x(\varepsilon))=(\tau(t(\varepsilon),x(\varepsilon)),\xi(t(\varepsilon),x(\varepsilon)))

with(t​(0),x​(0))=(t,x)(t(0),x(0))=(t,x).

For an Itô SDE, Itô’s formula specifies how such a coordinate change transforms the drift and diffusion coefficients(μ,σ)(\mu,\sigma). We callΦε\Phi_{\varepsilon}a (Lie-point) symmetry if this transformation maps the SDE to the same SDE. In contrast to deterministic systems—where symmetries literally map solution trajectories to solution trajectories - SDE paths are random, so the natural invariance notion isdistributional: a symmetry preserves thelawof the process, meaning it maps sample paths to sample paths whose induced stochastic dynamics are equivalent in the transformed coordinates.

Finally, symmetry generators inherit an algebraic structure. They are closed under theLie bracket[X,Y]:=X​Y−Y​X,[X,Y]:=XY-YX,

i.e. withX=(τX,ξX)X=(\tau_{X},\xi_{X})andY=(τY,ξY)Y=(\tau_{Y},\xi_{Y}),[X,Y]=(X​(τY)−Y​(τX))​∂t+(X​(ξY)−Y​(ξX))​∂x,[X,Y]=\bigl(X(\tau_{Y})-Y(\tau_{X})\bigr)\partial_{t}+\bigl(X(\xi_{Y})-Y(\xi_{X})\bigr)\partial_{x},

which captures how infinitesimal symmetries compose. This closure endows the symmetry generators with the structure of a Lie algebra. Learning multiple generators{Xi}\{X_{i}\}therefore amounts to learning a symmetrysubspace: any linear combination is another valid infinitesimal symmetry direction, while the bracket encodes their composition structure. This Lie algebra is the chief object we aim to discover and evaluate in this work.

For instance, the two-dimensional space𝔤={a​∂x+b​x​∂x:a,b∈ℝ}\mathfrak{g}=\{a\,\partial_{x}+b\,x\partial_{x}\!:a,b\in\mathbb{R}\}

is closed under the Lie bracket, and a direct calculation using Lie bracket’s formula gives:[x​∂x,∂x]⋅f=x​∂x∂xf−∂x(x​∂xf)=−∂xf[x\partial_{x},\partial_{x}]\cdot f=x\partial_{x}\partial_{x}f-\partial_{x}(x\partial_{x}f)=-\partial_{x}f

So,[x​∂x,∂x]=−∂x[x\partial_{x},\partial_{x}]=-\partial_{x}which again lies inside𝔤\mathfrak{g}, showing its closure. In what follows, our symmetry generators are represented as such vector fields; the Lie bracket provides
the natural notion of “closure” under composition of infinitesimal symmetries, and the resulting Lie
algebra structure is the object we aim to learn.

## Appendix BDetails of Span Alignment via Principal Angles

This appendix states the mathematical procedure used to compare thespanof learned
symmetry generators to thespanof analytic (ground-truth) generators. Because a symmetry
algebra is only identifiable up to an arbitrary change of basis (any invertible mixing of a valid
generator set spans the same subspace), we evaluate agreement at the subspace level via principal
angles.

## Vectorizing generators on a common domain.

Fix an evaluation domainΩ⊂ℝ×ℝd\Omega\subset\mathbb{R}\times\mathbb{R}^{d}in the variables(t,𝐱)(t,\mathbf{x}),
and choose a finite set of pointsΩeval={(tp,𝐱p)}p=1B⊂Ω\Omega_{\mathrm{eval}}=\{(t_{p},\mathbf{x}_{p})\}_{p=1}^{B}\subset\OmegawhereBBis the number of evaluation points.
For a learned projectable generatorXi=τi​(t)​∂t+ξi​(t,𝐱)⋅∇𝐱,i=1,…,m,X_{i}\;=\;\tau_{i}(t)\,\partial_{t}\;+\;\xi_{i}(t,\mathbf{x})\cdot\nabla_{\mathbf{x}},\qquad i=1,\dots,m,

define itsvectorized representationonΩeval\Omega_{\mathrm{eval}}by stacking its components:vi:=(τi​(tp),ξi​(tp,𝐱p))p=1B∈ℝB​(1+d).v_{i}\;:=\;\bigl(\tau_{i}(t_{p}),\ \xi_{i}(t_{p},\mathbf{x}_{p})\bigr)_{p=1}^{B}\in\mathbb{R}^{B(1+d)}.(13)

Collect these columns intoV=[v1,…,vm]∈ℝB​(1+d)×m.V\;=\;[v_{1},\dots,v_{m}]\in\mathbb{R}^{B(1+d)\times m}.

Similarly, given analytic generators{Wj}j=1r\{W_{j}\}_{j=1}^{r}with components(τ~j,ξ~j)(\tilde{\tau}_{j},\tilde{\xi}_{j}), definewj:=(τ~j​(tp),ξ~j​(tp,𝐱p))p=1B∈ℝB​(1+d),w_{j}\;:=\;\bigl(\tilde{\tau}_{j}(t_{p}),\ \tilde{\xi}_{j}(t_{p},\mathbf{x}_{p})\bigr)_{p=1}^{B}\in\mathbb{R}^{B(1+d)},W=[w1,…,wr]∈ℝB​(1+d)×r.W=[w_{1},\dots,w_{r}]\in\mathbb{R}^{B(1+d)\times r}.

By construction,span​(V)\mathrm{span}(V)andspan​(W)\mathrm{span}(W)represent the learned and ground-truth
symmetry subspaces overΩeval\Omega_{\mathrm{eval}}.

## Principal angles between subspaces.

LetQVQ_{V}andQWQ_{W}be orthonormal bases forspan​(V)\mathrm{span}(V)andspan​(W)\mathrm{span}(W), e.g. from
reduced QR factorizations. The principal anglesθ1≤⋯≤θmin⁡(m,r)∈[0,π/2]\theta_{1}\leq\cdots\leq\theta_{\min(m,r)}\in[0,\pi/2]between the two subspaces are defined bycos⁡(θℓ)=σℓ​(QV⊤​QW),ℓ=1,…,min⁡(m,r),\cos(\theta_{\ell})=\sigma_{\ell}\!\left(Q_{V}^{\top}Q_{W}\right),\quad\ell=1,\dots,\min(m,r),

whereσℓ​(⋅)\sigma_{\ell}(\cdot)denotes theℓ\ellth singular value in descending order. Small principal
angles indicate that the learned generators span (up to basis change) the same symmetry directions
as the analytic generators onΩeval\Omega_{\mathrm{eval}}.

## Dimension-mismatch protocol (subset comparisons).

When the learned generator countmmdiffers from the analytic dimensionrr, we compute principal
angles by comparing subspaces of equal dimension:
- •

Ifm>rm>r, we evaluate principal angles betweenspan​(VS)\mathrm{span}(V_{S})andspan​(W)\mathrm{span}(W)for
all subsetsS⊂{1,…,m}S\subset\{1,\dots,m\}with|S|=r|S|=r, whereVSV_{S}denotes the submatrix ofVVwith columns
indexed bySS.
- •

Ifm<rm<r, we evaluate principal angles betweenspan​(V)\mathrm{span}(V)andspan​(WT)\mathrm{span}(W_{T})for
all subsetsT⊂{1,…,r}T\subset\{1,\dots,r\}with|T|=m|T|=m, whereWTW_{T}denotes the corresponding submatrix ofWW.

For each subset comparison, we report the full set of principal angles and often summarize alignment
by the maximum principal angle within that subset. This yields a basis-invariant diagnostic of how
closely the learned span matches the analytic symmetry span across candidate dimensions.

## Appendix CLoss Functions

## C.1Lie-Algebra Structure Losses

## (L1) Lie-bracket closure + constancy (fixed).

For each pair(i,j)(i,j), we fit coefficientsci​jk​(t,x)c^{k}_{ij}(t,x)such that[Xi,Xj]​(t,x)≈∑k=1mci​jk​(t,x)​Xk​(t,x)[X_{i},X_{j}](t,x)\approx\sum_{k=1}^{m}c^{k}_{ij}(t,x)\,X_{k}(t,x), and penalize the projection residual:L1:=𝔼(t,x)∈Ω​[∑1≤i<j≤m‖[Xi,Xj]−∑k=1mci​jk​Xk‖2]L_{1}:=\;\mathbb{E}_{(t,x)\in\Omega}\!\left[\sum_{1\leq i<j\leq m}\left\|[X_{i},X_{j}]-\sum_{k=1}^{m}c^{k}_{ij}X_{k}\right\|^{2}\right]+𝔼(t,x)∈Ω​[∑1≤i<j≤m∑k=1m‖∇t,xci​jk​(t,x)‖2]+\mathbb{E}_{(t,x)\in\Omega}\!\left[\sum_{1\leq i<j\leq m}\sum_{k=1}^{m}\|\nabla_{t,x}c^{k}_{ij}(t,x)\|^{2}\right]

## (L2) Jacobi identity loss.

Using the fitted coefficientsci​jkc^{k}_{ij}, we penalize violations of the Jacobi identity:L2:=∑triples​(i,j,k)‖∑cyclic​(i,j,k)∑ℓ=1mci​jℓ​cℓ​kp‖2L_{2}:=\sum_{\text{triples }(i,j,k)}\left\|\sum_{\mathrm{cyclic}(i,j,k)}\;\sum_{\ell=1}^{m}c^{\ell}_{ij}\,c^{p}_{\ell k}\right\|^{2}

## (L3) Skew-symmetry (antisymmetry) loss.

We enforce[Xi,Xj]=−[Xj,Xi][X_{i},X_{j}]=-[X_{j},X_{i}]:L3:=𝔼(t,x)∈Ω​[∑1≤i<j≤m‖[Xi,Xj]+[Xj,Xi]‖2]L_{3}:=\mathbb{E}_{(t,x)\in\Omega}\!\left[\sum_{1\leq i<j\leq m}\bigl\|[X_{i},X_{j}]+[X_{j},X_{i}]\bigr\|^{2}\right]

## (L4) Bilinearity loss.

Samplinga,b∼𝒰​[−1,1]a,b\sim\mathcal{U}[-1,1]and indices(i,j,k)(i,j,k), we penalize violations of bilinearity:L4:=𝔼​[‖[a​Xi+b​Xj,Xk]−a​[Xi,Xk]−b​[Xj,Xk]‖2]L_{4}:=\mathbb{E}\!\left[\bigl\|[aX_{i}+bX_{j},X_{k}]-a[X_{i},X_{k}]-b[X_{j},X_{k}]\bigr\|^{2}\right]+𝔼​[‖[Xk,a​Xi+b​Xj]−a​[Xk,Xi]−b​[Xk,Xj]‖2]+\mathbb{E}\!\left[\bigl\|[X_{k},aX_{i}+bX_{j}]-a[X_{k},X_{i}]-b[X_{k},X_{j}]\bigr\|^{2}\right]

## (L5) Functional independence loss.

OnΩspan={(tp,xp)}p=1P\Omega_{\mathrm{span}}=\{(t_{p},x_{p})\}_{p=1}^{P}, definevi:=(τi​(tp),ξi​(tp,xp))p=1P∈ℝ2​Pv_{i}:=(\tau_{i}(t_{p}),\xi_{i}(t_{p},x_{p}))_{p=1}^{P}\in\mathbb{R}^{2P}andV=[v1,…,vm]∈ℝ2​P×mV=[v_{1},\dots,v_{m}]\in\mathbb{R}^{2P\times m}, with Gram matrixG:=V⊤​VG:=V^{\top}V.
We penalize near-singularity viaL5:=−log⁡det⁡(G+ϵ​I),L_{5}:=-\log\det(G+\epsilon I),

withϵ>0\epsilon>0.

## C.2SDE-Validity Losses

## (L6) SDE determining-equation loss (IIC).

We enforce the determining equations in Theorem2.1. For each generatorXiX_{i}and each(t,x)∈Ω(t,x)\in\Omega, define residualsr1(i)​(t,x)=ξt+f​ξx−ξ​fx−∂t(f​τ)+12​σ2​ξx​x,r^{(i)}_{1}(t,x)=\xi_{t}+f\,\xi_{x}-\xi\,f_{x}-\partial_{t}(f\tau)+\tfrac{1}{2}\sigma^{2}\,\xi_{xx},r2(i)​(t,x)=σ​ξx−ξ​σx−τ​σt−12​σ​τt,r^{(i)}_{2}(t,x)=\sigma\,\xi_{x}-\xi\,\sigma_{x}-\tau\,\sigma_{t}-\tfrac{1}{2}\sigma\,\tau_{t},

where all quantities are evaluated at(t,x)(t,x), subscripts denote partial derivatives, and∂t(f​τ)=ft​τ+f​τt\partial_{t}(f\tau)=f_{t}\tau+f\tau_{t}. We use the squared residual loss:L6:=1m​∑i=1m𝔼(t,x)∈Ω​[|r1(i)​(t,x)|2+|r2(i)​(t,x)|2]L_{6}:=\frac{1}{m}\sum_{i=1}^{m}\mathbb{E}_{(t,x)\in\Omega}\!\left[\,|r^{(i)}_{1}(t,x)|^{2}+|r^{(i)}_{2}(t,x)|^{2}\,\right]

## (L7) Prolonged pushforward residual.

The determining-equation loss is local. We add a finite-ε\varepsilonconsistency loss that checks whether the
learned generator approximately pushes thesurrogate coefficients(f,σ)(f,\sigma)to the surrogate coefficients
evaluated at the pushed point.

Fix a smallε>0\varepsilon>0. For generatorXiX_{i}, let(t,x)↦(t~,x~)(t,x)\mapsto(\tilde{t},\tilde{x})be the
point transformation obtained by integratingdtdε=τi​(t),dxdε=ξi​(t,x).\frac{\differential t}{\differential\varepsilon}=\tau_{i}(t),\qquad\frac{\differential x}{\differential\varepsilon}=\xi_{i}(t,x).

Along this flow, we propagate coefficient fields(μ,ς)(\mu,\varsigma)using the prolonged system
in our implementation:dςdε=ς​(∂xξi−12​∂tτi)\frac{\differential\varsigma}{\differential\varepsilon}=\varsigma\Bigl(\partial_{x}\xi_{i}-\tfrac{1}{2}\,\partial_{t}\tau_{i}\Bigr)dμdε=∂tξi+μ​∂xξi+12​ς2​∂x​xξi−μ​∂tτi,\frac{\differential\mu}{\differential\varepsilon}=\partial_{t}\xi_{i}+\mu\,\partial_{x}\xi_{i}+\tfrac{1}{2}\varsigma^{2}\,\partial_{xx}\xi_{i}-\mu\,\partial_{t}\tau_{i},

initialized atμ​(0)=f​(t,x)\mu(0)=f(t,x)andς​(0)=σ​(t,x)\varsigma(0)=\sigma(t,x). After oneε\varepsilon-step, letμpred,ςpred\mu_{\mathrm{pred}},\varsigma_{\mathrm{pred}}be the propagated coefficients, and define
direct evaluations at the pushed pointμeval:=f​(t~,x~),ςeval:=σ​(t~,x~).\mu_{\mathrm{eval}}:=f(\tilde{t},\tilde{x}),\qquad\varsigma_{\mathrm{eval}}:=\sigma(\tilde{t},\tilde{x}).

We penalize discrepancies and include a soft barrier discouraging negative pushed time
increments along pushed trajectories:L7:=1m​∑i=1m𝔼​[(μpred−μeval)2+(ςpred−ςeval)2]L_{7}:=\;\frac{1}{m}\sum_{i=1}^{m}\mathbb{E}\!\left[(\mu_{\mathrm{pred}}-\mu_{\mathrm{eval}})^{2}+(\varsigma_{\mathrm{pred}}-\varsigma_{\mathrm{eval}})^{2}\right]+λΔ​t​1m​∑i=1m𝔼​[softplus⁡(−Δ​t~)].\;+\;\lambda_{\Delta t}\,\frac{1}{m}\sum_{i=1}^{m}\mathbb{E}\!\left[\operatorname{softplus}(-\Delta\tilde{t})\right].

The expectations are over sampled trajectory points (coefficient terms) and adjacent time
pairs (forΔ​t~\Delta\tilde{t}). We integrate the above prolonged system numerically.

## C.3FP-Validity Losses

## (L8) Fokker-Planck Determining Equations

This loss enforces the determining equations for Lie point symmetries of the 1D Fokker-Planck equation, given byut=A​ux​x+B​ux+C​uu_{t}=Au_{xx}+Bu_{x}+Cu, whereA=−12​σ2A=-\frac{1}{2}\sigma^{2},B=f−(A)xB=f-(A)_{x}, andC=fx−(A)x​xC=f_{x}-(A)_{xx}. For each generatorXi=τi​(t)​∂t+ξi​(t,x)​∂x+ϕi​(t,x,u)​∂uX_{i}=\tau_{i}(t)\partial_{t}+\xi_{i}(t,x)\partial_{x}+\phi_{i}(t,x,u)\partial_{u}, withϕi​(t,x,u)=βi​(t,x)​u\phi_{i}(t,x,u)=\beta_{i}(t,x)u, the following three equations must hold:Ri,1\displaystyle R_{i,1}=(τ˙i​A+τi​At)+ξi​Ax−2​A​ξi,x≈0\displaystyle=(\dot{\tau}_{i}A+\tau_{i}A_{t})+\xi_{i}A_{x}-2A\xi_{i,x}\approx 0Ri,2\displaystyle R_{i,2}=(τ˙i​B+τi​Bt)−(ξ˙i+B​ξi,x−ξi​Bx)+2​A​βi,x\displaystyle=(\dot{\tau}_{i}B+\tau_{i}B_{t})-(\dot{\xi}_{i}+B\xi_{i,x}-\xi_{i}B_{x})+2A\beta_{i,x}−A​ξi,x​x≈0\displaystyle\;\;-A\xi_{i,xx}\approx 0Ri,3\displaystyle R_{i,3}=(τ˙i​C+τi​Ct)+β˙i+A​βi,x​x+B​βi,x+ξi​Cx≈0\displaystyle=(\dot{\tau}_{i}C+\tau_{i}C_{t})+\dot{\beta}_{i}+A\beta_{i,xx}+B\beta_{i,x}+\xi_{i}C_{x}\approx 0

where(⋅)˙\dot{(\cdot)}denotes∂t(⋅)\partial_{t}(\cdot), and subscriptst,x,x​xt,x,xxdenote partial derivatives. The loss functionL8L_{8}is the mean-squared (or mean-absolute) sum of these residuals over a batch of(t,x)(t,x)points:L8:=1m​|ℬ|​∑i=1m∑(t,x)∈ℬ(Ri,12+Ri,22+Ri,32)L_{8}:=\frac{1}{m|\mathcal{B}|}\sum_{i=1}^{m}\sum_{(t,x)\in\mathcal{B}}(R_{i,1}^{2}+R_{i,2}^{2}+R_{i,3}^{2})

## (L9) Fokker-Planck After-Flow (Pushforward onuu)

This loss ensures that the learned generators approximately preserve the solution of the Fokker-Planck equation. For a given solutionu​(t,x)u(t,x)of the FP equation, flowing(t,x,u)(t,x,u)along the prolonged generatorXi=τi​∂t+ξi​∂x+βi​u​∂uX_{i}=\tau_{i}\partial_{t}+\xi_{i}\partial_{x}+\beta_{i}u\partial_{u}for a small stepε\varepsilonshould result in another valid solution. Let(t0,x0,u0)(t_{0},x_{0},u_{0})be an initial point (whereu0=u^​(t0,x0)u_{0}=\hat{u}(t_{0},x_{0})is the learned FP surrogate solution). We numerically integrate the system:d​td​α\displaystyle\frac{dt}{d\alpha}=τi​(t)\displaystyle=\tau_{i}(t)d​xd​α\displaystyle\frac{dx}{d\alpha}=ξi​(t,x)\displaystyle=\xi_{i}(t,x)d​ud​α\displaystyle\frac{du}{d\alpha}=βi​(t,x)​u\displaystyle=\beta_{i}(t,x)u

fromα=0\alpha=0toα=ε\alpha=\varepsilon, yielding(tε,xε,uε)(t_{\varepsilon},x_{\varepsilon},u_{\varepsilon}). The loss penalizes the difference between the flowed solutionuεu_{\varepsilon}and the learned FP surrogate evaluated at the flowed point,u^​(tε,xε)\hat{u}(t_{\varepsilon},x_{\varepsilon}):L9:=1m​|ℬ|​∑i=1m∑(t0,x0)∈ℬ(u^​(tε,xε)−uε)2L_{9}:=\frac{1}{m|\mathcal{B}|}\sum_{i=1}^{m}\sum_{(t_{0},x_{0})\in\mathcal{B}}(\hat{u}(t_{\varepsilon},x_{\varepsilon})-u_{\varepsilon})^{2}

whereℬ\mathcal{B}is a batch of collocation points. The integration uses Heun’s method, and the residuals can be either squared (L2) or absolute (L1).

## Appendix DFokker–Planck Symmetries

This appendix records (i) the standard FP symmetry structure used to motivate optional
FP-route losses, and (ii) proofs that the relevant sets of generators form Lie algebras.

## D.1FP Equation Associated with an Itô SDE

For an Itô SDE inℝn\mathbb{R}^{n}dxi=fi​(t,x)​dt+σki​(t,x)​dwk,\differential x^{i}=f^{i}(t,x)\,\differential t+\sigma^{i}_{\;k}(t,x)\,\differential w^{k},

the forward FP equation for a one-point densityu​(x,t)u(x,t)can be written asut+Ai​j​(t,x)​ui​j+Bi​(t,x)​ui+C​(t,x)​u=0,u_{t}+A^{ij}(t,x)u_{ij}+B^{i}(t,x)u_{i}+C(t,x)u=0,(14)

with coefficients (one common convention)Ai​j:=−12​(σ​σ𝖳)i​j,Bi:=fi−∂j(σ​σ𝖳)i​j,A^{ij}:=-\tfrac{1}{2}(\sigma\sigma^{\mathsf{T}})^{ij},\ B^{i}:=f^{i}-\partial_{j}(\sigma\sigma^{\mathsf{T}})^{ij},C:=∂ifi−12​∂i​j2(σ​σ𝖳)i​j.C:=\partial_{i}f^{i}-\tfrac{1}{2}\partial_{ij}^{2}(\sigma\sigma^{\mathsf{T}})^{ij}.

## D.2Projectable FP Symmetries Act Affinely inuu

Because the FP equation is linear inuu, any Lie-point symmetry must act affinely inuu:X=τ​(t)​∂t+ξi​(t,x)​∂xi+(α​(t,x)+β​(t,x)​u)​∂u.X=\tau(t)\partial_{t}+\xi^{i}(t,x)\partial_{x^{i}}+(\alpha(t,x)+\beta(t,x)u)\partial_{u}.

The “α\alpha-part” corresponds to the linear superposition symmetry:Xα=α​∂uX_{\alpha}=\alpha\partial_{u}for any solutionα\alphaof the FP equation.

## D.3Lie Algebra Structure Proofs

## Theorem D.1(FP symmetries form a Lie algebra).

Let𝔤FP\mathfrak{g}_{\mathrm{FP}}denote the set of Lie-point symmetry generators of the FP
equation. Then𝔤FP\mathfrak{g}_{\mathrm{FP}}is a Lie algebra under the commutator[X1,X2]=X1​X2−X2​X1[X_{1},X_{2}]=X_{1}X_{2}-X_{2}X_{1}.

## Proof.

The infinitesimal invariance condition is linear inXX, so𝔤FP\mathfrak{g}_{\mathrm{FP}}is a
vector space.
Closure under brackets follows from the standard fact that prolongation commutes with Lie
brackets:pr(2)​[X1,X2]=[pr(2)​X1,pr(2)​X2]\mathrm{pr}^{(2)}[X_{1},X_{2}]=[\mathrm{pr}^{(2)}X_{1},\mathrm{pr}^{(2)}X_{2}],
together with the invariance identitypr(2)​X​(ΔFP)=λX​ΔFP\mathrm{pr}^{(2)}X(\Delta_{\mathrm{FP}})=\lambda_{X}\Delta_{\mathrm{FP}}for some scalar
functionλX\lambda_{X}on jet space. Applying the commutator toΔFP\Delta_{\mathrm{FP}}yieldspr(2)​[X1,X2]​(ΔFP)=λ[X1,X2]​ΔFP\mathrm{pr}^{(2)}[X_{1},X_{2}](\Delta_{\mathrm{FP}})=\lambda_{[X_{1},X_{2}]}\Delta_{\mathrm{FP}},
hence[X1,X2]∈𝔤FP[X_{1},X_{2}]\in\mathfrak{g}_{\mathrm{FP}}.
∎

## Appendix ESDE symmetries as a Lie-subalgebra of FP Symmetries

Classical results relate SDE symmetries to a subalgebra of FP symmetries; in particular, the
projectable SDE symmetry algebra𝔤Ito\mathfrak{g}_{\mathrm{Ito}}embeds into FP symmetries by
adding an appropriate vertical component inuu, and one obtains a nested structure𝔤Ito⊂𝔤FP.\mathfrak{g}_{\mathrm{Ito}}\subset\mathfrak{g}_{\mathrm{FP}}.We now prove this containment more formally.

## E.1Quotienting Out the Superposition Ideal and the SDE–FP Isomorphism

Let𝔤Ito\mathfrak{g}_{\mathrm{Ito}}be the Lie algebra ofprojectableItô symmetry generatorsX=τ​(t)​∂t+ξi​(t,x)​∂xi,X=\tau(t)\,\partial_{t}+\xi^{i}(t,x)\,\partial_{x_{i}},

whose coefficients satisfy the Itô determining equations(3.4)in[Gaeta and Quintero,1999].

Let𝔤FP\mathfrak{g}_{\mathrm{FP}}be the Lie algebra of projectable Lie point symmetry generators
of the associated FP equation, and letℐ:={Xα=α​(t,x)​∂u:α​solves the FP equation}.\mathcal{I}:=\bigl\{X_{\alpha}=\alpha(t,x)\,\partial_{u}\;:\;\alpha\text{ solves the FP equation}\bigr\}.

By [Thm. 3][Gaeta and Quintero,1999], theseXαX_{\alpha}are precisely the “trivial” symmetries coming from
linear superposition, and the general projectable FP symmetry hasϕ=α+β​u.\phi=\alpha+\beta u.

In particular,ℐ\mathcal{I}is an (infinite-dimensional) Lie ideal in𝔤FP\mathfrak{g}_{\mathrm{FP}}, so the quotient𝔤FPess:=𝔤FP/ℐ\mathfrak{g}_{\mathrm{FP}}^{\mathrm{ess}}:=\mathfrak{g}_{\mathrm{FP}}/\mathcal{I}

is a Lie algebra.

Define theSDE-induced essential symmetry subalgebraas the image in the quotient
of the ansatzτ​∂t+ξi​∂xi−(div⁡ξ)​u​∂u,\tau\,\partial_{t}+\xi^{i}\partial_{x_{i}}-(\operatorname{div}\xi)\,u\,\partial_{u},

which is exactly the “probabilistically compatible” form singled out in[Gaeta and Quintero,1999](see Remark 11 and equation (5.10)). Concretely,𝔤SDEess:={[τ∂t+ξi∂xi\displaystyle\mathfrak{g}_{\mathrm{SDE}}^{\mathrm{ess}}:=\Bigl\{\bigl[\tau\,\partial_{t}+\xi^{i}\partial_{x_{i}}−(divξ)u∂u]∈𝔤FPess:\displaystyle-(\operatorname{div}\xi)\,u\,\partial_{u}\bigr]\in\mathfrak{g}_{\mathrm{FP}}^{\mathrm{ess}}\;:(τ,ξ)satisfy (3.4)}.\displaystyle(\tau,\xi)\text{ satisfy (3.4)}\Bigr\}.

## Theorem E.1(Lie-algebra isomorphism moduloℐ\mathcal{I}).

DefineΦ:𝔤Ito→𝔤FPess\Phi:\mathfrak{g}_{\mathrm{Ito}}\to\mathfrak{g}_{\mathrm{FP}}^{\mathrm{ess}}as:Φ​(τ​∂t+ξi​∂xi):=[τ​∂t+ξi​∂xi−(div⁡ξ)​u​∂u]\Phi\!\left(\tau\,\partial_{t}+\xi^{i}\partial_{x_{i}}\right):=\bigl[\tau\,\partial_{t}+\xi^{i}\partial_{x_{i}}-(\operatorname{div}\xi)\,u\,\partial_{u}\bigr]

ThenΦ\Phiis a Lie-algebra isomorphism𝔤Ito→≅𝔤SDEess⊆𝔤FPess.\mathfrak{g}_{\mathrm{Ito}}\;\xrightarrow{\ \cong\ }\;\mathfrak{g}_{\mathrm{SDE}}^{\mathrm{ess}}\subseteq\mathfrak{g}_{\mathrm{FP}}^{\mathrm{ess}}.

## Proof

## (1) Well-defined.

LetX=τ​∂t+ξi​∂xi∈𝔤ItoX=\tau\partial_{t}+\xi^{i}\partial_{x_{i}}\in\mathfrak{g}_{\mathrm{Ito}}.
By [Thm. 4][Gaeta and Quintero,1999],XXextends to an FP symmetryX+ϕ​∂u,ϕ=α+β​u,X+\phi\,\partial_{u},\qquad\phi=\alpha+\beta u,

withβ=−div⁡ξ+c0\beta=-\operatorname{div}\xi+c_{0}.
Imposing preservation of normalization, [AppendixB][Gaeta and Quintero,1999]forcesc0=0c_{0}=0andβ=−div⁡ξ\beta=-\operatorname{div}\xi.
Thusτ​∂t+ξi​∂xi−(div⁡ξ)​u​∂u\tau\partial_{t}+\xi^{i}\partial_{x_{i}}-(\operatorname{div}\xi)\,u\partial_{u}

is an FP symmetry, and its class moduloℐ\mathcal{I}definesΦ​(X)∈𝔤FPess\Phi(X)\in\mathfrak{g}_{\mathrm{FP}}^{\mathrm{ess}}.

## (2) Linearity.

Immediate from linearity of the divergence operator and of the quotient map.

## (3) Homomorphism property.

LetXa=τa​∂t+ξai​∂xi,Xb=τb​∂t+ξbi​∂xi,X_{a}=\tau_{a}\partial_{t}+\xi_{a}^{i}\partial_{x_{i}},\qquad X_{b}=\tau_{b}\partial_{t}+\xi_{b}^{i}\partial_{x_{i}},

and setYa:=Xa−(div⁡ξa)​u​∂u,Yb:=Xb−(div⁡ξb)​u​∂u.Y_{a}:=X_{a}-(\operatorname{div}\xi_{a})u\partial_{u},\qquad Y_{b}:=X_{b}-(\operatorname{div}\xi_{b})u\partial_{u}.

A direct computation of commutators on(t,x,u)(t,x,u)yields[Ya,Yb]=[Xa,Xb]−(Xa​(div⁡ξb)−Xb​(div⁡ξa))​u​∂u.[Y_{a},Y_{b}]=[X_{a},X_{b}]-\bigl(X_{a}(\operatorname{div}\xi_{b})-X_{b}(\operatorname{div}\xi_{a})\bigr)u\partial_{u}.

Writing[Xa,Xb]=τc​∂t+ξci​∂xi,[X_{a},X_{b}]=\tau_{c}\partial_{t}+\xi_{c}^{i}\partial_{x_{i}},

one hasdiv⁡ξc=Xa​(div⁡ξb)−Xb​(div⁡ξa),\operatorname{div}\xi_{c}=X_{a}(\operatorname{div}\xi_{b})-X_{b}(\operatorname{div}\xi_{a}),

and therefore[Ya,Yb]=τc​∂t+ξci​∂xi−(div⁡ξc)​u​∂u.[Y_{a},Y_{b}]=\tau_{c}\partial_{t}+\xi_{c}^{i}\partial_{x_{i}}-(\operatorname{div}\xi_{c})u\partial_{u}.

Passing to classes in the quotient gives[Φ​(Xa),Φ​(Xb)]=Φ​([Xa,Xb]),[\Phi(X_{a}),\Phi(X_{b})]=\Phi([X_{a},X_{b}]),

soΦ\Phipreserves Lie brackets.

## (4) Injective.

IfΦ​(X)=0\Phi(X)=0, then the representativeY=τ​∂t+ξi​∂xi−(div⁡ξ)​u​∂uY=\tau\partial_{t}+\xi^{i}\partial_{x_{i}}-(\operatorname{div}\xi)u\partial_{u}

lies inℐ\mathcal{I}.
But every element ofℐ\mathcal{I}has vanishing∂t\partial_{t}and∂xi\partial_{x_{i}}components, henceτ=ξ≡0\tau=\xi\equiv 0andX=0X=0.

## (5) Image and isomorphism.

By definition,𝔤SDEess\mathfrak{g}_{\mathrm{SDE}}^{\mathrm{ess}}consists exactly of the classesΦ​(X)\Phi(X)with(τ,ξ)(\tau,\xi)satisfying (3.4).
ThusIm​(Φ)=𝔤SDEess,\mathrm{Im}(\Phi)=\mathfrak{g}_{\mathrm{SDE}}^{\mathrm{ess}},

andΦ\Phiis a Lie-algebra isomorphism onto this subalgebra.□\square

## Remark (essential FP symmetries vs. superposition)

Because the FP equation is linear, its Lie point symmetry algebra contains the
infinite-dimensional family of solution-translation symmetriesXα=α​(t,x)​∂u,X_{\alpha}=\alpha(t,x)\partial_{u},

whereα\alphais any solution of the FP equation.
In [Thm. 3][Gaeta and Quintero,1999]these appear as theα\alpha-term inϕ=α+β​u\phi=\alpha+\beta uand are explicitly identified as the symmetries
implied by linear superposition.
Quotienting by the idealℐ={Xα}\mathcal{I}=\{X_{\alpha}\}

removes precisely these trivial directions and yields theessentialFP symmetry algebra𝔤FPess=𝔤FP/ℐ.\mathfrak{g}_{\mathrm{FP}}^{\mathrm{ess}}=\mathfrak{g}_{\mathrm{FP}}/\mathcal{I}.In this quotient, the mapΦ\Phiidentifies each genuine Itô symmetry(τ,ξ)(\tau,\xi)with the unique normalization-compatible FP symmetry class
whoseuu-component is fixed byβ=−div⁡ξ\beta=-\operatorname{div}\xi(cf.[Gaeta and Quintero,1999], Remark 11, equation (5.10), and AppendixB).

## Appendix FSDE–Fokker–Planck Subalgebra Validation

The theoretical relation in AppendixEimplies that projectable SDE symmetry generators embed into the Fokker–Planck symmetry algebra. Thus, learned SDE generators should form a subalgebra of the learned Fokker–Planck generators when both are projected to the common(τ,ξ)(\tau,\xi)-space, discarding theuu-component of the Fokker–Planck generators.

To test this relation empirically, we train both SDE and Fokker–Planck generators for Example 1 and compare the span of the learned SDE generators with the projected(τ,ξ)(\tau,\xi)-span of the learned Fokker–Planck generators using principal angles. The resulting angles are2.00∘,13.63∘,18.81∘.2.00^{\circ},\ 13.63^{\circ},\ 18.81^{\circ}.These small angles confirm that the learned SDE generators are recovered as a subalgebra of the learned Fokker–Planck generators, providing a direct quantitative validation of the SDE–Fokker–Planck connection beyond qualitative comparison.

## Appendix GPlots and Heat Maps of Learned SDE Symmetry Generators

In this section, we present plots and heatmaps of the learned symmetry generators. As discussed in the main text and in the principal-angle evaluation methodology, the discovered functions are generally close to linear combinations of the ground-truth symmetries associated with each SDE. Consequently, they may not admit direct interpretation in terms of functional form or scale relative to the underlying ground-truth symmetry functions. These visualizations are included primarily for completeness and to provide qualitative insight into the types of functions ultimately learned by LieStoNet.(a)τi​(t)\tau_{i}(t)(Example 1).(b)ξi​(t,x)\xi_{i}(t,x)(Example 1).Figure 4:Learned generator components for Example 1. Part (a): temporal componentτi​(t)\tau_{i}(t). Part (b): spatial componentξi​(t,x)\xi_{i}(t,x)visualized as heat maps.(a)τi​(t)\tau_{i}(t)(Example 2).(b)ξi​(t,x)\xi_{i}(t,x)(Example 2).Figure 5:Learned generator components for Example 2. Part (a):τi​(t)\tau_{i}(t). Part (b):ξi​(t,x)\xi_{i}(t,x)heat maps.(a)τi​(t)\tau_{i}(t)(Example 3).(b)ξi​(t,x)\xi_{i}(t,x)(Example 3).Figure 6:Learned generator components for Example 3. Part (a):τi​(t)\tau_{i}(t). Part (b):ξi​(t,x)\xi_{i}(t,x)heat maps.(a)τi​(t)\tau_{i}(t)(Example 4).(b)ξi​(t,x)\xi_{i}(t,x)(Example 4).Figure 7:Learned generator components for Example 4. Part (a):τi​(t)\tau_{i}(t). Part (b):ξi​(t,x)\xi_{i}(t,x)heat maps.

## Appendix HSensitivity to Surrogate Approximation Error

LieStoNet computes the symmetry losses using the learned neural SDE surrogate(f^,σ^)(\hat{f},\hat{\sigma}), so surrogate misspecification can affect the recovered generators. Let(f,σ)(f,\sigma)denote the true drift and diffusion,G⋆G^{\star}a true symmetry generator,G^\hat{G}a learned generator, andDf,σ​(⋅)D_{f,\sigma}(\cdot)the SDE determining-equation operator. A standard perturbation argument gives‖Df,σ​(G^)‖≤‖Df^,σ^​(G^)‖+C​(G^)​(‖f^−f‖C1+‖σ^−σ‖C1),\|D_{f,\sigma}(\hat{G})\|\;\leq\;\|D_{\hat{f},\hat{\sigma}}(\hat{G})\|+C(\hat{G})\Bigl(\|\hat{f}-f\|_{C^{1}}+\|\hat{\sigma}-\sigma\|_{C^{1}}\Bigr),

whereC​(G^)C(\hat{G})depends on the size and smoothness of the learned generator. Thus, the determining-equation residual under the true SDE is controlled by two terms: the residual minimized during training under the surrogate, and theC1C^{1}approximation error of the surrogate itself. Under a local stability condition for the determining operator, this implies that symmetry recovery degrades continuously with surrogate error (forC⋆C^{\star}being the local stability constant):infA∈G​L​(k)∥G^−AG⋆∥≤C⋆(∥Df^,σ^(G^)∥+\inf_{A\in GL(k)}\|\hat{G}-AG^{\star}\|\;\leq\;C^{\star}\Bigl(\|D_{\hat{f},\hat{\sigma}}(\hat{G})\|+∥f^−f∥C1+∥σ^−σ∥C1).\|\hat{f}-f\|_{C^{1}}+\|\hat{\sigma}-\sigma\|_{C^{1}}\Bigr).

Empirically, we perturb the surrogate in Example 1 using structured sine perturbations and random MLP perturbations. The maximum principal angle and determining-equation loss increase smoothly with perturbation amplitude, rather than exhibiting abrupt instability.δ\deltaSine perturbationRandom MLP perturbationθ\thetaL6L_{6}θ\thetaL6L_{6}01.8∘1.8^{\circ}3.7×10−23.7\times 10^{-2}2.1∘2.1^{\circ}4.2×10−24.2\times 10^{-2}0.023.1∘3.1^{\circ}5.8×10−25.8\times 10^{-2}2.2∘2.2^{\circ}4.5×10−24.5\times 10^{-2}0.112.2∘12.2^{\circ}9.6×10−29.6\times 10^{-2}2.8∘2.8^{\circ}1.1×10−11.1\times 10^{-1}0.535.9∘35.9^{\circ}1.2×10−11.2\times 10^{-1}14.8∘14.8^{\circ}2.1×10−12.1\times 10^{-1}Table 9:Sensitivity to surrogate perturbations.Hereδ\deltais perturbation amplitude,θ\thetais the maximum principal angle, andL6L_{6}is the SDE determining-equation loss. Recovery degrades smoothly as the surrogate is perturbed.

## Appendix IComputational Overhead of Loss Terms

The main computational cost in Stage 2 comes from repeated automatic differentiation of the generator networks, especially for losses involving Jacobians and Hessians. LetDg(1)D_{g}^{(1)}andDg(2)D_{g}^{(2)}denote the cost of evaluating first- and second-order derivatives of one generator network,BBthe number of sampled space–time points in a minibatch,mmthe number of learned generators,nnthe state dimension, andNNthe number of subsampled trajectory time points. The algebraic and SDE-validity losses scale polynomially in these quantities:L1,L3\displaystyle L_{1},L_{3}=O​(B​(m​Dg(1)+m2)),\displaystyle=O\!\left(B(mD_{g}^{(1)}+m^{2})\right),\qquadL2\displaystyle L_{2}=O​(B​(m​Dg(2)+m3)),\displaystyle=O\!\left(B(mD_{g}^{(2)}+m^{3})\right),L4\displaystyle L_{4}=O​(B​(m​Dg(1)+m3)),\displaystyle=O\!\left(B(mD_{g}^{(1)}+m^{3})\right),\qquadL6\displaystyle L_{6}=O​(B​m​Dg(2)),\displaystyle=O(BmD_{g}^{(2)}),\qquadL7\displaystyle L_{7}=O​(2​n​N​m​Dg(2)).\displaystyle=O(2nNmD_{g}^{(2)}).

Thus the cost grows polynomially rather than combinatorially in the number of generators.

We also measure per-loss wall-clock time for one representative setting,m=3m=3,B=2048B=2048, on an NVIDIA H100 GPU. The finite-step after-push lossL7L_{7}is the most expensive term, while the algebraic losses together account for roughly half of the measured total. This overhead is empirically useful: the ablation in AppendixOshows that removing the algebraic losses substantially worsens symmetry recovery.LossL1L_{1}L2L_{2}L3L_{3}L4L_{4}L5L_{5}L6L_{6}L7L_{7}Time (ms)0.430.760.380.520.470.472.15Table 10:Per-loss wall-clock time.Measured form=3m=3,B=2048B=2048, on an NVIDIA H100 GPU.

## Appendix JComplete Lie Point Symmetry Derivation for Example 1:d​x=σ0​d​W​(t)dx=\sigma_{0}dW(t)

We recall from Theorem2.1that a symmetry generator for an SDE must satisfy the determining equationsξt+f​ξx−ξ​fx−∂t(f​τ)+12​σ2​ξx​x=0,\xi_{t}+f\xi_{x}-\xi f_{x}-\partial_{t}(f\tau)+\tfrac{1}{2}\sigma^{2}\xi_{xx}=0,σ​ξx−ξ​σx−τ​σt−12​σ​τt=0.\sigma\xi_{x}-\xi\sigma_{x}-\tau\sigma_{t}-\tfrac{1}{2}\sigma\tau_{t}=0.

Withf=0,σ=σ0f=0,\sigma=\sigma_{0}the determining equations becomeξt+12​σ02​ξx​x=0\xi_{t}+\frac{1}{2}\sigma_{0}^{2}\xi_{xx}=0andξx=12​τt\xi_{x}=\frac{1}{2}\tau_{t}. Sinceτ\tauis only a function oftt, the second one implies thatξ\xiis linear inxx, substituting which into the first one givesξt=0\xi_{t}=0. Thus,ξ​(t,x)=c1​x+c2\xi(t,x)=c_{1}x+c_{2}. Substituting this inξx=12​τt\xi_{x}=\frac{1}{2}\tau_{t}and solving givesτ​(t)=2​c1​t+c3\tau(t)=2c_{1}t+c_{3}. Thus, a general symmetry has the formX0=τ​(t)​∂t+ξ​(x)​∂x=(2​c1​t+c3)​∂t+(c1​x+c2)​∂x.X_{0}=\tau(t)\partial_{t}+\xi(x)\partial_{x}=(2c_{1}t+c_{3})\partial_{t}+(c_{1}x+c_{2})\partial_{x}.

We find that there are three independent constants of integration implying that the symmetry Lie algebra is three dimensional. Choosing one constant as non-zero while others being zero gives a simple basis for these generators producing:c3=1:v1\displaystyle c_{3}=1:v_{1}=∂t\displaystyle=\partial_{t}c2=1:v2\displaystyle c_{2}=1:v_{2}=∂x\displaystyle=\partial_{x}c1=1:v3\displaystyle c_{1}=1:v_{3}=2​t​∂t+x​∂x\displaystyle=2t\partial_{t}+x\partial_{x}

## Appendix KComplete Lie Point symmetry derivation for example 2:d​x=x​d​t+d​W​(t)dx=xdt+dW(t)

In this case, withf=x,σ=1f=x,\sigma=1, the second determining equation givesξx=12​τt\xi_{x}=\frac{1}{2}\tau_{t}. Differentiating w.r.t.xxand then integrating givesξ​(t,x)=a​(t)​x+b​(t)\xi(t,x)=a(t)x+b(t)implyingτt=2​a​(t)\tau_{t}=2a(t). We now plug these into the first equation resulting ina′​(t)​x+(b′​(t)−b​(t))−x​τt=0a^{\prime}(t)x+\big(b^{\prime}(t)-b(t)\big)-x\tau_{t}=0

Since this is a linear expression inxxthat’s identically 0, the coefficients must be 0 separately, producinga′=τta^{\prime}=\tau_{t},b′=bb^{\prime}=b. Combined withτt=2​a​(t)\tau_{t}=2a(t)this givesa​(t)=c1​e2​t,b​(t)=c2​eta(t)=c_{1}e^{2t},b(t)=c_{2}e^{t}. Substituting these into our previous expressions forξ,τ\xi,\tauwe get that a general symmetry has the form:X=(c1​e2​t+c3)​∂t+(c1​e2​t​x+c2​et)​∂xX=\big(c_{1}e^{2t}+c_{3}\big)\partial_{t}+\big(c_{1}e^{2t}x+c_{2}e^{t}\big)\partial_{x}

Similarly as before, choosing values for the constants with one non-zero constant at a time gives the following three generators as a basis:c3=1:v1\displaystyle c_{3}=1:v_{1}=∂t\displaystyle=\partial_{t}c2=1:v2\displaystyle c_{2}=1:v_{2}=et​∂x\displaystyle=e^{t}\partial_{x}c1=1:v3\displaystyle c_{1}=1:v_{3}=e2​t​(∂t+x​∂x)\displaystyle=e^{2t}(\partial_{t}+x\partial_{x})

## Appendix LComplete Lie Point Symmetry Derivation for Example 3:d​x=y​d​tdx=ydt,d​y=−k2​y​d​t+2​k2​d​W​(t)dy=-k^{2}ydt+\sqrt{2k^{2}}dW(t)

This is a two dimensional example with drift and diffusion given by:f=(y−k2​y),σ=(0002​k2)f=\begin{pmatrix}y\\
-k^{2}y\end{pmatrix},\;\;\sigma=\begin{pmatrix}0&0\\
0&\sqrt{2k^{2}}\end{pmatrix}

The general symmetry looks likeX0=τ​(t)​∂t+ξ1​(t,x,y)​∂x+ξ2​(t,x,y)​∂yX_{0}=\tau(t)\partial_{t}+\xi^{1}(t,x,y)\partial_{x}+\xi^{2}(t,x,y)\partial_{y}

with the determining equations as∂tξi+fj​∂jξi−ξj​∂jfi−∂t(fi​τ)+12​(σ​σT)j​k​∂j​k2ξi=0,\partial_{t}\xi^{i}+f^{j}\partial_{j}\xi^{i}-\xi^{j}\partial_{j}f^{i}-\partial_{t}(f^{i}\tau)+\tfrac{1}{2}(\sigma\sigma^{T})^{jk}\partial^{2}_{jk}\xi^{i}=0,(σj∂jk)ξi−(ξj∂j)σi−kτ∂tσi−k12σi,kτt=0.(\sigma^{j}{}_{k}\partial_{j})\xi^{i}-(\xi^{j}\partial_{j})\sigma^{i}{}_{k}-\tau\partial_{t}\sigma^{i}{}_{k}-\tfrac{1}{2}\sigma^{i}{}_{k},\tau_{t}=0.

We first use the second equation to constrainξ1,ξ2\xi^{1},\xi^{2}. Sinceσ22\sigma^{2}_{2}is the only non-zero component, the non-trivial constraints come fromk=2k=2.
- •

For (i=1,k=2i=1,k=2):(σj​∂j2⁡ξ1=0⇒∂yξ1=0)(\sigma^{j}{}_{2}\partial_{j}\xi^{1}=0\Rightarrow\partial_{y}\xi^{1}=0). Thus,ξ1=a​(x,t)\xi^{1}=a(x,t)(noyy-dependence).
- •

For (i=2,k=2i=2,k=2):(σj​∂j2⁡ξ2−12​σ2​τt2=0⇒∂yξ2=12​τt)(\sigma^{j}{}_{2}\partial_{j}\xi^{2}-\tfrac{1}{2}\sigma^{2}{}_{2}\tau_{t}=0\Rightarrow\partial_{y}\xi^{2}=\tfrac{1}{2}\tau_{t}).
Henceξ2=12​τt​y+g​(x,t).\xi^{2}=\tfrac{1}{2}\tau_{t}y+g(x,t).

We now use the first determining equation. Note thatσ​σT=diag​(0,2​k2)\sigma\sigma^{T}=\mathrm{diag}(0,2k^{2}), so the diffusion term is12​(σ​σT)j​k​∂j​k2ξi=k2​∂y​y2ξi\tfrac{1}{2}(\sigma\sigma^{T})^{jk}\partial^{2}_{jk}\xi^{i}=k^{2}\partial^{2}_{yy}\xi^{i}; butξ1\xi^{1}is independent ofyy, andξ2\xi^{2}is at most linear inyy, so∂y​y2ξi=0\partial^{2}_{yy}\xi^{i}=0and the diffusion term drops out for the first equation for bothi=1,2i=1,2. The first determining equation then gives
- •

Fori=1i=1, withf1=yf^{1}=y,f2=−k2​yf^{2}=-k^{2}y, one getsat+y​ax−ξ2−y​τt=0a_{t}+ya_{x}-\xi^{2}-y\tau_{t}=0. Substituteξ2=12​τt​y+g​(x,t)\xi^{2}=\tfrac{1}{2}\tau_{t}y+g(x,t)to getat−g+y​(ax−32​τt)=0a_{t}-g+y\Big(a_{x}-\tfrac{3}{2}\tau_{t}\Big)=0. Thusax=32​τt,g=at.a_{x}=\tfrac{3}{2}\tau_{t},\ \ g=a_{t}.
- •

Fori=2i=2the first determining equation on substituting the drift and diffusion gives(12​τt​t​y+gt)+(y​gx−12​k2​τt​y)\left(\tfrac{1}{2}\tau_{tt}y+g_{t}\right)+\left(yg_{x}-\tfrac{1}{2}k^{2}\tau_{t}y\right)+k2​(12​τt​y+g)+k2​y​τt=0+k^{2}\left(\tfrac{1}{2}\tau_{t}y+g\right)+k^{2}y\tau_{t}=0

which on simplifying isy​(12​τt​t+gx+k2​τt)+(gt+k2​g)=0.y\Big(\tfrac{1}{2}\tau_{tt}+g_{x}+k^{2}\tau_{t}\Big)+\big(g_{t}+k^{2}g\big)=0.

Since a linear expression inyybeing identically 0 implies that the coefficients are each 0, we getgt+k2​g=0{g_{t}+k^{2}g=0}and12​τt​t+gx+k2​τt=0{\tfrac{1}{2}\tau_{tt}+g_{x}+k^{2}\tau_{t}=0}.
In the second equation, we use the fact thatgx=at​x=32​τt​tg_{x}=a_{tx}=\frac{3}{2}\tau_{tt}, giving us2​τt​t+k2​τt=02\tau_{tt}+k^{2}\tau_{t}=0.

Integratingax=32​τta_{x}=\frac{3}{2}\tau_{t}with respect toxxgivesa​(x,t)=32​τt​x+h​(t)a(x,t)=\frac{3}{2}\tau_{t}x+h(t)for somehh. Theng=at=32​τt​t​x+h′​(t)g=a_{t}=\frac{3}{2}\tau_{tt}x+h^{\prime}(t). Substituting this ingt+k2​g=0g_{t}+k^{2}g=0gives32​x​(τt​t​t+k2​τt​t)+h′′+k2​h=0.\frac{3}{2}x(\tau_{ttt}+k^{2}\tau_{tt})+h^{\prime\prime}+k^{2}h=0.

The coefficient ofxxmust be 0 for this expression to be identically 0, thusτt​t​t+k2​τt​t=0\tau_{ttt}+k^{2}\tau_{tt}=0. Along with the previously found relation2​τt​t+k2​τt=02\tau_{tt}+k^{2}\tau_{t}=0, this yieldsτt​t=0\tau_{tt}=0thus implyingτt=0\tau_{t}=0i.e.τ​(t)=c1\tau(t)=c_{1}.
Usingτt=c1\tau_{t}=c_{1}inax=32​τta_{x}=\frac{3}{2}\tau_{t}impliesa​(x,t)=a​(t)a(x,t)=a(t)is independent ofxx. Thus,g​(x,t)=atg(x,t)=a_{t}is also independent ofxx. Solvinggt+kg=0g_{t}+k^{g}=0yieldsg​(t)=c2​r−k2​tg(t)=c_{2}r^{-k^{2}t}. Substituting this and integratingg=atg=a_{t}givesa​(t)=c3−c2k2​e−k2​ta(t)=c_{3}-\frac{c_{2}}{k^{2}}e^{-k^{2}t}. Thus, a general symmetry looks like:X=c1​∂t+(c3−c2k2​e−k2​t)​∂x+c2​e−k2​t​∂y.X=c_{1}\partial_{t}+\left(c_{3}-\frac{c_{2}}{k^{2}}e^{-k^{2}t}\right)\partial_{x}+c_{2}e^{-k^{2}t}\partial_{y}.

Choosing one constant non-zero at a time while others as zero gives the following set as generators:c1=1:v1\displaystyle c_{1}=1:v_{1}=∂t\displaystyle=\partial_{t}c3=1:v2\displaystyle c_{3}=1:v_{2}=∂x\displaystyle=\partial_{x}c2=1:v3\displaystyle c_{2}=1:v_{3}=e−k2​t​(k−2​∂x−∂y)\displaystyle=e^{-k^{2}t}(k^{-2}\partial_{x}-\partial_{y})

## Appendix MComplete Lie Point Symmetry Derivation for Example 4:d​x=(a1/x)​d​t+d​W1;dx=(a_{1}/x)dt+dW_{1};d​y=a2​d​t+d​W2dy=a_{2}dt+dW_{2}f=(a1/xa2),σ=(1001)f=\begin{pmatrix}a_{1}/x\\
a_{2}\end{pmatrix},\;\;\sigma=\begin{pmatrix}1&0\\
0&1\end{pmatrix}

Once again, the general symmetry looks likeX0=τ​(t)​∂t+ξ1​(t,x,y)​∂x+ξ2​(t,x,y)​∂yX_{0}=\tau(t)\partial_{t}+\xi^{1}(t,x,y)\partial_{x}+\xi^{2}(t,x,y)\partial_{y}

with the determining equations as∂tξi+fj​∂jξi−ξj​∂jfi−∂t(fi​τ)+12​(σ​σT)j​k​∂j​k2ξi=0,\partial_{t}\xi^{i}+f^{j}\partial_{j}\xi^{i}-\xi^{j}\partial_{j}f^{i}-\partial_{t}(f^{i}\tau)+\tfrac{1}{2}(\sigma\sigma^{T})^{jk}\partial^{2}_{jk}\xi^{i}=0,(σj∂jk)ξi−(ξj∂j)σi−kτ∂tσi−k12σi,kτt=0.(\sigma^{j}{}_{k}\partial_{j})\xi^{i}-(\xi^{j}\partial_{j})\sigma^{i}{}_{k}-\tau\partial_{t}\sigma^{i}{}_{k}-\tfrac{1}{2}\sigma^{i}{}_{k},\tau_{t}=0.

σ\sigmais constant so that(ξ⋅∇)​σ=0=∂tσ(\xi\cdot\nabla)\sigma=0=\partial_{t}\sigma. Again, we use the second equation to get the form ofξ\xi, which gives us∂kξi−12​δki​τt=0\partial_{k}\xi^{i}-\frac{1}{2}\delta^{i}_{k}\tau_{t}=0. For differenti,ki,kwe have:i=1,k=1:ξx1=12​τti=1,k=1:\xi^{1}_{x}=\frac{1}{2}\tau_{t}i=1,k=2:ξy1=0i=1,k=2:\xi^{1}_{y}=0i=2,k=1:ξx2=0i=2,k=1:\xi^{2}_{x}=0i=2,k=2:ξy2=12​τti=2,k=2:\xi^{2}_{y}=\frac{1}{2}\tau_{t}

Integrating these givesξ1​(t,x,y)=12​τt​(t)​x+g1​(t){\ \xi^{1}(t,x,y)=\frac{1}{2}\tau_{t}(t)x+g_{1}(t)\ }ξ2​(t,x,y)=12​τt​(t)​y+g2​(t)\xi^{2}(t,x,y)=\frac{1}{2}\tau_{t}(t)y+g_{2}(t)

Thus,ξ\xiare at most linear inx,yx,yand second spatial derivatives all vanish. The first determining equation fori=1i=1on plugging the expressions forξ1,ξ2\xi^{1},\xi^{2}, along with the drift and diffusion functions gives the following.
- •

Fori=1i=1this gives12​τt​t​x+g1′​(t)+a1​g1​(t)x2=0.\tfrac{1}{2}\tau_{tt}x+g_{1}^{\prime}(t)+\frac{a_{1}g_{1}(t)}{x^{2}}=0.\

For this equality to hold, the coefficients of various powers ofxxshould separately be0. Thus we getτt​t=0=g1​(t)\tau_{tt}=0=g_{1}(t). Hence,τ​(t)=c1​t+c2,ξ1​(x,y,t)=c12​x.\tau(t)=c_{1}t+c_{2},\ \ \ \xi^{1}(x,y,t)=\frac{c_{1}}{2}x.
- •

Fori=2i=2the determining equation gives12​τt​t​y+g2′−a22​τt=0.\frac{1}{2}\tau_{tt}y+g_{2}^{\prime}-\frac{a_{2}}{2}\tau_{t}=0.

Equating coefficients inyygivesτt​t=0\tau_{tt}=0(consistent with earlier) andg2′=a22​τt=a22​c1g_{2}^{\prime}=\frac{a_{2}}{2}\tau_{t}=\frac{a_{2}}{2}c_{1}. On integrating the last equation we getg2​(t)=a22​c1​t+c3g_{2}(t)=\frac{a_{2}}{2}c_{1}t+c_{3}.

The general symmetry thus looks likeX=(c1​t+c2)​∂t+c12​x​∂x+(c12​(y+a2​t)+c3)​∂y.X=(c_{1}t+c_{2})\partial_{t}+\frac{c_{1}}{2}x\partial_{x}+\left(\frac{c_{1}}{2}(y+a_{2}t)+c_{3}\right)\partial_{y}.

Choosing one constant as non-zero at a time gives the following basis of generators:c2=1:v1\displaystyle c_{2}=1:v_{1}=∂t\displaystyle=\partial_{t}c3=1:v2\displaystyle c_{3}=1:v_{2}=∂y\displaystyle=\partial_{y}c1=1:v3\displaystyle c_{1}=1:v_{3}=2​t​∂t+x​∂x+(y+a2​t)​∂y\displaystyle=2t\partial_{t}+x\partial_{x}+(y+a_{2}t)\partial_{y}

## Appendix NComplete Derivation for Fokker-Planck Symmetries for Example 1:d​x=σ0​d​w​(t)dx=\sigma_{0}dw(t)

For the 1-d brownian motiond​x=σ0​d​w​(t)dx=\sigma_{0}dw(t), the associated FP equation isut=σ022​ux​xu_{t}=\frac{\sigma_{0}^{2}}{2}u_{xx}. Following the notation from (5)
, this meansA=−σ022,B=0,C=0A=-\frac{\sigma_{0}^{2}}{2},B=0,C=0. The three FP determining equations from theorem2.2boil down to:ξx=12​τt,−ξt+2​A​βx−A​ξx​x=0,βt+A​βx​x=0.\xi_{x}=\frac{1}{2}\tau_{t},\ \ -\xi_{t}+2A\beta_{x}-A\xi_{xx}=0,\ \ \beta_{t}+A\beta_{xx}=0.

The first equation easily solves toξ​(t,x)=12​τt​(t)​x+k​(t)\xi(t,x)=\frac{1}{2}\tau_{t}(t)x+k(t)wherek​(t)k(t)is any function oftt. Substituting this result into the second equation givesβx=12​A​(12​τt​t​x+k′)=τt​t4​A​x+k′2​A\beta_{x}=\frac{1}{2A}\left(\frac{1}{2}\tau_{tt}x+k^{\prime}\right)=\frac{\tau_{tt}}{4A}x+\frac{k^{\prime}}{2A}

which upon integrating with respect toxxgives:β​(t,x)=τt​t8​A​x2+k′2​A​x+m​(t)\beta(t,x)=\frac{\tau_{tt}}{8A}x^{2}+\frac{k^{\prime}}{2A}x+m(t)

for somem​(t)m(t). Substituting this into the third equation givesβt+A​βx​x=(τt​t​t8​A​x2+k′′2​A​x+m′​(t))+A⋅τt​t4​A=0\beta_{t}+A\beta_{xx}=\left(\frac{\tau_{ttt}}{8A}x^{2}+\frac{k^{\prime\prime}}{2A}x+m^{\prime}(t)\right)+A\cdot\frac{\tau_{tt}}{4A}=0

This is a quadratic inxxwhich is identically 0. Thus, each coefficient in the quadratic must vanish separately, giving usτt​t​t=0,k′′=0,m′​(t)+14​τt​t=0.\tau_{ttt}=0,\ \ k^{\prime\prime}=0,\ \ m^{\prime}(t)+\frac{1}{4}\tau_{tt}=0.

Integrating these gives:τ​(t)=a​t2+b​t+c,k​(t)=d​t+e,m​(t)=−a2​t+f.{\tau(t)=at^{2}+bt+c},\quad{k(t)=dt+e},\quad{m(t)=-\frac{a}{2}t+f}.

Substituting these into expressions forβ\betaandξ\xifrom earlier, we get:τ=a​t2+b​t+c\tau=at^{2}+bt+cξ=12​τt​x+d​t+e\xi=\tfrac{1}{2}\tau_{t}x+dt+eβ=τt​t8​A​x2+d2​A​x−a2​t+f.\beta=\frac{\tau_{tt}}{8A}x^{2}+\frac{d}{2A}x-\frac{a}{2}t+f.

Thus, there are six independent parameters/constantsa,b,c,d,e,fa,b,c,d,e,fresulting in a six dimensional vector space for the set of symmetries. We may choose any 6 linearly independent vectors for(a,b,c,d,e,f)(a,b,c,d,e,f)to get a vector-space basis for the Lie algebra. We choose the 6 vectors where each of the parameters except for one parameter is zero. Using these choices in the general expression for a symmetry,V=τ​∂t+ξ​∂x+β​u​∂uV=\tau\partial_{t}+\xi\partial_{x}+\beta u\partial_{u}, gives us the following six familiar set of symmetry generators:c=1:v1\displaystyle c=1:v_{1}=∂t\displaystyle=\partial_{t}e=1:v2\displaystyle e=1:v_{2}=∂x\displaystyle=\partial_{x}f=1:v3\displaystyle f=1:v_{3}=u​∂u\displaystyle=u\partial_{u}d=1:v4\displaystyle d=1:v_{4}=t​∂x−xσ02​u​∂u\displaystyle=t\partial_{x}-\frac{x}{\sigma_{0}^{2}}u\partial_{u}b=1:v5\displaystyle b=1:v_{5}=t​∂t+x2​∂x\displaystyle=t\partial_{t}+\frac{x}{2}\partial_{x}a=1:v6\displaystyle a=1:v_{6}=t2​∂t+t​x​∂x−12​(t+x2σ02)​u​∂u\displaystyle=t^{2}\partial_{t}+tx\partial_{x}-\frac{1}{2}\Bigl(t+\frac{x^{2}}{\sigma_{0}^{2}}\Bigr)u\partial_{u}ExampleState(T,Δ​t)(T,\Delta t)NNntrajn_{\mathrm{traj}}(Stage 1)B=ntraj​NB=n_{\mathrm{traj}}NStage-1 surrogate1 (Brownian)1D(5.0,0.01)(5.0,\,0.01)50020481,024,000MLP[2,64,64,2][2,64,64,2],tanh,σ^=softplus+10−3\hat{\sigma}=\mathrm{softplus}+10^{-3}2 (d​x=x​d​t+σ​d​Wdx=x\,dt+\sigma dW)1D(5.0,0.01)(5.0,\,0.01)500512256,000MLP[2,64,64,2][2,64,64,2],tanh, i.i.d. increment dataset over|x|≤2|x|\leq 23 (2D linear)2D(2.0,0.01)(2.0,\,0.01)2002048409,600MLP[3,64,64,4][3,64,64,4],tanh, diagonalσ^∈ℝ2\hat{\sigma}\in\mathbb{R}^{2}4 (2D, PSD diffusion)2D(2.0,0.01)(2.0,\,0.01)2002048409,600Drift MLP + Cholesky MLP,swish,Σ=L​L⊤\Sigma=LL^{\top}Table 11:Stage-1 (surrogate) dataset sizes and architectures. HereN=⌊T/Δ​t⌋N=\lfloor T/\Delta t\rfloorandBBcounts increment samples (one per time step per trajectory).

## Appendix OAblation Study for Generator-Training Losses

We ablate the generator-training lossesL1,…,L7L_{1},\ldots,L_{7}by removing one loss at a time while keeping all other experimental settings fixed. The results are shown in table12. In both examples, removing any single loss term worsens recovery, as measured by the maximum principal angle between the learned and analytic symmetry-algebra spans. This supports the practical role of each loss in addition to its theoretical motivation.

The degradation is consistent with the intended function of the losses. RemovingL1L_{1}, which enforces Lie-bracket closure, orL6L_{6}, which enforces the SDE determining equations, causes the largest deterioration. RemovingL2L_{2}andL3L_{3}, corresponding to algebraic identities, has a milder effect in Example 2 but a stronger effect in Example 1. RemovingL7L_{7}, the finite-step after-push loss, also degrades performance, indicating that the local infinitesimal constraints inL6L_{6}alone are not sufficient for robust recovery in practice.Fullw/oL1L_{1}w/oL2L_{2}w/oL3L_{3}w/oL4L_{4}w/oL5L_{5}w/oL6L_{6}w/oL7L_{7}Example 16.26∘6.26^{\circ}55.56∘55.56^{\circ}25.89∘25.89^{\circ}35.05∘35.05^{\circ}36.60∘36.60^{\circ}39.77∘39.77^{\circ}86.78∘86.78^{\circ}44.54∘44.54^{\circ}Example 219.37∘19.37^{\circ}72.37∘72.37^{\circ}25.81∘25.81^{\circ}26.56∘26.56^{\circ}37.86∘37.86^{\circ}42.62∘42.62^{\circ}86.39∘86.39^{\circ}57.00∘57.00^{\circ}Table 12:Ablation of generator-training losses.Entries are maximum principal angles between learned and analytic symmetry-algebra spans; smaller is better. “Full” uses all lossesL1,…,L7L_{1},\ldots,L_{7}, while each ablated column removes exactly one loss.

## Appendix PImplementation Details for Learning SDE Symmetries

This section documents the exact experimental/implementation choices used in the accompanying notebooks forSDE symmetry learning(all Fokker–Planck symmetry components are intentionally omitted). Across all examples, the pipeline has two stages:
- 1.

Neural SDE surrogate (Stage 1).Fit a neural surrogate for the drift and diffusion from increment data using an increment-likelihood objective.
- 2.

Generator learning (Stage 2).Fit neural symmetry generators(τ,ξ)(\tau,\xi)(and an auxiliaryβ\betahead for code-compatibility that isunusedfor the SDE-only write-up) by minimizing a weighted sum of algebraic consistency terms (closure/Jacobi/etc.) and the Ito determining equations / pushforward constraints computed using the learned surrogate coefficients.

All notebooks run injaxwithjax_enable_x64=Trueand use float64 throughout for stability.

## P.0.1Stage 1: Neural SDE surrogate training

## Increment dataset construction.

Lettn=n​Δ​tt_{n}=n\Delta twithΔ​t=dt\Delta t=\texttt{dt}andn=0,…,N−1n=0,\dots,N-1, whereN=⌊T/Δ​t⌋N=\lfloor T/\Delta t\rfloor. The Stage-1 dataset consists of pairs(zn,Δ​Xn)\bigl(z_{n},\Delta X_{n}\bigr)whereΔ​Xn=Xn+1−Xn\Delta X_{n}=X_{n+1}-X_{n}andzn={(tn,xn)(1D examples)(tn,xn,yn)(2D time-dependent example)(xn,yn)(2D time-homogeneous example)z_{n}=\begin{cases}(t_{n},x_{n})&\text{(1D examples)}\\
(t_{n},x_{n},y_{n})&\text{(2D time-dependent example)}\\
(x_{n},y_{n})&\text{(2D time-homogeneous example)}\end{cases}

For simulated path data (Examples 1, 3, 4), the notebook forms all increments from the full trajectory bank, yieldingB=ntraj⋅NB=n_{\mathrm{traj}}\cdot Ntraining samples. Example 2 is special: Stage 1 is built as ani.i.d. increment datasetby sampling(t,x)(t,x)values and drawingΔ​x\Delta xdirectly from the Euler increment distribution for the target SDE; a pseudo-“trajectory” tensor is only created for downstream API compatibility.

## Input normalization.

In all Stage-1 surrogates, inputs are z-scored:z~=(z−μz)/(σz+10−8),\tilde{z}=(z-\mu_{z})/(\sigma_{z}+10^{-8}),

where(μz,σz)(\mu_{z},\sigma_{z})are empirical mean/std over the full Stage-1 input cloud.

## Surrogate parameterizations and likelihood.
- •

Examples 1 & 2 (1D).A single MLP mapsz~=(t~,x~)\tilde{z}=(\tilde{t},\tilde{x})to two outputs(f^,g)(\hat{f},g), with diffusion enforced positive viaσ^​(z~)=softplus​(g​(z~))+σmin.\hat{\sigma}(\tilde{z})=\mathrm{softplus}(g(\tilde{z}))+\sigma_{\min}.

The increment model isΔ​x∼𝒩​(f^​Δ​t,σ^2​Δ​t)\Delta x\sim\mathcal{N}(\hat{f}\,\Delta t,\;\hat{\sigma}^{2}\,\Delta t)and the loss is the per-sample Gaussian negative log-likelihood (dropping constants) averaged over minibatches.
- •

Example 3 (2D, diagonal diffusion).A single MLP mapsz~=(t~,x~,y~)\tilde{z}=(\tilde{t},\tilde{x},\tilde{y})to(f^x,f^y,gx,gy)(\hat{f}_{x},\hat{f}_{y},g_{x},g_{y})and setsσ^i=softplus​(gi)+σmin\hat{\sigma}_{i}=\mathrm{softplus}(g_{i})+\sigma_{\min}. The likelihood is a factorized diagonal Gaussian forΔ​(x,y)\Delta(x,y).
- •

Example 4 (2D, PSD diffusion via Cholesky).Two MLPs are trained: a drift networkf^​(x,y)\hat{f}(x,y)and a diffusion-Cholesky network returning(ℓ11raw,ℓ21,ℓ22raw)(\ell_{11}^{\rm raw},\ell_{21},\ell_{22}^{\rm raw}), withℓ11\displaystyle\ell_{11}=softplus​(ℓ11raw)+σfloor\displaystyle=\mathrm{softplus}(\ell_{11}^{\rm raw})+\sigma_{\rm floor}ℓ22\displaystyle\ell_{22}=softplus​(ℓ22raw)+σfloor,\displaystyle=\mathrm{softplus}(\ell_{22}^{\rm raw})+\sigma_{\rm floor},L\displaystyle L=(ℓ110ℓ21ℓ22);Σ=L​L⊤.\displaystyle=\begin{pmatrix}\ell_{11}&0\\
\ell_{21}&\ell_{22}\end{pmatrix};\Sigma=LL^{\top}.

The increment model is multivariate GaussianΔ​X∼𝒩​(f^​Δ​t,Σ​Δ​t)\Delta X\sim\mathcal{N}(\hat{f}\,\Delta t,\;\Sigma\,\Delta t).

## Regularization and optimizers.
- •

Examples 1/2/3:The Stage-1 objective adds explicit L2 weight decay asweight_decay * l2_tree(params)(even though the optimizer is plain Adam). Optimization usesoptax.adam(lr)with minibatches sampledwithout replacementfrom the full increment dataset each step.
- •

Example 4:Drift and diffusion-Cholesky networks are optimized with separateadamwoptimizers (weight_decay=0=0) and global-norm gradient clipping. Training alternates multiple drift steps and fewer diffusion steps per outer iteration. Additional diffusion regularizers are used: (i) a JVP-based smoothness penalty onL​(x,y)L(x,y), (ii) a minibatch variance stabilizer ondiag​(L)\mathrm{diag}(L), and (iii) a whitening/calibration penalty encouragingz=LΔ​t−1​(Δ​X−f^​Δ​t)∼𝒩​(0,I)z=L_{\Delta t}^{-1}(\Delta X-\hat{f}\Delta t)\sim\mathcal{N}(0,I).

## P.0.2Stage 2: Symmetry generator parameterization and training

## Training point cloud for Stage 2.

All generator losses are evaluated on minibatches of a point cloud in the extended space(t,x)(t,x)or(t,x,y)(t,x,y):𝒯={(tn,xn)}​or​{(tn,xn,yn)}.\mathcal{T}=\{(t_{n},x_{n})\}\ \text{or}\ \{(t_{n},x_{n},y_{n})\}.

The source of this cloud differs by example:
- •

Examples 1 & 2:simulate the learned surrogate by Euler–Maruyama usingCFGGenwithntraj=256n_{\mathrm{traj}}=256, and flatten all(N+1)(N{+}1)states, givingBgen=ntraj​(N+1)B_{\rm gen}=n_{\mathrm{traj}}(N{+}1)points.
- •

Example 3:simulate the learned surrogate withntraj=256n_{\mathrm{traj}}=256but additionally (i) enforce domain control inx∈[xmin,xmax]x\in[x_{\min},x_{\max}]via clipping at evaluation time and reflection after stepping, (ii) optionallyoversamplecandidate trajectories (traj_balance_oversample=12) and greedily select a subset whose histogram occupancy overxx-bins is closer to uniform, and (iii) build𝒯\mathcal{T}as a fixed-sizemixtureof trajectory points and uniform box samples with fractiontx_mix_uniform_frac=0.7(total point count kept constant).
- •

Example 4:constructsTX_gendirectly from the available(t,X​Y)(t,XY)tensor by flattening all observed path states, yieldingBgen=ntraj​(N+1)B_{\rm gen}=n_{\mathrm{traj}}(N{+}1)points with the full data trajectory bank. Its minibatch sampler mixes half empirical points and half uniform box samples in bounds inferred fromTX_gen, with anxx-floor to avoid instability nearx=0x=0.ExampleStepsBatchOptimizerLR(s)Weight decayExtra regularizers110,0004096Adam3×10−33\!\times\!10^{-3}10−610^{-6}(explicit L2)—22,0004096Adam3×10−33\!\times\!10^{-3}10−610^{-6}(explicit L2)—310,0004096Adam3×10−33\!\times\!10^{-3}10−610^{-6}(explicit L2)—420,000 outer8192AdamW + clip (separate for drift/diff)2×10−32\!\times\!10^{-3}(drift),10−310^{-3}(diff)0JVP-smooth (10−310^{-3}), var (5×10−45\!\times\!10^{-4}), whiten (5×10−35\!\times\!10^{-3})Table 13:Stage-1 (surrogate) optimization settings. Example 4 alternatesdrift_steps_per_iter=3anddiff_steps_per_iter=1inside each outer step.

## Generator neural architectures.

Each generatori=1,…,mi=1,\dots,mis represented by neural fields:τi​(t)∈ℝ,ξi​(t,x)∈ℝ​(1D)orξi​(t,x,y)∈ℝ2​(2D).\tau_{i}(t)\in\mathbb{R},\ \ \xi_{i}(t,x)\in\mathbb{R}\ \text{(1D)}\ \ \text{or}\ \ \xi_{i}(t,x,y)\in\mathbb{R}^{2}\ \text{(2D)}.

In code, each generator uses separate MLPs forτ\tauandξ\xi. A third headβ\betais also instantiated for compatibility with shared utilities but isnot usedin the SDE-only description here.
- •

Examples 1 & 2:tanhMLPs with fixed widths:τ\tau:[1,32,32,1][1,32,32,1];ξ\xi:[2,64,64,1][2,64,64,1]in 1D (Ex. 1) and[3,64,64,2][3,64,64,2]in 2D (Ex. 4).m=3m=3(Ex. 1) andm=3m=3(Ex. 4).
- •

Example 3:deeperswishnetworks withdepth_tau=3,depth_xi=3, width 64, andm=3m=3generators.
- •

Example 4:tanhMLPs withτ\tauas[1,32,32,1][1,32,32,1]andξ\xias[3,64,64,2][3,64,64,2], withm=3m=3.

## Stage-2 loss terms and weighting.

The generator objective is a weighted sum of seven lossesL1,…,L7L_{1},\dots,L_{7}computed on minibatches from𝒯\mathcal{T}. The code uses:
- •

Structural/algebraic terms:closure (L1L_{1}), Jacobi (L2L_{2}), skew-symmetry (L3L_{3}), bilinearity (L4L_{4}), and an independence/scaling term (L5L_{5}) withs5_mode="sigma"ands5_tau=0.8(Examples 1–4).
- •

SDE-specific constraints:the Ito determining equations (L6L_{6}) computed using surrogate coefficient functionsμ​(⋅)\mu(\cdot)andσ​(⋅)\sigma(\cdot)derived from the learned Stage-1 network(s), and a pushforward consistency term (L7L_{7}) comparing transformed coefficients under the learned generator-induced flow, using a small finiteϵ\epsilonstep (e.g.s7_eps=1e-2) and typically a single step (e.g.s7_steps=1in the fixed-weight notebooks).

Weighting:
- •

Examples 1–3 (fixed weights):LossWeightssets(w1:7)=(1.0,0.1,0.1,0.1,⋆,1.0,0.1),(w_{1:7})=(1.0,\,0.1,\,0.1,\,0.1,\,\star,\,1.0,\,0.1),

with⋆=0.1\star=0.1in Examples 1 and 3, and⋆=0.5\star=0.5in Example 2. Generator L2 decay is applied withweight_decay=1e-6.
- •

Example 4 (scheduled weights):w6=10w_{6}=10,w7=2w_{7}=2, andw5=2w_{5}=2are kept large throughout, whilew1w_{1}–w4w_{4}are ramped on only in the final 40% of training after 60% progress via a piecewise-linear schedule.

## Stage-2 optimization.
- •

Examples 1–3:optax.clip_by_global_norm (1.0)+optax.adam. The nominalGenTrainConfig.lris overridden to10−410^{-4}in Examples 1 and 3; Example 4 uses10−410^{-4}directly. Minibatches are sampled uniformly without replacement from the preparedTX_genarray after filtering non-finite rows.
- •

Example 4:optax.clip_by_global_norm+optax.adamwwith a learning-rate schedule: 5% linear warmup from 0 tolr, followed by cosine decay down toalpha=0.1oflr. The sampler mixes half empiricalTX_genpoints and half uniform box points each step.ExamplemmStage-2 cloud sourcentrajn_{\mathrm{traj}}(gen)BgenB_{\rm gen}τ\taunetξ\xinetActivation13surrogate sim, flatten(t,x)(t,x)256256​(500+1)=128,256256(500{+}1)=128{,}256[1,32,32,1][1,32,32,1][2,64,64,1][2,64,64,1]tanh23surrogate sim + reflection + mixture cloud256kept at128,256128{,}256depth 3, width 64depth 3, width 64swish33surrogate sim, flatten(t,x,y)(t,x,y)256256​(200+1)=51,456256(200{+}1)=51{,}456[1,32,32,1][1,32,32,1][3,64,64,2][3,64,64,2]tanh43data flatten(t,x,y)(t,x,y)20482048​(200+1)=411,6482048(200{+}1)=411{,}648[1,32,32,1][1,32,32,1][3,64,64,2][3,64,64,2]tanhTable 14:Stage-2 (generator) architectures and the point clouds used for training the SDE symmetry generators.BgenB_{\rm gen}counts(t,state)(t,\text{state})points used for generator losses.ExampleStepsBatchLROptimizerWeights(w1,…,w7)(w_{1},\dots,w_{7})Sampling notes13000204810−410^{-4}clip(1.0)+Adam(1,0.1,0.1,0.1,0.1,1,0.1)uniform minibatches fromTX_gen23000102410−410^{-4}clip(1.0)+Adam(1,0.1,0.1,0.1,0.5,1,0.1)xx-reflection in sim; 70% uniform box points; optional traj balancing33000102410−410^{-4}clip(1.0)+Adam(1,0.1,0.1,0.1,0.1,1,0.1)uniform minibatches fromTX_gen;print_every=10460002562×10−42\!\times\!10^{-4}(scheduled)clip(1.0)+AdamWscheduled:w6=10,w7=2,w5=2w_{6}{=}10,w_{7}{=}2,w_{5}{=}2, rampw1:4w_{1:4}half empiricalTX_gen+ half uniform box; warmup+cosine LRTable 15:Stage-2 (generator) optimization and weighting differences across examples.

## Appendix QSensitivity of the Maximum Principal Angle to Weight Choices

Table16reports the maximum principal angle as the weights(w6,w7)(w_{6},w_{7})are varied. Overall, the response is markedly non-monotone in both weights, indicating a strong interaction between the two penalty terms. Across the sweep, the maximum principal angle ranges from14.71∘14.71^{\circ}(at(w6,w7)=(1.0,0.7)(w_{6},w_{7})=(1.0,0.7)) to55.31∘55.31^{\circ}(at(w6,w7)=(0.2,0.9)(w_{6},w_{7})=(0.2,0.9)). For fixedw6w_{6}, changingw7w_{7}can induce substantial variation: for example, atw6=0.2w_{6}=0.2the angle increases from21.35∘21.35^{\circ}atw7=0.1w_{7}=0.1to42.28∘42.28^{\circ}atw7=0.5w_{7}=0.5and further to55.31∘55.31^{\circ}atw7=0.9w_{7}=0.9, whereas atw6=0.6w_{6}=0.6the angle peaks at37.00∘37.00^{\circ}forw7=0.3w_{7}=0.3and then decreases to21.13∘21.13^{\circ}forw7=0.9w_{7}=0.9. Similarly, for fixedw7w_{7}, decreasingw6w_{6}does not uniformly increase or decrease the angle (e.g., atw7=0.1w_{7}=0.1the values span22.64∘22.64^{\circ}atw6=1.0w_{6}=1.0up to39.21∘39.21^{\circ}atw6=0.4w_{6}=0.4and down to21.35∘21.35^{\circ}atw6=0.2w_{6}=0.2). These trends suggest that the maximum principal angle is sensitive to the relative balance between the two weights rather than to either weight in isolation, motivating the use of a small grid search over(w6,w7)(w_{6},w_{7})when selecting a stable operating point.Table 16:Maximum principal angle as a function of weightsw6w_{6}andw7w_{7}.w6w_{6}w7w_{7}Max. principal angle (deg)1.00.122.641.00.326.781.00.523.381.00.714.711.00.919.900.80.135.920.80.324.360.80.520.860.80.718.810.80.931.710.60.122.400.60.337.000.60.534.190.60.729.910.60.921.130.40.139.210.40.327.910.40.525.480.40.737.230.40.923.490.20.121.350.20.325.100.20.542.280.20.720.480.20.955.31

## 


- 


Major funding support from
