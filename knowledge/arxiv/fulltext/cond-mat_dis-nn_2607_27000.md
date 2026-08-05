# On the robustness of noisy solutions in non-convex neural networks

**arXiv ID**: 2607.27000v1
**Authors**: Enrico M. Malatesta, Alessandra Passalacqua, Riccardo Zecchina
**Published**: 2026-07-29
**Categories**: cond-mat.dis-nn, cs.LG, math.PR
**Comments**: 25 pages, 13 figures
**HTML URL**: https://arxiv.org/html/2607.27000v1

## Abstract

Optimization in non-convex neural network models is strongly influenced by the geometry of the solution space: sparse, isolated, point-like clusters are typically algorithmically inaccessible, whereas wide and flat regions can be found efficiently despite being relatively rare. At zero temperature this picture has been formalized in binary perceptrons through the overlap gap property (OGP), which limits algorithmic access to configurations with zero training error above a critical constraint density $α_{\rm OGP}$. Here we extend this description to finite temperature, where a positive training error is allowed and statistically penalized. We first show that the frozen one-step replica-symmetry-breaking solution, dominating the zero temperature equilibrium measure, survives at any finite temperature. We furthermore derive a general criterion, based on the smoothness of the single-pattern Gibbs weight near the decision boundary, that determines when a finite-temperature relaxation of the loss removes freezing. We then extend the OGP construction to finite temperature and show that dense, algorithmically accessible regions of finite-energy configurations persist beyond $α_{\rm OGP}$, up to a threshold $α_{\rm OGP}(ε)$ that grows with the allowed training error $ε$. Finally, in the teacher-student setting, we show that these wide, finite-energy regions still retain good generalization. Using a finite energy message-passing algorithm, we demonstrate numerically that thermal noise enables effective generalization in the regime of constraint densities where both recovering the teacher and finding a zero temperature solution are computationally hard.

## Full Text

On the robustness of noisy solutions in non-convex neural networks

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.27000v1 [cond-mat.dis-nn] 29 Jul 2026

## On the robustness of noisy solutions in non-convex neural networksEnrico M. MalatestaDepartment of Computing Sciences, Bocconi University, Milano, ItalyBocconi Institute for Data Science and Analytics (BIDSA)Alessandra PassalacquaDepartment of Computing Sciences, Bocconi University, Milano, ItalyRiccardo ZecchinaDepartment of Computing Sciences, Bocconi University, Milano, ItalyBocconi Institute for Data Science and Analytics (BIDSA)

## Abstract

Optimization in non-convex neural network models is strongly influenced by the geometry of the solution space: sparse, isolated, point-like clusters are typically algorithmically inaccessible, whereas wide and flat regions can be found efficiently despite being relatively rare. At zero temperature this picture has been formalized in binary perceptrons through the overlap gap property (OGP), which limits algorithmic access to configurations with zero training error above a critical constraint densityαOGP\alpha_{\rm OGP}. Here we extend this description to finite temperature, where a positive training error is allowed and statistically penalized. We first show that the frozen one-step replica-symmetry-breaking solution, dominating the zero temperature equilibrium measure, survives at any finite temperature. We furthermore derive a general criterion, based on the smoothness of the single-pattern Gibbs weight near the decision boundary, that determines when a finite-temperature relaxation of the loss removes freezing. We then extend the OGP construction to finite temperature and show that dense, algorithmically accessible regions of finite-energy configurations persist beyondαOGP\alpha_{\rm OGP}, up to a thresholdαOGP​(ϵ)\alpha_{\rm OGP}(\epsilon)that grows with the allowed training errorϵ\epsilon. Finally, in the teacher-student setting, we show that these wide, finite-energy regions still retain good generalization. Using a finite energy message-passing algorithm, we demonstrate numerically that thermal noise enables effective generalization in the regime of constraint densities where both recovering the teacher and finding a zero temperature solution are computationally hard.

## IIntroduction

Over the last decade, numerous studies at the intersection of statistical physics and machine learning showed how the local geometry of the energy landscape of neural networks can be exploited to guide their optimization, and consequently improve their performance, despite the practical difficulty of navigating highly non-convex spacesBaldassiet al.(2015,2016); Chaudhariet al.(2019). The robust ensemble formalism was introduced in the study of non-convex neural networks, to prove the existence of atypical, but algorithmically accessible and well-generalizing, wide and flat regions at zero training error, as opposed to inaccessible isolated, point-like solutions, and algorithms designed to search for these regions turned out to be successful. At the same time, mathematicians have introduced the rigorous theoretical framework of the overlap gap property (OGP): whenever the near-optimal solutions of a problem lie in small, or even point-like, disconnected clusters, these become unreachable to a broad class of optimization algorithmsGamarnik (2021).
The general formulation of the OGP theory makes it applicable to some well-known problems in statistical physics of complex systemsGamarnik and Jagannath (2021), random graph theoryGamarnik and Sudan (2017)and simple neural network modelsGamarniket al.(2022).

This body of work, however, has almost exclusively been developed at zero temperature, where learning is phrased as a constraint satisfaction problem (CSP): a configuration has nonzero weight in the partition function only if it fits every training point correctly. A partial exception is offered by studies that relax the requirement by introducing a stability margin in the classification constraint, which enlarges the space of solutions of the CSP while remaining at zero temperatureBaldassiet al.(2023);
even so, both settings ultimately demand exact satisfaction of a fixed number of constraints. This is a demanding requirement,
at odds with how learning is typically carried out in practice, where a nonzero training error is common - and can even improve generalization and robustness to noise, in contrast to overfitting. A prominent example
is offered by large language models,
which are extremely heavy to train, so that
compute-optimal training generally stops before convergence,
and a nonzero training loss is the rule rather than the exceptionKaplanet al.(2020); Hoffmannet al.(2022).

In this work we extend the study of the geometry of the configuration space to finite temperature, where imperfect classification is allowed but statistically penalized.
We consider the paradigmatic case of binary perceptrons, either storing random patterns or learning a classification rule from a teacher. The simplicity of the architecture allows a tractable analytical study, and yet the discreteness of the weights renders the solution space non-convex, endowing it with the rich geometrical structure that motivates our study.
Models are introduced in SectionII, each being defined through its Hamiltonian.
For each model, we will consider two classes of optimal and near-optimal weights in the energy landscape, corresponding to equilibrium and out-of-equilibrium configurations.
The equilibrium ones are those typically encountered when sampling from the Gibbs measure with the standard error counting loss, at temperatureTT. At zero temperature, these are known to be organized in a frozen one-step replica-symmetry-breaking (1RSB) structureKrauth and Mézard (1989); Aubinet al.(2019), decomposed into exponentially many geometrically isolated, point-like clustersHuang and Kabashima (2014); Gamarniket al.(2022).
The second class consists of atypical, out-of equilibrium configurations, obtained by biasing the measure to favor regions with large local entropy, that are invisible to the equilibrium analysis, but visible to common optimization algorithms because of their geometrical accessibility.

In Sec.IIIwe start our discussion from the typical equilibrium configurations.
We ask whether raising the temperature is sufficient to dynamically unfreeze the landscape, and show that it is not: the frozen structure persists at every finite temperature, in agreement with the dynamical field theory analysis ofHorner (1992). We show that the dynamical temperature diverges in the thermodynamic limit. We identify the general mechanism responsible for freezing, related to the roughness of the Gibbs weight in the equilibrium measure: some modifications of the Hamiltonian can change the structure of the landscape, allowing the emergence of clusters even at the typical level.

Then, in Sec.IV, considering again the standard error-counting loss function, we move to the study of atypical dense regions of solutions. At zero temperature, these exist for constraint densitiesα\alphasmaller than a thresholdαOGP\alpha_{\rm OGP}, and are algorithmically reachable (up to a small gap)Baldassiet al.(2016). We show that the onset of the overlap gap property can be followed in temperature: dense flat regions still exist as thermal noise is injected,
but they exist up to a thresholdαOGP​(ϵ)\alpha_{\rm OGP}(\epsilon)that grows with the allowed energyϵ\epsilon.
Our approach is based on the replica methodMézardet al.(1987)and it gives results that are compatible with the previous analytical estimatesGamarniket al.(2022); Stojnic (2026a,b).
We probe the accessibility of the near-optimal clusters numerically, with a message passing algorithm naturally devised to converge towards finite-energy flat regions in the energy landscape, even beyond the zero-temperature OGP threshold.
Finally, in Sec.V, we focus on the teacher-student setting and test the generalization performance of the finite-energy wide clusters, showing that the thermal noise in training error does not obstruct learning.
On the contrary: beyond the zero-temperature OGP threshold, restricting the search to exact-fit configurations can create an algorithmic obstruction, whereas accessible finite-error dense regions may still generalize well.
This suggests that it is beneficial to shape optimization algorithms to search for wide regions rather than isolated global minima, even when the former carry finite energy.

## IIModels and finite-temperature ensembles

We consider a class of binary perceptrons models having withNNIsing weights𝒘∈{−1,+1}N\bm{w}\in\{-1,+1\}^{N}, trained on datasets comprisingP=α​NP=\alpha Nrandom patterns divided into two classes. The input vectors have independent standard Gaussian entries,xiμ∼𝒩​(0,1)x_{i}^{\mu}\sim\mathcal{N}(0,1), and we denote byhμ​(𝒘)=1N​∑i=1Nwi​xiμh^{\mu}(\bm{w})=\frac{1}{\sqrt{N}}\sum_{i=1}^{N}w_{i}x_{i}^{\mu}(1)

the local field associated with the patternμ\mu. The quantitysμ​(𝒘)=yμ​hμ​(𝒘),s^{\mu}(\bm{w})=y^{\mu}h^{\mu}(\bm{w}),(2)

is the stability of the input𝒙μ\bm{x}^{\mu},
whereyμ=±1y^{\mu}=\pm 1is the binary label associated to the input pattern.
In the case of the asymmetric binary perceptron (ABP), the perceptron is said to classify the pattern𝒙μ\bm{x}^{\mu}correctly wheneversμ​(𝒘)>0s^{\mu}(\bm{w})>0. We will call𝒘\bm{w}asolutionof the ABP problem ifsμ​(𝒘)>0s^{\mu}(\bm{w})>0for anyμ∈[P]\mu\in[P].

In the following we shall consider two classical ways of generating the labels. In thestoragesetting the labelsyμ=±1y^{\mu}=\pm 1are independent Rademacher random variables. Since the distribution of the patterns is symmetric, the labels can then be gauged away and one may setyμ=1y^{\mu}=1for allμ\muwithout loss of generality. In this setting, one can focus on theoptimizationtask, by which we mean finding student configurations𝒘\bm{w}that achieve zero training error, at constraint densityα\alpha.
In theteacher-studentproblem, instead, the labels are generated by a planted binary teacher𝒘⋆∈{−1,+1}N\bm{w}^{\star}\in\{-1,+1\}^{N}viayμ=sign⁡(1N​∑i=1Nwi⋆​xiμ).y^{\mu}=\operatorname{sign}\left(\frac{1}{\sqrt{N}}\sum_{i=1}^{N}w_{i}^{\star}x_{i}^{\mu}\right).(3)

In the teacher-student setting, our main focus will be again the optimization task.
This has to be distinguished from theinferencetask, where one is interested in inferring the planted signalGyörgyi (1990); Gardner and Derrida (1989). The teacher-student setting also allows to study thegeneralizationcapability of the network. In particular, the teacher-student overlapr​(𝒘,𝒘⋆)=1N​∑i=1Nwi​wi⋆r(\bm{w},\bm{w}^{\star})=\frac{1}{N}\sum_{i=1}^{N}w_{i}w_{i}^{\star}determines the generalization error of the student throughϵg​(r)=1π​arccos⁡r,\epsilon_{g}(r)=\frac{1}{\pi}\arccos r,(4)

which is the probability that the student and the teacher disagree on a previously unseen Gaussian input. Both the storage and teacher-student settings have been studied extensively in the statistical mechanics literature, seeGardner and Derrida (1988,1989); Krauth and Mézard (1989); Györgyi (1990); Opper and Haussler (1991); Huang and Kabashima (2014); Baldassiet al.(2015,2021,2023).

While our main focus is the optimization problem, it is also useful to consider configurations with a finite training error. To this end, we introduce a Gibbs measure over the weight configurations, where each pattern contributes through a single-pattern Boltzmann factor𝒦\mathcal{K}. The Gibbs partition function isZ𝒟​(β)=∑𝒘∈{±1}N∏μ=1α​N𝒦​(sμ​(𝒘)),Z_{\mathcal{D}}(\beta)=\sum_{\bm{w}\in\{\pm 1\}^{N}}\prod_{\mu=1}^{\alpha N}\mathcal{K}\left(s^{\mu}(\bm{w})\right),(5)

where the dependence on the inverse temperature (β\beta) is encoded in𝒦\mathcal{K}. In the zero-temperature limit, suitable choices of𝒦\mathcal{K}recover the hard-constraint optimization problem discussed above. The quenched free entropy density associated to the partition function is:ϕ​(β)=limN→∞1N​𝔼𝒟​log⁡Z𝒟​(β).\phi(\beta)=\lim_{N\to\infty}\frac{1}{N}\mathbb{E}_{\mathcal{D}}\log Z_{\mathcal{D}}(\beta).(6)

The model we will focus on in this paper is the ABP, with single Gibbs weight given by𝒦ABP​(s)=e−β​Θ​(−s)=e−β+(1−e−β)​Θ​(s).\mathcal{K}^{\rm ABP}(s)=e^{-\beta\Theta(-s)}=e^{-\beta}+\left(1-e^{-\beta}\right)\Theta(s).(7)

In the zero-temperature limit, the measure is uniform on zero-error solutions whenever such solutions exist, while at positive temperature it also assigns weighte−βe^{-\beta}to each violated constraint. Equivalently, this corresponds to weighting configurations𝒘\bm{w}according to a Gibbs distribution having as energy a loss functionℒ𝒟\mathcal{L}_{\mathcal{D}}Z𝒟​(β)=∑𝒘e−β​ℒ𝒟​(𝒘),ℒ𝒟​(𝒘)=∑μ=1α​NΘ​(−sμ​(𝒘)).Z_{\mathcal{D}}(\beta)=\sum_{\bm{w}}e^{-\beta\mathcal{L}_{\mathcal{D}}(\bm{w})},\qquad\mathcal{L}_{\mathcal{D}}(\bm{w})=\sum_{\mu=1}^{\alpha N}\Theta\left(-s^{\mu}(\bm{w})\right).(8)

which counts the number of misclassified training patterns. The same formalism is generic and can be used also to study other models. For example, similar results that we will present for the ABP will be valid for the symmetric binary perceptron (SBP)Aubinet al.(2019); Gamarniket al.(2022)as well and will be discussed in the appendices. In the SBP with marginκ>0\kappa>0the labels play no role and the constraint requires the local field to lie inside a window of width2​κ2\kappa:|sμ​(𝒘)|=|hμ​(𝒘)|≤κ.|s^{\mu}(\bm{w})|=|h^{\mu}(\bm{w})|\leq\kappa.(9)

The single-pattern Gibbs weight corresponding to an error counting loss function is therefore𝒦SBP​(s)=e−β​Θ​(|s|−κ)=e−β+(1−e−β)​Θ​(κ−|s|).\mathcal{K}^{\rm SBP}(s)=e^{-\beta\Theta(|s|-\kappa)}=e^{-\beta}+\left(1-e^{-\beta}\right)\Theta(\kappa-|s|).(10)

Other choices of𝒦\mathcal{K}may impose the same hard constraint in the limitβ→∞\beta\to\infty, but they can lead to different finite-temperature physics. This point is central for the discussion of the
next section.

The free entropy in equation (6) can be computed using the replica methodMézardet al.(1987). The derivations using a Replica-Symmetric (RS) or a 1-step Replica Symmetry Breaking (1RSB) Ansatz are standard in the statistical physics literature and the detailed derivations are reported for convenience of the reader in AppendixA.

## IIIDynamical temperature and freezing

At zero temperature the equilibrium measure of the ABP and SBP equipped, respectively, with the Gibbs weight (7) and (10) is known to be described by a frozen one-step replica-symmetry-breaking (1RSB) structureHuang and Kabashima (2014); Aubinet al.(2019); Perkins and Xu (2024); Barbieret al.(2024); Barbier (2025a). In this picture the Gibbs measure decomposes into exponentially many clusters which are separated by extensive Hamming distances, while each individual cluster is point-like.
In replica notation this means that the intra-state overlap between pairs of solutions isq1=1,q_{1}=1,(11)

whereas the inter-state overlapq0q_{0}remains strictly smaller thanq1q_{1}. In the SBP, the symmetry𝒘↦−𝒘\bm{w}\mapsto-\bm{w}further impliesq0=0q_{0}=0, i.e. the point-like clusters are orthogonal.

A natural question is whether this frozen structure is exclusively a zero-temperature property, or whether it persists when positive training error configurations are assigned finite Gibbs weight. More generally, we ask how this equilibrium picture depends on the specific choice of the finite-temperature single-pattern Gibbs weight𝒦\mathcal{K}. We can answer those questions by computing the so-calleddynamical temperatureTdT_{d}. This is defined as the largest temperature below which the 1RSB saddle-point equations admit a non-trivial solution with the Parisi block parameterm=1m=1andq1>q0q_{1}>q_{0}Kirkpatrick and Thirumalai (1987). If, in addition, one hasq1=1q_{1}=1, then forT<TdT<T_{d}the corresponding 1RSB phase is frozen.

For the error-counting single-pattern weights𝒦ABP\mathcal{K}_{\rm ABP}and𝒦SBP\mathcal{K}_{\rm SBP}, the computation reported in AppendixBshows that, for every fixedα>0\alpha>0and every inverse temperatureβ>0\beta>0, them=1m=11RSB equations admit a non-trivial frozen solution. Therefore, the dynamical temperature diverges in the thermodynamic limit. In other words, the equilibrium measure is dynamically glassy at every finite temperature. This result is in agreement with what Horner found for the ABP in the storage setting using dynamical field theory techniquesHorner (1992). At finiteNN, the singular solutionq1=1q_{1}=1is rounded by the discreteness of the configuration space. Using the natural finite-size cutoff1−q1≃1N,1-q_{1}\simeq\frac{1}{N},(12)

one obtains the scaling withNNof the dynamical temperature (66):Td≃N1/4log⁡N.T_{d}\simeq\frac{N^{1/4}}{\sqrt{\log N}}\,.(13)

The mechanism leading to this result is quite general, and clarifies which features of the finite-temperature Gibbs weight are responsible for freezing. As detailed in AppendixB.2,
the 1RSB saddle point equations involve the functionℋ​(x,y)=∫D​z​𝒦​(x+y​z),\mathcal{H}(x,y)=\int Dz\,\mathcal{K}(x+yz)\,,(14)

whereD​z=d​z2​π​e−z2/2Dz=\frac{dz}{\sqrt{2\pi}}e^{-z^{2}/2}andy=1−q1y=\sqrt{1-q_{1}}.
The limitq1→1q_{1}\to 1therefore corresponds to the limity→0y\to 0. Possible singularities in this limit can only come from the decision boundaries, namely from the points where the zero-temperature constraint changes value and where𝒦\mathcal{K}may be non-smooth. We denote such a boundary bybb. For example, in the ABP one hasb=0b=0, while in the SBP with marginκ\kappathe boundaries areb=±κb=\pm\kappa. A crucial quantity controlling the onset of freezing is the boundary layer termℬ𝒦​(b,y)≡y​∫𝑑u​[∂xℋ​(b+y​u,y)]2ℋ​(b+y​u,y).\mathcal{B}_{\mathcal{K}}(b,y)\equiv y\int du\,\frac{\left[\partial_{x}\mathcal{H}(b+yu,y)\right]^{2}}{\mathcal{H}(b+yu,y)}.(15)

In particular, ifℬ𝒦​(b,y)→∞asy→0,\mathcal{B}_{\mathcal{K}}(b,y)\to\infty\qquad\text{as}\qquad y\to 0,(16)

we argue in AppendixB.2that the solution space is frozen. Conversely, ifℬ𝒦​(b,y)\mathcal{B}_{\mathcal{K}}(b,y)remains finite, or vanishes, asy→0y\to 0, then the frozen phase is absent. In that case a non-trivial 1RSB solution withq1<1q_{1}<1may still appear, which does not
describe point-like clusters. We illustrate below such criterion on three types of single-pattern weights𝒦\mathcal{K}shown in Fig.1that have been considered in the literature.
- 1.

Jump discontinuity.Consider a single pattern Gibbs weight that has a jump discontinuity at the decision boundary.𝒦ABP\mathcal{K}^{\rm ABP}and𝒦SBP\mathcal{K}^{\rm SBP}given in (7) and (10) fall in this class: for anyβ>0\beta>0, they are discontinuous at the decision boundary, namely at the origin for the ABP and at±κ\pm\kappafor the SBP. As we show inB.2, this is responsible for the divergence ofℬ𝒦\mathcal{B}_{\mathcal{K}}wheny→0y\to 0ℬ𝒦​(b,y)≃C​(β)y,\mathcal{B}_{\mathcal{K}}(b,y)\simeq\frac{C(\beta)}{y}\,,(17)

whereC​(β)C(\beta)is a positive constant for everyβ>0\beta>0, and
vanishes only atβ=0\beta=0. This is the reason why the frozen solution dominates the Gibbs measure at all finite temperatures.
- 2.

Horner’s weight.A different finite-temperature continuation has been considered first by HornerHorner (1992)and more recently inCataniaet al.(2024)in the case of the ABP. This is obtained by replacing the error-counting loss by a soft penalty for violated constraints𝒦​(s)=e−β​(−s)γ​Θ​(−s);\mathcal{K}(s)=e^{-\beta(-s)^{\gamma}\Theta(-s)}\,;(18)

see the left panel of Figure1for a plot. We are considering here for simplicity the case of the ABP, but the considerations we are making can be extended to any model. Note that forγ=0\gamma=0equation (18) reduces to the error-counting weight in (7), so we should expect freezing. Forγ>0\gamma>0andβ<∞\beta<\infty, the Gibbs weight (18) is instead continuous at the decision boundary. In this case the boundary layer term scales asℬ𝒦​(b,y)∼y2​γ−1.\mathcal{B}_{\mathcal{K}}(b,y)\sim y^{2\gamma-1}.(19)

wheny→0y\to 0.
Hence freezing is expected whenγ<1/2\gamma<1/2, while forγ>1/2\gamma>1/2the boundary layer is not singular enough to produce a frozen solution. A dynamical transition to a non-frozen phase may still be present at a finite temperature (and indeed it occurs, seeHorner (1992)). Finally, since in the limitβ→∞\beta\to\inftyone has𝒦​(s)→Θ​(s)\mathcal{K}(s)\to\Theta(s), the frozen solution is restored at zero temperature.
- 3.

Logarithmic potential.Another class consists of Gibbs weights that vanish as a power law when the decision boundary is approached from within the feasible region. For example, consider:𝒦​(s)=sγ​Θ​(s)\mathcal{K}(s)=s^{\gamma}\Theta(s)(20)

This should be distinguished from the soft-penalty form in Eq. (18), which smooths the cost of violated constraints. Here, instead, the weight suppresses configurations that satisfy the constraint only marginally, assigning larger weight to configurations deeper inside the feasible region.

Equivalently, this choice induces, within the feasible region, a logarithmic potentialV​(s)=−log⁡𝒦​(s)=−γ​log⁡sV(s)=-\log\mathcal{K}(s)=-\gamma\log s, which penalizes small positive stabilities and favors configurations farther from the decision boundaryStraziotaet al.(2025). In this case one can show that the boundary layer termℬ𝒦\mathcal{B}_{\mathcal{K}}behaves asℬ𝒦​(b,y)∼yγ−1.\mathcal{B}_{\mathcal{K}}(b,y)\sim y^{\gamma-1}.(21)

Therefore the frozen solution is expected forγ<1\gamma<1, while it
is absent forγ>1\gamma>1. This picture has also been observed inStraziotaet al.(2025)using a Franz-Parisi potential approach.Figure 1:Plot of the single pattern Gibbs weight. Left:𝒦​(s)=e−β​(−s)γ​Θ​(−s)\mathcal{K}(s)=e^{-\beta(-s)^{\gamma}\Theta(-s)}forβ=2\beta=2andγ=0\gamma=0, 0.5, 1, 2. This form of the single pattern weight has been in considered by HornerHorner (1992)for integer values ofγ\gamma. Right:𝒦​(s)=sγ​Θ​(s)\mathcal{K}(s)=s^{\gamma}\Theta(s)considered inStraziotaet al.(2025)for the same values ofγ\gammaas in the left panel. In both the left and right plot,𝒦\mathcal{K}has a jump discontinuity at the decision boundaryb=0b=0forγ=0\gamma=0, which induces freezing. In left plot the discontinuity is recovered also in the largeβ\betalimit.

## IVThe Overlap Gap Property

The frozen equilibrium picture described in the previous section does not by itself imply that the problem of finding configurations𝒘\bm{w}with a given energy level is algorithmically hard. The reason is that efficient algorithms do not need to sample from the equilibrium Gibbs measure. They may instead operate out of equilibrium, following atypical trajectories in configuration space and exploiting regions that are exponentially subdominant in the equilibrium measure. This distinction is particularly important in the case of the binary perceptron with error counting loss (7) which, as pointed out in the previous section, has a frozen landscape at any finite temperature and positive constraint density.

In the past decade, the statistical-physics literature has shown that message-passing algorithms, especially when combined with reinforcement or with local-entropy biases, can efficiently find solutions and improve the algorithmic thresholds of many different constraint satisfaction problems, ranging from theKK-SAT and perceptron modelBraunstein and Zecchina (2006); Baldassi and Braunstein (2015); Barbier (2025b), to the graph coloring problemAngelini and Ricci-Tersenghi (2023); Budzynskiet al.(2019); Budzynski and Semerjian (2020). InBaldassiet al.(2015)it has been conjectured that algorithmic success is associated with the existence of dense regions of solutions which, despite being rare and invisible to the equilibrium measure, are basins of attraction much larger than typical equilibrium states.
A recent theoretical explanation for this effectiveness was that imposing local entropy biases could delay the dynamical transitionBudzynskiet al.(2019); Budzynski and Semerjian (2020), with random hypergraph bicoloring constituting a notable exceptionAngeliniet al.(2025).

This physical picture has recently been reformulated, in the mathematical literature, through the framework of the overlap gap property (OGP). OGP is a geometric obstruction in the space of near-optimal configurations. Such a topological obstruction has been used to explain algorithmic barriers in random optimization problemsGamarnik and Sudan (2017)and, more recently, in perceptron-type modelsGamarnik (2021); Gamarniket al.(2022); Benedettiet al.(2025). Informally,mm-OGP holds when relevantmm-tuples of configurations, organize into separated regions: they can be mutually close or mutually far, but there is an entire interval of intermediate overlaps in which no such configurations can be found. This gap provides an obstruction to broad classes of so-calledstablealgorithms,
namely algorithms whose outputs remain close, with high probability and under a common random seed, when applied to sufficiently close or correlated instances of the random problem.

Here we study the OGP by consideringmmreal replicas, orclones, of the system constrained to have fixed mutual overlap. We limit ourselves here for simplicity to the ABP with the error counting loss (7) but the technical derivations presented in AppendixA.2are general. Form≥2m\geq 2andq1∈[−1,1]q_{1}\in[-1,1]the cloned partition function is defined asZm,𝒟​(q1;β)=∑{𝒘a}a=1m∏a=1me−β​ℒ𝒟​(𝒘a)​∏1≤a<b≤mδ​(q1−1N​∑i=1Nwia​wib).\begin{split}Z_{m,\mathcal{D}}(q_{1};\beta)=\sum_{\{\bm{w}^{a}\}_{a=1}^{m}}\prod_{a=1}^{m}e^{-\beta\mathcal{L}_{\mathcal{D}}(\bm{w}^{a})}\prod_{1\leq a<b\leq m}\delta\left(q_{1}-\frac{1}{N}\sum_{i=1}^{N}w_{i}^{a}w_{i}^{b}\right).\end{split}(22)

The corresponding quenched free entropy per clone isϕm​(q1;β)=limN→∞1N​m​𝔼𝒟​ln⁡Zm,𝒟​(q1;β).\phi_{m}(q_{1};\beta)=\lim_{N\to\infty}\frac{1}{Nm}\mathbb{E}_{\mathcal{D}}\ln Z_{m,\mathcal{D}}(q_{1};\beta).(23)

This quantity can be computed with the replica method. At the RS level, the result can be found simply by imposing a 1RSB structure on the equilibrium measure (8) and treating bothmmandq1q_{1}as external parameters rather than variational onesMonasson (1995a); Baldassiet al.(2020), see AppendixA.2. At zero temperature,Zm,𝒟​(q1;∞)Z_{m,\mathcal{D}}(q_{1};\infty)countsmm-tuples of
solutions at mutual overlapq1q_{1}. Thus, if forα\alphalarger than a certain thresholdαm​(q1)\alpha_{m}(q_{1})one hasϕm​(q1;∞)<0,\phi_{m}(q_{1};\infty)<0,(24)

then with high probability no suchmm-tuple exists. The onset of themm-OGP threshold is therefore obtained by finding the minimal value of the constraint densityα\alphafor which a forbidden interval of overlaps (24) starts being non-empty:αOGP​(m)=minq1⁡αm​(q1)\alpha_{\rm OGP}(m)=\min_{q_{1}}\alpha_{m}(q_{1})(25)

This threshold can be determined equivalently by the conditionsBenedettiet al.(2025)ϕm​(q1;∞)\displaystyle\phi_{m}(q_{1};\infty)=0,\displaystyle=0,(26a)∂q1ϕm​(q1;∞)\displaystyle\partial_{q_{1}}\phi_{m}(q_{1};\infty)=0.\displaystyle=0.(26b)

At finite temperature the cloned partition function no longer counts configurations of zero training error. Rather, it weights configurations proportionally to their Boltzmann weight, at inverse temperatureβ\beta. The entropysm​(q1;β)s_{m}(q_{1};\beta), i.e. the log-number of configurations that dominate the measure, can be found by a Legendre transform of the free entropy:sm​(q1;β)=ϕm​(q1;β)+β​α​ϵm​(q1;β),s_{m}(q_{1};\beta)=\phi_{m}(q_{1};\beta)+\beta\alpha\epsilon_{m}(q_{1};\beta)\,,(27)

whereϵm​(q1;β)=−1α​∂ϕm​(q1;β)∂β=𝔼𝒟​⟨1α​N​m​∑a=1mℒ𝒟​(𝒘a)⟩𝒟\epsilon_{m}(q_{1};\beta)=-\frac{1}{\alpha}\frac{\partial\phi_{m}(q_{1};\beta)}{\partial\beta}=\mathbb{E}_{\mathcal{D}}\left\langle\frac{1}{\alpha Nm}\sum_{a=1}^{m}\mathcal{L}_{\mathcal{D}}(\bm{w}^{a})\right\rangle_{\mathcal{D}}(28)

represents the average training error per pattern of themmclones sampled from the constrained Gibbs measure induced by (22).
The finite-temperature OGP threshold is therefore defined by the solution of the system of equationssm​(q1;β)\displaystyle s_{m}(q_{1};\beta)=0,\displaystyle=0,(29a)∂q1sm​(q1;β)\displaystyle\partial_{q_{1}}s_{m}(q_{1};\beta)=0.\displaystyle=0.(29b)Figure 2:Emergence of the OGP at finite temperature in the ABP, teacher-student setting. The left panel depicts the entropysm​(q1;β)s_{m}(q_{1};\beta)form=2m=2andβ=5.0\beta=5.0, versus the overlap between the two clonesq1q_{1}. For these values ofmmandβ\beta, the OGP threshold isαOGP≃1.950\alpha_{\rm OGP}\simeq 1.950andq1OGP≃0.988q_{1}^{\rm OGP}\simeq 0.988. Notice how, forα>αOGP\alpha>\alpha_{\rm OGP}, there is an entire interval ofq1q_{1}’s for which the entropy is negative, meaning that, with high probability at largeNN, couples of configurations satisfying the energy constraint exists at either small or very large overlaps, with an entirely forbidden interval of intermediate Hamming distances. The inset shows a zoom of the largeq1q_{1}region. Right:αOGP\alpha_{\rm OGP}vsmm, for different values ofβ\beta. The change in monotonicity that occurs at largemmis unphysical, and conjectured to be due to the RS Ansatz for the computation of the quenched free entropy; however, at higher temperatures the change of slope becomes progressively weaker.

The left panel of Figure2shows the entropysm​(q1;β)s_{m}(q_{1};\beta)form=2m=2and a positive temperature, as a function of the overlap between pairs of solutionsq1q_{1}, for different values ofα\alpha. The entropy is a non-monotonic function ofq1q_{1}. Asα\alphais increased, the entropy curves shift downward. The OGP threshold is identified as the smallest value ofα\alphaat which a forbidden interval of overlaps appears, namely when the minimum of the entropy curve as a function ofq1q_{1}first touches zero.

The right panel of Figure2showsαOGP\alpha_{\rm OGP}as a function ofmm. For all the values ofβ\betawe have plotted,αOGP​(m)\alpha_{\rm OGP}(m)is a non-monotonic function ofmm.Figure 3:OGP thresholds in the training error vsα\alphaplane. For each training error, the Overlap Gap Property holds forα>minm⁡αOGP​(m)\alpha>\min_{m}\alpha_{\rm OGP}(m). The inset plot shows the same OGP thresholds but in theα−T\alpha-Tplane.

The OGP thresholdαOGP​(m)\alpha_{\rm OGP}(m), is however expected to be a non-increasing function ofmm. Indeed, if for a given value ofα\alphathere existmmconfigurations𝒘1,…,𝒘m\bm{w}^{1},\ldots,\bm{w}^{m}satisfying the prescribed single-replica energy constraint and the required pairwise overlap constraints, then any subset ofm′<mm^{\prime}<mamong them automatically satisfies the same conditions. Hence the existence of an admissiblemm-tuple implies the existence of an admissiblem′m^{\prime}-tuple ifm′<mm^{\prime}<m. Consequently, increasingmmcan only make the constrained replicated problem in (22) harder to satisfy, and the OGP threshold is expected to be non-increasing:αOGP​(m)≤αOGP​(m′)form′<m.\alpha_{\rm OGP}(m)\leq\alpha_{\rm OGP}(m^{\prime})\qquad\text{for}\quad m^{\prime}<m\,.(30)

The non-monotonic dependence onmmobserved in the RS computation is therefore unphysical, and should be interpreted as an artefact of the RS Ansatz for the replicated constrained problem. The same phenomenon was already observed at zero temperature for both the ABP, SBP and in related modelsGamarniket al.(2022); Benedettiet al.(2025,2026). At finite temperature the artefact persists, but it becomes progressively less pronounced. More precisely, letm⋆=argminmαOGP​(m)m_{\star}=\operatorname*{argmin}_{m}\alpha_{\rm OGP}(m)(31)

denote the value ofmmbeyond which the RS estimate of the OGP threshold starts increasing. We observe thatm⋆m_{\star}shifts to larger values as the temperature is increased, indicating that the onset of the unphysical non-monotone regime is delayed. Some additional figures for the SBP showing a similar phenomenology are reported in AppendixA.2. Notice that the corresponding constrained density thresholdαOGP=minm⁡αOGP​(m)\alpha_{\rm OGP}=\min_{m}\alpha_{\rm OGP}(m)(32)

is an upper bound to the appearance of an overlap gapped phase. Determining the exact value of the OGP threshold requires a more refined replica ansatz capable of eliminating the unphysical non-monotonic dependence ofαOGP​(m)\alpha_{\rm OGP}(m)onmm.

Figure3summarizes the finite-temperature OGP threshold in the ABP, in the teacher-student setting. The plot shows, as a function of the constraint densityα\alpha, the training errorϵm\epsilon_{m}at which the OGP first appears for several values ofmm. Equivalently, the curve separates, for any value ofα\alpha, a large training error region, which it is expected to be algorithmically accessible, from a low training error region, where we expect algorithmic hardness because of the presence of an overlap gap. In the right panel of Figure4we show similar OGP curves in the storage case. In the limitϵ→0\epsilon\to 0(or correspondinglyβ→∞\beta\to\infty), we find in the teacher-student settingαOGP≃1.154\alpha_{\rm OGP}\simeq 1.154, that is the zero-temperature threshold previously found inBaldassiet al.(2015).
In the storage setting we similarly findαOGP≃0.784\alpha_{\rm OGP}\simeq 0.784Benedettiet al.(2025)which is compatible to the results found inBaldassiet al.(2015,2021)using different approaches.Algorithm 1Fixed-temperature reinforced AMPInput:patterns{𝒙μ,yμ}μ=1P\{\bm{x}^{\mu},y^{\mu}\}_{\mu=1}^{P},
inverse temperatureβ\beta, target training errorϵtarg\epsilon^{\rm targ},
reinforcement parameterρ\rho, maximum number of iterationstmaxt_{\max}.Initialize:AMP local fields𝒉t=0∈ℝN\bm{h}^{t=0}\in\mathbb{R}^{N}, marginal magnetization𝒂t=0∈ℝN\bm{a}^{t=0}\in\mathbb{R}^{N}, energetic channel𝒈t=0∈ℝP\bm{g}^{t=0}\in\mathbb{R}^{P}, initial reinforcementρ0=0\rho_{0}=0, and𝒘best←sign⁡(𝒂0)\bm{w}_{\rm best}\leftarrow\operatorname{sign}(\bm{a}^{0}).fort=1,…,tmaxt=1,\ldots,t_{\max}doPerform one rAMP update:(𝒉t,𝒂t,𝒈t)←rAMPstep​(𝒉t−1,𝒂t−1,𝒈t−1;ρt−1,β).\displaystyle(\bm{h}^{t},\bm{a}^{t},\bm{g}^{t})\leftarrow\mathrm{rAMPstep}\left(\bm{h}^{t-1},\bm{a}^{t-1},\bm{g}^{t-1};\rho_{t-1},\beta\right).\lx@algorithmicx@hfillSee Algorithm2for the explicit update.(33)Update the reinforcement:ρt←1−(1−ρ)t.\rho_{t}\leftarrow 1-(1-\rho)^{t}.(34)Construct the binary estimator:𝒘t←sign⁡(𝒂t).\bm{w}^{t}\leftarrow\operatorname{sign}(\bm{a}^{t}).(35)ifϵ​(𝒘t)<ϵ​(𝒘best)\epsilon(\bm{w}^{t})<\epsilon(\bm{w}_{\rm best})then𝒘best←𝒘t\bm{w}_{\rm best}\leftarrow\bm{w}^{t}.endififϵ​(𝒘t)≤ϵtarg\epsilon(\bm{w}^{t})\leq\epsilon^{\rm targ}thenreturnsuccess,𝒘t\bm{w}^{t}.endifendforreturnfailure,𝒘best\bm{w}_{\rm best}.

## IV.1Numerical simulations

We now compare the finite-temperature OGP thresholds with the performance of an explicit algorithmic search for low-energy configurations. For a given value of the constraint densityα=P/N\alpha=P/N, we look for binary configurations with empirical training errorϵ​(𝒘)=1P​∑μ=1PΘ​(−yμN​𝒘⋅𝒙μ)\epsilon(\bm{w})=\frac{1}{P}\sum_{\mu=1}^{P}\Theta\left(-\frac{y^{\mu}}{\sqrt{N}}\bm{w}\cdot\bm{x}^{\mu}\right)(36)

smaller than a prescribed thresholdϵtarg\epsilon^{\rm targ}.
Our starting point is Approximate Message Passing (AMP) applied to the finite-temperature Gibbs measure. At fixed inverse temperatureβ\beta, AMP gives an estimate to the one-site marginal magnetizationsai=⟨wi⟩β,a_{i}=\langle w_{i}\rangle_{\beta}\,,(37)

where⟨∙⟩β\langle\bullet\rangle_{\beta}denotes the average over the Gibbs measure at finite temperature. Equivalently, it computes the local fieldshih_{i}such thatai=tanh⁡hia_{i}=\tanh h_{i}. A binary candidate configuration is then obtained by𝒘⋆=sign⁡(𝒂).\bm{w}_{\star}=\operatorname{sign}(\bm{a}).(38)

However, the standard AMP algorithm does not necessarily produce strongly polarized magnetizationsaia_{i}. This implies that the binary estimator in equation (38) may not correspond to a low-error configuration.Figure 4:OGP vs rAMP algorithm in the ABP, storage setting. Left panel: probability of finding a configuration with target training errorϵtarg\epsilon^{\rm targ}vsα\alphausing the rAMP algorithm at fixed temperature as given in1. Here we have usedN=8000N=8000and we have averaged the results over6060samples. The dashed lines represent sigmoidal fits to the data. Right panel: phase diagram. The red points represent the performance achieved by rAMP at finite temperature and forN=8000N=8000and averaged over6060samples. For each point we have optimized the reinforcement parameterρ\rhoand the inverse temperatureβ\betain order to achieve the highest value of the constraint density possible. The green, blue, and yellow curves denote the boundaries marking the presence ofmm-OGP form=2m=2,33, and44, respectively.

To turn the AMP marginals into an actual binary assignment with low training error, we use the reinforced AMP (rAMP) algorithmBraunstein and Zecchina (2006); Baldassi and Braunstein (2015). The idea of reinforcement is to add a self-aligning contribution to the AMP field update, which progressively polarizes the local fields and drives the magnetizationsaia_{i}towards the vertices of the hypercube. More precisely, ifhi,AMPth_{i,\mathrm{AMP}}^{t}denotes the usual AMP update at iterationtt(see equation (92d) in the Appendix for its expression), we replace it by adding a memory termρt−1​hit−1\rho_{t-1}h_{i}^{t-1}:hit=hi,AMPt+ρt−1​hit−1.h_{i}^{t}=h_{i,\mathrm{AMP}}^{t}+\rho_{t-1}h_{i}^{t-1}.(39)

Usually the reinforcement strengthρt\rho_{t}is set to zero at timet=0t=0and increased during the dynamics. We have used a schedule of the typeρt=1−(1−ρ)t,\rho_{t}=1-(1-\rho)^{t},(40)

whereρ\rhocontrols the rate at which reinforcement is switched on. Ifρ=0\rho=0one hasρt=0\rho_{t}=0for alltt, and the algorithm reduces to
standard AMP.

The complete procedure is summarized in Algorithm1, and detailed in AppendixC. At each iteration we perform one rAMP update at the current value ofβ\beta, construct the binary estimator𝒘t=sign⁡(𝒂t)\bm{w}^{t}=\operatorname{sign}(\bm{a}^{t}), and measure its training error. The run is declared successful ifϵ​(𝒘t)≤ϵtarg\epsilon(\bm{w}^{t})\leq\epsilon^{\rm targ}before the maximal number of iterations is reached. We also record the smallest training error encountered along the trajectory.

The left panel of Figure4shows the empirical success probability as a function ofα\alphafor several values of the target training error, in the storage setting and forN=8000N=8000. For eachϵtarg\epsilon^{\rm targ}, the success probability has a sharp drop asα\alphais increased. As expected, allowing a larger training error shifts this algorithmic transition to larger values ofα\alpha: low-energy states with positive error remain accessible in a range of densities where exact solutions are no longer found by the algorithm. For each target training error the algorithmic transition can be estimated by fitting the data to a sigmoid and finding the point where the success probability is1/21/2. In the right panel of Fig.4we summarize the same data in a phase diagram. The red points show the best rAMP algorithmic threshold for each considered target training errorϵtarg\epsilon^{\rm targ}. Those points have been obtained by tuning the rAMP hyperparameters, namely the reinforcementρ\rhoand the inverse temperatureβ\beta, see AppendixCfor additional details. Whenϵtarg=0\epsilon^{\rm targ}=0, we setβ=∞\beta=\inftyand the procedure reduces to the standard zero temperature rAMP algorithmBraunstein and Zecchina (2006). Those points are to be compared to the OGP thresholds which we present form=2m=2, 3 and 4. The rAMP algorithm qualitatively follows the trend of the OGP thresholds.Figure 5:Left panel: generalization of a clone drawn from the constrained measure withm=2m=2(22) versus the mutual clone overlapq1q_{1}, for several values of the inverse temperatureβ\beta. Here we setα=1.3\alpha=1.3, corresponding to a constraint density in the hard region; the qualitative behavior, however, is unchanged for other values ofα\alpha. The plot shows that for each inverse temperature there exists an overlapq1⋆q_{1}^{\star}with minimal generalization error. Right panel: the red line represents the generalization of a clone drawn from the constrained measure withm=3m=3andq1=0.98q_{1}=0.98versus the temperature. We also display the typical generalization error (blue curve, obtained from the uncloned Gibbs measure (8)) and the Bayesian generalization error (green) for comparison. In both panels, the dashed segments of the curves correspond to unphysical branches with negative entropy.

## VFollowing wide minima in temperature in the teacher–student frameworkFigure 6:Schematic phase diagram of the binary teacher–student perceptron. The upper panels illustrate the structure of the training error landscape in the different regimes, while the lower panel shows the corresponding generalization error as a function of the constraint densityα\alpha. Forα<αOGP≃1.154\alpha<\alpha_{\rm OGP}\simeq 1.154, a wide minimum of zero-training error solutions distinct from the teacher𝒘⋆\bm{w}^{\star}coexists with smaller, isolated clusters of solutions. The wide minimum is easily accessible to local algorithms (such as the zero temperature rAMPBraunstein and Zecchina (2006), black stars in the bottom panel), whereas the isolated clusters are not. This makes the task of optimization, i.e. of finding a zero training error configuration easy (phase A in the diagram). Nevertheless, exact inference remains information-theoretically impossible belowαIT≃1.249\alpha_{\rm IT}\simeq 1.249. Forα>αOGP\alpha>\alpha_{\rm OGP}, the wide minimum moves to positive training error and therefore no longer contains solutions. In the regimeαOGP<α<αIT\alpha_{\rm OGP}<\alpha<\alpha_{\rm IT}(phase B), zero-training error configurations distinct from the teacher survive only in isolated clusters separated by an overlap gap and are thus inaccessible to stable algorithms. ForαIT<α<αAMP≃1.492\alpha_{\rm IT}<\alpha<\alpha_{\rm AMP}\simeq 1.492(phase C), the only zero-training error configuration is the teacher, which nevertheless remains algorithmically inaccessible. However, the wide minimum of configurations at positive training error can still be targeted by the finite temperature rAMP algorithm described in1(fuchsia stars) and retain good generalization capabilities. Finally, forα>αAMP\alpha>\alpha_{\rm AMP}(phase D), the teacher can be efficiently recovered. We also show in the bottom panel the generalization error of typical (isolated) solutions (blue), of a clone drawn from the constrained measure (22) withm=3m=3andq1=0.9q_{1}=0.9(red). The green curve represents the Bayesian error i.e. the error of the barycenter over all typical solutions. The dashed parts of the curves correspond to an unphysical negative entropy.

We now turn to the teacher–student setting and investigate the generalization properties of finite-energy configurations that can be targeted by algorithms.

As shown in the previous section, the wide and flat region of zero training error solutions fractures onceα\alphaexceedsαOGP≃1.154\alpha_{\rm OGP}\simeq 1.154due to the presence of OGP in the space of solutions. Nevertheless, robust dense configurations continue to exist at positive training error and may, in principle, be targeted by algorithms operating at finite temperature. In this section, we study the question of whether those regions at finite training error retain good generalization properties. We first show analytical evidence that such configurations have rather good generalization and then provide numerical evidence that these regions are also algorithmically accessible.

Our analytical approach is based on a comparison between two classes of estimators. The first consists of typical students sampled from the Gibbs measure in Eq. (8). As discussed above, this measure is dominated by isolated frozen configurations, which may have a nonzero overlap with the teacher but are not expected to be efficiently accessible to stable algorithms. The second class is obtained from the constrainedmm-clone measure introduced in Eq. (22), in whichmmstudents are constrained to have mutual overlapq1q_{1}. By forcing several configurations to remain close to one another, this measure favors regions with large local entropy and therefore provides a proxy for wide and flat portions of the landscape.

The left panel of Figure5shows the generalization error of a clone drawn from the constrained measure as a function of the imposed mutual overlapq1q_{1}. At fixedα\alphaandβ\beta, the dependence onq1q_{1}is non-monotonic. For smallq1q_{1}, the clones are too far apart to identify a coherent local structure, whereas the limitq1→1q_{1}\to 1approaches an isolated configuration. Between these two limits, the generalization error reaches a minimum at an optimal overlapq1⋆q_{1}^{\star}. The same analysis can be repeated at finite temperature. Increasing the temperature generally worsens generalization, as expected, but the degradation is gradual. Wide regions can therefore be continuously followed from zero to positive temperature while retaining a generalization error substantially smaller than that of typical configurations. Searching for robust configurations with low, but nonzero, training error therefore does not immediately compromise their alignment with the teacher. This behavior is shown more directly in the right panel of Fig.5, where we compare the optimal generalization error of the constrained clones with that of a typical Gibbs configuration and with the Bayesian estimator associated with the barycenter of the Gibbs measure. Over the temperature range shown, the constrained-clone estimator continues to outperform a typical isolated configuration.

We now place this result in the phase diagram of the binary teacher–student perceptron and examine whether these informative wide regions are also algorithmically accessible. Figure6summarizes the resulting picture. Forα<αOGP≃1.154\alpha<\alpha_{\rm OGP}\simeq 1.154, a wide minimum containing zero-training error configurations coexists with smaller, isolated clusters. The wide minimum is accessible to local algorithms, whereas the isolated clusters are not. Onceα\alphaexceedsαOGP\alpha_{\rm OGP}, the wide minimum moves to positive training error. In the intervalαOGP<α<αIT≃1.249\alpha_{\rm OGP}<\alpha<\alpha_{\rm IT}\simeq 1.249, exact solutions distinct from the teacher survive only in isolated clusters separated by an overlap gap. ForαIT<α<αAMP≃1.492\alpha_{\rm IT}<\alpha<\alpha_{\rm AMP}\simeq 1.492, the teacher is the only zero-training error configuration in the largeNNlimit, but it remains inaccessible to stable algorithms. Nevertheless, the finite-training error continuation of the wide minimum persists throughout this hard region.

The finite-temperature rAMP algorithm introduced in the previous section is able to target this positive-energy wide region, as shown by the fuchsia symbols in Fig.6. The figure therefore combines two complementary conclusions: the analytical calculation of Figure5shows that wide finite-energy configurations retain favorable generalization properties, while the numerical results of Fig.6show that such configurations can be reached algorithmically beyond the zero-temperature OGP threshold. Finally, forα>αAMP\alpha>\alpha_{\rm AMP}, the teacher itself becomes efficiently recoverable.

Finite temperature thus plays a dual role. It relaxes the exact-fitting constraint and restores access to a wide basin in the hard phase, while preserving much of the statistical information carried by the corresponding zero-temperature dense region.

## VIConclusions

We studied the finite-temperature geometry of the solution space of binary perceptron models, extending the zero-temperature picture of frozen 1RSB structure and the overlap gap property to the regime where imperfect classification is allowed and statistically weighted. We found that the equilibrium measure remains dynamically frozen at every finite temperature, and traced this to a discontinuity of the single-pattern Gibbs weight at the decision boundary. Smoothing the Gibbs weight, as in Horner’s constructionHorner (1992), removes the frozen solution at any positive temperature, while using the log-potential on constraints satisfied with high margin, as inStraziotaet al.(2025), removes freezing down to zero temperature. At the level of atypical dense regions, we showed that the OGP threshold can be continuously followed in temperature, growing asαOGP​(T)\alpha_{\rm OGP}(T), consistent with the intuition that tolerating errors makes room for more constraints - a trend qualitatively reproduced by a finite-temperature message-passing algorithm. In the teacher-student setting, these finite-energy dense regions remain informative about the planted signal, and thermal noise extends the range of constraint densities over which good generalization is algorithmically achievable, even when exact recovery of the teacher is information theoretically impossible.

An open question for future work is whether these finite-temperature wide minima are responsible for the information-theoretic hardness of exact inference in the regimeαIT<α<αAMP\alpha_{\rm IT}<\alpha<\alpha_{\rm AMP}. It also remains to be understood whether, forα>αAMP\alpha>\alpha_{\rm AMP}, the teacher becomes embedded within such wide finite-energy minima, thereby explaining the empirical success of replicated or annealed search strategies.

Acknowledgements.
We thank Gianmarco Perrupato for interesting discussions.

## References
- Baldassiet al.(2015)C. Baldassi, A. Ingrosso,
C. Lucibello, L. Saglietti, and R. Zecchina,Phys. Rev. Lett.115, 128101 (2015).
- Baldassiet al.(2016)C. Baldassi, C. Borgs,
J. T. Chayes, A. Ingrosso, C. Lucibello, L. Saglietti, and R. Zecchina,Proceedings of the National Academy of Sciences113, E7655 (2016),https://www.pnas.org/doi/pdf/10.1073/pnas.1608103113.
- Chaudhariet al.(2019)P. Chaudhari, A. Choromanska, S. Soatto,
Y. LeCun, C. Baldassi, C. Borgs, J. Chayes, L. Sagun, and R. Zecchina,Journal of Statistical Mechanics:
Theory and Experiment2019, 124018 (2019).
- Gamarnik (2021)D. Gamarnik,Proceedings of the National Academy of Sciences 
(2021), 10.1073/pnas.2108492118.
- Gamarnik and Jagannath (2021)D. Gamarnik and A. Jagannath,The Annals of Probability49, pp. 180 (2021).
- Gamarnik and Sudan (2017)D. Gamarnik and M. Sudan,The Annals of Probability45, 2353 (2017).
- Gamarniket al.(2022)D. Gamarnik, E. C. Kizildag, W. Perkins, and C. Xu, in2022
IEEE 63rd Annual Symposium on Foundations of Computer Science (FOCS)(2022) pp. 576–587.
- Baldassiet al.(2023)C. Baldassi, E. M. Malatesta, G. Perugini,
 and R. Zecchina,Phys. Rev. E108, 024310 (2023).
- Kaplanet al.(2020)J. Kaplan, S. McCandlish,
T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei,ArXivabs/2001.08361(2020).
- Hoffmannet al.(2022)J. Hoffmann, S. Borgeaud,
A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. de Las Casas, L. A. Hendricks, J. Welbl, A. Clark,
T. Hennigan, E. Noland, K. Millican, G. van den Driessche, B. Damoc, A. Guy, S. Osindero, K. Simonyan,
E. Elsen, O. Vinyals, J. W. Rae, and L. Sifre, inProceedings of the 36th International Conference on
Neural Information Processing Systems, NIPS
’22 (Curran Associates Inc., Red Hook, NY, USA, 2022).
- Krauth and Mézard (1989)W. Krauth and M. Mézard,Journal de Physique (1989), 10.1051/jphys:0198900500200305700.
- Aubinet al.(2019)B. Aubin, W. Perkins, and L. Zdeborová, Journal of Physics
A: Mathematical and Theoretical52, 294003 (2019).
- Huang and Kabashima (2014)H. Huang and Y. Kabashima,Physical Review E (2014), 10.1103/physreve.90.052813.
- Horner (1992)H. Horner,Zeitschrift für Physik B Condensed Matter86, 291 (1992).
- Mézardet al.(1987)M. Mézard, G. Parisi,
 and M. A. Virasoro,Spin glass theory
and beyond(World Scientific, Singapore, 1987).
- Stojnic (2026a)M. Stojnic, arXiv
preprint arXiv:2601.10628 (2026a).
- Stojnic (2026b)M. Stojnic, arXiv
preprint arXiv:2604.19712 (2026b).
- Györgyi (1990)G. Györgyi,Phys. Rev. A41, 7097(R) (1990).
- Gardner and Derrida (1989)E. Gardner and B. Derrida,Journal of Physics A: Mathematical and
General22, 1983
(1989).
- Gardner and Derrida (1988)E. Gardner and B. Derrida,Journal of Physics A: Mathematical and
General (1988), 10.1088/0305-4470/21/1/031.
- Opper and Haussler (1991)M. Opper and D. Haussler,Phys. Rev. Lett.66, 2677 (1991).
- Baldassiet al.(2021)C. Baldassi, C. Lauditi,
E. M. Malatesta, G. Perugini, and R. Zecchina,Phys. Rev. Lett.127, 278301 (2021).
- Perkins and Xu (2024)W. Perkins and C. Xu,Random Structures & Algorithms64, 856 (2024).
- Barbieret al.(2024)D. Barbier, A. El Alaoui,
F. Krzakala, and L. Zdeborová,Journal of Physics A: Mathematical and Theoretical57, 195202 (2024).
- Barbier (2025a)D. Barbier,SciPost Phys.18, 115 (2025a).
- Kirkpatrick and Thirumalai (1987)T. R. Kirkpatrick and D. Thirumalai,Phys. Rev. Lett.58, 2091 (1987).
- Cataniaet al.(2024)G. Catania, A. Decelle, and B. Seoane,Physical Review E (2024), 10.1103/physreve.109.065313.
- Straziotaet al.(2025)D. Straziota, E. Demyanenko, C. Baldassi, and C. Lucibello, inAdvances in Neural Information Processing
Systems, Vol. 38, edited by D. Belgrave, C. Zhang, H. Lin, R. Pascanu, P. Koniusz, M. Ghassemi, and N. Chen (Curran Associates,
Inc., 2025) pp. 111927–111966.
- Braunstein and Zecchina (2006)A. Braunstein and R. Zecchina,Physical Review Letters96(2006), 10.1103/physrevlett.96.030201.
- Baldassi and Braunstein (2015)C. Baldassi and A. Braunstein,Journal of Statistical Mechanics: Theory and
Experiment2015(2015), 10.1088/1742-5468/2015/08/p08008.
- Barbier (2025b)D. Barbier, arXiv
preprint arXiv:2505.20954 (2025b).
- Angelini and Ricci-Tersenghi (2023)M. C. Angelini and F. Ricci-Tersenghi,Phys. Rev. X13, 021011 (2023).
- Budzynskiet al.(2019)L. Budzynski, F. Ricci-Tersenghi, and G. Semerjian,Journal of Statistical Mechanics: Theory and
Experiment2019, 023302
(2019).
- Budzynski and Semerjian (2020)L. Budzynski and G. Semerjian,Journal of Statistical Mechanics: Theory and
Experiment2020, 103406
(2020).
- Angeliniet al.(2025)M. C. Angelini, L. Budzynski,
 and F. Ricci-Tersenghi,Phys. Rev. E112, 064117 (2025).
- Benedettiet al.(2025)M. Benedetti, A. Bogdanov,
E. M. Malatesta, M. Mézard, G. Perrupato, A. Rosen, N. I. Schwartzbach, and R. Zecchina,Journal
of Statistical Mechanics: Theory and Experiment2025, 123303 (2025).
- Monasson (1995a)R. Monasson,Phys. Rev. Lett.75, 2847 (1995a).
- Baldassiet al.(2020)C. Baldassi, F. Pittorino,
 and R. Zecchina,Proceedings of the National Academy of Sciences117, 161 (2020),https://www.pnas.org/doi/pdf/10.1073/pnas.1908636117.
- Benedettiet al.(2026)M. Benedetti, A. Bogdanov,
E. M. Malatesta, M. Mézard, G. Perrupato, A. Rosen, N. I. Schwartzbach, and R. Zecchina,Phys. Rev. X16, 021051 (2026).
- Malatesta (2023)E. M. Malatesta, arXiv preprint arXiv:2309.09240 (2023).
- Parisi (1979)G. Parisi, Physics Letters A73, 203 (1979).
- Monasson (1995b)R. Monasson,Phys. Rev. Lett.75, 2847 (1995b).
- Mézard and Montanari (2009)M. Mézard and A. Montanari,Information, Physics, and Computation(Oxford University Press, 2009).

## Appendices

## Appendix AThe free entropy

The quenched average in the definition of the free entropy in equation (6) of the main text can be performed introducingnnvirtualreplicas of the system and using the replica trick:ϕ=limN→∞limn→0⟨Z𝒟n⟩𝒟−1n​N.\phi=\lim_{N\to\infty}\lim_{n\to 0}\frac{\langle Z^{n}_{\mathcal{D}}\rangle_{\mathcal{D}}-1}{nN}\,.(41)

After standard manipulations, one finds the general expression for the replicated partition function:⟨Z𝒟n⟩𝒟=∫∏a<bd​qa​b​d​q^a​b​∏ad​ra​d​r^a​eN​S​(𝒒,𝒒^,𝒓,𝒓^),\langle Z^{n}_{\mathcal{D}}\rangle_{\mathcal{D}}=\int\prod_{a<b}dq_{ab}d\hat{q}_{ab}\prod_{a}dr_{a}d\hat{r}_{a}\,e^{NS(\bm{q},\bm{\hat{q}},\bm{r},\bm{\hat{r}})}\,,(42)

whereqa​bq_{ab}andrar_{a}physically represent the student-student overlap matrix and the teacher-student overlap – when a teacher is present,ra>0r_{a}>0, see Table1– respectivelyMalatesta (2023). The functionSSis decomposed into anentropicGSG_{S}and anenergetictermGEG_{E}as:S​(𝒒,𝒒^,𝒓,𝒓^)\displaystyle S(\bm{q},\bm{\hat{q}},\bm{r},\bm{\hat{r}})=GS​(𝒒,𝒒^,𝒓,𝒓^)+α​GE​(𝒒,𝒓),\displaystyle=G_{S}(\bm{q},\bm{\hat{q}},\bm{r},\bm{\hat{r}})+\alpha G_{E}(\bm{q},\bm{r})\,,(43a)GS​(𝒒,𝒒^,𝒓,𝒓^)\displaystyle G_{S}(\bm{q},\bm{\hat{q}},\bm{r},\bm{\hat{r}})=−12​∑a≠bqa​b​q^a​b−∑ara​r^a+ln​∑{wa=±1}e12​∑a≠bq^a​b​wa​wb+∑ar^a​wa,\displaystyle=-\frac{1}{2}\sum_{a\neq b}q_{ab}\hat{q}_{ab}-\sum_{a}r_{a}\hat{r}_{a}+\ln\sum_{\{w^{a}=\pm 1\}}\ e^{\frac{1}{2}\sum_{a\neq b}\hat{q}_{ab}w^{a}w^{b}+\sum_{a}\hat{r}_{a}w^{a}}\,,(43b)GE​(𝒒,𝒓)\displaystyle G_{E}(\bm{q},\bm{r})=ln​∫d​ν​d​ν^2​π​∏ad​ua​d​u^a2​π​∏a𝒦​(sign⁡(ν)​ua)​ei​∑aua​u^a+i​ν​ν^−12​∑a​bqa​b​u^a​u^b−ν^22−ν^​∑au^a​ra.\displaystyle=\ln\int\frac{d\nu d\hat{\nu}}{2\pi}\prod_{a}\frac{du_{a}d\hat{u}_{a}}{2\pi}\prod_{a}\mathcal{K}\left(\operatorname{sign}(\nu)u_{a}\right)e^{i\sum_{a}u_{a}\hat{u}_{a}+i\nu\hat{\nu}-\frac{1}{2}\sum_{ab}q_{ab}\hat{u}_{a}\hat{u}_{b}-\frac{\hat{\nu}^{2}}{2}-\hat{\nu}\sum_{a}\hat{u}_{a}r_{a}}\,.(43c)

The free entropyϕ\phican be computed by solving the following extremization problemϕ=limn→0extr𝒒,𝒒^,𝒓,𝒓^​S​(𝒒,𝒒^,𝒓,𝒓^)n.\phi=\lim_{n\to 0}\mathrm{extr}_{\bm{q},\hat{\bm{q}},\bm{r},\hat{\bm{r}}}\,\frac{S(\bm{q},\hat{\bm{q}},\bm{r},\hat{\bm{r}})}{n}\,.(44)

Note how the energetic term depends on the generic Gibbs weight𝒦\mathcal{K}; see Eqs. (7), (10) in the main text. We keep the discussion general, but for clarity of the reader, Table1contains a summary of how to specify the equations for the model considered in this paper (ABP/SBP) and setting (storage/teacher-student).SBP (with marginκ>0\kappa>0)ABP (storage)ABP (teacher-student)𝒦S​B​P\mathcal{K}^{SBP}𝒦A​B​P\mathcal{K}^{ABP}𝒦A​B​P\mathcal{K}^{ABP}r=r^=0r=\hat{r}=0r=r^=0r=\hat{r}=0r=r⋆,r^=r^⋆r=r^{\star},\;\hat{r}=\hat{r}^{\star}Table 1:Recipe for each model, to be inserted in Eq. (43). The single-pattern Gibbs weight for the ABP and SBP models,𝒦A​B​P\mathcal{K}_{ABP}and𝒦S​B​P\mathcal{K}_{SBP}, are defined in Eqs. (7) and (10), respectively.

## A.1RS Ansatz

We consider here the standard replica symmetric (RS) assumption on the student overlap matrix and its conjugateqa​b\displaystyle q_{ab}=δa​b+(1−δa​b)​q\displaystyle=\delta_{ab}+(1-\delta_{ab})q\,q^a​b\displaystyle\hat{q}_{ab}=(1−δa​b)​q^;\displaystyle=(1-\delta_{ab})\hat{q}\,;

moreover we impose for the teacher-student overlapsra\displaystyle r_{a}=r\displaystyle=r\,r^a\displaystyle\hat{r}_{a}=r^.\displaystyle=\hat{r}\,.

A standard computation gives the free entropy (44):SRS​(q,q^,r,r^)\displaystyle S^{\mathrm{RS}}(q,\hat{q},r,\hat{r})=𝒢SRS​(q,q^,r,r^)+α​𝒢ERS​(q,r),\displaystyle=\mathcal{G}^{\mathrm{RS}}_{S}(q,\hat{q},r,\hat{r})+\alpha\mathcal{G}^{\mathrm{RS}}_{E}(q,r)\,,(45a)𝒢SRS​(q,q^,r,r^)\displaystyle\mathcal{G}^{\mathrm{RS}}_{S}(q,\hat{q},r,\hat{r})=−q^2​(1−q)−r^​r+∫D​z​ln⁡2​cosh⁡(q^​z+r^),\displaystyle=-\frac{\hat{q}}{2}(1-q)-\hat{r}r+\int Dz\,\ln 2\cosh\left(\sqrt{\hat{q}}z+\hat{r}\right)\,,(45b)𝒢ERS​(q,r)\displaystyle\mathcal{G}^{\mathrm{RS}}_{E}(q,r)=2​∫D​z​H​(−r​zq−r2)​ln⁡ℋ​(q​z,1−q),\displaystyle=2\int Dz\,H\left(-\frac{rz}{\sqrt{q-r^{2}}}\right)\ln\mathcal{H}\left(\sqrt{q}z,\sqrt{1-q}\right)\,,(45c)

whereℋ​(x,y)=∫D​z​𝒦​(x+y​z).\mathcal{H}(x,y)=\int Dz\,\mathcal{K}(x+yz)\,.(46)

In particular for the ABP and SBP with standard training error loss function one hasℋ​(x,y)\displaystyle\mathcal{H}(x,y)=e−β+(1−e−β)​ℋ∞​(x,y),\displaystyle=e^{-\beta}+(1-e^{-\beta})\mathcal{H}_{\infty}(x,y)\,,(47a)

whereℋ∞​(x,y)\mathcal{H}_{\infty}(x,y)depends on the particular model we consider:ℋ∞ABP​(x,y)\displaystyle\mathcal{H}_{\infty}^{\mathrm{ABP}}\left(x,y\right)=H​(−xy),\displaystyle=H\left(-\frac{x}{y}\right)\,,(48a)ℋ∞SBP​(x,y)\displaystyle\mathcal{H}_{\infty}^{\mathrm{SBP}}\left(x,y\right)=∑s=±1s​H​(−s​κ+xy),\displaystyle=\sum_{s=\pm 1}sH\left(\frac{-s\kappa+x}{y}\right)\,,(48b)

beingH​(x)=∫x∞D​h=12​Erfc​(x2)H(x)=\int_{x}^{\infty}Dh=\frac{1}{2}\mathrm{Erfc}\left(\frac{x}{\sqrt{2}}\right). The thermodynamic free entropy is computed at the values ofq,q^,r,r^q,\hat{q},r,\hat{r}extremizing the functionSR​SS^{RS}:ϕRS=extrq,q^,r,r^​[SRS​(q,q^,r,r^)].\phi^{\mathrm{RS}}=\mathrm{extr}_{q,\hat{q},r,\hat{r}}\left[S^{\mathrm{RS}}(q,\hat{q},r,\hat{r})\right]\,.(49)

In the SBP the equilibrium value of the overlap isq=q^=0q=\hat{q}=0by symmetry111The same argument for the SBP applies for the parameterq0q_{0}in the 1RSB computation..

## A.21RSB Ansatz and entropy of them-cloned systemFigure 7:Left panel: SBP:ϕm​(q1)\phi_{m}(q_{1})forκ=1\kappa=1,m=2m=2,β→∞\beta\to\inftyfor different values ofα\alpha. Atα≃1.700\alpha\simeq 1.700, the minimum of the free entropy reaches zero, marking the OGP threshold, see Table2.
Right panel: ABP:ϕm​(q1)\phi_{m}(q_{1})form=4m=4andβ→∞\beta\to\infty. Our OGP threshold estimate for the ABP isαOGP≃0.784\alpha_{\rm OGP}\simeq 0.784, see Figure8.

A more refined parameterization of the student overlap matrixqa​bq_{ab}is in general needed to compute the equilibrium value of the free entropyParisi (1979). We consider here a 1-step replica symmetry breaking (1RSB) Ansatz which consists in imposingqa​b\displaystyle q_{ab}=q0+(q1−q0)​Ia​b(n,m)+(1−q1)​Ia​b(n,1)\displaystyle=q_{0}+(q_{1}-q_{0})I_{ab}^{(n,m)}+(1-q_{1})I_{ab}^{(n,1)}(50a)q^a​b\displaystyle\hat{q}_{ab}={q^0+(q^1−q^0)​Ia​b(n,m)+(1−q^1)​Ia​b(n,1)a≠b0a=b\displaystyle=\begin{cases}\hat{q}_{0}+(\hat{q}_{1}-\hat{q}_{0})I_{ab}^{(n,m)}+(1-\hat{q}_{1})I_{ab}^{(n,1)}\quad&a\neq b\\
0&a=b\end{cases}(50b)

whereIa​b(n,m)I_{ab}^{(n,m)}is the(a,b)(a,b)element of a block matrix of sizen×nn\times nwhose diagonal blocks have sizem×mm\times mand contain all ones and outside of them the matrix is composed of zeros. We leave unchanged the Ansatz over the teacher-student overlaps.
The corresponding free entropy is given by:ϕ1​R​S​B\displaystyle\phi^{\mathrm{1RSB}}=extrq0,q^0,q1,q^1,r,r^,m​[S1​R​S​B​(q0,q^0,q1,q^1,r,r^,m)]\displaystyle=\mathrm{extr}_{q_{0},\hat{q}_{0},q_{1},\hat{q}_{1},r,\hat{r},m}\left[S^{\mathrm{1RSB}}(q_{0},\hat{q}_{0},q_{1},\hat{q}_{1},r,\hat{r},m)\right](51a)S1​R​S​B\displaystyle S^{\mathrm{1RSB}}=𝒢S1​R​S​B+α​𝒢E1​R​S​B\displaystyle=\mathcal{G}^{\mathrm{1RSB}}_{S}+\alpha\mathcal{G}^{\mathrm{1RSB}}_{E}(51b)𝒢S1​R​S​B\displaystyle\mathcal{G}_{S}^{\mathrm{1RSB}}=−q^12​(1−q1)+m2​(q0​q^0−q1​q^1)−r^​r+1m​∫D​z0​ln​∫D​z1​(2​cosh⁡(q^0​z0+q^1−q^0​z1+r^))m\displaystyle=-\frac{\hat{q}_{1}}{2}\left(1-q_{1}\right)+\frac{m}{2}\left(q_{0}\hat{q}_{0}-q_{1}\hat{q}_{1}\right)-\hat{r}r+\frac{1}{m}\int Dz_{0}\,\ln\int Dz_{1}\left(2\cosh\left(\sqrt{\hat{q}_{0}}z_{0}+\sqrt{\hat{q}_{1}-\hat{q}_{0}}z_{1}+\hat{r}\right)\right)^{m}(51c)𝒢E1​R​S​B\displaystyle\mathcal{G}_{E}^{\mathrm{1RSB}}=2m​∫D​z0​H​(−r​z0q0−r2)​ln​∫D​z1​ℋm​(q0​z0+q1−q0​z1,1−q1)\displaystyle=\frac{2}{m}\int Dz_{0}\,H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)\,\ln\int Dz_{1}\,\mathcal{H}^{m}\left({\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1}},{\sqrt{1-q_{1}}}\right)(51d)

whereℋ\mathcal{H}is defined in (47a).
Note also that this expression can be used to find the entropy density ofmm-clones of the model constrained to be at a given overlapq1q_{1}as in equation (23)Monasson (1995b). Indeed, notice that in this case themmreplicas are “real”, andnnvirtual replicas of the cloned system are introduced, so thatnnshould be replaced withn​mnmin the previous formulas (50). Moreover one should not optimize over bothmmandq1q_{1}, as they are treated as external parameters. Mathematically, we have:ϕm​(q1)=extrq0,q^0,q^1,r,r^​[𝒢S1​R​S​B+α​𝒢E1​R​S​B].\phi_{m}(q_{1})=\mathrm{extr}_{q_{0},\hat{q}_{0},\hat{q}_{1},r,\hat{r}}\left[\mathcal{G}^{\mathrm{1RSB}}_{S}+\alpha\mathcal{G}^{\mathrm{1RSB}}_{E}\right]\,.(52)

Figure7shows exemplary curves for the SBP and ABP as a function of the overlapq1q_{1}. As described in the main text, themm-OGP threshold at zero temperature can be found by solving (26):ϕm​(q1)\displaystyle\phi_{m}(q_{1})=0,\displaystyle=0\,,∂q1ϕm​(q1)\displaystyle\partial_{q_{1}}\phi_{m}(q_{1})=0.\displaystyle=0\,.

Similar conditions hold forαOGP\alpha_{\rm OGP}threshold atβ>0\beta>0, see Eqs. (29).
Figure8showsαOGP\alpha_{\rm OGP}as a function ofmmfor the SBP and ABP in the storage setting and for different values of the inverse temperatureβ\beta. Note that ifm′>mm^{\prime}>mone should haveαOGP​(m′)<αOGP​(m)\alpha_{\rm OGP}(m^{\prime})<\alpha_{\rm OGP}(m), by the very definition of OGP. The increasing part of those curves are therefore clearly nonphysicalBenedettiet al.(2025). It can be verified that such points are also characterized by a negative complexityΣ<0\Sigma<0. We have summarized in table2the OGP threshold we have obtained for the SBP withκ=1\kappa=1at zero temperature, and we compare them with the rigorous annealed bound established inGamarniket al.(2022).Figure 8:αOGP\alpha_{\rm OGP}as a function ofmmfor the SBP withκ=1\kappa=1and ABP (right panel). At larger temperatures, the curves become less unphysical as the increasing part of the curves become less pronounced. Therefore the RS approximation we made on the on the cloned free entropy in equation (23) becomes less dramatic.mmRS estimate ofαOGP(sbp)​(m)\alpha^{(\mathrm{sbp})}_{\mathrm{OGP}}(m)Annealed boundGamarniket al.(2022)221.70011.70011.711.71331.66641.66641.6671.667441.65781.6578–551.65931.6593–Table 2:OGP threshold for the symmetric binary perceptron withκ=1\kappa=1: comparison between the RS estimate and the rigorous first moment bounds of Ref.Gamarniket al.(2022). Our RS estimates of the OGP thresholds are consistent with the ones reported inStojnic (2026a,b)obtained using another analytical machinery.

## Appendix BComputation of the dynamical temperature

We carry out here the computation of the dynamical temperatureTdT_{d}. The computation is general for both the storage and teacher-student settings.
In order to find outTdT_{d}, we need to expand the 1RSB free entropy functionalS1​R​S​BS^{\mathrm{1RSB}}given in (51b) aroundm=1m=1Kirkpatrick and Thirumalai (1987). At zeroth order we simply get the RS free entropy (45), withq=q0q=q_{0}andq^=q^0\hat{q}=\hat{q}_{0}.
The first order correction is:S1​R​S​B​(q0,q^0,q1,q^1,r,r^)=SRS​(q0,q^0,r,r^)+(m−1)​ϕ~​(q0,q^0,q1,q^1,r,r^)+O​((m−1)2),S^{\mathrm{1RSB}}(q_{0},\hat{q}_{0},q_{1},\hat{q}_{1},r,\hat{r})=S^{\mathrm{RS}}(q_{0},\hat{q}_{0},r,\hat{r})+(m-1)\tilde{\phi}(q_{0},\hat{q}_{0},q_{1},\hat{q}_{1},r,\hat{r})+O\left((m-1)^{2}\right)\,,(53)

where the functionϕ~\tilde{\phi}is defined asϕ~\displaystyle\tilde{\phi}=∂S1​R​S​B∂m|m=1=∂𝒢S∂m|m=1+α​∂𝒢E∂m|m=1,\displaystyle=\left.\frac{\partial S^{\mathrm{1RSB}}}{\partial m}\right|_{m=1}=\left.\frac{\partial\mathcal{G}_{S}}{\partial m}\right|_{m=1}+\alpha\left.\frac{\partial\mathcal{G}_{E}}{\partial m}\right|_{m=1}\,,(54)

and it is given byϕ~​(q0,q^0,q1,q^1,r,r^)=−SRS​(q0,q^0,r,r^)−r​r^+q0​q^0−q^12​(1+q1)+ℐS​(q^0,q^1,r^)+α​ℐE​(q0,q1,r)\displaystyle\tilde{\phi}(q_{0},\hat{q}_{0},q_{1},\hat{q}_{1},r,\hat{r})=-S^{\mathrm{RS}}(q_{0},\hat{q}_{0},r,\hat{r})-r\hat{r}+q_{0}\hat{q}_{0}-\frac{\hat{q}_{1}}{2}(1+q_{1})+\mathcal{I}_{S}(\hat{q}_{0},\hat{q}_{1},\hat{r})+\alpha\mathcal{I}_{E}(q_{0},q_{1},r)(55a)ℐS\displaystyle\mathcal{I}_{S}=e−q^1−q^02​∫D​z0​∫D​z1​cosh⁡(q^0​z0+q^1−q^0​z1+r^)​ln⁡2​cosh⁡(q^0​z0+q^1−q^0​z1+r^)cosh⁡(q^0​z0+r^)\displaystyle=e^{-\frac{\hat{q}_{1}-\hat{q}_{0}}{2}}\int Dz_{0}\,\frac{\int Dz_{1}\,\cosh\left(\sqrt{\hat{q}_{0}}z_{0}+\sqrt{\hat{q}_{1}-\hat{q}_{0}}z_{1}+\hat{r}\right)\ln 2\cosh\left(\sqrt{\hat{q}_{0}}z_{0}+\sqrt{\hat{q}_{1}-\hat{q}_{0}}z_{1}+\hat{r}\right)}{\cosh(\sqrt{\hat{q}_{0}}z_{0}+\hat{r})}(55b)ℐE\displaystyle\mathcal{I}_{E}=2​∫D​z0​H​(−r​z0q0−r2)​∫D​z1​ℋ​(q0​z0+q1−q0​z1,1−q1)​ln⁡ℋ​(q0​z0+q1−q0​z1,1−q1)ℋ​(q0​z0,1−q0)\displaystyle=2\int Dz_{0}\,H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)\frac{\int Dz_{1}\,\mathcal{H}\left({\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1}},{\sqrt{1-q_{1}}}\right)\ln\mathcal{H}\left({\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1}},{\sqrt{1-q_{1}}}\right)}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}},{\sqrt{1-q_{0}}}\right)}(55c)

We recall that equilibrium values of the parametersq0,q0^,q1,q1^,r,r^q_{0},\hat{q_{0}},q_{1},\hat{q_{1}},r,\hat{r}are those that extremizeS1​R​S​BS^{\rm 1RSB}.
Notice thatq0q_{0},q^0\hat{q}_{0},rr,r^\hat{r}in them→1m\to 1limit need to solve the saddle point equations for the RS free entropy (45), whileq1q_{1}andq^1\hat{q}_{1}can be found by extremizingϕ~\tilde{\phi}only. In summary one has to solve the following saddle point equations:∂q^0SRS​(q0,q^0,r,r^)\displaystyle\partial_{\hat{q}_{0}}S^{\mathrm{RS}}(q_{0},\hat{q}_{0},r,\hat{r})=0,\displaystyle=0\,,(56a)∂q0SRS​(q0,q^0,r,r^)\displaystyle\partial_{q_{0}}S^{\mathrm{RS}}(q_{0},\hat{q}_{0},r,\hat{r})=0,\displaystyle=0\,,(56b)∂r^SRS​(q0,q^0,r,r^)\displaystyle\partial_{\hat{r}}S^{\mathrm{RS}}(q_{0},\hat{q}_{0},r,\hat{r})=0,\displaystyle=0\,,(56c)∂rSRS​(q0,q^0,r,r^)\displaystyle\partial_{r}S^{\mathrm{RS}}(q_{0},\hat{q}_{0},r,\hat{r})=0,\displaystyle=0\,,(56d)∂q^1ϕ~​(q0,q^0,q1,q^1,r,r^)\displaystyle\partial_{\hat{q}_{1}}\tilde{\phi}(q_{0},\hat{q}_{0},q_{1},\hat{q}_{1},r,\hat{r})=0\displaystyle=0(56e)∂q1ϕ~​(q0,q^0,q1,q^1,r,r^)\displaystyle\partial_{q_{1}}\tilde{\phi}(q_{0},\hat{q}_{0},q_{1},\hat{q}_{1},r,\hat{r})=0.\displaystyle=0\,.(56f)

The dynamical temperatureTd​(α)T_{d}(\alpha)for a fixed value ofα\alphais defined as the largest temperature for which a solution withq1>q0q_{1}>q_{0}appears. This can be found numerically as follows. First we numerically solve the first four equations above, respectively forq0q_{0},q^0\hat{q}_{0},rrandr^\hat{r}.
Then consider the last two equations in (56). Using the property of the Kernel (46)∂yℋ​(x,y)=y​∂x2ℋ​(x,y)\partial_{y}\mathcal{H}(x,y)=y\partial_{x}^{2}\mathcal{H}(x,y)and an integration by parts they read0=∂ϕ~∂q^1\displaystyle 0=\frac{\partial\tilde{\phi}}{\partial\hat{q}_{1}}=−q12+12​e−q^1−q^02​∫D​z0​∫D​z1​sinh⁡(q^0​z0+q^1−q^0​z1+r^)​tanh⁡(q^0​z0+q^1−q^0​z1+r^)cosh⁡(q^0​z0+r^)\displaystyle=-\frac{q_{1}}{2}+\frac{1}{2}e^{-\frac{\hat{q}_{1}-\hat{q}_{0}}{2}}\int Dz_{0}\,\frac{\int Dz_{1}\,\sinh\left(\sqrt{\hat{q}_{0}}z_{0}+\sqrt{\hat{q}_{1}-\hat{q}_{0}}z_{1}+\hat{r}\right)\tanh\left(\sqrt{\hat{q}_{0}}z_{0}+\sqrt{\hat{q}_{1}-\hat{q}_{0}}z_{1}+\hat{r}\right)}{\cosh(\sqrt{\hat{q}_{0}}z_{0}+\hat{r})}(57)0=∂ϕ~∂q1\displaystyle 0=\frac{\partial\tilde{\phi}}{\partial q_{1}}=−q^12+α2​∫D​z0​2​H​(−r​z0q0−r2)ℋ​(q0​z0,1−q0)​∫D​z1​(∂xℋ​(q0​z0+q1−q0​z1,1−q1))2ℋ​(q0​z0+q1−q0​z1,1−q1)\displaystyle=-\frac{\hat{q}_{1}}{2}+\frac{\alpha}{2}\int Dz_{0}\,\frac{2H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}},{\sqrt{1-q_{0}}}\right)}\int Dz_{1}\frac{\left(\partial_{x}\mathcal{H}\left({\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1}},{\sqrt{1-q_{1}}}\right)\right)^{2}}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1}},{\sqrt{1-q_{1}}}\right)}(58)

Via equation (58) one expressesq^1\hat{q}_{1}in terms ofq1q_{1}and inserts it in equation (57). One then plots∂q^1ϕ~\partial_{\hat{q}_{1}}\tilde{\phi}as a function ofq1q_{1}. This function will have at any temperature a root whenq1=q0q_{1}=q_{0}corresponding to the RS solution; this is also the only one whenT>Td​(α)T>T_{d}(\alpha). AtTd​(α)T_{d}(\alpha),∂q^1ϕ~\partial_{\hat{q}_{1}}\tilde{\phi}develops a new root at a valueq1>q0q_{1}>q_{0}.

The dynamical temperature depends heavily on the nature of the factor𝒦\mathcal{K}which enters into the definition ofℋ​(x,y)\mathcal{H}(x,y), see (46). In the following subsection we will specialize to the case of the ABP and SBP constraints and with the standard training error loss, counting the number of unsatisfied constraints. We show that wheneverβ=1/T>0\beta=1/T>0, the saddle point equations admit the solutionq1=1q_{1}=1.
This can be observed in Figure9, where we plot∂q^1ϕ~\partial_{\hat{q}_{1}}\tilde{\phi}as a function ofq1q_{1}(for the ABP in the storage case, where one furthermore hasr=r^=0r=\hat{r}=0). This means that in the perceptron model the dynamical temperature always diverges in the largeNNlimit.

The solutionq1=1q_{1}=1corresponds to the so calledfrozen 1RSBscenario already found inHuang and Kabashima (2014)from the zero-temperature static analysis and is consistent with the results found by HornerHorner (1992)in the storage case, which were derived using dynamical mean-field theory.
We will also discuss how to avoid this frozen phase by changing the expression of the energy function.Figure 9:Left:∂q^1ϕ~\partial_{\hat{q}_{1}}\tilde{\phi}for the ABP in the storage case (wherer=r^=0r=\hat{r}=0) as a function ofq1q_{1}, forα=0.7\alpha=0.7and different values ofβ\beta. The solutions of the SPE are the zeros of this function. There is always a zero inq1=q0q_{1}=q_{0}(the value ofq0q_{0}depends onα\alphaandβ\beta) corresponding to the RS solution. For anyβ>0\beta>0, another non-trivial solution of the saddle point equation is found inq1=1q_{1}=1. Right: ABP in the storage setting. The panel presentsϕ~\tilde{\phi}as a function ofq1q_{1}, forα=0.7\alpha=0.7and different values ofβ\beta: its derivative vanishes atq1=1q_{1}=1.

## B.1The frozen 1RSB solution

We specialize here the computation to the ABP for simplicity. Equation (58) solved forq^1\hat{q}_{1}then reads:q^1=α​(1−e−β)21−q1​∫D​z0​2​H​(−r​z0q0−r2)ℋ​(q0​z0,1−q0)​∫D​z1​G​(q0​z0+q1−q0​z11−q1)2ℋ​(q0​z0+q1−q0​z1,1−q1),\hat{q}_{1}=\alpha\frac{(1-e^{-\beta})^{2}}{1-q_{1}}\int Dz_{0}\,\frac{2H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}},{\sqrt{1-q_{0}}}\right)}\int Dz_{1}\,\frac{G\left(\frac{\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1}}{\sqrt{1-q_{1}}}\right)^{2}}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1}},{\sqrt{1-q_{1}}}\right)}\,,(59)

whereG​(x)G(x)denotes the standard Gaussian density function.
Substituting (59) in (57), we have∂ϕ~∂q^1\frac{\partial\tilde{\phi}}{\partial\hat{q}_{1}}as a function ofq1q_{1}only. We want to show that for anyβ>0\beta>0, this derivative vanishes in the limitq1=1q_{1}=1. To do so, takeq1=1−ϵ.q_{1}=1-\epsilon\,.(60)

Then, we computeq^1\hat{q}_{1}from (59), as a function ofϵ≃0\epsilon\simeq 0:q^1\displaystyle\hat{q}_{1}≃α​(1−e−β)2ϵ​∫D​z0​2​H​(−r​z0q0−r2)ℋ​(q0​z0,1−q0)​∫D​z1​G​(q0​z0+1−q0​z1ϵ)2ℋ​(q0​z0+1−q0​z1,ϵ)\displaystyle\simeq\alpha\frac{(1-e^{-\beta})^{2}}{\epsilon}\int Dz_{0}\,\frac{2H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}},{\sqrt{1-q_{0}}}\right)}\int Dz_{1}\frac{G\left(\frac{\sqrt{q_{0}}z_{0}+\sqrt{1-q_{0}}z_{1}}{\sqrt{\epsilon}}\right)^{2}}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}+\sqrt{1-q_{0}}z_{1}},{\sqrt{\epsilon}}\right)}≃α​(1−e−β)2ϵ​∫D​z0​2​H​(−r​z0q0−r2)ℋ​(q0​z0,1−q0)​ϵ1−q0​G​(q0​z01−q0)​∫𝑑u​G​(u)2ℋ​(u,1)\displaystyle\simeq\alpha\frac{(1-e^{-\beta})^{2}}{\epsilon}\int Dz_{0}\,\frac{2H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}},{\sqrt{1-q_{0}}}\right)}\frac{\sqrt{\epsilon}}{\sqrt{1-q_{0}}}G\left(\frac{\sqrt{q_{0}}z_{0}}{\sqrt{1-q_{0}}}\right)\int du\frac{G\left(u\right)^{2}}{\mathcal{H}\left(u,1\right)}=C​(q0,r,α,β)ϵ,\displaystyle=\frac{C(q_{0},r,\alpha,\beta)}{\sqrt{\epsilon}}\,,

whereC​(q0,r,α,β)=α​(1−e−β)21−q0​∫D​z0​2​H​(−r​z0q0−r2)​G​(q0​z01−q0)ℋ​(q0​z0,1−q0)​∫𝑑u​G​(u)2ℋ​(u,1).C(q_{0},r,\alpha,\beta)=\alpha\,\frac{(1-e^{-\beta})^{2}}{\sqrt{1-q_{0}}}\int Dz_{0}\,\frac{2H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)G\left(\frac{\sqrt{q_{0}}z_{0}}{\sqrt{1-q_{0}}}\right)}{\mathcal{H}\left({\sqrt{q_{0}}z_{0}},{\sqrt{1-q_{0}}}\right)}\,\int du\frac{G\left(u\right)^{2}}{\mathcal{H}\left(u,1\right)}\,.(61)

Notice thatC​(q0,r,α,β)>0C(q_{0},r,\alpha,\beta)>0whenβ>0\beta>0and 0 ifβ=0\beta=0. For smallβ\beta, we can useℋ​(x,y)−1≃1+O​(β)\mathcal{H}(x,y)^{-1}\simeq 1+O(\beta), so thatC​(q0,r,α,β)=c​(α,q0)​β2+O​(β3).C(q_{0},r,\alpha,\beta)=c(\alpha,q_{0})\,\beta^{2}+O\left(\beta^{3}\right)\,.(62)

Then, we consider the saddle point equation (57). Rewrite it as a self-consistent equation:q1=f​(q^1​(q1)),\displaystyle q_{1}=f(\hat{q}_{1}(q_{1}))\,,(63)

wheref​(q^1)f(\hat{q}_{1})is given by the right-hand-side of (57):f​(q^1)\displaystyle f(\hat{q}_{1})=e−q^1−q^02​∫D​z0​D​z1​cosh⁡(q^0​z0+q^1−q^0​z1+r^)−[cosh⁡(q^0​z0+q^1−q^0​z1+r^)]−1cosh⁡(q^0​z0+r^)\displaystyle=e^{-\frac{\hat{q}_{1}-\hat{q}_{0}}{2}}\int Dz_{0}Dz_{1}\frac{\cosh\left(\sqrt{\hat{q}_{0}}z_{0}+\sqrt{\hat{q}_{1}-\hat{q}_{0}}z_{1}+\hat{r}\right)-[\cosh\left(\sqrt{\hat{q}_{0}}z_{0}+\sqrt{\hat{q}_{1}-\hat{q}_{0}}z_{1}+\hat{r}\right)]^{-1}}{\cosh(\sqrt{\hat{q}_{0}}z_{0}+\hat{r})}

andq^1​(q1)\hat{q}_{1}(q_{1})is given by (59). We want to show thatf​(q^1​(q1))→1f(\hat{q}_{1}(q_{1}))\to 1in the limitq1→1q_{1}\to 1, satisfying a consistency relation. We have:f​(Cϵ)≃e−q^1−q^02​∫D​ucosh⁡(q^0​u+r^)​[eq^1−q^02​cosh⁡(q^0​u+r^)−π2​ϵ1/4C1/2+o​(ϵ3/4C3/2)]≃1−π2​e−C2​ϵ​ϵ1/4C1/2,\begin{split}f\left(\frac{C}{\sqrt{\epsilon}}\right)&\simeq e^{-\frac{\hat{q}_{1}-\hat{q}_{0}}{2}}\int\frac{Du}{\cosh(\sqrt{\hat{q}_{0}}u+\hat{r})}\,\left[e^{\frac{\hat{q}_{1}-\hat{q}_{0}}{2}}\cosh(\sqrt{\hat{q}_{0}}u+\hat{r})-\sqrt{\frac{\pi}{2}}\frac{{\epsilon}^{1/4}}{C^{1/2}}+o\left(\frac{\epsilon^{3/4}}{C^{3/2}}\right)\right]\\
&\simeq 1-\sqrt{\frac{\pi}{2}}e^{-\frac{C}{2\sqrt{\epsilon}}}\frac{\epsilon^{1/4}}{C^{1/2}}\,,\end{split}(64)

having used∫−∞∞dxcosh(x)−1=π\int_{-\infty}^{\infty}dx\,\cosh(x)^{-1}=\pi. Since forϵ→0\epsilon\to 0one hasf→1f\to 1whenC>0C>0, we have shown that the frozen solutionq1=1q_{1}=1is always a solution for anyβ>0\beta>0. Soβd=0\beta_{d}=0in the thermodynamic limit.
Finally, one can also compute the behavior ofβd\beta_{d}asϵ→0\epsilon\to 0, by solving (63) for smallβ\beta:1−ϵ=1−π2​e−c​β22​ϵ​ϵ1/4c1/2​β1-\epsilon=1-\sqrt{\frac{\pi}{2}}e^{-\frac{c\beta^{2}}{2\sqrt{\epsilon}}}\frac{\epsilon^{1/4}}{c^{1/2}\beta}

In the smallϵ\epsilonlimit,βd\beta_{d}vanishes as:βd∼ϵ1/4​ln⁡(1ϵ)\beta_{d}\sim\epsilon^{1/4}\sqrt{\ln\left(\frac{1}{\epsilon}\right)}(65)

Settingϵ≃1N\epsilon\simeq\frac{1}{N}(60), this heuristically identifies the scaling ofβd\beta_{d}with N:βd∼ln⁡(N)N1/4.\beta_{d}\sim\frac{\sqrt{\ln\left(N\right)}}{N^{1/4}}\,.(66)

We point out that this result does not depend onrrandr^\hat{r}, and that the exact same scaling is found for the SBP, where we have a further simplification due to the fact thatq0=q^0=0q_{0}=\hat{q}_{0}=0.

## B.2General criterion for freezing

The previous computation for the ABP shows that the existence of the frozen solution is controlled by the behaviour of the energetic saddle-point equation (58):q^1=α​∫D​z0​2​H​(−r​z0q0−r2)ℋ​(q0​z0,1−q0)​∫D​z1​[∂xℋ​(q0​z0+q1−q0​z1,1−q1)]2ℋ​(q0​z0+q1−q0​z1,1−q1)=α​∫D​z0​2​H​(−r​z0q0−r2)ℋ​(q0​z0,1−q0)​∫d​xq1−q0​G​(x−q0​z0q1−q0)​[∂xℋ​(x,1−q1)]2ℋ​(x,1−q1)\begin{split}\hat{q}_{1}&=\alpha\int Dz_{0}\,\frac{2H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)}{\mathcal{H}\left(\sqrt{q_{0}}z_{0},\sqrt{1-q_{0}}\right)}\int Dz_{1}\,\frac{\left[\partial_{x}\mathcal{H}\left(\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1},\sqrt{1-q_{1}}\right)\right]^{2}}{\mathcal{H}\left(\sqrt{q_{0}}z_{0}+\sqrt{q_{1}-q_{0}}z_{1},\sqrt{1-q_{1}}\right)}\\
&=\alpha\int Dz_{0}\,\frac{2H\left(-\frac{rz_{0}}{\sqrt{q_{0}-r^{2}}}\right)}{\mathcal{H}\left(\sqrt{q_{0}}z_{0},\sqrt{1-q_{0}}\right)}\int\frac{dx}{\sqrt{q_{1}-q_{0}}}\,G\left(\frac{x-\sqrt{q_{0}}z_{0}}{\sqrt{q_{1}-q_{0}}}\right)\frac{\left[\partial_{x}\mathcal{H}\left(x,\sqrt{1-q_{1}}\right)\right]^{2}}{\mathcal{H}\left(x,\sqrt{1-q_{1}}\right)}\end{split}(67)

The entropic saddle-point equation, instead, is independent of the particular energetic factor. It can be written asq1=f​(q^1),q_{1}=f(\hat{q}_{1}),(68)

and, forq^1→∞\hat{q}_{1}\to\infty, one has as shown in (64)f​(q^1)=1−π2​q^1−1/2​e−q^1/2​[1+o​(1)],f(\hat{q}_{1})=1-\sqrt{\frac{\pi}{2}}\,\hat{q}_{1}^{-1/2}e^{-\hat{q}_{1}/2}\left[1+o(1)\right],(69)

Therefore the frozen solutionq1=1q_{1}=1can be obtained only if the energetic equation sendsq^1\hat{q}_{1}to infinity whenq1→1q_{1}\to 1. The singularity of (67) is entirely determined by the small-yybehaviour of[∂xℋ​(x,y)]2ℋ​(x,y),y=1−q1\frac{\left[\partial_{x}\mathcal{H}(x,y)\right]^{2}}{\mathcal{H}(x,y)},\qquad y=\sqrt{1-q_{1}}(70)

In order to make this statement more explicit, let us go back to the
definition of the kernelℋ​(x,y)=∫D​z​𝒦​(x+y​z),\mathcal{H}(x,y)=\int Dz\,\mathcal{K}(x+yz),(71)

where𝒦\mathcal{K}is the single-pattern Boltzmann factor, Cf. Eqs. (7), (10). Thusℋ​(x,y)\mathcal{H}(x,y)is a Gaussian smoothing of𝒦\mathcal{K}on a
scaleyy. If𝒦\mathcal{K}is smooth around a pointxx, then∂xℋ​(x,y)\partial_{x}\mathcal{H}(x,y)remains finite asy→0y\to 0. Singular
contributions can only arise close to points where𝒦\mathcal{K}is
non-smooth. This usually happens near the decision boundaries of the constraints.

Letbbbe such a decision boundary point. In thexxintegral appearing in
(67), the Gaussian density multiplying(∂xℋ)2/ℋ(\partial_{x}\mathcal{H})^{2}/\mathcal{H}is smooth on the scaleyy.
Therefore, close tobb, one can setx=b+y​u,d​x=y​d​u.x=b+yu,\qquad dx=y\,du.(72)

The whole question is then
reduced to the scaling withyyof theboundary layerterm:ℬ𝒦​(b,y)≡y​∫𝑑u​[∂xℋ​(b+y​u,y)]2ℋ​(b+y​u,y).\mathcal{B}_{\mathcal{K}}(b,y)\equiv y\int du\,\frac{\left[\partial_{x}\mathcal{H}(b+yu,y)\right]^{2}}{\mathcal{H}(b+yu,y)}.(73)

If this quantity diverges asy→0y\to 0, thenq^1→∞\hat{q}_{1}\to\infty. Since the
entropic equation satisfies (69), this implies that
the frozen solutionq1=1q_{1}=1is present. If instead
(73) stays finite, or vanishes, the
energetic equation does not forceq^1→∞\hat{q}_{1}\to\infty, and the frozen solution atq1=1q_{1}=1is absent.

We now discuss the possible behaviors of𝒦\mathcal{K}at a boundary.
- •

Jump discontinuity.Suppose that, close tobb, the Boltzmann factor has a finite jump:𝒦​(s)=𝒦−+Δ​𝒦​Θ​(s−b),Δ​𝒦≠0.\mathcal{K}(s)=\mathcal{K}_{-}+\Delta\mathcal{K}\,\Theta(s-b),\qquad\Delta\mathcal{K}\neq 0.(74)

This is the case for both (7) and (10) forb=0b=0andb=±κb=\pm\kapparespectively.
Then, using (71) and settingx=b+y​ux=b+yu,ℋ​(b+y​u,y)=𝒦−+Δ​𝒦​∫D​z​Θ​(u+z).\mathcal{H}(b+yu,y)=\mathcal{K}_{-}+\Delta\mathcal{K}\int Dz\,\Theta(u+z).(75)

Thusℋ​(b+y​u,y)\mathcal{H}(b+yu,y)is of order one inside the boundary layer.
On the other hand,∂xℋ​(b+y​u,y)=Δ​𝒦​∫D​z​δ​(b+y​u+y​z−b)=Δ​𝒦y​G​(u).\partial_{x}\mathcal{H}(b+yu,y)=\Delta\mathcal{K}\int Dz\,\delta(b+yu+yz-b)=\frac{\Delta\mathcal{K}}{y}\,G(u).(76)

Thereforeℬ𝒦​(b,y)≃(Δ​𝒦)2y​∫𝑑u​G​(u)2𝒦−+Δ​𝒦​∫D​z​Θ​(u+z).\mathcal{B}_{\mathcal{K}}(b,y)\simeq\frac{(\Delta\mathcal{K})^{2}}{y}\int du\,\frac{G(u)^{2}}{\mathcal{K}_{-}+\Delta\mathcal{K}\int Dz\,\Theta(u+z)}.(77)

Hence a jump produces the divergenceℬ𝒦​(b,y)=O​(1y)=O​(11−q1)\mathcal{B}_{\mathcal{K}}(b,y)=O\left(\frac{1}{y}\right)=O\left(\frac{1}{\sqrt{1-q_{1}}}\right)(78)

This is precisely the mechanism found in the ABP/SBP computation done in the previous subsection. Indeed for the ABP:𝒦−=e−β\mathcal{K}_{-}=e^{-\beta},Δ​𝒦=1−e−β\Delta\mathcal{K}=1-e^{-\beta}andb=0b=0.
- •

Vanishing power at the boundary.Suppose instead that the Boltzmann factor vanishes continuously at the boundary as𝒦​(s)≃A​(s−b)γ​Θ​(s−b),A,γ>0.\mathcal{K}(s)\simeq A(s-b)^{\gamma}\Theta(s-b),\qquad A,\gamma>0.(79)

see the right panel of Figure1. Thenℋ​(b+y​u,y)\displaystyle\mathcal{H}(b+yu,y)=∫D​z​𝒦​(b+y​(u+z))≃A​yγ​∫D​z​(u+z)γ​Θ​(u+z)≡A​yγ​Fγ​(u)\displaystyle=\int Dz\,\mathcal{K}(b+y(u+z))\simeq Ay^{\gamma}\int Dz\,(u+z)^{\gamma}\Theta(u+z)\equiv Ay^{\gamma}F_{\gamma}(u)(80)

whereFγ​(u)=∫D​z​(u+z)γ​Θ​(u+z)F_{\gamma}(u)=\int Dz\,(u+z)^{\gamma}\Theta(u+z).
We therefore have∂xℋ​(b+y​u,y)≃A​yγ−1​Fγ′​(u).\partial_{x}\mathcal{H}(b+yu,y)\simeq Ay^{\gamma-1}F_{\gamma}^{\prime}(u).(81)

Thereforeℬ𝒦​(b,y)≃yγ−1​∫𝑑u​Fγ′​(u)2Fγ​(u).\mathcal{B}_{\mathcal{K}}(b,y)\simeq y^{\gamma-1}\int du\,\frac{F_{\gamma}^{\prime}(u)^{2}}{F_{\gamma}(u)}.(82)

Consequently, ifγ<1\gamma<1,q^1\hat{q}_{1}diverges and one has the frozen solutionq1=1q_{1}=1, whereas ifγ>1\gamma>1the frozen solution is lost. The caseγ=1\gamma=1is marginal. This criterion also explains why the logarithmic potential studied inStraziotaet al.(2025), which falls in this category, can remove freezing.
- •

Continuous non-zero value at the boundary.Another possibility for the behavior of the kernel near the boundary point is the following𝒦​(s)=𝒦0+A​(b−s)γ​Θ​(b−s),𝒦0>0.\mathcal{K}(s)=\mathcal{K}_{0}+A(b-s)^{\gamma}\Theta(b-s)\,,\qquad\mathcal{K}_{0}>0.(83)

In this caseℋ​(b+y​u,y)=𝒦0+O​(yγ),\mathcal{H}(b+yu,y)=\mathcal{K}_{0}+O(y^{\gamma}),(84)

while∂xℋ​(b+y​u,y)=O​(yγ−1).\partial_{x}\mathcal{H}(b+yu,y)=O(y^{\gamma-1}).(85)

Henceℬ𝒦​(b,y)∼y2​γ−1.\mathcal{B}_{\mathcal{K}}(b,y)\sim y^{2\gamma-1}.(86)

Therefore, for ordinary integer powersγ>1/2\gamma>1/2, there is no divergent boundary contribution. This category includes the single pattern Gibbs weight𝒦​(s)=e−β​(−s)γ​Θ​(−s)=e−β​(−s)γ+(1−e−β​(−s)γ)​Θ​(s)\mathcal{K}(s)=e^{-\beta(-s)^{\gamma}\Theta(-s)}=e^{-\beta(-s)^{\gamma}}+\left(1-e^{-\beta(-s)^{\gamma}}\right)\Theta(s)(87)

studied by HornerHorner (1992)and byCataniaet al.(2024), who focused on positive integers values ofγ\gamma; see also the left panel of Figure1for a plot. At finiteβ\betathis factor is continuous ats=0s=0:𝒦​(0−)=𝒦​(0+)=1.\mathcal{K}(0^{-})=\mathcal{K}(0^{+})=1.(88)

Close to the boundary,𝒦​(s)=1−β​(−s)γ​Θ​(−s)+⋯.\mathcal{K}(s)=1-\beta(-s)^{\gamma}\Theta(-s)+\cdots.(89)

This is of the form (83) with𝒦0=1\mathcal{K}_{0}=1,A=−βA=-\beta.
For the usual integer casesγ≥1\gamma\geq 1, the boundary contribution does not diverge. Hence,
at finiteβ\beta, the energetic saddle equation does not forceq^1→∞\hat{q}_{1}\to\inftyasq1→1q_{1}\to 1, and the frozen solution
disappears. A dynamical transition may still occur, but at a finite temperature and withq1<1q_{1}<1at the transition. At zero temperature, however, as𝒦​(s)→Θ​(s)\mathcal{K}(s)\to\Theta(s), the jump is restored, and the freezing mechanism reappears.

## Appendix CDetail of the message passing algorithms

In this section, we provide details of the message passing algorithm used in the main text to search for minimal error configurations in the ABP. We start from a short review of the AMP algorithm, then we move to the description of AMP+reinforcement.

## C.1Approximate Message Passing

Consider the Gibbs measure induced by the partition function (5):p𝒟​(𝒘)=∏μ=1P𝒦​(sμ​(𝒘))Z𝒟.\displaystyle p_{\mathcal{D}}\left(\bm{w}\right)=\frac{\prod_{\mu=1}^{P}\mathcal{K}\left(s^{\mu}(\bm{w})\right)}{Z_{\mathcal{D}}}\,.(90)

The Approximate Message Passing (AMP) algorithm provides an iterative approximation to the local marginals of the measure (90).
AMP is obtained from the Belief Propagation (BP) equations using a Gaussian approximation which parametrizes the one site marginalsmi​(wi)=∑𝒘\ip𝒟​(𝒘)m_{i}(w_{i})=\sum_{\bm{w}_{\backslash i}}\,p_{\mathcal{D}}(\bm{w})in terms of its meanaia_{i}and variancebib_{i}. Being the weights binary in our setting, the one site meanai\displaystyle a_{i}=∑wi=±1mi​(wi)​wi≡⟨wi⟩β\displaystyle=\sum_{w_{i}=\pm 1}\,m_{i}(w_{i})\,w_{i}\equiv\langle w_{i}\rangle_{\beta}(91)

completely determines also the variance of the one site marginal viabi=1−ai2b_{i}=1-a_{i}^{2}. Starting att=0t=0from a random guess for the one site marginalsait=0a_{i}^{t=0}and initializing randomly thePPdimensional vectorgμt=0g_{\mu}^{t=0}the AMP algorithm consists in the following update equations:Vμt\displaystyle V_{\mu}^{t}=∑i=1N(xiμ)2N​[1−(ait−1)2],\displaystyle=\sum_{i=1}^{N}\frac{(x_{i}^{\mu})^{2}}{N}\left[1-\left(a_{i}^{t-1}\right)^{2}\right]\,,(92a)Mμt\displaystyle M_{\mu}^{t}=∑i=1NxiμN​ait−1−Vμt​gμt−1,\displaystyle=\sum_{i=1}^{N}\frac{x_{i}^{\mu}}{\sqrt{N}}a_{i}^{t-1}-V_{\mu}^{t}g_{\mu}^{t-1}\,,(92b)gμt\displaystyle g_{\mu}^{t}=gE​(yμ,Mμt,Vμt;β),\displaystyle=g_{E}(y^{\mu},M_{\mu}^{t},V_{\mu}^{t};\beta)\,,(92c)hit\displaystyle h_{i}^{t}=∑μ=1PxiμN​gE​(yμ,Mμt,Vμt;β)−ait−1​∑μ=1P(xiμ)2N​∂MgE​(yμ,Mμt,Vμt;β),\displaystyle=\sum_{\mu=1}^{P}\frac{x_{i}^{\mu}}{\sqrt{N}}g_{E}(y^{\mu},M_{\mu}^{t},V_{\mu}^{t};\beta)-a_{i}^{t-1}\sum_{\mu=1}^{P}\frac{(x_{i}^{\mu})^{2}}{N}\partial_{M}g_{E}(y^{\mu},M_{\mu}^{t},V_{\mu}^{t};\beta)\,,(92d)ait\displaystyle a_{i}^{t}=tanh⁡(hit),\displaystyle=\tanh(h_{i}^{t})\,,(92e)

which are iterated fort=1,…,tmaxt=1,\dots,t_{\rm max}or until convergence. The functiongEg_{E}is called theenergetic channeland depends in general on the detail of the model. For example in the case of ABP with error counting loss function it reads:gE​(y,M,V;β)=∂Mlog⁡[e−β+(1−e−β)​H​(−y​MV)],g_{E}(y,M,V;\beta)=\partial_{M}\log\left[e^{-\beta}+\left(1-e^{-\beta}\right)H\left(-\frac{yM}{\sqrt{V}}\right)\right],(93)

where we remind thatH​(x)≡12​Erfc​(x2)H(x)\equiv\frac{1}{2}\mathrm{Erfc}\left(\frac{x}{\sqrt{2}}\right). When AMP converges, it can be used to compute on a single sample other observables that are computed via the replica method. For example the overlap between two students sampled from (90) can be written in terms of the one-site magnetizations as:qN=1N​∑i=1N⟨wi⟩β​⟨wi⟩β=1N​∑i=1Nai2.q_{N}=\frac{1}{N}\sum_{i=1}^{N}\langle w_{i}\rangle_{\beta}\langle w_{i}\rangle_{\beta}=\frac{1}{N}\sum_{i=1}^{N}a_{i}^{2}\,.(94)

In the largeNNlimit, this can be proved to converge to the replica method RS order parameterqqMézard and Montanari (2009).
As a check of the reliability of our algorithm at finite temperature we confirmed this by running a few experiments, as reported in Figure10.Figure 10:The AMP algorithm was tested at different values of temperature, corresponding toβ=∞\beta=\infty,β=6.0\beta=6.0,β=3.0\beta=3.0(left to right). The plots present the typical RS overlapqqas a function of the constraint densityα\alpha: experimental points (blue) were obtained withN=1000N=1000and averaged over2020samples, and they agree with the theoretical RS curve (red).Algorithm 2One AMP+reinforcement updatefunctionrAMPstep(𝒉t−1,𝒂t−1,𝒈t−1;ρt−1,β\bm{h}^{t-1},\bm{a}^{t-1},\bm{g}^{t-1};\rho_{t-1},\beta)Compute the variancesVμt←∑i=1N(xiμ)2N​[1−(ait−1)2],μ=1,…,P.V_{\mu}^{t}\leftarrow\sum_{i=1}^{N}\frac{(x_{i}^{\mu})^{2}}{N}\left[1-\left(a_{i}^{t-1}\right)^{2}\right],\qquad\mu=1,\ldots,P.(95)Compute the Onsager-corrected meansMμt←∑i=1NxiμN​ait−1−Vμt​gμt−1,μ=1,…,P.M_{\mu}^{t}\leftarrow\sum_{i=1}^{N}\frac{x_{i}^{\mu}}{\sqrt{N}}a_{i}^{t-1}-V_{\mu}^{t}g_{\mu}^{t-1},\qquad\mu=1,\ldots,P.(96)Update the energetic messagesgμt←gE​(yμ,Mμt,Vμt;β),μ=1,…,P.g_{\mu}^{t}\leftarrow g_{E}(y^{\mu},M_{\mu}^{t},V_{\mu}^{t};\beta),\qquad\mu=1,\ldots,P.(97)Update the fieldshit←\displaystyle h_{i}^{t}\leftarrow∑μ=1PxiμN​gμt−ait−1​∑μ=1P(xiμ)2N​∂MgE​(yμ,Mμt,Vμt;β)+ρt−1​hit−1,i=1,…,N.\displaystyle\sum_{\mu=1}^{P}\frac{x_{i}^{\mu}}{\sqrt{N}}g_{\mu}^{t}-a_{i}^{t-1}\sum_{\mu=1}^{P}\frac{(x_{i}^{\mu})^{2}}{N}\partial_{M}g_{E}(y^{\mu},M_{\mu}^{t},V_{\mu}^{t};\beta)+\rho_{t-1}h_{i}^{t-1},\qquad i=1,\ldots,N.(98)Update the magnetizationsait←tanh⁡(hit),i=1,…,N.a_{i}^{t}\leftarrow\tanh(h_{i}^{t}),\qquad i=1,\ldots,N.(99)return(𝒉t,𝒂t,𝒈t)(\bm{h}^{t},\bm{a}^{t},\bm{g}^{t}).endfunction

## C.2AMP + reinforcement (rAMP)Figure 11:ABP, storage setting. Training-error trajectories of rAMP forN=1000N=1000,α=0.9\alpha=0.9, reinforcement rateρ=10−4\rho=10^{-4}, and different inverse temperaturesβ\beta. All curves use the same dataset and initialization. The dashed horizontal line marks the target training errorϵtarg=0.025\epsilon^{\mathrm{targ}}=0.025. Among the values considered, onlyβ=4\beta=4reaches the target within10410^{4}iterations.

The reinforcement AMP algorithm (rAMP)Braunstein and Zecchina (2006)is a modification of the AMP iteration designed to turn the soft marginal information
computed by AMP into an actual binary configuration. Standard AMP estimates the local magnetizationsai≃⟨wi⟩a_{i}\simeq\langle w_{i}\rangleof the Gibbs measure, but these magnetizations need not be close to±1\pm 1. The role of reinforcement is to progressively polarize the local fields, so that the magnetizations become closer to the vertices of the hypercube and the configuration given bywi=sign⁡(ai)w_{i}=\operatorname{sign}(a_{i})(100)

can be used as a candidate low-error assignment. Operationally, reinforcement is implemented by adding to the AMP field
update a term proportional to the previous local field,hit=hi,AMPt+ρt−1​hit−1,h_{i}^{t}=h_{i,\mathrm{AMP}}^{t}+\rho_{t-1}h_{i}^{t-1},(101)

wherehi,AMPth_{i,\mathrm{AMP}}^{t}denotes the standard AMP update, see (92d). The parameterρt\rho_{t}is increased during the dynamics according to a reinforcement schedule. In the experiments reported in the main text we useρt=1−(1−ρ)t,\rho_{t}=1-(1-\rho)^{t},(102)

whereρ\rhocontrols the speed at which the reinforcement is switched on. For smallρ\rhoand early times,ρt≃ρ​t\rho_{t}\simeq\rho t, while at longer times the reinforcement strength approaches one. Settingρ=0\rho=0givesρt=0\rho_{t}=0for alltt, and one recovers the standard AMP iteration.

The explicit one-step rAMP update is given in Algorithm2. The fixed-temperature reinforced dynamics, obtained by iterating this update at fixedβ\beta, is summarized in Algorithm1in the main text.

We show in Figure11the behavior of the rAMP algorithm for fixed reinforcement rate and several values ofβ\betaforα=0.9\alpha=0.9andN=1000N=1000in the storage setting of the ABP. Notice that theβ=∞\beta=\inftytrajectory stops before reaching the maximum number of iterations, because the rAMP produces diverging updates. This is expected as forα>0.784\alpha>0.784it is hard to find solutions, and in addition forα\alphagreater than the SAT/UNSAT thresholdαS=0.833\alpha_{S}=0.833solutions do not exist at all in the largeNNlimitKrauth and Mézard (1989). Decreasing the value ofβ\betaallows to search for configurations having a certain positive value of the training error. Moreover, the resulting AMP updates are less singular and the local marginals are initially less polarized, which makes the subsequent reinforcement dynamics more stable. If one continues decreasingβ\betabut maintaining fixed the reinforcement rateρ\rho, the trajectory tends to stabilize at a higher training error value before exploring lower training error configurations at a larger number of iterations. The figure therefore shows that for each fixed reinforcement rate, there exists an optimal value ofβ\betathat allows to probe the lowest achievable training error configurations.

We also tested a temperature-annealing schedule. However, this introduces some additional hyperparameters: the starting temperatureβ0\beta_{0}, the temperature increment or cooling rateΔ​β\Delta\betaand the frequency of incrementΔit\Delta_{\rm it}. Those new hyperparameters need to be tuned optimally together with the reinforcement schedule. Overall, we found no substantial improvement from incorporating temperature annealing.

## Appendix DAdditional figuresFigure 12:Generalization error as a function of the overlapq1q_{1}between the clones, form=2m=2andm=3m=3, andβ=∞\beta=\infty. The left picture corresponds to the easy phase of Figure6(α=1.0\alpha=1.0), while the right figure to the hard phase (α=1.3\alpha=1.3) and all its points are characterized by a negative entropy. Clusters ofm=3m=3clones can achieve a better generalization, if the hyperparameterq1q_{1}is tuned conveniently.Figure 13:Left: the picture shows the entropy of the RS solution, as a function of the teacher-student overlapr​(𝒘,𝒘⋆)r(\bm{w},\bm{w}^{\star}), in the hard phase (α=1.3\alpha=1.3). The entropy increases with temperature, as expected. The same happens with solution of the33-cloned system: the right picture shows the generalization error of a solution in the cluster, as a function of the mutual overlapq1q_{1}, similarly to Figure5. The dashed parts of the curve signal a negative entropy.

## 


- 


Major funding support from
